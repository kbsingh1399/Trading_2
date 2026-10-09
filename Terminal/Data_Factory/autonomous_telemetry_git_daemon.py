#!/usr/bin/env python3
"""
Terminal/Data_Factory/autonomous_telemetry_git_daemon.py
=========================================================
Zero-Token Autonomous Background Telemetry & Git Synchronization Daemon.

Operates 100% autonomously without LLM / AI token consumption:
1. Every 60 seconds, refreshes the live 24-asset market orderbook, liquidation
   observed depth, indicators, and MT5 account state via generate_full_snapshot().
2. Validates the successful generation's identity, age and provenance.
3. Fetches canonical main and permits only a safe fast-forward.
4. Commits only the fresh snapshot, preserving the operator's staged work.
5. All operations are non-blocking, headless, and logged to logs/autonomous_telemetry_git_daemon.log.
"""
from __future__ import annotations

import datetime
import json
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

BRANCH_NAME = "main"
CANONICAL_REMOTE = "https://github.com/kbsingh1399/Trading_2"
SNAPSHOT_FILE = "docs/telemetry/live_snapshot_latest.json"
INTERVAL_SECONDS = 60


PID_FILE = ROOT / "logs" / "autonomous_telemetry_git_daemon.pid"
_singleton_handle = None


def enforce_single_instance() -> None:
    """Hold an OS lock; a stale PID must never terminate an unrelated process."""
    global _singleton_handle
    if _singleton_handle is not None:
        return
    handle = PID_FILE.with_suffix(".lock").open("a+b")
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
        raise SystemExit(f"Telemetry publisher lock unavailable: {exc}") from exc
    _singleton_handle = handle


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


def load_successful_generation(generated_snapshot, *, clock=None):
    """Require the exact result of this cycle, never a leftover fresh file."""
    from Terminal.Telemetry_Provenance import validate_observed_snapshot
    try:
        document = json.loads((ROOT / SNAPSHOT_FILE).read_text(encoding="utf-8"))
        observed_now = clock() if clock is not None else time.time()
        if (not isinstance(generated_snapshot, dict) or not document.get("generation_id")
                or document != generated_snapshot or not validate_observed_snapshot(document)
                or document.get("snapshot_status") != "LIVE_OBSERVATION"
                or observed_now is None
                or not 0 <= float(observed_now) - float(document["as_of_epoch"]) <= 180):
            raise ValueError("missing, stale or mismatched successful generation")
        cap = document["capacity"]
        from Terminal.risk.live_admission import MAX_FILLED
        if (cap["max_concurrent"] != MAX_FILLED or cap["inventory_status"] != "OBSERVED"
                or cap["filled"] != len(document["active_positions"])
                or cap["pending"] != len(document["pending_orders"])
                or cap["used_joint_fill"] != cap["filled"] + cap["pending"]
                or document["account"].get("currency") != "USD"
                or document["account"].get("login") != 5064568):
            raise ValueError("capacity/account provenance invalid")
        for entry in document["assets_matrix_24"].values():
            for key, period in (("1h", 3600), ("4h", 14400)):
                bars, quality = entry[f"htf_{key}_ohlcv"], entry["htf_history"][key]
                if (quality["source"] != "MT5_BROKER_COMPLETED_BARS" or quality["completed_count"] != len(bars)
                        or any(float(b["close_ts"]) != float(b["ts"]) + period
                               or float(b["close_ts"]) > float(document["as_of_epoch"]) for b in bars)
                        or any(float(right["ts"]) <= float(left["ts"]) for left, right in zip(bars, bars[1:]))):
                    raise ValueError("completed broker HTF provenance invalid")
        return document
    except (OSError, ValueError, TypeError, KeyError) as exc:
        logger.error("REFUSING invalid telemetry publication: %s", exc)
        return None


def sync_git_cycle(generated_snapshot=None, *, clock=None):
    """Publish this successful cycle's snapshot alone to canonical main."""
    if load_successful_generation(generated_snapshot, clock=clock) is None:
        return False
    code, branch, _ = run_cmd(["git", "branch", "--show-current"])
    if code or branch != BRANCH_NAME:
        logger.warning("REFUSING telemetry publication outside main")
        return False
    for kind in ("--fetch", "--push"):
        args = ["git", "remote", "get-url", "--all"] + (["--push"] if kind == "--push" else []) + ["origin"]
        code, urls, _ = run_cmd(args)
        if code or any(url.removesuffix(".git").rstrip("/") != CANONICAL_REMOTE for url in urls.splitlines()) or not urls:
            logger.warning("REFUSING noncanonical origin %s URL", kind)
            return False
    code, staged, _ = run_cmd(["git", "diff", "--cached", "--name-only"])
    if code or any(path != SNAPSHOT_FILE for path in staged.splitlines()):
        logger.info("Telemetry publication deferred: operator has staged changes")
        return False
    code, _, err = run_cmd(["git", "fetch", "origin", BRANCH_NAME])
    if code:
        logger.warning("git fetch failed: %s", err)
        return False
    local_code, local_rev, _ = run_cmd(["git", "rev-parse", "HEAD"])
    remote_code, remote_rev, _ = run_cmd(["git", "rev-parse", f"origin/{BRANCH_NAME}"])
    if local_code or remote_code or not local_rev or not remote_rev:
        return False
    if local_rev != remote_rev:
        code, _, _ = run_cmd(["git", "merge-base", "--is-ancestor", "HEAD", f"origin/{BRANCH_NAME}"])
        if code:
            logger.warning("Telemetry publication deferred: local main is ahead or diverged")
            return False
        code, _, err = run_cmd(["git", "merge", "--ff-only", f"origin/{BRANCH_NAME}"])
        if code:
            logger.warning("Safe fast-forward unavailable; preserving local work: %s", err)
            return False
    # A fast-forward or another writer may have replaced the generated file.
    if load_successful_generation(generated_snapshot, clock=clock) is None:
        return False
    code, modified, _ = run_cmd(["git", "status", "--porcelain", "--", SNAPSHOT_FILE])
    if code or not modified:
        return False
    # --only excludes every foreign index entry even if it appears after the
    # initial staged-work check; no bare commit, directory add or auto-stash.
    now_str = generated_snapshot["as_of_utc"]
    code, _, err = run_cmd(["git", "commit", "--only", "-m", f"telemetry: observed snapshot [as_of {now_str}]", "--", SNAPSHOT_FILE])
    if code:
        logger.warning("Telemetry commit failed: %s", err)
        return False
    code, _, err = run_cmd(["git", "push", "origin", "HEAD:main"])
    if code:
        logger.warning("Telemetry push failed; retaining local commit for review: %s", err)
        return False
    logger.info("Published this cycle's observed snapshot to canonical origin/main")
    return True



def main():
    enforce_single_instance()
    logger.info("=====================================================================")
    logger.info("Starting Zero-Token Autonomous Telemetry & Git Synchronization Daemon")
    logger.info(f"Target Branch: {BRANCH_NAME} | Cadence: Every {INTERVAL_SECONDS}s | PID: {os.getpid()}")
    logger.info("=====================================================================")

    from Terminal.MT5_Execution_Bridge import MT5ExecutionBridge
    from Terminal.Data_Factory import generate_telemetry_snapshot as gen_mod
    # Keep confirmed clock evidence across cycles; cold deployment requires a
    # process restart rather than reloading unverified source during dispatch.
    bridge = MT5ExecutionBridge(5064568)
    iteration = 0
    while True:
        try:
            iteration += 1
            t_start = time.time()
            now_str = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
            logger.info(f"--- Iteration #{iteration} [{now_str}] ---")

            # Step 1: Generate fresh observations using this process's pinned code.
            snapshot = None
            try:
                snapshot = gen_mod.generate_full_snapshot(bridge=bridge)
                equity = snapshot.get("account", {}).get("equity_usd", 0.0)
                cushion = snapshot.get("account", {}).get("cushion_above_floor_usd", 0.0)
                pending = snapshot.get("capacity", {}).get("pending", 0)
                logger.info(f"Telemetry generated. Equity: {equity:.2f} USD | Cushion: +{cushion:.2f} USD | Pending Orders: {pending}")
            except Exception as exc:
                logger.error(f"Error during generate_full_snapshot: {exc}", exc_info=True)

            # Step 2: Git Synchronization (fetch, pull Arena messages, push telemetry)
            try:
                if snapshot is not None:
                    sync_git_cycle(snapshot, clock=bridge.broker_utc_now)
            except Exception as exc:
                logger.error(f"Error during sync_git_cycle: {exc}", exc_info=True)

            # Memory cleanup
            gc.collect()

            elapsed = time.time() - t_start
            sleep_time = max(5.0, INTERVAL_SECONDS - elapsed)
            logger.info(f"Cycle completed in {elapsed:.2f}s. Sleeping for {sleep_time:.2f}s...")
            time.sleep(sleep_time)
        except Exception as loop_err:
            logger.error(f"Unhandled daemon loop exception in iteration #{iteration}: {loop_err}", exc_info=True)
            time.sleep(5.0)


if __name__ == "__main__":
    main()
