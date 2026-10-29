# 🔬 MASTER 43-FEED QUANTITATIVE DOSSIER: BCH (Bitcoin Cash)
**MT5 Symbol**: `BCHUSD.p` | **Category**: `Crypto PoW` | **Tier**: `Tier 1`
**Execution Posture**: `PASSIVE LIMIT ONLY` | **Timestamp**: 2026-10-29 14:43:14 UTC
**Pipeline Clearance**: `QUALIFIED` | **Data Freshness**: `1.2m`

---

## 1. MT5 Live Broker Telemetry & Spread Friction Gate
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet)*
- **Live Bid Quote**: `279.16000` | **Live Ask Quote**: `279.64000` | **Mid Price**: `279.40000`
- **Spread Points**: `480.0 pts` | **Spread BPS**: `17.18 bps` (Mandatory Cap: `25.0 bps`)
- **Gate Status**: **`PASS`** (Spread friction within mandatory threshold; safe for maker execution)
- **Order Allowed**: `BUY_LIMIT / SELL_LIMIT` | **Pillar 1 Clearance**: `QUALIFIED`
- **Broker Specifications**: Contract Size=`1.00` | Tick Value=`1.00 USD` | Min Lot=`0.01` | Digits=`5`
- **Account Capital Context**: Balance=`4,744.55 USD` | Equity=`4,744.32 USD` | Free Margin=`4,342.62 USD` | Inviolate Hard Floor=`4,775.00 USD` (Cushion: `-30.68 USD`)
- **Pipeline Health**: Feed #00 Status=`PASS` | Overall Pipeline Telemetry=`33/33 FEEDS PASS (SYNCHRONIZED)`

---

## 2. Technical Profile, Multi-Sigma VWAP Dispersion & Volatility
*(Sources: 11_Technical.parquet, 11_Technical_BTC_Ribbon.parquet)*
- **Last Verified Price**: `278.26000` | **24h Change**: `-5.34%` (24h High: `294.66000`, 24h Low: `274.76000`)
- **Weekly Range**: Week High=`304.16000` | Week Low=`274.15900` | Daily POC=`278.83000` | Daily VAH=`283.26000` | Daily VAL=`275.45000`
- **Session VWAP**: `280.65264` | **Rolling 24h VWAP**: `283.73719` | **Distance to VWAP**: `-0.85%`
- **VWAP Z-Score**: `-0.79 sigma` | **Mean Reversion Bias**: **`FAIR VALUE`**
- **VWAP Dispersion Bands**:
  * +1.00 sigma: `283.66792` | -1.00 sigma: `277.63737`
  * +1.28 sigma (80% CI): `284.51219` | -1.28 sigma: `276.79310`
  * +2.00 sigma (95% CI): `286.68319` | -2.00 sigma: `274.62210`
  * +2.01 sigma: `286.71334` | -2.01 sigma: `274.59195`
  * +2.51 sigma (98.8% CI): `288.22098` | -2.51 sigma: `273.08431`
  * +3.00 sigma (99.7% CI Extreme): `289.69846` | -3.00 sigma: `271.60683`
- **Oscillators & Volatility**:
  * **RSI (14)**: `43.27` | **RSI State**: **`BEARISH`**
  * **ATR (14)**: `1.23144` | **ATR %**: `0.44%`
  * **Bollinger Bands**: Upper=`280.70903` | Mid=`279.09500` | Lower=`277.48097` | Bandwidth=`1.16%`
  * **MACD**: Line=`-0.4946` | Signal=`-0.4593` | Hist=`-0.0353`
- **Exponential Moving Average Ribbon (EMA)**:
  * Short Horizon: EMA-5=`278.32857` | EMA-9=`278.52895` | EMA-13=`278.68650` | EMA-20=`278.91541`
  * Intermediate: EMA-34=`279.53898` | EMA-50=`280.52602` | EMA-89=`282.83130` | EMA-100=`283.31312`
  * Institutional: EMA-144=`284.36320` | EMA-200=`284.08995` (Slope: `-0.239%`) | EMA-233=`284.22673` (Slope: `-0.208%`)
  * **Trend Bias**: **`STRONG BEARISH`**

---

## 3. Auction Market Structure & Value Profile
*(Sources: 20_Auction_Market_Structure.parquet)*
- **Daily Auction Value Area**:
  * High (VAH): `283.26000` | Point of Control (POC): `278.83000` | Low (VAL): `275.45000`
  * Distance to POC: `+0.21%` | Distance to VAH: `-1.36%` | Distance to VAL: `+1.44%`
  * **Value Area Position**: **`INSIDE_VALUE (Balance)`** | **Auction Regime**: **`ROTATIONAL_BALANCE`** | **Session Bias**: **`BEARISH (Below Pivot)`**
- **Prior Day & Weekly Auction Profile**:
  * Prior Day: PD VAH=`299.16000` | PD POC=`296.76000` | PD VAL=`289.44000` | PDH=`304.16000` | PDL=`281.75000` | PDC=`288.90000`
  * Monday Reference: Monday High=`283.95000` | Monday Low=`273.26000` | Monday Mid=`278.61000`
  * Weekly Value Area: Weekly VAH=`289.22000` | Weekly POC=`278.72000` | Weekly VAL=`275.22000`
  * Multi-Week Extremes: Current Week High (CWH)=`304.16000` | CWL=`273.26000` | Prior Week High (PWH)=`290.06000` | PWL=`264.76000`
  * Multi-Month Extremes: Current Month High (CMH)=`322.26000` | CML=`255.33000` | Prior Month High (PMH)=`365.66000` | PML=`212.46000`
- **Session Liquidity Extremes & Initial Balance**:
  * Asian Session: Range `[274.76000 - 290.60000]`
  * London Session: Range `[276.86000 - 281.86000]`
  * New York Session: Range `[277.16000 - 281.56000]`
  * Initial Balance (IB): IB High=`281.86000` | IB Low=`279.31000`
- **Fibonacci Golden Pocket & Optimal Trade Entry (OTE)**:
  * Swing Range: High=`294.16000` | Low=`274.76000` | Direction=`BEARISH_IMPULSE`
  * Golden Pocket [0.618 - 0.65]: `[286.75000 - 287.37000]`
  * Optimal Trade Entry (0.702): `288.38000` | Invalidation Level: `290.01000` | Status: **`SHALLOW_RETRACE`**
- **Classical & Weekly Pivots**:
  * Daily Classical: Pivot=`291.60000` | R1=`301.46000` | S1=`279.05000` | R2=`314.01000` | S2=`269.19000`
  * Weekly Classical: Weekly Pivot=`278.09000` | Weekly R1=`291.43000` | Weekly S1=`266.13000`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Orderflow
*(Sources: 18_CVD.parquet, 18_CVD_30D_5m.parquet, 18_CVD_30D_15m.parquet, 18_CVD_30D_1h.parquet, 18_CVD_30D_4h.parquet, 18_CVD_30D_ALL.parquet, 21_Tradfye_Orderflow.parquet)*
- **Primary 15m CVD Microstructure (18_CVD_30D_15m.parquet)**:
  * Candle Delta: `+132,045.23 USD` (Base: `+472.7750 coins`) | Delta %: `+14.69%`
  * Taker Volumes: Taker Buy=`515,488.00 USD` | Taker Sell=`383,442.77 USD` | Total Vol=`3,222.38 USD`
  * Cumulative CVD: `-2,348,276.54 USD` (Base: `-8,282.2130`)
  * Rolling CVD Z-Score: `+0.47 sigma` | Price Return: `+0.33%`
  * **Delta Regime**: **`DELTA ALIGNED`** | Trades Count: `6,177`
- **Multi-Timeframe Delta Comparison**:
  * 5m Bar: Delta=`-15,016.34 USD` | Delta %=`-11.49%` | Z-Score=`-0.75` | Regime=`BEARISH ABSORPTION`
  * 1h Bar: Delta=`+131,590.82 USD` | Delta %=`+14.65%` | Z-Score=`+0.27` | Regime=`DELTA ALIGNED`
  * 4h Bar: Delta=`+1,383,933.19 USD` | Delta %=`+16.99%` | Z-Score=`+1.25` | Regime=`AGGRESSIVE BUYING`
  * 30D Consolidated (ALL): Cumulative Trend=`-1,919,037.96 USD` | Long-Term Regime=`AGGRESSIVE BUYING`
- **Institutional Footprint & Deribit Options Armor (21_Tradfye_Orderflow.parquet)**:
  * Candle VWAP: `281.52071` | Estimated POC: `281.73000` | Avg Trade Size: `153.34 USD`
  * Net Delta USD: `+41,861.00 USD` | Net Delta %: `+8.03%` | Orderflow CVD: `+41,861.00 USD`
  * Orderflow Regime: **`TWO_SIDED_ABSORPTION`** | Orderflow Divergence: **`BULLISH_EXPANSION`**
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
- **Hyperliquid Elite Trader Positioning (4_Hyperliquid_Analysis.parquet)**:
  * Wallet `0x12d20c0196...` (0x12d2...f97f): `Long` `1,014,721.23 USD` (3,627.2430 BCH, Margin: 101,472.12 USD, Leverage: 10X Cross, Entry: 303.2600 USD, Current: 279.4200 USD, Est Liq: 0.00 USD, PnL: -85,278.11 USD [-8.40%], Fees: +6,565.69 USD)

---

## 6. Liquidation Max Pain, Heatmaps & Cascade Boundaries
*(Sources: 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 14_Hyperdash_Liq_Map.parquet, 14_Liquidation_Matrix.parquet, 15_Hyperdash_Stops_Map.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`290.27000` (Vol: `199,700 USD`, Dist: `+3.69%`) | Long MP=`271.71000` (Vol: `159,600 USD`, Dist: `-2.94%`)
  * 48H Horizon: Short MP=`290.32000` (Vol: `213,700 USD`, Dist: `+3.71%`) | Long MP=`271.85000` (Vol: `166,000 USD`, Dist: `-2.89%`)
  * 3D Horizon: Short MP=`290.32000` (Vol: `213,700 USD`, Dist: `+3.71%`) | Long MP=`274.67000` (Vol: `204,600 USD`, Dist: `-1.88%`)
  * 7D Horizon: Short MP=`290.28000` (Vol: `199,700 USD`, Dist: `+3.69%`) | Long MP=`263.68000` (Vol: `297,200 USD`, Dist: `-5.81%`)
- **Exchange Cumulative Liquidation Cascades (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
  * 1D Cascade: Total=`8.10M USD` | Short Liq Pool=`8.10M USD` | Long Liq Pool=`0 USD` | Venues: Binance=`4.64K USD`, OKX=`3.36K USD`, Bybit=`4.26K USD`
  * 7D Cascade: Total=`10.81M USD` | Short Liq Pool=`10.81M USD` | Long Liq Pool=`0 USD` | Venues: Binance=`40.67K USD`, OKX=`0 USD`, Bybit=`0 USD`
- **Cross-Venue Liquidation Matrix & Heatmaps (14_Liquidation_Matrix.parquet, 7_Liq_Heapmap.parquet)**:
  * Liquidation Matrix Strike: Price=`533.50000` | Vol=`178 USD` | Cumulative=`125,340 USD` | Venue=`Hyperliquid L1` | Side=`Short Liquidation`
  * Multi-Timeframe Heatmap Density: 1h=`0.00 USD` | 4h=`0.00 USD` | 12h=`584.43K USD` | 24h=`1.29M USD`
- **Hyperdash Real-Time Liquidation & Retail Stop Protection (14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet)**:
  * Hyperdash Liq Cluster: Mark=`278.7100 USD` | Cluster Price=`533.5000 USD` | Dist=`+91.42%` | Cumulative=`125.34K USD` | Short=`177.66 USD` | Long=`0 USD` | Size=`0.3330 BCH`
  * **Retail Stops Map (Pitfall 2 & 4 Defense)**:
    - `Sell Stop`: `143.5000 USD` (Dist: `-48.51%`, Cumulative Stops: `253.63K USD`, Buy: `0 USD`, Sell: `210.94 USD`, Coins: `1.4700 BCH`)
    - `Sell Stop`: `145.5000 USD` (Dist: `-47.80%`, Cumulative Stops: `253.42K USD`, Buy: `0 USD`, Sell: `2.07K USD`, Coins: `14.2000 BCH`)
    - `Sell Stop`: `178.5000 USD` (Dist: `-35.95%`, Cumulative Stops: `251.36K USD`, Buy: `0 USD`, Sell: `2.53K USD`, Coins: `14.1670 BCH`)
- **Live Forced Liquidation Momentum (7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)**:
  * Real-Time Stream: Coin=`BCHUSDT` | Side=`Long` | Price=`289.68 USD` | Amount=`7.87K USD` | Exchange=`Binance` | Time=`2026-10-28 21:50:17 IST`
  * Multi-Timeframe Forced Aggregates (5m): Long Liq=`16,500.00 USD` | Short Liq=`0.00 USD` | Total=`16,500.00 USD` | Net Delta=`-16,500.00 USD` | Dominant=`LONGS_FLUSHED`

---

## 7. Derivatives Sentiment, Open Interest & Funding Dynamics
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet, 6_Funding_Fee_Settlement.parquet, 13_Hyperliquid.parquet)*
- **Aggregated Open Interest Breakdown (5_OI.parquet)**:
  * Total Open Interest: `307.70M USD` (`1,101,520.6 BCH`) | OI / 24h Volume Ratio: `0.8107`
  * OI Expansion Rate: 1h Change=`+0.64%` | 4h Change=`+0.87%` | 24h Change=`-8.73%`
  * Venue Concentration:
    - Binance: `90.84M USD` | Bybit: `38.13M USD` | OKX: `24.52M USD` | CME Institutional: `0.00 USD`
    - Gate: `53.07M USD` | MEXC: `19.14M USD` | Hyperliquid DEX: `7.75M USD` | Bitget: `18.73M USD`
    - KuCoin: `12.51M USD` | BingX: `8.44M USD` | Bitunix: `3.46M USD` | Others: `31.11M USD`
- **Cross-Exchange Perpetual Funding Rates (5_Funding_Rate.parquet)**:
  * Major CEX Rates: Binance=`+0.0034%` | OKX=`+0.0100%` | Bybit=`+0.0100%` | Bitget=`+0.0060%`
  * Mid-Tier CEX Rates: KuCoin=`+0.0084%` | MEXC=`+0.0034%` | Gate=`+0.0100%` | BingX=`+0.0100%` | Bitunix=`+0.0036%`
  * Alternative Venues: WhiteBIT=`+0.0100%` | LBank=`+0.0034%` | tradeXYZ=`-`
  * Inverse Coin-Margined: CoinM Binance=`+0.0050%` | CoinM OKX=`+0.0100%` | CoinM Bybit=`+0.0100%`
- **Exchange Long / Short Ratio Dynamics (3_Exchanges_LS_Ratio*.parquet)**:
  * 15m Tactical: L/S Ratio=`0.68` (Longs: `40.57%`, Shorts: `59.43%`, Total Vol: `3.65M USD`)
  * 1h Primary: L/S Ratio=`0.84` (Longs: `45.58%`, Shorts: `54.42%`, Total Vol: `16.87M USD`)
  * 4h Macro: L/S Ratio=`0.93` (Longs: `48.15%`, Shorts: `51.85%`, Total Vol: `101.21M USD`)
- **Funding Fee Settlement & DEX Arbitrage (6_Funding_Fee_Settlement.parquet, 13_Hyperliquid.parquet)**:
  * Settlement Payouts: Current Expected=`8.92K USD` | Last 24h=`10.97K USD` | Last 3D=`85.53K USD` | Last 7D=`126.00K USD`

---

## 8. Microstructure Footprint, Tape Imbalances & Macro Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 16_Hyperdash_telegram_Intel.parquet, 19_News.parquet, 19_Calendar.parquet)*
- **Bar-by-Bar Microstructure Footprint (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
  * Venue Source: `CoinGlass-AggregatedFutures(Binance)` | Timeframe: `15m` | Last Price: `279.40000`
  * Footprint Auction Profile: Bar VWAP=`278.95604` | Bar POC=`278.76500` | Bar VAH=`279.36500` | Bar VAL=`278.46500`
  * Orderflow Volumes: Total Vol=`807,924.95 USD` | Taker Buy=`459,310.58 USD` | Taker Sell=`348,614.37 USD`
  * Bar Delta Profile: Delta=`+110,696.21 USD` (`+13.70%`) | Max Delta=`+111,268.02 USD` | Min Delta=`-45,743.54 USD` | Cumulative Bar Delta=`+1,353,390.93 USD`
  * Order Execution Dynamics: Trades Count=`5,164` | Avg Trade Size=`156.45 USD`
  * Tape Imbalances: Imbalance Ratio=`300.0%` | Buy Imbalances Count=`24` | Sell Imbalances Count=`21`
  * Footprint Open Interest: Bar OI=`0.00 USD` | Bar OI Change=`+0.00 USD`
- **CoinGlass Algorithmic Footprint Signals (25_CoinGlass_Footprint_Signals.parquet)**:
  * Signal Classification: Type=`Exhaustion` | Bias: **`BULLISH`** | Signal Time=`10-28 06:21` | Timeframe=`Range 1`
  * Signal Context: Headline=`Seller exhaustion` | Price Level=`293.97000` | Absorbed Volume=`0.00 USD`
  * Bar Footprint Context: Current Bar Delta=`+0.00 USD` | Current Bar Volume=`0.00 USD` | Delta in View=`+0.00 USD`
  * Historical Detail: `New 10-bar low with almost no volume in the bottom 10% of the bar, closed in the upper half, bullish · 293.97` | KPI=`—` | Bias=`—`
- **Multi-Horizon Macro Capital Netflows (2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet)**:
  * Spot Capital Netflows:
    - Tactical: 5m=`-1.81K` | 15m=`+2.78K` | 30m=`+6.53K` | 1h=`+50.73K`
    - Intermediate: 2h=`+30.26K` | 4h=`-93.18K` | 6h=`-48.18K` | 8h=`-72.99K` | 12h=`-614.72K` | 24h=`-2.34M`
    - Macro Horizons: 1-Week=`-257.03K` | 15-Day=`+2.16M` | 30-Day=`-14.40M` | Market Cap=`5.61B`
  * Futures Capital Netflows:
    - Tactical: 5m=`-85.50K` | 15m=`+243.23K` | 30m=`+21.07K` | 1h=`+901.48K`
    - Intermediate: 2h=`+1.58M` | 4h=`+1.53M` | 6h=`+1.24M` | 8h=`-681.93K` | 12h=`-1.18M` | 24h=`-8.11M`
    - Macro Horizons: 1-Week=`-11.04M` | 15-Day=`-31.92M` | 30-Day=`-138.38M` | Market Cap=`5.61B`

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
- **Stand-Aside Reason**: Absence of statistically validated auction edge and defending resting armor. Standing aside preserves statutory hard floor.