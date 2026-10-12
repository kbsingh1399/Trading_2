"""Tests for `regime_attribution` and the four reviewed-but-inert desk upgrades.

Context for why these exist. On 2026-10-12 the desk diagnosed a "structural
gating paralysis where 24/24 assets are constantly vetoed by classify_regime()
-> UNDEFINED" and proposed four architectural upgrades to cure it. The Council
tested the diagnosis before wiring anything in, and it did not survive:

  * The 1H efficiency-ratio floor was the FIRST binding leg on 21 of 24 assets,
    but every one of those 21 independently failed drift_t_1h >= 2.0. Relaxing
    the ER floor to zero therefore admitted ZERO assets.
  * Granting every asset a certified regime and re-running the full candidate
    screen produced 0 of 24 tradeable candidates. What actually binds is B6
    (no target inside 4.0 ATR), B2 (retrace outside [0.236, 0.618]) and G-6
    (gamma > 0.15) -- not the regime gate.

So the upgrades ship as reviewed, tested formulations that are NOT reachable
from the live routing path. These tests pin two things:

  1. `regime_attribution` agrees with `classify_regime` -- a diagnostic that
     disagrees with the thing it explains is worse than no diagnostic.
  2. Each upgrade is INERT while its flag is off, and behaves as specified when
     the flag is on. Inertness is the property that makes this safe to merge
     onto a branch feeding a live account.
"""
from __future__ import annotations

import pathlib
import sys

import numpy as np
import pytest

ROOT = pathlib.Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from Terminal.decision_gates_v3 import (  # noqa: E402
    ALLOW_EMA200_STRUCTURAL_FALLBACK,
    ALLOW_M1_PRICE_ONLY_VARIANT,
    ALLOW_REGIME_HYSTERESIS,
    EMA200_DRIFT_T_HI,
    EMA200_DRIFT_T_LO,
    M1_VOLUME_EXPANSION_MIN,
    M1_WICK_REJECTION_MIN,
    REGIME_HYSTERESIS_BARS,
    RegimeParams,
    apply_regime_hysteresis,
    classify_regime,
    ema200_structural_confirms,
    m1_price_only_variant_ok,
    regime_attribution,
)


# ---------------------------------------------------------------- flags are off
def test_all_upgrade_flags_default_off():
    """Nothing in this module may change live behaviour by default."""
    assert ALLOW_REGIME_HYSTERESIS is False
    assert ALLOW_EMA200_STRUCTURAL_FALLBACK is False
    assert ALLOW_M1_PRICE_ONLY_VARIANT is False


def test_m1_range_override_still_ratified_off():
    """Upgrade 2 already existed; the Council must not have flipped it."""
    from Terminal.dg_hardening import ALLOW_M1_RANGE_OVERRIDE

    assert ALLOW_M1_RANGE_OVERRIDE is False


# ------------------------------------------------------- attribution agreement
def _series(rng, n, drift, vol, start=100.0):
    return list(start + np.cumsum(rng.normal(drift, vol, n)))


@pytest.mark.parametrize("drift,vol,sign", [
    (0.9, 1.0, 1),      # strong up trend
    (-0.9, 1.0, -1),    # strong down trend
    (0.0, 1.0, None),   # pure noise
    (0.2, 2.0, 1),      # weak drift, high vol
    (0.0, 0.1, None),   # near-flat
])
def test_attribution_agrees_with_classify_regime(drift, vol, sign):
    """A diagnostic that disagrees with the router it explains is worthless."""
    rng = np.random.default_rng(11)
    c15 = _series(rng, 200, drift, vol)
    c1h = _series(rng, 80, drift * 4, vol)
    c4h = _series(rng, 60, drift * 8, vol)
    p = RegimeParams()

    regime, _ = classify_regime(c15, c1h, c4h, p, structural_sign=sign)
    attr = regime_attribution(c15, c1h, c4h, p, structural_sign=sign)

    if regime == "UNDEFINED":
        assert attr["binding_leg"] is not None, "UNDEFINED must carry a named leg"
    else:
        assert attr["binding_leg"] is None, f"{regime} must not name a blocking leg"


def test_attribution_names_er_floor_when_er_is_the_first_failure():
    """The leg the 2026-10-12 diagnosis blamed: must be reported honestly."""
    rng = np.random.default_rng(3)
    # Low ER (choppy) but a clear positive drift, so ER binds before drift does.
    closes = list(100 + np.cumsum(rng.normal(0.0, 1.0, 200)) + np.linspace(0, 30, 200))
    attr = regime_attribution(closes, closes[::4], closes[::8], RegimeParams(),
                              structural_sign=1)
    assert attr["er_1h_min"] == pytest.approx(0.20)
    assert attr["drift_t_1h_min"] == pytest.approx(2.0)


def test_attribution_flags_structural_sign_undetermined():
    """`structural_sign=None` is a distinct failure and must be named as such.

    The base series must be long enough that every timeframe clears its own
    minimum: n_4h + 1 = 31 bars of 4H, so the 1-in-8 slice needs >= 248 points.
    """
    rng = np.random.default_rng(5)
    noise = _series(rng, 400, 0.0, 1.0)
    attr = regime_attribution(noise, noise[::4], noise[::8], RegimeParams(),
                              structural_sign=None)
    assert attr["binding_leg"] in (
        "er_1h_below_floor", "drift_t_1h_below_min", "structural_sign_undetermined")
    assert attr["structural_sign"] is None


def test_attribution_reports_relaxation_counterfactuals():
    """`would_admit_if_relaxed` is the field that stops a wasted threshold change."""
    rng = np.random.default_rng(13)
    noise = _series(rng, 400, 0.0, 1.0)
    attr = regime_attribution(noise, noise[::4], noise[::8], RegimeParams(),
                              structural_sign=None)
    assert isinstance(attr["would_admit_if_relaxed"], list)
    for leg in attr["would_admit_if_relaxed"]:
        assert leg in ("er_1h_floor", "drift_t_1h_floor_to_1p2", "vr_z_mr")


def test_attribution_fails_closed_on_short_history():
    rng = np.random.default_rng(17)
    short = _series(rng, 10, 0.0, 1.0)
    attr = regime_attribution(short, short, short, RegimeParams(), structural_sign=1)
    assert attr["binding_leg"] == "data_invalid:regime_history_or_statistics"
    assert attr["would_admit_if_relaxed"] == []


# ------------------------------------------------------- Upgrade 1: hysteresis
def test_hysteresis_inert_while_flag_off():
    assert apply_regime_hysteresis("UNDEFINED", "TREND_UP", swing_intact=True,
                                  bars_since_certified=1) == "UNDEFINED"


def test_hysteresis_retains_trend_within_window(monkeypatch):
    import Terminal.decision_gates_v3 as G
    monkeypatch.setattr(G, "ALLOW_REGIME_HYSTERESIS", True)
    assert apply_regime_hysteresis("UNDEFINED", "TREND_UP", swing_intact=True,
                                  bars_since_certified=REGIME_HYSTERESIS_BARS) == "TREND_UP"
    assert apply_regime_hysteresis("UNDEFINED", "TREND_DOWN", swing_intact=True,
                                  bars_since_certified=1) == "TREND_DOWN"


@pytest.mark.parametrize("bars", [REGIME_HYSTERESIS_BARS + 1, 99])
def test_hysteresis_expires_outside_memory_window(monkeypatch, bars):
    import Terminal.decision_gates_v3 as G
    monkeypatch.setattr(G, "ALLOW_REGIME_HYSTERESIS", True)
    assert apply_regime_hysteresis("UNDEFINED", "TREND_UP", swing_intact=True,
                                  bars_since_certified=bars) == "UNDEFINED"


@pytest.mark.parametrize("swing", [False, None])
def test_hysteresis_refuses_when_swing_points_broken(monkeypatch, swing):
    """The whole safety of hysteresis rests on unbroken structure."""
    import Terminal.decision_gates_v3 as G
    monkeypatch.setattr(G, "ALLOW_REGIME_HYSTERESIS", True)
    assert apply_regime_hysteresis("UNDEFINED", "TREND_UP", swing_intact=swing,
                                  bars_since_certified=1) == "UNDEFINED"


@pytest.mark.parametrize("current", ["TREND_DOWN", "MEAN_REVERT"])
def test_hysteresis_never_overrides_a_live_label(monkeypatch, current):
    """A real, freshly-computed regime always beats a remembered one."""
    import Terminal.decision_gates_v3 as G
    monkeypatch.setattr(G, "ALLOW_REGIME_HYSTERESIS", True)
    assert apply_regime_hysteresis(current, "TREND_UP", swing_intact=True,
                                  bars_since_certified=1) == current


@pytest.mark.parametrize("prior", [None, "UNDEFINED", "MEAN_REVERT", "RANGE"])
def test_hysteresis_only_remembers_trends(monkeypatch, prior):
    import Terminal.decision_gates_v3 as G
    monkeypatch.setattr(G, "ALLOW_REGIME_HYSTERESIS", True)
    assert apply_regime_hysteresis("UNDEFINED", prior, swing_intact=True,
                                  bars_since_certified=1) == "UNDEFINED"


def test_hysteresis_requires_a_bar_count(monkeypatch):
    import Terminal.decision_gates_v3 as G
    monkeypatch.setattr(G, "ALLOW_REGIME_HYSTERESIS", True)
    assert apply_regime_hysteresis("UNDEFINED", "TREND_UP", swing_intact=True,
                                  bars_since_certified=None) == "UNDEFINED"


# --------------------------------------------------- Upgrade 4: EMA200 fallback
def test_ema200_inert_while_flag_off():
    assert ema200_structural_confirms(105, 100, 0.5, 1.5, 1) is False


def test_ema200_admits_aligned_long(monkeypatch):
    import Terminal.decision_gates_v3 as G
    monkeypatch.setattr(G, "ALLOW_EMA200_STRUCTURAL_FALLBACK", True)
    assert ema200_structural_confirms(105, 100, 0.5, 1.5, 1) is True


def test_ema200_admits_aligned_short(monkeypatch):
    import Terminal.decision_gates_v3 as G
    monkeypatch.setattr(G, "ALLOW_EMA200_STRUCTURAL_FALLBACK", True)
    assert ema200_structural_confirms(95, 100, -0.5, -1.5, -1) is True


@pytest.mark.parametrize("drift,expect", [
    (EMA200_DRIFT_T_LO, True), (EMA200_DRIFT_T_HI, True),   # inclusive band edges
    (EMA200_DRIFT_T_LO - 0.01, False), (EMA200_DRIFT_T_HI + 0.01, False),
    (0.0, False), (2.5, False), (-1.5, False),
])
def test_ema200_band_is_inclusive_and_bounded(monkeypatch, drift, expect):
    """The band must not leak: >= 2.0 already has STAT/STRUCT, < 1.2 is too weak."""
    import Terminal.decision_gates_v3 as G
    monkeypatch.setattr(G, "ALLOW_EMA200_STRUCTURAL_FALLBACK", True)
    assert ema200_structural_confirms(105, 100, 0.5, drift, 1) is expect


@pytest.mark.parametrize("mid,ema,slope", [
    (95, 100, 0.5),    # wrong side of EMA
    (105, 100, -0.5),  # right side, wrong slope
    (95, 100, -0.5),   # both wrong for a long
])
def test_ema200_requires_price_and_slope_alignment(monkeypatch, mid, ema, slope):
    import Terminal.decision_gates_v3 as G
    monkeypatch.setattr(G, "ALLOW_EMA200_STRUCTURAL_FALLBACK", True)
    assert ema200_structural_confirms(mid, ema, slope, 1.5, 1) is False


@pytest.mark.parametrize("args", [
    (None, 100, 0.5, 1.5, 1), (105, None, 0.5, 1.5, 1), (105, 100, None, 1.5, 1),
    (105, 100, 0.5, None, 1), (105, 100, 0.5, 1.5, 0), (105, 100, 0.5, 1.5, 7),
    (float("nan"), 100, 0.5, 1.5, 1),
])
def test_ema200_fails_closed_on_bad_input(monkeypatch, args):
    import Terminal.decision_gates_v3 as G
    monkeypatch.setattr(G, "ALLOW_EMA200_STRUCTURAL_FALLBACK", True)
    assert ema200_structural_confirms(*args) is False


# ---------------------------------------------- Upgrade 3: M1 price-only variant
def test_m1_price_only_inert_while_flag_off():
    ctx = {"allow_price_only_variant": True, "rejection_wick_ratio": 0.9,
           "volume_expansion_ratio": 3.0}
    assert m1_price_only_variant_ok(ctx) is False


def _m1_ctx(**over):
    ctx = {"allow_price_only_variant": True, "rejection_wick_ratio": 0.45,
           "volume_expansion_ratio": 2.0}
    ctx.update(over)
    return ctx


def test_m1_price_only_admits_with_both_substitutes(monkeypatch):
    import Terminal.decision_gates_v3 as G
    monkeypatch.setattr(G, "ALLOW_M1_PRICE_ONLY_VARIANT", True)
    assert m1_price_only_variant_ok(_m1_ctx()) is True


@pytest.mark.parametrize("wick", [M1_WICK_REJECTION_MIN, M1_WICK_REJECTION_MIN - 0.01, 0.0])
def test_m1_price_only_wick_threshold(monkeypatch, wick):
    import Terminal.decision_gates_v3 as G
    monkeypatch.setattr(G, "ALLOW_M1_PRICE_ONLY_VARIANT", True)
    expect = wick >= M1_WICK_REJECTION_MIN
    assert m1_price_only_variant_ok(_m1_ctx(rejection_wick_ratio=wick)) is expect


@pytest.mark.parametrize("vol", [M1_VOLUME_EXPANSION_MIN, M1_VOLUME_EXPANSION_MIN - 0.1])
def test_m1_price_only_volume_threshold(monkeypatch, vol):
    import Terminal.decision_gates_v3 as G
    monkeypatch.setattr(G, "ALLOW_M1_PRICE_ONLY_VARIANT", True)
    expect = vol >= M1_VOLUME_EXPANSION_MIN
    assert m1_price_only_variant_ok(_m1_ctx(volume_expansion_ratio=vol)) is expect


def test_m1_price_only_refuses_when_real_tape_present(monkeypatch):
    """If CVD exists, A2's absorption proof governs. No shortcut."""
    import Terminal.decision_gates_v3 as G
    monkeypatch.setattr(G, "ALLOW_M1_PRICE_ONLY_VARIANT", True)
    assert m1_price_only_variant_ok(_m1_ctx(orderflow={"cvd_push1": -1.0})) is False


def test_m1_price_only_requires_caller_opt_in(monkeypatch):
    import Terminal.decision_gates_v3 as G
    monkeypatch.setattr(G, "ALLOW_M1_PRICE_ONLY_VARIANT", True)
    ctx = _m1_ctx()
    del ctx["allow_price_only_variant"]
    assert m1_price_only_variant_ok(ctx) is False
    assert m1_price_only_variant_ok(_m1_ctx(allow_price_only_variant=False)) is False


@pytest.mark.parametrize("bad", [{"rejection_wick_ratio": None},
                                 {"volume_expansion_ratio": None},
                                 {"rejection_wick_ratio": float("nan")},
                                 {"volume_expansion_ratio": float("nan")}])
def test_m1_price_only_fails_closed_on_missing_evidence(monkeypatch, bad):
    import Terminal.decision_gates_v3 as G
    monkeypatch.setattr(G, "ALLOW_M1_PRICE_ONLY_VARIANT", True)
    assert m1_price_only_variant_ok(_m1_ctx(**bad)) is False


def test_m1_price_only_rejects_non_dict(monkeypatch):
    import Terminal.decision_gates_v3 as G
    monkeypatch.setattr(G, "ALLOW_M1_PRICE_ONLY_VARIANT", True)
    assert m1_price_only_variant_ok(None) is False
    assert m1_price_only_variant_ok("nope") is False
