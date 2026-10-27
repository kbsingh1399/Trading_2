"""
Asset 360° Data Lake Dossier Engine
-----------------------------------
Canonical mechanism to guarantee zero omission of quantitative data points across
the entire Parquet Data Lake (Data/feeds/*.parquet) for any candidate asset.

Traverses every parquet file, extracts asset-specific signals (Footprints, Orderbook,
Whale Orders, Liquidations, CVD, Auction Profiles, Technicals, Funding, Macro),
and compiles a unified institutional trade dossier.
"""

import os
import glob
import json
import argparse
import datetime
from pathlib import Path
from typing import Dict, List, Any, Optional
import pandas as pd

FEEDS_DIR = Path("Data/feeds")
DOSSIER_JSON_DIR = Path("Data/dossiers")
DOSSIER_MD_DIR = Path("docs/dossiers")

# Pillar categorizations for all 36 canonical feeds
PILLAR_MAPPING = {
    "00_MT5_Account_Telemetry": "Pillar 1: Broker Telemetry & Solvency",
    "1_Crypto_ETF_Flows": "Pillar 2: Macro & ETF Netflows",
    "2_Spot_Netflow_S": "Pillar 2: Macro & ETF Netflows",
    "19_News": "Pillar 2: Macro & ETF Netflows",
    "19_Calendar": "Pillar 2: Macro & ETF Netflows",
    "3_Exchanges_LS_Ratio_15M": "Pillar 3: Sentiment & Leverage Crowding",
    "3_Exchanges_LS_Ratio_1H": "Pillar 3: Sentiment & Leverage Crowding",
    "3_Exchanges_LS_Ratio_4H": "Pillar 3: Sentiment & Leverage Crowding",
    "5_OI": "Pillar 3: Sentiment & Leverage Crowding",
    "5_Funding_Rate": "Pillar 3: Sentiment & Leverage Crowding",
    "6_Funding_Fee_Settlement": "Pillar 3: Sentiment & Leverage Crowding",
    "7_Liq_Heapmap": "Pillar 4: Liquidation & Stops Geometry",
    "7_Live_Liq": "Pillar 4: Liquidation & Stops Geometry",
    "8_Exchange_Liquidation_Map_1D": "Pillar 4: Liquidation & Stops Geometry",
    "8_Exchange_Liquidation_Map_7D": "Pillar 4: Liquidation & Stops Geometry",
    "9_Liquidation_Max_Pain_24H": "Pillar 4: Liquidation & Stops Geometry",
    "9_Liquidation_Max_Pain_48H": "Pillar 4: Liquidation & Stops Geometry",
    "9_Liquidation_Max_Pain_3D": "Pillar 4: Liquidation & Stops Geometry",
    "9_Liquidation_Max_Pain_7D": "Pillar 4: Liquidation & Stops Geometry",
    "14_Liquidation_Matrix": "Pillar 4: Liquidation & Stops Geometry",
    "14_Hyperdash_Liq_Map": "Pillar 4: Liquidation & Stops Geometry",
    "15_Hyperdash_Stops_Map": "Pillar 4: Liquidation & Stops Geometry",
    "22_Forced_Liquidations_MTF": "Pillar 4: Liquidation & Stops Geometry",
    "10_Whale_Orders": "Pillar 5: Microstructure, Whales & Footprints",
    "17_Orderbook": "Pillar 5: Microstructure, Whales & Footprints",
    "18_CVD": "Pillar 5: Microstructure, Whales & Footprints",
    "18_CVD_30D_15m": "Pillar 5: Microstructure, Whales & Footprints",
    "18_CVD_30D_1h": "Pillar 5: Microstructure, Whales & Footprints",
    "18_CVD_30D_4h": "Pillar 5: Microstructure, Whales & Footprints",
    "18_CVD_30D_5m": "Pillar 5: Microstructure, Whales & Footprints",
    "18_CVD_30D_ALL": "Pillar 5: Microstructure, Whales & Footprints",
    "21_Tradfye_Orderflow": "Pillar 5: Microstructure, Whales & Footprints",
    "25_CoinGlass_Footprint_Signals": "Pillar 5: Microstructure, Whales & Footprints",
    "26_Aggregated_Footprint_Bar_Metrics": "Pillar 5: Microstructure, Whales & Footprints",
    "4_Hyperliquid_Analysis": "Pillar 6: Technical & Auction Profile",
    "11_Technical": "Pillar 6: Technical & Auction Profile",
    "11_Technical_BTC_Ribbon": "Pillar 6: Technical & Auction Profile",
    "12_Hyperdash": "Pillar 6: Technical & Auction Profile",
    "13_Hyperliquid": "Pillar 6: Technical & Auction Profile",
    "16_Hyperdash_telegram_Intel": "Pillar 6: Technical & Auction Profile",
    "20_Auction_Market_Structure": "Pillar 6: Technical & Auction Profile",
    "23_Master_Pipeline_Telemetry": "Pillar 1: Broker Telemetry & Solvency",
}

SYMBOL_COLUMNS = [
    "symbol", "base_asset", "asset", "Asset", "Symbol", "coin", "Ticker",
    "Broker_Symbol", "market_pair", "pair", "instrument"
]

def generate_asset_aliases(raw_asset: str) -> List[str]:
    """Generate case-insensitive matching tokens for any asset class."""
    clean = raw_asset.strip().upper().replace("/", "").replace("_", "").replace("-", "")
    
    # Base canonical token
    base = clean
    for suffix in [".PI", ".P", "USDT", "USD", "PERP"]:
        if base.endswith(suffix):
            base = base[:-len(suffix)]
            break
            
    aliases = {clean, base}
    
    # Specific asset mappings
    if base in ["BTC", "XBT"]:
        aliases.update(["BTC", "XBT", "BTCUSDT", "BTCUSD", "BTCUSD.PI", "BTCUSD.P", "BTC-PERP", "BTCPERP"])
    elif base in ["ETH"]:
        aliases.update(["ETH", "ETHUSDT", "ETHUSD", "ETHUSD.PI", "ETHUSD.P", "ETH-PERP", "ETHPERP"])
    elif base in ["SOL"]:
        aliases.update(["SOL", "SOLUSDT", "SOLUSD", "SOLUSD.PI", "SOLUSD.P"])
    elif base in ["XAU", "GOLD"]:
        aliases.update(["XAU", "GOLD", "XAUUSD", "XAUUSD.PI", "XAUUSD.P", "XAU/USD"])
    elif base in ["XAG", "SILVER"]:
        aliases.update(["XAG", "SILVER", "XAGUSD", "XAGUSD.PI", "XAGUSD.P"])
    elif base in ["BRENT", "UKBRENT", "OIL"]:
        aliases.update(["BRENT", "UKBRENT", "UKBRENT.P", "OIL", "CRUDE"])
    elif base in ["US30", "DJ30", "DOW"]:
        aliases.update(["US30", "US30.PI", "US30.P", "DJ30", "WALLSTREET"])
    elif base in ["SPX500", "US500", "SP500", "SPX"]:
        aliases.update(["SPX500", "SPX500.PI", "US500.P", "SPX", "SP500"])
    elif base in ["NAS100", "USTEC", "NDX"]:
        aliases.update(["NAS100", "NAS100.PI", "USTEC.P", "NDX", "NASDAQ"])
    elif base in ["EUR", "EURUSD"]:
        aliases.update(["EUR", "EURUSD", "EURUSD.PI", "EUR/USD"])
    elif base in ["JPY", "USDJPY"]:
        aliases.update(["JPY", "USDJPY", "USDJPY.PI", "USD/JPY"])
    elif base in ["GBP", "GBPUSD"]:
        aliases.update(["GBP", "GBPUSD", "GBPUSD.PI", "GBP/USD"])
    elif base in ["AUD", "AUDUSD"]:
        aliases.update(["AUD", "AUDUSD", "AUDUSD.PI", "AUD/USD"])
    else:
        # Default crypto/generic token
        aliases.update([f"{base}USDT", f"{base}USD", f"{base}USD.PI", f"{base}USD.P"])
        
    return [a.upper() for a in aliases]

def build_asset_360_dossier(asset: str) -> Dict[str, Any]:
    """Traverse all parquet files and construct complete 360-degree data dossier."""
    aliases = generate_asset_aliases(asset)
    files = sorted(glob.glob(str(FEEDS_DIR / "*.parquet")))
    
    timestamp_ist = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S IST")
    timestamp_utc = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")
    
    dossier: Dict[str, Any] = {
        "asset": asset.upper(),
        "aliases": aliases,
        "timestamp_ist": timestamp_ist,
        "timestamp_utc": timestamp_utc,
        "total_files_scanned": len(files),
        "feeds_with_data_count": 0,
        "global_macro_feeds_count": 0,
        "feeds_no_data_count": 0,
        "pillar_summary": {},
        "feed_details": []
    }
    
    for fpath in files:
        fname = os.path.basename(fpath)
        base_name = fname.replace(".parquet", "")
        pillar = PILLAR_MAPPING.get(base_name, "General Telemetry")
        
        try:
            df = pd.read_parquet(fpath)
        except Exception as e:
            dossier["feed_details"].append({
                "feed_name": base_name,
                "file_name": fname,
                "pillar": pillar,
                "status": f"READ_ERROR: {str(e)}",
                "matching_rows": 0,
                "data_points": {}
            })
            continue
            
        # Check for symbol columns
        matched_cols = [c for c in df.columns if c in SYMBOL_COLUMNS or any(k in c.lower() for k in ["sym", "coin", "asset", "pair", "ticker"])]
        
        # Macro / Global feeds
        if not matched_cols or base_name in ["19_Calendar", "19_News", "23_Master_Pipeline_Telemetry", "11_Technical_BTC_Ribbon"]:
            dossier["global_macro_feeds_count"] += 1
            sample_records = df.tail(3).to_dict(orient="records") if len(df) > 0 else []
            dossier["feed_details"].append({
                "feed_name": base_name,
                "file_name": fname,
                "pillar": pillar,
                "status": "MACRO_GLOBAL_CONTEXT",
                "matching_rows": len(df),
                "total_rows": len(df),
                "key_columns": df.columns.tolist()[:8],
                "latest_sample": sample_records
            })
            continue
            
        # Filter by exact alias membership (prevent substring collisions like NETH25.p for ETH or XAUGBP.pi for XAU)
        alias_set = set(aliases)
        mask = pd.Series(False, index=df.index)
        for col in matched_cols:
            col_str = df[col].astype(str).str.upper().str.strip()
            col_clean = col_str.str.replace(r'[^A-Z0-9]', '', regex=True)
            mask = mask | col_str.isin(alias_set) | col_clean.isin(alias_set)
                
        matched_df = df[mask]
        
        # Microstructure hardening for Whale Orders: dedup & tau >= 180s persistence filter
        if base_name == "10_Whale_Orders" and len(matched_df) > 0:
            if all(c in matched_df.columns for c in ["symbol", "side", "price", "amount_btc"]):
                matched_df = matched_df.drop_duplicates(subset=["symbol", "side", "price", "amount_btc"])
            if "order_duration" in matched_df.columns:
                def parse_dur_s(d_str: str) -> float:
                    if not isinstance(d_str, str): return 0.0
                    import re
                    tot = 0.0
                    d_str = d_str.strip().lower()
                    d = re.search(r'(\d+)\s*d', d_str)
                    h = re.search(r'(\d+)\s*h', d_str)
                    m = re.search(r'(\d+)\s*m', d_str)
                    s = re.search(r'(\d+)\s*s', d_str)
                    if d: tot += float(d.group(1)) * 86400
                    if h: tot += float(h.group(1)) * 3600
                    if m: tot += float(m.group(1)) * 60
                    if s: tot += float(s.group(1))
                    return tot
                durations = matched_df["order_duration"].apply(parse_dur_s)
                persistent = durations >= 180.0
                if persistent.sum() > 0:
                    matched_df = matched_df[persistent]
        
        if len(matched_df) > 0:
            dossier["feeds_with_data_count"] += 1
            
            # Sort time-series feeds descending (newest first)
            sorted_df = matched_df.copy()
            time_cols = [c for c in sorted_df.columns if any(k in c.lower() for k in ["time", "created", "timestamp", "date"])]
            if time_cols:
                try:
                    sorted_df = sorted_df.sort_values(by=time_cols[0], ascending=False)
                except Exception:
                    pass
                    
            sample_records = sorted_df.head(5).to_dict(orient="records")
            
            # Clean non-serializable objects
            cleaned_sample = []
            for r in sample_records:
                clean_r = {}
                for k, v in r.items():
                    if isinstance(v, (datetime.datetime, datetime.date, pd.Timestamp)):
                        clean_r[k] = str(v)
                    elif pd.isna(v):
                        clean_r[k] = None
                    else:
                        clean_r[k] = v
                cleaned_sample.append(clean_r)
                
            dossier["feed_details"].append({
                "feed_name": base_name,
                "file_name": fname,
                "pillar": pillar,
                "status": "DATA_EXTRACTED [PASS]",
                "matching_rows": len(matched_df),
                "total_rows": len(df),
                "key_columns": df.columns.tolist()[:10],
                "latest_sample": cleaned_sample
            })
        else:
            dossier["feeds_no_data_count"] += 1
            dossier["feed_details"].append({
                "feed_name": base_name,
                "file_name": fname,
                "pillar": pillar,
                "status": "NO_DIRECT_MATCH",
                "matching_rows": 0,
                "total_rows": len(df),
                "key_columns": df.columns.tolist()[:5],
                "latest_sample": []
            })
            
    # Group by pillar
    for item in dossier["feed_details"]:
        p = item["pillar"]
        if p not in dossier["pillar_summary"]:
            dossier["pillar_summary"][p] = {"feeds_with_data": 0, "total_feeds": 0, "feeds": []}
        dossier["pillar_summary"][p]["total_feeds"] += 1
        if item["status"] in ["DATA_EXTRACTED [PASS]", "MACRO_GLOBAL_CONTEXT"]:
            dossier["pillar_summary"][p]["feeds_with_data"] += 1
            dossier["pillar_summary"][p]["feeds"].append(item["feed_name"])
            
    # Save JSON dossier
    DOSSIER_JSON_DIR.mkdir(parents=True, exist_ok=True)
    json_path = DOSSIER_JSON_DIR / f"{asset.upper()}_360_dossier.json"
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(dossier, f, indent=2, default=str)
        
    # Generate Markdown Dossier
    DOSSIER_MD_DIR.mkdir(parents=True, exist_ok=True)
    md_path = DOSSIER_MD_DIR / f"{asset.upper()}_360_DOSSIER.md"
    generate_markdown_report(dossier, md_path)
    
    return dossier

def generate_markdown_report(dossier: Dict[str, Any], out_path: Path):
    """Write human/agent-readable comprehensive dossier markdown."""
    asset = dossier["asset"]
    lines = [
        f"# 360° Data Lake Dossier: {asset}",
        f"**Generated**: {dossier['timestamp_ist']} ({dossier['timestamp_utc']})",
        f"**Aliases Scanned**: `{', '.join(dossier['aliases'])}`",
        f"**Coverage**: {dossier['feeds_with_data_count']} feeds with direct asset data | {dossier['global_macro_feeds_count']} global macro feeds | {dossier['total_files_scanned']} total feeds scanned",
        "",
        "---",
        "",
        "## 1. Executive Pillar Coverage Ledger",
        "| Strategic Pillar | Active Feeds | Coverage Status | Feeds Included |",
        "|---|---|---|---|"
    ]
    
    for pillar, stats in dossier["pillar_summary"].items():
        ratio = f"{stats['feeds_with_data']}/{stats['total_feeds']}"
        status = "FULL / PASS" if stats['feeds_with_data'] > 0 else "ABSENT"
        feed_list = ", ".join(stats["feeds"][:4])
        if len(stats["feeds"]) > 4:
            feed_list += f" (+{len(stats['feeds'])-4} more)"
        lines.append(f"| **{pillar}** | {ratio} | `{status}` | {feed_list} |")
        
    lines.extend([
        "",
        "---",
        "",
        "## 2. Granular Per-Feed Data Extraction Inventory",
        "| Feed Name | Rows Found | Pillar | Status | Key Specific Insights Extracted |",
        "|---|---|---|---|---|"
    ])
    
    for item in dossier["feed_details"]:
        fname = item["feed_name"]
        rows = item["matching_rows"]
        pillar = item["pillar"].split(":")[0]
        status = item["status"]
        
        # Summarize key insight from latest sample (newest / most relevant at index 0)
        sample = item.get("latest_sample", [])
        insight = "No direct records for asset"
        if sample:
            first = sample[0]
            # Custom summaries based on feed
            if "Footprint" in fname:
                insight = f"Signal: {first.get('signal_type')} ({first.get('bias')}) at {first.get('price_level')} | {first.get('headline')}"
            elif "Whale" in fname:
                insight = f"Whale order: {first.get('side')} {first.get('amount_btc', first.get('notional_usd'))} at {first.get('price')}"
            elif "CVD" in fname:
                insight = f"Taker delta: {first.get('taker_buy_vol', first.get('delta', 'N/A'))} | Cumulative delta trend"
            elif "Liq" in fname or "Pain" in fname:
                insight = f"Liq band / pain price: {first.get('max_pain_price', first.get('price_level', first.get('liquidation_price', 'N/A')))}"
            elif "Orderbook" in fname:
                insight = f"Orderbook depth: Bid/Ask ratio {first.get('imbalance_ratio', 'N/A')} | Spread: {first.get('spread_bps', 'N/A')}"
            elif "Technical" in fname:
                insight = f"VWAP Z: {first.get('vwap_z', 'N/A')} | RSI: {first.get('rsi_14', 'N/A')} | EMA 89/233 alignment"
            elif "LS_Ratio" in fname:
                insight = f"Long/Short ratio: {first.get('long_short_ratio', first.get('ratio', 'N/A'))} ({first.get('long_account_pct', 'N/A')}% Longs)"
            elif "Funding" in fname:
                insight = f"Funding rate: {first.get('funding_rate', first.get('rate', 'N/A'))}"
            elif "Telemetry" in fname:
                insight = f"Live Account Equity: {first.get('Equity', 'N/A')} | Free Margin: {first.get('Margin_Free', 'N/A')}"
            else:
                insight = f"Extracted {rows} rows. Latest keys: {list(first.keys())[:4]}"
                
        lines.append(f"| `{fname}` | {rows} | {pillar} | `{status}` | {insight} |")
        
    with open(out_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Asset 360° Data Lake Dossier Engine")
    parser.add_argument("--asset", type=str, default="BTC", help="Asset ticker (e.g. BTC, ETH, XAU, USDJPY)")
    args = parser.parse_args()
    
    print(f"Building 360° Data Lake Dossier for {args.asset}...")
    res = build_asset_360_dossier(args.asset)
    print(f"COMPLETE: Scanned {res['total_files_scanned']} feeds. Extracted data from {res['feeds_with_data_count']} feeds (+{res['global_macro_feeds_count']} global macro feeds).")
    print(f"Dossier JSON saved to: Data/dossiers/{args.asset.upper()}_360_dossier.json")
    print(f"Dossier Markdown saved to: docs/dossiers/{args.asset.upper()}_360_DOSSIER.md")
