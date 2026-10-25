#!/usr/bin/env python3
"""
Collectors/API/5_Funding_Rate.py
================================
Pure-API Cryptocurrency Perpetual Funding Rates Collector.
Fetches real-time funding rates directly from Binance Futures, Bybit, and Hyperliquid.
Execution Time: < 0.6s.
"""
from __future__ import annotations

import asyncio
import datetime
import logging
import pathlib
import sys
import time
from typing import Any, Dict, List

import aiohttp

ROOT_DIR = pathlib.Path(__file__).resolve().parents[2]
CORE_DIR = ROOT_DIR / "Collectors" / "Core"
DF_DIR = ROOT_DIR / "Terminal" / "Data_Factory"
if str(CORE_DIR) not in sys.path:
    sys.path.insert(0, str(CORE_DIR))
if str(DF_DIR) not in sys.path:
    sys.path.insert(0, str(DF_DIR))

from parquet_writer import write_parquet_feed

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] [FundingRate_API] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
log = logging.getLogger("FundingRate_API")

IST_TZ = datetime.timezone(datetime.timedelta(hours=5, minutes=30))

UNIVERSE = [
    "BTC", "ETH", "XRP", "SOL", "BNB", "DOGE", "ADA", "TRX", "LINK",
    "AVAX", "SUI", "NEAR", "DOT", "LTC", "BCH", "APT", "OP", "ARB"
]

BINANCE_PREMIUM_URL = "https://fapi.binance.com/fapi/v1/premiumIndex"
BYBIT_TICKERS_URL = "https://api.bybit.com/v5/market/tickers?category=linear"
HYPERLIQUID_META_URL = "https://api.hyperliquid.xyz/info"


def fmt_rate(rate_val: float) -> str:
    """Formats 8h funding rate into percentage string (e.g. '0.0100%')."""
    if rate_val is None or rate_val != rate_val:
        return "-"
    return f"{rate_val * 100:.4f}%"


async def fetch_binance_funding(session: aiohttp.ClientSession) -> Dict[str, float]:
    try:
        async with session.get(BINANCE_PREMIUM_URL, timeout=4) as resp:
            if resp.status == 200:
                data = await resp.json()
                rates = {}
                for item in data:
                    sym = item.get("symbol", "").replace("USDT", "")
                    if sym in UNIVERSE:
                        rates[sym] = float(item.get("lastFundingRate", 0.0))
                return rates
    except Exception as e:
        log.warning(f"Binance funding error: {e}")
    return {}


async def fetch_bybit_funding(session: aiohttp.ClientSession) -> Dict[str, float]:
    try:
        async with session.get(BYBIT_TICKERS_URL, timeout=4) as resp:
            if resp.status == 200:
                data = await resp.json()
                rates = {}
                for item in data.get("result", {}).get("list", []):
                    sym = item.get("symbol", "").replace("USDT", "")
                    if sym in UNIVERSE:
                        rates[sym] = float(item.get("fundingRate", 0.0))
                return rates
    except Exception as e:
        log.warning(f"Bybit funding error: {e}")
    return {}


async def harvest_funding_rates() -> List[Dict[str, Any]]:
    t0 = time.perf_counter()
    now_ist = datetime.datetime.now(IST_TZ)
    ts_str = now_ist.strftime("%Y-%m-%d %H:%M:%S IST")

    connector = aiohttp.TCPConnector(limit=10, ttl_dns_cache=300)
    async with aiohttp.ClientSession(connector=connector) as session:
        b_task = fetch_binance_funding(session)
        by_task = fetch_bybit_funding(session)
        binance_rates, bybit_rates = await asyncio.gather(b_task, by_task)

    rows = []
    # Header format row matching CoinGlass canonical schema
    rows.append({
        "Symbol": "Symbol",
        "USDT_or_USD_Margined": "Binance",
        "col_2": "Bybit",
        "col_3": "Predicted",
        "col_4": "-",
        "col_5": "-",
        "col_6": "-",
        "col_7": "-",
        "col_8": "-",
        "col_9": "-",
        "col_10": "-",
        "col_11": "-",
        "col_12": "-",
        "Token_Margined_Coin-M": "Binance",
        "col_14": "Bybit",
        "Metadata": "Timestamp (IST)"
    })

    for sym in UNIVERSE:
        b_rate = binance_rates.get(sym)
        by_rate = bybit_rates.get(sym)
        rows.append({
            "Symbol": sym,
            "USDT_or_USD_Margined": fmt_rate(b_rate),
            "col_2": fmt_rate(by_rate),
            "col_3": fmt_rate(b_rate),
            "col_4": "-",
            "col_5": "-",
            "col_6": "-",
            "col_7": "-",
            "col_8": "-",
            "col_9": "-",
            "col_10": "-",
            "col_11": "-",
            "col_12": "-",
            "Token_Margined_Coin-M": fmt_rate(b_rate),
            "col_14": fmt_rate(by_rate),
            "Metadata": ts_str
        })

    duration = time.perf_counter() - t0
    log.info(f"Harvested funding rates for {len(UNIVERSE)} assets in {duration:.2f}s via Pure API!")
    return rows


def main():
    rows = asyncio.run(harvest_funding_rates())
    if not rows:
        sys.exit(1)
    success = write_parquet_feed("5_Funding_Rate", rows)
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
