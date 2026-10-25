#!/usr/bin/env python3
"""
Terminal/Data_Factory/run_unified_30_sheets_cycle.py
=====================================================
Master Autonomous 30-Sheet Excel Refresh & IST Standardization Orchestrator.
Guarantees that in EVERY cycle:
  1. ALL 30 canonical sheets in Data/DataBase_Trading.xlsx are harvested & updated.
  2. All timestamps inside tables and Row 1 top banners are formatted in IST (UTC+5:30).
  3. Row 1 top banner is stamped ONLY ONCE row data is filled (row_count > 0).
  4. Generates an institutional 30-sheet verification checklist scorecard.
  5. If ANY sheet fails to update or is stale (>30m), flags the exact failure and wakes up.
"""

from __future__ import annotations

import argparse
import datetime
import json
import logging
import os
import pathlib
import subprocess
import sys
import time
import urllib.request

try:
    import openpyxl
except ImportError:
    openpyxl = None

ROOT_DIR = pathlib.Path(__file__).resolve().parents[2]
DATA_DIR = ROOT_DIR / "Data"
MODULES_DIR = DATA_DIR / "Excel_Modules"
EXCEL_PATH = DATA_DIR / "DataBase_Trading.xlsx"
CHECKLIST_SCRIPT = ROOT_DIR / "Terminal" / "Data_Factory" / "excel_sheet_checklist_auditor.py"
CDP_BASE_URL = "http://127.0.0.1:9222"

IST_TIMEZONE = datetime.timezone(datetime.timedelta(hours=5, minutes=30))
UTC_TIMEZONE = datetime.timezone.utc

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] [30SheetsCycle] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
log = logging.getLogger("30SheetsCycle")

# 1. Tier 1A: Pure API Modules (Can run concurrently with 3 workers)
API_MODULES = [
    {"id": 0, "name": "MT5 Telemetry", "script": MODULES_DIR / "00_MT5_Account_Telemetry.py", "sheet": "00_MT5_Account_Telemetry", "timeout": 60, "args": []},
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

# 2. Tier 1B: Browser CDP Modules (Run sequentially through Edge queue worker, preserving Arena tab)
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
    """Forces closure of any lingering web scraping tabs on Edge port 9222 while preserving Arena and Z.ai."""
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


def preflight_hygiene():
    """Verifies Edge CDP on port 9222 and cleans temporary files."""
    # Check CDP
    try:
        req = urllib.request.urlopen(f"{CDP_BASE_URL}/json", timeout=3)
        tabs = json.loads(req.read().decode())
        has_arena = any("arena.ai" in t.get("url", "").lower() for t in tabs)
        log.info(f"[Pre-Flight] Edge CDP active on port 9222 ({len(tabs)} tabs open). Arena.ai preserved: {has_arena}")
        reap_scraping_tabs()
    except Exception as e:
        log.warning(f"[Pre-Flight] Edge CDP not reachable on port 9222: {e}")

    # Clean orphaned .tmp.xlsx files
    tmp_files = list(DATA_DIR.glob("*.tmp.xlsx"))
    for f in tmp_files:
        try:
            f.unlink()
        except Exception:
            pass
    if tmp_files:
        log.info(f"[Pre-Flight] Cleaned up {len(tmp_files)} orphaned temporary files.")


def run_single_module(mod: dict) -> tuple[str, bool, float, str]:
    """Executes a single harvester script subprocess safely."""
    sheet = mod["sheet"]
    script_path = mod["script"]
    timeout = mod.get("timeout", 120)
    args = mod.get("args", [])
    
    if not script_path.exists():
        return sheet, False, 0.0, "Script file not found"

    cmd = [sys.executable, str(script_path)] + args
    t0 = time.perf_counter()
    try:
        proc = subprocess.run(
            cmd,
            cwd=str(MODULES_DIR),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
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
    finally:
        reap_scraping_tabs()


def execute_unified_30_sheets_cycle() -> dict:
    """Executes all 30 modules and runs the checklist auditor."""
    t_start = time.perf_counter()
    now_ist = datetime.datetime.now(IST_TIMEZONE)
    now_utc = datetime.datetime.now(UTC_TIMEZONE)

    log.info("================================================================================")
    log.info("          STARTING UNIFIED 30-SHEET REFRESH & IST STANDARDIZATION CYCLE         ")
    log.info(f"          Start Time: {now_ist.strftime('%Y-%m-%d %H:%M:%S IST')} ({now_utc.strftime('%Y-%m-%d %H:%M:%S UTC')})")
    log.info(f"          Target Workbook: {EXCEL_PATH.name}                                  ")
    log.info("================================================================================")

    preflight_hygiene()

    results = []

    # 1. Phase 1: Pure API Modules (Run sequentially or in small pool to avoid openpyxl lock contention)
    log.info(f"\n--- Phase 1: Executing {len(API_MODULES)} Pure API Modules ---")
    for mod in API_MODULES:
        sheet, success, duration, err = run_single_module(mod)
        status_str = "PASS" if success else "FAIL"
        err_msg = f" | Error: {err}" if not success else ""
        log.info(f"  [{status_str}] {sheet:<30} ({duration:>5.1f}s){err_msg}")
        results.append({"sheet": sheet, "tier": "API", "success": success, "duration": duration, "error": err})

    # 2. Phase 2: Browser CDP Modules (Run sequentially through Edge tab queue)
    log.info(f"\n--- Phase 2: Executing {len(BROWSER_MODULES)} Browser CDP Modules ---")
    for mod in BROWSER_MODULES:
        sheet, success, duration, err = run_single_module(mod)
        status_str = "PASS" if success else "FAIL"
        err_msg = f" | Error: {err}" if not success else ""
        log.info(f"  [{status_str}] {sheet:<30} ({duration:>5.1f}s){err_msg}")
        results.append({"sheet": sheet, "tier": "Browser", "success": success, "duration": duration, "error": err})

    total_time = time.perf_counter() - t_start
    passed_count = sum(1 for r in results if r["success"])

    log.info("--------------------------------------------------------------------------------")
    log.info(f"Harvester Execution Complete: {passed_count}/{len(results)} Modules Passed in {total_time:.1f}s.")
    log.info("--------------------------------------------------------------------------------\n")

    # 3. Phase 3: Run Master 30-Sheet Verification Checklist
    log.info("--- Phase 3: Running Autonomous 30-Sheet Checklist & IST Audit ---")
    checklist_passed = False
    checklist_data = {}
    try:
        proc_check = subprocess.run(
            [sys.executable, str(CHECKLIST_SCRIPT)],
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


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Unified 30-Sheet Excel Refresh Cycle")
    parser.add_argument("--continuous", action="store_true", help="Run continuously in background")
    parser.add_argument("--interval", type=int, default=300, help="Interval between cycles in seconds (default: 300s = 5m)")
    args = parser.parse_args()

    if args.continuous:
        log.info(f"Starting continuous 30-sheet refresh daemon (cycle interval: {args.interval}s)...")
        while True:
            try:
                execute_unified_30_sheets_cycle()
            except Exception as e:
                log.error(f"Error in continuous cycle: {e}")
            time.sleep(args.interval)
    else:
        summary = execute_unified_30_sheets_cycle()
        sys.exit(0 if summary.get("checklist_passed") else 1)
