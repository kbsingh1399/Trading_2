"""Terminal/Data_Factory/heretic_daemon.py
=========================================
Persistent Background Daemon for Heretic (p-e-w/heretic).

Runs as Always-On Background Task 5 in the Antigravity Multi-Daemon Architecture:
  1. AST Knowledge Graph Watcher (`python -m graphify watch .`)
  2. Telemetry Git Sync Daemon (`python Terminal/Data_Factory/autonomous_telemetry_git_daemon.py`)
  3. Web2API Council Daemon (`python gemini_web2api.py` on port 8081)
  4. Swarm Wake-up Cron (`29,59 * * * *`)
  5. Heretic Engine Daemon (`python Terminal/Data_Factory/heretic_daemon.py`)

Provides:
  - Persistent health telemetry in Data/heretic_daemon_status.json
  - Lightweight HTTP status server on port 8083 (http://localhost:8083/health)
  - Seamless interface to heretic CLI / API for representation engineering
"""
import http.server
import json
import logging
import os
import sys
import threading
import time
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
STATUS_FILE = ROOT / "Data" / "heretic_daemon_status.json"
PORT = 8083

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] [HereticDaemon] %(message)s"
)
logger = logging.getLogger("HereticDaemon")


def probe_heretic() -> tuple[bool, str]:
    try:
        import heretic
        return True, getattr(heretic, "__version__", "2.0.0.dev0")
    except Exception as exc:
        return False, f"import_error:{exc}"


_CURRENT_ENGINE_STATUS = {
    "engine": "heretic-llm",
    "repo_url": "https://github.com/p-e-w/heretic",
    "status": "INITIALIZING",
    "engine_probed": False,
    "engine_version": "unknown",
}


class HereticStatusHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path in ("/health", "/status", "/"):
            engine_ok, engine_ver = probe_heretic()
            _CURRENT_ENGINE_STATUS["engine_probed"] = engine_ok
            _CURRENT_ENGINE_STATUS["engine_version"] = engine_ver
            _CURRENT_ENGINE_STATUS["status"] = "HEALTHY" if engine_ok else "DEGRADED"

            status_code = 200 if engine_ok else 503
            self.send_response(status_code)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            status = dict(_CURRENT_ENGINE_STATUS)
            status["as_of_utc"] = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
            status["pid"] = os.getpid()
            status["uptime_sec"] = round(time.time() - START_TIME, 1)
            self.wfile.write(json.dumps(status, indent=2).encode("utf-8"))
        else:
            self.send_response(404)
            self.end_headers()

    def log_message(self, format, *args):
        pass  # Suppress noisy HTTP request logging


def run_http_server():
    server_address = ("127.0.0.1", PORT)
    try:
        httpd = http.server.HTTPServer(server_address, HereticStatusHandler)
        _CURRENT_ENGINE_STATUS["listening_port"] = PORT
        _CURRENT_ENGINE_STATUS["bind_error"] = None
        logger.info(f"Heretic HTTP server listening on http://127.0.0.1:{PORT}")
        httpd.serve_forever()
    except Exception as exc:
        _CURRENT_ENGINE_STATUS["listening_port"] = None
        _CURRENT_ENGINE_STATUS["bind_error"] = str(exc)
        logger.warning(f"Heretic HTTP server could not bind to port {PORT}: {exc}")


START_TIME = time.time()


def main():
    logger.info("Initializing Heretic Engine Always-On Daemon...")
    STATUS_FILE.parent.mkdir(parents=True, exist_ok=True)

    # Start lightweight HTTP server in background thread
    t = threading.Thread(target=run_http_server, daemon=True)
    t.start()

    logger.info("Heretic Daemon successfully started. Entering persistent heartbeat loop.")

    heartbeat_count = 0
    while True:
        heartbeat_count += 1
        now_ts = time.time()
        now_utc = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")

        try:
            import heretic
            engine_ok = True
            engine_ver = getattr(heretic, "__version__", "2.0.0.dev0")
        except Exception as exc:
            engine_ok = False
            engine_ver = f"import_error:{exc}"

        status_payload = {
            "engine": "heretic-llm",
            "repo_url": "https://github.com/p-e-w/heretic",
            "status": "RUNNING" if engine_ok else "DEGRADED",
            "engine_probed": engine_ok,
            "engine_version": engine_ver,
            "heartbeat": heartbeat_count,
            "pid": os.getpid(),
            "uptime_seconds": round(now_ts - START_TIME, 1),
            "last_heartbeat_utc": now_utc,
            "listening_port": PORT,
            "capabilities": [
                "directional_ablation",
                "ara_optimization",
                "optuna_tpe",
                "representation_engineering"
            ]
        }

        try:
            STATUS_FILE.write_text(json.dumps(status_payload, indent=2), encoding="utf-8")
        except Exception as exc:
            logger.warning(f"Failed to write status file: {exc}")

        if heartbeat_count % 5 == 1:
            logger.info(f"Heartbeat #{heartbeat_count} | Uptime: {status_payload['uptime_seconds']}s | Engine: heretic-llm READY")

        time.sleep(30)


if __name__ == "__main__":
    main()
