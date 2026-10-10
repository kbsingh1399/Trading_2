"""Regression tests for the whale-persistence series, the rolling spread median,
and the two operator policy changes to Gates G-6 and G-4.

Every test here is hermetic: pure functions over in-memory fixtures, or a tmp
path for the JSON state. No network, no live telemetry, no clock.
"""
from __future__ import annotations

import importlib.util
import pathlib
import sys

import pytest

ROOT = pathlib.Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from Terminal.decision_gates_v3 import (  # noqa: E402
    FRICTION_BASE_MAX_R,
    FRICTION_RELAXED_MAX_R,
    SendLimits,
    htf_confirms_direction,
    m1_range_override_ok,
    model1_checklist,
    pre_send_gate,
)
from Terminal.microstructure_state import (  # noqa: E402
    carry_forward_unseen,
    estimate_cycle_interval,
    expected_samples,
    observe_and_median_spread,
    prune_wall_state,
    record_cycle_interval,
    record_spread_observation,
    rolling_spread_median_bps,
    wall_persistence_record,
)


# ------------------------------------------------- 1. whale wall persistence
def test_first_sighting_is_a_single_sample_and_not_g7_eligible():
    """A wall seen once cannot claim 180s of persistence."""
    prev, new = {}, {}
    out = wall_persistence_record(prev, new, "BTC_SELL_83862.0", 1000.0)
    assert out["persist_s"] == 0.0
    assert out["samples"] == 1
    assert out["persistence_status"] == "SINGLE_SAMPLE"
    assert out["gate_g7_eligible"] is False
    assert new["BTC_SELL_83862.0"]["run_start"] == 1000.0


def test_unbroken_run_accumulates_persist_s_and_presence():
    """Continuous observation across cycles builds real persist_s."""
    state, now = {}, 1000.0
    for _ in range(5):                      # 5 cycles at 60s => 240s span
        out = wall_persistence_record(state, state, "ETH_BUY_2461.8", now)
        now += 60.0
    assert out["persist_s"] == 240.0
    assert out["samples"] == 5
    assert out["presence_frac"] == pytest.approx(1.0)
    assert out["persistence_status"] == "PERSISTENT_VERIFIED"
    assert out["gate_g7_eligible"] is True


def test_gap_longer_than_30s_restarts_the_run():
    """A wall that vanishes and returns is a NEW observation.

    Carrying the original sighting forward would fabricate continuity -- the
    same class of error as clamping a wall's age up to the 180s threshold.
    """
    state = {}
    wall_persistence_record(state, state, "BTC_SELL_83862.0", 1000.0)
    wall_persistence_record(state, state, "BTC_SELL_83862.0", 1060.0)
    # 300s gap -- far beyond gap_reset_s
    out = wall_persistence_record(state, state, "BTC_SELL_83862.0", 1360.0)
    assert out["persist_s"] == 0.0
    assert out["samples"] == 1
    assert out["run_start"] == 1360.0
    assert out["gate_g7_eligible"] is False


def test_gap_at_the_boundary_does_not_restart():
    state = {}
    wall_persistence_record(state, state, "BTC_SELL_83862.0", 1000.0)
    out = wall_persistence_record(state, state, "BTC_SELL_83862.0", 1030.0)
    assert out["samples"] == 2
    assert out["run_start"] == 1000.0


def test_flickering_wall_cannot_reach_the_0p9_presence_threshold():
    """Seen every other cycle => presence ~0.5, so G-7 must refuse it."""
    state, now = {}, 1000.0
    for i in range(12):
        if i % 2 == 0:
            out = wall_persistence_record(state, state, "SOL_SELL_111.7", now)
        now += 60.0
    assert out["presence_frac"] < 0.9
    assert out["gate_g7_eligible"] is False


def test_persist_s_alone_is_not_enough_for_g7():
    """200s of span with a missed sample must still fail on presence.

    This is the case the gap multiplier exists to expose: the run survives one
    missed sample, so persist_s clears 180, but attendance does not clear 0.9.
    """
    state = {}
    wall_persistence_record(state, state, "BTC_SELL_83862.0", 1000.0)
    wall_persistence_record(state, state, "BTC_SELL_83862.0", 1060.0)
    out = wall_persistence_record(state, state, "BTC_SELL_83862.0", 1200.0)
    assert out["persist_s"] == 200.0
    assert out["samples"] == 3
    assert out["presence_frac"] < 0.9
    assert out["gate_g7_eligible"] is False


def test_legacy_float_state_record_is_migrated_not_discarded():
    """Old state files stored a bare first_seen float."""
    state = {"BTC_SELL_83862.0": 900.0}
    out = wall_persistence_record(state, state, "BTC_SELL_83862.0", 1000.0)
    assert out["first_seen"] == 900.0        # preserved
    assert out["run_start"] == 1000.0        # but the run restarts
    assert out["persist_s"] == 0.0


def test_malformed_state_record_degrades_to_single_sample():
    state = {"BTC_SELL_83862.0": {"run_start": "garbage", "samples": None}}
    out = wall_persistence_record(state, state, "BTC_SELL_83862.0", 1000.0)
    assert out["persistence_status"] == "SINGLE_SAMPLE"
    assert out["gate_g7_eligible"] is False


def test_expected_samples_uses_the_measured_interval():
    assert expected_samples(1000.0, 1000.0, 60.0) == 1
    assert expected_samples(1000.0, 1300.0, 60.0) == 6
    # A wrong denominator would silently skew every presence_frac.
    assert expected_samples(1000.0, 1300.0, 30.0) == 11


def test_cycle_interval_is_measured_and_robust_to_junk():
    prev, new = {}, {}
    record_cycle_interval(prev, new, 1000.0)
    record_cycle_interval(new, prev, 1060.0)
    record_cycle_interval(prev, new, 1120.0)
    assert estimate_cycle_interval(new) == 60.0
    # No samples yet -> documented default, never a fabricated 0.
    assert estimate_cycle_interval({}) == 60.0
    # A backward clock must not corrupt the series.
    a, b = {}, {}
    record_cycle_interval(a, b, 2000.0)
    record_cycle_interval(b, a, 1000.0)
    assert estimate_cycle_interval(a) == 60.0


def test_prune_wall_state_bounds_growth_and_keeps_meta():
    state = {
        "__meta__": {"intervals": [60.0], "last_ts": 5000.0},
        "BTC_SELL_83862.0": {"last_seen": 4990.0, "run_start": 4900.0, "samples": 3},
        "ETH_BUY_2461.8": {"last_seen": 1000.0, "run_start": 900.0, "samples": 2},
        "GARBAGE": {"last_seen": "not-a-number"},
    }
    out = prune_wall_state(state, 5000.0, max_age_s=600.0)
    assert "__meta__" in out
    assert "BTC_SELL_83862.0" in out
    assert "ETH_BUY_2461.8" not in out      # aged out
    assert "GARBAGE" not in out             # unreadable -> dropped


# ------------------------------------------------ 2. rolling spread median
def test_rolling_median_uses_the_window_not_the_spot():
    """The defect being fixed: spot spread made 'x > 1.5x', always false."""
    hist = {}
    for i, bps in enumerate([2.0, 2.0, 2.0, 2.0, 40.0]):
        hist = record_spread_observation(hist, "BTCUSD.pi", 1000.0 + 60 * i, bps)
    med = rolling_spread_median_bps(hist, "BTCUSD.pi", 1240.0)
    assert med == 2.0                       # median, not the 40 bps spike
    assert med != 40.0


def test_rolling_median_excludes_prints_outside_the_window():
    hist = {}
    hist = record_spread_observation(hist, "BTCUSD.pi", 1000.0, 30.0)
    hist = record_spread_observation(hist, "BTCUSD.pi", 9000.0, 2.0)
    assert rolling_spread_median_bps(hist, "BTCUSD.pi", 9000.0, window_s=3600.0) == 2.0


def test_rolling_median_returns_none_rather_than_a_fabricated_default():
    assert rolling_spread_median_bps({}, "BTCUSD.pi", 1000.0) is None
    assert rolling_spread_median_bps({"BTCUSD.pi": []}, "BTCUSD.pi", 1000.0) is None


def test_record_spread_rejects_nonpositive_and_malformed_prints():
    hist = record_spread_observation({}, "X", 1000.0, 0.0)
    assert hist["X"] == []
    hist = record_spread_observation(hist, "X", 1000.0, -5.0)
    assert hist["X"] == []
    hist = record_spread_observation(hist, "X", "bad", 5.0)
    assert hist["X"] == []


def test_observe_and_median_spread_round_trips_through_disk(tmp_path):
    path = tmp_path / "Data" / ".spread_history_state.json"
    assert observe_and_median_spread("BTCUSD.pi", 1.8, 1000.0, path) == 1.8
    observe_and_median_spread("BTCUSD.pi", 2.0, 1060.0, path)
    med = observe_and_median_spread("BTCUSD.pi", 12.0, 1120.0, path)
    assert med == 2.0                       # 12 bps spike does not move the median
    assert path.exists()


def test_observe_and_median_spread_survives_an_unwritable_path():
    """A state-write failure must not take down order dispatch."""
    med = observe_and_median_spread("BTCUSD.pi", 2.5, 1000.0, "/dev/null/impossible/x.json")
    assert med == 2.5


# ------------------------------------------------- 3. G-6 friction policy (3a)
def _ev_ctx(**over):
    ctx = dict(
        direction="LONG", entry=100.0, sl=90.0, tp=125.0,
        risk_usd=10.0, round_trip_cost_usd=1.8, stop_slip_r=0.10,
        p_win_lower_bound=0.4197, spread_bps=18.0,
        regime="MEAN_REVERT", vwap_z=-2.5, atr=10.0, session_sigma=9.0,
        session_bars=40, vwap_slope_sigma_per_bar=0.0, vol_ratio_4_96=1.0,
        sweep_z=-2.5, vwap_z_change_4bars=0.0, sweep_extreme=99.0, vwap=110.0,
        reclaim_close=True, tick=None, spread=1.0, sigma_bar=5.0,
        orderflow=None, flush=None, wall=None,
    )
    ctx.update(over)
    return ctx


def _call_net_ev(rr, ctx):
    from Terminal.decision_gates_v3 import Verdict, _net_ev
    v = Verdict(True)
    _net_ev(v, ctx, rr, min_rr=1.5)
    return v


def test_flat_friction_cap_still_rejects_a_wide_spread():
    """c = 1.8/10 = 0.18R. With RR 2.0 the relaxed path is unavailable."""
    v = _call_net_ev(2.0, _ev_ctx())
    assert v.metrics["friction_relaxed"] is False
    assert v.metrics["friction_cap_r"] == FRICTION_BASE_MAX_R
    assert "EV_friction_gt_0p15R" in v.failures


def test_relaxed_friction_admits_a_proven_asymmetric_trade():
    """RR 2.8 with positive EV_lower and spread <= 20 bps => 0.20R cap."""
    v = _call_net_ev(2.8, _ev_ctx())
    assert v.metrics["friction_relaxed"] is True
    assert v.metrics["friction_cap_r"] == FRICTION_RELAXED_MAX_R
    assert v.metrics["ev_lower_r"] > 0.15
    assert not any(f.startswith("EV_friction") for f in v.failures)


def test_relaxation_refuses_when_ev_lower_is_thin():
    """Same friction, but EV_lower below +0.15R must fall back to 0.15R."""
    v = _call_net_ev(2.8, _ev_ctx(p_win_lower_bound=0.34))
    assert v.metrics["friction_relaxed"] is False
    assert "EV_friction_gt_0p15R" in v.failures


def test_relaxation_refuses_when_spread_exceeds_the_hard_ceiling():
    v = _call_net_ev(2.8, _ev_ctx(spread_bps=35.0))
    assert v.metrics["friction_relaxed"] is False


def test_relaxation_refuses_below_2p5R():
    v = _call_net_ev(2.4, _ev_ctx())
    assert v.metrics["friction_relaxed"] is False


def test_pre_send_gate_honours_the_relaxed_friction_flag():
    """The relaxed G-6 cap must be reachable through the real pre-send path."""
    lim = SendLimits()
    assert lim.max_spread_frac_r == 0.10
    assert lim.max_spread_frac_r_relaxed == 0.20

    class _Info:
        trade_mode = 1          # == SYMBOL_TRADE_MODE_FULL
        point = 0.01
        trade_stops_level = 0
        volume_min = 0.01
        volume_step = 0.01

    class _Tick:
        bid, ask, time_msc = 100.0, 100.15, 1000   # 0.15 abs = 15% of 1.0 risk

    class _Allowed:
        trade_allowed = True

    class _Check:
        retcode = 0

    class FakeMT5:
        SYMBOL_TRADE_MODE_FULL = 1
        ORDER_TYPE_BUY_LIMIT = 2
        def symbol_info(self, s): return _Info()
        def symbol_info_tick(self, s): return _Tick()
        def account_info(self): return _Allowed()
        def terminal_info(self): return _Allowed()
        def orders_get(self, symbol=None): return []
        def positions_get(self): return []
        def order_check(self, req): return _Check()

    base = dict(server_now_ms=1000, spread_median_bps_this_hour=15.0,
                mid_at_decision=100.075, atr=1.0, decision_age_s=0.0,
                joint_fill_ok=True, blackout_active=False)
    req = {"symbol": "BTCUSD.pi", "type": 2, "price": 100.0, "sl": 99.0,
           "tp": 103.0, "volume": 0.02, "comment": "x"}

    _, strict, _ = pre_send_gate(FakeMT5(), req, dict(base, friction_relaxed=False),
                                 lim, now_ms=1000)
    _, relaxed, _ = pre_send_gate(FakeMT5(), req, dict(base, friction_relaxed=True),
                                  lim, now_ms=1000)
    assert "spread_gt_10pct_of_R" in strict
    assert "spread_gt_10pct_of_R" not in relaxed
    # Nothing else should differ -- the flag must move friction and only friction.
    assert [x for x in strict if x != "spread_gt_10pct_of_R"] == \
           [x for x in relaxed if x != "spread_gt_10pct_of_R"]


# ------------------------------------------- 4. G-4 Model 1 decoupling (3b)
def test_htf_confirms_direction_and_fails_closed():
    down = {"t": -6.0, "er": 0.30}
    assert htf_confirms_direction(down, -1) is True
    assert htf_confirms_direction(down, +1) is False
    # Unreadable stats must be treated as adverse, never permissive.
    assert htf_confirms_direction({}, +1) is True
    assert htf_confirms_direction({"t": "x", "er": 0.3}, -1) is True


def _m1_ctx(**over):
    ctx = dict(regime="MEAN_REVERT", vwap_z=-2.6, atr=10.0, session_sigma=9.0,
               session_bars=40)
    ctx.update(over)
    return ctx


def test_range_override_requires_all_four_conditions():
    ok = dict(absorption_verified=True, htf_adverse_trend=False)
    assert m1_range_override_ok(_m1_ctx(regime="UNDEFINED", m1_range_override=ok)) is True
    # regime must be a consolidation label
    assert m1_range_override_ok(_m1_ctx(regime="TREND_UP", m1_range_override=ok)) is False
    assert m1_range_override_ok(_m1_ctx(regime="TREND_DOWN", m1_range_override=ok)) is False
    # |Z| >= 2.0 required
    assert m1_range_override_ok(_m1_ctx(regime="UNDEFINED", vwap_z=-1.4, m1_range_override=ok)) is False
    # absorption must be explicitly verified
    assert m1_range_override_ok(_m1_ctx(regime="UNDEFINED",
                                        m1_range_override=dict(ok, absorption_verified=False))) is False
    assert m1_range_override_ok(_m1_ctx(regime="UNDEFINED",
                                        m1_range_override={"htf_adverse_trend": False})) is False


def test_range_override_refuses_an_htf_confirmed_cascade():
    """The shipped rule barred Model 1 outside MEAN_REVERT because a stretched
    |Z| in a TREND selects cascades, not exhaustion. That hazard must survive
    the relaxation."""
    adverse = dict(absorption_verified=True, htf_adverse_trend=True)
    assert m1_range_override_ok(_m1_ctx(regime="UNDEFINED", m1_range_override=adverse)) is False
    # Missing the flag entirely must also refuse (fail closed, not fail open).
    assert m1_range_override_ok(_m1_ctx(regime="UNDEFINED",
                                        m1_range_override={"absorption_verified": True})) is False


def test_model1_checklist_admits_a_verified_range_reversion():
    of = dict(cvd_push1=-100.0, cvd_push2=-40.0, aggr_usd_sweep=300.0,
              aggr_usd_median_1m=100.0, lambda_sweep=0.3,
              lambda_median_60m=1.0, bars_cvd_turned=4)
    base = dict(
        direction="SHORT", regime="UNDEFINED", vwap_z=2.6, sweep_z=2.6,
        vwap_z_change_4bars=0.0, atr=100.0, session_sigma=90.0, session_bars=40,
        vwap_slope_sigma_per_bar=0.0, vol_ratio_4_96=1.0, entry=100.0, sl=112.0,
        tp=70.0, vwap=70.0, sweep_extreme=101.0, spread=1.0, tick=None,
        risk_usd=10.0, round_trip_cost_usd=0.5, p_win_lower_bound=0.4197,
        sigma_bar=5.0, orderflow=of, flush=None, reclaim_close=True,
    )
    blocked = model1_checklist(dict(base))
    assert "A1_regime_not_mean_revert" in blocked.failures

    unlocked = model1_checklist(dict(
        base,
        m1_range_override=dict(absorption_verified=True, htf_adverse_trend=False)))
    assert "A1_regime_not_mean_revert" not in unlocked.failures
    assert unlocked.metrics["m1_range_override_used"] is True


def test_model1_checklist_still_refuses_an_htf_cascade():
    of = dict(cvd_push1=-100.0, cvd_push2=-40.0, aggr_usd_sweep=300.0,
              aggr_usd_median_1m=100.0, lambda_sweep=0.3,
              lambda_median_60m=1.0, bars_cvd_turned=4)
    v = model1_checklist(dict(
        direction="SHORT", regime="UNDEFINED", vwap_z=2.6, sweep_z=2.6,
        vwap_z_change_4bars=0.0, atr=100.0, session_sigma=90.0, session_bars=40,
        vwap_slope_sigma_per_bar=0.0, vol_ratio_4_96=1.0, entry=100.0, sl=112.0,
        tp=70.0, vwap=70.0, sweep_extreme=101.0, spread=1.0, tick=None,
        risk_usd=10.0, round_trip_cost_usd=0.5, p_win_lower_bound=0.4197,
        sigma_bar=5.0, orderflow=of, flush=None, reclaim_close=True,
        m1_range_override=dict(absorption_verified=True, htf_adverse_trend=True)))
    assert "A1_regime_not_mean_revert" in v.failures


def test_carry_forward_unseen_preserves_last_seen_so_a_gap_can_be_measured():
    """A wall absent from one snapshot must not be forgotten.

    Without carry-forward, reappearance looks like a brand-new sighting, so
    every intermittent wall resets to persist_s=0 / presence_frac=1.0 and G-7
    can neither confirm nor deny anything.
    """
    prev, new = {}, {}
    wall_persistence_record(prev, prev, "ETH_BUY_2461.8", 1000.0)
    wall_persistence_record(prev, prev, "ETH_BUY_2461.8", 1060.0)
    # Cycle where ETH is absent from the book.
    carry_forward_unseen(prev, new)
    assert new["ETH_BUY_2461.8"]["last_seen"] == 1060.0
    # It returns 120s later -- one missed sample, so the run must CONTINUE.
    out = wall_persistence_record(new, new, "ETH_BUY_2461.8", 1180.0)
    assert out["samples"] == 3
    assert out["persist_s"] == 180.0
    assert out["presence_frac"] < 0.9            # 3 seen of 4 expected
    assert out["gate_g7_eligible"] is False      # span ok, attendance not


def test_carry_forward_does_not_clobber_this_cycles_records():
    prev = {"BTC_SELL_83862.0": {"last_seen": 1000.0, "run_start": 1000.0,
                                 "first_seen": 1000.0, "samples": 1}}
    new = {"BTC_SELL_83862.0": {"last_seen": 1060.0, "run_start": 1000.0,
                                "first_seen": 1000.0, "samples": 2}}
    carry_forward_unseen(prev, new)
    assert new["BTC_SELL_83862.0"]["samples"] == 2


# ------------------------------------- 5. wall authenticity (Corrections A/B)
from Terminal.microstructure_state import (  # noqa: E402
    WALL_GENUINE,
    WALL_MIRRORED_LEG,
    WALL_TOP_OF_BOOK,
    classify_wall,
    is_mirrored_leg,
    is_top_of_book,
)


def test_top_of_book_is_recognised_on_its_own_side_only():
    bb, ba = 82850.5, 82850.6
    assert is_top_of_book("BUY", 82850.5, bb, ba) is True
    assert is_top_of_book("SELL", 82850.6, bb, ba) is True
    # A BUY level is measured against the best BID, not the best ask.
    assert is_top_of_book("BUY", 82850.6, bb, ba) is False
    assert is_top_of_book("SELL", 82850.5, bb, ba) is False
    # One tick behind the touch is resting depth, not the touch.
    assert is_top_of_book("BUY", 82850.4, bb, ba) is False


def test_top_of_book_fails_safe_on_missing_or_bad_data():
    """An unreadable book must not silently certify a wall."""
    assert is_top_of_book("BUY", 82850.5, None, 82850.6) is False
    assert is_top_of_book("BUY", 82850.5, "x", "y") is False
    assert is_top_of_book("BUY", "x", 82850.5, 82850.6) is False
    assert is_top_of_book("BUY", 0.0, 82850.5, 82850.6) is False


def test_mirror_detection_uses_size_match_not_just_proximity():
    assert is_mirrored_leg("BUY", 83000.0, 500000.0, [(83000.1, 480000.0)]) is True
    # 52% ratio -- a real bracket asymmetry, not a mirror.
    assert is_mirrored_leg("BUY", 83000.0, 500000.0, [(83000.1, 260000.0)]) is False
    # Same size but far away in price is unrelated depth.
    assert is_mirrored_leg("BUY", 83000.0, 500000.0, [(83500.0, 500000.0)]) is False


def test_mirror_detection_fails_safe_on_junk():
    assert is_mirrored_leg("BUY", 83000.0, 500000.0, []) is False
    assert is_mirrored_leg("BUY", 83000.0, 500000.0, [("x", "y"), (0, 0)]) is False
    assert is_mirrored_leg("BUY", 83000.0, 0.0, [(83000.0, 500000.0)]) is False
    assert is_mirrored_leg("BUY", 83000.0, 500000.0, None) is False


def test_classify_wall_checks_the_touch_before_the_mirror():
    """A level AT the touch is top-of-book regardless of what sits opposite."""
    bb, ba = 82850.5, 82850.6
    assert classify_wall("BUY", 82850.5, 719970.84, bb, ba,
                         [(82850.6, 719970.84)]) == WALL_TOP_OF_BOOK
    assert classify_wall("BUY", 82832.0, 1004485.0, bb, ba,
                         [(82832.1, 1004485.0)]) == WALL_MIRRORED_LEG
    assert classify_wall("BUY", 82832.0, 1004485.0, bb, ba, []) == WALL_GENUINE


def test_persistence_alone_no_longer_certifies_gate_g7():
    """The regression being fixed: 180s on the book used to be sufficient.

    BTC's best bid and best ask (719,971 / 377,384 USD) both cleared the 150k
    threshold and were certified PERSISTENT_VERIFIED + gate_g7_eligible in
    OPPOSITE directions at once, which made the flag worthless as evidence of
    directional whale commitment. Authenticity must gate eligibility too.
    """
    state = {}
    now = 1000.0
    for _ in range(5):
        pers = wall_persistence_record(state, state, "BTC_SELL_82850.6", now)
        now += 60.0
    assert pers["persistence_status"] == "PERSISTENT_VERIFIED"   # persistence is real
    wclass = classify_wall("SELL", 82850.6, 377384.48, 82850.5, 82850.6,
                           [(82850.5, 719970.84)])
    assert wclass == WALL_TOP_OF_BOOK
    # This is the exact expression the generator now publishes.
    assert (pers["gate_g7_eligible"] and wclass == WALL_GENUINE) is False


# Wallet receipts are distinct from telemetry generation clocks.
def test_repeated_and_backward_wall_timestamps_do_not_add_evidence():
    state = {}
    for stamp in (1000.0, 1060.0, 1180.0):
        before = wall_persistence_record(state, state, "wallet", stamp)
    saved = dict(state["wallet"])
    assert before["presence_frac"] == 0.75
    for stamp in (1180.0, 1120.0, 1180.0):
        after = wall_persistence_record(state, state, "wallet", stamp, cycle_interval_s=120.0)
        assert state["wallet"] == saved
        assert after["samples"] == 3
        assert after["persist_s"] == 180.0
        assert after["presence_frac"] == 0.75
        assert after["gate_g7_eligible"] is False


def _wallet_row(**changes):
    return dict({"address": "0xaaa", "side": "BUY", "price": 100.0, "size": 2000.0,
                 "notional_usd": 200000.0, "observed_at": 1000.0,
                 "timestamp_basis": "RECEIPT_ONLY",
                 "coverage": "WALLET_ATTRIBUTED_SNAPSHOT_NO_ORDER_ID_NOT_FULL_L3",
                 "source": "HYPERDASH_GRAPHQL_ORDERBOOK_SNAPSHOT"}, **changes)


def _map_wallet_rows(rows, state, as_of, interval=60.0):
    from Terminal.Data_Factory.generate_telemetry_snapshot import sampled_wallet_whale_walls
    return sampled_wallet_whale_walls(rows, {"bids": [{"price": 99.0}], "asks": [{"price": 101.0}]},
                                     "BTC", 100.0, state, state, as_of, interval)


def test_wallet_mapping_preserves_provider_provenance_and_source_receipt():
    original = _wallet_row(provider_detail="retained")
    state = {}
    result = _map_wallet_rows([original], state, 1100.0)[0]
    for field in ("observed_at", "timestamp_basis", "coverage", "source", "provider_detail"):
        assert result[field] == original[field]
    assert state["BTC_L3_0xaaa_BUY_100.0"]["last_seen"] == 1000.0
    assert result["identity_kind"] == "WALLET_PRICE_LEVEL_NO_ORDER_ID"
    assert result["persistence_basis"] == "SAMPLED_RECEIPT_RECURRENCE"
    assert "samples" not in original


def test_cached_wallet_reads_cannot_repair_missing_presence():
    state = {}
    for observed in (1000.0, 1060.0, 1180.0):
        result = _map_wallet_rows([_wallet_row(observed_at=observed)], state, observed)[0]
    before = dict(state["BTC_L3_0xaaa_BUY_100.0"])
    for generation in (1240.0, 1300.0, 1360.0):
        result = _map_wallet_rows([_wallet_row(observed_at=1180.0)], state, generation, interval=120.0)[0]
        assert result["presence_frac"] == 0.75
        assert result["samples"] == 3
        assert result["persist_s"] == 180.0
        assert result["gate_g7_eligible"] is False
        assert state["BTC_L3_0xaaa_BUY_100.0"] == before


def test_backward_wallet_receipt_does_not_rewind_or_extend_state():
    state = {}
    _map_wallet_rows([_wallet_row(observed_at=1000.0)], state, 1000.0)
    _map_wallet_rows([_wallet_row(observed_at=1060.0)], state, 1060.0)
    before = dict(state["BTC_L3_0xaaa_BUY_100.0"])
    result = _map_wallet_rows([_wallet_row(observed_at=1020.0)], state, 1120.0)[0]
    assert result["samples"] == 2 and result["persist_s"] == 60.0
    assert state["BTC_L3_0xaaa_BUY_100.0"] == before


@pytest.mark.parametrize("observed", [None, "bad", float("nan"), float("inf"), 0.0, 1100.0])
def test_invalid_wallet_timestamp_has_no_persistence_evidence(observed):
    state = {}
    result = _map_wallet_rows([_wallet_row(observed_at=observed)], state, 1000.0)[0]
    assert not state
    assert result["persistence_status"] == "INVALID_OBSERVATION_TIMESTAMP"
    assert result["gate_g7_eligible"] is False


def test_matching_opposite_sizes_from_different_wallets_are_not_mirrors():
    rows = [_wallet_row(), _wallet_row(address="0xbbb", side="SELL", price=100.01)]
    result = _map_wallet_rows(rows, {}, 1000.0)
    assert all(r["wall_class"] == "GENUINE" for r in result)


def test_matching_opposite_sizes_from_same_wallet_are_mirrors():
    rows = [_wallet_row(), _wallet_row(address="0xAAA", side="SELL", price=100.01)]
    result = _map_wallet_rows(rows, {}, 1000.0)
    assert all(r["wall_class"] == "MIRRORED_LEG" for r in result)
    assert all(r["gate_g7_eligible"] is False for r in result)


def test_wallet_recurrence_is_explicitly_sampled_without_order_identity():
    state = {}
    for observed in (1000.0, 1060.0, 1120.0, 1180.0):
        result = _map_wallet_rows([_wallet_row(observed_at=observed)], state, observed)[0]
    assert result["persistence_status"] == "SAMPLED_RECURRENCE_VERIFIED"
    assert result["identity_kind"] == "WALLET_PRICE_LEVEL_NO_ORDER_ID"
    assert result["persistence_basis"] == "SAMPLED_RECEIPT_RECURRENCE"
    assert result["sample_span_sec"] == 180.0
    assert result["samples"] == 4
