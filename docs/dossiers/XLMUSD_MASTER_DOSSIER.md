# 🔬 MASTER 43-FEED QUANTITATIVE DOSSIER: XLMUSD (Stellar / USD)
**MT5 Symbol**: `XLMUSD.p` | **Category**: `Crypto Altcoin` | **Tier**: `Tier 2`
**Execution Posture**: `PASSIVE LIMIT ONLY` | **Timestamp**: 2026-10-29 14:43:14 UTC
**Pipeline Clearance**: `QUALIFIED` | **Data Freshness**: `1.2m`

---

## 1. MT5 Live Broker Telemetry & Spread Friction Gate
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet)*
- **Live Bid Quote**: `0.17078` | **Live Ask Quote**: `0.17112` | **Mid Price**: `0.17095`
- **Spread Points**: `34.0 pts` | **Spread BPS**: `19.89 bps` (Mandatory Cap: `25.0 bps`)
- **Gate Status**: **`PASS`** (Spread friction within mandatory threshold; safe for maker execution)
- **Order Allowed**: `BUY_LIMIT / SELL_LIMIT` | **Pillar 1 Clearance**: `QUALIFIED`
- **Broker Specifications**: Contract Size=`1.00` | Tick Value=`1.00 USD` | Min Lot=`0.01` | Digits=`5`
- **Account Capital Context**: Balance=`4,744.55 USD` | Equity=`4,744.32 USD` | Free Margin=`4,342.62 USD` | Inviolate Hard Floor=`4,775.00 USD` (Cushion: `-30.68 USD`)
- **Pipeline Health**: Feed #00 Status=`PASS` | Overall Pipeline Telemetry=`33/33 FEEDS PASS (SYNCHRONIZED)`

---

## 2. Technical Profile, Multi-Sigma VWAP Dispersion & Volatility
*(Sources: 11_Technical.parquet, 11_Technical_BTC_Ribbon.parquet)*
- **Last Verified Price**: `0.17068` | **24h Change**: `+1.02%` (24h High: `0.17486`, 24h Low: `0.16652`)
- **Weekly Range**: Week High=`0.17486` | Week Low=`0.16612` | Daily POC=`0.16750` | Daily VAH=`0.17050` | Daily VAL=`0.16680`
- **Session VWAP**: `0.16872` | **Rolling 24h VWAP**: `0.16973` | **Distance to VWAP**: `+1.16%`
- **VWAP Z-Score**: `+1.36 sigma` | **Mean Reversion Bias**: **`FAIR VALUE`**
- **VWAP Dispersion Bands**:
  * +1.00 sigma: `0.17016` | -1.00 sigma: `0.16728`
  * +1.28 sigma (80% CI): `0.17056` | -1.28 sigma: `0.16688`
  * +2.00 sigma (95% CI): `0.17159` | -2.00 sigma: `0.16584`
  * +2.01 sigma: `0.17161` | -2.01 sigma: `0.16583`
  * +2.51 sigma (98.8% CI): `0.17233` | -2.51 sigma: `0.16511`
  * +3.00 sigma (99.7% CI Extreme): `0.17303` | -3.00 sigma: `0.16440`
- **Oscillators & Volatility**:
  * **RSI (14)**: `62.94` | **RSI State**: **`BULLISH`**
  * **ATR (14)**: `0.00068` | **ATR %**: `0.40%`
  * **Bollinger Bands**: Upper=`0.17141` | Mid=`0.16954` | Lower=`0.16768` | Bandwidth=`2.20%`
  * **MACD**: Line=`+0.0006` | Signal=`+0.0005` | Hist=`+0.0001`
- **Exponential Moving Average Ribbon (EMA)**:
  * Short Horizon: EMA-5=`0.17056` | EMA-9=`0.17033` | EMA-13=`0.17008` | EMA-20=`0.16972`
  * Intermediate: EMA-34=`0.16940` | EMA-50=`0.16936` | EMA-89=`0.16953` | EMA-100=`0.16957`
  * Institutional: EMA-144=`0.16961` | EMA-200=`0.16942` (Slope: `+0.057%`) | EMA-233=`0.16931` (Slope: `+0.056%`)
  * **Trend Bias**: **`BULLISH`**

---

## 3. Auction Market Structure & Value Profile
*(Sources: 20_Auction_Market_Structure.parquet)*
- **Daily Auction Value Area**:
  * High (VAH): `0.17050` | Point of Control (POC): `0.16750` | Low (VAL): `0.16680`
  * Distance to POC: `+2.07%` | Distance to VAH: `+0.30%` | Distance to VAL: `+2.50%`
  * **Value Area Position**: **`ABOVE_VALUE (Imbalance)`** | **Auction Regime**: **`RANGE_EXPANSION`** | **Session Bias**: **`BEARISH (Below Pivot)`**
- **Prior Day & Weekly Auction Profile**:
  * Prior Day: PD VAH=`0.17220` | PD POC=`0.17150` | PD VAL=`0.16980` | PDH=`0.17490` | PDL=`0.16840` | PDC=`0.17330`
  * Monday Reference: Monday High=`0.17070` | Monday Low=`0.16620` | Monday Mid=`0.16840`
  * Weekly Value Area: Weekly VAH=`0.17010` | Weekly POC=`0.16760` | Weekly VAL=`0.16700`
  * Multi-Week Extremes: Current Week High (CWH)=`0.17490` | CWL=`0.16610` | Prior Week High (PWH)=`0.18690` | PWL=`0.16600`
  * Multi-Month Extremes: Current Month High (CMH)=`0.23070` | CML=`0.16600` | Prior Month High (PMH)=`0.23670` | PML=`0.17110`
- **Session Liquidity Extremes & Initial Balance**:
  * Asian Session: Range `[0.16650 - 0.17400]`
  * London Session: Range `[0.16680 - 0.17080]`
  * New York Session: Range `[0.16800 - 0.17150]`
  * Initial Balance (IB): IB High=`0.16960` | IB Low=`0.16840`
- **Fibonacci Golden Pocket & Optimal Trade Entry (OTE)**:
  * Swing Range: High=`0.17490` | Low=`0.16650` | Direction=`BEARISH_IMPULSE`
  * Golden Pocket [0.618 - 0.65]: `[0.17170 - 0.17190]`
  * Optimal Trade Entry (0.702): `0.17240` | Invalidation Level: `0.17310` | Status: **`SHALLOW_RETRACE`**
- **Classical & Weekly Pivots**:
  * Daily Classical: Pivot=`0.17220` | R1=`0.17600` | S1=`0.16950` | R2=`0.17870` | S2=`0.16570`
  * Weekly Classical: Weekly Pivot=`0.17370` | Weekly R1=`0.18150` | Weekly S1=`0.16060`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Orderflow
*(Sources: 18_CVD.parquet, 18_CVD_30D_5m.parquet, 18_CVD_30D_15m.parquet, 18_CVD_30D_1h.parquet, 18_CVD_30D_4h.parquet, 18_CVD_30D_ALL.parquet, 21_Tradfye_Orderflow.parquet)*
- **Interbank Spot Orderflow Mechanics**: Decentralized OTC market structure. CVD taker deltas do not apply to interbank spot flow. Tape volume governed by broker tick volume with live spread friction of `19.89 bps`.
- **Session Volume Structure**: Price operating at `ABOVE_VALUE (Imbalance)` with Daily POC at `0.16750` (VAH: `0.17050` / VAL: `0.16680`).

---

## 5. Institutional Whale Armor & Resting Orderbook Depth
*(Sources: 10_Whale_Orders.parquet, 12_Hyperdash.parquet, 17_Orderbook.parquet, 4_Hyperliquid_Analysis.parquet)*
- **Interbank Institutional Tier-1 Depth**: Decentralized OTC spot liquidity. Resting whale limit walls from crypto venues do not apply.
- **Verified Broker Armor**: Live Bid `0.17078` / Live Ask `0.17112` with institutional spread of `19.89 bps`. Structural defense anchored at Asian Range `[0.16650 - 0.17400]` and London Range `[0.16680 - 0.17080]`.

---

## 6. Liquidation Max Pain, Heatmaps & Cascade Boundaries
*(Sources: 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 14_Hyperdash_Liq_Map.parquet, 14_Liquidation_Matrix.parquet, 15_Hyperdash_Stops_Map.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`0.17647` (Vol: `114,500 USD`, Dist: `+3.14%`) | Long MP=`0.16567` (Vol: `77,700 USD`, Dist: `-3.17%`)
  * 48H Horizon: Short MP=`0.17617` (Vol: `116,400 USD`, Dist: `+2.97%`) | Long MP=`0.16597` (Vol: `98,100 USD`, Dist: `-2.99%`)
  * 3D Horizon: Short MP=`0.17610` (Vol: `121,600 USD`, Dist: `+2.93%`) | Long MP=`0.16463` (Vol: `161,000 USD`, Dist: `-3.78%`)
  * 7D Horizon: Short MP=`0.17963` (Vol: `185,000 USD`, Dist: `+4.99%`) | Long MP=`0.16486` (Vol: `258,600 USD`, Dist: `-3.64%`)
- **Exchange Cumulative Liquidation Cascades (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
  * 1D Cascade: Total=`0.00 USD` | Short Liq Pool=`0.00 USD` | Long Liq Pool=`0.00 USD` | Venues: Binance=`0.00 USD`, OKX=`0.00 USD`, Bybit=`0.00 USD`
  * 7D Cascade: Total=`0.00 USD` | Short Liq Pool=`0.00 USD` | Long Liq Pool=`0.00 USD` | Venues: Binance=`0.00 USD`, OKX=`0.00 USD`, Bybit=`0.00 USD`
- **Cross-Venue Liquidation Matrix & Heatmaps (14_Liquidation_Matrix.parquet, 7_Liq_Heapmap.parquet)**:
  * Liquidation Matrix Strike: Price=`0.00000` | Vol=`0 USD` | Cumulative=`0 USD` | Venue=`-` | Side=`-`
  * Multi-Timeframe Heatmap Density: 1h=`0.00 USD` | 4h=`0.00 USD` | 12h=`0.00 USD` | 24h=`0.00 USD`
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
  * Major CEX Rates: Binance=`+0.0050%` | OKX=`+0.0100%` | Bybit=`+0.0076%` | Bitget=`+0.0100%`
  * Mid-Tier CEX Rates: KuCoin=`+0.0100%` | MEXC=`+0.0048%` | Gate=`+0.0052%` | BingX=`+0.0100%` | Bitunix=`+0.0050%`
  * Alternative Venues: WhiteBIT=`+0.0100%` | LBank=`+0.0049%` | tradeXYZ=`-`
  * Inverse Coin-Margined: CoinM Binance=`+0.0058%` | CoinM OKX=`+0.0000%` | CoinM Bybit=`+0.0100%`
- **Exchange Long / Short Ratio Dynamics (3_Exchanges_LS_Ratio*.parquet)**:
  * 15m Tactical: L/S Ratio=`1.00` (Longs: `50.00%`, Shorts: `50.00%`, Total Vol: `0.00 USD`)
  * 1h Primary: L/S Ratio=`1.00` (Longs: `50.00%`, Shorts: `50.00%`, Total Vol: `0.00 USD`)
  * 4h Macro: L/S Ratio=`1.00` (Longs: `50.00%`, Shorts: `50.00%`, Total Vol: `0.00 USD`)
- **Funding Fee Settlement & DEX Arbitrage (6_Funding_Fee_Settlement.parquet, 13_Hyperliquid.parquet)**:
  * Settlement Payouts: Current Expected=`5.74K USD` | Last 24h=`-9.65K USD` | Last 3D=`22.59K USD` | Last 7D=`45.37K USD`

---

## 8. Microstructure Footprint, Tape Imbalances & Macro Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 16_Hyperdash_telegram_Intel.parquet, 19_News.parquet, 19_Calendar.parquet)*
- **Bar-by-Bar Microstructure Footprint (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
  * Venue Source: `Aggregated` | Timeframe: `15m` | Last Price: `0.17095`
  * Footprint Auction Profile: Bar VWAP=`0.17095` | Bar POC=`0.17095` | Bar VAH=`0.17129` | Bar VAL=`0.17061`
  * Orderflow Volumes: Total Vol=`0.00 USD` | Taker Buy=`0.00 USD` | Taker Sell=`0.00 USD`
  * Bar Delta Profile: Delta=`+0.00 USD` (`+0.00%`) | Max Delta=`+0.00 USD` | Min Delta=`+0.00 USD` | Cumulative Bar Delta=`+0.00 USD`
  * Order Execution Dynamics: Trades Count=`0` | Avg Trade Size=`0.00 USD`
  * Tape Imbalances: Imbalance Ratio=`0.0%` | Buy Imbalances Count=`0` | Sell Imbalances Count=`0`
  * Footprint Open Interest: Bar OI=`0.00 USD` | Bar OI Change=`+0.00 USD`
- **Multi-Horizon Macro Capital Netflows (2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet)**:
  * Spot Capital Netflows:
    - Tactical: 5m=`+17.48K` | 15m=`-44.93K` | 30m=`+29.17K` | 1h=`-19.50K`
    - Intermediate: 2h=`+594.23K` | 4h=`+521.12K` | 6h=`+555.67K` | 8h=`+577.21K` | 12h=`-95.24K` | 24h=`+297.62K`
    - Macro Horizons: 1-Week=`+4.54M` | 15-Day=`+6.60M` | 30-Day=`-24.07M` | Market Cap=`6.02B`
  * Futures Capital Netflows:
    - Tactical: 5m=`-12.85K` | 15m=`+21.98K` | 30m=`-107.68K` | 1h=`-57.09K`
    - Intermediate: 2h=`+470.55K` | 4h=`+522.90K` | 6h=`+246.93K` | 8h=`-747.86K` | 12h=`-55.34K` | 24h=`+253.88K`
    - Macro Horizons: 1-Week=`-3.19M` | 15-Day=`-14.18M` | 30-Day=`-85.89M` | Market Cap=`6.02B`

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