import pathlib
import json
import pandas as pd
import datetime

ROOT = pathlib.Path(r"C:\Users\SIGMA\Documents\Trading_2")
FEEDS_DIR = ROOT / "Data" / "feeds"

FILES = [
    "00_MT5_Account_Telemetry.parquet",
    "1_Crypto_ETF_Flows.parquet",
    "2_Spot_Netflow_S.parquet",
    "2_Future_Netflow.parquet",
    "3_Exchanges_LS_Ratio_15M.parquet",
    "3_Exchanges_LS_Ratio_1H.parquet",
    "3_Exchanges_LS_Ratio_4H.parquet",
    "4_Hyperliquid_Analysis.parquet",
    "5_Funding_Rate.parquet",
    "5_OI.parquet",
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
    "19_News.parquet",
    "19_Calendar.parquet",
    "20_Auction_Market_Structure.parquet",
    "21_Tradfye_Orderflow.parquet",
    "22_Forced_Liquidations_MTF.parquet",
    "23_Master_Pipeline_Telemetry.parquet",
    "25_CoinGlass_Footprint_Signals.parquet",
    "26_Aggregated_Footprint_Bar_Metrics.parquet"
]

def analyze_all():
    summary = []
    print(f"Analyzing all {len(FILES)} Parquet files...")
    
    for idx, fname in enumerate(FILES):
        fpath = FEEDS_DIR / fname
        if not fpath.exists():
            summary.append({
                "idx": idx,
                "file": fname,
                "status": "MISSING",
                "rows": 0,
                "cols": [],
                "insight": "File not found on disk"
            })
            continue
            
        try:
            df = pd.read_parquet(fpath)
            cols = list(df.columns)
            rows = len(df)
            
            # Find timestamp col
            ts_val = "N/A"
            for c in cols:
                if "time" in c.lower() or "date" in c.lower():
                    ts_val = str(df[c].iloc[-1])
                    break
                    
            # Extract key insight based on file type
            insight = ""
            if "00_MT5" in fname:
                bal = df[df["Broker_Symbol"] == "Realized Balance (USD)"]["Gate_Status"].values
                insight = f"Account Balance: {bal[0] if len(bal) > 0 else 'N/A'}"
            elif "1_Crypto_ETF" in fname:
                ibit = df[df["Ticker"].astype(str).str.contains("IBIT")] if "Ticker" in df.columns else df.head(1)
                insight = f"IBIT Flow: {ibit['NetInflow_USD'].iloc[-1] if 'NetInflow_USD' in ibit.columns else 'Recorded'}"
            elif "2_Spot_Netflow" in fname or "2_Future_Netflow" in fname:
                val = df['1h_netflow'].iloc[-1] if '1h_netflow' in df.columns else (df['netflow_usd'].iloc[-1] if 'netflow_usd' in df.columns else 'Active')
                insight = f"Netflow 1h: {val}"
            elif "5_Funding" in fname:
                btc = df[df["Symbol"] == "BTC"] if "Symbol" in df.columns else df.head(1)
                insight = f"BTC Binance Funding: {btc['USDT_Binance'].iloc[-1] if 'USDT_Binance' in btc.columns else 'Active'}"
            elif "5_OI" in fname:
                btc = df[df["Asset"] == "BTC"] if "Asset" in df.columns else df.head(1)
                insight = f"Total BTC OI: {btc['Total_OI_USD'].iloc[-1] if 'Total_OI_USD' in btc.columns else 'Active'}"
            elif "10_Whale" in fname:
                top_w = df.sort_values(by="notional_usd", ascending=False).iloc[0] if "notional_usd" in df.columns and len(df) > 0 else None
                insight = f"Top Whale: {top_w['symbol']} {top_w['side']} ${top_w['notional_usd']:,.0f} @ {top_w['price']}" if top_w is not None else "Active"
            elif "9_Liquidation_Max_Pain" in fname:
                btc = df[df["symbol"] == "BTC"] if "symbol" in df.columns else df.head(1)
                insight = f"BTC Short Max Pain: {btc['short_max_pain_price'].iloc[-1]}, Long Max Pain: {btc['long_max_pain_price'].iloc[-1]}" if len(btc) > 0 else "Active"
            elif "20_Auction" in fname:
                insight = f"Total auction value structures tracked: {len(df)} assets"
            elif "18_CVD" in fname:
                insight = f"CVD series tracked across {len(df)} bars/assets"
            else:
                insight = f"{rows} records across {len(cols)} columns"

            summary.append({
                "idx": idx,
                "file": fname,
                "status": "PASS",
                "rows": rows,
                "cols_count": len(cols),
                "cols": cols[:6],
                "timestamp": ts_val,
                "insight": insight
            })
        except Exception as e:
            summary.append({
                "idx": idx,
                "file": fname,
                "status": f"ERROR: {e}",
                "rows": 0,
                "cols": [],
                "insight": str(e)
            })

    out_file = ROOT / "Data" / "all_43_parquet_deep_analysis.json"
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(summary, f, indent=2)
    print(f"Successfully analyzed all {len(summary)} files. Saved to {out_file}")

if __name__ == "__main__":
    analyze_all()
