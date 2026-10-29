# 🔬 MASTER 43-FEED QUANTITATIVE DOSSIER: DSHUSD (DSH/USD)
**MT5 Symbol**: `DSHUSD.p` | **Category**: `Forex Cross` | **Tier**: `Tier 2`
**Execution Posture**: `PASSIVE LIMIT ONLY` | **Timestamp**: 2026-10-29 14:43:14 UTC
**Pipeline Clearance**: `QUALIFIED` | **Data Freshness**: `1.2m`

---

## 1. MT5 Live Broker Telemetry & Spread Friction Gate
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet)*
- **Live Bid Quote**: `50.44500` | **Live Ask Quote**: `50.49900` | **Mid Price**: `50.47200`
- **Spread Points**: `54.0 pts` | **Spread BPS**: `10.70 bps` (Mandatory Cap: `25.0 bps`)
- **Gate Status**: **`PASS`** (Spread friction within mandatory threshold; safe for maker execution)
- **Order Allowed**: `BUY_LIMIT / SELL_LIMIT` | **Pillar 1 Clearance**: `QUALIFIED`
- **Broker Specifications**: Contract Size=`1.00` | Tick Value=`1.00 USD` | Min Lot=`0.01` | Digits=`5`
- **Account Capital Context**: Balance=`4,744.55 USD` | Equity=`4,744.32 USD` | Free Margin=`4,342.62 USD` | Inviolate Hard Floor=`4,775.00 USD` (Cushion: `-30.68 USD`)
- **Pipeline Health**: Feed #00 Status=`PASS` | Overall Pipeline Telemetry=`33/33 FEEDS PASS (SYNCHRONIZED)`

---

## 2. Technical Profile, Multi-Sigma VWAP Dispersion & Volatility
*(Sources: 11_Technical.parquet, 11_Technical_BTC_Ribbon.parquet)*
- **Last Verified Price**: `50.47400` | **24h Change**: `-4.57%` (24h High: `54.17200`, 24h Low: `49.89100`)
- **Weekly Range**: Week High=`55.83500` | Week Low=`49.89100` | Daily POC=`50.39000` | Daily VAH=`51.98900` | Daily VAL=`49.99100`
- **Session VWAP**: `51.22253` | **Rolling 24h VWAP**: `52.08373` | **Distance to VWAP**: `-1.46%`
- **VWAP Z-Score**: `-0.79 sigma` | **Mean Reversion Bias**: **`FAIR VALUE`**
- **VWAP Dispersion Bands**:
  * +1.00 sigma: `52.16629` | -1.00 sigma: `50.27877`
  * +1.28 sigma (80% CI): `52.43054` | -1.28 sigma: `50.01452`
  * +2.00 sigma (95% CI): `53.11005` | -2.00 sigma: `49.33501`
  * +2.01 sigma: `53.11949` | -2.01 sigma: `49.32558`
  * +2.51 sigma (98.8% CI): `53.59137` | -2.51 sigma: `48.85370`
  * +3.00 sigma (99.7% CI Extreme): `54.05381` | -3.00 sigma: `48.39126`
- **Oscillators & Volatility**:
  * **RSI (14)**: `47.63` | **RSI State**: **`NEUTRAL`**
  * **ATR (14)**: `0.32585` | **ATR %**: `0.65%`
  * **Bollinger Bands**: Upper=`50.80535` | Mid=`50.39165` | Lower=`49.97795` | Bandwidth=`1.64%`
  * **MACD**: Line=`-0.2119` | Signal=`-0.2654` | Hist=`+0.0535`
- **Exponential Moving Average Ribbon (EMA)**:
  * Short Horizon: EMA-5=`50.31936` | EMA-9=`50.31062` | EMA-13=`50.34140` | EMA-20=`50.43596`
  * Intermediate: EMA-34=`50.70651` | EMA-50=`51.04178` | EMA-89=`51.71998` | EMA-100=`51.86780`
  * Institutional: EMA-144=`52.29389` | EMA-200=`52.64015` (Slope: `-0.562%`) | EMA-233=`52.83831` (Slope: `-0.517%`)
  * **Trend Bias**: **`NEUTRAL / CHOP`**

---

## 3. Auction Market Structure & Value Profile
*(Sources: 20_Auction_Market_Structure.parquet)*
- **Daily Auction Value Area**:
  * High (VAH): `51.98900` | Point of Control (POC): `50.39000` | Low (VAL): `49.99100`
  * Distance to POC: `+0.23%` | Distance to VAH: `-2.85%` | Distance to VAL: `+1.03%`
  * **Value Area Position**: **`INSIDE_VALUE (Balance)`** | **Auction Regime**: **`ROTATIONAL_BALANCE`** | **Session Bias**: **`BEARISH (Below Pivot)`**
- **Prior Day & Weekly Auction Profile**:
  * Prior Day: PD VAH=`54.77400` | PD POC=`53.22500` | PD VAL=`52.82200` | PDH=`55.67000` | PDL=`52.65100` | PDC=`53.85900`
  * Monday Reference: Monday High=`53.38900` | Monday Low=`50.00300` | Monday Mid=`51.69600`
  * Weekly Value Area: Weekly VAH=`55.30000` | Weekly POC=`54.98300` | Weekly VAL=`51.81300`
  * Multi-Week Extremes: Current Week High (CWH)=`55.83500` | CWL=`49.89100` | Prior Week High (PWH)=`55.91400` | PWL=`46.69100`
  * Multi-Month Extremes: Current Month High (CMH)=`60.94300` | CML=`45.64700` | Prior Month High (PMH)=`78.66800` | PML=`41.08000`
- **Session Liquidity Extremes & Initial Balance**:
  * Asian Session: Range `[50.81100 - 54.17200]`
  * London Session: Range `[49.89100 - 51.92200]`
  * New York Session: Range `[49.89100 - 50.83400]`
  * Initial Balance (IB): IB High=`51.92200` | IB Low=`51.15000`
- **Fibonacci Golden Pocket & Optimal Trade Entry (OTE)**:
  * Swing Range: High=`54.17200` | Low=`49.89100` | Direction=`BEARISH_IMPULSE`
  * Golden Pocket [0.618 - 0.65]: `[52.53700 - 52.67400]`
  * Optimal Trade Entry (0.702): `52.89600` | Invalidation Level: `53.25600` | Status: **`SHALLOW_RETRACE`**
- **Classical & Weekly Pivots**:
  * Daily Classical: Pivot=`54.06000` | R1=`55.46900` | S1=`52.45000` | R2=`57.07900` | S2=`51.04100`
  * Weekly Classical: Weekly Pivot=`51.46200` | Weekly R1=`56.23400` | Weekly S1=`47.01100`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Orderflow
*(Sources: 18_CVD.parquet, 18_CVD_30D_5m.parquet, 18_CVD_30D_15m.parquet, 18_CVD_30D_1h.parquet, 18_CVD_30D_4h.parquet, 18_CVD_30D_ALL.parquet, 21_Tradfye_Orderflow.parquet)*
- **Interbank Spot Orderflow Mechanics**: Decentralized OTC market structure. CVD taker deltas do not apply to interbank spot flow. Tape volume governed by broker tick volume with live spread friction of `10.70 bps`.
- **Session Volume Structure**: Price operating at `INSIDE_VALUE (Balance)` with Daily POC at `50.39000` (VAH: `51.98900` / VAL: `49.99100`).

---

## 5. Institutional Whale Armor & Resting Orderbook Depth
*(Sources: 10_Whale_Orders.parquet, 12_Hyperdash.parquet, 17_Orderbook.parquet, 4_Hyperliquid_Analysis.parquet)*
- **Interbank Institutional Tier-1 Depth**: Decentralized OTC spot liquidity. Resting whale limit walls from crypto venues do not apply.
- **Verified Broker Armor**: Live Bid `50.44500` / Live Ask `50.49900` with institutional spread of `10.70 bps`. Structural defense anchored at Asian Range `[50.81100 - 54.17200]` and London Range `[49.89100 - 51.92200]`.

---

## 6. Liquidation Max Pain, Heatmaps & Cascade Boundaries
*(Sources: 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 14_Hyperdash_Liq_Map.parquet, 14_Liquidation_Matrix.parquet, 15_Hyperdash_Stops_Map.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **TradFi Structural Liquidity Boundaries**: Centralized perp liquidation feeds do not apply to interbank OTC spot.
- **Stop-Run Cascades & Liquidity Pools**: Primary institutional stop pools reside beyond Classical Pivot extremes (S1: `52.45000` / S2: `51.04100` for long stops; R1: `55.46900` / R2: `57.07900` for short stops) and Asian session extremes `[50.81100 - 54.17200]`.

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
- **Stand-Aside Reason**: Absence of statistically validated auction edge and defending resting armor. Standing aside preserves statutory hard floor.