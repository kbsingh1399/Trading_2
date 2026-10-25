#!/usr/bin/env python3
"""
Data/Excel_Modules/18_CVD.py
============================
Multi-Asset Multi-Timeframe Continuous Cumulative Volume Delta (CVD) Engine.
Captures institutional 30-day continuous candle CVD data across all core asset classes:
  1. CRYPTO: 18 Institutional Binance USDT-M Perpetuals
     (BTC, ETH, XRP, SOL, BNB, DOGE, ADA, TRX, LINK, AVAX, SUI, NEAR, DOT, LTC, BCH, APT, OP, ARB)
  2. METALS: Gold (PAXG / XAUUSD.pi / xyz:GOLD), Silver (XAGUSD.pi / xyz:SILVER)
  3. INDICES: S&P 500 (SP500.p / xyz:SP500), Nasdaq 100 (NAS100.p), Russell 2000 (US2000.p)
  4. FOREX: EUR/USD (EURUSD.pi), GBP/USD (GBPUSD.pi), USD/JPY (USDJPY.pi), AUD/USD (AUDUSD.pi)
  5. COMMODITIES: Crude Oil WTI (USWTI.p / xyz:CL)

Timeframes:
  - 5m  (5-Minute Microstructure Tape)
  - 15m (15-Minute Tactical Execution)
  - 1h  (1-Hour Institutional Session Trend)
  - 4h  (4-Hour Macro Swing Structure)

Calculations:
  - Taker Buy vs Taker Sell Volume (USD & Base Units)
  - Net Candle Delta (Quote USD & Base Units)
  - Delta % of Candle Volume
  - Continuous 30-Day Cumulative Volume Delta (CVD)
  - 20-Period Rolling CVD Z-Score
  - Microstructure Regime Classification:
      * BULLISH ABSORPTION (Price < Open, Delta > 0)
      * BEARISH ABSORPTION (Price > Open, Delta < 0)
      * AGGRESSIVE BUYING (Price > Open, Delta > 0, Delta % > +15%)
      * AGGRESSIVE SELLING (Price < Open, Delta < 0, Delta % < -15%)
      * DELTA ALIGNED
      * NEUTRAL CHOP

Outputs:
  - Excel Worksheet: '18_CVD' positioned at Index 26 in Data/DataBase_Trading.xlsx
  - High-Speed Parquet Datasets: Data/CVD/18_CVD_30D_ALL.parquet for instant ML/quant query
"""

from __future__ import annotations

try:
    import excel_lock_hook
except Exception:
    pass

import argparse
import asyncio
import datetime
import json
import logging
import math
import os
import pathlib
import sys
import time
import urllib.request
import zipfile
from typing import Any, Dict, List, Optional, Tuple

import aiohttp
import numpy as np
import pandas as pd

try:
    import openpyxl
    from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
    from openpyxl.utils import get_column_letter
except ImportError:
    openpyxl = None

try:
    import MetaTrader5 as mt5
except ImportError:
    mt5 = None

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] [%(name)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
log = logging.getLogger("18_CVD")

MODULES_DIR = pathlib.Path(__file__).resolve().parent
ROOT_DIR = MODULES_DIR.parents[1]
CORE_DIR = ROOT_DIR / "Collectors" / "Core"
DF_DIR = ROOT_DIR / "Terminal" / "Data_Factory"
if str(CORE_DIR) not in sys.path:
    sys.path.insert(0, str(CORE_DIR))
if str(DF_DIR) not in sys.path:
    sys.path.insert(0, str(DF_DIR))

try:
    from parquet_writer import write_parquet_feed
except Exception:
    write_parquet_feed = None

DEFAULT_EXCEL_PATH = ROOT_DIR / "Data" / "DataBase_Trading.xlsx"
DEFAULT_PARQUET_DIR = ROOT_DIR / "Data" / "CVD"
BINANCE_FAPI_URL = "https://fapi.binance.com/fapi/v1/klines"
HL_INFO_URL = "https://api.hyperliquid.xyz/info"
SHEET_NAME = "18_CVD"

# Core Asset Roster across All 5 Asset Classes
DEFAULT_ASSET_ROSTER = [
    # (Category, Display Symbol, Binance Symbol, MT5 Symbol, Hyperliquid Symbol)
    # 1. CRYPTO
    ("CRYPTO", "BTC", "BTCUSDT", "BTCUSD.pi", "BTC"),
    ("CRYPTO", "ETH", "ETHUSDT", "ETHUSD.pi", "ETH"),
    ("CRYPTO", "SOL", "SOLUSDT", "SOLUSD.p", "SOL"),
    ("CRYPTO", "BNB", "BNBUSDT", "BNBUSD.p", "BNB"),
    ("CRYPTO", "XRP", "XRPUSDT", "XRPUSD.pi", "XRP"),
    ("CRYPTO", "DOGE", "DOGEUSDT", "DOGUSD.p", "DOGE"),
    ("CRYPTO", "ADA", "ADAUSDT", "ADAUSD.p", "ADA"),
    ("CRYPTO", "TRX", "TRXUSDT", "TRXUSD.p", "TRX"),
    ("CRYPTO", "LINK", "LINKUSDT", "LNKUSD.p", "LINK"),
    ("CRYPTO", "AVAX", "AVAXUSDT", "AVXUSD.p", "AVAX"),
    ("CRYPTO", "SUI", "SUIUSDT", None, "SUI"),
    ("CRYPTO", "NEAR", "NEARUSDT", "NERUSD.p", "NEAR"),
    ("CRYPTO", "DOT", "DOTUSDT", "DOTUSD.pi", "DOT"),
    ("CRYPTO", "LTC", "LTCUSDT", "LTCUSD.pi", "LTC"),
    ("CRYPTO", "BCH", "BCHUSDT", "BCHUSD.p", "BCH"),
    ("CRYPTO", "APT", "APTUSDT", None, "APT"),
    ("CRYPTO", "OP", "OPUSDT", None, "OP"),
    ("CRYPTO", "ARB", "ARBUSDT", None, "ARB"),
    # 2. METALS
    ("METALS", "GOLD", "PAXGUSDT", "XAUUSD.pi", "xyz:GOLD"),
    ("METALS", "SILVER", None, "XAGUSD.pi", "xyz:SILVER"),
    # 3. INDICES
    ("INDICES", "SP500", None, "SP500.p", "xyz:SP500"),
    ("INDICES", "NAS100", None, "NAS100.p", "xyz:QQQ"),
    ("INDICES", "US2000", None, "US2000.p", None),
    # 4. FOREX
    ("FOREX", "EURUSD", None, "EURUSD.pi", "xyz:EUR"),
    ("FOREX", "GBPUSD", None, "GBPUSD.pi", "xyz:GBP"),
    ("FOREX", "USDJPY", None, "USDJPY.pi", "xyz:JPY"),
    ("FOREX", "AUDUSD", None, "AUDUSD.pi", None),
    # 5. COMMODITIES
    ("COMMODITIES", "WTI_OIL", None, "USWTI.p", "xyz:CL"),
]

TIMEFRAMES_DEFAULT = ["4h", "1h", "15m", "5m"]


# =====================================================================
# 1. BINANCE FUTURES KLINE HARVESTER (ASYNC & CONCURRENT)
# =====================================================================
async def fetch_binance_klines_series(
    session: aiohttp.ClientSession,
    sem: asyncio.Semaphore,
    symbol: str,
    interval: str,
    start_ms: int,
    now_ms: int,
) -> List[Dict[str, Any]]:
    """Fetches continuous klines for a Binance symbol over the 30-day window."""
    all_bars = []
    curr_start = start_ms
    max_retries = 3

    async with sem:
        while curr_start < now_ms:
            params = {
                "symbol": symbol,
                "interval": interval,
                "startTime": curr_start,
                "limit": 1500,
            }
            success = False
            for attempt in range(max_retries):
                try:
                    async with session.get(BINANCE_FAPI_URL, params=params, timeout=12) as resp:
                        if resp.status == 429:
                            log.warning(f"Binance 429 rate limit hit for {symbol} {interval}. Backing off 2s...")
                            await asyncio.sleep(2.0)
                            continue
                        if resp.status != 200:
                            log.warning(f"Binance HTTP {resp.status} for {symbol} {interval}")
                            break
                        data = await resp.json()
                        if not data or not isinstance(data, list):
                            break
                        all_bars.extend(data)
                        if len(data) < 1500:
                            success = True
                            break
                        # Next page starts after last bar's close time
                        curr_start = data[-1][6] + 1
                        success = True
                        break
                except Exception as exc:
                    if attempt == max_retries - 1:
                        log.debug(f"Failed fetching {symbol} {interval} page: {exc}")
                    await asyncio.sleep(0.5)

            if not success or (len(all_bars) > 0 and len(data) < 1500):
                break

    # Parse and normalize kline records
    records = []
    for bar in all_bars:
        try:
            open_ms = int(bar[0])
            open_p = float(bar[1])
            high_p = float(bar[2])
            low_p = float(bar[3])
            close_p = float(bar[4])
            vol_base = float(bar[5])
            close_ms = int(bar[6])
            vol_quote = float(bar[7])
            trades_cnt = int(bar[8])
            buy_base = float(bar[9])
            buy_quote = float(bar[10])

            sell_quote = max(0.0, vol_quote - buy_quote)
            candle_delta_usd = buy_quote - sell_quote
            candle_delta_base = 2.0 * buy_base - vol_base
            delta_pct = (candle_delta_usd / vol_quote * 100.0) if vol_quote > 0 else 0.0

            records.append({
                "timestamp_ms": open_ms,
                "open": open_p,
                "high": high_p,
                "low": low_p,
                "close": close_p,
                "total_volume": vol_base,
                "quote_volume_usd": vol_quote,
                "taker_buy_vol": buy_quote,
                "taker_sell_vol": sell_quote,
                "candle_delta": candle_delta_usd,
                "candle_delta_base": candle_delta_base,
                "delta_pct": delta_pct,
                "trades_count": trades_cnt,
                "source": "Binance Futures",
            })
        except Exception:
            continue

    return records


# =====================================================================
# 2. METATRADER 5 HARVESTER (FOREX, METALS, INDICES, COMMODITIES)
# =====================================================================
MT5_TIMEFRAME_MAP = {
    "5m": 5,    # mt5.TIMEFRAME_M5
    "15m": 15,  # mt5.TIMEFRAME_M15
    "1h": 16385,# mt5.TIMEFRAME_H1
    "4h": 16388,# mt5.TIMEFRAME_H4
}


def fetch_mt5_series(
    mt5_symbol: str,
    interval: str,
    utc_from: datetime.datetime,
    utc_to: datetime.datetime,
) -> List[Dict[str, Any]]:
    """Fetches continuous rates from MT5 and applies Lee-Ready Tick Delta Volume Split."""
    if not mt5 or not mt5.initialize():
        return []

    tf_const = MT5_TIMEFRAME_MAP.get(interval)
    if tf_const is None:
        return []

    try:
        rates = mt5.copy_rates_range(mt5_symbol, tf_const, utc_from, utc_to)
    except Exception as exc:
        log.debug(f"MT5 copy_rates_range failed for {mt5_symbol} {interval}: {exc}")
        return []

    if rates is None or len(rates) == 0:
        return []

    records = []
    for r in rates:
        try:
            open_ms = int(r["time"]) * 1000
            open_p = float(r["open"])
            high_p = float(r["high"])
            low_p = float(r["low"])
            close_p = float(r["close"])
            tick_vol = float(r["tick_volume"])
            real_vol = float(r["real_volume"])
            vol = real_vol if real_vol > 0 else tick_vol

            # Estimate USD Quote Turnover
            quote_vol_usd = vol * close_p

            # Quantitative Tick Delta / Imbalance Model (Lee-Ready Volume Split)
            hl = high_p - low_p
            if hl > 1e-8:
                # Fractional buyer pressure determined by intra-bar close location
                buy_fraction = ((close_p - low_p) + 0.5 * (close_p - open_p + hl)) / (2.0 * hl)
                buy_fraction = max(0.05, min(0.95, buy_fraction))
                buy_vol = quote_vol_usd * buy_fraction
                sell_vol = quote_vol_usd * (1.0 - buy_fraction)
            else:
                buy_vol = quote_vol_usd * 0.5
                sell_vol = quote_vol_usd * 0.5

            candle_delta_usd = buy_vol - sell_vol
            delta_pct = (candle_delta_usd / quote_vol_usd * 100.0) if quote_vol_usd > 0 else 0.0

            records.append({
                "timestamp_ms": open_ms,
                "open": open_p,
                "high": high_p,
                "low": low_p,
                "close": close_p,
                "total_volume": vol,
                "quote_volume_usd": quote_vol_usd,
                "taker_buy_vol": buy_vol,
                "taker_sell_vol": sell_vol,
                "candle_delta": candle_delta_usd,
                "candle_delta_base": (candle_delta_usd / close_p) if close_p > 0 else 0.0,
                "delta_pct": delta_pct,
                "trades_count": int(tick_vol),
                "source": "MT5 Interbank",
            })
        except Exception:
            continue

    return records


# =====================================================================
# 3. HYPERLIQUID ON-CHAIN FALLBACK HARVESTER
# =====================================================================
async def fetch_hyperliquid_series(
    session: aiohttp.ClientSession,
    coin: str,
    interval: str,
    start_ms: int,
) -> List[Dict[str, Any]]:
    """Fetches continuous candle snapshot from Hyperliquid API."""
    body = {"type": "candleSnapshot", "req": {"coin": coin, "interval": interval, "startTime": start_ms}}
    try:
        async with session.post(HL_INFO_URL, json=body, timeout=10) as resp:
            if resp.status != 200:
                return []
            data = await resp.json()
            if not data or not isinstance(data, list):
                return []
    except Exception:
        return []

    records = []
    for bar in data:
        try:
            open_ms = int(bar["t"])
            open_p = float(bar["o"])
            high_p = float(bar["h"])
            low_p = float(bar["l"])
            close_p = float(bar["c"])
            vol_coin = float(bar["v"])
            trades_cnt = int(bar.get("n", 0))

            quote_vol_usd = vol_coin * close_p
            hl = high_p - low_p
            if hl > 1e-8:
                buy_fraction = ((close_p - low_p) + 0.5 * (close_p - open_p + hl)) / (2.0 * hl)
                buy_fraction = max(0.05, min(0.95, buy_fraction))
                buy_vol = quote_vol_usd * buy_fraction
                sell_vol = quote_vol_usd * (1.0 - buy_fraction)
            else:
                buy_vol = quote_vol_usd * 0.5
                sell_vol = quote_vol_usd * 0.5

            candle_delta_usd = buy_vol - sell_vol
            delta_pct = (candle_delta_usd / quote_vol_usd * 100.0) if quote_vol_usd > 0 else 0.0

            records.append({
                "timestamp_ms": open_ms,
                "open": open_p,
                "high": high_p,
                "low": low_p,
                "close": close_p,
                "total_volume": vol_coin,
                "quote_volume_usd": quote_vol_usd,
                "taker_buy_vol": buy_vol,
                "taker_sell_vol": sell_vol,
                "candle_delta": candle_delta_usd,
                "candle_delta_base": vol_coin * (buy_fraction - (1.0 - buy_fraction)),
                "delta_pct": delta_pct,
                "trades_count": trades_cnt,
                "source": "Hyperliquid",
            })
        except Exception:
            continue

    return records


# =====================================================================
# 4. QUANTITATIVE VECTORIZED METRICS & REGIME CLASSIFICATION
# =====================================================================
def enrich_series_with_quant_metrics(
    records: List[Dict[str, Any]],
    category: str,
    symbol: str,
    pair: str,
    timeframe: str,
) -> List[Dict[str, Any]]:
    """Calculates continuous Cumulative Volume Delta (CVD), rolling Z-scores, and divergence regimes."""
    if not records:
        return []

    # Sort strictly chronologically ascending (oldest -> newest) for running cumulative math
    records.sort(key=lambda x: x["timestamp_ms"])

    deltas = np.array([r["candle_delta"] for r in records], dtype=float)
    cvd_array = np.cumsum(deltas)

    deltas_base = np.array([r.get("candle_delta_base", 0.0) for r in records], dtype=float)
    cvd_base_array = np.cumsum(deltas_base)

    # 20-period rolling z-score of candle delta
    window = 20
    zscores = np.zeros(len(records), dtype=float)
    for i in range(len(records)):
        start_idx = max(0, i - window + 1)
        sub = deltas[start_idx : i + 1]
        std = np.std(sub)
        mean = np.mean(sub)
        zscores[i] = (deltas[i] - mean) / (std if std > 1e-8 else 1.0)

    enriched = []
    for i, r in enumerate(records):
        ist_tz = datetime.timezone(datetime.timedelta(hours=5, minutes=30))
        ts_utc = datetime.datetime.fromtimestamp(
            r["timestamp_ms"] / 1000.0, tz=datetime.timezone.utc
        ).strftime("%Y-%m-%d %H:%M:%S")
        ts_ist = datetime.datetime.fromtimestamp(
            r["timestamp_ms"] / 1000.0, tz=ist_tz
        ).strftime("%Y-%m-%d %H:%M:%S IST")

        open_p = r["open"]
        close_p = r["close"]
        delta_usd = r["candle_delta"]
        delta_base = r.get("candle_delta_base", 0.0)
        delta_pct = r["delta_pct"]
        cvd_val = float(cvd_array[i])
        cvd_base_val = float(cvd_base_array[i])
        zscore_val = float(zscores[i])

        price_return_pct = ((close_p - open_p) / open_p * 100.0) if open_p > 0 else 0.0

        # Microstructure Regime & Absorption Divergence
        if close_p < open_p and delta_usd > 0:
            regime = "BULLISH ABSORPTION"
        elif close_p > open_p and delta_usd < 0:
            regime = "BEARISH ABSORPTION"
        elif close_p > open_p and delta_pct > 15.0:
            regime = "AGGRESSIVE BUYING"
        elif close_p < open_p and delta_pct < -15.0:
            regime = "AGGRESSIVE SELLING"
        elif abs(delta_pct) < 5.0:
            regime = "NEUTRAL CHOP"
        else:
            regime = "DELTA ALIGNED"

        enriched.append({
            "timestamp_ist": ts_ist,
            "timestamp_utc": ts_utc,
            "timestamp_ms": r["timestamp_ms"],
            "category": category,
            "symbol": symbol,
            "market_pair": pair,
            "source": r["source"],
            "timeframe": timeframe,
            "open": open_p,
            "high": r["high"],
            "low": r["low"],
            "close": close_p,
            "total_volume": r["total_volume"],
            "quote_volume_usd": r["quote_volume_usd"],
            "taker_buy_vol": r["taker_buy_vol"],
            "taker_sell_vol": r["taker_sell_vol"],
            "candle_delta": delta_usd,
            "candle_delta_base": delta_base,
            "delta_pct": delta_pct,
            "cumulative_cvd": cvd_val,
            "cumulative_cvd_base": cvd_base_val,
            "cvd_zscore": zscore_val,
            "price_return_pct": price_return_pct,
            "regime": regime,
            "trades_count": r["trades_count"],
        })

    return enriched


# =====================================================================
# 5. MASTER MULTI-ASSET HARVESTING ORCHESTRATOR
# =====================================================================
async def harvest_all_assets_cvd(
    roster: List[Tuple[str, str, Optional[str], Optional[str], Optional[str]]],
    timeframes: List[str] = TIMEFRAMES_DEFAULT,
    days: int = 30,
) -> List[Dict[str, Any]]:
    """Harvests continuous 30-day CVD data across Crypto, Metals, Indices, Forex, and Commodities."""
    now_ms = int(time.time() * 1000)
    start_ms = now_ms - (days * 24 * 3600 * 1000)
    utc_now = datetime.datetime.now(datetime.timezone.utc)
    utc_from = utc_now - datetime.timedelta(days=days)

    log.info(
        f"Starting institutional CVD harvest across {len(roster)} assets and {len(timeframes)} timeframes over last {days} days..."
    )

    all_enriched_rows: List[Dict[str, Any]] = []
    sem = asyncio.Semaphore(12)

    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Institutional-CVD-Engine/2.0"}
    async with aiohttp.ClientSession(headers=headers) as session:
        # 1. Dispatch Binance Crypto & Gold Tasks
        binance_tasks = []
        for cat, sym, binance_sym, mt5_sym, hl_sym in roster:
            if binance_sym:
                for tf in timeframes:
                    t = fetch_binance_klines_series(session, sem, binance_sym, tf, start_ms, now_ms)
                    binance_tasks.append((cat, sym, binance_sym, tf, t))

        log.info(f"Dispatched {len(binance_tasks)} parallel Binance kline fetchers...")
        binance_results = await asyncio.gather(*[item[4] for item in binance_tasks])

        for (cat, sym, binance_sym, tf, _), records in zip(binance_tasks, binance_results):
            if records:
                enriched = enrich_series_with_quant_metrics(records, cat, sym, binance_sym, tf)
                all_enriched_rows.extend(enriched)
                log.info(f"[PASS] Binance {sym} ({binance_sym}) [{tf}]: {len(enriched)} continuous bars")

        # 2. Harvest MT5 Rates for Forex, Metals, Indices, Commodities
        mt5_count = 0
        for cat, sym, binance_sym, mt5_sym, hl_sym in roster:
            if mt5_sym:
                # If already fetched via Binance (like PAXG for GOLD), keep Binance as primary crypto/tokenized,
                # but MT5 provides interbank spot Gold XAUUSD, Silver XAGUSD, SP500, FX, etc.
                if cat in ("METALS", "INDICES", "FOREX", "COMMODITIES") and (not binance_sym or sym != "GOLD"):
                    for tf in timeframes:
                        records = fetch_mt5_series(mt5_sym, tf, utc_from, utc_now)
                        if records:
                            enriched = enrich_series_with_quant_metrics(records, cat, sym, mt5_sym, tf)
                            all_enriched_rows.extend(enriched)
                            mt5_count += len(enriched)
                            log.info(f"[PASS] MT5 Interbank {sym} ({mt5_sym}) [{tf}]: {len(enriched)} bars")
                        elif hl_sym:
                            # Fallback to Hyperliquid if MT5 rates were empty
                            hl_records = await fetch_hyperliquid_series(session, hl_sym, tf, start_ms)
                            if hl_records:
                                enriched = enrich_series_with_quant_metrics(hl_records, cat, sym, hl_sym, tf)
                                all_enriched_rows.extend(enriched)
                                log.info(f"[PASS-FALLBACK] Hyperliquid {sym} ({hl_sym}) [{tf}]: {len(enriched)} bars")

    # Shutdown MT5 cleanly if it was used
    if mt5:
        try:
            mt5.shutdown()
        except Exception:
            pass

    log.info(f"Harvest complete. Total continuous CVD candle rows collected: {len(all_enriched_rows):,}")
    return all_enriched_rows


# =====================================================================
# 6. EXCEL WORKSHEET GENERATOR & STYLER
# =====================================================================
def export_cvd_to_excel(
    rows: List[Dict[str, Any]],
    excel_path: pathlib.Path = DEFAULT_EXCEL_PATH,
    sheet_name: str = SHEET_NAME,
    max_excel_rows: int = 1500,
) -> int:
    """Writes CVD dataset into Data/DataBase_Trading.xlsx at Index 26 with institutional formatting."""
    if openpyxl is None:
        log.error("openpyxl is not installed. Skipping Excel export.")
        return 0

    if not excel_path.exists():
        log.error(f"Excel workbook not found at {excel_path}")
        return 0

    # Multi-Horizon Ring Buffer for Excel display:
    # Ensure all timeframes (5m, 15m, 1h, 4h) across all symbols are preserved
    # so that high-timeframe diagnostics survive compression while keeping total rows <= max_excel_rows.
    tf_order = {"5m": 1, "15m": 2, "1h": 3, "4h": 4}
    if max_excel_rows > 0 and len(rows) > max_excel_rows:
        grouped = {}
        for r in rows:
            key = (r["symbol"], r["timeframe"])
            if key not in grouped:
                grouped[key] = []
            grouped[key].append(r)

        for key in grouped:
            grouped[key].sort(key=lambda x: -x["timestamp_ms"])

        num_pairs = len(grouped)
        quota = max(15, max_excel_rows // max(1, num_pairs))
        balanced_rows = []
        for key, items in grouped.items():
            balanced_rows.extend(items[:quota])

        balanced_rows.sort(
            key=lambda x: (
                -x["timestamp_ms"],
                x["category"],
                x["symbol"],
                tf_order.get(x["timeframe"], 99),
            )
        )
        display_rows = balanced_rows[:max_excel_rows]
    else:
        rows.sort(
            key=lambda x: (
                -x["timestamp_ms"],
                x["category"],
                x["symbol"],
                tf_order.get(x["timeframe"], 99),
            )
        )
        display_rows = rows

    log.info(f"Opening workbook {excel_path.name} to write sheet '{sheet_name}'...")
    try:
        from filelock import FileLock
        lock = FileLock(str(excel_path) + ".lock", timeout=120)
    except ImportError:
        lock = None

    class _NoLock:
        def __enter__(self): return self
        def __exit__(self, *args): pass

    with (lock if lock else _NoLock()):
        wb = openpyxl.load_workbook(excel_path)

    # Position at Index 26 (immediately after 17_Orderbook at Index 25)
    if sheet_name in wb.sheetnames:
        idx = wb.sheetnames.index(sheet_name)
        wb.remove(wb[sheet_name])
        ws = wb.create_sheet(title=sheet_name, index=idx)
    else:
        if "17_Orderbook" in wb.sheetnames:
            target_idx = wb.sheetnames.index("17_Orderbook") + 1
        elif "16_Hyperdash_telegram_Intel" in wb.sheetnames:
            target_idx = wb.sheetnames.index("16_Hyperdash_telegram_Intel") + 2
        else:
            target_idx = 26 if len(wb.sheetnames) >= 26 else len(wb.sheetnames)
        ws = wb.create_sheet(title=sheet_name, index=target_idx)

    final_idx = wb.sheetnames.index(sheet_name)
    log.info(f"Target worksheet '{sheet_name}' positioned at index {final_idx}")

    # Typography & Colors
    hdr_font = Font(name="Segoe UI", size=10, bold=True, color="FFFFFF")
    hdr_fill = PatternFill(start_color="0F172A", end_color="0F172A", fill_type="solid")

    base_font = Font(name="Segoe UI", size=9, color="000000")
    bold_font = Font(name="Segoe UI", size=9, bold=True, color="000000")
    mono_font = Font(name="Consolas", size=9, color="334155")
    green_font = Font(name="Segoe UI", size=9, bold=True, color="00A86B")
    red_font = Font(name="Segoe UI", size=9, bold=True, color="E53935")

    fill_pos_delta = PatternFill(start_color="DCFCE7", end_color="DCFCE7", fill_type="solid")
    fill_neg_delta = PatternFill(start_color="FEE2E2", end_color="FEE2E2", fill_type="solid")
    fill_bull_absorp = PatternFill(start_color="D1FAE5", end_color="D1FAE5", fill_type="solid")
    fill_bear_absorp = PatternFill(start_color="FFE4E6", end_color="FFE4E6", fill_type="solid")
    fill_agg_buy = PatternFill(start_color="E0F2FE", end_color="E0F2FE", fill_type="solid")
    fill_agg_sell = PatternFill(start_color="FEF3C7", end_color="FEF3C7", fill_type="solid")

    # Category Badges Font & Fill
    badge_colors = {
        "CRYPTO": ("0284C7", "E0F2FE"),
        "INDICES": ("1E293B", "F1F5F9"),
        "METALS": ("B45309", "FEF3C7"),
        "COMMODITIES": ("3F6212", "ECFCCB"),
        "FOREX": ("047857", "ECFDF5"),
    }

    thin_border_side = Side(border_style="thin", color="E2E8F0")
    row_border = Border(
        left=thin_border_side,
        right=thin_border_side,
        top=thin_border_side,
        bottom=thin_border_side,
    )

    headers = [
        "Timestamp (IST)",
        "Asset Class",
        "Symbol",
        "Market Pair",
        "Data Source",
        "Timeframe",
        "Open Price",
        "High Price",
        "Low Price",
        "Close Price",
        "Total Volume",
        "Quote Volume (USD)",
        "Taker Buy Volume",
        "Taker Sell Volume",
        "Candle Delta (USD)",
        "Candle Delta (Coins)",
        "Delta % of Vol",
        "Cumulative CVD (USD)",
        "Cumulative CVD (Coins)",
        "CVD Z-Score (20)",
        "Price Return %",
        "Orderflow Regime",
        "Trades / Ticks",
    ]

    ws.row_dimensions[1].height = 26
    ws.append(headers)

    for col_idx in range(1, len(headers) + 1):
        cell = ws.cell(row=1, column=col_idx)
        cell.font = hdr_font
        cell.fill = hdr_fill
        cell.alignment = Alignment(horizontal="center", vertical="center", wrap_text=False)

    # Direct Atomic Parquet Feed Export
    if write_parquet_feed is not None and display_rows:
        try:
            feed_rows = []
            for r in display_rows:
                feed_rows.append({
                    "Timestamp_IST": r.get("timestamp_ist", r.get("timestamp_utc", "")),
                    "Asset_Class": r.get("category", ""),
                    "Symbol": r.get("symbol", ""),
                    "Market_Pair": r.get("market_pair", ""),
                    "Data_Source": r.get("source", ""),
                    "Timeframe": r.get("timeframe", ""),
                    "Open_Price": r.get("open", 0.0),
                    "High_Price": r.get("high", 0.0),
                    "Low_Price": r.get("low", 0.0),
                    "Close_Price": r.get("close", 0.0),
                    "Total_Volume": r.get("total_volume", 0.0),
                    "Quote_Volume_USD": r.get("quote_volume_usd", 0.0),
                    "Taker_Buy_Volume": r.get("taker_buy_vol", 0.0),
                    "Taker_Sell_Volume": r.get("taker_sell_vol", 0.0),
                    "Candle_Delta_USD": r.get("candle_delta", 0.0),
                    "Candle_Delta_Coins": r.get("candle_delta_base", 0.0),
                    "Delta_%_of_Vol": r.get("delta_pct", 0.0) / 100.0,
                    "Cumulative_CVD_USD": r.get("cumulative_cvd", 0.0),
                    "Cumulative_CVD_Coins": r.get("cumulative_cvd_base", 0.0),
                    "CVD_Z-Score_20": r.get("cvd_zscore", 0.0),
                    "Price_Return_%": r.get("price_return_pct", 0.0) / 100.0,
                    "Orderflow_Regime": r.get("regime", ""),
                    "Trades___Ticks": r.get("trades_count", 0),
                })
            write_parquet_feed("18_CVD", feed_rows)
            log.info(f"[PASS] Directly dumped {len(feed_rows)} rows to Data/feeds/18_CVD.parquet!")
        except Exception as exc:
            log.warning(f"Direct parquet write warning: {exc}")

    log.info(f"Writing {len(display_rows):,} rows to worksheet '{sheet_name}'...")
    t0 = time.time()

    for r in display_rows:
        ws.append([
            r.get("timestamp_ist", r["timestamp_utc"]),
            r["category"],
            r["symbol"],
            r["market_pair"],
            r["source"],
            r["timeframe"],
            r["open"],
            r["high"],
            r["low"],
            r["close"],
            r["total_volume"],
            r["quote_volume_usd"],
            r["taker_buy_vol"],
            r["taker_sell_vol"],
            r["candle_delta"],
            r["candle_delta_base"],
            r["delta_pct"] / 100.0,
            r["cumulative_cvd"],
            r["cumulative_cvd_base"],
            r["cvd_zscore"],
            r["price_return_pct"] / 100.0,
            r["regime"],
            r["trades_count"],
        ])

    log.info(f"Data rows appended in {time.time() - t0:.2f}s. Formatting styling and semantic cells...")

    # Format numeric cells and apply semantic highlights
    for row_idx in range(2, len(display_rows) + 2):
        ws.row_dimensions[row_idx].height = 19

        # Alignment
        ws.cell(row=row_idx, column=1).alignment = Alignment(horizontal="center", vertical="center")
        ws.cell(row=row_idx, column=2).alignment = Alignment(horizontal="center", vertical="center")
        ws.cell(row=row_idx, column=3).alignment = Alignment(horizontal="center", vertical="center")
        ws.cell(row=row_idx, column=4).alignment = Alignment(horizontal="center", vertical="center")
        ws.cell(row=row_idx, column=5).alignment = Alignment(horizontal="center", vertical="center")
        ws.cell(row=row_idx, column=6).alignment = Alignment(horizontal="center", vertical="center")

        cat_val = ws.cell(row=row_idx, column=2).value
        if cat_val in badge_colors:
            fg, bg = badge_colors[cat_val]
            ws.cell(row=row_idx, column=2).font = Font(name="Segoe UI", size=8, bold=True, color=fg)
            ws.cell(row=row_idx, column=2).fill = PatternFill(start_color=bg, end_color=bg, fill_type="solid")

        # Symbol bold
        ws.cell(row=row_idx, column=3).font = bold_font

        # Numbers
        # Price formatting (forex with 5 decimals, crypto/stocks with 2-4 decimals)
        close_p = ws.cell(row=row_idx, column=10).value
        price_fmt = "0.00000" if (cat_val == "FOREX" or (close_p and close_p < 1.0)) else "#,##0.00"
        for c_idx in (7, 8, 9, 10):
            c = ws.cell(row=row_idx, column=c_idx)
            c.number_format = price_fmt
            c.alignment = Alignment(horizontal="right", vertical="center")

        # Volumes
        ws.cell(row=row_idx, column=11).number_format = "#,##0.00"
        ws.cell(row=row_idx, column=12).number_format = "$#,##0"
        ws.cell(row=row_idx, column=13).number_format = "$#,##0"
        ws.cell(row=row_idx, column=14).number_format = "$#,##0"

        # Candle Delta (USD)
        delta_cell = ws.cell(row=row_idx, column=15)
        delta_cell.number_format = "+$#,##0;-$#,##0;$0"
        delta_cell.alignment = Alignment(horizontal="right", vertical="center")
        delta_val = delta_cell.value or 0.0

        if delta_val > 0:
            delta_cell.fill = fill_pos_delta
            delta_cell.font = green_font
        elif delta_val < 0:
            delta_cell.fill = fill_neg_delta
            delta_cell.font = red_font

        # Candle Delta (Coins)
        delta_coin_cell = ws.cell(row=row_idx, column=16)
        delta_coin_cell.number_format = "+#,##0.00;-#,##0.00;0.00"
        delta_coin_cell.alignment = Alignment(horizontal="right", vertical="center")
        delta_coin_val = delta_coin_cell.value or 0.0
        delta_coin_cell.font = green_font if delta_coin_val >= 0 else red_font

        # Delta %
        pct_cell = ws.cell(row=row_idx, column=17)
        pct_cell.number_format = "+0.00%;-0.00%;0.00%"
        pct_cell.alignment = Alignment(horizontal="right", vertical="center")

        # CVD (USD)
        cvd_cell = ws.cell(row=row_idx, column=18)
        cvd_cell.number_format = "+$#,##0;-$#,##0;$0"
        cvd_cell.alignment = Alignment(horizontal="right", vertical="center")
        cvd_val = cvd_cell.value or 0.0
        cvd_cell.font = green_font if cvd_val >= 0 else red_font

        # CVD (Coins)
        cvd_coin_cell = ws.cell(row=row_idx, column=19)
        cvd_coin_cell.number_format = "+#,##0.00;-#,##0.00;0.00"
        cvd_coin_cell.alignment = Alignment(horizontal="right", vertical="center")
        cvd_coin_val = cvd_coin_cell.value or 0.0
        cvd_coin_cell.font = green_font if cvd_coin_val >= 0 else red_font

        # Z-Score
        z_cell = ws.cell(row=row_idx, column=20)
        z_cell.number_format = "+0.00;-0.00;0.00"
        z_cell.alignment = Alignment(horizontal="right", vertical="center")

        # Price Return %
        ret_cell = ws.cell(row=row_idx, column=21)
        ret_cell.number_format = "+0.00%;-0.00%;0.00%"
        ret_cell.alignment = Alignment(horizontal="right", vertical="center")

        # Regime highlight
        regime_cell = ws.cell(row=row_idx, column=22)
        regime_cell.alignment = Alignment(horizontal="center", vertical="center")
        regime_val = str(regime_cell.value or "")

        if "BULLISH ABSORPTION" in regime_val:
            regime_cell.fill = fill_bull_absorp
            regime_cell.font = Font(name="Segoe UI", size=8, bold=True, color="065F46")
        elif "BEARISH ABSORPTION" in regime_val:
            regime_cell.fill = fill_bear_absorp
            regime_cell.font = Font(name="Segoe UI", size=8, bold=True, color="9F1239")
        elif "AGGRESSIVE BUYING" in regime_val:
            regime_cell.fill = fill_agg_buy
            regime_cell.font = Font(name="Segoe UI", size=8, bold=True, color="075985")
        elif "AGGRESSIVE SELLING" in regime_val:
            regime_cell.fill = fill_agg_sell
            regime_cell.font = Font(name="Segoe UI", size=8, bold=True, color="92400E")

        # Trades Count
        ws.cell(row=row_idx, column=23).number_format = "#,##0"
        ws.cell(row=row_idx, column=23).alignment = Alignment(horizontal="right", vertical="center")

    # Column Widths
    col_widths = {
        "A": 20, # Timestamp
        "B": 14, # Asset Class
        "C": 12, # Symbol
        "D": 14, # Market Pair
        "E": 16, # Data Source
        "F": 12, # Timeframe
        "G": 14, # Open
        "H": 14, # High
        "I": 14, # Low
        "J": 14, # Close
        "K": 16, # Total Volume
        "L": 20, # Quote Volume
        "M": 18, # Taker Buy
        "N": 18, # Taker Sell
        "O": 20, # Candle Delta USD
        "P": 20, # Candle Delta Coins
        "Q": 15, # Delta %
        "R": 22, # Cumulative CVD USD
        "S": 22, # Cumulative CVD Coins
        "T": 16, # Z-Score
        "U": 15, # Return %
        "V": 24, # Regime
        "W": 14, # Trades
    }
    for col_let, w in col_widths.items():
        ws.column_dimensions[col_let].width = w

    # UI Polish: Enable Gridlines, AutoFilter, Freeze Panes at A2
    ws.views.sheetView[0].showGridLines = True
    ws.auto_filter.ref = f"A1:W{len(display_rows) + 1}"
    ws.freeze_panes = "A2"

    t_save = time.time()
        # Enforce Operator Invariant: Stamp Tier-1 Completion Banner ONLY ONCE row data is filled
    if ws.max_row > 1:
        try:
            from logger_config import stamp_sheet_completion_ist
            ws.insert_rows(1)
            stamp_sheet_completion_ist(
                ws=ws,
                sheet_title="18_CVD",
                row_count=ws.max_row - 2,
                banner_cell="A1",
                status="LIVE",
                merge_max_col=ws.max_column
            )
            ws.freeze_panes = "A3"
        except Exception as _e:
            pass

    temp_excel = excel_path.with_name(f"{excel_path.stem}_{os.getpid()}_{int(time.time()*1000)}.tmp.xlsx")
    wb.save(temp_excel)
    wb.close()
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
    log.info(f"Saved worksheet '{sheet_name}' in {time.time() - t_save:.2f}s with {len(display_rows):,} rows.")
    return len(display_rows)


# =====================================================================
# 7. PARQUET EXPORTER FOR VECTORIZED STRATEGY BACKTESTING
# =====================================================================
def export_cvd_to_parquet(
    rows: List[Dict[str, Any]],
    parquet_dir: pathlib.Path = DEFAULT_PARQUET_DIR,
) -> pathlib.Path:
    """Exports the complete 30-day continuous dataset to Parquet for sub-millisecond querying."""
    parquet_dir.mkdir(parents=True, exist_ok=True)
    df = pd.DataFrame(rows)

    all_path = parquet_dir / "18_CVD_30D_ALL.parquet"
    df.to_parquet(all_path, index=False, engine="pyarrow")
    log.info(f"Exported complete {len(df):,} rows to {all_path}")

    # Export individual timeframe parquets for fast modular loading
    for tf, sub_df in df.groupby("timeframe"):
        tf_path = parquet_dir / f"18_CVD_30D_{tf}.parquet"
        sub_df.to_parquet(tf_path, index=False, engine="pyarrow")

    return all_path


# =====================================================================
# 8. STANDALONE & PIPELINE ENTRYPOINT
# =====================================================================
def main() -> int:
    parser = argparse.ArgumentParser(
        description="18_CVD: Multi-Asset Multi-Timeframe Continuous CVD Engine (Crypto, Metals, Indices, Forex, Commodities)"
    )
    parser.add_argument(
        "--excel-path",
        type=pathlib.Path,
        default=DEFAULT_EXCEL_PATH,
        help="Path to Data/DataBase_Trading.xlsx",
    )
    parser.add_argument(
        "--parquet-dir",
        type=pathlib.Path,
        default=DEFAULT_PARQUET_DIR,
        help="Directory to save fast vectorized Parquet datasets",
    )
    parser.add_argument(
        "--days",
        type=int,
        default=30,
        help="Continuous lookback window in days (default: 30)",
    )
    parser.add_argument(
        "--timeframes",
        nargs="+",
        default=TIMEFRAMES_DEFAULT,
        help="Timeframes to harvest: 5m, 15m, 1h, 4h",
    )
    parser.add_argument(
        "--max-excel-rows",
        type=int,
        default=1500,
        help="Maximum rows to insert into Excel sheet (default: 50000, 0 for unlimited)",
    )
    parser.add_argument(
        "--symbols",
        nargs="+",
        default=None,
        help="Optional list of display symbols to filter (e.g. BTC ETH GOLD SP500 EURUSD)",
    )

    args = parser.parse_args()

    # Filter roster if custom symbols provided
    roster = DEFAULT_ASSET_ROSTER
    if args.symbols:
        target_syms = set(s.upper() for s in args.symbols)
        roster = [item for item in roster if item[1].upper() in target_syms]

    log.info(
        f"Initializing 18_CVD with {len(roster)} assets across categories, lookback: {args.days} days, timeframes: {args.timeframes}"
    )

    # 1. Harvest Continuous Data
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    try:
        rows = loop.run_until_complete(
            harvest_all_assets_cvd(roster, timeframes=args.timeframes, days=args.days)
        )
    finally:
        loop.close()

    if not rows:
        log.error("Failed to harvest any CVD candle records. Aborting.")
        return 1

    # 2. Persist Vectorized Parquets for Zero-Latency Strategy Ingestion
    export_cvd_to_parquet(rows, parquet_dir=args.parquet_dir)

    # 3. Export Formatted Worksheet to Excel
    written = export_cvd_to_excel(
        rows,
        excel_path=args.excel_path,
        sheet_name=SHEET_NAME,
        max_excel_rows=args.max_excel_rows,
    )

    log.info(f"[SUCCESS] 18_CVD completed successfully with {written:,} rows in Excel and {len(rows):,} in Parquet.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
