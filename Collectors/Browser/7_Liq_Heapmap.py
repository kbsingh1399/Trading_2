#!/usr/bin/env python3
"""
Data/Excel_Modules/7_Liq_Heapmap.py
==================================
Live CoinGlass Liquidation Heatmap Multi-Timeframe Scraper & Excel Dumper.
Captures the Liquidation Heatmap across all 4 timeframes (1h, 4h, 12h, 24h)
from https://www.coinglass.com/liquidations and formats into worksheet '7_Liq_Heapmap'
in Data/feeds/<feed_name>.parquet (positioned at Index 9, immediately after '6_Funding_Fee_Settlement').

Layout Matches Operator Sketch:
  Rank | Asset | 1hour | 4hour | 12 hour | 24hour | Timestamp (UTC)

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
import re
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
log = logging.getLogger("7_Liq_Heapmap")

MODULES_DIR = pathlib.Path(__file__).resolve().parent
ROOT_DIR = MODULES_DIR.parents[1]
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
    ("timestamp_ist", "Timestamp (IST)", 24, "center"),
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
    ist_tz = datetime.timezone(datetime.timedelta(hours=5, minutes=30))
    now_ist = datetime.datetime.now(ist_tz)
    ts_str = now_ist.strftime("%Y-%m-%d %H:%M:%S IST")

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
            const tabs = Array.from(document.querySelectorAll('#heatmap .MuiTab-root, .lp-heat-panel .MuiTab-root, div[role="tablist"] button, .MuiTabs-root button, div[role="tab"], .ant-tabs-tab'));
            const btn = tabs.find(b => b.innerText.trim().toLowerCase() === tf.toLowerCase() || b.innerText.trim().toLowerCase().includes(tf.toLowerCase()));
            if (btn) {
                btn.click();
                await new Promise(r => setTimeout(r, 1500));
            }
            
            const tiles = Array.from(document.querySelectorAll('.lp-tile, div[class*="lp-tile"], div[class*="heatmap-tile"], div[class*="tile"], div[role="gridcell"]'));
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
                const tabs = Array.from(document.querySelectorAll('#heatmap .MuiTab-root, .lp-heat-panel .MuiTab-root, div[role="tablist"] button, .MuiTabs-root button, div[role="tab"], .ant-tabs-tab'));
                const btn = tabs.find(b => b.innerText.trim().toLowerCase() === tf.toLowerCase() || b.innerText.trim().toLowerCase().includes(tf.toLowerCase()));
                if (btn) {{
                    btn.click();
                    await new Promise(r => setTimeout(r, 1500));
                }}
                
                const tiles = Array.from(document.querySelectorAll('.lp-tile, div[class*="lp-tile"], div[class*="heatmap-tile"], div[class*="tile"], div[role="gridcell"]'));
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
                "timestamp_ist": ts_str,
            }
        )

    log.info(f"Heatmap matrix built: {len(records)} unique assets across 1h, 4h, 12h, 24h.")
    return records


def dump_to_parquet(records: list[dict]) -> bool:
    if not records:
        log.error("No records to dump to Parquet.")
        return False
    meta = write_parquet_feed(SHEET_NAME, records)
    log.info(f"Successfully dumped {len(records)} Heatmap rows into Parquet feed '{SHEET_NAME}': {meta.get('byte_size')} bytes in {meta.get('write_latency_ms', 0):.2f}ms.")
    return True


def main():
    parser = argparse.ArgumentParser(description="CoinGlass Liquidation Heatmap Multi-Timeframe Pure-Parquet Dumper")
    args = parser.parse_args()

    records = asyncio.run(harvest_liquidation_heatmap())
    if not records:
        log.error("No records harvested from Heatmap.")
        sys.exit(1)

    success = dump_to_parquet(records)
    if not success:
        log.error("Failed to dump data to Parquet.")
        sys.exit(1)

    log.info("7_Liq_Heapmap module completed successfully.")


if __name__ == "__main__":
    main()
