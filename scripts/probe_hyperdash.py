#!/usr/bin/env python3
"""Read-only local Hyperdash API probe (no trading, no cached data).

Run on a machine that can reach Hyperdash/Hyperliquid:
    python scripts/probe_hyperdash.py BTC
The probe reports provider receipt times and the latest analytics sample time.
It does NOT certify chart methodology, full-market stop coverage, or L3 events.
"""
from __future__ import annotations

import json
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from Terminal.Api_Client import HyperdashClient  # noqa: E402


def main(coin: str):
    client = HyperdashClient(timeout=7)
    book = client.fetch_l2_book(coin)
    bid, ask = book["best_bid"], book["best_ask"]
    if not (0 < bid < ask):
        raise RuntimeError("Hyperliquid book crossed or missing; refusing comparison")
    mid = (bid + ask) / 2
    results = {"coin": coin, "retrieved_utc": datetime.now(timezone.utc).isoformat(),
               "l2": {"venue": "HYPERLIQUID", "best_bid": bid, "best_ask": ask,
                      "timestamp": book.get("timestamp")},
               "limitations": ["Hyperdash GraphQL endpoint/schema cannot be verified by an offline run",
                               "Wallet-attributed snapshots do not prove full matching-engine L3",
                               "Stop and liquidation chart computation/coverage remains unverified"]}
    endpoints = {
        "wallet_attributed_orders": lambda: client.fetch_l3_orders(coin, mid * .98, mid * 1.02),
        "stop_landscape": lambda: client.fetch_stops(coin, mid * .8, mid * 1.2),
        "liquidation_landscape": lambda: client.fetch_liquidations(coin, mid * .8, mid * 1.2),
    }
    for name, call in endpoints.items():
        try:
            response = call()
            if isinstance(response, list):
                results[name] = {"provider": "HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT",
                                 "coverage": "PRICE_WINDOW_WALLET_ATTRIBUTED_NO_ORDER_ID",
                                 "rows": len(response),
                                 "sample": response[:2]}
            else:
                bands = response.get("bands") or []
                results[name] = {"provider": response.get("source"), "kind": response.get("kind"),
                                 "received_at": response.get("received_at"),
                                 "last_band_sample_at": max((b.get("observed_at") or 0 for b in bands), default=None),
                                 "band_count": len(bands), "size_unit": response.get("size_unit"),
                                 "sample": bands[:2]}
        except Exception as exc:
            results[name] = {"status": "UNAVAILABLE", "error": str(exc)}
    print(json.dumps(results, indent=2, default=str, allow_nan=False))
    return 0 if all("status" not in results[name] for name in endpoints) else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1].upper() if len(sys.argv) > 1 else "BTC"))
