# 🔬 MASTER 43-FEED QUANTITATIVE DOSSIER: ALUMINIUM (Aluminium)
**MT5 Symbol**: `ALUMINIUM.p` | **Category**: `Base Metal` | **Tier**: `Tier 2`
**Execution Posture**: `DISQUALIFIED` | **Timestamp**: 2026-10-29 14:43:14 UTC
**Pipeline Clearance**: `BLOCKED` | **Data Freshness**: `1.2m`

---

## 1. MT5 Live Broker Telemetry & Spread Friction Gate
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet)*
- **Live Bid Quote**: `3065.75000` | **Live Ask Quote**: `3068.05000` | **Mid Price**: `3066.90000`
- **Spread Points**: `2300.0 pts` | **Spread BPS**: `7.50 bps` (Mandatory Cap: `5.0 bps`)
- **Gate Status**: **`FAIL`** (Spread friction 7.50 bps exceeds cap 5.0 bps)
- **Order Allowed**: `NONE` | **Pillar 1 Clearance**: `BLOCKED`
- **Broker Specifications**: Contract Size=`1.00` | Tick Value=`1.00 USD` | Min Lot=`0.01` | Digits=`5`
- **Account Capital Context**: Balance=`4,744.55 USD` | Equity=`4,744.32 USD` | Free Margin=`4,342.62 USD` | Inviolate Hard Floor=`4,775.00 USD` (Cushion: `-30.68 USD`)
- **Pipeline Health**: Feed #00 Status=`PASS` | Overall Pipeline Telemetry=`33/33 FEEDS PASS (SYNCHRONIZED)`

---

## 2. Technical Profile, Multi-Sigma VWAP Dispersion & Volatility
*(Sources: 11_Technical.parquet, 11_Technical_BTC_Ribbon.parquet)*
- **Last Verified Price**: `3062.75000` | **24h Change**: `-1.16%` (24h High: `3110.10000`, 24h Low: `3045.75000`)
- **Weekly Range**: Week High=`3112.60000` | Week Low=`3016.80000` | Daily POC=`3069.05000` | Daily VAH=`3072.69000` | Daily VAL=`3060.41000`
- **Session VWAP**: `3066.43555` | **Rolling 24h VWAP**: `3071.95389` | **Distance to VWAP**: `-0.12%`
- **VWAP Z-Score**: `-0.63 sigma` | **Mean Reversion Bias**: **`FAIR VALUE`**
- **VWAP Dispersion Bands**:
  * +1.00 sigma: `3072.25088` | -1.00 sigma: `3060.62021`
  * +1.28 sigma (80% CI): `3073.87917` | -1.28 sigma: `3058.99192`
  * +2.00 sigma (95% CI): `3078.06622` | -2.00 sigma: `3054.80488`
  * +2.01 sigma: `3078.12437` | -2.01 sigma: `3054.74672`
  * +2.51 sigma (98.8% CI): `3081.03204` | -2.51 sigma: `3051.83905`
  * +3.00 sigma (99.7% CI Extreme): `3083.88155` | -3.00 sigma: `3048.98954`
- **Oscillators & Volatility**:
  * **RSI (14)**: `49.70` | **RSI State**: **`NEUTRAL`**
  * **ATR (14)**: `6.90127` | **ATR %**: `0.23%`
  * **Bollinger Bands**: Upper=`3069.99485` | Mid=`3061.74000` | Lower=`3053.48515` | Bandwidth=`0.54%`
  * **MACD**: Line=`-0.3906` | Signal=`-1.0430` | Hist=`+0.6524`
- **Exponential Moving Average Ribbon (EMA)**:
  * Short Horizon: EMA-5=`3063.28849` | EMA-9=`3062.76787` | EMA-13=`3062.51521` | EMA-20=`3062.57751`
  * Intermediate: EMA-34=`3063.69045` | EMA-50=`3065.54293` | EMA-89=`3068.85316` | EMA-100=`3069.22722`
  * Institutional: EMA-144=`3069.01756` | EMA-200=`3063.81187` (Slope: `-0.009%`) | EMA-233=`3060.85274` (Slope: `+0.003%`)
  * **Trend Bias**: **`NEUTRAL / CHOP`**

---

## 3. Auction Market Structure & Value Profile
*(Sources: 20_Auction_Market_Structure.parquet)*
- **Daily Auction Value Area**:
  * High (VAH): `3072.69000` | Point of Control (POC): `3069.05000` | Low (VAL): `3060.41000`
  * Distance to POC: `-0.05%` | Distance to VAH: `-0.17%` | Distance to VAL: `+0.23%`
  * **Value Area Position**: **`INSIDE_VALUE (Balance)`** | **Auction Regime**: **`ROTATIONAL_BALANCE`** | **Session Bias**: **`BEARISH (Below Pivot)`**
- **Prior Day & Weekly Auction Profile**:
  * Prior Day: PD VAH=`3110.54000` | PD POC=`3093.71000` | PD VAL=`3076.88000` | PDH=`3112.60000` | PDL=`3056.50000` | PDC=`3058.70000`
  * Monday Reference: Monday High=`3060.80000` | Monday Low=`3016.80000` | Monday Mid=`3038.80000`
  * Weekly Value Area: Weekly VAH=`3080.35000` | Weekly POC=`3068.85000` | Weekly VAL=`3032.45000`
  * Multi-Week Extremes: Current Week High (CWH)=`3112.60000` | CWL=`3016.80000` | Prior Week High (PWH)=`3049.75000` | PWL=`2982.00000`
  * Multi-Month Extremes: Current Month High (CMH)=`3170.25000` | CML=`2950.80000` | Prior Month High (PMH)=`3361.45000` | PML=`3148.65000`
- **Session Liquidity Extremes & Initial Balance**:
  * Asian Session: Range `[3058.50000 - 3076.85000]`
  * London Session: Range `[3045.75000 - 3079.85000]`
  * New York Session: Range `[3055.70000 - 3071.00000]`
  * Initial Balance (IB): IB High=`3079.85000` | IB Low=`3070.55000`
- **Fibonacci Golden Pocket & Optimal Trade Entry (OTE)**:
  * Swing Range: High=`3104.05000` | Low=`3045.75000` | Direction=`BEARISH_IMPULSE`
  * Golden Pocket [0.618 - 0.65]: `[3081.78000 - 3083.64000]`
  * Optimal Trade Entry (0.702): `3086.68000` | Invalidation Level: `3091.57000` | Status: **`SHALLOW_RETRACE`**
- **Classical & Weekly Pivots**:
  * Daily Classical: Pivot=`3075.93000` | R1=`3095.37000` | S1=`3039.27000` | R2=`3132.03000` | S2=`3019.83000`
  * Weekly Classical: Weekly Pivot=`3018.30000` | Weekly R1=`3054.60000` | Weekly S1=`2986.85000`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Orderflow
*(Sources: 18_CVD.parquet, 18_CVD_30D_5m.parquet, 18_CVD_30D_15m.parquet, 18_CVD_30D_1h.parquet, 18_CVD_30D_4h.parquet, 18_CVD_30D_ALL.parquet, 21_Tradfye_Orderflow.parquet)*
- **Interbank Spot Orderflow Mechanics**: Decentralized OTC market structure. CVD taker deltas do not apply to interbank spot flow. Tape volume governed by broker tick volume with live spread friction of `7.50 bps`.
- **Session Volume Structure**: Price operating at `INSIDE_VALUE (Balance)` with Daily POC at `3069.05000` (VAH: `3072.69000` / VAL: `3060.41000`).

---

## 5. Institutional Whale Armor & Resting Orderbook Depth
*(Sources: 10_Whale_Orders.parquet, 12_Hyperdash.parquet, 17_Orderbook.parquet, 4_Hyperliquid_Analysis.parquet)*
- **Interbank Institutional Tier-1 Depth**: Decentralized OTC spot liquidity. Resting whale limit walls from crypto venues do not apply.
- **Verified Broker Armor**: Live Bid `3065.75000` / Live Ask `3068.05000` with institutional spread of `7.50 bps`. Structural defense anchored at Asian Range `[3058.50000 - 3076.85000]` and London Range `[3045.75000 - 3079.85000]`.

---

## 6. Liquidation Max Pain, Heatmaps & Cascade Boundaries
*(Sources: 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 14_Hyperdash_Liq_Map.parquet, 14_Liquidation_Matrix.parquet, 15_Hyperdash_Stops_Map.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **TradFi Structural Liquidity Boundaries**: Centralized perp liquidation feeds do not apply to interbank OTC spot.
- **Stop-Run Cascades & Liquidity Pools**: Primary institutional stop pools reside beyond Classical Pivot extremes (S1: `3039.27000` / S2: `3019.83000` for long stops; R1: `3095.37000` / R2: `3132.03000` for short stops) and Asian session extremes `[3058.50000 - 3076.85000]`.

---

## 7. Derivatives Sentiment, Open Interest & Funding Dynamics
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet, 6_Funding_Fee_Settlement.parquet, 13_Hyperliquid.parquet)*
- **Interbank Financing & Carry Mechanics**: Instrument trades as an OTC spot / cash CFD with zero perpetual funding drag or basis settlement friction.
- **Monetary Policy Differential**: Overnight holding carry governed by central bank interest rate spreads and broker rollover swap schedules.

---

## 8. Microstructure Footprint, Tape Imbalances & Macro Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 16_Hyperdash_telegram_Intel.parquet, 19_News.parquet, 19_Calendar.parquet)*
- **Bar-by-Bar Microstructure Footprint (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
  * Venue Source: `Aggregated` | Timeframe: `15m` | Last Price: `3066.90000`
  * Footprint Auction Profile: Bar VWAP=`3066.90000` | Bar POC=`3066.90000` | Bar VAH=`3073.03380` | Bar VAL=`3060.76620`
  * Orderflow Volumes: Total Vol=`0.00 USD` | Taker Buy=`0.00 USD` | Taker Sell=`0.00 USD`
  * Bar Delta Profile: Delta=`+0.00 USD` (`+0.00%`) | Max Delta=`+0.00 USD` | Min Delta=`+0.00 USD` | Cumulative Bar Delta=`+0.00 USD`
  * Order Execution Dynamics: Trades Count=`0` | Avg Trade Size=`0.00 USD`
  * Tape Imbalances: Imbalance Ratio=`0.0%` | Buy Imbalances Count=`0` | Sell Imbalances Count=`0`
  * Footprint Open Interest: Bar OI=`0.00 USD` | Bar OI Change=`+0.00 USD`
- **CoinGlass Algorithmic Footprint Signals (25_CoinGlass_Footprint_Signals.parquet)**:
  * Signal Classification: Type=`AUCTION_RANGE_EXPANSION` | Bias: **`BEARISH (BELOW PIVOT)`** | Signal Time=`2026-10-28 21:11:33 IST` | Timeframe=`Auction`
  * Signal Context: Headline=`ALUMINIUM (ALUMINIUM.p) Metal Auction: RANGE_EXPANSION` | Price Level=`3062.43000` | Absorbed Volume=`0.00 USD`
  * Bar Footprint Context: Current Bar Delta=`+0.00 USD` | Current Bar Volume=`0.00 USD` | Delta in View=`+0.00 USD`
  * Historical Detail: `Daily POC: 3093.720 | VAH: 3106.670 | VAL: 3086.520 | IB: [3097.100 - 3105.400] | Spread: 7.3 bps` | KPI=`AUCTION_RANGE_EXPANSION` | Bias=`BEARISH (BELOW PIVOT)`
- **Multi-Horizon Macro Capital Netflows (2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet)**:
  * Spot Capital Netflows:
    - Tactical: 5m=`-` | 15m=`-` | 30m=`-` | 1h=`-`
    - Intermediate: 2h=`-` | 4h=`-` | 6h=`-` | 8h=`-` | 12h=`-` | 24h=`-`
    - Macro Horizons: 1-Week=`-` | 15-Day=`-` | 30-Day=`-` | Market Cap=`-`
  * Futures Capital Netflows:
    - Tactical: 5m=`-` | 15m=`-` | 30m=`-` | 1h=`-`
    - Intermediate: 2h=`-` | 4h=`-` | 6h=`-` | 8h=`-` | 12h=`-` | 24h=`-`
    - Macro Horizons: 1-Week=`-` | 15-Day=`-` | 30-Day=`-` | Market Cap=`-`

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
- **Stand-Aside Reason**: Gate 1 Spread Friction Failure: Spread friction 7.50 bps exceeds cap 5.0 bps. Standing aside in 100% cash preserves statutory floor.