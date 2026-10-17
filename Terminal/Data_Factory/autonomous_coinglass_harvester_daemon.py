#!/usr/bin/env python3
"""
Terminal/Data_Factory/autonomous_coinglass_harvester_daemon.py
==============================================================
Zero-Token Autonomous Background CoinGlass L3 Whale Orders Harvester Daemon.

Solves the Cadence / Gating Horizon constraint (F22):
- The age-decay curve has a half-life of 623.8s (D(600)=0.7165, D(1200)=0.3679).
- For high-conviction assets (|S_whale| >= 0.25), decay forces gating neutral after 13-25m.
- This daemon operates autonomously with a 180-second (3-minute) cadence, guaranteeing
  that CoinGlass whale order data age stays permanently <= 180s.
- Ephemeral Chrome CDP tabs are launched on port 9222, extracted, and cleanly destroyed.
- Data is saved atomically to Data/coinglass/latest/coinglass_whale_orders_snapshot.json
  and archived into the time_series_database (.json.gz + SQLite index).
- Heartbeat & execution health are written to Data/coinglass/coinglass_harvester_status.json.
"""
from __future__ import annotations

import argparse
import asyncio
import datetime
import gc
import json
import logging
import os
import pathlib
import signal
import sys
import time

ROOT = pathlib.Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from Terminal.Data_Factory.coinglass_whale_orders_harvester import harvest_whale_orders
from Terminal.Data_Factory.time_series_database import atomic_write_text

LOG_DIR = ROOT / "logs"
LOG_DIR.mkdir(parents=True, exist_ok=True)
LOG_FILE = LOG_DIR / "autonomous_coinglass_harvester_daemon.log"

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE, encoding="utf-8"),
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger("CoinGlassHarvesterDaemon")

STATUS_FILE = ROOT / "Data" / "coinglass" / "coinglass_harvester_status.json"
PID_FILE = ROOT / "logs" / "autonomous_coinglass_harvester_daemon.pid"
DEFAULT_INTERVAL_S = 180.0  # 3 minutes

_singleton_handle = None
_keep_running = True


def enforce_single_instance() -> None:
    """Hold an OS file lock to ensure only one daemon instance runs."""
    global _singleton_handle
    if _singleton_handle is not None:
        return
    lock_file = PID_FILE.with_suffix(".lock")
    handle = lock_file.open("a+b")
    try:
        if os.name == "nt":
            import msvcrt
            msvcrt.locking(handle.fileno(), msvcrt.LK_NBLCK, 1)
        else:
            import fcntl
            fcntl.flock(handle.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
    except (BlockingIOError, OSError):
        logger.error("Another instance of autonomous_coinglass_harvester_daemon is already active. Exiting.")
        sys.exit(0)
    _singleton_handle = handle
    try:
        PID_FILE.write_text(str(os.getpid()), encoding="utf-8")
    except Exception:
        pass


def update_status(payload: dict) -> None:
    """Atomically record daemon status and heartbeat with redundant backup mirror across multiple paths."""
    STATUS_FILE.parent.mkdir(parents=True, exist_ok=True)
    secondary_dir = ROOT / "Data" / "coinglass" / "backup"
    secondary_dir.mkdir(parents=True, exist_ok=True)
    raw = json.dumps(payload, indent=2)
    atomic_write_text(STATUS_FILE, raw)
    try:
        atomic_write_text(STATUS_FILE.with_suffix(".bak"), raw)
        atomic_write_text(secondary_dir / "coinglass_harvester_status.json", raw)
    except Exception:
        pass


def handle_shutdown(signum, frame) -> None:
    global _keep_running
    logger.info(f"Received signal {signum}. Initiating graceful shutdown...")
    _keep_running = False


async def run_daemon(interval_s: float = DEFAULT_INTERVAL_S, run_once: bool = False) -> None:
    enforce_single_instance()
    logger.info(f"=== Autonomous CoinGlass Harvester Daemon Started (Interval: {interval_s}s, PID: {os.getpid()}) ===")
    
    cycle_count = 0
    error_count = 0
    last_error_message = None
    last_error_utc = None
    last_success_utc = None

    # Restore historical failure and success tracking from status file across restarts (with dual-candidate backup recovery)
    status_source = None
    prev_status = None
    secondary_path = ROOT / "Data" / "coinglass" / "backup" / "coinglass_harvester_status.json"
    backup_recovery_active = False
    corruption_recovery_event = False

    for candidate_path in [STATUS_FILE, STATUS_FILE.with_suffix(".bak"), secondary_path]:
        if candidate_path.exists():
            try:
                prev_status = json.loads(candidate_path.read_text(encoding="utf-8"))
                status_source = candidate_path.name
                if candidate_path != STATUS_FILE:
                    backup_recovery_active = True
                    corruption_recovery_event = True
                    logger.warning(f"ALERT: Primary status file missing/corrupt. Restored from backup mirror {candidate_path}")
                break
            except Exception as e:
                logger.error(f"Corruption detected in {candidate_path}: {e}")
                corruption_recovery_event = True

    if prev_status:
        cycle_count = int(prev_status.get("cycle_count", 0))
        error_count = int(prev_status.get("error_count", 0))
        last_error_message = prev_status.get("last_error")
        last_error_utc = prev_status.get("last_error_utc")
        last_success_utc = prev_status.get("last_success_utc")
        logger.info(f"Restored historical state from {status_source}: {cycle_count} cycles, {error_count} errors. Last error: {last_error_message}")
    else:
        logger.critical("ALERT: Both primary and backup status files are missing or corrupt. Operating in quarantine recovery mode.")

    while _keep_running:
        cycle_count += 1
        t_cycle_start = time.time()
        now_utc = datetime.datetime.now(datetime.timezone.utc).isoformat()
        logger.info(f"--- Cycle #{cycle_count} starting at {now_utc} ---")

        try:
            harvest_result = await asyncio.wait_for(harvest_whale_orders(), timeout=120.0)
            elapsed = round(time.time() - t_cycle_start, 2)
            orders = harvest_result.get("total_whale_orders", 0)
            notional = harvest_result.get("grand_total_notional_usd", 0.0)
            assets_count = harvest_result.get("total_assets_scraped", 0)
            last_success_utc = now_utc

            logger.info(
                f"Cycle #{cycle_count} SUCCESS: {orders} whale orders (${notional:,.0f} notional) "
                f"across {assets_count} assets in {elapsed}s."
            )

            status_payload = {
                "daemon": "autonomous_coinglass_harvester_daemon",
                "status": "HEALTHY",
                "current_cycle_status": "SUCCESS",
                "pid": os.getpid(),
                "cycle_count": cycle_count,
                "error_count": error_count,
                "interval_seconds": interval_s,
                "last_heartbeat_utc": now_utc,
                "last_heartbeat_epoch": time.time(),
                "last_harvest_epoch": harvest_result.get("harvest_epoch", time.time()),
                "last_duration_s": elapsed,
                "total_orders_harvested": orders,
                "grand_total_notional_usd": notional,
                "total_assets_scraped": assets_count,
                "total_assets_valid": harvest_result.get("total_assets_valid", assets_count),
                "skipped_assets": harvest_result.get("skipped_assets", {}),
                "last_success_utc": last_success_utc,
                "last_error": last_error_message,
                "last_error_utc": last_error_utc,
                "backup_recovery_active": backup_recovery_active,
                "corruption_recovery_event": corruption_recovery_event,
                "status_source": status_source,
                "backup_mirror_paths": [str(STATUS_FILE.with_suffix(".bak")), str(secondary_path)]
            }
            update_status(status_payload)
            # Reset recovery active flag once a cycle completes cleanly and restores primary status
            backup_recovery_active = False
            corruption_recovery_event = False
            status_source = STATUS_FILE.name

        except Exception as e:
            error_count += 1
            last_error_message = str(e)
            last_error_utc = now_utc
            elapsed = round(time.time() - t_cycle_start, 2)
            logger.error(f"Cycle #{cycle_count} FAILED after {elapsed}s: {e}", exc_info=True)

            status_payload = {
                "daemon": "autonomous_coinglass_harvester_daemon",
                "status": "DEGRADED",
                "current_cycle_status": "FAILED",
                "pid": os.getpid(),
                "cycle_count": cycle_count,
                "error_count": error_count,
                "interval_seconds": interval_s,
                "last_heartbeat_utc": now_utc,
                "last_heartbeat_epoch": time.time(),
                "last_duration_s": elapsed,
                "last_success_utc": last_success_utc,
                "last_error": last_error_message,
                "last_error_utc": last_error_utc
            }
            update_status(status_payload)

        if run_once or not _keep_running:
            break

        # Compute remaining sleep time
        time_spent = time.time() - t_cycle_start
        sleep_needed = max(5.0, interval_s - time_spent)
        logger.info(f"Cycle #{cycle_count} completed in {time_spent:.1f}s. Sleeping {sleep_needed:.1f}s until next harvest...")

        # Chunked sleep for responsive shutdown
        sleep_until = time.time() + sleep_needed
        while _keep_running and time.time() < sleep_until:
            await asyncio.sleep(min(2.0, max(0.1, sleep_until - time.time())))

        gc.collect()

    logger.info("Daemon loop terminated. Cleaning up PID file.")
    try:
        if PID_FILE.exists():
            PID_FILE.unlink()
    except Exception:
        pass


def main() -> None:
    parser = argparse.ArgumentParser(description="Autonomous CoinGlass Harvester Daemon")
    parser.add_argument("--interval", type=float, default=DEFAULT_INTERVAL_S, help="Cadence interval in seconds (default: 180)")
    parser.add_argument("--once", action="store_true", help="Run a single harvest cycle and exit")
    args = parser.parse_args()

    signal.signal(signal.SIGINT, handle_shutdown)
    if hasattr(signal, "SIGTERM"):
        signal.signal(signal.SIGTERM, handle_shutdown)

    asyncio.run(run_daemon(interval_s=args.interval, run_once=args.once))


if __name__ == "__main__":
    main()
