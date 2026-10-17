"""
System Memory & Resource Optimization Engine
Institutional RAM monitor, Working Set Trimmer, Standby Cache Purger.
Zero-external-dependency Win32 Ctypes & PowerShell execution.
"""

import ctypes
from ctypes import wintypes
import gc
import logging
import os
import subprocess
from pathlib import Path
from typing import Dict, Any

logger = logging.getLogger("MemoryOptimizer")

ROOT = Path(__file__).resolve().parent.parent.parent
FREE_RAM_SCRIPT = ROOT / ".agents" / "scripts" / "free_ram.ps1"


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


def get_system_memory_status() -> Dict[str, Any]:
    """Retrieve exact physical and virtual memory statistics via Windows API."""
    try:
        stat = MEMORYSTATUSEX()
        stat.dwLength = ctypes.sizeof(MEMORYSTATUSEX)
        kernel32 = ctypes.WinDLL("kernel32", use_last_error=True)
        if kernel32.GlobalMemoryStatusEx(ctypes.byref(stat)):
            total_gb = stat.ullTotalPhys / (1024**3)
            avail_gb = stat.ullAvailPhys / (1024**3)
            used_gb = total_gb - avail_gb
            return {
                "memory_load_pct": int(stat.dwMemoryLoad),
                "total_phys_gb": round(total_gb, 2),
                "used_phys_gb": round(used_gb, 2),
                "avail_phys_gb": round(avail_gb, 2),
            }
    except Exception as exc:
        logger.warning("Failed querying GlobalMemoryStatusEx: %s", exc)
    return {
        "memory_load_pct": -1,
        "total_phys_gb": 0.0,
        "used_phys_gb": 0.0,
        "avail_phys_gb": 0.0,
    }


def trim_current_process_working_set() -> bool:
    """Trim working set of current Python process to flush pages to standby pool."""
    try:
        gc.collect()
        kernel32 = ctypes.WinDLL("kernel32", use_last_error=True)
        psapi = ctypes.WinDLL("psapi", use_last_error=True)
        kernel32.GetCurrentProcess.restype = wintypes.HANDLE
        psapi.EmptyWorkingSet.argtypes = [wintypes.HANDLE]
        psapi.EmptyWorkingSet.restype = wintypes.BOOL

        handle = kernel32.GetCurrentProcess()
        return bool(psapi.EmptyWorkingSet(handle))
    except Exception as exc:
        logger.warning("Failed trimming current process working set: %s", exc)
        return False


def optimize_ram(threshold_pct: int = 75, force: bool = False) -> Dict[str, Any]:
    """
    Perform multi-tier RAM optimization:
    Tier 1: In-process GC and working set trimming.
    Tier 2: If memory load >= threshold_pct or force=True, execute free_ram.ps1 system-wide.
    """
    initial_stats = get_system_memory_status()
    trim_current_process_working_set()

    triggered_system_cleanup = False
    system_cleanup_output = ""

    if (initial_stats["memory_load_pct"] >= threshold_pct or force) and FREE_RAM_SCRIPT.exists():
        try:
            logger.info(
                "Memory load at %d%% (threshold: %d%%). Triggering system-wide RAM cleanup...",
                initial_stats["memory_load_pct"],
                threshold_pct,
            )
            res = subprocess.run(
                ["powershell", "-ExecutionPolicy", "Bypass", "-File", str(FREE_RAM_SCRIPT)],
                capture_output=True,
                text=True,
                timeout=30,
            )
            triggered_system_cleanup = True
            system_cleanup_output = res.stdout.strip()
            logger.info("System-wide RAM optimization executed: exit_code=%d", res.returncode)
        except Exception as exc:
            logger.warning("Failed executing free_ram.ps1: %s", exc)

    final_stats = get_system_memory_status()
    return {
        "initial": initial_stats,
        "final": final_stats,
        "freed_gb": round(max(0.0, final_stats["avail_phys_gb"] - initial_stats["avail_phys_gb"]), 2),
        "triggered_system_cleanup": triggered_system_cleanup,
        "system_cleanup_output": system_cleanup_output,
    }


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    res = optimize_ram(threshold_pct=70)
    print(res)
