#!/usr/bin/env python3
"""
Collectors/Core/liquidation_maxpain_core.py
===========================================
Shared Core Extraction & Parquet Writing Engine for CoinGlass Liquidation Max Pain Feeds:
  - 9_Liquidation_Max_Pain_24H.parquet (24H timeframe: '24H')
  - 9_Liquidation_Max_Pain_48H.parquet (48H timeframe: '48H')
  - 9_Liquidation_Max_Pain_3D.parquet  (3D timeframe:  '3D')
  - 9_Liquidation_Max_Pain_7D.parquet  (7D timeframe:  '1W')

Target Page: https://www.coinglass.com/liquidation-maxpain
Extracts multi-asset items across modern CoinGlass CSS-module PainTable layout with single-session tab rotation.
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
    ("24H", "24H", "9_Liquidation_Max_Pain_24H"),
    ("48H", "48H", "9_Liquidation_Max_Pain_48H"),
    ("3D", "3D", "9_Liquidation_Max_Pain_3D"),
    ("7D", "1W", "9_Liquidation_Max_Pain_7D"),
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


def parse_num(val_str: Any) -> Optional[float]:
    """Parses raw text into clean float, handling commas, currencies, unicode minus signs."""
    if val_str is None:
        return None
    s = (
        str(val_str)
        .replace(",", "")
        .replace("$", "")
        .replace("%", "")
        .replace("\u2212", "-")
        .replace("+", "")
        .strip()
    )
    try:
        return float(s)
    except ValueError:
        return None


def parse_vol(val_str: Any) -> Optional[float]:
    """Parses '$67.5M', '$2.51B', '$500K' into numeric float."""
    if val_str is None:
        return None
    s = str(val_str).replace(",", "").replace("$", "").strip()
    mult = 1.0
    if s.endswith("B") or s.endswith("b"):
        mult = 1e9
        s = s[:-1]
    elif s.endswith("M") or s.endswith("m"):
        mult = 1e6
        s = s[:-1]
    elif s.endswith("K") or s.endswith("k"):
        mult = 1e3
        s = s[:-1]
    try:
        return float(s) * mult
    except ValueError:
        return None


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
    ('24H', '48H', '3D', '1W'), extracts all candidates for each,
    and writes immediately to respective Parquet feeds.
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

        async def click_at(x: float, y: float):
            await cdp_cmd("Input.dispatchMouseEvent", {"type": "mouseMoved", "x": x, "y": y})
            await asyncio.sleep(0.04)
            await cdp_cmd("Input.dispatchMouseEvent", {"type": "mousePressed", "x": x, "y": y, "button": "left", "clickCount": 1})
            await asyncio.sleep(0.04)
            await cdp_cmd("Input.dispatchMouseEvent", {"type": "mouseReleased", "x": x, "y": y, "button": "left", "clickCount": 1})

        # Hydration check: wait until table tbody rows are populated
        hydrated = False
        for attempt in range(30):
            js_check = "document.querySelectorAll('table tbody tr').length"
            res = await cdp_cmd("Runtime.evaluate", {"expression": js_check, "returnByValue": True})
            row_count = res.get("value", 0)
            if row_count > 10:
                hydrated = True
                log.info(f"Table hydrated successfully in {time.time() - t0:.2f}s with {row_count} rows.")
                break
            await asyncio.sleep(0.8)

        if not hydrated:
            raise TimeoutError(f"CoinGlass table failed to hydrate within timeout on tab {tab_id}")

        # Rotate through all 4 timeframes in this single tab session
        for tf_code, tf_dropdown_val, feed_name in MAXPAIN_TIMEFRAMES:
            log.info(f"Rotating to timeframe '{tf_code}' (Option '{tf_dropdown_val}') -> Feed '{feed_name}'...")

            # Check current Window trigger text
            js_get_trig = """
            (() => {
                const boxes = Array.from(document.querySelectorAll('.ui_selBox__kgpsT, [data-role="select-trigger"]'));
                const b = boxes.find(x => x.innerText.includes('Window'));
                if (!b) return null;
                const r = b.getBoundingClientRect();
                return { x: Math.round(r.x + r.width/2), y: Math.round(r.y + r.height/2), text: b.innerText.trim() };
            })()
            """
            trig_res = await cdp_cmd("Runtime.evaluate", {"expression": js_get_trig, "returnByValue": True})
            trig = trig_res.get("value")

            # If not already on the desired timeframe, click trigger and select option
            if trig and (tf_dropdown_val not in trig["text"]):
                log.info(f"  -> Opening Window dropdown at ({trig['x']}, {trig['y']}) (Current: '{trig['text']}')...")
                await click_at(trig["x"], trig["y"])
                await asyncio.sleep(0.6)

                js_find_opt = f"""
                (() => {{
                    const target = "{tf_dropdown_val}".toUpperCase();
                    const walker = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT);
                    let node;
                    while ((node = walker.nextNode())) {{
                        const txt = node.nodeValue.trim();
                        if (txt.toUpperCase() === target) {{
                            const el = node.parentElement;
                            const r = el.getBoundingClientRect();
                            if (r.width > 0 && r.height > 0 && r.y > 150) {{
                                return {{ x: Math.round(r.x + r.width/2), y: Math.round(r.y + r.height/2), text: txt }};
                            }}
                        }}
                    }}
                    return null;
                }})()
                """
                opt_res = await cdp_cmd("Runtime.evaluate", {"expression": js_find_opt, "returnByValue": True})
                opt_coord = opt_res.get("value")
                if opt_coord:
                    log.info(f"  -> Clicking timeframe option '{tf_dropdown_val}' at ({opt_coord['x']}, {opt_coord['y']})...")
                    await click_at(opt_coord["x"], opt_coord["y"])
                    await asyncio.sleep(1.2)
                else:
                    log.warning(f"  -> Could not locate dropdown coordinate for '{tf_dropdown_val}'")

            # Extract table rows
            js_extract = """
            (() => {
                const rows = Array.from(document.querySelectorAll('table tbody tr'));
                return rows.map((tr, idx) => {
                    const tds = Array.from(tr.querySelectorAll('td'));
                    if (tds.length < 5) return null;
                    const rankText = tds[1] ? tds[1].innerText.trim() : String(idx + 1);
                    const symEl = tds[2] ? tds[2].querySelector('b, [class*="coin"]') : null;
                    const symText = symEl ? symEl.innerText.trim() : (tds[2] ? tds[2].innerText.trim() : '');
                    const pEl = tds[3] ? tds[3].querySelector('span') : null;
                    const priceText = pEl ? pEl.innerText.trim() : (tds[3] ? tds[3].innerText.trim() : '');
                    const lpPriceEl = tds[4] ? tds[4].querySelector('b') : null;
                    const lpVolEl = tds[4] ? tds[4].querySelector('span span, [class*="pv"] span') : null;
                    const lpDistEl = tds[4] ? tds[4].querySelector('[class*="dp"]') : null;
                    const spPriceEl = tds[5] ? tds[5].querySelector('b') : null;
                    const spVolEl = tds[5] ? tds[5].querySelector('span span, [class*="pv"] span') : null;
                    const spDistEl = tds[5] ? tds[5].querySelector('[class*="dp"]') : null;

                    return {
                        ranking_str: rankText,
                        symbol: symText.split('\\n')[0].trim(),
                        price_str: priceText.split('\\n')[0].trim(),
                        long_price_str: lpPriceEl ? lpPriceEl.innerText.trim() : '',
                        long_vol_str: lpVolEl ? lpVolEl.innerText.trim() : '',
                        long_dist_str: lpDistEl ? lpDistEl.innerText.trim() : '',
                        short_price_str: spPriceEl ? spPriceEl.innerText.trim() : '',
                        short_vol_str: spVolEl ? spVolEl.innerText.trim() : '',
                        short_dist_str: spDistEl ? spDistEl.innerText.trim() : ''
                    };
                }).filter(Boolean);
            })()
            """
            extract_res = await cdp_cmd("Runtime.evaluate", {"expression": js_extract, "returnByValue": True})
            raw_records = extract_res.get("value", [])

            now_ist_str = datetime.datetime.now(IST_TZ).strftime("%Y-%m-%d %H:%M:%S IST")
            cleaned_records = []
            for r in raw_records:
                price = parse_num(r.get("price_str"))
                s_price = parse_num(r.get("short_price_str"))
                s_vol = parse_vol(r.get("short_vol_str"))
                s_dist_pct = parse_num(r.get("short_dist_str"))
                
                l_price = parse_num(r.get("long_price_str"))
                l_vol = parse_vol(r.get("long_vol_str"))
                l_dist_pct = parse_num(r.get("long_dist_str"))

                s_dist_usd = (s_price - price) if (s_price is not None and price is not None) else None
                l_dist_usd = (l_price - price) if (l_price is not None and price is not None) else None

                cleaned_records.append({
                    "ranking": int(r["ranking_str"]) if r.get("ranking_str", "").isdigit() else len(cleaned_records) + 1,
                    "symbol": r.get("symbol", ""),
                    "price": price,
                    "short_max_pain_price": s_price,
                    "short_max_pain_vol": s_vol,
                    "short_distance_usd": s_dist_usd,
                    "short_distance_pct": s_dist_pct,
                    "long_max_pain_price": l_price,
                    "long_max_pain_vol": l_vol,
                    "long_distance_usd": l_dist_usd,
                    "long_distance_pct": l_dist_pct,
                    "timestamp_ist": now_ist_str,
                })

            if cleaned_records:
                meta = write_parquet_feed(feed_name, cleaned_records, merge_missing_assets=True)
                results[feed_name] = len(cleaned_records)
                log.info(f"  -> Dumped {len(cleaned_records)} assets to '{feed_name}.parquet' (Size: {meta.get('byte_size')}B)")
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

    if not args.force and parquet_path.exists():
        age_sec = now_ts - os.path.getmtime(parquet_path)
        if age_sec < 90.0:
            log.info(f"Feed '{sheet_name}' is already fresh ({age_sec:.1f}s old). Skipping redundant tab hydration.")
            sys.exit(0)

    log.info(f"Starting {log_name} [{timeframe_code} - '{timeframe_label}'] -> Feed '{sheet_name}'...")
    try:
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
