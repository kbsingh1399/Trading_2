# 🔬 MASTER 43-FEED QUANTITATIVE DOSSIER: NZDUSD (New Zealand Dollar / US Dollar)
**MT5 Symbol**: `NZDUSD.pi` | **Category**: `FX Major` | **Tier**: `Tier 3`
**Execution Posture**: `PASSIVE LIMIT ONLY` | **Timestamp**: 2026-10-29 14:43:14 UTC
**Pipeline Clearance**: `QUALIFIED` | **Data Freshness**: `1.2m`

---

## 1. MT5 Live Broker Telemetry & Spread Friction Gate
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet)*
- **Live Bid Quote**: `0.56100` | **Live Ask Quote**: `0.56103` | **Mid Price**: `0.56102`
- **Spread Points**: `3.0 pts` | **Spread BPS**: `0.53 bps` (Mandatory Cap: `5.0 bps`)
- **Gate Status**: **`PASS`** (Spread friction within mandatory threshold; safe for maker execution)
- **Order Allowed**: `BUY_LIMIT / SELL_LIMIT` | **Pillar 1 Clearance**: `QUALIFIED`
- **Broker Specifications**: Contract Size=`1.00` | Tick Value=`1.00 USD` | Min Lot=`0.01` | Digits=`5`
- **Account Capital Context**: Balance=`4,744.55 USD` | Equity=`4,744.32 USD` | Free Margin=`4,342.62 USD` | Inviolate Hard Floor=`4,775.00 USD` (Cushion: `-30.68 USD`)
- **Pipeline Health**: Feed #00 Status=`PASS` | Overall Pipeline Telemetry=`33/33 FEEDS PASS (SYNCHRONIZED)`

---

## 2. Technical Profile, Multi-Sigma VWAP Dispersion & Volatility
*(Sources: 11_Technical.parquet, 11_Technical_BTC_Ribbon.parquet)*
- **Last Verified Price**: `0.56152` | **24h Change**: `+0.03%` (24h High: `0.56384`, 24h Low: `0.56078`)
- **Weekly Range**: Week High=`0.57075` | Week Low=`0.55680` | Daily POC=`0.56185` | Daily VAH=`0.56229` | Daily VAL=`0.56116`
- **Session VWAP**: `0.56179` | **Rolling 24h VWAP**: `0.56206` | **Distance to VWAP**: `-0.05%`
- **VWAP Z-Score**: `-0.55 sigma` | **Mean Reversion Bias**: **`FAIR VALUE`**
- **VWAP Dispersion Bands**:
  * +1.00 sigma: `0.56228` | -1.00 sigma: `0.56130`
  * +1.28 sigma (80% CI): `0.56242` | -1.28 sigma: `0.56116`
  * +2.00 sigma (95% CI): `0.56277` | -2.00 sigma: `0.56081`
  * +2.01 sigma: `0.56277` | -2.01 sigma: `0.56080`
  * +2.51 sigma (98.8% CI): `0.56302` | -2.51 sigma: `0.56056`
  * +3.00 sigma (99.7% CI Extreme): `0.56326` | -3.00 sigma: `0.56032`
- **Oscillators & Volatility**:
  * **RSI (14)**: `50.22` | **RSI State**: **`NEUTRAL`**
  * **ATR (14)**: `0.00060` | **ATR %**: `0.11%`
  * **Bollinger Bands**: Upper=`0.56189` | Mid=`0.56136` | Lower=`0.56084` | Bandwidth=`0.19%`
  * **MACD**: Line=`-0.0001` | Signal=`-0.0001` | Hist=`+0.0000`
- **Exponential Moving Average Ribbon (EMA)**:
  * Short Horizon: EMA-5=`0.56141` | EMA-9=`0.56141` | EMA-13=`0.56142` | EMA-20=`0.56145`
  * Intermediate: EMA-34=`0.56156` | EMA-50=`0.56167` | EMA-89=`0.56197` | EMA-100=`0.56209`
  * Institutional: EMA-144=`0.56262` | EMA-200=`0.56374` (Slope: `-0.052%`) | EMA-233=`0.56430` (Slope: `-0.055%`)
  * **Trend Bias**: **`NEUTRAL / CHOP`**

---

## 3. Auction Market Structure & Value Profile
*(Sources: 20_Auction_Market_Structure.parquet)*
- **Daily Auction Value Area**:
  * High (VAH): `0.56229` | Point of Control (POC): `0.56185` | Low (VAL): `0.56116`
  * Distance to POC: `-0.14%` | Distance to VAH: `-0.22%` | Distance to VAL: `-0.02%`
  * **Value Area Position**: **`BELOW_VALUE (Imbalance)`** | **Auction Regime**: **`RANGE_EXPANSION`** | **Session Bias**: **`BEARISH (Below Pivot)`**
- **Prior Day & Weekly Auction Profile**:
  * Prior Day: PD VAH=`0.56300` | PD POC=`0.56136` | PD VAL=`0.56042` | PDH=`0.56849` | PDL=`0.55680` | PDC=`0.56253`
  * Monday Reference: Monday High=`0.57071` | Monday Low=`0.56696` | Monday Mid=`0.56883`
  * Weekly Value Area: Weekly VAH=`0.57070` | Weekly POC=`0.57005` | Weekly VAL=`0.56178`
  * Multi-Week Extremes: Current Week High (CWH)=`0.57075` | CWL=`0.55680` | Prior Week High (PWH)=`0.57101` | PWL=`0.56479`
  * Multi-Month Extremes: Current Month High (CMH)=`0.57101` | CML=`0.55653` | Prior Month High (PMH)=`0.59288` | PML=`0.56260`
- **Session Liquidity Extremes & Initial Balance**:
  * Asian Session: Range `[0.56173 - 0.56364]`
  * London Session: Range `[0.56078 - 0.56239]`
  * New York Session: Range `[0.56068 - 0.56211]`
  * Initial Balance (IB): IB High=`0.56216` | IB Low=`0.56156`
- **Fibonacci Golden Pocket & Optimal Trade Entry (OTE)**:
  * Swing Range: High=`0.56384` | Low=`0.56068` | Direction=`BEARISH_IMPULSE`
  * Golden Pocket [0.618 - 0.65]: `[0.56263 - 0.56273]`
  * Optimal Trade Entry (0.702): `0.56290` | Invalidation Level: `0.56316` | Status: **`SHALLOW_RETRACE`**
- **Classical & Weekly Pivots**:
  * Daily Classical: Pivot=`0.56261` | R1=`0.56841` | S1=`0.55672` | R2=`0.57430` | S2=`0.55092`
  * Weekly Classical: Weekly Pivot=`0.56840` | Weekly R1=`0.57202` | Weekly S1=`0.56580`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Orderflow
*(Sources: 18_CVD.parquet, 18_CVD_30D_5m.parquet, 18_CVD_30D_15m.parquet, 18_CVD_30D_1h.parquet, 18_CVD_30D_4h.parquet, 18_CVD_30D_ALL.parquet, 21_Tradfye_Orderflow.parquet)*
- **Interbank Spot Orderflow Mechanics**: Decentralized OTC market structure. CVD taker deltas do not apply to interbank spot flow. Tape volume governed by broker tick volume with live spread friction of `0.53 bps`.
- **Session Volume Structure**: Price operating at `BELOW_VALUE (Imbalance)` with Daily POC at `0.56185` (VAH: `0.56229` / VAL: `0.56116`).

---

## 5. Institutional Whale Armor & Resting Orderbook Depth
*(Sources: 10_Whale_Orders.parquet, 12_Hyperdash.parquet, 17_Orderbook.parquet, 4_Hyperliquid_Analysis.parquet)*
- **Interbank Institutional Tier-1 Depth**: Decentralized OTC spot liquidity. Resting whale limit walls from crypto venues do not apply.
- **Verified Broker Armor**: Live Bid `0.56100` / Live Ask `0.56103` with institutional spread of `0.53 bps`. Structural defense anchored at Asian Range `[0.56173 - 0.56364]` and London Range `[0.56078 - 0.56239]`.

---

## 6. Liquidation Max Pain, Heatmaps & Cascade Boundaries
*(Sources: 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 14_Hyperdash_Liq_Map.parquet, 14_Liquidation_Matrix.parquet, 15_Hyperdash_Stops_Map.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **TradFi Structural Liquidity Boundaries**: Centralized perp liquidation feeds do not apply to interbank OTC spot.
- **Stop-Run Cascades & Liquidity Pools**: Primary institutional stop pools reside beyond Classical Pivot extremes (S1: `0.55672` / S2: `0.55092` for long stops; R1: `0.56841` / R2: `0.57430` for short stops) and Asian session extremes `[0.56173 - 0.56364]`.

---

## 7. Derivatives Sentiment, Open Interest & Funding Dynamics
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet, 6_Funding_Fee_Settlement.parquet, 13_Hyperliquid.parquet)*
- **Interbank Financing & Carry Mechanics**: Instrument trades as an OTC spot / cash CFD with zero perpetual funding drag or basis settlement friction.
- **Monetary Policy Differential**: Overnight holding carry governed by central bank interest rate spreads and broker rollover swap schedules.

---

## 8. Microstructure Footprint, Tape Imbalances & Macro Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 16_Hyperdash_telegram_Intel.parquet, 19_News.parquet, 19_Calendar.parquet)*
- **Decentralized Spot Flow Profile**: Footprint bar metrics and crypto ETF flows not applicable to OTC spot interbank asset.
- **Institutional Tape Dynamics**: Multi-dealer foreign exchange volume driven by international trade settlements, sovereign reserve reallocation, and London/NY fixing windows.

---

## 9. TradFi & Interbank Market Mechanics
*(Applicable to Foreign Exchange Majors, Precious Metals, Global Equity Indices, and Commodities)*
- **Central Bank Monetary Policy & Rate Differential**:
  * Prevailing Policy Stance: `Reserve Bank of New Zealand Official Cash Rate (4.75%) Accelerated Easing vs Fed Funds`
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
  * `Mon Oct 26 All Day` [NZD - Low Impact]: Bank Holiday (Forecast: , Previous: )
  * `Tue Oct 27 5:45pm` [USD - Low Impact]: ADP Weekly Employment Change (Forecast: , Previous: 17.5K)
  * `Tue Oct 27 6:00pm` [USD - Low Impact]: Core Durable Goods Orders m/m (Forecast: 0.6%, Previous: 0.2%)
- **Real-Time Macro Catalysts & Headlines (19_News.parquet)**:
  * `1 hr 20 min ago` [Inflation & CPI]: Fed's Favorite Inflation Indicator Surges In September As Soaring Energy Costs Drags Americans' Savings Rate To 4-Year Lows (zerohedge.com)
  * `1 hr 50 min ago` [Labor & Employment]: US Unemployment Insurance Weekly Claims (dol.gov)
  * `1 hr 50 min ago` [General Market Intel]: US Personal Income and Outlays, September 2026 (bea.gov)

---

## 10. Algorithmic Trade Formulation & Sovereign Decision
- **Sovereign Gate Decision**: **`STANDBY_RADAR`**
- **Dynamic Capacity Verification**: Active Open=`0` | Resting Pending=`2` | Capacity Check: `N_open + N_pending <= 3` (**`PASS`**)
- **Triple Floor Solvency Check**: Current Equity=`4,744.32 USD` | Hard Floor=`4,775.00 USD` | Buffer=`-30.68 USD` | Solvency Check: **`DEFENSE_MODE`**
- **Autonomous Limit Order Formulation (If Admitted)**:
```json
{
  "ticket": "PENDING_DISPATCH",
  "direction": "SELL_LIMIT",
  "lots": 0.12,
  "entry": 0.5632,
  "sl": 0.56388,
  "tp": 0.5605,
  "risk_usd": 8.16,
  "rr": 3.97,
  "model": "MODEL_1_FADE",
  "thesis": "Daily VAH + 0.35 ATR sweep exhaustion with structural stop above Asian High and R1."
}
```
- **Stand-Aside Reason**: Previous resting order completed/cancelled; candidate retained on priority tactical radar.