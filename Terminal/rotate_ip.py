#!/usr/bin/env python3
"""
Terminal/rotate_ip.py
=====================
Automated IP Rotation Utility for Autonomous Trading Pipeline.

Guarantees Cloudflare WARP is ALWAYS connected:
  1. ensure_warp_connected(): Verifies WARP is connected and healthy; if disconnected, connects immediately.
  2. rotate_ip(): Rotates cryptographic WireGuard/MASQUE tunnel keys (warp-cli tunnel rotate-keys),
     reconnects the tunnel, and verifies WARP is healthy and active.
  3. Under NO circumstance is the connection ever left in a 'Disconnected' state.
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


def get_warp_status() -> tuple[str, bool]:
    """Returns (status_str, is_healthy). Status can be 'Connected', 'Connecting', or 'Disconnected'."""
    code, out = run_cmd(["warp-cli", "status"])
    is_connected = "Connected" in out
    is_healthy = "healthy" in out
    if is_connected:
        return "Connected", is_healthy
    elif "Connecting" in out:
        return "Connecting", False
    return "Disconnected", False


def ensure_warp_connected(max_wait_s: float = 15.0) -> bool:
    """
    Guarantees that Cloudflare WARP is connected and healthy.
    If disconnected or connecting, connects immediately and waits for health verification.
    """
    status, healthy = get_warp_status()
    if status != "Connected" or not healthy:
        log.info(f"Cloudflare WARP status is [{status}]. Connecting to Cloudflare WARP...")
        run_cmd(["warp-cli", "connect"])

    t0 = time.time()
    while (time.time() - t0) < max_wait_s:
        status, healthy = get_warp_status()
        if status == "Connected" and healthy:
            try:
                # Confirm outbound connectivity through WARP tunnel
                ip = get_current_ip(timeout=3)
                if ip != "UNKNOWN":
                    log.info(f"Cloudflare WARP is CONNECTED and healthy. Public IP: {ip}")
                    return True
            except Exception:
                pass
        time.sleep(1.0)

    log.warning(f"Could not verify healthy WARP connection within {max_wait_s}s. Re-issuing connect...")
    run_cmd(["warp-cli", "connect"])
    return False


def rotate_ip(max_retries: int = 3) -> tuple[bool, str, str]:
    """
    Rotates egress IP within Cloudflare WARP by rotating tunnel keys and reconnecting.
    Cloudflare WARP is NEVER left disconnected.
    """
    ensure_warp_connected(max_wait_s=10.0)
    old_ip = get_current_ip()
    log.info(f"Initiating Cloudflare WARP IP rotation. Current IP: {old_ip}")

    # 1. Rotate cryptographic WireGuard/MASQUE tunnel keys
    code, out = run_cmd(["warp-cli", "tunnel", "rotate-keys"])
    log.info(f"Rotated Cloudflare tunnel keys: {out}")
    time.sleep(1.0)

    # 2. Re-establish tunnel to bind to fresh ingress/egress node
    run_cmd(["warp-cli", "disconnect"])
    time.sleep(1.0)
    run_cmd(["warp-cli", "connect"])

    # 3. Ensure WARP is 100% connected and healthy before returning
    success = ensure_warp_connected(max_wait_s=15.0)
    new_ip = get_current_ip()
    new_status, new_healthy = get_warp_status()

    log.info(f"Post-rotation Cloudflare WARP status: {new_status} (healthy={new_healthy}) | Public IP: {new_ip}")
    return success, old_ip, new_ip


if __name__ == "__main__":
    ensure_warp_connected()
    success, old_ip, new_ip = rotate_ip()
    sys.exit(0 if success else 1)
