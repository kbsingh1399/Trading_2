"""
API Parallel Harvester (Tier 1A Producer)
Executes all pure REST and WebSocket API data collectors concurrently using a thread pool.
Bypasses sequential execution bottlenecks and completes the entire API suite in parallel.
Can run in one-shot mode or as a continuous 60-second background daemon.
"""

from __future__ import annotations

import argparse
from concurrent.futures import ThreadPoolExecutor, as_completed
import datetime
import pathlib
import subprocess
import sys
import time

from logger_config import emit_telemetry_event, get_system_ram_telemetry, setup_institutional_logger

MODULES_DIR = pathlib.Path(__file__).resolve().parent
ROOT_DIR = MODULES_DIR.parents[1]

log = setup_institutional_logger("APIHarvester")

# All pure API modules (Zero browser / Zero CDP requirements)
API_MODULES = [
    {
        "id": 1,
        "name": "Crypto ETF Flows",
        "script": MODULES_DIR / "1_Crypto_ETF_Flows.py",
        "sheet": "1_Crypto_ETF_Flows",
        "timeout": 120,
    },
    {
        "id": 6,
        "name": "Hyperliquid Whale Analysis",
        "script": MODULES_DIR / "4_Hyperliquid_Analysis.py",
        "sheet": "4_Hyperliquid_Analysis",
        "timeout": 120,
    },
    {
        "id": 7,
        "name": "Futures Open Interest Analysis",
        "script": MODULES_DIR / "5_OI.py",
        "sheet": "5_OI",
        "timeout": 180,
    },
    {
        "id": 8,
        "name": "Crypto Funding Rate Across Exchanges",
        "script": MODULES_DIR / "5_Funding_Rate.py",
        "sheet": "5_Funding_Rate",
        "timeout": 180,
    },
    {
        "id": 9,
        "name": "Funding Fee Settlement",
        "script": MODULES_DIR / "6_Funding_Fee_Settlement.py",
        "sheet": "6_Funding_Fee_Settlement",
        "timeout": 120,
    },
    {
        "id": 19,
        "name": "Quantitative Technical Indicators & VWAP",
        "script": MODULES_DIR / "11_Technical.py",
        "sheet": "11_Technical",
        "timeout": 180,
    },
    {
        "id": 20,
        "name": "Hyperdash On-Chain Flow Intelligence",
        "script": MODULES_DIR / "12_Hyperdash.py",
        "sheet": "12_Hyperdash",
        "timeout": 120,
    },
    {
        "id": 21,
        "name": "Hyperliquid L1 Native Exchange Engine",
        "script": MODULES_DIR / "13_Hyperliquid.py",
        "sheet": "13_Hyperliquid",
        "timeout": 120,
    },
    {
        "id": 22,
        "name": "Hyperdash Liquidation Price Ladder",
        "script": MODULES_DIR / "14_Hyperdash_Liq_Map.py",
        "sheet": "14_Hyperdash_Liq_Map",
        "timeout": 120,
    },
    {
        "id": 23,
        "name": "Hyperdash Stop Orders Price Ladder",
        "script": MODULES_DIR / "15_Hyperdash_Stops_Map.py",
        "sheet": "15_Hyperdash_Stops_Map",
        "timeout": 120,
    },
    {
        "id": 24,
        "name": "Hyperdash Telegram Flow Intelligence",
        "script": MODULES_DIR / "16_Hyperdash_telegram_Intel.py",
        "sheet": "16_Hyperdash_telegram_Intel",
        "timeout": 120,
    },
    {
        "id": 25,
        "name": "Hyperdash L2/L3 Orderbook & Whale Attribution",
        "script": MODULES_DIR / "17_Orderbook.py",
        "sheet": "17_Orderbook",
        "timeout": 180,
    },
    {
        "id": 26,
        "name": "Continuous Multi-Asset CVD Engine",
        "script": MODULES_DIR / "18_CVD.py",
        "sheet": "18_CVD",
        "timeout": 240,
    },
]


def run_single_api_collector(module_meta: dict) -> tuple[int, str, bool, float, str]:
    """Worker task executing a single API collector subprocess."""
    mid = module_meta["id"]
    name = module_meta["name"]
    sheet = module_meta["sheet"]
    script_path = module_meta["script"]
    timeout_sec = module_meta.get("timeout", 60)

    if not script_path.exists():
        return mid, sheet, False, 0.0, "Script not found"

    cmd = [sys.executable, str(script_path)]
    t0 = time.perf_counter()

    try:
        proc = subprocess.run(
            cmd,
            cwd=str(MODULES_DIR),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            timeout=timeout_sec,
            check=False,
        )
        elapsed = time.perf_counter() - t0
        success = (proc.returncode == 0)
        status_str = "PASS" if success else "FAIL"
        err = "OK" if success else (proc.stderr.strip()[-200:] if proc.stderr else f"Exit code {proc.returncode}")

        emit_telemetry_event(
            event_type="API_PARALLEL_HARVEST",
            module_id=mid,
            sheet=sheet,
            status=status_str,
            duration=elapsed,
            metadata={"name": name},
        )
        return mid, sheet, success, elapsed, err

    except subprocess.TimeoutExpired:
        elapsed = time.perf_counter() - t0
        return mid, sheet, False, elapsed, "TimeoutExpired"
    except Exception as e:
        elapsed = time.perf_counter() - t0
        return mid, sheet, False, elapsed, str(e)


def execute_parallel_api_harvest(max_workers: int = 6) -> dict:
    """Executes all registered API collectors concurrently across a thread pool."""
    log.info("================================================================================")
    log.info(f"     PARALLEL API HARVESTER: Launching {len(API_MODULES)} modules ({max_workers} concurrent workers)     ")
    log.info("================================================================================")

    t_start = time.perf_counter()
    results = []

    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        future_map = {
            executor.submit(run_single_api_collector, mod): mod
            for mod in API_MODULES
        }

        for future in as_completed(future_map):
            mod = future_map[future]
            try:
                mid, sheet, success, duration, err = future.result()
                status_str = "PASS" if success else "FAIL"
                log.info(f"  [Module {mid:>2}] {sheet:<30} | [{status_str}] in {duration:>6.2f}s")
                results.append({
                    "id": mid,
                    "sheet": sheet,
                    "success": success,
                    "duration": duration,
                    "error": err,
                })
            except Exception as exc:
                log.error(f"  [Module {mod['id']:>2}] Exception in future: {exc}")

    total_time = time.perf_counter() - t_start
    passed = sum(1 for r in results if r["success"])
    log.info("--------------------------------------------------------------------------------")
    log.info(f"Parallel API Harvest Complete: {passed}/{len(API_MODULES)} PASS in {total_time:.2f}s total wall clock time.")
    log.info("================================================================================")

    return {
        "passed": passed,
        "total": len(API_MODULES),
        "total_wall_time": total_time,
        "results": results,
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Parallel API Harvester")
    parser.add_argument("--workers", type=int, default=6, help="Concurrent worker count")
    parser.add_argument("--loop", action="store_true", help="Run continuously with 60-second interval")
    parser.add_argument("--interval", type=int, default=60, help="Interval in seconds for loop mode")
    args = parser.parse_args()

    if args.loop:
        log.info(f"[APIHarvester] Starting continuous 60s loop (interval={args.interval}s)...")
        while True:
            try:
                execute_parallel_api_harvest(max_workers=args.workers)
            except Exception as e:
                log.error(f"[APIHarvester] Error in cycle: {e}")
            time.sleep(args.interval)
    else:
        execute_parallel_api_harvest(max_workers=args.workers)
