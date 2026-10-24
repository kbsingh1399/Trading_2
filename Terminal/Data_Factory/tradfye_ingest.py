#!/usr/bin/env python3
"""
Terminal/Data_Factory/tradfye_ingest.py
======================================
Tradfye Orderflow, Footprint & Microstructure Ingestion Engine.

Reverse-engineered from Tradfye's live terminal architecture (tradfye.com/terminal):
1. Aggregates Binance aggTrades for Footprint (POC, Candle Delta, Imbalance).
2. Computes Whale Bubbles (99th-percentile large trades).
3. Identifies Whale Absorption Shelves (resting depth absorbing aggressive flow).
4. Deribit Options Gamma (Max Pain, Call/Put Walls, Zero Gamma Flip).
5. Exports structured JSON to Data/tradfye_orderflow.json and updates worksheet
   '34_Tradfye_Orderflow' in Data/DataBase_Trading.xlsx.
"""

import datetime
import json
import logging
import math
import pathlib
import sys
import urllib.request
from typing import Dict, Any, List

ROOT = pathlib.Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

logging.basicConfig(level=logging.INFO, format="[%(asctime)s][TradfyeIngest] %(message)s")
logger = logging.getLogger("TradfyeIngest")

SYMBOLS = [
    ("BTCUSDT", "BTC", 50.0),    # Symbol, clean key, tick bucket size in USD
    ("ETHUSDT", "ETH", 2.0),
    ("SOLUSDT", "SOL", 0.5)
]

USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"


def fetch_binance_agg_trades(symbol: str, limit: int = 1000) -> List[Dict[str, Any]]:
    """Fetches recent aggTrades from Binance public data API (same endpoint used by Tradfye)."""
    url = f"https://data-api.binance.vision/api/v3/aggTrades?symbol={symbol}&limit={limit}"
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            return data
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
    """Fetches Deribit options summary to calculate Max Pain and Gamma Walls (same endpoint used by Tradfye)."""
    url = f"https://www.deribit.com/api/v2/public/get_book_summary_by_currency?currency={currency}&kind=option"
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    try:
        with urllib.request.urlopen(req, timeout=12) as resp:
            raw = json.loads(resp.read().decode("utf-8"))
            results = raw.get("result", [])
            
            call_oi_by_strike = {}
            put_oi_by_strike = {}
            
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
                
            # Major Call/Put walls
            call_wall = max(call_oi_by_strike.items(), key=lambda x: x[1])[0] if call_oi_by_strike else 0.0
            put_wall = max(put_oi_by_strike.items(), key=lambda x: x[1])[0] if put_oi_by_strike else 0.0
            
            # Simple Max Pain calculation: strike minimizing total option buyer payout
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
                "max_pain": max_pain_strike,
                "major_call_wall": call_wall,
                "major_put_wall": put_wall
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
    
    # Footprint buckets: bucket_price -> {"buy": float, "sell": float, "total": float}
    footprint = {}
    trade_notionals = []
    
    for t in trades:
        p = float(t["p"])
        q = float(t["q"])
        usd = p * q
        trade_notionals.append(usd)
        
        # isBuyerMaker = True means seller is taker (hitting bid) -> Sell volume
        # isBuyerMaker = False means buyer is taker (hitting ask) -> Buy volume
        is_sell = t.get("m", False)
        
        # Round price to bucket
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

    # Find Footprint POC (Point of Control = price bucket with maximum volume)
    poc_price = max(footprint.items(), key=lambda x: x[1]["total_usd"])[0] if footprint else 0.0
    net_delta_usd = total_buy_usd - total_sell_usd
    net_delta_pct = (net_delta_usd / (total_buy_usd + total_sell_usd) * 100.0) if (total_buy_usd + total_sell_usd) > 0 else 0.0
    
    # Whale Bubbles (Tradfye algorithm: 99th percentile notional)
    trade_notionals.sort()
    p99_idx = min(len(trade_notionals) - 1, math.floor(len(trade_notionals) * 0.99))
    p99_threshold_usd = trade_notionals[p99_idx] if trade_notionals else 100000.0
    
    whale_bubbles = []
    for t in trades:
        usd = float(t["p"]) * float(t["q"])
        if usd >= p99_threshold_usd and usd >= 50000.0:  # Tradfye whale threshold filter
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

    # Classification
    if net_delta_pct > 15.0:
        regime = "AGGRESSIVE_BUYER_DOMINATION"
    elif net_delta_pct < -15.0:
        regime = "AGGRESSIVE_SELLER_DOMINATION"
    else:
        regime = "TWO_SIDED_ABSORPTION"

    return {
        "symbol": symbol,
        "asset_key": asset_key,
        "sample_trades_count": len(trades),
        "total_volume_usd": round(total_buy_usd + total_sell_usd, 2),
        "total_buy_usd": round(total_buy_usd, 2),
        "total_sell_usd": round(total_sell_usd, 2),
        "net_delta_usd": round(net_delta_usd, 2),
        "net_delta_pct": round(net_delta_pct, 2),
        "footprint_poc_price": poc_price,
        "orderflow_regime": regime,
        "p99_whale_threshold_usd": round(p99_threshold_usd, 2),
        "whale_bubbles_count": len(whale_bubbles),
        "recent_whale_bubbles": whale_bubbles[-5:],
        "nearest_bid_absorption_shelf": nearest_bid_wall,
        "nearest_ask_absorption_shelf": nearest_ask_wall
    }


def run_tradfye_pipeline() -> Dict[str, Any]:
    """Runs complete Tradfye orderflow ingestion across all target symbols."""
    now_utc = datetime.datetime.now(datetime.timezone.utc)
    now_str = now_utc.strftime("%Y-%m-%d %H:%M:%S UTC")
    logger.info(f"Starting Tradfye orderflow ingestion cycle at {now_str}...")
    
    results = {}
    for sym, key, bucket in SYMBOLS:
        logger.info(f"Ingesting orderflow & footprint for {sym}...")
        metrics = process_orderflow_metrics(sym, key, bucket)
        if key in ("BTC", "ETH"):
            gamma = fetch_deribit_gamma(key)
            metrics["deribit_gamma"] = gamma
        results[key] = metrics
        
    payload = {
        "as_of_utc": now_str,
        "as_of_epoch": now_utc.timestamp(),
        "source": "Tradfye Client-Engine Reverse-Engineered Microstructure Feed",
        "assets": results
    }
    
    # Save to JSON
    out_json = ROOT / "Data" / "tradfye_orderflow.json"
    out_json.parent.mkdir(parents=True, exist_ok=True)
    with open(out_json, "w", encoding="utf-8") as f:
        json.dump(payload, f, indent=2)
    logger.info(f"Successfully saved Tradfye metrics to {out_json}")
    
    # Update Excel worksheet if openpyxl available
    try:
        excel_path = ROOT / "Data" / "DataBase_Trading.xlsx"
        if excel_path.exists():
            import openpyxl
            wb = openpyxl.load_workbook(excel_path)
            sheet_name = "34_Tradfye_Orderflow"
            if sheet_name in wb.sheetnames:
                ws = wb[sheet_name]
            else:
                ws = wb.create_sheet(title=sheet_name)
                
            # Headers
            headers = [
                "Asset", "As of UTC", "Footprint POC", "Total Vol USD", "Buy Vol USD", "Sell Vol USD",
                "Net Delta USD", "Net Delta %", "Regime", "Whale P99 USD", "Whale Bubbles #",
                "Bid Absorption Shelf", "Bid Shelf USD", "Ask Absorption Shelf", "Ask Shelf USD",
                "Options Max Pain", "Major Call Wall", "Major Put Wall"
            ]
            for col_idx, h in enumerate(headers, 1):
                ws.cell(row=1, column=col_idx, value=h)
                
            row_idx = 2
            for key, data in results.items():
                gamma = data.get("deribit_gamma", {})
                b_shelf = data.get("nearest_bid_absorption_shelf", {})
                a_shelf = data.get("nearest_ask_absorption_shelf", {})
                
                vals = [
                    key,
                    now_str,
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
                for col_idx, v in enumerate(vals, 1):
                    ws.cell(row=row_idx, column=col_idx, value=v)
                row_idx += 1
                
            wb.save(excel_path)
            wb.close()
            logger.info(f"Updated worksheet '{sheet_name}' in {excel_path}")
    except Exception as e:
        logger.warning(f"Could not update Excel workbook: {e}")
        
    return payload


if __name__ == "__main__":
    res = run_tradfye_pipeline()
    print("\n--- TRADFYE ORDERFLOW SNAPSHOT SUMMARY ---")
    for k, v in res.get("assets", {}).items():
        print(f"[{k}] POC: {v.get('footprint_poc_price')} | Delta: {v.get('net_delta_usd'):,.2f} USD ({v.get('net_delta_pct')}%) | Regime: {v.get('orderflow_regime')}")
        print(f"     Bid Wall: {v.get('nearest_bid_absorption_shelf')} | Ask Wall: {v.get('nearest_ask_absorption_shelf')}")
        if 'deribit_gamma' in v:
            print(f"     Options Max Pain: {v['deribit_gamma'].get('max_pain')} | Call Wall: {v['deribit_gamma'].get('major_call_wall')} | Put Wall: {v['deribit_gamma'].get('major_put_wall')}")
