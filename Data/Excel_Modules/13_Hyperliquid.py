#!/usr/bin/env python3
"""
Data/Excel_Modules/13_Hyperliquid.py
====================================
Dedicated Excel Module 21: Hyperliquid L1 Native Exchange & Microstructure Engine.
Extracts comprehensive real-time market data directly from Hyperliquid's official
L1 API (https://api.hyperliquid.xyz/info):
  - Section 1: All-Asset Perpetual & HIP-3 Builder Screener (Global, XYZ, FLX DEXes - 290+ Markets)
  - Section 2: Predicted Funding Rates Comparison (Hyperliquid vs Binance vs Bybit Arbitrage Matrix)
  - Section 3: Multi-Asset Level 2 Orderbook Depth & Imbalance Matrix (Top 15 Perpetuals)
  - Section 4: Real-Time Tick Trades Tape with Aggressor Side & Ethereum Wallet Attribution
  - Section 5: Hyperliquid Spot Market Ecosystem Overview (Top Native Spot Tokens)

Target Sheet: '13_Hyperliquid' in Data/DataBase_Trading.xlsx
Position: Immediately following '12_Hyperdash'.
"""

from __future__ import annotations

import argparse
import datetime
import json
import logging
import math
import pathlib
import sys
import time
import urllib.request
import urllib.error
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

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] [13_Hyperliquid] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
log = logging.getLogger("13_Hyperliquid")

DEFAULT_EXCEL_PATH = ROOT_DIR / "Data" / "DataBase_Trading.xlsx"
TARGET_SHEET_NAME = "13_Hyperliquid"
TARGET_INDEX = 21

HL_INFO_URL = "https://api.hyperliquid.xyz/info"
DEFAULT_HEADERS = {
    "Content-Type": "application/json",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
}

TOP_WATCHLIST = [
    "BTC", "ETH", "SOL", "BNB", "XRP", "DOGE", "ADA", "SUI",
    "LINK", "AVAX", "NEAR", "DOT", "LTC", "BCH", "APT"
]

# -------------------------------------------------------------------------
# Table Schemas
# -------------------------------------------------------------------------
SECTION_1_COLS = [
    ("sr_no", "Sr. No.", 8, "center"),
    ("coin", "Asset", 10, "center"),
    ("signal_market", "Market Identifier", 16, "center"),
    ("dex", "Origin DEX", 12, "center"),
    ("mark_px", "Mark Price ($)", 16, "right"),
    ("change_24h", "24h Chg (%)", 14, "right"),
    ("volume_24h", "24h Volume (USD)", 20, "right"),
    ("open_interest", "Open Interest (Tokens)", 22, "right"),
    ("open_interest_usd", "Open Interest (USD)", 22, "right"),
    ("funding_rate", "1h Funding Rate", 16, "right"),
    ("funding_annualized", "Funding APR (%)", 16, "right"),
    ("max_leverage", "Max Lev", 10, "center"),
    ("sz_decimals", "Decimals", 10, "center"),
]

SECTION_2_COLS = [
    ("sr_no", "Sr. No.", 8, "center"),
    ("coin", "Asset", 10, "center"),
    ("hl_funding", "Hyperliquid 1h Rate", 18, "right"),
    ("hl_apr", "Hyperliquid APR (%)", 18, "right"),
    ("bin_funding", "Binance Pred. Rate", 18, "right"),
    ("bybit_funding", "Bybit Pred. Rate", 18, "right"),
    ("arb_spread_bps", "Funding Spread (bps)", 18, "right"),
    ("next_time_utc", "Next Funding Time (UTC)", 22, "center"),
]

SECTION_3_COLS = [
    ("sr_no", "Sr. No.", 8, "center"),
    ("coin", "Asset", 10, "center"),
    ("best_bid", "Best Bid ($)", 16, "right"),
    ("best_ask", "Best Ask ($)", 16, "right"),
    ("spread", "Spread ($)", 14, "right"),
    ("spread_bps", "Spread (bps)", 14, "right"),
    ("bid_vol_usd", "Top 20 Bid Vol ($)", 20, "right"),
    ("ask_vol_usd", "Top 20 Ask Vol ($)", 20, "right"),
    ("bid_pct", "Bid Depth (%)", 14, "right"),
    ("ask_pct", "Ask Depth (%)", 14, "right"),
    ("imbalance_state", "Orderbook Microstructure Bias", 28, "center"),
]

SECTION_4_COLS = [
    ("sr_no", "Sr. No.", 8, "center"),
    ("time_utc", "Trade Time (UTC)", 20, "center"),
    ("coin", "Asset", 10, "center"),
    ("side", "Aggressor Side", 14, "center"),
    ("price", "Execution Price ($)", 18, "right"),
    ("size", "Size (Tokens)", 16, "right"),
    ("notional_usd", "Notional (USD)", 18, "right"),
    ("trade_id", "Transaction ID (TID)", 20, "center"),
    ("user_1", "Participant Wallet 1", 44, "left"),
    ("user_2", "Participant Wallet 2", 44, "left"),
]

SECTION_5_COLS = [
    ("sr_no", "Sr. No.", 8, "center"),
    ("pair", "Spot Pair", 16, "center"),
    ("mark_px", "Mark Price ($)", 16, "right"),
    ("change_24h", "24h Chg (%)", 14, "right"),
    ("volume_24h", "24h Volume (USD)", 20, "right"),
    ("circulating_supply", "Circulating Supply", 22, "right"),
    ("fdv_usd", "Fully Diluted Val ($)", 22, "right"),
]


def post_hl_api(payload: dict, timeout: int = 8) -> Any:
    """Helper to query Hyperliquid L1 info API."""
    data_bytes = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(HL_INFO_URL, data=data_bytes, headers=DEFAULT_HEADERS)
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return json.loads(resp.read().decode("utf-8"))


def harvest_hyperliquid_data() -> Dict[str, Any]:
    """Harvests all 5 sections of native Hyperliquid L1 data."""
    t0 = time.time()
    log.info("Harvesting Hyperliquid L1 native market data...")
    client = HyperdashClient()

    # 1. Complete Perpetual Screener (All Markets)
    all_perps = client.fetch_all_assets()
    log.info(f"Fetched {len(all_perps)} perpetual markets from Hyperliquid.")

    # 2. Predicted Funding Rates
    predicted_fundings_raw = []
    try:
        predicted_fundings_raw = post_hl_api({"type": "predictedFundings"})
        log.info(f"Fetched predicted fundings for {len(predicted_fundings_raw)} markets.")
    except Exception as e:
        log.warning(f"Could not fetch predictedFundings: {e}")

    parsed_funding_cmp = []
    for item in predicted_fundings_raw:
        if not isinstance(item, list) or len(item) < 2:
            continue
        coin = item[0]
        rates_map = {}
        next_ts = None
        for ex_info in item[1]:
            if isinstance(ex_info, list) and len(ex_info) == 2:
                ex_name = ex_info[0]
                details = ex_info[1]
                if isinstance(details, dict):
                    rates_map[ex_name] = float(details.get("fundingRate", 0.0))
                    if not next_ts and details.get("nextFundingTime"):
                        next_ts = details.get("nextFundingTime")

        hl_rate = rates_map.get("HlPerp")
        bin_rate = rates_map.get("BinPerp")
        bybit_rate = rates_map.get("BybitPerp")

        if hl_rate is not None:
            hl_apr = hl_rate * 24 * 365 * 100.0
            # Arb spread in bps against Binance or Bybit
            ref_rate = bin_rate if bin_rate is not None else bybit_rate
            arb_bps = (hl_rate - ref_rate) * 10000.0 if ref_rate is not None else 0.0
            next_dt_str = datetime.datetime.fromtimestamp(next_ts / 1000.0, tz=datetime.timezone.utc).strftime("%Y-%m-%d %H:%M") if next_ts else "N/A"

            parsed_funding_cmp.append({
                "coin": coin,
                "hl_funding": hl_rate,
                "hl_apr": hl_apr,
                "bin_funding": bin_rate,
                "bybit_funding": bybit_rate,
                "arb_spread_bps": arb_bps,
                "next_time_utc": next_dt_str,
            })

    # Sort funding comparison by absolute arb spread
    parsed_funding_cmp.sort(key=lambda x: abs(x.get("arb_spread_bps", 0.0)), reverse=True)

    # 3. Multi-Asset L2 Orderbook Depth & Imbalance Matrix (Top 15 assets)
    l2_depth_matrix = []
    for coin in TOP_WATCHLIST:
        try:
            l2 = client.fetch_l2_book(coin)
            b_vol = l2.get("bid_volume_usd", 0.0)
            a_vol = l2.get("ask_volume_usd", 0.0)
            b_pct = l2.get("bid_pct", 50.0)

            if b_pct >= 60.0:
                imb = "HEAVY BID ACCUMULATION"
            elif b_pct <= 40.0:
                imb = "HEAVY ASK PRESSURE"
            else:
                imb = "BALANCED BOOK"

            l2_depth_matrix.append({
                "coin": coin,
                "best_bid": l2.get("best_bid"),
                "best_ask": l2.get("best_ask"),
                "spread": l2.get("spread"),
                "spread_bps": l2.get("spread_bps"),
                "bid_vol_usd": b_vol,
                "ask_vol_usd": a_vol,
                "bid_pct": b_pct,
                "ask_pct": 100.0 - b_pct,
                "imbalance_state": imb,
            })
        except Exception as e:
            log.warning(f"Could not fetch L2 book for {coin}: {e}")

    # 4. Recent Tick Trades Tape (BTC, ETH, SOL, HYPE)
    recent_tape = []
    for coin in ("BTC", "ETH", "SOL", "HYPE"):
        try:
            trades = post_hl_api({"type": "recentTrades", "coin": coin})
            for t in (trades or []):
                t_side = "BUY" if t.get("side") == "B" else "SELL"
                px = float(t.get("px", 0.0))
                sz = float(t.get("sz", 0.0))
                users = t.get("users", [])
                u1 = users[0] if len(users) > 0 else ""
                u2 = users[1] if len(users) > 1 else ""
                t_time = datetime.datetime.fromtimestamp(t.get("time", 0) / 1000.0, tz=datetime.timezone.utc).strftime("%Y-%m-%d %H:%M:%S")

                recent_tape.append({
                    "time_utc": t_time,
                    "time_raw": t.get("time", 0),
                    "coin": coin,
                    "side": t_side,
                    "price": px,
                    "size": sz,
                    "notional_usd": px * sz,
                    "trade_id": str(t.get("tid", t.get("hash", ""))),
                    "user_1": u1,
                    "user_2": u2,
                })
        except Exception as e:
            log.warning(f"Could not fetch recent trades for {coin}: {e}")

    # Sort tape chronologically descending
    recent_tape.sort(key=lambda x: x.get("time_raw", 0), reverse=True)

    # 5. Spot Market Ecosystem Overview
    spot_markets = []
    try:
        spot_raw = post_hl_api({"type": "spotMetaAndAssetCtxs"})
        if spot_raw and len(spot_raw) == 2:
            meta_u = spot_raw[0].get("universe", [])
            ctxs = spot_raw[1]
            ctx_map = {c.get("coin"): c for c in ctxs}

            for pair_info in meta_u:
                pair_name = pair_info.get("name")
                c_data = ctx_map.get(pair_name, {})
                mark_px = float(c_data.get("markPx") or 0.0)
                if mark_px <= 0:
                    continue
                vlm = float(c_data.get("dayNtlVlm") or 0.0)
                prev_px = float(c_data.get("prevDayPx") or 0.0)
                chg = ((mark_px - prev_px) / prev_px * 100.0) if prev_px > 0 else 0.0
                circ_supply = float(c_data.get("circulatingSupply") or 0.0)
                fdv = circ_supply * mark_px if circ_supply > 0 else None

                spot_markets.append({
                    "pair": pair_name,
                    "mark_px": mark_px,
                    "change_24h": chg,
                    "volume_24h": vlm,
                    "circulating_supply": circ_supply,
                    "fdv_usd": fdv,
                })
            # Sort spot markets by 24h volume descending
            spot_markets.sort(key=lambda x: x.get("volume_24h", 0.0), reverse=True)
            log.info(f"Fetched {len(spot_markets)} active spot markets from Hyperliquid.")
    except Exception as e:
        log.warning(f"Could not fetch spot markets: {e}")

    log.info(f"Hyperliquid harvest completed in {time.time() - t0:.2f}s.")
    return {
        "perpetuals": all_perps,
        "funding_cmp": parsed_funding_cmp,
        "l2_depth": l2_depth_matrix,
        "trades_tape": recent_tape,
        "spot_markets": spot_markets,
    }


def dump_hyperliquid_to_excel(
    data: Dict[str, Any],
    excel_path: pathlib.Path = DEFAULT_EXCEL_PATH,
    sheet_name: str = TARGET_SHEET_NAME,
    target_index: int = TARGET_INDEX,
) -> bool:
    """Dumps all 5 sections of native Hyperliquid L1 data into Excel with institutional formatting."""
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

    def render_table_section(
        banner_title: str,
        columns_def: List[Tuple[str, str, int, str]],
        records: List[Dict[str, Any]],
        start_row: int,
        is_main_banner: bool = False,
        max_rows: Optional[int] = None,
    ) -> int:
        last_letter = get_column_letter(len(columns_def))
        ws.merge_cells(f"A{start_row}:{last_letter}{start_row}")
        sb = ws[f"A{start_row}"]
        sb.value = banner_title
        sb.font = font_banner if is_main_banner else font_sub_banner
        sb.fill = fill_banner if is_main_banner else fill_sub_banner
        sb.alignment = Alignment(horizontal="center", vertical="center")
        ws.row_dimensions[start_row].height = 28 if is_main_banner else 26
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

                # Number formats
                if k in ("volume_24h", "open_interest_usd", "notional_usd", "bid_vol_usd", "ask_vol_usd", "fdv_usd"):
                    if val is not None and not (isinstance(val, float) and (math.isnan(val) or math.isinf(val))):
                        cell.value = float(val)
                        cell.number_format = "$#,##0.00"
                    else:
                        cell.value = ""
                elif k in ("mark_px", "price", "best_bid", "best_ask", "spread"):
                    if val is not None and not (isinstance(val, float) and (math.isnan(val) or math.isinf(val))):
                        cell.value = float(val)
                        cell.number_format = "$#,##0.00" if abs(float(val)) >= 1 else "$#,##0.0000"
                    else:
                        cell.value = ""
                elif k in ("change_24h", "funding_annualized", "hl_apr", "bid_pct", "ask_pct"):
                    if val is not None and not (isinstance(val, float) and (math.isnan(val) or math.isinf(val))):
                        cell.value = float(val) / 100.0
                        cell.number_format = "+0.00%;-0.00%;0.00%"
                    else:
                        cell.value = ""
                elif k in ("funding_rate", "hl_funding", "bin_funding", "bybit_funding"):
                    if val is not None and not (isinstance(val, float) and (math.isnan(val) or math.isinf(val))):
                        cell.value = float(val)
                        cell.number_format = "+0.0000%;-0.0000%;0.0000%"
                    else:
                        cell.value = ""
                elif k in ("spread_bps", "arb_spread_bps"):
                    if val is not None and not (isinstance(val, float) and (math.isnan(val) or math.isinf(val))):
                        cell.value = float(val)
                        cell.number_format = "+0.00;-0.00;0.00"
                    else:
                        cell.value = ""
                elif k in ("open_interest", "size", "circulating_supply"):
                    if val is not None and not (isinstance(val, float) and (math.isnan(val) or math.isinf(val))):
                        cell.value = float(val)
                        cell.number_format = "#,##0.00"
                    else:
                        cell.value = ""
                elif k in ("max_leverage", "sz_decimals", "sr_no"):
                    if val is not None:
                        cell.value = int(val)
                        cell.number_format = "#,##0"
                    else:
                        cell.value = ""
                else:
                    cell.value = str(val) if val is not None else ""

                cell.alignment = Alignment(horizontal=align, vertical="center")
                cell.border = row_border
                cell.fill = r_fill

                # Conditional Color
                sval = str(val).upper()
                if "BUY" in sval or "ACCUMULATION" in sval:
                    cell.font = green_font
                elif "SELL" in sval or "PRESSURE" in sval:
                    cell.font = red_font
                elif k in ("change_24h", "funding_annualized", "hl_apr", "arb_spread_bps"):
                    if isinstance(val, (int, float)):
                        cell.font = green_font if val > 0 else (red_font if val < 0 else base_font)
                    else:
                        cell.font = base_font
                else:
                    cell.font = base_font

            row_idx += 1

        return row_idx + 1  # Add blank buffer row

    # =========================================================================
    # SECTION 1: All-Asset Perpetual & HIP-3 Builder Screener (Global, XYZ, FLX)
    # =========================================================================
    perps = data.get("perpetuals", [])
    sec1_rows = []
    for p in perps:
        sig = p.get("signal_market", "")
        origin = "Global L1"
        if sig.startswith("xyz:"):
            origin = "xyz HIP-3"
        elif sig.startswith("flx:"):
            origin = "flx HIP-3"

        sec1_rows.append({
            "coin": p.get("coin"),
            "signal_market": sig,
            "dex": origin,
            "mark_px": p.get("mark_px"),
            "change_24h": p.get("change_24h"),
            "volume_24h": p.get("volume_24h"),
            "open_interest": p.get("open_interest"),
            "open_interest_usd": p.get("open_interest_usd"),
            "funding_rate": p.get("funding_rate"),
            "funding_annualized": p.get("funding_annualized"),
            "max_leverage": p.get("max_leverage"),
            "sz_decimals": p.get("sz_decimals"),
        })

    current_row = render_table_section(
        f"SECTION 1: HYPERLIQUID ALL-ASSET PERPETUAL & HIP-3 BUILDER SCREENER ({len(sec1_rows)} MARKETS) [as_of {now_utc}]",
        SECTION_1_COLS,
        sec1_rows,
        current_row,
        is_main_banner=True,
    )

    # =========================================================================
    # SECTION 2: Predicted Funding Rates Comparison
    # =========================================================================
    funding_cmp = data.get("funding_cmp", [])
    current_row = render_table_section(
        f"SECTION 2: PREDICTED FUNDING RATES & MULTI-EXCHANGE ARBITRAGE MATRIX (HYPERLIQUID VS BINANCE VS BYBIT - TOP {min(len(funding_cmp), 60)} MARKETS)",
        SECTION_2_COLS,
        funding_cmp,
        current_row,
        max_rows=60,
    )

    # =========================================================================
    # SECTION 3: Multi-Asset Level 2 Orderbook Depth & Imbalance Matrix
    # =========================================================================
    l2_depth = data.get("l2_depth", [])
    current_row = render_table_section(
        f"SECTION 3: LEVEL 2 ORDERBOOK DEPTH & MICROSTRUCTURE IMBALANCE MATRIX ({len(l2_depth)} TOP PERPETUALS)",
        SECTION_3_COLS,
        l2_depth,
        current_row,
    )

    # =========================================================================
    # SECTION 4: Real-Time Tick Trades Tape
    # =========================================================================
    trades_tape = data.get("trades_tape", [])
    current_row = render_table_section(
        f"SECTION 4: REAL-TIME TICK TRADES TAPE WITH ON-CHAIN WALLET ATTRIBUTION (LAST {min(len(trades_tape), 100)} TRADES)",
        SECTION_4_COLS,
        trades_tape,
        current_row,
        max_rows=100,
    )

    # =========================================================================
    # SECTION 5: Hyperliquid Spot Market Ecosystem Overview
    # =========================================================================
    spot_markets = data.get("spot_markets", [])
    current_row = render_table_section(
        f"SECTION 5: HYPERLIQUID SPOT MARKET ECOSYSTEM OVERVIEW (TOP {min(len(spot_markets), 50)} ACTIVE SPOT PAIRS)",
        SECTION_5_COLS,
        spot_markets,
        current_row,
        max_rows=50,
    )

    temp_excel = excel_path.with_suffix(".tmp.xlsx")
    wb.save(temp_excel)
    wb.close()
    import zipfile
    with zipfile.ZipFile(temp_excel, "r") as _z:
        if _z.testzip() is None:
            temp_excel.replace(excel_path)
        else:
            if temp_excel.exists(): temp_excel.unlink()
            raise ValueError("Corrupt zip produced during export")
    log.info(f"Successfully dumped Hyperliquid data to '{sheet_name}' in {excel_path} (Index: {target_index}).")
    return True


def main():
    parser = argparse.ArgumentParser(description="Hyperliquid L1 Native Exchange Module 21")
    parser.add_argument("--excel", default=str(DEFAULT_EXCEL_PATH), help="Path to DataBase_Trading.xlsx")
    parser.add_argument("--sheet", default=TARGET_SHEET_NAME, help="Target sheet name")
    parser.add_argument("--index", type=int, default=TARGET_INDEX, help="Worksheet index position")
    args = parser.parse_args()

    t_start = time.time()
    log.info(f"Starting Hyperliquid L1 Native Exchange module for sheet '{args.sheet}' (Index: {args.index})...")

    harvest_data = harvest_hyperliquid_data()
    success = dump_hyperliquid_to_excel(
        harvest_data,
        excel_path=pathlib.Path(args.excel),
        sheet_name=args.sheet,
        target_index=args.index,
    )

    if success:
        log.info(f"Hyperliquid module completed successfully in {time.time() - t_start:.2f}s.")
        sys.exit(0)
    else:
        log.error("Hyperliquid module failed.")
        sys.exit(1)


if __name__ == "__main__":
    main()
