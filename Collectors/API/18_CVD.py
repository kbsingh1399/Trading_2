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
  - Excel Worksheet: '18_CVD' positioned at Index 26 in Data/feeds/<feed_name>.parquet
  - High-Speed Parquet Datasets: Data/CVD/18_CVD_30D_ALL.parquet for instant ML/quant query
"""

from __future__ import annotations


import argparse
import asyncio
import datetime
import json
import logging
import math
import os
import pathlib
ROOT = pathlib.Path(__file__).resolve().parents[2]
import sys
import time
import urllib.request
import zipfile
from typing import Any, Dict, List, Optional, Tuple

import aiohttp
import numpy as np
import pandas as pd


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
def export_cvd_to_parquet(
    rows: List[Dict[str, Any]],
    parquet_dir: pathlib.Path = DEFAULT_PARQUET_DIR,
) -> pathlib.Path:
    """Exports dataset to Data/feeds/18_CVD.parquet and timeframe parquets."""
    parquet_dir.mkdir(parents=True, exist_ok=True)
    df = pd.DataFrame(rows)

    # 1. Primary Canonical Parquet Feed (< 1500 rows for high-speed audit)
    sys.path.insert(0, str(ROOT / 'Collectors' / 'Core'))
    sys.path.insert(0, str(ROOT / 'Terminal' / 'Data_Factory'))
    from parquet_feed_writer import write_parquet_feed
    capped_rows = rows[-1500:] if len(rows) > 1500 else rows
    meta = write_parquet_feed("18_CVD", capped_rows)
    log.info(f"Exported canonical 18_CVD feed ({len(capped_rows):,} rows): {meta.get('byte_size')} bytes.")

    all_path = parquet_dir / "18_CVD_30D_ALL.parquet"
    df.to_parquet(all_path, index=False, engine="pyarrow")
    write_parquet_feed("18_CVD_30D_ALL", df)
    log.info(f"Exported complete {len(df):,} rows to {all_path} and Data/feeds/18_CVD_30D_ALL.parquet")

    for tf, sub_df in df.groupby("timeframe"):
        tf_path = parquet_dir / f"18_CVD_30D_{tf}.parquet"
        sub_df.to_parquet(tf_path, index=False, engine="pyarrow")
        write_parquet_feed(f"18_CVD_30D_{tf}", sub_df)
        log.info(f"Mirrored timeframe CVD feed to Data/feeds/18_CVD_30D_{tf}.parquet ({len(sub_df):,} rows)")

    return all_path


def main() -> int:
    parser = argparse.ArgumentParser(
        description="18_CVD: Multi-Asset Multi-Timeframe Continuous CVD Engine"
    )
    parser.add_argument("--days", type=int, default=1, help="Lookback days")
    parser.add_argument("--timeframes", nargs="+", default=["5m", "15m", "1h", "4h"])
    parser.add_argument("--symbols", nargs="+", default=None)
    parser.add_argument("--parquet-dir", type=pathlib.Path, default=DEFAULT_PARQUET_DIR)
    args = parser.parse_args()

    roster = DEFAULT_ASSET_ROSTER
    if args.symbols:
        target_syms = set(s.upper() for s in args.symbols)
        roster = [item for item in roster if item[1].upper() in target_syms]

    log.info(f"Initializing 18_CVD with {len(roster)} assets across categories...")
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

    export_cvd_to_parquet(rows, parquet_dir=args.parquet_dir)
    log.info(f"[SUCCESS] 18_CVD completed successfully with {len(rows):,} rows in Parquet.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
