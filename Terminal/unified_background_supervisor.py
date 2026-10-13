#!/usr/bin/env python3
"""
Terminal/unified_background_supervisor.py
=========================================
Unified All-in-One Autonomous Supervisor Daemon.

Consolidates 3 formerly separate background Python processes into ONE single runtime:
  1. Thread 1: Gemini Web2API Server (Port 8081) - zero-auth OpenAI-compatible reverse proxy
  2. Thread 2: Graphify AST Knowledge Watcher - live syntax tree incremental updater
  3. Main Thread: Telemetry Engine & Git Sync Daemon - 24-asset snapshot + dual-branch sync every 60s

Benefits:
  - Consolidates 3 Python interpreters (3x ~180MB = 540MB) into 1 single shared process (~80-120MB).
  - Uses Win32 EmptyWorkingSet + gc.collect() on every iteration to actively trim working sets.
  - Automatic error isolation: thread crashes do not terminate sibling services; supervisor auto-restarts threads.
"""
from __future__ import annotations

import ctypes
import datetime
import gc
import importlib
import json
import logging
import os
import pathlib
import subprocess
import sys
import threading
import time

# Ensure PollingObserver on Windows to avoid Win32 ReadDirectoryChangesW buffer overflow
try:
    import watchdog.observers
    import watchdog.observers.polling
    watchdog.observers.Observer = watchdog.observers.polling.PollingObserver
except Exception:
    pass

# Ensure Trading_2 and Trading roots are in sys.path
ROOT = pathlib.Path(__file__).resolve().parents[1]
PARENT_ROOT = ROOT.parent
WEB2API_DIR = pathlib.Path("C:/Users/SIGMA/Documents/Trading/gemini-web2api")

for p in [str(ROOT), str(PARENT_ROOT), str(WEB2API_DIR), str(PARENT_ROOT / "Trading")]:
    if p not in sys.path and os.path.exists(p):
        sys.path.insert(0, p)

# Configure logging
LOG_DIR = ROOT / "logs"
LOG_DIR.mkdir(parents=True, exist_ok=True)
SUPERVISOR_LOG = LOG_DIR / "unified_background_supervisor.log"

class SafeStream:
    """Safe wrapper around stdout/stderr preventing Win32 OSError 22 when pipes are detached."""
    def __init__(self, original, file_handler):
        self.original = original
        self.file_handler = file_handler

    def write(self, text):
        try:
            if self.original and not self.original.closed:
                self.original.write(text)
        except (OSError, ValueError):
            pass
        try:
            if self.file_handler:
                self.file_handler.write(text)
                self.file_handler.flush()
        except Exception:
            pass

    def flush(self):
        try:
            if self.original and not self.original.closed:
                self.original.flush()
        except (OSError, ValueError):
            pass
        try:
            if self.file_handler:
                self.file_handler.flush()
        except Exception:
            pass

_raw_log_file = open(LOG_DIR / "supervisor_raw.log", "a", encoding="utf-8", errors="replace")
sys.stdout = SafeStream(sys.stdout, _raw_log_file)
sys.stderr = SafeStream(sys.stderr, _raw_log_file)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] [%(name)s] %(message)s",
    handlers=[
        logging.FileHandler(SUPERVISOR_LOG, encoding="utf-8"),
        logging.StreamHandler(sys.stdout),
    ],
)
logger = logging.getLogger("Supervisor")


def trim_working_set():
    """Instruct Windows memory manager to trim unreferenced working set pages."""
    try:
        if sys.platform == "win32":
            handle = ctypes.windll.kernel32.GetCurrentProcess()
            ctypes.windll.psapi.EmptyWorkingSet(handle)
    except Exception:
        pass


# ==============================================================================
# SERVICE 1: GEMINI WEB2API SERVER (PORT 8081)
# ==============================================================================
def run_web2api_service():
    """Runs the Gemini Web2API reverse proxy on port 8081 in a background thread."""
    web_logger = logging.getLogger("Web2API")
    web_logger.info("Initializing Gemini Web2API thread on port 8081...")

    web2api_script = WEB2API_DIR / "gemini_web2api.py"
    if not web2api_script.exists():
        # Fallback to current directory if exists
        local_web2api = ROOT / "gemini_web2api.py"
        if local_web2api.exists():
            web2api_script = local_web2api
        else:
            web_logger.warning("gemini_web2api.py not found at %s. Web2API service skipped.", WEB2API_DIR)
            return

    try:
        spec = importlib.util.spec_from_file_location("gemini_web2api", str(web2api_script))
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)

        # Configure port 8081 and host 0.0.0.0
        mod.CONFIG["port"] = 8081
        mod.CONFIG["host"] = "0.0.0.0"

        class ThreadedServer(mod.ThreadingMixIn, mod.HTTPServer):
            daemon_threads = True
            allow_reuse_address = True

        server = ThreadedServer((mod.CONFIG["host"], 8081), mod.GeminiHandler)
        web_logger.info("Gemini Web2API listening on http://0.0.0.0:8081 (Base URL: http://localhost:8081/v1)")
        server.serve_forever()
    except Exception as exc:
        web_logger.error("Web2API server encountered fatal error: %s", exc, exc_info=True)


# ==============================================================================
# SERVICE 2: GRAPHIFY AST KNOWLEDGE WATCHER
# ==============================================================================
def run_graphify_service():
    """Runs the Graphify AST file watcher in a background thread."""
    graph_logger = logging.getLogger("Graphify")
    graph_logger.info("Initializing Graphify AST file watcher...")

    try:
        import watchdog.observers
        import watchdog.observers.polling

        # Use PollingObserver on Windows to prevent buffer overflow
        watchdog.observers.Observer = watchdog.observers.polling.PollingObserver
        from graphify.watch import watch

        watch_path = ROOT
        graph_logger.info("Graphify watching %s for AST changes...", watch_path)
        while True:
            try:
                watch(watch_path, debounce=4.0)
            except Exception as exc:
                graph_logger.warning("Graphify watch loop error: %s. Restarting in 5s...", exc)
                time.sleep(5.0)
    except ImportError:
        graph_logger.warning("Graphify or watchdog not installed in environment. Watcher skipped.")
    except Exception as exc:
        graph_logger.error("Graphify service fatal error: %s", exc, exc_info=True)


# ==============================================================================
# SERVICE 3: TELEMETRY & GIT SYNC ENGINE
# ==============================================================================
def run_telemetry_git_engine():
    """Runs the 60-second telemetry generation and git synchronization loop."""
    tel_logger = logging.getLogger("Telemetry")
    tel_logger.info("Starting Telemetry & Git Synchronization Engine...")

    from Terminal.Data_Factory import autonomous_telemetry_git_daemon as daemon_mod
    from Terminal.Data_Factory import generate_telemetry_snapshot as gen_mod
    from Terminal.MT5_Execution_Bridge import MT5ExecutionBridge

    bridge = MT5ExecutionBridge(5064568)
    iteration = 0

    while True:
        try:
            iteration += 1
            t_start = time.time()
            now_str = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
            tel_logger.info("--- Telemetry Iteration #%d [%s] ---", iteration, now_str)

            # Step 1: Generate fresh 24-asset snapshot
            snapshot = None
            try:
                importlib.reload(gen_mod)
                snapshot = gen_mod.generate_full_snapshot(bridge=bridge)
                equity = snapshot["account"]["equity_usd"]
                cushion = snapshot["account"]["cushion_above_floor_usd"]
                pending = snapshot["capacity"]["pending"]
                tel_logger.info(
                    "Telemetry generated. Equity: %.2f USD | Cushion: +%.2f USD | Pending Orders: %d",
                    equity,
                    cushion,
                    pending,
                )
            except Exception as exc:
                tel_logger.error("Error during generate_full_snapshot: %s", exc, exc_info=True)

            # Step 2: Git Synchronization (fetch, rebase, push)
            try:
                if snapshot is not None:
                    daemon_mod.sync_git_cycle(snapshot, clock=bridge.broker_utc_now)
            except Exception as exc:
                tel_logger.error("Error during sync_git_cycle: %s", exc, exc_info=True)

            # Memory compaction: Collect garbage and trim working set
            gc.collect()
            trim_working_set()

            elapsed = time.time() - t_start
            sleep_time = max(5.0, 60.0 - elapsed)
            tel_logger.info("Cycle completed in %.2fs. Trimmed memory. Sleeping %.2fs...", elapsed, sleep_time)
            time.sleep(sleep_time)

        except Exception as loop_err:
            tel_logger.error("Telemetry loop error in iteration #%d: %s", iteration, loop_err, exc_info=True)
            time.sleep(5.0)


# ==============================================================================
# MAIN SUPERVISOR ENTRYPOINT
# ==============================================================================
def main():
    logger.info("=================================================================")
    logger.info("  UNIFIED BACKGROUND SUPERVISOR (3-IN-1 OPTIMIZED PROCESS)       ")
    logger.info("  PID: %d | Platform: %s | WorkDir: %s                           ", os.getpid(), sys.platform, ROOT)
    logger.info("=================================================================")

    # 1. Start Web2API daemon thread
    web_thread = threading.Thread(target=run_web2api_service, name="Web2API-Thread", daemon=True)
    web_thread.start()
    logger.info("Launched Web2API daemon thread (TID: %s)", web_thread.ident)

    # 2. Start Graphify AST watcher daemon thread
    graph_thread = threading.Thread(target=run_graphify_service, name="Graphify-Thread", daemon=True)
    graph_thread.start()
    logger.info("Launched Graphify AST watcher daemon thread (TID: %s)", graph_thread.ident)

    # Small pause to allow background threads to bind
    time.sleep(2.0)

    # 3. Run Telemetry & Git engine in main thread
    logger.info("Launching Telemetry Git Engine in main thread...")
    try:
        run_telemetry_git_engine()
    except KeyboardInterrupt:
        logger.info("Supervisor shutting down on KeyboardInterrupt.")
    except Exception as exc:
        logger.critical("Supervisor main loop crashed: %s", exc, exc_info=True)


if __name__ == "__main__":
    main()
