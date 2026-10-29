# 🔬 MASTER 43-FEED QUANTITATIVE DOSSIER: AUDJPY (AUD/JPY)
**MT5 Symbol**: `AUDJPY.pi` | **Category**: `Forex Cross` | **Tier**: `Tier 2`
**Execution Posture**: `PASSIVE LIMIT ONLY` | **Timestamp**: 2026-10-29 14:43:14 UTC
**Pipeline Clearance**: `QUALIFIED` | **Data Freshness**: `1.2m`

---

## 1. MT5 Live Broker Telemetry & Spread Friction Gate
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet)*
- **Live Bid Quote**: `110.82600` | **Live Ask Quote**: `110.83100` | **Mid Price**: `110.82850`
- **Spread Points**: `5.0 pts` | **Spread BPS**: `0.45 bps` (Mandatory Cap: `5.0 bps`)
- **Gate Status**: **`PASS`** (Spread friction within mandatory threshold; safe for maker execution)
- **Order Allowed**: `BUY_LIMIT / SELL_LIMIT` | **Pillar 1 Clearance**: `QUALIFIED`
- **Broker Specifications**: Contract Size=`1.00` | Tick Value=`1.00 USD` | Min Lot=`0.01` | Digits=`5`
- **Account Capital Context**: Balance=`4,744.55 USD` | Equity=`4,744.32 USD` | Free Margin=`4,342.62 USD` | Inviolate Hard Floor=`4,775.00 USD` (Cushion: `-30.68 USD`)
- **Pipeline Health**: Feed #00 Status=`PASS` | Overall Pipeline Telemetry=`33/33 FEEDS PASS (SYNCHRONIZED)`

---

## 2. Technical Profile, Multi-Sigma VWAP Dispersion & Volatility
*(Sources: 11_Technical.parquet, 11_Technical_BTC_Ribbon.parquet)*
- **Last Verified Price**: `110.77600` | **24h Change**: `-0.51%` (24h High: `111.56300`, 24h Low: `110.69700`)
- **Weekly Range**: Week High=`111.56300` | Week Low=`110.36000` | Daily POC=`111.09800` | Daily VAH=`111.35200` | Daily VAL=`111.04600`
- **Session VWAP**: `111.17899` | **Rolling 24h VWAP**: `111.25160` | **Distance to VWAP**: `-0.36%`
- **VWAP Z-Score**: `-2.52 sigma` | **Mean Reversion Bias**: **`EXTREME OVERSOLD`**
- **VWAP Dispersion Bands**:
  * +1.00 sigma: `111.33891` | -1.00 sigma: `111.01906`
  * +1.28 sigma (80% CI): `111.38369` | -1.28 sigma: `110.97429`
  * +2.00 sigma (95% CI): `111.49884` | -2.00 sigma: `110.85914`
  * +2.01 sigma: `111.50044` | -2.01 sigma: `110.85754`
  * +2.51 sigma (98.8% CI): `111.58040` | -2.51 sigma: `110.77758`
  * +3.00 sigma (99.7% CI Extreme): `111.65876` | -3.00 sigma: `110.69921`
- **Oscillators & Volatility**:
  * **RSI (14)**: `23.20` | **RSI State**: **`OVERSOLD`**
  * **ATR (14)**: `0.08653` | **ATR %**: `0.08%`
  * **Bollinger Bands**: Upper=`111.28526` | Mid=`111.06455` | Lower=`110.84384` | Bandwidth=`0.40%`
  * **MACD**: Line=`-0.0769` | Signal=`-0.0454` | Hist=`-0.0315`
- **Exponential Moving Average Ribbon (EMA)**:
  * Short Horizon: EMA-5=`110.89450` | EMA-9=`110.96311` | EMA-13=`111.00212` | EMA-20=`111.04471`
  * Intermediate: EMA-34=`111.09811` | EMA-50=`111.13489` | EMA-89=`111.16321` | EMA-100=`111.16175`
  * Institutional: EMA-144=`111.13392` | EMA-200=`111.07855` (Slope: `-0.004%`) | EMA-233=`111.02922` (Slope: `+0.001%`)
  * **Trend Bias**: **`BEARISH`**

---

## 3. Auction Market Structure & Value Profile
*(Sources: 20_Auction_Market_Structure.parquet)*
- **Daily Auction Value Area**:
  * High (VAH): `111.35200` | Point of Control (POC): `111.09800` | Low (VAL): `111.04600`
  * Distance to POC: `-0.24%` | Distance to VAH: `-0.46%` | Distance to VAL: `-0.19%`
  * **Value Area Position**: **`BELOW_VALUE (Imbalance)`** | **Auction Regime**: **`TREND_DOWN_ACCEPTANCE`** | **Session Bias**: **`BEARISH (Below Pivot)`**
- **Prior Day & Weekly Auction Profile**:
  * Prior Day: PD VAH=`111.47900` | PD POC=`111.37400` | PD VAL=`111.06600` | PDH=`111.49800` | PDL=`110.86600` | PDC=`111.32000`
  * Monday Reference: Monday High=`110.75700` | Monday Low=`110.08100` | Monday Mid=`110.41900`
  * Weekly Value Area: Weekly VAH=`111.44900` | Weekly POC=`111.00500` | Weekly VAL=`110.62900`
  * Multi-Week Extremes: Current Week High (CWH)=`111.56300` | CWL=`110.08100` | Prior Week High (PWH)=`111.30700` | PWL=`109.48700`
  * Multi-Month Extremes: Current Month High (CMH)=`111.56300` | CML=`108.63300` | Prior Month High (PMH)=`114.67300` | PML=`108.88800`
- **Session Liquidity Extremes & Initial Balance**:
  * Asian Session: Range `[111.17200 - 111.56300]`
  * London Session: Range `[110.99900 - 111.41000]`
  * New York Session: Range `[110.69700 - 111.23000]`
  * Initial Balance (IB): IB High=`111.41000` | IB Low=`111.20400`
- **Fibonacci Golden Pocket & Optimal Trade Entry (OTE)**:
  * Swing Range: High=`111.56300` | Low=`110.69700` | Direction=`BEARISH_IMPULSE`
  * Golden Pocket [0.618 - 0.65]: `[111.23200 - 111.26000]`
  * Optimal Trade Entry (0.702): `111.30500` | Invalidation Level: `111.37800` | Status: **`SHALLOW_RETRACE`**
- **Classical & Weekly Pivots**:
  * Daily Classical: Pivot=`111.22800` | R1=`111.59000` | S1=`110.95800` | R2=`111.86000` | S2=`110.59600`
  * Weekly Classical: Weekly Pivot=`110.36600` | Weekly R1=`111.24400` | Weekly S1=`109.42400`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Orderflow
*(Sources: 18_CVD.parquet, 18_CVD_30D_5m.parquet, 18_CVD_30D_15m.parquet, 18_CVD_30D_1h.parquet, 18_CVD_30D_4h.parquet, 18_CVD_30D_ALL.parquet, 21_Tradfye_Orderflow.parquet)*
- **Interbank Spot Orderflow Mechanics**: Decentralized OTC market structure. CVD taker deltas do not apply to interbank spot flow. Tape volume governed by broker tick volume with live spread friction of `0.45 bps`.
- **Session Volume Structure**: Price operating at `BELOW_VALUE (Imbalance)` with Daily POC at `111.09800` (VAH: `111.35200` / VAL: `111.04600`).

---

## 5. Institutional Whale Armor & Resting Orderbook Depth
*(Sources: 10_Whale_Orders.parquet, 12_Hyperdash.parquet, 17_Orderbook.parquet, 4_Hyperliquid_Analysis.parquet)*
- **Interbank Institutional Tier-1 Depth**: Decentralized OTC spot liquidity. Resting whale limit walls from crypto venues do not apply.
- **Verified Broker Armor**: Live Bid `110.82600` / Live Ask `110.83100` with institutional spread of `0.45 bps`. Structural defense anchored at Asian Range `[111.17200 - 111.56300]` and London Range `[110.99900 - 111.41000]`.

---

## 6. Liquidation Max Pain, Heatmaps & Cascade Boundaries
*(Sources: 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 14_Hyperdash_Liq_Map.parquet, 14_Liquidation_Matrix.parquet, 15_Hyperdash_Stops_Map.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **TradFi Structural Liquidity Boundaries**: Centralized perp liquidation feeds do not apply to interbank OTC spot.
- **Stop-Run Cascades & Liquidity Pools**: Primary institutional stop pools reside beyond Classical Pivot extremes (S1: `110.95800` / S2: `110.59600` for long stops; R1: `111.59000` / R2: `111.86000` for short stops) and Asian session extremes `[111.17200 - 111.56300]`.

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
  * `Mon Oct 26 2:40am` [AUD - Low Impact]: RBA Assist Gov Jones Speaks (Forecast: , Previous: )
  * `Tue Oct 27 5:20am` [JPY - Low Impact]: SPPI y/y (Forecast: 3.7%, Previous: 3.5%)
  * `Tue Oct 27 10:30am` [JPY - Low Impact]: BOJ Core CPI y/y (Forecast: 1.9%, Previous: 1.8%)
- **Real-Time Macro Catalysts & Headlines (19_News.parquet)**:
  * `7 hr ago` [General Market Intel]: Japan's consumer confidence weakens in October (breakingthenews.net)
  * `13 hr ago` [Trade & Geopolitics]: International Trade Price Indexes, Australia, September 2026 (abs.gov.au)
  * `38 hr ago` [Inflation & CPI]: Australia CPI explained: why 2 inflation readings land today and which one the RBA watches (investinglive.com)

---

## 10. Algorithmic Trade Formulation & Sovereign Decision
- **Sovereign Gate Decision**: **`FAIL_CLOSED_STAND_ASIDE`**
- **Dynamic Capacity Verification**: Active Open=`0` | Resting Pending=`2` | Capacity Check: `N_open + N_pending <= 3` (**`PASS`**)
- **Triple Floor Solvency Check**: Current Equity=`4,744.32 USD` | Hard Floor=`4,775.00 USD` | Buffer=`-30.68 USD` | Solvency Check: **`DEFENSE_MODE`**
- **Stand-Aside Reason**: Absence of statistically validated auction edge and defending resting armor. Standing aside preserves statutory hard floor.