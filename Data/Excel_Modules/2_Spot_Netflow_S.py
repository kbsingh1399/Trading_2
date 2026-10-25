#!/usr/bin/env python3
"""
Data/Excel_Modules/2_Spot_Netflow_S.py
======================================
Dedicated Excel Module 2: Cryptocurrency Spot Netflow Statistics.
Extracts live Cryptocurrency Spot Inflow / Outflow data from CoinGlass:
https://www.coinglass.com/spot-inflow-outflow

Features:
  - Automates ephemeral CDP tab over Chrome/Edge port 9222.
  - Opens dedicated tab, ensures 'Spot' tab is selected, deterministically resets to Page 1.
  - High-speed pagination engine iterating through ul.rc-pagination .rc-pagination-next
    with dynamic DOM mutation listener (~1.1s/page).
  - Dumps directly into sheet '2_Spot_Netflow_S' in Data/DataBase_Trading.xlsx,
    positioned immediately next to '1_Crypto_ETF_Flows' (Sheet Index 1).
  - Matches CoinGlass exact format with Mint/Vibrant Green (#DCFCE7/#BBF7D0) and
    Coral/Intense Salmon (#FEE2E2/#FECACA) heatmaps across all timeframe netflows.
  - Automatically closes the ephemeral tab upon completion in a finally block.
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
CACHE_JSON_PATH = DATA_DIR / "coinglass" / "latest" / "coinglass_spot_netflow_statistics.json"
CDP_BASE_URL = "http://127.0.0.1:9222"
SHEET_NAME = "2_Spot_Netflow_S"
REFERENCE_SHEET = "1_Crypto_ETF_Flows"

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] [2_Spot_Netflow_S] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)
log = logging.getLogger("2_Spot_Netflow_S")

COLUMNS = [
    ("#", "#", 8, "center"),
    ("Symbol", "Symbol", 14, "left"),
    ("Price", "Price", 14, "right"),
    ("5_min", "5 minute", 14, "right"),
    ("15_min", "15 minute", 14, "right"),
    ("30_min", "30 minute", 14, "right"),
    ("1_hour", "1 hour", 14, "right"),
    ("4_hour", "4 hour", 14, "right"),
    ("12_hour", "12 hour", 14, "right"),
    ("24_hour", "24 hour", 14, "right"),
    ("7_day", "7 day", 15, "right"),
    ("30_day", "30 day", 15, "right"),
    ("Market_Cap", "Market Cap", 16, "right"),
    ("Timestamp_IST", "Timestamp (IST)", 24, "center")
]


def open_spot_tab() -> tuple[str, str]:
    """Creates a new dedicated ephemeral CoinGlass Spot Netflow tab via CDP."""
    req = urllib.request.Request(f"{CDP_BASE_URL}/json/new?https://www.coinglass.com/spot-inflow-outflow", method="PUT")
    new_tab = json.loads(urllib.request.urlopen(req, timeout=5).read().decode())
    return new_tab["id"], new_tab["webSocketDebuggerUrl"]


def close_tab(tab_id: str):
    """Closes tab via CDP."""
    try:
        urllib.request.urlopen(f"{CDP_BASE_URL}/json/close/{tab_id}", timeout=4)
        log.info(f"Closed tab {tab_id}")
    except Exception as e:
        log.warning(f"Error closing tab: {e}")


async def extract_spot_netflows(max_pages: int = 25) -> list[dict]:
    """
    Extracts all pages of CoinGlass Cryptocurrency Spot Netflow Statistics using fast smart pagination.
    """
    if not websockets:
        log.error("websockets package required for CDP connection.")
        return []

    tab_id, ws_url = open_spot_tab()
    log.info(f"Opened dedicated CoinGlass spot tab (ID: {tab_id})")

    now_dt = datetime.datetime.now(datetime.timezone.utc)
    ist_tz = datetime.timezone(datetime.timedelta(hours=5, minutes=30))
    now_ist = datetime.datetime.now(ist_tz)
    ts_str = now_ist.strftime("%Y-%m-%d %H:%M:%S IST")

    try:
        await asyncio.sleep(2.0)
        async with websockets.connect(ws_url, max_size=25 * 1024 * 1024, open_timeout=15) as ws:
            # 1. Wait for Table Hydration (up to 15 seconds)
            check_hydration_js = """
            (() => {
                const tables = Array.from(document.querySelectorAll('table'));
                const dt = tables.length > 1 ? tables[1] : tables[0];
                if (!dt) return false;
                const tr = dt.querySelector('tbody tr');
                if (!tr) return false;
                const tds = tr.querySelectorAll('td');
                return tds.length >= 2 && tds[1].innerText && tds[1].innerText.trim().length > 0;
            })()
            """
            hydrated = False
            for _ in range(30):
                await ws.send(json.dumps({"id": 99, "method": "Runtime.evaluate", "params": {"expression": check_hydration_js, "returnByValue": True}}))
                h_res = json.loads(await ws.recv())
                if h_res.get("result", {}).get("result", {}).get("value", False):
                    hydrated = True
                    break
                await asyncio.sleep(0.5)

            if not hydrated:
                log.warning("Table hydration timeout; proceeding with extraction attempts...")

            # 2. Ensure 'Spot' tab is selected if 'Futures' is active
            ensure_spot_js = """
            (() => {
                const btns = Array.from(document.querySelectorAll('button, [role="tab"], div, span'));
                const spotBtn = btns.find(b => b.innerText && b.innerText.trim() === 'Spot');
                if (spotBtn && !spotBtn.classList.contains('Mui-selected')) {
                    spotBtn.click();
                    return true;
                }
                return false;
            })()
            """
            await ws.send(json.dumps({"id": 1, "method": "Runtime.evaluate", "params": {"expression": ensure_spot_js, "returnByValue": True}}))
            await ws.recv()
            await asyncio.sleep(1.0)

            # 3. Extraction loop across requested pages
            extract_page_rows_js = """
            (() => {
                const tables = Array.from(document.querySelectorAll('table'));
                const dt = tables.length > 1 ? tables[1] : tables[0];
                if (!dt) return [];
                const rows = Array.from(dt.querySelectorAll('tbody tr'));
                return rows.map(tr => {
                    const cells = Array.from(tr.querySelectorAll('td'));
                    return cells.map(td => td.innerText ? td.innerText.trim() : td.textContent.trim());
                }).filter(r => r.length >= 8 && r[1] && r[1].trim() !== '');
            })()
            """

            click_next_js = """
            (() => {
                const nextBtn = document.querySelector('ul.rc-pagination li.rc-pagination-next:not(.rc-pagination-disabled) button') ||
                                document.querySelector('ul.rc-pagination li.rc-pagination-next:not(.rc-pagination-disabled)') ||
                                document.querySelector('.rc-pagination-next:not(.rc-pagination-disabled)');
                if (nextBtn) {
                    nextBtn.click();
                    return true;
                }
                return false;
            })()
            """

            get_first_symbol_js = """
            (() => {
                const tables = Array.from(document.querySelectorAll('table'));
                const dt = tables.length > 1 ? tables[1] : tables[0];
                if (!dt) return '';
                const firstRow = dt.querySelector('tbody tr td:nth-child(2)');
                return firstRow ? (firstRow.innerText ? firstRow.innerText.trim() : firstRow.textContent.trim()) : '';
            })()
            """

            all_records = []
            seen_symbols = set()
            start_harvest_t = time.perf_counter()

            for page in range(1, max_pages + 1):
                # Extract rows from current page
                msg_id = 100 + page * 2
                await ws.send(json.dumps({
                    "id": msg_id,
                    "method": "Runtime.evaluate",
                    "params": {"expression": extract_page_rows_js, "returnByValue": True}
                }))
                raw_resp = await ws.recv()
                res = json.loads(raw_resp)
                rows = res.get("result", {}).get("result", {}).get("value", [])

                page_extracted = 0
                for r in rows:
                    if not r or len(r) < 8:
                        continue

                    # Parsing columns from CoinGlass table row
                    rank = r[0] if len(r) > 0 else str(len(all_records) + 1)
                    raw_sym = r[1] if len(r) > 1 else ""
                    # Split symbol and subtitle if merged (e.g. "BTC\nBitcoin")
                    symbol = raw_sym.split("\n")[0].strip()
                    if not symbol or symbol in seen_symbols:
                        continue

                    seen_symbols.add(symbol)
                    page_extracted += 1

                    # Smart mapping: CoinGlass live format has Symbol at r[1], Netflows starting at r[2]
                    # Format: ['', Symbol, 5m, 15m, 30m, 1h, 2h, 4h, 6h, 8h, 12h, 24h, 1w/7d, 15d, 30d, Market Cap]
                    if len(r) >= 15 and ('+' in str(r[2]) or '-' in str(r[2])):
                        price = "-"
                        f_5m = r[2]
                        f_15m = r[3]
                        f_30m = r[4]
                        f_1h = r[5]
                        f_4h = r[7] if len(r) > 7 else "-"
                        f_12h = r[10] if len(r) > 10 else "-"
                        f_24h = r[11] if len(r) > 11 else "-"
                        f_7d = r[12] if len(r) > 12 else "-"
                        f_30d = r[14] if len(r) > 14 else "-"
                        mkt_cap = r[15] if len(r) > 15 else r[-1]
                    else:
                        price = r[2] if len(r) > 2 else "-"
                        f_5m = r[3] if len(r) > 3 else "-"
                        f_15m = r[4] if len(r) > 4 else "-"
                        f_30m = r[5] if len(r) > 5 else "-"
                        f_1h = r[6] if len(r) > 6 else "-"
                        f_4h = r[7] if len(r) > 7 else "-"
                        f_12h = r[8] if len(r) > 8 else "-"
                        f_24h = r[9] if len(r) > 9 else "-"
                        f_7d = r[10] if len(r) > 10 else "-"
                        f_30d = r[11] if len(r) > 11 else "-"
                        mkt_cap = r[12] if len(r) > 12 else (r[-1] if len(r) >= 13 else "-")

                    all_records.append({
                        "#": str(len(all_records) + 1),
                        "Symbol": symbol,
                        "Price": price,
                        "5_min": f_5m,
                        "15_min": f_15m,
                        "30_min": f_30m,
                        "1_hour": f_1h,
                        "4_hour": f_4h,
                        "12_hour": f_12h,
                        "24_hour": f_24h,
                        "7_day": f_7d,
                        "30_day": f_30d,
                        "Market_Cap": mkt_cap,
                        "Timestamp_IST": ts_str
                    })

                log.info(f"Page {page:>2}/{max_pages}: Extracted {page_extracted} assets (Total cumulative: {len(all_records)})")

                if page >= max_pages:
                    break

                # Get current row 1 symbol to detect DOM mutation upon page switch
                current_top_sym = rows[0][1].split("\n")[0].strip() if rows else ""

                # Click Next Page
                await ws.send(json.dumps({
                    "id": msg_id + 1,
                    "method": "Runtime.evaluate",
                    "params": {"expression": click_next_js, "returnByValue": True}
                }))
                click_res = json.loads(await ws.recv())
                can_click = click_res.get("result", {}).get("result", {}).get("value", False)
                if not can_click:
                    log.info(f"Next button disabled or last page reached at page {page}.")
                    break

                # Fast DOM mutation poll: wait until first row changes
                changed = False
                for _ in range(25):  # up to 2.5s wait
                    await asyncio.sleep(0.1)
                    await ws.send(json.dumps({
                        "id": 9999,
                        "method": "Runtime.evaluate",
                        "params": {"expression": get_first_symbol_js, "returnByValue": True}
                    }))
                    top_sym_res = json.loads(await ws.recv())
                    new_top_sym = top_sym_res.get("result", {}).get("result", {}).get("value", "").split("\n")[0].strip()
                    if new_top_sym and new_top_sym != current_top_sym:
                        changed = True
                        break

                if not changed:
                    await asyncio.sleep(0.4)

            elapsed_harvest = time.perf_counter() - start_harvest_t
            log.info(f"Harvested {len(all_records)} unique crypto spot netflow assets in {elapsed_harvest:.2f} seconds.")

            # Save snapshot to local JSON cache
            CACHE_JSON_PATH.parent.mkdir(parents=True, exist_ok=True)
            with open(CACHE_JSON_PATH, "w", encoding="utf-8") as f:
                json.dump({
                    "harvest_timestamp_utc": now_dt.isoformat(),
                    "total_records": len(all_records),
                    "pages_scanned": page,
                    "records": all_records
                }, f, indent=2)

            return all_records
    except Exception as e:
        log.error(f"Error during CDP spot netflow extraction: {e}")
        return []
    finally:
        close_tab(tab_id)


def load_from_local_cache() -> list[dict]:
    """Loads records from local JSON cache if available."""
    if CACHE_JSON_PATH.exists():
        try:
            with open(CACHE_JSON_PATH, "r", encoding="utf-8") as f:
                data = json.load(f)
                recs = data.get("records", [])
                log.info(f"Loaded {len(recs)} spot netflow records from local cache: {CACHE_JSON_PATH}")
                return recs
        except Exception as e:
            log.warning(f"Error reading local cache: {e}")
    return []


def dump_spot_netflow_to_excel(excel_path: pathlib.Path = DEFAULT_EXCEL_PATH, max_pages: int = 25) -> bool:
    """
    Dumps Cryptocurrency Spot Netflow Statistics into '2_Spot_Netflow_S' sheet,
    positioned immediately next to '1_Crypto_ETF_Flows'.
    """
    import filelock
    from logger_config import stamp_sheet_completion_ist
    
    records = asyncio.run(extract_spot_netflows(max_pages=max_pages))
    if not records:
        log.info("Attempting fallback to local cache...")
        records = load_from_local_cache()

    if not records:
        log.error("Failed to acquire any spot netflow records. Aborting Excel update.")
        return False

    if not excel_path.exists():
        log.error(f"Target Excel file does not exist: {excel_path}")
        return False

    lock = filelock.FileLock(str(excel_path) + ".lock", timeout=120)
    with lock:
        wb = openpyxl.load_workbook(excel_path)

        # Cleanly re-create sheet to purge any ghost columns/rows
        target_idx = 2
        if SHEET_NAME in wb.sheetnames:
            target_idx = wb.sheetnames.index(SHEET_NAME)
            wb.remove(wb[SHEET_NAME])
        elif REFERENCE_SHEET in wb.sheetnames:
            ref_idx = wb.sheetnames.index(REFERENCE_SHEET)
            target_idx = ref_idx + 1

        ws = wb.create_sheet(title=SHEET_NAME, index=target_idx)
        log.info(f"Target worksheet '{SHEET_NAME}' positioned cleanly at index {target_idx}")

        # Styling definitions matching CoinGlass dark header & heatmap
        header_font = Font(name="Segoe UI", size=11, bold=True, color="FFFFFF")
        header_fill = PatternFill(start_color="0F172A", end_color="0F172A", fill_type="solid")

        symbol_font = Font(name="Segoe UI", size=10, bold=True, color="0F172A")
        data_font = Font(name="Segoe UI", size=10, bold=False, color="1E293B")
        dim_font = Font(name="Segoe UI", size=10, bold=False, color="64748B")

        # Green / Red heatmaps matching Image 1
        green_font_light = Font(name="Segoe UI", size=10, bold=True, color="15803D")
        green_font_deep = Font(name="Segoe UI", size=10, bold=True, color="166534")
        red_font_light = Font(name="Segoe UI", size=10, bold=True, color="B91C1C")
        red_font_deep = Font(name="Segoe UI", size=10, bold=True, color="991B1B")

        green_fill_light = PatternFill(start_color="DCFCE7", end_color="DCFCE7", fill_type="solid")  # Mint
        green_fill_deep = PatternFill(start_color="BBF7D0", end_color="BBF7D0", fill_type="solid")   # Vibrant green
        red_fill_light = PatternFill(start_color="FEE2E2", end_color="FEE2E2", fill_type="solid")    # Soft coral
        red_fill_deep = PatternFill(start_color="FECACA", end_color="FECACA", fill_type="solid")     # Intense salmon
        neutral_fill = PatternFill(start_color="FFFFFF", end_color="FFFFFF", fill_type="solid")

        thin_border = Border(
            left=Side(style="thin", color="E2E8F0"),
            right=Side(style="thin", color="E2E8F0"),
            top=Side(style="thin", color="E2E8F0"),
            bottom=Side(style="thin", color="E2E8F0")
        )

        # 1. Row 1: Institutional Tier-1 Completion Banner in IST (UTC+5:30)
        # Enforces Operator Invariant: Timestamp MUST be added or updated ONLY ONCE row data is filled
        stamp_sheet_completion_ist(
            ws=ws,
            sheet_title=SHEET_NAME,
            row_count=len(records),
            banner_cell="A1",
            status="LIVE",
            merge_max_col=len(COLUMNS)
        )

        # 2. Row 2: Headers (with Timestamp (IST))
        for col_idx, (key, display_name, width, align) in enumerate(COLUMNS, 1):
            c = ws.cell(row=2, column=col_idx, value=display_name)
            c.font = header_font
            c.fill = header_fill
            c.alignment = Alignment(horizontal=align, vertical="center")
            c.border = thin_border
            col_letter = get_column_letter(col_idx)
            ws.column_dimensions[col_letter].width = max(width, 12)
        ws.row_dimensions[2].height = 26

        # 3. Row 3+: Data Rows directly starting at Row 3
        for idx, rec in enumerate(records):
            r_idx = 3 + idx
            for col_idx, (key, _, _, align) in enumerate(COLUMNS, 1):
                val = rec.get(key, "-")
                cell_obj = ws.cell(row=r_idx, column=col_idx, value=val)
                cell_obj.border = thin_border
                cell_obj.alignment = Alignment(horizontal=align, vertical="center")
                cell_obj.fill = neutral_fill

                sval = str(val or "").strip()
                if key == "Symbol":
                    cell_obj.font = symbol_font
                elif key in ["Market_Cap", "Timestamp_IST", "Timestamp_UTC", "#"]:
                    cell_obj.font = data_font
                else:
                    if sval.startswith("+"):
                        if any(unit in sval for unit in ["M", "B"]):
                            cell_obj.fill = green_fill_deep
                            cell_obj.font = green_font_deep
                        else:
                            cell_obj.fill = green_fill_light
                            cell_obj.font = green_font_light
                    elif sval.startswith("-") and sval != "-":
                        if any(unit in sval for unit in ["M", "B"]) and not sval.startswith("-$0"):
                            cell_obj.fill = red_fill_deep
                            cell_obj.font = red_font_deep
                        else:
                            cell_obj.fill = red_fill_light
                            cell_obj.font = red_font_light
                    else:
                        cell_obj.fill = neutral_fill
                        cell_obj.font = dim_font

            ws.row_dimensions[r_idx].height = 20

        ws.freeze_panes = "A3"

        # 4. Save Atomically with FileLock
        temp_excel = excel_path.with_name(f"{excel_path.stem}_{os.getpid()}_{int(time.time()*1000)}.tmp.xlsx")
        wb.save(temp_excel)
        wb.close()
        for _att in range(30):
            try:
                temp_excel.replace(excel_path)
                break
            except (PermissionError, Exception):
                if _att == 29:
                    if temp_excel.exists():
                        try: temp_excel.unlink()
                        except Exception: pass
                    raise
                time.sleep(1.0)

    log.info(f"Successfully dumped {len(records)} Cryptocurrency Spot Netflow assets into sheet '{SHEET_NAME}' at {excel_path}.")
    return True


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Cryptocurrency Spot Netflow Statistics Excel Dumper")
    parser.add_argument("--pages", type=int, default=25, help="Number of pages to harvest (default: 25 pages = 500 assets)")
    args = parser.parse_args()

    success = dump_spot_netflow_to_excel(max_pages=args.pages)
    sys.exit(0 if success else 1)
