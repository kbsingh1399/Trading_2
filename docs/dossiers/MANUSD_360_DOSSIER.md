# 🔬 MASTER 43-FEED QUANTITATIVE DOSSIER: MANUSD (Decentraland / USD)
**MT5 Symbol**: `MANUSD.p` | **Category**: `Crypto Altcoin` | **Tier**: `Tier 2`
**Execution Posture**: `DISQUALIFIED` | **Timestamp**: 2026-10-29 14:43:14 UTC
**Pipeline Clearance**: `BLOCKED` | **Data Freshness**: `1.2m`

---

## 1. MT5 Live Broker Telemetry & Spread Friction Gate
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet)*
- **Live Bid Quote**: `0.07680` | **Live Ask Quote**: `0.07890` | **Mid Price**: `0.07785`
- **Spread Points**: `21.0 pts` | **Spread BPS**: `269.75 bps` (Mandatory Cap: `25.0 bps`)
- **Gate Status**: **`FAIL`** (Spread friction 269.75 bps exceeds cap 25.0 bps)
- **Order Allowed**: `NONE` | **Pillar 1 Clearance**: `BLOCKED`
- **Broker Specifications**: Contract Size=`1.00` | Tick Value=`1.00 USD` | Min Lot=`0.01` | Digits=`5`
- **Account Capital Context**: Balance=`4,744.55 USD` | Equity=`4,744.32 USD` | Free Margin=`4,342.62 USD` | Inviolate Hard Floor=`4,775.00 USD` (Cushion: `-30.68 USD`)
- **Pipeline Health**: Feed #00 Status=`PASS` | Overall Pipeline Telemetry=`33/33 FEEDS PASS (SYNCHRONIZED)`

---

## 2. Technical Profile, Multi-Sigma VWAP Dispersion & Volatility
*(Sources: 11_Technical.parquet, 11_Technical_BTC_Ribbon.parquet)*
- **Last Verified Price**: `0.07670` | **24h Change**: `-0.13%` (24h High: `0.08020`, 24h Low: `0.07430`)
- **Weekly Range**: Week High=`0.08020` | Week Low=`0.07430` | Daily POC=`0.07579` | Daily VAH=`0.07634` | Daily VAL=`0.07470`
- **Session VWAP**: `0.07586` | **Rolling 24h VWAP**: `0.07684` | **Distance to VWAP**: `+1.11%`
- **VWAP Z-Score**: `+0.90 sigma` | **Mean Reversion Bias**: **`FAIR VALUE`**
- **VWAP Dispersion Bands**:
  * +1.00 sigma: `0.07679` | -1.00 sigma: `0.07493`
  * +1.28 sigma (80% CI): `0.07705` | -1.28 sigma: `0.07467`
  * +2.00 sigma (95% CI): `0.07773` | -2.00 sigma: `0.07399`
  * +2.01 sigma: `0.07774` | -2.01 sigma: `0.07398`
  * +2.51 sigma (98.8% CI): `0.07820` | -2.51 sigma: `0.07352`
  * +3.00 sigma (99.7% CI Extreme): `0.07866` | -3.00 sigma: `0.07306`
- **Oscillators & Volatility**:
  * **RSI (14)**: `66.52` | **RSI State**: **`BULLISH`**
  * **ATR (14)**: `0.00037` | **ATR %**: `0.48%`
  * **Bollinger Bands**: Upper=`0.07683` | Mid=`0.07580` | Lower=`0.07476` | Bandwidth=`2.73%`
  * **MACD**: Line=`+0.0003` | Signal=`+0.0002` | Hist=`+0.0001`
- **Exponential Moving Average Ribbon (EMA)**:
  * Short Horizon: EMA-5=`0.07646` | EMA-9=`0.07627` | EMA-13=`0.07612` | EMA-20=`0.07593`
  * Intermediate: EMA-34=`0.07586` | EMA-50=`0.07598` | EMA-89=`0.07636` | EMA-100=`0.07645`
  * Institutional: EMA-144=`0.07669` | EMA-200=`0.07680` (Slope: `-0.109%`) | EMA-233=`0.07683` (Slope: `-0.097%`)
  * **Trend Bias**: **`NEUTRAL / CHOP`**

---

## 3. Auction Market Structure & Value Profile
*(Sources: 20_Auction_Market_Structure.parquet)*
- **Daily Auction Value Area**:
  * High (VAH): `0.07634` | Point of Control (POC): `0.07579` | Low (VAL): `0.07470`
  * Distance to POC: `+0.00%` | Distance to VAH: `+0.00%` | Distance to VAL: `+0.00%`
  * **Value Area Position**: **`INSIDE_VALUE (Balance)`** | **Auction Regime**: **`BALANCED_AUCTION`** | **Session Bias**: **`NEUTRAL`**
- **Prior Day & Weekly Auction Profile**:
  * Prior Day: PD VAH=`0.07816` | PD POC=`0.07785` | PD VAL=`0.07754` | PDH=`0.07832` | PDL=`0.07738` | PDC=`0.07785`
  * Monday Reference: Monday High=`0.07824` | Monday Low=`0.07746` | Monday Mid=`0.07785`
  * Weekly Value Area: Weekly VAH=`0.07847` | Weekly POC=`0.07785` | Weekly VAL=`0.07723`
  * Multi-Week Extremes: Current Week High (CWH)=`0.07863` | CWL=`0.07707` | Prior Week High (PWH)=`0.07902` | PWL=`0.07668`
  * Multi-Month Extremes: Current Month High (CMH)=`0.07941` | CML=`0.07629` | Prior Month High (PMH)=`0.07980` | PML=`0.07590`
- **Session Liquidity Extremes & Initial Balance**:
  * Asian Session: Range `[0.07769 - 0.07801]`
  * London Session: Range `[0.07754 - 0.07816]`
  * New York Session: Range `[0.07746 - 0.07824]`
  * Initial Balance (IB): IB High=`0.07808` | IB Low=`0.07762`
- **Fibonacci Golden Pocket & Optimal Trade Entry (OTE)**:
  * Swing Range: High=`0.08020` | Low=`0.07430` | Direction=`NONE`
  * Golden Pocket [0.618 - 0.65]: `[0.07769 - 0.07801]`
  * Optimal Trade Entry (0.702): `0.07785` | Invalidation Level: `0.00000` | Status: **`NONE`**
- **Classical & Weekly Pivots**:
  * Daily Classical: Pivot=`0.07785` | R1=`0.07808` | S1=`0.07762` | R2=`0.07832` | S2=`0.07738`
  * Weekly Classical: Weekly Pivot=`0.07785` | Weekly R1=`0.07863` | Weekly S1=`0.07707`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Orderflow
*(Sources: 18_CVD.parquet, 18_CVD_30D_5m.parquet, 18_CVD_30D_15m.parquet, 18_CVD_30D_1h.parquet, 18_CVD_30D_4h.parquet, 18_CVD_30D_ALL.parquet, 21_Tradfye_Orderflow.parquet)*
- **Interbank Spot Orderflow Mechanics**: Decentralized OTC market structure. CVD taker deltas do not apply to interbank spot flow. Tape volume governed by broker tick volume with live spread friction of `269.75 bps`.
- **Session Volume Structure**: Price operating at `INSIDE_VALUE (Balance)` with Daily POC at `0.07579` (VAH: `0.07634` / VAL: `0.07470`).

---

## 5. Institutional Whale Armor & Resting Orderbook Depth
*(Sources: 10_Whale_Orders.parquet, 12_Hyperdash.parquet, 17_Orderbook.parquet, 4_Hyperliquid_Analysis.parquet)*
- **Interbank Institutional Tier-1 Depth**: Decentralized OTC spot liquidity. Resting whale limit walls from crypto venues do not apply.
- **Verified Broker Armor**: Live Bid `0.07680` / Live Ask `0.07890` with institutional spread of `269.75 bps`. Structural defense anchored at Asian Range `[0.07769 - 0.07801]` and London Range `[0.07754 - 0.07816]`.

---

## 6. Liquidation Max Pain, Heatmaps & Cascade Boundaries
*(Sources: 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 14_Hyperdash_Liq_Map.parquet, 14_Liquidation_Matrix.parquet, 15_Hyperdash_Stops_Map.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`0.07927` (Vol: `15,503 USD`, Dist: `+1.42%`) | Long MP=`0.07620` (Vol: `16,115 USD`, Dist: `-2.51%`)
  * 48H Horizon: Short MP=`0.07931` (Vol: `16,115 USD`, Dist: `+1.47%`) | Long MP=`0.07616` (Vol: `18,356 USD`, Dist: `-2.56%`)
  * 3D Horizon: Short MP=`0.08118` (Vol: `14,103 USD`, Dist: `+3.87%`) | Long MP=`0.07615` (Vol: `28,390 USD`, Dist: `-2.58%`)
  * 7D Horizon: Short MP=`0.08120` (Vol: `21,062 USD`, Dist: `+4.25%`) | Long MP=`0.07619` (Vol: `29,406 USD`, Dist: `-2.18%`)
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
  * Major CEX Rates: Binance=`+0.0043%` | OKX=`+0.0090%` | Bybit=`+0.0100%` | Bitget=`+0.0100%`
  * Mid-Tier CEX Rates: KuCoin=`+0.0100%` | MEXC=`+0.0045%` | Gate=`+0.0100%` | BingX=`+0.0100%` | Bitunix=`+0.0047%`
  * Alternative Venues: WhiteBIT=`+0.0100%` | LBank=`+0.0045%` | tradeXYZ=`-`
  * Inverse Coin-Margined: CoinM Binance=`+0.0000%` | CoinM OKX=`+0.0000%` | CoinM Bybit=`+0.0000%`
- **Exchange Long / Short Ratio Dynamics (3_Exchanges_LS_Ratio*.parquet)**:
  * 15m Tactical: L/S Ratio=`1.00` (Longs: `50.00%`, Shorts: `50.00%`, Total Vol: `0.00 USD`)
  * 1h Primary: L/S Ratio=`1.00` (Longs: `50.00%`, Shorts: `50.00%`, Total Vol: `0.00 USD`)
  * 4h Macro: L/S Ratio=`1.00` (Longs: `50.00%`, Shorts: `50.00%`, Total Vol: `0.00 USD`)
- **Funding Fee Settlement & DEX Arbitrage (6_Funding_Fee_Settlement.parquet, 13_Hyperliquid.parquet)**:
  * Settlement Payouts: Current Expected=`474.71 USD` | Last 24h=`-133.23 USD` | Last 3D=`2.67K USD` | Last 7D=`2.32K USD`

---

## 8. Microstructure Footprint, Tape Imbalances & Macro Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 16_Hyperdash_telegram_Intel.parquet, 19_News.parquet, 19_Calendar.parquet)*
- **Bar-by-Bar Microstructure Footprint (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
  * Venue Source: `Aggregated` | Timeframe: `15m` | Last Price: `0.07785`
  * Footprint Auction Profile: Bar VWAP=`0.07785` | Bar POC=`0.07785` | Bar VAH=`0.07801` | Bar VAL=`0.07769`
  * Orderflow Volumes: Total Vol=`0.00 USD` | Taker Buy=`0.00 USD` | Taker Sell=`0.00 USD`
  * Bar Delta Profile: Delta=`+0.00 USD` (`+0.00%`) | Max Delta=`+0.00 USD` | Min Delta=`+0.00 USD` | Cumulative Bar Delta=`+0.00 USD`
  * Order Execution Dynamics: Trades Count=`0` | Avg Trade Size=`0.00 USD`
  * Tape Imbalances: Imbalance Ratio=`0.0%` | Buy Imbalances Count=`0` | Sell Imbalances Count=`0`
  * Footprint Open Interest: Bar OI=`0.00 USD` | Bar OI Change=`+0.00 USD`
- **Multi-Horizon Macro Capital Netflows (2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet)**:
  * Spot Capital Netflows:
    - Tactical: 5m=`-520.48` | 15m=`-1.42K` | 30m=`-9.19K` | 1h=`-6.53K`
    - Intermediate: 2h=`-2.45K` | 4h=`-576.06` | 6h=`+2.43K` | 8h=`+3.02K` | 12h=`+1.64K` | 24h=`-12.83K`
    - Macro Horizons: 1-Week=`-146.14K` | 15-Day=`-293.01K` | 30-Day=`-4.88M` | Market Cap=`154.38M`
  * Futures Capital Netflows:
    - Tactical: 5m=`-5.03K` | 15m=`-3.69K` | 30m=`-15.37K` | 1h=`+1.48K`
    - Intermediate: 2h=`-2.46K` | 4h=`-48.00K` | 6h=`-71.31K` | 8h=`-11.45K` | 12h=`-105.93K` | 24h=`+17.04K`
    - Macro Horizons: 1-Week=`-405.66K` | 15-Day=`-1.24M` | 30-Day=`-16.21M` | Market Cap=`154.38M`

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
- **Stand-Aside Reason**: Gate 1 Spread Friction Failure: Spread friction 269.75 bps exceeds cap 25.0 bps. Standing aside in 100% cash preserves statutory floor.