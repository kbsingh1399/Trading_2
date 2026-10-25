#!/usr/bin/env python3
"""
Data/Excel_Modules/7_Live_Liq.py
================================
Live CoinGlass Real-Time Liquidations Feed Scraper & Excel Dumper.
Captures all available streaming/historical liquidation orders (~1,000 orders)
from the 'Live Liquidations' virtual feed on https://www.coinglass.com/liquidations
and dumps into worksheet '7_Live_Liq' in Data/DataBase_Trading.xlsx
(positioned at Index 10, immediately after '7_Liq_Heapmap').

Columns:
  # | Coin / Pair | Side | Price | Amount | Time | Exchange | Full Timestamp (UTC)

Security & Cleanliness Invariants:
  - Ephemeral CDP tab on port 9222 opened and strictly closed in finally: block.
  - Preserves arena.ai tab untouched.
  - Zero external browser window pollution.
"""

from __future__ import annotations

try:
    import excel_lock_hook
except Exception:
    pass

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
log = logging.getLogger("7_Live_Liq")

MODULES_DIR = pathlib.Path(__file__).resolve().parent
ROOT_DIR = MODULES_DIR.parents[1]
DEFAULT_EXCEL_PATH = ROOT_DIR / "Data" / "DataBase_Trading.xlsx"
CDP_BASE_URL = "http://127.0.0.1:9222"
TARGET_URL = "https://www.coinglass.com/liquidations"
SHEET_NAME = "7_Live_Liq"

COLUMNS_DEF = [
    ("idx", "#", 8, "center"),
    ("coin", "Coin / Pair", 20, "center"),
    ("side", "Side", 14, "center"),
    ("price", "Price", 18, "right"),
    ("amount", "Amount", 18, "right"),
    ("time", "Time", 18, "center"),
    ("exchange", "Exchange", 16, "center"),
    ("full_time", "Timestamp (IST)", 24, "center"),
]


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


async def harvest_live_liquidations(max_orders: int = 1000) -> list[dict]:
    """Navigates to CoinGlass Liquidations, virtually scrolls through the Live Liquidations feed,

    and collects up to max_orders live liquidation orders.
    """
    if not websockets:
        raise RuntimeError("websockets package is required.")

    tab_id, ws_url = open_ephemeral_tab()
    log.info(f"Opened dedicated ephemeral tab (ID: {tab_id}) for Live Liquidations harvest.")

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

        # Fast virtual scroll and harvest script
        scroll_script = """
        (async () => {
            const scrollEl = document.querySelector('.lp-virtual-list, .ant-table-body, div[class*="virtual-list"], div[class*="table-body"], div[role="table"]');
            if (!scrollEl) return { error: 'No .lp-virtual-list container found' };
            
            const collectedMap = new Map();
            
            function harvestVisible() {
                const rows = document.querySelectorAll('.lp-order, tr.ant-table-row, div[role="row"]:not([role="rowheader"]), div[class*="order-row"]');
                rows.forEach(r => {
                    const idxStr = r.getAttribute('aria-rowindex');
                    if (!idxStr) return;
                    
                    const contractEl = r.querySelector('.lp-contract');
                    const title = contractEl ? (contractEl.getAttribute('title') || '') : '';
                    const parts = title.split('·').map(s => s.trim());
                    const exchange = parts[0] || '';
                    const side = parts[1] || (r.className.includes('long') ? 'Long' : (r.className.includes('short') ? 'Short' : ''));
                    const fullTime = parts[2] || '';
                    
                    const coinEl = r.querySelector('.lp-contract-name') || r.querySelector('b') || r.querySelector('span');
                    const coin = coinEl ? coinEl.innerText.trim() : '';
                    
                    const priceEl = r.querySelector('.lp-price') || r.children[1];
                    const price = priceEl ? priceEl.innerText.trim() : '';
                    
                    const amountEl = r.querySelector('.lp-amount') || r.children[2];
                    const amount = amountEl ? amountEl.innerText.trim() : '';
                    
                    const timeEl = r.querySelector('.lp-time') || r.children[3];
                    const time = timeEl ? timeEl.innerText.trim().replace(/\\n/g, ' ') : '';
                    
                    // Deduplicate key
                    const key = `${idxStr}_${coin}_${price}_${amount}_${time}`;
                    if (!collectedMap.has(key)) {
                        collectedMap.set(key, {
                            rowIndex: parseInt(idxStr, 10),
                            coin,
                            side,
                            price,
                            amount,
                            time,
                            fullTime,
                            exchange
                        });
                    }
                });
            }
            
            // Initial harvest
            harvestVisible();
            
            const maxScroll = scrollEl.scrollHeight || 52000;
            const step = 800;
            
            for (let pos = 500; pos <= maxScroll; pos += step) {
                scrollEl.scrollTop = pos;
                scrollEl.dispatchEvent(new Event('scroll'));
                await new Promise(r => setTimeout(r, 35));
                harvestVisible();
                if (collectedMap.size >= 1000) break;
            }
            
            // Convert to array sorted by rowIndex
            const allOrders = Array.from(collectedMap.values());
            allOrders.sort((a, b) => a.rowIndex - b.rowIndex);
            
            return {
                totalCount: allOrders.length,
                orders: allOrders
            };
        })()
        """

        log.info("Executing fast virtual scroll across all 1,000 Live Liquidation orders...")
        eval_res = await cdp_cmd(
            "Runtime.evaluate",
            {"expression": scroll_script, "awaitPromise": True, "returnByValue": True},
        )

        res_val = eval_res.get("result", {}).get("value", {})
        orders = res_val.get("orders", [])
        log.info(f"Successfully harvested {len(orders)} Live Liquidation orders.")

        await ws.close()

    finally:
        close_tab(tab_id)

    # Format records
    ist_tz = datetime.timezone(datetime.timedelta(hours=5, minutes=30))
    now_ist_str = datetime.datetime.now(ist_tz).strftime("%Y-%m-%d %H:%M:%S IST")
    records: list[dict] = []
    for i, o in enumerate(orders, start=1):
        raw_full = o.get("fullTime", "").strip()
        ts_val = f"{raw_full} IST" if (raw_full and "IST" not in raw_full) else (raw_full or now_ist_str)
        records.append(
            {
                "idx": i,
                "coin": o.get("coin", "-"),
                "side": o.get("side", "-"),
                "price": o.get("price", "-"),
                "amount": o.get("amount", "-"),
                "time": o.get("time", "-"),
                "exchange": o.get("exchange", "-"),
                "full_time": ts_val,
            }
        )

    return records


def dump_to_excel(records: list[dict], excel_path: pathlib.Path = DEFAULT_EXCEL_PATH) -> bool:
    """Dumps live liquidation feed into worksheet '7_Live_Liq'."""
    if not excel_path.exists():
        log.error(f"Excel workbook not found at: {excel_path}")
        return False

    if not records:
        log.error("Integrity guard: 0 records extracted. Aborting dump to prevent empty sheet.")
        return False

    try:
        from filelock import FileLock
        lock = FileLock(str(excel_path) + ".lock", timeout=120)
    except ImportError:
        lock = None

    class _NoLock:
        def __enter__(self): return self
        def __exit__(self, *args): pass

    with (lock if lock else _NoLock()):
        wb = openpyxl.load_workbook(excel_path)

        # Place sheet 7_Live_Liq at Index 10 (immediately after 7_Liq_Heapmap)
        if SHEET_NAME in wb.sheetnames:
            idx = wb.sheetnames.index(SHEET_NAME)
            wb.remove(wb[SHEET_NAME])
            ws = wb.create_sheet(title=SHEET_NAME, index=idx)
        else:
            target_idx = 10 if len(wb.sheetnames) >= 10 else len(wb.sheetnames)
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
        row_border = Border(
            left=thin_border_side, right=thin_border_side, top=thin_border_side, bottom=thin_border_side
        )

        # 1. Header Row (Row 2, Row 1 reserved for Banner)
        ws.row_dimensions[2].height = 26
        for col_idx, (col_key, header_title, width, align) in enumerate(COLUMNS_DEF, start=1):
            cell = ws.cell(row=2, column=col_idx, value=header_title)
            cell.font = hdr_font
            cell.fill = hdr_fill
            cell.alignment = Alignment(horizontal=align, vertical="center")
            cell.border = row_border
            col_letter = get_column_letter(col_idx)
            ws.column_dimensions[col_letter].width = width

        # 2. Data Rows (Row 3+)
        current_row = 3
        for r in records:
            ws.row_dimensions[current_row].height = 20

            # # (Col 1)
            c1 = ws.cell(row=current_row, column=1, value=r.get("idx", ""))
            c1.font = subdued_font
            c1.alignment = Alignment(horizontal="center", vertical="center")
            c1.border = row_border

            # Coin / Pair (Col 2)
            c2 = ws.cell(row=current_row, column=2, value=r.get("coin", "-"))
            c2.font = bold_font
            c2.alignment = Alignment(horizontal="center", vertical="center")
            c2.border = row_border

            # Side (Col 3) - Color Coded
            side_val = r.get("side", "-")
            c3 = ws.cell(row=current_row, column=3, value=side_val)
            if "long" in side_val.lower():
                c3.font = green_font
            elif "short" in side_val.lower():
                c3.font = red_font
            else:
                c3.font = base_font
            c3.alignment = Alignment(horizontal="center", vertical="center")
            c3.border = row_border

            # Price (Col 4)
            c4 = ws.cell(row=current_row, column=4, value=r.get("price", "-"))
            c4.font = base_font
            c4.alignment = Alignment(horizontal="right", vertical="center")
            c4.border = row_border

            # Amount (Col 5)
            c5 = ws.cell(row=current_row, column=5, value=r.get("amount", "-"))
            c5.font = bold_font
            c5.alignment = Alignment(horizontal="right", vertical="center")
            c5.border = row_border

            # Time (Col 6)
            c6 = ws.cell(row=current_row, column=6, value=r.get("time", "-"))
            c6.font = base_font
            c6.alignment = Alignment(horizontal="center", vertical="center")
            c6.border = row_border

            # Exchange (Col 7)
            c7 = ws.cell(row=current_row, column=7, value=r.get("exchange", "-"))
            c7.font = bold_font
            c7.alignment = Alignment(horizontal="center", vertical="center")
            c7.border = row_border

            # Full Timestamp (Col 8)
            c8 = ws.cell(row=current_row, column=8, value=r.get("full_time", "-"))
            c8.font = subdued_font
            c8.alignment = Alignment(horizontal="center", vertical="center")
            c8.border = row_border

            current_row += 1

        # Stamp Tier-1 Completion Banner ONLY ONCE row data is filled
        try:
            from logger_config import stamp_sheet_completion_ist
            stamp_sheet_completion_ist(
                ws=ws,
                sheet_title=SHEET_NAME,
                row_count=len(records),
                banner_cell="A1",
                status="LIVE",
                merge_max_col=len(COLUMNS_DEF)
            )
        except Exception as _e:
            log.warning(f"Error stamping banner: {_e}")

        ws.freeze_panes = "A3"

        import os, time
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
        log.info(f"Successfully saved {len(records)} rows to {excel_path} [{SHEET_NAME}].")
        return True


def main():
    parser = argparse.ArgumentParser(description="CoinGlass Live Liquidations Feed Scraper")
    parser.add_argument(
        "--excel-path",
        type=pathlib.Path,
        default=DEFAULT_EXCEL_PATH,
        help="Path to DataBase_Trading.xlsx",
    )
    args = parser.parse_args()

    records = asyncio.run(harvest_live_liquidations())
    if not records:
        log.error("No records harvested from Live Liquidations feed.")
        sys.exit(1)

    success = dump_to_excel(records, args.excel_path)
    if not success:
        log.error("Failed to dump data to Excel.")
        sys.exit(1)

    log.info("7_Live_Liq module completed successfully.")


if __name__ == "__main__":
    main()
