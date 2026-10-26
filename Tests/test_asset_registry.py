#!/usr/bin/env python3
"""
Tests/test_asset_registry.py
============================
Unit tests for Terminal/Data_Factory/asset_registry.py
"""

import pathlib
import sys
import pytest

ROOT_DIR = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT_DIR / "Terminal" / "Data_Factory"))

from asset_registry import AssetRegistry, asset_registry


def test_asset_registry_loading():
    """Verifies that the catalog is properly loaded with expected asset counts."""
    assert len(asset_registry.assets) >= 38
    assert "BTC" in asset_registry.assets
    assert "EURUSD" in asset_registry.assets
    assert "XAUT" in asset_registry.assets
    assert "SP500" in asset_registry.assets


def test_canonical_alias_resolution():
    """Verifies canonical symbol resolution for aliases and venue identifiers."""
    assert asset_registry.canonical("btc") == "BTC"
    assert asset_registry.canonical("Bitcoin") == "BTC"
    assert asset_registry.canonical("BTCUSDT") == "BTC"
    assert asset_registry.canonical("XAUUSD.pi") == "XAUUSD"
    assert asset_registry.canonical("xyz:GOLD") == "XAUUSD" or asset_registry.canonical("xyz:GOLD") in ["XAUUSD", "XAUT", "PAXG"]
    assert asset_registry.canonical("Euro / US Dollar") == "EURUSD"
    assert asset_registry.canonical("EUR/USD") == "EURUSD"
    assert asset_registry.canonical("Tether Gold") == "XAUT"


def test_get_assets_for_collector():
    """Verifies collector-specific symbol filtering."""
    liq_map_assets = asset_registry.get_assets_for_collector("8_Exchange_Liquidation_Map_1D")
    assert "BTC" in liq_map_assets
    assert "EURUSD" in liq_map_assets
    assert "XAUT" in liq_map_assets
    assert len(liq_map_assets) >= 23

    spot_netflow_assets = asset_registry.get_assets_for_collector("2_Spot_Netflow_S")
    assert "BTC" in spot_netflow_assets
    assert "XAUT" in spot_netflow_assets

    tech_assets = asset_registry.get_assets_for_collector("11_Technical")
    assert len(tech_assets) >= 38


def test_expected_title_tokens():
    """Verifies expected title tokens for chart verification."""
    btc_tokens = asset_registry.get_expected_title_tokens("BTC")
    assert "BTC" in btc_tokens or "Bitcoin" in btc_tokens

    eur_tokens = asset_registry.get_expected_title_tokens("EURUSD")
    assert any("EUR" in tok for tok in eur_tokens)

    xaut_tokens = asset_registry.get_expected_title_tokens("XAUT")
    assert any("Gold" in tok or "XAUT" in tok for tok in xaut_tokens)


def test_reference_price_resolution():
    """Verifies reference price fallback and caching."""
    btc_price = asset_registry.get_reference_price("BTC")
    assert btc_price > 10000.0  # Real or realistic fallback

    eur_price = asset_registry.get_reference_price("EURUSD")
    assert 0.8 < eur_price < 2.0  # EURUSD realistic bounds

    xaut_price = asset_registry.get_reference_price("XAUT")
    assert 2000.0 < xaut_price < 6000.0  # Gold price bounds


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
