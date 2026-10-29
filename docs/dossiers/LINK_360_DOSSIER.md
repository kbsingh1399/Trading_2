# 🔬 MASTER 43-FEED QUANTITATIVE DOSSIER: LINK (Chainlink)
**MT5 Symbol**: `LNKUSD.p` | **Category**: `Crypto DeFi` | **Tier**: `Tier 1`
**Execution Posture**: `DISQUALIFIED` | **Timestamp**: 2026-10-29 14:43:14 UTC
**Pipeline Clearance**: `BLOCKED` | **Data Freshness**: `1.2m`

---

## 1. MT5 Live Broker Telemetry & Spread Friction Gate
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet)*
- **Live Bid Quote**: `11.61900` | **Live Ask Quote**: `11.70600` | **Mid Price**: `11.66250`
- **Spread Points**: `87.0 pts` | **Spread BPS**: `74.60 bps` (Mandatory Cap: `25.0 bps`)
- **Gate Status**: **`FAIL`** (Spread friction 74.60 bps exceeds cap 25.0 bps)
- **Order Allowed**: `NONE` | **Pillar 1 Clearance**: `BLOCKED`
- **Broker Specifications**: Contract Size=`1.00` | Tick Value=`1.00 USD` | Min Lot=`0.01` | Digits=`5`
- **Account Capital Context**: Balance=`4,744.55 USD` | Equity=`4,744.32 USD` | Free Margin=`4,342.62 USD` | Inviolate Hard Floor=`4,775.00 USD` (Cushion: `-30.68 USD`)
- **Pipeline Health**: Feed #00 Status=`PASS` | Overall Pipeline Telemetry=`33/33 FEEDS PASS (SYNCHRONIZED)`

---

## 2. Technical Profile, Multi-Sigma VWAP Dispersion & Volatility
*(Sources: 11_Technical.parquet, 11_Technical_BTC_Ribbon.parquet)*
- **Last Verified Price**: `11.59100` | **24h Change**: `+1.02%` (24h High: `11.93600`, 24h Low: `11.23100`)
- **Weekly Range**: Week High=`11.93600` | Week Low=`11.16700` | Daily POC=`11.32400` | Daily VAH=`11.61000` | Daily VAL=`11.29500`
- **Session VWAP**: `11.46463` | **Rolling 24h VWAP**: `11.53629` | **Distance to VWAP**: `+1.10%`
- **VWAP Z-Score**: `+0.98 sigma` | **Mean Reversion Bias**: **`FAIR VALUE`**
- **VWAP Dispersion Bands**:
  * +1.00 sigma: `11.59330` | -1.00 sigma: `11.33596`
  * +1.28 sigma (80% CI): `11.62932` | -1.28 sigma: `11.29994`
  * +2.00 sigma (95% CI): `11.72196` | -2.00 sigma: `11.20729`
  * +2.01 sigma: `11.72325` | -2.01 sigma: `11.20601`
  * +2.51 sigma (98.8% CI): `11.78758` | -2.51 sigma: `11.14167`
  * +3.00 sigma (99.7% CI Extreme): `11.85063` | -3.00 sigma: `11.07863`
- **Oscillators & Volatility**:
  * **RSI (14)**: `58.13` | **RSI State**: **`BULLISH`**
  * **ATR (14)**: `0.06058` | **ATR %**: `0.52%`
  * **Bollinger Bands**: Upper=`11.64979` | Mid=`11.52325` | Lower=`11.39671` | Bandwidth=`2.20%`
  * **MACD**: Line=`+0.0401` | Signal=`+0.0346` | Hist=`+0.0055`
- **Exponential Moving Average Ribbon (EMA)**:
  * Short Horizon: EMA-5=`11.57924` | EMA-9=`11.56861` | EMA-13=`11.55372` | EMA-20=`11.53050`
  * Intermediate: EMA-34=`11.50845` | EMA-50=`11.50647` | EMA-89=`11.51854` | EMA-100=`11.52061`
  * Institutional: EMA-144=`11.51856` | EMA-200=`11.48964` (Slope: `+0.086%`) | EMA-233=`11.47701` (Slope: `+0.085%`)
  * **Trend Bias**: **`STRONG BULLISH`**

---

## 3. Auction Market Structure & Value Profile
*(Sources: 20_Auction_Market_Structure.parquet)*
- **Daily Auction Value Area**:
  * High (VAH): `11.61000` | Point of Control (POC): `11.32400` | Low (VAL): `11.29500`
  * Distance to POC: `+2.99%` | Distance to VAH: `+0.45%` | Distance to VAL: `+3.25%`
  * **Value Area Position**: **`ABOVE_VALUE (Imbalance)`** | **Auction Regime**: **`RANGE_EXPANSION`** | **Session Bias**: **`BEARISH (Below Pivot)`**
- **Prior Day & Weekly Auction Profile**:
  * Prior Day: PD VAH=`11.69200` | PD POC=`11.50100` | PD VAL=`11.43800` | PDH=`11.93600` | PDL=`11.38500` | PDC=`11.74900`
  * Monday Reference: Monday High=`11.56700` | Monday Low=`11.20800` | Monday Mid=`11.38700`
  * Weekly Value Area: Weekly VAH=`11.53400` | Weekly POC=`11.41600` | Weekly VAL=`11.25700`
  * Multi-Week Extremes: Current Week High (CWH)=`11.93600` | CWL=`11.16700` | Prior Week High (PWH)=`12.75400` | PWL=`11.18100`
  * Multi-Month Extremes: Current Month High (CMH)=`14.60400` | CML=`11.16700` | Prior Month High (PMH)=`15.72300` | PML=`10.54700`
- **Session Liquidity Extremes & Initial Balance**:
  * Asian Session: Range `[11.23100 - 11.85300]`
  * London Session: Range `[11.30100 - 11.60200]`
  * New York Session: Range `[11.41500 - 11.64100]`
  * Initial Balance (IB): IB High=`11.55600` | IB Low=`11.40600`
- **Fibonacci Golden Pocket & Optimal Trade Entry (OTE)**:
  * Swing Range: High=`11.93600` | Low=`11.23100` | Direction=`BEARISH_IMPULSE`
  * Golden Pocket [0.618 - 0.65]: `[11.66700 - 11.68900]`
  * Optimal Trade Entry (0.702): `11.72600` | Invalidation Level: `11.78500` | Status: **`SHALLOW_RETRACE`**
- **Classical & Weekly Pivots**:
  * Daily Classical: Pivot=`11.69000` | R1=`11.99500` | S1=`11.44400` | R2=`12.24100` | S2=`11.13900`
  * Weekly Classical: Weekly Pivot=`11.79000` | Weekly R1=`12.40000` | Weekly S1=`10.82700`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Orderflow
*(Sources: 18_CVD.parquet, 18_CVD_30D_5m.parquet, 18_CVD_30D_15m.parquet, 18_CVD_30D_1h.parquet, 18_CVD_30D_4h.parquet, 18_CVD_30D_ALL.parquet, 21_Tradfye_Orderflow.parquet)*
- **Primary 15m CVD Microstructure (18_CVD_30D_15m.parquet)**:
  * Candle Delta: `+115,593.83 USD` (Base: `+9,909.9300 coins`) | Delta %: `+10.86%`
  * Taker Volumes: Taker Buy=`590,072.04 USD` | Taker Sell=`474,478.21 USD` | Total Vol=`91,360.65 USD`
  * Cumulative CVD: `+474,815.16 USD` (Base: `+35,271.6800`)
  * Rolling CVD Z-Score: `+0.53 sigma` | Price Return: `+0.24%`
  * **Delta Regime**: **`DELTA ALIGNED`** | Trades Count: `6,199`
- **Multi-Timeframe Delta Comparison**:
  * 5m Bar: Delta=`+8,416.69 USD` | Delta %=`+3.31%` | Z-Score=`+0.19` | Regime=`NEUTRAL CHOP`
  * 1h Bar: Delta=`+115,106.46 USD` | Delta %=`+10.81%` | Z-Score=`+0.22` | Regime=`DELTA ALIGNED`
  * 4h Bar: Delta=`-21,413.80 USD` | Delta %=`-0.16%` | Z-Score=`-0.13` | Regime=`BEARISH ABSORPTION`
  * 30D Consolidated (ALL): Cumulative Trend=`+870,921.13 USD` | Long-Term Regime=`BEARISH ABSORPTION`
- **Institutional Footprint & Deribit Options Armor (21_Tradfye_Orderflow.parquet)**:
  * Candle VWAP: `11.40026` | Estimated POC: `11.40625` | Avg Trade Size: `257.28 USD`
  * Net Delta USD: `+348,863.46 USD` | Net Delta %: `+39.21%` | Orderflow CVD: `+348,863.46 USD`
  * Orderflow Regime: **`AGGRESSIVE_BUYER_DOMINATION`** | Orderflow Divergence: **`BULLISH_EXPANSION`**
  * Deribit Options Walls: Max Pain=`0.00` | Call Wall=`0.00` | Put Wall=`0.00`

---

## 5. Institutional Whale Armor & Resting Orderbook Depth
*(Sources: 10_Whale_Orders.parquet, 12_Hyperdash.parquet, 17_Orderbook.parquet, 4_Hyperliquid_Analysis.parquet)*
- **Defending Resting Whale Walls (10_Whale_Orders.parquet)**:
  * Defending Bid Wall: `11.23800` (`195764.3709` coins / `2,210,000.00 USD` on `Hyperliquid`, persistent for `2h 03m`, Traded: `0.0%`, Order ID: `CG_WHALE_LINK_T_73`)
  * Defending Ask Wall: `11.95000` (`195815.8996` coins / `2,340,000.00 USD` on `Hyperliquid`, persistent for `2h 03m`, Traded: `0.0%`, Order ID: `CG_WHALE_LINK_T_17`)
  * Total Whale Armor Pool: Bids Pool=`23,003,400.00 USD` | Asks Pool=`23,887,100.00 USD` (Tracked Orders: `190`)
- **Hyperdash Resting Depth & L3 Telemetry (12_Hyperdash.parquet)**:
  * `NEUTRAL`: `0.00 USD` @ `0.00000` (Size: `0.0`, Detail: Delta: +0, Wallet: None, Timestamp: 2026-10-29 19:44:05 IST)
- **Hyperliquid Elite Trader Positioning (4_Hyperliquid_Analysis.parquet)**:
  * Wallet `0x73ce82fb75...` (0x73ce...8ce9): `Long` `4,668,935.40 USD` (400,011.6000 LINK, Margin: 933,787.08 USD, Leverage: 5X Cross, Entry: 12.0490 USD, Current: 11.6615 USD, Est Liq: 9.1293 USD, PnL: -150,818.31 USD [-3.23%], Fees: +300,120.04 USD)
  * Wallet `0x5b5d51203a...` (0x5b5d...c060): `Short` `3,638,491.55 USD` (311,728.2000 LINK, Margin: 1,212,830.52 USD, Leverage: 3X Cross, Entry: 13.6084 USD, Current: 11.6615 USD, Est Liq: 448.9085 USD, PnL: +603,640.56 USD [+16.59%], Fees: -45,066.39 USD)
  * Wallet `0xb83de012db...` (0xb83d...6e36): `Short` `3,596,750.14 USD` (308,152.0000 LINK, Margin: 1,198,916.71 USD, Leverage: 3X Cross, Entry: 12.9328 USD, Current: 11.6615 USD, Est Liq: 372.7559 USD, PnL: +388,503.35 USD [+10.80%], Fees: -55,134.90 USD)

---

## 6. Liquidation Max Pain, Heatmaps & Cascade Boundaries
*(Sources: 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 14_Hyperdash_Liq_Map.parquet, 14_Liquidation_Matrix.parquet, 15_Hyperdash_Stops_Map.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`11.80400` (Vol: `215,600 USD`, Dist: `+1.12%`) | Long MP=`11.18300` (Vol: `185,200 USD`, Dist: `-4.20%`)
  * 48H Horizon: Short MP=`12.05000` (Vol: `224,500 USD`, Dist: `+3.23%`) | Long MP=`11.27900` (Vol: `248,100 USD`, Dist: `-3.37%`)
  * 3D Horizon: Short MP=`12.21900` (Vol: `248,100 USD`, Dist: `+4.68%`) | Long MP=`11.15200` (Vol: `359,300 USD`, Dist: `-4.46%`)
  * 7D Horizon: Short MP=`12.22000` (Vol: `248,100 USD`, Dist: `+4.69%`) | Long MP=`11.15600` (Vol: `661,300 USD`, Dist: `-4.43%`)
- **Exchange Cumulative Liquidation Cascades (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
  * 1D Cascade: Total=`6.60M USD` | Short Liq Pool=`6.60M USD` | Long Liq Pool=`0 USD` | Venues: Binance=`7.49K USD`, OKX=`3.61K USD`, Bybit=`8.01K USD`
  * 7D Cascade: Total=`17.21M USD` | Short Liq Pool=`17.21M USD` | Long Liq Pool=`0 USD` | Venues: Binance=`41.14K USD`, OKX=`16.61K USD`, Bybit=`13.08K USD`
- **Cross-Venue Liquidation Matrix & Heatmaps (14_Liquidation_Matrix.parquet, 7_Liq_Heapmap.parquet)**:
  * Liquidation Matrix Strike: Price=`22.75000` | Vol=`910 USD` | Cumulative=`4,260,000 USD` | Venue=`Hyperliquid L1` | Side=`Short Liquidation`
  * Multi-Timeframe Heatmap Density: 1h=`0.00 USD` | 4h=`0.00 USD` | 12h=`0.00 USD` | 24h=`0.00 USD`
- **Hyperdash Real-Time Liquidation & Retail Stop Protection (14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet)**:
  * Hyperdash Liq Cluster: Mark=`11.6500 USD` | Cluster Price=`22.7500 USD` | Dist=`+95.28%` | Cumulative=`4.26M USD` | Short=`910.00 USD` | Long=`0 USD` | Size=`40.0000 LINK`
  * **Retail Stops Map (Pitfall 2 & 4 Defense)**:
    - `Sell Stop`: `3.5500 USD` (Dist: `-69.53%`, Cumulative Stops: `656.41K USD`, Buy: `0 USD`, Sell: `431.68 USD`, Coins: `121.6000 LINK`)
    - `Sell Stop`: `4.5500 USD` (Dist: `-60.94%`, Cumulative Stops: `655.98K USD`, Buy: `0 USD`, Sell: `290.29 USD`, Coins: `63.8000 LINK`)
    - `Sell Stop`: `5.2500 USD` (Dist: `-54.94%`, Cumulative Stops: `655.69K USD`, Buy: `0 USD`, Sell: `120.22 USD`, Coins: `22.9000 LINK`)
- **Live Forced Liquidation Momentum (7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)**:
  * Multi-Timeframe Forced Aggregates (5m): Long Liq=`0.00 USD` | Short Liq=`0.00 USD` | Total=`0.00 USD` | Net Delta=`0.00 USD` | Dominant=`BALANCED`

---

## 7. Derivatives Sentiment, Open Interest & Funding Dynamics
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet, 6_Funding_Fee_Settlement.parquet, 13_Hyperliquid.parquet)*
- **Aggregated Open Interest Breakdown (5_OI.parquet)**:
  * Total Open Interest: `556.59M USD` (`47,765,003.0 LINK`) | OI / 24h Volume Ratio: `1.1034`
  * OI Expansion Rate: 1h Change=`+0.23%` | 4h Change=`+1.81%` | 24h Change=`-0.76%`
  * Venue Concentration:
    - Binance: `106.18M USD` | Bybit: `65.91M USD` | OKX: `26.47M USD` | CME Institutional: `15.38M USD`
    - Gate: `90.63M USD` | MEXC: `39.49M USD` | Hyperliquid DEX: `56.35M USD` | Bitget: `46.49M USD`
    - KuCoin: `17.06M USD` | BingX: `17.66M USD` | Bitunix: `7.34M USD` | Others: `67.63M USD`
- **Cross-Exchange Perpetual Funding Rates (5_Funding_Rate.parquet)**:
  * Major CEX Rates: Binance=`+0.0100%` | OKX=`+0.0100%` | Bybit=`+0.0100%` | Bitget=`+0.0086%`
  * Mid-Tier CEX Rates: KuCoin=`+0.0100%` | MEXC=`+0.0100%` | Gate=`+0.0097%` | BingX=`+0.0100%` | Bitunix=`+0.0100%`
  * Alternative Venues: WhiteBIT=`+0.0100%` | LBank=`+0.0100%` | tradeXYZ=`-`
  * Inverse Coin-Margined: CoinM Binance=`+0.0100%` | CoinM OKX=`+0.0100%` | CoinM Bybit=`+0.0100%`
- **Exchange Long / Short Ratio Dynamics (3_Exchanges_LS_Ratio*.parquet)**:
  * 15m Tactical: L/S Ratio=`0.94` (Longs: `48.56%`, Shorts: `51.44%`, Total Vol: `3.95M USD`)
  * 1h Primary: L/S Ratio=`1.03` (Longs: `50.69%`, Shorts: `49.31%`, Total Vol: `54.52M USD`)
  * 4h Macro: L/S Ratio=`0.93` (Longs: `48.28%`, Shorts: `51.72%`, Total Vol: `88.69M USD`)
- **Funding Fee Settlement & DEX Arbitrage (6_Funding_Fee_Settlement.parquet, 13_Hyperliquid.parquet)**:
  * Settlement Payouts: Current Expected=`18.66K USD` | Last 24h=`39.23K USD` | Last 3D=`101.03K USD` | Last 7D=`149.67K USD`

---

## 8. Microstructure Footprint, Tape Imbalances & Macro Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 16_Hyperdash_telegram_Intel.parquet, 19_News.parquet, 19_Calendar.parquet)*
- **Bar-by-Bar Microstructure Footprint (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
  * Venue Source: `CoinGlass-AggregatedFutures(Binance)` | Timeframe: `15m` | Last Price: `11.66250`
  * Footprint Auction Profile: Bar VWAP=`11.65263` | Bar POC=`11.66250` | Bar VAH=`11.68050` | Bar VAL=`11.62650`
  * Orderflow Volumes: Total Vol=`895,782.28 USD` | Taker Buy=`489,905.36 USD` | Taker Sell=`405,876.92 USD`
  * Bar Delta Profile: Delta=`+84,028.43 USD` (`+9.38%`) | Max Delta=`+84,028.43 USD` | Min Delta=`-27,552.44 USD` | Cumulative Bar Delta=`+441,275.45 USD`
  * Order Execution Dynamics: Trades Count=`5,156` | Avg Trade Size=`173.74 USD`
  * Tape Imbalances: Imbalance Ratio=`300.0%` | Buy Imbalances Count=`13` | Sell Imbalances Count=`4`
  * Footprint Open Interest: Bar OI=`0.00 USD` | Bar OI Change=`+0.00 USD`
- **CoinGlass Algorithmic Footprint Signals (25_CoinGlass_Footprint_Signals.parquet)**:
  * Signal Classification: Type=`Exhaustion` | Bias: **`BEARISH`** | Signal Time=`10-28 07:47` | Timeframe=`Volume 250K LINK`
  * Signal Context: Headline=`Buyer exhaustion` | Price Level=`11.78100` | Absorbed Volume=`0.00 USD`
  * Bar Footprint Context: Current Bar Delta=`+0.00 USD` | Current Bar Volume=`0.00 USD` | Delta in View=`+0.00 USD`
  * Historical Detail: `New 10-bar high with almost no volume in the top 10% of the bar, closed in the lower half, bearish · 11.781` | KPI=`—` | Bias=`—`
- **Multi-Horizon Macro Capital Netflows (2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet)**:
  * Spot Capital Netflows:
    - Tactical: 5m=`+37.89K` | 15m=`+31.61K` | 30m=`-181.76K` | 1h=`-34.81K`
    - Intermediate: 2h=`-79.30K` | 4h=`+98.52K` | 6h=`-199.42K` | 8h=`-37.80K` | 12h=`+484.09K` | 24h=`-466.90`
    - Macro Horizons: 1-Week=`-10.17M` | 15-Day=`-26.27M` | 30-Day=`-75.60M` | Market Cap=`8.71B`
  * Futures Capital Netflows:
    - Tactical: 5m=`+43.70K` | 15m=`+211.23K` | 30m=`+203.60K` | 1h=`+116.52K`
    - Intermediate: 2h=`+221.28K` | 4h=`+165.37K` | 6h=`+447.77K` | 8h=`+1.01M` | 12h=`+64.19K` | 24h=`-2.37M`
    - Macro Horizons: 1-Week=`-29.15M` | 15-Day=`-44.16M` | 30-Day=`-191.94M` | Market Cap=`8.71B`
- **Telegram Intelligence Alert**: `[MARKET_INTEL] #LINK Whale SELL: 5.04K USD at 11.5520 USD [API] (Impact: NEWS_INTEL)`

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
- **Stand-Aside Reason**: Gate 1 Spread Friction Failure: Spread friction 74.60 bps exceeds cap 25.0 bps. Standing aside in 100% cash preserves statutory floor.