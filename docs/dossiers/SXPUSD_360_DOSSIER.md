# 🔬 MASTER 43-FEED QUANTITATIVE DOSSIER: SXPUSD (SXP/USD)
**MT5 Symbol**: `SXPUSD.p` | **Category**: `Forex Cross` | **Tier**: `Tier 2`
**Execution Posture**: `DISQUALIFIED` | **Timestamp**: 2026-10-29 14:43:14 UTC
**Pipeline Clearance**: `BLOCKED` | **Data Freshness**: `1.2m`

---

## 1. MT5 Live Broker Telemetry & Spread Friction Gate
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet)*
- **Live Bid Quote**: `0.04960` | **Live Ask Quote**: `0.05170` | **Mid Price**: `0.05065`
- **Spread Points**: `21.0 pts` | **Spread BPS**: `414.61 bps` (Mandatory Cap: `25.0 bps`)
- **Gate Status**: **`FAIL`** (Spread friction 414.61 bps exceeds cap 25.0 bps)
- **Order Allowed**: `NONE` | **Pillar 1 Clearance**: `BLOCKED`
- **Broker Specifications**: Contract Size=`1.00` | Tick Value=`1.00 USD` | Min Lot=`0.01` | Digits=`5`
- **Account Capital Context**: Balance=`4,744.55 USD` | Equity=`4,744.32 USD` | Free Margin=`4,342.62 USD` | Inviolate Hard Floor=`4,775.00 USD` (Cushion: `-30.68 USD`)
- **Pipeline Health**: Feed #00 Status=`PASS` | Overall Pipeline Telemetry=`33/33 FEEDS PASS (SYNCHRONIZED)`

---

## 2. Technical Profile, Multi-Sigma VWAP Dispersion & Volatility
*(Sources: 11_Technical.parquet, 11_Technical_BTC_Ribbon.parquet)*
- **Last Verified Price**: `0.06730` | **24h Change**: `+16.44%` (24h High: `0.07550`, 24h Low: `0.05480`)
- **Weekly Range**: Week High=`0.07550` | Week Low=`0.04560` | Daily POC=`0.06730` | Daily VAH=`0.06730` | Daily VAL=`0.06730`
- **Session VWAP**: `0.06730` | **Rolling 24h VWAP**: `0.06639` | **Distance to VWAP**: `+0.00%`
- **VWAP Z-Score**: `+0.20 sigma` | **Mean Reversion Bias**: **`FAIR VALUE`**
- **VWAP Dispersion Bands**:
  * +1.00 sigma: `0.07096` | -1.00 sigma: `0.06183`
  * +1.28 sigma (80% CI): `0.07223` | -1.28 sigma: `0.06055`
  * +2.00 sigma (95% CI): `0.07552` | -2.00 sigma: `0.05726`
  * +2.01 sigma: `0.07556` | -2.01 sigma: `0.05722`
  * +2.51 sigma (98.8% CI): `0.07785` | -2.51 sigma: `0.05494`
  * +3.00 sigma (99.7% CI Extreme): `0.08008` | -3.00 sigma: `0.05270`
- **Oscillators & Volatility**:
  * **RSI (14)**: `51.09` | **RSI State**: **`NEUTRAL`**
  * **ATR (14)**: `0.00116` | **ATR %**: `1.73%`
  * **Bollinger Bands**: Upper=`0.06886` | Mid=`0.06673` | Lower=`0.06461` | Bandwidth=`6.37%`
  * **MACD**: Line=`+0.0001` | Signal=`+0.0000` | Hist=`+0.0001`
- **Exponential Moving Average Ribbon (EMA)**:
  * Short Horizon: EMA-5=`0.06737` | EMA-9=`0.06733` | EMA-13=`0.06725` | EMA-20=`0.06718`
  * Intermediate: EMA-34=`0.06705` | EMA-50=`0.06657` | EMA-89=`0.06457` | EMA-100=`0.06396`
  * Institutional: EMA-144=`0.06180` | EMA-200=`0.05945` (Slope: `+1.730%`) | EMA-233=`0.05802` (Slope: `+1.781%`)
  * **Trend Bias**: **`STRONG BULLISH`**

---

## 3. Auction Market Structure & Value Profile
*(Sources: 20_Auction_Market_Structure.parquet)*
- **Daily Auction Value Area**:
  * High (VAH): `0.06730` | Point of Control (POC): `0.06730` | Low (VAL): `0.06730`
  * Distance to POC: `+0.00%` | Distance to VAH: `+0.00%` | Distance to VAL: `+0.00%`
  * **Value Area Position**: **`INSIDE_VALUE (Balance)`** | **Auction Regime**: **`BALANCED_AUCTION`** | **Session Bias**: **`NEUTRAL`**
- **Prior Day & Weekly Auction Profile**:
  * Prior Day: PD VAH=`0.05085` | PD POC=`0.05065` | PD VAL=`0.05045` | PDH=`0.05095` | PDL=`0.05035` | PDC=`0.05065`
  * Monday Reference: Monday High=`0.05090` | Monday Low=`0.05040` | Monday Mid=`0.05065`
  * Weekly Value Area: Weekly VAH=`0.05106` | Weekly POC=`0.05065` | Weekly VAL=`0.05024`
  * Multi-Week Extremes: Current Week High (CWH)=`0.05116` | CWL=`0.05014` | Prior Week High (PWH)=`0.05141` | PWL=`0.04989`
  * Multi-Month Extremes: Current Month High (CMH)=`0.05166` | CML=`0.04964` | Prior Month High (PMH)=`0.05192` | PML=`0.04938`
- **Session Liquidity Extremes & Initial Balance**:
  * Asian Session: Range `[0.05055 - 0.05075]`
  * London Session: Range `[0.05045 - 0.05085]`
  * New York Session: Range `[0.05040 - 0.05090]`
  * Initial Balance (IB): IB High=`0.05080` | IB Low=`0.05050`
- **Fibonacci Golden Pocket & Optimal Trade Entry (OTE)**:
  * Swing Range: High=`0.07550` | Low=`0.05480` | Direction=`NONE`
  * Golden Pocket [0.618 - 0.65]: `[0.05055 - 0.05075]`
  * Optimal Trade Entry (0.702): `0.05065` | Invalidation Level: `0.00000` | Status: **`NONE`**
- **Classical & Weekly Pivots**:
  * Daily Classical: Pivot=`0.05065` | R1=`0.05080` | S1=`0.05050` | R2=`0.05095` | S2=`0.05035`
  * Weekly Classical: Weekly Pivot=`0.05065` | Weekly R1=`0.05116` | Weekly S1=`0.05014`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Orderflow
*(Sources: 18_CVD.parquet, 18_CVD_30D_5m.parquet, 18_CVD_30D_15m.parquet, 18_CVD_30D_1h.parquet, 18_CVD_30D_4h.parquet, 18_CVD_30D_ALL.parquet, 21_Tradfye_Orderflow.parquet)*
- **Interbank Spot Orderflow Mechanics**: Decentralized OTC market structure. CVD taker deltas do not apply to interbank spot flow. Tape volume governed by broker tick volume with live spread friction of `414.61 bps`.
- **Session Volume Structure**: Price operating at `INSIDE_VALUE (Balance)` with Daily POC at `0.06730` (VAH: `0.06730` / VAL: `0.06730`).

---

## 5. Institutional Whale Armor & Resting Orderbook Depth
*(Sources: 10_Whale_Orders.parquet, 12_Hyperdash.parquet, 17_Orderbook.parquet, 4_Hyperliquid_Analysis.parquet)*
- **Interbank Institutional Tier-1 Depth**: Decentralized OTC spot liquidity. Resting whale limit walls from crypto venues do not apply.
- **Verified Broker Armor**: Live Bid `0.04960` / Live Ask `0.05170` with institutional spread of `414.61 bps`. Structural defense anchored at Asian Range `[0.05055 - 0.05075]` and London Range `[0.05045 - 0.05085]`.

---

## 6. Liquidation Max Pain, Heatmaps & Cascade Boundaries
*(Sources: 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 14_Hyperdash_Liq_Map.parquet, 14_Liquidation_Matrix.parquet, 15_Hyperdash_Stops_Map.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **TradFi Structural Liquidity Boundaries**: Centralized perp liquidation feeds do not apply to interbank OTC spot.
- **Stop-Run Cascades & Liquidity Pools**: Primary institutional stop pools reside beyond Classical Pivot extremes (S1: `0.05050` / S2: `0.05035` for long stops; R1: `0.05080` / R2: `0.05095` for short stops) and Asian session extremes `[0.05055 - 0.05075]`.

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
- **Stand-Aside Reason**: Gate 1 Spread Friction Failure: Spread friction 414.61 bps exceeds cap 25.0 bps. Standing aside in 100% cash preserves statutory floor.