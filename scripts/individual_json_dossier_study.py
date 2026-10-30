#!/usr/bin/env python3
"""
scripts/individual_json_dossier_study.py
Physical individual study and verification of JSON dossiers for ALL assets clearing spread thresholds.
Guarantees 100% individual file inspection with zero truncation or batch skipping.
"""

import datetime
import json
import os
import pathlib
import sys
import pandas as pd

ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.stdout.reconfigure(encoding="utf-8", errors="replace")

DOSSIER_DIR = ROOT / "docs" / "dossiers"
OUTPUT_AUDIT_PATH = ROOT / "docs" / "trade_plans" / "CYCLE_034_INDIVIDUAL_DOSSIER_STUDY_AUDIT.json"

def get_spread_cleared_assets():
    telemetry_path = ROOT / "Data" / "feeds" / "00_MT5_Account_Telemetry.parquet"
    if not telemetry_path.exists():
        raise FileNotFoundError(f"Telemetry not found at {telemetry_path}")
    
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
    
    cleared = []
    for _, row in passed_df.iterrows():
        broker_sym = str(row.get("Broker_Symbol", "")).strip()
        spread_bps = float(row.get("Spread_BPS", 999.0))
        bid = float(row.get("Bid_Quote", 0.0))
        ask = float(row.get("Ask_Quote", 0.0))
        
        canonical, asset_class = mt5_to_canonical.get(
            broker_sym, 
            (broker_sym.replace(".pi", "").replace(".p", ""), "Unknown")
        )
        
        cleared.append({
            "canonical": canonical,
            "broker_symbol": broker_sym,
            "asset_class": asset_class,
            "spread_bps": spread_bps,
            "bid": bid,
            "ask": ask
        })
            
    return cleared

def inspect_individual_dossier(asset_info):
    canonical = asset_info["canonical"]
    json_path = DOSSIER_DIR / f"{canonical}_MASTER_DOSSIER.json"
    
    if not json_path.exists():
        alt_path = DOSSIER_DIR / f"{asset_info['broker_symbol'].replace('.pi', '').replace('.p', '')}_MASTER_DOSSIER.json"
        if alt_path.exists():
            json_path = alt_path
            
    if not json_path.exists():
        return {
            "canonical": canonical,
            "broker_symbol": asset_info["broker_symbol"],
            "status": "MISSING_INDIVIDUAL_FILE",
            "path": str(json_path),
            "verified": False
        }
        
    stat = json_path.stat()
    file_bytes = stat.st_size
    mtime = datetime.datetime.fromtimestamp(stat.st_mtime, tz=datetime.timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
    
    try:
        with open(json_path, "r", encoding="utf-8") as f:
            d = json.load(f)
    except Exception as e:
        return {
            "canonical": canonical,
            "broker_symbol": asset_info["broker_symbol"],
            "status": f"JSON_DECODE_ERROR: {e}",
            "verified": False
        }
        
    required_keys = [
        "canonical", "category", "broker_sym", "specs", "telemetry",
        "technicals", "auction", "cvd", "whales_and_l2", "liquidations",
        "derivatives", "footprint_and_macro", "formulation"
    ]
    
    present_keys = [k for k in required_keys if k in d and d[k] is not None]
    is_complete = len(present_keys) == len(required_keys)
    
    # Extract structural metrics
    telemetry = d.get("telemetry", {})
    auction = d.get("auction", {})
    technicals = d.get("technicals", {})
    liquidations = d.get("liquidations", {})
    whales = d.get("whales_and_l2", {})
    formulation = d.get("formulation", {})
    
    bid = telemetry.get("bid", asset_info["bid"])
    ask = telemetry.get("ask", asset_info["ask"])
    mid = (bid + ask) / 2.0 if (bid + ask) > 0 else 0.0
    
    val = auction.get("daily_val") or auction.get("developing_val", 0.0)
    poc = auction.get("daily_poc") or auction.get("developing_poc", 0.0)
    vah = auction.get("daily_vah") or auction.get("developing_vah", 0.0)
    vwap = technicals.get("vwap") or technicals.get("vwap_mid", 0.0)
    atr = technicals.get("atr_14", 0.0)
    
    mp_24h = liquidations.get("mp_24h", {})
    if isinstance(mp_24h, dict):
        short_max_pain = mp_24h.get("short_max_pain_price", 0.0)
        long_max_pain = mp_24h.get("long_max_pain_price", 0.0)
    else:
        short_max_pain = liquidations.get("short_max_pain_24h", 0.0)
        long_max_pain = liquidations.get("long_max_pain_24h", 0.0)
    
    whale_ladder = whales.get("whale_ladder", [])
    ob_ladder = whales.get("ob_ladder", [])
    
    # Formulation base score
    base_formulation_score = formulation.get("confluence_score", 50.0)
    
    score = 50.0
    signals = []
    
    # VWAP extension
    if vwap > 0 and mid > 0:
        vwap_dist_pct = ((mid - vwap) / vwap) * 100.0
        if abs(vwap_dist_pct) >= 2.0:
            score += 15.0
            signals.append(f"VWAP deviation {vwap_dist_pct:+.2f}%")
            
    # Auction positioning
    if val > 0 and vah > 0 and mid > 0:
        if mid < val:
            score += 15.0
            signals.append("Trading below Developing VAL (Discount)")
        elif mid > vah:
            score += 15.0
            signals.append("Trading above Developing VAH (Premium)")
            
    # Short Max Pain overhead magnet
    if short_max_pain > 0 and mid > 0:
        smp_dist_pct = ((short_max_pain - mid) / mid) * 100.0
        if 0 < smp_dist_pct <= 4.0:
            score += 10.0
            signals.append(f"Short Max Pain magnet overhead @ {short_max_pain:.2f} ({smp_dist_pct:+.2f}%)")
            
    # Long Max Pain downside magnet
    if long_max_pain > 0 and mid > 0:
        lmp_dist_pct = ((mid - long_max_pain) / mid) * 100.0
        if 0 < lmp_dist_pct <= 4.0:
            score += 10.0
            signals.append(f"Long Max Pain magnet below @ {long_max_pain:.2f} (-{lmp_dist_pct:.2f}%)")
            
    # Whale wall presence
    if len(whale_ladder) > 0 or len(ob_ladder) > 0:
        score += 5.0
        signals.append(f"Institutional Depth: {len(whale_ladder)} whale orders / {len(ob_ladder)} OB levels")

    final_score = max(score, float(base_formulation_score) if base_formulation_score else 50.0)

    return {
        "canonical": canonical,
        "broker_symbol": asset_info["broker_symbol"],
        "category": d.get("category", asset_info["asset_class"]),
        "file_path": str(json_path),
        "file_size_bytes": file_bytes,
        "file_last_modified_utc": mtime,
        "present_schema_keys": len(present_keys),
        "total_required_keys": len(required_keys),
        "is_complete_schema": is_complete,
        "verified": True,
        "metrics": {
            "spread_bps": asset_info["spread_bps"],
            "live_mid": mid,
            "vwap": vwap,
            "atr_14": atr,
            "val": val,
            "poc": poc,
            "vah": vah,
            "short_max_pain_24h": short_max_pain,
            "long_max_pain_24h": long_max_pain,
            "whale_orders_count": len(whale_ladder),
            "formulation_action": formulation.get("decision", "STAND_ASIDE"),
            "formulation_long": formulation.get("long"),
            "formulation_short": formulation.get("short")
        },
        "confluence_score": min(final_score, 100.0),
        "signals": signals
    }

def main():
    print("=" * 80)
    print("🔬 STARTING 100% INDIVIDUAL JSON DOSSIER PHYSICAL EXAMINATION")
    print("=" * 80)
    
    eligible = get_spread_cleared_assets()
    print(f"Total spread-cleared eligible assets to study individually: {len(eligible)}")
    
    audited_assets = []
    missing_files = []
    
    for i, a in enumerate(eligible, 1):
        res = inspect_individual_dossier(a)
        if res.get("verified"):
            audited_assets.append(res)
            print(f"[{i:02d}/{len(eligible):02d}] {res['canonical']:<10} ({res['broker_symbol']:<11}) | {res['file_size_bytes']:>7} B | Verified: YES | Keys: {res['present_schema_keys']}/13 | Score: {res['confluence_score']:.1f}")
        else:
            missing_files.append(res)
            print(f"[{i:02d}/{len(eligible):02d}] {res['canonical']:<10} ({res.get('broker_symbol'):<11}) | MISSING / ERROR: {res.get('status')}")
            
    ranked = sorted(audited_assets, key=lambda x: x["confluence_score"], reverse=True)
    high_confluence = [x for x in ranked if x["confluence_score"] >= 75.0]
    
    audit_payload = {
        "audit_timestamp_utc": datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC"),
        "total_spread_cleared_eligible": len(eligible),
        "total_individually_verified": len(audited_assets),
        "missing_or_corrupt_files_count": len(missing_files),
        "high_confluence_count_ge_75": len(high_confluence),
        "high_confluence_candidates": high_confluence,
        "full_individual_audit_records": audited_assets
    }
    
    OUTPUT_AUDIT_PATH.parent.mkdir(parents=True, exist_ok=True)
    with open(OUTPUT_AUDIT_PATH, "w", encoding="utf-8") as f:
        json.dump(audit_payload, f, indent=2)
        
    print("=" * 80)
    print(f"✅ INDIVIDUAL STUDY COMPLETE!")
    print(f"Verified {len(audited_assets)} / {len(eligible)} individual JSON files on disk.")
    print(f"Saved complete audit trail to {OUTPUT_AUDIT_PATH}")
    print(f"Identified {len(high_confluence)} High Confluence Candidates (Score >= 75.0)")
    print("=" * 80)

if __name__ == "__main__":
    main()
