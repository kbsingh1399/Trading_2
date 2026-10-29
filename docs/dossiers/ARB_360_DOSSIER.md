# 🔬 MASTER 43-FEED QUANTITATIVE DOSSIER: ARB (Arbitrum)
**MT5 Symbol**: `ARBUSD.p` | **Category**: `Crypto Alt L2` | **Tier**: `Tier 1`
**Execution Posture**: `PASSIVE_MAKER_LIMIT_ONLY` | **Timestamp**: 2026-10-29 14:43:14 UTC
**Pipeline Clearance**: `DISQUALIFIED` | **Data Freshness**: `1.2m`

---

## 1. MT5 Live Broker Telemetry & Spread Friction Gate
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet)*
- **Live Bid Quote**: `0.17000` | **Live Ask Quote**: `0.17000` | **Mid Price**: `0.17000`
- **Spread Points**: `0.0 pts` | **Spread BPS**: `999.00 bps` (Mandatory Cap: `25.0 bps`)
- **Gate Status**: **`FAIL`** (UNLISTED_ON_MT5_BROKER (Zero broker telemetry stream))
- **Order Allowed**: `BUY_LIMIT / SELL_LIMIT` | **Pillar 1 Clearance**: `DISQUALIFIED`
- **Broker Specifications**: Contract Size=`1.00` | Tick Value=`1.00 USD` | Min Lot=`0.01` | Digits=`5`
- **Account Capital Context**: Balance=`4,744.55 USD` | Equity=`4,744.32 USD` | Free Margin=`4,342.62 USD` | Inviolate Hard Floor=`4,775.00 USD` (Cushion: `-30.68 USD`)
- **Pipeline Health**: Feed #00 Status=`PASS` | Overall Pipeline Telemetry=`33/33 FEEDS PASS (SYNCHRONIZED)`

---

## 2. Technical Profile, Multi-Sigma VWAP Dispersion & Volatility
*(Sources: 11_Technical.parquet, 11_Technical_BTC_Ribbon.parquet)*
- **Live Quote Baseline**: Last Mid Price=`0.17000` | Spread=`999.00 bps` (0.0 pts)
- **Empirical Status**: Asset indicator stream unindexed in 11_Technical collector snapshot. Mathematical indicators reference live MT5 Bid/Ask quotes and session auction structures.

---

## 3. Auction Market Structure & Value Profile
*(Sources: 20_Auction_Market_Structure.parquet)*
- **Daily Auction Value Area**:
  * High (VAH): `0.17051` | Point of Control (POC): `0.17000` | Low (VAL): `0.16949`
  * Distance to POC: `+0.00%` | Distance to VAH: `+0.00%` | Distance to VAL: `+0.00%`
  * **Value Area Position**: **`INSIDE_VALUE (Balance)`** | **Auction Regime**: **`BALANCED_AUCTION`** | **Session Bias**: **`NEUTRAL`**
- **Prior Day & Weekly Auction Profile**:
  * Prior Day: PD VAH=`0.17068` | PD POC=`0.17000` | PD VAL=`0.16932` | PDH=`0.17102` | PDL=`0.16898` | PDC=`0.17000`
  * Monday Reference: Monday High=`0.17085` | Monday Low=`0.16915` | Monday Mid=`0.17000`
  * Weekly Value Area: Weekly VAH=`0.17136` | Weekly POC=`0.17000` | Weekly VAL=`0.16864`
  * Multi-Week Extremes: Current Week High (CWH)=`0.17170` | CWL=`0.16830` | Prior Week High (PWH)=`0.17255` | PWL=`0.16745`
  * Multi-Month Extremes: Current Month High (CMH)=`0.17340` | CML=`0.16660` | Prior Month High (PMH)=`0.17425` | PML=`0.16575`
- **Session Liquidity Extremes & Initial Balance**:
  * Asian Session: Range `[0.16966 - 0.17034]`
  * London Session: Range `[0.16932 - 0.17068]`
  * New York Session: Range `[0.16915 - 0.17085]`
  * Initial Balance (IB): IB High=`0.17051` | IB Low=`0.16949`
- **Fibonacci Golden Pocket & Optimal Trade Entry (OTE)**:
  * Swing Range: High=`0.17170` | Low=`0.16830` | Direction=`NONE`
  * Golden Pocket [0.618 - 0.65]: `[0.16966 - 0.17034]`
  * Optimal Trade Entry (0.702): `0.17000` | Invalidation Level: `0.00000` | Status: **`NONE`**
- **Classical & Weekly Pivots**:
  * Daily Classical: Pivot=`0.17000` | R1=`0.17051` | S1=`0.16949` | R2=`0.17102` | S2=`0.16898`
  * Weekly Classical: Weekly Pivot=`0.17000` | Weekly R1=`0.17170` | Weekly S1=`0.16830`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Orderflow
*(Sources: 18_CVD.parquet, 18_CVD_30D_5m.parquet, 18_CVD_30D_15m.parquet, 18_CVD_30D_1h.parquet, 18_CVD_30D_4h.parquet, 18_CVD_30D_ALL.parquet, 21_Tradfye_Orderflow.parquet)*
- **Primary 15m CVD Microstructure (18_CVD_30D_15m.parquet)**:
  * Candle Delta: `-54,420.04 USD` (Base: `-320,551.2000 coins`) | Delta %: `-7.82%`
  * Taker Volumes: Taker Buy=`320,649.51 USD` | Taker Sell=`375,069.55 USD` | Total Vol=`4,088,604.80 USD`
  * Cumulative CVD: `-3,419,417.80 USD` (Base: `-20,125,274.9000`)
  * Rolling CVD Z-Score: `+0.01 sigma` | Price Return: `+0.32%`
  * **Delta Regime**: **`BEARISH ABSORPTION`** | Trades Count: `11,066`
- **Multi-Timeframe Delta Comparison**:
  * 5m Bar: Delta=`-8,695.54 USD` | Delta %=`-7.97%` | Z-Score=`+0.31` | Regime=`BEARISH ABSORPTION`
  * 1h Bar: Delta=`-54,420.04 USD` | Delta %=`-7.82%` | Z-Score=`+0.20` | Regime=`BEARISH ABSORPTION`
  * 4h Bar: Delta=`-637,911.18 USD` | Delta %=`-6.77%` | Z-Score=`-0.47` | Regime=`BEARISH ABSORPTION`
  * 30D Consolidated (ALL): Cumulative Trend=`-2,877,494.82 USD` | Long-Term Regime=`BEARISH ABSORPTION`
- **Institutional Footprint & Deribit Options Armor (21_Tradfye_Orderflow.parquet)**:
  * Candle VWAP: `0.16486` | Estimated POC: `0.16503` | Avg Trade Size: `103.29 USD`
  * Net Delta USD: `+69,690.68 USD` | Net Delta %: `+14.19%` | Orderflow CVD: `+69,690.68 USD`
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
  * 24H Horizon: Short MP=`0.17841` (Vol: `147,300 USD`, Dist: `+4.64%`) | Long MP=`0.15979` (Vol: `147,500 USD`, Dist: `-6.28%`)
  * 48H Horizon: Short MP=`0.17841` (Vol: `147,300 USD`, Dist: `+4.64%`) | Long MP=`0.15979` (Vol: `154,300 USD`, Dist: `-6.28%`)
  * 3D Horizon: Short MP=`0.17841` (Vol: `147,300 USD`, Dist: `+4.64%`) | Long MP=`0.15979` (Vol: `205,900 USD`, Dist: `-6.28%`)
  * 7D Horizon: Short MP=`0.18752` (Vol: `158,800 USD`, Dist: `+9.98%`) | Long MP=`0.16132` (Vol: `344,500 USD`, Dist: `-5.38%`)
- **Exchange Cumulative Liquidation Cascades (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
  * 1D Cascade: Total=`3.16M USD` | Short Liq Pool=`3.16M USD` | Long Liq Pool=`0 USD` | Venues: Binance=`2.53K USD`, OKX=`3.64K USD`, Bybit=`0 USD`
  * 7D Cascade: Total=`11.46M USD` | Short Liq Pool=`11.46M USD` | Long Liq Pool=`0 USD` | Venues: Binance=`14.33K USD`, OKX=`11.22K USD`, Bybit=`5.20K USD`
- **Cross-Venue Liquidation Matrix & Heatmaps (14_Liquidation_Matrix.parquet, 7_Liq_Heapmap.parquet)**:
  * Liquidation Matrix Strike: Price=`0.33950` | Vol=`63,790 USD` | Cumulative=`636,600 USD` | Venue=`Hyperliquid L1` | Side=`Short Liquidation`
  * Multi-Timeframe Heatmap Density: 1h=`0.00 USD` | 4h=`355.77K USD` | 12h=`465.64K USD` | 24h=`1.06M USD`
- **Hyperdash Real-Time Liquidation & Retail Stop Protection (14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet)**:
  * Hyperdash Liq Cluster: Mark=`0.170110 USD` | Cluster Price=`0.339500 USD` | Dist=`+99.58%` | Cumulative=`636.60K USD` | Short=`63.79K USD` | Long=`0 USD` | Size=`187,887.7000 ARB`
  * **Retail Stops Map (Pitfall 2 & 4 Defense)**:
    - `Sell Stop`: `0.016500 USD` (Dist: `-90.30%`, Cumulative Stops: `748.07K USD`, Buy: `0 USD`, Sell: `3.09K USD`, Coins: `187,462.9000 ARB`)
    - `Sell Stop`: `0.035500 USD` (Dist: `-79.13%`, Cumulative Stops: `744.98K USD`, Buy: `0 USD`, Sell: `355.00 USD`, Coins: `10,000.0000 ARB`)
    - `Sell Stop`: `0.042500 USD` (Dist: `-75.02%`, Cumulative Stops: `744.62K USD`, Buy: `0 USD`, Sell: `453.00 USD`, Coins: `10,658.9000 ARB`)
- **Live Forced Liquidation Momentum (7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)**:
  * Multi-Timeframe Forced Aggregates (5m): Long Liq=`0.00 USD` | Short Liq=`0.00 USD` | Total=`0.00 USD` | Net Delta=`0.00 USD` | Dominant=`BALANCED`

---

## 7. Derivatives Sentiment, Open Interest & Funding Dynamics
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet, 6_Funding_Fee_Settlement.parquet, 13_Hyperliquid.parquet)*
- **Aggregated Open Interest Breakdown (5_OI.parquet)**:
  * Total Open Interest: `213.35M USD` (`1,255,126,388.4 ARB`) | OI / 24h Volume Ratio: `0.7773`
  * OI Expansion Rate: 1h Change=`-1.37%` | 4h Change=`-0.01%` | 24h Change=`-8.65%`
  * Venue Concentration:
    - Binance: `49.45M USD` | Bybit: `29.77M USD` | OKX: `16.95M USD` | CME Institutional: `0.00 USD`
    - Gate: `22.19M USD` | MEXC: `27.64M USD` | Hyperliquid DEX: `14.72M USD` | Bitget: `16.45M USD`
    - KuCoin: `13.75M USD` | BingX: `5.24M USD` | Bitunix: `1.61M USD` | Others: `15.58M USD`
- **Cross-Exchange Perpetual Funding Rates (5_Funding_Rate.parquet)**:
  * Major CEX Rates: Binance=`+0.0100%` | OKX=`+0.0099%` | Bybit=`+0.0100%` | Bitget=`+0.0072%`
  * Mid-Tier CEX Rates: KuCoin=`+0.0100%` | MEXC=`+0.0099%` | Gate=`+0.0027%` | BingX=`+0.0100%` | Bitunix=`+0.0100%`
  * Alternative Venues: WhiteBIT=`+0.0100%` | LBank=`+0.0100%` | tradeXYZ=`-`
  * Inverse Coin-Margined: CoinM Binance=`+0.0000%` | CoinM OKX=`+0.0000%` | CoinM Bybit=`+0.0000%`
- **Exchange Long / Short Ratio Dynamics (3_Exchanges_LS_Ratio*.parquet)**:
  * 15m Tactical: L/S Ratio=`0.82` (Longs: `44.96%`, Shorts: `55.04%`, Total Vol: `3.65M USD`)
  * 1h Primary: L/S Ratio=`0.95` (Longs: `48.74%`, Shorts: `51.26%`, Total Vol: `105.40M USD`)
  * 4h Macro: L/S Ratio=`1.24` (Longs: `55.33%`, Shorts: `44.67%`, Total Vol: `48.58M USD`)
- **Funding Fee Settlement & DEX Arbitrage (6_Funding_Fee_Settlement.parquet, 13_Hyperliquid.parquet)**:
  * Settlement Payouts: Current Expected=`9.57K USD` | Last 24h=`645.76 USD` | Last 3D=`18.56K USD` | Last 7D=`31.80K USD`

---

## 8. Microstructure Footprint, Tape Imbalances & Macro Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 16_Hyperdash_telegram_Intel.parquet, 19_News.parquet, 19_Calendar.parquet)*
- **Bar-by-Bar Microstructure Footprint (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
  * Venue Source: `CoinGlass-AggregatedFutures(Binance)` | Timeframe: `15m` | Last Price: `0.17000`
  * Footprint Auction Profile: Bar VWAP=`0.17015` | Bar POC=`0.17041` | Bar VAH=`0.17067` | Bar VAL=`0.16951`
  * Orderflow Volumes: Total Vol=`611,622.67 USD` | Taker Buy=`277,546.25 USD` | Taker Sell=`334,076.43 USD`
  * Bar Delta Profile: Delta=`-56,530.18 USD` (`-9.24%`) | Max Delta=`+5,535.89 USD` | Min Delta=`-76,724.83 USD` | Cumulative Bar Delta=`-624,797.84 USD`
  * Order Execution Dynamics: Trades Count=`9,296` | Avg Trade Size=`65.79 USD`
  * Tape Imbalances: Imbalance Ratio=`300.0%` | Buy Imbalances Count=`12` | Sell Imbalances Count=`31`
  * Footprint Open Interest: Bar OI=`0.00 USD` | Bar OI Change=`+0.00 USD`
- **CoinGlass Algorithmic Footprint Signals (25_CoinGlass_Footprint_Signals.parquet)**:
  * Signal Classification: Type=`Bear div` | Bias: **`BEARISH`** | Signal Time=`10-28 06:51` | Timeframe=`Range 0.0005`
  * Signal Context: Headline=`Higher high, lower Cumulative Delta` | Price Level=`0.16912` | Absorbed Volume=`1,600,000.00 USD`
  * Bar Footprint Context: Current Bar Delta=`+0.00 USD` | Current Bar Volume=`0.00 USD` | Delta in View=`+0.00 USD`
  * Historical Detail: `Higher high than 10-28 06:27, yet Cumulative Delta fell 1.6M over the swing. Buyers aren't following through, bearish · 0.16912` | KPI=`—` | Bias=`—`
- **Multi-Horizon Macro Capital Netflows (2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet)**:
  * Spot Capital Netflows:
    - Tactical: 5m=`+1.97K` | 15m=`+17.65K` | 30m=`-9.28K` | 1h=`-87.47K`
    - Intermediate: 2h=`+25.38K` | 4h=`+370.81K` | 6h=`+479.27K` | 8h=`+80.99K` | 12h=`-210.56K` | 24h=`-552.75K`
    - Macro Horizons: 1-Week=`-5.03M` | 15-Day=`-11.44M` | 30-Day=`-32.88M` | Market Cap=`1.17B`
  * Futures Capital Netflows:
    - Tactical: 5m=`+38.18K` | 15m=`+95.98K` | 30m=`+140.80K` | 1h=`-438.74K`
    - Intermediate: 2h=`-963.15K` | 4h=`-1.65M` | 6h=`-1.34M` | 8h=`-2.36M` | 12h=`-610.47K` | 24h=`-4.91M`
    - Macro Horizons: 1-Week=`-29.21M` | 15-Day=`-41.55M` | 30-Day=`-163.77M` | Market Cap=`1.17B`

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