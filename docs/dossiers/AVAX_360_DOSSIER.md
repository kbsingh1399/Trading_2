# 🔬 MASTER 43-FEED QUANTITATIVE DOSSIER: AVAX (Avalanche)
**MT5 Symbol**: `AVXUSD.p` | **Category**: `Crypto Alt L1` | **Tier**: `Tier 1`
**Execution Posture**: `DISQUALIFIED` | **Timestamp**: 2026-10-29 14:43:14 UTC
**Pipeline Clearance**: `BLOCKED` | **Data Freshness**: `1.2m`

---

## 1. MT5 Live Broker Telemetry & Spread Friction Gate
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet)*
- **Live Bid Quote**: `8.81000` | **Live Ask Quote**: `8.85000` | **Mid Price**: `8.83000`
- **Spread Points**: `4.0 pts` | **Spread BPS**: `45.30 bps` (Mandatory Cap: `25.0 bps`)
- **Gate Status**: **`FAIL`** (Spread friction 45.30 bps exceeds cap 25.0 bps)
- **Order Allowed**: `NONE` | **Pillar 1 Clearance**: `BLOCKED`
- **Broker Specifications**: Contract Size=`1.00` | Tick Value=`1.00 USD` | Min Lot=`0.01` | Digits=`5`
- **Account Capital Context**: Balance=`4,744.55 USD` | Equity=`4,744.32 USD` | Free Margin=`4,342.62 USD` | Inviolate Hard Floor=`4,775.00 USD` (Cushion: `-30.68 USD`)
- **Pipeline Health**: Feed #00 Status=`PASS` | Overall Pipeline Telemetry=`33/33 FEEDS PASS (SYNCHRONIZED)`

---

## 2. Technical Profile, Multi-Sigma VWAP Dispersion & Volatility
*(Sources: 11_Technical.parquet, 11_Technical_BTC_Ribbon.parquet)*
- **Last Verified Price**: `8.80000` | **24h Change**: `+0.11%` (24h High: `9.14000`, 24h Low: `8.53000`)
- **Weekly Range**: Week High=`9.14000` | Week Low=`8.53000` | Daily POC=`8.74000` | Daily VAH=`8.81000` | Daily VAL=`8.59000`
- **Session VWAP**: `8.70251` | **Rolling 24h VWAP**: `8.78952` | **Distance to VWAP**: `+1.12%`
- **VWAP Z-Score**: `+1.01 sigma` | **Mean Reversion Bias**: **`FAIR VALUE`**
- **VWAP Dispersion Bands**:
  * +1.00 sigma: `8.79890` | -1.00 sigma: `8.60611`
  * +1.28 sigma (80% CI): `8.82590` | -1.28 sigma: `8.57912`
  * +2.00 sigma (95% CI): `8.89530` | -2.00 sigma: `8.50971`
  * +2.01 sigma: `8.89627` | -2.01 sigma: `8.50875`
  * +2.51 sigma (98.8% CI): `8.94446` | -2.51 sigma: `8.46055`
  * +3.00 sigma (99.7% CI Extreme): `8.99170` | -3.00 sigma: `8.41331`
- **Oscillators & Volatility**:
  * **RSI (14)**: `59.44` | **RSI State**: **`BULLISH`**
  * **ATR (14)**: `0.04873` | **ATR %**: `0.55%`
  * **Bollinger Bands**: Upper=`8.81013` | Mid=`8.73850` | Lower=`8.66687` | Bandwidth=`1.64%`
  * **MACD**: Line=`+0.0225` | Signal=`+0.0156` | Hist=`+0.0068`
- **Exponential Moving Average Ribbon (EMA)**:
  * Short Horizon: EMA-5=`8.77806` | EMA-9=`8.76603` | EMA-13=`8.75564` | EMA-20=`8.74198`
  * Intermediate: EMA-34=`8.73354` | EMA-50=`8.74138` | EMA-89=`8.77314` | EMA-100=`8.78098`
  * Institutional: EMA-144=`8.80349` | EMA-200=`8.81237` (Slope: `-0.080%`) | EMA-233=`8.81911` (Slope: `-0.076%`)
  * **Trend Bias**: **`BULLISH`**

---

## 3. Auction Market Structure & Value Profile
*(Sources: 20_Auction_Market_Structure.parquet)*
- **Daily Auction Value Area**:
  * High (VAH): `8.81000` | Point of Control (POC): `8.74000` | Low (VAL): `8.59000`
  * Distance to POC: `+1.04%` | Distance to VAH: `+0.18%` | Distance to VAL: `+2.80%`
  * **Value Area Position**: **`ABOVE_VALUE (Imbalance)`** | **Auction Regime**: **`RANGE_EXPANSION`** | **Session Bias**: **`BEARISH (Below Pivot)`**
- **Prior Day & Weekly Auction Profile**:
  * Prior Day: PD VAH=`9.02000` | PD POC=`8.99000` | PD VAL=`8.86000` | PDH=`9.14000` | PDL=`8.76000` | PDC=`8.99000`
  * Monday Reference: Monday High=`9.03000` | Monday Low=`8.73000` | Monday Mid=`8.88000`
  * Weekly Value Area: Weekly VAH=`8.96000` | Weekly POC=`8.91000` | Weekly VAL=`8.74000`
  * Multi-Week Extremes: Current Week High (CWH)=`9.14000` | CWL=`8.53000` | Prior Week High (PWH)=`10.03000` | PWL=`8.65000`
  * Multi-Month Extremes: Current Month High (CMH)=`11.71000` | CML=`8.53000` | Prior Month High (PMH)=`11.98000` | PML=`7.02000`
- **Session Liquidity Extremes & Initial Balance**:
  * Asian Session: Range `[8.53000 - 9.04000]`
  * London Session: Range `[8.59000 - 8.81000]`
  * New York Session: Range `[8.68000 - 8.83000]`
  * Initial Balance (IB): IB High=`8.78000` | IB Low=`8.65000`
- **Fibonacci Golden Pocket & Optimal Trade Entry (OTE)**:
  * Swing Range: High=`9.14000` | Low=`8.53000` | Direction=`BEARISH_IMPULSE`
  * Golden Pocket [0.618 - 0.65]: `[8.91000 - 8.93000]`
  * Optimal Trade Entry (0.702): `8.96000` | Invalidation Level: `9.01000` | Status: **`SHALLOW_RETRACE`**
- **Classical & Weekly Pivots**:
  * Daily Classical: Pivot=`8.96000` | R1=`9.17000` | S1=`8.79000` | R2=`9.34000` | S2=`8.58000`
  * Weekly Classical: Weekly Pivot=`9.20000` | Weekly R1=`9.76000` | Weekly S1=`8.38000`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Orderflow
*(Sources: 18_CVD.parquet, 18_CVD_30D_5m.parquet, 18_CVD_30D_15m.parquet, 18_CVD_30D_1h.parquet, 18_CVD_30D_4h.parquet, 18_CVD_30D_ALL.parquet, 21_Tradfye_Orderflow.parquet)*
- **Primary 15m CVD Microstructure (18_CVD_30D_15m.parquet)**:
  * Candle Delta: `-10,485.67 USD` (Base: `-1,193.0000 coins`) | Delta %: `-1.05%`
  * Taker Volumes: Taker Buy=`492,320.27 USD` | Taker Sell=`502,805.95 USD` | Total Vol=`112,807.00 USD`
  * Cumulative CVD: `+772,159.38 USD` (Base: `+76,946.0000`)
  * Rolling CVD Z-Score: `+0.01 sigma` | Price Return: `+0.17%`
  * **Delta Regime**: **`BEARISH ABSORPTION`** | Trades Count: `6,019`
- **Multi-Timeframe Delta Comparison**:
  * 5m Bar: Delta=`+30,429.91 USD` | Delta %=`+17.48%` | Z-Score=`+0.31` | Regime=`AGGRESSIVE BUYING`
  * 1h Bar: Delta=`-10,468.00 USD` | Delta %=`-1.05%` | Z-Score=`-0.06` | Regime=`BEARISH ABSORPTION`
  * 4h Bar: Delta=`-64,174.86 USD` | Delta %=`-0.60%` | Z-Score=`-0.19` | Regime=`BEARISH ABSORPTION`
  * 30D Consolidated (ALL): Cumulative Trend=`+1,160,233.05 USD` | Long-Term Regime=`BEARISH ABSORPTION`
- **Institutional Footprint & Deribit Options Armor (21_Tradfye_Orderflow.parquet)**:
  * Candle VWAP: `8.63000` | Estimated POC: `8.63200` | Avg Trade Size: `206.63 USD`
  * Net Delta USD: `+92,714.86 USD` | Net Delta %: `+6.67%` | Orderflow CVD: `+92,714.86 USD`
  * Orderflow Regime: **`TWO_SIDED_ABSORPTION`** | Orderflow Divergence: **`BULLISH_EXPANSION`**
  * Deribit Options Walls: Max Pain=`0.00` | Call Wall=`0.00` | Put Wall=`0.00`

---

## 5. Institutional Whale Armor & Resting Orderbook Depth
*(Sources: 10_Whale_Orders.parquet, 12_Hyperdash.parquet, 17_Orderbook.parquet, 4_Hyperliquid_Analysis.parquet)*
- **Defending Resting Whale Walls (10_Whale_Orders.parquet)**:
  * Defending Bid Wall: `7.43800` (`139822.5329` coins / `1,040,000.00 USD` on `Binance`, persistent for `15m 56s`, Traded: `0.0%`, Order ID: `CG_LADDER_AVAX_99`)
  * Defending Ask Wall: `9.00500` (`94947.2515` coins / `855,000.00 USD` on `Hyperliquid`, persistent for `27m 49s`, Traded: `0.0%`, Order ID: `CG_WHALE_AVAX_T_11`)
  * Total Whale Armor Pool: Bids Pool=`21,500,300.00 USD` | Asks Pool=`20,157,500.00 USD` (Tracked Orders: `190`)
- **Hyperdash Resting Depth & L3 Telemetry (12_Hyperdash.parquet)**:
  * `NEUTRAL`: `0.00 USD` @ `0.00000` (Size: `0.0`, Detail: Delta: +0, Wallet: None, Timestamp: 2026-10-29 19:44:05 IST)
- **Consolidated L2 Orderbook Depth & Skew (17_Orderbook.parquet)**:
  * `ASK`: `358.78 USD` @ `8.83 USD` (Coins: 40.6200 AVAX, Cumulative: 35,703.50 USD, Tier: 1 orders, Dist: +0.06%, Bias: B/A: 61.3% / 38.7%)
  * `ASK`: `1,358.63 USD` @ `8.83 USD` (Coins: 153.8200 AVAX, Cumulative: 35,344.72 USD, Tier: 2 orders, Dist: +0.06%, Bias: B/A: 61.3% / 38.7%)
  * `ASK`: `999.93 USD` @ `8.83 USD` (Coins: 113.2100 AVAX, Cumulative: 33,986.08 USD, Tier: 1 orders, Dist: +0.06%, Bias: B/A: 61.3% / 38.7%)
- **Hyperliquid Elite Trader Positioning (4_Hyperliquid_Analysis.parquet)**:
  * Wallet `0x77375a8c9d...` (0x7737...bf66): `Short` `1,514,517.05 USD` (171,568.0600 AVAX, Margin: 151,451.70 USD, Leverage: 10X Cross, Entry: 7.4346 USD, Current: 8.8255 USD, Est Liq: 111.6992 USD, PnL: -238,972.03 USD [-15.78%], Fees: -14,711.08 USD)
  * Wallet `0xeadc152ac1...` (0xeadc...9d55): `Long` `1,413,294.99 USD` (160,070.5600 AVAX, Margin: 141,329.50 USD, Leverage: 10X Cross, Entry: 8.1066 USD, Current: 8.8255 USD, Est Liq: 0.00 USD, PnL: +115,657.41 USD [+8.18%], Fees: +110,418.51 USD)

---

## 6. Liquidation Max Pain, Heatmaps & Cascade Boundaries
*(Sources: 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 14_Hyperdash_Liq_Map.parquet, 14_Liquidation_Matrix.parquet, 15_Hyperdash_Stops_Map.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`8.96220` (Vol: `194,000 USD`, Dist: `+1.37%`) | Long MP=`8.45820` (Vol: `190,100 USD`, Dist: `-4.33%`)
  * 48H Horizon: Short MP=`8.96220` (Vol: `194,000 USD`, Dist: `+1.37%`) | Long MP=`8.45820` (Vol: `190,100 USD`, Dist: `-4.33%`)
  * 3D Horizon: Short MP=`8.96220` (Vol: `194,000 USD`, Dist: `+1.37%`) | Long MP=`8.55060` (Vol: `157,300 USD`, Dist: `-3.28%`)
  * 7D Horizon: Short MP=`9.28220` (Vol: `346,800 USD`, Dist: `+4.99%`) | Long MP=`8.53700` (Vol: `343,100 USD`, Dist: `-3.44%`)
- **Exchange Cumulative Liquidation Cascades (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
  * 1D Cascade: Total=`4.75M USD` | Short Liq Pool=`4.75M USD` | Long Liq Pool=`0 USD` | Venues: Binance=`9.81K USD`, OKX=`0 USD`, Bybit=`0 USD`
  * 7D Cascade: Total=`15.55M USD` | Short Liq Pool=`15.55M USD` | Long Liq Pool=`0 USD` | Venues: Binance=`28.63K USD`, OKX=`3.27K USD`, Bybit=`4.65K USD`
- **Cross-Venue Liquidation Matrix & Heatmaps (14_Liquidation_Matrix.parquet, 7_Liq_Heapmap.parquet)**:
  * Liquidation Matrix Strike: Price=`17.64500` | Vol=`6,530 USD` | Cumulative=`1,540,000 USD` | Venue=`Hyperliquid L1` | Side=`Short Liquidation`
  * Multi-Timeframe Heatmap Density: 1h=`0.00 USD` | 4h=`0.00 USD` | 12h=`284.19K USD` | 24h=`1.19M USD`
- **Hyperdash Real-Time Liquidation & Retail Stop Protection (14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet)**:
  * Hyperdash Liq Cluster: Mark=`8.8270 USD` | Cluster Price=`17.6450 USD` | Dist=`+99.90%` | Cumulative=`1.54M USD` | Short=`6.53K USD` | Long=`0 USD` | Size=`370.0600 AVAX`
  * **Retail Stops Map (Pitfall 2 & 4 Defense)**:
    - `Sell Stop`: `1.2050 USD` (Dist: `-86.35%`, Cumulative Stops: `333.63K USD`, Buy: `0 USD`, Sell: `137.09 USD`, Coins: `113.7700 AVAX`)
    - `Sell Stop`: `2.3250 USD` (Dist: `-73.66%`, Cumulative Stops: `333.49K USD`, Buy: `0 USD`, Sell: `611.73 USD`, Coins: `263.1100 AVAX`)
    - `Sell Stop`: `4.0050 USD` (Dist: `-54.63%`, Cumulative Stops: `332.88K USD`, Buy: `0 USD`, Sell: `793.75 USD`, Coins: `198.1900 AVAX`)
- **Live Forced Liquidation Momentum (7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)**:
  * Multi-Timeframe Forced Aggregates (5m): Long Liq=`0.00 USD` | Short Liq=`0.00 USD` | Total=`0.00 USD` | Net Delta=`0.00 USD` | Dominant=`BALANCED`

---

## 7. Derivatives Sentiment, Open Interest & Funding Dynamics
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet, 6_Funding_Fee_Settlement.parquet, 13_Hyperliquid.parquet)*
- **Aggregated Open Interest Breakdown (5_OI.parquet)**:
  * Total Open Interest: `381.92M USD` (`43,320,504.4 AVAX`) | OI / 24h Volume Ratio: `0.9420`
  * OI Expansion Rate: 1h Change=`+0.32%` | 4h Change=`+1.10%` | 24h Change=`-2.04%`
  * Venue Concentration:
    - Binance: `88.71M USD` | Bybit: `59.43M USD` | OKX: `12.64M USD` | CME Institutional: `0.00 USD`
    - Gate: `54.72M USD` | MEXC: `36.43M USD` | Hyperliquid DEX: `17.94M USD` | Bitget: `26.37M USD`
    - KuCoin: `13.24M USD` | BingX: `24.84M USD` | Bitunix: `3.22M USD` | Others: `44.38M USD`
- **Cross-Exchange Perpetual Funding Rates (5_Funding_Rate.parquet)**:
  * Major CEX Rates: Binance=`+0.0100%` | OKX=`+0.0100%` | Bybit=`+0.0075%` | Bitget=`+0.0100%`
  * Mid-Tier CEX Rates: KuCoin=`+0.0018%` | MEXC=`+0.0100%` | Gate=`+0.0015%` | BingX=`+0.0100%` | Bitunix=`+0.0055%`
  * Alternative Venues: WhiteBIT=`+0.0100%` | LBank=`+0.0100%` | tradeXYZ=`-`
  * Inverse Coin-Margined: CoinM Binance=`+0.0100%` | CoinM OKX=`+0.0000%` | CoinM Bybit=`+0.0100%`
- **Exchange Long / Short Ratio Dynamics (3_Exchanges_LS_Ratio*.parquet)**:
  * 15m Tactical: L/S Ratio=`0.94` (Longs: `48.56%`, Shorts: `51.44%`, Total Vol: `3.95M USD`)
  * 1h Primary: L/S Ratio=`0.99` (Longs: `49.71%`, Shorts: `50.29%`, Total Vol: `23.93M USD`)
  * 4h Macro: L/S Ratio=`0.93` (Longs: `48.28%`, Shorts: `51.72%`, Total Vol: `88.69M USD`)
- **Funding Fee Settlement & DEX Arbitrage (6_Funding_Fee_Settlement.parquet, 13_Hyperliquid.parquet)**:
  * Settlement Payouts: Current Expected=`14.21K USD` | Last 24h=`22.13K USD` | Last 3D=`69.43K USD` | Last 7D=`58.50K USD`

---

## 8. Microstructure Footprint, Tape Imbalances & Macro Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 16_Hyperdash_telegram_Intel.parquet, 19_News.parquet, 19_Calendar.parquet)*
- **Bar-by-Bar Microstructure Footprint (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
  * Venue Source: `CoinGlass-AggregatedFutures(Binance)` | Timeframe: `15m` | Last Price: `8.83000`
  * Footprint Auction Profile: Bar VWAP=`8.82136` | Bar POC=`8.82050` | Bar VAH=`8.83550` | Bar VAL=`8.80450`
  * Orderflow Volumes: Total Vol=`849,519.07 USD` | Taker Buy=`394,689.65 USD` | Taker Sell=`454,829.42 USD`
  * Bar Delta Profile: Delta=`-60,139.77 USD` (`-7.08%`) | Max Delta=`+0.00 USD` | Min Delta=`-65,148.40 USD` | Cumulative Bar Delta=`+327,012.04 USD`
  * Order Execution Dynamics: Trades Count=`4,982` | Avg Trade Size=`170.52 USD`
  * Tape Imbalances: Imbalance Ratio=`300.0%` | Buy Imbalances Count=`3` | Sell Imbalances Count=`5`
  * Footprint Open Interest: Bar OI=`0.00 USD` | Bar OI Change=`+0.00 USD`
- **CoinGlass Algorithmic Footprint Signals (25_CoinGlass_Footprint_Signals.parquet)**:
  * Signal Classification: Type=`Divergence` | Bias: **`BEARISH`** | Signal Time=`10-28 06:13` | Timeframe=`Range 0.025`
  * Signal Context: Headline=`Rally without taker buying` | Price Level=`8.98000` | Absorbed Volume=`0.00 USD`
  * Bar Footprint Context: Current Bar Delta=`+0.00 USD` | Current Bar Volume=`0.00 USD` | Delta in View=`+0.00 USD`
  * Historical Detail: `Closed up on negative Delta (−29%), bearish · 8.9800` | KPI=`—` | Bias=`—`
- **Multi-Horizon Macro Capital Netflows (2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet)**:
  * Spot Capital Netflows:
    - Tactical: 5m=`+646.83` | 15m=`-40.79K` | 30m=`-95.79K` | 1h=`-99.88K`
    - Intermediate: 2h=`-248.41K` | 4h=`-379.80K` | 6h=`-407.59K` | 8h=`-477.49K` | 12h=`+13.32K` | 24h=`+88.75K`
    - Macro Horizons: 1-Week=`-6.91M` | 15-Day=`-22.61M` | 30-Day=`-51.83M` | Market Cap=`3.91B`
  * Futures Capital Netflows:
    - Tactical: 5m=`-9.89K` | 15m=`+40.36K` | 30m=`+39.43K` | 1h=`-41.56K`
    - Intermediate: 2h=`+829.06K` | 4h=`+74.94K` | 6h=`+389.58K` | 8h=`-73.62K` | 12h=`-312.86K` | 24h=`-336.55K`
    - Macro Horizons: 1-Week=`-42.93M` | 15-Day=`-82.26M` | 30-Day=`-275.11M` | Market Cap=`3.91B`
- **Telegram Intelligence Alert**: `[MARKET_INTEL] #AVAX Whale SELL: 5.18K USD at 8.9425 USD [API] (Impact: NEWS_INTEL)`

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
- **Stand-Aside Reason**: Gate 1 Spread Friction Failure: Spread friction 45.30 bps exceeds cap 25.0 bps. Standing aside in 100% cash preserves statutory floor.