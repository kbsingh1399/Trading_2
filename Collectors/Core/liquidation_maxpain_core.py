#!/usr/bin/env python3
"""
Collectors/Core/liquidation_maxpain_core.py
===========================================
Shared Core Extraction & Parquet Writing Engine for CoinGlass Liquidation Max Pain Feeds:
  - 9_Liquidation_Max_Pain_24H.parquet (24H timeframe: '24 hour')
  - 9_Liquidation_Max_Pain_48H.parquet (48H timeframe: '48 hour')
  - 9_Liquidation_Max_Pain_3D.parquet  (3D timeframe:  '3 day')
  - 9_Liquidation_Max_Pain_7D.parquet  (7D timeframe:  '1 week')

Target Page: https://www.coinglass.com/liquidation-maxpain
Extracts 100% of candidates (~747 multi-asset items across 15 pages) with single-session tab rotation.
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
from typing import Any, Dict, List, Optional, Tuple

ROOT = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'Collectors' / 'Core'))
sys.path.insert(0, str(ROOT / 'Terminal' / 'Data_Factory'))
from parquet_feed_writer import write_parquet_feed, IST_TZ, UTC_TZ

try:
    import websockets
except ImportError:
    websockets = None

CDP_BASE_URL = "http://127.0.0.1:9222"
TARGET_URL = "https://www.coinglass.com/liquidation-maxpain"

MAXPAIN_TIMEFRAMES = [
    ("24H", "24 hour", "9_Liquidation_Max_Pain_24H"),
    ("48H", "48 hour", "9_Liquidation_Max_Pain_48H"),
    ("3D", "3 day", "9_Liquidation_Max_Pain_3D"),
    ("7D", "1 week", "9_Liquidation_Max_Pain_7D"),
]

COLUMNS_DEF = [
    ("ranking", "Ranking", 10, "center"),
    ("symbol", "Symbol", 12, "center"),
    ("price", "Price", 18, "right"),
    ("short_max_pain_price", "Short Max Pain Price", 22, "right"),
    ("short_max_pain_vol", "Short Max Pain Vol", 20, "right"),
    ("short_distance_usd", "Short Distance ($)", 20, "right"),
    ("short_distance_pct", "Short Distance (%)", 20, "right"),
    ("long_max_pain_price", "Long Max Pain Price", 22, "right"),
    ("long_max_pain_vol", "Long Max Pain Vol", 20, "right"),
    ("long_distance_usd", "Long Distance ($)", 20, "right"),
    ("long_distance_pct", "Long Distance (%)", 20, "right"),
    ("timestamp_ist", "Timestamp (IST)", 24, "center"),
]


def format_currency(val: float | None) -> str:
    """Formats price into clean currency string with adaptive precision matching CoinGlass UI."""
    if val is None:
        return "$0.00"
    abs_val = abs(val)
    if abs_val >= 1000:
        return f"${val:,.2f}"
    elif abs_val >= 1:
        s = f"{val:.4f}".rstrip("0")
        if s.endswith("."):
            s += "00"
        elif len(s.split(".")[1]) < 2:
            s += "0"
        return f"${s}"
    elif abs_val >= 0.0001:
        s = f"{val:.6f}".rstrip("0")
        return f"${s}"
    else:
        return f"${val:.8f}"


def format_vol(val: float | None) -> str:
    """Formats notional volume into human-readable compact currency string ($M, $K, $B)."""
    if val is None or val == 0:
        return "$0.00"
    abs_val = abs(val)
    if abs_val >= 1e9:
        return f"${val / 1e9:.2f}B"
    elif abs_val >= 1e6:
        return f"${val / 1e6:.2f}M"
    elif abs_val >= 1e3:
        return f"${val / 1e3:.2f}K"
    else:
        return f"${val:.2f}"


def format_distance_usd(val: float | None) -> str:
    """Formats USD distance with explicit sign prefix."""
    if val is None or val == 0:
        return "$0.00"
    abs_val = abs(val)
    if abs_val >= 1000:
        sign = "+" if val > 0 else "-"
        return f"{sign}${abs_val:,.2f}"
    elif abs_val >= 1:
        sign = "+" if val > 0 else "-"
        s = f"{abs_val:.4f}".rstrip("0")
        if s.endswith("."):
            s += "00"
        elif len(s.split(".")[1]) < 2:
            s += "0"
        return f"{sign}${s}"
    else:
        sign = "+" if val > 0 else "-"
        s = f"{abs_val:.6f}".rstrip("0")
        return f"{sign}${s}"


def format_distance_pct(val: float | None) -> str:
    """Formats percentage distance with explicit sign prefix."""
    if val is None or val == 0:
        return "0.00%"
    sign = "+" if val > 0 else ""
    return f"{sign}{val:.2f}%"


def get_or_open_tab(target_url: str = TARGET_URL, cdp_base_url: str = CDP_BASE_URL) -> Tuple[str, str, bool]:
    """Finds an existing Liquidation Max Pain tab or creates a dedicated ephemeral tab."""
    try:
        req = urllib.request.Request(f"{cdp_base_url}/json")
        tabs = json.loads(urllib.request.urlopen(req, timeout=5).read().decode())
        for t in tabs:
            if "liquidation-maxpain" in t.get("url", ""):
                return t["id"], t["webSocketDebuggerUrl"], False
    except Exception:
        pass

    req = urllib.request.Request(f"{cdp_base_url}/json/new?{target_url}", method="PUT")
    new_tab = json.loads(urllib.request.urlopen(req, timeout=10).read().decode())
    return new_tab["id"], new_tab["webSocketDebuggerUrl"], True


def close_tab(tab_id: str, cdp_base_url: str = CDP_BASE_URL, log: logging.Logger = None):
    """Closes ephemeral tab via CDP, strictly preserving other tabs."""
    try:
        urllib.request.urlopen(f"{cdp_base_url}/json/close/{tab_id}", timeout=5)
        if log:
            log.info(f"Closed ephemeral tab {tab_id}")
    except Exception as e:
        if log:
            log.warning(f"Error closing tab {tab_id}: {e}")


async def harvest_all_maxpain_timeframes_unified(
    cdp_base_url: str = CDP_BASE_URL,
    target_url: str = TARGET_URL,
    log: logging.Logger = None,
) -> dict[str, int]:
    """
    Connects to CoinGlass /liquidation-maxpain once, rotates through all 4 timeframes
    ('24 hour', '48 hour', '3 day', '1 week'), extracts 100% of candidates (~747 assets)
    for each, and writes immediately to respective Parquet feeds.
    """
    if not websockets:
        raise RuntimeError("websockets package is required.")

    if log is None:
        log = logging.getLogger("LiquidationMaxPainCore")

    tab_id, ws_url, is_ephemeral = get_or_open_tab(target_url, cdp_base_url)
    log.info(f"Connected to CoinGlass Max Pain tab (ID: {tab_id}, is_ephemeral={is_ephemeral}).")

    t0 = time.time()
    results: dict[str, int] = {}

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

        msg_id = 1

        async def cdp_cmd(method: str, params: dict | None = None) -> dict:
            nonlocal msg_id
            curr_id = msg_id
            msg_id += 1
            payload = {"id": curr_id, "method": method, "params": params or {}}
            await ws.send(json.dumps(payload))
            while True:
                resp = json.loads(await ws.recv())
                if resp.get("id") == curr_id:
                    return resp.get("result", {}).get("result", {})

        # Hydration check
        hydrated = False
        for attempt in range(30):
            js_check = """
            (() => {
                const table = document.querySelector('.ant-table');
                if (!table) return false;
                const fiberKey = Object.keys(table).find(k => k.startsWith('__reactFiber$'));
                if (!fiberKey) return false;
                let cur = table[fiberKey];
                while (cur) {
                    if (cur.memoizedProps && cur.memoizedProps.dataSource && cur.memoizedProps.dataSource.length > 0) {
                        return true;
                    }
                    cur = cur.return;
                }
                return false;
            })()
            """
            res = await cdp_cmd("Runtime.evaluate", {"expression": js_check, "returnByValue": True})
            if res.get("value") is True:
                hydrated = True
                log.info(f"Table hydrated successfully in {time.time() - t0:.2f}s.")
                break
            await asyncio.sleep(0.5)

        if not hydrated:
            raise TimeoutError(f"CoinGlass table failed to hydrate within timeout on tab {tab_id}")

        js_extract = """
        (() => {
            const table = document.querySelector('.ant-table');
            if (!table) return { error: "No table element" };
            const fiberKey = Object.keys(table).find(k => k.startsWith('__reactFiber$'));
            if (!fiberKey) return { error: "No fiberKey" };
            let cur = table[fiberKey];
            while (cur) {
                if (cur.memoizedProps && cur.memoizedProps.dataSource && cur.memoizedProps.dataSource.length > 0) {
                    const ds = cur.memoizedProps.dataSource;
                    return {
                        success: true,
                        count: ds.length,
                        records: ds.map((item, idx) => {
                            const price = item.price;
                            const sPrice = item.maxLongLiquidationPrice;
                            const sVol = item.maxLongLiquidationLevel;
                            const lPrice = item.maxShortLiquidationPrice;
                            const lVol = item.maxShortLiquidationLevel;
                            
                            const sDistUsd = (sPrice != null && price != null) ? (sPrice - price) : null;
                            const sDistPct = (sDistUsd != null && price) ? (sDistUsd / price) * 100 : null;
                            
                            const lDistUsd = (lPrice != null && price != null) ? (lPrice - price) : null;
                            const lDistPct = (lDistUsd != null && price) ? (lDistUsd / price) * 100 : null;
                            
                            return {
                                ranking: idx + 1,
                                symbol: item.symbol || '',
                                price: price,
                                short_max_pain_price: sPrice,
                                short_max_pain_vol: sVol,
                                short_distance_usd: sDistUsd,
                                short_distance_pct: sDistPct,
                                long_max_pain_price: lPrice,
                                long_max_pain_vol: lVol,
                                long_distance_usd: lDistUsd,
                                long_distance_pct: lDistPct
                            };
                        })
                    };
                }
                cur = cur.return;
            }
            return { error: "No dataSource found in React Fiber tree" };
        })()
        """

        # Rotate through all 4 timeframes in this single tab session
        for tf_code, tf_label, feed_name in MAXPAIN_TIMEFRAMES:
            log.info(f"Rotating to timeframe '{tf_label}' ({tf_code}) -> Feed '{feed_name}'...")

            js_switch = f"""
            (() => {{
                const targetLabel = {json.dumps(tf_label)}.toLowerCase().trim();
                const candidates = Array.from(document.querySelectorAll('button[role="tab"], div[role="tab"], .ant-tabs-tab, button.MuiTab-root, div.MuiTab-root'));
                let targetTab = candidates.find(t => t.innerText.trim().toLowerCase() === targetLabel);
                if (!targetTab) {{
                    targetTab = candidates.find(t => t.innerText.trim().toLowerCase().includes(targetLabel));
                }}
                if (!targetTab) return {{ error: "Tab not found: " + targetLabel }};
                
                const isSelected = targetTab.getAttribute('aria-selected') === 'true' || 
                                   targetTab.classList.contains('Mui-selected') || 
                                   targetTab.classList.contains('ant-tabs-tab-active');
                if (!isSelected) {{
                    targetTab.click();
                    return {{ clicked: true, selected: false }};
                }}
                return {{ clicked: false, selected: true }};
            }})()
            """
            switch_res = await cdp_cmd("Runtime.evaluate", {"expression": js_switch, "returnByValue": True})
            switch_val = switch_res.get("value", {})
            if switch_val.get("clicked"):
                await asyncio.sleep(1.2)
            else:
                await asyncio.sleep(0.3)

            # Actively rotate through all pagination pages for this timeframe
            js_paginate = """
            (async () => {
                const pagination = document.querySelector('ul.ant-pagination');
                if (!pagination) return { totalPages: 1, rotated: 1 };
                
                const items = Array.from(pagination.querySelectorAll('.ant-pagination-item'));
                const pageNumbers = items.map(it => parseInt(it.innerText.trim())).filter(n => !isNaN(n));
                const maxPage = Math.max(...pageNumbers, 1);
                
                let count = 0;
                for (let p = 1; p <= maxPage; p++) {
                    const btn = Array.from(pagination.querySelectorAll('.ant-pagination-item')).find(it => it.innerText.trim() === String(p));
                    if (btn) {
                        btn.click();
                        count++;
                    } else {
                        const nextBtn = pagination.querySelector('.ant-pagination-next button, .ant-pagination-next');
                        if (nextBtn) {
                            nextBtn.click();
                            count++;
                        }
                    }
                    await new Promise(r => setTimeout(r, 180));
                }
                
                // Reset to page 1
                const p1 = Array.from(pagination.querySelectorAll('.ant-pagination-item')).find(it => it.innerText.trim() === '1');
                if (p1) p1.click();
                await new Promise(r => setTimeout(r, 200));
                
                return { totalPages: maxPage, rotated: count };
            })()
            """
            pag_res = await cdp_cmd("Runtime.evaluate", {"expression": js_paginate, "awaitPromise": True, "returnByValue": True})
            pag_val = pag_res.get("value", {})
            log.info(f"  -> [{tf_code}] Paginated through all {pag_val.get('rotated', 1)}/{pag_val.get('totalPages', 1)} pages.")

            extract_res = await cdp_cmd("Runtime.evaluate", {"expression": js_extract, "returnByValue": True})
            extract_val = extract_res.get("value", {})
            records = extract_val.get("records", [])

            if records:
                meta = write_parquet_feed(feed_name, records)
                results[feed_name] = len(records)
                log.info(f"  -> Dumped {len(records)} assets to '{feed_name}.parquet' (Size: {meta.get('byte_size')}B)")
            else:
                log.warning(f"  -> No records extracted for {feed_name}")

        await ws.close()

    finally:
        if is_ephemeral:
            close_tab(tab_id, cdp_base_url, log)

    total_time = time.time() - t0
    log.info(f"Single-session unified Max Pain rotation complete in {total_time:.2f}s across {len(results)} feeds.")
    return results


async def harvest_liquidation_maxpain(
    timeframe_code: str,
    timeframe_label: str,
    cdp_base_url: str = CDP_BASE_URL,
    target_url: str = TARGET_URL,
    log: logging.Logger = None,
) -> List[Dict[str, Any]]:
    """Harvests a single timeframe."""
    results = await harvest_all_maxpain_timeframes_unified(cdp_base_url, target_url, log)
    feed_target = f"9_Liquidation_Max_Pain_{timeframe_code}"
    # Read the parquet directly
    parquet_path = ROOT / "Data" / "feeds" / f"{feed_target}.parquet"
    if parquet_path.exists():
        import pyarrow.parquet as pq
        table = pq.read_table(str(parquet_path))
        return table.to_pylist()
    return []


def run_maxpain_harvest(
    timeframe_code: str,
    timeframe_label: str,
    sheet_name: str,
    target_index: int,
    log_name: str,
):
    """CLI orchestrator entrypoint for Max Pain module."""
    parser = argparse.ArgumentParser(description=f"CoinGlass Liquidation Max Pain {timeframe_code} Parquet Dumper")
    parser.add_argument("--cdp-url", type=str, default=CDP_BASE_URL)
    parser.add_argument("--force", action="store_true", help="Force harvest even if feed is fresh")
    args = parser.parse_args()

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] [%(name)s] %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )
    log = logging.getLogger(log_name)

    parquet_path = ROOT / "Data" / "feeds" / f"{sheet_name}.parquet"
    now_ts = time.time()

    # Fast cache bypass: If feed was updated within last 90 seconds and not forced, reuse fresh parquet
    if not args.force and parquet_path.exists():
        age_sec = now_ts - os.path.getmtime(parquet_path)
        if age_sec < 90.0:
            log.info(f"Feed '{sheet_name}' is already fresh ({age_sec:.1f}s old). Skipping redundant tab hydration.")
            sys.exit(0)

    log.info(f"Starting {log_name} [{timeframe_code} - '{timeframe_label}'] -> Feed '{sheet_name}'...")
    try:
        # Run unified rotation which updates all 4 feeds in one single tab session
        results = asyncio.run(harvest_all_maxpain_timeframes_unified(cdp_base_url=args.cdp_url, log=log))
        if sheet_name not in results or results[sheet_name] == 0:
            log.error(f"Harvest for {sheet_name} returned 0 records.")
            sys.exit(1)

        log.info(f"Unified harvest finished successfully. Feed '{sheet_name}' updated.")
        sys.exit(0)
    except Exception as exc:
        log.exception(f"Unhandled error in {log_name}: {exc}")
        sys.exit(1)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="CoinGlass Max Pain Unified Rotator")
    parser.add_argument("--rotate-all-tabs", action="store_true", default=True)
    args = parser.parse_args()
    logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
    asyncio.run(harvest_all_maxpain_timeframes_unified())
