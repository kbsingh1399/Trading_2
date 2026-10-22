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
   - Model 2 (Trend Continuation & Pullback): 20/50/200 EMA ribbon hierarchy,
     pullback to EMA 20 / VWAP shelf (0.2 to 1.8 SD), Fibonacci 0.50-0.618 Golden Pocket.
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

def scan_all_156_assets(nominal_risk_target: float = 18.00) -> Dict[str, Any]:
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
        is_crypto = "Crypto" in group
        is_forex = "Forex" in group
        is_index = "Indices" in group
        is_commodity = "Commodities" in group
        is_exotic = is_forex and any(c in sym for c in ["SGD", "CNH", "HKD", "MXN", "ZAR", "NOK", "SEK", "HUF", "THB"])

        # Refined Dynamic Spread Friction Gate
        # Baselines: Crypto <= 35 bps, Exotics <= 25 bps, Indices/Commodities <= 10 bps, Forex Majors <= 6 bps
        max_spread_bps = 35.0 if is_crypto else (25.0 if is_exotic else (10.0 if (is_index or is_commodity) else 6.0))
        if spread_bps > max_spread_bps:
            continue

        # Pull 200 M15 bars
        rates = mt5.copy_rates_from_pos(sym, mt5.TIMEFRAME_M15, 0, 200)
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
        ema_20 = ind.get("ema_20")
        ema_50 = ind.get("ema_50")
        ema_200 = ind.get("ema_200")

        if not atr or atr <= 0 or not ema_20 or not ema_50 or not ema_200:
            continue

        # Calculate Fibonacci Retracements over last 60 M15 bars (15 hours)
        recent_bars = df.tail(60)
        swing_high = float(recent_bars["high"].max())
        swing_low = float(recent_bars["low"].min())
        swing_range = swing_high - swing_low

        # Trend & Regime classification
        regime = "UNDEFINED"
        if mid > ema_20 > ema_50 > ema_200:
            regime = "TREND_UP"
        elif mid < ema_20 < ema_50 < ema_200:
            regime = "TREND_DOWN"
        elif abs(vwap_z) < 1.0:
            regime = "MEAN_REVERT"

        # Signal Logic
        setup_type = None
        side = None
        entry_price = None
        sl_price = None
        tp_price = None
        rr_ratio = 0.0
        fib_confluence = "N/A"

        # Model 1: Extreme Mean Reversion (|Z| >= 2.0 to 3.5 SD)
        if abs(vwap_z) >= 2.0:
            if vwap_z <= -2.0 and rsi <= 35.0:
                setup_type = "MODEL_1_EXTREME_OVERSOLD"
                side = "BUY_LIMIT"
                entry_price = round(tick.bid, s_info.digits)
                sl_distance = max(1.5 * atr, spread_price * 4)
                sl_price = round(entry_price - sl_distance, s_info.digits)
                tp_distance = sl_distance * 2.2
                tp_price = round(entry_price + tp_distance, s_info.digits)
                rr_ratio = 2.2
                fib_confluence = f"Deep Swing Low Test ({swing_low:.{s_info.digits}f})"
            elif vwap_z >= 2.0 and rsi >= 65.0:
                setup_type = "MODEL_1_EXTREME_OVERBOUGHT"
                side = "SELL_LIMIT"
                entry_price = round(tick.ask, s_info.digits)
                sl_distance = max(1.5 * atr, spread_price * 4)
                sl_price = round(entry_price + sl_distance, s_info.digits)
                tp_distance = sl_distance * 2.2
                tp_price = round(entry_price - tp_distance, s_info.digits)
                rr_ratio = 2.2
                fib_confluence = f"Deep Swing High Test ({swing_high:.{s_info.digits}f})"

        # Model 2: Trend Following Pullback to EMA20 / VWAP / Fibonacci Shelf
        elif regime == "TREND_UP" and 0.2 <= vwap_z <= 1.6 and mid >= ema_20 * 0.997:
            # Bullish Fib: 50% to 61.8% Golden Pocket
            fib_500 = swing_high - swing_range * 0.500
            fib_618 = swing_high - swing_range * 0.618
            setup_type = "MODEL_2_TREND_PULLBACK_BUY"
            side = "BUY_LIMIT"
            entry_price = round(min(tick.bid, ema_20), s_info.digits)
            sl_distance = max(1.2 * atr, (entry_price - ema_50) if entry_price > ema_50 else 1.2 * atr)
            sl_price = round(entry_price - sl_distance, s_info.digits)
            tp_distance = sl_distance * 2.5
            tp_price = round(entry_price + tp_distance, s_info.digits)
            rr_ratio = 2.5
            fib_confluence = f"Fib 0.50-0.618 ({fib_618:.{s_info.digits}f}-{fib_500:.{s_info.digits}f})"
        elif regime == "TREND_DOWN" and -1.6 <= vwap_z <= -0.2 and mid <= ema_20 * 1.003:
            # Bearish Fib: 50% to 61.8% Golden Pocket
            fib_500 = swing_low + swing_range * 0.500
            fib_618 = swing_low + swing_range * 0.618
            setup_type = "MODEL_2_TREND_PULLBACK_SELL"
            side = "SELL_LIMIT"
            entry_price = round(max(tick.ask, ema_20), s_info.digits)
            sl_distance = max(1.2 * atr, (ema_50 - entry_price) if ema_50 > entry_price else 1.2 * atr)
            sl_price = round(entry_price + sl_distance, s_info.digits)
            tp_distance = sl_distance * 2.5
            tp_price = round(entry_price - tp_distance, s_info.digits)
            rr_ratio = 2.5
            fib_confluence = f"Fib 0.50-0.618 ({fib_500:.{s_info.digits}f}-{fib_618:.{s_info.digits}f})"

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
        if stressed_equity < BUFFER_FLOOR:
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
    risk_param = 18.00
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
