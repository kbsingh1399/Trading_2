# 🔬 MASTER 43-FEED QUANTITATIVE DOSSIER: US2000 (Russell 2000 Index)
**MT5 Symbol**: `US2000.p` | **Category**: `Equity Index` | **Tier**: `Tier 2`
**Execution Posture**: `PASSIVE LIMIT ONLY` | **Timestamp**: 2026-10-29 14:43:14 UTC
**Pipeline Clearance**: `QUALIFIED` | **Data Freshness**: `1.2m`

---

## 1. MT5 Live Broker Telemetry & Spread Friction Gate
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet)*
- **Live Bid Quote**: `2855.56000` | **Live Ask Quote**: `2855.88000` | **Mid Price**: `2855.72000`
- **Spread Points**: `32.0 pts` | **Spread BPS**: `1.12 bps` (Mandatory Cap: `5.0 bps`)
- **Gate Status**: **`PASS`** (Spread friction within mandatory threshold; safe for maker execution)
- **Order Allowed**: `BUY_LIMIT / SELL_LIMIT` | **Pillar 1 Clearance**: `QUALIFIED`
- **Broker Specifications**: Contract Size=`1.00` | Tick Value=`1.00 USD` | Min Lot=`0.01` | Digits=`5`
- **Account Capital Context**: Balance=`4,744.55 USD` | Equity=`4,744.32 USD` | Free Margin=`4,342.62 USD` | Inviolate Hard Floor=`4,775.00 USD` (Cushion: `-30.68 USD`)
- **Pipeline Health**: Feed #00 Status=`PASS` | Overall Pipeline Telemetry=`33/33 FEEDS PASS (SYNCHRONIZED)`

---

## 2. Technical Profile, Multi-Sigma VWAP Dispersion & Volatility
*(Sources: 11_Technical.parquet, 11_Technical_BTC_Ribbon.parquet)*
- **Last Verified Price**: `2857.04000` | **24h Change**: `+1.25%` (24h High: `2861.66000`, 24h Low: `2807.55000`)
- **Weekly Range**: Week High=`2861.66000` | Week Low=`2774.90000` | Daily POC=`2843.11000` | Daily VAH=`2849.09000` | Daily VAL=`2837.82000`
- **Session VWAP**: `2845.05301` | **Rolling 24h VWAP**: `2830.07714` | **Distance to VWAP**: `+0.42%`
- **VWAP Z-Score**: `+2.40 sigma` | **Mean Reversion Bias**: **`EXTREME OVERBOUGHT`**
- **VWAP Dispersion Bands**:
  * +1.00 sigma: `2850.04540` | -1.00 sigma: `2840.06061`
  * +1.28 sigma (80% CI): `2851.44328` | -1.28 sigma: `2838.66274`
  * +2.00 sigma (95% CI): `2855.03780` | -2.00 sigma: `2835.06821`
  * +2.01 sigma: `2855.08773` | -2.01 sigma: `2835.01829`
  * +2.51 sigma (98.8% CI): `2857.58392` | -2.51 sigma: `2832.52209`
  * +3.00 sigma (99.7% CI Extreme): `2860.03020` | -3.00 sigma: `2830.07582`
- **Oscillators & Volatility**:
  * **RSI (14)**: `71.57` | **RSI State**: **`OVERBOUGHT`**
  * **ATR (14)**: `5.68914` | **ATR %**: `0.20%`
  * **Bollinger Bands**: Upper=`2852.74339` | Mid=`2842.88150` | Lower=`2833.01961` | Bandwidth=`0.69%`
  * **MACD**: Line=`+0.9323` | Signal=`-0.5173` | Hist=`+1.4496`
- **Exponential Moving Average Ribbon (EMA)**:
  * Short Horizon: EMA-5=`2847.81485` | EMA-9=`2844.94648` | EMA-13=`2843.91234` | EMA-20=`2843.35294`
  * Intermediate: EMA-34=`2842.81178` | EMA-50=`2841.57940` | EMA-89=`2837.13103` | EMA-100=`2835.80241`
  * Institutional: EMA-144=`2830.30011` | EMA-200=`2823.77168` (Slope: `+0.081%`) | EMA-233=`2820.22981` (Slope: `+0.083%`)
  * **Trend Bias**: **`STRONG BULLISH`**

---

## 3. Auction Market Structure & Value Profile
*(Sources: 20_Auction_Market_Structure.parquet)*
- **Daily Auction Value Area**:
  * High (VAH): `2849.09000` | Point of Control (POC): `2843.11000` | Low (VAL): `2837.82000`
  * Distance to POC: `+0.45%` | Distance to VAH: `+0.23%` | Distance to VAL: `+0.63%`
  * **Value Area Position**: **`ABOVE_VALUE (Imbalance)`** | **Auction Regime**: **`TREND_UP_ACCEPTANCE`** | **Session Bias**: **`BULLISH (Above Pivot)`**
- **Prior Day & Weekly Auction Profile**:
  * Prior Day: PD VAH=`2823.02000` | PD POC=`2816.63000` | PD VAL=`2812.02000` | PDH=`2845.90000` | PDL=`2807.55000` | PDC=`2839.29000`
  * Monday Reference: Monday High=`2805.58000` | Monday Low=`2774.90000` | Monday Mid=`2790.24000`
  * Weekly Value Area: Weekly VAH=`2832.07000` | Weekly POC=`2817.24000` | Weekly VAL=`2783.24000`
  * Multi-Week Extremes: Current Week High (CWH)=`2867.61000` | CWL=`2774.90000` | Prior Week High (PWH)=`2792.55000` | PWL=`2716.48000`
  * Multi-Month Extremes: Current Month High (CMH)=`2868.84000` | CML=`2713.91000` | Prior Month High (PMH)=`2978.23000` | PML=`2790.78000`
- **Session Liquidity Extremes & Initial Balance**:
  * Asian Session: Range `[2836.43000 - 2850.55000]`
  * London Session: Range `[2833.10000 - 2851.88000]`
  * New York Session: Range `[2833.10000 - 2867.61000]`
  * Initial Balance (IB): IB High=`2851.88000` | IB Low=`2846.53000`
- **Fibonacci Golden Pocket & Optimal Trade Entry (OTE)**:
  * Swing Range: High=`2867.61000` | Low=`2807.55000` | Direction=`BULLISH_IMPULSE`
  * Golden Pocket [0.618 - 0.65]: `[2828.57000 - 2830.49000]`
  * Optimal Trade Entry (0.702): `2825.45000` | Invalidation Level: `2820.40000` | Status: **`SHALLOW_RETRACE`**
- **Classical & Weekly Pivots**:
  * Daily Classical: Pivot=`2830.91000` | R1=`2854.28000` | S1=`2815.93000` | R2=`2869.26000` | S2=`2792.56000`
  * Weekly Classical: Weekly Pivot=`2761.91000` | Weekly R1=`2807.33000` | Weekly S1=`2731.26000`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Orderflow
*(Sources: 18_CVD.parquet, 18_CVD_30D_5m.parquet, 18_CVD_30D_15m.parquet, 18_CVD_30D_1h.parquet, 18_CVD_30D_4h.parquet, 18_CVD_30D_ALL.parquet, 21_Tradfye_Orderflow.parquet)*
- **Primary 15m CVD Microstructure (18_CVD_30D_15m.parquet)**:
  * Candle Delta: `-4,253,470.37 USD` (Base: `-1,496.1888 coins`) | Delta %: `-32.62%`
  * Taker Volumes: Taker Buy=`4,393,387.16 USD` | Taker Sell=`8,646,857.53 USD` | Total Vol=`4,587.00 USD`
  * Cumulative CVD: `+149,477,642.48 USD` (Base: `+52,682.1995`)
  * Rolling CVD Z-Score: `-0.48 sigma` | Price Return: `-0.01%`
  * **Delta Regime**: **`AGGRESSIVE SELLING`** | Trades Count: `4,587`
- **Multi-Timeframe Delta Comparison**:
  * 5m Bar: Delta=`-1,888,739.38 USD` | Delta %=`-48.28%` | Z-Score=`-0.74` | Regime=`AGGRESSIVE SELLING`
  * 1h Bar: Delta=`-46,189,286.12 USD` | Delta %=`-85.75%` | Z-Score=`-0.79` | Regime=`AGGRESSIVE SELLING`
  * 4h Bar: Delta=`-44,634,268.87 USD` | Delta %=`-16.64%` | Z-Score=`-0.71` | Regime=`AGGRESSIVE SELLING`
  * 30D Consolidated (ALL): Cumulative Trend=`+584,903,692.33 USD` | Long-Term Regime=`AGGRESSIVE SELLING`
- **Institutional Footprint & Deribit Options Armor (21_Tradfye_Orderflow.parquet)**:
  * Candle VWAP: `2855.72000` | Estimated POC: `2855.72000` | Avg Trade Size: `0.00 USD`
  * Net Delta USD: `+0.00 USD` | Net Delta %: `+0.00%` | Orderflow CVD: `+0.00 USD`
  * Orderflow Regime: **`BALANCED`** | Orderflow Divergence: **`NONE`**
  * Deribit Options Walls: Max Pain=`0.00` | Call Wall=`0.00` | Put Wall=`0.00`

---

## 5. Institutional Whale Armor & Resting Orderbook Depth
*(Sources: 10_Whale_Orders.parquet, 12_Hyperdash.parquet, 17_Orderbook.parquet, 4_Hyperliquid_Analysis.parquet)*
- **Interbank Institutional Tier-1 Depth**: Decentralized OTC spot liquidity. Resting whale limit walls from crypto venues do not apply.
- **Verified Broker Armor**: Live Bid `2855.56000` / Live Ask `2855.88000` with institutional spread of `1.12 bps`. Structural defense anchored at Asian Range `[2836.43000 - 2850.55000]` and London Range `[2833.10000 - 2851.88000]`.

---

## 6. Liquidation Max Pain, Heatmaps & Cascade Boundaries
*(Sources: 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 14_Hyperdash_Liq_Map.parquet, 14_Liquidation_Matrix.parquet, 15_Hyperdash_Stops_Map.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **TradFi Structural Liquidity Boundaries**: Centralized perp liquidation feeds do not apply to interbank OTC spot.
- **Stop-Run Cascades & Liquidity Pools**: Primary institutional stop pools reside beyond Classical Pivot extremes (S1: `2815.93000` / S2: `2792.56000` for long stops; R1: `2854.28000` / R2: `2869.26000` for short stops) and Asian session extremes `[2836.43000 - 2850.55000]`.

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
- **Stand-Aside Reason**: Absence of statistically validated auction edge and defending resting armor. Standing aside preserves statutory hard floor.