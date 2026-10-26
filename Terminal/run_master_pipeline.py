#!/usr/bin/env python3
"""
Terminal/run_master_pipeline.py
===============================
Master Unified Quantitative Data Pipeline Runner.
Orchestrates end-to-end execution across:
  1. Pure-API Feeds (18 high-velocity & tactical feeds executed in parallel, < 10s)
  2. Browser CDP Feeds (14 macro & tactical feeds with strict Edge tab hygiene)
  3. Master Scorecard Auditor (Validates 33 canonical feeds & refreshes 23_Master_Pipeline_Telemetry)

Usage:
  python Terminal/run_master_pipeline.py              # Full pipeline (API + Browser + Audit)
  python Terminal/run_master_pipeline.py --api-only   # High-speed API refresh (< 10s)
  python Terminal/run_master_pipeline.py --audit-only # Instant freshness scorecard check
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

ROOT_DIR = pathlib.Path(__file__).resolve().parents[1]
COLLECTORS_API_DIR = ROOT_DIR / "Collectors" / "API"
COLLECTORS_BROWSER_DIR = ROOT_DIR / "Collectors" / "Browser"
LOG_DIR = ROOT_DIR / "logs"
LOG_DIR.mkdir(parents=True, exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] [MasterPipeline] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    handlers=[
        logging.StreamHandler(sys.stdout),
        logging.FileHandler(LOG_DIR / "master_pipeline.log", encoding="utf-8"),
    ],
)
log = logging.getLogger("MasterPipeline")

# 12 Pure-API Collectors
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

# 20 Browser CDP Collectors
BROWSER_COLLECTORS = [
    "1_Crypto_ETF_Flows.py",
    "2_Spot_Netflow_S.py",
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


def run_script(script_path: pathlib.Path, timeout: int = 120) -> tuple[str, bool, float, str]:
    """Runs a single collector script with elapsed time tracking."""
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


def run_api_phase(parallel: bool = True) -> int:
    """Executes all 18 Pure-API collectors in parallel or batch."""
    log.info("=" * 80)
    log.info(f"   PHASE 1: EXECUTING {len(API_COLLECTORS)} PURE-API COLLECTORS")
    log.info("=" * 80)
    t0 = time.perf_counter()
    failures = 0

    scripts = [COLLECTORS_API_DIR / s for s in API_COLLECTORS if (COLLECTORS_API_DIR / s).exists()]

    if parallel:
        with concurrent.futures.ThreadPoolExecutor(max_workers=6) as executor:
            future_to_script = {executor.submit(run_script, s, 120): s for s in scripts}
            for future in concurrent.futures.as_completed(future_to_script):
                name, success, dt, err = future.result()
                status = "PASS" if success else "FAIL"
                if not success:
                    failures += 1
                    log.error(f"  [API] {name:<35} [{status}] ({dt:.2f}s) - Error: {err[:100]}")
                else:
                    log.info(f"  [API] {name:<35} [{status}] ({dt:.2f}s)")
    else:
        for s in scripts:
            name, success, dt, err = run_script(s, 120)
            status = "PASS" if success else "FAIL"
            if not success:
                failures += 1
                log.error(f"  [API] {name:<35} [{status}] ({dt:.2f}s) - Error: {err[:100]}")
            else:
                log.info(f"  [API] {name:<35} [{status}] ({dt:.2f}s)")

    total_dt = time.perf_counter() - t0
    log.info(f"Phase 1 Complete in {total_dt:.2f}s. Failures: {failures}/{len(scripts)}")
    return failures


def cleanup_browser_tabs() -> int:
    """Closes all collector ephemeral tabs via CDP while protecting Arena and Z.ai."""
    closed_count = 0
    try:
        req = urllib.request.Request("http://127.0.0.1:9222/json", timeout=3)
        with urllib.request.urlopen(req) as resp:
            tabs = json.loads(resp.read().decode("utf-8"))
        for t in tabs:
            if t.get("type") != "page":
                continue
            url = t.get("url", "").lower()
            title = t.get("title", "").lower()
            # NEVER close Arena, Z.ai, or default empty tab
            if "arena.ai" in url or "chat.z.ai" in url or "z.ai" in url:
                continue
            if url.startswith("edge://newtab") or url.startswith("chrome://"):
                continue
            # Close collector tabs
            if any(k in url for k in ["coinglass.com", "forexfactory.com", "hyperliquid", "about:blank"]) or \
               any(k in title for k in ["coinglass", "forex factory"]):
                tab_id = t.get("id")
                try:
                    urllib.request.urlopen(f"http://127.0.0.1:9222/json/close/{tab_id}", timeout=3)
                    closed_count += 1
                except Exception:
                    pass
    except Exception as e:
        log.debug(f"cleanup_browser_tabs notice: {e}")
    return closed_count


def run_browser_phase() -> int:
    """Executes the Browser CDP collectors sequentially with strict tab hygiene."""
    log.info("=" * 80)
    log.info(f"   PHASE 2: EXECUTING {len(BROWSER_COLLECTORS)} BROWSER CDP COLLECTORS")
    log.info("=" * 80)
    t0 = time.perf_counter()
    failures = 0

    cleanup_browser_tabs()

    scripts = [COLLECTORS_BROWSER_DIR / s for s in BROWSER_COLLECTORS if (COLLECTORS_BROWSER_DIR / s).exists()]
    for s in scripts:
        # Enforce clean slate: close any lingering collector tabs before launching next collector
        cleanup_browser_tabs()
        timeout = 180 if s.name in ["5_OI.py", "25_CoinGlass_Footprint_Signals.py", "8_Exchange_Liquidation_Map_7D.py", "10_Whale_Orders.py"] else 120
        name, success, dt, err = run_script(s, timeout)
        status = "PASS" if success else "FAIL"
        if not success:
            failures += 1
            log.warning(f"  [Browser] {name:<35} [{status}] ({dt:.2f}s) - Notice: {err[:100]}")
        else:
            log.info(f"  [Browser] {name:<35} [{status}] ({dt:.2f}s)")

        # Enforce instant tab hygiene after every collector
        cleanup_browser_tabs()

    cleanup_browser_tabs()
    total_dt = time.perf_counter() - t0
    log.info(f"Phase 2 Complete in {total_dt:.2f}s. Failures: {failures}/{len(scripts)}")
    return failures


def run_post_processing_phase() -> bool:
    """Executes post-processing engines: Unified Liquidation Matrix across all venues."""
    log.info("=" * 80)
    log.info("   PHASE 2.5: UNIFIED MULTI-VENUE LIQUIDATION MATRIX SYNTHESIS")
    log.info("=" * 80)
    matrix_script = ROOT_DIR / "Terminal" / "Data_Factory" / "unified_liquidation_matrix.py"
    if not matrix_script.exists():
        log.warning("unified_liquidation_matrix.py not found.")
        return False
    proc = subprocess.run([sys.executable, str(matrix_script)], cwd=str(ROOT_DIR))
    return proc.returncode == 0


def run_audit_phase() -> bool:
    """Executes the 33-feed freshness & health scorecard auditor."""
    log.info("=" * 80)
    log.info("   PHASE 3: EXECUTING 33-FEED FRESHNESS & HEALTH SCORECARD AUDIT")
    log.info("=" * 80)
    auditor_script = ROOT_DIR / "Terminal" / "parquet_checklist_auditor.py"
    if not auditor_script.exists():
        log.error("Auditor script missing.")
        return False
    proc = subprocess.run([sys.executable, str(auditor_script)], cwd=str(ROOT_DIR))
    return proc.returncode == 0


def main():
    parser = argparse.ArgumentParser(description="Master Unified Quantitative Data Pipeline Runner")
    parser.add_argument("--api-only", action="store_true", help="Run only the 18 Pure-API collectors (< 10s)")
    parser.add_argument("--browser-only", action="store_true", help="Run only the 14 Browser collectors")
    parser.add_argument("--audit-only", action="store_true", help="Run only the freshness scorecard audit")
    parser.add_argument("--sequential", action="store_true", help="Run API collectors sequentially instead of in parallel")
    args = parser.parse_args()

    t_start = time.perf_counter()

    if args.audit_only:
        all_passed = run_audit_phase()
        sys.exit(0 if all_passed else 1)

    if not args.browser_only:
        run_api_phase(parallel=not args.sequential)

    if not args.api_only:
        run_browser_phase()

    # Always synthesize Unified Liquidation Matrix
    run_post_processing_phase()

    all_passed = run_audit_phase()
    cleanup_browser_tabs()
    total_time = time.perf_counter() - t_start
    log.info(f"Master Pipeline Execution Finished in {total_time:.2f}s. All Feeds Healthy: {all_passed}")
    cleanup_browser_tabs()
    sys.exit(0 if all_passed else 1)


if __name__ == "__main__":
    main()
