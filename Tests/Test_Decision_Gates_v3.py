"""Unit test suite for Terminal/decision_gates_v3.py.
Verifies estimators, regime router, Model 1 / Model 2 checklists,
resting order invalidation, diffusion TTL, and fail-closed gates.
"""
import math
import numpy as np
import pytest

from Terminal.decision_gates_v3 import (
    yang_zhang_sigma,
    efficiency_ratio,
    variance_ratio,
    slope_tstat_nw,
    classify_regime,
    model1_checklist,
    model2_checklist,
    resting_order_invalidation,
    diffusion_ttl_minutes,
    hold_cut_decision,
    markout_report,
    RegimeParams,
    pre_send_gate,
    htf_confirms_direction,
    m1_range_override_ok,
    pullback_geometry,
    named_pool_inside_horizon,
    MIN_POOL_NOTIONAL_USD,
)


def test_estimators_basic():
    # Constant series
    c_flat = [100.0] * 50
    assert efficiency_ratio(c_flat, 20) == 0.0

    # Trend series
    c_trend = [100.0 + i for i in range(60)]
    er = efficiency_ratio(c_trend, 20)
    assert er is not None and abs(er - 1.0) < 1e-6

    # Variance ratio on trending series
    vr, z = variance_ratio(c_trend, q=4, n=48)
    assert vr is not None and z is not None

    # Slope t-stat
    t = slope_tstat_nw(c_trend, 48)
    assert t is not None and t > 0


def test_classify_regime_flat_undefined():
    c_15m = [100.0 + 0.1 * (i % 2) for i in range(120)]
    c_1h = [100.0 + 0.1 * (i % 2) for i in range(60)]
    c_4h = [100.0 + 0.1 * (i % 2) for i in range(40)]

    regime, stats = classify_regime(c_15m, c_1h, c_4h)
    assert regime in ("UNDEFINED", "MEAN_REVERT")


def test_model1_checklist_fail_closed_no_tape():
    ctx = {
        "direction": "LONG",
        "regime": "MEAN_REVERT",
        "vwap_z": -1.8,
        "sweep_z": -2.2,
        "vwap_z_change_4bars": 0.2,
        "atr": 10.0,
        "session_sigma": 9.0,
        "session_bars": 20,
        "vwap_slope_sigma_per_bar": 0.01,
        "vol_ratio_4_96": 1.2,
        "reclaim_close": True,
        "entry": 100.0,
        "sl": 88.0,
        "tp": 115.0,
        "vwap": 118.0,
        "sweep_extreme": 95.0,
        "spread": 0.2,
        "risk_usd": 12.0,
        "round_trip_cost_usd": 0.5,
        "p_win_lower_bound": 0.65,
    }
    # No orderflow tape provided -> MUST FAIL CLOSED
    v = model1_checklist(ctx)
    assert not v.passed
    assert "A2_no_tape_fail_closed" in v.failures


def test_model1_checklist_with_valid_tape():
    ctx = {
        "direction": "LONG",
        "regime": "MEAN_REVERT",
        "vwap_z": -1.8,
        "sweep_z": -2.4,
        "vwap_z_change_4bars": 0.2,
        "atr": 10.0,
        "session_sigma": 9.0,
        "session_bars": 20,
        "vwap_slope_sigma_per_bar": 0.01,
        "vol_ratio_4_96": 1.2,
        "reclaim_close": True,
        "entry": 100.0,
        "sl": 88.0,
        "tp": 118.0,
        "vwap": 120.0,
        "sweep_extreme": 95.0,
        "spread": 0.2,
        "risk_usd": 12.0,
        "round_trip_cost_usd": 0.5,
        "p_win_lower_bound": 0.65,
        "wall": {"usd": 200000.0, "persist_s": 200.0, "presence_frac": 1.0,
                 "dist_from_entry_atr": .1, "median_1m_traded_usd": 25000.0,
                 # dg_context always stamps these; G-7 rejects unlabelled walls.
                 "wall_class": "GENUINE", "gate_g7_eligible": True},
        "orderflow": {
            "cvd_push1": -100.0,
            "cvd_push2": -40.0,
            "aggr_usd_sweep": 500000.0,
            "aggr_usd_median_1m": 100000.0,
            "lambda_sweep": 0.001,
            "lambda_median_60m": 0.005,
            "bars_cvd_turned": 4,
        },
    }
    v = model1_checklist(ctx)
    assert v.passed, f"Failed with: {v.failures}"


def test_model2_checklist_fails_when_first_obstacle_missing():
    ctx = {
        "direction": "LONG",
        "regime": "TREND_UP",
        "atr": 10.0,
        "sigma_bar": 0.005,
        "geometry": {
            "retrace": 0.382,
            "depth_sigma": 1.2,
            "velocity_ratio": 0.45,
            "bars_pullback": 5,
            "bars_impulse": 12,
        },
        "structure_intact": True,
        "exhaustion_flags": {"vol_spike": False, "long_wick": False},
        "shelf": {"price": 100.0, "confluence": 3},
        "entry": 100.0,
        "sl": 83.0,
        "tp": 135.0,
        "tick": 0.1,
        "risk_usd": 12.0,
        "round_trip_cost_usd": 0.6,
        "p_win_lower_bound": 0.60,
        "allow_price_only_variant": True,
        # first_obstacle omitted
    }
    v = model2_checklist(ctx)
    assert not v.passed
    assert "B6_first_obstacle_missing" in v.failures


def test_model2_checklist_passes_with_obstacle():
    ctx = {
        "direction": "LONG",
        "regime": "TREND_UP",
        "atr": 10.0,
        "sigma_bar": 0.005,
        "geometry": {
            "retrace": 0.382,
            "depth_sigma": 1.2,
            "velocity_ratio": 0.45,
            "bars_pullback": 5,
            "bars_impulse": 12,
        },
        "structure_intact": True,
        "exhaustion_flags": {"vol_spike": False, "long_wick": False},
        "shelf": {"price": 100.0, "confluence": 3},
        "entry": 100.0,
        "sl": 83.0,
        "tp": 135.0,
        "first_obstacle": 140.0,
        "tick": 0.1,
        "risk_usd": 12.0,
        "round_trip_cost_usd": 0.6,
        "p_win_lower_bound": 0.60,
        "wall": {"usd": 200000.0, "persist_s": 200.0, "presence_frac": 1.0,
                 "dist_from_entry_atr": .1, "median_1m_traded_usd": 25000.0,
                 # dg_context always stamps these; G-7 rejects unlabelled walls.
                 "wall_class": "GENUINE", "gate_g7_eligible": True},
        "allow_price_only_variant": True,
    }
    v = model2_checklist(ctx)
    assert v.passed, f"Failed with: {v.failures}"


def test_resting_order_invalidation_zero_median_spread():
    o = {
        "direction": "LONG",
        "atr": 10.0,
        "limit": 100.0,
        "regime_at_stage": "TREND_UP",
        "ttl_minutes": 60.0,
    }
    m = {
        "regime": "TREND_UP",
        "new_counter_swing": False,
        "mid": 102.0,
        "ret_3bars_log": 0.001,
        "sigma_bar": 0.005,
        "minutes_resting": 10.0,
        "macro_blackout": False,
        "spread_bps": 0.5,
        "spread_median_bps": 0.0,  # Raw spread account with 0.0 median
    }
    verdict, reasons = resting_order_invalidation(o, m)
    # 0.5 bps spread is <= max(1.0, 2.5 * 0.0) = 1.0 bps, so it should KEEP
    assert verdict == "KEEP"


def test_diffusion_ttl_minutes():
    # Zero volatility safeguard returns min_ttl_minutes
    ttl = diffusion_ttl_minutes(dist_at_stage=10.0, sigma_bar_price=0.0, min_ttl_minutes=15.0)
    assert ttl == 15.0

    # Normal calculation
    ttl2 = diffusion_ttl_minutes(dist_at_stage=5.0, sigma_bar_price=2.0, bar_minutes=15, mult=2.0)
    expected = 2.0 * (5.0 / 2.0) ** 2 * 15.0
    assert abs(ttl2 - expected) < 1e-6


def _valid_gate_context(model=2, direction="LONG"):
    side = 1 if direction == "LONG" else -1
    ctx = dict(direction=direction, regime="TREND_UP" if side == 1 else "TREND_DOWN",
               atr=10.0, sigma_bar=.005, entry=100.0, sl=100.0 - side * 17.0,
               tp=100.0 + side * 35.0, first_obstacle=100.0 + side * 40.0,
               tick=.1, risk_usd=12.0, round_trip_cost_usd=.5, p_win_lower_bound=.65,
               geometry=dict(retrace=.382, depth_sigma=1.2, velocity_ratio=.45,
                             bars_pullback=5, bars_impulse=12), structure_intact=True,
               exhaustion_flags=dict(vol_spike=False, long_wick=False),
               shelf=dict(price=100.0, confluence=3), allow_price_only_variant=True,
               wall=dict(usd=200000.0, persist_s=200.0, presence_frac=1.0,
                         dist_from_entry_atr=.1, median_1m_traded_usd=25000.0,
                         wall_class="GENUINE", gate_g7_eligible=True))
    if model == 1:
        ctx.update(regime="MEAN_REVERT", sl=100.0 - side * 12.0, tp=100.0 + side * 18.0,
                   vwap=100.0 + side * 20.0, sweep_extreme=100.0 - side * 5.0,
                   vwap_z=-side * 1.8, sweep_z=-side * 2.4, vwap_z_change_4bars=side * .2,
                   session_sigma=9.0, session_bars=20, vwap_slope_sigma_per_bar=.01,
                   vol_ratio_4_96=1.2, reclaim_close=True, spread=.2,
                   orderflow=dict(cvd_push1=-side * 100.0, cvd_push2=-side * 40.0,
                                  aggr_usd_sweep=500000.0, aggr_usd_median_1m=100000.0,
                                  lambda_sweep=.001, lambda_median_60m=.005, bars_cvd_turned=4))
    return ctx


@pytest.mark.parametrize("model", [1, 2])
@pytest.mark.parametrize("direction", ["LONG", "SHORT"])
def test_protective_brackets_are_signed_for_both_models(model, direction):
    gate = model1_checklist if model == 1 else model2_checklist
    ctx = _valid_gate_context(model, direction)
    assert gate(ctx).passed
    # Same absolute stop distance, but the stop sits on the profitable side.
    ctx["sl"] = 2 * ctx["entry"] - ctx["sl"]
    assert not gate(ctx).passed
    assert any("invalid_protective_bracket" in reason for reason in gate(ctx).failures)


@pytest.mark.parametrize("gate", [model1_checklist, model2_checklist])
@pytest.mark.parametrize("ctx", [None, {}, [], {"direction": "LONG"}])
def test_missing_context_returns_a_verdict_instead_of_raising(gate, ctx):
    verdict = gate(ctx)
    assert not verdict.passed and verdict.failures


@pytest.mark.parametrize("model,key,value", [(1, "orderflow", {}), (1, "orderflow", []),
                                            (1, "flush", {}), (2, "geometry", None),
                                            (2, "geometry", {}), (2, "geometry", []),
                                            (2, "shelf", {}), (2, "orderflow", {}),
                                            (2, "exhaustion_flags", [False]), (2, "wall", [])])
def test_incomplete_nested_evidence_returns_a_failed_verdict(model, key, value):
    ctx = _valid_gate_context(model)
    ctx[key] = value
    assert not (model1_checklist if model == 1 else model2_checklist)(ctx).passed


@pytest.mark.parametrize("model,key", [(1, "atr"), (1, "session_sigma"), (1, "vol_ratio_4_96"),
                                     (1, "risk_usd"), (2, "atr"), (2, "sigma_bar"),
                                     (2, "risk_usd"), (2, "tick")])
@pytest.mark.parametrize("bad", [None, float("nan"), float("inf"), 0.0, -1.0, True])
def test_unknown_or_nonpositive_scale_cannot_admit_a_trade(model, key, bad):
    ctx = _valid_gate_context(model)
    ctx[key] = bad
    gate = model1_checklist if model == 1 else model2_checklist
    verdict = gate(ctx)
    assert not verdict.passed
    assert f"data_invalid:{key}" in verdict.failures


@pytest.mark.parametrize("field", ["cvd_push1", "cvd_push2", "aggr_usd_sweep", "aggr_usd_median_1m",
                                  "lambda_sweep", "lambda_median_60m", "bars_cvd_turned"])
def test_model1_requires_measured_absorption_operands(field):
    ctx = _valid_gate_context(1)
    del ctx["orderflow"][field]
    verdict = model1_checklist(ctx)
    assert not verdict.passed
    assert f"data_invalid:orderflow.{field}" in verdict.failures


@pytest.mark.parametrize("model", [1, 2])
@pytest.mark.parametrize("wall", [None, {}, {"usd": float("nan")},
                                  dict(usd=149999, persist_s=200, presence_frac=1,
                                       dist_from_entry_atr=.1, median_1m_traded_usd=25000),
                                  dict(usd=200000, persist_s=179, presence_frac=1,
                                       dist_from_entry_atr=.1, median_1m_traded_usd=25000),
                                  dict(usd=200000, persist_s=200, presence_frac=0,
                                       dist_from_entry_atr=.1, median_1m_traded_usd=25000),
                                  dict(usd=200000, persist_s=200, presence_frac=1,
                                       dist_from_entry_atr=-.1, median_1m_traded_usd=25000)])
def test_missing_or_unqualified_wall_cannot_admit_either_model(model, wall):
    ctx = _valid_gate_context(model)
    ctx["wall"] = wall
    assert not (model1_checklist if model == 1 else model2_checklist)(ctx).passed


@pytest.mark.parametrize("bad", [None, [], [100] * 15, [0] * 120, [float("nan")] * 120,
                                  [float("inf")] * 120, [[100]] * 120, "bad"])
def test_router_fails_closed_with_invalid_required_history(bad):
    trend = [100.0 + i for i in range(120)]
    for timeframe in range(3):
        closes = [trend, trend, trend]
        closes[timeframe] = bad
        regime, stats = classify_regime(*closes)
        assert regime == "UNDEFINED"
        assert stats["data_invalid"] == "regime_history_or_statistics"


@pytest.mark.parametrize("last,now,max_age", [(None, 1000, 1800), (900, None, 1800),
                                            (float("nan"), 1000, 1800), (900, 1000, float("nan")),
                                            ("900", 1000, 1800)])
def test_router_rejects_partially_supplied_or_invalid_clock(last, now, max_age):
    trend = [100.0 + i for i in range(120)]
    regime, stats = classify_regime(trend, trend, trend, last_close_epoch=last,
                                  as_of_epoch=now, max_staleness_s=max_age)
    assert regime == "UNDEFINED" and stats["stale"]


def test_nonfinite_htf_and_override_evidence_fail_closed():
    assert htf_confirms_direction({"t": float("nan"), "er": .3}, 1)
    assert htf_confirms_direction({"t": 4, "er": float("inf")}, 1)
    assert not m1_range_override_ok(dict(regime="UNDEFINED", vwap_z=float("nan"),
        m1_range_override=dict(absorption_verified=True, htf_adverse_trend=False)))


@pytest.mark.parametrize("sigma", [None, 0, -1, float("nan"), float("inf")])
def test_pullback_depth_does_not_fabricate_sigma(sigma):
    geometry = pullback_geometry([101, 112, 109], [99, 100, 105], [100, 110, 107], "LONG", 0, 1, sigma)
    assert geometry["depth_sigma"] is None


@pytest.mark.parametrize("kind,key,bad", [("req", "sl", float("nan")), ("req", "volume", 0),
                                        ("req", "volume", None), ("plan", "atr", 0),
                                        ("plan", "decision_age_s", -1), ("plan", "mid_at_decision", float("inf")),
                                        ("plan", "spread_median_bps_this_hour", float("nan"))])
def test_pre_send_unknown_numeric_inputs_are_rejected(kind, key, bad):
    from Tests.Test_Clock_Hardening import send_fixture
    broker, req, plan = send_fixture()
    (req if kind == "req" else plan)[key] = bad
    assert pre_send_gate(broker, req, plan)[0] is False


@pytest.mark.parametrize("field,bad", [("volume_step", 0), ("volume_min", None), ("volume_max", .05),
                                    ("point", float("nan")), ("trade_stops_level", -1)])
def test_pre_send_rejects_invalid_broker_volume_and_distance_contract(field, bad):
    from Tests.Test_Clock_Hardening import send_fixture
    broker, req, plan = send_fixture()
    setattr(broker.symbol_info("BTC"), field, bad)
    assert not pre_send_gate(broker, req, plan)[0]


@pytest.mark.parametrize("flag", ["false", "true", 1, None])
def test_pre_send_does_not_accept_malformed_friction_relaxation(flag):
    from Tests.Test_Clock_Hardening import send_fixture
    broker, req, plan = send_fixture()
    plan["friction_relaxed"] = flag
    assert "data_invalid:plan.friction_relaxed" in pre_send_gate(broker, req, plan)[1]


@pytest.mark.parametrize("direction", ["LONG", "SHORT"])
def test_pre_send_requires_passive_type_and_signed_brackets(direction):
    from Tests.Test_Clock_Hardening import send_fixture
    broker, req, plan = send_fixture()
    if direction == "SHORT":
        req.update(type=3, price=101, sl=102, tp=98)
    assert pre_send_gate(broker, req, plan)[0]
    req["sl"] = 2 * req["price"] - req["sl"]
    assert "invalid_protective_bracket" in pre_send_gate(broker, req, plan)[1]
    req["type"] = 0
    assert "passive_limit_type_required" in pre_send_gate(broker, req, plan)[1]


@pytest.mark.parametrize("ctx,key", [("order", "atr"), ("market", "sigma_bar"), ("market", "mid")])
def test_unobservable_resting_risk_or_volatility_cancels(ctx, key):
    order = dict(direction="LONG", atr=10, limit=100, regime_at_stage="TREND_UP", ttl_minutes=60)
    market = dict(regime="TREND_UP", new_counter_swing=False, mid=102, ret_3bars_log=.001,
                  sigma_bar=.005, minutes_resting=10, macro_blackout=False, spread_bps=.5, spread_median_bps=0)
    (order if ctx == "order" else market)[key] = float("nan")
    verdict, reasons = resting_order_invalidation(order, market)
    assert verdict == "CANCEL" and reasons


# ---------------------------------------------------------------------------
# Session-maturity guards. Regression coverage for the live 2026-10-11 02:21 UTC
# state: BTC classified MEAN_REVERT by classify_regime() while its session VWAP
# was only 9 bars old. Until this point NO test pinned A1_session_sigma_*, even
# though those two lines are the only thing standing between a MEAN_REVERT
# regime with |Z| >= 2.0 and a live counter-trend ticket.
# ---------------------------------------------------------------------------

def _m1_ctx(**over):
    """Model 1 ctx matching the BTC 02:21:41 UTC telemetry, SHORT side."""
    ctx = {
        "direction": "SHORT",
        "regime": "MEAN_REVERT",
        "entry": 82_969.0,
        "sl": 83_147.7,          # 1.5 ATR above
        "tp": 82_611.6,
        "atr": 119.11,
        "risk_usd": 15.0,
        "round_trip_cost_usd": 16.0,
        "reclaim_close": True,
        "vwap_z": 2.47,
        "sweep_z": 2.60,
        "vwap_z_change_4bars": 0.5,
        "session_sigma": 28.94,   # 0.243 ATR -- far below the 0.8 ATR floor
        "session_bars": 9,        # below the 16-bar maturity floor
        "vwap_slope_sigma_per_bar": 0.01,
        "vol_ratio_4_96": 1.2,
        "vwap": 82_897.66,
        "sweep_extreme": 83_050.0,
        "p_win_lower_bound": 0.42,
    }
    ctx.update(over)
    return ctx


def test_immature_session_short_circuits_before_a1_is_reached():
    """The live shape: VWAP inputs unresolved, so admission fails closed first.

    build_dg_context returns session_vwap_history_unavailable at session_bars=9,
    leaving every VWAP-derived field None. The checklist must stop there and
    never evaluate A1 -- an empty A1 failure list here would mean A1 PASSED,
    which is the misreading this test exists to prevent.
    """
    ctx = _m1_ctx(vwap_z=None, sweep_z=None, vwap_z_change_4bars=None,
                  session_sigma=None, vwap_slope_sigma_per_bar=None, vwap=None)
    v = model1_checklist(ctx)
    assert not v.passed
    assert "data_invalid:session_sigma" in v.failures
    assert not any(f.startswith("A1_") for f in v.failures), \
        "A1 must not be evaluated once admission has failed closed"


def test_maturity_guards_fire_even_with_fully_valid_vwap_inputs():
    """Both A1 maturity guards are independent of admission validation.

    Supplying every field admission asks for must still produce exactly the two
    session-maturity rejections -- proving the block is the maturity floor and
    not a data-quality artefact.
    """
    v = model1_checklist(_m1_ctx())
    assert not v.passed
    assert "A1_session_sigma_immature_lt16bars" in v.failures
    assert "A1_session_sigma_lt_0p8atr" in v.failures
    assert not any(f.startswith("data_invalid") for f in v.failures), \
        "admission should be clean; only maturity should reject"


def test_mean_revert_regime_limb_is_satisfied_when_regime_flips():
    """MEAN_REVERT satisfies A1's regime limb -- the block is maturity, not G-4.

    On 2026-10-11 02:00-02:25 UTC classify_regime() returned MEAN_REVERT for BTC
    for 26 consecutive snapshots while |Z| rose past 2.0. Model 1 is admissible
    only in MEAN_REVERT, so the regime gate opened while G-3 stayed shut.
    """
    v = model1_checklist(_m1_ctx())
    assert "A1_regime_not_mean_revert" not in v.failures
    assert "A1_z_below_2" not in v.failures          # SHORT at Z +2.60 clears 2.0
    assert "A1_z_beyond_3p5_cascade_zone" not in v.failures
    # Flip the regime and the same context must now be rejected on regime too.
    v2 = model1_checklist(_m1_ctx(regime="TREND_UP"))
    assert "A1_regime_not_mean_revert" in v2.failures


def test_z_above_3p5_is_rejected_even_in_mean_revert():
    """Z climbed to 3.23 by 02:25 UTC; the cascade ceiling must hold.

    Beyond 3.5 SD the move is a liquidation cascade, not exhaustion, so Model 1
    must stand down even though every maturity limb would otherwise pass.
    """
    v = model1_checklist(_m1_ctx(session_bars=20, session_sigma=120.0,
                                vwap_z=3.80, sweep_z=3.80))
    assert "A1_z_beyond_3p5_cascade_zone" in v.failures
    assert "A1_session_sigma_immature_lt16bars" not in v.failures
    assert "A1_session_sigma_lt_0p8atr" not in v.failures


def test_session_sigma_floor_is_scaled_to_atr_not_absolute():
    """The 0.8 ATR floor is relative, so it must move with volatility."""
    # Same absolute sigma, double the ATR -> now insufficient.
    assert "A1_session_sigma_lt_0p8atr" in model1_checklist(
        _m1_ctx(session_bars=20, atr=119.11, session_sigma=80.0)).failures
    # Comfortably above 0.8 ATR -> the guard clears.
    assert "A1_session_sigma_lt_0p8atr" not in model1_checklist(
        _m1_ctx(session_bars=20, atr=119.11, session_sigma=100.0)).failures


# ---------------------------------------------------------------------------
# A1's sigma and Z limbs are COUPLED, not independent. The snapshot publishes
# vwap_z = (price - session_vwap) / session_sigma, so requiring BOTH
# sigma >= 0.8*ATR and |Z| >= 2.0 implies |price - VWAP| >= 1.6*ATR. Nothing in
# the code or the tests stated that floor, and it is the real reason Model 1
# cannot fire: on 2026-10-11 02:51 UTC the offset was 99.04 USD (0.83 ATR)
# against a 190.56 USD floor. Growing sigma towards maturity *lowers* Z at a
# fixed offset, so maturation alone moves the setup further from admissible.
# ---------------------------------------------------------------------------

def test_a1_sigma_and_z_limbs_imply_a_1p6_atr_vwap_distance_floor():
    """At sigma exactly 0.8*ATR, the Z floor of 2.0 equals 1.6 ATR of offset."""
    atr = 119.10
    sigma_floor = 0.8 * atr            # 95.28
    offset_at_2sd = 2.0 * sigma_floor  # 190.56 == 1.6 * atr
    assert offset_at_2sd == pytest.approx(1.6 * atr)

    # Exactly at the coupled floor -> the Z limb clears by construction.
    v = model1_checklist(_m1_ctx(session_bars=20, atr=atr, session_sigma=sigma_floor,
                                vwap_z=2.0, sweep_z=2.0))
    assert "A1_session_sigma_lt_0p8atr" not in v.failures
    assert "A1_z_below_2" not in v.failures

    # A hair inside it -> maturity is satisfied but the Z limb is not.
    v2 = model1_checklist(_m1_ctx(session_bars=20, atr=atr, session_sigma=sigma_floor,
                                  vwap_z=1.875, sweep_z=1.875))
    assert "A1_session_sigma_lt_0p8atr" not in v2.failures
    assert "A1_z_below_2" in v2.failures


def test_sigma_maturation_alone_cannot_open_model1_at_a_short_offset():
    """The live 02:51 UTC offset: maturing sigma pushes Z below the trigger.

    offset 99.04 USD at 0.83 ATR. Once sigma reaches the required 95.28, the same
    offset yields Z = 1.04, so the maturity limb and the trigger limb trade off
    against each other. A desk waiting for session_bars to hit 16 without price
    extending is waiting for a setup that retires itself.
    """
    atr, offset = 119.10, 99.04
    assert offset / atr == pytest.approx(0.8316, abs=1e-4)
    z_once_mature = offset / (0.8 * atr)
    assert z_once_mature == pytest.approx(1.0395, abs=1e-4)

    v = model1_checklist(_m1_ctx(session_bars=20, atr=atr, session_sigma=0.8 * atr,
                                 vwap_z=z_once_mature, sweep_z=z_once_mature))
    assert "A1_session_sigma_lt_0p8atr" not in v.failures, "maturity limb should clear"
    assert "A1_z_below_2" in v.failures, "trigger limb must still reject"


def test_model1_needs_both_a_mature_session_and_an_extended_price():
    """Neither limb alone is sufficient; the admissible region is their product."""
    atr = 119.10
    # Immature session but a violent extension -> still rejected on maturity.
    v1 = model1_checklist(_m1_ctx(session_bars=9, atr=atr, session_sigma=30.0,
                                  vwap_z=6.0, sweep_z=3.0))
    assert "A1_session_sigma_immature_lt16bars" in v1.failures
    # Mature session, extended price, sigma commensurate -> both limbs clear.
    v2 = model1_checklist(_m1_ctx(session_bars=20, atr=atr, session_sigma=0.8 * atr,
                                  vwap_z=2.4, sweep_z=2.4))
    assert "A1_session_sigma_immature_lt16bars" not in v2.failures
    assert "A1_session_sigma_lt_0p8atr" not in v2.failures
    assert "A1_z_below_2" not in v2.failures
    assert "A1_z_beyond_3p5_cascade_zone" not in v2.failures


# ---------------------------------------------------------------------------
# A target anchor must be backed by real liquidity, not merely be close.
# MAX_TARGET_DIST_ATR validates distance only. On 2026-10-11 03:24:33 UTC the
# first non-empty top_short_squeeze_bands_above entry in ~13 cycles appeared at
# 82,950.0, +1.209 ATR from mid 82,800.0 -- inside the horizon -- carrying just
# 23,055.66 USD. Distance would have accepted it; size must not.
# ---------------------------------------------------------------------------

_LIVE_0324 = dict(entry=82_800.0, atr=124.11)


def test_tiny_band_inside_horizon_is_not_a_valid_target_anchor():
    """The live 03:24 UTC band: inside the 4.0 ATR window, but only 23k USD."""
    pools = [{"min_price": 82_900.0, "max_price": 83_000.0, "mid_price": 82_950.0,
              "size": 0.2782, "notional_usd": 23_055.66, "distance_pct": 0.11}]
    assert named_pool_inside_horizon(pools, side="LONG", **_LIVE_0324) is None


def test_pool_size_floor_matches_the_g7_wall_standard():
    assert MIN_POOL_NOTIONAL_USD == 150_000.0


def test_sufficient_pool_inside_horizon_is_returned_with_distance():
    pools = [{"mid_price": 82_950.0, "notional_usd": 23_055.66},   # too small
             {"mid_price": 82_941.96, "notional_usd": 900_000.0}]  # POC-sized
    got = named_pool_inside_horizon(pools, side="LONG", **_LIVE_0324)
    assert got is not None
    price, note, dist = got
    assert price == pytest.approx(82_941.96)
    assert note == pytest.approx(900_000.0)
    assert dist == pytest.approx((82_941.96 - 82_800.0) / 124.11, abs=1e-6)
    assert 0 < dist <= 4.0


def test_pool_beyond_the_horizon_is_rejected_even_when_large():
    """The standing 84,028.99 overhead pool is 8.51 ATR out -- size cannot save it."""
    pools = [{"price": 84_028.99, "notional_usd": 24_946_160.0}]
    assert named_pool_inside_horizon(pools, side="LONG", **_LIVE_0324) is None


def test_nearest_qualifying_pool_wins_regardless_of_list_order():
    pools = [{"mid_price": 83_200.0, "notional_usd": 500_000.0},   # +3.22 ATR
             {"mid_price": 82_950.0, "notional_usd": 400_000.0}]   # +1.21 ATR
    got = named_pool_inside_horizon(pools, side="LONG", **_LIVE_0324)
    assert got[0] == pytest.approx(82_950.0)


def test_short_side_looks_below_entry_and_ignores_pools_above():
    pools = [{"mid_price": 82_950.0, "notional_usd": 900_000.0},   # wrong side
             {"mid_price": 82_600.0, "notional_usd": 900_000.0}]   # -1.61 ATR
    got = named_pool_inside_horizon(pools, side="SHORT", **_LIVE_0324)
    assert got is not None and got[0] == pytest.approx(82_600.0)
    assert got[2] == pytest.approx((82_800.0 - 82_600.0) / 124.11, abs=1e-6)


def test_pool_selector_is_malformed_input_safe():
    assert named_pool_inside_horizon(None, side="LONG", **_LIVE_0324) is None
    assert named_pool_inside_horizon([], side="LONG", **_LIVE_0324) is None
    assert named_pool_inside_horizon([None, 5, "x", {}], side="LONG", **_LIVE_0324) is None
    assert named_pool_inside_horizon([{"mid_price": None, "notional_usd": 1e6}],
                                     side="LONG", **_LIVE_0324) is None
    assert named_pool_inside_horizon([{"mid_price": 82_950.0, "notional_usd": None}],
                                     side="LONG", **_LIVE_0324) is None
    assert named_pool_inside_horizon([{"mid_price": 82_950.0, "notional_usd": 1e6}],
                                     82_800.0, 0.0, side="LONG") is None
    assert named_pool_inside_horizon([{"mid_price": 82_950.0, "notional_usd": 1e6}],
                                     float("nan"), 124.11, side="LONG") is None
    assert named_pool_inside_horizon([{"mid_price": 82_950.0, "notional_usd": 1e6}],
                                     82_800.0, 124.11, max_dist_atr=0.0, side="LONG") is None
    assert named_pool_inside_horizon([{"mid_price": 82_950.0, "notional_usd": 1e6}],
                                     82_800.0, 124.11, min_notional_usd=float("nan"),
                                     side="LONG") is None


# ---------------------------------------------------------------------------
# A1_z_still_accelerating. Every pre-existing test supplied a vwap_z_change_4bars
# that PASSED this guard, so the rejecting direction was never covered -- even
# though it is the one that matters. Measured live at 2026-10-11 03:50:37 UTC,
# dz4 = (82,876.0 - 83,033.0) / 56.1188 = -2.7976, i.e. price had fallen 2.80
# session-sigma over four 15m bars while |Z| was crossing back above 2.0. The
# trigger looked live; the acceleration guard is what stops the desk buying it.
# ---------------------------------------------------------------------------

def test_z_acceleration_guard_rejects_the_live_falling_knife():
    """The measured 03:50 UTC pattern: trigger satisfied, acceleration fatal."""
    v = model1_checklist(_m1_ctx(direction="LONG", session_bars=20,
                                 atr=127.05, session_sigma=56.12,
                                 vwap_z=-1.71, sweep_z=-2.13,
                                 vwap_z_change_4bars=-2.7976))
    # LONG needs -side*z = +2.13 >= 2.0, so the trigger itself clears...
    assert "A1_z_below_2" not in v.failures
    assert "A1_z_beyond_3p5_cascade_zone" not in v.failures
    # ...but Z is still driving into the extreme, which is the reject.
    assert "A1_z_still_accelerating" in v.failures


def test_z_acceleration_guard_is_signed_by_direction():
    """The same dz4 is fatal for one side and acceptable for the other."""
    # dz4 = +1.2 (Z rising): fatal for a SHORT chasing up, fine for a LONG.
    up = dict(vwap_z_change_4bars=1.2)
    assert "A1_z_still_accelerating" in model1_checklist(
        _m1_ctx(direction="SHORT", session_bars=20, session_sigma=100.0, atr=100.0,
                vwap_z=2.4, sweep_z=2.4, **up)).failures
    assert "A1_z_still_accelerating" not in model1_checklist(
        _m1_ctx(direction="LONG", session_bars=20, session_sigma=100.0, atr=100.0,
                vwap_z=-2.4, sweep_z=-2.4, **up)).failures
    # Mirrored: dz4 = -1.2 is fatal for the LONG, fine for the SHORT.
    down = dict(vwap_z_change_4bars=-1.2)
    assert "A1_z_still_accelerating" in model1_checklist(
        _m1_ctx(direction="LONG", session_bars=20, session_sigma=100.0, atr=100.0,
                vwap_z=-2.4, sweep_z=-2.4, **down)).failures
    assert "A1_z_still_accelerating" not in model1_checklist(
        _m1_ctx(direction="SHORT", session_bars=20, session_sigma=100.0, atr=100.0,
                vwap_z=2.4, sweep_z=2.4, **down)).failures


def test_z_acceleration_guard_boundary_is_0p75_in_sigma_units():
    for side, dz4, expect in (("LONG", -0.75, False), ("LONG", -0.7501, True),
                              ("SHORT", 0.75, False), ("SHORT", 0.7501, True)):
        z = -2.4 if side == "LONG" else 2.4
        v = model1_checklist(_m1_ctx(direction=side, session_bars=20,
                                     session_sigma=100.0, atr=100.0,
                                     vwap_z=z, sweep_z=z, vwap_z_change_4bars=dz4))
        assert ("A1_z_still_accelerating" in v.failures) is expect, (side, dz4)


def test_at_the_live_0350_state_both_directions_are_independently_blocked():
    """Neither side is a hair away -- each is stopped by a different limb.

    LONG: trigger clears at |Z| 2.13 but dz4 = -2.7976 rejects on acceleration.
    SHORT: dz4 is acceptable, but -side*z = -1.71 never reaches the 2.0 floor.
    """
    live = dict(session_bars=20, atr=127.05, session_sigma=56.12,
                vwap_z_change_4bars=-2.7976)
    long_ = model1_checklist(_m1_ctx(direction="LONG", vwap_z=-1.71, sweep_z=-2.13, **live))
    short_ = model1_checklist(_m1_ctx(direction="SHORT", vwap_z=-1.71, sweep_z=-2.13, **live))
    assert "A1_z_still_accelerating" in long_.failures
    assert "A1_z_still_accelerating" not in short_.failures
    assert "A1_z_below_2" in short_.failures
    assert not long_.passed and not short_.passed


# ---------------------------------------------------------------------------
# A5 vs A1: the target anchor is measured from ENTRY, the trigger from the
# RECLAIMED SWEEP. Verified live on generation 90174a2ec7414f1996e97b6b2f7b6e54
# (2026-10-11 04:50:33 UTC): BTC sweep_z = -2.7007 (LONG) / +2.3230 (SHORT) so
# both directions clear A1_z_below_2, while ctx["vwap_z"] is only +0.4500 and the
# publisher's vwap_z_score only +0.61. A1 is therefore satisfiable by an extension
# that has ALREADY been reclaimed -- and A5 then refuses to trade it, because a
# mean-reversion target may not run past VWAP. These tests pin that asymmetry so a
# future refactor cannot silently make A1 and A5 disagree about which price is the
# extension.
# ---------------------------------------------------------------------------

_LIVE_0450 = dict(entry=82_910.5, atr=132.8556, vwap=82_861.72205265639,
                  session_bars=19, session_sigma=80.6175,
                  vwap_slope_sigma_per_bar=-0.0018045616603178103,
                  vwap_z=0.45000084074022156, vwap_z_change_4bars=0.2729,
                  vol_ratio_4_96=1.5022)


def test_a1_z_limbs_read_the_reclaimed_sweep_extreme_not_the_live_extension():
    """At 04:50 both directions clear the Z limbs off sweep_z while vwap_z is 0.45."""
    long_ = model1_checklist(_m1_ctx(direction="LONG", sweep_z=-2.7006794462510153,
                                     sweep_extreme=82_644.0, **_LIVE_0450))
    short_ = model1_checklist(_m1_ctx(direction="SHORT", sweep_z=2.3230430585972166,
                                      sweep_extreme=83_049.0, **_LIVE_0450))
    for v in (long_, short_):
        assert "A1_z_below_2" not in v.failures
        assert "A1_z_beyond_3p5_cascade_zone" not in v.failures
    # The live session-VWAP extension alone would never reach the trigger.
    assert abs(_LIVE_0450["vwap_z"]) < 2.0


def test_the_live_0450_a1_is_reduced_to_the_sigma_limb_alone():
    """Nine cycles of A1 rejections narrowed to exactly one failing limb.

    04:20 UTC failed A1_session_sigma_lt_0p8atr, A1_vwap_sloped (-0.19218) and
    A1_z_still_accelerating. By 04:50 the slope had flattened to -0.0018 and dz4
    to +0.2729, leaving the sigma floor (80.6175 vs 106.2845) as the only A1
    rejection. Pin this so a regression in the slope/acceleration limbs is caught
    by a change in this list rather than by a silent trade.
    """
    long_ = model1_checklist(_m1_ctx(direction="LONG", sweep_z=-2.7006794462510153,
                                     sweep_extreme=82_644.0, **_LIVE_0450))
    assert [f for f in long_.failures if f.startswith("A1_")] == ["A1_session_sigma_lt_0p8atr"]
    assert _LIVE_0450["session_sigma"] < 0.8 * _LIVE_0450["atr"]
    assert 0.8 * _LIVE_0450["atr"] - _LIVE_0450["session_sigma"] == pytest.approx(25.6670, abs=1e-3)


def test_clearing_the_sigma_limb_alone_does_not_admit_a_trade():
    """The sigma floor is the last A1 limb, not the binding constraint.

    Counterfactual verified against the live 04:50 payload: lifting session_sigma
    to 0.8*ATR + 1 empties the A1 list, yet A2 (no tape), A3 (no eligible whale
    wall behind entry) and A5/EV all still reject. A desk waiting on session
    maturity alone is waiting on the wrong limb.
    """
    # Live 04:50 sizing: 15.00 USD risk on a 1.5 ATR (199.2834) stop, so the
    # round-trip spread cost is 15.0 USD * 15.0/199.2834 = 1.1290 USD = 0.0753 R.
    ctx = _m1_ctx(direction="LONG", sweep_z=-2.7006794462510153, sweep_extreme=82_644.0,
                  wall=None, orderflow=None, p_win_lower_bound=None,
                  round_trip_cost_usd=1.12904536955913, **_LIVE_0450)
    ctx["sl"] = ctx["entry"] - 1.5 * ctx["atr"]
    ctx["tp"] = ctx["entry"] + 2.5 * 1.5 * ctx["atr"]
    assert [f for f in model1_checklist(ctx).failures if f.startswith("A1_")] == \
        ["A1_session_sigma_lt_0p8atr"]
    lifted = dict(ctx, session_sigma=0.8 * ctx["atr"] + 1.0)
    remaining = model1_checklist(lifted).failures
    assert not any(f.startswith("A1_") for f in remaining)
    # wall/orderflow are None, so both fail CLOSED rather than vacuously skipping.
    for expected in ("A2_no_tape_fail_closed", "A3_no_wall_fail_closed",
                     "A5_tp_beyond_vwap", "EV_p_win_lower_bound_missing"):
        assert expected in remaining, expected
    # Correctly sized friction is well inside the 0.15 R cap -- it is not what
    # stops this trade, and the test must not imply otherwise.
    assert "EV_friction_gt_0p15R" not in remaining


def test_a_mean_reversion_long_is_geometrically_locked_out_while_price_sits_above_vwap():
    """A5_tp_beyond_vwap and A5_invalid_protective_bracket are jointly unsatisfiable.

    The bracket limb needs side*(tp - entry) > 0, the anchor limb needs
    side*(vwap - tp) >= 0. With entry > vwap a LONG therefore needs
    tp > entry > vwap >= tp. No TP exists. This is a structural lock, not a
    calibration miss, and it holds for every TP the desk could stage.
    """
    entry, vwap = _LIVE_0450["entry"], _LIVE_0450["vwap"]
    assert entry > vwap
    for tp in (entry + 1.0, entry + 100.0, vwap + (entry - vwap) / 2, entry + 10_000.0):
        v = model1_checklist(_m1_ctx(direction="LONG", tp=tp, sweep_z=-2.7006794462510153,
                                     sweep_extreme=82_644.0, **_LIVE_0450))
        assert "A5_tp_beyond_vwap" in v.failures, tp


def test_a_vwap_anchored_short_cannot_reach_min_rr_at_the_live_0450_offset():
    """Max R for a VWAP-anchored reversion is |entry - vwap| / (1.5 * ATR).

    Live 04:50: 48.7779 / 199.2834 = 0.2448 R against a 1.5 minimum. Reaching
    1.5 needs |entry - vwap| >= 2.25 * ATR = 298.93 USD; the live offset is short
    by 250.15 USD (1.88 ATR). The SHORT is the only direction A5 leaves open, and
    it has no room to pay for its own stop.
    """
    entry, vwap, atr = _LIVE_0450["entry"], _LIVE_0450["vwap"], _LIVE_0450["atr"]
    stop = 1.5 * atr
    max_rr = abs(entry - vwap) / stop
    assert max_rr == pytest.approx(0.2448, abs=1e-4)
    assert max_rr < 1.5
    assert 1.5 * stop - abs(entry - vwap) == pytest.approx(250.15, abs=0.05)
    v = model1_checklist(_m1_ctx(direction="SHORT", tp=vwap, sl=entry + stop,
                                 sweep_z=2.3230430585972166, sweep_extreme=83_049.0,
                                 **_LIVE_0450))
    assert "EV_rr_below_1.5" in v.failures
    assert "A5_tp_beyond_vwap" not in v.failures


# ---------------------------------------------------------------------------
# Generation 1eb3a3ff37e94205851e05d218eb92af (2026-10-11 05:20:51 UTC).
#
# MEAN_REVERT is the ONLY regime that admits Model 1, and it requires
# 15m vr_z < vr_z_mr. On the 05:00 bar the live 15m vr_z was
# -1.499972800508274 -- a deficit of 2.72e-05, i.e. 27 parts per million, from
# the -1.5 threshold. On the 05:15 bar it was -1.4970742598814974, a deficit of
# 2.93e-03. Two consecutive bars missed the sole gateway to Model 1 by less than
# three thousandths of a sigma-unit, while 1h ER (0.1377 vs 0.20) and 4h ER
# (0.2692 vs 0.30) both passed. A hard binary admission gate sitting on a
# continuous estimator is a coin flip at this precision. These tests pin the live
# numbers so the boundary cannot move silently, and so any future hysteresis
# proposal is measured against a recorded event rather than a recollection.
#
# NOTE: no gate behaviour is changed here. RegimeParams.vr_z_mr stays -1.5.
# ---------------------------------------------------------------------------

_LIVE_0520_C15 = [
    82620.0, 82627.0, 82604.0, 82718.0, 82772.0, 82694.0, 82710.0, 82798.0, 82669.0,
    82591.0, 82561.0, 82677.0, 82725.0, 82785.31, 82772.51, 82753.7, 82797.3, 82804.0,
    82821.0, 82806.0, 82793.0, 82759.0, 82687.0, 82734.0, 82777.0, 82730.0, 82730.0,
    82832.0, 82790.0, 82786.0, 82781.0, 82783.0, 82732.0, 82736.0, 82779.0, 82715.0,
    82754.0, 82711.0, 82873.0, 82942.0, 82906.0, 82887.0, 82900.0, 82955.0, 82954.0,
    82944.0, 82916.0, 82961.0, 82936.0, 82979.0, 82958.0, 83040.0, 83022.0, 82959.0,
    82928.0, 82937.0, 82947.0, 82933.0, 82954.0, 82993.0, 82994.0, 82967.0, 82947.0,
    82990.0, 82958.0, 82916.0, 82970.0, 83002.0, 82954.0, 82940.0, 82953.0, 82967.0,
    83008.0, 82958.0, 82959.0, 82926.0, 82891.0, 82935.0, 82869.0, 82876.0, 82886.0,
    82900.0, 82933.0, 82929.0, 82943.0, 82950.0, 82960.0, 83033.0, 82991.0, 82879.0,
    82830.0, 82876.0, 82717.0, 82781.0, 82816.0, 82898.0, 82916.0
]

_LIVE_0520_C1H = [
    82165.0, 82272.0, 82502.5, 82559.5, 82611.5, 82585.5, 82476.0, 83164.5, 82950.5,
    82542.0, 82954.0, 82793.5, 82661.5, 82641.5, 82366.5, 82240.0, 82413.0, 82465.0,
    82548.0, 82540.0, 82479.0, 82615.0, 82556.0, 82514.0, 82620.0, 82772.0, 82669.0,
    82725.0, 82797.3, 82793.0, 82777.0, 82790.0, 82732.0, 82754.0, 82906.0, 82954.0,
    82936.0, 83022.0, 82947.0, 82994.0, 82958.0, 82954.0, 83008.0, 82891.0, 82886.0,
    82943.0, 82991.0, 82717.0, 82916.0
]

_LIVE_0520_C4H = [
    85603.0, 86001.5, 86184.0, 85581.5, 85593.0, 85525.0, 84076.0, 83912.5, 83452.0,
    83329.5, 83396.0, 83315.0, 82582.0, 82806.5, 82244.0, 80865.5, 81760.0, 81721.0,
    82165.0, 82611.5, 82950.5, 82661.5, 82413.0, 82479.0, 82620.0, 82797.3, 82732.0,
    82936.0, 82958.0, 82886.0, 82916.0
]


_LIVE_0520_TF = dict(last_close_epoch=1_791_695_700.0, as_of_epoch=1_791_695_701.0)


def test_the_live_0520_regime_missed_mean_revert_by_27_parts_per_million():
    """The 05:00-bar vr_z was -1.4999728: UNDEFINED by 2.72e-05."""
    regime, stats = classify_regime(_LIVE_0520_C15, _LIVE_0520_C1H, _LIVE_0520_C4H,
                                    **_LIVE_0520_TF)
    vr_z = stats["15m"]["vr_z"]
    assert vr_z == pytest.approx(-1.499972800508274, abs=1e-12)
    assert RegimeParams().vr_z_mr == -1.5
    assert vr_z - (-1.5) == pytest.approx(2.71995e-05, abs=1e-9)
    assert regime == "UNDEFINED"
    # The other two MEAN_REVERT limbs passed comfortably -- vr_z was the sole
    # discriminator, so the whole Model 1 gateway turned on 27 ppm.
    assert stats["1h"]["er"] < RegimeParams().er_mr
    assert stats["4h"]["er"] < 0.30
    assert not stats["stale"]


def test_a_27ppm_shift_in_the_vr_z_threshold_flips_the_only_admissible_regime():
    """Same series, threshold moved by less than the live deficit -> MEAN_REVERT.

    This is the sensitivity statement: nothing about the market changed, only the
    fourth decimal place of a policy constant.
    """
    tight = classify_regime(_LIVE_0520_C15, _LIVE_0520_C1H, _LIVE_0520_C4H,
                            **_LIVE_0520_TF)[0]
    relaxed = classify_regime(_LIVE_0520_C15, _LIVE_0520_C1H, _LIVE_0520_C4H,
                              p=RegimeParams(vr_z_mr=-1.4999), **_LIVE_0520_TF)[0]
    assert tight == "UNDEFINED"
    assert relaxed == "MEAN_REVERT"


def test_the_0515_bar_missed_by_2p9_thousandths_and_the_miss_is_stable_within_a_bar():
    """The next bar's vr_z was -1.4970743, and it is frozen until the next close.

    The 15m stats only recompute on a bar close, so all fourteen snapshots from
    05:15:52 to 05:28:50 UTC carried the identical value. A boundary miss here is
    not intra-bar noise -- it is a fixed verdict for fifteen minutes, re-drawn at
    the next close.
    """
    assert -1.4970742598814974 - (-1.5) == pytest.approx(2.9257401e-03, abs=1e-9)
    assert abs(-1.4970742598814974) < 1.5


# ---------------------------------------------------------------------------
# A5 geometry at 05:20: BOTH directions are now locked out, for mirror-image
# reasons. At 04:50 only the LONG was (entry above VWAP). By 05:20 the SHORT is
# locked too: A5_entry_not_inside_sweep needs entry < sweep_extreme (82,969.0)
# while RR 1.5 against a 1.5 ATR stop with the target capped at VWAP needs
# entry >= vwap + 1.5*stop = 83,145.17. Those are 176.17 USD apart.
# ---------------------------------------------------------------------------

_LIVE_0520 = dict(entry=82_970.5, atr=124.35, vwap=82_865.38716080518,
                  session_bars=21, session_sigma=79.61590573571561,
                  vwap_slope_sigma_per_bar=0.02985934395632176,
                  vwap_z=0.9120393534911577, vwap_z_change_4bars=1.9719677688671946,
                  vol_ratio_4_96=0.7294142582471651, reclaim_close=True)


def test_at_the_live_0520_state_both_directions_are_geometrically_locked_by_a5():
    """LONG: no TP satisfies tp > entry and tp <= vwap. SHORT: no entry satisfies
    entry < sweep_extreme and entry >= vwap + 1.5*stop."""
    entry, vwap, atr = _LIVE_0520["entry"], _LIVE_0520["vwap"], _LIVE_0520["atr"]
    stop = 1.5 * atr
    assert entry > vwap
    for tp in (entry + 1.0, vwap + (entry - vwap) / 2, entry + 10_000.0):
        v = model1_checklist(_m1_ctx(direction="LONG", tp=tp, sl=entry - stop,
                                     regime="MEAN_REVERT", sweep_z=-2.780690099037219,
                                     sweep_extreme=82_644.0, **_LIVE_0520))
        assert "A5_tp_beyond_vwap" in v.failures, tp
    # SHORT: the two A5/EV requirements on entry are mutually exclusive.
    max_entry_for_sweep = 82_969.0
    min_entry_for_rr = vwap + 1.5 * stop
    assert min_entry_for_rr == pytest.approx(83_145.17, abs=0.05)
    assert min_entry_for_rr - max_entry_for_sweep == pytest.approx(176.17, abs=0.05)
    v = model1_checklist(_m1_ctx(direction="SHORT", tp=vwap, sl=entry + stop,
                                 regime="MEAN_REVERT", sweep_z=1.3014087855604763,
                                 sweep_extreme=82_969.0, **_LIVE_0520))
    assert "A5_entry_not_inside_sweep" in v.failures
    assert "EV_rr_below_1.5" in v.failures
    assert "A5_tp_beyond_vwap" not in v.failures


def test_the_first_qualified_exit_anchor_of_the_session_sits_below_vwap_and_is_unusable():
    """A sell-stop cluster at 82,750.0 finally qualifies -- and A5 refuses it.

    named_pool_inside_horizon returned its first non-None result of the session:
    (82750.0, 7060213.45 USD, 1.7732 ATR). It clears both the 4.0 ATR horizon and
    the 150k size floor. But 82,750.0 < VWAP 82,865.39, so a SHORT targeting it
    runs past the mean and A5_tp_beyond_vwap rejects it. A reachable, named,
    sized pool is not automatically a legal target.
    """
    pools = [{"min_price": 82_700.0, "max_price": 82_800.0, "mid_price": 82_750.0,
              "size": 84.85, "notional_usd": 7_060_213.45, "distance_pct": -0.27}]
    anchor = named_pool_inside_horizon(pools, side="SHORT",
                                       entry=_LIVE_0520["entry"], atr=_LIVE_0520["atr"])
    assert anchor is not None
    price, notional, dist = anchor
    assert price == 82_750.0
    assert notional >= MIN_POOL_NOTIONAL_USD
    assert dist == pytest.approx(1.7732, abs=1e-3)
    v = model1_checklist(_m1_ctx(direction="SHORT", tp=price,
                                 sl=_LIVE_0520["entry"] + 1.5 * _LIVE_0520["atr"],
                                 regime="MEAN_REVERT", sweep_z=1.3014087855604763,
                                 sweep_extreme=82_969.0, **_LIVE_0520))
    assert "A5_tp_beyond_vwap" in v.failures


# ---------------------------------------------------------------------------
# Generation 372c3b6eb5ad42d6b9014559f70845ce (2026-10-11 05:50:09 UTC).
#
# Three cycles of convergence, verified from the snapshots:
#   cycle   ATR       0.8*ATR    sigma     sigma shortfall   offset    1.6*ATR shortfall
#   04:50   132.8556  106.2845   80.6175   25.6670           48.7779   163.7911
#   05:20   124.3500   99.4800   79.6159   19.8641          105.1128    93.8472
#   05:50   120.9956   96.7965   80.3485   16.4480          105.2317    88.3613
#
# The sigma shortfall is closing ~4.6 USD per cycle while the offset shortfall is
# closing ~5 USD per cycle from a much larger base. At the live offset the two A1
# limbs are mutually exclusive: sigma >= 0.8*ATR forces |vwap_z| to 1.0871, below
# the 2.0 trigger. A1 stays alive only because it reads sweep_z, not vwap_z -- at
# the floor sigma, sweep_z is still -2.3531. Which Z the trigger reads therefore
# decides whether session maturation retires the setup or preserves it.
# ---------------------------------------------------------------------------

_LIVE_0550 = dict(atr=120.9956, entry=82_977.0, vwap=82_871.76827280433,
                  session_sigma=80.34849785747018, session_bars=23,
                  vwap_slope_sigma_per_bar=0.0346365134303889,
                  vwap_z=1.3594744159304195, vwap_z_change_4bars=1.0330000213225308,
                  vol_ratio_4_96=0.6956680596469594, reclaim_close=True)
_SWEEP_LONG_0550 = 82_644.0
_SWEEP_SHORT_0550 = 83_005.0


def test_the_live_0550_a1_sigma_and_z_limbs_are_mutually_exclusive_on_mid_price():
    """sigma >= 0.8*ATR forces |vwap_z| below the 2.0 trigger at this offset."""
    offset = _LIVE_0550["entry"] - _LIVE_0550["vwap"]
    floor = 0.8 * _LIVE_0550["atr"]
    assert offset == pytest.approx(105.2317, abs=1e-3)
    assert floor - _LIVE_0550["session_sigma"] == pytest.approx(16.4480, abs=1e-3)
    # The coupling: sigma >= 0.8*ATR AND |Z| >= 2.0 together need 1.6*ATR of offset.
    assert 1.6 * _LIVE_0550["atr"] - offset == pytest.approx(88.3613, abs=1e-3)
    # At the floor sigma the mid-referenced Z collapses below the trigger.
    assert offset / floor == pytest.approx(1.0871, abs=1e-4)


def test_maturing_sigma_preserves_the_trigger_only_because_a1_reads_sweep_z():
    """At the floor sigma, sweep_z is -2.3531 (passes) while vwap_z is +1.0871 (fails).

    This is the operative consequence of the sweep-vs-mid asymmetry pinned at
    04:50: session maturation would retire a vwap_z-triggered Model 1 but leaves a
    sweep_z-triggered one alive. The choice of reference is the whole difference.
    """
    floor = 0.8 * _LIVE_0550["atr"]
    sweep_z_at_floor = (_SWEEP_LONG_0550 - _LIVE_0550["vwap"]) / floor
    vwap_z_at_floor = (_LIVE_0550["entry"] - _LIVE_0550["vwap"]) / floor
    assert sweep_z_at_floor == pytest.approx(-2.3531, abs=1e-4)
    assert vwap_z_at_floor == pytest.approx(1.0871, abs=1e-4)
    assert abs(sweep_z_at_floor) >= 2.0
    assert abs(vwap_z_at_floor) < 2.0


def test_the_sigma_shortfall_is_closing_faster_than_the_offset_shortfall():
    """The three-cycle convergence series, verified from the published snapshots."""
    series = [  # (atr, sigma, offset)
        (132.8556, 80.6175, 48.7779),
        (124.3500, 79.6159, 105.1128),
        (120.9956, 80.3485, 105.2317),
    ]
    sig_short = [0.8 * atr - sig for atr, sig, _ in series]
    off_short = [1.6 * atr - off for atr, _, off in series]
    assert sig_short == pytest.approx([25.6670, 19.8641, 16.4480], abs=1e-3)
    assert off_short == pytest.approx([163.7911, 93.8472, 88.3613], abs=1e-3)
    # Sigma is nearly home; the offset that the coupling actually requires is not.
    assert sig_short[-1] / sig_short[0] == pytest.approx(0.6408, abs=1e-3)
    assert off_short[-1] / off_short[0] == pytest.approx(0.5395, abs=1e-3)
    assert off_short[-1] > 5 * sig_short[-1]


def test_the_live_0550_short_gained_a_sweep_high_but_lost_two_a1_limbs_instead():
    """The blocking limb rotates every cycle; the count never reaches zero.

    At 05:20 the SHORT failed A5_entry_not_inside_sweep (sweep_extreme 82,969.0 sat
    1.5 USD BELOW mid). By 05:50 sweep_extreme is 83,005.0, above mid, so that limb
    clears -- and A1_z_below_2 (sweep_z +1.6582) plus A1_z_still_accelerating
    (dz4 +1.0330) reject instead. Clearing one limb is not progress toward a trade.
    """
    stop = 1.5 * _LIVE_0550["atr"]
    ctx = dict(_LIVE_0550, direction="SHORT", regime="MEAN_REVERT",
               sweep_z=1.6581732172766934, sweep_extreme=_SWEEP_SHORT_0550,
               sl=_LIVE_0550["entry"] + stop, tp=_LIVE_0550["entry"] - stop,
               risk_usd=15.0, round_trip_cost_usd=16.0 * (15.0 / stop),
               wall=None, orderflow=None, p_win_lower_bound=None,
               tick=0.01, spread=16.0, sigma_bar=0.0012, structure_intact=True,
               exhaustion_flags={"vol_spike": False, "long_wick": False},
               geometry={"retrace": 0.5, "depth_sigma": 1.0, "velocity_ratio": 1.0,
                         "bars_pullback": 4, "bars_impulse": 8},
               shelf={"price": None, "confluence": 0}, first_obstacle=None,
               allow_price_only_variant=False, m1_range_override=None)
    v = model1_checklist(ctx)
    assert "A5_entry_not_inside_sweep" not in v.failures
    assert "A1_z_below_2" in v.failures
    assert "A1_z_still_accelerating" in v.failures
    assert not v.passed


def test_gate_b1_prefers_entry_z_for_limit_orders():
    """Verify B1 evaluates entry_z rather than completed bar vwap_z when supplied."""
    base_ctx = {
        "direction": "LONG",
        "regime": "TREND_UP",
        "atr": 10.0,
        "sigma_bar": 0.005,
        "geometry": {
            "retrace": 0.382,
            "depth_sigma": 1.2,
            "velocity_ratio": 0.45,
            "bars_pullback": 5,
            "bars_impulse": 12,
        },
        "structure_intact": True,
        "exhaustion_flags": {"vol_spike": False, "long_wick": False},
        "shelf": {"price": 100.0, "confluence": 3},
        "entry": 100.0,
        "sl": 83.0,
        "tp": 135.0,
        "first_obstacle": 140.0,
        "tick": 0.1,
        "risk_usd": 10.0,
        "round_trip_cost_usd": 0.6,
        "p_win_lower_bound": 0.60,
        "wall": {
            "usd": 200000.0, "persist_s": 200.0, "presence_frac": 1.0,
            "dist_from_entry_atr": 0.1, "median_1m_traded_usd": 25000.0,
            "wall_class": "GENUINE", "gate_g7_eligible": True,
        },
        "allow_price_only_variant": True,
    }

    # Case 1: completed bar close is stretched at +2.50 SD, but entry_z is +0.35 SD.
    ctx_entry_pass = dict(base_ctx, vwap_z=2.50, entry_z=0.35)
    v_pass = model2_checklist(ctx_entry_pass)
    assert "B1_z_outside_model2_location_bound" not in v_pass.failures

    # Case 2: entry_z itself is stretched at +2.50 SD -> must fail even if vwap_z is +0.35 SD.
    ctx_entry_fail = dict(base_ctx, vwap_z=0.35, entry_z=2.50)
    v_fail = model2_checklist(ctx_entry_fail)
    assert "B1_z_outside_model2_location_bound" in v_fail.failures


def test_gate_b2_relaxed_velocity_ratio_under_3_bars():
    """Verify B2 velocity_ratio relaxation (6.0 vs 0.60) based on pullback bar count."""
    base_ctx = {
        "direction": "LONG",
        "regime": "TREND_UP",
        "atr": 10.0,
        "sigma_bar": 0.005,
        "structure_intact": True,
        "exhaustion_flags": {"vol_spike": False, "long_wick": False},
        "shelf": {"price": 100.0, "confluence": 3},
        "entry": 100.0,
        "sl": 83.0,
        "tp": 135.0,
        "first_obstacle": 140.0,
        "tick": 0.1,
        "risk_usd": 10.0,
        "round_trip_cost_usd": 0.6,
        "p_win_lower_bound": 0.60,
        "wall": {
            "usd": 200000.0, "persist_s": 200.0, "presence_frac": 1.0,
            "dist_from_entry_atr": 0.1, "median_1m_traded_usd": 25000.0,
            "wall_class": "GENUINE", "gate_g7_eligible": True,
        },
        "allow_price_only_variant": True,
    }

    # Pullback has only 2 bars and velocity_ratio = 2.5: allowed under relaxed bound (<= 6.0).
    ctx_fast_turn = dict(base_ctx, geometry={
        "retrace": 0.382,
        "depth_sigma": 1.2,
        "velocity_ratio": 2.5,
        "bars_pullback": 2,
        "bars_impulse": 12,
    })
    v_fast = model2_checklist(ctx_fast_turn)
    assert "B2_pullback_velocity_ge_impulse" not in v_fast.failures

    # Pullback has 4 bars and velocity_ratio = 2.5: must reject under standard bound (<= 0.60).
    ctx_mature_fast = dict(base_ctx, geometry={
        "retrace": 0.382,
        "depth_sigma": 1.2,
        "velocity_ratio": 2.5,
        "bars_pullback": 4,
        "bars_impulse": 12,
    })
    v_mature = model2_checklist(ctx_mature_fast)
    assert "B2_pullback_velocity_ge_impulse" in v_mature.failures

    # Pullback has 2 bars and velocity_ratio = 7.0: must reject even under relaxed bound (> 6.0).
    ctx_excessive = dict(base_ctx, geometry={
        "retrace": 0.382,
        "depth_sigma": 1.2,
        "velocity_ratio": 7.0,
        "bars_pullback": 2,
        "bars_impulse": 12,
    })
    v_excessive = model2_checklist(ctx_excessive)
    assert "B2_pullback_velocity_ge_impulse" in v_excessive.failures


def test_gate_b6_allow_trend_continuation_target():
    """Verify B6 allow_trend_continuation_target allows targets beyond first obstacle."""
    base_ctx = {
        "direction": "LONG",
        "regime": "TREND_UP",
        "atr": 10.0,
        "sigma_bar": 0.005,
        "geometry": {
            "retrace": 0.382,
            "depth_sigma": 1.2,
            "velocity_ratio": 0.45,
            "bars_pullback": 5,
            "bars_impulse": 12,
        },
        "structure_intact": True,
        "exhaustion_flags": {"vol_spike": False, "long_wick": False},
        "shelf": {"price": 100.0, "confluence": 3},
        "entry": 100.0,
        "sl": 83.0,
        "tp": 135.0,  # Target is beyond first obstacle at 120.0
        "first_obstacle": 120.0,
        "tick": 0.1,
        "risk_usd": 10.0,
        "round_trip_cost_usd": 0.6,
        "p_win_lower_bound": 0.60,
        "wall": {
            "usd": 200000.0, "persist_s": 200.0, "presence_frac": 1.0,
            "dist_from_entry_atr": 0.1, "median_1m_traded_usd": 25000.0,
            "wall_class": "GENUINE", "gate_g7_eligible": True,
        },
        "allow_price_only_variant": True,
    }

    # Case 1: default allow_trend_continuation_target=False -> fails B6_tp_beyond_first_obstacle.
    v_blocked = model2_checklist(dict(base_ctx, allow_trend_continuation_target=False))
    assert "B6_tp_beyond_first_obstacle" in v_blocked.failures

    # Case 2: allow_trend_continuation_target=True -> passes B6 obstacle check.
    v_allowed = model2_checklist(dict(base_ctx, allow_trend_continuation_target=True))
    assert "B6_tp_beyond_first_obstacle" not in v_allowed.failures


def test_gate_b4_allow_price_only_variant_when_depth_certified():
    """Verify B4 allow_price_only_variant cleanly bypasses missing tape requirement."""
    base_ctx = {
        "direction": "LONG",
        "regime": "TREND_UP",
        "atr": 10.0,
        "sigma_bar": 0.005,
        "geometry": {
            "retrace": 0.382,
            "depth_sigma": 1.2,
            "velocity_ratio": 0.45,
            "bars_pullback": 5,
            "bars_impulse": 12,
        },
        "structure_intact": True,
        "exhaustion_flags": {"vol_spike": False, "long_wick": False},
        "shelf": {"price": 100.0, "confluence": 3},
        "entry": 100.0,
        "sl": 83.0,
        "tp": 135.0,
        "first_obstacle": 140.0,
        "tick": 0.1,
        "risk_usd": 10.0,
        "round_trip_cost_usd": 0.6,
        "p_win_lower_bound": 0.60,
        "wall": {
            "usd": 200000.0, "persist_s": 200.0, "presence_frac": 1.0,
            "dist_from_entry_atr": 0.1, "median_1m_traded_usd": 25000.0,
            "wall_class": "GENUINE", "gate_g7_eligible": True,
        },
        "orderflow": None,  # tape missing
    }

    # Case 1: allow_price_only_variant=False -> fails B4_no_tape_fail_closed.
    v_fail = model2_checklist(dict(base_ctx, allow_price_only_variant=False))
    assert "B4_no_tape_fail_closed" in v_fail.failures

    # Case 2: allow_price_only_variant=True -> passes B4.
    v_pass = model2_checklist(dict(base_ctx, allow_price_only_variant=True))
    assert "B4_no_tape_fail_closed" not in v_pass.failures

