"""
Terminal/Candle_Indicator_Engine.py
===================================
Institutional Historical Candle Persistence, Gap-Detection & Indicator Engine.

Key Responsibilities:
1. Persists completed 15m OHLCV candles to Data/Candles/{ASSET}_15m.parquet.
2. Performs gap audits: detects missing candles, non-monotonic timestamps, and weekend/session halts.
3. Computes deterministic causal indicators:
   - True Daily Session VWAP (resets 00:00 UTC) with +/-1, +/-2, +/-3 SD bands and vwap_z.
   - Rolling 24h VWAP (96-bar window) with continuous volatility bands.
   - EMA 20, EMA 50, EMA 200 and 3-hour slope.
   - ATR(14) and Wilder RSI(14).
4. Mean-Reversion Scanner: Identifies extreme deviations (>= +2 SD or <= -2 SD from VWAP)
   for Gold, Silver, and Institutional Crypto Perpetuals.
"""
from __future__ import annotations

import argparse
import math
import pathlib
import sys
import time
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from typing import Any, Dict, List, Optional, Tuple

import numpy as np
import pandas as pd

ROOT = pathlib.Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from Terminal.Asset_Universe import UNIVERSE, EXTENDED_UNIVERSE, canonical_asset
from Terminal.MT5_Execution_Bridge import MT5ExecutionBridge
from Terminal.risk.fail_closed import bar_fresh, num

CANDLE_DIR = ROOT / "Data" / "Candles"
CANDLE_DIR.mkdir(parents=True, exist_ok=True)

try:
    import numba

    @numba.njit(fastmath=True, cache=True)
    def _calc_ema_series_numba(arr: np.ndarray, period: int) -> np.ndarray:
        n = len(arr)
        out = np.empty(n, dtype=np.float64)
        if n < period or period <= 0:
            out[:] = np.nan
            return out
        out[:period - 1] = np.nan
        sma = 0.0
        for i in range(period):
            sma += arr[i]
        sma /= period
        out[period - 1] = sma
        alpha = 2.0 / (period + 1.0)
        one_minus_alpha = 1.0 - alpha
        for i in range(period, n):
            out[i] = alpha * arr[i] + one_minus_alpha * out[i - 1]
        return out

    @numba.njit(fastmath=True, cache=True)
    def _calc_ema_ribbon_numba(arr: np.ndarray, periods: np.ndarray) -> np.ndarray:
        n = len(arr)
        num_p = len(periods)
        out = np.empty((num_p, n), dtype=np.float64)
        for p_idx in range(num_p):
            p = periods[p_idx]
            if n < p or p <= 0:
                out[p_idx, :] = np.nan
                continue
            out[p_idx, :p - 1] = np.nan
            sma = 0.0
            for i in range(p):
                sma += arr[i]
            sma /= p
            out[p_idx, p - 1] = sma
            alpha = 2.0 / (p + 1.0)
            one_minus_alpha = 1.0 - alpha
            for i in range(p, n):
                out[p_idx, i] = alpha * arr[i] + one_minus_alpha * out[p_idx, i - 1]
        return out

    NUMBA_AVAILABLE = True
except Exception:
    NUMBA_AVAILABLE = False


def _calc_ema_series_numpy(arr: np.ndarray, period: int) -> np.ndarray:
    n = len(arr)
    out = np.full(n, np.nan, dtype=np.float64)
    if n < period or period <= 0:
        return out
    sma = float(np.mean(arr[:period]))
    out[period - 1] = sma
    alpha = 2.0 / (period + 1.0)
    one_minus = 1.0 - alpha
    prev = sma
    for i in range(period, n):
        prev = alpha * arr[i] + one_minus * prev
        out[i] = prev
    return out


def calc_ema_series(arr: np.ndarray, period: int) -> np.ndarray:
    """Institutional SMA-seeded Exponential Moving Average full series."""
    arr_c = np.ascontiguousarray(arr, dtype=np.float64)
    if NUMBA_AVAILABLE:
        return _calc_ema_series_numba(arr_c, period)
    return _calc_ema_series_numpy(arr_c, period)


SUPERSET_EMA_PERIODS: Tuple[int, ...] = (5, 9, 13, 20, 34, 50, 89, 100, 144, 200, 233)
FIB_EMA_PERIODS: Tuple[int, ...] = (5, 13, 34, 89, 144, 233)


def calc_ema_ribbon(arr: np.ndarray, periods: Tuple[int, ...] = SUPERSET_EMA_PERIODS) -> Dict[int, np.ndarray]:
    """Computes multi-timeframe Fibonacci Prime & Superset EMA ribbon series with institutional SMA seeding in a single pass."""
    arr_c = np.ascontiguousarray(arr, dtype=np.float64)
    if NUMBA_AVAILABLE:
        p_arr = np.array(periods, dtype=np.int64)
        matrix = _calc_ema_ribbon_numba(arr_c, p_arr)
        return {p: matrix[idx] for idx, p in enumerate(periods)}
    return {p: _calc_ema_series_numpy(arr_c, p) for p in periods}


def calc_ema(arr: np.ndarray, period: int) -> Optional[float]:
    """Returns latest institutional SMA-seeded EMA value, or None if insufficient bars."""
    if len(arr) < period or period <= 0:
        return None
    s = calc_ema_series(arr, period)
    val = s[-1]
    return float(val) if not np.isnan(val) else None


def classify_ema_ribbon(
    price: float,
    ema_5: Optional[float] = None,
    ema_13: Optional[float] = None,
    ema_34: Optional[float] = None,
    ema_89: Optional[float] = None,
    ema_144: Optional[float] = None,
    ema_233: Optional[float] = None,
    *,
    slope_34: Optional[float] = None,
    slope_233: Optional[float] = None,
    ema_9: Optional[float] = None,
    ema_20: Optional[float] = None,
    ema_50: Optional[float] = None,
    ema_100: Optional[float] = None,
    ema_200: Optional[float] = None,
    **kwargs,
) -> Tuple[str, Optional[float]]:
    """
    Classifies structural alignment of the multi-timeframe Fibonacci Prime EMA ribbon:
    (5, 13, 34, 89, 144, 233) with O(1) slope validation and full legacy fallback.
    """
    # 1. Modern 6-tier Fibonacci Prime stack
    if ema_5 and ema_13 and ema_34 and ema_89 and ema_144 and ema_233:
        spread_pct = ((ema_13 - ema_233) / ema_233) * 100.0 if ema_233 > 0 else 0.0

        is_bull_stack = ema_5 > ema_13 > ema_34 > ema_89 > ema_144 > ema_233
        is_bear_stack = ema_5 < ema_13 < ema_34 < ema_89 < ema_144 < ema_233
        macro_bull = ema_34 > ema_89 > ema_144 > ema_233 and (slope_233 is None or slope_233 >= 0)
        macro_bear = ema_34 < ema_89 < ema_144 < ema_233 and (slope_233 is None or slope_233 <= 0)

        if price > ema_5 and is_bull_stack and (slope_233 is None or slope_233 > 0):
            return "PERFECT_BULLISH", spread_pct
        elif macro_bull and (price < ema_5 or price < ema_13):
            return "PULLBACK_IN_BULL", spread_pct
        elif is_bull_stack:
            return "BULLISH_ALIGNMENT", spread_pct
        elif price < ema_5 and is_bear_stack and (slope_233 is None or slope_233 < 0):
            return "PERFECT_BEARISH", spread_pct
        elif macro_bear and (price > ema_5 or price > ema_13):
            return "PULLBACK_IN_BEAR", spread_pct
        elif is_bear_stack:
            return "BEARISH_ALIGNMENT", spread_pct
        else:
            return "COMPRESSING_NEUTRAL", spread_pct

    # 2. Legacy fallback
    e20 = ema_20 or ema_13
    e50 = ema_50 or ema_34
    e200 = ema_200 or ema_233
    e9 = ema_9 or ema_5 or price
    if not (e20 and e50 and e200):
        return "INSUFFICIENT_DATA", None

    spread_pct = ((e20 - e200) / e200) * 100.0 if e200 > 0 else 0.0
    if price > e9 > e20 > e50 > e200:
        return "PERFECT_BULLISH", spread_pct
    elif e20 > e50 > e200 and price < e9:
        return "PULLBACK_IN_BULL", spread_pct
    elif e20 > e50 > e200:
        return "BULLISH_ALIGNMENT", spread_pct
    elif price < e9 < e20 < e50 < e200:
        return "PERFECT_BEARISH", spread_pct
    elif e20 < e50 < e200 and price > e9:
        return "PULLBACK_IN_BEAR", spread_pct
    elif e20 < e50 < e200:
        return "BEARISH_ALIGNMENT", spread_pct
    else:
        return "COMPRESSING_NEUTRAL", spread_pct


class CandleIndicatorEngine:
    calc_ema = staticmethod(calc_ema)
    calc_ema_series = staticmethod(calc_ema_series)
    calc_ema_ribbon = staticmethod(calc_ema_ribbon)
    classify_ema_ribbon = staticmethod(classify_ema_ribbon)
    def __init__(
        self,
        bridge: Optional[MT5ExecutionBridge] = None,
        storage_dir: pathlib.Path = CANDLE_DIR,
        universe: Tuple[str, ...] = UNIVERSE,
    ):
        self.bridge = bridge or MT5ExecutionBridge(5064568)
        self.storage_dir = pathlib.Path(storage_dir)
        self.storage_dir.mkdir(parents=True, exist_ok=True)
        self.universe = list(universe)
        self.cache: Dict[str, List[Dict[str, Any]]] = {}

    def sync_candles(self, asset: str, count: int = 800) -> Dict[str, Any]:
        """Fetch completed 15m bars from MT5, audit gaps, persist to disk."""
        asset = canonical_asset(asset)
        symbol = self.bridge.resolve_symbol(asset)
        if not symbol:
            return {"asset": asset, "success": False, "error": f"Symbol unresolved for {asset}"}

        bars = self.bridge.get_recent_bars(symbol, count=count)
        if not bars:
            return {"asset": asset, "success": False, "error": "No bars returned by broker"}

        # Sort chronologically by open time
        ordered = sorted(bars, key=lambda b: float(b.get("time", 0.0)))

        # Gap detection & sanity audit
        times = [float(b["time"]) for b in ordered]
        gaps: List[Dict[str, Any]] = []
        for i in range(1, len(times)):
            delta = times[i] - times[i - 1]
            if delta > 900.0:
                missing_bars = int(round((delta - 900.0) / 900.0))
                gaps.append({
                    "start_utc": datetime.fromtimestamp(times[i - 1], tz=timezone.utc).strftime("%Y-%m-%d %H:%M"),
                    "end_utc": datetime.fromtimestamp(times[i], tz=timezone.utc).strftime("%Y-%m-%d %H:%M"),
                    "delta_seconds": int(delta),
                    "missing_bars": missing_bars,
                })

        # Save to disk as Parquet for durable historical cache
        df = pd.DataFrame(ordered)
        now_utc = datetime.now(timezone.utc).timestamp()
        offset_sec = 0
        if times:
            diff = times[-1] - now_utc
            if abs(diff) < 86400 * 3 and diff > 1800:
                offset_sec = int(round(diff / 3600.0) * 3600)
        df["utc_time"] = df["time"] - offset_sec
        df["datetime_utc"] = pd.to_datetime(df["utc_time"], unit="s", utc=True)
        parquet_file = self.storage_dir / f"{asset}_15m.parquet"
        df.to_parquet(parquet_file, index=False)

        self.cache[asset] = ordered
        indicators = self.compute_indicators(ordered)

        return {
            "asset": asset,
            "symbol": symbol,
            "success": True,
            "bar_count": len(ordered),
            "first_bar_utc": datetime.fromtimestamp(times[0], tz=timezone.utc).strftime("%Y-%m-%d %H:%M"),
            "latest_bar_utc": datetime.fromtimestamp(times[-1], tz=timezone.utc).strftime("%Y-%m-%d %H:%M"),
            "latest_close": ordered[-1]["close"],
            "gap_count": len(gaps),
            "gaps": gaps[-5:],  # Last 5 gaps if any (e.g. weekend closures on Gold/Silver)
            "indicators": indicators,
        }

    def sync_all(self, count: int = 512, max_workers: int = 6) -> Dict[str, Dict[str, Any]]:
        """Sync all assets in the universe concurrently."""
        results: Dict[str, Dict[str, Any]] = {}
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            future_to_asset = {
                executor.submit(self.sync_candles, asset, count): asset for asset in self.universe
            }
            for future in future_to_asset:
                asset = future_to_asset[future]
                try:
                    results[asset] = future.result()
                except Exception as exc:
                    results[asset] = {"asset": asset, "success": False, "error": str(exc)}
        return results

    @staticmethod
    def compute_indicators(bars: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Compute Session VWAP, Rolling VWAP, EMAs, ATR, RSI from historical bars."""
        if len(bars) < 14:
            return {}

        closes = np.array([float(b["close"]) for b in bars])
        highs = np.array([float(b["high"]) for b in bars])
        lows = np.array([float(b["low"]) for b in bars])
        times = np.array([float(b["time"]) for b in bars])
        volumes = np.array([float(b.get("real_volume") or b.get("volume") or b.get("tick_volume") or 0.0) for b in bars])

        # Typical price
        tps = (highs + lows + closes) / 3.0
        last_price = closes[-1]
        now_ts = times[-1] + 900.0  # Close of latest bar

        # Clean volume resolution (prioritize real volume, fall back to tick volume, strict float)
        vols_list = []
        for b in bars:
            rv = num(b.get("real_volume"))
            v = num(b.get("volume"))
            tv = num(b.get("tick_volume"))
            chosen = rv if (rv is not None and rv > 0) else (v if (v is not None and v > 0) else (tv if (tv is not None and tv > 0) else 0.0))
            vols_list.append(max(float(chosen), 0.0))
        volumes = np.array(vols_list)

        # -------------------------------------------------------------
        # 1. Daily Session VWAP (Anchored strictly to 00:00:00 UTC)
        # -------------------------------------------------------------
        now_utc = datetime.now(timezone.utc).timestamp()
        offset_sec = 0
        if len(times) > 0:
            diff = times[-1] - now_utc
            if abs(diff) < 86400 * 3 and diff > 1800:
                offset_sec = int(round(diff / 3600.0) * 3600)

        utc_times = times - offset_sec
        latest_dt = datetime.fromtimestamp(utc_times[-1], tz=timezone.utc)
        session_start_ts = datetime(
            latest_dt.year, latest_dt.month, latest_dt.day, 0, 0, 0, tzinfo=timezone.utc
        ).timestamp()

        session_mask = utc_times >= session_start_ts
        if np.sum(session_mask) >= 3 and np.sum(volumes[session_mask]) > 0:
            s_tps = tps[session_mask]
            s_vols = volumes[session_mask]
            s_cum_vol = np.sum(s_vols)
            s_vwap = np.sum(s_tps * s_vols) / max(s_cum_vol, 1e-9)
            s_var = np.sum(s_vols * ((s_tps - s_vwap) ** 2)) / max(s_cum_vol, 1e-9)
            s_sigma = math.sqrt(max(0.0, s_var))
            s_bars_count = int(np.sum(session_mask))
        else:
            # Fall back to rolling 96 bars if early in session (< 1h)
            s_vwap = None
            s_sigma = None
            s_bars_count = 0

        # -------------------------------------------------------------
        # 2. Rolling 24-Hour VWAP (96 bars lookback)
        # -------------------------------------------------------------
        r_window = min(len(bars), 96)
        r_tps = tps[-r_window:]
        r_vols = volumes[-r_window:]
        r_cum_vol = np.sum(r_vols)
        if r_cum_vol > 0:
            r_vwap = np.sum(r_tps * r_vols) / r_cum_vol
            r_var = np.sum(r_vols * ((r_tps - r_vwap) ** 2)) / r_cum_vol
            r_sigma = math.sqrt(max(0.0, r_var))
        else:
            r_vwap = r_sigma = None

        # Price-only bars never masquerade as volume-weighted observations.
        primary_vwap = s_vwap if (s_vwap is not None and s_bars_count >= 8) else r_vwap
        primary_sigma = s_sigma if (s_sigma is not None and s_bars_count >= 8) else r_sigma
        vwap_z = ((last_price - primary_vwap) / primary_sigma
                  if primary_vwap is not None and primary_sigma and primary_sigma > 1e-8 else None)
        upper_1 = primary_vwap + primary_sigma if primary_vwap is not None and primary_sigma is not None else None
        lower_1 = primary_vwap - primary_sigma if primary_vwap is not None and primary_sigma is not None else None
        upper_2 = primary_vwap + 2.0 * primary_sigma if upper_1 is not None else None
        lower_2 = primary_vwap - 2.0 * primary_sigma if lower_1 is not None else None
        upper_3 = primary_vwap + 3.0 * primary_sigma if upper_1 is not None else None
        lower_3 = primary_vwap - 3.0 * primary_sigma if lower_1 is not None else None

        # -------------------------------------------------------------
        # 3. Vectorized Superset & Fibonacci Prime EMA Ribbon (5, 9, 13, 20, 34, 50, 89, 100, 144, 200, 233)
        # -------------------------------------------------------------
        ribbon = calc_ema_ribbon(closes, SUPERSET_EMA_PERIODS)
        
        # Fibonacci Prime & Sequence EMAs
        ema_5 = float(ribbon[5][-1]) if len(closes) >= 5 and not np.isnan(ribbon[5][-1]) else None
        ema_13 = float(ribbon[13][-1]) if len(closes) >= 13 and not np.isnan(ribbon[13][-1]) else None
        ema_34 = float(ribbon[34][-1]) if len(closes) >= 34 and not np.isnan(ribbon[34][-1]) else None
        ema_89 = float(ribbon[89][-1]) if len(closes) >= 89 and not np.isnan(ribbon[89][-1]) else None
        ema_144 = float(ribbon[144][-1]) if len(closes) >= 144 and not np.isnan(ribbon[144][-1]) else None
        ema_233 = float(ribbon[233][-1]) if len(closes) >= 233 and not np.isnan(ribbon[233][-1]) else None

        # Legacy EMAs (Zero-regression compatibility)
        ema_9 = float(ribbon[9][-1]) if len(closes) >= 9 and not np.isnan(ribbon[9][-1]) else None
        ema_20 = float(ribbon[20][-1]) if len(closes) >= 20 and not np.isnan(ribbon[20][-1]) else None
        ema_50 = float(ribbon[50][-1]) if len(closes) >= 50 and not np.isnan(ribbon[50][-1]) else None
        ema_100 = float(ribbon[100][-1]) if len(closes) >= 100 and not np.isnan(ribbon[100][-1]) else None
        ema_200 = float(ribbon[200][-1]) if len(closes) >= 200 and not np.isnan(ribbon[200][-1]) else None

        # O(1) Slope Calculations:
        s233 = ribbon[233]
        ema_233_slope_pct = ((ema_233 - float(s233[-13])) / float(s233[-13]) * 100.0
                             if len(closes) >= 246 and ema_233 is not None and not np.isnan(s233[-13]) and s233[-13] > 0 else None)

        s34 = ribbon[34]
        ema_34_slope_pct = ((ema_34 - float(s34[-5])) / float(s34[-5]) * 100.0
                            if len(closes) >= 39 and ema_34 is not None and not np.isnan(s34[-5]) and s34[-5] > 0 else None)

        s13 = ribbon[13]
        ema_13_slope_pct = ((ema_13 - float(s13[-5])) / float(s13[-5]) * 100.0
                            if len(closes) >= 18 and ema_13 is not None and not np.isnan(s13[-5]) and s13[-5] > 0 else None)

        # Legacy slopes
        s200 = ribbon[200]
        ema_200_slope_pct = ((ema_200 - float(s200[-13])) / float(s200[-13]) * 100.0
                             if len(closes) >= 212 and ema_200 is not None and not np.isnan(s200[-13]) and s200[-13] > 0 else None)

        s50 = ribbon[50]
        ema_50_slope_pct = ((ema_50 - float(s50[-9])) / float(s50[-9]) * 100.0
                            if len(closes) >= 58 and ema_50 is not None and not np.isnan(s50[-9]) and s50[-9] > 0 else None)

        s20 = ribbon[20]
        ema_20_slope_pct = ((ema_20 - float(s20[-5])) / float(s20[-5]) * 100.0
                            if len(closes) >= 24 and ema_20 is not None and not np.isnan(s20[-5]) and s20[-5] > 0 else None)

        ribbon_state, ribbon_spread_pct = classify_ema_ribbon(
            last_price, ema_5=ema_5, ema_13=ema_13, ema_34=ema_34, ema_89=ema_89, ema_144=ema_144, ema_233=ema_233,
            slope_34=ema_34_slope_pct, slope_233=ema_233_slope_pct,
            ema_9=ema_9, ema_20=ema_20, ema_50=ema_50, ema_100=ema_100, ema_200=ema_200
        )

        # -------------------------------------------------------------
        # 4. Wilder Average True Range (ATR 14)
        # -------------------------------------------------------------
        tr = [highs[0] - lows[0]]
        for i in range(1, len(bars)):
            tr.append(max(highs[i] - lows[i], abs(highs[i] - closes[i - 1]), abs(lows[i] - closes[i - 1])))
        if len(tr) >= 14:
            atr = float(np.mean(tr[:14]))
            for i in range(14, len(tr)):
                atr = (atr * 13.0 + tr[i]) / 14.0
            atr_14 = float(atr)
        else:
            atr_14 = float(np.mean(tr))

        # -------------------------------------------------------------
        # 5. Wilder RSI (14)
        # -------------------------------------------------------------
        diffs = np.diff(closes)
        gains = np.maximum(diffs, 0.0)
        losses = np.maximum(-diffs, 0.0)
        if len(gains) >= 14:
            avg_gain = float(np.mean(gains[:14]))
            avg_loss = float(np.mean(losses[:14]))
            for i in range(14, len(gains)):
                avg_gain = (avg_gain * 13.0 + gains[i]) / 14.0
                avg_loss = (avg_loss * 13.0 + losses[i]) / 14.0
            rs = avg_gain / max(avg_loss, 1e-12)
            rsi_14 = 100.0 - (100.0 / (1.0 + rs))
        else:
            rsi_14 = None  # 14 deltas need at least 15 observed closes

        # -------------------------------------------------------------
        # 6. Swing Extremes (24h / 96 bars)
        # -------------------------------------------------------------
        h24 = float(np.max(highs[-96:]))
        l24 = float(np.min(lows[-96:]))

        return {
            "last_price": float(last_price),
            "session_vwap": float(s_vwap) if s_vwap else None,
            "session_sigma": float(s_sigma) if s_sigma else None,
            "session_bars": s_bars_count,
            "rolling_vwap_24h": float(r_vwap) if r_vwap is not None else None,
            "rolling_sigma_24h": float(r_sigma) if r_sigma is not None else None,
            "active_vwap": float(primary_vwap) if primary_vwap is not None else None,
            "active_sigma": float(primary_sigma) if primary_sigma is not None else None,
            "vwap_z": float(vwap_z) if vwap_z is not None else None,
            "upper_1sd": float(upper_1) if upper_1 is not None else None,
            "lower_1sd": float(lower_1) if lower_1 is not None else None,
            "upper_2sd": float(upper_2) if upper_2 is not None else None,
            "lower_2sd": float(lower_2) if lower_2 is not None else None,
            "upper_3sd": float(upper_3) if upper_3 is not None else None,
            "lower_3sd": float(lower_3) if lower_3 is not None else None,
            "ema_5": float(ema_5) if ema_5 is not None else None,
            "ema_13": float(ema_13) if ema_13 is not None else None,
            "ema_34": float(ema_34) if ema_34 is not None else None,
            "ema_89": float(ema_89) if ema_89 is not None else None,
            "ema_144": float(ema_144) if ema_144 is not None else None,
            "ema_233": float(ema_233) if ema_233 is not None else None,
            "ema_13_slope_pct": float(ema_13_slope_pct) if ema_13_slope_pct is not None else None,
            "ema_34_slope_pct": float(ema_34_slope_pct) if ema_34_slope_pct is not None else None,
            "ema_233_slope_pct": float(ema_233_slope_pct) if ema_233_slope_pct is not None else None,
            "ema_9": float(ema_9) if ema_9 is not None else None,
            "ema_20": float(ema_20) if ema_20 is not None else None,
            "ema_50": float(ema_50) if ema_50 is not None else None,
            "ema_100": float(ema_100) if ema_100 is not None else None,
            "ema_200": float(ema_200) if ema_200 is not None else None,
            "ema_20_slope_pct": float(ema_20_slope_pct) if ema_20_slope_pct is not None else None,
            "ema_50_slope_pct": float(ema_50_slope_pct) if ema_50_slope_pct is not None else None,
            "ema_200_slope_pct": float(ema_200_slope_pct) if ema_200_slope_pct is not None else None,
            "ema_ribbon_state": ribbon_state,
            "ema_ribbon_spread_pct": float(ribbon_spread_pct) if ribbon_spread_pct is not None else None,
            "atr_14": float(atr_14),
            "atr_pct": float(atr_14 / last_price * 100.0),
            "rsi_14": float(rsi_14) if rsi_14 is not None else None,
            "high_24h": h24,
            "low_24h": l24,
        }

    def scan_vwap_opportunities(self, z_threshold: float = 1.75) -> List[Dict[str, Any]]:
        """Identify assets stretched beyond +/- 2 SD from VWAP."""
        if not self.cache:
            self.sync_all()

        opportunities = []
        for asset, bars in self.cache.items():
            if not bars:
                continue
            ind = self.compute_indicators(bars)
            if not ind or ind.get("vwap_z") is None or ind.get("rsi_14") is None:
                continue

            z = ind["vwap_z"]
            px = ind["last_price"]
            vwap = ind["active_vwap"]
            sigma = ind["active_sigma"]
            atr = ind["atr_14"]
            rsi = ind["rsi_14"]

            # Extreme Overbought (>= +1.75 SD, target mean reversion SHORT)
            if z >= z_threshold:
                dist_pct = (px - vwap) / vwap * 100.0
                opp = {
                    "asset": asset,
                    "direction": "SHORT",
                    "bias": "EXTREME_OVERBOUGHT",
                    "current_price": px,
                    "vwap": vwap,
                    "upper_2sd": ind["upper_2sd"],
                    "vwap_z": round(z, 2),
                    "dist_to_vwap_pct": round(dist_pct, 2),
                    "rsi_14": round(rsi, 1),
                    "atr_14": round(atr, 4),
                    "suggested_sl": round(px + 1.5 * atr, 4),
                    "suggested_tp": round(vwap, 4),
                    "potential_r": round((px - vwap) / (1.5 * atr), 2) if atr > 0 else 0.0,
                    "confluence": "Look for Ask Whale Walls + Long Squeeze Sweeps",
                }
                opportunities.append(opp)

            # Extreme Oversold (<= -1.75 SD, target mean reversion LONG)
            elif z <= -z_threshold:
                dist_pct = (vwap - px) / vwap * 100.0
                opp = {
                    "asset": asset,
                    "direction": "LONG",
                    "bias": "EXTREME_OVERSOLD",
                    "current_price": px,
                    "vwap": vwap,
                    "lower_2sd": ind["lower_2sd"],
                    "vwap_z": round(z, 2),
                    "dist_to_vwap_pct": round(dist_pct, 2),
                    "rsi_14": round(rsi, 1),
                    "atr_14": round(atr, 4),
                    "suggested_sl": round(px - 1.5 * atr, 4),
                    "suggested_tp": round(vwap, 4),
                    "potential_r": round((vwap - px) / (1.5 * atr), 2) if atr > 0 else 0.0,
                    "confluence": "Look for Bid Whale Walls + Short Squeeze Sweeps",
                }
                opportunities.append(opp)

        # Sort by absolute deviation magnitude
        opportunities.sort(key=lambda x: abs(x["vwap_z"]), reverse=True)
        return opportunities


def main():
    parser = argparse.ArgumentParser(description="Candle Persistence & Indicator Engine")
    parser.add_argument("--sync", action="store_true", help="Sync all candles from MT5")
    parser.add_argument("--scan", action="store_true", help="Scan for VWAP 2 SD opportunities")
    parser.add_argument("--extended", action="store_true", help="Scan full 24-asset extended universe")
    parser.add_argument("--asset", type=str, default=None, help="Inspect specific asset")
    args = parser.parse_args()

    active_uni = EXTENDED_UNIVERSE if args.extended else UNIVERSE
    engine = CandleIndicatorEngine(universe=active_uni)

    if args.asset:
        res = engine.sync_candles(args.asset)
        print(f"\n=== CANDLE AUDIT FOR {args.asset} ===")
        print(f"Symbol: {res.get('symbol')} | Bars: {res.get('bar_count')} | Latest Close: {res.get('latest_close')}")
        print(f"Range: {res.get('first_bar_utc')} -> {res.get('latest_bar_utc')} UTC")
        print(f"Gaps Detected: {res.get('gap_count')}")
        if res.get("gaps"):
            for g in res["gaps"]:
                print(f"  Gap: {g['start_utc']} to {g['end_utc']} ({g['missing_bars']} bars)")
        ind = res.get("indicators", {})
        print("\n--- INDICATORS ---")
        print(f"Price: {ind.get('last_price')} | VWAP: {ind.get('active_vwap'):.2f} (Z: {ind.get('vwap_z'):.2f} SD)")
        print(f"Bands: Lower 2 SD = {ind.get('lower_2sd'):.2f} | Upper 2 SD = {ind.get('upper_2sd'):.2f}")
        print(f"EMA 200: {ind.get('ema_200'):.2f} (Slope: {ind.get('ema_200_slope_pct'):.3f}%) | RSI: {ind.get('rsi_14'):.1f} | ATR: {ind.get('atr_14'):.2f}")
        return

    print("\n[SYNC] Fetching and auditing completed 15m candles across universe...")
    t0 = time.time()
    results = engine.sync_all()
    t1 = time.time()
    print(f"[OK] Synced {len(results)} assets in {(t1 - t0):.2f}s.\n")

    print(f"{'Asset':<8} {'Price':<10} {'VWAP':<10} {'VWAP Z':<8} {'Upper 2SD':<10} {'Lower 2SD':<10} {'RSI':<6} {'Bars':<6} {'Gaps':<5}")
    print("-" * 80)
    for asset, r in results.items():
        if not r.get("success"):
            print(f"{asset:<8} ERROR: {r.get('error')}")
            continue
        ind = r.get("indicators", {})
        px = ind.get("last_price", 0.0)
        vwap = ind.get("active_vwap", 0.0)
        z = ind.get("vwap_z", 0.0)
        u2 = ind.get("upper_2sd", 0.0)
        l2 = ind.get("lower_2sd", 0.0)
        rsi = ind.get("rsi_14", 50.0)
        bars = r.get("bar_count", 0)
        gaps = r.get("gap_count", 0)
        print(f"{asset:<8} {px:<10.2f} {vwap:<10.2f} {z:<8.2f} {u2:<10.2f} {l2:<10.2f} {rsi:<6.1f} {bars:<6} {gaps:<5}")

    print("\n[SCAN] Scanning for extreme VWAP extensions (|Z| >= 1.75 SD)...")
    opps = engine.scan_vwap_opportunities()
    if not opps:
        print("No assets currently stretched beyond +/- 1.75 SD from VWAP.")
    else:
        print(f"Found {len(opps)} extreme VWAP opportunities:\n")
        for op in opps:
            print(f"  * {op['asset']} {op['direction']} ({op['bias']}):")
            print(f"    Current: {op['current_price']} | VWAP: {op['vwap']:.2f} | Z-Score: {op['vwap_z']} SD")
            print(f"    Suggested SL: {op['suggested_sl']} | Suggested TP: {op['suggested_tp']} | R:R: +{op['potential_r']}R")
            print(f"    Notes: {op['confluence']}\n")


if __name__ == "__main__":
    main()
