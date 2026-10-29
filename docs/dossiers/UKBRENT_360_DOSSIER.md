# 🔬 MASTER 43-FEED QUANTITATIVE DOSSIER: UKBRENT (Brent Crude Oil)
**MT5 Symbol**: `UKBRENT.p` | **Category**: `Energy Commodity` | **Tier**: `Tier 2`
**Execution Posture**: `PASSIVE LIMIT ONLY` | **Timestamp**: 2026-10-29 14:43:14 UTC
**Pipeline Clearance**: `QUALIFIED` | **Data Freshness**: `1.2m`

---

## 1. MT5 Live Broker Telemetry & Spread Friction Gate
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet)*
- **Live Bid Quote**: `115.18600` | **Live Ask Quote**: `115.22600` | **Mid Price**: `115.20600`
- **Spread Points**: `40.0 pts` | **Spread BPS**: `3.47 bps` (Mandatory Cap: `5.0 bps`)
- **Gate Status**: **`PASS`** (Spread friction within mandatory threshold; safe for maker execution)
- **Order Allowed**: `BUY_LIMIT / SELL_LIMIT` | **Pillar 1 Clearance**: `QUALIFIED`
- **Broker Specifications**: Contract Size=`1.00` | Tick Value=`1.00 USD` | Min Lot=`0.01` | Digits=`5`
- **Account Capital Context**: Balance=`4,744.55 USD` | Equity=`4,744.32 USD` | Free Margin=`4,342.62 USD` | Inviolate Hard Floor=`4,775.00 USD` (Cushion: `-30.68 USD`)
- **Pipeline Health**: Feed #00 Status=`PASS` | Overall Pipeline Telemetry=`33/33 FEEDS PASS (SYNCHRONIZED)`

---

## 2. Technical Profile, Multi-Sigma VWAP Dispersion & Volatility
*(Sources: 11_Technical.parquet, 11_Technical_BTC_Ribbon.parquet)*
- **Last Verified Price**: `114.54200` | **24h Change**: `-1.43%` (24h High: `117.46600`, 24h Low: `113.71000`)
- **Weekly Range**: Week High=`117.62500` | Week Low=`113.71000` | Daily POC=`115.19600` | Daily VAH=`115.51400` | Daily VAL=`114.74700`
- **Session VWAP**: `114.97165` | **Rolling 24h VWAP**: `115.59715` | **Distance to VWAP**: `-0.37%`
- **VWAP Z-Score**: `-1.13 sigma` | **Mean Reversion Bias**: **`FAIR VALUE`**
- **VWAP Dispersion Bands**:
  * +1.00 sigma: `115.35078` | -1.00 sigma: `114.59251`
  * +1.28 sigma (80% CI): `115.45694` | -1.28 sigma: `114.48635`
  * +2.00 sigma (95% CI): `115.72992` | -2.00 sigma: `114.21337`
  * +2.01 sigma: `115.73371` | -2.01 sigma: `114.20958`
  * +2.51 sigma (98.8% CI): `115.92328` | -2.51 sigma: `114.02001`
  * +3.00 sigma (99.7% CI Extreme): `116.10906` | -3.00 sigma: `113.83423`
- **Oscillators & Volatility**:
  * **RSI (14)**: `43.60` | **RSI State**: **`BEARISH`**
  * **ATR (14)**: `0.43491` | **ATR %**: `0.38%`
  * **Bollinger Bands**: Upper=`115.60588` | Mid=`114.89805` | Lower=`114.19022` | Bandwidth=`1.23%`
  * **MACD**: Line=`-0.1752` | Signal=`-0.0924` | Hist=`-0.0829`
- **Exponential Moving Average Ribbon (EMA)**:
  * Short Horizon: EMA-5=`114.47939` | EMA-9=`114.63719` | EMA-13=`114.73224` | EMA-20=`114.82992`
  * Intermediate: EMA-34=`114.95509` | EMA-50=`115.07679` | EMA-89=`115.27379` | EMA-100=`115.30746`
  * Institutional: EMA-144=`115.38560` | EMA-200=`115.39779` (Slope: `-0.064%`) | EMA-233=`115.33584` (Slope: `-0.048%`)
  * **Trend Bias**: **`STRONG BEARISH`**

---

## 3. Auction Market Structure & Value Profile
*(Sources: 20_Auction_Market_Structure.parquet)*
- **Daily Auction Value Area**:
  * High (VAH): `115.51400` | Point of Control (POC): `115.19600` | Low (VAL): `114.74700`
  * Distance to POC: `-0.02%` | Distance to VAH: `-0.30%` | Distance to VAL: `+0.37%`
  * **Value Area Position**: **`INSIDE_VALUE (Balance)`** | **Auction Regime**: **`ROTATIONAL_BALANCE`** | **Session Bias**: **`BEARISH (Below Pivot)`**
- **Prior Day & Weekly Auction Profile**:
  * Prior Day: PD VAH=`116.72000` | PD POC=`116.16400` | PD VAL=`115.60700` | PDH=`117.46600` | PDL=`114.48400` | PDC=`115.37800`
  * Monday Reference: Monday High=`117.62500` | Monday Low=`114.21000` | Monday Mid=`115.91700`
  * Weekly Value Area: Weekly VAH=`116.04600` | Weekly POC=`115.18500` | Weekly VAL=`114.45400`
  * Multi-Week Extremes: Current Week High (CWH)=`117.62500` | CWL=`113.71000` | Prior Week High (PWH)=`118.22600` | PWL=`107.38700`
  * Multi-Month Extremes: Current Month High (CMH)=`118.22600` | CML=`101.43000` | Prior Month High (PMH)=`110.42000` | PML=`92.11300`
- **Session Liquidity Extremes & Initial Balance**:
  * Asian Session: Range `[114.80800 - 115.69200]`
  * London Session: Range `[114.23600 - 115.67100]`
  * New York Session: Range `[113.71000 - 115.42600]`
  * Initial Balance (IB): IB High=`114.94700` | IB Low=`114.43700`
- **Fibonacci Golden Pocket & Optimal Trade Entry (OTE)**:
  * Swing Range: High=`117.46600` | Low=`113.71000` | Direction=`BEARISH_IMPULSE`
  * Golden Pocket [0.618 - 0.65]: `[116.03100 - 116.15100]`
  * Optimal Trade Entry (0.702): `116.34700` | Invalidation Level: `116.66200` | Status: **`SHALLOW_RETRACE`**
- **Classical & Weekly Pivots**:
  * Daily Classical: Pivot=`115.77600` | R1=`117.06800` | S1=`114.08600` | R2=`118.75800` | S2=`112.79400`
  * Weekly Classical: Weekly Pivot=`114.44600` | Weekly R1=`121.50500` | Weekly S1=`110.66600`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Orderflow
*(Sources: 18_CVD.parquet, 18_CVD_30D_5m.parquet, 18_CVD_30D_15m.parquet, 18_CVD_30D_1h.parquet, 18_CVD_30D_4h.parquet, 18_CVD_30D_ALL.parquet, 21_Tradfye_Orderflow.parquet)*
- **Interbank Spot Orderflow Mechanics**: Decentralized OTC market structure. CVD taker deltas do not apply to interbank spot flow. Tape volume governed by broker tick volume with live spread friction of `3.47 bps`.
- **Session Volume Structure**: Price operating at `INSIDE_VALUE (Balance)` with Daily POC at `115.19600` (VAH: `115.51400` / VAL: `114.74700`).

---

## 5. Institutional Whale Armor & Resting Orderbook Depth
*(Sources: 10_Whale_Orders.parquet, 12_Hyperdash.parquet, 17_Orderbook.parquet, 4_Hyperliquid_Analysis.parquet)*
- **Interbank Institutional Tier-1 Depth**: Decentralized OTC spot liquidity. Resting whale limit walls from crypto venues do not apply.
- **Verified Broker Armor**: Live Bid `115.18600` / Live Ask `115.22600` with institutional spread of `3.47 bps`. Structural defense anchored at Asian Range `[114.80800 - 115.69200]` and London Range `[114.23600 - 115.67100]`.

---

## 6. Liquidation Max Pain, Heatmaps & Cascade Boundaries
*(Sources: 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 14_Hyperdash_Liq_Map.parquet, 14_Liquidation_Matrix.parquet, 15_Hyperdash_Stops_Map.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **TradFi Structural Liquidity Boundaries**: Centralized perp liquidation feeds do not apply to interbank OTC spot.
- **Stop-Run Cascades & Liquidity Pools**: Primary institutional stop pools reside beyond Classical Pivot extremes (S1: `114.08600` / S2: `112.79400` for long stops; R1: `117.06800` / R2: `118.75800` for short stops) and Asian session extremes `[114.80800 - 115.69200]`.

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
  * Mid-Tier CEX Rates: KuCoin=`+0.0000%` | MEXC=`-0.0036%` | Gate=`+0.0000%` | BingX=`+0.0000%` | Bitunix=`+0.0000%`
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