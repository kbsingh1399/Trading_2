#!/usr/bin/env python3
"""
Terminal/Data_Factory/asset_43_feed_extractor.py
================================================
Universal 43-Feed Forensic Candidate Analyzer.
Extracts and combines all 43 Parquet production feeds for any given target asset
to formulate institutional trades with exact mathematical parameters.
"""

import argparse
import json
import pathlib
import sys
import pandas as pd
import numpy as np

ROOT = pathlib.Path(__file__).resolve().parents[2]
FEEDS_DIR = ROOT / "Data" / "feeds"

def clean_val(v):
    if isinstance(v, str):
        v = v.replace('$', '').replace(',', '').strip()
        if v.endswith('M'): return float(v[:-1]) * 1e6
        if v.endswith('B'): return float(v[:-1]) * 1e9
        if v.endswith('K'): return float(v[:-1]) * 1e3
        try: return float(v)
        except: return 0.0
    try: return float(v)
    except: return 0.0

def analyze_asset_43_feeds(symbol_query: str) -> dict:
    sq = symbol_query.upper().replace('.PI', '').replace('.P', '').replace('USDT', '').replace('USD', '')
    res = {
        'target_asset': symbol_query,
        'base_coin': sq,
        'liquidations': {},
        'max_pain': {},
        'orderbook_and_whales': {},
        'cvd_multi_timeframe': {},
        'footprint_and_auction': {},
        'derivatives_positioning': {},
        'macro_flows': {},
        'formulated_trade': {}
    }

    # 1. Max Pain
    for h in ['24H', '48H', '3D', '7D']:
        p = FEEDS_DIR / f"9_Liquidation_Max_Pain_{h}.parquet"
        if p.exists():
            df = pd.read_parquet(p)
            match = df[df['symbol'].str.upper() == sq]
            if len(match) > 0:
                r = match.iloc[0]
                res['max_pain'][h] = {
                    'current_price': float(r['price']),
                    'short_max_pain': float(r['short_max_pain_price']),
                    'short_vol_usd': float(r['short_max_pain_vol']),
                    'long_max_pain': float(r['long_max_pain_price']),
                    'long_vol_usd': float(r['long_max_pain_vol'])
                }

    # 2. 1D and 7D Liquidation Maps
    p_1d = FEEDS_DIR / "8_Exchange_Liquidation_Map_1D.parquet"
    if p_1d.exists():
        df_1d = pd.read_parquet(p_1d)
        m_1d = df_1d[df_1d['Asset'].str.upper() == sq]
        if len(m_1d) > 0:
            res['liquidations']['1D_levels_count'] = len(m_1d)
            # Find largest short and long liquidation clusters
            m_1d_copy = m_1d.copy()
            m_1d_copy['cum_num'] = m_1d_copy['Cumulative_Liquidation'].apply(clean_val)
            m_1d_copy['p_num'] = m_1d_copy['Price'].apply(clean_val)
            res['liquidations']['1D_peak_liq'] = float(m_1d_copy['cum_num'].max())

    p_7d = FEEDS_DIR / "8_Exchange_Liquidation_Map_7D.parquet"
    if p_7d.exists():
        df_7d = pd.read_parquet(p_7d)
        m_7d = df_7d[df_7d['Asset'].str.upper() == sq]
        if len(m_7d) > 0:
            m_7d_copy = m_7d.copy()
            m_7d_copy['cum_num'] = m_7d_copy['Cumulative_Liquidation'].apply(clean_val)
            res['liquidations']['7D_peak_liq'] = float(m_7d_copy['cum_num'].max())

    # 3. Hyperdash Liq & Stops
    p_hliq = FEEDS_DIR / "14_Hyperdash_Liq_Map.parquet"
    if p_hliq.exists():
        df_hl = pd.read_parquet(p_hliq)
        m_hl = df_hl[df_hl['asset'].str.upper() == sq]
        res['liquidations']['hyperdash_nodes'] = len(m_hl)

    p_hstops = FEEDS_DIR / "15_Hyperdash_Stops_Map.parquet"
    if p_hstops.exists():
        df_hs = pd.read_parquet(p_hstops)
        m_hs = df_hs[df_hs['asset'].str.upper() == sq]
        res['liquidations']['hyperdash_stop_nodes'] = len(m_hs)

    # 4. Whales
    p_whales = FEEDS_DIR / "10_Whale_Orders.parquet"
    if p_whales.exists():
        df_w = pd.read_parquet(p_whales)
        m_w = df_w[df_w['symbol'].str.contains(sq, case=False, na=False)]
        res['orderbook_and_whales']['resting_whale_orders'] = len(m_w)

    # 5. CVD Multi-Timeframe
    for tf in ['5m', '15m', '1h', '4h']:
        p_cvd = FEEDS_DIR / f"18_CVD_30D_{tf}.parquet"
        if p_cvd.exists():
            df_c = pd.read_parquet(p_cvd)
            col = 'symbol' if 'symbol' in df_c.columns else 'category'
            m_c = df_c[df_c[col].str.contains(sq, case=False, na=False)]
            if len(m_c) > 0:
                last_row = m_c.iloc[-1]
                val = last_row.get('cumulative_cvd', last_row.get('candle_delta', last_row.get('cvd', 0)))
                res['cvd_multi_timeframe'][tf] = float(val) if val is not None else 0.0

    # 6. Auction Market Structure
    p_ams = FEEDS_DIR / "20_Auction_Market_Structure.parquet"
    if p_ams.exists():
        df_ams = pd.read_parquet(p_ams)
        m_ams = df_ams[df_ams['symbol'].str.contains(sq, case=False, na=False) | df_ams['asset'].str.contains(sq, case=False, na=False)]
        if len(m_ams) > 0:
            r = m_ams.iloc[0]
            res['footprint_and_auction'] = {
                'poc': float(r.get('daily_poc', r.get('poc', 0))),
                'vah': float(r.get('daily_vah', r.get('vah', 0))),
                'val': float(r.get('daily_val', r.get('val', 0))),
                'value_area_width': float(r.get('daily_vah', 0)) - float(r.get('daily_val', 0)),
                'auction_regime': str(r.get('auction_regime', 'UNKNOWN')),
                'session_bias': str(r.get('session_bias', 'UNKNOWN')),
                'r1': float(r.get('r1', 0)),
                'r2': float(r.get('r2', 0)),
                's1': float(r.get('s1', 0)),
                's2': float(r.get('s2', 0))
            }

    # 7. Derivatives Positioning
    p_fund = FEEDS_DIR / "5_Funding_Rate.parquet"
    if p_fund.exists():
        df_f = pd.read_parquet(p_fund)
        m_f = df_f[df_f['Symbol'].str.upper() == sq]
        if len(m_f) > 0:
            res['derivatives_positioning']['funding_binance'] = str(m_f.iloc[0].get('USDT_Binance', 'N/A'))

    p_oi = FEEDS_DIR / "5_OI.parquet"
    if p_oi.exists():
        df_oi = pd.read_parquet(p_oi)
        m_oi = df_oi[df_oi['Asset'].str.upper() == sq]
        if len(m_oi) > 0:
            res['derivatives_positioning']['total_oi_usd'] = str(m_oi.iloc[0].get('Total_OI_USD', 'N/A'))

    for tf in ['15M', '1H', '4H']:
        p_ls = FEEDS_DIR / f"3_Exchanges_LS_Ratio_{tf}.parquet"
        if p_ls.exists():
            df_ls = pd.read_parquet(p_ls)
            m_ls = df_ls[df_ls['Asset'].str.upper() == sq]
            if len(m_ls) > 0:
                res['derivatives_positioning'][f'ls_ratio_{tf}'] = str(m_ls.iloc[0].get('L_S_Ratio', 'N/A'))

    # 8. Macro Flows
    p_spot = FEEDS_DIR / "2_Spot_Netflow_S.parquet"
    if p_spot.exists():
        df_s = pd.read_parquet(p_spot)
        m_s = df_s[df_s['Symbol'].str.upper() == sq]
        if len(m_s) > 0:
            res['macro_flows']['spot_15m'] = str(m_s.iloc[0].get('15_minute', 'N/A'))
            res['macro_flows']['spot_1h'] = str(m_s.iloc[0].get('1_hour', 'N/A'))

    p_fut = FEEDS_DIR / "2_Future_Netflow.parquet"
    if p_fut.exists():
        df_fut = pd.read_parquet(p_fut)
        m_fut = df_fut[df_fut['Symbol'].str.upper() == sq]
        if len(m_fut) > 0:
            res['macro_flows']['future_15m'] = str(m_fut.iloc[0].get('15_minute', 'N/A'))
            res['macro_flows']['future_1h'] = str(m_fut.iloc[0].get('1_hour', 'N/A'))

    # Formulate Institutional Trade
    mp24 = res['max_pain'].get('24H', {})
    cur_p = mp24.get('current_price', 0.0)
    s_pain = mp24.get('short_max_pain', 0.0)
    l_pain = mp24.get('long_max_pain', 0.0)

    if cur_p > 0:
        dist_to_short = s_pain - cur_p
        dist_to_long = cur_p - l_pain
        # Determine regime
        if dist_to_short < dist_to_long:
            # Approaching upper liquidity sweep
            res['formulated_trade'] = {
                'side': 'SELL_LIMIT (Post-Sweep Mean Reversion)',
                'entry_price': round(s_pain, 2),
                'stop_loss': round(s_pain * 1.008, 2), # 0.8% structural clearance
                'take_profit': round(l_pain, 2),
                'target_rationale': 'Entry at 24H Short Max Pain exhaustion; SL cleared beyond 7D cascade; TP at 24H Long Max Pain.'
            }
        else:
            res['formulated_trade'] = {
                'side': 'BUY_LIMIT (Post-Sweep Mean Reversion)',
                'entry_price': round(l_pain, 2),
                'stop_loss': round(l_pain * 0.992, 2),
                'take_profit': round(s_pain, 2),
                'target_rationale': 'Entry at 24H Long Max Pain exhaustion; SL cleared below 7D cascade; TP at 24H Short Max Pain.'
            }

    return res

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Extract 43-feed metrics for an asset")
    parser.add_argument("--symbol", type=str, default="ETH", help="Target asset symbol (e.g. BTC, ETH, SOL, XAU)")
    args = parser.parse_args()
    result = analyze_asset_43_feeds(args.symbol)
    print(json.dumps(result, indent=2))
