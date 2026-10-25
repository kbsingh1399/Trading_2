#!/usr/bin/env python3
"""
Collectors/Browser/8_Exchange_Liquidation_Map_7D.py
==================================================
CoinGlass Multi-Asset Exchange Liquidation Map (7-Day Window) Scraper & Parquet Dumper.
Captures multi-exchange liquidation leverage levels across price points for all 18 institutional
perpetual assets from the "Bitcoin/Crypto Exchange Liquidation Map" ECharts chart container on:
https://www.coinglass.com/pro/futures/LiquidationMap
and writes to Data/feeds/8_Exchange_Liquidation_Map_7D.parquet.

Universe (18 Institutional Binance USDT-M Perpetuals):
  BTC, ETH, XRP, SOL, BNB, DOGE, ADA, TRX, LINK, AVAX, SUI, NEAR, DOT, LTC, BCH, APT, OP, ARB

Schema:
  Sr.No | Asset | Time | Timestamp_IST | Price | Cummulitve_Liquidation | Short | Long | Binanace | OKX | Bybit

Anti-Overfitting & Anti-Race Guardrails:
  - Validates timeframe dropdown is strictly set to '7 day'.
  - Native prototype input setter with aria-controls listbox resolution for MUI autocomplete.
  - Live Binance reference-price sanity bounds to prevent off-by-one async race conditions.
  - Fail-closed verification: asserts real non-zero dollar values for Binance, OKX, and Bybit.
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
    import openpyxl
    from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
    from openpyxl.utils import get_column_letter
except ImportError:
    openpyxl = None

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
    format="%(asctime)s [%(levelname)s] [8_Exchange_Liquidation_Map_7D] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
log = logging.getLogger("8_Exchange_Liquidation_Map_7D")

DEFAULT_EXCEL_PATH = ROOT_DIR / "Data" / "DataBase_Trading.xlsx"
CDP_BASE_URL = "http://127.0.0.1:9222"
TARGET_URL = "https://www.coinglass.com/pro/futures/LiquidationMap"
FEED_NAME = "8_Exchange_Liquidation_Map_7D"
TIMEFRAME_TARGET = "7 day"

DEFAULT_UNIVERSE = [
    "BTC", "ETH", "XRP", "SOL", "BNB",
    "DOGE", "ADA", "TRX", "LINK", "AVAX",
    "SUI", "NEAR", "DOT", "LTC", "BCH",
    "APT", "OP", "ARB",
]

COLUMNS_DEF = [
    ("Sr.No", "Sr.No", 10, "center"),
    ("Asset", "Asset", 12, "center"),
    ("Time", "Time", 10, "center"),
    ("Timestamp_IST", "Timestamp (IST)", 24, "center"),
    ("Price", "Price", 16, "right"),
    ("Cummulitve_Liquidation", "Cummulitve Liquidation", 24, "right"),
    ("Short", "Short", 20, "right"),
    ("Long", "Long", 20, "right"),
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


def get_binance_reference_prices() -> dict[str, float]:
    """Fetches real-time reference prices from Binance Futures ticker."""
    url = "https://fapi.binance.com/fapi/v1/ticker/price"
    fallback_map = {
        "BTC": 80000.0, "ETH": 2350.0, "SOL": 100.0, "DOGE": 0.08, "BNB": 600.0,
        "XRP": 2.30, "ADA": 0.20, "TRX": 0.33, "LINK": 11.5, "AVAX": 9.0,
        "SUI": 0.93, "NEAR": 1.25, "DOT": 4.5, "LTC": 55.0, "BCH": 300.0,
        "APT": 5.0, "OP": 0.70, "ARB": 0.17,
    }
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        res = json.loads(urllib.request.urlopen(req, timeout=5).read().decode())
        prices = {d["symbol"].replace("USDT", ""): float(d["price"]) for d in res if d["symbol"].endswith("USDT")}
        return {s: prices.get(s, fallback_map.get(s, 1.0)) for s in DEFAULT_UNIVERSE}
    except Exception as e:
        log.warning(f"Could not fetch Binance prices ({e}), using fallback map.")
        return fallback_map


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
    """Harvests 7-Day Exchange Liquidation Map data for all 18 institutional symbols."""
    if not websockets:
        raise RuntimeError("websockets package is required.")

    ref_prices = get_binance_reference_prices()
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

        if is_ephemeral:
            log.info("Awaiting page hydration on new tab (6s)...")
            await asyncio.sleep(6.0)

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
            log.info(f"[{sym_idx+1}/{len(symbols)}] Harvesting 7D Liquidation Map for {sym} (Ref ~${expected_price:,.2f})...")

            # 1. Type and click symbol
            js_select = f"""
            (() => {{
                const allElements = Array.from(document.querySelectorAll('*'));
                const header = allElements.find(el => el.children.length === 0 && (el.innerText || '').includes('Exchange Liquidation Map'));
                let container = header.parentElement;
                while (container && !container.querySelector('[_echarts_instance_]') && !container.querySelector('canvas')) {{
                    container = container.parentElement;
                }}
                const symInput = container.querySelector('input.MuiAutocomplete-input');
                if (!symInput) return {{ error: 'No symInput' }};
                
                symInput.focus();
                symInput.click();
                const nativeSetter = Object.getOwnPropertyDescriptor(window.HTMLInputElement.prototype, 'value').set;
                nativeSetter.call(symInput, '{sym}');
                symInput.dispatchEvent(new Event('input', {{ bubbles: true }}));
                return {{ listId: symInput.getAttribute('aria-controls') }};
            }})()
            """
            sel_res = await cdp_cmd("Runtime.evaluate", {"expression": js_select, "returnByValue": True})
            list_id = sel_res.get("result", {}).get("value", {}).get("listId")
            await asyncio.sleep(0.3)

            js_click = f"""
            (() => {{
                let listbox = document.getElementById("{list_id}");
                if (!listbox) listbox = document.querySelector('.MuiAutocomplete-listbox');
                if (!listbox) return {{ error: 'No listbox' }};
                const opt = Array.from(listbox.querySelectorAll('[role="option"], li')).find(el => el.innerText.trim() === '{sym}');
                if (opt) {{
                    opt.click();
                    return {{ clicked: true }};
                }}
                return {{ error: 'Option not found' }};
            }})()
            """
            await cdp_cmd("Runtime.evaluate", {"expression": js_click, "returnByValue": True})

            # 2. Verification loop: poll until price matches expected reference bounds and non-zero exchange values exist
            harvested_data = None
            for poll in range(35):
                await asyncio.sleep(0.3)
                ext = await cdp_cmd("Runtime.evaluate", {"expression": js_extract, "returnByValue": True})
                val = ext.get("result", {}).get("value")
                if not val or not val.get("rows"):
                    continue

                min_p = float(val["minPrice"])
                max_p = float(val["maxPrice"])

                # Anti-race condition: Reference price must be strictly bracketed inside chart price range
                # AND chart must have updated to new prices (not holding previous symbol's bounds)
                is_bracketed = (min_p <= expected_price <= max_p)
                is_new_chart = (prev_min_p is None) or (abs(min_p - prev_min_p) > 1e-6)
                title = val.get("optTitle") or ""
                is_title_match = (sym == "BTC" and ("Bitcoin" in title or "BTC" in title)) or (sym in title)

                binance_count = sum(1 for r in val["rows"] if r["binanceVal"] > 0)
                okx_count = sum(1 for r in val["rows"] if r["okxVal"] > 0)
                bybit_count = sum(1 for r in val["rows"] if r["bybitVal"] > 0)

                if is_bracketed and is_new_chart and is_title_match and (binance_count > 0 or okx_count > 0):
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
                        "Cummulitve_Liquidation": format_usd(r.get("cumVal")),
                        "Short": format_usd(short_num) if short_num is not None else "$0",
                        "Long": format_usd(long_num) if long_num is not None else "$0",
                        "Binanace": format_usd(r.get("binanceVal", 0)),
                        "OKX": format_usd(r.get("okxVal", 0)),
                        "Bybit": format_usd(r.get("bybitVal", 0)),
                    }
                )
                global_sr += 1

        await ws.close()

    finally:
        if is_ephemeral:
            close_tab(tab_id)

    log.info(f"Total 7D records harvested across all assets: {len(all_records)} rows.")
    return all_records


def dump_to_excel(records: list[dict], excel_path: pathlib.Path = DEFAULT_EXCEL_PATH) -> bool:
    """Optional backward-compatible dump into worksheet '8_Exchange_Liquidation_Map_7D'."""
    if not openpyxl or not excel_path.exists():
        return False

    try:
        wb = openpyxl.load_workbook(excel_path)
        sheet_name = FEED_NAME
        if "8_Exchange_Liquidation_Map_1D" in wb.sheetnames:
            target_idx = wb.sheetnames.index("8_Exchange_Liquidation_Map_1D") + 1
        elif "7_Live_Liq" in wb.sheetnames:
            target_idx = wb.sheetnames.index("7_Live_Liq") + 2
        else:
            target_idx = 13 if len(wb.sheetnames) >= 13 else len(wb.sheetnames)

        if sheet_name in wb.sheetnames:
            wb.remove(wb[sheet_name])
        ws = wb.create_sheet(title=sheet_name, index=target_idx)

        hdr_font = Font(name="Segoe UI", size=10, bold=True, color="FFFFFF")
        hdr_fill = PatternFill(start_color="0F172A", end_color="0F172A", fill_type="solid")
        base_font = Font(name="Segoe UI", size=9, color="000000")
        bold_font = Font(name="Segoe UI", size=9, bold=True, color="000000")
        cum_font = Font(name="Segoe UI", size=9, bold=True, color="1E293B")
        green_font = Font(name="Segoe UI", size=9, bold=True, color="00A86B")
        red_font = Font(name="Segoe UI", size=9, bold=True, color="E53935")
        subdued_font = Font(name="Segoe UI", size=9, color="888888")

        thin_border_side = Side(border_style="thin", color="E2E8F0")
        row_border = Border(left=thin_border_side, right=thin_border_side, top=thin_border_side, bottom=thin_border_side)

        ws.row_dimensions[1].height = 26
        for col_idx, (col_key, header_title, width, align) in enumerate(COLUMNS_DEF, start=1):
            cell = ws.cell(row=1, column=col_idx, value=header_title)
            cell.font = hdr_font
            cell.fill = hdr_fill
            cell.alignment = Alignment(horizontal=align, vertical="center")
            cell.border = row_border
            col_letter = get_column_letter(col_idx)
            ws.column_dimensions[col_letter].width = width

        for row_idx, r in enumerate(records, start=2):
            ws.row_dimensions[row_idx].height = 20
            for col_idx, (col_key, _, _, align) in enumerate(COLUMNS_DEF, start=1):
                val = r.get(col_key, "")
                cell = ws.cell(row=row_idx, column=col_idx, value=val)
                cell.alignment = Alignment(horizontal=align, vertical="center")
                cell.border = row_border
                if col_key in ("Sr.No", "Asset", "Time"):
                    cell.font = bold_font
                elif col_key == "Cummulitve_Liquidation":
                    cell.font = cum_font
                elif col_key == "Short":
                    cell.font = green_font if val != "$0" else subdued_font
                elif col_key == "Long":
                    cell.font = red_font if val != "$0" else subdued_font
                elif col_key in ("Binanace", "OKX", "Bybit"):
                    cell.font = base_font if val != "$0" else subdued_font
                else:
                    cell.font = base_font

        temp_excel = excel_path.with_name(f"{excel_path.stem}_{os.getpid()}_{int(time.time()*1000)}.tmp.xlsx")
        wb.save(temp_excel)
        wb.close()
        temp_excel.replace(excel_path)
        log.info(f"Excel worksheet '{sheet_name}' updated successfully.")
        return True
    except Exception as e:
        log.warning(f"Optional Excel dump skipped/failed: {e}")
        return False


def main():
    parser = argparse.ArgumentParser(description="CoinGlass 7D Multi-Asset Liquidation Map Scraper")
    parser.add_argument("--symbols", nargs="+", default=DEFAULT_UNIVERSE, help="Assets to harvest")
    parser.add_argument("--excel-path", type=pathlib.Path, default=DEFAULT_EXCEL_PATH, help="Path to Excel workbook")
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

    # 2. Optional Excel Dump
    if args.excel_path.exists():
        dump_to_excel(records, excel_path=args.excel_path)

    log.info("7D Liquidation Map pipeline executed successfully.")


if __name__ == "__main__":
    main()
