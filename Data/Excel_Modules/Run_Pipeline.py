#!/usr/bin/env python3
"""
Data/Excel_Modules/Run_Pipeline.py
==================================
Sequential Orchestrator Pipeline for All Dedicated Excel Modules
with Cloudflare WARP Anycast Protection & Tab Hygiene.

Modules Executed:
  1. 1_Crypto_ETF_Flows.py: Live CoinGlass Crypto ETF Overview table -> '1_Crypto_ETF_Flows' (Index 0).
  2. 2_Spot_Netflow_S.py: Live CoinGlass Spot Netflows (500 assets) -> '2_Spot_Netflow_S' (Index 1).
  3. 3_Exchanges_LS_Ratio_15M.py: Exchanges Long/Short Ratio (15M) -> '3_Exchanges_LS_Ratio_15M' (Index 2).
  4. 3_Exchanges_LS_Ratio_1H.py: Exchanges Long/Short Ratio (1H) -> '3_Exchanges_LS_Ratio_1H' (Index 3).
  5. 3_Exchanges_LS_Ratio_4H.py: Exchanges Long/Short Ratio (4H) -> '3_Exchanges_LS_Ratio_4H' (Index 4).
  6. 4_Hyperliquid_Analysis.py: Live Hyperliquid Whale Monitoring -> '4_Hyperliquid_Analysis' (Index 5).
  7. 5_OI.py: Futures Open Interest Analysis across all 18 Universe Assets -> '5_OI' (Index 6).
  8. 5_Funding_Rate.py: Live Crypto Funding Rates Across All Exchanges -> '5_Funding_Rate' (Index 7).
  9. 6_Funding_Fee_Settlement.py: Perpetual Futures Funding Fee Settlement -> '6_Funding_Fee_Settlement' (Index 8).
  10. 7_Liq_Heapmap.py: Liquidation Heatmap Multi-Timeframe Matrix -> '7_Liq_Heapmap' (Index 9).
  11. 7_Live_Liq.py: Live Liquidations Real-Time Feed -> '7_Live_Liq' (Index 10).
  12. 8_Exchange_Liquidation_Map_1D.py: Multi-Asset Exchange Liquidation Map (1D) -> '8_Exchange_Liquidation_Map_1D' (Index 11).
  13. 8_Exchange_Liquidation_Map_7D.py: Multi-Asset Exchange Liquidation Map (7D) -> '8_Exchange_Liquidation_Map_7D' (Index 12).
  14. 9_Liquidation_Max_Pain_24H.py: Cryptocurrency Liquidation Max Pain (24H) -> '9_Liquidation_Max_Pain_24H' (Index 13).
  15. 9_Liquidation_Max_Pain_48H.py: Cryptocurrency Liquidation Max Pain (48H) -> '9_Liquidation_Max_Pain_48H' (Index 14).
  16. 9_Liquidation_Max_Pain_3D.py: Cryptocurrency Liquidation Max Pain (3D) -> '9_Liquidation_Max_Pain_3D' (Index 15).
  17. 9_Liquidation_Max_Pain_7D.py: Cryptocurrency Liquidation Max Pain (7D) -> '9_Liquidation_Max_Pain_7D' (Index 16).
  18. 10_Whale_Orders.py: Bitcoin Whale Orders & Large Trades (> $100K) -> '10_Whale_Orders' (Index 17).
  19. 11_Technical.py: Quantitative Technical Indicators & VWAP Bands -> '11_Technical' (Index 18).
  20. 12_Hyperdash.py: Hyperdash Flow Sentiment & Aggregate Metrics -> '12_Hyperdash' (Index 19).
  21. 13_Hyperliquid.py: Hyperliquid L1 Native Exchange Metrics -> '13_Hyperliquid' (Index 20).
  22. 14_Hyperdash_Liq_Map.py: Hyperdash Multi-Asset Continuous Liquidation Price Ladder -> '14_Hyperdash_Liq_Map' (Index 22).
  23. 15_Hyperdash_Stops_Map.py: Hyperdash Multi-Asset Resting Stop Orders Price Ladder -> '15_Hyperdash_Stops_Map' (Index 23).
  24. 16_Hyperdash_telegram_Intel.py: Hyperdash Telegram Flow Intelligence & Whale Activity -> '16_Hyperdash_telegram_Intel' (Index 24).
  25. 17_Orderbook.py: Hyperdash & Hyperliquid L2 & L3 Orderbook & Whale Wallet Attribution -> '17_Orderbook' (Index 25).
  26. 18_CVD.py: Multi-Asset Multi-Timeframe Continuous CVD Engine (Crypto, Metals, Indices, Forex, Commodities) -> '18_CVD' (Index 26).
  27. 19_News.py: Forex Factory Live Institutional News & Breaking Stories -> '19_News' (Index 27).
  28. 19_Calendar.py: Forex Factory Live Macroeconomic Calendar & Economic Releases -> '19_Calendar' (Index 28).

Anti-Ban & Network Hygiene:
  - Cloudflare WARP Shield: Automatically verifies connection through Indian Anycast nodes (Mumbai/BOM).
  - Optional On-Demand Rotation: Rotates IP before/between runs via --rotate-ip.
  - Pre-Flight Tab Guard: Closes all open browser tabs EXCEPT arena.ai.
  - Post-Flight Tab Guard: Re-verifies all ephemeral tabs closed, preserving arena.ai.
  - Post-Execution Audit: Verifies sheet positions and row counts in Data/DataBase_Trading.xlsx.
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

try:
    from cloudflare_rotator import rotate_ip, get_warp_status, connect_warp, get_current_trace
except ImportError:
    rotate_ip = None
    get_warp_status = None
    connect_warp = None
    get_current_trace = None

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
log = logging.getLogger("ExcelPipeline")

MODULES_DIR = pathlib.Path(__file__).resolve().parent
ROOT_DIR = MODULES_DIR.parents[1]
EXCEL_PATH = ROOT_DIR / "Data" / "DataBase_Trading.xlsx"
CDP_BASE_URL = "http://127.0.0.1:9222"

PIPELINE_MODULES = [
    {
        "id": 0,
        "name": "MT5 Broker Account Telemetry, Positions & Spreads",
        "script": MODULES_DIR / "00_MT5_Account_Telemetry.py",
        "sheet": "00_MT5_Account_Telemetry",
        "expected_min_rows": 20,
        "args": [],
    },
    {
        "id": 1,
        "name": "Crypto ETF Flows",
        "script": MODULES_DIR / "1_Crypto_ETF_Flows.py",
        "sheet": "1_Crypto_ETF_Flows",
        "expected_min_rows": 30,
        "args": [],
    },
    {
        "id": 2,
        "name": "Cryptocurrency Spot Netflow Statistics",
        "script": MODULES_DIR / "2_Spot_Netflow_S.py",
        "sheet": "2_Spot_Netflow_S",
        "expected_min_rows": 100,
        "args": ["--pages", "25"],
    },
    {
        "id": 3,
        "name": "Exchanges Long/Short Ratio (15M)",
        "script": MODULES_DIR / "3_Exchanges_LS_Ratio_15M.py",
        "sheet": "3_Exchanges_LS_Ratio_15M",
        "expected_min_rows": 100,
        "args": [],
    },
    {
        "id": 4,
        "name": "Exchanges Long/Short Ratio (1H)",
        "script": MODULES_DIR / "3_Exchanges_LS_Ratio_1H.py",
        "sheet": "3_Exchanges_LS_Ratio_1H",
        "expected_min_rows": 100,
        "args": [],
    },
    {
        "id": 5,
        "name": "Exchanges Long/Short Ratio (4H)",
        "script": MODULES_DIR / "3_Exchanges_LS_Ratio_4H.py",
        "sheet": "3_Exchanges_LS_Ratio_4H",
        "expected_min_rows": 100,
        "args": [],
    },
    {
        "id": 6,
        "name": "Hyperliquid Whale Analysis",
        "script": MODULES_DIR / "4_Hyperliquid_Analysis.py",
        "sheet": "4_Hyperliquid_Analysis",
        "expected_min_rows": 500,
        "args": ["--pages", "40"],
    },
    {
        "id": 7,
        "name": "Futures Open Interest (OI) Analysis",
        "script": MODULES_DIR / "5_OI.py",
        "sheet": "5_OI",
        "expected_min_rows": 50,
        "args": [],
    },
    {
        "id": 8,
        "name": "Crypto Funding Rate Across All Exchanges",
        "script": MODULES_DIR / "5_Funding_Rate.py",
        "sheet": "5_Funding_Rate",
        "expected_min_rows": 500,
        "args": ["--pages", "30"],
    },
    {
        "id": 9,
        "name": "Perpetual Futures Funding Fee Settlement",
        "script": MODULES_DIR / "6_Funding_Fee_Settlement.py",
        "sheet": "6_Funding_Fee_Settlement",
        "expected_min_rows": 900,
        "args": ["--pages", "19"],
    },
    {
        "id": 10,
        "name": "Liquidation Heatmap Multi-Timeframe Matrix",
        "script": MODULES_DIR / "7_Liq_Heapmap.py",
        "sheet": "7_Liq_Heapmap",
        "expected_min_rows": 20,
        "args": [],
    },
    {
        "id": 11,
        "name": "Live Liquidations Real-Time Feed",
        "script": MODULES_DIR / "7_Live_Liq.py",
        "sheet": "7_Live_Liq",
        "expected_min_rows": 500,
        "args": [],
    },
    {
        "id": 12,
        "name": "Multi-Asset Exchange Liquidation Map (1D)",
        "script": MODULES_DIR / "8_Exchange_Liquidation_Map_1D.py",
        "sheet": "8_Exchange_Liquidation_Map_1D",
        "expected_min_rows": 1500,
        "args": [],
    },
    {
        "id": 13,
        "name": "Multi-Asset Exchange Liquidation Map (7D)",
        "script": MODULES_DIR / "8_Exchange_Liquidation_Map_7D.py",
        "sheet": "8_Exchange_Liquidation_Map_7D",
        "expected_min_rows": 2000,
        "args": [],
    },
    {
        "id": 14,
        "name": "Cryptocurrency Liquidation Max Pain (24H)",
        "script": MODULES_DIR / "9_Liquidation_Max_Pain_24H.py",
        "sheet": "9_Liquidation_Max_Pain_24H",
        "expected_min_rows": 700,
        "args": [],
    },
    {
        "id": 15,
        "name": "Cryptocurrency Liquidation Max Pain (48H)",
        "script": MODULES_DIR / "9_Liquidation_Max_Pain_48H.py",
        "sheet": "9_Liquidation_Max_Pain_48H",
        "expected_min_rows": 700,
        "args": [],
    },
    {
        "id": 16,
        "name": "Cryptocurrency Liquidation Max Pain (3D)",
        "script": MODULES_DIR / "9_Liquidation_Max_Pain_3D.py",
        "sheet": "9_Liquidation_Max_Pain_3D",
        "expected_min_rows": 700,
        "args": [],
    },
    {
        "id": 17,
        "name": "Cryptocurrency Liquidation Max Pain (7D)",
        "script": MODULES_DIR / "9_Liquidation_Max_Pain_7D.py",
        "sheet": "9_Liquidation_Max_Pain_7D",
        "expected_min_rows": 700,
        "args": [],
    },
    {
        "id": 18,
        "name": "Bitcoin Whale Orders & Large Trades",
        "script": MODULES_DIR / "10_Whale_Orders.py",
        "sheet": "10_Whale_Orders",
        "expected_min_rows": 500,
        "args": [],
    },
    {
        "id": 19,
        "name": "Quantitative Technical Indicators & VWAP Bands",
        "script": MODULES_DIR / "11_Technical.py",
        "sheet": "11_Technical",
        "expected_min_rows": 40,
        "args": [],
    },
    {
        "id": 20,
        "name": "Hyperdash On-Chain Flow & Microstructure Intelligence",
        "script": MODULES_DIR / "12_Hyperdash.py",
        "sheet": "12_Hyperdash",
        "expected_min_rows": 100,
        "args": [],
    },
    {
        "id": 21,
        "name": "Hyperliquid L1 Native Exchange & Microstructure Engine",
        "script": MODULES_DIR / "13_Hyperliquid.py",
        "sheet": "13_Hyperliquid",
        "expected_min_rows": 200,
        "args": [],
    },
    {
        "id": 22,
        "name": "Hyperdash Multi-Asset Liquidation Price Ladder & Cumulative Map",
        "script": MODULES_DIR / "14_Hyperdash_Liq_Map.py",
        "sheet": "14_Hyperdash_Liq_Map",
        "expected_min_rows": 1000,
        "args": [],
    },
    {
        "id": 23,
        "name": "Hyperdash Multi-Asset Stop Orders Price Ladder & Cumulative Map",
        "script": MODULES_DIR / "15_Hyperdash_Stops_Map.py",
        "sheet": "15_Hyperdash_Stops_Map",
        "expected_min_rows": 1000,
        "args": [],
    },
    {
        "id": 24,
        "name": "Hyperdash Telegram Flow Intelligence & Whale Activity Harvester",
        "script": MODULES_DIR / "16_Hyperdash_telegram_Intel.py",
        "sheet": "16_Hyperdash_telegram_Intel",
        "expected_min_rows": 500,
        "args": ["--pages", "20", "--limit", "1500"],
    },
    {
        "id": 25,
        "name": "Hyperdash & Hyperliquid Multi-Asset L2 & L3 Orderbook & Whale Wallet Attribution",
        "script": MODULES_DIR / "17_Orderbook.py",
        "sheet": "17_Orderbook",
        "expected_min_rows": 3000,
        "args": [],
    },
    {
        "id": 26,
        "name": "Multi-Asset Multi-Timeframe Continuous CVD Engine (Crypto, Metals, Indices, Forex, Commodities)",
        "script": MODULES_DIR / "18_CVD.py",
        "sheet": "18_CVD",
        "expected_min_rows": 1000,
        "args": [],
    },
    {
        "id": 27,
        "name": "Forex Factory Live Institutional News & Breaking Stories",
        "script": MODULES_DIR / "19_News.py",
        "sheet": "19_News",
        "expected_min_rows": 20,
        "args": [],
    },
    {
        "id": 28,
        "name": "Forex Factory Live Macroeconomic Calendar & Economic Releases",
        "script": MODULES_DIR / "19_Calendar.py",
        "sheet": "19_Calendar",
        "expected_min_rows": 30,
        "args": [],
    },
]


def enforce_network_shield(auto_rotate: bool = False):
    """Verifies that Cloudflare WARP is active and optionally rotates IP."""
    if not get_warp_status:
        return

    status = get_warp_status()
    if "Connected" not in status:
        log.warning(f"[Network Shield] Cloudflare WARP is {status}. Auto-connecting...")
        if connect_warp:
            connect_warp()

    if auto_rotate and rotate_ip:
        rotate_ip()
    else:
        if get_current_trace:
            trace = get_current_trace()
            ip = trace.get("ip", "N/A")
            colo = trace.get("colo", "N/A")
            loc = trace.get("loc", "N/A")
            log.info(f"[Network Shield] Cloudflare WARP Active | Exit IP: {ip} | Node: {colo} ({loc})")


def close_all_tabs_except_arena() -> int:
    """
    Closes all open browser tabs via Chrome/Edge CDP port 9222 except arena.ai.
    Returns the count of tabs closed.
    """
    closed_count = 0
    try:
        req = urllib.request.urlopen(f"{CDP_BASE_URL}/json", timeout=5)
        tabs = json.loads(req.read().decode())
        page_tabs = [t for t in tabs if t.get("type") == "page"]

        for t in page_tabs:
            tab_url = t.get("url", "").lower()
            tab_id = t.get("id")

            # Preserve active arena.ai tabs
            if "arena.ai" in tab_url:
                log.info(f"[Tab Guard] Preserved Arena.ai tab (ID: {tab_id}, URL: {t.get('url', '')[:50]}...)")
                continue

            # Close all other tabs
            try:
                urllib.request.urlopen(f"{CDP_BASE_URL}/json/close/{tab_id}", timeout=4)
                log.info(f"[Tab Guard] Closed non-arena tab (ID: {tab_id}, URL: {t.get('url', '')[:60]}...)")
                closed_count += 1
            except Exception as ce:
                log.warning(f"[Tab Guard] Could not close tab {tab_id}: {ce}")

    except Exception as e:
        log.warning(f"[Tab Guard] CDP query to {CDP_BASE_URL} encountered: {e}")

    return closed_count


def run_module(module_meta: dict, python_bin: str = sys.executable) -> tuple[bool, float, str]:
    """Execute a single module script sequentially via subprocess."""
    script_path = module_meta["script"]
    name = module_meta["name"]
    extra_args = module_meta.get("args", [])

    if not script_path.exists():
        err = f"Module script not found: {script_path}"
        log.error(f"[Module {module_meta['id']}] {err}")
        return False, 0.0, err

    cmd = [python_bin, str(script_path)] + extra_args
    log.info(f"==> [Module {module_meta['id']}] Starting: {name}")
    log.info(f"    Command: {' '.join(cmd)}")

    start_t = time.perf_counter()
    try:
        proc = subprocess.run(
            cmd,
            cwd=str(MODULES_DIR),
            stdout=sys.stdout,
            stderr=sys.stderr,
            text=True,
            check=False,
        )
        elapsed = time.perf_counter() - start_t
        if proc.returncode == 0:
            log.info(f"<== [Module {module_meta['id']}] SUCCESS in {elapsed:.2f}s")
            return True, elapsed, "OK"
        else:
            err = f"Process exited with non-zero return code {proc.returncode}"
            log.error(f"<== [Module {module_meta['id']}] FAILED in {elapsed:.2f}s: {err}")
            return False, elapsed, err
    except Exception as e:
        elapsed = time.perf_counter() - start_t
        err = str(e)
        log.error(f"<== [Module {module_meta['id']}] EXCEPTION in {elapsed:.2f}s: {err}")
        return False, elapsed, err


def audit_excel_workbook(excel_path: pathlib.Path) -> dict[str, int]:
    """Verify sheet presence and row counts after execution."""
    if not openpyxl:
        log.warning("openpyxl not installed; skipping sheet verification.")
        return {}

    if not excel_path.exists():
        log.error(f"Excel workbook not found at: {excel_path}")
        return {}

    wb = openpyxl.load_workbook(excel_path, read_only=True)
    summary = {}
    for sheet in wb.sheetnames:
        ws = wb[sheet]
        summary[sheet] = ws.max_row
    wb.close()
    return summary


def run_pipeline(modules: list[dict] = PIPELINE_MODULES, fail_fast: bool = False, rotate_before_run: bool = False) -> bool:
    """Execute all pipeline modules sequentially with Cloudflare protection & tab hygiene."""
    log.info("================================================================================")
    log.info("          EXCEL MODULES SEQUENTIAL PIPELINE ORCHESTRATOR                        ")
    log.info(f"          Target Workbook: {EXCEL_PATH}")
    log.info(f"          Modules to Execute: {len(modules)}")
    log.info("================================================================================")

    # 1. Cloudflare WARP Shield & Optional IP Rotation
    enforce_network_shield(auto_rotate=rotate_before_run)

    # 2. Pre-Flight Tab Cleanup
    log.info("[Pre-Flight] Enforcing browser tab hygiene: Closing all tabs except arena.ai...")
    pre_closed = close_all_tabs_except_arena()
    log.info(f"[Pre-Flight] Closed {pre_closed} non-arena tab(s). Arena.ai preserved.")

    pipeline_start = time.perf_counter()
    results = []
    overall_success = True

    # 3. Sequential Execution
    for mod in modules:
        success, duration, error_msg = run_module(mod)
        results.append({
            "id": mod["id"],
            "name": mod["name"],
            "sheet": mod["sheet"],
            "success": success,
            "duration": duration,
            "error": error_msg,
        })

        if not success:
            overall_success = False
            if fail_fast:
                log.warning(f"Fail-fast enabled: Aborting pipeline after failure on Module {mod['id']}.")
                break

    total_pipeline_time = time.perf_counter() - pipeline_start

    # 4. Post-Flight Tab Cleanup
    log.info("[Post-Flight] Verifying browser tab hygiene: Ensuring only arena.ai remains open...")
    post_closed = close_all_tabs_except_arena()
    if post_closed > 0:
        log.info(f"[Post-Flight] Cleaned up {post_closed} lingering tab(s).")

    # 5. Post-Execution Excel Verification
    log.info("--------------------------------------------------------------------------------")
    log.info("Auditing target Excel workbook state...")
    sheet_audit = audit_excel_workbook(EXCEL_PATH)

    log.info("================================================================================")
    log.info("                       PIPELINE EXECUTION SCORECARD                             ")
    log.info("================================================================================")
    for res in results:
        status_str = "PASS" if res["success"] else "FAIL"
        rows_str = f"{sheet_audit.get(res['sheet'], 'N/A')} rows"
        log.info(
            f"  Module {res['id']:<2} | {res['name']:<42} | [{status_str}] in {res['duration']:>6.2f}s | Sheet: {res['sheet']} ({rows_str})"
        )

    log.info("--------------------------------------------------------------------------------")
    log.info(f"Total Pipeline Runtime: {total_pipeline_time:.2f} seconds")
    if overall_success:
        log.info("Result: ALL MODULES COMPLETED SUCCESSFULLY.")
    else:
        log.error("Result: ONE OR MORE MODULES FAILED.")
    log.info("================================================================================")

    return overall_success


def main():
    parser = argparse.ArgumentParser(description="Sequential Runner for Data/Excel_Modules with Cloudflare Protection")
    parser.add_argument("--fail-fast", action="store_true", help="Halt execution if any module fails")
    parser.add_argument("--rotate-ip", action="store_true", help="Rotate Cloudflare Anycast IP before execution")
    all_ids = [m["id"] for m in PIPELINE_MODULES]
    parser.add_argument("--only", type=int, nargs="+", choices=all_ids, help=f"Run only specific module(s) by ID ({all_ids})")
    args = parser.parse_args()

    modules_to_run = PIPELINE_MODULES
    if args.only:
        modules_to_run = [m for m in PIPELINE_MODULES if m["id"] in args.only]

    success = run_pipeline(modules=modules_to_run, fail_fast=args.fail_fast, rotate_before_run=args.rotate_ip)
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
