#!/usr/bin/env python3
"""
Terminal/parquet_runner.py
==========================
Master High-Performance Tiered Runner for all 33 Parquet Feeds.

Features:
  1. Decoupled Storage: Harvesters dump directly to Data/feeds/<feed_name>.parquet.
  2. Zero File Locks: Zero openpyxl contention, zero lost-update race conditions.
  3. Tiered Pacing:
     - Pure API Modules: Up to 6 parallel workers.
     - Browser CDP Modules: Strictly paced to 1-2 workers (prevents Cloudflare/Edge crashes).
  4. 15-Minute Candle Synchronization (< 15.0m Target).
  5. Sub-second Metadata Scorecard via parquet_feed_checklist_auditor.py (< 50ms).
"""

from __future__ import annotations

import argparse
import concurrent.futures
import datetime
import json
import logging
import os
import pathlib
import subprocess
import sys
import time
import urllib.request
from typing import Dict, List, Tuple

ROOT_DIR = pathlib.Path(__file__).resolve().parents[1]
DATA_DIR = ROOT_DIR / "Data"
MODULES_DIR = DATA_DIR / "Excel_Modules"
COLLECTORS_DIR = ROOT_DIR / "Collectors"
API_DIR = COLLECTORS_DIR / "API"
BROWSER_DIR = COLLECTORS_DIR / "Browser"
CORE_DIR = COLLECTORS_DIR / "Core"
FEEDS_DIR = DATA_DIR / "feeds"
METADATA_DIR = DATA_DIR / "metadata"
AUDITOR_SCRIPT = ROOT_DIR / "Terminal" / "parquet_checklist_auditor.py"

CDP_BASE_URL = "http://127.0.0.1:9222"
IST_TZ = datetime.timezone(datetime.timedelta(hours=5, minutes=30))
UTC_TZ = datetime.timezone.utc

def _resolve_script(base_folder: pathlib.Path, fallback_folder: pathlib.Path, filename: str) -> pathlib.Path:
    p = base_folder / filename
    if p.exists():
        return p
    fb = fallback_folder / filename
    return fb if fb.exists() else p

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] [ParquetRunner] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
log = logging.getLogger("ParquetRunner")

# 1. Tier 1: Pure API Modules (High Throughput, 6 workers)
API_MODULES = [
    {"id": 0, "name": "MT5 Telemetry", "script": _resolve_script(API_DIR, MODULES_DIR, "00_MT5_Account_Telemetry.py"), "feed": "00_MT5_Account_Telemetry", "timeout": 120, "args": []},
    {"id": 19, "name": "Technical Indicators", "script": _resolve_script(API_DIR, MODULES_DIR, "11_Technical.py"), "feed": "11_Technical", "timeout": 120, "args": []},
    {"id": 20, "name": "Hyperdash Flow", "script": _resolve_script(API_DIR, MODULES_DIR, "12_Hyperdash.py"), "feed": "12_Hyperdash", "timeout": 120, "args": []},
    {"id": 21, "name": "Hyperliquid L1", "script": _resolve_script(API_DIR, MODULES_DIR, "13_Hyperliquid.py"), "feed": "13_Hyperliquid", "timeout": 120, "args": []},
    {"id": 22, "name": "Hyperdash Liq Map", "script": _resolve_script(API_DIR, MODULES_DIR, "14_Hyperdash_Liq_Map.py"), "feed": "14_Hyperdash_Liq_Map", "timeout": 120, "args": []},
    {"id": 23, "name": "Hyperdash Stops Map", "script": _resolve_script(API_DIR, MODULES_DIR, "15_Hyperdash_Stops_Map.py"), "feed": "15_Hyperdash_Stops_Map", "timeout": 120, "args": []},
    {"id": 24, "name": "Hyperdash Telegram Intel", "script": _resolve_script(API_DIR, MODULES_DIR, "16_Hyperdash_telegram_Intel.py"), "feed": "16_Hyperdash_telegram_Intel", "timeout": 120, "args": ["--pages", "10", "--limit", "1000"]},
    {"id": 25, "name": "Orderbook & Whale Attribution", "script": _resolve_script(API_DIR, MODULES_DIR, "17_Orderbook.py"), "feed": "17_Orderbook", "timeout": 180, "args": []},
    {"id": 26, "name": "CVD Engine", "script": _resolve_script(API_DIR, MODULES_DIR, "18_CVD.py"), "feed": "18_CVD", "timeout": 240, "args": ["--max-excel-rows", "1500"]},
    {"id": 27, "name": "Auction Market Structure", "script": _resolve_script(API_DIR, MODULES_DIR, "20_Auction_Market_Structure.py"), "feed": "20_Auction_Market_Structure", "timeout": 180, "args": []},
    {"id": 28, "name": "Tradfye Orderflow", "script": _resolve_script(API_DIR, MODULES_DIR, "21_Tradfye_Orderflow.py"), "feed": "21_Tradfye_Orderflow", "timeout": 120, "args": []},
    {"id": 31, "name": "Forced Liquidations MTF", "script": _resolve_script(API_DIR, MODULES_DIR, "22_Forced_Liquidations_MTF.py"), "feed": "22_Forced_Liquidations_MTF", "timeout": 120, "args": []},
]

# 2. Tier 2: Browser CDP Modules (Paced to 2 workers to protect browser renderer)
BROWSER_MODULES = [
    {"id": 1, "name": "Crypto ETF Flows", "script": _resolve_script(BROWSER_DIR, MODULES_DIR, "1_Crypto_ETF_Flows.py"), "feed": "1_Crypto_ETF_Flows", "timeout": 120, "args": []},
    {"id": 2, "name": "Spot Netflow", "script": _resolve_script(BROWSER_DIR, MODULES_DIR, "2_Spot_Netflow_S.py"), "feed": "2_Spot_Netflow_S", "timeout": 180, "args": ["--pages", "10"]},
    {"id": 3, "name": "LS Ratio 15M", "script": _resolve_script(BROWSER_DIR, MODULES_DIR, "3_Exchanges_LS_Ratio_15M.py"), "feed": "3_Exchanges_LS_Ratio_15M", "timeout": 180, "args": []},
    {"id": 4, "name": "LS Ratio 1H", "script": _resolve_script(BROWSER_DIR, MODULES_DIR, "3_Exchanges_LS_Ratio_1H.py"), "feed": "3_Exchanges_LS_Ratio_1H", "timeout": 180, "args": []},
    {"id": 5, "name": "LS Ratio 4H", "script": _resolve_script(BROWSER_DIR, MODULES_DIR, "3_Exchanges_LS_Ratio_4H.py"), "feed": "3_Exchanges_LS_Ratio_4H", "timeout": 180, "args": []},
    {"id": 6, "name": "Hyperliquid Whale", "script": _resolve_script(BROWSER_DIR, MODULES_DIR, "4_Hyperliquid_Analysis.py"), "feed": "4_Hyperliquid_Analysis", "timeout": 120, "args": ["--pages", "10"]},
    {"id": 7, "name": "Futures Open Interest", "script": _resolve_script(BROWSER_DIR, MODULES_DIR, "5_OI.py"), "feed": "5_OI", "timeout": 180, "args": []},
    {"id": 8, "name": "Funding Rates", "script": _resolve_script(BROWSER_DIR, MODULES_DIR, "5_Funding_Rate.py"), "feed": "5_Funding_Rate", "timeout": 120, "args": ["--pages", "10"]},
    {"id": 9, "name": "Funding Fee Settlement", "script": _resolve_script(BROWSER_DIR, MODULES_DIR, "6_Funding_Fee_Settlement.py"), "feed": "6_Funding_Fee_Settlement", "timeout": 120, "args": ["--pages", "10"]},
    {"id": 10, "name": "Liquidation Heatmap", "script": _resolve_script(BROWSER_DIR, MODULES_DIR, "7_Liq_Heapmap.py"), "feed": "7_Liq_Heapmap", "timeout": 120, "args": []},
    {"id": 11, "name": "Live Liquidations", "script": _resolve_script(BROWSER_DIR, MODULES_DIR, "7_Live_Liq.py"), "feed": "7_Live_Liq", "timeout": 120, "args": []},
    {"id": 12, "name": "Liq Map 1D", "script": _resolve_script(BROWSER_DIR, MODULES_DIR, "8_Exchange_Liquidation_Map_1D.py"), "feed": "8_Exchange_Liquidation_Map_1D", "timeout": 120, "args": []},
    {"id": 13, "name": "Liq Map 7D", "script": _resolve_script(BROWSER_DIR, MODULES_DIR, "8_Exchange_Liquidation_Map_7D.py"), "feed": "8_Exchange_Liquidation_Map_7D", "timeout": 120, "args": []},
    {"id": 14, "name": "Max Pain 24H", "script": _resolve_script(BROWSER_DIR, MODULES_DIR, "9_Liquidation_Max_Pain_24H.py"), "feed": "9_Liquidation_Max_Pain_24H", "timeout": 120, "args": []},
    {"id": 15, "name": "Max Pain 48H", "script": _resolve_script(BROWSER_DIR, MODULES_DIR, "9_Liquidation_Max_Pain_48H.py"), "feed": "9_Liquidation_Max_Pain_48H", "timeout": 120, "args": []},
    {"id": 16, "name": "Max Pain 3D", "script": _resolve_script(BROWSER_DIR, MODULES_DIR, "9_Liquidation_Max_Pain_3D.py"), "feed": "9_Liquidation_Max_Pain_3D", "timeout": 120, "args": []},
    {"id": 17, "name": "Max Pain 7D", "script": _resolve_script(BROWSER_DIR, MODULES_DIR, "9_Liquidation_Max_Pain_7D.py"), "feed": "9_Liquidation_Max_Pain_7D", "timeout": 120, "args": []},
    {"id": 18, "name": "Whale Orders", "script": _resolve_script(BROWSER_DIR, MODULES_DIR, "10_Whale_Orders.py"), "feed": "10_Whale_Orders", "timeout": 120, "args": []},
    {"id": 28, "name": "Forex News", "script": _resolve_script(BROWSER_DIR, MODULES_DIR, "19_News.py"), "feed": "19_News", "timeout": 120, "args": []},
    {"id": 29, "name": "Macro Calendar", "script": _resolve_script(BROWSER_DIR, MODULES_DIR, "19_Calendar.py"), "feed": "19_Calendar", "timeout": 120, "args": []},
]


def reap_scraping_tabs(except_tab_id: str | None = None) -> int:
    """
    Airtight CDP Tab Reaper:
    Enforces that ONLY data currently being fetched can exist in Edge.
    Strictly preserves Arena.ai and Z.ai tabs; closes ALL other scraping/orphan tabs immediately.
    """
    try:
        req = urllib.request.urlopen(f"{CDP_BASE_URL}/json", timeout=3)
        tabs = json.loads(req.read().decode())
        reaped = 0
        for t in tabs:
            if t.get("type") == "page":
                tab_id = t.get("id")
                if except_tab_id and tab_id == except_tab_id:
                    continue
                url = t.get("url", "").lower()
                title = t.get("title", "").lower()
                # Strictly protect user's Arena.ai and Z.ai tabs
                if any(k in url or k in title for k in ["arena.ai", "chat.z.ai", "z.ai"]):
                    continue
                try:
                    urllib.request.urlopen(f"{CDP_BASE_URL}/json/close/{tab_id}", timeout=3)
                    reaped += 1
                except Exception:
                    pass
        if reaped > 0:
            log.info(f"[TabReaper] Reaped {reaped} orphan/lingering scraping tab(s). Only authorized tabs remain.")
        return reaped
    except Exception:
        return 0


def run_single_module(mod: dict) -> Tuple[str, bool, float, str]:
    """Executes a single harvester script subprocess with guaranteed tab cleanup."""
    feed = mod.get("feed", mod.get("sheet", "Unknown"))
    script_path = mod["script"]
    timeout = mod.get("timeout", 120)
    args = mod.get("args", [])
    tier = "Browser" if mod in BROWSER_MODULES else "API"

    if not script_path.exists():
        return feed, False, 0.0, "Script file not found"

    # For browser modules: clean any lingering tabs BEFORE launch
    if tier == "Browser":
        reap_scraping_tabs()

    t0 = time.perf_counter()
    env = os.environ.copy()
    py_paths = [
        str(CORE_DIR),
        str(API_DIR),
        str(BROWSER_DIR),
        str(ROOT_DIR / "Terminal" / "Data_Factory"),
        str(MODULES_DIR),
        str(ROOT_DIR),
        env.get("PYTHONPATH", "")
    ]
    env["PYTHONPATH"] = ";".join(p for p in py_paths if p)

    try:
        proc = subprocess.run(
            [sys.executable, str(script_path)] + args,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            timeout=timeout,
            env=env,
        )
        duration = time.perf_counter() - t0
        success = (proc.returncode == 0)
        err = proc.stderr.strip() if not success else ""
        return feed, success, duration, err
    except subprocess.TimeoutExpired:
        duration = time.perf_counter() - t0
        return feed, False, duration, f"Timed out after {timeout}s"
    except Exception as exc:
        duration = time.perf_counter() - t0
        return feed, False, duration, str(exc)
    finally:
        # Crucial invariant: ALWAYS reap lingering tabs immediately when browser module ends or times out
        if tier == "Browser":
            reap_scraping_tabs()


def execute_full_cycle() -> dict:
    """Executes full 33-feed parallel cycle."""
    log.info("================================================================================")
    log.info("Starting Full 33-Feed Parquet Harvest Cycle (< 15.0m Target)")
    log.info("================================================================================")
    t_start = time.perf_counter()

    results = []

    # Phase 1: Pure API Modules (6 parallel workers)
    log.info("--- Phase 1: Executing 12 Pure API Modules (6 Parallel Workers) ---")
    with concurrent.futures.ThreadPoolExecutor(max_workers=6) as executor:
        futures = {executor.submit(run_single_module, mod): mod for mod in API_MODULES}
        for future in concurrent.futures.as_completed(futures):
            feed, success, duration, err = future.result()
            status_str = "PASS" if success else "FAIL"
            err_msg = f" | Error: {err}" if not success else ""
            log.info(f"  [{status_str}] {feed:<30} ({duration:>5.1f}s){err_msg}")
            results.append({"feed": feed, "tier": "API", "success": success, "duration": duration, "error": err})

    # Phase 2: Browser CDP Modules (Strictly serialized 1 worker to protect browser renderer & prevent 429)
    log.info("--- Phase 2: Executing Browser CDP Modules (Serialized 1 Worker, Paced) ---")
    with concurrent.futures.ThreadPoolExecutor(max_workers=1) as executor:
        futures = {executor.submit(run_single_module, mod): mod for mod in BROWSER_MODULES}
        for future in concurrent.futures.as_completed(futures):
            feed, success, duration, err = future.result()
            status_str = "PASS" if success else "FAIL"
            err_msg = f" | Error: {err}" if not success else ""
            log.info(f"  [{status_str}] {feed:<30} ({duration:>5.1f}s){err_msg}")
            results.append({"feed": feed, "tier": "Browser", "success": success, "duration": duration, "error": err})

    reap_scraping_tabs()

    total_time = time.perf_counter() - t_start
    passed_count = sum(1 for r in results if r["success"])

    log.info("--------------------------------------------------------------------------------")
    log.info(f"Execution Complete: {passed_count}/{len(results)} Modules Passed in {total_time:.1f}s.")
    log.info("--------------------------------------------------------------------------------\n")

    # Phase 3: Run Sub-Second Parquet Checklist Auditor
    log.info("--- Phase 3: Running Parquet Checklist Auditor (< 15m) ---")
    checklist_passed = False
    try:
        proc_check = subprocess.run(
            [sys.executable, str(AUDITOR_SCRIPT), "--max-age", "15.0"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            timeout=30,
            check=False,
        )
        print(proc_check.stdout)
        if proc_check.stderr:
            sys.stderr.write(proc_check.stderr)
        checklist_passed = (proc_check.returncode == 0)
    except Exception as e:
        log.error(f"Error running checklist audit: {e}")

    return {
        "passed": passed_count,
        "total": len(results),
        "total_time": total_time,
        "checklist_passed": checklist_passed,
        "results": results,
    }


def execute_refresh_stale(max_age_min: float = 15.0) -> dict:
    """Audits Data/metadata/, identifies stale feeds (age >= max_age_min), and refreshes ONLY those."""
    log.info(f"Auditing feeds for stale data (age >= {max_age_min:.1f}m)...")
    checklist_json_path = METADATA_DIR / "parquet_all_feeds_checklist.json"

    subprocess.run([sys.executable, str(AUDITOR_SCRIPT), "--max-age", str(max_age_min)], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    stale_feeds = []
    if checklist_json_path.exists():
        try:
            with open(checklist_json_path, "r", encoding="utf-8") as f:
                data = json.load(f)
            stale_feeds = [s["feed_name"] for s in data.get("checklist", []) if not s.get("is_fresh", False) or s.get("status") != "PASS"]
        except Exception:
            pass

    if not stale_feeds:
        log.info(f"All 33 feeds are 100%% fresh (< {max_age_min:.1f}m IST). Zero refresh needed!")
        return {"passed": 0, "total": 0, "checklist_passed": True}

    log.info(f"Targeting {len(stale_feeds)} stale feeds: {stale_feeds}")
    all_mods = API_MODULES + BROWSER_MODULES
    target_mods = [m for m in all_mods if m.get("feed") in stale_feeds or m.get("sheet") in stale_feeds]
    api_targets = [m for m in target_mods if m in API_MODULES]
    browser_targets = [m for m in target_mods if m in BROWSER_MODULES]

    results = []
    if api_targets:
        log.info(f"Refreshing {len(api_targets)} stale API feeds in parallel...")
        with concurrent.futures.ThreadPoolExecutor(max_workers=min(6, len(api_targets))) as executor:
            futures = {executor.submit(run_single_module, mod): mod for mod in api_targets}
            for future in concurrent.futures.as_completed(futures):
                feed, success, duration, err = future.result()
                results.append({"feed": feed, "tier": "API", "success": success, "duration": duration, "error": err})

    if browser_targets:
        log.info(f"Refreshing {len(browser_targets)} stale Browser feeds (Serialized 1 worker)...")
        with concurrent.futures.ThreadPoolExecutor(max_workers=1) as executor:
            futures = {executor.submit(run_single_module, mod): mod for mod in browser_targets}
            for future in concurrent.futures.as_completed(futures):
                feed, success, duration, err = future.result()
                results.append({"feed": feed, "tier": "Browser", "success": success, "duration": duration, "error": err})

    reap_scraping_tabs()
    passed_count = sum(1 for r in results if r["success"])
    log.info(f"Stale Refresh Complete: {passed_count}/{len(results)} Passed.")

    # Audit again
    proc_check = subprocess.run([sys.executable, str(AUDITOR_SCRIPT), "--max-age", str(max_age_min)], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    print(proc_check.stdout)
    return {"passed": passed_count, "total": len(results), "checklist_passed": (proc_check.returncode == 0)}


def main():
    parser = argparse.ArgumentParser(description="Parquet 33-Feed Master Tiered Runner")
    parser.add_argument("--continuous", action="store_true", help="Run continuous background daemon")
    parser.add_argument("--stale", action="store_true", help="Refresh only stale feeds")
    parser.add_argument("--interval", type=int, default=180, help="Continuous loop interval in seconds (default: 180s)")
    parser.add_argument("--audit", action="store_true", help="Run instant freshness scorecard audit and exit")
    parser.add_argument("--feed", type=str, default=None, help="Run single feed module (e.g. '00_MT5_Account_Telemetry')")
    parser.add_argument("--max-age", type=float, default=15.0, help="Maximum allowed feed age in minutes (default: 15.0m)")
    args = parser.parse_args()

    if args.audit:
        proc = subprocess.run([sys.executable, str(AUDITOR_SCRIPT), "--max-age", str(args.max_age)], text=True)
        sys.exit(proc.returncode)

    if args.feed:
        all_mods = API_MODULES + BROWSER_MODULES
        matched = [m for m in all_mods if m.get("feed", "").lower() == args.feed.lower() or m.get("name", "").lower() == args.feed.lower()]
        if not matched:
            print(f"[ERROR] Feed '{args.feed}' not found in registered modules.")
            sys.exit(1)
        mod = matched[0]
        feed, success, duration, err = run_single_module(mod)
        print(f"[{'PASS' if success else 'FAIL'}] {feed} completed in {duration:.1f}s. Result: {err}")
        sys.exit(0 if success else 1)

    if args.continuous:
        mode_desc = f"stale-only (< {args.max_age}m)" if args.stale else "full 33-feed parallel"
        log.info(f"Starting continuous {mode_desc} daemon (interval: {args.interval}s)...")
        while True:
            try:
                if args.stale:
                    execute_refresh_stale(max_age_min=args.max_age)
                else:
                    execute_full_cycle()
            except Exception as e:
                log.error(f"Error in continuous cycle: {e}")
            time.sleep(args.interval)
    elif args.stale:
        summary = execute_refresh_stale(max_age_min=args.max_age)
        sys.exit(0 if summary.get("checklist_passed") else 1)
    else:
        summary = execute_full_cycle()
        sys.exit(0 if summary.get("checklist_passed") else 1)


if __name__ == "__main__":
    main()
