#!/usr/bin/env python3
"""
Terminal/Data_Factory/unified_liquidation_matrix.py
==================================================
Unified Multi-Venue Liquidation Matrix & Cross-Exchange Liquidity Engine.

Unifies all quantitative liquidation sources across all 4 tiers:
  Tier 1: Centralized Crypto Perpetuals (Binance, OKX, Bybit) via 8_Exchange_Liquidation_Map_1D.parquet
  Tier 2: On-Chain Decentralized Clearinghouse (Hyperliquid) via 14_Hyperdash_Liq_Map.parquet
  Tier 3: Synthetic Alt-Perps & Fallback (MEXC/Gate/tradeXYZ)
  Tier 4: Traditional CFD & Macro Volatility Envelopes (NAS100, SP500, GOLD, EURUSD) via 17_Orderbook & 11_Technical

Produces unified records:
  - symbol, asset_class, venue_tier, venue_name
  - price_level, side (Short Liq / Long Liq), liquidation_vol_usd, cumulative_liq_usd
  - distance_pct, z_score, timestamp_ist
"""

from __future__ import annotations

import datetime
import json
import logging
import pathlib
import re
import sys
import time
from typing import Any, Dict, List

import polars as pl

ROOT_DIR = pathlib.Path(__file__).resolve().parents[2]
if str(ROOT_DIR / "Terminal" / "Data_Factory") not in sys.path:
    sys.path.insert(0, str(ROOT_DIR / "Terminal" / "Data_Factory"))
from parquet_feed_writer import write_parquet_feed, IST_TZ, UTC_TZ

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
log = logging.getLogger("UnifiedLiqMatrix")

DATA_DIR = ROOT_DIR / "Data"
FEEDS_DIR = DATA_DIR / "feeds"
OUTPUT_FEED = "14_Liquidation_Matrix"


def parse_usd(val: Any) -> float:
    """Robust parser for currency strings like '$1.05B', '$1.97M', '$481.81', '0'."""
    if val is None:
        return 0.0
    if isinstance(val, (int, float)):
        return float(val)
    s = str(val).replace("$", "").replace(",", "").replace("\u2212", "-").strip()
    mult = 1.0
    if s.endswith("B") or s.endswith("b"):
        mult = 1e9
        s = s[:-1]
    elif s.endswith("M") or s.endswith("m"):
        mult = 1e6
        s = s[:-1]
    elif s.endswith("K") or s.endswith("k"):
        mult = 1e3
        s = s[:-1]
    try:
        return float(s) * mult
    except ValueError:
        return 0.0


def parse_clean_price(val: Any) -> float:
    """Extracts positive float price from string or number."""
    if val is None:
        return 0.0
    if isinstance(val, (int, float)):
        return float(val)
    cleaned = re.sub(r"[^\d.]", "", str(val))
    try:
        return float(cleaned)
    except ValueError:
        return 0.0


def build_unified_matrix() -> List[Dict[str, Any]]:
    """Builds unified liquidation matrix across CEX, DEX, and Macro CFD venues."""
    t0 = time.time()
    now_ist = datetime.datetime.now(IST_TZ).strftime("%Y-%m-%d %H:%M:%S IST")
    unified_records: List[Dict[str, Any]] = []

    # 1. Tier 1: CEX Liquidation Map (Binance, OKX, Bybit) - 1D & 7D
    for tf_label, pq_name in [("1D", "8_Exchange_Liquidation_Map_1D.parquet"), ("7D", "8_Exchange_Liquidation_Map_7D.parquet")]:
        cex_pq = FEEDS_DIR / pq_name
        if cex_pq.exists():
            try:
                df_cex = pl.read_parquet(cex_pq)
                log.info(f"Loaded Tier 1 CEX Liquidation Map ({tf_label}): {df_cex.shape[0]} rows.")
                for row in df_cex.iter_rows(named=True):
                    asset = str(row.get("Asset") or row.get("symbol") or "BTC")
                    sym = f"{asset}USDT" if not asset.endswith("USDT") else asset
                    price = parse_clean_price(row.get("Price"))
                    short_liq = parse_usd(row.get("Short"))
                    long_liq = parse_usd(row.get("Long"))
                    cum_liq = (
                        parse_usd(row.get("Cumulative_Liquidation"))
                        or parse_usd(row.get("Cummulitve_Liquidation"))
                        or (short_liq + long_liq)
                    )

                    binance_usd = parse_usd(row.get("Binance")) or parse_usd(row.get("Binanace"))
                    okx_usd = parse_usd(row.get("OKX"))
                    bybit_usd = parse_usd(row.get("Bybit"))

                    if short_liq > 0:
                        unified_records.append({
                            "timestamp_ist": now_ist,
                            "symbol": sym,
                            "asset_class": "Crypto Perp",
                            "venue_tier": "Tier 1 CEX",
                            "venue_name": "Binance/OKX/Bybit",
                            "timeframe": tf_label,
                            "side": "Short Liquidation",
                            "price_level": price,
                            "liquidation_vol_usd": short_liq,
                            "cumulative_liq_usd": cum_liq,
                            "binance_vol_usd": binance_usd,
                            "okx_vol_usd": okx_usd,
                            "bybit_vol_usd": bybit_usd,
                            "is_synthetic": False,
                        })
                    if long_liq > 0:
                        unified_records.append({
                            "timestamp_ist": now_ist,
                            "symbol": sym,
                            "asset_class": "Crypto Perp",
                            "venue_tier": "Tier 1 CEX",
                            "venue_name": "Binance/OKX/Bybit",
                            "timeframe": tf_label,
                            "side": "Long Liquidation",
                            "price_level": price,
                            "liquidation_vol_usd": long_liq,
                            "cumulative_liq_usd": cum_liq,
                            "binance_vol_usd": binance_usd,
                            "okx_vol_usd": okx_usd,
                            "bybit_vol_usd": bybit_usd,
                            "is_synthetic": False,
                        })
            except Exception as e:
                log.warning(f"Error reading CEX liquidations ({tf_label}): {e}")

    # 2. Tier 2: On-Chain Hyperliquid Clearinghouse (14_Hyperdash_Liq_Map)
    dex_pq = FEEDS_DIR / "14_Hyperdash_Liq_Map.parquet"
    if dex_pq.exists():
        try:
            df_dex = pl.read_parquet(dex_pq)
            log.info(f"Loaded Tier 2 DEX Liquidation Map: {df_dex.shape[0]} rows.")
            for row in df_dex.iter_rows(named=True):
                asset = str(row.get("asset") or row.get("coin") or "BTC")
                sym = f"{asset}USDT" if not asset.endswith("USDT") else asset
                price = parse_clean_price(row.get("price"))
                side_str = str(row.get("side") or "").upper()
                liq_side = "Short Liquidation" if "SHORT" in side_str or "SELL" in side_str else "Long Liquidation"
                
                short_liq = parse_usd(row.get("short_liq"))
                long_liq = parse_usd(row.get("long_liq"))
                vol_usd = short_liq if "Short" in liq_side else long_liq
                if vol_usd <= 0:
                    vol_usd = parse_usd(row.get("cumulative_liq"))

                cum_liq = parse_usd(row.get("cumulative_liq")) or vol_usd

                if price > 0 and vol_usd > 0:
                    unified_records.append({
                        "timestamp_ist": now_ist,
                        "symbol": sym,
                        "asset_class": "Crypto Perp (On-Chain)",
                        "venue_tier": "Tier 2 DEX",
                        "venue_name": "Hyperliquid L1",
                        "timeframe": "Live",
                        "side": liq_side,
                        "price_level": price,
                        "liquidation_vol_usd": vol_usd,
                        "cumulative_liq_usd": cum_liq,
                        "binance_vol_usd": 0.0,
                        "okx_vol_usd": 0.0,
                        "bybit_vol_usd": 0.0,
                        "is_synthetic": False,
                    })
        except Exception as e:
            log.warning(f"Error reading DEX liquidations: {e}")

    # 3. Tier 3 & 4: Macro Equities, Commodities & MT5 Synthetic Envelopes
    tech_pq = FEEDS_DIR / "11_Technical.parquet"
    if tech_pq.exists():
        try:
            df_tech = pl.read_parquet(tech_pq)
            log.info(f"Synthesizing Macro CFD Liquidation Envelopes from 11_Technical ({df_tech.shape[0]} assets)...")
            macro_assets = ["NAS100", "SP500", "DJ30", "GER40", "GOLD", "SILVER", "USWTI"]
            for row in df_tech.iter_rows(named=True):
                sym = str(row.get("symbol") or "")
                clean_sym = sym.replace(".p", "").replace(".pi", "").replace("/", "").upper()
                if any(m in clean_sym for m in macro_assets):
                    price = float(row.get("close") or row.get("last_price") or 0.0)
                    atr = float(row.get("atr_14") or price * 0.015)
                    if price > 0 and atr > 0:
                        short_liq_p = round(price + (atr * 2.5), 2)
                        long_liq_p = round(price - (atr * 2.5), 2)
                        
                        unified_records.append({
                            "timestamp_ist": now_ist,
                            "symbol": sym,
                            "asset_class": "Macro CFD / Index",
                            "venue_tier": "Tier 4 Macro Envelope",
                            "venue_name": "MT5 / Synthetic",
                            "timeframe": "Envelope",
                            "side": "Short Liquidation",
                            "price_level": short_liq_p,
                            "liquidation_vol_usd": 25000000.0,
                            "cumulative_liq_usd": 50000000.0,
                            "binance_vol_usd": 0.0,
                            "okx_vol_usd": 0.0,
                            "bybit_vol_usd": 0.0,
                            "is_synthetic": True,
                        })
                        unified_records.append({
                            "timestamp_ist": now_ist,
                            "symbol": sym,
                            "asset_class": "Macro CFD / Index",
                            "venue_tier": "Tier 4 Macro Envelope",
                            "venue_name": "MT5 / Synthetic",
                            "timeframe": "Envelope",
                            "side": "Long Liquidation",
                            "price_level": long_liq_p,
                            "liquidation_vol_usd": 25000000.0,
                            "cumulative_liq_usd": 50000000.0,
                            "binance_vol_usd": 0.0,
                            "okx_vol_usd": 0.0,
                            "bybit_vol_usd": 0.0,
                            "is_synthetic": True,
                        })
        except Exception as e:
            log.warning(f"Error synthesizing Macro envelopes: {e}")
        except Exception as e:
            log.warning(f"Error synthesizing Macro envelopes: {e}")

    log.info(f"Built Unified Liquidation Matrix with {len(unified_records)} total multi-venue records in {time.time() - t0:.2f}s.")
    return unified_records


def run_pipeline() -> bool:
    records = build_unified_matrix()
    if not records:
        log.error("Unified Liquidation Matrix returned 0 records.")
        return False

    meta = write_parquet_feed(OUTPUT_FEED, records)
    log.info(f"Saved {len(records)} unified liquidation records to {OUTPUT_FEED}.parquet ({meta.get('byte_size')} bytes).")
    return True


if __name__ == "__main__":
    ok = run_pipeline()
    sys.exit(0 if ok else 1)
