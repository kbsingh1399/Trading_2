# 🏛️ SOVEREIGN CANDIDATE DOSSIER: TRX
**Canonical Key**: `TRX` | **Broker Instrument**: `TRXUSD.p` | **Asset Class**: `Crypto Alt L1`
**Timestamp**: `2026-10-30 14:26:38 IST` (`2026-10-30 08:56:38 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `0.3312` | **Live Ask Quote**: `0.3333` | **Mid Price**: `0.3322`
- **Spread Points**: `21.00` | **Spread BPS**: `63.21 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `0.3471` | VWAP Z-Score: `-1.91` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `0.0033` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `34.67` (State: `OVERSOLD`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `0.3727` | Lower -3.00σ Band: `0.3215`
  * Upper +2.51σ Band: `0.3685` | Lower -2.51σ Band: `0.3257`
  * Upper +2.01σ Band: `0.3643` | Lower -2.01σ Band: `0.3299`
  * Upper +2.00σ Band: `0.3642` | Lower -2.00σ Band: `0.3300`
  * Upper +1.28σ Band: `0.3580` | Lower -1.28σ Band: `0.3362`
  * Upper +1.00σ Band: `0.3556` | Lower -1.00σ Band: `0.3385`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`0.3333` | EMA-20=`0.3372` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`0.3401` (Slope: `+0.0000`) | EMA-100=`0.3384`
  * Institutional Anchors: EMA-144=`0.3368` | EMA-200=`0.3354` (Slope: `-0.0483`) | EMA-233=`0.3347`
- **Range Boundaries**: 24H High=`0.3632` | 24H Low=`0.3275` | Weekly High=`0.3632` | Weekly Low=`0.3266`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `0.3578` (Distance: `-7.13%`)
  * Point of Control (POC) = `0.3513` (Distance: `-5.43%`)
  * Value Area Low (VAL) = `0.3431` (Distance: `-3.16%`)
  * Auction Positioning: `BELOW_VALUE (Imbalance)` | Session Bias: **`BULLISH (Above Pivot)`** | Market Regime: `RANGE_EXPANSION`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`0.3312` | POC=`0.3307` | VAL=`0.3293`
  * Prior Day Extremes: PDH=`0.3335` | PDL=`0.3275` | PDC=`0.3275`
  * Monday Range Blueprint: High=`0.3310` | Mid=`0.3300` | Low=`0.3289`
  * Developing Weekly Value Area: Weekly VAH=`0.3470` | Weekly POC=`0.3306` | Weekly VAL=`0.3267`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`0.3632` | Low=`0.3335`
  * London Session (08:00-16:00 UTC): High=`0.3444` | Low=`0.3299`
  * New York Session (13:00-21:00 UTC): High=`0.3342` | Low=`0.3303`
  * Initial Balance (First Hour): IB High=`0.3444` | IB Low=`0.3379`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `0.3309` - `0.3336`
  * Optimal Trade Entry (OTE 0.705): `0.3329`
  * Structural Invalidation Anchor (0.786): `0.3349`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `0.3310` | `0.3329` | `0.3307` | `0.3323` | `4,709,238` | 1,562,705.60 USD | 246,521.79 USD | `+15.78%` | -2,732,267.55 USD | `+0.47` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `5m` | `0.3322` | `0.3327` | `0.3316` | `0.3322` | `3,967,865` | 1,317,669.81 USD | 202,644.60 USD | `+15.38%` | -2,529,622.95 USD | `+0.29` | **`BULLISH`** | `DELTA ALIGNED` |
| `5m` | `0.3322` | `0.3323` | `0.3318` | `0.3320` | `264,708` | 87,908.69 USD | -5,119.62 USD | `-5.82%` | -2,534,742.57 USD | `-0.39` | **`BEARISH`** | `DELTA ALIGNED` |
| `15m` | `0.3371` | `0.3377` | `0.3336` | `0.3337` | `8,089,678` | 2,717,916.28 USD | -174,716.54 USD | `-6.43%` | -3,012,262.19 USD | `+0.25` | **`BEARISH`** | `DELTA ALIGNED` |
| `15m` | `0.3336` | `0.3350` | `0.3308` | `0.3310` | `10,878,463` | 3,615,541.77 USD | 33,472.85 USD | `+0.93%` | -2,978,789.34 USD | `+0.47` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `15m` | `0.3310` | `0.3329` | `0.3307` | `0.3321` | `8,936,144` | 2,966,402.04 USD | 445,301.15 USD | `+15.01%` | -2,533,488.19 USD | `+0.90` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `1h` | `0.3381` | `0.3426` | `0.3338` | `0.3379` | `87,240,035` | 29,393,992.16 USD | -4,638,752.48 USD | `-15.78%` | -4,783,336.65 USD | `-2.30` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `1h` | `0.3379` | `0.3380` | `0.3310` | `0.3371` | `71,304,583` | 23,823,772.16 USD | 1,991,288.68 USD | `+8.36%` | -2,792,047.97 USD | `+1.07` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `1h` | `0.3371` | `0.3377` | `0.3307` | `0.3321` | `27,904,285` | 9,299,860.09 USD | 304,057.46 USD | `+3.27%` | -2,487,990.51 USD | `+0.21` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `0.3533` | `0.3608` | `0.3475` | `0.3495` | `257,452,106` | 91,407,782.04 USD | 2,108,185.60 USD | `+2.31%` | 4,840,432.56 USD | `+0.97` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `0.3495` | `0.3497` | `0.3310` | `0.3371` | `257,957,739` | 87,367,227.03 USD | -7,246,486.44 USD | `-8.29%` | -2,406,053.88 USD | `-1.94` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.3371` | `0.3377` | `0.3307` | `0.3320` | `27,909,952` | 9,301,742.14 USD | 302,803.08 USD | `+3.26%` | -2,103,250.80 USD | `+0.20` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `0.3314` | `0.3316` | `0.3310` | `0.3315` | `11,250,742` | 3,727,253.77 USD | 212,090.87 USD | `+5.69%` | 581,399.04 USD | `-1.00` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `0.3315` | `0.3653` | `0.3282` | `0.3533` | `793,774,795` | 276,969,161.06 USD | 2,150,847.92 USD | `+0.78%` | 2,732,246.96 USD | `+1.41` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `0.3533` | `0.3608` | `0.3475` | `0.3495` | `257,452,106` | 91,407,782.04 USD | 2,108,185.60 USD | `+2.31%` | 4,840,432.56 USD | `+0.97` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `0.3495` | `0.3497` | `0.3310` | `0.3371` | `257,957,739` | 87,367,227.03 USD | -7,246,486.44 USD | `-8.29%` | -2,406,053.88 USD | `-1.94` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.3371` | `0.3377` | `0.3307` | `0.3320` | `27,909,952` | 9,301,742.14 USD | 302,803.08 USD | `+3.26%` | -2,103,250.80 USD | `+0.20` | **`BULLISH`** | `BULLISH ABSORPTION` |

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
| --- | **`0.3322`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `MID` | Regular L2 Book | - | - | - | Interbank L2 | 0.00% | Interbank |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 14:22:11 IST` |

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
| `1D` | `Long Liquidation` | `0.2972` | 11,460,000.00 USD | 11,460,000.00 USD | 28.80 USD | 0.00 USD | 2,320.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.2975` | 1,010.00 USD | 830,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.2976` | 11,460,000.00 USD | 11,460,000.00 USD | 208.32 USD | 2,950.00 USD | 2,060.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.2977` | 18,610,000.00 USD | 18,610,000.00 USD | 53,890.00 USD | 18,540.00 USD | 17,670.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.2980` | 11,450,000.00 USD | 11,450,000.00 USD | 17,570.00 USD | 5,070.00 USD | 9,160.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.2983` | 18,520,000.00 USD | 18,520,000.00 USD | 172,020.00 USD | 15,470.00 USD | 39,660.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.2984` | 11,420,000.00 USD | 11,420,000.00 USD | 117,500.00 USD | 13,460.00 USD | 21,230.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.2985` | 759.68 USD | 829,250.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.2988` | 11,270,000.00 USD | 11,270,000.00 USD | 27,450.00 USD | 2,360.00 USD | 8,790.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.2989` | 18,290,000.00 USD | 18,290,000.00 USD | 111,920.00 USD | 18,720.00 USD | 23,920.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.2992` | 11,230,000.00 USD | 11,230,000.00 USD | 9,680.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.2995` | 18,140,000.00 USD | 18,140,000.00 USD | 8,380.00 USD | 2,190.00 USD | 48,990.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.2995` | 197.37 USD | 828,490.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.2996` | 11,220,000.00 USD | 11,220,000.00 USD | 1,230.00 USD | 1,250.00 USD | 15,560.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3000` | 11,200,000.00 USD | 11,200,000.00 USD | 8,760.00 USD | 11,490.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3001` | 18,080,000.00 USD | 18,080,000.00 USD | 1,880.00 USD | 15,390.00 USD | 30,210.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3004` | 11,180,000.00 USD | 11,180,000.00 USD | 4,620.00 USD | 10,980.00 USD | 32,950.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3005` | 10,490.00 USD | 828,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.3007` | 18,030,000.00 USD | 18,030,000.00 USD | 13,780.00 USD | 2,960.00 USD | 22,100.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3008` | 11,130,000.00 USD | 11,130,000.00 USD | 23,780.00 USD | 3,410.00 USD | 16,090.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3012` | 11,090,000.00 USD | 11,090,000.00 USD | 0.00 USD | 3,170.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3013` | 17,990,000.00 USD | 17,990,000.00 USD | 2,700.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3015` | 128.44 USD | 817,810.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3016` | 11,090,000.00 USD | 11,090,000.00 USD | 1,010.00 USD | 6,470.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3019` | 17,990,000.00 USD | 17,990,000.00 USD | 0.00 USD | 8,660.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3020` | 11,080,000.00 USD | 11,080,000.00 USD | 14,850.00 USD | 2,010.00 USD | 16,590.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3024` | 11,050,000.00 USD | 11,050,000.00 USD | 2,600.00 USD | 6,590.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3025` | 17,980,000.00 USD | 17,980,000.00 USD | 0.00 USD | 9,860.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3025` | 2,620.00 USD | 817,680.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3028` | 11,040,000.00 USD | 11,040,000.00 USD | 23,320.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3031` | 17,970,000.00 USD | 17,970,000.00 USD | 50,940.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3032` | 11,010,000.00 USD | 11,010,000.00 USD | 1,580.00 USD | 2,750.00 USD | 18,790.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3035` | 266.47 USD | 815,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3036` | 10,990,000.00 USD | 10,990,000.00 USD | 1,260.00 USD | 3,230.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3040` | 10,990,000.00 USD | 10,990,000.00 USD | 537.63 USD | 9,300.00 USD | 44,700.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3044` | 10,930,000.00 USD | 10,930,000.00 USD | 0.00 USD | 10,830.00 USD | 11,650.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3045` | 138.24 USD | 814,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3048` | 10,910,000.00 USD | 10,910,000.00 USD | 31,710.00 USD | 13,780.00 USD | 49,740.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3049` | 17,920,000.00 USD | 17,920,000.00 USD | 18,870.00 USD | 0.00 USD | 66,870.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3052` | 10,810,000.00 USD | 10,810,000.00 USD | 46,990.00 USD | 15,890.00 USD | 11,570.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3055` | 17,840,000.00 USD | 17,840,000.00 USD | 1,250.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3055` | 14,670.00 USD | 814,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3056` | 10,740,000.00 USD | 10,740,000.00 USD | 0.00 USD | 0.00 USD | 37,740.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3060` | 10,700,000.00 USD | 10,700,000.00 USD | 885.25 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3061` | 17,830,000.00 USD | 17,830,000.00 USD | 32,690.00 USD | 7,690.00 USD | 37,210.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3064` | 10,700,000.00 USD | 10,700,000.00 USD | 29,570.00 USD | 16,530.00 USD | 56,460.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3067` | 17,760,000.00 USD | 17,760,000.00 USD | 5,220.00 USD | 8,110.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3068` | 10,600,000.00 USD | 10,600,000.00 USD | 1,540.00 USD | 15,440.00 USD | 48,460.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3072` | 10,530,000.00 USD | 10,530,000.00 USD | 95.13 USD | 1,940.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3073` | 17,740,000.00 USD | 17,740,000.00 USD | 9,190.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3075` | 6,650.00 USD | 799,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3076` | 10,530,000.00 USD | 10,530,000.00 USD | 23,540.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3079` | 17,730,000.00 USD | 17,730,000.00 USD | 37,430.00 USD | 10,270.00 USD | 50,200.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3080` | 10,510,000.00 USD | 10,510,000.00 USD | 15.29 USD | 0.00 USD | 12,250.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3084` | 10,500,000.00 USD | 10,500,000.00 USD | 18,680.00 USD | 0.00 USD | 15,810.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3085` | 17,640,000.00 USD | 17,640,000.00 USD | 2,870.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3085` | 291.53 USD | 793,340.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3088` | 10,460,000.00 USD | 10,460,000.00 USD | 594.68 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3091` | 17,630,000.00 USD | 17,630,000.00 USD | 12,490.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3092` | 10,460,000.00 USD | 10,460,000.00 USD | 14,750.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3095` | 192.51 USD | 793,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3096` | 10,450,000.00 USD | 10,450,000.00 USD | 610.25 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3097` | 17,620,000.00 USD | 17,620,000.00 USD | 83,130.00 USD | 3,620.00 USD | 54,360.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3100` | 10,440,000.00 USD | 10,440,000.00 USD | 4,440.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3103` | 17,480,000.00 USD | 17,480,000.00 USD | 67,180.00 USD | 0.00 USD | 63,310.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3104` | 10,440,000.00 USD | 10,440,000.00 USD | 56,750.00 USD | 15,820.00 USD | 46,470.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3105` | 820.96 USD | 792,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3108` | 10,320,000.00 USD | 10,320,000.00 USD | 1,350.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3109` | 17,350,000.00 USD | 17,350,000.00 USD | 6,350.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3112` | 10,320,000.00 USD | 10,320,000.00 USD | 0.00 USD | 4,980.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3115` | 17,340,000.00 USD | 17,340,000.00 USD | 5,350.00 USD | 0.00 USD | 37,490.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3115` | 13,600.00 USD | 792,030.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3116` | 10,310,000.00 USD | 10,310,000.00 USD | 2,250.00 USD | 12,220.00 USD | 17,620.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3120` | 10,280,000.00 USD | 10,280,000.00 USD | 23,970.00 USD | 2,560.00 USD | 33,830.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3121` | 17,300,000.00 USD | 17,300,000.00 USD | 166,810.00 USD | 19,620.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3124` | 10,220,000.00 USD | 10,220,000.00 USD | 12,740.00 USD | 3,560.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3125` | 17,570.00 USD | 778,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.3127` | 17,110,000.00 USD | 17,110,000.00 USD | 16,750.00 USD | 54,460.00 USD | 57,690.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3128` | 10,210,000.00 USD | 10,210,000.00 USD | 3,480.00 USD | 35,920.00 USD | 29,100.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3132` | 10,140,000.00 USD | 10,140,000.00 USD | 2,980.00 USD | 26,460.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3133` | 16,980,000.00 USD | 16,980,000.00 USD | 3,990.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3135` | 681.55 USD | 760,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3136` | 10,110,000.00 USD | 10,110,000.00 USD | 5,020.00 USD | 10,610.00 USD | 9,590.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3139` | 16,980,000.00 USD | 16,980,000.00 USD | 2,940.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3140` | 10,080,000.00 USD | 10,080,000.00 USD | 6,950.00 USD | 0.00 USD | 9,540.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3144` | 10,070,000.00 USD | 10,070,000.00 USD | 2,430.00 USD | 5,900.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3145` | 16,980,000.00 USD | 16,980,000.00 USD | 247,620.00 USD | 51,270.00 USD | 17,870.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3145` | 116.05 USD | 760,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3148` | 10,060,000.00 USD | 10,060,000.00 USD | 1,420.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3151` | 16,660,000.00 USD | 16,660,000.00 USD | 206,090.00 USD | 23,130.00 USD | 49,320.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3152` | 10,060,000.00 USD | 10,060,000.00 USD | 1,210.00 USD | 23,750.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3155` | 1,370.00 USD | 760,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3156` | 10,030,000.00 USD | 10,030,000.00 USD | 28,750.00 USD | 3,680.00 USD | 10,790.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3157` | 16,380,000.00 USD | 16,380,000.00 USD | 393,090.00 USD | 93,740.00 USD | 60,300.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3160` | 9,990,000.00 USD | 9,990,000.00 USD | 5,430.00 USD | 0.00 USD | 5,450.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3163` | 15,830,000.00 USD | 15,830,000.00 USD | 483,870.00 USD | 182,370.00 USD | 192,840.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3164` | 9,980,000.00 USD | 9,980,000.00 USD | 45,260.00 USD | 33,960.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3165` | 2,360.00 USD | 758,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3168` | 9,900,000.00 USD | 9,900,000.00 USD | 0.00 USD | 10,820.00 USD | 29,770.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3169` | 14,980,000.00 USD | 14,980,000.00 USD | 403,830.00 USD | 106,680.00 USD | 142,240.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3172` | 9,860,000.00 USD | 9,860,000.00 USD | 18,490.00 USD | 33,870.00 USD | 27,630.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3175` | 14,320,000.00 USD | 14,320,000.00 USD | 146,800.00 USD | 53,470.00 USD | 69,280.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3175` | 4,060.00 USD | 756,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3176` | 9,780,000.00 USD | 9,780,000.00 USD | 41,110.00 USD | 6,450.00 USD | 25,690.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3180` | 9,700,000.00 USD | 9,700,000.00 USD | 109,700.00 USD | 42,080.00 USD | 67,350.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3181` | 14,050,000.00 USD | 14,050,000.00 USD | 743,630.00 USD | 76,910.00 USD | 182,330.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3184` | 9,490,000.00 USD | 9,490,000.00 USD | 308,240.00 USD | 33,540.00 USD | 56,970.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3185` | 642.10 USD | 752,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.3187` | 13,050,000.00 USD | 13,050,000.00 USD | 411,400.00 USD | 97,820.00 USD | 24,770.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3188` | 9,090,000.00 USD | 9,090,000.00 USD | 79,880.00 USD | 35,830.00 USD | 56,940.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3192` | 8,910,000.00 USD | 8,910,000.00 USD | 88,600.00 USD | 3,120.00 USD | 59,760.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3193` | 12,520,000.00 USD | 12,520,000.00 USD | 118,210.00 USD | 25,780.00 USD | 168,960.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3196` | 8,760,000.00 USD | 8,760,000.00 USD | 61,510.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3199` | 12,200,000.00 USD | 12,200,000.00 USD | 0.00 USD | 38,380.00 USD | 63,420.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3200` | 8,700,000.00 USD | 8,700,000.00 USD | 145,190.00 USD | 33,980.00 USD | 14,150.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3204` | 8,510,000.00 USD | 8,510,000.00 USD | 174,840.00 USD | 45,390.00 USD | 126,790.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3205` | 12,100,000.00 USD | 12,100,000.00 USD | 94,770.00 USD | 59,200.00 USD | 130,760.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3205` | 455.75 USD | 751,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3208` | 8,160,000.00 USD | 8,160,000.00 USD | 128,590.00 USD | 13,140.00 USD | 63,020.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3211` | 11,820,000.00 USD | 11,820,000.00 USD | 562,620.00 USD | 117,230.00 USD | 244,340.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3212` | 7,960,000.00 USD | 7,960,000.00 USD | 1,300.00 USD | 25,860.00 USD | 99,450.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3216` | 7,830,000.00 USD | 7,830,000.00 USD | 5,550.00 USD | 30,210.00 USD | 78,920.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3217` | 10,890,000.00 USD | 10,890,000.00 USD | 284,850.00 USD | 58,690.00 USD | 107,900.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3220` | 7,710,000.00 USD | 7,710,000.00 USD | 35,920.00 USD | 37,230.00 USD | 72,520.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3223` | 10,440,000.00 USD | 10,440,000.00 USD | 643,460.00 USD | 196,690.00 USD | 103,370.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3224` | 7,570,000.00 USD | 7,570,000.00 USD | 132,310.00 USD | 19,600.00 USD | 182,490.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3228` | 7,230,000.00 USD | 7,230,000.00 USD | 91,010.00 USD | 46,020.00 USD | 106,810.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3229` | 9,500,000.00 USD | 9,500,000.00 USD | 859,960.00 USD | 299,190.00 USD | 385,680.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3232` | 6,990,000.00 USD | 6,990,000.00 USD | 56,470.00 USD | 13,130.00 USD | 49,900.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3235` | 7,950,000.00 USD | 7,950,000.00 USD | 709,160.00 USD | 213,370.00 USD | 371,680.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3235` | 128.43 USD | 751,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3236` | 6,870,000.00 USD | 6,870,000.00 USD | 6,420.00 USD | 66,660.00 USD | 158,610.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3240` | 6,640,000.00 USD | 6,640,000.00 USD | 567.10 USD | 35,800.00 USD | 50,800.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3241` | 6,660,000.00 USD | 6,660,000.00 USD | 432,660.00 USD | 149,860.00 USD | 138,560.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3244` | 6,550,000.00 USD | 6,550,000.00 USD | 149,810.00 USD | 42,240.00 USD | 261,780.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3247` | 5,940,000.00 USD | 5,940,000.00 USD | 849,100.00 USD | 127,310.00 USD | 353,590.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3248` | 6,100,000.00 USD | 6,100,000.00 USD | 708,820.00 USD | 100,990.00 USD | 212,330.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3252` | 5,080,000.00 USD | 5,080,000.00 USD | 420,090.00 USD | 99,340.00 USD | 253,530.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3253` | 4,610,000.00 USD | 4,610,000.00 USD | 1,220,000.00 USD | 137,440.00 USD | 241,690.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3256` | 4,300,000.00 USD | 4,300,000.00 USD | 312,250.00 USD | 60,830.00 USD | 365,380.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3259` | 3,010,000.00 USD | 3,010,000.00 USD | 182,240.00 USD | 92,250.00 USD | 346,980.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3260` | 3,570,000.00 USD | 3,570,000.00 USD | 79,940.00 USD | 9,800.00 USD | 77,800.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3264` | 3,400,000.00 USD | 3,400,000.00 USD | 43,780.00 USD | 30,260.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3265` | 2,390,000.00 USD | 2,390,000.00 USD | 79,990.00 USD | 19,240.00 USD | 93,040.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3268` | 3,320,000.00 USD | 3,320,000.00 USD | 124,870.00 USD | 159,980.00 USD | 380,710.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3271` | 2,190,000.00 USD | 2,190,000.00 USD | 189,530.00 USD | 138,680.00 USD | 261,530.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3272` | 2,660,000.00 USD | 2,660,000.00 USD | 38,550.00 USD | 50,640.00 USD | 201,620.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3275` | 163.42 USD | 751,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3276` | 2,370,000.00 USD | 2,370,000.00 USD | 202,430.00 USD | 41,150.00 USD | 228,020.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3277` | 1,600,000.00 USD | 1,600,000.00 USD | 0.00 USD | 29,390.00 USD | 85,620.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3280` | 1,900,000.00 USD | 1,900,000.00 USD | 57,970.00 USD | 59,480.00 USD | 34,900.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3283` | 1,490,000.00 USD | 1,490,000.00 USD | 89,030.00 USD | 25,670.00 USD | 275,050.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3284` | 1,740,000.00 USD | 1,740,000.00 USD | 0.00 USD | 36,370.00 USD | 30,620.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3285` | 745,260.00 USD | 750,880.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3288` | 1,680,000.00 USD | 1,680,000.00 USD | 155,850.00 USD | 16,100.00 USD | 155,080.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3289` | 1,100,000.00 USD | 1,100,000.00 USD | 2,520.00 USD | 43,290.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3292` | 1,350,000.00 USD | 1,350,000.00 USD | 0.00 USD | 39,200.00 USD | 80,060.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3295` | 1,050,000.00 USD | 1,050,000.00 USD | 254,700.00 USD | 83,080.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3295` | 839.90 USD | 5,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3296` | 1,230,000.00 USD | 1,230,000.00 USD | 167,290.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3300` | 1,060,000.00 USD | 1,060,000.00 USD | 36,460.00 USD | 13,760.00 USD | 30,950.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3301` | 716,630.00 USD | 716,630.00 USD | 184,120.00 USD | 9,050.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3304` | 981,540.00 USD | 981,540.00 USD | 1,210.00 USD | 0.00 USD | 74,690.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3307` | 523,460.00 USD | 523,460.00 USD | 167,950.00 USD | 10,690.00 USD | 294,170.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3308` | 905,630.00 USD | 905,630.00 USD | 121,770.00 USD | 64,330.00 USD | 221,420.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3312` | 498,110.00 USD | 498,110.00 USD | 644.45 USD | 74,280.00 USD | 310,080.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3313` | 50,650.00 USD | 50,650.00 USD | 0.00 USD | 50,650.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3315` | 4,780.00 USD | 4,780.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3316` | 113,100.00 USD | 113,100.00 USD | 0.00 USD | 113,100.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3319` | 57,890.00 USD | 57,890.00 USD | 0.00 USD | 57,890.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3324` | 87,140.00 USD | 87,140.00 USD | 0.00 USD | 87,140.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3356` | 152,390.00 USD | 152,390.00 USD | 0.00 USD | 0.00 USD | 65,250.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3360` | 231,430.00 USD | 231,430.00 USD | 0.00 USD | 0.00 USD | 79,030.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3368` | 304,340.00 USD | 304,340.00 USD | 72,920.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3376` | 633,980.00 USD | 633,980.00 USD | 329,640.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3379` | 79,280.00 USD | 79,280.00 USD | 0.00 USD | 21,390.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3380` | 678,820.00 USD | 678,820.00 USD | 44,840.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3384` | 733,920.00 USD | 733,920.00 USD | 27,070.00 USD | 0.00 USD | 28,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3385` | 204,930.00 USD | 204,930.00 USD | 125,650.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3388` | 912,310.00 USD | 912,310.00 USD | 139,840.00 USD | 11,160.00 USD | 27,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3391` | 439,600.00 USD | 439,600.00 USD | 0.00 USD | 0.00 USD | 234,660.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3392` | 1,020,000.00 USD | 1,020,000.00 USD | 25,850.00 USD | 0.00 USD | 77,800.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3396` | 1,070,000.00 USD | 1,070,000.00 USD | 54,090.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3397` | 948,010.00 USD | 948,010.00 USD | 257,550.00 USD | 250,860.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3400` | 1,240,000.00 USD | 1,240,000.00 USD | 43,780.00 USD | 67,960.00 USD | 57,610.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3403` | 2,340,000.00 USD | 2,340,000.00 USD | 1,070,000.00 USD | 103,630.00 USD | 223,390.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3404` | 1,730,000.00 USD | 1,730,000.00 USD | 134,550.00 USD | 29,780.00 USD | 329,990.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3408` | 1,870,000.00 USD | 1,870,000.00 USD | 71,510.00 USD | 0.00 USD | 62,320.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3409` | 2,820,000.00 USD | 2,820,000.00 USD | 0.00 USD | 29,390.00 USD | 446,990.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3412` | 2,180,000.00 USD | 2,180,000.00 USD | 208,300.00 USD | 20,560.00 USD | 80,830.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3415` | 2,900,000.00 USD | 2,900,000.00 USD | 0.00 USD | 0.00 USD | 85,620.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3416` | 2,850,000.00 USD | 2,850,000.00 USD | 605,570.00 USD | 25,060.00 USD | 44,630.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3420` | 2,890,000.00 USD | 2,890,000.00 USD | 0.00 USD | 39,260.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3421` | 2,950,000.00 USD | 2,950,000.00 USD | 0.00 USD | 43,290.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3424` | 3,020,000.00 USD | 3,020,000.00 USD | 71,180.00 USD | 58,610.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3427` | 3,040,000.00 USD | 3,040,000.00 USD | 0.00 USD | 92,380.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3428` | 3,250,000.00 USD | 3,250,000.00 USD | 60,980.00 USD | 171,280.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3432` | 3,500,000.00 USD | 3,500,000.00 USD | 105,330.00 USD | 137,290.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3433` | 3,290,000.00 USD | 3,290,000.00 USD | 254,700.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3436` | 3,670,000.00 USD | 3,670,000.00 USD | 0.00 USD | 82,150.00 USD | 93,930.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3440` | 3,690,000.00 USD | 3,690,000.00 USD | 0.00 USD | 16,160.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3444` | 3,760,000.00 USD | 3,760,000.00 USD | 0.00 USD | 48,600.00 USD | 18,140.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3445` | 3,400,000.00 USD | 3,400,000.00 USD | 103,130.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3448` | 4,030,000.00 USD | 4,030,000.00 USD | 35,950.00 USD | 62,260.00 USD | 174,680.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3451` | 3,490,000.00 USD | 3,490,000.00 USD | 62,830.00 USD | 28,550.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3452` | 4,230,000.00 USD | 4,230,000.00 USD | 56,600.00 USD | 77,650.00 USD | 70,680.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3456` | 4,490,000.00 USD | 4,490,000.00 USD | 71,070.00 USD | 7,470.00 USD | 180,610.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3457` | 3,850,000.00 USD | 3,850,000.00 USD | 0.00 USD | 29,340.00 USD | 332,190.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3460` | 5,000,000.00 USD | 5,000,000.00 USD | 181,240.00 USD | 26,850.00 USD | 299,880.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3464` | 5,030,000.00 USD | 5,030,000.00 USD | 21,890.00 USD | 7,110.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3468` | 5,130,000.00 USD | 5,130,000.00 USD | 0.00 USD | 48,870.00 USD | 50,420.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3469` | 4,040,000.00 USD | 4,040,000.00 USD | 60,310.00 USD | 51,820.00 USD | 75,520.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3472` | 5,220,000.00 USD | 5,220,000.00 USD | 0.00 USD | 31,080.00 USD | 56,190.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3475` | 4,080,000.00 USD | 4,080,000.00 USD | 0.00 USD | 40,540.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3476` | 5,290,000.00 USD | 5,290,000.00 USD | 23,470.00 USD | 51,860.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3480` | 5,420,000.00 USD | 5,420,000.00 USD | 0.00 USD | 11,950.00 USD | 120,420.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3481` | 4,160,000.00 USD | 4,160,000.00 USD | 19,060.00 USD | 14,700.00 USD | 42,810.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3484` | 5,450,000.00 USD | 5,450,000.00 USD | 0.00 USD | 22,220.00 USD | 8,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3487` | 4,180,000.00 USD | 4,180,000.00 USD | 6,050.00 USD | 21,650.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3488` | 5,520,000.00 USD | 5,520,000.00 USD | 39,690.00 USD | 27,650.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3492` | 5,610,000.00 USD | 5,610,000.00 USD | 5,430.00 USD | 19,600.00 USD | 61,240.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3493` | 4,210,000.00 USD | 4,210,000.00 USD | 5,810.00 USD | 24,660.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3496` | 5,720,000.00 USD | 5,720,000.00 USD | 32,290.00 USD | 0.00 USD | 79,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3499` | 4,340,000.00 USD | 4,340,000.00 USD | 127,350.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3500` | 6,180,000.00 USD | 6,180,000.00 USD | 52,670.00 USD | 0.00 USD | 410,930.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3504` | 6,240,000.00 USD | 6,240,000.00 USD | 0.00 USD | 6,880.00 USD | 46,960.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3505` | 4,350,000.00 USD | 4,350,000.00 USD | 5,650.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3508` | 6,320,000.00 USD | 6,320,000.00 USD | 75,920.00 USD | 8,080.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3511` | 5,320,000.00 USD | 5,320,000.00 USD | 704,750.00 USD | 0.00 USD | 271,800.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3512` | 6,400,000.00 USD | 6,400,000.00 USD | 0.00 USD | 4,320.00 USD | 76,540.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3516` | 6,470,000.00 USD | 6,470,000.00 USD | 21,910.00 USD | 5,720.00 USD | 43,290.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3517` | 5,330,000.00 USD | 5,330,000.00 USD | 7,560.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3520` | 6,550,000.00 USD | 6,550,000.00 USD | 30,910.00 USD | 18,240.00 USD | 28,330.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3523` | 5,750,000.00 USD | 5,750,000.00 USD | 279,190.00 USD | 28,950.00 USD | 107,430.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3524` | 6,560,000.00 USD | 6,560,000.00 USD | 4,750.00 USD | 3,730.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3528` | 6,730,000.00 USD | 6,730,000.00 USD | 103,690.00 USD | 38,340.00 USD | 28,910.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3529` | 5,750,000.00 USD | 5,750,000.00 USD | 2,170.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3532` | 6,950,000.00 USD | 6,950,000.00 USD | 67,090.00 USD | 64,680.00 USD | 88,110.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3535` | 6,030,000.00 USD | 6,030,000.00 USD | 11,650.00 USD | 77,960.00 USD | 187,450.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3536` | 7,220,000.00 USD | 7,220,000.00 USD | 61,430.00 USD | 12,790.00 USD | 195,270.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3540` | 7,330,000.00 USD | 7,330,000.00 USD | 54,890.00 USD | 58,780.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3541` | 6,950,000.00 USD | 6,950,000.00 USD | 808,160.00 USD | 118,370.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3544` | 7,480,000.00 USD | 7,480,000.00 USD | 25,450.00 USD | 82,120.00 USD | 37,920.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3547` | 7,240,000.00 USD | 7,240,000.00 USD | 0.00 USD | 0.00 USD | 288,450.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3548` | 7,560,000.00 USD | 7,560,000.00 USD | 5,450.00 USD | 41,620.00 USD | 31,910.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3552` | 7,640,000.00 USD | 7,640,000.00 USD | 2,640.00 USD | 36,790.00 USD | 47,950.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3553` | 7,360,000.00 USD | 7,360,000.00 USD | 4,360.00 USD | 117,050.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3556` | 7,700,000.00 USD | 7,700,000.00 USD | 20,180.00 USD | 38,770.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3559` | 7,370,000.00 USD | 7,370,000.00 USD | 4,230.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3560` | 7,790,000.00 USD | 7,790,000.00 USD | 331.60 USD | 7,120.00 USD | 78,340.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3564` | 7,890,000.00 USD | 7,890,000.00 USD | 2,250.00 USD | 29,510.00 USD | 67,310.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3565` | 7,410,000.00 USD | 7,410,000.00 USD | 0.00 USD | 43,060.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3568` | 7,890,000.00 USD | 7,890,000.00 USD | 1,450.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3571` | 7,420,000.00 USD | 7,420,000.00 USD | 8,530.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3572` | 7,900,000.00 USD | 7,900,000.00 USD | 1,770.00 USD | 6,920.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3576` | 8,080,000.00 USD | 8,080,000.00 USD | 161,360.00 USD | 18,380.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3577` | 7,540,000.00 USD | 7,540,000.00 USD | 124,630.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3580` | 8,120,000.00 USD | 8,120,000.00 USD | 2,390.00 USD | 0.00 USD | 38,950.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3583` | 7,680,000.00 USD | 7,680,000.00 USD | 0.00 USD | 0.00 USD | 135,900.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3584` | 8,150,000.00 USD | 8,150,000.00 USD | 17,760.00 USD | 14,930.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3588` | 8,170,000.00 USD | 8,170,000.00 USD | 4,700.00 USD | 15,750.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3589` | 8,050,000.00 USD | 8,050,000.00 USD | 1,610.00 USD | 50,650.00 USD | 320,430.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3592` | 8,260,000.00 USD | 8,260,000.00 USD | 50,450.00 USD | 0.00 USD | 33,590.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3595` | 8,200,000.00 USD | 8,200,000.00 USD | 0.00 USD | 0.00 USD | 146,290.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3596` | 8,480,000.00 USD | 8,480,000.00 USD | 108,840.00 USD | 12,460.00 USD | 99,590.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3600` | 8,680,000.00 USD | 8,680,000.00 USD | 1,160.00 USD | 36,520.00 USD | 163,110.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3601` | 8,700,000.00 USD | 8,700,000.00 USD | 0.00 USD | 161,200.00 USD | 338,540.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3604` | 8,850,000.00 USD | 8,850,000.00 USD | 61,130.00 USD | 32,860.00 USD | 81,590.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3607` | 9,090,000.00 USD | 9,090,000.00 USD | 325,970.00 USD | 68,030.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3608` | 9,040,000.00 USD | 9,040,000.00 USD | 48,390.00 USD | 21,980.00 USD | 113,790.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3612` | 9,360,000.00 USD | 9,360,000.00 USD | 37,640.00 USD | 43,670.00 USD | 236,630.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3613` | 9,780,000.00 USD | 9,780,000.00 USD | 73,540.00 USD | 330,040.00 USD | 288,930.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3615` | 743.61 USD | 743.61 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.3616` | 9,720,000.00 USD | 9,720,000.00 USD | 225,600.00 USD | 32,620.00 USD | 104,310.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3619` | 9,990,000.00 USD | 9,990,000.00 USD | 0.00 USD | 209,940.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3620` | 10,040,000.00 USD | 10,040,000.00 USD | 143,010.00 USD | 103,770.00 USD | 71,510.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3624` | 10,190,000.00 USD | 10,190,000.00 USD | 98,860.00 USD | 52,010.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3625` | 10,190,000.00 USD | 10,190,000.00 USD | 0.00 USD | 191,880.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3628` | 11,330,000.00 USD | 11,330,000.00 USD | 1,040,000.00 USD | 42,520.00 USD | 55,750.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3631` | 10,300,000.00 USD | 10,300,000.00 USD | 0.00 USD | 114,740.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3632` | 11,770,000.00 USD | 11,770,000.00 USD | 223,360.00 USD | 66,850.00 USD | 151,730.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3635` | 31,260.00 USD | 32,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.3636` | 12,070,000.00 USD | 12,070,000.00 USD | 183,690.00 USD | 48,500.00 USD | 71,910.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3637` | 10,320,000.00 USD | 10,320,000.00 USD | 1,540.00 USD | 21,530.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3640` | 12,380,000.00 USD | 12,380,000.00 USD | 0.00 USD | 229,250.00 USD | 76,240.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3643` | 11,120,000.00 USD | 11,120,000.00 USD | 3,350.00 USD | 0.00 USD | 789,140.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3644` | 12,720,000.00 USD | 12,720,000.00 USD | 294,060.00 USD | 16,650.00 USD | 35,280.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3645` | 12,390.00 USD | 44,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.3648` | 13,050,000.00 USD | 13,050,000.00 USD | 142,360.00 USD | 59,680.00 USD | 124,520.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3649` | 11,300,000.00 USD | 11,300,000.00 USD | 181,300.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3652` | 13,260,000.00 USD | 13,260,000.00 USD | 14,300.00 USD | 19,500.00 USD | 178,200.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3655` | 12,090,000.00 USD | 12,090,000.00 USD | 679,620.00 USD | 112,770.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3656` | 14,070,000.00 USD | 14,070,000.00 USD | 472,800.00 USD | 122,700.00 USD | 215,370.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3660` | 14,260,000.00 USD | 14,260,000.00 USD | 113,330.00 USD | 58,300.00 USD | 15,560.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3661` | 12,980,000.00 USD | 12,980,000.00 USD | 687,450.00 USD | 0.00 USD | 207,150.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3664` | 14,960,000.00 USD | 14,960,000.00 USD | 565,690.00 USD | 70,580.00 USD | 66,590.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3665` | 1,160.00 USD | 45,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.3667` | 13,520,000.00 USD | 13,520,000.00 USD | 422,000.00 USD | 15,390.00 USD | 103,350.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3668` | 15,390,000.00 USD | 15,390,000.00 USD | 149,300.00 USD | 62,870.00 USD | 217,960.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3672` | 15,710,000.00 USD | 15,710,000.00 USD | 5,540.00 USD | 84,880.00 USD | 221,800.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3673` | 14,210,000.00 USD | 14,210,000.00 USD | 511,100.00 USD | 53,040.00 USD | 122,410.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3675` | 1,960.00 USD | 47,520.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.3676` | 16,010,000.00 USD | 16,010,000.00 USD | 65,370.00 USD | 43,540.00 USD | 191,130.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3679` | 14,470,000.00 USD | 14,470,000.00 USD | 257,550.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3680` | 16,850,000.00 USD | 16,850,000.00 USD | 751,690.00 USD | 25,610.00 USD | 69,530.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3684` | 17,050,000.00 USD | 17,050,000.00 USD | 0.00 USD | 89,530.00 USD | 108,180.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3685` | 14,650,000.00 USD | 14,650,000.00 USD | 2,700.00 USD | 102,650.00 USD | 72,350.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3688` | 17,970,000.00 USD | 17,970,000.00 USD | 717,520.00 USD | 148,460.00 USD | 52,150.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3691` | 15,060,000.00 USD | 15,060,000.00 USD | 148,800.00 USD | 261,530.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3692` | 18,130,000.00 USD | 18,130,000.00 USD | 85,740.00 USD | 49,680.00 USD | 23,760.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3696` | 18,380,000.00 USD | 18,380,000.00 USD | 163,960.00 USD | 88,200.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3697` | 15,220,000.00 USD | 15,220,000.00 USD | 736.13 USD | 163,180.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3700` | 19,100,000.00 USD | 19,100,000.00 USD | 527,250.00 USD | 167,220.00 USD | 27,870.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3703` | 15,270,000.00 USD | 15,270,000.00 USD | 50,940.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3704` | 19,940,000.00 USD | 19,940,000.00 USD | 247,740.00 USD | 31,710.00 USD | 560,920.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3705` | 278.99 USD | 47,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.3708` | 20,090,000.00 USD | 20,090,000.00 USD | 111,100.00 USD | 21,340.00 USD | 12,600.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3712` | 20,850,000.00 USD | 20,850,000.00 USD | 439,350.00 USD | 93,240.00 USD | 225,950.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3715` | 15,670,000.00 USD | 15,670,000.00 USD | 1,320.00 USD | 0.00 USD | 394,570.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3715` | 179.43 USD | 47,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.3716` | 21,960,000.00 USD | 21,960,000.00 USD | 75,660.00 USD | 220,760.00 USD | 817,010.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3720` | 22,090,000.00 USD | 22,090,000.00 USD | 11,440.00 USD | 25,960.00 USD | 89,260.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3721` | 16,420,000.00 USD | 16,420,000.00 USD | 5,330.00 USD | 0.00 USD | 747,740.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3724` | 22,980,000.00 USD | 22,980,000.00 USD | 471,540.00 USD | 54,250.00 USD | 370,690.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3725` | 186.25 USD | 48,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.3727` | 16,700,000.00 USD | 16,700,000.00 USD | 213,190.00 USD | 0.00 USD | 66,870.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3728` | 23,620,000.00 USD | 23,620,000.00 USD | 34,330.00 USD | 100,040.00 USD | 503,910.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3732` | 24,400,000.00 USD | 24,400,000.00 USD | 61,850.00 USD | 61,600.00 USD | 655,100.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3733` | 16,890,000.00 USD | 16,890,000.00 USD | 188,670.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3735` | 7,210.00 USD | 55,370.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.3736` | 24,610,000.00 USD | 24,610,000.00 USD | 213,540.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3739` | 25,060,000.00 USD | 25,060,000.00 USD | 16,060.00 USD | 163,770.00 USD | 266,490.00 USD | `Tier 1 CEX` |
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
| `Live` | `Long` | `0.0775` | 1,210,000.00 USD | 0.00 USD | 3,170.00 USD | `-77.05%` | `40,871.00` |
| `Live` | `Long` | `0.0795` | 1,210,000.00 USD | 0.00 USD | 7,010.00 USD | `-76.46%` | `88,233.00` |
| `Live` | `Long` | `0.0845` | 1,200,000.00 USD | 0.00 USD | 120.67 USD | `-74.98%` | `1,428.00` |
| `Live` | `Long` | `0.0865` | 1,200,000.00 USD | 0.00 USD | 179.83 USD | `-74.39%` | `2,079.00` |
| `Live` | `Long` | `0.0925` | 1,200,000.00 USD | 0.00 USD | 918.15 USD | `-72.61%` | `9,926.00` |
| `Live` | `Long` | `0.1145` | 1,200,000.00 USD | 0.00 USD | 2,290.00 USD | `-66.10%` | `20,000.00` |
| `Live` | `Long` | `0.1165` | 1,200,000.00 USD | 0.00 USD | 391.44 USD | `-65.51%` | `3,360.00` |
| `Live` | `Long` | `0.1315` | 1,200,000.00 USD | 0.00 USD | 10,100.00 USD | `-61.07%` | `76,797.00` |
| `Live` | `Long` | `0.1515` | 1,190,000.00 USD | 0.00 USD | 48,430.00 USD | `-55.14%` | `319,639.00` |
| `Live` | `Long` | `0.1575` | 1,140,000.00 USD | 0.00 USD | 6,470.00 USD | `-53.37%` | `41,100.00` |
| `Live` | `Long` | `0.1585` | 1,130,000.00 USD | 0.00 USD | 388.01 USD | `-53.07%` | `2,448.00` |
| `Live` | `Long` | `0.1655` | 1,130,000.00 USD | 0.00 USD | 496.50 USD | `-51.00%` | `3,000.00` |
| `Live` | `Long` | `0.1675` | 1,130,000.00 USD | 0.00 USD | 36,640.00 USD | `-50.41%` | `218,745.00` |
| `Live` | `Long` | `0.1685` | 1,090,000.00 USD | 0.00 USD | 20,120.00 USD | `-50.11%` | `119,400.00` |
| `Live` | `Long` | `0.1695` | 1,070,000.00 USD | 0.00 USD | 3,390.00 USD | `-49.81%` | `20,000.00` |
| `Live` | `Long` | `0.1725` | 1,070,000.00 USD | 0.00 USD | 11,100.00 USD | `-48.93%` | `64,322.00` |
| `Live` | `Long` | `0.1735` | 1,060,000.00 USD | 0.00 USD | 339.71 USD | `-48.63%` | `1,958.00` |
| `Live` | `Long` | `0.1745` | 1,060,000.00 USD | 0.00 USD | 5,280.00 USD | `-48.33%` | `30,233.00` |
| `Live` | `Long` | `0.1755` | 1,050,000.00 USD | 0.00 USD | 1,430.00 USD | `-48.04%` | `8,162.00` |
| `Live` | `Long` | `0.1765` | 1,050,000.00 USD | 0.00 USD | 333.06 USD | `-47.74%` | `1,887.00` |
| `Live` | `Long` | `0.1775` | 1,050,000.00 USD | 0.00 USD | 207.50 USD | `-47.45%` | `1,169.00` |
| `Live` | `Long` | `0.1815` | 1,050,000.00 USD | 0.00 USD | 100.37 USD | `-46.26%` | `553.00` |
| `Live` | `Long` | `0.1875` | 1,050,000.00 USD | 0.00 USD | 36,310.00 USD | `-44.49%` | `193,636.00` |
| `Live` | `Long` | `0.1975` | 1,020,000.00 USD | 0.00 USD | 632.00 USD | `-41.52%` | `3,200.00` |
| `Live` | `Long` | `0.2155` | 1,010,000.00 USD | 0.00 USD | 194.81 USD | `-36.20%` | `904.00` |
| `Live` | `Long` | `0.2165` | 1,010,000.00 USD | 0.00 USD | 2,000.00 USD | `-35.90%` | `9,239.00` |
| `Live` | `Long` | `0.2175` | 1,010,000.00 USD | 0.00 USD | 227.29 USD | `-35.60%` | `1,045.00` |
| `Live` | `Long` | `0.2185` | 1,010,000.00 USD | 0.00 USD | 512.82 USD | `-35.31%` | `2,347.00` |
| `Live` | `Long` | `0.2245` | 1,010,000.00 USD | 0.00 USD | 4,570.00 USD | `-33.53%` | `20,360.00` |
| `Live` | `Long` | `0.2285` | 1,010,000.00 USD | 0.00 USD | 111.97 USD | `-32.35%` | `490.00` |
| `Live` | `Long` | `0.2295` | 1,010,000.00 USD | 0.00 USD | 2,070.00 USD | `-32.05%` | `9,004.00` |
| `Live` | `Long` | `0.2305` | 1,010,000.00 USD | 0.00 USD | 410.06 USD | `-31.75%` | `1,779.00` |
| `Live` | `Long` | `0.2325` | 1,000,000.00 USD | 0.00 USD | 2,040.00 USD | `-31.16%` | `8,767.00` |
| `Live` | `Long` | `0.2335` | 1,000,000.00 USD | 0.00 USD | 797.64 USD | `-30.87%` | `3,416.00` |
| `Live` | `Long` | `0.2345` | 1,000,000.00 USD | 0.00 USD | 5,700.00 USD | `-30.57%` | `24,311.00` |
| `Live` | `Long` | `0.2355` | 996,250.00 USD | 0.00 USD | 3,130.00 USD | `-30.27%` | `13,311.00` |
| `Live` | `Long` | `0.2365` | 993,110.00 USD | 0.00 USD | 686.56 USD | `-29.98%` | `2,903.00` |
| `Live` | `Long` | `0.2375` | 992,430.00 USD | 0.00 USD | 568.81 USD | `-29.68%` | `2,395.00` |
| `Live` | `Long` | `0.2395` | 991,860.00 USD | 0.00 USD | 1,570.00 USD | `-29.09%` | `6,544.00` |
| `Live` | `Long` | `0.2415` | 990,290.00 USD | 0.00 USD | 139.35 USD | `-28.50%` | `577.00` |
| `Live` | `Long` | `0.2435` | 990,150.00 USD | 0.00 USD | 885.85 USD | `-27.91%` | `3,638.00` |
| `Live` | `Long` | `0.2445` | 989,270.00 USD | 0.00 USD | 3,380.00 USD | `-27.61%` | `13,828.00` |
| `Live` | `Long` | `0.2455` | 985,890.00 USD | 0.00 USD | 384.94 USD | `-27.31%` | `1,568.00` |
| `Live` | `Long` | `0.2485` | 985,500.00 USD | 0.00 USD | 11,890.00 USD | `-26.42%` | `47,833.00` |
| `Live` | `Long` | `0.2505` | 973,610.00 USD | 0.00 USD | 262.02 USD | `-25.83%` | `1,046.00` |
| `Live` | `Long` | `0.2555` | 973,350.00 USD | 0.00 USD | 1,220.00 USD | `-24.35%` | `4,794.00` |
| `Live` | `Long` | `0.2575` | 972,130.00 USD | 0.00 USD | 301.79 USD | `-23.76%` | `1,172.00` |
| `Live` | `Long` | `0.2595` | 971,830.00 USD | 0.00 USD | 749.18 USD | `-23.17%` | `2,887.00` |
| `Live` | `Long` | `0.2625` | 971,080.00 USD | 0.00 USD | 108.15 USD | `-22.28%` | `412.00` |
| `Live` | `Long` | `0.2645` | 970,970.00 USD | 0.00 USD | 2,650.00 USD | `-21.69%` | `10,032.00` |
| `Live` | `Long` | `0.2655` | 968,320.00 USD | 0.00 USD | 193.02 USD | `-21.39%` | `727.00` |
| `Live` | `Long` | `0.2675` | 968,120.00 USD | 0.00 USD | 321.54 USD | `-20.80%` | `1,202.00` |
| `Live` | `Long` | `0.2685` | 967,800.00 USD | 0.00 USD | 3,150.00 USD | `-20.50%` | `11,746.00` |
| `Live` | `Long` | `0.2745` | 964,650.00 USD | 0.00 USD | 84,690.00 USD | `-18.73%` | `308,536.00` |
| `Live` | `Long` | `0.2785` | 879,950.00 USD | 0.00 USD | 13,010.00 USD | `-17.54%` | `46,725.00` |
| `Live` | `Long` | `0.2795` | 866,940.00 USD | 0.00 USD | 6,260.00 USD | `-17.25%` | `22,380.00` |
| `Live` | `Long` | `0.2805` | 860,690.00 USD | 0.00 USD | 605.32 USD | `-16.95%` | `2,158.00` |
| `Live` | `Long` | `0.2815` | 860,080.00 USD | 0.00 USD | 15,010.00 USD | `-16.65%` | `53,321.00` |
| `Live` | `Long` | `0.2825` | 845,070.00 USD | 0.00 USD | 1,730.00 USD | `-16.36%` | `6,123.00` |
| `Live` | `Long` | `0.2855` | 843,340.00 USD | 0.00 USD | 6,660.00 USD | `-15.47%` | `23,313.00` |
| `Live` | `Long` | `0.2865` | 836,680.00 USD | 0.00 USD | 4,150.00 USD | `-15.17%` | `14,481.00` |
| `Live` | `Long` | `0.2905` | 832,540.00 USD | 0.00 USD | 821.82 USD | `-13.99%` | `2,829.00` |
| `Live` | `Long` | `0.2915` | 831,710.00 USD | 0.00 USD | 954.37 USD | `-13.69%` | `3,274.00` |
| `Live` | `Long` | `0.2935` | 830,760.00 USD | 0.00 USD | 213.08 USD | `-13.10%` | `726.00` |
| `Live` | `Long` | `0.2945` | 830,550.00 USD | 0.00 USD | 124.87 USD | `-12.81%` | `424.00` |
| `Live` | `Long` | `0.2955` | 830,420.00 USD | 0.00 USD | 156.61 USD | `-12.51%` | `530.00` |
| `Live` | `Long` | `0.2975` | 830,270.00 USD | 0.00 USD | 1,010.00 USD | `-11.92%` | `3,398.00` |
| `Live` | `Long` | `0.2985` | 829,250.00 USD | 0.00 USD | 759.68 USD | `-11.62%` | `2,545.00` |
| `Live` | `Long` | `0.2995` | 828,490.00 USD | 0.00 USD | 197.37 USD | `-11.32%` | `659.00` |
| `Live` | `Long` | `0.3005` | 828,300.00 USD | 0.00 USD | 10,490.00 USD | `-11.03%` | `34,910.00` |
| `Live` | `Long` | `0.3015` | 817,810.00 USD | 0.00 USD | 128.44 USD | `-10.73%` | `426.00` |
| `Live` | `Long` | `0.3025` | 817,680.00 USD | 0.00 USD | 2,620.00 USD | `-10.44%` | `8,655.00` |
| `Live` | `Long` | `0.3035` | 815,060.00 USD | 0.00 USD | 266.47 USD | `-10.14%` | `878.00` |
| `Live` | `Long` | `0.3045` | 814,790.00 USD | 0.00 USD | 138.24 USD | `-9.84%` | `454.00` |
| `Live` | `Long` | `0.3055` | 814,660.00 USD | 0.00 USD | 14,670.00 USD | `-9.55%` | `48,026.00` |
| `Live` | `Long` | `0.3075` | 799,980.00 USD | 0.00 USD | 6,650.00 USD | `-8.96%` | `21,612.00` |
| `Live` | `Long` | `0.3085` | 793,340.00 USD | 0.00 USD | 291.53 USD | `-8.66%` | `945.00` |
| `Live` | `Long` | `0.3095` | 793,050.00 USD | 0.00 USD | 192.51 USD | `-8.36%` | `622.00` |
| `Live` | `Long` | `0.3105` | 792,850.00 USD | 0.00 USD | 820.96 USD | `-8.07%` | `2,644.00` |
| `Live` | `Long` | `0.3115` | 792,030.00 USD | 0.00 USD | 13,600.00 USD | `-7.77%` | `43,671.00` |
| `Live` | `Long` | `0.3125` | 778,430.00 USD | 0.00 USD | 17,570.00 USD | `-7.48%` | `56,226.00` |
| `Live` | `Long` | `0.3135` | 760,860.00 USD | 0.00 USD | 681.55 USD | `-7.18%` | `2,174.00` |
| `Live` | `Long` | `0.3145` | 760,180.00 USD | 0.00 USD | 116.05 USD | `-6.88%` | `369.00` |
| `Live` | `Long` | `0.3155` | 760,060.00 USD | 0.00 USD | 1,370.00 USD | `-6.59%` | `4,354.00` |
| `Live` | `Long` | `0.3165` | 758,690.00 USD | 0.00 USD | 2,360.00 USD | `-6.29%` | `7,449.00` |
| `Live` | `Long` | `0.3175` | 756,330.00 USD | 0.00 USD | 4,060.00 USD | `-6.00%` | `12,777.00` |
| `Live` | `Long` | `0.3185` | 752,270.00 USD | 0.00 USD | 642.10 USD | `-5.70%` | `2,016.00` |
| `Live` | `Long` | `0.3205` | 751,630.00 USD | 0.00 USD | 455.75 USD | `-5.11%` | `1,422.00` |
| `Live` | `Long` | `0.3235` | 751,180.00 USD | 0.00 USD | 128.43 USD | `-4.22%` | `397.00` |
| `Live` | `Long` | `0.3275` | 751,050.00 USD | 0.00 USD | 163.42 USD | `-3.03%` | `499.00` |
| `Live` | `Long` | `0.3285` | 750,880.00 USD | 0.00 USD | 745,260.00 USD | `-2.74%` | `2,268,686.00` |
| `Live` | `Long` | `0.3295` | 5,620.00 USD | 0.00 USD | 839.90 USD | `-2.44%` | `2,549.00` |
| `Live` | `Long` | `0.3315` | 4,780.00 USD | 0.00 USD | 4,780.00 USD | `-1.85%` | `14,420.00` |
| `Live` | `Short` | `0.3615` | 743.61 USD | 743.61 USD | 0.00 USD | `+7.03%` | `2,057.00` |
| `Live` | `Short` | `0.3635` | 32,000.00 USD | 31,260.00 USD | 0.00 USD | `+7.62%` | `85,992.00` |
| `Live` | `Short` | `0.3645` | 44,400.00 USD | 12,390.00 USD | 0.00 USD | `+7.92%` | `34,003.00` |
| `Live` | `Short` | `0.3665` | 45,560.00 USD | 1,160.00 USD | 0.00 USD | `+8.51%` | `3,165.00` |
| `Live` | `Short` | `0.3675` | 47,520.00 USD | 1,960.00 USD | 0.00 USD | `+8.81%` | `5,333.00` |
| `Live` | `Short` | `0.3705` | 47,790.00 USD | 278.99 USD | 0.00 USD | `+9.70%` | `753.00` |
| `Live` | `Short` | `0.3715` | 47,970.00 USD | 179.43 USD | 0.00 USD | `+9.99%` | `483.00` |
| `Live` | `Short` | `0.3725` | 48,160.00 USD | 186.25 USD | 0.00 USD | `+10.29%` | `500.00` |
| `Live` | `Short` | `0.3735` | 55,370.00 USD | 7,210.00 USD | 0.00 USD | `+10.58%` | `19,294.00` |
| `Live` | `Short` | `0.3755` | 61,480.00 USD | 6,120.00 USD | 0.00 USD | `+11.18%` | `16,287.00` |
| `Live` | `Short` | `0.3775` | 61,590.00 USD | 104.19 USD | 0.00 USD | `+11.77%` | `276.00` |
| `Live` | `Short` | `0.3785` | 618,010.00 USD | 556,430.00 USD | 0.00 USD | `+12.07%` | `1,470,083.00` |
| `Live` | `Short` | `0.3835` | 618,130.00 USD | 115.05 USD | 0.00 USD | `+13.55%` | `300.00` |
| `Live` | `Short` | `0.3865` | 618,390.00 USD | 265.53 USD | 0.00 USD | `+14.43%` | `687.00` |
| `Live` | `Short` | `0.3895` | 623,150.00 USD | 4,760.00 USD | 0.00 USD | `+15.32%` | `12,210.00` |
| `Live` | `Short` | `0.3905` | 629,150.00 USD | 6,000.00 USD | 0.00 USD | `+15.62%` | `15,374.00` |
| `Live` | `Short` | `0.3935` | 630,640.00 USD | 1,480.00 USD | 0.00 USD | `+16.51%` | `3,770.00` |
| `Live` | `Short` | `0.3945` | 748,760.00 USD | 118,130.00 USD | 0.00 USD | `+16.80%` | `299,436.00` |
| `Live` | `Short` | `0.4085` | 748,930.00 USD | 170.75 USD | 0.00 USD | `+20.95%` | `418.00` |
| `Live` | `Short` | `0.4095` | 749,170.00 USD | 239.56 USD | 0.00 USD | `+21.24%` | `585.00` |
| `Live` | `Short` | `0.4185` | 750,310.00 USD | 1,130.00 USD | 0.00 USD | `+23.91%` | `2,704.00` |
| `Live` | `Short` | `0.4295` | 760,520.00 USD | 10,210.00 USD | 0.00 USD | `+27.17%` | `23,779.00` |
| `Live` | `Short` | `0.4305` | 762,010.00 USD | 1,490.00 USD | 0.00 USD | `+27.46%` | `3,464.00` |
| `Live` | `Short` | `0.4315` | 767,490.00 USD | 5,480.00 USD | 0.00 USD | `+27.76%` | `12,710.00` |
| `Live` | `Short` | `0.4365` | 840,040.00 USD | 72,540.00 USD | 0.00 USD | `+29.24%` | `166,191.00` |
| `Live` | `Short` | `0.4415` | 840,410.00 USD | 377.48 USD | 0.00 USD | `+30.72%` | `855.00` |
| `Live` | `Short` | `0.4445` | 862,640.00 USD | 22,230.00 USD | 0.00 USD | `+31.61%` | `50,000.00` |
| `Live` | `Short` | `0.4465` | 863,660.00 USD | 1,020.00 USD | 0.00 USD | `+32.20%` | `2,284.00` |
| `Live` | `Short` | `0.4475` | 929,270.00 USD | 65,610.00 USD | 0.00 USD | `+32.49%` | `146,614.00` |
| `Live` | `Short` | `0.4515` | 929,590.00 USD | 318.76 USD | 0.00 USD | `+33.68%` | `706.00` |
| `Live` | `Short` | `0.4525` | 930,160.00 USD | 570.15 USD | 0.00 USD | `+33.97%` | `1,260.00` |
| `Live` | `Short` | `0.4625` | 930,430.00 USD | 267.32 USD | 0.00 USD | `+36.94%` | `578.00` |
| `Live` | `Short` | `0.4705` | 1,210,000.00 USD | 282,390.00 USD | 0.00 USD | `+39.30%` | `600,198.00` |
| `Live` | `Short` | `0.4805` | 1,220,000.00 USD | 2,880.00 USD | 0.00 USD | `+42.26%` | `6,000.00` |
| `Live` | `Short` | `0.4895` | 1,220,000.00 USD | 839.49 USD | 0.00 USD | `+44.93%` | `1,715.00` |
| `Live` | `Short` | `0.4905` | 1,220,000.00 USD | 5,120.00 USD | 0.00 USD | `+45.23%` | `10,430.00` |
| `Live` | `Short` | `0.4995` | 1,220,000.00 USD | 2,730.00 USD | 0.00 USD | `+47.89%` | `5,465.00` |
| `Live` | `Short` | `0.5015` | 1,250,000.00 USD | 23,370.00 USD | 0.00 USD | `+48.48%` | `46,591.00` |
| `Live` | `Short` | `0.5335` | 1,250,000.00 USD | 668.48 USD | 0.00 USD | `+57.96%` | `1,253.00` |
| `Live` | `Short` | `0.5545` | 1,290,000.00 USD | 41,030.00 USD | 0.00 USD | `+64.17%` | `74,000.00` |
| `Live` | `Short` | `0.5575` | 1,290,000.00 USD | 740.92 USD | 0.00 USD | `+65.06%` | `1,329.00` |
| `Live` | `Short` | `0.5585` | 1,290,000.00 USD | 2,320.00 USD | 0.00 USD | `+65.36%` | `4,154.00` |
| `Live` | `Short` | `0.5615` | 1,290,000.00 USD | 140.38 USD | 0.00 USD | `+66.25%` | `250.00` |
| `Live` | `Short` | `0.5685` | 2,030,000.00 USD | 737,490.00 USD | 0.00 USD | `+68.32%` | `1,297,248.00` |
| `Live` | `Short` | `0.6135` | 2,030,000.00 USD | 371.17 USD | 0.00 USD | `+81.64%` | `605.00` |
| `Live` | `Short` | `0.6145` | 2,030,000.00 USD | 3,920.00 USD | 0.00 USD | `+81.94%` | `6,380.00` |
| `Live` | `Short` | `0.6155` | 2,060,000.00 USD | 24,620.00 USD | 0.00 USD | `+82.24%` | `40,000.00` |
| `Live` | `Short` | `0.6215` | 2,060,000.00 USD | 793.03 USD | 0.00 USD | `+84.01%` | `1,276.00` |
| `Live` | `Short` | `0.6275` | 2,060,000.00 USD | 1,130.00 USD | 0.00 USD | `+85.79%` | `1,808.00` |
| `Live` | `Short` | `0.6345` | 2,070,000.00 USD | 6,820.00 USD | 0.00 USD | `+87.86%` | `10,756.00` |
| `Live` | `Short` | `0.6515` | 2,170,000.00 USD | 103,110.00 USD | 0.00 USD | `+92.89%` | `158,269.00` |
| `Live` | `Short` | `0.6545` | 2,170,000.00 USD | 706.21 USD | 0.00 USD | `+93.78%` | `1,079.00` |
| `Live` | `Short` | `0.6615` | 2,170,000.00 USD | 2,060.00 USD | 0.00 USD | `+95.85%` | `3,114.00` |
| `Live` | `Short` | `0.6635` | 2,180,000.00 USD | 3,740.00 USD | 0.00 USD | `+96.45%` | `5,632.00` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `0.0665` | 888,870.00 USD | 0.00 USD | 112.32 USD | `-80.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0945` | 888,760.00 USD | 0.00 USD | 198.45 USD | `-72.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1415` | 888,560.00 USD | 0.00 USD | 330.26 USD | `-58.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2035` | 888,230.00 USD | 0.00 USD | 1,750.00 USD | `-39.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2105` | 886,480.00 USD | 0.00 USD | 2,220.00 USD | `-37.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2195` | 884,260.00 USD | 0.00 USD | 450.41 USD | `-35.01%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2305` | 883,810.00 USD | 0.00 USD | 121.70 USD | `-31.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2345` | 883,690.00 USD | 0.00 USD | 705.61 USD | `-30.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2355` | 882,990.00 USD | 0.00 USD | 159.20 USD | `-30.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2405` | 882,830.00 USD | 0.00 USD | 1,200.00 USD | `-28.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2415` | 881,630.00 USD | 0.00 USD | 127.51 USD | `-28.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2505` | 881,500.00 USD | 0.00 USD | 1,850.00 USD | `-25.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2515` | 879,640.00 USD | 0.00 USD | 41,500.00 USD | `-25.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2565` | 838,150.00 USD | 0.00 USD | 1,920.00 USD | `-24.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2605` | 836,220.00 USD | 0.00 USD | 664.01 USD | `-22.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2625` | 835,560.00 USD | 0.00 USD | 954.98 USD | `-22.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2635` | 834,600.00 USD | 0.00 USD | 103.56 USD | `-21.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2675` | 834,500.00 USD | 0.00 USD | 695.50 USD | `-20.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2685` | 833,800.00 USD | 0.00 USD | 1,630.00 USD | `-20.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2695` | 832,180.00 USD | 0.00 USD | 1,470.00 USD | `-20.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2755` | 830,700.00 USD | 0.00 USD | 101.94 USD | `-18.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2775` | 830,600.00 USD | 0.00 USD | 3,260.00 USD | `-17.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2815` | 827,340.00 USD | 0.00 USD | 2,550.00 USD | `-16.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2835` | 824,790.00 USD | 0.00 USD | 229.92 USD | `-16.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2875` | 824,560.00 USD | 0.00 USD | 8,010.00 USD | `-14.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2935` | 816,550.00 USD | 0.00 USD | 11,610.00 USD | `-13.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2965` | 804,940.00 USD | 0.00 USD | 111.19 USD | `-12.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2985` | 804,830.00 USD | 0.00 USD | 433.42 USD | `-11.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3005` | 804,400.00 USD | 0.00 USD | 2,710.00 USD | `-11.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3045` | 801,690.00 USD | 0.00 USD | 503.95 USD | `-9.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3065` | 801,190.00 USD | 0.00 USD | 1,400.00 USD | `-9.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3075` | 799,790.00 USD | 0.00 USD | 193.11 USD | `-8.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3085` | 799,590.00 USD | 0.00 USD | 15,150.00 USD | `-8.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3095` | 784,440.00 USD | 0.00 USD | 156.30 USD | `-8.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3105` | 784,280.00 USD | 0.00 USD | 12,200.00 USD | `-8.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3115` | 772,080.00 USD | 0.00 USD | 6,530.00 USD | `-7.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3125` | 765,550.00 USD | 0.00 USD | 524,570.00 USD | `-7.48%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3135` | 240,980.00 USD | 0.00 USD | 1,270.00 USD | `-7.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3145` | 239,710.00 USD | 0.00 USD | 53,690.00 USD | `-6.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3155` | 186,030.00 USD | 0.00 USD | 2,570.00 USD | `-6.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3165` | 183,460.00 USD | 0.00 USD | 6,100.00 USD | `-6.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3175` | 177,360.00 USD | 0.00 USD | 850.90 USD | `-6.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3185` | 176,510.00 USD | 0.00 USD | 1,160.00 USD | `-5.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3195` | 175,350.00 USD | 0.00 USD | 6,220.00 USD | `-5.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3205` | 169,130.00 USD | 0.00 USD | 10,320.00 USD | `-5.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3215` | 158,810.00 USD | 0.00 USD | 43,760.00 USD | `-4.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3225` | 115,040.00 USD | 0.00 USD | 131.90 USD | `-4.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3235` | 114,910.00 USD | 0.00 USD | 7,040.00 USD | `-4.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3245` | 107,870.00 USD | 0.00 USD | 3,870.00 USD | `-3.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3255` | 104,000.00 USD | 0.00 USD | 65,070.00 USD | `-3.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3265` | 38,930.00 USD | 0.00 USD | 6,130.00 USD | `-3.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3275` | 32,800.00 USD | 0.00 USD | 7,430.00 USD | `-3.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3285` | 25,360.00 USD | 0.00 USD | 4,270.00 USD | `-2.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3295` | 21,090.00 USD | 0.00 USD | 1,960.00 USD | `-2.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3305` | 19,140.00 USD | 0.00 USD | 949.53 USD | `-2.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3315` | 18,190.00 USD | 0.00 USD | 100.11 USD | `-1.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3325` | 18,090.00 USD | 0.00 USD | 5,730.00 USD | `-1.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3335` | 12,360.00 USD | 0.00 USD | 4,880.00 USD | `-1.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3345` | 7,480.00 USD | 0.00 USD | 6,940.00 USD | `-0.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3355` | 542.77 USD | 0.00 USD | 138.56 USD | `-0.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3365` | 404.21 USD | 0.00 USD | 265.50 USD | `-0.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3375` | 138.71 USD | 0.00 USD | 138.71 USD | `-0.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3385` | 157.74 USD | 157.74 USD | 0.00 USD | `+0.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3395` | 7,070.00 USD | 6,910.00 USD | 0.00 USD | `+0.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3405` | 8,470.00 USD | 1,400.00 USD | 0.00 USD | `+0.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3415` | 8,960.00 USD | 486.30 USD | 0.00 USD | `+1.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3425` | 9,390.00 USD | 431.55 USD | 0.00 USD | `+1.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3435` | 10,220.00 USD | 828.18 USD | 0.00 USD | `+1.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3445` | 12,160.00 USD | 1,950.00 USD | 0.00 USD | `+2.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3455` | 12,600.00 USD | 435.33 USD | 0.00 USD | `+2.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3465` | 13,160.00 USD | 555.44 USD | 0.00 USD | `+2.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3475` | 13,430.00 USD | 274.18 USD | 0.00 USD | `+2.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3485` | 13,870.00 USD | 439.11 USD | 0.00 USD | `+3.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3495` | 14,860.00 USD | 996.08 USD | 0.00 USD | `+3.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3505` | 15,530.00 USD | 665.60 USD | 0.00 USD | `+3.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3515` | 16,450.00 USD | 919.52 USD | 0.00 USD | `+4.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3525` | 25,140.00 USD | 8,690.00 USD | 0.00 USD | `+4.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3535` | 25,460.00 USD | 312.14 USD | 0.00 USD | `+4.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3545` | 25,810.00 USD | 354.50 USD | 0.00 USD | `+4.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3555` | 25,940.00 USD | 132.96 USD | 0.00 USD | `+5.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3565` | 65,370.00 USD | 39,430.00 USD | 0.00 USD | `+5.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3575` | 105,760.00 USD | 40,390.00 USD | 0.00 USD | `+5.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3585` | 109,070.00 USD | 3,310.00 USD | 0.00 USD | `+6.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3595` | 110,100.00 USD | 1,030.00 USD | 0.00 USD | `+6.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3605` | 113,040.00 USD | 2,940.00 USD | 0.00 USD | `+6.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3615` | 113,270.00 USD | 224.49 USD | 0.00 USD | `+7.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3635` | 113,370.00 USD | 103.23 USD | 0.00 USD | `+7.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3645` | 116,070.00 USD | 2,700.00 USD | 0.00 USD | `+7.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3655` | 157,810.00 USD | 41,740.00 USD | 0.00 USD | `+8.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3665` | 158,240.00 USD | 433.57 USD | 0.00 USD | `+8.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3675` | 158,410.00 USD | 172.72 USD | 0.00 USD | `+8.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3685` | 158,630.00 USD | 218.89 USD | 0.00 USD | `+9.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3695` | 172,970.00 USD | 14,330.00 USD | 0.00 USD | `+9.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3705` | 176,440.00 USD | 3,480.00 USD | 0.00 USD | `+9.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3715` | 176,620.00 USD | 174.60 USD | 0.00 USD | `+9.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3725` | 176,730.00 USD | 107.28 USD | 0.00 USD | `+10.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3735` | 177,170.00 USD | 439.61 USD | 0.00 USD | `+10.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3745` | 177,600.00 USD | 437.79 USD | 0.00 USD | `+10.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3755` | 180,000.00 USD | 2,400.00 USD | 0.00 USD | `+11.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3765` | 180,180.00 USD | 182.60 USD | 0.00 USD | `+11.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3775` | 186,640.00 USD | 6,450.00 USD | 0.00 USD | `+11.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3785` | 186,910.00 USD | 275.17 USD | 0.00 USD | `+12.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3795` | 187,480.00 USD | 569.25 USD | 0.00 USD | `+12.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3805` | 193,460.00 USD | 5,980.00 USD | 0.00 USD | `+12.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3815` | 193,710.00 USD | 257.89 USD | 0.00 USD | `+12.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3825` | 193,980.00 USD | 262.78 USD | 0.00 USD | `+13.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3835` | 194,200.00 USD | 224.73 USD | 0.00 USD | `+13.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3855` | 194,820.00 USD | 621.04 USD | 0.00 USD | `+14.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3865` | 195,560.00 USD | 742.08 USD | 0.00 USD | `+14.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3875` | 196,680.00 USD | 1,110.00 USD | 0.00 USD | `+14.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3885` | 196,860.00 USD | 181.04 USD | 0.00 USD | `+15.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3895` | 197,350.00 USD | 490.38 USD | 0.00 USD | `+15.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3905` | 197,490.00 USD | 138.63 USD | 0.00 USD | `+15.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3915` | 197,760.00 USD | 276.40 USD | 0.00 USD | `+15.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3945` | 197,890.00 USD | 126.24 USD | 0.00 USD | `+16.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3965` | 200,290.00 USD | 2,400.00 USD | 0.00 USD | `+17.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3975` | 201,700.00 USD | 1,410.00 USD | 0.00 USD | `+17.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3985` | 202,900.00 USD | 1,200.00 USD | 0.00 USD | `+17.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3995` | 274,390.00 USD | 71,490.00 USD | 0.00 USD | `+18.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4005` | 275,260.00 USD | 864.28 USD | 0.00 USD | `+18.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4015` | 279,180.00 USD | 3,920.00 USD | 0.00 USD | `+18.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4035` | 358,510.00 USD | 79,330.00 USD | 0.00 USD | `+19.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4055` | 359,710.00 USD | 1,200.00 USD | 0.00 USD | `+20.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4065` | 360,910.00 USD | 1,200.00 USD | 0.00 USD | `+20.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4085` | 361,050.00 USD | 138.07 USD | 0.00 USD | `+20.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4095` | 362,310.00 USD | 1,270.00 USD | 0.00 USD | `+21.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4135` | 362,650.00 USD | 331.63 USD | 0.00 USD | `+22.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4175` | 362,960.00 USD | 313.54 USD | 0.00 USD | `+23.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4205` | 363,150.00 USD | 186.70 USD | 0.00 USD | `+24.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4275` | 363,470.00 USD | 325.75 USD | 0.00 USD | `+26.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4305` | 363,660.00 USD | 183.82 USD | 0.00 USD | `+27.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4355` | 363,960.00 USD | 299.19 USD | 0.00 USD | `+28.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4405` | 402,530.00 USD | 38,580.00 USD | 0.00 USD | `+30.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4445` | 402,700.00 USD | 170.69 USD | 0.00 USD | `+31.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4475` | 402,840.00 USD | 135.59 USD | 0.00 USD | `+32.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4495` | 404,360.00 USD | 1,520.00 USD | 0.00 USD | `+33.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4505` | 404,680.00 USD | 320.31 USD | 0.00 USD | `+33.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4545` | 410,020.00 USD | 5,340.00 USD | 0.00 USD | `+34.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4605` | 411,490.00 USD | 1,470.00 USD | 0.00 USD | `+36.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4895` | 492,260.00 USD | 80,770.00 USD | 0.00 USD | `+44.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4905` | 492,430.00 USD | 169.22 USD | 0.00 USD | `+45.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4945` | 492,580.00 USD | 153.79 USD | 0.00 USD | `+46.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4965` | 493,310.00 USD | 724.89 USD | 0.00 USD | `+47.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.5005` | 504,460.00 USD | 11,150.00 USD | 0.00 USD | `+48.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.5055` | 506,390.00 USD | 1,930.00 USD | 0.00 USD | `+49.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.5295` | 506,520.00 USD | 135.02 USD | 0.00 USD | `+56.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6305` | 506,760.00 USD | 240.85 USD | 0.00 USD | `+86.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6325` | 507,860.00 USD | 1,100.00 USD | 0.00 USD | `+87.27%` | `TACTICAL (Retail Cluster)` |

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
| `5:00 UTC` | `0.3320` | `0.3319` | `0.3320` | `0.3323` | `0.3316` | 814,397.94 USD | 470,141.90 USD | 344,256.04 USD | 125,885.86 USD | `+15.46%` | `22B / 13S` |

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
  * `2026-10-30 14:10:12 IST`: [channelnewsasia.com] - (Sentiment: `Neutral`)
  * `2026-10-30 13:52:12 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 13:51:12 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 13:32:12 IST`: [kof.ethz.ch] - (Sentiment: `Neutral`)
  * `2026-10-30 13:24:12 IST`: [gerlachmacro.substack.com] - (Sentiment: `Neutral`)
  * `2026-10-30 13:24:12 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-30 13:22:12 IST`: [insee.fr] - (Sentiment: `Neutral`)
  * `2026-10-30 13:21:12 IST`: [insee.fr] - (Sentiment: `Neutral`)
  * `2026-10-30 14:17:12 IST`: [@FirstSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 14:17:12 IST`: [nationwide.co.uk] - (Sentiment: `Neutral`)
  * `2026-10-30 14:17:12 IST`: [destatis.de] - (Sentiment: `Neutral`)
  * `2026-10-30 14:17:12 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-30 14:17:12 IST`: [@FirstSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 14:16:12 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-30 14:16:12 IST`: [insee.fr] - (Sentiment: `Neutral`)


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
  * Execution Entry: `0.3431` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `0.3360` (Risk Distance: `0.0071` pts)
  * +2.5R Take Profit: `0.3609`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `0.3578` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `0.3649` (Risk Distance: `0.0071` pts)
  * +2.5R Take Profit: `0.3400`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`0.3349`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
