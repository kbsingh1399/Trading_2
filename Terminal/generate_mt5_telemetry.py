#!/usr/bin/env python3
"""
Terminal/generate_mt5_telemetry.py
==================================
Extracts live broker telemetry, account state, and instrument quotes from MetaTrader 5:
- Account equity, balance, free margin, and leverage
- Exact floor cushion above 4,775.00 USD hard floor and 4,795.00 USD operating buffer
- Current risk capacity (number of concurrent positions allowed in $15-$25 envelope)
- Live Bid, Ask, Mid, and Spread in basis points (bps) across Universe perpetuals
- Spread Gate qualification (Crypto <= 25.0 bps, TradFi <= 5.0 bps)
- Persists to Data/telemetry/mt5_account_telemetry.json and Data/telemetry/live_snapshot_latest.json
"""

from __future__ import annotations

import datetime
import json
import logging
import os
import shutil
import pathlib
import sys
import time

ROOT_DIR = pathlib.Path(__file__).resolve().parents[1]
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

try:
    import MetaTrader5 as mt5
    MT5_AVAILABLE = True
except ImportError:
    mt5 = None
    MT5_AVAILABLE = False

from Terminal.MT5_Execution_Bridge import MT5ExecutionBridge
from Terminal.Asset_Universe import (
    COMPLETE_UNIVERSE,
    ALL_INDICES_16,
    ALL_COMMODITIES_14,
    ALL_FOREX_MAJORS_7,
    ALL_FOREX_CROSSES_25,
    ALL_58_CRYPTO_ASSETS,
    canonical_asset,
)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
log = logging.getLogger("MT5Telemetry")

TELEMETRY_DIR = ROOT_DIR / "Data" / "telemetry"
TELEMETRY_DIR.mkdir(parents=True, exist_ok=True)
TELEMETRY_PATH = TELEMETRY_DIR / "mt5_account_telemetry.json"
SNAPSHOT_PATH = TELEMETRY_DIR / "live_snapshot_latest.json"

HARD_FLOOR_USD = 4775.00
OPERATING_BUFFER_USD = 4795.00
BASE_RISK_USD = 15.00
MAX_RISK_USD = 25.00

PRIMARY_18_ASSETS = list(ALL_58_CRYPTO_ASSETS)

TRADFI_CFD_ASSETS = list(
    ALL_INDICES_16 + ALL_COMMODITIES_14 + ALL_FOREX_MAJORS_7 + ALL_FOREX_CROSSES_25
)


def harvest_mt5_telemetry() -> dict:
    t0 = time.perf_counter()
    if not MT5_AVAILABLE:
        log.error("MetaTrader5 python package not available.")
        return {"error": "mt5_not_available"}

    bridge = MT5ExecutionBridge()
    if not bridge.initialized:
        log.error("Failed to connect to MetaTrader 5.")
        return {"error": "mt5_connect_failed"}

    account_summary = bridge.get_account_summary()
    open_positions = bridge.get_open_positions()
    pending_orders = bridge.get_pending_orders()

    equity = account_summary.get("equity_usd", 0.0)
    balance = account_summary.get("balance_usd", 0.0)
    margin_free = account_summary.get("margin_free_usd", 0.0)

    hard_cushion = round(equity - HARD_FLOOR_USD, 2)
    operating_cushion = round(equity - OPERATING_BUFFER_USD, 2)

    # Dynamic capacity sizing (Operator Mandate: Max 4 running filled positions across orthogonal clusters)
    # Resting limit orders do NOT consume slots until filled.
    # Risk budget per trade is strictly 12.00–15.00 USD nominal, preserving buffer.
    if operating_cushion <= 0:
        max_positions = 0
        status_msg = "CAPITAL_PRESERVATION_HALT: Operating buffer breached"
    elif operating_cushion < BASE_RISK_USD:
        max_positions = 1
        status_msg = f"DEFENSIVE_MODE: Cushion ({operating_cushion} USD) < Base Risk ({BASE_RISK_USD} USD)"
    elif operating_cushion < (BASE_RISK_USD * 2):
        max_positions = 1
        status_msg = "NOMINAL_DEFENSE: Max 1 initial filled position active (4 running slots authorized upon Early-BE)"
    elif operating_cushion < (BASE_RISK_USD * 3):
        max_positions = 2
        status_msg = "STANDARD_OPERATION: Max 2 filled positions active (4 running slots authorized upon Early-BE)"
    else:
        max_positions = 4
        status_msg = "FULL_CAPACITY: Max 4 running filled positions authorized across orthogonal clusters"

    # Instrument quotes & spreads
    instrument_quotes = {}
    
    # Process Crypto (threshold <= 25.0 bps) and TradFi CFDs (threshold <= 5.0 bps)
    asset_groups = [
        (PRIMARY_18_ASSETS, 25.0, "CRYPTO"),
        (TRADFI_CFD_ASSETS, 5.0, "TRADFI"),
    ]

    for asset_list, max_spread_bps, asset_class in asset_groups:
        for asset in asset_list:
            broker_sym = bridge.resolve_symbol(asset)
            if not broker_sym:
                instrument_quotes[asset] = {
                    "broker_symbol": None,
                    "asset_class": asset_class,
                    "status": "UNRESOLVED",
                }
                continue

            quote = bridge.get_symbol_price(broker_sym)
            if not quote:
                instrument_quotes[asset] = {
                    "broker_symbol": broker_sym,
                    "asset_class": asset_class,
                    "status": "NO_QUOTE",
                }
                continue

            bid = quote["bid"]
            ask = quote["ask"]
            mid = (bid + ask) / 2.0 if (bid + ask) > 0 else 0.0

            # Edge-case: Crossed book detection (bid >= ask or negative spread)
            if bid >= ask or mid <= 0:
                instrument_quotes[asset] = {
                    "broker_symbol": broker_sym,
                    "asset_class": asset_class,
                    "bid": bid,
                    "ask": ask,
                    "mid": mid,
                    "spread_points": quote.get("spread", 0),
                    "spread_bps": 0.0,
                    "spread_eligible": False,
                    "contract_size": quote.get("contract_size", 1.0),
                    "point": quote.get("point", 0.01),
                    "status": "CROSSED_BOOK_ANOMALY",
                }
                continue

            spread_pts = quote["spread"]
            spread_bps = round(((ask - bid) / mid) * 10000.0, 2)

            # Eligibility threshold by asset class
            spread_eligible = spread_bps <= max_spread_bps

            # Edge-case: Check for stale weekend/closed market tick
            tick_age = quote.get("broker_tick_age")
            is_stale_market = (tick_age is not None and tick_age > 7200)

            if is_stale_market:
                status_str = "MARKET_CLOSED_OR_STALE"
                spread_eligible = False
            elif spread_eligible:
                status_str = "PASS"
            else:
                status_str = "SPREAD_DISQUALIFIED"

            instrument_quotes[asset] = {
                "broker_symbol": broker_sym,
                "asset_class": asset_class,
                "bid": bid,
                "ask": ask,
                "mid": mid,
                "spread_points": spread_pts,
                "spread_bps": spread_bps,
                "spread_eligible": spread_eligible,
                "contract_size": quote.get("contract_size", 1.0),
                "point": quote.get("point", 0.01),
                "tick_size": quote.get("tick_size", 0.01),
                "status": status_str,
            }

    now_utc = datetime.datetime.now(datetime.timezone.utc).isoformat()
    duration_sec = round(time.perf_counter() - t0, 3)

    now_epoch = time.time()
    telemetry_payload = {
        "as_of_epoch": now_epoch,
        "generation_id": f"gen_{int(now_epoch * 1000)}",
        "snapshot_status": "LIVE_OBSERVATION",
        "timestamp_utc": now_utc,
        "harvest_duration_seconds": duration_sec,
        "account": {
            "login": account_summary.get("login"),
            "company": account_summary.get("company"),
            "currency": account_summary.get("currency"),
            "balance_usd": balance,
            "equity_usd": equity,
            "margin_free_usd": margin_free,
            "hard_floor_usd": HARD_FLOOR_USD,
            "operating_buffer_usd": OPERATING_BUFFER_USD,
            "hard_floor_cushion_usd": hard_cushion,
            "operating_buffer_cushion_usd": operating_cushion,
            "capacity_status": status_msg,
            "max_concurrent_positions": max_positions,
            "base_risk_usd": BASE_RISK_USD,
            "max_risk_usd": MAX_RISK_USD,
        },
        "open_positions_count": len(open_positions),
        "open_positions": open_positions,
        "pending_orders_count": len(pending_orders),
        "pending_orders": pending_orders,
        "universe_quotes": instrument_quotes,
    }

    # Atomic write to JSON
    temp_path = TELEMETRY_PATH.with_suffix(".tmp")
    with open(temp_path, "w", encoding="utf-8") as f:
        json.dump(telemetry_payload, f, indent=2)
    os.replace(temp_path, TELEMETRY_PATH)

    # Also mirror to live_snapshot_latest.json in both Data/telemetry and docs/telemetry
    temp_snap = SNAPSHOT_PATH.with_suffix(".tmp")
    with open(temp_snap, "w", encoding="utf-8") as f:
        json.dump(telemetry_payload, f, indent=2)
    os.replace(temp_snap, SNAPSHOT_PATH)

    docs_snap = ROOT_DIR / "docs" / "telemetry" / "live_snapshot_latest.json"
    try:
        docs_snap.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(SNAPSHOT_PATH, docs_snap)
    except Exception as e:
        log.warning(f"Could not mirror to docs/telemetry: {e}")

    log.info(f"MT5 Telemetry harvested in {duration_sec}s. Equity: {equity} USD | Cushion: {operating_cushion} USD | Open: {len(open_positions)}")
    return telemetry_payload


if __name__ == "__main__":
    result = harvest_mt5_telemetry()
    print(f"Summary: Equity={result['account']['equity_usd']} USD, Cushion={result['account']['operating_buffer_cushion_usd']} USD, MaxPositions={result['account']['max_concurrent_positions']}")
