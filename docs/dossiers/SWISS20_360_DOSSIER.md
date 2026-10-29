# 🔬 MASTER 43-FEED QUANTITATIVE DOSSIER: SWISS20 (Swiss Market Index 20)
**MT5 Symbol**: `SWISS20.p` | **Category**: `Equity Index` | **Tier**: `Tier 2`
**Execution Posture**: `PASSIVE LIMIT ONLY` | **Timestamp**: 2026-10-29 14:43:14 UTC
**Pipeline Clearance**: `QUALIFIED` | **Data Freshness**: `1.2m`

---

## 1. MT5 Live Broker Telemetry & Spread Friction Gate
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet)*
- **Live Bid Quote**: `14788.00000` | **Live Ask Quote**: `14792.00000` | **Mid Price**: `14790.00000`
- **Spread Points**: `400.0 pts` | **Spread BPS**: `2.70 bps` (Mandatory Cap: `5.0 bps`)
- **Gate Status**: **`PASS`** (Spread friction within mandatory threshold; safe for maker execution)
- **Order Allowed**: `BUY_LIMIT / SELL_LIMIT` | **Pillar 1 Clearance**: `QUALIFIED`
- **Broker Specifications**: Contract Size=`1.00` | Tick Value=`1.00 USD` | Min Lot=`0.01` | Digits=`5`
- **Account Capital Context**: Balance=`4,744.55 USD` | Equity=`4,744.32 USD` | Free Margin=`4,342.62 USD` | Inviolate Hard Floor=`4,775.00 USD` (Cushion: `-30.68 USD`)
- **Pipeline Health**: Feed #00 Status=`PASS` | Overall Pipeline Telemetry=`33/33 FEEDS PASS (SYNCHRONIZED)`

---

## 2. Technical Profile, Multi-Sigma VWAP Dispersion & Volatility
*(Sources: 11_Technical.parquet, 11_Technical_BTC_Ribbon.parquet)*
- **Last Verified Price**: `14840.50000` | **24h Change**: `+1.97%` (24h High: `14872.50000`, 24h Low: `14536.50000`)
- **Weekly Range**: Week High=`14872.50000` | Week Low=`14466.50000` | Daily POC=`14746.35000` | Daily VAH=`14871.51000` | Daily VAL=`14688.73000`
- **Session VWAP**: `14732.08674` | **Rolling 24h VWAP**: `14670.55249` | **Distance to VWAP**: `+0.74%`
- **VWAP Z-Score**: `+1.29 sigma` | **Mean Reversion Bias**: **`FAIR VALUE`**
- **VWAP Dispersion Bands**:
  * +1.00 sigma: `14816.29532` | -1.00 sigma: `14647.87816`
  * +1.28 sigma (80% CI): `14839.87373` | -1.28 sigma: `14624.29976`
  * +2.00 sigma (95% CI): `14900.50391` | -2.00 sigma: `14563.66958`
  * +2.01 sigma: `14901.34599` | -2.01 sigma: `14562.82749`
  * +2.51 sigma (98.8% CI): `14943.45028` | -2.51 sigma: `14520.72320`
  * +3.00 sigma (99.7% CI Extreme): `14984.71249` | -3.00 sigma: `14479.46099`
- **Oscillators & Volatility**:
  * **RSI (14)**: `77.13` | **RSI State**: **`OVERBOUGHT`**
  * **ATR (14)**: `23.71077` | **ATR %**: `0.16%`
  * **Bollinger Bands**: Upper=`14843.14026` | Mid=`14776.77500` | Lower=`14710.40974` | Bandwidth=`0.90%`
  * **MACD**: Line=`+41.5423` | Signal=`+38.8827` | Hist=`+2.6596`
- **Exponential Moving Average Ribbon (EMA)**:
  * Short Horizon: EMA-5=`14825.12450` | EMA-9=`14809.98784` | EMA-13=`14796.61233` | EMA-20=`14774.93819`
  * Intermediate: EMA-34=`14739.35869` | EMA-50=`14710.57631` | EMA-89=`14669.79158` | EMA-100=`14662.17425`
  * Institutional: EMA-144=`14638.02123` | EMA-200=`14617.74090` (Slope: `+0.156%`) | EMA-233=`14607.88605` (Slope: `+0.140%`)
  * **Trend Bias**: **`STRONG BULLISH`**

---

## 3. Auction Market Structure & Value Profile
*(Sources: 20_Auction_Market_Structure.parquet)*
- **Daily Auction Value Area**:
  * High (VAH): `14871.51000` | Point of Control (POC): `14746.35000` | Low (VAL): `14688.73000`
  * Distance to POC: `+0.28%` | Distance to VAH: `-0.56%` | Distance to VAL: `+0.68%`
  * **Value Area Position**: **`INSIDE_VALUE (Balance)`** | **Auction Regime**: **`ROTATIONAL_BALANCE`** | **Session Bias**: **`BULLISH (Above Pivot)`**
- **Prior Day & Weekly Auction Profile**:
  * Prior Day: PD VAH=`14619.83000` | PD POC=`14600.95000` | PD VAL=`14555.44000` | PDH=`14667.00000` | PDL=`14500.50000` | PDC=`14610.50000`
  * Monday Reference: Monday High=`14552.00000` | Monday Low=`14452.00000` | Monday Mid=`14502.00000`
  * Weekly Value Area: Weekly VAH=`14616.00000` | Weekly POC=`14596.37000` | Weekly VAL=`14498.25000`
  * Multi-Week Extremes: Current Week High (CWH)=`14872.50000` | CWL=`14452.00000` | Prior Week High (PWH)=`14616.00000` | PWL=`14300.50000`
  * Multi-Month Extremes: Current Month High (CMH)=`14872.50000` | CML=`13589.90000` | Prior Month High (PMH)=`14464.50000` | PML=`13695.40000`
- **Session Liquidity Extremes & Initial Balance**:
  * Asian Session: Range `[14574.50000 - 14616.50000]`
  * London Session: Range `[14594.50000 - 14818.00000]`
  * New York Session: Range `[14738.00000 - 14872.50000]`
  * Initial Balance (IB): IB High=`14633.50000` | IB Low=`14606.50000`
- **Fibonacci Golden Pocket & Optimal Trade Entry (OTE)**:
  * Swing Range: High=`14872.50000` | Low=`14536.50000` | Direction=`BULLISH_IMPULSE`
  * Golden Pocket [0.618 - 0.65]: `[14654.10000 - 14664.85000]`
  * Optimal Trade Entry (0.702): `14636.63000` | Invalidation Level: `14608.40000` | Status: **`SHALLOW_RETRACE`**
- **Classical & Weekly Pivots**:
  * Daily Classical: Pivot=`14592.67000` | R1=`14684.83000` | S1=`14518.33000` | R2=`14759.17000` | S2=`14426.17000`
  * Weekly Classical: Weekly Pivot=`14465.50000` | Weekly R1=`14630.50000` | Weekly S1=`14315.00000`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Orderflow
*(Sources: 18_CVD.parquet, 18_CVD_30D_5m.parquet, 18_CVD_30D_15m.parquet, 18_CVD_30D_1h.parquet, 18_CVD_30D_4h.parquet, 18_CVD_30D_ALL.parquet, 21_Tradfye_Orderflow.parquet)*
- **Interbank Spot Orderflow Mechanics**: Decentralized OTC market structure. CVD taker deltas do not apply to interbank spot flow. Tape volume governed by broker tick volume with live spread friction of `2.70 bps`.
- **Session Volume Structure**: Price operating at `INSIDE_VALUE (Balance)` with Daily POC at `14746.35000` (VAH: `14871.51000` / VAL: `14688.73000`).

---

## 5. Institutional Whale Armor & Resting Orderbook Depth
*(Sources: 10_Whale_Orders.parquet, 12_Hyperdash.parquet, 17_Orderbook.parquet, 4_Hyperliquid_Analysis.parquet)*
- **Interbank Institutional Tier-1 Depth**: Decentralized OTC spot liquidity. Resting whale limit walls from crypto venues do not apply.
- **Verified Broker Armor**: Live Bid `14788.00000` / Live Ask `14792.00000` with institutional spread of `2.70 bps`. Structural defense anchored at Asian Range `[14574.50000 - 14616.50000]` and London Range `[14594.50000 - 14818.00000]`.

---

## 6. Liquidation Max Pain, Heatmaps & Cascade Boundaries
*(Sources: 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 14_Hyperdash_Liq_Map.parquet, 14_Liquidation_Matrix.parquet, 15_Hyperdash_Stops_Map.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **TradFi Structural Liquidity Boundaries**: Centralized perp liquidation feeds do not apply to interbank OTC spot.
- **Stop-Run Cascades & Liquidity Pools**: Primary institutional stop pools reside beyond Classical Pivot extremes (S1: `14518.33000` / S2: `14426.17000` for long stops; R1: `14684.83000` / R2: `14759.17000` for short stops) and Asian session extremes `[14574.50000 - 14616.50000]`.

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