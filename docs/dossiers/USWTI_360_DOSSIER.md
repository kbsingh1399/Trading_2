# 🔬 MASTER 43-FEED QUANTITATIVE DOSSIER: USWTI (WTI Crude Oil)
**MT5 Symbol**: `USWTI.p` | **Category**: `Energy Commodity` | **Tier**: `Tier 2`
**Execution Posture**: `DISQUALIFIED` | **Timestamp**: 2026-10-29 14:43:14 UTC
**Pipeline Clearance**: `BLOCKED` | **Data Freshness**: `1.2m`

---

## 1. MT5 Live Broker Telemetry & Spread Friction Gate
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet)*
- **Live Bid Quote**: `101.72700` | **Live Ask Quote**: `101.77900` | **Mid Price**: `101.75300`
- **Spread Points**: `52.0 pts` | **Spread BPS**: `5.11 bps` (Mandatory Cap: `5.0 bps`)
- **Gate Status**: **`FAIL`** (Spread friction 5.11 bps exceeds cap 5.0 bps)
- **Order Allowed**: `NONE` | **Pillar 1 Clearance**: `BLOCKED`
- **Broker Specifications**: Contract Size=`1.00` | Tick Value=`1.00 USD` | Min Lot=`0.01` | Digits=`5`
- **Account Capital Context**: Balance=`4,744.55 USD` | Equity=`4,744.32 USD` | Free Margin=`4,342.62 USD` | Inviolate Hard Floor=`4,775.00 USD` (Cushion: `-30.68 USD`)
- **Pipeline Health**: Feed #00 Status=`PASS` | Overall Pipeline Telemetry=`33/33 FEEDS PASS (SYNCHRONIZED)`

---

## 2. Technical Profile, Multi-Sigma VWAP Dispersion & Volatility
*(Sources: 11_Technical.parquet, 11_Technical_BTC_Ribbon.parquet)*
- **Last Verified Price**: `101.16700` | **24h Change**: `-1.15%` (24h High: `104.23300`, 24h Low: `100.45600`)
- **Weekly Range**: Week High=`104.23300` | Week Low=`100.17000` | Daily POC=`102.03000` | Daily VAH=`102.69700` | Daily VAL=`101.83000`
- **Session VWAP**: `102.01399` | **Rolling 24h VWAP**: `102.53772` | **Distance to VWAP**: `-0.83%`
- **VWAP Z-Score**: `-1.71 sigma` | **Mean Reversion Bias**: **`OVERSOLD`**
- **VWAP Dispersion Bands**:
  * +1.00 sigma: `102.51047` | -1.00 sigma: `101.51751`
  * +1.28 sigma (80% CI): `102.64948` | -1.28 sigma: `101.37850`
  * +2.00 sigma (95% CI): `103.00695` | -2.00 sigma: `101.02103`
  * +2.01 sigma: `103.01191` | -2.01 sigma: `101.01607`
  * +2.51 sigma (98.8% CI): `103.26015` | -2.51 sigma: `100.76783`
  * +3.00 sigma (99.7% CI Extreme): `103.50343` | -3.00 sigma: `100.52455`
- **Oscillators & Volatility**:
  * **RSI (14)**: `37.95` | **RSI State**: **`BEARISH`**
  * **ATR (14)**: `0.44648` | **ATR %**: `0.44%`
  * **Bollinger Bands**: Upper=`102.97887` | Mid=`101.97515` | Lower=`100.97143` | Bandwidth=`1.97%`
  * **MACD**: Line=`-0.2440` | Signal=`-0.0974` | Hist=`-0.1466`
- **Exponential Moving Average Ribbon (EMA)**:
  * Short Horizon: EMA-5=`101.29194` | EMA-9=`101.55457` | EMA-13=`101.70388` | EMA-20=`101.84479`
  * Intermediate: EMA-34=`101.98987` | EMA-50=`102.09502` | EMA-89=`102.21016` | EMA-100=`102.21905`
  * Institutional: EMA-144=`102.24347` | EMA-200=`102.20820` (Slope: `-0.040%`) | EMA-233=`102.11196` (Slope: `-0.024%`)
  * **Trend Bias**: **`STRONG BEARISH`**

---

## 3. Auction Market Structure & Value Profile
*(Sources: 20_Auction_Market_Structure.parquet)*
- **Daily Auction Value Area**:
  * High (VAH): `102.69700` | Point of Control (POC): `102.03000` | Low (VAL): `101.83000`
  * Distance to POC: `-0.28%` | Distance to VAH: `-0.93%` | Distance to VAL: `-0.09%`
  * **Value Area Position**: **`BELOW_VALUE (Imbalance)`** | **Auction Regime**: **`RANGE_EXPANSION`** | **Session Bias**: **`BEARISH (Below Pivot)`**
- **Prior Day & Weekly Auction Profile**:
  * Prior Day: PD VAH=`103.28400` | PD POC=`102.39700` | PD VAL=`101.63800` | PDH=`104.23300` | PDL=`100.43500` | PDC=`102.64900`
  * Monday Reference: Monday High=`103.88400` | Monday Low=`101.08300` | Monday Mid=`102.48300`
  * Weekly Value Area: Weekly VAH=`103.00100` | Weekly POC=`102.02500` | Weekly VAL=`101.45700`
  * Multi-Week Extremes: Current Week High (CWH)=`104.23300` | CWL=`100.17000` | Prior Week High (PWH)=`104.76600` | PWL=`96.22100`
  * Multi-Month Extremes: Current Month High (CMH)=`104.76600` | CML=`88.37500` | Prior Month High (PMH)=`106.74600` | PML=`86.51500`
- **Session Liquidity Extremes & Initial Balance**:
  * Asian Session: Range `[101.92500 - 102.95500]`
  * London Session: Range `[101.24500 - 102.74900]`
  * New York Session: Range `[100.45600 - 102.74900]`
  * Initial Balance (IB): IB High=`102.04000` | IB Low=`101.67000`
- **Fibonacci Golden Pocket & Optimal Trade Entry (OTE)**:
  * Swing Range: High=`104.23300` | Low=`100.45600` | Direction=`BEARISH_IMPULSE`
  * Golden Pocket [0.618 - 0.65]: `[102.79000 - 102.91100]`
  * Optimal Trade Entry (0.702): `103.10700` | Invalidation Level: `103.42500` | Status: **`SHALLOW_RETRACE`**
- **Classical & Weekly Pivots**:
  * Daily Classical: Pivot=`102.43900` | R1=`104.44300` | S1=`100.64500` | R2=`106.23700` | S2=`98.64100`
  * Weekly Classical: Weekly Pivot=`101.76500` | Weekly R1=`107.31000` | Weekly S1=`98.76500`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Orderflow
*(Sources: 18_CVD.parquet, 18_CVD_30D_5m.parquet, 18_CVD_30D_15m.parquet, 18_CVD_30D_1h.parquet, 18_CVD_30D_4h.parquet, 18_CVD_30D_ALL.parquet, 21_Tradfye_Orderflow.parquet)*
- **Primary 15m CVD Microstructure (18_CVD_30D_15m.parquet)**:
  * Candle Delta: `+68,370.89 USD` (Base: `+670.5000 coins`) | Delta %: `+75.00%`
  * Taker Volumes: Taker Buy=`79,766.03 USD` | Taker Sell=`11,395.15 USD` | Total Vol=`894.00 USD`
  * Cumulative CVD: `+578,630.14 USD` (Base: `+5,596.8436`)
  * Rolling CVD Z-Score: `+0.80 sigma` | Price Return: `+0.12%`
  * **Delta Regime**: **`AGGRESSIVE BUYING`** | Trades Count: `894`
- **Multi-Timeframe Delta Comparison**:
  * 5m Bar: Delta=`+21,394.36 USD` | Delta %=`+74.14%` | Z-Score=`+1.22` | Regime=`AGGRESSIVE BUYING`
  * 1h Bar: Delta=`+382,796.14 USD` | Delta %=`+86.35%` | Z-Score=`+1.52` | Regime=`AGGRESSIVE BUYING`
  * 4h Bar: Delta=`+137,301.80 USD` | Delta %=`+6.58%` | Z-Score=`+0.36` | Regime=`DELTA ALIGNED`
  * 30D Consolidated (ALL): Cumulative Trend=`-758,225.93 USD` | Long-Term Regime=`DELTA ALIGNED`
- **Institutional Footprint & Deribit Options Armor (21_Tradfye_Orderflow.parquet)**:
  * Candle VWAP: `101.75300` | Estimated POC: `101.75300` | Avg Trade Size: `0.00 USD`
  * Net Delta USD: `+0.00 USD` | Net Delta %: `+0.00%` | Orderflow CVD: `+0.00 USD`
  * Orderflow Regime: **`BALANCED`** | Orderflow Divergence: **`NONE`**
  * Deribit Options Walls: Max Pain=`0.00` | Call Wall=`0.00` | Put Wall=`0.00`

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
  * Wallet `0x0cc159b29f...` (0x0cc1...c7cb): `Long` `30,406,608.24 USD` (300,817.2560 xyz:CL, Margin: 10,135,536.08 USD, Leverage: 3X Cross, Entry: 98.8950 USD, Current: 101.0000 USD, Est Liq: 32.5293 USD, PnL: +657,107.20 USD [+2.16%], Fees: -10,250.27 USD)
  * Wallet `0x30afce2f68...` (0x30af...393e): `Long` `17,947,179.01 USD` (177,712.4370 xyz:CL, Margin: 1,799,888.80 USD, Leverage: 10X Isolated, Entry: 100.9800 USD, Current: 101.0000 USD, Est Liq: 93.1917 USD, PnL: +1,777.12 USD [+0.01%], Fees: +39.63 USD)
  * Wallet `0xebe126adab...` (0xebe1...4070): `Long` `16,273,874.24 USD` (160,999.9430 xyz:CL, Margin: 813,693.71 USD, Leverage: 20X Cross, Entry: 101.8710 USD, Current: 101.0000 USD, Est Liq: 31.2155 USD, PnL: -127,453.76 USD [-0.78%], Fees: -679.41 USD)

---

## 6. Liquidation Max Pain, Heatmaps & Cascade Boundaries
*(Sources: 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 14_Hyperdash_Liq_Map.parquet, 14_Liquidation_Matrix.parquet, 15_Hyperdash_Stops_Map.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`103.96000` (Vol: `6,300,000 USD`, Dist: `+3.00%`) | Long MP=`99.15000` (Vol: `4,000,000 USD`, Dist: `-1.77%`)
  * 48H Horizon: Short MP=`0.00000` (Vol: `0 USD`, Dist: `+0.00%`) | Long MP=`99.25000` (Vol: `11,700,000 USD`, Dist: `-1.66%`)
  * 3D Horizon: Short MP=`103.95000` (Vol: `7,900,000 USD`, Dist: `+3.00%`) | Long MP=`99.25000` (Vol: `9,800,000 USD`, Dist: `-1.66%`)
  * 7D Horizon: Short MP=`104.02000` (Vol: `12,400,000 USD`, Dist: `+3.06%`) | Long MP=`99.18000` (Vol: `15,700,000 USD`, Dist: `-1.74%`)
- **Exchange Cumulative Liquidation Cascades (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
  * 1D Cascade: Total=`0.00 USD` | Short Liq Pool=`0.00 USD` | Long Liq Pool=`0.00 USD` | Venues: Binance=`0.00 USD`, OKX=`0.00 USD`, Bybit=`0.00 USD`
  * 7D Cascade: Total=`0.00 USD` | Short Liq Pool=`0.00 USD` | Long Liq Pool=`0.00 USD` | Venues: Binance=`0.00 USD`, OKX=`0.00 USD`, Bybit=`0.00 USD`
- **Cross-Venue Liquidation Matrix & Heatmaps (14_Liquidation_Matrix.parquet, 7_Liq_Heapmap.parquet)**:
  * Liquidation Matrix Strike: Price=`100.05000` | Vol=`25,000,000 USD` | Cumulative=`50,000,000 USD` | Venue=`MT5 / Synthetic` | Side=`Long Liquidation`
  * Multi-Timeframe Heatmap Density: 1h=`0.00 USD` | 4h=`90.36K USD` | 12h=`0.00 USD` | 24h=`0.00 USD`
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
  * Major CEX Rates: Binance=`+0.0000%` | OKX=`+0.0000%` | Bybit=`+0.0000%` | Bitget=`+0.0000%`
  * Mid-Tier CEX Rates: KuCoin=`+0.0000%` | MEXC=`+0.0000%` | Gate=`+0.0000%` | BingX=`+0.0000%` | Bitunix=`+0.0000%`
  * Alternative Venues: WhiteBIT=`+0.0000%` | LBank=`+0.0000%` | tradeXYZ=`-`
  * Inverse Coin-Margined: CoinM Binance=`+0.0000%` | CoinM OKX=`+0.0000%` | CoinM Bybit=`+0.0000%`
- **Exchange Long / Short Ratio Dynamics (3_Exchanges_LS_Ratio*.parquet)**:
  * 15m Tactical: L/S Ratio=`1.00` (Longs: `50.00%`, Shorts: `50.00%`, Total Vol: `0.00 USD`)
  * 1h Primary: L/S Ratio=`1.00` (Longs: `50.00%`, Shorts: `50.00%`, Total Vol: `0.00 USD`)
  * 4h Macro: L/S Ratio=`1.00` (Longs: `50.00%`, Shorts: `50.00%`, Total Vol: `0.00 USD`)
- **Funding Fee Settlement & DEX Arbitrage (6_Funding_Fee_Settlement.parquet, 13_Hyperliquid.parquet)**:
  * Settlement Payouts: Current Expected=`-13.92K USD` | Last 24h=`-159.23K USD` | Last 3D=`-426.22K USD` | Last 7D=`-798.78K USD`

---

## 8. Microstructure Footprint, Tape Imbalances & Macro Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 16_Hyperdash_telegram_Intel.parquet, 19_News.parquet, 19_Calendar.parquet)*
- **Bar-by-Bar Microstructure Footprint (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
  * Venue Source: `MT5-Interbank-CVD` | Timeframe: `15m` | Last Price: `101.75300`
  * Footprint Auction Profile: Bar VWAP=`101.97000` | Bar POC=`101.97000` | Bar VAH=`101.98500` | Bar VAL=`101.80500`
  * Orderflow Volumes: Total Vol=`91,161.18 USD` | Taker Buy=`79,766.03 USD` | Taker Sell=`11,395.15 USD`
  * Bar Delta Profile: Delta=`+68,370.89 USD` (`+75.00%`) | Max Delta=`+68,370.89 USD` | Min Delta=`+0.00 USD` | Cumulative Bar Delta=`+578,630.14 USD`
  * Order Execution Dynamics: Trades Count=`894` | Avg Trade Size=`101.97 USD`
  * Tape Imbalances: Imbalance Ratio=`300.0%` | Buy Imbalances Count=`1` | Sell Imbalances Count=`0`
  * Footprint Open Interest: Bar OI=`0.00 USD` | Bar OI Change=`+0.00 USD`
- **CoinGlass Algorithmic Footprint Signals (25_CoinGlass_Footprint_Signals.parquet)**:
  * Signal Classification: Type=`AGGRESSIVE BUYING` | Bias: **`BULLISH`** | Signal Time=`2026-10-28 17:30:00 IST` | Timeframe=`4h`
  * Signal Context: Headline=`WTI_OIL Macro Delta Flow: AGGRESSIVE BUYING` | Price Level=`102.68100` | Absorbed Volume=`803,986.89 USD`
  * Bar Footprint Context: Current Bar Delta=`+803,986.89 USD` | Current Bar Volume=`1,833,574.62 USD` | Delta in View=`+675,086.77 USD`
  * Historical Detail: `Bar Delta: 803,986.89 USD | Cumulative CVD: 675,086.77 | CVD Z-Score: 0.75 | Vol: 1,833,574.62 USD` | KPI=`AGGRESSIVE BUYING` | Bias=`BULLISH`
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
- **Stand-Aside Reason**: Gate 1 Spread Friction Failure: Spread friction 5.11 bps exceeds cap 5.0 bps. Standing aside in 100% cash preserves statutory floor.