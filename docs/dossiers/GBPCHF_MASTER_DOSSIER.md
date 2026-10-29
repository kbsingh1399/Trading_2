# 🔬 MASTER 43-FEED QUANTITATIVE DOSSIER: GBPCHF (GBP/CHF)
**MT5 Symbol**: `GBPCHF.pi` | **Category**: `Forex Cross` | **Tier**: `Tier 2`
**Execution Posture**: `PASSIVE LIMIT ONLY` | **Timestamp**: 2026-10-29 14:43:14 UTC
**Pipeline Clearance**: `QUALIFIED` | **Data Freshness**: `1.2m`

---

## 1. MT5 Live Broker Telemetry & Spread Friction Gate
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet)*
- **Live Bid Quote**: `1.10406` | **Live Ask Quote**: `1.10416` | **Mid Price**: `1.10411`
- **Spread Points**: `10.0 pts` | **Spread BPS**: `0.91 bps` (Mandatory Cap: `5.0 bps`)
- **Gate Status**: **`PASS`** (Spread friction within mandatory threshold; safe for maker execution)
- **Order Allowed**: `BUY_LIMIT / SELL_LIMIT` | **Pillar 1 Clearance**: `QUALIFIED`
- **Broker Specifications**: Contract Size=`1.00` | Tick Value=`1.00 USD` | Min Lot=`0.01` | Digits=`5`
- **Account Capital Context**: Balance=`4,744.55 USD` | Equity=`4,744.32 USD` | Free Margin=`4,342.62 USD` | Inviolate Hard Floor=`4,775.00 USD` (Cushion: `-30.68 USD`)
- **Pipeline Health**: Feed #00 Status=`PASS` | Overall Pipeline Telemetry=`33/33 FEEDS PASS (SYNCHRONIZED)`

---

## 2. Technical Profile, Multi-Sigma VWAP Dispersion & Volatility
*(Sources: 11_Technical.parquet, 11_Technical_BTC_Ribbon.parquet)*
- **Last Verified Price**: `1.10345` | **24h Change**: `-0.02%` (24h High: `1.10474`, 24h Low: `1.10161`)
- **Weekly Range**: Week High=`1.10482` | Week Low=`1.10154` | Daily POC=`1.10358` | Daily VAH=`1.10386` | Daily VAL=`1.10300`
- **Session VWAP**: `1.10329` | **Rolling 24h VWAP**: `1.10348` | **Distance to VWAP**: `+0.01%`
- **VWAP Z-Score**: `+0.32 sigma` | **Mean Reversion Bias**: **`FAIR VALUE`**
- **VWAP Dispersion Bands**:
  * +1.00 sigma: `1.10379` | -1.00 sigma: `1.10279`
  * +1.28 sigma (80% CI): `1.10393` | -1.28 sigma: `1.10265`
  * +2.00 sigma (95% CI): `1.10429` | -2.00 sigma: `1.10229`
  * +2.01 sigma: `1.10430` | -2.01 sigma: `1.10228`
  * +2.51 sigma (98.8% CI): `1.10455` | -2.51 sigma: `1.10203`
  * +3.00 sigma (99.7% CI Extreme): `1.10480` | -3.00 sigma: `1.10178`
- **Oscillators & Volatility**:
  * **RSI (14)**: `50.69` | **RSI State**: **`NEUTRAL`**
  * **ATR (14)**: `0.00059` | **ATR %**: `0.05%`
  * **Bollinger Bands**: Upper=`1.10446` | Mid=`1.10337` | Lower=`1.10228` | Bandwidth=`0.20%`
  * **MACD**: Line=`+0.0001` | Signal=`+0.0001` | Hist=`+0.0000`
- **Exponential Moving Average Ribbon (EMA)**:
  * Short Horizon: EMA-5=`1.10356` | EMA-9=`1.10357` | EMA-13=`1.10353` | EMA-20=`1.10346`
  * Intermediate: EMA-34=`1.10339` | EMA-50=`1.10336` | EMA-89=`1.10335` | EMA-100=`1.10336`
  * Institutional: EMA-144=`1.10338` | EMA-200=`1.10343` (Slope: `+0.002%`) | EMA-233=`1.10342` (Slope: `+0.002%`)
  * **Trend Bias**: **`NEUTRAL / CHOP`**

---

## 3. Auction Market Structure & Value Profile
*(Sources: 20_Auction_Market_Structure.parquet)*
- **Daily Auction Value Area**:
  * High (VAH): `1.10386` | Point of Control (POC): `1.10358` | Low (VAL): `1.10300`
  * Distance to POC: `+0.05%` | Distance to VAH: `+0.02%` | Distance to VAL: `+0.10%`
  * **Value Area Position**: **`ABOVE_VALUE (Imbalance)`** | **Auction Regime**: **`RANGE_EXPANSION`** | **Session Bias**: **`BULLISH (Above Pivot)`**
- **Prior Day & Weekly Auction Profile**:
  * Prior Day: PD VAH=`1.10411` | PD POC=`1.10377` | PD VAL=`1.10307` | PDH=`1.10474` | PDL=`1.10154` | PDC=`1.10322`
  * Monday Reference: Monday High=`1.10482` | Monday Low=`1.10040` | Monday Mid=`1.10261`
  * Weekly Value Area: Weekly VAH=`1.10430` | Weekly POC=`1.10369` | Weekly VAL=`1.10277`
  * Multi-Week Extremes: Current Week High (CWH)=`1.10482` | CWL=`1.10040` | Prior Week High (PWH)=`1.10634` | PWL=`1.09621`
  * Multi-Month Extremes: Current Month High (CMH)=`1.11044` | CML=`1.08894` | Prior Month High (PMH)=`1.10966` | PML=`1.08933`
- **Session Liquidity Extremes & Initial Balance**:
  * Asian Session: Range `[1.10213 - 1.10402]`
  * London Session: Range `[1.10161 - 1.10419]`
  * New York Session: Range `[1.10276 - 1.10444]`
  * Initial Balance (IB): IB High=`1.10409` | IB Low=`1.10354`
- **Fibonacci Golden Pocket & Optimal Trade Entry (OTE)**:
  * Swing Range: High=`1.10474` | Low=`1.10161` | Direction=`BEARISH_IMPULSE`
  * Golden Pocket [0.618 - 0.65]: `[1.10354 - 1.10364]`
  * Optimal Trade Entry (0.702): `1.10381` | Invalidation Level: `1.10407` | Status: **`STRUCTURE_INVALIDATED`**
- **Classical & Weekly Pivots**:
  * Daily Classical: Pivot=`1.10317` | R1=`1.10479` | S1=`1.10159` | R2=`1.10637` | S2=`1.09997`
  * Weekly Classical: Weekly Pivot=`1.10164` | Weekly R1=`1.10707` | Weekly S1=`1.09694`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Orderflow
*(Sources: 18_CVD.parquet, 18_CVD_30D_5m.parquet, 18_CVD_30D_15m.parquet, 18_CVD_30D_1h.parquet, 18_CVD_30D_4h.parquet, 18_CVD_30D_ALL.parquet, 21_Tradfye_Orderflow.parquet)*
- **Interbank Spot Orderflow Mechanics**: Decentralized OTC market structure. CVD taker deltas do not apply to interbank spot flow. Tape volume governed by broker tick volume with live spread friction of `0.91 bps`.
- **Session Volume Structure**: Price operating at `ABOVE_VALUE (Imbalance)` with Daily POC at `1.10358` (VAH: `1.10386` / VAL: `1.10300`).

---

## 5. Institutional Whale Armor & Resting Orderbook Depth
*(Sources: 10_Whale_Orders.parquet, 12_Hyperdash.parquet, 17_Orderbook.parquet, 4_Hyperliquid_Analysis.parquet)*
- **Interbank Institutional Tier-1 Depth**: Decentralized OTC spot liquidity. Resting whale limit walls from crypto venues do not apply.
- **Verified Broker Armor**: Live Bid `1.10406` / Live Ask `1.10416` with institutional spread of `0.91 bps`. Structural defense anchored at Asian Range `[1.10213 - 1.10402]` and London Range `[1.10161 - 1.10419]`.

---

## 6. Liquidation Max Pain, Heatmaps & Cascade Boundaries
*(Sources: 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 14_Hyperdash_Liq_Map.parquet, 14_Liquidation_Matrix.parquet, 15_Hyperdash_Stops_Map.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **TradFi Structural Liquidity Boundaries**: Centralized perp liquidation feeds do not apply to interbank OTC spot.
- **Stop-Run Cascades & Liquidity Pools**: Primary institutional stop pools reside beyond Classical Pivot extremes (S1: `1.10159` / S2: `1.09997` for long stops; R1: `1.10479` / R2: `1.10637` for short stops) and Asian session extremes `[1.10213 - 1.10402]`.

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
  * `Sun Oct 25 6:30am` [CHF - Low Impact]: Daylight Saving Time Shift (Forecast: , Previous: )
  * `Sun Oct 25 6:30am` [GBP - Low Impact]: Daylight Saving Time Shift (Forecast: , Previous: )
  * `Mon Oct 26 4:30pm` [GBP - Low Impact]: CBI Realized Sales (Forecast: -47, Previous: -55)
- **Real-Time Macro Catalysts & Headlines (19_News.parquet)**:
  * `4 hr ago` [General Market Intel]: UK Money and Credit - September 2026 (bankofengland.co.uk)

---

## 10. Algorithmic Trade Formulation & Sovereign Decision
- **Sovereign Gate Decision**: **`FAIL_CLOSED_STAND_ASIDE`**
- **Dynamic Capacity Verification**: Active Open=`0` | Resting Pending=`2` | Capacity Check: `N_open + N_pending <= 3` (**`PASS`**)
- **Triple Floor Solvency Check**: Current Equity=`4,744.32 USD` | Hard Floor=`4,775.00 USD` | Buffer=`-30.68 USD` | Solvency Check: **`DEFENSE_MODE`**
- **Stand-Aside Reason**: Absence of statistically validated auction edge and defending resting armor. Standing aside preserves statutory hard floor.