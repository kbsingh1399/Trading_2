# Tests/Test_Forced_Liquidation_Daemon.py
import datetime
import pytest

from Terminal.Data_Factory.forced_liquidation_daemon import (
    ForcedLiquidationAggregator,
    LiquidationEvent,
    IST_TIMEZONE,
    UTC_TIMEZONE,
)

def test_liquidation_candle_bucketing_and_metrics():
    aggregator = ForcedLiquidationAggregator(symbols=["BTCUSDT", "ETHUSDT"])
    now_utc = datetime.datetime(2026, 10, 25, 12, 7, 30, tzinfo=UTC_TIMEZONE)

    # Ingest Long liquidation (Sell order on tape)
    event_long = LiquidationEvent(
        symbol="BTCUSDT",
        side="SELL",
        price=80500.0,
        quantity=2.0,
        usd_value=161000.0,
        timestamp_utc=now_utc,
    )
    aggregator.ingest_event(event_long)

    # Ingest Short liquidation (Buy order on tape)
    event_short = LiquidationEvent(
        symbol="BTCUSDT",
        side="BUY",
        price=80550.0,
        quantity=5.0,
        usd_value=402750.0,
        timestamp_utc=now_utc + datetime.timedelta(seconds=15),
    )
    aggregator.ingest_event(event_short)

    # Query 5m candle
    candle_5m = aggregator.get_current_candle("BTCUSDT", "5m", now_utc)
    assert candle_5m is not None
    assert candle_5m["long_liq_usd"] == 161000.0
    assert candle_5m["short_liq_usd"] == 402750.0
    assert candle_5m["total_liq_usd"] == 563750.0
    assert candle_5m["net_liq_delta_usd"] == 241750.0  # Short Liq - Long Liq
    assert "IST" in candle_5m["candle_start_ist"]
    assert candle_5m["dominant_side"] == "SHORTS_PURGED"

def test_multi_timeframe_buckets():
    aggregator = ForcedLiquidationAggregator(symbols=["BTCUSDT"])
    now_utc = datetime.datetime(2026, 10, 25, 12, 14, 0, tzinfo=UTC_TIMEZONE)

    # 15m candle bucket alignment
    bucket_15m_start, bucket_15m_end = aggregator.get_candle_bounds(now_utc, "15m")
    assert bucket_15m_start == datetime.datetime(2026, 10, 25, 12, 0, 0, tzinfo=UTC_TIMEZONE)
    assert bucket_15m_end == datetime.datetime(2026, 10, 25, 12, 15, 0, tzinfo=UTC_TIMEZONE)

    # 1h candle bucket alignment
    bucket_1h_start, bucket_1h_end = aggregator.get_candle_bounds(now_utc, "1h")
    assert bucket_1h_start == datetime.datetime(2026, 10, 25, 12, 0, 0, tzinfo=UTC_TIMEZONE)
    assert bucket_1h_end == datetime.datetime(2026, 10, 25, 13, 0, 0, tzinfo=UTC_TIMEZONE)

    # 4h candle bucket alignment
    bucket_4h_start, bucket_4h_end = aggregator.get_candle_bounds(now_utc, "4h")
    assert bucket_4h_start == datetime.datetime(2026, 10, 25, 12, 0, 0, tzinfo=UTC_TIMEZONE)
    assert bucket_4h_end == datetime.datetime(2026, 10, 25, 16, 0, 0, tzinfo=UTC_TIMEZONE)
