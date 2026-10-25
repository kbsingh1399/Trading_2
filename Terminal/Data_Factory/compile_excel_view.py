#!/usr/bin/env python3
"""
Terminal/Data_Factory/compile_excel_view.py
==========================================
On-Demand Excel View Compiler.
Reads all 33 production Parquet feeds from Data/feeds/ and compiles them
into Data/DataBase_Trading.xlsx (or Data/views/DataBase_Trading.xlsx) in a single,
fast serial commit without holding any pipeline locks.
"""

from __future__ import annotations

import datetime
import logging
import os
import pathlib
import sys
import time

ROOT_DIR = pathlib.Path(__file__).resolve().parents[2]
DATA_DIR = ROOT_DIR / "Data"
FEEDS_DIR = DATA_DIR / "feeds"
METADATA_DIR = DATA_DIR / "metadata"
TARGET_EXCEL = DATA_DIR / "DataBase_Trading.xlsx"

DATA_FACTORY_DIR = ROOT_DIR / "Terminal" / "Data_Factory"
if str(DATA_FACTORY_DIR) not in sys.path:
    sys.path.insert(0, str(DATA_FACTORY_DIR))

from parquet_feed_writer import read_parquet_feed, get_parquet_feed_metadata
from parquet_feed_checklist_auditor import CANONICAL_FEEDS

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
log = logging.getLogger("ExcelCompiler")


def compile_excel():
    import openpyxl
    from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
    from openpyxl.utils import get_column_letter

    t0 = time.perf_counter()
    log.info("Compiling on-demand Excel workbook from 33 Parquet feeds...")

    wb = openpyxl.Workbook()
    # Remove default sheet
    wb.remove(wb.active)

    font_banner = Font(name="Calibri", size=10, bold=True, color="FFFFFF")
    fill_banner = PatternFill(start_color="1B365D", end_color="1B365D", fill_type="solid")
    font_header = Font(name="Calibri", size=10, bold=True, color="FFFFFF")
    fill_header = PatternFill(start_color="2C3E50", end_color="2C3E50", fill_type="solid")
    font_data = Font(name="Calibri", size=9)

    compiled_count = 0

    for feed_info in CANONICAL_FEEDS:
        feed_name = feed_info["name"]
        parquet_path = FEEDS_DIR / f"{feed_name}.parquet"
        if not parquet_path.exists():
            continue

        try:
            tbl = read_parquet_feed(feed_name)
            meta = get_parquet_feed_metadata(feed_name) or {}
            ws = wb.create_sheet(title=feed_name[:31])  # Excel 31-char limit

            # Row 1: Title
            ws.cell(row=1, column=1, value=feed_name)
            ws.cell(row=1, column=1).font = Font(name="Calibri", size=12, bold=True)

            # Row 2: Banner
            banner_text = f"{feed_name} | LAST UPDATED: {meta.get('timestamp_ist', 'N/A')} | ROWS: {tbl.num_rows} | STATUS: LIVE"
            ws.merge_cells(start_row=2, start_column=1, end_row=2, end_column=max(5, tbl.num_columns))
            b_cell = ws.cell(row=2, column=1, value=banner_text)
            b_cell.font = font_banner
            b_cell.fill = fill_banner
            b_cell.alignment = Alignment(horizontal="center", vertical="center")

            # Row 3: Headers
            col_names = tbl.column_names
            for col_i, col_name in enumerate(col_names, start=1):
                c = ws.cell(row=3, column=col_i, value=col_name)
                c.font = font_header
                c.fill = fill_header

            # Data rows (max 500 for fast preview)
            pydict = tbl.slice(0, min(500, tbl.num_rows)).to_pydict()
            num_rows = min(500, tbl.num_rows)
            for row_i in range(num_rows):
                for col_i, col_name in enumerate(col_names, start=1):
                    val = pydict[col_name][row_i]
                    if val is not None:
                        ws.cell(row=4 + row_i, column=col_i, value=str(val) if not isinstance(val, (int, float, bool)) else val).font = font_data

            compiled_count += 1
        except Exception as e:
            log.warning(f"Error compiling sheet for {feed_name}: {e}")

    # Atomic write to DataBase_Trading.xlsx
    tmp_path = TARGET_EXCEL.with_name(f"DataBase_Trading_{os.getpid()}_{int(time.time()*1000)}.tmp.xlsx")
    wb.save(tmp_path)
    wb.close()
    os.replace(tmp_path, TARGET_EXCEL)

    duration = time.perf_counter() - t0
    log.info(f"Compiled {compiled_count} sheets into {TARGET_EXCEL} in {duration:.2f}s.")


if __name__ == "__main__":
    compile_excel()
