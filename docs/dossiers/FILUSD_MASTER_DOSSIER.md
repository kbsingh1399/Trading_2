# 🔬 MASTER 43-FEED QUANTITATIVE DOSSIER: FILUSD (Filecoin / USD)
**MT5 Symbol**: `FILUSD.p` | **Category**: `Crypto Altcoin` | **Tier**: `Tier 2`
**Execution Posture**: `DISQUALIFIED` | **Timestamp**: 2026-10-29 14:43:14 UTC
**Pipeline Clearance**: `BLOCKED` | **Data Freshness**: `1.2m`

---

## 1. MT5 Live Broker Telemetry & Spread Friction Gate
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet)*
- **Live Bid Quote**: `0.89200` | **Live Ask Quote**: `0.93200` | **Mid Price**: `0.91200`
- **Spread Points**: `40.0 pts` | **Spread BPS**: `438.60 bps` (Mandatory Cap: `25.0 bps`)
- **Gate Status**: **`FAIL`** (Spread friction 438.60 bps exceeds cap 25.0 bps)
- **Order Allowed**: `NONE` | **Pillar 1 Clearance**: `BLOCKED`
- **Broker Specifications**: Contract Size=`1.00` | Tick Value=`1.00 USD` | Min Lot=`0.01` | Digits=`5`
- **Account Capital Context**: Balance=`4,744.55 USD` | Equity=`4,744.32 USD` | Free Margin=`4,342.62 USD` | Inviolate Hard Floor=`4,775.00 USD` (Cushion: `-30.68 USD`)
- **Pipeline Health**: Feed #00 Status=`PASS` | Overall Pipeline Telemetry=`33/33 FEEDS PASS (SYNCHRONIZED)`

---

## 2. Technical Profile, Multi-Sigma VWAP Dispersion & Volatility
*(Sources: 11_Technical.parquet, 11_Technical_BTC_Ribbon.parquet)*
- **Last Verified Price**: `0.89000` | **24h Change**: `+3.37%` (24h High: `0.91400`, 24h Low: `0.84500`)
- **Weekly Range**: Week High=`0.91400` | Week Low=`0.84500` | Daily POC=`0.89300` | Daily VAH=`0.90200` | Daily VAL=`0.86000`
- **Session VWAP**: `0.87055` | **Rolling 24h VWAP**: `0.87752` | **Distance to VWAP**: `+2.23%`
- **VWAP Z-Score**: `+1.26 sigma` | **Mean Reversion Bias**: **`FAIR VALUE`**
- **VWAP Dispersion Bands**:
  * +1.00 sigma: `0.88603` | -1.00 sigma: `0.85508`
  * +1.28 sigma (80% CI): `0.89037` | -1.28 sigma: `0.85074`
  * +2.00 sigma (95% CI): `0.90151` | -2.00 sigma: `0.83960`
  * +2.01 sigma: `0.90166` | -2.01 sigma: `0.83944`
  * +2.51 sigma (98.8% CI): `0.90940` | -2.51 sigma: `0.83170`
  * +3.00 sigma (99.7% CI Extreme): `0.91699` | -3.00 sigma: `0.82412`
- **Oscillators & Volatility**:
  * **RSI (14)**: `64.72` | **RSI State**: **`BULLISH`**
  * **ATR (14)**: `0.00581` | **ATR %**: `0.65%`
  * **Bollinger Bands**: Upper=`0.89860` | Mid=`0.88275` | Lower=`0.86690` | Bandwidth=`3.59%`
  * **MACD**: Line=`+0.0066` | Signal=`+0.0062` | Hist=`+0.0004`
- **Exponential Moving Average Ribbon (EMA)**:
  * Short Horizon: EMA-5=`0.88996` | EMA-9=`0.88848` | EMA-13=`0.88636` | EMA-20=`0.88271`
  * Intermediate: EMA-34=`0.87830` | EMA-50=`0.87656` | EMA-89=`0.87663` | EMA-100=`0.87693`
  * Institutional: EMA-144=`0.87817` | EMA-200=`0.87884` (Slope: `+0.137%`) | EMA-233=`0.87970` (Slope: `+0.105%`)
  * **Trend Bias**: **`BULLISH`**

---

## 3. Auction Market Structure & Value Profile
*(Sources: 20_Auction_Market_Structure.parquet)*
- **Daily Auction Value Area**:
  * High (VAH): `0.90200` | Point of Control (POC): `0.89300` | Low (VAL): `0.86000`
  * Distance to POC: `+2.14%` | Distance to VAH: `+1.06%` | Distance to VAL: `+6.11%`
  * **Value Area Position**: **`ABOVE_VALUE (Imbalance)`** | **Auction Regime**: **`RANGE_EXPANSION`** | **Session Bias**: **`BULLISH (Above Pivot)`**
- **Prior Day & Weekly Auction Profile**:
  * Prior Day: PD VAH=`0.90100` | PD POC=`0.89200` | PD VAL=`0.87400` | PDH=`0.91400` | PDL=`0.85700` | PDC=`0.90100`
  * Monday Reference: Monday High=`0.91200` | Monday Low=`0.87800` | Monday Mid=`0.89500`
  * Weekly Value Area: Weekly VAH=`0.90000` | Weekly POC=`0.89400` | Weekly VAL=`0.87300`
  * Multi-Week Extremes: Current Week High (CWH)=`0.91400` | CWL=`0.84500` | Prior Week High (PWH)=`1.07200` | PWL=`0.88600`
  * Multi-Month Extremes: Current Month High (CMH)=`1.25600` | CML=`0.84500` | Prior Month High (PMH)=`1.20800` | PML=`0.65200`
- **Session Liquidity Extremes & Initial Balance**:
  * Asian Session: Range `[0.84700 - 0.91000]`
  * London Session: Range `[0.84500 - 0.89500]`
  * New York Session: Range `[0.86900 - 0.89500]`
  * Initial Balance (IB): IB High=`0.87200` | IB Low=`0.85500`
- **Fibonacci Golden Pocket & Optimal Trade Entry (OTE)**:
  * Swing Range: High=`0.91400` | Low=`0.84500` | Direction=`BEARISH_IMPULSE`
  * Golden Pocket [0.618 - 0.65]: `[0.88800 - 0.89000]`
  * Optimal Trade Entry (0.702): `0.89300` | Invalidation Level: `0.89900` | Status: **`STRUCTURE_INVALIDATED`**
- **Classical & Weekly Pivots**:
  * Daily Classical: Pivot=`0.89100` | R1=`0.92400` | S1=`0.86700` | R2=`0.94800` | S2=`0.83400`
  * Weekly Classical: Weekly Pivot=`0.95500` | Weekly R1=`1.02300` | Weekly S1=`0.83700`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Orderflow
*(Sources: 18_CVD.parquet, 18_CVD_30D_5m.parquet, 18_CVD_30D_15m.parquet, 18_CVD_30D_1h.parquet, 18_CVD_30D_4h.parquet, 18_CVD_30D_ALL.parquet, 21_Tradfye_Orderflow.parquet)*
- **Interbank Spot Orderflow Mechanics**: Decentralized OTC market structure. CVD taker deltas do not apply to interbank spot flow. Tape volume governed by broker tick volume with live spread friction of `438.60 bps`.
- **Session Volume Structure**: Price operating at `ABOVE_VALUE (Imbalance)` with Daily POC at `0.89300` (VAH: `0.90200` / VAL: `0.86000`).

---

## 5. Institutional Whale Armor & Resting Orderbook Depth
*(Sources: 10_Whale_Orders.parquet, 12_Hyperdash.parquet, 17_Orderbook.parquet, 4_Hyperliquid_Analysis.parquet)*
- **Defending Resting Whale Walls (10_Whale_Orders.parquet)**:
  * Defending Bid Wall: `0.00000` (`0.0000` coins / `0.00 USD` on `-`, persistent for `-`, Traded: `0.0%`, Order ID: `-`)
  * Defending Ask Wall: `0.00000` (`0.0000` coins / `0.00 USD` on `-`, persistent for `-`, Traded: `0.0%`, Order ID: `-`)
  * Total Whale Armor Pool: Bids Pool=`0.00 USD` | Asks Pool=`0.00 USD` (Tracked Orders: `0`)
- **Hyperdash Resting Depth & L3 Telemetry (12_Hyperdash.parquet)**:
  * `NEUTRAL`: `0.00 USD` @ `0.00000` (Size: `0.0`, Detail: Delta: +0, Wallet: None, Timestamp: 2026-10-29 19:44:05 IST)
- **Hyperliquid Elite Trader Positioning (4_Hyperliquid_Analysis.parquet)**:
  * Wallet `0xeadc152ac1...` (0xeadc...9d55): `Long` `1,821,040.00 USD` (2,000,000.0000 FIL, Margin: 364,208.00 USD, Leverage: 5X Cross, Entry: 0.982400 USD, Current: 0.910500 USD, Est Liq: 0.00 USD, PnL: -143,726.39 USD [-7.89%], Fees: +24,047.61 USD)

---

## 6. Liquidation Max Pain, Heatmaps & Cascade Boundaries
*(Sources: 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 14_Hyperdash_Liq_Map.parquet, 14_Liquidation_Matrix.parquet, 15_Hyperdash_Stops_Map.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`0.91992` (Vol: `164,828 USD`, Dist: `+2.24%`) | Long MP=`0.87312` (Vol: `103,313 USD`, Dist: `-2.97%`)
  * 48H Horizon: Short MP=`0.93553` (Vol: `183,913 USD`, Dist: `+3.97%`) | Long MP=`0.87316` (Vol: `123,659 USD`, Dist: `-2.96%`)
  * 3D Horizon: Short MP=`0.93412` (Vol: `290,792 USD`, Dist: `+3.81%`) | Long MP=`0.87822` (Vol: `163,060 USD`, Dist: `-2.40%`)
  * 7D Horizon: Short MP=`1.02220` (Vol: `374,142 USD`, Dist: `+14.12%`) | Long MP=`0.87932` (Vol: `266,421 USD`, Dist: `-1.83%`)
- **Exchange Cumulative Liquidation Cascades (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
  * 1D Cascade: Total=`0.00 USD` | Short Liq Pool=`0.00 USD` | Long Liq Pool=`0.00 USD` | Venues: Binance=`0.00 USD`, OKX=`0.00 USD`, Bybit=`0.00 USD`
  * 7D Cascade: Total=`0.00 USD` | Short Liq Pool=`0.00 USD` | Long Liq Pool=`0.00 USD` | Venues: Binance=`0.00 USD`, OKX=`0.00 USD`, Bybit=`0.00 USD`
- **Cross-Venue Liquidation Matrix & Heatmaps (14_Liquidation_Matrix.parquet, 7_Liq_Heapmap.parquet)**:
  * Liquidation Matrix Strike: Price=`0.00000` | Vol=`0 USD` | Cumulative=`0 USD` | Venue=`-` | Side=`-`
  * Multi-Timeframe Heatmap Density: 1h=`0.00 USD` | 4h=`0.00 USD` | 12h=`324.36K USD` | 24h=`0.00 USD`
- **Hyperdash Real-Time Liquidation & Retail Stop Protection (14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet)**:
  * Hyperdash Liq Cluster: Mark=`0.910350 USD` | Cluster Price=`1.7965 USD` | Dist=`+97.34%` | Cumulative=`18.48K USD` | Short=`661.47 USD` | Long=`0 USD` | Size=`368.2000 FIL`
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
  * Major CEX Rates: Binance=`+0.0095%` | OKX=`+0.0018%` | Bybit=`+0.0100%` | Bitget=`+0.0100%`
  * Mid-Tier CEX Rates: KuCoin=`+0.0100%` | MEXC=`+0.0000%` | Gate=`-0.0037%` | BingX=`+0.0100%` | Bitunix=`+0.0093%`
  * Alternative Venues: WhiteBIT=`+0.0100%` | LBank=`+0.0092%` | tradeXYZ=`-`
  * Inverse Coin-Margined: CoinM Binance=`+0.0100%` | CoinM OKX=`+0.0100%` | CoinM Bybit=`+0.0100%`
- **Exchange Long / Short Ratio Dynamics (3_Exchanges_LS_Ratio*.parquet)**:
  * 15m Tactical: L/S Ratio=`1.00` (Longs: `50.00%`, Shorts: `50.00%`, Total Vol: `0.00 USD`)
  * 1h Primary: L/S Ratio=`1.00` (Longs: `50.00%`, Shorts: `50.00%`, Total Vol: `0.00 USD`)
  * 4h Macro: L/S Ratio=`1.00` (Longs: `50.00%`, Shorts: `50.00%`, Total Vol: `0.00 USD`)
- **Funding Fee Settlement & DEX Arbitrage (6_Funding_Fee_Settlement.parquet, 13_Hyperliquid.parquet)**:
  * Settlement Payouts: Current Expected=`7.66K USD` | Last 24h=`-5.96K USD` | Last 3D=`13.02K USD` | Last 7D=`-32.57K USD`

---

## 8. Microstructure Footprint, Tape Imbalances & Macro Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 16_Hyperdash_telegram_Intel.parquet, 19_News.parquet, 19_Calendar.parquet)*
- **Bar-by-Bar Microstructure Footprint (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
  * Venue Source: `Aggregated` | Timeframe: `15m` | Last Price: `0.91200`
  * Footprint Auction Profile: Bar VWAP=`0.91200` | Bar POC=`0.91200` | Bar VAH=`0.91382` | Bar VAL=`0.91018`
  * Orderflow Volumes: Total Vol=`0.00 USD` | Taker Buy=`0.00 USD` | Taker Sell=`0.00 USD`
  * Bar Delta Profile: Delta=`+0.00 USD` (`+0.00%`) | Max Delta=`+0.00 USD` | Min Delta=`+0.00 USD` | Cumulative Bar Delta=`+0.00 USD`
  * Order Execution Dynamics: Trades Count=`0` | Avg Trade Size=`0.00 USD`
  * Tape Imbalances: Imbalance Ratio=`0.0%` | Buy Imbalances Count=`0` | Sell Imbalances Count=`0`
  * Footprint Open Interest: Bar OI=`0.00 USD` | Bar OI Change=`+0.00 USD`
- **Multi-Horizon Macro Capital Netflows (2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet)**:
  * Spot Capital Netflows:
    - Tactical: 5m=`+10.00K` | 15m=`-14.52K` | 30m=`-8.54K` | 1h=`-42.27K`
    - Intermediate: 2h=`+13.03K` | 4h=`-186.86K` | 6h=`+33.79K` | 8h=`-418.95K` | 12h=`-763.63K` | 24h=`-1.28M`
    - Macro Horizons: 1-Week=`-11.20M` | 15-Day=`-27.27M` | 30-Day=`-51.42M` | Market Cap=`762.80M`
  * Futures Capital Netflows:
    - Tactical: 5m=`-103.87K` | 15m=`-68.27K` | 30m=`-760.21K` | 1h=`-812.18K`
    - Intermediate: 2h=`-96.05K` | 4h=`-1.07M` | 6h=`+850.29K` | 8h=`-200.20K` | 12h=`-756.46K` | 24h=`-2.81M`
    - Macro Horizons: 1-Week=`-45.93M` | 15-Day=`-127.62M` | 30-Day=`-299.74M` | Market Cap=`762.80M`

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
- **Stand-Aside Reason**: Gate 1 Spread Friction Failure: Spread friction 438.60 bps exceeds cap 25.0 bps. Standing aside in 100% cash preserves statutory floor.