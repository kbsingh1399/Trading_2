# 🔬 MASTER 43-FEED QUANTITATIVE DOSSIER: EURNZD (EUR/NZD)
**MT5 Symbol**: `EURNZD.pi` | **Category**: `Forex Cross` | **Tier**: `Tier 2`
**Execution Posture**: `PASSIVE LIMIT ONLY` | **Timestamp**: 2026-10-29 14:43:14 UTC
**Pipeline Clearance**: `QUALIFIED` | **Data Freshness**: `1.2m`

---

## 1. MT5 Live Broker Telemetry & Spread Friction Gate
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet)*
- **Live Bid Quote**: `1.98518` | **Live Ask Quote**: `1.98533` | **Mid Price**: `1.98525`
- **Spread Points**: `15.0 pts` | **Spread BPS**: `0.76 bps` (Mandatory Cap: `5.0 bps`)
- **Gate Status**: **`PASS`** (Spread friction within mandatory threshold; safe for maker execution)
- **Order Allowed**: `BUY_LIMIT / SELL_LIMIT` | **Pillar 1 Clearance**: `QUALIFIED`
- **Broker Specifications**: Contract Size=`1.00` | Tick Value=`1.00 USD` | Min Lot=`0.01` | Digits=`5`
- **Account Capital Context**: Balance=`4,744.55 USD` | Equity=`4,744.32 USD` | Free Margin=`4,342.62 USD` | Inviolate Hard Floor=`4,775.00 USD` (Cushion: `-30.68 USD`)
- **Pipeline Health**: Feed #00 Status=`PASS` | Overall Pipeline Telemetry=`33/33 FEEDS PASS (SYNCHRONIZED)`

---

## 2. Technical Profile, Multi-Sigma VWAP Dispersion & Volatility
*(Sources: 11_Technical.parquet, 11_Technical_BTC_Ribbon.parquet)*
- **Last Verified Price**: `1.98297` | **24h Change**: `+0.04%` (24h High: `1.98601`, 24h Low: `1.97868`)
- **Weekly Range**: Week High=`1.99151` | Week Low=`1.95404` | Daily POC=`1.98308` | Daily VAH=`1.98482` | Daily VAL=`1.98163`
- **Session VWAP**: `1.98281` | **Rolling 24h VWAP**: `1.98265` | **Distance to VWAP**: `+0.01%`
- **VWAP Z-Score**: `+0.12 sigma` | **Mean Reversion Bias**: **`FAIR VALUE`**
- **VWAP Dispersion Bands**:
  * +1.00 sigma: `1.98421` | -1.00 sigma: `1.98141`
  * +1.28 sigma (80% CI): `1.98460` | -1.28 sigma: `1.98102`
  * +2.00 sigma (95% CI): `1.98560` | -2.00 sigma: `1.98001`
  * +2.01 sigma: `1.98562` | -2.01 sigma: `1.98000`
  * +2.51 sigma (98.8% CI): `1.98632` | -2.51 sigma: `1.97930`
  * +3.00 sigma (99.7% CI Extreme): `1.98700` | -3.00 sigma: `1.97862`
- **Oscillators & Volatility**:
  * **RSI (14)**: `48.61` | **RSI State**: **`NEUTRAL`**
  * **ATR (14)**: `0.00153` | **ATR %**: `0.08%`
  * **Bollinger Bands**: Upper=`1.98668` | Mid=`1.98380` | Lower=`1.98091` | Bandwidth=`0.29%`
  * **MACD**: Line=`-0.0003` | Signal=`+0.0000` | Hist=`-0.0003`
- **Exponential Moving Average Ribbon (EMA)**:
  * Short Horizon: EMA-5=`1.98234` | EMA-9=`1.98275` | EMA-13=`1.98302` | EMA-20=`1.98323`
  * Intermediate: EMA-34=`1.98326` | EMA-50=`1.98312` | EMA-89=`1.98220` | EMA-100=`1.98184`
  * Institutional: EMA-144=`1.98025` | EMA-200=`1.97702` (Slope: `+0.041%`) | EMA-233=`1.97521` (Slope: `+0.044%`)
  * **Trend Bias**: **`NEUTRAL / CHOP`**

---

## 3. Auction Market Structure & Value Profile
*(Sources: 20_Auction_Market_Structure.parquet)*
- **Daily Auction Value Area**:
  * High (VAH): `1.98482` | Point of Control (POC): `1.98308` | Low (VAL): `1.98163`
  * Distance to POC: `+0.00%` | Distance to VAH: `+0.00%` | Distance to VAL: `+0.00%`
  * **Value Area Position**: **`INSIDE_VALUE (Balance)`** | **Auction Regime**: **`BALANCED_AUCTION`** | **Session Bias**: **`NEUTRAL`**
- **Prior Day & Weekly Auction Profile**:
  * Prior Day: PD VAH=`1.99320` | PD POC=`1.98525` | PD VAL=`1.97731` | PDH=`1.99717` | PDL=`1.97334` | PDC=`1.98525`
  * Monday Reference: Monday High=`1.99518` | Monday Low=`1.97533` | Monday Mid=`1.98525`
  * Weekly Value Area: Weekly VAH=`2.00114` | Weekly POC=`1.98525` | Weekly VAL=`1.96937`
  * Multi-Week Extremes: Current Week High (CWH)=`2.00511` | CWL=`1.96540` | Prior Week High (PWH)=`2.01503` | PWL=`1.95548`
  * Multi-Month Extremes: Current Month High (CMH)=`2.02496` | CML=`1.94555` | Prior Month High (PMH)=`2.03489` | PML=`1.93562`
- **Session Liquidity Extremes & Initial Balance**:
  * Asian Session: Range `[1.98128 - 1.98923]`
  * London Session: Range `[1.97731 - 1.99320]`
  * New York Session: Range `[1.97533 - 1.99518]`
  * Initial Balance (IB): IB High=`1.99121` | IB Low=`1.97930`
- **Fibonacci Golden Pocket & Optimal Trade Entry (OTE)**:
  * Swing Range: High=`1.98601` | Low=`1.97868` | Direction=`NONE`
  * Golden Pocket [0.618 - 0.65]: `[1.98128 - 1.98923]`
  * Optimal Trade Entry (0.702): `1.98525` | Invalidation Level: `0.00000` | Status: **`NONE`**
- **Classical & Weekly Pivots**:
  * Daily Classical: Pivot=`1.98525` | R1=`1.99121` | S1=`1.97930` | R2=`1.99717` | S2=`1.97334`
  * Weekly Classical: Weekly Pivot=`1.98525` | Weekly R1=`2.00511` | Weekly S1=`1.96540`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Orderflow
*(Sources: 18_CVD.parquet, 18_CVD_30D_5m.parquet, 18_CVD_30D_15m.parquet, 18_CVD_30D_1h.parquet, 18_CVD_30D_4h.parquet, 18_CVD_30D_ALL.parquet, 21_Tradfye_Orderflow.parquet)*
- **Interbank Spot Orderflow Mechanics**: Decentralized OTC market structure. CVD taker deltas do not apply to interbank spot flow. Tape volume governed by broker tick volume with live spread friction of `0.76 bps`.
- **Session Volume Structure**: Price operating at `INSIDE_VALUE (Balance)` with Daily POC at `1.98308` (VAH: `1.98482` / VAL: `1.98163`).

---

## 5. Institutional Whale Armor & Resting Orderbook Depth
*(Sources: 10_Whale_Orders.parquet, 12_Hyperdash.parquet, 17_Orderbook.parquet, 4_Hyperliquid_Analysis.parquet)*
- **Interbank Institutional Tier-1 Depth**: Decentralized OTC spot liquidity. Resting whale limit walls from crypto venues do not apply.
- **Verified Broker Armor**: Live Bid `1.98518` / Live Ask `1.98533` with institutional spread of `0.76 bps`. Structural defense anchored at Asian Range `[1.98128 - 1.98923]` and London Range `[1.97731 - 1.99320]`.

---

## 6. Liquidation Max Pain, Heatmaps & Cascade Boundaries
*(Sources: 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 14_Hyperdash_Liq_Map.parquet, 14_Liquidation_Matrix.parquet, 15_Hyperdash_Stops_Map.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **TradFi Structural Liquidity Boundaries**: Centralized perp liquidation feeds do not apply to interbank OTC spot.
- **Stop-Run Cascades & Liquidity Pools**: Primary institutional stop pools reside beyond Classical Pivot extremes (S1: `1.97930` / S2: `1.97334` for long stops; R1: `1.99121` / R2: `1.99717` for short stops) and Asian session extremes `[1.98128 - 1.98923]`.

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
  * `Mon Oct 26 All Day` [NZD - Low Impact]: Bank Holiday (Forecast: , Previous: )
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