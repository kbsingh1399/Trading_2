#!/usr/bin/env python3
"""
Data/Excel_Modules/14_Hyperdash_Liq_Map.py
==========================================
Hyperdash Multi-Asset On-Chain Liquidation Price Ladder & Cumulative Map (100% Native API).
Captures point-by-point long/short liquidation levels and cumulative curves across all 18 institutional
perpetual assets directly from Hyperdash GraphQL API (https://api.hyperdash.com/graphql) without browser or CDP overhead,
and stacks them asset-over-asset into worksheet '14_Hyperdash_Liq_Map' in Data/feeds/<feed_name>.parquet
(positioned at Index 22, immediately after '13_Hyperliquid').

Universe (18 Institutional Binance USDT-M Perpetuals):
  BTC, ETH, XRP, SOL, BNB, DOGE, ADA, TRX, LINK, AVAX, SUI, NEAR, DOT, LTC, BCH, APT, OP, ARB

Layout Matches Operator Specifications & 8_Exchange_Liquidation_Map_1D:
  Sr.No | Asset | Time | TimeStamp | Mark Price | Price | Distance (%) | Side | Cumulative Liquidation | Short Liquidation | Long Liquidation | Size (Coins)
"""

from __future__ import annotations

import pathlib
import sys
ROOT_DIR_FOR_PQ = pathlib.Path(__file__).resolve().parents[2]
if str(ROOT_DIR_FOR_PQ / "Collectors" / "Core") not in sys.path:
    sys.path.insert(0, str(ROOT_DIR_FOR_PQ / "Collectors" / "Core"))
if str(ROOT_DIR_FOR_PQ / "Terminal" / "Data_Factory") not in sys.path:
    sys.path.insert(0, str(ROOT_DIR_FOR_PQ / "Terminal" / "Data_Factory"))
from parquet_feed_writer import write_parquet_feed, IST_TZ, UTC_TZ


# Pure Parquet Pipeline

import argparse
import datetime
import json
import logging
import pathlib
import sys
import time
import urllib.request


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] [%(name)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
log = logging.getLogger("14_Hyperdash_Liq_Map")

MODULES_DIR = pathlib.Path(__file__).resolve().parent
ROOT_DIR = MODULES_DIR.parents[1]
GRAPHQL_URL = "https://api.hyperdash.com/graphql"
SHEET_NAME = "14_Hyperdash_Liq_Map"

DEFAULT_UNIVERSE = [
    "BTC", "ETH", "XRP", "SOL", "BNB",
    "DOGE", "ADA", "TRX", "LINK", "AVAX",
    "SUI", "NEAR", "DOT", "LTC", "BCH",
    "APT", "OP", "ARB",
]

COLUMNS_DEF = [
    ("sr_no", "Sr.No", 10, "center"),
    ("asset", "Asset", 12, "center"),
    ("time_window", "Time", 10, "center"),
    ("timestamp_ist", "Timestamp (IST)", 24, "center"),
    ("mark_price", "Mark Price", 16, "right"),
    ("price", "Price", 16, "right"),
    ("distance_pct", "Distance (%)", 14, "right"),
    ("side", "Side", 12, "center"),
    ("cumulative_liq", "Cumulative Liquidation", 24, "right"),
    ("short_liq", "Short Liquidation", 20, "right"),
    ("long_liq", "Long Liquidation", 20, "right"),
    ("size_coins", "Size (Coins)", 18, "right"),
]

QUERY_LIQS = """
query GetLiquidationLevelsV2($coin: String!, $minPrice: Float!, $maxPrice: Float!, $startTime: Float!, $endTime: Float) {
  analytics {
    liquidationLevels: liquidationLevelsV2(
      coin: $coin
      minPrice: $minPrice
      maxPrice: $maxPrice
      startTime: $startTime
      endTime: $endTime
    ) {
      coin
      currentPrice
      bandSize
      bands {
        minPrice
        maxPrice
        historicalData {
          timestamp
          totalAmount
        }
      }
    }
  }
}
"""


def format_usd(val: float | None) -> str:
    """Formats float amount to human-readable string matching CoinGlass/Hyperdash UI."""
    if val is None or val == 0:
        return "$0"
    abs_val = abs(val)
    if abs_val >= 1e9:
        return f"${val / 1e9:.2f}B"
    elif abs_val >= 1e6:
        return f"${val / 1e6:.2f}M"
    elif abs_val >= 1e3:
        return f"${val / 1e3:.2f}K"
    elif abs_val >= 1:
        return f"${val:.2f}"
    else:
        return f"${val:.4f}"


def format_price(val: float | None) -> str:
    if val is None:
        return "$0"
    if val >= 1000:
        return f"${val:,.2f}"
    elif val >= 1:
        return f"${val:,.4f}"
    else:
        return f"${val:,.6f}"


def fetch_liquidation_ladder(coin: str, now_ms: float, start_ms: float) -> tuple[float, list[dict]]:
    """Fetches full liquidation band ladder for coin via Hyperdash native GraphQL API."""
    payload = json.dumps({
        "query": QUERY_LIQS,
        "variables": {
            "coin": coin,
            "minPrice": 0.0,
            "maxPrice": 10000000.0,
            "startTime": start_ms,
            "endTime": now_ms
        }
    }).encode("utf-8")
    
    req = urllib.request.Request(
        GRAPHQL_URL,
        data=payload,
        headers={
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
            "Content-Type": "application/json"
        }
    )
    
    try:
        with urllib.request.urlopen(req, timeout=12) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            analytics = data.get("data", {}).get("analytics", {})
            liq_data = analytics.get("liquidationLevels")
            if not liq_data:
                return 0.0, []
            
            mark_price = float(liq_data.get("currentPrice") or 0.0)
            bands = liq_data.get("bands", [])
            
            active_bands = []
            for b in bands:
                hist = b.get("historicalData")
                if hist and len(hist) > 0:
                    last_pt = hist[-1]
                    amt = float(last_pt.get("totalAmount") or 0.0)
                    if abs(amt) > 0:
                        mid_px = (float(b["minPrice"]) + float(b["maxPrice"])) / 2.0
                        notional = abs(amt) * mid_px
                        is_short = (amt < 0) or (mid_px > mark_price)
                        active_bands.append({
                            "mid_px": mid_px,
                            "amt": abs(amt),
                            "notional": notional,
                            "side": "Short" if is_short else "Long",
                        })
            return mark_price, active_bands
    except Exception as e:
        log.warning(f"Error fetching liquidation ladder for {coin}: {e}")
        return 0.0, []


def harvest_all_liquidation_maps(symbols: list[str]) -> list[dict]:
    """Iterates through symbols, calculates cumulative curves outward from mark, and stacks rows."""
    all_records = []
    global_sr_no = 1
    now = datetime.datetime.now(datetime.timezone.utc)
    ist_tz = datetime.timezone(datetime.timedelta(hours=5, minutes=30))
    now_ist = datetime.datetime.now(ist_tz)
    ts_str = now_ist.strftime("%Y-%m-%d %H:%M:%S IST")
    now_ms = now.timestamp() * 1000
    start_ms = now_ms - 24 * 3600 * 1000

    from concurrent.futures import ThreadPoolExecutor

    def _fetch_liq_worker(sym: str):
        return sym, fetch_liquidation_ladder(sym, now_ms, start_ms)

    log.info(f"Concurrently harvesting Hyperdash Liquidation Map for {len(symbols)} symbols...")
    with ThreadPoolExecutor(max_workers=9) as executor:
        fetched_dict = dict(executor.map(_fetch_liq_worker, symbols))

    for idx, sym in enumerate(symbols, start=1):
        mark_px, bands = fetched_dict.get(sym, (0.0, []))
        if not bands or mark_px <= 0:
            log.warning(f"  No active liquidation bands for {sym}")
            continue

        # Separate into Longs (< mark_px) and Shorts (> mark_px)
        longs = [b for b in bands if b["side"] == "Long"]
        shorts = [b for b in bands if b["side"] == "Short"]

        # Sort Longs descending by price (closest to mark first for cumulative sum)
        longs.sort(key=lambda x: x["mid_px"], reverse=True)
        cum_long = 0.0
        for b in longs:
            cum_long += b["notional"]
            b["cum_notional"] = cum_long

        # Sort Shorts ascending by price (closest to mark first for cumulative sum)
        shorts.sort(key=lambda x: x["mid_px"])
        cum_short = 0.0
        for b in shorts:
            cum_short += b["notional"]
            b["cum_notional"] = cum_short

        # For the worksheet display: stack in price ascending order (institutional ladder)
        # Combine and sort ascending by price
        all_sym_bands = longs + shorts
        all_sym_bands.sort(key=lambda x: x["mid_px"])

        log.info(f"  {sym}: Mark={mark_px:,.2f} | Long Bands={len(longs)} | Short Bands={len(shorts)} | Total={len(all_sym_bands)}")

        for b in all_sym_bands:
            px = b["mid_px"]
            side = b["side"]
            notional = b["notional"]
            cum_notional = b["cum_notional"]
            amt = b["amt"]
            dist_pct = ((px - mark_px) / mark_px) * 100.0

            short_val = format_usd(notional) if side == "Short" else "$0"
            long_val = format_usd(notional) if side == "Long" else "$0"
            cum_val = format_usd(cum_notional)

            all_records.append({
                "sr_no": global_sr_no,
                "asset": sym,
                "time_window": "Live",
                "timestamp_ist": ts_str,
                "mark_price": format_price(mark_px),
                "price": format_price(px),
                "distance_pct": f"{dist_pct:+.2f}%",
                "side": side,
                "cumulative_liq": cum_val,
                "short_liq": short_val,
                "long_liq": long_val,
                "size_coins": f"{amt:,.4f} {sym}",
            })
            global_sr_no += 1

    log.info(f"Total Liquidation Map records across all {len(symbols)} assets: {len(all_records)} rows.")
    return all_records


def dump_to_parquet(records: list[dict], feed_name: str = SHEET_NAME) -> bool:
    if not records:
        log.warning("No liquidation records to dump to Parquet.")
        return False
    meta = write_parquet_feed(feed_name, records)
    log.info(f"Successfully dumped {len(records)} Hyperdash Liq Map rows into Parquet feed '{feed_name}': {meta.get('byte_size')} bytes in {meta.get('write_latency_ms', 0):.2f}ms.")
    return True


def main():
    parser = argparse.ArgumentParser(description="Hyperdash Liquidation Map Pure-Parquet Dumper")
    parser.add_argument("--sheet-name", default=SHEET_NAME, help="Target feed name")
    args = parser.parse_args()

    t_start = time.time()
    log.info("Starting Hyperdash Liquidation Map harvest...")
    records = harvest_all_liquidation_maps(DEFAULT_UNIVERSE)
    if not records:
        log.error("No liquidation records returned from Hyperdash.")
        sys.exit(1)

    success = dump_to_parquet(records, feed_name=args.sheet_name)
    elapsed = time.time() - t_start
    log.info(f"14_Hyperdash_Liq_Map completed in {elapsed:.2f}s with status: {'SUCCESS' if success else 'FAILED'}")
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
