# 🔬 MASTER 43-FEED QUANTITATIVE DOSSIER: COMUSD (COM/USD)
**MT5 Symbol**: `COMUSD.p` | **Category**: `Forex Cross` | **Tier**: `Tier 2`
**Execution Posture**: `DISQUALIFIED` | **Timestamp**: 2026-10-29 14:43:14 UTC
**Pipeline Clearance**: `BLOCKED` | **Data Freshness**: `1.2m`

---

## 1. MT5 Live Broker Telemetry & Spread Friction Gate
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet)*
- **Live Bid Quote**: `21.47000` | **Live Ask Quote**: `21.77000` | **Mid Price**: `21.62000`
- **Spread Points**: `30.0 pts` | **Spread BPS**: `138.76 bps` (Mandatory Cap: `25.0 bps`)
- **Gate Status**: **`FAIL`** (Spread friction 138.76 bps exceeds cap 25.0 bps)
- **Order Allowed**: `NONE` | **Pillar 1 Clearance**: `BLOCKED`
- **Broker Specifications**: Contract Size=`1.00` | Tick Value=`1.00 USD` | Min Lot=`0.01` | Digits=`5`
- **Account Capital Context**: Balance=`4,744.55 USD` | Equity=`4,744.32 USD` | Free Margin=`4,342.62 USD` | Inviolate Hard Floor=`4,775.00 USD` (Cushion: `-30.68 USD`)
- **Pipeline Health**: Feed #00 Status=`PASS` | Overall Pipeline Telemetry=`33/33 FEEDS PASS (SYNCHRONIZED)`

---

## 2. Technical Profile, Multi-Sigma VWAP Dispersion & Volatility
*(Sources: 11_Technical.parquet, 11_Technical_BTC_Ribbon.parquet)*
- **Last Verified Price**: `21.45000` | **24h Change**: `+1.27%` (24h High: `21.70000`, 24h Low: `20.87000`)
- **Weekly Range**: Week High=`22.26000` | Week Low=`20.57000` | Daily POC=`21.39700` | Daily VAH=`21.50580` | Daily VAL=`21.09780`
- **Session VWAP**: `21.22496` | **Rolling 24h VWAP**: `21.27404` | **Distance to VWAP**: `+1.06%`
- **VWAP Z-Score**: `+1.32 sigma` | **Mean Reversion Bias**: **`FAIR VALUE`**
- **VWAP Dispersion Bands**:
  * +1.00 sigma: `21.39585` | -1.00 sigma: `21.05408`
  * +1.28 sigma (80% CI): `21.44370` | -1.28 sigma: `21.00623`
  * +2.00 sigma (95% CI): `21.56673` | -2.00 sigma: `20.88319`
  * +2.01 sigma: `21.56844` | -2.01 sigma: `20.88148`
  * +2.51 sigma (98.8% CI): `21.65388` | -2.51 sigma: `20.79604`
  * +3.00 sigma (99.7% CI Extreme): `21.73762` | -3.00 sigma: `20.71231`
- **Oscillators & Volatility**:
  * **RSI (14)**: `63.51` | **RSI State**: **`BULLISH`**
  * **ATR (14)**: `0.10959` | **ATR %**: `0.51%`
  * **Bollinger Bands**: Upper=`21.54409` | Mid=`21.31850` | Lower=`21.09291` | Bandwidth=`2.12%`
  * **MACD**: Line=`+0.0635` | Signal=`+0.0562` | Hist=`+0.0073`
- **Exponential Moving Average Ribbon (EMA)**:
  * Short Horizon: EMA-5=`21.41280` | EMA-9=`21.39500` | EMA-13=`21.37231` | EMA-20=`21.33651`
  * Intermediate: EMA-34=`21.29597` | EMA-50=`21.27915` | EMA-89=`21.27084` | EMA-100=`21.27084`
  * Institutional: EMA-144=`21.27336` | EMA-200=`21.27876` (Slope: `+0.071%`) | EMA-233=`21.27834` (Slope: `+0.061%`)
  * **Trend Bias**: **`STRONG BULLISH`**

---

## 3. Auction Market Structure & Value Profile
*(Sources: 20_Auction_Market_Structure.parquet)*
- **Daily Auction Value Area**:
  * High (VAH): `21.50580` | Point of Control (POC): `21.39700` | Low (VAL): `21.09780`
  * Distance to POC: `+0.00%` | Distance to VAH: `+0.00%` | Distance to VAL: `+0.00%`
  * **Value Area Position**: **`INSIDE_VALUE (Balance)`** | **Auction Regime**: **`BALANCED_AUCTION`** | **Session Bias**: **`NEUTRAL`**
- **Prior Day & Weekly Auction Profile**:
  * Prior Day: PD VAH=`21.70648` | PD POC=`21.62000` | PD VAL=`21.53352` | PDH=`21.74972` | PDL=`21.49028` | PDC=`21.62000`
  * Monday Reference: Monday High=`21.72810` | Monday Low=`21.51190` | Monday Mid=`21.62000`
  * Weekly Value Area: Weekly VAH=`21.79296` | Weekly POC=`21.62000` | Weekly VAL=`21.44704`
  * Multi-Week Extremes: Current Week High (CWH)=`21.83620` | CWL=`21.40380` | Prior Week High (PWH)=`21.94430` | PWL=`21.29570`
  * Multi-Month Extremes: Current Month High (CMH)=`22.05240` | CML=`21.18760` | Prior Month High (PMH)=`22.16050` | PML=`21.07950`
- **Session Liquidity Extremes & Initial Balance**:
  * Asian Session: Range `[21.57676 - 21.66324]`
  * London Session: Range `[21.53352 - 21.70648]`
  * New York Session: Range `[21.51190 - 21.72810]`
  * Initial Balance (IB): IB High=`21.68486` | IB Low=`21.55514`
- **Fibonacci Golden Pocket & Optimal Trade Entry (OTE)**:
  * Swing Range: High=`21.70000` | Low=`20.87000` | Direction=`NONE`
  * Golden Pocket [0.618 - 0.65]: `[21.57676 - 21.66324]`
  * Optimal Trade Entry (0.702): `21.62000` | Invalidation Level: `0.00000` | Status: **`NONE`**
- **Classical & Weekly Pivots**:
  * Daily Classical: Pivot=`21.62000` | R1=`21.68486` | S1=`21.55514` | R2=`21.74972` | S2=`21.49028`
  * Weekly Classical: Weekly Pivot=`21.62000` | Weekly R1=`21.83620` | Weekly S1=`21.40380`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Orderflow
*(Sources: 18_CVD.parquet, 18_CVD_30D_5m.parquet, 18_CVD_30D_15m.parquet, 18_CVD_30D_1h.parquet, 18_CVD_30D_4h.parquet, 18_CVD_30D_ALL.parquet, 21_Tradfye_Orderflow.parquet)*
- **Interbank Spot Orderflow Mechanics**: Decentralized OTC market structure. CVD taker deltas do not apply to interbank spot flow. Tape volume governed by broker tick volume with live spread friction of `138.76 bps`.
- **Session Volume Structure**: Price operating at `INSIDE_VALUE (Balance)` with Daily POC at `21.39700` (VAH: `21.50580` / VAL: `21.09780`).

---

## 5. Institutional Whale Armor & Resting Orderbook Depth
*(Sources: 10_Whale_Orders.parquet, 12_Hyperdash.parquet, 17_Orderbook.parquet, 4_Hyperliquid_Analysis.parquet)*
- **Interbank Institutional Tier-1 Depth**: Decentralized OTC spot liquidity. Resting whale limit walls from crypto venues do not apply.
- **Verified Broker Armor**: Live Bid `21.47000` / Live Ask `21.77000` with institutional spread of `138.76 bps`. Structural defense anchored at Asian Range `[21.57676 - 21.66324]` and London Range `[21.53352 - 21.70648]`.

---

## 6. Liquidation Max Pain, Heatmaps & Cascade Boundaries
*(Sources: 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 14_Hyperdash_Liq_Map.parquet, 14_Liquidation_Matrix.parquet, 15_Hyperdash_Stops_Map.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **TradFi Structural Liquidity Boundaries**: Centralized perp liquidation feeds do not apply to interbank OTC spot.
- **Stop-Run Cascades & Liquidity Pools**: Primary institutional stop pools reside beyond Classical Pivot extremes (S1: `21.55514` / S2: `21.49028` for long stops; R1: `21.68486` / R2: `21.74972` for short stops) and Asian session extremes `[21.57676 - 21.66324]`.

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
- **Stand-Aside Reason**: Gate 1 Spread Friction Failure: Spread friction 138.76 bps exceeds cap 25.0 bps. Standing aside in 100% cash preserves statutory floor.