#!/usr/bin/env python3
"""
Data/Excel_Modules/21_Tradfye_Orderflow.py
=========================================
Tradfye Multi-Timeframe Orderflow, Footprint POC, Delta & Options Gamma Module.
Ingests continuous 2-day multi-timeframe candle orderflow data for ALL 18 assets 
in our quantitative trading universe directly from Binance Futures & Deribit.

Key Capabilities:
1. Full 18-Asset Universe: BTC, ETH, SOL, BNB, XRP, DOGE, ADA, TRX, LINK, AVAX, SUI, NEAR, DOT, LTC, BCH, APT, OP, ARB.
2. Multi-Timeframe Continuous 2-Day Coverage:
   - 15m: 192 candles (exactly 48h / 2 days continuous master trading horizon)
   - 1h:  48 candles  (exactly 48h / 2 days continuous macro structure)
   - 5m:  144 candles (12h continuous high-precision execution & micro orderflow)
   Total: 6,912 continuous orderflow candles.
3. Orderflow Footprint Metrics per Candle:
   - OHLC, Total Vol ($), Taker Buy Vol ($), Taker Sell Vol ($)
   - Net Delta ($), Net Delta (%), Cumulative Volume Delta (CVD $)
   - Candle VWAP ($), Trades Count, Avg Trade Size ($), Estimated POC ($)
   - Orderflow Regime (AGGRESSIVE_BUYER_DOMINATION, AGGRESSIVE_SELLER_DOMINATION, TWO_SIDED_ABSORPTION)
   - Delta Divergence (BEARISH_ABSORPTION, BULLISH_ABSORPTION, EXPANSION, CHOP)
   - Deribit Options Gamma (Max Pain, Major Call Wall, Major Put Wall for BTC, ETH, SOL)
4. Fast concurrent async fetching (ThreadPoolExecutor, < 3.0s network turnaround).
5. Canonical Institutional Excel Formatting:
   - Row 1 Top Banner: "21_Tradfye_Orderflow | LAST UPDATED: YYYY-MM-DD HH:MM:SS IST (UTC) | ROWS: [N] | STATUS: LIVE"
   - Row 2 Column Headers with freeze_panes = "A3"
   - Dual IST & UTC timestamps, openpyxl gridlines enabled, 0 formula errors.
"""

from __future__ import annotations

import concurrent.futures
import datetime
import json
import logging
import math
import os
import pathlib
import sys
import tempfile
import time
import urllib.request
from typing import Dict, Any, List, Tuple

ROOT_DIR = pathlib.Path(__file__).resolve().parents[2]
DATA_DIR = ROOT_DIR / "Data"
EXCEL_PATH = DATA_DIR / "DataBase_Trading.xlsx"

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] [21_Tradfye] %(message)s")
logger = logging.getLogger("21_Tradfye")

# 18 Canonical Institutional Binance USDT-M Perpetuals
UNIVERSE_SYMBOLS: List[Tuple[str, str]] = [
    ("BTCUSDT", "BTC"),
    ("ETHUSDT", "ETH"),
    ("SOLUSDT", "SOL"),
    ("BNBUSDT", "BNB"),
    ("XRPUSDT", "XRP"),
    ("DOGEUSDT", "DOGE"),
    ("ADAUSDT", "ADA"),
    ("TRXUSDT", "TRX"),
    ("LINKUSDT", "LINK"),
    ("AVAXUSDT", "AVAX"),
    ("SUIUSDT", "SUI"),
    ("NEARUSDT", "NEAR"),
    ("DOTUSDT", "DOT"),
    ("LTCUSDT", "LTC"),
    ("BCHUSDT", "BCH"),
    ("APTUSDT", "APT"),
    ("OPUSDT", "OP"),
    ("ARBUSDT", "ARB"),
]

# Multi-timeframe specifications for continuous 2-day coverage
TIMEFRAMES: List[Tuple[str, int]] = [
    ("15m", 192),  # 48 hours = 2 days continuous (master trading horizon)
    ("1h", 48),    # 48 hours = 2 days continuous (macro trend & structural horizon)
    ("5m", 144),   # 12 hours continuous (high-frequency micro execution horizon)
]

USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
IST_TIMEZONE = datetime.timezone(datetime.timedelta(hours=5, minutes=30))
UTC_TIMEZONE = datetime.timezone.utc


def fetch_binance_klines(symbol: str, interval: str, limit: int) -> Tuple[str, str, List[Any]]:
    """Fetches klines from Binance Futures public API."""
    url = f"https://fapi.binance.com/fapi/v1/klines?symbol={symbol}&interval={interval}&limit={limit}"
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    try:
        with urllib.request.urlopen(req, timeout=8) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            if isinstance(data, list):
                return (symbol, interval, data)
    except Exception as e:
        logger.warning(f"Error fetching {symbol} {interval}: {e}")
    return (symbol, interval, [])


def fetch_deribit_gamma(currency: str = "BTC") -> Dict[str, float]:
    """Fetches Deribit options summary to calculate Max Pain and Gamma Walls."""
    url = f"https://www.deribit.com/api/v2/public/get_book_summary_by_currency?currency={currency}&kind=option"
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            raw = json.loads(resp.read().decode("utf-8"))
            results = raw.get("result", [])
            
            call_oi: Dict[float, float] = {}
            put_oi: Dict[float, float] = {}
            
            for item in results:
                inst_name = item.get("instrument_name", "")
                parts = inst_name.split("-")
                if len(parts) >= 4:
                    try:
                        strike = float(parts[2])
                        opt_type = parts[3]
                        oi = float(item.get("open_interest", 0.0))
                        if opt_type == "C":
                            call_oi[strike] = call_oi.get(strike, 0.0) + oi
                        elif opt_type == "P":
                            put_oi[strike] = put_oi.get(strike, 0.0) + oi
                    except ValueError:
                        continue
                        
            all_strikes = sorted(list(set(list(call_oi.keys()) + list(put_oi.keys()))))
            if not all_strikes:
                return {"max_pain": 0.0, "call_wall": 0.0, "put_wall": 0.0}
                
            call_wall = max(call_oi.items(), key=lambda x: x[1])[0] if call_oi else 0.0
            put_wall = max(put_oi.items(), key=lambda x: x[1])[0] if put_oi else 0.0
            
            min_pain = float("inf")
            max_pain_strike = all_strikes[len(all_strikes)//2]
            
            for test_strike in all_strikes:
                total_loss = 0.0
                for c_strike, c_oi in call_oi.items():
                    if test_strike > c_strike:
                        total_loss += (test_strike - c_strike) * c_oi
                for p_strike, p_oi in put_oi.items():
                    if test_strike < p_strike:
                        total_loss += (p_strike - test_strike) * p_oi
                if total_loss < min_pain:
                    min_pain = total_loss
                    max_pain_strike = test_strike
                    
            return {
                "max_pain": float(max_pain_strike),
                "call_wall": float(call_wall),
                "put_wall": float(put_wall)
            }
    except Exception as e:
        logger.warning(f"Error fetching Deribit options for {currency}: {e}")
        return {"max_pain": 0.0, "call_wall": 0.0, "put_wall": 0.0}


def process_all_universe_orderflow() -> List[Dict[str, Any]]:
    """Concurrently harvests multi-timeframe orderflow across all 18 universe symbols."""
    t0 = time.time()
    
    # 1. Fetch Deribit Options Gamma for BTC, ETH, SOL
    deribit_gamma: Dict[str, Dict[str, float]] = {}
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as gamma_executor:
        gamma_futures = {
            gamma_executor.submit(fetch_deribit_gamma, cur): cur
            for cur in ["BTC", "ETH", "SOL"]
        }
        for fut in concurrent.futures.as_completed(gamma_futures):
            cur = gamma_futures[fut]
            try:
                deribit_gamma[cur] = fut.result()
            except Exception:
                deribit_gamma[cur] = {"max_pain": 0.0, "call_wall": 0.0, "put_wall": 0.0}

    # 2. Concurrently fetch all Kline series (18 symbols * 3 timeframes = 54 queries)
    raw_series: List[Tuple[str, str, List[Any]]] = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=14) as kline_executor:
        kline_futures = [
            kline_executor.submit(fetch_binance_klines, sym, tf, lim)
            for sym, _ in UNIVERSE_SYMBOLS
            for tf, lim in TIMEFRAMES
        ]
        for fut in concurrent.futures.as_completed(kline_futures):
            raw_series.append(fut.result())
            
    logger.info(f"Harvested {len(raw_series)} series in {time.time()-t0:.2f}s")
    
    # Map raw series by (symbol, timeframe)
    series_map: Dict[Tuple[str, str], List[Any]] = {
        (sym, tf): klines for sym, tf, klines in raw_series
    }
    
    # 3. Process each symbol & timeframe chronologically for CVD accumulation
    all_rows: List[Dict[str, Any]] = []
    
    for sym, asset in UNIVERSE_SYMBOLS:
        opt_info = deribit_gamma.get(asset, {"max_pain": 0.0, "call_wall": 0.0, "put_wall": 0.0})
        
        for tf, _ in TIMEFRAMES:
            klines = series_map.get((sym, tf), [])
            if not klines:
                continue
                
            # Sort ascending by open time (Index 0) for monotonic CVD accumulation
            sorted_klines = sorted(klines, key=lambda k: int(k[0]))
            
            cumulative_delta_usd = 0.0
            series_rows: List[Dict[str, Any]] = []
            
            for k in sorted_klines:
                open_time_ms = int(k[0])
                open_p = float(k[1])
                high_p = float(k[2])
                low_p = float(k[3])
                close_p = float(k[4])
                base_vol = float(k[5])
                quote_vol = float(k[7])
                trades_count = int(k[8])
                taker_buy_quote = float(k[10])
                
                taker_sell_quote = max(0.0, quote_vol - taker_buy_quote)
                net_delta_usd = taker_buy_quote - taker_sell_quote
                net_delta_pct = (net_delta_usd / quote_vol * 100.0) if quote_vol > 0 else 0.0
                cumulative_delta_usd += net_delta_usd
                
                candle_vwap = (quote_vol / base_vol) if base_vol > 0 else close_p
                avg_trade_usd = (quote_vol / trades_count) if trades_count > 0 else 0.0
                poc_estimate = (high_p + low_p + 2.0 * close_p) / 4.0
                
                # Orderflow Regime Classification
                if net_delta_pct > 12.0:
                    regime = "AGGRESSIVE_BUYER_DOMINATION"
                elif net_delta_pct < -12.0:
                    regime = "AGGRESSIVE_SELLER_DOMINATION"
                else:
                    regime = "TWO_SIDED_ABSORPTION"
                    
                # Delta Divergence Classification
                price_change = close_p - open_p
                if price_change > 0 and net_delta_usd < 0:
                    divergence = "BEARISH_ABSORPTION"  # Buyers pushing up absorbed by limit sellers
                elif price_change < 0 and net_delta_usd > 0:
                    divergence = "BULLISH_ABSORPTION"  # Sellers pushing down absorbed by limit buyers
                elif price_change > 0 and net_delta_usd > 0:
                    divergence = "BULLISH_EXPANSION"
                elif price_change < 0 and net_delta_usd < 0:
                    divergence = "BEARISH_EXPANSION"
                else:
                    divergence = "NEUTRAL_CHOP"
                    
                dt_utc = datetime.datetime.fromtimestamp(open_time_ms / 1000.0, tz=UTC_TIMEZONE)
                dt_ist = dt_utc.astimezone(IST_TIMEZONE)
                
                series_rows.append({
                    "timestamp_ist": dt_ist.strftime("%Y-%m-%d %H:%M:%S IST"),
                    "timestamp_utc": dt_utc.strftime("%Y-%m-%d %H:%M:%S UTC"),
                    "asset": asset,
                    "market_pair": sym,
                    "timeframe": tf,
                    "open": open_p,
                    "high": high_p,
                    "low": low_p,
                    "close": close_p,
                    "total_vol_usd": quote_vol,
                    "taker_buy_usd": taker_buy_quote,
                    "taker_sell_usd": taker_sell_quote,
                    "net_delta_usd": net_delta_usd,
                    "net_delta_pct": net_delta_pct,
                    "cvd_usd": cumulative_delta_usd,
                    "candle_vwap": candle_vwap,
                    "trades_count": trades_count,
                    "avg_trade_usd": avg_trade_usd,
                    "poc_estimate": poc_estimate,
                    "regime": regime,
                    "divergence": divergence,
                    "deribit_max_pain": opt_info.get("max_pain", 0.0),
                    "deribit_call_wall": opt_info.get("call_wall", 0.0),
                    "deribit_put_wall": opt_info.get("put_wall", 0.0),
                })
                
            # Place newest candle at top of that series for immediate operator visibility
            series_rows.reverse()
            all_rows.extend(series_rows)
            
    logger.info(f"Total processed orderflow candle records: {len(all_rows)}")
    return all_rows


def update_excel_workbook(rows: List[Dict[str, Any]], max_retries: int = 6, retry_delay: float = 3.0) -> bool:
    """Writes all rows into DataBase_Trading.xlsx worksheet '21_Tradfye_Orderflow' with retry loop."""
    if not EXCEL_PATH.exists():
        logger.error(f"Workbook {EXCEL_PATH} not found!")
        return False
        
    for attempt in range(1, max_retries + 1):
        try:
            import openpyxl
            from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
            
            t0 = time.time()
            wb = openpyxl.load_workbook(EXCEL_PATH)
            sheet_name = "21_Tradfye_Orderflow"
            
            if sheet_name in wb.sheetnames:
                ws = wb[sheet_name]
                # Clear existing data rows completely
                ws.delete_rows(1, ws.max_row + 1)
            else:
                ws = wb.create_sheet(title=sheet_name)
                
            now_utc = datetime.datetime.now(UTC_TIMEZONE)
            now_ist = now_utc.astimezone(IST_TIMEZONE)
            ist_str = now_ist.strftime("%Y-%m-%d %H:%M:%S IST")
            utc_str = now_utc.strftime("%Y-%m-%d %H:%M:%S UTC")
            
            # Row 1 Banner
            banner_text = f"21_Tradfye_Orderflow | LAST UPDATED: {ist_str} ({utc_str}) | ROWS: {len(rows)} | STATUS: LIVE"
            ws.cell(row=1, column=1, value=banner_text)
            ws.merge_cells(start_row=1, start_column=1, end_row=1, end_column=25)
            
            banner_fill = PatternFill(start_color="1F4E78", end_color="1F4E78", fill_type="solid")
            banner_font = Font(name="Calibri", size=11, bold=True, color="FFFFFF")
            ws.cell(row=1, column=1).fill = banner_fill
            ws.cell(row=1, column=1).font = banner_font
            ws.cell(row=1, column=1).alignment = Alignment(horizontal="center", vertical="center")
            
            # Row 2 Headers
            headers = [
                "Sr.No", "Timestamp (IST)", "Timestamp (UTC)", "Asset", "Market Pair",
                "Timeframe", "Open ($)", "High ($)", "Low ($)", "Close ($)",
                "Total Vol ($)", "Taker Buy Vol ($)", "Taker Sell Vol ($)", "Net Delta ($)", "Net Delta (%)",
                "CVD ($)", "Candle VWAP ($)", "Trades Count", "Avg Trade ($)", "POC Estimate ($)",
                "Orderflow Regime", "Delta Divergence", "Deribit Max Pain ($)", "Deribit Call Wall ($)", "Deribit Put Wall ($)"
            ]
            
            header_fill = PatternFill(start_color="2F5597", end_color="2F5597", fill_type="solid")
            header_font = Font(name="Calibri", size=10, bold=True, color="FFFFFF")
            
            for col_idx, h in enumerate(headers, 1):
                c = ws.cell(row=2, column=col_idx, value=h)
                c.fill = header_fill
                c.font = header_font
                c.alignment = Alignment(horizontal="center", vertical="center")
                
            # Rows 3 onwards: Append data
            thin_side = Side(style="thin", color="D9D9D9")
            thin_border = Border(left=thin_side, right=thin_side, top=thin_side, bottom=thin_side)
            
            zebra_fill = PatternFill(start_color="F9FAFB", end_color="F9FAFB", fill_type="solid")
            white_fill = PatternFill(start_color="FFFFFF", end_color="FFFFFF", fill_type="solid")
            
            align_center = Alignment(horizontal="center", vertical="center")
            align_right = Alignment(horizontal="right", vertical="center")
            align_left = Alignment(horizontal="left", vertical="center")
            
            regime_buyer_fill = PatternFill(start_color="E2EFDA", end_color="E2EFDA", fill_type="solid")
            regime_seller_fill = PatternFill(start_color="FCE4D6", end_color="FCE4D6", fill_type="solid")
            
            for r_idx, row in enumerate(rows, 3):
                sr_no = r_idx - 2
                is_zebra = (sr_no % 2 == 0)
                base_fill = zebra_fill if is_zebra else white_fill
                
                price_fmt = "$#,##0.00" if row["close"] >= 1.0 else "$#,##0.0000"
                
                c_vals = [
                    (1, sr_no, align_center, "0"),
                    (2, row["timestamp_ist"], align_center, None),
                    (3, row["timestamp_utc"], align_center, None),
                    (4, row["asset"], align_center, None),
                    (5, row["market_pair"], align_center, None),
                    (6, row["timeframe"], align_center, None),
                    (7, row["open"], align_right, price_fmt),
                    (8, row["high"], align_right, price_fmt),
                    (9, row["low"], align_right, price_fmt),
                    (10, row["close"], align_right, price_fmt),
                    (11, row["total_vol_usd"], align_right, "$#,##0.00"),
                    (12, row["taker_buy_usd"], align_right, "$#,##0.00"),
                    (13, row["taker_sell_usd"], align_right, "$#,##0.00"),
                    (14, row["net_delta_usd"], align_right, "$#,##0.00"),
                    (15, row["net_delta_pct"] / 100.0, align_right, "0.00%"),
                    (16, row["cvd_usd"], align_right, "$#,##0.00"),
                    (17, row["candle_vwap"], align_right, price_fmt),
                    (18, row["trades_count"], align_right, "#,##0"),
                    (19, row["avg_trade_usd"], align_right, "$#,##0.00"),
                    (20, row["poc_estimate"], align_right, price_fmt),
                    (21, row["regime"], align_center, None),
                    (22, row["divergence"], align_center, None),
                    (23, row["deribit_max_pain"] if row["deribit_max_pain"] > 0 else "-", align_right, price_fmt if row["deribit_max_pain"] > 0 else None),
                    (24, row["deribit_call_wall"] if row["deribit_call_wall"] > 0 else "-", align_right, price_fmt if row["deribit_call_wall"] > 0 else None),
                    (25, row["deribit_put_wall"] if row["deribit_put_wall"] > 0 else "-", align_right, price_fmt if row["deribit_put_wall"] > 0 else None),
                ]
                
                for col_i, val, aln, num_fmt in c_vals:
                    cell = ws.cell(row=r_idx, column=col_i, value=val)
                    cell.alignment = aln
                    cell.border = thin_border
                    
                    if col_i == 21:
                        if val == "AGGRESSIVE_BUYER_DOMINATION":
                            cell.fill = regime_buyer_fill
                        elif val == "AGGRESSIVE_SELLER_DOMINATION":
                            cell.fill = regime_seller_fill
                        else:
                            cell.fill = base_fill
                    else:
                        cell.fill = base_fill
                        
                    if num_fmt:
                        cell.number_format = num_fmt
                        
            # Sheet view formatting
            ws.views.sheetView[0].showGridLines = True
            ws.freeze_panes = "A3"
            
            # Auto-fit column widths
            col_widths = {
                1: 8, 2: 24, 3: 24, 4: 10, 5: 14, 6: 12,
                7: 14, 8: 14, 9: 14, 10: 14, 11: 18, 12: 18,
                13: 18, 14: 18, 15: 14, 16: 20, 17: 16, 18: 14,
                19: 16, 20: 16, 21: 30, 22: 24, 23: 18, 24: 18, 25: 18
            }
            for col_idx, width in col_widths.items():
                col_letter = openpyxl.utils.get_column_letter(col_idx)
                ws.column_dimensions[col_letter].width = width

            # Atomic file write to avoid file-lock conflicts
            temp_dir = DATA_DIR
            temp_fd, temp_path_str = tempfile.mkstemp(prefix="DataBase_Trading_tmp_", suffix=".xlsx", dir=temp_dir)
            os.close(temp_fd)
            temp_path = pathlib.Path(temp_path_str)
            
            wb.save(temp_path)
            wb.close()
            
            # Replace atomically
            temp_path.replace(EXCEL_PATH)
            logger.info(f"Successfully saved {len(rows)} orderflow rows into {EXCEL_PATH} in {time.time()-t0:.2f}s")
            return True
            
        except Exception as e:
            logger.warning(f"Attempt {attempt}/{max_retries} failed with {type(e).__name__}: {e}. Retrying in {retry_delay}s...")
            time.sleep(retry_delay)
            
    logger.error(f"All {max_retries} attempts to update Excel workbook failed!")
    return False


def main():
    logger.info("Starting Tradfye Multi-Timeframe Orderflow Harvesting for 18-Asset Universe...")
    start_time = time.time()
    rows = process_all_universe_orderflow()
    if not rows:
        logger.error("No orderflow rows harvested!")
        sys.exit(1)
        
    success = update_excel_workbook(rows)
    if success:
        logger.info(f"Tradfye Orderflow completed successfully in {time.time()-start_time:.2f}s!")
        sys.exit(0)
    else:
        logger.error("Failed to update Excel workbook!")
        sys.exit(1)


if __name__ == "__main__":
    main()
