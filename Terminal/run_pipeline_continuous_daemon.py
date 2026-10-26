#!/usr/bin/env python3
"""
Terminal/run_pipeline_continuous_daemon.py
==========================================
Persistent Background 100% Pure-Parquet Pipeline Daemon.
Executes the unified multi-asset Parquet data pipeline, then sleeps for exactly
120 seconds (2 minutes) before starting the next cycle, guaranteeing:
  1. Continuous, fresh institutional data across all 33 production Parquet feeds.
  2. Zero Excel or openpyxl file-lock contention (atomic Parquet writes).
  3. Automatic MT5 broker telemetry & tick quotes updates.
  4. Real-time health audit via parquet_checklist_auditor.py.
  5. Strict 2-minute gap between cycles.

Usage:
  python Terminal/run_pipeline_continuous_daemon.py                 # Default: full pipeline, 2m gap
  python Terminal/run_pipeline_continuous_daemon.py --api-only      # Fast pure-API mode (< 15s), 2m gap
  python Terminal/run_pipeline_continuous_daemon.py --gap 120       # Custom gap in seconds
"""

from __future__ import annotations

import argparse
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
    format="%(asctime)s [%(levelname)s] [ParquetPipelineDaemon] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    handlers=[
        logging.StreamHandler(sys.stdout),
        logging.FileHandler(LOG_DIR / "parquet_pipeline_daemon.log", encoding="utf-8"),
    ],
)
log = logging.getLogger("ParquetPipelineDaemon")


def run_single_cycle(cycle_count: int, api_only: bool = False, gap_seconds: int = 120) -> bool:
    """Executes a single end-to-end Parquet data pipeline cycle."""
    log.info("=" * 80)
    log.info(f"   STARTING PARQUET DATA UPDATION CYCLE #{cycle_count}")
    log.info(f"   Timestamp: {datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')}")
    log.info(f"   Mode: {'Pure-API Only' if api_only else 'Full Multi-Engine (API + Browser)'}")
    log.info("=" * 80)
    t0 = time.perf_counter()

    master_script = ROOT_DIR / "Terminal" / "run_master_pipeline.py"
    if not master_script.exists():
        log.error(f"Master pipeline script not found: {master_script}")
        return False

    cmd = [sys.executable, str(master_script)]
    if api_only:
        cmd.append("--api-only")

    try:
        proc = subprocess.run(
            cmd,
            cwd=str(ROOT_DIR),
            check=False,
            timeout=1800,
        )
        elapsed = time.perf_counter() - t0
        success = (proc.returncode == 0)
        status_str = "SUCCESS" if success else f"FAILED (code {proc.returncode})"

        log.info("=" * 80)
        log.info(f"   CYCLE #{cycle_count} COMPLETE: [{status_str}] in {elapsed:.2f}s ({elapsed/60:.2f} min)")
        log.info(f"   Next cycle will start in {gap_seconds} seconds ({gap_seconds/60:.1f} minutes)...")
        log.info("=" * 80)
        return success

    except subprocess.TimeoutExpired:
        log.error(f"[Cycle #{cycle_count}] Pipeline timed out after 1800s.")
        return False
    except Exception as e:
        log.error(f"[Cycle #{cycle_count}] Unexpected pipeline execution error: {e}")
        return False


def main():
    parser = argparse.ArgumentParser(description="Persistent Background 100% Pure-Parquet Pipeline Daemon")
    parser.add_argument("--api-only", action="store_true", help="Execute only the 18 Pure-API collectors (< 15s)")
    parser.add_argument("--gap", type=int, default=120, help="Gap in seconds between cycles (default: 120s / 2m)")
    args = parser.parse_args()

    log.info("100% Pure-Parquet Data Updation Daemon initialized.")
    log.info(f"Configured gap between cycles: {args.gap} seconds ({args.gap/60:.1f} minutes).")

    cycle_count = 1
    while True:
        try:
            run_single_cycle(cycle_count, api_only=args.api_only, gap_seconds=args.gap)
            cycle_count += 1

            # Rotate public egress IP after each cycle to prevent CoinGlass 429 rate limiting
            log.info("Triggering automated IP rotation via Cloudflare WARP before next cycle...")
            try:
                if str(ROOT_DIR / "Terminal") not in sys.path:
                    sys.path.insert(0, str(ROOT_DIR / "Terminal"))
                from rotate_ip import rotate_ip
                rotate_ip()
            except Exception as rot_exc:
                log.warning(f"Automated IP rotation notice: {rot_exc}")

            log.info(f"Sleeping for {args.gap}s ({args.gap/60:.1f} minutes) before next cycle...")
            time.sleep(args.gap)
        except KeyboardInterrupt:
            log.info("Daemon received shutdown interrupt. Exiting cleanly.")
            break
        except Exception as e:
            log.error(f"Unexpected daemon error: {e}. Retrying in 30s...")
            time.sleep(30)


if __name__ == "__main__":
    main()
