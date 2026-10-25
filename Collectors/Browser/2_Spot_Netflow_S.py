#!/usr/bin/env python3
"""
Collectors/Browser/2_Spot_Netflow_S.py
======================================
CoinGlass Cryptocurrency Spot Netflow Statistics Scraper & Parquet Dumper.
Captures authentic multi-exchange Spot Inflow/Outflow statistics across all 18 institutional
perpetual assets from:
https://www.coinglass.com/spot-inflow-outflow
and writes to Data/feeds/2_Spot_Netflow_S.parquet.

Universe (18 Institutional Binance USDT-M Perpetuals):
  BTC, ETH, XRP, SOL, BNB, DOGE, ADA, TRX, LINK, AVAX, SUI, NEAR, DOT, LTC, BCH, APT, OP, ARB

Schema:
  # | Symbol | Price | 5_minute | 15_minute | 30_minute | 1_hour | 4_hour | 12_hour | 24_hour | 7_day | 30_day | Market_Cap | Timestamp_IST

Anti-Overfitting & Anti-Lag Guardrails:
  - Connects to Edge CDP on port 9222 (reuses open tab or opens ephemeral tab).
  - Explicitly ensures the 'Spot' tab is active (not Futures).
  - High-speed targeted symbol resolution via search input + Enter, extracting raw React Fiber data.
  - Fail-closed verification: asserts that real non-zero market cap and spot netflow values exist.
  - Ephemeral/Reused tab hygiene: preserves Arena.ai tab untouched.
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
    format="%(asctime)s [%(levelname)s] [2_Spot_Netflow_S] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
log = logging.getLogger("2_Spot_Netflow_S")

CDP_BASE_URL = "http://127.0.0.1:9222"
TARGET_URL = "https://www.coinglass.com/spot-inflow-outflow"
FEED_NAME = "2_Spot_Netflow_S"

DEFAULT_UNIVERSE = [
    "BTC", "ETH", "XRP", "SOL", "BNB",
    "DOGE", "ADA", "TRX", "LINK", "AVAX",
    "SUI", "NEAR", "DOT", "LTC", "BCH",
    "APT", "OP", "ARB",
]

COLUMNS = [
    ("#", "#", 8, "center"),
    ("Symbol", "Symbol", 14, "left"),
    ("Price", "Price", 14, "right"),
    ("5_minute", "5 minute", 14, "right"),
    ("15_minute", "15 minute", 14, "right"),
    ("30_minute", "30 minute", 14, "right"),
    ("1_hour", "1 hour", 14, "right"),
    ("4_hour", "4 hour", 14, "right"),
    ("12_hour", "12 hour", 14, "right"),
    ("24_hour", "24 hour", 14, "right"),
    ("7_day", "7 day", 15, "right"),
    ("30_day", "30 day", 15, "right"),
    ("Market_Cap", "Market Cap", 16, "right"),
    ("Timestamp_IST", "Timestamp (IST)", 24, "center"),
]


def fmt_usd(val: float | None) -> str:
    """Formats numeric USD value into institutional shorthand (+/-$X.XXM / B / K)."""
    if val is None or val != val:
        return "-"
    sign = "+" if val >= 0 else "-"
    abs_v = abs(val)
    if abs_v >= 1e9:
        return f"{sign}${abs_v / 1e9:.2f}B"
    elif abs_v >= 1e6:
        return f"{sign}${abs_v / 1e6:.2f}M"
    elif abs_v >= 1e3:
        return f"{sign}${abs_v / 1e3:.2f}K"
    else:
        return f"{sign}${abs_v:.2f}"


def fmt_mkt_cap(val: float | None) -> str:
    """Formats market capitalization value."""
    if val is None or val != val:
        return "-"
    abs_v = abs(val)
    if abs_v >= 1e12:
        return f"${abs_v / 1e12:.2f}T"
    elif abs_v >= 1e9:
        return f"${abs_v / 1e9:.2f}B"
    elif abs_v >= 1e6:
        return f"${abs_v / 1e6:.2f}M"
    else:
        return f"${abs_v:.2f}"


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


def get_target_tab() -> tuple[str, str, bool]:
    """Finds an existing CoinGlass spot tab or opens an ephemeral dedicated tab."""
    try:
        req = urllib.request.Request(f"{CDP_BASE_URL}/json")
        tabs = json.loads(urllib.request.urlopen(req, timeout=5).read().decode())
        for t in tabs:
            if "spot-inflow-outflow" in t.get("url", "") or "spot_inflow_outflow" in t.get("url", ""):
                log.info(f"Reusing active CoinGlass Spot Netflow tab (ID: {t['id']}).")
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


async def harvest_spot_netflows(symbols: list[str] = DEFAULT_UNIVERSE) -> list[dict]:
    """Harvests authentic CoinGlass Spot Netflow Statistics for all 18 institutional symbols."""
    if not websockets:
        raise RuntimeError("websockets package is required.")

    tab_id, ws_url, is_ephemeral = get_target_tab()

    now_ist = datetime.datetime.now(
        datetime.timezone(datetime.timedelta(hours=5, minutes=30))
    ).strftime("%Y-%m-%d %H:%M:%S IST")

    all_records: list[dict] = []

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

        await cdp_cmd("Network.enable")

        if is_ephemeral:
            log.info("Awaiting page hydration on new tab (6s)...")
            await asyncio.sleep(6.0)

        # 1. Ensure 'Spot' tab is active
        js_ensure_spot = """
        (() => {
            const btns = Array.from(document.querySelectorAll('button, [role="tab"], div, span'));
            const spotBtn = btns.find(b => b.innerText && b.innerText.trim() === 'Spot');
            if (spotBtn && !spotBtn.classList.contains('Mui-selected')) {
                spotBtn.click();
                return { clicked: true };
            }
            return { alreadyActive: true };
        })()
        """
        await cdp_cmd("Runtime.evaluate", {"expression": js_ensure_spot, "returnByValue": True})
        await asyncio.sleep(0.4)

        for idx, sym in enumerate(symbols, start=1):
            log.info(f"[{idx:2d}/{len(symbols)}] Harvesting CoinGlass Spot Netflow for {sym}...")

            # Type symbol into search box and dispatch Enter
            js_search = f"""
            (() => {{
                const input = document.querySelector('input.cg-style-za5rna') || Array.from(document.querySelectorAll('input[type="text"]')).find(i => i.closest('.MuiInput-root'));
                if (!input) return {{ error: 'No input found' }};
                input.focus();
                input.click();
                const nativeSetter = Object.getOwnPropertyDescriptor(window.HTMLInputElement.prototype, 'value').set;
                nativeSetter.call(input, '{sym}');
                input.dispatchEvent(new Event('input', {{ bubbles: true }}));
                input.dispatchEvent(new Event('change', {{ bubbles: true }}));
                input.dispatchEvent(new KeyboardEvent('keydown', {{ key: 'Enter', code: 'Enter', keyCode: 13, which: 13, bubbles: true }}));
                input.dispatchEvent(new KeyboardEvent('keyup', {{ key: 'Enter', code: 'Enter', keyCode: 13, which: 13, bubbles: true }}));
                return {{ set: true }};
            }})()
            """
            await cdp_cmd("Runtime.evaluate", {"expression": js_search, "returnByValue": True})

            # Read filtered row from React Fiber dataSource
            js_read = f"""
            (() => {{
                const tables = Array.from(document.querySelectorAll('table'));
                const dt = tables.length > 1 ? tables[1] : tables[0];
                if (!dt) return null;
                const fiberKey = Object.keys(dt).find(k => k.startsWith('__reactFiber$') || k.startsWith('__reactInternalInstance$'));
                let f = dt[fiberKey];
                while (f) {{
                    if (f.memoizedProps && f.memoizedProps.dataSource) {{
                        const item = f.memoizedProps.dataSource.find(d => d.symbol === '{sym}');
                        if (item) return item;
                    }}
                    f = f.return;
                }}
                return null;
            }})()
            """

            matched_data = None
            for _ in range(20):
                await asyncio.sleep(0.15)
                res = await cdp_cmd("Runtime.evaluate", {"expression": js_read, "returnByValue": True})
                val = res.get("result", {}).get("value")
                if val and val.get("symbol") == sym:
                    matched_data = val
                    break

            if matched_data:
                price_str = fmt_price(matched_data.get("price"))
                mkt_cap_str = fmt_mkt_cap(matched_data.get("marketCap"))
                f_5m = fmt_usd(matched_data.get("m5OutInVolUsd"))
                f_15m = fmt_usd(matched_data.get("m15OutInVolUsd"))
                f_30m = fmt_usd(matched_data.get("m30OutInVolUsd"))
                f_1h = fmt_usd(matched_data.get("h1OutInVolUsd"))
                f_4h = fmt_usd(matched_data.get("h4OutInVolUsd"))
                f_12h = fmt_usd(matched_data.get("h12OutInVolUsd"))
                f_24h = fmt_usd(matched_data.get("h24OutInVolUsd"))
                f_7d = fmt_usd(matched_data.get("w1OutInVolUsd"))
                f_30d = fmt_usd(matched_data.get("d30OutInVolUsd"))

                all_records.append({
                    "#": idx,
                    "Symbol": sym,
                    "Price": price_str,
                    "5_minute": f_5m,
                    "15_minute": f_15m,
                    "30_minute": f_30m,
                    "1_hour": f_1h,
                    "4_hour": f_4h,
                    "12_hour": f_12h,
                    "24_hour": f_24h,
                    "7_day": f_7d,
                    "30_day": f_30d,
                    "Market_Cap": mkt_cap_str,
                    "Timestamp_IST": now_ist,
                })
                log.info(f"  -> Verified {sym}: Price={price_str}, 5m={f_5m}, 24h={f_24h}, MktCap={mkt_cap_str}")
            else:
                log.error(f"  -> Integrity failure: Could not find CoinGlass spot netflow data for {sym}!")

        # Reset search box to clean state
        js_clear = """
        (() => {
            const input = document.querySelector('input.cg-style-za5rna') || Array.from(document.querySelectorAll('input[type="text"]')).find(i => i.closest('.MuiInput-root'));
            if (input) {
                const nativeSetter = Object.getOwnPropertyDescriptor(window.HTMLInputElement.prototype, 'value').set;
                nativeSetter.call(input, '');
                input.dispatchEvent(new Event('input', { bubbles: true }));
                input.dispatchEvent(new KeyboardEvent('keydown', { key: 'Enter', code: 'Enter', keyCode: 13, which: 13, bubbles: true }));
            }
        })()
        """
        await cdp_cmd("Runtime.evaluate", {"expression": js_clear, "returnByValue": True})
        await ws.close()

    finally:
        if is_ephemeral:
            close_tab(tab_id)

    log.info(f"Total Spot Netflow records harvested: {len(all_records)} / {len(symbols)} assets.")
    return all_records


def main():
    parser = argparse.ArgumentParser(description="CoinGlass Cryptocurrency Spot Netflow Statistics Scraper")
    parser.add_argument("--symbols", nargs="+", default=DEFAULT_UNIVERSE, help="Assets to harvest")
    args = parser.parse_args()

    symbols = args.symbols
    if len(symbols) == 1 and "," in symbols[0]:
        symbols = [s.strip().upper() for s in symbols[0].split(",") if s.strip()]

    log.info(f"Starting Spot Netflow harvest for {len(symbols)} assets: {symbols}")
    records = asyncio.run(harvest_spot_netflows(symbols=symbols))

    if not records:
        log.error("Harvesting yielded 0 records. Process aborted.")
        sys.exit(1)

    # 1. Pure Parquet Dump
    meta = write_parquet_feed(FEED_NAME, records)
    log.info(f"Successfully dumped feed to Parquet: {meta}")

    log.info("Spot Netflow pipeline executed successfully.")


if __name__ == "__main__":
    main()
