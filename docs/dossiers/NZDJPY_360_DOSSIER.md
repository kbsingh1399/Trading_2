# 🔬 MASTER 43-FEED QUANTITATIVE DOSSIER: NZDJPY (NZD/JPY)
**MT5 Symbol**: `NZDJPY.pi` | **Category**: `Forex Cross` | **Tier**: `Tier 2`
**Execution Posture**: `PASSIVE LIMIT ONLY` | **Timestamp**: 2026-10-29 14:43:14 UTC
**Pipeline Clearance**: `QUALIFIED` | **Data Freshness**: `1.2m`

---

## 1. MT5 Live Broker Telemetry & Spread Friction Gate
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet)*
- **Live Bid Quote**: `88.58800` | **Live Ask Quote**: `88.59300` | **Mid Price**: `88.59050`
- **Spread Points**: `5.0 pts` | **Spread BPS**: `0.56 bps` (Mandatory Cap: `5.0 bps`)
- **Gate Status**: **`PASS`** (Spread friction within mandatory threshold; safe for maker execution)
- **Order Allowed**: `BUY_LIMIT / SELL_LIMIT` | **Pillar 1 Clearance**: `QUALIFIED`
- **Broker Specifications**: Contract Size=`1.00` | Tick Value=`1.00 USD` | Min Lot=`0.01` | Digits=`5`
- **Account Capital Context**: Balance=`4,744.55 USD` | Equity=`4,744.32 USD` | Free Margin=`4,342.62 USD` | Inviolate Hard Floor=`4,775.00 USD` (Cushion: `-30.68 USD`)
- **Pipeline Health**: Feed #00 Status=`PASS` | Overall Pipeline Telemetry=`33/33 FEEDS PASS (SYNCHRONIZED)`

---

## 2. Technical Profile, Multi-Sigma VWAP Dispersion & Volatility
*(Sources: 11_Technical.parquet, 11_Technical_BTC_Ribbon.parquet)*
- **Last Verified Price**: `88.62500` | **24h Change**: `-0.20%` (24h High: `89.03900`, 24h Low: `88.52300`)
- **Weekly Range**: Week High=`90.03500` | Week Low=`88.07400` | Daily POC=`88.66300` | Daily VAH=`88.75900` | Daily VAL=`88.61700`
- **Session VWAP**: `88.70221` | **Rolling 24h VWAP**: `88.76203` | **Distance to VWAP**: `-0.09%`
- **VWAP Z-Score**: `-1.13 sigma` | **Mean Reversion Bias**: **`FAIR VALUE`**
- **VWAP Dispersion Bands**:
  * +1.00 sigma: `88.77055` | -1.00 sigma: `88.63386`
  * +1.28 sigma (80% CI): `88.78969` | -1.28 sigma: `88.61472`
  * +2.00 sigma (95% CI): `88.83890` | -2.00 sigma: `88.56551`
  * +2.01 sigma: `88.83958` | -2.01 sigma: `88.56483`
  * +2.51 sigma (98.8% CI): `88.87376` | -2.51 sigma: `88.53065`
  * +3.00 sigma (99.7% CI Extreme): `88.90725` | -3.00 sigma: `88.49716`
- **Oscillators & Volatility**:
  * **RSI (14)**: `44.50` | **RSI State**: **`BEARISH`**
  * **ATR (14)**: `0.08710` | **ATR %**: `0.10%`
  * **Bollinger Bands**: Upper=`88.79099` | Mid=`88.68260` | Lower=`88.57421` | Bandwidth=`0.24%`
  * **MACD**: Line=`-0.0037` | Signal=`+0.0032` | Hist=`-0.0069`
- **Exponential Moving Average Ribbon (EMA)**:
  * Short Horizon: EMA-5=`88.66395` | EMA-9=`88.68008` | EMA-13=`88.68472` | EMA-20=`88.68657`
  * Intermediate: EMA-34=`88.69053` | EMA-50=`88.69939` | EMA-89=`88.74060` | EMA-100=`88.75669`
  * Institutional: EMA-144=`88.82914` | EMA-200=`88.98574` (Slope: `-0.041%`) | EMA-233=`89.05845` (Slope: `-0.043%`)
  * **Trend Bias**: **`STRONG BEARISH`**

---

## 3. Auction Market Structure & Value Profile
*(Sources: 20_Auction_Market_Structure.parquet)*
- **Daily Auction Value Area**:
  * High (VAH): `88.75900` | Point of Control (POC): `88.66300` | Low (VAL): `88.61700`
  * Distance to POC: `-0.07%` | Distance to VAH: `-0.18%` | Distance to VAL: `-0.02%`
  * **Value Area Position**: **`BELOW_VALUE (Imbalance)`** | **Auction Regime**: **`RANGE_EXPANSION`** | **Session Bias**: **`BEARISH (Below Pivot)`**
- **Prior Day & Weekly Auction Profile**:
  * Prior Day: PD VAH=`88.97600` | PD POC=`88.83800` | PD VAL=`88.49300` | PDH=`89.79700` | PDL=`88.07400` | PDC=`88.75800`
  * Monday Reference: Monday High=`89.62100` | Monday Low=`89.24400` | Monday Mid=`89.43300`
  * Weekly Value Area: Weekly VAH=`90.02800` | Weekly POC=`89.46600` | Weekly VAL=`88.76000`
  * Multi-Week Extremes: Current Week High (CWH)=`90.03500` | CWL=`88.07400` | Prior Week High (PWH)=`90.33800` | PWL=`88.69600`
  * Multi-Month Extremes: Current Month High (CMH)=`90.33800` | CML=`88.07400` | Prior Month High (PMH)=`94.70700` | PML=`88.22900`
- **Session Liquidity Extremes & Initial Balance**:
  * Asian Session: Range `[88.60500 - 88.95700]`
  * London Session: Range `[88.58300 - 88.78600]`
  * New York Session: Range `[88.52300 - 88.79800]`
  * Initial Balance (IB): IB High=`88.75600` | IB Low=`88.63100`
- **Fibonacci Golden Pocket & Optimal Trade Entry (OTE)**:
  * Swing Range: High=`89.03900` | Low=`88.52300` | Direction=`BEARISH_IMPULSE`
  * Golden Pocket [0.618 - 0.65]: `[88.84200 - 88.85800]`
  * Optimal Trade Entry (0.702): `88.88500` | Invalidation Level: `88.92900` | Status: **`SHALLOW_RETRACE`**
- **Classical & Weekly Pivots**:
  * Daily Classical: Pivot=`88.87600` | R1=`89.67900` | S1=`87.95600` | R2=`90.59900` | S2=`87.15300`
  * Weekly Classical: Weekly Pivot=`89.45500` | Weekly R1=`90.21300` | Weekly S1=`88.57100`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Orderflow
*(Sources: 18_CVD.parquet, 18_CVD_30D_5m.parquet, 18_CVD_30D_15m.parquet, 18_CVD_30D_1h.parquet, 18_CVD_30D_4h.parquet, 18_CVD_30D_ALL.parquet, 21_Tradfye_Orderflow.parquet)*
- **Interbank Spot Orderflow Mechanics**: Decentralized OTC market structure. CVD taker deltas do not apply to interbank spot flow. Tape volume governed by broker tick volume with live spread friction of `0.56 bps`.
- **Session Volume Structure**: Price operating at `BELOW_VALUE (Imbalance)` with Daily POC at `88.66300` (VAH: `88.75900` / VAL: `88.61700`).

---

## 5. Institutional Whale Armor & Resting Orderbook Depth
*(Sources: 10_Whale_Orders.parquet, 12_Hyperdash.parquet, 17_Orderbook.parquet, 4_Hyperliquid_Analysis.parquet)*
- **Interbank Institutional Tier-1 Depth**: Decentralized OTC spot liquidity. Resting whale limit walls from crypto venues do not apply.
- **Verified Broker Armor**: Live Bid `88.58800` / Live Ask `88.59300` with institutional spread of `0.56 bps`. Structural defense anchored at Asian Range `[88.60500 - 88.95700]` and London Range `[88.58300 - 88.78600]`.

---

## 6. Liquidation Max Pain, Heatmaps & Cascade Boundaries
*(Sources: 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 14_Hyperdash_Liq_Map.parquet, 14_Liquidation_Matrix.parquet, 15_Hyperdash_Stops_Map.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **TradFi Structural Liquidity Boundaries**: Centralized perp liquidation feeds do not apply to interbank OTC spot.
- **Stop-Run Cascades & Liquidity Pools**: Primary institutional stop pools reside beyond Classical Pivot extremes (S1: `87.95600` / S2: `87.15300` for long stops; R1: `89.67900` / R2: `90.59900` for short stops) and Asian session extremes `[88.60500 - 88.95700]`.

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
  * Alternative Venues: WhiteBIT=`+0.0000%` | LBank=`+0.0200%` | tradeXYZ=`-0.0012%`
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
  * `Mon Oct 26 All Day` [NZD - Low Impact]: Bank Holiday (Forecast: , Previous: )
  * `Tue Oct 27 5:20am` [JPY - Low Impact]: SPPI y/y (Forecast: 3.7%, Previous: 3.5%)
  * `Tue Oct 27 10:30am` [JPY - Low Impact]: BOJ Core CPI y/y (Forecast: 1.9%, Previous: 1.8%)
- **Real-Time Macro Catalysts & Headlines (19_News.parquet)**:
  * `7 hr ago` [General Market Intel]: Japan's consumer confidence weakens in October (breakingthenews.net)
  * `14 hr ago` [General Market Intel]: ANZ New Zealand Business Outlook: Resilient (anz.co.nz)

---

## 10. Algorithmic Trade Formulation & Sovereign Decision
- **Sovereign Gate Decision**: **`FAIL_CLOSED_STAND_ASIDE`**
- **Dynamic Capacity Verification**: Active Open=`0` | Resting Pending=`2` | Capacity Check: `N_open + N_pending <= 3` (**`PASS`**)
- **Triple Floor Solvency Check**: Current Equity=`4,744.32 USD` | Hard Floor=`4,775.00 USD` | Buffer=`-30.68 USD` | Solvency Check: **`DEFENSE_MODE`**
- **Stand-Aside Reason**: Absence of statistically validated auction edge and defending resting armor. Standing aside preserves statutory hard floor.