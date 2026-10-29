# 🔬 MASTER 43-FEED QUANTITATIVE DOSSIER: ALGUSD (Algorand / USD)
**MT5 Symbol**: `ALGUSD.p` | **Category**: `Crypto Altcoin` | **Tier**: `Tier 2`
**Execution Posture**: `DISQUALIFIED` | **Timestamp**: 2026-10-29 14:43:14 UTC
**Pipeline Clearance**: `BLOCKED` | **Data Freshness**: `1.2m`

---

## 1. MT5 Live Broker Telemetry & Spread Friction Gate
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet)*
- **Live Bid Quote**: `0.09950` | **Live Ask Quote**: `0.10170` | **Mid Price**: `0.10060`
- **Spread Points**: `22.0 pts` | **Spread BPS**: `218.69 bps` (Mandatory Cap: `25.0 bps`)
- **Gate Status**: **`FAIL`** (Spread friction 218.69 bps exceeds cap 25.0 bps)
- **Order Allowed**: `NONE` | **Pillar 1 Clearance**: `BLOCKED`
- **Broker Specifications**: Contract Size=`1.00` | Tick Value=`1.00 USD` | Min Lot=`0.01` | Digits=`5`
- **Account Capital Context**: Balance=`4,744.55 USD` | Equity=`4,744.32 USD` | Free Margin=`4,342.62 USD` | Inviolate Hard Floor=`4,775.00 USD` (Cushion: `-30.68 USD`)
- **Pipeline Health**: Feed #00 Status=`PASS` | Overall Pipeline Telemetry=`33/33 FEEDS PASS (SYNCHRONIZED)`

---

## 2. Technical Profile, Multi-Sigma VWAP Dispersion & Volatility
*(Sources: 11_Technical.parquet, 11_Technical_BTC_Ribbon.parquet)*
- **Last Verified Price**: `0.09920` | **24h Change**: `-0.60%` (24h High: `0.10480`, 24h Low: `0.09720`)
- **Weekly Range**: Week High=`0.10510` | Week Low=`0.09720` | Daily POC=`0.09810` | Daily VAH=`0.09960` | Daily VAL=`0.09740`
- **Session VWAP**: `0.09898` | **Rolling 24h VWAP**: `0.10030` | **Distance to VWAP**: `+0.22%`
- **VWAP Z-Score**: `+0.16 sigma` | **Mean Reversion Bias**: **`FAIR VALUE`**
- **VWAP Dispersion Bands**:
  * +1.00 sigma: `0.10034` | -1.00 sigma: `0.09762`
  * +1.28 sigma (80% CI): `0.10072` | -1.28 sigma: `0.09724`
  * +2.00 sigma (95% CI): `0.10170` | -2.00 sigma: `0.09626`
  * +2.01 sigma: `0.10171` | -2.01 sigma: `0.09625`
  * +2.51 sigma (98.8% CI): `0.10239` | -2.51 sigma: `0.09557`
  * +3.00 sigma (99.7% CI Extreme): `0.10305` | -3.00 sigma: `0.09491`
- **Oscillators & Volatility**:
  * **RSI (14)**: `54.34` | **RSI State**: **`NEUTRAL`**
  * **ATR (14)**: `0.00052` | **ATR %**: `0.53%`
  * **Bollinger Bands**: Upper=`0.09985` | Mid=`0.09873` | Lower=`0.09761` | Bandwidth=`2.27%`
  * **MACD**: Line=`+0.0002` | Signal=`+0.0001` | Hist=`+0.0001`
- **Exponential Moving Average Ribbon (EMA)**:
  * Short Horizon: EMA-5=`0.09924` | EMA-9=`0.09915` | EMA-13=`0.09903` | EMA-20=`0.09890`
  * Intermediate: EMA-34=`0.09890` | EMA-50=`0.09912` | EMA-89=`0.09973` | EMA-100=`0.09988`
  * Institutional: EMA-144=`0.10038` | EMA-200=`0.10084` (Slope: `-0.224%`) | EMA-233=`0.10109` (Slope: `-0.218%`)
  * **Trend Bias**: **`NEUTRAL / CHOP`**

---

## 3. Auction Market Structure & Value Profile
*(Sources: 20_Auction_Market_Structure.parquet)*
- **Daily Auction Value Area**:
  * High (VAH): `0.09960` | Point of Control (POC): `0.09810` | Low (VAL): `0.09740`
  * Distance to POC: `+2.51%` | Distance to VAH: `+0.90%` | Distance to VAL: `+3.24%`
  * **Value Area Position**: **`ABOVE_VALUE (Imbalance)`** | **Auction Regime**: **`RANGE_EXPANSION`** | **Session Bias**: **`BEARISH (Below Pivot)`**
- **Prior Day & Weekly Auction Profile**:
  * Prior Day: PD VAH=`0.10380` | PD POC=`0.10230` | PD VAL=`0.10110` | PDH=`0.10480` | PDL=`0.09940` | PDC=`0.10310`
  * Monday Reference: Monday High=`0.10460` | Monday Low=`0.10150` | Monday Mid=`0.10310`
  * Weekly Value Area: Weekly VAH=`0.10420` | Weekly POC=`0.10230` | Weekly VAL=`0.10140`
  * Multi-Week Extremes: Current Week High (CWH)=`0.10510` | CWL=`0.09720` | Prior Week High (PWH)=`0.11550` | PWL=`0.09960`
  * Multi-Month Extremes: Current Month High (CMH)=`0.14220` | CML=`0.09720` | Prior Month High (PMH)=`0.13920` | PML=`0.08390`
- **Session Liquidity Extremes & Initial Balance**:
  * Asian Session: Range `[0.09720 - 0.10370]`
  * London Session: Range `[0.09720 - 0.09990]`
  * New York Session: Range `[0.09780 - 0.10000]`
  * Initial Balance (IB): IB High=`0.09990` | IB Low=`0.09870`
- **Fibonacci Golden Pocket & Optimal Trade Entry (OTE)**:
  * Swing Range: High=`0.10480` | Low=`0.09720` | Direction=`BEARISH_IMPULSE`
  * Golden Pocket [0.618 - 0.65]: `[0.10190 - 0.10210]`
  * Optimal Trade Entry (0.702): `0.10250` | Invalidation Level: `0.10320` | Status: **`SHALLOW_RETRACE`**
- **Classical & Weekly Pivots**:
  * Daily Classical: Pivot=`0.10240` | R1=`0.10550` | S1=`0.10010` | R2=`0.10780` | S2=`0.09700`
  * Weekly Classical: Weekly Pivot=`0.10660` | Weekly R1=`0.11350` | Weekly S1=`0.09760`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Orderflow
*(Sources: 18_CVD.parquet, 18_CVD_30D_5m.parquet, 18_CVD_30D_15m.parquet, 18_CVD_30D_1h.parquet, 18_CVD_30D_4h.parquet, 18_CVD_30D_ALL.parquet, 21_Tradfye_Orderflow.parquet)*
- **Interbank Spot Orderflow Mechanics**: Decentralized OTC market structure. CVD taker deltas do not apply to interbank spot flow. Tape volume governed by broker tick volume with live spread friction of `218.69 bps`.
- **Session Volume Structure**: Price operating at `ABOVE_VALUE (Imbalance)` with Daily POC at `0.09810` (VAH: `0.09960` / VAL: `0.09740`).

---

## 5. Institutional Whale Armor & Resting Orderbook Depth
*(Sources: 10_Whale_Orders.parquet, 12_Hyperdash.parquet, 17_Orderbook.parquet, 4_Hyperliquid_Analysis.parquet)*
- **Interbank Institutional Tier-1 Depth**: Decentralized OTC spot liquidity. Resting whale limit walls from crypto venues do not apply.
- **Verified Broker Armor**: Live Bid `0.09950` / Live Ask `0.10170` with institutional spread of `218.69 bps`. Structural defense anchored at Asian Range `[0.09720 - 0.10370]` and London Range `[0.09720 - 0.09990]`.

---

## 6. Liquidation Max Pain, Heatmaps & Cascade Boundaries
*(Sources: 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 14_Hyperdash_Liq_Map.parquet, 14_Liquidation_Matrix.parquet, 15_Hyperdash_Stops_Map.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`0.10676` (Vol: `34,982 USD`, Dist: `+3.28%`) | Long MP=`0.10154` (Vol: `29,089 USD`, Dist: `-1.77%`)
  * 48H Horizon: Short MP=`0.10673` (Vol: `34,069 USD`, Dist: `+3.26%`) | Long MP=`0.10157` (Vol: `32,528 USD`, Dist: `-1.74%`)
  * 3D Horizon: Short MP=`0.10649` (Vol: `32,467 USD`, Dist: `+3.02%`) | Long MP=`0.10085` (Vol: `37,584 USD`, Dist: `-2.44%`)
  * 7D Horizon: Short MP=`0.10672` (Vol: `62,664 USD`, Dist: `+3.72%`) | Long MP=`0.10083` (Vol: `53,529 USD`, Dist: `-2.01%`)
- **Exchange Cumulative Liquidation Cascades (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
  * 1D Cascade: Total=`0.00 USD` | Short Liq Pool=`0.00 USD` | Long Liq Pool=`0.00 USD` | Venues: Binance=`0.00 USD`, OKX=`0.00 USD`, Bybit=`0.00 USD`
  * 7D Cascade: Total=`0.00 USD` | Short Liq Pool=`0.00 USD` | Long Liq Pool=`0.00 USD` | Venues: Binance=`0.00 USD`, OKX=`0.00 USD`, Bybit=`0.00 USD`
- **Cross-Venue Liquidation Matrix & Heatmaps (14_Liquidation_Matrix.parquet, 7_Liq_Heapmap.parquet)**:
  * Liquidation Matrix Strike: Price=`0.19050` | Vol=`102 USD` | Cumulative=`5,610 USD` | Venue=`Hyperliquid L1` | Side=`Short Liquidation`
  * Multi-Timeframe Heatmap Density: 1h=`0.00 USD` | 4h=`0.00 USD` | 12h=`0.00 USD` | 24h=`0.00 USD`
- **Hyperdash Real-Time Liquidation & Retail Stop Protection (14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet)**:
  * Hyperdash Liq Cluster: Mark=`0.100350 USD` | Cluster Price=`0.190500 USD` | Dist=`+89.84%` | Cumulative=`5.61K USD` | Short=`102.49 USD` | Long=`0 USD` | Size=`538.0000 ALGO`
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
  * Major CEX Rates: Binance=`-0.0019%` | OKX=`-0.0111%` | Bybit=`+0.0022%` | Bitget=`+0.0028%`
  * Mid-Tier CEX Rates: KuCoin=`+0.0100%` | MEXC=`-0.0019%` | Gate=`-0.0039%` | BingX=`+0.0024%` | Bitunix=`+0.0011%`
  * Alternative Venues: WhiteBIT=`+0.0100%` | LBank=`-0.0019%` | tradeXYZ=`-`
  * Inverse Coin-Margined: CoinM Binance=`+0.0000%` | CoinM OKX=`+0.0000%` | CoinM Bybit=`+0.0000%`
- **Exchange Long / Short Ratio Dynamics (3_Exchanges_LS_Ratio*.parquet)**:
  * 15m Tactical: L/S Ratio=`1.00` (Longs: `50.00%`, Shorts: `50.00%`, Total Vol: `0.00 USD`)
  * 1h Primary: L/S Ratio=`1.00` (Longs: `50.00%`, Shorts: `50.00%`, Total Vol: `0.00 USD`)
  * 4h Macro: L/S Ratio=`1.00` (Longs: `50.00%`, Shorts: `50.00%`, Total Vol: `0.00 USD`)
- **Funding Fee Settlement & DEX Arbitrage (6_Funding_Fee_Settlement.parquet, 13_Hyperliquid.parquet)**:
  * Settlement Payouts: Current Expected=`-421.17 USD` | Last 24h=`-5.65K USD` | Last 3D=`-2.59K USD` | Last 7D=`-6.48K USD`

---

## 8. Microstructure Footprint, Tape Imbalances & Macro Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 16_Hyperdash_telegram_Intel.parquet, 19_News.parquet, 19_Calendar.parquet)*
- **Bar-by-Bar Microstructure Footprint (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
  * Venue Source: `Aggregated` | Timeframe: `15m` | Last Price: `0.10060`
  * Footprint Auction Profile: Bar VWAP=`0.10060` | Bar POC=`0.10060` | Bar VAH=`0.10080` | Bar VAL=`0.10040`
  * Orderflow Volumes: Total Vol=`0.00 USD` | Taker Buy=`0.00 USD` | Taker Sell=`0.00 USD`
  * Bar Delta Profile: Delta=`+0.00 USD` (`+0.00%`) | Max Delta=`+0.00 USD` | Min Delta=`+0.00 USD` | Cumulative Bar Delta=`+0.00 USD`
  * Order Execution Dynamics: Trades Count=`0` | Avg Trade Size=`0.00 USD`
  * Tape Imbalances: Imbalance Ratio=`0.0%` | Buy Imbalances Count=`0` | Sell Imbalances Count=`0`
  * Footprint Open Interest: Bar OI=`0.00 USD` | Bar OI Change=`+0.00 USD`
- **Multi-Horizon Macro Capital Netflows (2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet)**:
  * Spot Capital Netflows:
    - Tactical: 5m=`-1.25K` | 15m=`+5.31K` | 30m=`-4.36K` | 1h=`-41.50K`
    - Intermediate: 2h=`-31.80K` | 4h=`-19.57K` | 6h=`+20.85K` | 8h=`+42.66K` | 12h=`+131.60K` | 24h=`+34.13K`
    - Macro Horizons: 1-Week=`-1.54M` | 15-Day=`-2.34M` | 30-Day=`-12.55M` | Market Cap=`911.62M`
  * Futures Capital Netflows:
    - Tactical: 5m=`-81.54K` | 15m=`+60.22K` | 30m=`-67.25K` | 1h=`-118.81K`
    - Intermediate: 2h=`-71.22K` | 4h=`-89.88K` | 6h=`+41.15K` | 8h=`+239.69K` | 12h=`+136.36K` | 24h=`+90.65K`
    - Macro Horizons: 1-Week=`-2.33M` | 15-Day=`-5.86M` | 30-Day=`-20.45M` | Market Cap=`911.62M`

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
- **Stand-Aside Reason**: Gate 1 Spread Friction Failure: Spread friction 218.69 bps exceeds cap 25.0 bps. Standing aside in 100% cash preserves statutory floor.