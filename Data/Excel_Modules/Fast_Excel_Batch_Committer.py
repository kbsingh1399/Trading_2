"""
Fast Excel Batch Committer (Tier 2 Consumer)
Eliminates repetitive multi-minute workbook open/save overhead.
Loads Data/DataBase_Trading.xlsx ONCE, applies all fresh staged dataframes from
Data/staging/*.parquet across all 29 target sheets, and performs a SINGLE atomic commit.
"""

from __future__ import annotations

import argparse
import datetime
import os
import pathlib
import sys
import time
import openpyxl
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
from openpyxl.utils import get_column_letter
import pandas as pd

from logger_config import emit_telemetry_event, get_system_ram_telemetry, setup_institutional_logger

MODULES_DIR = pathlib.Path(__file__).resolve().parent
ROOT_DIR = MODULES_DIR.parents[1]
EXCEL_PATH = ROOT_DIR / "Data" / "DataBase_Trading.xlsx"
STAGING_DIR = ROOT_DIR / "Data" / "staging"
STAGING_DIR.mkdir(parents=True, exist_ok=True)

log = setup_institutional_logger("BatchCommitter")

# Canonical 29-Sheet Ordered Layout
CANONICAL_ORDER = [
    "Crypto_ETF_Flows",
    "1_Crypto_ETF_Flows",
    "2_Spot_Netflow_S",
    "3_Exchanges_LS_Ratio_15M",
    "3_Exchanges_LS_Ratio_1H",
    "3_Exchanges_LS_Ratio_4H",
    "4_Hyperliquid_Analysis",
    "5_OI",
    "5_Funding_Rate",
    "6_Funding_Fee_Settlement",
    "7_Liq_Heapmap",
    "7_Live_Liq",
    "8_Exchange_Liquidation_Map_1D",
    "8_Exchange_Liquidation_Map_7D",
    "9_Liquidation_Max_Pain_24H",
    "9_Liquidation_Max_Pain_48H",
    "9_Liquidation_Max_Pain_3D",
    "9_Liquidation_Max_Pain_7D",
    "10_Whale_Orders",
    "11_Technical",
    "12_Hyperdash",
    "13_Hyperliquid",
    "14_Hyperdash_Liq_Map",
    "15_Hyperdash_Stops_Map",
    "16_Hyperdash_telegram_Intel",
    "17_Orderbook",
    "18_CVD",
    "19_News",
    "19_Calendar",
    "20_Auction_Market_Structure",
]

# Styles
HEADER_FILL = PatternFill(start_color="1B365D", end_color="1B365D", fill_type="solid")
HEADER_FONT = Font(name="Segoe UI", size=10, bold=True, color="FFFFFF")
ZEBRA_FILL = PatternFill(start_color="F9FAFB", end_color="F9FAFB", fill_type="solid")
DEFAULT_FONT = Font(name="Segoe UI", size=9)
THIN_BORDER = Border(
    left=Side(style="thin", color="E5E7EB"),
    right=Side(style="thin", color="E5E7EB"),
    top=Side(style="thin", color="E5E7EB"),
    bottom=Side(style="thin", color="E5E7EB"),
)


def style_worksheet(ws: openpyxl.worksheet.worksheet.Worksheet, max_col: int, max_row: int) -> None:
    """Applies institutional header styling, alternating rows, freeze panes, and auto-filters."""
    ws.views.sheetView[0].showGridLines = True
    ws.freeze_panes = "A2"

    for col in range(1, max_col + 1):
        cell = ws.cell(row=1, column=col)
        cell.fill = HEADER_FILL
        cell.font = HEADER_FONT
        cell.alignment = Alignment(horizontal="center", vertical="center", wrap_text=False)
        cell.border = THIN_BORDER

    for row in range(2, max_row + 1):
        is_even = (row % 2 == 0)
        for col in range(1, max_col + 1):
            cell = ws.cell(row=row, column=col)
            cell.font = DEFAULT_FONT
            cell.border = THIN_BORDER
            if is_even:
                cell.fill = ZEBRA_FILL

    # Auto column widths
    for col in range(1, max_col + 1):
        col_letter = get_column_letter(col)
        max_len = 0
        for r in range(1, min(max_row + 1, 50)):
            val = ws.cell(row=r, column=col).value
            if val is not None:
                max_len = max(max_len, len(str(val)))
        ws.column_dimensions[col_letter].width = max(max_len + 3, 12)

    if max_row > 1 and max_col > 0:
        ws.auto_filter.ref = f"A1:{get_column_letter(max_col)}{max_row}"


def commit_staged_sheets(staging_dir: pathlib.Path = STAGING_DIR, excel_path: pathlib.Path = EXCEL_PATH) -> dict:
    """
    Scans staging directory, loads workbook once, updates all modified sheets,
    ensures canonical order, and saves workbook in a single atomic pass.
    """
    parquet_files = list(staging_dir.glob("*.parquet"))
    if not parquet_files:
        log.info("[BatchCommitter] No staged .parquet files found to commit.")
        return {"updated": 0, "duration": 0.0}

    log.info(f"[BatchCommitter] Found {len(parquet_files)} staged datasets to flush into {excel_path.name}...")
    t0 = time.perf_counter()

    if not excel_path.exists():
        wb = openpyxl.Workbook()
        wb.remove(wb.active)
    else:
        wb = openpyxl.load_workbook(excel_path)

    load_time = time.perf_counter() - t0
    log.info(f"[BatchCommitter] Workbook loaded in {load_time:.2f}s. Existing sheets: {len(wb.sheetnames)}")

    updated_count = 0
    updated_sheets = []

    for pq_path in parquet_files:
        sheet_name = pq_path.stem
        try:
            df = pd.read_parquet(pq_path)
            if df.empty:
                continue

            if sheet_name in wb.sheetnames:
                ws = wb[sheet_name]
                ws.delete_rows(1, ws.max_row + 1)
            else:
                ws = wb.create_sheet(title=sheet_name)

            headers = list(df.columns)
            ws.append(headers)

            for row in df.itertuples(index=False, name=None):
                clean_row = ["" if pd.isna(v) else v for v in row]
                ws.append(clean_row)

            style_worksheet(ws, len(headers), len(df) + 1)
            updated_count += 1
            updated_sheets.append((sheet_name, len(df)))
            log.info(f"  -> Sheet '{sheet_name}': Flushed {len(df)} rows.")

        except Exception as e:
            log.error(f"[BatchCommitter] Error writing sheet '{sheet_name}': {e}")

    # Reorder sheets to canonical order
    current_sheets = [s for s in wb.sheetnames]
    ordered_sheets = [s for s in CANONICAL_ORDER if s in current_sheets]
    trailing_sheets = [s for s in current_sheets if s not in CANONICAL_ORDER]
    final_order = ordered_sheets + trailing_sheets

    wb._sheets = [wb[name] for name in final_order]

    t_save = time.perf_counter()
    log.info(f"[BatchCommitter] Saving {len(wb.sheetnames)} sheets to {excel_path}...")
    wb.save(excel_path)
    save_time = time.perf_counter() - t_save
    total_time = time.perf_counter() - t0

    log.info(f"[BatchCommitter] [SUCCESS] Committed {updated_count} sheets in {total_time:.2f}s (Save IO: {save_time:.2f}s).")
    emit_telemetry_event(
        event_type="BATCH_EXCEL_COMMIT",
        status="PASS",
        duration=total_time,
        metadata={"sheets_updated": updated_count, "save_io_sec": round(save_time, 2)},
    )

    return {
        "updated": updated_count,
        "sheets": updated_sheets,
        "total_duration": total_time,
        "save_duration": save_time,
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Fast Excel Batch Committer")
    parser.add_argument("--staging-dir", default=str(STAGING_DIR), help="Path to staging directory")
    parser.add_argument("--excel-path", default=str(EXCEL_PATH), help="Target Excel workbook")
    args = parser.parse_args()

    commit_staged_sheets(pathlib.Path(args.staging_dir), pathlib.Path(args.excel_path))
