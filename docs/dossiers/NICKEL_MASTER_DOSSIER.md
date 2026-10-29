# 🔬 MASTER 43-FEED QUANTITATIVE DOSSIER: NICKEL (Nickel)
**MT5 Symbol**: `NICKEL.p` | **Category**: `Base Metal` | **Tier**: `Tier 2`
**Execution Posture**: `DISQUALIFIED` | **Timestamp**: 2026-10-29 14:43:14 UTC
**Pipeline Clearance**: `BLOCKED` | **Data Freshness**: `1.2m`

---

## 1. MT5 Live Broker Telemetry & Spread Friction Gate
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet)*
- **Live Bid Quote**: `15478.28000` | **Live Ask Quote**: `15496.22000` | **Mid Price**: `15487.25000`
- **Spread Points**: `17940.0 pts` | **Spread BPS**: `11.58 bps` (Mandatory Cap: `5.0 bps`)
- **Gate Status**: **`FAIL`** (Spread friction 11.58 bps exceeds cap 5.0 bps)
- **Order Allowed**: `NONE` | **Pillar 1 Clearance**: `BLOCKED`
- **Broker Specifications**: Contract Size=`1.00` | Tick Value=`1.00 USD` | Min Lot=`0.01` | Digits=`5`
- **Account Capital Context**: Balance=`4,744.55 USD` | Equity=`4,744.32 USD` | Free Margin=`4,342.62 USD` | Inviolate Hard Floor=`4,775.00 USD` (Cushion: `-30.68 USD`)
- **Pipeline Health**: Feed #00 Status=`PASS` | Overall Pipeline Telemetry=`33/33 FEEDS PASS (SYNCHRONIZED)`

---

## 2. Technical Profile, Multi-Sigma VWAP Dispersion & Volatility
*(Sources: 11_Technical.parquet, 11_Technical_BTC_Ribbon.parquet)*
- **Last Verified Price**: `15498.53000` | **24h Change**: `-1.31%` (24h High: `15830.03000`, 24h Low: `15468.53000`)
- **Weekly Range**: Week High=`15923.53000` | Week Low=`15430.28000` | Daily POC=`15678.74000` | Daily VAH=`15753.10000` | Daily VAL=`15592.94000`
- **Session VWAP**: `15638.58387` | **Rolling 24h VWAP**: `15658.10845` | **Distance to VWAP**: `-0.90%`
- **VWAP Z-Score**: `-2.09 sigma` | **Mean Reversion Bias**: **`EXTREME OVERSOLD`**
- **VWAP Dispersion Bands**:
  * +1.00 sigma: `15705.67975` | -1.00 sigma: `15571.48798`
  * +1.28 sigma (80% CI): `15724.46660` | -1.28 sigma: `15552.70113`
  * +2.00 sigma (95% CI): `15772.77564` | -2.00 sigma: `15504.39210`
  * +2.01 sigma: `15773.44660` | -2.01 sigma: `15503.72114`
  * +2.51 sigma (98.8% CI): `15806.99454` | -2.51 sigma: `15470.17320`
  * +3.00 sigma (99.7% CI Extreme): `15839.87153` | -3.00 sigma: `15437.29621`
- **Oscillators & Volatility**:
  * **RSI (14)**: `32.06` | **RSI State**: **`BEARISH`**
  * **ATR (14)**: `36.72682` | **ATR %**: `0.24%`
  * **Bollinger Bands**: Upper=`15627.91747` | Mid=`15569.29250` | Lower=`15510.66753` | Bandwidth=`0.75%`
  * **MACD**: Line=`-31.0002` | Signal=`-25.2790` | Hist=`-5.7212`
- **Exponential Moving Average Ribbon (EMA)**:
  * Short Horizon: EMA-5=`15526.46298` | EMA-9=`15543.90147` | EMA-13=`15555.89428` | EMA-20=`15572.52996`
  * Intermediate: EMA-34=`15596.63190` | EMA-50=`15613.96307` | EMA-89=`15633.94660` | EMA-100=`15637.39897`
  * Institutional: EMA-144=`15649.23808` | EMA-200=`15663.71026` (Slope: `-0.084%`) | EMA-233=`15663.93058` (Slope: `-0.072%`)
  * **Trend Bias**: **`STRONG BEARISH`**

---

## 3. Auction Market Structure & Value Profile
*(Sources: 20_Auction_Market_Structure.parquet)*
- **Daily Auction Value Area**:
  * High (VAH): `15753.10000` | Point of Control (POC): `15678.74000` | Low (VAL): `15592.94000`
  * Distance to POC: `+0.00%` | Distance to VAH: `+0.00%` | Distance to VAL: `+0.00%`
  * **Value Area Position**: **`INSIDE_VALUE (Balance)`** | **Auction Regime**: **`BALANCED_AUCTION`** | **Session Bias**: **`NEUTRAL`**
- **Prior Day & Weekly Auction Profile**:
  * Prior Day: PD VAH=`15549.19900` | PD POC=`15487.25000` | PD VAL=`15425.30100` | PDH=`15580.17350` | PDL=`15394.32650` | PDC=`15487.25000`
  * Monday Reference: Monday High=`15564.68625` | Monday Low=`15409.81375` | Monday Mid=`15487.25000`
  * Weekly Value Area: Weekly VAH=`15611.14800` | Weekly POC=`15487.25000` | Weekly VAL=`15363.35200`
  * Multi-Week Extremes: Current Week High (CWH)=`15642.12250` | CWL=`15332.37750` | Prior Week High (PWH)=`15719.55875` | PWL=`15254.94125`
  * Multi-Month Extremes: Current Month High (CMH)=`15796.99500` | CML=`15177.50500` | Prior Month High (PMH)=`15874.43125` | PML=`15100.06875`
- **Session Liquidity Extremes & Initial Balance**:
  * Asian Session: Range `[15456.27550 - 15518.22450]`
  * London Session: Range `[15425.30100 - 15549.19900]`
  * New York Session: Range `[15409.81375 - 15564.68625]`
  * Initial Balance (IB): IB High=`15533.71175` | IB Low=`15440.78825`
- **Fibonacci Golden Pocket & Optimal Trade Entry (OTE)**:
  * Swing Range: High=`15830.03000` | Low=`15468.53000` | Direction=`NONE`
  * Golden Pocket [0.618 - 0.65]: `[15456.27550 - 15518.22450]`
  * Optimal Trade Entry (0.702): `15487.25000` | Invalidation Level: `0.00000` | Status: **`NONE`**
- **Classical & Weekly Pivots**:
  * Daily Classical: Pivot=`15487.25000` | R1=`15533.71175` | S1=`15440.78825` | R2=`15580.17350` | S2=`15394.32650`
  * Weekly Classical: Weekly Pivot=`15487.25000` | Weekly R1=`15642.12250` | Weekly S1=`15332.37750`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Orderflow
*(Sources: 18_CVD.parquet, 18_CVD_30D_5m.parquet, 18_CVD_30D_15m.parquet, 18_CVD_30D_1h.parquet, 18_CVD_30D_4h.parquet, 18_CVD_30D_ALL.parquet, 21_Tradfye_Orderflow.parquet)*
- **Interbank Spot Orderflow Mechanics**: Decentralized OTC market structure. CVD taker deltas do not apply to interbank spot flow. Tape volume governed by broker tick volume with live spread friction of `11.58 bps`.
- **Session Volume Structure**: Price operating at `INSIDE_VALUE (Balance)` with Daily POC at `15678.74000` (VAH: `15753.10000` / VAL: `15592.94000`).

---

## 5. Institutional Whale Armor & Resting Orderbook Depth
*(Sources: 10_Whale_Orders.parquet, 12_Hyperdash.parquet, 17_Orderbook.parquet, 4_Hyperliquid_Analysis.parquet)*
- **Interbank Institutional Tier-1 Depth**: Decentralized OTC spot liquidity. Resting whale limit walls from crypto venues do not apply.
- **Verified Broker Armor**: Live Bid `15478.28000` / Live Ask `15496.22000` with institutional spread of `11.58 bps`. Structural defense anchored at Asian Range `[15456.27550 - 15518.22450]` and London Range `[15425.30100 - 15549.19900]`.

---

## 6. Liquidation Max Pain, Heatmaps & Cascade Boundaries
*(Sources: 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 14_Hyperdash_Liq_Map.parquet, 14_Liquidation_Matrix.parquet, 15_Hyperdash_Stops_Map.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **TradFi Structural Liquidity Boundaries**: Centralized perp liquidation feeds do not apply to interbank OTC spot.
- **Stop-Run Cascades & Liquidity Pools**: Primary institutional stop pools reside beyond Classical Pivot extremes (S1: `15440.78825` / S2: `15394.32650` for long stops; R1: `15533.71175` / R2: `15580.17350` for short stops) and Asian session extremes `[15456.27550 - 15518.22450]`.

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
- **Stand-Aside Reason**: Gate 1 Spread Friction Failure: Spread friction 11.58 bps exceeds cap 5.0 bps. Standing aside in 100% cash preserves statutory floor.