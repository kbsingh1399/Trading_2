# 🔬 MASTER 43-FEED QUANTITATIVE DOSSIER: SNXUSD (SNX/USD)
**MT5 Symbol**: `SNXUSD.p` | **Category**: `Forex Cross` | **Tier**: `Tier 2`
**Execution Posture**: `DISQUALIFIED` | **Timestamp**: 2026-10-29 14:43:14 UTC
**Pipeline Clearance**: `BLOCKED` | **Data Freshness**: `1.2m`

---

## 1. MT5 Live Broker Telemetry & Spread Friction Gate
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet)*
- **Live Bid Quote**: `0.19000` | **Live Ask Quote**: `0.21000` | **Mid Price**: `0.20000`
- **Spread Points**: `20.0 pts` | **Spread BPS**: `1000.00 bps` (Mandatory Cap: `25.0 bps`)
- **Gate Status**: **`FAIL`** (Spread friction 1000.00 bps exceeds cap 25.0 bps)
- **Order Allowed**: `NONE` | **Pillar 1 Clearance**: `BLOCKED`
- **Broker Specifications**: Contract Size=`1.00` | Tick Value=`1.00 USD` | Min Lot=`0.01` | Digits=`5`
- **Account Capital Context**: Balance=`4,744.55 USD` | Equity=`4,744.32 USD` | Free Margin=`4,342.62 USD` | Inviolate Hard Floor=`4,775.00 USD` (Cushion: `-30.68 USD`)
- **Pipeline Health**: Feed #00 Status=`PASS` | Overall Pipeline Telemetry=`33/33 FEEDS PASS (SYNCHRONIZED)`

---

## 2. Technical Profile, Multi-Sigma VWAP Dispersion & Volatility
*(Sources: 11_Technical.parquet, 11_Technical_BTC_Ribbon.parquet)*
- **Last Verified Price**: `0.19000` | **24h Change**: `+1.60%` (24h High: `0.19600`, 24h Low: `0.18400`)
- **Weekly Range**: Week High=`0.19600` | Week Low=`0.18300` | Daily POC=`0.18500` | Daily VAH=`0.19000` | Daily VAL=`0.18500`
- **Session VWAP**: `0.18740` | **Rolling 24h VWAP**: `0.18866` | **Distance to VWAP**: `+1.39%`
- **VWAP Z-Score**: `+1.28 sigma` | **Mean Reversion Bias**: **`FAIR VALUE`**
- **VWAP Dispersion Bands**:
  * +1.00 sigma: `0.18943` | -1.00 sigma: `0.18536`
  * +1.28 sigma (80% CI): `0.19000` | -1.28 sigma: `0.18479`
  * +2.00 sigma (95% CI): `0.19146` | -2.00 sigma: `0.18333`
  * +2.01 sigma: `0.19148` | -2.01 sigma: `0.18331`
  * +2.51 sigma (98.8% CI): `0.19250` | -2.51 sigma: `0.18229`
  * +3.00 sigma (99.7% CI Extreme): `0.19349` | -3.00 sigma: `0.18130`
- **Oscillators & Volatility**:
  * **RSI (14)**: `70.37` | **RSI State**: **`OVERBOUGHT`**
  * **ATR (14)**: `0.00079` | **ATR %**: `0.42%`
  * **Bollinger Bands**: Upper=`0.19060` | Mid=`0.18780` | Lower=`0.18500` | Bandwidth=`2.98%`
  * **MACD**: Line=`+0.0008` | Signal=`+0.0005` | Hist=`+0.0003`
- **Exponential Moving Average Ribbon (EMA)**:
  * Short Horizon: EMA-5=`0.18948` | EMA-9=`0.18907` | EMA-13=`0.18869` | EMA-20=`0.18822`
  * Intermediate: EMA-34=`0.18786` | EMA-50=`0.18788` | EMA-89=`0.18826` | EMA-100=`0.18834`
  * Institutional: EMA-144=`0.18843` | EMA-200=`0.18818` (Slope: `+0.040%`) | EMA-233=`0.18808` (Slope: `+0.040%`)
  * **Trend Bias**: **`BULLISH`**

---

## 3. Auction Market Structure & Value Profile
*(Sources: 20_Auction_Market_Structure.parquet)*
- **Daily Auction Value Area**:
  * High (VAH): `0.19000` | Point of Control (POC): `0.18500` | Low (VAL): `0.18500`
  * Distance to POC: `+8.13%` | Distance to VAH: `+5.43%` | Distance to VAL: `+8.13%`
  * **Value Area Position**: **`ABOVE_VALUE (Imbalance)`** | **Auction Regime**: **`TREND_UP_ACCEPTANCE`** | **Session Bias**: **`BULLISH (Above Pivot)`**
- **Prior Day & Weekly Auction Profile**:
  * Prior Day: PD VAH=`0.19200` | PD POC=`0.19100` | PD VAL=`0.18900` | PDH=`0.19600` | PDL=`0.18700` | PDC=`0.19200`
  * Monday Reference: Monday High=`0.19000` | Monday Low=`0.18300` | Monday Mid=`0.18600`
  * Weekly Value Area: Weekly VAH=`0.19000` | Weekly POC=`0.18500` | Weekly VAL=`0.18400`
  * Multi-Week Extremes: Current Week High (CWH)=`0.19600` | CWL=`0.18300` | Prior Week High (PWH)=`0.22100` | PWL=`0.18300`
  * Multi-Month Extremes: Current Month High (CMH)=`0.25200` | CML=`0.18300` | Prior Month High (PMH)=`0.26700` | PML=`0.18400`
- **Session Liquidity Extremes & Initial Balance**:
  * Asian Session: Range `[0.18500 - 0.19400]`
  * London Session: Range `[0.18400 - 0.18900]`
  * New York Session: Range `[0.18600 - 0.19100]`
  * Initial Balance (IB): IB High=`0.18900` | IB Low=`0.18600`
- **Fibonacci Golden Pocket & Optimal Trade Entry (OTE)**:
  * Swing Range: High=`0.19600` | Low=`0.18400` | Direction=`BEARISH_IMPULSE`
  * Golden Pocket [0.618 - 0.65]: `[0.19100 - 0.19200]`
  * Optimal Trade Entry (0.702): `0.19200` | Invalidation Level: `0.19300` | Status: **`STRUCTURE_INVALIDATED`**
- **Classical & Weekly Pivots**:
  * Daily Classical: Pivot=`0.19200` | R1=`0.19600` | S1=`0.18700` | R2=`0.20100` | S2=`0.18300`
  * Weekly Classical: Weekly Pivot=`0.19700` | Weekly R1=`0.21100` | Weekly S1=`0.17300`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Orderflow
*(Sources: 18_CVD.parquet, 18_CVD_30D_5m.parquet, 18_CVD_30D_15m.parquet, 18_CVD_30D_1h.parquet, 18_CVD_30D_4h.parquet, 18_CVD_30D_ALL.parquet, 21_Tradfye_Orderflow.parquet)*
- **Interbank Spot Orderflow Mechanics**: Decentralized OTC market structure. CVD taker deltas do not apply to interbank spot flow. Tape volume governed by broker tick volume with live spread friction of `1000.00 bps`.
- **Session Volume Structure**: Price operating at `ABOVE_VALUE (Imbalance)` with Daily POC at `0.18500` (VAH: `0.19000` / VAL: `0.18500`).

---

## 5. Institutional Whale Armor & Resting Orderbook Depth
*(Sources: 10_Whale_Orders.parquet, 12_Hyperdash.parquet, 17_Orderbook.parquet, 4_Hyperliquid_Analysis.parquet)*
- **Interbank Institutional Tier-1 Depth**: Decentralized OTC spot liquidity. Resting whale limit walls from crypto venues do not apply.
- **Verified Broker Armor**: Live Bid `0.19000` / Live Ask `0.21000` with institutional spread of `1000.00 bps`. Structural defense anchored at Asian Range `[0.18500 - 0.19400]` and London Range `[0.18400 - 0.18900]`.

---

## 6. Liquidation Max Pain, Heatmaps & Cascade Boundaries
*(Sources: 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 14_Hyperdash_Liq_Map.parquet, 14_Liquidation_Matrix.parquet, 15_Hyperdash_Stops_Map.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`0.20304` (Vol: `5,068 USD`, Dist: `+2.13%`) | Long MP=`0.19136` (Vol: `8,564 USD`, Dist: `-3.74%`)
  * 48H Horizon: Short MP=`0.20086` (Vol: `6,141 USD`, Dist: `+1.04%`) | Long MP=`0.19110` (Vol: `10,670 USD`, Dist: `-3.87%`)
  * 3D Horizon: Short MP=`0.20293` (Vol: `8,461 USD`, Dist: `+2.08%`) | Long MP=`0.19120` (Vol: `11,981 USD`, Dist: `-3.82%`)
  * 7D Horizon: Short MP=`0.23490` (Vol: `11,910 USD`, Dist: `+18.40%`) | Long MP=`0.19140` (Vol: `14,644 USD`, Dist: `-3.53%`)
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
  * Major CEX Rates: Binance=`+0.0100%` | OKX=`+0.0100%` | Bybit=`+0.0100%` | Bitget=`+0.0100%`
  * Mid-Tier CEX Rates: KuCoin=`+0.0100%` | MEXC=`+0.0100%` | Gate=`+0.0100%` | BingX=`+0.0100%` | Bitunix=`+0.0060%`
  * Alternative Venues: WhiteBIT=`+0.0100%` | LBank=`+0.0100%` | tradeXYZ=`-`
  * Inverse Coin-Margined: CoinM Binance=`+0.0000%` | CoinM OKX=`+0.0000%` | CoinM Bybit=`+0.0000%`
- **Exchange Long / Short Ratio Dynamics (3_Exchanges_LS_Ratio*.parquet)**:
  * 15m Tactical: L/S Ratio=`1.00` (Longs: `50.00%`, Shorts: `50.00%`, Total Vol: `0.00 USD`)
  * 1h Primary: L/S Ratio=`1.00` (Longs: `50.00%`, Shorts: `50.00%`, Total Vol: `0.00 USD`)
  * 4h Macro: L/S Ratio=`1.00` (Longs: `50.00%`, Shorts: `50.00%`, Total Vol: `0.00 USD`)
- **Funding Fee Settlement & DEX Arbitrage (6_Funding_Fee_Settlement.parquet, 13_Hyperliquid.parquet)**:
  * Settlement Payouts: Current Expected=`432.06 USD` | Last 24h=`770.14 USD` | Last 3D=`2.27K USD` | Last 7D=`3.03K USD`

---

## 8. Microstructure Footprint, Tape Imbalances & Macro Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 16_Hyperdash_telegram_Intel.parquet, 19_News.parquet, 19_Calendar.parquet)*
- **Decentralized Spot Flow Profile**: Footprint bar metrics and crypto ETF flows not applicable to OTC spot interbank asset.
- **Institutional Tape Dynamics**: Multi-dealer foreign exchange volume driven by international trade settlements, sovereign reserve reallocation, and London/NY fixing windows.

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
- **Stand-Aside Reason**: Gate 1 Spread Friction Failure: Spread friction 1000.00 bps exceeds cap 25.0 bps. Standing aside in 100% cash preserves statutory floor.