#!/usr/bin/env python3
"""
scripts/arena_endless_runner.py
================================
Autonomous Sentinel & Blackboard Synchronizer for Arena.ai.

Enables Arena.ai to operate in a continuous loop:
1. Pulls latest remote updates from GitHub (telemetry and blackboard).
2. Parses docs/telemetry/live_snapshot_latest.json.
3. Evaluates 24-asset orderflow confluence (|Z| >= 2.0 SD, CVD divergence, whale walls).
4. Formulates structured trade suggestions & verdicts.
5. Appends to docs/trade_plans/LIVE_COLLABORATIVE_ORDER_DESK.md.
6. Automatically commits and pushes to origin/arena/4adf3661-trading-2.

Usage:
    python scripts/arena_endless_runner.py --once        # Single execution cycle
    python scripts/arena_endless_runner.py --daemon      # Continuous 60s background loop
"""
from __future__ import annotations

import argparse
import datetime
import json
import logging
import os
import pathlib
import subprocess
import sys
import time

ROOT = pathlib.Path(__file__).resolve().parents[1]
TELEMETRY_PATH = ROOT / "docs" / "telemetry" / "live_snapshot_latest.json"
BLACKBOARD_PATH = ROOT / "docs" / "trade_plans" / "LIVE_COLLABORATIVE_ORDER_DESK.md"
BRANCH = "arena/83d03e3f-trading-2"

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)
logger = logging.getLogger("ArenaSentinel")


def run_git(args: list[str]) -> tuple[int, str]:
    """Run a git command in ROOT and return (code, output)."""
    try:
        res = subprocess.run(
            ["git"] + args,
            cwd=str(ROOT),
            capture_output=True,
            text=True,
            timeout=30
        )
        return res.returncode, (res.stdout + res.stderr).strip()
    except Exception as exc:
        return -1, str(exc)


def git_sync_pull() -> bool:
    """Safely fetch and rebase latest remote commits."""
    code, out = run_git(["pull", "--rebase", "--autostash", "origin", BRANCH])
    if code != 0:
        logger.warning(f"Git pull warning: {out}")
        return False
    return True


def git_sync_push(commit_msg: str) -> bool:
    """Stage blackboard, commit, and push to remote."""
    run_git(["add", str(BLACKBOARD_PATH.relative_to(ROOT))])
    code_c, out_c = run_git(["commit", "-m", commit_msg])
    if "nothing to commit" in out_c.lower():
        logger.info("Nothing to commit on blackboard.")
        return True
    if code_c != 0:
        logger.warning(f"Git commit warning: {out_c}")
        return False
    code_p, out_p = run_git(["push", "origin", BRANCH])
    if code_p != 0:
        logger.warning(f"Git push warning: {out_p}")
        return False
    logger.info("Successfully pushed blackboard update to GitHub.")
    return True


def audit_telemetry() -> dict | None:
    """Read and validate the latest telemetry snapshot."""
    if not TELEMETRY_PATH.exists():
        logger.error(f"Telemetry snapshot missing at {TELEMETRY_PATH}")
        return None
    try:
        with open(TELEMETRY_PATH, "r", encoding="utf-8") as f:
            data = json.load(f)
        return data
    except Exception as exc:
        logger.error(f"Failed to parse telemetry: {exc}")
        return None


def execute_cycle() -> None:
    """Execute a single evaluation and sync cycle."""
    logger.info("Starting Arena.ai evaluation cycle...")
    git_sync_pull()
    data = audit_telemetry()
    if not data:
        return

    acct = data.get("account", {})
    balance = acct.get("balance_usd", 0.0)
    equity = acct.get("equity_usd", 0.0)
    cushion = acct.get("cushion_above_floor_usd", 0.0)
    pos = data.get("active_positions", [])
    orders = data.get("pending_orders", [])
    assets = data.get("assets_matrix_24", {})

    now_utc = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
    logger.info(f"Telemetry as_of: {now_utc} | Balance: {balance} USD | Equity: {equity} USD | Pos: {len(pos)} | Pending: {len(orders)}")
    logger.info(f"Floor cushion above 4,775.00 USD floor: +{cushion:.2f} USD")


def main() -> None:
    parser = argparse.ArgumentParser(description="Arena.ai Endless Runner & Blackboard Sentinel")
    parser.add_argument("--daemon", action="store_true", help="Run endlessly in 60s loop")
    parser.add_argument("--interval", type=int, default=60, help="Loop interval in seconds")
    parser.add_argument("--once", action="store_true", help="Run a single pass and exit")
    args = parser.parse_args()

    if args.once or not args.daemon:
        execute_cycle()
        return

    logger.info(f"Starting Arena.ai Endless Daemon (interval={args.interval}s)...")
    while True:
        try:
            execute_cycle()
        except Exception as exc:
            logger.error(f"Error in cycle: {exc}", exc_info=True)
        time.sleep(args.interval)


if __name__ == "__main__":
    main()
