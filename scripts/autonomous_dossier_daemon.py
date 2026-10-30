#!/usr/bin/env python3
"""
scripts/autonomous_dossier_daemon.py
====================================
Autonomous Background Dossier Updation Daemon.
Regenerates all 162 Sovereign Master Dossiers and 162 360-Dossiers every 180 seconds (3 minutes)
using 100% structured data from all 43 Parquet feeds.

Features:
- Fixed 180-second cadence.
- Logs cycle telemetry to logs/autonomous_dossier_daemon.log and Data/dossier_daemon_status.json.
- Zero memory leakage: forces aggressive garbage collection after each cycle.
- Exception-resilient: captures and logs errors without terminating the loop.
"""

from __future__ import annotations
import datetime
import gc
import json
import logging
import os
import pathlib
import sys
import time
import traceback

ROOT = pathlib.Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

LOG_DIR = ROOT / "logs"
LOG_DIR.mkdir(parents=True, exist_ok=True)
LOG_FILE = LOG_DIR / "autonomous_dossier_daemon.log"
STATUS_FILE = ROOT / "Data" / "dossier_daemon_status.json"

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] [DossierDaemon] %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE, encoding="utf-8"),
        logging.StreamHandler(sys.stdout),
    ],
)
logger = logging.getLogger("DossierDaemon")

INTERVAL_SECONDS = 180  # 3 minutes


def run_daemon():
    logger.info("=" * 80)
    logger.info("🏛️ INITIATING AUTONOMOUS DOSSIER UPDATION DAEMON (3-MINUTE CADENCE)")
    logger.info(f"Target: All 162 Master Dossiers & 162 360-Dossiers in docs/dossiers/")
    logger.info(f"Interval: {INTERVAL_SECONDS} seconds (3.0 minutes)")
    logger.info("=" * 80)

    from scripts.sovereign_dossier_engine import run_pipeline

    cycle_count = 0

    while True:
        cycle_count += 1
        t0 = time.perf_counter()
        now_utc = datetime.datetime.now(datetime.timezone.utc)
        now_ist = now_utc + datetime.timedelta(hours=5, minutes=30)
        logger.info(f">>> [CYCLE #{cycle_count}] Starting dossier refresh at {now_ist.strftime('%Y-%m-%d %H:%M:%S IST')}...")

        success = False
        error_msg = None
        elapsed = 0.0

        try:
            run_pipeline()
            elapsed = time.perf_counter() - t0
            success = True
            logger.info(f"✅ [CYCLE #{cycle_count}] Completed dossier refresh in {elapsed:.3f}s")
        except Exception as e:
            elapsed = time.perf_counter() - t0
            error_msg = str(e)
            logger.error(f"❌ [CYCLE #{cycle_count}] Error during dossier refresh: {e}")
            logger.error(traceback.format_exc())

        # Update status JSON
        try:
            status_data = {
                "cycle_count": cycle_count,
                "timestamp_utc": now_utc.strftime("%Y-%m-%d %H:%M:%S UTC"),
                "timestamp_ist": now_ist.strftime("%Y-%m-%d %H:%M:%S IST"),
                "elapsed_seconds": round(elapsed, 3),
                "success": success,
                "error": error_msg,
                "next_run_seconds": INTERVAL_SECONDS,
            }
            STATUS_FILE.parent.mkdir(parents=True, exist_ok=True)
            STATUS_FILE.write_text(json.dumps(status_data, indent=2), encoding="utf-8")
        except Exception as json_err:
            logger.warning(f"Failed to write daemon status JSON: {json_err}")

        # Aggressive memory cleanup
        gc.collect()

        logger.info(f"Sleeping for {INTERVAL_SECONDS}s before next cycle...\n")
        time.sleep(INTERVAL_SECONDS)


if __name__ == "__main__":
    try:
        run_daemon()
    except KeyboardInterrupt:
        logger.info("Dossier Updation Daemon stopped by operator.")
        sys.exit(0)
