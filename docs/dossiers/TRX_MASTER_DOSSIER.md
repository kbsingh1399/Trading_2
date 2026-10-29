# 🔬 MASTER 43-FEED QUANTITATIVE DOSSIER: TRX (TRON)
**MT5 Symbol**: `TRXUSD.p` | **Category**: `Crypto Alt L1` | **Tier**: `Tier 1`
**Execution Posture**: `DISQUALIFIED` | **Timestamp**: 2026-10-29 14:43:14 UTC
**Pipeline Clearance**: `BLOCKED` | **Data Freshness**: `1.2m`

---

## 1. MT5 Live Broker Telemetry & Spread Friction Gate
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet)*
- **Live Bid Quote**: `0.33070` | **Live Ask Quote**: `0.33180` | **Mid Price**: `0.33125`
- **Spread Points**: `11.0 pts` | **Spread BPS**: `33.21 bps` (Mandatory Cap: `25.0 bps`)
- **Gate Status**: **`FAIL`** (Spread friction 33.21 bps exceeds cap 25.0 bps)
- **Order Allowed**: `NONE` | **Pillar 1 Clearance**: `BLOCKED`
- **Broker Specifications**: Contract Size=`1.00` | Tick Value=`1.00 USD` | Min Lot=`0.01` | Digits=`5`
- **Account Capital Context**: Balance=`4,744.55 USD` | Equity=`4,744.32 USD` | Free Margin=`4,342.62 USD` | Inviolate Hard Floor=`4,775.00 USD` (Cushion: `-30.68 USD`)
- **Pipeline Health**: Feed #00 Status=`PASS` | Overall Pipeline Telemetry=`33/33 FEEDS PASS (SYNCHRONIZED)`

---

## 2. Technical Profile, Multi-Sigma VWAP Dispersion & Volatility
*(Sources: 11_Technical.parquet, 11_Technical_BTC_Ribbon.parquet)*
- **Last Verified Price**: `0.33120` | **24h Change**: `+0.00%` (24h High: `0.33150`, 24h Low: `0.32850`)
- **Weekly Range**: Week High=`0.33190` | Week Low=`0.32660` | Daily POC=`0.33080` | Daily VAH=`0.33120` | Daily VAL=`0.32910`
- **Session VWAP**: `0.33005` | **Rolling 24h VWAP**: `0.32989` | **Distance to VWAP**: `+0.35%`
- **VWAP Z-Score**: `+1.36 sigma` | **Mean Reversion Bias**: **`FAIR VALUE`**
- **VWAP Dispersion Bands**:
  * +1.00 sigma: `0.33089` | -1.00 sigma: `0.32920`
  * +1.28 sigma (80% CI): `0.33113` | -1.28 sigma: `0.32896`
  * +2.00 sigma (95% CI): `0.33174` | -2.00 sigma: `0.32835`
  * +2.01 sigma: `0.33175` | -2.01 sigma: `0.32835`
  * +2.51 sigma (98.8% CI): `0.33217` | -2.51 sigma: `0.32792`
  * +3.00 sigma (99.7% CI Extreme): `0.33259` | -3.00 sigma: `0.32751`
- **Oscillators & Volatility**:
  * **RSI (14)**: `61.37` | **RSI State**: **`BULLISH`**
  * **ATR (14)**: `0.00035` | **ATR %**: `0.10%`
  * **Bollinger Bands**: Upper=`0.33118` | Mid=`0.33085` | Lower=`0.33052` | Bandwidth=`0.20%`
  * **MACD**: Line=`+0.0001` | Signal=`+0.0001` | Hist=`+0.0000`
- **Exponential Moving Average Ribbon (EMA)**:
  * Short Horizon: EMA-5=`0.33101` | EMA-9=`0.33094` | EMA-13=`0.33090` | EMA-20=`0.33084`
  * Intermediate: EMA-34=`0.33068` | EMA-50=`0.33053` | EMA-89=`0.33032` | EMA-100=`0.33028`
  * Institutional: EMA-144=`0.33014` | EMA-200=`0.32987` (Slope: `+0.039%`) | EMA-233=`0.32981` (Slope: `+0.035%`)
  * **Trend Bias**: **`STRONG BULLISH`**

---

## 3. Auction Market Structure & Value Profile
*(Sources: 20_Auction_Market_Structure.parquet)*
- **Daily Auction Value Area**:
  * High (VAH): `0.33120` | Point of Control (POC): `0.33080` | Low (VAL): `0.32910`
  * Distance to POC: `+0.16%` | Distance to VAH: `+0.04%` | Distance to VAL: `+0.69%`
  * **Value Area Position**: **`ABOVE_VALUE (Imbalance)`** | **Auction Regime**: **`RANGE_EXPANSION`** | **Session Bias**: **`BULLISH (Above Pivot)`**
- **Prior Day & Weekly Auction Profile**:
  * Prior Day: PD VAH=`0.33140` | PD POC=`0.33090` | PD VAL=`0.33040` | PDH=`0.33190` | PDL=`0.32880` | PDC=`0.32890`
  * Monday Reference: Monday High=`0.33100` | Monday Low=`0.32890` | Monday Mid=`0.33000`
  * Weekly Value Area: Weekly VAH=`0.33120` | Weekly POC=`0.33080` | Weekly VAL=`0.32890`
  * Multi-Week Extremes: Current Week High (CWH)=`0.33190` | CWL=`0.32660` | Prior Week High (PWH)=`0.33290` | PWL=`0.32700`
  * Multi-Month Extremes: Current Month High (CMH)=`0.33810` | CML=`0.32410` | Prior Month High (PMH)=`0.34850` | PML=`0.32030`
- **Session Liquidity Extremes & Initial Balance**:
  * Asian Session: Range `[0.32850 - 0.33060]`
  * London Session: Range `[0.33030 - 0.33110]`
  * New York Session: Range `[0.33010 - 0.33130]`
  * Initial Balance (IB): IB High=`0.33110` | IB Low=`0.33030`
- **Fibonacci Golden Pocket & Optimal Trade Entry (OTE)**:
  * Swing Range: High=`0.33140` | Low=`0.32850` | Direction=`BEARISH_IMPULSE`
  * Golden Pocket [0.618 - 0.65]: `[0.33030 - 0.33040]`
  * Optimal Trade Entry (0.702): `0.33050` | Invalidation Level: `0.33080` | Status: **`STRUCTURE_INVALIDATED`**
- **Classical & Weekly Pivots**:
  * Daily Classical: Pivot=`0.32990` | R1=`0.33090` | S1=`0.32780` | R2=`0.33300` | S2=`0.32680`
  * Weekly Classical: Weekly Pivot=`0.32990` | Weekly R1=`0.33280` | Weekly S1=`0.32690`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Orderflow
*(Sources: 18_CVD.parquet, 18_CVD_30D_5m.parquet, 18_CVD_30D_15m.parquet, 18_CVD_30D_1h.parquet, 18_CVD_30D_4h.parquet, 18_CVD_30D_ALL.parquet, 21_Tradfye_Orderflow.parquet)*
- **Primary 15m CVD Microstructure (18_CVD_30D_15m.parquet)**:
  * Candle Delta: `-388,095.11 USD` (Base: `-1,171,583.0000 coins`) | Delta %: `-13.98%`
  * Taker Volumes: Taker Buy=`1,193,566.19 USD` | Taker Sell=`1,581,661.29 USD` | Total Vol=`8,380,257.00 USD`
  * Cumulative CVD: `+72,788.11 USD` (Base: `+220,527.0000`)
  * Rolling CVD Z-Score: `-3.31 sigma` | Price Return: `-0.10%`
  * **Delta Regime**: **`DELTA ALIGNED`** | Trades Count: `7,801`
- **Multi-Timeframe Delta Comparison**:
  * 5m Bar: Delta=`+288,459.44 USD` | Delta %=`+67.40%` | Z-Score=`+1.97` | Regime=`AGGRESSIVE BUYING`
  * 1h Bar: Delta=`-388,095.11 USD` | Delta %=`-13.98%` | Z-Score=`-1.86` | Regime=`DELTA ALIGNED`
  * 4h Bar: Delta=`+86,567.60 USD` | Delta %=`+1.75%` | Z-Score=`+0.00` | Regime=`BULLISH ABSORPTION`
  * 30D Consolidated (ALL): Cumulative Trend=`+502,057.77 USD` | Long-Term Regime=`BULLISH ABSORPTION`
- **Institutional Footprint & Deribit Options Armor (21_Tradfye_Orderflow.parquet)**:
  * Candle VWAP: `0.33014` | Estimated POC: `0.33008` | Avg Trade Size: `324.19 USD`
  * Net Delta USD: `+363,112.78 USD` | Net Delta %: `+35.46%` | Orderflow CVD: `+363,112.78 USD`
  * Orderflow Regime: **`AGGRESSIVE_BUYER_DOMINATION`** | Orderflow Divergence: **`BULLISH_EXPANSION`**
  * Deribit Options Walls: Max Pain=`0.00` | Call Wall=`0.00` | Put Wall=`0.00`

---

## 5. Institutional Whale Armor & Resting Orderbook Depth
*(Sources: 10_Whale_Orders.parquet, 12_Hyperdash.parquet, 17_Orderbook.parquet, 4_Hyperliquid_Analysis.parquet)*
- **Defending Resting Whale Walls (10_Whale_Orders.parquet)**:
  * Defending Bid Wall: `0.32470` (`914690.4835` coins / `355,000.00 USD` on `Binance`, persistent for `11m 11s`, Traded: `0.0%`, Order ID: `CG_WHALE_TRX_T_81`)
  * Defending Ask Wall: `0.33180` (`379746.8354` coins / `212,000.00 USD` on `Binance`, persistent for `12m 21s`, Traded: `0.0%`, Order ID: `CG_WHALE_TRX_T_34`)
  * Total Whale Armor Pool: Bids Pool=`9,533,400.00 USD` | Asks Pool=`8,488,000.00 USD` (Tracked Orders: `182`)
- **Hyperdash Resting Depth & L3 Telemetry (12_Hyperdash.parquet)**:
  * `NEUTRAL`: `0.00 USD` @ `0.00000` (Size: `0.0`, Detail: Delta: +0, Wallet: None, Timestamp: 2026-10-29 19:44:05 IST)
- **Hyperliquid Elite Trader Positioning (4_Hyperliquid_Analysis.parquet)**:
  * Wallet `0xeadc152ac1...` (0xeadc...9d55): `Long` `1,326,320.00 USD` (4,000,000.0000 TRX, Margin: 132,632.00 USD, Leverage: 10X Cross, Entry: 0.342100 USD, Current: 0.331560 USD, Est Liq: 0.00 USD, PnL: -42,158.09 USD [-3.18%], Fees: -27,482.87 USD)
  * Wallet `0xecb63caa47...` (0xecb6...2b00): `Long` `1,085,865.63 USD` (3,275,020.0000 TRX, Margin: 108,586.56 USD, Leverage: 10X Cross, Entry: 0.330600 USD, Current: 0.331560 USD, Est Liq: 0.00 USD, PnL: +3,014.01 USD [+0.28%], Fees: -28,788.27 USD)

---

## 6. Liquidation Max Pain, Heatmaps & Cascade Boundaries
*(Sources: 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 14_Hyperdash_Liq_Map.parquet, 14_Liquidation_Matrix.parquet, 15_Hyperdash_Stops_Map.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`0.33826` (Vol: `341,600 USD`, Dist: `+2.08%`) | Long MP=`0.32503` (Vol: `314,500 USD`, Dist: `-1.91%`)
  * 48H Horizon: Short MP=`0.33817` (Vol: `425,500 USD`, Dist: `+2.06%`) | Long MP=`0.32492` (Vol: `425,500 USD`, Dist: `-1.94%`)
  * 3D Horizon: Short MP=`0.33830` (Vol: `453,400 USD`, Dist: `+2.10%`) | Long MP=`0.32499` (Vol: `454,200 USD`, Dist: `-1.92%`)
  * 7D Horizon: Short MP=`0.33685` (Vol: `499,100 USD`, Dist: `+1.66%`) | Long MP=`0.32499` (Vol: `515,000 USD`, Dist: `-1.92%`)
- **Exchange Cumulative Liquidation Cascades (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
  * 1D Cascade: Total=`2.94M USD` | Short Liq Pool=`2.94M USD` | Long Liq Pool=`0 USD` | Venues: Binance=`13.31K USD`, OKX=`2.51K USD`, Bybit=`2.74K USD`
  * 7D Cascade: Total=`13.81M USD` | Short Liq Pool=`13.81M USD` | Long Liq Pool=`0 USD` | Venues: Binance=`60.98K USD`, OKX=`4.81K USD`, Bybit=`2.64K USD`
- **Cross-Venue Liquidation Matrix & Heatmaps (14_Liquidation_Matrix.parquet, 7_Liq_Heapmap.parquet)**:
  * Liquidation Matrix Strike: Price=`0.63150` | Vol=`340 USD` | Cumulative=`1,810,000 USD` | Venue=`Hyperliquid L1` | Side=`Short Liquidation`
  * Multi-Timeframe Heatmap Density: 1h=`0.00 USD` | 4h=`0.00 USD` | 12h=`0.00 USD` | 24h=`0.00 USD`
- **Hyperdash Real-Time Liquidation & Retail Stop Protection (14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet)**:
  * Hyperdash Liq Cluster: Mark=`0.331960 USD` | Cluster Price=`0.631500 USD` | Dist=`+90.23%` | Cumulative=`1.81M USD` | Short=`340.38 USD` | Long=`0 USD` | Size=`539.0000 TRX`
  * **Retail Stops Map (Pitfall 2 & 4 Defense)**:
    - `Sell Stop`: `0.180500 USD` (Dist: `-45.63%`, Cumulative Stops: `826.95K USD`, Buy: `0 USD`, Sell: `6.10K USD`, Coins: `33,792.0000 TRX`)
    - `Sell Stop`: `0.203500 USD` (Dist: `-38.70%`, Cumulative Stops: `820.85K USD`, Buy: `0 USD`, Sell: `1.75K USD`, Coins: `8,609.0000 TRX`)
    - `Sell Stop`: `0.210500 USD` (Dist: `-36.59%`, Cumulative Stops: `819.10K USD`, Buy: `0 USD`, Sell: `579.72 USD`, Coins: `2,754.0000 TRX`)
- **Live Forced Liquidation Momentum (7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)**:
  * Multi-Timeframe Forced Aggregates (5m): Long Liq=`0.00 USD` | Short Liq=`0.00 USD` | Total=`0.00 USD` | Net Delta=`0.00 USD` | Dominant=`BALANCED`

---

## 7. Derivatives Sentiment, Open Interest & Funding Dynamics
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet, 6_Funding_Fee_Settlement.parquet, 13_Hyperliquid.parquet)*
- **Aggregated Open Interest Breakdown (5_OI.parquet)**:
  * Total Open Interest: `299.84M USD` (`904,904,332.4 TRX`) | OI / 24h Volume Ratio: `2.7102`
  * OI Expansion Rate: 1h Change=`+4.51%` | 4h Change=`+4.79%` | 24h Change=`+0.66%`
  * Venue Concentration:
    - Binance: `90.29M USD` | Bybit: `49.83M USD` | OKX: `13.89M USD` | CME Institutional: `0.00 USD`
    - Gate: `79.33M USD` | MEXC: `8.98M USD` | Hyperliquid DEX: `11.42M USD` | Bitget: `10.18M USD`
    - KuCoin: `6.01M USD` | BingX: `4.78M USD` | Bitunix: `1.48M USD` | Others: `23.65M USD`
- **Cross-Exchange Perpetual Funding Rates (5_Funding_Rate.parquet)**:
  * Major CEX Rates: Binance=`+0.0100%` | OKX=`+0.0100%` | Bybit=`+0.0059%` | Bitget=`+0.0100%`
  * Mid-Tier CEX Rates: KuCoin=`+0.0100%` | MEXC=`+0.0100%` | Gate=`+0.0099%` | BingX=`+0.0100%` | Bitunix=`+0.0100%`
  * Alternative Venues: WhiteBIT=`+0.0100%` | LBank=`+0.0100%` | tradeXYZ=`-`
  * Inverse Coin-Margined: CoinM Binance=`+0.0100%` | CoinM OKX=`+0.0000%` | CoinM Bybit=`+0.0000%`
- **Exchange Long / Short Ratio Dynamics (3_Exchanges_LS_Ratio*.parquet)**:
  * 15m Tactical: L/S Ratio=`0.96` (Longs: `48.95%`, Shorts: `51.05%`, Total Vol: `10.74M USD`)
  * 1h Primary: L/S Ratio=`1.03` (Longs: `50.69%`, Shorts: `49.31%`, Total Vol: `54.52M USD`)
  * 4h Macro: L/S Ratio=`1.02` (Longs: `50.53%`, Shorts: `49.47%`, Total Vol: `176.77M USD`)
- **Funding Fee Settlement & DEX Arbitrage (6_Funding_Fee_Settlement.parquet, 13_Hyperliquid.parquet)**:
  * Settlement Payouts: Current Expected=`12.75K USD` | Last 24h=`8.30K USD` | Last 3D=`-75.25K USD` | Last 7D=`-283.91K USD`

---

## 8. Microstructure Footprint, Tape Imbalances & Macro Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 16_Hyperdash_telegram_Intel.parquet, 19_News.parquet, 19_Calendar.parquet)*
- **Bar-by-Bar Microstructure Footprint (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
  * Venue Source: `CoinGlass-AggregatedFutures(Binance)` | Timeframe: `15m` | Last Price: `0.33125`
  * Footprint Auction Profile: Bar VWAP=`0.33115` | Bar POC=`0.33174` | Bar VAH=`0.33176` | Bar VAL=`0.33064`
  * Orderflow Volumes: Total Vol=`2,412,422.91 USD` | Taker Buy=`899,769.26 USD` | Taker Sell=`1,512,653.64 USD`
  * Bar Delta Profile: Delta=`-612,884.38 USD` (`-25.41%`) | Max Delta=`+20,594.08 USD` | Min Delta=`-615,732.78 USD` | Cumulative Bar Delta=`-81,921.64 USD`
  * Order Execution Dynamics: Trades Count=`6,343` | Avg Trade Size=`380.33 USD`
  * Tape Imbalances: Imbalance Ratio=`300.0%` | Buy Imbalances Count=`12` | Sell Imbalances Count=`29`
  * Footprint Open Interest: Bar OI=`0.00 USD` | Bar OI Change=`+0.00 USD`
- **CoinGlass Algorithmic Footprint Signals (25_CoinGlass_Footprint_Signals.parquet)**:
  * Signal Classification: Type=`Absorption` | Bias: **`BULLISH`** | Signal Time=`10-28 05:44` | Timeframe=`Volume 1.0M TRX`
  * Signal Context: Headline=`Selling absorbed at the low` | Price Level=`0.33180` | Absorbed Volume=`198,000.00 USD`
  * Bar Footprint Context: Current Bar Delta=`+0.00 USD` | Current Bar Volume=`0.00 USD` | Delta in View=`+0.00 USD`
  * Historical Detail: `198K of taker selling at the low (30%+ of the bar's selling), yet closed near the high, bullish · 0.33180` | KPI=`—` | Bias=`—`
- **Multi-Horizon Macro Capital Netflows (2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet)**:
  * Spot Capital Netflows:
    - Tactical: 5m=`+304.87K` | 15m=`-832.47K` | 30m=`-851.11K` | 1h=`-825.23K`
    - Intermediate: 2h=`-878.32K` | 4h=`-726.29K` | 6h=`-836.75K` | 8h=`-639.64K` | 12h=`+2.12M` | 24h=`-226.32K`
    - Macro Horizons: 1-Week=`-9.33M` | 15-Day=`-23.96M` | 30-Day=`-23.31M` | Market Cap=`31.49B`
  * Futures Capital Netflows:
    - Tactical: 5m=`-757.87K` | 15m=`-866.17K` | 30m=`-858.66K` | 1h=`-547.36K`
    - Intermediate: 2h=`-378.61K` | 4h=`-368.95K` | 6h=`-198.97K` | 8h=`+445.14K` | 12h=`+1.71M` | 24h=`+441.21K`
    - Macro Horizons: 1-Week=`-2.93M` | 15-Day=`-6.02M` | 30-Day=`+3.66M` | Market Cap=`31.49B`
- **Telegram Intelligence Alert**: `[MARKET_INTEL] #TRX Whale SELL: 8.10K USD at 0.3315 USD [API] (Impact: NEWS_INTEL)`

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
- **Stand-Aside Reason**: Gate 1 Spread Friction Failure: Spread friction 33.21 bps exceeds cap 25.0 bps. Standing aside in 100% cash preserves statutory floor.