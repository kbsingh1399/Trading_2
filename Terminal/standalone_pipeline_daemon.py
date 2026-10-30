#!/usr/bin/env python3
"""
Terminal/standalone_pipeline_daemon.py
======================================
Production-Grade Standalone Data Pipeline Daemon for Trading_2.
Continuously runs all quantitative collectors (Pure-API + Browser + Telemetry),
dumping and maintaining 100% fresh data across all 43 canonical Parquet feeds in Data/feeds/.

Usage:
  python Terminal/standalone_pipeline_daemon.py               # Continuous mode (120s interval)
  python Terminal/standalone_pipeline_daemon.py --once        # Single run and exit
  python Terminal/standalone_pipeline_daemon.py --api-only    # High-velocity API feeds only (< 15s)
  python Terminal/standalone_pipeline_daemon.py --interval 60 # Custom interval in seconds
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
import subprocess
import sys
import time
import traceback

ROOT_DIR = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT_DIR))

FEEDS_DIR = ROOT_DIR / "Data" / "feeds"
FEEDS_DIR.mkdir(parents=True, exist_ok=True)
LOG_DIR = ROOT_DIR / "logs"
LOG_DIR.mkdir(parents=True, exist_ok=True)

STATUS_FILE = ROOT_DIR / "Data" / "pipeline_daemon_status.json"
LOG_FILE = LOG_DIR / "standalone_pipeline_daemon.log"

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] [StandalonePipeline] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    handlers=[
        logging.StreamHandler(sys.stdout),
        logging.FileHandler(LOG_FILE, encoding="utf-8"),
    ],
)
log = logging.getLogger("StandalonePipeline")

API_COLLECTORS = [
    "00_MT5_Account_Telemetry.py",
    "11_Technical.py",
    "12_Hyperdash.py",
    "13_Hyperliquid.py",
    "14_Hyperdash_Liq_Map.py",
    "15_Hyperdash_Stops_Map.py",
    "16_Hyperdash_telegram_Intel.py",
    "17_Orderbook.py",
    "18_CVD.py",
    "20_Auction_Market_Structure.py",
    "21_Tradfye_Orderflow.py",
    "22_Forced_Liquidations_MTF.py",
]

BROWSER_COLLECTORS = [
    "1_Crypto_ETF_Flows.py",
    "2_Spot_Netflow_S.py",
    "2_Future_Netflow.py",
    "3_Exchanges_LS_Ratio_15M.py",
    "3_Exchanges_LS_Ratio_1H.py",
    "3_Exchanges_LS_Ratio_4H.py",
    "4_Hyperliquid_Analysis.py",
    "5_OI.py",
    "5_Funding_Rate.py",
    "6_Funding_Fee_Settlement.py",
    "7_Liq_Heapmap.py",
    "7_Live_Liq.py",
    "8_Exchange_Liquidation_Map_1D.py",
    "8_Exchange_Liquidation_Map_7D.py",
    "9_Liquidation_Max_Pain_24H.py",
    "9_Liquidation_Max_Pain_48H.py",
    "9_Liquidation_Max_Pain_3D.py",
    "9_Liquidation_Max_Pain_7D.py",
    "10_Whale_Orders.py",
    "19_News.py",
    "19_Calendar.py",
    "25_CoinGlass_Footprint_Signals.py",
    "26_Aggregated_Footprint_Bar_Metrics.py",
]

def run_collector(script_path: pathlib.Path, timeout: int = 120) -> tuple[str, bool, float, str]:
    t0 = time.perf_counter()
    name = script_path.name
    try:
        proc = subprocess.run(
            [sys.executable, str(script_path)],
            cwd=str(ROOT_DIR),
            capture_output=True,
            text=True,
            timeout=timeout,
        )
        dt = time.perf_counter() - t0
        success = (proc.returncode == 0)
        err = proc.stderr.strip() if not success else ""
        return name, success, dt, err
    except subprocess.TimeoutExpired:
        dt = time.perf_counter() - t0
        return name, False, dt, f"Timed out after {timeout}s"
    except Exception as e:
        dt = time.perf_counter() - t0
        return name, False, dt, str(e)

def execute_pipeline_cycle(cycle_id: int, api_only: bool = False) -> dict:
    t_start = time.perf_counter()
    now_utc = datetime.datetime.now(datetime.timezone.utc)
    now_ist = now_utc + datetime.timedelta(hours=5, minutes=30)
    log.info("=" * 80)
    log.info(f"🚀 [CYCLE #{cycle_id}] EXECUTING STANDALONE DATA PIPELINE")
    log.info(f"   Time: {now_ist.strftime('%Y-%m-%d %H:%M:%S IST')} ({now_utc.strftime('%H:%M:%S UTC')})")
    log.info(f"   Mode: {'Pure-API Only' if api_only else 'Full Multi-Feed (API + Browser)'}")
    log.info("=" * 80)

    results = {}
    passed = 0
    failed = 0

    # Phase 1: Pure-API Collectors
    api_dir = ROOT_DIR / "Collectors" / "API"
    api_scripts = [api_dir / s for s in API_COLLECTORS if (api_dir / s).exists()]
    log.info(f">> Phase 1: Executing {len(api_scripts)} Pure-API Collectors in parallel...")
    with concurrent.futures.ThreadPoolExecutor(max_workers=6) as executor:
        futures = {executor.submit(run_collector, s, 90): s.name for s in api_scripts}
        for f in concurrent.futures.as_completed(futures):
            name, ok, dt, err = f.result()
            results[name] = {"success": ok, "elapsed": round(dt, 2), "error": err}
            if ok:
                passed += 1
                log.info(f"   [API] {name:<35} PASS ({dt:.2f}s)")
            else:
                failed += 1
                log.error(f"   [API] {name:<35} FAIL ({dt:.2f}s) - {err[:120]}")

    # Phase 2: Browser CDP Collectors
    if not api_only:
        browser_dir = ROOT_DIR / "Collectors" / "Browser"
        browser_scripts = [browser_dir / s for s in BROWSER_COLLECTORS if (browser_dir / s).exists()]
        log.info(f">> Phase 2: Executing {len(browser_scripts)} Browser Collectors...")
        for s in browser_scripts:
            name, ok, dt, err = run_collector(s, 120)
            results[name] = {"success": ok, "elapsed": round(dt, 2), "error": err}
            if ok:
                passed += 1
                log.info(f"   [BROWSER] {name:<35} PASS ({dt:.2f}s)")
            else:
                failed += 1
                log.warning(f"   [BROWSER] {name:<35} FAIL/WARN ({dt:.2f}s) - {err[:120]}")

    # Phase 3: Telemetry & Parquet Audit
    auditor_script = ROOT_DIR / "Terminal" / "parquet_checklist_auditor.py"
    if auditor_script.exists():
        run_collector(auditor_script, 60)

    elapsed_total = time.perf_counter() - t_start
    parquet_files = list(FEEDS_DIR.glob("*.parquet"))
    log.info(f"✅ [CYCLE #{cycle_id}] Completed in {elapsed_total:.2f}s | Passed: {passed} | Failed: {failed} | Active Feeds: {len(parquet_files)}")

    status_data = {
        "cycle_id": cycle_id,
        "last_updated_utc": now_utc.strftime("%Y-%m-%d %H:%M:%S UTC"),
        "last_updated_ist": now_ist.strftime("%Y-%m-%d %H:%M:%S IST"),
        "elapsed_seconds": round(elapsed_total, 2),
        "total_collectors": len(results),
        "passed": passed,
        "failed": failed,
        "parquet_feeds_count": len(parquet_files),
        "api_only": api_only,
    }
    try:
        STATUS_FILE.write_text(json.dumps(status_data, indent=2), encoding="utf-8")
    except Exception:
        pass

    gc.collect()
    return status_data

def main():
    parser = argparse.ArgumentParser(description="Standalone Pure-Parquet Pipeline Daemon")
    parser.add_argument("--once", action="store_true", help="Execute single cycle and exit")
    parser.add_argument("--api-only", action="store_true", help="Execute only high-speed pure-API collectors")
    parser.add_argument("--interval", type=int, default=120, help="Cadence gap between cycles in seconds (default: 120s)")
    args = parser.parse_args()

    log.info("=" * 80)
    log.info("🏛️ STANDALONE PARQUET DATA PIPELINE DAEMON INITIALIZED")
    log.info(f"Mode: {'Single-Pass (--once)' if args.once else f'Continuous Loop ({args.interval}s interval)'}")
    log.info(f"Data Feeds Directory: {FEEDS_DIR}")
    log.info("=" * 80)

    cycle_count = 0
    while True:
        cycle_count += 1
        try:
            execute_pipeline_cycle(cycle_count, api_only=args.api_only)
        except Exception as e:
            log.error(f"Unhandled exception in pipeline cycle #{cycle_count}: {e}\n{traceback.format_exc()}")

        if args.once:
            log.info("Single-pass execution complete (--once). Exiting cleanly.")
            break

        log.info(f"Sleeping for {args.interval}s until next pipeline cycle...")
        time.sleep(args.interval)

if __name__ == "__main__":
    main()
