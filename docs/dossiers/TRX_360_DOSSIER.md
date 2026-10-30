# 🏛️ SOVEREIGN CANDIDATE DOSSIER: TRX
**Canonical Key**: `TRX` | **Broker Instrument**: `TRXUSD.p` | **Asset Class**: `Crypto Alt L1`
**Timestamp**: `2026-10-30 16:09:31 IST` (`2026-10-30 10:39:31 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `0.3366` | **Live Ask Quote**: `0.3406` | **Mid Price**: `0.3386`
- **Spread Points**: `40.00` | **Spread BPS**: `118.13 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `0.3445` | VWAP Z-Score: `-0.79` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `0.0029` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `50.91` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `0.3729` | Lower -3.00σ Band: `0.3161`
  * Upper +2.51σ Band: `0.3682` | Lower -2.51σ Band: `0.3208`
  * Upper +2.01σ Band: `0.3635` | Lower -2.01σ Band: `0.3255`
  * Upper +2.00σ Band: `0.3634` | Lower -2.00σ Band: `0.3256`
  * Upper +1.28σ Band: `0.3566` | Lower -1.28σ Band: `0.3324`
  * Upper +1.00σ Band: `0.3539` | Lower -1.00σ Band: `0.3350`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`0.3338` | EMA-20=`0.3353` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`0.3384` (Slope: `+0.0000`) | EMA-100=`0.3377`
  * Institutional Anchors: EMA-144=`0.3365` | EMA-200=`0.3352` (Slope: `-0.0987`) | EMA-233=`0.3346`
- **Range Boundaries**: 24H High=`0.3632` | 24H Low=`0.3275` | Weekly High=`0.3632` | Weekly Low=`0.3266`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `0.3580` (Distance: `-5.22%`)
  * Point of Control (POC) = `0.3513` (Distance: `-3.42%`)
  * Value Area Low (VAL) = `0.3396` (Distance: `-0.08%`)
  * Auction Positioning: `BELOW_VALUE (Imbalance)` | Session Bias: **`BULLISH (Above Pivot)`** | Market Regime: `FAILED_AUCTION_REVERSAL`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`0.3312` | POC=`0.3307` | VAL=`0.3293`
  * Prior Day Extremes: PDH=`0.3335` | PDL=`0.3275` | PDC=`0.3275`
  * Monday Range Blueprint: High=`0.3310` | Mid=`0.3300` | Low=`0.3289`
  * Developing Weekly Value Area: Weekly VAH=`0.3462` | Weekly POC=`0.3306` | Weekly VAL=`0.3267`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`0.3632` | Low=`0.3335`
  * London Session (08:00-16:00 UTC): High=`0.3444` | Low=`0.3299`
  * New York Session (13:00-21:00 UTC): High=`0.3374` | Low=`0.3319`
  * Initial Balance (First Hour): IB High=`0.3444` | IB Low=`0.3379`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `0.3372` - `0.3400`
  * Optimal Trade Entry (OTE 0.705): `0.3393`
  * Structural Invalidation Anchor (0.786): `0.3413`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `0.3347` | `0.3360` | `0.3347` | `0.3359` | `962,413` | 322,701.60 USD | -22,597.10 USD | `-7.00%` | -2,775,662.86 USD | `-0.06` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `5m` | `0.3359` | `0.3360` | `0.3343` | `0.3348` | `1,761,843` | 590,098.00 USD | -172,054.86 USD | `-29.16%` | -2,947,717.71 USD | `-1.01` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `5m` | `0.3348` | `0.3348` | `0.3344` | `0.3345` | `101,683` | 34,019.92 USD | -18,410.97 USD | `-54.12%` | -2,966,128.69 USD | `+0.15` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `0.3361` | `0.3364` | `0.3341` | `0.3346` | `5,867,877` | 1,965,380.04 USD | -165,908.48 USD | `-8.44%` | -2,682,956.82 USD | `+0.23` | **`BEARISH`** | `DELTA ALIGNED` |
| `15m` | `0.3346` | `0.3360` | `0.3335` | `0.3359` | `5,474,292` | 1,833,198.85 USD | -23,457.81 USD | `-1.28%` | -2,706,414.63 USD | `+0.31` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `15m` | `0.3359` | `0.3360` | `0.3343` | `0.3345` | `1,860,308` | 623,041.42 USD | -191,068.03 USD | `-30.67%` | -2,897,482.67 USD | `+0.14` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `1h` | `0.3371` | `0.3377` | `0.3307` | `0.3324` | `39,413,287` | 13,120,323.22 USD | 312,055.16 USD | `+2.38%` | -2,219,666.72 USD | `+0.21` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `1h` | `0.3324` | `0.3367` | `0.3318` | `0.3346` | `29,287,422` | 9,766,957.28 USD | -468,481.97 USD | `-4.80%` | -2,688,148.69 USD | `-0.16` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `1h` | `0.3346` | `0.3360` | `0.3335` | `0.3345` | `7,334,600` | 2,456,240.27 USD | -214,525.85 USD | `-8.73%` | -2,902,674.54 USD | `-0.03` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.3533` | `0.3608` | `0.3475` | `0.3495` | `257,452,106` | 91,407,782.04 USD | 2,108,185.60 USD | `+2.31%` | 4,840,432.56 USD | `+0.97` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `0.3495` | `0.3497` | `0.3310` | `0.3371` | `257,957,739` | 87,367,227.03 USD | -7,246,486.44 USD | `-8.29%` | -2,406,053.88 USD | `-1.94` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.3371` | `0.3377` | `0.3307` | `0.3345` | `76,037,806` | 25,344,356.06 USD | -370,591.66 USD | `-1.46%` | -2,776,645.54 USD | `+0.03` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `0.3314` | `0.3316` | `0.3310` | `0.3315` | `11,250,742` | 3,727,253.77 USD | 212,090.87 USD | `+5.69%` | 581,399.04 USD | `-1.00` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `0.3315` | `0.3653` | `0.3282` | `0.3533` | `793,774,795` | 276,969,161.06 USD | 2,150,847.92 USD | `+0.78%` | 2,732,246.96 USD | `+1.41` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `0.3533` | `0.3608` | `0.3475` | `0.3495` | `257,452,106` | 91,407,782.04 USD | 2,108,185.60 USD | `+2.31%` | 4,840,432.56 USD | `+0.97` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `0.3495` | `0.3497` | `0.3310` | `0.3371` | `257,957,739` | 87,367,227.03 USD | -7,246,486.44 USD | `-8.29%` | -2,406,053.88 USD | `-1.94` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.3371` | `0.3400` | `0.3307` | `0.3394` | `86,425,357` | 28,853,139.36 USD | -22,693.65 USD | `-0.08%` | -2,428,747.52 USD | `+0.12` | **`BEARISH`** | `BEARISH ABSORPTION` |

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
| --- | **`0.3386`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `MID` | Regular L2 Book | - | - | - | Interbank L2 | 0.00% | Interbank |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 16:01:49 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `1081` | `0xecb6...2b00` | `LONG` | 1,999,474.94 USD | `5,869,932.00` | `0.3344` | `0.3402` | `0.000000` | 36,708.61 USD | `+1.84%` | `10X Cross` |
| `1273` | `0x8dd7...fa30` | `SHORT` | 1,702,300.00 USD | `5,000,000.00` | `0.3334` | `0.3402` | `0.3731` | -35,499.93 USD | `-2.09%` | `6X Cross` |
| `1575` | `0xeadc...9d55` | `LONG` | 1,361,720.00 USD | `4,000,000.00` | `0.3421` | `0.3402` | `0.000000` | -6,758.09 USD | `-0.50%` | `10X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `0.3318` | 6,469.10 USD | `-` | `NEWS_INTEL` | `-` | #TRX Whale BUY: 6.47K USD at 0.3318 USD [API] | `2026-10-29 11:35:32` |
| `ANNOUNCEMENT` | `INFO` | `0.3318` | 9,999.82 USD | `-` | `NEWS_INTEL` | `-` | #TRX Whale BUY: 10.00K USD at 0.3318 USD [API] | `2026-10-29 11:35:32` |
| `ANNOUNCEMENT` | `INFO` | `0.3316` | 6,423.42 USD | `-` | `NEWS_INTEL` | `-` | #TRX Whale SELL: 6.42K USD at 0.3316 USD [API] | `2026-10-29 12:41:40` |
| `ANNOUNCEMENT` | `INFO` | `0.3318` | 6,464.73 USD | `-` | `NEWS_INTEL` | `-` | #TRX Whale SELL: 6.46K USD at 0.3318 USD [API] | `2026-10-29 13:28:43` |
| `ANNOUNCEMENT` | `INFO` | `0.3312` | 6,464.28 USD | `-` | `NEWS_INTEL` | `-` | #TRX Whale SELL: 6.46K USD at 0.3312 USD [API] | `2026-10-29 18:05:53` |
| `ANNOUNCEMENT` | `INFO` | `0.3314` | 5,738.36 USD | `-` | `NEWS_INTEL` | `-` | #TRX Whale BUY: 5.74K USD at 0.3314 USD [API] | `2026-10-29 18:33:20` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`0.3675` (Vol: 1,300,000.00 USD, Dist: `+8.72%`) | Long MP=`0.3298` (Vol: 509,400.00 USD, Dist: `--2.44%`)
  * 48H Horizon: Short MP=`0.3675` (Vol: 1,300,000.00 USD, Dist: `+8.72%`) | Long MP=`0.3249` (Vol: 724,200.00 USD, Dist: `--3.90%`)
  * 3D Horizon: Short MP=`0.3662` (Vol: 1,100,000.00 USD, Dist: `+8.32%`) | Long MP=`0.3250` (Vol: 996,100.00 USD, Dist: `--3.87%`)
  * 7D Horizon: Short MP=`0.3661` (Vol: 1,100,000.00 USD, Dist: `+8.31%`) | Long MP=`0.3248` (Vol: 1,000,000.00 USD, Dist: `--3.90%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long Liquidation` | `0.0785` | 6,930.00 USD | 1,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0795` | 226.18 USD | 1,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0875` | 868.52 USD | 1,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0905` | 188.15 USD | 1,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1145` | 2,450.00 USD | 1,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1155` | 265.88 USD | 1,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1165` | 123.26 USD | 1,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1385` | 11,410.00 USD | 1,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1475` | 44,010.00 USD | 1,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1585` | 388.01 USD | 1,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1675` | 10,230.00 USD | 1,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1685` | 20,120.00 USD | 1,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1705` | 511.50 USD | 1,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1715` | 4,470.00 USD | 1,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1725` | 10,440.00 USD | 1,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1735` | 339.71 USD | 1,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1745` | 5,170.00 USD | 1,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1755` | 38,650.00 USD | 1,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1765` | 174.38 USD | 1,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1775` | 1,400.00 USD | 1,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1815` | 100.37 USD | 1,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1845` | 165.87 USD | 1,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1855` | 109.63 USD | 1,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1875` | 36,310.00 USD | 1,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1975` | 632.00 USD | 1,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2105` | 14,200.00 USD | 1,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2165` | 1,520.00 USD | 1,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2185` | 512.82 USD | 1,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2205` | 493.04 USD | 1,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2225` | 232.51 USD | 1,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2245` | 4,570.00 USD | 1,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2265` | 204.76 USD | 1,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2295` | 2,070.00 USD | 1,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2305` | 410.06 USD | 1,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2325` | 2,420.00 USD | 1,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2335` | 553.86 USD | 1,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2345` | 5,700.00 USD | 1,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2355` | 3,130.00 USD | 1,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2365` | 686.56 USD | 1,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2375` | 826.50 USD | 1,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2395` | 151.36 USD | 1,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2425` | 6,760.00 USD | 1,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2435` | 885.85 USD | 1,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2445` | 464.79 USD | 1,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2455` | 384.94 USD | 1,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2475` | 11,840.00 USD | 1,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2505` | 555.61 USD | 993,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2565` | 1,520.00 USD | 993,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2595` | 749.18 USD | 991,670.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2615` | 107.74 USD | 990,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2635` | 4,550.00 USD | 990,820.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2645` | 2,650.00 USD | 986,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2655` | 193.02 USD | 983,610.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2675` | 321.54 USD | 983,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2685` | 3,390.00 USD | 983,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2735` | 220.99 USD | 979,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2745` | 84,470.00 USD | 979,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2785` | 15,180.00 USD | 895,010.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2795` | 6,260.00 USD | 879,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2805` | 13,300.00 USD | 873,580.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2815` | 3,690.00 USD | 860,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2825` | 838.74 USD | 856,590.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2845` | 357.90 USD | 855,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2855` | 6,300.00 USD | 855,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2865` | 4,310.00 USD | 849,100.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2905` | 821.82 USD | 844,780.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2915` | 954.37 USD | 843,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2935` | 213.08 USD | 843,010.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2945` | 124.87 USD | 842,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.2953` | 22,390,000.00 USD | 22,390,000.00 USD | 82,100.00 USD | 0.00 USD | 10,820.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.2955` | 156.61 USD | 842,670.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.2959` | 22,300,000.00 USD | 22,300,000.00 USD | 108,710.00 USD | 22,740.00 USD | 9,700.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.2965` | 22,150,000.00 USD | 22,150,000.00 USD | 123,080.00 USD | 36,820.00 USD | 59,640.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.2965` | 1,010.00 USD | 842,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.2971` | 21,940,000.00 USD | 21,940,000.00 USD | 88,780.00 USD | 34,680.00 USD | 52,660.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.2977` | 15,840,000.00 USD | 15,840,000.00 USD | 13,380.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.2977` | 21,760,000.00 USD | 21,760,000.00 USD | 53,680.00 USD | 18,540.00 USD | 17,670.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.2981` | 15,830,000.00 USD | 15,830,000.00 USD | 12,230.00 USD | 5,290.00 USD | 10,710.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.2983` | 21,670,000.00 USD | 21,670,000.00 USD | 170,240.00 USD | 15,470.00 USD | 39,660.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.2985` | 15,800,000.00 USD | 15,800,000.00 USD | 107,040.00 USD | 10,860.00 USD | 12,860.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.2985` | 759.68 USD | 841,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.2989` | 15,670,000.00 USD | 15,670,000.00 USD | 26,190.00 USD | 0.00 USD | 8,790.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.2989` | 21,440,000.00 USD | 21,440,000.00 USD | 112,680.00 USD | 18,720.00 USD | 23,920.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.2993` | 15,640,000.00 USD | 15,640,000.00 USD | 55,190.00 USD | 33,830.00 USD | 56,800.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.2995` | 21,290,000.00 USD | 21,290,000.00 USD | 10,860.00 USD | 69,130.00 USD | 80,320.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.2995` | 197.37 USD | 840,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.2997` | 15,490,000.00 USD | 15,490,000.00 USD | 600.83 USD | 28,790.00 USD | 46,110.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3001` | 15,420,000.00 USD | 15,420,000.00 USD | 8,760.00 USD | 14,600.00 USD | 14,510.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3001` | 21,130,000.00 USD | 21,130,000.00 USD | 3,960.00 USD | 34,510.00 USD | 93,100.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3005` | 15,380,000.00 USD | 15,380,000.00 USD | 15,600.00 USD | 7,870.00 USD | 18,440.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3005` | 10,620.00 USD | 840,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.3007` | 21,000,000.00 USD | 21,000,000.00 USD | 13,780.00 USD | 2,960.00 USD | 22,100.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3009` | 15,340,000.00 USD | 15,340,000.00 USD | 35,140.00 USD | 8,400.00 USD | 16,090.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3013` | 15,280,000.00 USD | 15,280,000.00 USD | 17,320.00 USD | 3,170.00 USD | 9,220.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3015` | 102.81 USD | 829,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3017` | 15,250,000.00 USD | 15,250,000.00 USD | 1,010.00 USD | 8,490.00 USD | 9,760.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3019` | 20,960,000.00 USD | 20,960,000.00 USD | 0.00 USD | 8,660.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3021` | 15,230,000.00 USD | 15,230,000.00 USD | 14,850.00 USD | 4,540.00 USD | 16,590.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3025` | 15,190,000.00 USD | 15,190,000.00 USD | 2,600.00 USD | 2,050.00 USD | 17,010.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3025` | 20,950,000.00 USD | 20,950,000.00 USD | 0.00 USD | 22,200.00 USD | 55,830.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3025` | 2,510.00 USD | 829,820.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3029` | 15,170,000.00 USD | 15,170,000.00 USD | 24,570.00 USD | 0.00 USD | 6,190.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3031` | 20,870,000.00 USD | 20,870,000.00 USD | 50,940.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3033` | 15,140,000.00 USD | 15,140,000.00 USD | 1,070.00 USD | 8,320.00 USD | 12,600.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3035` | 4,040.00 USD | 827,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3037` | 15,120,000.00 USD | 15,120,000.00 USD | 517.67 USD | 3,230.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3037` | 20,820,000.00 USD | 20,820,000.00 USD | 1,880.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3041` | 15,110,000.00 USD | 15,110,000.00 USD | 965.78 USD | 9,300.00 USD | 75,700.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3043` | 20,820,000.00 USD | 20,820,000.00 USD | 2,700.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3045` | 15,030,000.00 USD | 15,030,000.00 USD | 9,150.00 USD | 13,170.00 USD | 7,480.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3045` | 138.24 USD | 823,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3049` | 15,000,000.00 USD | 15,000,000.00 USD | 37,610.00 USD | 11,440.00 USD | 62,400.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3049` | 20,820,000.00 USD | 20,820,000.00 USD | 18,360.00 USD | 0.00 USD | 66,870.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3053` | 14,890,000.00 USD | 14,890,000.00 USD | 46,990.00 USD | 20,580.00 USD | 49,310.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3055` | 20,730,000.00 USD | 20,730,000.00 USD | 1,490.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3055` | 14,670.00 USD | 823,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3061` | 14,770,000.00 USD | 14,770,000.00 USD | 9,630.00 USD | 2,350.00 USD | 56,460.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3061` | 20,730,000.00 USD | 20,730,000.00 USD | 32,930.00 USD | 7,690.00 USD | 37,210.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3065` | 14,700,000.00 USD | 14,700,000.00 USD | 29,570.00 USD | 26,740.00 USD | 35,690.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3065` | 5,900.00 USD | 808,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.3067` | 20,650,000.00 USD | 20,650,000.00 USD | 6,300.00 USD | 8,110.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3069` | 14,610,000.00 USD | 14,610,000.00 USD | 1,540.00 USD | 2,880.00 USD | 12,760.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3073` | 14,590,000.00 USD | 14,590,000.00 USD | 23,280.00 USD | 1,940.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3073` | 20,640,000.00 USD | 20,640,000.00 USD | 7,990.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3075` | 722.62 USD | 802,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3077` | 14,570,000.00 USD | 14,570,000.00 USD | 350.20 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3079` | 20,630,000.00 USD | 20,630,000.00 USD | 37,350.00 USD | 10,270.00 USD | 50,200.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3081` | 14,570,000.00 USD | 14,570,000.00 USD | 18,400.00 USD | 0.00 USD | 12,250.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3085` | 14,540,000.00 USD | 14,540,000.00 USD | 340.09 USD | 0.00 USD | 15,810.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3085` | 20,530,000.00 USD | 20,530,000.00 USD | 3,660.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3085` | 291.53 USD | 801,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3089` | 14,520,000.00 USD | 14,520,000.00 USD | 550.01 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3091` | 20,530,000.00 USD | 20,530,000.00 USD | 7,040.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3093` | 14,520,000.00 USD | 14,520,000.00 USD | 14,750.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3095` | 192.51 USD | 801,540.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3097` | 14,500,000.00 USD | 14,500,000.00 USD | 7,620.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3097` | 20,520,000.00 USD | 20,520,000.00 USD | 79,880.00 USD | 3,620.00 USD | 54,360.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3101` | 14,500,000.00 USD | 14,500,000.00 USD | 41,340.00 USD | 15,820.00 USD | 46,470.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3103` | 20,380,000.00 USD | 20,380,000.00 USD | 67,180.00 USD | 0.00 USD | 63,310.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3105` | 14,390,000.00 USD | 14,390,000.00 USD | 21,200.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3105` | 820.96 USD | 801,350.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.3109` | 20,250,000.00 USD | 20,250,000.00 USD | 19,040.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3113` | 14,370,000.00 USD | 14,370,000.00 USD | 0.00 USD | 4,980.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3115` | 20,230,000.00 USD | 20,230,000.00 USD | 10,250.00 USD | 0.00 USD | 37,490.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3115` | 13,600.00 USD | 800,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3117` | 14,370,000.00 USD | 14,370,000.00 USD | 15,480.00 USD | 12,220.00 USD | 17,620.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3121` | 14,320,000.00 USD | 14,320,000.00 USD | 11,560.00 USD | 2,560.00 USD | 33,830.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3121` | 20,180,000.00 USD | 20,180,000.00 USD | 162,320.00 USD | 19,620.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3125` | 14,270,000.00 USD | 14,270,000.00 USD | 12,740.00 USD | 13,530.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3125` | 17,810.00 USD | 786,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.3127` | 20,000,000.00 USD | 20,000,000.00 USD | 12,250.00 USD | 54,460.00 USD | 57,690.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3129` | 14,250,000.00 USD | 14,250,000.00 USD | 3,990.00 USD | 28,470.00 USD | 29,100.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3133` | 14,190,000.00 USD | 14,190,000.00 USD | 4,020.00 USD | 23,940.00 USD | 9,590.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3133` | 19,880,000.00 USD | 19,880,000.00 USD | 4,440.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3135` | 446.11 USD | 769,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3137` | 14,150,000.00 USD | 14,150,000.00 USD | 4,590.00 USD | 10,610.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3139` | 19,870,000.00 USD | 19,870,000.00 USD | 3,330.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3141` | 14,130,000.00 USD | 14,130,000.00 USD | 6,900.00 USD | 0.00 USD | 9,540.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3145` | 14,120,000.00 USD | 14,120,000.00 USD | 1,910.00 USD | 5,900.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3145` | 19,870,000.00 USD | 19,870,000.00 USD | 247,920.00 USD | 51,270.00 USD | 17,870.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3145` | 577.11 USD | 768,680.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3149` | 14,110,000.00 USD | 14,110,000.00 USD | 1,570.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3151` | 19,550,000.00 USD | 19,550,000.00 USD | 204,770.00 USD | 23,130.00 USD | 49,320.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3153` | 14,110,000.00 USD | 14,110,000.00 USD | 29,750.00 USD | 25,600.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3155` | 11,510.00 USD | 768,100.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3157` | 14,050,000.00 USD | 14,050,000.00 USD | 12,120.00 USD | 1,830.00 USD | 16,240.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3157` | 19,280,000.00 USD | 19,280,000.00 USD | 393,880.00 USD | 93,740.00 USD | 60,300.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3161` | 14,020,000.00 USD | 14,020,000.00 USD | 4,260.00 USD | 2,990.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3163` | 18,730,000.00 USD | 18,730,000.00 USD | 495,020.00 USD | 174,600.00 USD | 189,520.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3165` | 14,010,000.00 USD | 14,010,000.00 USD | 45,260.00 USD | 30,980.00 USD | 9,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3165` | 935.89 USD | 756,590.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3169` | 13,930,000.00 USD | 13,930,000.00 USD | 1,090.00 USD | 10,820.00 USD | 20,780.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3169` | 17,870,000.00 USD | 17,870,000.00 USD | 417,170.00 USD | 104,590.00 USD | 135,950.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3173` | 13,900,000.00 USD | 13,900,000.00 USD | 25,580.00 USD | 33,870.00 USD | 27,630.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3175` | 17,210,000.00 USD | 17,210,000.00 USD | 140,810.00 USD | 53,470.00 USD | 69,280.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3175` | 2,290.00 USD | 755,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3177` | 13,810,000.00 USD | 13,810,000.00 USD | 47,770.00 USD | 8,980.00 USD | 30,890.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3181` | 13,720,000.00 USD | 13,720,000.00 USD | 260,170.00 USD | 41,280.00 USD | 69,790.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3181` | 16,950,000.00 USD | 16,950,000.00 USD | 738,240.00 USD | 76,910.00 USD | 182,330.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3185` | 13,350,000.00 USD | 13,350,000.00 USD | 153,950.00 USD | 52,920.00 USD | 51,330.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3185` | 1,300.00 USD | 753,370.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.3187` | 15,950,000.00 USD | 15,950,000.00 USD | 407,530.00 USD | 97,820.00 USD | 24,770.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3189` | 13,090,000.00 USD | 13,090,000.00 USD | 172,980.00 USD | 5,580.00 USD | 48,660.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3193` | 12,860,000.00 USD | 12,860,000.00 USD | 154,490.00 USD | 107,560.00 USD | 180,830.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3193` | 15,420,000.00 USD | 15,420,000.00 USD | 180,550.00 USD | 123,840.00 USD | 247,300.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3197` | 12,420,000.00 USD | 12,420,000.00 USD | 74,370.00 USD | 118,340.00 USD | 160,310.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3199` | 14,870,000.00 USD | 14,870,000.00 USD | 0.00 USD | 191,160.00 USD | 267,030.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3201` | 12,070,000.00 USD | 12,070,000.00 USD | 208,440.00 USD | 48,100.00 USD | 111,260.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3205` | 11,700,000.00 USD | 11,700,000.00 USD | 163,900.00 USD | 31,270.00 USD | 102,160.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3205` | 14,410,000.00 USD | 14,410,000.00 USD | 167,490.00 USD | 59,200.00 USD | 130,760.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3205` | 2,930.00 USD | 752,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3209` | 11,400,000.00 USD | 11,400,000.00 USD | 88,570.00 USD | 29,040.00 USD | 54,070.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3211` | 14,050,000.00 USD | 14,050,000.00 USD | 568,110.00 USD | 135,070.00 USD | 244,340.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3213` | 11,230,000.00 USD | 11,230,000.00 USD | 54,680.00 USD | 30,340.00 USD | 107,830.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3217` | 11,040,000.00 USD | 11,040,000.00 USD | 5,980.00 USD | 33,860.00 USD | 146,990.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3217` | 13,110,000.00 USD | 13,110,000.00 USD | 285,190.00 USD | 58,690.00 USD | 107,900.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3221` | 10,850,000.00 USD | 10,850,000.00 USD | 97,900.00 USD | 33,430.00 USD | 72,520.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3223` | 12,650,000.00 USD | 12,650,000.00 USD | 643,460.00 USD | 265,170.00 USD | 156,030.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3225` | 10,650,000.00 USD | 10,650,000.00 USD | 70,750.00 USD | 33,350.00 USD | 202,490.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3229` | 10,340,000.00 USD | 10,340,000.00 USD | 91,010.00 USD | 55,060.00 USD | 129,350.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3229` | 11,590,000.00 USD | 11,590,000.00 USD | 858,070.00 USD | 283,650.00 USD | 518,610.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3233` | 10,070,000.00 USD | 10,070,000.00 USD | 56,470.00 USD | 35,600.00 USD | 49,900.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3235` | 9,930,000.00 USD | 9,930,000.00 USD | 709,160.00 USD | 228,450.00 USD | 359,100.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3235` | 128.43 USD | 749,140.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3237` | 9,920,000.00 USD | 9,920,000.00 USD | 6,420.00 USD | 83,630.00 USD | 171,270.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3241` | 9,660,000.00 USD | 9,660,000.00 USD | 966.93 USD | 27,720.00 USD | 119,400.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3241` | 8,630,000.00 USD | 8,630,000.00 USD | 432,660.00 USD | 149,860.00 USD | 138,560.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3245` | 9,520,000.00 USD | 9,520,000.00 USD | 256,740.00 USD | 54,650.00 USD | 265,030.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3247` | 7,910,000.00 USD | 7,910,000.00 USD | 846,180.00 USD | 127,310.00 USD | 353,590.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3249` | 8,940,000.00 USD | 8,940,000.00 USD | 818,640.00 USD | 91,640.00 USD | 179,470.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3253` | 7,850,000.00 USD | 7,850,000.00 USD | 217,740.00 USD | 107,140.00 USD | 423,830.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3253` | 6,580,000.00 USD | 6,580,000.00 USD | 1,220,000.00 USD | 137,440.00 USD | 241,690.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3255` | 3,580.00 USD | 749,010.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3257` | 7,100,000.00 USD | 7,100,000.00 USD | 542,240.00 USD | 48,220.00 USD | 229,640.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3259` | 4,980,000.00 USD | 4,980,000.00 USD | 306,910.00 USD | 288,370.00 USD | 503,650.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3261` | 6,280,000.00 USD | 6,280,000.00 USD | 150,120.00 USD | 371,060.00 USD | 555,160.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3265` | 5,200,000.00 USD | 5,200,000.00 USD | 65,640.00 USD | 156,570.00 USD | 345,910.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3265` | 3,880,000.00 USD | 3,880,000.00 USD | 80,120.00 USD | 324,810.00 USD | 500,270.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3269` | 4,640,000.00 USD | 4,640,000.00 USD | 200,120.00 USD | 143,860.00 USD | 378,850.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3271` | 2,980,000.00 USD | 2,980,000.00 USD | 320,700.00 USD | 138,680.00 USD | 261,530.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3273` | 3,910,000.00 USD | 3,910,000.00 USD | 38,550.00 USD | 24,720.00 USD | 174,670.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3275` | 163.42 USD | 745,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3277` | 3,680,000.00 USD | 3,680,000.00 USD | 317,170.00 USD | 71,740.00 USD | 161,500.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3277` | 2,260,000.00 USD | 2,260,000.00 USD | 0.00 USD | 29,390.00 USD | 85,620.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3281` | 3,120,000.00 USD | 3,120,000.00 USD | 106,720.00 USD | 57,800.00 USD | 120,850.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3283` | 2,140,000.00 USD | 2,140,000.00 USD | 89,030.00 USD | 61,340.00 USD | 275,050.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3285` | 2,840,000.00 USD | 2,840,000.00 USD | 0.00 USD | 48,460.00 USD | 79,430.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3285` | 745,260.00 USD | 745,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3289` | 2,710,000.00 USD | 2,710,000.00 USD | 155,850.00 USD | 21,810.00 USD | 155,080.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3289` | 1,720,000.00 USD | 1,720,000.00 USD | 0.00 USD | 180,260.00 USD | 105,320.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3293` | 2,380,000.00 USD | 2,380,000.00 USD | 977.29 USD | 60,450.00 USD | 165,140.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3295` | 1,430,000.00 USD | 1,430,000.00 USD | 254,700.00 USD | 83,080.00 USD | 279,140.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3297` | 2,150,000.00 USD | 2,150,000.00 USD | 166,310.00 USD | 18,090.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3301` | 1,970,000.00 USD | 1,970,000.00 USD | 36,460.00 USD | 58,700.00 USD | 30,950.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3301` | 815,180.00 USD | 815,180.00 USD | 185,020.00 USD | 47,610.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3305` | 1,840,000.00 USD | 1,840,000.00 USD | 112,020.00 USD | 33,940.00 USD | 74,690.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3307` | 582,550.00 USD | 582,550.00 USD | 167,950.00 USD | 10,690.00 USD | 294,170.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3309` | 1,620,000.00 USD | 1,620,000.00 USD | 11,600.00 USD | 48,170.00 USD | 444,920.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3313` | 1,120,000.00 USD | 1,120,000.00 USD | 61,660.00 USD | 128,440.00 USD | 183,340.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3313` | 109,740.00 USD | 109,740.00 USD | 0.00 USD | 50,650.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3317` | 742,760.00 USD | 742,760.00 USD | 27,700.00 USD | 58,950.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3319` | 59,090.00 USD | 59,090.00 USD | 0.00 USD | 57,890.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3321` | 656,110.00 USD | 656,110.00 USD | 18,060.00 USD | 23,430.00 USD | 100,730.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3325` | 513,880.00 USD | 513,880.00 USD | 0.00 USD | 9,670.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3329` | 504,220.00 USD | 504,220.00 USD | 17,980.00 USD | 0.00 USD | 39,970.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3333` | 446,260.00 USD | 446,260.00 USD | 43,710.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3361` | 1,200.00 USD | 1,200.00 USD | 1,200.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3369` | 402,560.00 USD | 402,560.00 USD | 72,920.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3377` | 329,640.00 USD | 329,640.00 USD | 329,640.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3385` | 125,650.00 USD | 125,650.00 USD | 125,650.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3391` | 484,990.00 USD | 484,990.00 USD | 124,670.00 USD | 0.00 USD | 234,660.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3397` | 1,910,000.00 USD | 1,910,000.00 USD | 257,550.00 USD | 752,550.00 USD | 410,830.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3401` | 220,570.00 USD | 220,570.00 USD | 0.00 USD | 15,510.00 USD | 205,050.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3403` | 3,580,000.00 USD | 3,580,000.00 USD | 1,200,000.00 USD | 103,630.00 USD | 376,470.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3405` | 554,610.00 USD | 554,610.00 USD | 0.00 USD | 14,270.00 USD | 319,770.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3409` | 800,040.00 USD | 800,040.00 USD | 183,630.00 USD | 34,110.00 USD | 27,700.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3409` | 4,060,000.00 USD | 4,060,000.00 USD | 0.00 USD | 29,390.00 USD | 446,990.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3413` | 1,170,000.00 USD | 1,170,000.00 USD | 279,850.00 USD | 11,360.00 USD | 80,830.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3415` | 4,180,000.00 USD | 4,180,000.00 USD | 0.00 USD | 35,670.00 USD | 85,620.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3417` | 1,980,000.00 USD | 1,980,000.00 USD | 585,390.00 USD | 25,060.00 USD | 197,540.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3421` | 2,090,000.00 USD | 2,090,000.00 USD | 71,180.00 USD | 39,260.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3421` | 4,220,000.00 USD | 4,220,000.00 USD | 0.00 USD | 43,290.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3425` | 2,250,000.00 USD | 2,250,000.00 USD | 0.00 USD | 159,430.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3427` | 4,840,000.00 USD | 4,840,000.00 USD | 0.00 USD | 229,350.00 USD | 384,460.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3429` | 2,520,000.00 USD | 2,520,000.00 USD | 60,980.00 USD | 120,450.00 USD | 85,070.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3433` | 2,820,000.00 USD | 2,820,000.00 USD | 105,330.00 USD | 167,240.00 USD | 30,950.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3433` | 5,130,000.00 USD | 5,130,000.00 USD | 254,700.00 USD | 38,560.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3437` | 3,000,000.00 USD | 3,000,000.00 USD | 0.00 USD | 117,260.00 USD | 62,980.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3441` | 3,050,000.00 USD | 3,050,000.00 USD | 0.00 USD | 45,070.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3445` | 3,180,000.00 USD | 3,180,000.00 USD | 0.00 USD | 28,520.00 USD | 106,240.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3445` | 5,230,000.00 USD | 5,230,000.00 USD | 103,130.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3445` | 2,280.00 USD | 2,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.3449` | 3,550,000.00 USD | 3,550,000.00 USD | 97,620.00 USD | 92,440.00 USD | 183,340.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3451` | 5,320,000.00 USD | 5,320,000.00 USD | 62,830.00 USD | 28,550.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3453` | 3,820,000.00 USD | 3,820,000.00 USD | 130,670.00 USD | 47,460.00 USD | 84,370.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3457` | 4,600,000.00 USD | 4,600,000.00 USD | 170,670.00 USD | 57,370.00 USD | 553,330.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3457` | 5,750,000.00 USD | 5,750,000.00 USD | 62,340.00 USD | 29,340.00 USD | 332,190.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3461` | 5,230,000.00 USD | 5,230,000.00 USD | 198,910.00 USD | 190,690.00 USD | 242,890.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3463` | 6,200,000.00 USD | 6,200,000.00 USD | 0.00 USD | 250,840.00 USD | 205,410.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3465` | 5,480,000.00 USD | 5,480,000.00 USD | 39,870.00 USD | 67,330.00 USD | 142,350.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3469` | 5,680,000.00 USD | 5,680,000.00 USD | 81,330.00 USD | 42,550.00 USD | 75,450.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3469` | 6,530,000.00 USD | 6,530,000.00 USD | 124,720.00 USD | 51,820.00 USD | 152,060.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3473` | 5,740,000.00 USD | 5,740,000.00 USD | 0.00 USD | 35,130.00 USD | 31,160.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3475` | 6,570,000.00 USD | 6,570,000.00 USD | 0.00 USD | 40,540.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3477` | 5,920,000.00 USD | 5,920,000.00 USD | 51,860.00 USD | 48,500.00 USD | 77,670.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3481` | 6,070,000.00 USD | 6,070,000.00 USD | 53,360.00 USD | 29,570.00 USD | 64,980.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3481` | 6,660,000.00 USD | 6,660,000.00 USD | 6,440.00 USD | 32,530.00 USD | 42,810.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3485` | 6,170,000.00 USD | 6,170,000.00 USD | 9,350.00 USD | 16,180.00 USD | 76,450.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3487` | 6,690,000.00 USD | 6,690,000.00 USD | 8,310.00 USD | 21,650.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3489` | 6,300,000.00 USD | 6,300,000.00 USD | 41,500.00 USD | 23,850.00 USD | 61,240.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3493` | 6,340,000.00 USD | 6,340,000.00 USD | 3,620.00 USD | 33,350.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3493` | 6,980,000.00 USD | 6,980,000.00 USD | 10,490.00 USD | 93,150.00 USD | 192,230.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3497` | 6,870,000.00 USD | 6,870,000.00 USD | 32,290.00 USD | 0.00 USD | 497,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3499` | 7,120,000.00 USD | 7,120,000.00 USD | 139,880.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3501` | 6,980,000.00 USD | 6,980,000.00 USD | 52,670.00 USD | 9,040.00 USD | 50,760.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3505` | 7,120,000.00 USD | 7,120,000.00 USD | 74,220.00 USD | 33,830.00 USD | 31,490.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3505` | 7,150,000.00 USD | 7,150,000.00 USD | 11,960.00 USD | 19,280.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3505` | 8,650.00 USD | 10,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.3509` | 7,140,000.00 USD | 7,140,000.00 USD | 2,790.00 USD | 16,810.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3511` | 8,110,000.00 USD | 8,110,000.00 USD | 690,500.00 USD | 0.00 USD | 271,800.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3513` | 7,210,000.00 USD | 7,210,000.00 USD | 0.00 USD | 0.00 USD | 76,540.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3515` | 175.05 USD | 11,110.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.3517` | 7,370,000.00 USD | 7,370,000.00 USD | 52,740.00 USD | 5,720.00 USD | 101,300.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3521` | 7,510,000.00 USD | 7,510,000.00 USD | 47,300.00 USD | 21,980.00 USD | 69,070.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3523` | 8,530,000.00 USD | 8,530,000.00 USD | 277,410.00 USD | 28,950.00 USD | 107,430.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3525` | 7,570,000.00 USD | 7,570,000.00 USD | 13,010.00 USD | 17,990.00 USD | 28,910.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3525` | 112.45 USD | 11,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.3529` | 7,730,000.00 USD | 7,730,000.00 USD | 102,610.00 USD | 57,540.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3533` | 7,960,000.00 USD | 7,960,000.00 USD | 76,080.00 USD | 44,040.00 USD | 108,090.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3535` | 8,800,000.00 USD | 8,800,000.00 USD | 4,830.00 USD | 77,960.00 USD | 187,450.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3537` | 8,270,000.00 USD | 8,270,000.00 USD | 83,280.00 USD | 29,120.00 USD | 195,270.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3541` | 8,430,000.00 USD | 8,430,000.00 USD | 83,770.00 USD | 80,430.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3541` | 9,730,000.00 USD | 9,730,000.00 USD | 810,900.00 USD | 118,370.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3545` | 8,550,000.00 USD | 8,550,000.00 USD | 5,220.00 USD | 44,140.00 USD | 69,820.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3545` | 29,460.00 USD | 40,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.3547` | 10,020,000.00 USD | 10,020,000.00 USD | 5,390.00 USD | 0.00 USD | 288,450.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3549` | 8,610,000.00 USD | 8,610,000.00 USD | 6,350.00 USD | 53,970.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3553` | 8,710,000.00 USD | 8,710,000.00 USD | 21,530.00 USD | 24,430.00 USD | 47,950.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3553` | 10,150,000.00 USD | 10,150,000.00 USD | 12,710.00 USD | 117,050.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3557` | 8,750,000.00 USD | 8,750,000.00 USD | 853.70 USD | 38,770.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3559` | 10,170,000.00 USD | 10,170,000.00 USD | 13,500.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3561` | 8,880,000.00 USD | 8,880,000.00 USD | 331.60 USD | 25,000.00 USD | 106,140.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3565` | 8,930,000.00 USD | 8,930,000.00 USD | 3,070.00 USD | 11,630.00 USD | 39,520.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3565` | 10,210,000.00 USD | 10,210,000.00 USD | 0.00 USD | 43,060.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3569` | 8,940,000.00 USD | 8,940,000.00 USD | 1,450.00 USD | 6,920.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3573` | 9,080,000.00 USD | 9,080,000.00 USD | 131,970.00 USD | 9,250.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3577` | 9,120,000.00 USD | 9,120,000.00 USD | 31,960.00 USD | 9,130.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3577` | 10,330,000.00 USD | 10,330,000.00 USD | 124,630.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3581` | 9,160,000.00 USD | 9,160,000.00 USD | 3,560.00 USD | 0.00 USD | 38,950.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3583` | 10,470,000.00 USD | 10,470,000.00 USD | 0.00 USD | 0.00 USD | 135,900.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3585` | 9,200,000.00 USD | 9,200,000.00 USD | 18,570.00 USD | 14,930.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3589` | 9,220,000.00 USD | 9,220,000.00 USD | 3,780.00 USD | 15,750.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3589` | 10,840,000.00 USD | 10,840,000.00 USD | 0.00 USD | 50,650.00 USD | 320,430.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3593` | 9,420,000.00 USD | 9,420,000.00 USD | 66,040.00 USD | 0.00 USD | 133,180.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3595` | 10,990,000.00 USD | 10,990,000.00 USD | 0.00 USD | 0.00 USD | 146,290.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3597` | 9,520,000.00 USD | 9,520,000.00 USD | 91,900.00 USD | 12,460.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3601` | 9,720,000.00 USD | 9,720,000.00 USD | 1,360.00 USD | 36,520.00 USD | 163,110.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3601` | 11,490,000.00 USD | 11,490,000.00 USD | 4,230.00 USD | 161,200.00 USD | 338,540.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3605` | 9,910,000.00 USD | 9,910,000.00 USD | 61,580.00 USD | 32,860.00 USD | 94,650.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3607` | 11,890,000.00 USD | 11,890,000.00 USD | 330,010.00 USD | 68,030.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3609` | 10,150,000.00 USD | 10,150,000.00 USD | 75,390.00 USD | 25,740.00 USD | 133,760.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3613` | 10,420,000.00 USD | 10,420,000.00 USD | 11,270.00 USD | 59,640.00 USD | 203,600.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3613` | 12,580,000.00 USD | 12,580,000.00 USD | 73,920.00 USD | 330,040.00 USD | 288,930.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3617` | 10,800,000.00 USD | 10,800,000.00 USD | 225,910.00 USD | 50,630.00 USD | 104,310.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3619` | 12,790,000.00 USD | 12,790,000.00 USD | 3,790.00 USD | 209,940.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3621` | 11,090,000.00 USD | 11,090,000.00 USD | 143,010.00 USD | 75,820.00 USD | 71,510.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3625` | 11,240,000.00 USD | 11,240,000.00 USD | 99,950.00 USD | 49,330.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3625` | 12,990,000.00 USD | 12,990,000.00 USD | 2,300.00 USD | 191,880.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3629` | 12,470,000.00 USD | 12,470,000.00 USD | 1,120,000.00 USD | 35,410.00 USD | 79,610.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3631` | 13,100,000.00 USD | 13,100,000.00 USD | 738.08 USD | 114,740.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3633` | 12,890,000.00 USD | 12,890,000.00 USD | 144,090.00 USD | 72,670.00 USD | 199,780.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3635` | 12,360.00 USD | 53,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.3637` | 13,140,000.00 USD | 13,140,000.00 USD | 183,690.00 USD | 65,110.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3637` | 13,130,000.00 USD | 13,130,000.00 USD | 1,090.00 USD | 21,530.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3641` | 13,510,000.00 USD | 13,510,000.00 USD | 85,150.00 USD | 206,820.00 USD | 76,240.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3643` | 13,920,000.00 USD | 13,920,000.00 USD | 1,580.00 USD | 0.00 USD | 789,140.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3645` | 13,820,000.00 USD | 13,820,000.00 USD | 255,500.00 USD | 16,650.00 USD | 35,280.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3649` | 14,170,000.00 USD | 14,170,000.00 USD | 96,700.00 USD | 59,680.00 USD | 195,820.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3649` | 14,100,000.00 USD | 14,100,000.00 USD | 182,150.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3653` | 14,660,000.00 USD | 14,660,000.00 USD | 303,010.00 USD | 19,500.00 USD | 165,330.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3655` | 14,890,000.00 USD | 14,890,000.00 USD | 677,860.00 USD | 112,770.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3657` | 15,190,000.00 USD | 15,190,000.00 USD | 218,660.00 USD | 149,310.00 USD | 163,370.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3661` | 15,650,000.00 USD | 15,650,000.00 USD | 277,650.00 USD | 88,330.00 USD | 96,250.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3661` | 15,890,000.00 USD | 15,890,000.00 USD | 691,690.00 USD | 66,940.00 USD | 238,480.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3665` | 16,300,000.00 USD | 16,300,000.00 USD | 468,570.00 USD | 117,940.00 USD | 66,840.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3665` | 3,110.00 USD | 56,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.3667` | 16,510,000.00 USD | 16,510,000.00 USD | 424,170.00 USD | 34,510.00 USD | 166,250.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3669` | 16,710,000.00 USD | 16,710,000.00 USD | 98,960.00 USD | 26,330.00 USD | 281,260.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3673` | 17,020,000.00 USD | 17,020,000.00 USD | 52,240.00 USD | 102,840.00 USD | 158,510.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3673` | 17,200,000.00 USD | 17,200,000.00 USD | 511,100.00 USD | 53,040.00 USD | 122,410.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3677` | 17,750,000.00 USD | 17,750,000.00 USD | 494,570.00 USD | 41,730.00 USD | 191,130.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3679` | 17,460,000.00 USD | 17,460,000.00 USD | 259,090.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3681` | 18,250,000.00 USD | 18,250,000.00 USD | 310,830.00 USD | 87,330.00 USD | 103,470.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3685` | 18,820,000.00 USD | 18,820,000.00 USD | 327,450.00 USD | 152,380.00 USD | 93,220.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3685` | 17,640,000.00 USD | 17,640,000.00 USD | 1,610.00 USD | 102,650.00 USD | 72,350.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3689` | 19,340,000.00 USD | 19,340,000.00 USD | 404,300.00 USD | 56,330.00 USD | 52,150.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3691` | 18,040,000.00 USD | 18,040,000.00 USD | 147,650.00 USD | 261,530.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3693` | 19,450,000.00 USD | 19,450,000.00 USD | 79,910.00 USD | 4,540.00 USD | 23,760.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3697` | 19,700,000.00 USD | 19,700,000.00 USD | 155,550.00 USD | 83,650.00 USD | 17,010.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3697` | 18,280,000.00 USD | 18,280,000.00 USD | 0.00 USD | 175,510.00 USD | 55,830.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3701` | 20,450,000.00 USD | 20,450,000.00 USD | 527,250.00 USD | 196,170.00 USD | 27,870.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3703` | 18,330,000.00 USD | 18,330,000.00 USD | 50,940.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3705` | 21,270,000.00 USD | 21,270,000.00 USD | 249,050.00 USD | 8,320.00 USD | 560,920.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3705` | 278.99 USD | 56,440.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.3709` | 21,420,000.00 USD | 21,420,000.00 USD | 109,790.00 USD | 24,570.00 USD | 12,600.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3709` | 18,330,000.00 USD | 18,330,000.00 USD | 1,880.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3713` | 22,790,000.00 USD | 22,790,000.00 USD | 482,060.00 USD | 90,010.00 USD | 804,260.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3715` | 18,730,000.00 USD | 18,730,000.00 USD | 3,890.00 USD | 0.00 USD | 394,570.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3717` | 23,330,000.00 USD | 23,330,000.00 USD | 44,820.00 USD | 220,760.00 USD | 269,700.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3721` | 23,490,000.00 USD | 23,490,000.00 USD | 9,150.00 USD | 62,750.00 USD | 85,090.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3721` | 19,480,000.00 USD | 19,480,000.00 USD | 1,320.00 USD | 0.00 USD | 747,740.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3725` | 24,570,000.00 USD | 24,570,000.00 USD | 511,460.00 USD | 31,730.00 USD | 537,700.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3725` | 186.25 USD | 56,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.3727` | 19,760,000.00 USD | 19,760,000.00 USD | 213,190.00 USD | 0.00 USD | 66,870.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3729` | 25,080,000.00 USD | 25,080,000.00 USD | 33,900.00 USD | 128,180.00 USD | 349,570.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3733` | 25,860,000.00 USD | 25,860,000.00 USD | 105,050.00 USD | 23,870.00 USD | 655,100.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3733` | 19,940,000.00 USD | 19,940,000.00 USD | 188,670.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3735` | 7,070.00 USD | 63,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.3737` | 26,110,000.00 USD | 26,110,000.00 USD | 154,860.00 USD | 94,700.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3739` | 20,420,000.00 USD | 20,420,000.00 USD | 247,740.00 USD | 7,690.00 USD | 218,010.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3741` | 26,630,000.00 USD | 26,630,000.00 USD | 41,360.00 USD | 71,420.00 USD | 403,580.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3745` | 27,000,000.00 USD | 27,000,000.00 USD | 30,710.00 USD | 35,840.00 USD | 305,620.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3745` | 20,820,000.00 USD | 20,820,000.00 USD | 249,860.00 USD | 115,430.00 USD | 37,210.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3749` | 27,770,000.00 USD | 27,770,000.00 USD | 229,090.00 USD | 20,770.00 USD | 520,920.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3753` | 27,940,000.00 USD | 27,940,000.00 USD | 134,010.00 USD | 0.00 USD | 31,010.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3755` | 4,030.00 USD | 67,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.3756` | 27,960,000.00 USD | 27,960,000.00 USD | 23,190.00 USD | 1,940.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3757` | 21,120,000.00 USD | 21,120,000.00 USD | 0.00 USD | 0.00 USD | 302,240.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3763` | 21,300,000.00 USD | 21,300,000.00 USD | 35,610.00 USD | 92,380.00 USD | 50,200.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3775` | 21,300,000.00 USD | 21,300,000.00 USD | 897.53 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3775` | 104.19 USD | 67,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.3781` | 21,330,000.00 USD | 21,330,000.00 USD | 23,800.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3785` | 556,430.00 USD | 624,250.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.3787` | 21,470,000.00 USD | 21,470,000.00 USD | 89,270.00 USD | 3,620.00 USD | 54,360.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3793` | 21,940,000.00 USD | 21,940,000.00 USD | 27,760.00 USD | 0.00 USD | 437,170.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3795` | 773.04 USD | 625,030.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.3799` | 21,940,000.00 USD | 21,940,000.00 USD | 4,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3805` | 3,390.00 USD | 628,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.3811` | 21,980,000.00 USD | 21,980,000.00 USD | 0.00 USD | 0.00 USD | 37,490.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3817` | 22,160,000.00 USD | 22,160,000.00 USD | 156,690.00 USD | 19,620.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3823` | 22,270,000.00 USD | 22,270,000.00 USD | 0.00 USD | 54,460.00 USD | 57,690.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3835` | 22,270,000.00 USD | 22,270,000.00 USD | 880.35 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3835` | 115.05 USD | 628,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.3853` | 22,270,000.00 USD | 22,270,000.00 USD | 768.95 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3855` | 264.84 USD | 628,800.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.3859` | 22,340,000.00 USD | 22,340,000.00 USD | 71,390.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3865` | 22,500,000.00 USD | 22,500,000.00 USD | 112,700.00 USD | 45,110.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3865` | 1,550,000.00 USD | 2,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.3877` | 22,620,000.00 USD | 22,620,000.00 USD | 123,270.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3883` | 22,670,000.00 USD | 22,670,000.00 USD | 0.00 USD | 0.00 USD | 48,960.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3889` | 22,770,000.00 USD | 22,770,000.00 USD | 103,020.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3895` | 22,810,000.00 USD | 22,810,000.00 USD | 0.00 USD | 41,060.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3895` | 4,760.00 USD | 2,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.3901` | 22,870,000.00 USD | 22,870,000.00 USD | 59,060.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3905` | 6,000.00 USD | 2,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.3907` | 22,990,000.00 USD | 22,990,000.00 USD | 0.00 USD | 50,210.00 USD | 63,420.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3919` | 22,990,000.00 USD | 22,990,000.00 USD | 2,670.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3925` | 23,150,000.00 USD | 23,150,000.00 USD | 447.70 USD | 1,190.00 USD | 157,830.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3931` | 23,180,000.00 USD | 23,180,000.00 USD | 24,750.00 USD | 2,840.00 USD | 2,800.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3935` | 1,480.00 USD | 2,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.3937` | 23,210,000.00 USD | 23,210,000.00 USD | 22,020.00 USD | 1,070.00 USD | 5,410.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3943` | 23,240,000.00 USD | 23,240,000.00 USD | 24,650.00 USD | 3,090.00 USD | 784.19 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3945` | 118,130.00 USD | 2,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.3949` | 23,370,000.00 USD | 23,370,000.00 USD | 110,030.00 USD | 8,290.00 USD | 18,490.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3955` | 23,600,000.00 USD | 23,600,000.00 USD | 107,070.00 USD | 8,610.00 USD | 110,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3961` | 23,780,000.00 USD | 23,780,000.00 USD | 122,560.00 USD | 54,030.00 USD | 7,040.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3967` | 23,810,000.00 USD | 23,810,000.00 USD | 12,400.00 USD | 6,010.00 USD | 4,840.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3973` | 23,950,000.00 USD | 23,950,000.00 USD | 16,600.00 USD | 1,440.00 USD | 123,860.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3979` | 24,060,000.00 USD | 24,060,000.00 USD | 57,520.00 USD | 38,460.00 USD | 11,500.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3985` | 24,090,000.00 USD | 24,090,000.00 USD | 23,360.00 USD | 3,160.00 USD | 10,200.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3991` | 24,130,000.00 USD | 24,130,000.00 USD | 0.00 USD | 16,880.00 USD | 24,490.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3997` | 24,160,000.00 USD | 24,160,000.00 USD | 0.00 USD | 27,240.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.4001` | 24,170,000.00 USD | 24,170,000.00 USD | 0.00 USD | 7,690.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.4015` | 327.62 USD | 2,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4085` | 170.75 USD | 2,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4095` | 239.56 USD | 2,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4145` | 12,440.00 USD | 2,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4165` | 94,510.00 USD | 2,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4185` | 998.96 USD | 2,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4235` | 134.25 USD | 2,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4245` | 3,930.00 USD | 2,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4335` | 1,500.00 USD | 2,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4355` | 70,890.00 USD | 2,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4365` | 1,490.00 USD | 2,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4415` | 377.48 USD | 2,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4425` | 13,280.00 USD | 2,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4435` | 3,460.00 USD | 2,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4445` | 22,200.00 USD | 2,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4455` | 1,020.00 USD | 2,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4465` | 5,520.00 USD | 2,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4475` | 65,610.00 USD | 2,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4675` | 270.22 USD | 2,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4895` | 839.49 USD | 2,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4905` | 5,120.00 USD | 2,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4995` | 2,730.00 USD | 2,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.5005` | 23,320.00 USD | 2,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.5325` | 667.22 USD | 2,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.5355` | 1,170.00 USD | 2,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.5475` | 40,520.00 USD | 2,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.5575` | 3,060.00 USD | 2,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.5605` | 140.12 USD | 2,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.5765` | 747,860.00 USD | 3,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.5855` | 115.93 USD | 3,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.5935` | 4,900.00 USD | 3,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.6155` | 24,620.00 USD | 3,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.6265` | 379.03 USD | 3,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.6335` | 6,810.00 USD | 3,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.6505` | 102,000.00 USD | 3,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.6515` | 951.19 USD | 3,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.6545` | 706.21 USD | 3,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.6615` | 2,060.00 USD | 3,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.6635` | 3,740.00 USD | 3,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `0.0785` | 1,250,000.00 USD | 0.00 USD | 6,930.00 USD | `-76.58%` | `88,233.00` |
| `Live` | `Long` | `0.0795` | 1,240,000.00 USD | 0.00 USD | 226.18 USD | `-76.28%` | `2,845.00` |
| `Live` | `Long` | `0.0875` | 1,240,000.00 USD | 0.00 USD | 868.52 USD | `-73.89%` | `9,926.00` |
| `Live` | `Long` | `0.0905` | 1,240,000.00 USD | 0.00 USD | 188.15 USD | `-73.00%` | `2,079.00` |
| `Live` | `Long` | `0.1145` | 1,240,000.00 USD | 0.00 USD | 2,450.00 USD | `-65.84%` | `21,428.00` |
| `Live` | `Long` | `0.1155` | 1,240,000.00 USD | 0.00 USD | 265.88 USD | `-65.54%` | `2,302.00` |
| `Live` | `Long` | `0.1165` | 1,240,000.00 USD | 0.00 USD | 123.26 USD | `-65.24%` | `1,058.00` |
| `Live` | `Long` | `0.1385` | 1,240,000.00 USD | 0.00 USD | 11,410.00 USD | `-58.68%` | `82,417.00` |
| `Live` | `Long` | `0.1475` | 1,220,000.00 USD | 0.00 USD | 44,010.00 USD | `-55.99%` | `298,397.00` |
| `Live` | `Long` | `0.1585` | 1,180,000.00 USD | 0.00 USD | 388.01 USD | `-52.71%` | `2,448.00` |
| `Live` | `Long` | `0.1675` | 1,180,000.00 USD | 0.00 USD | 10,230.00 USD | `-50.02%` | `61,100.00` |
| `Live` | `Long` | `0.1685` | 1,170,000.00 USD | 0.00 USD | 20,120.00 USD | `-49.72%` | `119,400.00` |
| `Live` | `Long` | `0.1705` | 1,150,000.00 USD | 0.00 USD | 511.50 USD | `-49.13%` | `3,000.00` |
| `Live` | `Long` | `0.1715` | 1,150,000.00 USD | 0.00 USD | 4,470.00 USD | `-48.83%` | `26,050.00` |
| `Live` | `Long` | `0.1725` | 1,150,000.00 USD | 0.00 USD | 10,440.00 USD | `-48.53%` | `60,538.00` |
| `Live` | `Long` | `0.1735` | 1,130,000.00 USD | 0.00 USD | 339.71 USD | `-48.23%` | `1,958.00` |
| `Live` | `Long` | `0.1745` | 1,130,000.00 USD | 0.00 USD | 5,170.00 USD | `-47.93%` | `29,642.00` |
| `Live` | `Long` | `0.1755` | 1,130,000.00 USD | 0.00 USD | 38,650.00 USD | `-47.64%` | `220,201.00` |
| `Live` | `Long` | `0.1765` | 1,090,000.00 USD | 0.00 USD | 174.38 USD | `-47.34%` | `988.00` |
| `Live` | `Long` | `0.1775` | 1,090,000.00 USD | 0.00 USD | 1,400.00 USD | `-47.04%` | `7,875.00` |
| `Live` | `Long` | `0.1815` | 1,090,000.00 USD | 0.00 USD | 100.37 USD | `-45.85%` | `553.00` |
| `Live` | `Long` | `0.1845` | 1,090,000.00 USD | 0.00 USD | 165.87 USD | `-44.95%` | `899.00` |
| `Live` | `Long` | `0.1855` | 1,090,000.00 USD | 0.00 USD | 109.63 USD | `-44.65%` | `591.00` |
| `Live` | `Long` | `0.1875` | 1,090,000.00 USD | 0.00 USD | 36,310.00 USD | `-44.05%` | `193,636.00` |
| `Live` | `Long` | `0.1975` | 1,050,000.00 USD | 0.00 USD | 632.00 USD | `-41.07%` | `3,200.00` |
| `Live` | `Long` | `0.2105` | 1,050,000.00 USD | 0.00 USD | 14,200.00 USD | `-37.19%` | `67,468.00` |
| `Live` | `Long` | `0.2165` | 1,040,000.00 USD | 0.00 USD | 1,520.00 USD | `-35.40%` | `7,003.00` |
| `Live` | `Long` | `0.2185` | 1,040,000.00 USD | 0.00 USD | 512.82 USD | `-34.81%` | `2,347.00` |
| `Live` | `Long` | `0.2205` | 1,040,000.00 USD | 0.00 USD | 493.04 USD | `-34.21%` | `2,236.00` |
| `Live` | `Long` | `0.2225` | 1,040,000.00 USD | 0.00 USD | 232.51 USD | `-33.61%` | `1,045.00` |
| `Live` | `Long` | `0.2245` | 1,030,000.00 USD | 0.00 USD | 4,570.00 USD | `-33.02%` | `20,360.00` |
| `Live` | `Long` | `0.2265` | 1,030,000.00 USD | 0.00 USD | 204.76 USD | `-32.42%` | `904.00` |
| `Live` | `Long` | `0.2295` | 1,030,000.00 USD | 0.00 USD | 2,070.00 USD | `-31.52%` | `9,004.00` |
| `Live` | `Long` | `0.2305` | 1,030,000.00 USD | 0.00 USD | 410.06 USD | `-31.22%` | `1,779.00` |
| `Live` | `Long` | `0.2325` | 1,030,000.00 USD | 0.00 USD | 2,420.00 USD | `-30.63%` | `10,412.00` |
| `Live` | `Long` | `0.2335` | 1,030,000.00 USD | 0.00 USD | 553.86 USD | `-30.33%` | `2,372.00` |
| `Live` | `Long` | `0.2345` | 1,020,000.00 USD | 0.00 USD | 5,700.00 USD | `-30.03%` | `24,311.00` |
| `Live` | `Long` | `0.2355` | 1,020,000.00 USD | 0.00 USD | 3,130.00 USD | `-29.73%` | `13,311.00` |
| `Live` | `Long` | `0.2365` | 1,020,000.00 USD | 0.00 USD | 686.56 USD | `-29.43%` | `2,903.00` |
| `Live` | `Long` | `0.2375` | 1,020,000.00 USD | 0.00 USD | 826.50 USD | `-29.14%` | `3,480.00` |
| `Live` | `Long` | `0.2395` | 1,010,000.00 USD | 0.00 USD | 151.36 USD | `-28.54%` | `632.00` |
| `Live` | `Long` | `0.2425` | 1,010,000.00 USD | 0.00 USD | 6,760.00 USD | `-27.64%` | `27,881.00` |
| `Live` | `Long` | `0.2435` | 1,010,000.00 USD | 0.00 USD | 885.85 USD | `-27.35%` | `3,638.00` |
| `Live` | `Long` | `0.2445` | 1,010,000.00 USD | 0.00 USD | 464.79 USD | `-27.05%` | `1,901.00` |
| `Live` | `Long` | `0.2455` | 1,010,000.00 USD | 0.00 USD | 384.94 USD | `-26.75%` | `1,568.00` |
| `Live` | `Long` | `0.2475` | 1,010,000.00 USD | 0.00 USD | 11,840.00 USD | `-26.15%` | `47,833.00` |
| `Live` | `Long` | `0.2505` | 993,750.00 USD | 0.00 USD | 555.61 USD | `-25.26%` | `2,218.00` |
| `Live` | `Long` | `0.2565` | 993,190.00 USD | 0.00 USD | 1,520.00 USD | `-23.47%` | `5,912.00` |
| `Live` | `Long` | `0.2595` | 991,670.00 USD | 0.00 USD | 749.18 USD | `-22.57%` | `2,887.00` |
| `Live` | `Long` | `0.2615` | 990,920.00 USD | 0.00 USD | 107.74 USD | `-21.98%` | `412.00` |
| `Live` | `Long` | `0.2635` | 990,820.00 USD | 0.00 USD | 4,550.00 USD | `-21.38%` | `17,283.00` |
| `Live` | `Long` | `0.2645` | 986,260.00 USD | 0.00 USD | 2,650.00 USD | `-21.08%` | `10,032.00` |
| `Live` | `Long` | `0.2655` | 983,610.00 USD | 0.00 USD | 193.02 USD | `-20.78%` | `727.00` |
| `Live` | `Long` | `0.2675` | 983,420.00 USD | 0.00 USD | 321.54 USD | `-20.18%` | `1,202.00` |
| `Live` | `Long` | `0.2685` | 983,090.00 USD | 0.00 USD | 3,390.00 USD | `-19.89%` | `12,636.00` |
| `Live` | `Long` | `0.2735` | 979,700.00 USD | 0.00 USD | 220.99 USD | `-18.39%` | `808.00` |
| `Live` | `Long` | `0.2745` | 979,480.00 USD | 0.00 USD | 84,470.00 USD | `-18.10%` | `307,728.00` |
| `Live` | `Long` | `0.2785` | 895,010.00 USD | 0.00 USD | 15,180.00 USD | `-16.90%` | `54,497.00` |
| `Live` | `Long` | `0.2795` | 879,830.00 USD | 0.00 USD | 6,260.00 USD | `-16.60%` | `22,380.00` |
| `Live` | `Long` | `0.2805` | 873,580.00 USD | 0.00 USD | 13,300.00 USD | `-16.31%` | `47,408.00` |
| `Live` | `Long` | `0.2815` | 860,280.00 USD | 0.00 USD | 3,690.00 USD | `-16.01%` | `13,109.00` |
| `Live` | `Long` | `0.2825` | 856,590.00 USD | 0.00 USD | 838.74 USD | `-15.71%` | `2,969.00` |
| `Live` | `Long` | `0.2845` | 855,750.00 USD | 0.00 USD | 357.90 USD | `-15.11%` | `1,258.00` |
| `Live` | `Long` | `0.2855` | 855,390.00 USD | 0.00 USD | 6,300.00 USD | `-14.81%` | `22,055.00` |
| `Live` | `Long` | `0.2865` | 849,100.00 USD | 0.00 USD | 4,310.00 USD | `-14.52%` | `15,057.00` |
| `Live` | `Long` | `0.2905` | 844,780.00 USD | 0.00 USD | 821.82 USD | `-13.32%` | `2,829.00` |
| `Live` | `Long` | `0.2915` | 843,960.00 USD | 0.00 USD | 954.37 USD | `-13.02%` | `3,274.00` |
| `Live` | `Long` | `0.2935` | 843,010.00 USD | 0.00 USD | 213.08 USD | `-12.43%` | `726.00` |
| `Live` | `Long` | `0.2945` | 842,790.00 USD | 0.00 USD | 124.87 USD | `-12.13%` | `424.00` |
| `Live` | `Long` | `0.2955` | 842,670.00 USD | 0.00 USD | 156.61 USD | `-11.83%` | `530.00` |
| `Live` | `Long` | `0.2965` | 842,510.00 USD | 0.00 USD | 1,010.00 USD | `-11.53%` | `3,398.00` |
| `Live` | `Long` | `0.2985` | 841,500.00 USD | 0.00 USD | 759.68 USD | `-10.94%` | `2,545.00` |
| `Live` | `Long` | `0.2995` | 840,740.00 USD | 0.00 USD | 197.37 USD | `-10.64%` | `659.00` |
| `Live` | `Long` | `0.3005` | 840,550.00 USD | 0.00 USD | 10,620.00 USD | `-10.34%` | `35,336.00` |
| `Live` | `Long` | `0.3015` | 829,930.00 USD | 0.00 USD | 102.81 USD | `-10.04%` | `341.00` |
| `Live` | `Long` | `0.3025` | 829,820.00 USD | 0.00 USD | 2,510.00 USD | `-9.74%` | `8,314.00` |
| `Live` | `Long` | `0.3035` | 827,310.00 USD | 0.00 USD | 4,040.00 USD | `-9.44%` | `13,300.00` |
| `Live` | `Long` | `0.3045` | 823,270.00 USD | 0.00 USD | 138.24 USD | `-9.15%` | `454.00` |
| `Live` | `Long` | `0.3055` | 823,130.00 USD | 0.00 USD | 14,670.00 USD | `-8.85%` | `48,026.00` |
| `Live` | `Long` | `0.3065` | 808,460.00 USD | 0.00 USD | 5,900.00 USD | `-8.55%` | `19,262.00` |
| `Live` | `Long` | `0.3075` | 802,560.00 USD | 0.00 USD | 722.62 USD | `-8.25%` | `2,350.00` |
| `Live` | `Long` | `0.3085` | 801,840.00 USD | 0.00 USD | 291.53 USD | `-7.95%` | `945.00` |
| `Live` | `Long` | `0.3095` | 801,540.00 USD | 0.00 USD | 192.51 USD | `-7.65%` | `622.00` |
| `Live` | `Long` | `0.3105` | 801,350.00 USD | 0.00 USD | 820.96 USD | `-7.35%` | `2,644.00` |
| `Live` | `Long` | `0.3115` | 800,530.00 USD | 0.00 USD | 13,600.00 USD | `-7.06%` | `43,671.00` |
| `Live` | `Long` | `0.3125` | 786,930.00 USD | 0.00 USD | 17,810.00 USD | `-6.76%` | `56,977.00` |
| `Live` | `Long` | `0.3135` | 769,120.00 USD | 0.00 USD | 446.11 USD | `-6.46%` | `1,423.00` |
| `Live` | `Long` | `0.3145` | 768,680.00 USD | 0.00 USD | 577.11 USD | `-6.16%` | `1,835.00` |
| `Live` | `Long` | `0.3155` | 768,100.00 USD | 0.00 USD | 11,510.00 USD | `-5.86%` | `36,472.00` |
| `Live` | `Long` | `0.3165` | 756,590.00 USD | 0.00 USD | 935.89 USD | `-5.56%` | `2,957.00` |
| `Live` | `Long` | `0.3175` | 755,660.00 USD | 0.00 USD | 2,290.00 USD | `-5.27%` | `7,205.00` |
| `Live` | `Long` | `0.3185` | 753,370.00 USD | 0.00 USD | 1,300.00 USD | `-4.97%` | `4,080.00` |
| `Live` | `Long` | `0.3205` | 752,070.00 USD | 0.00 USD | 2,930.00 USD | `-4.37%` | `9,154.00` |
| `Live` | `Long` | `0.3235` | 749,140.00 USD | 0.00 USD | 128.43 USD | `-3.48%` | `397.00` |
| `Live` | `Long` | `0.3255` | 749,010.00 USD | 0.00 USD | 3,580.00 USD | `-2.88%` | `11,000.00` |
| `Live` | `Long` | `0.3275` | 745,430.00 USD | 0.00 USD | 163.42 USD | `-2.28%` | `499.00` |
| `Live` | `Long` | `0.3285` | 745,260.00 USD | 0.00 USD | 745,260.00 USD | `-1.98%` | `2,268,686.00` |
| `Live` | `Short` | `0.3445` | 2,280.00 USD | 2,280.00 USD | 0.00 USD | `+2.79%` | `6,622.00` |
| `Live` | `Short` | `0.3505` | 10,930.00 USD | 8,650.00 USD | 0.00 USD | `+4.58%` | `24,688.00` |
| `Live` | `Short` | `0.3515` | 11,110.00 USD | 175.05 USD | 0.00 USD | `+4.88%` | `498.00` |
| `Live` | `Short` | `0.3525` | 11,220.00 USD | 112.45 USD | 0.00 USD | `+5.18%` | `319.00` |
| `Live` | `Short` | `0.3545` | 40,690.00 USD | 29,460.00 USD | 0.00 USD | `+5.77%` | `83,113.00` |
| `Live` | `Short` | `0.3635` | 53,050.00 USD | 12,360.00 USD | 0.00 USD | `+8.46%` | `34,003.00` |
| `Live` | `Short` | `0.3665` | 56,160.00 USD | 3,110.00 USD | 0.00 USD | `+9.35%` | `8,498.00` |
| `Live` | `Short` | `0.3705` | 56,440.00 USD | 278.99 USD | 0.00 USD | `+10.55%` | `753.00` |
| `Live` | `Short` | `0.3725` | 56,630.00 USD | 186.25 USD | 0.00 USD | `+11.14%` | `500.00` |
| `Live` | `Short` | `0.3735` | 63,690.00 USD | 7,070.00 USD | 0.00 USD | `+11.44%` | `18,920.00` |
| `Live` | `Short` | `0.3755` | 67,720.00 USD | 4,030.00 USD | 0.00 USD | `+12.04%` | `10,732.00` |
| `Live` | `Short` | `0.3775` | 67,830.00 USD | 104.19 USD | 0.00 USD | `+12.64%` | `276.00` |
| `Live` | `Short` | `0.3785` | 624,250.00 USD | 556,430.00 USD | 0.00 USD | `+12.93%` | `1,470,083.00` |
| `Live` | `Short` | `0.3795` | 625,030.00 USD | 773.04 USD | 0.00 USD | `+13.23%` | `2,037.00` |
| `Live` | `Short` | `0.3805` | 628,420.00 USD | 3,390.00 USD | 0.00 USD | `+13.53%` | `8,919.00` |
| `Live` | `Short` | `0.3835` | 628,530.00 USD | 115.05 USD | 0.00 USD | `+14.43%` | `300.00` |
| `Live` | `Short` | `0.3855` | 628,800.00 USD | 264.84 USD | 0.00 USD | `+15.02%` | `687.00` |
| `Live` | `Short` | `0.3865` | 2,170,000.00 USD | 1,550,000.00 USD | 0.00 USD | `+15.32%` | `4,000,000.00` |
| `Live` | `Short` | `0.3895` | 2,180,000.00 USD | 4,760.00 USD | 0.00 USD | `+16.22%` | `12,210.00` |
| `Live` | `Short` | `0.3905` | 2,190,000.00 USD | 6,000.00 USD | 0.00 USD | `+16.51%` | `15,374.00` |
| `Live` | `Short` | `0.3935` | 2,190,000.00 USD | 1,480.00 USD | 0.00 USD | `+17.41%` | `3,770.00` |
| `Live` | `Short` | `0.3945` | 2,310,000.00 USD | 118,130.00 USD | 0.00 USD | `+17.71%` | `299,436.00` |
| `Live` | `Short` | `0.4015` | 2,310,000.00 USD | 327.62 USD | 0.00 USD | `+19.80%` | `816.00` |
| `Live` | `Short` | `0.4085` | 2,310,000.00 USD | 170.75 USD | 0.00 USD | `+21.89%` | `418.00` |
| `Live` | `Short` | `0.4095` | 2,310,000.00 USD | 239.56 USD | 0.00 USD | `+22.18%` | `585.00` |
| `Live` | `Short` | `0.4145` | 2,320,000.00 USD | 12,440.00 USD | 0.00 USD | `+23.68%` | `30,000.00` |
| `Live` | `Short` | `0.4165` | 2,410,000.00 USD | 94,510.00 USD | 0.00 USD | `+24.27%` | `226,922.00` |
| `Live` | `Short` | `0.4185` | 2,410,000.00 USD | 998.96 USD | 0.00 USD | `+24.87%` | `2,387.00` |
| `Live` | `Short` | `0.4235` | 2,410,000.00 USD | 134.25 USD | 0.00 USD | `+26.36%` | `317.00` |
| `Live` | `Short` | `0.4245` | 2,420,000.00 USD | 3,930.00 USD | 0.00 USD | `+26.66%` | `9,259.00` |
| `Live` | `Short` | `0.4335` | 2,420,000.00 USD | 1,500.00 USD | 0.00 USD | `+29.35%` | `3,464.00` |
| `Live` | `Short` | `0.4355` | 2,490,000.00 USD | 70,890.00 USD | 0.00 USD | `+29.94%` | `162,775.00` |
| `Live` | `Short` | `0.4365` | 2,490,000.00 USD | 1,490.00 USD | 0.00 USD | `+30.24%` | `3,416.00` |
| `Live` | `Short` | `0.4415` | 2,490,000.00 USD | 377.48 USD | 0.00 USD | `+31.73%` | `855.00` |
| `Live` | `Short` | `0.4425` | 2,510,000.00 USD | 13,280.00 USD | 0.00 USD | `+32.03%` | `30,000.00` |
| `Live` | `Short` | `0.4435` | 2,510,000.00 USD | 3,460.00 USD | 0.00 USD | `+32.33%` | `7,800.00` |
| `Live` | `Short` | `0.4445` | 2,530,000.00 USD | 22,200.00 USD | 0.00 USD | `+32.63%` | `49,950.00` |
| `Live` | `Short` | `0.4455` | 2,530,000.00 USD | 1,020.00 USD | 0.00 USD | `+32.93%` | `2,284.00` |
| `Live` | `Short` | `0.4465` | 2,540,000.00 USD | 5,520.00 USD | 0.00 USD | `+33.22%` | `12,352.00` |
| `Live` | `Short` | `0.4475` | 2,600,000.00 USD | 65,610.00 USD | 0.00 USD | `+33.52%` | `146,614.00` |
| `Live` | `Short` | `0.4675` | 2,600,000.00 USD | 270.22 USD | 0.00 USD | `+39.49%` | `578.00` |
| `Live` | `Short` | `0.4895` | 2,600,000.00 USD | 839.49 USD | 0.00 USD | `+46.05%` | `1,715.00` |
| `Live` | `Short` | `0.4905` | 2,610,000.00 USD | 5,120.00 USD | 0.00 USD | `+46.35%` | `10,430.00` |
| `Live` | `Short` | `0.4995` | 2,610,000.00 USD | 2,730.00 USD | 0.00 USD | `+49.04%` | `5,465.00` |
| `Live` | `Short` | `0.5005` | 2,640,000.00 USD | 23,320.00 USD | 0.00 USD | `+49.34%` | `46,591.00` |
| `Live` | `Short` | `0.5325` | 2,640,000.00 USD | 667.22 USD | 0.00 USD | `+58.88%` | `1,253.00` |
| `Live` | `Short` | `0.5355` | 2,640,000.00 USD | 1,170.00 USD | 0.00 USD | `+59.78%` | `2,193.00` |
| `Live` | `Short` | `0.5475` | 2,680,000.00 USD | 40,520.00 USD | 0.00 USD | `+63.36%` | `74,000.00` |
| `Live` | `Short` | `0.5575` | 2,680,000.00 USD | 3,060.00 USD | 0.00 USD | `+66.34%` | `5,483.00` |
| `Live` | `Short` | `0.5605` | 2,680,000.00 USD | 140.12 USD | 0.00 USD | `+67.24%` | `250.00` |
| `Live` | `Short` | `0.5765` | 3,430,000.00 USD | 747,860.00 USD | 0.00 USD | `+72.01%` | `1,297,248.00` |
| `Live` | `Short` | `0.5855` | 3,430,000.00 USD | 115.93 USD | 0.00 USD | `+74.70%` | `198.00` |
| `Live` | `Short` | `0.5935` | 3,430,000.00 USD | 4,900.00 USD | 0.00 USD | `+77.08%` | `8,250.00` |
| `Live` | `Short` | `0.6155` | 3,460,000.00 USD | 24,620.00 USD | 0.00 USD | `+83.65%` | `40,000.00` |
| `Live` | `Short` | `0.6265` | 3,460,000.00 USD | 379.03 USD | 0.00 USD | `+86.93%` | `605.00` |
| `Live` | `Short` | `0.6335` | 3,470,000.00 USD | 6,810.00 USD | 0.00 USD | `+89.02%` | `10,756.00` |
| `Live` | `Short` | `0.6505` | 3,570,000.00 USD | 102,000.00 USD | 0.00 USD | `+94.09%` | `156,809.00` |
| `Live` | `Short` | `0.6515` | 3,570,000.00 USD | 951.19 USD | 0.00 USD | `+94.39%` | `1,460.00` |
| `Live` | `Short` | `0.6545` | 3,570,000.00 USD | 706.21 USD | 0.00 USD | `+95.29%` | `1,079.00` |
| `Live` | `Short` | `0.6615` | 3,570,000.00 USD | 2,060.00 USD | 0.00 USD | `+97.37%` | `3,114.00` |
| `Live` | `Short` | `0.6635` | 3,580,000.00 USD | 3,740.00 USD | 0.00 USD | `+97.97%` | `5,632.00` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `0.0925` | 2,140,000.00 USD | 0.00 USD | 407.56 USD | `-72.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0945` | 2,140,000.00 USD | 0.00 USD | 198.45 USD | `-71.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1415` | 2,140,000.00 USD | 0.00 USD | 330.26 USD | `-57.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2035` | 2,140,000.00 USD | 0.00 USD | 1,750.00 USD | `-39.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2105` | 2,140,000.00 USD | 0.00 USD | 579.72 USD | `-37.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2165` | 2,140,000.00 USD | 0.00 USD | 1,030.00 USD | `-35.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2195` | 2,140,000.00 USD | 0.00 USD | 515.61 USD | `-34.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2305` | 2,140,000.00 USD | 0.00 USD | 121.70 USD | `-31.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2345` | 2,140,000.00 USD | 0.00 USD | 705.61 USD | `-30.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2355` | 2,140,000.00 USD | 0.00 USD | 159.20 USD | `-29.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2405` | 2,140,000.00 USD | 0.00 USD | 1,200.00 USD | `-28.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2415` | 2,140,000.00 USD | 0.00 USD | 127.51 USD | `-27.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2505` | 2,140,000.00 USD | 0.00 USD | 1,850.00 USD | `-25.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2515` | 2,130,000.00 USD | 0.00 USD | 41,500.00 USD | `-24.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2565` | 2,090,000.00 USD | 0.00 USD | 1,920.00 USD | `-23.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2605` | 2,090,000.00 USD | 0.00 USD | 664.01 USD | `-22.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2625` | 2,090,000.00 USD | 0.00 USD | 954.98 USD | `-21.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2635` | 2,090,000.00 USD | 0.00 USD | 103.56 USD | `-21.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2675` | 2,090,000.00 USD | 0.00 USD | 695.50 USD | `-20.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2685` | 2,090,000.00 USD | 0.00 USD | 1,630.00 USD | `-19.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2695` | 2,090,000.00 USD | 0.00 USD | 1,470.00 USD | `-19.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2755` | 2,080,000.00 USD | 0.00 USD | 101.94 USD | `-17.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2775` | 2,080,000.00 USD | 0.00 USD | 3,260.00 USD | `-17.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2815` | 2,080,000.00 USD | 0.00 USD | 2,550.00 USD | `-16.01%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2835` | 2,080,000.00 USD | 0.00 USD | 229.92 USD | `-15.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2875` | 2,080,000.00 USD | 0.00 USD | 8,010.00 USD | `-14.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2935` | 2,070,000.00 USD | 0.00 USD | 11,610.00 USD | `-12.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2965` | 2,060,000.00 USD | 0.00 USD | 111.19 USD | `-11.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2985` | 2,060,000.00 USD | 0.00 USD | 433.42 USD | `-10.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3005` | 2,060,000.00 USD | 0.00 USD | 2,710.00 USD | `-10.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3045` | 2,060,000.00 USD | 0.00 USD | 503.95 USD | `-9.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3065` | 2,050,000.00 USD | 0.00 USD | 1,400.00 USD | `-8.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3075` | 2,050,000.00 USD | 0.00 USD | 193.11 USD | `-8.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3085` | 2,050,000.00 USD | 0.00 USD | 15,150.00 USD | `-7.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3095` | 2,040,000.00 USD | 0.00 USD | 156.30 USD | `-7.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3105` | 2,040,000.00 USD | 0.00 USD | 12,200.00 USD | `-7.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3115` | 2,030,000.00 USD | 0.00 USD | 6,530.00 USD | `-7.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3125` | 2,020,000.00 USD | 0.00 USD | 524,570.00 USD | `-6.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3135` | 1,490,000.00 USD | 0.00 USD | 1,270.00 USD | `-6.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3145` | 1,490,000.00 USD | 0.00 USD | 53,690.00 USD | `-6.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3155` | 1,440,000.00 USD | 0.00 USD | 644.88 USD | `-5.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3165` | 1,440,000.00 USD | 0.00 USD | 7,400.00 USD | `-5.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3175` | 1,430,000.00 USD | 0.00 USD | 850.90 USD | `-5.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3185` | 1,430,000.00 USD | 0.00 USD | 1,730.00 USD | `-4.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3195` | 1,430,000.00 USD | 0.00 USD | 5,610.00 USD | `-4.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3205` | 1,420,000.00 USD | 0.00 USD | 10,160.00 USD | `-4.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3215` | 1,410,000.00 USD | 0.00 USD | 43,760.00 USD | `-4.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3225` | 1,370,000.00 USD | 0.00 USD | 5,520.00 USD | `-3.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3235` | 1,360,000.00 USD | 0.00 USD | 7,040.00 USD | `-3.48%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3245` | 1,360,000.00 USD | 0.00 USD | 3,970.00 USD | `-3.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3255` | 1,350,000.00 USD | 0.00 USD | 2,240.00 USD | `-2.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3265` | 1,350,000.00 USD | 0.00 USD | 6,130.00 USD | `-2.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3275` | 1,340,000.00 USD | 0.00 USD | 7,620.00 USD | `-2.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3285` | 1,340,000.00 USD | 0.00 USD | 4,270.00 USD | `-1.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3295` | 1,330,000.00 USD | 0.00 USD | 1,320,000.00 USD | `-1.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3305` | 13,100.00 USD | 0.00 USD | 949.53 USD | `-1.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3315` | 12,150.00 USD | 0.00 USD | 984.22 USD | `-1.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3325` | 11,160.00 USD | 0.00 USD | 5,730.00 USD | `-0.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3335` | 5,440.00 USD | 0.00 USD | 4,880.00 USD | `-0.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3345` | 560.96 USD | 0.00 USD | 560.96 USD | `-0.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3355` | 8,260.00 USD | 8,260.00 USD | 0.00 USD | `+0.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3365` | 8,520.00 USD | 265.50 USD | 0.00 USD | `+0.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3375` | 10,550.00 USD | 2,020.00 USD | 0.00 USD | `+0.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3385` | 12,000.00 USD | 1,450.00 USD | 0.00 USD | `+1.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3395` | 12,960.00 USD | 960.45 USD | 0.00 USD | `+1.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3405` | 14,410.00 USD | 1,460.00 USD | 0.00 USD | `+1.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3415` | 14,900.00 USD | 486.30 USD | 0.00 USD | `+1.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3425` | 15,330.00 USD | 431.55 USD | 0.00 USD | `+2.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3435` | 16,160.00 USD | 828.18 USD | 0.00 USD | `+2.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3445` | 16,650.00 USD | 488.16 USD | 0.00 USD | `+2.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3455` | 17,080.00 USD | 435.33 USD | 0.00 USD | `+3.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3465` | 17,640.00 USD | 555.44 USD | 0.00 USD | `+3.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3475` | 17,910.00 USD | 274.18 USD | 0.00 USD | `+3.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3485` | 18,350.00 USD | 439.11 USD | 0.00 USD | `+3.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3495` | 20,300.00 USD | 1,950.00 USD | 0.00 USD | `+4.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3505` | 20,970.00 USD | 665.60 USD | 0.00 USD | `+4.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3515` | 21,570.00 USD | 605.63 USD | 0.00 USD | `+4.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3525` | 22,000.00 USD | 423.70 USD | 0.00 USD | `+5.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3535` | 22,310.00 USD | 312.14 USD | 0.00 USD | `+5.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3545` | 22,660.00 USD | 354.50 USD | 0.00 USD | `+5.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3555` | 22,800.00 USD | 132.96 USD | 0.00 USD | `+6.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3565` | 62,230.00 USD | 39,430.00 USD | 0.00 USD | `+6.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3575` | 102,620.00 USD | 40,390.00 USD | 0.00 USD | `+6.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3585` | 105,920.00 USD | 3,310.00 USD | 0.00 USD | `+6.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3595` | 106,960.00 USD | 1,030.00 USD | 0.00 USD | `+7.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3605` | 109,900.00 USD | 2,940.00 USD | 0.00 USD | `+7.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3615` | 110,120.00 USD | 224.49 USD | 0.00 USD | `+7.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3635` | 110,220.00 USD | 103.23 USD | 0.00 USD | `+8.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3645` | 112,920.00 USD | 2,700.00 USD | 0.00 USD | `+8.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3655` | 123,230.00 USD | 10,310.00 USD | 0.00 USD | `+9.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3665` | 123,490.00 USD | 256.55 USD | 0.00 USD | `+9.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3675` | 123,660.00 USD | 172.72 USD | 0.00 USD | `+9.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3685` | 123,880.00 USD | 218.89 USD | 0.00 USD | `+9.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3695` | 138,490.00 USD | 14,610.00 USD | 0.00 USD | `+10.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3705` | 139,090.00 USD | 597.99 USD | 0.00 USD | `+10.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3715` | 139,270.00 USD | 174.60 USD | 0.00 USD | `+10.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3725` | 139,370.00 USD | 107.28 USD | 0.00 USD | `+11.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3735` | 139,810.00 USD | 439.61 USD | 0.00 USD | `+11.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3745` | 140,250.00 USD | 437.79 USD | 0.00 USD | `+11.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3755` | 142,720.00 USD | 2,470.00 USD | 0.00 USD | `+12.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3765` | 142,900.00 USD | 182.60 USD | 0.00 USD | `+12.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3775` | 149,350.00 USD | 6,450.00 USD | 0.00 USD | `+12.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3785` | 149,630.00 USD | 275.17 USD | 0.00 USD | `+12.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3795` | 150,200.00 USD | 569.25 USD | 0.00 USD | `+13.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3805` | 156,280.00 USD | 6,080.00 USD | 0.00 USD | `+13.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3815` | 156,540.00 USD | 257.89 USD | 0.00 USD | `+13.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3825` | 156,800.00 USD | 262.78 USD | 0.00 USD | `+14.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3835` | 157,030.00 USD | 224.73 USD | 0.00 USD | `+14.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3855` | 157,650.00 USD | 621.04 USD | 0.00 USD | `+15.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3865` | 158,390.00 USD | 742.08 USD | 0.00 USD | `+15.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3875` | 159,500.00 USD | 1,110.00 USD | 0.00 USD | `+15.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3885` | 159,690.00 USD | 181.04 USD | 0.00 USD | `+15.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3895` | 1,720,000.00 USD | 1,560,000.00 USD | 0.00 USD | `+16.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3905` | 1,720,000.00 USD | 138.63 USD | 0.00 USD | `+16.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3915` | 1,720,000.00 USD | 276.40 USD | 0.00 USD | `+16.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3945` | 1,720,000.00 USD | 126.24 USD | 0.00 USD | `+17.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3965` | 1,720,000.00 USD | 2,400.00 USD | 0.00 USD | `+18.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3975` | 1,720,000.00 USD | 647.13 USD | 0.00 USD | `+18.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3985` | 1,720,000.00 USD | 1,200.00 USD | 0.00 USD | `+18.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3995` | 1,790,000.00 USD | 71,490.00 USD | 0.00 USD | `+19.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4005` | 1,800,000.00 USD | 864.28 USD | 0.00 USD | `+19.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4015` | 1,800,000.00 USD | 3,920.00 USD | 0.00 USD | `+19.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4035` | 1,880,000.00 USD | 79,330.00 USD | 0.00 USD | `+20.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4055` | 1,880,000.00 USD | 1,200.00 USD | 0.00 USD | `+20.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4065` | 1,880,000.00 USD | 1,200.00 USD | 0.00 USD | `+21.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4085` | 1,880,000.00 USD | 138.07 USD | 0.00 USD | `+21.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4095` | 1,880,000.00 USD | 1,270.00 USD | 0.00 USD | `+22.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4135` | 1,880,000.00 USD | 331.63 USD | 0.00 USD | `+23.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4175` | 1,880,000.00 USD | 313.54 USD | 0.00 USD | `+24.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4205` | 1,880,000.00 USD | 186.70 USD | 0.00 USD | `+25.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4275` | 1,880,000.00 USD | 325.75 USD | 0.00 USD | `+27.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4305` | 1,880,000.00 USD | 183.82 USD | 0.00 USD | `+28.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4355` | 1,880,000.00 USD | 299.19 USD | 0.00 USD | `+29.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4405` | 1,920,000.00 USD | 38,580.00 USD | 0.00 USD | `+31.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4445` | 1,920,000.00 USD | 170.69 USD | 0.00 USD | `+32.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4475` | 1,920,000.00 USD | 135.59 USD | 0.00 USD | `+33.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4495` | 1,920,000.00 USD | 1,520.00 USD | 0.00 USD | `+34.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4505` | 1,920,000.00 USD | 320.31 USD | 0.00 USD | `+34.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4545` | 1,930,000.00 USD | 5,340.00 USD | 0.00 USD | `+35.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4605` | 1,930,000.00 USD | 1,470.00 USD | 0.00 USD | `+37.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4895` | 2,010,000.00 USD | 80,770.00 USD | 0.00 USD | `+46.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4905` | 2,010,000.00 USD | 169.22 USD | 0.00 USD | `+46.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4945` | 2,010,000.00 USD | 153.79 USD | 0.00 USD | `+47.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4965` | 2,010,000.00 USD | 724.89 USD | 0.00 USD | `+48.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.5005` | 2,020,000.00 USD | 11,150.00 USD | 0.00 USD | `+49.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.5055` | 2,030,000.00 USD | 1,930.00 USD | 0.00 USD | `+50.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.5175` | 2,030,000.00 USD | 2,280.00 USD | 0.00 USD | `+54.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.5295` | 2,030,000.00 USD | 135.02 USD | 0.00 USD | `+57.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6255` | 2,030,000.00 USD | 1,160.00 USD | 0.00 USD | `+86.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6305` | 2,030,000.00 USD | 240.85 USD | 0.00 USD | `+88.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6325` | 2,030,000.00 USD | 1,100.00 USD | 0.00 USD | `+88.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6695` | 2,030,000.00 USD | 1,050.00 USD | 0.00 USD | `+99.76%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `0.2953` | 22,390,000.00 USD | 0.00 USD | 22,390,000.00 USD | 82,100.00 USD | 0.00 USD | 10,820.00 USD |
| `7D` | `0.2959` | 22,300,000.00 USD | 0.00 USD | 22,300,000.00 USD | 108,710.00 USD | 22,740.00 USD | 9,700.00 USD |
| `7D` | `0.2965` | 22,150,000.00 USD | 0.00 USD | 22,150,000.00 USD | 123,080.00 USD | 36,820.00 USD | 59,640.00 USD |
| `7D` | `0.2971` | 21,940,000.00 USD | 0.00 USD | 21,940,000.00 USD | 88,780.00 USD | 34,680.00 USD | 52,660.00 USD |
| `1D` | `0.2977` | 15,840,000.00 USD | 0.00 USD | 15,840,000.00 USD | 13,380.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.2977` | 21,760,000.00 USD | 0.00 USD | 21,760,000.00 USD | 53,680.00 USD | 18,540.00 USD | 17,670.00 USD |
| `1D` | `0.2981` | 15,830,000.00 USD | 0.00 USD | 15,830,000.00 USD | 12,230.00 USD | 5,290.00 USD | 10,710.00 USD |
| `7D` | `0.2983` | 21,670,000.00 USD | 0.00 USD | 21,670,000.00 USD | 170,240.00 USD | 15,470.00 USD | 39,660.00 USD |
| `1D` | `0.2985` | 15,800,000.00 USD | 0.00 USD | 15,800,000.00 USD | 107,040.00 USD | 10,860.00 USD | 12,860.00 USD |
| `1D` | `0.2989` | 15,670,000.00 USD | 0.00 USD | 15,670,000.00 USD | 26,190.00 USD | 0.00 USD | 8,790.00 USD |
| `7D` | `0.2989` | 21,440,000.00 USD | 0.00 USD | 21,440,000.00 USD | 112,680.00 USD | 18,720.00 USD | 23,920.00 USD |
| `1D` | `0.2993` | 15,640,000.00 USD | 0.00 USD | 15,640,000.00 USD | 55,190.00 USD | 33,830.00 USD | 56,800.00 USD |
| `7D` | `0.2995` | 21,290,000.00 USD | 0.00 USD | 21,290,000.00 USD | 10,860.00 USD | 69,130.00 USD | 80,320.00 USD |
| `1D` | `0.2997` | 15,490,000.00 USD | 0.00 USD | 15,490,000.00 USD | 600.83 USD | 28,790.00 USD | 46,110.00 USD |
| `1D` | `0.3001` | 15,420,000.00 USD | 0.00 USD | 15,420,000.00 USD | 8,760.00 USD | 14,600.00 USD | 14,510.00 USD |
| `7D` | `0.3001` | 21,130,000.00 USD | 0.00 USD | 21,130,000.00 USD | 3,960.00 USD | 34,510.00 USD | 93,100.00 USD |
| `1D` | `0.3005` | 15,380,000.00 USD | 0.00 USD | 15,380,000.00 USD | 15,600.00 USD | 7,870.00 USD | 18,440.00 USD |
| `7D` | `0.3007` | 21,000,000.00 USD | 0.00 USD | 21,000,000.00 USD | 13,780.00 USD | 2,960.00 USD | 22,100.00 USD |
| `1D` | `0.3009` | 15,340,000.00 USD | 0.00 USD | 15,340,000.00 USD | 35,140.00 USD | 8,400.00 USD | 16,090.00 USD |
| `1D` | `0.3013` | 15,280,000.00 USD | 0.00 USD | 15,280,000.00 USD | 17,320.00 USD | 3,170.00 USD | 9,220.00 USD |
| `1D` | `0.3017` | 15,250,000.00 USD | 0.00 USD | 15,250,000.00 USD | 1,010.00 USD | 8,490.00 USD | 9,760.00 USD |
| `7D` | `0.3019` | 20,960,000.00 USD | 0.00 USD | 20,960,000.00 USD | 0.00 USD | 8,660.00 USD | 0.00 USD |
| `1D` | `0.3021` | 15,230,000.00 USD | 0.00 USD | 15,230,000.00 USD | 14,850.00 USD | 4,540.00 USD | 16,590.00 USD |
| `1D` | `0.3025` | 15,190,000.00 USD | 0.00 USD | 15,190,000.00 USD | 2,600.00 USD | 2,050.00 USD | 17,010.00 USD |
| `7D` | `0.3025` | 20,950,000.00 USD | 0.00 USD | 20,950,000.00 USD | 0.00 USD | 22,200.00 USD | 55,830.00 USD |
| `1D` | `0.3029` | 15,170,000.00 USD | 0.00 USD | 15,170,000.00 USD | 24,570.00 USD | 0.00 USD | 6,190.00 USD |
| `7D` | `0.3031` | 20,870,000.00 USD | 0.00 USD | 20,870,000.00 USD | 50,940.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3033` | 15,140,000.00 USD | 0.00 USD | 15,140,000.00 USD | 1,070.00 USD | 8,320.00 USD | 12,600.00 USD |
| `1D` | `0.3037` | 15,120,000.00 USD | 0.00 USD | 15,120,000.00 USD | 517.67 USD | 3,230.00 USD | 0.00 USD |
| `7D` | `0.3037` | 20,820,000.00 USD | 0.00 USD | 20,820,000.00 USD | 1,880.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3041` | 15,110,000.00 USD | 0.00 USD | 15,110,000.00 USD | 965.78 USD | 9,300.00 USD | 75,700.00 USD |
| `7D` | `0.3043` | 20,820,000.00 USD | 0.00 USD | 20,820,000.00 USD | 2,700.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3045` | 15,030,000.00 USD | 0.00 USD | 15,030,000.00 USD | 9,150.00 USD | 13,170.00 USD | 7,480.00 USD |
| `1D` | `0.3049` | 15,000,000.00 USD | 0.00 USD | 15,000,000.00 USD | 37,610.00 USD | 11,440.00 USD | 62,400.00 USD |
| `7D` | `0.3049` | 20,820,000.00 USD | 0.00 USD | 20,820,000.00 USD | 18,360.00 USD | 0.00 USD | 66,870.00 USD |
| `1D` | `0.3053` | 14,890,000.00 USD | 0.00 USD | 14,890,000.00 USD | 46,990.00 USD | 20,580.00 USD | 49,310.00 USD |
| `7D` | `0.3055` | 20,730,000.00 USD | 0.00 USD | 20,730,000.00 USD | 1,490.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3061` | 14,770,000.00 USD | 0.00 USD | 14,770,000.00 USD | 9,630.00 USD | 2,350.00 USD | 56,460.00 USD |
| `7D` | `0.3061` | 20,730,000.00 USD | 0.00 USD | 20,730,000.00 USD | 32,930.00 USD | 7,690.00 USD | 37,210.00 USD |
| `1D` | `0.3065` | 14,700,000.00 USD | 0.00 USD | 14,700,000.00 USD | 29,570.00 USD | 26,740.00 USD | 35,690.00 USD |
| `7D` | `0.3067` | 20,650,000.00 USD | 0.00 USD | 20,650,000.00 USD | 6,300.00 USD | 8,110.00 USD | 0.00 USD |
| `1D` | `0.3069` | 14,610,000.00 USD | 0.00 USD | 14,610,000.00 USD | 1,540.00 USD | 2,880.00 USD | 12,760.00 USD |
| `1D` | `0.3073` | 14,590,000.00 USD | 0.00 USD | 14,590,000.00 USD | 23,280.00 USD | 1,940.00 USD | 0.00 USD |
| `7D` | `0.3073` | 20,640,000.00 USD | 0.00 USD | 20,640,000.00 USD | 7,990.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3077` | 14,570,000.00 USD | 0.00 USD | 14,570,000.00 USD | 350.20 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3079` | 20,630,000.00 USD | 0.00 USD | 20,630,000.00 USD | 37,350.00 USD | 10,270.00 USD | 50,200.00 USD |
| `1D` | `0.3081` | 14,570,000.00 USD | 0.00 USD | 14,570,000.00 USD | 18,400.00 USD | 0.00 USD | 12,250.00 USD |
| `1D` | `0.3085` | 14,540,000.00 USD | 0.00 USD | 14,540,000.00 USD | 340.09 USD | 0.00 USD | 15,810.00 USD |
| `7D` | `0.3085` | 20,530,000.00 USD | 0.00 USD | 20,530,000.00 USD | 3,660.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3089` | 14,520,000.00 USD | 0.00 USD | 14,520,000.00 USD | 550.01 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3091` | 20,530,000.00 USD | 0.00 USD | 20,530,000.00 USD | 7,040.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3093` | 14,520,000.00 USD | 0.00 USD | 14,520,000.00 USD | 14,750.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3097` | 14,500,000.00 USD | 0.00 USD | 14,500,000.00 USD | 7,620.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3097` | 20,520,000.00 USD | 0.00 USD | 20,520,000.00 USD | 79,880.00 USD | 3,620.00 USD | 54,360.00 USD |
| `1D` | `0.3101` | 14,500,000.00 USD | 0.00 USD | 14,500,000.00 USD | 41,340.00 USD | 15,820.00 USD | 46,470.00 USD |
| `7D` | `0.3103` | 20,380,000.00 USD | 0.00 USD | 20,380,000.00 USD | 67,180.00 USD | 0.00 USD | 63,310.00 USD |
| `1D` | `0.3105` | 14,390,000.00 USD | 0.00 USD | 14,390,000.00 USD | 21,200.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3109` | 20,250,000.00 USD | 0.00 USD | 20,250,000.00 USD | 19,040.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3113` | 14,370,000.00 USD | 0.00 USD | 14,370,000.00 USD | 0.00 USD | 4,980.00 USD | 0.00 USD |
| `7D` | `0.3115` | 20,230,000.00 USD | 0.00 USD | 20,230,000.00 USD | 10,250.00 USD | 0.00 USD | 37,490.00 USD |
| `1D` | `0.3117` | 14,370,000.00 USD | 0.00 USD | 14,370,000.00 USD | 15,480.00 USD | 12,220.00 USD | 17,620.00 USD |
| `1D` | `0.3121` | 14,320,000.00 USD | 0.00 USD | 14,320,000.00 USD | 11,560.00 USD | 2,560.00 USD | 33,830.00 USD |
| `7D` | `0.3121` | 20,180,000.00 USD | 0.00 USD | 20,180,000.00 USD | 162,320.00 USD | 19,620.00 USD | 0.00 USD |
| `1D` | `0.3125` | 14,270,000.00 USD | 0.00 USD | 14,270,000.00 USD | 12,740.00 USD | 13,530.00 USD | 0.00 USD |
| `7D` | `0.3127` | 20,000,000.00 USD | 0.00 USD | 20,000,000.00 USD | 12,250.00 USD | 54,460.00 USD | 57,690.00 USD |
| `1D` | `0.3129` | 14,250,000.00 USD | 0.00 USD | 14,250,000.00 USD | 3,990.00 USD | 28,470.00 USD | 29,100.00 USD |
| `1D` | `0.3133` | 14,190,000.00 USD | 0.00 USD | 14,190,000.00 USD | 4,020.00 USD | 23,940.00 USD | 9,590.00 USD |
| `7D` | `0.3133` | 19,880,000.00 USD | 0.00 USD | 19,880,000.00 USD | 4,440.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3137` | 14,150,000.00 USD | 0.00 USD | 14,150,000.00 USD | 4,590.00 USD | 10,610.00 USD | 0.00 USD |
| `7D` | `0.3139` | 19,870,000.00 USD | 0.00 USD | 19,870,000.00 USD | 3,330.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3141` | 14,130,000.00 USD | 0.00 USD | 14,130,000.00 USD | 6,900.00 USD | 0.00 USD | 9,540.00 USD |
| `1D` | `0.3145` | 14,120,000.00 USD | 0.00 USD | 14,120,000.00 USD | 1,910.00 USD | 5,900.00 USD | 0.00 USD |
| `7D` | `0.3145` | 19,870,000.00 USD | 0.00 USD | 19,870,000.00 USD | 247,920.00 USD | 51,270.00 USD | 17,870.00 USD |
| `1D` | `0.3149` | 14,110,000.00 USD | 0.00 USD | 14,110,000.00 USD | 1,570.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3151` | 19,550,000.00 USD | 0.00 USD | 19,550,000.00 USD | 204,770.00 USD | 23,130.00 USD | 49,320.00 USD |
| `1D` | `0.3153` | 14,110,000.00 USD | 0.00 USD | 14,110,000.00 USD | 29,750.00 USD | 25,600.00 USD | 0.00 USD |
| `1D` | `0.3157` | 14,050,000.00 USD | 0.00 USD | 14,050,000.00 USD | 12,120.00 USD | 1,830.00 USD | 16,240.00 USD |
| `7D` | `0.3157` | 19,280,000.00 USD | 0.00 USD | 19,280,000.00 USD | 393,880.00 USD | 93,740.00 USD | 60,300.00 USD |
| `1D` | `0.3161` | 14,020,000.00 USD | 0.00 USD | 14,020,000.00 USD | 4,260.00 USD | 2,990.00 USD | 0.00 USD |
| `7D` | `0.3163` | 18,730,000.00 USD | 0.00 USD | 18,730,000.00 USD | 495,020.00 USD | 174,600.00 USD | 189,520.00 USD |
| `1D` | `0.3165` | 14,010,000.00 USD | 0.00 USD | 14,010,000.00 USD | 45,260.00 USD | 30,980.00 USD | 9,000.00 USD |
| `1D` | `0.3169` | 13,930,000.00 USD | 0.00 USD | 13,930,000.00 USD | 1,090.00 USD | 10,820.00 USD | 20,780.00 USD |
| `7D` | `0.3169` | 17,870,000.00 USD | 0.00 USD | 17,870,000.00 USD | 417,170.00 USD | 104,590.00 USD | 135,950.00 USD |
| `1D` | `0.3173` | 13,900,000.00 USD | 0.00 USD | 13,900,000.00 USD | 25,580.00 USD | 33,870.00 USD | 27,630.00 USD |
| `7D` | `0.3175` | 17,210,000.00 USD | 0.00 USD | 17,210,000.00 USD | 140,810.00 USD | 53,470.00 USD | 69,280.00 USD |
| `1D` | `0.3177` | 13,810,000.00 USD | 0.00 USD | 13,810,000.00 USD | 47,770.00 USD | 8,980.00 USD | 30,890.00 USD |
| `1D` | `0.3181` | 13,720,000.00 USD | 0.00 USD | 13,720,000.00 USD | 260,170.00 USD | 41,280.00 USD | 69,790.00 USD |
| `7D` | `0.3181` | 16,950,000.00 USD | 0.00 USD | 16,950,000.00 USD | 738,240.00 USD | 76,910.00 USD | 182,330.00 USD |
| `1D` | `0.3185` | 13,350,000.00 USD | 0.00 USD | 13,350,000.00 USD | 153,950.00 USD | 52,920.00 USD | 51,330.00 USD |
| `7D` | `0.3187` | 15,950,000.00 USD | 0.00 USD | 15,950,000.00 USD | 407,530.00 USD | 97,820.00 USD | 24,770.00 USD |
| `1D` | `0.3189` | 13,090,000.00 USD | 0.00 USD | 13,090,000.00 USD | 172,980.00 USD | 5,580.00 USD | 48,660.00 USD |
| `1D` | `0.3193` | 12,860,000.00 USD | 0.00 USD | 12,860,000.00 USD | 154,490.00 USD | 107,560.00 USD | 180,830.00 USD |
| `7D` | `0.3193` | 15,420,000.00 USD | 0.00 USD | 15,420,000.00 USD | 180,550.00 USD | 123,840.00 USD | 247,300.00 USD |
| `1D` | `0.3197` | 12,420,000.00 USD | 0.00 USD | 12,420,000.00 USD | 74,370.00 USD | 118,340.00 USD | 160,310.00 USD |
| `7D` | `0.3199` | 14,870,000.00 USD | 0.00 USD | 14,870,000.00 USD | 0.00 USD | 191,160.00 USD | 267,030.00 USD |
| `1D` | `0.3201` | 12,070,000.00 USD | 0.00 USD | 12,070,000.00 USD | 208,440.00 USD | 48,100.00 USD | 111,260.00 USD |
| `1D` | `0.3205` | 11,700,000.00 USD | 0.00 USD | 11,700,000.00 USD | 163,900.00 USD | 31,270.00 USD | 102,160.00 USD |
| `7D` | `0.3205` | 14,410,000.00 USD | 0.00 USD | 14,410,000.00 USD | 167,490.00 USD | 59,200.00 USD | 130,760.00 USD |
| `1D` | `0.3209` | 11,400,000.00 USD | 0.00 USD | 11,400,000.00 USD | 88,570.00 USD | 29,040.00 USD | 54,070.00 USD |
| `7D` | `0.3211` | 14,050,000.00 USD | 0.00 USD | 14,050,000.00 USD | 568,110.00 USD | 135,070.00 USD | 244,340.00 USD |
| `1D` | `0.3213` | 11,230,000.00 USD | 0.00 USD | 11,230,000.00 USD | 54,680.00 USD | 30,340.00 USD | 107,830.00 USD |
| `1D` | `0.3217` | 11,040,000.00 USD | 0.00 USD | 11,040,000.00 USD | 5,980.00 USD | 33,860.00 USD | 146,990.00 USD |
| `7D` | `0.3217` | 13,110,000.00 USD | 0.00 USD | 13,110,000.00 USD | 285,190.00 USD | 58,690.00 USD | 107,900.00 USD |
| `1D` | `0.3221` | 10,850,000.00 USD | 0.00 USD | 10,850,000.00 USD | 97,900.00 USD | 33,430.00 USD | 72,520.00 USD |
| `7D` | `0.3223` | 12,650,000.00 USD | 0.00 USD | 12,650,000.00 USD | 643,460.00 USD | 265,170.00 USD | 156,030.00 USD |
| `1D` | `0.3225` | 10,650,000.00 USD | 0.00 USD | 10,650,000.00 USD | 70,750.00 USD | 33,350.00 USD | 202,490.00 USD |
| `1D` | `0.3229` | 10,340,000.00 USD | 0.00 USD | 10,340,000.00 USD | 91,010.00 USD | 55,060.00 USD | 129,350.00 USD |
| `7D` | `0.3229` | 11,590,000.00 USD | 0.00 USD | 11,590,000.00 USD | 858,070.00 USD | 283,650.00 USD | 518,610.00 USD |
| `1D` | `0.3233` | 10,070,000.00 USD | 0.00 USD | 10,070,000.00 USD | 56,470.00 USD | 35,600.00 USD | 49,900.00 USD |
| `7D` | `0.3235` | 9,930,000.00 USD | 0.00 USD | 9,930,000.00 USD | 709,160.00 USD | 228,450.00 USD | 359,100.00 USD |
| `1D` | `0.3237` | 9,920,000.00 USD | 0.00 USD | 9,920,000.00 USD | 6,420.00 USD | 83,630.00 USD | 171,270.00 USD |
| `1D` | `0.3241` | 9,660,000.00 USD | 0.00 USD | 9,660,000.00 USD | 966.93 USD | 27,720.00 USD | 119,400.00 USD |
| `7D` | `0.3241` | 8,630,000.00 USD | 0.00 USD | 8,630,000.00 USD | 432,660.00 USD | 149,860.00 USD | 138,560.00 USD |
| `1D` | `0.3245` | 9,520,000.00 USD | 0.00 USD | 9,520,000.00 USD | 256,740.00 USD | 54,650.00 USD | 265,030.00 USD |
| `7D` | `0.3247` | 7,910,000.00 USD | 0.00 USD | 7,910,000.00 USD | 846,180.00 USD | 127,310.00 USD | 353,590.00 USD |
| `1D` | `0.3249` | 8,940,000.00 USD | 0.00 USD | 8,940,000.00 USD | 818,640.00 USD | 91,640.00 USD | 179,470.00 USD |
| `1D` | `0.3253` | 7,850,000.00 USD | 0.00 USD | 7,850,000.00 USD | 217,740.00 USD | 107,140.00 USD | 423,830.00 USD |
| `7D` | `0.3253` | 6,580,000.00 USD | 0.00 USD | 6,580,000.00 USD | 1,220,000.00 USD | 137,440.00 USD | 241,690.00 USD |
| `1D` | `0.3257` | 7,100,000.00 USD | 0.00 USD | 7,100,000.00 USD | 542,240.00 USD | 48,220.00 USD | 229,640.00 USD |
| `7D` | `0.3259` | 4,980,000.00 USD | 0.00 USD | 4,980,000.00 USD | 306,910.00 USD | 288,370.00 USD | 503,650.00 USD |
| `1D` | `0.3261` | 6,280,000.00 USD | 0.00 USD | 6,280,000.00 USD | 150,120.00 USD | 371,060.00 USD | 555,160.00 USD |
| `1D` | `0.3265` | 5,200,000.00 USD | 0.00 USD | 5,200,000.00 USD | 65,640.00 USD | 156,570.00 USD | 345,910.00 USD |
| `7D` | `0.3265` | 3,880,000.00 USD | 0.00 USD | 3,880,000.00 USD | 80,120.00 USD | 324,810.00 USD | 500,270.00 USD |
| `1D` | `0.3269` | 4,640,000.00 USD | 0.00 USD | 4,640,000.00 USD | 200,120.00 USD | 143,860.00 USD | 378,850.00 USD |
| `7D` | `0.3271` | 2,980,000.00 USD | 0.00 USD | 2,980,000.00 USD | 320,700.00 USD | 138,680.00 USD | 261,530.00 USD |
| `1D` | `0.3273` | 3,910,000.00 USD | 0.00 USD | 3,910,000.00 USD | 38,550.00 USD | 24,720.00 USD | 174,670.00 USD |
| `1D` | `0.3277` | 3,680,000.00 USD | 0.00 USD | 3,680,000.00 USD | 317,170.00 USD | 71,740.00 USD | 161,500.00 USD |
| `7D` | `0.3277` | 2,260,000.00 USD | 0.00 USD | 2,260,000.00 USD | 0.00 USD | 29,390.00 USD | 85,620.00 USD |
| `1D` | `0.3281` | 3,120,000.00 USD | 0.00 USD | 3,120,000.00 USD | 106,720.00 USD | 57,800.00 USD | 120,850.00 USD |
| `7D` | `0.3283` | 2,140,000.00 USD | 0.00 USD | 2,140,000.00 USD | 89,030.00 USD | 61,340.00 USD | 275,050.00 USD |
| `1D` | `0.3285` | 2,840,000.00 USD | 0.00 USD | 2,840,000.00 USD | 0.00 USD | 48,460.00 USD | 79,430.00 USD |
| `1D` | `0.3289` | 2,710,000.00 USD | 0.00 USD | 2,710,000.00 USD | 155,850.00 USD | 21,810.00 USD | 155,080.00 USD |
| `7D` | `0.3289` | 1,720,000.00 USD | 0.00 USD | 1,720,000.00 USD | 0.00 USD | 180,260.00 USD | 105,320.00 USD |
| `1D` | `0.3293` | 2,380,000.00 USD | 0.00 USD | 2,380,000.00 USD | 977.29 USD | 60,450.00 USD | 165,140.00 USD |
| `7D` | `0.3295` | 1,430,000.00 USD | 0.00 USD | 1,430,000.00 USD | 254,700.00 USD | 83,080.00 USD | 279,140.00 USD |
| `1D` | `0.3297` | 2,150,000.00 USD | 0.00 USD | 2,150,000.00 USD | 166,310.00 USD | 18,090.00 USD | 0.00 USD |
| `1D` | `0.3301` | 1,970,000.00 USD | 0.00 USD | 1,970,000.00 USD | 36,460.00 USD | 58,700.00 USD | 30,950.00 USD |
| `7D` | `0.3301` | 815,180.00 USD | 0.00 USD | 815,180.00 USD | 185,020.00 USD | 47,610.00 USD | 0.00 USD |
| `1D` | `0.3305` | 1,840,000.00 USD | 0.00 USD | 1,840,000.00 USD | 112,020.00 USD | 33,940.00 USD | 74,690.00 USD |
| `7D` | `0.3307` | 582,550.00 USD | 0.00 USD | 582,550.00 USD | 167,950.00 USD | 10,690.00 USD | 294,170.00 USD |
| `1D` | `0.3309` | 1,620,000.00 USD | 0.00 USD | 1,620,000.00 USD | 11,600.00 USD | 48,170.00 USD | 444,920.00 USD |
| `1D` | `0.3313` | 1,120,000.00 USD | 0.00 USD | 1,120,000.00 USD | 61,660.00 USD | 128,440.00 USD | 183,340.00 USD |
| `7D` | `0.3313` | 109,740.00 USD | 0.00 USD | 109,740.00 USD | 0.00 USD | 50,650.00 USD | 0.00 USD |
| `1D` | `0.3317` | 742,760.00 USD | 0.00 USD | 742,760.00 USD | 27,700.00 USD | 58,950.00 USD | 0.00 USD |
| `7D` | `0.3319` | 59,090.00 USD | 0.00 USD | 59,090.00 USD | 0.00 USD | 57,890.00 USD | 0.00 USD |
| `1D` | `0.3321` | 656,110.00 USD | 0.00 USD | 656,110.00 USD | 18,060.00 USD | 23,430.00 USD | 100,730.00 USD |
| `1D` | `0.3325` | 513,880.00 USD | 0.00 USD | 513,880.00 USD | 0.00 USD | 9,670.00 USD | 0.00 USD |
| `1D` | `0.3329` | 504,220.00 USD | 0.00 USD | 504,220.00 USD | 17,980.00 USD | 0.00 USD | 39,970.00 USD |
| `1D` | `0.3333` | 446,260.00 USD | 0.00 USD | 446,260.00 USD | 43,710.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3361` | 1,200.00 USD | 0.00 USD | 1,200.00 USD | 1,200.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3369` | 402,560.00 USD | 0.00 USD | 402,560.00 USD | 72,920.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3377` | 329,640.00 USD | 0.00 USD | 329,640.00 USD | 329,640.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3380` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3385` | 125,650.00 USD | 125,650.00 USD | 0.00 USD | 125,650.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3389` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3391` | 484,990.00 USD | 484,990.00 USD | 0.00 USD | 124,670.00 USD | 0.00 USD | 234,660.00 USD |
| `7D` | `0.3397` | 1,910,000.00 USD | 1,910,000.00 USD | 0.00 USD | 257,550.00 USD | 752,550.00 USD | 410,830.00 USD |
| `1D` | `0.3401` | 220,570.00 USD | 220,570.00 USD | 0.00 USD | 0.00 USD | 15,510.00 USD | 205,050.00 USD |
| `7D` | `0.3403` | 3,580,000.00 USD | 3,580,000.00 USD | 0.00 USD | 1,200,000.00 USD | 103,630.00 USD | 376,470.00 USD |
| `1D` | `0.3405` | 554,610.00 USD | 554,610.00 USD | 0.00 USD | 0.00 USD | 14,270.00 USD | 319,770.00 USD |
| `1D` | `0.3409` | 800,040.00 USD | 800,040.00 USD | 0.00 USD | 183,630.00 USD | 34,110.00 USD | 27,700.00 USD |
| `7D` | `0.3409` | 4,060,000.00 USD | 4,060,000.00 USD | 0.00 USD | 0.00 USD | 29,390.00 USD | 446,990.00 USD |
| `1D` | `0.3413` | 1,170,000.00 USD | 1,170,000.00 USD | 0.00 USD | 279,850.00 USD | 11,360.00 USD | 80,830.00 USD |
| `7D` | `0.3415` | 4,180,000.00 USD | 4,180,000.00 USD | 0.00 USD | 0.00 USD | 35,670.00 USD | 85,620.00 USD |
| `1D` | `0.3417` | 1,980,000.00 USD | 1,980,000.00 USD | 0.00 USD | 585,390.00 USD | 25,060.00 USD | 197,540.00 USD |
| `1D` | `0.3421` | 2,090,000.00 USD | 2,090,000.00 USD | 0.00 USD | 71,180.00 USD | 39,260.00 USD | 0.00 USD |
| `7D` | `0.3421` | 4,220,000.00 USD | 4,220,000.00 USD | 0.00 USD | 0.00 USD | 43,290.00 USD | 0.00 USD |
| `1D` | `0.3425` | 2,250,000.00 USD | 2,250,000.00 USD | 0.00 USD | 0.00 USD | 159,430.00 USD | 0.00 USD |
| `7D` | `0.3427` | 4,840,000.00 USD | 4,840,000.00 USD | 0.00 USD | 0.00 USD | 229,350.00 USD | 384,460.00 USD |
| `1D` | `0.3429` | 2,520,000.00 USD | 2,520,000.00 USD | 0.00 USD | 60,980.00 USD | 120,450.00 USD | 85,070.00 USD |
| `1D` | `0.3433` | 2,820,000.00 USD | 2,820,000.00 USD | 0.00 USD | 105,330.00 USD | 167,240.00 USD | 30,950.00 USD |
| `7D` | `0.3433` | 5,130,000.00 USD | 5,130,000.00 USD | 0.00 USD | 254,700.00 USD | 38,560.00 USD | 0.00 USD |
| `1D` | `0.3437` | 3,000,000.00 USD | 3,000,000.00 USD | 0.00 USD | 0.00 USD | 117,260.00 USD | 62,980.00 USD |
| `1D` | `0.3441` | 3,050,000.00 USD | 3,050,000.00 USD | 0.00 USD | 0.00 USD | 45,070.00 USD | 0.00 USD |
| `1D` | `0.3445` | 3,180,000.00 USD | 3,180,000.00 USD | 0.00 USD | 0.00 USD | 28,520.00 USD | 106,240.00 USD |
| `7D` | `0.3445` | 5,230,000.00 USD | 5,230,000.00 USD | 0.00 USD | 103,130.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3449` | 3,550,000.00 USD | 3,550,000.00 USD | 0.00 USD | 97,620.00 USD | 92,440.00 USD | 183,340.00 USD |
| `7D` | `0.3451` | 5,320,000.00 USD | 5,320,000.00 USD | 0.00 USD | 62,830.00 USD | 28,550.00 USD | 0.00 USD |
| `1D` | `0.3453` | 3,820,000.00 USD | 3,820,000.00 USD | 0.00 USD | 130,670.00 USD | 47,460.00 USD | 84,370.00 USD |
| `1D` | `0.3457` | 4,600,000.00 USD | 4,600,000.00 USD | 0.00 USD | 170,670.00 USD | 57,370.00 USD | 553,330.00 USD |
| `7D` | `0.3457` | 5,750,000.00 USD | 5,750,000.00 USD | 0.00 USD | 62,340.00 USD | 29,340.00 USD | 332,190.00 USD |
| `1D` | `0.3461` | 5,230,000.00 USD | 5,230,000.00 USD | 0.00 USD | 198,910.00 USD | 190,690.00 USD | 242,890.00 USD |
| `7D` | `0.3463` | 6,200,000.00 USD | 6,200,000.00 USD | 0.00 USD | 0.00 USD | 250,840.00 USD | 205,410.00 USD |
| `1D` | `0.3465` | 5,480,000.00 USD | 5,480,000.00 USD | 0.00 USD | 39,870.00 USD | 67,330.00 USD | 142,350.00 USD |
| `1D` | `0.3469` | 5,680,000.00 USD | 5,680,000.00 USD | 0.00 USD | 81,330.00 USD | 42,550.00 USD | 75,450.00 USD |
| `7D` | `0.3469` | 6,530,000.00 USD | 6,530,000.00 USD | 0.00 USD | 124,720.00 USD | 51,820.00 USD | 152,060.00 USD |
| `1D` | `0.3473` | 5,740,000.00 USD | 5,740,000.00 USD | 0.00 USD | 0.00 USD | 35,130.00 USD | 31,160.00 USD |
| `7D` | `0.3475` | 6,570,000.00 USD | 6,570,000.00 USD | 0.00 USD | 0.00 USD | 40,540.00 USD | 0.00 USD |
| `1D` | `0.3477` | 5,920,000.00 USD | 5,920,000.00 USD | 0.00 USD | 51,860.00 USD | 48,500.00 USD | 77,670.00 USD |
| `1D` | `0.3481` | 6,070,000.00 USD | 6,070,000.00 USD | 0.00 USD | 53,360.00 USD | 29,570.00 USD | 64,980.00 USD |
| `7D` | `0.3481` | 6,660,000.00 USD | 6,660,000.00 USD | 0.00 USD | 6,440.00 USD | 32,530.00 USD | 42,810.00 USD |
| `1D` | `0.3485` | 6,170,000.00 USD | 6,170,000.00 USD | 0.00 USD | 9,350.00 USD | 16,180.00 USD | 76,450.00 USD |
| `7D` | `0.3487` | 6,690,000.00 USD | 6,690,000.00 USD | 0.00 USD | 8,310.00 USD | 21,650.00 USD | 0.00 USD |
| `1D` | `0.3489` | 6,300,000.00 USD | 6,300,000.00 USD | 0.00 USD | 41,500.00 USD | 23,850.00 USD | 61,240.00 USD |
| `1D` | `0.3493` | 6,340,000.00 USD | 6,340,000.00 USD | 0.00 USD | 3,620.00 USD | 33,350.00 USD | 0.00 USD |
| `7D` | `0.3493` | 6,980,000.00 USD | 6,980,000.00 USD | 0.00 USD | 10,490.00 USD | 93,150.00 USD | 192,230.00 USD |
| `1D` | `0.3497` | 6,870,000.00 USD | 6,870,000.00 USD | 0.00 USD | 32,290.00 USD | 0.00 USD | 497,210.00 USD |
| `7D` | `0.3499` | 7,120,000.00 USD | 7,120,000.00 USD | 0.00 USD | 139,880.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3501` | 6,980,000.00 USD | 6,980,000.00 USD | 0.00 USD | 52,670.00 USD | 9,040.00 USD | 50,760.00 USD |
| `1D` | `0.3505` | 7,120,000.00 USD | 7,120,000.00 USD | 0.00 USD | 74,220.00 USD | 33,830.00 USD | 31,490.00 USD |
| `7D` | `0.3505` | 7,150,000.00 USD | 7,150,000.00 USD | 0.00 USD | 11,960.00 USD | 19,280.00 USD | 0.00 USD |
| `1D` | `0.3509` | 7,140,000.00 USD | 7,140,000.00 USD | 0.00 USD | 2,790.00 USD | 16,810.00 USD | 0.00 USD |
| `7D` | `0.3511` | 8,110,000.00 USD | 8,110,000.00 USD | 0.00 USD | 690,500.00 USD | 0.00 USD | 271,800.00 USD |
| `1D` | `0.3513` | 7,210,000.00 USD | 7,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 76,540.00 USD |
| `1D` | `0.3517` | 7,370,000.00 USD | 7,370,000.00 USD | 0.00 USD | 52,740.00 USD | 5,720.00 USD | 101,300.00 USD |
| `1D` | `0.3521` | 7,510,000.00 USD | 7,510,000.00 USD | 0.00 USD | 47,300.00 USD | 21,980.00 USD | 69,070.00 USD |
| `7D` | `0.3523` | 8,530,000.00 USD | 8,530,000.00 USD | 0.00 USD | 277,410.00 USD | 28,950.00 USD | 107,430.00 USD |
| `1D` | `0.3525` | 7,570,000.00 USD | 7,570,000.00 USD | 0.00 USD | 13,010.00 USD | 17,990.00 USD | 28,910.00 USD |
| `1D` | `0.3529` | 7,730,000.00 USD | 7,730,000.00 USD | 0.00 USD | 102,610.00 USD | 57,540.00 USD | 0.00 USD |
| `1D` | `0.3533` | 7,960,000.00 USD | 7,960,000.00 USD | 0.00 USD | 76,080.00 USD | 44,040.00 USD | 108,090.00 USD |
| `7D` | `0.3535` | 8,800,000.00 USD | 8,800,000.00 USD | 0.00 USD | 4,830.00 USD | 77,960.00 USD | 187,450.00 USD |
| `1D` | `0.3537` | 8,270,000.00 USD | 8,270,000.00 USD | 0.00 USD | 83,280.00 USD | 29,120.00 USD | 195,270.00 USD |
| `1D` | `0.3541` | 8,430,000.00 USD | 8,430,000.00 USD | 0.00 USD | 83,770.00 USD | 80,430.00 USD | 0.00 USD |
| `7D` | `0.3541` | 9,730,000.00 USD | 9,730,000.00 USD | 0.00 USD | 810,900.00 USD | 118,370.00 USD | 0.00 USD |
| `1D` | `0.3545` | 8,550,000.00 USD | 8,550,000.00 USD | 0.00 USD | 5,220.00 USD | 44,140.00 USD | 69,820.00 USD |
| `7D` | `0.3547` | 10,020,000.00 USD | 10,020,000.00 USD | 0.00 USD | 5,390.00 USD | 0.00 USD | 288,450.00 USD |
| `1D` | `0.3549` | 8,610,000.00 USD | 8,610,000.00 USD | 0.00 USD | 6,350.00 USD | 53,970.00 USD | 0.00 USD |
| `1D` | `0.3553` | 8,710,000.00 USD | 8,710,000.00 USD | 0.00 USD | 21,530.00 USD | 24,430.00 USD | 47,950.00 USD |
| `7D` | `0.3553` | 10,150,000.00 USD | 10,150,000.00 USD | 0.00 USD | 12,710.00 USD | 117,050.00 USD | 0.00 USD |
| `1D` | `0.3557` | 8,750,000.00 USD | 8,750,000.00 USD | 0.00 USD | 853.70 USD | 38,770.00 USD | 0.00 USD |
| `7D` | `0.3559` | 10,170,000.00 USD | 10,170,000.00 USD | 0.00 USD | 13,500.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3561` | 8,880,000.00 USD | 8,880,000.00 USD | 0.00 USD | 331.60 USD | 25,000.00 USD | 106,140.00 USD |
| `1D` | `0.3565` | 8,930,000.00 USD | 8,930,000.00 USD | 0.00 USD | 3,070.00 USD | 11,630.00 USD | 39,520.00 USD |
| `7D` | `0.3565` | 10,210,000.00 USD | 10,210,000.00 USD | 0.00 USD | 0.00 USD | 43,060.00 USD | 0.00 USD |
| `1D` | `0.3569` | 8,940,000.00 USD | 8,940,000.00 USD | 0.00 USD | 1,450.00 USD | 6,920.00 USD | 0.00 USD |
| `1D` | `0.3573` | 9,080,000.00 USD | 9,080,000.00 USD | 0.00 USD | 131,970.00 USD | 9,250.00 USD | 0.00 USD |
| `1D` | `0.3577` | 9,120,000.00 USD | 9,120,000.00 USD | 0.00 USD | 31,960.00 USD | 9,130.00 USD | 0.00 USD |
| `7D` | `0.3577` | 10,330,000.00 USD | 10,330,000.00 USD | 0.00 USD | 124,630.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3581` | 9,160,000.00 USD | 9,160,000.00 USD | 0.00 USD | 3,560.00 USD | 0.00 USD | 38,950.00 USD |
| `7D` | `0.3583` | 10,470,000.00 USD | 10,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 135,900.00 USD |
| `1D` | `0.3585` | 9,200,000.00 USD | 9,200,000.00 USD | 0.00 USD | 18,570.00 USD | 14,930.00 USD | 0.00 USD |
| `1D` | `0.3589` | 9,220,000.00 USD | 9,220,000.00 USD | 0.00 USD | 3,780.00 USD | 15,750.00 USD | 0.00 USD |
| `7D` | `0.3589` | 10,840,000.00 USD | 10,840,000.00 USD | 0.00 USD | 0.00 USD | 50,650.00 USD | 320,430.00 USD |
| `1D` | `0.3593` | 9,420,000.00 USD | 9,420,000.00 USD | 0.00 USD | 66,040.00 USD | 0.00 USD | 133,180.00 USD |
| `7D` | `0.3595` | 10,990,000.00 USD | 10,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 146,290.00 USD |
| `1D` | `0.3597` | 9,520,000.00 USD | 9,520,000.00 USD | 0.00 USD | 91,900.00 USD | 12,460.00 USD | 0.00 USD |
| `1D` | `0.3601` | 9,720,000.00 USD | 9,720,000.00 USD | 0.00 USD | 1,360.00 USD | 36,520.00 USD | 163,110.00 USD |
| `7D` | `0.3601` | 11,490,000.00 USD | 11,490,000.00 USD | 0.00 USD | 4,230.00 USD | 161,200.00 USD | 338,540.00 USD |
| `1D` | `0.3605` | 9,910,000.00 USD | 9,910,000.00 USD | 0.00 USD | 61,580.00 USD | 32,860.00 USD | 94,650.00 USD |
| `7D` | `0.3607` | 11,890,000.00 USD | 11,890,000.00 USD | 0.00 USD | 330,010.00 USD | 68,030.00 USD | 0.00 USD |
| `1D` | `0.3609` | 10,150,000.00 USD | 10,150,000.00 USD | 0.00 USD | 75,390.00 USD | 25,740.00 USD | 133,760.00 USD |
| `1D` | `0.3613` | 10,420,000.00 USD | 10,420,000.00 USD | 0.00 USD | 11,270.00 USD | 59,640.00 USD | 203,600.00 USD |
| `7D` | `0.3613` | 12,580,000.00 USD | 12,580,000.00 USD | 0.00 USD | 73,920.00 USD | 330,040.00 USD | 288,930.00 USD |
| `1D` | `0.3617` | 10,800,000.00 USD | 10,800,000.00 USD | 0.00 USD | 225,910.00 USD | 50,630.00 USD | 104,310.00 USD |
| `7D` | `0.3619` | 12,790,000.00 USD | 12,790,000.00 USD | 0.00 USD | 3,790.00 USD | 209,940.00 USD | 0.00 USD |
| `1D` | `0.3621` | 11,090,000.00 USD | 11,090,000.00 USD | 0.00 USD | 143,010.00 USD | 75,820.00 USD | 71,510.00 USD |
| `1D` | `0.3625` | 11,240,000.00 USD | 11,240,000.00 USD | 0.00 USD | 99,950.00 USD | 49,330.00 USD | 0.00 USD |
| `7D` | `0.3625` | 12,990,000.00 USD | 12,990,000.00 USD | 0.00 USD | 2,300.00 USD | 191,880.00 USD | 0.00 USD |
| `1D` | `0.3629` | 12,470,000.00 USD | 12,470,000.00 USD | 0.00 USD | 1,120,000.00 USD | 35,410.00 USD | 79,610.00 USD |
| `7D` | `0.3631` | 13,100,000.00 USD | 13,100,000.00 USD | 0.00 USD | 738.08 USD | 114,740.00 USD | 0.00 USD |
| `1D` | `0.3633` | 12,890,000.00 USD | 12,890,000.00 USD | 0.00 USD | 144,090.00 USD | 72,670.00 USD | 199,780.00 USD |
| `1D` | `0.3637` | 13,140,000.00 USD | 13,140,000.00 USD | 0.00 USD | 183,690.00 USD | 65,110.00 USD | 0.00 USD |
| `7D` | `0.3637` | 13,130,000.00 USD | 13,130,000.00 USD | 0.00 USD | 1,090.00 USD | 21,530.00 USD | 0.00 USD |
| `1D` | `0.3641` | 13,510,000.00 USD | 13,510,000.00 USD | 0.00 USD | 85,150.00 USD | 206,820.00 USD | 76,240.00 USD |
| `7D` | `0.3643` | 13,920,000.00 USD | 13,920,000.00 USD | 0.00 USD | 1,580.00 USD | 0.00 USD | 789,140.00 USD |
| `1D` | `0.3645` | 13,820,000.00 USD | 13,820,000.00 USD | 0.00 USD | 255,500.00 USD | 16,650.00 USD | 35,280.00 USD |
| `1D` | `0.3649` | 14,170,000.00 USD | 14,170,000.00 USD | 0.00 USD | 96,700.00 USD | 59,680.00 USD | 195,820.00 USD |
| `7D` | `0.3649` | 14,100,000.00 USD | 14,100,000.00 USD | 0.00 USD | 182,150.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3653` | 14,660,000.00 USD | 14,660,000.00 USD | 0.00 USD | 303,010.00 USD | 19,500.00 USD | 165,330.00 USD |
| `7D` | `0.3655` | 14,890,000.00 USD | 14,890,000.00 USD | 0.00 USD | 677,860.00 USD | 112,770.00 USD | 0.00 USD |
| `1D` | `0.3657` | 15,190,000.00 USD | 15,190,000.00 USD | 0.00 USD | 218,660.00 USD | 149,310.00 USD | 163,370.00 USD |
| `1D` | `0.3661` | 15,650,000.00 USD | 15,650,000.00 USD | 0.00 USD | 277,650.00 USD | 88,330.00 USD | 96,250.00 USD |
| `7D` | `0.3661` | 15,890,000.00 USD | 15,890,000.00 USD | 0.00 USD | 691,690.00 USD | 66,940.00 USD | 238,480.00 USD |
| `1D` | `0.3665` | 16,300,000.00 USD | 16,300,000.00 USD | 0.00 USD | 468,570.00 USD | 117,940.00 USD | 66,840.00 USD |
| `7D` | `0.3667` | 16,510,000.00 USD | 16,510,000.00 USD | 0.00 USD | 424,170.00 USD | 34,510.00 USD | 166,250.00 USD |
| `1D` | `0.3669` | 16,710,000.00 USD | 16,710,000.00 USD | 0.00 USD | 98,960.00 USD | 26,330.00 USD | 281,260.00 USD |
| `1D` | `0.3673` | 17,020,000.00 USD | 17,020,000.00 USD | 0.00 USD | 52,240.00 USD | 102,840.00 USD | 158,510.00 USD |
| `7D` | `0.3673` | 17,200,000.00 USD | 17,200,000.00 USD | 0.00 USD | 511,100.00 USD | 53,040.00 USD | 122,410.00 USD |
| `1D` | `0.3677` | 17,750,000.00 USD | 17,750,000.00 USD | 0.00 USD | 494,570.00 USD | 41,730.00 USD | 191,130.00 USD |
| `7D` | `0.3679` | 17,460,000.00 USD | 17,460,000.00 USD | 0.00 USD | 259,090.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3681` | 18,250,000.00 USD | 18,250,000.00 USD | 0.00 USD | 310,830.00 USD | 87,330.00 USD | 103,470.00 USD |
| `1D` | `0.3685` | 18,820,000.00 USD | 18,820,000.00 USD | 0.00 USD | 327,450.00 USD | 152,380.00 USD | 93,220.00 USD |
| `7D` | `0.3685` | 17,640,000.00 USD | 17,640,000.00 USD | 0.00 USD | 1,610.00 USD | 102,650.00 USD | 72,350.00 USD |
| `1D` | `0.3689` | 19,340,000.00 USD | 19,340,000.00 USD | 0.00 USD | 404,300.00 USD | 56,330.00 USD | 52,150.00 USD |
| `7D` | `0.3691` | 18,040,000.00 USD | 18,040,000.00 USD | 0.00 USD | 147,650.00 USD | 261,530.00 USD | 0.00 USD |
| `1D` | `0.3693` | 19,450,000.00 USD | 19,450,000.00 USD | 0.00 USD | 79,910.00 USD | 4,540.00 USD | 23,760.00 USD |
| `1D` | `0.3697` | 19,700,000.00 USD | 19,700,000.00 USD | 0.00 USD | 155,550.00 USD | 83,650.00 USD | 17,010.00 USD |
| `7D` | `0.3697` | 18,280,000.00 USD | 18,280,000.00 USD | 0.00 USD | 0.00 USD | 175,510.00 USD | 55,830.00 USD |
| `1D` | `0.3701` | 20,450,000.00 USD | 20,450,000.00 USD | 0.00 USD | 527,250.00 USD | 196,170.00 USD | 27,870.00 USD |
| `7D` | `0.3703` | 18,330,000.00 USD | 18,330,000.00 USD | 0.00 USD | 50,940.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3705` | 21,270,000.00 USD | 21,270,000.00 USD | 0.00 USD | 249,050.00 USD | 8,320.00 USD | 560,920.00 USD |
| `1D` | `0.3709` | 21,420,000.00 USD | 21,420,000.00 USD | 0.00 USD | 109,790.00 USD | 24,570.00 USD | 12,600.00 USD |
| `7D` | `0.3709` | 18,330,000.00 USD | 18,330,000.00 USD | 0.00 USD | 1,880.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3713` | 22,790,000.00 USD | 22,790,000.00 USD | 0.00 USD | 482,060.00 USD | 90,010.00 USD | 804,260.00 USD |
| `7D` | `0.3715` | 18,730,000.00 USD | 18,730,000.00 USD | 0.00 USD | 3,890.00 USD | 0.00 USD | 394,570.00 USD |
| `1D` | `0.3717` | 23,330,000.00 USD | 23,330,000.00 USD | 0.00 USD | 44,820.00 USD | 220,760.00 USD | 269,700.00 USD |
| `1D` | `0.3721` | 23,490,000.00 USD | 23,490,000.00 USD | 0.00 USD | 9,150.00 USD | 62,750.00 USD | 85,090.00 USD |
| `7D` | `0.3721` | 19,480,000.00 USD | 19,480,000.00 USD | 0.00 USD | 1,320.00 USD | 0.00 USD | 747,740.00 USD |
| `1D` | `0.3725` | 24,570,000.00 USD | 24,570,000.00 USD | 0.00 USD | 511,460.00 USD | 31,730.00 USD | 537,700.00 USD |
| `7D` | `0.3727` | 19,760,000.00 USD | 19,760,000.00 USD | 0.00 USD | 213,190.00 USD | 0.00 USD | 66,870.00 USD |
| `1D` | `0.3729` | 25,080,000.00 USD | 25,080,000.00 USD | 0.00 USD | 33,900.00 USD | 128,180.00 USD | 349,570.00 USD |
| `1D` | `0.3733` | 25,860,000.00 USD | 25,860,000.00 USD | 0.00 USD | 105,050.00 USD | 23,870.00 USD | 655,100.00 USD |
| `7D` | `0.3733` | 19,940,000.00 USD | 19,940,000.00 USD | 0.00 USD | 188,670.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3737` | 26,110,000.00 USD | 26,110,000.00 USD | 0.00 USD | 154,860.00 USD | 94,700.00 USD | 0.00 USD |
| `7D` | `0.3739` | 20,420,000.00 USD | 20,420,000.00 USD | 0.00 USD | 247,740.00 USD | 7,690.00 USD | 218,010.00 USD |
| `1D` | `0.3741` | 26,630,000.00 USD | 26,630,000.00 USD | 0.00 USD | 41,360.00 USD | 71,420.00 USD | 403,580.00 USD |
| `1D` | `0.3745` | 27,000,000.00 USD | 27,000,000.00 USD | 0.00 USD | 30,710.00 USD | 35,840.00 USD | 305,620.00 USD |
| `7D` | `0.3745` | 20,820,000.00 USD | 20,820,000.00 USD | 0.00 USD | 249,860.00 USD | 115,430.00 USD | 37,210.00 USD |
| `1D` | `0.3749` | 27,770,000.00 USD | 27,770,000.00 USD | 0.00 USD | 229,090.00 USD | 20,770.00 USD | 520,920.00 USD |
| `1D` | `0.3753` | 27,940,000.00 USD | 27,940,000.00 USD | 0.00 USD | 134,010.00 USD | 0.00 USD | 31,010.00 USD |
| `1D` | `0.3756` | 27,960,000.00 USD | 27,960,000.00 USD | 0.00 USD | 23,190.00 USD | 1,940.00 USD | 0.00 USD |
| `7D` | `0.3757` | 21,120,000.00 USD | 21,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 302,240.00 USD |
| `7D` | `0.3763` | 21,300,000.00 USD | 21,300,000.00 USD | 0.00 USD | 35,610.00 USD | 92,380.00 USD | 50,200.00 USD |
| `7D` | `0.3775` | 21,300,000.00 USD | 21,300,000.00 USD | 0.00 USD | 897.53 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3781` | 21,330,000.00 USD | 21,330,000.00 USD | 0.00 USD | 23,800.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3787` | 21,470,000.00 USD | 21,470,000.00 USD | 0.00 USD | 89,270.00 USD | 3,620.00 USD | 54,360.00 USD |
| `7D` | `0.3793` | 21,940,000.00 USD | 21,940,000.00 USD | 0.00 USD | 27,760.00 USD | 0.00 USD | 437,170.00 USD |
| `7D` | `0.3799` | 21,940,000.00 USD | 21,940,000.00 USD | 0.00 USD | 4,000.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3811` | 21,980,000.00 USD | 21,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 37,490.00 USD |
| `7D` | `0.3817` | 22,160,000.00 USD | 22,160,000.00 USD | 0.00 USD | 156,690.00 USD | 19,620.00 USD | 0.00 USD |
| `7D` | `0.3823` | 22,270,000.00 USD | 22,270,000.00 USD | 0.00 USD | 0.00 USD | 54,460.00 USD | 57,690.00 USD |
| `7D` | `0.3835` | 22,270,000.00 USD | 22,270,000.00 USD | 0.00 USD | 880.35 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3853` | 22,270,000.00 USD | 22,270,000.00 USD | 0.00 USD | 768.95 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3859` | 22,340,000.00 USD | 22,340,000.00 USD | 0.00 USD | 71,390.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3865` | 22,500,000.00 USD | 22,500,000.00 USD | 0.00 USD | 112,700.00 USD | 45,110.00 USD | 0.00 USD |
| `7D` | `0.3877` | 22,620,000.00 USD | 22,620,000.00 USD | 0.00 USD | 123,270.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3883` | 22,670,000.00 USD | 22,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 48,960.00 USD |
| `7D` | `0.3889` | 22,770,000.00 USD | 22,770,000.00 USD | 0.00 USD | 103,020.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3895` | 22,810,000.00 USD | 22,810,000.00 USD | 0.00 USD | 0.00 USD | 41,060.00 USD | 0.00 USD |
| `7D` | `0.3901` | 22,870,000.00 USD | 22,870,000.00 USD | 0.00 USD | 59,060.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3907` | 22,990,000.00 USD | 22,990,000.00 USD | 0.00 USD | 0.00 USD | 50,210.00 USD | 63,420.00 USD |
| `7D` | `0.3919` | 22,990,000.00 USD | 22,990,000.00 USD | 0.00 USD | 2,670.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3925` | 23,150,000.00 USD | 23,150,000.00 USD | 0.00 USD | 447.70 USD | 1,190.00 USD | 157,830.00 USD |
| `7D` | `0.3931` | 23,180,000.00 USD | 23,180,000.00 USD | 0.00 USD | 24,750.00 USD | 2,840.00 USD | 2,800.00 USD |
| `7D` | `0.3937` | 23,210,000.00 USD | 23,210,000.00 USD | 0.00 USD | 22,020.00 USD | 1,070.00 USD | 5,410.00 USD |
| `7D` | `0.3943` | 23,240,000.00 USD | 23,240,000.00 USD | 0.00 USD | 24,650.00 USD | 3,090.00 USD | 784.19 USD |
| `7D` | `0.3949` | 23,370,000.00 USD | 23,370,000.00 USD | 0.00 USD | 110,030.00 USD | 8,290.00 USD | 18,490.00 USD |
| `7D` | `0.3955` | 23,600,000.00 USD | 23,600,000.00 USD | 0.00 USD | 107,070.00 USD | 8,610.00 USD | 110,780.00 USD |
| `7D` | `0.3961` | 23,780,000.00 USD | 23,780,000.00 USD | 0.00 USD | 122,560.00 USD | 54,030.00 USD | 7,040.00 USD |
| `7D` | `0.3967` | 23,810,000.00 USD | 23,810,000.00 USD | 0.00 USD | 12,400.00 USD | 6,010.00 USD | 4,840.00 USD |
| `7D` | `0.3973` | 23,950,000.00 USD | 23,950,000.00 USD | 0.00 USD | 16,600.00 USD | 1,440.00 USD | 123,860.00 USD |
| `7D` | `0.3979` | 24,060,000.00 USD | 24,060,000.00 USD | 0.00 USD | 57,520.00 USD | 38,460.00 USD | 11,500.00 USD |
| `7D` | `0.3985` | 24,090,000.00 USD | 24,090,000.00 USD | 0.00 USD | 23,360.00 USD | 3,160.00 USD | 10,200.00 USD |
| `7D` | `0.3991` | 24,130,000.00 USD | 24,130,000.00 USD | 0.00 USD | 0.00 USD | 16,880.00 USD | 24,490.00 USD |
| `7D` | `0.3997` | 24,160,000.00 USD | 24,160,000.00 USD | 0.00 USD | 0.00 USD | 27,240.00 USD | 0.00 USD |
| `7D` | `0.4001` | 24,170,000.00 USD | 24,170,000.00 USD | 0.00 USD | 0.00 USD | 7,690.00 USD | 0.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `433.06M` | Total OI Tokens: `1,274,641,604.7 TRX`
  * 1h OI Change: `+3.98%` | 4h OI Change: `+6.54%` | 24h OI Change: `+51.31%`
  * Exchange Breakdown: Binance=`108.55M` | Bybit=`86.28M` | OKX=`27.82M` | Hyperliquid=`19.31M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `-100.09K` | Last 24h: `-632.70K` | Last 3d: `-621.37K` | Last 7d: `-893.87K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `-0.0594%` | **USDT OKX** | `-0.3669%` |
| **USDT Bybit** | `0.0747%` | **USDT KuCoin** | `-0.0575%` |
| **USDT MEXC** | `-0.0576%` | **USDT BingX** | `0.0790%` |
| **USDT Gate** | `-0.1674%` | **USDT Bitget** | `-0.2079%` |
| **CoinM Binance** | `-0.1150%` | **CoinM OKX** | `-` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `TRX` | `53.78%` | `46.22%` | `1.16` | 5,580,000.00 USD |
| `15M` | `Binance` | `59.68%` | `40.32%` | `1.48` | 1,720,000.00 USD |
| `15M` | `OKX` | `57.96%` | `42.04%` | `1.38` | 493,390.00 USD |
| `15M` | `Bybit` | `61.03%` | `38.97%` | `1.57` | 561,810.00 USD |
| `15M` | `KuCoin` | `45.77%` | `54.23%` | `0.84` | 213,250.00 USD |
| `15M` | `Gate` | `72.26%` | `27.74%` | `2.60` | 116,920.00 USD |
| `15M` | `Bitget` | `66.42%` | `33.58%` | `1.98` | 151,360.00 USD |
| `15M` | `BingX` | `52.21%` | `47.79%` | `1.09` | 141,020.00 USD |
| `15M` | `MEXC` | `67.36%` | `32.64%` | `2.06` | 680,010.00 USD |
| `15M` | `Bitunix` | `48.96%` | `51.04%` | `0.96` | 139,970.00 USD |
| `15M` | `Hyperliquid` | `34.94%` | `65.06%` | `0.54` | 67,230.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `46.2%` | `53.8%` | `0.86` | 845,100.00 USD |
| `15M` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `WhiteBIT` | `0%` | `100%` | `0.00` | 364,680.00 USD |
| `15M` | `HTX` | `50.51%` | `49.49%` | `1.02` | 21,970.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `69.62%` | `30.38%` | `2.29` | 46,960.00 USD |
| `15M` | `Aster` | `3.17%` | `96.83%` | `0.03` | 7,530.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `0%` | `100%` | `0.00` | 379.26 USD |
| `15M` | `Whale Positions` | `59.68%` | `40.32%` | `1.48` | 1,720,000.00 USD |
| `15M` | `Global Accounts` | `53.78%` | `46.22%` | `1.16` | 5,580,000.00 USD |
| `1H` | `TRX` | `43.74%` | `56.26%` | `0.78` | 58,160,000.00 USD |
| `1H` | `Binance` | `43.7%` | `56.3%` | `0.78` | 31,640,000.00 USD |
| `1H` | `OKX` | `52.98%` | `47.02%` | `1.13` | 6,060,000.00 USD |
| `1H` | `Bybit` | `32.78%` | `67.22%` | `0.49` | 6,610,000.00 USD |
| `1H` | `KuCoin` | `52.68%` | `47.32%` | `1.11` | 782,180.00 USD |
| `1H` | `Gate` | `47.95%` | `52.05%` | `0.92` | 3,000,000.00 USD |
| `1H` | `Bitget` | `46.48%` | `53.52%` | `0.87` | 1,320,000.00 USD |
| `1H` | `BingX` | `54.61%` | `45.39%` | `1.20` | 1,130,000.00 USD |
| `1H` | `MEXC` | `59.95%` | `40.05%` | `1.50` | 742,140.00 USD |
| `1H` | `Bitunix` | `30.9%` | `69.1%` | `0.45` | 1,850,000.00 USD |
| `1H` | `Hyperliquid` | `54.66%` | `45.34%` | `1.21` | 1,990,000.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `60.78%` | `39.22%` | `1.55` | 325,460.00 USD |
| `1H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `WhiteBIT` | `4.99%` | `95.01%` | `0.05` | 943,680.00 USD |
| `1H` | `HTX` | `43.18%` | `56.82%` | `0.76` | 410,790.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `41.75%` | `58.25%` | `0.72` | 203,860.00 USD |
| `1H` | `Aster` | `45.72%` | `54.28%` | `0.84` | 887,570.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `52.42%` | `47.58%` | `1.10` | 256,060.00 USD |
| `1H` | `Whale Positions` | `43.7%` | `56.3%` | `0.78` | 31,640,000.00 USD |
| `1H` | `Global Accounts` | `43.74%` | `56.26%` | `0.78` | 58,160,000.00 USD |
| `4H` | `TRX` | `41.31%` | `58.69%` | `0.70` | 260,410,000.00 USD |
| `4H` | `Binance` | `39.43%` | `60.57%` | `0.65` | 165,910,000.00 USD |
| `4H` | `OKX` | `46.73%` | `53.27%` | `0.88` | 21,940,000.00 USD |
| `4H` | `Bybit` | `35.73%` | `64.27%` | `0.56` | 18,420,000.00 USD |
| `4H` | `KuCoin` | `48.2%` | `51.8%` | `0.93` | 3,240,000.00 USD |
| `4H` | `Gate` | `48.77%` | `51.23%` | `0.95` | 12,800,000.00 USD |
| `4H` | `Bitget` | `44.94%` | `55.06%` | `0.82` | 5,880,000.00 USD |
| `4H` | `BingX` | `46.54%` | `53.46%` | `0.87` | 5,120,000.00 USD |
| `4H` | `MEXC` | `53.07%` | `46.93%` | `1.13` | 3,050,000.00 USD |
| `4H` | `Bitunix` | `41.79%` | `58.21%` | `0.72` | 6,740,000.00 USD |
| `4H` | `Hyperliquid` | `50.54%` | `49.46%` | `1.02` | 6,260,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `50.6%` | `49.4%` | `1.02` | 2,190,000.00 USD |
| `4H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `WhiteBIT` | `2.85%` | `97.15%` | `0.03` | 2,290,000.00 USD |
| `4H` | `HTX` | `52.79%` | `47.21%` | `1.12` | 1,660,000.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `69.9%` | `30.1%` | `2.32` | 1,040,000.00 USD |
| `4H` | `Aster` | `47.85%` | `52.15%` | `0.92` | 2,470,000.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `65.9%` | `34.1%` | `1.93` | 1,420,000.00 USD |
| `4H` | `Whale Positions` | `39.43%` | `60.57%` | `0.65` | 165,910,000.00 USD |
| `4H` | `Global Accounts` | `41.31%` | `58.69%` | `0.70` | 260,410,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5:00 UTC` | `0.3312` | `0.3323` | `0.3312` | `0.3350` | `0.3309` | 3,615,541.77 USD | 1,824,507.31 USD | 1,791,034.46 USD | 33,472.85 USD | `+0.93%` | `10B / 13S` |
| `0:00 UTC` | `0.3320` | `0.3319` | `0.3320` | `0.3329` | `0.3307` | 3,613,244.76 USD | 2,074,143.60 USD | 1,539,101.16 USD | 535,042.44 USD | `+14.81%` | `13B / 9S` |
| `5:00 UTC` | `0.3320` | `0.3320` | `0.3320` | `0.3328` | `0.3316` | 3,173,620.42 USD | 1,545,938.41 USD | 1,627,682.01 USD | -81,743.60 USD | `-2.58%` | `29B / 18S` |
| `0:00 UTC` | `0.3323` | `0.3323` | `0.3323` | `0.3332` | `0.3318` | 1,965,395.58 USD | 930,788.45 USD | 1,034,607.13 USD | -103,818.67 USD | `-5.28%` | `16B / 20S` |
| `5:00 UTC` | `0.3320` | `0.3322` | `0.3320` | `0.3328` | `0.3319` | 2,011,353.25 USD | 833,950.97 USD | 1,177,402.29 USD | -343,451.32 USD | `-17.08%` | `9B / 10S` |
| `0:00 UTC` | `0.3339` | `0.3340` | `0.3339` | `0.3367` | `0.3319` | 3,824,828.40 USD | 1,984,762.45 USD | 1,840,065.95 USD | 144,696.50 USD | `+3.78%` | `20B / 6S` |
| `5:00 UTC` | `0.3351` | `0.3349` | `0.3351` | `0.3364` | `0.3341` | 1,965,380.04 USD | 899,735.78 USD | 1,065,644.26 USD | -165,908.48 USD | `-8.44%` | `11B / 14S` |
| `0:00 UTC` | `0.3351` | `0.3349` | `0.3351` | `0.3360` | `0.3335` | 1,833,198.85 USD | 904,870.52 USD | 928,328.33 USD | -23,457.81 USD | `-1.28%` | `23B / 24S` |
| `5:00 UTC` | `0.3348` | `0.3371` | `0.3348` | `0.3399` | `0.3343` | 3,666,829.89 USD | 1,892,139.69 USD | 1,774,690.20 USD | 117,449.48 USD | `+3.20%` | `16B / 11S` |
| `0:00 UTC` | `0.3400` | `0.3396` | `0.3400` | `0.3406` | `0.3377` | 4,936,873.78 USD | 1,674,457.40 USD | 3,262,416.38 USD | -1,587,958.98 USD | `-32.17%` | `22B / 11S` |

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
| `5m` | -33,710.00 USD | 693,530.00 USD | **`ACCUMULATION`** |
| `15m` | -1,300,000.00 USD | 439,440.00 USD | **`DISTRIBUTION`** |
| `30m` | -1,530,000.00 USD | 520,100.00 USD | **`DISTRIBUTION`** |
| `1h` | -3,280,000.00 USD | 836,240.00 USD | **`DISTRIBUTION`** |
| `2h` | -2,100,000.00 USD | 2,650,000.00 USD | **`ACCUMULATION`** |
| `4h` | 1,010,000.00 USD | 3,360,000.00 USD | **`ACCUMULATION`** |
| `6h` | 6,180,000.00 USD | -5,210,000.00 USD | **`ACCUMULATION`** |
| `8h` | 12,100,000.00 USD | -6,110,000.00 USD | **`ACCUMULATION`** |
| `12h` | 18,870,000.00 USD | 3,300,000.00 USD | **`ACCUMULATION`** |
| `24h` | 18,790,000.00 USD | 6,240,000.00 USD | **`ACCUMULATION`** |
| `1w` | 12,360,000.00 USD | 4,800,000.00 USD | **`ACCUMULATION`** |
| `30d` | -11,560,000.00 USD | 5,730,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-33.71K` | 15m=`-1.30M` | 1h=`-3.28M` | 24h=`+18.79M`
* Futures Capital Netflows: 5m=`+693.53K` | 15m=`+439.44K` | 1h=`+836.24K` | 24h=`+6.24M`
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
  * `2026-10-30 15:49:45 IST`: [istat.it] - (Sentiment: `Neutral`)
  * `2026-10-30 15:32:45 IST`: [ec.europa.eu] - (Sentiment: `Neutral`)
  * `2026-10-30 15:32:45 IST`: [ec.europa.eu] - (Sentiment: `Neutral`)
  * `2026-10-30 15:18:45 IST`: [dailyforex.com] - (Sentiment: `Neutral`)
  * `2026-10-30 15:12:45 IST`: [breakingthenews.net] - (Sentiment: `Neutral`)
  * `2026-10-30 16:07:45 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 16:07:45 IST`: [@FirstSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 16:07:45 IST`: [destatis.de] - (Sentiment: `Neutral`)
  * `2026-10-30 16:07:45 IST`: [istat.it] - (Sentiment: `Neutral`)
  * `2026-10-30 16:07:45 IST`: [channelnewsasia.com] - (Sentiment: `Neutral`)
  * `2026-10-30 16:06:45 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 16:06:45 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 16:06:45 IST`: [kof.ethz.ch] - (Sentiment: `Neutral`)
  * `2026-10-30 16:06:45 IST`: [gerlachmacro.substack.com] - (Sentiment: `Neutral`)
  * `2026-10-30 16:06:45 IST`: [@financialjuice] - (Sentiment: `Neutral`)


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
  * Execution Entry: `0.3396` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `0.3302` (Risk Distance: `0.0094` pts)
  * +2.5R Take Profit: `0.3632`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `0.3580` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `0.3674` (Risk Distance: `0.0094` pts)
  * +2.5R Take Profit: `0.3344`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`0.3413`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
