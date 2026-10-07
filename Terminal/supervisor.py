#!/usr/bin/env python3
"""Terminal/supervisor.py
================================
P2 FIX — Unified Process Supervisor.

Manages all three production daemons with automatic restart:
  1. telemetry_daemon   — autonomous_telemetry_git_daemon.py (60s git push)
  2. ratchet_monitor    — standalone ratchet polling loop (30s MT5 SL checks)
  3. risk_monitor       — arena_endless_runner.py (60s read-only risk monitor)

USAGE:
  python Terminal/supervisor.py [--dry-run]

  Or run as a Windows Scheduled Task:
  schtasks /Create /SC ONLOGON /TN "TradingSupervisor" /TR "python c:\\...\\Terminal\\supervisor.py" /F

The supervisor logs to Terminal/logs/supervisor.log.
"""
from __future__ import annotations

import argparse
import logging
import os
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# ---------------------------------------------------------------------------
# Logging
# ---------------------------------------------------------------------------
LOG_DIR = ROOT / "Terminal" / "logs"
LOG_DIR.mkdir(parents=True, exist_ok=True)
LOG_FILE = LOG_DIR / "supervisor.log"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s][Supervisor] %(levelname)s %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE, encoding="utf-8"),
        logging.StreamHandler(sys.stdout),
    ],
)
logger = logging.getLogger("Supervisor")


# ---------------------------------------------------------------------------
# Process definitions
# ---------------------------------------------------------------------------
PROCESSES = [
    {
        "name":          "telemetry_daemon",
        "cmd":           [sys.executable,
                          str(ROOT / "Terminal" / "Data_Factory" / "autonomous_telemetry_git_daemon.py")],
        "restart_delay": 10,
        "critical":      True,   # If True, supervisor alerts on repeated crashes
        "crash_limit":   5,
        "description":   "MT5 → telemetry JSON → GitHub (60s cycle)",
    },
    {
        "name":          "ratchet_monitor",
        "cmd":           [sys.executable, "-m", "Terminal.risk.ratchet_standalone"],
        "restart_delay": 5,
        "critical":      True,
        "crash_limit":   10,
        "description":   "Automated Phase 0/1/2 SL ratchet (30s poll)",
    },
    {
        "name":          "risk_monitor",
        "cmd":           [sys.executable,
                          str(ROOT / "scripts" / "arena_endless_runner.py"),
                          "--daemon", "--interval", "60", "--publish"],
        "restart_delay": 5,
        "critical":      False,
        "crash_limit":   20,
        "description":   "Read-only risk monitor + blackout alerts (60s cycle)",
    },
]


# ---------------------------------------------------------------------------
# Supervisor core
# ---------------------------------------------------------------------------
class Supervisor:
    def __init__(self, dry_run: bool = False):
        self.dry_run = dry_run
        self._procs: dict[str, subprocess.Popen] = {}
        self._crash_counts: dict[str, int] = {p["name"]: 0 for p in PROCESSES}
        self._last_start: dict[str, float] = {}

    def _launch(self, cfg: dict) -> subprocess.Popen | None:
        name = cfg["name"]
        if self.dry_run:
            logger.info("[DRY-RUN] Would launch: %s → %s", name, " ".join(str(c) for c in cfg["cmd"]))
            return None
        # Skip ratchet_standalone if module doesn't exist yet (optional)
        if name == "ratchet_monitor":
            try:
                import importlib
                importlib.util.find_spec("Terminal.risk.ratchet_standalone")
            except Exception:
                logger.info("ratchet_monitor skipped — ratchet_standalone not yet present.")
                return None
        # Skip risk_monitor if script doesn't exist
        if name == "risk_monitor":
            script = Path(cfg["cmd"][-3])
            if not script.exists():
                logger.info("risk_monitor skipped — %s not found.", script)
                return None
        try:
            proc = subprocess.Popen(
                cfg["cmd"],
                cwd=str(ROOT),
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                text=True,
                bufsize=1,
            )
            self._last_start[name] = time.time()
            logger.info("Launched %s (pid=%d): %s", name, proc.pid, cfg["description"])
            return proc
        except Exception as exc:
            logger.error("Failed to launch %s: %s", name, exc)
            return None

    def run(self) -> None:
        logger.info("Supervisor starting. dry_run=%s", self.dry_run)
        logger.info("Root: %s", ROOT)

        # Initial launch of all processes
        for cfg in PROCESSES:
            proc = self._launch(cfg)
            if proc:
                self._procs[cfg["name"]] = proc

        # Watch loop
        while True:
            try:
                for cfg in PROCESSES:
                    name = cfg["name"]
                    proc = self._procs.get(name)

                    if proc is None:
                        continue

                    if proc.poll() is not None:
                        exit_code = proc.returncode
                        self._crash_counts[name] += 1
                        count = self._crash_counts[name]
                        logger.warning(
                            "%s died (exit=%d, crash #%d). Restarting in %ds.",
                            name, exit_code, count, cfg["restart_delay"],
                        )

                        if cfg["critical"] and count >= cfg["crash_limit"]:
                            logger.error(
                                "CRITICAL: %s has crashed %d times — requires manual intervention.",
                                name, count,
                            )
                            # Alert via desk append if possible
                            self._alert_desk(name, count)

                        time.sleep(cfg["restart_delay"])
                        new_proc = self._launch(cfg)
                        if new_proc:
                            self._procs[name] = new_proc
                        else:
                            self._procs[name] = None

                # Heartbeat every 30 seconds
                now_utc = datetime.now(timezone.utc).strftime("%H:%M:%S UTC")
                live = [n for n, p in self._procs.items() if p and p.poll() is None]
                logger.info("Heartbeat %s | Live: %s", now_utc, ", ".join(live) or "NONE")
                time.sleep(30)

            except KeyboardInterrupt:
                logger.info("Supervisor shutting down (KeyboardInterrupt).")
                for proc in self._procs.values():
                    if proc and proc.poll() is None:
                        proc.terminate()
                break
            except Exception as exc:
                logger.error("Supervisor loop error: %s", exc)
                time.sleep(5)

    def _alert_desk(self, process_name: str, crash_count: int) -> None:
        """Append a critical alert to the live order desk."""
        try:
            desk = ROOT / "docs" / "trade_plans" / "LIVE_COLLABORATIVE_ORDER_DESK.md"
            if not desk.exists():
                return
            now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
            alert = (
                f"\n---\n\n## 🚨 SUPERVISOR ALERT — {now}\n\n"
                f"**CRITICAL**: Process `{process_name}` has crashed {crash_count} times "
                f"and may require manual restart. All ratchet and blackout monitoring "
                f"may be degraded until this process is restored.\n\n"
                f"**Action required**: Check `Terminal/logs/supervisor.log` and restart manually.\n"
            )
            with open(desk, "a", encoding="utf-8") as f:
                f.write(alert)
            logger.info("Crash alert appended to order desk for %s.", process_name)
        except Exception as exc:
            logger.warning("Failed to write crash alert to desk: %s", exc)


# ---------------------------------------------------------------------------
# Standalone ratchet monitor entry point (Terminal.risk.ratchet_standalone)
# ---------------------------------------------------------------------------
def _run_ratchet_standalone() -> None:
    """Standalone ratchet polling process — loads existing MT5 positions and runs."""
    logging.basicConfig(level=logging.INFO)
    from Terminal.risk.ratchet_manager import get_ratchet_manager
    try:
        import MetaTrader5 as mt5
        if not mt5.initialize():
            logger.error("MT5 initialize failed.")
            return
        manager = get_ratchet_manager()
        # Auto-register all currently open positions
        positions = mt5.positions_get() or []
        for p in positions:
            direction = 1 if p.type == mt5.ORDER_TYPE_BUY else -1
            manager.register(
                ticket=p.ticket,
                symbol=p.symbol,
                entry=float(p.price_open),
                sl=float(p.sl),
                tp=float(p.tp),
                direction=direction,
                staged_at=float(p.time),
            )
        logger.info("Ratchet standalone: registered %d open positions.", len(positions))
        manager.run_loop(interval_seconds=30)
    except Exception as exc:
        logger.error("Ratchet standalone error: %s", exc)
        raise


# ---------------------------------------------------------------------------
# Main entry point
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Trading system process supervisor.")
    parser.add_argument("--dry-run", action="store_true", help="Log what would be launched, don't actually launch.")
    parser.add_argument("--ratchet-only", action="store_true", help="Run only the ratchet monitor loop.")
    args = parser.parse_args()

    if args.ratchet_only:
        _run_ratchet_standalone()
    else:
        Supervisor(dry_run=args.dry_run).run()
