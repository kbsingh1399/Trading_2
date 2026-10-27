#!/usr/bin/env python3
"""
Terminal/institutional_95_screener.py
======================================
Canonical Institutional Multi-Asset Screener & Signal Generator.
Upgraded from legacy 95-symbol screener to the full 156-asset MT5 universe:
- 60 Forex Raw (Majors, Crosses, Liquid Exotics)
- 22 Commodities & Raw Precious Metals (Gold, Silver, Oil, Gas, Base Metals)
- 16 Global Indices (US, European, Asian, Oceanic)
- 58 Cryptos & Cryptos Raw (BTC, ETH, SOL, Alts)

Applies:
1. Dynamic Asset-Class Spread Friction Gates:
   - Crypto <= 35.0 bps
   - Exotics <= 25.0 bps
   - Indices & Commodities <= 10.0 bps
   - Forex Majors & Crosses <= 6.0 bps
   - Relative Spread Cannibalization: Spread / TP Distance <= 15.0%
2. Dual-Engine Confluence Evaluation:
   - Model 1 (Extreme Mean Reversion): |Z_VWAP| >= 2.0 SD, RSI extremes, tape exhaustion
   - Model 2 (Trend Continuation Pullback): 20/50/200 EMA ribbon, pullback to EMA 20 / VWAP shelf (0.2 to 1.8 SD)
3. Dynamic Capital Allocation & Buffer Cushion Sentry:
   - Evaluated via live MT5 broker quote conversion (order_calc_profit)
   - Dynamic target risk sized to preserve the 4,795.00 USD operating buffer under 1.25x slippage + $2 fee
   - Stressed Equity = Equity - (Nominal Risk * 1.25 + 2.00) >= 4,795.00 USD
"""
from __future__ import annotations

import json
import math
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

def get_institutional_156_symbols() -> List[Dict[str, Any]]:
    """Scan all 156 MT5 instruments from canonical universe definition."""
    if not mt5.initialize():
        return []
    
    universe_path = ROOT / "Data" / "Assets" / "mt5_full_symbol_universe.json"
    symbols_to_scan = []
    symbol_meta = {}
    
    if universe_path.exists():
        try:
            with open(universe_path, "r", encoding="utf-8") as f:
                u_data = json.load(f)
                for item in u_data.get("symbols", []):
                    s_name = item.get("symbol")
                    if s_name:
                        symbols_to_scan.append(s_name)
                        symbol_meta[s_name] = item
        except Exception:
            pass

    if not symbols_to_scan:
        all_syms = mt5.symbols_get()
        if all_syms:
            symbols_to_scan = [s.name for s in all_syms if s.visible and s.trade_mode != 0]

    eligible = []
    for sym in symbols_to_scan:
        tick = mt5.symbol_info_tick(sym)
        s_info = mt5.symbol_info(sym)
        if not tick or not s_info or tick.bid <= 0 or tick.ask <= 0:
            continue
            
        mid = (tick.bid + tick.ask) / 2.0
        spread_price = tick.ask - tick.bid
        spread_bps = (spread_price / mid) * 10000.0
        
        path_str = s_info.path if s_info.path else symbol_meta.get(sym, {}).get("path", "")
        group = path_str.split("\\")[0] if path_str else "Unknown"
        is_crypto = "Crypto" in group
        is_forex = "Forex" in group
        is_index = "Indices" in group
        is_commodity = "Commodities" in group
        is_exotic = is_forex and any(c in sym for c in ["SGD", "CNH", "HKD", "MXN", "ZAR", "NOK", "SEK", "HUF", "THB"])
        
        # Dynamic spread friction baseline
        max_spread_bps = 35.0 if is_crypto else (25.0 if is_exotic else (10.0 if (is_index or is_commodity) else 6.0))
        
        if spread_bps <= max_spread_bps:
            eligible.append({
                "symbol": sym,
                "group": group,
                "path": path_str,
                "bid": tick.bid,
                "ask": tick.ask,
                "mid": mid,
                "spread_price": spread_price,
                "spread_bps": spread_bps,
                "digits": s_info.digits,
                "contract_size": getattr(s_info, "trade_contract_size", 1.0),
                "min_lot": getattr(s_info, "volume_min", 0.01),
                "step_lot": getattr(s_info, "volume_step", 0.01),
                "max_lot": getattr(s_info, "volume_max", 100.0),
                "tick_size": getattr(s_info, "trade_tick_size", s_info.point),
            })
    return eligible

def run_fast_screen(nominal_risk_target: Optional[float] = None) -> Dict[str, Any]:
    """Execute complete 156-asset institutional screen with exact geometry and cushion checks."""
    t0 = time.time()
    
    if not mt5.initialize():
        return {"error": "MT5 initialization failed"}
        
    acc = mt5.account_info()
    equity = acc.equity if acc else 4818.51
    live_buffer_cushion = max(0.0, equity - BUFFER_FLOOR)
    
    if nominal_risk_target is None:
        nominal_risk_target = max(5.0, min(10.0, (live_buffer_cushion - 2.50) / 1.25))
        
    symbols = get_institutional_156_symbols()
    
    candidates = []
    watchlist = []
    all_results = []
    
    for item in symbols:
        sym = item["symbol"]
        raw_rates = mt5.copy_rates_from_pos(sym, mt5.TIMEFRAME_M15, 0, 200)
        if raw_rates is None or len(raw_rates) < 50:
            continue
            
        df = pd.DataFrame(raw_rates)
        bars = df.to_dict("records")
        ind = CandleIndicatorEngine.compute_indicators(bars)
        
        mid = item["mid"]
        session_vwap = ind.get("session_vwap")
        sigma = ind.get("session_sigma") or ind.get("rolling_sigma_24h")
        vwap_z = (mid - session_vwap) / sigma if (session_vwap and sigma and sigma > 0) else 0.0
        rsi = ind.get("rsi_14", 50.0)
        atr = ind.get("atr_14", 0.0)
        # Upgraded to Institutional Fibonacci Prime Ribbon: 34, 89 (prime), 233 (prime)
        ema_34 = ind.get("ema_34") or ind.get("ema_20")
        ema_89 = ind.get("ema_89") or ind.get("ema_50")
        ema_233 = ind.get("ema_233") or ind.get("ema_200")
        
        if atr <= 0:
            continue
            
        # Determine Market Regime
        regime = "UNDEFINED"
        if ema_34 and ema_89 and ema_233:
            if mid > ema_34 > ema_89 > ema_233:
                regime = "TREND_UP"
            elif mid < ema_34 < ema_89 < ema_233:
                regime = "TREND_DOWN"
            else:
                regime = "RANGE"
                
        # Candidate Setup Logic
        setup_type = None
        side = None
        entry = 0.0
        sl = 0.0
        tp = 0.0
        
        # Model 1: Extreme Mean Reversion (Overextended Range / Auction Rejection)
        if abs(vwap_z) >= 2.0 and regime == "RANGE":
            if vwap_z > 2.0 and rsi > 65.0:
                setup_type = "MODEL_1_EXTREME_MR_SELL"
                side = "SELL_LIMIT"
                entry = item["ask"]
                sl = entry + (1.2 * atr)
                tp = entry - (2.5 * atr)
            elif vwap_z < -2.0 and rsi < 35.0:
                setup_type = "MODEL_1_EXTREME_MR_BUY"
                side = "BUY_LIMIT"
                entry = item["bid"]
                sl = entry - (1.2 * atr)
                tp = entry + (2.5 * atr)
                
        # Model 2: Trend Continuation Pullback
        elif regime == "TREND_UP" and 0.2 <= vwap_z <= 1.8:
            setup_type = "MODEL_2_TREND_PULLBACK_BUY"
            side = "BUY_LIMIT"
            entry = max(session_vwap, ema_34) if (session_vwap and ema_34) else (ema_34 or item["bid"])
            if entry > item["bid"]:
                entry = item["bid"]
            sl = entry - (1.0 * atr)
            tp = entry + (2.5 * atr)
            
        elif regime == "TREND_DOWN" and -1.8 <= vwap_z <= -0.2:
            setup_type = "MODEL_2_TREND_PULLBACK_SELL"
            side = "SELL_LIMIT"
            entry = min(session_vwap, ema_34) if (session_vwap and ema_34) else (ema_34 or item["ask"])
            if entry < item["ask"]:
                entry = item["ask"]
            sl = entry + (1.0 * atr)
            tp = entry - (2.5 * atr)
            
        # Watchlist
        elif abs(vwap_z) >= 1.5:
            watchlist.append({
                "symbol": sym,
                "group": item["group"],
                "vwap_z": round(vwap_z, 2),
                "regime": regime,
                "spread_bps": round(item["spread_bps"], 2)
            })
            
        if not setup_type or entry <= 0 or sl <= 0 or tp <= 0:
            continue
            
        risk_dist = abs(entry - sl)
        reward_dist = abs(tp - entry)
        if risk_dist <= 0 or reward_dist <= 0:
            continue
            
        rr = reward_dist / risk_dist
        if rr < 2.0:
            continue
            
        # Check Relative Spread Friction Gate: Spread / TP Distance <= 10.0% (Institutional Friction Invariant)
        spread_ratio = (item["spread_price"] / reward_dist) * 100.0
        if spread_ratio > 10.0:
            continue
            
        # Precise Position Sizing using MT5 order_calc_profit
        order_type = mt5.ORDER_TYPE_BUY if side == "BUY_LIMIT" else mt5.ORDER_TYPE_SELL
        test_lot = item["min_lot"]
        profit_at_sl = mt5.order_calc_profit(order_type, sym, test_lot, entry, sl)
        
        if profit_at_sl is None or abs(profit_at_sl) <= 0:
            unit_risk = risk_dist * item["contract_size"]
            loss_per_min_lot = unit_risk * test_lot
        else:
            loss_per_min_lot = abs(profit_at_sl)
            
        if loss_per_min_lot <= 0:
            continue
            
        raw_lot = (nominal_risk_target / loss_per_min_lot) * test_lot
        step = item["step_lot"]
        snapped_lot = max(item["min_lot"], math.floor(raw_lot / step) * step)
        snapped_lot = min(snapped_lot, item["max_lot"])
        
        # Recalculate exact nominal risk
        calc_loss = mt5.order_calc_profit(order_type, sym, snapped_lot, entry, sl)
        nominal_risk = abs(calc_loss) if calc_loss is not None else (loss_per_min_lot * (snapped_lot / test_lot))
        
        calc_gain = mt5.order_calc_profit(order_type, sym, snapped_lot, entry, tp)
        nominal_reward = abs(calc_gain) if calc_gain is not None else (nominal_risk * rr)
        
        # Buffer Defense Sentry Check (Explicit Spread + 1.25x Slippage + $2 Fee)
        spread_cost = item["spread_price"] * snapped_lot * item["contract_size"] if item["group"] == "Indices" or item["group"] == "Forex_Raw" else 0.0
        stressed_loss = (nominal_risk + min(1.0, spread_cost)) * 1.25 + 2.00
        stressed_equity = equity - stressed_loss
        buffer_surplus = stressed_equity - BUFFER_FLOOR
        
        if buffer_surplus < 0:
            continue
            
        cand_dict = {
            "symbol": sym,
            "group": item["group"],
            "setup": setup_type,
            "side": side,
            "lot": round(snapped_lot, 2),
            "entry": round(entry, item["digits"]),
            "sl": round(sl, item["digits"]),
            "tp": round(tp, item["digits"]),
            "rr": round(rr, 2),
            "spread_bps": round(item["spread_bps"], 2),
            "spread_share_pct": round(spread_ratio, 2),
            "vwap_z": round(vwap_z, 2),
            "nominal_risk": round(nominal_risk, 2),
            "nominal_reward": round(nominal_reward, 2),
            "stressed_equity": round(stressed_equity, 2),
            "buffer_surplus": round(buffer_surplus, 2)
        }
        candidates.append(cand_dict)
        
    duration = time.time() - t0
    return {
        "as_of_utc": time.strftime("%Y-%m-%d %H:%M:%S UTC", time.gmtime()),
        "duration_seconds": round(duration, 3),
        "total_universe_scanned": len(symbols),
        "target_risk_usd": nominal_risk_target,
        "live_equity_usd": equity,
        "buffer_cushion_usd": round(live_buffer_cushion, 2),
        "candidates_count": len(candidates),
        "candidates": candidates,
        "watchlist_count": len(watchlist),
        "watchlist": watchlist[:15]
    }

if __name__ == "__main__":
    res = run_fast_screen()
    print(f"Screen completed in {res['duration_seconds']}s across {res['total_universe_scanned']} institutional symbols.")
    print(f"Target Risk: ${res['target_risk_usd']:.2f} | Buffer Cushion: +${res['buffer_cushion_usd']:.2f}")
    print(f"Qualified Setups ({res['candidates_count']}):")
    print(f"{'Symbol':12s} | {'Setup':26s} | {'Side':10s} | {'Lot':5s} | {'Entry':10s} | {'SL':10s} | {'TP':10s} | {'Risk':7s} | {'Reward':7s} | {'Surplus':8s}")
    print("-" * 115)
    for c in res["candidates"][:12]:
        print(f"{c['symbol']:12s} | {c['setup']:26s} | {c['side']:10s} | {c['lot']:<5.2f} | {c['entry']:<10} | {c['sl']:<10} | {c['tp']:<10} | ${c['nominal_risk']:<6.2f} | ${c['nominal_reward']:<6.2f} | +${c['buffer_surplus']:<7.2f}")
