import math
import numpy as np
import pytest
from Terminal.dg_hardening import (
    BasisDecision, basis_drift_decision, translate_wall_distance,
    select_backing_wall, quantize_to_tick, robust_basis_sigma,
    gap_stressed_loss, joint_floor_check, clopper_pearson_bounds,
    binary_ev_lower, ternary_ev_lower, causal_dz4, reclaim_close_strict,
    drift_tstat_nw, discrete_order_checks, derive_m1_range_override,
)

ATR, TICK = 100.0, 0.5


def ok_decision(**kw):
    base = dict(broker_mid=83010.0, venue_mid=83000.0, b_hat=10.0, atr=ATR, tick=TICK,
                broker_ts=1000.0, venue_ts=1000.5)
    base.update(kw)
    return basis_drift_decision(**base)


# ---- Option A' ---------------------------------------------------------------
def test_cold_start_fails_closed():
    assert ok_decision(b_hat=None).reason == "venue_basis_cold_start"


def test_missing_venue_mid_fails_closed():
    assert ok_decision(venue_mid=None).reason == "venue_basis_mid_unavailable"


def test_clock_skew_and_unverified_clock():
    assert ok_decision(venue_ts=1060.0).reason == "venue_basis_clock_skew"
    assert ok_decision(venue_ts=None).reason == "venue_basis_clock_unverified"


def test_drift_trips_and_sigma_scaling():
    assert not ok_decision(broker_mid=83040.0).ok  # drift 30 > 25 cap
    tight = [10.0 + 0.1 * (i % 3) for i in range(20)]
    d = ok_decision(broker_mid=83013.0, basis_samples=tight)  # drift 3, tol ~4*sigma_b
    assert d.tol < 25.0 and not d.ok


def test_tol_never_below_two_ticks():
    d = ok_decision(basis_samples=[10.0] * 20)  # sigma_b = 0
    assert d.ok and d.tol == pytest.approx(2 * TICK)


def test_regime_shift_detected():
    assert ok_decision(b_hat_long=-40.0).reason == "venue_basis_regime_shift"


def test_error_budgeted_band():
    d = BasisDecision(True, "ok", b_now=10.0, b_hat=10.0, drift=5.0)
    ok, dist, wall, _ = translate_wall_distance(83000.0, 82980.0, 1, d, ATR, TICK)
    assert ok and wall == 82990.0 and dist == pytest.approx(0.15)
    ok, _, _, why = translate_wall_distance(83000.0, 82968.0, 1, d, ATR, TICK)  # 0.22+0.05
    assert not ok and why == "wall_outside_band_after_basis_error"
    ok, _, _, why = translate_wall_distance(83000.0, 82988.0, 1, d, ATR, TICK)  # 0.02-0.05
    assert not ok and why == "wall_not_behind_entry_within_basis_error"


def test_quantize():
    assert quantize_to_tick(100.26, 0.25) == 100.25 and quantize_to_tick(1, 0) is None


def wall(**kw):
    w = dict(side="BUY", price=82980.0, notional_usd=300_000.0, persist_s=400.0,
             presence_frac=0.95, gate_g7_eligible=True, wall_class="GENUINE",
             address="0xabc", venue="BINANCE")
    w.update(kw)
    return w


def quotes(**kw):
    q = dict(mid=83000.0, ts=1000.0, b_hat=10.0, b_hat_long=None, samples=None)
    q.update(kw)
    return {"BINANCE": q}


def test_select_wall_happy_and_grid_excluded():
    ctx, _ = select_backing_wall([wall()], entry=83000.0, side=1, atr=ATR, tick=TICK,
                                 broker_mid=83010.0, broker_ts=1000.0, venue_quotes=quotes())
    assert ctx and ctx["venue"] == "BINANCE" and ctx["dist_from_entry_atr"] <= 0.25
    ctx, diag = select_backing_wall([wall()], entry=83000.0, side=1, atr=ATR, tick=TICK,
                                    broker_mid=83010.0, broker_ts=1000.0, venue_quotes=quotes(),
                                    grid_addrs={"0xabc"})
    assert ctx is None and diag["rejections"]["two_sided_grid"] == 1


def test_select_wall_no_quote_for_venue_fails_closed():
    ctx, diag = select_backing_wall([wall(venue="HYPERLIQUID")], entry=83000.0, side=1, atr=ATR, tick=TICK,
                                    broker_mid=83010.0, broker_ts=1000.0, venue_quotes=quotes())
    assert ctx is None and "venue_basis_mid_unavailable" in diag["rejections"]


def test_robust_sigma_min_samples():
    assert robust_basis_sigma([1.0] * 3) is None


# ---- Floor -------------------------------------------------------------------
def sp500(**kw):
    a = dict(direction="LONG", entry=7770.0, sl=7761.5, volume=0.13,
             usd_per_price_unit_per_lot=10.0, asset_class="INDEX",
             crosses_session_close=True)
    a.update(kw)
    return gap_stressed_loss(**a)


def test_weekend_gap_dominates_and_breaches_floor():
    loss = sp500()
    assert loss > 250.0
    assert not joint_floor_check(4896.55, 4896.55, [loss])["ok"]


def test_intraday_still_above_legacy():
    legacy = 1.25 * 8.5 * 1.3 + 2.0
    assert sp500(crosses_session_close=False) >= legacy


def test_breakeven_stop_is_not_zero_risk():
    assert sp500(sl=7770.0) > 2.0


def test_floor_check_fail_closed():
    assert not joint_floor_check(None, 1, [])["ok"]
    assert not joint_floor_check(5000, 5000, [float("nan")])["ok"]


# ---- Expectancy ----------------------------------------------------------------
def test_clopper_pearson_matches_snapshot():
    lo, hi = clopper_pearson_bounds(11, 17)
    assert lo == pytest.approx(0.4197, abs=1e-3) and lo < 11 / 17 < hi


def test_ternary_flips_sign_vs_binary():
    assert binary_ev_lower(11, 17, rr=2.5, cost_r=0.05) > 0.2
    t = ternary_ev_lower(6, 5, 6, rr=2.5, cost_r=0.05)
    assert t["ev_lower_r"] < 0
    assert t["p_tp_lower"] + t["p_scratch"] + t["p_sl_upper"] == pytest.approx(1.0)


def test_bounds_invalid():
    assert clopper_pearson_bounds(5, 3) is None and clopper_pearson_bounds(1, 0) is None


# ---- dz4 / reclaim / regime --------------------------------------------------
def bars_from(closes, vol=100.0, wick=0.5):
    return [dict(high=c + wick, low=c - wick, close=c, volume=vol) for c in closes]


def test_causal_dz4_uses_past_sigma():
    rng = np.random.default_rng(0)
    closes = 100 + np.cumsum(rng.normal(0, 0.3, 40))
    d = causal_dz4(bars_from(closes))
    assert d is not None and math.isfinite(d)
    assert causal_dz4(bars_from(closes[:10])) is None


def test_reclaim_requires_pierce_then_close_inside():
    b = bars_from([100.0] * 10)
    assert not reclaim_close_strict(b, 1, vwap=100.0, sigma=1.0)  # never pierced
    b[-3]["low"] = 97.5
    assert reclaim_close_strict(b, 1, vwap=100.0, sigma=1.0)
    b[-1]["close"] = 97.9
    assert not reclaim_close_strict(b, 1, vwap=100.0, sigma=1.0)


def test_drift_tstat_false_pass_rate_on_random_walk():
    rng = np.random.default_rng(42)
    hits = sum(abs(drift_tstat_nw(100 * np.exp(np.cumsum(rng.normal(0, 0.01, 49))), 48)) > 2.0
               for _ in range(400))
    assert hits / 400 < 0.12


def test_drift_tstat_detects_trend():
    closes = 100 * np.exp(np.cumsum(np.full(49, 0.002) + np.random.default_rng(1).normal(0, 0.003, 49)))
    assert drift_tstat_nw(closes, 48) > 2.0


def test_override_disabled_by_default():
    assert derive_m1_range_override({"absorption_verified": True, "htf_adverse_trend": False},
                                   {"t": 0.0, "er": 0.1}, "LONG", orderflow_present=True) is None


# ---- Pre-send discrete ---------------------------------------------------------
def order(**kw):
    a = dict(price=7770.0, sl=7761.5, tp=7791.25, volume=0.13, side=1,
             bid=7775.0, ask=7775.3, tick_size=0.25, point=0.01,
             stops_level_pts=50, freeze_level_pts=0,
             volume_min=0.01, volume_step=0.01, volume_max=50.0,
             risk_budget_usd=14.5, usd_per_price_unit_per_lot=10.0)
    a.update(kw)
    return discrete_order_checks(**a)


def test_discrete_clean():
    assert order() == []


def test_discrete_violations():
    assert "price_off_tick" in order(price=7770.1)
    assert "volume_not_on_step_round_down_required" in order(volume=0.135)
    assert any(r.startswith("realised_risk") for r in order(volume=0.2))
    assert "limit_inside_stops_or_freeze_level" in order(freeze_level_pts=600)
