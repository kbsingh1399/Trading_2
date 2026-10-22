#!/usr/bin/env python3
"""
Data/Excel_Modules/8_Exchange_Liquidation_Map_7D.py
==================================================
CoinGlass Multi-Asset Exchange Liquidation Map (7-Day Window) Scraper & Excel Dumper.
Switches to the '7 day' timeframe dropdown and captures multi-exchange liquidation
leverage levels across price points for all 18 institutional perpetual assets in the trading universe
from https://www.coinglass.com/pro/futures/LiquidationMap and stacks them into worksheet
'8_Exchange_Liquidation_Map_7D' in Data/DataBase_Trading.xlsx (positioned at Index 12,
immediately after '8_Exchange_Liquidation_Map_1D').

Universe (18 Institutional Binance USDT-M Perpetuals):
  BTC, ETH, XRP, SOL, BNB, DOGE, ADA, TRX, LINK, AVAX, SUI, NEAR, DOT, LTC, BCH, APT, OP, ARB

Layout Matches Operator Image 4 Format:
  Sr.No | Asset | Time | TimeStamp | Price | Cummulitve Liquidation | Short | Long | Binanace | OKX | Bybit

Security & Cleanliness Invariants:
  - Ephemeral CDP tab on port 9222 opened and strictly closed in finally: block.
  - Preserves arena.ai tab untouched.
  - Zero external browser window pollution.
"""

from __future__ import annotations

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
    import openpyxl
    from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
    from openpyxl.utils import get_column_letter
except ImportError:
    openpyxl = None

try:
    import websockets
except ImportError:
    websockets = None

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] [%(name)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
log = logging.getLogger("8_Exchange_Liquidation_Map_7D")

MODULES_DIR = pathlib.Path(__file__).resolve().parent
ROOT_DIR = MODULES_DIR.parents[1]
DEFAULT_EXCEL_PATH = ROOT_DIR / "Data" / "DataBase_Trading.xlsx"
CDP_BASE_URL = "http://127.0.0.1:9222"
TARGET_URL = "https://www.coinglass.com/pro/futures/LiquidationMap"
SHEET_NAME = "8_Exchange_Liquidation_Map_7D"

# Canonical 18 Institutional Binance USDT-M Perpetual Universe
DEFAULT_UNIVERSE = [
    "BTC", "ETH", "XRP", "SOL", "BNB",
    "DOGE", "ADA", "TRX", "LINK", "AVAX",
    "SUI", "NEAR", "DOT", "LTC", "BCH",
    "APT", "OP", "ARB",
]

COLUMNS_DEF = [
    ("sr_no", "Sr.No", 10, "center"),
    ("asset", "Asset", 12, "center"),
    ("time_window", "Time", 10, "center"),
    ("timestamp_utc", "TimeStamp", 24, "center"),
    ("price", "Price", 16, "right"),
    ("cumulative_liq", "Cummulitve Liquidation", 24, "right"),
    ("short_liq", "Short", 20, "right"),
    ("long_liq", "Long", 20, "right"),
    ("binance", "Binanace", 18, "right"),
    ("okx", "OKX", 18, "right"),
    ("bybit", "Bybit", 18, "right"),
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


async def harvest_exchange_liquidation_map_7d(symbols: list[str] = DEFAULT_UNIVERSE) -> list[dict]:
    """Navigates to LiquidationMap, sets '7 day' timeframe, and extracts data for all symbols."""
    if not websockets:
        raise RuntimeError("websockets package is required.")

    tab_id, ws_url = open_ephemeral_tab()
    log.info(f"Opened dedicated ephemeral tab (ID: {tab_id}) for 7D Multi-Asset harvest ({len(symbols)} assets).")

    now_dt = datetime.datetime.now(datetime.timezone.utc)
    ts_str = now_dt.strftime("%Y-%m-%d %H:%M:%S UTC")

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
        log.info("Awaiting page hydration (6s)...")
        await asyncio.sleep(6)

        # 1. Switch timeframe to 7 day
        switch_7d_js = """
        async () => {
            const echartsDoms = Array.from(document.querySelectorAll('[_echarts_instance_]'));
            const chartDom = echartsDoms[1];
            if (!chartDom) return { error: 'Exchange Liquidation Map chart not found' };
            
            let container = chartDom.parentElement;
            while (container && !container.innerText.includes('Exchange Liquidation Map')) {
                container = container.parentElement;
            }
            if (!container) return { error: 'Container not found' };
            
            const timeBtn = container.querySelector('.MuiSelect-button');
            if (!timeBtn) return { error: 'Time dropdown button not found' };
            
            const controlsId = timeBtn.getAttribute('aria-controls');
            timeBtn.click();
            await new Promise(r => setTimeout(r, 600));
            
            const listbox = controlsId ? document.getElementById(controlsId) : document.querySelector('[role="listbox"]');
            if (!listbox) return { error: 'Time listbox not found' };
            
            const opt7 = Array.from(listbox.querySelectorAll('[role="option"], li')).find(el => el.innerText.trim() === '7 day');
            if (!opt7) return { error: '7 day option not found in listbox' };
            
            opt7.click();
            return { switched: true };
        }
        """

        log.info("Switching timeframe to 7-Day window...")
        sw_res = await cdp_cmd("Runtime.evaluate", {
            "expression": f"({switch_7d_js})()",
            "awaitPromise": True,
            "returnByValue": True
        })
        sw_val = sw_res.get("result", {}).get("value", {})
        if sw_val.get("error"):
            log.warning(f"Warning during 7D timeframe switch: {sw_val.get('error')}")

        # Wait for 7D network response for initial asset (BTC)
        end_wait = asyncio.get_event_loop().time() + 8
        while asyncio.get_event_loop().time() < end_wait:
            try:
                msg = await asyncio.wait_for(ws.recv(), timeout=1)
                d = json.loads(msg)
                if d.get("method") == "Network.responseReceived":
                    url = d.get("params", {}).get("response", {}).get("url", "")
                    if "exLiqMap" in url and "interval=5" in url:
                        log.info(f"7D initial BTC response received: {url}")
                        break
            except asyncio.TimeoutError:
                pass

        await asyncio.sleep(1.0)

        open_popup_js = """
        () => {
            const echartsDoms = Array.from(document.querySelectorAll('[_echarts_instance_]'));
            const chartDom = echartsDoms[1];
            if (!chartDom) return false;
            let container = chartDom.parentElement;
            while (container && !container.innerText.includes('Exchange Liquidation Map')) {
                container = container.parentElement;
            }
            if (!container) return false;
            const popupBtn = container.querySelector('.MuiAutocomplete-popupIndicator');
            if (popupBtn) {
                popupBtn.click();
                return true;
            }
            return false;
        }
        """

        click_symbol_js = """
        (targetSymbol) => {
            const listbox = document.querySelector('.MuiAutocomplete-listbox') || document.querySelector('[role="listbox"]');
            if (!listbox) return { error: 'Listbox not found' };
            const optEl = Array.from(listbox.querySelectorAll('li, [role="option"]')).find(el => el.innerText.trim() === targetSymbol);
            if (!optEl) return { error: `Symbol ${targetSymbol} not found in listbox` };
            optEl.click();
            return { clicked: true };
        }
        """

        extract_opt_js = """
        (targetSymbol) => {
            const echartsDoms = Array.from(document.querySelectorAll('[_echarts_instance_]'));
            const chartDom = echartsDoms[1];
            if (!chartDom) return { error: 'Chart DOM not found' };
            
            const fiberKey = Object.keys(chartDom).find(k => k.startsWith('__reactFiber$') || k.startsWith('__reactInternalInstance$'));
            if (!fiberKey) return { error: 'No React fiberKey' };
            
            const options = [];
            let f = chartDom[fiberKey];
            while (f) {
                const p = f.memoizedProps || {};
                if (p.option && p.option.xAxis && p.option.xAxis[0] && p.option.xAxis[0].data) {
                    options.push({
                        title: p.title || '',
                        option: p.option
                    });
                }
                f = f.return;
            }
            
            const isBtc = (targetSymbol === 'BTC');
            const matched = options.filter(o => {
                if (isBtc) {
                    return o.title.includes('BTC') || o.title.includes('Bitcoin');
                }
                return o.title.includes(targetSymbol);
            });
            
            if (!matched.length) {
                return { error: `No options found matching title ${targetSymbol}`, totalFound: options.length };
            }
            
            const best = matched[matched.length - 1];
            const opt = best.option;
            const prices = (opt.xAxis && opt.xAxis[0] ? opt.xAxis[0].data : []) || [];
            const series = opt.series || [];
            
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
            return { rows };
        }
        """

        global_sr_no = 1

        for sym_idx, sym in enumerate(symbols):
            log.info(f"[{sym_idx+1}/{len(symbols)}] Harvesting 7D Liquidation Map for {sym}...")
            
            # For the first symbol if BTC, it's already switched to 7D above
            if sym_idx == 0 and sym == "BTC":
                pass
            else:
                # 1. Open popup
                await cdp_cmd("Runtime.evaluate", {"expression": f"({open_popup_js})()"})
                await asyncio.sleep(0.4)
                
                # 2. Click target symbol
                click_res = await cdp_cmd("Runtime.evaluate", {
                    "expression": f"({click_symbol_js})('{sym}')",
                    "returnByValue": True
                })
                click_val = click_res.get("result", {}).get("value", {})
                if click_val.get("error"):
                    log.warning(f"Failed to click symbol {sym}: {click_val.get('error')}. Retrying with re-open...")
                    await cdp_cmd("Runtime.evaluate", {"expression": f"({open_popup_js})()"})
                    await asyncio.sleep(0.5)
                    await cdp_cmd("Runtime.evaluate", {
                        "expression": f"({click_symbol_js})('{sym}')",
                        "returnByValue": True
                    })

                # 3. Wait for 7D Network response for this symbol
                response_seen = False
                end_wait = asyncio.get_event_loop().time() + 8
                while asyncio.get_event_loop().time() < end_wait:
                    try:
                        msg = await asyncio.wait_for(ws.recv(), timeout=1)
                        d = json.loads(msg)
                        if d.get("method") == "Network.responseReceived":
                            url = d.get("params", {}).get("response", {}).get("url", "")
                            if "exLiqMap" in url and f"symbol={sym}" in url and "interval=5" in url:
                                response_seen = True
                                break
                    except asyncio.TimeoutError:
                        pass

                if not response_seen:
                    log.warning(f"7D exLiqMap network event not observed for {sym}, proceeding with fiber fallback...")

                # Allow React state and fiber tree to settle
                await asyncio.sleep(0.8)

            # 4. Extract data from fiber
            eval_res = await cdp_cmd("Runtime.evaluate", {
                "expression": f"({extract_opt_js})('{sym}')",
                "returnByValue": True
            })
            val = eval_res.get("result", {}).get("value", {})
            if val.get("error"):
                log.error(f"Error extracting 7D data for {sym}: {val.get('error')}")
                continue

            raw_rows = val.get("rows", [])
            log.info(f"Extracted {len(raw_rows)} 7D price levels for {sym}.")

            for r in raw_rows:
                price = r.get("price")
                cum_num = r.get("cumVal")
                short_num = r.get("shortVal")
                long_num = r.get("longVal")
                binance_num = r.get("binanceVal", 0)
                okx_num = r.get("okxVal", 0)
                bybit_num = r.get("bybitVal", 0)

                all_records.append(
                    {
                        "sr_no": global_sr_no,
                        "asset": sym,
                        "time_window": "7D",
                        "timestamp_utc": ts_str,
                        "price": price,
                        "cumulative_liq": format_usd(cum_num),
                        "short_liq": format_usd(short_num) if short_num is not None else "$0",
                        "long_liq": format_usd(long_num) if long_num is not None else "$0",
                        "binance": format_usd(binance_num),
                        "okx": format_usd(okx_num),
                        "bybit": format_usd(bybit_num),
                    }
                )
                global_sr_no += 1

        await ws.close()

    finally:
        close_tab(tab_id)

    log.info(f"Total 7D records harvested across all assets: {len(all_records)} rows.")
    return all_records


def dump_to_excel(records: list[dict], excel_path: pathlib.Path = DEFAULT_EXCEL_PATH) -> bool:
    """Dumps 7-Day multi-asset liquidation map data into worksheet '8_Exchange_Liquidation_Map_7D'."""
    if not excel_path.exists():
        log.error(f"Excel workbook not found at: {excel_path}")
        return False

    if not records:
        log.error("Integrity guard: 0 records extracted. Aborting dump to prevent empty sheet.")
        return False

    wb = openpyxl.load_workbook(excel_path)

    # Place sheet immediately after 8_Exchange_Liquidation_Map_1D
    if "8_Exchange_Liquidation_Map_1D" in wb.sheetnames:
        target_idx = wb.sheetnames.index("8_Exchange_Liquidation_Map_1D") + 1
    else:
        target_idx = 13 if len(wb.sheetnames) >= 13 else len(wb.sheetnames)

    if SHEET_NAME in wb.sheetnames:
        wb.remove(wb[SHEET_NAME])
    ws = wb.create_sheet(title=SHEET_NAME, index=target_idx)

    log.info(f"Target worksheet '{SHEET_NAME}' positioned at index {wb.sheetnames.index(SHEET_NAME)}")

    # Visual Styles
    hdr_font = Font(name="Segoe UI", size=10, bold=True, color="FFFFFF")
    hdr_fill = PatternFill(start_color="0F172A", end_color="0F172A", fill_type="solid")

    base_font = Font(name="Segoe UI", size=9, color="000000")
    bold_font = Font(name="Segoe UI", size=9, bold=True, color="000000")
    cum_font = Font(name="Segoe UI", size=9, bold=True, color="1E293B")
    green_font = Font(name="Segoe UI", size=9, bold=True, color="00A86B")
    red_font = Font(name="Segoe UI", size=9, bold=True, color="E53935")
    subdued_font = Font(name="Segoe UI", size=9, color="888888")

    thin_border_side = Side(border_style="thin", color="E2E8F0")
    row_border = Border(
        left=thin_border_side, right=thin_border_side, top=thin_border_side, bottom=thin_border_side
    )

    # 1. Header Row
    ws.row_dimensions[1].height = 26
    for col_idx, (col_key, header_title, width, align) in enumerate(COLUMNS_DEF, start=1):
        cell = ws.cell(row=1, column=col_idx, value=header_title)
        cell.font = hdr_font
        cell.fill = hdr_fill
        cell.alignment = Alignment(horizontal=align, vertical="center")
        cell.border = row_border
        col_letter = get_column_letter(col_idx)
        ws.column_dimensions[col_letter].width = width

    # 2. Data Rows
    for row_idx, r in enumerate(records, start=2):
        ws.row_dimensions[row_idx].height = 20
        for col_idx, (col_key, _, _, align) in enumerate(COLUMNS_DEF, start=1):
            val = r.get(col_key, "")
            cell = ws.cell(row=row_idx, column=col_idx, value=val)
            cell.alignment = Alignment(horizontal=align, vertical="center")
            cell.border = row_border

            # Typography and semantics
            if col_key in ("sr_no", "asset", "time_window"):
                cell.font = bold_font
            elif col_key == "cumulative_liq":
                cell.font = cum_font
            elif col_key == "short_liq":
                cell.font = green_font if val != "$0" else subdued_font
            elif col_key == "long_liq":
                cell.font = red_font if val != "$0" else subdued_font
            elif col_key in ("binance", "okx", "bybit"):
                cell.font = base_font if val != "$0" else subdued_font
            else:
                cell.font = base_font

    ws.freeze_panes = "A2"

    import os, time
    temp_excel = excel_path.with_name(f"{excel_path.stem}_{os.getpid()}_{int(time.time()*1000)}.tmp.xlsx")
    wb.save(temp_excel)
    wb.close()
    import time, zipfile
    _is_valid = False
    with zipfile.ZipFile(temp_excel, "r") as _z:
        _is_valid = (_z.testzip() is None)
    if _is_valid:
        for _att in range(10):
            try:
                temp_excel.replace(excel_path)
                break
            except PermissionError:
                if _att == 9: raise
                time.sleep(0.5)
    else:
        if temp_excel.exists(): temp_excel.unlink()
        raise ValueError("Corrupt zip produced during export")
    log.info(f"Successfully saved {len(records)} rows to '{SHEET_NAME}' at {excel_path}")
    return True


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
        log.error("Harvesting yielded 0 records. Excel dump aborted.")
        sys.exit(1)

    success = dump_to_excel(records, excel_path=args.excel_path)
    if not success:
        sys.exit(1)

    log.info("7D Liquidation Map pipeline executed successfully.")


if __name__ == "__main__":
    main()
