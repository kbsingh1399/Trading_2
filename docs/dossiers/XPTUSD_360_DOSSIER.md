# 🔬 MASTER 43-FEED QUANTITATIVE DOSSIER: XPTUSD (XPT/USD)
**MT5 Symbol**: `XPTUSD.pi` | **Category**: `Forex Cross` | **Tier**: `Tier 2`
**Execution Posture**: `DISQUALIFIED` | **Timestamp**: 2026-10-29 14:43:14 UTC
**Pipeline Clearance**: `BLOCKED` | **Data Freshness**: `1.2m`

---

## 1. MT5 Live Broker Telemetry & Spread Friction Gate
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet)*
- **Live Bid Quote**: `1477.36000` | **Live Ask Quote**: `1478.86000` | **Mid Price**: `1478.11000`
- **Spread Points**: `150.0 pts` | **Spread BPS**: `10.15 bps` (Mandatory Cap: `5.0 bps`)
- **Gate Status**: **`FAIL`** (Spread friction 10.15 bps exceeds cap 5.0 bps)
- **Order Allowed**: `NONE` | **Pillar 1 Clearance**: `BLOCKED`
- **Broker Specifications**: Contract Size=`1.00` | Tick Value=`1.00 USD` | Min Lot=`0.01` | Digits=`5`
- **Account Capital Context**: Balance=`4,744.55 USD` | Equity=`4,744.32 USD` | Free Margin=`4,342.62 USD` | Inviolate Hard Floor=`4,775.00 USD` (Cushion: `-30.68 USD`)
- **Pipeline Health**: Feed #00 Status=`PASS` | Overall Pipeline Telemetry=`33/33 FEEDS PASS (SYNCHRONIZED)`

---

## 2. Technical Profile, Multi-Sigma VWAP Dispersion & Volatility
*(Sources: 11_Technical.parquet, 11_Technical_BTC_Ribbon.parquet)*
- **Last Verified Price**: `1481.55000` | **24h Change**: `-4.51%` (24h High: `1556.70000`, 24h Low: `1478.09000`)
- **Weekly Range**: Week High=`1556.70000` | Week Low=`1478.09000` | Daily POC=`1482.15000` | Daily VAH=`1527.59000` | Daily VAL=`1475.72000`
- **Session VWAP**: `1510.82400` | **Rolling 24h VWAP**: `1523.59825` | **Distance to VWAP**: `-1.94%`
- **VWAP Z-Score**: `-1.50 sigma` | **Mean Reversion Bias**: **`FAIR VALUE`**
- **VWAP Dispersion Bands**:
  * +1.00 sigma: `1530.34176` | -1.00 sigma: `1491.30623`
  * +1.28 sigma (80% CI): `1535.80674` | -1.28 sigma: `1485.84125`
  * +2.00 sigma (95% CI): `1549.85953` | -2.00 sigma: `1471.78846`
  * +2.01 sigma: `1550.05471` | -2.01 sigma: `1471.59328`
  * +2.51 sigma (98.8% CI): `1559.81359` | -2.51 sigma: `1461.83440`
  * +3.00 sigma (99.7% CI Extreme): `1569.37730` | -3.00 sigma: `1452.27069`
- **Oscillators & Volatility**:
  * **RSI (14)**: `34.70` | **RSI State**: **`BEARISH`**
  * **ATR (14)**: `6.61097` | **ATR %**: `0.45%`
  * **Bollinger Bands**: Upper=`1507.04832` | Mid=`1491.53350` | Lower=`1476.01868` | Bandwidth=`2.08%`
  * **MACD**: Line=`-7.5099` | Signal=`-7.3879` | Hist=`-0.1220`
- **Exponential Moving Average Ribbon (EMA)**:
  * Short Horizon: EMA-5=`1483.02180` | EMA-9=`1485.04661` | EMA-13=`1487.27026` | EMA-20=`1491.11119`
  * Intermediate: EMA-34=`1498.01639` | EMA-50=`1504.30401` | EMA-89=`1513.85611` | EMA-100=`1515.60849`
  * Institutional: EMA-144=`1519.96634` | EMA-200=`1522.07505` (Slope: `-0.298%`) | EMA-233=`1522.40388` (Slope: `-0.256%`)
  * **Trend Bias**: **`STRONG BEARISH`**

---

## 3. Auction Market Structure & Value Profile
*(Sources: 20_Auction_Market_Structure.parquet)*
- **Daily Auction Value Area**:
  * High (VAH): `1527.59000` | Point of Control (POC): `1482.15000` | Low (VAL): `1475.72000`
  * Distance to POC: `-0.26%` | Distance to VAH: `-3.23%` | Distance to VAL: `+0.17%`
  * **Value Area Position**: **`INSIDE_VALUE (Balance)`** | **Auction Regime**: **`ROTATIONAL_BALANCE`** | **Session Bias**: **`BEARISH (Below Pivot)`**
- **Prior Day & Weekly Auction Profile**:
  * Prior Day: PD VAH=`1544.14000` | PD POC=`1538.53000` | PD VAL=`1530.44000` | PDH=`1556.70000` | PDL=`1525.56000` | PDC=`1534.85000`
  * Monday Reference: Monday High=`1564.57000` | Monday Low=`1515.93000` | Monday Mid=`1540.25000`
  * Weekly Value Area: Weekly VAH=`1552.40000` | Weekly POC=`1538.14000` | Weekly VAL=`1521.51000`
  * Multi-Week Extremes: Current Week High (CWH)=`1564.57000` | CWL=`1475.49000` | Prior Week High (PWH)=`1662.06000` | PWL=`1541.87000`
  * Multi-Month Extremes: Current Month High (CMH)=`1746.05000` | CML=`1475.49000` | Prior Month High (PMH)=`1928.64000` | PML=`1678.54000`
- **Session Liquidity Extremes & Initial Balance**:
  * Asian Session: Range `[1517.70000 - 1544.35000]`
  * London Session: Range `[1479.56000 - 1528.24000]`
  * New York Session: Range `[1475.49000 - 1502.48000]`
  * Initial Balance (IB): IB High=`1528.24000` | IB Low=`1512.68000`
- **Fibonacci Golden Pocket & Optimal Trade Entry (OTE)**:
  * Swing Range: High=`1556.70000` | Low=`1475.49000` | Direction=`BEARISH_IMPULSE`
  * Golden Pocket [0.618 - 0.65]: `[1525.68000 - 1528.28000]`
  * Optimal Trade Entry (0.702): `1532.50000` | Invalidation Level: `1539.32000` | Status: **`SHALLOW_RETRACE`**
- **Classical & Weekly Pivots**:
  * Daily Classical: Pivot=`1539.04000` | R1=`1552.51000` | S1=`1521.37000` | R2=`1570.18000` | S2=`1507.90000`
  * Weekly Classical: Weekly Pivot=`1582.44000` | Weekly R1=`1623.01000` | Weekly S1=`1502.82000`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Orderflow
*(Sources: 18_CVD.parquet, 18_CVD_30D_5m.parquet, 18_CVD_30D_15m.parquet, 18_CVD_30D_1h.parquet, 18_CVD_30D_4h.parquet, 18_CVD_30D_ALL.parquet, 21_Tradfye_Orderflow.parquet)*
- **Interbank Spot Orderflow Mechanics**: Decentralized OTC market structure. CVD taker deltas do not apply to interbank spot flow. Tape volume governed by broker tick volume with live spread friction of `10.15 bps`.
- **Session Volume Structure**: Price operating at `INSIDE_VALUE (Balance)` with Daily POC at `1482.15000` (VAH: `1527.59000` / VAL: `1475.72000`).

---

## 5. Institutional Whale Armor & Resting Orderbook Depth
*(Sources: 10_Whale_Orders.parquet, 12_Hyperdash.parquet, 17_Orderbook.parquet, 4_Hyperliquid_Analysis.parquet)*
- **Interbank Institutional Tier-1 Depth**: Decentralized OTC spot liquidity. Resting whale limit walls from crypto venues do not apply.
- **Verified Broker Armor**: Live Bid `1477.36000` / Live Ask `1478.86000` with institutional spread of `10.15 bps`. Structural defense anchored at Asian Range `[1517.70000 - 1544.35000]` and London Range `[1479.56000 - 1528.24000]`.

---

## 6. Liquidation Max Pain, Heatmaps & Cascade Boundaries
*(Sources: 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 14_Hyperdash_Liq_Map.parquet, 14_Liquidation_Matrix.parquet, 15_Hyperdash_Stops_Map.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`1557.48500` (Vol: `80,586 USD`, Dist: `+0.95%`) | Long MP=`1489.89000` (Vol: `174,235 USD`, Dist: `-3.43%`)
  * 48H Horizon: Short MP=`1555.80200` (Vol: `144,629 USD`, Dist: `+0.84%`) | Long MP=`1496.71700` (Vol: `139,286 USD`, Dist: `-2.99%`)
  * 3D Horizon: Short MP=`1555.80200` (Vol: `144,629 USD`, Dist: `+0.84%`) | Long MP=`1496.71700` (Vol: `139,286 USD`, Dist: `-2.99%`)
  * 7D Horizon: Short MP=`1610.38800` (Vol: `202,579 USD`, Dist: `+4.67%`) | Long MP=`1496.60400` (Vol: `159,771 USD`, Dist: `-2.73%`)
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
  * Major CEX Rates: Binance=`+0.0262%` | OKX=`+0.0659%` | Bybit=`+0.0000%` | Bitget=`+0.0398%`
  * Mid-Tier CEX Rates: KuCoin=`+0.0209%` | MEXC=`+0.0258%` | Gate=`+0.0189%` | BingX=`+0.0000%` | Bitunix=`+0.0246%`
  * Alternative Venues: WhiteBIT=`+0.0000%` | LBank=`+0.0000%` | tradeXYZ=`-`
  * Inverse Coin-Margined: CoinM Binance=`+0.0000%` | CoinM OKX=`+0.0000%` | CoinM Bybit=`+0.0000%`
- **Exchange Long / Short Ratio Dynamics (3_Exchanges_LS_Ratio*.parquet)**:
  * 15m Tactical: L/S Ratio=`1.00` (Longs: `50.00%`, Shorts: `50.00%`, Total Vol: `0.00 USD`)
  * 1h Primary: L/S Ratio=`1.00` (Longs: `50.00%`, Shorts: `50.00%`, Total Vol: `0.00 USD`)
  * 4h Macro: L/S Ratio=`1.00` (Longs: `50.00%`, Shorts: `50.00%`, Total Vol: `0.00 USD`)
- **Funding Fee Settlement & DEX Arbitrage (6_Funding_Fee_Settlement.parquet, 13_Hyperliquid.parquet)**:
  * Settlement Payouts: Current Expected=`2.06K USD` | Last 24h=`1.54K USD` | Last 3D=`12.15K USD` | Last 7D=`22.84K USD`

---

## 8. Microstructure Footprint, Tape Imbalances & Macro Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 16_Hyperdash_telegram_Intel.parquet, 19_News.parquet, 19_Calendar.parquet)*
- **Bar-by-Bar Microstructure Footprint (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
  * Venue Source: `Aggregated` | Timeframe: `15m` | Last Price: `1478.11000`
  * Footprint Auction Profile: Bar VWAP=`1478.11000` | Bar POC=`1478.11000` | Bar VAH=`1481.06622` | Bar VAL=`1475.15378`
  * Orderflow Volumes: Total Vol=`0.00 USD` | Taker Buy=`0.00 USD` | Taker Sell=`0.00 USD`
  * Bar Delta Profile: Delta=`+0.00 USD` (`+0.00%`) | Max Delta=`+0.00 USD` | Min Delta=`+0.00 USD` | Cumulative Bar Delta=`+0.00 USD`
  * Order Execution Dynamics: Trades Count=`0` | Avg Trade Size=`0.00 USD`
  * Tape Imbalances: Imbalance Ratio=`0.0%` | Buy Imbalances Count=`0` | Sell Imbalances Count=`0`
  * Footprint Open Interest: Bar OI=`0.00 USD` | Bar OI Change=`+0.00 USD`
- **CoinGlass Algorithmic Footprint Signals (25_CoinGlass_Footprint_Signals.parquet)**:
  * Signal Classification: Type=`AUCTION_ROTATIONAL_BALANCE` | Bias: **`BULLISH (ABOVE PIVOT)`** | Signal Time=`2026-10-28 21:11:33 IST` | Timeframe=`Auction`
  * Signal Context: Headline=`PLATINUM (XPTUSD.pi) Metal Auction: ROTATIONAL_BALANCE` | Price Level=`1543.28000` | Absorbed Volume=`0.00 USD`
  * Bar Footprint Context: Current Bar Delta=`+0.00 USD` | Current Bar Volume=`0.00 USD` | Delta in View=`+0.00 USD`
  * Historical Detail: `Daily POC: 1534.110 | VAH: 1544.220 | VAL: 1530.610 | IB: [1529.240 - 1534.390] | Spread: 35.8 bps` | KPI=`AUCTION_ROTATIONAL_BALANCE` | Bias=`BULLISH (ABOVE PIVOT)`
- **Multi-Horizon Macro Capital Netflows (2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet)**:
  * Spot Capital Netflows:
    - Tactical: 5m=`-` | 15m=`-` | 30m=`-` | 1h=`-`
    - Intermediate: 2h=`-` | 4h=`-` | 6h=`-` | 8h=`-` | 12h=`-` | 24h=`-`
    - Macro Horizons: 1-Week=`-` | 15-Day=`-` | 30-Day=`-` | Market Cap=`-`
  * Futures Capital Netflows:
    - Tactical: 5m=`-` | 15m=`-` | 30m=`-` | 1h=`-`
    - Intermediate: 2h=`-` | 4h=`-` | 6h=`-` | 8h=`-` | 12h=`-` | 24h=`-`
    - Macro Horizons: 1-Week=`-` | 15-Day=`-` | 30-Day=`-` | Market Cap=`-`

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
  * Mandatory spread gate threshold: `5.0 bps`.
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
- **Stand-Aside Reason**: Gate 1 Spread Friction Failure: Spread friction 10.15 bps exceeds cap 5.0 bps. Standing aside in 100% cash preserves statutory floor.