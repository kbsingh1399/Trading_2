#!/usr/bin/env python3
"""
Data/Excel_Modules/12_Hyperdash.py
==================================
Dedicated Excel Module 20: Hyperdash On-Chain Flow & Microstructure Intelligence.
Extracts and consolidates comprehensive intelligence from Hyperdash GraphQL API
(https://api.hyperdash.com/graphql) and Hyperdash On-Chain Flow Engine:
  - Section 1: Macro Hyperdash On-Chain Intelligence Summary & Telemetry
  - Section 2: Universe Per-Asset On-Chain Flow Attribution Matrix
  - Section 3: Level 3 Institutional Resting Whale Orders (Mapped to Ethereum Hex Addresses)
  - Section 4: Top Liquidation Clusters & Liquidation Whale Addresses (BTC & ETH)
  - Section 5: Top Stop-Loss Clusters & Whale Stop Addresses (BTC & ETH)
  - Section 6: Recent Confirmed On-Chain Liquidations Feed (Hyperliquid L1)
  - Section 7: Recent Whale Trades & Smart Money Executions

Target Sheet: '12_Hyperdash' in Data/DataBase_Trading.xlsx
Position: Immediately following '11_Technical'.
"""

from __future__ import annotations

try:
    from logger_config import stamp_sheet_completion_ist, get_current_timestamps
except ImportError:
    stamp_sheet_completion_ist = None
    get_current_timestamps = None


import argparse
import datetime
import json
import logging
import math
import pathlib
import sys
import time
from typing import Any, Dict, List, Optional, Tuple

try:
    import openpyxl
    from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
    from openpyxl.utils import get_column_letter
except ImportError:
    openpyxl = None

MODULES_DIR = pathlib.Path(__file__).resolve().parent
ROOT_DIR = MODULES_DIR.parents[1]
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

from Terminal.Api_Client import HyperdashClient
from Terminal.Asset_Universe import COMPLETE_UNIVERSE, canonical_asset
from Terminal.Data_Factory.hyperdash_flow_feed import get_hyperdash_flow_intelligence

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] [12_Hyperdash] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
log = logging.getLogger("12_Hyperdash")

DEFAULT_EXCEL_PATH = ROOT_DIR / "Data" / "DataBase_Trading.xlsx"
TARGET_SHEET_NAME = "12_Hyperdash"
TARGET_INDEX = 20

# -------------------------------------------------------------------------
# Table Schemas
# -------------------------------------------------------------------------
SECTION_2_COLS = [
    ("sr_no", "Sr. No.", 8, "center"),
    ("asset", "Asset", 12, "center"),
    ("liquidations_usd", "Liquidations (USD)", 20, "right"),
    ("imminent_liqs_usd", "Imminent Hazards (USD)", 22, "right"),
    ("twap_notional_usd", "TWAP Notional (USD)", 22, "right"),
    ("whale_trades_usd", "Whale Trades (USD)", 20, "right"),
    ("oi_surges_count", "OI Surges", 12, "right"),
    ("dominant_bias", "Dominant Flow Bias", 30, "center"),
]

SECTION_3_COLS = [
    ("sr_no", "Sr. No.", 8, "center"),
    ("coin", "Asset", 10, "center"),
    ("side", "Side", 10, "center"),
    ("price", "Limit Price ($)", 16, "right"),
    ("size", "Size (Tokens)", 16, "right"),
    ("notional_usd", "Notional (USD)", 18, "right"),
    ("address", "Ethereum Wallet Address", 44, "left"),
    ("source", "Telemetry Source", 36, "center"),
]

SECTION_4_COLS = [
    ("sr_no", "Sr. No.", 8, "center"),
    ("coin", "Asset", 10, "center"),
    ("side", "Risk Side", 12, "center"),
    ("price", "Liq Price ($)", 16, "right"),
    ("size", "Size (Tokens)", 16, "right"),
    ("notional_usd", "Estimated Notional ($)", 22, "right"),
    ("address", "Ethereum Wallet Address", 44, "left"),
]

SECTION_5_COLS = [
    ("sr_no", "Sr. No.", 8, "center"),
    ("coin", "Asset", 10, "center"),
    ("side", "Stop Type", 14, "center"),
    ("price", "Trigger Price ($)", 16, "right"),
    ("size", "Size (Tokens)", 16, "right"),
    ("notional_usd", "Estimated Notional ($)", 22, "right"),
    ("address", "Ethereum Wallet Address", 44, "left"),
]

SECTION_6_COLS = [
    ("sr_no", "Sr. No.", 8, "center"),
    ("date_label", "Date / Time", 18, "center"),
    ("coin", "Asset", 10, "center"),
    ("side", "Liquidation Side", 18, "center"),
    ("notional_usd", "Notional (USD)", 18, "right"),
    ("price", "Execution Price ($)", 18, "right"),
    ("market_impact", "Forced Market Impact", 22, "center"),
    ("wallet_address", "Ethereum Wallet Address", 44, "left"),
]

SECTION_7_COLS = [
    ("sr_no", "Sr. No.", 8, "center"),
    ("date_label", "Date / Time", 18, "center"),
    ("coin", "Asset", 10, "center"),
    ("side", "Trade Side", 14, "center"),
    ("notional_usd", "Notional (USD)", 18, "right"),
    ("price", "Execution Price ($)", 18, "right"),
    ("wallet_address", "Ethereum Wallet Address", 44, "left"),
]


def harvest_hyperdash_data() -> Dict[str, Any]:
    """Harvests flow feed intelligence and GraphQL L3/Liqs/Stops data."""
    t0 = time.time()
    log.info("Harvesting Hyperdash on-chain flow intelligence...")
    flow_intel = get_hyperdash_flow_intelligence()
    log.info(f"Gathered flow intelligence across {len(flow_intel.get('universe_asset_breakdown', {}))} assets.")

    client = HyperdashClient()
    l3_orders: List[Dict[str, Any]] = []
    top_liqs: List[Dict[str, Any]] = []
    top_stops: List[Dict[str, Any]] = []

    # 1. Fetch L3 Resting Whale Orders for BTC & ETH
    for coin in ("BTC", "ETH"):
        try:
            l2 = client.fetch_l2_book(coin)
            mid = l2.get("best_bid", 0.0)
            if mid > 0:
                orders = client.fetch_l3_orders(coin, mid * 0.98, mid * 1.02)
                for o in orders[:50]:  # Top 50 whale orders per coin
                    l3_orders.append({
                        "coin": coin,
                        "side": o.get("side"),
                        "price": o.get("price"),
                        "size": o.get("size"),
                        "notional_usd": o.get("notional_usd"),
                        "address": o.get("address"),
                        "source": o.get("source", "HYPERDASH_L3_RESTING"),
                    })
        except Exception as e:
            log.warning(f"Could not harvest L3 orders for {coin}: {e}")

    # 2. Fetch Top Liquidation Whales for BTC & ETH
    for coin in ("BTC", "ETH"):
        try:
            l2 = client.fetch_l2_book(coin)
            mid = l2.get("best_bid", 0.0)
            if mid > 0:
                liq_data = client.fetch_liquidations(coin, mid * 0.90, mid * 1.10)
                for w in liq_data.get("top_long_whales", []):
                    top_liqs.append({
                        "coin": coin,
                        "side": "LONG_AT_RISK",
                        "price": float(w.get("price", 0.0)),
                        "size": float(w.get("size", 0.0)),
                        "notional_usd": float(w.get("price", 0.0)) * float(w.get("size", 0.0)),
                        "address": w.get("address", ""),
                    })
                for w in liq_data.get("top_short_whales", []):
                    top_liqs.append({
                        "coin": coin,
                        "side": "SHORT_AT_RISK",
                        "price": float(w.get("price", 0.0)),
                        "size": float(w.get("size", 0.0)),
                        "notional_usd": float(w.get("price", 0.0)) * float(w.get("size", 0.0)),
                        "address": w.get("address", ""),
                    })
        except Exception as e:
            log.warning(f"Could not harvest liquidation levels for {coin}: {e}")

    # 3. Fetch Top Stop-Loss Whales for BTC & ETH
    for coin in ("BTC", "ETH"):
        try:
            l2 = client.fetch_l2_book(coin)
            mid = l2.get("best_bid", 0.0)
            if mid > 0:
                stop_data = client.fetch_stops(coin, mid * 0.90, mid * 1.10)
                for w in stop_data.get("top_buy_whales", []):
                    top_stops.append({
                        "coin": coin,
                        "side": "BUY_STOP",
                        "price": float(w.get("price", 0.0)),
                        "size": float(w.get("size", 0.0)),
                        "notional_usd": float(w.get("price", 0.0)) * float(w.get("size", 0.0)),
                        "address": w.get("address", ""),
                    })
                for w in stop_data.get("top_sell_whales", []):
                    top_stops.append({
                        "coin": coin,
                        "side": "SELL_STOP",
                        "price": float(w.get("price", 0.0)),
                        "size": float(w.get("size", 0.0)),
                        "notional_usd": float(w.get("price", 0.0)) * float(w.get("size", 0.0)),
                        "address": w.get("address", ""),
                    })
        except Exception as e:
            log.warning(f"Could not harvest stop levels for {coin}: {e}")

    # Sort orders and liqs by notional descending
    l3_orders.sort(key=lambda x: x.get("notional_usd", 0.0), reverse=True)
    top_liqs.sort(key=lambda x: x.get("notional_usd", 0.0), reverse=True)
    top_stops.sort(key=lambda x: x.get("notional_usd", 0.0), reverse=True)

    log.info(f"Hyperdash harvest completed in {time.time() - t0:.2f}s: "
             f"{len(l3_orders)} L3 orders, {len(top_liqs)} liqs, {len(top_stops)} stops.")

    return {
        "flow_intel": flow_intel,
        "l3_orders": l3_orders,
        "top_liqs": top_liqs,
        "top_stops": top_stops,
    }


def dump_hyperdash_to_excel(
    data: Dict[str, Any],
    excel_path: pathlib.Path = DEFAULT_EXCEL_PATH,
    sheet_name: str = TARGET_SHEET_NAME,
    target_index: int = TARGET_INDEX,
) -> bool:
    """Dumps all 7 sections of Hyperdash intelligence into Excel with institutional formatting."""
    if not openpyxl:
        log.error("openpyxl is not installed.")
        return False

    if not excel_path.exists():
        log.error(f"Excel workbook not found at: {excel_path}")
        return False

    wb = openpyxl.load_workbook(excel_path)
    if sheet_name in wb.sheetnames:
        wb.remove(wb[sheet_name])

    ws = wb.create_sheet(title=sheet_name, index=target_index)

    # Styling Palette
    font_banner = Font(name="Segoe UI", size=11, bold=True, color="FFFFFF")
    fill_banner = PatternFill(start_color="0F172A", end_color="0F172A", fill_type="solid")

    font_sub_banner = Font(name="Segoe UI", size=10, bold=True, color="FFFFFF")
    fill_sub_banner = PatternFill(start_color="1E293B", end_color="1E293B", fill_type="solid")

    hdr_font = Font(name="Segoe UI", size=9, bold=True, color="FFFFFF")
    hdr_fill = PatternFill(start_color="334155", end_color="334155", fill_type="solid")

    base_font = Font(name="Segoe UI", size=9, color="0F172A")
    bold_font = Font(name="Segoe UI", size=9, bold=True, color="0F172A")
    green_font = Font(name="Segoe UI", size=9, bold=True, color="00A86B")
    red_font = Font(name="Segoe UI", size=9, bold=True, color="E53935")

    fill_zebra = PatternFill(start_color="F8FAFC", end_color="F8FAFC", fill_type="solid")
    fill_white = PatternFill(start_color="FFFFFF", end_color="FFFFFF", fill_type="solid")

    thin_border_side = Side(border_style="thin", color="E2E8F0")
    row_border = Border(
        left=thin_border_side, right=thin_border_side, top=thin_border_side, bottom=thin_border_side
    )

    now_utc = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
    current_row = 1

    # =========================================================================
    # SECTION 1: Macro Hyperdash Intelligence Summary & Telemetry
    # =========================================================================
    summary = data.get("flow_intel", {}).get("summary", {})
    sec1_metrics = [
        ("Total Alerts Tracked", summary.get("total_alerts_tracked", 0), "#,##0"),
        ("Total Liquidations Volume", summary.get("total_liquidations_volume_usd", 0.0), "$#,##0.00"),
        ("Long Liquidations Volume", summary.get("long_liquidations_volume_usd", 0.0), "$#,##0.00"),
        ("Short Liquidations Volume", summary.get("short_liquidations_volume_usd", 0.0), "$#,##0.00"),
        ("Long to Short Liq Ratio", summary.get("long_to_short_liq_ratio", 0.0), "0.00"),
        ("Imminent Liquidation Alerts", summary.get("imminent_liquidation_alerts_count", 0), "#,##0"),
        ("Active TWAP Orders Tracked", summary.get("active_twap_orders_count", 0), "#,##0"),
        ("Total TWAP Notional", summary.get("total_twap_notional_usd", 0.0), "$#,##0.00"),
        ("Whale Trades Tracked", summary.get("whale_trades_count", 0), "#,##0"),
        ("Open Interest Surges Tracked", summary.get("oi_surges_count", 0), "#,##0"),
        ("Volume Surges Tracked", summary.get("volume_surges_count", 0), "#,##0"),
        ("Collateral Inflows (USDC)", summary.get("collateral_inflows_usd", 0.0), "$#,##0.00"),
        ("Collateral Outflows (USDC)", summary.get("collateral_outflows_usd", 0.0), "$#,##0.00"),
        ("Net Collateral Expansion", summary.get("net_collateral_expansion_usd", 0.0), "$#,##0.00"),
        ("Macro Orderflow Tilt", summary.get("macro_orderflow_tilt", "BALANCED"), "@"),
    ]

    ws.merge_cells("A1:D1")
    s1_banner = ws["A1"]
    if get_current_timestamps:
        _ist_ts, _utc_ts = get_current_timestamps()
        s1_banner.value = f"12_Hyperdash | LAST UPDATED: {_ist_ts} ({_utc_ts}) | ROWS: {current_row} | STATUS: LIVE"
        s1_banner.font = Font(name="Segoe UI", size=10, bold=True, color="155724")
        s1_banner.fill = PatternFill(start_color="D4EDDA", end_color="D4EDDA", fill_type="solid")
    else:
        s1_banner.value = f"SECTION 1: HYPERDASH MACRO ON-CHAIN FLOW INTELLIGENCE SUMMARY [as_of {now_utc}]"
    s1_banner.font = font_banner
    s1_banner.fill = fill_banner
    s1_banner.alignment = Alignment(horizontal="center", vertical="center")
    ws.row_dimensions[1].height = 28

    # Section 1 Headers
    ws.row_dimensions[2].height = 24
    s1_hdrs = [("A", "Metric Identifier", 32), ("B", "Metric Value", 24), ("C", "Description / Classification", 36)]
    for col_l, title, width in s1_hdrs:
        c = ws[f"{col_l}2"]
        c.value = title
        c.font = hdr_font
        c.fill = hdr_fill
        c.alignment = Alignment(horizontal="center", vertical="center")
        c.border = row_border
        ws.column_dimensions[col_l].width = width

    current_row = 3
    for label, val, num_fmt in sec1_metrics:
        ws.row_dimensions[current_row].height = 20
        c1 = ws.cell(row=current_row, column=1, value=label)
        c2 = ws.cell(row=current_row, column=2, value=val)
        c3 = ws.cell(row=current_row, column=3, value="Macro Telemetry Alert")

        c1.font = bold_font
        c1.alignment = Alignment(horizontal="left", vertical="center")
        c1.border = row_border

        c2.font = bold_font
        c2.number_format = num_fmt
        c2.alignment = Alignment(horizontal="right" if num_fmt != "@" else "center", vertical="center")
        c2.border = row_border

        if "BEARISH" in str(val):
            c2.font = red_font
        elif "BULLISH" in str(val):
            c2.font = green_font

        c3.font = base_font
        c3.alignment = Alignment(horizontal="left", vertical="center")
        c3.border = row_border

        r_fill = fill_zebra if current_row % 2 == 0 else fill_white
        c1.fill = r_fill
        c2.fill = r_fill
        c3.fill = r_fill
        current_row += 1

    current_row += 1  # Buffer

    # =========================================================================
    # Helper to render tabular sections
    # =========================================================================
    def render_table_section(
        banner_title: str,
        columns_def: List[Tuple[str, str, int, str]],
        records: List[Dict[str, Any]],
        start_row: int,
        max_rows: Optional[int] = None,
    ) -> int:
        last_letter = get_column_letter(len(columns_def))
        ws.merge_cells(f"A{start_row}:{last_letter}{start_row}")
        sb = ws[f"A{start_row}"]
        sb.value = banner_title
        sb.font = font_sub_banner
        sb.fill = fill_sub_banner
        sb.alignment = Alignment(horizontal="center", vertical="center")
        ws.row_dimensions[start_row].height = 26
        row_idx = start_row + 1

        # Header Row
        ws.row_dimensions[row_idx].height = 24
        for col_i, (k, title, width, align) in enumerate(columns_def, start=1):
            cell = ws.cell(row=row_idx, column=col_i, value=title)
            cell.font = hdr_font
            cell.fill = hdr_fill
            cell.alignment = Alignment(horizontal=align, vertical="center")
            cell.border = row_border
            col_letter = get_column_letter(col_i)
            if ws.column_dimensions[col_letter].width is None or ws.column_dimensions[col_letter].width < width:
                ws.column_dimensions[col_letter].width = width
        row_idx += 1

        # Data Rows
        sliced_records = records[:max_rows] if max_rows else records
        for i, rec in enumerate(sliced_records, start=1):
            ws.row_dimensions[row_idx].height = 19
            r_fill = fill_zebra if row_idx % 2 == 0 else fill_white

            for col_i, (k, _, _, align) in enumerate(columns_def, start=1):
                cell = ws.cell(row=row_idx, column=col_i)
                val = rec.get(k)
                if k == "sr_no":
                    val = i

                if k in ("liquidations_usd", "imminent_liqs_usd", "twap_notional_usd", "whale_trades_usd", "notional_usd"):
                    if val is not None and not (isinstance(val, float) and (math.isnan(val) or math.isinf(val))):
                        cell.value = float(val)
                        cell.number_format = "$#,##0.00"
                    else:
                        cell.value = 0.0
                        cell.number_format = "$#,##0.00"
                elif k in ("price", "limit_price", "liq_price", "trigger_price"):
                    if val is not None and not (isinstance(val, float) and (math.isnan(val) or math.isinf(val))):
                        cell.value = float(val)
                        cell.number_format = "$#,##0.00" if abs(float(val)) >= 1 else "$#,##0.0000"
                    else:
                        cell.value = ""
                elif k in ("size", "oi_surges_count", "sr_no"):
                    if val is not None and not (isinstance(val, float) and (math.isnan(val) or math.isinf(val))):
                        cell.value = float(val) if k == "size" else int(val)
                        cell.number_format = "#,##0.00" if k == "size" else "#,##0"
                    else:
                        cell.value = ""
                else:
                    cell.value = str(val) if val is not None else ""

                cell.alignment = Alignment(horizontal=align, vertical="center")
                cell.border = row_border
                cell.fill = r_fill

                # Conditional Color
                sval = str(val).upper()
                if "BUY" in sval or "LONG" in sval:
                    cell.font = green_font
                elif "SELL" in sval or "SHORT" in sval:
                    cell.font = red_font
                elif "VOLATILITY" in sval or "HAZARD" in sval:
                    cell.font = red_font
                elif "ACCUMULATION" in sval:
                    cell.font = green_font
                else:
                    cell.font = base_font

            row_idx += 1

        return row_idx + 1  # Add blank buffer row

    # =========================================================================
    # SECTION 2: Universe Per-Asset On-Chain Flow Attribution Matrix
    # =========================================================================
    breakdown = data.get("flow_intel", {}).get("universe_asset_breakdown", {})
    sec2_rows = []
    for asset, info in sorted(breakdown.items(), key=lambda x: x[1].get("liquidations_usd", 0.0), reverse=True):
        sec2_rows.append({
            "asset": asset,
            "liquidations_usd": info.get("liquidations_usd", 0.0),
            "imminent_liqs_usd": info.get("imminent_liqs_usd", 0.0),
            "twap_notional_usd": info.get("twap_notional_usd", 0.0),
            "whale_trades_usd": info.get("whale_trades_usd", 0.0),
            "oi_surges_count": info.get("oi_surges_count", 0),
            "dominant_bias": info.get("dominant_bias", "BALANCED_TWO_SIDED_FLOW"),
        })

    current_row = render_table_section(
        f"SECTION 2: UNIVERSE PER-ASSET ON-CHAIN FLOW ATTRIBUTION MATRIX ({len(sec2_rows)} ASSETS)",
        SECTION_2_COLS,
        sec2_rows,
        current_row,
    )

    # =========================================================================
    # SECTION 3: Level 3 Institutional Resting Whale Orders (Mapped to Ethereum Addresses)
    # =========================================================================
    l3_orders = data.get("l3_orders", [])
    current_row = render_table_section(
        f"SECTION 3: LEVEL 3 INSTITUTIONAL RESTING WHALE ORDERS (TOP {min(len(l3_orders), 80)} ORDERS MAPPED TO ETH WALLETS)",
        SECTION_3_COLS,
        l3_orders,
        current_row,
        max_rows=80,
    )

    # =========================================================================
    # SECTION 4: Top Liquidation Clusters & Liquidation Whale Addresses
    # =========================================================================
    top_liqs = data.get("top_liqs", [])
    current_row = render_table_section(
        f"SECTION 4: TOP ON-CHAIN LIQUIDATION CLUSTERS & WHALE ADDRESSES (BTC & ETH)",
        SECTION_4_COLS,
        top_liqs,
        current_row,
        max_rows=40,
    )

    # =========================================================================
    # SECTION 5: Top Stop-Loss Clusters & Whale Stop Addresses
    # =========================================================================
    top_stops = data.get("top_stops", [])
    current_row = render_table_section(
        f"SECTION 5: TOP ON-CHAIN STOP-LOSS CLUSTERS & WHALE STOP ADDRESSES (BTC & ETH)",
        SECTION_5_COLS,
        top_stops,
        current_row,
        max_rows=40,
    )

    # =========================================================================
    # SECTION 6: Recent Confirmed Forced Liquidations Feed (Hyperliquid L1)
    # =========================================================================
    rec_liqs = data.get("flow_intel", {}).get("recent_confirmed_liquidations", [])
    s6_rows = []
    for r in reversed(rec_liqs[-100:]):
        s6_rows.append({
            "date_label": f"{r.get('date_heading', '')} {r.get('time_label', '')}".strip(),
            "coin": r.get("coin"),
            "side": r.get("side"),
            "notional_usd": r.get("notional_usd"),
            "price": r.get("price"),
            "market_impact": r.get("market_impact"),
            "wallet_address": r.get("wallet_address"),
        })

    current_row = render_table_section(
        f"SECTION 6: RECENT CONFIRMED ON-CHAIN FORCED LIQUIDATIONS FEED (LAST {len(s6_rows)} LIQUIDATIONS)",
        SECTION_6_COLS,
        s6_rows,
        current_row,
        max_rows=100,
    )

    # =========================================================================
    # SECTION 7: Recent Whale Trades & Smart Money Executions
    # =========================================================================
    rec_whales = data.get("flow_intel", {}).get("whale_trades", [])
    s7_rows = []
    for r in reversed(rec_whales[-100:]):
        s7_rows.append({
            "date_label": f"{r.get('date_heading', '')} {r.get('time_label', '')}".strip(),
            "coin": r.get("coin"),
            "side": r.get("side"),
            "notional_usd": r.get("notional_usd"),
            "price": r.get("price"),
            "wallet_address": r.get("wallet_address"),
        })

    current_row = render_table_section(
        f"SECTION 7: RECENT WHALE TRADES & SMART MONEY EXECUTIONS (LAST {len(s7_rows)} EXECUTIONS)",
        SECTION_7_COLS,
        s7_rows,
        current_row,
        max_rows=100,
    )

    import os, time
    temp_excel = excel_path.with_name(f"{excel_path.stem}_{os.getpid()}_{int(time.time()*1000)}.tmp.xlsx")
    wb.save(temp_excel)
    wb.close()
    import time, zipfile
    _is_valid = False
    with zipfile.ZipFile(temp_excel, "r") as _z:
        _is_valid = (_z.testzip() is None)
    if _is_valid:
        for _att in range(30):
            try:
                temp_excel.replace(excel_path)
                break
            except PermissionError:
                if _att == 29: raise
                time.sleep(1.0)
    else:
        if temp_excel.exists(): temp_excel.unlink()
        raise ValueError("Corrupt zip produced during export")
    log.info(f"Successfully dumped Hyperdash intelligence to '{sheet_name}' in {excel_path} (Index: {target_index}).")
    return True


def main():
    parser = argparse.ArgumentParser(description="Hyperdash On-Chain Intelligence Module 20")
    parser.add_argument("--excel", default=str(DEFAULT_EXCEL_PATH), help="Path to DataBase_Trading.xlsx")
    parser.add_argument("--sheet", default=TARGET_SHEET_NAME, help="Target sheet name")
    parser.add_argument("--index", type=int, default=TARGET_INDEX, help="Worksheet index position")
    args = parser.parse_args()

    t_start = time.time()
    log.info(f"Starting Hyperdash On-Chain Intelligence module for sheet '{args.sheet}' (Index: {args.index})...")

    harvest_data = harvest_hyperdash_data()
    success = dump_hyperdash_to_excel(
        harvest_data,
        excel_path=pathlib.Path(args.excel),
        sheet_name=args.sheet,
        target_index=args.index,
    )

    if success:
        log.info(f"Hyperdash module completed successfully in {time.time() - t_start:.2f}s.")
        sys.exit(0)
    else:
        log.error("Hyperdash module failed.")
        sys.exit(1)


if __name__ == "__main__":
    main()
