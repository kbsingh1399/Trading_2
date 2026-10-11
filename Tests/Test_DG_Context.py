"""Tests for Terminal/dg_context.py context builder and evaluator."""
import pytest
from Terminal.dg_context import build_dg_context, evaluate_candidate_dg_v3


def test_build_dg_context_basic():
    now = (1791576000//86400)*86400+16*3600
    bars_15m = [
        {"time": now-(50-i)*900, "open": 100.0, "high": 102.0, "low": 99.0,
         "close": 101.0+.02*(i%2), "volume": 1000}
        for i in range(50)
    ]
    features = {"direction": "LONG", "atr": 2.0}
    quote = {"bid": 100.9, "ask": 101.1, "point": 0.01, "tick_size": 0.01, "time_msc": now*1000}
    pivots = {"vwap": 100.5, "vwap_sigma": 1.5, "swing_high": 105.0, "swing_low": 97.0}
    sizing = {"risk_usd": 12.0, "friction_usd": 0.40}

    ctx, missing = build_dg_context(
        features=features,
        payload={},
        pivots=pivots,
        quote=quote,
        bars_15m=bars_15m,
        entry=100.0,
        sl=96.0,
        tp=108.0,
        sizing=sizing,
        regime="TREND_UP",
    )
    assert not missing
    assert ctx["direction"] == "LONG"
    assert ctx["regime"] == "TREND_UP"
    assert ctx["entry"] == 100.0
    assert ctx["sl"] == 96.0
    assert ctx["tp"] == 108.0


def test_evaluate_candidate_dg_v3_execution():
    bars_15m = [
        {"open": 100.0 + i * 0.1, "high": 101.0 + i * 0.1, "low": 99.5 + i * 0.1, "close": 100.5 + i * 0.1, "volume": 1000}
        for i in range(60)
    ]
    features = {"direction": "LONG", "atr": 2.0}
    quote = {"bid": 106.4, "ask": 106.6, "point": 0.01, "tick_size": 0.01}
    pivots = {"vwap": 104.0, "vwap_sigma": 1.5, "swing_high": 115.0, "swing_low": 102.0}
    sizing = {"risk_usd": 12.0, "friction_usd": 0.40}

    res = evaluate_candidate_dg_v3(
        features=features,
        payload={},
        pivots=pivots,
        quote=quote,
        bars_15m=bars_15m,
        entry=104.0,
        sl=100.0,
        tp=114.0,
        sizing=sizing,
        symbol="BTCUSD.pi",
    )
    assert "regime" in res
    assert "passed" in res
    assert isinstance(res["failures"], list)


def context_fixture(count=60, now=None, direction="LONG", payload=None, pivots=None, features=None):
    now = now or (1791576000//86400)*86400+16*3600
    bars = [{"time": now-(count-i)*900, "open": 100, "high": 103,
             "low": 99, "close": 100+i*.01, "volume": 1000} for i in range(count)]
    args = dict(features={"direction": direction, "atr": 2, "asset": "BTC"} | (features or {}),
                payload=payload or {}, pivots=pivots, quote={"bid": 100, "ask": 100.02, "time_msc": now*1000},
                bars_15m=bars, entry=100, sl=96 if direction=="LONG" else 104,
                tp=108 if direction=="LONG" else 92, sizing={"risk_usd": 10, "friction_usd": .5}, symbol="BTCUSD.pi")
    return args


def test_partial_tape_and_absent_shelves_never_become_passing_evidence():
    args = context_fixture(payload={"orderflow": {"cvd_divergence": {"observed": True}}})
    ctx, missing = build_dg_context(**args)
    assert not missing
    assert ctx["orderflow"] is None and not ctx["allow_price_only_variant"]
    assert ctx["shelf"] == {"price": None, "confluence": 0}
    assert ctx["first_obstacle"] is None and ctx["p_win_lower_bound"] is None


@pytest.mark.parametrize("calibrated, probability, expected", [(False, .7, None), (True, .7, .7), (True, float("nan"), None)])
def test_win_probability_requires_explicit_calibrated_input(calibrated, probability, expected):
    ctx, _ = build_dg_context(**context_fixture(features={"p_win_lower_bound": probability,
                                                           "p_win_lower_bound_calibrated": calibrated}))
    assert ctx["p_win_lower_bound"] == expected


@pytest.mark.parametrize("direction,close,low,high", [("LONG", 95, 94, 99), ("SHORT", 110, 109, 111)])
def test_new_structure_break_is_not_hidden_by_including_latest_candle(direction, close, low, high):
    args = context_fixture(direction=direction)
    args["bars_15m"][-1].update(open=close, close=close, low=low, high=high)
    ctx, _ = build_dg_context(**args)
    assert not ctx["structure_intact"]


def test_swing_index_uses_forward_slice_and_excludes_pullback_candle(monkeypatch):
    import Terminal.dg_context as module
    args = context_fixture()
    args["bars_15m"][45]["high"] = 120
    args["bars_15m"][-1]["high"] = 130
    seen = []
    original = module.pullback_geometry
    def geometry(*pos, **kw):
        seen.append(kw["swing_idx"])
        return original(*pos, **kw)
    monkeypatch.setattr(module, "pullback_geometry", geometry)
    build_dg_context(**args)
    assert seen == [45]


@pytest.mark.parametrize("direction,highs,lows,closes", [("LONG", [102,120,126], [100,115,124], [101,119,125]),
                                                       ("SHORT", [120,104,96], [119,100,94], [120,101,95])])
def test_breakout_beyond_impulse_is_not_a_positive_retracement(direction, highs, lows, closes):
    from Terminal.decision_gates_v3 import pullback_geometry
    value = pullback_geometry(highs, lows, closes, direction, impulse_start=0, swing_idx=1, sigma_bar=.01)
    assert value["retrace"] < 0


def test_session_maturity_and_vwap_slope_are_measured_from_current_utc_day():
    day = (1791576000//86400)*86400
    args = context_fixture(count=180, now=day+3*900)
    ctx, missing = build_dg_context(**args)
    assert not missing
    assert ctx["session_bars"] == 3
    assert ctx["vwap_slope_sigma_per_bar"] > 0
    assert ctx["vwap_anchor_basis"] == "UTC_DAY"
    # Causal dz4 requires >= 5 session bars; 3-bar session fails closed (P1-2)
    assert ctx["vwap_z_change_4bars"] is None


def test_session_dz4_computed_causally_when_session_has_sufficient_bars():
    day = (1791576000//86400)*86400
    args = context_fixture(count=180, now=day+20*900)
    ctx, missing = build_dg_context(**args)
    assert not missing
    assert ctx["session_bars"] == 20
    assert ctx["vwap_z_change_4bars"] is not None


def test_missing_timestamps_and_forming_bars_do_not_produce_session_evidence():
    args = context_fixture()
    for row in args["bars_15m"]:
        row.pop("time")
    ctx, missing = build_dg_context(**args)
    assert "session_vwap_history_unavailable" in missing
    assert ctx["session_bars"] == 0 and ctx["vwap"] is None
    args = context_fixture()
    args["bars_15m"][-1]["time"] = args["quote"]["time_msc"]/1000
    assert "session_vwap_history_unavailable" in build_dg_context(**args)[1]


@pytest.mark.parametrize("field,value", [("high", None), ("low", float("nan")),
                                        ("close", 0), ("open", "100"), ("volume", -1)])
def test_malformed_bar_returns_failure_instead_of_throwing(field, value):
    args = context_fixture()
    args["bars_15m"][-1][field] = value
    ctx, failures = build_dg_context(**args)
    assert ctx == {} and failures


@pytest.mark.parametrize("change", [{"wall_class": "MIRRORED_LEG"}, {"wall_class": "TOP_OF_BOOK"},
                                    {"gate_g7_eligible": False}, {"persist_s": None},
                                    {"presence_frac": None}, {"price": "bad"}])
def test_wall_authenticity_and_measurements_cannot_be_bypassed(change):
    wall = {"side": "BUY", "price": 99.9, "notional_usd": 200000,
            "persist_s": 180, "presence_frac": .95, "wall_class": "GENUINE", "gate_g7_eligible": True}
    wall.update(change)
    ctx, _ = build_dg_context(**context_fixture(payload={"whale_walls_l3": [wall]}))
    assert ctx["wall"] is None


def test_measured_wall_is_mapped_without_fabricating_a_tape_baseline():
    wall = {"side": "BUY", "price": 99.9, "notional_usd": 200000,
            "persist_s": 180, "presence_frac": .95, "wall_class": "GENUINE", "gate_g7_eligible": True}
    ctx, _ = build_dg_context(**context_fixture(payload={"whale_walls_l3": [wall]}))
    assert ctx["wall"]["persist_s"] == 180
    assert ctx["wall"]["presence_frac"] == .95
    assert ctx["wall"]["median_1m_traded_usd"] is None


def test_absent_inventory_and_context_are_failures():
    result = evaluate_candidate_dg_v3({}, {}, None, {}, None)
    assert not result["passed"] and result["failures"] == ["context_input_invalid"]


@pytest.mark.parametrize("pivots", [{"vwap": []}, {"S1": {"price": 100}}, {"swing_high": {}}])
def test_nested_values_in_scalar_pivot_fields_fail_closed(pivots):
    ctx, failures = build_dg_context(**context_fixture(pivots=pivots))
    assert not ctx and failures == ["pivot_invalid"]


# ---------------------------------------------------------------------------
# Telemetry key aliases. The live MT5 path supplies quote["time_msc"] and
# bar["time"]. The emitted snapshot renames them to broker_tick_time_utc_msc and
# ts (Data_Factory/generate_telemetry_snapshot.py:1547), so every published
# snapshot returned session_vwap_history_unavailable -- at bar 0 and at bar 17
# alike. That was a key mismatch, not session immaturity, and it is why Model 1
# never reached A1 across a whole session of council cycles.
# ---------------------------------------------------------------------------

def _alias_bars(n=20, day_start=1791568000, key="time"):
    bars = []
    for i in range(n):
        close = 100.0 + 0.3 * i
        bars.append({key: day_start + i * 900, "open": close - 0.1,
                     "high": close + 0.5, "low": close - 0.5,
                     "close": close, "volume": 1000 + 10 * i})
    return bars


def _alias_quote(day_start=1791568000, n=20, key="time_msc"):
    observed = day_start + n * 900
    return {"bid": 100.9, "ask": 101.1, "point": 0.01, "tick_size": 0.01,
            key: observed * 1000}


def test_session_vwap_is_identical_under_telemetry_key_aliases():
    from Terminal.dg_context import _session_vwap
    canonical = _session_vwap(_alias_bars(key="time"), _alias_quote(key="time_msc"))
    aliased = _session_vwap(_alias_bars(key="ts"),
                            _alias_quote(key="broker_tick_time_utc_msc"))
    assert canonical[0] is not None, "canonical form must produce a session VWAP"
    assert aliased == canonical


def test_telemetry_only_payload_produces_a_session_instead_of_failing_closed():
    from Terminal.dg_context import _session_vwap
    vwap, sigma, slope, rows = _session_vwap(
        _alias_bars(key="ts"), _alias_quote(key="broker_tick_time_utc_msc"))
    assert vwap is not None and vwap > 0
    assert sigma is not None and sigma > 0
    assert slope is not None
    assert rows == 20


def test_session_vwap_prefers_time_msc_when_both_keys_are_present():
    from Terminal.dg_context import _session_vwap
    bars = _alias_bars(key="time")
    both = _alias_quote(key="time_msc")
    both["broker_tick_time_utc_msc"] = 1  # absurd value that must be ignored
    assert _session_vwap(bars, both) == _session_vwap(bars, _alias_quote(key="time_msc"))


@pytest.mark.parametrize("quote", [None, 5, "x", {}, {"time_msc": None},
                                   {"broker_tick_time_utc_msc": None}])
def test_session_vwap_fails_closed_without_a_usable_tick_clock(quote):
    from Terminal.dg_context import _session_vwap
    assert _session_vwap(_alias_bars(), quote) == (None, None, None, 0)


@pytest.mark.parametrize("bar", [None, 5, "x", {}, {"time": None, "ts": None}])
def test_session_vwap_fails_closed_on_bars_without_a_timestamp(bar):
    from Terminal.dg_context import _session_vwap
    bars = _alias_bars()
    bars[-1] = bar
    assert _session_vwap(bars, _alias_quote()) == (None, None, None, 0)


def test_build_dg_context_accepts_a_published_telemetry_snapshot_shape():
    """End-to-end: telemetry-shaped keys must not yield session_vwap_history_unavailable."""
    n = 20
    day_start = 1791568000
    bars = _alias_bars(n=n, day_start=day_start, key="ts")
    quote = {"bid": 100.9, "ask": 101.1, "point": 0.01, "tick_size": 0.01,
             "broker_tick_time_utc_msc": (day_start + n * 900) * 1000}
    ctx, missing = build_dg_context(
        features={"direction": "LONG", "atr": 2.0}, payload={}, pivots=None,
        quote=quote, bars_15m=bars, entry=100.0, sl=96.0, tp=108.0,
        sizing={"risk_usd": 12.0, "friction_usd": 0.40}, regime="MEAN_REVERT")
    assert "session_vwap_history_unavailable" not in missing
    assert ctx["vwap"] > 0 and ctx["session_sigma"] > 0
    assert ctx["session_bars"] == n


def test_evaluate_candidate_dg_v3_accepts_telemetry_snapshot_keys():
    """evaluate_candidate_dg_v3 must accept broker_tick_time_utc_msc and ts keys."""
    from Terminal.dg_context import evaluate_candidate_dg_v3
    from Terminal.policy import HTF_STRATEGY_MIN
    n = 100
    day_start = 1791568000
    bars_15m = _alias_bars(n=n, day_start=day_start, key="ts")
    bars_1h = _alias_bars(n=HTF_STRATEGY_MIN + 5, day_start=day_start, key="ts")
    bars_4h = _alias_bars(n=HTF_STRATEGY_MIN + 5, day_start=day_start, key="ts")
    observed = day_start + n * 900
    quote = {"bid": 100.9, "ask": 101.1, "point": 0.01, "tick_size": 0.01,
             "broker_tick_time_utc_msc": observed * 1000}
    res = evaluate_candidate_dg_v3(
        features={"direction": "LONG", "atr": 2.0},
        payload={},
        pivots=None,
        quote=quote,
        bars_15m=bars_15m,
        bars_1h=bars_1h,
        bars_4h=bars_4h,
        entry=100.0,
        sl=96.0,
        tp=108.0,
        sizing={"risk_usd": 12.0, "friction_usd": 0.40},
        symbol="TEST.p",
        as_of_epoch=observed,
    )
    assert res["failures"] != ["regime_history_time_invalid_or_noncausal"]
    assert res["regime"] != "UNDEFINED"


def test_audited_sample_admits_clopper_pearson_lower_bound():
    """An audited sample n >= 15 admits the exact Clopper-Pearson bound even if n < 100."""
    payload_audited = {
        "p_win_lower_bound": 0.4197,
        "p_win_lower_bound_calibrated": False,
        "p_win_calibration_sample_n": 17,
    }
    ctx, _ = build_dg_context(**context_fixture(payload=payload_audited))
    assert ctx["p_win_lower_bound"] == 0.4197

    # But an insufficient sample (< 15) without calibration remains blocked
    payload_small = {
        "p_win_lower_bound": 0.4197,
        "p_win_lower_bound_calibrated": False,
        "p_win_calibration_sample_n": 10,
    }
    ctx_small, _ = build_dg_context(**context_fixture(payload=payload_small))
    assert ctx_small["p_win_lower_bound"] is None


