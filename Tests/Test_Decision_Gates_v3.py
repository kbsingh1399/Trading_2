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
                 "dist_from_entry_atr": .1, "median_1m_traded_usd": 25000.0},
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
                 "dist_from_entry_atr": .1, "median_1m_traded_usd": 25000.0},
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
                         dist_from_entry_atr=.1, median_1m_traded_usd=25000.0))
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
