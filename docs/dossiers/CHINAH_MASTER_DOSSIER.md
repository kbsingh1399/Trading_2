# 🔬 MASTER 43-FEED QUANTITATIVE DOSSIER: CHINAH (Hang Seng China Enterprises Index)
**MT5 Symbol**: `CHINAH.p` | **Category**: `Equity Index` | **Tier**: `Tier 2`
**Execution Posture**: `DISQUALIFIED` | **Timestamp**: 2026-10-29 14:43:14 UTC
**Pipeline Clearance**: `BLOCKED` | **Data Freshness**: `1.2m`

---

## 1. MT5 Live Broker Telemetry & Spread Friction Gate
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet)*
- **Live Bid Quote**: `7798.49000` | **Live Ask Quote**: `7818.49000` | **Mid Price**: `7808.49000`
- **Spread Points**: `2000.0 pts` | **Spread BPS**: `25.61 bps` (Mandatory Cap: `5.0 bps`)
- **Gate Status**: **`FAIL`** (Spread friction 25.61 bps exceeds cap 5.0 bps)
- **Order Allowed**: `NONE` | **Pillar 1 Clearance**: `BLOCKED`
- **Broker Specifications**: Contract Size=`1.00` | Tick Value=`1.00 USD` | Min Lot=`0.01` | Digits=`5`
- **Account Capital Context**: Balance=`4,744.55 USD` | Equity=`4,744.32 USD` | Free Margin=`4,342.62 USD` | Inviolate Hard Floor=`4,775.00 USD` (Cushion: `-30.68 USD`)
- **Pipeline Health**: Feed #00 Status=`PASS` | Overall Pipeline Telemetry=`33/33 FEEDS PASS (SYNCHRONIZED)`

---

## 2. Technical Profile, Multi-Sigma VWAP Dispersion & Volatility
*(Sources: 11_Technical.parquet, 11_Technical_BTC_Ribbon.parquet)*
- **Last Verified Price**: `7793.99000` | **24h Change**: `+0.34%` (24h High: `7833.50000`, 24h Low: `7729.49000`)
- **Weekly Range**: Week High=`7833.50000` | Week Low=`7710.45000` | Daily POC=`7782.54000` | Daily VAH=`7810.27000` | Daily VAL=`7768.67000`
- **Session VWAP**: `7789.27082` | **Rolling 24h VWAP**: `7784.58520` | **Distance to VWAP**: `+0.06%`
- **VWAP Z-Score**: `+0.26 sigma` | **Mean Reversion Bias**: **`FAIR VALUE`**
- **VWAP Dispersion Bands**:
  * +1.00 sigma: `7807.11007` | -1.00 sigma: `7771.43157`
  * +1.28 sigma (80% CI): `7812.10506` | -1.28 sigma: `7766.43658`
  * +2.00 sigma (95% CI): `7824.94933` | -2.00 sigma: `7753.59232`
  * +2.01 sigma: `7825.12772` | -2.01 sigma: `7753.41393`
  * +2.51 sigma (98.8% CI): `7834.04734` | -2.51 sigma: `7744.49430`
  * +3.00 sigma (99.7% CI Extreme): `7842.78858` | -3.00 sigma: `7735.75307`
- **Oscillators & Volatility**:
  * **RSI (14)**: `59.42` | **RSI State**: **`BULLISH`**
  * **ATR (14)**: `12.91604` | **ATR %**: `0.17%`
  * **Bollinger Bands**: Upper=`7792.84865` | Mid=`7777.48300` | Lower=`7762.11735` | Bandwidth=`0.40%`
  * **MACD**: Line=`+1.6049` | Signal=`-0.0953` | Hist=`+1.7002`
- **Exponential Moving Average Ribbon (EMA)**:
  * Short Horizon: EMA-5=`7784.63516` | EMA-9=`7782.24968` | EMA-13=`7780.84286` | EMA-20=`7779.73098`
  * Intermediate: EMA-34=`7779.59473` | EMA-50=`7779.72441` | EMA-89=`7778.78943` | EMA-100=`7778.29711`
  * Institutional: EMA-144=`7776.18312` | EMA-200=`7774.42367` (Slope: `+0.012%`) | EMA-233=`7772.50521` (Slope: `+0.013%`)
  * **Trend Bias**: **`STRONG BULLISH`**

---

## 3. Auction Market Structure & Value Profile
*(Sources: 20_Auction_Market_Structure.parquet)*
- **Daily Auction Value Area**:
  * High (VAH): `7810.27000` | Point of Control (POC): `7782.54000` | Low (VAL): `7768.67000`
  * Distance to POC: `+0.33%` | Distance to VAH: `-0.02%` | Distance to VAL: `+0.51%`
  * **Value Area Position**: **`INSIDE_VALUE (Balance)`** | **Auction Regime**: **`ROTATIONAL_BALANCE`** | **Session Bias**: **`BULLISH (Above Pivot)`**
- **Prior Day & Weekly Auction Profile**:
  * Prior Day: PD VAH=`7783.65000` | PD POC=`7772.35000` | PD VAL=`7761.87000` | PDH=`7806.84000` | PDL=`7746.34000` | PDC=`7766.30000`
  * Monday Reference: Monday High=`7816.55000` | Monday Low=`7710.45000` | Monday Mid=`7763.50000`
  * Weekly Value Area: Weekly VAH=`7800.28000` | Weekly POC=`7782.23000` | Weekly VAL=`7755.98000`
  * Multi-Week Extremes: Current Week High (CWH)=`7833.50000` | CWL=`7710.45000` | Prior Week High (PWH)=`8123.60000` | PWL=`7658.12000`
  * Multi-Month Extremes: Current Month High (CMH)=`8238.99000` | CML=`7658.12000` | Prior Month High (PMH)=`8597.71000` | PML=`8065.23000`
- **Session Liquidity Extremes & Initial Balance**:
  * Asian Session: Range `[7731.49000 - 7833.50000]`
  * London Session: Range `[7729.49000 - 7820.50000]`
  * New York Session: Range `[7765.30000 - 7802.99000]`
  * Initial Balance (IB): IB High=`7820.50000` | IB Low=`7780.50000`
- **Fibonacci Golden Pocket & Optimal Trade Entry (OTE)**:
  * Swing Range: High=`7833.50000` | Low=`7729.49000` | Direction=`BEARISH_IMPULSE`
  * Golden Pocket [0.618 - 0.65]: `[7793.77000 - 7797.10000]`
  * Optimal Trade Entry (0.702): `7802.51000` | Invalidation Level: `7811.24000` | Status: **`DEEP_SHELF_TEST (0.786)`**
- **Classical & Weekly Pivots**:
  * Daily Classical: Pivot=`7773.16000` | R1=`7799.98000` | S1=`7739.48000` | R2=`7833.66000` | S2=`7712.66000`
  * Weekly Classical: Weekly Pivot=`7839.34000` | Weekly R1=`8020.56000` | Weekly S1=`7555.08000`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Orderflow
*(Sources: 18_CVD.parquet, 18_CVD_30D_5m.parquet, 18_CVD_30D_15m.parquet, 18_CVD_30D_1h.parquet, 18_CVD_30D_4h.parquet, 18_CVD_30D_ALL.parquet, 21_Tradfye_Orderflow.parquet)*
- **Interbank Spot Orderflow Mechanics**: Decentralized OTC market structure. CVD taker deltas do not apply to interbank spot flow. Tape volume governed by broker tick volume with live spread friction of `25.61 bps`.
- **Session Volume Structure**: Price operating at `INSIDE_VALUE (Balance)` with Daily POC at `7782.54000` (VAH: `7810.27000` / VAL: `7768.67000`).

---

## 5. Institutional Whale Armor & Resting Orderbook Depth
*(Sources: 10_Whale_Orders.parquet, 12_Hyperdash.parquet, 17_Orderbook.parquet, 4_Hyperliquid_Analysis.parquet)*
- **Interbank Institutional Tier-1 Depth**: Decentralized OTC spot liquidity. Resting whale limit walls from crypto venues do not apply.
- **Verified Broker Armor**: Live Bid `7798.49000` / Live Ask `7818.49000` with institutional spread of `25.61 bps`. Structural defense anchored at Asian Range `[7731.49000 - 7833.50000]` and London Range `[7729.49000 - 7820.50000]`.

---

## 6. Liquidation Max Pain, Heatmaps & Cascade Boundaries
*(Sources: 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 14_Hyperdash_Liq_Map.parquet, 14_Liquidation_Matrix.parquet, 15_Hyperdash_Stops_Map.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **TradFi Structural Liquidity Boundaries**: Centralized perp liquidation feeds do not apply to interbank OTC spot.
- **Stop-Run Cascades & Liquidity Pools**: Primary institutional stop pools reside beyond Classical Pivot extremes (S1: `7739.48000` / S2: `7712.66000` for long stops; R1: `7799.98000` / R2: `7833.66000` for short stops) and Asian session extremes `[7731.49000 - 7833.50000]`.

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
- **Economic Calendar Clearance**: Zero high-impact calendar blackout restrictions currently active for this currency pair.

---

## 10. Algorithmic Trade Formulation & Sovereign Decision
- **Sovereign Gate Decision**: **`FAIL_CLOSED_STAND_ASIDE`**
- **Dynamic Capacity Verification**: Active Open=`0` | Resting Pending=`2` | Capacity Check: `N_open + N_pending <= 3` (**`PASS`**)
- **Triple Floor Solvency Check**: Current Equity=`4,744.32 USD` | Hard Floor=`4,775.00 USD` | Buffer=`-30.68 USD` | Solvency Check: **`DEFENSE_MODE`**
- **Stand-Aside Reason**: Gate 1 Spread Friction Failure: Spread friction 25.61 bps exceeds cap 5.0 bps. Standing aside in 100% cash preserves statutory floor.