# 🔬 MASTER 43-FEED QUANTITATIVE DOSSIER: GAUCNH (GAU/CNH)
**MT5 Symbol**: `GAUCNH.pi` | **Category**: `Forex Exotic` | **Tier**: `Tier 3`
**Execution Posture**: `PASSIVE LIMIT ONLY` | **Timestamp**: 2026-10-29 14:43:14 UTC
**Pipeline Clearance**: `QUALIFIED` | **Data Freshness**: `1.2m`

---

## 1. MT5 Live Broker Telemetry & Spread Friction Gate
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet)*
- **Live Bid Quote**: `860.78800` | **Live Ask Quote**: `861.05900` | **Mid Price**: `860.92350`
- **Spread Points**: `271.0 pts` | **Spread BPS**: `3.15 bps` (Mandatory Cap: `5.0 bps`)
- **Gate Status**: **`PASS`** (Spread friction within mandatory threshold; safe for maker execution)
- **Order Allowed**: `BUY_LIMIT / SELL_LIMIT` | **Pillar 1 Clearance**: `QUALIFIED`
- **Broker Specifications**: Contract Size=`1.00` | Tick Value=`1.00 USD` | Min Lot=`0.01` | Digits=`5`
- **Account Capital Context**: Balance=`4,744.55 USD` | Equity=`4,744.32 USD` | Free Margin=`4,342.62 USD` | Inviolate Hard Floor=`4,775.00 USD` (Cushion: `-30.68 USD`)
- **Pipeline Health**: Feed #00 Status=`PASS` | Overall Pipeline Telemetry=`33/33 FEEDS PASS (SYNCHRONIZED)`

---

## 2. Technical Profile, Multi-Sigma VWAP Dispersion & Volatility
*(Sources: 11_Technical.parquet, 11_Technical_BTC_Ribbon.parquet)*
- **Last Verified Price**: `861.17800` | **24h Change**: `-0.83%` (24h High: `874.17300`, 24h Low: `859.62100`)
- **Weekly Range**: Week High=`874.17300` | Week Low=`854.92700` | Daily POC=`862.13822` | Daily VAH=`864.47982` | Daily VAL=`860.61618`
- **Session VWAP**: `863.38609` | **Rolling 24h VWAP**: `865.00806` | **Distance to VWAP**: `-0.26%`
- **VWAP Z-Score**: `-0.95 sigma` | **Mean Reversion Bias**: **`FAIR VALUE`**
- **VWAP Dispersion Bands**:
  * +1.00 sigma: `865.71207` | -1.00 sigma: `861.06011`
  * +1.28 sigma (80% CI): `866.36335` | -1.28 sigma: `860.40883`
  * +2.00 sigma (95% CI): `868.03806` | -2.00 sigma: `858.73412`
  * +2.01 sigma: `868.06132` | -2.01 sigma: `858.71086`
  * +2.51 sigma (98.8% CI): `869.22431` | -2.51 sigma: `857.54787`
  * +3.00 sigma (99.7% CI Extreme): `870.36404` | -3.00 sigma: `856.40814`
- **Oscillators & Volatility**:
  * **RSI (14)**: `45.30` | **RSI State**: **`NEUTRAL`**
  * **ATR (14)**: `1.92448` | **ATR %**: `0.22%`
  * **Bollinger Bands**: Upper=`863.82145` | Mid=`862.03045` | Lower=`860.23945` | Bandwidth=`0.42%`
  * **MACD**: Line=`-0.5688` | Signal=`-0.5515` | Hist=`-0.0174`
- **Exponential Moving Average Ribbon (EMA)**:
  * Short Horizon: EMA-5=`861.26345` | EMA-9=`861.45708` | EMA-13=`861.62732` | EMA-20=`861.90420`
  * Intermediate: EMA-34=`862.50254` | EMA-50=`863.14492` | EMA-89=`864.16703` | EMA-100=`864.33541`
  * Institutional: EMA-144=`864.49354` | EMA-200=`864.18156` (Slope: `-0.036%`) | EMA-233=`863.95172` (Slope: `-0.028%`)
  * **Trend Bias**: **`STRONG BEARISH`**

---

## 3. Auction Market Structure & Value Profile
*(Sources: 20_Auction_Market_Structure.parquet)*
- **Daily Auction Value Area**:
  * High (VAH): `864.47982` | Point of Control (POC): `862.13822` | Low (VAL): `860.61618`
  * Distance to POC: `+0.00%` | Distance to VAH: `+0.00%` | Distance to VAL: `+0.00%`
  * **Value Area Position**: **`INSIDE_VALUE (Balance)`** | **Auction Regime**: **`BALANCED_AUCTION`** | **Session Bias**: **`NEUTRAL`**
- **Prior Day & Weekly Auction Profile**:
  * Prior Day: PD VAH=`864.36719` | PD POC=`860.92350` | PD VAL=`857.47981` | PDH=`866.08904` | PDL=`855.75796` | PDC=`860.92350`
  * Monday Reference: Monday High=`865.22812` | Monday Low=`856.61888` | Monday Mid=`860.92350`
  * Weekly Value Area: Weekly VAH=`867.81089` | Weekly POC=`860.92350` | Weekly VAL=`854.03611`
  * Multi-Week Extremes: Current Week High (CWH)=`869.53274` | CWL=`852.31426` | Prior Week High (PWH)=`873.83735` | PWL=`848.00965`
  * Multi-Month Extremes: Current Month High (CMH)=`878.14197` | CML=`843.70503` | Prior Month High (PMH)=`882.44659` | PML=`839.40041`
- **Session Liquidity Extremes & Initial Balance**:
  * Asian Session: Range `[859.20165 - 862.64535]`
  * London Session: Range `[857.47981 - 864.36719]`
  * New York Session: Range `[856.61888 - 865.22812]`
  * Initial Balance (IB): IB High=`863.50627` | IB Low=`858.34073`
- **Fibonacci Golden Pocket & Optimal Trade Entry (OTE)**:
  * Swing Range: High=`874.17300` | Low=`859.62100` | Direction=`NONE`
  * Golden Pocket [0.618 - 0.65]: `[859.20165 - 862.64535]`
  * Optimal Trade Entry (0.702): `860.92350` | Invalidation Level: `0.00000` | Status: **`NONE`**
- **Classical & Weekly Pivots**:
  * Daily Classical: Pivot=`860.92350` | R1=`863.50627` | S1=`858.34073` | R2=`866.08904` | S2=`855.75796`
  * Weekly Classical: Weekly Pivot=`860.92350` | Weekly R1=`869.53274` | Weekly S1=`852.31426`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Orderflow
*(Sources: 18_CVD.parquet, 18_CVD_30D_5m.parquet, 18_CVD_30D_15m.parquet, 18_CVD_30D_1h.parquet, 18_CVD_30D_4h.parquet, 18_CVD_30D_ALL.parquet, 21_Tradfye_Orderflow.parquet)*
- **Interbank Spot Orderflow Mechanics**: Decentralized OTC market structure. CVD taker deltas do not apply to interbank spot flow. Tape volume governed by broker tick volume with live spread friction of `3.15 bps`.
- **Session Volume Structure**: Price operating at `INSIDE_VALUE (Balance)` with Daily POC at `862.13822` (VAH: `864.47982` / VAL: `860.61618`).

---

## 5. Institutional Whale Armor & Resting Orderbook Depth
*(Sources: 10_Whale_Orders.parquet, 12_Hyperdash.parquet, 17_Orderbook.parquet, 4_Hyperliquid_Analysis.parquet)*
- **Interbank Institutional Tier-1 Depth**: Decentralized OTC spot liquidity. Resting whale limit walls from crypto venues do not apply.
- **Verified Broker Armor**: Live Bid `860.78800` / Live Ask `861.05900` with institutional spread of `3.15 bps`. Structural defense anchored at Asian Range `[859.20165 - 862.64535]` and London Range `[857.47981 - 864.36719]`.

---

## 6. Liquidation Max Pain, Heatmaps & Cascade Boundaries
*(Sources: 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 14_Hyperdash_Liq_Map.parquet, 14_Liquidation_Matrix.parquet, 15_Hyperdash_Stops_Map.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **TradFi Structural Liquidity Boundaries**: Centralized perp liquidation feeds do not apply to interbank OTC spot.
- **Stop-Run Cascades & Liquidity Pools**: Primary institutional stop pools reside beyond Classical Pivot extremes (S1: `858.34073` / S2: `855.75796` for long stops; R1: `863.50627` / R2: `866.08904` for short stops) and Asian session extremes `[859.20165 - 862.64535]`.

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
- **Economic Calendar Clearance**: Zero high-impact calendar blackout restrictions currently active for this currency pair.

---

## 10. Algorithmic Trade Formulation & Sovereign Decision
- **Sovereign Gate Decision**: **`FAIL_CLOSED_STAND_ASIDE`**
- **Dynamic Capacity Verification**: Active Open=`0` | Resting Pending=`2` | Capacity Check: `N_open + N_pending <= 3` (**`PASS`**)
- **Triple Floor Solvency Check**: Current Equity=`4,744.32 USD` | Hard Floor=`4,775.00 USD` | Buffer=`-30.68 USD` | Solvency Check: **`DEFENSE_MODE`**
- **Stand-Aside Reason**: Absence of statistically validated auction edge and defending resting armor. Standing aside preserves statutory hard floor.