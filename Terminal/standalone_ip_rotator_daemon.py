#!/usr/bin/env python3
"""
Terminal/standalone_ip_rotator_daemon.py
========================================
Dedicated background daemon for continuous Cloudflare WARP egress IP rotation.

Features:
- Rotates WireGuard/MASQUE tunnel keys and reconnects at a configurable interval (default: 300s).
- Guarantees WARP connection is NEVER left in a disconnected or degraded state.
- Atomically writes real-time health telemetry to Data/ip_rotator_status.json.
- Gracefully handles termination signals (SIGINT, SIGTERM).
"""

from __future__ import annotations
import argparse
import datetime
import json
import logging
import os
import pathlib
import signal
import sys
import time

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

ROOT_DIR = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT_DIR))

from Terminal.rotate_ip import ensure_warp_connected, get_current_ip, get_warp_status, rotate_ip

PID_FILE = ROOT_DIR / "Data" / "standalone_ip_rotator_daemon.pid"
STATUS_FILE = ROOT_DIR / "Data" / "ip_rotator_status.json"

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] [IPRotatorDaemon] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
log = logging.getLogger("IPRotatorDaemon")

RUNNING = True


def signal_handler(signum, frame):
    global RUNNING
    log.info(f"Signal {signum} received. Initiating graceful shutdown of IP Rotator Daemon...")
    RUNNING = False


def record_status(status_dict: dict) -> None:
    try:
        STATUS_FILE.parent.mkdir(parents=True, exist_ok=True)
        tmp = STATUS_FILE.with_suffix(".tmp")
        tmp.write_text(json.dumps(status_dict, indent=2), encoding="utf-8")
        tmp.replace(STATUS_FILE)
    except Exception as e:
        log.warning(f"Failed to record status file: {e}")


def write_pid():
    PID_FILE.parent.mkdir(parents=True, exist_ok=True)
    PID_FILE.write_text(str(os.getpid()), encoding="utf-8")


def remove_pid():
    if PID_FILE.exists():
        try:
            PID_FILE.unlink()
        except Exception:
            pass


def run_daemon(interval_sec: int = 300):
    global RUNNING
    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)

    write_pid()
    log.info(f"IP Rotator Daemon started (PID {os.getpid()}). Rotation interval: {interval_sec}s.")

    # Step 0: Ensure initial connection
    ensure_warp_connected(max_wait_s=15.0)
    current_ip = get_current_ip()
    warp_status, is_healthy = get_warp_status()
    log.info(f"Initial State: Status={warp_status}, Healthy={is_healthy}, Public IP={current_ip}")

    rotation_count = 0
    state = {
        "pid": os.getpid(),
        "status": "RUNNING",
        "current_ip": current_ip,
        "previous_ip": None,
        "rotation_count": 0,
        "last_rotation_utc": datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC"),
        "warp_healthy": is_healthy,
        "warp_status": warp_status,
        "interval_seconds": interval_sec,
    }
    record_status(state)

    while RUNNING:
        try:
            log.info(f"Sleeping for {interval_sec}s until next IP rotation...")
            # Sleep in 1-second chunks so signal handler responds promptly
            for _ in range(interval_sec):
                if not RUNNING:
                    break
                time.sleep(1.0)

            if not RUNNING:
                break

            log.info(f"--- [Rotation #{rotation_count + 1}] Starting scheduled IP rotation ---")
            state["status"] = "ROTATING"
            record_status(state)

            t0 = time.time()
            success, old_ip, new_ip = rotate_ip()
            dt = time.time() - t0

            cur_status, cur_healthy = get_warp_status()
            if success and cur_healthy:
                rotation_count += 1
                log.info(f"✅ Rotation #{rotation_count} SUCCESSFUL in {dt:.2f}s: {old_ip} -> {new_ip}")
                state.update({
                    "status": "HEALTHY",
                    "current_ip": new_ip,
                    "previous_ip": old_ip,
                    "rotation_count": rotation_count,
                    "last_rotation_utc": datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC"),
                    "warp_healthy": True,
                    "warp_status": "Connected",
                    "last_duration_sec": round(dt, 2),
                })
            else:
                log.warning(f"⚠️ Rotation #{rotation_count + 1} did not verify healthy in {dt:.2f}s. Re-ensuring connection...")
                ensure_warp_connected(max_wait_s=15.0)
                re_ip = get_current_ip()
                re_status, re_healthy = get_warp_status()
                state.update({
                    "status": "RECOVERED" if re_healthy else "UNHEALTHY",
                    "current_ip": re_ip,
                    "warp_healthy": re_healthy,
                    "warp_status": re_status,
                })

            record_status(state)

        except Exception as exc:
            log.error(f"Unexpected error in IP Rotator loop: {exc}", exc_info=True)
            ensure_warp_connected(max_wait_s=15.0)
            time.sleep(10.0)

    remove_pid()
    state["status"] = "STOPPED"
    record_status(state)
    log.info("IP Rotator Daemon terminated cleanly.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Standalone Cloudflare WARP IP Rotator Daemon")
    parser.add_argument("--interval", type=int, default=300, help="Rotation interval in seconds (default: 300)")
    args = parser.parse_args()

    run_daemon(interval_sec=args.interval)
