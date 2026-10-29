# 🔬 MASTER 43-FEED QUANTITATIVE DOSSIER: EURUSD (Euro / US Dollar)
**MT5 Symbol**: `EURUSD.pi` | **Category**: `FX Major` | **Tier**: `Tier 3`
**Execution Posture**: `PASSIVE LIMIT ONLY` | **Timestamp**: 2026-10-29 14:43:14 UTC
**Pipeline Clearance**: `QUALIFIED` | **Data Freshness**: `1.2m`

---

## 1. MT5 Live Broker Telemetry & Spread Friction Gate
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet)*
- **Live Bid Quote**: `1.11375` | **Live Ask Quote**: `1.11376` | **Mid Price**: `1.11376`
- **Spread Points**: `1.0 pts` | **Spread BPS**: `0.09 bps` (Mandatory Cap: `5.0 bps`)
- **Gate Status**: **`PASS`** (Spread friction within mandatory threshold; safe for maker execution)
- **Order Allowed**: `BUY_LIMIT / SELL_LIMIT` | **Pillar 1 Clearance**: `QUALIFIED`
- **Broker Specifications**: Contract Size=`1.00` | Tick Value=`1.00 USD` | Min Lot=`0.01` | Digits=`5`
- **Account Capital Context**: Balance=`4,744.55 USD` | Equity=`4,744.32 USD` | Free Margin=`4,342.62 USD` | Inviolate Hard Floor=`4,775.00 USD` (Cushion: `-30.68 USD`)
- **Pipeline Health**: Feed #00 Status=`PASS` | Overall Pipeline Telemetry=`33/33 FEEDS PASS (SYNCHRONIZED)`

---

## 2. Technical Profile, Multi-Sigma VWAP Dispersion & Volatility
*(Sources: 11_Technical.parquet, 11_Technical_BTC_Ribbon.parquet)*
- **Last Verified Price**: `1.11354` | **24h Change**: `+0.07%` (24h High: `1.11694`, 24h Low: `1.11045`)
- **Weekly Range**: Week High=`1.11999` | Week Low=`1.11045` | Daily POC=`1.11374` | Daily VAH=`1.11513` | Daily VAL=`1.11318`
- **Session VWAP**: `1.11385` | **Rolling 24h VWAP**: `1.11430` | **Distance to VWAP**: `-0.03%`
- **VWAP Z-Score**: `-0.36 sigma` | **Mean Reversion Bias**: **`FAIR VALUE`**
- **VWAP Dispersion Bands**:
  * +1.00 sigma: `1.11473` | -1.00 sigma: `1.11298`
  * +1.28 sigma (80% CI): `1.11497` | -1.28 sigma: `1.11273`
  * +2.00 sigma (95% CI): `1.11560` | -2.00 sigma: `1.11210`
  * +2.01 sigma: `1.11561` | -2.01 sigma: `1.11209`
  * +2.51 sigma (98.8% CI): `1.11605` | -2.51 sigma: `1.11166`
  * +3.00 sigma (99.7% CI Extreme): `1.11648` | -3.00 sigma: `1.11123`
- **Oscillators & Volatility**:
  * **RSI (14)**: `48.61` | **RSI State**: **`NEUTRAL`**
  * **ATR (14)**: `0.00101` | **ATR %**: `0.09%`
  * **Bollinger Bands**: Upper=`1.11543` | Mid=`1.11375` | Lower=`1.11208` | Bandwidth=`0.30%`
  * **MACD**: Line=`-0.0003` | Signal=`-0.0002` | Hist=`-0.0002`
- **Exponential Moving Average Ribbon (EMA)**:
  * Short Horizon: EMA-5=`1.11301` | EMA-9=`1.11326` | EMA-13=`1.11343` | EMA-20=`1.11361`
  * Intermediate: EMA-34=`1.11382` | EMA-50=`1.11395` | EMA-89=`1.11404` | EMA-100=`1.11406`
  * Institutional: EMA-144=`1.11422` | EMA-200=`1.11459` (Slope: `-0.010%`) | EMA-233=`1.11468` (Slope: `-0.010%`)
  * **Trend Bias**: **`STRONG BEARISH`**

---

## 3. Auction Market Structure & Value Profile
*(Sources: 20_Auction_Market_Structure.parquet)*
- **Daily Auction Value Area**:
  * High (VAH): `1.11513` | Point of Control (POC): `1.11374` | Low (VAL): `1.11318`
  * Distance to POC: `+0.00%` | Distance to VAH: `-0.12%` | Distance to VAL: `+0.06%`
  * **Value Area Position**: **`INSIDE_VALUE (Balance)`** | **Auction Regime**: **`ROTATIONAL_BALANCE`** | **Session Bias**: **`BEARISH (Below Pivot)`**
- **Prior Day & Weekly Auction Profile**:
  * Prior Day: PD VAH=`1.11519` | PD POC=`1.11258` | PD VAL=`1.11175` | PDH=`1.11694` | PDL=`1.11128` | PDC=`1.11524`
  * Monday Reference: Monday High=`1.12267` | Monday Low=`1.11731` | Monday Mid=`1.11999`
  * Weekly Value Area: Weekly VAH=`1.11644` | Weekly POC=`1.11375` | Weekly VAL=`1.11204`
  * Multi-Week Extremes: Current Week High (CWH)=`1.12267` | CWL=`1.11045` | Prior Week High (PWH)=`1.12608` | PWL=`1.11808`
  * Multi-Month Extremes: Current Month High (CMH)=`1.13368` | CML=`1.11045` | Prior Month High (PMH)=`1.16542` | PML=`1.13117`
- **Session Liquidity Extremes & Initial Balance**:
  * Asian Session: Range `[1.11339 - 1.11609]`
  * London Session: Range `[1.11254 - 1.11521]`
  * New York Session: Range `[1.11045 - 1.11521]`
  * Initial Balance (IB): IB High=`1.11449` | IB Low=`1.11355`
- **Fibonacci Golden Pocket & Optimal Trade Entry (OTE)**:
  * Swing Range: High=`1.11694` | Low=`1.11045` | Direction=`BEARISH_IMPULSE`
  * Golden Pocket [0.618 - 0.65]: `[1.11446 - 1.11467]`
  * Optimal Trade Entry (0.702): `1.11501` | Invalidation Level: `1.11555` | Status: **`SHALLOW_RETRACE`**
- **Classical & Weekly Pivots**:
  * Daily Classical: Pivot=`1.11449` | R1=`1.11769` | S1=`1.11203` | R2=`1.12015` | S2=`1.10883`
  * Weekly Classical: Weekly Pivot=`1.12140` | Weekly R1=`1.12473` | Weekly S1=`1.11673`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Orderflow
*(Sources: 18_CVD.parquet, 18_CVD_30D_5m.parquet, 18_CVD_30D_15m.parquet, 18_CVD_30D_1h.parquet, 18_CVD_30D_4h.parquet, 18_CVD_30D_ALL.parquet, 21_Tradfye_Orderflow.parquet)*
- **Primary 15m CVD Microstructure (18_CVD_30D_15m.parquet)**:
  * Candle Delta: `-222.98 USD` (Base: `-200.0000 coins`) | Delta %: `-25.64%`
  * Taker Volumes: Taker Buy=`323.32 USD` | Taker Sell=`546.30 USD` | Total Vol=`780.00 USD`
  * Cumulative CVD: `+6,191.90 USD` (Base: `+5,540.6202`)
  * Rolling CVD Z-Score: `-0.59 sigma` | Price Return: `+0.00%`
  * **Delta Regime**: **`BEARISH ABSORPTION`** | Trades Count: `780`
- **Multi-Timeframe Delta Comparison**:
  * 5m Bar: Delta=`-165.93 USD` | Delta %=`-78.33%` | Z-Score=`-1.62` | Regime=`AGGRESSIVE SELLING`
  * 1h Bar: Delta=`-2,196.71 USD` | Delta %=`-57.94%` | Z-Score=`-0.96` | Regime=`AGGRESSIVE SELLING`
  * 4h Bar: Delta=`-13,427.34 USD` | Delta %=`-60.67%` | Z-Score=`-1.67` | Regime=`AGGRESSIVE SELLING`
  * 30D Consolidated (ALL): Cumulative Trend=`-4,966.80 USD` | Long-Term Regime=`AGGRESSIVE SELLING`
- **Institutional Footprint & Deribit Options Armor (21_Tradfye_Orderflow.parquet)**:
  * Candle VWAP: `1.11376` | Estimated POC: `1.11376` | Avg Trade Size: `0.00 USD`
  * Net Delta USD: `+0.00 USD` | Net Delta %: `+0.00%` | Orderflow CVD: `+0.00 USD`
  * Orderflow Regime: **`BALANCED`** | Orderflow Divergence: **`NONE`**
  * Deribit Options Walls: Max Pain=`0.00` | Call Wall=`0.00` | Put Wall=`0.00`

---

## 5. Institutional Whale Armor & Resting Orderbook Depth
*(Sources: 10_Whale_Orders.parquet, 12_Hyperdash.parquet, 17_Orderbook.parquet, 4_Hyperliquid_Analysis.parquet)*
- **Defending Resting Whale Walls (10_Whale_Orders.parquet)**:
  * Defending Bid Wall: `0.00000` (`0.0000` coins / `0.00 USD` on `-`, persistent for `-`, Traded: `0.0%`, Order ID: `-`)
  * Defending Ask Wall: `0.00000` (`0.0000` coins / `0.00 USD` on `-`, persistent for `-`, Traded: `0.0%`, Order ID: `-`)
  * Total Whale Armor Pool: Bids Pool=`0.00 USD` | Asks Pool=`0.00 USD` (Tracked Orders: `0`)
- **Hyperdash Resting Depth & L3 Telemetry (12_Hyperdash.parquet)**:
  * `NEUTRAL`: `0.00 USD` @ `0.00000` (Size: `0.0`, Detail: Delta: +0, Wallet: None, Timestamp: 2026-10-29 19:44:05 IST)
- **Hyperliquid Elite Trader Positioning (4_Hyperliquid_Analysis.parquet)**:
  * Wallet `0x091159a810...` (0x0911...129a): `Long` `9,913,363.35 USD` (8,898,889.9000 xyz:EUR, Margin: 554,798.09 USD, Leverage: 20X Isolated, Entry: 1.1488 USD, Current: 1.1139 USD, Est Liq: 1.0623 USD, PnL: -309,379.07 USD [-3.12%], Fees: +62,301.36 USD)
  * Wallet `0xe03ba8a86e...` (0xe03b...ed11): `Short` `1,950,132.35 USD` (1,750,724.8000 xyz:EUR, Margin: 170,381.23 USD, Leverage: 50X Isolated, Entry: 1.1443 USD, Current: 1.1139 USD, Est Liq: 1.1992 USD, PnL: +53,217.10 USD [+2.73%], Fees: -16,119.34 USD)
  * Wallet `0x3f31bdff8e...` (0x3f31...a3d7): `Short` `1,199,126.83 USD` (1,076,512.1000 xyz:EUR, Margin: 31,090.05 USD, Leverage: 50X Isolated, Entry: 1.1146 USD, Current: 1.1139 USD, Est Liq: 1.1315 USD, PnL: +804.62 USD [+0.07%], Fees: -3,422.73 USD)

---

## 6. Liquidation Max Pain, Heatmaps & Cascade Boundaries
*(Sources: 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 14_Hyperdash_Liq_Map.parquet, 14_Liquidation_Matrix.parquet, 15_Hyperdash_Stops_Map.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **TradFi Structural Liquidity Boundaries**: Centralized perp liquidation feeds do not apply to interbank OTC spot.
- **Stop-Run Cascades & Liquidity Pools**: Primary institutional stop pools reside beyond Classical Pivot extremes (S1: `1.11203` / S2: `1.10883` for long stops; R1: `1.11769` / R2: `1.12015` for short stops) and Asian session extremes `[1.11339 - 1.11609]`.

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
  * Settlement Payouts: Current Expected=`311.48 USD` | Last 24h=`0.00 USD` | Last 3D=`169.62 USD` | Last 7D=`229.77 USD`

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
  * `Mon Oct 26 2:30pm` [EUR - Low Impact]: German ifo Business Climate (Forecast: 90.0, Previous: 89.9)
  * `Tue Oct 27 1:30pm` [EUR - Low Impact]: Spanish Unemployment Rate (Forecast: 9.9%, Previous: 9.9%)
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