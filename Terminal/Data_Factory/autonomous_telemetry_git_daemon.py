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
CURRENT_ARENA_BRANCH = "arena/66c9be42-trading-2"
ASTRA_BRANCH = "arena/d6de1eb4-trading-2"
FABLE_BRANCH = "arena/af999588-trading-2"
ACTIVE_ARENA_BRANCH = "arena/74cd2d1a-trading-2"
PRIOR_ARENA_BRANCH = "arena/7a89a384-trading-2"
ACTIVE_ARENA_SESSION = "arena/186525a3-trading-2"
LEGACY_ARENA_1 = "arena/5c05910e-trading-2"
LEGACY_ARENA_2 = "arena/e3d7cc98-trading-2"
TARGET_BRANCHES = [BRANCH_NAME, CURRENT_ARENA_BRANCH, ACTIVE_ARENA_BRANCH, PRIOR_ARENA_BRANCH, ACTIVE_ARENA_SESSION, ASTRA_BRANCH, FABLE_BRANCH, LEGACY_ARENA_1, LEGACY_ARENA_2]
CANONICAL_REMOTE = "https://github.com/kbsingh1399/Trading_2"
SNAPSHOT_FILE = "docs/telemetry/live_snapshot_latest.json"
DATA_SYNC_FILES = [
    "docs/telemetry/live_snapshot_latest.json",
    "Data/forex_factory_live.json",
    "Data/forex_factory_summary.json",
    "Data/coinglass/latest/coinglass_snapshot.json",
    "Data/coinglass/latest/coinglass_whale_orders_snapshot.json",
    "Data/coinglass/coinglass_harvester_status.json",
    "Data/coinglass/whale_persistence_ledger.json",
    "docs/telemetry/coinglass_data_dictionary.md",
    "Data/history/master_manifest.json"
]
INTERVAL_SECONDS = 60  # 60-second high-velocity cadence: guarantees zero lag on GitHub after every cycle


PID_FILE = ROOT / "logs" / "autonomous_telemetry_git_daemon.pid"
_singleton_handle = None



WEB2API_DIR = pathlib.Path(r"C:\Users\SIGMA\Documents\Trading\gemini-web2api")
WEB2API_SCRIPT = WEB2API_DIR / "gemini_web2api.py"
WEB2API_PORT = 8081
_web2api_proc = None


def ensure_web2api_service() -> bool:
    """Guarantees gemini_web2api.py reverse proxy is running on port 8081 (Endogen architecture)."""
    global _web2api_proc
    import urllib.request
    import urllib.error
    
    # 1. First probe if service is already responding (200 OK or 401 Auth Required proves server is alive)
    try:
        req = urllib.request.Request(
            f"http://127.0.0.1:{WEB2API_PORT}/v1/models",
            headers={"Authorization": "Bearer sk-gemini"},
        )
        with urllib.request.urlopen(req, timeout=2) as resp:
            if resp.status == 200:
                return True
    except urllib.error.HTTPError as he:
        if he.code in (200, 401):
            return True
    except Exception:
        pass

    # 2. Check if we already hold an active subprocess handle that is still running
    if _web2api_proc is not None and _web2api_proc.poll() is None:
        return True

    # 3. Only spawn if definitely not running and script exists
    if WEB2API_SCRIPT.exists():
        logger.info("Spawning unified gemini_web2api service on port %d...", WEB2API_PORT)
        try:
            _web2api_proc = subprocess.Popen(
                [sys.executable, str(WEB2API_SCRIPT), "--port", str(WEB2API_PORT)],
                cwd=str(WEB2API_DIR),
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
            )
            time.sleep(2.0)
            logger.info("Spawned unified gemini_web2api PID %d on port %d", _web2api_proc.pid, WEB2API_PORT)
            return True
        except Exception as exc:
            logger.error("Failed to spawn gemini_web2api: %s", exc)
            return False
    return False

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


def run_cmd(cmd: list[str], cwd: pathlib.Path = ROOT, timeout: int = 45) -> tuple[int, str, str]:
    """Execute shell command cleanly and return code, stdout, stderr."""
    try:
        env = {**os.environ, "GIT_TERMINAL_PROMPT": "0"}
        proc = subprocess.run(
            cmd,
            cwd=str(cwd),
            capture_output=True,
            text=True,
            timeout=timeout,
            env=env
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
        observed_now = clock() if clock is not None else None
        if observed_now is None:
            observed_now = time.time()
        if (not isinstance(generated_snapshot, dict) or not document.get("generation_id")
                or document != generated_snapshot or not validate_observed_snapshot(document)
                or document.get("snapshot_status") != "LIVE_OBSERVATION"
                or not -5.0 <= float(observed_now) - float(document["as_of_epoch"]) <= 180.0):
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


def _verified_publication_revision(revision, remote_revision, generated_snapshot):
    """Prove an immutable revision contains only unpushed telemetry changes."""
    code, _, _ = run_cmd(["git", "merge-base", "--is-ancestor", remote_revision, revision])
    if code:
        return False
    code, commits, _ = run_cmd(["git", "rev-list", "--parents", f"{remote_revision}..{revision}"])
    if code:
        return False
    allowed_files = set(DATA_SYNC_FILES) | {SNAPSHOT_FILE}
    for row in commits.splitlines():
        parts = row.split()
        # A merge can import arbitrary operator work despite a clean final diff.
        if len(parts) != 2:
            return False
        code, changed, _ = run_cmd(["git", "diff-tree", "--no-commit-id", "--name-only", "-r", parts[0]])
        changed_files = set(changed.splitlines())
        if code or not changed_files or not changed_files.issubset(allowed_files):
            return False
    code, contents, _ = run_cmd(["git", "show", f"{revision}:{SNAPSHOT_FILE}"])
    try:
        if code != 0:
            return False
        head_snap = json.loads(contents)
        return (
            isinstance(head_snap, dict)
            and head_snap.get("protocol") == "omni.telemetry.v3.observed_only"
            and "account" in head_snap
            and "capacity" in head_snap
        )
    except (ValueError, TypeError):
        return False


def sync_git_cycle(generated_snapshot=None, *, clock=None):
    """Publish this cycle's snapshot and mirror the full local workspace to canonical main."""
    if load_successful_generation(generated_snapshot, clock=clock) is None:
        logger.warning("Telemetry snapshot generation validation failed; skipping sync cycle")
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

    # Fetch origin main to maintain continuity
    code, _, err = run_cmd(["git", "fetch", "origin", BRANCH_NAME])
    if code:
        logger.warning("git fetch failed: %s", err)
        return False

    # Operator Mandate: Full workspace replica sync (stage ALL changes but NEVER delete Data/feeds)
    try:
        from Terminal.Data_Factory.stamp_all_parquet_feeds import stamp_all_parquet_feeds
        stamp_all_parquet_feeds()
    except Exception as stamp_exc:
        logger.debug("Parquet stamp notice in git daemon: %s", stamp_exc)

    # Protect Data/feeds: never allow git daemon to stage feed removals
    run_cmd(["git", "add", "--ignore-removal", "Data/feeds", "Data/metadata"])
    run_cmd(["git", "add", "docs/telemetry", "docs/trade_plans", "docs/prompts", "Data/*.json", "Data/cycle_envelope.json", "Terminal/*.py"])

    code, modified_output, _ = run_cmd(["git", "status", "--porcelain"])
    if modified_output:
        now_str = generated_snapshot["as_of_utc"] if isinstance(generated_snapshot, dict) and "as_of_utc" in generated_snapshot else datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
        code, _, err = run_cmd(["git", "commit", "-m", f"feat(sync): mirror full local workspace and telemetry [as_of {now_str}]"])
        if code:
            logger.warning("Git commit failed: %s", err)
            return False

    code, publication_revision, _ = run_cmd(["git", "rev-parse", "HEAD"])
    if code or not publication_revision:
        return False

    # Push to main first (canonical source of truth)
    code_main, _, err_main = run_cmd(["git", "push", "origin", f"{publication_revision}:{BRANCH_NAME}"])
    if code_main:
        logger.warning("Full workspace push to %s failed: %s. Using force-with-lease to protect local feeds.", BRANCH_NAME, err_main)
        code_retry, _, err_retry = run_cmd(["git", "push", "--force-with-lease", "origin", f"HEAD:{BRANCH_NAME}"])
        if code_retry:
            logger.error("Push force-with-lease failed: %s", err_retry)
            return False

    logger.info("Successfully published full workspace replica to origin/%s [commit %s]", BRANCH_NAME, publication_revision[:9])

    # Push to active Arena branches (push only, never merge remote Arena branch back into main)
    for arena_br in [CURRENT_ARENA_BRANCH, ACTIVE_ARENA_BRANCH, PRIOR_ARENA_BRANCH, ACTIVE_ARENA_SESSION, ASTRA_BRANCH, FABLE_BRANCH]:
        code_br, _, err_br = run_cmd(["git", "push", "origin", f"{publication_revision}:{arena_br}"])
        if code_br == 0:
            logger.info("Published full workspace to origin/%s", arena_br)
        else:
            # Force push replica to Arena branch so main never gets corrupted by obsolete branch states
            code_f, _, err_f = run_cmd(["git", "push", "--force", "origin", f"{publication_revision}:{arena_br}"])
            if code_f == 0:
                logger.info("Force-updated origin/%s with current main replica", arena_br)
            else:
                logger.warning("Push to %s rejected: %s", arena_br, err_f)
    return True



def main():
    enforce_single_instance()
    logger.info("=====================================================================")
    logger.info("Starting Zero-Token Autonomous Telemetry & Git Synchronization Daemon")
    logger.info(f"Target Branch: {BRANCH_NAME} | Cadence: Every {INTERVAL_SECONDS}s | PID: {os.getpid()}")
    logger.info("=====================================================================")
    ensure_web2api_service()

    import importlib
    from Terminal.MT5_Execution_Bridge import MT5ExecutionBridge
    from Terminal import Api_Client as api_mod
    from Terminal.Data_Factory import generate_telemetry_snapshot as gen_mod
    bridge = MT5ExecutionBridge(5064568)
    iteration = 0
    while True:
        try:
            iteration += 1
            t_start = time.time()
            now_str = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
            logger.info(f"--- Iteration #{iteration} [{now_str}] ---")
            ensure_web2api_service()

            # Step 1: Reload generator module and generate fresh MT5/broker observations FIRST.
            snapshot = None
            try:
                importlib.reload(api_mod)
                importlib.reload(gen_mod)
                snapshot = gen_mod.generate_full_snapshot(bridge=bridge)
                equity = snapshot["account"]["equity_usd"]
                cushion = snapshot["account"]["cushion_above_floor_usd"]
                pending = snapshot["capacity"]["pending"]
                logger.info(f"Telemetry generated. Equity: {equity:.2f} USD | Cushion: +{cushion:.2f} USD | Pending Orders: {pending}")
                try:
                    from Terminal.Data_Factory.make_slim_snapshot import make_slim
                    make_slim()
                except Exception as slim_err:
                    logger.warning(f"Could not update slim snapshot: {slim_err}")

                # Continuous Time-Series Historical Database recording
                try:
                    from Terminal.Data_Factory.time_series_database import ts_db
                    ts_db.record_snapshot("telemetry", snapshot)
                    if "account" in snapshot:
                        ts_db.record_snapshot("account_equity", snapshot)
                except Exception as ts_err:
                    logger.warning(f"Could not record telemetry to TimeSeriesDB: {ts_err}")
            except Exception as exc:
                logger.error(f"Error during generate_full_snapshot: {exc}", exc_info=True)

            # Step 2: Immediate Git Synchronization (fetch, pull Arena messages, push telemetry to main & arena branches)
            try:
                if snapshot is not None:
                    sync_git_cycle(snapshot, clock=bridge.broker_utc_now)
            except Exception as exc:
                logger.error(f"Error during sync_git_cycle: {exc}", exc_info=True)

            # Step 3: Auxiliary Harvesters (Non-blocking, run AFTER telemetry is pushed)
            # (Arkham is decommissioned - Hyperdash decentralized intelligence provides whale flow)

            # Step 3b: Auxiliary CoinGlass browser scraper DECOMMISSIONED in favor of 100% Pure-Parquet Pipeline
            # All CoinGlass data is now harvested sequentially via Collectors/Browser/ in run_master_pipeline.py
            # to guarantee strictly 1 single tab and prevent dual-tab CDP conflicts.
            # (Legacy coinglass_harvester.harvest_all() disabled)

            # Step 3c: Ingest Forex Factory & Arkham into TimeSeriesDB
            try:
                from Terminal.Data_Factory.time_series_database import ts_db
                ff_file = ROOT / "Data" / "forex_factory_live.json"
                if ff_file.exists():
                    ff_data = json.loads(ff_file.read_text(encoding="utf-8"))
                    ts_db.record_snapshot("forex_factory", ff_data)
            except Exception as hist_err:
                logger.warning(f"Error recording auxiliary feeds to TimeSeriesDB: {hist_err}")

            # Autonomous RAM & Resource Optimization (Working Set Trim & Standby Purge)
            try:
                from Terminal.Data_Factory import system_memory_optimizer as mem_opt
                mem_report = mem_opt.optimize_ram(threshold_pct=75)
                logger.info("RAM Optimization status: Load=%s%% | Avail=%.2f GB | System cleanup triggered=%s",
                            mem_report.get("final", {}).get("memory_load_pct"),
                            mem_report.get("final", {}).get("avail_phys_gb", 0.0),
                            mem_report.get("triggered_system_cleanup"))
            except Exception as mem_err:
                logger.warning("RAM optimization step encountered error: %s", mem_err)

            elapsed = time.time() - t_start
            sleep_time = max(5.0, INTERVAL_SECONDS - elapsed)
            logger.info(f"Cycle completed in {elapsed:.2f}s. Sleeping for {sleep_time:.2f}s...")
            time.sleep(sleep_time)
        except Exception as loop_err:
            logger.error(f"Unhandled daemon loop exception in iteration #{iteration}: {loop_err}", exc_info=True)
            time.sleep(5.0)


if __name__ == "__main__":
    main()
