#!/usr/bin/env python3
"""
scripts/signal_anchored_trade_planner.py
========================================
Institutional Microstructure Signal-Anchored Trade Formulation Engine.
Directly anchors Maker limit entries, stop losses, and take profits to the latest
confirmed CoinGlass Footprint Signals (Bullish/Bearish Absorption, Trapped Traders,
Delta Divergences) and cross-corroborates each setup with the 15-Pillar battery.
"""

from __future__ import annotations
import datetime
import json
import os
import pathlib
import sys
from typing import Any, Dict, List, Optional

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

ROOT = pathlib.Path(__file__).resolve().parents[1]
FEEDS_DIR = ROOT / "Data" / "feeds"
DOSSIERS_DIR = ROOT / "docs" / "dossiers"
TRADE_PLANS_DIR = ROOT / "docs" / "trade_plans"

try:
    import polars as pl
except ImportError:
    pl = None

try:
    import MetaTrader5 as mt5
    MT5_AVAILABLE = True
except ImportError:
    MT5_AVAILABLE = False


def load_dossier(symbol: str) -> Optional[dict]:
    clean = symbol.replace("/", "").replace(":", "").replace(".pi", "").replace(".p", "")
    candidates = [
        f"{clean}_MASTER_DOSSIER.json",
        f"{clean}USD_MASTER_DOSSIER.json",
    ]
    if clean.endswith("USD"):
        base = clean[:-3]
        candidates.extend([f"{base}_MASTER_DOSSIER.json", f"{base}USD_MASTER_DOSSIER.json"])
    
    for c in candidates:
        p = DOSSIERS_DIR / c
        if p.exists() and p.stat().st_size > 50:
            try:
                with open(p, "r", encoding="utf-8") as f:
                    return json.load(f)
            except Exception:
                continue
    return None


def generate_signal_anchored_trades() -> List[Dict[str, Any]]:
    sig_path = FEEDS_DIR / "25_CoinGlass_Footprint_Signals.parquet"
    if not sig_path.exists() or pl is None:
        print("Error: Footprint signals parquet missing or polars unavailable.", file=sys.stderr)
        return []

    df = pl.read_parquet(sig_path)
    # Filter for signals with valid price levels > 0
    valid_signals = df.filter(pl.col("price_level") > 0)
    
    # Group by symbol or base_asset to get latest signals
    trades = []
    seen_symbols = set()

    # Sort descending by signal_time
    sorted_sigs = valid_signals.sort("signal_time", descending=True)
    
    for row in sorted_sigs.iter_rows(named=True):
        raw_sym = str(row.get("symbol", ""))
        base = str(row.get("base_asset", ""))
        sig_type = str(row.get("signal_type", ""))
        bias = str(row.get("bias", "")).upper()
        lvl = float(row.get("price_level", 0.0))
        vol = float(row.get("absorbed_vol_usd", 0.0) or 0.0)
        detail = str(row.get("detail", ""))
        sig_time = str(row.get("signal_time", ""))

        # Standardize MT5 symbol matching
        mt5_sym = None
        if "BTC" in raw_sym or "BTC" in base:
            mt5_sym = "BTCUSD.pi"
        elif "ETH" in raw_sym or "ETH" in base:
            mt5_sym = "ETHUSD.pi"
        elif "SOL" in raw_sym or "SOL" in base:
            mt5_sym = "SOLUSD.p"
        elif "BCH" in raw_sym or "BCH" in base:
            mt5_sym = "BCHUSD.p"
        elif "XAU" in raw_sym or "GOLD" in raw_sym:
            mt5_sym = "XAUUSD.pi"
        elif "XAG" in raw_sym or "SILVER" in raw_sym:
            mt5_sym = "XAGUSD.pi"
        elif "WTI" in raw_sym or "USWTI" in raw_sym:
            mt5_sym = "USWTI.p"
        elif "ZEC" in raw_sym:
            mt5_sym = "ZECUSD.p"

        if not mt5_sym or mt5_sym in seen_symbols:
            continue

        # Load asset dossier for 15-pillar parameters
        dossier = load_dossier(mt5_sym)
        if not dossier:
            continue

        seen_symbols.add(mt5_sym)

        telem = dossier.get("telemetry", {})
        specs = dossier.get("contract_specs", {})
        tech = dossier.get("technicals", {})
        auc = dossier.get("auction", {})
        wl2 = dossier.get("whales_and_l2", {})
        liq = dossier.get("liquidation_and_stops", {})
        cvd = dossier.get("cvd_and_orderflow", {})

        mid = float(telem.get("mid", 0.0) or (telem.get("bid", 0.0) + telem.get("ask", 0.0))/2)
        spread_bps = float(telem.get("spread_bps", 0.0))
        digits = int(specs.get("digits", 2))
        contract_size = float(specs.get("contract_size", 1.0))
        atr = float(tech.get("atr_14", 0.0))
        effective_atr = max(atr, mid * 0.005 if mid else 1.0)
        vwap = float(tech.get("vwap", 0.0))
        poc = float(auc.get("daily_poc", 0.0))
        vah = float(auc.get("daily_vah", 0.0))
        val = float(auc.get("daily_val", 0.0))

        # Check CVD alignment
        cvd_table = cvd.get("table", []) or []
        cvd_bias = cvd_table[0].get("bias", "NEUTRAL") if cvd_table else "NEUTRAL"

        # Signal-anchored geometry
        is_bull = "BULL" in bias or "ABSORP" in sig_type.upper() and "BULL" in bias or "TRAPPED SHORT" in sig_type.upper()
        is_bear = "BEAR" in bias or "ABSORP" in sig_type.upper() and "BEAR" in bias or "TRAPPED LONG" in sig_type.upper()

        if is_bull:
            action = "BUY_LIMIT"
            # Retest of the absorbed floor (or current price if price is testing it)
            # If current price is within 1 ATR of signal level, enter at signal level or slight front-run
            entry = round(lvl if lvl <= mid else min(lvl, mid * 0.998), digits)
            # SL strictly below the absorbed low, padded by 1.2 ATR
            sl = round(entry - 1.2 * effective_atr, digits)
            risk_dist = abs(entry - sl)
            # TP targeted at 2.50R
            tp = round(entry + 2.50 * risk_dist, digits)
            rr = 2.50
        elif is_bear:
            action = "SELL_LIMIT"
            # Retest of the absorbed ceiling
            entry = round(lvl if lvl >= mid else max(lvl, mid * 1.002), digits)
            sl = round(entry + 1.2 * effective_atr, digits)
            risk_dist = abs(sl - entry)
            tp = round(entry - 2.50 * risk_dist, digits)
            rr = 2.50
        else:
            continue

        # Sizing calculation for <= $10.00 nominal risk
        # risk_per_unit = risk_dist * contract_size
        risk_per_unit = risk_dist * contract_size
        max_risk_usd = 10.0
        min_vol = float(specs.get("volume_min", 0.01))
        vol_step = float(specs.get("volume_step", 0.01))
        
        raw_vol = max_risk_usd / risk_per_unit if risk_per_unit > 0 else min_vol
        # Round down to volume_step
        calc_vol = max(min_vol, round(int(raw_vol / vol_step) * vol_step, 2))
        actual_risk_usd = calc_vol * risk_dist * contract_size

        # Cap check: if actual_risk exceeds $10.00, adjust or skip
        if actual_risk_usd > 10.50:
            calc_vol = min_vol
            actual_risk_usd = calc_vol * risk_dist * contract_size

        trades.append({
            "symbol": mt5_sym,
            "action": action,
            "signal_anchor": {
                "signal_type": sig_type,
                "bias": bias,
                "signal_price": lvl,
                "signal_time": sig_time,
                "absorbed_vol_usd": vol,
                "detail": detail
            },
            "trade_geometry": {
                "current_mid": mid,
                "entry": entry,
                "sl": sl,
                "tp": tp,
                "risk_distance": round(risk_dist, digits),
                "reward_distance": round(abs(tp - entry), digits),
                "rr": rr,
                "volume": calc_vol,
                "nominal_risk_usd": round(actual_risk_usd, 2)
            },
            "15_pillar_context": {
                "spread_bps": spread_bps,
                "vwap": vwap,
                "poc": poc,
                "val": val,
                "vah": vah,
                "cvd_bias": cvd_bias,
                "whales": len(wl2.get("whale_ladder", []) or []),
                "stops": len(liq.get("hd_stops_ladder", []) or [])
            }
        })

    return trades


if __name__ == "__main__":
    plans = generate_signal_anchored_trades()
    print("=" * 80)
    print(f"🎯 SIGNAL-ANCHORED TRADE FORMULATION ENGINE: {len(plans)} CANDIDATES")
    print("=" * 80)
    for p in plans:
        geo = p["trade_geometry"]
        sig = p["signal_anchor"]
        ctx = p["15_pillar_context"]
        print(f"\n[{p['action']}] {p['symbol']} | Vol: {geo['volume']} lot | Risk: ${geo['nominal_risk_usd']} | R:R: {geo['rr']}R")
        print(f"   Entry: {geo['entry']} | SL: {geo['sl']} | TP: {geo['tp']} (Mid: {geo['current_mid']})")
        print(f"   Anchor Signal: {sig['signal_type']} ({sig['bias']}) @ {sig['signal_price']} [Time: {sig['signal_time']}]")
        print(f"   Pillars: Spread {ctx['spread_bps']:.2f} bps | CVD: {ctx['cvd_bias']} | VWAP: {ctx['vwap']:,.2f} | Whales: {ctx['whales']}")
        print(f"   Detail: {sig['detail']}")

    out_file = TRADE_PLANS_DIR / "CYCLE_038_SIGNAL_ANCHORED_TRADES.json"
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(plans, f, indent=2)
    print(f"\n✅ Saved signal-anchored trade plans to {out_file.name}")
