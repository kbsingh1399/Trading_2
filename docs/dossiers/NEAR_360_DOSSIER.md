# 🔬 MASTER 43-FEED QUANTITATIVE DOSSIER: NEAR (Near Protocol)
**MT5 Symbol**: `NERUSD.p` | **Category**: `Crypto Alt L1` | **Tier**: `Tier 1`
**Execution Posture**: `DISQUALIFIED` | **Timestamp**: 2026-10-29 14:43:14 UTC
**Pipeline Clearance**: `BLOCKED` | **Data Freshness**: `1.2m`

---

## 1. MT5 Live Broker Telemetry & Spread Friction Gate
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet)*
- **Live Bid Quote**: `4.43300` | **Live Ask Quote**: `4.46300` | **Mid Price**: `4.44800`
- **Spread Points**: `30.0 pts` | **Spread BPS**: `67.45 bps` (Mandatory Cap: `25.0 bps`)
- **Gate Status**: **`FAIL`** (Spread friction 67.45 bps exceeds cap 25.0 bps)
- **Order Allowed**: `NONE` | **Pillar 1 Clearance**: `BLOCKED`
- **Broker Specifications**: Contract Size=`1.00` | Tick Value=`1.00 USD` | Min Lot=`0.01` | Digits=`5`
- **Account Capital Context**: Balance=`4,744.55 USD` | Equity=`4,744.32 USD` | Free Margin=`4,342.62 USD` | Inviolate Hard Floor=`4,775.00 USD` (Cushion: `-30.68 USD`)
- **Pipeline Health**: Feed #00 Status=`PASS` | Overall Pipeline Telemetry=`33/33 FEEDS PASS (SYNCHRONIZED)`

---

## 2. Technical Profile, Multi-Sigma VWAP Dispersion & Volatility
*(Sources: 11_Technical.parquet, 11_Technical_BTC_Ribbon.parquet)*
- **Last Verified Price**: `4.43300` | **24h Change**: `-2.46%` (24h High: `4.79800`, 24h Low: `4.26900`)
- **Weekly Range**: Week High=`4.79800` | Week Low=`4.26900` | Daily POC=`4.40900` | Daily VAH=`4.50000` | Daily VAL=`4.31300`
- **Session VWAP**: `4.43229` | **Rolling 24h VWAP**: `4.53963` | **Distance to VWAP**: `+0.02%`
- **VWAP Z-Score**: `+0.01 sigma` | **Mean Reversion Bias**: **`FAIR VALUE`**
- **VWAP Dispersion Bands**:
  * +1.00 sigma: `4.52476` | -1.00 sigma: `4.33982`
  * +1.28 sigma (80% CI): `4.55066` | -1.28 sigma: `4.31392`
  * +2.00 sigma (95% CI): `4.61724` | -2.00 sigma: `4.24734`
  * +2.01 sigma: `4.61816` | -2.01 sigma: `4.24642`
  * +2.51 sigma (98.8% CI): `4.66440` | -2.51 sigma: `4.20018`
  * +3.00 sigma (99.7% CI Extreme): `4.70971` | -3.00 sigma: `4.15487`
- **Oscillators & Volatility**:
  * **RSI (14)**: `55.26` | **RSI State**: **`BULLISH`**
  * **ATR (14)**: `0.03863` | **ATR %**: `0.87%`
  * **Bollinger Bands**: Upper=`4.47435` | Mid=`4.39455` | Lower=`4.31475` | Bandwidth=`3.63%`
  * **MACD**: Line=`+0.0123` | Signal=`+0.0025` | Hist=`+0.0098`
- **Exponential Moving Average Ribbon (EMA)**:
  * Short Horizon: EMA-5=`4.43536` | EMA-9=`4.42661` | EMA-13=`4.41743` | EMA-20=`4.40813`
  * Intermediate: EMA-34=`4.41275` | EMA-50=`4.43314` | EMA-89=`4.48046` | EMA-100=`4.49008`
  * Institutional: EMA-144=`4.51239` | EMA-200=`4.51668` (Slope: `-0.274%`) | EMA-233=`4.51773` (Slope: `-0.236%`)
  * **Trend Bias**: **`NEUTRAL / CHOP`**

---

## 3. Auction Market Structure & Value Profile
*(Sources: 20_Auction_Market_Structure.parquet)*
- **Daily Auction Value Area**:
  * High (VAH): `4.50000` | Point of Control (POC): `4.40900` | Low (VAL): `4.31300`
  * Distance to POC: `+0.89%` | Distance to VAH: `-1.14%` | Distance to VAL: `+3.15%`
  * **Value Area Position**: **`INSIDE_VALUE (Balance)`** | **Auction Regime**: **`ROTATIONAL_BALANCE`** | **Session Bias**: **`BEARISH (Below Pivot)`**
- **Prior Day & Weekly Auction Profile**:
  * Prior Day: PD VAH=`4.73400` | PD POC=`4.68100` | PD VAL=`4.60700` | PDH=`4.79800` | PDL=`4.52700` | PDC=`4.71500`
  * Monday Reference: Monday High=`4.64900` | Monday Low=`4.41300` | Monday Mid=`4.53100`
  * Weekly Value Area: Weekly VAH=`4.62000` | Weekly POC=`4.44400` | Weekly VAL=`4.39800`
  * Multi-Week Extremes: Current Week High (CWH)=`4.79800` | CWL=`4.26900` | Prior Week High (PWH)=`5.43500` | PWL=`4.22700`
  * Multi-Month Extremes: Current Month High (CMH)=`5.98800` | CML=`4.22700` | Prior Month High (PMH)=`5.56000` | PML=`1.81300`
- **Session Liquidity Extremes & Initial Balance**:
  * Asian Session: Range `[4.38800 - 4.75300]`
  * London Session: Range `[4.26900 - 4.49700]`
  * New York Session: Range `[4.33600 - 4.50100]`
  * Initial Balance (IB): IB High=`4.49700` | IB Low=`4.42600`
- **Fibonacci Golden Pocket & Optimal Trade Entry (OTE)**:
  * Swing Range: High=`4.79800` | Low=`4.26900` | Direction=`BEARISH_IMPULSE`
  * Golden Pocket [0.618 - 0.65]: `[4.59600 - 4.61300]`
  * Optimal Trade Entry (0.702): `4.64000` | Invalidation Level: `4.68500` | Status: **`SHALLOW_RETRACE`**
- **Classical & Weekly Pivots**:
  * Daily Classical: Pivot=`4.68000` | R1=`4.83300` | S1=`4.56200` | R2=`4.95100` | S2=`4.40900`
  * Weekly Classical: Weekly Pivot=`4.73800` | Weekly R1=`5.24900` | Weekly S1=`4.04100`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Orderflow
*(Sources: 18_CVD.parquet, 18_CVD_30D_5m.parquet, 18_CVD_30D_15m.parquet, 18_CVD_30D_1h.parquet, 18_CVD_30D_4h.parquet, 18_CVD_30D_ALL.parquet, 21_Tradfye_Orderflow.parquet)*
- **Primary 15m CVD Microstructure (18_CVD_30D_15m.parquet)**:
  * Candle Delta: `+21,684.49 USD` (Base: `+4,751.0000 coins`) | Delta %: `+0.62%`
  * Taker Volumes: Taker Buy=`1,765,291.79 USD` | Taker Sell=`1,743,607.30 USD` | Total Vol=`790,141.00 USD`
  * Cumulative CVD: `-27,753,246.59 USD` (Base: `-6,227,274.0000`)
  * Rolling CVD Z-Score: `+0.25 sigma` | Price Return: `+0.00%`
  * **Delta Regime**: **`NEUTRAL CHOP`** | Trades Count: `12,136`
- **Multi-Timeframe Delta Comparison**:
  * 5m Bar: Delta=`-87,113.07 USD` | Delta %=`-8.18%` | Z-Score=`-0.08` | Regime=`BEARISH ABSORPTION`
  * 1h Bar: Delta=`+21,684.49 USD` | Delta %=`+0.62%` | Z-Score=`+0.43` | Regime=`NEUTRAL CHOP`
  * 4h Bar: Delta=`-1,774,845.48 USD` | Delta %=`-2.35%` | Z-Score=`+0.37` | Regime=`BEARISH ABSORPTION`
  * 30D Consolidated (ALL): Cumulative Trend=`-27,159,114.66 USD` | Long-Term Regime=`BEARISH ABSORPTION`
- **Institutional Footprint & Deribit Options Armor (21_Tradfye_Orderflow.parquet)**:
  * Candle VWAP: `4.46109` | Estimated POC: `4.46025` | Avg Trade Size: `459.23 USD`
  * Net Delta USD: `+363,163.53 USD` | Net Delta %: `+11.28%` | Orderflow CVD: `+363,163.53 USD`
  * Orderflow Regime: **`TWO_SIDED_ABSORPTION`** | Orderflow Divergence: **`BULLISH_EXPANSION`**
  * Deribit Options Walls: Max Pain=`0.00` | Call Wall=`0.00` | Put Wall=`0.00`

---

## 5. Institutional Whale Armor & Resting Orderbook Depth
*(Sources: 10_Whale_Orders.parquet, 12_Hyperdash.parquet, 17_Orderbook.parquet, 4_Hyperliquid_Analysis.parquet)*
- **Defending Resting Whale Walls (10_Whale_Orders.parquet)**:
  * Defending Bid Wall: `4.41400` (`151336.6561` coins / `669,000.00 USD` on `Binance`, persistent for `2m 01s`, Traded: `0.0%`, Order ID: `CG_WHALE_NEAR_T_79`)
  * Defending Ask Wall: `4.47000` (`152348.9933` coins / `681,000.00 USD` on `Binance`, persistent for `24s`, Traded: `0.0%`, Order ID: `CG_LADDER_NEAR_15`)
  * Total Whale Armor Pool: Bids Pool=`15,859,300.00 USD` | Asks Pool=`10,517,400.00 USD` (Tracked Orders: `182`)
- **Hyperdash Resting Depth & L3 Telemetry (12_Hyperdash.parquet)**:
  * `NEUTRAL`: `0.00 USD` @ `0.00000` (Size: `0.0`, Detail: Delta: +0, Wallet: None, Timestamp: 2026-10-29 19:44:05 IST)
- **Hyperliquid Elite Trader Positioning (4_Hyperliquid_Analysis.parquet)**:
  * Wallet `0x77375a8c9d...` (0x7737...bf66): `Long` `25,043,383.58 USD` (5,640,376.3000 NEAR, Margin: 2,504,338.36 USD, Leverage: 10X Cross, Entry: 2.3530 USD, Current: 4.4390 USD, Est Liq: 0.934400 USD, PnL: +11,771,480.75 USD [+47.00%], Fees: +509,899.90 USD)
  * Wallet `0xb581d667c5...` (0xb581...6f4f): `Long` `15,980,400.00 USD` (3,600,000.0000 NEAR, Margin: 3,995,100.00 USD, Leverage: 4X Cross, Entry: 5.1925 USD, Current: 4.4390 USD, Est Liq: 0.00 USD, PnL: -2,712,635.22 USD [-16.97%], Fees: +71,400.88 USD)
  * Wallet `0xdd53c52973...` (0xdd53...2b13): `Short` `10,675,258.87 USD` (2,400,202.1000 NEAR, Margin: 3,558,419.62 USD, Leverage: 3X Cross, Entry: 2.3104 USD, Current: 4.4390 USD, Est Liq: 27.1609 USD, PnL: -5,129,854.99 USD [-48.05%], Fees: -351,882.28 USD)

---

## 6. Liquidation Max Pain, Heatmaps & Cascade Boundaries
*(Sources: 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 14_Hyperdash_Liq_Map.parquet, 14_Liquidation_Matrix.parquet, 15_Hyperdash_Stops_Map.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`4.55500` (Vol: `717,200 USD`, Dist: `+2.36%`) | Long MP=`4.26380` (Vol: `591,700 USD`, Dist: `-4.18%`)
  * 48H Horizon: Short MP=`4.55500` (Vol: `717,200 USD`, Dist: `+2.36%`) | Long MP=`4.26380` (Vol: `591,700 USD`, Dist: `-4.18%`)
  * 3D Horizon: Short MP=`4.55500` (Vol: `717,200 USD`, Dist: `+2.36%`) | Long MP=`4.26380` (Vol: `618,400 USD`, Dist: `-4.18%`)
  * 7D Horizon: Short MP=`5.02750` (Vol: `914,000 USD`, Dist: `+12.98%`) | Long MP=`4.22800` (Vol: `1,200,000 USD`, Dist: `-4.99%`)
- **Exchange Cumulative Liquidation Cascades (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
  * 1D Cascade: Total=`27.28M USD` | Short Liq Pool=`27.28M USD` | Long Liq Pool=`0 USD` | Venues: Binance=`5.05K USD`, OKX=`7.52K USD`, Bybit=`77.90K USD`
  * 7D Cascade: Total=`44.64M USD` | Short Liq Pool=`44.64M USD` | Long Liq Pool=`0 USD` | Venues: Binance=`127.17K USD`, OKX=`103.06K USD`, Bybit=`116.44K USD`
- **Cross-Venue Liquidation Matrix & Heatmaps (14_Liquidation_Matrix.parquet, 7_Liq_Heapmap.parquet)**:
  * Liquidation Matrix Strike: Price=`8.88500` | Vol=`1,490,000 USD` | Cumulative=`37,200,000 USD` | Venue=`Hyperliquid L1` | Side=`Short Liquidation`
  * Multi-Timeframe Heatmap Density: 1h=`126.43K USD` | 4h=`261.77K USD` | 12h=`3.11M USD` | 24h=`5.13M USD`
- **Hyperdash Real-Time Liquidation & Retail Stop Protection (14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet)**:
  * Hyperdash Liq Cluster: Mark=`4.4548 USD` | Cluster Price=`8.8850 USD` | Dist=`+99.45%` | Cumulative=`37.20M USD` | Short=`1.49M USD` | Long=`0 USD` | Size=`168,122.0000 NEAR`
  * **Retail Stops Map (Pitfall 2 & 4 Defense)**:
    - `Sell Stop`: `0.805000 USD` (Dist: `-81.93%`, Cumulative Stops: `4.67M USD`, Buy: `0 USD`, Sell: `107.71 USD`, Coins: `133.8000 NEAR`)
    - `Sell Stop`: `0.825000 USD` (Dist: `-81.48%`, Cumulative Stops: `4.67M USD`, Buy: `0 USD`, Sell: `209.80 USD`, Coins: `254.3000 NEAR`)
    - `Sell Stop`: `1.0050 USD` (Dist: `-77.44%`, Cumulative Stops: `4.67M USD`, Buy: `0 USD`, Sell: `717.17 USD`, Coins: `713.6000 NEAR`)
- **Live Forced Liquidation Momentum (7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)**:
  * Multi-Timeframe Forced Aggregates (5m): Long Liq=`0.00 USD` | Short Liq=`0.00 USD` | Total=`0.00 USD` | Net Delta=`0.00 USD` | Dominant=`BALANCED`

---

## 7. Derivatives Sentiment, Open Interest & Funding Dynamics
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet, 6_Funding_Fee_Settlement.parquet, 13_Hyperliquid.parquet)*
- **Aggregated Open Interest Breakdown (5_OI.parquet)**:
  * Total Open Interest: `1.28B USD` (`289,882,977.4 NEAR`) | OI / 24h Volume Ratio: `0.7508`
  * OI Expansion Rate: 1h Change=`-1.50%` | 4h Change=`+1.16%` | 24h Change=`-1.78%`
  * Venue Concentration:
    - Binance: `249.32M USD` | Bybit: `172.78M USD` | OKX: `54.38M USD` | CME Institutional: `0.00 USD`
    - Gate: `173.20M USD` | MEXC: `70.17M USD` | Hyperliquid DEX: `258.57M USD` | Bitget: `79.76M USD`
    - KuCoin: `64.96M USD` | BingX: `51.56M USD` | Bitunix: `6.99M USD` | Others: `103.08M USD`
- **Cross-Exchange Perpetual Funding Rates (5_Funding_Rate.parquet)**:
  * Major CEX Rates: Binance=`+0.0079%` | OKX=`+0.0078%` | Bybit=`+0.0100%` | Bitget=`+0.0081%`
  * Mid-Tier CEX Rates: KuCoin=`+0.0100%` | MEXC=`+0.0079%` | Gate=`+0.0100%` | BingX=`+0.0100%` | Bitunix=`+0.0081%`
  * Alternative Venues: WhiteBIT=`+0.0100%` | LBank=`+0.0100%` | tradeXYZ=`-`
  * Inverse Coin-Margined: CoinM Binance=`+0.0100%` | CoinM OKX=`+0.0000%` | CoinM Bybit=`+0.0100%`
- **Exchange Long / Short Ratio Dynamics (3_Exchanges_LS_Ratio*.parquet)**:
  * 15m Tactical: L/S Ratio=`0.83` (Longs: `45.41%`, Shorts: `54.59%`, Total Vol: `5.59M USD`)
  * 1h Primary: L/S Ratio=`1.23` (Longs: `55.12%`, Shorts: `44.88%`, Total Vol: `55.28M USD`)
  * 4h Macro: L/S Ratio=`0.88` (Longs: `46.68%`, Shorts: `53.32%`, Total Vol: `82.36M USD`)
- **Funding Fee Settlement & DEX Arbitrage (6_Funding_Fee_Settlement.parquet, 13_Hyperliquid.parquet)**:
  * Settlement Payouts: Current Expected=`41.23K USD` | Last 24h=`106.01K USD` | Last 3D=`314.39K USD` | Last 7D=`172.37K USD`

---

## 8. Microstructure Footprint, Tape Imbalances & Macro Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 16_Hyperdash_telegram_Intel.parquet, 19_News.parquet, 19_Calendar.parquet)*
- **Bar-by-Bar Microstructure Footprint (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
  * Venue Source: `CoinGlass-AggregatedFutures(Binance)` | Timeframe: `15m` | Last Price: `4.44800`
  * Footprint Auction Profile: Bar VWAP=`4.44330` | Bar POC=`4.44250` | Bar VAH=`4.45850` | Bar VAL=`4.42150`
  * Orderflow Volumes: Total Vol=`2,728,868.42 USD` | Taker Buy=`1,311,393.58 USD` | Taker Sell=`1,417,474.85 USD`
  * Bar Delta Profile: Delta=`-106,081.27 USD` (`-3.89%`) | Max Delta=`+0.00 USD` | Min Delta=`-311,503.36 USD` | Cumulative Bar Delta=`-1,651,829.30 USD`
  * Order Execution Dynamics: Trades Count=`9,783` | Avg Trade Size=`278.94 USD`
  * Tape Imbalances: Imbalance Ratio=`300.0%` | Buy Imbalances Count=`6` | Sell Imbalances Count=`10`
  * Footprint Open Interest: Bar OI=`0.00 USD` | Bar OI Change=`+0.00 USD`
- **CoinGlass Algorithmic Footprint Signals (25_CoinGlass_Footprint_Signals.parquet)**:
  * Signal Classification: Type=`Exhaustion` | Bias: **`BULLISH`** | Signal Time=`10-28 05:31` | Timeframe=`Range 0.02`
  * Signal Context: Headline=`Seller exhaustion` | Price Level=`4.65300` | Absorbed Volume=`0.00 USD`
  * Bar Footprint Context: Current Bar Delta=`+0.00 USD` | Current Bar Volume=`0.00 USD` | Delta in View=`+0.00 USD`
  * Historical Detail: `New 10-bar low with almost no volume in the bottom 10% of the bar, closed in the upper half, bullish · 4.6530` | KPI=`—` | Bias=`—`
- **Multi-Horizon Macro Capital Netflows (2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet)**:
  * Spot Capital Netflows:
    - Tactical: 5m=`+4.12K` | 15m=`+115.25K` | 30m=`+211.08K` | 1h=`-411.46K`
    - Intermediate: 2h=`-408.52K` | 4h=`-2.83M` | 6h=`-2.47M` | 8h=`-1.01M` | 12h=`-4.33M` | 24h=`-7.94M`
    - Macro Horizons: 1-Week=`-70.13M` | 15-Day=`-119.74M` | 30-Day=`-234.99M` | Market Cap=`5.82B`
  * Futures Capital Netflows:
    - Tactical: 5m=`-293.94K` | 15m=`+491.34K` | 30m=`+1.51M` | 1h=`-2.76M`
    - Intermediate: 2h=`+223.30K` | 4h=`-1.37M` | 6h=`+1.59M` | 8h=`-27.42M` | 12h=`-26.34M` | 24h=`-52.17M`
    - Macro Horizons: 1-Week=`-100.74M` | 15-Day=`-230.51M` | 30-Day=`-689.41M` | Market Cap=`5.82B`
- **Telegram Intelligence Alert**: `[MARKET_INTEL] #NEAR Liquidated Long: 0.02K USD at 4.7899 USD [API] (Impact: NEWS_INTEL)`

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
- **Stand-Aside Reason**: Gate 1 Spread Friction Failure: Spread friction 67.45 bps exceeds cap 25.0 bps. Standing aside in 100% cash preserves statutory floor.