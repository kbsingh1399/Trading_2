#!/usr/bin/env python3
"""
Collectors/Browser/6_Funding_Fee_Settlement.py
=============================================
Live CoinGlass Perpetual Futures Funding Fee Settlement Data Scraper & Parquet Dumper.
Scrapes the complete Funding Fee Settlement Overview across all market pairs (~937+ crypto pairs)
from https://www.coinglass.com/funding-fees with tab rotation across timeframes:
Current, 24 hour, 3 day, 7 day.
Writes atomically to Data/feeds/6_Funding_Fee_Settlement.parquet.

Security & Cleanliness Invariants:
  - Ephemeral/Reused CDP tab on port 9222.
  - Tab rotation through timeframe tabs: Current, 24 hour, 3 day, 7 day.
  - Direct React Fiber extraction dumping 100% of available market assets in seconds.
  - Preserves arena.ai tab untouched.
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
from typing import Any, Dict, List, Optional

try:
    import websockets
except ImportError:
    websockets = None

MODULES_DIR = pathlib.Path(__file__).resolve().parent
ROOT_DIR = MODULES_DIR.parents[1]
sys.path.insert(0, str(ROOT_DIR / "Collectors" / "Core"))
sys.path.insert(0, str(ROOT_DIR / "Terminal" / "Data_Factory"))

try:
    from parquet_writer import write_parquet_feed
except ImportError:
    from parquet_feed_writer import write_parquet_feed

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] [6_Funding_Fee_Settlement] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
log = logging.getLogger("6_Funding_Fee_Settlement")

CDP_BASE_URL = "http://127.0.0.1:9222"
TARGET_URL = "https://www.coinglass.com/funding-fees"
FEED_NAME = "6_Funding_Fee_Settlement"

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

IST_TZ = datetime.timezone(datetime.timedelta(hours=5, minutes=30))


def fmt_usd(val: float | None) -> str:
    """Formats numeric USD value into shorthand currency (e.g. '$1.16M' or '-$379.23K')."""
    if val is None or val != val:
        return "-"
    if val == 0:
        return "$0.00"
    sign = "-" if val < 0 else ""
    abs_v = abs(val)
    if abs_v >= 1e9:
        return f"{sign}${abs_v / 1e9:.2f}B"
    elif abs_v >= 1e6:
        return f"{sign}${abs_v / 1e6:.2f}M"
    elif abs_v >= 1e3:
        return f"{sign}${abs_v / 1e3:.2f}K"
    else:
        return f"{sign}${abs_v:.2f}"


def fmt_price(val: float | None) -> str:
    """Formats price with appropriate precision."""
    if val is None or val != val:
        return "-"
    if val >= 1000:
        return f"${val:,.2f}"
    elif val >= 1:
        return f"${val:.4f}"
    else:
        return f"${val:.6f}"


def fmt_pct(val: float | None) -> str:
    """Formats percentage change."""
    if val is None or val != val:
        return "-"
    return f"{val:+.2f}%"


def get_target_tab() -> tuple[str, str, bool]:
    """Finds existing Funding Fees tab or opens dedicated ephemeral tab."""
    try:
        req = urllib.request.Request(f"{CDP_BASE_URL}/json")
        tabs = json.loads(urllib.request.urlopen(req, timeout=5).read().decode())
        for t in tabs:
            if "funding-fees" in t.get("url", ""):
                log.info(f"Reusing active CoinGlass Funding Fees tab (ID: {t['id']}).")
                return t["id"], t["webSocketDebuggerUrl"], False
    except Exception as e:
        log.warning(f"Failed to query existing tabs: {e}")

    req = urllib.request.Request(f"{CDP_BASE_URL}/json/new?{TARGET_URL}", method="PUT")
    new_tab = json.loads(urllib.request.urlopen(req, timeout=10).read().decode())
    log.info(f"Opened dedicated ephemeral tab (ID: {new_tab['id']}).")
    return new_tab["id"], new_tab["webSocketDebuggerUrl"], True


def close_tab(tab_id: str):
    """Closes tab via CDP."""
    try:
        urllib.request.urlopen(f"{CDP_BASE_URL}/json/close/{tab_id}", timeout=4)
        log.info(f"Closed ephemeral tab {tab_id}")
    except Exception as e:
        log.warning(f"Error closing tab {tab_id}: {e}")


async def harvest_funding_fee_settlements() -> list[dict]:
    """Harvests CoinGlass Funding Fee Settlement Data with tab rotation across all 4 timeframes."""
    if not websockets:
        raise RuntimeError("websockets package is required.")

    tab_id, ws_url, is_ephemeral = get_target_tab()
    now_ist = datetime.datetime.now(IST_TZ).strftime("%Y-%m-%d %H:%M:%S IST")

    records: list[dict] = []

    try:
        ws = None
        for attempt in range(10):
            try:
                ws = await websockets.connect(ws_url, max_size=25 * 1024 * 1024, open_timeout=15)
                break
            except Exception as e:
                log.warning(f"Connect attempt {attempt+1} failed: {e}. Retrying in 1s...")
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

        if is_ephemeral:
            log.info("Awaiting Funding Fees page hydration (3.5s)...")
            await asyncio.sleep(3.5)

        # Tab Rotation Function
        async def click_tab(tab_label: str) -> bool:
            js_tab = f"""
            (() => {{
                const tabs = Array.from(document.querySelectorAll('[role="tab"]'));
                const target = tabs.find(t => t.innerText && t.innerText.trim() === '{tab_label}');
                if (target) {{
                    target.click();
                    return true;
                }}
                return false;
            }})()
            """
            res = await cdp_cmd("Runtime.evaluate", {"expression": js_tab, "returnByValue": True})
            return bool(res.get("result", {}).get("value"))

        # Perform tab rotation through all 4 timeframes: Current, 24 hour, 3 day, 7 day
        timeframe_tabs = ["Current", "24 hour", "3 day", "7 day"]
        for tname in timeframe_tabs:
            clicked = await click_tab(tname)
            log.info(f"Tab rotation -> '{tname}' (clicked: {clicked})")
            await asyncio.sleep(0.3)

        # Ensure return to 'Current'
        await click_tab("Current")
        await asyncio.sleep(0.3)

        # In-memory React Fiber extraction for all available assets
        js_extract = """
        (() => {
            const table = document.querySelector('table');
            if (!table) return null;
            const fiberKey = Object.keys(table).find(k => k.startsWith('__reactFiber$') || k.startsWith('__reactInternalInstance$'));
            let cur = table[fiberKey];
            while (cur) {
                if (cur.memoizedProps && cur.memoizedProps.dataSource) {
                    return JSON.stringify(cur.memoizedProps.dataSource);
                }
                cur = cur.return;
            }
            return null;
        })()
        """

        raw_data = None
        for _ in range(30):
            res = await cdp_cmd("Runtime.evaluate", {"expression": js_extract, "returnByValue": True})
            val = res.get("result", {}).get("value")
            if val:
                raw_data = json.loads(val)
                if len(raw_data) >= 10:
                    break
            await asyncio.sleep(0.2)

        if not raw_data:
            raise RuntimeError("Failed to extract Funding Fees dataSource from React Fiber.")

        log.info(f"Successfully extracted {len(raw_data)} assets from Funding Fees React Fiber.")

        for idx, item in enumerate(raw_data, start=1):
            sym = item.get("symbol")
            if not sym:
                continue

            last_24h_val = (item.get("longFlowUsd1d") or 0.0) + (item.get("shortFlowUsd1d") or 0.0)
            last_3d_val = (item.get("longFlowUsd3d") or 0.0) + (item.get("shortFlowUsd3d") or 0.0)
            last_7d_val = (item.get("longFlowUsd7d") or 0.0) + (item.get("shortFlowUsd7d") or 0.0)

            records.append({
                "rank": idx,
                "symbol": sym,
                "price": fmt_price(item.get("price")),
                "price_24h_pct": fmt_pct(item.get("priceChangePercent24h")),
                "open_interest": fmt_usd(item.get("openInterest")),
                "current": fmt_usd(item.get("flowUsd")),
                "last_24h": fmt_usd(last_24h_val),
                "last_3d": fmt_usd(last_3d_val),
                "last_7d": fmt_usd(last_7d_val),
                "timestamp_ist": now_ist,
            })

        await ws.close()

    finally:
        close_tab(tab_id)

    log.info(f"Total Funding Fee Settlement records harvested: {len(records)} assets.")
    return records


def main():
    parser = argparse.ArgumentParser(description="CoinGlass Funding Fee Settlement Scraper")
    args = parser.parse_args()

    log.info("Starting Funding Fee Settlement harvest with tab rotation...")
    records = asyncio.run(harvest_funding_fee_settlements())

    if not records:
        log.error("Harvesting yielded 0 records. Process aborted.")
        sys.exit(1)

    # Pure Atomic Parquet Dump
    meta = write_parquet_feed(FEED_NAME, records)
    log.info(f"Successfully dumped feed to Parquet: {meta}")
    log.info("Funding Fee Settlement pipeline executed successfully.")


if __name__ == "__main__":
    main()
