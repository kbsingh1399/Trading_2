"""
Institutional Logging & Resource Telemetry Infrastructure for Trading Data Pipeline
Provides dual output (Console + Rotating Log File), Windows Kernel RAM telemetry,
and atomic JSON event streaming for the autonomous telemetry daemon.
"""

from __future__ import annotations

import ctypes
import datetime
import json
import logging
from logging.handlers import RotatingFileHandler
import os
import pathlib
import sys
import time

MODULES_DIR = pathlib.Path(__file__).resolve().parent
ROOT_DIR = MODULES_DIR.parents[1]
LOGS_DIR = ROOT_DIR / "logs"
TELEMETRY_DIR = ROOT_DIR / "Data" / "telemetry"
TELEMETRY_FILE = TELEMETRY_DIR / "pipeline_events.jsonl"
DEFAULT_LOG_FILE = LOGS_DIR / "excel_pipeline.log"

LOGS_DIR.mkdir(parents=True, exist_ok=True)
TELEMETRY_DIR.mkdir(parents=True, exist_ok=True)


class MEMORYSTATUSEX(ctypes.Structure):
    _fields_ = [
        ("dwLength", ctypes.c_ulong),
        ("dwMemoryLoad", ctypes.c_ulong),
        ("ullTotalPhys", ctypes.c_ulonglong),
        ("ullAvailPhys", ctypes.c_ulonglong),
        ("ullTotalPageFile", ctypes.c_ulonglong),
        ("ullAvailPageFile", ctypes.c_ulonglong),
        ("ullTotalVirtual", ctypes.c_ulonglong),
        ("ullAvailVirtual", ctypes.c_ulonglong),
        ("sullAvailExtendedVirtual", ctypes.c_ulonglong),
    ]


def get_system_ram_telemetry() -> dict[str, float]:
    """Retrieves kernel-level physical RAM metrics on Windows via ctypes."""
    try:
        stat = MEMORYSTATUSEX()
        stat.dwLength = ctypes.sizeof(MEMORYSTATUSEX)
        if ctypes.windll.kernel32.GlobalMemoryStatusEx(ctypes.byref(stat)):
            total_mb = round(stat.ullTotalPhys / (1024 * 1024), 1)
            avail_mb = round(stat.ullAvailPhys / (1024 * 1024), 1)
            used_mb = round((stat.ullTotalPhys - stat.ullAvailPhys) / (1024 * 1024), 1)
            load_pct = int(stat.dwMemoryLoad)
            return {
                "used_mb": used_mb,
                "avail_mb": avail_mb,
                "total_mb": total_mb,
                "load_pct": load_pct,
            }
    except Exception:
        pass
    return {"used_mb": 0.0, "avail_mb": 0.0, "total_mb": 0.0, "load_pct": 0}


def emit_telemetry_event(
    event_type: str,
    module_id: int | None = None,
    sheet: str | None = None,
    status: str | None = None,
    duration: float | None = None,
    metadata: dict | None = None,
) -> None:
    """Emits an atomic machine-readable JSONL audit record to Data/telemetry/pipeline_events.jsonl."""
    ram = get_system_ram_telemetry()
    payload = {
        "timestamp": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "event": event_type,
        "module_id": module_id,
        "sheet": sheet,
        "status": status,
        "duration_sec": round(duration, 3) if duration is not None else None,
        "ram": ram,
        "metadata": metadata or {},
    }
    try:
        with open(TELEMETRY_FILE, "a", encoding="utf-8") as f:
            f.write(json.dumps(payload) + "\n")
    except Exception as e:
        sys.stderr.write(f"[Telemetry Error] Failed to write event: {e}\n")


def setup_institutional_logger(name: str, log_file: pathlib.Path | str | None = None) -> logging.Logger:
    """
    Sets up a hardened logger with dual handlers:
    1. Standard Output handler (formatted for console).
    2. 50 MB Rotating File Handler (retained across runs in logs/excel_pipeline.log).
    """
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    # Avoid duplicate handlers if already configured
    if logger.handlers:
        return logger

    formatter = logging.Formatter(
        fmt="%(asctime)s [%(levelname)s] [%(name)s] %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    # 1. Console handler
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    # 2. Rotating file handler
    target_log_file = pathlib.Path(log_file) if log_file else DEFAULT_LOG_FILE
    target_log_file.parent.mkdir(parents=True, exist_ok=True)
    try:
        file_handler = RotatingFileHandler(
            filename=str(target_log_file),
            maxBytes=50 * 1024 * 1024,  # 50 MB
            backupCount=5,
            encoding="utf-8",
        )
        file_handler.setLevel(logging.INFO)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
    except Exception as e:
        sys.stderr.write(f"[Logger Setup Warning] Could not initialize file handler for {target_log_file}: {e}\n")

    logger.propagate = False
    return logger
