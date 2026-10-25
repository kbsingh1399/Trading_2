#!/usr/bin/env python3
"""
Terminal/run_pipeline_continuous_daemon.py
==========================================
Persistent Background Data Updation Daemon.
Executes the full Excel Data Pipeline, then waits exactly 5 minutes (300 seconds)
after completion before starting the next cycle, guaranteeing:
- Continuous, fresh institutional data across all 29 sheets of DataBase_Trading.xlsx
- Zero overlap / zero race conditions (strict sequential gap of 5 minutes between cycles)
- Automatic execution of MT5 live telemetry at the start of each cycle
- Tab hygiene preserving Arena.ai on Edge CDP port 9222
"""

from __future__ import annotations

import datetime
import logging
import os
import pathlib
import subprocess
import sys
import time

ROOT_DIR = pathlib.Path(__file__).resolve().parents[1]
LOG_DIR = ROOT_DIR / "logs"
LOG_DIR.mkdir(parents=True, exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] [DataPipelineDaemon] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    handlers=[
        logging.StreamHandler(sys.stdout),
        logging.FileHandler(LOG_DIR / "pipeline_daemon.log", encoding="utf-8"),
    ],
)
log = logging.getLogger("PipelineDaemon")

GAP_BETWEEN_CYCLES_SECONDS = 300  # 5 minutes exact gap between cycle finish and next start


def run_single_full_update(cycle_count: int) -> bool:
    """Executes MT5 telemetry followed by the master 28-module pipeline."""
    log.info("=" * 80)
    log.info(f"   STARTING DATA UPDATION CYCLE #{cycle_count}")
    log.info(f"   Timestamp: {datetime.datetime.now(datetime.timezone.utc).isoformat()}")
    log.info("=" * 80)
    t0 = time.perf_counter()

    # 1. Harvest MT5 Live Account & Universe Quotes Telemetry
    try:
        telemetry_script = ROOT_DIR / "Terminal" / "generate_mt5_telemetry.py"
        if telemetry_script.exists():
            log.info("[Phase 1] Harvesting live MT5 broker telemetry...")
            subprocess.run([sys.executable, str(telemetry_script)], check=False, cwd=str(ROOT_DIR), timeout=30)
        
        sheet_script = ROOT_DIR / "Collectors" / "API" / "00_MT5_Account_Telemetry.py"
        if sheet_script.exists():
            log.info("[Phase 1b] Updating Sheet '00_MT5_Account_Telemetry'...")
            subprocess.run([sys.executable, str(sheet_script)], check=False, cwd=str(ROOT_DIR), timeout=60)
    except Exception as e:
        log.warning(f"[Phase 1] Telemetry harvest notice: {e}")

    # 2. Execute Master Unified Pipeline (Pure-API + Browser + Scorecard Audit)
    master_script = ROOT_DIR / "Terminal" / "run_master_pipeline.py"
    if not master_script.exists():
        log.error(f"Master pipeline script not found: {master_script}")
        return False

    try:
        log.info("[Phase 2] Executing Master Unified Pipeline...")
        proc = subprocess.run(
            [sys.executable, str(master_script)],
            cwd=str(ROOT_DIR),
            check=False,
            timeout=3600,
        )
        elapsed = time.perf_counter() - t0
        success = (proc.returncode == 0)
        status_str = "SUCCESS" if success else f"FAILED (code {proc.returncode})"

        log.info("=" * 80)
        log.info(f"   CYCLE #{cycle_count} COMPLETE: [{status_str}] in {elapsed:.2f}s ({elapsed/60:.2f} min)")
        log.info(f"   Next cycle will start in {GAP_BETWEEN_CYCLES_SECONDS} seconds (5 minutes)...")
        log.info("=" * 80)
        return success

    except subprocess.TimeoutExpired:
        log.error(f"[Cycle #{cycle_count}] Pipeline timed out after 3600s.")
        return False
    except Exception as e:
        log.error(f"[Cycle #{cycle_count}] Exception executing pipeline: {e}")
        return False


def main():
    log.info("Master Data Updation Daemon initialized.")
    log.info(f"Gap between cycles configured to: {GAP_BETWEEN_CYCLES_SECONDS} seconds (5 minutes).")

    cycle_count = 1
    while True:
        try:
            run_single_full_update(cycle_count)
            cycle_count += 1
            log.info(f"Sleeping for {GAP_BETWEEN_CYCLES_SECONDS}s (5 minutes) before next cycle...")
            time.sleep(GAP_BETWEEN_CYCLES_SECONDS)
        except KeyboardInterrupt:
            log.info("Daemon received shutdown signal. Exiting gracefully.")
            break
        except Exception as e:
            log.error(f"Unexpected daemon error: {e}. Retrying in 60s...")
            time.sleep(60)


if __name__ == "__main__":
    main()
