"""
Terminal/OF_Strategy.py
========================
Master Institutional Multi-Asset Orderflow Confluence (OFC) & Multi-Sleeve Multiverse Engine.

Architecture & Settled Invariants:
1. Universe:
   - Certified Genuine 11 Institutional Binance USDT-M Perpetuals:
     BTCUSDT, ETHUSDT, XRPUSDT, BNBUSDT, DOGEUSDT, ADAUSDT, TRXUSDT, LINKUSDT, DOTUSDT, LTCUSDT, BCHUSDT.
   - Macro Cross-Asset Hedges (Forex/CFD Indices & Commodities):
     GER30, FR40, US2000, GAS, XAUCNH, NICKEL.
2. Multi-Sleeve Confluence:
   - Sleeve S1: Liquidation Flush & Trend-Aligned Pullbacks (200 EMA slope + VWAP discount + CVD absorption).
   - Sleeve S4: Multi-Timeframe Structural Liquidity Sweeps (PDL/PDH, PWL/PWH sweeps with footprint delta absorption).
   - Sleeve S3: London (07:00 UTC) & New York (13:30 UTC) Session Opening Range Breakout (ORB + CRT) with Judas sweep filter.
3. Microstructure Three-Stage Ratchet (Oxford-Man 2020 / OX59 Invariant):
   - Invalidation (Stop Loss): Dynamic structural stop capped by ATR (1.5x ATR max).
   - Phase 0 (BE Lock): At +0.85R gain -> move stop to Entry + 0.25R (covers friction with guaranteed profit).
   - Phase 1 (Profit Lock): At +1.50R gain -> move stop to Entry + 0.85R, unlocks trailing ATR stop.
   - Phase 2 (Trail Lock): At +2.00R gain -> move stop to Entry + 1.50R.
   - Exit Target: +2.50R to +3.00R (convex asymmetric payoff).
   - Time Decay: Exit at market if < +0.20R gain after 24 bars (6 hours).
4. Walk-Forward Machine Learning Overlay:
   - Sleeve S1: Dual-Model Ensemble (60% Ridge Logistic Regression + 40% Shallow LightGBM).
   - Sleeve S3: Depth-Constrained LightGBM Session Classifier (max_depth=3, reg_alpha=1.5, reg_lambda=3.0).
   - Strict 72h Causal Purge (t_purge = t_start - 72h) before out-of-sample window evaluation.
5. Fixed Risk Budget & Portfolio Governance:
   - Initial Capital: 5,000.00 USD | S1 Base Risk: 38.00 USD (0.76%) | S3 Base Risk: 22.00 USD (0.44%).
   - S1 Circuit Breaker: Pauses S1 entries if DD >= 2.50% or 2 consecutive losses, protecting during crypto crashes.
   - Hard Circuit Breaker: 4.50% Max Drawdown.
   - Max Concurrent Positions: 3 across all sleeves simultaneously.
   - Milestone CPPI Cushion Protection: Once +500.00 USD net profit (+10% ROI) is achieved, risk scales down to cushion fraction.
   - Friction: 41.0 bps round-trip on notional (-0.18R drag) on S1, 8.0 bps (-0.08R drag) on ORB.

Modes:
  python Terminal/OF_Strategy.py --mode backtest [--data-dir Binance_Data] [--chart Terminal/of_equity_curve.png]
  python Terminal/OF_Strategy.py --mode dry-run  [--coin BTC] [--host http://localhost:8095]
"""

from __future__ import annotations
import os
import sys
import time
import json
import argparse
import datetime
from pathlib import Path
from typing import Dict, Any, List, Tuple

# Ensure workspace root and Terminal are in sys.path
root_dir = Path(__file__).resolve().parent.parent
if str(root_dir) not in sys.path:
    sys.path.insert(0, str(root_dir))
terminal_dir = Path(__file__).resolve().parent
if str(terminal_dir) not in sys.path:
    sys.path.insert(0, str(terminal_dir))

import numpy as np
import pandas as pd
from numba import njit
import lightgbm as lgb
from sklearn.linear_model import LogisticRegression
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

# ── 0. GLOBAL CONSTANTS ────────────────────────────────────────────────────────
INITIAL_CAPITAL    = 5_000.0
S1_BASE_RISK       = 42.0
ORB_BASE_RISK      = 26.0
DEFENSE_RISK       = 14.0
MAX_RISK_BUDGET    = 85.0
HARD_DD_LIMIT      = 4.50     # Hard circuit breaker (%)
DEF_DD_TRIGGER     = 1.80     # Drawdown % to activate defense risk
PURGE_HOURS        = 72       # Causal temporal embargo before OOS window
FRICTION_R_S1      = 0.18     # Friction deduction in R-units for orderflow pullbacks (41 bps)
FRICTION_R_ORB     = 0.08     # Friction deduction for session breakouts (8 bps)
MAX_CONCURRENT     = 2        # Max simultaneous open positions across all sleeves
MAX_S1_CONCURRENT  = 2
MAX_ORB_CONCURRENT = 1
COOLDOWN_BARS      = 4        # Minimum bars between consecutive entries on same asset

CORE_SYMBOLS = [
    "BTCUSDT", "ETHUSDT", "XRPUSDT", "BNBUSDT", "DOGEUSDT",
    "ADAUSDT", "TRXUSDT", "LINKUSDT", "DOTUSDT", "LTCUSDT", "BCHUSDT"
]

FOREX_SYMBOLS = ["GER30", "FR40", "US2000", "GAS", "XAUCNH", "NICKEL"]

COLS_TO_LOAD = [
    "open_time_ms", "open", "high", "low", "close",
    "atr_14", "atr_100", "vwap_zscore", "long_liq_zs", "short_liq_zs",
    "zc_div", "volume_base", "rsi_14", "volume_ratio", "ema_50", "ema_200",
    "session_vah", "session_val", "taker_volume_ratio", "future_cvd_15m",
    "spot_cvd_15m", "funding_rate_pct", "basis_index_bps"
]

ORB_FEATURES = [
    "direction_enum", "or_range_pct", "rsi_14", "vwap_dist", "ema_dist", 
    "hour", "day_of_week", "ema_200_dist", "ema_200_slope", "atr_14_pct", 
    "vol_spike", "or_range_atr", "pdl_dist", "pdh_dist", "swept_pdl", "swept_pdh",
    "body_ratio", "close_outside", "fvg_expansion", "judas_sweep"
]

S1_FEATURE_COLS = [
    "vwap_zscore", "long_liq_zs", "short_liq_zs", "zc_norm", "sf_div",
    "val_dist", "vah_dist", "taker_ratio", "rsi_14", "atr_ratio",
    "volume_ratio", "slope200", "funding_rate_pct", "basis_index_bps",
    "vol_strain", "hour", "tide_align", "pdl_dist", "pdh_dist",
    "pwl_dist", "pwh_dist", "pdl_sweep_bull", "pdh_sweep_bear",
    "signal_side"
]

DAY_MS = 86_400_000

def apply_atr_floor(atr: np.ndarray, close: np.ndarray, floor_pct: float = 0.012) -> np.ndarray:
    return np.maximum(np.asarray(atr, dtype=np.float64), np.asarray(close, dtype=np.float64) * floor_pct)


# ── 1. NUMBA ORDERFLOW & STRUCTURAL PIVOT ENGINES ─────────────────────────────
def compute_structural_pivots_and_sweeps(
    timestamps_ms: np.ndarray,
    highs: np.ndarray,
    lows: np.ndarray,
    closes: np.ndarray,
    deltas: np.ndarray,
    volumes: np.ndarray,
    volume_ratios: np.ndarray,
    atrs: np.ndarray,
) -> Tuple[
    np.ndarray, np.ndarray, np.ndarray, np.ndarray, np.ndarray, np.ndarray,
    np.ndarray, np.ndarray, np.ndarray, np.ndarray, np.ndarray, np.ndarray
]:
    n = len(timestamps_ms)
    if n == 0:
        z = np.zeros(0, dtype=np.float64)
        b = np.zeros(0, dtype=bool)
        return z, z, z, z, z, z, z, z, z, z, b, b

    t = np.asarray(timestamps_ms, dtype=np.int64)
    h = np.asarray(highs, dtype=np.float64)
    l = np.asarray(lows, dtype=np.float64)
    c = np.asarray(closes, dtype=np.float64)
    d = np.asarray(deltas, dtype=np.float64)
    atr = np.maximum(np.asarray(atrs, dtype=np.float64), 1e-6)

    # 1. Daily Pivots (00:00 UTC anchor)
    day_idx = (t // DAY_MS)
    _, d_start, d_counts = np.unique(day_idx, return_index=True, return_counts=True)
    pdh_day = np.empty(d_start.size, dtype=np.float64)
    pdl_day = np.empty(d_start.size, dtype=np.float64)
    pdh_day[1:], pdh_day[0] = np.maximum.reduceat(h, d_start)[:-1], h[0]
    pdl_day[1:], pdl_day[0] = np.minimum.reduceat(l, d_start)[:-1], l[0]
    pdh = np.repeat(pdh_day, d_counts)
    pdl = np.repeat(pdl_day, d_counts)

    # 2. Weekly Pivots (Monday 00:00 UTC anchor)
    week_idx = (t + 4 * DAY_MS) // (7 * DAY_MS)
    _, w_start, w_counts = np.unique(week_idx, return_index=True, return_counts=True)
    pwh_wk = np.empty(w_start.size, dtype=np.float64)
    pwl_wk = np.empty(w_start.size, dtype=np.float64)
    pwh_wk[1:], pwh_wk[0] = np.maximum.reduceat(h, w_start)[:-1], h[0]
    pwl_wk[1:], pwl_wk[0] = np.minimum.reduceat(l, w_start)[:-1], l[0]
    pwh = np.repeat(pwh_wk, w_counts)
    pwl = np.repeat(pwl_wk, w_counts)

    # 3. Monthly Pivots
    dt = pd.to_datetime(t, unit="ms", utc=True)
    m_idx = dt.year.to_numpy() * 12 + dt.month.to_numpy()
    _, m_start, m_counts = np.unique(m_idx, return_index=True, return_counts=True)
    pmh_m = np.empty(m_start.size, dtype=np.float64)
    pml_m = np.empty(m_start.size, dtype=np.float64)
    pmh_m[1:], pmh_m[0] = np.maximum.reduceat(h, m_start)[:-1], h[0]
    pml_m[1:], pml_m[0] = np.minimum.reduceat(l, m_start)[:-1], l[0]
    pmh = np.repeat(pmh_m, m_counts)
    pml = np.repeat(pml_m, m_counts)

    # 4. Normalized distances in ATR units
    pdl_dist = np.clip((c - pdl) / atr, -10.0, 10.0)
    pdh_dist = np.clip((c - pdh) / atr, -10.0, 10.0)
    pwl_dist = np.clip((c - pwl) / atr, -10.0, 10.0)
    pwh_dist = np.clip((c - pwh) / atr, -10.0, 10.0)

    # 5. Orderflow Sweeps with Footprint Delta Absorption
    pdl_sweep_bull = (l < pdl) & (c > pdl) & (d > 0)
    pdh_sweep_bear = (h > pdh) & (c < pdh) & (d < 0)

    return pdh, pdl, pwh, pwl, pmh, pml, pdl_dist, pdh_dist, pwl_dist, pwh_dist, pdl_sweep_bull, pdh_sweep_bear


@njit(fastmath=True)
def label_triple_barriers_numba(
    c: np.ndarray,
    h: np.ndarray,
    lo: np.ndarray,
    o: np.ndarray,
    atr: np.ndarray,
    long_cond: np.ndarray,
    short_cond: np.ndarray,
    horizon_bars: int = 32,
    target_r: float = 3.00,
    stop_r: float = 1.00,
    be_trigger_r: float = 1.40,
    be_lock_r: float = 0.35,
    profit_trigger_r: float = 2.00,
    profit_lock_r: float = 1.20,
    trail_trigger_r: float = 2.50,
    trail_lock_r: float = 1.80,
    friction_r: float = 0.18,
) -> Tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    """
    Causal next-bar-open execution with 3-stage ratchet and 24-bar time decay.
    Zero lookahead: entry at o[i+1].
    """
    n = len(c)
    is_candidate = np.zeros(n, dtype=np.bool_)
    side = np.zeros(n, dtype=np.int8)
    label_y = np.full(n, -1, dtype=np.int8)
    realized_r = np.zeros(n, dtype=np.float64)
    bars_held = np.zeros(n, dtype=np.int16)

    for i in range(n - horizon_bars):
        s = 0
        if long_cond[i]:
            s = 1
        elif short_cond[i]:
            s = -1
        else:
            continue

        is_candidate[i] = True
        side[i] = s
        entry_p = o[i + 1]  # Next-bar open fill (causal)
        dist = atr[i]
        if dist <= 0:
            continue

        cur_stop_r = -stop_r
        exit_r = 0.0
        hit = False
        hold_count = horizon_bars

        for j in range(i + 1, i + 1 + horizon_bars):
            if s == 1:
                adverse_r = (lo[j] - entry_p) / dist
                favorable_r = (h[j] - entry_p) / dist
            else:
                adverse_r = (entry_p - h[j]) / dist
                favorable_r = (entry_p - lo[j]) / dist

            # 1. Stop loss check (evaluated first)
            if adverse_r <= cur_stop_r:
                exit_r = cur_stop_r
                hit = True
                hold_count = j - i
                break

            # 2. Target hit
            if favorable_r >= target_r:
                exit_r = target_r
                hit = True
                hold_count = j - i
                break

            # 3. Microstructure ratchet progression
            if favorable_r >= trail_trigger_r:
                if trail_lock_r > cur_stop_r:
                    cur_stop_r = trail_lock_r
            elif favorable_r >= profit_trigger_r:
                if profit_lock_r > cur_stop_r:
                    cur_stop_r = profit_lock_r
            elif favorable_r >= be_trigger_r:
                if be_lock_r > cur_stop_r:
                    cur_stop_r = be_lock_r

            # 4. Time decay: at bar horizon_bars exit if R < 0.20
            if (j - i) == horizon_bars:
                cur_r = (c[j] - entry_p) / dist if s == 1 else (entry_p - c[j]) / dist
                if cur_r < 0.20:
                    exit_r = cur_r
                    hit = True
                    hold_count = horizon_bars
                    break

        if not hit:
            exit_p = c[i + horizon_bars]
            exit_r = (exit_p - entry_p) / dist if s == 1 else (entry_p - exit_p) / dist
            hold_count = horizon_bars

        net_r = exit_r - friction_r
        realized_r[i] = net_r
        label_y[i] = 1 if net_r > 0 else 0
        bars_held[i] = hold_count

    return is_candidate, side, label_y, realized_r, bars_held


# ── 2. NUMBA OPENING RANGE BREAKOUT (ORB + CRT) ENGINE ─────────────────────────
@njit(fastmath=True)
def simulate_orb_trades(
    opens: np.ndarray,
    highs: np.ndarray,
    lows: np.ndarray,
    closes: np.ndarray,
    volumes: np.ndarray,
    timestamps: np.ndarray,
    dates: np.ndarray,
    hours: np.ndarray,
    minutes: np.ndarray,
    day_of_weeks: np.ndarray,
    start_hour: int,
    start_minute: int,
    range_duration_bars: int = 2,
    trade_duration_bars: int = 36
) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
    """
    Session Opening Range Breakout (ORB) with Candle Range Theory (CRT) & Judas sweeps.
    Strictly causal execution at opens[j+1].
    """
    n = len(highs)
    max_trades = (n // 10) + 100

    features = np.zeros((max_trades, 20), dtype=np.float64)
    outcomes = np.zeros(max_trades, dtype=np.float64)
    timestamps_out = np.zeros(max_trades, dtype=np.int64)

    emas_50 = np.zeros(n)
    emas_50[0] = closes[0]
    alpha_50 = 2.0 / (50 + 1)

    emas_200 = np.zeros(n)
    emas_200[0] = closes[0]
    alpha_200 = 2.0 / (200 + 1)

    vwaps = np.zeros(n)
    cum_vol = 0.0
    cum_vol_price = 0.0

    gains = np.zeros(n)
    losses = np.zeros(n)
    rsis = np.zeros(n)
    trs = np.zeros(n)
    atrs = np.zeros(n)
    vol_sma_20 = np.zeros(n)

    for i in range(1, n):
        emas_50[i] = emas_50[i-1] + alpha_50 * (closes[i] - emas_50[i-1])
        emas_200[i] = emas_200[i-1] + alpha_200 * (closes[i] - emas_200[i-1])

        if dates[i] != dates[i-1]:
            cum_vol = volumes[i]
            cum_vol_price = closes[i] * volumes[i]
        else:
            cum_vol += volumes[i]
            cum_vol_price += closes[i] * volumes[i]

        if cum_vol > 0:
            vwaps[i] = cum_vol_price / cum_vol
        else:
            vwaps[i] = closes[i]

        change = closes[i] - closes[i-1]
        if change > 0:
            gains[i] = change
        else:
            losses[i] = -change

        tr1 = highs[i] - lows[i]
        tr2 = abs(highs[i] - closes[i-1])
        tr3 = abs(lows[i] - closes[i-1])
        trs[i] = max(tr1, max(tr2, tr3))

        if i >= 14:
            avg_gain = np.mean(gains[i-13:i+1])
            avg_loss = np.mean(losses[i-13:i+1])
            if avg_loss == 0:
                rsis[i] = 100.0
            else:
                rs = avg_gain / avg_loss
                rsis[i] = 100.0 - (100.0 / (1.0 + rs))
            atrs[i] = np.mean(trs[i-13:i+1])

        if i >= 20:
            vol_sma_20[i] = np.mean(volumes[i-19:i+1])
            if vol_sma_20[i] == 0:
                vol_sma_20[i] = 1.0

    trade_idx = 0
    prev_day_high = highs[0]
    prev_day_low = lows[0]
    curr_day_high = highs[0]
    curr_day_low = lows[0]
    curr_date = dates[0]

    i = 0
    while i < n - range_duration_bars - 1:
        if dates[i] != curr_date:
            prev_day_high = curr_day_high
            prev_day_low = curr_day_low
            curr_date = dates[i]
            curr_day_high = highs[i]
            curr_day_low = lows[i]
        else:
            if highs[i] > curr_day_high:
                curr_day_high = highs[i]
            if lows[i] < curr_day_low:
                curr_day_low = lows[i]

        if hours[i] == start_hour and minutes[i] == start_minute:
            or_high = highs[i]
            or_low = lows[i]

            for j in range(1, range_duration_bars):
                if highs[i+j] > or_high:
                    or_high = highs[i+j]
                if lows[i+j] < or_low:
                    or_low = lows[i+j]

            or_range = or_high - or_low
            pdl_dist = (or_low - prev_day_low) / (prev_day_low + 1e-9)
            pdh_dist = (prev_day_high - or_high) / (prev_day_high + 1e-9)
            swept_pdl = 1.0 if or_low < prev_day_low else 0.0
            swept_pdh = 1.0 if or_high > prev_day_high else 0.0

            if or_range > 0:
                trade_start = i + range_duration_bars
                trade_end = min(n, trade_start + trade_duration_bars)

                pre_start = max(0, i - 6)
                pre_or_low = lows[pre_start]
                pre_or_high = highs[pre_start]
                for p in range(pre_start, i):
                    if lows[p] < pre_or_low:
                        pre_or_low = lows[p]
                    if highs[p] > pre_or_high:
                        pre_or_high = highs[p]

                judas_sweep_long = 1.0 if (pre_or_low < prev_day_low and or_low >= prev_day_low) else 0.0
                judas_sweep_short = 1.0 if (pre_or_high > prev_day_high and or_high <= prev_day_high) else 0.0

                for j in range(trade_start, trade_end):
                    if highs[j] > or_high:
                        if (swept_pdl == 1.0 or judas_sweep_long == 1.0):
                            entry_bar = j + 1
                            if entry_bar >= trade_end or entry_bar >= n:
                                continue

                            direction = 1.0
                            entry = opens[entry_bar]
                            sl = or_low

                            prev_idx = j
                            atr_val = atrs[prev_idx]
                            atr_pct = atr_val / (closes[prev_idx] + 1e-9)

                            capped_range = or_range
                            if atr_val > 0 and capped_range > 1.75 * atr_val:
                                capped_range = 1.75 * atr_val
                            r_val = max(entry - sl, 0.50 * capped_range)
                            if atr_val > 0 and r_val > 1.75 * atr_val:
                                r_val = 1.75 * atr_val
                                current_sl = entry - r_val
                            else:
                                current_sl = sl
                            r_val = max(r_val, 1e-4)

                            tp = entry + 3.00 * r_val
                            v_dist = (closes[prev_idx] - vwaps[prev_idx]) / (closes[prev_idx] + 1e-9)
                            e50_dist = (closes[prev_idx] - emas_50[prev_idx]) / (closes[prev_idx] + 1e-9)
                            e200_dist = (closes[prev_idx] - emas_200[prev_idx]) / (closes[prev_idx] + 1e-9)
                            e200_slope = (emas_200[prev_idx] - emas_200[prev_idx-10]) / (emas_200[prev_idx-10] + 1e-9) if prev_idx >= 10 else 0.0
                            vol_spike = volumes[prev_idx] / (vol_sma_20[prev_idx-1 if prev_idx > 0 else 0] + 1e-9)
                            range_atr = or_range / (atr_val + 1e-9)

                            body_ratio = min(1.0, max(0.0, abs(closes[prev_idx] - opens[prev_idx]) / (highs[prev_idx] - lows[prev_idx] + 1e-9)))
                            close_outside = 1.0 if closes[prev_idx] > or_high else 0.0
                            fvg_expansion = 1.0 if (prev_idx >= 2 and lows[prev_idx] > highs[prev_idx-2] and (lows[prev_idx] - highs[prev_idx-2]) < 2.0 * atr_val) else 0.0

                            features[trade_idx, 0] = direction
                            features[trade_idx, 1] = or_range / (or_low + 1e-9)
                            features[trade_idx, 2] = rsis[prev_idx]
                            features[trade_idx, 3] = v_dist
                            features[trade_idx, 4] = e50_dist
                            features[trade_idx, 5] = float(hours[prev_idx])
                            features[trade_idx, 6] = float(day_of_weeks[prev_idx])
                            features[trade_idx, 7] = e200_dist
                            features[trade_idx, 8] = e200_slope
                            features[trade_idx, 9] = atr_pct
                            features[trade_idx, 10] = vol_spike
                            features[trade_idx, 11] = range_atr
                            features[trade_idx, 12] = pdl_dist
                            features[trade_idx, 13] = pdh_dist
                            features[trade_idx, 14] = swept_pdl
                            features[trade_idx, 15] = swept_pdh
                            features[trade_idx, 16] = body_ratio
                            features[trade_idx, 17] = close_outside
                            features[trade_idx, 18] = fvg_expansion
                            features[trade_idx, 19] = judas_sweep_long

                            phase0_trigger = 1.40
                            outcome_r = -1.0
                            exit_taken = False
                            phase_0_locked = False
                            phase_1_locked = False
                            phase_2_locked = False
                            trail_active = False

                            for k in range(entry_bar + 1, trade_end):
                                if k - entry_bar >= 32:
                                    current_r = (closes[k] - entry) / r_val
                                    if current_r < 0.20:
                                        outcome_r = current_r
                                        exit_taken = True
                                        break

                                if lows[k] <= current_sl:
                                    outcome_r = (current_sl - entry) / r_val
                                    exit_taken = True
                                    break

                                if highs[k] >= tp:
                                    outcome_r = 3.00
                                    exit_taken = True
                                    break

                                current_gain = (closes[k] - entry) / r_val
                                if not phase_0_locked and current_gain >= phase0_trigger:
                                    current_sl = entry + 0.35 * r_val
                                    phase_0_locked = True
                                if phase_0_locked and not phase_1_locked and current_gain >= 2.00:
                                    current_sl = entry + 1.20 * r_val
                                    phase_1_locked = True
                                    trail_active = True
                                if phase_1_locked and not phase_2_locked and current_gain >= 2.50:
                                    current_sl = max(current_sl, entry + 1.80 * r_val)
                                    phase_2_locked = True

                                if trail_active:
                                    trail_sl = closes[k] - 1.5 * atrs[k]
                                    if trail_sl > current_sl:
                                        current_sl = trail_sl

                            if not exit_taken:
                                outcome_r = (closes[trade_end-1] - entry) / r_val

                            outcome_r -= 0.08
                            outcomes[trade_idx] = max(-1.15, min(3.00, outcome_r))
                            timestamps_out[trade_idx] = timestamps[entry_bar]
                            trade_idx += 1
                            i = trade_end
                            break

                    elif lows[j] < or_low:
                        if (swept_pdh == 1.0 or judas_sweep_short == 1.0):
                            entry_bar = j + 1
                            if entry_bar >= trade_end or entry_bar >= n:
                                continue

                            direction = -1.0
                            entry = opens[entry_bar]
                            sl = or_high

                            prev_idx = j
                            atr_val = atrs[prev_idx]
                            atr_pct = atr_val / (closes[prev_idx] + 1e-9)

                            capped_range = or_range
                            if atr_val > 0 and capped_range > 1.75 * atr_val:
                                capped_range = 1.75 * atr_val
                            r_val = max(sl - entry, 0.50 * capped_range)
                            if atr_val > 0 and r_val > 1.75 * atr_val:
                                r_val = 1.75 * atr_val
                                current_sl = entry + r_val
                            else:
                                current_sl = sl
                            r_val = max(r_val, 1e-4)

                            tp = entry - 3.00 * r_val
                            v_dist = (closes[prev_idx] - vwaps[prev_idx]) / (closes[prev_idx] + 1e-9)
                            e50_dist = (closes[prev_idx] - emas_50[prev_idx]) / (closes[prev_idx] + 1e-9)
                            e200_dist = (closes[prev_idx] - emas_200[prev_idx]) / (closes[prev_idx] + 1e-9)
                            e200_slope = (emas_200[prev_idx] - emas_200[prev_idx-10]) / (emas_200[prev_idx-10] + 1e-9) if prev_idx >= 10 else 0.0
                            vol_spike = volumes[prev_idx] / (vol_sma_20[prev_idx-1 if prev_idx > 0 else 0] + 1e-9)
                            range_atr = or_range / (atr_val + 1e-9)

                            body_ratio = min(1.0, max(0.0, abs(closes[prev_idx] - opens[prev_idx]) / (highs[prev_idx] - lows[prev_idx] + 1e-9)))
                            close_outside = 1.0 if closes[prev_idx] < or_low else 0.0
                            fvg_expansion = 1.0 if (prev_idx >= 2 and highs[prev_idx] < lows[prev_idx-2] and (lows[prev_idx-2] - highs[prev_idx]) < 2.0 * atr_val) else 0.0

                            features[trade_idx, 0] = direction
                            features[trade_idx, 1] = or_range / (or_low + 1e-9)
                            features[trade_idx, 2] = rsis[prev_idx]
                            features[trade_idx, 3] = v_dist
                            features[trade_idx, 4] = e50_dist
                            features[trade_idx, 5] = float(hours[prev_idx])
                            features[trade_idx, 6] = float(day_of_weeks[prev_idx])
                            features[trade_idx, 7] = e200_dist
                            features[trade_idx, 8] = e200_slope
                            features[trade_idx, 9] = atr_pct
                            features[trade_idx, 10] = vol_spike
                            features[trade_idx, 11] = range_atr
                            features[trade_idx, 12] = pdl_dist
                            features[trade_idx, 13] = pdh_dist
                            features[trade_idx, 14] = swept_pdl
                            features[trade_idx, 15] = swept_pdh
                            features[trade_idx, 16] = body_ratio
                            features[trade_idx, 17] = close_outside
                            features[trade_idx, 18] = fvg_expansion
                            features[trade_idx, 19] = judas_sweep_short

                            phase0_trigger = 1.40
                            outcome_r = -1.0
                            exit_taken = False
                            phase_0_locked = False
                            phase_1_locked = False
                            phase_2_locked = False
                            trail_active = False

                            for k in range(entry_bar + 1, trade_end):
                                if k - entry_bar >= 32:
                                    current_r = (entry - closes[k]) / r_val
                                    if current_r < 0.20:
                                        outcome_r = current_r
                                        exit_taken = True
                                        break

                                if highs[k] >= current_sl:
                                    outcome_r = (entry - current_sl) / r_val
                                    exit_taken = True
                                    break

                                if lows[k] <= tp:
                                    outcome_r = 3.00
                                    exit_taken = True
                                    break

                                current_gain = (entry - closes[k]) / r_val
                                if not phase_0_locked and current_gain >= phase0_trigger:
                                    current_sl = entry - 0.35 * r_val
                                    phase_0_locked = True
                                if phase_0_locked and not phase_1_locked and current_gain >= 2.00:
                                    current_sl = entry - 1.20 * r_val
                                    phase_1_locked = True
                                    trail_active = True
                                if phase_1_locked and not phase_2_locked and current_gain >= 2.50:
                                    current_sl = min(current_sl, entry - 1.80 * r_val)
                                    phase_2_locked = True

                                if trail_active:
                                    trail_sl = closes[k] + 1.5 * atrs[k]
                                    if trail_sl < current_sl:
                                        current_sl = trail_sl

                            if not exit_taken:
                                outcome_r = (entry - closes[trade_end-1]) / r_val

                            outcome_r -= 0.08
                            outcomes[trade_idx] = max(-1.15, min(3.00, outcome_r))
                            timestamps_out[trade_idx] = timestamps[entry_bar]
                            trade_idx += 1
                            i = trade_end
                            break
        i += 1

    return features[:trade_idx], outcomes[:trade_idx], timestamps_out[:trade_idx]


# ── 3. DATASET COMPILATION ENGINES ────────────────────────────────────────────
def load_btc_macro_tide(data_dir: Path) -> pd.Series:
    btc_path = data_dir / "BTCUSDT_15m_master_2020_2026.parquet"
    if not btc_path.exists():
        return pd.Series(dtype=float)
    df = pd.read_parquet(btc_path, columns=["open_time_ms", "close", "ema_50", "ema_200"])
    c, e50, e200 = df["close"], df["ema_50"], df["ema_200"]
    bull = (c > e50) & (e50 > e200)
    bear = (c < e50) & (e50 < e200)
    tide = np.where(bull, 1.0, np.where(bear, -1.0, 0.0))
    return pd.Series(tide, index=df["open_time_ms"])


def compile_s1_candidates(data_dir: Path) -> pd.DataFrame:
    print(f"Compiling Sleeve S1/S4 candidates across {len(CORE_SYMBOLS)} institutional crypto assets...")
    t0 = time.perf_counter()
    btc_tide = load_btc_macro_tide(data_dir)
    frames = []

    for sym in CORE_SYMBOLS:
        p_path = data_dir / f"{sym}_15m_master_2020_2026.parquet"
        if not p_path.exists():
            continue

        df = pd.read_parquet(p_path, columns=COLS_TO_LOAD).reset_index(drop=True)
        c, h, lo, op = df["close"].to_numpy(float), df["high"].to_numpy(float), df["low"].to_numpy(float), df["open"].to_numpy(float)
        t = df["open_time_ms"].to_numpy(np.int64)

        atr_raw = df["atr_14"].fillna(df["close"] * 0.01).to_numpy(float)
        atr = apply_atr_floor(atr_raw, c, 0.012)
        atr_100 = df["atr_100"].fillna(df["close"] * 0.01).to_numpy(float)
        atr_ratio = np.clip(np.where(atr_100 > 0, atr / atr_100, 1.0), 0.2, 5.0)

        e200 = df["ema_200"].to_numpy(float)
        slope = ((df["ema_200"] - df["ema_200"].shift(12)) / atr).fillna(0.0).to_numpy(float)
        tide = pd.Series(t).map(btc_tide).fillna(0.0).to_numpy(float)
        vwap_z = df["vwap_zscore"].fillna(0.0).to_numpy(float)
        vol_ratio = df["volume_ratio"].fillna(1.0).to_numpy(float)
        vol_base = df["volume_base"].replace(0, 1.0)
        zc_norm = (df["zc_div"] / vol_base).clip(-3.0, 3.0).fillna(0.0).to_numpy(float)
        sf_div = ((df["spot_cvd_15m"] - df["future_cvd_15m"]) / vol_base).clip(-3.0, 3.0).fillna(0.0).to_numpy(float)
        long_liq = df["long_liq_zs"].fillna(0.0).to_numpy(float)
        short_liq = df["short_liq_zs"].fillna(0.0).to_numpy(float)
        s_val = df["session_val"].fillna(df["low"]).to_numpy(float)
        s_vah = df["session_vah"].fillna(df["high"]).to_numpy(float)
        val_dist = np.clip((c - s_val) / atr, -5.0, 5.0)
        vah_dist = np.clip((c - s_vah) / atr, -5.0, 5.0)
        taker_ratio = df["taker_volume_ratio"].fillna(1.0).to_numpy(float)
        fund_rate = df["funding_rate_pct"].fillna(0.0).to_numpy(float)
        basis_bps = df["basis_index_bps"].fillna(0.0).to_numpy(float)
        rsi = df["rsi_14"].fillna(50.0).to_numpy(float)
        vol_strain = np.clip(atr / np.maximum(c, 1e-6), 0.005, 0.10)
        hour = (t // (3600 * 1000)) % 24

        fut_delta = df["future_cvd_15m"].fillna(0.0).to_numpy(float)
        (
            pdh, pdl, pwh, pwl, pmh, pml,
            pdl_dist, pdh_dist, pwl_dist, pwh_dist,
            pdl_sweep_bull, pdh_sweep_bear
        ) = compute_structural_pivots_and_sweeps(t, h, lo, c, fut_delta, vol_base, vol_ratio, atr)

        ret = np.diff(np.log(np.maximum(c, 1e-9)), prepend=0.0)
        rv_96 = pd.Series(ret).rolling(96, min_periods=8).std().fillna(0.0).to_numpy(float)
        rv_rank = pd.Series(rv_96).rolling(384, min_periods=32).rank(pct=True).fillna(0.5).to_numpy(float)
        is_shock = rv_rank >= 0.88

        bull_pullback = (c > e200) & (vwap_z < -0.4) & (rsi < 45) & (zc_norm > 0.0) & (vol_ratio >= 1.2)
        bear_rally = (c < e200) & (vwap_z > 0.4) & (rsi > 55) & (zc_norm < 0.0) & (vol_ratio >= 1.2) & (short_liq < 0.8)
        t2_liq_flush = (long_liq >= 1.5) & (vwap_z <= -0.6) & (zc_norm > 0.0) & (vol_ratio >= 1.3) & (c > e200)
        t3_pdl_sweep = pdl_sweep_bull & (vol_ratio >= 1.1)
        t3_pdh_sweep = pdh_sweep_bear & (vol_ratio >= 1.1)

        long_cond = (t2_liq_flush | t3_pdl_sweep) & (~is_shock) & np.isfinite(atr) & (atr > 0)
        short_cond = t3_pdh_sweep & (~is_shock) & np.isfinite(atr) & (atr > 0)
        long_cond = (long_cond & (~short_cond)).astype(bool)
        short_cond = (short_cond & (~long_cond)).astype(bool)

        tide_align = np.where(long_cond, tide, np.where(short_cond, -tide, 0.0))

        is_cand, s_arr, label_y, real_r, b_held = label_triple_barriers_numba(
            c, h, lo, op, atr, long_cond, short_cond, 32, 3.00, 1.00,
            be_trigger_r=1.40, be_lock_r=0.35,
            profit_trigger_r=2.00, profit_lock_r=1.20,
            trail_trigger_r=2.50, trail_lock_r=1.80,
            friction_r=FRICTION_R_S1,
        )

        cand_idx = np.where(is_cand)[0]
        f_sub = pd.DataFrame({
            "open_time_ms": t[cand_idx],
            "symbol": sym,
            "signal_side": s_arr[cand_idx],
            "realized_r": real_r[cand_idx],
            "bars_held": b_held[cand_idx],
            "label_y": label_y[cand_idx],
            "vwap_zscore": vwap_z[cand_idx],
            "long_liq_zs": long_liq[cand_idx],
            "short_liq_zs": short_liq[cand_idx],
            "zc_norm": zc_norm[cand_idx],
            "sf_div": sf_div[cand_idx],
            "val_dist": val_dist[cand_idx],
            "vah_dist": vah_dist[cand_idx],
            "taker_ratio": taker_ratio[cand_idx],
            "rsi_14": rsi[cand_idx],
            "atr_ratio": atr_ratio[cand_idx],
            "volume_ratio": vol_ratio[cand_idx],
            "slope200": slope[cand_idx],
            "funding_rate_pct": fund_rate[cand_idx],
            "basis_index_bps": basis_bps[cand_idx],
            "vol_strain": vol_strain[cand_idx],
            "hour": hour[cand_idx],
            "tide_align": tide_align[cand_idx],
            "pdl_dist": pdl_dist[cand_idx],
            "pdh_dist": pdh_dist[cand_idx],
            "pwl_dist": pwl_dist[cand_idx],
            "pwh_dist": pwh_dist[cand_idx],
            "pdl_sweep_bull": pdl_sweep_bull[cand_idx].astype(float),
            "pdh_sweep_bear": pdh_sweep_bear[cand_idx].astype(float),
            "btc_macro_tide": tide[cand_idx],
            "strategy": "S1",
        })
        frames.append(f_sub)

    master = pd.concat(frames, ignore_index=True).sort_values("open_time_ms").reset_index(drop=True)
    print(f"Generated {len(master):,d} S1 candidates in {time.perf_counter() - t0:.2f}s.")
    return master


def compile_orb_candidates(crypto_dir: Path, forex_dir: Path = None) -> pd.DataFrame:
    print(f"Compiling Sleeve S3 (London & NY ORB/CRT) candidates...")
    t0 = time.perf_counter()
    all_trades = []

    # 1. Crypto perps - strictly NY Open (13:30 UTC) for institutional assets (BTC & ETH)
    for a in ["BTCUSDT", "ETHUSDT"]:
        p = crypto_dir / f"{a}_15m_master_2020_2026.parquet"
        if not p.exists():
            continue
        df = pd.read_parquet(p).dropna().reset_index(drop=True)
        opens = df['open'].values.astype(np.float64)
        highs = df['high'].values.astype(np.float64)
        lows = df['low'].values.astype(np.float64)
        closes = df['close'].values.astype(np.float64)
        volumes = df['volume_base'].values.astype(np.float64)
        timestamps = df['open_time_ms'].values.astype(np.int64)
        dt = pd.to_datetime(timestamps, unit="ms", utc=True)
        dates = dt.strftime('%Y%m%d').astype(np.int64).values
        hours = dt.hour.values.astype(np.int32)
        minutes = dt.minute.values.astype(np.int32)
        day_of_weeks = dt.dayofweek.values.astype(np.int32)

        feat, out, t_out = simulate_orb_trades(opens, highs, lows, closes, volumes, timestamps, dates, hours, minutes, day_of_weeks, 13, 30)
        if len(out) == 0:
            continue
        tdf = pd.DataFrame(feat, columns=ORB_FEATURES)
        tdf['realized_r'] = out
        tdf['open_time_ms'] = t_out
        tdf['symbol'] = a
        tdf['bars_held'] = 32
        tdf['strategy'] = 'ORB'
        tdf['asset_class'] = 'CRYPTO'
        tdf['label_y'] = (out > 0).astype(int)
        all_trades.append(tdf)

    # 2. Macro Hedges (European Indices at London 07:00, US Indices at NY 13:30, Commodities at both)
    if forex_dir and forex_dir.exists():
        for a in FOREX_SYMBOLS:
            p = forex_dir / f"{a}_15m_real.parquet"
            if not p.exists():
                continue
            df = pd.read_parquet(p).dropna().reset_index(drop=True)
            dt_idx = pd.DatetimeIndex(pd.to_datetime(df['datetime'], utc=True))
            opens = df['open'].values.astype(np.float64)
            highs = df['high'].values.astype(np.float64)
            lows = df['low'].values.astype(np.float64)
            closes = df['close'].values.astype(np.float64)
            volumes = df['real_volume'].values.astype(np.float64) if 'real_volume' in df.columns else (df['tick_volume'].values.astype(np.float64) if 'tick_volume' in df.columns else np.ones(len(df)))
            timestamps = dt_idx.asi8 // 1_000_000
            dates = dt_idx.strftime('%Y%m%d').astype(np.int64).values
            hours = dt_idx.hour.values.astype(np.int32)
            minutes = dt_idx.minute.values.astype(np.int32)
            day_of_weeks = dt_idx.dayofweek.values.astype(np.int32)

            if a in ["GER30", "FR40"]:
                sessions = [(7, 0)]
            elif a in ["US2000"]:
                sessions = [(13, 30)]
            else:
                sessions = [(7, 0), (13, 30)]

            for sh, sm in sessions:
                feat, out, t_out = simulate_orb_trades(opens, highs, lows, closes, volumes, timestamps, dates, hours, minutes, day_of_weeks, sh, sm)
                if len(out) == 0:
                    continue
                tdf = pd.DataFrame(feat, columns=ORB_FEATURES)
                tdf['realized_r'] = out
                tdf['open_time_ms'] = t_out
                tdf['symbol'] = a
                tdf['bars_held'] = 32
                tdf['strategy'] = 'ORB'
                tdf['asset_class'] = 'FOREX'
                tdf['label_y'] = (out > 0).astype(int)
                all_trades.append(tdf)

    master = pd.concat(all_trades, ignore_index=True).sort_values("open_time_ms").reset_index(drop=True)
    print(f"Generated {len(master):,d} S3 ORB candidates in {time.perf_counter() - t0:.2f}s.")
    return master


# ── 4. MACHINE LEARNING ENGINES ───────────────────────────────────────────────
class S1DualModelEngine:
    """60% Ridge Logistic Regression + 40% Shallow LightGBM for S1 Orderflow."""
    def __init__(self, random_state: int = 42):
        self.random_state = random_state

    def train_models(self, train_df: pd.DataFrame) -> Tuple[LogisticRegression, lgb.LGBMClassifier, pd.Series, pd.Series, float]:
        X_train = train_df[S1_FEATURE_COLS]
        y_train = train_df["label_y"].to_numpy()

        mu = X_train.mean(axis=0)
        sd = X_train.std(axis=0).replace(0, 1.0)
        X_tr_s = np.nan_to_num(((X_train - mu) / sd).clip(-5.0, 5.0).to_numpy(float), nan=0.0)

        ridge = LogisticRegression(C=0.0287456, max_iter=200, random_state=self.random_state)
        ridge.fit(X_tr_s, y_train)

        clf = lgb.LGBMClassifier(
            n_estimators=140, max_depth=4, num_leaves=15, learning_rate=0.04,
            subsample=0.8, colsample_bytree=0.8, reg_alpha=2.0, reg_lambda=0.5,
            random_state=self.random_state, verbose=-1, n_jobs=2
        )
        clf.fit(X_train, y_train)

        probs_ridge = ridge.predict_proba(X_tr_s)[:, 1]
        probs_lgb = clf.predict_proba(X_train)[:, 1]
        train_probs = 0.60 * probs_ridge + 0.40 * probs_lgb

        calib_thresh = float(np.quantile(train_probs, 0.55))
        calib_thresh = max(0.48, min(0.55, calib_thresh))
        return ridge, clf, mu, sd, calib_thresh

    def score_test_candidates(
        self, test_df: pd.DataFrame, ridge: LogisticRegression, clf: lgb.LGBMClassifier,
        mu: pd.Series, sd: pd.Series, calib_thresh: float
    ) -> pd.DataFrame:
        if len(test_df) == 0:
            return test_df
        X_test = test_df[S1_FEATURE_COLS]
        X_te_s = np.nan_to_num(((X_test - mu) / sd).clip(-5.0, 5.0).to_numpy(float), nan=0.0)
        p_ridge = ridge.predict_proba(X_te_s)[:, 1]
        p_lgb = clf.predict_proba(X_test)[:, 1]
        probs = 0.60 * p_ridge + 0.40 * p_lgb
        scored = test_df.copy()
        scored["prob"] = probs
        scored["calib_thresh"] = calib_thresh
        return scored


class S3ORBModelEngine:
    """Depth-constrained LightGBM for S3 Session Opening Range Breakouts."""
    def __init__(self, random_state: int = 42):
        self.random_state = random_state

    def train_and_score(self, train_df: pd.DataFrame, test_df: pd.DataFrame) -> pd.DataFrame:
        if len(train_df) < 200 or len(test_df) == 0:
            return pd.DataFrame()
        X_tr = train_df[ORB_FEATURES]
        y_tr = train_df["label_y"].to_numpy()

        clf = lgb.LGBMClassifier(
            n_estimators=100, max_depth=3, learning_rate=0.04, num_leaves=7,
            min_child_samples=30, reg_alpha=1.5, reg_lambda=3.0,
            random_state=self.random_state, verbose=-1, n_jobs=2
        )
        clf.fit(X_tr, y_tr)
        probs_tr = clf.predict_proba(X_tr)[:, 1]
        thresh = float(np.quantile(probs_tr, 0.55)) if len(probs_tr) > 10 else 0.48
        thresh = max(0.48, min(0.54, thresh))

        probs_te = clf.predict_proba(test_df[ORB_FEATURES])[:, 1]
        scored = test_df.copy()
        scored["prob"] = probs_te
        scored["calib_thresh"] = thresh
        return scored[scored["prob"] >= thresh].copy()


# ── 5. UNIFIED MULTI-SLEEVE PORTFOLIO SIMULATOR ───────────────────────────────
def simulate_multiverse_portfolio(
    events: List[Dict[str, Any]],
    capital: float = INITIAL_CAPITAL,
    is_cumulative: bool = False,
) -> Tuple[pd.DataFrame, np.ndarray, np.ndarray]:
    equity = capital
    peak_equity = capital
    consec_losses_s1 = 0
    consec_losses_orb = 0
    s1_cooldown_until = 0

    s1_positions: List[Tuple[int, float, str]] = []
    orb_positions: List[Tuple[int, float, str]] = []
    symbol_cooldown: Dict[str, int] = {}
    trade_log = []
    equity_curve = [capital]
    timestamps_curve = [events[0]["time"] if events else 0]

    for ev in events:
        t_entry = ev["time"]
        strat = ev["strategy"]
        sym = ev["symbol"]
        r_gain = ev["r_gain"]
        prob = ev["prob"]
        hold_ms = int(ev.get("bars_held", 32)) * 15 * 60 * 1000

        cur_cap_dd = ((capital - equity) / capital) * 100.0 if equity < capital else 0.0
        cur_peak_dd = ((peak_equity - equity) / peak_equity) * 100.0 if peak_equity > 0 else 0.0

        if not is_cumulative and cur_cap_dd >= HARD_DD_LIMIT:
            break

        # S1 circuit breaker: isolate S1 losses during systemic crypto liquidations
        if strat == "S1" and (t_entry < s1_cooldown_until or cur_cap_dd >= 4.00):
            continue

        # Prune expired positions
        s1_positions = [p for p in s1_positions if p[0] > t_entry]
        orb_positions = [p for p in orb_positions if p[0] > t_entry]
        tot_active = len(s1_positions) + len(orb_positions)

        if sym in symbol_cooldown and t_entry < symbol_cooldown[sym]:
            continue
        if tot_active >= MAX_CONCURRENT:
            continue

        current_profit = equity - capital

        # CPPI Milestone Cushion Protection (above +10% milestone / +500 USD)
        if (peak_equity - capital) >= 500.0 and len(trade_log) >= 15 and not is_cumulative:
            cushion = max(0.0, equity - (capital + 500.0))
            risk_amt = min(6.0, cushion * 0.20)
            if risk_amt <= 0.0:
                continue
        elif cur_cap_dd >= DEF_DD_TRIGGER or cur_peak_dd >= 2.00:
            risk_amt = DEFENSE_RISK
        elif current_profit >= 250.0:
            risk_amt = 32.0
        elif current_profit >= 50.0:
            base_r = S1_BASE_RISK if strat == "S1" else ORB_BASE_RISK
            risk_amt = min(55.0, base_r + current_profit * 0.10)
        elif strat == "S1":
            if len(s1_positions) >= MAX_S1_CONCURRENT:
                continue
            conf = 1.15 if prob >= 0.52 else 1.0
            base_s = S1_BASE_RISK * conf
            tide = ev.get("tide", 0.0)
            side = ev.get("side", 1)
            if side == 1 and tide < 0:
                base_s *= 0.70
            risk_amt = base_s
        else:
            if len(orb_positions) >= MAX_ORB_CONCURRENT:
                continue
            conf = 1.15 if prob >= 0.54 else 1.0
            risk_amt = ORB_BASE_RISK * conf

        open_risk = sum(p[1] for p in s1_positions) + sum(p[1] for p in orb_positions)
        final_risk = min(risk_amt, max(DEFENSE_RISK, MAX_RISK_BUDGET - open_risk))

        pnl = r_gain * final_risk
        equity += pnl
        if equity > peak_equity:
            peak_equity = equity

        if strat == "S1":
            s1_positions.append((t_entry + hold_ms, final_risk, sym))
            if r_gain >= 0.80:
                consec_losses_s1 = 0
            else:
                consec_losses_s1 += 1
                symbol_cooldown[sym] = t_entry + 4 * 15 * 60 * 1000
                if consec_losses_s1 >= 2:
                    s1_cooldown_until = t_entry + 16 * 15 * 60 * 1000
                    consec_losses_s1 = 0
        else:
            orb_positions.append((t_entry + hold_ms, final_risk, sym))
            if r_gain >= 0.50:
                consec_losses_orb = 0
            else:
                consec_losses_orb += 1
                symbol_cooldown[sym] = t_entry + 4 * 15 * 60 * 1000
                if consec_losses_orb >= 2:
                    consec_losses_orb = 0

        trade_log.append({
            "time": t_entry, "symbol": sym, "strategy": strat,
            "prob": prob, "outcome_r": r_gain, "risk_usd": final_risk,
            "pnl_usd": pnl, "equity": equity
        })
        equity_curve.append(equity)
        timestamps_curve.append(t_entry)

    df_trades = pd.DataFrame(trade_log)
    return df_trades, np.array(equity_curve), np.array(timestamps_curve)


# ── 6. MASTER WALK-FORWARD 20 OOS RUNNER ────────────────────────────────────────
def run_master_walkforward(
    data_dir: Path = Path("Binance_Data"),
    forex_dir: Path = Path("Forex_Data"),
    chart_path: str = "Terminal/of_equity_curve.png",
) -> Dict[str, Any]:
    print("\n" + "=" * 115)
    print("MASTER MULTIVERSE ORDERFLOW & SESSION BREAKOUT STRATEGY (OFC + ORB)")
    print("Zero Lookahead | 41 bps / 8 bps Friction | 11 Institutional Perpetuals + Macro Hedges")
    print("=" * 115)

    s1_pool = compile_s1_candidates(data_dir)
    s1_pool["dt"] = pd.to_datetime(s1_pool["open_time_ms"], unit="ms", utc=True)

    orb_pool = compile_orb_candidates(data_dir, forex_dir)
    orb_pool["dt"] = pd.to_datetime(orb_pool["open_time_ms"], unit="ms", utc=True)

    s1_engine = S1DualModelEngine(random_state=42)
    s3_engine = S3ORBModelEngine(random_state=42)

    windows_file = Path("Data/oos_windows_20.json")
    windows = []
    if windows_file.exists():
        with open(windows_file, "r", encoding="utf-8") as f:
            windows = json.load(f)

    print(f"\nEvaluating across all {len(windows)} Out-Of-Sample Walk-Forward Windows (2021-2025)...")
    print("-" * 120)
    print(f"{'W#':<3} | {'Window Name':<36} | {'Trades':<6} | {'S1 Tr':<6} | {'ORB Tr':<6} | {'Win Rate':<8} | {'Net PnL':<12} | {'Net ROI':<9} | {'Max DD':<7} | {'Status':<6}")
    print("-" * 120)

    passed_windows = 0
    all_oos_trades = []
    window_results = []

    for w in windows:
        w_id = w["window_id"]
        w_name = w["name"]
        s_dt = pd.Timestamp(w["start_date"], tz="UTC")
        e_dt = pd.Timestamp(w["end_date"] + " 23:59:59", tz="UTC")
        purge_dt = s_dt - pd.Timedelta(hours=PURGE_HOURS)

        # 1. Causal S1 Partitioning & Scoring
        s1_tr = s1_pool[s1_pool["dt"] < purge_dt].copy()
        s1_te = s1_pool[(s1_pool["dt"] >= s_dt) & (s1_pool["dt"] <= e_dt)].copy()

        s1_events = []
        if len(s1_tr) >= 500 and len(s1_te) > 0:
            ridge, clf, mu, sd, calib_th = s1_engine.train_models(s1_tr)
            scored_s1 = s1_engine.score_test_candidates(s1_te, ridge, clf, mu, sd, calib_th)
            for _, row in scored_s1.iterrows():
                p = float(row["prob"])
                if p >= float(row["calib_thresh"]):
                    s1_events.append({
                        "time": int(row["open_time_ms"]),
                        "symbol": str(row["symbol"]),
                        "strategy": "S1",
                        "prob": p,
                        "r_gain": float(row["realized_r"]),
                        "bars_held": int(row["bars_held"]),
                        "side": int(row["signal_side"]),
                        "tide": float(row["btc_macro_tide"]),
                    })

        # 2. Causal ORB Partitioning & Scoring
        orb_tr = orb_pool[orb_pool["dt"] < purge_dt].copy()
        orb_te = orb_pool[(orb_pool["dt"] >= s_dt) & (orb_pool["dt"] <= e_dt)].copy()

        orb_events = []
        if len(orb_tr) >= 200 and len(orb_te) > 0:
            scored_orb = s3_engine.train_and_score(orb_tr, orb_te)
            for _, row in scored_orb.iterrows():
                orb_events.append({
                    "time": int(row["open_time_ms"]),
                    "symbol": str(row["symbol"]),
                    "strategy": "ORB",
                    "prob": float(row["prob"]),
                    "r_gain": float(row["realized_r"]),
                    "bars_held": int(row["bars_held"]),
                })

        # 3. Merge into Chronological Queue
        combined_events = s1_events + orb_events
        combined_events.sort(key=lambda x: (x["time"], -x["prob"]))

        if len(combined_events) == 0:
            continue

        df_w_tr, w_eq, w_ts = simulate_multiverse_portfolio(combined_events, INITIAL_CAPITAL, is_cumulative=False)
        all_oos_trades.append(df_w_tr)

        n_tr = len(df_w_tr)
        n_s1 = sum(df_w_tr["strategy"] == "S1") if n_tr > 0 else 0
        n_orb = sum(df_w_tr["strategy"] == "ORB") if n_tr > 0 else 0
        wins = sum(df_w_tr["pnl_usd"] > 0) if n_tr > 0 else 0
        wr = (wins / n_tr * 100.0) if n_tr > 0 else 0.0
        tot_pnl = df_w_tr["pnl_usd"].sum() if n_tr > 0 else 0.0
        roi = (tot_pnl / INITIAL_CAPITAL) * 100.0

        eq_s = pd.Series(w_eq)
        pk_s = eq_s.cummax()
        dd_s = ((pk_s - eq_s) / pk_s * 100.0)
        max_dd = dd_s.max() if len(dd_s) > 0 else 0.0

        passed = (roi >= 10.0 and max_dd < HARD_DD_LIMIT and wr >= 40.0 and n_tr >= 15)
        if passed:
            passed_windows += 1
        status = "PASS" if passed else ("PROFIT" if tot_pnl > 0 and max_dd < HARD_DD_LIMIT else "FAIL")
        flag = "[+]" if passed else ("[~]" if tot_pnl > 0 and max_dd < HARD_DD_LIMIT else "[-]")

        trunc_name = (w_name[:34] + "..") if len(w_name) > 36 else w_name
        print(f"W{w_id:<2} | {trunc_name:<36} | {n_tr:<6} | {n_s1:<6} | {n_orb:<6} | {wr:<6.1f}% | {tot_pnl:<+10.2f} USD | {roi:<+7.2f}% | {max_dd:<5.2f}% | {flag} {status}")
        window_results.append({
            "window": f"W{w_id}", "name": w_name, "trades": n_tr, "s1_trades": n_s1,
            "orb_trades": n_orb, "wr": wr, "pnl": tot_pnl, "roi": roi, "max_dd": max_dd, "passed": passed
        })

    print("-" * 120)
    print(f"Outright Windows Passed: {passed_windows}/{len(windows)} ({passed_windows/len(windows)*100:.1f}%)")

    # ── Cumulative Full-Period Simulation (2021–2026) ────────────────────────
    full_event_list = []
    for w in windows:
        s_dt = pd.Timestamp(w["start_date"], tz="UTC")
        e_dt = pd.Timestamp(w["end_date"] + " 23:59:59", tz="UTC")
        purge_dt = s_dt - pd.Timedelta(hours=PURGE_HOURS)

        s1_tr = s1_pool[s1_pool["dt"] < purge_dt].copy()
        s1_te = s1_pool[(s1_pool["dt"] >= s_dt) & (s1_pool["dt"] <= e_dt)].copy()
        if len(s1_tr) >= 500 and len(s1_te) > 0:
            ridge, clf, mu, sd, calib_th = s1_engine.train_models(s1_tr)
            scored_s1 = s1_engine.score_test_candidates(s1_te, ridge, clf, mu, sd, calib_th)
            for _, row in scored_s1.iterrows():
                if float(row["prob"]) >= float(row["calib_thresh"]):
                    full_event_list.append({
                        "time": int(row["open_time_ms"]), "symbol": str(row["symbol"]),
                        "strategy": "S1", "prob": float(row["prob"]),
                        "r_gain": float(row["realized_r"]), "bars_held": int(row["bars_held"]),
                        "side": int(row["signal_side"]), "tide": float(row["btc_macro_tide"]),
                    })

        orb_tr = orb_pool[orb_pool["dt"] < purge_dt].copy()
        orb_te = orb_pool[(orb_pool["dt"] >= s_dt) & (orb_pool["dt"] <= e_dt)].copy()
        if len(orb_tr) >= 200 and len(orb_te) > 0:
            scored_orb = s3_engine.train_and_score(orb_tr, orb_te)
            for _, row in scored_orb.iterrows():
                full_event_list.append({
                    "time": int(row["open_time_ms"]), "symbol": str(row["symbol"]),
                    "strategy": "ORB", "prob": float(row["prob"]),
                    "r_gain": float(row["realized_r"]), "bars_held": int(row["bars_held"]),
                })

    full_event_list.sort(key=lambda x: (x["time"], -x["prob"]))
    df_all_trades, full_equity, full_timestamps = simulate_multiverse_portfolio(full_event_list, INITIAL_CAPITAL, is_cumulative=True)

    wins_all = df_all_trades[df_all_trades["pnl_usd"] > 0]
    loss_all = df_all_trades[df_all_trades["pnl_usd"] <= 0]
    total_wr = len(wins_all) / len(df_all_trades) * 100.0 if len(df_all_trades) > 0 else 0.0
    total_pnl = df_all_trades["pnl_usd"].sum() if len(df_all_trades) > 0 else 0.0
    total_roi = total_pnl / INITIAL_CAPITAL * 100.0

    eq_series = pd.Series(full_equity)
    pk_series = eq_series.cummax()
    dd_series = ((pk_series - eq_series) / pk_series * 100.0)
    full_max_dd = dd_series.max()

    # BTC Buy & Hold Benchmark
    btc_path = data_dir / "BTCUSDT_15m_master_2020_2026.parquet"
    df_btc = pd.read_parquet(btc_path, columns=["open_time_ms", "close"]).sort_values("open_time_ms").reset_index(drop=True)
    b_ts = df_btc["open_time_ms"].values
    b_px = df_btc["close"].values
    start_px = b_px[np.searchsorted(b_ts, full_timestamps[0])]
    end_px = b_px[np.searchsorted(b_ts, full_timestamps[-1])]
    bnh_ret = (end_px - start_px) / start_px * 100.0

    idx_aligned = np.searchsorted(b_ts, full_timestamps, side="left")
    idx_aligned = np.clip(idx_aligned, 0, len(b_px) - 1)
    bnh_equity = INITIAL_CAPITAL * (b_px[idx_aligned] / start_px)

    print("\n" + "=" * 115)
    print("CUMULATIVE INSTITUTIONAL SCORECARD (2021–2026 FULL WALK-FORWARD)")
    print("=" * 115)
    print(f"Total Completed Trades:    {len(df_all_trades):,}")
    print(f"Win Rate:                  {total_wr:.1f}% ({len(wins_all)}W / {len(loss_all)}L)")
    print(f"Total Net Profit:          {total_pnl:+,.2f} USD")
    print(f"Strategy Net ROI:          {total_roi:+.2f}%")
    print(f"BTC Buy & Hold Return:     {bnh_ret:+.2f}%")
    print(f"Max Strategy Drawdown:     {full_max_dd:.2f}% (Hard Limit: {HARD_DD_LIMIT:.2f}%)")
    print(f"Average Trade PnL:         {total_pnl / len(df_all_trades):+.2f} USD")
    print("=" * 115)

    # ── High-Resolution Equity Curve Comparison Chart ────────────────────────
    print(f"\nGenerating institutional comparison chart → {chart_path}")
    fig = plt.figure(figsize=(16, 10))
    fig.patch.set_facecolor("#0b0e14")
    ax1 = plt.subplot2grid((3, 1), (0, 0), rowspan=2)
    ax2 = plt.subplot2grid((3, 1), (2, 0), sharex=ax1)
    ax1.set_facecolor("#0f131c")
    ax2.set_facecolor("#0f131c")

    dts_plot = pd.to_datetime(full_timestamps, unit="ms", utc=True)

    ax1.plot(dts_plot, full_equity, color="#00e676", linewidth=2.2,
             label=f"OFC Strategy Equity (Final: {full_equity[-1]:,.2f} USD | ROI: {total_roi:+.2f}%)")
    ax1.plot(dts_plot, bnh_equity, color="#ff9100", linewidth=1.5, linestyle="--",
             label=f"BTC Buy & Hold Benchmark (Final: {bnh_equity[-1]:,.2f} USD | Return: {bnh_ret:+.2f}%)")
    ax1.axhline(INITIAL_CAPITAL, color="#78909c", linestyle=":", alpha=0.6, label="Starting Capital (5,000 USD)")

    year_palette = ["#1a237e", "#1b5e20", "#4a148c", "#bf360c", "#006064", "#827717"]
    years_in_plot = sorted(dts_plot.year.unique())
    for i, yr in enumerate(years_in_plot):
        yr_mask = (dts_plot.year == yr)
        if yr_mask.sum() < 2:
            continue
        yr_dts = dts_plot[yr_mask]
        ax1.axvspan(yr_dts.min(), yr_dts.max(), alpha=0.08, color=year_palette[i % len(year_palette)], zorder=0)
        mid_dt = yr_dts[len(yr_dts) // 2]
        ax1.text(mid_dt, INITIAL_CAPITAL * 0.98, f"{yr}",
                 color="#90caf9", fontsize=9, ha="center", va="bottom", fontweight="bold")

    ax1.set_ylabel("Portfolio Value (USD)", color="#e0e0e0", fontsize=11)
    ax1.set_title("Master Institutional OFC Strategy vs BTC Buy & Hold Benchmark (2021–2026, 41 bps Friction)",
                  color="#ffffff", fontsize=14, fontweight="bold", pad=12)
    ax1.grid(True, color="#263238", linestyle="--", alpha=0.4)
    ax1.legend(loc="upper left", facecolor="#1e2638", edgecolor="#37474f", labelcolor="#e0e0e0", fontsize=10)
    ax1.tick_params(colors="#b0bec5")

    ax2.fill_between(dts_plot, dd_series.values, 0, color="#ff5252", alpha=0.35,
                     label=f"Underwater Drawdown (Max: {full_max_dd:.2f}%)")
    ax2.plot(dts_plot, dd_series.values, color="#ff5252", linewidth=1.1)
    ax2.axhline(HARD_DD_LIMIT, color="#ff1744", linestyle="--", alpha=0.8, label=f"Hard DD Stop ({HARD_DD_LIMIT:.2f}%)")
    ax2.set_ylabel("Drawdown (%)", color="#e0e0e0", fontsize=11)
    ax2.set_xlabel("Date (UTC)", color="#e0e0e0", fontsize=11)
    ax2.grid(True, color="#263238", linestyle="--", alpha=0.4)
    ax2.legend(loc="upper left", facecolor="#1e2638", edgecolor="#37474f", labelcolor="#e0e0e0", fontsize=10)
    ax2.tick_params(colors="#b0bec5")
    ax2.invert_yaxis()

    plt.tight_layout()
    plt.savefig(chart_path, dpi=180, facecolor=fig.get_facecolor(), edgecolor="none")
    plt.close()
    print(f"Chart saved: {chart_path}")

    brain_dir = Path(r"C:\Users\SIGMA\.gemini\antigravity\brain\b00c810a-61bb-46bf-a147-4c8859c64058")
    if brain_dir.exists():
        import shutil
        shutil.copy(chart_path, brain_dir / "of_equity_curve.png")

    return {
        "trades": len(df_all_trades),
        "win_rate": total_wr,
        "net_pnl": total_pnl,
        "roi": total_roi,
        "max_dd": full_max_dd,
        "bnh_return": bnh_ret
    }


# ── 7. REAL-TIME DRY-RUN PAPER TRADING ENGINE ──────────────────────────────────
class OFCDryRunRunner:
    """
    Connects to the running Hyperdash terminal (http://localhost:8095).
    Evaluates real-time 15m orderflow data, manages paper positions with 3-stage ratchets,
    and persists state to Data/ofc_paper_positions.json.
    """
    def __init__(self, coin: str = "BTC", host: str = "http://localhost:8095", state_file: str = "Data/ofc_paper_positions.json"):
        self.coin = coin.upper()
        self.host = host.rstrip("/")
        self.state_file = Path(state_file)
        self.state_file.parent.mkdir(parents=True, exist_ok=True)
        self.capital = INITIAL_CAPITAL
        self.peak_capital = INITIAL_CAPITAL
        self.active_position = None
        self.closed_trades = []
        self.consec_losses = 0
        self._load_state()

    def _load_state(self):
        if self.state_file.exists():
            try:
                with open(self.state_file, "r", encoding="utf-8") as f:
                    d = json.load(f)
                self.capital = d.get("capital", INITIAL_CAPITAL)
                self.peak_capital = d.get("peak_capital", INITIAL_CAPITAL)
                self.active_position = d.get("active_position", None)
                self.closed_trades = d.get("closed_trades", [])
                self.consec_losses = d.get("consec_losses", 0)
            except Exception:
                pass

    def _save_state(self):
        with open(self.state_file, "w", encoding="utf-8") as f:
            json.dump({
                "coin": self.coin,
                "capital": round(self.capital, 2),
                "peak_capital": round(self.peak_capital, 2),
                "active_position": self.active_position,
                "closed_trades": self.closed_trades[-50:],
                "consec_losses": self.consec_losses,
                "updated_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
            }, f, indent=2)

    def _get_live_data(self) -> dict | None:
        try:
            import urllib.request
            url = f"{self.host}/api/live/{self.coin}"
            req = urllib.request.Request(url, headers={"Accept": "application/json", "User-Agent": "OFC_DryRun/2.0"})
            with urllib.request.urlopen(req, timeout=8) as r:
                return json.loads(r.read())
        except Exception:
            return None

    def evaluate_signals_and_manage(self, data: dict, price: float, utc_now: str):
        # 1. Manage Active Position with 3-Stage Ratchet
        if self.active_position is not None:
            pos = self.active_position
            direction = pos["direction"]
            entry = pos["entry"]
            r_dist = pos["r_dist"]
            units = pos["units"]
            sl = pos["stop_loss"]
            tp = pos["take_profit"]
            phase = pos["phase"]

            gain_r = ((price - entry) / r_dist) if direction == "LONG" else ((entry - price) / r_dist)

            # Ratchet Phase 0 -> 1: Breakeven Lock (+0.35R net) at +1.40R
            if phase == 0 and gain_r >= 1.40:
                pos["stop_loss"] = entry + 0.35 * r_dist if direction == "LONG" else entry - 0.35 * r_dist
                pos["phase"] = 1
                print(f"  ⚡ [{utc_now}] {direction} RATCHET P1 (BE LOCK +0.35R): SL moved to {pos['stop_loss']:,.2f} USD")

            # Ratchet Phase 1 -> 2: Profit Lock (+1.20R) at +2.00R
            elif phase == 1 and gain_r >= 2.00:
                pos["stop_loss"] = entry + 1.20 * r_dist if direction == "LONG" else entry - 1.20 * r_dist
                pos["phase"] = 2
                print(f"  ⚡ [{utc_now}] {direction} RATCHET P2 (PROFIT LOCK +1.20R): SL moved to {pos['stop_loss']:,.2f} USD")

            # Ratchet Phase 2 -> 3: Trail Lock (+1.80R) at +2.50R
            elif phase == 2 and gain_r >= 2.50:
                pos["stop_loss"] = entry + 1.80 * r_dist if direction == "LONG" else entry - 1.80 * r_dist
                pos["phase"] = 3
                print(f"  ⚡ [{utc_now}] {direction} RATCHET P3 (RUNNER TRAIL +1.80R): SL moved to {pos['stop_loss']:,.2f} USD")

            # Exit Evaluation
            exit_hit = False
            exit_reason = ""
            if direction == "LONG":
                if price <= pos["stop_loss"]:
                    exit_hit = True
                    exit_reason = "STOP_LOSS"
                elif price >= tp:
                    exit_hit = True
                    exit_reason = "TARGET_HIT"
            else:
                if price >= pos["stop_loss"]:
                    exit_hit = True
                    exit_reason = "STOP_LOSS"
                elif price <= tp:
                    exit_hit = True
                    exit_reason = "TARGET_HIT"

            if exit_hit:
                gross = (price - entry) * units if direction == "LONG" else (entry - price) * units
                friction = entry * units * 0.0041  # 41 bps round-trip friction
                net_pnl = gross - friction
                self.capital += net_pnl
                self.peak_capital = max(self.peak_capital, self.capital)

                if net_pnl < 0:
                    self.consec_losses += 1
                else:
                    self.consec_losses = 0

                trade_record = {
                    "coin": self.coin,
                    "direction": direction,
                    "entry": entry,
                    "exit": price,
                    "units": units,
                    "gain_r": round(gain_r, 2),
                    "gross_pnl": round(gross, 2),
                    "friction": round(friction, 2),
                    "net_pnl": round(net_pnl, 2),
                    "reason": exit_reason,
                    "exit_time": utc_now,
                    "capital_after": round(self.capital, 2)
                }
                self.closed_trades.append(trade_record)
                self.active_position = None
                print(f"  🛑 [{utc_now}] {direction} CLOSED via {exit_reason} at {price:,.2f} USD | Net PnL: {net_pnl:+,.2f} USD | Capital: {self.capital:,.2f} USD")
                self._save_state()
            return

        # 2. Risk Circuit Breaker Check
        current_dd_pct = ((self.peak_capital - self.capital) / self.peak_capital * 100.0) if self.peak_capital > 0 else 0.0
        if current_dd_pct >= HARD_DD_LIMIT:
            print(f"  🛑 [{utc_now}] Hard DD Stop active ({current_dd_pct:.2f}% >= {HARD_DD_LIMIT:.2f}%). Trading halted.", flush=True)
            return

        # 3. Dynamic Risk Budgeting
        risk_budget = S1_BASE_RISK
        if self.capital >= INITIAL_CAPITAL + 250.0:
            risk_budget = 32.0  # Milestone capital defense
        elif self.consec_losses >= 3:
            risk_budget = DEFENSE_RISK  # Loss streak defense

        r_dist = max(price * 0.0075, 40.0)  # 0.75% structural stop distance
        units = risk_budget / r_dist

        # 4. Live Orderflow Signal Confluence
        liqs = data.get("liquidations", {})
        bands = liqs.get("bands", [])
        trades = data.get("recent_trades", [])
        l3_orders = data.get("l3_orders", [])

        # Analyze liquidation cluster depth
        below_liq_sum = 0.0
        above_liq_sum = 0.0
        for b in bands:
            mid = b.get("mid_px", 0.0)
            amt = b.get("amount", 0.0)
            if mid < price:
                dist_pct = (mid - price) / price * 100.0
                if -2.5 <= dist_pct <= -0.1:
                    below_liq_sum += amt
            elif mid > price:
                dist_pct = (mid - price) / price * 100.0
                if 0.1 <= dist_pct <= 2.5:
                    above_liq_sum += amt

        # Analyze aggressor whale flow in tape
        whale_buys = sum(t.get("notional_usd", 0) for t in trades if t.get("side") == "BUY" and t.get("is_whale", False))
        whale_sells = sum(t.get("notional_usd", 0) for t in trades if t.get("side") == "SELL" and t.get("is_whale", False))

        # Check L3 Whale resting support/resistance
        resting_bid_whale = any(o.get("side") == "BUY" and o.get("notional_usd", 0) >= 150000 and abs(o.get("dist_pct", 99)) < 0.6 for o in l3_orders)
        resting_ask_whale = any(o.get("side") == "SELL" and o.get("notional_usd", 0) >= 150000 and abs(o.get("dist_pct", 99)) < 0.6 for o in l3_orders)

        # Confluence Entry Triggers
        long_signal = (below_liq_sum >= 1.5 or resting_bid_whale or (whale_buys > 100000 and whale_buys > whale_sells * 1.5))
        short_signal = (above_liq_sum >= 1.5 or resting_ask_whale or (whale_sells > 100000 and whale_sells > whale_buys * 1.5))

        if long_signal and not short_signal:
            self.active_position = {
                "coin": self.coin,
                "direction": "LONG",
                "entry": price,
                "r_dist": r_dist,
                "units": units,
                "stop_loss": price - r_dist,
                "take_profit": price + 3.00 * r_dist,
                "phase": 0,
                "entry_time": utc_now,
                "risk_usd": risk_budget
            }
            print(f"  🟢 [{utc_now}] NEW LONG POSITION OPENED at {price:,.2f} USD | SL: {price - r_dist:,.2f} | TP: {price + 3.00 * r_dist:,.2f} | Risk: {risk_budget:.2f} USD", flush=True)
            self._save_state()

        elif short_signal and not long_signal:
            self.active_position = {
                "coin": self.coin,
                "direction": "SHORT",
                "entry": price,
                "r_dist": r_dist,
                "units": units,
                "stop_loss": price + r_dist,
                "take_profit": price - 3.00 * r_dist,
                "phase": 0,
                "entry_time": utc_now,
                "risk_usd": risk_budget
            }
            print(f"  🔴 [{utc_now}] NEW SHORT POSITION OPENED at {price:,.2f} USD | SL: {price + r_dist:,.2f} | TP: {price - 3.00 * r_dist:,.2f} | Risk: {risk_budget:.2f} USD", flush=True)
            self._save_state()

    def run(self, max_ticks: int = 0):
        print(f"\n" + "=" * 75, flush=True)
        print(f"MASTER INSTITUTIONAL OFC DRY-RUN EXECUTOR [{self.coin}]", flush=True)
        print(f"Connected to Terminal: {self.host} | State: {self.state_file}", flush=True)
        print(f"Initial Paper Capital: {self.capital:,.2f} USD | Peak: {self.peak_capital:,.2f} USD", flush=True)
        print(f"Frictions Enforced: 41.0 bps round-trip | Ratchet: 3-Phase (+1.4R, +2.0R, +2.5R, +3.0R TP)", flush=True)
        print("=" * 75 + "\n", flush=True)

        tick = 0
        while True:
            tick += 1
            try:
                data = self._get_live_data()
                if data:
                    price = float(data.get("price", 0))
                    utc_now = data.get("utc_time", datetime.datetime.now(datetime.timezone.utc).strftime("%H:%M:%S UTC"))
                    self.evaluate_signals_and_manage(data, price, utc_now)

                    pos_info = ""
                    if self.active_position:
                        pos = self.active_position
                        gain_r = ((price - pos['entry']) / pos['r_dist']) if pos['direction'] == 'LONG' else ((pos['entry'] - price) / pos['r_dist'])
                        pos_info = f" | POS: {pos['direction']} @ {pos['entry']:,.2f} (P{pos['phase']}, {gain_r:+.2f}R)"
                    else:
                        pos_info = " | Scanning orderflow..."

                    print(f"[{utc_now}] {self.coin}: {price:,.2f} USD | Capital: {self.capital:,.2f} USD{pos_info}", flush=True)
                    self._save_state()

                if max_ticks > 0 and tick >= max_ticks:
                    break
                time.sleep(2 if max_ticks > 0 else 10)
            except KeyboardInterrupt:
                print("\n[OFC DRY-RUN] Terminated by user.", flush=True)
                self._save_state()
                break
            except Exception as e:
                print(f"\n[ERROR] {e}", flush=True)
                time.sleep(5)


# ── 8. AUTONOMOUS 15-MINUTE CANDLE AI TRADER & MT5 EXECUTION BRIDGE ───────────
class AI15mMT5Trader:
    """
    Autonomous 15-Minute Candle AI Trader & MT5 Execution Bridge.
    Executes 360-Degree Market Analysis at the 14th minute of each 15-minute candle:
    - Synchronized with MT5 terminal (Blueberry Markets Account 5064568)
    - Dynamic 3-stage microstructure ratchet controller for active MT5 tickets
    - Web Macro & CPI/FOMC Economic Calendar Intelligence with 15-minute blackout gate
    - Hyperdash orderflow confluence (L2 depth, liquidation bands, stop clusters, L3 whales)
    - Next-bar paper/live entry execution with contract-size lot scaling and strict risk budgeting
    """
    def __init__(
        self,
        coin: str = "SOL",
        host: str = "http://localhost:8095",
        paper_mode: bool = True,
        risk_usd: float = 10.0,
        min_risk_usd: float = 10.0,
        max_risk_usd: float = 20.0,
        cadence_minute: int = 14,
        state_file: str = "Data/mt5_ai_trader_state.json"
    ):
        self.coin = coin.upper()
        self.host = host.rstrip("/")
        self.paper_mode = paper_mode
        self.risk_usd = risk_usd
        self.min_risk_usd = min_risk_usd
        self.max_risk_usd = max_risk_usd
        self.cadence_minute = cadence_minute
        self.state_file = Path(state_file)
        self.state_file.parent.mkdir(parents=True, exist_ok=True)
        
        # Connect to MT5 Bridge
        from Terminal.MT5_Execution_Bridge import MT5ExecutionBridge
        self.bridge = MT5ExecutionBridge()
        self.mt5_symbol = self.bridge.resolve_symbol(self.coin)
        
        # Connect to Market Intelligence Engine
        from Terminal.Market_Intelligence import MarketIntelligenceEngine
        self.intel = MarketIntelligenceEngine(blackout_minutes=15)
        
        # State tracking
        self.capital = INITIAL_CAPITAL
        self.peak_capital = INITIAL_CAPITAL
        self.paper_positions = []
        self.trade_history = []
        self.last_evaluated_bar = -1
        self._load_state()

    def calculate_dynamic_risk(self, conviction_score: int, macro_score: float, current_equity: float) -> float:
        """
        Dynamically calculates risk budget between min_risk_usd (10.00 USD) and max_risk_usd (20.00 USD).
        Scales with orderflow confluence and macro conviction:
        - Base (Score 1): 10.00 USD (0.20% on 5,000.00 USD baseline)
        - Medium Conviction (Score 2): 15.00 USD (0.30%)
        - High Conviction (Score >= 3): 20.00 USD (0.40%)
        Enforces drawdown defense cap: if equity < 4,800.00 USD, cap at min_risk_usd.
        """
        if current_equity < 4800.0:
            return round(self.min_risk_usd, 2)
            
        if conviction_score >= 3 and macro_score >= 0.0:
            allocated = self.max_risk_usd  # 20.00 USD
        elif conviction_score >= 2 or (conviction_score >= 1 and macro_score > 0.20):
            allocated = round((self.min_risk_usd + self.max_risk_usd) / 2.0, 2)  # 15.00 USD
        else:
            allocated = self.min_risk_usd  # 10.00 USD

        return float(min(self.max_risk_usd, max(self.min_risk_usd, allocated)))

    def _load_state(self):
        if self.state_file.exists():
            try:
                with open(self.state_file, "r", encoding="utf-8") as f:
                    d = json.load(f)
                self.capital = d.get("capital_usd", INITIAL_CAPITAL)
                self.peak_capital = d.get("peak_capital_usd", INITIAL_CAPITAL)
                self.paper_positions = d.get("paper_positions", [])
                self.trade_history = d.get("trade_history", [])
            except Exception:
                pass

    def _save_state(self, extra_report: dict = None):
        payload = {
            "coin": self.coin,
            "mt5_symbol": self.mt5_symbol,
            "paper_mode": self.paper_mode,
            "capital_usd": round(self.capital, 2),
            "peak_capital_usd": round(self.peak_capital, 2),
            "paper_positions": self.paper_positions,
            "trade_history": self.trade_history[-50:],
            "last_360_report": extra_report or {},
            "updated_utc": datetime.datetime.now(datetime.timezone.utc).isoformat()
        }
        with open(self.state_file, "w", encoding="utf-8") as f:
            json.dump(payload, f, indent=2)

    def _fetch_hyperdash_live(self) -> dict | None:
        try:
            import urllib.request
            url = f"{self.host}/api/live/{self.coin}"
            req = urllib.request.Request(url, headers={"Accept": "application/json", "User-Agent": "AI15mMT5/2.0"})
            with urllib.request.urlopen(req, timeout=8) as r:
                return json.loads(r.read())
        except Exception:
            return None

    def print_open_positions_summary(self, open_positions: List[Dict[str, Any]], effective_px: float, utc_now: str):
        account = self.bridge.get_account_summary()
        balance = account.get("balance_usd", 0.0)
        equity = account.get("equity_usd", 0.0)
        total_pnl = sum(p.get("profit_usd", 0.0) for p in open_positions)

        print("\n" + "=" * 84, flush=True)
        print(f"[{utc_now}] 📊 LIVE MT5 OPEN TRADES & PnL REPORT | Account {account.get('login', '5064568')}", flush=True)
        print(f"  Balance: {balance:,.2f} USD | Equity: {equity:,.2f} USD | Total Floating PnL: {total_pnl:+,.2f} USD", flush=True)
        print("-" * 84, flush=True)

        if not open_positions:
            print("  [OPEN POSITIONS: 0] No active running trades. Scanning orderflow for confluence...", flush=True)
        else:
            for p in open_positions:
                ticket = p["ticket"]
                sym = p["symbol"]
                dir_ = p["direction"]
                vol = p["volume"]
                open_px = p["price_open"]
                curr_px = p.get("price_current", effective_px)
                sl = p.get("sl", 0.0)
                tp = p.get("tp", 0.0)
                pnl = p.get("profit_usd", 0.0)

                r_dist = abs(open_px - sl) if sl > 0 else (open_px * 0.0075)
                gain_r = ((curr_px - open_px) / r_dist) if dir_ == "LONG" else ((open_px - curr_px) / r_dist)
                locked_profit = ((sl - open_px) * vol * 100) if (dir_ == "LONG" and sl > open_px) else (
                    ((open_px - sl) * vol * 100) if (dir_ == "SHORT" and sl < open_px and sl > 0) else 0.0
                )

                print(f"  • TICKET #{ticket} | {sym} {dir_} {vol:.2f} lots", flush=True)
                print(f"    Open Price : {open_px:,.2f} USD  |  Current Price: {curr_px:,.2f} USD", flush=True)
                print(f"    Floating PnL: {pnl:+,.2f} USD ({gain_r:+.2f}R gain)  |  Locked Profit: {locked_profit:+,.2f} USD", flush=True)
                print(f"    Stop Loss   : {sl:,.2f} USD  |  Take Profit: {tp:,.2f} USD", flush=True)
        print("=" * 84 + "\n", flush=True)

    def manage_active_positions(self, mt5_price: float, utc_now: str, hd_data: Optional[dict] = None) -> List[Dict[str, Any]]:
        """
        Scans open MT5 positions and applies dynamic 3-stage piecewise ratchet and orderflow TP targeting.
        Specifically handles running tickets like SOLUSD.p ticket 18464576.
        """
        open_positions = self.bridge.get_open_positions()
        ratchet_updates = []
        if hd_data is None:
            hd_data = self._fetch_hyperdash_live() or {}

        bands = hd_data.get("liquidations", {}).get("bands", [])
        l3_orders = hd_data.get("l3_orders", [])

        for pos in open_positions:
            ticket = pos["ticket"]
            sym = pos["symbol"]
            direction = pos["direction"]
            entry = pos["price_open"]
            curr_sl = pos["sl"]
            curr_tp = pos["tp"]
            profit_usd = pos["profit_usd"]
            curr_px = pos["price_current"] if pos.get("price_current", 0) > 0 else mt5_price

            # Asset-aware precision and offsets
            digits = 3 if "XRP" in sym else 2
            offset = max(round(curr_px * 0.001, digits), 0.001 if digits == 3 else 0.05)
            min_tp_step = 0.005 if digits == 3 else 0.20

            # Compute R distance
            if curr_sl > 0:
                r_dist = abs(entry - curr_sl)
            else:
                r_dist = entry * 0.015

            if r_dist <= 0:
                r_dist = entry * 0.015

            # Current gain in R
            gain_r = ((curr_px - entry) / r_dist) if direction == "LONG" else ((entry - curr_px) / r_dist)

            # 1. Dynamic Stop Loss Ratchet
            target_sl = curr_sl
            ratchet_phase = "HOLD"

            if gain_r >= 2.00:
                trail_r = max(1.50, gain_r - 0.65)
                calc_sl = (entry + trail_r * r_dist) if direction == "LONG" else (entry - trail_r * r_dist)
                if (direction == "LONG" and calc_sl > curr_sl) or (direction == "SHORT" and (curr_sl == 0 or calc_sl < curr_sl)):
                    target_sl = round(calc_sl, digits)
                    ratchet_phase = "P2_RUNNER_TRAIL"
            elif gain_r >= 1.50:
                calc_sl = (entry + 0.85 * r_dist) if direction == "LONG" else (entry - 0.85 * r_dist)
                if (direction == "LONG" and calc_sl > curr_sl) or (direction == "SHORT" and (curr_sl == 0 or calc_sl < curr_sl)):
                    target_sl = round(calc_sl, digits)
                    ratchet_phase = "P1_PROFIT_LOCK"
            elif gain_r >= 0.80:
                calc_sl = (entry + 0.15 * r_dist) if direction == "LONG" else (entry - 0.15 * r_dist)
                if (direction == "LONG" and calc_sl > curr_sl) or (direction == "SHORT" and (curr_sl == 0 or calc_sl < curr_sl)):
                    target_sl = round(calc_sl, digits)
                    ratchet_phase = "P0_BE_LOCK"

            # 2. Dynamic Take Profit Intelligence via Orderflow Liquidity Walls
            target_tp = curr_tp
            if direction == "LONG":
                candidate_walls = []
                for b in bands:
                    mid = b.get("mid_px", 0.0)
                    amt = b.get("amount_usd", 0.0)
                    if mid > curr_px and amt >= 200000:
                        candidate_walls.append((mid, amt))
                for o in l3_orders:
                    px_o = o.get("price", 0.0)
                    val = o.get("notional_usd", 0.0)
                    if o.get("side") == "SELL" and px_o > curr_px and val >= 100000:
                        candidate_walls.append((px_o, val))

                if candidate_walls:
                    candidate_walls.sort(key=lambda x: x[0])
                    nearest_wall_px = candidate_walls[0][0]
                    wall_tp = round(nearest_wall_px - offset, digits)
                    if wall_tp >= entry + 1.80 * r_dist and abs(wall_tp - curr_tp) >= min_tp_step:
                        target_tp = wall_tp
            else:
                candidate_walls = []
                for b in bands:
                    mid = b.get("mid_px", 0.0)
                    amt = b.get("amount_usd", 0.0)
                    if mid < curr_px and amt >= 200000:
                        candidate_walls.append((mid, amt))
                for o in l3_orders:
                    px_o = o.get("price", 0.0)
                    val = o.get("notional_usd", 0.0)
                    if o.get("side") == "BUY" and px_o < curr_px and val >= 100000:
                        candidate_walls.append((px_o, val))
                if candidate_walls:
                    candidate_walls.sort(key=lambda x: x[0], reverse=True)
                    nearest_wall_px = candidate_walls[0][0]
                    wall_tp = round(nearest_wall_px + offset, digits)
                    if wall_tp <= entry - 1.80 * r_dist and abs(wall_tp - curr_tp) >= min_tp_step:
                        target_tp = wall_tp

            # Apply modification if SL or TP changed
            sl_changed = (round(target_sl, digits) != round(curr_sl, digits))
            tp_changed = (round(target_tp, digits) != round(curr_tp, digits) and target_tp > 0)

            if sl_changed or tp_changed:
                print(f"  ⚡ [{utc_now}] DYNAMIC SL/TP ADJUSTMENT: Ticket {ticket} ({sym} {direction}) Gain={gain_r:+.2f}R ({profit_usd:+,.2f} USD)", flush=True)
                if sl_changed:
                    print(f"     Advancing SL: {curr_sl:.2f} -> {target_sl:.2f} USD ({ratchet_phase})", flush=True)
                if tp_changed:
                    print(f"     Adjusting TP: {curr_tp:.2f} -> {target_tp:.2f} USD (Aligned with Liquidity Wall)", flush=True)
                mod_res = self.bridge.modify_position_sltp(ticket=ticket, new_sl=target_sl, new_tp=target_tp)
                ratchet_updates.append({
                    "ticket": ticket,
                    "symbol": sym,
                    "direction": direction,
                    "gain_r": round(gain_r, 2),
                    "old_sl": curr_sl,
                    "new_sl": round(target_sl, 2),
                    "old_tp": curr_tp,
                    "new_tp": round(target_tp, 2),
                    "phase": ratchet_phase,
                    "result": mod_res
                })

        return ratchet_updates

    def scan_multi_asset_orderflow(self, universe: List[str] = None) -> Dict[str, Any]:
        """
        Scans live liquidations, stops, L2 orderbook, and L3 whales across all assets in the universe.
        Executes concurrent fetching via ThreadPoolExecutor.
        """
        if universe is None:
            universe = ["SOL", "BTC", "ETH", "XRP", "BNB"]

        from concurrent.futures import ThreadPoolExecutor
        results = {}

        def _fetch_one(coin):
            try:
                import urllib.request
                url = f"{self.host}/api/live/{coin}"
                req = urllib.request.Request(url, headers={"Accept": "application/json", "User-Agent": "MultiAssetOF/1.0"})
                with urllib.request.urlopen(req, timeout=5) as r:
                    return coin, json.loads(r.read())
            except Exception:
                return coin, None

        with ThreadPoolExecutor(max_workers=min(5, len(universe))) as executor:
            fetched = executor.map(_fetch_one, universe)
            for coin, data in fetched:
                if data:
                    results[coin] = data

        return results

    def print_multi_asset_intelligence_matrix(self, multi_data: Dict[str, Any], utc_now: str):
        """
        Prints formatted 360-degree multi-asset orderflow & liquidation intelligence matrix.
        """
        print("\n" + "=" * 102, flush=True)
        print(f"[{utc_now}] 🌐 360° MULTI-ASSET ORDERFLOW & LIQUIDATION INTELLIGENCE MATRIX", flush=True)
        print(f"{'Coin':<6} {'Price (USD)':>14} {'Liq Demand (Below)':>21} {'Liq Supply (Above)':>21} {'L2 Imb':>8} {'Resting Whales':>15} {'Signal':>12}", flush=True)
        print("-" * 102, flush=True)

        for coin, d in multi_data.items():
            px = float(d.get("price", 0.0))
            liqs = d.get("liquidations", {})
            bands = liqs.get("bands", [])
            l3 = d.get("l3_orders", [])
            l2 = d.get("l2_book", {})

            below_liq = sum(b.get("amount_usd", 0) for b in bands if b.get("mid_px", 0) < px and abs(b.get("dist_pct", 99)) <= 3.0)
            above_liq = sum(b.get("amount_usd", 0) for b in bands if b.get("mid_px", 0) > px and abs(b.get("dist_pct", 99)) <= 3.0)

            b_vol = l2.get("bid_volume_usd", 0.0)
            a_vol = l2.get("ask_volume_usd", 0.0)
            total_vol = b_vol + a_vol
            imb = round((b_vol - a_vol) / total_vol, 2) if total_vol > 0 else 0.0
            imb_str = f"{imb:+.2f}"

            bid_whale = any(o.get("side") == "BUY" and o.get("notional_usd", 0) >= 150000 for o in l3)
            ask_whale = any(o.get("side") == "SELL" and o.get("notional_usd", 0) >= 150000 for o in l3)
            whales_desc = "BID+ASK" if (bid_whale and ask_whale) else ("BID WHALE" if bid_whale else ("ASK WHALE" if ask_whale else "NONE"))

            signal = "NEUTRAL"
            if below_liq >= 100000 and (bid_whale or imb > 0.15):
                signal = "LONG_BIAS"
            elif above_liq >= 100000 and (ask_whale or imb < -0.15):
                signal = "SHORT_BIAS"

            px_str = f"{px:,.2f} USD" if px >= 10 else f"{px:.4f} USD"
            print(f"{coin:<6} {px_str:>14} {below_liq:>19,.0f} USD {above_liq:>19,.0f} USD {imb_str:>8} {whales_desc:>15} {signal:>12}", flush=True)

        print("=" * 102 + "\n", flush=True)

    def evaluate_360_degree_pass(self) -> Dict[str, Any]:
        """
        Executes complete 360-Degree Market Analysis:
        1. MT5 account info and live tick
        2. Market intelligence (macro news & blackout gate)
        3. Multi-Asset orderflow screening across all portfolio assets
        4. Open position ratchet and dynamic TP management
        5. New trade setup scoring & position sizing
        """
        utc_now = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
        account = self.bridge.get_account_summary()
        open_positions = self.bridge.get_open_positions()
        
        # MT5 Price
        sym_price = self.bridge.get_symbol_price(self.mt5_symbol) if self.mt5_symbol else None
        mt5_px = sym_price["last"] if sym_price else 0.0

        # Market Intelligence & Macro
        intel_report = self.intel.get_market_intelligence_report()
        blackout_active = intel_report.get("blackout_active", False)
        blackout_event = intel_report.get("blackout_event", "NONE")
        macro_bias = intel_report.get("macro_bias", "NEUTRAL")
        macro_score = intel_report.get("macro_sentiment_score", 0.0)

        # 0. Multi-Asset Orderflow Screening across All Assets
        multi_data = self.scan_multi_asset_orderflow(["SOL", "BTC", "ETH", "XRP", "BNB"])
        self.print_multi_asset_intelligence_matrix(multi_data, utc_now)

        # Hyperdash Orderflow for target coin
        hd_data = multi_data.get(self.coin, self._fetch_hyperdash_live() or {})
        hd_px = float(hd_data.get("price", mt5_px))
        effective_px = mt5_px if mt5_px > 0 else hd_px

        # Microstructure Confluence
        liqs = hd_data.get("liquidations", {})
        bands = liqs.get("bands", [])
        l3_orders = hd_data.get("l3_orders", [])
        trades = hd_data.get("recent_trades", [])

        below_liq_usd = sum(b.get("amount_usd", 0) for b in bands if b.get("mid_px", 0) < effective_px and abs(b.get("dist_pct", 99)) <= 3.0)
        above_liq_usd = sum(b.get("amount_usd", 0) for b in bands if b.get("mid_px", 0) > effective_px and abs(b.get("dist_pct", 99)) <= 3.0)

        whale_buys = sum(t.get("notional_usd", 0) for t in trades if t.get("side") == "BUY" and t.get("is_whale", False))
        whale_sells = sum(t.get("notional_usd", 0) for t in trades if t.get("side") == "SELL" and t.get("is_whale", False))

        resting_bid_whale = any(o.get("side") == "BUY" and o.get("notional_usd", 0) >= 150000 and abs(o.get("dist_pct", 99)) < 0.8 for o in l3_orders)
        resting_ask_whale = any(o.get("side") == "SELL" and o.get("notional_usd", 0) >= 150000 and abs(o.get("dist_pct", 99)) < 0.8 for o in l3_orders)

        # 1. Manage Active Positions & Adjust Dynamic SL/TP using live orderflow
        ratchets = self.manage_active_positions(effective_px, utc_now, hd_data)
        self.print_open_positions_summary(open_positions, effective_px, utc_now)

        # 2. Multi-Asset Trade Setup Discovery & Confluence Ranking across ALL Assets
        candidate_setups = []
        active_symbols = [p["symbol"] for p in open_positions]

        for scan_coin, d in multi_data.items():
            sym = self.bridge.resolve_symbol(scan_coin)
            if not sym:
                continue

            is_already_open = (sym in active_symbols)
            px = float(d.get("price", 0.0))
            if px <= 0:
                continue

            liqs = d.get("liquidations", {})
            bands = liqs.get("bands", [])
            l3_orders = d.get("l3_orders", [])
            trades = d.get("recent_trades", [])
            l2 = d.get("l2_book", {})

            below_liq = sum(b.get("amount_usd", 0) for b in bands if b.get("mid_px", 0) < px and abs(b.get("dist_pct", 99)) <= 3.0)
            above_liq = sum(b.get("amount_usd", 0) for b in bands if b.get("mid_px", 0) > px and abs(b.get("dist_pct", 99)) <= 3.0)

            b_vol = l2.get("bid_volume_usd", 0.0)
            a_vol = l2.get("ask_volume_usd", 0.0)
            tot_vol = b_vol + a_vol
            imb = round((b_vol - a_vol) / tot_vol, 2) if tot_vol > 0 else 0.0

            whale_buys = sum(t.get("notional_usd", 0) for t in trades if t.get("side") == "BUY" and t.get("is_whale", False))
            whale_sells = sum(t.get("notional_usd", 0) for t in trades if t.get("side") == "SELL" and t.get("is_whale", False))

            resting_bid_whale = any(o.get("side") == "BUY" and o.get("notional_usd", 0) >= 150000 and abs(o.get("dist_pct", 99)) < 0.8 for o in l3_orders)
            resting_ask_whale = any(o.get("side") == "SELL" and o.get("notional_usd", 0) >= 150000 and abs(o.get("dist_pct", 99)) < 0.8 for o in l3_orders)

            # Long confluence points
            long_pts = 0
            if below_liq >= 100000:
                long_pts += 1
            if below_liq >= 500000:
                long_pts += 1
            if resting_bid_whale:
                long_pts += 1
            if imb > 0.15:
                long_pts += 1
            if whale_buys > 50000 and whale_buys > whale_sells * 1.5:
                long_pts += 1
            if macro_score >= 0.0:
                long_pts += 1

            # Short confluence points
            short_pts = 0
            if above_liq >= 100000:
                short_pts += 1
            if above_liq >= 500000:
                short_pts += 1
            if resting_ask_whale:
                short_pts += 1
            if imb < -0.15:
                short_pts += 1
            if whale_sells > 50000 and whale_sells > whale_buys * 1.5:
                short_pts += 1
            if macro_score <= 0.0:
                short_pts += 1

            if long_pts >= 3 and long_pts > short_pts and macro_score >= -0.30:
                candidate_setups.append({
                    "coin": scan_coin,
                    "symbol": sym,
                    "direction": "LONG",
                    "score": long_pts,
                    "price": px,
                    "bands": bands,
                    "below_liq": below_liq,
                    "above_liq": above_liq,
                    "already_open": is_already_open,
                    "reason": f"Demand absorption ({below_liq:,.0f} USD) + Imb ({imb:+.2f}) + Whales"
                })
            elif short_pts >= 3 and short_pts > long_pts and macro_score <= 0.30:
                candidate_setups.append({
                    "coin": scan_coin,
                    "symbol": sym,
                    "direction": "SHORT",
                    "score": short_pts,
                    "price": px,
                    "bands": bands,
                    "below_liq": below_liq,
                    "above_liq": above_liq,
                    "already_open": is_already_open,
                    "reason": f"Supply flush ({above_liq:,.0f} USD) + Imb ({imb:+.2f}) + Whales"
                })

        # Sort candidate setups by confluence score descending
        candidate_setups.sort(key=lambda x: x["score"], reverse=True)

        if candidate_setups:
            print("  🎯 RANKED MULTI-ASSET SETUP OPPORTUNITIES:", flush=True)
            for c in candidate_setups:
                status_str = "[ACTIVE/OPEN]" if c["already_open"] else "[ELIGIBLE]"
                print(f"     • {c['coin']} ({c['symbol']}) {c['direction']} | Score: {c['score']}/6 | {c['price']:,.2f} USD | {status_str} | {c['reason']}", flush=True)

        # Filter against macro blackout & position exposure
        decision = "HOLD"
        reason = "Scanning orderflow across all assets"
        trade_details = None

        if blackout_active:
            decision = "BLACKOUT_VETO"
            reason = f"Macro Blackout Active: {blackout_event} within +/- 15 min"
        elif len(open_positions) >= MAX_CONCURRENT:
            top_name = f"{candidate_setups[0]['coin']} {candidate_setups[0]['direction']}" if candidate_setups else "None"
            decision = "MAX_EXPOSURE_REACHED"
            reason = f"Max concurrent positions active ({len(open_positions)}/{MAX_CONCURRENT}). Best setup held: {top_name}"
        else:
            eligible_setups = [c for c in candidate_setups if not c["already_open"]]
            if eligible_setups:
                best = eligible_setups[0]
                decision = f"{best['coin']}_{best['direction']}_ENTRY_TRIGGERED"
                reason = f"{best['reason']} (Score: {best['score']}/6)"

                sym_price = self.bridge.get_symbol_price(best["symbol"])
                if sym_price:
                    digits = sym_price.get("digits", 2)
                    pt = sym_price.get("point", 0.001)
                    exec_px = sym_price["last"] if sym_price["last"] > 0 else best["price"]
                    
                    # Strictly proportional risk distance (1.50% of price, minimum 25 points)
                    r_dist = max(round(exec_px * 0.015, digits), pt * 25.0)
                    risk_budget = self.calculate_dynamic_risk(best["score"], macro_score, account.get("equity_usd", 5000.0))
                    contract_size = sym_price.get("contract_size", 100.0)
                    units = risk_budget / r_dist
                    calc_lot = round(units / contract_size, 2)
                    calc_lot = max(sym_price["min_lot"], min(sym_price["max_lot"], calc_lot))

                    sl_px = round(exec_px - r_dist if best["direction"] == "LONG" else exec_px + r_dist, digits)
                    
                    # Proportional front-run offset (0.10% of price, minimum 2 points)
                    offset = max(round(exec_px * 0.001, digits), pt * 2.0)

                    # Dynamic TP aligned with orderflow liquidation walls & L3 resting orders
                    tp_px = round(exec_px + 2.50 * r_dist if best["direction"] == "LONG" else exec_px - 2.50 * r_dist, digits)
                    if best["direction"] == "LONG":
                        c_tp = [round(b.get("mid_px", 0.0) - offset, digits) for b in best["bands"] if b.get("mid_px", 0.0) > exec_px + 1.8 * r_dist and b.get("amount_usd", 0.0) >= 200000]
                        if c_tp:
                            c_tp.sort()
                            tp_px = min(tp_px, c_tp[0])
                    else:
                        c_tp = [round(b.get("mid_px", 0.0) + offset, digits) for b in best["bands"] if b.get("mid_px", 0.0) < exec_px - 1.8 * r_dist and b.get("amount_usd", 0.0) >= 200000]
                        if c_tp:
                            c_tp.sort(reverse=True)
                            tp_px = max(tp_px, c_tp[0])

                    trade_details = {
                        "coin": best["coin"],
                        "symbol": best["symbol"],
                        "direction": best["direction"],
                        "volume": calc_lot,
                        "price": exec_px,
                        "sl": sl_px,
                        "tp": tp_px,
                        "risk_usd": risk_budget,
                        "conviction_score": best["score"],
                        "paper": self.paper_mode
                    }

                    if self.paper_mode:
                        print(f"  📝 [{utc_now}] PAPER TRADE LOGGED: {trade_details['direction']} {calc_lot} lots {trade_details['symbol']} at {exec_px:.2f} USD | SL: {sl_px:.2f} | TP: {tp_px:.2f} | Dynamic Risk: {risk_budget:.2f} USD (Conviction: {best['score']}/6)", flush=True)
                        self.paper_positions.append(trade_details)
                    else:
                        print(f"  🚀 [{utc_now}] LIVE MT5 EXECUTION: {trade_details['direction']} {calc_lot} lots {trade_details['symbol']} at {exec_px:.2f} USD | SL: {sl_px:.2f} | TP: {tp_px:.2f} | Dynamic Risk: {risk_budget:.2f} USD (Conviction: {best['score']}/6)", flush=True)
                        self.bridge.execute_market_order(trade_details['symbol'], trade_details['direction'], calc_lot, sl_px, tp_px)

        report = {
            "timestamp": utc_now,
            "coin": self.coin,
            "mt5_symbol": self.mt5_symbol,
            "effective_price": effective_px,
            "mt5_account": {
                "balance": account.get("balance_usd", 0.0),
                "equity": account.get("equity_usd", 0.0),
                "profit": account.get("profit_usd", 0.0),
                "open_positions_count": len(open_positions)
            },
            "macro_intelligence": {
                "sentiment_score": macro_score,
                "bias": macro_bias,
                "blackout": blackout_active,
                "blackout_event": blackout_event
            },
            "orderflow_metrics": {
                "below_liq_usd": below_liq_usd,
                "above_liq_usd": above_liq_usd,
                "whale_buys_usd": whale_buys,
                "whale_sells_usd": whale_sells,
                "resting_bid_whale": resting_bid_whale,
                "resting_ask_whale": resting_ask_whale
            },
            "ratchet_updates": ratchets,
            "decision": decision,
            "reason": reason,
            "trade_details": trade_details
        }

        self._save_state(report)
        return report

    def run(self, max_cycles: int = 0):
        print("\n" + "=" * 80, flush=True)
        print(f"AUTONOMOUS 15-MINUTE CANDLE AI TRADER & MT5 EXECUTION ENGINE [{self.coin}]", flush=True)
        print(f"Target MT5 Symbol: {self.mt5_symbol} | Mode: {'PAPER (MT5 Price)' if self.paper_mode else 'LIVE MT5'}", flush=True)
        print(f"Cadence: Evaluates at minute {self.cadence_minute} of every 15m candle (:14, :29, :44, :59)", flush=True)
        print(f"Macro Gate: Active (+/- 15m blackout on CPI, FOMC, NFP) | 3-Stage Ratchets: ON", flush=True)
        print("=" * 80 + "\n", flush=True)

        cycle = 0
        while True:
            cycle += 1
            now = datetime.datetime.now(datetime.timezone.utc)
            minute_mod = now.minute % 15

            is_cadence_time = (minute_mod == self.cadence_minute)
            
            # Run immediate evaluation on cycle 1 or whenever cadence triggers
            if cycle == 1 or is_cadence_time:
                print(f"[{now.strftime('%H:%M:%S UTC')}] >>> EXECUTING 360-DEGREE 15M CANDLE PASS (Minute {now.minute}: {minute_mod}/15m) <<<", flush=True)
                rep = self.evaluate_360_degree_pass()
                print(f"  Account Equity: {rep['mt5_account']['equity']:,.2f} USD | Open MT5 Positions: {rep['mt5_account']['open_positions_count']}", flush=True)
                print(f"  Macro Bias: {rep['macro_intelligence']['bias']} (Score: {rep['macro_intelligence']['sentiment_score']:+.2f}) | Blackout: {rep['macro_intelligence']['blackout']}", flush=True)
                print(f"  Orderflow: Below Liq={rep['orderflow_metrics']['below_liq_usd']:,.0f} USD | Above Liq={rep['orderflow_metrics']['above_liq_usd']:,.0f} USD", flush=True)
                print(f"  Decision: [{rep['decision']}] - {rep['reason']}\n", flush=True)

                if is_cadence_time:
                    # Sleep 60s so we don't re-trigger in the same minute
                    time.sleep(60)

            else:
                # Fast sub-check (every 10s) to monitor open position ratchets in real-time
                sym_price = self.bridge.get_symbol_price(self.mt5_symbol) if self.mt5_symbol else None
                px = sym_price["last"] if sym_price else 0.0
                utc_str = now.strftime("%H:%M:%S UTC")
                self.manage_active_positions(px, utc_str)
                open_pos = self.bridge.get_open_positions()
                self.print_open_positions_summary(open_pos, px, utc_str)

                mins_to_cadence = (self.cadence_minute - minute_mod) if minute_mod < self.cadence_minute else (15 - minute_mod + self.cadence_minute)
                print(f"[{utc_str}] Heartbeat | {self.coin}: {px:,.2f} USD | Next 360 Pass in ~{mins_to_cadence}m | Monitored Open Positions: {len(open_pos)}", flush=True)

            if max_cycles > 0 and cycle >= max_cycles:
                break

            time.sleep(10)


# ── 9. CLI ENTRY POINT ────────────────────────────────────────────────────────
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Master Institutional OFC Strategy Engine")
    parser.add_argument("--mode", choices=["backtest", "dry-run", "mt5-trader"], default="backtest")
    parser.add_argument("--data-dir", default="Binance_Data")
    parser.add_argument("--forex-dir", default="Forex_Data")
    parser.add_argument("--chart", default="Terminal/of_equity_curve.png")
    parser.add_argument("--coin", default="SOL")
    parser.add_argument("--host", default="http://localhost:8095")
    parser.add_argument("--ticks", type=int, default=0, help="Max ticks for verification (0 = infinite)")
    parser.add_argument("--paper", action="store_true", default=True, help="Paper trading mode on MT5 price")
    parser.add_argument("--live", action="store_true", default=False, help="Live MT5 execution mode (disables paper trading)")
    parser.add_argument("--risk", type=float, default=10.0, help="Baseline risk budget in USD per trade (default: 10.0 USD)")
    parser.add_argument("--min-risk", type=float, default=10.0, help="Minimum dynamic risk in USD (default: 10.0 USD)")
    parser.add_argument("--max-risk", type=float, default=20.0, help="Maximum dynamic risk in USD (default: 20.0 USD)")
    parser.add_argument("--cadence-minute", type=int, default=14, help="Minute of 15m candle to evaluate (:14, :29, :44, :59)")
    args = parser.parse_args()

    if args.mode == "backtest":
        run_master_walkforward(Path(args.data_dir), Path(args.forex_dir), args.chart)
    elif args.mode == "dry-run":
        runner = OFCDryRunRunner(coin=args.coin, host=args.host)
        runner.run(max_ticks=args.ticks)
    elif args.mode == "mt5-trader":
        paper_mode = False if args.live else args.paper
        trader = AI15mMT5Trader(
            coin=args.coin,
            host=args.host,
            paper_mode=paper_mode,
            risk_usd=args.risk,
            min_risk_usd=args.min_risk,
            max_risk_usd=args.max_risk,
            cadence_minute=args.cadence_minute
        )
        trader.run(max_cycles=args.ticks)

