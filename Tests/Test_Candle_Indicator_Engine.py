"""
Tests/Test_Candle_Indicator_Engine.py
=====================================
Unit tests for the Candle Persistence, Gap-Detection & Indicator Engine.
"""
from __future__ import annotations

import pathlib
import tempfile
import numpy as np
import pytest

from Terminal.Candle_Indicator_Engine import CandleIndicatorEngine


def _generate_synthetic_bars(count=96, start_time=1791200000.0, step=900.0, base_price=100.0, has_gap=False):
    bars = []
    curr_time = start_time
    curr_px = base_price
    for i in range(count):
        if has_gap and i == 20:
            curr_time += 1800.0  # Introduce a 30m gap (missing 1 bar)
        high = curr_px + 1.0
        low = curr_px - 1.0
        close = curr_px + 0.2
        volume = 1000.0 + (i * 10.0)
        bars.append({
            "time": curr_time,
            "open": curr_px,
            "high": high,
            "low": low,
            "close": close,
            "volume": volume,
            "tick_volume": volume,
            "real_volume": 0.0,
        })
        curr_time += step
        curr_px += 0.1
    return bars


def test_indicator_math_and_bands_ordering():
    bars = _generate_synthetic_bars(count=96, base_price=2000.0)
    ind = CandleIndicatorEngine.compute_indicators(bars)

    assert "active_vwap" in ind
    assert "active_sigma" in ind
    assert ind["active_sigma"] > 0

    # Mathematical structural ordering of bands
    assert ind["upper_3sd"] >= ind["upper_2sd"]
    assert ind["upper_2sd"] >= ind["upper_1sd"]
    assert ind["upper_1sd"] >= ind["active_vwap"]
    assert ind["active_vwap"] >= ind["lower_1sd"]
    assert ind["lower_1sd"] >= ind["lower_2sd"]
    assert ind["lower_2sd"] >= ind["lower_3sd"]

    # Indicators present
    assert ind["atr_14"] > 0
    assert 0 <= ind["rsi_14"] <= 100
    assert ind["ema_20"] > 0
    assert ind["ema_50"] > 0


def test_gap_detection():
    with tempfile.TemporaryDirectory() as tmpdir:
        class MockBridge:
            def resolve_symbol(self, asset):
                return f"{asset}USD"

            def get_recent_bars(self, symbol, count=96):
                return _generate_synthetic_bars(count=96, has_gap=True)

        engine = CandleIndicatorEngine(bridge=MockBridge(), storage_dir=pathlib.Path(tmpdir))
        res = engine.sync_candles("GOLD", count=96)

        assert res["success"] is True
        assert res["gap_count"] == 1
        assert res["gaps"][0]["missing_bars"] == 2

        # Check that parquet file was saved
        pq_path = pathlib.Path(tmpdir) / "GOLD_15m.parquet"
        assert pq_path.exists()


def test_vwap_opportunity_scanner():
    bars = _generate_synthetic_bars(count=96, base_price=100.0)
    # Artificially pump the last bar far above Upper 2 SD
    bars[-1]["close"] = 150.0
    bars[-1]["high"] = 151.0

    class MockBridge:
        def resolve_symbol(self, asset):
            return f"{asset}USD"

        def get_recent_bars(self, symbol, count=96):
            return bars

    with tempfile.TemporaryDirectory() as tmpdir:
        engine = CandleIndicatorEngine(bridge=MockBridge(), storage_dir=pathlib.Path(tmpdir), universe=("GOLD",))
        engine.sync_candles("GOLD")
        opps = engine.scan_vwap_opportunities(z_threshold=1.75)

        assert len(opps) == 1
        assert opps[0]["asset"] == "GOLD"
        assert opps[0]["direction"] == "SHORT"
        assert opps[0]["bias"] == "EXTREME_OVERBOUGHT"
        assert opps[0]["vwap_z"] > 1.75
