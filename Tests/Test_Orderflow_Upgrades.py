"""Tests/Test_Orderflow_Upgrades.py
===================================
TDD suite for enhanced multi-horizon orderflow, TradFi tick CVD, HTF auction profiles,
and trapped trader detection in the telemetry pipeline.
"""
from __future__ import annotations

import pathlib
import sys
import time
import pytest
import numpy as np

REPO_ROOT = pathlib.Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

import Terminal.Data_Factory.generate_telemetry_snapshot as gts


# ---------------------------------------------------------------------------
# Test 1: Multi-Horizon Crypto CVD Calculation & Divergence Classification
# ---------------------------------------------------------------------------
def test_compute_multi_horizon_cvd_metrics():
    """Verify calculation of session, weekly, 24h CVD and divergence classification."""
    now_ts = 1791925000  # Arbitrary reference timestamp
    
    # 96 15m bars (24 hours) with mock volume and taker buy
    mock_15m_bars = []
    base_price = 83000.0
    for i in range(96):
        bar_ts = now_ts - (96 - i) * 900
        # Simulated price downtrend with bullish taker delta absorption
        p_close = base_price - i * 5.0
        q_vol = 1_000_000.0
        # More taker buys than sells => positive delta
        taker_buy = 650_000.0
        mock_15m_bars.append({
            "ts": bar_ts,
            "open": p_close + 2.0,
            "high": p_close + 5.0,
            "low": p_close - 5.0,
            "close": p_close,
            "quote_vol": q_vol,
            "taker_buy": taker_buy,
            "delta": taker_buy - (q_vol - taker_buy)  # +300,000 delta per bar
        })

    metrics = gts.compute_multi_horizon_cvd_metrics(mock_15m_bars, now_ts)
    assert isinstance(metrics, dict)
    assert "session_cvd_usd" in metrics
    assert "weekly_cvd_usd" in metrics
    assert "cvd_24h_usd" in metrics
    assert "bar_delta_15m_usd" in metrics
    assert "divergence" in metrics
    
    # Trailing 24h CVD must equal sum of all 96 bar deltas: 96 * 300,000 = 28,800,000
    assert metrics["cvd_24h_usd"] == 28_800_000.0
    assert metrics["bar_delta_15m_usd"] == 300_000.0
    # Price fell while delta was strongly positive => Bullish Absorption
    assert metrics["divergence"] == "BULLISH_ABSORPTION"


# ---------------------------------------------------------------------------
# Test 2: TradFi MT5 Tick-Delta Proxy (Lee-Ready Rule)
# ---------------------------------------------------------------------------
def test_compute_tradfi_tick_orderflow():
    """Verify Lee-Ready tick aggressor classification and OFI on mock MT5 ticks."""
    now_ts = 1791925000
    
    # Mock ticks: (time, bid, ask, last, volume, time_msc, flags, volume_real)
    mock_ticks = []
    base_bid = 7800.0
    base_ask = 7800.5
    for i in range(100):
        t_ts = now_ts - (100 - i) * 5
        # Upward price progression with buyer aggression
        bid = base_bid + (i // 10) * 0.25
        ask = base_ask + (i // 10) * 0.25
        # flags: 1030 = bid/ask update
        mock_ticks.append((t_ts, bid, ask, 0.0, 1, t_ts * 1000, 1030, 1.0))
        
    flow = gts.compute_tradfi_tick_orderflow(mock_ticks, now_ts)
    assert isinstance(flow, dict)
    assert flow["status"] == "CALCULATED_FROM_MT5_TICKS"
    assert "session_tick_cvd" in flow
    assert "15m_tick_cvd" in flow
    assert "5m_tick_cvd" in flow
    assert "flow_bias" in flow
    assert "order_flow_imbalance_ofi" in flow
    assert flow["flow_bias"] in ("BUYER_AGGRESSION", "SELLER_AGGRESSION", "NEUTRAL")


# ---------------------------------------------------------------------------
# Test 3: Multi-Timeframe Anchored Value Areas (HTF Auction Profiles)
# ---------------------------------------------------------------------------
def test_compute_htf_auction_profiles():
    """Verify calculation of Prior Day and Prior Week POC, VAH, VAL, and Weekly VWAP."""
    now_ts = 1791925000
    
    # 400 bars of 15m
    mock_bars = []
    for i in range(400):
        t_ts = now_ts - (400 - i) * 900
        p = 83000.0 + 50.0 * np.sin(i / 10.0)
        mock_bars.append({
            "time": t_ts,
            "open": p - 5.0,
            "high": p + 10.0,
            "low": p - 10.0,
            "close": p + 2.0,
            "volume": 100.0,
            "real_volume": 100.0
        })
        
    htf_prof = gts.compute_htf_auction_profiles(mock_bars, now_ts)
    assert isinstance(htf_prof, dict)
    assert "prior_day_poc" in htf_prof
    assert "prior_day_vah" in htf_prof
    assert "prior_day_val" in htf_prof
    assert "prior_week_poc" in htf_prof
    assert "prior_week_vah" in htf_prof
    assert "prior_week_val" in htf_prof
    assert "weekly_vwap" in htf_prof
    assert htf_prof["prior_day_poc"] is not None
    assert htf_prof["prior_day_vah"] is not None
    assert htf_prof["prior_day_val"] is not None
    assert htf_prof["prior_day_vah"] >= htf_prof["prior_day_val"]


# ---------------------------------------------------------------------------
# Test 4: Footprint POC Delta & Trapped Trader Detection
# ---------------------------------------------------------------------------
def test_detect_trapped_traders():
    """Verify trapped buyer / seller detection based on POC location and delta."""
    # Case 1: Trapped buyers (POC at high of range, positive delta, but price closed below POC)
    low_price = 100.0
    high_price = 110.0
    poc_price = 109.5  # Upper 33%
    poc_delta = +500_000.0
    current_price = 105.0  # Rejected downwards
    
    signal = gts.detect_trapped_traders(poc_price, poc_delta, current_price, low_price, high_price)
    assert signal == "TRAPPED_BUYERS_ABOVE"
    
    # Case 2: Trapped sellers (POC at low of range, negative delta, but price bounced above POC)
    poc_price_low = 100.5  # Lower 33%
    poc_delta_low = -500_000.0
    current_price_high = 106.0  # Rebounded upwards
    
    signal_low = gts.detect_trapped_traders(poc_price_low, poc_delta_low, current_price_high, low_price, high_price)
    assert signal_low == "TRAPPED_SELLERS_BELOW"


# ---------------------------------------------------------------------------
# Test 5: TradFi Ticks Numpy Structured Record Compatibility
# ---------------------------------------------------------------------------
def test_compute_tradfi_tick_orderflow_numpy_records():
    """Verify that MT5 numpy structured void records are correctly processed."""
    now_ts = 1791925000
    dtype = np.dtype([
        ('time', 'i8'), ('bid', 'f8'), ('ask', 'f8'), ('last', 'f8'),
        ('volume', 'u8'), ('time_msc', 'i8'), ('flags', 'u4'), ('volume_real', 'f8')
    ])
    raw_array = np.zeros(50, dtype=dtype)
    for i in range(50):
        t_ts = now_ts - (50 - i) * 5
        raw_array[i] = (t_ts, 7800.0 + i * 0.1, 7800.5 + i * 0.1, 0.0, 1, t_ts * 1000, 1030, 1.0)

    # Pass list of numpy.void items as returned by MT5 copy_ticks_from
    ticks_list = list(raw_array)
    res = gts.compute_tradfi_tick_orderflow(ticks_list, now_ts)
    assert res["status"] == "CALCULATED_FROM_MT5_TICKS"
    assert res["tick_count_analyzed"] == 50
    assert isinstance(res["session_tick_cvd"], float)
    assert isinstance(res["15m_tick_cvd"], float)
    assert isinstance(res["order_flow_imbalance_ofi"], float)
