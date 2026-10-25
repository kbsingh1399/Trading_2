#!/usr/bin/env python3
"""
Data/Excel_Modules/20_Auction_Market_Structure.py
=================================================
Institutional Auction Market Structure, Volume Profile & Session Extremes Engine.

Computes and publishes institutional auction market structure across 54 Universe Assets:
  - Developing Volume Profile (Current Day 00:00 UTC anchor):
      * Daily POC ($) (Point of Control)
      * Daily VAH ($) (70% Volume Area High)
      * Daily VAL ($) (70% Volume Area Low)
      * Value Area Positioning: ABOVE_VALUE / INSIDE_VALUE / BELOW_VALUE
      * Distances to POC, VAH, VAL (%)
  - Prior Day Benchmark Profile & Extremes:
      * PD_POC ($), PD_VAH ($), PD_VAL ($)
      * PDH ($) (Prior Day High), PDL ($) (Prior Day Low), PDC ($) (Close), PDO ($) (Open)
  - Weekly Macro Profile & Extremes:
      * Weekly POC ($), Weekly VAH ($), Weekly VAL ($)
      * CWH ($) (Current Week High), CWL ($) (Current Week Low), CWO ($) (Open)
      * PWH ($) (Prior Week High), PWL ($) (Prior Week Low), PWC ($) (Close)
  - Intraday Session Extremes (UTC boundaries):
      * Asian Session High & Low (00:00 - 08:00 UTC)
      * London Session High & Low (08:00 - 16:00 UTC)
      * New York Session High & Low (13:30 - 20:00 UTC)
      * Initial Balance: IB High & Low (First 60m of London session)
  - Live Broker Telemetry:
      * Real-time Bid, Ask, Spread (bps)
      * Spread Gate Status: PASS / FAIL (Crypto <= 25.0 bps, TradFi <= 5.0 bps)
  - Section 2: Institutional Pivot Points & Key Magnet Shelves (P, R1, S1, R2, S2, Weekly Pivot)

Outputs:
  - Target Sheet: '20_Auction_Market_Structure' in Data/feeds/<feed_name>.parquet
  - Staging Parquet: Data/staging/20_Auction_Market_Structure.parquet
  - Live JSON Telemetry: Data/telemetry/auction_market_structure.json
"""

from __future__ import annotations


import argparse
import datetime
import json
import logging
import math
import os
import pathlib
import sys
import time
from typing import Any, Dict, List, Optional, Tuple

import numpy as np
import pandas as pd

try:
    import MetaTrader5 as mt5
except ImportError:
    mt5 = None


MODULES_DIR = pathlib.Path(__file__).resolve().parent
ROOT_DIR = MODULES_DIR.parents[1]
ROOT = ROOT_DIR
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s][AuctionStructure] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
log = logging.getLogger("AuctionStructure")

STAGING_DIR = ROOT_DIR / "Data" / "staging"
STAGING_DIR.mkdir(parents=True, exist_ok=True)
TELEMETRY_DIR = ROOT_DIR / "Data" / "telemetry"
TELEMETRY_DIR.mkdir(parents=True, exist_ok=True)

TARGET_SHEET_NAME = "20_Auction_Market_Structure"
TARGET_INDEX = 32

# Comprehensive 54-Asset Institutional Universe
INSTITUTIONAL_ASSETS = [
    # Crypto Perpetuals & Raw Majors (31)
    ("BTC", "BTCUSD.pi", "Crypto Major", 25.0, 2),
    ("ETH", "ETHUSD.pi", "Crypto Major", 25.0, 2),
    ("SOL", "SOLUSD.p", "Crypto Alt L1", 25.0, 2),
    ("BNB", "BNBUSD.p", "Crypto Major", 25.0, 2),
    ("XRP", "XRPUSD.pi", "Crypto Major", 25.0, 4),
    ("ADA", "ADAUSD.p", "Crypto Alt L1", 25.0, 4),
    ("DOGE", "DOGUSD.p", "Crypto Meme", 25.0, 5),
    ("TRX", "TRXUSD.p", "Crypto Alt L1", 25.0, 4),
    ("DOT", "DOTUSD.pi", "Crypto Alt L1", 25.0, 4),
    ("LINK", "LNKUSD.p", "Crypto DeFi", 25.0, 3),
    ("BCH", "BCHUSD.p", "Crypto PoW", 25.0, 2),
    ("LTC", "LTCUSD.pi", "Crypto PoW", 25.0, 3),
    ("AVAX", "AVXUSD.p", "Crypto Alt L1", 25.0, 2),
    ("NEAR", "NERUSD.p", "Crypto Alt L1", 25.0, 3),
    ("UNI", "UNIUSD.p", "Crypto DeFi", 25.0, 3),
    ("XLM", "XLMUSD.p", "Crypto Payment", 25.0, 4),
    ("XMR", "XMRUSD.p", "Crypto Privacy", 25.0, 2),
    ("ATOM", "ATMUSD.p", "Crypto Alt L1", 25.0, 3),
    ("AAVE", "AVEUSD.p", "Crypto DeFi", 25.0, 2),
    ("ALGO", "ALGUSD.p", "Crypto Alt L1", 25.0, 4),
    ("DASH", "DSHUSD.p", "Crypto PoW", 25.0, 3),
    ("ZEC", "ZECUSD.p", "Crypto Privacy", 25.0, 2),
    ("YFI", "YFIUSD.p", "Crypto DeFi", 25.0, 1),
    ("FIL", "FILUSD.p", "Crypto Storage", 25.0, 3),
    ("HBAR", "BARUSD.p", "Crypto Enterprise", 25.0, 4),
    ("SAND", "SNDUSD.p", "Crypto Metaverse", 25.0, 4),
    ("SNX", "SNXUSD.p", "Crypto DeFi", 25.0, 3),
    ("NEO", "NEOUSD.p", "Crypto Alt L1", 25.0, 2),
    ("CRV", "CRVUSD.p", "Crypto DeFi", 25.0, 3),
    ("AXS", "AXSUSD.p", "Crypto Gaming", 25.0, 2),
    ("SUSHI", "XSIUSD.p", "Crypto DeFi", 25.0, 3),
    # Global Equity Indices (15)
    ("DJ30", "DJ30.p", "Equity Index US", 5.0, 2),
    ("SP500", "SP500.p", "Equity Index US", 5.0, 2),
    ("NAS100", "NAS100.p", "Equity Index Tech", 5.0, 2),
    ("US2000", "US2000.p", "Equity Index US", 5.0, 2),
    ("GER40", "GER40.p", "Equity Index EU", 5.0, 2),
    ("UK100", "UK100.p", "Equity Index UK", 5.0, 2),
    ("JP225", "JP225.p", "Equity Index Asia", 5.0, 1),
    ("AU200", "AU200.p", "Equity Index Asia", 5.0, 2),
    ("FR40", "FR40.p", "Equity Index EU", 5.0, 2),
    ("HK50", "HK50.p", "Equity Index Asia", 5.0, 2),
    ("STOXX50", "STOXX50.p", "Equity Index EU", 5.0, 2),
    ("CHINA50", "CHINA50.p", "Equity Index Asia", 5.0, 2),
    ("CHINAH", "CHINAH.p", "Equity Index Asia", 5.0, 2),
    ("NETH25", "NETH25.p", "Equity Index EU", 5.0, 2),
    ("SWISS20", "SWISS20.p", "Equity Index EU", 5.0, 2),
    # Commodities & Precious Metals (14)
    ("GOLD", "XAUUSD.pi", "Precious Metal", 5.0, 2),
    ("SILVER", "XAGUSD.pi", "Precious Metal", 5.0, 3),
    ("GOLD_EUR", "XAUEUR.pi", "Precious Metal", 5.0, 2),
    ("GOLD_AUD", "XAUAUD.pi", "Precious Metal", 5.0, 2),
    ("GOLD_GBP", "XAUGBP.pi", "Precious Metal", 5.0, 2),
    ("USWTI", "USWTI.p", "Energy Commodity", 5.0, 3),
    ("UKBRENT", "UKBRENT.p", "Energy Commodity", 5.0, 3),
    ("GAS", "GAS.p", "Energy Commodity", 5.0, 3),
    ("COPPER", "COPPER.p", "Industrial Metal", 5.0, 3),
    ("PLATINUM", "XPTUSD.pi", "Precious Metal", 5.0, 2),
    ("PALLADIUM", "XPDUSD.pi", "Precious Metal", 5.0, 2),
    ("ALUMINIUM", "ALUMINIUM.p", "Industrial Metal", 5.0, 2),
    ("LEAD", "LEAD.p", "Industrial Metal", 5.0, 2),
    ("ZINC", "ZINC.p", "Industrial Metal", 5.0, 2),
    # Forex Majors & Liquid Crosses (24)
    ("EURUSD", "EURUSD.pi", "FX Major", 5.0, 5),
    ("GBPUSD", "GBPUSD.pi", "FX Major", 5.0, 5),
    ("USDJPY", "USDJPY.pi", "FX Major", 5.0, 3),
    ("AUDUSD", "AUDUSD.pi", "FX Major", 5.0, 5),
    ("USDCAD", "USDCAD.pi", "FX Major", 5.0, 5),
    ("USDCHF", "USDCHF.pi", "FX Major", 5.0, 5),
    ("NZDUSD", "NZDUSD.pi", "FX Major", 5.0, 5),
    ("EURGBP", "EURGBP.pi", "FX Cross", 5.0, 5),
    ("EURJPY", "EURJPY.pi", "FX Cross", 5.0, 3),
    ("GBPJPY", "GBPJPY.pi", "FX Cross", 5.0, 3),
    ("AUDJPY", "AUDJPY.pi", "FX Cross", 5.0, 3),
    ("CHFJPY", "CHFJPY.pi", "FX Cross", 5.0, 3),
    ("CADJPY", "CADJPY.pi", "FX Cross", 5.0, 3),
    ("EURAUD", "EURAUD.pi", "FX Cross", 5.0, 5),
    ("GBPAUD", "GBPAUD.pi", "FX Cross", 5.0, 5),
    ("EURCAD", "EURCAD.pi", "FX Cross", 5.0, 5),
    ("EURCHF", "EURCHF.pi", "FX Cross", 5.0, 5),
    ("GBPCAD", "GBPCAD.pi", "FX Cross", 5.0, 5),
    ("GBPCHF", "GBPCHF.pi", "FX Cross", 5.0, 5),
    ("AUDCAD", "AUDCAD.pi", "FX Cross", 5.0, 5),
    ("AUDCHF", "AUDCHF.pi", "FX Cross", 5.0, 5),
    ("CADCHF", "CADCHF.pi", "FX Cross", 5.0, 5),
    ("NZDJPY", "NZDJPY.pi", "FX Cross", 5.0, 3),
    ("USDCNH", "USDCNH.pi", "FX Liquid", 5.0, 4),
]

COLUMNS_DEF = [
    ("sr_no", "Sr. No.", 8, "center"),
    ("asset", "Asset", 10, "center"),
    ("symbol", "Broker Symbol", 13, "center"),
    ("category", "Category", 16, "center"),
    ("price", "Current Price", 14, "right"),
    ("spread_bps", "Spread (bps)", 12, "right"),
    ("spread_gate", "Spread Gate", 12, "center"),
    ("va_position", "Value Area Status", 18, "center"),
    ("daily_poc", "Daily POC ($)", 14, "right"),
    ("daily_vah", "Daily VAH ($)", 14, "right"),
    ("daily_val", "Daily VAL ($)", 14, "right"),
    ("dist_poc_pct", "Dist POC (%)", 12, "right"),
    ("dist_vah_pct", "Dist VAH (%)", 12, "right"),
    ("dist_val_pct", "Dist VAL (%)", 12, "right"),
    ("pd_poc", "Prior Day POC ($)", 15, "right"),
    ("pd_vah", "Prior Day VAH ($)", 15, "right"),
    ("pd_val", "Prior Day VAL ($)", 15, "right"),
    ("pdh", "Prior Day High ($)", 15, "right"),
    ("pdl", "Prior Day Low ($)", 15, "right"),
    ("pdc", "Prior Day Close ($)", 15, "right"),
    ("weekly_poc", "Weekly POC ($)", 14, "right"),
    ("weekly_vah", "Weekly VAH ($)", 14, "right"),
    ("weekly_val", "Weekly VAL ($)", 14, "right"),
    ("cwh", "Current Week High", 15, "right"),
    ("cwl", "Current Week Low", 15, "right"),
    ("pwh", "Prior Week High", 15, "right"),
    ("pwl", "Prior Week Low", 15, "right"),
    ("asian_high", "Asian High (00-08z)", 16, "right"),
    ("asian_low", "Asian Low (00-08z)", 16, "right"),
    ("london_high", "London High (08-16z)", 17, "right"),
    ("london_low", "London Low (08-16z)", 17, "right"),
    ("ny_high", "NY High (13-20z)", 16, "right"),
    ("ny_low", "NY Low (13-20z)", 16, "right"),
    ("ib_high", "IB High (08-09z)", 15, "right"),
    ("ib_low", "IB Low (08-09z)", 15, "right"),
    ("monday_high", "Monday High ($)", 15, "right"),
    ("monday_low", "Monday Low ($)", 15, "right"),
    ("monday_mid", "Monday Mid / WIB ($)", 16, "right"),
    ("cmh", "Current Month High ($)", 16, "right"),
    ("cml", "Current Month Low ($)", 16, "right"),
    ("pmh", "Prior Month High ($)", 16, "right"),
    ("pml", "Prior Month Low ($)", 16, "right"),
    ("fib_swing_h", "Fib Swing High ($)", 15, "right"),
    ("fib_swing_l", "Fib Swing Low ($)", 15, "right"),
    ("fib_dir", "Fib Impulse Dir", 16, "center"),
    ("fib_gp_min", "Fib GP Lower ($)", 15, "right"),
    ("fib_gp_max", "Fib GP Upper ($)", 15, "right"),
    ("fib_ote", "Fib OTE 0.702 ($)", 16, "right"),
    ("fib_inval", "Fib Inval 0.786 ($)", 16, "right"),
    ("fib_status", "Fib Golden Zone Status", 22, "center"),
    ("auction_regime", "Auction Market Regime", 22, "center"),
    ("timestamp", "Timestamp (IST)", 22, "center"),
]

PIVOT_COLUMNS_DEF = [
    ("sr_no", "Sr. No.", 8, "center"),
    ("asset", "Asset", 10, "center"),
    ("symbol", "Broker Symbol", 13, "center"),
    ("price", "Current Price", 14, "right"),
    ("pivot", "Daily Pivot (P)", 14, "right"),
    ("r1", "Daily R1", 14, "right"),
    ("s1", "Daily S1", 14, "right"),
    ("r2", "Daily R2", 14, "right"),
    ("s2", "Daily S2", 14, "right"),
    ("weekly_pivot", "Weekly Pivot (P)", 15, "right"),
    ("weekly_r1", "Weekly R1", 15, "right"),
    ("weekly_s1", "Weekly S1", 15, "right"),
    ("session_bias", "Session Bias vs Pivot", 20, "center"),
    ("timestamp", "Timestamp (IST)", 22, "center"),
]


def compute_volume_profile(df_subset: pd.DataFrame, n_bins: int = 150) -> Dict[str, Optional[float]]:
    """Calculates Point of Control (POC), Value Area High (VAH), and Value Area Low (VAL)."""
    if df_subset is None or df_subset.empty:
        return {"poc": None, "vah": None, "val": None, "high": None, "low": None, "vol": 0.0}

    p_min = df_subset["low"].min()
    p_max = df_subset["high"].max()
    vol_series = df_subset["tick_volume"] if "tick_volume" in df_subset else df_subset["volume"]
    vol_sum = float(vol_series.sum())

    if p_min == p_max or vol_sum <= 0:
        return {
            "poc": float(p_min),
            "vah": float(p_min),
            "val": float(p_min),
            "high": float(p_max),
            "low": float(p_min),
            "vol": vol_sum,
        }

    bins = np.linspace(p_min, p_max, n_bins + 1)
    bin_centers = (bins[:-1] + bins[1:]) / 2.0
    vol_profile = np.zeros(n_bins)

    for _, row in df_subset.iterrows():
        b_low = row["low"]
        b_high = row["high"]
        b_vol = row.get("tick_volume", 0)
        if b_vol <= 0:
            b_vol = row.get("real_volume", 0)
        if b_vol <= 0:
            b_vol = 1.0

        idx_low = max(0, np.searchsorted(bins, b_low, side="left") - 1)
        idx_high = min(n_bins - 1, np.searchsorted(bins, b_high, side="right"))
        if idx_high < idx_low:
            idx_high = idx_low
        count = idx_high - idx_low + 1
        vol_profile[idx_low : idx_high + 1] += b_vol / count

    poc_idx = int(np.argmax(vol_profile))
    poc = bin_centers[poc_idx]

    target_vol = vol_profile.sum() * 0.70
    current_vol = vol_profile[poc_idx]
    up_idx = poc_idx
    down_idx = poc_idx

    while current_vol < target_vol and (up_idx < n_bins - 1 or down_idx > 0):
        next_up_vol = vol_profile[up_idx + 1] if up_idx < n_bins - 1 else -1.0
        next_down_vol = vol_profile[down_idx - 1] if down_idx > 0 else -1.0

        if next_up_vol >= next_down_vol and next_up_vol >= 0:
            up_idx += 1
            current_vol += next_up_vol
        elif next_down_vol >= 0:
            down_idx -= 1
            current_vol += next_down_vol
        else:
            break

    val = bin_centers[down_idx]
    vah = bin_centers[up_idx]

    return {
        "poc": float(poc),
        "vah": float(vah),
        "val": float(val),
        "high": float(p_max),
        "low": float(p_min),
        "vol": vol_sum,
    }


def harvest_auction_market_structure() -> Tuple[List[Dict[str, Any]], List[Dict[str, Any]]]:
    """Polls MT5 for all 54 assets, computes auction profiles and pivots."""
    if mt5 is None or not mt5.initialize():
        log.error("Failed to initialize MetaTrader 5.")
        return [], []

    log.info(f"Connected to MT5. Harvesting auction structure across {len(INSTITUTIONAL_ASSETS)} institutional assets...")

    structure_records: List[Dict[str, Any]] = []
    pivot_records: List[Dict[str, Any]] = []

    for idx, (asset, sym, cat, max_spread_bps, digits) in enumerate(INSTITUTIONAL_ASSETS, start=1):
        # 1. Fetch live tick for spreads
        tick = mt5.symbol_info_tick(sym)
        bid = float(tick.bid) if tick else 0.0
        ask = float(tick.ask) if tick else 0.0
        mid = (bid + ask) / 2.0 if (bid > 0 and ask > 0) else 0.0
        spread_bps = ((ask - bid) / bid * 10000.0) if bid > 0 else 0.0
        spread_gate = "PASS" if spread_bps <= max_spread_bps else "FAIL"

        # 2. Fetch M15 bars (last 1200 bars = ~12.5 trading days) and D1 bars (last 70 days for monthly macro extents)
        bars = mt5.copy_rates_from_pos(sym, mt5.TIMEFRAME_M15, 0, 1200)
        if bars is None or len(bars) < 30:
            log.warning(f"Insufficient bars for {sym} ({asset}). Skipping.")
            continue

        bars_d1 = mt5.copy_rates_from_pos(sym, mt5.TIMEFRAME_D1, 0, 70)
        df_d1 = pd.DataFrame(bars_d1) if (bars_d1 is not None and len(bars_d1) > 0) else pd.DataFrame()
        if not df_d1.empty:
            df_d1["dt"] = pd.to_datetime(df_d1["time"], unit="s", utc=True)

        df = pd.DataFrame(bars)
        df["dt"] = pd.to_datetime(df["time"], unit="s", utc=True)
        now_dt = df.iloc[-1]["dt"]
        today_date = now_dt.date()
        yesterday_date = today_date - datetime.timedelta(days=1)

        # Handle weekend gap for yesterday
        prev_dates = sorted(list(set(df[df["dt"].dt.date < today_date]["dt"].dt.date)))
        prior_trading_date = prev_dates[-1] if prev_dates else yesterday_date

        # Week boundaries (Monday 00:00 UTC)
        curr_week_start = now_dt - datetime.timedelta(days=now_dt.weekday())
        curr_week_start = curr_week_start.replace(hour=0, minute=0, second=0, microsecond=0)
        prior_week_start = curr_week_start - datetime.timedelta(days=7)
        prior_week_end = curr_week_start

        # Subsets
        df_today = df[df["dt"].dt.date == today_date]
        df_yesterday = df[df["dt"].dt.date == prior_trading_date]
        df_curr_week = df[df["dt"] >= curr_week_start]
        df_prior_week = df[(df["dt"] >= prior_week_start) & (df["dt"] < prior_week_end)]

        # Monday Opening Range (Weekly Initial Balance - WIB)
        df_monday = df[(df["dt"] >= curr_week_start) & (df["dt"] < curr_week_start + datetime.timedelta(days=1))]
        if df_monday.empty or len(df_monday) < 4:
            df_monday = df[(df["dt"] >= prior_week_start) & (df["dt"] < prior_week_start + datetime.timedelta(days=1))]

        # Monthly Macro Extents from D1
        if not df_d1.empty:
            curr_month_bars = df_d1[(df_d1["dt"].dt.year == now_dt.year) & (df_d1["dt"].dt.month == now_dt.month)]
            prior_year = now_dt.year - 1 if now_dt.month == 1 else now_dt.year
            prior_month = 12 if now_dt.month == 1 else now_dt.month - 1
            prior_month_bars = df_d1[(df_d1["dt"].dt.year == prior_year) & (df_d1["dt"].dt.month == prior_month)]
            cmh_val = float(curr_month_bars["high"].max()) if not curr_month_bars.empty else None
            cml_val = float(curr_month_bars["low"].min()) if not curr_month_bars.empty else None
            pmh_val = float(prior_month_bars["high"].max()) if not prior_month_bars.empty else None
            pml_val = float(prior_month_bars["low"].min()) if not prior_month_bars.empty else None
        else:
            cmh_val = float(df_curr_week["high"].max()) if not df_curr_week.empty else None
            cml_val = float(df_curr_week["low"].min()) if not df_curr_week.empty else None
            pmh_val = float(df_prior_week["high"].max()) if not df_prior_week.empty else None
            pml_val = float(df_prior_week["low"].min()) if not df_prior_week.empty else None

        # Session subsets today
        df_asian = df_today[(df_today["dt"].dt.hour >= 0) & (df_today["dt"].dt.hour < 8)]
        df_london = df_today[(df_today["dt"].dt.hour >= 8) & (df_today["dt"].dt.hour < 16)]
        df_ny = df_today[(df_today["dt"].dt.hour >= 13) & (df_today["dt"].dt.hour < 20)]
        df_ib = df_today[(df_today["dt"].dt.hour == 8)]  # London Initial Balance 08:00 - 09:00 UTC

        # Profiles
        prof_today = compute_volume_profile(df_today)
        prof_yesterday = compute_volume_profile(df_yesterday)
        prof_curr_week = compute_volume_profile(df_curr_week)
        prof_prior_week = compute_volume_profile(df_prior_week)

        # Extremes
        cur_px = float(df.iloc[-1]["close"]) if mid == 0.0 else mid
        daily_poc = prof_today["poc"]
        daily_vah = prof_today["vah"]
        daily_val = prof_today["val"]

        dist_poc = ((cur_px - daily_poc) / daily_poc * 100.0) if daily_poc else None
        dist_vah = ((cur_px - daily_vah) / daily_vah * 100.0) if daily_vah else None
        dist_val = ((cur_px - daily_val) / daily_val * 100.0) if daily_val else None

        # Value area status
        if daily_vah is not None and daily_val is not None:
            if cur_px > daily_vah:
                va_pos = "ABOVE_VALUE (Imbalance)"
            elif cur_px < daily_val:
                va_pos = "BELOW_VALUE (Imbalance)"
            else:
                va_pos = "INSIDE_VALUE (Balance)"
        else:
            va_pos = "N/A"

        # Prior day levels
        pdh = float(df_yesterday["high"].max()) if not df_yesterday.empty else None
        pdl = float(df_yesterday["low"].min()) if not df_yesterday.empty else None
        pdc = float(df_yesterday.iloc[-1]["close"]) if not df_yesterday.empty else None

        # Weekly levels
        cwh = float(df_curr_week["high"].max()) if not df_curr_week.empty else None
        cwl = float(df_curr_week["low"].min()) if not df_curr_week.empty else None
        pwh = float(df_prior_week["high"].max()) if not df_prior_week.empty else None
        pwl = float(df_prior_week["low"].min()) if not df_prior_week.empty else None
        pwc = float(df_prior_week.iloc[-1]["close"]) if not df_prior_week.empty else None

        # Session levels
        asian_h = float(df_asian["high"].max()) if not df_asian.empty else None
        asian_l = float(df_asian["low"].min()) if not df_asian.empty else None
        london_h = float(df_london["high"].max()) if not df_london.empty else None
        london_l = float(df_london["low"].min()) if not df_london.empty else None
        ny_h = float(df_ny["high"].max()) if not df_ny.empty else None
        ny_l = float(df_ny["low"].min()) if not df_ny.empty else None
        ib_h = float(df_ib["high"].max()) if not df_ib.empty else None
        ib_l = float(df_ib["low"].min()) if not df_ib.empty else None

        # Auction regime
        if pdh and pdl and daily_vah and daily_val:
            if cur_px > daily_vah and cur_px > pdh:
                regime = "TREND_UP_ACCEPTANCE"
            elif cur_px < daily_val and cur_px < pdl:
                regime = "TREND_DOWN_ACCEPTANCE"
            elif daily_val <= cur_px <= daily_vah:
                regime = "ROTATIONAL_BALANCE"
            elif cur_px > pdh and cur_px <= daily_vah:
                regime = "FAILED_AUCTION_REVERSAL"
            else:
                regime = "RANGE_EXPANSION"
        else:
            regime = "DEVELOPING"

        # Monday Opening Range (Weekly Initial Balance)
        mon_h = float(df_monday["high"].max()) if not df_monday.empty else None
        mon_l = float(df_monday["low"].min()) if not df_monday.empty else None
        mon_mid = (mon_h + mon_l) / 2.0 if (mon_h is not None and mon_l is not None) else None

        # Symmetrical Fibonacci Golden Zone (OTE) across governing 96-bar (24h) swing
        swing_window = df.tail(96)
        if len(swing_window) >= 16:
            sw_h = float(swing_window["high"].max())
            sw_l = float(swing_window["low"].min())
            idx_sw_h = int(swing_window["high"].values.argmax())
            idx_sw_l = int(swing_window["low"].values.argmin())
            sw_delta = sw_h - sw_l

            if sw_delta > 0:
                if idx_sw_h >= idx_sw_l:
                    # Bullish impulse (L -> H), retrace drops from H towards L
                    fib_dir = "BULLISH_IMPULSE"
                    fib_gp_min = round(sw_h - 0.650 * sw_delta, digits)
                    fib_gp_max = round(sw_h - 0.618 * sw_delta, digits)
                    fib_ote = round(sw_h - 0.702 * sw_delta, digits)
                    fib_inval = round(sw_h - 0.786 * sw_delta, digits)

                    if cur_px > sw_h:
                        fib_status = "EXPANSION_NEW_HIGH"
                    elif cur_px > fib_gp_max:
                        fib_status = "SHALLOW_RETRACE"
                    elif cur_px >= fib_gp_min:
                        fib_status = "IN_GOLDEN_POCKET (0.618-0.650)"
                    elif cur_px >= fib_ote:
                        fib_status = "IN_OTE_ZONE (0.702)"
                    elif cur_px >= fib_inval:
                        fib_status = "DEEP_SHELF_TEST (0.786)"
                    else:
                        fib_status = "STRUCTURE_INVALIDATED"
                else:
                    # Bearish impulse (H -> L), retrace rallies from L towards H
                    fib_dir = "BEARISH_IMPULSE"
                    fib_gp_min = round(sw_l + 0.618 * sw_delta, digits)
                    fib_gp_max = round(sw_l + 0.650 * sw_delta, digits)
                    fib_ote = round(sw_l + 0.702 * sw_delta, digits)
                    fib_inval = round(sw_l + 0.786 * sw_delta, digits)

                    if cur_px < sw_l:
                        fib_status = "EXPANSION_NEW_LOW"
                    elif cur_px < fib_gp_min:
                        fib_status = "SHALLOW_RETRACE"
                    elif cur_px <= fib_gp_max:
                        fib_status = "IN_GOLDEN_POCKET (0.618-0.650)"
                    elif cur_px <= fib_ote:
                        fib_status = "IN_OTE_ZONE (0.702)"
                    elif cur_px <= fib_inval:
                        fib_status = "DEEP_SHELF_TEST (0.786)"
                    else:
                        fib_status = "STRUCTURE_INVALIDATED"
            else:
                sw_h, sw_l, fib_dir, fib_gp_min, fib_gp_max, fib_ote, fib_inval, fib_status = None, None, "FLAT", None, None, None, None, "N/A"
        else:
            sw_h, sw_l, fib_dir, fib_gp_min, fib_gp_max, fib_ote, fib_inval, fib_status = None, None, "N/A", None, None, None, None, "N/A"

        now_ist = (datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(hours=5, minutes=30)).strftime("%Y-%m-%d %H:%M:%S IST")
        structure_records.append({
            "timestamp": now_ist,
            "sr_no": idx,
            "asset": asset,
            "symbol": sym,
            "category": cat,
            "price": round(cur_px, digits),
            "spread_bps": round(spread_bps, 2),
            "spread_gate": spread_gate,
            "va_position": va_pos,
            "daily_poc": round(daily_poc, digits) if daily_poc else None,
            "daily_vah": round(daily_vah, digits) if daily_vah else None,
            "daily_val": round(daily_val, digits) if daily_val else None,
            "dist_poc_pct": round(dist_poc, 2) if dist_poc else None,
            "dist_vah_pct": round(dist_vah, 2) if dist_vah else None,
            "dist_val_pct": round(dist_val, 2) if dist_val else None,
            "pd_poc": round(prof_yesterday["poc"], digits) if prof_yesterday["poc"] else None,
            "pd_vah": round(prof_yesterday["vah"], digits) if prof_yesterday["vah"] else None,
            "pd_val": round(prof_yesterday["val"], digits) if prof_yesterday["val"] else None,
            "pdh": round(pdh, digits) if pdh else None,
            "pdl": round(pdl, digits) if pdl else None,
            "pdc": round(pdc, digits) if pdc else None,
            "monday_high": round(mon_h, digits) if mon_h else None,
            "monday_low": round(mon_l, digits) if mon_l else None,
            "monday_mid": round(mon_mid, digits) if mon_mid else None,
            "weekly_poc": round(prof_curr_week["poc"], digits) if prof_curr_week["poc"] else None,
            "weekly_vah": round(prof_curr_week["vah"], digits) if prof_curr_week["vah"] else None,
            "weekly_val": round(prof_curr_week["val"], digits) if prof_curr_week["val"] else None,
            "cwh": round(cwh, digits) if cwh else None,
            "cwl": round(cwl, digits) if cwl else None,
            "pwh": round(pwh, digits) if pwh else None,
            "pwl": round(pwl, digits) if pwl else None,
            "cmh": round(cmh_val, digits) if cmh_val else None,
            "cml": round(cml_val, digits) if cml_val else None,
            "pmh": round(pmh_val, digits) if pmh_val else None,
            "pml": round(pml_val, digits) if pml_val else None,
            "asian_high": round(asian_h, digits) if asian_h else None,
            "asian_low": round(asian_l, digits) if asian_l else None,
            "london_high": round(london_h, digits) if london_h else None,
            "london_low": round(london_l, digits) if london_l else None,
            "ny_high": round(ny_h, digits) if ny_h else None,
            "ny_low": round(ny_l, digits) if ny_l else None,
            "ib_high": round(ib_h, digits) if ib_h else None,
            "ib_low": round(ib_l, digits) if ib_l else None,
            "fib_swing_h": round(sw_h, digits) if sw_h else None,
            "fib_swing_l": round(sw_l, digits) if sw_l else None,
            "fib_dir": fib_dir,
            "fib_gp_min": fib_gp_min,
            "fib_gp_max": fib_gp_max,
            "fib_ote": fib_ote,
            "fib_inval": fib_inval,
            "fib_status": fib_status,
            "auction_regime": regime,
        })

        # Section 2: Pivots
        if pdh and pdl and pdc:
            pp = (pdh + pdl + pdc) / 3.0
            r1 = 2.0 * pp - pdl
            s1 = 2.0 * pp - pdh
            r2 = pp + (pdh - pdl)
            s2 = pp - (pdh - pdl)
            bias = "BULLISH (Above Pivot)" if cur_px > pp else "BEARISH (Below Pivot)"
        else:
            pp = r1 = s1 = r2 = s2 = None
            bias = "N/A"

        if pwh and pwl and pwc:
            w_pp = (pwh + pwl + pwc) / 3.0
            w_r1 = 2.0 * w_pp - pwl
            w_s1 = 2.0 * w_pp - pwh
        else:
            w_pp = w_r1 = w_s1 = None

        pivot_records.append({
            "timestamp": now_ist,
            "sr_no": idx,
            "asset": asset,
            "symbol": sym,
            "price": round(cur_px, digits),
            "pivot": round(pp, digits) if pp else None,
            "r1": round(r1, digits) if r1 else None,
            "s1": round(s1, digits) if s1 else None,
            "r2": round(r2, digits) if r2 else None,
            "s2": round(s2, digits) if s2 else None,
            "weekly_pivot": round(w_pp, digits) if w_pp else None,
            "weekly_r1": round(w_r1, digits) if w_r1 else None,
            "weekly_s1": round(w_s1, digits) if w_s1 else None,
            "session_bias": bias,
        })

    mt5.shutdown()
    log.info(f"Successfully computed auction market structure for {len(structure_records)} assets.")
    return structure_records, pivot_records


def run_auction_module(
    sheet_name: str = TARGET_SHEET_NAME,
    target_index: int = TARGET_INDEX,
) -> bool:
    """Executes full harvest and Parquet dump for Auction Market Structure."""
    t0 = time.time()
    structure_records, pivot_records = harvest_auction_market_structure()
    if not structure_records:
        log.error("Zero auction records harvested.")
        return False

    all_records = list(structure_records)
    if pivot_records:
        all_records.extend(pivot_records)

    sys.path.insert(0, str(ROOT / 'Collectors' / 'Core'))
    sys.path.insert(0, str(ROOT / 'Terminal' / 'Data_Factory'))
    from parquet_feed_writer import write_parquet_feed
    meta = write_parquet_feed(sheet_name, all_records)
    elapsed = time.time() - t0
    log.info(f"Auction Market Structure completed in {elapsed:.2f}s with {len(all_records)} records ({meta.get('byte_size')} bytes).")
    return True


def main():
    parser = argparse.ArgumentParser(description="Auction Market Structure & Volume Profile Pure-Parquet Dumper")
    parser.add_argument("--sheet-name", default=TARGET_SHEET_NAME, help="Target feed name")
    args = parser.parse_args()

    ok = run_auction_module(sheet_name=args.sheet_name)
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
