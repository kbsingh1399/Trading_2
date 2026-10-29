# 🔬 MASTER 43-FEED QUANTITATIVE DOSSIER: BATUSD (Basic Attention Token / USD)
**MT5 Symbol**: `BATUSD.p` | **Category**: `Crypto Altcoin` | **Tier**: `Tier 2`
**Execution Posture**: `DISQUALIFIED` | **Timestamp**: 2026-10-29 14:43:14 UTC
**Pipeline Clearance**: `BLOCKED` | **Data Freshness**: `1.2m`

---

## 1. MT5 Live Broker Telemetry & Spread Friction Gate
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet)*
- **Live Bid Quote**: `0.13560` | **Live Ask Quote**: `0.13780` | **Mid Price**: `0.13670`
- **Spread Points**: `22.0 pts` | **Spread BPS**: `160.94 bps` (Mandatory Cap: `25.0 bps`)
- **Gate Status**: **`FAIL`** (Spread friction 160.94 bps exceeds cap 25.0 bps)
- **Order Allowed**: `NONE` | **Pillar 1 Clearance**: `BLOCKED`
- **Broker Specifications**: Contract Size=`1.00` | Tick Value=`1.00 USD` | Min Lot=`0.01` | Digits=`5`
- **Account Capital Context**: Balance=`4,744.55 USD` | Equity=`4,744.32 USD` | Free Margin=`4,342.62 USD` | Inviolate Hard Floor=`4,775.00 USD` (Cushion: `-30.68 USD`)
- **Pipeline Health**: Feed #00 Status=`PASS` | Overall Pipeline Telemetry=`33/33 FEEDS PASS (SYNCHRONIZED)`

---

## 2. Technical Profile, Multi-Sigma VWAP Dispersion & Volatility
*(Sources: 11_Technical.parquet, 11_Technical_BTC_Ribbon.parquet)*
- **Last Verified Price**: `0.13720` | **24h Change**: `-1.37%` (24h High: `0.14360`, 24h Low: `0.13500`)
- **Weekly Range**: Week High=`0.15280` | Week Low=`0.13500` | Daily POC=`0.13719` | Daily VAH=`0.13806` | Daily VAL=`0.13601`
- **Session VWAP**: `0.13733` | **Rolling 24h VWAP**: `0.13814` | **Distance to VWAP**: `-0.10%`
- **VWAP Z-Score**: `-0.11 sigma` | **Mean Reversion Bias**: **`FAIR VALUE`**
- **VWAP Dispersion Bands**:
  * +1.00 sigma: `0.13847` | -1.00 sigma: `0.13619`
  * +1.28 sigma (80% CI): `0.13879` | -1.28 sigma: `0.13587`
  * +2.00 sigma (95% CI): `0.13961` | -2.00 sigma: `0.13506`
  * +2.01 sigma: `0.13962` | -2.01 sigma: `0.13504`
  * +2.51 sigma (98.8% CI): `0.14019` | -2.51 sigma: `0.13447`
  * +3.00 sigma (99.7% CI Extreme): `0.14074` | -3.00 sigma: `0.13392`
- **Oscillators & Volatility**:
  * **RSI (14)**: `53.36` | **RSI State**: **`NEUTRAL`**
  * **ATR (14)**: `0.00094` | **ATR %**: `0.68%`
  * **Bollinger Bands**: Upper=`0.13774` | Mid=`0.13643` | Lower=`0.13513` | Bandwidth=`1.92%`
  * **MACD**: Line=`-0.0000` | Signal=`-0.0001` | Hist=`+0.0001`
- **Exponential Moving Average Ribbon (EMA)**:
  * Short Horizon: EMA-5=`0.13692` | EMA-9=`0.13685` | EMA-13=`0.13678` | EMA-20=`0.13675`
  * Intermediate: EMA-34=`0.13693` | EMA-50=`0.13733` | EMA-89=`0.13851` | EMA-100=`0.13883`
  * Institutional: EMA-144=`0.13984` | EMA-200=`0.14060` (Slope: `-0.343%`) | EMA-233=`0.14142` (Slope: `-0.353%`)
  * **Trend Bias**: **`NEUTRAL / CHOP`**

---

## 3. Auction Market Structure & Value Profile
*(Sources: 20_Auction_Market_Structure.parquet)*
- **Daily Auction Value Area**:
  * High (VAH): `0.13806` | Point of Control (POC): `0.13719` | Low (VAL): `0.13601`
  * Distance to POC: `+0.00%` | Distance to VAH: `+0.00%` | Distance to VAL: `+0.00%`
  * **Value Area Position**: **`INSIDE_VALUE (Balance)`** | **Auction Regime**: **`BALANCED_AUCTION`** | **Session Bias**: **`NEUTRAL`**
- **Prior Day & Weekly Auction Profile**:
  * Prior Day: PD VAH=`0.13725` | PD POC=`0.13670` | PD VAL=`0.13615` | PDH=`0.13752` | PDL=`0.13588` | PDC=`0.13670`
  * Monday Reference: Monday High=`0.13738` | Monday Low=`0.13602` | Monday Mid=`0.13670`
  * Weekly Value Area: Weekly VAH=`0.13779` | Weekly POC=`0.13670` | Weekly VAL=`0.13561`
  * Multi-Week Extremes: Current Week High (CWH)=`0.13807` | CWL=`0.13533` | Prior Week High (PWH)=`0.13875` | PWL=`0.13465`
  * Multi-Month Extremes: Current Month High (CMH)=`0.13943` | CML=`0.13397` | Prior Month High (PMH)=`0.14012` | PML=`0.13328`
- **Session Liquidity Extremes & Initial Balance**:
  * Asian Session: Range `[0.13643 - 0.13697]`
  * London Session: Range `[0.13615 - 0.13725]`
  * New York Session: Range `[0.13602 - 0.13738]`
  * Initial Balance (IB): IB High=`0.13711` | IB Low=`0.13629`
- **Fibonacci Golden Pocket & Optimal Trade Entry (OTE)**:
  * Swing Range: High=`0.14360` | Low=`0.13500` | Direction=`NONE`
  * Golden Pocket [0.618 - 0.65]: `[0.13643 - 0.13697]`
  * Optimal Trade Entry (0.702): `0.13670` | Invalidation Level: `0.00000` | Status: **`NONE`**
- **Classical & Weekly Pivots**:
  * Daily Classical: Pivot=`0.13670` | R1=`0.13711` | S1=`0.13629` | R2=`0.13752` | S2=`0.13588`
  * Weekly Classical: Weekly Pivot=`0.13670` | Weekly R1=`0.13807` | Weekly S1=`0.13533`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Orderflow
*(Sources: 18_CVD.parquet, 18_CVD_30D_5m.parquet, 18_CVD_30D_15m.parquet, 18_CVD_30D_1h.parquet, 18_CVD_30D_4h.parquet, 18_CVD_30D_ALL.parquet, 21_Tradfye_Orderflow.parquet)*
- **Interbank Spot Orderflow Mechanics**: Decentralized OTC market structure. CVD taker deltas do not apply to interbank spot flow. Tape volume governed by broker tick volume with live spread friction of `160.94 bps`.
- **Session Volume Structure**: Price operating at `INSIDE_VALUE (Balance)` with Daily POC at `0.13719` (VAH: `0.13806` / VAL: `0.13601`).

---

## 5. Institutional Whale Armor & Resting Orderbook Depth
*(Sources: 10_Whale_Orders.parquet, 12_Hyperdash.parquet, 17_Orderbook.parquet, 4_Hyperliquid_Analysis.parquet)*
- **Interbank Institutional Tier-1 Depth**: Decentralized OTC spot liquidity. Resting whale limit walls from crypto venues do not apply.
- **Verified Broker Armor**: Live Bid `0.13560` / Live Ask `0.13780` with institutional spread of `160.94 bps`. Structural defense anchored at Asian Range `[0.13643 - 0.13697]` and London Range `[0.13615 - 0.13725]`.

---

## 6. Liquidation Max Pain, Heatmaps & Cascade Boundaries
*(Sources: 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 14_Hyperdash_Liq_Map.parquet, 14_Liquidation_Matrix.parquet, 15_Hyperdash_Stops_Map.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`0.15151` (Vol: `31,835 USD`, Dist: `+3.59%`) | Long MP=`0.13720` (Vol: `31,547 USD`, Dist: `-6.19%`)
  * 48H Horizon: Short MP=`0.15151` (Vol: `31,835 USD`, Dist: `+3.59%`) | Long MP=`0.13859` (Vol: `36,270 USD`, Dist: `-5.24%`)
  * 3D Horizon: Short MP=`0.15146` (Vol: `31,835 USD`, Dist: `+3.60%`) | Long MP=`0.13850` (Vol: `31,611 USD`, Dist: `-5.26%`)
  * 7D Horizon: Short MP=`0.22393` (Vol: `104,012 USD`, Dist: `+54.41%`) | Long MP=`0.13868` (Vol: `46,128 USD`, Dist: `-4.37%`)
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
  * Major CEX Rates: Binance=`+0.0100%` | OKX=`+0.0079%` | Bybit=`+0.0100%` | Bitget=`+0.0092%`
  * Mid-Tier CEX Rates: KuCoin=`+0.0100%` | MEXC=`+0.0082%` | Gate=`+0.0100%` | BingX=`+0.0100%` | Bitunix=`+0.0100%`
  * Alternative Venues: WhiteBIT=`+0.0100%` | LBank=`+0.0000%` | tradeXYZ=`-`
  * Inverse Coin-Margined: CoinM Binance=`+0.0000%` | CoinM OKX=`+0.0000%` | CoinM Bybit=`+0.0000%`
- **Exchange Long / Short Ratio Dynamics (3_Exchanges_LS_Ratio*.parquet)**:
  * 15m Tactical: L/S Ratio=`1.00` (Longs: `50.00%`, Shorts: `50.00%`, Total Vol: `0.00 USD`)
  * 1h Primary: L/S Ratio=`1.00` (Longs: `50.00%`, Shorts: `50.00%`, Total Vol: `0.00 USD`)
  * 4h Macro: L/S Ratio=`1.00` (Longs: `50.00%`, Shorts: `50.00%`, Total Vol: `0.00 USD`)
- **Funding Fee Settlement & DEX Arbitrage (6_Funding_Fee_Settlement.parquet, 13_Hyperliquid.parquet)**:
  * Settlement Payouts: Current Expected=`1.15K USD` | Last 24h=`1.34K USD` | Last 3D=`5.40K USD` | Last 7D=`8.98K USD`

---

## 8. Microstructure Footprint, Tape Imbalances & Macro Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 16_Hyperdash_telegram_Intel.parquet, 19_News.parquet, 19_Calendar.parquet)*
- **Bar-by-Bar Microstructure Footprint (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
  * Venue Source: `Aggregated` | Timeframe: `15m` | Last Price: `0.13670`
  * Footprint Auction Profile: Bar VWAP=`0.13670` | Bar POC=`0.13670` | Bar VAH=`0.13697` | Bar VAL=`0.13643`
  * Orderflow Volumes: Total Vol=`0.00 USD` | Taker Buy=`0.00 USD` | Taker Sell=`0.00 USD`
  * Bar Delta Profile: Delta=`+0.00 USD` (`+0.00%`) | Max Delta=`+0.00 USD` | Min Delta=`+0.00 USD` | Cumulative Bar Delta=`+0.00 USD`
  * Order Execution Dynamics: Trades Count=`0` | Avg Trade Size=`0.00 USD`
  * Tape Imbalances: Imbalance Ratio=`0.0%` | Buy Imbalances Count=`0` | Sell Imbalances Count=`0`
  * Footprint Open Interest: Bar OI=`0.00 USD` | Bar OI Change=`+0.00 USD`
- **Multi-Horizon Macro Capital Netflows (2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet)**:
  * Spot Capital Netflows:
    - Tactical: 5m=`-20.05K` | 15m=`-15.89K` | 30m=`-3.17K` | 1h=`-1.13K`
    - Intermediate: 2h=`-12.83K` | 4h=`-7.35K` | 6h=`-19.27K` | 8h=`+3.06K` | 12h=`+126.91` | 24h=`+109.15K`
    - Macro Horizons: 1-Week=`-977.01K` | 15-Day=`-6.40M` | 30-Day=`-6.39M` | Market Cap=`206.06M`
  * Futures Capital Netflows:
    - Tactical: 5m=`-46.55K` | 15m=`-51.01K` | 30m=`-10.34K` | 1h=`-69.97K`
    - Intermediate: 2h=`+44.40K` | 4h=`+108.07K` | 6h=`+84.43K` | 8h=`+276.94K` | 12h=`+603.03K` | 24h=`+970.46K`
    - Macro Horizons: 1-Week=`+119.60K` | 15-Day=`+8.67M` | 30-Day=`+24.61M` | Market Cap=`206.06M`

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
- **Stand-Aside Reason**: Gate 1 Spread Friction Failure: Spread friction 160.94 bps exceeds cap 25.0 bps. Standing aside in 100% cash preserves statutory floor.