"""Regression tests for the two defects found in the Arena council review.

1. `p_win_lower_bound` was a hardcoded literal (0.48) published alongside
   `p_win_lower_bound_calibrated: True`. `_net_ev` consumes that scalar and has
   no way to detect that no sample supports it, so the expectancy gate could be
   satisfied by an unearned edge.

2. `classify_regime` is a pure function of price series, so a market that had
   already closed for the weekend could still be returned as MEAN_REVERT from
   its stale Friday bars and read as tradeable.
"""
from __future__ import annotations

import importlib.util
import pathlib
import sys

import pytest

ROOT = pathlib.Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from Terminal.decision_gates_v3 import classify_regime  # noqa: E402

_gen_path = ROOT / "Terminal" / "Data_Factory" / "generate_telemetry_snapshot.py"
_spec = importlib.util.spec_from_file_location("gen_telemetry", _gen_path)
gen = importlib.util.module_from_spec(_spec)
sys.modules["gen_telemetry"] = gen
_spec.loader.exec_module(gen)


# ------------------------------------------------ 1. win-rate lower bound
def test_p_win_lower_bound_matches_exact_clopper_pearson():
    """The bound must be the exact CP limit, not an approximation or a guess.

    Cross-checked against scipy where available; the pinned literals keep the
    test meaningful on machines that do not ship scipy.
    """
    pinned = {(11, 17): 0.41970535, (10, 17): 0.36400877, (9, 17): 0.31082957,
              (5, 10): 0.22244110, (1, 17): 0.00301271, (16, 17): 0.74987555,
              (100, 200): 0.43964103, (30, 50): 0.47388025, (7, 20): 0.17731092}
    for (wins, n), expected in pinned.items():
        assert gen.p_win_lower_bound(wins, n) == pytest.approx(expected, abs=1e-7)

    try:
        from scipy import stats
    except ImportError:
        pytest.skip("scipy not installed; pinned literals already verified")
    for (wins, n) in pinned:
        expected = stats.beta.ppf(0.05, wins, n - wins + 1)
        assert gen.p_win_lower_bound(wins, n) == pytest.approx(expected, abs=1e-9)


@pytest.mark.parametrize("wins,n,expected", [
    (0, 17, 0.0),     # no wins -> no evidence of edge
    (0, 0, 0.0),      # empty record must not divide by zero
    (17, 17, None),   # perfect record must NOT certify p = 1.0
])
def test_p_win_lower_bound_edge_cases(wins, n, expected):
    got = gen.p_win_lower_bound(wins, n)
    if expected is None:
        assert got < 1.0
    else:
        assert got == expected


def test_p_win_lower_bound_is_conservative_for_the_published_record():
    """The audited 11/17 record cannot support the 0.48 that used to be hardcoded."""
    assert gen.p_win_lower_bound(11, 17) < 0.48
    assert gen.p_win_lower_bound(11, 17) == pytest.approx(0.4197, abs=1e-3)


def test_small_sample_is_not_reported_as_calibrated():
    cal = gen.p_win_calibration(wins=11, n=17)
    assert cal["p_win_lower_bound_calibrated"] is False
    assert cal["p_win_calibration_sample_n"] == 17
    assert "CLOPPER_PEARSON" in cal["p_win_calibration_method"]


def test_large_sample_is_reported_as_calibrated():
    cal = gen.p_win_calibration(wins=600, n=1000)
    assert cal["p_win_calibration_sample_n"] >= gen.P_WIN_MIN_SAMPLE
    assert cal["p_win_lower_bound_calibrated"] is True


def test_no_hardcoded_win_rate_literal_remains_in_generator():
    """Guard against the constant being reintroduced."""
    src = _gen_path.read_text()
    assert '"p_win_lower_bound": 0.48' not in src
    assert '"p_win_lower_bound_calibrated": True' not in src


# ------------------------------------------------ 2. regime staleness guard
def _synthetic_series(n, start=100.0, drift=0.0):
    return [start + drift * i for i in range(n)]


def test_classify_regime_backward_compatible_without_epochs():
    """Omitting the new kwargs must reproduce the original behaviour exactly."""
    c15 = _synthetic_series(100)
    c1 = _synthetic_series(96)
    c4 = _synthetic_series(96)
    a = classify_regime(c15, c1, c4)[0]
    b = classify_regime(c15, c1, c4, last_close_epoch=None, as_of_epoch=None)[0]
    assert a == b


def test_fresh_bars_are_not_suppressed_by_the_guard():
    c15, c1, c4 = _synthetic_series(100), _synthetic_series(96), _synthetic_series(96)
    now = 1_800_000_000.0
    regime, stats = classify_regime(c15, c1, c4, last_close_epoch=now - 300, as_of_epoch=now)
    assert stats["stale"] is False
    assert stats["bar_age_s"] == pytest.approx(300.0)


def test_stale_bars_force_undefined():
    """A 9.7-hour-old bar set must never yield a tradeable regime."""
    c15, c1, c4 = _synthetic_series(100), _synthetic_series(96), _synthetic_series(96)
    now = 1_800_000_000.0
    regime, stats = classify_regime(c15, c1, c4, last_close_epoch=now - 34_816, as_of_epoch=now)
    assert regime == "UNDEFINED"
    assert stats["stale"] is True


def test_staleness_threshold_boundary():
    """Exactly at the threshold is fresh; one second past it is stale."""
    c15, c1, c4 = _synthetic_series(100), _synthetic_series(96), _synthetic_series(96)
    now = 1_800_000_000.0
    _, st_in = classify_regime(c15, c1, c4, last_close_epoch=now - 1800, as_of_epoch=now)
    outside, st_out = classify_regime(c15, c1, c4, last_close_epoch=now - 1801, as_of_epoch=now)
    assert st_in["stale"] is False
    assert st_out["stale"] is True
    assert outside == "UNDEFINED"


def test_guard_overrides_a_regime_that_would_otherwise_be_tradeable():
    """The guard must fire even when the series would classify as MEAN_REVERT."""
    # Flat 1H (low ER, low |t|) + anti-persistent 15m drives MEAN_REVERT.
    flat1h = [100.0 + (0.01 if i % 2 else -0.01) for i in range(96)]
    flat4h = [100.0 + (0.01 if i % 2 else -0.01) for i in range(96)]
    antiper15 = [100.0 + (1.0 if i % 2 else -1.0) for i in range(100)]
    now = 1_800_000_000.0
    fresh, _ = classify_regime(antiper15, flat1h, flat4h,
                               last_close_epoch=now - 300, as_of_epoch=now)
    stale, st = classify_regime(antiper15, flat1h, flat4h,
                                last_close_epoch=now - 34_816, as_of_epoch=now)
    assert fresh == "MEAN_REVERT"
    assert stale == "UNDEFINED" and st["stale"] is True


def test_evaluate_candidate_dg_v3_staleness_guard_wired():
    """Verify that evaluate_candidate_dg_v3 suppresses stale bars to UNDEFINED in live admission."""
    from Terminal.dg_context import evaluate_candidate_dg_v3
    now = 1_800_000_000.0
    stale_bar_time = now - 34_816 - 900
    bars_15m = [
        {"time": stale_bar_time - (100 - i) * 900, "open": 100.0, "high": 101.0,
         "low": 99.0, "close": 100.0 + (1.0 if i % 2 else -1.0), "volume": 1000}
        for i in range(100)
    ]
    bars_1h = [
        {"time": stale_bar_time - (60 - i) * 3600, "open": 100.0, "high": 100.1,
         "low": 99.9, "close": 100.0 + (0.01 if i % 2 else -0.01), "volume": 4000}
        for i in range(60)
    ]
    bars_4h = [
        {"time": stale_bar_time - (60 - i) * 14400, "open": 100.0, "high": 100.1,
         "low": 99.9, "close": 100.0 + (0.01 if i % 2 else -0.01), "volume": 16000}
        for i in range(60)
    ]
    quote = {"bid": 100.0, "ask": 100.02, "point": 0.01, "tick_size": 0.01, "time_msc": now * 1000}
    features = {"direction": "LONG", "atr": 2.0}
    sizing = {"risk_usd": 12.0, "friction_usd": 0.40}

    res_stale = evaluate_candidate_dg_v3(
        features=features, payload={}, pivots=None, quote=quote,
        bars_15m=bars_15m, bars_1h=bars_1h, bars_4h=bars_4h,
        entry=100.0, sl=96.0, tp=108.0, sizing=sizing, symbol="SP500.p"
    )
    assert res_stale["regime"] == "UNDEFINED"
    assert res_stale["stats"]["stale"] is True
    assert res_stale["stats"]["bar_age_s"] > 1800.0

    fresh_now = 1_800_000_000.0
    fresh_bar_time = fresh_now - 300 - 900
    bars_15m_fresh = [
        {"time": fresh_bar_time - (100 - i) * 900, "open": 100.0, "high": 101.0,
         "low": 99.0, "close": 100.0 + (1.0 if i % 2 else -1.0), "volume": 1000}
        for i in range(100)
    ]
    bars_1h_fresh = [
        {"time": fresh_bar_time - (60 - i) * 3600, "open": 100.0, "high": 100.1,
         "low": 99.9, "close": 100.0 + (0.01 if i % 2 else -0.01), "volume": 4000}
        for i in range(60)
    ]
    bars_4h_fresh = [
        {"time": fresh_bar_time - (60 - i) * 14400, "open": 100.0, "high": 100.1,
         "low": 99.9, "close": 100.0 + (0.01 if i % 2 else -0.01), "volume": 16000}
        for i in range(60)
    ]
    quote_fresh = {"bid": 100.0, "ask": 100.02, "point": 0.01, "tick_size": 0.01, "time_msc": fresh_now * 1000}
    res_fresh = evaluate_candidate_dg_v3(
        features=features, payload={}, pivots=None, quote=quote_fresh,
        bars_15m=bars_15m_fresh, bars_1h=bars_1h_fresh, bars_4h=bars_4h_fresh,
        entry=100.0, sl=96.0, tp=108.0, sizing=sizing, symbol="BTCUSD.pi"
    )
    assert res_fresh["stats"]["stale"] is False
    assert res_fresh["regime"] == "MEAN_REVERT"

