#!/usr/bin/env python3
"""
Terminal/multi_asset_opportunity_scanner.py
============================================
Exhaustive Multi-Asset Opportunity Scanner & Signal Generator.
Scans all 156 MT5 instruments across 6 asset classes:
- Forex Raw Majors, Liquid Crosses, and Exotics (60 pairs)
- Commodities & Raw Precious Metals (22 assets: Gold, Silver, Oil, etc.)
- Major & Minor Global Indices (16 indices: US, EU, Asia-Pacific)
- Cryptos & Cryptos Raw (58 perpetual instruments)

Evaluates:
1. Dynamic Spread Friction Gate:
   - Flexible baseline caps: Crypto <= 35 bps, Indices/Commodities <= 10 bps,
     Forex Majors/Crosses <= 6 bps, Exotics <= 25 bps.
   - Efficiency filter: Spread / TP Distance <= 15% (Spread does not cannibalize target).
2. Dual-Engine Confluence Stack:
   - Model 1 (Extreme Mean Reversion): |VWAP Z| >= 2.0 SD, RSI extremes (<35 or >65),
     liquidity sweep / rejection.
   - Model 2 (Trend Continuation & Pullback): Fibonacci Prime EMA ribbon hierarchy (13/34/89/233),
     pullback to EMA 34 / VWAP shelf (0.2 to 1.7 SD), Symmetrical Fibonacci Golden Zone (0.618-0.650 GP, 0.702 OTE, 0.786 Invalidation Shelf).
3. Institutional Position Sizing & Floor Cushion Defense:
   - Evaluated via exact broker quote conversion (mt5.order_calc_profit).
   - Nominal risk target: 18.00 USD (expandable to 25.00-35.00 USD for pristine confluence).
   - Inviolable operating buffer defense: Stressed Equity = Equity - (Risk * 1.25 + 2.00) >= 4,795.00 USD.
4. Complete Execution Ticket Geometry:
   Symbol, Group, Side, Lot, Entry, SL, TP, R:R, Nominal Risk, Stressed Equity, Buffer Surplus.
"""

from __future__ import annotations
import json
import pathlib
import sys
import time
from typing import Any, Dict, List, Optional

import MetaTrader5 as mt5
import numpy as np
import pandas as pd

ROOT = pathlib.Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from Terminal.Candle_Indicator_Engine import CandleIndicatorEngine

HARD_FLOOR = 4775.00
BUFFER_FLOOR = 4795.00
ADMISSION_FLOOR = 4795.00

def scan_all_156_assets(nominal_risk_target: float = 10.00) -> Dict[str, Any]:
    if not mt5.initialize():
        return {"error": "MT5 initialization failed"}

    acc = mt5.account_info()
    if not acc:
        return {"error": "MT5 account info unavailable"}

    equity = acc.equity
    balance = acc.balance
    live_cushion = equity - BUFFER_FLOOR

    # Load 156 symbol universe definition
    universe_path = ROOT / "Data" / "Assets" / "mt5_full_symbol_universe.json"
    symbols_to_scan = []
    if universe_path.exists():
        try:
            with open(universe_path, "r", encoding="utf-8") as f:
                u_data = json.load(f)
                symbols_to_scan = [s["symbol"] for s in u_data.get("symbols", [])]
        except Exception:
            pass

    if not symbols_to_scan:
        # Fallback to all MT5 symbols
        symbols_to_scan = [s.name for s in mt5.symbols_get() or []]

    opportunities = []

    for sym in symbols_to_scan:
        tick = mt5.symbol_info_tick(sym)
        s_info = mt5.symbol_info(sym)
        if not tick or not s_info or tick.bid <= 0 or tick.ask <= 0:
            continue

        mid = (tick.bid + tick.ask) / 2.0
        spread_price = tick.ask - tick.bid
        spread_bps = (spread_price / mid) * 10000.0

        group = s_info.path.split("\\")[0] if s_info.path else "Unknown"
        is_crypto = "Crypto" in group or any(k in sym for k in ["BTC", "ETH", "SOL", "XRP", "BNB", "ADA", "DOG", "LTC", "DOT"])
        is_forex = "Forex" in group
        is_index = "Indices" in group
        is_commodity = "Commodities" in group
        is_exotic = is_forex and any(c in sym for c in ["SGD", "CNH", "HKD", "MXN", "ZAR", "NOK", "SEK", "HUF", "THB"])

        # Weekend venue gate: If weekend, exclusively trade 24/7 crypto perpetuals
        import datetime
        now_utc = datetime.datetime.now(datetime.timezone.utc)
        if now_utc.weekday() in (5, 6) and not is_crypto:
            continue

        # Trade mode gate: Symbol must be active for full trading
        if s_info.trade_mode != mt5.SYMBOL_TRADE_MODE_FULL:
            continue

        # Refined Dynamic Spread Friction Gate
        # Baselines: Crypto <= 35 bps, Exotics <= 25 bps, Indices/Commodities <= 10 bps, Forex Majors <= 6 bps
        max_spread_bps = 35.0 if is_crypto else (25.0 if is_exotic else (10.0 if (is_index or is_commodity) else 6.0))
        if spread_bps > max_spread_bps:
            continue

        # Pull 350 M15 bars (ensures 233-period Fibonacci Prime EMA has sufficient historical depth)
        rates = mt5.copy_rates_from_pos(sym, mt5.TIMEFRAME_M15, 0, 350)
        if rates is None or len(rates) < 50:
            continue

        df = pd.DataFrame(rates)
        bars = df.to_dict("records")
        ind = CandleIndicatorEngine.compute_indicators(bars)

        vwap = ind.get("session_vwap")
        sigma = ind.get("session_sigma") or ind.get("rolling_sigma_24h")
        if not vwap or not sigma or sigma <= 0:
            continue

        vwap_z = (mid - vwap) / sigma
        rsi = ind.get("rsi_14", 50.0)
        atr = ind.get("atr_14", 0.0)
        
        # Fibonacci Prime EMAs (with backward compatibility fallback)
        ema_5 = ind.get("ema_5", ind.get("ema_9"))
        ema_13 = ind.get("ema_13", ind.get("ema_20"))
        ema_34 = ind.get("ema_34", ind.get("ema_20"))
        ema_89 = ind.get("ema_89", ind.get("ema_50"))
        ema_144 = ind.get("ema_144", ind.get("ema_100"))
        ema_233 = ind.get("ema_233") or ind.get("ema_144") or ind.get("ema_89")

        if not atr or atr <= 0 or not ema_13 or not ema_34 or not ema_89:
            continue

        # Symmetrical Fibonacci Retracement impulse over last 96 M15 bars (24 hours)
        recent_bars = df.tail(96)
        high_idx = recent_bars["high"].idxmax()
        low_idx = recent_bars["low"].idxmin()
        swing_high = float(recent_bars["high"].max())
        swing_low = float(recent_bars["low"].min())
        swing_range = swing_high - swing_low

        if swing_range <= 0:
            continue

        # Trend & Regime classification: Fibonacci Prime Ribbon Hierarchy
        # Allows pullbacks into dynamic EMA 34/89 shelves while maintaining structural hierarchy
        regime = "UNDEFINED"
        if ema_13 > ema_34 > ema_89 and mid >= ema_89:
            regime = "TREND_UP"
        elif ema_13 < ema_34 < ema_89 and mid <= ema_89:
            regime = "TREND_DOWN"
        elif abs(vwap_z) >= 1.8:
            regime = "MEAN_REVERT"

        if regime == "TREND_UP" or (regime != "TREND_DOWN" and low_idx < high_idx):
            # Bullish Impulse (Low -> High), Retracement pulls down
            fib_dir = "BULLISH"
            fib_gp_max = swing_high - 0.618 * swing_range
            fib_gp_min = swing_high - 0.650 * swing_range
            fib_ote = swing_high - 0.702 * swing_range
            fib_inval = swing_high - 0.786 * swing_range
        else:
            # Bearish Impulse (High -> Low), Retracement rallies up
            fib_dir = "BEARISH"
            fib_gp_min = swing_low + 0.618 * swing_range
            fib_gp_max = swing_low + 0.650 * swing_range
            fib_ote = swing_low + 0.702 * swing_range
            fib_inval = swing_low + 0.786 * swing_range

        # Signal Logic
        setup_type = None
        side = None
        entry_price = None
        sl_price = None
        tp_price = None
        rr_ratio = 0.0
        fib_confluence = "N/A"

        # Model 1A: Extreme Statistical Mean Reversion (|Z| >= 1.8 to 3.5 SD)
        if abs(vwap_z) >= 1.8:
            if vwap_z <= -1.8 and rsi <= 38.0:
                setup_type = "MODEL_1A_EXTREME_OVERSOLD"
                side = "BUY_LIMIT"
                entry_price = round(tick.bid, s_info.digits)
                sl_distance = max(1.4 * atr, spread_price * 4)
                sl_price = round(entry_price - sl_distance, s_info.digits)
                tp_distance = sl_distance * 2.2
                tp_price = round(entry_price + tp_distance, s_info.digits)
                rr_ratio = 2.2
                fib_confluence = f"Deep Swing Low Test ({swing_low:.{s_info.digits}f})"
            elif vwap_z >= 1.8 and rsi >= 62.0:
                setup_type = "MODEL_1A_EXTREME_OVERBOUGHT"
                side = "SELL_LIMIT"
                entry_price = round(tick.ask, s_info.digits)
                sl_distance = max(1.4 * atr, spread_price * 4)
                sl_price = round(entry_price + sl_distance, s_info.digits)
                tp_distance = sl_distance * 2.2
                tp_price = round(entry_price - tp_distance, s_info.digits)
                rr_ratio = 2.2
                fib_confluence = f"Deep Swing High Test ({swing_high:.{s_info.digits}f})"

        # Model 2B: Trend Following Pullback into Symmetrical Golden Zone & Fib-Prime EMA Shelf
        elif regime == "TREND_UP" and 0.2 <= vwap_z <= 1.7 and fib_dir == "BULLISH" and mid >= fib_inval:
            pullback_target = max(fib_gp_min, ema_34)
            setup_type = "MODEL_2B_TREND_PULLBACK_BUY"
            side = "BUY_LIMIT"
            entry_price = round(min(tick.bid, pullback_target), s_info.digits)
            sl_candidate = min(fib_inval - 0.40 * atr, ema_89 - 0.20 * atr)
            sl_distance = max(1.2 * atr, abs(entry_price - sl_candidate))
            sl_price = round(entry_price - sl_distance, s_info.digits)
            tp_distance = sl_distance * 2.5
            tp_price = round(entry_price + tp_distance, s_info.digits)
            rr_ratio = 2.5
            fib_confluence = f"OTE/GP [0.618-0.702] ({fib_ote:.{s_info.digits}f}-{fib_gp_max:.{s_info.digits}f}) | Inval 0.786: {fib_inval:.{s_info.digits}f}"
        elif regime == "TREND_DOWN" and -1.7 <= vwap_z <= -0.2 and fib_dir == "BEARISH" and mid <= fib_inval:
            pullback_target = min(fib_gp_max, ema_34)
            setup_type = "MODEL_2B_TREND_PULLBACK_SELL"
            side = "SELL_LIMIT"
            entry_price = round(max(tick.ask, pullback_target), s_info.digits)
            sl_candidate = max(fib_inval + 0.40 * atr, ema_89 + 0.20 * atr)
            sl_distance = max(1.2 * atr, abs(sl_candidate - entry_price))
            sl_price = round(entry_price + sl_distance, s_info.digits)
            tp_distance = sl_distance * 2.5
            tp_price = round(entry_price - tp_distance, s_info.digits)
            rr_ratio = 2.5
            fib_confluence = f"OTE/GP [0.618-0.702] ({fib_gp_min:.{s_info.digits}f}-{fib_ote:.{s_info.digits}f}) | Inval 0.786: {fib_inval:.{s_info.digits}f}"

        # Model 1B: Failed Auction / Swing Liquidity Sweep Reclaim
        elif not setup_type:
            # Check for swing low sweep and reclaim in the last 4 bars
            if recent_bars["low"].iloc[-4:].min() <= swing_low and mid > swing_low and rsi < 48:
                setup_type = "MODEL_1B_SWEEP_RECLAIM_BUY"
                side = "BUY_LIMIT"
                entry_price = round(tick.bid, s_info.digits)
                sl_distance = max(1.2 * atr, abs(entry_price - (recent_bars["low"].min() - 0.40 * atr)))
                sl_price = round(entry_price - sl_distance, s_info.digits)
                tp_distance = sl_distance * 2.2
                tp_price = round(entry_price + tp_distance, s_info.digits)
                rr_ratio = 2.2
                fib_confluence = f"Swing Low Liquidity Sweep & Reclaim ({swing_low:.{s_info.digits}f})"
            elif recent_bars["high"].iloc[-4:].max() >= swing_high and mid < swing_high and rsi > 52:
                setup_type = "MODEL_1B_SWEEP_RECLAIM_SELL"
                side = "SELL_LIMIT"
                entry_price = round(tick.ask, s_info.digits)
                sl_distance = max(1.2 * atr, abs((recent_bars["high"].max() + 0.40 * atr) - entry_price))
                sl_price = round(entry_price + sl_distance, s_info.digits)
                tp_distance = sl_distance * 2.2
                tp_price = round(entry_price - tp_distance, s_info.digits)
                rr_ratio = 2.2
                fib_confluence = f"Swing High Liquidity Sweep & Reclaim ({swing_high:.{s_info.digits}f})"

        # Model 4A: Volatility Squeeze & Compression Ribbon Breakout
        elif not setup_type and regime in ("TREND_UP", "TREND_DOWN"):
            ema_spread = abs(ema_13 - ema_89) / mid
            if ema_spread < 0.008:  # Ribbon compression knot < 0.8%
                if regime == "TREND_UP" and mid > ema_13 and rsi > 50:
                    setup_type = "MODEL_4A_SQUEEZE_BREAKOUT_BUY"
                    side = "BUY_LIMIT"
                    entry_price = round(min(tick.bid, ema_13), s_info.digits)
                    sl_distance = max(1.2 * atr, abs(entry_price - (ema_89 - 0.30 * atr)))
                    sl_price = round(entry_price - sl_distance, s_info.digits)
                    tp_distance = sl_distance * 2.5
                    tp_price = round(entry_price + tp_distance, s_info.digits)
                    rr_ratio = 2.5
                    fib_confluence = f"Compression Knot Breakout (Spread: {ema_spread*100:.2f}%)"
                elif regime == "TREND_DOWN" and mid < ema_13 and rsi < 50:
                    setup_type = "MODEL_4A_SQUEEZE_BREAKOUT_SELL"
                    side = "SELL_LIMIT"
                    entry_price = round(max(tick.ask, ema_13), s_info.digits)
                    sl_distance = max(1.2 * atr, abs((ema_89 + 0.30 * atr) - entry_price))
                    sl_price = round(entry_price + sl_distance, s_info.digits)
                    tp_distance = sl_distance * 2.5
                    tp_price = round(entry_price - tp_distance, s_info.digits)
                    rr_ratio = 2.5
                    fib_confluence = f"Compression Knot Breakdown (Spread: {ema_spread*100:.2f}%)"


        if not setup_type or not entry_price or not sl_price or not tp_price:
            continue

        tp_distance_points = abs(tp_price - entry_price)
        if tp_distance_points <= 0:
            continue

        # Efficiency filter: spread price must not consume > 15% of TP distance
        if spread_price / tp_distance_points > 0.15:
            continue

        # Position Sizing: exact quote conversion via mt5.order_calc_profit
        order_type_check = mt5.ORDER_TYPE_BUY if "BUY" in side else mt5.ORDER_TYPE_SELL
        test_profit_1lot = mt5.order_calc_profit(order_type_check, sym, 1.0, entry_price, sl_price)

        point = s_info.point
        if test_profit_1lot is not None and abs(test_profit_1lot) > 0:
            risk_per_1_lot = abs(test_profit_1lot)
        else:
            tick_value = getattr(s_info, "trade_tick_value", 1.0) or 1.0
            tick_size = getattr(s_info, "trade_tick_size", point) or point
            risk_per_1_lot = (abs(entry_price - sl_price) / tick_size) * tick_value if tick_size > 0 else 1000.0

        if risk_per_1_lot <= 0:
            continue

        calc_lot = nominal_risk_target / risk_per_1_lot
        min_lot = getattr(s_info, "volume_min", 0.01)
        step_lot = getattr(s_info, "volume_step", 0.01)
        max_lot = getattr(s_info, "volume_max", 100.0)

        steps = round(calc_lot / step_lot)
        lot = max(min_lot, min(steps * step_lot, max_lot))
        lot = round(lot, 2)

        # Recalculate exact actual cash risk using mt5.order_calc_profit
        exact_profit = mt5.order_calc_profit(order_type_check, sym, lot, entry_price, sl_price)
        actual_risk = abs(exact_profit) if (exact_profit is not None and abs(exact_profit) > 0) else lot * risk_per_1_lot

        stressed_loss = actual_risk * 1.25 + 2.00  # 1.25x slippage stress + 2.00 commission reserve
        stressed_equity = equity - stressed_loss

        # Inviolable operating buffer defense gate (stressed equity >= 4,795.00 USD)
        if stressed_equity < ADMISSION_FLOOR:
            continue

        potential_reward = actual_risk * rr_ratio

        opportunities.append({
            "symbol": sym,
            "group": group,
            "spread_bps": round(spread_bps, 2),
            "regime": regime,
            "vwap_z": round(vwap_z, 2),
            "rsi": round(rsi, 1),
            "atr": round(atr, 5),
            "setup_type": setup_type,
            "side": side,
            "lot": lot,
            "entry": entry_price,
            "sl": sl_price,
            "tp": tp_price,
            "rr": rr_ratio,
            "fib_confluence": fib_confluence,
            "nominal_risk_usd": round(actual_risk, 2),
            "potential_reward_usd": round(potential_reward, 2),
            "stressed_equity_usd": round(stressed_equity, 2),
            "buffer_surplus_usd": round(stressed_equity - BUFFER_FLOOR, 2)
        })

    # Sort opportunities:
    # 1. Model 1 extreme first, then Model 2
    # 2. Lowest spread
    # 3. Best buffer surplus
    opportunities.sort(key=lambda x: (
        0 if "MODEL_1" in x["setup_type"] else 1,
        x["spread_bps"],
        -x["buffer_surplus_usd"]
    ))

    return {
        "as_of_utc": time.strftime("%Y-%m-%d %H:%M:%S UTC", time.gmtime()),
        "total_scanned": len(symbols_to_scan),
        "total_opportunities": len(opportunities),
        "live_equity": equity,
        "buffer_floor": BUFFER_FLOOR,
        "hard_floor": HARD_FLOOR,
        "opportunities": opportunities
    }

if __name__ == "__main__":
    risk_param = 10.00
    if len(sys.argv) > 1:
        try:
            risk_param = float(sys.argv[1])
        except ValueError:
            pass

    res = scan_all_156_assets(nominal_risk_target=risk_param)
    print(f"Scanned {res.get('total_scanned')} symbols. Found {res.get('total_opportunities')} qualified opportunities (Target Risk: ${risk_param:.2f}).")
    print("=" * 130)
    print(f"{'Symbol':<12} | {'Asset Class':<18} | {'Setup':<26} | {'Side':<10} | {'Lot':<5} | {'Entry':<10} | {'SL':<10} | {'TP':<10} | {'Risk $':<7} | {'Reward $':<8} | {'Surplus $'}")
    print("-" * 130)
    for opp in res.get("opportunities", [])[:20]:
        print(f"{opp['symbol']:<12} | {opp['group']:<18} | {opp['setup_type']:<26} | {opp['side']:<10} | {opp['lot']:<5.2f} | {opp['entry']:<10} | {opp['sl']:<10} | {opp['tp']:<10} | {opp['nominal_risk_usd']:<7.2f} | {opp['potential_reward_usd']:<8.2f} | +{opp['buffer_surplus_usd']:.2f}")
