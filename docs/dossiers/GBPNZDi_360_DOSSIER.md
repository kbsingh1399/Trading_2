# 🔬 MASTER 43-FEED QUANTITATIVE DOSSIER: GBPNZD (GBP/NZD)
**MT5 Symbol**: `GBPNZD.pi` | **Category**: `Forex Cross` | **Tier**: `Tier 2`
**Execution Posture**: `PASSIVE LIMIT ONLY` | **Timestamp**: 2026-10-29 14:43:14 UTC
**Pipeline Clearance**: `QUALIFIED` | **Data Freshness**: `1.2m`

---

## 1. MT5 Live Broker Telemetry & Spread Friction Gate
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet)*
- **Live Bid Quote**: `2.37609` | **Live Ask Quote**: `2.37618` | **Mid Price**: `2.37614`
- **Spread Points**: `9.0 pts` | **Spread BPS**: `0.38 bps` (Mandatory Cap: `5.0 bps`)
- **Gate Status**: **`PASS`** (Spread friction within mandatory threshold; safe for maker execution)
- **Order Allowed**: `BUY_LIMIT / SELL_LIMIT` | **Pillar 1 Clearance**: `QUALIFIED`
- **Broker Specifications**: Contract Size=`1.00` | Tick Value=`1.00 USD` | Min Lot=`0.01` | Digits=`5`
- **Account Capital Context**: Balance=`4,744.55 USD` | Equity=`4,744.32 USD` | Free Margin=`4,342.62 USD` | Inviolate Hard Floor=`4,775.00 USD` (Cushion: `-30.68 USD`)
- **Pipeline Health**: Feed #00 Status=`PASS` | Overall Pipeline Telemetry=`33/33 FEEDS PASS (SYNCHRONIZED)`

---

## 2. Technical Profile, Multi-Sigma VWAP Dispersion & Volatility
*(Sources: 11_Technical.parquet, 11_Technical_BTC_Ribbon.parquet)*
- **Last Verified Price**: `2.37277` | **24h Change**: `+0.25%` (24h High: `2.37502`, 24h Low: `2.36352`)
- **Weekly Range**: Week High=`2.38142` | Week Low=`2.33558` | Daily POC=`2.37025` | Daily VAH=`2.37330` | Daily VAL=`2.36877`
- **Session VWAP**: `2.37069` | **Rolling 24h VWAP**: `2.36946` | **Distance to VWAP**: `+0.09%`
- **VWAP Z-Score**: `+1.05 sigma` | **Mean Reversion Bias**: **`FAIR VALUE`**
- **VWAP Dispersion Bands**:
  * +1.00 sigma: `2.37267` | -1.00 sigma: `2.36871`
  * +1.28 sigma (80% CI): `2.37322` | -1.28 sigma: `2.36815`
  * +2.00 sigma (95% CI): `2.37465` | -2.00 sigma: `2.36673`
  * +2.01 sigma: `2.37467` | -2.01 sigma: `2.36671`
  * +2.51 sigma (98.8% CI): `2.37566` | -2.51 sigma: `2.36572`
  * +3.00 sigma (99.7% CI Extreme): `2.37663` | -3.00 sigma: `2.36475`
- **Oscillators & Volatility**:
  * **RSI (14)**: `53.03` | **RSI State**: **`NEUTRAL`**
  * **ATR (14)**: `0.00183` | **ATR %**: `0.08%`
  * **Bollinger Bands**: Upper=`2.37515` | Mid=`2.37245` | Lower=`2.36975` | Bandwidth=`0.23%`
  * **MACD**: Line=`+0.0005` | Signal=`+0.0007` | Hist=`-0.0001`
- **Exponential Moving Average Ribbon (EMA)**:
  * Short Horizon: EMA-5=`2.37257` | EMA-9=`2.37257` | EMA-13=`2.37249` | EMA-20=`2.37224`
  * Intermediate: EMA-34=`2.37167` | EMA-50=`2.37107` | EMA-89=`2.36939` | EMA-100=`2.36885`
  * Institutional: EMA-144=`2.36659` | EMA-200=`2.36244` (Slope: `+0.055%`) | EMA-233=`2.36021` (Slope: `+0.057%`)
  * **Trend Bias**: **`STRONG BULLISH`**

---

## 3. Auction Market Structure & Value Profile
*(Sources: 20_Auction_Market_Structure.parquet)*
- **Daily Auction Value Area**:
  * High (VAH): `2.37330` | Point of Control (POC): `2.37025` | Low (VAL): `2.36877`
  * Distance to POC: `+0.00%` | Distance to VAH: `+0.00%` | Distance to VAL: `+0.00%`
  * **Value Area Position**: **`INSIDE_VALUE (Balance)`** | **Auction Regime**: **`BALANCED_AUCTION`** | **Session Bias**: **`NEUTRAL`**
- **Prior Day & Weekly Auction Profile**:
  * Prior Day: PD VAH=`2.38564` | PD POC=`2.37614` | PD VAL=`2.36663` | PDH=`2.39039` | PDL=`2.36188` | PDC=`2.37614`
  * Monday Reference: Monday High=`2.38802` | Monday Low=`2.36425` | Monday Mid=`2.37614`
  * Weekly Value Area: Weekly VAH=`2.39514` | Weekly POC=`2.37614` | Weekly VAL=`2.35713`
  * Multi-Week Extremes: Current Week High (CWH)=`2.39990` | CWL=`2.35237` | Prior Week High (PWH)=`2.41178` | PWL=`2.34049`
  * Multi-Month Extremes: Current Month High (CMH)=`2.42366` | CML=`2.32861` | Prior Month High (PMH)=`2.43554` | PML=`2.31673`
- **Session Liquidity Extremes & Initial Balance**:
  * Asian Session: Range `[2.37138 - 2.38089]`
  * London Session: Range `[2.36663 - 2.38564]`
  * New York Session: Range `[2.36425 - 2.38802]`
  * Initial Balance (IB): IB High=`2.38326` | IB Low=`2.36901`
- **Fibonacci Golden Pocket & Optimal Trade Entry (OTE)**:
  * Swing Range: High=`2.37502` | Low=`2.36352` | Direction=`NONE`
  * Golden Pocket [0.618 - 0.65]: `[2.37138 - 2.38089]`
  * Optimal Trade Entry (0.702): `2.37614` | Invalidation Level: `0.00000` | Status: **`NONE`**
- **Classical & Weekly Pivots**:
  * Daily Classical: Pivot=`2.37614` | R1=`2.38326` | S1=`2.36901` | R2=`2.39039` | S2=`2.36188`
  * Weekly Classical: Weekly Pivot=`2.37614` | Weekly R1=`2.39990` | Weekly S1=`2.35237`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Orderflow
*(Sources: 18_CVD.parquet, 18_CVD_30D_5m.parquet, 18_CVD_30D_15m.parquet, 18_CVD_30D_1h.parquet, 18_CVD_30D_4h.parquet, 18_CVD_30D_ALL.parquet, 21_Tradfye_Orderflow.parquet)*
- **Interbank Spot Orderflow Mechanics**: Decentralized OTC market structure. CVD taker deltas do not apply to interbank spot flow. Tape volume governed by broker tick volume with live spread friction of `0.38 bps`.
- **Session Volume Structure**: Price operating at `INSIDE_VALUE (Balance)` with Daily POC at `2.37025` (VAH: `2.37330` / VAL: `2.36877`).

---

## 5. Institutional Whale Armor & Resting Orderbook Depth
*(Sources: 10_Whale_Orders.parquet, 12_Hyperdash.parquet, 17_Orderbook.parquet, 4_Hyperliquid_Analysis.parquet)*
- **Interbank Institutional Tier-1 Depth**: Decentralized OTC spot liquidity. Resting whale limit walls from crypto venues do not apply.
- **Verified Broker Armor**: Live Bid `2.37609` / Live Ask `2.37618` with institutional spread of `0.38 bps`. Structural defense anchored at Asian Range `[2.37138 - 2.38089]` and London Range `[2.36663 - 2.38564]`.

---

## 6. Liquidation Max Pain, Heatmaps & Cascade Boundaries
*(Sources: 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 14_Hyperdash_Liq_Map.parquet, 14_Liquidation_Matrix.parquet, 15_Hyperdash_Stops_Map.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **TradFi Structural Liquidity Boundaries**: Centralized perp liquidation feeds do not apply to interbank OTC spot.
- **Stop-Run Cascades & Liquidity Pools**: Primary institutional stop pools reside beyond Classical Pivot extremes (S1: `2.36901` / S2: `2.36188` for long stops; R1: `2.38326` / R2: `2.39039` for short stops) and Asian session extremes `[2.37138 - 2.38089]`.

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
  * `Mon Oct 26 All Day` [NZD - Low Impact]: Bank Holiday (Forecast: , Previous: )
  * `Mon Oct 26 4:30pm` [GBP - Low Impact]: CBI Realized Sales (Forecast: -47, Previous: -55)
- **Real-Time Macro Catalysts & Headlines (19_News.parquet)**:
  * `4 hr ago` [General Market Intel]: UK Money and Credit - September 2026 (bankofengland.co.uk)
  * `14 hr ago` [General Market Intel]: ANZ New Zealand Business Outlook: Resilient (anz.co.nz)

---

## 10. Algorithmic Trade Formulation & Sovereign Decision
- **Sovereign Gate Decision**: **`FAIL_CLOSED_STAND_ASIDE`**
- **Dynamic Capacity Verification**: Active Open=`0` | Resting Pending=`2` | Capacity Check: `N_open + N_pending <= 3` (**`PASS`**)
- **Triple Floor Solvency Check**: Current Equity=`4,744.32 USD` | Hard Floor=`4,775.00 USD` | Buffer=`-30.68 USD` | Solvency Check: **`DEFENSE_MODE`**
- **Stand-Aside Reason**: Absence of statistically validated auction edge and defending resting armor. Standing aside preserves statutory hard floor.