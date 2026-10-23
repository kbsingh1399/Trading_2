#!/usr/bin/env python3
"""
Data/Excel_Modules/11_Technical.py
==================================
Dedicated Excel Module 19: Quantitative Technical Indicators & VWAP Bands Suite.
Computes and publishes institutional technical indicators across all 43 Universe Assets:
  - Daily Session VWAP (00:00:00 UTC anchor) with +/-1σ, +/-2σ, +/-3σ Volatility Bands
  - VWAP Z-Score (σ) and Distance to VWAP (%)
  - Rolling 24-Hour Continuous VWAP & Volatility Bands
  - Moving Averages: EMA 9, EMA 20, EMA 50, EMA 200 and 3-hour slope
  - Volatility Envelopes: Wilder ATR(14), ATR%, Bollinger Bands (Upper, Mid, Lower, Bandwidth)
  - Momentum & Oscillators: Wilder RSI(14), RSI State, MACD Line (12, 26), Signal (9), Histogram
  - Market Regimes: Multi-EMA Trend Bias & Mean Reversion Extremes

Also includes Section 2: Detailed 15-Minute Historical Indicator Ribbon (Last 100 Bars)
for Bitcoin (BTC) to provide full chronological transparency of indicator evolution.

Target Sheet: '11_Technical' in Data/DataBase_Trading.xlsx
Position: Index 18 (immediately following '10_Whale_Orders').
"""

from __future__ import annotations

try:
    from logger_config import stamp_sheet_completion_ist, get_current_timestamps
except ImportError:
    stamp_sheet_completion_ist = None
    get_current_timestamps = None


import argparse
import datetime
import json
import logging
import math
import pathlib
import sys
import time
from typing import Any, Dict, List, Optional, Tuple

import numpy as np
import pandas as pd

try:
    import openpyxl
    from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
    from openpyxl.utils import get_column_letter
except ImportError:
    openpyxl = None

MODULES_DIR = pathlib.Path(__file__).resolve().parent
ROOT_DIR = MODULES_DIR.parents[1]
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

from Terminal.Asset_Universe import COMPLETE_UNIVERSE, canonical_asset
from Terminal.Candle_Indicator_Engine import CandleIndicatorEngine

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
log = logging.getLogger("TechnicalModule")

DEFAULT_EXCEL_PATH = ROOT_DIR / "Data" / "DataBase_Trading.xlsx"
TARGET_SHEET_NAME = "11_Technical"
TARGET_INDEX = 19

ASSET_CATEGORIES = {
    "BTC": "Crypto Major", "ETH": "Crypto Major", "SOL": "Crypto Alt L1",
    "BNB": "Crypto Major", "XRP": "Crypto Major", "ADA": "Crypto Alt L1",
    "DOGE": "Crypto Meme", "TRX": "Crypto Alt L1", "DOT": "Crypto Alt L1",
    "LINK": "Crypto DeFi", "BCH": "Crypto PoW", "LTC": "Crypto PoW",
    "AVAX": "Crypto Alt L1", "NEAR": "Crypto Alt L1",
    "GOLD": "Precious Metal", "SILVER": "Precious Metal", "USWTI": "Energy Commodity",
    "SP500": "Equity Index US", "NAS100": "Equity Index Tech", "DJ30": "Equity Index US",
    "GER40": "Equity Index EU", "EURUSD": "FX Major", "GBPUSD": "FX Major", "USDJPY": "FX Major",
    "AAVE": "Crypto DeFi", "ALGO": "Crypto Alt L1", "AR": "Crypto Storage",
    "ATOM": "Crypto Alt L1", "AXS": "Crypto Gaming", "COMP": "Crypto DeFi",
    "CRV": "Crypto DeFi", "DASH": "Crypto Privacy", "FIL": "Crypto Storage",
    "HBAR": "Crypto Alt L1", "IOTA": "Crypto IoT", "NEO": "Crypto Alt L1",
    "SAND": "Crypto Metaverse", "SNX": "Crypto DeFi", "SUSHI": "Crypto DeFi",
    "UNI": "Crypto DeFi", "XLM": "Crypto Payment", "XMR": "Crypto Privacy", "ZEC": "Crypto Privacy",
}

COLUMNS_DEF = [
    ("sr_no", "Sr. No.", 8, "center"),
    ("asset", "Asset", 10, "center"),
    ("category", "Category", 16, "center"),
    ("symbol", "Broker Symbol", 14, "center"),
    ("last_price", "Price ($)", 14, "right"),
    ("change_24h_pct", "24h Chg (%)", 12, "right"),
    ("session_vwap", "Daily VWAP ($)", 14, "right"),
    ("vwap_z", "VWAP Z-Score (σ)", 15, "right"),
    ("upper_1sd", "VWAP +1σ ($)", 14, "right"),
    ("lower_1sd", "VWAP -1σ ($)", 14, "right"),
    ("upper_1_28sd", "VWAP +1.28σ (80%)", 16, "right"),
    ("lower_1_28sd", "VWAP -1.28σ (80%)", 16, "right"),
    ("upper_2sd", "VWAP +2σ ($)", 14, "right"),
    ("lower_2sd", "VWAP -2σ ($)", 14, "right"),
    ("upper_2_01sd", "VWAP +2.01σ (95%)", 16, "right"),
    ("lower_2_01sd", "VWAP -2.01σ (95%)", 16, "right"),
    ("upper_2_51sd", "VWAP +2.51σ (99%)", 16, "right"),
    ("lower_2_51sd", "VWAP -2.51σ (99%)", 16, "right"),
    ("upper_3sd", "VWAP +3σ ($)", 14, "right"),
    ("lower_3sd", "VWAP -3σ ($)", 14, "right"),
    ("dist_to_vwap_pct", "Dist VWAP (%)", 14, "right"),
    ("rolling_vwap_24h", "24h VWAP ($)", 14, "right"),
    ("ema_9", "EMA 9 ($)", 14, "right"),
    ("ema_20", "EMA 20 ($)", 14, "right"),
    ("ema_50", "EMA 50 ($)", 14, "right"),
    ("ema_100", "EMA 100 ($)", 14, "right"),
    ("ema_200", "EMA 200 ($)", 14, "right"),
    ("ema_200_slope_pct", "EMA 200 Slope (%/3h)", 18, "right"),
    ("trend_bias", "Trend Bias", 16, "center"),
    ("rsi_14", "RSI (14)", 11, "right"),
    ("rsi_state", "RSI State", 14, "center"),
    ("atr_14", "ATR (14) ($)", 13, "right"),
    ("atr_pct", "ATR (%)", 11, "right"),
    ("bb_upper", "BB Upper ($)", 14, "right"),
    ("bb_mid", "BB Mid (20) ($)", 14, "right"),
    ("bb_lower", "BB Lower ($)", 14, "right"),
    ("bb_bandwidth", "BB Bandwidth (%)", 16, "right"),
    ("macd_line", "MACD Line", 13, "right"),
    ("macd_signal", "MACD Signal", 13, "right"),
    ("macd_hist", "MACD Hist", 13, "right"),
    ("mr_bias", "Mean Reversion Bias", 20, "center"),
    ("high_24h", "24h High ($)", 14, "right"),
    ("low_24h", "24h Low ($)", 14, "right"),
    ("daily_poc", "Daily POC ($)", 14, "right"),
    ("daily_vah", "Daily VAH ($)", 14, "right"),
    ("daily_val", "Daily VAL ($)", 14, "right"),
    ("week_high", "Week High ($)", 14, "right"),
    ("week_low", "Week Low ($)", 14, "right"),
]

HIST_COLUMNS_DEF = [
    ("bar_time_ist", "Bar Time (IST)", 18, "center"),
    ("open", "Open ($)", 13, "right"),
    ("high", "High ($)", 13, "right"),
    ("low", "Low ($)", 13, "right"),
    ("close", "Close ($)", 13, "right"),
    ("volume", "Volume", 12, "right"),
    ("session_vwap", "Daily VWAP ($)", 14, "right"),
    ("vwap_u1", "VWAP +1σ ($)", 13, "right"),
    ("vwap_l1", "VWAP -1σ ($)", 13, "right"),
    ("vwap_u1_28", "VWAP +1.28σ ($)", 14, "right"),
    ("vwap_l1_28", "VWAP -1.28σ ($)", 14, "right"),
    ("vwap_u2", "VWAP +2σ ($)", 13, "right"),
    ("vwap_l2", "VWAP -2σ ($)", 13, "right"),
    ("vwap_u2_01", "VWAP +2.01σ ($)", 14, "right"),
    ("vwap_l2_01", "VWAP -2.01σ ($)", 14, "right"),
    ("vwap_u2_51", "VWAP +2.51σ ($)", 14, "right"),
    ("vwap_l2_51", "VWAP -2.51σ ($)", 14, "right"),
    ("vwap_u3", "VWAP +3σ ($)", 13, "right"),
    ("vwap_l3", "VWAP -3σ ($)", 13, "right"),
    ("vwap_z", "VWAP Z-Score (σ)", 15, "right"),
    ("ema_9", "EMA 9 ($)", 13, "right"),
    ("ema_20", "EMA 20 ($)", 13, "right"),
    ("ema_50", "EMA 50 ($)", 13, "right"),
    ("ema_100", "EMA 100 ($)", 13, "right"),
    ("ema_200", "EMA 200 ($)", 13, "right"),
    ("rsi_14", "RSI (14)", 11, "right"),
    ("atr_14", "ATR (14) ($)", 12, "right"),
    ("bb_upper", "BB Upper ($)", 13, "right"),
    ("bb_mid", "BB Mid ($)", 13, "right"),
    ("bb_lower", "BB Lower ($)", 13, "right"),
    ("macd_hist", "MACD Hist", 13, "right"),
]


def compute_asset_indicators(bars: List[Dict[str, Any]], asset: str, symbol: str) -> Dict[str, Any]:
    """Computes comprehensive quantitative technical indicators for an asset."""
    if len(bars) < 20:
        return {}

    closes = np.array([float(b["close"]) for b in bars])
    highs = np.array([float(b["high"]) for b in bars])
    lows = np.array([float(b["low"]) for b in bars])

    # Base indicators from CandleIndicatorEngine
    base_ind = CandleIndicatorEngine.compute_indicators(bars)
    px = closes[-1]

    # Fast EMA 9 and EMA 100 from optimized CandleIndicatorEngine ribbon
    ema_9 = base_ind.get("ema_9")
    ema_100 = base_ind.get("ema_100")

    # Bollinger Bands (20, 2.0)
    sma_20 = float(np.mean(closes[-20:]))
    std_20 = float(np.std(closes[-20:]))
    bb_upper = sma_20 + 2.0 * std_20
    bb_lower = sma_20 - 2.0 * std_20
    bb_bw = ((bb_upper - bb_lower) / sma_20 * 100.0) if sma_20 > 0 else 0.0

    # MACD (12, 26, 9)
    if len(closes) >= 35:
        s_closes = pd.Series(closes)
        ema_12 = s_closes.ewm(span=12, adjust=False).mean()
        ema_26 = s_closes.ewm(span=26, adjust=False).mean()
        macd_line = ema_12 - ema_26
        macd_sig = macd_line.ewm(span=9, adjust=False).mean()
        macd_hist = macd_line - macd_sig
        m_line = float(macd_line.iloc[-1])
        m_sig = float(macd_sig.iloc[-1])
        m_hist = float(macd_hist.iloc[-1])
    else:
        m_line = m_sig = m_hist = None

    # 24h Price Change % (96 bars)
    lookback_24h = min(len(closes), 96)
    ref_px = closes[-lookback_24h]
    chg_24h = ((px - ref_px) / ref_px * 100.0) if ref_px > 0 else 0.0

    # Distance to VWAP %
    svwap = base_ind.get("session_vwap")
    dist_vwap_pct = ((px - svwap) / svwap * 100.0) if svwap else None

    # TradingView Confidence Interval Standard Deviation Bands (1.28, 2.01, 2.51)
    act_vwap = base_ind.get("active_vwap") or base_ind.get("session_vwap")
    act_sig = base_ind.get("active_sigma") or base_ind.get("session_sigma")
    if act_vwap is not None and act_sig is not None and act_sig > 0:
        u_1_28 = act_vwap + 1.28 * act_sig
        l_1_28 = act_vwap - 1.28 * act_sig
        u_2_01 = act_vwap + 2.01 * act_sig
        l_2_01 = act_vwap - 2.01 * act_sig
        u_2_51 = act_vwap + 2.51 * act_sig
        l_2_51 = act_vwap - 2.51 * act_sig
    else:
        u_1_28 = l_1_28 = u_2_01 = l_2_01 = u_2_51 = l_2_51 = None

    # Multi-EMA Trend Bias
    e20 = base_ind.get("ema_20")
    e50 = base_ind.get("ema_50")
    e200 = base_ind.get("ema_200")

    if e20 and e50 and e200:
        if px > e20 > e50 > e200:
            trend = "STRONG BULLISH"
        elif px > e20 > e50:
            trend = "BULLISH"
        elif px < e20 < e50 < e200:
            trend = "STRONG BEARISH"
        elif px < e20 < e50:
            trend = "BEARISH"
        else:
            trend = "NEUTRAL / CHOP"
    elif e20 and e50:
        trend = "BULLISH" if e20 > e50 else "BEARISH"
    else:
        trend = "NEUTRAL"

    # RSI State
    rsi = base_ind.get("rsi_14")
    if rsi is not None:
        if rsi >= 70.0:
            rsi_state = "OVERBOUGHT"
        elif rsi >= 55.0:
            rsi_state = "BULLISH"
        elif rsi <= 30.0:
            rsi_state = "OVERSOLD"
        elif rsi <= 45.0:
            rsi_state = "BEARISH"
        else:
            rsi_state = "NEUTRAL"
    else:
        rsi_state = "N/A"

    # Mean Reversion Bias
    z = base_ind.get("vwap_z")
    if z is not None:
        if z >= 2.0:
            mr_bias = "EXTREME OVERBOUGHT"
        elif z <= -2.0:
            mr_bias = "EXTREME OVERSOLD"
        elif z >= 1.5:
            mr_bias = "OVERBOUGHT"
        elif z <= -1.5:
            mr_bias = "OVERSOLD"
        else:
            mr_bias = "FAIR VALUE"
    else:
        mr_bias = "N/A"

    # Calculate Developing Volume Profile (POC, VAH, VAL) and Week High/Low from bars
    daily_poc = daily_vah = daily_val = week_high = week_low = None
    try:
        if bars:
            df_b = pd.DataFrame(bars)
            df_b["dt"] = pd.to_datetime(df_b["time"], unit="s", utc=True)
            last_dt = df_b.iloc[-1]["dt"]
            
            # Today bars
            df_td = df_b[df_b["dt"].dt.date == last_dt.date()]
            if not df_td.empty:
                p_min, p_max = float(df_td["low"].min()), float(df_td["high"].max())
                vol_s = df_td.get("tick_volume") if "tick_volume" in df_td else df_td.get("volume")
                vol_sum = float(vol_s.sum()) if vol_s is not None else 1.0
                if p_min < p_max and vol_sum > 0:
                    nb = 100
                    bins = np.linspace(p_min, p_max, nb + 1)
                    bin_centers = (bins[:-1] + bins[1:]) / 2.0
                    vp = np.zeros(nb)
                    for _, br in df_td.iterrows():
                        v_val = br.get("tick_volume", 1.0) or 1.0
                        il = max(0, np.searchsorted(bins, br["low"], side="left") - 1)
                        ih = min(nb - 1, np.searchsorted(bins, br["high"], side="right"))
                        vp[il : max(il + 1, ih + 1)] += v_val / max(1, ih - il + 1)
                    p_idx = int(np.argmax(vp))
                    daily_poc = float(bin_centers[p_idx])
                    t_vol = vp.sum() * 0.70
                    c_vol, u_i, d_i = vp[p_idx], p_idx, p_idx
                    while c_vol < t_vol and (u_i < nb - 1 or d_i > 0):
                        nu = vp[u_i + 1] if u_i < nb - 1 else -1.0
                        nd = vp[d_i - 1] if d_i > 0 else -1.0
                        if nu >= nd and nu >= 0:
                            u_i += 1; c_vol += nu
                        elif nd >= 0:
                            d_i -= 1; c_vol += nd
                        else: break
                    daily_val = float(bin_centers[d_i])
                    daily_vah = float(bin_centers[u_i])
                else:
                    daily_poc = daily_vah = daily_val = p_min

            # Current Week bars
            curr_wk_start = last_dt - datetime.timedelta(days=last_dt.weekday())
            curr_wk_start = curr_wk_start.replace(hour=0, minute=0, second=0, microsecond=0)
            df_wk = df_b[df_b["dt"] >= curr_wk_start]
            if not df_wk.empty:
                week_high = float(df_wk["high"].max())
                week_low = float(df_wk["low"].min())
    except Exception as e:
        log.warning(f"Error computing POC/VAH for {asset}: {e}")

    return {
        "asset": asset,
        "category": ASSET_CATEGORIES.get(asset, "Crypto Alt"),
        "symbol": symbol,
        "last_price": px,
        "change_24h_pct": chg_24h,
        "session_vwap": svwap,
        "vwap_z": z,
        "upper_1sd": base_ind.get("upper_1sd"),
        "lower_1sd": base_ind.get("lower_1sd"),
        "upper_1_28sd": u_1_28,
        "lower_1_28sd": l_1_28,
        "upper_2sd": base_ind.get("upper_2sd"),
        "lower_2sd": base_ind.get("lower_2sd"),
        "upper_2_01sd": u_2_01,
        "lower_2_01sd": l_2_01,
        "upper_2_51sd": u_2_51,
        "lower_2_51sd": l_2_51,
        "upper_3sd": base_ind.get("upper_3sd"),
        "lower_3sd": base_ind.get("lower_3sd"),
        "dist_to_vwap_pct": dist_vwap_pct,
        "rolling_vwap_24h": base_ind.get("rolling_vwap_24h"),
        "ema_9": ema_9,
        "ema_20": e20,
        "ema_50": e50,
        "ema_100": ema_100,
        "ema_200": e200,
        "ema_200_slope_pct": base_ind.get("ema_200_slope_pct"),
        "trend_bias": trend,
        "rsi_14": rsi,
        "rsi_state": rsi_state,
        "atr_14": base_ind.get("atr_14"),
        "atr_pct": base_ind.get("atr_pct"),
        "bb_upper": bb_upper,
        "bb_mid": sma_20,
        "bb_lower": bb_lower,
        "bb_bandwidth": bb_bw,
        "macd_line": m_line,
        "macd_signal": m_sig,
        "macd_hist": m_hist,
        "mr_bias": mr_bias,
        "high_24h": base_ind.get("high_24h"),
        "low_24h": base_ind.get("low_24h"),
        "daily_poc": daily_poc,
        "daily_vah": daily_vah,
        "daily_val": daily_val,
        "week_high": week_high,
        "week_low": week_low,
    }


def compute_btc_historical_ribbon(bars: List[Dict[str, Any]], limit: int = 100) -> List[Dict[str, Any]]:
    """Computes chronological bar-by-bar indicator series for Bitcoin."""
    if not bars:
        return []

    df = pd.DataFrame(bars)
    df["tp"] = (df["high"] + df["low"] + df["close"]) / 3.0
    vol = df.get("real_volume")
    if vol is None or (vol == 0).all():
        vol = df.get("volume")
    if vol is None or (vol == 0).all():
        vol = df.get("tick_volume")
    df["vol"] = pd.to_numeric(vol, errors="coerce").fillna(1.0).replace(0, 1.0)

    # Date grouping for daily session VWAP
    df["dt"] = pd.to_datetime(df["time"], unit="s", utc=True)
    df["date"] = df["dt"].dt.date

    def calc_day_vwap(g):
        cum_vol = g["vol"].cumsum()
        cum_tp_vol = (g["tp"] * g["vol"]).cumsum()
        vwap = cum_tp_vol / cum_vol
        dev_sq = (g["tp"] - vwap) ** 2
        cum_dev = (dev_sq * g["vol"]).cumsum()
        sigma = np.sqrt(np.maximum(0.0, cum_dev / cum_vol))
        g["session_vwap"] = vwap
        g["session_sigma"] = sigma
        return g

    df = df.groupby("date", group_keys=False).apply(calc_day_vwap)
    df["vwap_z"] = (df["close"] - df["session_vwap"]) / df["session_sigma"].replace(0, np.nan)
    df["vwap_u1"] = df["session_vwap"] + df["session_sigma"]
    df["vwap_l1"] = df["session_vwap"] - df["session_sigma"]
    df["vwap_u1_28"] = df["session_vwap"] + 1.28 * df["session_sigma"]
    df["vwap_l1_28"] = df["session_vwap"] - 1.28 * df["session_sigma"]
    df["vwap_u2"] = df["session_vwap"] + 2.0 * df["session_sigma"]
    df["vwap_l2"] = df["session_vwap"] - 2.0 * df["session_sigma"]
    df["vwap_u2_01"] = df["session_vwap"] + 2.01 * df["session_sigma"]
    df["vwap_l2_01"] = df["session_vwap"] - 2.01 * df["session_sigma"]
    df["vwap_u2_51"] = df["session_vwap"] + 2.51 * df["session_sigma"]
    df["vwap_l2_51"] = df["session_vwap"] - 2.51 * df["session_sigma"]
    df["vwap_u3"] = df["session_vwap"] + 3.0 * df["session_sigma"]
    df["vwap_l3"] = df["session_vwap"] - 3.0 * df["session_sigma"]

    # EMAs
    df["ema_9"] = df["close"].ewm(span=9, adjust=False).mean()
    df["ema_20"] = df["close"].ewm(span=20, adjust=False).mean()
    df["ema_50"] = df["close"].ewm(span=50, adjust=False).mean()
    df["ema_100"] = df["close"].ewm(span=100, adjust=False).mean()
    df["ema_200"] = df["close"].ewm(span=200, adjust=False).mean()

    # RSI 14
    delta = df["close"].diff()
    gain = delta.clip(lower=0.0)
    loss = -delta.clip(upper=0.0)
    avg_gain = gain.ewm(com=13, min_periods=14).mean()
    avg_loss = loss.ewm(com=13, min_periods=14).mean()
    rs = avg_gain / avg_loss.replace(0, 1e-12)
    df["rsi_14"] = 100.0 - (100.0 / (1.0 + rs))

    # ATR 14
    tr1 = df["high"] - df["low"]
    tr2 = (df["high"] - df["close"].shift(1)).abs()
    tr3 = (df["low"] - df["close"].shift(1)).abs()
    tr = pd.concat([tr1, tr2, tr3], axis=1).max(axis=1)
    df["atr_14"] = tr.ewm(com=13, min_periods=14).mean()

    # Bollinger Bands (20, 2)
    df["bb_mid"] = df["close"].rolling(20).mean()
    df["bb_std"] = df["close"].rolling(20).std()
    df["bb_upper"] = df["bb_mid"] + 2.0 * df["bb_std"]
    df["bb_lower"] = df["bb_mid"] - 2.0 * df["bb_std"]

    # MACD (12, 26, 9)
    ema12 = df["close"].ewm(span=12, adjust=False).mean()
    ema26 = df["close"].ewm(span=26, adjust=False).mean()
    df["macd_line"] = ema12 - ema26
    df["macd_signal"] = df["macd_line"].ewm(span=9, adjust=False).mean()
    df["macd_hist"] = df["macd_line"] - df["macd_signal"]

    # Slice the last N bars and format for output
    tail_df = df.tail(limit).copy()
    hist_records = []
    for _, row in tail_df.iterrows():
        hist_records.append({
            "bar_time_utc": row["dt"].strftime("%Y-%m-%d %H:%M"),
            "open": float(row["open"]),
            "high": float(row["high"]),
            "low": float(row["low"]),
            "close": float(row["close"]),
            "volume": float(row["vol"]),
            "session_vwap": float(row["session_vwap"]) if pd.notnull(row["session_vwap"]) else None,
            "vwap_u1": float(row["vwap_u1"]) if pd.notnull(row["vwap_u1"]) else None,
            "vwap_l1": float(row["vwap_l1"]) if pd.notnull(row["vwap_l1"]) else None,
            "vwap_u1_28": float(row["vwap_u1_28"]) if pd.notnull(row["vwap_u1_28"]) else None,
            "vwap_l1_28": float(row["vwap_l1_28"]) if pd.notnull(row["vwap_l1_28"]) else None,
            "vwap_u2": float(row["vwap_u2"]) if pd.notnull(row["vwap_u2"]) else None,
            "vwap_l2": float(row["vwap_l2"]) if pd.notnull(row["vwap_l2"]) else None,
            "vwap_u2_01": float(row["vwap_u2_01"]) if pd.notnull(row["vwap_u2_01"]) else None,
            "vwap_l2_01": float(row["vwap_l2_01"]) if pd.notnull(row["vwap_l2_01"]) else None,
            "vwap_u2_51": float(row["vwap_u2_51"]) if pd.notnull(row["vwap_u2_51"]) else None,
            "vwap_l2_51": float(row["vwap_l2_51"]) if pd.notnull(row["vwap_l2_51"]) else None,
            "vwap_u3": float(row["vwap_u3"]) if pd.notnull(row["vwap_u3"]) else None,
            "vwap_l3": float(row["vwap_l3"]) if pd.notnull(row["vwap_l3"]) else None,
            "vwap_z": float(row["vwap_z"]) if pd.notnull(row["vwap_z"]) else None,
            "ema_9": float(row["ema_9"]) if pd.notnull(row["ema_9"]) else None,
            "ema_20": float(row["ema_20"]) if pd.notnull(row["ema_20"]) else None,
            "ema_50": float(row["ema_50"]) if pd.notnull(row["ema_50"]) else None,
            "ema_100": float(row["ema_100"]) if pd.notnull(row["ema_100"]) else None,
            "ema_200": float(row["ema_200"]) if pd.notnull(row["ema_200"]) else None,
            "rsi_14": float(row["rsi_14"]) if pd.notnull(row["rsi_14"]) else None,
            "atr_14": float(row["atr_14"]) if pd.notnull(row["atr_14"]) else None,
            "bb_upper": float(row["bb_upper"]) if pd.notnull(row["bb_upper"]) else None,
            "bb_mid": float(row["bb_mid"]) if pd.notnull(row["bb_mid"]) else None,
            "bb_lower": float(row["bb_lower"]) if pd.notnull(row["bb_lower"]) else None,
            "macd_hist": float(row["macd_hist"]) if pd.notnull(row["macd_hist"]) else None,
        })
    return hist_records


def harvest_all_technical_data() -> Tuple[List[Dict[str, Any]], List[Dict[str, Any]]]:
    """Syncs candles for all universe assets and computes indicators and BTC history."""
    t0 = time.time()
    log.info(f"Syncing 15m historical candles across {len(COMPLETE_UNIVERSE)} universe assets...")
    engine = CandleIndicatorEngine(universe=COMPLETE_UNIVERSE)
    sync_results = engine.sync_all(count=300, max_workers=10)
    log.info(f"Synchronized candles in {time.time() - t0:.2f}s.")

    # 1. Multi-Asset Screener Table
    screener_records = []
    idx = 1
    for asset in COMPLETE_UNIVERSE:
        bars = engine.cache.get(asset, [])
        if not bars:
            continue
        symbol = sync_results.get(asset, {}).get("symbol", asset)
        ind_data = compute_asset_indicators(bars, asset, symbol)
        if ind_data:
            ind_data["sr_no"] = idx
            screener_records.append(ind_data)
            idx += 1

    # 2. Bitcoin Historical Ribbon (Last 100 bars)
    btc_bars = engine.cache.get("BTC", [])
    btc_hist = compute_btc_historical_ribbon(btc_bars, limit=100)

    log.info(f"Computed indicators for {len(screener_records)} assets and {len(btc_hist)} BTC historical bars.")
    return screener_records, btc_hist


def dump_technical_to_excel(
    screener_records: List[Dict[str, Any]],
    btc_hist: List[Dict[str, Any]],
    sheet_name: str = TARGET_SHEET_NAME,
    target_index: int = TARGET_INDEX,
    excel_path: pathlib.Path = DEFAULT_EXCEL_PATH,
) -> bool:
    """Writes multi-asset screener and historical ribbon to Excel worksheet with institutional styling."""
    if not excel_path.exists():
        log.error(f"Excel workbook not found at: {excel_path}")
        return False

    if not screener_records:
        log.error("0 screener records generated. Aborting Excel dump.")
        return False

    wb = openpyxl.load_workbook(excel_path)

    # Recreate sheet at specified index
    if sheet_name in wb.sheetnames:
        wb.remove(wb[sheet_name])

    ws = wb.create_sheet(title=sheet_name, index=target_index)

    # Color Palette & Styling
    font_banner = Font(name="Segoe UI", size=11, bold=True, color="FFFFFF")
    fill_banner = PatternFill(start_color="0F172A", end_color="0F172A", fill_type="solid")

    font_sub_banner = Font(name="Segoe UI", size=10, bold=True, color="FFFFFF")
    fill_sub_banner = PatternFill(start_color="1E293B", end_color="1E293B", fill_type="solid")

    hdr_font = Font(name="Segoe UI", size=9, bold=True, color="FFFFFF")
    hdr_fill = PatternFill(start_color="334155", end_color="334155", fill_type="solid")

    base_font = Font(name="Segoe UI", size=9, color="0F172A")
    bold_font = Font(name="Segoe UI", size=9, bold=True, color="0F172A")
    green_font = Font(name="Segoe UI", size=9, bold=True, color="00A86B")
    red_font = Font(name="Segoe UI", size=9, bold=True, color="E53935")

    fill_zebra = PatternFill(start_color="F8FAFC", end_color="F8FAFC", fill_type="solid")
    fill_white = PatternFill(start_color="FFFFFF", end_color="FFFFFF", fill_type="solid")

    thin_border_side = Side(border_style="thin", color="E2E8F0")
    row_border = Border(
        left=thin_border_side, right=thin_border_side, top=thin_border_side, bottom=thin_border_side
    )

    ist_tz = datetime.timezone(datetime.timedelta(hours=5, minutes=30))
    now_ist = datetime.datetime.now(ist_tz)
    now_utc = now_ist.strftime("%Y-%m-%d %H:%M:%S IST")

    # =========================================================================
    # SECTION 1: Multi-Asset Indicator Matrix (All 43 Assets)
    # =========================================================================
    last_col_letter = get_column_letter(len(COLUMNS_DEF))

    # Banner Row 1
    ws.merge_cells(f"A1:{last_col_letter}1")
    t1 = ws["A1"]
    if get_current_timestamps:
        _ist_ts, _utc_ts = get_current_timestamps()
        t1.value = f"11_Technical | LAST UPDATED: {_ist_ts} ({_utc_ts}) | ROWS: {len(screener_records)} | STATUS: LIVE"
        t1.font = Font(name="Segoe UI", size=10, bold=True, color="155724")
        t1.fill = PatternFill(start_color="D4EDDA", end_color="D4EDDA", fill_type="solid")
    else:
        t1.value = f"SECTION 1: QUANTITATIVE TECHNICAL INDICATORS & VWAP BANDS MATRIX ({len(screener_records)} ASSETS) [as_of {now_utc}]"
    t1.font = font_banner
    t1.fill = fill_banner
    t1.alignment = Alignment(horizontal="center", vertical="center")
    ws.row_dimensions[1].height = 28

    # Header Row 2
    ws.row_dimensions[2].height = 26
    for col_idx, (col_key, header_title, width, align) in enumerate(COLUMNS_DEF, start=1):
        c = ws.cell(row=2, column=col_idx, value=header_title)
        c.font = hdr_font
        c.fill = hdr_fill
        c.alignment = Alignment(horizontal=align, vertical="center")
        c.border = row_border
        col_letter = get_column_letter(col_idx)
        ws.column_dimensions[col_letter].width = width

    # Data Rows
    current_row = 3
    for r in screener_records:
        ws.row_dimensions[current_row].height = 20
        row_fill = fill_zebra if (current_row % 2 == 0) else fill_white

        for col_idx, (col_key, _, _, align) in enumerate(COLUMNS_DEF, start=1):
            cell = ws.cell(row=current_row, column=col_idx)
            val = r.get(col_key)

            # Format cell values and number formats
            if col_key in ("last_price", "session_vwap", "upper_1sd", "lower_1sd", "upper_1_28sd", "lower_1_28sd",
                           "upper_2sd", "lower_2sd", "upper_2_01sd", "lower_2_01sd", "upper_2_51sd", "lower_2_51sd",
                           "upper_3sd", "lower_3sd", "rolling_vwap_24h", "ema_9", "ema_20", "ema_50", "ema_100", "ema_200",
                           "atr_14", "bb_upper", "bb_mid", "bb_lower", "high_24h", "low_24h", "daily_poc", "daily_vah", "daily_val", "week_high", "week_low"):
                if val is not None and not (isinstance(val, float) and (math.isnan(val) or math.isinf(val))):
                    cell.value = float(val)
                    if abs(float(val)) >= 1000:
                        cell.number_format = "$#,##0.00"
                    elif abs(float(val)) >= 1:
                        cell.number_format = "$#,##0.0000"
                    else:
                        cell.number_format = "$#,##0.000000"
                else:
                    cell.value = ""

            elif col_key in ("change_24h_pct", "dist_to_vwap_pct", "ema_200_slope_pct", "atr_pct", "bb_bandwidth"):
                if val is not None and not (isinstance(val, float) and (math.isnan(val) or math.isinf(val))):
                    cell.value = float(val) / 100.0
                    cell.number_format = "+0.00%;-0.00%;0.00%"
                else:
                    cell.value = ""

            elif col_key in ("vwap_z", "macd_line", "macd_signal", "macd_hist"):
                if val is not None and not (isinstance(val, float) and (math.isnan(val) or math.isinf(val))):
                    cell.value = float(val)
                    cell.number_format = "+0.00;-0.00;0.00"
                else:
                    cell.value = ""

            elif col_key == "rsi_14":
                if val is not None and not (isinstance(val, float) and (math.isnan(val) or math.isinf(val))):
                    cell.value = float(val)
                    cell.number_format = "0.0"
                else:
                    cell.value = ""

            elif col_key == "sr_no":
                cell.value = int(val)
                cell.number_format = "#,##0"

            else:
                cell.value = str(val) if val is not None else ""

            cell.alignment = Alignment(horizontal=align, vertical="center")
            cell.border = row_border
            cell.fill = row_fill

            # Typography & Semantic Highlighting
            if col_key in ("sr_no", "asset", "category"):
                cell.font = bold_font
            elif col_key in ("change_24h_pct", "dist_to_vwap_pct"):
                num_val = r.get(col_key)
                if num_val is not None and num_val > 0:
                    cell.font = green_font
                elif num_val is not None and num_val < 0:
                    cell.font = red_font
                else:
                    cell.font = base_font
            elif col_key == "trend_bias":
                if "BULLISH" in str(val):
                    cell.font = green_font
                elif "BEARISH" in str(val):
                    cell.font = red_font
                else:
                    cell.font = base_font
            elif col_key == "rsi_state":
                if val in ("BULLISH", "OVERBOUGHT"):
                    cell.font = green_font
                elif val in ("BEARISH", "OVERSOLD"):
                    cell.font = red_font
                else:
                    cell.font = base_font
            elif col_key == "mr_bias":
                if "OVERBOUGHT" in str(val):
                    cell.font = red_font
                elif "OVERSOLD" in str(val):
                    cell.font = green_font
                else:
                    cell.font = base_font
            else:
                cell.font = base_font

        current_row += 1

    # Blank buffer row
    current_row += 1

    # =========================================================================
    # SECTION 2: Bitcoin (BTC) 15-Minute Historical Candle Indicator Ribbon
    # =========================================================================
    hist_col_count = len(HIST_COLUMNS_DEF)
    hist_last_letter = get_column_letter(hist_col_count)

    ws.merge_cells(f"A{current_row}:{hist_last_letter}{current_row}")
    sec2_cell = ws[f"A{current_row}"]
    sec2_cell.value = f"SECTION 2: BITCOIN (BTC) 15-MINUTE HISTORICAL CANDLE INDICATOR RIBBON (LAST {len(btc_hist)} BARS)"
    sec2_cell.font = font_sub_banner
    sec2_cell.fill = fill_sub_banner
    sec2_cell.alignment = Alignment(horizontal="center", vertical="center")
    ws.row_dimensions[current_row].height = 26
    current_row += 1

    # Header Row for Section 2
    sec2_hdr_row = current_row
    ws.row_dimensions[sec2_hdr_row].height = 24
    for col_idx, (col_key, header_title, width, align) in enumerate(HIST_COLUMNS_DEF, start=1):
        c = ws.cell(row=sec2_hdr_row, column=col_idx, value=header_title)
        c.font = hdr_font
        c.fill = hdr_fill
        c.alignment = Alignment(horizontal=align, vertical="center")
        c.border = row_border
    current_row += 1

    # Data Rows for Section 2
    for r in btc_hist:
        ws.row_dimensions[current_row].height = 19
        row_fill = fill_zebra if (current_row % 2 == 0) else fill_white

        for col_idx, (col_key, _, _, align) in enumerate(HIST_COLUMNS_DEF, start=1):
            cell = ws.cell(row=current_row, column=col_idx)
            val = r.get(col_key)

            if col_key in ("open", "high", "low", "close", "session_vwap", "vwap_u1", "vwap_l1",
                           "vwap_u1_28", "vwap_l1_28", "vwap_u2", "vwap_l2", "vwap_u2_01", "vwap_l2_01",
                           "vwap_u2_51", "vwap_l2_51", "vwap_u3", "vwap_l3", "ema_9", "ema_20", "ema_50",
                           "ema_100", "ema_200", "atr_14", "bb_upper", "bb_mid", "bb_lower"):
                if val is not None and not (isinstance(val, float) and (math.isnan(val) or math.isinf(val))):
                    cell.value = float(val)
                    cell.number_format = "$#,##0.00"
                else:
                    cell.value = ""

            elif col_key == "volume":
                if val is not None and not (isinstance(val, float) and (math.isnan(val) or math.isinf(val))):
                    cell.value = float(val)
                    cell.number_format = "#,##0"
                else:
                    cell.value = ""

            elif col_key in ("vwap_z", "macd_hist"):
                if val is not None and not (isinstance(val, float) and (math.isnan(val) or math.isinf(val))):
                    cell.value = float(val)
                    cell.number_format = "+0.00;-0.00;0.00"
                else:
                    cell.value = ""

            elif col_key == "rsi_14":
                if val is not None and not (isinstance(val, float) and (math.isnan(val) or math.isinf(val))):
                    cell.value = float(val)
                    cell.number_format = "0.0"
                else:
                    cell.value = ""

            else:
                cell.value = str(val) if val is not None else ""

            cell.alignment = Alignment(horizontal=align, vertical="center")
            cell.border = row_border
            cell.fill = row_fill

            # Formatting
            if col_key in ("bar_time_utc", "close"):
                cell.font = bold_font
            elif col_key == "macd_hist":
                num_val = r.get(col_key)
                if num_val is not None and num_val > 0:
                    cell.font = green_font
                elif num_val is not None and num_val < 0:
                    cell.font = red_font
                else:
                    cell.font = base_font
            else:
                cell.font = base_font

        current_row += 1

    # Freeze panes at E3 so Sr. No., Asset, Category, Symbol remain sticky while scrolling horizontally/vertically
    ws.freeze_panes = "E3"

    import os, time
    temp_excel = excel_path.with_name(f"{excel_path.stem}_{os.getpid()}_{int(time.time()*1000)}.tmp.xlsx")
    wb.save(temp_excel)
    wb.close()
    import time, zipfile
    _is_valid = False
    with zipfile.ZipFile(temp_excel, "r") as _z:
        _is_valid = (_z.testzip() is None)
    if _is_valid:
        for _att in range(30):
            try:
                temp_excel.replace(excel_path)
                break
            except PermissionError:
                if _att == 29: raise
                time.sleep(1.0)
    else:
        if temp_excel.exists(): temp_excel.unlink()
        raise ValueError("Corrupt zip produced during export")
    wb.close()
    log.info(
        f"Dumped {len(screener_records)} asset rows and {len(btc_hist)} BTC historical rows to sheet "
        f"'{sheet_name}' in {excel_path.name} (positioned at Index {target_index}) successfully."
    )
    return True


def run_technical_module(
    sheet_name: str = TARGET_SHEET_NAME,
    target_index: int = TARGET_INDEX,
    excel_path: pathlib.Path = DEFAULT_EXCEL_PATH,
) -> bool:
    """Executes the full technical indicators generation and Excel dumping workflow."""
    t_start = time.time()
    log.info(f"Starting Quantitative Technical Indicators module for sheet '{sheet_name}' (Target Index: {target_index})...")

    screener_records, btc_hist = harvest_all_technical_data()
    if not screener_records:
        log.error("Failed to generate technical indicators records. Aborting.")
        return False

    success = dump_technical_to_excel(
        screener_records=screener_records,
        btc_hist=btc_hist,
        sheet_name=sheet_name,
        target_index=target_index,
        excel_path=excel_path,
    )

    elapsed = time.time() - t_start
    if success:
        log.info(f"Technical module completed successfully in {elapsed:.2f}s.")
        return True
    else:
        log.error(f"Technical module failed during Excel dump after {elapsed:.2f}s.")
        return False


def main():
    parser = argparse.ArgumentParser(description="Quantitative Technical Indicators & VWAP Bands Excel Publisher")
    parser.add_argument("--sheet-name", default=TARGET_SHEET_NAME, help="Target worksheet name")
    parser.add_argument("--target-index", type=int, default=TARGET_INDEX, help="Worksheet index in workbook")
    parser.add_argument("--excel-path", default=str(DEFAULT_EXCEL_PATH), help="Path to DataBase_Trading.xlsx")

    args = parser.parse_args()

    ok = run_technical_module(
        sheet_name=args.sheet_name,
        target_index=args.target_index,
        excel_path=pathlib.Path(args.excel_path),
    )
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
