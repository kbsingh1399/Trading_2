# 🔬 MASTER 43-FEED QUANTITATIVE DOSSIER: USDCNH (USD/CNH)
**MT5 Symbol**: `USDCNH.pi` | **Category**: `Forex Exotic` | **Tier**: `Tier 3`
**Execution Posture**: `PASSIVE LIMIT ONLY` | **Timestamp**: 2026-10-29 14:43:14 UTC
**Pipeline Clearance**: `QUALIFIED` | **Data Freshness**: `1.2m`

---

## 1. MT5 Live Broker Telemetry & Spread Friction Gate
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet)*
- **Live Bid Quote**: `6.65864` | **Live Ask Quote**: `6.65871` | **Mid Price**: `6.65868`
- **Spread Points**: `7.0 pts` | **Spread BPS**: `0.11 bps` (Mandatory Cap: `5.0 bps`)
- **Gate Status**: **`PASS`** (Spread friction within mandatory threshold; safe for maker execution)
- **Order Allowed**: `BUY_LIMIT / SELL_LIMIT` | **Pillar 1 Clearance**: `QUALIFIED`
- **Broker Specifications**: Contract Size=`1.00` | Tick Value=`1.00 USD` | Min Lot=`0.01` | Digits=`5`
- **Account Capital Context**: Balance=`4,744.55 USD` | Equity=`4,744.32 USD` | Free Margin=`4,342.62 USD` | Inviolate Hard Floor=`4,775.00 USD` (Cushion: `-30.68 USD`)
- **Pipeline Health**: Feed #00 Status=`PASS` | Overall Pipeline Telemetry=`33/33 FEEDS PASS (SYNCHRONIZED)`

---

## 2. Technical Profile, Multi-Sigma VWAP Dispersion & Volatility
*(Sources: 11_Technical.parquet, 11_Technical_BTC_Ribbon.parquet)*
- **Last Verified Price**: `6.65816` | **24h Change**: `-0.08%` (24h High: `6.66524`, 24h Low: `6.65618`)
- **Weekly Range**: Week High=`6.67065` | Week Low=`6.65618` | Daily POC=`6.65870` | Daily VAH=`6.65960` | Daily VAL=`6.65810`
- **Session VWAP**: `6.65912` | **Rolling 24h VWAP**: `6.66073` | **Distance to VWAP**: `-0.01%`
- **VWAP Z-Score**: `-1.05 sigma` | **Mean Reversion Bias**: **`FAIR VALUE`**
- **VWAP Dispersion Bands**:
  * +1.00 sigma: `6.66003` | -1.00 sigma: `6.65820`
  * +1.28 sigma (80% CI): `6.66029` | -1.28 sigma: `6.65795`
  * +2.00 sigma (95% CI): `6.66094` | -2.00 sigma: `6.65729`
  * +2.01 sigma: `6.66095` | -2.01 sigma: `6.65728`
  * +2.51 sigma (98.8% CI): `6.66141` | -2.51 sigma: `6.65682`
  * +3.00 sigma (99.7% CI Extreme): `6.66186` | -3.00 sigma: `6.65637`
- **Oscillators & Volatility**:
  * **RSI (14)**: `41.68` | **RSI State**: **`BEARISH`**
  * **ATR (14)**: `0.00070` | **ATR %**: `0.01%`
  * **Bollinger Bands**: Upper=`6.65940` | Mid=`6.65886` | Lower=`6.65833` | Bandwidth=`0.02%`
  * **MACD**: Line=`-0.0001` | Signal=`-0.0001` | Hist=`-0.0000`
- **Exponential Moving Average Ribbon (EMA)**:
  * Short Horizon: EMA-5=`6.65861` | EMA-9=`6.65870` | EMA-13=`6.65874` | EMA-20=`6.65878`
  * Intermediate: EMA-34=`6.65891` | EMA-50=`6.65919` | EMA-89=`6.66010` | EMA-100=`6.66036`
  * Institutional: EMA-144=`6.66133` | EMA-200=`6.66231` (Slope: `-0.007%`) | EMA-233=`6.66291` (Slope: `-0.007%`)
  * **Trend Bias**: **`STRONG BEARISH`**

---

## 3. Auction Market Structure & Value Profile
*(Sources: 20_Auction_Market_Structure.parquet)*
- **Daily Auction Value Area**:
  * High (VAH): `6.65960` | Point of Control (POC): `6.65870` | Low (VAL): `6.65810`
  * Distance to POC: `+0.00%` | Distance to VAH: `-0.01%` | Distance to VAL: `+0.01%`
  * **Value Area Position**: **`INSIDE_VALUE (Balance)`** | **Auction Regime**: **`ROTATIONAL_BALANCE`** | **Session Bias**: **`BEARISH (Below Pivot)`**
- **Prior Day & Weekly Auction Profile**:
  * Prior Day: PD VAH=`6.66540` | PD POC=`6.66330` | PD VAL=`6.66170` | PDH=`6.66750` | PDL=`6.66060` | PDC=`6.66090`
  * Monday Reference: Monday High=`6.66970` | Monday Low=`6.66690` | Monday Mid=`6.66830`
  * Weekly Value Area: Weekly VAH=`6.66930` | Weekly POC=`6.66820` | Weekly VAL=`6.66200`
  * Multi-Week Extremes: Current Week High (CWH)=`6.67070` | CWL=`6.65620` | Prior Week High (PWH)=`6.68540` | PWL=`6.66800`
  * Multi-Month Extremes: Current Month High (CMH)=`6.72220` | CML=`6.65620` | Prior Month High (PMH)=`6.72670` | PML=`6.69110`
- **Session Liquidity Extremes & Initial Balance**:
  * Asian Session: Range `[6.65800 - 6.66260]`
  * London Session: Range `[6.65620 - 6.65970]`
  * New York Session: Range `[6.65780 - 6.65970]`
  * Initial Balance (IB): IB High=`6.65870` | IB Low=`6.65810`
- **Fibonacci Golden Pocket & Optimal Trade Entry (OTE)**:
  * Swing Range: High=`6.66520` | Low=`6.65620` | Direction=`BEARISH_IMPULSE`
  * Golden Pocket [0.618 - 0.65]: `[6.66180 - 6.66210]`
  * Optimal Trade Entry (0.702): `6.66250` | Invalidation Level: `6.66330` | Status: **`SHALLOW_RETRACE`**
- **Classical & Weekly Pivots**:
  * Daily Classical: Pivot=`6.66300` | R1=`6.66540` | S1=`6.65850` | R2=`6.66990` | S2=`6.65610`
  * Weekly Classical: Weekly Pivot=`6.67410` | Weekly R1=`6.68020` | Weekly S1=`6.66290`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Orderflow
*(Sources: 18_CVD.parquet, 18_CVD_30D_5m.parquet, 18_CVD_30D_15m.parquet, 18_CVD_30D_1h.parquet, 18_CVD_30D_4h.parquet, 18_CVD_30D_ALL.parquet, 21_Tradfye_Orderflow.parquet)*
- **Interbank Spot Orderflow Mechanics**: Decentralized OTC market structure. CVD taker deltas do not apply to interbank spot flow. Tape volume governed by broker tick volume with live spread friction of `0.11 bps`.
- **Session Volume Structure**: Price operating at `INSIDE_VALUE (Balance)` with Daily POC at `6.65870` (VAH: `6.65960` / VAL: `6.65810`).

---

## 5. Institutional Whale Armor & Resting Orderbook Depth
*(Sources: 10_Whale_Orders.parquet, 12_Hyperdash.parquet, 17_Orderbook.parquet, 4_Hyperliquid_Analysis.parquet)*
- **Interbank Institutional Tier-1 Depth**: Decentralized OTC spot liquidity. Resting whale limit walls from crypto venues do not apply.
- **Verified Broker Armor**: Live Bid `6.65864` / Live Ask `6.65871` with institutional spread of `0.11 bps`. Structural defense anchored at Asian Range `[6.65800 - 6.66260]` and London Range `[6.65620 - 6.65970]`.

---

## 6. Liquidation Max Pain, Heatmaps & Cascade Boundaries
*(Sources: 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 14_Hyperdash_Liq_Map.parquet, 14_Liquidation_Matrix.parquet, 15_Hyperdash_Stops_Map.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **TradFi Structural Liquidity Boundaries**: Centralized perp liquidation feeds do not apply to interbank OTC spot.
- **Stop-Run Cascades & Liquidity Pools**: Primary institutional stop pools reside beyond Classical Pivot extremes (S1: `6.65850` / S2: `6.65610` for long stops; R1: `6.66540` / R2: `6.66990` for short stops) and Asian session extremes `[6.65800 - 6.66260]`.

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