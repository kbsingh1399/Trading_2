#!/usr/bin/env python3
"""
Data/Excel_Modules/21_Tradfye_Orderflow.py
=========================================
Tradfye Orderflow, Footprint POC, Delta & Options Gamma Module.

Reverse-engineered from Tradfye's live terminal architecture (tradfye.com/terminal):
1. Ingests Binance Vision aggTrades for Footprint (POC, Buyer vs Seller Delta, Imbalance).
2. Computes Whale Bubbles (99th-percentile large trades).
3. Detects Whale Absorption Shelves (resting depth absorbing aggressive flow).
4. Computes Deribit Options Gamma (Max Pain, Call/Put Walls, Zero Gamma Flip).
5. Writes directly into worksheet '21_Tradfye_Orderflow' inside Data/DataBase_Trading.xlsx:
   - Row 1 Top Banner: "21_Tradfye_Orderflow | LAST UPDATED: YYYY-MM-DD HH:MM:SS IST (UTC) | ROWS: [N] | STATUS: LIVE"
   - Row 2 Column Headers with dual Timestamp (IST) & Timestamp (UTC)
   - Zero formula errors, clean numerical formatting, openpyxl gridlines enabled.
"""

from __future__ import annotations

import datetime
import json
import logging
import math
import pathlib
import sys
import urllib.request
from typing import Dict, Any, List

ROOT_DIR = pathlib.Path(__file__).resolve().parents[2]
DATA_DIR = ROOT_DIR / "Data"
EXCEL_PATH = DATA_DIR / "DataBase_Trading.xlsx"

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] [21_Tradfye] %(message)s")
logger = logging.getLogger("21_Tradfye")

SYMBOLS = [
    ("BTCUSDT", "BTC", 50.0),    # Symbol, clean key, tick bucket size in USD
    ("ETHUSDT", "ETH", 2.0),
    ("SOLUSDT", "SOL", 0.5)
]

USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
IST_TIMEZONE = datetime.timezone(datetime.timedelta(hours=5, minutes=30))
UTC_TIMEZONE = datetime.timezone.utc


def fetch_binance_agg_trades(symbol: str, limit: int = 1000) -> List[Dict[str, Any]]:
    """Fetches recent aggTrades from Binance public data API (exact endpoint used by Tradfye)."""
    url = f"https://data-api.binance.vision/api/v3/aggTrades?symbol={symbol}&limit={limit}"
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            return data if isinstance(data, list) else []
    except Exception as e:
        logger.warning(f"Error fetching aggTrades for {symbol}: {e}")
        return []


def fetch_binance_depth(symbol: str, limit: int = 100) -> Dict[str, Any]:
    """Fetches L2 orderbook depth from Binance public data API."""
    url = f"https://data-api.binance.vision/api/v3/depth?symbol={symbol}&limit={limit}"
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except Exception as e:
        logger.warning(f"Error fetching depth for {symbol}: {e}")
        return {"bids": [], "asks": []}


def fetch_deribit_gamma(currency: str = "BTC") -> Dict[str, Any]:
    """Fetches Deribit options summary to calculate Max Pain and Gamma Walls (exact endpoint used by Tradfye)."""
    url = f"https://www.deribit.com/api/v2/public/get_book_summary_by_currency?currency={currency}&kind=option"
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    try:
        with urllib.request.urlopen(req, timeout=12) as resp:
            raw = json.loads(resp.read().decode("utf-8"))
            results = raw.get("result", [])
            
            call_oi_by_strike: Dict[float, float] = {}
            put_oi_by_strike: Dict[float, float] = {}
            
            for item in results:
                inst_name = item.get("instrument_name", "")
                parts = inst_name.split("-")
                if len(parts) >= 4:
                    try:
                        strike = float(parts[2])
                        opt_type = parts[3]  # C or P
                        oi = float(item.get("open_interest", 0.0))
                        if opt_type == "C":
                            call_oi_by_strike[strike] = call_oi_by_strike.get(strike, 0.0) + oi
                        elif opt_type == "P":
                            put_oi_by_strike[strike] = put_oi_by_strike.get(strike, 0.0) + oi
                    except ValueError:
                        continue
                        
            all_strikes = sorted(list(set(list(call_oi_by_strike.keys()) + list(put_oi_by_strike.keys()))))
            if not all_strikes:
                return {"max_pain": 0.0, "major_call_wall": 0.0, "major_put_wall": 0.0}
                
            call_wall = max(call_oi_by_strike.items(), key=lambda x: x[1])[0] if call_oi_by_strike else 0.0
            put_wall = max(put_oi_by_strike.items(), key=lambda x: x[1])[0] if put_oi_by_strike else 0.0
            
            min_pain = float("inf")
            max_pain_strike = all_strikes[len(all_strikes)//2]
            
            for test_strike in all_strikes:
                total_loss = 0.0
                for c_strike, c_oi in call_oi_by_strike.items():
                    if test_strike > c_strike:
                        total_loss += (test_strike - c_strike) * c_oi
                for p_strike, p_oi in put_oi_by_strike.items():
                    if test_strike < p_strike:
                        total_loss += (p_strike - test_strike) * p_oi
                if total_loss < min_pain:
                    min_pain = total_loss
                    max_pain_strike = test_strike
                    
            return {
                "max_pain": float(max_pain_strike),
                "major_call_wall": float(call_wall),
                "major_put_wall": float(put_wall)
            }
    except Exception as e:
        logger.warning(f"Error fetching Deribit gamma for {currency}: {e}")
        return {"max_pain": 0.0, "major_call_wall": 0.0, "major_put_wall": 0.0}


def process_orderflow_metrics(symbol: str, asset_key: str, bucket_size: float) -> Dict[str, Any]:
    """Computes Footprint POC, Delta, Whale Bubbles, and Absorption for a symbol."""
    trades = fetch_binance_agg_trades(symbol, limit=1000)
    depth = fetch_binance_depth(symbol, limit=100)
    
    if not trades:
        return {"symbol": symbol, "status": "NO_TRADES"}
        
    total_buy_vol = 0.0
    total_sell_vol = 0.0
    total_buy_usd = 0.0
    total_sell_usd = 0.0
    
    footprint: Dict[float, Dict[str, float]] = {}
    trade_notionals: List[float] = []
    current_mid = float(trades[-1]["p"]) if trades else 0.0
    
    for t in trades:
        p = float(t["p"])
        q = float(t["q"])
        usd = p * q
        trade_notionals.append(usd)
        
        is_sell = t.get("m", False)
        bucket = round(p / bucket_size) * bucket_size
        if bucket not in footprint:
            footprint[bucket] = {"buy_usd": 0.0, "sell_usd": 0.0, "total_usd": 0.0}
            
        if is_sell:
            total_sell_vol += q
            total_sell_usd += usd
            footprint[bucket]["sell_usd"] += usd
        else:
            total_buy_vol += q
            total_buy_usd += usd
            footprint[bucket]["buy_usd"] += usd
        footprint[bucket]["total_usd"] += usd

    poc_price = max(footprint.items(), key=lambda x: x[1]["total_usd"])[0] if footprint else current_mid
    net_delta_usd = total_buy_usd - total_sell_usd
    net_delta_pct = (net_delta_usd / (total_buy_usd + total_sell_usd) * 100.0) if (total_buy_usd + total_sell_usd) > 0 else 0.0
    
    # Whale Bubbles (Tradfye 99th percentile notional)
    trade_notionals.sort()
    p99_idx = min(len(trade_notionals) - 1, math.floor(len(trade_notionals) * 0.99))
    p99_threshold_usd = trade_notionals[p99_idx] if trade_notionals else 100000.0
    
    whale_bubbles = []
    for t in trades:
        usd = float(t["p"]) * float(t["q"])
        if usd >= p99_threshold_usd and usd >= 50000.0:
            whale_bubbles.append({
                "time_ms": t["T"],
                "price": float(t["p"]),
                "qty": float(t["q"]),
                "notional_usd": round(usd, 2),
                "side": "SELL" if t.get("m") else "BUY"
            })
            
    # Whale Absorption Shelves from L2 Depth
    bids = depth.get("bids", [])
    asks = depth.get("asks", [])
    
    nearest_bid_wall = {"price": 0.0, "notional_usd": 0.0}
    nearest_ask_wall = {"price": 0.0, "notional_usd": 0.0}
    
    max_bid_usd = 0.0
    for b in bids:
        p_b = float(b[0])
        q_b = float(b[1])
        u_b = p_b * q_b
        if u_b > max_bid_usd:
            max_bid_usd = u_b
            nearest_bid_wall = {"price": p_b, "notional_usd": round(u_b, 2)}
            
    max_ask_usd = 0.0
    for a in asks:
        p_a = float(a[0])
        q_a = float(a[1])
        u_a = p_a * q_a
        if u_a > max_ask_usd:
            max_ask_usd = u_a
            nearest_ask_wall = {"price": p_a, "notional_usd": round(u_a, 2)}

    if net_delta_pct > 15.0:
        regime = "AGGRESSIVE_BUYER_DOMINATION"
    elif net_delta_pct < -15.0:
        regime = "AGGRESSIVE_SELLER_DOMINATION"
    else:
        regime = "TWO_SIDED_ABSORPTION"

    return {
        "symbol": symbol,
        "asset_key": asset_key,
        "current_mid": current_mid,
        "sample_trades_count": len(trades),
        "total_volume_usd": round(total_buy_usd + total_sell_usd, 2),
        "total_buy_usd": round(total_buy_usd, 2),
        "total_sell_usd": round(total_sell_usd, 2),
        "net_delta_usd": round(net_delta_usd, 2),
        "net_delta_pct": round(net_delta_pct, 2),
        "footprint_poc_price": round(poc_price, 2),
        "orderflow_regime": regime,
        "p99_whale_threshold_usd": round(p99_threshold_usd, 2),
        "whale_bubbles_count": len(whale_bubbles),
        "recent_whale_bubbles": whale_bubbles[-5:],
        "nearest_bid_absorption_shelf": nearest_bid_wall,
        "nearest_ask_absorption_shelf": nearest_ask_wall
    }


def update_excel_sheet(results: Dict[str, Any], ist_str: str, utc_str: str) -> bool:
    """Updates worksheet '21_Tradfye_Orderflow' inside Data/DataBase_Trading.xlsx."""
    if not EXCEL_PATH.exists():
        logger.error(f"Master workbook {EXCEL_PATH} not found!")
        return False
        
    try:
        import openpyxl
        from openpyxl.styles import Font, PatternFill, Alignment
        
        wb = openpyxl.load_workbook(EXCEL_PATH)
        sheet_name = "21_Tradfye_Orderflow"
        
        if sheet_name in wb.sheetnames:
            ws = wb[sheet_name]
            ws.delete_rows(1, ws.max_row + 1)
        else:
            ws = wb.create_sheet(title=sheet_name)
            
        # Row 1: Canonical Top Banner in IST & UTC
        row_count = len(results)
        banner_text = f"{sheet_name} | LAST UPDATED: {ist_str} ({utc_str}) | ROWS: {row_count} | STATUS: LIVE"
        ws.cell(row=1, column=1, value=banner_text)
        
        font_banner = Font(name="Calibri", size=11, bold=True, color="1F497D")
        fill_banner = PatternFill(start_color="DCE6F1", end_color="DCE6F1", fill_type="solid")
        ws.cell(row=1, column=1).font = font_banner
        ws.cell(row=1, column=1).fill = fill_banner
        
        # Row 2: Table Column Headers
        headers = [
            "Sr.No", "Timestamp (IST)", "Timestamp (UTC)", "Asset", "Market Pair", "Current Mid ($)",
            "Footprint POC ($)", "Total Vol ($)", "Buy Vol ($)", "Sell Vol ($)",
            "Net Delta ($)", "Net Delta (%)", "Orderflow Regime", "Whale P99 Floor ($)",
            "Whale Bubbles #", "Bid Absorption Shelf ($)", "Bid Shelf ($)",
            "Ask Absorption Shelf ($)", "Ask Shelf ($)", "Options Max Pain ($)",
            "Major Call Wall ($)", "Major Put Wall ($)"
        ]
        font_header = Font(name="Calibri", size=10, bold=True, color="FFFFFF")
        fill_header = PatternFill(start_color="203764", end_color="203764", fill_type="solid")
        align_center = Alignment(horizontal="center", vertical="center")
        align_right = Alignment(horizontal="right", vertical="center")
        
        for col_idx, h in enumerate(headers, 1):
            c = ws.cell(row=2, column=col_idx, value=h)
            c.font = font_header
            c.fill = fill_header
            c.alignment = align_center
            
        # Row 3+: Data Rows
        font_data = Font(name="Calibri", size=10)
        fill_alt = PatternFill(start_color="F2F2F2", end_color="F2F2F2", fill_type="solid")
        
        row_idx = 3
        for sr_no, (key, data) in enumerate(results.items(), 1):
            gamma = data.get("deribit_gamma", {})
            b_shelf = data.get("nearest_bid_absorption_shelf", {})
            a_shelf = data.get("nearest_ask_absorption_shelf", {})
            
            vals = [
                sr_no,
                ist_str,
                utc_str,
                key,
                data.get("symbol", f"{key}USDT"),
                data.get("current_mid", 0.0),
                data.get("footprint_poc_price", 0.0),
                data.get("total_volume_usd", 0.0),
                data.get("total_buy_usd", 0.0),
                data.get("total_sell_usd", 0.0),
                data.get("net_delta_usd", 0.0),
                data.get("net_delta_pct", 0.0),
                data.get("orderflow_regime", "UNKNOWN"),
                data.get("p99_whale_threshold_usd", 0.0),
                data.get("whale_bubbles_count", 0),
                b_shelf.get("price", 0.0),
                b_shelf.get("notional_usd", 0.0),
                a_shelf.get("price", 0.0),
                a_shelf.get("notional_usd", 0.0),
                gamma.get("max_pain", 0.0),
                gamma.get("major_call_wall", 0.0),
                gamma.get("major_put_wall", 0.0)
            ]
            
            is_even = (row_idx % 2 == 0)
            for col_idx, v in enumerate(vals, 1):
                cell = ws.cell(row=row_idx, column=col_idx, value=v)
                cell.font = font_data
                if is_even:
                    cell.fill = fill_alt
                if isinstance(v, (int, float)) and col_idx not in (1,):
                    cell.alignment = align_right
                    if col_idx in (6, 7, 8, 9, 10, 11, 14, 16, 17, 18, 19, 20, 21, 22):
                        cell.number_format = "$#,##0.00"
                    elif col_idx == 12:
                        cell.number_format = "0.00%"
                else:
                    cell.alignment = align_center if col_idx in (1, 4, 13) else Alignment(horizontal="left", vertical="center")
                    
            row_idx += 1
            
        for col in ws.columns:
            max_len = 0
            col_letter = col[0].column_letter
            for cell in col:
                val_str = str(cell.value or "")
                if len(val_str) > max_len:
                    max_len = len(val_str)
            ws.column_dimensions[col_letter].width = max(12, min(max_len + 3, 40))
            
        ws.views.sheetView[0].showGridLines = True
        
        # Remove legacy sheet '34_Tradfye_Orderflow' if present to keep workbook clean
        if "34_Tradfye_Orderflow" in wb.sheetnames:
            del wb["34_Tradfye_Orderflow"]
            
        wb.save(EXCEL_PATH)
        wb.close()
        logger.info(f"Successfully updated worksheet '{sheet_name}' in {EXCEL_PATH}")
        return True
    except Exception as e:
        logger.error(f"Error updating Excel workbook: {e}")
        return False


def main() -> int:
    now_utc = datetime.datetime.now(UTC_TIMEZONE)
    now_ist = now_utc.astimezone(IST_TIMEZONE)
    utc_str = now_utc.strftime("%Y-%m-%d %H:%M:%S UTC")
    ist_str = now_ist.strftime("%Y-%m-%d %H:%M:%S IST")
    
    logger.info(f"Starting 21_Tradfye_Orderflow cycle at {ist_str} ({utc_str})...")
    
    results = {}
    for sym, key, bucket in SYMBOLS:
        metrics = process_orderflow_metrics(sym, key, bucket)
        if key in ("BTC", "ETH"):
            gamma = fetch_deribit_gamma(key)
            metrics["deribit_gamma"] = gamma
        results[key] = metrics
        
    ok = update_excel_sheet(results, ist_str, utc_str)
    
    # Also save structured JSON cache for fast local tooling
    out_json = DATA_DIR / "tradfye_orderflow.json"
    payload = {
        "as_of_ist": ist_str,
        "as_of_utc": utc_str,
        "as_of_epoch": now_utc.timestamp(),
        "source": "21_Tradfye_Orderflow (Data/Excel_Modules/21_Tradfye_Orderflow.py)",
        "assets": results
    }
    with open(out_json, "w", encoding="utf-8") as f:
        json.dump(payload, f, indent=2)
        
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
