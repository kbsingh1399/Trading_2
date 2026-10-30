import json
import pathlib

p = pathlib.Path("docs/trade_plans/CYCLE_037_MULTI_FEED_EXAMINATION_CERTIFICATE.json")
cert = json.loads(p.read_text(encoding="utf-8"))

for c in cert.get("candidates", []):
    sym = c.get("broker_symbol") or c.get("canonical")
    act = c.get("action")
    ent = c.get("entry")
    sl = c.get("sl")
    tp = c.get("tp")
    rr = c.get("rr_ratio")
    r_usd = c.get("nominal_risk_usd")
    feats = c.get("extracted_15_features", {})
    
    tech = feats.get("8_Technicals_VWAP_Dispersion", {})
    auc = feats.get("12_Auction_Market_Structure", {})
    liq = feats.get("6_Multi_Horizon_Liquidations", {})
    fund = feats.get("4_Funding_Rates_Settlement", {})
    oi = feats.get("5_Open_Interest_Dynamics", {})
    whales = feats.get("7_Whale_Orders_Large_Trades", {})
    stops = feats.get("9_Hyperdash_Stops_Intel", {})
    mt5_t = feats.get("15_MT5_Broker_Telemetry", {})
    
    print(f"Candidate: {sym} | Action: {act} @ {ent} | SL: {sl} | TP: {tp} | RR: {rr}R | Risk: ${r_usd}")
    print(f"  -> POC: {auc.get('poc')} | VAL: {auc.get('val')} | VAH: {auc.get('vah')}")
    print(f"  -> VWAP: {tech.get('vwap'):.2f} | RSI: {tech.get('rsi_14'):.2f} | ATR: {tech.get('atr_14'):.2f}")
    print(f"  -> Short Pain: {liq.get('short_max_pain_24h')} | Long Pain: {liq.get('long_max_pain_24h')}")
    print(f"  -> Funding Binance: {fund.get('usdt_binance')} | Bybit: {fund.get('usdt_bybit')} | OI: {oi.get('total_oi_usd')}")
    print(f"  -> Whales: {whales.get('total_whale_orders')} | Stop Clusters: {stops.get('total_stop_clusters')}")
    print("-" * 60)
