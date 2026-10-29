# 🔬 MASTER 43-FEED QUANTITATIVE DOSSIER: ZECUSD (Zcash / USD)
**MT5 Symbol**: `ZECUSD.p` | **Category**: `Crypto Altcoin` | **Tier**: `Tier 2`
**Execution Posture**: `PASSIVE LIMIT ONLY` | **Timestamp**: 2026-10-29 14:43:14 UTC
**Pipeline Clearance**: `QUALIFIED` | **Data Freshness**: `1.2m`

---

## 1. MT5 Live Broker Telemetry & Spread Friction Gate
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet)*
- **Live Bid Quote**: `1278.53000` | **Live Ask Quote**: `1279.33000` | **Mid Price**: `1278.93000`
- **Spread Points**: `80.0 pts` | **Spread BPS**: `6.26 bps` (Mandatory Cap: `25.0 bps`)
- **Gate Status**: **`PASS`** (Spread friction within mandatory threshold; safe for maker execution)
- **Order Allowed**: `BUY_LIMIT / SELL_LIMIT` | **Pillar 1 Clearance**: `QUALIFIED`
- **Broker Specifications**: Contract Size=`1.00` | Tick Value=`1.00 USD` | Min Lot=`0.01` | Digits=`5`
- **Account Capital Context**: Balance=`4,744.55 USD` | Equity=`4,744.32 USD` | Free Margin=`4,342.62 USD` | Inviolate Hard Floor=`4,775.00 USD` (Cushion: `-30.68 USD`)
- **Pipeline Health**: Feed #00 Status=`PASS` | Overall Pipeline Telemetry=`33/33 FEEDS PASS (SYNCHRONIZED)`

---

## 2. Technical Profile, Multi-Sigma VWAP Dispersion & Volatility
*(Sources: 11_Technical.parquet, 11_Technical_BTC_Ribbon.parquet)*
- **Last Verified Price**: `1275.55000` | **24h Change**: `-0.31%` (24h High: `1318.68000`, 24h Low: `1230.00000`)
- **Weekly Range**: Week High=`1328.99000` | Week Low=`1210.62000` | Daily POC=`1245.67000` | Daily VAH=`1278.18000` | Daily VAL=`1230.30000`
- **Session VWAP**: `1258.64549` | **Rolling 24h VWAP**: `1271.22390` | **Distance to VWAP**: `+1.34%`
- **VWAP Z-Score**: `+0.85 sigma` | **Mean Reversion Bias**: **`FAIR VALUE`**
- **VWAP Dispersion Bands**:
  * +1.00 sigma: `1278.53460` | -1.00 sigma: `1238.75637`
  * +1.28 sigma (80% CI): `1284.10356` | -1.28 sigma: `1233.18742`
  * +2.00 sigma (95% CI): `1298.42372` | -2.00 sigma: `1218.86725`
  * +2.01 sigma: `1298.62261` | -2.01 sigma: `1218.66836`
  * +2.51 sigma (98.8% CI): `1308.56717` | -2.51 sigma: `1208.72380`
  * +3.00 sigma (99.7% CI Extreme): `1318.31284` | -3.00 sigma: `1198.97814`
- **Oscillators & Volatility**:
  * **RSI (14)**: `58.56` | **RSI State**: **`BULLISH`**
  * **ATR (14)**: `9.80503` | **ATR %**: `0.77%`
  * **Bollinger Bands**: Upper=`1285.37861` | Mid=`1264.24450` | Lower=`1243.11039` | Bandwidth=`3.34%`
  * **MACD**: Line=`+6.5427` | Signal=`+5.0657` | Hist=`+1.4770`
- **Exponential Moving Average Ribbon (EMA)**:
  * Short Horizon: EMA-5=`1275.19765` | EMA-9=`1272.68897` | EMA-13=`1269.94742` | EMA-20=`1266.08378`
  * Intermediate: EMA-34=`1262.90482` | EMA-50=`1263.46041` | EMA-89=`1268.34693` | EMA-100=`1269.42667`
  * Institutional: EMA-144=`1270.58933` | EMA-200=`1267.40357` (Slope: `+0.035%`) | EMA-233=`1266.55593` (Slope: `+0.037%`)
  * **Trend Bias**: **`BULLISH`**

---

## 3. Auction Market Structure & Value Profile
*(Sources: 20_Auction_Market_Structure.parquet)*
- **Daily Auction Value Area**:
  * High (VAH): `1278.18000` | Point of Control (POC): `1245.67000` | Low (VAL): `1230.30000`
  * Distance to POC: `+2.68%` | Distance to VAH: `+0.07%` | Distance to VAL: `+3.97%`
  * **Value Area Position**: **`ABOVE_VALUE (Imbalance)`** | **Auction Regime**: **`RANGE_EXPANSION`** | **Session Bias**: **`BEARISH (Below Pivot)`**
- **Prior Day & Weekly Auction Profile**:
  * Prior Day: PD VAH=`1320.44000` | PD POC=`1312.10000` | PD VAL=`1285.78000` | PDH=`1328.99000` | PDL=`1263.19000` | PDC=`1296.46000`
  * Monday Reference: Monday High=`1267.53000` | Monday Low=`1176.75000` | Monday Mid=`1222.14000`
  * Weekly Value Area: Weekly VAH=`1289.92000` | Weekly POC=`1238.15000` | Weekly VAL=`1195.53000`
  * Multi-Week Extremes: Current Week High (CWH)=`1328.99000` | CWL=`1176.75000` | Prior Week High (PWH)=`1367.38000` | PWL=`1062.01000`
  * Multi-Month Extremes: Current Month High (CMH)=`1448.46000` | CML=`1048.03000` | Prior Month High (PMH)=`1694.42000` | PML=`787.75000`
- **Session Liquidity Extremes & Initial Balance**:
  * Asian Session: Range `[1230.00000 - 1318.68000]`
  * London Session: Range `[1233.52000 - 1276.13000]`
  * New York Session: Range `[1250.65000 - 1287.09000]`
  * Initial Balance (IB): IB High=`1255.79000` | IB Low=`1245.43000`
- **Fibonacci Golden Pocket & Optimal Trade Entry (OTE)**:
  * Swing Range: High=`1318.68000` | Low=`1230.00000` | Direction=`BEARISH_IMPULSE`
  * Golden Pocket [0.618 - 0.65]: `[1284.80000 - 1287.64000]`
  * Optimal Trade Entry (0.702): `1292.25000` | Invalidation Level: `1299.70000` | Status: **`SHALLOW_RETRACE`**
- **Classical & Weekly Pivots**:
  * Daily Classical: Pivot=`1296.21000` | R1=`1329.24000` | S1=`1263.44000` | R2=`1362.01000` | S2=`1230.41000`
  * Weekly Classical: Weekly Pivot=`1214.66000` | Weekly R1=`1367.30000` | Weekly S1=`1061.93000`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Orderflow
*(Sources: 18_CVD.parquet, 18_CVD_30D_5m.parquet, 18_CVD_30D_15m.parquet, 18_CVD_30D_1h.parquet, 18_CVD_30D_4h.parquet, 18_CVD_30D_ALL.parquet, 21_Tradfye_Orderflow.parquet)*
- **Interbank Spot Orderflow Mechanics**: Decentralized OTC market structure. CVD taker deltas do not apply to interbank spot flow. Tape volume governed by broker tick volume with live spread friction of `6.26 bps`.
- **Session Volume Structure**: Price operating at `ABOVE_VALUE (Imbalance)` with Daily POC at `1245.67000` (VAH: `1278.18000` / VAL: `1230.30000`).

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
  * Wallet `0xb83de012db...` (0xb83d...6e36): `Short` `67,331,916.86 USD` (52,582.5200 ZEC, Margin: 22,443,972.29 USD, Leverage: 3X Cross, Entry: 1,336.45 USD, Current: 1,277.70 USD, Est Liq: 3,382.40 USD, PnL: +2,941,998.04 USD [+4.37%], Fees: -684,940.17 USD)
  * Wallet `0x5b5d51203a...` (0x5b5d...c060): `Short` `52,151,704.60 USD` (40,727.6100 ZEC, Margin: 17,383,901.54 USD, Leverage: 3X Cross, Entry: 1,478.36 USD, Current: 1,277.70 USD, Est Liq: 4,608.84 USD, PnL: +8,058,559.59 USD [+15.45%], Fees: -620,670.63 USD)
  * Wallet `0x7fdafde5cf...` (0x7fda...17d1): `Short` `25,619,680.58 USD` (20,007.5600 ZEC, Margin: 5,123,936.12 USD, Leverage: 5X Cross, Entry: 1,251.76 USD, Current: 1,277.70 USD, Est Liq: 2,862.62 USD, PnL: -574,973.57 USD [-2.24%], Fees: -192,380.28 USD)

---

## 6. Liquidation Max Pain, Heatmaps & Cascade Boundaries
*(Sources: 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 14_Hyperdash_Liq_Map.parquet, 14_Liquidation_Matrix.parquet, 15_Hyperdash_Stops_Map.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`1288.96000` (Vol: `1,400,000 USD`, Dist: `+0.78%`) | Long MP=`1243.06000` (Vol: `1,400,000 USD`, Dist: `-2.81%`)
  * 48H Horizon: Short MP=`1332.96000` (Vol: `2,800,000 USD`, Dist: `+4.22%`) | Long MP=`1243.86000` (Vol: `1,400,000 USD`, Dist: `-2.74%`)
  * 3D Horizon: Short MP=`1332.46000` (Vol: `2,200,000 USD`, Dist: `+4.18%`) | Long MP=`1199.86000` (Vol: `1,800,000 USD`, Dist: `-6.18%`)
  * 7D Horizon: Short MP=`1333.81000` (Vol: `3,100,000 USD`, Dist: `+4.29%`) | Long MP=`1228.42000` (Vol: `2,600,000 USD`, Dist: `-3.95%`)
- **Exchange Cumulative Liquidation Cascades (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
  * 1D Cascade: Total=`0.00 USD` | Short Liq Pool=`0.00 USD` | Long Liq Pool=`0.00 USD` | Venues: Binance=`0.00 USD`, OKX=`0.00 USD`, Bybit=`0.00 USD`
  * 7D Cascade: Total=`0.00 USD` | Short Liq Pool=`0.00 USD` | Long Liq Pool=`0.00 USD` | Venues: Binance=`0.00 USD`, OKX=`0.00 USD`, Bybit=`0.00 USD`
- **Cross-Venue Liquidation Matrix & Heatmaps (14_Liquidation_Matrix.parquet, 7_Liq_Heapmap.parquet)**:
  * Liquidation Matrix Strike: Price=`0.00000` | Vol=`0 USD` | Cumulative=`0 USD` | Venue=`-` | Side=`-`
  * Multi-Timeframe Heatmap Density: 1h=`180.04K USD` | 4h=`693.55K USD` | 12h=`2.30M USD` | 24h=`7.30M USD`
- **Hyperdash Real-Time Liquidation & Retail Stop Protection (14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet)**:
  * Hyperdash Liq Cluster: Mark=`0.00 USD` | Cluster Price=`0.00 USD` | Dist=`-` | Cumulative=`0.00 USD` | Short=`0.00 USD` | Long=`0.00 USD` | Size=`-`
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
  * Major CEX Rates: Binance=`+0.0034%` | OKX=`-0.0029%` | Bybit=`+0.0093%` | Bitget=`-0.0027%`
  * Mid-Tier CEX Rates: KuCoin=`+0.0007%` | MEXC=`+0.0034%` | Gate=`-0.0038%` | BingX=`+0.0091%` | Bitunix=`+0.0035%`
  * Alternative Venues: WhiteBIT=`+0.0100%` | LBank=`+0.0034%` | tradeXYZ=`-`
  * Inverse Coin-Margined: CoinM Binance=`+0.0000%` | CoinM OKX=`+0.0000%` | CoinM Bybit=`+0.0000%`
- **Exchange Long / Short Ratio Dynamics (3_Exchanges_LS_Ratio*.parquet)**:
  * 15m Tactical: L/S Ratio=`1.00` (Longs: `50.00%`, Shorts: `50.00%`, Total Vol: `0.00 USD`)
  * 1h Primary: L/S Ratio=`1.00` (Longs: `50.00%`, Shorts: `50.00%`, Total Vol: `0.00 USD`)
  * 4h Macro: L/S Ratio=`1.00` (Longs: `50.00%`, Shorts: `50.00%`, Total Vol: `0.00 USD`)
- **Funding Fee Settlement & DEX Arbitrage (6_Funding_Fee_Settlement.parquet, 13_Hyperliquid.parquet)**:
  * Settlement Payouts: Current Expected=`31.81K USD` | Last 24h=`55.65K USD` | Last 3D=`287.36K USD` | Last 7D=`770.46K USD`

---

## 8. Microstructure Footprint, Tape Imbalances & Macro Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 16_Hyperdash_telegram_Intel.parquet, 19_News.parquet, 19_Calendar.parquet)*
- **Bar-by-Bar Microstructure Footprint (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
  * Venue Source: `CoinGlass-AggregatedFutures(Binance)` | Timeframe: `15m` | Last Price: `1278.93000`
  * Footprint Auction Profile: Bar VWAP=`1276.38653` | Bar POC=`1276.95000` | Bar VAH=`1278.75000` | Bar VAL=`1272.15000`
  * Orderflow Volumes: Total Vol=`9,550,391.77 USD` | Taker Buy=`4,466,289.90 USD` | Taker Sell=`5,084,101.87 USD`
  * Bar Delta Profile: Delta=`-617,811.98 USD` (`-6.47%`) | Max Delta=`+0.00 USD` | Min Delta=`-1,291,486.37 USD` | Cumulative Bar Delta=`-1,148,807.51 USD`
  * Order Execution Dynamics: Trades Count=`36,028` | Avg Trade Size=`265.08 USD`
  * Tape Imbalances: Imbalance Ratio=`300.0%` | Buy Imbalances Count=`1` | Sell Imbalances Count=`2`
  * Footprint Open Interest: Bar OI=`0.00 USD` | Bar OI Change=`+0.00 USD`
- **CoinGlass Algorithmic Footprint Signals (25_CoinGlass_Footprint_Signals.parquet)**:
  * Signal Classification: Type=`Trapped longs` | Bias: **`BEARISH`** | Signal Time=`10-28 06:52` | Timeframe=`Range 5`
  * Signal Context: Headline=`Failed breakout` | Price Level=`1309.20000` | Absorbed Volume=`1,800.00 USD`
  * Bar Footprint Context: Current Bar Delta=`+0.00 USD` | Current Bar Volume=`0.00 USD` | Delta in View=`+0.00 USD`
  * Historical Detail: `Broke the 5-bar high on 1.8K of taker buying at the top, then fell back into the lower part of the bar 1 bars later. Breakout buyers trapped, bearish · 1,309.2` | KPI=`—` | Bias=`—`
- **Multi-Horizon Macro Capital Netflows (2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet)**:
  * Spot Capital Netflows:
    - Tactical: 5m=`+1.38M` | 15m=`+2.39M` | 30m=`+2.99M` | 1h=`+2.33M`
    - Intermediate: 2h=`+3.26M` | 4h=`+7.37M` | 6h=`+1.16M` | 8h=`+1.48M` | 12h=`-4.44M` | 24h=`-13.63M`
    - Macro Horizons: 1-Week=`+28.13M` | 15-Day=`+32.18M` | 30-Day=`+21.31M` | Market Cap=`21.61B`
  * Futures Capital Netflows:
    - Tactical: 5m=`-1.29M` | 15m=`+797.29K` | 30m=`+9.36M` | 1h=`-1.20M`
    - Intermediate: 2h=`+5.60M` | 4h=`+18.07M` | 6h=`+20.80M` | 8h=`+18.19M` | 12h=`+28.88M` | 24h=`+780.14K`
    - Macro Horizons: 1-Week=`+156.18M` | 15-Day=`+251.25M` | 30-Day=`-663.73M` | Market Cap=`21.61B`
- **Telegram Intelligence Alert**: `[MARKET_INTEL] #ZEC Liquidated Long: 10.41K USD at 1289.6000 USD [API] (Impact: NEWS_INTEL)`

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