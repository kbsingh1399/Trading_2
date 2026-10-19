import os
import sys

sys.path.insert(0, os.path.dirname(__file__))

import pytest  # noqa: E402

from remediation_r2 import (  # noqa: E402
    quote_age_or_none, execution_status, orderbook_spread, within_window,
    harvest_key, sheet_guard, FRESHNESS_MAX_S,
)


def test_missing_quote_age_is_none_not_fresh():
    assert quote_age_or_none(None) is None             # was 0.5 s default
    assert quote_age_or_none("0.5") == 0.5            # explicit value kept
    assert quote_age_or_none(-1.0) is None


def test_execution_status_fail_closed():
    assert execution_status(0.0, 0.0, 0.1) == ("MISSING QUOTE", "RED")
    assert execution_status(100.0, 100.0, 0.1) == ("INACTIVE", "AMBER")   # locked
    assert execution_status(81722.0, 81738.0, None) == ("INACTIVE", "AMBER")
    assert execution_status(81722.0, 81738.0, 6.0) == ("INACTIVE", "AMBER")
    assert execution_status(81722.0, 81738.0, 0.1) == ("ACTIVE EXECUTION", "GREEN")


def test_orderbook_spread_keeps_five_second_gate():
    assert FRESHNESS_MAX_S == 5.0
    assert orderbook_spread(81722.0, 81738.0, 60.0) is None   # was accepted under 60 s
    assert orderbook_spread(81722.0, 81738.0, None) is None
    assert round(orderbook_spread(81722.0, 81738.0, 4.9), 2) == 1.96


def test_within_window():
    assert within_window("3 hours ago") is True
    assert within_window("2 days ago") is False
    assert within_window("Just now") is False
    assert within_window(None) is False


def test_harvest_key_dedupes_same_page_read_twice():
    row = {"time": "3 hours ago", "tx_hash": "0x" + "a" * 64, "from_address": "0x" + "b" * 40,
           "to_address": "0x" + "c" * 40, "token_symbol": "USDC",
           "token_value": "1,000", "usd_value": "$1.0M"}
    epoch = 1_800_000_000.0
    assert harvest_key(row, epoch) == harvest_key(dict(row), epoch)
    assert harvest_key(row, epoch) != harvest_key(dict(row, tx_hash="0x" + "d" * 64), epoch)


def test_harvest_key_rejects_unparseable_time():
    assert harvest_key({"time": "Just now", "tx_hash": "0x1"}, 1_800_000_000.0) is None


def test_sheet_guard_detects_renamed_sheet():
    required = ["Telemetry_System_State", "Arkham_Transfers_100K", "Hyperdash_Flow_Feed"]
    actual = ["Telemetry_System_State", "Arkham_Transfers_100k", "Hyperdash_Flow_Feed"]
    missing, unexpected = sheet_guard(actual, required)
    assert missing == ["Arkham_Transfers_100K"]
    assert unexpected == ["Arkham_Transfers_100k"]


def test_sheet_guard_clean_match():
    assert sheet_guard(["A", "B"], ["A", "B"]) == ([], [])
