# 🔬 MASTER 43-FEED QUANTITATIVE DOSSIER: SUI (Sui)
**MT5 Symbol**: `SUIUSD.p` | **Category**: `Crypto Alt L1` | **Tier**: `Tier 1`
**Execution Posture**: `PASSIVE_MAKER_LIMIT_ONLY` | **Timestamp**: 2026-10-29 14:43:14 UTC
**Pipeline Clearance**: `DISQUALIFIED` | **Data Freshness**: `1.2m`

---

## 1. MT5 Live Broker Telemetry & Spread Friction Gate
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet)*
- **Live Bid Quote**: `0.91000` | **Live Ask Quote**: `0.91000` | **Mid Price**: `0.91000`
- **Spread Points**: `0.0 pts` | **Spread BPS**: `999.00 bps` (Mandatory Cap: `25.0 bps`)
- **Gate Status**: **`FAIL`** (UNLISTED_ON_MT5_BROKER (Zero broker telemetry stream))
- **Order Allowed**: `BUY_LIMIT / SELL_LIMIT` | **Pillar 1 Clearance**: `DISQUALIFIED`
- **Broker Specifications**: Contract Size=`1.00` | Tick Value=`1.00 USD` | Min Lot=`0.01` | Digits=`5`
- **Account Capital Context**: Balance=`4,744.55 USD` | Equity=`4,744.32 USD` | Free Margin=`4,342.62 USD` | Inviolate Hard Floor=`4,775.00 USD` (Cushion: `-30.68 USD`)
- **Pipeline Health**: Feed #00 Status=`PASS` | Overall Pipeline Telemetry=`33/33 FEEDS PASS (SYNCHRONIZED)`

---

## 2. Technical Profile, Multi-Sigma VWAP Dispersion & Volatility
*(Sources: 11_Technical.parquet, 11_Technical_BTC_Ribbon.parquet)*
- **Live Quote Baseline**: Last Mid Price=`0.91000` | Spread=`999.00 bps` (0.0 pts)
- **Empirical Status**: Asset indicator stream unindexed in 11_Technical collector snapshot. Mathematical indicators reference live MT5 Bid/Ask quotes and session auction structures.

---

## 3. Auction Market Structure & Value Profile
*(Sources: 20_Auction_Market_Structure.parquet)*
- **Daily Auction Value Area**:
  * High (VAH): `0.91273` | Point of Control (POC): `0.91000` | Low (VAL): `0.90727`
  * Distance to POC: `+0.00%` | Distance to VAH: `+0.00%` | Distance to VAL: `+0.00%`
  * **Value Area Position**: **`INSIDE_VALUE (Balance)`** | **Auction Regime**: **`BALANCED_AUCTION`** | **Session Bias**: **`NEUTRAL`**
- **Prior Day & Weekly Auction Profile**:
  * Prior Day: PD VAH=`0.91364` | PD POC=`0.91000` | PD VAL=`0.90636` | PDH=`0.91546` | PDL=`0.90454` | PDC=`0.91000`
  * Monday Reference: Monday High=`0.91455` | Monday Low=`0.90545` | Monday Mid=`0.91000`
  * Weekly Value Area: Weekly VAH=`0.91728` | Weekly POC=`0.91000` | Weekly VAL=`0.90272`
  * Multi-Week Extremes: Current Week High (CWH)=`0.91910` | CWL=`0.90090` | Prior Week High (PWH)=`0.92365` | PWL=`0.89635`
  * Multi-Month Extremes: Current Month High (CMH)=`0.92820` | CML=`0.89180` | Prior Month High (PMH)=`0.93275` | PML=`0.88725`
- **Session Liquidity Extremes & Initial Balance**:
  * Asian Session: Range `[0.90818 - 0.91182]`
  * London Session: Range `[0.90636 - 0.91364]`
  * New York Session: Range `[0.90545 - 0.91455]`
  * Initial Balance (IB): IB High=`0.91273` | IB Low=`0.90727`
- **Fibonacci Golden Pocket & Optimal Trade Entry (OTE)**:
  * Swing Range: High=`0.91910` | Low=`0.90090` | Direction=`NONE`
  * Golden Pocket [0.618 - 0.65]: `[0.90818 - 0.91182]`
  * Optimal Trade Entry (0.702): `0.91000` | Invalidation Level: `0.00000` | Status: **`NONE`**
- **Classical & Weekly Pivots**:
  * Daily Classical: Pivot=`0.91000` | R1=`0.91273` | S1=`0.90727` | R2=`0.91546` | S2=`0.90454`
  * Weekly Classical: Weekly Pivot=`0.91000` | Weekly R1=`0.91910` | Weekly S1=`0.90090`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Orderflow
*(Sources: 18_CVD.parquet, 18_CVD_30D_5m.parquet, 18_CVD_30D_15m.parquet, 18_CVD_30D_1h.parquet, 18_CVD_30D_4h.parquet, 18_CVD_30D_ALL.parquet, 21_Tradfye_Orderflow.parquet)*
- **Primary 15m CVD Microstructure (18_CVD_30D_15m.parquet)**:
  * Candle Delta: `+189,671.04 USD` (Base: `+203,296.7000 coins`) | Delta %: `+8.21%`
  * Taker Volumes: Taker Buy=`1,249,940.45 USD` | Taker Sell=`1,060,269.41 USD` | Total Vol=`2,478,261.10 USD`
  * Cumulative CVD: `-6,549,766.27 USD` (Base: `-7,161,768.5000`)
  * Rolling CVD Z-Score: `+0.25 sigma` | Price Return: `+0.41%`
  * **Delta Regime**: **`DELTA ALIGNED`** | Trades Count: `10,443`
- **Multi-Timeframe Delta Comparison**:
  * 5m Bar: Delta=`+258,747.57 USD` | Delta %=`+47.71%` | Z-Score=`+0.76` | Regime=`AGGRESSIVE BUYING`
  * 1h Bar: Delta=`+189,671.04 USD` | Delta %=`+8.21%` | Z-Score=`+0.45` | Regime=`DELTA ALIGNED`
  * 4h Bar: Delta=`+1,169,612.89 USD` | Delta %=`+5.12%` | Z-Score=`+0.50` | Regime=`DELTA ALIGNED`
  * 30D Consolidated (ALL): Cumulative Trend=`-4,861,631.06 USD` | Long-Term Regime=`DELTA ALIGNED`
- **Institutional Footprint & Deribit Options Armor (21_Tradfye_Orderflow.parquet)**:
  * Candle VWAP: `0.90685` | Estimated POC: `0.90760` | Avg Trade Size: `273.00 USD`
  * Net Delta USD: `+137,956.25 USD` | Net Delta %: `+8.20%` | Orderflow CVD: `+137,956.25 USD`
  * Orderflow Regime: **`TWO_SIDED_ABSORPTION`** | Orderflow Divergence: **`BULLISH_EXPANSION`**
  * Deribit Options Walls: Max Pain=`0.00` | Call Wall=`0.00` | Put Wall=`0.00`

---

## 5. Institutional Whale Armor & Resting Orderbook Depth
*(Sources: 10_Whale_Orders.parquet, 12_Hyperdash.parquet, 17_Orderbook.parquet, 4_Hyperliquid_Analysis.parquet)*
- **Defending Resting Whale Walls (10_Whale_Orders.parquet)**:
  * Defending Bid Wall: `0.00000` (`0.0000` coins / `0.00 USD` on `-`, persistent for `-`, Traded: `0.0%`, Order ID: `-`)
  * Defending Ask Wall: `0.95080` (`1765890.6000` coins / `1,679,008.78 USD` on `MT5-Crypto`, persistent for `Resting Book`, Traded: `0.0%`, Order ID: `MT5_SUI_SELL_0`)
  * Total Whale Armor Pool: Bids Pool=`0.00 USD` | Asks Pool=`6,385,741.46 USD` (Tracked Orders: `19`)
- **Hyperdash Resting Depth & L3 Telemetry (12_Hyperdash.parquet)**:
  * `NEUTRAL`: `0.00 USD` @ `0.00000` (Size: `0.0`, Detail: Delta: +0, Wallet: None, Timestamp: 2026-10-29 19:44:05 IST)
- **Consolidated L2 Orderbook Depth & Skew (17_Orderbook.parquet)**:
  * `ASK`: `1,178.59 USD` @ `0.9345 USD` (Coins: 1,261.2000 SUI, Cumulative: 35,060.66 USD, Tier: 1 orders, Dist: +0.05%, Bias: B/A: 64.0% / 36.0%)
  * `ASK`: `1,178.57 USD` @ `0.9345 USD` (Coins: 1,261.2000 SUI, Cumulative: 33,882.07 USD, Tier: 1 orders, Dist: +0.05%, Bias: B/A: 64.0% / 36.0%)
  * `ASK`: `1,999.95 USD` @ `0.9345 USD` (Coins: 2,140.2000 SUI, Cumulative: 32,703.50 USD, Tier: 1 orders, Dist: +0.05%, Bias: B/A: 64.0% / 36.0%)
- **Hyperliquid Elite Trader Positioning (4_Hyperliquid_Analysis.parquet)**:
  * Wallet `0xb83de012db...` (0xb83d...6e36): `Short` `3,564,081.96 USD` (3,817,609.4000 SUI, Margin: 1,188,027.32 USD, Leverage: 3X Cross, Entry: 1.1051 USD, Current: 0.932740 USD, Est Liq: 30.0802 USD, PnL: +654,653.36 USD [+18.37%], Fees: -50,093.80 USD)
  * Wallet `0xa2ce501d9c...` (0xa2ce...3126): `Long` `2,333,784.71 USD` (2,500,010.4000 SUI, Margin: 233,378.47 USD, Leverage: 10X Cross, Entry: 0.859700 USD, Current: 0.932740 USD, Est Liq: 0.00 USD, PnL: +184,578.18 USD [+7.91%], Fees: +107,909.51 USD)
  * Wallet `0x9946e6adf9...` (0x9946...0852): `Short` `1,515,021.62 USD` (1,622,322.0000 SUI, Margin: 151,502.16 USD, Leverage: 10X Cross, Entry: 1.0826 USD, Current: 0.932740 USD, Est Liq: 1.5823 USD, PnL: +241,309.20 USD [+15.93%], Fees: -5,702.79 USD)

---

## 6. Liquidation Max Pain, Heatmaps & Cascade Boundaries
*(Sources: 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 14_Hyperdash_Liq_Map.parquet, 14_Liquidation_Matrix.parquet, 15_Hyperdash_Stops_Map.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`0.94360` (Vol: `402,000 USD`, Dist: `+0.94%`) | Long MP=`0.88870` (Vol: `546,500 USD`, Dist: `-4.93%`)
  * 48H Horizon: Short MP=`0.94360` (Vol: `402,000 USD`, Dist: `+0.94%`) | Long MP=`0.88870` (Vol: `650,000 USD`, Dist: `-4.93%`)
  * 3D Horizon: Short MP=`0.94360` (Vol: `402,000 USD`, Dist: `+0.94%`) | Long MP=`0.88870` (Vol: `820,500 USD`, Dist: `-4.93%`)
  * 7D Horizon: Short MP=`0.94302` (Vol: `467,400 USD`, Dist: `+0.88%`) | Long MP=`0.88896` (Vol: `1,100,000 USD`, Dist: `-4.90%`)
- **Exchange Cumulative Liquidation Cascades (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
  * 1D Cascade: Total=`11.39M USD` | Short Liq Pool=`11.39M USD` | Long Liq Pool=`0 USD` | Venues: Binance=`4.46K USD`, OKX=`5.18K USD`, Bybit=`0 USD`
  * 7D Cascade: Total=`32.55M USD` | Short Liq Pool=`32.55M USD` | Long Liq Pool=`0 USD` | Venues: Binance=`47.67K USD`, OKX=`11.52K USD`, Bybit=`30.72K USD`
- **Cross-Venue Liquidation Matrix & Heatmaps (14_Liquidation_Matrix.parquet, 7_Liq_Heapmap.parquet)**:
  * Liquidation Matrix Strike: Price=`1.85350` | Vol=`190 USD` | Cumulative=`3,930,000 USD` | Venue=`Hyperliquid L1` | Side=`Short Liquidation`
  * Multi-Timeframe Heatmap Density: 1h=`0.00 USD` | 4h=`0.00 USD` | 12h=`470.07K USD` | 24h=`1.40M USD`
- **Hyperdash Real-Time Liquidation & Retail Stop Protection (14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet)**:
  * Hyperdash Liq Cluster: Mark=`0.931750 USD` | Cluster Price=`1.8535 USD` | Dist=`+98.93%` | Cumulative=`3.93M USD` | Short=`190.35 USD` | Long=`0 USD` | Size=`102.7000 SUI`
  * **Retail Stops Map (Pitfall 2 & 4 Defense)**:
    - `Sell Stop`: `0.070500 USD` (Dist: `-92.43%`, Cumulative Stops: `1.65M USD`, Buy: `0 USD`, Sell: `165.53 USD`, Coins: `2,348.0000 SUI`)
    - `Sell Stop`: `0.075500 USD` (Dist: `-91.90%`, Cumulative Stops: `1.65M USD`, Buy: `0 USD`, Sell: `294.53 USD`, Coins: `3,901.1000 SUI`)
    - `Sell Stop`: `0.082500 USD` (Dist: `-91.15%`, Cumulative Stops: `1.65M USD`, Buy: `0 USD`, Sell: `1.59K USD`, Coins: `19,310.7000 SUI`)
- **Live Forced Liquidation Momentum (7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)**:
  * Multi-Timeframe Forced Aggregates (5m): Long Liq=`0.00 USD` | Short Liq=`0.00 USD` | Total=`0.00 USD` | Net Delta=`0.00 USD` | Dominant=`BALANCED`

---

## 7. Derivatives Sentiment, Open Interest & Funding Dynamics
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet, 6_Funding_Fee_Settlement.parquet, 13_Hyperliquid.parquet)*
- **Aggregated Open Interest Breakdown (5_OI.parquet)**:
  * Total Open Interest: `629.76M USD` (`675,951,467.8 SUI`) | OI / 24h Volume Ratio: `0.9361`
  * OI Expansion Rate: 1h Change=`+0.60%` | 4h Change=`+1.64%` | 24h Change=`+1.54%`
  * Venue Concentration:
    - Binance: `120.40M USD` | Bybit: `83.94M USD` | OKX: `34.91M USD` | CME Institutional: `0.00 USD`
    - Gate: `112.17M USD` | MEXC: `87.08M USD` | Hyperliquid DEX: `32.14M USD` | Bitget: `56.11M USD`
    - KuCoin: `38.75M USD` | BingX: `19.55M USD` | Bitunix: `6.98M USD` | Others: `37.73M USD`
- **Cross-Exchange Perpetual Funding Rates (5_Funding_Rate.parquet)**:
  * Major CEX Rates: Binance=`+0.0076%` | OKX=`+0.0080%` | Bybit=`-0.0048%` | Bitget=`+0.0078%`
  * Mid-Tier CEX Rates: KuCoin=`+0.0100%` | MEXC=`+0.0075%` | Gate=`+0.0060%` | BingX=`+0.0081%` | Bitunix=`+0.0033%`
  * Alternative Venues: WhiteBIT=`+0.0100%` | LBank=`+0.0074%` | tradeXYZ=`-`
  * Inverse Coin-Margined: CoinM Binance=`+0.0100%` | CoinM OKX=`+0.0100%` | CoinM Bybit=`+0.0100%`
- **Exchange Long / Short Ratio Dynamics (3_Exchanges_LS_Ratio*.parquet)**:
  * 15m Tactical: L/S Ratio=`0.94` (Longs: `48.56%`, Shorts: `51.44%`, Total Vol: `3.95M USD`)
  * 1h Primary: L/S Ratio=`0.92` (Longs: `47.81%`, Shorts: `52.19%`, Total Vol: `26.33M USD`)
  * 4h Macro: L/S Ratio=`0.93` (Longs: `48.28%`, Shorts: `51.72%`, Total Vol: `88.69M USD`)
- **Funding Fee Settlement & DEX Arbitrage (6_Funding_Fee_Settlement.parquet, 13_Hyperliquid.parquet)**:
  * Settlement Payouts: Current Expected=`6.82K USD` | Last 24h=`8.36K USD` | Last 3D=`78.39K USD` | Last 7D=`138.14K USD`

---

## 8. Microstructure Footprint, Tape Imbalances & Macro Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 16_Hyperdash_telegram_Intel.parquet, 19_News.parquet, 19_Calendar.parquet)*
- **Bar-by-Bar Microstructure Footprint (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
  * Venue Source: `CoinGlass-AggregatedFutures(Binance)` | Timeframe: `15m` | Last Price: `0.91000`
  * Footprint Auction Profile: Bar VWAP=`0.93193` | Bar POC=`0.93345` | Bar VAH=`0.93415` | Bar VAL=`0.92975`
  * Orderflow Volumes: Total Vol=`1,869,478.89 USD` | Taker Buy=`918,311.50 USD` | Taker Sell=`951,167.39 USD`
  * Bar Delta Profile: Delta=`-32,855.88 USD` (`-1.76%`) | Max Delta=`+103,702.02 USD` | Min Delta=`-53,181.14 USD` | Cumulative Bar Delta=`+914,121.51 USD`
  * Order Execution Dynamics: Trades Count=`8,328` | Avg Trade Size=`224.48 USD`
  * Tape Imbalances: Imbalance Ratio=`300.0%` | Buy Imbalances Count=`8` | Sell Imbalances Count=`5`
  * Footprint Open Interest: Bar OI=`0.00 USD` | Bar OI Change=`+0.00 USD`
- **CoinGlass Algorithmic Footprint Signals (25_CoinGlass_Footprint_Signals.parquet)**:
  * Signal Classification: Type=`Exhaustion` | Bias: **`BEARISH`** | Signal Time=`10-28 06:51` | Timeframe=`Range 0.0025`
  * Signal Context: Headline=`Buyer exhaustion` | Price Level=`0.93480` | Absorbed Volume=`0.00 USD`
  * Bar Footprint Context: Current Bar Delta=`+0.00 USD` | Current Bar Volume=`0.00 USD` | Delta in View=`+0.00 USD`
  * Historical Detail: `New 10-bar high with almost no volume in the top 10% of the bar, closed in the lower half, bearish · 0.93480` | KPI=`—` | Bias=`—`
- **Multi-Horizon Macro Capital Netflows (2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet)**:
  * Spot Capital Netflows:
    - Tactical: 5m=`-5.18K` | 15m=`+165.13K` | 30m=`-53.53K` | 1h=`-304.49K`
    - Intermediate: 2h=`+24.74K` | 4h=`+36.60K` | 6h=`-63.81K` | 8h=`+505.38K` | 12h=`-457.99K` | 24h=`+1.84M`
    - Macro Horizons: 1-Week=`-21.54M` | 15-Day=`-55.02M` | 30-Day=`-149.63M` | Market Cap=`3.84B`
  * Futures Capital Netflows:
    - Tactical: 5m=`+404.18K` | 15m=`+547.52K` | 30m=`+859.03K` | 1h=`+928.31K`
    - Intermediate: 2h=`+1.81M` | 4h=`+205.93K` | 6h=`+722.15K` | 8h=`-146.45K` | 12h=`-1.58M` | 24h=`-8.58M`
    - Macro Horizons: 1-Week=`-61.22M` | 15-Day=`-120.95M` | 30-Day=`-472.93M` | Market Cap=`3.84B`
- **Telegram Intelligence Alert**: `[MARKET_INTEL] #SUI Whale SELL: 7.76K USD at 0.9310 USD [API] (Impact: NEWS_INTEL)`

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