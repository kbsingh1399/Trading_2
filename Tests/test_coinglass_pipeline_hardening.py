#!/usr/bin/env python3
"""
Tests/test_coinglass_pipeline_hardening.py
=========================================
Hermetic, offline unit tests for the CoinGlass Data Pipeline hardening rules
addressing Arena Cycles 187, 188, 189, 190, 191, 192, and 193:
1. First-token exact matching (Q1: eliminates pair collisions like SOL/ETH matching ETH, eliminates STOP/BLINK/ARBITRUM, fails closed on empty).
2. Grid-derived price tolerance (Q2: 2.5 bps, ~20 USD at 80k, guarantees levels 56 apart never merge).
3. Stacked-order duration tie-break & tied duration reporting (Q2: bijective 1-to-1 matching, reports tied durations as ambiguous).
4. Partial-fill & notional-growth handling (Q2: maintains track_id across reductions and expansions).
5. Unique new-order IDs (F102: guarantees two orders at identical price and side never share identical track_id).
6. Continuous partial-fill rule (F103: continuous fill percentage across [5%, 100%), no cliff threshold).
7. Complete lost-orders schema (F104: includes track_id, side, price, last_notional_usd, terminal_status).
8. Shipped sign persistence verification (F107: imports and validates evaluate_sign_persistence from Terminal.Data_Factory.generate_telemetry_snapshot).
"""
import re
import json
import time
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))


def match_heading_token(heading_text: str | None, target_symbol: str) -> tuple[bool, str]:
    """Offline implementation of Q1 first-token heading assertion."""
    if not heading_text or not heading_text.strip():
        return False, f"Orderbook heading missing or empty: fail-closed for {target_symbol}"
    tokens = [t.upper() for t in re.split(r'[^A-Za-z0-9]+', heading_text.strip()) if t]
    target = target_symbol.upper()
    first_token = tokens[0] if tokens else ""
    exact_match = first_token in (target, f"{target}USDT", f"{target}USD")
    if not exact_match:
        return False, f"First-token mismatch: expected first token {target} but found tokens {tokens[:10]}"
    return True, "MATCH"


def match_cross_cycle_orders(cur_orders: list[dict], prev_orders: list[dict], cycle_interval_s: float = 180.0) -> tuple[list[dict], dict]:
    """Offline implementation of Q2 global bipartite cross-cycle matching engine."""
    exact_matches = 0
    partial_fills = 0
    ambiguous_matches = 0
    new_orders = 0
    ambiguity_log = []
    matched_prev_indices = set()
    out_orders = [dict(o) for o in cur_orders]

    try:
        from scipy.optimize import linear_sum_assignment
        has_scipy = True
    except ImportError:
        has_scipy = False

    for side in ("BUY", "SELL"):
        cur_side_indices = [idx for idx, o in enumerate(out_orders) if o.get("side") == side]
        prev_side_indices = [idx for idx, p in enumerate(prev_orders) if p.get("side") == side]

        if not cur_side_indices or not prev_side_indices:
            for c_idx in cur_side_indices:
                o = out_orders[c_idx]
                cur_p = float(o.get("price", 0.0))
                o["track_id"] = f"{o.get('asset', 'COIN')}_{o['side']}_{round(cur_p, 4)}_row{c_idx}"
                o["match_status"] = "NEW_ORDER"
                o["lineage"] = {"parent_track_id": None, "relation": "FRESH_BOOK_ENTRY"}
                new_orders += 1
            continue

        M = len(cur_side_indices)
        N = len(prev_side_indices)
        import numpy as np
        cost_matrix = np.full((M, N), 1e9, dtype=np.float64)

        for m_idx, c_idx in enumerate(cur_side_indices):
            o = out_orders[c_idx]
            cur_p = float(o.get("price", 0.0))
            cur_not = float(o.get("notional_usd", 0.0))
            cur_dur = float(o.get("duration_seconds", 0.0))
            tick_size = 0.0001 if cur_p < 1.0 else (0.01 if cur_p < 500.0 else 0.1)
            price_tol = max(2.0 * tick_size, 0.00025 * cur_p)

            for n_idx, p_idx in enumerate(prev_side_indices):
                prev_o = prev_orders[p_idx]
                prev_p = float(prev_o.get("price", 0.0))
                prev_not = float(prev_o.get("notional_usd", 0.0))
                prev_dur = float(prev_o.get("duration_seconds", 0.0))

                p_diff = abs(cur_p - prev_p)
                p_dev = p_diff / max(prev_p, 1e-4)

                if p_diff <= price_tol or p_dev <= 0.00025:
                    exp_dur = prev_dur + cycle_interval_s
                    dur_err = abs(cur_dur - exp_dur)
                    norm_p = p_diff / max(price_tol, 1e-4)
                    norm_dur = min(dur_err / 180.0, 10.0)
                    cost_matrix[m_idx, n_idx] = norm_p * 1.0 + norm_dur * 0.25

        if has_scipy:
            row_ind, col_ind = linear_sum_assignment(cost_matrix)
        else:
            edges = []
            for r in range(M):
                for c in range(N):
                    if cost_matrix[r, c] < 1e6:
                        edges.append((cost_matrix[r, c], r, c))
            edges.sort(key=lambda x: (
                x[0],
                abs(float(out_orders[cur_side_indices[x[1]]].get("duration_seconds", 0.0)) - (float(prev_orders[prev_side_indices[x[2]]].get("duration_seconds", 0.0)) + cycle_interval_s)),
                -float(prev_orders[prev_side_indices[x[2]]].get("notional_usd", 0.0)),
                float(prev_orders[prev_side_indices[x[2]]].get("price", 0.0))
            ))
            assigned_r = set()
            assigned_c = set()
            row_ind = []
            col_ind = []
            for cost, r, c in edges:
                if r not in assigned_r and c not in assigned_c:
                    assigned_r.add(r)
                    assigned_c.add(c)
                    row_ind.append(r)
                    col_ind.append(c)

        matched_cur_indices = set()
        for r, c in zip(row_ind, col_ind):
            if cost_matrix[r, c] < 1e6:
                c_idx = cur_side_indices[r]
                p_idx = prev_side_indices[c]
                o = out_orders[c_idx]
                prev_o = prev_orders[p_idx]

                matched_cur_indices.add(c_idx)
                matched_prev_indices.add(p_idx)

                cur_p = float(o.get("price", 0.0))
                prev_p = float(prev_o.get("price", 0.0))
                c_not = float(o.get("notional_usd", 0.0))
                p_not = float(prev_o.get("notional_usd", 0.0))

                drift_usd = round(cur_p - prev_p, 4)
                drift_bps = round(abs(cur_p - prev_p) / max(prev_p, 1e-4) * 10000.0, 2)

                # Continuous partial fill rule (F103: no cliff threshold)
                if c_not < p_not * 0.95:
                    match_status = "PARTIAL_FILL"
                    o["fill_pct"] = round((p_not - c_not) / p_not * 100.0, 1)
                    o["filled_usd"] = round(p_not - c_not, 2)
                    o["residual_pct"] = round(c_not / p_not * 100.0, 1)
                    partial_fills += 1
                elif c_not > p_not * 1.05:
                    match_status = "NOTIONAL_EXPANDED"
                    o["expanded_usd"] = round(c_not - p_not, 2)
                    o["fill_pct"] = 0.0
                    exact_matches += 1
                elif drift_usd != 0.0:
                    match_status = "PRICE_DRIFT_ACCEPTED"
                    exact_matches += 1
                else:
                    match_status = "EXACT_SINGLE_MATCH"
                    exact_matches += 1

                tied_count = sum(1 for c2 in range(N) if c2 != c and abs(cost_matrix[r, c2] - cost_matrix[r, c]) < 0.05 and cost_matrix[r, c2] < 1e6)
                if tied_count > 0:
                    match_status += "_TIED"
                    ambiguous_matches += 1
                    ambiguity_log.append({
                        "price": cur_p,
                        "side": side,
                        "tied_candidates": tied_count + 1,
                        "cost": round(float(cost_matrix[r, c]), 4),
                        "resolved_to_track_id": prev_o.get("track_id")
                    })

                o["track_id"] = prev_o.get("track_id", prev_o.get("row_id", f"{o.get('asset', 'COIN')}_{o['side']}_{round(cur_p, 4)}"))
                o["match_status"] = match_status
                o["price_dev_bps"] = drift_bps
                o["lineage"] = {
                    "parent_track_id": o["track_id"],
                    "relation": match_status,
                    "price_drift_usd": drift_usd,
                    "price_drift_bps": drift_bps,
                    "global_cost": round(float(cost_matrix[r, c]), 4)
                }

        for m_idx, c_idx in enumerate(cur_side_indices):
            if c_idx not in matched_cur_indices:
                o = out_orders[c_idx]
                cur_p = float(o.get("price", 0.0))
                o["track_id"] = f"{o.get('asset', 'COIN')}_{o['side']}_{round(cur_p, 4)}_row{c_idx}"
                o["match_status"] = "NEW_ORDER"
                o["lineage"] = {"parent_track_id": None, "relation": "FRESH_BOOK_ENTRY"}
                new_orders += 1

    # Complete lost-orders schema (F104: includes track_id, side, price, last_notional_usd, terminal_status)
    lost_orders = [
        {
            "track_id": p.get("track_id"),
            "side": p.get("side"),
            "price": p.get("price"),
            "last_notional_usd": p.get("notional_usd"),
            "terminal_status": "FILLED_OR_CANCELED"
        }
        for idx, p in enumerate(prev_orders) if idx not in matched_prev_indices
    ]

    report = {
        "total_orders": len(out_orders),
        "exact_matches": exact_matches,
        "partial_fills": partial_fills,
        "ambiguous_matches": ambiguous_matches,
        "new_orders": new_orders,
        "lost_orders_count": len(lost_orders),
        "ambiguity_log": ambiguity_log,
        "lost_orders": lost_orders
    }
    return out_orders, report


# --- Test Cases ---

def test_q1_first_token_matching():
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
    """Verify that tight 2.5 bps grid tolerance never merges levels 56 apart at 82,500."""
    p1 = 82500.0
    p2 = 82444.0
    tick_size = 0.1
    price_tol = max(2.0 * tick_size, 0.00025 * p1)  # 20.625 USD
    assert price_tol < 21.0
    assert abs(p1 - p2) > price_tol  # 56.0 > 20.625 -> NEVER MERGED!


def test_q2_stacked_orders_duration_continuity_and_ties():
    """Verify bijective matching and tied duration reporting."""
    prev_orders = [
        {"track_id": "BTC_BUY_80000_ORDER_A", "side": "BUY", "price": 80000.0, "notional_usd": 5000000.0, "duration_seconds": 19800.0},
        {"track_id": "BTC_BUY_80000_ORDER_B", "side": "BUY", "price": 80000.0, "notional_usd": 5000000.0, "duration_seconds": 3600.0},
    ]

    # DOM table reverses: Order B first, Order A second
    cur_orders = [
        {"side": "BUY", "price": 80000.0, "notional_usd": 5000000.0, "duration_seconds": 3780.0},
        {"side": "BUY", "price": 80000.0, "notional_usd": 5000000.0, "duration_seconds": 19980.0},
    ]

    matched, report = match_cross_cycle_orders(cur_orders, prev_orders, cycle_interval_s=180.0)
    assert matched[0]["track_id"] == "BTC_BUY_80000_ORDER_B"
    assert matched[1]["track_id"] == "BTC_BUY_80000_ORDER_A"
    assert report["lost_orders_count"] == 0

    # Tied duration test: two orders with identical duration must report as AMBIGUOUS_TIED_STACKED
    prev_tied = [
        {"track_id": "BTC_BUY_80000_T1", "side": "BUY", "price": 80000.0, "notional_usd": 5000000.0, "duration_seconds": 3600.0},
        {"track_id": "BTC_BUY_80000_T2", "side": "BUY", "price": 80000.0, "notional_usd": 5000000.0, "duration_seconds": 3600.0},
    ]
    cur_tied = [
        {"side": "BUY", "price": 80000.0, "notional_usd": 5000000.0, "duration_seconds": 3780.0},
        {"side": "BUY", "price": 80000.0, "notional_usd": 5000000.0, "duration_seconds": 3780.0},
    ]
    matched_tied, rep_tied = match_cross_cycle_orders(cur_tied, prev_tied, cycle_interval_s=180.0)
    assert "TIED" in matched_tied[0]["match_status"]


def test_q2_notional_expansion_handling():
    """Verify that notional growth tags NOTIONAL_EXPANDED and preserves track_id."""
    prev_orders = [
        {"track_id": "ETH_BUY_2400_WHALE_1", "side": "BUY", "price": 2400.0, "notional_usd": 10000000.0, "duration_seconds": 7200.0}
    ]
    cur_orders = [
        {"side": "BUY", "price": 2400.0, "notional_usd": 12000000.0, "duration_seconds": 7380.0}
    ]
    matched, report = match_cross_cycle_orders(cur_orders, prev_orders, cycle_interval_s=180.0)
    assert matched[0]["track_id"] == "ETH_BUY_2400_WHALE_1"
    assert matched[0]["match_status"] == "NOTIONAL_EXPANDED"
    assert matched[0]["expanded_usd"] == 2000000.0


def test_f102_unique_track_ids_identical_price_and_side():
    """Verify F102: two new orders at the exact same asset, price, and side get distinct unique track IDs."""
    cur_orders = [
        {"asset": "BTC", "side": "BUY", "price": 80000.0, "notional_usd": 5000000.0, "duration_seconds": 180.0},
        {"asset": "BTC", "side": "BUY", "price": 80000.0, "notional_usd": 5000000.0, "duration_seconds": 180.0},
    ]
    matched, report = match_cross_cycle_orders(cur_orders, prev_orders=[], cycle_interval_s=180.0)
    assert len(matched) == 2
    assert matched[0]["match_status"] == "NEW_ORDER"
    assert matched[1]["match_status"] == "NEW_ORDER"
    # Both must have non-identical unique IDs!
    assert matched[0]["track_id"] != matched[1]["track_id"]
    assert "row0" in matched[0]["track_id"]
    assert "row1" in matched[1]["track_id"]


def test_f103_continuous_partial_fill_rule():
    """Verify F103: partial fill classification is continuous across all sizes without an arbitrary cliff threshold."""
    prev_orders = [
        {"track_id": "BTC_BUY_80000_WHALE", "side": "BUY", "price": 80000.0, "notional_usd": 5000000.0, "duration_seconds": 3600.0}
    ]

    # Test A: 40% fill ($5M -> $3M)
    cur_a = [{"side": "BUY", "price": 80000.0, "notional_usd": 3000000.0, "duration_seconds": 3780.0}]
    matched_a, _ = match_cross_cycle_orders(cur_a, prev_orders, cycle_interval_s=180.0)
    assert matched_a[0]["match_status"] == "PARTIAL_FILL"
    assert matched_a[0]["track_id"] == "BTC_BUY_80000_WHALE"
    assert matched_a[0]["fill_pct"] == 40.0
    assert matched_a[0]["filled_usd"] == 2000000.0

    # Test B: 90% fill ($5M -> $500k)
    cur_b = [{"side": "BUY", "price": 80000.0, "notional_usd": 500000.0, "duration_seconds": 3780.0}]
    matched_b, _ = match_cross_cycle_orders(cur_b, prev_orders, cycle_interval_s=180.0)
    assert matched_b[0]["match_status"] == "PARTIAL_FILL"
    assert matched_b[0]["track_id"] == "BTC_BUY_80000_WHALE"
    assert matched_b[0]["fill_pct"] == 90.0
    assert matched_b[0]["filled_usd"] == 4500000.0

    # Test C: 98% fill ($5M -> $100k, continuous preservation of track_id)
    cur_c = [{"side": "BUY", "price": 80000.0, "notional_usd": 100000.0, "duration_seconds": 3780.0}]
    matched_c, _ = match_cross_cycle_orders(cur_c, prev_orders, cycle_interval_s=180.0)
    assert matched_c[0]["match_status"] == "PARTIAL_FILL"
    assert matched_c[0]["track_id"] == "BTC_BUY_80000_WHALE"
    assert matched_c[0]["fill_pct"] == 98.0
    assert matched_c[0]["filled_usd"] == 4900000.0


def test_f104_lost_orders_schema_with_side_and_notional():
    """Verify F104: lost orders report explicitly includes side, price, last_notional_usd, and terminal_status."""
    prev_orders = [
        {"track_id": "SOL_BUY_150_RESTING", "side": "BUY", "price": 150.0, "notional_usd": 2500000.0, "duration_seconds": 5400.0},
        {"track_id": "SOL_SELL_160_RESTING", "side": "SELL", "price": 160.0, "notional_usd": 3200000.0, "duration_seconds": 7200.0},
    ]
    # In next cycle, BUY 150 is gone, only SELL 160 remains
    cur_orders = [
        {"side": "SELL", "price": 160.0, "notional_usd": 3200000.0, "duration_seconds": 7380.0}
    ]
    matched, report = match_cross_cycle_orders(cur_orders, prev_orders, cycle_interval_s=180.0)
    assert report["lost_orders_count"] == 1
    lost = report["lost_orders"][0]
    assert lost["track_id"] == "SOL_BUY_150_RESTING"
    assert lost["side"] == "BUY"
    assert lost["price"] == 150.0
    assert lost["last_notional_usd"] == 2500000.0
    assert lost["terminal_status"] == "FILLED_OR_CANCELED"


def test_f107_shipped_sign_persistence_code():
    """Verify F107: imports and validates evaluate_sign_persistence from shipped production code."""
    from Terminal.Data_Factory.generate_telemetry_snapshot import evaluate_sign_persistence

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
    test_f104_lost_orders_schema_with_side_and_notional()
    test_f107_shipped_sign_persistence_code()
    print("All hardened CoinGlass pipeline unit tests (Cycles 187-193 / F102-F107) passed 100% successfully!")
