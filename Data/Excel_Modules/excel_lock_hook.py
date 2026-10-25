#!/usr/bin/env python3
"""
Data/Excel_Modules/excel_lock_hook.py
======================================
High-performance non-blocking cross-process FileLock hook for Data/DataBase_Trading.xlsx.
Architectural Design:
  1. Temporary file saves (*.tmp.xlsx) run 100% concurrently without lock contention.
  2. Direct saves to DataBase_Trading.xlsx acquire FileLock.
  3. Atomic replacement (os.replace / Path.replace) acquires FileLock for only ~50ms NTFS rename.
  4. load_workbook allows concurrent readers with fast retry on transient replace collisions.
"""

import io
import os
import pathlib
import threading
import time
import openpyxl

try:
    from filelock import FileLock
except ImportError:
    FileLock = None

ROOT = pathlib.Path(__file__).resolve().parents[2]
DATA_DIR = ROOT / "Data"
EXCEL_PATH = DATA_DIR / "DataBase_Trading.xlsx"
LOCK_PATH = DATA_DIR / "DataBase_Trading.xlsx.lock"

_orig_load_workbook = openpyxl.load_workbook
_orig_workbook_save = openpyxl.Workbook.save
_orig_os_replace = os.replace
_orig_path_replace = pathlib.Path.replace

_tls = threading.local()


class ReentrantFileLock:
    """Process-level re-entrant wrapper around filelock on Windows to prevent self-deadlocks."""
    def __init__(self, lock_path: str, timeout: float = 60.0):
        self.lock_path = lock_path
        self.timeout = timeout
        self.fl = FileLock(lock_path, timeout=timeout) if FileLock else None

    def __enter__(self):
        depth = getattr(_tls, "depth", 0)
        if depth == 0 and self.fl is not None:
            self.fl.acquire(timeout=self.timeout)
        _tls.depth = depth + 1
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        depth = getattr(_tls, "depth", 1) - 1
        _tls.depth = depth
        if depth == 0 and self.fl is not None:
            try:
                self.fl.release()
            except Exception:
                pass


def get_lock(timeout=60.0):
    return ReentrantFileLock(str(LOCK_PATH), timeout=timeout)


def locked_load_workbook(filename, *args, **kwargs):
    """Loads workbook from in-memory BytesIO so Windows file handle is never kept open."""
    fn_str = str(filename)
    is_target = "DataBase_Trading.xlsx" in fn_str and (".tmp." not in fn_str)
    if not is_target:
        return _orig_load_workbook(filename, *args, **kwargs)

    # Read binary bytes into BytesIO under FileLock (held for ~5ms), releasing handle immediately
    for attempt in range(15):
        try:
            with get_lock(timeout=30.0):
                with open(filename, "rb") as f:
                    data = io.BytesIO(f.read())
            return _orig_load_workbook(data, *args, **kwargs)
        except (PermissionError, OSError, EOFError, Exception) as e:
            if attempt == 14:
                raise
            time.sleep(0.1 * (attempt + 1))


def locked_workbook_save(self, filename, *args, **kwargs):
    """Acquires lock ONLY when saving directly to master DataBase_Trading.xlsx (not unique tmp files)."""
    fn_str = str(filename)
    is_exact_master = ("DataBase_Trading.xlsx" in fn_str) and (".tmp." not in fn_str)
    if is_exact_master and FileLock is not None:
        with get_lock(timeout=60.0):
            return _orig_workbook_save(self, filename, *args, **kwargs)
    return _orig_workbook_save(self, filename, *args, **kwargs)


def locked_os_replace(src, dst, *args, **kwargs):
    """Acquires lock before replacing DataBase_Trading.xlsx (held for ~5ms atomic rename)."""
    is_target = "DataBase_Trading.xlsx" in str(dst)
    if is_target and FileLock is not None:
        with get_lock(timeout=60.0):
            for attempt in range(25):
                try:
                    return _orig_os_replace(src, dst, *args, **kwargs)
                except (PermissionError, OSError):
                    if attempt == 24:
                        raise
                    time.sleep(0.05 * (attempt + 1))
    return _orig_os_replace(src, dst, *args, **kwargs)


def locked_path_replace(self, target, *args, **kwargs):
    """Acquires lock before pathlib.Path.replace into DataBase_Trading.xlsx."""
    is_target = "DataBase_Trading.xlsx" in str(target)
    if is_target and FileLock is not None:
        with get_lock(timeout=60.0):
            for attempt in range(25):
                try:
                    return _orig_path_replace(self, target, *args, **kwargs)
                except (PermissionError, OSError):
                    if attempt == 24:
                        raise
                    time.sleep(0.05 * (attempt + 1))
    return _orig_path_replace(self, target, *args, **kwargs)


# Apply hooks globally
openpyxl.load_workbook = locked_load_workbook
openpyxl.Workbook.save = locked_workbook_save
os.replace = locked_os_replace
pathlib.Path.replace = locked_path_replace
