# 🔬 MASTER 43-FEED QUANTITATIVE DOSSIER: UK100 (FTSE 100 Index)
**MT5 Symbol**: `UK100.p` | **Category**: `Equity Index` | **Tier**: `Tier 1`
**Execution Posture**: `PASSIVE LIMIT ONLY` | **Timestamp**: 2026-10-29 14:43:14 UTC
**Pipeline Clearance**: `QUALIFIED` | **Data Freshness**: `1.2m`

---

## 1. MT5 Live Broker Telemetry & Spread Friction Gate
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet)*
- **Live Bid Quote**: `10733.51000` | **Live Ask Quote**: `10735.21000` | **Mid Price**: `10734.36000`
- **Spread Points**: `170.0 pts` | **Spread BPS**: `1.58 bps` (Mandatory Cap: `5.0 bps`)
- **Gate Status**: **`PASS`** (Spread friction within mandatory threshold; safe for maker execution)
- **Order Allowed**: `BUY_LIMIT / SELL_LIMIT` | **Pillar 1 Clearance**: `QUALIFIED`
- **Broker Specifications**: Contract Size=`1.00` | Tick Value=`1.00 USD` | Min Lot=`0.01` | Digits=`5`
- **Account Capital Context**: Balance=`4,744.55 USD` | Equity=`4,744.32 USD` | Free Margin=`4,342.62 USD` | Inviolate Hard Floor=`4,775.00 USD` (Cushion: `-30.68 USD`)
- **Pipeline Health**: Feed #00 Status=`PASS` | Overall Pipeline Telemetry=`33/33 FEEDS PASS (SYNCHRONIZED)`

---

## 2. Technical Profile, Multi-Sigma VWAP Dispersion & Volatility
*(Sources: 11_Technical.parquet, 11_Technical_BTC_Ribbon.parquet)*
- **Last Verified Price**: `10753.30000` | **24h Change**: `+0.47%` (24h High: `10774.11000`, 24h Low: `10667.38000`)
- **Weekly Range**: Week High=`10774.11000` | Week Low=`10638.36000` | Daily POC=`10732.16000` | Daily VAH=`10753.61000` | Daily VAL=`10706.92000`
- **Session VWAP**: `10736.10463` | **Rolling 24h VWAP**: `10715.28996` | **Distance to VWAP**: `+0.16%`
- **VWAP Z-Score**: `+0.95 sigma` | **Mean Reversion Bias**: **`FAIR VALUE`**
- **VWAP Dispersion Bands**:
  * +1.00 sigma: `10754.20259` | -1.00 sigma: `10718.00666`
  * +1.28 sigma (80% CI): `10759.27002` | -1.28 sigma: `10712.93923`
  * +2.00 sigma (95% CI): `10772.30055` | -2.00 sigma: `10699.90870`
  * +2.01 sigma: `10772.48153` | -2.01 sigma: `10699.72772`
  * +2.51 sigma (98.8% CI): `10781.53052` | -2.51 sigma: `10690.67874`
  * +3.00 sigma (99.7% CI Extreme): `10790.39852` | -3.00 sigma: `10681.81074`
- **Oscillators & Volatility**:
  * **RSI (14)**: `57.52` | **RSI State**: **`BULLISH`**
  * **ATR (14)**: `15.63071` | **ATR %**: `0.15%`
  * **Bollinger Bands**: Upper=`10768.45022` | Mid=`10740.17850` | Lower=`10711.90678` | Bandwidth=`0.53%`
  * **MACD**: Line=`+9.7634` | Signal=`+8.3065` | Hist=`+1.4569`
- **Exponential Moving Average Ribbon (EMA)**:
  * Short Horizon: EMA-5=`10755.50449` | EMA-9=`10751.94145` | EMA-13=`10748.32942` | EMA-20=`10743.11545`
  * Intermediate: EMA-34=`10735.17975` | EMA-50=`10728.12973` | EMA-89=`10716.18093` | EMA-100=`10714.02648`
  * Institutional: EMA-144=`10709.58764` | EMA-200=`10710.08646` (Slope: `+0.045%`) | EMA-233=`10709.42433` (Slope: `+0.039%`)
  * **Trend Bias**: **`STRONG BULLISH`**

---

## 3. Auction Market Structure & Value Profile
*(Sources: 20_Auction_Market_Structure.parquet)*
- **Daily Auction Value Area**:
  * High (VAH): `10753.61000` | Point of Control (POC): `10732.16000` | Low (VAL): `10706.92000`
  * Distance to POC: `+0.02%` | Distance to VAH: `-0.18%` | Distance to VAL: `+0.25%`
  * **Value Area Position**: **`INSIDE_VALUE (Balance)`** | **Auction Regime**: **`ROTATIONAL_BALANCE`** | **Session Bias**: **`BULLISH (Above Pivot)`**
- **Prior Day & Weekly Auction Profile**:
  * Prior Day: PD VAH=`10709.92000` | PD POC=`10691.51000` | PD VAL=`10661.82000` | PDH=`10727.44000` | PDL=`10638.36000` | PDC=`10692.44000`
  * Monday Reference: Monday High=`10772.44000` | Monday Low=`10677.38000` | Monday Mid=`10724.91000`
  * Weekly Value Area: Weekly VAH=`10734.74000` | Weekly POC=`10677.73000` | Weekly VAL=`10645.15000`
  * Multi-Week Extremes: Current Week High (CWH)=`10774.11000` | CWL=`10638.36000` | Prior Week High (PWH)=`10880.78000` | PWL=`10621.43000`
  * Multi-Month Extremes: Current Month High (CMH)=`10886.69000` | CML=`10359.16000` | Prior Month High (PMH)=`10867.16000` | PML=`10534.61000`
- **Session Liquidity Extremes & Initial Balance**:
  * Asian Session: Range `[10679.48000 - 10724.67000]`
  * London Session: Range `[10698.84000 - 10769.43000]`
  * New York Session: Range `[10714.37000 - 10774.11000]`
  * Initial Balance (IB): IB High=`10722.87000` | IB Low=`10706.79000`
- **Fibonacci Golden Pocket & Optimal Trade Entry (OTE)**:
  * Swing Range: High=`10774.11000` | Low=`10667.38000` | Direction=`BULLISH_IMPULSE`
  * Golden Pocket [0.618 - 0.65]: `[10704.74000 - 10708.15000]`
  * Optimal Trade Entry (0.702): `10699.19000` | Invalidation Level: `10690.22000` | Status: **`SHALLOW_RETRACE`**
- **Classical & Weekly Pivots**:
  * Daily Classical: Pivot=`10686.08000` | R1=`10733.80000` | S1=`10644.72000` | R2=`10775.16000` | S2=`10597.00000`
  * Weekly Classical: Weekly Pivot=`10732.35000` | Weekly R1=`10843.27000` | Weekly S1=`10583.92000`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Orderflow
*(Sources: 18_CVD.parquet, 18_CVD_30D_5m.parquet, 18_CVD_30D_15m.parquet, 18_CVD_30D_1h.parquet, 18_CVD_30D_4h.parquet, 18_CVD_30D_ALL.parquet, 21_Tradfye_Orderflow.parquet)*
- **Interbank Spot Orderflow Mechanics**: Decentralized OTC market structure. CVD taker deltas do not apply to interbank spot flow. Tape volume governed by broker tick volume with live spread friction of `1.58 bps`.
- **Session Volume Structure**: Price operating at `INSIDE_VALUE (Balance)` with Daily POC at `10732.16000` (VAH: `10753.61000` / VAL: `10706.92000`).

---

## 5. Institutional Whale Armor & Resting Orderbook Depth
*(Sources: 10_Whale_Orders.parquet, 12_Hyperdash.parquet, 17_Orderbook.parquet, 4_Hyperliquid_Analysis.parquet)*
- **Interbank Institutional Tier-1 Depth**: Decentralized OTC spot liquidity. Resting whale limit walls from crypto venues do not apply.
- **Verified Broker Armor**: Live Bid `10733.51000` / Live Ask `10735.21000` with institutional spread of `1.58 bps`. Structural defense anchored at Asian Range `[10679.48000 - 10724.67000]` and London Range `[10698.84000 - 10769.43000]`.

---

## 6. Liquidation Max Pain, Heatmaps & Cascade Boundaries
*(Sources: 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 14_Hyperdash_Liq_Map.parquet, 14_Liquidation_Matrix.parquet, 15_Hyperdash_Stops_Map.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **TradFi Structural Liquidity Boundaries**: Centralized perp liquidation feeds do not apply to interbank OTC spot.
- **Stop-Run Cascades & Liquidity Pools**: Primary institutional stop pools reside beyond Classical Pivot extremes (S1: `10644.72000` / S2: `10597.00000` for long stops; R1: `10733.80000` / R2: `10775.16000` for short stops) and Asian session extremes `[10679.48000 - 10724.67000]`.

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
- **Upcoming High-Impact Economic Calendar Events (19_Calendar.parquet)**:
  * `Tue Oct 27 5:45pm` [USD - Low Impact]: ADP Weekly Employment Change (Forecast: , Previous: 17.5K)
  * `Tue Oct 27 6:00pm` [USD - Low Impact]: Core Durable Goods Orders m/m (Forecast: 0.6%, Previous: 0.2%)
  * `Tue Oct 27 6:00pm` [USD - Low Impact]: Durable Goods Orders m/m (Forecast: 2.0%, Previous: -0.1%)
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