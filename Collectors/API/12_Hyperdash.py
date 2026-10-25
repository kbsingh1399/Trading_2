#!/usr/bin/env python3
"""
Data/Excel_Modules/12_Hyperdash.py
==================================
Dedicated Excel Module 20: Hyperdash On-Chain Flow & Microstructure Intelligence.
Extracts and consolidates comprehensive intelligence from Hyperdash GraphQL API
(https://api.hyperdash.com/graphql) and Hyperdash On-Chain Flow Engine:
  - Section 1: Macro Hyperdash On-Chain Intelligence Summary & Telemetry
  - Section 2: Universe Per-Asset On-Chain Flow Attribution Matrix
  - Section 3: Level 3 Institutional Resting Whale Orders (Mapped to Ethereum Hex Addresses)
  - Section 4: Top Liquidation Clusters & Liquidation Whale Addresses (BTC & ETH)
  - Section 5: Top Stop-Loss Clusters & Whale Stop Addresses (BTC & ETH)
  - Section 6: Recent Confirmed On-Chain Liquidations Feed (Hyperliquid L1)
  - Section 7: Recent Whale Trades & Smart Money Executions

Target Sheet: '12_Hyperdash' in Data/feeds/<feed_name>.parquet
Position: Immediately following '11_Technical'.
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

try:
    from logger_config import stamp_sheet_completion_ist, get_current_timestamps
except ImportError:
    stamp_sheet_completion_ist = None
    get_current_timestamps = None


import argparse
import datetime
import json
import logging
import math
import pathlib
import sys
import time
from typing import Any, Dict, List, Optional, Tuple


MODULES_DIR = pathlib.Path(__file__).resolve().parent
ROOT_DIR = MODULES_DIR.parents[1]
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

from Terminal.Api_Client import HyperdashClient
from Terminal.Asset_Universe import COMPLETE_UNIVERSE, canonical_asset
from Terminal.Data_Factory.hyperdash_flow_feed import get_hyperdash_flow_intelligence

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] [12_Hyperdash] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
log = logging.getLogger("12_Hyperdash")

TARGET_SHEET_NAME = "12_Hyperdash"
TARGET_INDEX = 20

# -------------------------------------------------------------------------
# Table Schemas
# -------------------------------------------------------------------------
SECTION_2_COLS = [
    ("sr_no", "Sr. No.", 8, "center"),
    ("asset", "Asset", 12, "center"),
    ("liquidations_usd", "Liquidations (USD)", 20, "right"),
    ("imminent_liqs_usd", "Imminent Hazards (USD)", 22, "right"),
    ("twap_notional_usd", "TWAP Notional (USD)", 22, "right"),
    ("whale_trades_usd", "Whale Trades (USD)", 20, "right"),
    ("oi_surges_count", "OI Surges", 12, "right"),
    ("dominant_bias", "Dominant Flow Bias", 30, "center"),
]

SECTION_3_COLS = [
    ("sr_no", "Sr. No.", 8, "center"),
    ("coin", "Asset", 10, "center"),
    ("side", "Side", 10, "center"),
    ("price", "Limit Price ($)", 16, "right"),
    ("size", "Size (Tokens)", 16, "right"),
    ("notional_usd", "Notional (USD)", 18, "right"),
    ("address", "Ethereum Wallet Address", 44, "left"),
    ("source", "Telemetry Source", 36, "center"),
]

SECTION_4_COLS = [
    ("sr_no", "Sr. No.", 8, "center"),
    ("coin", "Asset", 10, "center"),
    ("side", "Risk Side", 12, "center"),
    ("price", "Liq Price ($)", 16, "right"),
    ("size", "Size (Tokens)", 16, "right"),
    ("notional_usd", "Estimated Notional ($)", 22, "right"),
    ("address", "Ethereum Wallet Address", 44, "left"),
]

SECTION_5_COLS = [
    ("sr_no", "Sr. No.", 8, "center"),
    ("coin", "Asset", 10, "center"),
    ("side", "Stop Type", 14, "center"),
    ("price", "Trigger Price ($)", 16, "right"),
    ("size", "Size (Tokens)", 16, "right"),
    ("notional_usd", "Estimated Notional ($)", 22, "right"),
    ("address", "Ethereum Wallet Address", 44, "left"),
]

SECTION_6_COLS = [
    ("sr_no", "Sr. No.", 8, "center"),
    ("date_label", "Date / Time", 18, "center"),
    ("coin", "Asset", 10, "center"),
    ("side", "Liquidation Side", 18, "center"),
    ("notional_usd", "Notional (USD)", 18, "right"),
    ("price", "Execution Price ($)", 18, "right"),
    ("market_impact", "Forced Market Impact", 22, "center"),
    ("wallet_address", "Ethereum Wallet Address", 44, "left"),
]

SECTION_7_COLS = [
    ("sr_no", "Sr. No.", 8, "center"),
    ("date_label", "Date / Time", 18, "center"),
    ("coin", "Asset", 10, "center"),
    ("side", "Trade Side", 14, "center"),
    ("notional_usd", "Notional (USD)", 18, "right"),
    ("price", "Execution Price ($)", 18, "right"),
    ("wallet_address", "Ethereum Wallet Address", 44, "left"),
]


def harvest_hyperdash_data() -> Dict[str, Any]:
    """Harvests flow feed intelligence and GraphQL L3/Liqs/Stops data."""
    t0 = time.time()
    log.info("Harvesting Hyperdash on-chain flow intelligence...")
    flow_intel = get_hyperdash_flow_intelligence()
    log.info(f"Gathered flow intelligence across {len(flow_intel.get('universe_asset_breakdown', {}))} assets.")

    client = HyperdashClient()
    l3_orders: List[Dict[str, Any]] = []
    top_liqs: List[Dict[str, Any]] = []
    top_stops: List[Dict[str, Any]] = []

    # 1. Fetch L3 Resting Whale Orders for BTC & ETH
    for coin in ("BTC", "ETH"):
        try:
            l2 = client.fetch_l2_book(coin)
            mid = l2.get("best_bid", 0.0)
            if mid > 0:
                orders = client.fetch_l3_orders(coin, mid * 0.98, mid * 1.02)
                for o in orders[:50]:  # Top 50 whale orders per coin
                    l3_orders.append({
                        "coin": coin,
                        "side": o.get("side"),
                        "price": o.get("price"),
                        "size": o.get("size"),
                        "notional_usd": o.get("notional_usd"),
                        "address": o.get("address"),
                        "source": o.get("source", "HYPERDASH_L3_RESTING"),
                    })
        except Exception as e:
            log.warning(f"Could not harvest L3 orders for {coin}: {e}")

    # 2. Fetch Top Liquidation Whales for BTC & ETH
    for coin in ("BTC", "ETH"):
        try:
            l2 = client.fetch_l2_book(coin)
            mid = l2.get("best_bid", 0.0)
            if mid > 0:
                liq_data = client.fetch_liquidations(coin, mid * 0.90, mid * 1.10)
                for w in liq_data.get("top_long_whales", []):
                    top_liqs.append({
                        "coin": coin,
                        "side": "LONG_AT_RISK",
                        "price": float(w.get("price", 0.0)),
                        "size": float(w.get("size", 0.0)),
                        "notional_usd": float(w.get("price", 0.0)) * float(w.get("size", 0.0)),
                        "address": w.get("address", ""),
                    })
                for w in liq_data.get("top_short_whales", []):
                    top_liqs.append({
                        "coin": coin,
                        "side": "SHORT_AT_RISK",
                        "price": float(w.get("price", 0.0)),
                        "size": float(w.get("size", 0.0)),
                        "notional_usd": float(w.get("price", 0.0)) * float(w.get("size", 0.0)),
                        "address": w.get("address", ""),
                    })
        except Exception as e:
            log.warning(f"Could not harvest liquidation levels for {coin}: {e}")

    # 3. Fetch Top Stop-Loss Whales for BTC & ETH
    for coin in ("BTC", "ETH"):
        try:
            l2 = client.fetch_l2_book(coin)
            mid = l2.get("best_bid", 0.0)
            if mid > 0:
                stop_data = client.fetch_stops(coin, mid * 0.90, mid * 1.10)
                for w in stop_data.get("top_buy_whales", []):
                    top_stops.append({
                        "coin": coin,
                        "side": "BUY_STOP",
                        "price": float(w.get("price", 0.0)),
                        "size": float(w.get("size", 0.0)),
                        "notional_usd": float(w.get("price", 0.0)) * float(w.get("size", 0.0)),
                        "address": w.get("address", ""),
                    })
                for w in stop_data.get("top_sell_whales", []):
                    top_stops.append({
                        "coin": coin,
                        "side": "SELL_STOP",
                        "price": float(w.get("price", 0.0)),
                        "size": float(w.get("size", 0.0)),
                        "notional_usd": float(w.get("price", 0.0)) * float(w.get("size", 0.0)),
                        "address": w.get("address", ""),
                    })
        except Exception as e:
            log.warning(f"Could not harvest stop levels for {coin}: {e}")

    # Sort orders and liqs by notional descending
    l3_orders.sort(key=lambda x: x.get("notional_usd", 0.0), reverse=True)
    top_liqs.sort(key=lambda x: x.get("notional_usd", 0.0), reverse=True)
    top_stops.sort(key=lambda x: x.get("notional_usd", 0.0), reverse=True)

    log.info(f"Hyperdash harvest completed in {time.time() - t0:.2f}s: "
             f"{len(l3_orders)} L3 orders, {len(top_liqs)} liqs, {len(top_stops)} stops.")

    return {
        "flow_intel": flow_intel,
        "l3_orders": l3_orders,
        "top_liqs": top_liqs,
        "top_stops": top_stops,
    }


def dump_hyperdash_to_parquet(data: dict, sheet_name: str = TARGET_SHEET_NAME) -> bool:
    rows = []
    ts_ist = datetime.datetime.now(IST_TZ).strftime("%Y-%m-%d %H:%M:%S IST")
    flow = data.get("flow_intel", {})

    # 1. Macro flow metrics
    sec1_metrics = [
        ("Total 24h Flow Volume (USD)", flow.get("total_volume_usd", 0.0)),
        ("Net Taker Flow Delta (USD)", flow.get("net_taker_delta_usd", 0.0)),
        ("Institutional Flow Bias", flow.get("flow_bias", "NEUTRAL")),
        ("Imminent Liquidations at Risk", flow.get("imminent_liqs_usd", 0.0)),
        ("Resting L3 Whale Wall Ratio", flow.get("whale_wall_ratio", 1.0)),
    ]
    for lbl, val in sec1_metrics:
        rows.append({
            "Section": "FLOW_METRICS",
            "Asset": "MACRO",
            "Type_or_Side": lbl,
            "Price": None,
            "Size": None,
            "Notional_USD": float(val) if isinstance(val, (int, float)) else None,
            "Detail": str(val),
            "Wallet_or_Address": None,
            "Timestamp_IST": ts_ist,
        })

    # 2. Universe Flow Breakdown
    for sym, uflow in flow.get("universe_asset_breakdown", {}).items():
        rows.append({
            "Section": "UNIVERSE_FLOW",
            "Asset": sym,
            "Type_or_Side": uflow.get("bias", "NEUTRAL"),
            "Price": uflow.get("price", 0.0),
            "Size": uflow.get("volume", 0.0),
            "Notional_USD": uflow.get("notional_usd", 0.0),
            "Detail": f"Delta: {uflow.get('delta_usd', 0.0):+,.0f}",
            "Wallet_or_Address": None,
            "Timestamp_IST": ts_ist,
        })

    # 3. L3 Orders
    for o in data.get("l3_orders", []):
        rows.append({
            "Section": "L3_RESTING_ORDER",
            "Asset": o.get("coin", "BTC"),
            "Type_or_Side": o.get("side", ""),
            "Price": o.get("price"),
            "Size": o.get("size"),
            "Notional_USD": o.get("notional_usd"),
            "Detail": o.get("source", "L3_ORDER"),
            "Wallet_or_Address": o.get("address", ""),
            "Timestamp_IST": ts_ist,
        })

    # 4. Top Liqs
    for l in data.get("top_liqs", []):
        rows.append({
            "Section": "TOP_LIQUIDATIONS",
            "Asset": l.get("coin", "BTC"),
            "Type_or_Side": l.get("side", ""),
            "Price": l.get("price"),
            "Size": l.get("size"),
            "Notional_USD": l.get("notional_usd"),
            "Detail": "AT_RISK_LIQ",
            "Wallet_or_Address": l.get("address", ""),
            "Timestamp_IST": ts_ist,
        })

    # 5. Top Stops
    for s in data.get("top_stops", []):
        rows.append({
            "Section": "TOP_STOPS",
            "Asset": s.get("coin", "BTC"),
            "Type_or_Side": s.get("side", ""),
            "Price": s.get("price"),
            "Size": s.get("size"),
            "Notional_USD": s.get("notional_usd"),
            "Detail": "TRIGGER_STOP",
            "Wallet_or_Address": s.get("address", ""),
            "Timestamp_IST": ts_ist,
        })

    meta = write_parquet_feed(sheet_name, rows)
    log.info(f"Successfully dumped {len(rows)} Hyperdash rows into Parquet feed '{sheet_name}': {meta.get('byte_size')} bytes in {meta.get('write_latency_ms', 0):.2f}ms.")
    return True


def main():
    parser = argparse.ArgumentParser(description="Hyperdash On-Chain Intelligence Pure-Parquet Dumper")
    parser.add_argument("--sheet", default=TARGET_SHEET_NAME, help="Target feed name")
    args = parser.parse_args()

    t_start = time.time()
    log.info(f"Starting Hyperdash On-Chain Intelligence module for feed '{args.sheet}'...")
    harvest_data = harvest_hyperdash_data()
    success = dump_hyperdash_to_parquet(harvest_data, sheet_name=args.sheet)

    if success:
        log.info(f"Hyperdash module completed successfully in {time.time() - t_start:.2f}s.")
        sys.exit(0)
    else:
        log.error("Hyperdash module failed.")
        sys.exit(1)


if __name__ == "__main__":
    main()
