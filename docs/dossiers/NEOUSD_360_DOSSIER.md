# 🔬 MASTER 43-FEED QUANTITATIVE DOSSIER: NEOUSD (NEO/USD)
**MT5 Symbol**: `NEOUSD.p` | **Category**: `Forex Cross` | **Tier**: `Tier 2`
**Execution Posture**: `DISQUALIFIED` | **Timestamp**: 2026-10-29 14:43:14 UTC
**Pipeline Clearance**: `BLOCKED` | **Data Freshness**: `1.2m`

---

## 1. MT5 Live Broker Telemetry & Spread Friction Gate
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet)*
- **Live Bid Quote**: `2.11200` | **Live Ask Quote**: `2.13700` | **Mid Price**: `2.12450`
- **Spread Points**: `250.0 pts` | **Spread BPS**: `117.67 bps` (Mandatory Cap: `25.0 bps`)
- **Gate Status**: **`FAIL`** (Spread friction 117.67 bps exceeds cap 25.0 bps)
- **Order Allowed**: `NONE` | **Pillar 1 Clearance**: `BLOCKED`
- **Broker Specifications**: Contract Size=`1.00` | Tick Value=`1.00 USD` | Min Lot=`0.01` | Digits=`5`
- **Account Capital Context**: Balance=`4,744.55 USD` | Equity=`4,744.32 USD` | Free Margin=`4,342.62 USD` | Inviolate Hard Floor=`4,775.00 USD` (Cushion: `-30.68 USD`)
- **Pipeline Health**: Feed #00 Status=`PASS` | Overall Pipeline Telemetry=`33/33 FEEDS PASS (SYNCHRONIZED)`

---

## 2. Technical Profile, Multi-Sigma VWAP Dispersion & Volatility
*(Sources: 11_Technical.parquet, 11_Technical_BTC_Ribbon.parquet)*
- **Last Verified Price**: `2.10500` | **24h Change**: `+1.30%` (24h High: `2.14900`, 24h Low: `2.04400`)
- **Weekly Range**: Week High=`2.14900` | Week Low=`2.01600` | Daily POC=`2.05000` | Daily VAH=`2.10000` | Daily VAL=`2.04000`
- **Session VWAP**: `2.07632` | **Rolling 24h VWAP**: `2.08862` | **Distance to VWAP**: `+1.38%`
- **VWAP Z-Score**: `+1.33 sigma` | **Mean Reversion Bias**: **`FAIR VALUE`**
- **VWAP Dispersion Bands**:
  * +1.00 sigma: `2.09784` | -1.00 sigma: `2.05481`
  * +1.28 sigma (80% CI): `2.10386` | -1.28 sigma: `2.04879`
  * +2.00 sigma (95% CI): `2.11935` | -2.00 sigma: `2.03330`
  * +2.01 sigma: `2.11956` | -2.01 sigma: `2.03308`
  * +2.51 sigma (98.8% CI): `2.13032` | -2.51 sigma: `2.02233`
  * +3.00 sigma (99.7% CI Extreme): `2.14086` | -3.00 sigma: `2.01179`
- **Oscillators & Volatility**:
  * **RSI (14)**: `66.54` | **RSI State**: **`BULLISH`**
  * **ATR (14)**: `0.01121` | **ATR %**: `0.53%`
  * **Bollinger Bands**: Upper=`2.11069` | Mid=`2.08000` | Lower=`2.04931` | Bandwidth=`2.95%`
  * **MACD**: Line=`+0.0096` | Signal=`+0.0062` | Hist=`+0.0034`
- **Exponential Moving Average Ribbon (EMA)**:
  * Short Horizon: EMA-5=`2.09988` | EMA-9=`2.09443` | EMA-13=`2.08974` | EMA-20=`2.08403`
  * Intermediate: EMA-34=`2.07948` | EMA-50=`2.07926` | EMA-89=`2.08173` | EMA-100=`2.08219`
  * Institutional: EMA-144=`2.08237` | EMA-200=`2.07872` (Slope: `+0.064%`) | EMA-233=`2.07639` (Slope: `+0.066%`)
  * **Trend Bias**: **`STRONG BULLISH`**

---

## 3. Auction Market Structure & Value Profile
*(Sources: 20_Auction_Market_Structure.parquet)*
- **Daily Auction Value Area**:
  * High (VAH): `2.10000` | Point of Control (POC): `2.05000` | Low (VAL): `2.04000`
  * Distance to POC: `+3.44%` | Distance to VAH: `+1.07%` | Distance to VAL: `+3.89%`
  * **Value Area Position**: **`ABOVE_VALUE (Imbalance)`** | **Auction Regime**: **`RANGE_EXPANSION`** | **Session Bias**: **`BULLISH (Above Pivot)`**
- **Prior Day & Weekly Auction Profile**:
  * Prior Day: PD VAH=`2.12000` | PD POC=`2.09000` | PD VAL=`2.08000` | PDH=`2.15000` | PDL=`2.06000` | PDC=`2.13000`
  * Monday Reference: Monday High=`2.10000` | Monday Low=`2.05000` | Monday Mid=`2.08000`
  * Weekly Value Area: Weekly VAH=`2.10000` | Weekly POC=`2.07000` | Weekly VAL=`2.05000`
  * Multi-Week Extremes: Current Week High (CWH)=`2.15000` | CWL=`2.02000` | Prior Week High (PWH)=`2.30000` | PWL=`2.05000`
  * Multi-Month Extremes: Current Month High (CMH)=`2.75000` | CML=`2.02000` | Prior Month High (PMH)=`2.75000` | PML=`1.98000`
- **Session Liquidity Extremes & Initial Balance**:
  * Asian Session: Range `[2.04000 - 2.14000]`
  * London Session: Range `[2.04000 - 2.10000]`
  * New York Session: Range `[2.06000 - 2.12000]`
  * Initial Balance (IB): IB High=`2.08000` | IB Low=`2.06000`
- **Fibonacci Golden Pocket & Optimal Trade Entry (OTE)**:
  * Swing Range: High=`2.15000` | Low=`2.04000` | Direction=`BEARISH_IMPULSE`
  * Golden Pocket [0.618 - 0.65]: `[2.11000 - 2.11000]`
  * Optimal Trade Entry (0.702): `2.12000` | Invalidation Level: `2.13000` | Status: **`DEEP_SHELF_TEST (0.786)`**
- **Classical & Weekly Pivots**:
  * Daily Classical: Pivot=`2.11000` | R1=`2.16000` | S1=`2.07000` | R2=`2.20000` | S2=`2.02000`
  * Weekly Classical: Weekly Pivot=`2.14000` | Weekly R1=`2.24000` | Weekly S1=`1.99000`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Orderflow
*(Sources: 18_CVD.parquet, 18_CVD_30D_5m.parquet, 18_CVD_30D_15m.parquet, 18_CVD_30D_1h.parquet, 18_CVD_30D_4h.parquet, 18_CVD_30D_ALL.parquet, 21_Tradfye_Orderflow.parquet)*
- **Interbank Spot Orderflow Mechanics**: Decentralized OTC market structure. CVD taker deltas do not apply to interbank spot flow. Tape volume governed by broker tick volume with live spread friction of `117.67 bps`.
- **Session Volume Structure**: Price operating at `ABOVE_VALUE (Imbalance)` with Daily POC at `2.05000` (VAH: `2.10000` / VAL: `2.04000`).

---

## 5. Institutional Whale Armor & Resting Orderbook Depth
*(Sources: 10_Whale_Orders.parquet, 12_Hyperdash.parquet, 17_Orderbook.parquet, 4_Hyperliquid_Analysis.parquet)*
- **Interbank Institutional Tier-1 Depth**: Decentralized OTC spot liquidity. Resting whale limit walls from crypto venues do not apply.
- **Verified Broker Armor**: Live Bid `2.11200` / Live Ask `2.13700` with institutional spread of `117.67 bps`. Structural defense anchored at Asian Range `[2.04000 - 2.14000]` and London Range `[2.04000 - 2.10000]`.

---

## 6. Liquidation Max Pain, Heatmaps & Cascade Boundaries
*(Sources: 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 14_Hyperdash_Liq_Map.parquet, 14_Liquidation_Matrix.parquet, 15_Hyperdash_Stops_Map.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`2.09410` (Vol: `6,546 USD`, Dist: `+1.02%`) | Long MP=`2.02440` (Vol: `8,055 USD`, Dist: `-2.34%`)
  * 48H Horizon: Short MP=`2.13540` (Vol: `8,681 USD`, Dist: `+2.96%`) | Long MP=`2.02380` (Vol: `8,055 USD`, Dist: `-2.42%`)
  * 3D Horizon: Short MP=`2.12080` (Vol: `12,807 USD`, Dist: `+2.31%`) | Long MP=`2.01100` (Vol: `8,852 USD`, Dist: `-2.99%`)
  * 7D Horizon: Short MP=`2.32380` (Vol: `18,026 USD`, Dist: `+12.42%`) | Long MP=`2.01180` (Vol: `9,629 USD`, Dist: `-2.67%`)
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
  * Major CEX Rates: Binance=`+0.0100%` | OKX=`+0.0047%` | Bybit=`+0.0100%` | Bitget=`+0.0100%`
  * Mid-Tier CEX Rates: KuCoin=`-0.0206%` | MEXC=`+0.0100%` | Gate=`+0.0011%` | BingX=`+0.0100%` | Bitunix=`+0.0100%`
  * Alternative Venues: WhiteBIT=`+0.0100%` | LBank=`+0.0100%` | tradeXYZ=`-`
  * Inverse Coin-Margined: CoinM Binance=`+0.0000%` | CoinM OKX=`+0.0000%` | CoinM Bybit=`+0.0000%`
- **Exchange Long / Short Ratio Dynamics (3_Exchanges_LS_Ratio*.parquet)**:
  * 15m Tactical: L/S Ratio=`1.00` (Longs: `50.00%`, Shorts: `50.00%`, Total Vol: `0.00 USD`)
  * 1h Primary: L/S Ratio=`1.00` (Longs: `50.00%`, Shorts: `50.00%`, Total Vol: `0.00 USD`)
  * 4h Macro: L/S Ratio=`1.00` (Longs: `50.00%`, Shorts: `50.00%`, Total Vol: `0.00 USD`)
- **Funding Fee Settlement & DEX Arbitrage (6_Funding_Fee_Settlement.parquet, 13_Hyperliquid.parquet)**:
  * Settlement Payouts: Current Expected=`443.87 USD` | Last 24h=`1.25K USD` | Last 3D=`2.69K USD` | Last 7D=`6.53K USD`

---

## 8. Microstructure Footprint, Tape Imbalances & Macro Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 16_Hyperdash_telegram_Intel.parquet, 19_News.parquet, 19_Calendar.parquet)*
- **Bar-by-Bar Microstructure Footprint (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
  * Venue Source: `Aggregated` | Timeframe: `15m` | Last Price: `2.12450`
  * Footprint Auction Profile: Bar VWAP=`2.12450` | Bar POC=`2.12450` | Bar VAH=`2.12875` | Bar VAL=`2.12025`
  * Orderflow Volumes: Total Vol=`0.00 USD` | Taker Buy=`0.00 USD` | Taker Sell=`0.00 USD`
  * Bar Delta Profile: Delta=`+0.00 USD` (`+0.00%`) | Max Delta=`+0.00 USD` | Min Delta=`+0.00 USD` | Cumulative Bar Delta=`+0.00 USD`
  * Order Execution Dynamics: Trades Count=`0` | Avg Trade Size=`0.00 USD`
  * Tape Imbalances: Imbalance Ratio=`0.0%` | Buy Imbalances Count=`0` | Sell Imbalances Count=`0`
  * Footprint Open Interest: Bar OI=`0.00 USD` | Bar OI Change=`+0.00 USD`
- **Multi-Horizon Macro Capital Netflows (2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet)**:
  * Spot Capital Netflows:
    - Tactical: 5m=`+9.34K` | 15m=`+20.32K` | 30m=`+21.43K` | 1h=`+1.55K`
    - Intermediate: 2h=`+21.31K` | 4h=`+20.68K` | 6h=`+25.71K` | 8h=`+19.23K` | 12h=`+43.35K` | 24h=`+35.28K`
    - Macro Horizons: 1-Week=`-387.74K` | 15-Day=`-895.63K` | 30-Day=`-2.40M` | Market Cap=`149.84M`
  * Futures Capital Netflows:
    - Tactical: 5m=`-3.13K` | 15m=`+17.19K` | 30m=`+31.17K` | 1h=`-9.05K`
    - Intermediate: 2h=`+4.36K` | 4h=`+4.27K` | 6h=`+109.10K` | 8h=`+38.06K` | 12h=`+20.96K` | 24h=`-11.17K`
    - Macro Horizons: 1-Week=`-51.65K` | 15-Day=`-1.09M` | 30-Day=`-6.31M` | Market Cap=`149.84M`

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
- **Stand-Aside Reason**: Gate 1 Spread Friction Failure: Spread friction 117.67 bps exceeds cap 25.0 bps. Standing aside in 100% cash preserves statutory floor.