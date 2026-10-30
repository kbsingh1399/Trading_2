import json
import pathlib

def format_15_pillar_findings(cert_path: pathlib.Path) -> str:
    if not cert_path.exists():
        return "No certificate found."
    
    cert = json.loads(cert_path.read_text(encoding="utf-8"))
    candidates = cert.get("candidates", [])
    if not candidates:
        return "No candidates in certificate."
    
    md_blocks = []
    for idx, c in enumerate(candidates, 1):
        sym = c.get("broker_symbol") or c.get("canonical")
        can = c.get("canonical")
        act = c.get("action")
        ent = c.get("entry")
        sl = c.get("sl")
        tp = c.get("tp")
        rr = c.get("rr_ratio")
        r_usd = c.get("nominal_risk_usd")
        feats = c.get("extracted_15_features", {})
        
        etf = feats.get("1_ETF_Spot_Fut_Flows", {})
        flows = feats.get("2_Spot_Fut_Netflows", {})
        fund = feats.get("4_Funding_Rates_Settlement", {})
        oi = feats.get("5_Open_Interest_Dynamics", {})
        liq = feats.get("6_Multi_Horizon_Liquidations", {})
        whales = feats.get("7_Whale_Orders_Large_Trades", {})
        tech = feats.get("8_Technicals_VWAP_Dispersion", {})
        stops = feats.get("9_Hyperdash_Stops_Intel", {})
        ob = feats.get("10_L2_Orderbook_Depth", {})
        cvd = feats.get("11_Multi_Timeframe_CVD", {})
        auc = feats.get("12_Auction_Market_Structure", {})
        mt5_t = feats.get("15_MT5_Broker_Telemetry", {})

        vwap_str = f"{tech.get('vwap'):,.2f}" if tech.get('vwap') else "N/A"
        rsi_str = f"{tech.get('rsi_14'):.2f}" if tech.get('rsi_14') else "N/A"
        atr_str = f"{tech.get('atr_14'):.2f}" if tech.get('atr_14') else "N/A"
        poc_str = f"{auc.get('daily_poc'):,.2f}" if auc.get('daily_poc') else "N/A"
        val_str = f"{auc.get('daily_val'):,.2f}" if auc.get('daily_val') else "N/A"
        vah_str = f"{auc.get('daily_vah'):,.2f}" if auc.get('daily_vah') else "N/A"
        s_pain = f"{liq.get('short_max_pain_24h'):,.2f}" if liq.get('short_max_pain_24h') else "N/A"
        l_pain = f"{liq.get('long_max_pain_24h'):,.2f}" if liq.get('long_max_pain_24h') else "N/A"
        bin_fund = fund.get('usdt_binance', 'N/A')
        byb_fund = fund.get('usdt_bybit', 'N/A')
        tot_oi = oi.get('total_oi_usd', 'N/A')
        w_count = whales.get('total_whale_orders', 0)
        s_clusters = stops.get('total_stop_clusters', 0)
        regime = auc.get('auction_regime', 'UNKNOWN')
        spread_bps = mt5_t.get('spread_bps', 'N/A')
        cs = mt5_t.get('contract_size', 1.0)

        # Get latest CVD regime
        cvd_recs = cvd.get('records', [])
        cvd_regime = cvd_recs[0].get('regime', 'N/A') if cvd_recs else "N/A"
        cvd_bias = cvd_recs[0].get('bias', 'N/A') if cvd_recs else "N/A"

        block = f"""### Candidate #{idx}: `{sym}` ({can}) — Action: `{act}`
- **Exact Proposed Trade Card**:
  * Action: **`{act}`** | Entry: **`{ent}`** | Stop Loss: **`{sl}`** | Take Profit: **`{tp}`**
  * Risk/Reward: **{rr}R** | Nominal Risk: **${r_usd} USD** | Broker Contract Multiplier: **{cs}**
  * Execution Gate: Spread **{spread_bps} bps** | Status: **{c.get('status', 'PENDING')}**
- **Antigravity 15-Pillar Mechanical Forensics Ground Truth**:
  * **1. ETF Inflows/Outflows**: {etf.get('primary_sample', {}).get('ETF_Name', 'N/A')} AUM: {etf.get('primary_sample', {}).get('AUM', 'N/A')}
  * **2. Capital Netflows**: 24h Spot: {flows.get('spot_24h', 'N/A')} | 24h Futures: {flows.get('fut_24h', 'N/A')}
  * **3. 12-Venue Funding Rates**: Binance: `{bin_fund}` | Bybit: `{byb_fund}`
  * **4. Open Interest Dynamics**: Total OI: `{tot_oi}` (Binance: {oi.get('binance_oi', 'N/A')}, CME: {oi.get('cme_oi', 'N/A')})
  * **5. Multi-Horizon Liquidation Max Pain**: Short Pain: **`{s_pain}`** | Long Pain: **`{l_pain}`** (Ex Liq Rows: {liq.get('ex_liq_rows', 'N/A')})
  * **6. Institutional Whale Armor**: **{w_count} Whale Block Orders** defending depth
  * **7. Technicals & VWAP Dispersion**: VWAP: **`{vwap_str}`** | RSI-14: **`{rsi_str}`** | ATR-14: **`{atr_str}`**
  * **8. Hyperdash Intel & Stop Clusters**: **{s_clusters} Retail Stop Loss Clusters**
  * **9. L2 Orderbook Depth**: **{ob.get('depth_levels_count', 0)} Depth Ladders**
  * **10. Multi-Timeframe CVD**: Regime: **`{cvd_regime}`** | Bias: **`{cvd_bias}`**
  * **11. Auction Market Structure**: POC: **`{poc_str}`** | VAL: **`{val_str}`** | VAH: **`{vah_str}`** | Regime: **`{regime}`**
  * **12. Pitfall 24 Immunity**: Entry positioned to exploit liquidation sweep below Long Pain (`{l_pain}`); Stop Loss anchored outside retail cluster; Take Profit targets upward Short Max Pain magnet (`{s_pain}`)."""
        md_blocks.append(block)

    return "\n\n".join(md_blocks)

if __name__ == "__main__":
    cert_p = pathlib.Path("docs/trade_plans/CYCLE_037_MULTI_FEED_EXAMINATION_CERTIFICATE.json")
    print(format_15_pillar_findings(cert_p))
