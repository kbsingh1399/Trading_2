#!/usr/bin/env python3
"""
Terminal/Data_Factory/autonomous_telemetry_git_daemon.py
=========================================================
Zero-Token Autonomous Background Telemetry & Git Synchronization Daemon.

Operates 100% autonomously without LLM / AI token consumption:
1. Every 60 seconds, refreshes the live 24-asset market orderbook, liquidation
   bands, stop clusters, indicators, and MT5 account state via generate_full_snapshot().
2. Automatically performs git fetch against origin/arena/4adf3661-trading-2.
3. If Arena.ai has pushed a new commit (Council report or trade plan):
   - Rebases remote commits into local branch.
   - Logs commit details and alerts the trading engine.
4. Automatically commits and pushes fresh telemetry updates to GitHub every 60 seconds.
5. All operations are non-blocking, headless, and logged to logs/autonomous_telemetry_git_daemon.log.
"""
from __future__ import annotations

import datetime
import gc
import logging
import os
import pathlib
import subprocess
import sys
import time

ROOT = pathlib.Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

LOG_DIR = ROOT / "logs"
LOG_DIR.mkdir(parents=True, exist_ok=True)
LOG_FILE = LOG_DIR / "autonomous_telemetry_git_daemon.log"

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE, encoding="utf-8"),
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger("TelemetryGitDaemon")

BRANCH_NAME = "arena/83d03e3f-trading-2"
INTERVAL_SECONDS = 60


PID_FILE = ROOT / "logs" / "autonomous_telemetry_git_daemon.pid"


def enforce_single_instance() -> None:
    """Ensure exactly one instance of this daemon runs across the OS."""
    current_pid = os.getpid()
    if PID_FILE.exists():
        try:
            content = PID_FILE.read_text(encoding="utf-8").strip()
            if content:
                old_pid = int(content)
                if old_pid != current_pid:
                    check = subprocess.run(
                        ["tasklist", "/FI", f"PID eq {old_pid}"],
                        capture_output=True,
                        text=True
                    )
                    if str(old_pid) in check.stdout:
                        logger.warning(f"Detected existing daemon instance PID {old_pid}. Terminating to eliminate split-brain...")
                        subprocess.run(["taskkill", "/F", "/PID", str(old_pid)], capture_output=True)
                        time.sleep(1.0)
        except Exception as exc:
            logger.warning(f"Error checking previous PID file: {exc}")
    try:
        PID_FILE.write_text(str(current_pid), encoding="utf-8")
    except Exception as exc:
        logger.warning(f"Failed to write PID file: {exc}")


def run_cmd(cmd: list[str], cwd: pathlib.Path = ROOT) -> tuple[int, str, str]:
    """Execute shell command cleanly and return code, stdout, stderr."""
    try:
        proc = subprocess.run(
            cmd,
            cwd=str(cwd),
            capture_output=True,
            text=True,
            timeout=45
        )
        return proc.returncode, proc.stdout.strip(), proc.stderr.strip()
    except subprocess.TimeoutExpired:
        return -1, "", "Timeout expired"
    except Exception as exc:
        return -1, "", str(exc)


def sync_git_cycle():
    """Fetch from remote, pull Arena updates, and push fresh telemetry."""
    # 1. Fetch remote
    code, out, err = run_cmd(["git", "fetch", "origin", BRANCH_NAME])
    if code != 0:
        logger.warning(f"git fetch failed: {err}")
        return

    # 2. Check if remote has new commits
    code, local_rev, _ = run_cmd(["git", "rev-parse", "HEAD"])
    code, remote_rev, _ = run_cmd(["git", "rev-parse", f"origin/{BRANCH_NAME}"])

    if local_rev != remote_rev and remote_rev:
        logger.info(f"Detected new remote revision on origin/{BRANCH_NAME}: {remote_rev[:7]} (local: {local_rev[:7]})")
        # Pull with rebase
        pull_code, pull_out, pull_err = run_cmd(["git", "pull", "--rebase", "--autostash", "origin", BRANCH_NAME])
        if pull_code == 0:
            logger.info(f"Successfully rebased remote changes from Arena.ai: {pull_out}")
            # Log any newly received trade plans or audits
            code, diff_files, _ = run_cmd(["git", "diff", "--name-only", f"{local_rev}..{remote_rev}"])
            if diff_files:
                logger.info(f"Files updated by Arena.ai:\n{diff_files}")
        else:
            logger.error(f"git pull --rebase failed: {pull_err}")
            run_cmd(["git", "rebase", "--abort"])

    # 3. Check for modified telemetry or audit files to commit and push
    code, status_out, _ = run_cmd(["git", "status", "--porcelain", "docs/telemetry/", "docs/audits/"])
    if status_out:
        run_cmd(["git", "add", "docs/telemetry/live_snapshot_latest.json", "docs/audits/"])
        now_str = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
        commit_msg = f"telemetry: live 1m auto-sync [as_of {now_str}]"
        c_code, c_out, c_err = run_cmd(["git", "commit", "-m", commit_msg])
        if c_code == 0:
            logger.info(f"Committed fresh telemetry: {commit_msg}")
            p_code, p_out, p_err = run_cmd(["git", "push", "origin", BRANCH_NAME])
            if p_code == 0:
                logger.info(f"Successfully pushed telemetry to origin/{BRANCH_NAME}")
                # Also keep main updated at all times per user directive
                run_cmd(["git", "push", "origin", f"{BRANCH_NAME}:main"])
            else:
                logger.warning(f"git push rejected or failed: {p_err}. Retrying with rebase...")
                run_cmd(["git", "pull", "--rebase", "--autostash", "origin", BRANCH_NAME])
                run_cmd(["git", "push", "origin", BRANCH_NAME])
                run_cmd(["git", "push", "origin", f"{BRANCH_NAME}:main"])


def main():
    enforce_single_instance()
    logger.info("=====================================================================")
    logger.info("Starting Zero-Token Autonomous Telemetry & Git Synchronization Daemon")
    logger.info(f"Target Branch: {BRANCH_NAME} | Cadence: Every {INTERVAL_SECONDS}s | PID: {os.getpid()}")
    logger.info("=====================================================================")

    import importlib
    iteration = 0
    while True:
        iteration += 1
        t_start = time.time()
        now_str = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
        logger.info(f"--- Iteration #{iteration} [{now_str}] ---")

        # Step 1: Refresh telemetry snapshot with dynamic reload to eliminate stale RAM state
        try:
            import Terminal.Data_Factory.generate_telemetry_snapshot as gen_mod
            importlib.reload(gen_mod)
            snapshot = gen_mod.generate_full_snapshot()
            equity = snapshot.get("account", {}).get("equity_usd", 0.0)
            cushion = snapshot.get("account", {}).get("cushion_above_floor_usd", 0.0)
            pending = snapshot.get("capacity", {}).get("pending", 0)
            logger.info(f"Telemetry generated. Equity: {equity:.2f} USD | Cushion: +{cushion:.2f} USD | Pending Orders: {pending}")
        except Exception as exc:
            logger.error(f"Error during generate_full_snapshot: {exc}")

        # Step 2: Git Synchronization (fetch, pull Arena messages, push telemetry)
        try:
            sync_git_cycle()
        except Exception as exc:
            logger.error(f"Error during sync_git_cycle: {exc}")

        # Memory cleanup
        gc.collect()

        elapsed = time.time() - t_start
        sleep_time = max(5.0, INTERVAL_SECONDS - elapsed)
        logger.info(f"Cycle completed in {elapsed:.2f}s. Sleeping for {sleep_time:.2f}s...")
        time.sleep(sleep_time)


if __name__ == "__main__":
    main()
