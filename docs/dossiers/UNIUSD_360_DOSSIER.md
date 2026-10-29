# 🔬 MASTER 43-FEED QUANTITATIVE DOSSIER: UNIUSD (Uniswap / USD)
**MT5 Symbol**: `UNIUSD.p` | **Category**: `Crypto Altcoin` | **Tier**: `Tier 2`
**Execution Posture**: `DISQUALIFIED` | **Timestamp**: 2026-10-29 14:43:14 UTC
**Pipeline Clearance**: `BLOCKED` | **Data Freshness**: `1.2m`

---

## 1. MT5 Live Broker Telemetry & Spread Friction Gate
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet)*
- **Live Bid Quote**: `7.20300` | **Live Ask Quote**: `7.22600` | **Mid Price**: `7.21450`
- **Spread Points**: `23.0 pts` | **Spread BPS**: `31.88 bps` (Mandatory Cap: `25.0 bps`)
- **Gate Status**: **`FAIL`** (Spread friction 31.88 bps exceeds cap 25.0 bps)
- **Order Allowed**: `NONE` | **Pillar 1 Clearance**: `BLOCKED`
- **Broker Specifications**: Contract Size=`1.00` | Tick Value=`1.00 USD` | Min Lot=`0.01` | Digits=`5`
- **Account Capital Context**: Balance=`4,744.55 USD` | Equity=`4,744.32 USD` | Free Margin=`4,342.62 USD` | Inviolate Hard Floor=`4,775.00 USD` (Cushion: `-30.68 USD`)
- **Pipeline Health**: Feed #00 Status=`PASS` | Overall Pipeline Telemetry=`33/33 FEEDS PASS (SYNCHRONIZED)`

---

## 2. Technical Profile, Multi-Sigma VWAP Dispersion & Volatility
*(Sources: 11_Technical.parquet, 11_Technical_BTC_Ribbon.parquet)*
- **Last Verified Price**: `7.16700` | **24h Change**: `+2.72%` (24h High: `7.33100`, 24h Low: `6.89400`)
- **Weekly Range**: Week High=`7.33100` | Week Low=`6.89400` | Daily POC=`7.00600` | Daily VAH=`7.19000` | Daily VAL=`6.92500`
- **Session VWAP**: `7.07816` | **Rolling 24h VWAP**: `7.10292` | **Distance to VWAP**: `+1.26%`
- **VWAP Z-Score**: `+0.91 sigma` | **Mean Reversion Bias**: **`FAIR VALUE`**
- **VWAP Dispersion Bands**:
  * +1.00 sigma: `7.17628` | -1.00 sigma: `6.98004`
  * +1.28 sigma (80% CI): `7.20375` | -1.28 sigma: `6.95257`
  * +2.00 sigma (95% CI): `7.27439` | -2.00 sigma: `6.88193`
  * +2.01 sigma: `7.27537` | -2.01 sigma: `6.88094`
  * +2.51 sigma (98.8% CI): `7.32443` | -2.51 sigma: `6.83189`
  * +3.00 sigma (99.7% CI Extreme): `7.37251` | -3.00 sigma: `6.78381`
- **Oscillators & Volatility**:
  * **RSI (14)**: `57.04` | **RSI State**: **`BULLISH`**
  * **ATR (14)**: `0.05463` | **ATR %**: `0.76%`
  * **Bollinger Bands**: Upper=`7.26065` | Mid=`7.11780` | Lower=`6.97495` | Bandwidth=`4.01%`
  * **MACD**: Line=`+0.0387` | Signal=`+0.0354` | Hist=`+0.0033`
- **Exponential Moving Average Ribbon (EMA)**:
  * Short Horizon: EMA-5=`7.17130` | EMA-9=`7.16500` | EMA-13=`7.15175` | EMA-20=`7.12982`
  * Intermediate: EMA-34=`7.10563` | EMA-50=`7.09668` | EMA-89=`7.09390` | EMA-100=`7.09389`
  * Institutional: EMA-144=`7.09204` | EMA-200=`7.08485` (Slope: `+0.150%`) | EMA-233=`7.08170` (Slope: `+0.132%`)
  * **Trend Bias**: **`STRONG BULLISH`**

---

## 3. Auction Market Structure & Value Profile
*(Sources: 20_Auction_Market_Structure.parquet)*
- **Daily Auction Value Area**:
  * High (VAH): `7.19000` | Point of Control (POC): `7.00600` | Low (VAL): `6.92500`
  * Distance to POC: `+2.95%` | Distance to VAH: `+0.32%` | Distance to VAL: `+4.16%`
  * **Value Area Position**: **`ABOVE_VALUE (Imbalance)`** | **Auction Regime**: **`RANGE_EXPANSION`** | **Session Bias**: **`BULLISH (Above Pivot)`**
- **Prior Day & Weekly Auction Profile**:
  * Prior Day: PD VAH=`7.17800` | PD POC=`7.05100` | PD VAL=`7.02600` | PDH=`7.32200` | PDL=`6.95400` | PDC=`7.22300`
  * Monday Reference: Monday High=`7.17300` | Monday Low=`6.75900` | Monday Mid=`6.96600`
  * Weekly Value Area: Weekly VAH=`7.17300` | Weekly POC=`7.04300` | Weekly VAL=`6.96300`
  * Multi-Week Extremes: Current Week High (CWH)=`7.33100` | CWL=`6.75900` | Prior Week High (PWH)=`7.76400` | PWL=`6.50200`
  * Multi-Month Extremes: Current Month High (CMH)=`9.30700` | CML=`6.50200` | Prior Month High (PMH)=`10.89800` | PML=`5.16500`
- **Session Liquidity Extremes & Initial Balance**:
  * Asian Session: Range `[6.89400 - 7.33100]`
  * London Session: Range `[6.95200 - 7.22200]`
  * New York Session: Range `[6.99900 - 7.25200]`
  * Initial Balance (IB): IB High=`7.12100` | IB Low=`7.01900`
- **Fibonacci Golden Pocket & Optimal Trade Entry (OTE)**:
  * Swing Range: High=`7.33100` | Low=`6.89400` | Direction=`BEARISH_IMPULSE`
  * Golden Pocket [0.618 - 0.65]: `[7.16400 - 7.17800]`
  * Optimal Trade Entry (0.702): `7.20100` | Invalidation Level: `7.23700` | Status: **`DEEP_SHELF_TEST (0.786)`**
- **Classical & Weekly Pivots**:
  * Daily Classical: Pivot=`7.16600` | R1=`7.37900` | S1=`7.01100` | R2=`7.53400` | S2=`6.79800`
  * Weekly Classical: Weekly Pivot=`7.07100` | Weekly R1=`7.64000` | Weekly S1=`6.37800`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Orderflow
*(Sources: 18_CVD.parquet, 18_CVD_30D_5m.parquet, 18_CVD_30D_15m.parquet, 18_CVD_30D_1h.parquet, 18_CVD_30D_4h.parquet, 18_CVD_30D_ALL.parquet, 21_Tradfye_Orderflow.parquet)*
- **Interbank Spot Orderflow Mechanics**: Decentralized OTC market structure. CVD taker deltas do not apply to interbank spot flow. Tape volume governed by broker tick volume with live spread friction of `31.88 bps`.
- **Session Volume Structure**: Price operating at `ABOVE_VALUE (Imbalance)` with Daily POC at `7.00600` (VAH: `7.19000` / VAL: `6.92500`).

---

## 5. Institutional Whale Armor & Resting Orderbook Depth
*(Sources: 10_Whale_Orders.parquet, 12_Hyperdash.parquet, 17_Orderbook.parquet, 4_Hyperliquid_Analysis.parquet)*
- **Defending Resting Whale Walls (10_Whale_Orders.parquet)**:
  * Defending Bid Wall: `7.16600` (`41724.8116` coins / `299,000.00 USD` on `Hyperliquid`, persistent for `9s`, Traded: `0.0%`, Order ID: `CG_WHALE_UNI_T_62`)
  * Defending Ask Wall: `7.27700` (`58678.0267` coins / `427,000.00 USD` on `Binance`, persistent for `33s`, Traded: `0.0%`, Order ID: `CG_LADDER_UNI_6`)
  * Total Whale Armor Pool: Bids Pool=`13,208,300.00 USD` | Asks Pool=`12,779,100.00 USD` (Tracked Orders: `190`)
- **Hyperdash Resting Depth & L3 Telemetry (12_Hyperdash.parquet)**:
  * `NEUTRAL`: `0.00 USD` @ `0.00000` (Size: `0.0`, Detail: Delta: +0, Wallet: None, Timestamp: 2026-10-29 19:44:05 IST)
- **Hyperliquid Elite Trader Positioning (4_Hyperliquid_Analysis.parquet)**:
  * Wallet `0x53969485d7...` (0x5396...8b79): `Long` `7,217,298.56 USD` (999,999.8000 UNI, Margin: 1,443,459.71 USD, Leverage: 5X Cross, Entry: 6.8807 USD, Current: 7.2132 USD, Est Liq: 5.6630 USD, PnL: +336,600.23 USD [+4.66%], Fees: +8,699.46 USD)
  * Wallet `0x9df286bcee...` (0x9df2...c665): `Short` `3,248,325.00 USD` (450,000.0000 UNI, Margin: 324,832.50 USD, Leverage: 10X Cross, Entry: 4.4911 USD, Current: 7.2132 USD, Est Liq: 70.9738 USD, PnL: -1,227,324.87 USD [-37.78%], Fees: -78,664.09 USD)
  * Wallet `0xdd53c52973...` (0xdd53...2b13): `Short` `2,595,395.21 USD` (359,478.0000 UNI, Margin: 865,131.74 USD, Leverage: 3X Cross, Entry: 7.2870 USD, Current: 7.2132 USD, Est Liq: 159.8962 USD, PnL: +24,109.27 USD [+0.93%], Fees: -4,958.78 USD)

---

## 6. Liquidation Max Pain, Heatmaps & Cascade Boundaries
*(Sources: 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 14_Hyperdash_Liq_Map.parquet, 14_Liquidation_Matrix.parquet, 15_Hyperdash_Stops_Map.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`7.42850` (Vol: `470,100 USD`, Dist: `+2.56%`) | Long MP=`6.90850` (Vol: `353,400 USD`, Dist: `-4.62%`)
  * 48H Horizon: Short MP=`7.42850` (Vol: `404,800 USD`, Dist: `+2.56%`) | Long MP=`6.90850` (Vol: `378,300 USD`, Dist: `-4.62%`)
  * 3D Horizon: Short MP=`7.35050` (Vol: `437,300 USD`, Dist: `+1.48%`) | Long MP=`6.90850` (Vol: `643,300 USD`, Dist: `-4.62%`)
  * 7D Horizon: Short MP=`7.42960` (Vol: `619,800 USD`, Dist: `+2.58%`) | Long MP=`6.91120` (Vol: `661,400 USD`, Dist: `-4.58%`)
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
  * Major CEX Rates: Binance=`+0.0100%` | OKX=`+0.0100%` | Bybit=`-0.0001%` | Bitget=`+0.0026%`
  * Mid-Tier CEX Rates: KuCoin=`+0.0100%` | MEXC=`+0.0100%` | Gate=`-0.0037%` | BingX=`+0.0100%` | Bitunix=`+0.0100%`
  * Alternative Venues: WhiteBIT=`-0.0095%` | LBank=`+0.0100%` | tradeXYZ=`-`
  * Inverse Coin-Margined: CoinM Binance=`+0.0100%` | CoinM OKX=`+0.0100%` | CoinM Bybit=`+0.0100%`
- **Exchange Long / Short Ratio Dynamics (3_Exchanges_LS_Ratio*.parquet)**:
  * 15m Tactical: L/S Ratio=`1.00` (Longs: `50.00%`, Shorts: `50.00%`, Total Vol: `0.00 USD`)
  * 1h Primary: L/S Ratio=`1.00` (Longs: `50.00%`, Shorts: `50.00%`, Total Vol: `0.00 USD`)
  * 4h Macro: L/S Ratio=`1.00` (Longs: `50.00%`, Shorts: `50.00%`, Total Vol: `0.00 USD`)
- **Funding Fee Settlement & DEX Arbitrage (6_Funding_Fee_Settlement.parquet, 13_Hyperliquid.parquet)**:
  * Settlement Payouts: Current Expected=`21.71K USD` | Last 24h=`60.93K USD` | Last 3D=`140.85K USD` | Last 7D=`214.96K USD`

---

## 8. Microstructure Footprint, Tape Imbalances & Macro Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 16_Hyperdash_telegram_Intel.parquet, 19_News.parquet, 19_Calendar.parquet)*
- **Bar-by-Bar Microstructure Footprint (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
  * Venue Source: `CoinGlass-AggregatedFutures(Binance)` | Timeframe: `15m` | Last Price: `7.21450`
  * Footprint Auction Profile: Bar VWAP=`7.19810` | Bar POC=`7.20450` | Bar VAH=`7.21550` | Bar VAL=`7.17550`
  * Orderflow Volumes: Total Vol=`1,351,066.39 USD` | Taker Buy=`695,594.09 USD` | Taker Sell=`655,472.30 USD`
  * Bar Delta Profile: Delta=`+40,121.79 USD` (`+2.97%`) | Max Delta=`+145,180.81 USD` | Min Delta=`-1,514.25 USD` | Cumulative Bar Delta=`-3,232,662.25 USD`
  * Order Execution Dynamics: Trades Count=`7,065` | Avg Trade Size=`191.23 USD`
  * Tape Imbalances: Imbalance Ratio=`300.0%` | Buy Imbalances Count=`2` | Sell Imbalances Count=`3`
  * Footprint Open Interest: Bar OI=`0.00 USD` | Bar OI Change=`+0.00 USD`
- **CoinGlass Algorithmic Footprint Signals (25_CoinGlass_Footprint_Signals.parquet)**:
  * Signal Classification: Type=`Exhaustion` | Bias: **`BULLISH`** | Signal Time=`10-28 05:38` | Timeframe=`Range 0.02`
  * Signal Context: Headline=`Seller exhaustion` | Price Level=`7.04200` | Absorbed Volume=`0.00 USD`
  * Bar Footprint Context: Current Bar Delta=`+0.00 USD` | Current Bar Volume=`0.00 USD` | Delta in View=`+0.00 USD`
  * Historical Detail: `New 10-bar low with almost no volume in the bottom 10% of the bar, closed in the upper half, bullish · 7.0420` | KPI=`—` | Bias=`—`
- **Multi-Horizon Macro Capital Netflows (2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet)**:
  * Spot Capital Netflows:
    - Tactical: 5m=`+135.74K` | 15m=`+93.01K` | 30m=`+369.85K` | 1h=`-42.66K`
    - Intermediate: 2h=`-95.77K` | 4h=`+464.76K` | 6h=`+23.38K` | 8h=`+85.72K` | 12h=`-163.10K` | 24h=`+2.28M`
    - Macro Horizons: 1-Week=`-7.43M` | 15-Day=`-12.44M` | 30-Day=`-44.67M` | Market Cap=`4.49B`
  * Futures Capital Netflows:
    - Tactical: 5m=`-68.61K` | 15m=`+126.90K` | 30m=`+1.39M` | 1h=`-3.99M`
    - Intermediate: 2h=`-3.64M` | 4h=`-4.52M` | 6h=`-4.36M` | 8h=`-6.14M` | 12h=`-7.69M` | 24h=`-12.60M`
    - Macro Horizons: 1-Week=`-56.93M` | 15-Day=`-124.17M` | 30-Day=`-484.60M` | Market Cap=`4.49B`
- **Telegram Intelligence Alert**: `[MARKET_INTEL] #UNI Liquidated Long: 8.08K USD at 7.2493 USD [API] (Impact: NEWS_INTEL)`

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
- **Stand-Aside Reason**: Gate 1 Spread Friction Failure: Spread friction 31.88 bps exceeds cap 25.0 bps. Standing aside in 100% cash preserves statutory floor.