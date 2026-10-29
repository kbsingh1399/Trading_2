# 🔬 MASTER 43-FEED QUANTITATIVE DOSSIER: ADA (Cardano)
**MT5 Symbol**: `ADAUSD.p` | **Category**: `Crypto Alt L1` | **Tier**: `Tier 1`
**Execution Posture**: `DISQUALIFIED` | **Timestamp**: 2026-10-29 14:43:14 UTC
**Pipeline Clearance**: `BLOCKED` | **Data Freshness**: `1.2m`

---

## 1. MT5 Live Broker Telemetry & Spread Friction Gate
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet)*
- **Live Bid Quote**: `0.20070` | **Live Ask Quote**: `0.20280` | **Mid Price**: `0.20175`
- **Spread Points**: `21.0 pts` | **Spread BPS**: `104.09 bps` (Mandatory Cap: `25.0 bps`)
- **Gate Status**: **`FAIL`** (Spread friction 104.09 bps exceeds cap 25.0 bps)
- **Order Allowed**: `NONE` | **Pillar 1 Clearance**: `BLOCKED`
- **Broker Specifications**: Contract Size=`1.00` | Tick Value=`1.00 USD` | Min Lot=`0.01` | Digits=`5`
- **Account Capital Context**: Balance=`4,744.55 USD` | Equity=`4,744.32 USD` | Free Margin=`4,342.62 USD` | Inviolate Hard Floor=`4,775.00 USD` (Cushion: `-30.68 USD`)
- **Pipeline Health**: Feed #00 Status=`PASS` | Overall Pipeline Telemetry=`33/33 FEEDS PASS (SYNCHRONIZED)`

---

## 2. Technical Profile, Multi-Sigma VWAP Dispersion & Volatility
*(Sources: 11_Technical.parquet, 11_Technical_BTC_Ribbon.parquet)*
- **Last Verified Price**: `0.20060` | **24h Change**: `-0.05%` (24h High: `0.20860`, 24h Low: `0.19440`)
- **Weekly Range**: Week High=`0.20860` | Week Low=`0.19440` | Daily POC=`0.19690` | Daily VAH=`0.20050` | Daily VAL=`0.19530`
- **Session VWAP**: `0.19840` | **Rolling 24h VWAP**: `0.20051` | **Distance to VWAP**: `+1.11%`
- **VWAP Z-Score**: `+0.94 sigma` | **Mean Reversion Bias**: **`FAIR VALUE`**
- **VWAP Dispersion Bands**:
  * +1.00 sigma: `0.20075` | -1.00 sigma: `0.19605`
  * +1.28 sigma (80% CI): `0.20141` | -1.28 sigma: `0.19539`
  * +2.00 sigma (95% CI): `0.20310` | -2.00 sigma: `0.19370`
  * +2.01 sigma: `0.20313` | -2.01 sigma: `0.19367`
  * +2.51 sigma (98.8% CI): `0.20430` | -2.51 sigma: `0.19250`
  * +3.00 sigma (99.7% CI Extreme): `0.20545` | -3.00 sigma: `0.19135`
- **Oscillators & Volatility**:
  * **RSI (14)**: `59.89` | **RSI State**: **`BULLISH`**
  * **ATR (14)**: `0.00107` | **ATR %**: `0.53%`
  * **Bollinger Bands**: Upper=`0.20096` | Mid=`0.19935` | Lower=`0.19773` | Bandwidth=`1.62%`
  * **MACD**: Line=`+0.0006` | Signal=`+0.0004` | Hist=`+0.0001`
- **Exponential Moving Average Ribbon (EMA)**:
  * Short Horizon: EMA-5=`0.20016` | EMA-9=`0.19993` | EMA-13=`0.19970` | EMA-20=`0.19937`
  * Intermediate: EMA-34=`0.19913` | EMA-50=`0.19930` | EMA-89=`0.20010` | EMA-100=`0.20032`
  * Institutional: EMA-144=`0.20100` | EMA-200=`0.20148` (Slope: `-0.107%`) | EMA-233=`0.20183` (Slope: `-0.110%`)
  * **Trend Bias**: **`BULLISH`**

---

## 3. Auction Market Structure & Value Profile
*(Sources: 20_Auction_Market_Structure.parquet)*
- **Daily Auction Value Area**:
  * High (VAH): `0.20050` | Point of Control (POC): `0.19690` | Low (VAL): `0.19530`
  * Distance to POC: `+2.51%` | Distance to VAH: `+0.65%` | Distance to VAL: `+3.31%`
  * **Value Area Position**: **`ABOVE_VALUE (Imbalance)`** | **Auction Regime**: **`RANGE_EXPANSION`** | **Session Bias**: **`BEARISH (Below Pivot)`**
- **Prior Day & Weekly Auction Profile**:
  * Prior Day: PD VAH=`0.20670` | PD POC=`0.20540` | PD VAL=`0.20180` | PDH=`0.20860` | PDL=`0.19940` | PDC=`0.20540`
  * Monday Reference: Monday High=`0.20680` | Monday Low=`0.19910` | Monday Mid=`0.20300`
  * Weekly Value Area: Weekly VAH=`0.20580` | Weekly POC=`0.20300` | Weekly VAL=`0.20110`
  * Multi-Week Extremes: Current Week High (CWH)=`0.20860` | CWL=`0.19440` | Prior Week High (PWH)=`0.22910` | PWL=`0.19920`
  * Multi-Month Extremes: Current Month High (CMH)=`0.28110` | CML=`0.19440` | Prior Month High (PMH)=`0.26410` | PML=`0.18880`
- **Session Liquidity Extremes & Initial Balance**:
  * Asian Session: Range `[0.19440 - 0.20650]`
  * London Session: Range `[0.19570 - 0.20090]`
  * New York Session: Range `[0.19790 - 0.20140]`
  * Initial Balance (IB): IB High=`0.20000` | IB Low=`0.19770`
- **Fibonacci Golden Pocket & Optimal Trade Entry (OTE)**:
  * Swing Range: High=`0.20860` | Low=`0.19440` | Direction=`BEARISH_IMPULSE`
  * Golden Pocket [0.618 - 0.65]: `[0.20320 - 0.20360]`
  * Optimal Trade Entry (0.702): `0.20440` | Invalidation Level: `0.20560` | Status: **`SHALLOW_RETRACE`**
- **Classical & Weekly Pivots**:
  * Daily Classical: Pivot=`0.20450` | R1=`0.20950` | S1=`0.20030` | R2=`0.21370` | S2=`0.19530`
  * Weekly Classical: Weekly Pivot=`0.21090` | Weekly R1=`0.22250` | Weekly S1=`0.19260`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Orderflow
*(Sources: 18_CVD.parquet, 18_CVD_30D_5m.parquet, 18_CVD_30D_15m.parquet, 18_CVD_30D_1h.parquet, 18_CVD_30D_4h.parquet, 18_CVD_30D_ALL.parquet, 21_Tradfye_Orderflow.parquet)*
- **Primary 15m CVD Microstructure (18_CVD_30D_15m.parquet)**:
  * Candle Delta: `+40,585.47 USD` (Base: `+201,370.0000 coins`) | Delta %: `+2.94%`
  * Taker Volumes: Taker Buy=`710,006.00 USD` | Taker Sell=`669,420.54 USD` | Total Vol=`6,835,212.00 USD`
  * Cumulative CVD: `+419,070.21 USD` (Base: `+1,227,260.0000`)
  * Rolling CVD Z-Score: `-0.04 sigma` | Price Return: `+0.05%`
  * **Delta Regime**: **`NEUTRAL CHOP`** | Trades Count: `5,018`
- **Multi-Timeframe Delta Comparison**:
  * 5m Bar: Delta=`+57,606.07 USD` | Delta %=`+14.25%` | Z-Score=`+0.02` | Regime=`DELTA ALIGNED`
  * 1h Bar: Delta=`+40,585.47 USD` | Delta %=`+2.94%` | Z-Score=`+0.04` | Regime=`NEUTRAL CHOP`
  * 4h Bar: Delta=`+888,165.08 USD` | Delta %=`+5.12%` | Z-Score=`+0.32` | Regime=`DELTA ALIGNED`
  * 30D Consolidated (ALL): Cumulative Trend=`+55,869.93 USD` | Long-Term Regime=`DELTA ALIGNED`
- **Institutional Footprint & Deribit Options Armor (21_Tradfye_Orderflow.parquet)**:
  * Candle VWAP: `0.19720` | Estimated POC: `0.19715` | Avg Trade Size: `419.85 USD`
  * Net Delta USD: `+55,541.76 USD` | Net Delta %: `+3.48%` | Orderflow CVD: `+55,541.76 USD`
  * Orderflow Regime: **`TWO_SIDED_ABSORPTION`** | Orderflow Divergence: **`BULLISH_EXPANSION`**
  * Deribit Options Walls: Max Pain=`0.00` | Call Wall=`0.00` | Put Wall=`0.00`

---

## 5. Institutional Whale Armor & Resting Orderbook Depth
*(Sources: 10_Whale_Orders.parquet, 12_Hyperdash.parquet, 17_Orderbook.parquet, 4_Hyperliquid_Analysis.parquet)*
- **Defending Resting Whale Walls (10_Whale_Orders.parquet)**:
  * Defending Bid Wall: `0.20010` (`2303848.0760` coins / `461,000.00 USD` on `Binance`, persistent for `1h 51m`, Traded: `0.0%`, Order ID: `CG_LADDER_ADA_83`)
  * Defending Ask Wall: `0.20590` (`2068965.5172` coins / `426,000.00 USD` on `Binance`, persistent for `9h 12m`, Traded: `0.0%`, Order ID: `CG_LADDER_ADA_11`)
  * Total Whale Armor Pool: Bids Pool=`14,890,400.00 USD` | Asks Pool=`14,043,400.00 USD` (Tracked Orders: `182`)
- **Hyperdash Resting Depth & L3 Telemetry (12_Hyperdash.parquet)**:
  * `NEUTRAL`: `0.00 USD` @ `0.00000` (Size: `0.0`, Detail: Delta: +0, Wallet: None, Timestamp: 2026-10-29 19:44:05 IST)
- **Hyperliquid Elite Trader Positioning (4_Hyperliquid_Analysis.parquet)**:
  * Wallet `0x77eeda1995...` (0x77ee...2902): `Short` `4,324,192.17 USD` (21,412,192.0000 ADA, Margin: 432,419.22 USD, Leverage: 10X Cross, Entry: 0.191100 USD, Current: 0.201800 USD, Est Liq: 0.566800 USD, PnL: -232,940.43 USD [-5.39%], Fees: +7,385.62 USD)
  * Wallet `0x123dbca6a2...` (0x123d...3bff): `Long` `1,896,381.44 USD` (9,393,142.0000 ADA, Margin: 189,638.14 USD, Leverage: 10X Cross, Entry: 0.291200 USD, Current: 0.201800 USD, Est Liq: 0.00 USD, PnL: -839,354.50 USD [-44.26%], Fees: -8,173.51 USD)
  * Wallet `0x77375a8c9d...` (0x7737...bf66): `Short` `1,834,203.27 USD` (9,091,466.0000 ADA, Margin: 183,420.33 USD, Leverage: 10X Cross, Entry: 0.219000 USD, Current: 0.201800 USD, Est Liq: 2.1431 USD, PnL: +156,786.53 USD [+8.55%], Fees: +576.65 USD)

---

## 6. Liquidation Max Pain, Heatmaps & Cascade Boundaries
*(Sources: 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 14_Hyperdash_Liq_Map.parquet, 14_Liquidation_Matrix.parquet, 15_Hyperdash_Stops_Map.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`0.20470` (Vol: `214,800 USD`, Dist: `+1.24%`) | Long MP=`0.19270` (Vol: `248,000 USD`, Dist: `-4.70%`)
  * 48H Horizon: Short MP=`0.21370` (Vol: `235,900 USD`, Dist: `+5.69%`) | Long MP=`0.19270` (Vol: `248,000 USD`, Dist: `-4.70%`)
  * 3D Horizon: Short MP=`0.21110` (Vol: `241,100 USD`, Dist: `+4.40%`) | Long MP=`0.19270` (Vol: `248,000 USD`, Dist: `-4.70%`)
  * 7D Horizon: Short MP=`0.21237` (Vol: `359,800 USD`, Dist: `+5.03%`) | Long MP=`0.19259` (Vol: `321,900 USD`, Dist: `-4.75%`)
- **Exchange Cumulative Liquidation Cascades (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
  * 1D Cascade: Total=`9.98M USD` | Short Liq Pool=`9.98M USD` | Long Liq Pool=`0 USD` | Venues: Binance=`46.10K USD`, OKX=`11.06K USD`, Bybit=`15.42K USD`
  * 7D Cascade: Total=`29.71M USD` | Short Liq Pool=`29.71M USD` | Long Liq Pool=`0 USD` | Venues: Binance=`149.81K USD`, OKX=`47.32K USD`, Bybit=`85.13K USD`
- **Cross-Venue Liquidation Matrix & Heatmaps (14_Liquidation_Matrix.parquet, 7_Liq_Heapmap.parquet)**:
  * Liquidation Matrix Strike: Price=`0.40450` | Vol=`1,030 USD` | Cumulative=`3,280,000 USD` | Venue=`Hyperliquid L1` | Side=`Short Liquidation`
  * Multi-Timeframe Heatmap Density: 1h=`0.00 USD` | 4h=`0.00 USD` | 12h=`374.83K USD` | 24h=`2.61M USD`
- **Hyperdash Real-Time Liquidation & Retail Stop Protection (14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet)**:
  * Hyperdash Liq Cluster: Mark=`0.202050 USD` | Cluster Price=`0.404500 USD` | Dist=`+100.20%` | Cumulative=`3.28M USD` | Short=`1.03K USD` | Long=`0 USD` | Size=`2,543.0000 ADA`
  * **Retail Stops Map (Pitfall 2 & 4 Defense)**:
    - `Sell Stop`: `0.059500 USD` (Dist: `-70.55%`, Cumulative Stops: `639.29M USD`, Buy: `0 USD`, Sell: `415.13 USD`, Coins: `6,977.0000 ADA`)
    - `Sell Stop`: `0.061500 USD` (Dist: `-69.56%`, Cumulative Stops: `639.29M USD`, Buy: `0 USD`, Sell: `463.46 USD`, Coins: `7,536.0000 ADA`)
    - `Sell Stop`: `0.110500 USD` (Dist: `-45.31%`, Cumulative Stops: `639.29M USD`, Buy: `0 USD`, Sell: `1.10K USD`, Coins: `10,000.0000 ADA`)
- **Live Forced Liquidation Momentum (7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)**:
  * Multi-Timeframe Forced Aggregates (5m): Long Liq=`0.00 USD` | Short Liq=`0.00 USD` | Total=`0.00 USD` | Net Delta=`0.00 USD` | Dominant=`BALANCED`

---

## 7. Derivatives Sentiment, Open Interest & Funding Dynamics
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet, 6_Funding_Fee_Settlement.parquet, 13_Hyperliquid.parquet)*
- **Aggregated Open Interest Breakdown (5_OI.parquet)**:
  * Total Open Interest: `455.02M USD` (`2,253,135,026.1 ADA`) | OI / 24h Volume Ratio: `0.7583`
  * OI Expansion Rate: 1h Change=`+0.83%` | 4h Change=`+2.21%` | 24h Change=`-2.05%`
  * Venue Concentration:
    - Binance: `85.26M USD` | Bybit: `53.28M USD` | OKX: `31.90M USD` | CME Institutional: `8.50M USD`
    - Gate: `71.16M USD` | MEXC: `40.90M USD` | Hyperliquid DEX: `30.41M USD` | Bitget: `40.83M USD`
    - KuCoin: `21.15M USD` | BingX: `12.00M USD` | Bitunix: `4.31M USD` | Others: `55.32M USD`
- **Cross-Exchange Perpetual Funding Rates (5_Funding_Rate.parquet)**:
  * Major CEX Rates: Binance=`+0.0100%` | OKX=`-0.0038%` | Bybit=`+0.0050%` | Bitget=`+0.0005%`
  * Mid-Tier CEX Rates: KuCoin=`+0.0042%` | MEXC=`+0.0100%` | Gate=`+0.0100%` | BingX=`+0.0100%` | Bitunix=`+0.0150%`
  * Alternative Venues: WhiteBIT=`+0.0100%` | LBank=`+0.0100%` | tradeXYZ=`-`
  * Inverse Coin-Margined: CoinM Binance=`+0.0100%` | CoinM OKX=`+0.0100%` | CoinM Bybit=`+0.0100%`
- **Exchange Long / Short Ratio Dynamics (3_Exchanges_LS_Ratio*.parquet)**:
  * 15m Tactical: L/S Ratio=`0.81` (Longs: `44.70%`, Shorts: `55.30%`, Total Vol: `10.64M USD`)
  * 1h Primary: L/S Ratio=`1.06` (Longs: `51.39%`, Shorts: `48.61%`, Total Vol: `106.42M USD`)
  * 4h Macro: L/S Ratio=`1.08` (Longs: `52.00%`, Shorts: `48.00%`, Total Vol: `317.19M USD`)
- **Funding Fee Settlement & DEX Arbitrage (6_Funding_Fee_Settlement.parquet, 13_Hyperliquid.parquet)**:
  * Settlement Payouts: Current Expected=`8.72K USD` | Last 24h=`-492.56 USD` | Last 3D=`57.99K USD` | Last 7D=`35.83K USD`

---

## 8. Microstructure Footprint, Tape Imbalances & Macro Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 16_Hyperdash_telegram_Intel.parquet, 19_News.parquet, 19_Calendar.parquet)*
- **Bar-by-Bar Microstructure Footprint (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
  * Venue Source: `CoinGlass-AggregatedFutures(Binance)` | Timeframe: `15m` | Last Price: `0.20175`
  * Footprint Auction Profile: Bar VWAP=`0.20192` | Bar POC=`0.20195` | Bar VAH=`0.20235` | Bar VAL=`0.20135`
  * Orderflow Volumes: Total Vol=`1,055,965.92 USD` | Taker Buy=`522,223.33 USD` | Taker Sell=`533,742.59 USD`
  * Bar Delta Profile: Delta=`-11,519.25 USD` (`-1.09%`) | Max Delta=`+19,556.57 USD` | Min Delta=`-21,238.79 USD` | Cumulative Bar Delta=`+672,919.04 USD`
  * Order Execution Dynamics: Trades Count=`4,124` | Avg Trade Size=`256.05 USD`
  * Tape Imbalances: Imbalance Ratio=`300.0%` | Buy Imbalances Count=`2` | Sell Imbalances Count=`1`
  * Footprint Open Interest: Bar OI=`0.00 USD` | Bar OI Change=`+0.00 USD`
- **CoinGlass Algorithmic Footprint Signals (25_CoinGlass_Footprint_Signals.parquet)**:
  * Signal Classification: Type=`Absorption` | Bias: **`BULLISH`** | Signal Time=`10-28 07:53` | Timeframe=`Range 0.001`
  * Signal Context: Headline=`Selling absorbed at the low` | Price Level=`0.20630` | Absorbed Volume=`3,600,000.00 USD`
  * Bar Footprint Context: Current Bar Delta=`+0.00 USD` | Current Bar Volume=`0.00 USD` | Delta in View=`+0.00 USD`
  * Historical Detail: `3.6M of taker selling at the low (30%+ of the bar's selling), yet closed near the high, bullish · 0.20630` | KPI=`—` | Bias=`—`
- **Multi-Horizon Macro Capital Netflows (2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet)**:
  * Spot Capital Netflows:
    - Tactical: 5m=`-844.79` | 15m=`+145.33K` | 30m=`+164.78K` | 1h=`-54.16K`
    - Intermediate: 2h=`+90.48K` | 4h=`+280.78K` | 6h=`+445.96K` | 8h=`+313.64K` | 12h=`-169.42K` | 24h=`-2.63M`
    - Macro Horizons: 1-Week=`-14.87M` | 15-Day=`-32.08M` | 30-Day=`-70.32M` | Market Cap=`7.43B`
  * Futures Capital Netflows:
    - Tactical: 5m=`+31.91K` | 15m=`+329.99K` | 30m=`+554.17K` | 1h=`+920.06K`
    - Intermediate: 2h=`+1.56M` | 4h=`+1.12M` | 6h=`+2.61M` | 8h=`+2.61M` | 12h=`+1.98M` | 24h=`-2.73M`
    - Macro Horizons: 1-Week=`-36.59M` | 15-Day=`-54.91M` | 30-Day=`-190.05M` | Market Cap=`7.43B`
- **Telegram Intelligence Alert**: `[MARKET_INTEL] #ADA Whale BUY: 6.66K USD at 0.2061 USD [API] (Impact: NEWS_INTEL)`

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
- **Stand-Aside Reason**: Gate 1 Spread Friction Failure: Spread friction 104.09 bps exceeds cap 25.0 bps. Standing aside in 100% cash preserves statutory floor.