# 🔬 MASTER 43-FEED QUANTITATIVE DOSSIER: PAXG (Paxos Gold)
**MT5 Symbol**: `XAUUSD.pi` | **Category**: `Tokenized Metal` | **Tier**: `Tier 2`
**Execution Posture**: `PASSIVE LIMIT ONLY` | **Timestamp**: 2026-10-29 14:43:14 UTC
**Pipeline Clearance**: `QUALIFIED` | **Data Freshness**: `1.2m`

---

## 1. MT5 Live Broker Telemetry & Spread Friction Gate
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet)*
- **Live Bid Quote**: `4021.45000` | **Live Ask Quote**: `4021.53000` | **Mid Price**: `4021.49000`
- **Spread Points**: `8.0 pts` | **Spread BPS**: `0.20 bps` (Mandatory Cap: `5.0 bps`)
- **Gate Status**: **`PASS`** (Spread friction within mandatory threshold; safe for maker execution)
- **Order Allowed**: `BUY_LIMIT / SELL_LIMIT` | **Pillar 1 Clearance**: `QUALIFIED`
- **Broker Specifications**: Contract Size=`1.00` | Tick Value=`1.00 USD` | Min Lot=`0.01` | Digits=`5`
- **Account Capital Context**: Balance=`4,744.55 USD` | Equity=`4,744.32 USD` | Free Margin=`4,342.62 USD` | Inviolate Hard Floor=`4,775.00 USD` (Cushion: `-30.68 USD`)
- **Pipeline Health**: Feed #00 Status=`PASS` | Overall Pipeline Telemetry=`33/33 FEEDS PASS (SYNCHRONIZED)`

---

## 2. Technical Profile, Multi-Sigma VWAP Dispersion & Volatility
*(Sources: 11_Technical.parquet, 11_Technical_BTC_Ribbon.parquet)*
- **Last Verified Price**: `4023.51000` | **24h Change**: `-0.76%` (24h High: `4082.75000`, 24h Low: `4015.80000`)
- **Weekly Range**: Week High=`4082.75000` | Week Low=`3988.86000` | Daily POC=`4027.39000` | Daily VAH=`4041.65000` | Daily VAL=`4019.90000`
- **Session VWAP**: `4034.46063` | **Rolling 24h VWAP**: `4041.75408` | **Distance to VWAP**: `-0.27%`
- **VWAP Z-Score**: `-0.97 sigma` | **Mean Reversion Bias**: **`FAIR VALUE`**
- **VWAP Dispersion Bands**:
  * +1.00 sigma: `4045.69553` | -1.00 sigma: `4023.22572`
  * +1.28 sigma (80% CI): `4048.84130` | -1.28 sigma: `4020.07995`
  * +2.00 sigma (95% CI): `4056.93044` | -2.00 sigma: `4011.99082`
  * +2.01 sigma: `4057.04278` | -2.01 sigma: `4011.87847`
  * +2.51 sigma (98.8% CI): `4062.66024` | -2.51 sigma: `4006.26101`
  * +3.00 sigma (99.7% CI Extreme): `4068.16534` | -3.00 sigma: `4000.75591`
- **Oscillators & Volatility**:
  * **RSI (14)**: `45.54` | **RSI State**: **`NEUTRAL`**
  * **ATR (14)**: `9.06849` | **ATR %**: `0.23%`
  * **Bollinger Bands**: Upper=`4035.60019` | Mid=`4027.25450` | Lower=`4018.90881` | Bandwidth=`0.41%`
  * **MACD**: Line=`-2.6386` | Signal=`-2.5638` | Hist=`-0.0748`
- **Exponential Moving Average Ribbon (EMA)**:
  * Short Horizon: EMA-5=`4023.74313` | EMA-9=`4024.61613` | EMA-13=`4025.40387` | EMA-20=`4026.69576`
  * Intermediate: EMA-34=`4029.42039` | EMA-50=`4032.23279` | EMA-89=`4036.42043` | EMA-100=`4037.04619`
  * Institutional: EMA-144=`4037.18295` | EMA-200=`4035.12572` (Slope: `-0.029%`) | EMA-233=`4033.69463` (Slope: `-0.021%`)
  * **Trend Bias**: **`STRONG BEARISH`**

---

## 3. Auction Market Structure & Value Profile
*(Sources: 20_Auction_Market_Structure.parquet)*
- **Daily Auction Value Area**:
  * High (VAH): `4041.65000` | Point of Control (POC): `4027.39000` | Low (VAL): `4019.90000`
  * Distance to POC: `-0.15%` | Distance to VAH: `-0.51%` | Distance to VAL: `+0.03%`
  * **Value Area Position**: **`INSIDE_VALUE (Balance)`** | **Auction Regime**: **`ROTATIONAL_BALANCE`** | **Session Bias**: **`BEARISH (Below Pivot)`**
- **Prior Day & Weekly Auction Profile**:
  * Prior Day: PD VAH=`4059.03000` | PD POC=`4041.68000` | PD VAL=`4035.89000` | PDH=`4082.75000` | PDL=`4024.90000` | PDC=`4067.36000`
  * Monday Reference: Monday High=`4030.02000` | Monday Low=`3978.16000` | Monday Mid=`4004.09000`
  * Weekly Value Area: Weekly VAH=`4053.12000` | Weekly POC=`4016.16000` | Weekly VAL=`4005.70000`
  * Multi-Week Extremes: Current Week High (CWH)=`4082.75000` | CWL=`3978.16000` | Prior Week High (PWH)=`4190.47000` | PWL=`3975.67000`
  * Multi-Month Extremes: Current Month High (CMH)=`4225.70000` | CML=`3975.67000` | Prior Month High (PMH)=`4510.85000` | PML=`4110.90000`
- **Session Liquidity Extremes & Initial Balance**:
  * Asian Session: Range `[4035.73000 - 4069.28000]`
  * London Session: Range `[4015.80000 - 4046.38000]`
  * New York Session: Range `[4016.77000 - 4039.31000]`
  * Initial Balance (IB): IB High=`4046.38000` | IB Low=`4022.15000`
- **Fibonacci Golden Pocket & Optimal Trade Entry (OTE)**:
  * Swing Range: High=`4082.75000` | Low=`4015.80000` | Direction=`BEARISH_IMPULSE`
  * Golden Pocket [0.618 - 0.65]: `[4057.18000 - 4059.32000]`
  * Optimal Trade Entry (0.702): `4062.80000` | Invalidation Level: `4068.42000` | Status: **`SHALLOW_RETRACE`**
- **Classical & Weekly Pivots**:
  * Daily Classical: Pivot=`4058.34000` | R1=`4091.77000` | S1=`4033.92000` | R2=`4116.19000` | S2=`4000.49000`
  * Weekly Classical: Weekly Pivot=`4053.98000` | Weekly R1=`4132.30000` | Weekly S1=`3917.50000`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Orderflow
*(Sources: 18_CVD.parquet, 18_CVD_30D_5m.parquet, 18_CVD_30D_15m.parquet, 18_CVD_30D_1h.parquet, 18_CVD_30D_4h.parquet, 18_CVD_30D_ALL.parquet, 21_Tradfye_Orderflow.parquet)*
- **Primary 15m CVD Microstructure (18_CVD_30D_15m.parquet)**:
  * Candle Delta: `+76,385.99 USD` (Base: `+18.9700 coins`) | Delta %: `+11.44%`
  * Taker Volumes: Taker Buy=`372,065.75 USD` | Taker Sell=`295,679.75 USD` | Total Vol=`165.82 USD`
  * Cumulative CVD: `+15,076.22 USD` (Base: `+4.5550`)
  * Rolling CVD Z-Score: `+0.23 sigma` | Price Return: `-0.05%`
  * **Delta Regime**: **`BULLISH ABSORPTION`** | Trades Count: `2,599`
- **Multi-Timeframe Delta Comparison**:
  * 5m Bar: Delta=`+51,434.71 USD` | Delta %=`+23.04%` | Z-Score=`+0.24` | Regime=`BULLISH ABSORPTION`
  * 1h Bar: Delta=`+76,695.97 USD` | Delta %=`+11.49%` | Z-Score=`+0.10` | Regime=`BULLISH ABSORPTION`
  * 4h Bar: Delta=`+899,327.52 USD` | Delta %=`+11.36%` | Z-Score=`+1.48` | Regime=`DELTA ALIGNED`
  * 30D Consolidated (ALL): Cumulative Trend=`+625,061.62 USD` | Long-Term Regime=`DELTA ALIGNED`
- **Institutional Footprint & Deribit Options Armor (21_Tradfye_Orderflow.parquet)**:
  * Candle VWAP: `4021.49000` | Estimated POC: `4021.49000` | Avg Trade Size: `0.00 USD`
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
- **Consolidated L2 Orderbook Depth & Skew (17_Orderbook.parquet)**:
  * `ASK`: `30,006.70 USD` @ `4,022.40 USD` (Coins: 7.4599 GOLD, Cumulative: 1,723,656.59 USD, Tier: 1 orders, Dist: +0.05%, Bias: B/A: 50.2% / 49.8%)
  * `ASK`: `14,397.02 USD` @ `4,022.30 USD` (Coins: 3.5793 GOLD, Cumulative: 1,693,649.89 USD, Tier: 5 orders, Dist: +0.05%, Bias: B/A: 50.2% / 49.8%)
  * `ASK`: `99,904.21 USD` @ `4,022.20 USD` (Coins: 24.8382 GOLD, Cumulative: 1,679,252.87 USD, Tier: 3 orders, Dist: +0.05%, Bias: B/A: 50.2% / 49.8%)
- **Hyperliquid Elite Trader Positioning (4_Hyperliquid_Analysis.parquet)**:
  * Wallet `0x2eddf3aa5c...` (0x2edd...8179): `Long` `1,821,104.19 USD` (452.2460 PAXG, Margin: 182,110.42 USD, Leverage: 10X Cross, Entry: 4,174.40 USD, Current: 4,025.80 USD, Est Liq: 0.00 USD, PnL: -66,754.15 USD [-3.67%], Fees: +48,569.51 USD)
  * Wallet `0x7a6d5fc57f...` (0x7a6d...f79c): `Short` `1,723,283.04 USD` (428.3790 PAXG, Margin: 172,328.30 USD, Leverage: 10X Cross, Entry: 4,136.09 USD, Current: 4,025.80 USD, Est Liq: 5,917.69 USD, PnL: +48,531.96 USD [+2.82%], Fees: -11,005.10 USD)
  * Wallet `0x51f6388553...` (0x51f6...2b39): `Long` `1,524,435.48 USD` (378.6060 PAXG, Margin: 152,443.55 USD, Leverage: 10X Cross, Entry: 4,235.75 USD, Current: 4,025.80 USD, Est Liq: 0.00 USD, PnL: -79,243.75 USD [-5.20%], Fees: +13,094.86 USD)

---

## 6. Liquidation Max Pain, Heatmaps & Cascade Boundaries
*(Sources: 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 14_Hyperdash_Liq_Map.parquet, 14_Liquidation_Matrix.parquet, 15_Hyperdash_Stops_Map.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`4109.95000` (Vol: `250,500 USD`, Dist: `+1.97%`) | Long MP=`3950.54000` (Vol: `316,800 USD`, Dist: `-1.99%`)
  * 48H Horizon: Short MP=`4142.42000` (Vol: `307,400 USD`, Dist: `+2.77%`) | Long MP=`3950.54000` (Vol: `316,800 USD`, Dist: `-1.99%`)
  * 3D Horizon: Short MP=`4115.27000` (Vol: `399,400 USD`, Dist: `+2.10%`) | Long MP=`3952.40000` (Vol: `407,100 USD`, Dist: `-1.94%`)
  * 7D Horizon: Short MP=`4117.50000` (Vol: `1,100,000 USD`, Dist: `+2.15%`) | Long MP=`3953.89000` (Vol: `1,100,000 USD`, Dist: `-1.90%`)
- **Exchange Cumulative Liquidation Cascades (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
  * 1D Cascade: Total=`3.82M USD` | Short Liq Pool=`3.82M USD` | Long Liq Pool=`0 USD` | Venues: Binance=`53.03K USD`, OKX=`0 USD`, Bybit=`5.55K USD`
  * 7D Cascade: Total=`16.50M USD` | Short Liq Pool=`16.50M USD` | Long Liq Pool=`0 USD` | Venues: Binance=`17.72K USD`, OKX=`0 USD`, Bybit=`2.55K USD`
- **Cross-Venue Liquidation Matrix & Heatmaps (14_Liquidation_Matrix.parquet, 7_Liq_Heapmap.parquet)**:
  * Liquidation Matrix Strike: Price=`4453.60000` | Vol=`16,460,000 USD` | Cumulative=`16,460,000 USD` | Venue=`Binance/OKX/Bybit` | Side=`Short Liquidation`
  * Multi-Timeframe Heatmap Density: 1h=`0.00 USD` | 4h=`0.00 USD` | 12h=`0.00 USD` | 24h=`0.00 USD`
- **Hyperdash Real-Time Liquidation & Retail Stop Protection (14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet)**:
  * Hyperdash Liq Cluster: Mark=`0.00 USD` | Cluster Price=`0.00 USD` | Dist=`-` | Cumulative=`0.00 USD` | Short=`0.00 USD` | Long=`0.00 USD` | Size=`-`
- **Live Forced Liquidation Momentum (7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)**:
  * Multi-Timeframe Forced Aggregates (5m): Long Liq=`0.00 USD` | Short Liq=`0.00 USD` | Total=`0.00 USD` | Net Delta=`0.00 USD` | Dominant=`BALANCED`

---

## 7. Derivatives Sentiment, Open Interest & Funding Dynamics
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet, 6_Funding_Fee_Settlement.parquet, 13_Hyperliquid.parquet)*
- **Aggregated Open Interest Breakdown (5_OI.parquet)**:
  * Total Open Interest: `275.70M USD` (`68,477.9 PAXG`) | OI / 24h Volume Ratio: `1.7903`
  * OI Expansion Rate: 1h Change=`-0.04%` | 4h Change=`+0.08%` | 24h Change=`+0.46%`
  * Venue Concentration:
    - Binance: `107.02M USD` | Bybit: `20.12M USD` | OKX: `0.00 USD` | CME Institutional: `0.00 USD`
    - Gate: `27.15M USD` | MEXC: `25.11M USD` | Hyperliquid DEX: `25.76M USD` | Bitget: `9.51M USD`
    - KuCoin: `32.68M USD` | BingX: `0.00 USD` | Bitunix: `1.61M USD` | Others: `26.74M USD`
- **Cross-Exchange Perpetual Funding Rates (5_Funding_Rate.parquet)**:
  * Major CEX Rates: Binance=`+0.0000%` | OKX=`+0.0000%` | Bybit=`+0.0000%` | Bitget=`+0.0000%`
  * Mid-Tier CEX Rates: KuCoin=`+0.0000%` | MEXC=`+0.0000%` | Gate=`+0.0000%` | BingX=`+0.0000%` | Bitunix=`+0.0000%`
  * Alternative Venues: WhiteBIT=`+0.0000%` | LBank=`+0.0000%` | tradeXYZ=`0.0006%`
  * Inverse Coin-Margined: CoinM Binance=`+0.0000%` | CoinM OKX=`+0.0000%` | CoinM Bybit=`+0.0000%`
- **Exchange Long / Short Ratio Dynamics (3_Exchanges_LS_Ratio*.parquet)**:
  * 15m Tactical: L/S Ratio=`0.82` (Longs: `44.96%`, Shorts: `55.04%`, Total Vol: `1.47M USD`)
  * 1h Primary: L/S Ratio=`1.09` (Longs: `52.18%`, Shorts: `47.82%`, Total Vol: `11.25M USD`)
  * 4h Macro: L/S Ratio=`0.95` (Longs: `48.64%`, Shorts: `51.36%`, Total Vol: `41.04M USD`)
- **Funding Fee Settlement & DEX Arbitrage (6_Funding_Fee_Settlement.parquet, 13_Hyperliquid.parquet)**:
  * Settlement Payouts: Current Expected=`4.45K USD` | Last 24h=`26.74K USD` | Last 3D=`98.64K USD` | Last 7D=`223.27K USD`

---

## 8. Microstructure Footprint, Tape Imbalances & Macro Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 16_Hyperdash_telegram_Intel.parquet, 19_News.parquet, 19_Calendar.parquet)*
- **Bar-by-Bar Microstructure Footprint (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
  * Venue Source: `Aggregated` | Timeframe: `15m` | Last Price: `4021.49000`
  * Footprint Auction Profile: Bar VWAP=`4021.49000` | Bar POC=`4021.49000` | Bar VAH=`4029.53298` | Bar VAL=`4013.44702`
  * Orderflow Volumes: Total Vol=`0.00 USD` | Taker Buy=`0.00 USD` | Taker Sell=`0.00 USD`
  * Bar Delta Profile: Delta=`+0.00 USD` (`+0.00%`) | Max Delta=`+0.00 USD` | Min Delta=`+0.00 USD` | Cumulative Bar Delta=`+0.00 USD`
  * Order Execution Dynamics: Trades Count=`0` | Avg Trade Size=`0.00 USD`
  * Tape Imbalances: Imbalance Ratio=`0.0%` | Buy Imbalances Count=`0` | Sell Imbalances Count=`0`
  * Footprint Open Interest: Bar OI=`0.00 USD` | Bar OI Change=`+0.00 USD`
- **CoinGlass Algorithmic Footprint Signals (25_CoinGlass_Footprint_Signals.parquet)**:
  * Signal Classification: Type=`AUCTION_ROTATIONAL_BALANCE` | Bias: **`BULLISH (ABOVE PIVOT)`** | Signal Time=`2026-10-28 21:11:32 IST` | Timeframe=`Auction`
  * Signal Context: Headline=`GOLD (XAUUSD.pi) Metal Auction: ROTATIONAL_BALANCE` | Price Level=`4045.64000` | Absorbed Volume=`0.00 USD`
  * Bar Footprint Context: Current Bar Delta=`+0.00 USD` | Current Bar Volume=`0.00 USD` | Delta in View=`+0.00 USD`
  * Historical Detail: `Daily POC: 4045.830 | VAH: 4058.030 | VAL: 4040.160 | IB: [4030.150 - 4037.780] | Spread: 0.2 bps` | KPI=`AUCTION_ROTATIONAL_BALANCE` | Bias=`BULLISH (ABOVE PIVOT)`
- **Multi-Horizon Macro Capital Netflows (2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet)**:
  * Spot Capital Netflows:
    - Tactical: 5m=`-19.77K` | 15m=`-31.55K` | 30m=`-30.13K` | 1h=`-178.40K`
    - Intermediate: 2h=`-301.02K` | 4h=`-457.93K` | 6h=`-564.00K` | 8h=`-478.34K` | 12h=`-293.87K` | 24h=`-622.47K`
    - Macro Horizons: 1-Week=`-10.89M` | 15-Day=`-15.82M` | 30-Day=`-21.36M` | Market Cap=`1.80B`
  * Futures Capital Netflows:
    - Tactical: 5m=`-33.28K` | 15m=`+67.64K` | 30m=`-45.78K` | 1h=`+319.42K`
    - Intermediate: 2h=`+466.16K` | 4h=`+823.28K` | 6h=`+598.44K` | 8h=`-324.14K` | 12h=`-142.95K` | 24h=`+111.17K`
    - Macro Horizons: 1-Week=`-10.51M` | 15-Day=`-18.08M` | 30-Day=`-74.01M` | Market Cap=`1.80B`

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
- **Stand-Aside Reason**: Absence of statistically validated auction edge and defending resting armor. Standing aside preserves statutory hard floor.