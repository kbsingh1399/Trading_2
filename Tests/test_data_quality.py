import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "Terminal", "Data_Factory")))

import pytest

from data_quality import (
    status_color,
    parse_time_ago_seconds,
    is_within_24h,
    parse_chain_from_url_or_text,
    parse_whale_change_pct,
    long_short_ratio,
    exchange_basis_bps,
    extract_largest_holding,
    dedup_arkham_transfers,
    WHALE_THRESHOLDS,
)


# ---- Status color & highlighting
def test_denied_shows_red_not_green():
    # Defect 1: DENIED_UNVERIFIED_ORDERFLOW contains VERIFIED, must be RED
    assert status_color("DENIED_UNVERIFIED_ORDERFLOW") == "RED"
    assert status_color("DENIED") == "RED"
    assert status_color("UNVERIFIED") == "RED"
    assert status_color("FAILED") == "RED"
    assert status_color("HARD FLOOR") == "RED"
    assert status_color("VIOLATION") == "RED"
    assert status_color("OFFLINE (500)") == "RED"


def test_status_color_green_tokens():
    assert status_color("ACTIVE") == "GREEN"
    assert status_color("VERIFIED") == "GREEN"
    assert status_color("CONFIRMED") == "GREEN"
    assert status_color("SAFE") == "GREEN"
    assert status_color("NOMINAL") == "GREEN"
    assert status_color("COMPLIANT") == "GREEN"


def test_status_color_amber_tokens():
    assert status_color("MONITORED") == "AMBER"
    assert status_color("STANDBY") == "AMBER"
    assert status_color("CALIBRATING") == "AMBER"
    assert status_color("WARNING") == "AMBER"


def test_status_color_none_or_na():
    assert status_color(None) is None
    assert status_color("") is None
    assert status_color("N/A") is None


# ---- Time ago parsing (24h)
def test_parse_time_ago_seconds():
    assert parse_time_ago_seconds("30s") == 30.0
    assert parse_time_ago_seconds("15m ago") == 900.0
    assert parse_time_ago_seconds("2h ago") == 7200.0
    assert parse_time_ago_seconds("1 day ago") == 86400.0
    assert parse_time_ago_seconds("invalid") is None
    assert parse_time_ago_seconds(None) is None


def test_is_within_24h():
    assert is_within_24h("2h ago") is True
    assert is_within_24h("23h ago") is True
    assert is_within_24h("25h ago") is False
    assert is_within_24h("2 days ago") is False


# ---- Chain parsing
def test_parse_chain_badges():
    # Defect 8: avoid 'database' matching 'base'
    assert parse_chain_from_url_or_text("https://example.com/icons/base.svg") == "Base"
    assert parse_chain_from_url_or_text("https://database.org/icon.png") == "Unknown"
    assert parse_chain_from_url_or_text("https://arkham.com/chains/ethereum") == "Ethereum"
    assert parse_chain_from_url_or_text("Solana") == "Solana"
    assert parse_chain_from_url_or_text("tron_trx") == "Tron"


# ---- Whale change percentage
def test_parse_whale_change_pct():
    # Defect 9: 0.4% must not become 40.00%
    assert parse_whale_change_pct("0.4%") == pytest.approx(0.004)
    assert parse_whale_change_pct(0.4) == pytest.approx(0.004)
    assert parse_whale_change_pct("-2.5%") == pytest.approx(-0.025)
    assert parse_whale_change_pct("-2.5") == pytest.approx(-0.025)
    assert parse_whale_change_pct("N/A") is None
    assert parse_whale_change_pct(None) is None


# ---- Long/Short ratio
def test_long_short_ratio():
    # Defect 10: short side 0 returns None, not USD amount
    assert long_short_ratio(100.0, 50.0) == 2.0
    assert long_short_ratio(100.0, 0.0) is None
    assert long_short_ratio(100.0, -10.0) is None
    assert long_short_ratio(None, 50.0) is None


# ---- Exchange basis bps
def test_exchange_basis_bps():
    # Defect 12: missing index returns None, not 0.0
    assert exchange_basis_bps(100.0, 100.0) == 0.0
    assert exchange_basis_bps(101.0, 100.0) == pytest.approx(100.0)
    assert exchange_basis_bps(100.0, None) is None
    assert exchange_basis_bps(None, 100.0) is None
    assert exchange_basis_bps(100.0, 0.0) is None


# ---- Largest holding
def test_extract_largest_holding_list():
    # Defect 14: unsorted list picks true max
    holdings = [
        {"symbol": "ETH", "value_usd": 500.0, "amount": 0.2},
        {"symbol": "BTC", "value_usd": 10000.0, "amount": 0.15},
        {"symbol": "SOL", "value_usd": 200.0, "amount": 1.0},
    ]
    sym, amt = extract_largest_holding(holdings)
    assert sym == "BTC"


def test_extract_largest_holding_dict():
    holdings = {
        "ETH": {"usd_value": 500.0, "amount": 0.2},
        "BTC": {"usd_value": 10000.0, "amount": 0.15},
    }
    sym, amt = extract_largest_holding(holdings)
    assert sym == "BTC"


# ---- Deduplication
def test_dedup_arkham_transfers():
    # Defect 6: deduplicate
    transfers = [
        {"tx_hash": "0xabc", "token": "BTC", "usd_val": 100000, "from_addr": "0x1", "to_addr": "0x2"},
        {"tx_hash": "0xabc", "token": "BTC", "usd_val": 100000, "from_addr": "0x1", "to_addr": "0x2"},
        {"tx_hash": "0xdef", "token": "ETH", "usd_val": 200000, "from_addr": "0x3", "to_addr": "0x4"},
    ]
    deduped = dedup_arkham_transfers(transfers)
    assert len(deduped) == 2
    assert deduped[0]["tx_hash"] == "0xabc"
    assert deduped[1]["tx_hash"] == "0xdef"


# ---- Whale thresholds
def test_whale_thresholds():
    assert WHALE_THRESHOLDS["ARKHAM_MIN_USD"] == 100000.0
    assert WHALE_THRESHOLDS["RESTING_WALL_MIN_USD"] == 100000.0
