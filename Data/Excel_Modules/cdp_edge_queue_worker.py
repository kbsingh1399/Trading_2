"""
CDP Edge Queue Worker (Tier 1B Producer)
Executes browser-based scraping jobs sequentially on the active Microsoft Edge debug session (port 9222).
Guarantees single-tab queue execution to prevent browser CPU spikes and strictly preserves the Arena.ai tab.
"""

from __future__ import annotations

import argparse
import datetime
import json
import pathlib
import subprocess
import sys
import time
import urllib.request

from logger_config import emit_telemetry_event, get_system_ram_telemetry, setup_institutional_logger

MODULES_DIR = pathlib.Path(__file__).resolve().parent
ROOT_DIR = MODULES_DIR.parents[1]
CDP_BASE_URL = "http://127.0.0.1:9222"

log = setup_institutional_logger("EdgeQueueWorker")

# Browser tasks that must execute through debug Edge
EDGE_BROWSER_JOBS = [
    {
        "id": 27,
        "name": "Forex Factory Institutional News",
        "script": MODULES_DIR / "19_News.py",
        "sheet": "19_News",
        "timeout": 90,
    },
    {
        "id": 28,
        "name": "Forex Factory Macroeconomic Calendar",
        "script": MODULES_DIR / "19_Calendar.py",
        "sheet": "19_Calendar",
        "timeout": 90,
    },
    {
        "id": 18,
        "name": "CoinGlass Whale Orders & Large Trades",
        "script": MODULES_DIR / "10_Whale_Orders.py",
        "sheet": "10_Whale_Orders",
        "timeout": 90,
    },
]


def verify_edge_cdp_and_arena() -> tuple[bool, str]:
    """Verifies that debug Edge is active on port 9222 and detects the Arena.ai tab."""
    try:
        req = urllib.request.urlopen(f"{CDP_BASE_URL}/json", timeout=5)
        tabs = json.loads(req.read().decode())
        arena_tabs = [t for t in tabs if "arena.ai" in t.get("url", "").lower()]

        if not arena_tabs:
            return False, "No active Arena.ai tab detected on Edge port 9222."

        arena_id = arena_tabs[0].get("id")
        return True, f"Edge CDP connected. Arena.ai tab guarded (ID: {arena_id})."
    except Exception as e:
        return False, f"Could not connect to Edge CDP at {CDP_BASE_URL}: {e}"


def run_edge_job(job: dict) -> tuple[bool, float, str]:
    """Runs a single browser scraping job through debug Edge."""
    script_path = job["script"]
    if not script_path.exists():
        return False, 0.0, f"Script not found: {script_path}"

    cmd = [sys.executable, str(script_path)]
    log.info(f"[EdgeQueue] Starting job {job['id']}: {job['name']}...")
    t0 = time.perf_counter()

    try:
        proc = subprocess.run(
            cmd,
            cwd=str(MODULES_DIR),
            stdout=sys.stdout,
            stderr=sys.stderr,
            text=True,
            timeout=job.get("timeout", 90),
            check=False,
        )
        elapsed = time.perf_counter() - t0
        success = (proc.returncode == 0)
        status_str = "PASS" if success else "FAIL"
        err = "OK" if success else f"Return code {proc.returncode}"

        log.info(f"[EdgeQueue] Job {job['id']} completed: [{status_str}] in {elapsed:.2f}s")
        emit_telemetry_event(
            event_type="EDGE_CDP_JOB",
            module_id=job["id"],
            sheet=job["sheet"],
            status=status_str,
            duration=elapsed,
            metadata={"job_name": job["name"]},
        )
        return success, elapsed, err

    except subprocess.TimeoutExpired:
        elapsed = time.perf_counter() - t0
        log.error(f"[EdgeQueue] Job {job['id']} TIMEOUT after {elapsed:.2f}s")
        return False, elapsed, "TimeoutExpired"
    except Exception as e:
        elapsed = time.perf_counter() - t0
        log.error(f"[EdgeQueue] Job {job['id']} EXCEPTION: {e}")
        return False, elapsed, str(e)


def run_cdp_queue_cycle() -> dict:
    """Executes a full cycle of Edge browser jobs in sequential order."""
    ok, msg = verify_edge_cdp_and_arena()
    if not ok:
        log.warning(f"[EdgeQueue] Pre-flight check warning: {msg}")
    else:
        log.info(f"[EdgeQueue] {msg}")

    t_start = time.perf_counter()
    results = []

    for job in EDGE_BROWSER_JOBS:
        success, duration, err = run_edge_job(job)
        results.append({
            "id": job["id"],
            "name": job["name"],
            "sheet": job["sheet"],
            "success": success,
            "duration": duration,
            "error": err,
        })
        time.sleep(1.0)  # Brief pause between browser tabs

    total_time = time.perf_counter() - t_start
    passed = sum(1 for r in results if r["success"])
    log.info(f"[EdgeQueue] Cycle finished: {passed}/{len(results)} jobs passed in {total_time:.2f}s.")

    return {
        "passed": passed,
        "total": len(results),
        "duration": total_time,
        "results": results,
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Edge CDP Queue Worker")
    parser.add_argument("--loop", action="store_true", help="Run continuously with 5-minute interval")
    parser.add_argument("--interval", type=int, default=300, help="Interval in seconds for loop mode")
    args = parser.parse_args()

    if args.loop:
        log.info(f"[EdgeQueue] Starting continuous loop with {args.interval}s interval...")
        while True:
            try:
                run_cdp_queue_cycle()
            except Exception as e:
                log.error(f"[EdgeQueue] Error in cycle: {e}")
            time.sleep(args.interval)
    else:
        run_cdp_queue_cycle()
