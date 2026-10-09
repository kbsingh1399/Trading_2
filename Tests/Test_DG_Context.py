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
    args["bars_15m"][-1].update(close=close, low=low, high=high)
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
    assert ctx["vwap_z_change_4bars"] == pytest.approx((args["bars_15m"][-1]["close"]-args["bars_15m"][-5]["close"])/ctx["session_sigma"])


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
