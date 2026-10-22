#!/usr/bin/env python3
"""
Terminal/Data_Factory/autonomous_git_sync_daemon.py
===================================================
Autonomous 5-Minute Git Synchronization Daemon for Trading_2.

Continuously commits and pushes all local files and directories to GitHub origin/main
every 5 minutes (300 seconds) without token cost.

Key Features:
1. Pure decoupled git sync — zero reliance on external APIs or telemetry schemas.
2. Excel Atomic Protection: Verifies Data/DataBase_Trading.xlsx is fully written
   and uncorrupted before staging. If in-flight, it temporarily unstages the file.
3. Fast-forward / Rebase resilience: Safely synchronizes with remote changes.
4. Non-blocking logging to logs/autonomous_git_sync_daemon.log and stdout.
"""

from __future__ import annotations

import datetime
import logging
import os
import pathlib
import subprocess
import sys
import time
import zipfile

ROOT = pathlib.Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

LOG_DIR = ROOT / "logs"
LOG_DIR.mkdir(parents=True, exist_ok=True)
LOG_FILE = LOG_DIR / "autonomous_git_sync_daemon.log"

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] [GitSyncDaemon] %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE, encoding="utf-8"),
        logging.StreamHandler(sys.stdout),
    ],
)
logger = logging.getLogger("GitSyncDaemon")

BRANCH_NAME = "main"
CANONICAL_REMOTE = "https://github.com/kbsingh1399/Trading_2"
SYNC_INTERVAL_SECONDS = 300  # 5 minutes exact cadence

PID_FILE = ROOT / "logs" / "autonomous_git_sync_daemon.pid"
_singleton_handle = None


def enforce_single_instance() -> None:
    """Acquire single-instance lock to prevent duplicate sync daemons."""
    global _singleton_handle
    if _singleton_handle is not None:
        return
    lock_path = PID_FILE.with_suffix(".lock")
    handle = lock_path.open("a+b")
    try:
        if handle.seek(0, os.SEEK_END) == 0:
            handle.write(b"0")
            handle.flush()
        handle.seek(0)
        if os.name == "nt":
            import msvcrt
            msvcrt.locking(handle.fileno(), msvcrt.LK_NBLCK, 1)
        else:
            import fcntl
            fcntl.flock(handle.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
        PID_FILE.write_text(str(os.getpid()), encoding="utf-8")
    except OSError as exc:
        handle.close()
        raise SystemExit(f"GitSyncDaemon lock unavailable: {exc}") from exc
    _singleton_handle = handle


def run_cmd(cmd: list[str], cwd: pathlib.Path = ROOT, timeout: int = 60) -> tuple[int, str, str]:
    """Execute shell command cleanly and return (returncode, stdout, stderr)."""
    try:
        env = {**os.environ, "GIT_TERMINAL_PROMPT": "0"}
        proc = subprocess.run(
            cmd,
            cwd=str(cwd),
            capture_output=True,
            text=True,
            timeout=timeout,
            env=env,
        )
        return proc.returncode, proc.stdout.strip(), proc.stderr.strip()
    except subprocess.TimeoutExpired:
        return -1, "", "Timeout expired"
    except Exception as exc:
        return -1, "", str(exc)


def is_excel_healthy(excel_path: pathlib.Path) -> bool:
    """Verify DataBase_Trading.xlsx is complete and not mid-write."""
    if not excel_path.exists():
        return False
    try:
        if excel_path.stat().st_size < 10_000_000:
            return False
        with zipfile.ZipFile(excel_path, "r") as zf:
            if zf.testzip() is not None:
                return False
            if "[Content_Types].xml" not in zf.namelist():
                return False
        return True
    except Exception:
        return False


def sync_cycle() -> bool:
    """Execute one full git add, commit, and push cycle."""
    code, current_branch, _ = run_cmd(["git", "branch", "--show-current"])
    if code != 0 or current_branch != BRANCH_NAME:
        logger.warning("Not on %s branch (current: %s); skipping sync", BRANCH_NAME, current_branch)
        return False

    # 1. Fetch remote to maintain continuity
    code, _, err = run_cmd(["git", "fetch", "origin", BRANCH_NAME])
    if code != 0:
        logger.warning("git fetch origin %s failed: %s", BRANCH_NAME, err)

    # 2. Check if remote is ahead and can fast-forward cleanly
    code_local, local_rev, _ = run_cmd(["git", "rev-parse", "HEAD"])
    code_remote, remote_rev, _ = run_cmd(["git", "rev-parse", f"origin/{BRANCH_NAME}"])
    if code_local == 0 and code_remote == 0 and local_rev and remote_rev and local_rev != remote_rev:
        ancestor_code, _, _ = run_cmd(["git", "merge-base", "--is-ancestor", "HEAD", f"origin/{BRANCH_NAME}"])
        if ancestor_code == 0:
            ff_code, _, ff_err = run_cmd(["git", "merge", "--ff-only", f"origin/{BRANCH_NAME}"])
            if ff_code != 0:
                logger.warning("Fast-forward merge failed: %s", ff_err)

    # 3. Stage all local workspace files
    run_cmd(["git", "add", "-A"])

    # 4. Protect Excel master file if currently in-flight
    excel_path = ROOT / "Data" / "DataBase_Trading.xlsx"
    if excel_path.exists():
        if not is_excel_healthy(excel_path):
            logger.warning(
                "DataBase_Trading.xlsx is currently being written (%d bytes); un-staging from this commit",
                excel_path.stat().st_size,
            )
            run_cmd(["git", "reset", "HEAD", "--", "Data/DataBase_Trading.xlsx"])
        else:
            run_cmd(["git", "add", "Data/DataBase_Trading.xlsx"])

    # 5. Check if there are changes to commit
    code_status, status_out, _ = run_cmd(["git", "status", "--porcelain"])
    if not status_out:
        logger.info("Workspace is clean; 0 changes to commit.")
        return True

    # 6. Commit changes
    now_str = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
    commit_msg = f"feat(sync): autonomous 5-minute workspace sync [as_of {now_str}]"
    code_commit, _, commit_err = run_cmd(["git", "commit", "-m", commit_msg])
    if code_commit != 0:
        logger.warning("git commit failed: %s", commit_err)
        return False

    # 7. Push to origin main
    code_rev, head_rev, _ = run_cmd(["git", "rev-parse", "HEAD"])
    code_push, _, push_err = run_cmd(["git", "push", "origin", f"HEAD:{BRANCH_NAME}"])
    if code_push != 0:
        logger.warning("Push to %s failed: %s; attempting pull --rebase", BRANCH_NAME, push_err)
        run_cmd(["git", "pull", "--rebase", "origin", BRANCH_NAME])
        code_retry, _, retry_err = run_cmd(["git", "push", "origin", f"HEAD:{BRANCH_NAME}"])
        if code_retry != 0:
            logger.error("Push retry failed: %s", retry_err)
            return False

    logger.info("Successfully pushed 5-minute sync to origin/%s [commit %s]", BRANCH_NAME, head_rev[:9] if head_rev else "HEAD")
    return True


def main() -> None:
    enforce_single_instance()
    logger.info("=" * 70)
    logger.info("STARTING AUTONOMOUS 5-MINUTE GIT SYNC DAEMON")
    logger.info("Branch: %s | Cadence: Every %ds (5 min) | PID: %d", BRANCH_NAME, SYNC_INTERVAL_SECONDS, os.getpid())
    logger.info("=" * 70)

    cycle_count = 0
    while True:
        try:
            cycle_count += 1
            t0 = time.time()
            now_utc = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
            logger.info("--- Cycle #%d [%s] ---", cycle_count, now_utc)
            sync_cycle()
            elapsed = time.time() - t0
            sleep_sec = max(5.0, SYNC_INTERVAL_SECONDS - elapsed)
            logger.info("Cycle #%d finished in %.2fs. Next sync in %.0fs...", cycle_count, elapsed, sleep_sec)
            time.sleep(sleep_sec)
        except Exception as loop_exc:
            logger.error("Unhandled error in git sync loop: %s", loop_exc, exc_info=True)
            time.sleep(10.0)


if __name__ == "__main__":
    main()
