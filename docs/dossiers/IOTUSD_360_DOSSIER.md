# 🔬 MASTER 43-FEED QUANTITATIVE DOSSIER: IOTUSD (IOT/USD)
**MT5 Symbol**: `IOTUSD.p` | **Category**: `Forex Cross` | **Tier**: `Tier 2`
**Execution Posture**: `DISQUALIFIED` | **Timestamp**: 2026-10-29 14:43:14 UTC
**Pipeline Clearance**: `BLOCKED` | **Data Freshness**: `1.2m`

---

## 1. MT5 Live Broker Telemetry & Spread Friction Gate
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet)*
- **Live Bid Quote**: `0.03940` | **Live Ask Quote**: `0.04170` | **Mid Price**: `0.04055`
- **Spread Points**: `23.0 pts` | **Spread BPS**: `567.20 bps` (Mandatory Cap: `25.0 bps`)
- **Gate Status**: **`FAIL`** (Spread friction 567.20 bps exceeds cap 25.0 bps)
- **Order Allowed**: `NONE` | **Pillar 1 Clearance**: `BLOCKED`
- **Broker Specifications**: Contract Size=`1.00` | Tick Value=`1.00 USD` | Min Lot=`0.01` | Digits=`5`
- **Account Capital Context**: Balance=`4,744.55 USD` | Equity=`4,744.32 USD` | Free Margin=`4,342.62 USD` | Inviolate Hard Floor=`4,775.00 USD` (Cushion: `-30.68 USD`)
- **Pipeline Health**: Feed #00 Status=`PASS` | Overall Pipeline Telemetry=`33/33 FEEDS PASS (SYNCHRONIZED)`

---

## 2. Technical Profile, Multi-Sigma VWAP Dispersion & Volatility
*(Sources: 11_Technical.parquet, 11_Technical_BTC_Ribbon.parquet)*
- **Last Verified Price**: `0.03940` | **24h Change**: `-1.75%` (24h High: `0.04170`, 24h Low: `0.03850`)
- **Weekly Range**: Week High=`0.04210` | Week Low=`0.03850` | Daily POC=`0.03879` | Daily VAH=`0.03927` | Daily VAL=`0.03859`
- **Session VWAP**: `0.03911` | **Rolling 24h VWAP**: `0.03971` | **Distance to VWAP**: `+0.75%`
- **VWAP Z-Score**: `+0.69 sigma` | **Mean Reversion Bias**: **`FAIR VALUE`**
- **VWAP Dispersion Bands**:
  * +1.00 sigma: `0.03953` | -1.00 sigma: `0.03868`
  * +1.28 sigma (80% CI): `0.03965` | -1.28 sigma: `0.03857`
  * +2.00 sigma (95% CI): `0.03995` | -2.00 sigma: `0.03826`
  * +2.01 sigma: `0.03996` | -2.01 sigma: `0.03826`
  * +2.51 sigma (98.8% CI): `0.04017` | -2.51 sigma: `0.03804`
  * +3.00 sigma (99.7% CI Extreme): `0.04038` | -3.00 sigma: `0.03784`
- **Oscillators & Volatility**:
  * **RSI (14)**: `63.15` | **RSI State**: **`BULLISH`**
  * **ATR (14)**: `0.00020` | **ATR %**: `0.51%`
  * **Bollinger Bands**: Upper=`0.03947` | Mid=`0.03911` | Lower=`0.03875` | Bandwidth=`1.83%`
  * **MACD**: Line=`+0.0001` | Signal=`+0.0000` | Hist=`+0.0000`
- **Exponential Moving Average Ribbon (EMA)**:
  * Short Horizon: EMA-5=`0.03931` | EMA-9=`0.03925` | EMA-13=`0.03921` | EMA-20=`0.03915`
  * Intermediate: EMA-34=`0.03915` | EMA-50=`0.03925` | EMA-89=`0.03955` | EMA-100=`0.03963`
  * Institutional: EMA-144=`0.03989` | EMA-200=`0.04011` (Slope: `-0.288%`) | EMA-233=`0.04025` (Slope: `-0.280%`)
  * **Trend Bias**: **`NEUTRAL / CHOP`**

---

## 3. Auction Market Structure & Value Profile
*(Sources: 20_Auction_Market_Structure.parquet)*
- **Daily Auction Value Area**:
  * High (VAH): `0.03927` | Point of Control (POC): `0.03879` | Low (VAL): `0.03859`
  * Distance to POC: `+0.00%` | Distance to VAH: `+0.00%` | Distance to VAL: `+0.00%`
  * **Value Area Position**: **`INSIDE_VALUE (Balance)`** | **Auction Regime**: **`BALANCED_AUCTION`** | **Session Bias**: **`NEUTRAL`**
- **Prior Day & Weekly Auction Profile**:
  * Prior Day: PD VAH=`0.04071` | PD POC=`0.04055` | PD VAL=`0.04039` | PDH=`0.04079` | PDL=`0.04031` | PDC=`0.04055`
  * Monday Reference: Monday High=`0.04075` | Monday Low=`0.04035` | Monday Mid=`0.04055`
  * Weekly Value Area: Weekly VAH=`0.04087` | Weekly POC=`0.04055` | Weekly VAL=`0.04023`
  * Multi-Week Extremes: Current Week High (CWH)=`0.04096` | CWL=`0.04014` | Prior Week High (PWH)=`0.04116` | PWL=`0.03994`
  * Multi-Month Extremes: Current Month High (CMH)=`0.04136` | CML=`0.03974` | Prior Month High (PMH)=`0.04156` | PML=`0.03954`
- **Session Liquidity Extremes & Initial Balance**:
  * Asian Session: Range `[0.04047 - 0.04063]`
  * London Session: Range `[0.04039 - 0.04071]`
  * New York Session: Range `[0.04035 - 0.04075]`
  * Initial Balance (IB): IB High=`0.04067` | IB Low=`0.04043`
- **Fibonacci Golden Pocket & Optimal Trade Entry (OTE)**:
  * Swing Range: High=`0.04170` | Low=`0.03850` | Direction=`NONE`
  * Golden Pocket [0.618 - 0.65]: `[0.04047 - 0.04063]`
  * Optimal Trade Entry (0.702): `0.04055` | Invalidation Level: `0.00000` | Status: **`NONE`**
- **Classical & Weekly Pivots**:
  * Daily Classical: Pivot=`0.04055` | R1=`0.04067` | S1=`0.04043` | R2=`0.04079` | S2=`0.04031`
  * Weekly Classical: Weekly Pivot=`0.04055` | Weekly R1=`0.04096` | Weekly S1=`0.04014`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Orderflow
*(Sources: 18_CVD.parquet, 18_CVD_30D_5m.parquet, 18_CVD_30D_15m.parquet, 18_CVD_30D_1h.parquet, 18_CVD_30D_4h.parquet, 18_CVD_30D_ALL.parquet, 21_Tradfye_Orderflow.parquet)*
- **Interbank Spot Orderflow Mechanics**: Decentralized OTC market structure. CVD taker deltas do not apply to interbank spot flow. Tape volume governed by broker tick volume with live spread friction of `567.20 bps`.
- **Session Volume Structure**: Price operating at `INSIDE_VALUE (Balance)` with Daily POC at `0.03879` (VAH: `0.03927` / VAL: `0.03859`).

---

## 5. Institutional Whale Armor & Resting Orderbook Depth
*(Sources: 10_Whale_Orders.parquet, 12_Hyperdash.parquet, 17_Orderbook.parquet, 4_Hyperliquid_Analysis.parquet)*
- **Interbank Institutional Tier-1 Depth**: Decentralized OTC spot liquidity. Resting whale limit walls from crypto venues do not apply.
- **Verified Broker Armor**: Live Bid `0.03940` / Live Ask `0.04170` with institutional spread of `567.20 bps`. Structural defense anchored at Asian Range `[0.04047 - 0.04063]` and London Range `[0.04039 - 0.04071]`.

---

## 6. Liquidation Max Pain, Heatmaps & Cascade Boundaries
*(Sources: 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 14_Hyperdash_Liq_Map.parquet, 14_Liquidation_Matrix.parquet, 15_Hyperdash_Stops_Map.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **TradFi Structural Liquidity Boundaries**: Centralized perp liquidation feeds do not apply to interbank OTC spot.
- **Stop-Run Cascades & Liquidity Pools**: Primary institutional stop pools reside beyond Classical Pivot extremes (S1: `0.04043` / S2: `0.04031` for long stops; R1: `0.04067` / R2: `0.04079` for short stops) and Asian session extremes `[0.04047 - 0.04063]`.

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
  * Mandatory spread gate threshold: `25.0 bps`.
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
- **Stand-Aside Reason**: Gate 1 Spread Friction Failure: Spread friction 567.20 bps exceeds cap 25.0 bps. Standing aside in 100% cash preserves statutory floor.