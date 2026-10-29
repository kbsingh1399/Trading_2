# 🔬 MASTER 43-FEED QUANTITATIVE DOSSIER: BNB (BNB)
**MT5 Symbol**: `BNBUSD.p` | **Category**: `Crypto Major` | **Tier**: `Tier 1`
**Execution Posture**: `PASSIVE LIMIT ONLY` | **Timestamp**: 2026-10-29 14:43:14 UTC
**Pipeline Clearance**: `QUALIFIED` | **Data Freshness**: `1.2m`

---

## 1. MT5 Live Broker Telemetry & Spread Friction Gate
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet)*
- **Live Bid Quote**: `743.00000` | **Live Ask Quote**: `743.70000` | **Mid Price**: `743.35000`
- **Spread Points**: `70.0 pts` | **Spread BPS**: `9.42 bps` (Mandatory Cap: `25.0 bps`)
- **Gate Status**: **`PASS`** (Spread friction within mandatory threshold; safe for maker execution)
- **Order Allowed**: `BUY_LIMIT / SELL_LIMIT` | **Pillar 1 Clearance**: `QUALIFIED`
- **Broker Specifications**: Contract Size=`1.00` | Tick Value=`1.00 USD` | Min Lot=`0.01` | Digits=`5`
- **Account Capital Context**: Balance=`4,744.55 USD` | Equity=`4,744.32 USD` | Free Margin=`4,342.62 USD` | Inviolate Hard Floor=`4,775.00 USD` (Cushion: `-30.68 USD`)
- **Pipeline Health**: Feed #00 Status=`PASS` | Overall Pipeline Telemetry=`33/33 FEEDS PASS (SYNCHRONIZED)`

---

## 2. Technical Profile, Multi-Sigma VWAP Dispersion & Volatility
*(Sources: 11_Technical.parquet, 11_Technical_BTC_Ribbon.parquet)*
- **Last Verified Price**: `743.70000` | **24h Change**: `-0.59%` (24h High: `759.80000`, 24h Low: `737.00000`)
- **Weekly Range**: Week High=`760.90000` | Week Low=`732.50000` | Daily POC=`741.03000` | Daily VAH=`751.67000` | Daily VAL=`738.44000`
- **Session VWAP**: `746.82576` | **Rolling 24h VWAP**: `748.33401` | **Distance to VWAP**: `-0.42%`
- **VWAP Z-Score**: `-0.57 sigma` | **Mean Reversion Bias**: **`FAIR VALUE`**
- **VWAP Dispersion Bands**:
  * +1.00 sigma: `752.35394` | -1.00 sigma: `741.29758`
  * +1.28 sigma (80% CI): `753.90183` | -1.28 sigma: `739.74968`
  * +2.00 sigma (95% CI): `757.88212` | -2.00 sigma: `735.76939`
  * +2.01 sigma: `757.93740` | -2.01 sigma: `735.71411`
  * +2.51 sigma (98.8% CI): `760.70149` | -2.51 sigma: `732.95002`
  * +3.00 sigma (99.7% CI Extreme): `763.41030` | -3.00 sigma: `730.24121`
- **Oscillators & Volatility**:
  * **RSI (14)**: `50.33` | **RSI State**: **`NEUTRAL`**
  * **ATR (14)**: `2.38310` | **ATR %**: `0.32%`
  * **Bollinger Bands**: Upper=`749.51210` | Mid=`742.09000` | Lower=`734.66790` | Bandwidth=`2.00%`
  * **MACD**: Line=`-1.8011` | Signal=`-2.4198` | Hist=`+0.6186`
- **Exponential Moving Average Ribbon (EMA)**:
  * Short Horizon: EMA-5=`742.02264` | EMA-9=`741.54357` | EMA-13=`741.73353` | EMA-20=`742.61918`
  * Intermediate: EMA-34=`744.42970` | EMA-50=`745.86335` | EMA-89=`747.38137` | EMA-100=`747.52687`
  * Institutional: EMA-144=`747.41132` | EMA-200=`746.48669` (Slope: `-0.107%`) | EMA-233=`745.84216` (Slope: `-0.081%`)
  * **Trend Bias**: **`NEUTRAL / CHOP`**

---

## 3. Auction Market Structure & Value Profile
*(Sources: 20_Auction_Market_Structure.parquet)*
- **Daily Auction Value Area**:
  * High (VAH): `751.67000` | Point of Control (POC): `741.03000` | Low (VAL): `738.44000`
  * Distance to POC: `+0.31%` | Distance to VAH: `-1.11%` | Distance to VAL: `+0.66%`
  * **Value Area Position**: **`INSIDE_VALUE (Balance)`** | **Auction Regime**: **`ROTATIONAL_BALANCE`** | **Session Bias**: **`BEARISH (Below Pivot)`**
- **Prior Day & Weekly Auction Profile**:
  * Prior Day: PD VAH=`752.98000` | PD POC=`743.64000` | PD VAL=`742.97000` | PDH=`760.90000` | PDL=`740.60000` | PDC=`754.40000`
  * Monday Reference: Monday High=`746.00000` | Monday Low=`730.90000` | Monday Mid=`738.45000`
  * Weekly Value Area: Weekly VAH=`748.80000` | Weekly POC=`741.00000` | Weekly VAL=`734.60000`
  * Multi-Week Extremes: Current Week High (CWH)=`760.90000` | CWL=`730.90000` | Prior Week High (PWH)=`750.90000` | PWL=`707.00000`
  * Multi-Month Extremes: Current Month High (CMH)=`809.50000` | CML=`704.50000` | Prior Month High (PMH)=`807.20000` | PML=`674.10000`
- **Session Liquidity Extremes & Initial Balance**:
  * Asian Session: Range `[743.20000 - 759.80000]`
  * London Session: Range `[737.00000 - 758.10000]`
  * New York Session: Range `[737.00000 - 748.40000]`
  * Initial Balance (IB): IB High=`758.10000` | IB Low=`753.70000`
- **Fibonacci Golden Pocket & Optimal Trade Entry (OTE)**:
  * Swing Range: High=`759.80000` | Low=`737.00000` | Direction=`BEARISH_IMPULSE`
  * Golden Pocket [0.618 - 0.65]: `[751.09000 - 751.82000]`
  * Optimal Trade Entry (0.702): `753.01000` | Invalidation Level: `754.92000` | Status: **`SHALLOW_RETRACE`**
- **Classical & Weekly Pivots**:
  * Daily Classical: Pivot=`751.97000` | R1=`763.33000` | S1=`743.03000` | R2=`772.27000` | S2=`731.67000`
  * Weekly Classical: Weekly Pivot=`732.43000` | Weekly R1=`757.87000` | Weekly S1=`713.97000`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Orderflow
*(Sources: 18_CVD.parquet, 18_CVD_30D_5m.parquet, 18_CVD_30D_15m.parquet, 18_CVD_30D_1h.parquet, 18_CVD_30D_4h.parquet, 18_CVD_30D_ALL.parquet, 21_Tradfye_Orderflow.parquet)*
- **Primary 15m CVD Microstructure (18_CVD_30D_15m.parquet)**:
  * Candle Delta: `-977,763.22 USD` (Base: `-1,313.3900 coins`) | Delta %: `-20.21%`
  * Taker Volumes: Taker Buy=`1,930,230.92 USD` | Taker Sell=`2,907,994.14 USD` | Total Vol=`6,496.73 USD`
  * Cumulative CVD: `-13,499,381.09 USD` (Base: `-17,726.5300`)
  * Rolling CVD Z-Score: `-0.47 sigma` | Price Return: `-0.08%`
  * **Delta Regime**: **`AGGRESSIVE SELLING`** | Trades Count: `12,700`
- **Multi-Timeframe Delta Comparison**:
  * 5m Bar: Delta=`-43,447.50 USD` | Delta %=`-3.08%` | Z-Score=`-0.70` | Regime=`BEARISH ABSORPTION`
  * 1h Bar: Delta=`-977,763.22 USD` | Delta %=`-20.21%` | Z-Score=`-0.09` | Regime=`AGGRESSIVE SELLING`
  * 4h Bar: Delta=`+10,057,115.74 USD` | Delta %=`+16.75%` | Z-Score=`+1.79` | Regime=`AGGRESSIVE BUYING`
  * 30D Consolidated (ALL): Cumulative Trend=`-13,957,538.70 USD` | Long-Term Regime=`AGGRESSIVE BUYING`
- **Institutional Footprint & Deribit Options Armor (21_Tradfye_Orderflow.parquet)**:
  * Candle VWAP: `747.17067` | Estimated POC: `747.24250` | Avg Trade Size: `479.07 USD`
  * Net Delta USD: `-991,202.15 USD` | Net Delta %: `-26.83%` | Orderflow CVD: `-991,202.15 USD`
  * Orderflow Regime: **`AGGRESSIVE_SELLER_DOMINATION`** | Orderflow Divergence: **`BEARISH_EXPANSION`**
  * Deribit Options Walls: Max Pain=`0.00` | Call Wall=`0.00` | Put Wall=`0.00`

---

## 5. Institutional Whale Armor & Resting Orderbook Depth
*(Sources: 10_Whale_Orders.parquet, 12_Hyperdash.parquet, 17_Orderbook.parquet, 4_Hyperliquid_Analysis.parquet)*
- **Defending Resting Whale Walls (10_Whale_Orders.parquet)**:
  * Defending Bid Wall: `740.81000` (`1403.8687` coins / `1,040,000.00 USD` on `Hyperliquid`, persistent for `5m 54s`, Traded: `0.0%`, Order ID: `CG_WHALE_BNB_T_62`)
  * Defending Ask Wall: `747.22000` (`1405.2086` coins / `1,050,000.00 USD` on `Hyperliquid`, persistent for `9m 18s`, Traded: `0.0%`, Order ID: `CG_WHALE_BNB_T_29`)
  * Total Whale Armor Pool: Bids Pool=`19,783,100.00 USD` | Asks Pool=`21,208,400.00 USD` (Tracked Orders: `182`)
- **Hyperdash Resting Depth & L3 Telemetry (12_Hyperdash.parquet)**:
  * `NEUTRAL`: `0.00 USD` @ `0.00000` (Size: `0.0`, Detail: Delta: +0, Wallet: None, Timestamp: 2026-10-29 19:44:05 IST)
- **Consolidated L2 Orderbook Depth & Skew (17_Orderbook.parquet)**:
  * `ASK`: `2,164.39 USD` @ `744.80 USD` (Coins: 2.9060 BNB, Cumulative: 34,217.71 USD, Tier: 4 orders, Dist: +0.04%, Bias: B/A: 77.3% / 22.7%)
  * `ASK`: `7,917.86 USD` @ `744.79 USD` (Coins: 10.6310 BNB, Cumulative: 32,053.32 USD, Tier: 2 orders, Dist: +0.04%, Bias: B/A: 77.3% / 22.7%)
  * `ASK`: `4,393.34 USD` @ `744.76 USD` (Coins: 5.8990 BNB, Cumulative: 24,135.46 USD, Tier: 1 orders, Dist: +0.04%, Bias: B/A: 77.3% / 22.7%)
- **Hyperliquid Elite Trader Positioning (4_Hyperliquid_Analysis.parquet)**:
  * Wallet `0xea0027b6ea...` (0xea00...a918): `Long` `3,051,136.95 USD` (4,098.4290 BNB, Margin: 610,227.39 USD, Leverage: 5X Cross, Entry: 787.2350 USD, Current: 744.1900 USD, Est Liq: 0.00 USD, PnL: -175,289.84 USD [-5.75%], Fees: +13,078.22 USD)
  * Wallet `0xb69eec8fea...` (0xb69e...033a): `Long` `2,087,812.98 USD` (2,805.7100 BNB, Margin: 208,781.30 USD, Leverage: 10X Cross, Entry: 772.9380 USD, Current: 744.1900 USD, Est Liq: 585.1495 USD, PnL: -80,829.60 USD [-3.87%], Fees: +6,347.74 USD)
  * Wallet `0xcac19662ec...` (0xcac1...26b3): `Long` `2,076,554.08 USD` (2,789.0430 BNB, Margin: 207,655.41 USD, Leverage: 10X Cross, Entry: 679.9140 USD, Current: 744.1900 USD, Est Liq: 0.00 USD, PnL: +180,242.91 USD [+8.68%], Fees: +29,858.59 USD)

---

## 6. Liquidation Max Pain, Heatmaps & Cascade Boundaries
*(Sources: 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 14_Hyperdash_Liq_Map.parquet, 14_Liquidation_Matrix.parquet, 15_Hyperdash_Stops_Map.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`758.31000` (Vol: `2,400,000 USD`, Dist: `+1.76%`) | Long MP=`737.63000` (Vol: `2,000,000 USD`, Dist: `-1.02%`)
  * 48H Horizon: Short MP=`758.54000` (Vol: `2,400,000 USD`, Dist: `+1.79%`) | Long MP=`736.45000` (Vol: `2,500,000 USD`, Dist: `-1.18%`)
  * 3D Horizon: Short MP=`766.52000` (Vol: `2,500,000 USD`, Dist: `+2.86%`) | Long MP=`736.48000` (Vol: `3,000,000 USD`, Dist: `-1.17%`)
  * 7D Horizon: Short MP=`758.15000` (Vol: `2,900,000 USD`, Dist: `+1.73%`) | Long MP=`728.45000` (Vol: `3,700,000 USD`, Dist: `-2.25%`)
- **Exchange Cumulative Liquidation Cascades (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
  * 1D Cascade: Total=`33.66M USD` | Short Liq Pool=`33.66M USD` | Long Liq Pool=`0 USD` | Venues: Binance=`47.09K USD`, OKX=`0 USD`, Bybit=`0 USD`
  * 7D Cascade: Total=`71.75M USD` | Short Liq Pool=`71.75M USD` | Long Liq Pool=`0 USD` | Venues: Binance=`43.11K USD`, OKX=`0 USD`, Bybit=`0 USD`
- **Cross-Venue Liquidation Matrix & Heatmaps (14_Liquidation_Matrix.parquet, 7_Liq_Heapmap.parquet)**:
  * Liquidation Matrix Strike: Price=`1472.50000` | Vol=`9,020 USD` | Cumulative=`8,820,000 USD` | Venue=`Hyperliquid L1` | Side=`Short Liquidation`
  * Multi-Timeframe Heatmap Density: 1h=`0.00 USD` | 4h=`0.00 USD` | 12h=`0.00 USD` | 24h=`1.16M USD`
- **Hyperdash Real-Time Liquidation & Retail Stop Protection (14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet)**:
  * Hyperdash Liq Cluster: Mark=`745.3600 USD` | Cluster Price=`1,472.50 USD` | Dist=`+97.56%` | Cumulative=`8.82M USD` | Short=`9.02K USD` | Long=`0 USD` | Size=`6.1240 BNB`
  * **Retail Stops Map (Pitfall 2 & 4 Defense)**:
    - `Sell Stop`: `300.5000 USD` (Dist: `-59.68%`, Cumulative Stops: `1.67M USD`, Buy: `0 USD`, Sell: `2.40K USD`, Coins: `8.0000 BNB`)
    - `Sell Stop`: `333.5000 USD` (Dist: `-55.26%`, Cumulative Stops: `1.67M USD`, Buy: `0 USD`, Sell: `333.50 USD`, Coins: `1.0000 BNB`)
    - `Sell Stop`: `350.5000 USD` (Dist: `-52.98%`, Cumulative Stops: `1.67M USD`, Buy: `0 USD`, Sell: `127.58 USD`, Coins: `0.3640 BNB`)
- **Live Forced Liquidation Momentum (7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)**:
  * Multi-Timeframe Forced Aggregates (5m): Long Liq=`0.00 USD` | Short Liq=`0.00 USD` | Total=`0.00 USD` | Net Delta=`0.00 USD` | Dominant=`BALANCED`

---

## 7. Derivatives Sentiment, Open Interest & Funding Dynamics
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet, 6_Funding_Fee_Settlement.parquet, 13_Hyperliquid.parquet)*
- **Aggregated Open Interest Breakdown (5_OI.parquet)**:
  * Total Open Interest: `1.24B USD` (`1,667,059.9 BNB`) | OI / 24h Volume Ratio: `0.9078`
  * OI Expansion Rate: 1h Change=`-0.34%` | 4h Change=`-1.50%` | 24h Change=`-1.83%`
  * Venue Concentration:
    - Binance: `584.69M USD` | Bybit: `106.69M USD` | OKX: `54.80M USD` | CME Institutional: `0.00 USD`
    - Gate: `171.31M USD` | MEXC: `70.17M USD` | Hyperliquid DEX: `46.40M USD` | Bitget: `69.10M USD`
    - KuCoin: `23.75M USD` | BingX: `32.48M USD` | Bitunix: `14.55M USD` | Others: `66.56M USD`
- **Cross-Exchange Perpetual Funding Rates (5_Funding_Rate.parquet)**:
  * Major CEX Rates: Binance=`+0.0000%` | OKX=`+0.0089%` | Bybit=`+0.0100%` | Bitget=`+0.0100%`
  * Mid-Tier CEX Rates: KuCoin=`+0.0100%` | MEXC=`+0.0000%` | Gate=`+0.0100%` | BingX=`+0.0100%` | Bitunix=`+0.0015%`
  * Alternative Venues: WhiteBIT=`-0.0188%` | LBank=`+0.0000%` | tradeXYZ=`-`
  * Inverse Coin-Margined: CoinM Binance=`+0.0133%` | CoinM OKX=`+0.0000%` | CoinM Bybit=`+0.0000%`
- **Exchange Long / Short Ratio Dynamics (3_Exchanges_LS_Ratio*.parquet)**:
  * 15m Tactical: L/S Ratio=`1.25` (Longs: `55.57%`, Shorts: `44.43%`, Total Vol: `22.42M USD`)
  * 1h Primary: L/S Ratio=`1.06` (Longs: `51.39%`, Shorts: `48.61%`, Total Vol: `106.42M USD`)
  * 4h Macro: L/S Ratio=`0.95` (Longs: `48.72%`, Shorts: `51.28%`, Total Vol: `6.26B USD`)
- **Funding Fee Settlement & DEX Arbitrage (6_Funding_Fee_Settlement.parquet, 13_Hyperliquid.parquet)**:
  * Settlement Payouts: Current Expected=`15.17K USD` | Last 24h=`107.98K USD` | Last 3D=`310.56K USD` | Last 7D=`375.06K USD`

---

## 8. Microstructure Footprint, Tape Imbalances & Macro Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 16_Hyperdash_telegram_Intel.parquet, 19_News.parquet, 19_Calendar.parquet)*
- **Bar-by-Bar Microstructure Footprint (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
  * Venue Source: `CoinGlass-AggregatedFutures(Binance)` | Timeframe: `15m` | Last Price: `743.35000`
  * Footprint Auction Profile: Bar VWAP=`744.82253` | Bar POC=`744.15000` | Bar VAH=`745.95000` | Bar VAL=`743.55000`
  * Orderflow Volumes: Total Vol=`3,757,094.11 USD` | Taker Buy=`1,329,538.27 USD` | Taker Sell=`2,427,555.84 USD`
  * Bar Delta Profile: Delta=`-1,098,017.56 USD` (`-29.23%`) | Max Delta=`+14,404.37 USD` | Min Delta=`-1,098,017.56 USD` | Cumulative Bar Delta=`+12,826,174.30 USD`
  * Order Execution Dynamics: Trades Count=`10,005` | Avg Trade Size=`375.52 USD`
  * Tape Imbalances: Imbalance Ratio=`300.0%` | Buy Imbalances Count=`0` | Sell Imbalances Count=`1`
  * Footprint Open Interest: Bar OI=`0.00 USD` | Bar OI Change=`+0.00 USD`
- **CoinGlass Algorithmic Footprint Signals (25_CoinGlass_Footprint_Signals.parquet)**:
  * Signal Classification: Type=`Trapped longs` | Bias: **`BEARISH`** | Signal Time=`10-28 09:02` | Timeframe=`Volume 10K BNB`
  * Signal Context: Headline=`Failed breakout` | Price Level=`749.29000` | Absorbed Volume=`1,800.00 USD`
  * Bar Footprint Context: Current Bar Delta=`+0.00 USD` | Current Bar Volume=`0.00 USD` | Delta in View=`+0.00 USD`
  * Historical Detail: `Broke the 5-bar high on 1.8K of taker buying at the top, then fell back into the lower part of the bar 1 bars later. Breakout buyers trapped, bearish · 749.29` | KPI=`—` | Bias=`—`
- **Multi-Horizon Macro Capital Netflows (2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet)**:
  * Spot Capital Netflows:
    - Tactical: 5m=`+94.87K` | 15m=`+469.32K` | 30m=`+1.21M` | 1h=`+1.75M`
    - Intermediate: 2h=`-2.77M` | 4h=`-12.70M` | 6h=`-9.50M` | 8h=`-3.54M` | 12h=`+264.00K` | 24h=`+3.62M`
    - Macro Horizons: 1-Week=`-29.29M` | 15-Day=`-96.73M` | 30-Day=`-125.25M` | Market Cap=`97.76B`
  * Futures Capital Netflows:
    - Tactical: 5m=`-1.10M` | 15m=`-484.95K` | 30m=`-101.95K` | 1h=`+5.49M`
    - Intermediate: 2h=`+9.26M` | 4h=`+4.71M` | 6h=`-7.42M` | 8h=`-14.67M` | 12h=`-15.50M` | 24h=`-20.97M`
    - Macro Horizons: 1-Week=`-45.50M` | 15-Day=`-77.80M` | 30-Day=`-367.68M` | Market Cap=`97.76B`

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
- **Sovereign Gate Decision**: **`STANDBY_RADAR`**
- **Dynamic Capacity Verification**: Active Open=`0` | Resting Pending=`2` | Capacity Check: `N_open + N_pending <= 3` (**`PASS`**)
- **Triple Floor Solvency Check**: Current Equity=`4,744.32 USD` | Hard Floor=`4,775.00 USD` | Buffer=`-30.68 USD` | Solvency Check: **`DEFENSE_MODE`**
- **Autonomous Limit Order Formulation (If Admitted)**:
```json
{
  "ticket": "PENDING_DISPATCH",
  "direction": "BUY_LIMIT",
  "lots": 0.05,
  "entry": 736.5,
  "sl": 730.0,
  "tp": 756.0,
  "risk_usd": 3.25,
  "rr": 3.0,
  "model": "MODEL_1_FADE",
  "thesis": "Defending bid wall and 7D Max Pain zone."
}
```
- **Stand-Aside Reason**: Radar monitoring defending bid wall.