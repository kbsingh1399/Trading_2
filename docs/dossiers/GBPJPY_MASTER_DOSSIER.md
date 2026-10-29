# 🔬 MASTER 43-FEED QUANTITATIVE DOSSIER: GBPJPY (British Pound / Japanese Yen)
**MT5 Symbol**: `GBPJPY.pi` | **Category**: `FX Cross` | **Tier**: `Tier 3`
**Execution Posture**: `PASSIVE LIMIT ONLY` | **Timestamp**: 2026-10-29 14:43:14 UTC
**Pipeline Clearance**: `QUALIFIED` | **Data Freshness**: `1.2m`

---

## 1. MT5 Live Broker Telemetry & Spread Friction Gate
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet)*
- **Live Bid Quote**: `210.50000` | **Live Ask Quote**: `210.50500` | **Mid Price**: `210.50250`
- **Spread Points**: `5.0 pts` | **Spread BPS**: `0.24 bps` (Mandatory Cap: `5.0 bps`)
- **Gate Status**: **`PASS`** (Spread friction within mandatory threshold; safe for maker execution)
- **Order Allowed**: `BUY_LIMIT / SELL_LIMIT` | **Pillar 1 Clearance**: `QUALIFIED`
- **Broker Specifications**: Contract Size=`1.00` | Tick Value=`1.00 USD` | Min Lot=`0.01` | Digits=`5`
- **Account Capital Context**: Balance=`4,744.55 USD` | Equity=`4,744.32 USD` | Free Margin=`4,342.62 USD` | Inviolate Hard Floor=`4,775.00 USD` (Cushion: `-30.68 USD`)
- **Pipeline Health**: Feed #00 Status=`PASS` | Overall Pipeline Telemetry=`33/33 FEEDS PASS (SYNCHRONIZED)`

---

## 2. Technical Profile, Multi-Sigma VWAP Dispersion & Volatility
*(Sources: 11_Technical.parquet, 11_Technical_BTC_Ribbon.parquet)*
- **Last Verified Price**: `210.29300` | **24h Change**: `+0.04%` (24h High: `210.66300`, 24h Low: `209.97100`)
- **Weekly Range**: Week High=`210.66300` | Week Low=`209.56600` | Daily POC=`210.20400` | Daily VAH=`210.39800` | Daily VAL=`210.07900`
- **Session VWAP**: `210.29723` | **Rolling 24h VWAP**: `210.35308` | **Distance to VWAP**: `-0.00%`
- **VWAP Z-Score**: `-0.03 sigma` | **Mean Reversion Bias**: **`FAIR VALUE`**
- **VWAP Dispersion Bands**:
  * +1.00 sigma: `210.45055` | -1.00 sigma: `210.14391`
  * +1.28 sigma (80% CI): `210.49348` | -1.28 sigma: `210.10098`
  * +2.00 sigma (95% CI): `210.60387` | -2.00 sigma: `209.99060`
  * +2.01 sigma: `210.60540` | -2.01 sigma: `209.98906`
  * +2.51 sigma (98.8% CI): `210.68206` | -2.51 sigma: `209.91240`
  * +3.00 sigma (99.7% CI Extreme): `210.75719` | -3.00 sigma: `209.83728`
- **Oscillators & Volatility**:
  * **RSI (14)**: `44.74` | **RSI State**: **`BEARISH`**
  * **ATR (14)**: `0.13586` | **ATR %**: `0.06%`
  * **Bollinger Bands**: Upper=`210.75666` | Mid=`210.41320` | Lower=`210.06974` | Bandwidth=`0.33%`
  * **MACD**: Line=`+0.0386` | Signal=`+0.0701` | Hist=`-0.0315`
- **Exponential Moving Average Ribbon (EMA)**:
  * Short Horizon: EMA-5=`210.37288` | EMA-9=`210.41712` | EMA-13=`210.42256` | EMA-20=`210.40420`
  * Intermediate: EMA-34=`210.36225` | EMA-50=`210.33011` | EMA-89=`210.27967` | EMA-100=`210.26953`
  * Institutional: EMA-144=`210.23933` | EMA-200=`210.23848` (Slope: `+0.015%`) | EMA-233=`210.20880` (Slope: `+0.014%`)
  * **Trend Bias**: **`NEUTRAL / CHOP`**

---

## 3. Auction Market Structure & Value Profile
*(Sources: 20_Auction_Market_Structure.parquet)*
- **Daily Auction Value Area**:
  * High (VAH): `210.39800` | Point of Control (POC): `210.20400` | Low (VAL): `210.07900`
  * Distance to POC: `+0.14%` | Distance to VAH: `+0.05%` | Distance to VAL: `+0.20%`
  * **Value Area Position**: **`ABOVE_VALUE (Imbalance)`** | **Auction Regime**: **`RANGE_EXPANSION`** | **Session Bias**: **`BULLISH (Above Pivot)`**
- **Prior Day & Weekly Auction Profile**:
  * Prior Day: PD VAH=`210.65000` | PD POC=`210.45500` | PD VAL=`209.89600` | PDH=`210.65400` | PDL=`209.56600` | PDC=`210.30900`
  * Monday Reference: Monday High=`210.42800` | Monday Low=`209.63100` | Monday Mid=`210.02900`
  * Weekly Value Area: Weekly VAH=`210.41100` | Weekly POC=`210.19900` | Weekly VAL=`209.89900`
  * Multi-Week Extremes: Current Week High (CWH)=`210.66300` | CWL=`209.56600` | Prior Week High (PWH)=`211.98900` | PWL=`209.11800`
  * Multi-Month Extremes: Current Month High (CMH)=`211.98900` | CML=`207.58300` | Prior Month High (PMH)=`216.83700` | PML=`206.88800`
- **Session Liquidity Extremes & Initial Balance**:
  * Asian Session: Range `[210.07800 - 210.43400]`
  * London Session: Range `[209.97100 - 210.66300]`
  * New York Session: Range `[210.11300 - 210.66300]`
  * Initial Balance (IB): IB High=`210.29700` | IB Low=`210.09600`
- **Fibonacci Golden Pocket & Optimal Trade Entry (OTE)**:
  * Swing Range: High=`210.66300` | Low=`209.97100` | Direction=`BULLISH_IMPULSE`
  * Golden Pocket [0.618 - 0.65]: `[210.21300 - 210.23500]`
  * Optimal Trade Entry (0.702): `210.17700` | Invalidation Level: `210.11900` | Status: **`SHALLOW_RETRACE`**
- **Classical & Weekly Pivots**:
  * Daily Classical: Pivot=`210.17600` | R1=`210.78700` | S1=`209.69900` | R2=`211.26400` | S2=`209.08800`
  * Weekly Classical: Weekly Pivot=`210.29000` | Weekly R1=`211.46100` | Weekly S1=`208.59000`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Orderflow
*(Sources: 18_CVD.parquet, 18_CVD_30D_5m.parquet, 18_CVD_30D_15m.parquet, 18_CVD_30D_1h.parquet, 18_CVD_30D_4h.parquet, 18_CVD_30D_ALL.parquet, 21_Tradfye_Orderflow.parquet)*
- **Interbank Spot Orderflow Mechanics**: Decentralized OTC market structure. CVD taker deltas do not apply to interbank spot flow. Tape volume governed by broker tick volume with live spread friction of `0.24 bps`.
- **Session Volume Structure**: Price operating at `ABOVE_VALUE (Imbalance)` with Daily POC at `210.20400` (VAH: `210.39800` / VAL: `210.07900`).

---

## 5. Institutional Whale Armor & Resting Orderbook Depth
*(Sources: 10_Whale_Orders.parquet, 12_Hyperdash.parquet, 17_Orderbook.parquet, 4_Hyperliquid_Analysis.parquet)*
- **Interbank Institutional Tier-1 Depth**: Decentralized OTC spot liquidity. Resting whale limit walls from crypto venues do not apply.
- **Verified Broker Armor**: Live Bid `210.50000` / Live Ask `210.50500` with institutional spread of `0.24 bps`. Structural defense anchored at Asian Range `[210.07800 - 210.43400]` and London Range `[209.97100 - 210.66300]`.

---

## 6. Liquidation Max Pain, Heatmaps & Cascade Boundaries
*(Sources: 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 14_Hyperdash_Liq_Map.parquet, 14_Liquidation_Matrix.parquet, 15_Hyperdash_Stops_Map.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **TradFi Structural Liquidity Boundaries**: Centralized perp liquidation feeds do not apply to interbank OTC spot.
- **Stop-Run Cascades & Liquidity Pools**: Primary institutional stop pools reside beyond Classical Pivot extremes (S1: `209.69900` / S2: `209.08800` for long stops; R1: `210.78700` / R2: `211.26400` for short stops) and Asian session extremes `[210.07800 - 210.43400]`.

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
  * Mid-Tier CEX Rates: KuCoin=`+0.0000%` | MEXC=`+0.0200%` | Gate=`+0.0000%` | BingX=`+0.0000%` | Bitunix=`+0.0000%`
  * Alternative Venues: WhiteBIT=`+0.0000%` | LBank=`+0.0200%` | tradeXYZ=`-0.0012%`
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
  * Prevailing Policy Stance: `Bank of England Bank Rate (5.00%) Restrictive vs Fed Funds (4.75-5.00%)`
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
  * `Sun Oct 25 6:30am` [GBP - Low Impact]: Daylight Saving Time Shift (Forecast: , Previous: )
  * `Mon Oct 26 4:30pm` [GBP - Low Impact]: CBI Realized Sales (Forecast: -47, Previous: -55)
  * `Tue Oct 27 5:20am` [JPY - Low Impact]: SPPI y/y (Forecast: 3.7%, Previous: 3.5%)
- **Real-Time Macro Catalysts & Headlines (19_News.parquet)**:
  * `4 hr ago` [General Market Intel]: UK Money and Credit - September 2026 (bankofengland.co.uk)
  * `7 hr ago` [General Market Intel]: Japan's consumer confidence weakens in October (breakingthenews.net)

---

## 10. Algorithmic Trade Formulation & Sovereign Decision
- **Sovereign Gate Decision**: **`FAIL_CLOSED_STAND_ASIDE`**
- **Dynamic Capacity Verification**: Active Open=`0` | Resting Pending=`2` | Capacity Check: `N_open + N_pending <= 3` (**`PASS`**)
- **Triple Floor Solvency Check**: Current Equity=`4,744.32 USD` | Hard Floor=`4,775.00 USD` | Buffer=`-30.68 USD` | Solvency Check: **`DEFENSE_MODE`**
- **Stand-Aside Reason**: Absence of statistically validated auction edge and defending resting armor. Standing aside preserves statutory hard floor.