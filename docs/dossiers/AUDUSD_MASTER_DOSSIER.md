# 🔬 MASTER 43-FEED QUANTITATIVE DOSSIER: AUDUSD (Australian Dollar / US Dollar)
**MT5 Symbol**: `AUDUSD.pi` | **Category**: `FX Major` | **Tier**: `Tier 3`
**Execution Posture**: `PASSIVE LIMIT ONLY` | **Timestamp**: 2026-10-29 14:43:14 UTC
**Pipeline Clearance**: `QUALIFIED` | **Data Freshness**: `1.2m`

---

## 1. MT5 Live Broker Telemetry & Spread Friction Gate
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet)*
- **Live Bid Quote**: `0.70184` | **Live Ask Quote**: `0.70186` | **Mid Price**: `0.70185`
- **Spread Points**: `2.0 pts` | **Spread BPS**: `0.28 bps` (Mandatory Cap: `5.0 bps`)
- **Gate Status**: **`PASS`** (Spread friction within mandatory threshold; safe for maker execution)
- **Order Allowed**: `BUY_LIMIT / SELL_LIMIT` | **Pillar 1 Clearance**: `QUALIFIED`
- **Broker Specifications**: Contract Size=`1.00` | Tick Value=`1.00 USD` | Min Lot=`0.01` | Digits=`5`
- **Account Capital Context**: Balance=`4,744.55 USD` | Equity=`4,744.32 USD` | Free Margin=`4,342.62 USD` | Inviolate Hard Floor=`4,775.00 USD` (Cushion: `-30.68 USD`)
- **Pipeline Health**: Feed #00 Status=`PASS` | Overall Pipeline Telemetry=`33/33 FEEDS PASS (SYNCHRONIZED)`

---

## 2. Technical Profile, Multi-Sigma VWAP Dispersion & Volatility
*(Sources: 11_Technical.parquet, 11_Technical_BTC_Ribbon.parquet)*
- **Last Verified Price**: `0.70188` | **24h Change**: `-0.28%` (24h High: `0.70680`, 24h Low: `0.70170`)
- **Weekly Range**: Week High=`0.70680` | Week Low=`0.70095` | Daily POC=`0.70436` | Daily VAH=`0.70471` | Daily VAL=`0.70190`
- **Session VWAP**: `0.70402` | **Rolling 24h VWAP**: `0.70427` | **Distance to VWAP**: `-0.30%`
- **VWAP Z-Score**: `-2.10 sigma` | **Mean Reversion Bias**: **`EXTREME OVERSOLD`**
- **VWAP Dispersion Bands**:
  * +1.00 sigma: `0.70503` | -1.00 sigma: `0.70300`
  * +1.28 sigma (80% CI): `0.70531` | -1.28 sigma: `0.70272`
  * +2.00 sigma (95% CI): `0.70605` | -2.00 sigma: `0.70198`
  * +2.01 sigma: `0.70606` | -2.01 sigma: `0.70197`
  * +2.51 sigma (98.8% CI): `0.70656` | -2.51 sigma: `0.70147`
  * +3.00 sigma (99.7% CI Extreme): `0.70706` | -3.00 sigma: `0.70097`
- **Oscillators & Volatility**:
  * **RSI (14)**: `30.48` | **RSI State**: **`BEARISH`**
  * **ATR (14)**: `0.00056` | **ATR %**: `0.08%`
  * **Bollinger Bands**: Upper=`0.70424` | Mid=`0.70305` | Lower=`0.70187` | Bandwidth=`0.34%`
  * **MACD**: Line=`-0.0006` | Signal=`-0.0004` | Hist=`-0.0001`
- **Exponential Moving Average Ribbon (EMA)**:
  * Short Horizon: EMA-5=`0.70219` | EMA-9=`0.70249` | EMA-13=`0.70271` | EMA-20=`0.70301`
  * Intermediate: EMA-34=`0.70344` | EMA-50=`0.70374` | EMA-89=`0.70397` | EMA-100=`0.70398`
  * Institutional: EMA-144=`0.70390` | EMA-200=`0.70370` (Slope: `-0.015%`) | EMA-233=`0.70352` (Slope: `-0.010%`)
  * **Trend Bias**: **`BEARISH`**

---

## 3. Auction Market Structure & Value Profile
*(Sources: 20_Auction_Market_Structure.parquet)*
- **Daily Auction Value Area**:
  * High (VAH): `0.70471` | Point of Control (POC): `0.70436` | Low (VAL): `0.70190`
  * Distance to POC: `-0.35%` | Distance to VAH: `-0.40%` | Distance to VAL: `-0.00%`
  * **Value Area Position**: **`BELOW_VALUE (Imbalance)`** | **Auction Regime**: **`TREND_DOWN_ACCEPTANCE`** | **Session Bias**: **`BEARISH (Below Pivot)`**
- **Prior Day & Weekly Auction Profile**:
  * Prior Day: PD VAH=`0.70428` | PD POC=`0.70333` | PD VAL=`0.70298` | PDH=`0.70647` | PDL=`0.70201` | PDC=`0.70535`
  * Monday Reference: Monday High=`0.70397` | Monday Low=`0.70123` | Monday Mid=`0.70260`
  * Weekly Value Area: Weekly VAH=`0.70421` | Weekly POC=`0.70335` | Weekly VAL=`0.70206`
  * Multi-Week Extremes: Current Week High (CWH)=`0.70680` | CWL=`0.70095` | Prior Week High (PWH)=`0.70383` | PWL=`0.69541`
  * Multi-Month Extremes: Current Month High (CMH)=`0.70680` | CML=`0.68942` | Prior Month High (PMH)=`0.72379` | PML=`0.69425`
- **Session Liquidity Extremes & Initial Balance**:
  * Asian Session: Range `[0.70472 - 0.70680]`
  * London Session: Range `[0.70231 - 0.70560]`
  * New York Session: Range `[0.70145 - 0.70419]`
  * Initial Balance (IB): IB High=`0.70560` | IB Low=`0.70461`
- **Fibonacci Golden Pocket & Optimal Trade Entry (OTE)**:
  * Swing Range: High=`0.70680` | Low=`0.70145` | Direction=`BEARISH_IMPULSE`
  * Golden Pocket [0.618 - 0.65]: `[0.70476 - 0.70493]`
  * Optimal Trade Entry (0.702): `0.70521` | Invalidation Level: `0.70566` | Status: **`SHALLOW_RETRACE`**
- **Classical & Weekly Pivots**:
  * Daily Classical: Pivot=`0.70461` | R1=`0.70721` | S1=`0.70275` | R2=`0.70907` | S2=`0.70015`
  * Weekly Classical: Weekly Pivot=`0.70091` | Weekly R1=`0.70640` | Weekly S1=`0.69798`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Orderflow
*(Sources: 18_CVD.parquet, 18_CVD_30D_5m.parquet, 18_CVD_30D_15m.parquet, 18_CVD_30D_1h.parquet, 18_CVD_30D_4h.parquet, 18_CVD_30D_ALL.parquet, 21_Tradfye_Orderflow.parquet)*
- **Primary 15m CVD Microstructure (18_CVD_30D_15m.parquet)**:
  * Candle Delta: `+147.35 USD` (Base: `+209.3220 coins`) | Delta %: `+42.37%`
  * Taker Volumes: Taker Buy=`247.55 USD` | Taker Sell=`100.20 USD` | Total Vol=`494.00 USD`
  * Cumulative CVD: `-3,525.84 USD` (Base: `-5,029.7520`)
  * Rolling CVD Z-Score: `+0.37 sigma` | Price Return: `+0.05%`
  * **Delta Regime**: **`AGGRESSIVE BUYING`** | Trades Count: `494`
- **Multi-Timeframe Delta Comparison**:
  * 5m Bar: Delta=`-81.31 USD` | Delta %=`-66.00%` | Z-Score=`-0.96` | Regime=`AGGRESSIVE SELLING`
  * 1h Bar: Delta=`-1,281.87 USD` | Delta %=`-72.32%` | Z-Score=`-0.49` | Regime=`AGGRESSIVE SELLING`
  * 4h Bar: Delta=`-13,295.01 USD` | Delta %=`-83.51%` | Z-Score=`-1.37` | Regime=`AGGRESSIVE SELLING`
  * 30D Consolidated (ALL): Cumulative Trend=`-8,894.12 USD` | Long-Term Regime=`AGGRESSIVE SELLING`
- **Institutional Footprint & Deribit Options Armor (21_Tradfye_Orderflow.parquet)**:
  * Candle VWAP: `0.70185` | Estimated POC: `0.70185` | Avg Trade Size: `0.00 USD`
  * Net Delta USD: `+0.00 USD` | Net Delta %: `+0.00%` | Orderflow CVD: `+0.00 USD`
  * Orderflow Regime: **`BALANCED`** | Orderflow Divergence: **`NONE`**
  * Deribit Options Walls: Max Pain=`0.00` | Call Wall=`0.00` | Put Wall=`0.00`

---

## 5. Institutional Whale Armor & Resting Orderbook Depth
*(Sources: 10_Whale_Orders.parquet, 12_Hyperdash.parquet, 17_Orderbook.parquet, 4_Hyperliquid_Analysis.parquet)*
- **Interbank Institutional Tier-1 Depth**: Decentralized OTC spot liquidity. Resting whale limit walls from crypto venues do not apply.
- **Verified Broker Armor**: Live Bid `0.70184` / Live Ask `0.70186` with institutional spread of `0.28 bps`. Structural defense anchored at Asian Range `[0.70472 - 0.70680]` and London Range `[0.70231 - 0.70560]`.

---

## 6. Liquidation Max Pain, Heatmaps & Cascade Boundaries
*(Sources: 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 14_Hyperdash_Liq_Map.parquet, 14_Liquidation_Matrix.parquet, 15_Hyperdash_Stops_Map.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **TradFi Structural Liquidity Boundaries**: Centralized perp liquidation feeds do not apply to interbank OTC spot.
- **Stop-Run Cascades & Liquidity Pools**: Primary institutional stop pools reside beyond Classical Pivot extremes (S1: `0.70275` / S2: `0.70015` for long stops; R1: `0.70721` / R2: `0.70907` for short stops) and Asian session extremes `[0.70472 - 0.70680]`.

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
  * Mid-Tier CEX Rates: KuCoin=`+0.0000%` | MEXC=`+0.0128%` | Gate=`+0.0000%` | BingX=`+0.0000%` | Bitunix=`+0.0000%`
  * Alternative Venues: WhiteBIT=`+0.0000%` | LBank=`+0.0128%` | tradeXYZ=`-`
  * Inverse Coin-Margined: CoinM Binance=`+0.0000%` | CoinM OKX=`+0.0000%` | CoinM Bybit=`+0.0000%`
- **Exchange Long / Short Ratio Dynamics (3_Exchanges_LS_Ratio*.parquet)**:
  * 15m Tactical: L/S Ratio=`1.00` (Longs: `50.00%`, Shorts: `50.00%`, Total Vol: `0.00 USD`)
  * 1h Primary: L/S Ratio=`1.00` (Longs: `50.00%`, Shorts: `50.00%`, Total Vol: `0.00 USD`)
  * 4h Macro: L/S Ratio=`1.00` (Longs: `50.00%`, Shorts: `50.00%`, Total Vol: `0.00 USD`)
- **Funding Fee Settlement & DEX Arbitrage (6_Funding_Fee_Settlement.parquet, 13_Hyperliquid.parquet)**:
  * Settlement Payouts: Current Expected=`0.00 USD` | Last 24h=`0.00 USD` | Last 3D=`0.00 USD` | Last 7D=`0.00 USD`

---

## 8. Microstructure Footprint, Tape Imbalances & Macro Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 16_Hyperdash_telegram_Intel.parquet, 19_News.parquet, 19_Calendar.parquet)*
- **Bar-by-Bar Microstructure Footprint (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
  * Venue Source: `MT5-Interbank-CVD` | Timeframe: `15m` | Last Price: `0.70185`
  * Footprint Auction Profile: Bar VWAP=`0.70395` | Bar POC=`0.70395` | Bar VAH=`0.70417` | Bar VAL=`0.70358`
  * Orderflow Volumes: Total Vol=`347.75 USD` | Taker Buy=`247.55 USD` | Taker Sell=`100.20 USD`
  * Bar Delta Profile: Delta=`+147.35 USD` (`+42.37%`) | Max Delta=`+147.35 USD` | Min Delta=`+0.00 USD` | Cumulative Bar Delta=`-3,525.84 USD`
  * Order Execution Dynamics: Trades Count=`494` | Avg Trade Size=`0.70 USD`
  * Tape Imbalances: Imbalance Ratio=`300.0%` | Buy Imbalances Count=`1` | Sell Imbalances Count=`0`
  * Footprint Open Interest: Bar OI=`0.00 USD` | Bar OI Change=`+0.00 USD`
- **CoinGlass Algorithmic Footprint Signals (25_CoinGlass_Footprint_Signals.parquet)**:
  * Signal Classification: Type=`BULLISH ABSORPTION` | Bias: **`BULLISH`** | Signal Time=`2026-10-28 17:30:00 IST` | Timeframe=`4h`
  * Signal Context: Headline=`AUDUSD Macro Delta Flow: BULLISH ABSORPTION` | Price Level=`0.70326` | Absorbed Volume=`1,134.94 USD`
  * Bar Footprint Context: Current Bar Delta=`+1,134.94 USD` | Current Bar Volume=`8,884.99 USD` | Delta in View=`-11,828.70 USD`
  * Historical Detail: `Bar Delta: 1,134.94 USD | Cumulative CVD: -11,828.70 | CVD Z-Score: 0.88 | Vol: 8,884.99 USD` | KPI=`BULLISH ABSORPTION` | Bias=`BULLISH`
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
  * Prevailing Policy Stance: `Reserve Bank of Australia Cash Rate (4.35%) Restrictive Anchor vs Fed Funds`
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
  * `Mon Oct 26 2:40am` [AUD - Low Impact]: RBA Assist Gov Jones Speaks (Forecast: , Previous: )
  * `Tue Oct 27 5:45pm` [USD - Low Impact]: ADP Weekly Employment Change (Forecast: , Previous: 17.5K)
  * `Tue Oct 27 6:00pm` [USD - Low Impact]: Core Durable Goods Orders m/m (Forecast: 0.6%, Previous: 0.2%)
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