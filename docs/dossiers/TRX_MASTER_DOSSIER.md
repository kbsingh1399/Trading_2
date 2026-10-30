# 🏛️ SOVEREIGN CANDIDATE DOSSIER: TRX
**Canonical Key**: `TRX` | **Broker Instrument**: `TRXUSD.p` | **Asset Class**: `Crypto Alt L1`
**Timestamp**: `2026-10-30 16:00:27 IST` (`2026-10-30 10:30:27 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `0.3328` | **Live Ask Quote**: `0.3365` | **Mid Price**: `0.3347`
- **Spread Points**: `37.00` | **Spread BPS**: `110.56 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `0.3448` | VWAP Z-Score: `-1.13` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `0.0027` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `44.45` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `0.3732` | Lower -3.00σ Band: `0.3164`
  * Upper +2.51σ Band: `0.3685` | Lower -2.51σ Band: `0.3210`
  * Upper +2.01σ Band: `0.3638` | Lower -2.01σ Band: `0.3258`
  * Upper +2.00σ Band: `0.3637` | Lower -2.00σ Band: `0.3258`
  * Upper +1.28σ Band: `0.3569` | Lower -1.28σ Band: `0.3327`
  * Upper +1.00σ Band: `0.3543` | Lower -1.00σ Band: `0.3353`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`0.3330` | EMA-20=`0.3352` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`0.3385` (Slope: `+0.0000`) | EMA-100=`0.3377`
  * Institutional Anchors: EMA-144=`0.3365` | EMA-200=`0.3352` (Slope: `-0.1134`) | EMA-233=`0.3346`
- **Range Boundaries**: 24H High=`0.3632` | 24H Low=`0.3275` | Weekly High=`0.3632` | Weekly Low=`0.3266`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `0.3578` (Distance: `-6.45%`)
  * Point of Control (POC) = `0.3513` (Distance: `-4.73%`)
  * Value Area Low (VAL) = `0.3402` (Distance: `-1.62%`)
  * Auction Positioning: `BELOW_VALUE (Imbalance)` | Session Bias: **`BULLISH (Above Pivot)`** | Market Regime: `FAILED_AUCTION_REVERSAL`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`0.3312` | POC=`0.3307` | VAL=`0.3293`
  * Prior Day Extremes: PDH=`0.3335` | PDL=`0.3275` | PDC=`0.3275`
  * Monday Range Blueprint: High=`0.3310` | Mid=`0.3300` | Low=`0.3289`
  * Developing Weekly Value Area: Weekly VAH=`0.3462` | Weekly POC=`0.3306` | Weekly VAL=`0.3267`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`0.3632` | Low=`0.3335`
  * London Session (08:00-16:00 UTC): High=`0.3444` | Low=`0.3299`
  * New York Session (13:00-21:00 UTC): High=`0.3341` | Low=`0.3319`
  * Initial Balance (First Hour): IB High=`0.3444` | IB Low=`0.3379`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `0.3333` - `0.3360`
  * Optimal Trade Entry (OTE 0.705): `0.3353`
  * Structural Invalidation Anchor (0.786): `0.3373`

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
| `4h` | `0.3371` | `0.3377` | `0.3307` | `0.3345` | `76,037,806` | 25,344,356.06 USD | -370,591.66 USD | `-1.46%` | -2,776,645.54 USD | `+0.03` | **`BEARISH`** | `NEUTRAL CHOP` |

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
| --- | **`0.3347`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `MID` | Regular L2 Book | - | - | - | Interbank L2 | 0.00% | Interbank |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 15:50:34 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `1092` | `0xecb6...2b00` | `LONG` | 1,967,953.40 USD | `5,869,932.00` | `0.3344` | `0.3351` | `0.000000` | 5,187.08 USD | `+0.26%` | `10X Cross` |
| `1453` | `0x8dd7...fa30` | `SHORT` | 1,486,590.11 USD | `4,434,141.00` | `0.3331` | `0.3351` | `0.3800` | -9,601.78 USD | `-0.65%` | `6X Cross` |
| `1579` | `0xeadc...9d55` | `LONG` | 1,341,200.00 USD | `4,000,000.00` | `0.3421` | `0.3351` | `0.000000` | -27,278.09 USD | `-2.03%` | `10X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `0.3316` | 7,871.14 USD | `-` | `NEWS_INTEL` | `-` | #TRX Whale BUY: 7.87K USD at 0.3316 USD [API] | `2026-10-29 10:14:22` |
| `ANNOUNCEMENT` | `INFO` | `0.3318` | 6,469.10 USD | `-` | `NEWS_INTEL` | `-` | #TRX Whale BUY: 6.47K USD at 0.3318 USD [API] | `2026-10-29 11:35:32` |
| `ANNOUNCEMENT` | `INFO` | `0.3318` | 9,999.82 USD | `-` | `NEWS_INTEL` | `-` | #TRX Whale BUY: 10.00K USD at 0.3318 USD [API] | `2026-10-29 11:35:32` |
| `ANNOUNCEMENT` | `INFO` | `0.3316` | 6,423.42 USD | `-` | `NEWS_INTEL` | `-` | #TRX Whale SELL: 6.42K USD at 0.3316 USD [API] | `2026-10-29 12:41:40` |
| `ANNOUNCEMENT` | `INFO` | `0.3318` | 6,464.73 USD | `-` | `NEWS_INTEL` | `-` | #TRX Whale SELL: 6.46K USD at 0.3318 USD [API] | `2026-10-29 13:28:43` |
| `ANNOUNCEMENT` | `INFO` | `0.3312` | 6,464.28 USD | `-` | `NEWS_INTEL` | `-` | #TRX Whale SELL: 6.46K USD at 0.3312 USD [API] | `2026-10-29 18:05:53` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`0.3675` (Vol: 1,300,000.00 USD, Dist: `+8.62%`) | Long MP=`0.3298` (Vol: 509,400.00 USD, Dist: `--2.53%`)
  * 48H Horizon: Short MP=`0.3675` (Vol: 1,300,000.00 USD, Dist: `+8.62%`) | Long MP=`0.3249` (Vol: 724,200.00 USD, Dist: `--3.99%`)
  * 3D Horizon: Short MP=`0.3662` (Vol: 1,100,000.00 USD, Dist: `+8.22%`) | Long MP=`0.3250` (Vol: 996,100.00 USD, Dist: `--3.96%`)
  * 7D Horizon: Short MP=`0.3661` (Vol: 1,100,000.00 USD, Dist: `+8.21%`) | Long MP=`0.3248` (Vol: 1,000,000.00 USD, Dist: `--3.99%`)
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
| `1D` | `Long Liquidation` | `0.2975` | 14,730,000.00 USD | 14,730,000.00 USD | 197.77 USD | 1,630.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.2977` | 21,760,000.00 USD | 21,760,000.00 USD | 53,680.00 USD | 18,540.00 USD | 17,670.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.2979` | 14,730,000.00 USD | 14,730,000.00 USD | 17,590.00 USD | 3,370.00 USD | 4,770.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.2983` | 14,700,000.00 USD | 14,700,000.00 USD | 85,050.00 USD | 8,000.00 USD | 21,370.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.2983` | 21,670,000.00 USD | 21,670,000.00 USD | 170,240.00 USD | 15,470.00 USD | 39,660.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.2985` | 759.68 USD | 841,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.2987` | 14,590,000.00 USD | 14,590,000.00 USD | 43,060.00 USD | 7,050.00 USD | 3,020.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.2989` | 21,440,000.00 USD | 21,440,000.00 USD | 112,680.00 USD | 18,720.00 USD | 23,920.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.2991` | 14,540,000.00 USD | 14,540,000.00 USD | 56,620.00 USD | 0.00 USD | 8,790.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.2995` | 14,470,000.00 USD | 14,470,000.00 USD | 13,470.00 USD | 57,880.00 USD | 85,870.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.2995` | 21,290,000.00 USD | 21,290,000.00 USD | 10,860.00 USD | 69,130.00 USD | 80,320.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.2995` | 197.37 USD | 840,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.2999` | 14,310,000.00 USD | 14,310,000.00 USD | 8,760.00 USD | 9,870.00 USD | 17,040.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3001` | 21,130,000.00 USD | 21,130,000.00 USD | 3,960.00 USD | 34,510.00 USD | 93,100.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3003` | 14,280,000.00 USD | 14,280,000.00 USD | 15,600.00 USD | 15,540.00 USD | 24,520.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3005` | 10,620.00 USD | 840,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3007` | 14,220,000.00 USD | 14,220,000.00 USD | 14,390.00 USD | 10,200.00 USD | 24,520.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3007` | 21,000,000.00 USD | 21,000,000.00 USD | 13,780.00 USD | 2,960.00 USD | 22,100.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3011` | 14,170,000.00 USD | 14,170,000.00 USD | 38,060.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3015` | 14,140,000.00 USD | 14,140,000.00 USD | 1,010.00 USD | 5,010.00 USD | 18,990.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3015` | 102.81 USD | 829,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3019` | 14,110,000.00 USD | 14,110,000.00 USD | 14,850.00 USD | 6,650.00 USD | 16,590.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3019` | 20,960,000.00 USD | 20,960,000.00 USD | 0.00 USD | 8,660.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3023` | 14,070,000.00 USD | 14,070,000.00 USD | 1,330.00 USD | 6,590.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3025` | 20,950,000.00 USD | 20,950,000.00 USD | 0.00 USD | 22,200.00 USD | 55,830.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3025` | 2,510.00 USD | 829,820.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3027` | 14,070,000.00 USD | 14,070,000.00 USD | 23,690.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3031` | 14,040,000.00 USD | 14,040,000.00 USD | 2,480.00 USD | 8,320.00 USD | 6,190.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3031` | 20,870,000.00 USD | 20,870,000.00 USD | 50,940.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3035` | 14,020,000.00 USD | 14,020,000.00 USD | 742.30 USD | 3,230.00 USD | 12,600.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3035` | 4,040.00 USD | 827,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.3037` | 20,820,000.00 USD | 20,820,000.00 USD | 1,880.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3039` | 14,010,000.00 USD | 14,010,000.00 USD | 1,060.00 USD | 0.00 USD | 44,700.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3043` | 13,960,000.00 USD | 13,960,000.00 USD | 0.00 USD | 20,130.00 USD | 11,650.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3043` | 20,820,000.00 USD | 20,820,000.00 USD | 2,700.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3045` | 138.24 USD | 823,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3047` | 13,930,000.00 USD | 13,930,000.00 USD | 31,710.00 USD | 13,780.00 USD | 49,740.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3049` | 20,820,000.00 USD | 20,820,000.00 USD | 18,360.00 USD | 0.00 USD | 66,870.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3051` | 13,840,000.00 USD | 13,840,000.00 USD | 18,730.00 USD | 2,510.00 USD | 11,570.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3055` | 13,800,000.00 USD | 13,800,000.00 USD | 28,250.00 USD | 13,380.00 USD | 37,740.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3055` | 20,730,000.00 USD | 20,730,000.00 USD | 1,490.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3055` | 14,670.00 USD | 823,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.3061` | 20,730,000.00 USD | 20,730,000.00 USD | 32,930.00 USD | 7,690.00 USD | 37,210.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3063` | 13,720,000.00 USD | 13,720,000.00 USD | 885.25 USD | 16,530.00 USD | 56,460.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3065` | 5,900.00 USD | 808,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3067` | 13,650,000.00 USD | 13,650,000.00 USD | 31,110.00 USD | 15,440.00 USD | 35,690.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3067` | 20,650,000.00 USD | 20,650,000.00 USD | 6,300.00 USD | 8,110.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3071` | 13,570,000.00 USD | 13,570,000.00 USD | 67.24 USD | 0.00 USD | 12,760.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3073` | 20,640,000.00 USD | 20,640,000.00 USD | 7,990.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3075` | 13,550,000.00 USD | 13,550,000.00 USD | 23,570.00 USD | 1,940.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3075` | 722.62 USD | 802,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3079` | 13,530,000.00 USD | 13,530,000.00 USD | 15.29 USD | 0.00 USD | 12,250.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3079` | 20,630,000.00 USD | 20,630,000.00 USD | 37,350.00 USD | 10,270.00 USD | 50,200.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3083` | 13,520,000.00 USD | 13,520,000.00 USD | 18,620.00 USD | 0.00 USD | 15,810.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3085` | 20,530,000.00 USD | 20,530,000.00 USD | 3,660.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3085` | 291.53 USD | 801,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3087` | 13,480,000.00 USD | 13,480,000.00 USD | 623.99 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3091` | 13,480,000.00 USD | 13,480,000.00 USD | 31.03 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3091` | 20,530,000.00 USD | 20,530,000.00 USD | 7,040.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3095` | 13,480,000.00 USD | 13,480,000.00 USD | 17,320.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3095` | 192.51 USD | 801,540.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.3097` | 20,520,000.00 USD | 20,520,000.00 USD | 79,880.00 USD | 3,620.00 USD | 54,360.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3099` | 13,460,000.00 USD | 13,460,000.00 USD | 8,120.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3103` | 13,460,000.00 USD | 13,460,000.00 USD | 58,110.00 USD | 15,820.00 USD | 46,470.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3103` | 20,380,000.00 USD | 20,380,000.00 USD | 67,180.00 USD | 0.00 USD | 63,310.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3105` | 820.96 USD | 801,350.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3107` | 13,340,000.00 USD | 13,340,000.00 USD | 1,350.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3109` | 20,250,000.00 USD | 20,250,000.00 USD | 19,040.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3115` | 13,330,000.00 USD | 13,330,000.00 USD | 977.81 USD | 9,110.00 USD | 17,620.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3115` | 20,230,000.00 USD | 20,230,000.00 USD | 10,250.00 USD | 0.00 USD | 37,490.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3115` | 13,600.00 USD | 800,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3119` | 13,310,000.00 USD | 13,310,000.00 USD | 26,060.00 USD | 10,650.00 USD | 17,440.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3121` | 20,180,000.00 USD | 20,180,000.00 USD | 162,320.00 USD | 19,620.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3123` | 13,250,000.00 USD | 13,250,000.00 USD | 12,740.00 USD | 0.00 USD | 16,390.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3125` | 17,810.00 USD | 786,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3127` | 13,220,000.00 USD | 13,220,000.00 USD | 2,560.00 USD | 39,470.00 USD | 7,580.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3127` | 20,000,000.00 USD | 20,000,000.00 USD | 12,250.00 USD | 54,460.00 USD | 57,690.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3131` | 13,170,000.00 USD | 13,170,000.00 USD | 3,600.00 USD | 2,520.00 USD | 21,520.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3133` | 19,880,000.00 USD | 19,880,000.00 USD | 4,440.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3135` | 13,150,000.00 USD | 13,150,000.00 USD | 5,830.00 USD | 23,940.00 USD | 9,590.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3135` | 446.11 USD | 769,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3139` | 13,110,000.00 USD | 13,110,000.00 USD | 4,710.00 USD | 10,610.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3139` | 19,870,000.00 USD | 19,870,000.00 USD | 3,330.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3143` | 13,090,000.00 USD | 13,090,000.00 USD | 3,210.00 USD | 3,580.00 USD | 9,540.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3145` | 19,870,000.00 USD | 19,870,000.00 USD | 247,920.00 USD | 51,270.00 USD | 17,870.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3145` | 577.11 USD | 768,680.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3147` | 13,070,000.00 USD | 13,070,000.00 USD | 2,670.00 USD | 2,330.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3151` | 13,070,000.00 USD | 13,070,000.00 USD | 4,850.00 USD | 23,750.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3151` | 19,550,000.00 USD | 19,550,000.00 USD | 204,770.00 USD | 23,130.00 USD | 49,320.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3155` | 13,040,000.00 USD | 13,040,000.00 USD | 33,260.00 USD | 3,680.00 USD | 10,790.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3155` | 11,510.00 USD | 768,100.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.3157` | 19,280,000.00 USD | 19,280,000.00 USD | 393,880.00 USD | 93,740.00 USD | 60,300.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3159` | 12,990,000.00 USD | 12,990,000.00 USD | 5,120.00 USD | 0.00 USD | 5,450.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3163` | 12,980,000.00 USD | 12,980,000.00 USD | 3,780.00 USD | 33,960.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3163` | 18,730,000.00 USD | 18,730,000.00 USD | 495,020.00 USD | 174,600.00 USD | 189,520.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3165` | 935.89 USD | 756,590.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3167` | 12,950,000.00 USD | 12,950,000.00 USD | 43,210.00 USD | 6,270.00 USD | 17,210.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3169` | 17,870,000.00 USD | 17,870,000.00 USD | 417,170.00 USD | 104,590.00 USD | 135,950.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3171` | 12,880,000.00 USD | 12,880,000.00 USD | 8,020.00 USD | 35,130.00 USD | 35,030.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3175` | 12,800,000.00 USD | 12,800,000.00 USD | 19,750.00 USD | 7,370.00 USD | 14,490.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3175` | 17,210,000.00 USD | 17,210,000.00 USD | 140,810.00 USD | 53,470.00 USD | 69,280.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3175` | 2,290.00 USD | 755,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3179` | 12,760,000.00 USD | 12,760,000.00 USD | 62,280.00 USD | 25,310.00 USD | 43,110.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3181` | 16,950,000.00 USD | 16,950,000.00 USD | 738,240.00 USD | 76,910.00 USD | 182,330.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3183` | 12,630,000.00 USD | 12,630,000.00 USD | 359,160.00 USD | 39,030.00 USD | 72,750.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3185` | 1,300.00 USD | 753,370.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3187` | 12,160,000.00 USD | 12,160,000.00 USD | 92,220.00 USD | 41,750.00 USD | 77,560.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3187` | 15,950,000.00 USD | 15,950,000.00 USD | 407,530.00 USD | 97,820.00 USD | 24,770.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3191` | 11,950,000.00 USD | 11,950,000.00 USD | 203,200.00 USD | 13,910.00 USD | 45,560.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3193` | 15,420,000.00 USD | 15,420,000.00 USD | 180,550.00 USD | 123,840.00 USD | 247,300.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3195` | 11,680,000.00 USD | 11,680,000.00 USD | 93,760.00 USD | 169,840.00 USD | 242,890.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3199` | 11,180,000.00 USD | 11,180,000.00 USD | 82,300.00 USD | 60,220.00 USD | 102,370.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3199` | 14,870,000.00 USD | 14,870,000.00 USD | 0.00 USD | 191,160.00 USD | 267,030.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3203` | 10,930,000.00 USD | 10,930,000.00 USD | 246,790.00 USD | 56,790.00 USD | 109,780.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3205` | 14,410,000.00 USD | 14,410,000.00 USD | 167,490.00 USD | 59,200.00 USD | 130,760.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3205` | 2,930.00 USD | 752,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3207` | 10,520,000.00 USD | 10,520,000.00 USD | 133,880.00 USD | 25,490.00 USD | 108,030.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3211` | 10,250,000.00 USD | 10,250,000.00 USD | 108,130.00 USD | 27,010.00 USD | 99,450.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3211` | 14,050,000.00 USD | 14,050,000.00 USD | 568,110.00 USD | 135,070.00 USD | 244,340.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3215` | 10,020,000.00 USD | 10,020,000.00 USD | 0.00 USD | 33,650.00 USD | 130,970.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3217` | 13,110,000.00 USD | 13,110,000.00 USD | 285,190.00 USD | 58,690.00 USD | 107,900.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3219` | 9,850,000.00 USD | 9,850,000.00 USD | 5,550.00 USD | 23,450.00 USD | 96,920.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3223` | 9,730,000.00 USD | 9,730,000.00 USD | 154,560.00 USD | 41,870.00 USD | 120,750.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3223` | 12,650,000.00 USD | 12,650,000.00 USD | 643,460.00 USD | 265,170.00 USD | 156,030.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3227` | 9,410,000.00 USD | 9,410,000.00 USD | 52,010.00 USD | 50,480.00 USD | 81,740.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3229` | 11,590,000.00 USD | 11,590,000.00 USD | 858,070.00 USD | 283,650.00 USD | 518,610.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3231` | 9,220,000.00 USD | 9,220,000.00 USD | 54,440.00 USD | 17,630.00 USD | 120,280.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3235` | 9,030,000.00 USD | 9,030,000.00 USD | 61,120.00 USD | 102,040.00 USD | 151,550.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3235` | 9,930,000.00 USD | 9,930,000.00 USD | 709,160.00 USD | 228,450.00 USD | 359,100.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3235` | 128.43 USD | 749,140.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3239` | 8,720,000.00 USD | 8,720,000.00 USD | 0.00 USD | 32,340.00 USD | 65,220.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3241` | 8,630,000.00 USD | 8,630,000.00 USD | 432,660.00 USD | 149,860.00 USD | 138,560.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3243` | 8,620,000.00 USD | 8,620,000.00 USD | 125,350.00 USD | 41,210.00 USD | 223,350.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3247` | 8,230,000.00 USD | 8,230,000.00 USD | 331,430.00 USD | 76,120.00 USD | 204,890.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3247` | 7,910,000.00 USD | 7,910,000.00 USD | 846,180.00 USD | 127,310.00 USD | 353,590.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3251` | 7,620,000.00 USD | 7,620,000.00 USD | 674,140.00 USD | 89,590.00 USD | 300,060.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3253` | 6,580,000.00 USD | 6,580,000.00 USD | 1,220,000.00 USD | 137,440.00 USD | 241,690.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3255` | 6,550,000.00 USD | 6,550,000.00 USD | 428,540.00 USD | 89,190.00 USD | 271,020.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3255` | 3,580.00 USD | 749,010.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3259` | 5,760,000.00 USD | 5,760,000.00 USD | 346,750.00 USD | 215,120.00 USD | 414,300.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3259` | 4,980,000.00 USD | 4,980,000.00 USD | 306,910.00 USD | 288,370.00 USD | 503,650.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3263` | 4,790,000.00 USD | 4,790,000.00 USD | 27,080.00 USD | 240,230.00 USD | 320,610.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3265` | 3,880,000.00 USD | 3,880,000.00 USD | 80,120.00 USD | 324,810.00 USD | 500,270.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3267` | 4,200,000.00 USD | 4,200,000.00 USD | 44,720.00 USD | 159,870.00 USD | 341,370.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3271` | 3,650,000.00 USD | 3,650,000.00 USD | 237,730.00 USD | 81,010.00 USD | 340,330.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3271` | 2,980,000.00 USD | 2,980,000.00 USD | 320,700.00 USD | 138,680.00 USD | 261,530.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3275` | 3,000,000.00 USD | 3,000,000.00 USD | 259,200.00 USD | 54,310.00 USD | 140,050.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3275` | 163.42 USD | 745,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.3277` | 2,260,000.00 USD | 2,260,000.00 USD | 0.00 USD | 29,390.00 USD | 85,620.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3279` | 2,540,000.00 USD | 2,540,000.00 USD | 164,690.00 USD | 55,350.00 USD | 133,800.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3283` | 2,190,000.00 USD | 2,190,000.00 USD | 0.00 USD | 29,070.00 USD | 169,660.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3283` | 2,140,000.00 USD | 2,140,000.00 USD | 89,030.00 USD | 61,340.00 USD | 275,050.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3285` | 745,260.00 USD | 745,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3287` | 1,990,000.00 USD | 1,990,000.00 USD | 117,140.00 USD | 39,260.00 USD | 146,190.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3289` | 1,720,000.00 USD | 1,720,000.00 USD | 0.00 USD | 180,260.00 USD | 105,320.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3291` | 1,690,000.00 USD | 1,690,000.00 USD | 38,710.00 USD | 66,400.00 USD | 119,580.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3295` | 1,460,000.00 USD | 1,460,000.00 USD | 61,960.00 USD | 15,860.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3295` | 1,430,000.00 USD | 1,430,000.00 USD | 254,700.00 USD | 83,080.00 USD | 279,140.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3299` | 1,380,000.00 USD | 1,380,000.00 USD | 141,790.00 USD | 18,090.00 USD | 30,950.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3301` | 815,180.00 USD | 815,180.00 USD | 185,020.00 USD | 47,610.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3303` | 1,190,000.00 USD | 1,190,000.00 USD | 1,210.00 USD | 67,660.00 USD | 74,690.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3307` | 1,050,000.00 USD | 1,050,000.00 USD | 121,770.00 USD | 37,920.00 USD | 87,100.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3307` | 582,550.00 USD | 582,550.00 USD | 167,950.00 USD | 10,690.00 USD | 294,170.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3311` | 803,120.00 USD | 803,120.00 USD | 644.45 USD | 100,700.00 USD | 416,060.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3313` | 109,740.00 USD | 109,740.00 USD | 0.00 USD | 50,650.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3315` | 285,720.00 USD | 285,720.00 USD | 0.00 USD | 65,830.00 USD | 28,340.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3319` | 191,550.00 USD | 191,550.00 USD | 0.00 USD | 47,270.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3319` | 59,090.00 USD | 59,090.00 USD | 0.00 USD | 57,890.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3359` | 144,280.00 USD | 144,280.00 USD | 0.00 USD | 0.00 USD | 144,280.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3361` | 1,200.00 USD | 1,200.00 USD | 1,200.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3367` | 72,920.00 USD | 72,920.00 USD | 72,920.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3375` | 402,560.00 USD | 402,560.00 USD | 329,640.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3383` | 502,490.00 USD | 502,490.00 USD | 71,900.00 USD | 0.00 USD | 28,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3385` | 125,650.00 USD | 125,650.00 USD | 125,650.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3387` | 678,170.00 USD | 678,170.00 USD | 137,130.00 USD | 11,160.00 USD | 27,380.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3391` | 1,010,000.00 USD | 1,010,000.00 USD | 258,550.00 USD | 27,820.00 USD | 49,390.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3391` | 484,990.00 USD | 484,990.00 USD | 124,670.00 USD | 0.00 USD | 234,660.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3395` | 1,950,000.00 USD | 1,950,000.00 USD | 115,280.00 USD | 333,450.00 USD | 485,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3397` | 1,910,000.00 USD | 1,910,000.00 USD | 257,550.00 USD | 752,550.00 USD | 410,830.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3399` | 2,330,000.00 USD | 2,330,000.00 USD | 43,780.00 USD | 120,440.00 USD | 218,200.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3403` | 2,940,000.00 USD | 2,940,000.00 USD | 209,800.00 USD | 61,580.00 USD | 336,240.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3403` | 3,580,000.00 USD | 3,580,000.00 USD | 1,200,000.00 USD | 103,630.00 USD | 376,470.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3407` | 3,110,000.00 USD | 3,110,000.00 USD | 71,510.00 USD | 0.00 USD | 100,230.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3409` | 4,060,000.00 USD | 4,060,000.00 USD | 0.00 USD | 29,390.00 USD | 446,990.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3411` | 3,460,000.00 USD | 3,460,000.00 USD | 265,070.00 USD | 39,790.00 USD | 45,840.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3415` | 4,370,000.00 USD | 4,370,000.00 USD | 672,650.00 USD | 21,540.00 USD | 211,420.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3415` | 4,180,000.00 USD | 4,180,000.00 USD | 0.00 USD | 35,670.00 USD | 85,620.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3419` | 4,500,000.00 USD | 4,500,000.00 USD | 39,640.00 USD | 48,460.00 USD | 48,810.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3421` | 4,220,000.00 USD | 4,220,000.00 USD | 0.00 USD | 43,290.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3423` | 4,610,000.00 USD | 4,610,000.00 USD | 71,180.00 USD | 33,440.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3427` | 4,800,000.00 USD | 4,800,000.00 USD | 0.00 USD | 195,320.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3427` | 4,840,000.00 USD | 4,840,000.00 USD | 0.00 USD | 229,350.00 USD | 384,460.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3431` | 5,160,000.00 USD | 5,160,000.00 USD | 166,310.00 USD | 193,980.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3433` | 5,130,000.00 USD | 5,130,000.00 USD | 254,700.00 USD | 38,560.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3435` | 5,310,000.00 USD | 5,310,000.00 USD | 0.00 USD | 117,530.00 USD | 30,950.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3439` | 5,420,000.00 USD | 5,420,000.00 USD | 0.00 USD | 40,260.00 USD | 62,980.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3443` | 5,470,000.00 USD | 5,470,000.00 USD | 0.00 USD | 38,110.00 USD | 18,140.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3445` | 5,230,000.00 USD | 5,230,000.00 USD | 103,130.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3445` | 2,280.00 USD | 2,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.3447` | 5,700,000.00 USD | 5,700,000.00 USD | 22,420.00 USD | 57,000.00 USD | 146,340.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3451` | 5,930,000.00 USD | 5,930,000.00 USD | 70,130.00 USD | 63,000.00 USD | 99,020.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3451` | 5,320,000.00 USD | 5,320,000.00 USD | 62,830.00 USD | 28,550.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3455` | 6,250,000.00 USD | 6,250,000.00 USD | 169,370.00 USD | 37,860.00 USD | 116,160.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3457` | 5,750,000.00 USD | 5,750,000.00 USD | 62,340.00 USD | 29,340.00 USD | 332,190.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3459` | 7,080,000.00 USD | 7,080,000.00 USD | 214,990.00 USD | 131,290.00 USD | 485,400.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3463` | 7,380,000.00 USD | 7,380,000.00 USD | 13,540.00 USD | 118,340.00 USD | 160,310.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3463` | 6,200,000.00 USD | 6,200,000.00 USD | 0.00 USD | 250,840.00 USD | 205,410.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3467` | 7,550,000.00 USD | 7,550,000.00 USD | 21,890.00 USD | 48,850.00 USD | 100,110.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3469` | 6,530,000.00 USD | 6,530,000.00 USD | 124,720.00 USD | 51,820.00 USD | 152,060.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3471` | 7,650,000.00 USD | 7,650,000.00 USD | 37,620.00 USD | 38,220.00 USD | 25,030.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3475` | 7,750,000.00 USD | 7,750,000.00 USD | 0.00 USD | 59,710.00 USD | 45,010.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3475` | 6,570,000.00 USD | 6,570,000.00 USD | 0.00 USD | 40,540.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3479` | 8,000,000.00 USD | 8,000,000.00 USD | 105,220.00 USD | 16,550.00 USD | 120,420.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3481` | 6,660,000.00 USD | 6,660,000.00 USD | 6,440.00 USD | 32,530.00 USD | 42,810.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3483` | 8,080,000.00 USD | 8,080,000.00 USD | 3,430.00 USD | 22,220.00 USD | 60,430.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3487` | 8,140,000.00 USD | 8,140,000.00 USD | 8,610.00 USD | 27,650.00 USD | 24,410.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3487` | 6,690,000.00 USD | 6,690,000.00 USD | 8,310.00 USD | 21,650.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3491` | 8,270,000.00 USD | 8,270,000.00 USD | 40,710.00 USD | 28,080.00 USD | 61,240.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3493` | 6,980,000.00 USD | 6,980,000.00 USD | 10,490.00 USD | 93,150.00 USD | 192,230.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3495` | 8,400,000.00 USD | 8,400,000.00 USD | 34,020.00 USD | 13,050.00 USD | 79,030.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3499` | 8,840,000.00 USD | 8,840,000.00 USD | 52,670.00 USD | 9,040.00 USD | 375,650.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3499` | 7,120,000.00 USD | 7,120,000.00 USD | 139,880.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3503` | 8,920,000.00 USD | 8,920,000.00 USD | 0.00 USD | 29,350.00 USD | 50,760.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3505` | 7,150,000.00 USD | 7,150,000.00 USD | 11,960.00 USD | 19,280.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3505` | 8,650.00 USD | 10,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.3507` | 9,040,000.00 USD | 9,040,000.00 USD | 75,920.00 USD | 12,560.00 USD | 31,490.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3511` | 9,070,000.00 USD | 9,070,000.00 USD | 1,090.00 USD | 4,320.00 USD | 32,490.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3511` | 8,110,000.00 USD | 8,110,000.00 USD | 690,500.00 USD | 0.00 USD | 271,800.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3515` | 9,180,000.00 USD | 9,180,000.00 USD | 21,910.00 USD | 0.00 USD | 87,340.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3515` | 175.05 USD | 11,110.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.3519` | 9,270,000.00 USD | 9,270,000.00 USD | 31,190.00 USD | 23,960.00 USD | 28,330.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3523` | 9,270,000.00 USD | 9,270,000.00 USD | 3,190.00 USD | 3,730.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3523` | 8,530,000.00 USD | 8,530,000.00 USD | 277,410.00 USD | 28,950.00 USD | 107,430.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3525` | 112.45 USD | 11,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.3527` | 9,440,000.00 USD | 9,440,000.00 USD | 102,610.00 USD | 38,340.00 USD | 28,910.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3531` | 9,600,000.00 USD | 9,600,000.00 USD | 6,270.00 USD | 61,120.00 USD | 88,110.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3535` | 9,850,000.00 USD | 9,850,000.00 USD | 125,280.00 USD | 16,340.00 USD | 113,320.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3535` | 8,800,000.00 USD | 8,800,000.00 USD | 4,830.00 USD | 77,960.00 USD | 187,450.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3539` | 10,030,000.00 USD | 10,030,000.00 USD | 57,460.00 USD | 33,520.00 USD | 81,960.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3541` | 9,730,000.00 USD | 9,730,000.00 USD | 810,900.00 USD | 118,370.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3543` | 10,200,000.00 USD | 10,200,000.00 USD | 28,820.00 USD | 107,380.00 USD | 37,920.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3545` | 29,460.00 USD | 40,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.3547` | 10,270,000.00 USD | 10,270,000.00 USD | 5,090.00 USD | 28,920.00 USD | 31,910.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3547` | 10,020,000.00 USD | 10,020,000.00 USD | 5,390.00 USD | 0.00 USD | 288,450.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3551` | 10,350,000.00 USD | 10,350,000.00 USD | 4,060.00 USD | 29,900.00 USD | 47,950.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3553` | 10,150,000.00 USD | 10,150,000.00 USD | 12,710.00 USD | 117,050.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3555` | 10,410,000.00 USD | 10,410,000.00 USD | 20,180.00 USD | 44,130.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3559` | 10,510,000.00 USD | 10,510,000.00 USD | 331.60 USD | 21,340.00 USD | 78,340.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3559` | 10,170,000.00 USD | 10,170,000.00 USD | 13,500.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3563` | 10,610,000.00 USD | 10,610,000.00 USD | 977.81 USD | 29,510.00 USD | 67,310.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3565` | 10,210,000.00 USD | 10,210,000.00 USD | 0.00 USD | 43,060.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3567` | 10,610,000.00 USD | 10,610,000.00 USD | 3,540.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3571` | 10,620,000.00 USD | 10,620,000.00 USD | 1,770.00 USD | 6,920.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3575` | 10,790,000.00 USD | 10,790,000.00 USD | 161,360.00 USD | 9,250.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3577` | 10,330,000.00 USD | 10,330,000.00 USD | 124,630.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3579` | 10,840,000.00 USD | 10,840,000.00 USD | 2,200.00 USD | 9,130.00 USD | 38,950.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3583` | 10,870,000.00 USD | 10,870,000.00 USD | 14,980.00 USD | 14,930.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3583` | 10,470,000.00 USD | 10,470,000.00 USD | 0.00 USD | 0.00 USD | 135,900.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3587` | 10,880,000.00 USD | 10,880,000.00 USD | 5,760.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3589` | 10,840,000.00 USD | 10,840,000.00 USD | 0.00 USD | 50,650.00 USD | 320,430.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3591` | 10,950,000.00 USD | 10,950,000.00 USD | 22,510.00 USD | 15,750.00 USD | 33,590.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3595` | 11,140,000.00 USD | 11,140,000.00 USD | 93,010.00 USD | 0.00 USD | 99,590.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3595` | 10,990,000.00 USD | 10,990,000.00 USD | 0.00 USD | 0.00 USD | 146,290.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3599` | 11,320,000.00 USD | 11,320,000.00 USD | 47,370.00 USD | 22,780.00 USD | 108,510.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3601` | 11,490,000.00 USD | 11,490,000.00 USD | 4,230.00 USD | 161,200.00 USD | 338,540.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3603` | 11,490,000.00 USD | 11,490,000.00 USD | 32,230.00 USD | 41,780.00 USD | 92,600.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3607` | 11,700,000.00 USD | 11,700,000.00 USD | 28,890.00 USD | 22,500.00 USD | 157,390.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3607` | 11,890,000.00 USD | 11,890,000.00 USD | 330,010.00 USD | 68,030.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3611` | 12,030,000.00 USD | 12,030,000.00 USD | 86,030.00 USD | 54,830.00 USD | 190,770.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3613` | 12,580,000.00 USD | 12,580,000.00 USD | 73,920.00 USD | 330,040.00 USD | 288,930.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3615` | 12,210,000.00 USD | 12,210,000.00 USD | 0.00 USD | 31,910.00 USD | 150,170.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3619` | 12,690,000.00 USD | 12,690,000.00 USD | 368,610.00 USD | 110,060.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3619` | 12,790,000.00 USD | 12,790,000.00 USD | 3,790.00 USD | 209,940.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3623` | 12,870,000.00 USD | 12,870,000.00 USD | 83,390.00 USD | 20,060.00 USD | 71,510.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3625` | 12,990,000.00 USD | 12,990,000.00 USD | 2,300.00 USD | 191,880.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3627` | 13,240,000.00 USD | 13,240,000.00 USD | 337,420.00 USD | 39,070.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3631` | 14,380,000.00 USD | 14,380,000.00 USD | 941,740.00 USD | 102,260.00 USD | 93,510.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3631` | 13,100,000.00 USD | 13,100,000.00 USD | 738.08 USD | 114,740.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3635` | 14,610,000.00 USD | 14,610,000.00 USD | 0.00 USD | 48,500.00 USD | 185,880.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3635` | 12,360.00 USD | 53,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.3637` | 13,130,000.00 USD | 13,130,000.00 USD | 1,090.00 USD | 21,530.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3639` | 15,030,000.00 USD | 15,030,000.00 USD | 183,690.00 USD | 152,650.00 USD | 76,240.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3643` | 15,310,000.00 USD | 15,310,000.00 USD | 167,490.00 USD | 81,220.00 USD | 35,280.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3643` | 13,920,000.00 USD | 13,920,000.00 USD | 1,580.00 USD | 0.00 USD | 789,140.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3647` | 15,720,000.00 USD | 15,720,000.00 USD | 268,930.00 USD | 27,770.00 USD | 110,900.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3649` | 14,100,000.00 USD | 14,100,000.00 USD | 182,150.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3651` | 15,900,000.00 USD | 15,900,000.00 USD | 2,860.00 USD | 55,980.00 USD | 123,070.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3655` | 16,650,000.00 USD | 16,650,000.00 USD | 411,730.00 USD | 107,280.00 USD | 227,180.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3655` | 14,890,000.00 USD | 14,890,000.00 USD | 677,860.00 USD | 112,770.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3659` | 17,110,000.00 USD | 17,110,000.00 USD | 233,580.00 USD | 113,780.00 USD | 113,740.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3661` | 15,890,000.00 USD | 15,890,000.00 USD | 691,690.00 USD | 66,940.00 USD | 238,480.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3663` | 17,720,000.00 USD | 17,720,000.00 USD | 449,010.00 USD | 99,370.00 USD | 62,910.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3665` | 3,110.00 USD | 56,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.3667` | 18,110,000.00 USD | 18,110,000.00 USD | 187,870.00 USD | 62,870.00 USD | 137,570.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3667` | 16,510,000.00 USD | 16,510,000.00 USD | 424,170.00 USD | 34,510.00 USD | 166,250.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3671` | 18,610,000.00 USD | 18,610,000.00 USD | 94,630.00 USD | 79,940.00 USD | 324,560.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3673` | 17,200,000.00 USD | 17,200,000.00 USD | 511,100.00 USD | 53,040.00 USD | 122,410.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3675` | 18,840,000.00 USD | 18,840,000.00 USD | 54,730.00 USD | 53,460.00 USD | 126,530.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3679` | 19,730,000.00 USD | 19,730,000.00 USD | 772,390.00 USD | 25,610.00 USD | 92,020.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3679` | 17,460,000.00 USD | 17,460,000.00 USD | 259,090.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3683` | 20,010,000.00 USD | 20,010,000.00 USD | 18,610.00 USD | 84,920.00 USD | 171,070.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3685` | 17,640,000.00 USD | 17,640,000.00 USD | 1,610.00 USD | 102,650.00 USD | 72,350.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3687` | 20,680,000.00 USD | 20,680,000.00 USD | 440,130.00 USD | 153,070.00 USD | 77,780.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3691` | 21,110,000.00 USD | 21,110,000.00 USD | 363,130.00 USD | 49,680.00 USD | 23,760.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3691` | 18,040,000.00 USD | 18,040,000.00 USD | 147,650.00 USD | 261,530.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3695` | 21,360,000.00 USD | 21,360,000.00 USD | 162,690.00 USD | 88,200.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3697` | 18,280,000.00 USD | 18,280,000.00 USD | 0.00 USD | 175,510.00 USD | 55,830.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3699` | 21,900,000.00 USD | 21,900,000.00 USD | 487,980.00 USD | 15,920.00 USD | 27,870.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3703` | 22,430,000.00 USD | 22,430,000.00 USD | 287,950.00 USD | 180,250.00 USD | 63,170.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3703` | 18,330,000.00 USD | 18,330,000.00 USD | 50,940.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3705` | 278.99 USD | 56,440.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.3707` | 22,970,000.00 USD | 22,970,000.00 USD | 1,640.00 USD | 29,660.00 USD | 510,340.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3709` | 18,330,000.00 USD | 18,330,000.00 USD | 1,880.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3711` | 23,830,000.00 USD | 23,830,000.00 USD | 547,890.00 USD | 84,630.00 USD | 225,950.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3715` | 18,730,000.00 USD | 18,730,000.00 USD | 3,890.00 USD | 0.00 USD | 394,570.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3721` | 19,480,000.00 USD | 19,480,000.00 USD | 1,320.00 USD | 0.00 USD | 747,740.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3725` | 186.25 USD | 56,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.3727` | 19,760,000.00 USD | 19,760,000.00 USD | 213,190.00 USD | 0.00 USD | 66,870.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3733` | 19,940,000.00 USD | 19,940,000.00 USD | 188,670.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3735` | 7,070.00 USD | 63,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.3739` | 20,420,000.00 USD | 20,420,000.00 USD | 247,740.00 USD | 7,690.00 USD | 218,010.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3745` | 20,820,000.00 USD | 20,820,000.00 USD | 249,860.00 USD | 115,430.00 USD | 37,210.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3755` | 4,030.00 USD | 67,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
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
| `1D` | `0.2975` | 14,730,000.00 USD | 0.00 USD | 14,730,000.00 USD | 197.77 USD | 1,630.00 USD | 0.00 USD |
| `7D` | `0.2977` | 21,760,000.00 USD | 0.00 USD | 21,760,000.00 USD | 53,680.00 USD | 18,540.00 USD | 17,670.00 USD |
| `1D` | `0.2979` | 14,730,000.00 USD | 0.00 USD | 14,730,000.00 USD | 17,590.00 USD | 3,370.00 USD | 4,770.00 USD |
| `1D` | `0.2983` | 14,700,000.00 USD | 0.00 USD | 14,700,000.00 USD | 85,050.00 USD | 8,000.00 USD | 21,370.00 USD |
| `7D` | `0.2983` | 21,670,000.00 USD | 0.00 USD | 21,670,000.00 USD | 170,240.00 USD | 15,470.00 USD | 39,660.00 USD |
| `1D` | `0.2987` | 14,590,000.00 USD | 0.00 USD | 14,590,000.00 USD | 43,060.00 USD | 7,050.00 USD | 3,020.00 USD |
| `7D` | `0.2989` | 21,440,000.00 USD | 0.00 USD | 21,440,000.00 USD | 112,680.00 USD | 18,720.00 USD | 23,920.00 USD |
| `1D` | `0.2991` | 14,540,000.00 USD | 0.00 USD | 14,540,000.00 USD | 56,620.00 USD | 0.00 USD | 8,790.00 USD |
| `1D` | `0.2995` | 14,470,000.00 USD | 0.00 USD | 14,470,000.00 USD | 13,470.00 USD | 57,880.00 USD | 85,870.00 USD |
| `7D` | `0.2995` | 21,290,000.00 USD | 0.00 USD | 21,290,000.00 USD | 10,860.00 USD | 69,130.00 USD | 80,320.00 USD |
| `1D` | `0.2999` | 14,310,000.00 USD | 0.00 USD | 14,310,000.00 USD | 8,760.00 USD | 9,870.00 USD | 17,040.00 USD |
| `7D` | `0.3001` | 21,130,000.00 USD | 0.00 USD | 21,130,000.00 USD | 3,960.00 USD | 34,510.00 USD | 93,100.00 USD |
| `1D` | `0.3003` | 14,280,000.00 USD | 0.00 USD | 14,280,000.00 USD | 15,600.00 USD | 15,540.00 USD | 24,520.00 USD |
| `1D` | `0.3007` | 14,220,000.00 USD | 0.00 USD | 14,220,000.00 USD | 14,390.00 USD | 10,200.00 USD | 24,520.00 USD |
| `7D` | `0.3007` | 21,000,000.00 USD | 0.00 USD | 21,000,000.00 USD | 13,780.00 USD | 2,960.00 USD | 22,100.00 USD |
| `1D` | `0.3011` | 14,170,000.00 USD | 0.00 USD | 14,170,000.00 USD | 38,060.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3015` | 14,140,000.00 USD | 0.00 USD | 14,140,000.00 USD | 1,010.00 USD | 5,010.00 USD | 18,990.00 USD |
| `1D` | `0.3019` | 14,110,000.00 USD | 0.00 USD | 14,110,000.00 USD | 14,850.00 USD | 6,650.00 USD | 16,590.00 USD |
| `7D` | `0.3019` | 20,960,000.00 USD | 0.00 USD | 20,960,000.00 USD | 0.00 USD | 8,660.00 USD | 0.00 USD |
| `1D` | `0.3023` | 14,070,000.00 USD | 0.00 USD | 14,070,000.00 USD | 1,330.00 USD | 6,590.00 USD | 0.00 USD |
| `7D` | `0.3025` | 20,950,000.00 USD | 0.00 USD | 20,950,000.00 USD | 0.00 USD | 22,200.00 USD | 55,830.00 USD |
| `1D` | `0.3027` | 14,070,000.00 USD | 0.00 USD | 14,070,000.00 USD | 23,690.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3031` | 14,040,000.00 USD | 0.00 USD | 14,040,000.00 USD | 2,480.00 USD | 8,320.00 USD | 6,190.00 USD |
| `7D` | `0.3031` | 20,870,000.00 USD | 0.00 USD | 20,870,000.00 USD | 50,940.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3035` | 14,020,000.00 USD | 0.00 USD | 14,020,000.00 USD | 742.30 USD | 3,230.00 USD | 12,600.00 USD |
| `7D` | `0.3037` | 20,820,000.00 USD | 0.00 USD | 20,820,000.00 USD | 1,880.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3039` | 14,010,000.00 USD | 0.00 USD | 14,010,000.00 USD | 1,060.00 USD | 0.00 USD | 44,700.00 USD |
| `1D` | `0.3043` | 13,960,000.00 USD | 0.00 USD | 13,960,000.00 USD | 0.00 USD | 20,130.00 USD | 11,650.00 USD |
| `7D` | `0.3043` | 20,820,000.00 USD | 0.00 USD | 20,820,000.00 USD | 2,700.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3047` | 13,930,000.00 USD | 0.00 USD | 13,930,000.00 USD | 31,710.00 USD | 13,780.00 USD | 49,740.00 USD |
| `7D` | `0.3049` | 20,820,000.00 USD | 0.00 USD | 20,820,000.00 USD | 18,360.00 USD | 0.00 USD | 66,870.00 USD |
| `1D` | `0.3051` | 13,840,000.00 USD | 0.00 USD | 13,840,000.00 USD | 18,730.00 USD | 2,510.00 USD | 11,570.00 USD |
| `1D` | `0.3055` | 13,800,000.00 USD | 0.00 USD | 13,800,000.00 USD | 28,250.00 USD | 13,380.00 USD | 37,740.00 USD |
| `7D` | `0.3055` | 20,730,000.00 USD | 0.00 USD | 20,730,000.00 USD | 1,490.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3061` | 20,730,000.00 USD | 0.00 USD | 20,730,000.00 USD | 32,930.00 USD | 7,690.00 USD | 37,210.00 USD |
| `1D` | `0.3063` | 13,720,000.00 USD | 0.00 USD | 13,720,000.00 USD | 885.25 USD | 16,530.00 USD | 56,460.00 USD |
| `1D` | `0.3067` | 13,650,000.00 USD | 0.00 USD | 13,650,000.00 USD | 31,110.00 USD | 15,440.00 USD | 35,690.00 USD |
| `7D` | `0.3067` | 20,650,000.00 USD | 0.00 USD | 20,650,000.00 USD | 6,300.00 USD | 8,110.00 USD | 0.00 USD |
| `1D` | `0.3071` | 13,570,000.00 USD | 0.00 USD | 13,570,000.00 USD | 67.24 USD | 0.00 USD | 12,760.00 USD |
| `7D` | `0.3073` | 20,640,000.00 USD | 0.00 USD | 20,640,000.00 USD | 7,990.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3075` | 13,550,000.00 USD | 0.00 USD | 13,550,000.00 USD | 23,570.00 USD | 1,940.00 USD | 0.00 USD |
| `1D` | `0.3079` | 13,530,000.00 USD | 0.00 USD | 13,530,000.00 USD | 15.29 USD | 0.00 USD | 12,250.00 USD |
| `7D` | `0.3079` | 20,630,000.00 USD | 0.00 USD | 20,630,000.00 USD | 37,350.00 USD | 10,270.00 USD | 50,200.00 USD |
| `1D` | `0.3083` | 13,520,000.00 USD | 0.00 USD | 13,520,000.00 USD | 18,620.00 USD | 0.00 USD | 15,810.00 USD |
| `7D` | `0.3085` | 20,530,000.00 USD | 0.00 USD | 20,530,000.00 USD | 3,660.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3087` | 13,480,000.00 USD | 0.00 USD | 13,480,000.00 USD | 623.99 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3091` | 13,480,000.00 USD | 0.00 USD | 13,480,000.00 USD | 31.03 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3091` | 20,530,000.00 USD | 0.00 USD | 20,530,000.00 USD | 7,040.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3095` | 13,480,000.00 USD | 0.00 USD | 13,480,000.00 USD | 17,320.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3097` | 20,520,000.00 USD | 0.00 USD | 20,520,000.00 USD | 79,880.00 USD | 3,620.00 USD | 54,360.00 USD |
| `1D` | `0.3099` | 13,460,000.00 USD | 0.00 USD | 13,460,000.00 USD | 8,120.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3103` | 13,460,000.00 USD | 0.00 USD | 13,460,000.00 USD | 58,110.00 USD | 15,820.00 USD | 46,470.00 USD |
| `7D` | `0.3103` | 20,380,000.00 USD | 0.00 USD | 20,380,000.00 USD | 67,180.00 USD | 0.00 USD | 63,310.00 USD |
| `1D` | `0.3107` | 13,340,000.00 USD | 0.00 USD | 13,340,000.00 USD | 1,350.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3109` | 20,250,000.00 USD | 0.00 USD | 20,250,000.00 USD | 19,040.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3115` | 13,330,000.00 USD | 0.00 USD | 13,330,000.00 USD | 977.81 USD | 9,110.00 USD | 17,620.00 USD |
| `7D` | `0.3115` | 20,230,000.00 USD | 0.00 USD | 20,230,000.00 USD | 10,250.00 USD | 0.00 USD | 37,490.00 USD |
| `1D` | `0.3119` | 13,310,000.00 USD | 0.00 USD | 13,310,000.00 USD | 26,060.00 USD | 10,650.00 USD | 17,440.00 USD |
| `7D` | `0.3121` | 20,180,000.00 USD | 0.00 USD | 20,180,000.00 USD | 162,320.00 USD | 19,620.00 USD | 0.00 USD |
| `1D` | `0.3123` | 13,250,000.00 USD | 0.00 USD | 13,250,000.00 USD | 12,740.00 USD | 0.00 USD | 16,390.00 USD |
| `1D` | `0.3127` | 13,220,000.00 USD | 0.00 USD | 13,220,000.00 USD | 2,560.00 USD | 39,470.00 USD | 7,580.00 USD |
| `7D` | `0.3127` | 20,000,000.00 USD | 0.00 USD | 20,000,000.00 USD | 12,250.00 USD | 54,460.00 USD | 57,690.00 USD |
| `1D` | `0.3131` | 13,170,000.00 USD | 0.00 USD | 13,170,000.00 USD | 3,600.00 USD | 2,520.00 USD | 21,520.00 USD |
| `7D` | `0.3133` | 19,880,000.00 USD | 0.00 USD | 19,880,000.00 USD | 4,440.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3135` | 13,150,000.00 USD | 0.00 USD | 13,150,000.00 USD | 5,830.00 USD | 23,940.00 USD | 9,590.00 USD |
| `1D` | `0.3139` | 13,110,000.00 USD | 0.00 USD | 13,110,000.00 USD | 4,710.00 USD | 10,610.00 USD | 0.00 USD |
| `7D` | `0.3139` | 19,870,000.00 USD | 0.00 USD | 19,870,000.00 USD | 3,330.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3143` | 13,090,000.00 USD | 0.00 USD | 13,090,000.00 USD | 3,210.00 USD | 3,580.00 USD | 9,540.00 USD |
| `7D` | `0.3145` | 19,870,000.00 USD | 0.00 USD | 19,870,000.00 USD | 247,920.00 USD | 51,270.00 USD | 17,870.00 USD |
| `1D` | `0.3147` | 13,070,000.00 USD | 0.00 USD | 13,070,000.00 USD | 2,670.00 USD | 2,330.00 USD | 0.00 USD |
| `1D` | `0.3151` | 13,070,000.00 USD | 0.00 USD | 13,070,000.00 USD | 4,850.00 USD | 23,750.00 USD | 0.00 USD |
| `7D` | `0.3151` | 19,550,000.00 USD | 0.00 USD | 19,550,000.00 USD | 204,770.00 USD | 23,130.00 USD | 49,320.00 USD |
| `1D` | `0.3155` | 13,040,000.00 USD | 0.00 USD | 13,040,000.00 USD | 33,260.00 USD | 3,680.00 USD | 10,790.00 USD |
| `7D` | `0.3157` | 19,280,000.00 USD | 0.00 USD | 19,280,000.00 USD | 393,880.00 USD | 93,740.00 USD | 60,300.00 USD |
| `1D` | `0.3159` | 12,990,000.00 USD | 0.00 USD | 12,990,000.00 USD | 5,120.00 USD | 0.00 USD | 5,450.00 USD |
| `1D` | `0.3163` | 12,980,000.00 USD | 0.00 USD | 12,980,000.00 USD | 3,780.00 USD | 33,960.00 USD | 0.00 USD |
| `7D` | `0.3163` | 18,730,000.00 USD | 0.00 USD | 18,730,000.00 USD | 495,020.00 USD | 174,600.00 USD | 189,520.00 USD |
| `1D` | `0.3167` | 12,950,000.00 USD | 0.00 USD | 12,950,000.00 USD | 43,210.00 USD | 6,270.00 USD | 17,210.00 USD |
| `7D` | `0.3169` | 17,870,000.00 USD | 0.00 USD | 17,870,000.00 USD | 417,170.00 USD | 104,590.00 USD | 135,950.00 USD |
| `1D` | `0.3171` | 12,880,000.00 USD | 0.00 USD | 12,880,000.00 USD | 8,020.00 USD | 35,130.00 USD | 35,030.00 USD |
| `1D` | `0.3175` | 12,800,000.00 USD | 0.00 USD | 12,800,000.00 USD | 19,750.00 USD | 7,370.00 USD | 14,490.00 USD |
| `7D` | `0.3175` | 17,210,000.00 USD | 0.00 USD | 17,210,000.00 USD | 140,810.00 USD | 53,470.00 USD | 69,280.00 USD |
| `1D` | `0.3179` | 12,760,000.00 USD | 0.00 USD | 12,760,000.00 USD | 62,280.00 USD | 25,310.00 USD | 43,110.00 USD |
| `7D` | `0.3181` | 16,950,000.00 USD | 0.00 USD | 16,950,000.00 USD | 738,240.00 USD | 76,910.00 USD | 182,330.00 USD |
| `1D` | `0.3183` | 12,630,000.00 USD | 0.00 USD | 12,630,000.00 USD | 359,160.00 USD | 39,030.00 USD | 72,750.00 USD |
| `1D` | `0.3187` | 12,160,000.00 USD | 0.00 USD | 12,160,000.00 USD | 92,220.00 USD | 41,750.00 USD | 77,560.00 USD |
| `7D` | `0.3187` | 15,950,000.00 USD | 0.00 USD | 15,950,000.00 USD | 407,530.00 USD | 97,820.00 USD | 24,770.00 USD |
| `1D` | `0.3191` | 11,950,000.00 USD | 0.00 USD | 11,950,000.00 USD | 203,200.00 USD | 13,910.00 USD | 45,560.00 USD |
| `7D` | `0.3193` | 15,420,000.00 USD | 0.00 USD | 15,420,000.00 USD | 180,550.00 USD | 123,840.00 USD | 247,300.00 USD |
| `1D` | `0.3195` | 11,680,000.00 USD | 0.00 USD | 11,680,000.00 USD | 93,760.00 USD | 169,840.00 USD | 242,890.00 USD |
| `1D` | `0.3199` | 11,180,000.00 USD | 0.00 USD | 11,180,000.00 USD | 82,300.00 USD | 60,220.00 USD | 102,370.00 USD |
| `7D` | `0.3199` | 14,870,000.00 USD | 0.00 USD | 14,870,000.00 USD | 0.00 USD | 191,160.00 USD | 267,030.00 USD |
| `1D` | `0.3203` | 10,930,000.00 USD | 0.00 USD | 10,930,000.00 USD | 246,790.00 USD | 56,790.00 USD | 109,780.00 USD |
| `7D` | `0.3205` | 14,410,000.00 USD | 0.00 USD | 14,410,000.00 USD | 167,490.00 USD | 59,200.00 USD | 130,760.00 USD |
| `1D` | `0.3207` | 10,520,000.00 USD | 0.00 USD | 10,520,000.00 USD | 133,880.00 USD | 25,490.00 USD | 108,030.00 USD |
| `1D` | `0.3211` | 10,250,000.00 USD | 0.00 USD | 10,250,000.00 USD | 108,130.00 USD | 27,010.00 USD | 99,450.00 USD |
| `7D` | `0.3211` | 14,050,000.00 USD | 0.00 USD | 14,050,000.00 USD | 568,110.00 USD | 135,070.00 USD | 244,340.00 USD |
| `1D` | `0.3215` | 10,020,000.00 USD | 0.00 USD | 10,020,000.00 USD | 0.00 USD | 33,650.00 USD | 130,970.00 USD |
| `7D` | `0.3217` | 13,110,000.00 USD | 0.00 USD | 13,110,000.00 USD | 285,190.00 USD | 58,690.00 USD | 107,900.00 USD |
| `1D` | `0.3219` | 9,850,000.00 USD | 0.00 USD | 9,850,000.00 USD | 5,550.00 USD | 23,450.00 USD | 96,920.00 USD |
| `1D` | `0.3223` | 9,730,000.00 USD | 0.00 USD | 9,730,000.00 USD | 154,560.00 USD | 41,870.00 USD | 120,750.00 USD |
| `7D` | `0.3223` | 12,650,000.00 USD | 0.00 USD | 12,650,000.00 USD | 643,460.00 USD | 265,170.00 USD | 156,030.00 USD |
| `1D` | `0.3227` | 9,410,000.00 USD | 0.00 USD | 9,410,000.00 USD | 52,010.00 USD | 50,480.00 USD | 81,740.00 USD |
| `7D` | `0.3229` | 11,590,000.00 USD | 0.00 USD | 11,590,000.00 USD | 858,070.00 USD | 283,650.00 USD | 518,610.00 USD |
| `1D` | `0.3231` | 9,220,000.00 USD | 0.00 USD | 9,220,000.00 USD | 54,440.00 USD | 17,630.00 USD | 120,280.00 USD |
| `1D` | `0.3235` | 9,030,000.00 USD | 0.00 USD | 9,030,000.00 USD | 61,120.00 USD | 102,040.00 USD | 151,550.00 USD |
| `7D` | `0.3235` | 9,930,000.00 USD | 0.00 USD | 9,930,000.00 USD | 709,160.00 USD | 228,450.00 USD | 359,100.00 USD |
| `1D` | `0.3239` | 8,720,000.00 USD | 0.00 USD | 8,720,000.00 USD | 0.00 USD | 32,340.00 USD | 65,220.00 USD |
| `7D` | `0.3241` | 8,630,000.00 USD | 0.00 USD | 8,630,000.00 USD | 432,660.00 USD | 149,860.00 USD | 138,560.00 USD |
| `1D` | `0.3243` | 8,620,000.00 USD | 0.00 USD | 8,620,000.00 USD | 125,350.00 USD | 41,210.00 USD | 223,350.00 USD |
| `1D` | `0.3247` | 8,230,000.00 USD | 0.00 USD | 8,230,000.00 USD | 331,430.00 USD | 76,120.00 USD | 204,890.00 USD |
| `7D` | `0.3247` | 7,910,000.00 USD | 0.00 USD | 7,910,000.00 USD | 846,180.00 USD | 127,310.00 USD | 353,590.00 USD |
| `1D` | `0.3251` | 7,620,000.00 USD | 0.00 USD | 7,620,000.00 USD | 674,140.00 USD | 89,590.00 USD | 300,060.00 USD |
| `7D` | `0.3253` | 6,580,000.00 USD | 0.00 USD | 6,580,000.00 USD | 1,220,000.00 USD | 137,440.00 USD | 241,690.00 USD |
| `1D` | `0.3255` | 6,550,000.00 USD | 0.00 USD | 6,550,000.00 USD | 428,540.00 USD | 89,190.00 USD | 271,020.00 USD |
| `1D` | `0.3259` | 5,760,000.00 USD | 0.00 USD | 5,760,000.00 USD | 346,750.00 USD | 215,120.00 USD | 414,300.00 USD |
| `7D` | `0.3259` | 4,980,000.00 USD | 0.00 USD | 4,980,000.00 USD | 306,910.00 USD | 288,370.00 USD | 503,650.00 USD |
| `1D` | `0.3263` | 4,790,000.00 USD | 0.00 USD | 4,790,000.00 USD | 27,080.00 USD | 240,230.00 USD | 320,610.00 USD |
| `7D` | `0.3265` | 3,880,000.00 USD | 0.00 USD | 3,880,000.00 USD | 80,120.00 USD | 324,810.00 USD | 500,270.00 USD |
| `1D` | `0.3267` | 4,200,000.00 USD | 0.00 USD | 4,200,000.00 USD | 44,720.00 USD | 159,870.00 USD | 341,370.00 USD |
| `1D` | `0.3271` | 3,650,000.00 USD | 0.00 USD | 3,650,000.00 USD | 237,730.00 USD | 81,010.00 USD | 340,330.00 USD |
| `7D` | `0.3271` | 2,980,000.00 USD | 0.00 USD | 2,980,000.00 USD | 320,700.00 USD | 138,680.00 USD | 261,530.00 USD |
| `1D` | `0.3275` | 3,000,000.00 USD | 0.00 USD | 3,000,000.00 USD | 259,200.00 USD | 54,310.00 USD | 140,050.00 USD |
| `7D` | `0.3277` | 2,260,000.00 USD | 0.00 USD | 2,260,000.00 USD | 0.00 USD | 29,390.00 USD | 85,620.00 USD |
| `1D` | `0.3279` | 2,540,000.00 USD | 0.00 USD | 2,540,000.00 USD | 164,690.00 USD | 55,350.00 USD | 133,800.00 USD |
| `1D` | `0.3283` | 2,190,000.00 USD | 0.00 USD | 2,190,000.00 USD | 0.00 USD | 29,070.00 USD | 169,660.00 USD |
| `7D` | `0.3283` | 2,140,000.00 USD | 0.00 USD | 2,140,000.00 USD | 89,030.00 USD | 61,340.00 USD | 275,050.00 USD |
| `1D` | `0.3287` | 1,990,000.00 USD | 0.00 USD | 1,990,000.00 USD | 117,140.00 USD | 39,260.00 USD | 146,190.00 USD |
| `7D` | `0.3289` | 1,720,000.00 USD | 0.00 USD | 1,720,000.00 USD | 0.00 USD | 180,260.00 USD | 105,320.00 USD |
| `1D` | `0.3291` | 1,690,000.00 USD | 0.00 USD | 1,690,000.00 USD | 38,710.00 USD | 66,400.00 USD | 119,580.00 USD |
| `1D` | `0.3295` | 1,460,000.00 USD | 0.00 USD | 1,460,000.00 USD | 61,960.00 USD | 15,860.00 USD | 0.00 USD |
| `7D` | `0.3295` | 1,430,000.00 USD | 0.00 USD | 1,430,000.00 USD | 254,700.00 USD | 83,080.00 USD | 279,140.00 USD |
| `1D` | `0.3299` | 1,380,000.00 USD | 0.00 USD | 1,380,000.00 USD | 141,790.00 USD | 18,090.00 USD | 30,950.00 USD |
| `7D` | `0.3301` | 815,180.00 USD | 0.00 USD | 815,180.00 USD | 185,020.00 USD | 47,610.00 USD | 0.00 USD |
| `1D` | `0.3303` | 1,190,000.00 USD | 0.00 USD | 1,190,000.00 USD | 1,210.00 USD | 67,660.00 USD | 74,690.00 USD |
| `1D` | `0.3307` | 1,050,000.00 USD | 0.00 USD | 1,050,000.00 USD | 121,770.00 USD | 37,920.00 USD | 87,100.00 USD |
| `7D` | `0.3307` | 582,550.00 USD | 0.00 USD | 582,550.00 USD | 167,950.00 USD | 10,690.00 USD | 294,170.00 USD |
| `1D` | `0.3311` | 803,120.00 USD | 0.00 USD | 803,120.00 USD | 644.45 USD | 100,700.00 USD | 416,060.00 USD |
| `7D` | `0.3313` | 109,740.00 USD | 0.00 USD | 109,740.00 USD | 0.00 USD | 50,650.00 USD | 0.00 USD |
| `1D` | `0.3315` | 285,720.00 USD | 0.00 USD | 285,720.00 USD | 0.00 USD | 65,830.00 USD | 28,340.00 USD |
| `1D` | `0.3319` | 191,550.00 USD | 0.00 USD | 191,550.00 USD | 0.00 USD | 47,270.00 USD | 0.00 USD |
| `7D` | `0.3319` | 59,090.00 USD | 0.00 USD | 59,090.00 USD | 0.00 USD | 57,890.00 USD | 0.00 USD |
| `1D` | `0.3359` | 144,280.00 USD | 0.00 USD | 144,280.00 USD | 0.00 USD | 0.00 USD | 144,280.00 USD |
| `7D` | `0.3361` | 1,200.00 USD | 0.00 USD | 1,200.00 USD | 1,200.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3366` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3367` | 72,920.00 USD | 72,920.00 USD | 0.00 USD | 72,920.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3375` | 402,560.00 USD | 402,560.00 USD | 0.00 USD | 329,640.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3380` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3383` | 502,490.00 USD | 502,490.00 USD | 0.00 USD | 71,900.00 USD | 0.00 USD | 28,030.00 USD |
| `7D` | `0.3385` | 125,650.00 USD | 125,650.00 USD | 0.00 USD | 125,650.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3387` | 678,170.00 USD | 678,170.00 USD | 0.00 USD | 137,130.00 USD | 11,160.00 USD | 27,380.00 USD |
| `1D` | `0.3391` | 1,010,000.00 USD | 1,010,000.00 USD | 0.00 USD | 258,550.00 USD | 27,820.00 USD | 49,390.00 USD |
| `7D` | `0.3391` | 484,990.00 USD | 484,990.00 USD | 0.00 USD | 124,670.00 USD | 0.00 USD | 234,660.00 USD |
| `1D` | `0.3395` | 1,950,000.00 USD | 1,950,000.00 USD | 0.00 USD | 115,280.00 USD | 333,450.00 USD | 485,780.00 USD |
| `7D` | `0.3397` | 1,910,000.00 USD | 1,910,000.00 USD | 0.00 USD | 257,550.00 USD | 752,550.00 USD | 410,830.00 USD |
| `1D` | `0.3399` | 2,330,000.00 USD | 2,330,000.00 USD | 0.00 USD | 43,780.00 USD | 120,440.00 USD | 218,200.00 USD |
| `1D` | `0.3403` | 2,940,000.00 USD | 2,940,000.00 USD | 0.00 USD | 209,800.00 USD | 61,580.00 USD | 336,240.00 USD |
| `7D` | `0.3403` | 3,580,000.00 USD | 3,580,000.00 USD | 0.00 USD | 1,200,000.00 USD | 103,630.00 USD | 376,470.00 USD |
| `1D` | `0.3407` | 3,110,000.00 USD | 3,110,000.00 USD | 0.00 USD | 71,510.00 USD | 0.00 USD | 100,230.00 USD |
| `7D` | `0.3409` | 4,060,000.00 USD | 4,060,000.00 USD | 0.00 USD | 0.00 USD | 29,390.00 USD | 446,990.00 USD |
| `1D` | `0.3411` | 3,460,000.00 USD | 3,460,000.00 USD | 0.00 USD | 265,070.00 USD | 39,790.00 USD | 45,840.00 USD |
| `1D` | `0.3415` | 4,370,000.00 USD | 4,370,000.00 USD | 0.00 USD | 672,650.00 USD | 21,540.00 USD | 211,420.00 USD |
| `7D` | `0.3415` | 4,180,000.00 USD | 4,180,000.00 USD | 0.00 USD | 0.00 USD | 35,670.00 USD | 85,620.00 USD |
| `1D` | `0.3419` | 4,500,000.00 USD | 4,500,000.00 USD | 0.00 USD | 39,640.00 USD | 48,460.00 USD | 48,810.00 USD |
| `7D` | `0.3421` | 4,220,000.00 USD | 4,220,000.00 USD | 0.00 USD | 0.00 USD | 43,290.00 USD | 0.00 USD |
| `1D` | `0.3423` | 4,610,000.00 USD | 4,610,000.00 USD | 0.00 USD | 71,180.00 USD | 33,440.00 USD | 0.00 USD |
| `1D` | `0.3427` | 4,800,000.00 USD | 4,800,000.00 USD | 0.00 USD | 0.00 USD | 195,320.00 USD | 0.00 USD |
| `7D` | `0.3427` | 4,840,000.00 USD | 4,840,000.00 USD | 0.00 USD | 0.00 USD | 229,350.00 USD | 384,460.00 USD |
| `1D` | `0.3431` | 5,160,000.00 USD | 5,160,000.00 USD | 0.00 USD | 166,310.00 USD | 193,980.00 USD | 0.00 USD |
| `7D` | `0.3433` | 5,130,000.00 USD | 5,130,000.00 USD | 0.00 USD | 254,700.00 USD | 38,560.00 USD | 0.00 USD |
| `1D` | `0.3435` | 5,310,000.00 USD | 5,310,000.00 USD | 0.00 USD | 0.00 USD | 117,530.00 USD | 30,950.00 USD |
| `1D` | `0.3439` | 5,420,000.00 USD | 5,420,000.00 USD | 0.00 USD | 0.00 USD | 40,260.00 USD | 62,980.00 USD |
| `1D` | `0.3443` | 5,470,000.00 USD | 5,470,000.00 USD | 0.00 USD | 0.00 USD | 38,110.00 USD | 18,140.00 USD |
| `7D` | `0.3445` | 5,230,000.00 USD | 5,230,000.00 USD | 0.00 USD | 103,130.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3447` | 5,700,000.00 USD | 5,700,000.00 USD | 0.00 USD | 22,420.00 USD | 57,000.00 USD | 146,340.00 USD |
| `1D` | `0.3451` | 5,930,000.00 USD | 5,930,000.00 USD | 0.00 USD | 70,130.00 USD | 63,000.00 USD | 99,020.00 USD |
| `7D` | `0.3451` | 5,320,000.00 USD | 5,320,000.00 USD | 0.00 USD | 62,830.00 USD | 28,550.00 USD | 0.00 USD |
| `1D` | `0.3455` | 6,250,000.00 USD | 6,250,000.00 USD | 0.00 USD | 169,370.00 USD | 37,860.00 USD | 116,160.00 USD |
| `7D` | `0.3457` | 5,750,000.00 USD | 5,750,000.00 USD | 0.00 USD | 62,340.00 USD | 29,340.00 USD | 332,190.00 USD |
| `1D` | `0.3459` | 7,080,000.00 USD | 7,080,000.00 USD | 0.00 USD | 214,990.00 USD | 131,290.00 USD | 485,400.00 USD |
| `1D` | `0.3463` | 7,380,000.00 USD | 7,380,000.00 USD | 0.00 USD | 13,540.00 USD | 118,340.00 USD | 160,310.00 USD |
| `7D` | `0.3463` | 6,200,000.00 USD | 6,200,000.00 USD | 0.00 USD | 0.00 USD | 250,840.00 USD | 205,410.00 USD |
| `1D` | `0.3467` | 7,550,000.00 USD | 7,550,000.00 USD | 0.00 USD | 21,890.00 USD | 48,850.00 USD | 100,110.00 USD |
| `7D` | `0.3469` | 6,530,000.00 USD | 6,530,000.00 USD | 0.00 USD | 124,720.00 USD | 51,820.00 USD | 152,060.00 USD |
| `1D` | `0.3471` | 7,650,000.00 USD | 7,650,000.00 USD | 0.00 USD | 37,620.00 USD | 38,220.00 USD | 25,030.00 USD |
| `1D` | `0.3475` | 7,750,000.00 USD | 7,750,000.00 USD | 0.00 USD | 0.00 USD | 59,710.00 USD | 45,010.00 USD |
| `7D` | `0.3475` | 6,570,000.00 USD | 6,570,000.00 USD | 0.00 USD | 0.00 USD | 40,540.00 USD | 0.00 USD |
| `1D` | `0.3479` | 8,000,000.00 USD | 8,000,000.00 USD | 0.00 USD | 105,220.00 USD | 16,550.00 USD | 120,420.00 USD |
| `7D` | `0.3481` | 6,660,000.00 USD | 6,660,000.00 USD | 0.00 USD | 6,440.00 USD | 32,530.00 USD | 42,810.00 USD |
| `1D` | `0.3483` | 8,080,000.00 USD | 8,080,000.00 USD | 0.00 USD | 3,430.00 USD | 22,220.00 USD | 60,430.00 USD |
| `1D` | `0.3487` | 8,140,000.00 USD | 8,140,000.00 USD | 0.00 USD | 8,610.00 USD | 27,650.00 USD | 24,410.00 USD |
| `7D` | `0.3487` | 6,690,000.00 USD | 6,690,000.00 USD | 0.00 USD | 8,310.00 USD | 21,650.00 USD | 0.00 USD |
| `1D` | `0.3491` | 8,270,000.00 USD | 8,270,000.00 USD | 0.00 USD | 40,710.00 USD | 28,080.00 USD | 61,240.00 USD |
| `7D` | `0.3493` | 6,980,000.00 USD | 6,980,000.00 USD | 0.00 USD | 10,490.00 USD | 93,150.00 USD | 192,230.00 USD |
| `1D` | `0.3495` | 8,400,000.00 USD | 8,400,000.00 USD | 0.00 USD | 34,020.00 USD | 13,050.00 USD | 79,030.00 USD |
| `1D` | `0.3499` | 8,840,000.00 USD | 8,840,000.00 USD | 0.00 USD | 52,670.00 USD | 9,040.00 USD | 375,650.00 USD |
| `7D` | `0.3499` | 7,120,000.00 USD | 7,120,000.00 USD | 0.00 USD | 139,880.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3503` | 8,920,000.00 USD | 8,920,000.00 USD | 0.00 USD | 0.00 USD | 29,350.00 USD | 50,760.00 USD |
| `7D` | `0.3505` | 7,150,000.00 USD | 7,150,000.00 USD | 0.00 USD | 11,960.00 USD | 19,280.00 USD | 0.00 USD |
| `1D` | `0.3507` | 9,040,000.00 USD | 9,040,000.00 USD | 0.00 USD | 75,920.00 USD | 12,560.00 USD | 31,490.00 USD |
| `1D` | `0.3511` | 9,070,000.00 USD | 9,070,000.00 USD | 0.00 USD | 1,090.00 USD | 4,320.00 USD | 32,490.00 USD |
| `7D` | `0.3511` | 8,110,000.00 USD | 8,110,000.00 USD | 0.00 USD | 690,500.00 USD | 0.00 USD | 271,800.00 USD |
| `1D` | `0.3515` | 9,180,000.00 USD | 9,180,000.00 USD | 0.00 USD | 21,910.00 USD | 0.00 USD | 87,340.00 USD |
| `1D` | `0.3519` | 9,270,000.00 USD | 9,270,000.00 USD | 0.00 USD | 31,190.00 USD | 23,960.00 USD | 28,330.00 USD |
| `1D` | `0.3523` | 9,270,000.00 USD | 9,270,000.00 USD | 0.00 USD | 3,190.00 USD | 3,730.00 USD | 0.00 USD |
| `7D` | `0.3523` | 8,530,000.00 USD | 8,530,000.00 USD | 0.00 USD | 277,410.00 USD | 28,950.00 USD | 107,430.00 USD |
| `1D` | `0.3527` | 9,440,000.00 USD | 9,440,000.00 USD | 0.00 USD | 102,610.00 USD | 38,340.00 USD | 28,910.00 USD |
| `1D` | `0.3531` | 9,600,000.00 USD | 9,600,000.00 USD | 0.00 USD | 6,270.00 USD | 61,120.00 USD | 88,110.00 USD |
| `1D` | `0.3535` | 9,850,000.00 USD | 9,850,000.00 USD | 0.00 USD | 125,280.00 USD | 16,340.00 USD | 113,320.00 USD |
| `7D` | `0.3535` | 8,800,000.00 USD | 8,800,000.00 USD | 0.00 USD | 4,830.00 USD | 77,960.00 USD | 187,450.00 USD |
| `1D` | `0.3539` | 10,030,000.00 USD | 10,030,000.00 USD | 0.00 USD | 57,460.00 USD | 33,520.00 USD | 81,960.00 USD |
| `7D` | `0.3541` | 9,730,000.00 USD | 9,730,000.00 USD | 0.00 USD | 810,900.00 USD | 118,370.00 USD | 0.00 USD |
| `1D` | `0.3543` | 10,200,000.00 USD | 10,200,000.00 USD | 0.00 USD | 28,820.00 USD | 107,380.00 USD | 37,920.00 USD |
| `1D` | `0.3547` | 10,270,000.00 USD | 10,270,000.00 USD | 0.00 USD | 5,090.00 USD | 28,920.00 USD | 31,910.00 USD |
| `7D` | `0.3547` | 10,020,000.00 USD | 10,020,000.00 USD | 0.00 USD | 5,390.00 USD | 0.00 USD | 288,450.00 USD |
| `1D` | `0.3551` | 10,350,000.00 USD | 10,350,000.00 USD | 0.00 USD | 4,060.00 USD | 29,900.00 USD | 47,950.00 USD |
| `7D` | `0.3553` | 10,150,000.00 USD | 10,150,000.00 USD | 0.00 USD | 12,710.00 USD | 117,050.00 USD | 0.00 USD |
| `1D` | `0.3555` | 10,410,000.00 USD | 10,410,000.00 USD | 0.00 USD | 20,180.00 USD | 44,130.00 USD | 0.00 USD |
| `1D` | `0.3559` | 10,510,000.00 USD | 10,510,000.00 USD | 0.00 USD | 331.60 USD | 21,340.00 USD | 78,340.00 USD |
| `7D` | `0.3559` | 10,170,000.00 USD | 10,170,000.00 USD | 0.00 USD | 13,500.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3563` | 10,610,000.00 USD | 10,610,000.00 USD | 0.00 USD | 977.81 USD | 29,510.00 USD | 67,310.00 USD |
| `7D` | `0.3565` | 10,210,000.00 USD | 10,210,000.00 USD | 0.00 USD | 0.00 USD | 43,060.00 USD | 0.00 USD |
| `1D` | `0.3567` | 10,610,000.00 USD | 10,610,000.00 USD | 0.00 USD | 3,540.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3571` | 10,620,000.00 USD | 10,620,000.00 USD | 0.00 USD | 1,770.00 USD | 6,920.00 USD | 0.00 USD |
| `1D` | `0.3575` | 10,790,000.00 USD | 10,790,000.00 USD | 0.00 USD | 161,360.00 USD | 9,250.00 USD | 0.00 USD |
| `7D` | `0.3577` | 10,330,000.00 USD | 10,330,000.00 USD | 0.00 USD | 124,630.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3579` | 10,840,000.00 USD | 10,840,000.00 USD | 0.00 USD | 2,200.00 USD | 9,130.00 USD | 38,950.00 USD |
| `1D` | `0.3583` | 10,870,000.00 USD | 10,870,000.00 USD | 0.00 USD | 14,980.00 USD | 14,930.00 USD | 0.00 USD |
| `7D` | `0.3583` | 10,470,000.00 USD | 10,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 135,900.00 USD |
| `1D` | `0.3587` | 10,880,000.00 USD | 10,880,000.00 USD | 0.00 USD | 5,760.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3589` | 10,840,000.00 USD | 10,840,000.00 USD | 0.00 USD | 0.00 USD | 50,650.00 USD | 320,430.00 USD |
| `1D` | `0.3591` | 10,950,000.00 USD | 10,950,000.00 USD | 0.00 USD | 22,510.00 USD | 15,750.00 USD | 33,590.00 USD |
| `1D` | `0.3595` | 11,140,000.00 USD | 11,140,000.00 USD | 0.00 USD | 93,010.00 USD | 0.00 USD | 99,590.00 USD |
| `7D` | `0.3595` | 10,990,000.00 USD | 10,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 146,290.00 USD |
| `1D` | `0.3599` | 11,320,000.00 USD | 11,320,000.00 USD | 0.00 USD | 47,370.00 USD | 22,780.00 USD | 108,510.00 USD |
| `7D` | `0.3601` | 11,490,000.00 USD | 11,490,000.00 USD | 0.00 USD | 4,230.00 USD | 161,200.00 USD | 338,540.00 USD |
| `1D` | `0.3603` | 11,490,000.00 USD | 11,490,000.00 USD | 0.00 USD | 32,230.00 USD | 41,780.00 USD | 92,600.00 USD |
| `1D` | `0.3607` | 11,700,000.00 USD | 11,700,000.00 USD | 0.00 USD | 28,890.00 USD | 22,500.00 USD | 157,390.00 USD |
| `7D` | `0.3607` | 11,890,000.00 USD | 11,890,000.00 USD | 0.00 USD | 330,010.00 USD | 68,030.00 USD | 0.00 USD |
| `1D` | `0.3611` | 12,030,000.00 USD | 12,030,000.00 USD | 0.00 USD | 86,030.00 USD | 54,830.00 USD | 190,770.00 USD |
| `7D` | `0.3613` | 12,580,000.00 USD | 12,580,000.00 USD | 0.00 USD | 73,920.00 USD | 330,040.00 USD | 288,930.00 USD |
| `1D` | `0.3615` | 12,210,000.00 USD | 12,210,000.00 USD | 0.00 USD | 0.00 USD | 31,910.00 USD | 150,170.00 USD |
| `1D` | `0.3619` | 12,690,000.00 USD | 12,690,000.00 USD | 0.00 USD | 368,610.00 USD | 110,060.00 USD | 0.00 USD |
| `7D` | `0.3619` | 12,790,000.00 USD | 12,790,000.00 USD | 0.00 USD | 3,790.00 USD | 209,940.00 USD | 0.00 USD |
| `1D` | `0.3623` | 12,870,000.00 USD | 12,870,000.00 USD | 0.00 USD | 83,390.00 USD | 20,060.00 USD | 71,510.00 USD |
| `7D` | `0.3625` | 12,990,000.00 USD | 12,990,000.00 USD | 0.00 USD | 2,300.00 USD | 191,880.00 USD | 0.00 USD |
| `1D` | `0.3627` | 13,240,000.00 USD | 13,240,000.00 USD | 0.00 USD | 337,420.00 USD | 39,070.00 USD | 0.00 USD |
| `1D` | `0.3631` | 14,380,000.00 USD | 14,380,000.00 USD | 0.00 USD | 941,740.00 USD | 102,260.00 USD | 93,510.00 USD |
| `7D` | `0.3631` | 13,100,000.00 USD | 13,100,000.00 USD | 0.00 USD | 738.08 USD | 114,740.00 USD | 0.00 USD |
| `1D` | `0.3635` | 14,610,000.00 USD | 14,610,000.00 USD | 0.00 USD | 0.00 USD | 48,500.00 USD | 185,880.00 USD |
| `7D` | `0.3637` | 13,130,000.00 USD | 13,130,000.00 USD | 0.00 USD | 1,090.00 USD | 21,530.00 USD | 0.00 USD |
| `1D` | `0.3639` | 15,030,000.00 USD | 15,030,000.00 USD | 0.00 USD | 183,690.00 USD | 152,650.00 USD | 76,240.00 USD |
| `1D` | `0.3643` | 15,310,000.00 USD | 15,310,000.00 USD | 0.00 USD | 167,490.00 USD | 81,220.00 USD | 35,280.00 USD |
| `7D` | `0.3643` | 13,920,000.00 USD | 13,920,000.00 USD | 0.00 USD | 1,580.00 USD | 0.00 USD | 789,140.00 USD |
| `1D` | `0.3647` | 15,720,000.00 USD | 15,720,000.00 USD | 0.00 USD | 268,930.00 USD | 27,770.00 USD | 110,900.00 USD |
| `7D` | `0.3649` | 14,100,000.00 USD | 14,100,000.00 USD | 0.00 USD | 182,150.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3651` | 15,900,000.00 USD | 15,900,000.00 USD | 0.00 USD | 2,860.00 USD | 55,980.00 USD | 123,070.00 USD |
| `1D` | `0.3655` | 16,650,000.00 USD | 16,650,000.00 USD | 0.00 USD | 411,730.00 USD | 107,280.00 USD | 227,180.00 USD |
| `7D` | `0.3655` | 14,890,000.00 USD | 14,890,000.00 USD | 0.00 USD | 677,860.00 USD | 112,770.00 USD | 0.00 USD |
| `1D` | `0.3659` | 17,110,000.00 USD | 17,110,000.00 USD | 0.00 USD | 233,580.00 USD | 113,780.00 USD | 113,740.00 USD |
| `7D` | `0.3661` | 15,890,000.00 USD | 15,890,000.00 USD | 0.00 USD | 691,690.00 USD | 66,940.00 USD | 238,480.00 USD |
| `1D` | `0.3663` | 17,720,000.00 USD | 17,720,000.00 USD | 0.00 USD | 449,010.00 USD | 99,370.00 USD | 62,910.00 USD |
| `1D` | `0.3667` | 18,110,000.00 USD | 18,110,000.00 USD | 0.00 USD | 187,870.00 USD | 62,870.00 USD | 137,570.00 USD |
| `7D` | `0.3667` | 16,510,000.00 USD | 16,510,000.00 USD | 0.00 USD | 424,170.00 USD | 34,510.00 USD | 166,250.00 USD |
| `1D` | `0.3671` | 18,610,000.00 USD | 18,610,000.00 USD | 0.00 USD | 94,630.00 USD | 79,940.00 USD | 324,560.00 USD |
| `7D` | `0.3673` | 17,200,000.00 USD | 17,200,000.00 USD | 0.00 USD | 511,100.00 USD | 53,040.00 USD | 122,410.00 USD |
| `1D` | `0.3675` | 18,840,000.00 USD | 18,840,000.00 USD | 0.00 USD | 54,730.00 USD | 53,460.00 USD | 126,530.00 USD |
| `1D` | `0.3679` | 19,730,000.00 USD | 19,730,000.00 USD | 0.00 USD | 772,390.00 USD | 25,610.00 USD | 92,020.00 USD |
| `7D` | `0.3679` | 17,460,000.00 USD | 17,460,000.00 USD | 0.00 USD | 259,090.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3683` | 20,010,000.00 USD | 20,010,000.00 USD | 0.00 USD | 18,610.00 USD | 84,920.00 USD | 171,070.00 USD |
| `7D` | `0.3685` | 17,640,000.00 USD | 17,640,000.00 USD | 0.00 USD | 1,610.00 USD | 102,650.00 USD | 72,350.00 USD |
| `1D` | `0.3687` | 20,680,000.00 USD | 20,680,000.00 USD | 0.00 USD | 440,130.00 USD | 153,070.00 USD | 77,780.00 USD |
| `1D` | `0.3691` | 21,110,000.00 USD | 21,110,000.00 USD | 0.00 USD | 363,130.00 USD | 49,680.00 USD | 23,760.00 USD |
| `7D` | `0.3691` | 18,040,000.00 USD | 18,040,000.00 USD | 0.00 USD | 147,650.00 USD | 261,530.00 USD | 0.00 USD |
| `1D` | `0.3695` | 21,360,000.00 USD | 21,360,000.00 USD | 0.00 USD | 162,690.00 USD | 88,200.00 USD | 0.00 USD |
| `7D` | `0.3697` | 18,280,000.00 USD | 18,280,000.00 USD | 0.00 USD | 0.00 USD | 175,510.00 USD | 55,830.00 USD |
| `1D` | `0.3699` | 21,900,000.00 USD | 21,900,000.00 USD | 0.00 USD | 487,980.00 USD | 15,920.00 USD | 27,870.00 USD |
| `1D` | `0.3703` | 22,430,000.00 USD | 22,430,000.00 USD | 0.00 USD | 287,950.00 USD | 180,250.00 USD | 63,170.00 USD |
| `7D` | `0.3703` | 18,330,000.00 USD | 18,330,000.00 USD | 0.00 USD | 50,940.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3707` | 22,970,000.00 USD | 22,970,000.00 USD | 0.00 USD | 1,640.00 USD | 29,660.00 USD | 510,340.00 USD |
| `7D` | `0.3709` | 18,330,000.00 USD | 18,330,000.00 USD | 0.00 USD | 1,880.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3711` | 23,830,000.00 USD | 23,830,000.00 USD | 0.00 USD | 547,890.00 USD | 84,630.00 USD | 225,950.00 USD |
| `7D` | `0.3715` | 18,730,000.00 USD | 18,730,000.00 USD | 0.00 USD | 3,890.00 USD | 0.00 USD | 394,570.00 USD |
| `7D` | `0.3721` | 19,480,000.00 USD | 19,480,000.00 USD | 0.00 USD | 1,320.00 USD | 0.00 USD | 747,740.00 USD |
| `7D` | `0.3727` | 19,760,000.00 USD | 19,760,000.00 USD | 0.00 USD | 213,190.00 USD | 0.00 USD | 66,870.00 USD |
| `7D` | `0.3733` | 19,940,000.00 USD | 19,940,000.00 USD | 0.00 USD | 188,670.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3739` | 20,420,000.00 USD | 20,420,000.00 USD | 0.00 USD | 247,740.00 USD | 7,690.00 USD | 218,010.00 USD |
| `7D` | `0.3745` | 20,820,000.00 USD | 20,820,000.00 USD | 0.00 USD | 249,860.00 USD | 115,430.00 USD | 37,210.00 USD |
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
  * Total Open Interest: `422.53M` | Total OI Tokens: `1,261,556,295.2 TRX`
  * 1h OI Change: `+2.65%` | 4h OI Change: `+3.61%` | 24h OI Change: `+47.72%`
  * Exchange Breakdown: Binance=`106.44M` | Bybit=`83.99M` | OKX=`27.31M` | Hyperliquid=`18.98M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `-61.31K` | Last 24h: `-632.70K` | Last 3d: `-621.37K` | Last 7d: `-893.87K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `-0.0507%` | **USDT OKX** | `-0.3543%` |
| **USDT Bybit** | `0.0949%` | **USDT KuCoin** | `-0.0681%` |
| **USDT MEXC** | `-0.0477%` | **USDT BingX** | `0.0968%` |
| **USDT Gate** | `-0.1564%` | **USDT Bitget** | `-0.2084%` |
| **CoinM Binance** | `-0.1014%` | **CoinM OKX** | `-` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `TRX` | `45.70%` | `54.30%` | `0.84` | 4,640,000.00 USD |
| `15M` | `Binance` | `52.41%` | `47.59%` | `1.10` | 1,280,000.00 USD |
| `15M` | `OKX` | `52.16%` | `47.84%` | `1.09` | 539,790.00 USD |
| `15M` | `Bybit` | `35.41%` | `64.59%` | `0.55` | 479,830.00 USD |
| `15M` | `KuCoin` | `44.46%` | `55.54%` | `0.80` | 33,060.00 USD |
| `15M` | `Gate` | `83.09%` | `16.91%` | `4.91` | 111,110.00 USD |
| `15M` | `Bitget` | `39.88%` | `60.12%` | `0.66` | 204,400.00 USD |
| `15M` | `BingX` | `8.87%` | `91.13%` | `0.10` | 511,710.00 USD |
| `15M` | `MEXC` | `59.87%` | `40.13%` | `1.49` | 204,510.00 USD |
| `15M` | `Bitunix` | `64.14%` | `35.86%` | `1.79` | 74,030.00 USD |
| `15M` | `Hyperliquid` | `85.77%` | `14.23%` | `6.03` | 237,350.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `53.54%` | `46.46%` | `1.15` | 647,010.00 USD |
| `15M` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `WhiteBIT` | `0%` | `100%` | `0.00` | 249,210.00 USD |
| `15M` | `HTX` | `44.5%` | `55.5%` | `0.80` | 10,130.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `66.83%` | `33.17%` | `2.01` | 64,590.00 USD |
| `15M` | `Aster` | `100%` | `0%` | `1.00` | 194.81 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `0%` | `100%` | `0.00` | 1.31 USD |
| `15M` | `Whale Positions` | `52.41%` | `47.59%` | `1.10` | 1,280,000.00 USD |
| `15M` | `Global Accounts` | `45.70%` | `54.30%` | `0.84` | 4,640,000.00 USD |
| `1H` | `TRX` | `44.19%` | `55.81%` | `0.79` | 59,290,000.00 USD |
| `1H` | `Binance` | `46.1%` | `53.9%` | `0.86` | 34,210,000.00 USD |
| `1H` | `OKX` | `47.98%` | `52.02%` | `0.92` | 4,880,000.00 USD |
| `1H` | `Bybit` | `32.12%` | `67.88%` | `0.47` | 6,570,000.00 USD |
| `1H` | `KuCoin` | `50.94%` | `49.06%` | `1.04` | 834,890.00 USD |
| `1H` | `Gate` | `47.72%` | `52.28%` | `0.91` | 2,920,000.00 USD |
| `1H` | `Bitget` | `43.06%` | `56.94%` | `0.76` | 1,260,000.00 USD |
| `1H` | `BingX` | `52.06%` | `47.94%` | `1.09` | 1,140,000.00 USD |
| `1H` | `MEXC` | `46.33%` | `53.67%` | `0.86` | 573,290.00 USD |
| `1H` | `Bitunix` | `33.57%` | `66.43%` | `0.51` | 1,930,000.00 USD |
| `1H` | `Hyperliquid` | `57.51%` | `42.49%` | `1.35` | 1,890,000.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `55.29%` | `44.71%` | `1.24` | 349,480.00 USD |
| `1H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `WhiteBIT` | `4.52%` | `95.48%` | `0.05` | 971,990.00 USD |
| `1H` | `HTX` | `45.33%` | `54.67%` | `0.83` | 362,790.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `42.19%` | `57.81%` | `0.73` | 254,350.00 USD |
| `1H` | `Aster` | `42.76%` | `57.24%` | `0.75` | 882,260.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `53.36%` | `46.64%` | `1.14` | 261,490.00 USD |
| `1H` | `Whale Positions` | `46.1%` | `53.9%` | `0.86` | 34,210,000.00 USD |
| `1H` | `Global Accounts` | `44.19%` | `55.81%` | `0.79` | 59,290,000.00 USD |
| `4H` | `TRX` | `44.22%` | `55.78%` | `0.79` | 161,370,000.00 USD |
| `4H` | `Binance` | `44.75%` | `55.25%` | `0.81` | 58,790,000.00 USD |
| `4H` | `OKX` | `46.94%` | `53.06%` | `0.88` | 32,910,000.00 USD |
| `4H` | `Bybit` | `42.26%` | `57.74%` | `0.73` | 10,870,000.00 USD |
| `4H` | `KuCoin` | `46.39%` | `53.61%` | `0.87` | 1,150,000.00 USD |
| `4H` | `Gate` | `46.2%` | `53.8%` | `0.86` | 27,580,000.00 USD |
| `4H` | `Bitget` | `47.13%` | `52.87%` | `0.89` | 2,590,000.00 USD |
| `4H` | `BingX` | `32%` | `68%` | `0.47` | 3,130,000.00 USD |
| `4H` | `MEXC` | `44.7%` | `55.3%` | `0.81` | 8,450,000.00 USD |
| `4H` | `Bitunix` | `47.15%` | `52.85%` | `0.89` | 3,970,000.00 USD |
| `4H` | `Hyperliquid` | `65.94%` | `34.06%` | `1.94` | 1,640,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `49.99%` | `50.01%` | `1.00` | 1,120,000.00 USD |
| `4H` | `Crypto.com` | `38.92%` | `61.08%` | `0.64` | 215,170.00 USD |
| `4H` | `WhiteBIT` | `14.25%` | `85.75%` | `0.17` | 6,260,000.00 USD |
| `4H` | `HTX` | `46.44%` | `53.56%` | `0.87` | 858,230.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `53.36%` | `46.64%` | `1.14` | 863,970.00 USD |
| `4H` | `Aster` | `37.25%` | `62.75%` | `0.59` | 871,190.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `58.36%` | `41.64%` | `1.40` | 88,970.00 USD |
| `4H` | `Whale Positions` | `44.75%` | `55.25%` | `0.81` | 58,790,000.00 USD |
| `4H` | `Global Accounts` | `44.22%` | `55.78%` | `0.79` | 161,370,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `0:00 UTC` | `0.3368` | `0.3360` | `0.3368` | `0.3377` | `0.3336` | 2,717,916.28 USD | 1,271,599.87 USD | 1,446,316.41 USD | -174,716.54 USD | `-6.43%` | `5B / 15S` |
| `5:00 UTC` | `0.3312` | `0.3323` | `0.3312` | `0.3350` | `0.3309` | 3,615,541.77 USD | 1,824,507.31 USD | 1,791,034.46 USD | 33,472.85 USD | `+0.93%` | `10B / 13S` |
| `0:00 UTC` | `0.3320` | `0.3319` | `0.3320` | `0.3329` | `0.3307` | 3,613,244.76 USD | 2,074,143.60 USD | 1,539,101.16 USD | 535,042.44 USD | `+14.81%` | `13B / 9S` |
| `5:00 UTC` | `0.3320` | `0.3320` | `0.3320` | `0.3328` | `0.3316` | 3,173,620.42 USD | 1,545,938.41 USD | 1,627,682.01 USD | -81,743.60 USD | `-2.58%` | `29B / 18S` |
| `0:00 UTC` | `0.3323` | `0.3323` | `0.3323` | `0.3332` | `0.3318` | 1,965,395.58 USD | 930,788.45 USD | 1,034,607.13 USD | -103,818.67 USD | `-5.28%` | `16B / 20S` |
| `5:00 UTC` | `0.3320` | `0.3322` | `0.3320` | `0.3328` | `0.3319` | 2,011,353.25 USD | 833,950.97 USD | 1,177,402.29 USD | -343,451.32 USD | `-17.08%` | `9B / 10S` |
| `0:00 UTC` | `0.3339` | `0.3340` | `0.3339` | `0.3367` | `0.3319` | 3,824,828.40 USD | 1,984,762.45 USD | 1,840,065.95 USD | 144,696.50 USD | `+3.78%` | `20B / 6S` |
| `5:00 UTC` | `0.3351` | `0.3349` | `0.3351` | `0.3364` | `0.3341` | 1,965,380.04 USD | 899,735.78 USD | 1,065,644.26 USD | -165,908.48 USD | `-8.44%` | `11B / 14S` |
| `0:00 UTC` | `0.3351` | `0.3349` | `0.3351` | `0.3360` | `0.3335` | 1,833,198.85 USD | 904,870.52 USD | 928,328.33 USD | -23,457.81 USD | `-1.28%` | `23B / 24S` |
| `5:00 UTC` | `0.3348` | `0.3369` | `0.3348` | `0.3399` | `0.3343` | 3,092,808.76 USD | 1,520,036.24 USD | 1,572,772.52 USD | -52,736.28 USD | `-1.71%` | `17B / 11S` |

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
| `5m` | 63,470.00 USD | -291,980.00 USD | **`DISTRIBUTION`** |
| `15m` | -79,220.00 USD | -409,950.00 USD | **`DISTRIBUTION`** |
| `30m` | -1,450,000.00 USD | -288,310.00 USD | **`DISTRIBUTION`** |
| `1h` | -1,580,000.00 USD | 114,600.00 USD | **`DISTRIBUTION`** |
| `2h` | 324,990.00 USD | 1,850,000.00 USD | **`ACCUMULATION`** |
| `4h` | 3,060,000.00 USD | 2,210,000.00 USD | **`ACCUMULATION`** |
| `6h` | 7,890,000.00 USD | -5,860,000.00 USD | **`ACCUMULATION`** |
| `8h` | 13,660,000.00 USD | -6,210,000.00 USD | **`ACCUMULATION`** |
| `12h` | 22,920,000.00 USD | -2,130,000.00 USD | **`ACCUMULATION`** |
| `24h` | 20,030,000.00 USD | 5,450,000.00 USD | **`ACCUMULATION`** |
| `1w` | 13,690,000.00 USD | 4,080,000.00 USD | **`ACCUMULATION`** |
| `30d` | -10,190,000.00 USD | 5,010,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+63.47K` | 15m=`-79.22K` | 1h=`-1.58M` | 24h=`+20.03M`
* Futures Capital Netflows: 5m=`-291.98K` | 15m=`-409.95K` | 1h=`+114.60K` | 24h=`+5.45M`
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
  * `2026-10-30 15:49:55 IST`: [istat.it] - (Sentiment: `Neutral`)
  * `2026-10-30 15:32:55 IST`: [ec.europa.eu] - (Sentiment: `Neutral`)
  * `2026-10-30 15:31:55 IST`: [ec.europa.eu] - (Sentiment: `Neutral`)
  * `2026-10-30 15:18:55 IST`: [dailyforex.com] - (Sentiment: `Neutral`)
  * `2026-10-30 15:12:55 IST`: [breakingthenews.net] - (Sentiment: `Neutral`)
  * `2026-10-30 15:56:55 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 15:56:55 IST`: [@FirstSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 15:56:55 IST`: [destatis.de] - (Sentiment: `Neutral`)
  * `2026-10-30 15:56:55 IST`: [istat.it] - (Sentiment: `Neutral`)
  * `2026-10-30 15:56:55 IST`: [channelnewsasia.com] - (Sentiment: `Neutral`)
  * `2026-10-30 15:55:55 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 15:55:55 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 15:55:55 IST`: [kof.ethz.ch] - (Sentiment: `Neutral`)
  * `2026-10-30 15:55:55 IST`: [gerlachmacro.substack.com] - (Sentiment: `Neutral`)
  * `2026-10-30 15:55:55 IST`: [@financialjuice] - (Sentiment: `Neutral`)


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
  * Execution Entry: `0.3402` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `0.3314` (Risk Distance: `0.0088` pts)
  * +2.5R Take Profit: `0.3623`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `0.3578` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `0.3666` (Risk Distance: `0.0088` pts)
  * +2.5R Take Profit: `0.3357`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`0.3373`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
