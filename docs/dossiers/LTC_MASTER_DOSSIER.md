# 🔬 MASTER 43-FEED QUANTITATIVE DOSSIER: LTC (Litecoin)
**MT5 Symbol**: `LTCUSD.pi` | **Category**: `Crypto PoW` | **Tier**: `Tier 1`
**Execution Posture**: `DISQUALIFIED` | **Timestamp**: 2026-10-29 14:43:14 UTC
**Pipeline Clearance**: `BLOCKED` | **Data Freshness**: `1.2m`

---

## 1. MT5 Live Broker Telemetry & Spread Friction Gate
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet)*
- **Live Bid Quote**: `57.84000` | **Live Ask Quote**: `58.14000` | **Mid Price**: `57.99000`
- **Spread Points**: `300.0 pts` | **Spread BPS**: `51.73 bps` (Mandatory Cap: `25.0 bps`)
- **Gate Status**: **`FAIL`** (Spread friction 51.73 bps exceeds cap 25.0 bps)
- **Order Allowed**: `NONE` | **Pillar 1 Clearance**: `BLOCKED`
- **Broker Specifications**: Contract Size=`1.00` | Tick Value=`1.00 USD` | Min Lot=`0.01` | Digits=`5`
- **Account Capital Context**: Balance=`4,744.55 USD` | Equity=`4,744.32 USD` | Free Margin=`4,342.62 USD` | Inviolate Hard Floor=`4,775.00 USD` (Cushion: `-30.68 USD`)
- **Pipeline Health**: Feed #00 Status=`PASS` | Overall Pipeline Telemetry=`33/33 FEEDS PASS (SYNCHRONIZED)`

---

## 2. Technical Profile, Multi-Sigma VWAP Dispersion & Volatility
*(Sources: 11_Technical.parquet, 11_Technical_BTC_Ribbon.parquet)*
- **Last Verified Price**: `57.73500` | **24h Change**: `+1.16%` (24h High: `59.62000`, 24h Low: `56.67000`)
- **Weekly Range**: Week High=`59.62000` | Week Low=`55.48500` | Daily POC=`57.83600` | Daily VAH=`58.27300` | Daily VAL=`56.73600`
- **Session VWAP**: `57.76280` | **Rolling 24h VWAP**: `58.14509` | **Distance to VWAP**: `-0.05%`
- **VWAP Z-Score**: `-0.04 sigma` | **Mean Reversion Bias**: **`FAIR VALUE`**
- **VWAP Dispersion Bands**:
  * +1.00 sigma: `58.45359` | -1.00 sigma: `57.07201`
  * +1.28 sigma (80% CI): `58.64701` | -1.28 sigma: `56.87859`
  * +2.00 sigma (95% CI): `59.14438` | -2.00 sigma: `56.38122`
  * +2.01 sigma: `59.15129` | -2.01 sigma: `56.37432`
  * +2.51 sigma (98.8% CI): `59.49668` | -2.51 sigma: `56.02892`
  * +3.00 sigma (99.7% CI Extreme): `59.83517` | -3.00 sigma: `55.69044`
- **Oscillators & Volatility**:
  * **RSI (14)**: `53.89` | **RSI State**: **`NEUTRAL`**
  * **ATR (14)**: `0.26909` | **ATR %**: `0.47%`
  * **Bollinger Bands**: Upper=`58.21391` | Mid=`57.59700` | Lower=`56.98009` | Bandwidth=`2.14%`
  * **MACD**: Line=`+0.1199` | Signal=`+0.1012` | Hist=`+0.0187`
- **Exponential Moving Average Ribbon (EMA)**:
  * Short Horizon: EMA-5=`57.77341` | EMA-9=`57.76640` | EMA-13=`57.71938` | EMA-20=`57.64360`
  * Intermediate: EMA-34=`57.60813` | EMA-50=`57.64802` | EMA-89=`57.69699` | EMA-100=`57.68972`
  * Institutional: EMA-144=`57.60678` | EMA-200=`57.41729` (Slope: `+0.085%`) | EMA-233=`57.25054` (Slope: `+0.104%`)
  * **Trend Bias**: **`NEUTRAL / CHOP`**

---

## 3. Auction Market Structure & Value Profile
*(Sources: 20_Auction_Market_Structure.parquet)*
- **Daily Auction Value Area**:
  * High (VAH): `58.27300` | Point of Control (POC): `57.83600` | Low (VAL): `56.73600`
  * Distance to POC: `+0.27%` | Distance to VAH: `-0.49%` | Distance to VAL: `+2.21%`
  * **Value Area Position**: **`INSIDE_VALUE (Balance)`** | **Auction Regime**: **`ROTATIONAL_BALANCE`** | **Session Bias**: **`BEARISH (Below Pivot)`**
- **Prior Day & Weekly Auction Profile**:
  * Prior Day: PD VAH=`58.43700` | PD POC=`57.22200` | PD VAL=`56.70100` | PDH=`59.62000` | PDL=`56.36500` | PDC=`58.69000`
  * Monday Reference: Monday High=`57.03000` | Monday Low=`55.77000` | Monday Mid=`56.40000`
  * Weekly Value Area: Weekly VAH=`57.62100` | Weekly POC=`56.49100` | Weekly VAL=`55.96700`
  * Multi-Week Extremes: Current Week High (CWH)=`59.62000` | CWL=`55.48500` | Prior Week High (PWH)=`62.19000` | PWL=`54.91000`
  * Multi-Month Extremes: Current Month High (CMH)=`72.12000` | CML=`54.91000` | Prior Month High (PMH)=`74.81000` | PML=`48.12500`
- **Session Liquidity Extremes & Initial Balance**:
  * Asian Session: Range `[56.73000 - 59.51500]`
  * London Session: Range `[56.67000 - 58.12000]`
  * New York Session: Range `[57.04000 - 58.13000]`
  * Initial Balance (IB): IB High=`58.02000` | IB Low=`57.29000`
- **Fibonacci Golden Pocket & Optimal Trade Entry (OTE)**:
  * Swing Range: High=`59.62000` | Low=`56.67000` | Direction=`BEARISH_IMPULSE`
  * Golden Pocket [0.618 - 0.65]: `[58.49300 - 58.58700]`
  * Optimal Trade Entry (0.702): `58.74100` | Invalidation Level: `58.98900` | Status: **`SHALLOW_RETRACE`**
- **Classical & Weekly Pivots**:
  * Daily Classical: Pivot=`58.22500` | R1=`60.08500` | S1=`56.83000` | R2=`61.48000` | S2=`54.97000`
  * Weekly Classical: Weekly Pivot=`57.98500` | Weekly R1=`61.06000` | Weekly S1=`53.78000`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Orderflow
*(Sources: 18_CVD.parquet, 18_CVD_30D_5m.parquet, 18_CVD_30D_15m.parquet, 18_CVD_30D_1h.parquet, 18_CVD_30D_4h.parquet, 18_CVD_30D_ALL.parquet, 21_Tradfye_Orderflow.parquet)*
- **Primary 15m CVD Microstructure (18_CVD_30D_15m.parquet)**:
  * Candle Delta: `+36,696.63 USD` (Base: `+633.5180 coins`) | Delta %: `+9.03%`
  * Taker Volumes: Taker Buy=`221,623.36 USD` | Taker Sell=`184,926.73 USD` | Total Vol=`7,013.85 USD`
  * Cumulative CVD: `+678,306.26 USD` (Base: `+12,575.6180`)
  * Rolling CVD Z-Score: `+0.01 sigma` | Price Return: `+0.19%`
  * **Delta Regime**: **`DELTA ALIGNED`** | Trades Count: `3,216`
- **Multi-Timeframe Delta Comparison**:
  * 5m Bar: Delta=`+2,800.32 USD` | Delta %=`+3.43%` | Z-Score=`-0.09` | Regime=`NEUTRAL CHOP`
  * 1h Bar: Delta=`+36,696.63 USD` | Delta %=`+9.03%` | Z-Score=`+0.18` | Regime=`DELTA ALIGNED`
  * 4h Bar: Delta=`+574,038.99 USD` | Delta %=`+9.98%` | Z-Score=`+1.26` | Regime=`DELTA ALIGNED`
  * 30D Consolidated (ALL): Cumulative Trend=`-1,245,824.28 USD` | Long-Term Regime=`DELTA ALIGNED`
- **Institutional Footprint & Deribit Options Armor (21_Tradfye_Orderflow.parquet)**:
  * Candle VWAP: `58.14864` | Estimated POC: `58.22000` | Avg Trade Size: `221.26 USD`
  * Net Delta USD: `-77,996.05 USD` | Net Delta %: `-13.06%` | Orderflow CVD: `-77,996.05 USD`
  * Orderflow Regime: **`AGGRESSIVE_SELLER_DOMINATION`** | Orderflow Divergence: **`BEARISH_ABSORPTION`**
  * Deribit Options Walls: Max Pain=`0.00` | Call Wall=`0.00` | Put Wall=`0.00`

---

## 5. Institutional Whale Armor & Resting Orderbook Depth
*(Sources: 10_Whale_Orders.parquet, 12_Hyperdash.parquet, 17_Orderbook.parquet, 4_Hyperliquid_Analysis.parquet)*
- **Defending Resting Whale Walls (10_Whale_Orders.parquet)**:
  * Defending Bid Wall: `57.26000` (`6531.6102` coins / `374,000.00 USD` on `Binance`, persistent for `28s`, Traded: `0.0%`, Order ID: `CG_LADDER_LTC_97`)
  * Defending Ask Wall: `58.36000` (`6271.4188` coins / `366,000.00 USD` on `Bybit`, persistent for `28s`, Traded: `0.0%`, Order ID: `CG_WHALE_LTC_T_9`)
  * Total Whale Armor Pool: Bids Pool=`11,224,100.00 USD` | Asks Pool=`11,163,000.00 USD` (Tracked Orders: `182`)
- **Hyperdash Resting Depth & L3 Telemetry (12_Hyperdash.parquet)**:
  * `NEUTRAL`: `0.00 USD` @ `0.00000` (Size: `0.0`, Detail: Delta: +0, Wallet: None, Timestamp: 2026-10-29 19:44:05 IST)
- **Hyperliquid Elite Trader Positioning (4_Hyperliquid_Analysis.parquet)**:
  * Wallet `0xeadc152ac1...` (0xeadc...9d55): `Long` `2,114,643.41 USD` (36,463.7700 LTC, Margin: 211,464.34 USD, Leverage: 10X Cross, Entry: 52.7832 USD, Current: 57.9380 USD, Est Liq: 0.00 USD, PnL: +189,967.46 USD [+8.98%], Fees: +104,931.32 USD)
  * Wallet `0x9aa589355b...` (0x9aa5...58af): `Short` `2,097,363.08 USD` (36,177.6500 LTC, Margin: 209,736.31 USD, Leverage: 10X Cross, Entry: 71.2176 USD, Current: 57.9380 USD, Est Liq: 269.2929 USD, PnL: +479,123.59 USD [+22.84%], Fees: -21,461.70 USD)
  * Wallet `0xcac19662ec...` (0xcac1...26b3): `Short` `1,009,974.37 USD` (17,411.5500 LTC, Margin: 100,997.44 USD, Leverage: 10X Cross, Entry: 49.0137 USD, Current: 57.9380 USD, Est Liq: 505.2141 USD, PnL: -156,569.05 USD [-15.50%], Fees: -23,974.19 USD)

---

## 6. Liquidation Max Pain, Heatmaps & Cascade Boundaries
*(Sources: 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 14_Hyperdash_Liq_Map.parquet, 14_Liquidation_Matrix.parquet, 15_Hyperdash_Stops_Map.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`59.03000` (Vol: `206,500 USD`, Dist: `+1.83%`) | Long MP=`56.68400` (Vol: `275,700 USD`, Dist: `-2.22%`)
  * 48H Horizon: Short MP=`58.99200` (Vol: `215,600 USD`, Dist: `+1.76%`) | Long MP=`56.71300` (Vol: `253,400 USD`, Dist: `-2.17%`)
  * 3D Horizon: Short MP=`60.60000` (Vol: `240,800 USD`, Dist: `+4.54%`) | Long MP=`56.69500` (Vol: `233,500 USD`, Dist: `-2.20%`)
  * 7D Horizon: Short MP=`59.03600` (Vol: `206,500 USD`, Dist: `+1.84%`) | Long MP=`55.26600` (Vol: `344,500 USD`, Dist: `-4.66%`)
- **Exchange Cumulative Liquidation Cascades (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
  * 1D Cascade: Total=`7.70M USD` | Short Liq Pool=`7.70M USD` | Long Liq Pool=`0 USD` | Venues: Binance=`10.61K USD`, OKX=`6.45K USD`, Bybit=`10.13K USD`
  * 7D Cascade: Total=`10.92M USD` | Short Liq Pool=`10.92M USD` | Long Liq Pool=`0 USD` | Venues: Binance=`44.99K USD`, OKX=`6.76K USD`, Bybit=`8.36K USD`
- **Cross-Venue Liquidation Matrix & Heatmaps (14_Liquidation_Matrix.parquet, 7_Liq_Heapmap.parquet)**:
  * Liquidation Matrix Strike: Price=`110.95000` | Vol=`665 USD` | Cumulative=`738,600 USD` | Venue=`Hyperliquid L1` | Side=`Short Liquidation`
  * Multi-Timeframe Heatmap Density: 1h=`0.00 USD` | 4h=`0.00 USD` | 12h=`0.00 USD` | 24h=`0.00 USD`
- **Hyperdash Real-Time Liquidation & Retail Stop Protection (14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet)**:
  * Hyperdash Liq Cluster: Mark=`57.9730 USD` | Cluster Price=`110.9500 USD` | Dist=`+91.38%` | Cumulative=`738.60K USD` | Short=`664.59 USD` | Long=`0 USD` | Size=`5.9900 LTC`
  * **Retail Stops Map (Pitfall 2 & 4 Defense)**:
    - `Sell Stop`: `20.0500 USD` (Dist: `-65.41%`, Cumulative Stops: `483.23K USD`, Buy: `0 USD`, Sell: `392.18 USD`, Coins: `19.5600 LTC`)
    - `Sell Stop`: `22.0500 USD` (Dist: `-61.97%`, Cumulative Stops: `482.84K USD`, Buy: `0 USD`, Sell: `2.31K USD`, Coins: `104.6200 LTC`)
    - `Sell Stop`: `25.0500 USD` (Dist: `-56.79%`, Cumulative Stops: `480.53K USD`, Buy: `0 USD`, Sell: `122.24 USD`, Coins: `4.8800 LTC`)
- **Live Forced Liquidation Momentum (7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)**:
  * Real-Time Stream: Coin=`LTCUSDT` | Side=`Short` | Price=`58.89 USD` | Amount=`1.34K USD` | Exchange=`Binance` | Time=`2026-10-28 21:47:16 IST`
  * Multi-Timeframe Forced Aggregates (5m): Long Liq=`0.00 USD` | Short Liq=`1,340.00 USD` | Total=`1,340.00 USD` | Net Delta=`1,340.00 USD` | Dominant=`BALANCED`

---

## 7. Derivatives Sentiment, Open Interest & Funding Dynamics
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet, 6_Funding_Fee_Settlement.parquet, 13_Hyperliquid.parquet)*
- **Aggregated Open Interest Breakdown (5_OI.parquet)**:
  * Total Open Interest: `455.49M USD` (`7,866,822.2 LTC`) | OI / 24h Volume Ratio: `1.0517`
  * OI Expansion Rate: 1h Change=`-0.65%` | 4h Change=`+1.39%` | 24h Change=`+0.22%`
  * Venue Concentration:
    - Binance: `81.76M USD` | Bybit: `69.32M USD` | OKX: `34.85M USD` | CME Institutional: `0.00 USD`
    - Gate: `81.97M USD` | MEXC: `55.85M USD` | Hyperliquid DEX: `22.85M USD` | Bitget: `32.59M USD`
    - KuCoin: `20.84M USD` | BingX: `17.51M USD` | Bitunix: `4.46M USD` | Others: `33.49M USD`
- **Cross-Exchange Perpetual Funding Rates (5_Funding_Rate.parquet)**:
  * Major CEX Rates: Binance=`+0.0100%` | OKX=`+0.0100%` | Bybit=`+0.0094%` | Bitget=`+0.0100%`
  * Mid-Tier CEX Rates: KuCoin=`+0.0100%` | MEXC=`+0.0100%` | Gate=`+0.0100%` | BingX=`+0.0100%` | Bitunix=`+0.0100%`
  * Alternative Venues: WhiteBIT=`+0.0100%` | LBank=`+0.0100%` | tradeXYZ=`-`
  * Inverse Coin-Margined: CoinM Binance=`+0.0100%` | CoinM OKX=`+0.0100%` | CoinM Bybit=`+0.0100%`
- **Exchange Long / Short Ratio Dynamics (3_Exchanges_LS_Ratio*.parquet)**:
  * 15m Tactical: L/S Ratio=`0.60` (Longs: `37.54%`, Shorts: `62.46%`, Total Vol: `8.40M USD`)
  * 1h Primary: L/S Ratio=`0.92` (Longs: `47.81%`, Shorts: `52.19%`, Total Vol: `26.33M USD`)
  * 4h Macro: L/S Ratio=`0.93` (Longs: `48.32%`, Shorts: `51.68%`, Total Vol: `20.43M USD`)
- **Funding Fee Settlement & DEX Arbitrage (6_Funding_Fee_Settlement.parquet, 13_Hyperliquid.parquet)**:
  * Settlement Payouts: Current Expected=`16.51K USD` | Last 24h=`6.52K USD` | Last 3D=`60.13K USD` | Last 7D=`92.20K USD`

---

## 8. Microstructure Footprint, Tape Imbalances & Macro Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 16_Hyperdash_telegram_Intel.parquet, 19_News.parquet, 19_Calendar.parquet)*
- **Bar-by-Bar Microstructure Footprint (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
  * Venue Source: `CoinGlass-AggregatedFutures(Binance)` | Timeframe: `15m` | Last Price: `57.99000`
  * Footprint Auction Profile: Bar VWAP=`57.96605` | Bar POC=`57.96500` | Bar VAH=`58.06500` | Bar VAL=`57.88500`
  * Orderflow Volumes: Total Vol=`346,305.83 USD` | Taker Buy=`187,646.24 USD` | Taker Sell=`158,659.59 USD`
  * Bar Delta Profile: Delta=`+28,986.64 USD` (`+8.37%`) | Max Delta=`+43,561.69 USD` | Min Delta=`-4,882.67 USD` | Cumulative Bar Delta=`+387,421.83 USD`
  * Order Execution Dynamics: Trades Count=`2,684` | Avg Trade Size=`129.03 USD`
  * Tape Imbalances: Imbalance Ratio=`300.0%` | Buy Imbalances Count=`3` | Sell Imbalances Count=`2`
  * Footprint Open Interest: Bar OI=`0.00 USD` | Bar OI Change=`+0.00 USD`
- **CoinGlass Algorithmic Footprint Signals (25_CoinGlass_Footprint_Signals.parquet)**:
  * Signal Classification: Type=`Absorption` | Bias: **`BULLISH`** | Signal Time=`10-28 07:52` | Timeframe=`Range 0.2`
  * Signal Context: Headline=`Selling absorbed at the low` | Price Level=`57.28000` | Absorbed Volume=`2,800.00 USD`
  * Bar Footprint Context: Current Bar Delta=`+0.00 USD` | Current Bar Volume=`0.00 USD` | Delta in View=`+0.00 USD`
  * Historical Detail: `2.8K of taker selling at the low (30%+ of the bar's selling), yet closed near the high, bullish · 57.280` | KPI=`—` | Bias=`—`
- **Multi-Horizon Macro Capital Netflows (2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet)**:
  * Spot Capital Netflows:
    - Tactical: 5m=`-17.60K` | 15m=`-58.42K` | 30m=`-87.08K` | 1h=`-332.61K`
    - Intermediate: 2h=`-73.24K` | 4h=`+536.04K` | 6h=`+675.86K` | 8h=`+769.68K` | 12h=`+333.12K` | 24h=`+786.83K`
    - Macro Horizons: 1-Week=`+2.54M` | 15-Day=`+1.13M` | 30-Day=`-23.38M` | Market Cap=`4.50B`
  * Futures Capital Netflows:
    - Tactical: 5m=`+57.10K` | 15m=`+105.85K` | 30m=`+167.65K` | 1h=`-62.00K`
    - Intermediate: 2h=`+1.57M` | 4h=`+2.49M` | 6h=`+2.87M` | 8h=`+1.91M` | 12h=`+987.98K` | 24h=`-681.87K`
    - Macro Horizons: 1-Week=`-23.70M` | 15-Day=`-51.89M` | 30-Day=`-199.16M` | Market Cap=`4.50B`
- **Telegram Intelligence Alert**: `[MARKET_INTEL] #LTC Whale SELL: 10.00K USD at 56.6050 USD [API] (Impact: NEWS_INTEL)`

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
- **Stand-Aside Reason**: Gate 1 Spread Friction Failure: Spread friction 51.73 bps exceeds cap 25.0 bps. Standing aside in 100% cash preserves statutory floor.