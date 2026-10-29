# 🔬 MASTER 43-FEED QUANTITATIVE DOSSIER: CADJPY (CAD/JPY)
**MT5 Symbol**: `CADJPY.pi` | **Category**: `Forex Cross` | **Tier**: `Tier 2`
**Execution Posture**: `PASSIVE LIMIT ONLY` | **Timestamp**: 2026-10-29 14:43:14 UTC
**Pipeline Clearance**: `QUALIFIED` | **Data Freshness**: `1.2m`

---

## 1. MT5 Live Broker Telemetry & Spread Friction Gate
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet)*
- **Live Bid Quote**: `112.78600` | **Live Ask Quote**: `112.79300` | **Mid Price**: `112.78950`
- **Spread Points**: `7.0 pts` | **Spread BPS**: `0.62 bps` (Mandatory Cap: `5.0 bps`)
- **Gate Status**: **`PASS`** (Spread friction within mandatory threshold; safe for maker execution)
- **Order Allowed**: `BUY_LIMIT / SELL_LIMIT` | **Pillar 1 Clearance**: `QUALIFIED`
- **Broker Specifications**: Contract Size=`1.00` | Tick Value=`1.00 USD` | Min Lot=`0.01` | Digits=`5`
- **Account Capital Context**: Balance=`4,744.55 USD` | Equity=`4,744.32 USD` | Free Margin=`4,342.62 USD` | Inviolate Hard Floor=`4,775.00 USD` (Cushion: `-30.68 USD`)
- **Pipeline Health**: Feed #00 Status=`PASS` | Overall Pipeline Telemetry=`33/33 FEEDS PASS (SYNCHRONIZED)`

---

## 2. Technical Profile, Multi-Sigma VWAP Dispersion & Volatility
*(Sources: 11_Technical.parquet, 11_Technical_BTC_Ribbon.parquet)*
- **Last Verified Price**: `112.72200` | **24h Change**: `+0.10%` (24h High: `113.10700`, 24h Low: `112.51200`)
- **Weekly Range**: Week High=`113.10700` | Week Low=`111.96700` | Daily POC=`112.83000` | Daily VAH=`112.94200` | Daily VAL=`112.77500`
- **Session VWAP**: `112.86978` | **Rolling 24h VWAP**: `112.80785` | **Distance to VWAP**: `-0.13%`
- **VWAP Z-Score**: `-1.68 sigma` | **Mean Reversion Bias**: **`OVERSOLD`**
- **VWAP Dispersion Bands**:
  * +1.00 sigma: `112.95763` | -1.00 sigma: `112.78194`
  * +1.28 sigma (80% CI): `112.98222` | -1.28 sigma: `112.75734`
  * +2.00 sigma (95% CI): `113.04547` | -2.00 sigma: `112.69410`
  * +2.01 sigma: `113.04635` | -2.01 sigma: `112.69322`
  * +2.51 sigma (98.8% CI): `113.09027` | -2.51 sigma: `112.64930`
  * +3.00 sigma (99.7% CI Extreme): `113.13331` | -3.00 sigma: `112.60625`
- **Oscillators & Volatility**:
  * **RSI (14)**: `35.43` | **RSI State**: **`BEARISH`**
  * **ATR (14)**: `0.08186` | **ATR %**: `0.07%`
  * **Bollinger Bands**: Upper=`113.14483` | Mid=`112.92575` | Lower=`112.70667` | Bandwidth=`0.39%`
  * **MACD**: Line=`-0.0133` | Signal=`+0.0241` | Hist=`-0.0374`
- **Exponential Moving Average Ribbon (EMA)**:
  * Short Horizon: EMA-5=`112.80086` | EMA-9=`112.85964` | EMA-13=`112.88355` | EMA-20=`112.89418`
  * Intermediate: EMA-34=`112.88607` | EMA-50=`112.86498` | EMA-89=`112.79929` | EMA-100=`112.78103`
  * Institutional: EMA-144=`112.71810` | EMA-200=`112.66400` (Slope: `+0.032%`) | EMA-233=`112.61873` (Slope: `+0.031%`)
  * **Trend Bias**: **`NEUTRAL / CHOP`**

---

## 3. Auction Market Structure & Value Profile
*(Sources: 20_Auction_Market_Structure.parquet)*
- **Daily Auction Value Area**:
  * High (VAH): `112.94200` | Point of Control (POC): `112.83000` | Low (VAL): `112.77500`
  * Distance to POC: `-0.04%` | Distance to VAH: `-0.14%` | Distance to VAL: `+0.01%`
  * **Value Area Position**: **`INSIDE_VALUE (Balance)`** | **Auction Regime**: **`ROTATIONAL_BALANCE`** | **Session Bias**: **`BULLISH (Above Pivot)`**
- **Prior Day & Weekly Auction Profile**:
  * Prior Day: PD VAH=`112.81100` | PD POC=`112.71400` | PD VAL=`112.31900` | PDH=`112.90100` | PDL=`112.13200` | PDC=`112.76200`
  * Monday Reference: Monday High=`112.40400` | Monday Low=`111.76300` | Monday Mid=`112.08400`
  * Weekly Value Area: Weekly VAH=`112.65500` | Weekly POC=`112.52000` | Weekly VAL=`111.90200`
  * Multi-Week Extremes: Current Week High (CWH)=`113.10700` | CWL=`111.76300` | Prior Week High (PWH)=`112.69200` | PWL=`111.48500`
  * Multi-Month Extremes: Current Month High (CMH)=`113.10700` | CML=`110.37700` | Prior Month High (PMH)=`115.42100` | PML=`110.16300`
- **Session Liquidity Extremes & Initial Balance**:
  * Asian Session: Range `[112.71100 - 112.98400]`
  * London Session: Range `[112.74000 - 113.10700]`
  * New York Session: Range `[112.58500 - 113.10700]`
  * Initial Balance (IB): IB High=`112.90200` | IB Low=`112.82000`
- **Fibonacci Golden Pocket & Optimal Trade Entry (OTE)**:
  * Swing Range: High=`113.10700` | Low=`112.51200` | Direction=`BULLISH_IMPULSE`
  * Golden Pocket [0.618 - 0.65]: `[112.72000 - 112.73900]`
  * Optimal Trade Entry (0.702): `112.68900` | Invalidation Level: `112.63900` | Status: **`SHALLOW_RETRACE`**
- **Classical & Weekly Pivots**:
  * Daily Classical: Pivot=`112.59800` | R1=`113.06500` | S1=`112.29600` | R2=`113.36700` | S2=`111.82900`
  * Weekly Classical: Weekly Pivot=`112.03300` | Weekly R1=`112.58100` | Weekly S1=`111.37400`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Orderflow
*(Sources: 18_CVD.parquet, 18_CVD_30D_5m.parquet, 18_CVD_30D_15m.parquet, 18_CVD_30D_1h.parquet, 18_CVD_30D_4h.parquet, 18_CVD_30D_ALL.parquet, 21_Tradfye_Orderflow.parquet)*
- **Interbank Spot Orderflow Mechanics**: Decentralized OTC market structure. CVD taker deltas do not apply to interbank spot flow. Tape volume governed by broker tick volume with live spread friction of `0.62 bps`.
- **Session Volume Structure**: Price operating at `INSIDE_VALUE (Balance)` with Daily POC at `112.83000` (VAH: `112.94200` / VAL: `112.77500`).

---

## 5. Institutional Whale Armor & Resting Orderbook Depth
*(Sources: 10_Whale_Orders.parquet, 12_Hyperdash.parquet, 17_Orderbook.parquet, 4_Hyperliquid_Analysis.parquet)*
- **Interbank Institutional Tier-1 Depth**: Decentralized OTC spot liquidity. Resting whale limit walls from crypto venues do not apply.
- **Verified Broker Armor**: Live Bid `112.78600` / Live Ask `112.79300` with institutional spread of `0.62 bps`. Structural defense anchored at Asian Range `[112.71100 - 112.98400]` and London Range `[112.74000 - 113.10700]`.

---

## 6. Liquidation Max Pain, Heatmaps & Cascade Boundaries
*(Sources: 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 14_Hyperdash_Liq_Map.parquet, 14_Liquidation_Matrix.parquet, 15_Hyperdash_Stops_Map.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **TradFi Structural Liquidity Boundaries**: Centralized perp liquidation feeds do not apply to interbank OTC spot.
- **Stop-Run Cascades & Liquidity Pools**: Primary institutional stop pools reside beyond Classical Pivot extremes (S1: `112.29600` / S2: `111.82900` for long stops; R1: `113.06500` / R2: `113.36700` for short stops) and Asian session extremes `[112.71100 - 112.98400]`.

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
  * Mid-Tier CEX Rates: KuCoin=`+0.0000%` | MEXC=`+0.0126%` | Gate=`+0.0000%` | BingX=`+0.0000%` | Bitunix=`+0.0000%`
  * Alternative Venues: WhiteBIT=`+0.0000%` | LBank=`+0.0000%` | tradeXYZ=`-`
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
  * Prevailing Policy Stance: `Bank of Japan Uncollateralized Call Rate (0.25%) Ultra-Loose vs Fed Funds (4.75-5.00%)`
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
  * `Tue Oct 27 5:20am` [JPY - Low Impact]: SPPI y/y (Forecast: 3.7%, Previous: 3.5%)
  * `Tue Oct 27 10:30am` [JPY - Low Impact]: BOJ Core CPI y/y (Forecast: 1.9%, Previous: 1.8%)
- **Real-Time Macro Catalysts & Headlines (19_News.parquet)**:
  * `9 min ago` [General Market Intel]: EU's Von der Leyen: talks under way on Canada as first associate member of EU (@financialjuice)
  * `7 hr ago` [General Market Intel]: Japan's consumer confidence weakens in October (breakingthenews.net)
  * `12 hr ago` [General Market Intel]: Kudos to the Bank of Canada (scotiabank.com)

---

## 10. Algorithmic Trade Formulation & Sovereign Decision
- **Sovereign Gate Decision**: **`FAIL_CLOSED_STAND_ASIDE`**
- **Dynamic Capacity Verification**: Active Open=`0` | Resting Pending=`2` | Capacity Check: `N_open + N_pending <= 3` (**`PASS`**)
- **Triple Floor Solvency Check**: Current Equity=`4,744.32 USD` | Hard Floor=`4,775.00 USD` | Buffer=`-30.68 USD` | Solvency Check: **`DEFENSE_MODE`**
- **Stand-Aside Reason**: Absence of statistically validated auction edge and defending resting armor. Standing aside preserves statutory hard floor.