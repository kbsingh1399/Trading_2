# 🔬 MASTER 43-FEED QUANTITATIVE DOSSIER: AVEUSD (Aave / USD)
**MT5 Symbol**: `AVEUSD.p` | **Category**: `Crypto Altcoin` | **Tier**: `Tier 2`
**Execution Posture**: `PASSIVE LIMIT ONLY` | **Timestamp**: 2026-10-29 14:43:14 UTC
**Pipeline Clearance**: `QUALIFIED` | **Data Freshness**: `1.2m`

---

## 1. MT5 Live Broker Telemetry & Spread Friction Gate
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet)*
- **Live Bid Quote**: `133.16000` | **Live Ask Quote**: `133.42000` | **Mid Price**: `133.29000`
- **Spread Points**: `26.0 pts` | **Spread BPS**: `19.51 bps` (Mandatory Cap: `25.0 bps`)
- **Gate Status**: **`PASS`** (Spread friction within mandatory threshold; safe for maker execution)
- **Order Allowed**: `BUY_LIMIT / SELL_LIMIT` | **Pillar 1 Clearance**: `QUALIFIED`
- **Broker Specifications**: Contract Size=`1.00` | Tick Value=`1.00 USD` | Min Lot=`0.01` | Digits=`5`
- **Account Capital Context**: Balance=`4,744.55 USD` | Equity=`4,744.32 USD` | Free Margin=`4,342.62 USD` | Inviolate Hard Floor=`4,775.00 USD` (Cushion: `-30.68 USD`)
- **Pipeline Health**: Feed #00 Status=`PASS` | Overall Pipeline Telemetry=`33/33 FEEDS PASS (SYNCHRONIZED)`

---

## 2. Technical Profile, Multi-Sigma VWAP Dispersion & Volatility
*(Sources: 11_Technical.parquet, 11_Technical_BTC_Ribbon.parquet)*
- **Last Verified Price**: `132.78000` | **24h Change**: `+1.34%` (24h High: `138.47000`, 24h Low: `128.25000`)
- **Weekly Range**: Week High=`138.47000` | Week Low=`128.25000` | Daily POC=`132.88000` | Daily VAH=`134.44000` | Daily VAL=`130.17000`
- **Session VWAP**: `131.20295` | **Rolling 24h VWAP**: `132.30056` | **Distance to VWAP**: `+1.20%`
- **VWAP Z-Score**: `+1.02 sigma` | **Mean Reversion Bias**: **`FAIR VALUE`**
- **VWAP Dispersion Bands**:
  * +1.00 sigma: `132.74819` | -1.00 sigma: `129.65772`
  * +1.28 sigma (80% CI): `133.18086` | -1.28 sigma: `129.22505`
  * +2.00 sigma (95% CI): `134.29343` | -2.00 sigma: `128.11248`
  * +2.01 sigma: `134.30888` | -2.01 sigma: `128.09703`
  * +2.51 sigma (98.8% CI): `135.08150` | -2.51 sigma: `127.32441`
  * +3.00 sigma (99.7% CI Extreme): `135.83866` | -3.00 sigma: `126.56724`
- **Oscillators & Volatility**:
  * **RSI (14)**: `58.53` | **RSI State**: **`BULLISH`**
  * **ATR (14)**: `0.91762` | **ATR %**: `0.69%`
  * **Bollinger Bands**: Upper=`134.02001` | Mid=`132.01000` | Lower=`129.99999` | Bandwidth=`3.05%`
  * **MACD**: Line=`+0.4955` | Signal=`+0.4933` | Hist=`+0.0022`
- **Exponential Moving Average Ribbon (EMA)**:
  * Short Horizon: EMA-5=`132.56256` | EMA-9=`132.50449` | EMA-13=`132.35640` | EMA-20=`132.07748`
  * Intermediate: EMA-34=`131.76858` | EMA-50=`131.71955` | EMA-89=`131.94903` | EMA-100=`132.02754`
  * Institutional: EMA-144=`132.31181` | EMA-200=`132.43977` (Slope: `+0.024%`) | EMA-233=`132.55764` (Slope: `+0.011%`)
  * **Trend Bias**: **`BULLISH`**

---

## 3. Auction Market Structure & Value Profile
*(Sources: 20_Auction_Market_Structure.parquet)*
- **Daily Auction Value Area**:
  * High (VAH): `134.44000` | Point of Control (POC): `132.88000` | Low (VAL): `130.17000`
  * Distance to POC: `+0.33%` | Distance to VAH: `-0.84%` | Distance to VAL: `+2.41%`
  * **Value Area Position**: **`INSIDE_VALUE (Balance)`** | **Auction Regime**: **`ROTATIONAL_BALANCE`** | **Session Bias**: **`BEARISH (Below Pivot)`**
- **Prior Day & Weekly Auction Profile**:
  * Prior Day: PD VAH=`135.85000` | PD POC=`134.70000` | PD VAL=`132.04000` | PDH=`138.47000` | PDL=`129.42000` | PDC=`134.07000`
  * Monday Reference: Monday High=`138.35000` | Monday Low=`132.27000` | Monday Mid=`135.31000`
  * Weekly Value Area: Weekly VAH=`135.98000` | Weekly POC=`134.76000` | Weekly VAL=`131.69000`
  * Multi-Week Extremes: Current Week High (CWH)=`138.47000` | CWL=`128.25000` | Prior Week High (PWH)=`160.27000` | PWL=`133.73000`
  * Multi-Month Extremes: Current Month High (CMH)=`187.38000` | CML=`128.25000` | Prior Month High (PMH)=`176.08000` | PML=`113.06000`
- **Session Liquidity Extremes & Initial Balance**:
  * Asian Session: Range `[128.25000 - 135.37000]`
  * London Session: Range `[129.16000 - 133.60000]`
  * New York Session: Range `[130.09000 - 133.60000]`
  * Initial Balance (IB): IB High=`131.85000` | IB Low=`129.90000`
- **Fibonacci Golden Pocket & Optimal Trade Entry (OTE)**:
  * Swing Range: High=`138.47000` | Low=`128.25000` | Direction=`BEARISH_IMPULSE`
  * Golden Pocket [0.618 - 0.65]: `[134.57000 - 134.89000]`
  * Optimal Trade Entry (0.702): `135.42000` | Invalidation Level: `136.28000` | Status: **`SHALLOW_RETRACE`**
- **Classical & Weekly Pivots**:
  * Daily Classical: Pivot=`133.99000` | R1=`138.55000` | S1=`129.50000` | R2=`143.04000` | S2=`124.94000`
  * Weekly Classical: Weekly Pivot=`143.84000` | Weekly R1=`153.96000` | Weekly S1=`127.42000`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Orderflow
*(Sources: 18_CVD.parquet, 18_CVD_30D_5m.parquet, 18_CVD_30D_15m.parquet, 18_CVD_30D_1h.parquet, 18_CVD_30D_4h.parquet, 18_CVD_30D_ALL.parquet, 21_Tradfye_Orderflow.parquet)*
- **Interbank Spot Orderflow Mechanics**: Decentralized OTC market structure. CVD taker deltas do not apply to interbank spot flow. Tape volume governed by broker tick volume with live spread friction of `19.51 bps`.
- **Session Volume Structure**: Price operating at `INSIDE_VALUE (Balance)` with Daily POC at `132.88000` (VAH: `134.44000` / VAL: `130.17000`).

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
  * Wallet `0x3ee505ba31...` (0x3ee5...4fab): `Long` `5,769,802.31 USD` (43,303.8300 AAVE, Margin: 576,980.23 USD, Leverage: 10X Cross, Entry: 77.3532 USD, Current: 133.1300 USD, Est Liq: 114.2570 USD, PnL: +2,420,112.27 USD [+41.94%], Fees: +247,175.54 USD)
  * Wallet `0x0514f2f3e0...` (0x0514...bdfe): `Short` `3,066,130.00 USD` (23,000.0000 AAVE, Margin: 306,613.00 USD, Leverage: 10X Cross, Entry: 87.4121 USD, Current: 133.1300 USD, Est Liq: 184.2300 USD, PnL: -1,055,650.78 USD [-34.43%], Fees: -135,549.28 USD)
  * Wallet `0x08c14b32c8...` (0x08c1...1135): `Long` `2,910,762.79 USD` (21,836.1800 AAVE, Margin: 291,076.28 USD, Leverage: 10X Cross, Entry: 80.8902 USD, Current: 133.1300 USD, Est Liq: 92.2441 USD, PnL: +1,144,428.44 USD [+39.32%], Fees: +127,929.79 USD)

---

## 6. Liquidation Max Pain, Heatmaps & Cascade Boundaries
*(Sources: 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 14_Hyperdash_Liq_Map.parquet, 14_Liquidation_Matrix.parquet, 15_Hyperdash_Stops_Map.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`133.91000` (Vol: `206,000 USD`, Dist: `+0.21%`) | Long MP=`128.71000` (Vol: `206,000 USD`, Dist: `-3.68%`)
  * 48H Horizon: Short MP=`133.91000` (Vol: `206,000 USD`, Dist: `+0.21%`) | Long MP=`128.71000` (Vol: `206,000 USD`, Dist: `-3.68%`)
  * 3D Horizon: Short MP=`133.91000` (Vol: `206,000 USD`, Dist: `+0.21%`) | Long MP=`128.71000` (Vol: `206,000 USD`, Dist: `-3.68%`)
  * 7D Horizon: Short MP=`139.76000` (Vol: `320,000 USD`, Dist: `+4.58%`) | Long MP=`127.18000` (Vol: `326,000 USD`, Dist: `-4.83%`)
- **Exchange Cumulative Liquidation Cascades (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
  * 1D Cascade: Total=`0.00 USD` | Short Liq Pool=`0.00 USD` | Long Liq Pool=`0.00 USD` | Venues: Binance=`0.00 USD`, OKX=`0.00 USD`, Bybit=`0.00 USD`
  * 7D Cascade: Total=`0.00 USD` | Short Liq Pool=`0.00 USD` | Long Liq Pool=`0.00 USD` | Venues: Binance=`0.00 USD`, OKX=`0.00 USD`, Bybit=`0.00 USD`
- **Cross-Venue Liquidation Matrix & Heatmaps (14_Liquidation_Matrix.parquet, 7_Liq_Heapmap.parquet)**:
  * Liquidation Matrix Strike: Price=`265.50000` | Vol=`231 USD` | Cumulative=`9,520,000 USD` | Venue=`Hyperliquid L1` | Side=`Short Liquidation`
  * Multi-Timeframe Heatmap Density: 1h=`0.00 USD` | 4h=`0.00 USD` | 12h=`275.66K USD` | 24h=`908.16K USD`
- **Hyperdash Real-Time Liquidation & Retail Stop Protection (14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet)**:
  * Hyperdash Liq Cluster: Mark=`133.1050 USD` | Cluster Price=`265.5000 USD` | Dist=`+99.47%` | Cumulative=`9.52M USD` | Short=`230.98 USD` | Long=`0 USD` | Size=`0.8700 AAVE`
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
  * Major CEX Rates: Binance=`+0.0057%` | OKX=`+0.0100%` | Bybit=`+0.0100%` | Bitget=`+0.0027%`
  * Mid-Tier CEX Rates: KuCoin=`+0.0100%` | MEXC=`+0.0058%` | Gate=`+0.0091%` | BingX=`+0.0100%` | Bitunix=`+0.0062%`
  * Alternative Venues: WhiteBIT=`-0.0026%` | LBank=`+0.0000%` | tradeXYZ=`-`
  * Inverse Coin-Margined: CoinM Binance=`+0.0100%` | CoinM OKX=`+0.0000%` | CoinM Bybit=`+0.0100%`
- **Exchange Long / Short Ratio Dynamics (3_Exchanges_LS_Ratio*.parquet)**:
  * 15m Tactical: L/S Ratio=`1.00` (Longs: `50.00%`, Shorts: `50.00%`, Total Vol: `0.00 USD`)
  * 1h Primary: L/S Ratio=`1.00` (Longs: `50.00%`, Shorts: `50.00%`, Total Vol: `0.00 USD`)
  * 4h Macro: L/S Ratio=`1.00` (Longs: `50.00%`, Shorts: `50.00%`, Total Vol: `0.00 USD`)
- **Funding Fee Settlement & DEX Arbitrage (6_Funding_Fee_Settlement.parquet, 13_Hyperliquid.parquet)**:
  * Settlement Payouts: Current Expected=`10.26K USD` | Last 24h=`24.24K USD` | Last 3D=`65.40K USD` | Last 7D=`98.48K USD`

---

## 8. Microstructure Footprint, Tape Imbalances & Macro Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 16_Hyperdash_telegram_Intel.parquet, 19_News.parquet, 19_Calendar.parquet)*
- **Bar-by-Bar Microstructure Footprint (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
  * Venue Source: `CoinGlass-AggregatedFutures(Binance)` | Timeframe: `15m` | Last Price: `133.29000`
  * Footprint Auction Profile: Bar VWAP=`132.97413` | Bar POC=`132.79500` | Bar VAH=`133.33500` | Bar VAL=`132.61500`
  * Orderflow Volumes: Total Vol=`927,178.60 USD` | Taker Buy=`448,934.81 USD` | Taker Sell=`478,243.79 USD`
  * Bar Delta Profile: Delta=`-29,308.98 USD` (`-3.16%`) | Max Delta=`+6,665.76 USD` | Min Delta=`-158,586.60 USD` | Cumulative Bar Delta=`+720,973.30 USD`
  * Order Execution Dynamics: Trades Count=`6,922` | Avg Trade Size=`133.95 USD`
  * Tape Imbalances: Imbalance Ratio=`300.0%` | Buy Imbalances Count=`15` | Sell Imbalances Count=`13`
  * Footprint Open Interest: Bar OI=`0.00 USD` | Bar OI Change=`+0.00 USD`
- **CoinGlass Algorithmic Footprint Signals (25_CoinGlass_Footprint_Signals.parquet)**:
  * Signal Classification: Type=`Exhaustion` | Bias: **`BEARISH`** | Signal Time=`10-28 07:26` | Timeframe=`Range 0.5`
  * Signal Context: Headline=`Buyer exhaustion` | Price Level=`135.17000` | Absorbed Volume=`0.00 USD`
  * Bar Footprint Context: Current Bar Delta=`+0.00 USD` | Current Bar Volume=`0.00 USD` | Delta in View=`+0.00 USD`
  * Historical Detail: `New 10-bar high with almost no volume in the top 10% of the bar, closed in the lower half, bearish · 135.17` | KPI=`—` | Bias=`—`
- **Multi-Horizon Macro Capital Netflows (2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet)**:
  * Spot Capital Netflows:
    - Tactical: 5m=`+18.41K` | 15m=`-96.46K` | 30m=`-163.09K` | 1h=`-328.30K`
    - Intermediate: 2h=`-76.05K` | 4h=`+116.27K` | 6h=`+6.16K` | 8h=`+134.97K` | 12h=`+221.77K` | 24h=`-2.08M`
    - Macro Horizons: 1-Week=`-23.58M` | 15-Day=`-43.63M` | 30-Day=`-114.03M` | Market Cap=`2.05B`
  * Futures Capital Netflows:
    - Tactical: 5m=`+30.74K` | 15m=`+210.19K` | 30m=`+360.85K` | 1h=`-222.27K`
    - Intermediate: 2h=`+951.72K` | 4h=`-507.12K` | 6h=`+415.48K` | 8h=`+368.97K` | 12h=`+1.33M` | 24h=`+433.39K`
    - Macro Horizons: 1-Week=`-43.26M` | 15-Day=`-50.59M` | 30-Day=`-106.86M` | Market Cap=`2.05B`

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