#!/usr/bin/env python3
"""
Data/Excel_Modules/excel_lock_hook.py
======================================
Global cross-process and cross-thread FileLock hook for openpyxl operations on Data/DataBase_Trading.xlsx.
Intercepts `openpyxl.load_workbook` and `openpyxl.Workbook.save` to serialize all Excel read/write
operations across parallel browser CDP harvesters, API workers, and streaming daemons.
Prevents zipfile EOFError and Windows file-sharing collisions.
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
    """Acquires lock before loading workbook if targeting DataBase_Trading.xlsx."""
    is_target = "DataBase_Trading.xlsx" in str(filename)
    if is_target and FileLock is not None:
        lock = FileLock(str(LOCK_PATH), timeout=120)
        # For read_only loads, retry on transient read collisions
        for attempt in range(5):
            try:
                with lock:
                    return _orig_load_workbook(filename, *args, **kwargs)
            except (EOFError, PermissionError, OSError) as e:
                if attempt == 4:
                    raise
                time.sleep(0.5 * (attempt + 1))
    return _orig_load_workbook(filename, *args, **kwargs)


def locked_workbook_save(self, filename, *args, **kwargs):
    """Acquires lock before saving workbook if targeting DataBase_Trading.xlsx."""
    is_target = "DataBase_Trading.xlsx" in str(filename)
    if is_target and FileLock is not None:
        lock = FileLock(str(LOCK_PATH), timeout=120)
        with lock:
            return _orig_workbook_save(self, filename, *args, **kwargs)
    return _orig_workbook_save(self, filename, *args, **kwargs)


# Monkey-patch openpyxl globally in current Python process
openpyxl.load_workbook = locked_load_workbook
openpyxl.Workbook.save = locked_workbook_save
