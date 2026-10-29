# 🔬 MASTER 43-FEED QUANTITATIVE DOSSIER: GBPUSD (British Pound / US Dollar)
**MT5 Symbol**: `GBPUSD.pi` | **Category**: `FX Major` | **Tier**: `Tier 3`
**Execution Posture**: `PASSIVE LIMIT ONLY` | **Timestamp**: 2026-10-29 14:43:14 UTC
**Pipeline Clearance**: `QUALIFIED` | **Data Freshness**: `1.2m`

---

## 1. MT5 Live Broker Telemetry & Spread Friction Gate
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet)*
- **Live Bid Quote**: `1.33304` | **Live Ask Quote**: `1.33305` | **Mid Price**: `1.33305`
- **Spread Points**: `1.0 pts` | **Spread BPS**: `0.08 bps` (Mandatory Cap: `5.0 bps`)
- **Gate Status**: **`PASS`** (Spread friction within mandatory threshold; safe for maker execution)
- **Order Allowed**: `BUY_LIMIT / SELL_LIMIT` | **Pillar 1 Clearance**: `QUALIFIED`
- **Broker Specifications**: Contract Size=`1.00` | Tick Value=`1.00 USD` | Min Lot=`0.01` | Digits=`5`
- **Account Capital Context**: Balance=`4,744.55 USD` | Equity=`4,744.32 USD` | Free Margin=`4,342.62 USD` | Inviolate Hard Floor=`4,775.00 USD` (Cushion: `-30.68 USD`)
- **Pipeline Health**: Feed #00 Status=`PASS` | Overall Pipeline Telemetry=`33/33 FEEDS PASS (SYNCHRONIZED)`

---

## 2. Technical Profile, Multi-Sigma VWAP Dispersion & Volatility
*(Sources: 11_Technical.parquet, 11_Technical_BTC_Ribbon.parquet)*
- **Last Verified Price**: `1.33242` | **24h Change**: `+0.28%` (24h High: `1.33387`, 24h Low: `1.32863`)
- **Weekly Range**: Week High=`1.33590` | Week Low=`1.32723` | Daily POC=`1.33207` | Daily VAH=`1.33306` | Daily VAL=`1.33127`
- **Session VWAP**: `1.33189` | **Rolling 24h VWAP**: `1.33178` | **Distance to VWAP**: `+0.04%`
- **VWAP Z-Score**: `+0.72 sigma` | **Mean Reversion Bias**: **`FAIR VALUE`**
- **VWAP Dispersion Bands**:
  * +1.00 sigma: `1.33263` | -1.00 sigma: `1.33115`
  * +1.28 sigma (80% CI): `1.33284` | -1.28 sigma: `1.33094`
  * +2.00 sigma (95% CI): `1.33337` | -2.00 sigma: `1.33041`
  * +2.01 sigma: `1.33338` | -2.01 sigma: `1.33040`
  * +2.51 sigma (98.8% CI): `1.33375` | -2.51 sigma: `1.33003`
  * +3.00 sigma (99.7% CI Extreme): `1.33411` | -3.00 sigma: `1.32967`
- **Oscillators & Volatility**:
  * **RSI (14)**: `53.78` | **RSI State**: **`NEUTRAL`**
  * **ATR (14)**: `0.00099` | **ATR %**: `0.07%`
  * **Bollinger Bands**: Upper=`1.33355` | Mid=`1.33195` | Lower=`1.33035` | Bandwidth=`0.24%`
  * **MACD**: Line=`+0.0001` | Signal=`+0.0001` | Hist=`-0.0000`
- **Exponential Moving Average Ribbon (EMA)**:
  * Short Horizon: EMA-5=`1.33210` | EMA-9=`1.33213` | EMA-13=`1.33211` | EMA-20=`1.33204`
  * Intermediate: EMA-34=`1.33196` | EMA-50=`1.33187` | EMA-89=`1.33166` | EMA-100=`1.33162`
  * Institutional: EMA-144=`1.33160` | EMA-200=`1.33188` (Slope: `+0.004%`) | EMA-233=`1.33195` (Slope: `+0.003%`)
  * **Trend Bias**: **`BULLISH`**

---

## 3. Auction Market Structure & Value Profile
*(Sources: 20_Auction_Market_Structure.parquet)*
- **Daily Auction Value Area**:
  * High (VAH): `1.33306` | Point of Control (POC): `1.33207` | Low (VAL): `1.33127`
  * Distance to POC: `+0.08%` | Distance to VAH: `+0.00%` | Distance to VAL: `+0.14%`
  * **Value Area Position**: **`ABOVE_VALUE (Imbalance)`** | **Auction Regime**: **`RANGE_EXPANSION`** | **Session Bias**: **`BULLISH (Above Pivot)`**
- **Prior Day & Weekly Auction Profile**:
  * Prior Day: PD VAH=`1.33166` | PD POC=`1.33007` | PD VAL=`1.32791` | PDH=`1.33384` | PDL=`1.32723` | PDC=`1.33257`
  * Monday Reference: Monday High=`1.33875` | Monday Low=`1.33272` | Monday Mid=`1.33574`
  * Weekly Value Area: Weekly VAH=`1.33487` | Weekly POC=`1.33195` | Weekly VAL=`1.32988`
  * Multi-Week Extremes: Current Week High (CWH)=`1.33875` | CWL=`1.32723` | Prior Week High (PWH)=`1.34190` | PWL=`1.32986`
  * Multi-Month Extremes: Current Month High (CMH)=`1.34190` | CML=`1.31367` | Prior Month High (PMH)=`1.35680` | PML=`1.32022`
- **Session Liquidity Extremes & Initial Balance**:
  * Asian Session: Range `[1.33024 - 1.33360]`
  * London Session: Range `[1.32961 - 1.33387]`
  * New York Session: Range `[1.33006 - 1.33387]`
  * Initial Balance (IB): IB High=`1.33206` | IB Low=`1.33108`
- **Fibonacci Golden Pocket & Optimal Trade Entry (OTE)**:
  * Swing Range: High=`1.33387` | Low=`1.32863` | Direction=`BULLISH_IMPULSE`
  * Golden Pocket [0.618 - 0.65]: `[1.33046 - 1.33063]`
  * Optimal Trade Entry (0.702): `1.33019` | Invalidation Level: `1.32975` | Status: **`SHALLOW_RETRACE`**
- **Classical & Weekly Pivots**:
  * Daily Classical: Pivot=`1.33121` | R1=`1.33520` | S1=`1.32859` | R2=`1.33782` | S2=`1.32460`
  * Weekly Classical: Weekly Pivot=`1.33633` | Weekly R1=`1.34280` | Weekly S1=`1.33076`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Orderflow
*(Sources: 18_CVD.parquet, 18_CVD_30D_5m.parquet, 18_CVD_30D_15m.parquet, 18_CVD_30D_1h.parquet, 18_CVD_30D_4h.parquet, 18_CVD_30D_ALL.parquet, 21_Tradfye_Orderflow.parquet)*
- **Primary 15m CVD Microstructure (18_CVD_30D_15m.parquet)**:
  * Candle Delta: `+246.52 USD` (Base: `+184.9909 coins`) | Delta %: `+19.09%`
  * Taker Volumes: Taker Buy=`768.90 USD` | Taker Sell=`522.38 USD` | Total Vol=`969.00 USD`
  * Cumulative CVD: `+7,982.80 USD` (Base: `+5,980.4869`)
  * Rolling CVD Z-Score: `+0.07 sigma` | Price Return: `+0.02%`
  * **Delta Regime**: **`AGGRESSIVE BUYING`** | Trades Count: `969`
- **Multi-Timeframe Delta Comparison**:
  * 5m Bar: Delta=`-155.94 USD` | Delta %=`-43.02%` | Z-Score=`-1.20` | Regime=`AGGRESSIVE SELLING`
  * 1h Bar: Delta=`-2,200.16 USD` | Delta %=`-40.17%` | Z-Score=`-0.70` | Regime=`AGGRESSIVE SELLING`
  * 4h Bar: Delta=`+4,068.43 USD` | Delta %=`+12.79%` | Z-Score=`-0.11` | Regime=`DELTA ALIGNED`
  * 30D Consolidated (ALL): Cumulative Trend=`+31,226.35 USD` | Long-Term Regime=`DELTA ALIGNED`
- **Institutional Footprint & Deribit Options Armor (21_Tradfye_Orderflow.parquet)**:
  * Candle VWAP: `1.33305` | Estimated POC: `1.33305` | Avg Trade Size: `0.00 USD`
  * Net Delta USD: `+0.00 USD` | Net Delta %: `+0.00%` | Orderflow CVD: `+0.00 USD`
  * Orderflow Regime: **`BALANCED`** | Orderflow Divergence: **`NONE`**
  * Deribit Options Walls: Max Pain=`0.00` | Call Wall=`0.00` | Put Wall=`0.00`

---

## 5. Institutional Whale Armor & Resting Orderbook Depth
*(Sources: 10_Whale_Orders.parquet, 12_Hyperdash.parquet, 17_Orderbook.parquet, 4_Hyperliquid_Analysis.parquet)*
- **Interbank Institutional Tier-1 Depth**: Decentralized OTC spot liquidity. Resting whale limit walls from crypto venues do not apply.
- **Verified Broker Armor**: Live Bid `1.33304` / Live Ask `1.33305` with institutional spread of `0.08 bps`. Structural defense anchored at Asian Range `[1.33024 - 1.33360]` and London Range `[1.32961 - 1.33387]`.

---

## 6. Liquidation Max Pain, Heatmaps & Cascade Boundaries
*(Sources: 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 14_Hyperdash_Liq_Map.parquet, 14_Liquidation_Matrix.parquet, 15_Hyperdash_Stops_Map.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **TradFi Structural Liquidity Boundaries**: Centralized perp liquidation feeds do not apply to interbank OTC spot.
- **Stop-Run Cascades & Liquidity Pools**: Primary institutional stop pools reside beyond Classical Pivot extremes (S1: `1.32859` / S2: `1.32460` for long stops; R1: `1.33520` / R2: `1.33782` for short stops) and Asian session extremes `[1.33024 - 1.33360]`.

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
- **Bar-by-Bar Microstructure Footprint (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
  * Venue Source: `MT5-Interbank-CVD` | Timeframe: `15m` | Last Price: `1.33305`
  * Footprint Auction Profile: Bar VWAP=`1.33259` | Bar POC=`1.33259` | Bar VAH=`1.33287` | Bar VAL=`1.33232`
  * Orderflow Volumes: Total Vol=`1,291.28 USD` | Taker Buy=`768.90 USD` | Taker Sell=`522.38 USD`
  * Bar Delta Profile: Delta=`+246.52 USD` (`+19.09%`) | Max Delta=`+246.52 USD` | Min Delta=`+0.00 USD` | Cumulative Bar Delta=`+7,982.80 USD`
  * Order Execution Dynamics: Trades Count=`969` | Avg Trade Size=`1.33 USD`
  * Tape Imbalances: Imbalance Ratio=`300.0%` | Buy Imbalances Count=`1` | Sell Imbalances Count=`0`
  * Footprint Open Interest: Bar OI=`0.00 USD` | Bar OI Change=`+0.00 USD`
- **CoinGlass Algorithmic Footprint Signals (25_CoinGlass_Footprint_Signals.parquet)**:
  * Signal Classification: Type=`BULLISH ABSORPTION` | Bias: **`BULLISH`** | Signal Time=`2026-10-28 17:30:00 IST` | Timeframe=`4h`
  * Signal Context: Headline=`GBPUSD Macro Delta Flow: BULLISH ABSORPTION` | Price Level=`1.32884` | Absorbed Volume=`1,668.59 USD`
  * Bar Footprint Context: Current Bar Delta=`+1,668.59 USD` | Current Bar Volume=`21,495.32 USD` | Delta in View=`-33,883.95 USD`
  * Historical Detail: `Bar Delta: 1,668.59 USD | Cumulative CVD: -33,883.95 | CVD Z-Score: 0.98 | Vol: 21,495.32 USD` | KPI=`BULLISH ABSORPTION` | Bias=`BULLISH`
- **Multi-Horizon Macro Capital Netflows (2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet)**:
  * Spot Capital Netflows:
    - Tactical: 5m=`-` | 15m=`-` | 30m=`-` | 1h=`-`
    - Intermediate: 2h=`-` | 4h=`-` | 6h=`-` | 8h=`-` | 12h=`-` | 24h=`-`
    - Macro Horizons: 1-Week=`-` | 15-Day=`-` | 30-Day=`-` | Market Cap=`-`
  * Futures Capital Netflows:
    - Tactical: 5m=`-` | 15m=`-` | 30m=`-` | 1h=`-`
    - Intermediate: 2h=`-` | 4h=`-` | 6h=`-` | 8h=`-` | 12h=`-` | 24h=`-`
    - Macro Horizons: 1-Week=`-` | 15-Day=`-` | 30-Day=`-` | Market Cap=`-`

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
  * `Mon Oct 26 4:30pm` [GBP - Low Impact]: CBI Realized Sales (Forecast: -47, Previous: -55)
  * `Tue Oct 27 5:31am` [GBP - Low Impact]: BRC Shop Price Index y/y (Forecast: 1.6%, Previous: 1.4%)
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