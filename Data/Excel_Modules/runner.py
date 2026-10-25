#!/usr/bin/env python3
"""
Data/Excel_Modules/runner.py
=============================
Master Unified Runner for all Excel Modules in Data/Excel_Modules/.
Coordinates execution across all 32 institutional sheets in Data/DataBase_Trading.xlsx:
  1. Pure API Modules (Tier 1A): Executed in parallel with 6 worker threads.
  2. Browser CDP Modules (Tier 1B): Executed across 3 parallel Edge tabs.
  3. Non-blocking FileLock: Serializes atomic replacement via excel_lock_hook.py.
  4. 5-Minute Freshness Guarantee: Enforces max sheet age < 5.0 minutes.
  5. Checklist Verification: Automatically audits and prints 32-sheet age scorecard.

Usage:
  python runner.py                      # Run full 32-sheet parallel cycle
  python runner.py --stale              # Refresh only stale sheets (age >= 5.0m)
  python runner.py --continuous         # Continuous background daemon (180s interval)
  python runner.py --audit              # Run 32-sheet age audit scorecard
  python runner.py --sheet 11_Technical # Run single module
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

MODULES_DIR = pathlib.Path(__file__).resolve().parent
ROOT_DIR = MODULES_DIR.parents[1]
DATA_DIR = ROOT_DIR / "Data"
EXCEL_PATH = DATA_DIR / "DataBase_Trading.xlsx"
CHECKLIST_SCRIPT = ROOT_DIR / "Terminal" / "Data_Factory" / "excel_sheet_checklist_auditor.py"
CDP_BASE_URL = "http://127.0.0.1:9222"

IST_TIMEZONE = datetime.timezone(datetime.timedelta(hours=5, minutes=30))
UTC_TIMEZONE = datetime.timezone.utc

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] [ExcelRunner] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
log = logging.getLogger("ExcelRunner")

# 1. Tier 1A: Pure API Modules (Execute in parallel across 6 worker threads)
API_MODULES = [
    {"id": 0, "name": "MT5 Telemetry", "script": MODULES_DIR / "00_MT5_Account_Telemetry.py", "sheet": "00_MT5_Account_Telemetry", "timeout": 120, "args": []},
    {"id": 6, "name": "Hyperliquid Whale", "script": MODULES_DIR / "4_Hyperliquid_Analysis.py", "sheet": "4_Hyperliquid_Analysis", "timeout": 120, "args": ["--pages", "10"]},
    {"id": 7, "name": "Futures Open Interest", "script": MODULES_DIR / "5_OI.py", "sheet": "5_OI", "timeout": 180, "args": []},
    {"id": 8, "name": "Funding Rates", "script": MODULES_DIR / "5_Funding_Rate.py", "sheet": "5_Funding_Rate", "timeout": 120, "args": ["--pages", "10"]},
    {"id": 9, "name": "Funding Fee Settlement", "script": MODULES_DIR / "6_Funding_Fee_Settlement.py", "sheet": "6_Funding_Fee_Settlement", "timeout": 120, "args": ["--pages", "10"]},
    {"id": 19, "name": "Technical Indicators", "script": MODULES_DIR / "11_Technical.py", "sheet": "11_Technical", "timeout": 120, "args": []},
    {"id": 20, "name": "Hyperdash Flow", "script": MODULES_DIR / "12_Hyperdash.py", "sheet": "12_Hyperdash", "timeout": 120, "args": []},
    {"id": 21, "name": "Hyperliquid L1", "script": MODULES_DIR / "13_Hyperliquid.py", "sheet": "13_Hyperliquid", "timeout": 120, "args": []},
    {"id": 22, "name": "Hyperdash Liq Map", "script": MODULES_DIR / "14_Hyperdash_Liq_Map.py", "sheet": "14_Hyperdash_Liq_Map", "timeout": 120, "args": []},
    {"id": 23, "name": "Hyperdash Stops Map", "script": MODULES_DIR / "15_Hyperdash_Stops_Map.py", "sheet": "15_Hyperdash_Stops_Map", "timeout": 120, "args": []},
    {"id": 24, "name": "Hyperdash Telegram Intel", "script": MODULES_DIR / "16_Hyperdash_telegram_Intel.py", "sheet": "16_Hyperdash_telegram_Intel", "timeout": 120, "args": ["--pages", "10", "--limit", "1000"]},
    {"id": 25, "name": "Orderbook & Whale Attribution", "script": MODULES_DIR / "17_Orderbook.py", "sheet": "17_Orderbook", "timeout": 180, "args": []},
    {"id": 26, "name": "CVD Engine", "script": MODULES_DIR / "18_CVD.py", "sheet": "18_CVD", "timeout": 240, "args": ["--max-excel-rows", "1500"]},
    {"id": 27, "name": "Auction Market Structure", "script": MODULES_DIR / "20_Auction_Market_Structure.py", "sheet": "20_Auction_Market_Structure", "timeout": 120, "args": []},
    {"id": 28, "name": "Tradfye Orderflow", "script": MODULES_DIR / "21_Tradfye_Orderflow.py", "sheet": "21_Tradfye_Orderflow", "timeout": 120, "args": []},
    {"id": 31, "name": "Forced Liquidations MTF", "script": MODULES_DIR / "22_Forced_Liquidations_MTF.py", "sheet": "22_Forced_Liquidations_MTF", "timeout": 120, "args": []},
]

# 2. Tier 1B: Browser CDP Modules (Execute across 3 parallel Edge tabs)
BROWSER_MODULES = [
    {"id": 1, "name": "Crypto ETF Flows", "script": MODULES_DIR / "1_Crypto_ETF_Flows.py", "sheet": "1_Crypto_ETF_Flows", "timeout": 120, "args": []},
    {"id": 2, "name": "Spot Netflow", "script": MODULES_DIR / "2_Spot_Netflow_S.py", "sheet": "2_Spot_Netflow_S", "timeout": 180, "args": ["--pages", "10"]},
    {"id": 3, "name": "LS Ratio 15M", "script": MODULES_DIR / "3_Exchanges_LS_Ratio_15M.py", "sheet": "3_Exchanges_LS_Ratio_15M", "timeout": 180, "args": []},
    {"id": 4, "name": "LS Ratio 1H", "script": MODULES_DIR / "3_Exchanges_LS_Ratio_1H.py", "sheet": "3_Exchanges_LS_Ratio_1H", "timeout": 120, "args": []},
    {"id": 5, "name": "LS Ratio 4H", "script": MODULES_DIR / "3_Exchanges_LS_Ratio_4H.py", "sheet": "3_Exchanges_LS_Ratio_4H", "timeout": 120, "args": []},
    {"id": 10, "name": "Liquidation Heatmap", "script": MODULES_DIR / "7_Liq_Heapmap.py", "sheet": "7_Liq_Heapmap", "timeout": 120, "args": []},
    {"id": 11, "name": "Live Liquidations", "script": MODULES_DIR / "7_Live_Liq.py", "sheet": "7_Live_Liq", "timeout": 120, "args": []},
    {"id": 12, "name": "Liq Map 1D", "script": MODULES_DIR / "8_Exchange_Liquidation_Map_1D.py", "sheet": "8_Exchange_Liquidation_Map_1D", "timeout": 120, "args": []},
    {"id": 13, "name": "Liq Map 7D", "script": MODULES_DIR / "8_Exchange_Liquidation_Map_7D.py", "sheet": "8_Exchange_Liquidation_Map_7D", "timeout": 120, "args": []},
    {"id": 14, "name": "Max Pain 24H", "script": MODULES_DIR / "9_Liquidation_Max_Pain_24H.py", "sheet": "9_Liquidation_Max_Pain_24H", "timeout": 120, "args": []},
    {"id": 15, "name": "Max Pain 48H", "script": MODULES_DIR / "9_Liquidation_Max_Pain_48H.py", "sheet": "9_Liquidation_Max_Pain_48H", "timeout": 120, "args": []},
    {"id": 16, "name": "Max Pain 3D", "script": MODULES_DIR / "9_Liquidation_Max_Pain_3D.py", "sheet": "9_Liquidation_Max_Pain_3D", "timeout": 120, "args": []},
    {"id": 17, "name": "Max Pain 7D", "script": MODULES_DIR / "9_Liquidation_Max_Pain_7D.py", "sheet": "9_Liquidation_Max_Pain_7D", "timeout": 120, "args": []},
    {"id": 18, "name": "Whale Orders", "script": MODULES_DIR / "10_Whale_Orders.py", "sheet": "10_Whale_Orders", "timeout": 120, "args": []},
    {"id": 28, "name": "Forex News", "script": MODULES_DIR / "19_News.py", "sheet": "19_News", "timeout": 120, "args": []},
    {"id": 29, "name": "Macro Calendar", "script": MODULES_DIR / "19_Calendar.py", "sheet": "19_Calendar", "timeout": 120, "args": []},
]


def reap_scraping_tabs():
    """Forces closure of lingering web scraping tabs on Edge port 9222 while preserving Arena and Z.ai."""
    try:
        req = urllib.request.urlopen(f"{CDP_BASE_URL}/json", timeout=3)
        tabs = json.loads(req.read().decode())
        reaped = 0
        for t in tabs:
            if t.get("type") == "page":
                url = t.get("url", "").lower()
                title = t.get("title", "").lower()
                # Strictly protect Arena.ai and Z.ai
                if any(k in url or k in title for k in ["arena.ai", "chat.z.ai", "z.ai"]):
                    continue
                tab_id = t.get("id")
                try:
                    urllib.request.urlopen(f"{CDP_BASE_URL}/json/close/{tab_id}", timeout=3)
                    reaped += 1
                except Exception:
                    pass
        if reaped > 0:
            log.info(f"[TabReaper] Reaped {reaped} lingering scraping tab(s) in Edge.")
    except Exception:
        pass


def run_single_module(mod: dict) -> tuple[str, bool, float, str]:
    """Executes a single harvester script subprocess safely with excel_lock_hook."""
    sheet = mod["sheet"]
    script_path = mod["script"]
    timeout = mod.get("timeout", 120)
    args = mod.get("args", [])

    if not script_path.exists():
        return sheet, False, 0.0, "Script file not found"

    # Set PYTHONPATH to include MODULES_DIR
    env = dict(os.environ)
    env["PYTHONPATH"] = str(MODULES_DIR) + os.pathsep + env.get("PYTHONPATH", "")

    cmd = [sys.executable, str(script_path)] + args
    t0 = time.perf_counter()
    try:
        proc = subprocess.run(
            cmd,
            cwd=str(MODULES_DIR),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            env=env,
            text=True,
            timeout=timeout,
            check=False
        )
        elapsed = time.perf_counter() - t0
        success = (proc.returncode == 0)
        err = "OK" if success else (proc.stderr.strip()[-200:] if proc.stderr else f"Exit code {proc.returncode}")
        return sheet, success, elapsed, err
    except subprocess.TimeoutExpired:
        elapsed = time.perf_counter() - t0
        return sheet, False, elapsed, "TimeoutExpired"
    except Exception as e:
        elapsed = time.perf_counter() - t0
        return sheet, False, elapsed, str(e)


def execute_full_cycle() -> dict:
    """Executes full 32-sheet parallel refresh cycle and runs checklist auditor."""
    t_start = time.perf_counter()
    now_ist = datetime.datetime.now(IST_TIMEZONE)
    now_utc = datetime.datetime.now(UTC_TIMEZONE)

    log.info("================================================================================")
    log.info("       STARTING UNIFIED 32-SHEET PARALLEL REFRESH (< 5M FRESHNESS GUARANTEE)    ")
    log.info(f"       Start Time: {now_ist.strftime('%Y-%m-%d %H:%M:%S IST')} ({now_utc.strftime('%Y-%m-%d %H:%M:%S UTC')})")
    log.info("================================================================================")

    reap_scraping_tabs()
    results = []

    # 1. Phase 1: Pure API Modules in parallel (6 worker threads)
    log.info(f"\n--- Phase 1: Executing {len(API_MODULES)} Pure API Modules in Parallel (6 workers) ---")
    with concurrent.futures.ThreadPoolExecutor(max_workers=6) as executor:
        future_to_mod = {executor.submit(run_single_module, mod): mod for mod in API_MODULES}
        for future in concurrent.futures.as_completed(future_to_mod):
            mod = future_to_mod[future]
            try:
                sheet, success, duration, err = future.result()
            except Exception as exc:
                sheet, success, duration, err = mod["sheet"], False, 0.0, str(exc)
            status_str = "PASS" if success else "FAIL"
            err_msg = f" | Error: {err}" if not success else ""
            log.info(f"  [{status_str}] {sheet:<30} ({duration:>5.1f}s){err_msg}")
            results.append({"sheet": sheet, "tier": "API", "success": success, "duration": duration, "error": err})

    # 2. Phase 2: Browser CDP Modules in parallel (3 parallel Edge tabs)
    log.info(f"\n--- Phase 2: Executing {len(BROWSER_MODULES)} Browser CDP Modules in Parallel (3 Edge tabs) ---")
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
        future_to_mod = {executor.submit(run_single_module, mod): mod for mod in BROWSER_MODULES}
        for future in concurrent.futures.as_completed(future_to_mod):
            mod = future_to_mod[future]
            try:
                sheet, success, duration, err = future.result()
            except Exception as exc:
                sheet, success, duration, err = mod["sheet"], False, 0.0, str(exc)
            status_str = "PASS" if success else "FAIL"
            err_msg = f" | Error: {err}" if not success else ""
            log.info(f"  [{status_str}] {sheet:<30} ({duration:>5.1f}s){err_msg}")
            results.append({"sheet": sheet, "tier": "Browser", "success": success, "duration": duration, "error": err})

    reap_scraping_tabs()

    total_time = time.perf_counter() - t_start
    passed_count = sum(1 for r in results if r["success"])

    log.info("--------------------------------------------------------------------------------")
    log.info(f"Execution Complete: {passed_count}/{len(results)} Modules Passed in {total_time:.1f}s.")
    log.info("--------------------------------------------------------------------------------\n")

    # 3. Phase 3: Run Master Checklist Auditor with 5.0m threshold
    log.info("--- Phase 3: Running Master 32-Sheet Checklist & Age Audit (< 5m) ---")
    checklist_passed = False
    try:
        proc_check = subprocess.run(
            [sys.executable, str(CHECKLIST_SCRIPT), "--max-age", "5.0"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            timeout=60,
            check=False
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
        "results": results
    }


def execute_refresh_stale(max_age_min: float = 5.0) -> dict:
    """Audits Data/DataBase_Trading.xlsx, identifies stale sheets (age >= 5m), and refreshes ONLY those modules in parallel."""
    log.info("Auditing sheets for stale data (age >= %.1fm)...", max_age_min)
    checklist_json_path = DATA_DIR / "excel_all_sheets_checklist.json"

    proc = subprocess.run([sys.executable, str(CHECKLIST_SCRIPT), "--max-age", str(max_age_min)], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    stale_sheets = []
    if checklist_json_path.exists():
        try:
            with open(checklist_json_path, "r", encoding="utf-8") as f:
                data = json.load(f)
            stale_sheets = [s["sheet_name"] for s in data.get("checklist", []) if not s.get("is_fresh", False) or s.get("status") != "PASS"]
        except Exception:
            pass

    if not stale_sheets:
        log.info("All 32 sheets are 100%% fresh (< %.1fm IST). Zero refresh needed!", max_age_min)
        return {"passed": 0, "total": 0, "checklist_passed": True}

    log.info("Targeting %d stale sheets: %s", len(stale_sheets), stale_sheets)
    target_mods = [m for m in (API_MODULES + BROWSER_MODULES) if m["sheet"] in stale_sheets]
    api_targets = [m for m in target_mods if m in API_MODULES]
    browser_targets = [m for m in target_mods if m in BROWSER_MODULES]

    results = []
    if api_targets:
        log.info("Executing %d stale API modules in parallel (6 workers)...", len(api_targets))
        with concurrent.futures.ThreadPoolExecutor(max_workers=min(6, len(api_targets))) as executor:
            future_to_mod = {executor.submit(run_single_module, mod): mod for mod in api_targets}
            for future in concurrent.futures.as_completed(future_to_mod):
                mod = future_to_mod[future]
                try:
                    sheet, success, duration, err = future.result()
                except Exception as exc:
                    sheet, success, duration, err = mod["sheet"], False, 0.0, str(exc)
                status_str = "PASS" if success else "FAIL"
                err_msg = f" | Error: {err}" if not success else ""
                log.info(f"  [{status_str}] {sheet:<30} ({duration:>5.1f}s){err_msg}")
                results.append({"sheet": sheet, "success": success, "duration": duration, "error": err})

    if browser_targets:
        log.info("Executing %d stale Browser modules across parallel Edge tabs (3 workers)...", len(browser_targets))
        with concurrent.futures.ThreadPoolExecutor(max_workers=min(3, len(browser_targets))) as executor:
            future_to_mod = {executor.submit(run_single_module, mod): mod for mod in browser_targets}
            for future in concurrent.futures.as_completed(future_to_mod):
                mod = future_to_mod[future]
                try:
                    sheet, success, duration, err = future.result()
                except Exception as exc:
                    sheet, success, duration, err = mod["sheet"], False, 0.0, str(exc)
                status_str = "PASS" if success else "FAIL"
                err_msg = f" | Error: {err}" if not success else ""
                log.info(f"  [{status_str}] {sheet:<30} ({duration:>5.1f}s){err_msg}")
                results.append({"sheet": sheet, "success": success, "duration": duration, "error": err})
        reap_scraping_tabs()

    # Re-run auditor with strict 5m threshold
    proc_check = subprocess.run([sys.executable, str(CHECKLIST_SCRIPT), "--max-age", str(max_age_min)], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    print(proc_check.stdout)
    checklist_passed = (proc_check.returncode == 0)
    return {"passed": sum(1 for r in results if r["success"]), "total": len(results), "checklist_passed": checklist_passed, "results": results}


def run_audit(max_age_min: float = 5.0) -> bool:
    """Runs the 32-sheet checklist auditor directly."""
    proc = subprocess.run([sys.executable, str(CHECKLIST_SCRIPT), "--max-age", str(max_age_min)], text=True)
    return proc.returncode == 0


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Master Excel Modules Runner (< 5m Freshness Guarantee)")
    parser.add_argument("--continuous", action="store_true", help="Run continuously in background every N seconds")
    parser.add_argument("--interval", type=int, default=180, help="Interval in seconds between cycles (default: 180s = 3m)")
    parser.add_argument("--stale", action="store_true", help="Refresh only stale sheets (age >= 5m)")
    parser.add_argument("--audit", action="store_true", help="Audit and print current 32-sheet age report")
    parser.add_argument("--sheet", type=str, default="", help="Run a specific sheet module (e.g. '11_Technical')")
    parser.add_argument("--max-age", type=float, default=5.0, help="Maximum allowed sheet age in minutes (default: 5.0m)")
    args = parser.parse_args()

    if args.audit:
        ok = run_audit(max_age_min=args.max_age)
        sys.exit(0 if ok else 1)

    if args.sheet:
        all_mods = API_MODULES + BROWSER_MODULES
        matched = [m for m in all_mods if m["sheet"].lower() == args.sheet.lower() or m["name"].lower() == args.sheet.lower()]
        if not matched:
            print(f"[ERROR] Sheet '{args.sheet}' not found in registered modules.")
            sys.exit(1)
        mod = matched[0]
        sheet, success, duration, err = run_single_module(mod)
        print(f"[{'PASS' if success else 'FAIL'}] {sheet} completed in {duration:.1f}s. Result: {err}")
        sys.exit(0 if success else 1)

    if args.continuous:
        mode_desc = f"stale-only (< {args.max_age}m)" if args.stale else "full 32-sheet parallel"
        log.info("Starting continuous %s daemon (interval: %ds)...", mode_desc, args.interval)
        while True:
            try:
                if args.stale:
                    execute_refresh_stale(max_age_min=args.max_age)
                else:
                    execute_full_cycle()
            except Exception as e:
                log.error("Error in continuous cycle: %s", e)
            time.sleep(args.interval)
    elif args.stale:
        summary = execute_refresh_stale(max_age_min=args.max_age)
        sys.exit(0 if summary.get("checklist_passed") else 1)
    else:
        summary = execute_full_cycle()
        sys.exit(0 if summary.get("checklist_passed") else 1)
