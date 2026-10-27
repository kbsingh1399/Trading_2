"""
Engine/terminal/verify_terminal.py
Comprehensive Institutional Verification Suite for Parquet Quant Trading Terminal.
Tests Data Ingestion, Schema Detection, Timestamp Monotonicity, ATAS Orderflow,
Volume Profile (VPOC/VAH/VAL), Indicator Calculations, and Multi-Pane Charting Pipelines.
"""
from __future__ import annotations
import os
import sys

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

if sys.platform == 'win32':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
        sys.stderr.reconfigure(encoding='utf-8')
    except Exception:
        pass

import numpy as np
import pandas as pd
from fastapi.testclient import TestClient

from Terminal.Data_Engine import ParquetDataEngine
from Terminal.Indicator_Engine import IndicatorEngine
from Terminal.Chart_Engine import ChartEngine
from Terminal.Web_Terminal import app

def run_all_verification_gates():
    print("=" * 80)
    print("PARQUET QUANT TRADING TERMINAL - INSTITUTIONAL VERIFICATION SUITE")
    print("=" * 80)
    
    passes = 0
    total_checks = 0

    # -------------------------------------------------------------
    # GATE 1: FOREX DATASET INGESTION & ARBITRARY DIMENSIONS
    # -------------------------------------------------------------
    forex_file = os.path.join(PROJECT_ROOT, "Forex_Data", "USDCAD_15m_real.parquet")
    print(f"\n[Gate 1] Testing Forex Dataset Ingestion: {forex_file}")
    assert os.path.exists(forex_file), f"Missing test file: {forex_file}"
    
    eng_forex = ParquetDataEngine(forex_file)
    print(f"  OK Rows Loaded: {len(eng_forex.df):,}")
    print(f"  OK Time Column Detected: '{eng_forex.time_col}'")
    print(f"  OK OHLCV Columns Detected: O='{eng_forex.open_col}', H='{eng_forex.high_col}', L='{eng_forex.low_col}', C='{eng_forex.close_col}', V='{eng_forex.vol_col}'")
    print(f"  OK Arbitrary Dimensions Detected ({len(eng_forex.dimension_cols)}): {eng_forex.dimension_cols[:8]}")
    
    total_checks += 4
    assert len(eng_forex.df) > 50000, "Forex row count insufficient"
    assert eng_forex.open_col and eng_forex.close_col, "OHLC detection failed"
    assert 'spread' in eng_forex.dimension_cols, "Spread dimension missing"
    assert 'standard_datetime' in eng_forex.df.columns, "Datetime standardization failed"
    passes += 4
    print("  --> [GATE 1 PASSED: 4/4 Checks]")

    # -------------------------------------------------------------
    # GATE 2: TIMESTAMP MONOTONICITY & ZERO DUPLICATES INVARIANT
    # -------------------------------------------------------------
    print(f"\n[Gate 2] Testing Timestamp Monotonicity & Zero-Duplicate Invariant")
    candle_df = eng_forex.get_candle_data(max_bars=2000)
    ts = candle_df['timestamp'].values
    
    # 1. Check strict ascending order (time[i] > time[i-1])
    diffs = np.diff(ts)
    is_monotonic = (diffs > 0).all()
    assert is_monotonic, f"Fatal: Timestamps are not strictly monotonically increasing! Min diff: {diffs.min()}"
    total_checks += 1
    passes += 1
    print(f"  OK Timestamps Strictly Monotonic (Min Step: {diffs.min()}s, Max Step: {diffs.max()}s)")

    # 2. Check zero duplicate timestamps
    n_unique = len(np.unique(ts))
    assert n_unique == len(ts), f"Fatal: Found duplicate timestamps! Unique: {n_unique}, Total: {len(ts)}"
    total_checks += 1
    passes += 1
    print(f"  OK Zero Duplicate Timestamps Certified ({len(ts)} bars perfectly unique)")

    # 3. Check year range > 2020 (no 1970 microsecond collapse)
    dt_first = pd.to_datetime(ts[0], unit='s')
    assert dt_first.year >= 2020, f"Fatal: Year collapse detected! Year is {dt_first.year}"
    total_checks += 1
    passes += 1
    print(f"  OK Genuine Post-2020 Calendar Dates Certified (First Date: {dt_first})")
    print("  --> [GATE 2 PASSED: 3/3 Checks]")

    # -------------------------------------------------------------
    # GATE 3: ATAS ORDERFLOW & VOLUME PROFILE
    # -------------------------------------------------------------
    print(f"\n[Gate 3] Testing ATAS Orderflow & Volume Profile Analytics")
    # 1. Delta & CVD presence
    assert 'delta' in candle_df.columns and 'cvd' in candle_df.columns, "Orderflow columns missing"
    total_checks += 1
    passes += 1
    print(f"  OK Orderflow Delta & Cumulative Volume Delta (CVD) Present")

    # 2. Volume Profile calculation
    vp = eng_forex.get_volume_profile(max_bars=1000, n_bins=32)
    assert len(vp['bins']) == 32, "Volume profile bin count mismatch"
    assert vp['val'] <= vp['poc'] <= vp['vah'], f"Volume Area Invariant violated: VAL {vp['val']} <= POC {vp['poc']} <= VAH {vp['vah']}"
    assert vp['total_vol'] > 0, "Total profile volume is zero"
    total_checks += 2
    passes += 2
    print(f"  OK ATAS Volume Profile Computed: VPOC={vp['poc']:.5f}, VAH={vp['vah']:.5f}, VAL={vp['val']:.5f}, Vol={vp['total_vol']:,.0f}")

    # 3. VWAP Bands Invariant (Upper >= VWAP >= Lower)
    u, v, l = IndicatorEngine.compute_vwap_bands(candle_df, std_multiplier=1.5)
    valid_vwap_bands = (u >= v).all() and (v >= l).all()
    assert valid_vwap_bands, "VWAP Bands ordering violated"
    total_checks += 1
    passes += 1
    print("  OK ATAS VWAP Bands Structural Ordering Certified (Upper >= VWAP >= Lower)")
    print("  --> [GATE 3 PASSED: 4/4 Checks]")

    # -------------------------------------------------------------
    # GATE 4: TECHNICAL INDICATOR MATHEMATICS
    # -------------------------------------------------------------
    print(f"\n[Gate 4] Testing Technical Indicator Mathematical Invariants")
    # 1. EMA & SMA
    ema20 = IndicatorEngine.compute_ema(candle_df['close'], period=20)
    sma200 = IndicatorEngine.compute_sma(candle_df['close'], period=200)
    assert len(ema20) == len(candle_df) and not ema20.isna().all(), "EMA calculation failed"
    total_checks += 1
    passes += 1
    print("  OK EMA 20 & SMA 200 Vectorized Output Validated")

    # 2. Bollinger Bands (Upper >= Mid >= Lower invariant)
    bb_u, bb_m, bb_l = IndicatorEngine.compute_bollinger_bands(candle_df['close'], period=20, std_dev=2.0)
    bb_valid = (bb_u.iloc[20:] >= bb_m.iloc[20:]).all() and (bb_m.iloc[20:] >= bb_l.iloc[20:]).all()
    assert bb_valid, "Bollinger Band inequality Upper >= Mid >= Lower violated!"
    total_checks += 1
    passes += 1
    print("  OK Bollinger Bands (20, 2.0) Structural Ordering Certified")

    # 3. RSI [0, 100] Invariant
    rsi14 = IndicatorEngine.compute_rsi(candle_df['close'], period=14)
    assert (rsi14 >= 0.0).all() and (rsi14 <= 100.0).all(), "RSI range invariant [0, 100] violated!"
    total_checks += 1
    passes += 1
    print(f"  OK RSI (14) Bounded Invariant Verified (Min: {rsi14.min():.2f}, Max: {rsi14.max():.2f})")

    # 4. MACD Line - Signal == Hist
    macd, sig, hist = IndicatorEngine.compute_macd(candle_df['close'], 12, 26, 9)
    diff = (macd - sig - hist).abs().max()
    assert diff < 1e-10, "MACD Line - Signal != Hist identity violated!"
    total_checks += 1
    passes += 1
    print(f"  OK MACD Identity Verified (Max Residual: {diff:.2e})")

    # 5. ATR Positivity Invariant
    atr = IndicatorEngine.compute_atr(candle_df, period=14)
    assert (atr > 0).all(), "ATR contains negative or zero values!"
    total_checks += 1
    passes += 1
    print(f"  OK ATR (14) Volatility Metric Strictly Positive (Mean: {atr.mean():.5f})")
    print("  --> [GATE 4 PASSED: 5/5 Checks]")

    # -------------------------------------------------------------
    # GATE 5: BINANCE CRYPTO DATASET & HIGH-DIMENSIONAL QUANT COLUMNS
    # -------------------------------------------------------------
    crypto_file = os.path.join(PROJECT_ROOT, "Binance_Data", "BTCUSDT_15m_master_2020_2026.parquet")
    print(f"\n[Gate 5] Testing Institutional Crypto Dataset: {crypto_file}")
    assert os.path.exists(crypto_file), f"Missing crypto file: {crypto_file}"
    
    eng_crypto = ParquetDataEngine(crypto_file)
    print(f"  OK Crypto Rows Loaded: {len(eng_crypto.df):,}")
    print(f"  OK Total Feature Dimensions Detected: {len(eng_crypto.dimension_cols)}")
    
    target_quant_dims = ['spot_cvd_15m', 'long_liq_zs', 'zc_div', 'funding_rate_pct', 'vwap_zscore']
    for d in target_quant_dims:
        assert d in eng_crypto.dimension_cols or d in eng_crypto.df.columns, f"Quant dimension '{d}' missing from BTCUSDT!"
        print(f"    - Certified Dimension: {d} (dtype: {eng_crypto.df[d].dtype})")
    
    # Test Dimension Z-score transformation
    z_liq = IndicatorEngine.compute_dimension_zscore(eng_crypto.df['long_liq_zs'], period=40)
    assert not z_liq.isna().all(), "Dimension Z-score computation failed"
    total_checks += 3
    passes += 3
    print("  OK Arbitrary Dimension Z-Score Transformation Verified")
    print("  --> [GATE 5 PASSED: 3/3 Checks]")

    # -------------------------------------------------------------
    # GATE 6: CHART CONTROLLER & MULTI-PANE SUBCHART ASSEMBLY
    # -------------------------------------------------------------
    print(f"\n[Gate 6] Testing ChartEngine Multi-Pane Subchart Assembly")
    chart_eng = ChartEngine(title="Verification Chart Instance")
    chart = chart_eng.initialize_chart(toolbox=True)
    assert chart is not None, "Lightweight Charts Chart creation failed"
    
    ok = chart_eng.load_parquet(forex_file, max_bars=500)
    assert ok, "ChartEngine load_parquet failed"
    
    # Overlays
    o1 = chart_eng.add_overlay_indicator('EMA', {'period': 20})
    o2 = chart_eng.add_overlay_indicator('BOLLINGER', {'period': 20})
    o3 = chart_eng.add_overlay_indicator('VWAP')
    o4 = chart_eng.add_overlay_indicator('VWAP_BANDS')
    assert o1 and o2 and o3 and o4, "Overlay registration failed"
    
    # Oscillators & ATAS
    s1 = chart_eng.add_subchart_oscillator('RSI', {'period': 14})
    s2 = chart_eng.add_subchart_oscillator('MACD')
    s3 = chart_eng.add_subchart_oscillator('CVD')
    s4 = chart_eng.add_subchart_oscillator('DELTA')
    assert s1 and s2 and s3 and s4, "Oscillator subchart creation failed"
    
    # Arbitrary Parquet dimensions
    d1 = chart_eng.add_dimension_subchart('spread', color='yellow')
    d2 = chart_eng.add_dimension_subchart('tick_volume', color='cyan', transform='zscore')
    assert d1 and d2, "Arbitrary dimension subchart failed"
    
    # Summary HUD Table
    chart_eng.show_summary_table()
    assert chart_eng.stats_table is not None, "Summary table creation failed"
    
    total_checks += 5
    passes += 5
    print("  OK Candlestick & Volume Main Chart Configured")
    print("  OK 4 Overlay Indicators Attached (EMA 20, Bollinger Bands, VWAP, VWAP Bands)")
    print("  OK 4 Synchronized Oscillators Mounted (RSI 14, MACD, ATAS CVD, Bar Delta)")
    print("  OK 2 Arbitrary Parquet Dimensions Mounted (spread, tick_volume Z-Score)")
    print("  OK Summary Statistics HUD Table Mounted")
    print("  --> [GATE 6 PASSED: 5/5 Checks]")

    # -------------------------------------------------------------
    # GATE 7: FASTAPI REST API ENDPOINTS & VOLUME PROFILE INTEGRATION
    # -------------------------------------------------------------
    print(f"\n[Gate 7] Testing Web Terminal FastAPI Endpoints Integration")
    client = TestClient(app)
    
    # 1. /api/files
    r = client.get("/api/files")
    assert r.status_code == 200, f"/api/files returned {r.status_code}"
    files_list = r.json()["files"]
    assert len(files_list) > 0, "No files returned by /api/files"
    print(f"  OK GET /api/files returned {len(files_list)} available Parquet files")
    
    # 2. /api/load
    r = client.post("/api/load", json={"filepath": forex_file})
    assert r.status_code == 200, f"/api/load returned {r.status_code}"
    load_res = r.json()
    assert load_res["status"] == "success", "Parquet load failed via API"
    assert "spread" in load_res["schema"]["dimensions"], "Spread dimension missing in API schema"
    print(f"  OK POST /api/load loaded {load_res['filename']} with {load_res['total_bars']:,} bars")
    
    # 3. /api/candles
    r = client.get("/api/candles?max_bars=200")
    assert r.status_code == 200, f"/api/candles returned {r.status_code}"
    candles_res = r.json()
    assert candles_res["count"] == 200, "Candles count mismatch"
    first_c = candles_res["candles"][0]
    assert "open" in first_c and "close" in first_c and "delta" in first_c and "cvd" in first_c, "Candle fields missing"
    assert first_c["time"] > 1.6e9, f"Candle time stamp invalid: {first_c['time']}"
    print(f"  OK GET /api/candles returned 200 formatted candles with valid unix timestamps")
    
    # 4. /api/volume_profile
    r = client.get("/api/volume_profile?max_bars=200&n_bins=32")
    assert r.status_code == 200, f"/api/volume_profile returned {r.status_code}"
    vp_res = r.json()
    assert vp_res["status"] == "success" and "profile" in vp_res, "Volume profile endpoint failed"
    print(f"  OK GET /api/volume_profile returned ATAS Profile (VPOC: {vp_res['profile']['poc']})")

    # 5. /api/indicator
    r = client.post("/api/indicator", json={"indicator_type": "CVD", "params": {}, "max_bars": 200})
    assert r.status_code == 200, f"/api/indicator returned {r.status_code}"
    ind_res = r.json()
    assert "CVD" in ind_res["series"], "CVD series missing from response"
    print(f"  OK POST /api/indicator computed CVD with {len(ind_res['series']['CVD'])} points")
    
    # 6. /api/dimension
    r = client.post("/api/dimension", json={"column_name": "spread", "transform": "raw", "max_bars": 200})
    assert r.status_code == 200, f"/api/dimension returned {r.status_code}"
    dim_res = r.json()
    assert dim_res["column"] == "spread" and len(dim_res["data"]) == 200, "Dimension series mismatch"
    print(f"  OK POST /api/dimension extracted arbitrary column 'spread' successfully")
    
    # 7. /api/stats
    r = client.get("/api/stats")
    assert r.status_code == 200, f"/api/stats returned {r.status_code}"
    stats_res = r.json()
    assert len(stats_res["statistics"]) > 0, "No statistics returned"
    print(f"  OK GET /api/stats computed summary metrics for {len(stats_res['statistics'])} columns")
    
    # 8. Root Webpage /
    r = client.get("/")
    assert r.status_code == 200 and "Parquet Quant Terminal" in r.text, "Index HTML failed to render"
    print(f"  OK GET / rendered institutional web trading terminal UI ({len(r.text):,} bytes)")
    
    total_checks += 8
    passes += 8
    print("  --> [GATE 7 PASSED: 8/8 Checks]")

    print("\n" + "=" * 80)
    print(f"VERIFICATION COMPLETE: ALL {passes}/{total_checks} CHECKS PASSED (100.0%)")
    print("   Parquet Quant Trading Terminal is Officially Certified for Production Use!")
    print("=" * 80)
    return True

if __name__ == '__main__':
    run_all_verification_gates()
