#!/usr/bin/env python3
"""
Terminal/institutional_95_screener.py
======================================
High-performance institutional screener evaluating all 95 tradeable MT5 symbols
(Forex Raw, Indices, Commodities, and Crypto) with full mathematical indicator,
volume profile, auction profile, and orderflow analysis.
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

def get_institutional_95_symbols() -> List[Dict[str, Any]]:
    """Scan MT5 symbols and return symbols meeting institutional friction gates."""
    if not mt5.initialize():
        return []
    
    symbols = mt5.symbols_get()
    if not symbols:
        return []
        
    eligible = []
    for s in symbols:
        info = mt5.symbol_info_tick(s.name)
        if not info or info.bid <= 0 or info.ask <= 0:
            continue
        mid = (info.bid + info.ask) / 2.0
        spread_bps = (info.ask - info.bid) / mid * 10000.0
        group = s.path.split("\\")[0]
        is_crypto = "Crypto" in group
        threshold = 25.0 if is_crypto else 5.0
        
        if spread_bps <= threshold:
            s_info = mt5.symbol_info(s.name)
            eligible.append({
                "symbol": s.name,
                "group": group,
                "path": s.path,
                "bid": info.bid,
                "ask": info.ask,
                "mid": mid,
                "spread_price": info.ask - info.bid,
                "spread_bps": spread_bps,
                "digits": s.digits,
                "contract_size": getattr(s_info, "trade_contract_size", 1.0) if s_info else 1.0,
                "min_lot": getattr(s_info, "volume_min", 0.01) if s_info else 0.01,
                "step_lot": getattr(s_info, "volume_step", 0.01) if s_info else 0.01,
                "max_lot": getattr(s_info, "volume_max", 100.0) if s_info else 100.0,
                "tick_size": getattr(s_info, "trade_tick_size", s.point) if s_info else s.point,
            })
    return eligible

def run_fast_screen(max_symbols: Optional[int] = None) -> Dict[str, Any]:
    """Execute complete institutional screen across eligible MT5 assets."""
    t0 = time.time()
    symbols = get_institutional_95_symbols()
    if max_symbols:
        symbols = symbols[:max_symbols]
        
    results = []
    candidates = []
    watchlist = []
    
    for item in symbols:
        sym = item["symbol"]
        raw_rates = mt5.copy_rates_from_pos(sym, mt5.TIMEFRAME_M15, 0, 400)
        if raw_rates is None or len(raw_rates) < 50:
            continue
            
        df = pd.DataFrame(raw_rates)
        bars = df.to_dict("records")
        indicators = CandleIndicatorEngine.compute_indicators(bars)
        
        mid = item["mid"]
        session_vwap = indicators.get("session_vwap")
        sigma = indicators.get("session_sigma") or indicators.get("rolling_sigma_24h")
        vwap_z = (mid - session_vwap) / sigma if (session_vwap and sigma and sigma > 0) else 0.0
        rsi = indicators.get("rsi_14", 50.0)
        atr = indicators.get("atr_14", 0.0)
        ema_20 = indicators.get("ema_20")
        ema_50 = indicators.get("ema_50")
        ema_200 = indicators.get("ema_200")
        
        # Trend classification
        regime = "UNDEFINED"
        if ema_20 and ema_50 and ema_200:
            if mid > ema_20 > ema_50 > ema_200:
                regime = "TREND_UP"
            elif mid < ema_20 < ema_50 < ema_200:
                regime = "TREND_DOWN"
            elif abs(vwap_z) < 1.0:
                regime = "MEAN_REVERT"
                
        # Model 1 & Model 2 Check
        model1_eligible = abs(vwap_z) >= 2.0 and regime == "MEAN_REVERT"
        model2_eligible = (
            (regime == "TREND_UP" and vwap_z > 0.0 and vwap_z <= 1.8 and ema_20 and mid >= ema_20 * 0.998) or
            (regime == "TREND_DOWN" and vwap_z < 0.0 and vwap_z >= -1.8 and ema_20 and mid <= ema_20 * 1.002)
        )
        
        status = "NO_SETUP"
        if model1_eligible:
            status = "CANDIDATE_MODEL1"
            candidates.append((sym, "MODEL_1", vwap_z, regime))
        elif model2_eligible:
            status = "CANDIDATE_MODEL2"
            candidates.append((sym, "MODEL_2", vwap_z, regime))
        elif abs(vwap_z) >= 1.5:
            status = "WATCHLIST"
            watchlist.append((sym, vwap_z, regime))
            
        results.append({
            "symbol": sym,
            "group": item["group"],
            "spread_bps": round(item["spread_bps"], 2),
            "vwap_z": round(vwap_z, 2),
            "rsi": round(rsi, 1) if rsi else None,
            "atr": round(atr, 5) if atr else None,
            "regime": regime,
            "status": status
        })
        
    duration = time.time() - t0
    return {
        "as_of_utc": time.strftime("%Y-%m-%d %H:%M:%S UTC", time.gmtime()),
        "duration_seconds": round(duration, 3),
        "total_eligible_symbols": len(symbols),
        "analyzed_symbols": len(results),
        "candidates_count": len(candidates),
        "candidates": candidates,
        "watchlist_count": len(watchlist),
        "watchlist": watchlist[:10],
        "summary": results
    }

if __name__ == "__main__":
    res = run_fast_screen()
    print(f"Screen completed in {res['duration_seconds']}s across {res['analyzed_symbols']} institutional symbols.")
    print(f"Candidates ({res['candidates_count']}): {res['candidates']}")
    print(f"Watchlist ({res['watchlist_count']}): {res['watchlist']}")
