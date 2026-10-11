"""Tests for Terminal/gate_diagnostics.py -- gate observability, no verdict change.

The numbers in these tests are the MEASURED live values from generation
ab5f242f (2026-10-11 12:10 UTC), so the suite pins the findings the council
ruled on rather than synthetic round numbers.
"""
import math

import pytest

from Terminal.gate_diagnostics import (
    G5_MAX_SPREAD_BPS_HARD,
    G6_FRICTION_BASE_MAX_R,
    G6_FRICTION_RELAXED_MAX_R,
    atr_in_bps,
    audit_venue_mid_independence,
    audit_wall_timestamps,
    friction_verdict,
    g7_readiness,
    audit_wall_venue_coverage,
    regime_proximity,
    spread_friction_r,
)

# ------------------------------------------------------- measured live fixtures
# sym: (mid, atr_14, spread_bps, gamma_r observed on generation ab5f242f)
LIVE = {
    "BTC":  (83102.0,   123.1303,   1.93,   0.1737),
    "ETH":  (2504.0,      4.003,   11.18,   0.9325),
    "SOL":  (109.55,      0.225,   24.65,   1.6002),
    "BNB":  (749.3,     0.7719,    8.01,   1.0367),
    "XRP":  (1.394,     0.0025,   28.69,   2.1330),
    "ADA":  (0.248,     0.0008,   84.69,   3.5005),
    "DOGE": (0.0854,   0.0002,  246.05,  14.0084),
    "BCH":  (277.95,    0.692,    20.87,   1.1177),
}


# ==================================================== spread_friction_r

@pytest.mark.parametrize("sym", sorted(LIVE))
def test_gamma_reproduces_the_measured_live_values(sym):
    mid, atr, bps, expected = LIVE[sym]
    assert spread_friction_r(bps, mid, atr) == pytest.approx(expected, abs=1e-3)


def test_sol_friction_is_far_above_every_candidate_cap():
    """The proposal claimed SOL was ~0.037 R. It measures 1.6002 R.

    This is the finding that decided the dynamic-spread ruling: SOL fails the
    shipped 0.15 base cap, the 0.20 relaxed cap, and the proposed 0.25 cap.
    """
    g = spread_friction_r(LIVE["SOL"][2], LIVE["SOL"][0], LIVE["SOL"][1])
    assert g == pytest.approx(1.6002, abs=1e-3)
    assert g > 0.25, "SOL would be admitted by the proposed gamma_max"
    assert g > 10 * G6_FRICTION_BASE_MAX_R


def test_sol_spread_exceeds_its_whole_atr():
    """SOL: 24.65 bps of spread against 20.54 bps of ATR."""
    ab = atr_in_bps(LIVE["SOL"][0], LIVE["SOL"][1])
    assert ab == pytest.approx(20.54, abs=0.05)
    assert LIVE["SOL"][2] > ab, "spread should exceed ATR for this finding to hold"


def test_no_crypto_passes_the_base_friction_cap():
    """BTC measures 0.1737 R against a 0.15 R base cap -- even it fails."""
    under = [s for s, (m, a, b, _g) in LIVE.items()
             if (spread_friction_r(b, m, a) or 9e9) <= G6_FRICTION_BASE_MAX_R]
    assert under == []


def test_btc_is_also_the_only_crypto_under_the_relaxed_cap():
    under = [s for s, (m, a, b, _g) in LIVE.items()
             if (spread_friction_r(b, m, a) or 9e9) <= G6_FRICTION_RELAXED_MAX_R]
    assert under == ["BTC"]


@pytest.mark.parametrize("bps,mid,atr", [
    (None, 100.0, 1.0), (10.0, None, 1.0), (10.0, 100.0, None),
    (10.0, 0.0, 1.0), (10.0, 100.0, 0.0), (10.0, -100.0, 1.0),
    (-1.0, 100.0, 1.0), (float("nan"), 100.0, 1.0), (float("inf"), 100.0, 1.0),
    (10.0, 100.0, float("nan")), (True, 100.0, 1.0),
])
def test_unusable_operands_return_none_never_zero(bps, mid, atr):
    """An unknown cost must never read as a free trade."""
    assert spread_friction_r(bps, mid, atr) is None


def test_atr_in_bps_rejects_bad_operands():
    assert atr_in_bps(0.0, 1.0) is None
    assert atr_in_bps(100.0, None) is None
    assert atr_in_bps(100.0, -1.0) is None


def test_friction_verdict_reports_both_gates_side_by_side():
    v = friction_verdict(LIVE["ETH"][2], LIVE["ETH"][0], LIVE["ETH"][1])
    assert v["g5_static_bps_ok"] is True, "ETH 11.18 bps passes the static cap"
    assert v["g6_base_ok"] is False, "ETH 0.9325 R fails the relative cap"
    assert v["g6_relaxed_ok"] is False
    assert v["gamma_max_required_r"] == pytest.approx(0.9325, abs=1e-3)


def test_friction_verdict_marks_unmeasurable_as_unmeasurable():
    v = friction_verdict(None, None, None)
    assert v["gamma_r"] is None
    assert v["g6_base_ok"] is False and v["g6_relaxed_ok"] is False
    assert v["margin_to_base_r"] is None, "must not imply infinite room"


# ==================================================== regime_proximity

def _stats(er15, vr15, t15, er1h, vr1h, t1h, er4h, vr4h, t4h):
    return {"15m": {"er": er15, "vr_z": vr15, "t": t15},
            "1h": {"er": er1h, "vr_z": vr1h, "t": t1h},
            "4h": {"er": er4h, "vr_z": vr4h, "t": t4h}}


# Measured live, generation ab5f242f.
LIVE_STATS = {
    "BTC": _stats(0.0, -0.9358, 0.0, 0.0196, 0.0, 0.0, 0.3160, 0.0, 0.0),
    "ETH": _stats(0.0, -1.3161, 0.0, 0.0033, 0.0, 0.0, 0.4552, 0.0, 0.0),
    "BNB": _stats(0.0, +0.6027, 0.0, 0.1120, 0.0, 0.0, 0.2696, 0.0, 0.0),
    "TRX": _stats(0.0, -0.5147, 0.0, 0.1405, 0.0, 0.0, 0.3010, 0.0, 0.0),
}


def test_btc_binding_leg_is_the_variance_ratio_by_a_wide_margin():
    p = regime_proximity(LIVE_STATS["BTC"])
    assert p["usable"] and p["mean_revert_ok"] is False
    assert p["binding_leg"] == "vr_z_15m_lt_cut"
    assert p["mean_revert_leg_margins"]["vr_z_15m_lt_cut"] == pytest.approx(-0.5642, abs=1e-3)


def test_epsilon_needed_exceeds_the_proposed_band_for_every_live_asset():
    """The proposal suggested epsilon = 0.05. Nothing needs less than 0.56."""
    for sym, st in LIVE_STATS.items():
        p = regime_proximity(st)
        assert p["epsilon_needed_to_flip_mr"] >= 0.05, sym
    assert regime_proximity(LIVE_STATS["BTC"])["epsilon_needed_to_flip_mr"] == pytest.approx(0.5642, abs=1e-3)


def test_epsilon_needed_is_zero_when_the_regime_already_qualifies():
    st = _stats(0.0, -2.0, 0.0, 0.05, 0.0, 0.0, 0.10, 0.0, 0.0)
    p = regime_proximity(st)
    assert p["mean_revert_ok"] is True
    assert p["epsilon_needed_to_flip_mr"] == 0.0
    assert p["binding_leg"] is None


def test_the_eth_knife_edge_would_have_flipped_but_only_at_that_instant():
    """ETH read -1.4998 at 11:19 and -1.3161 at 12:11 -- the edge was transient."""
    then = _stats(0.0, -1.4998, 0.0, 0.0411, 0.0, 0.0, 0.29, 0.0, 0.0)
    p_then = regime_proximity(then)
    assert p_then["epsilon_needed_to_flip_mr"] == pytest.approx(0.0002, abs=1e-6)
    now = regime_proximity(LIVE_STATS["ETH"])
    assert now["epsilon_needed_to_flip_mr"] == pytest.approx(0.1839, abs=1e-3)
    assert now["epsilon_needed_to_flip_mr"] > 900 * p_then["epsilon_needed_to_flip_mr"]


def test_trend_vote_accounting_is_reported():
    # 1H trending down: t negative, er high, vr_z low -> 1 of 3 votes for DOWN.
    st = _stats(0.0, 0.0, 0.0, 0.40, -2.0, -3.0, 0.30, 0.0, -2.0)
    p = regime_proximity(st)
    assert p["trend_votes_passing"] == 1
    assert p["trend_vote_margins"]["er_1h_gt_er_trend"] == pytest.approx(0.05)
    assert p["htf_margins"]["t_4h_margin"] == pytest.approx(-3.5)


@pytest.mark.parametrize("bad", [None, {}, [], "x", {"15m": {}, "1h": {}},
                                 {"15m": None, "1h": None, "4h": None}])
def test_malformed_stats_fail_closed(bad):
    p = regime_proximity(bad)
    assert p["usable"] is False
    assert "epsilon_needed_to_flip_mr" not in p


def test_partial_statistics_are_unavailable_not_zero():
    st = {"15m": {"er": 0.1, "vr_z": None}, "1h": {"er": 0.1}, "4h": {"er": 0.1}}
    assert regime_proximity(st)["reason"] == "regime_statistics_unavailable"


# ==================================================== audit_wall_timestamps

def _assets(n=3, wall_ts=1791720483.89, with_walls=True, extra_ts_field=None):
    out = {}
    for i in range(n):
        ob = {"wall_sample_ts_epoch": wall_ts,
              "whale_walls_l3": [{"price": 1.0}] if with_walls else []}
        if extra_ts_field:
            ob[extra_ts_field] = wall_ts
        out[f"SYM{i}"] = {"orderbook_live_depth": ob}
    return out


def test_detects_the_pre_fix_pipeline_signature():
    """One shared wall timestamp AND no venue ts field == pre-fix generator."""
    a = audit_wall_timestamps(_assets(3))
    assert a["shared_across_assets"] is True
    assert a["missing_ts_fields"] is True
    assert a["verdict"] == "pre_fix_pipeline_signature"


def test_fix_deployed_is_not_flagged_as_pre_fix():
    a = audit_wall_timestamps(_assets(3, extra_ts_field="binance_mid_ts"))
    assert a["missing_ts_fields"] is False
    assert a["verdict"] != "pre_fix_pipeline_signature"


def test_distinct_per_asset_timestamps_are_not_shared():
    assets = {f"S{i}": {"orderbook_live_depth": {
        "wall_sample_ts_epoch": 1791720483.0 + i,
        "binance_mid_ts": 1791720483.0 + i,
        "whale_walls_l3": [{"price": 1.0}]}} for i in range(3)}
    a = audit_wall_timestamps(assets)
    assert a["distinct_wall_ts"] == 3
    assert a["shared_across_assets"] is False


def test_clock_skew_is_measured_per_symbol():
    assets = _assets(2)
    broker = {"SYM0": 1791720504.89, "SYM1": 1791720504.89}
    a = audit_wall_timestamps(assets, broker_ts_by_symbol=broker, max_skew_s=5.0)
    assert a["skew_s"]["SYM0"] == pytest.approx(-21.0)
    assert a["skew_ok"]["SYM0"] is False
    assert a["max_abs_skew_s"] == pytest.approx(21.0)


def test_contemporaneous_book_passes():
    assets = {f"S{i}": {"orderbook_live_depth": {
        "wall_sample_ts_epoch": 1000.0 + i, "binance_mid_ts": 1000.0 + i,
        "whale_walls_l3": [{"price": 1.0}]}} for i in range(3)}
    broker = {f"S{i}": 1001.0 + i for i in range(3)}
    a = audit_wall_timestamps(assets, broker_ts_by_symbol=broker)
    assert a["verdict"] == "contemporaneous"


def test_no_walls_published_is_reported_honestly():
    a = audit_wall_timestamps(_assets(2, with_walls=False, extra_ts_field="binance_mid_ts"))
    assert a["assets_with_walls"] == 0
    assert a["verdict"] == "no_walls_published"


@pytest.mark.parametrize("bad", [None, {}, [], "x"])
def test_audit_fails_closed_on_bad_input(bad):
    a = audit_wall_timestamps(bad)
    assert a["verdict"] == "insufficient_data"
    assert a["shared_across_assets"] is None, "must not assert a signature without data"


def test_assets_without_an_orderbook_are_skipped_not_counted():
    a = audit_wall_timestamps({"A": {"orderbook_live_depth": None}, "B": {}})
    assert a["assets_examined"] == 0
    assert a["verdict"] == "insufficient_data"


# ==================================================== venue-mid independence

def _venue_assets(n, vm_offset=0.0, spread=2.0, mid=100.0):
    """n assets whose venue mid sits `vm_offset` from a mid of 100."""
    return {f"S{i}": {"quotes": {"bid": mid - spread / 2, "ask": mid + spread / 2, "mid": mid},
                      "orderbook_live_depth": {"binance_mid": mid + vm_offset}}
            for i in range(n)}


def test_independent_venue_crosses_the_broker_spread():
    """Measured pre-restart: 96 of 135 observations sat OUTSIDE the spread."""
    a = audit_venue_mid_independence(_venue_assets(20, vm_offset=5.0, spread=2.0))
    assert a["observations"] == 20
    assert a["inside_spread_share"] == 0.0
    assert a["verdict"] == "consistent_with_independent_venue"
    assert a["suspect"] is False


def test_broker_derived_venue_mid_is_flagged():
    """Measured post-restart: 60 of 65 observations sat INSIDE the spread."""
    a = audit_venue_mid_independence(_venue_assets(20, vm_offset=0.0, spread=2.0))
    assert a["inside_spread_share"] == 1.0
    assert a["exact_zero_share"] == 1.0
    assert a["verdict"] == "broker_derived_suspect"
    assert a["suspect"] is True


def test_exact_zero_basis_is_arithmetic_identity_not_agreement():
    a = audit_venue_mid_independence(_venue_assets(5, vm_offset=0.0))
    assert a["exact_zero"] == 5


def test_partially_inside_share_is_judged_on_the_threshold():
    # 15 of 20 inside = 0.75, below the 0.80 suspect threshold.
    assets = _venue_assets(15, vm_offset=0.0, spread=2.0)
    assets.update({f"O{i}": {"quotes": {"bid": 99.0, "ask": 101.0, "mid": 100.0},
                             "orderbook_live_depth": {"binance_mid": 120.0}} for i in range(5)})
    a = audit_venue_mid_independence(assets)
    assert a["inside_spread_share"] == pytest.approx(0.75)
    assert a["suspect"] is False


@pytest.mark.parametrize("bad", [None, {}, [], "x",
                                 {"A": {"quotes": None}},
                                 {"A": {"quotes": {"bid": 1.0}}}])
def test_independence_audit_fails_closed(bad):
    a = audit_venue_mid_independence(bad)
    assert a["verdict"] == "insufficient_data"
    assert a["suspect"] is None, "must not certify independence without data"


# ==================================================== composite G-7 readiness

def _readiness_assets(skew_ok=True, venue_independent=True, wall_venue="BINANCE",
                      drop_venue_mid=False, n=4):
    """4 assets; toggle each independent G-7 precondition separately.

    Timestamps are distinct per asset in both the passing and failing case: the
    real failure signature is per-asset stamps that all lag, not one shared stamp.
    """
    base = 1000.0
    out = {}
    for i in range(n):
        wts = base + i if skew_ok else base + i - 30.0
        vm = 200.0 if venue_independent else 100.0     # 100.0 == broker mid
        ob = {
            "wall_sample_ts_epoch": wts, "binance_mid_ts": wts,
            "whale_walls_l3": [{"price": 1.0, "source": wall_venue,
                                "gate_g7_eligible": True, "wall_class": "GENUINE"}],
        }
        if not drop_venue_mid:
            ob["binance_mid"] = vm
        out[f"S{i}"] = {"quotes": {"bid": 99.0, "ask": 101.0, "mid": 100.0},
                        "orderbook_live_depth": ob}
    broker = {f"S{i}": base + i for i in range(n)}
    return out, broker


def test_all_three_preconditions_met_reports_ready():
    a, b = _readiness_assets(skew_ok=True, venue_independent=True)
    r = g7_readiness(a, broker_ts_by_symbol=b, max_skew_s=5.0)
    assert r["ready"] is True
    assert r["blockers"] == []
    assert r["binding_blocker"] is None
    assert r["clock_fix_alone_would_open_gate"] is False


def test_clock_skew_alone_blocks():
    a, b = _readiness_assets(skew_ok=False, venue_independent=True)
    r = g7_readiness(a, broker_ts_by_symbol=b, max_skew_s=5.0)
    assert r["ready"] is False
    assert r["binding_blocker"] == "wall_timestamps:clock_skew_exceeds_allowance"
    # Only blocker left, coverage complete, mid independent -> a repair would open it.
    assert r["clock_fix_alone_would_open_gate"] is True


def test_broker_derived_venue_mid_blocks_independently():
    a, b = _readiness_assets(skew_ok=True, venue_independent=False)
    r = g7_readiness(a, broker_ts_by_symbol=b, max_skew_s=5.0)
    assert r["ready"] is False
    assert "venue_mid:broker_derived_suspect" in r["blockers"]
    assert r["clock_fix_alone_would_open_gate"] is False


def test_missing_venue_mid_binds_first():
    """A wall on a venue with no published mid binds before clock and drift."""
    a, b = _readiness_assets(skew_ok=True, venue_independent=True,
                             wall_venue="HYPERLIQUID")
    r = g7_readiness(a, broker_ts_by_symbol=b, max_skew_s=5.0)
    assert r["ready"] is False
    assert r["binding_blocker"] == "venue_coverage:wall_venue_mid_missing"
    assert r["blockers"][0].startswith("venue_coverage:")
    assert r["clock_fix_alone_would_open_gate"] is False


def test_clock_and_derived_mid_together_do_not_open_on_clock_fix():
    """Two blockers means a clock repair still leaves the gate shut."""
    a, b = _readiness_assets(skew_ok=False, venue_independent=False)
    r = g7_readiness(a, broker_ts_by_symbol=b, max_skew_s=5.0)
    assert r["ready"] is False
    assert len(r["blockers"]) == 2
    assert r["clock_fix_alone_would_open_gate"] is False


def test_dropped_venue_mid_is_a_coverage_gap():
    a, b = _readiness_assets(drop_venue_mid=True)
    r = g7_readiness(a, broker_ts_by_symbol=b, max_skew_s=5.0)
    assert r["venue_coverage_verdict"] == "wall_venue_mid_missing"
    assert r["ready"] is False


def test_venue_coverage_counts_walls_and_venues():
    a, _ = _readiness_assets(wall_venue="HYPERLIQUID")
    c = audit_wall_venue_coverage(a)
    assert c["g7_walls_total"] == 4
    assert c["wall_venues_total"] == {"HYPERLIQUID": 4}
    assert c["covered_assets"] == 0
    assert c["verdict"] == "wall_venue_mid_missing"
    assert c["per_asset"]["S0"]["uncovered_venues"] == ["HYPERLIQUID"]


def test_venue_coverage_complete_when_venue_matches():
    a, _ = _readiness_assets(wall_venue="BINANCE")
    c = audit_wall_venue_coverage(a)
    assert c["coverage_complete"] is True
    assert c["verdict"] == "venue_mid_covered"
    assert c["per_asset"]["S0"]["venues_with_mid"] == ["BINANCE"]


def test_venue_coverage_reads_the_venue_basis_block():
    a, _ = _readiness_assets(wall_venue="HYPERLIQUID")
    a["S0"]["orderbook_live_depth"]["venue_basis"] = {
        "HYPERLIQUID": {"mid": 100.5, "mid_ts": 1.0, "basis_median": 0.0}}
    c = audit_wall_venue_coverage(a)
    assert c["per_asset"]["S0"]["covered"] is True
    assert c["per_asset"]["S1"]["covered"] is False


def test_venue_coverage_ignores_non_g7_walls():
    a, _ = _readiness_assets()
    a["S0"]["orderbook_live_depth"]["whale_walls_l3"] = [
        {"price": 1.0, "source": "HYPERLIQUID", "gate_g7_eligible": False},
        {"price": 2.0, "source": "HYPERLIQUID", "wall_class": "MIRRORED_LEG"},
    ]
    c = audit_wall_venue_coverage(a)
    assert c["per_asset"]["S0"]["g7_walls"] == 0


@pytest.mark.parametrize("bad", [None, {}, []])
def test_coverage_and_readiness_fail_closed(bad):
    c = audit_wall_venue_coverage(bad)
    assert c["coverage_complete"] is False
    assert c["verdict"] == "no_g7_walls_published"
    r = g7_readiness(bad)
    assert r["ready"] is False
    assert r["clock_fix_alone_would_open_gate"] is False


@pytest.mark.parametrize("n", [0, 1, 5, 23])
def test_coverage_never_crashes_on_odd_asset_counts(n):
    a, _ = _readiness_assets(n=max(n, 1))
    if n == 0:
        a = {}
    c = audit_wall_venue_coverage(a)
    assert c["assets_examined"] == n
