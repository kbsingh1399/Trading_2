"""
Master Parallel Pipeline Orchestrator
Optimizes data harvesting by replacing the 18-minute sequential pipeline with:
1. Parallel API Harvester (Tier 1A): Concurrent multi-threaded API requests (every 60 seconds).
2. Staggered Edge CDP Worker (Tier 1B): Single-tab browser queue on Edge port 9222 (every 5 minutes).
3. Fast Excel Batch Committer (Tier 2): Single atomic openpyxl write pass (12-15 seconds).
4. Enterprise Logging & Telemetry: Rotating 50MB log file + JSONL telemetry stream + RAM metrics.
"""

from __future__ import annotations

import argparse
import datetime
import os
import pathlib
import sys
import threading
import time
import urllib.request

from logger_config import emit_telemetry_event, get_system_ram_telemetry, setup_institutional_logger
from api_parallel_harvester import execute_parallel_api_harvest
from cdp_edge_queue_worker import run_cdp_queue_cycle, verify_edge_cdp_and_arena
from Fast_Excel_Batch_Committer import commit_staged_sheets

MODULES_DIR = pathlib.Path(__file__).resolve().parent
ROOT_DIR = MODULES_DIR.parents[1]
EXCEL_PATH = ROOT_DIR / "Data" / "DataBase_Trading.xlsx"

log = setup_institutional_logger("ParallelPipeline")


def run_full_parallel_cycle(workers: int = 6) -> dict:
    """
    Executes one complete optimized parallel cycle:
    1. Runs pure API modules concurrently across a thread pool.
    2. Runs browser CDP modules through the Edge queue worker.
    3. Commits all staged data in a single atomic pass to Excel.
    """
    t0 = time.perf_counter()
    ram_pre = get_system_ram_telemetry()

    log.info("================================================================================")
    log.info("             STARTING HIGH-PERFORMANCE PARALLEL PIPELINE CYCLE                  ")
    log.info(f"             Target Workbook: {EXCEL_PATH.name}                                 ")
    log.info(f"             System RAM: {ram_pre['used_mb']} MB / {ram_pre['total_mb']} MB ({ram_pre['load_pct']}% load)      ")
    log.info("================================================================================")

    # 1. Edge CDP Verification
    edge_ok, edge_msg = verify_edge_cdp_and_arena()
    if edge_ok:
        log.info(f"[Pre-Flight] {edge_msg}")
    else:
        log.warning(f"[Pre-Flight] Warning: {edge_msg}")

    # 2. Phase 1: Parallel API Harvester
    t_api = time.perf_counter()
    api_summary = execute_parallel_api_harvest(max_workers=workers)
    api_duration = time.perf_counter() - t_api

    # 3. Phase 2: Edge CDP Queue Cycle
    t_cdp = time.perf_counter()
    cdp_summary = run_cdp_queue_cycle()
    cdp_duration = time.perf_counter() - t_cdp

    # 4. Phase 3: Single Atomic Excel Commit
    t_commit = time.perf_counter()
    commit_summary = commit_staged_sheets()
    commit_duration = time.perf_counter() - t_commit

    total_cycle_time = time.perf_counter() - t0
    ram_post = get_system_ram_telemetry()

    log.info("================================================================================")
    log.info("                  PARALLEL PIPELINE CYCLE SCORECARD                             ")
    log.info("================================================================================")
    log.info(f"  Phase 1 | Parallel API Ingestion ({api_summary['passed']}/{api_summary['total']} PASS)     | Duration: {api_duration:>6.2f}s")
    log.info(f"  Phase 2 | Edge CDP Browser Queue ({cdp_summary['passed']}/{cdp_summary['total']} PASS)     | Duration: {cdp_duration:>6.2f}s")
    log.info(f"  Phase 3 | Master Excel Batch Commit ({commit_summary.get('updated', 0)} sheets)       | Duration: {commit_duration:>6.2f}s")
    log.info("--------------------------------------------------------------------------------")
    log.info(f"  Total Cycle Wall-Clock Time: {total_cycle_time:.2f} seconds")
    log.info(f"  System RAM Load: {ram_post['load_pct']}% ({ram_post['used_mb']} MB used)")
    log.info("================================================================================")

    emit_telemetry_event(
        event_type="FULL_PARALLEL_CYCLE",
        status="PASS" if (api_summary["passed"] > 0) else "WARN",
        duration=total_cycle_time,
        metadata={
            "api_passed": api_summary["passed"],
            "cdp_passed": cdp_summary["passed"],
            "sheets_committed": commit_summary.get("updated", 0),
            "ram_load_pct": ram_post["load_pct"],
        },
    )

    return {
        "total_time": total_cycle_time,
        "api": api_summary,
        "cdp": cdp_summary,
        "commit": commit_summary,
    }


def run_continuous_daemon(api_interval: int = 60, cdp_interval: int = 300, workers: int = 6) -> None:
    """
    Runs the dual-cadence asynchronous daemon:
    - Thread 1: Fast API Harvesters loop every 60s (1 min).
    - Thread 2: Edge CDP Queue Worker loops every 300s (5 min).
    - Thread 3: Master Excel Batch Committer loops every 60s.
    """
    log.info("================================================================================")
    log.info("             STARTING CONTINUOUS DUAL-CADENCE BACKGROUND DAEMON                 ")
    log.info(f"             Fast API Ingestion Cadence : Every {api_interval} seconds (1 min)           ")
    log.info(f"             Edge CDP Browser Cadence   : Every {cdp_interval} seconds (5 min)          ")
    log.info(f"             Excel Batch Committer      : Every {api_interval} seconds (Atomic Commit)   ")
    log.info("================================================================================")

    stop_event = threading.Event()

    def api_worker_loop():
        log.info("[Daemon:API] Fast API worker loop started.")
        while not stop_event.is_set():
            try:
                execute_parallel_api_harvest(max_workers=workers)
            except Exception as e:
                log.error(f"[Daemon:API] Exception in API loop: {e}")
            stop_event.wait(api_interval)

    def cdp_worker_loop():
        log.info("[Daemon:CDP] Edge CDP worker loop started.")
        while not stop_event.is_set():
            try:
                run_cdp_queue_cycle()
            except Exception as e:
                log.error(f"[Daemon:CDP] Exception in CDP loop: {e}")
            stop_event.wait(cdp_interval)

    def committer_worker_loop():
        log.info("[Daemon:Committer] Excel batch committer loop started.")
        # Brief initial wait to let producers stage first batch
        stop_event.wait(15)
        while not stop_event.is_set():
            try:
                commit_staged_sheets()
            except Exception as e:
                log.error(f"[Daemon:Committer] Exception in commit loop: {e}")
            stop_event.wait(api_interval)

    t_api = threading.Thread(target=api_worker_loop, name="APIWorkerThread", daemon=True)
    t_cdp = threading.Thread(target=cdp_worker_loop, name="CDPWorkerThread", daemon=True)
    t_committer = threading.Thread(target=committer_worker_loop, name="CommitterThread", daemon=True)

    t_api.start()
    t_cdp.start()
    t_committer.start()

    try:
        while True:
            time.sleep(1.0)
    except KeyboardInterrupt:
        log.info("[Daemon] Shutdown signal received. Stopping threads...")
        stop_event.set()
        t_api.join(timeout=5)
        t_cdp.join(timeout=5)
        t_committer.join(timeout=5)
        log.info("[Daemon] All threads gracefully shut down.")


def run_continuous_cycles(gap_seconds: int = 300, workers: int = 1) -> None:
    """
    Runs full pipeline cycles continuously with an exact gap of gap_seconds (default 300s = 5 min)
    after completion before starting the next cycle.
    Guarantees:
    - 0 race conditions / 0 zip corruption by using sequential execution (workers=1)
    - Full 32-sheet Excel refresh
    - Strict 5-minute cooldown between cycles
    """
    log.info("=" * 80)
    log.info(f"   STARTING CONTINUOUS PIPELINE DAEMON: GAP = {gap_seconds}s ({gap_seconds/60:.1f} min), WORKERS = {workers}")
    log.info("=" * 80)
    cycle = 1
    while True:
        try:
            log.info(f"[ContinuousPipeline] >>> Starting Cycle #{cycle} at {datetime.datetime.now(datetime.timezone.utc).isoformat()}")
            summary = run_full_parallel_cycle(workers=workers)
            log.info(f"[ContinuousPipeline] <<< Cycle #{cycle} completed in {summary['total_time']:.2f}s.")
        except Exception as e:
            log.error(f"[ContinuousPipeline] Exception in Cycle #{cycle}: {e}")

        log.info(f"[ContinuousPipeline] Cooling down for {gap_seconds} seconds ({gap_seconds/60:.1f} minutes) before Cycle #{cycle+1}...")
        try:
            time.sleep(gap_seconds)
        except KeyboardInterrupt:
            log.info("[ContinuousPipeline] Shutdown received during sleep. Exiting.")
            break
        cycle += 1


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Master Parallel Pipeline Orchestrator")
    parser.add_argument("--run-once", action="store_true", help="Execute a single full parallel cycle and exit")
    parser.add_argument("--continuous", action="store_true", help="Run full pipeline continuously with 5-minute gap between cycles")
    parser.add_argument("--gap", type=int, default=300, help="Gap in seconds between cycles in continuous mode (default: 300 = 5 min)")
    parser.add_argument("--daemon", action="store_true", help="Run continuous dual-cadence background daemon")
    parser.add_argument("--api-only", action="store_true", help="Run only parallel API harvesters")
    parser.add_argument("--cdp-only", action="store_true", help="Run only Edge CDP queue worker")
    parser.add_argument("--commit-only", action="store_true", help="Run only Excel batch committer")
    parser.add_argument("--workers", type=int, default=1, help="Worker threads for API harvest (default: 1 for atomic safety)")
    parser.add_argument("--api-interval", type=int, default=60, help="API loop interval in seconds (default: 60)")
    parser.add_argument("--cdp-interval", type=int, default=300, help="CDP loop interval in seconds (default: 300)")

    args = parser.parse_args()

    if args.continuous:
        run_continuous_cycles(gap_seconds=args.gap, workers=args.workers)
    elif args.api_only:
        execute_parallel_api_harvest(max_workers=args.workers)
    elif args.cdp_only:
        run_cdp_queue_cycle()
    elif args.commit_only:
        commit_staged_sheets()
    elif args.daemon:
        run_continuous_daemon(
            api_interval=args.api_interval,
            cdp_interval=args.cdp_interval,
            workers=args.workers,
        )
    else:
        # Default behavior: run-once full cycle
        run_full_parallel_cycle(workers=args.workers)
