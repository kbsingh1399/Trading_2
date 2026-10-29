# 🔬 MASTER 43-FEED QUANTITATIVE DOSSIER: CHINA50 (China A50 Index)
**MT5 Symbol**: `CHINA50.p` | **Category**: `Equity Index` | **Tier**: `Tier 2`
**Execution Posture**: `DISQUALIFIED` | **Timestamp**: 2026-10-29 14:43:14 UTC
**Pipeline Clearance**: `BLOCKED` | **Data Freshness**: `1.2m`

---

## 1. MT5 Live Broker Telemetry & Spread Friction Gate
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet)*
- **Live Bid Quote**: `12864.06000` | **Live Ask Quote**: `12874.94000` | **Mid Price**: `12869.50000`
- **Spread Points**: `1088.0 pts` | **Spread BPS**: `8.45 bps` (Mandatory Cap: `5.0 bps`)
- **Gate Status**: **`FAIL`** (Spread friction 8.45 bps exceeds cap 5.0 bps)
- **Order Allowed**: `NONE` | **Pillar 1 Clearance**: `BLOCKED`
- **Broker Specifications**: Contract Size=`1.00` | Tick Value=`1.00 USD` | Min Lot=`0.01` | Digits=`5`
- **Account Capital Context**: Balance=`4,744.55 USD` | Equity=`4,744.32 USD` | Free Margin=`4,342.62 USD` | Inviolate Hard Floor=`4,775.00 USD` (Cushion: `-30.68 USD`)
- **Pipeline Health**: Feed #00 Status=`PASS` | Overall Pipeline Telemetry=`33/33 FEEDS PASS (SYNCHRONIZED)`

---

## 2. Technical Profile, Multi-Sigma VWAP Dispersion & Volatility
*(Sources: 11_Technical.parquet, 11_Technical_BTC_Ribbon.parquet)*
- **Last Verified Price**: `12863.06000` | **24h Change**: `-0.91%` (24h High: `13015.56000`, 24h Low: `12828.50000`)
- **Weekly Range**: Week High=`13073.06000` | Week Low=`12828.50000` | Daily POC=`12887.35000` | Daily VAH=`12945.65000` | Daily VAL=`12858.75000`
- **Session VWAP**: `12908.18100` | **Rolling 24h VWAP**: `12914.96674` | **Distance to VWAP**: `-0.35%`
- **VWAP Z-Score**: `-1.37 sigma` | **Mean Reversion Bias**: **`FAIR VALUE`**
- **VWAP Dispersion Bands**:
  * +1.00 sigma: `12941.06583` | -1.00 sigma: `12875.29616`
  * +1.28 sigma (80% CI): `12950.27359` | -1.28 sigma: `12866.08841`
  * +2.00 sigma (95% CI): `12973.95067` | -2.00 sigma: `12842.41133`
  * +2.01 sigma: `12974.27952` | -2.01 sigma: `12842.08248`
  * +2.51 sigma (98.8% CI): `12990.72194` | -2.51 sigma: `12825.64006`
  * +3.00 sigma (99.7% CI Extreme): `13006.83551` | -3.00 sigma: `12809.52649`
- **Oscillators & Volatility**:
  * **RSI (14)**: `38.19` | **RSI State**: **`BEARISH`**
  * **ATR (14)**: `16.07047` | **ATR %**: `0.12%`
  * **Bollinger Bands**: Upper=`12906.52838` | Mid=`12885.93500` | Lower=`12865.34162` | Bandwidth=`0.32%`
  * **MACD**: Line=`-7.9456` | Signal=`-6.6691` | Hist=`-1.2765`
- **Exponential Moving Average Ribbon (EMA)**:
  * Short Horizon: EMA-5=`12871.73658` | EMA-9=`12876.15156` | EMA-13=`12879.08846` | EMA-20=`12883.08009`
  * Intermediate: EMA-34=`12890.94571` | EMA-50=`12900.01350` | EMA-89=`12917.97205` | EMA-100=`12922.19050`
  * Institutional: EMA-144=`12936.16842` | EMA-200=`12950.81174` (Slope: `-0.068%`) | EMA-233=`12957.02498` (Slope: `-0.063%`)
  * **Trend Bias**: **`STRONG BEARISH`**

---

## 3. Auction Market Structure & Value Profile
*(Sources: 20_Auction_Market_Structure.parquet)*
- **Daily Auction Value Area**:
  * High (VAH): `12945.65000` | Point of Control (POC): `12887.35000` | Low (VAL): `12858.75000`
  * Distance to POC: `-0.13%` | Distance to VAH: `-0.58%` | Distance to VAL: `+0.09%`
  * **Value Area Position**: **`INSIDE_VALUE (Balance)`** | **Auction Regime**: **`ROTATIONAL_BALANCE`** | **Session Bias**: **`BEARISH (Below Pivot)`**
- **Prior Day & Weekly Auction Profile**:
  * Prior Day: PD VAH=`12996.11000` | PD POC=`12974.20000` | PD VAL=`12937.29000` | PDH=`13070.50000` | PDL=`12897.50000` | PDC=`12972.06000`
  * Monday Reference: Monday High=`13073.06000` | Monday Low=`12834.50000` | Monday Mid=`12953.78000`
  * Weekly Value Area: Weekly VAH=`13033.12000` | Weekly POC=`12967.90000` | Weekly VAL=`12904.31000`
  * Multi-Week Extremes: Current Week High (CWH)=`13073.06000` | CWL=`12828.50000` | Prior Week High (PWH)=`13446.50000` | PWL=`12647.50000`
  * Multi-Month Extremes: Current Month High (CMH)=`13999.50000` | CML=`12647.50000` | Prior Month High (PMH)=`14814.50000` | PML=`13834.50000`
- **Session Liquidity Extremes & Initial Balance**:
  * Asian Session: Range `[12828.50000 - 12993.50000]`
  * London Session: Range `[12858.50000 - 12991.00000]`
  * New York Session: Range `[12853.06000 - 12906.56000]`
  * Initial Balance (IB): IB High=`12991.00000` | IB Low=`12896.50000`
- **Fibonacci Golden Pocket & Optimal Trade Entry (OTE)**:
  * Swing Range: High=`13015.56000` | Low=`12828.50000` | Direction=`BEARISH_IMPULSE`
  * Golden Pocket [0.618 - 0.65]: `[12944.10000 - 12950.09000]`
  * Optimal Trade Entry (0.702): `12959.82000` | Invalidation Level: `12975.53000` | Status: **`SHALLOW_RETRACE`**
- **Classical & Weekly Pivots**:
  * Daily Classical: Pivot=`12980.02000` | R1=`13062.54000` | S1=`12889.54000` | R2=`13153.02000` | S2=`12807.02000`
  * Weekly Classical: Weekly Pivot=`13009.52000` | Weekly R1=`13371.54000` | Weekly S1=`12572.54000`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Orderflow
*(Sources: 18_CVD.parquet, 18_CVD_30D_5m.parquet, 18_CVD_30D_15m.parquet, 18_CVD_30D_1h.parquet, 18_CVD_30D_4h.parquet, 18_CVD_30D_ALL.parquet, 21_Tradfye_Orderflow.parquet)*
- **Interbank Spot Orderflow Mechanics**: Decentralized OTC market structure. CVD taker deltas do not apply to interbank spot flow. Tape volume governed by broker tick volume with live spread friction of `8.45 bps`.
- **Session Volume Structure**: Price operating at `INSIDE_VALUE (Balance)` with Daily POC at `12887.35000` (VAH: `12945.65000` / VAL: `12858.75000`).

---

## 5. Institutional Whale Armor & Resting Orderbook Depth
*(Sources: 10_Whale_Orders.parquet, 12_Hyperdash.parquet, 17_Orderbook.parquet, 4_Hyperliquid_Analysis.parquet)*
- **Interbank Institutional Tier-1 Depth**: Decentralized OTC spot liquidity. Resting whale limit walls from crypto venues do not apply.
- **Verified Broker Armor**: Live Bid `12864.06000` / Live Ask `12874.94000` with institutional spread of `8.45 bps`. Structural defense anchored at Asian Range `[12828.50000 - 12993.50000]` and London Range `[12858.50000 - 12991.00000]`.

---

## 6. Liquidation Max Pain, Heatmaps & Cascade Boundaries
*(Sources: 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 14_Hyperdash_Liq_Map.parquet, 14_Liquidation_Matrix.parquet, 15_Hyperdash_Stops_Map.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **TradFi Structural Liquidity Boundaries**: Centralized perp liquidation feeds do not apply to interbank OTC spot.
- **Stop-Run Cascades & Liquidity Pools**: Primary institutional stop pools reside beyond Classical Pivot extremes (S1: `12889.54000` / S2: `12807.02000` for long stops; R1: `13062.54000` / R2: `13153.02000` for short stops) and Asian session extremes `[12828.50000 - 12993.50000]`.

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
- **Stand-Aside Reason**: Gate 1 Spread Friction Failure: Spread friction 8.45 bps exceeds cap 5.0 bps. Standing aside in 100% cash preserves statutory floor.