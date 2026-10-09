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
