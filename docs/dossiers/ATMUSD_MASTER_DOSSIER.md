# 🔬 MASTER 43-FEED QUANTITATIVE DOSSIER: ATMUSD (Atletico Madrid / USD)
**MT5 Symbol**: `ATMUSD.p` | **Category**: `Crypto Altcoin` | **Tier**: `Tier 2`
**Execution Posture**: `DISQUALIFIED` | **Timestamp**: 2026-10-29 14:43:14 UTC
**Pipeline Clearance**: `BLOCKED` | **Data Freshness**: `1.2m`

---

## 1. MT5 Live Broker Telemetry & Spread Friction Gate
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet)*
- **Live Bid Quote**: `1.60400` | **Live Ask Quote**: `1.62700` | **Mid Price**: `1.61550`
- **Spread Points**: `23.0 pts` | **Spread BPS**: `142.37 bps` (Mandatory Cap: `25.0 bps`)
- **Gate Status**: **`FAIL`** (Spread friction 142.37 bps exceeds cap 25.0 bps)
- **Order Allowed**: `NONE` | **Pillar 1 Clearance**: `BLOCKED`
- **Broker Specifications**: Contract Size=`1.00` | Tick Value=`1.00 USD` | Min Lot=`0.01` | Digits=`5`
- **Account Capital Context**: Balance=`4,744.55 USD` | Equity=`4,744.32 USD` | Free Margin=`4,342.62 USD` | Inviolate Hard Floor=`4,775.00 USD` (Cushion: `-30.68 USD`)
- **Pipeline Health**: Feed #00 Status=`PASS` | Overall Pipeline Telemetry=`33/33 FEEDS PASS (SYNCHRONIZED)`

---

## 2. Technical Profile, Multi-Sigma VWAP Dispersion & Volatility
*(Sources: 11_Technical.parquet, 11_Technical_BTC_Ribbon.parquet)*
- **Last Verified Price**: `1.60700` | **24h Change**: `+0.06%` (24h High: `1.64700`, 24h Low: `1.56800`)
- **Weekly Range**: Week High=`1.65700` | Week Low=`1.56800` | Daily POC=`1.60700` | Daily VAH=`1.61700` | Daily VAL=`1.58000`
- **Session VWAP**: `1.59701` | **Rolling 24h VWAP**: `1.60512` | **Distance to VWAP**: `+0.63%`
- **VWAP Z-Score**: `+0.65 sigma` | **Mean Reversion Bias**: **`FAIR VALUE`**
- **VWAP Dispersion Bands**:
  * +1.00 sigma: `1.61238` | -1.00 sigma: `1.58165`
  * +1.28 sigma (80% CI): `1.61668` | -1.28 sigma: `1.57735`
  * +2.00 sigma (95% CI): `1.62774` | -2.00 sigma: `1.56628`
  * +2.01 sigma: `1.62790` | -2.01 sigma: `1.56613`
  * +2.51 sigma (98.8% CI): `1.63558` | -2.51 sigma: `1.55845`
  * +3.00 sigma (99.7% CI Extreme): `1.64311` | -3.00 sigma: `1.55092`
- **Oscillators & Volatility**:
  * **RSI (14)**: `52.51` | **RSI State**: **`NEUTRAL`**
  * **ATR (14)**: `0.00811` | **ATR %**: `0.50%`
  * **Bollinger Bands**: Upper=`1.61788` | Mid=`1.60705` | Lower=`1.59622` | Bandwidth=`1.35%`
  * **MACD**: Line=`+0.0030` | Signal=`+0.0037` | Hist=`-0.0007`
- **Exponential Moving Average Ribbon (EMA)**:
  * Short Horizon: EMA-5=`1.60714` | EMA-9=`1.60776` | EMA-13=`1.60724` | EMA-20=`1.60561`
  * Intermediate: EMA-34=`1.60361` | EMA-50=`1.60350` | EMA-89=`1.60574` | EMA-100=`1.60644`
  * Institutional: EMA-144=`1.60897` | EMA-200=`1.61022` (Slope: `-0.006%`) | EMA-233=`1.61138` (Slope: `-0.013%`)
  * **Trend Bias**: **`BULLISH`**

---

## 3. Auction Market Structure & Value Profile
*(Sources: 20_Auction_Market_Structure.parquet)*
- **Daily Auction Value Area**:
  * High (VAH): `1.61700` | Point of Control (POC): `1.60700` | Low (VAL): `1.58000`
  * Distance to POC: `+0.52%` | Distance to VAH: `-0.12%` | Distance to VAL: `+2.22%`
  * **Value Area Position**: **`INSIDE_VALUE (Balance)`** | **Auction Regime**: **`ROTATIONAL_BALANCE`** | **Session Bias**: **`BEARISH (Below Pivot)`**
- **Prior Day & Weekly Auction Profile**:
  * Prior Day: PD VAH=`1.63500` | PD POC=`1.61900` | PD VAL=`1.60800` | PDH=`1.64700` | PDL=`1.58900` | PDC=`1.63100`
  * Monday Reference: Monday High=`1.65700` | Monday Low=`1.60000` | Monday Mid=`1.62900`
  * Weekly Value Area: Weekly VAH=`1.63500` | Weekly POC=`1.61900` | Weekly VAL=`1.60300`
  * Multi-Week Extremes: Current Week High (CWH)=`1.65700` | CWL=`1.56800` | Prior Week High (PWH)=`1.80400` | PWL=`1.59000`
  * Multi-Month Extremes: Current Month High (CMH)=`2.07200` | CML=`1.56800` | Prior Month High (PMH)=`2.01700` | PML=`1.42900`
- **Session Liquidity Extremes & Initial Balance**:
  * Asian Session: Range `[1.56800 - 1.64100]`
  * London Session: Range `[1.57700 - 1.61800]`
  * New York Session: Range `[1.59600 - 1.61800]`
  * Initial Balance (IB): IB High=`1.60800` | IB Low=`1.58900`
- **Fibonacci Golden Pocket & Optimal Trade Entry (OTE)**:
  * Swing Range: High=`1.64700` | Low=`1.56800` | Direction=`BEARISH_IMPULSE`
  * Golden Pocket [0.618 - 0.65]: `[1.61700 - 1.61900]`
  * Optimal Trade Entry (0.702): `1.62300` | Invalidation Level: `1.63000` | Status: **`SHALLOW_RETRACE`**
- **Classical & Weekly Pivots**:
  * Daily Classical: Pivot=`1.62200` | R1=`1.65600` | S1=`1.59800` | R2=`1.68000` | S2=`1.56400`
  * Weekly Classical: Weekly Pivot=`1.67500` | Weekly R1=`1.76000` | Weekly S1=`1.54600`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Orderflow
*(Sources: 18_CVD.parquet, 18_CVD_30D_5m.parquet, 18_CVD_30D_15m.parquet, 18_CVD_30D_1h.parquet, 18_CVD_30D_4h.parquet, 18_CVD_30D_ALL.parquet, 21_Tradfye_Orderflow.parquet)*
- **Interbank Spot Orderflow Mechanics**: Decentralized OTC market structure. CVD taker deltas do not apply to interbank spot flow. Tape volume governed by broker tick volume with live spread friction of `142.37 bps`.
- **Session Volume Structure**: Price operating at `INSIDE_VALUE (Balance)` with Daily POC at `1.60700` (VAH: `1.61700` / VAL: `1.58000`).

---

## 5. Institutional Whale Armor & Resting Orderbook Depth
*(Sources: 10_Whale_Orders.parquet, 12_Hyperdash.parquet, 17_Orderbook.parquet, 4_Hyperliquid_Analysis.parquet)*
- **Interbank Institutional Tier-1 Depth**: Decentralized OTC spot liquidity. Resting whale limit walls from crypto venues do not apply.
- **Verified Broker Armor**: Live Bid `1.60400` / Live Ask `1.62700` with institutional spread of `142.37 bps`. Structural defense anchored at Asian Range `[1.56800 - 1.64100]` and London Range `[1.57700 - 1.61800]`.

---

## 6. Liquidation Max Pain, Heatmaps & Cascade Boundaries
*(Sources: 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 14_Hyperdash_Liq_Map.parquet, 14_Liquidation_Matrix.parquet, 15_Hyperdash_Stops_Map.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **TradFi Structural Liquidity Boundaries**: Centralized perp liquidation feeds do not apply to interbank OTC spot.
- **Stop-Run Cascades & Liquidity Pools**: Primary institutional stop pools reside beyond Classical Pivot extremes (S1: `1.59800` / S2: `1.56400` for long stops; R1: `1.65600` / R2: `1.68000` for short stops) and Asian session extremes `[1.56800 - 1.64100]`.

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
- **Stand-Aside Reason**: Gate 1 Spread Friction Failure: Spread friction 142.37 bps exceeds cap 25.0 bps. Standing aside in 100% cash preserves statutory floor.