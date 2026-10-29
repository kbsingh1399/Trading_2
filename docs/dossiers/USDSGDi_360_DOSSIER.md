# 🔬 MASTER 43-FEED QUANTITATIVE DOSSIER: USDSGD (USD/SGD)
**MT5 Symbol**: `USDSGD.pi` | **Category**: `Forex Exotic` | **Tier**: `Tier 3`
**Execution Posture**: `PASSIVE LIMIT ONLY` | **Timestamp**: 2026-10-29 14:43:14 UTC
**Pipeline Clearance**: `QUALIFIED` | **Data Freshness**: `1.2m`

---

## 1. MT5 Live Broker Telemetry & Spread Friction Gate
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet)*
- **Live Bid Quote**: `1.28133` | **Live Ask Quote**: `1.28138` | **Mid Price**: `1.28136`
- **Spread Points**: `5.0 pts` | **Spread BPS**: `0.39 bps` (Mandatory Cap: `5.0 bps`)
- **Gate Status**: **`PASS`** (Spread friction within mandatory threshold; safe for maker execution)
- **Order Allowed**: `BUY_LIMIT / SELL_LIMIT` | **Pillar 1 Clearance**: `QUALIFIED`
- **Broker Specifications**: Contract Size=`1.00` | Tick Value=`1.00 USD` | Min Lot=`0.01` | Digits=`5`
- **Account Capital Context**: Balance=`4,744.55 USD` | Equity=`4,744.32 USD` | Free Margin=`4,342.62 USD` | Inviolate Hard Floor=`4,775.00 USD` (Cushion: `-30.68 USD`)
- **Pipeline Health**: Feed #00 Status=`PASS` | Overall Pipeline Telemetry=`33/33 FEEDS PASS (SYNCHRONIZED)`

---

## 2. Technical Profile, Multi-Sigma VWAP Dispersion & Volatility
*(Sources: 11_Technical.parquet, 11_Technical_BTC_Ribbon.parquet)*
- **Last Verified Price**: `1.28118` | **24h Change**: `-0.12%` (24h High: `1.28369`, 24h Low: `1.27936`)
- **Weekly Range**: Week High=`1.28369` | Week Low=`1.27892` | Daily POC=`1.28117` | Daily VAH=`1.28170` | Daily VAL=`1.28044`
- **Session VWAP**: `1.28103` | **Rolling 24h VWAP**: `1.28142` | **Distance to VWAP**: `+0.01%`
- **VWAP Z-Score**: `+0.28 sigma` | **Mean Reversion Bias**: **`FAIR VALUE`**
- **VWAP Dispersion Bands**:
  * +1.00 sigma: `1.28156` | -1.00 sigma: `1.28051`
  * +1.28 sigma (80% CI): `1.28170` | -1.28 sigma: `1.28036`
  * +2.00 sigma (95% CI): `1.28208` | -2.00 sigma: `1.27998`
  * +2.01 sigma: `1.28209` | -2.01 sigma: `1.27997`
  * +2.51 sigma (98.8% CI): `1.28235` | -2.51 sigma: `1.27971`
  * +3.00 sigma (99.7% CI Extreme): `1.28261` | -3.00 sigma: `1.27945`
- **Oscillators & Volatility**:
  * **RSI (14)**: `48.45` | **RSI State**: **`NEUTRAL`**
  * **ATR (14)**: `0.00043` | **ATR %**: `0.03%`
  * **Bollinger Bands**: Upper=`1.28177` | Mid=`1.28132` | Lower=`1.28087` | Bandwidth=`0.07%`
  * **MACD**: Line=`+0.0002` | Signal=`+0.0002` | Hist=`-0.0000`
- **Exponential Moving Average Ribbon (EMA)**:
  * Short Horizon: EMA-5=`1.28145` | EMA-9=`1.28144` | EMA-13=`1.28140` | EMA-20=`1.28131`
  * Intermediate: EMA-34=`1.28120` | EMA-50=`1.28116` | EMA-89=`1.28121` | EMA-100=`1.28123`
  * Institutional: EMA-144=`1.28126` | EMA-200=`1.28120` (Slope: `+0.002%`) | EMA-233=`1.28115` (Slope: `+0.002%`)
  * **Trend Bias**: **`NEUTRAL / CHOP`**

---

## 3. Auction Market Structure & Value Profile
*(Sources: 20_Auction_Market_Structure.parquet)*
- **Daily Auction Value Area**:
  * High (VAH): `1.28170` | Point of Control (POC): `1.28117` | Low (VAL): `1.28044`
  * Distance to POC: `+0.00%` | Distance to VAH: `+0.00%` | Distance to VAL: `+0.00%`
  * **Value Area Position**: **`INSIDE_VALUE (Balance)`** | **Auction Regime**: **`BALANCED_AUCTION`** | **Session Bias**: **`NEUTRAL`**
- **Prior Day & Weekly Auction Profile**:
  * Prior Day: PD VAH=`1.28648` | PD POC=`1.28136` | PD VAL=`1.27623` | PDH=`1.28904` | PDL=`1.27367` | PDC=`1.28136`
  * Monday Reference: Monday High=`1.28776` | Monday Low=`1.27495` | Monday Mid=`1.28136`
  * Weekly Value Area: Weekly VAH=`1.29161` | Weekly POC=`1.28136` | Weekly VAL=`1.27110`
  * Multi-Week Extremes: Current Week High (CWH)=`1.29417` | CWL=`1.26854` | Prior Week High (PWH)=`1.30058` | PWL=`1.26213`
  * Multi-Month Extremes: Current Month High (CMH)=`1.30698` | CML=`1.25573` | Prior Month High (PMH)=`1.31339` | PML=`1.24932`
- **Session Liquidity Extremes & Initial Balance**:
  * Asian Session: Range `[1.27879 - 1.28392]`
  * London Session: Range `[1.27623 - 1.28648]`
  * New York Session: Range `[1.27495 - 1.28776]`
  * Initial Balance (IB): IB High=`1.28520` | IB Low=`1.27751`
- **Fibonacci Golden Pocket & Optimal Trade Entry (OTE)**:
  * Swing Range: High=`1.28369` | Low=`1.27936` | Direction=`NONE`
  * Golden Pocket [0.618 - 0.65]: `[1.27879 - 1.28392]`
  * Optimal Trade Entry (0.702): `1.28136` | Invalidation Level: `0.00000` | Status: **`NONE`**
- **Classical & Weekly Pivots**:
  * Daily Classical: Pivot=`1.28136` | R1=`1.28520` | S1=`1.27751` | R2=`1.28904` | S2=`1.27367`
  * Weekly Classical: Weekly Pivot=`1.28136` | Weekly R1=`1.29417` | Weekly S1=`1.26854`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Orderflow
*(Sources: 18_CVD.parquet, 18_CVD_30D_5m.parquet, 18_CVD_30D_15m.parquet, 18_CVD_30D_1h.parquet, 18_CVD_30D_4h.parquet, 18_CVD_30D_ALL.parquet, 21_Tradfye_Orderflow.parquet)*
- **Interbank Spot Orderflow Mechanics**: Decentralized OTC market structure. CVD taker deltas do not apply to interbank spot flow. Tape volume governed by broker tick volume with live spread friction of `0.39 bps`.
- **Session Volume Structure**: Price operating at `INSIDE_VALUE (Balance)` with Daily POC at `1.28117` (VAH: `1.28170` / VAL: `1.28044`).

---

## 5. Institutional Whale Armor & Resting Orderbook Depth
*(Sources: 10_Whale_Orders.parquet, 12_Hyperdash.parquet, 17_Orderbook.parquet, 4_Hyperliquid_Analysis.parquet)*
- **Interbank Institutional Tier-1 Depth**: Decentralized OTC spot liquidity. Resting whale limit walls from crypto venues do not apply.
- **Verified Broker Armor**: Live Bid `1.28133` / Live Ask `1.28138` with institutional spread of `0.39 bps`. Structural defense anchored at Asian Range `[1.27879 - 1.28392]` and London Range `[1.27623 - 1.28648]`.

---

## 6. Liquidation Max Pain, Heatmaps & Cascade Boundaries
*(Sources: 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 14_Hyperdash_Liq_Map.parquet, 14_Liquidation_Matrix.parquet, 15_Hyperdash_Stops_Map.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **TradFi Structural Liquidity Boundaries**: Centralized perp liquidation feeds do not apply to interbank OTC spot.
- **Stop-Run Cascades & Liquidity Pools**: Primary institutional stop pools reside beyond Classical Pivot extremes (S1: `1.27751` / S2: `1.27367` for long stops; R1: `1.28520` / R2: `1.28904` for short stops) and Asian session extremes `[1.27879 - 1.28392]`.

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
- **Stand-Aside Reason**: Absence of statistically validated auction edge and defending resting armor. Standing aside preserves statutory hard floor.