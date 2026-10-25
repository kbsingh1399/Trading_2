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

import os
import pathlib
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


def locked_load_workbook(filename, *args, **kwargs):
    """Loads workbook safely with retry on transient write collisions."""
    is_target = "DataBase_Trading.xlsx" in str(filename)
    if not is_target or FileLock is None:
        return _orig_load_workbook(filename, *args, **kwargs)

    for attempt in range(10):
        try:
            return _orig_load_workbook(filename, *args, **kwargs)
        except (EOFError, PermissionError, OSError, Exception) as e:
            if "not a zip file" in str(e).lower() or isinstance(e, (EOFError, PermissionError)):
                if attempt == 9:
                    try:
                        with FileLock(str(LOCK_PATH), timeout=30):
                            return _orig_load_workbook(filename, *args, **kwargs)
                    except Exception:
                        raise e
                time.sleep(0.2 * (attempt + 1))
            else:
                raise


def locked_workbook_save(self, filename, *args, **kwargs):
    """Acquires lock ONLY when saving directly to master DataBase_Trading.xlsx (not unique tmp files)."""
    fn_str = str(filename)
    is_exact_master = ("DataBase_Trading.xlsx" in fn_str) and (".tmp." not in fn_str)
    if is_exact_master and FileLock is not None:
        with FileLock(str(LOCK_PATH), timeout=120):
            return _orig_workbook_save(self, filename, *args, **kwargs)
    return _orig_workbook_save(self, filename, *args, **kwargs)


def locked_os_replace(src, dst, *args, **kwargs):
    """Acquires lock before replacing DataBase_Trading.xlsx (held for ~50ms atomic rename)."""
    is_target = "DataBase_Trading.xlsx" in str(dst)
    if is_target and FileLock is not None:
        with FileLock(str(LOCK_PATH), timeout=120):
            for attempt in range(40):
                try:
                    return _orig_os_replace(src, dst, *args, **kwargs)
                except (PermissionError, OSError):
                    if attempt == 39:
                        raise
                    time.sleep(0.1 * (attempt + 1))
    return _orig_os_replace(src, dst, *args, **kwargs)


def locked_path_replace(self, target, *args, **kwargs):
    """Acquires lock before pathlib.Path.replace into DataBase_Trading.xlsx."""
    is_target = "DataBase_Trading.xlsx" in str(target)
    if is_target and FileLock is not None:
        with FileLock(str(LOCK_PATH), timeout=120):
            for attempt in range(40):
                try:
                    return _orig_path_replace(self, target, *args, **kwargs)
                except (PermissionError, OSError):
                    if attempt == 39:
                        raise
                    time.sleep(0.1 * (attempt + 1))
    return _orig_path_replace(self, target, *args, **kwargs)


# Apply hooks globally
openpyxl.load_workbook = locked_load_workbook
openpyxl.Workbook.save = locked_workbook_save
os.replace = locked_os_replace
pathlib.Path.replace = locked_path_replace
