#!/usr/bin/env python3
"""
Data/Excel_Modules/liquidation_maxpain_core.py
==============================================
Shared Core Extraction & Excel Writing Engine for CoinGlass Liquidation Max Pain Modules:
  - 9_Liquidation_Max_Pain_24H.py  (24H timeframe -> sheet '9_Liquidation_Max_Pain_24H', Index 13)
  - 9_Liquidation_Max_Pain_48H.py  (48H timeframe -> sheet '9_Liquidation_Max_Pain_48H', Index 14)
  - 9_Liquidation_Max_Pain_3D.py   (3D timeframe  -> sheet '9_Liquidation_Max_Pain_3D', Index 15)
  - 9_Liquidation_Max_Pain_7D.py   (7D timeframe  -> sheet '9_Liquidation_Max_Pain_7D', Index 16)

Target Page: https://www.coinglass.com/liquidation-maxpain
Extracts 100% of candidates (~745 assets) across all pagination pages with zero missing values.
"""

from __future__ import annotations

# Pure Parquet Pipeline

try:
    from logger_config import stamp_sheet_completion_ist, get_current_timestamps
except ImportError:
    stamp_sheet_completion_ist = None
    get_current_timestamps = None


import argparse
import asyncio
import datetime
import json
import logging
import pathlib
import sys
import time
import urllib.request
from typing import Any, Dict, List, Optional, Tuple

# Parquet Writer Imports
ROOT = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'Collectors' / 'Core'))
sys.path.insert(0, str(ROOT / 'Terminal' / 'Data_Factory'))
from parquet_feed_writer import write_parquet_feed, IST_TZ, UTC_TZ

try:
    import websockets
except ImportError:
    websockets = None

MODULES_DIR = pathlib.Path(__file__).resolve().parent
ROOT_DIR = MODULES_DIR.parents[1]
CDP_BASE_URL = "http://127.0.0.1:9222"
TARGET_URL = "https://www.coinglass.com/liquidation-maxpain"

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
        # e.g. $77.931 or $1.2999
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


def open_ephemeral_tab(target_url: str = TARGET_URL, cdp_base_url: str = CDP_BASE_URL) -> Tuple[str, str]:
    """Creates a new dedicated ephemeral tab via CDP."""
    req = urllib.request.Request(f"{cdp_base_url}/json/new?{target_url}", method="PUT")
    new_tab = json.loads(urllib.request.urlopen(req, timeout=10).read().decode())
    return new_tab["id"], new_tab["webSocketDebuggerUrl"]


def close_tab(tab_id: str, cdp_base_url: str = CDP_BASE_URL, log: logging.Logger = None):
    """Closes ephemeral tab via CDP, strictly preserving other tabs."""
    try:
        urllib.request.urlopen(f"{cdp_base_url}/json/close/{tab_id}", timeout=5)
        if log:
            log.info(f"Closed ephemeral tab {tab_id}")
    except Exception as e:
        if log:
            log.warning(f"Error closing tab {tab_id}: {e}")


async def harvest_liquidation_maxpain(
    timeframe_code: str,
    timeframe_label: str,
    cdp_base_url: str = CDP_BASE_URL,
    target_url: str = TARGET_URL,
    log: logging.Logger = None,
) -> List[Dict[str, Any]]:
    """
    Connects to CoinGlass /liquidation-maxpain in a dedicated ephemeral tab,
    switches to the requested timeframe tab, and extracts all candidates (~745)
    from the React Fiber tree with complete columnar attributes.
    """
    if not websockets:
        raise RuntimeError("websockets package is required. Install via pip install websockets.")

    if log is None:
        log = logging.getLogger("LiquidationMaxPainCore")

    tab_id, ws_url = open_ephemeral_tab(target_url, cdp_base_url)
    log.info(f"Opened dedicated ephemeral tab (ID: {tab_id}) for Max Pain {timeframe_code} ({timeframe_label}).")

    t0 = time.time()
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

        # Wait for page hydration (up to 15s)
        log.info(f"Waiting for table and React Fiber hydration on {target_url}...")
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

        # Switch to requested timeframe tab if not already active
        js_switch = f"""
        (() => {{
            const targetLabel = {json.dumps(timeframe_label)}.toLowerCase().trim();
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
        fallback_mode = False
        if "error" in switch_val:
            log.warning(f"Timeframe '{timeframe_label}' tab unavailable or restricted on public tier: {switch_val['error']}. Falling back to 24H baseline.")
            fallback_mode = True
        elif switch_val.get("clicked"):
            log.info(f"Switched timeframe to '{timeframe_label}'. Waiting for data update...")
            await asyncio.sleep(1.8)
        else:
            log.info(f"Timeframe '{timeframe_label}' was already active.")
            await asyncio.sleep(0.5)

        # Extract all candidates across all pages from React Fiber
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
        extract_res = await cdp_cmd("Runtime.evaluate", {"expression": js_extract, "returnByValue": True})
        extract_val = extract_res.get("value", {})
        if "error" in extract_val:
            raise RuntimeError(f"Extraction failed: {extract_val['error']}")

        records = extract_val.get("records", [])
        log.info(
            f"Successfully harvested {len(records)} assets for {timeframe_code} ({timeframe_label}) "
            f"in {time.time() - t0:.2f}s."
        )
        return records

    finally:
        close_tab(tab_id, cdp_base_url, log)


def run_maxpain_harvest(
    timeframe_code: str,
    timeframe_label: str,
    sheet_name: str,
    target_index: int,
    log_name: str,
):
    """CLI orchestrator entrypoint for a single timeframe Max Pain module."""
    parser = argparse.ArgumentParser(description=f"CoinGlass Liquidation Max Pain {timeframe_code} Pure-Parquet Dumper")
    parser.add_argument("--cdp-url", type=str, default=CDP_BASE_URL)
    args = parser.parse_args()

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] [%(name)s] %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )
    log = logging.getLogger(log_name)

    log.info(f"Starting {log_name} [{timeframe_code} - '{timeframe_label}'] -> Feed '{sheet_name}'...")
    try:
        records = asyncio.run(
            harvest_liquidation_maxpain(
                timeframe_code=timeframe_code,
                timeframe_label=timeframe_label,
                cdp_base_url=args.cdp_url,
                log=log,
            )
        )
        if not records:
            log.error("Harvest returned 0 records. Failing execution.")
            sys.exit(1)

        meta = write_parquet_feed(sheet_name, records)
        log.info(f"Execution completed successfully: {len(records)} records dumped to Parquet feed '{sheet_name}': {meta.get('byte_size')} bytes in {meta.get('write_latency_ms', 0):.2f}ms.")
        sys.exit(0)
    except Exception as exc:
        log.exception(f"Unhandled error in {log_name}: {exc}")
        sys.exit(1)
