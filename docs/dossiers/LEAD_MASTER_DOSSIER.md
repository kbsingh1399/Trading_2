# 🔬 MASTER 43-FEED QUANTITATIVE DOSSIER: LEAD (Lead)
**MT5 Symbol**: `LEAD.p` | **Category**: `Base Metal` | **Tier**: `Tier 2`
**Execution Posture**: `DISQUALIFIED` | **Timestamp**: 2026-10-29 14:43:14 UTC
**Pipeline Clearance**: `BLOCKED` | **Data Freshness**: `1.2m`

---

## 1. MT5 Live Broker Telemetry & Spread Friction Gate
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet)*
- **Live Bid Quote**: `1909.15000` | **Live Ask Quote**: `1911.60000` | **Mid Price**: `1910.37500`
- **Spread Points**: `2450.0 pts` | **Spread BPS**: `12.82 bps` (Mandatory Cap: `5.0 bps`)
- **Gate Status**: **`FAIL`** (Spread friction 12.82 bps exceeds cap 5.0 bps)
- **Order Allowed**: `NONE` | **Pillar 1 Clearance**: `BLOCKED`
- **Broker Specifications**: Contract Size=`1.00` | Tick Value=`1.00 USD` | Min Lot=`0.01` | Digits=`5`
- **Account Capital Context**: Balance=`4,744.55 USD` | Equity=`4,744.32 USD` | Free Margin=`4,342.62 USD` | Inviolate Hard Floor=`4,775.00 USD` (Cushion: `-30.68 USD`)
- **Pipeline Health**: Feed #00 Status=`PASS` | Overall Pipeline Telemetry=`33/33 FEEDS PASS (SYNCHRONIZED)`

---

## 2. Technical Profile, Multi-Sigma VWAP Dispersion & Volatility
*(Sources: 11_Technical.parquet, 11_Technical_BTC_Ribbon.parquet)*
- **Last Verified Price**: `1908.65000` | **24h Change**: `-1.20%` (24h High: `1933.35000`, 24h Low: `1879.00000`)
- **Weekly Range**: Week High=`1940.05000` | Week Low=`1879.00000` | Daily POC=`1908.46000` | Daily VAH=`1909.88000` | Daily VAL=`1904.71000`
- **Session VWAP**: `1906.48077` | **Rolling 24h VWAP**: `1912.14721` | **Distance to VWAP**: `+0.11%`
- **VWAP Z-Score**: `+0.89 sigma` | **Mean Reversion Bias**: **`FAIR VALUE`**
- **VWAP Dispersion Bands**:
  * +1.00 sigma: `1908.91391` | -1.00 sigma: `1904.04763`
  * +1.28 sigma (80% CI): `1909.59519` | -1.28 sigma: `1903.36635`
  * +2.00 sigma (95% CI): `1911.34705` | -2.00 sigma: `1901.61449`
  * +2.01 sigma: `1911.37139` | -2.01 sigma: `1901.59016`
  * +2.51 sigma (98.8% CI): `1912.58796` | -2.51 sigma: `1900.37358`
  * +3.00 sigma (99.7% CI Extreme): `1913.78020` | -3.00 sigma: `1899.18135`
- **Oscillators & Volatility**:
  * **RSI (14)**: `52.71` | **RSI State**: **`NEUTRAL`**
  * **ATR (14)**: `2.59190` | **ATR %**: `0.14%`
  * **Bollinger Bands**: Upper=`1910.20472` | Mid=`1908.16750` | Lower=`1906.13028` | Bandwidth=`0.21%`
  * **MACD**: Line=`-0.0001` | Signal=`+0.1962` | Hist=`-0.1963`
- **Exponential Moving Average Ribbon (EMA)**:
  * Short Horizon: EMA-5=`1907.48560` | EMA-9=`1907.62715` | EMA-13=`1907.73531` | EMA-20=`1907.74793`
  * Intermediate: EMA-34=`1907.80202` | EMA-50=`1908.54581` | EMA-89=`1911.51310` | EMA-100=`1912.26394`
  * Institutional: EMA-144=`1914.36840` | EMA-200=`1915.38430` (Slope: `-0.050%`) | EMA-233=`1915.78110` (Slope: `-0.045%`)
  * **Trend Bias**: **`NEUTRAL / CHOP`**

---

## 3. Auction Market Structure & Value Profile
*(Sources: 20_Auction_Market_Structure.parquet)*
- **Daily Auction Value Area**:
  * High (VAH): `1909.88000` | Point of Control (POC): `1908.46000` | Low (VAL): `1904.71000`
  * Distance to POC: `+0.10%` | Distance to VAH: `+0.03%` | Distance to VAL: `+0.30%`
  * **Value Area Position**: **`ABOVE_VALUE (Imbalance)`** | **Auction Regime**: **`RANGE_EXPANSION`** | **Session Bias**: **`BULLISH (Above Pivot)`**
- **Prior Day & Weekly Auction Profile**:
  * Prior Day: PD VAH=`1939.85000` | PD POC=`1929.67000` | PD VAL=`1917.87000` | PDH=`1940.05000` | PDL=`1879.00000` | PDC=`1879.00000`
  * Monday Reference: Monday High=`1930.00000` | Monday Low=`1899.00000` | Monday Mid=`1914.50000`
  * Weekly Value Area: Weekly VAH=`1939.44000` | Weekly POC=`1927.23000` | Weekly VAL=`1910.14000`
  * Multi-Week Extremes: Current Week High (CWH)=`1940.05000` | CWL=`1879.00000` | Prior Week High (PWH)=`1918.10000` | PWL=`1871.45000`
  * Multi-Month Extremes: Current Month High (CMH)=`1940.05000` | CML=`1827.90000` | Prior Month High (PMH)=`1949.15000` | PML=`1851.20000`
- **Session Liquidity Extremes & Initial Balance**:
  * Asian Session: Range `[1896.25000 - 1906.60000]`
  * London Session: Range `[1904.65000 - 1911.45000]`
  * New York Session: Range `[1904.95000 - 1911.45000]`
  * Initial Balance (IB): IB High=`1909.80000` | IB Low=`1905.40000`
- **Fibonacci Golden Pocket & Optimal Trade Entry (OTE)**:
  * Swing Range: High=`1933.35000` | Low=`1879.00000` | Direction=`BEARISH_IMPULSE`
  * Golden Pocket [0.618 - 0.65]: `[1912.59000 - 1914.33000]`
  * Optimal Trade Entry (0.702): `1917.15000` | Invalidation Level: `1921.72000` | Status: **`SHALLOW_RETRACE`**
- **Classical & Weekly Pivots**:
  * Daily Classical: Pivot=`1899.35000` | R1=`1919.70000` | S1=`1858.65000` | R2=`1960.40000` | S2=`1838.30000`
  * Weekly Classical: Weekly Pivot=`1891.72000` | Weekly R1=`1911.98000` | Weekly S1=`1865.33000`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Orderflow
*(Sources: 18_CVD.parquet, 18_CVD_30D_5m.parquet, 18_CVD_30D_15m.parquet, 18_CVD_30D_1h.parquet, 18_CVD_30D_4h.parquet, 18_CVD_30D_ALL.parquet, 21_Tradfye_Orderflow.parquet)*
- **Interbank Spot Orderflow Mechanics**: Decentralized OTC market structure. CVD taker deltas do not apply to interbank spot flow. Tape volume governed by broker tick volume with live spread friction of `12.82 bps`.
- **Session Volume Structure**: Price operating at `ABOVE_VALUE (Imbalance)` with Daily POC at `1908.46000` (VAH: `1909.88000` / VAL: `1904.71000`).

---

## 5. Institutional Whale Armor & Resting Orderbook Depth
*(Sources: 10_Whale_Orders.parquet, 12_Hyperdash.parquet, 17_Orderbook.parquet, 4_Hyperliquid_Analysis.parquet)*
- **Interbank Institutional Tier-1 Depth**: Decentralized OTC spot liquidity. Resting whale limit walls from crypto venues do not apply.
- **Verified Broker Armor**: Live Bid `1909.15000` / Live Ask `1911.60000` with institutional spread of `12.82 bps`. Structural defense anchored at Asian Range `[1896.25000 - 1906.60000]` and London Range `[1904.65000 - 1911.45000]`.

---

## 6. Liquidation Max Pain, Heatmaps & Cascade Boundaries
*(Sources: 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 14_Hyperdash_Liq_Map.parquet, 14_Liquidation_Matrix.parquet, 15_Hyperdash_Stops_Map.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **TradFi Structural Liquidity Boundaries**: Centralized perp liquidation feeds do not apply to interbank OTC spot.
- **Stop-Run Cascades & Liquidity Pools**: Primary institutional stop pools reside beyond Classical Pivot extremes (S1: `1858.65000` / S2: `1838.30000` for long stops; R1: `1919.70000` / R2: `1960.40000` for short stops) and Asian session extremes `[1896.25000 - 1906.60000]`.

---

## 7. Derivatives Sentiment, Open Interest & Funding Dynamics
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet, 6_Funding_Fee_Settlement.parquet, 13_Hyperliquid.parquet)*
- **Interbank Financing & Carry Mechanics**: Instrument trades as an OTC spot / cash CFD with zero perpetual funding drag or basis settlement friction.
- **Monetary Policy Differential**: Overnight holding carry governed by central bank interest rate spreads and broker rollover swap schedules.

---

## 8. Microstructure Footprint, Tape Imbalances & Macro Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 16_Hyperdash_telegram_Intel.parquet, 19_News.parquet, 19_Calendar.parquet)*
- **Bar-by-Bar Microstructure Footprint (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
  * Venue Source: `Aggregated` | Timeframe: `15m` | Last Price: `1910.37500`
  * Footprint Auction Profile: Bar VWAP=`1910.37500` | Bar POC=`1910.37500` | Bar VAH=`1914.19575` | Bar VAL=`1906.55425`
  * Orderflow Volumes: Total Vol=`0.00 USD` | Taker Buy=`0.00 USD` | Taker Sell=`0.00 USD`
  * Bar Delta Profile: Delta=`+0.00 USD` (`+0.00%`) | Max Delta=`+0.00 USD` | Min Delta=`+0.00 USD` | Cumulative Bar Delta=`+0.00 USD`
  * Order Execution Dynamics: Trades Count=`0` | Avg Trade Size=`0.00 USD`
  * Tape Imbalances: Imbalance Ratio=`0.0%` | Buy Imbalances Count=`0` | Sell Imbalances Count=`0`
  * Footprint Open Interest: Bar OI=`0.00 USD` | Bar OI Change=`+0.00 USD`
- **CoinGlass Algorithmic Footprint Signals (25_CoinGlass_Footprint_Signals.parquet)**:
  * Signal Classification: Type=`AUCTION_RANGE_EXPANSION` | Bias: **`BEARISH (BELOW PIVOT)`** | Signal Time=`2026-10-28 21:11:33 IST` | Timeframe=`Auction`
  * Signal Context: Headline=`LEAD (LEAD.p) Metal Auction: RANGE_EXPANSION` | Price Level=`1922.43000` | Absorbed Volume=`0.00 USD`
  * Bar Footprint Context: Current Bar Delta=`+0.00 USD` | Current Bar Volume=`0.00 USD` | Delta in View=`+0.00 USD`
  * Historical Detail: `Daily POC: 1929.370 | VAH: 1932.270 | VAL: 1927.190 | IB: [1928.050 - 1932.100] | Spread: 12.8 bps` | KPI=`AUCTION_RANGE_EXPANSION` | Bias=`BEARISH (BELOW PIVOT)`
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
- **Stand-Aside Reason**: Gate 1 Spread Friction Failure: Spread friction 12.82 bps exceeds cap 5.0 bps. Standing aside in 100% cash preserves statutory floor.