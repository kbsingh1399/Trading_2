#!/usr/bin/env python3
"""
Data/Excel_Modules/15_Hyperdash_Stops_Map.py
============================================
Hyperdash Multi-Asset On-Chain Stop-Loss Orders Price Ladder & Cumulative Map (100% Native API).
Captures point-by-point buy/sell stop-loss clusters and cumulative curves across all 18 institutional
perpetual assets directly from Hyperdash GraphQL API (https://api.hyperdash.com/graphql) without browser or CDP overhead,
and stacks them asset-over-asset into worksheet '15_Hyperdash_Stops_Map' in Data/feeds/<feed_name>.parquet
(positioned at Index 23, immediately after '14_Hyperdash_Liq_Map').

Universe (18 Institutional Binance USDT-M Perpetuals):
  BTC, ETH, XRP, SOL, BNB, DOGE, ADA, TRX, LINK, AVAX, SUI, NEAR, DOT, LTC, BCH, APT, OP, ARB

Layout Matches Operator Specifications & 8_Exchange_Liquidation_Map_1D:
  Sr.No | Asset | Time | TimeStamp | Mark Price | Price | Distance (%) | Side | Cumulative Stops | Buy Stops | Sell Stops | Size (Coins)
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
log = logging.getLogger("15_Hyperdash_Stops_Map")

MODULES_DIR = pathlib.Path(__file__).resolve().parent
ROOT_DIR = MODULES_DIR.parents[1]
GRAPHQL_URL = "https://api.hyperdash.com/graphql"
SHEET_NAME = "15_Hyperdash_Stops_Map"

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
    ("side", "Side", 14, "center"),
    ("cumulative_stops", "Cumulative Stops", 24, "right"),
    ("buy_stops", "Buy Stops", 20, "right"),
    ("sell_stops", "Sell Stops", 20, "right"),
    ("size_coins", "Size (Coins)", 18, "right"),
]

QUERY_STOPS = """
query GetStopOrderLevelsV2($coin: String!, $minPrice: Float!, $maxPrice: Float!, $startTime: Float!, $endTime: Float) {
  analytics {
    stopOrderLevels: stopOrderLevelsV2(
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


def fetch_stops_ladder(coin: str, now_ms: float, start_ms: float) -> tuple[float, list[dict]]:
    """Fetches full stop order band ladder for coin via Hyperdash native GraphQL API."""
    payload = json.dumps({
        "query": QUERY_STOPS,
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
            stop_data = analytics.get("stopOrderLevels")
            if not stop_data:
                return 0.0, []
            
            mark_price = float(stop_data.get("currentPrice") or 0.0)
            bands = stop_data.get("bands", [])
            
            active_bands = []
            for b in bands:
                hist = b.get("historicalData")
                if hist and len(hist) > 0:
                    last_pt = hist[-1]
                    amt = float(last_pt.get("totalAmount") or 0.0)
                    if amt > 0:
                        mid_px = (float(b["minPrice"]) + float(b["maxPrice"])) / 2.0
                        notional = amt * mid_px
                        is_buy = mid_px > mark_price
                        active_bands.append({
                            "mid_px": mid_px,
                            "amt": amt,
                            "notional": notional,
                            "side": "Buy Stop" if is_buy else "Sell Stop",
                        })
            return mark_price, active_bands
    except Exception as e:
        log.warning(f"Error fetching stops ladder for {coin}: {e}")
        return 0.0, []


def harvest_all_stops_maps(symbols: list[str]) -> list[dict]:
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

    def _fetch_worker(sym: str):
        return sym, fetch_stops_ladder(sym, now_ms, start_ms)

    log.info(f"Concurrently harvesting Hyperdash Stops Map for {len(symbols)} symbols...")
    with ThreadPoolExecutor(max_workers=9) as executor:
        fetched_dict = dict(executor.map(_fetch_worker, symbols))

    for idx, sym in enumerate(symbols, start=1):
        mark_px, bands = fetched_dict.get(sym, (0.0, []))
        if not bands or mark_px <= 0:
            log.warning(f"  No active stop bands for {sym}")
            continue

        # Separate into Sell Stops (< mark_px) and Buy Stops (> mark_px)
        sells = [b for b in bands if b["side"] == "Sell Stop"]
        buys = [b for b in bands if b["side"] == "Buy Stop"]

        # Sort Sells descending by price (closest to mark first for cumulative sum)
        sells.sort(key=lambda x: x["mid_px"], reverse=True)
        cum_sells = 0.0
        for b in sells:
            cum_sells += b["notional"]
            b["cum_notional"] = cum_sells

        # Sort Buys ascending by price (closest to mark first for cumulative sum)
        buys.sort(key=lambda x: x["mid_px"])
        cum_buys = 0.0
        for b in buys:
            cum_buys += b["notional"]
            b["cum_notional"] = cum_buys

        # For the worksheet display: stack in price ascending order (institutional ladder)
        all_sym_bands = sells + buys
        all_sym_bands.sort(key=lambda x: x["mid_px"])

        log.info(f"  {sym}: Mark={mark_px:,.2f} | Sell Stops={len(sells)} | Buy Stops={len(buys)} | Total={len(all_sym_bands)}")

        for b in all_sym_bands:
            px = b["mid_px"]
            side = b["side"]
            notional = b["notional"]
            cum_notional = b["cum_notional"]
            amt = b["amt"]
            dist_pct = ((px - mark_px) / mark_px) * 100.0

            buy_val = format_usd(notional) if side == "Buy Stop" else "$0"
            sell_val = format_usd(notional) if side == "Sell Stop" else "$0"
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
                "cumulative_stops": cum_val,
                "buy_stops": buy_val,
                "sell_stops": sell_val,
                "size_coins": f"{amt:,.4f} {sym}",
            })
            global_sr_no += 1

    log.info(f"Total Stops Map records across all {len(symbols)} assets: {len(all_records)} rows.")
    return all_records


def dump_to_parquet(records: list[dict], feed_name: str = SHEET_NAME) -> bool:
    if not records:
        log.warning("No stops records to dump to Parquet.")
        return False
    meta = write_parquet_feed(feed_name, records)
    log.info(f"Successfully dumped {len(records)} Hyperdash Stops Map rows into Parquet feed '{feed_name}': {meta.get('byte_size')} bytes in {meta.get('write_latency_ms', 0):.2f}ms.")
    return True


def main():
    parser = argparse.ArgumentParser(description="Hyperdash Stop-Loss Cluster Map Pure-Parquet Dumper")
    parser.add_argument("--sheet-name", default=SHEET_NAME, help="Target feed name")
    args = parser.parse_args()

    t_start = time.time()
    log.info("Starting Hyperdash Stops Map harvest...")
    records = harvest_all_stops_maps(DEFAULT_UNIVERSE)
    if not records:
        log.error("No stop records returned from Hyperdash.")
        sys.exit(1)

    success = dump_to_parquet(records, feed_name=args.sheet_name)
    elapsed = time.time() - t_start
    log.info(f"15_Hyperdash_Stops_Map completed in {elapsed:.2f}s with status: {'SUCCESS' if success else 'FAILED'}")
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
