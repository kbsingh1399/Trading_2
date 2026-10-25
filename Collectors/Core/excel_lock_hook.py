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
    import filelock
    _OrigFileLock = filelock.FileLock
except ImportError:
    _OrigFileLock = None

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
        self.fl = _OrigFileLock(lock_path, timeout=timeout) if _OrigFileLock else None

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


# Globally patch filelock.FileLock so every module gets re-entrant locking automatically
if _OrigFileLock is not None:
    filelock.FileLock = ReentrantFileLock
    FileLock = ReentrantFileLock
else:
    FileLock = None


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


def _dump_workbook_sheets_to_parquet(wb):
    """Automatically extracts sheets from in-memory openpyxl workbook and dumps to Parquet."""
    try:
        import sys, datetime
        df_dir = ROOT / "Terminal" / "Data_Factory"
        if str(df_dir) not in sys.path:
            sys.path.insert(0, str(df_dir))
        from parquet_feed_writer import write_parquet_feed

        PURE_API_FEEDS = {
            "Crypto_ETF_Flows", "Top_Institutions", "ETF_Market_Overview",
            "2_Spot_Netflow_S",
            "3_Exchanges_LS_Ratio_15M", "3_Exchanges_LS_Ratio_1H", "3_Exchanges_LS_Ratio_4H",
            "5_Funding_Rate", "5_OI"
        }
        for sheet_name in wb.sheetnames:
            if sheet_name in PURE_API_FEEDS:
                continue
            ws = wb[sheet_name]
            rows = list(ws.iter_rows(values_only=True))
            if not rows or len(rows) < 2:
                continue

            header_idx = 0
            for i in range(min(5, len(rows))):
                non_empty = [c for c in rows[i] if c is not None]
                if len(non_empty) >= 2 and all(isinstance(c, str) for c in non_empty[:3]):
                    header_idx = i
                    break

            raw_headers = rows[header_idx]
            headers = []
            for col_idx, h in enumerate(raw_headers):
                if h is not None and str(h).strip():
                    h_clean = str(h).strip().replace(" ", "_").replace("(", "").replace(")", "").replace("/", "_")
                    headers.append((col_idx, h_clean))
                elif col_idx < 15:
                    headers.append((col_idx, f"col_{col_idx}"))

            data_rows = []
            for r in rows[header_idx + 1:]:
                if not any(c is not None for c in r):
                    continue
                row_dict = {}
                for col_idx, col_name in headers:
                    val = r[col_idx] if col_idx < len(r) else None
                    if isinstance(val, (datetime.datetime, datetime.date)):
                        val = str(val)
                    elif val is not None and not isinstance(val, (int, float, bool, str)):
                        val = str(val)
                    row_dict[col_name] = val
                data_rows.append(row_dict)

            if data_rows:
                write_parquet_feed(sheet_name, data_rows)
    except Exception:
        pass


def locked_workbook_save(self, filename, *args, **kwargs):
    """Acquires lock ONLY when saving directly to master DataBase_Trading.xlsx (not unique tmp files)."""
    # 1. Dual-write to individual high-speed Parquet feed
    _dump_workbook_sheets_to_parquet(self)

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
