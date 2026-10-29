# 🔬 MASTER 43-FEED QUANTITATIVE DOSSIER: JP225 (Nikkei 225 Index)
**MT5 Symbol**: `JP225.p` | **Category**: `Equity Index` | **Tier**: `Tier 1`
**Execution Posture**: `PASSIVE LIMIT ONLY` | **Timestamp**: 2026-10-29 14:43:14 UTC
**Pipeline Clearance**: `QUALIFIED` | **Data Freshness**: `1.2m`

---

## 1. MT5 Live Broker Telemetry & Spread Friction Gate
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet)*
- **Live Bid Quote**: `64469.50000` | **Live Ask Quote**: `64475.50000` | **Mid Price**: `64472.50000`
- **Spread Points**: `600.0 pts` | **Spread BPS**: `0.93 bps` (Mandatory Cap: `5.0 bps`)
- **Gate Status**: **`PASS`** (Spread friction within mandatory threshold; safe for maker execution)
- **Order Allowed**: `BUY_LIMIT / SELL_LIMIT` | **Pillar 1 Clearance**: `QUALIFIED`
- **Broker Specifications**: Contract Size=`1.00` | Tick Value=`1.00 USD` | Min Lot=`0.01` | Digits=`5`
- **Account Capital Context**: Balance=`4,744.55 USD` | Equity=`4,744.32 USD` | Free Margin=`4,342.62 USD` | Inviolate Hard Floor=`4,775.00 USD` (Cushion: `-30.68 USD`)
- **Pipeline Health**: Feed #00 Status=`PASS` | Overall Pipeline Telemetry=`33/33 FEEDS PASS (SYNCHRONIZED)`

---

## 2. Technical Profile, Multi-Sigma VWAP Dispersion & Volatility
*(Sources: 11_Technical.parquet, 11_Technical_BTC_Ribbon.parquet)*
- **Last Verified Price**: `64469.50000` | **24h Change**: `+0.19%` (24h High: `65372.50000`, 24h Low: `63759.00000`)
- **Weekly Range**: Week High=`65372.50000` | Week Low=`62138.50000` | Daily POC=`64565.70000` | Daily VAH=`64808.80000` | Daily VAL=`64285.70000`
- **Session VWAP**: `64453.76396` | **Rolling 24h VWAP**: `64464.15973` | **Distance to VWAP**: `+0.02%`
- **VWAP Z-Score**: `+0.07 sigma` | **Mean Reversion Bias**: **`FAIR VALUE`**
- **VWAP Dispersion Bands**:
  * +1.00 sigma: `64688.73359` | -1.00 sigma: `64218.79433`
  * +1.28 sigma (80% CI): `64754.52509` | -1.28 sigma: `64153.00283`
  * +2.00 sigma (95% CI): `64923.70323` | -2.00 sigma: `63983.82470`
  * +2.01 sigma: `64926.05292` | -2.01 sigma: `63981.47500`
  * +2.51 sigma (98.8% CI): `65043.53774` | -2.51 sigma: `63863.99019`
  * +3.00 sigma (99.7% CI Extreme): `65158.67286` | -3.00 sigma: `63748.85507`
- **Oscillators & Volatility**:
  * **RSI (14)**: `43.74` | **RSI State**: **`BEARISH`**
  * **ATR (14)**: `192.94670` | **ATR %**: `0.30%`
  * **Bollinger Bands**: Upper=`64865.99854` | Mid=`64668.07500` | Lower=`64470.15146` | Bandwidth=`0.61%`
  * **MACD**: Line=`+8.9188` | Signal=`+37.0786` | Hist=`-28.1598`
- **Exponential Moving Average Ribbon (EMA)**:
  * Short Horizon: EMA-5=`64575.15788` | EMA-9=`64609.35800` | EMA-13=`64622.25271` | EMA-20=`64621.98208`
  * Intermediate: EMA-34=`64592.79895` | EMA-50=`64555.60340` | EMA-89=`64471.27397` | EMA-100=`64445.52960`
  * Institutional: EMA-144=`64319.06125` | EMA-200=`64142.48513` (Slope: `+0.099%`) | EMA-233=`64030.61357` (Slope: `+0.104%`)
  * **Trend Bias**: **`NEUTRAL / CHOP`**

---

## 3. Auction Market Structure & Value Profile
*(Sources: 20_Auction_Market_Structure.parquet)*
- **Daily Auction Value Area**:
  * High (VAH): `64808.80000` | Point of Control (POC): `64565.70000` | Low (VAL): `64285.70000`
  * Distance to POC: `-0.14%` | Distance to VAH: `-0.52%` | Distance to VAL: `+0.29%`
  * **Value Area Position**: **`INSIDE_VALUE (Balance)`** | **Auction Regime**: **`ROTATIONAL_BALANCE`** | **Session Bias**: **`BULLISH (Above Pivot)`**
- **Prior Day & Weekly Auction Profile**:
  * Prior Day: PD VAH=`64598.90000` | PD POC=`64505.50000` | PD VAL=`64235.50000` | PDH=`65372.50000` | PDL=`63815.00000` | PDC=`64216.50000`
  * Monday Reference: Monday High=`63168.50000` | Monday Low=`62010.00000` | Monday Mid=`62589.20000`
  * Weekly Value Area: Weekly VAH=`64845.70000` | Weekly POC=`64509.50000` | Weekly VAL=`63343.80000`
  * Multi-Week Extremes: Current Week High (CWH)=`65372.50000` | CWL=`62010.00000` | Prior Week High (PWH)=`65404.00000` | PWL=`61484.00000`
  * Multi-Month Extremes: Current Month High (CMH)=`71332.50000` | CML=`61484.00000` | Prior Month High (PMH)=`67623.50000` | PML=`62717.00000`
- **Session Liquidity Extremes & Initial Balance**:
  * Asian Session: Range `[63759.00000 - 64783.00000]`
  * London Session: Range `[64224.50000 - 64864.00000]`
  * New York Session: Range `[64236.50000 - 64864.00000]`
  * Initial Balance (IB): IB High=`64849.00000` | IB Low=`64467.00000`
- **Fibonacci Golden Pocket & Optimal Trade Entry (OTE)**:
  * Swing Range: High=`65372.50000` | Low=`63759.00000` | Direction=`BEARISH_IMPULSE`
  * Golden Pocket [0.618 - 0.65]: `[64756.10000 - 64807.80000]`
  * Optimal Trade Entry (0.702): `64891.70000` | Invalidation Level: `65027.20000` | Status: **`SHALLOW_RETRACE`**
- **Classical & Weekly Pivots**:
  * Daily Classical: Pivot=`64468.00000` | R1=`65121.00000` | S1=`63563.50000` | R2=`66025.50000` | S2=`62910.50000`
  * Weekly Classical: Weekly Pivot=`63139.00000` | Weekly R1=`64794.00000` | Weekly S1=`60874.00000`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Orderflow
*(Sources: 18_CVD.parquet, 18_CVD_30D_5m.parquet, 18_CVD_30D_15m.parquet, 18_CVD_30D_1h.parquet, 18_CVD_30D_4h.parquet, 18_CVD_30D_ALL.parquet, 21_Tradfye_Orderflow.parquet)*
- **Interbank Spot Orderflow Mechanics**: Decentralized OTC market structure. CVD taker deltas do not apply to interbank spot flow. Tape volume governed by broker tick volume with live spread friction of `0.93 bps`.
- **Session Volume Structure**: Price operating at `INSIDE_VALUE (Balance)` with Daily POC at `64565.70000` (VAH: `64808.80000` / VAL: `64285.70000`).

---

## 5. Institutional Whale Armor & Resting Orderbook Depth
*(Sources: 10_Whale_Orders.parquet, 12_Hyperdash.parquet, 17_Orderbook.parquet, 4_Hyperliquid_Analysis.parquet)*
- **Interbank Institutional Tier-1 Depth**: Decentralized OTC spot liquidity. Resting whale limit walls from crypto venues do not apply.
- **Verified Broker Armor**: Live Bid `64469.50000` / Live Ask `64475.50000` with institutional spread of `0.93 bps`. Structural defense anchored at Asian Range `[63759.00000 - 64783.00000]` and London Range `[64224.50000 - 64864.00000]`.

---

## 6. Liquidation Max Pain, Heatmaps & Cascade Boundaries
*(Sources: 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 14_Hyperdash_Liq_Map.parquet, 14_Liquidation_Matrix.parquet, 15_Hyperdash_Stops_Map.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **TradFi Structural Liquidity Boundaries**: Centralized perp liquidation feeds do not apply to interbank OTC spot.
- **Stop-Run Cascades & Liquidity Pools**: Primary institutional stop pools reside beyond Classical Pivot extremes (S1: `63563.50000` / S2: `62910.50000` for long stops; R1: `65121.00000` / R2: `66025.50000` for short stops) and Asian session extremes `[63759.00000 - 64783.00000]`.

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