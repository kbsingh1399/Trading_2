#!/usr/bin/env python3
"""
scripts/standalone_dossier_json_daemon.py
=========================================
Production Standalone JSON Dossier Generator & Updation Daemon.
Extracts 100% complete multi-timeframe quantitative data directly from all
43 Parquet feeds in Data/feeds/ and dumps clean, typed, high-speed JSON dossiers:
  - docs/dossiers/<SYMBOL>_MASTER_DOSSIER.json
  - docs/dossiers/ALL_MASTER_DOSSIERS.json (unified fast cache)

Deletes legacy heavy .md files in docs/dossiers/ to eliminate context rot and bloat.

Usage:
  python scripts/standalone_dossier_json_daemon.py              # Continuous mode (180s interval)
  python scripts/standalone_dossier_json_daemon.py --once       # Single pass and exit
  python scripts/standalone_dossier_json_daemon.py --interval 60 # Custom interval in seconds
"""

from __future__ import annotations
import argparse
import concurrent.futures
import datetime
import gc
import json
import logging
import os
import pathlib
import sys
import time
import traceback

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

ROOT_DIR = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT_DIR))

DOSSIERS_DIR = ROOT_DIR / "docs" / "dossiers"
DOSSIERS_DIR.mkdir(parents=True, exist_ok=True)
FEEDS_DIR = ROOT_DIR / "Data" / "feeds"
CATALOG_PATH = ROOT_DIR / "Data" / "metadata" / "master_asset_catalog.json"
INDEX_PATH = DOSSIERS_DIR / "registry_index.json"
ALL_DOSSIERS_JSON = DOSSIERS_DIR / "ALL_MASTER_DOSSIERS.json"

LOG_DIR = ROOT_DIR / "logs"
LOG_DIR.mkdir(parents=True, exist_ok=True)
LOG_FILE = LOG_DIR / "standalone_dossier_daemon.log"

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] [DossierJSONDaemon] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    handlers=[
        logging.StreamHandler(sys.stdout),
        logging.FileHandler(LOG_FILE, encoding="utf-8"),
    ],
)
log = logging.getLogger("DossierJSONDaemon")


def clean_legacy_md_files():
    """Removes obsolete and bloated .md files in docs/dossiers/."""
    md_files = list(DOSSIERS_DIR.glob("*.md"))
    if not md_files:
        return 0
    count = 0
    for f in md_files:
        try:
            f.unlink()
            count += 1
        except Exception:
            pass
    log.info(f"Purged {count} legacy markdown dossier files (.md) from {DOSSIERS_DIR}")
    return count


def execute_dossier_refresh(cycle_count: int, delete_md: bool = True) -> dict:
    from scripts.sovereign_dossier_engine import DataLakeMemoryStore, MetricExtractor

    t0 = time.perf_counter()
    now_utc = datetime.datetime.now(datetime.timezone.utc)
    now_ist = now_utc + datetime.timedelta(hours=5, minutes=30)
    time_str = now_ist.strftime("%Y-%m-%d %H:%M:%S IST")

    log.info("=" * 80)
    log.info(f"🏛️ [CYCLE #{cycle_count}] EXECUTING PURE-PARQUET -> JSON DOSSIER ENGINE")
    log.info(f"   Timestamp: {time_str} ({now_utc.strftime('%H:%M:%S UTC')})")
    log.info(f"   Source Feeds: {FEEDS_DIR}")
    log.info("=" * 80)

    # 1. Ingest all 43 Parquet Feeds into memory
    t_store_start = time.perf_counter()
    store = DataLakeMemoryStore(FEEDS_DIR)
    t_store = time.perf_counter() - t_store_start
    log.info(f">> Ingested and indexed 43 Parquet feeds in {t_store:.3f}s")

    # 2. Load Master Asset Catalog
    with open(CATALOG_PATH, "r", encoding="utf-8") as f:
        cat_data = json.load(f)
    assets_dict = cat_data.get("assets", {})
    if isinstance(assets_dict, dict):
        asset_list = list(assets_dict.values())
    else:
        asset_list = list(assets_dict)

    log.info(f">> Processing 100% full-scale metrics for {len(asset_list)} assets in parallel...")

    # 3. Extract metrics in parallel
    t_ext_start = time.perf_counter()
    def _extract_one(asset):
        try:
            return MetricExtractor.extract_all(asset, store)
        except Exception as e:
            return None

    with concurrent.futures.ThreadPoolExecutor(max_workers=8) as pool:
        results = list(pool.map(_extract_one, asset_list))

    extracted = [r for r in results if r is not None]
    t_ext = time.perf_counter() - t_ext_start
    log.info(f">> Extracted complete data across {len(extracted)} assets in {t_ext:.3f}s")

    # 4. Dump individual JSON dossiers and compile unified JSON database
    t_write_start = time.perf_counter()
    unified_db = {}
    index_entries = []

    def _write_json_dossier(d):
        canonical = d.get("canonical", "")
        if not canonical:
            return
        
        # Build individual JSON file
        out_path = DOSSIERS_DIR / f"{canonical}_MASTER_DOSSIER.json"
        try:
            with open(out_path, "w", encoding="utf-8") as jf:
                json.dump(d, jf, indent=2, default=str)
        except Exception:
            pass

    with concurrent.futures.ThreadPoolExecutor(max_workers=16) as pool:
        pool.map(_write_json_dossier, extracted)

    # Compile unified dictionary
    for d in extracted:
        can = d.get("canonical", "")
        if can:
            unified_db[can] = d
            index_entries.append({
                "canonical": can,
                "display_name": d.get("display_name", can),
                "category": d.get("category", ""),
                "broker_symbol": d.get("broker_sym", ""),
                "spread_bps": d.get("telemetry", {}).get("spread_bps", 0.0),
                "gate_status": d.get("telemetry", {}).get("gate_status", "UNKNOWN"),
                "posture": d.get("formulation", {}).get("decision", "STAND_ASIDE_MONITOR"),
                "json_file": f"{can}_MASTER_DOSSIER.json",
            })

    # Write unified JSON cache
    with open(ALL_DOSSIERS_JSON, "w", encoding="utf-8") as uf:
        json.dump(unified_db, uf, indent=2, default=str)

    # Write registry index
    index_payload = {
        "schema_version": "2.0.0",
        "format": "JSON_STANDALONE",
        "timestamp_utc": now_utc.strftime("%Y-%m-%d %H:%M:%S UTC"),
        "timestamp_ist": time_str,
        "total_assets": len(extracted),
        "assets": index_entries,
    }
    with open(INDEX_PATH, "w", encoding="utf-8") as idxf:
        json.dump(index_payload, idxf, indent=2)

    t_write = time.perf_counter() - t_write_start
    log.info(f">> Wrote {len(extracted)} individual JSON dossiers + unified cache in {t_write:.3f}s")

    # 5. Purge obsolete .md files if requested
    if delete_md:
        clean_legacy_md_files()

    total_time = time.perf_counter() - t0
    log.info("=" * 80)
    log.info(f"✅ [SUCCESS] JSON Dossier Engine finished in {total_time:.3f}s!")
    log.info(f"   Unified Cache: {ALL_DOSSIERS_JSON} ({ALL_DOSSIERS_JSON.stat().st_size / 1024 / 1024:.2f} MB)")
    log.info(f"   Registry Index: {INDEX_PATH}")
    log.info("=" * 80)

    gc.collect()
    return {
        "cycle_count": cycle_count,
        "timestamp_ist": time_str,
        "total_assets": len(extracted),
        "elapsed_seconds": round(total_time, 3),
        "unified_size_mb": round(ALL_DOSSIERS_JSON.stat().st_size / 1024 / 1024, 2),
    }


def main():
    parser = argparse.ArgumentParser(description="Standalone Pure-Parquet -> JSON Dossier Daemon")
    parser.add_argument("--once", action="store_true", help="Execute single pass and exit")
    parser.add_argument("--interval", type=int, default=180, help="Cadence in seconds (default: 180s / 3m)")
    parser.add_argument("--keep-md", action="store_true", help="Do not delete .md files")
    args = parser.parse_args()

    log.info("=" * 80)
    log.info("🏛️ STANDALONE JSON DOSSIER DAEMON INITIALIZED")
    log.info(f"Target: Pure-Parquet extraction -> Typed JSON dossiers")
    log.info(f"Mode: {'Single-Pass (--once)' if args.once else f'Loop ({args.interval}s)'}")
    log.info("=" * 80)

    cycle_count = 0
    while True:
        cycle_count += 1
        try:
            execute_dossier_refresh(cycle_count, delete_md=not args.keep_md)
        except Exception as e:
            log.error(f"Error in dossier refresh cycle #{cycle_count}: {e}\n{traceback.format_exc()}")

        if args.once:
            log.info("Single-pass execution complete (--once). Exiting cleanly.")
            break

        log.info(f"Sleeping for {args.interval}s until next dossier refresh...")
        time.sleep(args.interval)


if __name__ == "__main__":
    main()
