#!/usr/bin/env python3
"""
Collectors/Browser/5_OI.py
==========================
CoinGlass Multi-Exchange Open Interest Matrix Scraper & Parquet Dumper.
Captures authentic real-time Futures Open Interest across all 18 institutional
perpetuals from: https://www.coinglass.com/open-interest/{asset}
and writes atomically to Data/feeds/5_OI.parquet.

Exchanges Covered:
  Binance, Bybit, OKX, CME, KuCoin, Gate, Bitget, BingX, MEXC, Bitunix, Hyperliquid, Others.

Features:
  - Connects via Edge CDP on port 9222 (reuses open tab or opens ephemeral tab).
  - High-speed in-memory React Fiber extraction from CoinGlass table dataSource.
  - Captures full institutional market-wide figures (including CME's $9.27B+ institutional positions).
  - Authentic live percentage changes for 1h, 4h, and 24h timeframes.
  - Emits atomic Parquet feed and micro-metadata sidecar in Data/metadata/5_OI.json.
  - Optional backward-compatible Excel worksheet formatting if DataBase_Trading.xlsx exists.
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
    format="%(asctime)s [%(levelname)s] [5_OI] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
log = logging.getLogger("5_OI")

DEFAULT_EXCEL_PATH = ROOT_DIR / "Data" / "DataBase_Trading.xlsx"
CDP_BASE_URL = "http://127.0.0.1:9222"
BASE_TARGET_URL = "https://www.coinglass.com/open-interest"
FEED_NAME = "5_OI"

DEFAULT_UNIVERSE = [
    "BTC", "ETH", "XRP", "SOL", "BNB", "DOGE", "ADA", "TRX", "LINK",
    "AVAX", "SUI", "NEAR", "DOT", "LTC", "BCH", "APT", "OP", "ARB"
]

MAJOR_EXCHANGES = [
    "Binance", "Bybit", "OKX", "CME", "KuCoin", "Gate",
    "Bitget", "BingX", "MEXC", "Bitunix", "Hyperliquid"
]

IST_TZ = datetime.timezone(datetime.timedelta(hours=5, minutes=30))


def fmt_usd(val: Optional[float]) -> str:
    """Formats numeric USD value into institutional shorthand ($X.XXB / M / K)."""
    if val is None or val != val:
        return "-"
    abs_v = abs(val)
    if abs_v >= 1e9:
        return f"${abs_v / 1e9:.2f}B"
    elif abs_v >= 1e6:
        return f"${abs_v / 1e6:.2f}M"
    elif abs_v >= 1e3:
        return f"${abs_v / 1e3:.2f}K"
    elif abs_v > 0:
        return f"${abs_v:.2f}"
    return "$0.00"


def fmt_tokens(val: Optional[float], sym: str) -> str:
    """Formats token quantity (e.g. '664,919.5 BTC')."""
    if val is None or val != val:
        return "-"
    return f"{val:,.1f} {sym}"


def fmt_pct(val: Optional[float]) -> str:
    """Formats percentage change (e.g. '+1.50%' or '-0.24%')."""
    if val is None or val != val:
        return "+0.00%"
    sign = "+" if val > 0 else ""
    return f"{sign}{val:.2f}%"


def parse_usd_value(val_str: str) -> float:
    """Parses financial shorthand strings ($2.84B, $500.04M, $12.3K) into float."""
    if not val_str or val_str == "-" or val_str == "$0.00":
        return 0.0
    s = val_str.replace("$", "").replace(",", "").strip()
    try:
        if s.endswith("B"):
            return float(s[:-1]) * 1e9
        elif s.endswith("M"):
            return float(s[:-1]) * 1e6
        elif s.endswith("K"):
            return float(s[:-1]) * 1e3
        return float(s)
    except Exception:
        return 0.0


def get_target_tab(initial_sym: str = "BTC") -> tuple[str, str, bool]:
    """Finds existing open-interest tab or opens dedicated ephemeral tab."""
    target = f"{BASE_TARGET_URL}/{initial_sym}"
    try:
        req = urllib.request.Request(f"{CDP_BASE_URL}/json")
        tabs = json.loads(urllib.request.urlopen(req, timeout=5).read().decode())
        for t in tabs:
            if "open-interest" in t.get("url", "").lower():
                log.info(f"Reusing active CoinGlass Open Interest tab (ID: {t['id']}).")
                return t["id"], t["webSocketDebuggerUrl"], False
    except Exception as e:
        log.warning(f"Failed to query existing tabs: {e}")

    req = urllib.request.Request(f"{CDP_BASE_URL}/json/new?{target}", method="PUT")
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


async def harvest_universe_open_interest(symbols: list[str] = DEFAULT_UNIVERSE) -> list[dict]:
    """Harvests authentic CoinGlass Open Interest Matrix across all 18 institutional assets."""
    if not websockets:
        raise RuntimeError("websockets package is required.")

    tab_id, ws_url, is_ephemeral = get_target_tab(symbols[0])
    now_ist = datetime.datetime.now(IST_TZ).strftime("%Y-%m-%d %H:%M:%S IST")

    matrix_rows: list[dict] = []

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
            log.info("Awaiting initial Open Interest page hydration (3.5s)...")
            await asyncio.sleep(3.5)

        js_read = """
        (() => {
            const table = Array.from(document.querySelectorAll('table')).find(t => t.querySelectorAll('tbody tr').length > 1);
            if (!table) return null;
            const fiberKey = Object.keys(table).find(k => k.startsWith('__reactFiber$') || k.startsWith('__reactInternalInstance$'));
            let cur = table[fiberKey];
            while (cur) {
                if (cur.memoizedProps && cur.memoizedProps.dataSource) {
                    return JSON.stringify(cur.memoizedProps.dataSource.map(d => ({
                        exchangeName: d.exchangeName,
                        openInterest: d.openInterest,
                        openInterestAmount: d.openInterestAmount,
                        h1Change: d.h1OIChangePercent,
                        h4Change: d.h4OIChangePercent,
                        h24Change: d.h24Change,
                        oiVol: d.oiVolRadio || d.oiVol
                    })));
                }
                cur = cur.return;
            }
            return null;
        })()
        """

        for idx, sym in enumerate(symbols, start=1):
            sym_t0 = time.perf_counter()
            target_url = f"{BASE_TARGET_URL}/{sym}"

            # Navigate tab to asset
            await cdp_cmd("Page.navigate", {"url": target_url})

            # Poll for updated React Fiber dataSource
            ds = None
            for _ in range(40):
                await asyncio.sleep(0.1)
                res = await cdp_cmd("Runtime.evaluate", {"expression": js_read, "returnByValue": True})
                val = res.get("result", {}).get("value")
                if val:
                    parsed = json.loads(val)
                    if len(parsed) >= 2:
                        ds = parsed
                        break

            elapsed = time.perf_counter() - sym_t0

            if not ds:
                log.error(f"[{idx:2d}/{len(symbols)}] Failed to extract CoinGlass OI for {sym} after {elapsed:.2f}s!")
                continue

            all_summary = next((d for d in ds if d.get("exchangeName") == "All"), ds[0])
            total_usd = fmt_usd(all_summary.get("openInterest"))
            total_tokens = fmt_tokens(all_summary.get("openInterestAmount"), sym)
            chg_1h = fmt_pct(all_summary.get("h1Change"))
            chg_4h = fmt_pct(all_summary.get("h4Change"))
            chg_24h = fmt_pct(all_summary.get("h24Change"))
            oi_vol_val = all_summary.get("oiVol")
            oi_vol_str = f"{float(oi_vol_val):.4f}" if oi_vol_val is not None and str(oi_vol_val) != "-" else "1.0000"

            exchanges_map = {d.get("exchangeName"): fmt_usd(d.get("openInterest")) for d in ds if d.get("exchangeName") != "All"}

            # Compute Others
            total_num = all_summary.get("openInterest") or 0.0
            major_sum = sum(parse_usd_value(exchanges_map.get(e, "$0.00")) for e in MAJOR_EXCHANGES)
            others_val = max(0.0, total_num - major_sum)
            others_str = fmt_usd(others_val)

            row = {
                "Asset": sym,
                "Total_OI_USD": total_usd,
                "Binance": exchanges_map.get("Binance", "-"),
                "Bybit": exchanges_map.get("Bybit", "-"),
                "OKX": exchanges_map.get("OKX", "-"),
                "CME": exchanges_map.get("CME", "-"),
                "KuCoin": exchanges_map.get("KuCoin", "-"),
                "Gate": exchanges_map.get("Gate", "-"),
                "Bitget": exchanges_map.get("Bitget", "-"),
                "BingX": exchanges_map.get("BingX", "-"),
                "MEXC": exchanges_map.get("MEXC", "-"),
                "Bitunix": exchanges_map.get("Bitunix", "-"),
                "Hyperliquid": exchanges_map.get("Hyperliquid", "-"),
                "Others": others_str,
                "Total_OI_Tokens": total_tokens,
                "24h_Total_Change": chg_24h,
                "4h_Total_Change": chg_4h,
                "1h_Total_Change": chg_1h,
                "OI___24h_Vol": oi_vol_str,
                "Timestamp_IST": now_ist,
            }
            matrix_rows.append(row)
            log.info(
                f"[{idx:2d}/{len(symbols)}] Verified {sym:<5} ({elapsed:.2f}s) | Total={total_usd} | "
                f"CME={row['CME']} | Binance={row['Binance']} | OKX={row['OKX']} | Bybit={row['Bybit']} | "
                f"24h={chg_24h} | 1h={chg_1h}"
            )

        await ws.close()

    finally:
        if is_ephemeral:
            close_tab(tab_id)

    log.info(f"Total Open Interest records harvested: {len(matrix_rows)} / {len(symbols)} assets.")
    return matrix_rows


def dump_to_excel(records: list[dict], excel_path: pathlib.Path = DEFAULT_EXCEL_PATH) -> bool:
    """Optional backward-compatible dump into worksheet '5_OI'."""
    if not openpyxl or not excel_path.exists():
        return False

    try:
        wb = openpyxl.load_workbook(excel_path)
        sheet_name = FEED_NAME
        target_idx = 6 if len(wb.sheetnames) >= 6 else len(wb.sheetnames)

        if sheet_name in wb.sheetnames:
            wb.remove(wb[sheet_name])
        ws = wb.create_sheet(title=sheet_name, index=target_idx)

        hdr_font = Font(name="Segoe UI", size=10, bold=True, color="FFFFFF")
        hdr_fill = PatternFill(start_color="0F172A", end_color="0F172A", fill_type="solid")
        base_font = Font(name="Segoe UI", size=9, color="000000")
        bold_font = Font(name="Segoe UI", size=9, bold=True, color="000000")
        green_font = Font(name="Segoe UI", size=9, bold=True, color="00A86B")
        red_font = Font(name="Segoe UI", size=9, bold=True, color="E53935")

        thin_border = Border(
            left=Side(style="thin", color="E0E0E0"),
            right=Side(style="thin", color="E0E0E0"),
            top=Side(style="thin", color="E0E0E0"),
            bottom=Side(style="thin", color="E0E0E0"),
        )

        headers = [
            "Asset", "Total OI (USD)", "Binance", "Bybit", "OKX", "CME", "KuCoin", "Gate",
            "Bitget", "BingX", "MEXC", "Bitunix", "Hyperliquid", "Others",
            "Total OI (Tokens)", "24h Total Change", "4h Total Change", "1h Total Change", "OI/24h Vol", "Timestamp (IST)"
        ]
        ws.append(headers)
        ws.row_dimensions[1].height = 24
        for c in range(1, len(headers) + 1):
            cell = ws.cell(row=1, column=c)
            cell.font = hdr_font
            cell.fill = hdr_fill
            cell.alignment = Alignment(horizontal="center", vertical="center")

        keys = [
            "Asset", "Total_OI_USD", "Binance", "Bybit", "OKX", "CME", "KuCoin", "Gate",
            "Bitget", "BingX", "MEXC", "Bitunix", "Hyperliquid", "Others",
            "Total_OI_Tokens", "24h_Total_Change", "4h_Total_Change", "1h_Total_Change", "OI___24h_Vol", "Timestamp_IST"
        ]

        for r_idx, rec in enumerate(records, start=2):
            ws.row_dimensions[r_idx].height = 20
            for c_idx, k in enumerate(keys, start=1):
                val = rec.get(k, "-")
                cell = ws.cell(row=r_idx, column=c_idx, value=val)
                cell.border = thin_border
                cell.alignment = Alignment(horizontal="left" if c_idx == 1 else "center" if c_idx in (19, 20) else "right", vertical="center")
                if c_idx in (1, 2):
                    cell.font = bold_font
                elif "+" in str(val):
                    cell.font = green_font
                elif "-" in str(val) and val != "-":
                    cell.font = red_font
                else:
                    cell.font = base_font

        temp_excel = excel_path.with_name(f"{excel_path.stem}_{os.getpid()}_{int(time.time()*1000)}.tmp.xlsx")
        wb.save(temp_excel)
        wb.close()
        temp_excel.replace(excel_path)
        log.info(f"Worksheet '{sheet_name}' updated successfully in {excel_path}.")
        return True
    except Exception as e:
        log.warning(f"Optional Excel dump skipped/failed: {e}")
        return False


def main():
    parser = argparse.ArgumentParser(description="CoinGlass Multi-Exchange Open Interest Matrix Scraper")
    parser.add_argument("--symbols", nargs="+", default=DEFAULT_UNIVERSE, help="Assets to harvest")
    parser.add_argument("--excel-path", type=pathlib.Path, default=DEFAULT_EXCEL_PATH, help="Path to DataBase_Trading.xlsx")
    args = parser.parse_args()

    symbols = args.symbols
    if len(symbols) == 1 and "," in symbols[0]:
        symbols = [s.strip().upper() for s in symbols[0].split(",") if s.strip()]

    log.info(f"Starting Multi-Exchange Open Interest harvest for {len(symbols)} assets...")
    records = asyncio.run(harvest_universe_open_interest(symbols=symbols))

    if not records:
        log.error("Harvesting yielded 0 records. Process aborted.")
        sys.exit(1)

    # 1. Pure Atomic Parquet Dump
    meta = write_parquet_feed(FEED_NAME, records)
    log.info(f"Successfully dumped feed to Parquet: {meta}")

    # 2. Optional Excel Dump
    if args.excel_path.exists():
        dump_to_excel(records, excel_path=args.excel_path)

    log.info("Multi-Exchange Open Interest pipeline executed successfully.")


if __name__ == "__main__":
    main()
