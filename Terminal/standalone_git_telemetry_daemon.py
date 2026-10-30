#!/usr/bin/env python3
"""
Terminal/standalone_git_telemetry_daemon.py
===========================================
Production Standalone Git Telemetry & Ledger Synchronization Daemon.
Continuously stages, commits, and pushes fresh telemetry snapshots,
JSON dossiers, and intelligence ledgers to GitHub origin/main.

Usage:
  python Terminal/standalone_git_telemetry_daemon.py             # Continuous loop (60s)
  python Terminal/standalone_git_telemetry_daemon.py --once      # Single push and exit
  python Terminal/standalone_git_telemetry_daemon.py --interval 30 # Custom interval
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
import traceback

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

ROOT_DIR = pathlib.Path(__file__).resolve().parents[1]
LOG_DIR = ROOT_DIR / "logs"
LOG_DIR.mkdir(parents=True, exist_ok=True)
LOG_FILE = LOG_DIR / "standalone_git_telemetry.log"

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] [GitTelemetry] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    handlers=[
        logging.StreamHandler(sys.stdout),
        logging.FileHandler(LOG_FILE, encoding="utf-8"),
    ],
)
log = logging.getLogger("GitTelemetry")

TRACKED_PATHS = [
    "Data/Manditory",
    "Data/feeds",
    "Data/metadata",
    "Data/cycle_envelope.json",
    "Data/council_surveillance_status.json",
    "docs/trade_plans",
    "docs/telemetry",
    "docs/dossiers",
    "Terminal",
    "scripts",
]

def run_git(args: list[str], timeout: int = 45) -> tuple[int, str, str]:
    try:
        proc = subprocess.run(
            ["git"] + args,
            cwd=str(ROOT_DIR),
            capture_output=True,
            text=True,
            timeout=timeout,
        )
        return proc.returncode, proc.stdout.strip(), proc.stderr.strip()
    except subprocess.TimeoutExpired:
        return 1, "", f"Git command timed out after {timeout}s"
    except Exception as e:
        return 1, "", str(e)

def sync_telemetry_to_git(cycle_count: int) -> bool:
    now_utc = datetime.datetime.now(datetime.timezone.utc)
    now_ist = now_utc + datetime.timedelta(hours=5, minutes=30)
    time_str = now_ist.strftime("%Y-%m-%d %H:%M:%S IST")

    # 1. Stage tracked paths
    for p in TRACKED_PATHS:
        full_p = ROOT_DIR / p
        if full_p.exists():
            run_git(["add", p])

    # 2. Check if staged changes exist
    code, out, _ = run_git(["diff", "--staged", "--name-only"])
    if not out.strip():
        log.info(f"[Sync #{cycle_count}] Workspace already in sync with git. No new changes.")
        return True

    changed_files = [f for f in out.splitlines() if f.strip()]
    log.info(f"[Sync #{cycle_count}] Staged {len(changed_files)} changed files for commit.")

    # 3. Commit
    commit_msg = f"feat(telemetry): automated institutional sync #{cycle_count} [{time_str}]"
    code, c_out, c_err = run_git(["commit", "-m", commit_msg])
    if code != 0:
        log.warning(f"[Sync #{cycle_count}] Commit notice: {c_err}")
        return False

    log.info(f"[Sync #{cycle_count}] Committed: {commit_msg}")

    # 4. Push to origin main
    code, p_out, p_err = run_git(["push", "origin", "main"], timeout=60)
    if code == 0:
        log.info(f"[Sync #{cycle_count}] SUCCESS: Pushed to GitHub origin/main!")
        return True
    else:
        log.warning(f"[Sync #{cycle_count}] Push failed ({p_err}). Attempting rebase...")
        run_git(["pull", "--rebase", "-X", "theirs", "origin", "main"], timeout=60)
        code2, _, p_err2 = run_git(["push", "origin", "main"], timeout=60)
        if code2 == 0:
            log.info(f"[Sync #{cycle_count}] SUCCESS: Pushed after rebase!")
            return True
        else:
            log.error(f"[Sync #{cycle_count}] Git push failed: {p_err2}")
            return False

def main():
    parser = argparse.ArgumentParser(description="Standalone Git Telemetry & Ledger Sync Daemon")
    parser.add_argument("--once", action="store_true", help="Run single sync and exit")
    parser.add_argument("--interval", type=int, default=60, help="Sync interval in seconds (default: 60s)")
    args = parser.parse_args()

    log.info("=" * 80)
    log.info("🏛️ STANDALONE GIT TELEMETRY & LEDGER DAEMON INITIALIZED")
    log.info(f"Target: origin/main | Mode: {'Single-Pass (--once)' if args.once else f'Loop ({args.interval}s)'}")
    log.info("=" * 80)

    count = 0
    while True:
        count += 1
        try:
            sync_telemetry_to_git(count)
        except Exception as e:
            log.error(f"Error in sync iteration #{count}: {e}\n{traceback.format_exc()}")

        if args.once:
            break

        time.sleep(args.interval)

if __name__ == "__main__":
    main()
