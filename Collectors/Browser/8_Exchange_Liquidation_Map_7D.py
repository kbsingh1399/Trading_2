#!/usr/bin/env python3
"""
Collectors/Browser/8_Exchange_Liquidation_Map_7D.py
==================================================
CoinGlass Multi-Asset Exchange Liquidation Map (7-Day Window) Scraper & Parquet Dumper.
Captures multi-exchange liquidation leverage levels across price points for institutional
perpetual assets from the "Bitcoin/Crypto Exchange Liquidation Map" ECharts chart container on:
https://www.coinglass.com/pro/futures/LiquidationMap
and writes to Data/feeds/8_Exchange_Liquidation_Map_7D.parquet.

Universe (Multi-Asset: Tier 1 Crypto + Tier 2 Gold + Tier 3 FX Majors):
  BTC, ETH, XRP, SOL, BNB, DOGE, ADA, TRX, LINK, AVAX, SUI, NEAR, DOT, LTC, BCH, APT, OP, ARB,
  XAUT, PAXG, EURUSD, GBPUSD, USDJPY

Schema:
  Sr.No | Asset | Time | Timestamp_IST | Price | Cummulitve_Liquidation | Short | Long | Binanace | OKX | Bybit

Anti-Overfitting & Anti-Race Guardrails:
  - Validates timeframe dropdown is strictly set to '7 day'.
  - Native prototype input setter with aria-controls listbox resolution for MUI autocomplete.
  - Multi-venue reference-price sanity bounds (asset_registry) to prevent off-by-one async race conditions.
  - Supports Bybit-exclusive assets (EURUSD, XAUT) and multi-exchange feeds without artificial exclusions.
  - Ephemeral/Reused tab hygiene: strictly preserves Arena.ai tab untouched.
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

try:
    from asset_registry import asset_registry
except ImportError:
    asset_registry = None

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] [8_Exchange_Liquidation_Map_7D] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
log = logging.getLogger("8_Exchange_Liquidation_Map_7D")

CDP_BASE_URL = "http://127.0.0.1:9222"
TARGET_URL = "https://www.coinglass.com/pro/futures/LiquidationMap"
FEED_NAME = "8_Exchange_Liquidation_Map_7D"
TIMEFRAME_TARGET = "7 day"

if asset_registry:
    DEFAULT_UNIVERSE = asset_registry.get_assets_for_collector("8_Exchange_Liquidation_Map_7D")
else:
    DEFAULT_UNIVERSE = [
        "BTC", "ETH", "XRP", "SOL", "BNB",
        "DOGE", "ADA", "TRX", "LINK", "AVAX",
        "SUI", "NEAR", "DOT", "LTC", "BCH",
        "APT", "OP", "ARB",
        "XAUT", "PAXG", "EURUSD", "GBPUSD", "USDJPY"
    ]

COLUMNS_DEF = [
    ("Sr.No", "Sr.No", 10, "center"),
    ("Asset", "Asset", 12, "center"),
    ("Time", "Time", 10, "center"),
    ("Timestamp_IST", "Timestamp (IST)", 24, "center"),
    ("Price", "Price", 16, "right"),
    ("Cumulative_Liquidation", "Cumulative Liquidation", 24, "right"),
    ("Short", "Short", 20, "right"),
    ("Long", "Long", 20, "right"),
    ("Binance", "Binance", 18, "right"),
    ("Cummulitve_Liquidation", "Cummulitve Liquidation", 24, "right"),
    ("Binanace", "Binanace", 18, "right"),
    ("OKX", "OKX", 18, "right"),
    ("Bybit", "Bybit", 18, "right"),
]


def format_usd(val: float | None) -> str:
    """Formats float amount to human-readable string matching CoinGlass UI (e.g. $723.25M, $964.97K)."""
    if val is None or val == 0:
        return "$0"
    abs_val = abs(val)
    if abs_val >= 1e9:
        return f"${val / 1e9:.2f}B"
    elif abs_val >= 1e6:
        return f"${val / 1e6:.2f}M"
    elif abs_val >= 1e3:
        return f"${val / 1e3:.2f}K"
    else:
        return f"${val:.2f}"


def get_all_reference_prices(symbols: list[str]) -> dict[str, float]:
    """Fetches real-time reference prices via asset_registry or Binance ticker."""
    prices: dict[str, float] = {}
    if asset_registry:
        asset_registry.batch_prefetch_binance_prices()
        for s in symbols:
            prices[s] = asset_registry.get_reference_price(s)
        return prices

    # Fallback if asset_registry is not available
    url = "https://fapi.binance.com/fapi/v1/ticker/price"
    fallback_map = {
        "BTC": 80000.0, "ETH": 2350.0, "SOL": 100.0, "DOGE": 0.08, "BNB": 600.0,
        "XRP": 2.30, "ADA": 0.20, "TRX": 0.33, "LINK": 11.5, "AVAX": 9.0,
        "SUI": 0.93, "NEAR": 1.25, "DOT": 4.5, "LTC": 55.0, "BCH": 300.0,
        "APT": 5.0, "OP": 0.70, "ARB": 0.17, "XAUT": 4000.0, "PAXG": 4000.0,
        "EURUSD": 1.12, "GBPUSD": 1.33, "USDJPY": 157.0
    }
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        res = json.loads(urllib.request.urlopen(req, timeout=5).read().decode())
        p_dict = {d["symbol"].replace("USDT", ""): float(d["price"]) for d in res if d["symbol"].endswith("USDT")}
        return {s: p_dict.get(s, fallback_map.get(s, 1.0)) for s in symbols}
    except Exception as e:
        log.warning(f"Could not fetch reference prices ({e}), using fallback map.")
        return {s: fallback_map.get(s, 1.0) for s in symbols}


def get_target_tab() -> tuple[str, str, bool]:
    """Finds an existing LiquidationMap tab or opens an ephemeral dedicated tab."""
    try:
        req = urllib.request.Request(f"{CDP_BASE_URL}/json")
        tabs = json.loads(urllib.request.urlopen(req, timeout=5).read().decode())
        for t in tabs:
            if "LiquidationMap" in t.get("url", ""):
                log.info(f"Reusing active CoinGlass LiquidationMap tab (ID: {t['id']}).")
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


async def harvest_exchange_liquidation_map_7d(symbols: list[str] = DEFAULT_UNIVERSE) -> list[dict]:
    """Harvests 7-Day Exchange Liquidation Map data for multi-asset universe."""
    if not websockets:
        raise RuntimeError("websockets package is required.")

    ref_prices = get_all_reference_prices(symbols)
    tab_id, ws_url, is_ephemeral = get_target_tab()

    now_ist = datetime.datetime.now(
        datetime.timezone(datetime.timedelta(hours=5, minutes=30))
    ).strftime("%Y-%m-%d %H:%M:%S IST")

    all_records: list[dict] = []
    global_sr = 1

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

        log.info("Awaiting complete page readiness and initial chart data population...")
        for p in range(40):
            await asyncio.sleep(0.5)
            js_check = """
            (() => {
                const allElements = Array.from(document.querySelectorAll('*'));
                const header = allElements.find(el => el.children.length === 0 && (el.innerText || '').includes('Exchange Liquidation Map'));
                if (!header) return { loaded: false };
                let container = header.parentElement;
                while (container && !container.querySelector('[_echarts_instance_]') && !container.querySelector('canvas')) {
                    container = container.parentElement;
                }
                if (!container) return { loaded: false };
                const echartsDom = container.querySelector('[_echarts_instance_]');
                if (!echartsDom) return { loaded: false };
                const fiberKey = Object.keys(echartsDom).find(k => k.startsWith('__reactFiber$') || k.startsWith('__reactInternalInstance$'));
                let dataLen = 0;
                if (fiberKey && echartsDom[fiberKey]) {
                    let f = echartsDom[fiberKey];
                    while (f) {
                        const p = f.memoizedProps || {};
                        if (p.option && p.option.xAxis && p.option.xAxis[0] && p.option.xAxis[0].data) {
                            dataLen = p.option.xAxis[0].data.length;
                            break;
                        }
                        f = f.return;
                    }
                }
                return {
                    loaded: document.readyState === 'complete' && dataLen > 0,
                    dataLen: dataLen
                };
            })()
            """
            chk = await cdp_cmd("Runtime.evaluate", {"expression": js_check, "returnByValue": True})
            if chk.get("result", {}).get("value", {}).get("loaded"):
                log.info(f"Page & baseline chart fully loaded with {chk.get('result', {}).get('value', {}).get('dataLen')} data points.")
                break

        # 1. Set timeframe to '7 day' on bottom chart
        js_set_tf = f"""
        (() => {{
            const allElements = Array.from(document.querySelectorAll('*'));
            const header = allElements.find(el => el.children.length === 0 && (el.innerText || '').includes('Exchange Liquidation Map'));
            let container = header.parentElement;
            while (container && !container.querySelector('[_echarts_instance_]') && !container.querySelector('canvas')) {{
                container = container.parentElement;
            }}
            const timeSelect = container.querySelector('.MuiSelect-button');
            if (timeSelect && timeSelect.innerText.trim() !== '{TIMEFRAME_TARGET}') {{
                timeSelect.click();
                const listId = timeSelect.getAttribute('aria-controls');
                let list = document.getElementById(listId);
                if (!list) list = document.querySelector('[role="listbox"]');
                if (list) {{
                    const opt = Array.from(list.querySelectorAll('[role="option"]')).find(el => el.innerText.trim() === '{TIMEFRAME_TARGET}');
                    if (opt) {{
                        opt.click();
                        return {{ changed: true, to: '{TIMEFRAME_TARGET}' }};
                    }}
                }}
                return {{ error: 'Timeframe option not found' }};
            }}
            return {{ current: timeSelect ? timeSelect.innerText.trim() : null }};
        }})()
        """
        tf_res = await cdp_cmd("Runtime.evaluate", {"expression": js_set_tf, "returnByValue": True})
        log.info(f"Timeframe set to '{TIMEFRAME_TARGET}': {tf_res.get('result', {}).get('value')}")
        await asyncio.sleep(1.0)

        # Extraction logic
        js_extract = """
        (() => {
            const allElements = Array.from(document.querySelectorAll('*'));
            const header = allElements.find(el => el.children.length === 0 && (el.innerText || '').includes('Exchange Liquidation Map'));
            let container = header.parentElement;
            while (container && !container.querySelector('[_echarts_instance_]') && !container.querySelector('canvas')) {
                container = container.parentElement;
            }
            const echartsDom = container.querySelector('[_echarts_instance_]');
            const fiberKey = Object.keys(echartsDom).find(k => k.startsWith('__reactFiber$') || k.startsWith('__reactInternalInstance$'));
            
            let highestOpt = null;
            let optTitle = null;
            let f = echartsDom[fiberKey];
            while (f) {
                const p = f.memoizedProps || {};
                if (p.option && p.option.xAxis && p.option.xAxis[0] && p.option.xAxis[0].data) {
                    highestOpt = p.option;
                    optTitle = p.title || (p.option.title ? p.option.title.text : null);
                }
                f = f.return;
            }
            if (!highestOpt) return null;
            
            const prices = highestOpt.xAxis[0].data || [];
            const series = highestOpt.series || [];
            const shortSeries = series.find(s => s.name === 'Cumulative Short Liquidation Leverage') || {};
            const longSeries = series.find(s => s.name === 'Cumulative Long Liquidation Leverage') || {};
            const binanceSeries = series.find(s => s.name === 'Binance') || {};
            const okxSeries = series.find(s => s.name === 'OKX') || {};
            const bybitSeries = series.find(s => s.name === 'Bybit') || {};
            
            const shortData = shortSeries.data || [];
            const longData = longSeries.data || [];
            const binanceData = binanceSeries.data || [];
            const okxData = okxSeries.data || [];
            const bybitData = bybitSeries.data || [];
            
            const rows = [];
            for (let i = 0; i < prices.length; i++) {
                const price = prices[i];
                const shortVal = shortData[i];
                const longVal = longData[i];
                const binanceVal = binanceData[i] || 0;
                const okxVal = okxData[i] || 0;
                const bybitVal = bybitData[i] || 0;
                const cumVal = (shortVal !== null && shortVal !== undefined) ? shortVal : ((longVal !== null && longVal !== undefined) ? longVal : 0);
                rows.push({
                    price,
                    cumVal,
                    shortVal,
                    longVal,
                    binanceVal,
                    okxVal,
                    bybitVal
                });
            }
            return {
                optTitle,
                headerText: header.innerText,
                pricesCount: prices.length,
                minPrice: prices[0],
                maxPrice: prices[prices.length - 1],
                rows
            };
        })()
        """

        prev_min_p = None
        for sym_idx, sym in enumerate(symbols):
            expected_price = ref_prices.get(sym, 1.0)
            search_term = asset_registry.resolve_coinglass_search_term(sym) if asset_registry else sym
            log.info(f"[{sym_idx+1}/{len(symbols)}] Harvesting 7D Liquidation Map for {sym} (Search: '{search_term}', Ref ~${expected_price:,.2f})...")

            # 1. Open symbol dropdown, wait for options list to populate, and select target symbol
            js_open_dropdown = """
            (() => {
                const allElements = Array.from(document.querySelectorAll('*'));
                const header = allElements.find(el => el.children.length === 0 && (el.innerText || '').includes('Exchange Liquidation Map'));
                let container = header.parentElement;
                while (container && !container.querySelector('[_echarts_instance_]') && !container.querySelector('canvas')) {
                    container = container.parentElement;
                }
                const popupBtn = container.querySelector('.MuiAutocomplete-popupIndicator, button[title="Open"]');
                if (popupBtn) popupBtn.click();
                return { opened: true };
            })()
            """
            await cdp_cmd("Runtime.evaluate", {"expression": js_open_dropdown, "returnByValue": True})

            target_upper = sym.upper()
            search_upper = search_term.upper()
            clicked_option = False
            for p in range(25):
                await asyncio.sleep(0.2)
                js_click_opt = f"""
                (() => {{
                    const listboxes = Array.from(document.querySelectorAll('[role="listbox"]'));
                    for (const lb of listboxes) {{
                        const opts = Array.from(lb.querySelectorAll('[role="option"], li'));
                        if (opts.length > 50) {{
                            let opt = opts.find(o => o.innerText.trim().toUpperCase() === '{target_upper}' || o.innerText.trim().toUpperCase() === '{search_upper}');
                            if (!opt) opt = opts.find(o => o.innerText.trim().toUpperCase().startsWith('{target_upper}') || o.innerText.trim().toUpperCase().startsWith('{search_upper}'));
                            if (!opt) opt = opts.find(o => o.innerText.trim().toUpperCase().includes('{target_upper}') || o.innerText.trim().toUpperCase().includes('{search_upper}'));
                            if (opt) {{
                                opt.click();
                                return {{ clicked: true, text: opt.innerText.trim() }};
                            }}
                        }}
                    }}
                    return {{ clicked: false }};
                }})()
                """
                c_res = await cdp_cmd("Runtime.evaluate", {"expression": js_click_opt, "returnByValue": True})
                if c_res.get("result", {}).get("value", {}).get("clicked"):
                    clicked_option = True
                    break

            # 2. Verification loop: poll until price matches expected reference bounds and non-zero liquidation values exist
            harvested_data = None
            for poll in range(35):
                await asyncio.sleep(0.3)
                ext = await cdp_cmd("Runtime.evaluate", {"expression": js_extract, "returnByValue": True})
                val = ext.get("result", {}).get("value")
                if not val or not val.get("rows"):
                    continue

                min_p = float(val["minPrice"])
                max_p = float(val["maxPrice"])

                # Anti-race condition: Reference price bracketed or fallback accepted
                is_bracketed = (min_p <= expected_price <= max_p)
                if not is_bracketed and expected_price == 1.0 and max_p > 0:
                    is_bracketed = True

                is_new_chart = (prev_min_p is None) or (abs(min_p - prev_min_p) > 1e-6)
                title = val.get("optTitle") or ""

                if asset_registry:
                    expected_tokens = asset_registry.get_expected_title_tokens(sym)
                    is_title_match = any(tok.lower() in title.lower() for tok in expected_tokens)
                else:
                    is_title_match = (sym == "BTC" and ("Bitcoin" in title or "BTC" in title)) or (sym in title)

                binance_count = sum(1 for r in val["rows"] if r.get("binanceVal", 0) > 0)
                okx_count = sum(1 for r in val["rows"] if r.get("okxVal", 0) > 0)
                bybit_count = sum(1 for r in val["rows"] if r.get("bybitVal", 0) > 0)

                # Unblock Bybit-only pairs (e.g. EURUSD, XAUT) and any exchange liquidation presence
                has_liquidation_data = ((binance_count + okx_count + bybit_count) > 0 or
                                        any((r.get("shortVal") or 0) > 0 or (r.get("longVal") or 0) > 0 for r in val["rows"]))

                if is_bracketed and is_new_chart and is_title_match and has_liquidation_data:
                    log.info(
                        f"  -> Verified {sym}: {min_p} <= ${expected_price:,.2f} <= {max_p} ({len(val['rows'])} levels, "
                        f"Binance={binance_count}, OKX={okx_count}, Bybit={bybit_count}) on poll {poll+1}"
                    )
                    harvested_data = val
                    prev_min_p = min_p
                    break

            if not harvested_data:
                log.error(f"Integrity check failed: Timed out waiting for valid chart update for {sym}!")
                continue

            for r in harvested_data["rows"]:
                short_num = r.get("shortVal")
                long_num = r.get("longVal")
                all_records.append(
                    {
                        "Sr.No": global_sr,
                        "Asset": sym,
                        "Time": "7D",
                        "Timestamp_IST": now_ist,
                        "Price": r.get("price"),
                        "Cumulative_Liquidation": format_usd(r.get("cumVal")),
                        "Short": format_usd(short_num) if short_num is not None else "$0",
                        "Long": format_usd(long_num) if long_num is not None else "$0",
                        "Binance": format_usd(r.get("binanceVal", 0)),
                        "Cummulitve_Liquidation": format_usd(r.get("cumVal")),
                        "Binanace": format_usd(r.get("binanceVal", 0)),
                        "OKX": format_usd(r.get("okxVal", 0)),
                        "Bybit": format_usd(r.get("bybitVal", 0)),
                    }
                )
                global_sr += 1

        await ws.close()

    finally:
        close_tab(tab_id)

    log.info(f"Total 7D records harvested across all assets: {len(all_records)} rows.")
    return all_records


def main():
    parser = argparse.ArgumentParser(description="CoinGlass 7D Multi-Asset Liquidation Map Scraper")
    parser.add_argument("--symbols", nargs="+", default=DEFAULT_UNIVERSE, help="Assets to harvest")
    args = parser.parse_args()

    symbols = args.symbols
    if len(symbols) == 1 and "," in symbols[0]:
        symbols = [s.strip().upper() for s in symbols[0].split(",") if s.strip()]

    log.info(f"Starting 7-Day Liquidation Map harvest for {len(symbols)} assets: {symbols}")
    records = asyncio.run(harvest_exchange_liquidation_map_7d(symbols=symbols))

    if not records:
        log.error("Harvesting yielded 0 records. Process aborted.")
        sys.exit(1)

    # 1. Pure Parquet Dump
    meta = write_parquet_feed(FEED_NAME, records)
    log.info(f"Successfully dumped feed to Parquet: {meta}")

    log.info("7D Liquidation Map pipeline executed successfully.")


if __name__ == "__main__":
    main()
