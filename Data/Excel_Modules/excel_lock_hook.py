#!/usr/bin/env python3
"""
Data/Excel_Modules/excel_lock_hook.py
======================================
High-performance cross-process FileLock hook for openpyxl operations on Data/DataBase_Trading.xlsx.
Serializes openpyxl.Workbook.save calls with an exclusive file lock (~0.8s hold time).
Allows concurrent read_only loads with automatic retry on transient write collisions.
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


def locked_load_workbook(filename, *args, **kwargs):
    """Loads workbook safely with retry on transient write collisions."""
    is_target = "DataBase_Trading.xlsx" in str(filename)
    if not is_target or FileLock is None:
        return _orig_load_workbook(filename, *args, **kwargs)

    # For read operations, attempt direct read with fast retry backoff
    for attempt in range(6):
        try:
            return _orig_load_workbook(filename, *args, **kwargs)
        except (EOFError, PermissionError, OSError, Exception) as e:
            if "not a zip file" in str(e).lower() or isinstance(e, (EOFError, PermissionError)):
                if attempt == 5:
                    # Final attempt: wait on lock
                    try:
                        with FileLock(str(LOCK_PATH), timeout=15):
                            return _orig_load_workbook(filename, *args, **kwargs)
                    except Exception:
                        raise e
                time.sleep(0.3 * (attempt + 1))
            else:
                raise


def locked_workbook_save(self, filename, *args, **kwargs):
    """Acquires exclusive lock before saving workbook to eliminate zipfile corruptions."""
    is_target = "DataBase_Trading.xlsx" in str(filename)
    if is_target and FileLock is not None:
        lock = FileLock(str(LOCK_PATH), timeout=30)
        with lock:
            return _orig_workbook_save(self, filename, *args, **kwargs)
    return _orig_workbook_save(self, filename, *args, **kwargs)


# Monkey-patch openpyxl globally in current Python process
openpyxl.load_workbook = locked_load_workbook
openpyxl.Workbook.save = locked_workbook_save
