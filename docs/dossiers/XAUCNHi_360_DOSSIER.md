# 🔬 MASTER 43-FEED QUANTITATIVE DOSSIER: XAUCNH (XAU/CNH)
**MT5 Symbol**: `XAUCNH.pi` | **Category**: `Forex Exotic` | **Tier**: `Tier 3`
**Execution Posture**: `PASSIVE LIMIT ONLY` | **Timestamp**: 2026-10-29 14:43:14 UTC
**Pipeline Clearance**: `QUALIFIED` | **Data Freshness**: `1.2m`

---

## 1. MT5 Live Broker Telemetry & Spread Friction Gate
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet)*
- **Live Bid Quote**: `26776.65000` | **Live Ask Quote**: `26778.17000` | **Mid Price**: `26777.41000`
- **Spread Points**: `152.0 pts` | **Spread BPS**: `0.57 bps` (Mandatory Cap: `5.0 bps`)
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
  * Candle VWAP: `26777.41000` | Estimated POC: `26777.41000` | Avg Trade Size: `0.00 USD`
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
  * Wallet `0x5b5d51203a...` (0x5b5d...c060): `Short` `25,699,860.51 USD` (6,388.0740 xyz:GOLD, Margin: 6,424,965.13 USD, Leverage: 4X Cross, Entry: 4,191.43 USD, Current: 4,023.00 USD, Est Liq: 26,924.19 USD, PnL: +1,075,360.67 USD [+4.18%], Fees: -646,136.58 USD)
  * Wallet `0x46921f6961...` (0x4692...164f): `Short` `25,298,312.02 USD` (6,287.3256 xyz:GOLD, Margin: 5,059,662.40 USD, Leverage: 5X Cross, Entry: 4,135.96 USD, Current: 4,023.00 USD, Est Liq: 13,226.96 USD, PnL: +705,853.45 USD [+2.79%], Fees: -238,011.27 USD)
  * Wallet `0xb83de012db...` (0xb83d...6e36): `Short` `23,003,731.91 USD` (5,717.0594 xyz:GOLD, Margin: 4,600,746.38 USD, Leverage: 5X Cross, Entry: 4,234.49 USD, Current: 4,023.00 USD, Est Liq: 24,867.61 USD, PnL: +1,205,143.32 USD [+5.24%], Fees: -584,837.77 USD)

---

## 6. Liquidation Max Pain, Heatmaps & Cascade Boundaries
*(Sources: 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 14_Hyperdash_Liq_Map.parquet, 14_Liquidation_Matrix.parquet, 15_Hyperdash_Stops_Map.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`4118.06000` (Vol: `271,900 USD`, Dist: `+2.34%`) | Long MP=`3958.87000` (Vol: `230,100 USD`, Dist: `-1.61%`)
  * 48H Horizon: Short MP=`4118.06000` (Vol: `350,900 USD`, Dist: `+2.34%`) | Long MP=`3958.87000` (Vol: `346,400 USD`, Dist: `-1.61%`)
  * 3D Horizon: Short MP=`4110.46000` (Vol: `300,700 USD`, Dist: `+2.15%`) | Long MP=`3959.21000` (Vol: `388,300 USD`, Dist: `-1.60%`)
  * 7D Horizon: Short MP=`4082.49000` (Vol: `552,000 USD`, Dist: `+1.46%`) | Long MP=`3921.81000` (Vol: `617,500 USD`, Dist: `-2.53%`)
- **Exchange Cumulative Liquidation Cascades (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
  * 1D Cascade: Total=`4.59M USD` | Short Liq Pool=`4.59M USD` | Long Liq Pool=`0 USD` | Venues: Binance=`26.43K USD`, OKX=`0 USD`, Bybit=`40.40K USD`
  * 7D Cascade: Total=`23.21M USD` | Short Liq Pool=`23.21M USD` | Long Liq Pool=`0 USD` | Venues: Binance=`40.60K USD`, OKX=`0 USD`, Bybit=`0 USD`
- **Cross-Venue Liquidation Matrix & Heatmaps (14_Liquidation_Matrix.parquet, 7_Liq_Heapmap.parquet)**:
  * Liquidation Matrix Strike: Price=`0.00000` | Vol=`0 USD` | Cumulative=`0 USD` | Venue=`-` | Side=`-`
  * Multi-Timeframe Heatmap Density: 1h=`60.57K USD` | 4h=`98.47K USD` | 12h=`1.18M USD` | 24h=`3.77M USD`
- **Hyperdash Real-Time Liquidation & Retail Stop Protection (14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet)**:
  * Hyperdash Liq Cluster: Mark=`0.00 USD` | Cluster Price=`0.00 USD` | Dist=`-` | Cumulative=`0.00 USD` | Short=`0.00 USD` | Long=`0.00 USD` | Size=`-`
- **Live Forced Liquidation Momentum (7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)**:
  * Multi-Timeframe Forced Aggregates (5m): Long Liq=`0.00 USD` | Short Liq=`0.00 USD` | Total=`0.00 USD` | Net Delta=`0.00 USD` | Dominant=`BALANCED`

---

## 7. Derivatives Sentiment, Open Interest & Funding Dynamics
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet, 6_Funding_Fee_Settlement.parquet, 13_Hyperliquid.parquet)*
- **Aggregated Open Interest Breakdown (5_OI.parquet)**:
  * Total Open Interest: `875.74M USD` (`217,860.4 XAUT`) | OI / 24h Volume Ratio: `2.1977`
  * OI Expansion Rate: 1h Change=`+0.30%` | 4h Change=`-0.81%` | 24h Change=`+3.91%`
  * Venue Concentration:
    - Binance: `62.67M USD` | Bybit: `144.15M USD` | OKX: `0.00 USD` | CME Institutional: `0.00 USD`
    - Gate: `162.01M USD` | MEXC: `406.78M USD` | Hyperliquid DEX: `0.00 USD` | Bitget: `45.63M USD`
    - KuCoin: `26.84M USD` | BingX: `0.00 USD` | Bitunix: `8.47M USD` | Others: `19.19M USD`
- **Cross-Exchange Perpetual Funding Rates (5_Funding_Rate.parquet)**:
  * Major CEX Rates: Binance=`+0.0000%` | OKX=`+0.0000%` | Bybit=`+0.0000%` | Bitget=`+0.0000%`
  * Mid-Tier CEX Rates: KuCoin=`+0.0000%` | MEXC=`+0.0000%` | Gate=`+0.0000%` | BingX=`+0.0000%` | Bitunix=`+0.0000%`
  * Alternative Venues: WhiteBIT=`+0.0000%` | LBank=`+0.0000%` | tradeXYZ=`0.0006%`
  * Inverse Coin-Margined: CoinM Binance=`+0.0000%` | CoinM OKX=`+0.0000%` | CoinM Bybit=`+0.0000%`
- **Exchange Long / Short Ratio Dynamics (3_Exchanges_LS_Ratio*.parquet)**:
  * 15m Tactical: L/S Ratio=`0.82` (Longs: `44.96%`, Shorts: `55.04%`, Total Vol: `1.47M USD`)
  * 1h Primary: L/S Ratio=`1.23` (Longs: `55.25%`, Shorts: `44.75%`, Total Vol: `105.40M USD`)
  * 4h Macro: L/S Ratio=`0.95` (Longs: `48.64%`, Shorts: `51.36%`, Total Vol: `41.04M USD`)
- **Funding Fee Settlement & DEX Arbitrage (6_Funding_Fee_Settlement.parquet, 13_Hyperliquid.parquet)**:
  * Settlement Payouts: Current Expected=`8.56K USD` | Last 24h=`39.24K USD` | Last 3D=`121.10K USD` | Last 7D=`298.84K USD`

---

## 8. Microstructure Footprint, Tape Imbalances & Macro Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 16_Hyperdash_telegram_Intel.parquet, 19_News.parquet, 19_Calendar.parquet)*
- **Bar-by-Bar Microstructure Footprint (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
  * Venue Source: `CoinGlass-AggregatedFutures(Binance)` | Timeframe: `15m` | Last Price: `26777.41000`
  * Footprint Auction Profile: Bar VWAP=`4031.86713` | Bar POC=`4029.75000` | Bar VAH=`4038.15000` | Bar VAL=`4027.65000`
  * Orderflow Volumes: Total Vol=`43,651,588.57 USD` | Taker Buy=`23,624,687.52 USD` | Taker Sell=`20,026,901.05 USD`
  * Bar Delta Profile: Delta=`+3,597,786.46 USD` (`+8.24%`) | Max Delta=`+3,937,170.73 USD` | Min Delta=`-101,976.41 USD` | Cumulative Bar Delta=`+3,647,818.84 USD`
  * Order Execution Dynamics: Trades Count=`33,257` | Avg Trade Size=`1,312.55 USD`
  * Tape Imbalances: Imbalance Ratio=`300.0%` | Buy Imbalances Count=`4` | Sell Imbalances Count=`1`
  * Footprint Open Interest: Bar OI=`0.00 USD` | Bar OI Change=`+0.00 USD`
- **CoinGlass Algorithmic Footprint Signals (25_CoinGlass_Footprint_Signals.parquet)**:
  * Signal Classification: Type=`AUCTION_ROTATIONAL_BALANCE` | Bias: **`BULLISH (ABOVE PIVOT)`** | Signal Time=`2026-10-28 21:11:32 IST` | Timeframe=`Auction`
  * Signal Context: Headline=`GOLD (XAUUSD.pi) Metal Auction: ROTATIONAL_BALANCE` | Price Level=`4045.64000` | Absorbed Volume=`0.00 USD`
  * Bar Footprint Context: Current Bar Delta=`+0.00 USD` | Current Bar Volume=`0.00 USD` | Delta in View=`+0.00 USD`
  * Historical Detail: `Daily POC: 4045.830 | VAH: 4058.030 | VAL: 4040.160 | IB: [4030.150 - 4037.780] | Spread: 0.2 bps` | KPI=`AUCTION_ROTATIONAL_BALANCE` | Bias=`BULLISH (ABOVE PIVOT)`
- **Multi-Horizon Macro Capital Netflows (2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet)**:
  * Spot Capital Netflows:
    - Tactical: 5m=`-2.86K` | 15m=`-7.50K` | 30m=`-57.51K` | 1h=`-149.16K`
    - Intermediate: 2h=`-652.04K` | 4h=`+1.11M` | 6h=`+1.27M` | 8h=`+2.56M` | 12h=`+2.17M` | 24h=`-705.15K`
    - Macro Horizons: 1-Week=`-95.42M` | 15-Day=`-128.87M` | 30-Day=`-176.99M` | Market Cap=`2.93B`
  * Futures Capital Netflows:
    - Tactical: 5m=`-73.11K` | 15m=`+147.56K` | 30m=`-168.42K` | 1h=`+299.47K`
    - Intermediate: 2h=`-115.25K` | 4h=`-459.20K` | 6h=`-175.10K` | 8h=`-751.08K` | 12h=`-329.78K` | 24h=`+70.63K`
    - Macro Horizons: 1-Week=`-23.57M` | 15-Day=`-37.51M` | 30-Day=`-87.88M` | Market Cap=`2.93B`

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
- **Economic Calendar Clearance**: Zero high-impact calendar blackout restrictions currently active for this currency pair.

---

## 10. Algorithmic Trade Formulation & Sovereign Decision
- **Sovereign Gate Decision**: **`FAIL_CLOSED_STAND_ASIDE`**
- **Dynamic Capacity Verification**: Active Open=`0` | Resting Pending=`2` | Capacity Check: `N_open + N_pending <= 3` (**`PASS`**)
- **Triple Floor Solvency Check**: Current Equity=`4,744.32 USD` | Hard Floor=`4,775.00 USD` | Buffer=`-30.68 USD` | Solvency Check: **`DEFENSE_MODE`**
- **Stand-Aside Reason**: Absence of statistically validated auction edge and defending resting armor. Standing aside preserves statutory hard floor.