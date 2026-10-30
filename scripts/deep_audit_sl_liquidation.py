import os
import json
import pandas as pd
import numpy as np
from datetime import datetime, timezone

def inspect_parquet_feeds():
    feeds_dir = "Data/feeds"
    checklist_path = "Data/metadata/parquet_all_feeds_checklist.json"
    if not os.path.exists(checklist_path):
        checklist_path = "Data/parquet_all_feeds_checklist.json"
    
    with open(checklist_path, 'r', encoding='utf-8') as f:
        checklist = json.load(f)
    
    print("--- PARQUET FRESHNESS AUDIT ---")
    rows = []
    # If checklist is dict or list
    items = checklist if isinstance(checklist, list) else checklist.get("feeds", checklist.get("checklist", []))
    if isinstance(checklist, dict) and not items:
        # maybe dict of feeds
        items = [{"name": k, **v} if isinstance(v, dict) else {"name": k} for k, v in checklist.items()]
        
    now = datetime.now()
    for item in items[:43]:
        name = item.get("feed_name", item.get("name", "Unknown"))
        file_name = item.get("file_name", name if name.endswith(".parquet") else f"{name}.parquet")
        fpath = os.path.join(feeds_dir, file_name)
        if os.path.exists(fpath):
            mtime = datetime.fromtimestamp(os.path.getmtime(fpath))
            age_min = (now - mtime).total_seconds() / 60.0
            size_kb = os.path.getsize(fpath) / 1024.0
            status = "PASS" if age_min < 5.0 else ("WARN" if age_min < 15.0 else "FAIL")
            rows.append({
                "feed": file_name,
                "tier": item.get("tier", "Standard"),
                "age_min": round(age_min, 1),
                "mtime": mtime.strftime("%Y-%m-%d %H:%M:%S"),
                "status": status
            })
    
    print(f"Total checked: {len(rows)}")
    for r in rows[:10]:
        print(r)

def inspect_sl_liquidation_defense():
    print("\n--- DEEP LIQUIDATION & SL ZONE AUDIT ---")
    
    # 1. 14_Liquidation_Matrix.parquet
    f_liq = "Data/feeds/14_Liquidation_Matrix.parquet"
    if os.path.exists(f_liq):
        df_liq = pd.read_parquet(f_liq)
        print(f"\n14_Liquidation_Matrix columns: {list(df_liq.columns)[:10]}, shape: {df_liq.shape}")
        # Look for BTC, BNB, etc.
        for sym in ['BTC', 'BTCUSDT', 'BNB', 'BNBUSDT', 'ETH']:
            sub = df_liq[df_liq.astype(str).apply(lambda row: row.str.contains(sym, case=False).any(), axis=1)]
            if len(sub) > 0:
                print(f"Liq Matrix match for {sym}: {len(sub)} rows")
                print(sub.head(2))
    
    # 2. 15_Hyperdash_Stops_Map.parquet
    f_stops = "Data/feeds/15_Hyperdash_Stops_Map.parquet"
    if os.path.exists(f_stops):
        df_stops = pd.read_parquet(f_stops)
        print(f"\n15_Hyperdash_Stops_Map columns: {list(df_stops.columns)}, shape: {df_stops.shape}")
        print("Sample stops map head:")
        print(df_stops.head(5))
        
    # 3. 10_Whale_Orders.parquet
    f_whale = "Data/feeds/10_Whale_Orders.parquet"
    if os.path.exists(f_whale):
        df_whale = pd.read_parquet(f_whale)
        print(f"\n10_Whale_Orders columns: {list(df_whale.columns)}, shape: {df_whale.shape}")
        for sym in ['BTC', 'BNB']:
            sub_w = df_whale[df_whale.astype(str).apply(lambda row: row.str.contains(sym, case=False).any(), axis=1)]
            if len(sub_w) > 0:
                print(f"Whale orders for {sym}: {len(sub_w)} rows")
                print(sub_w.head(3))
                
    # 4. 20_Auction_Market_Structure.parquet
    f_auc = "Data/feeds/20_Auction_Market_Structure.parquet"
    if os.path.exists(f_auc):
        df_auc = pd.read_parquet(f_auc)
        print(f"\n20_Auction_Market_Structure columns: {list(df_auc.columns)}, shape: {df_auc.shape}")
        print(df_auc.head(5))

    # 5. 00_MT5_Account_Telemetry.parquet
    f_telemetry = "Data/feeds/00_MT5_Account_Telemetry.parquet"
    if os.path.exists(f_telemetry):
        df_tel = pd.read_parquet(f_telemetry)
        print(f"\n00_MT5_Account_Telemetry columns: {list(df_tel.columns)}, shape: {df_tel.shape}")
        for sym in ['BTCUSD.pi', 'BNBUSD.p', 'XAUUSD.pi', 'NAS100.p', 'DJ30.p', 'AUDUSD.pi']:
            sub_t = df_tel[df_tel.astype(str).apply(lambda row: row.str.contains(sym, case=False).any(), axis=1)]
            if len(sub_t) > 0:
                print(f"Telemetry for {sym}:")
                print(sub_t[['symbol', 'bid', 'ask', 'spread', 'spread_bps', 'atr_14'] if 'atr_14' in sub_t.columns else sub_t.columns[:6]])

if __name__ == "__main__":
    inspect_parquet_feeds()
    inspect_sl_liquidation_defense()
