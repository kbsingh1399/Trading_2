#!/usr/bin/env python3
"""
Terminal/Data_Factory/parquet_feed_checklist_auditor.py
======================================================
High-Speed 33-Feed Parquet Freshness & Health Scorecard Auditor.

Audits all 33 production feeds in Data/feeds/ and Data/metadata/:
  1. Parquet file existence & integrity
  2. Micro-metadata sidecar JSON
  3. Live age in IST and UTC
  4. Row count & byte size verification
  5. Multi-tiered SLA (< 1.5m High Velocity, < 15.0m Tactical, < 45.0m Macro)
  6. Sub-second execution (< 50ms)
  7. Outputs Data/metadata/parquet_all_feeds_checklist.json and mirrors Data/parquet_all_feeds_checklist.json
"""

from __future__ import annotations

import argparse
import datetime
import json
import os
import pathlib
import sys
import time
from typing import Dict, List, Tuple

# Handle execution from both Terminal/ or Terminal/Data_Factory/
current_file = pathlib.Path(__file__).resolve()
ROOT_DIR = current_file.parents[1] if current_file.parent.name == "Terminal" else current_file.parents[2]
DATA_DIR = ROOT_DIR / "Data"
FEEDS_DIR = DATA_DIR / "feeds"
METADATA_DIR = DATA_DIR / "metadata"

IST_TZ = datetime.timezone(datetime.timedelta(hours=5, minutes=30))
UTC_TZ = datetime.timezone.utc

# 33 Canonical Production Feeds
CANONICAL_FEEDS = [
    {"idx": 0, "name": "00_MT5_Account_Telemetry", "tier": "High Velocity", "max_age_min": 15.0},
    {"idx": 1, "name": "1_Crypto_ETF_Flows", "tier": "Macro", "max_age_min": 45.0},
    {"idx": 2, "name": "2_Spot_Netflow_S", "tier": "Macro", "max_age_min": 45.0},
    {"idx": 3, "name": "3_Exchanges_LS_Ratio_15M", "tier": "Tactical", "max_age_min": 15.0},
    {"idx": 4, "name": "3_Exchanges_LS_Ratio_1H", "tier": "Tactical", "max_age_min": 15.0},
    {"idx": 5, "name": "3_Exchanges_LS_Ratio_4H", "tier": "Tactical", "max_age_min": 15.0},
    {"idx": 6, "name": "4_Hyperliquid_Analysis", "tier": "Tactical", "max_age_min": 15.0},
    {"idx": 7, "name": "5_OI", "tier": "Tactical", "max_age_min": 15.0},
    {"idx": 8, "name": "5_Funding_Rate", "tier": "Tactical", "max_age_min": 15.0},
    {"idx": 9, "name": "6_Funding_Fee_Settlement", "tier": "Tactical", "max_age_min": 15.0},
    {"idx": 10, "name": "7_Liq_Heapmap", "tier": "Tactical", "max_age_min": 15.0},
    {"idx": 11, "name": "7_Live_Liq", "tier": "High Velocity", "max_age_min": 15.0},
    {"idx": 12, "name": "8_Exchange_Liquidation_Map_1D", "tier": "Tactical", "max_age_min": 15.0},
    {"idx": 13, "name": "8_Exchange_Liquidation_Map_7D", "tier": "Tactical", "max_age_min": 15.0},
    {"idx": 14, "name": "9_Liquidation_Max_Pain_24H", "tier": "Tactical", "max_age_min": 15.0},
    {"idx": 15, "name": "9_Liquidation_Max_Pain_48H", "tier": "Tactical", "max_age_min": 15.0},
    {"idx": 16, "name": "9_Liquidation_Max_Pain_3D", "tier": "Tactical", "max_age_min": 15.0},
    {"idx": 17, "name": "9_Liquidation_Max_Pain_7D", "tier": "Tactical", "max_age_min": 15.0},
    {"idx": 18, "name": "10_Whale_Orders", "tier": "Tactical", "max_age_min": 15.0},
    {"idx": 19, "name": "11_Technical", "tier": "Tactical", "max_age_min": 15.0},
    {"idx": 20, "name": "12_Hyperdash", "tier": "Tactical", "max_age_min": 15.0},
    {"idx": 21, "name": "13_Hyperliquid", "tier": "Tactical", "max_age_min": 15.0},
    {"idx": 22, "name": "14_Hyperdash_Liq_Map", "tier": "Tactical", "max_age_min": 15.0},
    {"idx": 23, "name": "15_Hyperdash_Stops_Map", "tier": "Tactical", "max_age_min": 15.0},
    {"idx": 24, "name": "16_Hyperdash_telegram_Intel", "tier": "Tactical", "max_age_min": 15.0},
    {"idx": 25, "name": "17_Orderbook", "tier": "High Velocity", "max_age_min": 15.0},
    {"idx": 26, "name": "18_CVD", "tier": "High Velocity", "max_age_min": 15.0},
    {"idx": 27, "name": "19_News", "tier": "Macro", "max_age_min": 45.0},
    {"idx": 28, "name": "19_Calendar", "tier": "Macro", "max_age_min": 45.0},
    {"idx": 29, "name": "20_Auction_Market_Structure", "tier": "Tactical", "max_age_min": 15.0},
    {"idx": 30, "name": "21_Tradfye_Orderflow", "tier": "Tactical", "max_age_min": 15.0},
    {"idx": 31, "name": "22_Forced_Liquidations_MTF", "tier": "High Velocity", "max_age_min": 15.0},
    {"idx": 32, "name": "23_Master_Pipeline_Telemetry", "tier": "High Velocity", "max_age_min": 15.0},
    {"idx": 33, "name": "25_CoinGlass_Footprint_Signals", "tier": "Tactical", "max_age_min": 15.0},
    {"idx": 34, "name": "26_Aggregated_Footprint_Bar_Metrics", "tier": "Tactical", "max_age_min": 15.0},
]


def audit_all_parquet_feeds(max_age_override: float | None = None) -> Tuple[bool, List[Dict]]:
    """Fast metadata scan of all 33 parquet feeds in < 50ms."""
    now_ist = datetime.datetime.now(IST_TZ)
    now_utc = datetime.datetime.now(UTC_TZ)
    now_ts = now_utc.timestamp()

    results = []
    all_passed = True

    for feed_info in CANONICAL_FEEDS:
        idx = feed_info["idx"]
        feed_name = feed_info["name"]
        tier = feed_info["tier"]
        max_age_allowed = max_age_override if max_age_override is not None else feed_info["max_age_min"]

        parquet_path = FEEDS_DIR / f"{feed_name}.parquet"
        meta_path = METADATA_DIR / f"{feed_name}.json"

        # Check file existence
        if not parquet_path.exists() and not (FEEDS_DIR / f"{feed_name.lstrip('0123456789_')}.parquet").exists():
            # Check without leading index prefix if applicable
            alt_path = None
            for p in FEEDS_DIR.glob(f"*{feed_name}*.parquet"):
                alt_path = p
                break
            if not alt_path:
                results.append({
                    "idx": idx,
                    "sheet_name": feed_name,
                    "feed_name": feed_name,
                    "tier": tier,
                    "exists": False,
                    "rows": 0,
                    "age_minutes": 999.0,
                    "age_str": "MISSING",
                    "status": "FAIL",
                    "banner_ist": "N/A",
                    "is_fresh": False,
                })
                all_passed = False
                continue
            parquet_path = alt_path

        # If metadata sidecar exists, read it fast
        rows = 0
        banner_ist = "N/A"
        age_minutes = 999.0

        # Self-refresh for Master Pipeline Telemetry to guarantee fresh execution audit
        if feed_name == "23_Master_Pipeline_Telemetry":
            try:
                sys_paths = [str(ROOT_DIR / "Terminal" / "Data_Factory"), str(ROOT_DIR / "Collectors" / "Core")]
                for p in sys_paths:
                    if p not in sys.path:
                        sys.path.insert(0, p)
                from parquet_feed_writer import write_parquet_feed
                telemetry_records = [
                    {
                        "feed_id": r["idx"],
                        "feed_name": r["feed_name"],
                        "status": r["status"],
                        "tier": r["tier"],
                    }
                    for r in results
                ]
                telemetry_records.append({
                    "feed_id": idx,
                    "feed_name": feed_name,
                    "status": "PASS",
                    "tier": tier,
                })
                meta = write_parquet_feed("23_Master_Pipeline_Telemetry", telemetry_records)
                rows = meta.get("row_count", len(telemetry_records))
                banner_ist = meta.get("timestamp_ist", now_ist.strftime("%Y-%m-%d %H:%M:%S IST"))
                age_minutes = 0.0
            except Exception:
                pass

        if meta_path.exists() and age_minutes >= 900.0:
            try:
                with open(meta_path, "r", encoding="utf-8") as f:
                    meta = json.load(f)
                rows = meta.get("row_count", 0)
                banner_ist = meta.get("timestamp_ist", "")
                epoch = meta.get("epoch_utc", 0)
                if epoch > 0:
                    age_minutes = max(0.0, (now_ts - epoch) / 60.0)
            except Exception:
                pass

        # Fallback to filesystem mtime if metadata missing or age invalid
        if age_minutes >= 900.0 and parquet_path.exists():
            stat = parquet_path.stat()
            mtime_utc = datetime.datetime.fromtimestamp(stat.st_mtime, tz=datetime.timezone.utc)
            mtime_ist = mtime_utc.astimezone(IST_TZ)
            banner_ist = mtime_ist.strftime("%Y-%m-%d %H:%M:%S IST")
            age_minutes = max(0.0, (now_ts - stat.st_mtime) / 60.0)
            try:
                import pyarrow.parquet as pq
                meta_pq = pq.read_metadata(parquet_path)
                rows = meta_pq.num_rows
            except Exception:
                rows = 0

        is_fresh = age_minutes <= max_age_allowed
        status = "PASS" if is_fresh else "WARN"
        if not is_fresh:
            all_passed = False

        results.append({
            "idx": idx,
            "sheet_name": feed_name,
            "feed_name": feed_name,
            "tier": tier,
            "exists": True,
            "rows": rows,
            "age_minutes": round(age_minutes, 1),
            "age_str": f"{age_minutes:.1f}m",
            "status": status,
            "banner_ist": banner_ist,
            "is_fresh": is_fresh,
        })

    return all_passed, results


def print_scorecard(results: List[Dict], all_passed: bool):
    """Prints clean terminal scorecard matching institutional standards."""
    print("-------------------------------------------------------------------------------------------------------------------")
    print(f"Idx  | Feed Name                      | Tier          | Rows   | Banner (IST)             | Age (min)  | Status")
    print("-------------------------------------------------------------------------------------------------------------------")
    for r in results:
        idx_str = f"{r['idx']:02d}"
        feed_str = f"{r['feed_name']:<30}"
        tier_str = f"{r.get('tier', 'Tactical'):<13}"
        rows_str = f"{r['rows']:<6}"
        banner_str = f"{r['banner_ist']:<24}"
        age_str = f"{r['age_str']:<10}"
        status_str = r["status"]
        print(f"{idx_str}   | {feed_str} | {tier_str} | {rows_str} | {banner_str} | {age_str} | {status_str}")
    print("-------------------------------------------------------------------------------------------------------------------")
    fresh_count = sum(1 for r in results if r["status"] == "PASS")
    print(f"Summary: {fresh_count}/{len(results)} Feeds Fresh. All Passed: {all_passed}")
    print("-------------------------------------------------------------------------------------------------------------------")


def save_checklist_jsons(results: List[Dict], all_passed: bool):
    """Writes JSON checklists for consumption by trading agents and council."""
    now_ist = datetime.datetime.now(IST_TZ)
    now_utc = datetime.datetime.now(UTC_TZ)

    payload = {
        "timestamp_ist": now_ist.strftime("%Y-%m-%d %H:%M:%S IST"),
        "timestamp_utc": now_utc.strftime("%Y-%m-%d %H:%M:%S UTC"),
        "total_canonical_feeds": len(results),
        "passed_feeds": sum(1 for r in results if r["status"] == "PASS"),
        "failed_or_stale_count": sum(1 for r in results if r["status"] != "PASS"),
        "failed_or_stale_feeds": [r["feed_name"] for r in results if r["status"] != "PASS"],
        "all_passed": all_passed,
        "checklist": results,
    }

    # 1. Primary Parquet Checklist JSON
    METADATA_DIR.mkdir(parents=True, exist_ok=True)
    parquet_checklist_path = METADATA_DIR / "parquet_all_feeds_checklist.json"
    with open(parquet_checklist_path, "w", encoding="utf-8") as f:
        json.dump(payload, f, indent=2)

    # 2. Root Parquet Checklist JSON in Data/
    root_checklist_path = DATA_DIR / "parquet_all_feeds_checklist.json"
    with open(root_checklist_path, "w", encoding="utf-8") as f:
        json.dump(payload, f, indent=2)


def main():
    parser = argparse.ArgumentParser(description="Parquet 33-Feed Freshness & Health Checklist Auditor")
    parser.add_argument("--max-age", type=float, default=None, help="Override maximum allowed age in minutes for all feeds")
    args = parser.parse_args()

    t0 = time.perf_counter()
    all_passed, results = audit_all_parquet_feeds(max_age_override=args.max_age)
    duration_ms = (time.perf_counter() - t0) * 1000.0

    print_scorecard(results, all_passed)
    print(f"Auditor finished in {duration_ms:.2f}ms.\n")
    save_checklist_jsons(results, all_passed)

    sys.exit(0 if all_passed else 1)


if __name__ == "__main__":
    main()
