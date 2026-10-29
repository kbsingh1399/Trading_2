# 🔬 MASTER 43-FEED QUANTITATIVE DOSSIER: AXSUSD (Axie Infinity / USD)
**MT5 Symbol**: `AXSUSD.p` | **Category**: `Crypto Altcoin` | **Tier**: `Tier 2`
**Execution Posture**: `DISQUALIFIED` | **Timestamp**: 2026-10-29 14:43:14 UTC
**Pipeline Clearance**: `BLOCKED` | **Data Freshness**: `1.2m`

---

## 1. MT5 Live Broker Telemetry & Spread Friction Gate
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet)*
- **Live Bid Quote**: `0.83000` | **Live Ask Quote**: `1.04000` | **Mid Price**: `0.93500`
- **Spread Points**: `21.0 pts` | **Spread BPS**: `2245.99 bps` (Mandatory Cap: `25.0 bps`)
- **Gate Status**: **`FAIL`** (Spread friction 2245.99 bps exceeds cap 25.0 bps)
- **Order Allowed**: `NONE` | **Pillar 1 Clearance**: `BLOCKED`
- **Broker Specifications**: Contract Size=`1.00` | Tick Value=`1.00 USD` | Min Lot=`0.01` | Digits=`5`
- **Account Capital Context**: Balance=`4,744.55 USD` | Equity=`4,744.32 USD` | Free Margin=`4,342.62 USD` | Inviolate Hard Floor=`4,775.00 USD` (Cushion: `-30.68 USD`)
- **Pipeline Health**: Feed #00 Status=`PASS` | Overall Pipeline Telemetry=`33/33 FEEDS PASS (SYNCHRONIZED)`

---

## 2. Technical Profile, Multi-Sigma VWAP Dispersion & Volatility
*(Sources: 11_Technical.parquet, 11_Technical_BTC_Ribbon.parquet)*
- **Last Verified Price**: `0.83000` | **24h Change**: `-1.19%` (24h High: `0.88000`, 24h Low: `0.81000`)
- **Weekly Range**: Week High=`0.88000` | Week Low=`0.81000` | Daily POC=`0.82000` | Daily VAH=`0.84000` | Daily VAL=`0.81000`
- **Session VWAP**: `0.82662` | **Rolling 24h VWAP**: `0.83877` | **Distance to VWAP**: `+0.41%`
- **VWAP Z-Score**: `+0.31 sigma` | **Mean Reversion Bias**: **`FAIR VALUE`**
- **VWAP Dispersion Bands**:
  * +1.00 sigma: `0.83763` | -1.00 sigma: `0.81561`
  * +1.28 sigma (80% CI): `0.84071` | -1.28 sigma: `0.81253`
  * +2.00 sigma (95% CI): `0.84864` | -2.00 sigma: `0.80460`
  * +2.01 sigma: `0.84875` | -2.01 sigma: `0.80449`
  * +2.51 sigma (98.8% CI): `0.85425` | -2.51 sigma: `0.79898`
  * +3.00 sigma (99.7% CI Extreme): `0.85965` | -3.00 sigma: `0.79359`
- **Oscillators & Volatility**:
  * **RSI (14)**: `57.23` | **RSI State**: **`BULLISH`**
  * **ATR (14)**: `0.00347` | **ATR %**: `0.42%`
  * **Bollinger Bands**: Upper=`0.83604` | Mid=`0.82650` | Lower=`0.81696` | Bandwidth=`2.31%`
  * **MACD**: Line=`+0.0016` | Signal=`+0.0011` | Hist=`+0.0005`
- **Exponential Moving Average Ribbon (EMA)**:
  * Short Horizon: EMA-5=`0.82977` | EMA-9=`0.82913` | EMA-13=`0.82833` | EMA-20=`0.82724`
  * Intermediate: EMA-34=`0.82714` | EMA-50=`0.82895` | EMA-89=`0.83427` | EMA-100=`0.83551`
  * Institutional: EMA-144=`0.83890` | EMA-200=`0.84079` (Slope: `-0.176%`) | EMA-233=`0.84172` (Slope: `-0.161%`)
  * **Trend Bias**: **`NEUTRAL / CHOP`**

---

## 3. Auction Market Structure & Value Profile
*(Sources: 20_Auction_Market_Structure.parquet)*
- **Daily Auction Value Area**:
  * High (VAH): `0.84000` | Point of Control (POC): `0.82000` | Low (VAL): `0.81000`
  * Distance to POC: `+13.44%` | Distance to VAH: `+10.95%` | Distance to VAL: `+14.79%`
  * **Value Area Position**: **`ABOVE_VALUE (Imbalance)`** | **Auction Regime**: **`TREND_UP_ACCEPTANCE`** | **Session Bias**: **`BULLISH (Above Pivot)`**
- **Prior Day & Weekly Auction Profile**:
  * Prior Day: PD VAH=`0.87000` | PD POC=`0.86000` | PD VAL=`0.85000` | PDH=`0.88000` | PDL=`0.84000` | PDC=`0.86000`
  * Monday Reference: Monday High=`0.86000` | Monday Low=`0.82000` | Monday Mid=`0.84000`
  * Weekly Value Area: Weekly VAH=`0.86000` | Weekly POC=`0.84000` | Weekly VAL=`0.84000`
  * Multi-Week Extremes: Current Week High (CWH)=`0.88000` | CWL=`0.81000` | Prior Week High (PWH)=`0.97000` | PWL=`0.82000`
  * Multi-Month Extremes: Current Month High (CMH)=`1.35000` | CML=`0.81000` | Prior Month High (PMH)=`1.13000` | PML=`0.78000`
- **Session Liquidity Extremes & Initial Balance**:
  * Asian Session: Range `[0.81000 - 0.87000]`
  * London Session: Range `[0.81000 - 0.83000]`
  * New York Session: Range `[0.82000 - 0.84000]`
  * Initial Balance (IB): IB High=`0.83000` | IB Low=`0.82000`
- **Fibonacci Golden Pocket & Optimal Trade Entry (OTE)**:
  * Swing Range: High=`0.88000` | Low=`0.81000` | Direction=`BEARISH_IMPULSE`
  * Golden Pocket [0.618 - 0.65]: `[0.85000 - 0.86000]`
  * Optimal Trade Entry (0.702): `0.86000` | Invalidation Level: `0.87000` | Status: **`STRUCTURE_INVALIDATED`**
- **Classical & Weekly Pivots**:
  * Daily Classical: Pivot=`0.86000` | R1=`0.88000` | S1=`0.84000` | R2=`0.90000` | S2=`0.82000`
  * Weekly Classical: Weekly Pivot=`0.88000` | Weekly R1=`0.93000` | Weekly S1=`0.78000`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Orderflow
*(Sources: 18_CVD.parquet, 18_CVD_30D_5m.parquet, 18_CVD_30D_15m.parquet, 18_CVD_30D_1h.parquet, 18_CVD_30D_4h.parquet, 18_CVD_30D_ALL.parquet, 21_Tradfye_Orderflow.parquet)*
- **Interbank Spot Orderflow Mechanics**: Decentralized OTC market structure. CVD taker deltas do not apply to interbank spot flow. Tape volume governed by broker tick volume with live spread friction of `2245.99 bps`.
- **Session Volume Structure**: Price operating at `ABOVE_VALUE (Imbalance)` with Daily POC at `0.82000` (VAH: `0.84000` / VAL: `0.81000`).

---

## 5. Institutional Whale Armor & Resting Orderbook Depth
*(Sources: 10_Whale_Orders.parquet, 12_Hyperdash.parquet, 17_Orderbook.parquet, 4_Hyperliquid_Analysis.parquet)*
- **Interbank Institutional Tier-1 Depth**: Decentralized OTC spot liquidity. Resting whale limit walls from crypto venues do not apply.
- **Verified Broker Armor**: Live Bid `0.83000` / Live Ask `1.04000` with institutional spread of `2245.99 bps`. Structural defense anchored at Asian Range `[0.81000 - 0.87000]` and London Range `[0.81000 - 0.83000]`.

---

## 6. Liquidation Max Pain, Heatmaps & Cascade Boundaries
*(Sources: 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 14_Hyperdash_Liq_Map.parquet, 14_Liquidation_Matrix.parquet, 15_Hyperdash_Stops_Map.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`0.96636` (Vol: `19,660 USD`, Dist: `+0.97%`) | Long MP=`0.92862` (Vol: `15,710 USD`, Dist: `-2.98%`)
  * 48H Horizon: Short MP=`0.96436` (Vol: `25,085 USD`, Dist: `+0.76%`) | Long MP=`0.92802` (Vol: `23,037 USD`, Dist: `-3.04%`)
  * 3D Horizon: Short MP=`0.96883` (Vol: `25,470 USD`, Dist: `+1.23%`) | Long MP=`0.91537` (Vol: `28,937 USD`, Dist: `-4.36%`)
  * 7D Horizon: Short MP=`0.96640` (Vol: `39,137 USD`, Dist: `+1.26%`) | Long MP=`0.91662` (Vol: `35,732 USD`, Dist: `-3.96%`)
- **Exchange Cumulative Liquidation Cascades (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
  * 1D Cascade: Total=`0.00 USD` | Short Liq Pool=`0.00 USD` | Long Liq Pool=`0.00 USD` | Venues: Binance=`0.00 USD`, OKX=`0.00 USD`, Bybit=`0.00 USD`
  * 7D Cascade: Total=`0.00 USD` | Short Liq Pool=`0.00 USD` | Long Liq Pool=`0.00 USD` | Venues: Binance=`0.00 USD`, OKX=`0.00 USD`, Bybit=`0.00 USD`
- **Cross-Venue Liquidation Matrix & Heatmaps (14_Liquidation_Matrix.parquet, 7_Liq_Heapmap.parquet)**:
  * Liquidation Matrix Strike: Price=`1.60750` | Vol=`13,570 USD` | Cumulative=`13,910 USD` | Venue=`Hyperliquid L1` | Side=`Short Liquidation`
  * Multi-Timeframe Heatmap Density: 1h=`0.00 USD` | 4h=`0.00 USD` | 12h=`0.00 USD` | 24h=`0.00 USD`
- **Hyperdash Real-Time Liquidation & Retail Stop Protection (14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet)**:
  * Hyperdash Liq Cluster: Mark=`0.933400 USD` | Cluster Price=`1.6075 USD` | Dist=`+72.22%` | Cumulative=`13.91K USD` | Short=`13.57K USD` | Long=`0 USD` | Size=`8,442.7000 AXS`
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
  * Major CEX Rates: Binance=`+0.0050%` | OKX=`+0.0050%` | Bybit=`+0.0100%` | Bitget=`+0.0050%`
  * Mid-Tier CEX Rates: KuCoin=`+0.0050%` | MEXC=`+0.0050%` | Gate=`+0.0100%` | BingX=`+0.0050%` | Bitunix=`+0.0050%`
  * Alternative Venues: WhiteBIT=`+0.0050%` | LBank=`+0.0050%` | tradeXYZ=`-`
  * Inverse Coin-Margined: CoinM Binance=`+0.0000%` | CoinM OKX=`+0.0000%` | CoinM Bybit=`+0.0000%`
- **Exchange Long / Short Ratio Dynamics (3_Exchanges_LS_Ratio*.parquet)**:
  * 15m Tactical: L/S Ratio=`1.00` (Longs: `50.00%`, Shorts: `50.00%`, Total Vol: `0.00 USD`)
  * 1h Primary: L/S Ratio=`1.00` (Longs: `50.00%`, Shorts: `50.00%`, Total Vol: `0.00 USD`)
  * 4h Macro: L/S Ratio=`1.00` (Longs: `50.00%`, Shorts: `50.00%`, Total Vol: `0.00 USD`)
- **Funding Fee Settlement & DEX Arbitrage (6_Funding_Fee_Settlement.parquet, 13_Hyperliquid.parquet)**:
  * Settlement Payouts: Current Expected=`506.28 USD` | Last 24h=`593.92 USD` | Last 3D=`3.19K USD` | Last 7D=`2.12K USD`

---

## 8. Microstructure Footprint, Tape Imbalances & Macro Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 16_Hyperdash_telegram_Intel.parquet, 19_News.parquet, 19_Calendar.parquet)*
- **Bar-by-Bar Microstructure Footprint (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
  * Venue Source: `Aggregated` | Timeframe: `15m` | Last Price: `0.93500`
  * Footprint Auction Profile: Bar VWAP=`0.93500` | Bar POC=`0.93500` | Bar VAH=`0.93687` | Bar VAL=`0.93313`
  * Orderflow Volumes: Total Vol=`0.00 USD` | Taker Buy=`0.00 USD` | Taker Sell=`0.00 USD`
  * Bar Delta Profile: Delta=`+0.00 USD` (`+0.00%`) | Max Delta=`+0.00 USD` | Min Delta=`+0.00 USD` | Cumulative Bar Delta=`+0.00 USD`
  * Order Execution Dynamics: Trades Count=`0` | Avg Trade Size=`0.00 USD`
  * Tape Imbalances: Imbalance Ratio=`0.0%` | Buy Imbalances Count=`0` | Sell Imbalances Count=`0`
  * Footprint Open Interest: Bar OI=`0.00 USD` | Bar OI Change=`+0.00 USD`
- **Multi-Horizon Macro Capital Netflows (2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet)**:
  * Spot Capital Netflows:
    - Tactical: 5m=`+542.13` | 15m=`+4.56K` | 30m=`+8.96K` | 1h=`-6.55K`
    - Intermediate: 2h=`-7.00K` | 4h=`+5.71K` | 6h=`+32.18K` | 8h=`+19.51K` | 12h=`-28.92K` | 24h=`-197.56K`
    - Macro Horizons: 1-Week=`-1.74M` | 15-Day=`-3.47M` | 30-Day=`-26.41M` | Market Cap=`163.99M`
  * Futures Capital Netflows:
    - Tactical: 5m=`+495.18` | 15m=`-4.22K` | 30m=`-17.52K` | 1h=`-38.60K`
    - Intermediate: 2h=`-12.64K` | 4h=`-121.76K` | 6h=`-145.99K` | 8h=`-230.53K` | 12h=`-467.12K` | 24h=`-526.00K`
    - Macro Horizons: 1-Week=`-2.77M` | 15-Day=`-3.69M` | 30-Day=`-25.61M` | Market Cap=`163.99M`

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
- **Stand-Aside Reason**: Gate 1 Spread Friction Failure: Spread friction 2245.99 bps exceeds cap 25.0 bps. Standing aside in 100% cash preserves statutory floor.