# 🔬 MASTER 43-FEED QUANTITATIVE DOSSIER: FLWUSD (FLW/USD)
**MT5 Symbol**: `FLWUSD.p` | **Category**: `Forex Cross` | **Tier**: `Tier 2`
**Execution Posture**: `DISQUALIFIED` | **Timestamp**: 2026-10-29 14:43:14 UTC
**Pipeline Clearance**: `BLOCKED` | **Data Freshness**: `1.2m`

---

## 1. MT5 Live Broker Telemetry & Spread Friction Gate
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet)*
- **Live Bid Quote**: `0.01600` | **Live Ask Quote**: `0.03600` | **Mid Price**: `0.02600`
- **Spread Points**: `20.0 pts` | **Spread BPS**: `7692.31 bps` (Mandatory Cap: `25.0 bps`)
- **Gate Status**: **`FAIL`** (Spread friction 7692.31 bps exceeds cap 25.0 bps)
- **Order Allowed**: `NONE` | **Pillar 1 Clearance**: `BLOCKED`
- **Broker Specifications**: Contract Size=`1.00` | Tick Value=`1.00 USD` | Min Lot=`0.01` | Digits=`5`
- **Account Capital Context**: Balance=`4,744.55 USD` | Equity=`4,744.32 USD` | Free Margin=`4,342.62 USD` | Inviolate Hard Floor=`4,775.00 USD` (Cushion: `-30.68 USD`)
- **Pipeline Health**: Feed #00 Status=`PASS` | Overall Pipeline Telemetry=`33/33 FEEDS PASS (SYNCHRONIZED)`

---

## 2. Technical Profile, Multi-Sigma VWAP Dispersion & Volatility
*(Sources: 11_Technical.parquet, 11_Technical_BTC_Ribbon.parquet)*
- **Last Verified Price**: `0.01600` | **24h Change**: `+0.00%` (24h High: `0.01700`, 24h Low: `0.01500`)
- **Weekly Range**: Week High=`0.01700` | Week Low=`0.01500` | Daily POC=`0.01500` | Daily VAH=`0.01575` | Daily VAL=`0.01500`
- **Session VWAP**: `0.01537` | **Rolling 24h VWAP**: `0.01563` | **Distance to VWAP**: `+4.09%`
- **VWAP Z-Score**: `+1.61 sigma` | **Mean Reversion Bias**: **`OVERBOUGHT`**
- **VWAP Dispersion Bands**:
  * +1.00 sigma: `0.01576` | -1.00 sigma: `0.01498`
  * +1.28 sigma (80% CI): `0.01587` | -1.28 sigma: `0.01487`
  * +2.00 sigma (95% CI): `0.01615` | -2.00 sigma: `0.01459`
  * +2.01 sigma: `0.01616` | -2.01 sigma: `0.01458`
  * +2.51 sigma (98.8% CI): `0.01635` | -2.51 sigma: `0.01439`
  * +3.00 sigma (99.7% CI Extreme): `0.01655` | -3.00 sigma: `0.01420`
- **Oscillators & Volatility**:
  * **RSI (14)**: `82.31` | **RSI State**: **`OVERBOUGHT`**
  * **ATR (14)**: `0.00033` | **ATR %**: `2.09%`
  * **Bollinger Bands**: Upper=`0.01622` | Mid=`0.01530` | Lower=`0.01438` | Bandwidth=`11.98%`
  * **MACD**: Line=`+0.0002` | Signal=`+0.0001` | Hist=`+0.0001`
- **Exponential Moving Average Ribbon (EMA)**:
  * Short Horizon: EMA-5=`0.01591` | EMA-9=`0.01574` | EMA-13=`0.01561` | EMA-20=`0.01547`
  * Intermediate: EMA-34=`0.01539` | EMA-50=`0.01541` | EMA-89=`0.01553` | EMA-100=`0.01557`
  * Institutional: EMA-144=`0.01567` | EMA-200=`0.01575` (Slope: `-0.187%`) | EMA-233=`0.01579` (Slope: `-0.190%`)
  * **Trend Bias**: **`BULLISH`**

---

## 3. Auction Market Structure & Value Profile
*(Sources: 20_Auction_Market_Structure.parquet)*
- **Daily Auction Value Area**:
  * High (VAH): `0.01575` | Point of Control (POC): `0.01500` | Low (VAL): `0.01500`
  * Distance to POC: `+0.00%` | Distance to VAH: `+0.00%` | Distance to VAL: `+0.00%`
  * **Value Area Position**: **`INSIDE_VALUE (Balance)`** | **Auction Regime**: **`BALANCED_AUCTION`** | **Session Bias**: **`NEUTRAL`**
- **Prior Day & Weekly Auction Profile**:
  * Prior Day: PD VAH=`0.02610` | PD POC=`0.02600` | PD VAL=`0.02590` | PDH=`0.02616` | PDL=`0.02584` | PDC=`0.02600`
  * Monday Reference: Monday High=`0.02613` | Monday Low=`0.02587` | Monday Mid=`0.02600`
  * Weekly Value Area: Weekly VAH=`0.02621` | Weekly POC=`0.02600` | Weekly VAL=`0.02579`
  * Multi-Week Extremes: Current Week High (CWH)=`0.02626` | CWL=`0.02574` | Prior Week High (PWH)=`0.02639` | PWL=`0.02561`
  * Multi-Month Extremes: Current Month High (CMH)=`0.02652` | CML=`0.02548` | Prior Month High (PMH)=`0.02665` | PML=`0.02535`
- **Session Liquidity Extremes & Initial Balance**:
  * Asian Session: Range `[0.02595 - 0.02605]`
  * London Session: Range `[0.02590 - 0.02610]`
  * New York Session: Range `[0.02587 - 0.02613]`
  * Initial Balance (IB): IB High=`0.02608` | IB Low=`0.02592`
- **Fibonacci Golden Pocket & Optimal Trade Entry (OTE)**:
  * Swing Range: High=`0.01700` | Low=`0.01500` | Direction=`NONE`
  * Golden Pocket [0.618 - 0.65]: `[0.02595 - 0.02605]`
  * Optimal Trade Entry (0.702): `0.02600` | Invalidation Level: `0.00000` | Status: **`NONE`**
- **Classical & Weekly Pivots**:
  * Daily Classical: Pivot=`0.02600` | R1=`0.02608` | S1=`0.02592` | R2=`0.02616` | S2=`0.02584`
  * Weekly Classical: Weekly Pivot=`0.02600` | Weekly R1=`0.02626` | Weekly S1=`0.02574`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Orderflow
*(Sources: 18_CVD.parquet, 18_CVD_30D_5m.parquet, 18_CVD_30D_15m.parquet, 18_CVD_30D_1h.parquet, 18_CVD_30D_4h.parquet, 18_CVD_30D_ALL.parquet, 21_Tradfye_Orderflow.parquet)*
- **Interbank Spot Orderflow Mechanics**: Decentralized OTC market structure. CVD taker deltas do not apply to interbank spot flow. Tape volume governed by broker tick volume with live spread friction of `7692.31 bps`.
- **Session Volume Structure**: Price operating at `INSIDE_VALUE (Balance)` with Daily POC at `0.01500` (VAH: `0.01575` / VAL: `0.01500`).

---

## 5. Institutional Whale Armor & Resting Orderbook Depth
*(Sources: 10_Whale_Orders.parquet, 12_Hyperdash.parquet, 17_Orderbook.parquet, 4_Hyperliquid_Analysis.parquet)*
- **Interbank Institutional Tier-1 Depth**: Decentralized OTC spot liquidity. Resting whale limit walls from crypto venues do not apply.
- **Verified Broker Armor**: Live Bid `0.01600` / Live Ask `0.03600` with institutional spread of `7692.31 bps`. Structural defense anchored at Asian Range `[0.02595 - 0.02605]` and London Range `[0.02590 - 0.02610]`.

---

## 6. Liquidation Max Pain, Heatmaps & Cascade Boundaries
*(Sources: 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 14_Hyperdash_Liq_Map.parquet, 14_Liquidation_Matrix.parquet, 15_Hyperdash_Stops_Map.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **TradFi Structural Liquidity Boundaries**: Centralized perp liquidation feeds do not apply to interbank OTC spot.
- **Stop-Run Cascades & Liquidity Pools**: Primary institutional stop pools reside beyond Classical Pivot extremes (S1: `0.02592` / S2: `0.02584` for long stops; R1: `0.02608` / R2: `0.02616` for short stops) and Asian session extremes `[0.02595 - 0.02605]`.

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
- **Stand-Aside Reason**: Gate 1 Spread Friction Failure: Spread friction 7692.31 bps exceeds cap 25.0 bps. Standing aside in 100% cash preserves statutory floor.