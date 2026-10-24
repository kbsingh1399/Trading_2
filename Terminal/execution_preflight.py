#!/usr/bin/env python3
"""
Terminal/execution_preflight.py
Sub-second live MT5 execution preflight receipt generator.

Bridges the structural gap between the 5-minute Excel evidence snapshot
and the 15-second execution quote gate:
1. Captures sub-second MT5 tick, spread, and symbol specifications.
2. Validates tick freshness (age <= 15.0s).
3. Recomputes exact broker-native profit/loss at SL and TP, and required margin.
4. Executes native mt5.order_check() to guarantee execution feasibility without sending live orders.
5. Emits a deterministic SHA-256 signed preflight receipt bound to the dispatch nonce.
"""

import argparse
import datetime
import hashlib
import json
import math
import pathlib
import sys

try:
    import MetaTrader5 as mt5
except ImportError:
    mt5 = None

ROOT = pathlib.Path(__file__).resolve().parents[1]
DEFAULT_OUT = ROOT / "Data" / "execution_preflight_receipt.json"
ACCOUNT_LOGIN = 5064568


def run_preflight(
    symbol: str,
    action: str,
    volume: float,
    price: float,
    sl: float,
    tp: float,
    dispatch_nonce: str = "",
    max_tick_age_s: float = 15.0,
) -> dict:
    observed_at = datetime.datetime.now(datetime.timezone.utc)

    if mt5 is None:
        return {
            "status": "FAIL",
            "error": "MT5_MODULE_UNAVAILABLE",
            "observed_at_utc": observed_at.isoformat(),
        }

    if not mt5.initialize():
        return {
            "status": "FAIL",
            "error": "MT5_INITIALIZE_FAILED",
            "observed_at_utc": observed_at.isoformat(),
        }

    try:
        acc = mt5.account_info()
        if acc is None or acc.login != ACCOUNT_LOGIN:
            return {
                "status": "FAIL",
                "error": "ACCOUNT_IDENTITY_MISMATCH",
                "login": acc.login if acc else None,
                "observed_at_utc": observed_at.isoformat(),
            }

        sym_info = mt5.symbol_info(symbol)
        if sym_info is None:
            return {
                "status": "FAIL",
                "error": f"SYMBOL_NOT_FOUND: {symbol}",
                "observed_at_utc": observed_at.isoformat(),
            }

        tick = mt5.symbol_info_tick(symbol)
        if tick is None or tick.time == 0:
            return {
                "status": "FAIL",
                "error": f"NO_TICK_AVAILABLE: {symbol}",
                "observed_at_utc": observed_at.isoformat(),
            }

        # Broker server time offset (Blueberry Markets SVG is UTC+3 = 10800s)
        # We auto-calibrate offset: round((tick.time - observed_at.timestamp()) / 3600.0) * 3600
        offset_hours = round((tick.time - observed_at.timestamp()) / 3600.0)
        broker_offset_s = offset_hours * 3600.0
        tick_utc_ts = (tick.time_msc / 1000.0 if hasattr(tick, "time_msc") and tick.time_msc > 0 else float(tick.time)) - broker_offset_s
        tick_dt = datetime.datetime.fromtimestamp(tick_utc_ts, datetime.timezone.utc)
        tick_age_s = observed_at.timestamp() - tick_utc_ts
        quote_fresh = abs(tick_age_s) <= max_tick_age_s

        # Map action string to MT5 order type
        action_upper = action.upper()
        if action_upper in ("BUY_LIMIT", "LIMIT_BUY"):
            order_type = mt5.ORDER_TYPE_BUY_LIMIT
            trade_action = mt5.TRADE_ACTION_PENDING
            is_buy = True
        elif action_upper in ("SELL_LIMIT", "LIMIT_SELL"):
            order_type = mt5.ORDER_TYPE_SELL_LIMIT
            trade_action = mt5.TRADE_ACTION_PENDING
            is_buy = False
        elif action_upper == "BUY":
            order_type = mt5.ORDER_TYPE_BUY
            trade_action = mt5.TRADE_ACTION_DEAL
            is_buy = True
        elif action_upper == "SELL":
            order_type = mt5.ORDER_TYPE_SELL
            trade_action = mt5.TRADE_ACTION_DEAL
            is_buy = False
        else:
            return {
                "status": "FAIL",
                "error": f"UNSUPPORTED_ACTION: {action}",
                "observed_at_utc": observed_at.isoformat(),
            }

        # Broker native calculations (order_calc_profit/margin require ORDER_TYPE_BUY=0 or ORDER_TYPE_SELL=1)
        calc_action = mt5.ORDER_TYPE_BUY if is_buy else mt5.ORDER_TYPE_SELL
        profit_sl = mt5.order_calc_profit(calc_action, symbol, volume, price, sl)
        profit_tp = mt5.order_calc_profit(calc_action, symbol, volume, price, tp)
        margin_req = mt5.order_calc_margin(calc_action, symbol, volume, price)

        # Build native trade request for order_check
        req = {
            "action": trade_action,
            "symbol": symbol,
            "volume": float(volume),
            "type": order_type,
            "price": float(price),
            "sl": float(sl),
            "tp": float(tp),
            "type_time": mt5.ORDER_TIME_GTC,
            "type_filling": mt5.ORDER_FILLING_RETURN,
            "comment": f"preflight_{dispatch_nonce[:8]}" if dispatch_nonce else "preflight",
        }

        check_res = mt5.order_check(req)
        check_dict = check_res._asdict() if check_res is not None else None
        check_retcode = check_dict.get("retcode") if check_dict else -1
        check_pass = check_retcode == 0

        # Spread metrics
        spread_raw = tick.ask - tick.bid
        mid = (tick.ask + tick.bid) / 2.0
        spread_bps = (spread_raw / mid * 10000.0) if mid > 0 else 0.0

        receipt = {
            "schema_version": "1.0.0",
            "dispatch_nonce": dispatch_nonce,
            "observed_at_utc": observed_at.strftime("%Y-%m-%d %H:%M:%S UTC"),
            "account": {
                "login": acc.login,
                "server": acc.server,
                "balance": round(acc.balance, 2),
                "equity": round(acc.equity, 2),
                "margin_free": round(acc.margin_free, 2),
            },
            "candidate": {
                "symbol": symbol,
                "action": action_upper,
                "volume": round(volume, 4),
                "price": price,
                "sl": sl,
                "tp": tp,
            },
            "broker_tick": {
                "bid": tick.bid,
                "ask": tick.ask,
                "mid": round(mid, sym_info.digits),
                "spread_raw": round(spread_raw, sym_info.digits),
                "spread_bps": round(spread_bps, 2),
                "tick_time_utc": tick_dt.strftime("%Y-%m-%d %H:%M:%S UTC"),
                "tick_age_seconds": round(tick_age_s, 2),
                "quote_fresh": quote_fresh,
            },
            "broker_spec": {
                "digits": sym_info.digits,
                "point": sym_info.point,
                "trade_mode": sym_info.trade_mode,
                "trade_mode_desc": "FULL" if sym_info.trade_mode == mt5.SYMBOL_TRADE_MODE_FULL else str(sym_info.trade_mode),
                "volume_min": sym_info.volume_min,
                "volume_step": sym_info.volume_step,
                "volume_max": sym_info.volume_max,
                "stops_level": sym_info.trade_stops_level,
            },
            "broker_valuation": {
                "profit_at_sl_usd": round(profit_sl, 2) if profit_sl is not None else None,
                "profit_at_tp_usd": round(profit_tp, 2) if profit_tp is not None else None,
                "margin_required_usd": round(margin_req, 2) if margin_req is not None else None,
                "nominal_risk_usd": round(abs(profit_sl), 2) if profit_sl is not None else None,
                "ticket_stress_usd": round(1.25 * abs(profit_sl) + 2.0, 2) if profit_sl is not None else None,
            },
            "order_check": {
                "pass": check_pass,
                "retcode": check_retcode,
                "comment": check_dict.get("comment") if check_dict else "NO_RESULT",
                "margin_level_post_order": check_dict.get("margin_level") if check_dict else None,
                "margin_free_post_order": round(check_dict.get("margin_free", 0.0), 2) if check_dict else None,
            },
            "preflight_verdict": "PREFLIGHT_PASS" if (quote_fresh and check_pass and sym_info.trade_mode == mt5.SYMBOL_TRADE_MODE_FULL) else "PREFLIGHT_FAIL",
        }

        # Deterministic SHA-256
        serialized = json.dumps(receipt, sort_keys=True, indent=2).encode("utf-8")
        receipt["receipt_sha256"] = hashlib.sha256(serialized).hexdigest()
        return receipt

    finally:
        mt5.shutdown()


def main():
    parser = argparse.ArgumentParser(description="Live MT5 execution preflight receipt generator")
    parser.add_argument("--symbol", default="BTCUSD.pi")
    parser.add_argument("--action", default="SELL_LIMIT")
    parser.add_argument("--volume", type=float, default=0.04)
    parser.add_argument("--price", type=float, default=81300.0)
    parser.add_argument("--sl", type=float, default=81780.0)
    parser.add_argument("--tp", type=float, default=79850.0)
    parser.add_argument("--nonce", default="")
    parser.add_argument("--out", default=str(DEFAULT_OUT))
    args = parser.parse_args()

    res = run_preflight(
        symbol=args.symbol,
        action=args.action,
        volume=args.volume,
        price=args.price,
        sl=args.sl,
        tp=args.tp,
        dispatch_nonce=args.nonce,
    )

    out_path = pathlib.Path(args.out)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(res, f, indent=2)

    print(f"[Preflight] Verdict: {res.get('preflight_verdict')}")
    print(f"[Preflight] Symbol: {args.symbol} | Tick Age: {res.get('broker_tick', {}).get('tick_age_seconds')}s | Quote Fresh: {res.get('broker_tick', {}).get('quote_fresh')}")
    print(f"[Preflight] OrderCheck: {res.get('order_check', {}).get('pass')} ({res.get('order_check', {}).get('comment')})")
    print(f"[Preflight] Receipt written: {out_path} (SHA: {res.get('receipt_sha256', '')[:16]}...)")


if __name__ == "__main__":
    main()
