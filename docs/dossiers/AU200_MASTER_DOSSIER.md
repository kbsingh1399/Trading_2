# 🔬 MASTER 43-FEED QUANTITATIVE DOSSIER: AU200 (ASX 200 Index)
**MT5 Symbol**: `AU200.p` | **Category**: `Equity Index` | **Tier**: `Tier 2`
**Execution Posture**: `PASSIVE LIMIT ONLY` | **Timestamp**: 2026-10-29 14:43:14 UTC
**Pipeline Clearance**: `QUALIFIED` | **Data Freshness**: `1.2m`

---

## 1. MT5 Live Broker Telemetry & Spread Friction Gate
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet)*
- **Live Bid Quote**: `8923.65000` | **Live Ask Quote**: `8924.75000` | **Mid Price**: `8924.20000`
- **Spread Points**: `110.0 pts` | **Spread BPS**: `1.23 bps` (Mandatory Cap: `5.0 bps`)
- **Gate Status**: **`PASS`** (Spread friction within mandatory threshold; safe for maker execution)
- **Order Allowed**: `BUY_LIMIT / SELL_LIMIT` | **Pillar 1 Clearance**: `QUALIFIED`
- **Broker Specifications**: Contract Size=`1.00` | Tick Value=`1.00 USD` | Min Lot=`0.01` | Digits=`5`
- **Account Capital Context**: Balance=`4,744.55 USD` | Equity=`4,744.32 USD` | Free Margin=`4,342.62 USD` | Inviolate Hard Floor=`4,775.00 USD` (Cushion: `-30.68 USD`)
- **Pipeline Health**: Feed #00 Status=`PASS` | Overall Pipeline Telemetry=`33/33 FEEDS PASS (SYNCHRONIZED)`

---

## 2. Technical Profile, Multi-Sigma VWAP Dispersion & Volatility
*(Sources: 11_Technical.parquet, 11_Technical_BTC_Ribbon.parquet)*
- **Last Verified Price**: `8934.05000` | **24h Change**: `+0.82%` (24h High: `8946.45000`, 24h Low: `8852.75000`)
- **Weekly Range**: Week High=`8946.45000` | Week Low=`8755.35000` | Daily POC=`8886.90000` | Daily VAH=`8921.24000` | Daily VAL=`8878.59000`
- **Session VWAP**: `8904.00483` | **Rolling 24h VWAP**: `8888.82423` | **Distance to VWAP**: `+0.34%`
- **VWAP Z-Score**: `+1.59 sigma` | **Mean Reversion Bias**: **`OVERBOUGHT`**
- **VWAP Dispersion Bands**:
  * +1.00 sigma: `8922.93306` | -1.00 sigma: `8885.07660`
  * +1.28 sigma (80% CI): `8928.23296` | -1.28 sigma: `8879.77670`
  * +2.00 sigma (95% CI): `8941.86128` | -2.00 sigma: `8866.14838`
  * +2.01 sigma: `8942.05057` | -2.01 sigma: `8865.95910`
  * +2.51 sigma (98.8% CI): `8951.51468` | -2.51 sigma: `8856.49498`
  * +3.00 sigma (99.7% CI Extreme): `8960.78951` | -3.00 sigma: `8847.22015`
- **Oscillators & Volatility**:
  * **RSI (14)**: `65.80` | **RSI State**: **`BULLISH`**
  * **ATR (14)**: `10.84710` | **ATR %**: `0.12%`
  * **Bollinger Bands**: Upper=`8938.24559` | Mid=`8916.69000` | Lower=`8895.13441` | Bandwidth=`0.48%`
  * **MACD**: Line=`+8.3575` | Signal=`+6.4854` | Hist=`+1.8721`
- **Exponential Moving Average Ribbon (EMA)**:
  * Short Horizon: EMA-5=`8929.43818` | EMA-9=`8924.52124` | EMA-13=`8921.11969` | EMA-20=`8916.68049`
  * Intermediate: EMA-34=`8909.84357` | EMA-50=`8903.79060` | EMA-89=`8893.10065` | EMA-100=`8890.55862`
  * Institutional: EMA-144=`8881.11450` | EMA-200=`8869.67630` (Slope: `+0.069%`) | EMA-233=`8863.62572` (Slope: `+0.066%`)
  * **Trend Bias**: **`STRONG BULLISH`**

---

## 3. Auction Market Structure & Value Profile
*(Sources: 20_Auction_Market_Structure.parquet)*
- **Daily Auction Value Area**:
  * High (VAH): `8921.24000` | Point of Control (POC): `8886.90000` | Low (VAL): `8878.59000`
  * Distance to POC: `+0.41%` | Distance to VAH: `+0.03%` | Distance to VAL: `+0.51%`
  * **Value Area Position**: **`ABOVE_VALUE (Imbalance)`** | **Auction Regime**: **`RANGE_EXPANSION`** | **Session Bias**: **`BULLISH (Above Pivot)`**
- **Prior Day & Weekly Auction Profile**:
  * Prior Day: PD VAH=`8882.52000` | PD POC=`8875.31000` | PD VAL=`8857.62000` | PDH=`8938.55000` | PDL=`8840.25000` | PDC=`8876.25000`
  * Monday Reference: Monday High=`8838.60000` | Monday Low=`8715.35000` | Monday Mid=`8776.98000`
  * Weekly Value Area: Weekly VAH=`8919.49000` | Weekly POC=`8877.89000` | Weekly VAL=`8816.26000`
  * Multi-Week Extremes: Current Week High (CWH)=`8946.45000` | CWL=`8715.35000` | Prior Week High (PWH)=`8876.45000` | PWL=`8701.15000`
  * Multi-Month Extremes: Current Month High (CMH)=`8946.45000` | CML=`8526.00000` | Prior Month High (PMH)=`9072.00000` | PML=`8596.90000`
- **Session Liquidity Extremes & Initial Balance**:
  * Asian Session: Range `[8863.35000 - 8903.25000]`
  * London Session: Range `[8883.40000 - 8931.95000]`
  * New York Session: Range `[8894.65000 - 8946.45000]`
  * Initial Balance (IB): IB High=`8899.45000` | IB Low=`8886.45000`
- **Fibonacci Golden Pocket & Optimal Trade Entry (OTE)**:
  * Swing Range: High=`8946.45000` | Low=`8852.75000` | Direction=`BULLISH_IMPULSE`
  * Golden Pocket [0.618 - 0.65]: `[8885.55000 - 8888.54000]`
  * Optimal Trade Entry (0.702): `8880.67000` | Invalidation Level: `8872.80000` | Status: **`SHALLOW_RETRACE`**
- **Classical & Weekly Pivots**:
  * Daily Classical: Pivot=`8885.02000` | R1=`8929.78000` | S1=`8831.48000` | R2=`8983.32000` | S2=`8786.72000`
  * Weekly Classical: Weekly Pivot=`8773.08000` | Weekly R1=`8845.02000` | Weekly S1=`8669.72000`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Orderflow
*(Sources: 18_CVD.parquet, 18_CVD_30D_5m.parquet, 18_CVD_30D_15m.parquet, 18_CVD_30D_1h.parquet, 18_CVD_30D_4h.parquet, 18_CVD_30D_ALL.parquet, 21_Tradfye_Orderflow.parquet)*
- **Interbank Spot Orderflow Mechanics**: Decentralized OTC market structure. CVD taker deltas do not apply to interbank spot flow. Tape volume governed by broker tick volume with live spread friction of `1.23 bps`.
- **Session Volume Structure**: Price operating at `ABOVE_VALUE (Imbalance)` with Daily POC at `8886.90000` (VAH: `8921.24000` / VAL: `8878.59000`).

---

## 5. Institutional Whale Armor & Resting Orderbook Depth
*(Sources: 10_Whale_Orders.parquet, 12_Hyperdash.parquet, 17_Orderbook.parquet, 4_Hyperliquid_Analysis.parquet)*
- **Interbank Institutional Tier-1 Depth**: Decentralized OTC spot liquidity. Resting whale limit walls from crypto venues do not apply.
- **Verified Broker Armor**: Live Bid `8923.65000` / Live Ask `8924.75000` with institutional spread of `1.23 bps`. Structural defense anchored at Asian Range `[8863.35000 - 8903.25000]` and London Range `[8883.40000 - 8931.95000]`.

---

## 6. Liquidation Max Pain, Heatmaps & Cascade Boundaries
*(Sources: 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 14_Hyperdash_Liq_Map.parquet, 14_Liquidation_Matrix.parquet, 15_Hyperdash_Stops_Map.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **TradFi Structural Liquidity Boundaries**: Centralized perp liquidation feeds do not apply to interbank OTC spot.
- **Stop-Run Cascades & Liquidity Pools**: Primary institutional stop pools reside beyond Classical Pivot extremes (S1: `8831.48000` / S2: `8786.72000` for long stops; R1: `8929.78000` / R2: `8983.32000` for short stops) and Asian session extremes `[8863.35000 - 8903.25000]`.

---

## 7. Derivatives Sentiment, Open Interest & Funding Dynamics
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet, 6_Funding_Fee_Settlement.parquet, 13_Hyperliquid.parquet)*
- **Interbank Financing & Carry Mechanics**: Instrument trades as an OTC spot / cash CFD with zero perpetual funding drag or basis settlement friction.
- **Monetary Policy Differential**: Overnight holding carry governed by central bank interest rate spreads and broker rollover swap schedules.

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
  * Mandatory spread gate threshold: `5.0 bps`.
- **Upcoming High-Impact Economic Calendar Events (19_Calendar.parquet)**:
  * `Tue Oct 27 5:45pm` [USD - Low Impact]: ADP Weekly Employment Change (Forecast: , Previous: 17.5K)
  * `Tue Oct 27 6:00pm` [USD - Low Impact]: Core Durable Goods Orders m/m (Forecast: 0.6%, Previous: 0.2%)
  * `Tue Oct 27 6:00pm` [USD - Low Impact]: Durable Goods Orders m/m (Forecast: 2.0%, Previous: -0.1%)
- **Real-Time Macro Catalysts & Headlines (19_News.parquet)**:
  * `1 hr 20 min ago` [Inflation & CPI]: Fed's Favorite Inflation Indicator Surges In September As Soaring Energy Costs Drags Americans' Savings Rate To 4-Year Lows (zerohedge.com)
  * `1 hr 50 min ago` [Labor & Employment]: US Unemployment Insurance Weekly Claims (dol.gov)
  * `1 hr 50 min ago` [General Market Intel]: US Personal Income and Outlays, September 2026 (bea.gov)

---

## 10. Algorithmic Trade Formulation & Sovereign Decision
- **Sovereign Gate Decision**: **`FAIL_CLOSED_STAND_ASIDE`**
- **Dynamic Capacity Verification**: Active Open=`0` | Resting Pending=`2` | Capacity Check: `N_open + N_pending <= 3` (**`PASS`**)
- **Triple Floor Solvency Check**: Current Equity=`4,744.32 USD` | Hard Floor=`4,775.00 USD` | Buffer=`-30.68 USD` | Solvency Check: **`DEFENSE_MODE`**
- **Stand-Aside Reason**: Absence of statistically validated auction edge and defending resting armor. Standing aside preserves statutory hard floor.