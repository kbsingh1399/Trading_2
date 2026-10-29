# 🔬 MASTER 43-FEED QUANTITATIVE DOSSIER: GAS (Natural Gas)
**MT5 Symbol**: `GAS.p` | **Category**: `Energy / Commodity` | **Tier**: `Tier 2`
**Execution Posture**: `DISQUALIFIED` | **Timestamp**: 2026-10-29 14:43:14 UTC
**Pipeline Clearance**: `BLOCKED` | **Data Freshness**: `1.2m`

---

## 1. MT5 Live Broker Telemetry & Spread Friction Gate
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet)*
- **Live Bid Quote**: `2.65300` | **Live Ask Quote**: `2.67300` | **Mid Price**: `2.66300`
- **Spread Points**: `20.0 pts` | **Spread BPS**: `75.10 bps` (Mandatory Cap: `5.0 bps`)
- **Gate Status**: **`FAIL`** (Spread friction 75.10 bps exceeds cap 5.0 bps)
- **Order Allowed**: `NONE` | **Pillar 1 Clearance**: `BLOCKED`
- **Broker Specifications**: Contract Size=`1.00` | Tick Value=`1.00 USD` | Min Lot=`0.01` | Digits=`5`
- **Account Capital Context**: Balance=`4,744.55 USD` | Equity=`4,744.32 USD` | Free Margin=`4,342.62 USD` | Inviolate Hard Floor=`4,775.00 USD` (Cushion: `-30.68 USD`)
- **Pipeline Health**: Feed #00 Status=`PASS` | Overall Pipeline Telemetry=`33/33 FEEDS PASS (SYNCHRONIZED)`

---

## 2. Technical Profile, Multi-Sigma VWAP Dispersion & Volatility
*(Sources: 11_Technical.parquet, 11_Technical_BTC_Ribbon.parquet)*
- **Last Verified Price**: `2.64200` | **24h Change**: `-3.26%` (24h High: `2.77300`, 24h Low: `2.62100`)
- **Weekly Range**: Week High=`2.77300` | Week Low=`2.62100` | Daily POC=`2.73000` | Daily VAH=`2.76700` | Daily VAL=`2.64800`
- **Session VWAP**: `2.69075` | **Rolling 24h VWAP**: `2.71305` | **Distance to VWAP**: `-1.81%`
- **VWAP Z-Score**: `-1.13 sigma` | **Mean Reversion Bias**: **`FAIR VALUE`**
- **VWAP Dispersion Bands**:
  * +1.00 sigma: `2.73400` | -1.00 sigma: `2.64750`
  * +1.28 sigma (80% CI): `2.74610` | -1.28 sigma: `2.63539`
  * +2.00 sigma (95% CI): `2.77724` | -2.00 sigma: `2.60425`
  * +2.01 sigma: `2.77768` | -2.01 sigma: `2.60382`
  * +2.51 sigma (98.8% CI): `2.79930` | -2.51 sigma: `2.58220`
  * +3.00 sigma (99.7% CI Extreme): `2.82049` | -3.00 sigma: `2.56100`
- **Oscillators & Volatility**:
  * **RSI (14)**: `26.31` | **RSI State**: **`OVERSOLD`**
  * **ATR (14)**: `0.01987` | **ATR %**: `0.75%`
  * **Bollinger Bands**: Upper=`2.80028` | Mid=`2.70785` | Lower=`2.61542` | Bandwidth=`6.83%`
  * **MACD**: Line=`-0.0249` | Signal=`-0.0155` | Hist=`-0.0095`
- **Exponential Moving Average Ribbon (EMA)**:
  * Short Horizon: EMA-5=`2.64851` | EMA-9=`2.66325` | EMA-13=`2.67569` | EMA-20=`2.69018`
  * Intermediate: EMA-34=`2.70434` | EMA-50=`2.71158` | EMA-89=`2.71843` | EMA-100=`2.71912`
  * Institutional: EMA-144=`2.71961` | EMA-200=`2.71498` (Slope: `-0.160%`) | EMA-233=`2.71255` (Slope: `-0.126%`)
  * **Trend Bias**: **`STRONG BEARISH`**

---

## 3. Auction Market Structure & Value Profile
*(Sources: 20_Auction_Market_Structure.parquet)*
- **Daily Auction Value Area**:
  * High (VAH): `2.76700` | Point of Control (POC): `2.73000` | Low (VAL): `2.64800`
  * Distance to POC: `-2.60%` | Distance to VAH: `-3.92%` | Distance to VAL: `+0.42%`
  * **Value Area Position**: **`INSIDE_VALUE (Balance)`** | **Auction Regime**: **`ROTATIONAL_BALANCE`** | **Session Bias**: **`BEARISH (Below Pivot)`**
- **Prior Day & Weekly Auction Profile**:
  * Prior Day: PD VAH=`2.75800` | PD POC=`2.74000` | PD VAL=`2.73100` | PDH=`2.77300` | PDL=`2.69500` | PDC=`2.72100`
  * Monday Reference: Monday High=`2.71600` | Monday Low=`2.60700` | Monday Mid=`2.66200`
  * Weekly Value Area: Weekly VAH=`2.75700` | Weekly POC=`2.74000` | Weekly VAL=`2.66700`
  * Multi-Week Extremes: Current Week High (CWH)=`2.77300` | CWL=`2.60700` | Prior Week High (PWH)=`3.14800` | PWL=`2.63800`
  * Multi-Month Extremes: Current Month High (CMH)=`3.27700` | CML=`2.60700` | Prior Month High (PMH)=`3.25500` | PML=`2.73800`
- **Session Liquidity Extremes & Initial Balance**:
  * Asian Session: Range `[2.70200 - 2.73200]`
  * London Session: Range `[2.62100 - 2.77300]`
  * New York Session: Range `[2.62100 - 2.75000]`
  * Initial Balance (IB): IB High=`2.73500` | IB Low=`2.72300`
- **Fibonacci Golden Pocket & Optimal Trade Entry (OTE)**:
  * Swing Range: High=`2.77300` | Low=`2.62100` | Direction=`BEARISH_IMPULSE`
  * Golden Pocket [0.618 - 0.65]: `[2.71500 - 2.72000]`
  * Optimal Trade Entry (0.702): `2.72800` | Invalidation Level: `2.74000` | Status: **`SHALLOW_RETRACE`**
- **Classical & Weekly Pivots**:
  * Daily Classical: Pivot=`2.73000` | R1=`2.76400` | S1=`2.68600` | R2=`2.80800` | S2=`2.65200`
  * Weekly Classical: Weekly Pivot=`2.81500` | Weekly R1=`2.99200` | Weekly S1=`2.48200`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Orderflow
*(Sources: 18_CVD.parquet, 18_CVD_30D_5m.parquet, 18_CVD_30D_15m.parquet, 18_CVD_30D_1h.parquet, 18_CVD_30D_4h.parquet, 18_CVD_30D_ALL.parquet, 21_Tradfye_Orderflow.parquet)*
- **Interbank Spot Orderflow Mechanics**: Decentralized OTC market structure. CVD taker deltas do not apply to interbank spot flow. Tape volume governed by broker tick volume with live spread friction of `75.10 bps`.
- **Session Volume Structure**: Price operating at `INSIDE_VALUE (Balance)` with Daily POC at `2.73000` (VAH: `2.76700` / VAL: `2.64800`).

---

## 5. Institutional Whale Armor & Resting Orderbook Depth
*(Sources: 10_Whale_Orders.parquet, 12_Hyperdash.parquet, 17_Orderbook.parquet, 4_Hyperliquid_Analysis.parquet)*
- **Interbank Institutional Tier-1 Depth**: Decentralized OTC spot liquidity. Resting whale limit walls from crypto venues do not apply.
- **Verified Broker Armor**: Live Bid `2.65300` / Live Ask `2.67300` with institutional spread of `75.10 bps`. Structural defense anchored at Asian Range `[2.70200 - 2.73200]` and London Range `[2.62100 - 2.77300]`.

---

## 6. Liquidation Max Pain, Heatmaps & Cascade Boundaries
*(Sources: 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 14_Hyperdash_Liq_Map.parquet, 14_Liquidation_Matrix.parquet, 15_Hyperdash_Stops_Map.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`1.18590` (Vol: `3,334 USD`, Dist: `+1.10%`) | Long MP=`1.13910` (Vol: `3,334 USD`, Dist: `-2.89%`)
  * 48H Horizon: Short MP=`1.20870` (Vol: `8,998 USD`, Dist: `+3.04%`) | Long MP=`1.13720` (Vol: `8,141 USD`, Dist: `-3.05%`)
  * 3D Horizon: Short MP=`1.26620` (Vol: `10,074 USD`, Dist: `+7.95%`) | Long MP=`1.13880` (Vol: `7,101 USD`, Dist: `-2.92%`)
  * 7D Horizon: Short MP=`1.20940` (Vol: `8,687 USD`, Dist: `+3.28%`) | Long MP=`1.13800` (Vol: `9,665 USD`, Dist: `-2.82%`)
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
- **Stand-Aside Reason**: Gate 1 Spread Friction Failure: Spread friction 75.10 bps exceeds cap 5.0 bps. Standing aside in 100% cash preserves statutory floor.