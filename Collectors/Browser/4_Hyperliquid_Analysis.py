#!/usr/bin/env python3
"""
Data/Excel_Modules/4_Hyperliquid_Analysis.py
===========================================
Dedicated Excel Module 4: Hyperliquid Whale Analysis.
Extracts real-time Hyperliquid Whale Monitoring & Position data from CoinGlass:
https://www.coinglass.com/hyperliquid

Features:
  1. Full Wallet Address Extraction: Captures both the display handle (e.g. 0x5b5d..60)
     and the unmasked 42-character Ethereum hex address (0x5b5d51203a0f9079f8aeb098a6523a13f298c060)
     from DOM anchor hrefs.
  2. Multi-Page Traversal: Dynamically iterates through all available pagination pages
     (default: 40 pages, 50 rows per page = up to 2,000 whale positions).
  3. Visual & Qualitative Parity: Preserves CoinGlass multi-line formatted cells (Alt+Enter)
     with institutional color-coding (Emerald Green for Long/Profit, Crimson Red for Short/Loss).
  4. Tab Hygiene: Executes in a dedicated ephemeral tab via Edge/Chrome CDP (port 9222),
     always closing it in a finally block to ensure arena.ai remains untouched.
  5. Excel Placement: Dumps cleanly into worksheet '4_Hyperliquid_Analysis' positioned at
     Index 5 in Data/feeds/<feed_name>.parquet.
"""

from __future__ import annotations

# Pure Parquet Pipeline

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

# Parquet Writer Imports
ROOT = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'Collectors' / 'Core'))
sys.path.insert(0, str(ROOT / 'Terminal' / 'Data_Factory'))
from parquet_feed_writer import write_parquet_feed, IST_TZ, UTC_TZ

try:
    import websockets
except ImportError:
    websockets = None

ROOT = pathlib.Path(__file__).resolve().parents[2]
DATA_DIR = ROOT / "Data"
SHEET_NAME = "4_Hyperliquid_Analysis"
CDP_BASE_URL = "http://127.0.0.1:9222"
TARGET_URL = "https://www.coinglass.com/hyperliquid"

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] [4_Hyperliquid_Analysis] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)
log = logging.getLogger("4_Hyperliquid_Analysis")

# Table Schema Definition: (key, header_title, col_width, horizontal_align)
COLUMNS_SCHEMA = [
    ("rank", "#", 8, "center"),
    ("user_display", "User", 16, "center"),
    ("wallet_address", "Wallet Full Address", 46, "left"),
    ("asset", "Assets", 14, "center"),
    ("side", "Side", 12, "center"),
    ("position_formatted", "Position", 22, "right"),
    ("pnl_formatted", "Unrealised PNL (%)", 22, "right"),
    ("entry_formatted", "Entry Price", 20, "right"),
    ("liq_price", "Liq.Price", 16, "right"),
    ("margin", "Margin", 16, "right"),
    ("funding_fee", "Funding Fee", 16, "right"),
    ("current_price", "Price", 16, "right"),
    ("entry_time_formatted", "Entry Time", 18, "center"),
    ("position_usd", "Position (USD)", 18, "right"),
    ("position_tokens", "Position (Tokens)", 20, "right"),
    ("pnl_usd", "Unrealised PNL (USD)", 20, "right"),
    ("pnl_pct", "Unrealised PNL (%)_Val", 18, "right"),
    ("entry_price", "Entry Price (USD)", 18, "right"),
    ("leverage", "Leverage", 14, "center"),
    ("timestamp_ist", "Timestamp (IST)", 24, "center"),
]


def open_ephemeral_tab() -> tuple[str, str]:
    """Creates a new dedicated ephemeral CoinGlass Hyperliquid tab via CDP."""
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


async def harvest_hyperliquid_whale_data(max_pages: int = 40) -> list[dict]:
    """Navigates to CoinGlass Hyperliquid, extracts whale positions across pages with full addresses."""
    if not websockets:
        raise RuntimeError("websockets package is required.")

    tab_id, ws_url = open_ephemeral_tab()
    log.info(f"Opened dedicated ephemeral tab (ID: {tab_id}) for Hyperliquid Whale harvest.")

    now_dt = datetime.datetime.now(datetime.timezone.utc)
    ist_tz = datetime.timezone(datetime.timedelta(hours=5, minutes=30))
    now_ist = datetime.datetime.now(ist_tz)
    ts_str = now_ist.strftime("%Y-%m-%d %H:%M:%S IST")

    all_records: list[dict] = []
    seen_keys: set[str] = set()

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

        async with ws:
            await asyncio.sleep(4.0)
            # 1. Wait for table DOM readiness
            readiness_js = """
            (() => {
                const table = document.querySelector('.ant-table-body table') || 
                              Array.from(document.querySelectorAll('table')).find(t => t.querySelectorAll('tbody tr').length > 0) ||
                              document.querySelectorAll('table')[document.querySelectorAll('table').length - 1];
                if (!table) return 0;
                const rows = table.querySelectorAll('tbody tr');
                return rows.length;
            })()
            """
            table_ready = False
            for _ in range(40):  # up to 20s
                res = await cdp_cmd("Runtime.evaluate", {"expression": readiness_js, "returnByValue": True})
                cnt = res.get("result", {}).get("value", 0)
                if cnt >= 20:
                    table_ready = True
                    log.info(f"Hyperliquid table detected and ready with {cnt} rows.")
                    break
                await asyncio.sleep(0.5)

            if not table_ready:
                log.warning("Table readiness timed out after 20s; attempting Page.reload...")
                await cdp_cmd("Page.reload")
                await asyncio.sleep(4.0)
                for _ in range(30):
                    res = await cdp_cmd("Runtime.evaluate", {"expression": readiness_js, "returnByValue": True})
                    cnt = res.get("result", {}).get("value", 0)
                    if cnt >= 20:
                        table_ready = True
                        log.info(f"Hyperliquid table detected after reload with {cnt} rows.")
                        break
                    await asyncio.sleep(0.5)

            # 2. Iterate through pagination pages
            extract_page_rows_js = """
            (() => {
                const table = document.querySelector('.ant-table-body table') || 
                              Array.from(document.querySelectorAll('table')).find(t => t.querySelectorAll('tbody tr').length > 0) ||
                              document.querySelectorAll('table')[document.querySelectorAll('table').length - 1];
                if (!table) return [];
                const rows = Array.from(table.querySelectorAll('tbody tr'));
                return rows.map(tr => {
                    const tds = Array.from(tr.querySelectorAll('td'));
                    if (tds.length < 10) return null;

                    const rankText = tds[1].innerText.trim();
                    if (!rankText || isNaN(parseInt(rankText))) return null;

                    const userDisplay = tds[2].innerText.replace(/\\n/g, ' ').trim();
                    const a = tds[2].querySelector('a');
                    let fullAddress = "";
                    if (a && a.href) {
                        const parts = a.href.split('/hyperliquid/');
                        if (parts.length > 1) {
                            fullAddress = parts[1].split('?')[0].split('#')[0].trim();
                        }
                    }
                    if (!fullAddress) {
                        const match = tds[2].innerHTML.match(/0x[a-fA-F0-9]{40}/);
                        if (match) fullAddress = match[0];
                    }

                    const asset = tds[3].innerText.replace(/\\n/g, ' ').trim();
                    const side = tds[4].innerText.replace(/\\n/g, ' ').trim();

                    const posDivs = Array.from(tds[5].querySelectorAll('div')).filter(d => d.children.length === 0 && d.innerText.trim());
                    const posUsd = posDivs.length > 0 ? posDivs[0].innerText.trim() : "";
                    const posToken = posDivs.length > 1 ? posDivs[1].innerText.trim() : "";
                    const posFormatted = (posUsd && posToken) ? `${posUsd}\\n${posToken}` : tds[5].innerText.trim();

                    const pnlDivs = Array.from(tds[6].querySelectorAll('div')).filter(d => d.children.length === 0 && d.innerText.trim());
                    const pnlUsd = pnlDivs.length > 0 ? pnlDivs[0].innerText.trim() : "";
                    const pnlPct = pnlDivs.length > 1 ? pnlDivs[1].innerText.trim() : "";
                    const pnlFormatted = (pnlUsd && pnlPct) ? `${pnlUsd}\\n${pnlPct}` : tds[6].innerText.trim();

                    const entryDivs = Array.from(tds[7].querySelectorAll('div')).filter(d => d.children.length === 0 && d.innerText.trim());
                    const entryPrice = entryDivs.length > 0 ? entryDivs[0].innerText.trim() : "";
                    const leverage = entryDivs.length > 1 ? entryDivs[1].innerText.trim() : "";
                    const entryFormatted = (entryPrice && leverage) ? `${entryPrice}\\n${leverage}` : tds[7].innerText.trim();

                    const liqPrice = tds[8].innerText.replace(/\\n/g, ' ').trim();
                    const margin = tds[9].innerText.replace(/\\n/g, ' ').trim();
                    const fundingFee = tds[10].innerText.replace(/\\n/g, ' ').trim();
                    const currentPrice = tds[11].innerText.replace(/\\n/g, ' ').trim();

                    const timeDivs = Array.from(tds[12].querySelectorAll('div')).filter(d => d.children.length === 0 && d.innerText.trim());
                    const timeStr = timeDivs.length > 0 ? timeDivs[0].innerText.trim() : "";
                    const dateStr = timeDivs.length > 1 ? timeDivs[1].innerText.trim() : "";
                    const entryTimeFormatted = (timeStr && dateStr) ? `${timeStr}\\n${dateStr}` : tds[12].innerText.trim();

                    return {
                        rank: rankText,
                        user_display: userDisplay,
                        wallet_address: fullAddress || userDisplay,
                        asset: asset,
                        side: side,
                        position_formatted: posFormatted,
                        position_usd: posUsd,
                        position_tokens: posToken,
                        pnl_formatted: pnlFormatted,
                        pnl_usd: pnlUsd,
                        pnl_pct: pnlPct,
                        entry_formatted: entryFormatted,
                        entry_price: entryPrice,
                        leverage: leverage,
                        liq_price: liqPrice,
                        margin: margin,
                        funding_fee: fundingFee,
                        current_price: currentPrice,
                        entry_time_formatted: entryTimeFormatted
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
                res = await cdp_cmd("Runtime.evaluate", {"expression": extract_page_rows_js, "returnByValue": True})
                rows = res.get("result", {}).get("value", [])

                page_new_count = 0
                for r in rows:
                    r["timestamp_ist"] = ts_str
                    dedup_key = f"{r.get('rank')}_{r.get('wallet_address')}_{r.get('asset')}_{r.get('side')}"
                    if dedup_key not in seen_keys:
                        seen_keys.add(dedup_key)
                        all_records.append(r)
                        page_new_count += 1

                page_elapsed = time.perf_counter() - page_start_t
                log.info(
                    f"Page {page_idx:>2}/{max_pages}: Extracted {len(rows)} positions ({page_new_count} new, Total: {len(all_records)}) in {page_elapsed:.2f}s"
                )

                if page_idx >= max_pages:
                    break

                # Advance to next page
                res_click = await cdp_cmd("Runtime.evaluate", {"expression": click_next_page_js, "returnByValue": True})
                can_advance = res_click.get("result", {}).get("value", False)

                if not can_advance:
                    log.info(f"Reached final pagination page at page {page_idx}.")
                    break

                # Wait for active page indicator to update
                target_page_str = str(page_idx + 1)
                page_updated = False
                for _ in range(25):  # up to 2.5s
                    await asyncio.sleep(0.1)
                    res_p = await cdp_cmd("Runtime.evaluate", {"expression": get_active_page_js, "returnByValue": True})
                    curr_p = res_p.get("result", {}).get("value")
                    if curr_p == target_page_str:
                        page_updated = True
                        break

                if not page_updated:
                    await asyncio.sleep(0.5)

    finally:
        close_tab(tab_id)

    log.info(f"Harvest complete: {len(all_records)} total whale positions collected across {max_pages} pages.")
    return all_records


def dump_to_parquet(records: list[dict]) -> bool:
    if not records:
        log.error("No records to dump to Parquet.")
        return False
    meta = write_parquet_feed(SHEET_NAME, records)
    log.info(f"Successfully dumped {len(records)} Hyperliquid Whale records into Parquet feed '{SHEET_NAME}': {meta.get('byte_size')} bytes in {meta.get('write_latency_ms', 0):.2f}ms.")
    return True


def main():
    parser = argparse.ArgumentParser(description="CoinGlass Hyperliquid Whale Monitoring Pure-Parquet Dumper")
    parser.add_argument("--pages", type=int, default=40, help="Number of pages to scrape (default: 40)")
    args = parser.parse_args()

    records = asyncio.run(harvest_hyperliquid_whale_data(max_pages=args.pages))
    if not records:
        log.error("No records harvested from CoinGlass Hyperliquid.")
        sys.exit(1)

    ok = dump_to_parquet(records)
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
