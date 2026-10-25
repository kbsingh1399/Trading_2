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

ROOT = pathlib.Path(__file__).resolve().parents[2]
TELEMETRY_FILE = ROOT / "Data" / "telemetry" / "pipeline_events.jsonl"
DEFAULT_LOG_FILE = ROOT / "logs" / "pipeline.log"


def get_system_ram_telemetry() -> dict:
    """Queries Windows Kernel32 GlobalMemoryStatusEx for real-time physical RAM usage."""
    try:
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
        stat = MEMORYSTATUSEX()
        stat.dwLength = ctypes.sizeof(MEMORYSTATUSEX)
        if ctypes.windll.kernel32.GlobalMemoryStatusEx(ctypes.byref(stat)):
            total_mb = stat.ullTotalPhys / (1024 * 1024)
            avail_mb = stat.ullAvailPhys / (1024 * 1024)
            used_mb = total_mb - avail_mb
            return {
                "used_mb": round(used_mb, 1),
                "avail_mb": round(avail_mb, 1),
                "total_mb": round(total_mb, 1),
                "load_pct": int(stat.dwMemoryLoad),
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
        TELEMETRY_FILE.parent.mkdir(parents=True, exist_ok=True)
        with open(TELEMETRY_FILE, "a", encoding="utf-8") as f:
            f.write(json.dumps(payload) + "\n")
    except Exception as e:
        sys.stderr.write(f"[Telemetry Error] Failed to write event: {e}\n")


def setup_institutional_logger(name: str, log_file: pathlib.Path | str | None = None) -> logging.Logger:
    """Sets up a hardened logger with dual handlers."""
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    if logger.handlers:
        return logger

    formatter = logging.Formatter(
        fmt="%(asctime)s [%(levelname)s] [%(name)s] %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    target_log_file = pathlib.Path(log_file) if log_file else DEFAULT_LOG_FILE
    target_log_file.parent.mkdir(parents=True, exist_ok=True)
    try:
        file_handler = RotatingFileHandler(
            filename=str(target_log_file),
            maxBytes=50 * 1024 * 1024,
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


IST_TIMEZONE = datetime.timezone(datetime.timedelta(hours=5, minutes=30))
UTC_TIMEZONE = datetime.timezone.utc


def get_current_timestamps() -> tuple[str, str]:
    """Returns current timestamps formatted in IST (UTC+5:30) and UTC."""
    now_utc = datetime.datetime.now(UTC_TIMEZONE)
    now_ist = datetime.datetime.now(IST_TIMEZONE)
    ist_str = now_ist.strftime("%Y-%m-%d %H:%M:%S IST")
    utc_str = now_utc.strftime("%Y-%m-%d %H:%M:%S UTC")
    return ist_str, utc_str


def stamp_sheet_completion_ist(
    ws=None,
    sheet_title: str = "",
    row_count: int = 0,
    banner_cell: str = "A1",
    status: str = "LIVE",
    merge_max_col: int | None = None
) -> bool:
    """Legacy compatibility stub for sheet banner stamping."""
    return True
