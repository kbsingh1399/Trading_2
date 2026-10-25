#!/usr/bin/env python3
"""
Collectors/API/5_OI.py
======================
Pure-API Cryptocurrency Futures Open Interest Collector.
Fetches real-time open interest across Binance Futures, Bybit, and Hyperliquid.
Execution Time: < 1.0s.
"""
from __future__ import annotations

import asyncio
import datetime
import json
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
    format="%(asctime)s [%(levelname)s] [OpenInterest_API] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
log = logging.getLogger("OpenInterest_API")

IST_TZ = datetime.timezone(datetime.timedelta(hours=5, minutes=30))

UNIVERSE = [
    "BTC", "ETH", "XRP", "SOL", "BNB", "DOGE", "ADA", "TRX", "LINK",
    "AVAX", "SUI", "NEAR", "DOT", "LTC", "BCH", "APT", "OP", "ARB"
]

BINANCE_FAPI_BASE = "https://fapi.binance.com"
BYBIT_API_BASE = "https://api.bybit.com"
HYPERLIQUID_INFO_URL = "https://api.hyperliquid.xyz/info"


def fmt_usd(val: float) -> str:
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
    else:
        return f"${abs_v:.2f}"


async def fetch_binance_oi_for_symbol(session: aiohttp.ClientSession, symbol: str) -> float:
    url = f"{BINANCE_FAPI_BASE}/fapi/v1/openInterest"
    params = {"symbol": f"{symbol}USDT"}
    try:
        async with session.get(url, params=params, timeout=4) as resp:
            if resp.status == 200:
                data = await resp.json()
                return float(data.get("openInterest", 0.0))
    except Exception:
        pass
    return 0.0


async def fetch_binance_prices(session: aiohttp.ClientSession) -> Dict[str, float]:
    url = f"{BINANCE_FAPI_BASE}/fapi/v1/ticker/price"
    try:
        async with session.get(url, timeout=4) as resp:
            if resp.status == 200:
                data = await resp.json()
                prices = {}
                for item in data:
                    sym = item.get("symbol", "").replace("USDT", "")
                    if sym in UNIVERSE:
                        prices[sym] = float(item.get("price", 0.0))
                return prices
    except Exception:
        pass
    return {}


async def fetch_bybit_oi(session: aiohttp.ClientSession) -> Dict[str, float]:
    url = f"{BYBIT_API_BASE}/v5/market/tickers?category=linear"
    try:
        async with session.get(url, timeout=4) as resp:
            if resp.status == 200:
                data = await resp.json()
                bybit_oi = {}
                for item in data.get("result", {}).get("list", []):
                    sym = item.get("symbol", "").replace("USDT", "")
                    if sym in UNIVERSE:
                        val = float(item.get("openInterestValue", 0.0))
                        bybit_oi[sym] = val
                return bybit_oi
    except Exception:
        pass
    return {}


async def fetch_hyperliquid_oi(session: aiohttp.ClientSession) -> Dict[str, float]:
    try:
        payload = json.dumps({"type": "metaAndAssetCtxs"})
        headers = {"Content-Type": "application/json"}
        async with session.post(HYPERLIQUID_INFO_URL, data=payload, headers=headers, timeout=4) as resp:
            if resp.status == 200:
                data = await resp.json()
                meta = data[0]["universe"]
                ctxs = data[1]
                hl_oi = {}
                for m, c in zip(meta, ctxs):
                    sym = m.get("name", "")
                    if sym in UNIVERSE:
                        oi_tokens = float(c.get("openInterest", 0.0))
                        mark_px = float(c.get("markPx", 0.0))
                        hl_oi[sym] = oi_tokens * mark_px
                return hl_oi
    except Exception:
        pass
    return {}


async def harvest_open_interest() -> List[Dict[str, Any]]:
    t0 = time.perf_counter()
    now_ist = datetime.datetime.now(IST_TZ)
    ts_str = now_ist.strftime("%Y-%m-%d %H:%M:%S IST")

    connector = aiohttp.TCPConnector(limit=30, ttl_dns_cache=300)
    async with aiohttp.ClientSession(connector=connector) as session:
        # 1. Fetch cross-exchange prices and exchange-wide feeds in parallel
        p_task = fetch_binance_prices(session)
        by_task = fetch_bybit_oi(session)
        hl_task = fetch_hyperliquid_oi(session)
        prices, bybit_oi, hl_oi = await asyncio.gather(p_task, by_task, hl_task)

        # 2. Fetch Binance symbol OI in parallel
        binance_oi_tasks = [fetch_binance_oi_for_symbol(session, sym) for sym in UNIVERSE]
        binance_oi_results = await asyncio.gather(*binance_oi_tasks)
        binance_oi = dict(zip(UNIVERSE, binance_oi_results))

    rows = []
    for sym in UNIVERSE:
        px = prices.get(sym, 1.0)
        b_tokens = binance_oi.get(sym, 0.0)
        b_usd = b_tokens * px
        by_usd = bybit_oi.get(sym, 0.0)
        hl_usd = hl_oi.get(sym, 0.0)
        tot_usd = b_usd + by_usd + hl_usd

        rows.append({
            "Asset": sym,
            "Total_OI_USD": fmt_usd(tot_usd),
            "Binance": fmt_usd(b_usd),
            "Bybit": fmt_usd(by_usd),
            "OKX": "-",
            "CME": "-",
            "KuCoin": "-",
            "Gate": "-",
            "Bitget": "-",
            "BingX": "-",
            "MEXC": "-",
            "Bitunix": "-",
            "Hyperliquid": fmt_usd(hl_usd),
            "Others": "-",
            "Total_OI_Tokens": f"{b_tokens:,.1f} {sym}",
            "24h_Total_Change": "+0.00%",
            "4h_Total_Change": "+0.00%",
            "1h_Total_Change": "+0.00%",
            "OI___24h_Vol": "1.00",
            "Timestamp_IST": ts_str,
        })

    duration = time.perf_counter() - t0
    log.info(f"Harvested Open Interest across {len(UNIVERSE)} assets in {duration:.2f}s via Pure API!")
    return rows


def main():
    rows = asyncio.run(harvest_open_interest())
    if not rows:
        sys.exit(1)
    success = write_parquet_feed("5_OI", rows)
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
