# 🔬 MASTER 43-FEED QUANTITATIVE DOSSIER: SNDUSD (SND/USD)
**MT5 Symbol**: `SNDUSD.p` | **Category**: `Forex Cross` | **Tier**: `Tier 2`
**Execution Posture**: `DISQUALIFIED` | **Timestamp**: 2026-10-29 14:43:14 UTC
**Pipeline Clearance**: `BLOCKED` | **Data Freshness**: `1.2m`

---

## 1. MT5 Live Broker Telemetry & Spread Friction Gate
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet)*
- **Live Bid Quote**: `0.04680` | **Live Ask Quote**: `0.04900` | **Mid Price**: `0.04790`
- **Spread Points**: `22.0 pts` | **Spread BPS**: `459.29 bps` (Mandatory Cap: `25.0 bps`)
- **Gate Status**: **`FAIL`** (Spread friction 459.29 bps exceeds cap 25.0 bps)
- **Order Allowed**: `NONE` | **Pillar 1 Clearance**: `BLOCKED`
- **Broker Specifications**: Contract Size=`1.00` | Tick Value=`1.00 USD` | Min Lot=`0.01` | Digits=`5`
- **Account Capital Context**: Balance=`4,744.55 USD` | Equity=`4,744.32 USD` | Free Margin=`4,342.62 USD` | Inviolate Hard Floor=`4,775.00 USD` (Cushion: `-30.68 USD`)
- **Pipeline Health**: Feed #00 Status=`PASS` | Overall Pipeline Telemetry=`33/33 FEEDS PASS (SYNCHRONIZED)`

---

## 2. Technical Profile, Multi-Sigma VWAP Dispersion & Volatility
*(Sources: 11_Technical.parquet, 11_Technical_BTC_Ribbon.parquet)*
- **Last Verified Price**: `0.04670` | **24h Change**: `+0.00%` (24h High: `0.04730`, 24h Low: `0.04450`)
- **Weekly Range**: Week High=`0.04790` | Week Low=`0.04450` | Daily POC=`0.04490` | Daily VAH=`0.04640` | Daily VAL=`0.04460`
- **Session VWAP**: `0.04556` | **Rolling 24h VWAP**: `0.04596` | **Distance to VWAP**: `+2.49%`
- **VWAP Z-Score**: `+1.68 sigma` | **Mean Reversion Bias**: **`OVERBOUGHT`**
- **VWAP Dispersion Bands**:
  * +1.00 sigma: `0.04624` | -1.00 sigma: `0.04489`
  * +1.28 sigma (80% CI): `0.04643` | -1.28 sigma: `0.04470`
  * +2.00 sigma (95% CI): `0.04692` | -2.00 sigma: `0.04421`
  * +2.01 sigma: `0.04693` | -2.01 sigma: `0.04420`
  * +2.51 sigma (98.8% CI): `0.04726` | -2.51 sigma: `0.04386`
  * +3.00 sigma (99.7% CI Extreme): `0.04760` | -3.00 sigma: `0.04353`
- **Oscillators & Volatility**:
  * **RSI (14)**: `68.68` | **RSI State**: **`BULLISH`**
  * **ATR (14)**: `0.00028` | **ATR %**: `0.60%`
  * **Bollinger Bands**: Upper=`0.04700` | Mid=`0.04605` | Lower=`0.04510` | Bandwidth=`4.12%`
  * **MACD**: Line=`+0.0004` | Signal=`+0.0003` | Hist=`+0.0001`
- **Exponential Moving Average Ribbon (EMA)**:
  * Short Horizon: EMA-5=`0.04662` | EMA-9=`0.04648` | EMA-13=`0.04634` | EMA-20=`0.04614`
  * Intermediate: EMA-34=`0.04593` | EMA-50=`0.04587` | EMA-89=`0.04596` | EMA-100=`0.04600`
  * Institutional: EMA-144=`0.04613` | EMA-200=`0.04621` (Slope: `+0.045%`) | EMA-233=`0.04627` (Slope: `+0.023%`)
  * **Trend Bias**: **`BULLISH`**

---

## 3. Auction Market Structure & Value Profile
*(Sources: 20_Auction_Market_Structure.parquet)*
- **Daily Auction Value Area**:
  * High (VAH): `0.04640` | Point of Control (POC): `0.04490` | Low (VAL): `0.04460`
  * Distance to POC: `+6.66%` | Distance to VAH: `+3.28%` | Distance to VAL: `+7.41%`
  * **Value Area Position**: **`ABOVE_VALUE (Imbalance)`** | **Auction Regime**: **`RANGE_EXPANSION`** | **Session Bias**: **`BULLISH (Above Pivot)`**
- **Prior Day & Weekly Auction Profile**:
  * Prior Day: PD VAH=`0.04750` | PD POC=`0.04690` | PD VAL=`0.04650` | PDH=`0.04790` | PDL=`0.04570` | PDC=`0.04670`
  * Monday Reference: Monday High=`0.04790` | Monday Low=`0.04580` | Monday Mid=`0.04690`
  * Weekly Value Area: Weekly VAH=`0.04700` | Weekly POC=`0.04670` | Weekly VAL=`0.04590`
  * Multi-Week Extremes: Current Week High (CWH)=`0.04790` | CWL=`0.04450` | Prior Week High (PWH)=`0.06140` | PWL=`0.04650`
  * Multi-Month Extremes: Current Month High (CMH)=`0.08670` | CML=`0.04120` | Prior Month High (PMH)=`0.04580` | PML=`0.03130`
- **Session Liquidity Extremes & Initial Balance**:
  * Asian Session: Range `[0.04450 - 0.04710]`
  * London Session: Range `[0.04460 - 0.04690]`
  * New York Session: Range `[0.04550 - 0.04700]`
  * Initial Balance (IB): IB High=`0.04600` | IB Low=`0.04530`
- **Fibonacci Golden Pocket & Optimal Trade Entry (OTE)**:
  * Swing Range: High=`0.04730` | Low=`0.04450` | Direction=`BEARISH_IMPULSE`
  * Golden Pocket [0.618 - 0.65]: `[0.04620 - 0.04630]`
  * Optimal Trade Entry (0.702): `0.04650` | Invalidation Level: `0.04670` | Status: **`STRUCTURE_INVALIDATED`**
- **Classical & Weekly Pivots**:
  * Daily Classical: Pivot=`0.04680` | R1=`0.04780` | S1=`0.04560` | R2=`0.04900` | S2=`0.04460`
  * Weekly Classical: Weekly Pivot=`0.05160` | Weekly R1=`0.05680` | Weekly S1=`0.04190`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Orderflow
*(Sources: 18_CVD.parquet, 18_CVD_30D_5m.parquet, 18_CVD_30D_15m.parquet, 18_CVD_30D_1h.parquet, 18_CVD_30D_4h.parquet, 18_CVD_30D_ALL.parquet, 21_Tradfye_Orderflow.parquet)*
- **Interbank Spot Orderflow Mechanics**: Decentralized OTC market structure. CVD taker deltas do not apply to interbank spot flow. Tape volume governed by broker tick volume with live spread friction of `459.29 bps`.
- **Session Volume Structure**: Price operating at `ABOVE_VALUE (Imbalance)` with Daily POC at `0.04490` (VAH: `0.04640` / VAL: `0.04460`).

---

## 5. Institutional Whale Armor & Resting Orderbook Depth
*(Sources: 10_Whale_Orders.parquet, 12_Hyperdash.parquet, 17_Orderbook.parquet, 4_Hyperliquid_Analysis.parquet)*
- **Interbank Institutional Tier-1 Depth**: Decentralized OTC spot liquidity. Resting whale limit walls from crypto venues do not apply.
- **Verified Broker Armor**: Live Bid `0.04680` / Live Ask `0.04900` with institutional spread of `459.29 bps`. Structural defense anchored at Asian Range `[0.04450 - 0.04710]` and London Range `[0.04460 - 0.04690]`.

---

## 6. Liquidation Max Pain, Heatmaps & Cascade Boundaries
*(Sources: 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 14_Hyperdash_Liq_Map.parquet, 14_Liquidation_Matrix.parquet, 15_Hyperdash_Stops_Map.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **TradFi Structural Liquidity Boundaries**: Centralized perp liquidation feeds do not apply to interbank OTC spot.
- **Stop-Run Cascades & Liquidity Pools**: Primary institutional stop pools reside beyond Classical Pivot extremes (S1: `0.04560` / S2: `0.04460` for long stops; R1: `0.04780` / R2: `0.04900` for short stops) and Asian session extremes `[0.04450 - 0.04710]`.

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
- **Stand-Aside Reason**: Gate 1 Spread Friction Failure: Spread friction 459.29 bps exceeds cap 25.0 bps. Standing aside in 100% cash preserves statutory floor.