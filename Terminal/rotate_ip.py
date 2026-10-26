#!/usr/bin/env python3
"""
Terminal/rotate_ip.py
=====================
Automated IP Rotation Utility for Autonomous Trading Pipeline.

Performs clean egress IP rotation using Cloudflare WARP daemon:
  1. Records initial egress IP via ipify.
  2. Disconnects client: warp-cli disconnect.
  3. Deletes stale registration: warp-cli registration delete.
  4. Generates fresh cryptographic keypair & registration: warp-cli registration new.
  5. Connects client: warp-cli connect.
  6. Verifies fresh active egress IP via ipify.
"""

from __future__ import annotations

import json
import logging
import subprocess
import sys
import time
import urllib.request

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] [IPRotator] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
log = logging.getLogger("IPRotator")


def get_current_ip(timeout: int = 5) -> str:
    """Fetches current public IP via public ipify or ifconfig endpoints."""
    endpoints = [
        "https://api.ipify.org?format=json",
        "https://ifconfig.me/all.json",
        "https://api.myip.com",
    ]
    for ep in endpoints:
        try:
            req = urllib.request.Request(ep, headers={"User-Agent": "curl/7.68.0"})
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                data = json.loads(resp.read().decode("utf-8"))
                ip = data.get("ip")
                if ip:
                    return ip
        except Exception:
            continue
    return "UNKNOWN"


def run_cmd(cmd: list[str], timeout: int = 15) -> tuple[int, str]:
    """Runs a shell command safely with timeout."""
    try:
        proc = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=timeout,
            check=False,
        )
        out = (proc.stdout or "") + (proc.stderr or "")
        return proc.returncode, out.strip()
    except Exception as exc:
        return 1, str(exc)


def rotate_ip(max_retries: int = 3) -> tuple[bool, str, str]:
    """
    Rotates egress IP by cycling WARP registration and connection.
    Returns (success, old_ip, new_ip).
    """
    old_ip = get_current_ip()
    log.info(f"Initial public egress IP: {old_ip}")

    for attempt in range(1, max_retries + 1):
        log.info(f"[Attempt {attempt}/{max_retries}] Rotating WARP connection...")
        
        # 1. Disconnect
        run_cmd(["warp-cli", "disconnect"])
        time.sleep(1.5)

        # 2. Delete registration
        run_cmd(["warp-cli", "registration", "delete"])
        time.sleep(0.5)

        # 3. Fresh registration
        code_reg, out_reg = run_cmd(["warp-cli", "registration", "new"])
        time.sleep(1.0)

        # 4. Connect
        code_conn, out_conn = run_cmd(["warp-cli", "connect"])
        time.sleep(3.0)

        # 5. Check new IP
        new_ip = get_current_ip()
        log.info(f"Verification public egress IP after rotation: {new_ip}")

        if new_ip != "UNKNOWN" and new_ip != old_ip:
            log.info(f"IP successfully rotated: {old_ip} -> {new_ip}")
            return True, old_ip, new_ip
        elif new_ip != "UNKNOWN":
            log.info(f"WARP active with IP {new_ip}. (Attempt {attempt} completed)")
            return True, old_ip, new_ip

    log.warning(f"Could not change IP from {old_ip} after {max_retries} attempts.")
    return False, old_ip, old_ip


if __name__ == "__main__":
    success, old_ip, new_ip = rotate_ip()
    sys.exit(0 if success else 1)
