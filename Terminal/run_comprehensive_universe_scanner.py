"""Read-only structural radar. Candidates require the full council hard gates."""
import math
import sys
from decimal import Decimal, ROUND_FLOOR, ROUND_CEILING
from pathlib import Path
from datetime import datetime, timezone
import MetaTrader5 as mt5
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
from Terminal.generate_cycle_envelope import read_inventory, atomic_json, KERNEL_FLOOR, GLOBAL_RESERVE


def snap(price, tick, up=False):
    value = Decimal(str(price)) / Decimal(str(tick))
    return float(value.to_integral_value(rounding=ROUND_CEILING if up else ROUND_FLOOR) * Decimal(str(tick)))


def lot_star(api, info, buy, entry, stop, risk_budget, free_margin):
    """Largest broker-grid lot satisfying native stop risk and free margin."""
    values = (info.volume_min, info.volume_max, info.volume_step, risk_budget, free_margin)
    if any(not math.isfinite(float(v)) or v <= 0 for v in values) or info.volume_min > info.volume_max:
        return None
    low, high, step = map(lambda v: Decimal(str(v)), (info.volume_min, info.volume_max, info.volume_step))
    left, right = 0, int((high-low)/step)
    best = None
    while left <= right:
        index = (left+right)//2
        volume = float(low + index*step)
        kind = api.ORDER_TYPE_BUY if buy else api.ORDER_TYPE_SELL
        loss = api.order_calc_profit(kind, info.name, volume, entry, stop)
        margin = api.order_calc_margin(kind, info.name, volume, entry)
        if (loss is None or margin is None or not math.isfinite(float(loss))
                or not math.isfinite(float(margin)) or loss >= 0 or margin < 0):
            return None
        if abs(loss) <= risk_budget + 1e-9 and margin <= free_margin:
            best = {"lot": volume, "risk_usd": abs(float(loss)), "margin_usd": float(margin)}
            left = index + 1
        else:
            right = index - 1
    return best


def category_of(info):
    label = (getattr(info, "path", "") + " " + info.name).upper()
    if "CRYPTO" in label or any(x in info.name.upper() for x in ("BTC", "ETH", "SOL", "LTC", "XRP", "DOG", "BNB")):
        return "Crypto"
    if any(x in label for x in ("INDIC", "SP500", "NAS100", "DJ30", "GER40", "UK100", "US30", "JP225")):
        return "Indices"
    if any(x in label for x in ("METAL", "COMMOD", "XAU", "XAG", "WTI", "BRENT", "OIL")):
        return "Commodities/Metals"
    return "Forex/Other"


def scan(api, now=None):
    now = now or datetime.now(timezone.utc)
    account, positions, orders, solvency = read_inventory(api)
    symbols = api.symbols_get()
    if symbols is None:
        raise RuntimeError("symbol_inventory_unavailable")
    target = min(solvency["risk_max_usd"], solvency["nominal_risk_capacity_usd"])
    print(f"Balance: {account['balance']:.2f} USD | Equity: {account['equity']:.2f} USD | {solvency['capital_mode']}")
    print(f"Capital Risk Band: {solvency['risk_min_usd']:.2f} to {solvency['risk_max_usd']:.2f} USD | Dynamic Target Risk: {target:.2f} USD")
    print(f"Realized Headroom: {solvency['realized_headroom_usd']:.2f} USD | Existing Tickets: {len(positions)+len(orders)}/2")
    candidates, vetoes = [], {}
    active = [s for s in symbols if s.trade_mode != 0 and s.visible]
    pending_margin = 0.0
    for order in orders:
        kind = api.ORDER_TYPE_BUY if order["type"] in (2, 4, 6) else api.ORDER_TYPE_SELL
        margin = api.order_calc_margin(kind, order["symbol"], order["volume_current"], order["price_open"])
        if margin is None or not math.isfinite(float(margin)) or margin < 0:
            raise RuntimeError("pending_margin_unknown")
        pending_margin += margin
    available_margin = max(0.0, account["margin_free"] - pending_margin)
    if not solvency["new_risk_admissible"]:
        vetoes["portfolio"] = "capital_or_capacity_unavailable"
    else:
        for info in active:
            symbol, category = info.name, category_of(info)
            # This radar cannot certify native holidays, session calendars or
            # row-level workbook freshness. Full hard gates remain external.
            if now.weekday() >= 5 and category != "Crypto":
                vetoes[symbol] = "WATCHLIST_ONLY_WEEKEND_NATIVE_MARKET_CLOSED"
                continue
            try:
                quote = api.symbol_info_tick(symbol)
                if quote is None or not 0 < quote.bid < quote.ask:
                    raise ValueError("quote_unavailable_or_crossed")
                rates = api.copy_rates_from_pos(symbol, api.TIMEFRAME_M15, 1, 60)
                if rates is None or len(rates) < 50:
                    raise ValueError("completed_bars_insufficient")
                highs, lows, closes = (np.asarray(rates[key], dtype=float) for key in ("high", "low", "close"))
                if any(not np.isfinite(a).all() or np.any(a <= 0) for a in (highs, lows, closes)):
                    raise ValueError("bar_prices_invalid")
                tr = np.maximum(highs[1:]-lows[1:], np.maximum(abs(highs[1:]-closes[:-1]), abs(lows[1:]-closes[:-1])))
                atr = float(tr[-14:].mean())
                tick = float(info.trade_tick_size)
                if not math.isfinite(atr) or atr <= 0 or not math.isfinite(tick) or tick <= 0:
                    raise ValueError("atr_or_tick_invalid")
                ema20 = ema50 = float(closes[0])
                for close in closes[1:]:
                    ema20 += 2/21*(close-ema20)
                    ema50 += 2/51*(close-ema50)
                for buy, eligible in ((True, closes[-1] >= ema50), (False, closes[-1] <= ema20)):
                    if not eligible:
                        continue
                    entry = snap(float(min(lows[-20:]) if buy else max(highs[-20:])), tick, up=not buy)
                    stop = snap(entry+(-.35 if buy else .35)*atr, tick, up=not buy)
                    target_price = snap(entry+(1 if buy else -1)*3*abs(entry-stop), tick, up=not buy)
                    if not (stop < entry < target_price and entry < quote.bid if buy
                            else target_price < entry < stop and entry > quote.ask):
                        continue
                    if (quote.ask-quote.bid)/abs(target_price-entry) > .15:
                        continue
                    if abs((quote.bid if buy else quote.ask)-entry) > 2*atr:
                        continue
                    sized = lot_star(api, info, buy, entry, stop, target, available_margin)
                    if sized is None or sized["risk_usd"] < solvency["risk_min_usd"]-1e-9:
                        continue
                    total_stress = GLOBAL_RESERVE+solvency["existing_ticket_stress_usd"]+1.25*sized["risk_usd"]+2
                    post = min(account["balance"], account["equity"])-total_stress
                    if post < KERNEL_FLOOR:
                        continue
                    request = {"action": api.TRADE_ACTION_PENDING, "symbol": symbol,
                               "type": api.ORDER_TYPE_BUY_LIMIT if buy else api.ORDER_TYPE_SELL_LIMIT,
                               "volume": sized["lot"], "price": entry, "sl": stop, "tp": target_price,
                               "type_time": api.ORDER_TIME_GTC, "type_filling": api.ORDER_FILLING_RETURN}
                    checked = api.order_check(request)
                    if checked is None or checked.retcode != 0:
                        vetoes[symbol] = "broker_order_check_failed"
                        continue
                    candidates.append({"symbol": symbol, "category": category,
                                       "side": "BUY_LIMIT" if buy else "SELL_LIMIT",
                                       "entry": entry, "sl": stop, "tp": target_price, **sized,
                                       "stressed_equity": post, "order_check_retcode": checked.retcode,
                                       "authorization": "WATCHLIST_ONLY_PENDING_FULL_HARD_GATES",
                                       "p_fill": None, "p_tp": None, "ev_net": None, "utility": None})
            except (ValueError, TypeError, KeyError, AttributeError, OverflowError) as exc:
                vetoes[symbol] = str(exc)
    report = {"timestamp": now.isoformat(), "account_login": account["login"],
              "total": len(candidates), "symbols_evaluated": len(active), "broker_symbols": len(symbols),
              "risk_policy": solvency, "vetoes": vetoes,
              "authorization": "WATCHLIST_ONLY_PENDING_FULL_HARD_GATES",
              "pipeline": {c: [r for r in candidates if r["category"] == c]
                           for c in ("Crypto", "Indices", "Commodities/Metals", "Forex/Other")}}
    print(f"Evaluated: {len(active)} visible symbols | Structural watchlist candidates: {len(candidates)}")
    return report


def main():
    if not mt5.initialize():
        raise RuntimeError(f"MT5 initialization failed: {mt5.last_error()}")
    try:
        report = scan(mt5)
    finally:
        mt5.shutdown()
    atomic_json(ROOT / "Data/telemetry/potential_candidates_pipeline.json", report)
    return report


if __name__ == "__main__":
    main()
