# 🔬 MASTER 43-FEED QUANTITATIVE DOSSIER: EURAUD (EUR/AUD)
**MT5 Symbol**: `EURAUD.pi` | **Category**: `Forex Cross` | **Tier**: `Tier 2`
**Execution Posture**: `PASSIVE LIMIT ONLY` | **Timestamp**: 2026-10-29 14:43:14 UTC
**Pipeline Clearance**: `QUALIFIED` | **Data Freshness**: `1.2m`

---

## 1. MT5 Live Broker Telemetry & Spread Friction Gate
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet)*
- **Live Bid Quote**: `1.58684` | **Live Ask Quote**: `1.58693` | **Mid Price**: `1.58689`
- **Spread Points**: `9.0 pts` | **Spread BPS**: `0.57 bps` (Mandatory Cap: `5.0 bps`)
- **Gate Status**: **`PASS`** (Spread friction within mandatory threshold; safe for maker execution)
- **Order Allowed**: `BUY_LIMIT / SELL_LIMIT` | **Pillar 1 Clearance**: `QUALIFIED`
- **Broker Specifications**: Contract Size=`1.00` | Tick Value=`1.00 USD` | Min Lot=`0.01` | Digits=`5`
- **Account Capital Context**: Balance=`4,744.55 USD` | Equity=`4,744.32 USD` | Free Margin=`4,342.62 USD` | Inviolate Hard Floor=`4,775.00 USD` (Cushion: `-30.68 USD`)
- **Pipeline Health**: Feed #00 Status=`PASS` | Overall Pipeline Telemetry=`33/33 FEEDS PASS (SYNCHRONIZED)`

---

## 2. Technical Profile, Multi-Sigma VWAP Dispersion & Volatility
*(Sources: 11_Technical.parquet, 11_Technical_BTC_Ribbon.parquet)*
- **Last Verified Price**: `1.58647` | **24h Change**: `+0.35%` (24h High: `1.58670`, 24h Low: `1.57777`)
- **Weekly Range**: Week High=`1.59434` | Week Low=`1.57765` | Daily POC=`1.58450` | Daily VAH=`1.58501` | Daily VAL=`1.58044`
- **Session VWAP**: `1.58223` | **Rolling 24h VWAP**: `1.58207` | **Distance to VWAP**: `+0.27%`
- **VWAP Z-Score**: `+2.14 sigma` | **Mean Reversion Bias**: **`EXTREME OVERBOUGHT`**
- **VWAP Dispersion Bands**:
  * +1.00 sigma: `1.58421` | -1.00 sigma: `1.58025`
  * +1.28 sigma (80% CI): `1.58476` | -1.28 sigma: `1.57970`
  * +2.00 sigma (95% CI): `1.58618` | -2.00 sigma: `1.57828`
  * +2.01 sigma: `1.58620` | -2.01 sigma: `1.57826`
  * +2.51 sigma (98.8% CI): `1.58719` | -2.51 sigma: `1.57727`
  * +3.00 sigma (99.7% CI Extreme): `1.58816` | -3.00 sigma: `1.57630`
- **Oscillators & Volatility**:
  * **RSI (14)**: `68.51` | **RSI State**: **`BULLISH`**
  * **ATR (14)**: `0.00121` | **ATR %**: `0.08%`
  * **Bollinger Bands**: Upper=`1.58582` | Mid=`1.58408` | Lower=`1.58234` | Bandwidth=`0.22%`
  * **MACD**: Line=`+0.0008` | Signal=`+0.0007` | Hist=`+0.0000`
- **Exponential Moving Average Ribbon (EMA)**:
  * Short Horizon: EMA-5=`1.58500` | EMA-9=`1.58465` | EMA-13=`1.58440` | EMA-20=`1.58399`
  * Intermediate: EMA-34=`1.58331` | EMA-50=`1.58283` | EMA-89=`1.58243` | EMA-100=`1.58245`
  * Institutional: EMA-144=`1.58286` | EMA-200=`1.58383` (Slope: `+0.004%`) | EMA-233=`1.58437` (Slope: `+0.000%`)
  * **Trend Bias**: **`BULLISH`**

---

## 3. Auction Market Structure & Value Profile
*(Sources: 20_Auction_Market_Structure.parquet)*
- **Daily Auction Value Area**:
  * High (VAH): `1.58501` | Point of Control (POC): `1.58450` | Low (VAL): `1.58044`
  * Distance to POC: `+0.15%` | Distance to VAH: `+0.12%` | Distance to VAL: `+0.41%`
  * **Value Area Position**: **`ABOVE_VALUE (Imbalance)`** | **Auction Regime**: **`TREND_UP_ACCEPTANCE`** | **Session Bias**: **`BULLISH (Above Pivot)`**
- **Prior Day & Weekly Auction Profile**:
  * Prior Day: PD VAH=`1.58281` | PD POC=`1.58119` | PD VAL=`1.58083` | PDH=`1.58441` | PDL=`1.57765` | PDC=`1.58098`
  * Monday Reference: Monday High=`1.59767` | Monday Low=`1.59191` | Monday Mid=`1.59479`
  * Weekly Value Area: Weekly VAH=`1.58906` | Weekly POC=`1.58119` | Weekly VAL=`1.57772`
  * Multi-Week Extremes: Current Week High (CWH)=`1.59767` | CWL=`1.57765` | Prior Week High (PWH)=`1.61277` | PWL=`1.59036`
  * Multi-Month Extremes: Current Month High (CMH)=`1.63269` | CML=`1.57765` | Prior Month High (PMH)=`1.63350` | PML=`1.60771`
- **Session Liquidity Extremes & Initial Balance**:
  * Asian Session: Range `[1.57777 - 1.58242]`
  * London Session: Range `[1.57896 - 1.58499]`
  * New York Session: Range `[1.58148 - 1.58743]`
  * Initial Balance (IB): IB High=`1.58062` | IB Low=`1.57896`
- **Fibonacci Golden Pocket & Optimal Trade Entry (OTE)**:
  * Swing Range: High=`1.58743` | Low=`1.57777` | Direction=`BULLISH_IMPULSE`
  * Golden Pocket [0.618 - 0.65]: `[1.58115 - 1.58146]`
  * Optimal Trade Entry (0.702): `1.58065` | Invalidation Level: `1.57984` | Status: **`SHALLOW_RETRACE`**
- **Classical & Weekly Pivots**:
  * Daily Classical: Pivot=`1.58101` | R1=`1.58438` | S1=`1.57762` | R2=`1.58777` | S2=`1.57425`
  * Weekly Classical: Weekly Pivot=`1.59838` | Weekly R1=`1.60640` | Weekly S1=`1.58399`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Orderflow
*(Sources: 18_CVD.parquet, 18_CVD_30D_5m.parquet, 18_CVD_30D_15m.parquet, 18_CVD_30D_1h.parquet, 18_CVD_30D_4h.parquet, 18_CVD_30D_ALL.parquet, 21_Tradfye_Orderflow.parquet)*
- **Interbank Spot Orderflow Mechanics**: Decentralized OTC market structure. CVD taker deltas do not apply to interbank spot flow. Tape volume governed by broker tick volume with live spread friction of `0.57 bps`.
- **Session Volume Structure**: Price operating at `ABOVE_VALUE (Imbalance)` with Daily POC at `1.58450` (VAH: `1.58501` / VAL: `1.58044`).

---

## 5. Institutional Whale Armor & Resting Orderbook Depth
*(Sources: 10_Whale_Orders.parquet, 12_Hyperdash.parquet, 17_Orderbook.parquet, 4_Hyperliquid_Analysis.parquet)*
- **Interbank Institutional Tier-1 Depth**: Decentralized OTC spot liquidity. Resting whale limit walls from crypto venues do not apply.
- **Verified Broker Armor**: Live Bid `1.58684` / Live Ask `1.58693` with institutional spread of `0.57 bps`. Structural defense anchored at Asian Range `[1.57777 - 1.58242]` and London Range `[1.57896 - 1.58499]`.

---

## 6. Liquidation Max Pain, Heatmaps & Cascade Boundaries
*(Sources: 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 14_Hyperdash_Liq_Map.parquet, 14_Liquidation_Matrix.parquet, 15_Hyperdash_Stops_Map.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **TradFi Structural Liquidity Boundaries**: Centralized perp liquidation feeds do not apply to interbank OTC spot.
- **Stop-Run Cascades & Liquidity Pools**: Primary institutional stop pools reside beyond Classical Pivot extremes (S1: `1.57762` / S2: `1.57425` for long stops; R1: `1.58438` / R2: `1.58777` for short stops) and Asian session extremes `[1.57777 - 1.58242]`.

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
  * Mid-Tier CEX Rates: KuCoin=`+0.0000%` | MEXC=`+0.0032%` | Gate=`+0.0000%` | BingX=`+0.0000%` | Bitunix=`+0.0000%`
  * Alternative Venues: WhiteBIT=`+0.0000%` | LBank=`+0.0000%` | tradeXYZ=`0.0000%`
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
  * Prevailing Policy Stance: `ECB Deposit Facility (3.40%) Disinflationary Stance vs Fed Funds (4.75-5.00%)`
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
  * `Sun Oct 25 6:30am` [EUR - Low Impact]: Daylight Saving Time Shift (Forecast: , Previous: )
  * `Mon Oct 26 2:40am` [AUD - Low Impact]: RBA Assist Gov Jones Speaks (Forecast: , Previous: )
  * `Mon Oct 26 2:30pm` [EUR - Low Impact]: German ifo Business Climate (Forecast: 90.0, Previous: 89.9)
- **Real-Time Macro Catalysts & Headlines (19_News.parquet)**:
  * `10 min ago` [Central Banks & Rates]: ECB Pres Lagarde: Governing Council Debated Whether Hike Was Appropriate; Council Decided Unanimously To Hold (@LiveSquawk)
  * `30 min ago` [Central Banks & Rates]: ECB's Lagarde: Incoming data suggests economy expanding in Q3 (@financialjuice)
  * `41 min ago` [Central Banks & Rates]: ECB Governing Council Press Conference (youtube.com/ecbeuro)

---

## 10. Algorithmic Trade Formulation & Sovereign Decision
- **Sovereign Gate Decision**: **`FAIL_CLOSED_STAND_ASIDE`**
- **Dynamic Capacity Verification**: Active Open=`0` | Resting Pending=`2` | Capacity Check: `N_open + N_pending <= 3` (**`PASS`**)
- **Triple Floor Solvency Check**: Current Equity=`4,744.32 USD` | Hard Floor=`4,775.00 USD` | Buffer=`-30.68 USD` | Solvency Check: **`DEFENSE_MODE`**
- **Stand-Aside Reason**: Absence of statistically validated auction edge and defending resting armor. Standing aside preserves statutory hard floor.