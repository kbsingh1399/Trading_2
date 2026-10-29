# 🔬 MASTER 43-FEED QUANTITATIVE DOSSIER: APT (Aptos)
**MT5 Symbol**: `APTUSD.p` | **Category**: `Crypto Alt L1` | **Tier**: `Tier 1`
**Execution Posture**: `PASSIVE_MAKER_LIMIT_ONLY` | **Timestamp**: 2026-10-29 14:43:14 UTC
**Pipeline Clearance**: `DISQUALIFIED` | **Data Freshness**: `1.2m`

---

## 1. MT5 Live Broker Telemetry & Spread Friction Gate
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet)*
- **Live Bid Quote**: `0.69000` | **Live Ask Quote**: `0.69000` | **Mid Price**: `0.69000`
- **Spread Points**: `0.0 pts` | **Spread BPS**: `999.00 bps` (Mandatory Cap: `25.0 bps`)
- **Gate Status**: **`FAIL`** (UNLISTED_ON_MT5_BROKER (Zero broker telemetry stream))
- **Order Allowed**: `BUY_LIMIT / SELL_LIMIT` | **Pillar 1 Clearance**: `DISQUALIFIED`
- **Broker Specifications**: Contract Size=`1.00` | Tick Value=`1.00 USD` | Min Lot=`0.01` | Digits=`5`
- **Account Capital Context**: Balance=`4,744.55 USD` | Equity=`4,744.32 USD` | Free Margin=`4,342.62 USD` | Inviolate Hard Floor=`4,775.00 USD` (Cushion: `-30.68 USD`)
- **Pipeline Health**: Feed #00 Status=`PASS` | Overall Pipeline Telemetry=`33/33 FEEDS PASS (SYNCHRONIZED)`

---

## 2. Technical Profile, Multi-Sigma VWAP Dispersion & Volatility
*(Sources: 11_Technical.parquet, 11_Technical_BTC_Ribbon.parquet)*
- **Live Quote Baseline**: Last Mid Price=`0.69000` | Spread=`999.00 bps` (0.0 pts)
- **Empirical Status**: Asset indicator stream unindexed in 11_Technical collector snapshot. Mathematical indicators reference live MT5 Bid/Ask quotes and session auction structures.

---

## 3. Auction Market Structure & Value Profile
*(Sources: 20_Auction_Market_Structure.parquet)*
- **Daily Auction Value Area**:
  * High (VAH): `0.69207` | Point of Control (POC): `0.69000` | Low (VAL): `0.68793`
  * Distance to POC: `+0.00%` | Distance to VAH: `+0.00%` | Distance to VAL: `+0.00%`
  * **Value Area Position**: **`INSIDE_VALUE (Balance)`** | **Auction Regime**: **`BALANCED_AUCTION`** | **Session Bias**: **`NEUTRAL`**
- **Prior Day & Weekly Auction Profile**:
  * Prior Day: PD VAH=`0.69276` | PD POC=`0.69000` | PD VAL=`0.68724` | PDH=`0.69414` | PDL=`0.68586` | PDC=`0.69000`
  * Monday Reference: Monday High=`0.69345` | Monday Low=`0.68655` | Monday Mid=`0.69000`
  * Weekly Value Area: Weekly VAH=`0.69552` | Weekly POC=`0.69000` | Weekly VAL=`0.68448`
  * Multi-Week Extremes: Current Week High (CWH)=`0.69690` | CWL=`0.68310` | Prior Week High (PWH)=`0.70035` | PWL=`0.67965`
  * Multi-Month Extremes: Current Month High (CMH)=`0.70380` | CML=`0.67620` | Prior Month High (PMH)=`0.70725` | PML=`0.67275`
- **Session Liquidity Extremes & Initial Balance**:
  * Asian Session: Range `[0.68862 - 0.69138]`
  * London Session: Range `[0.68724 - 0.69276]`
  * New York Session: Range `[0.68655 - 0.69345]`
  * Initial Balance (IB): IB High=`0.69207` | IB Low=`0.68793`
- **Fibonacci Golden Pocket & Optimal Trade Entry (OTE)**:
  * Swing Range: High=`0.69690` | Low=`0.68310` | Direction=`NONE`
  * Golden Pocket [0.618 - 0.65]: `[0.68862 - 0.69138]`
  * Optimal Trade Entry (0.702): `0.69000` | Invalidation Level: `0.00000` | Status: **`NONE`**
- **Classical & Weekly Pivots**:
  * Daily Classical: Pivot=`0.69000` | R1=`0.69207` | S1=`0.68793` | R2=`0.69414` | S2=`0.68586`
  * Weekly Classical: Weekly Pivot=`0.69000` | Weekly R1=`0.69690` | Weekly S1=`0.68310`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Orderflow
*(Sources: 18_CVD.parquet, 18_CVD_30D_5m.parquet, 18_CVD_30D_15m.parquet, 18_CVD_30D_1h.parquet, 18_CVD_30D_4h.parquet, 18_CVD_30D_ALL.parquet, 21_Tradfye_Orderflow.parquet)*
- **Primary 15m CVD Microstructure (18_CVD_30D_15m.parquet)**:
  * Candle Delta: `-15,543.23 USD` (Base: `-23,244.9000 coins`) | Delta %: `-3.06%`
  * Taker Volumes: Taker Buy=`245,864.74 USD` | Taker Sell=`261,407.98 USD` | Total Vol=`744,838.50 USD`
  * Cumulative CVD: `-2,155,449.62 USD` (Base: `-3,175,622.6000`)
  * Rolling CVD Z-Score: `-0.21 sigma` | Price Return: `-0.10%`
  * **Delta Regime**: **`NEUTRAL CHOP`** | Trades Count: `5,783`
- **Multi-Timeframe Delta Comparison**:
  * 5m Bar: Delta=`+5,420.89 USD` | Delta %=`+9.38%` | Z-Score=`+0.05` | Regime=`DELTA ALIGNED`
  * 1h Bar: Delta=`-15,543.23 USD` | Delta %=`-3.06%` | Z-Score=`+0.43` | Regime=`NEUTRAL CHOP`
  * 4h Bar: Delta=`+104,162.58 USD` | Delta %=`+2.45%` | Z-Score=`+1.23` | Regime=`NEUTRAL CHOP`
  * 30D Consolidated (ALL): Cumulative Trend=`-2,247,782.31 USD` | Long-Term Regime=`NEUTRAL CHOP`
- **Institutional Footprint & Deribit Options Armor (21_Tradfye_Orderflow.parquet)**:
  * Candle VWAP: `0.66534` | Estimated POC: `0.66607` | Avg Trade Size: `80.06 USD`
  * Net Delta USD: `+38,467.19 USD` | Net Delta %: `+15.03%` | Orderflow CVD: `+38,467.19 USD`
  * Orderflow Regime: **`AGGRESSIVE_BUYER_DOMINATION`** | Orderflow Divergence: **`BULLISH_EXPANSION`**
  * Deribit Options Walls: Max Pain=`0.00` | Call Wall=`0.00` | Put Wall=`0.00`

---

## 5. Institutional Whale Armor & Resting Orderbook Depth
*(Sources: 10_Whale_Orders.parquet, 12_Hyperdash.parquet, 17_Orderbook.parquet, 4_Hyperliquid_Analysis.parquet)*
- **Defending Resting Whale Walls (10_Whale_Orders.parquet)**:
  * Defending Bid Wall: `0.00000` (`0.0000` coins / `0.00 USD` on `-`, persistent for `-`, Traded: `0.0%`, Order ID: `-`)
  * Defending Ask Wall: `0.00000` (`0.0000` coins / `0.00 USD` on `-`, persistent for `-`, Traded: `0.0%`, Order ID: `-`)
  * Total Whale Armor Pool: Bids Pool=`0.00 USD` | Asks Pool=`0.00 USD` (Tracked Orders: `0`)
- **Hyperdash Resting Depth & L3 Telemetry (12_Hyperdash.parquet)**:
  * `NEUTRAL`: `0.00 USD` @ `0.00000` (Size: `0.0`, Detail: Delta: +0, Wallet: None, Timestamp: 2026-10-29 19:44:05 IST)

---

## 6. Liquidation Max Pain, Heatmaps & Cascade Boundaries
*(Sources: 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 14_Hyperdash_Liq_Map.parquet, 14_Liquidation_Matrix.parquet, 15_Hyperdash_Stops_Map.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`0.70605` (Vol: `90,823 USD`, Dist: `+2.43%`) | Long MP=`0.67183` (Vol: `39,957 USD`, Dist: `-2.53%`)
  * 48H Horizon: Short MP=`0.70554` (Vol: `81,903 USD`, Dist: `+2.36%`) | Long MP=`0.67020` (Vol: `45,047 USD`, Dist: `-2.77%`)
  * 3D Horizon: Short MP=`0.72100` (Vol: `125,191 USD`, Dist: `+4.60%`) | Long MP=`0.67030` (Vol: `75,399 USD`, Dist: `-2.76%`)
  * 7D Horizon: Short MP=`0.85389` (Vol: `187,281 USD`, Dist: `+24.46%`) | Long MP=`0.66997` (Vol: `92,437 USD`, Dist: `-2.35%`)
- **Exchange Cumulative Liquidation Cascades (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
  * 1D Cascade: Total=`1.81M USD` | Short Liq Pool=`1.81M USD` | Long Liq Pool=`0 USD` | Venues: Binance=`0 USD`, OKX=`1.00K USD`, Bybit=`2.53K USD`
  * 7D Cascade: Total=`6.54M USD` | Short Liq Pool=`6.54M USD` | Long Liq Pool=`0 USD` | Venues: Binance=`29.14K USD`, OKX=`4.26K USD`, Bybit=`96.75 USD`
- **Cross-Venue Liquidation Matrix & Heatmaps (14_Liquidation_Matrix.parquet, 7_Liq_Heapmap.parquet)**:
  * Liquidation Matrix Strike: Price=`1.32950` | Vol=`285 USD` | Cumulative=`618,860 USD` | Venue=`Hyperliquid L1` | Side=`Short Liquidation`
  * Multi-Timeframe Heatmap Density: 1h=`0.00 USD` | 4h=`0.00 USD` | 12h=`0.00 USD` | 24h=`0.00 USD`
- **Hyperdash Real-Time Liquidation & Retail Stop Protection (14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet)**:
  * Hyperdash Liq Cluster: Mark=`0.683000 USD` | Cluster Price=`1.3295 USD` | Dist=`+94.66%` | Cumulative=`618.86K USD` | Short=`284.61 USD` | Long=`0 USD` | Size=`214.0700 APT`
  * **Retail Stops Map (Pitfall 2 & 4 Defense)**:
    - `Sell Stop`: `0.350500 USD` (Dist: `-48.68%`, Cumulative Stops: `123.18K USD`, Buy: `0 USD`, Sell: `340.19 USD`, Coins: `970.5800 APT`)
    - `Sell Stop`: `0.463500 USD` (Dist: `-32.14%`, Cumulative Stops: `122.84K USD`, Buy: `0 USD`, Sell: `104.57 USD`, Coins: `225.6000 APT`)
    - `Sell Stop`: `0.480500 USD` (Dist: `-29.65%`, Cumulative Stops: `122.73K USD`, Buy: `0 USD`, Sell: `14.74K USD`, Coins: `30,675.4000 APT`)
- **Live Forced Liquidation Momentum (7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)**:
  * Multi-Timeframe Forced Aggregates (5m): Long Liq=`0.00 USD` | Short Liq=`0.00 USD` | Total=`0.00 USD` | Net Delta=`0.00 USD` | Dominant=`BALANCED`

---

## 7. Derivatives Sentiment, Open Interest & Funding Dynamics
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet, 6_Funding_Fee_Settlement.parquet, 13_Hyperliquid.parquet)*
- **Aggregated Open Interest Breakdown (5_OI.parquet)**:
  * Total Open Interest: `98.50M USD` (`144,948,827.9 APT`) | OI / 24h Volume Ratio: `0.6485`
  * OI Expansion Rate: 1h Change=`-0.50%` | 4h Change=`+1.78%` | 24h Change=`-2.59%`
  * Venue Concentration:
    - Binance: `19.33M USD` | Bybit: `20.15M USD` | OKX: `4.77M USD` | CME Institutional: `0.00 USD`
    - Gate: `13.37M USD` | MEXC: `12.85M USD` | Hyperliquid DEX: `3.73M USD` | Bitget: `6.41M USD`
    - KuCoin: `3.78M USD` | BingX: `5.41M USD` | Bitunix: `785.94K USD` | Others: `7.92M USD`
- **Cross-Exchange Perpetual Funding Rates (5_Funding_Rate.parquet)**:
  * Major CEX Rates: Binance=`+0.0094%` | OKX=`+0.0067%` | Bybit=`+0.0016%` | Bitget=`+0.0100%`
  * Mid-Tier CEX Rates: KuCoin=`+0.0100%` | MEXC=`+0.0094%` | Gate=`+0.0038%` | BingX=`+0.0100%` | Bitunix=`+0.0090%`
  * Alternative Venues: WhiteBIT=`+0.0100%` | LBank=`+0.0031%` | tradeXYZ=`-`
  * Inverse Coin-Margined: CoinM Binance=`+0.0000%` | CoinM OKX=`+0.0000%` | CoinM Bybit=`+0.0100%`
- **Exchange Long / Short Ratio Dynamics (3_Exchanges_LS_Ratio*.parquet)**:
  * 15m Tactical: L/S Ratio=`0.68` (Longs: `40.57%`, Shorts: `59.43%`, Total Vol: `3.65M USD`)
  * 1h Primary: L/S Ratio=`1.09` (Longs: `52.22%`, Shorts: `47.78%`, Total Vol: `27.11M USD`)
  * 4h Macro: L/S Ratio=`0.84` (Longs: `45.62%`, Shorts: `54.38%`, Total Vol: `28.01M USD`)
- **Funding Fee Settlement & DEX Arbitrage (6_Funding_Fee_Settlement.parquet, 13_Hyperliquid.parquet)**:
  * Settlement Payouts: Current Expected=`2.51K USD` | Last 24h=`7.04K USD` | Last 3D=`8.52K USD` | Last 7D=`3.71K USD`

---

## 8. Microstructure Footprint, Tape Imbalances & Macro Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 16_Hyperdash_telegram_Intel.parquet, 19_News.parquet, 19_Calendar.parquet)*
- **Bar-by-Bar Microstructure Footprint (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
  * Venue Source: `CoinGlass-AggregatedFutures(Binance)` | Timeframe: `15m` | Last Price: `0.69000`
  * Footprint Auction Profile: Bar VWAP=`0.68115` | Bar POC=`0.68005` | Bar VAH=`0.68315` | Bar VAL=`0.67855`
  * Orderflow Volumes: Total Vol=`464,416.15 USD` | Taker Buy=`219,480.65 USD` | Taker Sell=`244,935.49 USD`
  * Bar Delta Profile: Delta=`-25,454.84 USD` (`-5.48%`) | Max Delta=`+0.00 USD` | Min Delta=`-104,977.92 USD` | Cumulative Bar Delta=`+87,686.41 USD`
  * Order Execution Dynamics: Trades Count=`4,909` | Avg Trade Size=`94.61 USD`
  * Tape Imbalances: Imbalance Ratio=`300.0%` | Buy Imbalances Count=`6` | Sell Imbalances Count=`10`
  * Footprint Open Interest: Bar OI=`0.00 USD` | Bar OI Change=`+0.00 USD`
- **CoinGlass Algorithmic Footprint Signals (25_CoinGlass_Footprint_Signals.parquet)**:
  * Signal Classification: Type=`Divergence` | Bias: **`BEARISH`** | Signal Time=`10-28 05:31` | Timeframe=`Range 0.002`
  * Signal Context: Headline=`Rally without taker buying` | Price Level=`0.69630` | Absorbed Volume=`0.00 USD`
  * Bar Footprint Context: Current Bar Delta=`+0.00 USD` | Current Bar Volume=`0.00 USD` | Delta in View=`+0.00 USD`
  * Historical Detail: `Closed up on negative Delta (−34%), bearish · 0.69630` | KPI=`—` | Bias=`—`
- **Multi-Horizon Macro Capital Netflows (2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet)**:
  * Spot Capital Netflows:
    - Tactical: 5m=`-5.57K` | 15m=`+57.72K` | 30m=`+47.92K` | 1h=`+140.46K`
    - Intermediate: 2h=`+35.43K` | 4h=`+83.80K` | 6h=`+68.19K` | 8h=`-78.45K` | 12h=`-428.01K` | 24h=`-915.21K`
    - Macro Horizons: 1-Week=`-5.47M` | 15-Day=`-9.50M` | 30-Day=`-29.87M` | Market Cap=`601.71M`
  * Futures Capital Netflows:
    - Tactical: 5m=`-46.09K` | 15m=`-77.52K` | 30m=`-20.72K` | 1h=`+58.17K`
    - Intermediate: 2h=`+27.77` | 4h=`-533.33K` | 6h=`-171.50K` | 8h=`-1.10M` | 12h=`-1.65M` | 24h=`-4.25M`
    - Macro Horizons: 1-Week=`-18.32M` | 15-Day=`-45.26M` | 30-Day=`-101.53M` | Market Cap=`601.71M`
- **Telegram Intelligence Alert**: `[MARKET_INTEL] #APT Liquidated Long: 0.38K USD at 0.8176 USD [API] (Impact: NEWS_INTEL)`

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
- **Stand-Aside Reason**: Gate 1 Spread Friction Failure: UNLISTED_ON_MT5_BROKER (Zero broker telemetry stream). Standing aside in 100% cash preserves statutory floor.