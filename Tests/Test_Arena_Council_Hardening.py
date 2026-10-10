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
import time as _time_mod

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
        entry=100.0, sl=96.0, tp=108.0, sizing=sizing, symbol="SP500.p",
        as_of_epoch=now,
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
        entry=100.0, sl=96.0, tp=108.0, sizing=sizing, symbol="BTCUSD.pi",
        as_of_epoch=fresh_now,
    )
    assert res_fresh["stats"]["stale"] is False
    assert res_fresh["regime"] == "MEAN_REVERT"


def test_staleness_survives_a_frozen_quote():
    """Regression: the quote freezes WITH the market, so it cannot date the bars.

    This is the real weekend-CFD failure mode. The earlier wiring derived the
    staleness clock from quote["time_msc"], and the test for it paired OLD bars
    with a FRESH quote -- a combination that cannot occur. In production both
    freeze at the Friday close, so (quote_time - last_bar_close) stays ~900s,
    the guard never fires, and a 10-hour-old history classifies as tradeable.
    Reproduced from live SP500 telemetry: quote age 36,812s, bar age 37,712s,
    yet quote-derived bar_age = 899s.
    """
    from Terminal.dg_context import evaluate_candidate_dg_v3

    # Mirror the live SP500 geometry exactly: bars and quote frozen together.
    last_bar_open = 1_791_577_800.0            # 2026-10-09 20:30 UTC
    last_close = last_bar_open + 900.0         # 20:45 UTC
    frozen_quote_epoch = last_close + 899.381  # quote froze just after the last bar
    wall_clock_now = last_close + 37_711.9     # 10.5 hours later

    def mk_bars(count, period, last_open, close_fn):
        return [{"time": last_open - (count - 1 - i) * period, "open": 100.0,
                 "high": 101.0, "low": 99.0, "close": close_fn(i), "volume": 1000}
                for i in range(count)]

    alt15 = lambda i: 100.0 + (1.0 if i % 2 else -1.0)
    flat = lambda i: 100.0 + (0.01 if i % 2 else -0.01)
    # Anchor HTF series so their newest bar CLOSES before the frozen quote;
    # otherwise the pre-existing causality check rejects the history first.
    bars_15m = mk_bars(100, 900, last_bar_open, alt15)
    bars_1h = mk_bars(60, 3600, last_bar_open - 2 * 3600, flat)
    bars_4h = mk_bars(60, 14400, last_bar_open - 2 * 14400, flat)
    frozen_quote = {"bid": 100.0, "ask": 100.02, "point": 0.01, "tick_size": 0.01,
                    "time_msc": frozen_quote_epoch * 1000}
    features = {"direction": "LONG", "atr": 2.0}
    sizing = {"risk_usd": 12.0, "friction_usd": 0.40}
    kw = dict(features=features, payload={}, pivots=None, quote=frozen_quote,
              bars_15m=bars_15m, bars_1h=bars_1h, bars_4h=bars_4h,
              entry=100.0, sl=96.0, tp=108.0, sizing=sizing, symbol="SP500.p")

    # A quote-derived clock would report ~899s and let this through.
    assert (frozen_quote_epoch - last_close) < 1800.0

    res = evaluate_candidate_dg_v3(as_of_epoch=wall_clock_now, **kw)
    assert res["regime"] == "UNDEFINED"
    assert res["stats"]["stale"] is True
    assert res["stats"]["bar_age_s"] > 1800.0


def test_default_staleness_clock_is_wall_time_not_quote_time():
    """Omitting as_of_epoch must use time.time(), never quote["time_msc"]."""
    from Terminal.dg_context import evaluate_candidate_dg_v3

    now = _time_mod.time()
    last_bar_open = now - 5 * 3600 - 900       # 5 hours stale
    alt15 = lambda i: 100.0 + (1.0 if i % 2 else -1.0)
    flat = lambda i: 100.0 + (0.01 if i % 2 else -0.01)
    bars_15m = [{"time": last_bar_open - (99 - i) * 900, "open": 100.0, "high": 101.0,
                 "low": 99.0, "close": alt15(i), "volume": 1000} for i in range(100)]
    # HTF newest bars must close before the frozen quote or causality rejects them.
    bars_1h = [{"time": last_bar_open - 2 * 3600 - (59 - i) * 3600, "open": 100.0,
                "high": 100.1, "low": 99.9, "close": flat(i), "volume": 4000}
               for i in range(60)]
    bars_4h = [{"time": last_bar_open - 2 * 14400 - (59 - i) * 14400, "open": 100.0,
                "high": 100.1, "low": 99.9, "close": flat(i), "volume": 16000}
               for i in range(60)]
    # Quote frozen alongside the bars -- the trap this test exists to catch.
    quote = {"bid": 100.0, "ask": 100.02, "point": 0.01, "tick_size": 0.01,
             "time_msc": (last_bar_open + 950.0) * 1000}

    res = evaluate_candidate_dg_v3(
        features={"direction": "LONG", "atr": 2.0}, payload={}, pivots=None, quote=quote,
        bars_15m=bars_15m, bars_1h=bars_1h, bars_4h=bars_4h,
        entry=100.0, sl=96.0, tp=108.0, sizing={"risk_usd": 12.0, "friction_usd": 0.40},
        symbol="SP500.p",
    )
    assert res["regime"] == "UNDEFINED"
    assert res["stats"]["stale"] is True
    assert res["stats"]["bar_age_s"] > 1800.0



def test_arena_bridge_does_not_reassert_the_spread_exemption_fallacy():
    """The council prompt must not claim maker limits pay zero spread.

    This fallacy was already eliminated once (session history: "maker limits do
    not escape spread or commission. Imposed hard 20.00 bps maximum spread
    gate"), and the protocol states it directly: "Maker limit orders do NOT
    eliminate the broker spread." A Buy Limit fills on Ask and exits on Bid, so
    the spread is paid round trip regardless of maker or taker entry. Leaving
    the claim in the generated prompt makes the desk re-litigate it every cycle
    and invites quarantined assets back in on a false premise.
    """
    src = (ROOT / "Terminal" / "arena_bridge.py").read_text()
    assert "zero spread" not in src
    assert "maker limits pay zero" not in src.lower()


def test_protocol_spread_gate_and_maker_language_are_consistent():
    """Protocol must keep both the maker-limit caveat and the 20 bps ceiling."""
    proto = (ROOT / "docs" / "specs" /
             "ANTIGRAVITY_ARENA_THINKING_CHAIN_COUNCIL_PROTOCOL.md").read_text()
    assert "Maker limit orders do NOT eliminate the broker spread." in proto
    assert "20.00 bps" in proto


def test_whale_wall_age_is_not_clamped_to_the_persistence_threshold():
    """The rendered wall age must not be floored at 180.

    arena_bridge.py used `age={max(w_age, 180)}s`. Because no persistence series
    is published, w_age resolved to ~0s and every wall in the council briefing
    rendered 'age=180s' -- which reads as persistence verified at exactly the
    >=180s mandate threshold. That fabricates compliance with mandate 4 for
    every wall in the universe and can induce a punch on unverified data.
    """
    src = (ROOT / "Terminal" / "arena_bridge.py").read_text()
    assert "max(w_age, 180)" not in src
    assert "no persistence series" in src


# ------------------------------------------------ 4. mirrored whale walls
def _load_arena_bridge():
    """Import arena_bridge with any absent transport dep stubbed out.

    The module imports websockets at module level purely for the live feed
    client; the pure helpers under test do not touch it. Stubbing keeps the
    regression test runnable in environments without the websocket client
    while still executing the real function body.
    """
    import types
    for name in ("websockets",):
        if name not in sys.modules:
            try:
                __import__(name)
            except ImportError:
                sys.modules[name] = types.ModuleType(name)
    spec = importlib.util.spec_from_file_location(
        "arena_bridge_under_test", ROOT / "Terminal" / "arena_bridge.py")
    mod = importlib.util.module_from_spec(spec)
    sys.modules["arena_bridge_under_test"] = mod
    spec.loader.exec_module(mod)
    return mod


def _bracket_pair(size=252.4353):
    """The real BTC L3 shape: one wallet, equal size, both sides."""
    return [
        {"address": "0xf5a523b1", "side": "SELL", "price": 83862.0,
         "size": size, "notional_usd": 21169733.32},
        {"address": "0xf5a523b1", "side": "BUY", "price": 81641.0,
         "size": size, "notional_usd": 20609074.41},
    ]


def test_size_matched_opposite_leg_is_detected_as_a_bracket():
    """A wall mirrored by an equal opposite leg must not read as directional.

    Live BTC L3 shows wallet 0xf5a523b1 quoting SELL 252.4353 @ 83862 and
    BUY 252.4353 @ 81641 -- identical size, both sides, straddling the market.
    The council briefing rendered only the ask leg as "Whale Wall: SELL at
    83862 (21,169,733.32 USD)", which the desk then reasoned about as a trapped
    short-liquidation magnet. A sell wall size-matched by an equal buy wall
    from the same wallet carries no net directional information.
    """
    ab = _load_arena_bridge()
    walls = _bracket_pair()
    mirror = ab.detect_mirrored_wall_leg(walls[0], walls)
    assert mirror is not None
    assert mirror["side"] == "BUY"
    assert mirror["price"] == 81641.0


def test_genuinely_one_sided_wall_is_not_flagged_as_a_bracket():
    """The detector must not cry wolf on real one-sided inventory."""
    ab = _load_arena_bridge()
    walls = [
        {"address": "0xaaaa", "side": "SELL", "price": 84000.0,
         "size": 200.0, "notional_usd": 16800000.0},
        {"address": "0xaaaa", "side": "BUY", "price": 82000.0,
         "size": 12.0, "notional_usd": 984000.0},
    ]
    assert ab.detect_mirrored_wall_leg(walls[0], walls) is None


def test_mirror_requires_the_same_wallet():
    """An equal opposite size from a DIFFERENT wallet is not a bracket."""
    ab = _load_arena_bridge()
    walls = [
        {"address": "0xaaaa", "side": "SELL", "price": 84000.0,
         "size": 200.0, "notional_usd": 16800000.0},
        {"address": "0xbbbb", "side": "BUY", "price": 82000.0,
         "size": 200.0, "notional_usd": 16400000.0},
    ]
    assert ab.detect_mirrored_wall_leg(walls[0], walls) is None


def test_mirror_detection_is_malformed_input_safe():
    """Telemetry gaps must degrade to 'no mirror', never raise."""
    ab = _load_arena_bridge()
    f = ab.detect_mirrored_wall_leg
    assert f(None, []) is None
    assert f({"side": "SELL", "size": 1.0}, []) is None
    assert f({"side": "HOLD", "size": 1.0}, []) is None
    assert f({"side": "SELL", "size": 0}, []) is None
    assert f({"side": "SELL", "size": "x"}, []) is None
    assert f({"side": "SELL", "size": 1.0}, [None, {"side": "BUY"}]) is None


def test_briefing_labels_mirrored_walls_as_brackets():
    """The render must carry the bracket verdict, not just the raw wall."""
    src = (ROOT / "Terminal" / "arena_bridge.py").read_text()
    assert "detect_mirrored_wall_leg(w, whales)" in src
    assert "NOT net directional inventory" in src


# ------------------------------------- 5. enforced regime vs cosmetic label
def _ramp(n, start=100.0, step=1.0):
    import math
    return [start + step * i + 0.05 * math.sin(i) for i in range(n)]


def _ramp_asset(as_of_epoch, age_s=0.0):
    """A frozen trending market: TREND_UP on the math, STALE on the clock."""
    close_ts = as_of_epoch - age_s
    return {
        "causal_indicators": {"trend_regime": "BULLISH"},
        "bars_15m_ohlcv": [{"close": v, "close_ts": close_ts} for v in _ramp(200)],
        "htf_1h_ohlcv": [{"close": v, "close_ts": close_ts} for v in _ramp(120)],
        "htf_4h_ohlcv": [{"close": v, "close_ts": close_ts} for v in _ramp(120)],
    }


def test_enforced_regime_exposes_the_cosmetic_label_divergence():
    """The 200-EMA label must not be presented as the regime the gates enforce.

    causal_indicators.trend_regime is a 200-EMA heuristic. model1_checklist
    requires regime == MEAN_REVERT and model2_checklist requires regime in
    {TREND_UP, TREND_DOWN}, both read from classify_regime(). Live BTC has
    repeatedly carried trend_regime=BULLISH while the enforced gate returned
    UNDEFINED, and the desk argued the long off the label. The briefing must
    show the binding verdict alongside it.
    """
    ab = _load_arena_bridge()
    cls = ab._load_gate_classifier()
    assert cls is not None
    asset = _ramp_asset(1_800_000_000.0, age_s=0.0)
    out = ab.enforced_regime(asset, cls, 1_800_000_000.0)
    # The math here is a clean uptrend, so the gate must agree with the label.
    assert "enforced_gate=TREND_UP(live)" == out
    # Now flip the path to a perfect alternation while leaving the label
    # untouched: the 200-EMA still says BULLISH, but the enforced gate lands on
    # the opposite engine. This is the divergence the briefing must expose.
    flat = {
        "causal_indicators": {"trend_regime": "BULLISH"},
        "bars_15m_ohlcv": [{"close": 100.0 + (1.0 if i % 2 else -1.0), "close_ts": 1_800_000_000.0}
                           for i in range(200)],
        "htf_1h_ohlcv": [{"close": 100.0 + (1.0 if i % 2 else -1.0), "close_ts": 1_800_000_000.0}
                         for i in range(120)],
        "htf_4h_ohlcv": [{"close": 100.0 + (1.0 if i % 2 else -1.0), "close_ts": 1_800_000_000.0}
                         for i in range(120)],
    }
    assert flat["causal_indicators"]["trend_regime"] == "BULLISH"
    assert ab.enforced_regime(flat, cls, 1_800_000_000.0) == "enforced_gate=MEAN_REVERT(live)"


def test_enforced_regime_threads_the_staleness_guard():
    """A frozen trending market must not render as a tradeable regime.

    Without as_of_epoch this exact series classifies TREND_UP. A weekend CFD
    publishes its Friday bars, so dropping the clock would advertise a live
    trend for a market that is shut -- the defect fixed in 1207d7d9.
    """
    ab = _load_arena_bridge()
    cls = ab._load_gate_classifier()
    now = 1_800_000_000.0
    asset = _ramp_asset(now, age_s=45000.0)
    assert ab.enforced_regime(asset, cls, None) == "enforced_gate=TREND_UP(live)"
    guarded = ab.enforced_regime(asset, cls, now)
    assert guarded == "enforced_gate=UNDEFINED(STALE_BARS_age=45000s)"


def test_enforced_regime_degrades_without_raising():
    """Telemetry gaps must render a string verdict, never crash the briefing."""
    ab = _load_arena_bridge()
    cls = ab._load_gate_classifier()
    now = 1_800_000_000.0
    assert ab.enforced_regime(_ramp_asset(now), None, now) == \
        "enforced_gate=UNAVAILABLE(module_load_failed)"
    assert ab.enforced_regime("not-a-dict", cls, now) == \
        "enforced_gate=UNAVAILABLE(no_asset_data)"
    assert ab.enforced_regime({}, cls, now) == "enforced_gate=UNDEFINED(live)"
    junk = {"bars_15m_ohlcv": [{"close": "x"}, None, {"close_ts": "y"}],
            "htf_1h_ohlcv": None, "htf_4h_ohlcv": []}
    assert ab.enforced_regime(junk, cls, now) == "enforced_gate=UNDEFINED(live)"


def test_briefing_marks_the_200ema_label_as_cosmetic():
    """The render must name the binding gate, not imply the label is it."""
    src = (ROOT / "Terminal" / "arena_bridge.py").read_text()
    assert "cosmetic, NOT the gate" in src
    assert "BINDING for both engines" in src
    assert "enforced_regime(t_asset, gate_classifier, snapshot_as_of)" in src
    # the old bare "Regime = <200EMA label>" framing must be gone
    assert "| Regime = {inds.get('trend_regime'" not in src
