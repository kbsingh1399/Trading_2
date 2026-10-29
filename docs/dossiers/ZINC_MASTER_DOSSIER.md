# 🔬 MASTER 43-FEED QUANTITATIVE DOSSIER: ZINC (Zinc)
**MT5 Symbol**: `ZINC.p` | **Category**: `Base Metal` | **Tier**: `Tier 2`
**Execution Posture**: `DISQUALIFIED` | **Timestamp**: 2026-10-29 14:43:14 UTC
**Pipeline Clearance**: `BLOCKED` | **Data Freshness**: `1.2m`

---

## 1. MT5 Live Broker Telemetry & Spread Friction Gate
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet)*
- **Live Bid Quote**: `3876.08800` | **Live Ask Quote**: `3878.81200` | **Mid Price**: `3877.45000`
- **Spread Points**: `2724.0 pts` | **Spread BPS**: `7.03 bps` (Mandatory Cap: `5.0 bps`)
- **Gate Status**: **`FAIL`** (Spread friction 7.03 bps exceeds cap 5.0 bps)
- **Order Allowed**: `NONE` | **Pillar 1 Clearance**: `BLOCKED`
- **Broker Specifications**: Contract Size=`1.00` | Tick Value=`1.00 USD` | Min Lot=`0.01` | Digits=`5`
- **Account Capital Context**: Balance=`4,744.55 USD` | Equity=`4,744.32 USD` | Free Margin=`4,342.62 USD` | Inviolate Hard Floor=`4,775.00 USD` (Cushion: `-30.68 USD`)
- **Pipeline Health**: Feed #00 Status=`PASS` | Overall Pipeline Telemetry=`33/33 FEEDS PASS (SYNCHRONIZED)`

---

## 2. Technical Profile, Multi-Sigma VWAP Dispersion & Volatility
*(Sources: 11_Technical.parquet, 11_Technical_BTC_Ribbon.parquet)*
- **Last Verified Price**: `3869.98800` | **24h Change**: `+0.05%` (24h High: `3899.03800`, 24h Low: `3836.84000`)
- **Weekly Range**: Week High=`3899.03800` | Week Low=`3737.33800` | Daily POC=`3859.92000` | Daily VAH=`3877.34000` | Daily VAL=`3853.08000`
- **Session VWAP**: `3868.95502` | **Rolling 24h VWAP**: `3866.08454` | **Distance to VWAP**: `+0.03%`
- **VWAP Z-Score**: `+0.09 sigma` | **Mean Reversion Bias**: **`FAIR VALUE`**
- **VWAP Dispersion Bands**:
  * +1.00 sigma: `3880.36007` | -1.00 sigma: `3857.54997`
  * +1.28 sigma (80% CI): `3883.55348` | -1.28 sigma: `3854.35656`
  * +2.00 sigma (95% CI): `3891.76512` | -2.00 sigma: `3846.14492`
  * +2.01 sigma: `3891.87917` | -2.01 sigma: `3846.03087`
  * +2.51 sigma (98.8% CI): `3897.58169` | -2.51 sigma: `3840.32835`
  * +3.00 sigma (99.7% CI Extreme): `3903.17017` | -3.00 sigma: `3834.73987`
- **Oscillators & Volatility**:
  * **RSI (14)**: `44.63` | **RSI State**: **`BEARISH`**
  * **ATR (14)**: `9.07122` | **ATR %**: `0.23%`
  * **Bollinger Bands**: Upper=`3899.24095` | Mid=`3882.82090` | Lower=`3866.40085` | Bandwidth=`0.85%`
  * **MACD**: Line=`-0.7418` | Signal=`+2.0760` | Hist=`-2.8177`
- **Exponential Moving Average Ribbon (EMA)**:
  * Short Horizon: EMA-5=`3871.37280` | EMA-9=`3874.49337` | EMA-13=`3876.26051` | EMA-20=`3877.07922`
  * Intermediate: EMA-34=`3875.59292` | EMA-50=`3873.04297` | EMA-89=`3866.66864` | EMA-100=`3864.68608`
  * Institutional: EMA-144=`3855.80841` | EMA-200=`3843.04102` (Slope: `+0.115%`) | EMA-233=`3835.55995` (Slope: `+0.119%`)
  * **Trend Bias**: **`NEUTRAL / CHOP`**

---

## 3. Auction Market Structure & Value Profile
*(Sources: 20_Auction_Market_Structure.parquet)*
- **Daily Auction Value Area**:
  * High (VAH): `3877.34000` | Point of Control (POC): `3859.92000` | Low (VAL): `3853.08000`
  * Distance to POC: `+0.45%` | Distance to VAH: `+0.00%` | Distance to VAL: `+0.63%`
  * **Value Area Position**: **`ABOVE_VALUE (Imbalance)`** | **Auction Regime**: **`TREND_UP_ACCEPTANCE`** | **Session Bias**: **`BULLISH (Above Pivot)`**
- **Prior Day & Weekly Auction Profile**:
  * Prior Day: PD VAH=`3870.19000` | PD POC=`3864.94000` | PD VAL=`3848.65000` | PDH=`3874.79000` | PDL=`3835.39000` | PDC=`3848.09000`
  * Monday Reference: Monday High=`3832.29000` | Monday Low=`3737.34000` | Monday Mid=`3784.81000`
  * Weekly Value Area: Weekly VAH=`3894.19000` | Weekly POC=`3860.77000` | Weekly VAL=`3814.41000`
  * Multi-Week Extremes: Current Week High (CWH)=`3899.04000` | CWL=`3737.34000` | Prior Week High (PWH)=`3765.34000` | PWL=`3647.74000`
  * Multi-Month Extremes: Current Month High (CMH)=`3899.04000` | CML=`3646.69000` | Prior Month High (PMH)=`4054.49000` | PML=`3729.54000`
- **Session Liquidity Extremes & Initial Balance**:
  * Asian Session: Range `[3847.79000 - 3868.74000]`
  * London Session: Range `[3849.14000 - 3899.04000]`
  * New York Session: Range `[3859.69000 - 3899.04000]`
  * Initial Balance (IB): IB High=`3879.59000` | IB Low=`3858.59000`
- **Fibonacci Golden Pocket & Optimal Trade Entry (OTE)**:
  * Swing Range: High=`3899.04000` | Low=`3836.84000` | Direction=`BULLISH_IMPULSE`
  * Golden Pocket [0.618 - 0.65]: `[3858.61000 - 3860.60000]`
  * Optimal Trade Entry (0.702): `3855.38000` | Invalidation Level: `3850.15000` | Status: **`SHALLOW_RETRACE`**
- **Classical & Weekly Pivots**:
  * Daily Classical: Pivot=`3852.75000` | R1=`3870.12000` | S1=`3830.72000` | R2=`3892.15000` | S2=`3813.35000`
  * Weekly Classical: Weekly Pivot=`3712.24000` | Weekly R1=`3776.74000` | Weekly S1=`3659.14000`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Orderflow
*(Sources: 18_CVD.parquet, 18_CVD_30D_5m.parquet, 18_CVD_30D_15m.parquet, 18_CVD_30D_1h.parquet, 18_CVD_30D_4h.parquet, 18_CVD_30D_ALL.parquet, 21_Tradfye_Orderflow.parquet)*
- **Interbank Spot Orderflow Mechanics**: Decentralized OTC market structure. CVD taker deltas do not apply to interbank spot flow. Tape volume governed by broker tick volume with live spread friction of `7.03 bps`.
- **Session Volume Structure**: Price operating at `ABOVE_VALUE (Imbalance)` with Daily POC at `3859.92000` (VAH: `3877.34000` / VAL: `3853.08000`).

---

## 5. Institutional Whale Armor & Resting Orderbook Depth
*(Sources: 10_Whale_Orders.parquet, 12_Hyperdash.parquet, 17_Orderbook.parquet, 4_Hyperliquid_Analysis.parquet)*
- **Interbank Institutional Tier-1 Depth**: Decentralized OTC spot liquidity. Resting whale limit walls from crypto venues do not apply.
- **Verified Broker Armor**: Live Bid `3876.08800` / Live Ask `3878.81200` with institutional spread of `7.03 bps`. Structural defense anchored at Asian Range `[3847.79000 - 3868.74000]` and London Range `[3849.14000 - 3899.04000]`.

---

## 6. Liquidation Max Pain, Heatmaps & Cascade Boundaries
*(Sources: 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 14_Hyperdash_Liq_Map.parquet, 14_Liquidation_Matrix.parquet, 15_Hyperdash_Stops_Map.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **TradFi Structural Liquidity Boundaries**: Centralized perp liquidation feeds do not apply to interbank OTC spot.
- **Stop-Run Cascades & Liquidity Pools**: Primary institutional stop pools reside beyond Classical Pivot extremes (S1: `3830.72000` / S2: `3813.35000` for long stops; R1: `3870.12000` / R2: `3892.15000` for short stops) and Asian session extremes `[3847.79000 - 3868.74000]`.

---

## 7. Derivatives Sentiment, Open Interest & Funding Dynamics
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet, 6_Funding_Fee_Settlement.parquet, 13_Hyperliquid.parquet)*
- **Interbank Financing & Carry Mechanics**: Instrument trades as an OTC spot / cash CFD with zero perpetual funding drag or basis settlement friction.
- **Monetary Policy Differential**: Overnight holding carry governed by central bank interest rate spreads and broker rollover swap schedules.

---

## 8. Microstructure Footprint, Tape Imbalances & Macro Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 16_Hyperdash_telegram_Intel.parquet, 19_News.parquet, 19_Calendar.parquet)*
- **Bar-by-Bar Microstructure Footprint (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
  * Venue Source: `Aggregated` | Timeframe: `15m` | Last Price: `3877.45000`
  * Footprint Auction Profile: Bar VWAP=`3877.45000` | Bar POC=`3877.45000` | Bar VAH=`3885.20490` | Bar VAL=`3869.69510`
  * Orderflow Volumes: Total Vol=`0.00 USD` | Taker Buy=`0.00 USD` | Taker Sell=`0.00 USD`
  * Bar Delta Profile: Delta=`+0.00 USD` (`+0.00%`) | Max Delta=`+0.00 USD` | Min Delta=`+0.00 USD` | Cumulative Bar Delta=`+0.00 USD`
  * Order Execution Dynamics: Trades Count=`0` | Avg Trade Size=`0.00 USD`
  * Tape Imbalances: Imbalance Ratio=`0.0%` | Buy Imbalances Count=`0` | Sell Imbalances Count=`0`
  * Footprint Open Interest: Bar OI=`0.00 USD` | Bar OI Change=`+0.00 USD`
- **CoinGlass Algorithmic Footprint Signals (25_CoinGlass_Footprint_Signals.parquet)**:
  * Signal Classification: Type=`AUCTION_ROTATIONAL_BALANCE` | Bias: **`BULLISH (ABOVE PIVOT)`** | Signal Time=`2026-10-28 21:11:33 IST` | Timeframe=`Auction`
  * Signal Context: Headline=`ZINC (ZINC.p) Metal Auction: ROTATIONAL_BALANCE` | Price Level=`3848.80000` | Absorbed Volume=`0.00 USD`
  * Bar Footprint Context: Current Bar Delta=`+0.00 USD` | Current Bar Volume=`0.00 USD` | Delta in View=`+0.00 USD`
  * Historical Detail: `Daily POC: 3856.530 | VAH: 3865.460 | VAL: 3844.710 | IB: [3844.290 - 3864.090] | Spread: 7.1 bps` | KPI=`AUCTION_ROTATIONAL_BALANCE` | Bias=`BULLISH (ABOVE PIVOT)`
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
- **Stand-Aside Reason**: Gate 1 Spread Friction Failure: Spread friction 7.03 bps exceeds cap 5.0 bps. Standing aside in 100% cash preserves statutory floor.