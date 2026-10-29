# 🔬 MASTER 43-FEED QUANTITATIVE DOSSIER: AUDCHF (AUD/CHF)
**MT5 Symbol**: `AUDCHF.pi` | **Category**: `Forex Cross` | **Tier**: `Tier 2`
**Execution Posture**: `PASSIVE LIMIT ONLY` | **Timestamp**: 2026-10-29 14:43:14 UTC
**Pipeline Clearance**: `QUALIFIED` | **Data Freshness**: `1.2m`

---

## 1. MT5 Live Broker Telemetry & Spread Friction Gate
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet)*
- **Live Bid Quote**: `0.58129` | **Live Ask Quote**: `0.58133` | **Mid Price**: `0.58131`
- **Spread Points**: `4.0 pts` | **Spread BPS**: `0.69 bps` (Mandatory Cap: `5.0 bps`)
- **Gate Status**: **`PASS`** (Spread friction within mandatory threshold; safe for maker execution)
- **Order Allowed**: `BUY_LIMIT / SELL_LIMIT` | **Pillar 1 Clearance**: `QUALIFIED`
- **Broker Specifications**: Contract Size=`1.00` | Tick Value=`1.00 USD` | Min Lot=`0.01` | Digits=`5`
- **Account Capital Context**: Balance=`4,744.55 USD` | Equity=`4,744.32 USD` | Free Margin=`4,342.62 USD` | Inviolate Hard Floor=`4,775.00 USD` (Cushion: `-30.68 USD`)
- **Pipeline Health**: Feed #00 Status=`PASS` | Overall Pipeline Telemetry=`33/33 FEEDS PASS (SYNCHRONIZED)`

---

## 2. Technical Profile, Multi-Sigma VWAP Dispersion & Volatility
*(Sources: 11_Technical.parquet, 11_Technical_BTC_Ribbon.parquet)*
- **Last Verified Price**: `0.58128` | **24h Change**: `-0.58%` (24h High: `0.58522`, 24h Low: `0.58100`)
- **Weekly Range**: Week High=`0.58522` | Week Low=`0.57939` | Daily POC=`0.58259` | Daily VAH=`0.58428` | Daily VAL=`0.58186`
- **Session VWAP**: `0.58327` | **Rolling 24h VWAP**: `0.58363` | **Distance to VWAP**: `-0.34%`
- **VWAP Z-Score**: `-1.96 sigma` | **Mean Reversion Bias**: **`OVERSOLD`**
- **VWAP Dispersion Bands**:
  * +1.00 sigma: `0.58429` | -1.00 sigma: `0.58226`
  * +1.28 sigma (80% CI): `0.58457` | -1.28 sigma: `0.58197`
  * +2.00 sigma (95% CI): `0.58531` | -2.00 sigma: `0.58124`
  * +2.01 sigma: `0.58532` | -2.01 sigma: `0.58123`
  * +2.51 sigma (98.8% CI): `0.58582` | -2.51 sigma: `0.58072`
  * +3.00 sigma (99.7% CI Extreme): `0.58632` | -3.00 sigma: `0.58022`
- **Oscillators & Volatility**:
  * **RSI (14)**: `25.75` | **RSI State**: **`OVERSOLD`**
  * **ATR (14)**: `0.00044` | **ATR %**: `0.08%`
  * **Bollinger Bands**: Upper=`0.58327` | Mid=`0.58242` | Lower=`0.58157` | Bandwidth=`0.29%`
  * **MACD**: Line=`-0.0004` | Signal=`-0.0004` | Hist=`-0.0001`
- **Exponential Moving Average Ribbon (EMA)**:
  * Short Horizon: EMA-5=`0.58174` | EMA-9=`0.58198` | EMA-13=`0.58215` | EMA-20=`0.58239`
  * Intermediate: EMA-34=`0.58274` | EMA-50=`0.58301` | EMA-89=`0.58330` | EMA-100=`0.58332`
  * Institutional: EMA-144=`0.58327` | EMA-200=`0.58301` (Slope: `-0.017%`) | EMA-233=`0.58283` (Slope: `-0.011%`)
  * **Trend Bias**: **`BEARISH`**

---

## 3. Auction Market Structure & Value Profile
*(Sources: 20_Auction_Market_Structure.parquet)*
- **Daily Auction Value Area**:
  * High (VAH): `0.58428` | Point of Control (POC): `0.58259` | Low (VAL): `0.58186`
  * Distance to POC: `-0.22%` | Distance to VAH: `-0.50%` | Distance to VAL: `-0.09%`
  * **Value Area Position**: **`BELOW_VALUE (Imbalance)`** | **Auction Regime**: **`TREND_DOWN_ACCEPTANCE`** | **Session Bias**: **`BEARISH (Below Pivot)`**
- **Prior Day & Weekly Auction Profile**:
  * Prior Day: PD VAH=`0.58441` | PD POC=`0.58410` | PD VAL=`0.58358` | PDH=`0.58494` | PDL=`0.58167` | PDC=`0.58397`
  * Monday Reference: Monday High=`0.58154` | Monday Low=`0.57842` | Monday Mid=`0.57998`
  * Weekly Value Area: Weekly VAH=`0.58479` | Weekly POC=`0.58411` | Weekly VAL=`0.58112`
  * Multi-Week Extremes: Current Week High (CWH)=`0.58522` | CWL=`0.57842` | Prior Week High (PWH)=`0.58086` | PWL=`0.57307`
  * Multi-Month Extremes: Current Month High (CMH)=`0.58522` | CML=`0.57044` | Prior Month High (PMH)=`0.58825` | PML=`0.57804`
- **Session Liquidity Extremes & Initial Balance**:
  * Asian Session: Range `[0.58330 - 0.58522]`
  * London Session: Range `[0.58190 - 0.58493]`
  * New York Session: Range `[0.58100 - 0.58312]`
  * Initial Balance (IB): IB High=`0.58493` | IB Low=`0.58414`
- **Fibonacci Golden Pocket & Optimal Trade Entry (OTE)**:
  * Swing Range: High=`0.58522` | Low=`0.58100` | Direction=`BEARISH_IMPULSE`
  * Golden Pocket [0.618 - 0.65]: `[0.58361 - 0.58374]`
  * Optimal Trade Entry (0.702): `0.58396` | Invalidation Level: `0.58432` | Status: **`SHALLOW_RETRACE`**
- **Classical & Weekly Pivots**:
  * Daily Classical: Pivot=`0.58353` | R1=`0.58538` | S1=`0.58211` | R2=`0.58680` | S2=`0.58026`
  * Weekly Classical: Weekly Pivot=`0.57808` | Weekly R1=`0.58308` | Weekly S1=`0.57529`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Orderflow
*(Sources: 18_CVD.parquet, 18_CVD_30D_5m.parquet, 18_CVD_30D_15m.parquet, 18_CVD_30D_1h.parquet, 18_CVD_30D_4h.parquet, 18_CVD_30D_ALL.parquet, 21_Tradfye_Orderflow.parquet)*
- **Interbank Spot Orderflow Mechanics**: Decentralized OTC market structure. CVD taker deltas do not apply to interbank spot flow. Tape volume governed by broker tick volume with live spread friction of `0.69 bps`.
- **Session Volume Structure**: Price operating at `BELOW_VALUE (Imbalance)` with Daily POC at `0.58259` (VAH: `0.58428` / VAL: `0.58186`).

---

## 5. Institutional Whale Armor & Resting Orderbook Depth
*(Sources: 10_Whale_Orders.parquet, 12_Hyperdash.parquet, 17_Orderbook.parquet, 4_Hyperliquid_Analysis.parquet)*
- **Interbank Institutional Tier-1 Depth**: Decentralized OTC spot liquidity. Resting whale limit walls from crypto venues do not apply.
- **Verified Broker Armor**: Live Bid `0.58129` / Live Ask `0.58133` with institutional spread of `0.69 bps`. Structural defense anchored at Asian Range `[0.58330 - 0.58522]` and London Range `[0.58190 - 0.58493]`.

---

## 6. Liquidation Max Pain, Heatmaps & Cascade Boundaries
*(Sources: 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 14_Hyperdash_Liq_Map.parquet, 14_Liquidation_Matrix.parquet, 15_Hyperdash_Stops_Map.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **TradFi Structural Liquidity Boundaries**: Centralized perp liquidation feeds do not apply to interbank OTC spot.
- **Stop-Run Cascades & Liquidity Pools**: Primary institutional stop pools reside beyond Classical Pivot extremes (S1: `0.58211` / S2: `0.58026` for long stops; R1: `0.58538` / R2: `0.58680` for short stops) and Asian session extremes `[0.58330 - 0.58522]`.

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
  * `Sun Oct 25 6:30am` [CHF - Low Impact]: Daylight Saving Time Shift (Forecast: , Previous: )
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