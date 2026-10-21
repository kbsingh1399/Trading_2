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
from Terminal.Asset_Universe import COMPLETE_UNIVERSE, canonical_asset

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

PRIMARY_18_ASSETS = [
    "BTC", "ETH", "XRP", "SOL", "BNB", "DOGE", "ADA", "TRX", "LINK",
    "AVAX", "SUI", "NEAR", "DOT", "LTC", "BCH", "APT", "OP", "ARB",
]


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

    # Dynamic capacity sizing
    # Under hard floor defense, risk budget is capped by operating cushion
    if operating_cushion <= 0:
        max_positions = 0
        status_msg = "CAPITAL_PRESERVATION_HALT: Operating buffer breached"
    elif operating_cushion < BASE_RISK_USD:
        max_positions = 1
        status_msg = f"DEFENSIVE_MODE: Cushion ({operating_cushion} USD) < Base Risk ({BASE_RISK_USD} USD)"
    elif operating_cushion < (BASE_RISK_USD * 2):
        max_positions = 1
        status_msg = "NOMINAL_DEFENSE: Max 1 position active"
    elif operating_cushion < (BASE_RISK_USD * 3):
        max_positions = 2
        status_msg = "STANDARD_OPERATION: Max 2 positions active"
    else:
        max_positions = 3
        status_msg = "FULL_CAPACITY: Max 3 positions active"

    # Instrument quotes & spreads
    instrument_quotes = {}
    for asset in PRIMARY_18_ASSETS:
        broker_sym = bridge.resolve_symbol(asset)
        if not broker_sym:
            instrument_quotes[asset] = {
                "broker_symbol": None,
                "status": "UNRESOLVED",
            }
            continue

        quote = bridge.get_symbol_price(broker_sym)
        if not quote:
            instrument_quotes[asset] = {
                "broker_symbol": broker_sym,
                "status": "NO_QUOTE",
            }
            continue

        bid = quote["bid"]
        ask = quote["ask"]
        mid = (bid + ask) / 2.0 if (bid + ask) > 0 else 0.0
        spread_pts = quote["spread"]
        spread_bps = round(((ask - bid) / mid) * 10000.0, 2) if mid > 0 else 0.0

        # Eligibility threshold: Crypto <= 25.0 bps
        spread_eligible = spread_bps <= 25.0

        instrument_quotes[asset] = {
            "broker_symbol": broker_sym,
            "bid": bid,
            "ask": ask,
            "mid": mid,
            "spread_points": spread_pts,
            "spread_bps": spread_bps,
            "spread_eligible": spread_eligible,
            "contract_size": quote.get("contract_size", 1.0),
            "point": quote.get("point", 0.01),
            "status": "PASS" if spread_eligible else "SPREAD_DISQUALIFIED",
        }

    now_utc = datetime.datetime.now(datetime.timezone.utc).isoformat()
    duration_sec = round(time.perf_counter() - t0, 3)

    telemetry_payload = {
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

    # Also mirror to live_snapshot_latest.json
    temp_snap = SNAPSHOT_PATH.with_suffix(".tmp")
    with open(temp_snap, "w", encoding="utf-8") as f:
        json.dump(telemetry_payload, f, indent=2)
    os.replace(temp_snap, SNAPSHOT_PATH)

    log.info(f"MT5 Telemetry harvested in {duration_sec}s. Equity: {equity} USD | Cushion: {operating_cushion} USD | Open: {len(open_positions)}")
    return telemetry_payload


if __name__ == "__main__":
    result = harvest_mt5_telemetry()
    print(f"Summary: Equity={result['account']['equity_usd']} USD, Cushion={result['account']['operating_buffer_cushion_usd']} USD, MaxPositions={result['account']['max_concurrent_positions']}")
