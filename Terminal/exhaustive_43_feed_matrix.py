"""
Terminal/exhaustive_43_feed_matrix.py
Forensically loads and extracts empirical data across ALL 43 Parquet Feeds for passed candidates.
"""

import json
import pathlib
import datetime
import pandas as pd
import numpy as np

ROOT = pathlib.Path(__file__).resolve().parents[1]
FEEDS_DIR = ROOT / "Data" / "feeds"

PARQUET_FILES = [
    "00_MT5_Account_Telemetry.parquet",
    "1_Crypto_ETF_Flows.parquet",
    "2_Spot_Netflow_S.parquet",
    "2_Future_Netflow.parquet",
    "3_Exchanges_LS_Ratio_15M.parquet",
    "3_Exchanges_LS_Ratio_1H.parquet",
    "3_Exchanges_LS_Ratio_4H.parquet",
    "4_Hyperliquid_Analysis.parquet",
    "5_OI.parquet",
    "5_Funding_Rate.parquet",
    "6_Funding_Fee_Settlement.parquet",
    "7_Liq_Heapmap.parquet",
    "7_Live_Liq.parquet",
    "8_Exchange_Liquidation_Map_1D.parquet",
    "8_Exchange_Liquidation_Map_7D.parquet",
    "9_Liquidation_Max_Pain_24H.parquet",
    "9_Liquidation_Max_Pain_48H.parquet",
    "9_Liquidation_Max_Pain_3D.parquet",
    "9_Liquidation_Max_Pain_7D.parquet",
    "10_Whale_Orders.parquet",
    "11_Technical.parquet",
    "11_Technical_BTC_Ribbon.parquet",
    "12_Hyperdash.parquet",
    "13_Hyperliquid.parquet",
    "14_Hyperdash_Liq_Map.parquet",
    "14_Liquidation_Matrix.parquet",
    "15_Hyperdash_Stops_Map.parquet",
    "16_Hyperdash_telegram_Intel.parquet",
    "17_Orderbook.parquet",
    "18_CVD.parquet",
    "18_CVD_30D_5m.parquet",
    "18_CVD_30D_15m.parquet",
    "18_CVD_30D_1h.parquet",
    "18_CVD_30D_4h.parquet",
    "18_CVD_30D_ALL.parquet",
    "19_Calendar.parquet",
    "19_News.parquet",
    "20_Auction_Market_Structure.parquet",
    "21_Tradfye_Orderflow.parquet",
    "22_Forced_Liquidations_MTF.parquet",
    "23_Master_Pipeline_Telemetry.parquet",
    "25_CoinGlass_Footprint_Signals.parquet",
    "26_Aggregated_Footprint_Bar_Metrics.parquet"
]

def audit_all_43_feeds():
    print(f"=== AUDITING ALL {len(PARQUET_FILES)} PARQUET FEEDS ===")
    feed_summary = []
    feed_dfs = {}
    
    for f in PARQUET_FILES:
        p = FEEDS_DIR / f
        if p.exists():
            try:
                df = pd.read_parquet(p)
                feed_dfs[f] = df
                cols = list(df.columns)
                feed_summary.append({
                    "feed": f,
                    "rows": len(df),
                    "cols": len(cols),
                    "columns_sample": cols[:5]
                })
            except Exception as e:
                feed_summary.append({
                    "feed": f,
                    "rows": 0,
                    "error": str(e)
                })
        else:
            feed_summary.append({
                "feed": f,
                "rows": 0,
                "error": "FILE_NOT_FOUND"
            })

    print(f"Loaded {len(feed_dfs)} / {len(PARQUET_FILES)} dataframes successfully.")
    
    # Check candidates
    df_telem = feed_dfs.get("00_MT5_Account_Telemetry.parquet", pd.DataFrame())
    candidates = ["AUDUSD.pi", "USDJPY.pi", "US2000.p", "XAUUSD.pi", "EURUSD.pi", "SP500.p", "BNBUSD.p", "BTCUSD.pi"]
    
    candidate_forensics = {}
    for c in candidates:
        candidate_forensics[c] = {}
        c_clean = c.split(".")[0].replace("USD", "").replace(".pi", "").replace(".p", "")
        
        # Check presence in feeds
        matched_feeds = []
        for feed_name, df in feed_dfs.items():
            sym_col = None
            for col in df.columns:
                if col.lower() in ["symbol", "broker_symbol", "coin", "ticker", "asset"]:
                    sym_col = col
                    break
            
            if sym_col:
                # search symbol
                try:
                    match = df[df[sym_col].astype(str).str.contains(c_clean, case=False, na=False)]
                    if not match.empty:
                        matched_feeds.append((feed_name, len(match)))
                except Exception:
                    pass
            else:
                # Macro/global feed (e.g. ETF flows, News, Calendar, Master telemetry)
                matched_feeds.append((feed_name, "GLOBAL_MACRO"))
                
        candidate_forensics[c]["matched_feed_count"] = len(matched_feeds)
        candidate_forensics[c]["matched_feeds"] = matched_feeds[:8]

    # Save forensic matrix
    matrix_file = ROOT / "Data" / "metadata" / "exhaustive_43_feed_matrix.json"
    matrix_file.parent.mkdir(parents=True, exist_ok=True)
    with open(matrix_file, "w", encoding="utf-8") as f:
        json.dump({
            "timestamp_utc": datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC"),
            "total_feeds": len(PARQUET_FILES),
            "loaded_feeds": len(feed_dfs),
            "feed_summary": feed_summary,
            "candidate_forensics": candidate_forensics
        }, f, indent=2)

    print(f"Audit completed! Saved to {matrix_file}")
    return feed_summary, candidate_forensics

if __name__ == "__main__":
    audit_all_43_feeds()
