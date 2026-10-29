# 🔬 MASTER 43-FEED QUANTITATIVE DOSSIER: NETH25 (NET/H25)
**MT5 Symbol**: `NETH25.p` | **Category**: `Forex Cross` | **Tier**: `Tier 2`
**Execution Posture**: `PASSIVE LIMIT ONLY` | **Timestamp**: 2026-10-29 14:43:14 UTC
**Pipeline Clearance**: `QUALIFIED` | **Data Freshness**: `1.2m`

---

## 1. MT5 Live Broker Telemetry & Spread Friction Gate
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet)*
- **Live Bid Quote**: `1141.10000` | **Live Ask Quote**: `1141.40000` | **Mid Price**: `1141.25000`
- **Spread Points**: `30.0 pts` | **Spread BPS**: `2.63 bps` (Mandatory Cap: `25.0 bps`)
- **Gate Status**: **`PASS`** (Spread friction within mandatory threshold; safe for maker execution)
- **Order Allowed**: `BUY_LIMIT / SELL_LIMIT` | **Pillar 1 Clearance**: `QUALIFIED`
- **Broker Specifications**: Contract Size=`1.00` | Tick Value=`1.00 USD` | Min Lot=`0.01` | Digits=`5`
- **Account Capital Context**: Balance=`4,744.55 USD` | Equity=`4,744.32 USD` | Free Margin=`4,342.62 USD` | Inviolate Hard Floor=`4,775.00 USD` (Cushion: `-30.68 USD`)
- **Pipeline Health**: Feed #00 Status=`PASS` | Overall Pipeline Telemetry=`33/33 FEEDS PASS (SYNCHRONIZED)`

---

## 2. Technical Profile, Multi-Sigma VWAP Dispersion & Volatility
*(Sources: 11_Technical.parquet, 11_Technical_BTC_Ribbon.parquet)*
- **Last Verified Price**: `1142.05000` | **24h Change**: `+0.67%` (24h High: `1147.15000`, 24h Low: `1132.90000`)
- **Weekly Range**: Week High=`1147.15000` | Week Low=`1127.75000` | Daily POC=`1135.95000` | Daily VAH=`1142.22000` | Daily VAL=`1134.58000`
- **Session VWAP**: `1140.16872` | **Rolling 24h VWAP**: `1138.79844` | **Distance to VWAP**: `+0.17%`
- **VWAP Z-Score**: `+0.61 sigma` | **Mean Reversion Bias**: **`FAIR VALUE`**
- **VWAP Dispersion Bands**:
  * +1.00 sigma: `1143.24408` | -1.00 sigma: `1137.09335`
  * +1.28 sigma (80% CI): `1144.10518` | -1.28 sigma: `1136.23225`
  * +2.00 sigma (95% CI): `1146.31945` | -2.00 sigma: `1134.01799`
  * +2.01 sigma: `1146.35020` | -2.01 sigma: `1133.98723`
  * +2.51 sigma (98.8% CI): `1147.88788` | -2.51 sigma: `1132.44955`
  * +3.00 sigma (99.7% CI Extreme): `1149.39481` | -3.00 sigma: `1130.94262`
- **Oscillators & Volatility**:
  * **RSI (14)**: `50.60` | **RSI State**: **`NEUTRAL`**
  * **ATR (14)**: `1.82696` | **ATR %**: `0.16%`
  * **Bollinger Bands**: Upper=`1146.03190` | Mid=`1142.83300` | Lower=`1139.63410` | Bandwidth=`0.56%`
  * **MACD**: Line=`+1.2181` | Signal=`+1.3755` | Hist=`-0.1574`
- **Exponential Moving Average Ribbon (EMA)**:
  * Short Horizon: EMA-5=`1143.35835` | EMA-9=`1143.37949` | EMA-13=`1143.11258` | EMA-20=`1142.49870`
  * Intermediate: EMA-34=`1141.34550` | EMA-50=`1140.38008` | EMA-89=`1139.05546` | EMA-100=`1138.81329`
  * Institutional: EMA-144=`1137.93077` | EMA-200=`1137.08350` (Slope: `+0.068%`) | EMA-233=`1136.74305` (Slope: `+0.061%`)
  * **Trend Bias**: **`NEUTRAL / CHOP`**

---

## 3. Auction Market Structure & Value Profile
*(Sources: 20_Auction_Market_Structure.parquet)*
- **Daily Auction Value Area**:
  * High (VAH): `1142.22000` | Point of Control (POC): `1135.95000` | Low (VAL): `1134.58000`
  * Distance to POC: `+0.45%` | Distance to VAH: `-0.10%` | Distance to VAL: `+0.57%`
  * **Value Area Position**: **`INSIDE_VALUE (Balance)`** | **Auction Regime**: **`ROTATIONAL_BALANCE`** | **Session Bias**: **`BULLISH (Above Pivot)`**
- **Prior Day & Weekly Auction Profile**:
  * Prior Day: PD VAH=`1138.56000` | PD POC=`1136.91000` | PD VAL=`1133.96000` | PDH=`1143.11000` | PDL=`1130.80000` | PDC=`1136.70000`
  * Monday Reference: Monday High=`1136.30000` | Monday Low=`1128.20000` | Monday Mid=`1132.25000`
  * Weekly Value Area: Weekly VAH=`1138.03000` | Weekly POC=`1134.15000` | Weekly VAL=`1130.92000`
  * Multi-Week Extremes: Current Week High (CWH)=`1147.15000` | CWL=`1127.75000` | Prior Week High (PWH)=`1145.55000` | PWL=`1124.35000`
  * Multi-Month Extremes: Current Month High (CMH)=`1147.40000` | CML=`1096.05000` | Prior Month High (PMH)=`1128.65000` | PML=`1089.05000`
- **Session Liquidity Extremes & Initial Balance**:
  * Asian Session: Range `[1134.55000 - 1138.55000]`
  * London Session: Range `[1134.28000 - 1146.45000]`
  * New York Session: Range `[1139.65000 - 1147.15000]`
  * Initial Balance (IB): IB High=`1139.25000` | IB Low=`1137.05000`
- **Fibonacci Golden Pocket & Optimal Trade Entry (OTE)**:
  * Swing Range: High=`1147.15000` | Low=`1134.15000` | Direction=`BULLISH_IMPULSE`
  * Golden Pocket [0.618 - 0.65]: `[1138.70000 - 1139.12000]`
  * Optimal Trade Entry (0.702): `1138.02000` | Invalidation Level: `1136.93000` | Status: **`SHALLOW_RETRACE`**
- **Classical & Weekly Pivots**:
  * Daily Classical: Pivot=`1136.87000` | R1=`1142.94000` | S1=`1130.63000` | R2=`1149.18000` | S2=`1124.56000`
  * Weekly Classical: Weekly Pivot=`1134.05000` | Weekly R1=`1143.75000` | Weekly S1=`1122.55000`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Orderflow
*(Sources: 18_CVD.parquet, 18_CVD_30D_5m.parquet, 18_CVD_30D_15m.parquet, 18_CVD_30D_1h.parquet, 18_CVD_30D_4h.parquet, 18_CVD_30D_ALL.parquet, 21_Tradfye_Orderflow.parquet)*
- **Interbank Spot Orderflow Mechanics**: Decentralized OTC market structure. CVD taker deltas do not apply to interbank spot flow. Tape volume governed by broker tick volume with live spread friction of `2.63 bps`.
- **Session Volume Structure**: Price operating at `INSIDE_VALUE (Balance)` with Daily POC at `1135.95000` (VAH: `1142.22000` / VAL: `1134.58000`).

---

## 5. Institutional Whale Armor & Resting Orderbook Depth
*(Sources: 10_Whale_Orders.parquet, 12_Hyperdash.parquet, 17_Orderbook.parquet, 4_Hyperliquid_Analysis.parquet)*
- **Interbank Institutional Tier-1 Depth**: Decentralized OTC spot liquidity. Resting whale limit walls from crypto venues do not apply.
- **Verified Broker Armor**: Live Bid `1141.10000` / Live Ask `1141.40000` with institutional spread of `2.63 bps`. Structural defense anchored at Asian Range `[1134.55000 - 1138.55000]` and London Range `[1134.28000 - 1146.45000]`.

---

## 6. Liquidation Max Pain, Heatmaps & Cascade Boundaries
*(Sources: 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 14_Hyperdash_Liq_Map.parquet, 14_Liquidation_Matrix.parquet, 15_Hyperdash_Stops_Map.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`351.53000` (Vol: `7,118 USD`, Dist: `+6.57%`) | Long MP=`317.61000` (Vol: `6,590 USD`, Dist: `-3.71%`)
  * 48H Horizon: Short MP=`351.50000` (Vol: `6,363 USD`, Dist: `+6.56%`) | Long MP=`318.25500` (Vol: `6,781 USD`, Dist: `-3.52%`)
  * 3D Horizon: Short MP=`351.50000` (Vol: `6,363 USD`, Dist: `+6.56%`) | Long MP=`318.25500` (Vol: `6,781 USD`, Dist: `-3.52%`)
  * 7D Horizon: Short MP=`340.03000` (Vol: `24,873 USD`, Dist: `+3.39%`) | Long MP=`295.39500` (Vol: `34,574 USD`, Dist: `-10.18%`)
- **Exchange Cumulative Liquidation Cascades (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
  * 1D Cascade: Total=`0.00 USD` | Short Liq Pool=`0.00 USD` | Long Liq Pool=`0.00 USD` | Venues: Binance=`0.00 USD`, OKX=`0.00 USD`, Bybit=`0.00 USD`
  * 7D Cascade: Total=`0.00 USD` | Short Liq Pool=`0.00 USD` | Long Liq Pool=`0.00 USD` | Venues: Binance=`0.00 USD`, OKX=`0.00 USD`, Bybit=`0.00 USD`
- **Cross-Venue Liquidation Matrix & Heatmaps (14_Liquidation_Matrix.parquet, 7_Liq_Heapmap.parquet)**:
  * Liquidation Matrix Strike: Price=`0.00000` | Vol=`0 USD` | Cumulative=`0 USD` | Venue=`-` | Side=`-`
  * Multi-Timeframe Heatmap Density: 1h=`0.00 USD` | 4h=`0.00 USD` | 12h=`0.00 USD` | 24h=`0.00 USD`
- **Hyperdash Real-Time Liquidation & Retail Stop Protection (14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet)**:
  * Hyperdash Liq Cluster: Mark=`0.00 USD` | Cluster Price=`0.00 USD` | Dist=`-` | Cumulative=`0.00 USD` | Short=`0.00 USD` | Long=`0.00 USD` | Size=`-`
- **Live Forced Liquidation Momentum (7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)**:
  * Multi-Timeframe Forced Aggregates (5m): Long Liq=`0.00 USD` | Short Liq=`0.00 USD` | Total=`0.00 USD` | Net Delta=`0.00 USD` | Dominant=`BALANCED`

---

## 7. Derivatives Sentiment, Open Interest & Funding Dynamics
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet, 6_Funding_Fee_Settlement.parquet, 13_Hyperliquid.parquet)*
- **Aggregated Open Interest Breakdown (5_OI.parquet)**:
  * Total Open Interest: `0.00 USD` (`-`) | OI / 24h Volume Ratio: `0.0000`
  * OI Expansion Rate: 1h Change=`+0.00%` | 4h Change=`+0.00%` | 24h Change=`+0.00%`
  * Venue Concentration:
    - Binance: `0.00 USD` | Bybit: `0.00 USD` | OKX: `0.00 USD` | CME Institutional: `0.00 USD`
    - Gate: `0.00 USD` | MEXC: `0.00 USD` | Hyperliquid DEX: `0.00 USD` | Bitget: `0.00 USD`
    - KuCoin: `0.00 USD` | BingX: `0.00 USD` | Bitunix: `0.00 USD` | Others: `0.00 USD`
- **Cross-Exchange Perpetual Funding Rates (5_Funding_Rate.parquet)**:
  * Major CEX Rates: Binance=`+0.0000%` | OKX=`+0.0000%` | Bybit=`+0.0000%` | Bitget=`+0.0000%`
  * Mid-Tier CEX Rates: KuCoin=`+0.0000%` | MEXC=`+0.0000%` | Gate=`+0.0000%` | BingX=`+0.0000%` | Bitunix=`-0.0011%`
  * Alternative Venues: WhiteBIT=`+0.0000%` | LBank=`+0.0000%` | tradeXYZ=`-0.0091%`
  * Inverse Coin-Margined: CoinM Binance=`+0.0000%` | CoinM OKX=`+0.0000%` | CoinM Bybit=`+0.0000%`
- **Exchange Long / Short Ratio Dynamics (3_Exchanges_LS_Ratio*.parquet)**:
  * 15m Tactical: L/S Ratio=`1.00` (Longs: `50.00%`, Shorts: `50.00%`, Total Vol: `0.00 USD`)
  * 1h Primary: L/S Ratio=`1.00` (Longs: `50.00%`, Shorts: `50.00%`, Total Vol: `0.00 USD`)
  * 4h Macro: L/S Ratio=`1.00` (Longs: `50.00%`, Shorts: `50.00%`, Total Vol: `0.00 USD`)
- **Funding Fee Settlement & DEX Arbitrage (6_Funding_Fee_Settlement.parquet, 13_Hyperliquid.parquet)**:
  * Settlement Payouts: Current Expected=`0.00 USD` | Last 24h=`-386.26 USD` | Last 3D=`1.27K USD` | Last 7D=`2.07K USD`

---

## 8. Microstructure Footprint, Tape Imbalances & Macro Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 16_Hyperdash_telegram_Intel.parquet, 19_News.parquet, 19_Calendar.parquet)*
- **Decentralized Spot Flow Profile**: Footprint bar metrics and crypto ETF flows not applicable to OTC spot interbank asset.
- **Institutional Tape Dynamics**: Multi-dealer foreign exchange volume driven by international trade settlements, sovereign reserve reallocation, and London/NY fixing windows.

---

## 9. TradFi & Interbank Market Mechanics
*(Applicable to Foreign Exchange Majors, Precious Metals, Global Equity Indices, and Commodities)*
- **Central Bank Monetary Policy & Rate Differential**:
  * Prevailing Policy Stance: `Federal Reserve (4.75% - 5.00%) Neutral-Gradualist Stance`
  * 2-Year Sovereign Yield Spread Direction & 10-Year Real Yield Momentum.
- **Session Liquidity Overlap & Global Fixing Architecture**:
  * Tokyo Fixing Window (00:55 UTC / 09:55 JST): Commercial export/import flow rebalancing.
  * London Morning Session Open (07:00 - 08:00 UTC): Institutional European bank order routing.
  * London/New York Session Overlap (12:00 - 16:00 UTC): Peak institutional daily volume and tightest interbank raw spreads.
  * WMR Benchmark 4:00 PM London Fix (16:00 UTC): Sovereign wealth and passive pension rebalancing flows.
- **Overnight Rollover & Spread Protection Gate (Strict Execution Invariant)**:
  * New York 5:00 PM Rollover Window (21:15 - 22:30 UTC / 02:45 - 04:00 IST): MANDATORY TRADING HALT.
  * Mandatory spread gate threshold: `25.0 bps`.
- **Economic Calendar Clearance**: Zero high-impact calendar blackout restrictions currently active for this currency pair.

---

## 10. Algorithmic Trade Formulation & Sovereign Decision
- **Sovereign Gate Decision**: **`FAIL_CLOSED_STAND_ASIDE`**
- **Dynamic Capacity Verification**: Active Open=`0` | Resting Pending=`2` | Capacity Check: `N_open + N_pending <= 3` (**`PASS`**)
- **Triple Floor Solvency Check**: Current Equity=`4,744.32 USD` | Hard Floor=`4,775.00 USD` | Buffer=`-30.68 USD` | Solvency Check: **`DEFENSE_MODE`**
- **Stand-Aside Reason**: Absence of statistically validated auction edge and defending resting armor. Standing aside preserves statutory hard floor.