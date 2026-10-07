"""Offline regression gates for observed-only telemetry and Hyperdash adapters."""
from __future__ import annotations

import copy
import json
import time

import pytest

from Terminal.Api_Client import HyperdashClient
from Terminal.Telemetry_Provenance import (
    validate_observed_snapshot, verified_wallet_block, verified_wallet_l3,
)
from Terminal.Data_Factory import ZeroCostDataFactory

NOW = 1791408000.0


def test_old_minute_snapshot_is_rejected_by_publisher():
    with open("docs/telemetry/live_snapshot_latest.json", encoding="utf-8") as stream:
        older = json.load(stream)
    if older.get("protocol") == "omni.telemetry.v2":
        assert not validate_observed_snapshot(older)
    good = {"protocol": "omni.telemetry.v3.observed_only",
            "trade_authorization": "DENIED_UNVERIFIED_ORDERFLOW",
            "assets_matrix_24": {str(i): {"quotes": {"quote_source": "UNAVAILABLE"},
                "orderbook_live_depth": {"whale_walls_l3": []},
                "structural_stop_clusters": {"source": "UNAVAILABLE"},
                "reconstructed_liquidations": {"source": "UNAVAILABLE"},
                "pioneer_microstructure_eval": {"confluence_trade_setup": None}}
                for i in range(24)}}
    assert validate_observed_snapshot(good)
    poisoned = copy.deepcopy(good)
    poisoned["assets_matrix_24"]["0"]["orderbook_live_depth"]["whale_walls_l3"] = [{"price": 1}]
    assert not validate_observed_snapshot(poisoned)
    poisoned = copy.deepcopy(good)
    poisoned["assets_matrix_24"]["0"]["structural_stop_clusters"]["source"] = "MODEL"
    assert not validate_observed_snapshot(poisoned)


def test_model_and_anonymous_l2_are_rejected_as_wallet_data():
    factory = ZeroCostDataFactory(["BTC"], clock=lambda: NOW)
    factory.ingest_book("BTC", {"ts": NOW, "best_bid": 100, "best_ask": 101,
        "bids": [{"price": 100, "size": 2000}],
        "asks": [{"price": 101, "size": 2000}]})
    data = factory.payload("BTC", NOW)
    assert data["l3_orders"] == []
    assert verified_wallet_l3(data, NOW) == []
    assert verified_wallet_block(data, "observed_stops", NOW) is None
    data["observed_stops"] = {"kind": "OBSERVED_STOP_ORDERS",
        "coverage": "SYNTHETIC_STRUCTURAL_MODEL", "bands": [{"address": "0xabc"}]}
    data["sources"]["wallet_risk"] = {"provider": "HYPERLIQUID_PUBLIC_INFO",
        "coverage": "SAMPLED_WALLETS", "observed_at": NOW}
    assert verified_wallet_block(data, "observed_stops", NOW) is None


def test_hyperdash_schema_missing_is_not_observed_zero(monkeypatch):
    client = HyperdashClient()
    monkeypatch.setattr(client, "_resolve_coin", lambda c: c)
    monkeypatch.setattr(client, "_post_json", lambda *args: {"data": {"analytics": {}}})
    with pytest.raises(RuntimeError, match="orderbookSnapshotFiltered"):
        client.fetch_l3_orders("BTC", 80, 120)
    with pytest.raises(RuntimeError, match="stopOrderLevels"):
        client.fetch_stops("BTC", 80, 120)
    with pytest.raises(RuntimeError, match="liquidationLevels"):
        client.fetch_liquidations("BTC", 80, 120)


def test_hyperdash_analytics_are_unverified_and_empty_hist_is_not_zero(monkeypatch):
    client = HyperdashClient()
    monkeypatch.setattr(client, "_resolve_coin", lambda c: c)
    monkeypatch.setattr(client, "_post_json", lambda url, payload: {"data": {"analytics": {
        "stopOrderLevels": {"bands": [{"minPrice": 80, "maxPrice": 81,
            "historicalData": []}]},
        "liquidationLevels": {"bands": []}}}})
    stop = client.fetch_stops("BTC", 80, 120)
    liq = client.fetch_liquidations("BTC", 80, 120)
    assert stop["kind"] == "UNVERIFIED_STOP_LANDSCAPE"
    assert liq["kind"] == "UNVERIFIED_BAND_LANDSCAPE"
    assert stop["bands"] == [] and stop["total_buy_size"] is None
    assert liq["total_long_size"] is None
