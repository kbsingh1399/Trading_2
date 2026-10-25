from __future__ import annotations

# Pure Parquet Pipeline

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
ROOT = ROOT_DIR
DATA_DIR = ROOT_DIR / "Data"

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


def dump_tradfye_to_parquet(rows: list[dict], feed_name: str = "21_Tradfye_Orderflow") -> bool:
    if not rows:
        logger.warning("No Tradfye orderflow rows to dump.")
        return False
    sys.path.insert(0, str(ROOT / 'Collectors' / 'Core'))
    sys.path.insert(0, str(ROOT / 'Terminal' / 'Data_Factory'))
    from parquet_feed_writer import write_parquet_feed
    meta = write_parquet_feed(feed_name, rows)
    logger.info(f"Successfully dumped {len(rows)} Tradfye orderflow rows into Parquet feed '{feed_name}': {meta.get('byte_size')} bytes in {meta.get('write_latency_ms', 0):.2f}ms.")
    return True


def main():
    logger.info("Starting Tradfye Multi-Timeframe Orderflow Harvesting for 18-Asset Universe...")
    start_time = time.time()
    rows = process_all_universe_orderflow()
    if not rows:
        logger.error("No orderflow rows harvested!")
        sys.exit(1)

    success = dump_tradfye_to_parquet(rows)
    if success:
        logger.info(f"Tradfye Orderflow completed successfully in {time.time()-start_time:.2f}s!")
        sys.exit(0)
    else:
        logger.error("Failed to dump Tradfye Orderflow to Parquet!")
        sys.exit(1)


if __name__ == "__main__":
    main()
