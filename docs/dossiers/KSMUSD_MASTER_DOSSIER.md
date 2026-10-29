# 🔬 MASTER 43-FEED QUANTITATIVE DOSSIER: KSMUSD (KSM/USD)
**MT5 Symbol**: `KSMUSD.p` | **Category**: `Forex Cross` | **Tier**: `Tier 2`
**Execution Posture**: `DISQUALIFIED` | **Timestamp**: 2026-10-29 14:43:14 UTC
**Pipeline Clearance**: `BLOCKED` | **Data Freshness**: `1.2m`

---

## 1. MT5 Live Broker Telemetry & Spread Friction Gate
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet)*
- **Live Bid Quote**: `3.64000` | **Live Ask Quote**: `3.85000` | **Mid Price**: `3.74500`
- **Spread Points**: `21.0 pts` | **Spread BPS**: `560.75 bps` (Mandatory Cap: `25.0 bps`)
- **Gate Status**: **`FAIL`** (Spread friction 560.75 bps exceeds cap 25.0 bps)
- **Order Allowed**: `NONE` | **Pillar 1 Clearance**: `BLOCKED`
- **Broker Specifications**: Contract Size=`1.00` | Tick Value=`1.00 USD` | Min Lot=`0.01` | Digits=`5`
- **Account Capital Context**: Balance=`4,744.55 USD` | Equity=`4,744.32 USD` | Free Margin=`4,342.62 USD` | Inviolate Hard Floor=`4,775.00 USD` (Cushion: `-30.68 USD`)
- **Pipeline Health**: Feed #00 Status=`PASS` | Overall Pipeline Telemetry=`33/33 FEEDS PASS (SYNCHRONIZED)`

---

## 2. Technical Profile, Multi-Sigma VWAP Dispersion & Volatility
*(Sources: 11_Technical.parquet, 11_Technical_BTC_Ribbon.parquet)*
- **Last Verified Price**: `3.63000` | **24h Change**: `+0.83%` (24h High: `3.75000`, 24h Low: `3.49000`)
- **Weekly Range**: Week High=`3.78000` | Week Low=`3.49000` | Daily POC=`3.51975` | Daily VAH=`3.59795` | Daily VAL=`3.49935`
- **Session VWAP**: `3.56297` | **Rolling 24h VWAP**: `3.60097` | **Distance to VWAP**: `+1.88%`
- **VWAP Z-Score**: `+1.52 sigma` | **Mean Reversion Bias**: **`OVERBOUGHT`**
- **VWAP Dispersion Bands**:
  * +1.00 sigma: `3.60706` | -1.00 sigma: `3.51889`
  * +1.28 sigma (80% CI): `3.61941` | -1.28 sigma: `3.50654`
  * +2.00 sigma (95% CI): `3.65115` | -2.00 sigma: `3.47480`
  * +2.01 sigma: `3.65159` | -2.01 sigma: `3.47435`
  * +2.51 sigma (98.8% CI): `3.67364` | -2.51 sigma: `3.45231`
  * +3.00 sigma (99.7% CI Extreme): `3.69524` | -3.00 sigma: `3.43071`
- **Oscillators & Volatility**:
  * **RSI (14)**: `67.66` | **RSI State**: **`BULLISH`**
  * **ATR (14)**: `0.01752` | **ATR %**: `0.48%`
  * **Bollinger Bands**: Upper=`3.65081` | Mid=`3.59550` | Lower=`3.54019` | Bandwidth=`3.08%`
  * **MACD**: Line=`+0.0207` | Signal=`+0.0169` | Hist=`+0.0038`
- **Exponential Moving Average Ribbon (EMA)**:
  * Short Horizon: EMA-5=`3.62702` | EMA-9=`3.61934` | EMA-13=`3.61121` | EMA-20=`3.59931`
  * Intermediate: EMA-34=`3.58776` | EMA-50=`3.58740` | EMA-89=`3.60282` | EMA-100=`3.60772`
  * Institutional: EMA-144=`3.62392` | EMA-200=`3.63629` (Slope: `-0.076%`) | EMA-233=`3.64608` (Slope: `-0.094%`)
  * **Trend Bias**: **`BULLISH`**

---

## 3. Auction Market Structure & Value Profile
*(Sources: 20_Auction_Market_Structure.parquet)*
- **Daily Auction Value Area**:
  * High (VAH): `3.59795` | Point of Control (POC): `3.51975` | Low (VAL): `3.49935`
  * Distance to POC: `+0.00%` | Distance to VAH: `+0.00%` | Distance to VAL: `+0.00%`
  * **Value Area Position**: **`INSIDE_VALUE (Balance)`** | **Auction Regime**: **`BALANCED_AUCTION`** | **Session Bias**: **`NEUTRAL`**
- **Prior Day & Weekly Auction Profile**:
  * Prior Day: PD VAH=`3.75998` | PD POC=`3.74500` | PD VAL=`3.73002` | PDH=`3.76747` | PDL=`3.72253` | PDC=`3.74500`
  * Monday Reference: Monday High=`3.76372` | Monday Low=`3.72628` | Monday Mid=`3.74500`
  * Weekly Value Area: Weekly VAH=`3.77496` | Weekly POC=`3.74500` | Weekly VAL=`3.71504`
  * Multi-Week Extremes: Current Week High (CWH)=`3.78245` | CWL=`3.70755` | Prior Week High (PWH)=`3.80117` | PWL=`3.68883`
  * Multi-Month Extremes: Current Month High (CMH)=`3.81990` | CML=`3.67010` | Prior Month High (PMH)=`3.83862` | PML=`3.65137`
- **Session Liquidity Extremes & Initial Balance**:
  * Asian Session: Range `[3.73751 - 3.75249]`
  * London Session: Range `[3.73002 - 3.75998]`
  * New York Session: Range `[3.72628 - 3.76372]`
  * Initial Balance (IB): IB High=`3.75623` | IB Low=`3.73377`
- **Fibonacci Golden Pocket & Optimal Trade Entry (OTE)**:
  * Swing Range: High=`3.75000` | Low=`3.49000` | Direction=`NONE`
  * Golden Pocket [0.618 - 0.65]: `[3.73751 - 3.75249]`
  * Optimal Trade Entry (0.702): `3.74500` | Invalidation Level: `0.00000` | Status: **`NONE`**
- **Classical & Weekly Pivots**:
  * Daily Classical: Pivot=`3.74500` | R1=`3.75623` | S1=`3.73377` | R2=`3.76747` | S2=`3.72253`
  * Weekly Classical: Weekly Pivot=`3.74500` | Weekly R1=`3.78245` | Weekly S1=`3.70755`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Orderflow
*(Sources: 18_CVD.parquet, 18_CVD_30D_5m.parquet, 18_CVD_30D_15m.parquet, 18_CVD_30D_1h.parquet, 18_CVD_30D_4h.parquet, 18_CVD_30D_ALL.parquet, 21_Tradfye_Orderflow.parquet)*
- **Interbank Spot Orderflow Mechanics**: Decentralized OTC market structure. CVD taker deltas do not apply to interbank spot flow. Tape volume governed by broker tick volume with live spread friction of `560.75 bps`.
- **Session Volume Structure**: Price operating at `INSIDE_VALUE (Balance)` with Daily POC at `3.51975` (VAH: `3.59795` / VAL: `3.49935`).

---

## 5. Institutional Whale Armor & Resting Orderbook Depth
*(Sources: 10_Whale_Orders.parquet, 12_Hyperdash.parquet, 17_Orderbook.parquet, 4_Hyperliquid_Analysis.parquet)*
- **Interbank Institutional Tier-1 Depth**: Decentralized OTC spot liquidity. Resting whale limit walls from crypto venues do not apply.
- **Verified Broker Armor**: Live Bid `3.64000` / Live Ask `3.85000` with institutional spread of `560.75 bps`. Structural defense anchored at Asian Range `[3.73751 - 3.75249]` and London Range `[3.73002 - 3.75998]`.

---

## 6. Liquidation Max Pain, Heatmaps & Cascade Boundaries
*(Sources: 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 14_Hyperdash_Liq_Map.parquet, 14_Liquidation_Matrix.parquet, 15_Hyperdash_Stops_Map.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`3.88280` (Vol: `3,124 USD`, Dist: `+1.59%`) | Long MP=`3.69990` (Vol: `3,961 USD`, Dist: `-3.19%`)
  * 48H Horizon: Short MP=`3.87360` (Vol: `3,703 USD`, Dist: `+1.35%`) | Long MP=`3.70310` (Vol: `5,966 USD`, Dist: `-3.11%`)
  * 3D Horizon: Short MP=`3.93050` (Vol: `5,237 USD`, Dist: `+2.84%`) | Long MP=`3.70300` (Vol: `6,804 USD`, Dist: `-3.11%`)
  * 7D Horizon: Short MP=`4.25750` (Vol: `16,582 USD`, Dist: `+11.63%`) | Long MP=`3.70100` (Vol: `9,842 USD`, Dist: `-2.96%`)
- **Exchange Cumulative Liquidation Cascades (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
  * 1D Cascade: Total=`0.00 USD` | Short Liq Pool=`0.00 USD` | Long Liq Pool=`0.00 USD` | Venues: Binance=`0.00 USD`, OKX=`0.00 USD`, Bybit=`0.00 USD`
  * 7D Cascade: Total=`0.00 USD` | Short Liq Pool=`0.00 USD` | Long Liq Pool=`0.00 USD` | Venues: Binance=`0.00 USD`, OKX=`0.00 USD`, Bybit=`0.00 USD`
- **Cross-Venue Liquidation Matrix & Heatmaps (14_Liquidation_Matrix.parquet, 7_Liq_Heapmap.parquet)**:
  * Liquidation Matrix Strike: Price=`0.00000` | Vol=`0 USD` | Cumulative=`0 USD` | Venue=`-` | Side=`-`
  * Multi-Timeframe Heatmap Density: 1h=`0.00 USD` | 4h=`0.00 USD` | 12h=`0.00 USD` | 24h=`0.00 USD`
- **Hyperdash Real-Time Liquidation & Retail Stop Protection (14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet)**:
  * Hyperdash Liq Cluster: Mark=`0.00 USD` | Cluster Price=`0.00 USD` | Dist=`-` | Cumulative=`0.00 USD` | Short=`0.00 USD` | Long=`0.00 USD` | Size=`-`
- **Live Forced Liquidation Momentum (7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)**:
  * Multi-Timeframe Forced Aggregates (5m): Long Liq=`0.00 USD` | Short Liq=`0.00 USD` | Total=`0.00 USD` | Net Delta=`0.00 USD` | Dominant=`BALANCED`

---

## 7. Derivatives Sentiment, Open Interest & Funding Dynamics
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet, 6_Funding_Fee_Settlement.parquet, 13_Hyperliquid.parquet)*
- **Aggregated Open Interest Breakdown (5_OI.parquet)**:
  * Total Open Interest: `0.00 USD` (`-`) | OI / 24h Volume Ratio: `0.0000`
  * OI Expansion Rate: 1h Change=`+0.00%` | 4h Change=`+0.00%` | 24h Change=`+0.00%`
  * Venue Concentration:
    - Binance: `0.00 USD` | Bybit: `0.00 USD` | OKX: `0.00 USD` | CME Institutional: `0.00 USD`
    - Gate: `0.00 USD` | MEXC: `0.00 USD` | Hyperliquid DEX: `0.00 USD` | Bitget: `0.00 USD`
    - KuCoin: `0.00 USD` | BingX: `0.00 USD` | Bitunix: `0.00 USD` | Others: `0.00 USD`
- **Cross-Exchange Perpetual Funding Rates (5_Funding_Rate.parquet)**:
  * Major CEX Rates: Binance=`+0.0100%` | OKX=`+0.0050%` | Bybit=`+0.0100%` | Bitget=`+0.0100%`
  * Mid-Tier CEX Rates: KuCoin=`+0.0100%` | MEXC=`+0.0100%` | Gate=`+0.0100%` | BingX=`+0.0070%` | Bitunix=`+0.0100%`
  * Alternative Venues: WhiteBIT=`+0.0100%` | LBank=`+0.0100%` | tradeXYZ=`-`
  * Inverse Coin-Margined: CoinM Binance=`+0.0000%` | CoinM OKX=`+0.0000%` | CoinM Bybit=`+0.0000%`
- **Exchange Long / Short Ratio Dynamics (3_Exchanges_LS_Ratio*.parquet)**:
  * 15m Tactical: L/S Ratio=`1.00` (Longs: `50.00%`, Shorts: `50.00%`, Total Vol: `0.00 USD`)
  * 1h Primary: L/S Ratio=`1.00` (Longs: `50.00%`, Shorts: `50.00%`, Total Vol: `0.00 USD`)
  * 4h Macro: L/S Ratio=`1.00` (Longs: `50.00%`, Shorts: `50.00%`, Total Vol: `0.00 USD`)
- **Funding Fee Settlement & DEX Arbitrage (6_Funding_Fee_Settlement.parquet, 13_Hyperliquid.parquet)**:
  * Settlement Payouts: Current Expected=`359.64 USD` | Last 24h=`560.56 USD` | Last 3D=`2.22K USD` | Last 7D=`3.82K USD`

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
- **Stand-Aside Reason**: Gate 1 Spread Friction Failure: Spread friction 560.75 bps exceeds cap 25.0 bps. Standing aside in 100% cash preserves statutory floor.