#!/usr/bin/env python3
"""
Data/Excel_Modules/7_Liq_Heapmap.py
==================================
Live CoinGlass Liquidation Heatmap Multi-Timeframe Scraper & Excel Dumper.
Captures the Liquidation Heatmap across all 4 timeframes (1h, 4h, 12h, 24h)
from https://www.coinglass.com/liquidations and formats into worksheet '7_Liq_Heapmap'
in Data/DataBase_Trading.xlsx (positioned at Index 9, immediately after '6_Funding_Fee_Settlement').

Layout Matches Operator Sketch:
  Rank | Asset | 1hour | 4hour | 12 hour | 24hour | Timestamp (UTC)

Security & Cleanliness Invariants:
  - Ephemeral CDP tab on port 9222 opened and strictly closed in finally: block.
  - Preserves arena.ai tab untouched.
  - Zero external browser window pollution.
"""

from __future__ import annotations

import argparse
import asyncio
import datetime
import json
import logging
import pathlib
import re
import sys
import time
import urllib.request

try:
    import openpyxl
    from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
    from openpyxl.utils import get_column_letter
except ImportError:
    openpyxl = None

try:
    import websockets
except ImportError:
    websockets = None

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] [%(name)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
log = logging.getLogger("7_Liq_Heapmap")

MODULES_DIR = pathlib.Path(__file__).resolve().parent
ROOT_DIR = MODULES_DIR.parents[1]
DEFAULT_EXCEL_PATH = ROOT_DIR / "Data" / "DataBase_Trading.xlsx"
CDP_BASE_URL = "http://127.0.0.1:9222"
TARGET_URL = "https://www.coinglass.com/liquidations"
SHEET_NAME = "7_Liq_Heapmap"

COLUMNS_DEF = [
    ("rank", "Rank", 10, "center"),
    ("asset", "Asset", 16, "center"),
    ("tf_1h", "1hour", 18, "right"),
    ("tf_4h", "4hour", 18, "right"),
    ("tf_12h", "12 hour", 18, "right"),
    ("tf_24h", "24hour", 18, "right"),
    ("timestamp_utc", "Timestamp (UTC)", 24, "center"),
]


def parse_numeric_value(val_str: str) -> float:
    """Parses strings like '$111.27M', '$653.30K', '$1.2B' into float values for ranking."""
    if not val_str:
        return 0.0
    cleaned = val_str.replace("$", "").replace(",", "").strip()
    mult = 1.0
    if cleaned.endswith("B"):
        mult = 1e9
        cleaned = cleaned[:-1]
    elif cleaned.endswith("M"):
        mult = 1e6
        cleaned = cleaned[:-1]
    elif cleaned.endswith("K"):
        mult = 1e3
        cleaned = cleaned[:-1]
    try:
        return float(cleaned) * mult
    except ValueError:
        return 0.0


def open_ephemeral_tab() -> tuple[str, str]:
    """Creates a new dedicated ephemeral tab via CDP."""
    req = urllib.request.Request(f"{CDP_BASE_URL}/json/new?{TARGET_URL}", method="PUT")
    new_tab = json.loads(urllib.request.urlopen(req, timeout=10).read().decode())
    return new_tab["id"], new_tab["webSocketDebuggerUrl"]


def close_tab(tab_id: str):
    """Closes tab via CDP."""
    try:
        urllib.request.urlopen(f"{CDP_BASE_URL}/json/close/{tab_id}", timeout=4)
        log.info(f"Closed ephemeral tab {tab_id}")
    except Exception as e:
        log.warning(f"Error closing tab {tab_id}: {e}")


async def harvest_liquidation_heatmap() -> list[dict]:
    """Navigates to CoinGlass Liquidations, clicks 1h, 4h, 12h, 24h tabs, and extracts all tiles."""
    if not websockets:
        raise RuntimeError("websockets package is required.")

    tab_id, ws_url = open_ephemeral_tab()
    log.info(f"Opened dedicated ephemeral tab (ID: {tab_id}) for Heatmap harvest.")

    now_dt = datetime.datetime.now(datetime.timezone.utc)
    ts_str = now_dt.strftime("%Y-%m-%d %H:%M:%S UTC")

    timeframes = ["1h", "4h", "12h", "24h"]
    tf_data: dict[str, dict[str, str]] = {tf: {} for tf in timeframes}

    try:
        ws = None
        for attempt in range(10):
            try:
                ws = await websockets.connect(ws_url, max_size=25 * 1024 * 1024, open_timeout=15)
                break
            except Exception as e:
                log.warning(f"WebSocket connect attempt {attempt+1} failed: {e}. Retrying in 1s...")
                await asyncio.sleep(1)

        if not ws:
            raise RuntimeError(f"Could not connect to CDP WebSocket at {ws_url}")

        mid = 1

        async def cdp_cmd(method: str, params: dict | None = None) -> dict:
            nonlocal mid
            m = mid
            mid += 1
            await ws.send(json.dumps({"id": m, "method": method, "params": params or {}}))
            while True:
                msg = await ws.recv()
                d = json.loads(msg)
                if d.get("id") == m:
                    return d.get("result", {})

        log.info("Awaiting page hydration (6s)...")
        await asyncio.sleep(6)

        # Extraction script per timeframe
        script_extract = """
        (async (tf) => {
            const tabs = Array.from(document.querySelectorAll('#heatmap .MuiTab-root, .lp-heat-panel .MuiTab-root'));
            const btn = tabs.find(b => b.innerText.trim() === tf);
            if (btn) {
                btn.click();
                await new Promise(r => setTimeout(r, 1500));
            }
            
            const tiles = Array.from(document.querySelectorAll('.lp-tile'));
            return tiles.map(t => {
                const aria = t.getAttribute('aria-label') || '';
                const titleEl = t.querySelector('.lp-tile-title b') || t.querySelector('b');
                const coin = titleEl ? titleEl.innerText.trim() : (aria.split(' ')[0] || '');
                const ariaParts = aria.split(' ');
                const amount = ariaParts.length > 1 ? ariaParts.slice(1).join(' ') : '';
                return { coin, amount };
            });
        })
        """

        for tf in timeframes:
            log.info(f"Switching Heatmap timeframe to '{tf}'...")
            res = await cdp_cmd(
                "Runtime.callFunctionOn",
                {
                    "functionDeclaration": script_extract,
                    "arguments": [{"value": tf}],
                    "executionContextId": None,
                    "returnByValue": True,
                    "awaitPromise": True,
                },
            )

            # In case callFunctionOn needs evaluate instead:
            eval_script = f"""
            (async () => {{
                const tf = '{tf}';
                const tabs = Array.from(document.querySelectorAll('#heatmap .MuiTab-root, .lp-heat-panel .MuiTab-root'));
                const btn = tabs.find(b => b.innerText.trim() === tf);
                if (btn) {{
                    btn.click();
                    await new Promise(r => setTimeout(r, 1500));
                }}
                
                const tiles = Array.from(document.querySelectorAll('.lp-tile'));
                return tiles.map(t => {{
                    const aria = t.getAttribute('aria-label') || '';
                    const titleEl = t.querySelector('.lp-tile-title b') || t.querySelector('b');
                    const coin = titleEl ? titleEl.innerText.trim() : (aria.split(' ')[0] || '');
                    const ariaParts = aria.split(' ');
                    const amount = ariaParts.length > 1 ? ariaParts.slice(1).join(' ') : '';
                    return {{ coin, amount }};
                }});
            }})()
            """
            eval_res = await cdp_cmd(
                "Runtime.evaluate",
                {"expression": eval_script, "awaitPromise": True, "returnByValue": True},
            )

            tile_list = eval_res.get("result", {}).get("value", [])
            log.info(f"Extracted {len(tile_list)} tiles for timeframe '{tf}'.")

            for item in tile_list:
                c = item.get("coin", "").strip()
                amt = item.get("amount", "").strip()
                if c and c != "Other":
                    tf_data[tf][c] = amt
                elif c == "Other":
                    tf_data[tf]["Other"] = amt

        await ws.close()

    finally:
        close_tab(tab_id)

    # Union of all assets seen across any timeframe
    all_assets: set[str] = set()
    for tf in timeframes:
        all_assets.update(tf_data[tf].keys())

    # Sort assets by 24h value descending, then 12h, 4h, 1h
    def sort_key(asset_name: str) -> float:
        if asset_name == "Other":
            return -1.0  # Put Other at the bottom
        val_24h = parse_numeric_value(tf_data["24h"].get(asset_name, ""))
        val_12h = parse_numeric_value(tf_data["12h"].get(asset_name, ""))
        val_4h = parse_numeric_value(tf_data["4h"].get(asset_name, ""))
        val_1h = parse_numeric_value(tf_data["1h"].get(asset_name, ""))
        return val_24h * 1000 + val_12h * 100 + val_4h * 10 + val_1h

    sorted_assets = sorted(list(all_assets), key=sort_key, reverse=True)

    records: list[dict] = []
    for rank_idx, asset in enumerate(sorted_assets, start=1):
        records.append(
            {
                "rank": rank_idx if asset != "Other" else len(sorted_assets),
                "asset": asset,
                "tf_1h": tf_data["1h"].get(asset, "-"),
                "tf_4h": tf_data["4h"].get(asset, "-"),
                "tf_12h": tf_data["12h"].get(asset, "-"),
                "tf_24h": tf_data["24h"].get(asset, "-"),
                "timestamp_utc": ts_str,
            }
        )

    log.info(f"Heatmap matrix built: {len(records)} unique assets across 1h, 4h, 12h, 24h.")
    return records


def dump_to_excel(records: list[dict], excel_path: pathlib.Path = DEFAULT_EXCEL_PATH) -> bool:
    """Dumps liquidation heatmap data into worksheet '7_Liq_Heapmap'."""
    if not excel_path.exists():
        log.error(f"Excel workbook not found at: {excel_path}")
        return False

    if not records:
        log.error("Integrity guard: 0 records extracted. Aborting dump to prevent empty sheet.")
        return False

    wb = openpyxl.load_workbook(excel_path)

    # Place sheet 7_Liq_Heapmap at Index 9 (immediately after 6_Funding_Fee_Settlement)
    if SHEET_NAME in wb.sheetnames:
        idx = wb.sheetnames.index(SHEET_NAME)
        wb.remove(wb[SHEET_NAME])
        ws = wb.create_sheet(title=SHEET_NAME, index=idx)
    else:
        target_idx = 9 if len(wb.sheetnames) >= 9 else len(wb.sheetnames)
        ws = wb.create_sheet(title=SHEET_NAME, index=target_idx)

    log.info(f"Target worksheet '{SHEET_NAME}' positioned at index {wb.sheetnames.index(SHEET_NAME)}")

    # Visual Styles
    hdr_font = Font(name="Segoe UI", size=10, bold=True, color="FFFFFF")
    hdr_fill = PatternFill(start_color="0F172A", end_color="0F172A", fill_type="solid")

    base_font = Font(name="Segoe UI", size=9, color="000000")
    bold_font = Font(name="Segoe UI", size=9, bold=True, color="000000")
    amt_font = Font(name="Segoe UI", size=9, bold=True, color="1E293B")
    subdued_font = Font(name="Segoe UI", size=9, color="888888")

    thin_border_side = Side(border_style="thin", color="E2E8F0")
    row_border = Border(
        left=thin_border_side, right=thin_border_side, top=thin_border_side, bottom=thin_border_side
    )

    # 1. Header Row
    ws.row_dimensions[1].height = 26
    for col_idx, (col_key, header_title, width, align) in enumerate(COLUMNS_DEF, start=1):
        cell = ws.cell(row=1, column=col_idx, value=header_title)
        cell.font = hdr_font
        cell.fill = hdr_fill
        cell.alignment = Alignment(horizontal=align, vertical="center")
        cell.border = row_border
        col_letter = get_column_letter(col_idx)
        ws.column_dimensions[col_letter].width = width

    # 2. Data Rows
    current_row = 2
    for r in records:
        ws.row_dimensions[current_row].height = 20

        # Rank (Col 1)
        c1 = ws.cell(row=current_row, column=1, value=r.get("rank", ""))
        c1.font = subdued_font
        c1.alignment = Alignment(horizontal="center", vertical="center")
        c1.border = row_border

        # Asset (Col 2)
        c2 = ws.cell(row=current_row, column=2, value=r.get("asset", "-"))
        c2.font = bold_font
        c2.alignment = Alignment(horizontal="center", vertical="center")
        c2.border = row_border

        # 1hour (Col 3)
        c3 = ws.cell(row=current_row, column=3, value=r.get("tf_1h", "-"))
        c3.font = amt_font
        c3.alignment = Alignment(horizontal="right", vertical="center")
        c3.border = row_border

        # 4hour (Col 4)
        c4 = ws.cell(row=current_row, column=4, value=r.get("tf_4h", "-"))
        c4.font = amt_font
        c4.alignment = Alignment(horizontal="right", vertical="center")
        c4.border = row_border

        # 12 hour (Col 5)
        c5 = ws.cell(row=current_row, column=5, value=r.get("tf_12h", "-"))
        c5.font = amt_font
        c5.alignment = Alignment(horizontal="right", vertical="center")
        c5.border = row_border

        # 24hour (Col 6)
        c6 = ws.cell(row=current_row, column=6, value=r.get("tf_24h", "-"))
        c6.font = amt_font
        c6.alignment = Alignment(horizontal="right", vertical="center")
        c6.border = row_border

        # Timestamp (Col 7)
        c7 = ws.cell(row=current_row, column=7, value=r.get("timestamp_utc", "-"))
        c7.font = subdued_font
        c7.alignment = Alignment(horizontal="center", vertical="center")
        c7.border = row_border

        current_row += 1

    # Freeze top row
    ws.freeze_panes = "A2"

    temp_excel = excel_path.with_suffix(".tmp.xlsx")
    wb.save(temp_excel)
    wb.close()
    import time, zipfile
    _is_valid = False
    with zipfile.ZipFile(temp_excel, "r") as _z:
        _is_valid = (_z.testzip() is None)
    if _is_valid:
        for _att in range(10):
            try:
                temp_excel.replace(excel_path)
                break
            except PermissionError:
                if _att == 9: raise
                time.sleep(0.5)
    else:
        if temp_excel.exists(): temp_excel.unlink()
        raise ValueError("Corrupt zip produced during export")
    wb.close()
    log.info(f"Successfully saved {len(records)} rows to {excel_path} [{SHEET_NAME}].")
    return True


def main():
    parser = argparse.ArgumentParser(description="CoinGlass Liquidation Heatmap Multi-Timeframe Scraper")
    parser.add_argument(
        "--excel-path",
        type=pathlib.Path,
        default=DEFAULT_EXCEL_PATH,
        help="Path to DataBase_Trading.xlsx",
    )
    args = parser.parse_args()

    records = asyncio.run(harvest_liquidation_heatmap())
    if not records:
        log.error("No records harvested from Heatmap.")
        sys.exit(1)

    success = dump_to_excel(records, args.excel_path)
    if not success:
        log.error("Failed to dump data to Excel.")
        sys.exit(1)

    log.info("7_Liq_Heapmap module completed successfully.")


if __name__ == "__main__":
    main()
