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

# Core always-on browser jobs (run every cycle)
CORE_BROWSER_JOBS = [
    {
        "id": 27,
        "name": "Forex Factory Institutional News",
        "script": MODULES_DIR / "19_News.py",
        "sheet": "19_News",
        "timeout": 180,
    },
    {
        "id": 28,
        "name": "Forex Factory Macroeconomic Calendar",
        "script": MODULES_DIR / "19_Calendar.py",
        "sheet": "19_Calendar",
        "timeout": 180,
    },
    {
        "id": 18,
        "name": "CoinGlass Whale Orders & Large Trades",
        "script": MODULES_DIR / "10_Whale_Orders.py",
        "sheet": "10_Whale_Orders",
        "timeout": 180,
    },
]

# Rotating CoinGlass scraping jobs (3 per cycle, fully rotating every 4 cycles / ~10-12 min)
ROTATING_COINGLASS_JOBS = [
    {"id": 2, "name": "Spot Netflow", "script": MODULES_DIR / "2_Spot_Netflow_S.py", "sheet": "2_Spot_Netflow_S", "timeout": 180},
    {"id": 3, "name": "Exchanges Long/Short Ratio 15M", "script": MODULES_DIR / "3_Exchanges_LS_Ratio_15M.py", "sheet": "3_Exchanges_LS_Ratio_15M", "timeout": 180},
    {"id": 10, "name": "Liquidation Heatmap", "script": MODULES_DIR / "7_Liq_Heapmap.py", "sheet": "7_Liq_Heapmap", "timeout": 180},
    {"id": 4, "name": "Exchanges Long/Short Ratio 1H", "script": MODULES_DIR / "3_Exchanges_LS_Ratio_1H.py", "sheet": "3_Exchanges_LS_Ratio_1H", "timeout": 180},
    {"id": 5, "name": "Exchanges Long/Short Ratio 4H", "script": MODULES_DIR / "3_Exchanges_LS_Ratio_4H.py", "sheet": "3_Exchanges_LS_Ratio_4H", "timeout": 180},
    {"id": 11, "name": "Live Liquidations", "script": MODULES_DIR / "7_Live_Liq.py", "sheet": "7_Live_Liq", "timeout": 180},
    {"id": 12, "name": "Exchange Liquidation Map 1D", "script": MODULES_DIR / "8_Exchange_Liquidation_Map_1D.py", "sheet": "8_Exchange_Liquidation_Map_1D", "timeout": 180},
    {"id": 13, "name": "Exchange Liquidation Map 7D", "script": MODULES_DIR / "8_Exchange_Liquidation_Map_7D.py", "sheet": "8_Exchange_Liquidation_Map_7D", "timeout": 180},
    {"id": 14, "name": "Liquidation Max Pain 24H", "script": MODULES_DIR / "9_Liquidation_Max_Pain_24H.py", "sheet": "9_Liquidation_Max_Pain_24H", "timeout": 180},
    {"id": 15, "name": "Liquidation Max Pain 48H", "script": MODULES_DIR / "9_Liquidation_Max_Pain_48H.py", "sheet": "9_Liquidation_Max_Pain_48H", "timeout": 180},
    {"id": 16, "name": "Liquidation Max Pain 3D", "script": MODULES_DIR / "9_Liquidation_Max_Pain_3D.py", "sheet": "9_Liquidation_Max_Pain_3D", "timeout": 180},
    {"id": 17, "name": "Liquidation Max Pain 7D", "script": MODULES_DIR / "9_Liquidation_Max_Pain_7D.py", "sheet": "9_Liquidation_Max_Pain_7D", "timeout": 180},
]

STATE_FILE = ROOT_DIR / "Data" / "cdp_rotation_state.json"

def get_next_job_batch(batch_size: int = 3) -> list[dict]:
    """Retrieves next batch of rotating CoinGlass jobs with persistent state."""
    current_idx = 0
    if STATE_FILE.exists():
        try:
            with open(STATE_FILE, "r", encoding="utf-8") as f:
                data = json.load(f)
                current_idx = data.get("current_index", 0)
        except Exception:
            current_idx = 0
            
    total_rot = len(ROTATING_COINGLASS_JOBS)
    selected = []
    for i in range(batch_size):
        idx = (current_idx + i) % total_rot
        selected.append(ROTATING_COINGLASS_JOBS[idx])
        
    next_idx = (current_idx + batch_size) % total_rot
    try:
        STATE_FILE.parent.mkdir(parents=True, exist_ok=True)
        with open(STATE_FILE, "w", encoding="utf-8") as f:
            json.dump({"current_index": next_idx, "updated_at": datetime.datetime.now(datetime.timezone.utc).isoformat()}, f, indent=2)
    except Exception as e:
        log.warning(f"Could not persist rotation state: {e}")
        
    return selected

EDGE_BROWSER_JOBS = CORE_BROWSER_JOBS


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

    active_jobs = CORE_BROWSER_JOBS + get_next_job_batch(3)
    log.info(f"[EdgeQueue] Active cycle queue ({len(active_jobs)} jobs): {[j['sheet'] for j in active_jobs]}")
    for job in active_jobs:
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
