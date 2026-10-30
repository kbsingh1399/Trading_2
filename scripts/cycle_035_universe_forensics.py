#!/usr/bin/env python3
"""
scripts/cycle_035_universe_forensics.py
Full-scale Cycle_035 individual JSON dossier examination and candidate trade formulation.
Calculates exact Entry, SL, TP, lots, and risk for Blueberry Markets MT5.
"""

import datetime
import json
import os
import pathlib
import sys
import pandas as pd
import MetaTrader5 as mt5

ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.stdout.reconfigure(encoding="utf-8", errors="replace")

DOSSIER_DIR = ROOT / "docs" / "dossiers"
OUTPUT_DB_PATH = ROOT / "docs" / "trade_plans" / "CYCLE_035_FULL_SCALE_UNIVERSE_DATABASE.json"

def calculate_trade_card(canonical, broker_sym, category, mid, bid, ask, spread_bps, auction, technicals, liquidations, whales):
    val = auction.get("daily_val") or auction.get("developing_val", 0.0)
    poc = auction.get("daily_poc") or auction.get("developing_poc", 0.0)
    vah = auction.get("daily_vah") or auction.get("developing_vah", 0.0)
    vwap = technicals.get("vwap") or technicals.get("vwap_mid", 0.0)
    atr = technicals.get("atr_14", 0.0)
    
    mp_24h = liquidations.get("mp_24h", {})
    if isinstance(mp_24h, dict):
        short_max_pain = float(mp_24h.get("short_max_pain_price", 0.0) or 0.0)
        long_max_pain = float(mp_24h.get("long_max_pain_price", 0.0) or 0.0)
    else:
        short_max_pain = float(liquidations.get("short_max_pain_24h", 0.0) or 0.0)
        long_max_pain = float(liquidations.get("long_max_pain_24h", 0.0) or 0.0)

    score = 50.0
    signals = []
    
    # Check VWAP deviation
    if vwap > 0 and mid > 0:
        vwap_dev = ((mid - vwap) / vwap) * 100.0
        if abs(vwap_dev) >= 1.5:
            score += 15.0
            signals.append(f"VWAP dev: {vwap_dev:+.2f}%")
            
    # Check Auction positioning
    if val > 0 and vah > 0 and mid > 0:
        if mid < val:
            score += 15.0
            signals.append(f"Trading below VAL ({val:.2f}) - Deep Discount")
        elif mid > vah:
            score += 15.0
            signals.append(f"Trading above VAH ({vah:.2f}) - High Premium")
            
    # Check Liquidation Max Pain
    if short_max_pain > 0 and mid > 0:
        smp_dist = ((short_max_pain - mid) / mid) * 100.0
        if 0.5 <= smp_dist <= 4.0:
            score += 10.0
            signals.append(f"Short Max Pain overhead @ {short_max_pain:.2f} (+{smp_dist:.2f}%)")
            
    if long_max_pain > 0 and mid > 0:
        lmp_dist = ((mid - long_max_pain) / mid) * 100.0
        if 0.5 <= lmp_dist <= 4.0:
            score += 10.0
            signals.append(f"Long Max Pain below @ {long_max_pain:.2f} (-{lmp_dist:.2f}%)")

    # Formulation card construction
    trade_card = None
    if score >= 75.0 and atr > 0:
        # Determine long vs short bias
        if mid < val or (long_max_pain > 0 and mid <= long_max_pain * 1.01):
            # Bullish Mean-Reversion Long
            entry = round(val if val > 0 else mid * 0.995, 4 if "JPY" in broker_sym else (2 if mid > 10 else 5))
            sl = round(entry - max(atr * 1.5, entry * 0.008), 4 if "JPY" in broker_sym else (2 if mid > 10 else 5))
            risk_dist = abs(entry - sl)
            tp = round(entry + (risk_dist * 2.5), 4 if "JPY" in broker_sym else (2 if mid > 10 else 5))
            rr = round(abs(tp - entry) / risk_dist, 3) if risk_dist > 0 else 0
            
            trade_card = {
                "action": "BUY_LIMIT",
                "entry": entry,
                "sl": sl,
                "tp": tp,
                "risk_distance": risk_dist,
                "rr_ratio": rr,
                "bias": "BULLISH_MEAN_REVERSION"
            }
        elif mid > vah or (short_max_pain > 0 and mid >= short_max_pain * 0.99):
            # Bearish Fading Short
            entry = round(vah if vah > 0 else mid * 1.005, 4 if "JPY" in broker_sym else (2 if mid > 10 else 5))
            sl = round(entry + max(atr * 1.5, entry * 0.008), 4 if "JPY" in broker_sym else (2 if mid > 10 else 5))
            risk_dist = abs(sl - entry)
            tp = round(entry - (risk_dist * 2.5), 4 if "JPY" in broker_sym else (2 if mid > 10 else 5))
            rr = round(abs(entry - tp) / risk_dist, 3) if risk_dist > 0 else 0
            
            trade_card = {
                "action": "SELL_LIMIT",
                "entry": entry,
                "sl": sl,
                "tp": tp,
                "risk_distance": risk_dist,
                "rr_ratio": rr,
                "bias": "BEARISH_MEAN_REVERSION"
            }

    return {
        "canonical": canonical,
        "broker_symbol": broker_sym,
        "category": category,
        "spread_bps": spread_bps,
        "live_mid": mid,
        "vwap": vwap,
        "atr_14": atr,
        "val": val,
        "poc": poc,
        "vah": vah,
        "short_max_pain": short_max_pain,
        "long_max_pain": long_max_pain,
        "confluence_score": min(score, 100.0),
        "signals": signals,
        "trade_card": trade_card
    }

def main():
    print("=" * 80)
    print("🔬 RUNNING CYCLE_035 UNIVERSE FORENSICS & CANDIDATE FORMULATION")
    print("=" * 80)
    
    telemetry_path = ROOT / "Data" / "feeds" / "00_MT5_Account_Telemetry.parquet"
    df = pd.read_parquet(telemetry_path)
    passed_df = df[(df["Gate_Status"] == "PASS") & (df["Category"] == "SPREAD_GATE")].copy()
    
    catalog_path = ROOT / "Data" / "metadata" / "master_asset_catalog.json"
    with open(catalog_path, "r", encoding="utf-8") as f:
        catalog_raw = json.load(f)
    catalog = catalog_raw.get("assets", catalog_raw)
    
    mt5_to_canonical = {}
    for canonical, meta in catalog.items():
        if isinstance(meta, dict):
            sym = meta.get("mt5_symbol") or meta.get("broker_symbol")
            if sym:
                mt5_to_canonical[sym] = (canonical, meta.get("asset_class", "Unknown"))

    eligible_assets = []
    for _, row in passed_df.iterrows():
        broker_sym = str(row.get("Broker_Symbol", "")).strip()
        spread_bps = float(row.get("Spread_BPS", 999.0))
        bid = float(row.get("Bid_Quote", 0.0))
        ask = float(row.get("Ask_Quote", 0.0))
        mid = (bid + ask) / 2.0 if (bid + ask) > 0 else float(row.get("Mid_Price", 0.0))
        
        canonical, asset_class = mt5_to_canonical.get(
            broker_sym, 
            (broker_sym.replace(".pi", "").replace(".p", ""), "Unknown")
        )
        eligible_assets.append({
            "canonical": canonical,
            "broker_symbol": broker_sym,
            "asset_class": asset_class,
            "spread_bps": spread_bps,
            "bid": bid,
            "ask": ask,
            "mid": mid
        })

    print(f"Total spread-cleared eligible assets: {len(eligible_assets)}")

    audited_records = []
    for i, a in enumerate(eligible_assets, 1):
        canonical = a["canonical"]
        json_file = DOSSIER_DIR / f"{canonical}_MASTER_DOSSIER.json"
        if not json_file.exists():
            alt = DOSSIER_DIR / f"{a['broker_symbol'].replace('.pi', '').replace('.p', '')}_MASTER_DOSSIER.json"
            if alt.exists():
                json_file = alt

        if not json_file.exists():
            continue

        with open(json_file, "r", encoding="utf-8") as f:
            d = json.load(f)

        card = calculate_trade_card(
            canonical=canonical,
            broker_sym=a["broker_symbol"],
            category=d.get("category", a["asset_class"]),
            mid=a["mid"],
            bid=a["bid"],
            ask=a["ask"],
            spread_bps=a["spread_bps"],
            auction=d.get("auction", {}),
            technicals=d.get("technicals", {}),
            liquidations=d.get("liquidations", {}),
            whales=d.get("whales_and_l2", {})
        )
        audited_records.append(card)

    # Rank by score
    ranked = sorted(audited_records, key=lambda x: x["confluence_score"], reverse=True)
    top_candidates = [r for r in ranked if r["trade_card"] is not None]

    print(f"\nIdentified {len(top_candidates)} Actionable High-Confluence Trade Setups:")
    for i, c in enumerate(top_candidates[:8], 1):
        tc = c["trade_card"]
        print(f"#{i} {c['canonical']} ({c['broker_symbol']}) | Score: {c['confluence_score']}/100 | Spread: {c['spread_bps']:.2f} bps")
        print(f"   Action: {tc['action']} @ {tc['entry']} | SL: {tc['sl']} | TP: {tc['tp']} | R:R: {tc['rr_ratio']:.2f}R")
        print(f"   Signals: {', '.join(c['signals'])}\n")

    output_payload = {
        "cycle_id": "Cycle_035",
        "timestamp_utc": datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC"),
        "total_eligible_assets": len(eligible_assets),
        "total_forensics_completed": len(audited_records),
        "top_candidates_count": len(top_candidates),
        "top_actionable_candidates": top_candidates,
        "all_ranked_assets": ranked
    }

    OUTPUT_DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    with open(OUTPUT_DB_PATH, "w", encoding="utf-8") as f:
        json.dump(output_payload, f, indent=2)

    print(f"Saved Cycle_035 Universe Database to {OUTPUT_DB_PATH}")

if __name__ == "__main__":
    main()
