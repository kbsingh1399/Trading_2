#!/usr/bin/env python3
"""
Data/Excel_Modules/6_Funding_Fee_Settlement.py
=============================================
Live CoinGlass Perpetual Futures Funding Fee Settlement Data Scraper & Excel Dumper.
Scrapes the complete 'Funding Fee Settlement Overview' table across all 19 pages (~950+ crypto pairs)
from https://www.coinglass.com/funding-fees and dumps into worksheet '6_Funding_Fee_Settlement'
in Data/feeds/<feed_name>.parquet (positioned at Index 8, immediately after '5_Funding_Rate').

Security & Cleanliness Invariants:
  - Ephemeral CDP tab on port 9222 opened and strictly closed in finally: block.
  - Preserves arena.ai tab untouched.
  - Zero external browser window pollution.
"""

from __future__ import annotations

import pathlib
import sys
ROOT_DIR_FOR_PQ = pathlib.Path(__file__).resolve().parents[2]
if str(ROOT_DIR_FOR_PQ / "Collectors" / "Core") not in sys.path:
    sys.path.insert(0, str(ROOT_DIR_FOR_PQ / "Collectors" / "Core"))
if str(ROOT_DIR_FOR_PQ / "Terminal" / "Data_Factory") not in sys.path:
    sys.path.insert(0, str(ROOT_DIR_FOR_PQ / "Terminal" / "Data_Factory"))
from parquet_feed_writer import write_parquet_feed, IST_TZ, UTC_TZ


# Pure Parquet Pipeline

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


async def harvest_funding_fee_settlements(max_pages: int = 19) -> list[dict]:
    """Navigates to CoinGlass Funding Fees, extracts all rows across all pagination pages."""
    if not websockets:
        raise RuntimeError("websockets package is required.")

    tab_id, ws_url = open_ephemeral_tab()
    log.info(f"Opened dedicated ephemeral tab (ID: {tab_id}) for Funding Fee Settlement harvest.")

    now_dt = datetime.datetime.now(datetime.timezone.utc)
    ist_tz = datetime.timezone(datetime.timedelta(hours=5, minutes=30))
    now_ist = datetime.datetime.now(ist_tz)
    ts_str = now_ist.strftime("%Y-%m-%d %H:%M:%S IST")

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
                        r["timestamp_ist"] = ts_str
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


def dump_to_parquet(records: list[dict]) -> bool:
    if not records:
        log.error("No records to dump to Parquet.")
        return False
    meta = write_parquet_feed(SHEET_NAME, records)
    log.info(f"Successfully dumped {len(records)} Funding Fee Settlement records into Parquet feed '{SHEET_NAME}': {meta.get('byte_size')} bytes in {meta.get('write_latency_ms', 0):.2f}ms.")
    return True


def main():
    parser = argparse.ArgumentParser(description="CoinGlass Perpetual Futures Funding Fee Settlement Pure-Parquet Dumper")
    parser.add_argument("--pages", type=int, default=19, help="Number of pages to harvest (default: 19)")
    args = parser.parse_args()

    start_time = time.perf_counter()
    records = asyncio.run(harvest_funding_fee_settlements(max_pages=args.pages))

    if not records:
        log.error("No funding fee settlement records harvested. Aborting Parquet dump.")
        sys.exit(1)

    success = dump_to_parquet(records)
    elapsed = time.perf_counter() - start_time
    log.info(f"Finished in {elapsed:.2f} seconds with status: {'SUCCESS' if success else 'FAILED'}")
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
