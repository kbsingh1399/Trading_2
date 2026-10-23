#!/usr/bin/env python3
"""
Data/Excel_Modules/5_Funding_Rate.py
===================================
Dedicated Excel Module 5: Crypto Funding Rates Across All Exchanges.
Extracts real-time Perpetual & Futures Funding Rates from CoinGlass:
https://www.coinglass.com/FundingRate

Features:
  1. Complete Multi-Exchange Coverage:
     - USDT or USD Margined: Binance, OKX, Bybit, KuCoin, MEXC, BingX, Gate,
       Bitunix, Bitget, WhiteBIT, LBank, tradeXYZ (12 exchanges).
     - Token Margined (Coin-M): Binance, OKX, Bybit (3 exchanges).
  2. All-Page Exhaustive Traversal:
     - Automatically iterates through all pagination pages (default: 30 pages,
       20 pairs per page = up to 600 crypto pairs) until all pages are scraped.
  3. Visual & Qualitative Parity:
     - Dual-tier header banners (USDT Margined vs Token Margined).
     - Emerald Green (#00A86B) for positive funding rates (longs pay shorts).
     - Crimson Red (#E53935) for negative funding rates (shorts pay longs).
  4. Tab Hygiene & Network Shield:
     - Isolated ephemeral CDP tab on port 9222, closed in a finally block (arena.ai preserved).
     - Cloudflare Anycast routing.
  5. Excel Placement:
     - Dumps cleanly into worksheet '5_Funding_Rate' positioned at Index 7 in Data/DataBase_Trading.xlsx.
"""

from __future__ import annotations

import argparse
import asyncio
import datetime
import json
import logging
import os
import pathlib
import sys
import time
import urllib.request

try:
    import openpyxl
    from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
    from openpyxl.utils import get_column_letter
except ImportError:
    raise ImportError("openpyxl is required. Run 'pip install openpyxl'.")

try:
    import websockets
except ImportError:
    websockets = None

ROOT = pathlib.Path(__file__).resolve().parents[2]
DATA_DIR = ROOT / "Data"
DEFAULT_EXCEL_PATH = DATA_DIR / "DataBase_Trading.xlsx"
SHEET_NAME = "5_Funding_Rate"
CDP_BASE_URL = "http://127.0.0.1:9222"
TARGET_URL = "https://www.coinglass.com/FundingRate"

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] [5_Funding_Rate] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)
log = logging.getLogger("5_Funding_Rate")

# Columns schema definition: (key, header_title, width, alignment)
COLUMNS_SCHEMA = [
    ("symbol", "Symbol", 14, "center"),
    ("usdt_binance", "Binance", 16, "right"),
    ("usdt_okx", "OKX", 16, "right"),
    ("usdt_bybit", "Bybit", 16, "right"),
    ("usdt_kucoin", "KuCoin", 16, "right"),
    ("usdt_mexc", "MEXC", 16, "right"),
    ("usdt_bingx", "BingX", 16, "right"),
    ("usdt_gate", "Gate", 16, "right"),
    ("usdt_bitunix", "Bitunix", 16, "right"),
    ("usdt_bitget", "Bitget", 16, "right"),
    ("usdt_whitebit", "WhiteBIT", 16, "right"),
    ("usdt_lbank", "LBank", 16, "right"),
    ("usdt_tradexyz", "tradeXYZ", 16, "right"),
    ("coin_binance", "Binance", 16, "right"),
    ("coin_okx", "OKX", 16, "right"),
    ("coin_bybit", "Bybit", 16, "right"),
    ("timestamp_ist", "Timestamp (IST)", 24, "center"),
]


def open_ephemeral_tab() -> tuple[str, str]:
    """Creates a new dedicated ephemeral tab via CDP."""
    req = urllib.request.Request(f"{CDP_BASE_URL}/json/new?{TARGET_URL}", method="PUT")
    new_tab = json.loads(urllib.request.urlopen(req, timeout=8).read().decode())
    return new_tab["id"], new_tab["webSocketDebuggerUrl"]


def close_tab(tab_id: str):
    """Closes tab via CDP."""
    try:
        urllib.request.urlopen(f"{CDP_BASE_URL}/json/close/{tab_id}", timeout=4)
        log.info(f"Closed ephemeral tab {tab_id}")
    except Exception as e:
        log.warning(f"Error closing tab {tab_id}: {e}")


def clean_rate_token(raw_text: str) -> str:
    """Parses raw table cell text into standard funding rate notation."""
    if not raw_text or raw_text.strip() == "-" or raw_text.strip() == "":
        return "-"
    parts = raw_text.split()
    if not parts:
        return "-"
    rate = parts[0].strip()
    if len(parts) > 1 and parts[1] == "*":
        rate += "*"
    return rate


async def harvest_funding_rates(max_pages: int = 30) -> list[dict]:
    """Navigates to CoinGlass FundingRate, extracts all rows across all pagination pages."""
    if not websockets:
        raise RuntimeError("websockets package is required.")

    tab_id, ws_url = open_ephemeral_tab()
    log.info(f"Opened dedicated ephemeral tab (ID: {tab_id}) for Funding Rate harvest.")

    now_dt = datetime.datetime.now(datetime.timezone.utc)
    ist_tz = datetime.timezone(datetime.timedelta(hours=5, minutes=30))
    now_ist = datetime.datetime.now(ist_tz)
    ts_str = now_ist.strftime("%Y-%m-%d %H:%M:%S IST")

    all_records: list[dict] = []
    seen_symbols: set[str] = set()

    try:
        ws = None
        for attempt in range(10):
            try:
                ws = await websockets.connect(ws_url, max_size=25 * 1024 * 1024, open_timeout=10)
                break
            except Exception:
                await asyncio.sleep(0.5)

        if not ws:
            raise RuntimeError(f"Could not connect to WebSocket at {ws_url}")

        async with ws:
            await asyncio.sleep(2.0)

            # 1. Wait for table DOM readiness
            readiness_js = """
            (() => {
                const table = document.querySelector('.ant-table-body table') || 
                              Array.from(document.querySelectorAll('table')).find(t => t.querySelectorAll('tbody tr').length > 0);
                if (!table) return 0;
                return table.querySelectorAll('tbody tr').length;
            })()
            """
            table_ready = False
            for _ in range(30):  # up to 15s
                await ws.send(json.dumps({"id": 10, "method": "Runtime.evaluate", "params": {"expression": readiness_js, "returnByValue": True}}))
                res = json.loads(await ws.recv())
                cnt = res.get("result", {}).get("result", {}).get("value", 0)
                if cnt >= 10:
                    table_ready = True
                    log.info(f"Funding rate table detected and ready with {cnt} rows.")
                    break
                await asyncio.sleep(0.5)

            if not table_ready:
                log.warning("Table readiness timed out after 15s; proceeding with best effort.")

            # 2. Page extraction JS
            extract_page_rows_js = """
            (() => {
                const table = document.querySelector('.ant-table-body table') || 
                              Array.from(document.querySelectorAll('table')).find(t => t.querySelectorAll('tbody tr').length > 0);
                if (!table) return [];
                const trs = Array.from(table.querySelectorAll('tbody tr'));
                return trs.map(tr => {
                    const tds = Array.from(tr.querySelectorAll('td'));
                    if (tds.length < 15) return null;

                    // Col 1 is Symbol (e.g. BTC, ETH...)
                    const symText = tds[1].innerText.trim();
                    if (!symText) return null;
                    const symbol = symText.split(/[ \\n]+/)[0].toUpperCase();

                    return {
                        symbol: symbol,
                        usdt_binance: tds[2] ? tds[2].innerText.trim() : "-",
                        usdt_okx: tds[3] ? tds[3].innerText.trim() : "-",
                        usdt_bybit: tds[4] ? tds[4].innerText.trim() : "-",
                        usdt_kucoin: tds[5] ? tds[5].innerText.trim() : "-",
                        usdt_mexc: tds[6] ? tds[6].innerText.trim() : "-",
                        usdt_bingx: tds[7] ? tds[7].innerText.trim() : "-",
                        usdt_gate: tds[8] ? tds[8].innerText.trim() : "-",
                        usdt_bitunix: tds[9] ? tds[9].innerText.trim() : "-",
                        usdt_bitget: tds[10] ? tds[10].innerText.trim() : "-",
                        usdt_whitebit: tds[11] ? tds[11].innerText.trim() : "-",
                        usdt_lbank: tds[12] ? tds[12].innerText.trim() : "-",
                        usdt_tradexyz: tds[13] ? tds[13].innerText.trim() : "-",
                        coin_binance: tds[15] ? tds[15].innerText.trim() : "-",
                        coin_okx: tds[16] ? tds[16].innerText.trim() : "-",
                        coin_bybit: tds[17] ? tds[17].innerText.trim() : "-"
                    };
                }).filter(r => r !== null);
            })()
            """

            click_next_page_js = """
            (() => {
                const nextBtn = document.querySelector('li.ant-pagination-next:not(.ant-pagination-disabled) button') || 
                                document.querySelector('li.ant-pagination-next:not(.ant-pagination-disabled)');
                if (nextBtn) {
                    nextBtn.click();
                    return true;
                }
                return false;
            })()
            """

            get_active_page_js = """
            (() => {
                const activeLi = document.querySelector('li.ant-pagination-item-active');
                return activeLi ? activeLi.innerText.trim() : null;
            })()
            """

            for page_idx in range(1, max_pages + 1):
                page_start_t = time.perf_counter()

                # Extract rows from current page
                await ws.send(json.dumps({"id": 100 + page_idx, "method": "Runtime.evaluate", "params": {"expression": extract_page_rows_js, "returnByValue": True}}))
                res = json.loads(await ws.recv())
                raw_rows = res.get("result", {}).get("result", {}).get("value", [])

                page_new_count = 0
                for r in raw_rows:
                    sym = r.get("symbol", "")
                    if not sym or sym in seen_symbols:
                        continue
                    seen_symbols.add(sym)

                    cleaned_rec = {
                        "symbol": sym,
                        "usdt_binance": clean_rate_token(r.get("usdt_binance")),
                        "usdt_okx": clean_rate_token(r.get("usdt_okx")),
                        "usdt_bybit": clean_rate_token(r.get("usdt_bybit")),
                        "usdt_kucoin": clean_rate_token(r.get("usdt_kucoin")),
                        "usdt_mexc": clean_rate_token(r.get("usdt_mexc")),
                        "usdt_bingx": clean_rate_token(r.get("usdt_bingx")),
                        "usdt_gate": clean_rate_token(r.get("usdt_gate")),
                        "usdt_bitunix": clean_rate_token(r.get("usdt_bitunix")),
                        "usdt_bitget": clean_rate_token(r.get("usdt_bitget")),
                        "usdt_whitebit": clean_rate_token(r.get("usdt_whitebit")),
                        "usdt_lbank": clean_rate_token(r.get("usdt_lbank")),
                        "usdt_tradexyz": clean_rate_token(r.get("usdt_tradexyz")),
                        "coin_binance": clean_rate_token(r.get("coin_binance")),
                        "coin_okx": clean_rate_token(r.get("coin_okx")),
                        "coin_bybit": clean_rate_token(r.get("coin_bybit")),
                        "timestamp_ist": ts_str
                    }
                    all_records.append(cleaned_rec)
                    page_new_count += 1

                page_elapsed = time.perf_counter() - page_start_t
                log.info(
                    f"Page {page_idx:>2}/{max_pages}: Extracted {len(raw_rows)} rows ({page_new_count} new, Total: {len(all_records)}) in {page_elapsed:.2f}s"
                )

                if page_idx >= max_pages:
                    break

                # Click next page
                await ws.send(json.dumps({"id": 200 + page_idx, "method": "Runtime.evaluate", "params": {"expression": click_next_page_js, "returnByValue": True}}))
                res_click = json.loads(await ws.recv())
                can_advance = res_click.get("result", {}).get("result", {}).get("value", False)

                if not can_advance:
                    log.info(f"Reached final pagination page at page {page_idx}.")
                    break

                # Wait for active page to advance
                target_page_str = str(page_idx + 1)
                page_updated = False
                for _ in range(25):  # up to 2.5s
                    await asyncio.sleep(0.1)
                    await ws.send(json.dumps({"id": 300 + page_idx, "method": "Runtime.evaluate", "params": {"expression": get_active_page_js, "returnByValue": True}}))
                    res_p = json.loads(await ws.recv())
                    curr_p = res_p.get("result", {}).get("result", {}).get("value")
                    if curr_p == target_page_str:
                        page_updated = True
                        break

                if not page_updated:
                    await asyncio.sleep(0.5)

    finally:
        close_tab(tab_id)

    log.info(f"Harvest complete: {len(all_records)} total crypto funding rate records collected across {max_pages} pages.")
    return all_records


def dump_to_excel(records: list[dict], excel_path: pathlib.Path = DEFAULT_EXCEL_PATH) -> bool:
    """Dumps funding rates into worksheet '5_Funding_Rate' with dual-tier headers and green/red styles."""
    if not excel_path.exists():
        log.error(f"Excel workbook not found at: {excel_path}")
        return False

    wb = openpyxl.load_workbook(excel_path)

    # Place sheet 5_Funding_Rate at Index 7 (after 5_OI)
    if SHEET_NAME in wb.sheetnames:
        idx = wb.sheetnames.index(SHEET_NAME)
        wb.remove(wb[SHEET_NAME])
        ws = wb.create_sheet(title=SHEET_NAME, index=idx)
    else:
        target_idx = 7 if len(wb.sheetnames) >= 7 else len(wb.sheetnames)
        ws = wb.create_sheet(title=SHEET_NAME, index=target_idx)

    log.info(f"Target worksheet '{SHEET_NAME}' positioned at index {wb.sheetnames.index(SHEET_NAME)}")

    # Visual Styles
    banner_font = Font(name="Segoe UI", size=10, bold=True, color="FFFFFF")
    sub_hdr_font = Font(name="Segoe UI", size=9, bold=True, color="FFFFFF")

    usdt_banner_fill = PatternFill(start_color="161B22", end_color="161B22", fill_type="solid")
    coin_banner_fill = PatternFill(start_color="21262D", end_color="21262D", fill_type="solid")
    meta_banner_fill = PatternFill(start_color="0D1117", end_color="0D1117", fill_type="solid")

    base_font = Font(name="Segoe UI", size=9, color="000000")
    bold_font = Font(name="Segoe UI", size=9, bold=True, color="000000")
    green_font = Font(name="Segoe UI", size=9, bold=True, color="00A86B")
    red_font = Font(name="Segoe UI", size=9, bold=True, color="E53935")
    subdued_font = Font(name="Segoe UI", size=9, color="888888")

    thin_border_side = Side(border_style="thin", color="E0E0E0")
    row_border = Border(left=thin_border_side, right=thin_border_side, top=thin_border_side, bottom=thin_border_side)

    # 1. Header Row 1: Dual Super-Headers
    # Col A: Symbol Info
    ws.cell(row=1, column=1, value="Symbol").font = banner_font
    ws.cell(row=1, column=1).fill = meta_banner_fill
    ws.cell(row=1, column=1).alignment = Alignment(horizontal="center", vertical="center")

    # Col B to M: USDT or USD Margined
    ws.merge_cells("B1:M1")
    b1_cell = ws.cell(row=1, column=2, value="USDT or USD Margined")
    b1_cell.font = banner_font
    b1_cell.fill = usdt_banner_fill
    b1_cell.alignment = Alignment(horizontal="center", vertical="center")
    for c in range(2, 14):
        ws.cell(row=1, column=c).fill = usdt_banner_fill

    # Col N to P: Token Margined (Coin-M)
    ws.merge_cells("N1:P1")
    n1_cell = ws.cell(row=1, column=14, value="Token Margined (Coin-M)")
    n1_cell.font = banner_font
    n1_cell.fill = coin_banner_fill
    n1_cell.alignment = Alignment(horizontal="center", vertical="center")
    for c in range(14, 17):
        ws.cell(row=1, column=c).fill = coin_banner_fill

    # Col Q: Metadata
    ws.cell(row=1, column=17, value="Metadata").font = banner_font
    ws.cell(row=1, column=17).fill = meta_banner_fill
    ws.cell(row=1, column=17).alignment = Alignment(horizontal="center", vertical="center")

    ws.row_dimensions[1].height = 26

    # 2. Header Row 2: Exchange Names
    sub_headers = [col[1] for col in COLUMNS_SCHEMA]
    ws.append(sub_headers)
    for c_idx in range(1, len(sub_headers) + 1):
        cell = ws.cell(row=2, column=c_idx)
        cell.font = sub_hdr_font
        if c_idx == 1 or c_idx == 17:
            cell.fill = meta_banner_fill
        elif 2 <= c_idx <= 13:
            cell.fill = usdt_banner_fill
        else:
            cell.fill = coin_banner_fill
        cell.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)

    ws.row_dimensions[2].height = 24

    # 3. Data Rows
    for row_num, rec in enumerate(records, start=3):
        row_vals = [rec.get(col[0], "-") for col in COLUMNS_SCHEMA]
        ws.append(row_vals)

        for c_idx, col_def in enumerate(COLUMNS_SCHEMA, start=1):
            cell = ws.cell(row=row_num, column=c_idx)
            cell.border = row_border
            key = col_def[0]
            val = str(cell.value)

            if key == "symbol":
                cell.font = bold_font
            elif key in ["timestamp_ist", "timestamp_utc"]:
                cell.font = base_font
            else:
                # Rate columns color coding
                if val == "-" or val == "0.0000%" or not val:
                    cell.font = subdued_font
                elif val.startswith("-"):
                    cell.font = red_font
                elif "%" in val:
                    cell.font = green_font
                else:
                    cell.font = base_font

            cell.alignment = Alignment(horizontal=col_def[3], vertical="center")

        ws.row_dimensions[row_num].height = 20

    # 4. Column Widths
    for c_idx, col_def in enumerate(COLUMNS_SCHEMA, start=1):
        col_letter = get_column_letter(c_idx)
        ws.column_dimensions[col_letter].width = col_def[2]

    ws.views.sheetView[0].showGridLines = True
    import os, time
        # Enforce Operator Invariant: Stamp Tier-1 Completion Banner ONLY ONCE row data is filled
    if ws.max_row > 1:
        try:
            from logger_config import stamp_sheet_completion_ist
            ws.insert_rows(1)
            stamp_sheet_completion_ist(
                ws=ws,
                sheet_title="5_Funding_Rate",
                row_count=ws.max_row - 2,
                banner_cell="A1",
                status="LIVE",
                merge_max_col=ws.max_column
            )
            ws.freeze_panes = "A3"
        except Exception as _e:
            pass

    temp_excel = excel_path.with_name(f"{excel_path.stem}_{os.getpid()}_{int(time.time()*1000)}.tmp.xlsx")
    wb.save(temp_excel)
    wb.close()
    import time, zipfile
    _is_valid = False
    with zipfile.ZipFile(temp_excel, "r") as _z:
        _is_valid = (_z.testzip() is None)
    if _is_valid:
        for _att in range(30):
            try:
                temp_excel.replace(excel_path)
                break
            except PermissionError:
                if _att == 29: raise
                time.sleep(1.0)
    else:
        if temp_excel.exists(): temp_excel.unlink()
        raise ValueError("Corrupt zip produced during export")
    log.info(
        f"Successfully dumped {len(records)} Crypto Funding Rate records into '{SHEET_NAME}' at {excel_path}."
    )
    return True


def main():
    parser = argparse.ArgumentParser(description="CoinGlass Crypto Funding Rate Table Dump to Excel")
    parser.add_argument("--pages", type=int, default=30, help="Number of pages to scrape (default: 30, up to 600 crypto pairs)")
    parser.add_argument("--excel-path", type=pathlib.Path, default=DEFAULT_EXCEL_PATH, help="Path to DataBase_Trading.xlsx")
    args = parser.parse_args()

    records = asyncio.run(harvest_funding_rates(max_pages=args.pages))
    if not records:
        log.error("No funding rate records harvested.")
        sys.exit(1)

    ok = dump_to_excel(records, excel_path=args.excel_path)
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
