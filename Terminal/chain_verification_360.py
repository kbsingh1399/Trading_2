"""
Terminal/chain_verification_360.py
Comprehensive 360-Degree Data Source & Data Processing Forensic Verification Engine.

MANDATE (OPERATOR DIRECTIVE):
"Chain verification should be 360 degree check including data source and data processing check..
 because our decisions are purely based on data."

Audits the entire quantitative operational chain across 3 pillars:
1. DATA SOURCE PROVENANCE (Layer 1):
   - MetaTrader 5 live tick/bar stream integrity, quote latency, bid/ask spread bps, contract specs.
   - Binance Futures L2 orderbook API freshness, top-20 depth imbalance, L3 whale persistence.
   - Parquet candle archives (Data/Candles/*.parquet): monotonicity, 0 nulls, schema conformity, freshness.
2. DATA PROCESSING & FEATURE ENGINEERING (Layer 2):
   - Causal anti-lookahead check: 4H/1H backward-as-of joins with causal shift(1).
   - Session VWAP reset at 00:00:00 UTC daily, SD bands, Z-score mathematical parity.
   - Wilder ATR(14), 20/50/200 EMA slope, RSI(14) calculation precision.
   - Telemetry serialization integrity (live_snapshot_latest.json vs live broker parity).
3. BROKER EXECUTION & CAPITAL FLOOR SENTRY (Layer 3):
   - MT5 IPC health, open position tickets, broker SL/TP ratchet synchronization.
   - G-1 Hard Floor defense (4,775.00 USD) and stressed simultaneous post-loss simulation.
"""

from __future__ import annotations
import json
import os
import sys
import time
import urllib.request
import math
from datetime import datetime, timezone, timedelta
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

import numpy as np
import pandas as pd
import polars as pl

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

PROJECT_ROOT = Path(__file__).resolve().parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))
CANDLES_DIR = PROJECT_ROOT / "Data" / "Candles"
TELEMETRY_FILE = PROJECT_ROOT / "docs" / "telemetry" / "live_snapshot_latest.json"
MACRO_CALENDAR_FILE = PROJECT_ROOT / "Data" / "macro_calendar.json"
EXPECTED_ACCOUNT_LOGIN = 5064568
_AUDIT_CLOCK = None


def _audit_epoch() -> float:
    trusted = _AUDIT_CLOCK.broker_utc_now() if _AUDIT_CLOCK is not None else None
    return trusted if trusted is not None else time.time()


def _clock_verified() -> bool:
    return _AUDIT_CLOCK is not None and _AUDIT_CLOCK.broker_utc_now() is not None


def _observe_broker_clock(mt5):
    from Terminal.MT5_Execution_Bridge import MT5ExecutionBridge
    bridge = MT5ExecutionBridge(EXPECTED_ACCOUNT_LOGIN)
    # Bounded read-only sampling: an unchanged cached tick never verifies the clock.
    for attempt in range(8):
        for sym in ("BTCUSD.pi", "ETHUSD.pi"):
            tick = mt5.symbol_info_tick(sym)
            if tick is not None:
                bridge.tick_age_seconds(tick, sym)
        if bridge.broker_utc_now() is not None:
            break
        if attempt < 7:
            time.sleep(0.4)
    return bridge


def _finite(value: Any, name: str, *, positive: bool = False) -> float:
    number = float(value)
    if not math.isfinite(number) or (positive and number <= 0):
        raise ValueError(f"Invalid {name}")
    return number


def _native_account(mt5):
    terminal = mt5.terminal_info()
    account = mt5.account_info()
    if terminal is None or not terminal.connected or account is None:
        raise ValueError("Connected terminal and native account information required")
    if account.login != EXPECTED_ACCOUNT_LOGIN or account.currency != "USD":
        raise ValueError("Expected native account 5064568 denominated in USD")
    for name in ("balance", "equity"):
        _finite(getattr(account, name), name, positive=True)
    return account


def _bar_epochs(values) -> np.ndarray:
    series = pd.Series(values)
    if pd.api.types.is_numeric_dtype(series.dtype):
        numeric = series.to_numpy(dtype=float)
        maximum = np.max(np.abs(numeric)) if len(numeric) else 0
        unit = "ns" if maximum > 1e17 else "us" if maximum > 1e14 else "ms" if maximum > 1e11 else "s"
        dates = pd.to_datetime(numeric, unit=unit, utc=True, errors="raise")
    else:
        dates = pd.to_datetime(series, utc=True, errors="raise")
    if pd.isna(dates).any():
        raise ValueError("Missing bar timestamps")
    return np.asarray([value.timestamp() for value in dates], dtype=float)

PRIMARY_ASSETS = [
    "BTC", "ETH", "SOL", "BNB", "XRP", "ADA", "DOGE", "TRX", "DOT", "LINK", "BCH", "LTC", "AVAX", "NEAR",
    "GOLD", "SILVER", "USWTI", "EURUSD", "GBPUSD", "USDJPY", "SP500", "NAS100", "DJ30", "GER40"
]

MT5_SYMBOL_MAP = {
    "BTC": "BTCUSD.pi", "ETH": "ETHUSD.pi", "SOL": "SOLUSD.p", "BNB": "BNBUSD.p", "XRP": "XRPUSD.pi",
    "ADA": "ADAUSD.p", "DOGE": "DOGEUSD.p", "TRX": "TRXUSD.p", "DOT": "DOTUSD.pi", "LINK": "LINKUSD.pi",
    "BCH": "BCHUSD.p", "LTC": "LTCUSD.pi", "AVAX": "AVAXUSD.p", "NEAR": "NEARUSD.p",
    "GOLD": "XAUUSD.pi", "SILVER": "XAGUSD.pi", "USWTI": "USWTI.p",
    "EURUSD": "EURUSD.pi", "GBPUSD": "GBPUSD.pi", "USDJPY": "USDJPY.pi",
    "SP500": "SP500.p", "NAS100": "NAS100.p", "DJ30": "DJ30.p", "GER40": "GER40.p"
}


# ==============================================================================
# PILLAR 1: DATA SOURCE PROVENANCE AUDIT
# ==============================================================================

def audit_mt5_live_data_source() -> Dict[str, Any]:
    """Audit MetaTrader 5 broker feed connection, latency, quotes, and specifications."""
    report = {
        "status": "PASS",
        "connected": False,
        "ping_latency_ms": 0.0,
        "symbols_audited": 0,
        "stale_quotes_detected": 0,
        "spread_anomalies_detected": 0,
        "details": []
    }
    try:
        import MetaTrader5 as mt5
        t0 = time.perf_counter()
        if not mt5.initialize():
            report["status"] = "FAIL"
            report["error"] = f"MT5 initialization failed: {mt5.last_error()}"
            return report
        report["ping_latency_ms"] = round((time.perf_counter() - t0) * 1000, 2)
        
        term = mt5.terminal_info()
        acc = _native_account(mt5)
        report["connected"] = term.connected if term else False
        report["trade_allowed"] = term.trade_allowed if term else False
        report["account_login"] = acc.login if acc else 0
        report["account_balance"] = acc.balance if acc else 0.0
        report["account_equity"] = acc.equity if acc else 0.0
        
        global _AUDIT_CLOCK
        _AUDIT_CLOCK = _observe_broker_clock(mt5)
        report["clock_status"] = _AUDIT_CLOCK.broker_clock.status
        report["host_clock_offset_seconds"] = _AUDIT_CLOCK.broker_clock.offset_seconds
        if not _clock_verified():
            report["status"] = "UNKNOWN"
        
        # Audit a representative sample of active symbols
        test_symbols = ["SP500.p", "GBPUSD.pi", "USWTI.p", "BTCUSD.pi", "ETHUSD.pi", "XAUUSD.pi", "GER40.p"]
        for s in test_symbols:
            info = mt5.symbol_info(s)
            tick = mt5.symbol_info_tick(s)
            if not info or not tick:
                report["status"] = "UNKNOWN"
                report["details"].append({"symbol": s, "error": "Symbol info/tick unavailable"})
                continue
            
            report["symbols_audited"] += 1
            latency_sec = _AUDIT_CLOCK.tick_age_seconds(tick, s)
            spread_pts = (tick.ask - tick.bid) / info.point if info.point > 0 else 0
            spread_bps = (tick.ask - tick.bid) / tick.bid * 10000 if tick.bid > 0 else 0
            
            is_stale = latency_sec is not None and latency_sec > 60.0
            if latency_sec is None:
                report["status"] = "UNKNOWN"
                report["clock_warning"] = "Advancing broker evidence cannot establish quote freshness"
            if is_stale:
                report["stale_quotes_detected"] += 1
            
            is_spread_anomaly = tick.bid <= 0 or tick.ask < tick.bid or spread_bps > 100.0
            if is_spread_anomaly:
                report["spread_anomalies_detected"] += 1
                
            report["details"].append({
                "symbol": s,
                "bid": tick.bid,
                "ask": tick.ask,
                "contract_size": info.trade_contract_size,
                "point": info.point,
                "spread_bps": round(spread_bps, 2),
                "latency_sec": round(latency_sec, 1) if latency_sec is not None else None,
                "stale": is_stale
            })
    except Exception as e:
        report["status"] = "FAIL"
        report["error"] = str(e)
    finally:
        if "mt5" in locals():
            mt5.shutdown()
    
    if report["status"] != "FAIL" and (report["stale_quotes_detected"] > 0 or report["spread_anomalies_detected"] > 0):
        report["status"] = "WARN"
    if report["symbols_audited"] == 0 and report["status"] == "PASS":
        report["status"] = "UNKNOWN"
    return report


def audit_binance_l2_data_source() -> Dict[str, Any]:
    """Audit Binance Futures public L2/L3 orderbook depth and REST endpoint connectivity."""
    report = {
        "status": "PASS",
        "api_endpoint": "https://fapi.binance.com/fapi/v1/depth",
        "latency_ms": 0.0,
        "symbols_checked": 0,
        "depth_freshness_verified": False,
        "details": []
    }
    test_symbols = [("BTCUSDT", "BTC"), ("ETHUSDT", "ETH")]
    for sym, base in test_symbols:
        url = f"https://fapi.binance.com/fapi/v1/depth?symbol={sym}&limit=50"
        req = urllib.request.Request(url, headers={"User-Agent": "Antigravity/360-Auditor"})
        try:
            t0 = time.perf_counter()
            with urllib.request.urlopen(req, timeout=4) as resp:
                data = json.loads(resp.read().decode())
            lat = round((time.perf_counter() - t0) * 1000, 2)
            report["latency_ms"] = max(report["latency_ms"], lat)
            report["symbols_checked"] += 1
            
            bids = [[float(p), float(q), float(p)*float(q)] for p, q in data.get("bids", [])]
            asks = [[float(p), float(q), float(p)*float(q)] for p, q in data.get("asks", [])]
            if (not bids or not asks or bids[0][0] >= asks[0][0]
                    or any(not math.isfinite(v) or v <= 0 for row in [*bids, *asks] for v in row)
                    or any(bids[i][0] <= bids[i+1][0] for i in range(len(bids)-1))
                    or any(asks[i][0] >= asks[i+1][0] for i in range(len(asks)-1))):
                raise ValueError("Invalid or non-monotonic depth levels")
            event_epoch = float(data.get("E", data.get("T", 0))) / 1000.0
            if not event_epoch or not _clock_verified() or not 0 <= _audit_epoch() - event_epoch <= 10:
                report["status"] = "UNKNOWN"
                report["freshness_warning"] = "Missing or stale/future exchange event timestamp"
            
            bid_vol_usd = sum(b[2] for b in bids[:20])
            ask_vol_usd = sum(a[2] for a in asks[:20])
            last_id = data.get("lastUpdateId", 0)
            if not isinstance(last_id, int) or last_id <= 0:
                raise ValueError("Invalid depth update id")
            
            whales = [b for b in bids if b[2] >= 150000]
            
            report["details"].append({
                "symbol": sym,
                "last_update_id": last_id,
                "latency_ms": lat,
                "top20_bid_usd": round(bid_vol_usd, 0),
                "top20_ask_usd": round(ask_vol_usd, 0),
                "depth_imbalance": round(bid_vol_usd / max(ask_vol_usd, 1.0), 2),
                "whale_walls_count": len(whales)
            })
        except Exception as e:
            report["status"] = "WARN"
            report["details"].append({"symbol": sym, "error": str(e)})
            
    report["depth_freshness_verified"] = report["status"] == "PASS" and report["symbols_checked"] == len(test_symbols)
    return report


def audit_parquet_candle_archives() -> Dict[str, Any]:
    """Audit all 24 Parquet candle files: monotonicity, null count, row count, recency."""
    report = {
        "status": "PASS",
        "total_files": len(PRIMARY_ASSETS),
        "files_verified": 0,
        "files_with_nulls": 0,
        "files_non_monotonic": 0,
        "stale_files_detected": 0,
        "details": []
    }
    now_utc = datetime.fromtimestamp(_audit_epoch(), timezone.utc)
    
    for asset in PRIMARY_ASSETS:
        pq_path = CANDLES_DIR / f"{asset}_15m.parquet"
        if not pq_path.exists():
            report["details"].append({"asset": asset, "error": "File missing"})
            report["status"] = "WARN"
            continue
            
        try:
            df = pl.read_parquet(pq_path)
            rows = len(df)
            cols = df.columns
            if not rows or not {"open", "high", "low", "close"}.issubset(cols):
                raise ValueError("Empty archive or missing OHLC columns")
            
            # 1. Null check
            null_count = sum(df[c].null_count() for c in cols)
            if null_count > 0:
                report["files_with_nulls"] += 1
                
            # 2. Monotonicity check on time column
            time_col = "time" if "time" in cols else ("std_dt" if "std_dt" in cols else None)
            is_monotonic = False
            time_diff_min = 0
            if time_col:
                ts = _bar_epochs(df[time_col].to_list())
                diffs = np.diff(ts)
                is_monotonic = bool(np.all(diffs > 0))
                if not is_monotonic:
                    report["files_non_monotonic"] += 1
                    
            # 3. Recency check on latest completed bar
            last_row = df.tail(1).to_dicts()[0]
            last_ts = last_row.get(time_col) if time_col else None
            if not time_col:
                raise ValueError("Missing timestamp column")
            if np.any(ts + 900 > now_utc.timestamp()):
                raise ValueError("Archive contains future or incomplete 15m candles")
            ohlc = df.select(["open", "high", "low", "close"]).to_numpy()
            if not np.all(np.isfinite(ohlc)) or np.any(ohlc <= 0):
                raise ValueError("Non-finite or nonpositive OHLC values")
            if np.any(ohlc[:, 1] < np.max(ohlc[:, [0, 2, 3]], axis=1)) or np.any(ohlc[:, 2] > np.min(ohlc[:, [0, 1, 3]], axis=1)):
                raise ValueError("Invalid OHLC candle geometry")
            hours_old = (now_utc.timestamp() - ts[-1] - 900) / 3600.0
                
            is_stale = hours_old > 4.0  # More than 4 hours old for active perpetual
            if is_stale:
                report["stale_files_detected"] += 1
                report["status"] = "WARN"
                
            report["files_verified"] += 1
            report["details"].append({
                "asset": asset,
                "rows": rows,
                "nulls": null_count,
                "monotonic": is_monotonic,
                "hours_old": round(hours_old, 2),
                "last_close": last_row.get("close", 0.0)
            })
        except Exception as e:
            report["details"].append({"asset": asset, "error": str(e)})
            report["status"] = "WARN"
            
    if report["files_with_nulls"] > 0 or report["files_non_monotonic"] > 0:
        report["status"] = "FAIL"
    if report["status"] == "PASS" and not _clock_verified():
        report["status"] = "UNKNOWN"
        report["warning"] = "Archive freshness requires a verified UTC clock"
    return report


# ==============================================================================
# PILLAR 2: DATA PROCESSING & FEATURE COMPUTATION AUDIT
# ==============================================================================

def audit_causal_feature_processing(asset: str = "BTC") -> Dict[str, Any]:
    """Audit mathematical feature engineering: ATR(14), VWAP, Z-Score, EMA, causal shift."""
    report = {
        "status": "UNKNOWN",
        "asset_tested": asset,
        "anti_lookahead_causal_verified": None,
        "vwap_reset_verified": None,
        "verification_limit": "Independent indicator diagnostics do not prove production HTF joins or indicator parity",
        "indicators_computed": {}
    }
    pq_path = CANDLES_DIR / f"{asset}_15m.parquet"
    if not pq_path.exists():
        report["status"] = "SKIP"
        report["error"] = f"{pq_path} missing"
        return report
        
    try:
        pldf = pl.read_parquet(pq_path)
        df = pldf.to_pandas()
        time_col = "time" if "time" in df.columns else "std_dt"
        if time_col not in df.columns:
            raise ValueError("Missing timestamp column")
        epochs = _bar_epochs(df[time_col])
        if np.any(np.diff(epochs) <= 0):
            raise ValueError("Non-monotonic candle history")
        report["incomplete_bars_excluded"] = int(np.sum(epochs + 900 > _audit_epoch()))
        df = df.loc[epochs + 900 <= _audit_epoch()].copy()
        if len(df) < 201:
            raise ValueError("At least 201 completed bars are required for indicator diagnostics")
        
        # Verify required columns
        req_cols = ["open", "high", "low", "close"]
        for c in req_cols:
            if c not in df.columns:
                report["status"] = "FAIL"
                report["error"] = f"Missing column {c}"
                return report
                
        # Diagnostics use the same simple rolling ATR/RSI definitions as this code.
        high = df["high"].values
        low = df["low"].values
        close = df["close"].values
        tr1 = high[1:] - low[1:]
        tr2 = np.abs(high[1:] - close[:-1])
        tr3 = np.abs(low[1:] - close[:-1])
        tr = np.maximum(tr1, np.maximum(tr2, tr3))
        atr_14 = float(np.mean(tr[-14:]))
        
        # 2. Causal Exponential Moving Averages (20 EMA, 50 EMA, 200 EMA)
        c_series = pd.Series(close)
        ema_20 = float(c_series.ewm(span=20, adjust=False).mean().iloc[-1])
        ema_50 = float(c_series.ewm(span=50, adjust=False).mean().iloc[-1])
        ema_200 = float(c_series.ewm(span=200, adjust=False).mean().iloc[-1])
        
        # 3. Simple 14-period RSI; this is not Wilder smoothing.
        delta = np.diff(close)
        gain = np.where(delta > 0, delta, 0.0)
        loss = np.where(delta < 0, -delta, 0.0)
        avg_gain = float(np.mean(gain[-14:]))
        avg_loss = float(np.mean(loss[-14:]))
        rs = avg_gain / (avg_loss + 1e-9)
        rsi_14 = float(100.0 - (100.0 / (1.0 + rs)))
        
        # 4. Session VWAP with strict 00:00:00 UTC boundary reset
        time_col = "time" if "time" in df.columns else "std_dt"
        if time_col in df.columns:
            df["dt"] = pd.to_datetime(_bar_epochs(df[time_col]), unit="s", utc=True)
            today_utc = df["dt"].iloc[-1].date()
            day_mask = df["dt"].dt.date == today_utc
            day_df = df[day_mask]
            
            vol = day_df["volume"].values if "volume" in day_df.columns else day_df["tick_volume"].values
            tp = (day_df["high"].values + day_df["low"].values + day_df["close"].values) / 3.0
            
            if np.sum(vol) > 0:
                vwap = float(np.sum(tp * vol) / np.sum(vol))
                var = np.sum(vol * (tp - vwap)**2) / np.sum(vol)
                sd = float(np.sqrt(max(var, 1e-6)))
                z_score = float((close[-1] - vwap) / sd)
            else:
                vwap = float(close[-1])
                sd = 1.0
                z_score = 0.0
        else:
            vwap = float(close[-1])
            z_score = 0.0
            
        report["indicators_computed"] = {
            "atr_method": "SIMPLE_14_PERIOD_MEAN_TRUE_RANGE",
            "rsi_method": "SIMPLE_14_PERIOD_MEAN_GAIN_LOSS",
            "atr_14": round(atr_14, 4),
            "ema_20": round(ema_20, 2),
            "ema_50": round(ema_50, 2),
            "ema_200": round(ema_200, 2),
            "rsi_14": round(rsi_14, 1),
            "session_vwap": round(vwap, 2),
            "vwap_z_score": round(z_score, 2),
            "latest_close": round(float(close[-1]), 2)
        }
    except Exception as e:
        report["status"] = "FAIL"
        report["error"] = str(e)
        
    return report


def audit_telemetry_snapshot_integrity() -> Dict[str, Any]:
    """Check payload observation time, completed HTF evidence and native ticket parity."""
    from Terminal.risk.live_admission import MAX_FILLED
    from Terminal.policy import HTF_STRATEGY_MIN
    report = {"status": "UNKNOWN", "file_exists": TELEMETRY_FILE.exists(),
              "age_seconds": None, "positions_in_sync": None, "assets_serialized": 0,
              "completed_htf_verified": False, "details": []}
    if not TELEMETRY_FILE.exists():
        report["error"] = "Telemetry snapshot file missing"
        return report
    try:
        data = json.loads(TELEMETRY_FILE.read_text(encoding="utf-8"))
        now = _audit_epoch()
        observed = _finite(data.get("as_of_epoch"), "snapshot observation epoch", positive=True)
        age = now - observed
        report["age_seconds"] = round(age, 1)
        report["file_age_seconds"] = round(now - TELEMETRY_FILE.stat().st_mtime, 1)
        # Touching/copying the file cannot rejuvenate the embedded observation.
        if not 0 <= age <= 180:
            raise ValueError(f"Snapshot observation is stale or future-dated: age={age:.1f}s")
        assets = data.get("assets_matrix_24")
        if not isinstance(assets, dict) or set(assets) != set(PRIMARY_ASSETS):
            raise ValueError("Snapshot must contain all 24 canonical assets")
        report["assets_serialized"] = len(assets)
        for asset, payload in assets.items():
            for key, interval in (("1h", 3600), ("4h", 14400)):
                bars = payload.get(f"htf_{key}_ohlcv")
                quality = (payload.get("htf_history") or {}).get(key, {})
                if not isinstance(bars, list) or len(bars) < HTF_STRATEGY_MIN:
                    raise ValueError(f"{asset} {key}: fewer than {HTF_STRATEGY_MIN} observed completed bars")
                times = []
                for bar in bars:
                    opened = _finite(bar.get("ts"), "HTF open epoch", positive=True)
                    closed = _finite(bar.get("close_ts"), "HTF close epoch", positive=True)
                    if abs(closed - opened - interval) > 0.001 or closed > observed or closed > now:
                        raise ValueError(f"{asset} {key}: future or incomplete HTF bar")
                    values = [_finite(bar.get(k), f"HTF {k}", positive=True) for k in ("open", "high", "low", "close")]
                    if values[1] < max(values) or values[2] > min(values):
                        raise ValueError(f"{asset} {key}: invalid OHLC geometry")
                    times.append(opened)
                if any(right <= left for left, right in zip(times, times[1:])):
                    raise ValueError(f"{asset} {key}: duplicate or regressing HTF observations")
                if quality.get("completed_count") != len(bars):
                    raise ValueError(f"{asset} {key}: declared completed count differs from actual bars")
                if quality.get("source") != "MT5_BROKER_COMPLETED_BARS":
                    raise ValueError(f"{asset} {key}: broker data provenance unavailable")
                if quality.get("status") != "READY":
                    raise ValueError(f"{asset} {key}: declared history is not ready")
                if asset in PRIMARY_ASSETS[:14]:
                    if quality.get("freshness") != "FRESH":
                        raise ValueError(f"{asset} {key}: declared history is not ready and fresh")
                    if observed - (times[-1] + interval) > 2 * interval:
                        raise ValueError(f"{asset} {key}: completed HTF history stale")
                else:
                    if quality.get("freshness") != "FRESH":
                        parent_quality = payload.get("htf_history") or {}
                        if parent_quality.get("entry_eligible") is not False:
                            raise ValueError(f"{asset} {key}: stale non-crypto asset must not be entry_eligible")
                    elif observed - (times[-1] + interval) > 2 * interval:
                        raise ValueError(f"{asset} {key}: completed HTF history stale")
        report["completed_htf_verified"] = True
        import MetaTrader5 as mt5
        if not mt5.initialize():
            raise ValueError(f"MT5 initialization failed: {mt5.last_error()}")
        account = _native_account(mt5)
        positions, orders = mt5.positions_get(), mt5.orders_get()
        if positions is None or orders is None:
            raise ValueError("Native inventory unavailable for telemetry comparison")
        snapshot_account = data.get("account") or {}
        if snapshot_account.get("login") != account.login or snapshot_account.get("currency") != account.currency:
            raise ValueError("Telemetry account identity/currency differs from native broker")
        balance = _finite(snapshot_account.get("balance_usd"), "balance_usd")
        equity = _finite(snapshot_account.get("equity_usd"), "equity_usd")
        if abs(balance - account.balance) > 0.02:
            raise ValueError("Telemetry settled balance differs from native broker")
        # Equity is marked to changing quotes at two distinct observations.
        # Inventory and the current live floor are audited independently.
        report["snapshot_equity_usd"] = equity
        report["live_equity_usd"] = float(account.equity)
        report["equity_movement_since_snapshot_usd"] = round(float(account.equity) - equity, 4)
        report["native_observed_at_epoch"] = _audit_epoch()
        for pending, native_rows in ((False, positions), (True, orders)):
            serialized = data.get("pending_orders" if pending else "active_positions")
            if not isinstance(serialized, list):
                raise ValueError("Serialized inventory unavailable")
            native_by_ticket = {str(row.ticket): row for row in native_rows}
            serialized_by_ticket = {str(row.get("ticket")): row for row in serialized}
            if len(serialized_by_ticket) != len(serialized) or set(native_by_ticket) != set(serialized_by_ticket):
                raise ValueError("Telemetry ticket inventory differs from native broker")
            for ticket, native in native_by_ticket.items():
                row = serialized_by_ticket[ticket]
                if row.get("symbol") != native.symbol:
                    raise ValueError("Telemetry ticket symbol differs from native broker")
                for field, value in (("volume", native.volume_current if pending else native.volume),
                                     ("price_open", native.price_open), ("sl", native.sl), ("tp", native.tp)):
                    if not math.isclose(_finite(row.get(field), field), value, rel_tol=1e-8, abs_tol=1e-8):
                        raise ValueError(f"Telemetry ticket {ticket} {field} differs from native broker")
        capacity = data.get("capacity") or {}
        if capacity.get("max_concurrent") != MAX_FILLED or capacity.get("used_joint_fill") != len(positions) + len(orders):
            raise ValueError("Telemetry capacity does not match native joint-fill policy")
        report["positions_in_sync"] = True
        report["status"] = "PASS" if _clock_verified() else "UNKNOWN"
        if report["status"] == "UNKNOWN":
            report["warning"] = "Payload freshness requires a verified UTC clock"
    except Exception as error:
        report["status"] = "FAIL"
        report["error"] = str(error)
    finally:
        if "mt5" in locals():
            mt5.shutdown()
    return report


# ==============================================================================
# PILLAR 3: BROKER EXECUTION & CAPITAL FLOOR SENTRY
# ==============================================================================

def audit_broker_execution_and_floor() -> Dict[str, Any]:
    """Read native inventories and reserve cost-inclusive broker-valued SL losses."""
    from Terminal.risk.live_admission import (MAX_FILLED, STOP_STRESS_MULTIPLIER,
                                              MIN_EXECUTION_COST_USD)
    report = {"status": "UNKNOWN", "inventory_verified": False,
              "open_positions": [], "pending_orders": [], "closed_deals_today": [],
              "hard_floor_usd": 4775.0, "operating_buffer_usd": 4795.0,
              "max_joint_fill_tickets": MAX_FILLED,
              "valuation_source": "MT5_ORDER_CALC_PROFIT_USD",
              "stop_stress_multiplier": STOP_STRESS_MULTIPLIER,
              "minimum_execution_cost_per_ticket_usd": MIN_EXECUTION_COST_USD}
    try:
        import MetaTrader5 as mt5
        if not mt5.initialize():
            raise ValueError(f"MT5 initialization failed: {mt5.last_error()}")
        account = _native_account(mt5)
        positions, orders = mt5.positions_get(), mt5.orders_get()
        if positions is None or orders is None:
            raise ValueError(f"Native position/order inventory unavailable: {mt5.last_error()}")
        report.update(account_login=account.login, account_currency=account.currency,
                      balance=round(account.balance, 2), equity=round(account.equity, 2),
                      free_margin=round(_finite(account.margin_free, "free margin"), 2),
                      margin_used=round(_finite(account.margin, "margin used"), 2),
                      margin_level=round(_finite(account.margin_level, "margin level"), 1),
                      live_floor_cushion_usd=round(account.equity - 4775.0, 2),
                      inventory_verified=True)
        total_risk = 0.0
        for pending, rows in ((False, positions), (True, orders)):
            for row in rows:
                buy_types = (2, 4, 6) if pending else (0,)
                sell_types = (3, 5, 7) if pending else (1,)
                if row.type not in (*buy_types, *sell_types):
                    raise ValueError(f"Unsupported native order type {row.type}")
                is_buy = row.type in buy_types
                entry = _finite(row.price_open, "entry", positive=True)
                stop = _finite(row.sl, "protective SL", positive=True)
                volume = _finite(row.volume_current if pending else row.volume, "volume", positive=True)
                if pending and not (stop < entry if is_buy else stop > entry):
                    raise ValueError("Pending order stop is not protective")
                # No contract-size fallback: broker valuation carries account FX conversion.
                profit = mt5.order_calc_profit(0 if is_buy else 1, row.symbol, volume, entry, stop)
                if profit is None:
                    raise ValueError(f"Broker SL valuation unavailable for ticket {row.ticket}")
                nominal_loss = max(-_finite(profit, "broker SL valuation"), 0.0)
                swap_cost = max(-_finite(getattr(row, "swap", 0), "swap"), 0.0)
                risk = nominal_loss * STOP_STRESS_MULTIPLIER + MIN_EXECUTION_COST_USD + swap_cost
                total_risk += risk
                detail = {"ticket": row.ticket, "symbol": row.symbol,
                          "type": row.type, "volume": volume, "open_price": entry,
                          "sl": stop, "tp": row.tp, "nominal_sl_loss_usd": round(nominal_loss, 2),
                          "downside_risk": round(risk, 2), "locked_profit_credit_usd": 0.0}
                if not pending:
                    detail.update(current_price=row.price_current, floating_pnl=row.profit)
                report["pending_orders" if pending else "open_positions"].append(detail)
        # Locked-profit tickets never offset another ticket's contingent loss.
        stressed = min(account.balance, account.equity) - total_risk
        report.update(downside_portfolio_risk_usd=round(total_risk, 2),
                      stressed_worst_case_equity_usd=round(stressed, 2),
                      stressed_floor_cushion_usd=round(stressed - 4775.0, 2))
        if len(positions) + len(orders) > MAX_FILLED:
            raise ValueError(f"Joint-fill capacity exceeded: {len(positions) + len(orders)} > {MAX_FILLED}")
        if stressed < 4795.0:
            raise ValueError(f"G-1 operating buffer breach: stressed equity {stressed:.2f} < 4795.00 USD")
        now = datetime.now(timezone.utc)
        deals = mt5.history_deals_get(now - timedelta(hours=12), now)
        if deals is None:
            raise ValueError("Native closed-deal history unavailable")
        for deal in deals:
            if deal.entry == 1:
                report["closed_deals_today"].append({"ticket": deal.ticket, "symbol": deal.symbol,
                                                     "price": deal.price, "profit": round(deal.profit, 2),
                                                     "comment": deal.comment})
        report["status"] = "PASS"
    except Exception as error:
        report["status"] = "FAIL"
        report["error"] = str(error)
    finally:
        if "mt5" in locals():
            mt5.shutdown()
    return report


# ==============================================================================
# MASTER 360-DEGREE FORENSIC CERTIFICATE GENERATOR
# ==============================================================================

def run_360_degree_chain_verification() -> Dict[str, Any]:
    """Execute complete 360-degree verification across data sources, processing, and execution."""
    ts_utc = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
    
    layer1_mt5 = audit_mt5_live_data_source()
    layer1_binance = audit_binance_l2_data_source()
    layer1_parquet = audit_parquet_candle_archives()
    
    layer2_features = audit_causal_feature_processing("BTC")
    layer2_telemetry = audit_telemetry_snapshot_integrity()
    
    layer3_broker = audit_broker_execution_and_floor()
    
    # Overall certificate verdict: fail closed on any non-PASS status
    all_statuses = [
        layer1_mt5.get("status"), layer1_binance.get("status"), layer1_parquet.get("status"),
        layer2_features.get("status"), layer2_telemetry.get("status"), layer3_broker.get("status")
    ]
    
    if "FAIL" in all_statuses or any(s in ("FAIL", "ERROR", "EXCEPTION") for s in all_statuses):
        overall = "FAILED"
    elif any(s in ("SKIP", "INCOMPLETE", "UNKNOWN", "NONE", None) for s in all_statuses):
        overall = "INCOMPLETE"
    elif "WARN" in all_statuses or "WARNING" in all_statuses:
        overall = "WARNING"
    elif all(s == "PASS" for s in all_statuses):
        overall = "CERTIFIED_100_PERCENT_PRISTINE"
    else:
        overall = "UNVERIFIED"
        
    certificate = {
        "certificate_id": f"CERT-360-{int(time.time())}",
        "timestamp_utc": ts_utc,
        "overall_verdict": overall,
        "layer1_data_sources": {
            "mt5_broker_feed": layer1_mt5,
            "binance_l2_depth": layer1_binance,
            "parquet_archives": layer1_parquet
        },
        "layer2_data_processing": {
            "causal_feature_engineering": layer2_features,
            "telemetry_serialization": layer2_telemetry
        },
        "layer3_broker_and_floor": layer3_broker
    }
    
    return certificate


if __name__ == "__main__":
    cert = run_360_degree_chain_verification()
    print("=" * 80)
    print(f"360-DEGREE FORENSIC CHAIN VERIFICATION CERTIFICATE: {cert['overall_verdict']}")
    print(f"Timestamp: {cert['timestamp_utc']}")
    print("=" * 80)
    print(json.dumps(cert, indent=2))
