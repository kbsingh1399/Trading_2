# 🔬 MASTER 43-FEED QUANTITATIVE DOSSIER: KNCUSD (KNC/USD)
**MT5 Symbol**: `KNCUSD.p` | **Category**: `Forex Cross` | **Tier**: `Tier 2`
**Execution Posture**: `DISQUALIFIED` | **Timestamp**: 2026-10-29 14:43:14 UTC
**Pipeline Clearance**: `BLOCKED` | **Data Freshness**: `1.2m`

---

## 1. MT5 Live Broker Telemetry & Spread Friction Gate
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet)*
- **Live Bid Quote**: `0.10700` | **Live Ask Quote**: `0.12700` | **Mid Price**: `0.11700`
- **Spread Points**: `20.0 pts` | **Spread BPS**: `1709.40 bps` (Mandatory Cap: `25.0 bps`)
- **Gate Status**: **`FAIL`** (Spread friction 1709.40 bps exceeds cap 25.0 bps)
- **Order Allowed**: `NONE` | **Pillar 1 Clearance**: `BLOCKED`
- **Broker Specifications**: Contract Size=`1.00` | Tick Value=`1.00 USD` | Min Lot=`0.01` | Digits=`5`
- **Account Capital Context**: Balance=`4,744.55 USD` | Equity=`4,744.32 USD` | Free Margin=`4,342.62 USD` | Inviolate Hard Floor=`4,775.00 USD` (Cushion: `-30.68 USD`)
- **Pipeline Health**: Feed #00 Status=`PASS` | Overall Pipeline Telemetry=`33/33 FEEDS PASS (SYNCHRONIZED)`

---

## 2. Technical Profile, Multi-Sigma VWAP Dispersion & Volatility
*(Sources: 11_Technical.parquet, 11_Technical_BTC_Ribbon.parquet)*
- **Last Verified Price**: `0.10700` | **24h Change**: `-1.83%` (24h High: `0.11100`, 24h Low: `0.10500`)
- **Weekly Range**: Week High=`0.11100` | Week Low=`0.10500` | Daily POC=`0.10598` | Daily VAH=`0.10706` | Daily VAL=`0.10562`
- **Session VWAP**: `0.10638` | **Rolling 24h VWAP**: `0.10761` | **Distance to VWAP**: `+0.59%`
- **VWAP Z-Score**: `+0.64 sigma` | **Mean Reversion Bias**: **`FAIR VALUE`**
- **VWAP Dispersion Bands**:
  * +1.00 sigma: `0.10735` | -1.00 sigma: `0.10540`
  * +1.28 sigma (80% CI): `0.10762` | -1.28 sigma: `0.10513`
  * +2.00 sigma (95% CI): `0.10832` | -2.00 sigma: `0.10443`
  * +2.01 sigma: `0.10833` | -2.01 sigma: `0.10442`
  * +2.51 sigma (98.8% CI): `0.10881` | -2.51 sigma: `0.10394`
  * +3.00 sigma (99.7% CI Extreme): `0.10929` | -3.00 sigma: `0.10346`
- **Oscillators & Volatility**:
  * **RSI (14)**: `59.07` | **RSI State**: **`BULLISH`**
  * **ATR (14)**: `0.00033` | **ATR %**: `0.31%`
  * **Bollinger Bands**: Upper=`0.10744` | Mid=`0.10645` | Lower=`0.10546` | Bandwidth=`1.87%`
  * **MACD**: Line=`+0.0002` | Signal=`+0.0002` | Hist=`+0.0001`
- **Exponential Moving Average Ribbon (EMA)**:
  * Short Horizon: EMA-5=`0.10696` | EMA-9=`0.10685` | EMA-13=`0.10672` | EMA-20=`0.10656`
  * Intermediate: EMA-34=`0.10650` | EMA-50=`0.10667` | EMA-89=`0.10722` | EMA-100=`0.10736`
  * Institutional: EMA-144=`0.10778` | EMA-200=`0.10808` (Slope: `-0.155%`) | EMA-233=`0.10823` (Slope: `-0.148%`)
  * **Trend Bias**: **`NEUTRAL / CHOP`**

---

## 3. Auction Market Structure & Value Profile
*(Sources: 20_Auction_Market_Structure.parquet)*
- **Daily Auction Value Area**:
  * High (VAH): `0.10706` | Point of Control (POC): `0.10598` | Low (VAL): `0.10562`
  * Distance to POC: `+0.00%` | Distance to VAH: `+0.00%` | Distance to VAL: `+0.00%`
  * **Value Area Position**: **`INSIDE_VALUE (Balance)`** | **Auction Regime**: **`BALANCED_AUCTION`** | **Session Bias**: **`NEUTRAL`**
- **Prior Day & Weekly Auction Profile**:
  * Prior Day: PD VAH=`0.11747` | PD POC=`0.11700` | PD VAL=`0.11653` | PDH=`0.11770` | PDL=`0.11630` | PDC=`0.11700`
  * Monday Reference: Monday High=`0.11758` | Monday Low=`0.11641` | Monday Mid=`0.11700`
  * Weekly Value Area: Weekly VAH=`0.11794` | Weekly POC=`0.11700` | Weekly VAL=`0.11606`
  * Multi-Week Extremes: Current Week High (CWH)=`0.11817` | CWL=`0.11583` | Prior Week High (PWH)=`0.11875` | PWL=`0.11524`
  * Multi-Month Extremes: Current Month High (CMH)=`0.11934` | CML=`0.11466` | Prior Month High (PMH)=`0.11992` | PML=`0.11407`
- **Session Liquidity Extremes & Initial Balance**:
  * Asian Session: Range `[0.11677 - 0.11723]`
  * London Session: Range `[0.11653 - 0.11747]`
  * New York Session: Range `[0.11641 - 0.11758]`
  * Initial Balance (IB): IB High=`0.11735` | IB Low=`0.11665`
- **Fibonacci Golden Pocket & Optimal Trade Entry (OTE)**:
  * Swing Range: High=`0.11100` | Low=`0.10500` | Direction=`NONE`
  * Golden Pocket [0.618 - 0.65]: `[0.11677 - 0.11723]`
  * Optimal Trade Entry (0.702): `0.11700` | Invalidation Level: `0.00000` | Status: **`NONE`**
- **Classical & Weekly Pivots**:
  * Daily Classical: Pivot=`0.11700` | R1=`0.11735` | S1=`0.11665` | R2=`0.11770` | S2=`0.11630`
  * Weekly Classical: Weekly Pivot=`0.11700` | Weekly R1=`0.11817` | Weekly S1=`0.11583`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Orderflow
*(Sources: 18_CVD.parquet, 18_CVD_30D_5m.parquet, 18_CVD_30D_15m.parquet, 18_CVD_30D_1h.parquet, 18_CVD_30D_4h.parquet, 18_CVD_30D_ALL.parquet, 21_Tradfye_Orderflow.parquet)*
- **Interbank Spot Orderflow Mechanics**: Decentralized OTC market structure. CVD taker deltas do not apply to interbank spot flow. Tape volume governed by broker tick volume with live spread friction of `1709.40 bps`.
- **Session Volume Structure**: Price operating at `INSIDE_VALUE (Balance)` with Daily POC at `0.10598` (VAH: `0.10706` / VAL: `0.10562`).

---

## 5. Institutional Whale Armor & Resting Orderbook Depth
*(Sources: 10_Whale_Orders.parquet, 12_Hyperdash.parquet, 17_Orderbook.parquet, 4_Hyperliquid_Analysis.parquet)*
- **Interbank Institutional Tier-1 Depth**: Decentralized OTC spot liquidity. Resting whale limit walls from crypto venues do not apply.
- **Verified Broker Armor**: Live Bid `0.10700` / Live Ask `0.12700` with institutional spread of `1709.40 bps`. Structural defense anchored at Asian Range `[0.11677 - 0.11723]` and London Range `[0.11653 - 0.11747]`.

---

## 6. Liquidation Max Pain, Heatmaps & Cascade Boundaries
*(Sources: 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 14_Hyperdash_Liq_Map.parquet, 14_Liquidation_Matrix.parquet, 15_Hyperdash_Stops_Map.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`0.12108` (Vol: `4,739 USD`, Dist: `+0.98%`) | Long MP=`0.11640` (Vol: `4,739 USD`, Dist: `-2.92%`)
  * 48H Horizon: Short MP=`0.12220` (Vol: `5,417 USD`, Dist: `+1.92%`) | Long MP=`0.11750` (Vol: `5,417 USD`, Dist: `-2.00%`)
  * 3D Horizon: Short MP=`0.12335` (Vol: `5,452 USD`, Dist: `+2.88%`) | Long MP=`0.11741` (Vol: `7,324 USD`, Dist: `-2.08%`)
  * 7D Horizon: Short MP=`0.12251` (Vol: `7,969 USD`, Dist: `+2.43%`) | Long MP=`0.11770` (Vol: `9,059 USD`, Dist: `-1.59%`)
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
- **Stand-Aside Reason**: Gate 1 Spread Friction Failure: Spread friction 1709.40 bps exceeds cap 25.0 bps. Standing aside in 100% cash preserves statutory floor.