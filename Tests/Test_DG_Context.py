"""Tests for Terminal/dg_context.py context builder and evaluator."""
import pytest
from Terminal.dg_context import build_dg_context, evaluate_candidate_dg_v3


def test_build_dg_context_basic():
    bars_15m = [
        {"open": 100.0, "high": 102.0, "low": 99.0, "close": 101.0, "volume": 1000}
        for _ in range(50)
    ]
    features = {"direction": "LONG", "atr": 2.0}
    quote = {"bid": 100.9, "ask": 101.1, "point": 0.01, "tick_size": 0.01}
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
