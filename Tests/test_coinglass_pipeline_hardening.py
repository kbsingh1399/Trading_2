#!/usr/bin/env python3
"""
Tests/test_coinglass_pipeline_hardening.py
=========================================
Hermetic, offline unit tests for the CoinGlass Data Pipeline hardening rules
addressing Arena Cycles 187, 188, 189, 190, 191, 192, 193, and 194:
1. First-token exact matching (Q1: eliminates pair collisions like SOL/ETH matching ETH, eliminates STOP/BLINK/ARBITRUM, fails closed on empty).
2. Grid-derived price tolerance (Q2: 2.5 bps, ~20 USD at 80k, guarantees levels 56 apart never merge when executed through matcher).
3. Stacked-order duration tie-break & tied duration reporting (Q2: bijective 1-to-1 matching, reports tied durations as ambiguous).
4. Partial-fill & notional-growth handling (Q2: maintains track_id across reductions and expansions).
5. Unique new-order IDs (F102: guarantees two orders at identical price and side never share identical track_id).
6. Continuous partial-fill rule (F103: continuous fill percentage across all reductions with zero cliff threshold).
7. Complete lost-orders schema with microstructure attribution (F104: FILLED_PRICE_CROSSED vs CANCELED_UNTOUCHED).
8. Shipped sign persistence verification (F107: imports and validates evaluate_sign_persistence from Terminal.Data_Factory.generate_telemetry_snapshot).
"""
import os
import pathlib
import sys

# Multi-path discovery ensuring imports succeed in any environment (pytest, repo-root, subfolder, offline sandbox)
_CANDIDATE_ROOTS = [
    pathlib.Path(__file__).resolve().parents[1],
    pathlib.Path.cwd(),
    pathlib.Path.cwd().parent,
]
for _root in _CANDIDATE_ROOTS:
    if (_root / "Terminal").exists() and str(_root) not in sys.path:
        sys.path.insert(0, str(_root))

from Terminal.Data_Factory.coinglass_whale_orders_harvester import (
    match_heading_token,
    match_cross_cycle_orders
)
from Terminal.Data_Factory.whale_persistence import evaluate_sign_persistence


# --- Test Cases ---

def test_q1_first_token_matching():
    """Verify Q1: First-token exact heading matching eliminates pair & substring collisions."""
    ok, _ = match_heading_token("BTC Whale Orders & Large Trades", "BTC")
    assert ok is True
    ok, _ = match_heading_token("BTCUSDT Whale Orders", "BTC")
    assert ok is True
    ok, _ = match_heading_token("ADA Large Orders", "ADA")
    assert ok is True

    # Pair collision: SOL/ETH Whale Orders must NOT match ETH
    ok, err = match_heading_token("SOL/ETH Whale Orders", "ETH")
    assert ok is False
    assert "First-token mismatch" in err

    # Substring collisions that MUST fail
    ok, err = match_heading_token("STOP ORDERS SUMMARY", "OP")
    assert ok is False
    assert "First-token mismatch" in err

    ok, err = match_heading_token("BLINK TRADING POOL", "LINK")
    assert ok is False
    assert "First-token mismatch" in err

    ok, err = match_heading_token("ARBITRUM ECOSYSTEM STATS", "ARB")
    assert ok is False
    assert "First-token mismatch" in err

    # Fail closed on empty/none
    ok, err = match_heading_token("", "BTC")
    assert ok is False
    assert "missing or empty" in err

    ok, err = match_heading_token(None, "BTC")
    assert ok is False
    assert "missing or empty" in err


def test_q2_grid_tolerance_non_merging():
    """Verify Q2: Tight 2.5 bps grid tolerance never merges levels 56 apart at 82,500 when passed to matcher."""
    # Case A: Level 56 USD apart (82500 vs 82444) -> 6.79 bps difference > 2.5 bps tolerance (20.625 USD)
    prev_orders = [
        {"track_id": "BTC_BUY_82500_RESTING", "side": "BUY", "price": 82500.0, "notional_usd": 5000000.0, "duration_seconds": 3600.0}
    ]
    cur_orders = [
        {"side": "BUY", "price": 82444.0, "notional_usd": 5000000.0, "duration_seconds": 3780.0}
    ]
    matched, report = match_cross_cycle_orders(cur_orders, prev_orders, cycle_interval_s=180.0, asset="BTC")
    # Must NOT merge: cur_orders[0] becomes NEW_ORDER with a fresh track_id
    assert matched[0]["match_status"] == "NEW_ORDER"
    assert matched[0]["track_id"] != "BTC_BUY_82500_RESTING"
    # Old order is lost
    assert report["lost_orders_count"] == 1
    assert report["lost_orders"][0]["track_id"] == "BTC_BUY_82500_RESTING"

    # Case B: Level within 2.5 bps tolerance (82500 vs 82510 -> 1.21 bps difference < 2.5 bps)
    cur_in_tol = [
        {"side": "BUY", "price": 82510.0, "notional_usd": 5000000.0, "duration_seconds": 3780.0}
    ]
    matched_tol, report_tol = match_cross_cycle_orders(cur_in_tol, prev_orders, cycle_interval_s=180.0, asset="BTC")
    # Must match with accepted price drift
    assert matched_tol[0]["match_status"] == "PRICE_DRIFT_ACCEPTED"
    assert matched_tol[0]["track_id"] == "BTC_BUY_82500_RESTING"
    assert report_tol["lost_orders_count"] == 0


def test_q2_stacked_orders_duration_continuity_and_ties():
    """Verify Q2: Bijective matching and tied duration reporting."""
    prev_orders = [
        {"track_id": "BTC_BUY_80000_ORDER_A", "side": "BUY", "price": 80000.0, "notional_usd": 5000000.0, "duration_seconds": 19800.0},
        {"track_id": "BTC_BUY_80000_ORDER_B", "side": "BUY", "price": 80000.0, "notional_usd": 5000000.0, "duration_seconds": 3600.0},
    ]

    # DOM table reverses: Order B first, Order A second
    cur_orders = [
        {"side": "BUY", "price": 80000.0, "notional_usd": 5000000.0, "duration_seconds": 3780.0},
        {"side": "BUY", "price": 80000.0, "notional_usd": 5000000.0, "duration_seconds": 19980.0},
    ]

    matched, report = match_cross_cycle_orders(cur_orders, prev_orders, cycle_interval_s=180.0, asset="BTC")
    assert matched[0]["track_id"] == "BTC_BUY_80000_ORDER_B"
    assert matched[1]["track_id"] == "BTC_BUY_80000_ORDER_A"
    assert report["lost_orders_count"] == 0

    # Tied duration test: two orders with identical duration must report as TIED
    prev_tied = [
        {"track_id": "BTC_BUY_80000_T1", "side": "BUY", "price": 80000.0, "notional_usd": 5000000.0, "duration_seconds": 3600.0},
        {"track_id": "BTC_BUY_80000_T2", "side": "BUY", "price": 80000.0, "notional_usd": 5000000.0, "duration_seconds": 3600.0},
    ]
    cur_tied = [
        {"side": "BUY", "price": 80000.0, "notional_usd": 5000000.0, "duration_seconds": 3780.0},
        {"side": "BUY", "price": 80000.0, "notional_usd": 5000000.0, "duration_seconds": 3780.0},
    ]
    matched_tied, rep_tied = match_cross_cycle_orders(cur_tied, prev_tied, cycle_interval_s=180.0, asset="BTC")
    assert "TIED" in matched_tied[0]["match_status"]


def test_q2_notional_expansion_handling():
    """Verify Q2: Notional growth tags NOTIONAL_EXPANDED and preserves track_id."""
    prev_orders = [
        {"track_id": "ETH_BUY_2400_WHALE_1", "side": "BUY", "price": 2400.0, "notional_usd": 10000000.0, "duration_seconds": 7200.0}
    ]
    cur_orders = [
        {"side": "BUY", "price": 2400.0, "notional_usd": 12000000.0, "duration_seconds": 7380.0}
    ]
    matched, report = match_cross_cycle_orders(cur_orders, prev_orders, cycle_interval_s=180.0, asset="ETH")
    assert matched[0]["track_id"] == "ETH_BUY_2400_WHALE_1"
    assert matched[0]["match_status"] == "NOTIONAL_EXPANDED"
    assert matched[0]["expanded_usd"] == 2000000.0


def test_f102_unique_track_ids_identical_price_and_side():
    """Verify F102: Two new orders at the exact same asset, price, and side receive distinct unique track IDs."""
    cur_orders = [
        {"side": "BUY", "price": 80000.0, "notional_usd": 5000000.0, "duration_seconds": 180.0},
        {"side": "BUY", "price": 80000.0, "notional_usd": 5000000.0, "duration_seconds": 180.0},
    ]
    matched, report = match_cross_cycle_orders(cur_orders, prev_orders=[], cycle_interval_s=180.0, asset="BTC")
    assert len(matched) == 2
    assert matched[0]["match_status"] == "NEW_ORDER"
    assert matched[1]["match_status"] == "NEW_ORDER"
    assert matched[0]["track_id"] != matched[1]["track_id"]
    assert "row0" in matched[0]["track_id"]
    assert "row1" in matched[1]["track_id"]


def test_f103_continuous_partial_fill_rule():
    """Verify F103: Partial fill classification is continuous across all sizes with zero cliff threshold."""
    prev_orders = [
        {"track_id": "BTC_BUY_80000_WHALE", "side": "BUY", "price": 80000.0, "notional_usd": 5000000.0, "duration_seconds": 3600.0}
    ]

    # Test A: 0.5% fill ($5,000,000 -> $4,975,000) -> PARTIAL_FILL (no cliff threshold!)
    cur_0_5 = [{"side": "BUY", "price": 80000.0, "notional_usd": 4975000.0, "duration_seconds": 3780.0}]
    matched_0_5, _ = match_cross_cycle_orders(cur_0_5, prev_orders, cycle_interval_s=180.0, asset="BTC")
    assert matched_0_5[0]["match_status"] == "PARTIAL_FILL"
    assert matched_0_5[0]["fill_pct"] == 0.5
    assert matched_0_5[0]["filled_usd"] == 25000.0
    assert matched_0_5[0]["residual_pct"] == 99.5

    # Test B: 4.9% fill ($5,000,000 -> $4,755,000) -> PARTIAL_FILL (smooth across 5% boundary)
    cur_4_9 = [{"side": "BUY", "price": 80000.0, "notional_usd": 4755000.0, "duration_seconds": 3780.0}]
    matched_4_9, _ = match_cross_cycle_orders(cur_4_9, prev_orders, cycle_interval_s=180.0, asset="BTC")
    assert matched_4_9[0]["match_status"] == "PARTIAL_FILL"
    assert matched_4_9[0]["fill_pct"] == 4.9
    assert matched_4_9[0]["filled_usd"] == 245000.0

    # Test C: 5.0% fill ($5,000,000 -> $4,750,000) -> PARTIAL_FILL
    cur_5_0 = [{"side": "BUY", "price": 80000.0, "notional_usd": 4750000.0, "duration_seconds": 3780.0}]
    matched_5_0, _ = match_cross_cycle_orders(cur_5_0, prev_orders, cycle_interval_s=180.0, asset="BTC")
    assert matched_5_0[0]["match_status"] == "PARTIAL_FILL"
    assert matched_5_0[0]["fill_pct"] == 5.0
    assert matched_5_0[0]["filled_usd"] == 250000.0

    # Test D: 5.2% fill ($5,000,000 -> $4,740,000) -> PARTIAL_FILL
    cur_5_2 = [{"side": "BUY", "price": 80000.0, "notional_usd": 4740000.0, "duration_seconds": 3780.0}]
    matched_5_2, _ = match_cross_cycle_orders(cur_5_2, prev_orders, cycle_interval_s=180.0, asset="BTC")
    assert matched_5_2[0]["match_status"] == "PARTIAL_FILL"
    assert matched_5_2[0]["fill_pct"] == 5.2
    assert matched_5_2[0]["filled_usd"] == 260000.0

    # Test E: 40% fill ($5M -> $3M)
    cur_40 = [{"side": "BUY", "price": 80000.0, "notional_usd": 3000000.0, "duration_seconds": 3780.0}]
    matched_40, _ = match_cross_cycle_orders(cur_40, prev_orders, cycle_interval_s=180.0, asset="BTC")
    assert matched_40[0]["match_status"] == "PARTIAL_FILL"
    assert matched_40[0]["fill_pct"] == 40.0
    assert matched_40[0]["filled_usd"] == 2000000.0

    # Test F: 98% fill ($5M -> $100k)
    cur_98 = [{"side": "BUY", "price": 80000.0, "notional_usd": 100000.0, "duration_seconds": 3780.0}]
    matched_98, _ = match_cross_cycle_orders(cur_98, prev_orders, cycle_interval_s=180.0, asset="BTC")
    assert matched_98[0]["match_status"] == "PARTIAL_FILL"
    assert matched_98[0]["fill_pct"] == 98.0
    assert matched_98[0]["filled_usd"] == 4900000.0


def test_f104_lost_orders_microstructure_attribution():
    """Verify F104: Lost orders include complete schema and attribute FILLED_PRICE_CROSSED vs CANCELED_UNTOUCHED."""
    prev_orders = [
        {"track_id": "SOL_BUY_150_RESTING", "side": "BUY", "price": 150.0, "notional_usd": 2500000.0, "duration_seconds": 5400.0},
        {"track_id": "SOL_SELL_160_RESTING", "side": "SELL", "price": 160.0, "notional_usd": 3200000.0, "duration_seconds": 7200.0},
    ]

    # Sub-test 1: Market traded down to 148 (below BUY 150). BUY 150 disappears.
    # Ref price 148 <= 150 -> BUY 150 was filled at market!
    cur_orders_1 = [
        {"side": "SELL", "price": 160.0, "notional_usd": 3200000.0, "duration_seconds": 7380.0}
    ]
    matched_1, report_1 = match_cross_cycle_orders(cur_orders_1, prev_orders, cycle_interval_s=180.0, ref_price=148.0, asset="SOL")
    assert report_1["lost_orders_count"] == 1
    lost_1 = report_1["lost_orders"][0]
    assert lost_1["track_id"] == "SOL_BUY_150_RESTING"
    assert lost_1["side"] == "BUY"
    assert lost_1["price"] == 150.0
    assert lost_1["last_notional_usd"] == 2500000.0
    assert lost_1["terminal_status"] == "FILLED_PRICE_CROSSED"

    # Sub-test 2: Market price remained at 155 (above BUY 150). BUY 150 was pulled/canceled.
    matched_2, report_2 = match_cross_cycle_orders(cur_orders_1, prev_orders, cycle_interval_s=180.0, ref_price=155.0, asset="SOL")
    assert report_2["lost_orders_count"] == 1
    lost_2 = report_2["lost_orders"][0]
    assert lost_2["terminal_status"] == "CANCELED_UNTOUCHED"

    # Sub-test 3: SELL 160 disappears when market rallied to 162.
    cur_orders_3 = [
        {"side": "BUY", "price": 150.0, "notional_usd": 2500000.0, "duration_seconds": 5580.0}
    ]
    matched_3, report_3 = match_cross_cycle_orders(cur_orders_3, prev_orders, cycle_interval_s=180.0, ref_price=162.0, asset="SOL")
    assert report_3["lost_orders_count"] == 1
    lost_3 = report_3["lost_orders"][0]
    assert lost_3["track_id"] == "SOL_SELL_160_RESTING"
    assert lost_3["terminal_status"] == "FILLED_PRICE_CROSSED"


def test_f107_shipped_sign_persistence_code():
    """Verify F107: Imports and validates evaluate_sign_persistence from shipped production code."""
    now = 2000.0

    # 1. Valid 4 adjacent harvests with positive score (span = 540s, gap = 180s)
    hist_pos = [
        {"harvest_epoch": 1460.0, "s": 0.35},
        {"harvest_epoch": 1640.0, "s": 0.40},
        {"harvest_epoch": 1820.0, "s": 0.45},
        {"harvest_epoch": 2000.0, "s": 0.38},
    ]
    ok, reason = evaluate_sign_persistence(hist_pos, now_ts=now)
    assert ok is True
    assert "PERSISTENT_POSITIVE" in reason

    # 2. Valid 4 adjacent harvests with negative score
    hist_neg = [
        {"harvest_epoch": 1460.0, "s": -0.35},
        {"harvest_epoch": 1640.0, "s": -0.40},
        {"harvest_epoch": 1820.0, "s": -0.45},
        {"harvest_epoch": 2000.0, "s": -0.38},
    ]
    ok, reason = evaluate_sign_persistence(hist_neg, now_ts=now)
    assert ok is True
    assert "PERSISTENT_NEGATIVE" in reason

    # 3. Gap too large (> 300s): non-adjacent harvest fails closed
    hist_gap = [
        {"harvest_epoch": 1100.0, "s": 0.35},
        {"harvest_epoch": 1460.0, "s": 0.40},  # gap = 360s > 300s
        {"harvest_epoch": 1640.0, "s": 0.45},
        {"harvest_epoch": 1820.0, "s": 0.38},
    ]
    ok, reason = evaluate_sign_persistence(hist_gap, now_ts=now)
    assert ok is False
    assert "HARVEST_GAP_TOO_LARGE" in reason

    # 4. Latest harvest stale (> 300s old): fails closed
    ok, reason = evaluate_sign_persistence(hist_pos, now_ts=now + 500.0)
    assert ok is False
    assert "LATEST_HARVEST_STALE" in reason

    # 5. Mixed signs (alternating +0.35 and -0.30): fails closed
    hist_mixed = [
        {"harvest_epoch": 1460.0, "s": 0.35},
        {"harvest_epoch": 1640.0, "s": -0.30},
        {"harvest_epoch": 1820.0, "s": 0.45},
        {"harvest_epoch": 2000.0, "s": 0.38},
    ]
    ok, reason = evaluate_sign_persistence(hist_mixed, now_ts=now)
    assert ok is False
    assert "SIGN_OR_MAGNITUDE_INCONSISTENT" in reason

    # 6. Insufficient history (< 4 harvests): fails closed
    ok, reason = evaluate_sign_persistence(hist_pos[:3], now_ts=now)
    assert ok is False
    assert "INSUFFICIENT_HISTORY" in reason


if __name__ == "__main__":
    test_q1_first_token_matching()
    test_q2_grid_tolerance_non_merging()
    test_q2_stacked_orders_duration_continuity_and_ties()
    test_q2_notional_expansion_handling()
    test_f102_unique_track_ids_identical_price_and_side()
    test_f103_continuous_partial_fill_rule()
    test_f104_lost_orders_microstructure_attribution()
    test_f107_shipped_sign_persistence_code()
    print("All 8 hardened CoinGlass pipeline unit tests (Cycles 187-194 / F102-F107) passed 100% successfully!")
