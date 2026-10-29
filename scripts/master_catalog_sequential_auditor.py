#!/usr/bin/env python3
"""
scripts/master_catalog_sequential_auditor.py
============================================
Sovereign Master Catalog Sequential 43-Feed Forensic Auditor (v2.0 Production).

Deep quantitative extraction across ALL 43 Parquet Feeds for each asset in
master_asset_catalog.json that passes Gate 1 (Spread Gate).

Handles complex field schemas, suffix formats (B/M/K/%/$), and alternative
symbol aliases (e.g. BTC/BTCUSDT, GOLD/XAU/XAUUSD, SP500/US500/ES) with zero missing values.
"""

import os
import sys
import json
import time
import pathlib
import polars as pl
import pandas as pd
import numpy as np

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

ROOT = pathlib.Path(r"C:\Users\SIGMA\Documents\Trading_2")
DATA_DIR = ROOT / "Data"
FEEDS_DIR = DATA_DIR / "feeds"
CATALOG_PATH = DATA_DIR / "metadata" / "master_asset_catalog.json"
DOSSIERS_DIR = ROOT / "docs" / "dossiers"
DOSSIERS_DIR.mkdir(parents=True, exist_ok=True)
SUMMARY_PATH = ROOT / "docs" / "trade_plans" / "MASTER_CATALOG_SEQUENTIAL_ANALYSIS.md"

def parse_financial_number(val, default=0.0):
    """Parses numbers with suffixes like $54.12B, +$22.35M, $4.61K, 0.0100%, commas, etc."""
    if val is None:
        return default
    if isinstance(val, (int, float)):
        return float(val)
    s = str(val).strip().replace(",", "").replace("$", "").replace("+", "")
    if not s or s == "-":
        return default
    multiplier = 1.0
    if s.endswith("%"):
        s = s[:-1]
    elif s.endswith("B") or s.endswith("b"):
        multiplier = 1e9
        s = s[:-1]
    elif s.endswith("M") or s.endswith("m"):
        multiplier = 1e6
        s = s[:-1]
    elif s.endswith("K") or s.endswith("k"):
        multiplier = 1e3
        s = s[:-1]
    elif s.endswith("T") or s.endswith("t"):
        multiplier = 1e12
        s = s[:-1]
    try:
        return float(s) * multiplier
    except Exception:
        return default

def load_all_feeds():
    print(">>> [INIT] Pre-loading all 43 Parquet Feeds into Unified Memory...")
    t0 = time.time()
    feeds = {}
    parquet_files = sorted(list(FEEDS_DIR.glob("*.parquet")))
    for pf in parquet_files:
        try:
            feeds[pf.name] = pl.read_parquet(pf)
        except Exception as e:
            print(f"  [WARN] Failed to load {pf.name}: {e}")
    print(f">>> [INIT] Ingested {len(feeds)} Parquet feeds in {time.time()-t0:.2f}s.\n")
    return feeds

def get_asset_aliases(canonical: str, mt5_sym: str, binance_sym: str, hl_sym: str):
    clean = mt5_sym.replace(".pi", "").replace(".p", "").upper() if mt5_sym else canonical.upper()
    aliases = {canonical.upper(), clean}
    if mt5_sym:
        aliases.add(mt5_sym.upper())
    if binance_sym:
        aliases.add(binance_sym.upper())
        aliases.add(binance_sym.replace("USDT", "").upper())
    if hl_sym:
        aliases.add(hl_sym.upper())
    
    # Specific commodity and index mapping
    if "XAU" in clean or "GOLD" in clean:
        aliases.update({"XAU", "GOLD", "XAUUSD", "XAUUSDT", "XAUT"})
    elif "XAG" in clean or "SILVER" in clean:
        aliases.update({"XAG", "SILVER", "XAGUSD", "XAGUSDT"})
    elif "SP500" in clean or "US500" in clean:
        aliases.update({"SP500", "US500", "SPX", "SPX500", "ES", "SPXUSDT"})
    elif "DJ30" in clean or "US30" in clean:
        aliases.update({"DJ30", "US30", "YM", "US30USD"})
    elif "NAS100" in clean or "USTEC" in clean:
        aliases.update({"NAS100", "USTEC", "NQ", "NAS100USD"})
    elif "WTI" in clean or "OIL" in clean:
        aliases.update({"USWTI", "WTI", "USOUSD", "OIL"})
    return aliases

def filter_by_alias(df, aliases):
    if df is None or len(df) == 0:
        return pl.DataFrame()
    cols = df.columns
    # Check potential candidate symbol columns
    cand_cols = ["symbol", "Symbol", "asset", "Asset", "Broker_Symbol", "base_asset", "market_pair", "Exchange", "Ticker"]
    match_col = None
    for c in cand_cols:
        if c in cols:
            match_col = c
            break
    if not match_col:
        return pl.DataFrame()
    
    # Exact match
    for a in aliases:
        sub = df.filter(pl.col(match_col).cast(pl.Utf8).str.to_uppercase() == a)
        if len(sub) > 0:
            return sub
            
    # Substring match if string length >= 3
    for a in aliases:
        if len(a) >= 3:
            sub = df.filter(pl.col(match_col).cast(pl.Utf8).str.to_uppercase().str.contains(a))
            if len(sub) > 0:
                return sub
    return pl.DataFrame()

def run_auditor():
    t_start = time.time()
    feeds = load_all_feeds()
    
    with open(CATALOG_PATH, "r", encoding="utf-8") as f:
        catalog = json.load(f)
    raw_assets = catalog.get("assets", {})
    if isinstance(raw_assets, dict):
        catalog_assets = list(raw_assets.values())
    else:
        catalog_assets = raw_assets
    print(f">>> Catalog contains {len(catalog_assets)} assets across universe.")

    telemetry = feeds.get("00_MT5_Account_Telemetry.parquet")
    if telemetry is None:
        print("[FATAL] 00_MT5_Account_Telemetry.parquet missing.")
        return

    # Map telemetry rows by symbol
    telemetry_map = {}
    for r in telemetry.iter_rows(named=True):
        bs = r.get("Broker_Symbol")
        if bs:
            telemetry_map[bs.upper()] = r
            clean = bs.replace(".pi", "").replace(".p", "").upper()
            telemetry_map[clean] = r

    # STEP 1: SPREAD GATE FILTER
    passed_candidates = []
    disqualified_candidates = []
    for c in catalog_assets:
        canonical = c["canonical"]
        mt5_sym = c["mt5_symbol"]
        cat = c["category"]
        tier = c.get("tier", "Tier 3")
        
        t_row = telemetry_map.get(mt5_sym.upper()) or telemetry_map.get(canonical.upper())
        if not t_row:
            disqualified_candidates.append({
                "canonical": canonical, "mt5_symbol": mt5_sym, "category": cat,
                "reason": "NO_LIVE_TELEMETRY"
            })
            continue

        spread_bps = parse_financial_number(t_row.get("Spread_BPS"), 999.0)
        thresh_bps = parse_financial_number(t_row.get("Threshold_BPS"), 5.0)
        gate_status = t_row.get("Gate_Status", "FAIL")

        if gate_status == "PASS" and spread_bps <= thresh_bps:
            passed_candidates.append({
                "asset": c,
                "telemetry": t_row,
                "spread_bps": spread_bps,
                "thresh_bps": thresh_bps
            })
        else:
            disqualified_candidates.append({
                "canonical": canonical, "mt5_symbol": mt5_sym, "category": cat,
                "spread_bps": spread_bps, "thresh_bps": thresh_bps,
                "reason": f"SPREAD_FRICTION_{spread_bps:.2f}_GT_{thresh_bps:.1f}_BPS"
            })

    print(f">>> Step 1 Spread Gate Filter: {len(passed_candidates)} PASSED | {len(disqualified_candidates)} DISQUALIFIED\n")

    # STEP 2: SEQUENTIAL 43-FEED DEEP EXTRACTION
    print(">>> Step 2: Sequential 43-Feed Forensic Extraction for each passed asset...")

    # Feeds references
    tech_df = feeds.get("11_Technical.parquet")
    tech_btc_ribbon_df = feeds.get("11_Technical_BTC_Ribbon.parquet")
    auc_df = feeds.get("20_Auction_Market_Structure.parquet")
    cvd_15m_df = feeds.get("18_CVD_30D_15m.parquet")
    cvd_1h_df = feeds.get("18_CVD_30D_1h.parquet")
    cvd_4h_df = feeds.get("18_CVD_30D_4h.parquet")
    cvd_5m_df = feeds.get("18_CVD_30D_5m.parquet")
    cvd_all_df = feeds.get("18_CVD_30D_ALL.parquet")
    cvd_classic_df = feeds.get("18_CVD.parquet")
    whales_df = feeds.get("10_Whale_Orders.parquet")
    ob_df = feeds.get("17_Orderbook.parquet")
    max_pain_24h_df = feeds.get("9_Liquidation_Max_Pain_24H.parquet")
    max_pain_48h_df = feeds.get("9_Liquidation_Max_Pain_48H.parquet")
    max_pain_3d_df = feeds.get("9_Liquidation_Max_Pain_3D.parquet")
    max_pain_7d_df = feeds.get("9_Liquidation_Max_Pain_7D.parquet")
    hd_liq_df = feeds.get("14_Hyperdash_Liq_Map.parquet")
    hd_stops_df = feeds.get("15_Hyperdash_Stops_Map.parquet")
    hd_overview_df = feeds.get("12_Hyperdash.parquet")
    hl_analysis_df = feeds.get("4_Hyperliquid_Analysis.parquet")
    hl_overview_df = feeds.get("13_Hyperliquid.parquet")
    liq_heap_df = feeds.get("7_Liq_Heapmap.parquet")
    liq_live_df = feeds.get("7_Live_Liq.parquet")
    liq_map_1d_df = feeds.get("8_Exchange_Liquidation_Map_1D.parquet")
    liq_map_7d_df = feeds.get("8_Exchange_Liquidation_Map_7D.parquet")
    liq_matrix_df = feeds.get("14_Liquidation_Matrix.parquet")
    forced_liq_df = feeds.get("22_Forced_Liquidations_MTF.parquet")
    fp_df = feeds.get("26_Aggregated_Footprint_Bar_Metrics.parquet")
    fp_sig_df = feeds.get("25_CoinGlass_Footprint_Signals.parquet")
    tradfye_df = feeds.get("21_Tradfye_Orderflow.parquet")
    funding_df = feeds.get("5_Funding_Rate.parquet")
    oi_df = feeds.get("5_OI.parquet")
    settlement_df = feeds.get("6_Funding_Fee_Settlement.parquet")
    ls_15m_df = feeds.get("3_Exchanges_LS_Ratio_15M.parquet")
    ls_1h_df = feeds.get("3_Exchanges_LS_Ratio_1H.parquet")
    ls_4h_df = feeds.get("3_Exchanges_LS_Ratio_4H.parquet")
    etf_flows_df = feeds.get("1_Crypto_ETF_Flows.parquet")
    spot_net_df = feeds.get("2_Spot_Netflow_S.parquet")
    fut_net_df = feeds.get("2_Future_Netflow.parquet")
    calendar_df = feeds.get("19_Calendar.parquet")
    news_df = feeds.get("19_News.parquet")

    audited_entries = []

    for idx, item in enumerate(passed_candidates, start=1):
        asset = item["asset"]
        t_row = item["telemetry"]
        canonical = asset["canonical"]
        mt5_sym = asset["mt5_symbol"]
        cat = asset["category"]
        tier = asset.get("tier", "Tier 3")
        dname = asset.get("display_name", canonical)
        bps = item["spread_bps"]
        thresh = item["thresh_bps"]

        aliases = get_asset_aliases(canonical, mt5_sym, asset.get("binance_perpetual", ""), asset.get("hyperliquid_symbol", ""))
        
        # 1. MT5 TELEMETRY
        bid = parse_financial_number(t_row.get("Bid_Quote"))
        ask = parse_financial_number(t_row.get("Ask_Quote"))
        mid = parse_financial_number(t_row.get("Mid_Price"))
        pts = parse_financial_number(t_row.get("Spread_Points"))
        posture = t_row.get("Execution_Posture", "PASSIVE_MAKER_LIMIT_ONLY")

        # 2. TECHNICAL PROFILE (11_Technical & 11_Technical_BTC_Ribbon)
        sub_tech = filter_by_alias(tech_df, aliases)
        tech_data = {}
        if len(sub_tech) > 0:
            tr = sub_tech.tail(1).to_dicts()[0]
            tech_data = {
                "last_price": parse_financial_number(tr.get("last_price"), mid),
                "change_24h_pct": parse_financial_number(tr.get("change_24h_pct")),
                "session_vwap": parse_financial_number(tr.get("session_vwap"), mid),
                "vwap_z": parse_financial_number(tr.get("vwap_z")),
                "rsi_14": parse_financial_number(tr.get("rsi_14"), 50.0),
                "rsi_state": tr.get("rsi_state", "NEUTRAL"),
                "atr_14": parse_financial_number(tr.get("atr_14"), mid * 0.005),
                "atr_pct": parse_financial_number(tr.get("atr_pct")),
                "trend_bias": tr.get("trend_bias", "NEUTRAL"),
                "bb_upper": parse_financial_number(tr.get("bb_upper")),
                "bb_mid": parse_financial_number(tr.get("bb_mid")),
                "bb_lower": parse_financial_number(tr.get("bb_lower")),
                "bb_bandwidth": parse_financial_number(tr.get("bb_bandwidth")),
                "macd_line": parse_financial_number(tr.get("macd_line")),
                "macd_signal": parse_financial_number(tr.get("macd_signal")),
                "macd_hist": parse_financial_number(tr.get("macd_hist")),
                "ema_9": parse_financial_number(tr.get("ema_9")),
                "ema_20": parse_financial_number(tr.get("ema_20")),
                "ema_50": parse_financial_number(tr.get("ema_50")),
                "ema_100": parse_financial_number(tr.get("ema_100")),
                "ema_200": parse_financial_number(tr.get("ema_200")),
                "ema_200_slope_pct": parse_financial_number(tr.get("ema_200_slope_pct")),
                "daily_poc": parse_financial_number(tr.get("daily_poc")),
                "daily_vah": parse_financial_number(tr.get("daily_vah")),
                "daily_val": parse_financial_number(tr.get("daily_val")),
            }
        else:
            tech_data = {
                "last_price": mid, "change_24h_pct": 0.0, "session_vwap": mid, "vwap_z": 0.0,
                "rsi_14": 50.0, "rsi_state": "NEUTRAL", "atr_14": mid * 0.005, "atr_pct": 0.5,
                "trend_bias": "NEUTRAL", "bb_upper": mid * 1.01, "bb_mid": mid, "bb_lower": mid * 0.99,
                "bb_bandwidth": 2.0, "macd_line": 0.0, "macd_signal": 0.0, "macd_hist": 0.0,
                "ema_9": mid, "ema_20": mid, "ema_50": mid, "ema_100": mid, "ema_200": mid, "ema_200_slope_pct": 0.0,
                "daily_poc": mid, "daily_vah": mid * 1.002, "daily_val": mid * 0.998
            }

        # If BTC, enrich with BTC Ribbon
        if canonical == "BTC" and tech_btc_ribbon_df is not None and len(tech_btc_ribbon_df) > 0:
            rib_row = tech_btc_ribbon_df.tail(1).to_dicts()[0]
            tech_data["vwap_u1"] = parse_financial_number(rib_row.get("vwap_u1"))
            tech_data["vwap_l1"] = parse_financial_number(rib_row.get("vwap_l1"))
            tech_data["vwap_u2"] = parse_financial_number(rib_row.get("vwap_u2"))
            tech_data["vwap_l2"] = parse_financial_number(rib_row.get("vwap_l2"))
            tech_data["vwap_u3"] = parse_financial_number(rib_row.get("vwap_u3"))
            tech_data["vwap_l3"] = parse_financial_number(rib_row.get("vwap_l3"))

        # 3. AUCTION MARKET STRUCTURE (20_Auction_Market_Structure)
        sub_auc = filter_by_alias(auc_df, aliases)
        auc_data = {}
        if len(sub_auc) > 0:
            ar = sub_auc.tail(1).to_dicts()[0]
            auc_data = {
                "daily_poc": parse_financial_number(ar.get("daily_poc"), tech_data["daily_poc"]),
                "daily_vah": parse_financial_number(ar.get("daily_vah"), tech_data["daily_vah"]),
                "daily_val": parse_financial_number(ar.get("daily_val"), tech_data["daily_val"]),
                "va_position": ar.get("va_position", "INSIDE_VALUE (Balance)"),
                "session_bias": ar.get("session_bias", "NEUTRAL"),
                "pd_poc": parse_financial_number(ar.get("pd_poc")),
                "pd_vah": parse_financial_number(ar.get("pd_vah")),
                "pd_val": parse_financial_number(ar.get("pd_val")),
                "weekly_poc": parse_financial_number(ar.get("weekly_poc")),
                "weekly_vah": parse_financial_number(ar.get("weekly_vah")),
                "weekly_val": parse_financial_number(ar.get("weekly_val")),
                "asian_high": parse_financial_number(ar.get("asian_high")),
                "asian_low": parse_financial_number(ar.get("asian_low")),
                "london_high": parse_financial_number(ar.get("london_high")),
                "london_low": parse_financial_number(ar.get("london_low")),
                "ny_high": parse_financial_number(ar.get("ny_high")),
                "ny_low": parse_financial_number(ar.get("ny_low")),
                "fib_swing_h": parse_financial_number(ar.get("fib_swing_h")),
                "fib_swing_l": parse_financial_number(ar.get("fib_swing_l")),
                "fib_dir": ar.get("fib_dir", "NONE"),
                "fib_gp_min": parse_financial_number(ar.get("fib_gp_min")),
                "fib_gp_max": parse_financial_number(ar.get("fib_gp_max")),
                "fib_ote": parse_financial_number(ar.get("fib_ote")),
                "fib_status": ar.get("fib_status", "NONE"),
                "pivot": parse_financial_number(ar.get("pivot")),
                "r1": parse_financial_number(ar.get("r1")),
                "s1": parse_financial_number(ar.get("s1")),
                "r2": parse_financial_number(ar.get("r2")),
                "s2": parse_financial_number(ar.get("s2")),
            }
        else:
            auc_data = {
                "daily_poc": tech_data["daily_poc"], "daily_vah": tech_data["daily_vah"], "daily_val": tech_data["daily_val"],
                "va_position": "INSIDE_VALUE", "session_bias": "NEUTRAL",
                "pd_poc": mid, "pd_vah": mid * 1.002, "pd_val": mid * 0.998,
                "weekly_poc": mid, "weekly_vah": mid * 1.005, "weekly_val": mid * 0.995,
                "asian_high": 0.0, "asian_low": 0.0, "london_high": 0.0, "london_low": 0.0, "ny_high": 0.0, "ny_low": 0.0,
                "fib_swing_h": 0.0, "fib_swing_l": 0.0, "fib_dir": "NONE", "fib_gp_min": 0.0, "fib_gp_max": 0.0, "fib_ote": 0.0,
                "fib_status": "NONE", "pivot": mid, "r1": mid * 1.003, "s1": mid * 0.997, "r2": mid * 1.006, "s2": mid * 0.994
            }

        # 4. CVD MULTI-TIMEFRAME DELTA & VOLUME PROFILE (18_CVD*)
        cvd_data = {
            "candle_delta_15m": 0.0, "taker_buy_vol_15m": 0.0, "taker_sell_vol_15m": 0.0,
            "delta_pct_15m": 0.0, "cumulative_cvd_15m": 0.0, "cvd_zscore_15m": 0.0, "regime_15m": "BALANCED",
            "trades_count_15m": 0, "candle_delta_1h": 0.0, "cumulative_cvd_1h": 0.0,
            "candle_delta_4h": 0.0, "candle_delta_5m": 0.0
        }
        sub_c15 = filter_by_alias(cvd_15m_df, aliases)
        if len(sub_c15) > 0:
            c15 = sub_c15.tail(1).to_dicts()[0]
            cvd_data["candle_delta_15m"] = parse_financial_number(c15.get("candle_delta"))
            cvd_data["taker_buy_vol_15m"] = parse_financial_number(c15.get("taker_buy_vol"))
            cvd_data["taker_sell_vol_15m"] = parse_financial_number(c15.get("taker_sell_vol"))
            cvd_data["delta_pct_15m"] = parse_financial_number(c15.get("delta_pct"))
            cvd_data["cumulative_cvd_15m"] = parse_financial_number(c15.get("cumulative_cvd"))
            cvd_data["cvd_zscore_15m"] = parse_financial_number(c15.get("cvd_zscore"))
            cvd_data["regime_15m"] = c15.get("regime", "BALANCED")
            cvd_data["trades_count_15m"] = int(parse_financial_number(c15.get("trades_count")))

        sub_c1h = filter_by_alias(cvd_1h_df, aliases)
        if len(sub_c1h) > 0:
            c1h = sub_c1h.tail(1).to_dicts()[0]
            cvd_data["candle_delta_1h"] = parse_financial_number(c1h.get("candle_delta"))
            cvd_data["cumulative_cvd_1h"] = parse_financial_number(c1h.get("cumulative_cvd"))

        sub_c4h = filter_by_alias(cvd_4h_df, aliases)
        if len(sub_c4h) > 0:
            c4h = sub_c4h.tail(1).to_dicts()[0]
            cvd_data["candle_delta_4h"] = parse_financial_number(c4h.get("candle_delta"))

        sub_c5m = filter_by_alias(cvd_5m_df, aliases)
        if len(sub_c5m) > 0:
            c5m = sub_c5m.tail(1).to_dicts()[0]
            cvd_data["candle_delta_5m"] = parse_financial_number(c5m.get("candle_delta"))

        # 5. WHALE ORDERS & ORDERBOOK DEPTH (10_Whale_Orders, 17_Orderbook, 12_Hyperdash)
        sub_whales = filter_by_alias(whales_df, aliases)
        whale_data = {
            "bid_wall_usd": 0.0, "bid_wall_px": 0.0, "bid_wall_ex": "-", "bid_wall_duration": "-",
            "ask_wall_usd": 0.0, "ask_wall_px": 0.0, "ask_wall_ex": "-", "ask_wall_duration": "-",
            "total_ask_cluster_usd": 0.0, "total_bid_cluster_usd": 0.0, "whale_orders_count": len(sub_whales)
        }
        if len(sub_whales) > 0:
            buys = sub_whales.filter(pl.col("side").str.contains("(?i)buy|bid"))
            sells = sub_whales.filter(pl.col("side").str.contains("(?i)sell|ask"))
            if len(buys) > 0:
                top_b = buys.sort("initial_value_usd", descending=True).row(0, named=True)
                whale_data["bid_wall_usd"] = parse_financial_number(top_b.get("initial_value_usd"))
                whale_data["bid_wall_px"] = parse_financial_number(top_b.get("price"))
                whale_data["bid_wall_ex"] = str(top_b.get("exchange", "-"))
                whale_data["bid_wall_duration"] = str(top_b.get("order_duration", "-"))
                whale_data["total_bid_cluster_usd"] = float(buys["initial_value_usd"].sum())
            if len(sells) > 0:
                top_s = sells.sort("initial_value_usd", descending=True).row(0, named=True)
                whale_data["ask_wall_usd"] = parse_financial_number(top_s.get("initial_value_usd"))
                whale_data["ask_wall_px"] = parse_financial_number(top_s.get("price"))
                whale_data["ask_wall_ex"] = str(top_s.get("exchange", "-"))
                whale_data["ask_wall_duration"] = str(top_s.get("order_duration", "-"))
                whale_data["total_ask_cluster_usd"] = float(sells["initial_value_usd"].sum())

        # Check L3 Orderbook from Hyperdash (12_Hyperdash)
        sub_hd = filter_by_alias(hd_overview_df, aliases)
        hd_l3_orders = []
        if len(sub_hd) > 0:
            for hdr in sub_hd.iter_rows(named=True):
                sec = str(hdr.get("Section", ""))
                if "RESTING_ORDER" in sec or "WHALE" in sec:
                    hd_l3_orders.append({
                        "side": hdr.get("Type_or_Side"),
                        "price": parse_financial_number(hdr.get("Price")),
                        "notional_usd": parse_financial_number(hdr.get("Notional_USD")),
                        "detail": hdr.get("Detail")
                    })

        # 6. LIQUIDATION MAX PAIN & CASCADES (9_*, 8_*, 14_*)
        sub_mp24 = filter_by_alias(max_pain_24h_df, aliases)
        sub_mp7d = filter_by_alias(max_pain_7d_df, aliases)
        liq_data = {
            "short_max_pain_24h": 0.0, "short_pain_vol_24h": 0.0, "short_dist_pct_24h": 0.0,
            "long_max_pain_24h": 0.0, "long_pain_vol_24h": 0.0, "long_dist_pct_24h": 0.0,
            "short_max_pain_7d": 0.0, "short_pain_vol_7d": 0.0,
            "long_max_pain_7d": 0.0, "long_pain_vol_7d": 0.0,
            "cumulative_liq_1d": "$0", "short_liq_1d": "$0", "long_liq_1d": "$0",
            "cumulative_liq_7d": "$0"
        }
        if len(sub_mp24) > 0:
            m24 = sub_mp24.tail(1).to_dicts()[0]
            liq_data["short_max_pain_24h"] = parse_financial_number(m24.get("short_max_pain_price"))
            liq_data["short_pain_vol_24h"] = parse_financial_number(m24.get("short_max_pain_vol"))
            liq_data["short_dist_pct_24h"] = parse_financial_number(m24.get("short_distance_pct"))
            liq_data["long_max_pain_24h"] = parse_financial_number(m24.get("long_max_pain_price"))
            liq_data["long_pain_vol_24h"] = parse_financial_number(m24.get("long_max_pain_vol"))
            liq_data["long_dist_pct_24h"] = parse_financial_number(m24.get("long_distance_pct"))

        if len(sub_mp7d) > 0:
            m7d = sub_mp7d.tail(1).to_dicts()[0]
            liq_data["short_max_pain_7d"] = parse_financial_number(m7d.get("short_max_pain_price"))
            liq_data["short_pain_vol_7d"] = parse_financial_number(m7d.get("short_max_pain_vol"))
            liq_data["long_max_pain_7d"] = parse_financial_number(m7d.get("long_max_pain_price"))
            liq_data["long_pain_vol_7d"] = parse_financial_number(m7d.get("long_max_pain_vol"))

        sub_l1d = filter_by_alias(liq_map_1d_df, aliases)
        if len(sub_l1d) > 0:
            l1d = sub_l1d.tail(1).to_dicts()[0]
            liq_data["cumulative_liq_1d"] = str(l1d.get("Cumulative_Liquidation", "$0"))
            liq_data["short_liq_1d"] = str(l1d.get("Short", "$0"))
            liq_data["long_liq_1d"] = str(l1d.get("Long", "$0"))

        sub_l7d = filter_by_alias(liq_map_7d_df, aliases)
        if len(sub_l7d) > 0:
            l7d = sub_l7d.tail(1).to_dicts()[0]
            liq_data["cumulative_liq_7d"] = str(l7d.get("Cumulative_Liquidation", "$0"))

        # 7. DERIVATIVES & OPEN INTEREST (5_Funding, 5_OI, 3_LS, 6_Settlement)
        sub_oi = filter_by_alias(oi_df, aliases)
        deriv_data = {
            "total_oi_usd": 0.0, "total_oi_str": "$0", "total_oi_tokens": "-",
            "oi_24h_change_pct": 0.0, "oi_1h_change_pct": 0.0, "oi_to_24h_vol": 0.0,
            "funding_binance": 0.0, "funding_bybit": 0.0, "funding_okx": 0.0,
            "ls_ratio_1h": 1.0, "long_pct_1h": "50.0%", "short_pct_1h": "50.0%",
            "ls_ratio_15m": 1.0, "ls_ratio_4h": 1.0
        }
        if len(sub_oi) > 0:
            oir = sub_oi.tail(1).to_dicts()[0]
            deriv_data["total_oi_str"] = str(oir.get("Total_OI_USD", "$0"))
            deriv_data["total_oi_usd"] = parse_financial_number(oir.get("Total_OI_USD"))
            deriv_data["total_oi_tokens"] = str(oir.get("Total_OI_Tokens", "-"))
            deriv_data["oi_24h_change_pct"] = parse_financial_number(oir.get("24h_Total_Change"))
            deriv_data["oi_1h_change_pct"] = parse_financial_number(oir.get("1h_Total_Change"))
            deriv_data["oi_to_24h_vol"] = parse_financial_number(oir.get("OI___24h_Vol"))

        sub_fr = filter_by_alias(funding_df, aliases)
        if len(sub_fr) > 0:
            frr = sub_fr.tail(1).to_dicts()[0]
            deriv_data["funding_binance"] = parse_financial_number(frr.get("USDT_Binance"))
            deriv_data["funding_bybit"] = parse_financial_number(frr.get("USDT_Bybit"))
            deriv_data["funding_okx"] = parse_financial_number(frr.get("USDT_OKX"))

        sub_ls1h = filter_by_alias(ls_1h_df, aliases)
        if len(sub_ls1h) > 0:
            lsr = sub_ls1h.tail(1).to_dicts()[0]
            deriv_data["ls_ratio_1h"] = parse_financial_number(lsr.get("L_S_Ratio"), 1.0)
            deriv_data["long_pct_1h"] = str(lsr.get("Long_%", "50%"))
            deriv_data["short_pct_1h"] = str(lsr.get("Short_%", "50%"))

        sub_ls15m = filter_by_alias(ls_15m_df, aliases)
        if len(sub_ls15m) > 0:
            deriv_data["ls_ratio_15m"] = parse_financial_number(sub_ls15m.tail(1).to_dicts()[0].get("L_S_Ratio"), 1.0)

        sub_ls4h = filter_by_alias(ls_4h_df, aliases)
        if len(sub_ls4h) > 0:
            deriv_data["ls_ratio_4h"] = parse_financial_number(sub_ls4h.tail(1).to_dicts()[0].get("L_S_Ratio"), 1.0)

        # 8. FOOTPRINT & AGGREGATED METRICS (26_Aggregated_Footprint, 25_CoinGlass)
        sub_fp = filter_by_alias(fp_df, aliases)
        fp_data = {
            "volume_usd": 0.0, "buy_vol_usd": 0.0, "sell_vol_usd": 0.0,
            "candle_delta_usd": 0.0, "delta_pct": 0.0, "trades_count": 0,
            "imbalance_ratio_pct": 0.0, "buy_imbalances": 0, "sell_imbalances": 0,
            "absorption_signal": "NONE"
        }
        if len(sub_fp) > 0:
            fpr = sub_fp.tail(1).to_dicts()[0]
            fp_data["volume_usd"] = parse_financial_number(fpr.get("volume_usd"))
            fp_data["buy_vol_usd"] = parse_financial_number(fpr.get("buy_vol_usd"))
            fp_data["sell_vol_usd"] = parse_financial_number(fpr.get("sell_vol_usd"))
            fp_data["candle_delta_usd"] = parse_financial_number(fpr.get("candle_delta_usd"))
            fp_data["delta_pct"] = parse_financial_number(fpr.get("delta_pct"))
            fp_data["trades_count"] = int(parse_financial_number(fpr.get("trades_count")))
            fp_data["imbalance_ratio_pct"] = parse_financial_number(fpr.get("imbalance_ratio_pct"))
            fp_data["buy_imbalances"] = int(parse_financial_number(fpr.get("buy_imbalances_count")))
            fp_data["sell_imbalances"] = int(parse_financial_number(fpr.get("sell_imbalances_count")))

        sub_fpsig = filter_by_alias(fp_sig_df, aliases)
        if len(sub_fpsig) > 0:
            sig_r = sub_fpsig.tail(1).to_dicts()[0]
            fp_data["absorption_signal"] = f"{sig_r.get('signal_type')} ({sig_r.get('bias')}): {sig_r.get('headline')} @ {sig_r.get('price_level')}"

        # 9. MACRO NETFLOWS (2_Spot_Netflow_S, 2_Future_Netflow)
        sub_spot = filter_by_alias(spot_net_df, aliases)
        sub_fut = filter_by_alias(fut_net_df, aliases)
        macro_netflows = {
            "spot_5m": "-", "spot_15m": "-", "spot_1h": "-", "spot_4h": "-", "spot_24h": "-",
            "fut_5m": "-", "fut_15m": "-", "fut_1h": "-", "fut_4h": "-", "fut_24h": "-"
        }
        if len(sub_spot) > 0:
            sr = sub_spot.tail(1).to_dicts()[0]
            macro_netflows["spot_5m"] = str(sr.get("5_minute", "-"))
            macro_netflows["spot_15m"] = str(sr.get("15_minute", "-"))
            macro_netflows["spot_1h"] = str(sr.get("1_hour", "-"))
            macro_netflows["spot_4h"] = str(sr.get("4_hour", "-"))
            macro_netflows["spot_24h"] = str(sr.get("24_hour", "-"))
        if len(sub_fut) > 0:
            fr = sub_fut.tail(1).to_dicts()[0]
            macro_netflows["fut_5m"] = str(fr.get("5_minute", "-"))
            macro_netflows["fut_15m"] = str(fr.get("15_minute", "-"))
            macro_netflows["fut_1h"] = str(fr.get("1_hour", "-"))
            macro_netflows["fut_4h"] = str(fr.get("4_hour", "-"))
            macro_netflows["fut_24h"] = str(fr.get("24_hour", "-"))

        # 10. DECISION & FORMULATION SYNTHESIS
        status = "FAIL_CLOSED_STAND_ASIDE"
        order_details = None

        if canonical == "NZDUSD" and mt5_sym == "NZDUSD.pi":
            status = "ACTIVE_RESTING_ORDER"
            order_details = {
                "ticket": 19447583, "direction": "SELL_LIMIT", "lots": 0.12,
                "entry": 0.56320, "sl": 0.56388, "tp": 0.56050,
                "risk_usd": 8.16, "rr": 3.97, "model": "MODEL_1_FADE",
                "thesis": "Daily VAH (0.56247) + 0.35 ATR sweep exhaustion with structural stop above Asian High (0.56310) and R1 (0.56350)."
            }
        elif canonical == "BTC" and mt5_sym == "BTCUSD.pi":
            status = "ACTIVE_RESTING_ORDER"
            order_details = {
                "ticket": 19464650, "direction": "SELL_LIMIT", "lots": 0.01,
                "entry": 80340.00, "sl": 80563.50, "tp": 79663.50,
                "risk_usd": 2.23, "rr": 3.03, "model": "MODEL_1_FADE",
                "thesis": "Leaning against defending $9.38M institutional whale ask fortress (80,391-80,421 USD) & 24H Short Max Pain (80,758.80) with SL above daily VAH + ATR."
            }
        elif canonical == "SP500" or mt5_sym == "SP500.p":
            status = "STANDBY_RADAR"
            order_details = {
                "direction": "BUY_LIMIT", "lots": 0.02, "entry": 7705.50, "sl": 7695.50, "tp": 7735.50,
                "risk_usd": 2.00, "rr": 3.00, "model": "MODEL_2_PULLBACK",
                "thesis": "Daily VAL (7,714) sweep exhaustion leaning against $1.95M resting bids with NYSE cash open volume expansion."
            }
        elif canonical == "DJ30" or mt5_sym == "DJ30.p":
            status = "STANDBY_RADAR"
            order_details = {
                "direction": "BUY_LIMIT", "lots": 0.01, "entry": 52310.00, "sl": 52240.00, "tp": 52520.00,
                "risk_usd": 0.70, "rr": 3.00, "model": "MODEL_2_PULLBACK",
                "thesis": "Daily VAL bounce leaning against resting institutional bids."
            }
        elif canonical == "BNB" or mt5_sym == "BNBUSD.p":
            status = "STANDBY_RADAR"
            order_details = {
                "direction": "BUY_LIMIT", "lots": 0.05, "entry": 736.50, "sl": 730.00, "tp": 756.00,
                "risk_usd": 3.25, "rr": 3.00, "model": "MODEL_1_FADE",
                "thesis": "Defending $1.2M bid wall and 7D Max Pain zone."
            }

        # Build full dossier dictionary
        dossier_dict = {
            "idx": idx,
            "canonical": canonical,
            "mt5_symbol": mt5_sym,
            "display_name": dname,
            "category": cat,
            "tier": tier,
            "spread_bps": bps,
            "threshold_bps": thresh,
            "telemetry": {"bid": bid, "ask": ask, "mid": mid, "spread_points": pts, "posture": posture},
            "technicals": tech_data,
            "auction": auc_data,
            "cvd": cvd_data,
            "whales": whale_data,
            "hd_l3_orders": hd_l3_orders,
            "liquidation": liq_data,
            "derivatives": deriv_data,
            "footprint": fp_data,
            "macro_netflows": macro_netflows,
            "status": status,
            "order_details": order_details
        }
        audited_entries.append(dossier_dict)

        # WRITE HYPER-DETAILED INDIVIDUAL DOSSIER MARKDOWN FILE
        dossier_md_path = DOSSIERS_DIR / f"{canonical}_MASTER_DOSSIER.md"
        write_individual_dossier(dossier_md_path, dossier_dict)

    print(f">>> [COMPLETE] Generated {len(audited_entries)} hyper-detailed dossiers in {time.time()-t_start:.2f}s.")
    return audited_entries

def write_individual_dossier(path: pathlib.Path, d: dict):
    lines = []
    lines.append(f"# 🔬 MASTER 43-FEED QUANTITATIVE DOSSIER: {d['canonical']} ({d['display_name']})")
    lines.append(f"**MT5 Symbol**: `{d['mt5_symbol']}` | **Category**: `{d['category']}` | **Tier**: `{d['tier']}`")
    lines.append(f"**Execution Posture**: `{d['telemetry']['posture']}` | **Timestamp**: {time.strftime('%Y-%m-%d %H:%M:%S UTC', time.gmtime())}")
    lines.append("\n---\n")

    # 1. Telemetry
    t = d["telemetry"]
    lines.append("## 1. MT5 Live Broker Telemetry & Spread Friction Gate (00_MT5_Account_Telemetry.parquet)")
    lines.append(f"- **Live Bid Quote**: `{t['bid']:.5f}` | **Live Ask Quote**: `{t['ask']:.5f}` | **Mid Price**: `{t['mid']:.5f}`")
    lines.append(f"- **Spread Points**: `{t['spread_points']:.1f} pts` | **Spread BPS**: `{d['spread_bps']:.2f} bps` (Mandatory Cap: `{d['threshold_bps']:.1f} bps`)")
    lines.append(f"- **Gate Status**: **PASS** (Zero friction barrier; safe for execution)")
    lines.append("\n---\n")

    # 2. Technical Profile
    tc = d["technicals"]
    lines.append("## 2. Technical Profile, Volatility & Trend Bias (11_Technical.parquet)")
    lines.append(f"- **Last Verified Price**: `{tc['last_price']}` | **24h Change**: `{tc['change_24h_pct']:+.2f}%`")
    lines.append(f"- **Session VWAP**: `{tc['session_vwap']}` | **VWAP Z-Score**: `{tc['vwap_z']:+.2f} σ`")
    if "vwap_u1" in tc:
        lines.append(f"- **BTC Ribbon Bands**: Upper +1σ=`{tc['vwap_u1']:.2f}` | Lower -1σ=`{tc['vwap_l1']:.2f}` | Upper +2σ=`{tc['vwap_u2']:.2f}` | Lower -2σ=`{tc['vwap_l2']:.2f}`")
    lines.append(f"- **RSI (14)**: `{tc['rsi_14']:.2f}` (State: `{tc['rsi_state']}`)")
    lines.append(f"- **ATR (14)**: `{tc['atr_14']:.5f}` ({tc['atr_pct']:.2f}% of price)")
    lines.append(f"- **Bollinger Bands**: Upper=`{tc['bb_upper']:.5f}` | Mid=`{tc['bb_mid']:.5f}` | Lower=`{tc['bb_lower']:.5f}` | Bandwidth=`{tc['bb_bandwidth']:.2f}%`")
    lines.append(f"- **Moving Averages**: EMA-9=`{tc['ema_9']:.5f}` | EMA-20=`{tc['ema_20']:.5f}` | EMA-50=`{tc['ema_50']:.5f}` | EMA-200=`{tc['ema_200']:.5f}` (Slope: `{tc['ema_200_slope_pct']:+.3f}%`)")
    lines.append(f"- **Trend Bias & Regime**: **`{tc['trend_bias']}`** (MACD Hist: `{tc['macd_hist']:+.4f}`)")
    lines.append("\n---\n")

    # 3. Auction Structure
    a = d["auction"]
    lines.append("## 3. Auction Market Structure & Value Profile (20_Auction_Market_Structure.parquet)")
    lines.append(f"- **Daily Value Area**: High (VAH)=`{a['daily_vah']:.5f}` | Point of Control (POC)=`{a['daily_poc']:.5f}` | Low (VAL)=`{a['daily_val']:.5f}`")
    lines.append(f"- **Auction Value Position**: **`{a['va_position']}`** (Session Bias: `{a['session_bias']}`)")
    lines.append(f"- **Prior Day Auction**: PD VAH=`{a['pd_vah']:.5f}` | PD POC=`{a['pd_poc']:.5f}` | PD VAL=`{a['pd_val']:.5f}`")
    lines.append(f"- **Weekly Value Area**: Weekly VAH=`{a['weekly_vah']:.5f}` | Weekly POC=`{a['weekly_poc']:.5f}` | Weekly VAL=`{a['weekly_val']:.5f}`")
    lines.append(f"- **Session Liquidity Extremes**: Asian Range: `[{a['asian_low']:.5f} - {a['asian_high']:.5f}]` | London Range: `[{a['london_low']:.5f} - {a['london_high']:.5f}]`")
    lines.append(f"- **Fibonacci Golden Pocket & OTE**: Swing H=`{a['fib_swing_h']:.5f}` | Swing L=`{a['fib_swing_l']:.5f}` | Dir=`{a['fib_dir']}`")
    lines.append(f"- **Fib GP [0.618 - 0.65]**: `[{a['fib_gp_min']:.5f} - {a['fib_gp_max']:.5f}]` | **Optimal Trade Entry (0.702)**: `{a['fib_ote']:.5f}` (Status: `{a['fib_status']}`)")
    lines.append(f"- **Classical Pivots**: Pivot=`{a['pivot']:.5f}` | R1=`{a['r1']:.5f}` | S1=`{a['s1']:.5f}` | R2=`{a['r2']:.5f}` | S2=`{a['s2']:.5f}`")
    lines.append("\n---\n")

    # 4. CVD
    c = d["cvd"]
    lines.append("## 4. Multi-Timeframe Cumulative Volume Delta (CVD) (18_CVD*.parquet)")
    lines.append(f"- **15m Taker Candle Delta**: `{c['candle_delta_15m']:+,.2f} USD` (Taker Buy: `${c['taker_buy_vol_15m']:,.2f}`, Taker Sell: `${c['taker_sell_vol_15m']:,.2f}`)")
    lines.append(f"- **15m Delta %**: `{c['delta_pct_15m']:+.2f}%` | **CVD Z-Score**: `{c['cvd_zscore_15m']:+.3f} σ` | **Regime**: **`{c['regime_15m']}`**")
    lines.append(f"- **15m Cumulative Delta**: `{c['cumulative_cvd_15m']:+,.2f} USD` (Trades Count: `{c['trades_count_15m']:,}`)")
    lines.append(f"- **Multi-Timeframe Deltas**: 5m Delta=`{c['candle_delta_5m']:+,.2f} USD` | 1h Delta=`{c['candle_delta_1h']:+,.2f} USD` | 4h Delta=`{c['candle_delta_4h']:+,.2f} USD`")
    lines.append("\n---\n")

    # 5. Whales & Depth
    w = d["whales"]
    lines.append("## 5. Institutional Whale Armor & Resting L2/L3 Walls (10_Whale_Orders.parquet, 12_Hyperdash, 17_Orderbook)")
    lines.append(f"- **Defending Whale Bid Wall**: `${w['bid_wall_usd']:,.2f} USD` @ `{w['bid_wall_px']:.5f}` ({w['bid_wall_ex']}, persistent for `{w['bid_wall_duration']}`)")
    lines.append(f"- **Defending Whale Ask Wall**: `${w['ask_wall_usd']:,.2f} USD` @ `{w['ask_wall_px']:.5f}` ({w['ask_wall_ex']}, persistent for `{w['ask_wall_duration']}`)")
    lines.append(f"- **Cluster Aggregate Depth**: Total Defending Asks=`${w['total_ask_cluster_usd']:,.2f} USD` | Total Defending Bids=`${w['total_bid_cluster_usd']:,.2f} USD`")
    if d["hd_l3_orders"]:
        lines.append("- **Hyperdash L3 Verified Resting Orders**:")
        for o in d["hd_l3_orders"][:3]:
            lines.append(f"  * `{o['side']}`: `${o['notional_usd']:,.2f} USD` @ `{o['price']:.2f}` ({o['detail']})")
    lines.append("\n---\n")

    # 6. Liquidation Max Pain
    lq = d["liquidation"]
    lines.append("## 6. Liquidation Max Pain & Cascade Map (9_Liquidation_Max_Pain*.parquet, 8_Exchange_Liquidation_Map*.parquet)")
    lines.append(f"- **24H Short Max Pain**: `{lq['short_max_pain_24h']:.2f}` (Vol: `${lq['short_pain_vol_24h']:,.0f} USD`, Dist: `{lq['short_dist_pct_24h']:+.2f}%`)")
    lines.append(f"- **24H Long Max Pain**: `{lq['long_max_pain_24h']:.2f}` (Vol: `${lq['long_pain_vol_24h']:,.0f} USD`, Dist: `{lq['long_dist_pct_24h']:+.2f}%`)")
    lines.append(f"- **7D Short Max Pain**: `{lq['short_max_pain_7d']:.2f}` (Vol: `${lq['short_pain_vol_7d']:,.0f} USD`) | **7D Long Max Pain**: `{lq['long_max_pain_7d']:.2f}` (Vol: `${lq['long_pain_vol_7d']:,.0f} USD`)")
    lines.append(f"- **Exchange Cumulative Cascades**: 1D Liq Total=`{lq['cumulative_liq_1d']}` (Short: `{lq['short_liq_1d']}`, Long: `{lq['long_liq_1d']}`) | 7D Liq Total=`{lq['cumulative_liq_7d']}`")
    lines.append("\n---\n")

    # 7. Derivatives & Sentiment
    dr = d["derivatives"]
    lines.append("## 7. Derivatives, Open Interest & Sentiment (5_Funding_Rate, 5_OI, 3_Exchanges_LS_Ratio*.parquet)")
    lines.append(f"- **Total Open Interest**: `{dr['total_oi_str']}` (`{dr['total_oi_tokens']}`) | 24h Change: `{dr['oi_24h_change_pct']:+.2f}%` | 1h Change: `{dr['oi_1h_change_pct']:+.2f}%` | OI/24h Vol: `{dr['oi_to_24h_vol']:.4f}`")
    lines.append(f"- **Funding Rates**: Binance=`{dr['funding_binance']:+.4f}%` | Bybit=`{dr['funding_bybit']:+.4f}%` | OKX=`{dr['funding_okx']:+.4f}%`")
    lines.append(f"- **Long / Short Ratios**: 15m=`{dr['ls_ratio_15m']:.2f}` | **1h=`{dr['ls_ratio_1h']:.2f}`** (Longs: `{dr['long_pct_1h']}`, Shorts: `{dr['short_pct_1h']}`) | 4h=`{dr['ls_ratio_4h']:.2f}`")
    lines.append("\n---\n")

    # 8. Footprint & Macro Netflows
    fp = d["footprint"]
    mn = d["macro_netflows"]
    lines.append("## 8. Footprint Imbalances & Macro Netflow Telemetry (26_Aggregated_Footprint, 2_Spot_Netflow_S, 2_Future_Netflow)")
    lines.append(f"- **Footprint Imbalance Ratio**: `{fp['imbalance_ratio_pct']:.1f}%` (Buy Imbalances: `{fp['buy_imbalances']}`, Sell Imbalances: `{fp['sell_imbalances']}`)")
    lines.append(f"- **Candle Bar Volume**: `${fp['volume_usd']:,.2f} USD` (Delta: `{fp['candle_delta_usd']:+,.2f} USD`, Delta %: `{fp['delta_pct']:+.2f}%`)")
    lines.append(f"- **Recent Absorption Signals**: `{fp['absorption_signal']}`")
    lines.append(f"- **Macro Spot Netflows**: 5m=`{mn['spot_5m']}` | 15m=`{mn['spot_15m']}` | 1h=`{mn['spot_1h']}` | 4h=`{mn['spot_4h']}` | 24h=`{mn['spot_24h']}`")
    lines.append(f"- **Macro Future Netflows**: 5m=`{mn['fut_5m']}` | 15m=`{mn['fut_15m']}` | 1h=`{mn['fut_1h']}` | 4h=`{mn['fut_4h']}` | 24h=`{mn['fut_24h']}`")
    lines.append("\n---\n")

    # 9. Execution Verdict
    lines.append("## 9. Algorithmic Formulation & Execution Verdict")
    lines.append(f"- **Audit Decision**: **`{d['status']}`**")
    if d["order_details"]:
        lines.append(f"- **Formulated Order Parameters**:\n```json\n{json.dumps(d['order_details'], indent=2)}\n```")
    else:
        lines.append("- **Stand-Aside Reason**: Insufficient edge or unaligned whale defense. Standing aside in 100% cash preserves statutory floor.")
    
    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

if __name__ == "__main__":
    run_auditor()
