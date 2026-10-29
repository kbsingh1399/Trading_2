import os, glob, json, time
import pandas as pd
import numpy as np

FEEDS_DIR = r"C:\Users\SIGMA\Documents\Trading_2\Data\feeds"

print("--- EXHAUSTIVE 43-FILE / 760-COLUMN AUDIT SCRIPT ---")

# Step 1: Inventory all files and count schema columns
files = sorted(glob.glob(os.path.join(FEEDS_DIR, "*.parquet")))
print(f"Total Parquet files located: {len(files)}")

file_catalog = {}
total_cols_sum = 0
for f in files:
    name = os.path.basename(f)
    try:
        df = pd.read_parquet(f)
        cols = list(df.columns)
        total_cols_sum += len(cols)
        file_catalog[name] = {
            "rows": len(df),
            "cols_count": len(cols),
            "cols": cols
        }
    except Exception as e:
        file_catalog[name] = {"error": str(e), "rows": 0, "cols_count": 0, "cols": []}

print(f"Total Schema Columns across all 43 files: {total_cols_sum}")

# Step 2: Load 00_MT5_Account_Telemetry to get all 156 assets
telemetry_df = pd.read_parquet(os.path.join(FEEDS_DIR, "00_MT5_Account_Telemetry.parquet"))
# filter for assets with Broker_Symbol and valid Spread_BPS
assets_df = telemetry_df[~telemetry_df["Broker_Symbol"].str.contains("Balance|Equity|Free Margin|Hard Floor|Operating Buffer|Capacity", case=False, na=False)].copy()
print(f"Total assets in 00_MT5_Account_Telemetry: {len(assets_df)}")

# Load Technical, Auction, OI, Funding, Whale, CVD, Max Pain, Netflow
tech_df = pd.read_parquet(os.path.join(FEEDS_DIR, "11_Technical.parquet"))
auction_df = pd.read_parquet(os.path.join(FEEDS_DIR, "20_Auction_Market_Structure.parquet"))
cvd_15m = pd.read_parquet(os.path.join(FEEDS_DIR, "18_CVD_30D_15m.parquet"))
cvd_1h = pd.read_parquet(os.path.join(FEEDS_DIR, "18_CVD_30D_1h.parquet"))
whales_df = pd.read_parquet(os.path.join(FEEDS_DIR, "10_Whale_Orders.parquet"))
maxpain_df = pd.read_parquet(os.path.join(FEEDS_DIR, "9_Liquidation_Max_Pain_24H.parquet"))
funding_df = pd.read_parquet(os.path.join(FEEDS_DIR, "5_Funding_Rate.parquet"))
spot_net_df = pd.read_parquet(os.path.join(FEEDS_DIR, "2_Spot_Netflow_S.parquet"))
fut_net_df = pd.read_parquet(os.path.join(FEEDS_DIR, "2_Future_Netflow.parquet"))

# Clean and normalize assets list
asset_inquest = []
passed_gate1 = []
disqualified = []

for idx, r in assets_df.iterrows():
    sym = str(r["Broker_Symbol"]).strip()
    cat = str(r["Category"]).strip()
    bid = float(r["Bid_Quote"]) if pd.notnull(r["Bid_Quote"]) else 0.0
    ask = float(r["Ask_Quote"]) if pd.notnull(r["Ask_Quote"]) else 0.0
    mid = float(r["Mid_Price"]) if pd.notnull(r["Mid_Price"]) else 0.0
    spread_pts = float(r["Spread_Points"]) if pd.notnull(r["Spread_Points"]) else 0.0
    spread_bps = float(r["Spread_BPS"]) if pd.notnull(r["Spread_BPS"]) else 999.0
    thresh_bps = float(r["Threshold_BPS"]) if pd.notnull(r["Threshold_BPS"]) else (12.0 if "Crypto" in cat else 5.0)
    gate_status = str(r["Gate_Status"]).strip()
    
    # Strip suffixes (.p, .pi) to match across feeds
    base = sym.replace(".p", "").replace(".pi", "")
    
    # Check technical
    tech_match = tech_df[tech_df["symbol"].astype(str).str.contains(base, case=False, na=False)]
    if len(tech_match) == 0:
        tech_match = tech_df[tech_df["asset"].astype(str).str.contains(base, case=False, na=False)]
    
    vwap_z = float(tech_match["vwap_z"].iloc[-1]) if len(tech_match) > 0 and pd.notnull(tech_match["vwap_z"].iloc[-1]) else 0.0
    rsi = float(tech_match["rsi_14"].iloc[-1]) if len(tech_match) > 0 and pd.notnull(tech_match["rsi_14"].iloc[-1]) else 50.0
    atr = float(tech_match["atr_14"].iloc[-1]) if len(tech_match) > 0 and pd.notnull(tech_match["atr_14"].iloc[-1]) else 0.0
    trend = str(tech_match["trend_bias"].iloc[-1]) if len(tech_match) > 0 and pd.notnull(tech_match["trend_bias"].iloc[-1]) else "NEUTRAL"
    
    # Check auction
    auc_match = auction_df[auction_df["symbol"].astype(str).str.contains(base, case=False, na=False)]
    if len(auc_match) == 0:
        auc_match = auction_df[auction_df["asset"].astype(str).str.contains(base, case=False, na=False)]
        
    va_pos = str(auc_match["va_position"].iloc[-1]) if len(auc_match) > 0 else "UNKNOWN"
    vah = float(auc_match["daily_vah"].iloc[-1]) if len(auc_match) > 0 and pd.notnull(auc_match["daily_vah"].iloc[-1]) else 0.0
    val = float(auc_match["daily_val"].iloc[-1]) if len(auc_match) > 0 and pd.notnull(auc_match["daily_val"].iloc[-1]) else 0.0
    poc = float(auc_match["daily_poc"].iloc[-1]) if len(auc_match) > 0 and pd.notnull(auc_match["daily_poc"].iloc[-1]) else 0.0
    fib_dir = str(auc_match["fib_dir"].iloc[-1]) if len(auc_match) > 0 and "fib_dir" in auc_match.columns else "NONE"
    fib_status = str(auc_match["fib_status"].iloc[-1]) if len(auc_match) > 0 and "fib_status" in auc_match.columns else "NONE"
    fib_ote = float(auc_match["fib_ote"].iloc[-1]) if len(auc_match) > 0 and "fib_ote" in auc_match.columns and pd.notnull(auc_match["fib_ote"].iloc[-1]) else 0.0
    
    # Check CVD
    cvd_match_15m = cvd_15m[cvd_15m["symbol"].astype(str).str.contains(base, case=False, na=False)]
    cvd_z_15m = float(cvd_match_15m["cvd_zscore"].iloc[-1]) if len(cvd_match_15m) > 0 and pd.notnull(cvd_match_15m["cvd_zscore"].iloc[-1]) else 0.0
    cvd_d_15m = float(cvd_match_15m["delta_pct"].iloc[-1]) if len(cvd_match_15m) > 0 and pd.notnull(cvd_match_15m["delta_pct"].iloc[-1]) else 0.0

    # Gate 1 classification
    is_pass = (spread_bps <= thresh_bps)
    
    item = {
        "sr_no": len(asset_inquest) + 1,
        "symbol": sym,
        "category": cat,
        "bid": bid,
        "ask": ask,
        "mid": mid,
        "spread_pts": spread_pts,
        "spread_bps": spread_bps,
        "threshold_bps": thresh_bps,
        "gate1_pass": is_pass,
        "vwap_z": vwap_z,
        "rsi_14": rsi,
        "atr_14": atr,
        "trend_bias": trend,
        "va_position": va_pos,
        "vah": vah,
        "val": val,
        "poc": poc,
        "fib_status": fib_status,
        "fib_ote": fib_ote,
        "cvd_z_15m": cvd_z_15m,
        "cvd_delta_pct_15m": cvd_d_15m
    }
    asset_inquest.append(item)
    if is_pass:
        passed_gate1.append(item)
    else:
        disqualified.append(item)

print(f"Total assets processed: {len(asset_inquest)}")
print(f"Passed Gate 1: {len(passed_gate1)} | Disqualified: {len(disqualified)}")

# Output summary to JSON
out_path = r"C:\Users\SIGMA\Documents\Trading_2\Data\sovereign_760_param_audit_summary.json"
with open(out_path, "w", encoding="utf-8") as f:
    json.dump({
        "timestamp_ist": time.strftime("%Y-%m-%d %H:%M:%S IST"),
        "total_files": len(files),
        "total_schema_columns": total_cols_sum,
        "total_assets": len(asset_inquest),
        "passed_gate1_count": len(passed_gate1),
        "disqualified_count": len(disqualified),
        "passed_sample": passed_gate1[:15],
        "disqualified_sample": disqualified[:15]
    }, f, indent=2)

print(f"Successfully saved {out_path}")
