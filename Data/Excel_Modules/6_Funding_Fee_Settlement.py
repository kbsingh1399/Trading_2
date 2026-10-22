#!/usr/bin/env python3
"""
Data/Excel_Modules/6_Funding_Fee_Settlement.py
=============================================
Live CoinGlass Perpetual Futures Funding Fee Settlement Data Scraper & Excel Dumper.
Scrapes the complete 'Funding Fee Settlement Overview' table across all 19 pages (~950+ crypto pairs)
from https://www.coinglass.com/funding-fees and dumps into worksheet '6_Funding_Fee_Settlement'
in Data/DataBase_Trading.xlsx (positioned at Index 8, immediately after '5_Funding_Rate').

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
log = logging.getLogger("6_Funding_Fee_Settlement")

MODULES_DIR = pathlib.Path(__file__).resolve().parent
ROOT_DIR = MODULES_DIR.parents[1]
DEFAULT_EXCEL_PATH = ROOT_DIR / "Data" / "DataBase_Trading.xlsx"
CDP_BASE_URL = "http://127.0.0.1:9222"
TARGET_URL = "https://www.coinglass.com/funding-fees"
SHEET_NAME = "6_Funding_Fee_Settlement"

COLUMNS_DEF = [
    ("rank", "#", 10, "center"),
    ("symbol", "Symbol", 16, "center"),
    ("price", "Price", 16, "right"),
    ("price_24h_pct", "Price (24h%)", 16, "right"),
    ("open_interest", "Open Interest", 18, "right"),
    ("current", "Current", 18, "right"),
    ("last_24h", "Last 24h", 18, "right"),
    ("last_3d", "Last 3 Days", 18, "right"),
    ("last_7d", "Last 7 Days", 18, "right"),
    ("timestamp_utc", "Timestamp (UTC)", 24, "center"),
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


async def harvest_funding_fee_settlements(max_pages: int = 19) -> list[dict]:
    """Navigates to CoinGlass Funding Fees, extracts all rows across all pagination pages."""
    if not websockets:
        raise RuntimeError("websockets package is required.")

    tab_id, ws_url = open_ephemeral_tab()
    log.info(f"Opened dedicated ephemeral tab (ID: {tab_id}) for Funding Fee Settlement harvest.")

    now_dt = datetime.datetime.now(datetime.timezone.utc)
    ts_str = now_dt.strftime("%Y-%m-%d %H:%M:%S UTC")

    all_records: list[dict] = []
    seen_ranks: set[str] = set()

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
                const table = document.querySelector('.ant-table-tbody') || document.querySelector('tbody');
                if (!table) return 0;
                return table.querySelectorAll('tr:not(.ant-table-measure-row)').length;
            })()
            """
            table_ready = False
            for _ in range(30):  # up to 15s
                await ws.send(json.dumps({"id": 10, "method": "Runtime.evaluate", "params": {"expression": readiness_js, "returnByValue": True}}))
                res = json.loads(await ws.recv())
                cnt = res.get("result", {}).get("result", {}).get("value", 0)
                if cnt >= 10:
                    table_ready = True
                    log.info(f"Funding fee settlement table detected and ready with {cnt} rows.")
                    break
                await asyncio.sleep(0.5)

            if not table_ready:
                log.warning("Table readiness timed out after 15s; proceeding with best effort.")

            # 2. Page extraction JS
            extract_page_rows_js = """
            (() => {
                const tbody = document.querySelector('.ant-table-tbody') || document.querySelector('tbody');
                if (!tbody) return [];
                const trs = Array.from(tbody.querySelectorAll('tr:not(.ant-table-measure-row)'));
                return trs.map(tr => {
                    const tds = Array.from(tr.querySelectorAll('td'));
                    if (tds.length < 9) return null;

                    const rank = tds[0].innerText.trim();
                    const symText = tds[1].innerText.trim();
                    if (!symText) return null;
                    const symbol = symText.split(/[ \\n]+/)[0].toUpperCase();

                    return {
                        rank: rank,
                        symbol: symbol,
                        price: tds[2] ? tds[2].innerText.trim() : "-",
                        price_24h_pct: tds[3] ? tds[3].innerText.trim() : "-",
                        open_interest: tds[4] ? tds[4].innerText.trim() : "-",
                        current: tds[5] ? tds[5].innerText.trim() : "-",
                        last_24h: tds[6] ? tds[6].innerText.trim() : "-",
                        last_3d: tds[7] ? tds[7].innerText.trim() : "-",
                        last_7d: tds[8] ? tds[8].innerText.trim() : "-"
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

            for page_idx in range(1, max_pages + 1):
                page_start_t = time.perf_counter()

                # Extract rows from current page
                msg_id = 100 + page_idx
                await ws.send(json.dumps({
                    "id": msg_id,
                    "method": "Runtime.evaluate",
                    "params": {"expression": extract_page_rows_js, "returnByValue": True}
                }))
                res = json.loads(await ws.recv())
                rows = res.get("result", {}).get("result", {}).get("value", [])

                page_new_count = 0
                first_row_rank = None
                for r in rows:
                    rank_key = r.get("rank")
                    if rank_key and rank_key not in seen_ranks:
                        seen_ranks.add(rank_key)
                        r["timestamp_utc"] = ts_str
                        all_records.append(r)
                        page_new_count += 1
                        if first_row_rank is None:
                            first_row_rank = rank_key

                page_dur = time.perf_counter() - page_start_t
                log.info(
                    f"Page {page_idx:>2}/{max_pages}: Extracted {len(rows)} rows ({page_new_count} new, Total: {len(all_records)}) in {page_dur:.2f}s"
                )

                if page_idx >= max_pages:
                    break

                # Click next page
                click_id = 200 + page_idx
                await ws.send(json.dumps({
                    "id": click_id,
                    "method": "Runtime.evaluate",
                    "params": {"expression": click_next_page_js, "returnByValue": True}
                }))
                res_click = json.loads(await ws.recv())
                clicked = res_click.get("result", {}).get("result", {}).get("value", False)

                if not clicked:
                    log.info(f"Next page button not found or disabled at page {page_idx}. Reached end of pagination.")
                    break

                # Wait for next page DOM transition (first row rank changes)
                check_transition_js = f"""
                (() => {{
                    const firstTd = document.querySelector('.ant-table-tbody tr:not(.ant-table-measure-row) td');
                    if (!firstTd) return false;
                    return firstTd.innerText.trim() !== '{first_row_rank}';
                }})()
                """
                transitioned = False
                for _ in range(25):  # up to 2.5s
                    await ws.send(json.dumps({
                        "id": 300 + page_idx,
                        "method": "Runtime.evaluate",
                        "params": {"expression": check_transition_js, "returnByValue": True}
                    }))
                    res_t = json.loads(await ws.recv())
                    if res_t.get("result", {}).get("result", {}).get("value", False):
                        transitioned = True
                        break
                    await asyncio.sleep(0.08)

                if not transitioned:
                    await asyncio.sleep(0.2)

    finally:
        close_tab(tab_id)

    log.info(f"Harvest complete: {len(all_records)} total funding fee settlement records collected across {max_pages} pages.")
    return all_records


def dump_to_excel(records: list[dict], excel_path: pathlib.Path = DEFAULT_EXCEL_PATH) -> bool:
    """Dumps funding fee settlement data into worksheet '6_Funding_Fee_Settlement'."""
    if not excel_path.exists():
        log.error(f"Excel workbook not found at: {excel_path}")
        return False

    wb = openpyxl.load_workbook(excel_path)

    # Place sheet 6_Funding_Fee_Settlement at Index 8 (immediately after 5_Funding_Rate)
    if SHEET_NAME in wb.sheetnames:
        idx = wb.sheetnames.index(SHEET_NAME)
        wb.remove(wb[SHEET_NAME])
        ws = wb.create_sheet(title=SHEET_NAME, index=idx)
    else:
        target_idx = 8 if len(wb.sheetnames) >= 8 else len(wb.sheetnames)
        ws = wb.create_sheet(title=SHEET_NAME, index=target_idx)

    log.info(f"Target worksheet '{SHEET_NAME}' positioned at index {wb.sheetnames.index(SHEET_NAME)}")

    # Visual Styles
    hdr_font = Font(name="Segoe UI", size=10, bold=True, color="FFFFFF")
    hdr_fill = PatternFill(start_color="0F172A", end_color="0F172A", fill_type="solid")

    base_font = Font(name="Segoe UI", size=9, color="000000")
    bold_font = Font(name="Segoe UI", size=9, bold=True, color="000000")
    green_font = Font(name="Segoe UI", size=9, bold=True, color="00A86B")
    red_font = Font(name="Segoe UI", size=9, bold=True, color="E53935")
    subdued_font = Font(name="Segoe UI", size=9, color="888888")

    thin_border_side = Side(border_style="thin", color="E2E8F0")
    row_border = Border(left=thin_border_side, right=thin_border_side, top=thin_border_side, bottom=thin_border_side)

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
        rank_val = r.get("rank", "")
        try:
            rank_num = int(rank_val)
        except (ValueError, TypeError):
            rank_num = rank_val
        c1 = ws.cell(row=current_row, column=1, value=rank_num)
        c1.font = subdued_font
        c1.alignment = Alignment(horizontal="center", vertical="center")
        c1.border = row_border

        # Symbol (Col 2)
        c2 = ws.cell(row=current_row, column=2, value=r.get("symbol", "-"))
        c2.font = bold_font
        c2.alignment = Alignment(horizontal="center", vertical="center")
        c2.border = row_border

        # Price (Col 3)
        c3 = ws.cell(row=current_row, column=3, value=r.get("price", "-"))
        c3.font = base_font
        c3.alignment = Alignment(horizontal="right", vertical="center")
        c3.border = row_border

        # Price (24h%) (Col 4)
        p24 = r.get("price_24h_pct", "-")
        c4 = ws.cell(row=current_row, column=4, value=p24)
        if p24.startswith("+"):
            c4.font = green_font
        elif p24.startswith("-"):
            c4.font = red_font
        else:
            c4.font = base_font
        c4.alignment = Alignment(horizontal="right", vertical="center")
        c4.border = row_border

        # Open Interest (Col 5)
        c5 = ws.cell(row=current_row, column=5, value=r.get("open_interest", "-"))
        c5.font = base_font
        c5.alignment = Alignment(horizontal="right", vertical="center")
        c5.border = row_border

        # Current (Col 6)
        curr = r.get("current", "-")
        c6 = ws.cell(row=current_row, column=6, value=curr)
        if curr.startswith("-") and curr != "-":
            c6.font = red_font
        elif curr.startswith("$") or (curr != "-" and not curr.startswith("-")):
            c6.font = green_font
        else:
            c6.font = base_font
        c6.alignment = Alignment(horizontal="right", vertical="center")
        c6.border = row_border

        # Last 24h (Col 7)
        l24 = r.get("last_24h", "-")
        c7 = ws.cell(row=current_row, column=7, value=l24)
        if l24.startswith("-") and l24 != "-":
            c7.font = red_font
        elif l24.startswith("$") or (l24 != "-" and not l24.startswith("-")):
            c7.font = green_font
        else:
            c7.font = base_font
        c7.alignment = Alignment(horizontal="right", vertical="center")
        c7.border = row_border

        # Last 3 Days (Col 8)
        l3d = r.get("last_3d", "-")
        c8 = ws.cell(row=current_row, column=8, value=l3d)
        if l3d.startswith("-") and l3d != "-":
            c8.font = red_font
        elif l3d.startswith("$") or (l3d != "-" and not l3d.startswith("-")):
            c8.font = green_font
        else:
            c8.font = base_font
        c8.alignment = Alignment(horizontal="right", vertical="center")
        c8.border = row_border

        # Last 7 Days (Col 9)
        l7d = r.get("last_7d", "-")
        c9 = ws.cell(row=current_row, column=9, value=l7d)
        if l7d.startswith("-") and l7d != "-":
            c9.font = red_font
        elif l7d.startswith("$") or (l7d != "-" and not l7d.startswith("-")):
            c9.font = green_font
        else:
            c9.font = base_font
        c9.alignment = Alignment(horizontal="right", vertical="center")
        c9.border = row_border

        # Timestamp UTC (Col 10)
        c10 = ws.cell(row=current_row, column=10, value=r.get("timestamp_utc", ""))
        c10.font = subdued_font
        c10.alignment = Alignment(horizontal="center", vertical="center")
        c10.border = row_border

        current_row += 1

    # Freeze panes below header
    ws.freeze_panes = "A2"

    temp_excel = excel_path.with_suffix(".tmp.xlsx")
    wb.save(temp_excel)
    wb.close()
    import zipfile
    with zipfile.ZipFile(temp_excel, "r") as _z:
        if _z.testzip() is None:
            temp_excel.replace(excel_path)
        else:
            if temp_excel.exists(): temp_excel.unlink()
            raise ValueError("Corrupt zip produced during export")
    log.info(
        f"Successfully dumped {len(records)} Funding Fee Settlement records into '{SHEET_NAME}' at {excel_path}."
    )
    return True


def main():
    parser = argparse.ArgumentParser(description="CoinGlass Perpetual Futures Funding Fee Settlement Scraper & Excel Dumper")
    parser.add_argument("--pages", type=int, default=19, help="Number of pages to harvest (default: 19)")
    parser.add_argument("--excel-path", type=pathlib.Path, default=DEFAULT_EXCEL_PATH, help="Path to target Excel workbook")
    args = parser.parse_args()

    log.info("================================================================================")
    log.info("           COINGLASS FUNDING FEE SETTLEMENT EXCEL DUMPER                        ")
    log.info(f"Target URL:    {TARGET_URL}")
    log.info(f"Pages:         {args.pages}")
    log.info(f"Target Sheet:  {SHEET_NAME}")
    log.info(f"Workbook:      {args.excel_path}")
    log.info("================================================================================")

    start_time = time.perf_counter()
    records = asyncio.run(harvest_funding_fee_settlements(max_pages=args.pages))

    if not records:
        log.error("No funding fee settlement records harvested. Aborting Excel dump.")
        sys.exit(1)

    success = dump_to_excel(records, excel_path=args.excel_path)
    elapsed = time.perf_counter() - start_time
    log.info(f"Finished in {elapsed:.2f} seconds with status: {'SUCCESS' if success else 'FAILED'}")
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
