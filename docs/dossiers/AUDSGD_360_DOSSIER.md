# 🔬 MASTER 43-FEED QUANTITATIVE DOSSIER: AUDSGD (AUD/SGD)
**MT5 Symbol**: `AUDSGD.pi` | **Category**: `Forex Exotic` | **Tier**: `Tier 3`
**Execution Posture**: `PASSIVE LIMIT ONLY` | **Timestamp**: 2026-10-29 14:43:14 UTC
**Pipeline Clearance**: `QUALIFIED` | **Data Freshness**: `1.2m`

---

## 1. MT5 Live Broker Telemetry & Spread Friction Gate
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet)*
- **Live Bid Quote**: `0.89929` | **Live Ask Quote**: `0.89934` | **Mid Price**: `0.89932`
- **Spread Points**: `5.0 pts` | **Spread BPS**: `0.56 bps` (Mandatory Cap: `5.0 bps`)
- **Gate Status**: **`PASS`** (Spread friction within mandatory threshold; safe for maker execution)
- **Order Allowed**: `BUY_LIMIT / SELL_LIMIT` | **Pillar 1 Clearance**: `QUALIFIED`
- **Broker Specifications**: Contract Size=`1.00` | Tick Value=`1.00 USD` | Min Lot=`0.01` | Digits=`5`
- **Account Capital Context**: Balance=`4,744.55 USD` | Equity=`4,744.32 USD` | Free Margin=`4,342.62 USD` | Inviolate Hard Floor=`4,775.00 USD` (Cushion: `-30.68 USD`)
- **Pipeline Health**: Feed #00 Status=`PASS` | Overall Pipeline Telemetry=`33/33 FEEDS PASS (SYNCHRONIZED)`

---

## 2. Technical Profile, Multi-Sigma VWAP Dispersion & Volatility
*(Sources: 11_Technical.parquet, 11_Technical_BTC_Ribbon.parquet)*
- **Last Verified Price**: `0.89923` | **24h Change**: `-0.40%` (24h High: `0.90500`, 24h Low: `0.89908`)
- **Weekly Range**: Week High=`0.90500` | Week Low=`0.89729` | Daily POC=`0.90106` | Daily VAH=`0.90290` | Daily VAL=`0.89911`
- **Session VWAP**: `0.90186` | **Rolling 24h VWAP**: `0.90243` | **Distance to VWAP**: `-0.29%`
- **VWAP Z-Score**: `-1.92 sigma` | **Mean Reversion Bias**: **`OVERSOLD`**
- **VWAP Dispersion Bands**:
  * +1.00 sigma: `0.90323` | -1.00 sigma: `0.90049`
  * +1.28 sigma (80% CI): `0.90362` | -1.28 sigma: `0.90010`
  * +2.00 sigma (95% CI): `0.90461` | -2.00 sigma: `0.89911`
  * +2.01 sigma: `0.90462` | -2.01 sigma: `0.89910`
  * +2.51 sigma (98.8% CI): `0.90531` | -2.51 sigma: `0.89841`
  * +3.00 sigma (99.7% CI Extreme): `0.90598` | -3.00 sigma: `0.89774`
- **Oscillators & Volatility**:
  * **RSI (14)**: `25.51` | **RSI State**: **`OVERSOLD`**
  * **ATR (14)**: `0.00054` | **ATR %**: `0.06%`
  * **Bollinger Bands**: Upper=`0.90216` | Mid=`0.90084` | Lower=`0.89953` | Bandwidth=`0.29%`
  * **MACD**: Line=`-0.0006` | Signal=`-0.0005` | Hist=`-0.0001`
- **Exponential Moving Average Ribbon (EMA)**:
  * Short Horizon: EMA-5=`0.89982` | EMA-9=`0.90021` | EMA-13=`0.90046` | EMA-20=`0.90078`
  * Intermediate: EMA-34=`0.90125` | EMA-50=`0.90160` | EMA-89=`0.90194` | EMA-100=`0.90195`
  * Institutional: EMA-144=`0.90187` | EMA-200=`0.90157` (Slope: `-0.013%`) | EMA-233=`0.90131` (Slope: `-0.008%`)
  * **Trend Bias**: **`BEARISH`**

---

## 3. Auction Market Structure & Value Profile
*(Sources: 20_Auction_Market_Structure.parquet)*
- **Daily Auction Value Area**:
  * High (VAH): `0.90290` | Point of Control (POC): `0.90106` | Low (VAL): `0.89911`
  * Distance to POC: `+0.00%` | Distance to VAH: `+0.00%` | Distance to VAL: `+0.00%`
  * **Value Area Position**: **`INSIDE_VALUE (Balance)`** | **Auction Regime**: **`BALANCED_AUCTION`** | **Session Bias**: **`NEUTRAL`**
- **Prior Day & Weekly Auction Profile**:
  * Prior Day: PD VAH=`0.90291` | PD POC=`0.89932` | PD VAL=`0.89572` | PDH=`0.90471` | PDL=`0.89392` | PDC=`0.89932`
  * Monday Reference: Monday High=`0.90381` | Monday Low=`0.89482` | Monday Mid=`0.89932`
  * Weekly Value Area: Weekly VAH=`0.90651` | Weekly POC=`0.89932` | Weekly VAL=`0.89212`
  * Multi-Week Extremes: Current Week High (CWH)=`0.90831` | CWL=`0.89032` | Prior Week High (PWH)=`0.91280` | PWL=`0.88583`
  * Multi-Month Extremes: Current Month High (CMH)=`0.91730` | CML=`0.88133` | Prior Month High (PMH)=`0.92180` | PML=`0.87683`
- **Session Liquidity Extremes & Initial Balance**:
  * Asian Session: Range `[0.89752 - 0.90111]`
  * London Session: Range `[0.89572 - 0.90291]`
  * New York Session: Range `[0.89482 - 0.90381]`
  * Initial Balance (IB): IB High=`0.90201` | IB Low=`0.89662`
- **Fibonacci Golden Pocket & Optimal Trade Entry (OTE)**:
  * Swing Range: High=`0.90500` | Low=`0.89908` | Direction=`NONE`
  * Golden Pocket [0.618 - 0.65]: `[0.89752 - 0.90111]`
  * Optimal Trade Entry (0.702): `0.89932` | Invalidation Level: `0.00000` | Status: **`NONE`**
- **Classical & Weekly Pivots**:
  * Daily Classical: Pivot=`0.89932` | R1=`0.90201` | S1=`0.89662` | R2=`0.90471` | S2=`0.89392`
  * Weekly Classical: Weekly Pivot=`0.89932` | Weekly R1=`0.90831` | Weekly S1=`0.89032`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Orderflow
*(Sources: 18_CVD.parquet, 18_CVD_30D_5m.parquet, 18_CVD_30D_15m.parquet, 18_CVD_30D_1h.parquet, 18_CVD_30D_4h.parquet, 18_CVD_30D_ALL.parquet, 21_Tradfye_Orderflow.parquet)*
- **Interbank Spot Orderflow Mechanics**: Decentralized OTC market structure. CVD taker deltas do not apply to interbank spot flow. Tape volume governed by broker tick volume with live spread friction of `0.56 bps`.
- **Session Volume Structure**: Price operating at `INSIDE_VALUE (Balance)` with Daily POC at `0.90106` (VAH: `0.90290` / VAL: `0.89911`).

---

## 5. Institutional Whale Armor & Resting Orderbook Depth
*(Sources: 10_Whale_Orders.parquet, 12_Hyperdash.parquet, 17_Orderbook.parquet, 4_Hyperliquid_Analysis.parquet)*
- **Interbank Institutional Tier-1 Depth**: Decentralized OTC spot liquidity. Resting whale limit walls from crypto venues do not apply.
- **Verified Broker Armor**: Live Bid `0.89929` / Live Ask `0.89934` with institutional spread of `0.56 bps`. Structural defense anchored at Asian Range `[0.89752 - 0.90111]` and London Range `[0.89572 - 0.90291]`.

---

## 6. Liquidation Max Pain, Heatmaps & Cascade Boundaries
*(Sources: 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 14_Hyperdash_Liq_Map.parquet, 14_Liquidation_Matrix.parquet, 15_Hyperdash_Stops_Map.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **TradFi Structural Liquidity Boundaries**: Centralized perp liquidation feeds do not apply to interbank OTC spot.
- **Stop-Run Cascades & Liquidity Pools**: Primary institutional stop pools reside beyond Classical Pivot extremes (S1: `0.89662` / S2: `0.89392` for long stops; R1: `0.90201` / R2: `0.90471` for short stops) and Asian session extremes `[0.89752 - 0.90111]`.

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
- **Decentralized Spot Flow Profile**: Footprint bar metrics and crypto ETF flows not applicable to OTC spot interbank asset.
- **Institutional Tape Dynamics**: Multi-dealer foreign exchange volume driven by international trade settlements, sovereign reserve reallocation, and London/NY fixing windows.

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
- **Real-Time Macro Catalysts & Headlines (19_News.parquet)**:
  * `13 hr ago` [Trade & Geopolitics]: International Trade Price Indexes, Australia, September 2026 (abs.gov.au)
  * `38 hr ago` [Inflation & CPI]: Australia CPI explained: why 2 inflation readings land today and which one the RBA watches (investinglive.com)

---

## 10. Algorithmic Trade Formulation & Sovereign Decision
- **Sovereign Gate Decision**: **`FAIL_CLOSED_STAND_ASIDE`**
- **Dynamic Capacity Verification**: Active Open=`0` | Resting Pending=`2` | Capacity Check: `N_open + N_pending <= 3` (**`PASS`**)
- **Triple Floor Solvency Check**: Current Equity=`4,744.32 USD` | Hard Floor=`4,775.00 USD` | Buffer=`-30.68 USD` | Solvency Check: **`DEFENSE_MODE`**
- **Stand-Aside Reason**: Absence of statistically validated auction edge and defending resting armor. Standing aside preserves statutory hard floor.