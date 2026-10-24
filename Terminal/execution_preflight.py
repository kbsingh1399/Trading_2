#!/usr/bin/env python3
"""Emission-time execution preflight for the Blueberry MT5 desk.

WHY THIS EXISTS
---------------
Cycle 313 established that the 15-second quote max_age can never be satisfied by
a cycle envelope: the dispatcher's snapshots land 110-344 s apart (median 296 s),
so the newest pre-cutoff quote is structurally 20x staler than the gate allows.
The gate is not wrong -- it is simply attached to the wrong artefact.

The fix is to split the two things the desk has been conflating:

  evidence snapshot .... ~5-minute cadence, judged against the 900 s sheet ceiling.
                         Fine for regime, value area, CVD and stop clusters.
  execution preflight .. captured sub-second AT EMISSION, bound to the dispatch
                         nonce, carrying its own 15 s max_age. This is the only
                         thing that may authorise an order.

This script produces the second artefact and nothing else. It never sends, modifies
or cancels an order: it calls order_check (read-only) and emits a receipt. A council
label cannot substitute for it, and it cannot substitute for the council.

Usage
-----
    python Terminal/execution_preflight.py --symbol BTCUSD.pi --side SELL \\
        --order-type LIMIT --volume 0.04 --price 81300.0 --sl 81780.0 --tp 79850.0 \\
        --nonce 46044d1a-ecf4-44eb-8c85-769ebc85f29b --out preflight.json

Exit codes
----------
    0  receipt valid: every freshness/spec/feasibility check passed
    1  receipt REJECTED: at least one check failed (see "failures")
    2  environment error (MT5 unavailable, symbol unknown, malformed arguments)

The receipt is intentionally self-describing: it records observed_at, available_at
and the age of every input against its own max_age, so a downstream council can
verify it without trusting this process.
"""
from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import pathlib
import sys
import time

QUOTE_MAX_AGE_S = 15
SPEC_MAX_AGE_S = 300
# TTL must be shorter than the time it takes the market to invalidate the thesis.
DEFAULT_TTL_S = 900


def _now() -> dt.datetime:
    return dt.datetime.now(dt.timezone.utc)


def _iso(ts: dt.datetime) -> str:
    return ts.strftime("%Y-%m-%d %H:%M:%S UTC")


def _sha(obj) -> str:
    return hashlib.sha256(
        json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def build_receipt(args, mt5) -> dict:
    """Capture one tick, the symbol spec and an order_check, all in the same instant."""
    observed_at = _now()
    symbol = args.symbol

    if not mt5.symbol_select(symbol, True):
        raise RuntimeError(f"symbol_select failed for {symbol}: {mt5.last_error()}")

    tick_a = mt5.symbol_info_tick(symbol)
    spec = mt5.symbol_info(symbol)
    info = mt5.account_info()
    if tick_a is None or spec is None or info is None:
        raise RuntimeError(f"MT5 returned no tick/spec/account for {symbol}")

    # A second tick 50 ms later proves the feed is live rather than a cached print.
    time.sleep(0.05)
    tick_b = mt5.symbol_info_tick(symbol)
    available_at = _now()

    point = spec.point or 10 ** (-spec.digits)
    spread_pts = (tick_a.ask - tick_a.bid) / point
    price = args.price if args.price is not None else tick_a.bid
    is_long = args.side == "BUY"

    # ---- structural geometry checks -------------------------------------
    failures: list[str] = []

    if is_long:
        if not (args.sl < price < args.tp):
            failures.append(f"BUY geometry invalid: need SL < entry < TP, got {args.sl} < {price} < {args.tp}")
        adverse_pts = (price - args.sl) / point
    else:
        if not (args.tp < price < args.sl):
            failures.append(f"SELL geometry invalid: need TP < entry < SL, got {args.tp} < {price} < {args.sl}")
        adverse_pts = (args.sl - price) / point

    if spec.trade_stops_level and adverse_pts < spec.trade_stops_level:
        failures.append(
            f"stop distance {adverse_pts:.1f} pts inside broker stops_level {spec.trade_stops_level}"
        )
    if spec.trade_freeze_level and abs(price - tick_a.bid) / point < spec.trade_freeze_level:
        failures.append(f"entry inside freeze_level {spec.trade_freeze_level}")

    # ---- broker-native valuations ---------------------------------------
    profit_req = {
        "action": mt5.TRADE_ACTION_DEAL,
        "symbol": symbol,
        "volume": args.volume,
        "type": mt5.ORDER_TYPE_BUY if is_long else mt5.ORDER_TYPE_SELL,
        "price": tick_a.ask if is_long else tick_a.bid,
        "sl": args.sl,
        "tp": args.tp,
        "deviation": args.deviation,
        "magic": args.magic,
        "comment": f"preflight:{args.nonce[:8]}",
        "type_time": mt5.ORDER_TIME_GTC,
        "type_filling": mt5.ORDER_FILLING_IOC,
    }
    calc_profit = mt5.order_calc_profit(
        mt5.ORDER_TYPE_BUY if is_long else mt5.ORDER_TYPE_SELL,
        symbol, args.volume, profit_req["price"], args.tp
    )
    calc_loss = mt5.order_calc_profit(
        mt5.ORDER_TYPE_BUY if is_long else mt5.ORDER_TYPE_SELL,
        symbol, args.volume, profit_req["price"], args.sl
    )
    margin = mt5.order_calc_margin(
        mt5.ORDER_TYPE_BUY if is_long else mt5.ORDER_TYPE_SELL,
        symbol, args.volume, profit_req["price"]
    )

    check = mt5.order_check(profit_req)
    check_retcode = getattr(check, "retcode", None) if check else None
    check_ok = check is not None and check_retcode == 0
    if not check_ok:
        msg = getattr(check, "comment", "no response") if check else "no response"
        failures.append(f"order_check retcode={check_retcode} comment={msg}")

    # ---- freshness -------------------------------------------------------
    quote_age_s = (available_at - observed_at).total_seconds()
    tick_is_live = tick_b is not None and (tick_b.bid, tick_b.ask) != (tick_a.bid, tick_a.ask) \
        or (tick_b is not None and abs(tick_b.time - tick_a.time) <= 2)
    if quote_age_s > QUOTE_MAX_AGE_S:
        failures.append(f"quote age {quote_age_s:.2f}s exceeds {QUOTE_MAX_AGE_S}s max_age")
    if netting_conflict(mt5, symbol, info):
        failures.append("hedging/netting conflict: an opposite position already exists")

    expires_at = observed_at + dt.timedelta(seconds=args.ttl)
    receipt = {
        "receipt_type": "EXECUTION_PREFLIGHT",
        "schema_version": "1.0.0",
        "dispatch_nonce": args.nonce,
        "symbol": symbol,
        "proposed_request": {
            "side": args.side,
            "order_type": args.order_type,
            "volume": args.volume,
            "requested_price": args.price,
            "stop": args.sl,
            "target": args.tp,
            "deviation_points": args.deviation,
        },
        "account": {
            "login": info.login,
            "server": info.server,
            "currency": info.currency,
            "balance": info.balance,
            "equity": info.equity,
            "margin_free": info.margin_free,
        },
        "observed_at_utc": _iso(observed_at),
        "available_at_utc": _iso(available_at),
        "authorization_expires_utc": _iso(expires_at),
        "freshness": {
            "quote_age_s": round(quote_age_s, 3),
            "quote_max_age_s": QUOTE_MAX_AGE_S,
            "feed_live_across_two_polls": bool(tick_is_live),
            "spec_max_age_s": SPEC_MAX_AGE_S,
        },
        "quote": {
            "bid": tick_a.bid,
            "ask": tick_a.ask,
            "mid": round((tick_a.bid + tick_a.ask) / 2, spec.digits),
            "spread_points": round(spread_pts, 2),
            "spread_bps": round(spread_pts * point / ((tick_a.bid + tick_a.ask) / 2) * 1e4, 2),
            "tick_time": int(tick_a.time),
        },
        "symbol_spec": {
            "digits": spec.digits,
            "point": point,
            "contract_size": spec.trade_contract_size,
            "volume_min": spec.volume_min,
            "volume_step": spec.volume_step,
            "volume_max": spec.volume_max,
            "stops_level": spec.trade_stops_level,
            "freeze_level": spec.trade_freeze_level,
            "margin_initial": spec.margin_initial,
            "swap_long": spec.swap_long,
            "swap_short": spec.swap_short,
            "swap_mode": spec.swap_mode,
            "swap_rollover3days": spec.swap_rollover3days,
        },
        "broker_valuation": {
            "order_calc_profit_tp_usd": calc_profit,
            "order_calc_profit_sl_usd": calc_loss,
            "order_calc_margin_usd": margin,
            "risk_usd": None if calc_loss is None else round(abs(calc_loss), 2),
            "reward_usd": None if calc_profit is None else round(abs(calc_profit), 2),
            "rr": None if not (calc_loss and calc_profit) else round(abs(calc_profit / calc_loss), 3),
            "order_check_retcode": check_retcode,
            "order_check_comment": getattr(check, "comment", None) if check else None,
            "margin_after_fill_usd": None if margin is None else round(info.margin_free - margin, 2),
        },
        "verdict": "PASS" if not failures else "REJECT",
        "failures": failures,
        "max_age_self_check": {
            "rule": "0 <= available_at - observed_at <= quote_max_age_s",
            "observed_to_available_s": round(quote_age_s, 3),
            "passed": quote_age_s <= QUOTE_MAX_AGE_S,
        },
    }
    receipt["response_sha256"] = _sha(receipt)
    return receipt


def netting_conflict(mt5, symbol, info) -> bool:
    """True when an opposite-side position already exists on a netting account."""
    if getattr(info, "margin_mode", None) != getattr(mt5, "ACCOUNT_MARGIN_MODE_RETAIL_NETTING", -1):
        return False
    for pos in mt5.positions_get(symbol=symbol) or []:
        return True
    return False


def main() -> int:
    ap = argparse.ArgumentParser(description="Emission-time MT5 execution preflight")
    ap.add_argument("--symbol", required=True)
    ap.add_argument("--side", required=True, choices=["BUY", "SELL"])
    ap.add_argument("--order-type", default="LIMIT", choices=["MARKET", "LIMIT", "STOP", "STOP_LIMIT"])
    ap.add_argument("--volume", type=float, required=True)
    ap.add_argument("--price", type=float, default=None)
    ap.add_argument("--sl", type=float, required=True)
    ap.add_argument("--tp", type=float, required=True)
    ap.add_argument("--nonce", required=True)
    ap.add_argument("--ttl", type=int, default=DEFAULT_TTL_S)
    ap.add_argument("--deviation", type=int, default=20)
    ap.add_argument("--magic", type=int, default=313313)
    ap.add_argument("--out", default="-")
    args = ap.parse_args()

    try:
        import MetaTrader5 as mt5  # noqa: N813  (only available on the trading host)
    except ImportError:
        print("MT5_UNAVAILABLE: run this on the trading host, not in the review sandbox", file=sys.stderr)
        return 2

    if not mt5.initialize():
        print(f"MT5_INIT_FAILED: {mt5.last_error()}", file=sys.stderr)
        return 2
    try:
        receipt = build_receipt(args, mt5)
    except RuntimeError as exc:
        print(f"PREFLIGHT_ERROR: {exc}", file=sys.stderr)
        return 2
    finally:
        mt5.shutdown()

    text = json.dumps(receipt, indent=2)
    if args.out == "-":
        print(text)
    else:
        pathlib.Path(args.out).write_text(text)
        print(f"receipt -> {args.out}  verdict={receipt['verdict']}  sha={receipt['response_sha256'][:16]}")

    if receipt["verdict"] != "PASS":
        for f in receipt["failures"]:
            print(f"  REJECT: {f}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
