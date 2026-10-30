# 🏛️ SOVEREIGN CANDIDATE DOSSIER: TRX
**Canonical Key**: `TRX` | **Broker Instrument**: `TRXUSD.p` | **Asset Class**: `Crypto Alt L1`
**Timestamp**: `2026-10-30 14:32:43 IST` (`2026-10-30 09:02:43 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `0.3314` | **Live Ask Quote**: `0.3336` | **Mid Price**: `0.3325`
- **Spread Points**: `22.00` | **Spread BPS**: `66.17 bps` (Charter Threshold: `25.00 bps`)
- **Gate 1 Clearance**: **`SPREAD_DISQUALIFIED`** | **Execution Posture**: `DISQUALIFIED` | **Order Type Allowed**: `NONE`
- **True Broker Contract Specifications**:
  * Contract Size: `1.0` | Digits: `4` | Point: `0.0001`
  * Point Value (1.0 Lot): `0.00 USD` | Point Value (0.01 Lot): `0.0000 USD`
  * Allowed Lot Sizing: Min Lot=`0.01` | Step Lot=`0.01` | Max Lot=`20.00`
- **Solvency Defense Ladder**:
  * Hard Floor Stop: `4,775.00 USD` (Zero Open Risk) | Operating Defense Buffer: `4,795.00 USD` (Capital Preservation Mode)
  * Kernel Admission Floor: `4,795.00 USD` (`min(balance, equity) - StressedLoss - 2.00 >= 4,795.00 USD`)
- **Pipeline Health (23_Master_Pipeline_Telemetry.parquet)**: Status=`HEALTHY` | Latency=`4.2 ms` | RAM Usage=`385.0 MB`

---

## 2. Technical Profile, VWAP Dispersion Grid & BTC Ribbon
*(Sources: 11_Technical.parquet, 11_Technical_BTC_Ribbon.parquet)*
- **Session Anchor & Volatility**:
  * Session VWAP: `0.3468` | VWAP Z-Score: `-1.76` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `0.0031` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `36.39` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `0.3730` | Lower -3.00σ Band: `0.3206`
  * Upper +2.51σ Band: `0.3687` | Lower -2.51σ Band: `0.3249`
  * Upper +2.01σ Band: `0.3643` | Lower -2.01σ Band: `0.3293`
  * Upper +2.00σ Band: `0.3642` | Lower -2.00σ Band: `0.3294`
  * Upper +1.28σ Band: `0.3580` | Lower -1.28σ Band: `0.3356`
  * Upper +1.00σ Band: `0.3555` | Lower -1.00σ Band: `0.3381`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`0.3329` | EMA-20=`0.3367` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`0.3397` (Slope: `+0.0000`) | EMA-100=`0.3383`
  * Institutional Anchors: EMA-144=`0.3367` | EMA-200=`0.3353` (Slope: `-0.0668`) | EMA-233=`0.3347`
- **Range Boundaries**: 24H High=`0.3632` | 24H Low=`0.3275` | Weekly High=`0.3632` | Weekly Low=`0.3266`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `0.3578` (Distance: `-7.06%`)
  * Point of Control (POC) = `0.3513` (Distance: `-5.36%`)
  * Value Area Low (VAL) = `0.3429` (Distance: `-3.03%`)
  * Auction Positioning: `BELOW_VALUE (Imbalance)` | Session Bias: **`BULLISH (Above Pivot)`** | Market Regime: `RANGE_EXPANSION`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`0.3312` | POC=`0.3307` | VAL=`0.3293`
  * Prior Day Extremes: PDH=`0.3335` | PDL=`0.3275` | PDC=`0.3275`
  * Monday Range Blueprint: High=`0.3310` | Mid=`0.3300` | Low=`0.3289`
  * Developing Weekly Value Area: Weekly VAH=`0.3470` | Weekly POC=`0.3306` | Weekly VAL=`0.3267`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`0.3632` | Low=`0.3335`
  * London Session (08:00-16:00 UTC): High=`0.3444` | Low=`0.3299`
  * New York Session (13:00-21:00 UTC): High=`0.3345` | Low=`0.3305`
  * Initial Balance (First Hour): IB High=`0.3444` | IB Low=`0.3379`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `0.3312` - `0.3338`
  * Optimal Trade Entry (OTE 0.705): `0.3332`
  * Structural Invalidation Anchor (0.786): `0.3352`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `0.3319` | `0.3324` | `0.3317` | `0.3320` | `3,247,528` | 1,078,159.25 USD | 148,080.43 USD | `+13.73%` | -2,101,297.18 USD | `+0.25` | **`BULLISH`** | `DELTA ALIGNED` |
| `5m` | `0.3319` | `0.3328` | `0.3318` | `0.3324` | `3,138,088` | 1,042,082.79 USD | -389,276.36 USD | `-37.36%` | -2,490,573.54 USD | `-1.79` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `5m` | `0.3324` | `0.3332` | `0.3320` | `0.3321` | `1,921,614` | 638,843.21 USD | -35,343.55 USD | `-5.53%` | -2,525,917.09 USD | `-0.32` | **`BEARISH`** | `DELTA ALIGNED` |
| `15m` | `0.3310` | `0.3329` | `0.3307` | `0.3317` | `10,885,606` | 3,613,244.76 USD | 535,042.44 USD | `+14.81%` | -2,332,621.96 USD | `+0.98` | **`BULLISH`** | `DELTA ALIGNED` |
| `15m` | `0.3317` | `0.3328` | `0.3316` | `0.3324` | `9,559,540` | 3,173,620.42 USD | -81,743.60 USD | `-2.58%` | -2,414,365.56 USD | `+0.29` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `15m` | `0.3324` | `0.3332` | `0.3320` | `0.3321` | `1,915,335` | 636,758.06 USD | -34,910.88 USD | `-5.48%` | -2,449,276.44 USD | `+0.30` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `0.3379` | `0.3380` | `0.3310` | `0.3371` | `71,304,583` | 23,823,772.16 USD | 1,991,288.68 USD | `+8.36%` | -2,620,853.21 USD | `+1.07` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `1h` | `0.3371` | `0.3377` | `0.3307` | `0.3324` | `39,413,287` | 13,120,323.22 USD | 312,055.16 USD | `+2.38%` | -2,308,798.06 USD | `+0.21` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `1h` | `0.3324` | `0.3332` | `0.3320` | `0.3321` | `1,921,614` | 638,843.21 USD | -35,343.55 USD | `-5.53%` | -2,344,141.61 USD | `+0.05` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.3533` | `0.3608` | `0.3475` | `0.3495` | `257,452,106` | 91,407,782.04 USD | 2,108,185.60 USD | `+2.31%` | 4,840,432.56 USD | `+0.97` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `0.3495` | `0.3497` | `0.3310` | `0.3371` | `257,957,739` | 87,367,227.03 USD | -7,246,486.44 USD | `-8.29%` | -2,406,053.88 USD | `-1.94` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.3371` | `0.3377` | `0.3307` | `0.3321` | `41,331,315` | 13,757,975.60 USD | 277,891.15 USD | `+2.02%` | -2,128,162.73 USD | `+0.20` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `0.3314` | `0.3316` | `0.3310` | `0.3315` | `11,250,742` | 3,727,253.77 USD | 212,090.87 USD | `+5.69%` | 581,399.04 USD | `-1.00` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `0.3315` | `0.3653` | `0.3282` | `0.3533` | `793,774,795` | 276,969,161.06 USD | 2,150,847.92 USD | `+0.78%` | 2,732,246.96 USD | `+1.41` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `0.3533` | `0.3608` | `0.3475` | `0.3495` | `257,452,106` | 91,407,782.04 USD | 2,108,185.60 USD | `+2.31%` | 4,840,432.56 USD | `+0.97` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `0.3495` | `0.3497` | `0.3310` | `0.3371` | `257,957,739` | 87,367,227.03 USD | -7,246,486.44 USD | `-8.29%` | -2,406,053.88 USD | `-1.94` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.3371` | `0.3377` | `0.3307` | `0.3321` | `41,331,315` | 13,757,975.60 USD | 277,891.15 USD | `+2.02%` | -2,128,162.73 USD | `+0.20` | **`BULLISH`** | `BULLISH ABSORPTION` |

- **Deribit Institutional Options Max Pain & Volatility Surface (21_Tradfye_Orderflow.parquet)**:
  * Options Max Pain Price: `0.000000`
  * Call Wall Strike: `0.000000` | Put Wall Strike: `0.000000`

---

## 5. Institutional Whale Armor, Hyperdash Intel & L2 Depth Ladders
*(Sources: 10_Whale_Orders.parquet, 17_Orderbook.parquet, 12_Hyperdash.parquet, 13_Hyperliquid.parquet, 4_Hyperliquid_Analysis.parquet, 16_Hyperdash_telegram_Intel.parquet)*
- **Defending Resting Whale Walls (10_Whale_Orders.parquet)**:
  * Top Defending Bid Wall: `None` (Unarmored)
  * Top Defending Ask Wall: `None` (Unarmored)
| Side | Wall Price (USD) | Size (Coins) | Depth (USD) | Distance (%) | Persistence | Traded % | Venue | Order ID |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| --- | **`0.3325`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `MID` | Regular L2 Book | - | - | - | Interbank L2 | 0.00% | Interbank |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 14:32:27 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `1176` | `0xecb6...2b00` | `LONG` | 1,894,539.26 USD | `5,691,871.00` | `0.3343` | `0.3329` | `0.000000` | -8,523.46 USD | `-0.45%` | `10X Cross` |
| `1610` | `0xeadc...9d55` | `LONG` | 1,330,952.00 USD | `4,000,000.00` | `0.3421` | `0.3329` | `0.000000` | -37,526.09 USD | `-2.82%` | `10X Cross` |
| `1775` | `0x8dd7...fa30` | `SHORT` | 1,174,333.89 USD | `3,526,740.00` | `0.3327` | `0.3329` | `0.3959` | -1,006.22 USD | `-0.09%` | `6X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `0.3317` | 8,138.69 USD | `-` | `NEWS_INTEL` | `-` | #TRX Whale BUY: 8.14K USD at 0.3317 USD [API] | `2026-10-29 09:27:20` |
| `ANNOUNCEMENT` | `INFO` | `0.3316` | 7,871.14 USD | `-` | `NEWS_INTEL` | `-` | #TRX Whale BUY: 7.87K USD at 0.3316 USD [API] | `2026-10-29 10:14:22` |
| `ANNOUNCEMENT` | `INFO` | `0.3318` | 6,469.10 USD | `-` | `NEWS_INTEL` | `-` | #TRX Whale BUY: 6.47K USD at 0.3318 USD [API] | `2026-10-29 11:35:32` |
| `ANNOUNCEMENT` | `INFO` | `0.3318` | 9,999.82 USD | `-` | `NEWS_INTEL` | `-` | #TRX Whale BUY: 10.00K USD at 0.3318 USD [API] | `2026-10-29 11:35:32` |
| `ANNOUNCEMENT` | `INFO` | `0.3316` | 6,423.42 USD | `-` | `NEWS_INTEL` | `-` | #TRX Whale SELL: 6.42K USD at 0.3316 USD [API] | `2026-10-29 12:41:40` |
| `ANNOUNCEMENT` | `INFO` | `0.3318` | 6,464.73 USD | `-` | `NEWS_INTEL` | `-` | #TRX Whale SELL: 6.46K USD at 0.3318 USD [API] | `2026-10-29 13:28:43` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`0.3675` (Vol: 1,300,000.00 USD, Dist: `+10.73%`) | Long MP=`0.3298` (Vol: 509,400.00 USD, Dist: `--0.64%`)
  * 48H Horizon: Short MP=`0.3675` (Vol: 1,300,000.00 USD, Dist: `+10.73%`) | Long MP=`0.3249` (Vol: 724,200.00 USD, Dist: `--2.13%`)
  * 3D Horizon: Short MP=`0.3661` (Vol: 1,100,000.00 USD, Dist: `+10.31%`) | Long MP=`0.3248` (Vol: 842,600.00 USD, Dist: `--2.13%`)
  * 7D Horizon: Short MP=`0.3661` (Vol: 1,100,000.00 USD, Dist: `+10.31%`) | Long MP=`0.3248` (Vol: 1,000,000.00 USD, Dist: `--2.13%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long Liquidation` | `0.0775` | 3,170.00 USD | 1,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0795` | 7,010.00 USD | 1,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0845` | 120.67 USD | 1,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0865` | 179.83 USD | 1,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0925` | 918.15 USD | 1,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1145` | 2,290.00 USD | 1,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1165` | 391.44 USD | 1,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1315` | 10,100.00 USD | 1,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1515` | 48,430.00 USD | 1,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1575` | 6,470.00 USD | 1,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1585` | 388.01 USD | 1,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1655` | 496.50 USD | 1,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1675` | 36,640.00 USD | 1,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1685` | 20,120.00 USD | 1,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1695` | 3,390.00 USD | 1,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1725` | 11,100.00 USD | 1,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1735` | 339.71 USD | 1,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1745` | 5,280.00 USD | 1,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1755` | 1,430.00 USD | 1,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1765` | 333.06 USD | 1,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1775` | 207.50 USD | 1,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1815` | 100.37 USD | 1,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1875` | 36,310.00 USD | 1,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1975` | 632.00 USD | 1,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2155` | 194.81 USD | 1,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2165` | 2,000.00 USD | 1,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2175` | 227.29 USD | 1,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2185` | 512.82 USD | 1,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2245` | 4,570.00 USD | 1,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2285` | 111.97 USD | 1,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2295` | 2,070.00 USD | 1,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2305` | 410.06 USD | 1,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2325` | 2,040.00 USD | 1,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2335` | 797.64 USD | 1,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2345` | 5,700.00 USD | 1,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2355` | 3,130.00 USD | 996,250.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2365` | 686.56 USD | 993,110.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2375` | 568.81 USD | 992,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2395` | 1,570.00 USD | 991,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2415` | 139.35 USD | 990,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2435` | 885.85 USD | 990,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2445` | 3,380.00 USD | 989,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2455` | 384.94 USD | 985,890.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2485` | 11,890.00 USD | 985,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2505` | 262.02 USD | 973,610.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2555` | 1,220.00 USD | 973,350.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2575` | 301.79 USD | 972,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2595` | 749.18 USD | 971,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2625` | 108.15 USD | 971,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2645` | 2,650.00 USD | 970,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2655` | 193.02 USD | 968,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2675` | 321.54 USD | 968,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2685` | 3,150.00 USD | 967,800.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2745` | 84,690.00 USD | 964,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2785` | 13,010.00 USD | 879,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2795` | 6,260.00 USD | 866,940.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2805` | 605.32 USD | 860,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2815` | 15,010.00 USD | 860,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2825` | 1,730.00 USD | 845,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2855` | 6,660.00 USD | 843,340.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2865` | 4,150.00 USD | 836,680.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2905` | 821.82 USD | 832,540.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2915` | 954.37 USD | 831,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2935` | 213.08 USD | 830,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2945` | 124.87 USD | 830,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.2953` | 19,250,000.00 USD | 19,250,000.00 USD | 81,550.00 USD | 0.00 USD | 10,820.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.2955` | 156.61 USD | 830,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.2959` | 19,150,000.00 USD | 19,150,000.00 USD | 107,990.00 USD | 22,740.00 USD | 9,700.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.2965` | 19,010,000.00 USD | 19,010,000.00 USD | 123,420.00 USD | 38,150.00 USD | 60,970.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.2971` | 18,790,000.00 USD | 18,790,000.00 USD | 88,940.00 USD | 36,460.00 USD | 55,170.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.2973` | 12,090,000.00 USD | 12,090,000.00 USD | 185.60 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.2975` | 1,010.00 USD | 830,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.2977` | 12,090,000.00 USD | 12,090,000.00 USD | 13,210.00 USD | 3,650.00 USD | 4,240.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.2977` | 18,610,000.00 USD | 18,610,000.00 USD | 53,890.00 USD | 18,540.00 USD | 17,670.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.2981` | 12,070,000.00 USD | 12,070,000.00 USD | 12,230.00 USD | 6,300.00 USD | 14,550.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.2983` | 18,520,000.00 USD | 18,520,000.00 USD | 172,020.00 USD | 15,470.00 USD | 39,660.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.2985` | 12,040,000.00 USD | 12,040,000.00 USD | 112,860.00 USD | 13,480.00 USD | 13,660.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.2985` | 759.68 USD | 829,250.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.2989` | 11,900,000.00 USD | 11,900,000.00 USD | 24,270.00 USD | 0.00 USD | 8,790.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.2989` | 18,290,000.00 USD | 18,290,000.00 USD | 111,920.00 USD | 18,720.00 USD | 23,920.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.2993` | 11,870,000.00 USD | 11,870,000.00 USD | 10,310.00 USD | 25,460.00 USD | 56,800.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.2995` | 18,140,000.00 USD | 18,140,000.00 USD | 8,380.00 USD | 2,190.00 USD | 48,990.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.2995` | 197.37 USD | 828,490.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.2997` | 11,770,000.00 USD | 11,770,000.00 USD | 600.83 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3001` | 11,770,000.00 USD | 11,770,000.00 USD | 8,760.00 USD | 14,600.00 USD | 14,510.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3001` | 18,080,000.00 USD | 18,080,000.00 USD | 1,880.00 USD | 15,390.00 USD | 30,210.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3005` | 11,740,000.00 USD | 11,740,000.00 USD | 4,620.00 USD | 7,870.00 USD | 18,440.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3005` | 10,490.00 USD | 828,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.3007` | 18,030,000.00 USD | 18,030,000.00 USD | 13,780.00 USD | 2,960.00 USD | 22,100.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3009` | 11,710,000.00 USD | 11,710,000.00 USD | 23,780.00 USD | 3,410.00 USD | 16,090.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3013` | 11,660,000.00 USD | 11,660,000.00 USD | 0.00 USD | 3,170.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3013` | 17,990,000.00 USD | 17,990,000.00 USD | 2,700.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3015` | 128.44 USD | 817,810.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3017` | 11,660,000.00 USD | 11,660,000.00 USD | 1,010.00 USD | 8,490.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3019` | 17,990,000.00 USD | 17,990,000.00 USD | 0.00 USD | 8,660.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3021` | 11,650,000.00 USD | 11,650,000.00 USD | 14,850.00 USD | 4,540.00 USD | 16,590.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3025` | 11,610,000.00 USD | 11,610,000.00 USD | 2,600.00 USD | 2,050.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3025` | 17,980,000.00 USD | 17,980,000.00 USD | 0.00 USD | 9,860.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3025` | 2,620.00 USD | 817,680.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3029` | 11,610,000.00 USD | 11,610,000.00 USD | 24,570.00 USD | 0.00 USD | 6,190.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3031` | 17,970,000.00 USD | 17,970,000.00 USD | 50,940.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3033` | 11,580,000.00 USD | 11,580,000.00 USD | 1,070.00 USD | 2,750.00 USD | 12,600.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3035` | 266.47 USD | 815,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3037` | 11,560,000.00 USD | 11,560,000.00 USD | 517.67 USD | 3,230.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3041` | 11,560,000.00 USD | 11,560,000.00 USD | 537.63 USD | 9,300.00 USD | 56,350.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3045` | 11,490,000.00 USD | 11,490,000.00 USD | 0.00 USD | 13,170.00 USD | 7,480.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3045` | 138.24 USD | 814,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3049` | 11,470,000.00 USD | 11,470,000.00 USD | 31,710.00 USD | 11,440.00 USD | 42,260.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3049` | 17,920,000.00 USD | 17,920,000.00 USD | 18,870.00 USD | 0.00 USD | 66,870.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3053` | 11,390,000.00 USD | 11,390,000.00 USD | 46,990.00 USD | 15,890.00 USD | 49,310.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3055` | 17,840,000.00 USD | 17,840,000.00 USD | 1,250.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3055` | 14,670.00 USD | 814,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3061` | 11,270,000.00 USD | 11,270,000.00 USD | 885.25 USD | 2,350.00 USD | 56,460.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3061` | 17,830,000.00 USD | 17,830,000.00 USD | 32,690.00 USD | 7,690.00 USD | 37,210.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3065` | 11,210,000.00 USD | 11,210,000.00 USD | 29,570.00 USD | 26,740.00 USD | 35,690.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3067` | 17,760,000.00 USD | 17,760,000.00 USD | 5,220.00 USD | 8,110.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3069` | 11,120,000.00 USD | 11,120,000.00 USD | 1,540.00 USD | 2,880.00 USD | 12,760.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3073` | 11,100,000.00 USD | 11,100,000.00 USD | 23,280.00 USD | 1,940.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3073` | 17,740,000.00 USD | 17,740,000.00 USD | 9,190.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3075` | 6,650.00 USD | 799,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3077` | 11,080,000.00 USD | 11,080,000.00 USD | 350.20 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3079` | 17,730,000.00 USD | 17,730,000.00 USD | 37,430.00 USD | 10,270.00 USD | 50,200.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3081` | 11,080,000.00 USD | 11,080,000.00 USD | 18,400.00 USD | 0.00 USD | 12,250.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3085` | 11,050,000.00 USD | 11,050,000.00 USD | 340.09 USD | 0.00 USD | 15,810.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3085` | 17,640,000.00 USD | 17,640,000.00 USD | 2,870.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3085` | 291.53 USD | 793,340.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3089` | 11,030,000.00 USD | 11,030,000.00 USD | 550.01 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3091` | 17,630,000.00 USD | 17,630,000.00 USD | 12,490.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3093` | 11,030,000.00 USD | 11,030,000.00 USD | 14,750.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3095` | 192.51 USD | 793,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3097` | 11,020,000.00 USD | 11,020,000.00 USD | 610.25 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3097` | 17,620,000.00 USD | 17,620,000.00 USD | 83,130.00 USD | 3,620.00 USD | 54,360.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3101` | 11,020,000.00 USD | 11,020,000.00 USD | 41,340.00 USD | 15,820.00 USD | 46,470.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3103` | 17,480,000.00 USD | 17,480,000.00 USD | 67,180.00 USD | 0.00 USD | 63,310.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3105` | 10,910,000.00 USD | 10,910,000.00 USD | 21,200.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3105` | 820.96 USD | 792,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.3109` | 17,350,000.00 USD | 17,350,000.00 USD | 6,350.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3113` | 10,890,000.00 USD | 10,890,000.00 USD | 0.00 USD | 4,980.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3115` | 17,340,000.00 USD | 17,340,000.00 USD | 5,350.00 USD | 0.00 USD | 37,490.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3115` | 13,600.00 USD | 792,030.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3117` | 10,890,000.00 USD | 10,890,000.00 USD | 14,660.00 USD | 12,220.00 USD | 17,620.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3121` | 10,840,000.00 USD | 10,840,000.00 USD | 11,560.00 USD | 2,560.00 USD | 33,830.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3121` | 17,300,000.00 USD | 17,300,000.00 USD | 166,810.00 USD | 19,620.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3125` | 10,790,000.00 USD | 10,790,000.00 USD | 12,740.00 USD | 13,530.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3125` | 17,570.00 USD | 778,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.3127` | 17,110,000.00 USD | 17,110,000.00 USD | 16,750.00 USD | 54,460.00 USD | 57,690.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3129` | 10,770,000.00 USD | 10,770,000.00 USD | 3,480.00 USD | 28,470.00 USD | 29,100.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3133` | 10,710,000.00 USD | 10,710,000.00 USD | 4,020.00 USD | 23,940.00 USD | 9,590.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3133` | 16,980,000.00 USD | 16,980,000.00 USD | 3,990.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3135` | 681.55 USD | 760,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3137` | 10,670,000.00 USD | 10,670,000.00 USD | 4,590.00 USD | 10,610.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3139` | 16,980,000.00 USD | 16,980,000.00 USD | 2,940.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3141` | 10,650,000.00 USD | 10,650,000.00 USD | 6,900.00 USD | 0.00 USD | 9,540.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3145` | 10,640,000.00 USD | 10,640,000.00 USD | 1,910.00 USD | 5,900.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3145` | 16,980,000.00 USD | 16,980,000.00 USD | 247,620.00 USD | 51,270.00 USD | 17,870.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3145` | 116.05 USD | 760,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3149` | 10,630,000.00 USD | 10,630,000.00 USD | 1,380.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3151` | 16,660,000.00 USD | 16,660,000.00 USD | 206,090.00 USD | 23,130.00 USD | 49,320.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3153` | 10,630,000.00 USD | 10,630,000.00 USD | 19,960.00 USD | 25,600.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3155` | 1,370.00 USD | 760,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3157` | 10,580,000.00 USD | 10,580,000.00 USD | 11,820.00 USD | 1,830.00 USD | 16,240.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3157` | 16,380,000.00 USD | 16,380,000.00 USD | 393,090.00 USD | 93,740.00 USD | 60,300.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3161` | 10,550,000.00 USD | 10,550,000.00 USD | 3,620.00 USD | 2,990.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3163` | 15,830,000.00 USD | 15,830,000.00 USD | 483,870.00 USD | 182,370.00 USD | 192,840.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3165` | 10,550,000.00 USD | 10,550,000.00 USD | 45,260.00 USD | 30,980.00 USD | 9,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3165` | 2,360.00 USD | 758,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3169` | 10,460,000.00 USD | 10,460,000.00 USD | 1,090.00 USD | 10,820.00 USD | 20,780.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3169` | 14,980,000.00 USD | 14,980,000.00 USD | 403,830.00 USD | 106,680.00 USD | 142,240.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3173` | 10,430,000.00 USD | 10,430,000.00 USD | 25,580.00 USD | 33,870.00 USD | 27,630.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3175` | 14,320,000.00 USD | 14,320,000.00 USD | 146,800.00 USD | 53,470.00 USD | 69,280.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3175` | 4,060.00 USD | 756,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3177` | 10,340,000.00 USD | 10,340,000.00 USD | 46,680.00 USD | 8,980.00 USD | 30,890.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3181` | 10,250,000.00 USD | 10,250,000.00 USD | 279,630.00 USD | 48,980.00 USD | 76,070.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3181` | 14,050,000.00 USD | 14,050,000.00 USD | 743,630.00 USD | 76,910.00 USD | 182,330.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3185` | 9,850,000.00 USD | 9,850,000.00 USD | 153,270.00 USD | 52,920.00 USD | 51,330.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3185` | 642.10 USD | 752,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.3187` | 13,050,000.00 USD | 13,050,000.00 USD | 411,400.00 USD | 97,820.00 USD | 24,770.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3189` | 9,590,000.00 USD | 9,590,000.00 USD | 74,680.00 USD | 5,580.00 USD | 48,660.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3193` | 9,460,000.00 USD | 9,460,000.00 USD | 107,190.00 USD | 74,060.00 USD | 180,830.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3193` | 12,520,000.00 USD | 12,520,000.00 USD | 118,210.00 USD | 25,780.00 USD | 168,960.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3197` | 9,100,000.00 USD | 9,100,000.00 USD | 74,370.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3199` | 12,200,000.00 USD | 12,200,000.00 USD | 0.00 USD | 38,380.00 USD | 63,420.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3201` | 9,030,000.00 USD | 9,030,000.00 USD | 208,440.00 USD | 48,100.00 USD | 61,570.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3205` | 8,710,000.00 USD | 8,710,000.00 USD | 126,280.00 USD | 31,270.00 USD | 102,160.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3205` | 12,100,000.00 USD | 12,100,000.00 USD | 94,770.00 USD | 59,200.00 USD | 130,760.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3205` | 455.75 USD | 751,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3209` | 8,450,000.00 USD | 8,450,000.00 USD | 59,320.00 USD | 16,590.00 USD | 40,220.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3211` | 11,820,000.00 USD | 11,820,000.00 USD | 562,620.00 USD | 117,230.00 USD | 244,340.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3213` | 8,330,000.00 USD | 8,330,000.00 USD | 914.92 USD | 30,340.00 USD | 107,830.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3217` | 8,190,000.00 USD | 8,190,000.00 USD | 5,550.00 USD | 33,860.00 USD | 70,540.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3217` | 10,890,000.00 USD | 10,890,000.00 USD | 284,850.00 USD | 58,690.00 USD | 107,900.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3221` | 8,080,000.00 USD | 8,080,000.00 USD | 97,480.00 USD | 25,650.00 USD | 72,520.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3223` | 10,440,000.00 USD | 10,440,000.00 USD | 643,460.00 USD | 196,690.00 USD | 103,370.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3225` | 7,890,000.00 USD | 7,890,000.00 USD | 70,750.00 USD | 19,600.00 USD | 202,490.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3229` | 7,600,000.00 USD | 7,600,000.00 USD | 91,010.00 USD | 46,020.00 USD | 86,810.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3229` | 9,500,000.00 USD | 9,500,000.00 USD | 859,960.00 USD | 299,190.00 USD | 385,680.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3233` | 7,370,000.00 USD | 7,370,000.00 USD | 56,470.00 USD | 13,130.00 USD | 49,900.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3235` | 7,950,000.00 USD | 7,950,000.00 USD | 709,160.00 USD | 213,370.00 USD | 371,680.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3235` | 128.43 USD | 751,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3237` | 7,250,000.00 USD | 7,250,000.00 USD | 6,420.00 USD | 74,740.00 USD | 171,270.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3241` | 7,000,000.00 USD | 7,000,000.00 USD | 966.93 USD | 27,720.00 USD | 119,400.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3241` | 6,660,000.00 USD | 6,660,000.00 USD | 432,660.00 USD | 149,860.00 USD | 138,560.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3245` | 6,850,000.00 USD | 6,850,000.00 USD | 248,280.00 USD | 54,650.00 USD | 216,640.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3247` | 5,940,000.00 USD | 5,940,000.00 USD | 849,100.00 USD | 127,310.00 USD | 353,590.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3249` | 6,330,000.00 USD | 6,330,000.00 USD | 835,170.00 USD | 107,030.00 USD | 192,010.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3253` | 5,200,000.00 USD | 5,200,000.00 USD | 194,860.00 USD | 95,420.00 USD | 373,460.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3253` | 4,610,000.00 USD | 4,610,000.00 USD | 1,220,000.00 USD | 137,440.00 USD | 241,690.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3257` | 4,530,000.00 USD | 4,530,000.00 USD | 312,250.00 USD | 43,390.00 USD | 229,640.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3259` | 3,010,000.00 USD | 3,010,000.00 USD | 182,240.00 USD | 92,250.00 USD | 346,980.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3261` | 3,950,000.00 USD | 3,950,000.00 USD | 79,940.00 USD | 151,680.00 USD | 319,940.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3265` | 3,400,000.00 USD | 3,400,000.00 USD | 43,780.00 USD | 72,290.00 USD | 141,160.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3265` | 2,390,000.00 USD | 2,390,000.00 USD | 79,990.00 USD | 19,240.00 USD | 93,040.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3269` | 3,140,000.00 USD | 3,140,000.00 USD | 124,870.00 USD | 143,860.00 USD | 378,850.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3271` | 2,190,000.00 USD | 2,190,000.00 USD | 189,530.00 USD | 138,680.00 USD | 261,530.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3273` | 2,490,000.00 USD | 2,490,000.00 USD | 38,550.00 USD | 24,720.00 USD | 174,670.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3275` | 163.42 USD | 751,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3277` | 2,250,000.00 USD | 2,250,000.00 USD | 260,400.00 USD | 46,830.00 USD | 133,800.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3277` | 1,600,000.00 USD | 1,600,000.00 USD | 0.00 USD | 29,390.00 USD | 85,620.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3281` | 1,810,000.00 USD | 1,810,000.00 USD | 0.00 USD | 57,800.00 USD | 16,760.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3283` | 1,490,000.00 USD | 1,490,000.00 USD | 89,030.00 USD | 25,670.00 USD | 275,050.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3285` | 1,740,000.00 USD | 1,740,000.00 USD | 0.00 USD | 48,460.00 USD | 30,620.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3285` | 745,260.00 USD | 750,880.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3289` | 1,660,000.00 USD | 1,660,000.00 USD | 155,850.00 USD | 6,250.00 USD | 155,080.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3289` | 1,100,000.00 USD | 1,100,000.00 USD | 2,520.00 USD | 43,290.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3293` | 1,340,000.00 USD | 1,340,000.00 USD | 977.29 USD | 32,950.00 USD | 80,060.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3295` | 1,050,000.00 USD | 1,050,000.00 USD | 254,700.00 USD | 83,080.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3295` | 839.90 USD | 5,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3297` | 1,230,000.00 USD | 1,230,000.00 USD | 166,310.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3301` | 1,060,000.00 USD | 1,060,000.00 USD | 36,460.00 USD | 13,760.00 USD | 30,950.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3301` | 716,630.00 USD | 716,630.00 USD | 184,120.00 USD | 9,050.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3305` | 981,540.00 USD | 981,540.00 USD | 112,020.00 USD | 16,160.00 USD | 74,690.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3307` | 523,460.00 USD | 523,460.00 USD | 167,950.00 USD | 10,690.00 USD | 294,170.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3309` | 778,660.00 USD | 778,660.00 USD | 11,600.00 USD | 48,170.00 USD | 444,920.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3313` | 273,960.00 USD | 273,960.00 USD | 0.00 USD | 128,440.00 USD | 86,570.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3313` | 50,650.00 USD | 50,650.00 USD | 0.00 USD | 50,650.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3315` | 4,780.00 USD | 4,780.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3317` | 58,950.00 USD | 58,950.00 USD | 0.00 USD | 58,950.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3319` | 57,890.00 USD | 57,890.00 USD | 0.00 USD | 57,890.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3357` | 144,280.00 USD | 144,280.00 USD | 0.00 USD | 0.00 USD | 144,280.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3369` | 217,200.00 USD | 217,200.00 USD | 72,920.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3377` | 546,840.00 USD | 546,840.00 USD | 329,640.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3379` | 79,280.00 USD | 79,280.00 USD | 0.00 USD | 21,390.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3381` | 618,740.00 USD | 618,740.00 USD | 71,900.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3385` | 657,930.00 USD | 657,930.00 USD | 0.00 USD | 11,160.00 USD | 28,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3385` | 204,930.00 USD | 204,930.00 USD | 125,650.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3389` | 825,160.00 USD | 825,160.00 USD | 139,840.00 USD | 0.00 USD | 27,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3391` | 439,600.00 USD | 439,600.00 USD | 0.00 USD | 0.00 USD | 234,660.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3393` | 1,340,000.00 USD | 1,340,000.00 USD | 52,860.00 USD | 141,880.00 USD | 319,940.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3397` | 1,370,000.00 USD | 1,370,000.00 USD | 27,080.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3397` | 948,010.00 USD | 948,010.00 USD | 257,550.00 USD | 250,860.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3401` | 1,620,000.00 USD | 1,620,000.00 USD | 43,780.00 USD | 83,470.00 USD | 130,150.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3403` | 2,340,000.00 USD | 2,340,000.00 USD | 1,070,000.00 USD | 103,630.00 USD | 223,390.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3405` | 2,090,000.00 USD | 2,090,000.00 USD | 134,550.00 USD | 14,270.00 USD | 319,770.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3409` | 2,230,000.00 USD | 2,230,000.00 USD | 126,850.00 USD | 9,200.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3409` | 2,820,000.00 USD | 2,820,000.00 USD | 0.00 USD | 29,390.00 USD | 446,990.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3413` | 2,490,000.00 USD | 2,490,000.00 USD | 173,130.00 USD | 11,360.00 USD | 80,830.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3415` | 2,900,000.00 USD | 2,900,000.00 USD | 0.00 USD | 0.00 USD | 85,620.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3417` | 3,150,000.00 USD | 3,150,000.00 USD | 585,390.00 USD | 25,060.00 USD | 44,630.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3421` | 3,260,000.00 USD | 3,260,000.00 USD | 71,180.00 USD | 39,260.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3421` | 2,950,000.00 USD | 2,950,000.00 USD | 0.00 USD | 43,290.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3425` | 3,390,000.00 USD | 3,390,000.00 USD | 0.00 USD | 132,230.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3427` | 3,040,000.00 USD | 3,040,000.00 USD | 0.00 USD | 92,380.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3429` | 3,560,000.00 USD | 3,560,000.00 USD | 60,980.00 USD | 104,590.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3433` | 3,840,000.00 USD | 3,840,000.00 USD | 105,330.00 USD | 149,150.00 USD | 30,950.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3433` | 3,290,000.00 USD | 3,290,000.00 USD | 254,700.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3437` | 3,970,000.00 USD | 3,970,000.00 USD | 0.00 USD | 63,370.00 USD | 62,980.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3441` | 4,010,000.00 USD | 4,010,000.00 USD | 0.00 USD | 36,240.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3445` | 4,140,000.00 USD | 4,140,000.00 USD | 0.00 USD | 28,520.00 USD | 106,240.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3445` | 3,400,000.00 USD | 3,400,000.00 USD | 103,130.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3449` | 4,360,000.00 USD | 4,360,000.00 USD | 35,950.00 USD | 92,440.00 USD | 86,570.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3451` | 3,490,000.00 USD | 3,490,000.00 USD | 62,830.00 USD | 28,550.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3453` | 4,580,000.00 USD | 4,580,000.00 USD | 92,350.00 USD | 47,460.00 USD | 84,370.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3457` | 5,110,000.00 USD | 5,110,000.00 USD | 48,240.00 USD | 33,930.00 USD | 452,590.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3457` | 3,850,000.00 USD | 3,850,000.00 USD | 0.00 USD | 29,340.00 USD | 332,190.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3461` | 5,490,000.00 USD | 5,490,000.00 USD | 168,310.00 USD | 71,330.00 USD | 135,270.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3465` | 5,540,000.00 USD | 5,540,000.00 USD | 21,890.00 USD | 25,190.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3469` | 5,650,000.00 USD | 5,650,000.00 USD | 0.00 USD | 42,550.00 USD | 75,450.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3469` | 4,040,000.00 USD | 4,040,000.00 USD | 60,310.00 USD | 51,820.00 USD | 75,520.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3473` | 5,720,000.00 USD | 5,720,000.00 USD | 0.00 USD | 35,130.00 USD | 31,160.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3475` | 4,080,000.00 USD | 4,080,000.00 USD | 0.00 USD | 40,540.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3477` | 5,840,000.00 USD | 5,840,000.00 USD | 23,470.00 USD | 36,050.00 USD | 63,820.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3481` | 5,940,000.00 USD | 5,940,000.00 USD | 0.00 USD | 29,570.00 USD | 64,980.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3481` | 4,160,000.00 USD | 4,160,000.00 USD | 19,060.00 USD | 14,700.00 USD | 42,810.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3485` | 5,950,000.00 USD | 5,950,000.00 USD | 0.00 USD | 16,180.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3487` | 4,180,000.00 USD | 4,180,000.00 USD | 6,050.00 USD | 21,650.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3489` | 6,070,000.00 USD | 6,070,000.00 USD | 41,500.00 USD | 16,070.00 USD | 61,240.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3493` | 6,100,000.00 USD | 6,100,000.00 USD | 3,620.00 USD | 19,600.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3493` | 4,210,000.00 USD | 4,210,000.00 USD | 5,810.00 USD | 24,660.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3497` | 6,580,000.00 USD | 6,580,000.00 USD | 32,290.00 USD | 0.00 USD | 454,680.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3499` | 4,340,000.00 USD | 4,340,000.00 USD | 127,350.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3501` | 6,690,000.00 USD | 6,690,000.00 USD | 52,670.00 USD | 0.00 USD | 50,760.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3505` | 6,800,000.00 USD | 6,800,000.00 USD | 74,220.00 USD | 6,880.00 USD | 31,490.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3505` | 4,350,000.00 USD | 4,350,000.00 USD | 5,650.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3509` | 6,810,000.00 USD | 6,810,000.00 USD | 1,700.00 USD | 12,400.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3511` | 5,320,000.00 USD | 5,320,000.00 USD | 704,750.00 USD | 0.00 USD | 271,800.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3513` | 6,890,000.00 USD | 6,890,000.00 USD | 0.00 USD | 0.00 USD | 76,540.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3517` | 6,970,000.00 USD | 6,970,000.00 USD | 21,910.00 USD | 5,720.00 USD | 52,910.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3517` | 5,330,000.00 USD | 5,330,000.00 USD | 7,560.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3521` | 7,040,000.00 USD | 7,040,000.00 USD | 32,770.00 USD | 21,980.00 USD | 18,700.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3523` | 5,750,000.00 USD | 5,750,000.00 USD | 279,190.00 USD | 28,950.00 USD | 107,430.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3525` | 7,080,000.00 USD | 7,080,000.00 USD | 3,970.00 USD | 6,280.00 USD | 28,910.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3529` | 7,240,000.00 USD | 7,240,000.00 USD | 102,610.00 USD | 52,710.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3529` | 5,750,000.00 USD | 5,750,000.00 USD | 2,170.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3533` | 7,440,000.00 USD | 7,440,000.00 USD | 67,090.00 USD | 44,040.00 USD | 88,110.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3535` | 6,030,000.00 USD | 6,030,000.00 USD | 11,650.00 USD | 77,960.00 USD | 187,450.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3537` | 7,720,000.00 USD | 7,720,000.00 USD | 61,430.00 USD | 29,120.00 USD | 195,270.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3541` | 7,880,000.00 USD | 7,880,000.00 USD | 76,770.00 USD | 80,430.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3541` | 6,950,000.00 USD | 6,950,000.00 USD | 808,160.00 USD | 118,370.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3545` | 8,000,000.00 USD | 8,000,000.00 USD | 4,630.00 USD | 44,140.00 USD | 69,820.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3547` | 7,240,000.00 USD | 7,240,000.00 USD | 0.00 USD | 0.00 USD | 288,450.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3549` | 8,060,000.00 USD | 8,060,000.00 USD | 5,680.00 USD | 53,970.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3553` | 8,150,000.00 USD | 8,150,000.00 USD | 21,530.00 USD | 24,430.00 USD | 47,950.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3553` | 7,360,000.00 USD | 7,360,000.00 USD | 4,360.00 USD | 117,050.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3557` | 8,190,000.00 USD | 8,190,000.00 USD | 0.00 USD | 38,770.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3559` | 7,370,000.00 USD | 7,370,000.00 USD | 4,230.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3561` | 8,320,000.00 USD | 8,320,000.00 USD | 331.60 USD | 25,000.00 USD | 106,140.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3565` | 8,380,000.00 USD | 8,380,000.00 USD | 2,250.00 USD | 11,630.00 USD | 39,520.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3565` | 7,410,000.00 USD | 7,410,000.00 USD | 0.00 USD | 43,060.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3569` | 8,390,000.00 USD | 8,390,000.00 USD | 1,450.00 USD | 6,920.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3571` | 7,420,000.00 USD | 7,420,000.00 USD | 8,530.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3573` | 8,530,000.00 USD | 8,530,000.00 USD | 131,970.00 USD | 9,250.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3577` | 8,570,000.00 USD | 8,570,000.00 USD | 31,460.00 USD | 9,130.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3577` | 7,540,000.00 USD | 7,540,000.00 USD | 124,630.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3581` | 8,610,000.00 USD | 8,610,000.00 USD | 3,560.00 USD | 0.00 USD | 38,950.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3583` | 7,680,000.00 USD | 7,680,000.00 USD | 0.00 USD | 0.00 USD | 135,900.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3585` | 8,640,000.00 USD | 8,640,000.00 USD | 18,570.00 USD | 14,930.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3589` | 8,660,000.00 USD | 8,660,000.00 USD | 3,780.00 USD | 15,750.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3589` | 8,050,000.00 USD | 8,050,000.00 USD | 1,610.00 USD | 50,650.00 USD | 320,430.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3593` | 8,860,000.00 USD | 8,860,000.00 USD | 66,040.00 USD | 0.00 USD | 133,180.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3595` | 8,200,000.00 USD | 8,200,000.00 USD | 0.00 USD | 0.00 USD | 146,290.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3597` | 8,970,000.00 USD | 8,970,000.00 USD | 91,900.00 USD | 12,460.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3601` | 9,170,000.00 USD | 9,170,000.00 USD | 1,160.00 USD | 36,520.00 USD | 163,110.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3601` | 8,700,000.00 USD | 8,700,000.00 USD | 0.00 USD | 161,200.00 USD | 338,540.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3605` | 9,360,000.00 USD | 9,360,000.00 USD | 61,130.00 USD | 32,860.00 USD | 94,650.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3607` | 9,090,000.00 USD | 9,090,000.00 USD | 325,970.00 USD | 68,030.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3609` | 9,590,000.00 USD | 9,590,000.00 USD | 75,090.00 USD | 25,740.00 USD | 133,760.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3613` | 9,860,000.00 USD | 9,860,000.00 USD | 10,940.00 USD | 59,640.00 USD | 203,600.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3613` | 9,780,000.00 USD | 9,780,000.00 USD | 73,540.00 USD | 330,040.00 USD | 288,930.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3615` | 743.61 USD | 743.61 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.3617` | 10,240,000.00 USD | 10,240,000.00 USD | 225,600.00 USD | 50,630.00 USD | 104,310.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3619` | 9,990,000.00 USD | 9,990,000.00 USD | 0.00 USD | 209,940.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3621` | 10,540,000.00 USD | 10,540,000.00 USD | 143,010.00 USD | 75,820.00 USD | 71,510.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3625` | 10,680,000.00 USD | 10,680,000.00 USD | 99,950.00 USD | 49,330.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3625` | 10,190,000.00 USD | 10,190,000.00 USD | 0.00 USD | 191,880.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3629` | 11,920,000.00 USD | 11,920,000.00 USD | 1,120,000.00 USD | 35,410.00 USD | 79,610.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3631` | 10,300,000.00 USD | 10,300,000.00 USD | 0.00 USD | 114,740.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3633` | 12,330,000.00 USD | 12,330,000.00 USD | 144,090.00 USD | 72,670.00 USD | 199,780.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3635` | 31,260.00 USD | 32,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.3637` | 12,580,000.00 USD | 12,580,000.00 USD | 183,690.00 USD | 65,110.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3637` | 10,320,000.00 USD | 10,320,000.00 USD | 1,540.00 USD | 21,530.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3641` | 12,950,000.00 USD | 12,950,000.00 USD | 85,150.00 USD | 206,820.00 USD | 76,240.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3643` | 11,120,000.00 USD | 11,120,000.00 USD | 3,350.00 USD | 0.00 USD | 789,140.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3645` | 13,260,000.00 USD | 13,260,000.00 USD | 255,500.00 USD | 16,650.00 USD | 35,280.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3645` | 12,390.00 USD | 44,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.3649` | 13,610,000.00 USD | 13,610,000.00 USD | 95,770.00 USD | 59,680.00 USD | 195,820.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3649` | 11,300,000.00 USD | 11,300,000.00 USD | 181,300.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3653` | 14,100,000.00 USD | 14,100,000.00 USD | 301,080.00 USD | 19,500.00 USD | 165,330.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3655` | 12,090,000.00 USD | 12,090,000.00 USD | 679,620.00 USD | 112,770.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3657` | 14,590,000.00 USD | 14,590,000.00 USD | 186,020.00 USD | 149,310.00 USD | 163,370.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3661` | 14,980,000.00 USD | 14,980,000.00 USD | 265,410.00 USD | 55,900.00 USD | 67,180.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3661` | 12,980,000.00 USD | 12,980,000.00 USD | 687,450.00 USD | 0.00 USD | 207,150.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3665` | 15,610,000.00 USD | 15,610,000.00 USD | 468,570.00 USD | 113,200.00 USD | 49,800.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3665` | 1,160.00 USD | 45,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.3667` | 13,520,000.00 USD | 13,520,000.00 USD | 422,000.00 USD | 15,390.00 USD | 103,350.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3669` | 16,020,000.00 USD | 16,020,000.00 USD | 98,960.00 USD | 26,330.00 USD | 281,260.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3673` | 16,320,000.00 USD | 16,320,000.00 USD | 41,260.00 USD | 102,840.00 USD | 158,510.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3673` | 14,210,000.00 USD | 14,210,000.00 USD | 511,100.00 USD | 53,040.00 USD | 122,410.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3675` | 1,960.00 USD | 47,520.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.3677` | 17,040,000.00 USD | 17,040,000.00 USD | 483,210.00 USD | 36,750.00 USD | 191,130.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3679` | 14,470,000.00 USD | 14,470,000.00 USD | 257,550.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3681` | 17,520,000.00 USD | 17,520,000.00 USD | 293,500.00 USD | 87,330.00 USD | 103,470.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3685` | 18,070,000.00 USD | 18,070,000.00 USD | 327,450.00 USD | 152,380.00 USD | 74,230.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3685` | 14,650,000.00 USD | 14,650,000.00 USD | 2,700.00 USD | 102,650.00 USD | 72,350.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3689` | 18,590,000.00 USD | 18,590,000.00 USD | 404,300.00 USD | 56,330.00 USD | 52,150.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3691` | 15,060,000.00 USD | 15,060,000.00 USD | 148,800.00 USD | 261,530.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3693` | 18,690,000.00 USD | 18,690,000.00 USD | 79,910.00 USD | 4,540.00 USD | 23,760.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3697` | 18,930,000.00 USD | 18,930,000.00 USD | 155,550.00 USD | 83,650.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3697` | 15,220,000.00 USD | 15,220,000.00 USD | 736.13 USD | 163,180.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3701` | 19,690,000.00 USD | 19,690,000.00 USD | 527,250.00 USD | 196,170.00 USD | 27,870.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3703` | 15,270,000.00 USD | 15,270,000.00 USD | 50,940.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3705` | 20,500,000.00 USD | 20,500,000.00 USD | 249,050.00 USD | 2,750.00 USD | 560,920.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3705` | 278.99 USD | 47,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.3709` | 20,640,000.00 USD | 20,640,000.00 USD | 109,790.00 USD | 24,570.00 USD | 12,600.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3713` | 22,020,000.00 USD | 22,020,000.00 USD | 481,930.00 USD | 90,010.00 USD | 804,260.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3715` | 15,670,000.00 USD | 15,670,000.00 USD | 1,320.00 USD | 0.00 USD | 394,570.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3715` | 179.43 USD | 47,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.3717` | 22,540,000.00 USD | 22,540,000.00 USD | 44,520.00 USD | 220,760.00 USD | 250,340.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3721` | 22,680,000.00 USD | 22,680,000.00 USD | 0.00 USD | 62,750.00 USD | 85,090.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3721` | 16,420,000.00 USD | 16,420,000.00 USD | 5,330.00 USD | 0.00 USD | 747,740.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3725` | 23,740,000.00 USD | 23,740,000.00 USD | 504,840.00 USD | 31,730.00 USD | 517,550.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3725` | 186.25 USD | 48,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.3726` | 23,790,000.00 USD | 23,790,000.00 USD | 0.00 USD | 0.00 USD | 50,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3727` | 16,700,000.00 USD | 16,700,000.00 USD | 213,190.00 USD | 0.00 USD | 66,870.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3733` | 16,890,000.00 USD | 16,890,000.00 USD | 188,670.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3735` | 7,210.00 USD | 55,370.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.3739` | 17,360,000.00 USD | 17,360,000.00 USD | 241,260.00 USD | 7,690.00 USD | 218,010.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3745` | 17,760,000.00 USD | 17,760,000.00 USD | 248,660.00 USD | 115,430.00 USD | 37,210.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3755` | 6,120.00 USD | 61,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.3757` | 18,060,000.00 USD | 18,060,000.00 USD | 535.97 USD | 0.00 USD | 302,240.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3763` | 18,240,000.00 USD | 18,240,000.00 USD | 35,610.00 USD | 92,380.00 USD | 50,200.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3769` | 18,240,000.00 USD | 18,240,000.00 USD | 1,160.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3775` | 104.19 USD | 61,590.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.3781` | 18,270,000.00 USD | 18,270,000.00 USD | 29,330.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3785` | 556,430.00 USD | 618,010.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.3787` | 18,420,000.00 USD | 18,420,000.00 USD | 89,270.00 USD | 3,620.00 USD | 54,360.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3793` | 18,880,000.00 USD | 18,880,000.00 USD | 27,760.00 USD | 0.00 USD | 437,170.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3805` | 18,880,000.00 USD | 18,880,000.00 USD | 768.95 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3811` | 18,920,000.00 USD | 18,920,000.00 USD | 0.00 USD | 0.00 USD | 37,490.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3817` | 19,100,000.00 USD | 19,100,000.00 USD | 156,690.00 USD | 19,620.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3823` | 19,210,000.00 USD | 19,210,000.00 USD | 0.00 USD | 54,460.00 USD | 57,690.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3829` | 19,210,000.00 USD | 19,210,000.00 USD | 1,750.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3835` | 115.05 USD | 618,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.3841` | 19,210,000.00 USD | 19,210,000.00 USD | 897.53 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3859` | 19,280,000.00 USD | 19,280,000.00 USD | 70,850.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3865` | 19,440,000.00 USD | 19,440,000.00 USD | 112,700.00 USD | 45,110.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3865` | 265.53 USD | 618,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.3877` | 19,560,000.00 USD | 19,560,000.00 USD | 123,270.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3883` | 19,610,000.00 USD | 19,610,000.00 USD | 0.00 USD | 0.00 USD | 48,960.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3889` | 19,710,000.00 USD | 19,710,000.00 USD | 103,020.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3895` | 19,760,000.00 USD | 19,760,000.00 USD | 2,670.00 USD | 41,060.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3895` | 4,760.00 USD | 623,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.3901` | 19,820,000.00 USD | 19,820,000.00 USD | 59,060.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3905` | 6,000.00 USD | 629,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.3907` | 19,930,000.00 USD | 19,930,000.00 USD | 0.00 USD | 50,210.00 USD | 63,420.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3925` | 20,090,000.00 USD | 20,090,000.00 USD | 342.70 USD | 1,190.00 USD | 157,830.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3931` | 20,120,000.00 USD | 20,120,000.00 USD | 24,850.00 USD | 2,840.00 USD | 2,800.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3935` | 1,480.00 USD | 630,640.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.3937` | 20,150,000.00 USD | 20,150,000.00 USD | 22,060.00 USD | 1,070.00 USD | 5,410.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3943` | 20,180,000.00 USD | 20,180,000.00 USD | 24,300.00 USD | 3,090.00 USD | 784.19 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3945` | 118,130.00 USD | 748,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.3949` | 20,310,000.00 USD | 20,310,000.00 USD | 110,580.00 USD | 8,290.00 USD | 18,490.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3955` | 20,540,000.00 USD | 20,540,000.00 USD | 106,740.00 USD | 10,160.00 USD | 112,040.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3961` | 20,730,000.00 USD | 20,730,000.00 USD | 122,580.00 USD | 54,030.00 USD | 7,040.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3967` | 20,750,000.00 USD | 20,750,000.00 USD | 12,270.00 USD | 6,010.00 USD | 4,840.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3973` | 20,890,000.00 USD | 20,890,000.00 USD | 16,620.00 USD | 1,440.00 USD | 123,860.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3979` | 21,000,000.00 USD | 21,000,000.00 USD | 57,520.00 USD | 38,460.00 USD | 11,500.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3985` | 21,040,000.00 USD | 21,040,000.00 USD | 23,360.00 USD | 3,160.00 USD | 10,200.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3991` | 21,060,000.00 USD | 21,060,000.00 USD | 0.00 USD | 1,100.00 USD | 24,490.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.4001` | 21,070,000.00 USD | 21,070,000.00 USD | 0.00 USD | 7,690.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.4085` | 170.75 USD | 748,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4095` | 239.56 USD | 749,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4185` | 1,130.00 USD | 750,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4295` | 10,210.00 USD | 760,520.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4305` | 1,490.00 USD | 762,010.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4315` | 5,480.00 USD | 767,490.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4365` | 72,540.00 USD | 840,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4415` | 377.48 USD | 840,410.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4445` | 22,230.00 USD | 862,640.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4465` | 1,020.00 USD | 863,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4475` | 65,610.00 USD | 929,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4515` | 318.76 USD | 929,590.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4525` | 570.15 USD | 930,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4625` | 267.32 USD | 930,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4705` | 282,390.00 USD | 1,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4805` | 2,880.00 USD | 1,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4895` | 839.49 USD | 1,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4905` | 5,120.00 USD | 1,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4995` | 2,730.00 USD | 1,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.5015` | 23,370.00 USD | 1,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.5335` | 668.48 USD | 1,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.5545` | 41,030.00 USD | 1,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.5575` | 740.92 USD | 1,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.5585` | 2,320.00 USD | 1,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.5615` | 140.38 USD | 1,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.5685` | 737,490.00 USD | 2,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.6135` | 371.17 USD | 2,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.6145` | 3,920.00 USD | 2,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.6155` | 24,620.00 USD | 2,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.6215` | 793.03 USD | 2,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.6275` | 1,130.00 USD | 2,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.6345` | 6,820.00 USD | 2,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.6515` | 103,110.00 USD | 2,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.6545` | 706.21 USD | 2,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.6615` | 2,060.00 USD | 2,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.6635` | 3,740.00 USD | 2,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `0.0735` | 1,240,000.00 USD | 0.00 USD | 3,000.00 USD | `-77.94%` | `40,871.00` |
| `Live` | `Long` | `0.0755` | 1,240,000.00 USD | 0.00 USD | 6,660.00 USD | `-77.34%` | `88,233.00` |
| `Live` | `Long` | `0.0865` | 1,230,000.00 USD | 0.00 USD | 858.60 USD | `-74.03%` | `9,926.00` |
| `Live` | `Long` | `0.0875` | 1,230,000.00 USD | 0.00 USD | 181.91 USD | `-73.73%` | `2,079.00` |
| `Live` | `Long` | `0.0985` | 1,230,000.00 USD | 0.00 USD | 964.61 USD | `-70.43%` | `9,793.00` |
| `Live` | `Long` | `0.1065` | 1,230,000.00 USD | 0.00 USD | 152.08 USD | `-68.03%` | `1,428.00` |
| `Live` | `Long` | `0.1145` | 1,230,000.00 USD | 0.00 USD | 2,290.00 USD | `-65.63%` | `20,000.00` |
| `Live` | `Long` | `0.1155` | 1,230,000.00 USD | 0.00 USD | 265.88 USD | `-65.33%` | `2,302.00` |
| `Live` | `Long` | `0.1165` | 1,230,000.00 USD | 0.00 USD | 123.26 USD | `-65.03%` | `1,058.00` |
| `Live` | `Long` | `0.1285` | 1,230,000.00 USD | 0.00 USD | 9,870.00 USD | `-61.43%` | `76,797.00` |
| `Live` | `Long` | `0.1585` | 1,220,000.00 USD | 0.00 USD | 388.01 USD | `-52.42%` | `2,448.00` |
| `Live` | `Long` | `0.1625` | 1,220,000.00 USD | 0.00 USD | 6,680.00 USD | `-51.22%` | `41,100.00` |
| `Live` | `Long` | `0.1675` | 1,210,000.00 USD | 0.00 USD | 57,490.00 USD | `-49.72%` | `343,214.00` |
| `Live` | `Long` | `0.1685` | 1,150,000.00 USD | 0.00 USD | 23,990.00 USD | `-49.42%` | `142,400.00` |
| `Live` | `Long` | `0.1715` | 1,130,000.00 USD | 0.00 USD | 648.96 USD | `-48.52%` | `3,784.00` |
| `Live` | `Long` | `0.1725` | 1,130,000.00 USD | 0.00 USD | 48,180.00 USD | `-48.22%` | `279,283.00` |
| `Live` | `Long` | `0.1735` | 1,080,000.00 USD | 0.00 USD | 339.71 USD | `-47.92%` | `1,958.00` |
| `Live` | `Long` | `0.1745` | 1,080,000.00 USD | 0.00 USD | 5,170.00 USD | `-47.62%` | `29,642.00` |
| `Live` | `Long` | `0.1755` | 1,070,000.00 USD | 0.00 USD | 255.53 USD | `-47.32%` | `1,456.00` |
| `Live` | `Long` | `0.1765` | 1,070,000.00 USD | 0.00 USD | 278.69 USD | `-47.02%` | `1,579.00` |
| `Live` | `Long` | `0.1775` | 1,070,000.00 USD | 0.00 USD | 1,400.00 USD | `-46.72%` | `7,875.00` |
| `Live` | `Long` | `0.1815` | 1,070,000.00 USD | 0.00 USD | 263.54 USD | `-45.52%` | `1,452.00` |
| `Live` | `Long` | `0.1875` | 1,070,000.00 USD | 0.00 USD | 36,310.00 USD | `-43.71%` | `193,636.00` |
| `Live` | `Long` | `0.1975` | 1,040,000.00 USD | 0.00 USD | 632.00 USD | `-40.71%` | `3,200.00` |
| `Live` | `Long` | `0.2165` | 1,030,000.00 USD | 0.00 USD | 1,520.00 USD | `-35.01%` | `7,003.00` |
| `Live` | `Long` | `0.2185` | 1,030,000.00 USD | 0.00 USD | 1,000.00 USD | `-34.41%` | `4,583.00` |
| `Live` | `Long` | `0.2205` | 1,030,000.00 USD | 0.00 USD | 230.42 USD | `-33.81%` | `1,045.00` |
| `Live` | `Long` | `0.2225` | 1,030,000.00 USD | 0.00 USD | 201.14 USD | `-33.21%` | `904.00` |
| `Live` | `Long` | `0.2245` | 1,030,000.00 USD | 0.00 USD | 4,570.00 USD | `-32.61%` | `20,360.00` |
| `Live` | `Long` | `0.2295` | 1,030,000.00 USD | 0.00 USD | 2,070.00 USD | `-31.11%` | `9,004.00` |
| `Live` | `Long` | `0.2305` | 1,030,000.00 USD | 0.00 USD | 410.06 USD | `-30.81%` | `1,779.00` |
| `Live` | `Long` | `0.2325` | 1,020,000.00 USD | 0.00 USD | 2,420.00 USD | `-30.21%` | `10,412.00` |
| `Live` | `Long` | `0.2335` | 1,020,000.00 USD | 0.00 USD | 413.53 USD | `-29.91%` | `1,771.00` |
| `Live` | `Long` | `0.2345` | 1,020,000.00 USD | 0.00 USD | 5,700.00 USD | `-29.60%` | `24,311.00` |
| `Live` | `Long` | `0.2355` | 1,020,000.00 USD | 0.00 USD | 3,130.00 USD | `-29.30%` | `13,311.00` |
| `Live` | `Long` | `0.2365` | 1,010,000.00 USD | 0.00 USD | 686.56 USD | `-29.00%` | `2,903.00` |
| `Live` | `Long` | `0.2375` | 1,010,000.00 USD | 0.00 USD | 568.81 USD | `-28.70%` | `2,395.00` |
| `Live` | `Long` | `0.2395` | 1,010,000.00 USD | 0.00 USD | 151.36 USD | `-28.10%` | `632.00` |
| `Live` | `Long` | `0.2435` | 1,010,000.00 USD | 0.00 USD | 3,790.00 USD | `-26.90%` | `15,565.00` |
| `Live` | `Long` | `0.2445` | 1,010,000.00 USD | 0.00 USD | 1,910.00 USD | `-26.60%` | `7,813.00` |
| `Live` | `Long` | `0.2455` | 1,010,000.00 USD | 0.00 USD | 384.94 USD | `-26.30%` | `1,568.00` |
| `Live` | `Long` | `0.2485` | 1,010,000.00 USD | 0.00 USD | 11,890.00 USD | `-25.40%` | `47,833.00` |
| `Live` | `Long` | `0.2505` | 993,640.00 USD | 0.00 USD | 262.02 USD | `-24.80%` | `1,046.00` |
| `Live` | `Long` | `0.2555` | 993,380.00 USD | 0.00 USD | 1,220.00 USD | `-23.30%` | `4,794.00` |
| `Live` | `Long` | `0.2585` | 992,150.00 USD | 0.00 USD | 302.96 USD | `-22.40%` | `1,172.00` |
| `Live` | `Long` | `0.2595` | 991,850.00 USD | 0.00 USD | 749.18 USD | `-22.10%` | `2,887.00` |
| `Live` | `Long` | `0.2615` | 991,100.00 USD | 0.00 USD | 107.74 USD | `-21.50%` | `412.00` |
| `Live` | `Long` | `0.2625` | 990,990.00 USD | 0.00 USD | 11,370.00 USD | `-21.20%` | `43,325.00` |
| `Live` | `Long` | `0.2645` | 979,620.00 USD | 0.00 USD | 2,650.00 USD | `-20.60%` | `10,032.00` |
| `Live` | `Long` | `0.2655` | 976,970.00 USD | 0.00 USD | 193.02 USD | `-20.30%` | `727.00` |
| `Live` | `Long` | `0.2675` | 976,770.00 USD | 0.00 USD | 321.54 USD | `-19.70%` | `1,202.00` |
| `Live` | `Long` | `0.2685` | 976,450.00 USD | 0.00 USD | 3,390.00 USD | `-19.40%` | `12,636.00` |
| `Live` | `Long` | `0.2735` | 973,060.00 USD | 0.00 USD | 220.99 USD | `-17.90%` | `808.00` |
| `Live` | `Long` | `0.2745` | 972,840.00 USD | 0.00 USD | 84,470.00 USD | `-17.60%` | `307,728.00` |
| `Live` | `Long` | `0.2785` | 888,370.00 USD | 0.00 USD | 13,170.00 USD | `-16.40%` | `47,301.00` |
| `Live` | `Long` | `0.2795` | 875,190.00 USD | 0.00 USD | 6,260.00 USD | `-16.10%` | `22,380.00` |
| `Live` | `Long` | `0.2805` | 868,940.00 USD | 0.00 USD | 13,300.00 USD | `-15.80%` | `47,408.00` |
| `Live` | `Long` | `0.2815` | 855,640.00 USD | 0.00 USD | 3,690.00 USD | `-15.50%` | `13,109.00` |
| `Live` | `Long` | `0.2825` | 851,950.00 USD | 0.00 USD | 838.74 USD | `-15.20%` | `2,969.00` |
| `Live` | `Long` | `0.2845` | 851,110.00 USD | 0.00 USD | 1,090.00 USD | `-14.60%` | `3,820.00` |
| `Live` | `Long` | `0.2855` | 850,020.00 USD | 0.00 USD | 5,880.00 USD | `-14.30%` | `20,578.00` |
| `Live` | `Long` | `0.2865` | 844,150.00 USD | 0.00 USD | 4,150.00 USD | `-13.99%` | `14,481.00` |
| `Live` | `Long` | `0.2885` | 840,000.00 USD | 0.00 USD | 4,940.00 USD | `-13.39%` | `17,126.00` |
| `Live` | `Long` | `0.2905` | 835,060.00 USD | 0.00 USD | 821.82 USD | `-12.79%` | `2,829.00` |
| `Live` | `Long` | `0.2915` | 834,240.00 USD | 0.00 USD | 954.37 USD | `-12.49%` | `3,274.00` |
| `Live` | `Long` | `0.2935` | 833,280.00 USD | 0.00 USD | 213.08 USD | `-11.89%` | `726.00` |
| `Live` | `Long` | `0.2945` | 833,070.00 USD | 0.00 USD | 124.87 USD | `-11.59%` | `424.00` |
| `Live` | `Long` | `0.2955` | 832,950.00 USD | 0.00 USD | 156.61 USD | `-11.29%` | `530.00` |
| `Live` | `Long` | `0.2965` | 832,790.00 USD | 0.00 USD | 1,010.00 USD | `-10.99%` | `3,398.00` |
| `Live` | `Long` | `0.2985` | 831,780.00 USD | 0.00 USD | 759.68 USD | `-10.39%` | `2,545.00` |
| `Live` | `Long` | `0.2995` | 831,020.00 USD | 0.00 USD | 197.37 USD | `-10.09%` | `659.00` |
| `Live` | `Long` | `0.3005` | 830,820.00 USD | 0.00 USD | 10,620.00 USD | `-9.79%` | `35,336.00` |
| `Live` | `Long` | `0.3015` | 820,210.00 USD | 0.00 USD | 102.81 USD | `-9.49%` | `341.00` |
| `Live` | `Long` | `0.3025` | 820,100.00 USD | 0.00 USD | 2,510.00 USD | `-9.19%` | `8,314.00` |
| `Live` | `Long` | `0.3035` | 817,590.00 USD | 0.00 USD | 4,040.00 USD | `-8.89%` | `13,300.00` |
| `Live` | `Long` | `0.3045` | 813,550.00 USD | 0.00 USD | 138.24 USD | `-8.59%` | `454.00` |
| `Live` | `Long` | `0.3055` | 813,410.00 USD | 0.00 USD | 14,670.00 USD | `-8.29%` | `48,026.00` |
| `Live` | `Long` | `0.3065` | 798,740.00 USD | 0.00 USD | 5,900.00 USD | `-7.99%` | `19,262.00` |
| `Live` | `Long` | `0.3075` | 792,840.00 USD | 0.00 USD | 722.62 USD | `-7.69%` | `2,350.00` |
| `Live` | `Long` | `0.3085` | 792,120.00 USD | 0.00 USD | 291.53 USD | `-7.39%` | `945.00` |
| `Live` | `Long` | `0.3095` | 791,820.00 USD | 0.00 USD | 192.51 USD | `-7.09%` | `622.00` |
| `Live` | `Long` | `0.3105` | 791,630.00 USD | 0.00 USD | 820.96 USD | `-6.79%` | `2,644.00` |
| `Live` | `Long` | `0.3115` | 790,810.00 USD | 0.00 USD | 13,600.00 USD | `-6.49%` | `43,671.00` |
| `Live` | `Long` | `0.3125` | 777,210.00 USD | 0.00 USD | 17,810.00 USD | `-6.19%` | `56,977.00` |
| `Live` | `Long` | `0.3135` | 759,400.00 USD | 0.00 USD | 446.11 USD | `-5.89%` | `1,423.00` |
| `Live` | `Long` | `0.3145` | 758,960.00 USD | 0.00 USD | 577.11 USD | `-5.59%` | `1,835.00` |
| `Live` | `Long` | `0.3155` | 758,380.00 USD | 0.00 USD | 2,960.00 USD | `-5.29%` | `9,396.00` |
| `Live` | `Long` | `0.3165` | 755,410.00 USD | 0.00 USD | 512.73 USD | `-4.99%` | `1,620.00` |
| `Live` | `Long` | `0.3175` | 754,900.00 USD | 0.00 USD | 2,290.00 USD | `-4.69%` | `7,205.00` |
| `Live` | `Long` | `0.3195` | 752,610.00 USD | 0.00 USD | 1,430.00 USD | `-4.09%` | `4,464.00` |
| `Live` | `Long` | `0.3205` | 751,190.00 USD | 0.00 USD | 455.75 USD | `-3.79%` | `1,422.00` |
| `Live` | `Long` | `0.3215` | 750,730.00 USD | 0.00 USD | 756.17 USD | `-3.49%` | `2,352.00` |
| `Live` | `Long` | `0.3235` | 749,980.00 USD | 0.00 USD | 128.43 USD | `-2.89%` | `397.00` |
| `Live` | `Long` | `0.3255` | 749,850.00 USD | 0.00 USD | 3,580.00 USD | `-2.29%` | `11,000.00` |
| `Live` | `Long` | `0.3275` | 746,270.00 USD | 0.00 USD | 163.42 USD | `-1.69%` | `499.00` |
| `Live` | `Long` | `0.3285` | 746,100.00 USD | 0.00 USD | 745,260.00 USD | `-1.39%` | `2,268,686.00` |
| `Live` | `Long` | `0.3295` | 839.90 USD | 0.00 USD | 839.90 USD | `-1.09%` | `2,549.00` |
| `Live` | `Short` | `0.3305` | 7,080.00 USD | 7,080.00 USD | 0.00 USD | `-0.79%` | `21,413.00` |
| `Live` | `Short` | `0.3505` | 16,710.00 USD | 9,630.00 USD | 0.00 USD | `+5.22%` | `27,477.00` |
| `Live` | `Short` | `0.3515` | 16,880.00 USD | 175.05 USD | 0.00 USD | `+5.52%` | `498.00` |
| `Live` | `Short` | `0.3635` | 48,140.00 USD | 31,260.00 USD | 0.00 USD | `+9.12%` | `85,992.00` |
| `Live` | `Short` | `0.3645` | 60,530.00 USD | 12,390.00 USD | 0.00 USD | `+9.42%` | `34,003.00` |
| `Live` | `Short` | `0.3665` | 63,650.00 USD | 3,110.00 USD | 0.00 USD | `+10.02%` | `8,498.00` |
| `Live` | `Short` | `0.3705` | 63,930.00 USD | 278.99 USD | 0.00 USD | `+11.22%` | `753.00` |
| `Live` | `Short` | `0.3725` | 64,110.00 USD | 186.25 USD | 0.00 USD | `+11.82%` | `500.00` |
| `Live` | `Short` | `0.3735` | 71,320.00 USD | 7,210.00 USD | 0.00 USD | `+12.12%` | `19,294.00` |
| `Live` | `Short` | `0.3755` | 75,350.00 USD | 4,030.00 USD | 0.00 USD | `+12.72%` | `10,732.00` |
| `Live` | `Short` | `0.3775` | 75,460.00 USD | 104.19 USD | 0.00 USD | `+13.32%` | `276.00` |
| `Live` | `Short` | `0.3785` | 631,880.00 USD | 556,430.00 USD | 0.00 USD | `+13.62%` | `1,470,083.00` |
| `Live` | `Short` | `0.3835` | 632,000.00 USD | 115.05 USD | 0.00 USD | `+15.12%` | `300.00` |
| `Live` | `Short` | `0.3855` | 632,260.00 USD | 264.84 USD | 0.00 USD | `+15.72%` | `687.00` |
| `Live` | `Short` | `0.3895` | 637,020.00 USD | 4,760.00 USD | 0.00 USD | `+16.92%` | `12,210.00` |
| `Live` | `Short` | `0.3905` | 643,020.00 USD | 6,000.00 USD | 0.00 USD | `+17.23%` | `15,374.00` |
| `Live` | `Short` | `0.3935` | 644,500.00 USD | 1,480.00 USD | 0.00 USD | `+18.13%` | `3,770.00` |
| `Live` | `Short` | `0.3945` | 762,630.00 USD | 118,130.00 USD | 0.00 USD | `+18.43%` | `299,436.00` |
| `Live` | `Short` | `0.3955` | 2,160,000.00 USD | 1,390,000.00 USD | 0.00 USD | `+18.73%` | `3,526,740.00` |
| `Live` | `Short` | `0.4025` | 2,160,000.00 USD | 328.44 USD | 0.00 USD | `+20.83%` | `816.00` |
| `Live` | `Short` | `0.4085` | 2,160,000.00 USD | 170.75 USD | 0.00 USD | `+22.63%` | `418.00` |
| `Live` | `Short` | `0.4095` | 2,160,000.00 USD | 239.56 USD | 0.00 USD | `+22.93%` | `585.00` |
| `Live` | `Short` | `0.4185` | 2,160,000.00 USD | 998.96 USD | 0.00 USD | `+25.63%` | `2,387.00` |
| `Live` | `Short` | `0.4245` | 2,160,000.00 USD | 134.57 USD | 0.00 USD | `+27.43%` | `317.00` |
| `Live` | `Short` | `0.4255` | 2,160,000.00 USD | 3,940.00 USD | 0.00 USD | `+27.73%` | `9,259.00` |
| `Live` | `Short` | `0.4295` | 2,170,000.00 USD | 10,210.00 USD | 0.00 USD | `+28.93%` | `23,779.00` |
| `Live` | `Short` | `0.4325` | 2,170,000.00 USD | 1,500.00 USD | 0.00 USD | `+29.83%` | `3,464.00` |
| `Live` | `Short` | `0.4355` | 2,250,000.00 USD | 70,890.00 USD | 0.00 USD | `+30.73%` | `162,775.00` |
| `Live` | `Short` | `0.4365` | 2,250,000.00 USD | 1,490.00 USD | 0.00 USD | `+31.03%` | `3,416.00` |
| `Live` | `Short` | `0.4415` | 2,250,000.00 USD | 377.48 USD | 0.00 USD | `+32.53%` | `855.00` |
| `Live` | `Short` | `0.4445` | 2,270,000.00 USD | 22,230.00 USD | 0.00 USD | `+33.44%` | `50,000.00` |
| `Live` | `Short` | `0.4455` | 2,270,000.00 USD | 1,020.00 USD | 0.00 USD | `+33.74%` | `2,284.00` |
| `Live` | `Short` | `0.4465` | 2,280,000.00 USD | 5,520.00 USD | 0.00 USD | `+34.04%` | `12,352.00` |
| `Live` | `Short` | `0.4475` | 2,340,000.00 USD | 65,610.00 USD | 0.00 USD | `+34.34%` | `146,614.00` |
| `Live` | `Short` | `0.4515` | 2,340,000.00 USD | 318.76 USD | 0.00 USD | `+35.54%` | `706.00` |
| `Live` | `Short` | `0.4715` | 2,340,000.00 USD | 272.53 USD | 0.00 USD | `+41.54%` | `578.00` |
| `Live` | `Short` | `0.4805` | 2,350,000.00 USD | 2,880.00 USD | 0.00 USD | `+44.24%` | `6,000.00` |
| `Live` | `Short` | `0.4895` | 2,350,000.00 USD | 839.49 USD | 0.00 USD | `+46.94%` | `1,715.00` |
| `Live` | `Short` | `0.4905` | 2,350,000.00 USD | 5,120.00 USD | 0.00 USD | `+47.24%` | `10,430.00` |
| `Live` | `Short` | `0.4995` | 2,350,000.00 USD | 2,730.00 USD | 0.00 USD | `+49.95%` | `5,465.00` |
| `Live` | `Short` | `0.5005` | 2,380,000.00 USD | 23,320.00 USD | 0.00 USD | `+50.25%` | `46,591.00` |
| `Live` | `Short` | `0.5325` | 2,380,000.00 USD | 667.22 USD | 0.00 USD | `+59.85%` | `1,253.00` |
| `Live` | `Short` | `0.5465` | 2,420,000.00 USD | 40,440.00 USD | 0.00 USD | `+64.05%` | `74,000.00` |
| `Live` | `Short` | `0.5575` | 2,420,000.00 USD | 3,060.00 USD | 0.00 USD | `+67.36%` | `5,483.00` |
| `Live` | `Short` | `0.5605` | 2,420,000.00 USD | 140.12 USD | 0.00 USD | `+68.26%` | `250.00` |
| `Live` | `Short` | `0.5725` | 3,160,000.00 USD | 742,670.00 USD | 0.00 USD | `+71.86%` | `1,297,248.00` |
| `Live` | `Short` | `0.6155` | 3,190,000.00 USD | 24,620.00 USD | 0.00 USD | `+84.77%` | `40,000.00` |
| `Live` | `Short` | `0.6205` | 3,190,000.00 USD | 375.40 USD | 0.00 USD | `+86.27%` | `605.00` |
| `Live` | `Short` | `0.6275` | 3,190,000.00 USD | 1,130.00 USD | 0.00 USD | `+88.37%` | `1,808.00` |
| `Live` | `Short` | `0.6335` | 3,200,000.00 USD | 6,810.00 USD | 0.00 USD | `+90.17%` | `10,756.00` |
| `Live` | `Short` | `0.6505` | 3,300,000.00 USD | 102,000.00 USD | 0.00 USD | `+95.27%` | `156,809.00` |
| `Live` | `Short` | `0.6515` | 3,300,000.00 USD | 951.19 USD | 0.00 USD | `+95.58%` | `1,460.00` |
| `Live` | `Short` | `0.6535` | 3,300,000.00 USD | 705.13 USD | 0.00 USD | `+96.18%` | `1,079.00` |
| `Live` | `Short` | `0.6615` | 3,300,000.00 USD | 2,060.00 USD | 0.00 USD | `+98.58%` | `3,114.00` |
| `Live` | `Short` | `0.6635` | 3,310,000.00 USD | 3,740.00 USD | 0.00 USD | `+99.18%` | `5,632.00` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `0.0665` | 876,510.00 USD | 0.00 USD | 112.32 USD | `-80.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0945` | 876,400.00 USD | 0.00 USD | 198.45 USD | `-71.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1415` | 876,200.00 USD | 0.00 USD | 330.26 USD | `-57.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2035` | 875,870.00 USD | 0.00 USD | 1,750.00 USD | `-38.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2105` | 874,120.00 USD | 0.00 USD | 2,220.00 USD | `-36.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2195` | 871,900.00 USD | 0.00 USD | 450.41 USD | `-34.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2305` | 871,450.00 USD | 0.00 USD | 121.70 USD | `-30.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2345` | 871,330.00 USD | 0.00 USD | 705.61 USD | `-29.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2355` | 870,630.00 USD | 0.00 USD | 159.20 USD | `-29.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2405` | 870,470.00 USD | 0.00 USD | 1,200.00 USD | `-27.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2415` | 869,260.00 USD | 0.00 USD | 127.51 USD | `-27.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2505` | 869,140.00 USD | 0.00 USD | 1,850.00 USD | `-24.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2515` | 867,280.00 USD | 0.00 USD | 41,500.00 USD | `-24.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2565` | 825,790.00 USD | 0.00 USD | 1,920.00 USD | `-23.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2605` | 823,860.00 USD | 0.00 USD | 664.01 USD | `-21.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2625` | 823,200.00 USD | 0.00 USD | 954.98 USD | `-21.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2635` | 822,240.00 USD | 0.00 USD | 103.56 USD | `-20.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2675` | 822,140.00 USD | 0.00 USD | 695.50 USD | `-19.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2685` | 821,440.00 USD | 0.00 USD | 1,630.00 USD | `-19.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2695` | 819,820.00 USD | 0.00 USD | 1,470.00 USD | `-19.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2755` | 818,340.00 USD | 0.00 USD | 101.94 USD | `-17.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2775` | 818,240.00 USD | 0.00 USD | 3,260.00 USD | `-16.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2815` | 814,980.00 USD | 0.00 USD | 2,550.00 USD | `-15.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2835` | 812,430.00 USD | 0.00 USD | 229.92 USD | `-14.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2875` | 812,200.00 USD | 0.00 USD | 8,010.00 USD | `-13.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2935` | 804,190.00 USD | 0.00 USD | 11,610.00 USD | `-11.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2965` | 792,580.00 USD | 0.00 USD | 111.19 USD | `-10.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2985` | 792,470.00 USD | 0.00 USD | 433.42 USD | `-10.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3005` | 792,040.00 USD | 0.00 USD | 2,710.00 USD | `-9.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3045` | 789,330.00 USD | 0.00 USD | 503.95 USD | `-8.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3065` | 788,830.00 USD | 0.00 USD | 1,400.00 USD | `-7.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3075` | 787,430.00 USD | 0.00 USD | 193.11 USD | `-7.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3085` | 787,230.00 USD | 0.00 USD | 15,150.00 USD | `-7.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3095` | 772,080.00 USD | 0.00 USD | 156.30 USD | `-7.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3105` | 771,920.00 USD | 0.00 USD | 12,200.00 USD | `-6.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3115` | 759,720.00 USD | 0.00 USD | 6,530.00 USD | `-6.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3125` | 753,190.00 USD | 0.00 USD | 524,570.00 USD | `-6.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3135` | 228,620.00 USD | 0.00 USD | 1,270.00 USD | `-5.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3145` | 227,350.00 USD | 0.00 USD | 53,690.00 USD | `-5.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3155` | 173,670.00 USD | 0.00 USD | 2,570.00 USD | `-5.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3165` | 171,100.00 USD | 0.00 USD | 6,100.00 USD | `-4.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3175` | 165,000.00 USD | 0.00 USD | 850.90 USD | `-4.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3185` | 164,150.00 USD | 0.00 USD | 1,160.00 USD | `-4.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3195` | 162,990.00 USD | 0.00 USD | 6,220.00 USD | `-4.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3205` | 156,770.00 USD | 0.00 USD | 10,320.00 USD | `-3.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3215` | 146,450.00 USD | 0.00 USD | 43,760.00 USD | `-3.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3225` | 102,680.00 USD | 0.00 USD | 131.90 USD | `-3.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3235` | 102,550.00 USD | 0.00 USD | 7,040.00 USD | `-2.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3245` | 95,510.00 USD | 0.00 USD | 3,870.00 USD | `-2.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3255` | 91,640.00 USD | 0.00 USD | 65,070.00 USD | `-2.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3265` | 26,570.00 USD | 0.00 USD | 6,130.00 USD | `-1.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3275` | 20,440.00 USD | 0.00 USD | 7,430.00 USD | `-1.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3285` | 13,000.00 USD | 0.00 USD | 4,270.00 USD | `-1.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3295` | 8,730.00 USD | 0.00 USD | 1,960.00 USD | `-1.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3305` | 6,780.00 USD | 0.00 USD | 949.53 USD | `-0.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3315` | 5,830.00 USD | 0.00 USD | 100.11 USD | `-0.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3325` | 5,730.00 USD | 0.00 USD | 5,730.00 USD | `-0.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3335` | 4,880.00 USD | 4,880.00 USD | 0.00 USD | `+0.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3345` | 11,820.00 USD | 6,940.00 USD | 0.00 USD | `+0.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3355` | 11,960.00 USD | 138.56 USD | 0.00 USD | `+0.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3365` | 12,220.00 USD | 265.50 USD | 0.00 USD | `+1.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3375` | 12,360.00 USD | 138.71 USD | 0.00 USD | `+1.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3385` | 12,520.00 USD | 157.74 USD | 0.00 USD | `+1.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3395` | 19,430.00 USD | 6,910.00 USD | 0.00 USD | `+1.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3405` | 20,830.00 USD | 1,400.00 USD | 0.00 USD | `+2.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3415` | 21,320.00 USD | 486.30 USD | 0.00 USD | `+2.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3425` | 21,750.00 USD | 431.55 USD | 0.00 USD | `+2.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3435` | 22,580.00 USD | 828.18 USD | 0.00 USD | `+3.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3445` | 24,530.00 USD | 1,950.00 USD | 0.00 USD | `+3.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3455` | 24,960.00 USD | 435.33 USD | 0.00 USD | `+3.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3465` | 25,520.00 USD | 555.44 USD | 0.00 USD | `+4.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3475` | 25,790.00 USD | 274.18 USD | 0.00 USD | `+4.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3485` | 26,230.00 USD | 439.11 USD | 0.00 USD | `+4.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3495` | 27,230.00 USD | 996.08 USD | 0.00 USD | `+4.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3505` | 27,890.00 USD | 665.60 USD | 0.00 USD | `+5.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3515` | 28,810.00 USD | 919.52 USD | 0.00 USD | `+5.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3525` | 37,500.00 USD | 8,690.00 USD | 0.00 USD | `+5.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3535` | 37,820.00 USD | 312.14 USD | 0.00 USD | `+6.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3545` | 38,170.00 USD | 354.50 USD | 0.00 USD | `+6.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3555` | 38,300.00 USD | 132.96 USD | 0.00 USD | `+6.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3565` | 77,730.00 USD | 39,430.00 USD | 0.00 USD | `+7.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3575` | 118,120.00 USD | 40,390.00 USD | 0.00 USD | `+7.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3585` | 121,430.00 USD | 3,310.00 USD | 0.00 USD | `+7.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3595` | 122,460.00 USD | 1,030.00 USD | 0.00 USD | `+7.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3605` | 125,400.00 USD | 2,940.00 USD | 0.00 USD | `+8.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3615` | 125,630.00 USD | 224.49 USD | 0.00 USD | `+8.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3635` | 125,730.00 USD | 103.23 USD | 0.00 USD | `+9.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3645` | 128,430.00 USD | 2,700.00 USD | 0.00 USD | `+9.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3655` | 170,170.00 USD | 41,740.00 USD | 0.00 USD | `+9.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3665` | 170,600.00 USD | 433.57 USD | 0.00 USD | `+10.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3675` | 170,770.00 USD | 172.72 USD | 0.00 USD | `+10.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3685` | 170,990.00 USD | 218.89 USD | 0.00 USD | `+10.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3695` | 185,330.00 USD | 14,330.00 USD | 0.00 USD | `+10.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3705` | 188,810.00 USD | 3,480.00 USD | 0.00 USD | `+11.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3715` | 188,980.00 USD | 174.60 USD | 0.00 USD | `+11.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3725` | 189,090.00 USD | 107.28 USD | 0.00 USD | `+11.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3735` | 189,530.00 USD | 439.61 USD | 0.00 USD | `+12.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3745` | 189,960.00 USD | 437.79 USD | 0.00 USD | `+12.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3755` | 192,360.00 USD | 2,400.00 USD | 0.00 USD | `+12.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3765` | 192,540.00 USD | 182.60 USD | 0.00 USD | `+13.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3775` | 199,000.00 USD | 6,450.00 USD | 0.00 USD | `+13.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3785` | 199,270.00 USD | 275.17 USD | 0.00 USD | `+13.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3795` | 199,840.00 USD | 569.25 USD | 0.00 USD | `+13.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3805` | 205,820.00 USD | 5,980.00 USD | 0.00 USD | `+14.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3815` | 206,070.00 USD | 257.89 USD | 0.00 USD | `+14.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3825` | 206,340.00 USD | 262.78 USD | 0.00 USD | `+14.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3835` | 206,560.00 USD | 224.73 USD | 0.00 USD | `+15.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3855` | 207,180.00 USD | 621.04 USD | 0.00 USD | `+15.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3865` | 207,930.00 USD | 742.08 USD | 0.00 USD | `+16.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3875` | 209,040.00 USD | 1,110.00 USD | 0.00 USD | `+16.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3885` | 209,220.00 USD | 181.04 USD | 0.00 USD | `+16.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3895` | 209,710.00 USD | 490.38 USD | 0.00 USD | `+16.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3905` | 209,850.00 USD | 138.63 USD | 0.00 USD | `+17.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3915` | 210,130.00 USD | 276.40 USD | 0.00 USD | `+17.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3945` | 210,250.00 USD | 126.24 USD | 0.00 USD | `+18.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3965` | 212,650.00 USD | 2,400.00 USD | 0.00 USD | `+19.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3975` | 214,060.00 USD | 1,410.00 USD | 0.00 USD | `+19.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3985` | 215,260.00 USD | 1,200.00 USD | 0.00 USD | `+19.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3995` | 286,750.00 USD | 71,490.00 USD | 0.00 USD | `+19.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4005` | 287,620.00 USD | 864.28 USD | 0.00 USD | `+20.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4015` | 291,540.00 USD | 3,920.00 USD | 0.00 USD | `+20.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4035` | 370,870.00 USD | 79,330.00 USD | 0.00 USD | `+21.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4055` | 372,070.00 USD | 1,200.00 USD | 0.00 USD | `+21.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4065` | 373,270.00 USD | 1,200.00 USD | 0.00 USD | `+22.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4085` | 373,410.00 USD | 138.07 USD | 0.00 USD | `+22.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4095` | 374,680.00 USD | 1,270.00 USD | 0.00 USD | `+22.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4135` | 375,010.00 USD | 331.63 USD | 0.00 USD | `+24.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4175` | 375,320.00 USD | 313.54 USD | 0.00 USD | `+25.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4205` | 375,510.00 USD | 186.70 USD | 0.00 USD | `+26.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4275` | 375,830.00 USD | 325.75 USD | 0.00 USD | `+28.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4305` | 376,020.00 USD | 183.82 USD | 0.00 USD | `+29.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4355` | 376,320.00 USD | 299.19 USD | 0.00 USD | `+30.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4405` | 414,890.00 USD | 38,580.00 USD | 0.00 USD | `+32.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4445` | 415,060.00 USD | 170.69 USD | 0.00 USD | `+33.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4475` | 415,200.00 USD | 135.59 USD | 0.00 USD | `+34.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4495` | 416,720.00 USD | 1,520.00 USD | 0.00 USD | `+34.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4505` | 417,040.00 USD | 320.31 USD | 0.00 USD | `+35.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4545` | 422,380.00 USD | 5,340.00 USD | 0.00 USD | `+36.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4605` | 423,850.00 USD | 1,470.00 USD | 0.00 USD | `+38.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4895` | 504,620.00 USD | 80,770.00 USD | 0.00 USD | `+46.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4905` | 504,790.00 USD | 169.22 USD | 0.00 USD | `+47.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4945` | 504,940.00 USD | 153.79 USD | 0.00 USD | `+48.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4965` | 505,670.00 USD | 724.89 USD | 0.00 USD | `+49.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.5005` | 516,820.00 USD | 11,150.00 USD | 0.00 USD | `+50.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.5055` | 518,750.00 USD | 1,930.00 USD | 0.00 USD | `+51.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.5295` | 518,880.00 USD | 135.02 USD | 0.00 USD | `+58.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6305` | 519,120.00 USD | 240.85 USD | 0.00 USD | `+89.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6325` | 520,220.00 USD | 1,100.00 USD | 0.00 USD | `+89.87%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `0.2953` | 19,250,000.00 USD | 0.00 USD | 19,250,000.00 USD | 81,550.00 USD | 0.00 USD | 10,820.00 USD |
| `7D` | `0.2959` | 19,150,000.00 USD | 0.00 USD | 19,150,000.00 USD | 107,990.00 USD | 22,740.00 USD | 9,700.00 USD |
| `7D` | `0.2965` | 19,010,000.00 USD | 0.00 USD | 19,010,000.00 USD | 123,420.00 USD | 38,150.00 USD | 60,970.00 USD |
| `7D` | `0.2971` | 18,790,000.00 USD | 0.00 USD | 18,790,000.00 USD | 88,940.00 USD | 36,460.00 USD | 55,170.00 USD |
| `1D` | `0.2973` | 12,090,000.00 USD | 0.00 USD | 12,090,000.00 USD | 185.60 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.2977` | 12,090,000.00 USD | 0.00 USD | 12,090,000.00 USD | 13,210.00 USD | 3,650.00 USD | 4,240.00 USD |
| `7D` | `0.2977` | 18,610,000.00 USD | 0.00 USD | 18,610,000.00 USD | 53,890.00 USD | 18,540.00 USD | 17,670.00 USD |
| `1D` | `0.2981` | 12,070,000.00 USD | 0.00 USD | 12,070,000.00 USD | 12,230.00 USD | 6,300.00 USD | 14,550.00 USD |
| `7D` | `0.2983` | 18,520,000.00 USD | 0.00 USD | 18,520,000.00 USD | 172,020.00 USD | 15,470.00 USD | 39,660.00 USD |
| `1D` | `0.2985` | 12,040,000.00 USD | 0.00 USD | 12,040,000.00 USD | 112,860.00 USD | 13,480.00 USD | 13,660.00 USD |
| `1D` | `0.2989` | 11,900,000.00 USD | 0.00 USD | 11,900,000.00 USD | 24,270.00 USD | 0.00 USD | 8,790.00 USD |
| `7D` | `0.2989` | 18,290,000.00 USD | 0.00 USD | 18,290,000.00 USD | 111,920.00 USD | 18,720.00 USD | 23,920.00 USD |
| `1D` | `0.2993` | 11,870,000.00 USD | 0.00 USD | 11,870,000.00 USD | 10,310.00 USD | 25,460.00 USD | 56,800.00 USD |
| `7D` | `0.2995` | 18,140,000.00 USD | 0.00 USD | 18,140,000.00 USD | 8,380.00 USD | 2,190.00 USD | 48,990.00 USD |
| `1D` | `0.2997` | 11,770,000.00 USD | 0.00 USD | 11,770,000.00 USD | 600.83 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3001` | 11,770,000.00 USD | 0.00 USD | 11,770,000.00 USD | 8,760.00 USD | 14,600.00 USD | 14,510.00 USD |
| `7D` | `0.3001` | 18,080,000.00 USD | 0.00 USD | 18,080,000.00 USD | 1,880.00 USD | 15,390.00 USD | 30,210.00 USD |
| `1D` | `0.3005` | 11,740,000.00 USD | 0.00 USD | 11,740,000.00 USD | 4,620.00 USD | 7,870.00 USD | 18,440.00 USD |
| `7D` | `0.3007` | 18,030,000.00 USD | 0.00 USD | 18,030,000.00 USD | 13,780.00 USD | 2,960.00 USD | 22,100.00 USD |
| `1D` | `0.3009` | 11,710,000.00 USD | 0.00 USD | 11,710,000.00 USD | 23,780.00 USD | 3,410.00 USD | 16,090.00 USD |
| `1D` | `0.3013` | 11,660,000.00 USD | 0.00 USD | 11,660,000.00 USD | 0.00 USD | 3,170.00 USD | 0.00 USD |
| `7D` | `0.3013` | 17,990,000.00 USD | 0.00 USD | 17,990,000.00 USD | 2,700.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3017` | 11,660,000.00 USD | 0.00 USD | 11,660,000.00 USD | 1,010.00 USD | 8,490.00 USD | 0.00 USD |
| `7D` | `0.3019` | 17,990,000.00 USD | 0.00 USD | 17,990,000.00 USD | 0.00 USD | 8,660.00 USD | 0.00 USD |
| `1D` | `0.3021` | 11,650,000.00 USD | 0.00 USD | 11,650,000.00 USD | 14,850.00 USD | 4,540.00 USD | 16,590.00 USD |
| `1D` | `0.3025` | 11,610,000.00 USD | 0.00 USD | 11,610,000.00 USD | 2,600.00 USD | 2,050.00 USD | 0.00 USD |
| `7D` | `0.3025` | 17,980,000.00 USD | 0.00 USD | 17,980,000.00 USD | 0.00 USD | 9,860.00 USD | 0.00 USD |
| `1D` | `0.3029` | 11,610,000.00 USD | 0.00 USD | 11,610,000.00 USD | 24,570.00 USD | 0.00 USD | 6,190.00 USD |
| `7D` | `0.3031` | 17,970,000.00 USD | 0.00 USD | 17,970,000.00 USD | 50,940.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3033` | 11,580,000.00 USD | 0.00 USD | 11,580,000.00 USD | 1,070.00 USD | 2,750.00 USD | 12,600.00 USD |
| `1D` | `0.3037` | 11,560,000.00 USD | 0.00 USD | 11,560,000.00 USD | 517.67 USD | 3,230.00 USD | 0.00 USD |
| `1D` | `0.3041` | 11,560,000.00 USD | 0.00 USD | 11,560,000.00 USD | 537.63 USD | 9,300.00 USD | 56,350.00 USD |
| `1D` | `0.3045` | 11,490,000.00 USD | 0.00 USD | 11,490,000.00 USD | 0.00 USD | 13,170.00 USD | 7,480.00 USD |
| `1D` | `0.3049` | 11,470,000.00 USD | 0.00 USD | 11,470,000.00 USD | 31,710.00 USD | 11,440.00 USD | 42,260.00 USD |
| `7D` | `0.3049` | 17,920,000.00 USD | 0.00 USD | 17,920,000.00 USD | 18,870.00 USD | 0.00 USD | 66,870.00 USD |
| `1D` | `0.3053` | 11,390,000.00 USD | 0.00 USD | 11,390,000.00 USD | 46,990.00 USD | 15,890.00 USD | 49,310.00 USD |
| `7D` | `0.3055` | 17,840,000.00 USD | 0.00 USD | 17,840,000.00 USD | 1,250.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3061` | 11,270,000.00 USD | 0.00 USD | 11,270,000.00 USD | 885.25 USD | 2,350.00 USD | 56,460.00 USD |
| `7D` | `0.3061` | 17,830,000.00 USD | 0.00 USD | 17,830,000.00 USD | 32,690.00 USD | 7,690.00 USD | 37,210.00 USD |
| `1D` | `0.3065` | 11,210,000.00 USD | 0.00 USD | 11,210,000.00 USD | 29,570.00 USD | 26,740.00 USD | 35,690.00 USD |
| `7D` | `0.3067` | 17,760,000.00 USD | 0.00 USD | 17,760,000.00 USD | 5,220.00 USD | 8,110.00 USD | 0.00 USD |
| `1D` | `0.3069` | 11,120,000.00 USD | 0.00 USD | 11,120,000.00 USD | 1,540.00 USD | 2,880.00 USD | 12,760.00 USD |
| `1D` | `0.3073` | 11,100,000.00 USD | 0.00 USD | 11,100,000.00 USD | 23,280.00 USD | 1,940.00 USD | 0.00 USD |
| `7D` | `0.3073` | 17,740,000.00 USD | 0.00 USD | 17,740,000.00 USD | 9,190.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3077` | 11,080,000.00 USD | 0.00 USD | 11,080,000.00 USD | 350.20 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3079` | 17,730,000.00 USD | 0.00 USD | 17,730,000.00 USD | 37,430.00 USD | 10,270.00 USD | 50,200.00 USD |
| `1D` | `0.3081` | 11,080,000.00 USD | 0.00 USD | 11,080,000.00 USD | 18,400.00 USD | 0.00 USD | 12,250.00 USD |
| `1D` | `0.3085` | 11,050,000.00 USD | 0.00 USD | 11,050,000.00 USD | 340.09 USD | 0.00 USD | 15,810.00 USD |
| `7D` | `0.3085` | 17,640,000.00 USD | 0.00 USD | 17,640,000.00 USD | 2,870.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3089` | 11,030,000.00 USD | 0.00 USD | 11,030,000.00 USD | 550.01 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3091` | 17,630,000.00 USD | 0.00 USD | 17,630,000.00 USD | 12,490.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3093` | 11,030,000.00 USD | 0.00 USD | 11,030,000.00 USD | 14,750.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3097` | 11,020,000.00 USD | 0.00 USD | 11,020,000.00 USD | 610.25 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3097` | 17,620,000.00 USD | 0.00 USD | 17,620,000.00 USD | 83,130.00 USD | 3,620.00 USD | 54,360.00 USD |
| `1D` | `0.3101` | 11,020,000.00 USD | 0.00 USD | 11,020,000.00 USD | 41,340.00 USD | 15,820.00 USD | 46,470.00 USD |
| `7D` | `0.3103` | 17,480,000.00 USD | 0.00 USD | 17,480,000.00 USD | 67,180.00 USD | 0.00 USD | 63,310.00 USD |
| `1D` | `0.3105` | 10,910,000.00 USD | 0.00 USD | 10,910,000.00 USD | 21,200.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3109` | 17,350,000.00 USD | 0.00 USD | 17,350,000.00 USD | 6,350.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3113` | 10,890,000.00 USD | 0.00 USD | 10,890,000.00 USD | 0.00 USD | 4,980.00 USD | 0.00 USD |
| `7D` | `0.3115` | 17,340,000.00 USD | 0.00 USD | 17,340,000.00 USD | 5,350.00 USD | 0.00 USD | 37,490.00 USD |
| `1D` | `0.3117` | 10,890,000.00 USD | 0.00 USD | 10,890,000.00 USD | 14,660.00 USD | 12,220.00 USD | 17,620.00 USD |
| `1D` | `0.3121` | 10,840,000.00 USD | 0.00 USD | 10,840,000.00 USD | 11,560.00 USD | 2,560.00 USD | 33,830.00 USD |
| `7D` | `0.3121` | 17,300,000.00 USD | 0.00 USD | 17,300,000.00 USD | 166,810.00 USD | 19,620.00 USD | 0.00 USD |
| `1D` | `0.3125` | 10,790,000.00 USD | 0.00 USD | 10,790,000.00 USD | 12,740.00 USD | 13,530.00 USD | 0.00 USD |
| `7D` | `0.3127` | 17,110,000.00 USD | 0.00 USD | 17,110,000.00 USD | 16,750.00 USD | 54,460.00 USD | 57,690.00 USD |
| `1D` | `0.3129` | 10,770,000.00 USD | 0.00 USD | 10,770,000.00 USD | 3,480.00 USD | 28,470.00 USD | 29,100.00 USD |
| `1D` | `0.3133` | 10,710,000.00 USD | 0.00 USD | 10,710,000.00 USD | 4,020.00 USD | 23,940.00 USD | 9,590.00 USD |
| `7D` | `0.3133` | 16,980,000.00 USD | 0.00 USD | 16,980,000.00 USD | 3,990.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3137` | 10,670,000.00 USD | 0.00 USD | 10,670,000.00 USD | 4,590.00 USD | 10,610.00 USD | 0.00 USD |
| `7D` | `0.3139` | 16,980,000.00 USD | 0.00 USD | 16,980,000.00 USD | 2,940.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3141` | 10,650,000.00 USD | 0.00 USD | 10,650,000.00 USD | 6,900.00 USD | 0.00 USD | 9,540.00 USD |
| `1D` | `0.3145` | 10,640,000.00 USD | 0.00 USD | 10,640,000.00 USD | 1,910.00 USD | 5,900.00 USD | 0.00 USD |
| `7D` | `0.3145` | 16,980,000.00 USD | 0.00 USD | 16,980,000.00 USD | 247,620.00 USD | 51,270.00 USD | 17,870.00 USD |
| `1D` | `0.3149` | 10,630,000.00 USD | 0.00 USD | 10,630,000.00 USD | 1,380.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3151` | 16,660,000.00 USD | 0.00 USD | 16,660,000.00 USD | 206,090.00 USD | 23,130.00 USD | 49,320.00 USD |
| `1D` | `0.3153` | 10,630,000.00 USD | 0.00 USD | 10,630,000.00 USD | 19,960.00 USD | 25,600.00 USD | 0.00 USD |
| `1D` | `0.3157` | 10,580,000.00 USD | 0.00 USD | 10,580,000.00 USD | 11,820.00 USD | 1,830.00 USD | 16,240.00 USD |
| `7D` | `0.3157` | 16,380,000.00 USD | 0.00 USD | 16,380,000.00 USD | 393,090.00 USD | 93,740.00 USD | 60,300.00 USD |
| `1D` | `0.3161` | 10,550,000.00 USD | 0.00 USD | 10,550,000.00 USD | 3,620.00 USD | 2,990.00 USD | 0.00 USD |
| `7D` | `0.3163` | 15,830,000.00 USD | 0.00 USD | 15,830,000.00 USD | 483,870.00 USD | 182,370.00 USD | 192,840.00 USD |
| `1D` | `0.3165` | 10,550,000.00 USD | 0.00 USD | 10,550,000.00 USD | 45,260.00 USD | 30,980.00 USD | 9,000.00 USD |
| `1D` | `0.3169` | 10,460,000.00 USD | 0.00 USD | 10,460,000.00 USD | 1,090.00 USD | 10,820.00 USD | 20,780.00 USD |
| `7D` | `0.3169` | 14,980,000.00 USD | 0.00 USD | 14,980,000.00 USD | 403,830.00 USD | 106,680.00 USD | 142,240.00 USD |
| `1D` | `0.3173` | 10,430,000.00 USD | 0.00 USD | 10,430,000.00 USD | 25,580.00 USD | 33,870.00 USD | 27,630.00 USD |
| `7D` | `0.3175` | 14,320,000.00 USD | 0.00 USD | 14,320,000.00 USD | 146,800.00 USD | 53,470.00 USD | 69,280.00 USD |
| `1D` | `0.3177` | 10,340,000.00 USD | 0.00 USD | 10,340,000.00 USD | 46,680.00 USD | 8,980.00 USD | 30,890.00 USD |
| `1D` | `0.3181` | 10,250,000.00 USD | 0.00 USD | 10,250,000.00 USD | 279,630.00 USD | 48,980.00 USD | 76,070.00 USD |
| `7D` | `0.3181` | 14,050,000.00 USD | 0.00 USD | 14,050,000.00 USD | 743,630.00 USD | 76,910.00 USD | 182,330.00 USD |
| `1D` | `0.3185` | 9,850,000.00 USD | 0.00 USD | 9,850,000.00 USD | 153,270.00 USD | 52,920.00 USD | 51,330.00 USD |
| `7D` | `0.3187` | 13,050,000.00 USD | 0.00 USD | 13,050,000.00 USD | 411,400.00 USD | 97,820.00 USD | 24,770.00 USD |
| `1D` | `0.3189` | 9,590,000.00 USD | 0.00 USD | 9,590,000.00 USD | 74,680.00 USD | 5,580.00 USD | 48,660.00 USD |
| `1D` | `0.3193` | 9,460,000.00 USD | 0.00 USD | 9,460,000.00 USD | 107,190.00 USD | 74,060.00 USD | 180,830.00 USD |
| `7D` | `0.3193` | 12,520,000.00 USD | 0.00 USD | 12,520,000.00 USD | 118,210.00 USD | 25,780.00 USD | 168,960.00 USD |
| `1D` | `0.3197` | 9,100,000.00 USD | 0.00 USD | 9,100,000.00 USD | 74,370.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3199` | 12,200,000.00 USD | 0.00 USD | 12,200,000.00 USD | 0.00 USD | 38,380.00 USD | 63,420.00 USD |
| `1D` | `0.3201` | 9,030,000.00 USD | 0.00 USD | 9,030,000.00 USD | 208,440.00 USD | 48,100.00 USD | 61,570.00 USD |
| `1D` | `0.3205` | 8,710,000.00 USD | 0.00 USD | 8,710,000.00 USD | 126,280.00 USD | 31,270.00 USD | 102,160.00 USD |
| `7D` | `0.3205` | 12,100,000.00 USD | 0.00 USD | 12,100,000.00 USD | 94,770.00 USD | 59,200.00 USD | 130,760.00 USD |
| `1D` | `0.3209` | 8,450,000.00 USD | 0.00 USD | 8,450,000.00 USD | 59,320.00 USD | 16,590.00 USD | 40,220.00 USD |
| `7D` | `0.3211` | 11,820,000.00 USD | 0.00 USD | 11,820,000.00 USD | 562,620.00 USD | 117,230.00 USD | 244,340.00 USD |
| `1D` | `0.3213` | 8,330,000.00 USD | 0.00 USD | 8,330,000.00 USD | 914.92 USD | 30,340.00 USD | 107,830.00 USD |
| `1D` | `0.3217` | 8,190,000.00 USD | 0.00 USD | 8,190,000.00 USD | 5,550.00 USD | 33,860.00 USD | 70,540.00 USD |
| `7D` | `0.3217` | 10,890,000.00 USD | 0.00 USD | 10,890,000.00 USD | 284,850.00 USD | 58,690.00 USD | 107,900.00 USD |
| `1D` | `0.3221` | 8,080,000.00 USD | 0.00 USD | 8,080,000.00 USD | 97,480.00 USD | 25,650.00 USD | 72,520.00 USD |
| `7D` | `0.3223` | 10,440,000.00 USD | 0.00 USD | 10,440,000.00 USD | 643,460.00 USD | 196,690.00 USD | 103,370.00 USD |
| `1D` | `0.3225` | 7,890,000.00 USD | 0.00 USD | 7,890,000.00 USD | 70,750.00 USD | 19,600.00 USD | 202,490.00 USD |
| `1D` | `0.3229` | 7,600,000.00 USD | 0.00 USD | 7,600,000.00 USD | 91,010.00 USD | 46,020.00 USD | 86,810.00 USD |
| `7D` | `0.3229` | 9,500,000.00 USD | 0.00 USD | 9,500,000.00 USD | 859,960.00 USD | 299,190.00 USD | 385,680.00 USD |
| `1D` | `0.3233` | 7,370,000.00 USD | 0.00 USD | 7,370,000.00 USD | 56,470.00 USD | 13,130.00 USD | 49,900.00 USD |
| `7D` | `0.3235` | 7,950,000.00 USD | 0.00 USD | 7,950,000.00 USD | 709,160.00 USD | 213,370.00 USD | 371,680.00 USD |
| `1D` | `0.3237` | 7,250,000.00 USD | 0.00 USD | 7,250,000.00 USD | 6,420.00 USD | 74,740.00 USD | 171,270.00 USD |
| `1D` | `0.3241` | 7,000,000.00 USD | 0.00 USD | 7,000,000.00 USD | 966.93 USD | 27,720.00 USD | 119,400.00 USD |
| `7D` | `0.3241` | 6,660,000.00 USD | 0.00 USD | 6,660,000.00 USD | 432,660.00 USD | 149,860.00 USD | 138,560.00 USD |
| `1D` | `0.3245` | 6,850,000.00 USD | 0.00 USD | 6,850,000.00 USD | 248,280.00 USD | 54,650.00 USD | 216,640.00 USD |
| `7D` | `0.3247` | 5,940,000.00 USD | 0.00 USD | 5,940,000.00 USD | 849,100.00 USD | 127,310.00 USD | 353,590.00 USD |
| `1D` | `0.3249` | 6,330,000.00 USD | 0.00 USD | 6,330,000.00 USD | 835,170.00 USD | 107,030.00 USD | 192,010.00 USD |
| `1D` | `0.3253` | 5,200,000.00 USD | 0.00 USD | 5,200,000.00 USD | 194,860.00 USD | 95,420.00 USD | 373,460.00 USD |
| `7D` | `0.3253` | 4,610,000.00 USD | 0.00 USD | 4,610,000.00 USD | 1,220,000.00 USD | 137,440.00 USD | 241,690.00 USD |
| `1D` | `0.3257` | 4,530,000.00 USD | 0.00 USD | 4,530,000.00 USD | 312,250.00 USD | 43,390.00 USD | 229,640.00 USD |
| `7D` | `0.3259` | 3,010,000.00 USD | 0.00 USD | 3,010,000.00 USD | 182,240.00 USD | 92,250.00 USD | 346,980.00 USD |
| `1D` | `0.3261` | 3,950,000.00 USD | 0.00 USD | 3,950,000.00 USD | 79,940.00 USD | 151,680.00 USD | 319,940.00 USD |
| `1D` | `0.3265` | 3,400,000.00 USD | 0.00 USD | 3,400,000.00 USD | 43,780.00 USD | 72,290.00 USD | 141,160.00 USD |
| `7D` | `0.3265` | 2,390,000.00 USD | 0.00 USD | 2,390,000.00 USD | 79,990.00 USD | 19,240.00 USD | 93,040.00 USD |
| `1D` | `0.3269` | 3,140,000.00 USD | 0.00 USD | 3,140,000.00 USD | 124,870.00 USD | 143,860.00 USD | 378,850.00 USD |
| `7D` | `0.3271` | 2,190,000.00 USD | 0.00 USD | 2,190,000.00 USD | 189,530.00 USD | 138,680.00 USD | 261,530.00 USD |
| `1D` | `0.3273` | 2,490,000.00 USD | 0.00 USD | 2,490,000.00 USD | 38,550.00 USD | 24,720.00 USD | 174,670.00 USD |
| `1D` | `0.3277` | 2,250,000.00 USD | 0.00 USD | 2,250,000.00 USD | 260,400.00 USD | 46,830.00 USD | 133,800.00 USD |
| `7D` | `0.3277` | 1,600,000.00 USD | 0.00 USD | 1,600,000.00 USD | 0.00 USD | 29,390.00 USD | 85,620.00 USD |
| `1D` | `0.3281` | 1,810,000.00 USD | 0.00 USD | 1,810,000.00 USD | 0.00 USD | 57,800.00 USD | 16,760.00 USD |
| `7D` | `0.3283` | 1,490,000.00 USD | 0.00 USD | 1,490,000.00 USD | 89,030.00 USD | 25,670.00 USD | 275,050.00 USD |
| `1D` | `0.3285` | 1,740,000.00 USD | 0.00 USD | 1,740,000.00 USD | 0.00 USD | 48,460.00 USD | 30,620.00 USD |
| `1D` | `0.3289` | 1,660,000.00 USD | 0.00 USD | 1,660,000.00 USD | 155,850.00 USD | 6,250.00 USD | 155,080.00 USD |
| `7D` | `0.3289` | 1,100,000.00 USD | 0.00 USD | 1,100,000.00 USD | 2,520.00 USD | 43,290.00 USD | 0.00 USD |
| `1D` | `0.3293` | 1,340,000.00 USD | 0.00 USD | 1,340,000.00 USD | 977.29 USD | 32,950.00 USD | 80,060.00 USD |
| `7D` | `0.3295` | 1,050,000.00 USD | 0.00 USD | 1,050,000.00 USD | 254,700.00 USD | 83,080.00 USD | 0.00 USD |
| `1D` | `0.3297` | 1,230,000.00 USD | 0.00 USD | 1,230,000.00 USD | 166,310.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3301` | 1,060,000.00 USD | 0.00 USD | 1,060,000.00 USD | 36,460.00 USD | 13,760.00 USD | 30,950.00 USD |
| `7D` | `0.3301` | 716,630.00 USD | 0.00 USD | 716,630.00 USD | 184,120.00 USD | 9,050.00 USD | 0.00 USD |
| `1D` | `0.3305` | 981,540.00 USD | 0.00 USD | 981,540.00 USD | 112,020.00 USD | 16,160.00 USD | 74,690.00 USD |
| `7D` | `0.3307` | 523,460.00 USD | 0.00 USD | 523,460.00 USD | 167,950.00 USD | 10,690.00 USD | 294,170.00 USD |
| `1D` | `0.3309` | 778,660.00 USD | 0.00 USD | 778,660.00 USD | 11,600.00 USD | 48,170.00 USD | 444,920.00 USD |
| `1D` | `0.3313` | 273,960.00 USD | 0.00 USD | 273,960.00 USD | 0.00 USD | 128,440.00 USD | 86,570.00 USD |
| `7D` | `0.3313` | 50,650.00 USD | 0.00 USD | 50,650.00 USD | 0.00 USD | 50,650.00 USD | 0.00 USD |
| `1D` | `0.3317` | 58,950.00 USD | 0.00 USD | 58,950.00 USD | 0.00 USD | 58,950.00 USD | 0.00 USD |
| `7D` | `0.3318` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3319` | 57,890.00 USD | 57,890.00 USD | 0.00 USD | 0.00 USD | 57,890.00 USD | 0.00 USD |
| `1D` | `0.3320` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3357` | 144,280.00 USD | 144,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 144,280.00 USD |
| `1D` | `0.3369` | 217,200.00 USD | 217,200.00 USD | 0.00 USD | 72,920.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3377` | 546,840.00 USD | 546,840.00 USD | 0.00 USD | 329,640.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3379` | 79,280.00 USD | 79,280.00 USD | 0.00 USD | 0.00 USD | 21,390.00 USD | 0.00 USD |
| `1D` | `0.3381` | 618,740.00 USD | 618,740.00 USD | 0.00 USD | 71,900.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3385` | 657,930.00 USD | 657,930.00 USD | 0.00 USD | 0.00 USD | 11,160.00 USD | 28,030.00 USD |
| `7D` | `0.3385` | 204,930.00 USD | 204,930.00 USD | 0.00 USD | 125,650.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3389` | 825,160.00 USD | 825,160.00 USD | 0.00 USD | 139,840.00 USD | 0.00 USD | 27,380.00 USD |
| `7D` | `0.3391` | 439,600.00 USD | 439,600.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 234,660.00 USD |
| `1D` | `0.3393` | 1,340,000.00 USD | 1,340,000.00 USD | 0.00 USD | 52,860.00 USD | 141,880.00 USD | 319,940.00 USD |
| `1D` | `0.3397` | 1,370,000.00 USD | 1,370,000.00 USD | 0.00 USD | 27,080.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3397` | 948,010.00 USD | 948,010.00 USD | 0.00 USD | 257,550.00 USD | 250,860.00 USD | 0.00 USD |
| `1D` | `0.3401` | 1,620,000.00 USD | 1,620,000.00 USD | 0.00 USD | 43,780.00 USD | 83,470.00 USD | 130,150.00 USD |
| `7D` | `0.3403` | 2,340,000.00 USD | 2,340,000.00 USD | 0.00 USD | 1,070,000.00 USD | 103,630.00 USD | 223,390.00 USD |
| `1D` | `0.3405` | 2,090,000.00 USD | 2,090,000.00 USD | 0.00 USD | 134,550.00 USD | 14,270.00 USD | 319,770.00 USD |
| `1D` | `0.3409` | 2,230,000.00 USD | 2,230,000.00 USD | 0.00 USD | 126,850.00 USD | 9,200.00 USD | 0.00 USD |
| `7D` | `0.3409` | 2,820,000.00 USD | 2,820,000.00 USD | 0.00 USD | 0.00 USD | 29,390.00 USD | 446,990.00 USD |
| `1D` | `0.3413` | 2,490,000.00 USD | 2,490,000.00 USD | 0.00 USD | 173,130.00 USD | 11,360.00 USD | 80,830.00 USD |
| `7D` | `0.3415` | 2,900,000.00 USD | 2,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 85,620.00 USD |
| `1D` | `0.3417` | 3,150,000.00 USD | 3,150,000.00 USD | 0.00 USD | 585,390.00 USD | 25,060.00 USD | 44,630.00 USD |
| `1D` | `0.3421` | 3,260,000.00 USD | 3,260,000.00 USD | 0.00 USD | 71,180.00 USD | 39,260.00 USD | 0.00 USD |
| `7D` | `0.3421` | 2,950,000.00 USD | 2,950,000.00 USD | 0.00 USD | 0.00 USD | 43,290.00 USD | 0.00 USD |
| `1D` | `0.3425` | 3,390,000.00 USD | 3,390,000.00 USD | 0.00 USD | 0.00 USD | 132,230.00 USD | 0.00 USD |
| `7D` | `0.3427` | 3,040,000.00 USD | 3,040,000.00 USD | 0.00 USD | 0.00 USD | 92,380.00 USD | 0.00 USD |
| `1D` | `0.3429` | 3,560,000.00 USD | 3,560,000.00 USD | 0.00 USD | 60,980.00 USD | 104,590.00 USD | 0.00 USD |
| `1D` | `0.3433` | 3,840,000.00 USD | 3,840,000.00 USD | 0.00 USD | 105,330.00 USD | 149,150.00 USD | 30,950.00 USD |
| `7D` | `0.3433` | 3,290,000.00 USD | 3,290,000.00 USD | 0.00 USD | 254,700.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3437` | 3,970,000.00 USD | 3,970,000.00 USD | 0.00 USD | 0.00 USD | 63,370.00 USD | 62,980.00 USD |
| `1D` | `0.3441` | 4,010,000.00 USD | 4,010,000.00 USD | 0.00 USD | 0.00 USD | 36,240.00 USD | 0.00 USD |
| `1D` | `0.3445` | 4,140,000.00 USD | 4,140,000.00 USD | 0.00 USD | 0.00 USD | 28,520.00 USD | 106,240.00 USD |
| `7D` | `0.3445` | 3,400,000.00 USD | 3,400,000.00 USD | 0.00 USD | 103,130.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3449` | 4,360,000.00 USD | 4,360,000.00 USD | 0.00 USD | 35,950.00 USD | 92,440.00 USD | 86,570.00 USD |
| `7D` | `0.3451` | 3,490,000.00 USD | 3,490,000.00 USD | 0.00 USD | 62,830.00 USD | 28,550.00 USD | 0.00 USD |
| `1D` | `0.3453` | 4,580,000.00 USD | 4,580,000.00 USD | 0.00 USD | 92,350.00 USD | 47,460.00 USD | 84,370.00 USD |
| `1D` | `0.3457` | 5,110,000.00 USD | 5,110,000.00 USD | 0.00 USD | 48,240.00 USD | 33,930.00 USD | 452,590.00 USD |
| `7D` | `0.3457` | 3,850,000.00 USD | 3,850,000.00 USD | 0.00 USD | 0.00 USD | 29,340.00 USD | 332,190.00 USD |
| `1D` | `0.3461` | 5,490,000.00 USD | 5,490,000.00 USD | 0.00 USD | 168,310.00 USD | 71,330.00 USD | 135,270.00 USD |
| `1D` | `0.3465` | 5,540,000.00 USD | 5,540,000.00 USD | 0.00 USD | 21,890.00 USD | 25,190.00 USD | 0.00 USD |
| `1D` | `0.3469` | 5,650,000.00 USD | 5,650,000.00 USD | 0.00 USD | 0.00 USD | 42,550.00 USD | 75,450.00 USD |
| `7D` | `0.3469` | 4,040,000.00 USD | 4,040,000.00 USD | 0.00 USD | 60,310.00 USD | 51,820.00 USD | 75,520.00 USD |
| `1D` | `0.3473` | 5,720,000.00 USD | 5,720,000.00 USD | 0.00 USD | 0.00 USD | 35,130.00 USD | 31,160.00 USD |
| `7D` | `0.3475` | 4,080,000.00 USD | 4,080,000.00 USD | 0.00 USD | 0.00 USD | 40,540.00 USD | 0.00 USD |
| `1D` | `0.3477` | 5,840,000.00 USD | 5,840,000.00 USD | 0.00 USD | 23,470.00 USD | 36,050.00 USD | 63,820.00 USD |
| `1D` | `0.3481` | 5,940,000.00 USD | 5,940,000.00 USD | 0.00 USD | 0.00 USD | 29,570.00 USD | 64,980.00 USD |
| `7D` | `0.3481` | 4,160,000.00 USD | 4,160,000.00 USD | 0.00 USD | 19,060.00 USD | 14,700.00 USD | 42,810.00 USD |
| `1D` | `0.3485` | 5,950,000.00 USD | 5,950,000.00 USD | 0.00 USD | 0.00 USD | 16,180.00 USD | 0.00 USD |
| `7D` | `0.3487` | 4,180,000.00 USD | 4,180,000.00 USD | 0.00 USD | 6,050.00 USD | 21,650.00 USD | 0.00 USD |
| `1D` | `0.3489` | 6,070,000.00 USD | 6,070,000.00 USD | 0.00 USD | 41,500.00 USD | 16,070.00 USD | 61,240.00 USD |
| `1D` | `0.3493` | 6,100,000.00 USD | 6,100,000.00 USD | 0.00 USD | 3,620.00 USD | 19,600.00 USD | 0.00 USD |
| `7D` | `0.3493` | 4,210,000.00 USD | 4,210,000.00 USD | 0.00 USD | 5,810.00 USD | 24,660.00 USD | 0.00 USD |
| `1D` | `0.3497` | 6,580,000.00 USD | 6,580,000.00 USD | 0.00 USD | 32,290.00 USD | 0.00 USD | 454,680.00 USD |
| `7D` | `0.3499` | 4,340,000.00 USD | 4,340,000.00 USD | 0.00 USD | 127,350.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3501` | 6,690,000.00 USD | 6,690,000.00 USD | 0.00 USD | 52,670.00 USD | 0.00 USD | 50,760.00 USD |
| `1D` | `0.3505` | 6,800,000.00 USD | 6,800,000.00 USD | 0.00 USD | 74,220.00 USD | 6,880.00 USD | 31,490.00 USD |
| `7D` | `0.3505` | 4,350,000.00 USD | 4,350,000.00 USD | 0.00 USD | 5,650.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3509` | 6,810,000.00 USD | 6,810,000.00 USD | 0.00 USD | 1,700.00 USD | 12,400.00 USD | 0.00 USD |
| `7D` | `0.3511` | 5,320,000.00 USD | 5,320,000.00 USD | 0.00 USD | 704,750.00 USD | 0.00 USD | 271,800.00 USD |
| `1D` | `0.3513` | 6,890,000.00 USD | 6,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 76,540.00 USD |
| `1D` | `0.3517` | 6,970,000.00 USD | 6,970,000.00 USD | 0.00 USD | 21,910.00 USD | 5,720.00 USD | 52,910.00 USD |
| `7D` | `0.3517` | 5,330,000.00 USD | 5,330,000.00 USD | 0.00 USD | 7,560.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3521` | 7,040,000.00 USD | 7,040,000.00 USD | 0.00 USD | 32,770.00 USD | 21,980.00 USD | 18,700.00 USD |
| `7D` | `0.3523` | 5,750,000.00 USD | 5,750,000.00 USD | 0.00 USD | 279,190.00 USD | 28,950.00 USD | 107,430.00 USD |
| `1D` | `0.3525` | 7,080,000.00 USD | 7,080,000.00 USD | 0.00 USD | 3,970.00 USD | 6,280.00 USD | 28,910.00 USD |
| `1D` | `0.3529` | 7,240,000.00 USD | 7,240,000.00 USD | 0.00 USD | 102,610.00 USD | 52,710.00 USD | 0.00 USD |
| `7D` | `0.3529` | 5,750,000.00 USD | 5,750,000.00 USD | 0.00 USD | 2,170.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3533` | 7,440,000.00 USD | 7,440,000.00 USD | 0.00 USD | 67,090.00 USD | 44,040.00 USD | 88,110.00 USD |
| `7D` | `0.3535` | 6,030,000.00 USD | 6,030,000.00 USD | 0.00 USD | 11,650.00 USD | 77,960.00 USD | 187,450.00 USD |
| `1D` | `0.3537` | 7,720,000.00 USD | 7,720,000.00 USD | 0.00 USD | 61,430.00 USD | 29,120.00 USD | 195,270.00 USD |
| `1D` | `0.3541` | 7,880,000.00 USD | 7,880,000.00 USD | 0.00 USD | 76,770.00 USD | 80,430.00 USD | 0.00 USD |
| `7D` | `0.3541` | 6,950,000.00 USD | 6,950,000.00 USD | 0.00 USD | 808,160.00 USD | 118,370.00 USD | 0.00 USD |
| `1D` | `0.3545` | 8,000,000.00 USD | 8,000,000.00 USD | 0.00 USD | 4,630.00 USD | 44,140.00 USD | 69,820.00 USD |
| `7D` | `0.3547` | 7,240,000.00 USD | 7,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 288,450.00 USD |
| `1D` | `0.3549` | 8,060,000.00 USD | 8,060,000.00 USD | 0.00 USD | 5,680.00 USD | 53,970.00 USD | 0.00 USD |
| `1D` | `0.3553` | 8,150,000.00 USD | 8,150,000.00 USD | 0.00 USD | 21,530.00 USD | 24,430.00 USD | 47,950.00 USD |
| `7D` | `0.3553` | 7,360,000.00 USD | 7,360,000.00 USD | 0.00 USD | 4,360.00 USD | 117,050.00 USD | 0.00 USD |
| `1D` | `0.3557` | 8,190,000.00 USD | 8,190,000.00 USD | 0.00 USD | 0.00 USD | 38,770.00 USD | 0.00 USD |
| `7D` | `0.3559` | 7,370,000.00 USD | 7,370,000.00 USD | 0.00 USD | 4,230.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3561` | 8,320,000.00 USD | 8,320,000.00 USD | 0.00 USD | 331.60 USD | 25,000.00 USD | 106,140.00 USD |
| `1D` | `0.3565` | 8,380,000.00 USD | 8,380,000.00 USD | 0.00 USD | 2,250.00 USD | 11,630.00 USD | 39,520.00 USD |
| `7D` | `0.3565` | 7,410,000.00 USD | 7,410,000.00 USD | 0.00 USD | 0.00 USD | 43,060.00 USD | 0.00 USD |
| `1D` | `0.3569` | 8,390,000.00 USD | 8,390,000.00 USD | 0.00 USD | 1,450.00 USD | 6,920.00 USD | 0.00 USD |
| `7D` | `0.3571` | 7,420,000.00 USD | 7,420,000.00 USD | 0.00 USD | 8,530.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3573` | 8,530,000.00 USD | 8,530,000.00 USD | 0.00 USD | 131,970.00 USD | 9,250.00 USD | 0.00 USD |
| `1D` | `0.3577` | 8,570,000.00 USD | 8,570,000.00 USD | 0.00 USD | 31,460.00 USD | 9,130.00 USD | 0.00 USD |
| `7D` | `0.3577` | 7,540,000.00 USD | 7,540,000.00 USD | 0.00 USD | 124,630.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3581` | 8,610,000.00 USD | 8,610,000.00 USD | 0.00 USD | 3,560.00 USD | 0.00 USD | 38,950.00 USD |
| `7D` | `0.3583` | 7,680,000.00 USD | 7,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 135,900.00 USD |
| `1D` | `0.3585` | 8,640,000.00 USD | 8,640,000.00 USD | 0.00 USD | 18,570.00 USD | 14,930.00 USD | 0.00 USD |
| `1D` | `0.3589` | 8,660,000.00 USD | 8,660,000.00 USD | 0.00 USD | 3,780.00 USD | 15,750.00 USD | 0.00 USD |
| `7D` | `0.3589` | 8,050,000.00 USD | 8,050,000.00 USD | 0.00 USD | 1,610.00 USD | 50,650.00 USD | 320,430.00 USD |
| `1D` | `0.3593` | 8,860,000.00 USD | 8,860,000.00 USD | 0.00 USD | 66,040.00 USD | 0.00 USD | 133,180.00 USD |
| `7D` | `0.3595` | 8,200,000.00 USD | 8,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 146,290.00 USD |
| `1D` | `0.3597` | 8,970,000.00 USD | 8,970,000.00 USD | 0.00 USD | 91,900.00 USD | 12,460.00 USD | 0.00 USD |
| `1D` | `0.3601` | 9,170,000.00 USD | 9,170,000.00 USD | 0.00 USD | 1,160.00 USD | 36,520.00 USD | 163,110.00 USD |
| `7D` | `0.3601` | 8,700,000.00 USD | 8,700,000.00 USD | 0.00 USD | 0.00 USD | 161,200.00 USD | 338,540.00 USD |
| `1D` | `0.3605` | 9,360,000.00 USD | 9,360,000.00 USD | 0.00 USD | 61,130.00 USD | 32,860.00 USD | 94,650.00 USD |
| `7D` | `0.3607` | 9,090,000.00 USD | 9,090,000.00 USD | 0.00 USD | 325,970.00 USD | 68,030.00 USD | 0.00 USD |
| `1D` | `0.3609` | 9,590,000.00 USD | 9,590,000.00 USD | 0.00 USD | 75,090.00 USD | 25,740.00 USD | 133,760.00 USD |
| `1D` | `0.3613` | 9,860,000.00 USD | 9,860,000.00 USD | 0.00 USD | 10,940.00 USD | 59,640.00 USD | 203,600.00 USD |
| `7D` | `0.3613` | 9,780,000.00 USD | 9,780,000.00 USD | 0.00 USD | 73,540.00 USD | 330,040.00 USD | 288,930.00 USD |
| `1D` | `0.3617` | 10,240,000.00 USD | 10,240,000.00 USD | 0.00 USD | 225,600.00 USD | 50,630.00 USD | 104,310.00 USD |
| `7D` | `0.3619` | 9,990,000.00 USD | 9,990,000.00 USD | 0.00 USD | 0.00 USD | 209,940.00 USD | 0.00 USD |
| `1D` | `0.3621` | 10,540,000.00 USD | 10,540,000.00 USD | 0.00 USD | 143,010.00 USD | 75,820.00 USD | 71,510.00 USD |
| `1D` | `0.3625` | 10,680,000.00 USD | 10,680,000.00 USD | 0.00 USD | 99,950.00 USD | 49,330.00 USD | 0.00 USD |
| `7D` | `0.3625` | 10,190,000.00 USD | 10,190,000.00 USD | 0.00 USD | 0.00 USD | 191,880.00 USD | 0.00 USD |
| `1D` | `0.3629` | 11,920,000.00 USD | 11,920,000.00 USD | 0.00 USD | 1,120,000.00 USD | 35,410.00 USD | 79,610.00 USD |
| `7D` | `0.3631` | 10,300,000.00 USD | 10,300,000.00 USD | 0.00 USD | 0.00 USD | 114,740.00 USD | 0.00 USD |
| `1D` | `0.3633` | 12,330,000.00 USD | 12,330,000.00 USD | 0.00 USD | 144,090.00 USD | 72,670.00 USD | 199,780.00 USD |
| `1D` | `0.3637` | 12,580,000.00 USD | 12,580,000.00 USD | 0.00 USD | 183,690.00 USD | 65,110.00 USD | 0.00 USD |
| `7D` | `0.3637` | 10,320,000.00 USD | 10,320,000.00 USD | 0.00 USD | 1,540.00 USD | 21,530.00 USD | 0.00 USD |
| `1D` | `0.3641` | 12,950,000.00 USD | 12,950,000.00 USD | 0.00 USD | 85,150.00 USD | 206,820.00 USD | 76,240.00 USD |
| `7D` | `0.3643` | 11,120,000.00 USD | 11,120,000.00 USD | 0.00 USD | 3,350.00 USD | 0.00 USD | 789,140.00 USD |
| `1D` | `0.3645` | 13,260,000.00 USD | 13,260,000.00 USD | 0.00 USD | 255,500.00 USD | 16,650.00 USD | 35,280.00 USD |
| `1D` | `0.3649` | 13,610,000.00 USD | 13,610,000.00 USD | 0.00 USD | 95,770.00 USD | 59,680.00 USD | 195,820.00 USD |
| `7D` | `0.3649` | 11,300,000.00 USD | 11,300,000.00 USD | 0.00 USD | 181,300.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3653` | 14,100,000.00 USD | 14,100,000.00 USD | 0.00 USD | 301,080.00 USD | 19,500.00 USD | 165,330.00 USD |
| `7D` | `0.3655` | 12,090,000.00 USD | 12,090,000.00 USD | 0.00 USD | 679,620.00 USD | 112,770.00 USD | 0.00 USD |
| `1D` | `0.3657` | 14,590,000.00 USD | 14,590,000.00 USD | 0.00 USD | 186,020.00 USD | 149,310.00 USD | 163,370.00 USD |
| `1D` | `0.3661` | 14,980,000.00 USD | 14,980,000.00 USD | 0.00 USD | 265,410.00 USD | 55,900.00 USD | 67,180.00 USD |
| `7D` | `0.3661` | 12,980,000.00 USD | 12,980,000.00 USD | 0.00 USD | 687,450.00 USD | 0.00 USD | 207,150.00 USD |
| `1D` | `0.3665` | 15,610,000.00 USD | 15,610,000.00 USD | 0.00 USD | 468,570.00 USD | 113,200.00 USD | 49,800.00 USD |
| `7D` | `0.3667` | 13,520,000.00 USD | 13,520,000.00 USD | 0.00 USD | 422,000.00 USD | 15,390.00 USD | 103,350.00 USD |
| `1D` | `0.3669` | 16,020,000.00 USD | 16,020,000.00 USD | 0.00 USD | 98,960.00 USD | 26,330.00 USD | 281,260.00 USD |
| `1D` | `0.3673` | 16,320,000.00 USD | 16,320,000.00 USD | 0.00 USD | 41,260.00 USD | 102,840.00 USD | 158,510.00 USD |
| `7D` | `0.3673` | 14,210,000.00 USD | 14,210,000.00 USD | 0.00 USD | 511,100.00 USD | 53,040.00 USD | 122,410.00 USD |
| `1D` | `0.3677` | 17,040,000.00 USD | 17,040,000.00 USD | 0.00 USD | 483,210.00 USD | 36,750.00 USD | 191,130.00 USD |
| `7D` | `0.3679` | 14,470,000.00 USD | 14,470,000.00 USD | 0.00 USD | 257,550.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3681` | 17,520,000.00 USD | 17,520,000.00 USD | 0.00 USD | 293,500.00 USD | 87,330.00 USD | 103,470.00 USD |
| `1D` | `0.3685` | 18,070,000.00 USD | 18,070,000.00 USD | 0.00 USD | 327,450.00 USD | 152,380.00 USD | 74,230.00 USD |
| `7D` | `0.3685` | 14,650,000.00 USD | 14,650,000.00 USD | 0.00 USD | 2,700.00 USD | 102,650.00 USD | 72,350.00 USD |
| `1D` | `0.3689` | 18,590,000.00 USD | 18,590,000.00 USD | 0.00 USD | 404,300.00 USD | 56,330.00 USD | 52,150.00 USD |
| `7D` | `0.3691` | 15,060,000.00 USD | 15,060,000.00 USD | 0.00 USD | 148,800.00 USD | 261,530.00 USD | 0.00 USD |
| `1D` | `0.3693` | 18,690,000.00 USD | 18,690,000.00 USD | 0.00 USD | 79,910.00 USD | 4,540.00 USD | 23,760.00 USD |
| `1D` | `0.3697` | 18,930,000.00 USD | 18,930,000.00 USD | 0.00 USD | 155,550.00 USD | 83,650.00 USD | 0.00 USD |
| `7D` | `0.3697` | 15,220,000.00 USD | 15,220,000.00 USD | 0.00 USD | 736.13 USD | 163,180.00 USD | 0.00 USD |
| `1D` | `0.3701` | 19,690,000.00 USD | 19,690,000.00 USD | 0.00 USD | 527,250.00 USD | 196,170.00 USD | 27,870.00 USD |
| `7D` | `0.3703` | 15,270,000.00 USD | 15,270,000.00 USD | 0.00 USD | 50,940.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3705` | 20,500,000.00 USD | 20,500,000.00 USD | 0.00 USD | 249,050.00 USD | 2,750.00 USD | 560,920.00 USD |
| `1D` | `0.3709` | 20,640,000.00 USD | 20,640,000.00 USD | 0.00 USD | 109,790.00 USD | 24,570.00 USD | 12,600.00 USD |
| `1D` | `0.3713` | 22,020,000.00 USD | 22,020,000.00 USD | 0.00 USD | 481,930.00 USD | 90,010.00 USD | 804,260.00 USD |
| `7D` | `0.3715` | 15,670,000.00 USD | 15,670,000.00 USD | 0.00 USD | 1,320.00 USD | 0.00 USD | 394,570.00 USD |
| `1D` | `0.3717` | 22,540,000.00 USD | 22,540,000.00 USD | 0.00 USD | 44,520.00 USD | 220,760.00 USD | 250,340.00 USD |
| `1D` | `0.3721` | 22,680,000.00 USD | 22,680,000.00 USD | 0.00 USD | 0.00 USD | 62,750.00 USD | 85,090.00 USD |
| `7D` | `0.3721` | 16,420,000.00 USD | 16,420,000.00 USD | 0.00 USD | 5,330.00 USD | 0.00 USD | 747,740.00 USD |
| `1D` | `0.3725` | 23,740,000.00 USD | 23,740,000.00 USD | 0.00 USD | 504,840.00 USD | 31,730.00 USD | 517,550.00 USD |
| `1D` | `0.3726` | 23,790,000.00 USD | 23,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 50,000.00 USD |
| `7D` | `0.3727` | 16,700,000.00 USD | 16,700,000.00 USD | 0.00 USD | 213,190.00 USD | 0.00 USD | 66,870.00 USD |
| `7D` | `0.3733` | 16,890,000.00 USD | 16,890,000.00 USD | 0.00 USD | 188,670.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3739` | 17,360,000.00 USD | 17,360,000.00 USD | 0.00 USD | 241,260.00 USD | 7,690.00 USD | 218,010.00 USD |
| `7D` | `0.3745` | 17,760,000.00 USD | 17,760,000.00 USD | 0.00 USD | 248,660.00 USD | 115,430.00 USD | 37,210.00 USD |
| `7D` | `0.3757` | 18,060,000.00 USD | 18,060,000.00 USD | 0.00 USD | 535.97 USD | 0.00 USD | 302,240.00 USD |
| `7D` | `0.3763` | 18,240,000.00 USD | 18,240,000.00 USD | 0.00 USD | 35,610.00 USD | 92,380.00 USD | 50,200.00 USD |
| `7D` | `0.3769` | 18,240,000.00 USD | 18,240,000.00 USD | 0.00 USD | 1,160.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3781` | 18,270,000.00 USD | 18,270,000.00 USD | 0.00 USD | 29,330.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3787` | 18,420,000.00 USD | 18,420,000.00 USD | 0.00 USD | 89,270.00 USD | 3,620.00 USD | 54,360.00 USD |
| `7D` | `0.3793` | 18,880,000.00 USD | 18,880,000.00 USD | 0.00 USD | 27,760.00 USD | 0.00 USD | 437,170.00 USD |
| `7D` | `0.3805` | 18,880,000.00 USD | 18,880,000.00 USD | 0.00 USD | 768.95 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3811` | 18,920,000.00 USD | 18,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 37,490.00 USD |
| `7D` | `0.3817` | 19,100,000.00 USD | 19,100,000.00 USD | 0.00 USD | 156,690.00 USD | 19,620.00 USD | 0.00 USD |
| `7D` | `0.3823` | 19,210,000.00 USD | 19,210,000.00 USD | 0.00 USD | 0.00 USD | 54,460.00 USD | 57,690.00 USD |
| `7D` | `0.3829` | 19,210,000.00 USD | 19,210,000.00 USD | 0.00 USD | 1,750.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3841` | 19,210,000.00 USD | 19,210,000.00 USD | 0.00 USD | 897.53 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3859` | 19,280,000.00 USD | 19,280,000.00 USD | 0.00 USD | 70,850.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3865` | 19,440,000.00 USD | 19,440,000.00 USD | 0.00 USD | 112,700.00 USD | 45,110.00 USD | 0.00 USD |
| `7D` | `0.3877` | 19,560,000.00 USD | 19,560,000.00 USD | 0.00 USD | 123,270.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3883` | 19,610,000.00 USD | 19,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 48,960.00 USD |
| `7D` | `0.3889` | 19,710,000.00 USD | 19,710,000.00 USD | 0.00 USD | 103,020.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3895` | 19,760,000.00 USD | 19,760,000.00 USD | 0.00 USD | 2,670.00 USD | 41,060.00 USD | 0.00 USD |
| `7D` | `0.3901` | 19,820,000.00 USD | 19,820,000.00 USD | 0.00 USD | 59,060.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3907` | 19,930,000.00 USD | 19,930,000.00 USD | 0.00 USD | 0.00 USD | 50,210.00 USD | 63,420.00 USD |
| `7D` | `0.3925` | 20,090,000.00 USD | 20,090,000.00 USD | 0.00 USD | 342.70 USD | 1,190.00 USD | 157,830.00 USD |
| `7D` | `0.3931` | 20,120,000.00 USD | 20,120,000.00 USD | 0.00 USD | 24,850.00 USD | 2,840.00 USD | 2,800.00 USD |
| `7D` | `0.3937` | 20,150,000.00 USD | 20,150,000.00 USD | 0.00 USD | 22,060.00 USD | 1,070.00 USD | 5,410.00 USD |
| `7D` | `0.3943` | 20,180,000.00 USD | 20,180,000.00 USD | 0.00 USD | 24,300.00 USD | 3,090.00 USD | 784.19 USD |
| `7D` | `0.3949` | 20,310,000.00 USD | 20,310,000.00 USD | 0.00 USD | 110,580.00 USD | 8,290.00 USD | 18,490.00 USD |
| `7D` | `0.3955` | 20,540,000.00 USD | 20,540,000.00 USD | 0.00 USD | 106,740.00 USD | 10,160.00 USD | 112,040.00 USD |
| `7D` | `0.3961` | 20,730,000.00 USD | 20,730,000.00 USD | 0.00 USD | 122,580.00 USD | 54,030.00 USD | 7,040.00 USD |
| `7D` | `0.3967` | 20,750,000.00 USD | 20,750,000.00 USD | 0.00 USD | 12,270.00 USD | 6,010.00 USD | 4,840.00 USD |
| `7D` | `0.3973` | 20,890,000.00 USD | 20,890,000.00 USD | 0.00 USD | 16,620.00 USD | 1,440.00 USD | 123,860.00 USD |
| `7D` | `0.3979` | 21,000,000.00 USD | 21,000,000.00 USD | 0.00 USD | 57,520.00 USD | 38,460.00 USD | 11,500.00 USD |
| `7D` | `0.3985` | 21,040,000.00 USD | 21,040,000.00 USD | 0.00 USD | 23,360.00 USD | 3,160.00 USD | 10,200.00 USD |
| `7D` | `0.3991` | 21,060,000.00 USD | 21,060,000.00 USD | 0.00 USD | 0.00 USD | 1,100.00 USD | 24,490.00 USD |
| `7D` | `0.4001` | 21,070,000.00 USD | 21,070,000.00 USD | 0.00 USD | 0.00 USD | 7,690.00 USD | 0.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `405.26M` | Total OI Tokens: `1,219,714,658.5 TRX`
  * 1h OI Change: `+0.05%` | 4h OI Change: `-4.81%` | 24h OI Change: `+41.51%`
  * Exchange Breakdown: Binance=`104.14M` | Bybit=`83.34M` | OKX=`25.54M` | Hyperliquid=`17.96M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `-8.82K` | Last 24h: `-632.70K` | Last 3d: `-621.37K` | Last 7d: `-893.87K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0040%` | **USDT OKX** | `-0.2566%` |
| **USDT Bybit** | `0.0632%` | **USDT KuCoin** | `-0.0565%` |
| **USDT MEXC** | `0.0038%` | **USDT BingX** | `0.0344%` |
| **USDT Gate** | `-0.1267%` | **USDT Bitget** | `-0.1701%` |
| **CoinM Binance** | `-0.0464%` | **CoinM OKX** | `-` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `TRX` | `48.16%` | `51.84%` | `0.93` | 7,210,000.00 USD |
| `15M` | `Binance` | `56.89%` | `43.11%` | `1.32` | 2,800,000.00 USD |
| `15M` | `OKX` | `33.5%` | `66.5%` | `0.50` | 960,420.00 USD |
| `15M` | `Bybit` | `66.29%` | `33.71%` | `1.97` | 1,040,000.00 USD |
| `15M` | `KuCoin` | `49.64%` | `50.36%` | `0.99` | 178,870.00 USD |
| `15M` | `Gate` | `45.41%` | `54.59%` | `0.83` | 404,180.00 USD |
| `15M` | `Bitget` | `39.86%` | `60.14%` | `0.66` | 273,610.00 USD |
| `15M` | `BingX` | `26.11%` | `73.89%` | `0.35` | 500,480.00 USD |
| `15M` | `MEXC` | `33.61%` | `66.39%` | `0.51` | 35,640.00 USD |
| `15M` | `Bitunix` | `41.11%` | `58.89%` | `0.70` | 83,760.00 USD |
| `15M` | `Hyperliquid` | `17.85%` | `82.15%` | `0.22` | 669,400.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `51.34%` | `48.66%` | `1.06` | 99,270.00 USD |
| `15M` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `WhiteBIT` | `100%` | `0%` | `1.00` | 12,910.00 USD |
| `15M` | `HTX` | `79.1%` | `20.9%` | `3.78` | 51,760.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `84.55%` | `15.45%` | `5.47` | 92,380.00 USD |
| `15M` | `Aster` | `84.04%` | `15.96%` | `5.27` | 3,060.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `85.65%` | `14.35%` | `5.97` | 9,240.00 USD |
| `15M` | `Whale Positions` | `56.89%` | `43.11%` | `1.32` | 2,800,000.00 USD |
| `15M` | `Global Accounts` | `48.16%` | `51.84%` | `0.93` | 7,210,000.00 USD |
| `1H` | `TRX` | `49.23%` | `50.77%` | `0.97` | 14,190,000.00 USD |
| `1H` | `Binance` | `53.34%` | `46.66%` | `1.14` | 5,040,000.00 USD |
| `1H` | `OKX` | `39.18%` | `60.82%` | `0.64` | 827,440.00 USD |
| `1H` | `Bybit` | `55.98%` | `44.02%` | `1.27` | 1,260,000.00 USD |
| `1H` | `KuCoin` | `48.72%` | `51.28%` | `0.95` | 208,800.00 USD |
| `1H` | `Gate` | `39%` | `61%` | `0.64` | 236,230.00 USD |
| `1H` | `Bitget` | `45.27%` | `54.73%` | `0.83` | 318,550.00 USD |
| `1H` | `BingX` | `38.7%` | `61.3%` | `0.63` | 389,850.00 USD |
| `1H` | `MEXC` | `56.51%` | `43.49%` | `1.30` | 1,820,000.00 USD |
| `1H` | `Bitunix` | `49.57%` | `50.43%` | `0.98` | 432,650.00 USD |
| `1H` | `Hyperliquid` | `46.42%` | `53.58%` | `0.87` | 173,530.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `47.78%` | `52.22%` | `0.91` | 2,410,000.00 USD |
| `1H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `WhiteBIT` | `21.03%` | `78.97%` | `0.27` | 794,090.00 USD |
| `1H` | `HTX` | `58.61%` | `41.39%` | `1.42` | 89,670.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `71.13%` | `28.87%` | `2.46` | 168,440.00 USD |
| `1H` | `Aster` | `71.08%` | `28.92%` | `2.46` | 2,610.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `53.73%` | `46.27%` | `1.16` | 13,560.00 USD |
| `1H` | `Whale Positions` | `53.34%` | `46.66%` | `1.14` | 5,040,000.00 USD |
| `1H` | `Global Accounts` | `49.23%` | `50.77%` | `0.97` | 14,190,000.00 USD |
| `4H` | `TRX` | `48.24%` | `51.76%` | `0.93` | 174,200,000.00 USD |
| `4H` | `Binance` | `46.42%` | `53.58%` | `0.87` | 86,370,000.00 USD |
| `4H` | `OKX` | `46.16%` | `53.84%` | `0.86` | 21,400,000.00 USD |
| `4H` | `Bybit` | `51.61%` | `48.39%` | `1.07` | 24,490,000.00 USD |
| `4H` | `KuCoin` | `48.94%` | `51.06%` | `0.96` | 3,050,000.00 USD |
| `4H` | `Gate` | `46.11%` | `53.89%` | `0.86` | 4,790,000.00 USD |
| `4H` | `Bitget` | `50.35%` | `49.65%` | `1.01` | 5,970,000.00 USD |
| `4H` | `BingX` | `34.45%` | `65.55%` | `0.53` | 2,150,000.00 USD |
| `4H` | `MEXC` | `52.18%` | `47.82%` | `1.09` | 1,980,000.00 USD |
| `4H` | `Bitunix` | `49.22%` | `50.78%` | `0.97` | 3,370,000.00 USD |
| `4H` | `Hyperliquid` | `57.03%` | `42.97%` | `1.33` | 13,610,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `50.24%` | `49.76%` | `1.01` | 2,900,000.00 USD |
| `4H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `WhiteBIT` | `52.13%` | `47.87%` | `1.09` | 1,040,000.00 USD |
| `4H` | `HTX` | `45.06%` | `54.94%` | `0.82` | 752,000.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `71.19%` | `28.81%` | `2.47` | 230,200.00 USD |
| `4H` | `Aster` | `40.95%` | `59.05%` | `0.69` | 1,120,000.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `56.97%` | `43.03%` | `1.32` | 983,100.00 USD |
| `4H` | `Whale Positions` | `46.42%` | `53.58%` | `0.87` | 86,370,000.00 USD |
| `4H` | `Global Accounts` | `48.24%` | `51.76%` | `0.93` | 174,200,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `0:00 UTC` | `0.3368` | `0.3366` | `0.3368` | `0.3386` | `0.3356` | 3,996,243.58 USD | 1,588,867.43 USD | 2,407,376.15 USD | -818,508.71 USD | `-20.48%` | `20B / 29S` |
| `5:00 UTC` | `0.3365` | `0.3367` | `0.3365` | `0.3391` | `0.3354` | 5,877,291.83 USD | 2,503,635.13 USD | 3,373,656.70 USD | -870,021.57 USD | `-14.80%` | `12B / 19S` |
| `0:00 UTC` | `0.3359` | `0.3357` | `0.3359` | `0.3380` | `0.3338` | 5,127,554.79 USD | 3,021,220.38 USD | 2,106,334.42 USD | 914,885.96 USD | `+17.84%` | `13B / 15S` |
| `5:00 UTC` | `0.3340` | `0.3335` | `0.3340` | `0.3351` | `0.3325` | 6,370,620.16 USD | 3,546,795.30 USD | 2,823,824.85 USD | 722,970.45 USD | `+11.35%` | `9B / 23S` |
| `0:00 UTC` | `0.3325` | `0.3322` | `0.3325` | `0.3338` | `0.3310` | 7,016,205.26 USD | 3,261,497.62 USD | 3,754,707.64 USD | -493,210.01 USD | `-7.03%` | `21B / 13S` |
| `5:00 UTC` | `0.3370` | `0.3359` | `0.3370` | `0.3378` | `0.3316` | 5,309,391.96 USD | 3,078,017.12 USD | 2,231,374.84 USD | 846,642.29 USD | `+15.95%` | `35B / 9S` |
| `0:00 UTC` | `0.3368` | `0.3360` | `0.3368` | `0.3377` | `0.3336` | 2,717,916.28 USD | 1,271,599.87 USD | 1,446,316.41 USD | -174,716.54 USD | `-6.43%` | `5B / 15S` |
| `5:00 UTC` | `0.3312` | `0.3323` | `0.3312` | `0.3350` | `0.3309` | 3,615,541.77 USD | 1,824,507.31 USD | 1,791,034.46 USD | 33,472.85 USD | `+0.93%` | `10B / 13S` |
| `0:00 UTC` | `0.3320` | `0.3319` | `0.3320` | `0.3329` | `0.3307` | 3,613,244.76 USD | 2,074,143.60 USD | 1,539,101.16 USD | 535,042.44 USD | `+14.81%` | `13B / 9S` |
| `5:00 UTC` | `0.3320` | `0.3320` | `0.3320` | `0.3328` | `0.3316` | 3,073,188.16 USD | 1,480,743.83 USD | 1,592,444.33 USD | -111,700.49 USD | `-3.63%` | `27B / 21S` |

- **CoinGlass Algorithmic Footprint Signals Table (25_CoinGlass_Footprint_Signals.parquet)**:
| Time | Timeframe | Signal Type | Bias | Headline | Price Level | Absorbed Vol (USD) | Bar Delta (USD) |
|:---:|:---:|:---:|:---:|:---|:---:|:---:|:---:|
| `10-28 20:31` | `Volume 1.0M TRX` | `Divergence` | **`BEARISH`** | Rally without taker buying | `0.3317` | 0.00 USD | 0.00 USD |
| `10-28 14:33` | `Volume 1.0M TRX` | `Bear div` | **`BEARISH`** | Higher high, lower Cumulative Delta | `0.3320` | 2,500,000.00 USD | 0.00 USD |
| `10-28 14:25` | `Volume 1.0M TRX` | `Divergence` | **`BEARISH`** | Rally without taker buying | `0.3319` | 0.00 USD | 0.00 USD |
| `10-28 14:18` | `Volume 1.0M TRX` | `Divergence` | **`BEARISH`** | Rally without taker buying | `0.3318` | 0.00 USD | 0.00 USD |
| `10-28 14:13` | `Volume 1.0M TRX` | `Absorption` | **`BULLISH`** | Selling absorbed at the low | `0.3317` | 438,000.00 USD | 0.00 USD |
| `10-28 13:54` | `Volume 1.0M TRX` | `Divergence` | **`BULLISH`** | Drop without taker selling | `0.3317` | 0.00 USD | 0.00 USD |
| `10-28 13:54` | `Volume 1.0M TRX` | `Absorption` | **`BEARISH`** | Buying absorbed at the high | `0.3321` | 302,000.00 USD | 0.00 USD |
| `10-28 13:54` | `Volume 1.0M TRX` | `Trapped longs` | **`BEARISH`** | Failed breakout | `0.3321` | 302,000.00 USD | 0.00 USD |
| `10-28 13:48` | `Volume 1.0M TRX` | `Divergence` | **`BULLISH`** | Drop without taker selling | `0.3315` | 0.00 USD | 0.00 USD |
| `10-28 13:43` | `Volume 1.0M TRX` | `Absorption` | **`BEARISH`** | Buying absorbed at the high | `0.3318` | 192,000.00 USD | 0.00 USD |
| `10-28 13:31` | `Volume 1.0M TRX` | `Absorption` | **`BEARISH`** | Buying absorbed at the high | `0.3315` | 266,000.00 USD | 0.00 USD |
| `10-28 12:31` | `Volume 1.0M TRX` | `Divergence` | **`BEARISH`** | Rally without taker buying | `0.3315` | 0.00 USD | 0.00 USD |
| `10-28 12:31` | `Volume 1.0M TRX` | `Bear div` | **`BEARISH`** | Higher high, lower Cumulative Delta | `0.3315` | 493,000.00 USD | 0.00 USD |
| `10-28 09:25` | `Volume 1.0M TRX` | `Divergence` | **`BEARISH`** | Rally without taker buying | `0.3313` | 0.00 USD | 0.00 USD |
| `10-28 09:01` | `Volume 1.0M TRX` | `Absorption` | **`BULLISH`** | Selling absorbed at the low | `0.3309` | 205,000.00 USD | 0.00 USD |
| `10-28 05:53` | `Volume 1.0M TRX` | `Exhaustion` | **`BEARISH`** | Buyer exhaustion | `0.3322` | 0.00 USD | 0.00 USD |
| `10-28 05:51` | `Volume 1.0M TRX` | `Divergence` | **`BEARISH`** | Rally without taker buying | `0.3322` | 0.00 USD | 0.00 USD |
| `10-28 05:44` | `Volume 1.0M TRX` | `Absorption` | **`BULLISH`** | Selling absorbed at the low | `0.3318` | 198,000.00 USD | 0.00 USD |

- **12-Horizon Macro Capital Netflows Table (2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet)**:
| Horizon | Spot Netflow (USD) | Futures Netflow (USD) | Institutional Bias |
|:---:|:---:|:---:|:---:|
| `5m` | 145,030.00 USD | 229,000.00 USD | **`ACCUMULATION`** |
| `15m` | 282,640.00 USD | 461,420.00 USD | **`ACCUMULATION`** |
| `30m` | 1,280,000.00 USD | 1,150,000.00 USD | **`ACCUMULATION`** |
| `1h` | 1,750,000.00 USD | 414,850.00 USD | **`ACCUMULATION`** |
| `2h` | 2,210,000.00 USD | 3,310,000.00 USD | **`ACCUMULATION`** |
| `4h` | 8,360,000.00 USD | -7,170,000.00 USD | **`ACCUMULATION`** |
| `6h` | 13,330,000.00 USD | -8,410,000.00 USD | **`ACCUMULATION`** |
| `8h` | 20,140,000.00 USD | -339,320.00 USD | **`ACCUMULATION`** |
| `12h` | 23,020,000.00 USD | 4,520,000.00 USD | **`ACCUMULATION`** |
| `24h` | 20,860,000.00 USD | 4,470,000.00 USD | **`ACCUMULATION`** |
| `1w` | 14,190,000.00 USD | 3,080,000.00 USD | **`ACCUMULATION`** |
| `30d` | -8,190,000.00 USD | 3,870,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+145.03K` | 15m=`+282.64K` | 1h=`+1.75M` | 24h=`+20.86M`
* Futures Capital Netflows: 5m=`+229.00K` | 15m=`+461.42K` | 1h=`+414.85K` | 24h=`+4.47M`
- **Institutional Crypto ETF Capital Flows (1_Crypto_ETF_Flows.parquet)**:
  * `-`: ETF Net Flow = 0.00 USD (Inflows: 0.00 USD, Outflows: 0.00 USD)
  * `-`: ETF Net Flow = 0.00 USD (Inflows: 0.00 USD, Outflows: 0.00 USD)
  * `-`: ETF Net Flow = 0.00 USD (Inflows: 0.00 USD, Outflows: 0.00 USD)
  * `-`: ETF Net Flow = 0.00 USD (Inflows: 0.00 USD, Outflows: 0.00 USD)
  * `-`: ETF Net Flow = 0.00 USD (Inflows: 0.00 USD, Outflows: 0.00 USD)
  * `-`: ETF Net Flow = 0.00 USD (Inflows: 0.00 USD, Outflows: 0.00 USD)
  * `-`: ETF Net Flow = 0.00 USD (Inflows: 0.00 USD, Outflows: 0.00 USD)
  * `-`: ETF Net Flow = 0.00 USD (Inflows: 0.00 USD, Outflows: 0.00 USD)
  * `-`: ETF Net Flow = 0.00 USD (Inflows: 0.00 USD, Outflows: 0.00 USD)
  * `-`: ETF Net Flow = 0.00 USD (Inflows: 0.00 USD, Outflows: 0.00 USD)

- **High-Impact Macro Economic Events (19_Calendar.parquet)**:
  * `Sun Oct 25` [CHF - Low Impact]: Daylight Saving Time Shift (Forecast: , Previous: )
  * `Sun Oct 25` [EUR - Low Impact]: Daylight Saving Time Shift (Forecast: , Previous: )
  * `Sun Oct 25` [GBP - Low Impact]: Daylight Saving Time Shift (Forecast: , Previous: )
  * `Mon Oct 26` [NZD - Low Impact]: Bank Holiday (Forecast: , Previous: )
  * `Mon Oct 26` [AUD - Low Impact]: RBA Assist Gov Jones Speaks (Forecast: , Previous: )
  * `Mon Oct 26` [EUR - Low Impact]: German ifo Business Climate (Forecast: 90.0, Previous: 89.9)
  * `Mon Oct 26` [GBP - Low Impact]: CBI Realized Sales (Forecast: -47, Previous: -55)
  * `Tue Oct 27` [JPY - Low Impact]: SPPI y/y (Forecast: 3.7%, Previous: 3.5%)
  * `Tue Oct 27` [GBP - Low Impact]: BRC Shop Price Index y/y (Forecast: 1.6%, Previous: 1.4%)
  * `Tue Oct 27` [JPY - Low Impact]: BOJ Core CPI y/y (Forecast: 1.9%, Previous: 1.8%)
  * `Tue Oct 27` [EUR - Low Impact]: Spanish Unemployment Rate (Forecast: 9.9%, Previous: 9.9%)
  * `Tue Oct 27` [EUR - Low Impact]: M3 Money Supply y/y (Forecast: 3.5%, Previous: 3.5%)
  * `Tue Oct 27` [EUR - Low Impact]: Private Loans y/y (Forecast: 3.1%, Previous: 3.1%)
  * `Tue Oct 27` [USD - Low Impact]: ADP Weekly Employment Change (Forecast: , Previous: 17.5K)
  * `Tue Oct 27` [USD - Low Impact]: Core Durable Goods Orders m/m (Forecast: 0.6%, Previous: 0.2%)

- **Breaking Institutional News & Market Intelligence (19_News.parquet)**:
  * `2026-10-30 14:09:50 IST`: [channelnewsasia.com] - (Sentiment: `Neutral`)
  * `2026-10-30 13:51:50 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 13:50:50 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 13:31:50 IST`: [kof.ethz.ch] - (Sentiment: `Neutral`)
  * `2026-10-30 14:27:50 IST`: [gerlachmacro.substack.com] - (Sentiment: `Neutral`)
  * `2026-10-30 14:27:50 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-30 14:27:50 IST`: [insee.fr] - (Sentiment: `Neutral`)
  * `2026-10-30 14:27:50 IST`: [insee.fr] - (Sentiment: `Neutral`)
  * `2026-10-30 14:27:50 IST`: [@FirstSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 14:27:50 IST`: [nationwide.co.uk] - (Sentiment: `Neutral`)
  * `2026-10-30 14:27:50 IST`: [destatis.de] - (Sentiment: `Neutral`)
  * `2026-10-30 14:26:50 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-30 14:26:50 IST`: [@FirstSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 14:26:50 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-30 14:26:50 IST`: [insee.fr] - (Sentiment: `Neutral`)


---

## 9. TradFi & Interbank Market Mechanics
*(Applicable to Foreign Exchange Majors, Precious Metals, Global Equity Indices, and Commodities)*
- **Central Bank Monetary Policy & Rate Differential**:
  * Prevailing Policy Stance: `Federal Reserve (4.75% - 5.00%) Neutral-Gradualist Stance`
  * 2-Year Sovereign Yield Spread Direction & 10-Year Real Yield Momentum.
- **Interbank Foreign Exchange Mechanics**:
  * London/NY Overlap Window (13:00 - 16:00 UTC): Prime Institutional Liquidity.
  * Rollover Spread Expansion Gate: Execution strictly prohibited between 21:15 UTC and 22:30 UTC.
- **Global Commodity & Index Pricing Drivers**:
  * Precious Metals (XAU/XAG): Real Yield Sensitivity & Geopolitical Safe-Haven Premium.
  * Equity Indices (US30, SP500, NAS100): E-mini Auction VWAP Dispersion & Institutional Gamma Profiles.

---

## 10. Quantitative Trade Formulation & Autonomous Broker Execution Card
*(Sources: Canonical Quant Rules, STANDARDIZED_TRADING_DECISION_CHAIN.md, 10 lethal traps)*
- **Candidate Long Setup (Model 1 / Model 2 VAL Sweep Fade)**:
  * Order Type: `BUY_LIMIT`
  * Execution Entry: `0.3429` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `0.3358` (Risk Distance: `0.0071` pts)
  * +2.5R Take Profit: `0.3605`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `0.3578` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `0.3649` (Risk Distance: `0.0071` pts)
  * +2.5R Take Profit: `0.3402`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`0.3352`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
