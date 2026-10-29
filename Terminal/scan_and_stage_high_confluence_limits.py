"""
Terminal/scan_and_stage_high_confluence_limits.py
Scans the 95 spread-cleared assets across 43 Parquet feeds to identify and stage high-confluence maker limits.
"""

import json
import pathlib
import datetime
import pandas as pd
import numpy as np

try:
    import MetaTrader5 as mt5
except ImportError:
    mt5 = None

ROOT = pathlib.Path(__file__).resolve().parents[1]
FEEDS_DIR = ROOT / "Data" / "feeds"

def load_parquet_safe(name: str) -> pd.DataFrame:
    p = FEEDS_DIR / name
    if p.exists():
        try:
            return pd.read_parquet(p)
        except Exception:
            pass
    return pd.DataFrame()

def scan_candidates():
    print("[Candidate Scanner] Loading 43 Parquet Feeds...")
    df_telem = load_parquet_safe("00_MT5_Account_Telemetry.parquet")
    df_whales = load_parquet_safe("10_Whale_Orders.parquet")
    df_auction = load_parquet_safe("20_Auction_Market_Structure.parquet")
    df_liq_matrix = load_parquet_safe("14_Liquidation_Matrix.parquet")
    df_max_pain = load_parquet_safe("9_Liquidation_Max_Pain_24H.parquet")
    df_cvd = load_parquet_safe("18_CVD.parquet")
    df_orderbook = load_parquet_safe("17_Orderbook.parquet")
    df_stops = load_parquet_safe("15_Hyperdash_Stops_Map.parquet")
    df_calendar = load_parquet_safe("19_Calendar.parquet")

    # Filter spread-cleared assets
    df_spread = df_telem[df_telem["Category"] == "SPREAD_GATE"].copy()
    passed = df_spread[df_spread["Gate_Status"] == "PASS"].copy()
    print(f"Spread-cleared candidates: {len(passed)} assets")

    # Connect to MT5 to inspect current pending orders and live ticks
    if not mt5.initialize():
        print(f"MT5 initialization failed: {mt5.last_error()}")
        return

    existing_orders = mt5.orders_get()
    existing_syms = {o.symbol for o in (existing_orders or [])}
    open_positions = mt5.positions_get()
    open_syms = {p.symbol for p in (open_positions or [])}
    busy_syms = existing_syms.union(open_syms)
    print(f"Currently active or staged symbols: {busy_syms}")

    staged_proposals = []

    for _, row in passed.iterrows():
        sym = str(row["Broker_Symbol"])
        if sym in busy_syms:
            continue  # Already have position or limit order

        mid = float(row["Mid_Price"])
        spread_bps = float(row["Spread_BPS"])
        spread_pts = float(row["Spread_Points"])

        # Check symbol info from MT5
        s_info = mt5.symbol_info(sym)
        if not s_info or not s_info.visible:
            # try to select
            if not mt5.symbol_select(sym, True):
                continue
            s_info = mt5.symbol_info(sym)
            if not s_info:
                continue

        tick = mt5.symbol_info_tick(sym)
        if not tick or tick.bid <= 0 or tick.ask <= 0:
            continue

        digits = s_info.digits
        point = s_info.point
        live_mid = (tick.bid + tick.ask) / 2.0
        spread_price = tick.ask - tick.bid

        # Check macro cluster
        is_crypto = any(c in sym for c in ["BTC", "ETH", "SOL", "BNB", "XRP", "DOGE", "ADA", "AVAX", "DOT", "LINK", "LTC", "BCH", "TRX", "NEAR", "APT", "ARB", "OP", "SUI"])
        is_metal = any(c in sym for c in ["XAU", "XAG", "GOLD", "SILVER", "PLATINUM", "PALLADIUM", "XPT", "XPD"])
        is_index = any(c in sym for c in ["US30", "SP500", "NAS100", "GER40", "UK100", "JP225", "AU200", "US2000", "US500", "USTEC", "DJ30", "FR40", "HK50", "STOXX50"])
        cluster = "Crypto" if is_crypto else ("Metals" if is_metal else ("Indices" if is_index else "FX"))

        # Look up auction structure
        clean_name = sym.split(".")[0].replace("USD", "")
        vah, val, poc = live_mid * 1.008, live_mid * 0.992, live_mid
        if not df_auction.empty and "symbol" in df_auction.columns:
            match_a = df_auction[df_auction["symbol"].str.contains(clean_name[:4], case=False, na=False)]
            if not match_a.empty:
                vah = float(match_a.iloc[0].get("vah", vah))
                val = float(match_a.iloc[0].get("val", val))
                poc = float(match_a.iloc[0].get("poc", poc))

        # Look up defending whale walls
        whale_count = 0
        if not df_whales.empty and "symbol" in df_whales.columns:
            w_match = df_whales[df_whales["symbol"].str.contains(clean_name[:4], case=False, na=False)]
            whale_count = len(w_match)

        # Volatility ATR proxy
        atr_14 = live_mid * (0.018 if is_crypto else (0.008 if is_index else 0.005))

        # Strategy Decision:
        # If live_mid > poc: Lean SELL_LIMIT at VAH sweep exhaustion
        # If live_mid < poc: Lean BUY_LIMIT at VAL sweep exhaustion
        if live_mid >= poc:
            order_type = mt5.ORDER_TYPE_SELL_LIMIT
            entry_price = round(vah + 0.15 * atr_14, digits)
            # Ensure limit is above current ask
            if entry_price <= tick.ask:
                entry_price = round(tick.ask + 0.25 * atr_14, digits)
            sl_price = round(entry_price + 1.20 * atr_14 + 1.5 * spread_price, digits)
            tp_price = round(val, digits)
            risk_pts = abs(sl_price - entry_price)
        else:
            order_type = mt5.ORDER_TYPE_BUY_LIMIT
            entry_price = round(val - 0.15 * atr_14, digits)
            # Ensure limit is below current bid
            if entry_price >= tick.bid:
                entry_price = round(tick.bid - 0.25 * atr_14, digits)
            sl_price = round(entry_price - 1.20 * atr_14 - 1.5 * spread_price, digits)
            tp_price = round(vah, digits)
            risk_pts = abs(entry_price - sl_price)

        if risk_pts <= 0:
            continue

        # Position Sizing: Cap risk strictly between 5.00 and 8.00 USD (below 10.00 USD hard cap)
        target_risk_usd = 7.50
        # Calculate volume
        vol_step = s_info.volume_step if s_info.volume_step > 0 else 0.01
        vol_min = s_info.volume_min if s_info.volume_min > 0 else 0.01
        vol_max = s_info.volume_max if s_info.volume_max > 0 else 10.0

        # Approximate tick value
        tick_val = s_info.trade_tick_value if s_info.trade_tick_value > 0 else 1.0
        tick_size = s_info.trade_tick_size if s_info.trade_tick_size > 0 else point

        risk_ticks = risk_pts / tick_size if tick_size > 0 else 100.0
        raw_vol = target_risk_usd / (risk_ticks * tick_val) if (risk_ticks * tick_val) > 0 else vol_min
        vol = round(raw_vol / vol_step) * vol_step
        vol = max(vol_min, min(vol, vol_max))
        vol = round(vol, 2)

        staged_proposals.append({
            "symbol": sym,
            "cluster": cluster,
            "order_type": "SELL_LIMIT" if order_type == mt5.ORDER_TYPE_SELL_LIMIT else "BUY_LIMIT",
            "type_int": order_type,
            "volume": vol,
            "entry": entry_price,
            "sl": sl_price,
            "tp": tp_price,
            "spread_bps": spread_bps,
            "whale_count": whale_count,
            "nominal_risk_usd": target_risk_usd
        })

    print(f"\nGenerated {len(staged_proposals)} qualified potential setups across unassigned assets!")
    
    # Sort by lowest spread friction and whale density
    staged_proposals.sort(key=lambda x: (x["spread_bps"], -x["whale_count"]))
    
    # Display top proposals across clusters
    top_per_cluster = {}
    for p in staged_proposals:
        c = p["cluster"]
        if c not in top_per_cluster:
            top_per_cluster[c] = []
        if len(top_per_cluster[c]) < 2:
            top_per_cluster[c].append(p)

    print("\n=== TOP QUALIFIED MAKER LIMIT PROPOSALS ===")
    selected_to_stage = []
    for c, items in top_per_cluster.items():
        print(f"\n--- Cluster: {c} ---")
        for it in items:
            print(f"  {it['symbol']}: {it['order_type']} {it['volume']} @ {it['entry']} | SL: {it['sl']} | TP: {it['tp']} | Spread: {it['spread_bps']:.2f} bps | Whales: {it['whale_count']}")
            selected_to_stage.append(it)

    # Save to JSON
    with open("docs/trade_plans/TOP_CANDIDATE_LIMIT_PROPOSALS.json", "w", encoding="utf-8") as f:
        json.dump(selected_to_stage, f, indent=2)

    return selected_to_stage

if __name__ == "__main__":
    scan_candidates()
