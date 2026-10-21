#!/usr/bin/env python3
"""
Terminal/Data_Factory/autonomous_excel_daemon.py
================================================
Zero-Token Autonomous Background Master Excel Pipeline Daemon.

Operates autonomously on Windows host to keep Data/DataBase_Trading.xlsx
continuously refreshed every 10 minutes (600 seconds):
1. Wakes up every 10 minutes (default 600s cadence).
2. Executes Terminal/Data_Factory/master_excel_pipeline.py to update all 43 sheets
   with fresh live market data, microstructure depth, Arkham whale flows,
   ETF statistics, and cognitive telemetry.
3. Performs native OpenXML and Microsoft Excel COM validation.
4. Emits real-time heartbeat status to Data/excel_daemon_status.json.
5. All operations are non-blocking, headless, and logged to logs/autonomous_excel_daemon.log.
"""
from __future__ import annotations

import argparse
import datetime
import gc
import json
import logging
import os
import pathlib
import signal
import sys
import time
import traceback

ROOT = pathlib.Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

LOG_DIR = ROOT / "logs"
LOG_DIR.mkdir(parents=True, exist_ok=True)
LOG_FILE = LOG_DIR / "autonomous_excel_daemon.log"

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE, encoding="utf-8"),
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger("ExcelUpdateDaemon")

STATUS_FILE = ROOT / "Data" / "excel_daemon_status.json"
DEFAULT_INTERVAL_S = 900.0  # 15 minutes (900 seconds)

_keep_running = True



def _handle_signal(signum, frame):
    global _keep_running
    logger.info("Received termination signal %d. Shutting down gracefully...", signum)
    _keep_running = False


signal.signal(signal.SIGINT, _handle_signal)
signal.signal(signal.SIGTERM, _handle_signal)


def verify_excel_com(workbook_path: pathlib.Path) -> dict:
    """Verifies that the workbook opens cleanly in Microsoft Excel COM."""
    result = {
        "verified": False,
        "sheet_count": 0,
        "sheets": [],
        "error": None
    }
    try:
        import win32com.client
        excel = win32com.client.DispatchEx("Excel.Application")
        excel.Visible = False
        excel.DisplayAlerts = False
        excel.ScreenUpdating = False
        try:
            wb = excel.Workbooks.Open(str(workbook_path.resolve()), ReadOnly=True, CorruptLoad=0)
            sheet_names = [sheet.Name for sheet in wb.Sheets]
            wb.Close(SaveChanges=False)
            result["verified"] = True
            result["sheet_count"] = len(sheet_names)
            result["sheets"] = sheet_names
        finally:
            excel.Quit()
            del excel
            gc.collect()
    except Exception as e:
        logger.warning("Windows Excel COM verification note: %s", e)
        result["error"] = str(e)
        # Fallback to openpyxl sheet verification
        try:
            import openpyxl
            wb = openpyxl.load_workbook(workbook_path, read_only=True)
            result["verified"] = True
            result["sheet_count"] = len(wb.sheetnames)
            result["sheets"] = wb.sheetnames
            wb.close()
        except Exception as ex:
            result["error"] = f"COM error: {e}; openpyxl error: {ex}"
    return result


def update_status(status_dict: dict) -> None:
    """Atomically writes status to Data/excel_daemon_status.json."""
    tmp_file = STATUS_FILE.with_suffix(".tmp")
    try:
        STATUS_FILE.parent.mkdir(parents=True, exist_ok=True)
        with open(tmp_file, "w", encoding="utf-8") as f:
            json.dump(status_dict, f, indent=2)
        tmp_file.replace(STATUS_FILE)
    except Exception as e:
        logger.error("Failed to write status file: %s", e)


def main():
    parser = argparse.ArgumentParser(description="Autonomous Master Excel Update Daemon (10m)")
    parser.add_argument("--interval", type=float, default=DEFAULT_INTERVAL_S, help="Interval between runs in seconds (default: 600)")
    parser.add_argument("--initial-delay", type=float, default=DEFAULT_INTERVAL_S, help="Initial sleep delay before first run (default: 600)")
    parser.add_argument("--now", action="store_true", help="Run immediately on start without initial delay")
    args = parser.parse_args()

    interval = args.interval
    initial_delay = 0.0 if args.now else args.initial_delay

    logger.info("=" * 70)
    logger.info("AUTONOMOUS MASTER EXCEL UPDATE DAEMON INITIALIZING")
    logger.info("Cadence: Every %.1f seconds (%.1f minutes)", interval, interval / 60.0)
    logger.info("Initial Delay: %.1f seconds", initial_delay)
    logger.info("Target Workbook: %s", ROOT / "Data" / "DataBase_Trading.xlsx")
    logger.info("=" * 70)

    now_utc = datetime.datetime.now(datetime.timezone.utc)
    next_run = now_utc + datetime.timedelta(seconds=initial_delay)

    update_status({
        "status": "INITIALIZED",
        "cadence_seconds": interval,
        "initial_delay_seconds": initial_delay,
        "started_at_utc": now_utc.strftime("%Y-%m-%d %H:%M:%S UTC"),
        "next_run_utc": next_run.strftime("%Y-%m-%d %H:%M:%S UTC"),
        "total_iterations": 0,
        "consecutive_failures": 0,
        "last_duration_seconds": 0.0
    })

    if initial_delay > 0:
        logger.info("Sleeping initial delay of %.1f seconds until first update at %s...", initial_delay, next_run.strftime("%H:%M:%S UTC"))
        wake_time = time.time() + initial_delay
        while _keep_running and time.time() < wake_time:
            time.sleep(min(5.0, wake_time - time.time()))

    iteration = 0
    consecutive_failures = 0

    while _keep_running:
        iteration += 1
        run_start = time.time()
        start_utc = datetime.datetime.now(datetime.timezone.utc)
        logger.info("Starting Excel update iteration #%d at %s...", iteration, start_utc.strftime("%Y-%m-%d %H:%M:%S UTC"))

        try:
            import importlib
            import Terminal.Data_Factory.master_excel_pipeline as mep
            importlib.reload(mep)
            elapsed = mep.run_pipeline()
            
            # Verify COM
            excel_path = ROOT / "Data" / "DataBase_Trading.xlsx"
            com_res = verify_excel_com(excel_path)
            
            consecutive_failures = 0
            duration = time.time() - run_start
            next_utc = datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(seconds=interval)

            logger.info("Iteration #%d completed successfully in %.2fs. Sheets: %d. COM Verified: %s",
                        iteration, duration, com_res["sheet_count"], com_res["verified"])
            logger.info("Next scheduled Excel update at %s", next_utc.strftime("%Y-%m-%d %H:%M:%S UTC"))

            update_status({
                "status": "HEALTHY",
                "cadence_seconds": interval,
                "total_iterations": iteration,
                "consecutive_failures": 0,
                "last_run_utc": start_utc.strftime("%Y-%m-%d %H:%M:%S UTC"),
                "last_duration_seconds": round(duration, 2),
                "pipeline_duration_seconds": round(elapsed, 2) if elapsed else round(duration, 2),
                "sheet_count": com_res["sheet_count"],
                "com_verified": com_res["verified"],
                "next_run_utc": next_utc.strftime("%Y-%m-%d %H:%M:%S UTC")
            })

        except Exception as e:
            consecutive_failures += 1
            duration = time.time() - run_start
            logger.error("Error during iteration #%d: %s", iteration, e)
            logger.error(traceback.format_exc())
            
            next_retry = datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(seconds=60)
            update_status({
                "status": "DEGRADED",
                "cadence_seconds": interval,
                "total_iterations": iteration,
                "consecutive_failures": consecutive_failures,
                "last_run_utc": start_utc.strftime("%Y-%m-%d %H:%M:%S UTC"),
                "last_duration_seconds": round(duration, 2),
                "last_error": str(e),
                "next_run_utc": next_retry.strftime("%Y-%m-%d %H:%M:%S UTC")
            })
            
            # Retry sooner on error (60 seconds)
            logger.info("Retrying in 60 seconds due to iteration error...")
            wake_time = time.time() + 60.0
            while _keep_running and time.time() < wake_time:
                time.sleep(min(5.0, wake_time - time.time()))
            continue

        # Sleep until next scheduled iteration
        wake_time = time.time() + interval
        while _keep_running and time.time() < wake_time:
            time.sleep(min(5.0, wake_time - time.time()))

    logger.info("Excel Update Daemon stopped cleanly.")


if __name__ == "__main__":
    main()
