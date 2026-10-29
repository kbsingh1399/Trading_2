# 🔬 MASTER 43-FEED QUANTITATIVE DOSSIER: SP500 (S&P 500 Index)
**MT5 Symbol**: `SP500.p` | **Category**: `Equity Index US` | **Tier**: `Tier 4`
**Execution Posture**: `PASSIVE LIMIT ONLY` | **Timestamp**: 2026-10-29 14:43:14 UTC
**Pipeline Clearance**: `QUALIFIED` | **Data Freshness**: `1.2m`

---

## 1. MT5 Live Broker Telemetry & Spread Friction Gate
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet)*
- **Live Bid Quote**: `7706.29000` | **Live Ask Quote**: `7706.53000` | **Mid Price**: `7706.41000`
- **Spread Points**: `24.0 pts` | **Spread BPS**: `0.31 bps` (Mandatory Cap: `5.0 bps`)
- **Gate Status**: **`PASS`** (Spread friction within mandatory threshold; safe for maker execution)
- **Order Allowed**: `BUY_LIMIT / SELL_LIMIT` | **Pillar 1 Clearance**: `QUALIFIED`
- **Broker Specifications**: Contract Size=`1.00` | Tick Value=`1.00 USD` | Min Lot=`0.01` | Digits=`5`
- **Account Capital Context**: Balance=`4,744.55 USD` | Equity=`4,744.32 USD` | Free Margin=`4,342.62 USD` | Inviolate Hard Floor=`4,775.00 USD` (Cushion: `-30.68 USD`)
- **Pipeline Health**: Feed #00 Status=`PASS` | Overall Pipeline Telemetry=`33/33 FEEDS PASS (SYNCHRONIZED)`

---

## 2. Technical Profile, Multi-Sigma VWAP Dispersion & Volatility
*(Sources: 11_Technical.parquet, 11_Technical_BTC_Ribbon.parquet)*
- **Last Verified Price**: `7711.79000` | **24h Change**: `-0.36%` (24h High: `7783.55000`, 24h Low: `7697.54000`)
- **Weekly Range**: Week High=`7783.55000` | Week Low=`7622.72000` | Daily POC=`7716.47000` | Daily VAH=`7729.46000` | Daily VAL=`7710.67000`
- **Session VWAP**: `7720.67600` | **Rolling 24h VWAP**: `7727.11748` | **Distance to VWAP**: `-0.12%`
- **VWAP Z-Score**: `-1.14 sigma` | **Mean Reversion Bias**: **`FAIR VALUE`**
- **VWAP Dispersion Bands**:
  * +1.00 sigma: `7728.46003` | -1.00 sigma: `7712.89196`
  * +1.28 sigma (80% CI): `7730.63956` | -1.28 sigma: `7710.71243`
  * +2.00 sigma (95% CI): `7736.24407` | -2.00 sigma: `7705.10792`
  * +2.01 sigma: `7736.32191` | -2.01 sigma: `7705.03008`
  * +2.51 sigma (98.8% CI): `7740.21393` | -2.51 sigma: `7701.13806`
  * +3.00 sigma (99.7% CI Extreme): `7744.02811` | -3.00 sigma: `7697.32389`
- **Oscillators & Volatility**:
  * **RSI (14)**: `41.49` | **RSI State**: **`BEARISH`**
  * **ATR (14)**: `10.39764` | **ATR %**: `0.13%`
  * **Bollinger Bands**: Upper=`7738.26219` | Mid=`7723.62500` | Lower=`7708.98781` | Bandwidth=`0.38%`
  * **MACD**: Line=`-2.5986` | Signal=`-1.0938` | Hist=`-1.5048`
- **Exponential Moving Average Ribbon (EMA)**:
  * Short Horizon: EMA-5=`7715.04542` | EMA-9=`7717.41092` | EMA-13=`7718.98705` | EMA-20=`7720.54790`
  * Intermediate: EMA-34=`7721.83120` | EMA-50=`7722.60225` | EMA-89=`7723.14332` | EMA-100=`7722.91280`
  * Institutional: EMA-144=`7720.05619` | EMA-200=`7713.96944` (Slope: `+0.009%`) | EMA-233=`7709.98852` (Slope: `+0.013%`)
  * **Trend Bias**: **`BEARISH`**

---

## 3. Auction Market Structure & Value Profile
*(Sources: 20_Auction_Market_Structure.parquet)*
- **Daily Auction Value Area**:
  * High (VAH): `7729.46000` | Point of Control (POC): `7716.47000` | Low (VAL): `7710.67000`
  * Distance to POC: `-0.12%` | Distance to VAH: `-0.29%` | Distance to VAL: `-0.04%`
  * **Value Area Position**: **`BELOW_VALUE (Imbalance)`** | **Auction Regime**: **`TREND_DOWN_ACCEPTANCE`** | **Session Bias**: **`BEARISH (Below Pivot)`**
- **Prior Day & Weekly Auction Profile**:
  * Prior Day: PD VAH=`7738.67000` | PD POC=`7727.63000` | PD VAL=`7723.02000` | PDH=`7783.55000` | PDL=`7714.51000` | PDC=`7724.35000`
  * Monday Reference: Monday High=`7701.39000` | Monday Low=`7613.99000` | Monday Mid=`7657.69000`
  * Weekly Value Area: Weekly VAH=`7741.16000` | Weekly POC=`7726.46000` | Weekly VAL=`7677.86000`
  * Multi-Week Extremes: Current Week High (CWH)=`7783.55000` | CWL=`7613.99000` | Prior Week High (PWH)=`7769.56000` | PWL=`7607.81000`
  * Multi-Month Extremes: Current Month High (CMH)=`7844.04000` | CML=`7607.81000` | Prior Month High (PMH)=`7781.20000` | PML=`7503.05000`
- **Session Liquidity Extremes & Initial Balance**:
  * Asian Session: Range `[7705.30000 - 7733.22000]`
  * London Session: Range `[7709.78000 - 7738.99000]`
  * New York Session: Range `[7697.54000 - 7735.97000]`
  * Initial Balance (IB): IB High=`7738.99000` | IB Low=`7722.51000`
- **Fibonacci Golden Pocket & Optimal Trade Entry (OTE)**:
  * Swing Range: High=`7783.55000` | Low=`7697.54000` | Direction=`BEARISH_IMPULSE`
  * Golden Pocket [0.618 - 0.65]: `[7750.69000 - 7753.45000]`
  * Optimal Trade Entry (0.702): `7757.92000` | Invalidation Level: `7765.14000` | Status: **`SHALLOW_RETRACE`**
- **Classical & Weekly Pivots**:
  * Daily Classical: Pivot=`7740.80000` | R1=`7767.10000` | S1=`7698.06000` | R2=`7809.84000` | S2=`7671.76000`
  * Weekly Classical: Weekly Pivot=`7669.53000` | Weekly R1=`7731.24000` | Weekly S1=`7569.49000`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Orderflow
*(Sources: 18_CVD.parquet, 18_CVD_30D_5m.parquet, 18_CVD_30D_15m.parquet, 18_CVD_30D_1h.parquet, 18_CVD_30D_4h.parquet, 18_CVD_30D_ALL.parquet, 21_Tradfye_Orderflow.parquet)*
- **Primary 15m CVD Microstructure (18_CVD_30D_15m.parquet)**:
  * Candle Delta: `-40,149,170.61 USD` (Base: `-5,192.2425 coins`) | Delta %: `-40.83%`
  * Taker Volumes: Taker Buy=`29,092,706.70 USD` | Taker Sell=`69,241,877.31 USD` | Total Vol=`12,717.00 USD`
  * Cumulative CVD: `+14,011,654.39 USD` (Base: `+1,614.7360`)
  * Rolling CVD Z-Score: `-0.75 sigma` | Price Return: `-0.02%`
  * **Delta Regime**: **`AGGRESSIVE SELLING`** | Trades Count: `12,717`
- **Multi-Timeframe Delta Comparison**:
  * 5m Bar: Delta=`-16,506,141.98 USD` | Delta %=`-59.16%` | Z-Score=`-0.97` | Regime=`AGGRESSIVE SELLING`
  * 1h Bar: Delta=`-317,427,120.94 USD` | Delta %=`-90.00%` | Z-Score=`-1.42` | Regime=`AGGRESSIVE SELLING`
  * 4h Bar: Delta=`-52,081,295.44 USD` | Delta %=`-3.22%` | Z-Score=`+0.09` | Regime=`NEUTRAL CHOP`
  * 30D Consolidated (ALL): Cumulative Trend=`-707,315,788.33 USD` | Long-Term Regime=`NEUTRAL CHOP`
- **Institutional Footprint & Deribit Options Armor (21_Tradfye_Orderflow.parquet)**:
  * Candle VWAP: `7706.41000` | Estimated POC: `7706.41000` | Avg Trade Size: `0.00 USD`
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
- **Consolidated L2 Orderbook Depth & Skew (17_Orderbook.parquet)**:
  * `ASK`: `4,710.26 USD` @ `7,709.10 USD` (Coins: 0.6110 SP500, Cumulative: 3,594,528.30 USD, Tier: 2 orders, Dist: +0.03%, Bias: B/A: 36.6% / 63.4%)
  * `ASK`: `110,870.84 USD` @ `7,709.00 USD` (Coins: 14.3820 SP500, Cumulative: 3,589,818.04 USD, Tier: 4 orders, Dist: +0.03%, Bias: B/A: 36.6% / 63.4%)
  * `ASK`: `211,354.91 USD` @ `7,708.90 USD` (Coins: 27.4170 SP500, Cumulative: 3,478,947.20 USD, Tier: 3 orders, Dist: +0.03%, Bias: B/A: 36.6% / 63.4%)
- **Hyperliquid Elite Trader Positioning (4_Hyperliquid_Analysis.parquet)**:
  * Wallet `0x519c721de7...` (0x519c...6a47): `Long` `17,383,328.59 USD` (120,759.4900 xyz:SPCX, Margin: 1,738,332.86 USD, Leverage: 10X Cross, Entry: 136.7186 USD, Current: 143.8100 USD, Est Liq: 0.00 USD, PnL: +873,252.43 USD [+5.02%], Fees: +47,483.80 USD)
  * Wallet `0x46921f6961...` (0x4692...164f): `Short` `14,700,394.52 USD` (102,185.4200 xyz:SPCX, Margin: 2,940,078.90 USD, Leverage: 5X Cross, Entry: 144.3174 USD, Current: 143.8100 USD, Est Liq: 707.3616 USD, PnL: +46,746.25 USD [+0.32%], Fees: -48,786.41 USD)
  * Wallet `0x024294c53a...` (0x0242...ffa1): `Short` `8,728,679.29 USD` (60,569.5600 xyz:SPCX, Margin: 872,867.93 USD, Leverage: 10X Cross, Entry: 146.4464 USD, Current: 143.8100 USD, Est Liq: 315.8781 USD, PnL: +141,516.41 USD [+1.62%], Fees: -10,563.59 USD)

---

## 6. Liquidation Max Pain, Heatmaps & Cascade Boundaries
*(Sources: 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 14_Hyperdash_Liq_Map.parquet, 14_Liquidation_Matrix.parquet, 15_Hyperdash_Stops_Map.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`0.38734` (Vol: `11,657 USD`, Dist: `+1.80%`) | Long MP=`0.36430` (Vol: `18,624 USD`, Dist: `-4.26%`)
  * 48H Horizon: Short MP=`0.38710` (Vol: `16,032 USD`, Dist: `+1.92%`) | Long MP=`0.36550` (Vol: `31,414 USD`, Dist: `-3.77%`)
  * 3D Horizon: Short MP=`0.38720` (Vol: `16,032 USD`, Dist: `+1.76%`) | Long MP=`0.36515` (Vol: `29,841 USD`, Dist: `-4.03%`)
  * 7D Horizon: Short MP=`0.40569` (Vol: `75,439 USD`, Dist: `+6.90%`) | Long MP=`0.36541` (Vol: `31,414 USD`, Dist: `-3.71%`)
- **Exchange Cumulative Liquidation Cascades (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
  * 1D Cascade: Total=`0.00 USD` | Short Liq Pool=`0.00 USD` | Long Liq Pool=`0.00 USD` | Venues: Binance=`0.00 USD`, OKX=`0.00 USD`, Bybit=`0.00 USD`
  * 7D Cascade: Total=`0.00 USD` | Short Liq Pool=`0.00 USD` | Long Liq Pool=`0.00 USD` | Venues: Binance=`0.00 USD`, OKX=`0.00 USD`, Bybit=`0.00 USD`
- **Cross-Venue Liquidation Matrix & Heatmaps (14_Liquidation_Matrix.parquet, 7_Liq_Heapmap.parquet)**:
  * Liquidation Matrix Strike: Price=`7685.80000` | Vol=`25,000,000 USD` | Cumulative=`50,000,000 USD` | Venue=`MT5 / Synthetic` | Side=`Long Liquidation`
  * Multi-Timeframe Heatmap Density: 1h=`924.78K USD` | 4h=`924.78K USD` | 12h=`943.87K USD` | 24h=`951.07K USD`
- **Hyperdash Real-Time Liquidation & Retail Stop Protection (14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet)**:
  * Hyperdash Liq Cluster: Mark=`0.00 USD` | Cluster Price=`0.00 USD` | Dist=`-` | Cumulative=`0.00 USD` | Short=`0.00 USD` | Long=`0.00 USD` | Size=`-`
- **Live Forced Liquidation Momentum (7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)**:
  * Multi-Timeframe Forced Aggregates (5m): Long Liq=`0.00 USD` | Short Liq=`0.00 USD` | Total=`0.00 USD` | Net Delta=`0.00 USD` | Dominant=`BALANCED`

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
  * Major CEX Rates: Binance=`+0.0050%` | OKX=`+0.0050%` | Bybit=`+0.0050%` | Bitget=`+0.0050%`
  * Mid-Tier CEX Rates: KuCoin=`+0.0050%` | MEXC=`+0.0050%` | Gate=`+0.0026%` | BingX=`+0.0050%` | Bitunix=`+0.0050%`
  * Alternative Venues: WhiteBIT=`+0.0000%` | LBank=`+0.0000%` | tradeXYZ=`-`
  * Inverse Coin-Margined: CoinM Binance=`+0.0000%` | CoinM OKX=`+0.0000%` | CoinM Bybit=`+0.0000%`
- **Exchange Long / Short Ratio Dynamics (3_Exchanges_LS_Ratio*.parquet)**:
  * 15m Tactical: L/S Ratio=`1.00` (Longs: `50.00%`, Shorts: `50.00%`, Total Vol: `0.00 USD`)
  * 1h Primary: L/S Ratio=`1.00` (Longs: `50.00%`, Shorts: `50.00%`, Total Vol: `0.00 USD`)
  * 4h Macro: L/S Ratio=`1.00` (Longs: `50.00%`, Shorts: `50.00%`, Total Vol: `0.00 USD`)
- **Funding Fee Settlement & DEX Arbitrage (6_Funding_Fee_Settlement.parquet, 13_Hyperliquid.parquet)**:
  * Settlement Payouts: Current Expected=`800.04 USD` | Last 24h=`4.78K USD` | Last 3D=`12.99K USD` | Last 7D=`27.44K USD`

---

## 8. Microstructure Footprint, Tape Imbalances & Macro Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 16_Hyperdash_telegram_Intel.parquet, 19_News.parquet, 19_Calendar.parquet)*
- **Bar-by-Bar Microstructure Footprint (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
  * Venue Source: `CoinGlass-AggregatedFutures(Binance)` | Timeframe: `15m` | Last Price: `7706.41000`
  * Footprint Auction Profile: Bar VWAP=`0.39748` | Bar POC=`0.39755` | Bar VAH=`0.39885` | Bar VAL=`0.39525`
  * Orderflow Volumes: Total Vol=`29,756.14 USD` | Taker Buy=`12,978.33 USD` | Taker Sell=`16,777.81 USD`
  * Bar Delta Profile: Delta=`-3,799.47 USD` (`-12.77%`) | Max Delta=`+80.23 USD` | Min Delta=`-5,906.64 USD` | Cumulative Bar Delta=`-14,983.94 USD`
  * Order Execution Dynamics: Trades Count=`750` | Avg Trade Size=`39.67 USD`
  * Tape Imbalances: Imbalance Ratio=`300.0%` | Buy Imbalances Count=`2` | Sell Imbalances Count=`10`
  * Footprint Open Interest: Bar OI=`0.00 USD` | Bar OI Change=`+0.00 USD`
- **CoinGlass Algorithmic Footprint Signals (25_CoinGlass_Footprint_Signals.parquet)**:
  * Signal Classification: Type=`Exhaustion` | Bias: **`BULLISH`** | Signal Time=`10-28 05:32` | Timeframe=`Range 0.001`
  * Signal Context: Headline=`Seller exhaustion` | Price Level=`0.38390` | Absorbed Volume=`0.00 USD`
  * Bar Footprint Context: Current Bar Delta=`+0.00 USD` | Current Bar Volume=`0.00 USD` | Delta in View=`+0.00 USD`
  * Historical Detail: `New 10-bar low with almost no volume in the bottom 10% of the bar, closed in the upper half, bullish · 0.38390` | KPI=`—` | Bias=`—`
- **Multi-Horizon Macro Capital Netflows (2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet)**:
  * Spot Capital Netflows:
    - Tactical: 5m=`-` | 15m=`-` | 30m=`-` | 1h=`-`
    - Intermediate: 2h=`-` | 4h=`-` | 6h=`-` | 8h=`-` | 12h=`-` | 24h=`-`
    - Macro Horizons: 1-Week=`-` | 15-Day=`-` | 30-Day=`-` | Market Cap=`-`
  * Futures Capital Netflows:
    - Tactical: 5m=`+1.55K` | 15m=`-20.07K` | 30m=`-8.20K` | 1h=`-22.80K`
    - Intermediate: 2h=`-54.91K` | 4h=`-79.48K` | 6h=`+52.39K` | 8h=`+22.38K` | 12h=`-74.81K` | 24h=`+336.93K`
    - Macro Horizons: 1-Week=`-95.37K` | 15-Day=`-2.20M` | 30-Day=`-11.45M` | Market Cap=`369.88M`

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
- **Sovereign Gate Decision**: **`STANDBY_RADAR`**
- **Dynamic Capacity Verification**: Active Open=`0` | Resting Pending=`2` | Capacity Check: `N_open + N_pending <= 3` (**`PASS`**)
- **Triple Floor Solvency Check**: Current Equity=`4,744.32 USD` | Hard Floor=`4,775.00 USD` | Buffer=`-30.68 USD` | Solvency Check: **`DEFENSE_MODE`**
- **Autonomous Limit Order Formulation (If Admitted)**:
```json
{
  "ticket": "PENDING_DISPATCH",
  "direction": "BUY_LIMIT",
  "lots": 0.02,
  "entry": 7705.5,
  "sl": 7695.5,
  "tp": 7735.5,
  "risk_usd": 2.0,
  "rr": 3.0,
  "model": "MODEL_2_PULLBACK",
  "thesis": "Daily VAL sweep exhaustion leaning against resting bids with NYSE cash open volume expansion."
}
```
- **Stand-Aside Reason**: High-conviction radar candidate; awaiting entry boundary tap during active market session.