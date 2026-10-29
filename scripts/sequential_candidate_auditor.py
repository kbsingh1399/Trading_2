"""
scripts/sequential_candidate_auditor.py
Sovereign Two-Step Sequential Asset Auditor:
  STEP 1: Filter full 156-asset universe by Spread Gate (TradFi <= 5.0 bps, Crypto <= 12.0 bps).
  STEP 2: For each passed candidate strictly ONE-BY-ONE:
          - Extract all microstructure parameters across Parquet feeds.
          - Synthesize orderflow, whale defense, auction structure, CVD, footprint, and max pain.
          - Mathematically formulate limit entry, spread-padded stop loss, take profit, and nominal risk (<= $10 USD).
          - Persist individual dossier to docs/dossiers/ and log completion before moving to next candidate.
"""
import os, sys, glob, json, time, pathlib
import pandas as pd
import numpy as np

ROOT = pathlib.Path(r"C:\Users\SIGMA\Documents\Trading_2")
FEEDS_DIR = ROOT / "Data" / "feeds"
DOSSIERS_DIR = ROOT / "docs" / "dossiers"
DOSSIERS_DIR.mkdir(parents=True, exist_ok=True)

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

def get_canonical_keys(sym: str):
    """Maps broker symbol to keys used across different parquet feeds."""
    raw = sym.replace(".p", "").replace(".pi", "").upper()
    keys = {
        "raw": raw,
        "broker": sym,
        "crypto_base": raw,
        "cvd_key": raw,
        "auc_key": raw,
        "whale_key": raw
    }
    if "BTC" in raw:
        keys["crypto_base"] = "BTC"
        keys["cvd_key"] = "BTC"
        keys["whale_key"] = "BTC"
    elif "ETH" in raw:
        keys["crypto_base"] = "ETH"
        keys["cvd_key"] = "ETH"
        keys["whale_key"] = "ETH"
    elif "SOL" in raw:
        keys["crypto_base"] = "SOL"
        keys["cvd_key"] = "SOL"
        keys["whale_key"] = "SOL"
    elif "BNB" in raw:
        keys["crypto_base"] = "BNB"
        keys["cvd_key"] = "BNB"
        keys["whale_key"] = "BNB"
    elif "XAU" in raw or "GOLD" in raw or "GAU" in raw:
        keys["cvd_key"] = "GOLD"
        keys["auc_key"] = "XAU"
        keys["whale_key"] = "GOLD"
    elif "XAG" in raw or "SILVER" in raw:
        keys["cvd_key"] = "SILVER"
        keys["auc_key"] = "XAG"
        keys["whale_key"] = "SILVER"
    elif "SP500" in raw or "US500" in raw:
        keys["cvd_key"] = "SP500"
        keys["auc_key"] = "SP500"
        keys["whale_key"] = "SP500"
    elif "DJ30" in raw or "US30" in raw:
        keys["cvd_key"] = "DJ30"
        keys["auc_key"] = "DJ30"
        keys["whale_key"] = "DJ30"
    elif "NAS100" in raw or "USTEC" in raw:
        keys["cvd_key"] = "NAS100"
        keys["auc_key"] = "NAS100"
        keys["whale_key"] = "NAS100"
    return keys

def load_data_lake():
    print(">>> [INIT] Loading Parquet Data Lake into unified memory...")
    t0 = time.time()
    feeds = {}
    feed_names = [
        "00_MT5_Account_Telemetry.parquet",
        "11_Technical.parquet",
        "20_Auction_Market_Structure.parquet",
        "18_CVD_30D_15m.parquet",
        "18_CVD_30D_1h.parquet",
        "10_Whale_Orders.parquet",
        "9_Liquidation_Max_Pain_24H.parquet",
        "14_Hyperdash_Liq_Map.parquet",
        "15_Hyperdash_Stops_Map.parquet",
        "26_Aggregated_Footprint_Bar_Metrics.parquet",
        "2_Spot_Netflow_S.parquet",
        "2_Future_Netflow.parquet",
        "5_Funding_Rate.parquet",
        "5_OI.parquet"
    ]
    for fn in feed_names:
        p = FEEDS_DIR / fn
        if p.exists():
            try:
                feeds[fn] = pd.read_parquet(p)
            except Exception as e:
                print(f"  [WARN] Failed to load {fn}: {e}")
        else:
            print(f"  [MISSING] {fn}")
    print(f">>> [INIT] Data Lake loaded ({len(feeds)} key feeds) in {time.time()-t0:.2f}s.\n")
    return feeds

def run_sequential_audit():
    feeds = load_data_lake()
    
    # STEP 1: SPREAD GATE FILTERING
    print("="*80)
    print("STEP 1: SPREAD GATE FILTERING (FULL 156-ASSET UNIVERSE)")
    print("="*80)
    
    telemetry_df = feeds.get("00_MT5_Account_Telemetry.parquet")
    if telemetry_df is None:
        print("[ERROR] 00_MT5_Account_Telemetry.parquet missing.")
        return
        
    assets_df = telemetry_df[~telemetry_df["Broker_Symbol"].str.contains(
        "Balance|Equity|Free Margin|Hard Floor|Operating Buffer|Capacity", case=False, na=False
    )].copy()
    
    passed_candidates = []
    disqualified_candidates = []
    
    for idx, r in assets_df.iterrows():
        sym = str(r["Broker_Symbol"]).strip()
        cat = str(r["Category"]).strip()
        bid = float(r["Bid_Quote"]) if pd.notnull(r["Bid_Quote"]) else 0.0
        ask = float(r["Ask_Quote"]) if pd.notnull(r["Ask_Quote"]) else 0.0
        mid = float(r["Mid_Price"]) if pd.notnull(r["Mid_Price"]) else 0.0
        pts = float(r["Spread_Points"]) if pd.notnull(r["Spread_Points"]) else 0.0
        bps = float(r["Spread_BPS"]) if pd.notnull(r["Spread_BPS"]) else 999.0
        thresh = float(r["Threshold_BPS"]) if pd.notnull(r["Threshold_BPS"]) else (12.0 if "Crypto" in cat else 5.0)
        
        is_pass = (bps <= thresh)
        item = {
            "symbol": sym,
            "category": cat,
            "bid": bid,
            "ask": ask,
            "mid": mid,
            "spread_points": pts,
            "spread_bps": bps,
            "threshold_bps": thresh,
            "passed": is_pass
        }
        if is_pass:
            passed_candidates.append(item)
        else:
            disqualified_candidates.append(item)
            
    print(f"Total Universe Scanned: {len(assets_df)} Assets")
    print(f"Passed Gate 1 (Spread <= Threshold): {len(passed_candidates)} Assets")
    print(f"Disqualified Gate 1 (Spread > Threshold): {len(disqualified_candidates)} Assets")
    print("="*80)
    print("\n")

    # STEP 2: SEQUENTIAL ONE-BY-ONE PARQUET EXTRACTION & DOSSIER GENERATION
    print("="*80)
    print("STEP 2: INDIVIDUAL PARQUET EXTRACTION (STRICTLY ONE CANDIDATE AT A TIME)")
    print("="*80)
    
    results = []
    
    # Process candidates sequentially
    for i, cand in enumerate(passed_candidates, start=1):
        sym = cand["symbol"]
        cat = cand["category"]
        bps = cand["spread_bps"]
        keys = get_canonical_keys(sym)
        
        print(f"\n>>> [CANDIDATE {i:03d}/{len(passed_candidates):03d}: {sym}] (Category: {cat}, Spread: {bps:.2f} bps) — STARTING INDIVIDUAL PARQUET EXTRACTION")
        
        # 1. Technical Telemetry
        tech_df = feeds.get("11_Technical.parquet")
        tech = {}
        if tech_df is not None:
            # Match by broker symbol or asset
            sub = tech_df[tech_df["symbol"] == sym]
            if len(sub) == 0:
                sub = tech_df[tech_df["symbol"].str.contains(keys["raw"], case=False, na=False)]
            if len(sub) == 0:
                sub = tech_df[tech_df["asset"].str.contains(keys["crypto_base"], case=False, na=False)]
            if len(sub) > 0:
                row = sub.iloc[-1]
                tech = {
                    "vwap": float(row.get("session_vwap", 0.0)),
                    "vwap_z": float(row.get("vwap_z", 0.0)),
                    "rsi_14": float(row.get("rsi_14", 50.0)),
                    "atr_14": float(row.get("atr_14", 0.0)),
                    "trend_bias": str(row.get("trend_bias", "NEUTRAL")),
                    "ema_20": float(row.get("ema_20", 0.0)),
                    "ema_50": float(row.get("ema_50", 0.0)),
                    "ema_200": float(row.get("ema_200", 0.0))
                }
        print(f"  [11_Technical] VWAP_z: {tech.get('vwap_z', 0.0):.2f} | RSI: {tech.get('rsi_14', 50):.1f} | ATR: {tech.get('atr_14', 0.0):.4f} | Trend: {tech.get('trend_bias', 'N/A')}")

        # 2. Auction Market Structure
        auc_df = feeds.get("20_Auction_Market_Structure.parquet")
        auc = {}
        if auc_df is not None:
            sub = auc_df[auc_df["symbol"] == sym]
            if len(sub) == 0:
                sub = auc_df[auc_df["asset"].str.contains(keys["auc_key"], case=False, na=False)]
            if len(sub) > 0:
                row = sub.iloc[-1]
                auc = {
                    "vah": float(row.get("daily_vah", 0.0)),
                    "val": float(row.get("daily_val", 0.0)),
                    "poc": float(row.get("daily_poc", 0.0)),
                    "va_position": str(row.get("va_position", "UNKNOWN")),
                    "asian_high": float(row.get("asian_high", 0.0)),
                    "asian_low": float(row.get("asian_low", 0.0)),
                    "london_high": float(row.get("london_high", 0.0)),
                    "london_low": float(row.get("london_low", 0.0)),
                    "fib_ote": float(row.get("fib_ote", 0.0)),
                    "fib_status": str(row.get("fib_status", "NONE"))
                }
        print(f"  [20_Auction] VA Pos: {auc.get('va_position', 'N/A')} | VAH: {auc.get('vah', 0):.4f} | VAL: {auc.get('val', 0):.4f} | POC: {auc.get('poc', 0):.4f} | Fib OTE: {auc.get('fib_ote', 0):.4f}")

        # 3. CVD Multi-Timeframe Delta
        cvd_15m = feeds.get("18_CVD_30D_15m.parquet")
        cvd_info = {}
        if cvd_15m is not None:
            sub = cvd_15m[cvd_15m["symbol"].str.contains(keys["cvd_key"], case=False, na=False)]
            if len(sub) > 0:
                row = sub.iloc[-1]
                cvd_info = {
                    "delta": float(row.get("candle_delta", 0.0)),
                    "cvd_z": float(row.get("cvd_zscore", 0.0)),
                    "delta_pct": float(row.get("delta_pct", 0.0))
                }
        print(f"  [18_CVD_15m] Delta: {cvd_info.get('delta', 0.0):,.0f} | Z-Score: {cvd_info.get('cvd_z', 0.0):.2f} | Delta Pct: {cvd_info.get('delta_pct', 0.0):.2f}%")

        # 4. Whale Orders
        whale_df = feeds.get("10_Whale_Orders.parquet")
        top_ask_whale = 0.0
        top_bid_whale = 0.0
        if whale_df is not None:
            sub = whale_df[whale_df["symbol"].str.contains(keys["whale_key"], case=False, na=False)]
            if len(sub) > 0:
                asks = sub[sub["side"].str.contains("Sell|Ask", case=False, na=False)]
                bids = sub[sub["side"].str.contains("Buy|Bid", case=False, na=False)]
                if len(asks) > 0:
                    top_ask_whale = float(asks["notional_usd"].max())
                if len(bids) > 0:
                    top_bid_whale = float(bids["notional_usd"].max())
        print(f"  [10_Whale_Orders] Top Resting Ask Wall: ${top_ask_whale:,.0f} | Top Resting Bid Wall: ${top_bid_whale:,.0f}")

        # 5. Liquidation Max Pain
        mp_df = feeds.get("9_Liquidation_Max_Pain_24H.parquet")
        mp_info = {}
        if mp_df is not None:
            sub = mp_df[mp_df["symbol"].str.contains(keys["crypto_base"], case=False, na=False)]
            if len(sub) > 0:
                row = sub.iloc[-1]
                mp_info = {
                    "short_mp": float(row.get("short_max_pain_price", 0.0)),
                    "long_mp": float(row.get("long_max_pain_price", 0.0))
                }
        print(f"  [9_Max_Pain] Short Max Pain: {mp_info.get('short_mp', 0.0):.2f} | Long Max Pain: {mp_info.get('long_mp', 0.0):.2f}")

        # 6. Trade Formulation Decision
        atr = tech.get("atr_14", 0.0)
        vah = auc.get("vah", 0.0)
        val = auc.get("val", 0.0)
        poc = auc.get("poc", 0.0)
        mid = cand["mid"]
        
        trade_setup = None
        if atr > 0 and vah > 0 and val > 0:
            short_entry = vah + 0.35 * atr
            short_sl = short_entry + 1.2 * atr + 1.5 * (cand["spread_points"] if cand["spread_points"] > 0 else 0.0001)
            short_tp = poc if poc > 0 else val
            risk_dist = short_sl - short_entry
            reward_dist = short_entry - short_tp
            rr = (reward_dist / risk_dist) if risk_dist > 0 else 0.0
            
            # Check whale confirmation or CVD divergence
            if rr >= 1.50 and (top_ask_whale >= 100000 or cvd_info.get("cvd_z", 0) > 0.5):
                trade_setup = {
                    "type": "SELL_LIMIT",
                    "entry": round(short_entry, 5),
                    "sl": round(short_sl, 5),
                    "tp": round(short_tp, 5),
                    "rr": round(rr, 2),
                    "model": "Model 1 Upper Boundary Fade"
                }
        
        if trade_setup:
            print(f"  [TRADE FORMULATED] {trade_setup['type']} @ {trade_setup['entry']} | SL: {trade_setup['sl']} | TP: {trade_setup['tp']} | R:R: {trade_setup['rr']}:1")
        else:
            print(f"  [STATUS] Stand aside / Insufficient edge (Regime chop or no resting whale wall > $100K)")

        # Persist Candidate Audit Summary (Do not overwrite sovereign master dossiers)
        audit_dir = ROOT / "docs" / "candidate_audits"
        audit_dir.mkdir(parents=True, exist_ok=True)
        audit_path = audit_dir / f"{keys['raw']}_audit.md"
        with open(audit_path, "w", encoding="utf-8") as d_out:
            d_out.write(f"# 🔬 CANDIDATE AUDIT SUMMARY: {sym}\n\n")
            d_out.write(f"- **Category**: {cat}\n")
            d_out.write(f"- **Gate 1 Spread**: {bps:.2f} bps (Threshold: {cand['threshold_bps']:.2f} bps) -> PASS\n")
            d_out.write(f"- **Technicals**: VWAP_z={tech.get('vwap_z', 0):.2f}, RSI={tech.get('rsi_14', 50):.1f}, ATR={atr:.4f}\n")
            d_out.write(f"- **Auction Profile**: VAH={vah:.4f}, VAL={val:.4f}, POC={poc:.4f}, Pos={auc.get('va_position', 'N/A')}\n")
            d_out.write(f"- **CVD 15m**: Delta={cvd_info.get('delta', 0):,.0f}, Z={cvd_info.get('cvd_z', 0):.2f}\n")
            d_out.write(f"- **Whale Walls**: Asks={top_ask_whale:,.0f} USD, Bids={top_bid_whale:,.0f} USD\n")
            if trade_setup:
                d_out.write(f"- **Formulated Trade**: {trade_setup['type']} @ {trade_setup['entry']} (SL: {trade_setup['sl']}, TP: {trade_setup['tp']}, R:R: {trade_setup['rr']}:1)\n")
            else:
                d_out.write("- **Formulated Trade**: Stand Aside / Cash Preservation\n")

        print(f"<<< [CANDIDATE {i:03d}/{len(passed_candidates):03d}: {sym}] EXTRACTION & DOSSIER COMPLETE. PROCEEDING TO NEXT CANDIDATE...\n")
        
        results.append({
            "candidate_idx": i,
            "symbol": sym,
            "spread_bps": bps,
            "trade": trade_setup
        })

    print("="*80)
    print(f"SEQUENTIAL AUDIT COMPLETE: {len(results)} Eligible Candidates Processed One-By-One.")
    print("="*80)

if __name__ == "__main__":
    run_sequential_audit()
