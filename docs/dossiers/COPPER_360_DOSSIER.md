# 🔬 MASTER 43-FEED QUANTITATIVE DOSSIER: COPPER (High Grade Copper)
**MT5 Symbol**: `COPPER.p` | **Category**: `Base Metal` | **Tier**: `Tier 2`
**Execution Posture**: `PASSIVE LIMIT ONLY` | **Timestamp**: 2026-10-29 14:43:14 UTC
**Pipeline Clearance**: `QUALIFIED` | **Data Freshness**: `1.2m`

---

## 1. MT5 Live Broker Telemetry & Spread Friction Gate
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet)*
- **Live Bid Quote**: `14316.42500` | **Live Ask Quote**: `14322.42500` | **Mid Price**: `14319.42500`
- **Spread Points**: `6000.0 pts` | **Spread BPS**: `4.19 bps` (Mandatory Cap: `5.0 bps`)
- **Gate Status**: **`PASS`** (Spread friction within mandatory threshold; safe for maker execution)
- **Order Allowed**: `BUY_LIMIT / SELL_LIMIT` | **Pillar 1 Clearance**: `QUALIFIED`
- **Broker Specifications**: Contract Size=`1.00` | Tick Value=`1.00 USD` | Min Lot=`0.01` | Digits=`5`
- **Account Capital Context**: Balance=`4,744.55 USD` | Equity=`4,744.32 USD` | Free Margin=`4,342.62 USD` | Inviolate Hard Floor=`4,775.00 USD` (Cushion: `-30.68 USD`)
- **Pipeline Health**: Feed #00 Status=`PASS` | Overall Pipeline Telemetry=`33/33 FEEDS PASS (SYNCHRONIZED)`

---

## 2. Technical Profile, Multi-Sigma VWAP Dispersion & Volatility
*(Sources: 11_Technical.parquet, 11_Technical_BTC_Ribbon.parquet)*
- **Last Verified Price**: `14307.37500` | **24h Change**: `-1.12%` (24h High: `14526.85000`, 24h Low: `14290.17500`)
- **Weekly Range**: Week High=`14526.85000` | Week Low=`14244.60000` | Daily POC=`14357.38000` | Daily VAH=`14430.95100` | Daily VAL=`14290.88200`
- **Session VWAP**: `14391.46608` | **Rolling 24h VWAP**: `14430.89678` | **Distance to VWAP**: `-0.58%`
- **VWAP Z-Score**: `-1.47 sigma` | **Mean Reversion Bias**: **`FAIR VALUE`**
- **VWAP Dispersion Bands**:
  * +1.00 sigma: `14448.71385` | -1.00 sigma: `14334.21832`
  * +1.28 sigma (80% CI): `14464.74322` | -1.28 sigma: `14318.18894`
  * +2.00 sigma (95% CI): `14505.96161` | -2.00 sigma: `14276.97055`
  * +2.01 sigma: `14506.53409` | -2.01 sigma: `14276.39807`
  * +2.51 sigma (98.8% CI): `14535.15797` | -2.51 sigma: `14247.77419`
  * +3.00 sigma (99.7% CI Extreme): `14563.20938` | -3.00 sigma: `14219.72279`
- **Oscillators & Volatility**:
  * **RSI (14)**: `30.56` | **RSI State**: **`BEARISH`**
  * **ATR (14)**: `22.39805` | **ATR %**: `0.16%`
  * **Bollinger Bands**: Upper=`14386.47032` | Mid=`14349.42875` | Lower=`14312.38718` | Bandwidth=`0.52%`
  * **MACD**: Line=`-23.8397` | Signal=`-22.0048` | Hist=`-1.8349`
- **Exponential Moving Average Ribbon (EMA)**:
  * Short Horizon: EMA-5=`14322.04452` | EMA-9=`14332.71191` | EMA-13=`14340.50873` | EMA-20=`14352.78964`
  * Intermediate: EMA-34=`14373.95546` | EMA-50=`14391.71018` | EMA-89=`14414.01595` | EMA-100=`14416.69477`
  * Institutional: EMA-144=`14417.97142` | EMA-200=`14405.45037` (Slope: `-0.057%`) | EMA-233=`14397.09500` (Slope: `-0.042%`)
  * **Trend Bias**: **`STRONG BEARISH`**

---

## 3. Auction Market Structure & Value Profile
*(Sources: 20_Auction_Market_Structure.parquet)*
- **Daily Auction Value Area**:
  * High (VAH): `14430.95100` | Point of Control (POC): `14357.38000` | Low (VAL): `14290.88200`
  * Distance to POC: `-0.26%` | Distance to VAH: `-0.77%` | Distance to VAL: `+0.21%`
  * **Value Area Position**: **`INSIDE_VALUE (Balance)`** | **Auction Regime**: **`ROTATIONAL_BALANCE`** | **Session Bias**: **`BEARISH (Below Pivot)`**
- **Prior Day & Weekly Auction Profile**:
  * Prior Day: PD VAH=`14487.86400` | PD POC=`14467.12000` | PD VAL=`14453.52800` | PDH=`14526.85000` | PDL=`14419.55000` | PDC=`14469.40000`
  * Monday Reference: Monday High=`14391.92500` | Monday Low=`14244.60000` | Monday Mid=`14318.26300`
  * Weekly Value Area: Weekly VAH=`14516.50100` | Weekly POC=`14465.69600` | Weekly VAL=`14349.03300`
  * Multi-Week Extremes: Current Week High (CWH)=`14526.85000` | CWL=`14244.60000` | Prior Week High (PWH)=`14470.67500` | PWL=`14038.20000`
  * Multi-Month Extremes: Current Month High (CMH)=`14699.27500` | CML=`14038.20000` | Prior Month High (PMH)=`14866.25000` | PML=`13922.77500`
- **Session Liquidity Extremes & Initial Balance**:
  * Asian Session: Range `[14435.50000 - 14502.40000]`
  * London Session: Range `[14330.47500 - 14491.90000]`
  * New York Session: Range `[14290.17500 - 14378.57500]`
  * Initial Balance (IB): IB High=`14491.90000` | IB Low=`14441.45000`
- **Fibonacci Golden Pocket & Optimal Trade Entry (OTE)**:
  * Swing Range: High=`14526.85000` | Low=`14290.17500` | Direction=`BEARISH_IMPULSE`
  * Golden Pocket [0.618 - 0.65]: `[14436.44000 - 14444.01400]`
  * Optimal Trade Entry (0.702): `14456.32100` | Invalidation Level: `14476.20200` | Status: **`SHALLOW_RETRACE`**
- **Classical & Weekly Pivots**:
  * Daily Classical: Pivot=`14471.93300` | R1=`14524.31700` | S1=`14417.01700` | R2=`14579.23300` | S2=`14364.63300`
  * Weekly Classical: Weekly Pivot=`14260.57500` | Weekly R1=`14482.95000` | Weekly S1=`14050.47500`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Orderflow
*(Sources: 18_CVD.parquet, 18_CVD_30D_5m.parquet, 18_CVD_30D_15m.parquet, 18_CVD_30D_1h.parquet, 18_CVD_30D_4h.parquet, 18_CVD_30D_ALL.parquet, 21_Tradfye_Orderflow.parquet)*
- **Interbank Spot Orderflow Mechanics**: Decentralized OTC market structure. CVD taker deltas do not apply to interbank spot flow. Tape volume governed by broker tick volume with live spread friction of `4.19 bps`.
- **Session Volume Structure**: Price operating at `INSIDE_VALUE (Balance)` with Daily POC at `14357.38000` (VAH: `14430.95100` / VAL: `14290.88200`).

---

## 5. Institutional Whale Armor & Resting Orderbook Depth
*(Sources: 10_Whale_Orders.parquet, 12_Hyperdash.parquet, 17_Orderbook.parquet, 4_Hyperliquid_Analysis.parquet)*
- **Interbank Institutional Tier-1 Depth**: Decentralized OTC spot liquidity. Resting whale limit walls from crypto venues do not apply.
- **Verified Broker Armor**: Live Bid `14316.42500` / Live Ask `14322.42500` with institutional spread of `4.19 bps`. Structural defense anchored at Asian Range `[14435.50000 - 14502.40000]` and London Range `[14330.47500 - 14491.90000]`.

---

## 6. Liquidation Max Pain, Heatmaps & Cascade Boundaries
*(Sources: 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 14_Hyperdash_Liq_Map.parquet, 14_Liquidation_Matrix.parquet, 15_Hyperdash_Stops_Map.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`6.72760` (Vol: `121,188 USD`, Dist: `+1.03%`) | Long MP=`6.59530` (Vol: `121,188 USD`, Dist: `-0.96%`)
  * 48H Horizon: Short MP=`6.70040` (Vol: `126,682 USD`, Dist: `+0.62%`) | Long MP=`6.56780` (Vol: `159,039 USD`, Dist: `-1.37%`)
  * 3D Horizon: Short MP=`6.70040` (Vol: `126,682 USD`, Dist: `+0.62%`) | Long MP=`6.56780` (Vol: `159,039 USD`, Dist: `-1.37%`)
  * 7D Horizon: Short MP=`6.69750` (Vol: `285,412 USD`, Dist: `+0.70%`) | Long MP=`6.37300` (Vol: `401,194 USD`, Dist: `-4.18%`)
- **Exchange Cumulative Liquidation Cascades (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
  * 1D Cascade: Total=`0.00 USD` | Short Liq Pool=`0.00 USD` | Long Liq Pool=`0.00 USD` | Venues: Binance=`0.00 USD`, OKX=`0.00 USD`, Bybit=`0.00 USD`
  * 7D Cascade: Total=`0.00 USD` | Short Liq Pool=`0.00 USD` | Long Liq Pool=`0.00 USD` | Venues: Binance=`0.00 USD`, OKX=`0.00 USD`, Bybit=`0.00 USD`
- **Cross-Venue Liquidation Matrix & Heatmaps (14_Liquidation_Matrix.parquet, 7_Liq_Heapmap.parquet)**:
  * Liquidation Matrix Strike: Price=`0.00000` | Vol=`0 USD` | Cumulative=`0 USD` | Venue=`-` | Side=`-`
  * Multi-Timeframe Heatmap Density: 1h=`49.18K USD` | 4h=`0.00 USD` | 12h=`0.00 USD` | 24h=`0.00 USD`
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
  * Major CEX Rates: Binance=`+0.0000%` | OKX=`+0.0000%` | Bybit=`+0.0000%` | Bitget=`+0.0076%`
  * Mid-Tier CEX Rates: KuCoin=`+0.0068%` | MEXC=`+0.0000%` | Gate=`+0.0000%` | BingX=`+0.0000%` | Bitunix=`+0.0012%`
  * Alternative Venues: WhiteBIT=`+0.0000%` | LBank=`+0.0000%` | tradeXYZ=`0.0006%`
  * Inverse Coin-Margined: CoinM Binance=`+0.0000%` | CoinM OKX=`+0.0000%` | CoinM Bybit=`+0.0000%`
- **Exchange Long / Short Ratio Dynamics (3_Exchanges_LS_Ratio*.parquet)**:
  * 15m Tactical: L/S Ratio=`1.00` (Longs: `50.00%`, Shorts: `50.00%`, Total Vol: `0.00 USD`)
  * 1h Primary: L/S Ratio=`1.00` (Longs: `50.00%`, Shorts: `50.00%`, Total Vol: `0.00 USD`)
  * 4h Macro: L/S Ratio=`1.00` (Longs: `50.00%`, Shorts: `50.00%`, Total Vol: `0.00 USD`)
- **Funding Fee Settlement & DEX Arbitrage (6_Funding_Fee_Settlement.parquet, 13_Hyperliquid.parquet)**:
  * Settlement Payouts: Current Expected=`0.00 USD` | Last 24h=`0.00 USD` | Last 3D=`636.16 USD` | Last 7D=`636.16 USD`

---

## 8. Microstructure Footprint, Tape Imbalances & Macro Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 16_Hyperdash_telegram_Intel.parquet, 19_News.parquet, 19_Calendar.parquet)*
- **Bar-by-Bar Microstructure Footprint (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
  * Venue Source: `Aggregated` | Timeframe: `15m` | Last Price: `14319.42500`
  * Footprint Auction Profile: Bar VWAP=`14319.42500` | Bar POC=`14319.42500` | Bar VAH=`14348.06385` | Bar VAL=`14290.78615`
  * Orderflow Volumes: Total Vol=`0.00 USD` | Taker Buy=`0.00 USD` | Taker Sell=`0.00 USD`
  * Bar Delta Profile: Delta=`+0.00 USD` (`+0.00%`) | Max Delta=`+0.00 USD` | Min Delta=`+0.00 USD` | Cumulative Bar Delta=`+0.00 USD`
  * Order Execution Dynamics: Trades Count=`0` | Avg Trade Size=`0.00 USD`
  * Tape Imbalances: Imbalance Ratio=`0.0%` | Buy Imbalances Count=`0` | Sell Imbalances Count=`0`
  * Footprint Open Interest: Bar OI=`0.00 USD` | Bar OI Change=`+0.00 USD`
- **CoinGlass Algorithmic Footprint Signals (25_CoinGlass_Footprint_Signals.parquet)**:
  * Signal Classification: Type=`AUCTION_ROTATIONAL_BALANCE` | Bias: **`BULLISH (ABOVE PIVOT)`** | Signal Time=`2026-10-28 21:11:33 IST` | Timeframe=`Auction`
  * Signal Context: Headline=`COPPER (COPPER.p) Metal Auction: ROTATIONAL_BALANCE` | Price Level=`14464.55000` | Absorbed Volume=`0.00 USD`
  * Bar Footprint Context: Current Bar Delta=`+0.00 USD` | Current Bar Volume=`0.00 USD` | Delta in View=`+0.00 USD`
  * Historical Detail: `Daily POC: 14469.924 | VAH: 14483.475 | VAL: 14453.427 | IB: [14446.650 - 14474.500] | Spread: 4.2 bps` | KPI=`AUCTION_ROTATIONAL_BALANCE` | Bias=`BULLISH (ABOVE PIVOT)`
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
- **Economic Calendar Clearance**: Zero high-impact calendar blackout restrictions currently active for this currency pair.

---

## 10. Algorithmic Trade Formulation & Sovereign Decision
- **Sovereign Gate Decision**: **`FAIL_CLOSED_STAND_ASIDE`**
- **Dynamic Capacity Verification**: Active Open=`0` | Resting Pending=`2` | Capacity Check: `N_open + N_pending <= 3` (**`PASS`**)
- **Triple Floor Solvency Check**: Current Equity=`4,744.32 USD` | Hard Floor=`4,775.00 USD` | Buffer=`-30.68 USD` | Solvency Check: **`DEFENSE_MODE`**
- **Stand-Aside Reason**: Absence of statistically validated auction edge and defending resting armor. Standing aside preserves statutory hard floor.