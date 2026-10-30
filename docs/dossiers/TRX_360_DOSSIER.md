# 🏛️ SOVEREIGN CANDIDATE DOSSIER: TRX
**Canonical Key**: `TRX` | **Broker Instrument**: `TRXUSD.p` | **Asset Class**: `Crypto Alt L1`
**Timestamp**: `2026-10-30 15:45:20 IST` (`2026-10-30 10:15:20 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `0.3334` | **Live Ask Quote**: `0.3367` | **Mid Price**: `0.3350`
- **Spread Points**: `33.00` | **Spread BPS**: `98.49 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `0.3452` | VWAP Z-Score: `-1.30` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `0.0028` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `41.75` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `0.3733` | Lower -3.00σ Band: `0.3170`
  * Upper +2.51σ Band: `0.3687` | Lower -2.51σ Band: `0.3216`
  * Upper +2.01σ Band: `0.3640` | Lower -2.01σ Band: `0.3263`
  * Upper +2.00σ Band: `0.3639` | Lower -2.00σ Band: `0.3264`
  * Upper +1.28σ Band: `0.3572` | Lower -1.28σ Band: `0.3331`
  * Upper +1.00σ Band: `0.3546` | Lower -1.00σ Band: `0.3358`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`0.3327` | EMA-20=`0.3353` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`0.3387` (Slope: `+0.0000`) | EMA-100=`0.3378`
  * Institutional Anchors: EMA-144=`0.3365` | EMA-200=`0.3352` (Slope: `-0.1172`) | EMA-233=`0.3346`
- **Range Boundaries**: 24H High=`0.3632` | 24H Low=`0.3275` | Weekly High=`0.3632` | Weekly Low=`0.3266`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `0.3578` (Distance: `-6.36%`)
  * Point of Control (POC) = `0.3513` (Distance: `-4.65%`)
  * Value Area Low (VAL) = `0.3404` (Distance: `-1.60%`)
  * Auction Positioning: `BELOW_VALUE (Imbalance)` | Session Bias: **`BULLISH (Above Pivot)`** | Market Regime: `FAILED_AUCTION_REVERSAL`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`0.3312` | POC=`0.3307` | VAL=`0.3293`
  * Prior Day Extremes: PDH=`0.3335` | PDL=`0.3275` | PDC=`0.3275`
  * Monday Range Blueprint: High=`0.3310` | Mid=`0.3300` | Low=`0.3289`
  * Developing Weekly Value Area: Weekly VAH=`0.3465` | Weekly POC=`0.3306` | Weekly VAL=`0.3267`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`0.3632` | Low=`0.3335`
  * London Session (08:00-16:00 UTC): High=`0.3444` | Low=`0.3299`
  * New York Session (13:00-21:00 UTC): High=`0.3339` | Low=`0.3319`
  * Initial Balance (First Hour): IB High=`0.3444` | IB Low=`0.3379`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `0.3337` - `0.3364`
  * Optimal Trade Entry (OTE 0.705): `0.3357`
  * Structural Invalidation Anchor (0.786): `0.3377`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `0.3361` | `0.3364` | `0.3344` | `0.3344` | `2,073,971` | 695,683.29 USD | -102,327.09 USD | `-14.71%` | -2,713,698.64 USD | `-0.68` | **`BEARISH`** | `DELTA ALIGNED` |
| `5m` | `0.3344` | `0.3356` | `0.3343` | `0.3346` | `1,962,872` | 657,038.77 USD | -135,568.90 USD | `-20.63%` | -2,849,267.54 USD | `-0.86` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `5m` | `0.3347` | `0.3353` | `0.3341` | `0.3347` | `1,721,049` | 575,854.96 USD | 90,701.83 USD | `+15.75%` | -2,758,565.71 USD | `+0.54` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `0.3319` | `0.3367` | `0.3319` | `0.3361` | `11,450,681` | 3,824,910.39 USD | 144,614.51 USD | `+3.78%` | -2,606,683.41 USD | `+0.55` | **`BULLISH`** | `NEUTRAL CHOP` |
| `15m` | `0.3361` | `0.3364` | `0.3341` | `0.3346` | `5,867,877` | 1,965,380.04 USD | -165,908.48 USD | `-8.44%` | -2,772,591.89 USD | `+0.23` | **`BEARISH`** | `DELTA ALIGNED` |
| `15m` | `0.3346` | `0.3358` | `0.3335` | `0.3351` | `4,596,639` | 1,538,887.74 USD | 6,674.22 USD | `+0.43%` | -2,765,917.66 USD | `+0.34` | **`BULLISH`** | `NEUTRAL CHOP` |
| `1h` | `0.3371` | `0.3377` | `0.3307` | `0.3324` | `39,413,287` | 13,120,323.22 USD | 312,055.16 USD | `+2.38%` | -2,219,666.72 USD | `+0.21` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `1h` | `0.3324` | `0.3367` | `0.3318` | `0.3346` | `29,287,422` | 9,766,957.28 USD | -468,481.97 USD | `-4.80%` | -2,688,148.69 USD | `-0.16` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `1h` | `0.3346` | `0.3358` | `0.3335` | `0.3351` | `4,597,579` | 1,539,202.77 USD | 6,755.33 USD | `+0.44%` | -2,681,393.36 USD | `+0.08` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `0.3533` | `0.3608` | `0.3475` | `0.3495` | `257,452,106` | 91,407,782.04 USD | 2,108,185.60 USD | `+2.31%` | 4,840,432.56 USD | `+0.97` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `0.3495` | `0.3497` | `0.3310` | `0.3371` | `257,957,739` | 87,367,227.03 USD | -7,246,486.44 USD | `-8.29%` | -2,406,053.88 USD | `-1.94` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.3371` | `0.3377` | `0.3307` | `0.3347` | `68,583,482` | 22,848,053.49 USD | -136,834.83 USD | `-0.60%` | -2,542,888.71 USD | `+0.09` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `0.3314` | `0.3316` | `0.3310` | `0.3315` | `11,250,742` | 3,727,253.77 USD | 212,090.87 USD | `+5.69%` | 581,399.04 USD | `-1.00` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `0.3315` | `0.3653` | `0.3282` | `0.3533` | `793,774,795` | 276,969,161.06 USD | 2,150,847.92 USD | `+0.78%` | 2,732,246.96 USD | `+1.41` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `0.3533` | `0.3608` | `0.3475` | `0.3495` | `257,452,106` | 91,407,782.04 USD | 2,108,185.60 USD | `+2.31%` | 4,840,432.56 USD | `+0.97` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `0.3495` | `0.3497` | `0.3310` | `0.3371` | `257,957,739` | 87,367,227.03 USD | -7,246,486.44 USD | `-8.29%` | -2,406,053.88 USD | `-1.94` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.3371` | `0.3377` | `0.3307` | `0.3351` | `73,297,348` | 24,426,168.24 USD | -149,752.59 USD | `-0.61%` | -2,555,806.47 USD | `+0.09` | **`BEARISH`** | `NEUTRAL CHOP` |

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
| --- | **`0.3350`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `MID` | Regular L2 Book | - | - | - | Interbank L2 | 0.00% | Interbank |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 15:40:55 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `1097` | `0xecb6...2b00` | `LONG` | 1,968,774.97 USD | `5,863,463.00` | `0.3344` | `0.3358` | `0.000000` | 8,174.36 USD | `+0.42%` | `10X Cross` |
| `1579` | `0xeadc...9d55` | `LONG` | 1,343,680.00 USD | `4,000,000.00` | `0.3421` | `0.3358` | `0.000000` | -24,798.09 USD | `-1.85%` | `10X Cross` |
| `1580` | `0x8dd7...fa30` | `SHORT` | 1,343,080.00 USD | `4,000,000.00` | `0.3329` | `0.3358` | `0.3866` | -11,591.31 USD | `-0.86%` | `6X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `0.3316` | 7,871.14 USD | `-` | `NEWS_INTEL` | `-` | #TRX Whale BUY: 7.87K USD at 0.3316 USD [API] | `2026-10-29 10:14:22` |
| `ANNOUNCEMENT` | `INFO` | `0.3318` | 6,469.10 USD | `-` | `NEWS_INTEL` | `-` | #TRX Whale BUY: 6.47K USD at 0.3318 USD [API] | `2026-10-29 11:35:32` |
| `ANNOUNCEMENT` | `INFO` | `0.3318` | 9,999.82 USD | `-` | `NEWS_INTEL` | `-` | #TRX Whale BUY: 10.00K USD at 0.3318 USD [API] | `2026-10-29 11:35:32` |
| `ANNOUNCEMENT` | `INFO` | `0.3316` | 6,423.42 USD | `-` | `NEWS_INTEL` | `-` | #TRX Whale SELL: 6.42K USD at 0.3316 USD [API] | `2026-10-29 12:41:40` |
| `ANNOUNCEMENT` | `INFO` | `0.3318` | 6,464.73 USD | `-` | `NEWS_INTEL` | `-` | #TRX Whale SELL: 6.46K USD at 0.3318 USD [API] | `2026-10-29 13:28:43` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`0.3675` (Vol: 1,300,000.00 USD, Dist: `+9.50%`) | Long MP=`0.3298` (Vol: 509,400.00 USD, Dist: `--1.74%`)
  * 48H Horizon: Short MP=`0.3675` (Vol: 1,300,000.00 USD, Dist: `+9.50%`) | Long MP=`0.3249` (Vol: 724,200.00 USD, Dist: `--3.22%`)
  * 3D Horizon: Short MP=`0.3675` (Vol: 1,300,000.00 USD, Dist: `+9.50%`) | Long MP=`0.3252` (Vol: 817,700.00 USD, Dist: `--3.12%`)
  * 7D Horizon: Short MP=`0.3661` (Vol: 1,100,000.00 USD, Dist: `+9.09%`) | Long MP=`0.3248` (Vol: 1,000,000.00 USD, Dist: `--3.22%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long Liquidation` | `0.0735` | 3,000.00 USD | 1,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0755` | 6,660.00 USD | 1,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0865` | 858.60 USD | 1,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0875` | 181.91 USD | 1,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0985` | 964.61 USD | 1,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1065` | 152.08 USD | 1,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1145` | 2,290.00 USD | 1,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1155` | 265.88 USD | 1,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1165` | 123.26 USD | 1,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1285` | 9,870.00 USD | 1,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1585` | 388.01 USD | 1,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1625` | 6,680.00 USD | 1,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1675` | 57,490.00 USD | 1,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1685` | 23,990.00 USD | 1,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1715` | 648.96 USD | 1,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1725` | 48,180.00 USD | 1,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1735` | 339.71 USD | 1,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1745` | 5,170.00 USD | 1,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1755` | 255.53 USD | 1,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1765` | 278.69 USD | 1,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1775` | 1,400.00 USD | 1,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1815` | 263.54 USD | 1,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1875` | 36,310.00 USD | 1,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1975` | 632.00 USD | 1,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2165` | 1,520.00 USD | 1,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2185` | 1,000.00 USD | 1,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2205` | 230.42 USD | 1,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2225` | 201.14 USD | 1,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2245` | 4,570.00 USD | 1,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2295` | 2,070.00 USD | 1,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2305` | 410.06 USD | 1,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2325` | 2,420.00 USD | 1,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2335` | 413.53 USD | 1,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2345` | 5,700.00 USD | 1,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2355` | 3,130.00 USD | 1,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2365` | 686.56 USD | 1,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2375` | 568.81 USD | 1,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2395` | 151.36 USD | 1,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2435` | 3,790.00 USD | 1,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2445` | 1,910.00 USD | 1,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2455` | 384.94 USD | 1,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2485` | 11,890.00 USD | 1,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2505` | 262.02 USD | 993,640.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2555` | 1,220.00 USD | 993,380.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2585` | 302.96 USD | 992,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2595` | 749.18 USD | 991,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2615` | 107.74 USD | 991,100.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2625` | 11,370.00 USD | 990,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2645` | 2,650.00 USD | 979,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2655` | 193.02 USD | 976,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2675` | 321.54 USD | 976,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2685` | 3,390.00 USD | 976,450.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2735` | 220.99 USD | 973,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2745` | 84,470.00 USD | 972,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2785` | 13,170.00 USD | 888,370.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2795` | 6,260.00 USD | 875,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2805` | 13,300.00 USD | 868,940.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2815` | 3,690.00 USD | 855,640.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2825` | 838.74 USD | 851,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2845` | 1,090.00 USD | 851,110.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2855` | 5,880.00 USD | 850,020.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2865` | 4,150.00 USD | 844,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2885` | 4,940.00 USD | 840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2905` | 821.82 USD | 835,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2915` | 954.37 USD | 834,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2935` | 213.08 USD | 833,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2945` | 124.87 USD | 833,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.2953` | 20,530,000.00 USD | 20,530,000.00 USD | 82,110.00 USD | 0.00 USD | 10,820.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.2955` | 156.61 USD | 832,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.2959` | 20,440,000.00 USD | 20,440,000.00 USD | 109,100.00 USD | 22,740.00 USD | 9,700.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.2965` | 20,300,000.00 USD | 20,300,000.00 USD | 122,490.00 USD | 38,150.00 USD | 60,970.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.2965` | 1,010.00 USD | 832,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.2971` | 20,070,000.00 USD | 20,070,000.00 USD | 88,760.00 USD | 36,460.00 USD | 52,660.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.2974` | 14,300,000.00 USD | 14,300,000.00 USD | 167.00 USD | 0.00 USD | 2,060.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.2977` | 19,900,000.00 USD | 19,900,000.00 USD | 53,840.00 USD | 18,540.00 USD | 17,670.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.2978` | 14,300,000.00 USD | 14,300,000.00 USD | 17,600.00 USD | 3,340.00 USD | 4,250.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.2982` | 14,280,000.00 USD | 14,280,000.00 USD | 26,560.00 USD | 7,720.00 USD | 17,280.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.2983` | 19,810,000.00 USD | 19,810,000.00 USD | 170,390.00 USD | 15,470.00 USD | 39,660.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.2985` | 759.68 USD | 831,780.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.2986` | 14,220,000.00 USD | 14,220,000.00 USD | 102,450.00 USD | 9,300.00 USD | 7,900.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.2989` | 19,580,000.00 USD | 19,580,000.00 USD | 109,910.00 USD | 18,720.00 USD | 23,920.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.2990` | 14,110,000.00 USD | 14,110,000.00 USD | 50,390.00 USD | 0.00 USD | 8,790.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.2994` | 14,050,000.00 USD | 14,050,000.00 USD | 19,550.00 USD | 37,800.00 USD | 85,870.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.2995` | 19,430,000.00 USD | 19,430,000.00 USD | 6,450.00 USD | 62,740.00 USD | 80,320.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.2995` | 197.37 USD | 831,020.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.2998` | 13,900,000.00 USD | 13,900,000.00 USD | 9,360.00 USD | 24,820.00 USD | 17,040.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3001` | 19,280,000.00 USD | 19,280,000.00 USD | 2,360.00 USD | 15,390.00 USD | 62,490.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3002` | 13,850,000.00 USD | 13,850,000.00 USD | 15,600.00 USD | 20,670.00 USD | 24,520.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3005` | 10,620.00 USD | 830,820.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3006` | 13,790,000.00 USD | 13,790,000.00 USD | 848.70 USD | 1,800.00 USD | 24,520.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3007` | 19,200,000.00 USD | 19,200,000.00 USD | 13,780.00 USD | 2,960.00 USD | 22,100.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3010` | 13,760,000.00 USD | 13,760,000.00 USD | 34,290.00 USD | 8,400.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3013` | 19,160,000.00 USD | 19,160,000.00 USD | 4,100.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3014` | 13,720,000.00 USD | 13,720,000.00 USD | 17,320.00 USD | 5,010.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3015` | 102.81 USD | 820,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3018` | 13,700,000.00 USD | 13,700,000.00 USD | 1,630.00 USD | 6,650.00 USD | 16,590.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3019` | 19,160,000.00 USD | 19,160,000.00 USD | 0.00 USD | 8,660.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3022` | 13,670,000.00 USD | 13,670,000.00 USD | 14,930.00 USD | 6,590.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3025` | 19,150,000.00 USD | 19,150,000.00 USD | 0.00 USD | 9,860.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3025` | 2,510.00 USD | 820,100.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3026` | 13,650,000.00 USD | 13,650,000.00 USD | 2,180.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3030` | 13,650,000.00 USD | 13,650,000.00 USD | 24,620.00 USD | 8,320.00 USD | 6,190.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3031` | 19,140,000.00 USD | 19,140,000.00 USD | 50,940.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3034` | 13,610,000.00 USD | 13,610,000.00 USD | 742.30 USD | 0.00 USD | 12,600.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3035` | 4,040.00 USD | 817,590.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.3037` | 19,090,000.00 USD | 19,090,000.00 USD | 2,700.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3038` | 13,600,000.00 USD | 13,600,000.00 USD | 517.67 USD | 3,230.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3042` | 13,590,000.00 USD | 13,590,000.00 USD | 537.63 USD | 9,300.00 USD | 56,350.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3043` | 19,080,000.00 USD | 19,080,000.00 USD | 1,880.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3045` | 138.24 USD | 813,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3046` | 13,530,000.00 USD | 13,530,000.00 USD | 31,710.00 USD | 18,130.00 USD | 7,480.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3049` | 19,080,000.00 USD | 19,080,000.00 USD | 18,020.00 USD | 0.00 USD | 66,870.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3050` | 13,470,000.00 USD | 13,470,000.00 USD | 165.80 USD | 8,990.00 USD | 53,820.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3054` | 13,410,000.00 USD | 13,410,000.00 USD | 46,820.00 USD | 13,380.00 USD | 37,740.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3055` | 19,000,000.00 USD | 19,000,000.00 USD | 1,760.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3055` | 14,670.00 USD | 813,410.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.3061` | 19,000,000.00 USD | 19,000,000.00 USD | 32,680.00 USD | 7,690.00 USD | 37,210.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3062` | 13,310,000.00 USD | 13,310,000.00 USD | 885.25 USD | 2,350.00 USD | 56,460.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3065` | 5,900.00 USD | 798,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3066` | 13,250,000.00 USD | 13,250,000.00 USD | 31,110.00 USD | 29,620.00 USD | 35,690.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3067` | 18,920,000.00 USD | 18,920,000.00 USD | 6,500.00 USD | 8,110.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3070` | 13,150,000.00 USD | 13,150,000.00 USD | 67.24 USD | 0.00 USD | 12,760.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3073` | 18,900,000.00 USD | 18,900,000.00 USD | 7,350.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3074` | 13,140,000.00 USD | 13,140,000.00 USD | 23,570.00 USD | 1,940.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3075` | 722.62 USD | 792,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.3079` | 18,900,000.00 USD | 18,900,000.00 USD | 38,320.00 USD | 10,270.00 USD | 50,200.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3082` | 13,120,000.00 USD | 13,120,000.00 USD | 18,640.00 USD | 0.00 USD | 12,250.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3085` | 18,800,000.00 USD | 18,800,000.00 USD | 2,360.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3085` | 291.53 USD | 792,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3086` | 13,080,000.00 USD | 13,080,000.00 USD | 363.64 USD | 0.00 USD | 15,810.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3090` | 13,070,000.00 USD | 13,070,000.00 USD | 291.38 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3091` | 18,790,000.00 USD | 18,790,000.00 USD | 8,030.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3094` | 13,070,000.00 USD | 13,070,000.00 USD | 17,320.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3095` | 192.51 USD | 791,820.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.3097` | 18,790,000.00 USD | 18,790,000.00 USD | 75,040.00 USD | 3,620.00 USD | 54,360.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3098` | 13,050,000.00 USD | 13,050,000.00 USD | 7,060.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3102` | 13,040,000.00 USD | 13,040,000.00 USD | 57,870.00 USD | 15,820.00 USD | 46,470.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3103` | 18,650,000.00 USD | 18,650,000.00 USD | 67,180.00 USD | 0.00 USD | 63,310.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3105` | 820.96 USD | 791,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3106` | 12,920,000.00 USD | 12,920,000.00 USD | 2,640.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3109` | 18,520,000.00 USD | 18,520,000.00 USD | 6,400.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3114` | 12,920,000.00 USD | 12,920,000.00 USD | 977.81 USD | 9,110.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3115` | 18,520,000.00 USD | 18,520,000.00 USD | 10,340.00 USD | 0.00 USD | 37,490.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3115` | 13,600.00 USD | 790,810.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3118` | 12,910,000.00 USD | 12,910,000.00 USD | 14,500.00 USD | 8,100.00 USD | 17,620.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3121` | 18,470,000.00 USD | 18,470,000.00 USD | 162,580.00 USD | 19,620.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3122` | 12,870,000.00 USD | 12,870,000.00 USD | 13,610.00 USD | 2,560.00 USD | 33,830.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3125` | 17,810.00 USD | 777,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3126` | 12,820,000.00 USD | 12,820,000.00 USD | 12,430.00 USD | 13,530.00 USD | 7,580.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3127` | 18,290,000.00 USD | 18,290,000.00 USD | 21,180.00 USD | 54,460.00 USD | 57,690.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3130` | 12,790,000.00 USD | 12,790,000.00 USD | 2,430.00 USD | 28,470.00 USD | 21,520.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3133` | 18,150,000.00 USD | 18,150,000.00 USD | 5,070.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3134` | 12,730,000.00 USD | 12,730,000.00 USD | 5,000.00 USD | 23,940.00 USD | 9,590.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3135` | 446.11 USD | 759,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3138` | 12,700,000.00 USD | 12,700,000.00 USD | 5,650.00 USD | 10,610.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3139` | 18,150,000.00 USD | 18,150,000.00 USD | 2,240.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3142` | 12,680,000.00 USD | 12,680,000.00 USD | 4,220.00 USD | 3,580.00 USD | 9,540.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3145` | 18,150,000.00 USD | 18,150,000.00 USD | 247,810.00 USD | 51,270.00 USD | 17,870.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3145` | 577.11 USD | 758,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3146` | 12,660,000.00 USD | 12,660,000.00 USD | 1,850.00 USD | 2,330.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3150` | 12,660,000.00 USD | 12,660,000.00 USD | 4,810.00 USD | 23,750.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3151` | 17,830,000.00 USD | 17,830,000.00 USD | 196,920.00 USD | 23,130.00 USD | 49,320.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3154` | 12,630,000.00 USD | 12,630,000.00 USD | 27,150.00 USD | 1,850.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3155` | 2,960.00 USD | 758,380.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.3157` | 17,560,000.00 USD | 17,560,000.00 USD | 392,580.00 USD | 93,740.00 USD | 60,300.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3158` | 12,600,000.00 USD | 12,600,000.00 USD | 10,540.00 USD | 1,830.00 USD | 16,240.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3162` | 12,570,000.00 USD | 12,570,000.00 USD | 5,670.00 USD | 5,180.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3163` | 17,010,000.00 USD | 17,010,000.00 USD | 478,060.00 USD | 182,370.00 USD | 192,840.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3165` | 512.73 USD | 755,410.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3166` | 12,560,000.00 USD | 12,560,000.00 USD | 43,210.00 USD | 35,060.00 USD | 17,210.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3169` | 16,160,000.00 USD | 16,160,000.00 USD | 417,380.00 USD | 106,680.00 USD | 135,950.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3170` | 12,470,000.00 USD | 12,470,000.00 USD | 6,720.00 USD | 35,130.00 USD | 18,370.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3174` | 12,410,000.00 USD | 12,410,000.00 USD | 21,050.00 USD | 7,370.00 USD | 31,150.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3175` | 15,500,000.00 USD | 15,500,000.00 USD | 140,810.00 USD | 53,470.00 USD | 69,280.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3175` | 2,290.00 USD | 754,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3178` | 12,350,000.00 USD | 12,350,000.00 USD | 59,190.00 USD | 9,500.00 USD | 32,130.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3181` | 15,240,000.00 USD | 15,240,000.00 USD | 751,290.00 USD | 76,910.00 USD | 182,330.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3182` | 12,240,000.00 USD | 12,240,000.00 USD | 329,920.00 USD | 43,320.00 USD | 82,320.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3186` | 11,790,000.00 USD | 11,790,000.00 USD | 80,290.00 USD | 54,030.00 USD | 44,470.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3187` | 14,230,000.00 USD | 14,230,000.00 USD | 408,400.00 USD | 97,820.00 USD | 24,770.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3190` | 11,610,000.00 USD | 11,610,000.00 USD | 191,070.00 USD | 0.00 USD | 56,530.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3193` | 13,690,000.00 USD | 13,690,000.00 USD | 118,210.00 USD | 104,710.00 USD | 247,300.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3194` | 11,360,000.00 USD | 11,360,000.00 USD | 150,770.00 USD | 117,490.00 USD | 267,590.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3195` | 1,430.00 USD | 752,610.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3198` | 10,830,000.00 USD | 10,830,000.00 USD | 84,870.00 USD | 108,400.00 USD | 64,920.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3199` | 13,220,000.00 USD | 13,220,000.00 USD | 0.00 USD | 127,390.00 USD | 190,470.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3202` | 10,570,000.00 USD | 10,570,000.00 USD | 219,620.00 USD | 63,290.00 USD | 122,200.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3205` | 12,910,000.00 USD | 12,910,000.00 USD | 100,160.00 USD | 59,200.00 USD | 130,760.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3205` | 455.75 USD | 751,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3206` | 10,160,000.00 USD | 10,160,000.00 USD | 127,850.00 USD | 16,080.00 USD | 119,210.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3210` | 9,900,000.00 USD | 9,900,000.00 USD | 88,620.00 USD | 31,880.00 USD | 38,170.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3211` | 12,620,000.00 USD | 12,620,000.00 USD | 569,720.00 USD | 117,230.00 USD | 244,340.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3214` | 9,740,000.00 USD | 9,740,000.00 USD | 53,360.00 USD | 45,170.00 USD | 83,510.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3215` | 756.17 USD | 750,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.3217` | 11,690,000.00 USD | 11,690,000.00 USD | 286,830.00 USD | 58,690.00 USD | 107,900.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3218` | 9,560,000.00 USD | 9,560,000.00 USD | 5,550.00 USD | 28,050.00 USD | 87,330.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3222` | 9,440,000.00 USD | 9,440,000.00 USD | 154,560.00 USD | 24,690.00 USD | 69,480.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3223` | 11,230,000.00 USD | 11,230,000.00 USD | 643,460.00 USD | 196,690.00 USD | 103,370.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3226` | 9,190,000.00 USD | 9,190,000.00 USD | 13,670.00 USD | 24,400.00 USD | 188,740.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3229` | 10,290,000.00 USD | 10,290,000.00 USD | 858,070.00 USD | 299,190.00 USD | 385,680.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3230` | 8,960,000.00 USD | 8,960,000.00 USD | 92,790.00 USD | 46,020.00 USD | 86,810.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3234` | 8,740,000.00 USD | 8,740,000.00 USD | 61,120.00 USD | 72,090.00 USD | 93,070.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3235` | 8,750,000.00 USD | 8,750,000.00 USD | 709,160.00 USD | 213,370.00 USD | 359,100.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3235` | 128.43 USD | 749,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3238` | 8,510,000.00 USD | 8,510,000.00 USD | 0.00 USD | 53,490.00 USD | 138,410.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3241` | 7,460,000.00 USD | 7,460,000.00 USD | 433,820.00 USD | 149,860.00 USD | 138,560.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3242` | 8,320,000.00 USD | 8,320,000.00 USD | 97,850.00 USD | 17,220.00 USD | 231,720.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3246` | 7,970,000.00 USD | 7,970,000.00 USD | 256,230.00 USD | 90,310.00 USD | 171,640.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3247` | 6,740,000.00 USD | 6,740,000.00 USD | 846,180.00 USD | 127,310.00 USD | 353,590.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3250` | 7,450,000.00 USD | 7,450,000.00 USD | 758,560.00 USD | 89,640.00 USD | 318,030.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3253` | 5,410,000.00 USD | 5,410,000.00 USD | 1,220,000.00 USD | 137,440.00 USD | 241,690.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3254` | 6,290,000.00 USD | 6,290,000.00 USD | 340,830.00 USD | 61,360.00 USD | 299,050.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3255` | 3,580.00 USD | 749,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3258` | 5,590,000.00 USD | 5,590,000.00 USD | 373,570.00 USD | 71,210.00 USD | 143,750.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3259` | 3,810,000.00 USD | 3,810,000.00 USD | 182,240.00 USD | 250,110.00 USD | 503,650.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3262` | 5,000,000.00 USD | 5,000,000.00 USD | 115,280.00 USD | 378,600.00 USD | 505,960.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3265` | 2,880,000.00 USD | 2,880,000.00 USD | 80,160.00 USD | 197,270.00 USD | 347,150.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3266` | 4,000,000.00 USD | 4,000,000.00 USD | 44,720.00 USD | 157,840.00 USD | 354,040.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3270` | 3,440,000.00 USD | 3,440,000.00 USD | 237,730.00 USD | 115,770.00 USD | 350,550.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3271` | 2,250,000.00 USD | 2,250,000.00 USD | 192,500.00 USD | 138,680.00 USD | 261,530.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3274` | 2,740,000.00 USD | 2,740,000.00 USD | 155,490.00 USD | 61,310.00 USD | 202,370.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3275` | 163.42 USD | 746,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.3277` | 1,660,000.00 USD | 1,660,000.00 USD | 0.00 USD | 29,390.00 USD | 85,620.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3278` | 2,320,000.00 USD | 2,320,000.00 USD | 268,410.00 USD | 32,310.00 USD | 133,800.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3282` | 1,880,000.00 USD | 1,880,000.00 USD | 0.00 USD | 61,320.00 USD | 16,760.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3283` | 1,550,000.00 USD | 1,550,000.00 USD | 89,030.00 USD | 25,670.00 USD | 275,050.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3285` | 745,260.00 USD | 746,100.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3286` | 1,810,000.00 USD | 1,810,000.00 USD | 45,960.00 USD | 39,260.00 USD | 113,560.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3289` | 1,160,000.00 USD | 1,160,000.00 USD | 0.00 USD | 43,290.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3290` | 1,610,000.00 USD | 1,610,000.00 USD | 109,890.00 USD | 44,530.00 USD | 72,140.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3294` | 1,380,000.00 USD | 1,380,000.00 USD | 61,960.00 USD | 26,090.00 USD | 80,060.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3295` | 1,110,000.00 USD | 1,110,000.00 USD | 255,850.00 USD | 83,080.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3295` | 839.90 USD | 839.90 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3298` | 1,210,000.00 USD | 1,210,000.00 USD | 105,330.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3301` | 774,520.00 USD | 774,520.00 USD | 184,120.00 USD | 9,050.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3302` | 1,110,000.00 USD | 1,110,000.00 USD | 37,670.00 USD | 58,700.00 USD | 93,930.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3305` | 7,080.00 USD | 7,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3306` | 917,340.00 USD | 917,340.00 USD | 110,810.00 USD | 16,160.00 USD | 11,710.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3307` | 581,350.00 USD | 581,350.00 USD | 167,950.00 USD | 10,690.00 USD | 294,170.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3310` | 778,660.00 USD | 778,660.00 USD | 11,600.00 USD | 122,460.00 USD | 444,920.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3313` | 108,550.00 USD | 108,550.00 USD | 0.00 USD | 50,650.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3314` | 199,680.00 USD | 199,680.00 USD | 0.00 USD | 54,160.00 USD | 86,570.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3318` | 58,950.00 USD | 58,950.00 USD | 0.00 USD | 58,950.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3319` | 57,890.00 USD | 57,890.00 USD | 0.00 USD | 57,890.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3358` | 144,280.00 USD | 144,280.00 USD | 0.00 USD | 0.00 USD | 144,280.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3370` | 217,200.00 USD | 217,200.00 USD | 72,920.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3374` | 546,840.00 USD | 546,840.00 USD | 329,640.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3379` | 21,390.00 USD | 21,390.00 USD | 0.00 USD | 21,390.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3382` | 618,740.00 USD | 618,740.00 USD | 71,900.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3385` | 147,040.00 USD | 147,040.00 USD | 125,650.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3386` | 778,070.00 USD | 778,070.00 USD | 92,750.00 USD | 11,160.00 USD | 55,410.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3390` | 1,160,000.00 USD | 1,160,000.00 USD | 302,930.00 USD | 27,820.00 USD | 49,390.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3391` | 381,700.00 USD | 381,700.00 USD | 0.00 USD | 0.00 USD | 234,660.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3394` | 1,960,000.00 USD | 1,960,000.00 USD | 115,280.00 USD | 200,920.00 USD | 485,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3397` | 1,640,000.00 USD | 1,640,000.00 USD | 262,880.00 USD | 586,760.00 USD | 410,790.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3398` | 2,350,000.00 USD | 2,350,000.00 USD | 43,780.00 USD | 216,810.00 USD | 129,840.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3402` | 2,840,000.00 USD | 2,840,000.00 USD | 20,340.00 USD | 97,740.00 USD | 374,530.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3403` | 3,040,000.00 USD | 3,040,000.00 USD | 1,070,000.00 USD | 103,630.00 USD | 223,390.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3406` | 3,250,000.00 USD | 3,250,000.00 USD | 260,970.00 USD | 0.00 USD | 150,300.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3409` | 3,510,000.00 USD | 3,510,000.00 USD | 0.00 USD | 29,390.00 USD | 446,990.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3410` | 3,570,000.00 USD | 3,570,000.00 USD | 257,330.00 USD | 34,110.00 USD | 27,700.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3414` | 4,070,000.00 USD | 4,070,000.00 USD | 376,520.00 USD | 27,220.00 USD | 97,590.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3415` | 3,600,000.00 USD | 3,600,000.00 USD | 0.00 USD | 0.00 USD | 85,620.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3418` | 4,480,000.00 USD | 4,480,000.00 USD | 343,500.00 USD | 32,360.00 USD | 27,870.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3421` | 3,640,000.00 USD | 3,640,000.00 USD | 0.00 USD | 43,290.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3422` | 4,580,000.00 USD | 4,580,000.00 USD | 71,180.00 USD | 31,660.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3426` | 4,740,000.00 USD | 4,740,000.00 USD | 0.00 USD | 156,700.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3427` | 3,730,000.00 USD | 3,730,000.00 USD | 0.00 USD | 92,380.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3430` | 5,130,000.00 USD | 5,130,000.00 USD | 166,310.00 USD | 220,760.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3433` | 3,990,000.00 USD | 3,990,000.00 USD | 254,700.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3434` | 5,240,000.00 USD | 5,240,000.00 USD | 0.00 USD | 83,080.00 USD | 30,950.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3438` | 5,350,000.00 USD | 5,350,000.00 USD | 0.00 USD | 49,600.00 USD | 62,980.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3442` | 5,400,000.00 USD | 5,400,000.00 USD | 0.00 USD | 51,170.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3445` | 4,090,000.00 USD | 4,090,000.00 USD | 103,130.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3446` | 5,570,000.00 USD | 5,570,000.00 USD | 0.00 USD | 60,100.00 USD | 106,240.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3450` | 5,770,000.00 USD | 5,770,000.00 USD | 35,950.00 USD | 45,930.00 USD | 119,850.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3451` | 4,180,000.00 USD | 4,180,000.00 USD | 62,830.00 USD | 28,550.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3454` | 6,060,000.00 USD | 6,060,000.00 USD | 126,310.00 USD | 54,930.00 USD | 106,680.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3457` | 4,540,000.00 USD | 4,540,000.00 USD | 0.00 USD | 29,340.00 USD | 332,190.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3458` | 6,830,000.00 USD | 6,830,000.00 USD | 159,870.00 USD | 100,770.00 USD | 507,890.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3462` | 7,260,000.00 USD | 7,260,000.00 USD | 168,310.00 USD | 124,400.00 USD | 142,100.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3463` | 4,920,000.00 USD | 4,920,000.00 USD | 0.00 USD | 167,950.00 USD | 205,390.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3466` | 7,460,000.00 USD | 7,460,000.00 USD | 21,890.00 USD | 65,550.00 USD | 106,440.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3469` | 5,110,000.00 USD | 5,110,000.00 USD | 60,310.00 USD | 51,820.00 USD | 75,520.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3470` | 7,590,000.00 USD | 7,590,000.00 USD | 37,620.00 USD | 36,280.00 USD | 61,300.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3474` | 7,670,000.00 USD | 7,670,000.00 USD | 0.00 USD | 42,560.00 USD | 31,160.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3475` | 5,150,000.00 USD | 5,150,000.00 USD | 0.00 USD | 40,540.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3478` | 7,890,000.00 USD | 7,890,000.00 USD | 51,860.00 USD | 40,550.00 USD | 134,270.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3481` | 5,210,000.00 USD | 5,210,000.00 USD | 6,440.00 USD | 14,700.00 USD | 42,810.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3482` | 7,980,000.00 USD | 7,980,000.00 USD | 56,790.00 USD | 20,460.00 USD | 8,380.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3486` | 8,020,000.00 USD | 8,020,000.00 USD | 7,190.00 USD | 32,250.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3487` | 5,230,000.00 USD | 5,230,000.00 USD | 0.00 USD | 21,650.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3490` | 8,130,000.00 USD | 8,130,000.00 USD | 40,230.00 USD | 10,900.00 USD | 61,240.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3493` | 5,260,000.00 USD | 5,260,000.00 USD | 0.00 USD | 24,660.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3494` | 8,240,000.00 USD | 8,240,000.00 USD | 5,420.00 USD | 24,400.00 USD | 79,030.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3498` | 8,700,000.00 USD | 8,700,000.00 USD | 83,150.00 USD | 0.00 USD | 375,650.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3499` | 5,390,000.00 USD | 5,390,000.00 USD | 133,490.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3502` | 8,780,000.00 USD | 8,780,000.00 USD | 0.00 USD | 29,350.00 USD | 50,760.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3505` | 5,400,000.00 USD | 5,400,000.00 USD | 12,030.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3505` | 9,630.00 USD | 16,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.3506` | 8,880,000.00 USD | 8,880,000.00 USD | 74,220.00 USD | 0.00 USD | 31,490.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3510` | 8,930,000.00 USD | 8,930,000.00 USD | 2,790.00 USD | 12,400.00 USD | 32,490.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3511` | 6,360,000.00 USD | 6,360,000.00 USD | 690,500.00 USD | 0.00 USD | 271,800.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3514` | 9,030,000.00 USD | 9,030,000.00 USD | 21,910.00 USD | 0.00 USD | 73,170.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3515` | 175.05 USD | 16,880.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.3517` | 6,380,000.00 USD | 6,380,000.00 USD | 12,290.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3518` | 9,110,000.00 USD | 9,110,000.00 USD | 30,510.00 USD | 11,560.00 USD | 42,500.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3522` | 9,130,000.00 USD | 9,130,000.00 USD | 2,260.00 USD | 16,140.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3523` | 6,790,000.00 USD | 6,790,000.00 USD | 277,410.00 USD | 28,950.00 USD | 107,430.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3526` | 9,170,000.00 USD | 9,170,000.00 USD | 5,360.00 USD | 6,280.00 USD | 28,910.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3530` | 9,410,000.00 USD | 9,410,000.00 USD | 101,220.00 USD | 52,710.00 USD | 88,110.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3534` | 9,680,000.00 USD | 9,680,000.00 USD | 127,850.00 USD | 56,820.00 USD | 87,200.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3535` | 7,060,000.00 USD | 7,060,000.00 USD | 4,830.00 USD | 77,960.00 USD | 187,450.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3538` | 9,820,000.00 USD | 9,820,000.00 USD | 3,230.00 USD | 21,150.00 USD | 108,070.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3541` | 7,980,000.00 USD | 7,980,000.00 USD | 799,020.00 USD | 118,370.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3542` | 10,020,000.00 USD | 10,020,000.00 USD | 83,710.00 USD | 84,150.00 USD | 37,920.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3546` | 10,110,000.00 USD | 10,110,000.00 USD | 5,090.00 USD | 51,930.00 USD | 31,910.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3547` | 8,280,000.00 USD | 8,280,000.00 USD | 11,040.00 USD | 0.00 USD | 288,450.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3550` | 10,160,000.00 USD | 10,160,000.00 USD | 2,710.00 USD | 42,500.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3553` | 8,390,000.00 USD | 8,390,000.00 USD | 0.00 USD | 117,050.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3554` | 10,260,000.00 USD | 10,260,000.00 USD | 21,530.00 USD | 40,120.00 USD | 47,950.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3558` | 10,320,000.00 USD | 10,320,000.00 USD | 331.60 USD | 25,350.00 USD | 30,620.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3559` | 8,410,000.00 USD | 8,410,000.00 USD | 13,630.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3562` | 10,460,000.00 USD | 10,460,000.00 USD | 977.81 USD | 17,880.00 USD | 115,040.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3565` | 8,450,000.00 USD | 8,450,000.00 USD | 0.00 USD | 43,060.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3566` | 10,470,000.00 USD | 10,470,000.00 USD | 2,090.00 USD | 11,630.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3570` | 10,480,000.00 USD | 10,480,000.00 USD | 3,220.00 USD | 6,920.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3571` | 8,460,000.00 USD | 8,460,000.00 USD | 9,210.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3574` | 10,620,000.00 USD | 10,620,000.00 USD | 131,860.00 USD | 9,250.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3577` | 8,590,000.00 USD | 8,590,000.00 USD | 124,630.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3578` | 10,690,000.00 USD | 10,690,000.00 USD | 31,190.00 USD | 9,130.00 USD | 27,240.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3582` | 10,720,000.00 USD | 10,720,000.00 USD | 2,980.00 USD | 14,930.00 USD | 11,710.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3583` | 8,720,000.00 USD | 8,720,000.00 USD | 0.00 USD | 0.00 USD | 135,900.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3586` | 10,740,000.00 USD | 10,740,000.00 USD | 17,760.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3589` | 9,090,000.00 USD | 9,090,000.00 USD | 0.00 USD | 50,650.00 USD | 320,430.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3590` | 10,790,000.00 USD | 10,790,000.00 USD | 3,780.00 USD | 15,750.00 USD | 33,590.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3594` | 11,000,000.00 USD | 11,000,000.00 USD | 111,740.00 USD | 0.00 USD | 99,590.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3595` | 9,240,000.00 USD | 9,240,000.00 USD | 0.00 USD | 0.00 USD | 146,290.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3598` | 11,130,000.00 USD | 11,130,000.00 USD | 46,200.00 USD | 22,780.00 USD | 64,450.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3601` | 9,740,000.00 USD | 9,740,000.00 USD | 4,040.00 USD | 161,200.00 USD | 338,540.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3602` | 11,330,000.00 USD | 11,330,000.00 USD | 32,190.00 USD | 32,480.00 USD | 136,650.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3606` | 11,550,000.00 USD | 11,550,000.00 USD | 30,100.00 USD | 26,580.00 USD | 157,390.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3607` | 10,140,000.00 USD | 10,140,000.00 USD | 330,200.00 USD | 68,030.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3610` | 11,770,000.00 USD | 11,770,000.00 USD | 75,090.00 USD | 45,020.00 USD | 100,930.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3613` | 10,840,000.00 USD | 10,840,000.00 USD | 77,710.00 USD | 330,040.00 USD | 288,930.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3614` | 11,960,000.00 USD | 11,960,000.00 USD | 10,940.00 USD | 40,360.00 USD | 135,700.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3618` | 12,340,000.00 USD | 12,340,000.00 USD | 225,600.00 USD | 56,810.00 USD | 104,310.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3619` | 11,050,000.00 USD | 11,050,000.00 USD | 3,500.00 USD | 209,940.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3622` | 12,650,000.00 USD | 12,650,000.00 USD | 169,910.00 USD | 69,640.00 USD | 71,510.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3625` | 11,240,000.00 USD | 11,240,000.00 USD | 2,410.00 USD | 191,880.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3626` | 12,780,000.00 USD | 12,780,000.00 USD | 73,050.00 USD | 49,330.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3630` | 14,070,000.00 USD | 14,070,000.00 USD | 1,120,000.00 USD | 93,320.00 USD | 79,610.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3631` | 11,360,000.00 USD | 11,360,000.00 USD | 678.26 USD | 114,740.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3634` | 14,430,000.00 USD | 14,430,000.00 USD | 144,090.00 USD | 14,760.00 USD | 199,780.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3635` | 31,260.00 USD | 48,140.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.3637` | 11,380,000.00 USD | 11,380,000.00 USD | 937.01 USD | 21,530.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3638` | 14,750,000.00 USD | 14,750,000.00 USD | 183,690.00 USD | 65,110.00 USD | 76,240.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3642` | 15,100,000.00 USD | 15,100,000.00 USD | 103,140.00 USD | 206,820.00 USD | 35,280.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3643` | 12,180,000.00 USD | 12,180,000.00 USD | 4,830.00 USD | 0.00 USD | 789,140.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3645` | 12,390.00 USD | 60,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.3646` | 15,480,000.00 USD | 15,480,000.00 USD | 333,280.00 USD | 21,220.00 USD | 26,970.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3649` | 12,350,000.00 USD | 12,350,000.00 USD | 177,470.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3650` | 15,700,000.00 USD | 15,700,000.00 USD | 2,410.00 USD | 55,120.00 USD | 168,850.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3654` | 16,320,000.00 USD | 16,320,000.00 USD | 405,500.00 USD | 47,350.00 USD | 165,330.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3655` | 13,140,000.00 USD | 13,140,000.00 USD | 677,860.00 USD | 112,770.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3658` | 16,920,000.00 USD | 16,920,000.00 USD | 240,260.00 USD | 152,790.00 USD | 203,990.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3661` | 14,130,000.00 USD | 14,130,000.00 USD | 685,520.00 USD | 60,550.00 USD | 238,480.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3662` | 17,200,000.00 USD | 17,200,000.00 USD | 161,450.00 USD | 61,740.00 USD | 55,630.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3665` | 3,110.00 USD | 63,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.3666` | 17,860,000.00 USD | 17,860,000.00 USD | 475,420.00 USD | 119,560.00 USD | 66,840.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3667` | 14,700,000.00 USD | 14,700,000.00 USD | 422,610.00 USD | 15,390.00 USD | 135,630.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3670` | 18,340,000.00 USD | 18,340,000.00 USD | 94,630.00 USD | 66,280.00 USD | 318,570.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3673` | 15,390,000.00 USD | 15,390,000.00 USD | 512,420.00 USD | 53,040.00 USD | 122,410.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3674` | 18,600,000.00 USD | 18,600,000.00 USD | 41,190.00 USD | 72,620.00 USD | 148,060.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3678` | 19,320,000.00 USD | 19,320,000.00 USD | 517,910.00 USD | 34,010.00 USD | 164,260.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3679` | 15,650,000.00 USD | 15,650,000.00 USD | 259,160.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3682` | 19,840,000.00 USD | 19,840,000.00 USD | 286,630.00 USD | 82,130.00 USD | 148,400.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3685` | 15,830,000.00 USD | 15,830,000.00 USD | 4,100.00 USD | 102,650.00 USD | 72,350.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3686` | 20,400,000.00 USD | 20,400,000.00 USD | 327,450.00 USD | 153,840.00 USD | 81,460.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3690` | 20,930,000.00 USD | 20,930,000.00 USD | 475,810.00 USD | 51,700.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3691` | 16,240,000.00 USD | 16,240,000.00 USD | 147,650.00 USD | 261,530.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3694` | 21,180,000.00 USD | 21,180,000.00 USD | 154,310.00 USD | 72,220.00 USD | 23,760.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3697` | 16,400,000.00 USD | 16,400,000.00 USD | 0.00 USD | 163,180.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3698` | 21,360,000.00 USD | 21,360,000.00 USD | 170,350.00 USD | 15,980.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3702` | 22,020,000.00 USD | 22,020,000.00 USD | 438,600.00 USD | 196,170.00 USD | 27,870.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3703` | 16,450,000.00 USD | 16,450,000.00 USD | 50,940.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3705` | 278.99 USD | 63,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.3706` | 22,780,000.00 USD | 22,780,000.00 USD | 177,000.00 USD | 8,320.00 USD | 573,510.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3709` | 16,450,000.00 USD | 16,450,000.00 USD | 1,540.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3710` | 22,970,000.00 USD | 22,970,000.00 USD | 110,310.00 USD | 42,590.00 USD | 38,120.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3714` | 24,360,000.00 USD | 24,360,000.00 USD | 489,730.00 USD | 116,180.00 USD | 783,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3715` | 16,850,000.00 USD | 16,850,000.00 USD | 4,580.00 USD | 0.00 USD | 394,570.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3718` | 24,860,000.00 USD | 24,860,000.00 USD | 36,200.00 USD | 182,160.00 USD | 274,660.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3721` | 17,600,000.00 USD | 17,600,000.00 USD | 0.00 USD | 0.00 USD | 747,740.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3722` | 25,170,000.00 USD | 25,170,000.00 USD | 185,610.00 USD | 68,140.00 USD | 62,210.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3725` | 186.25 USD | 64,110.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.3727` | 17,880,000.00 USD | 17,880,000.00 USD | 212,850.00 USD | 0.00 USD | 66,870.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3733` | 18,070,000.00 USD | 18,070,000.00 USD | 188,670.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3735` | 7,210.00 USD | 71,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.3739` | 18,540,000.00 USD | 18,540,000.00 USD | 242,460.00 USD | 7,690.00 USD | 218,010.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3745` | 18,940,000.00 USD | 18,940,000.00 USD | 248,660.00 USD | 115,430.00 USD | 37,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3751` | 18,940,000.00 USD | 18,940,000.00 USD | 5,330.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3755` | 4,030.00 USD | 75,350.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.3757` | 19,250,000.00 USD | 19,250,000.00 USD | 0.00 USD | 0.00 USD | 302,240.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3763` | 19,420,000.00 USD | 19,420,000.00 USD | 35,610.00 USD | 92,380.00 USD | 50,200.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3769` | 19,430,000.00 USD | 19,430,000.00 USD | 1,150.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3775` | 104.19 USD | 75,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.3781` | 19,450,000.00 USD | 19,450,000.00 USD | 23,800.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3785` | 556,430.00 USD | 631,880.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.3787` | 19,600,000.00 USD | 19,600,000.00 USD | 90,150.00 USD | 3,620.00 USD | 54,360.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3793` | 20,060,000.00 USD | 20,060,000.00 USD | 27,760.00 USD | 0.00 USD | 437,170.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3811` | 20,100,000.00 USD | 20,100,000.00 USD | 4,000.00 USD | 0.00 USD | 37,490.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3817` | 20,280,000.00 USD | 20,280,000.00 USD | 156,690.00 USD | 19,620.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3823` | 20,390,000.00 USD | 20,390,000.00 USD | 0.00 USD | 54,460.00 USD | 57,690.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3835` | 115.05 USD | 632,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.3853` | 20,390,000.00 USD | 20,390,000.00 USD | 535.97 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3855` | 264.84 USD | 632,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.3859` | 20,460,000.00 USD | 20,460,000.00 USD | 70,850.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3865` | 20,620,000.00 USD | 20,620,000.00 USD | 112,700.00 USD | 45,110.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3877` | 20,750,000.00 USD | 20,750,000.00 USD | 123,270.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3883` | 20,790,000.00 USD | 20,790,000.00 USD | 0.00 USD | 0.00 USD | 48,960.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3889` | 20,900,000.00 USD | 20,900,000.00 USD | 103,790.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3895` | 20,940,000.00 USD | 20,940,000.00 USD | 0.00 USD | 41,060.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3895` | 4,760.00 USD | 637,020.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.3901` | 21,000,000.00 USD | 21,000,000.00 USD | 59,060.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3905` | 6,000.00 USD | 643,020.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.3907` | 21,110,000.00 USD | 21,110,000.00 USD | 0.00 USD | 50,210.00 USD | 63,420.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3925` | 21,270,000.00 USD | 21,270,000.00 USD | 342.70 USD | 1,190.00 USD | 157,830.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3931` | 21,300,000.00 USD | 21,300,000.00 USD | 27,520.00 USD | 2,840.00 USD | 2,800.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3935` | 1,480.00 USD | 644,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.3937` | 21,330,000.00 USD | 21,330,000.00 USD | 21,970.00 USD | 1,070.00 USD | 5,410.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3943` | 21,360,000.00 USD | 21,360,000.00 USD | 24,790.00 USD | 3,090.00 USD | 784.19 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3945` | 118,130.00 USD | 762,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.3949` | 21,500,000.00 USD | 21,500,000.00 USD | 109,810.00 USD | 8,290.00 USD | 18,490.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3955` | 21,730,000.00 USD | 21,730,000.00 USD | 107,070.00 USD | 10,160.00 USD | 110,780.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3955` | 1,390,000.00 USD | 2,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.3961` | 21,910,000.00 USD | 21,910,000.00 USD | 122,550.00 USD | 54,030.00 USD | 7,040.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3967` | 21,930,000.00 USD | 21,930,000.00 USD | 12,300.00 USD | 6,010.00 USD | 4,840.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3973` | 22,070,000.00 USD | 22,070,000.00 USD | 16,660.00 USD | 1,440.00 USD | 123,860.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3979` | 22,180,000.00 USD | 22,180,000.00 USD | 57,690.00 USD | 38,460.00 USD | 11,500.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3985` | 22,220,000.00 USD | 22,220,000.00 USD | 23,360.00 USD | 3,160.00 USD | 10,200.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3991` | 22,260,000.00 USD | 22,260,000.00 USD | 0.00 USD | 16,880.00 USD | 24,490.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3997` | 22,270,000.00 USD | 22,270,000.00 USD | 0.00 USD | 8,610.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.4001` | 22,280,000.00 USD | 22,280,000.00 USD | 0.00 USD | 7,690.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.4025` | 328.44 USD | 2,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4085` | 170.75 USD | 2,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4095` | 239.56 USD | 2,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4185` | 998.96 USD | 2,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4245` | 134.57 USD | 2,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4255` | 3,940.00 USD | 2,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4295` | 10,210.00 USD | 2,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4325` | 1,500.00 USD | 2,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4355` | 70,890.00 USD | 2,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4365` | 1,490.00 USD | 2,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4415` | 377.48 USD | 2,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4445` | 22,230.00 USD | 2,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4455` | 1,020.00 USD | 2,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4465` | 5,520.00 USD | 2,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4475` | 65,610.00 USD | 2,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4515` | 318.76 USD | 2,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4715` | 272.53 USD | 2,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4805` | 2,880.00 USD | 2,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4895` | 839.49 USD | 2,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4905` | 5,120.00 USD | 2,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4995` | 2,730.00 USD | 2,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.5005` | 23,320.00 USD | 2,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.5325` | 667.22 USD | 2,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.5465` | 40,440.00 USD | 2,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.5575` | 3,060.00 USD | 2,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.5605` | 140.12 USD | 2,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.5725` | 742,670.00 USD | 3,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.6155` | 24,620.00 USD | 3,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.6205` | 375.40 USD | 3,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.6275` | 1,130.00 USD | 3,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.6335` | 6,810.00 USD | 3,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.6505` | 102,000.00 USD | 3,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.6515` | 951.19 USD | 3,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.6535` | 705.13 USD | 3,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.6615` | 2,060.00 USD | 3,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.6635` | 3,740.00 USD | 3,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

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
| `7D` | `0.2953` | 20,530,000.00 USD | 0.00 USD | 20,530,000.00 USD | 82,110.00 USD | 0.00 USD | 10,820.00 USD |
| `7D` | `0.2959` | 20,440,000.00 USD | 0.00 USD | 20,440,000.00 USD | 109,100.00 USD | 22,740.00 USD | 9,700.00 USD |
| `7D` | `0.2965` | 20,300,000.00 USD | 0.00 USD | 20,300,000.00 USD | 122,490.00 USD | 38,150.00 USD | 60,970.00 USD |
| `7D` | `0.2971` | 20,070,000.00 USD | 0.00 USD | 20,070,000.00 USD | 88,760.00 USD | 36,460.00 USD | 52,660.00 USD |
| `1D` | `0.2975` | 14,340,000.00 USD | 0.00 USD | 14,340,000.00 USD | 197.77 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.2977` | 19,900,000.00 USD | 0.00 USD | 19,900,000.00 USD | 53,840.00 USD | 18,540.00 USD | 17,670.00 USD |
| `1D` | `0.2979` | 14,340,000.00 USD | 0.00 USD | 14,340,000.00 USD | 17,590.00 USD | 3,370.00 USD | 4,770.00 USD |
| `1D` | `0.2983` | 14,320,000.00 USD | 0.00 USD | 14,320,000.00 USD | 86,380.00 USD | 8,000.00 USD | 21,640.00 USD |
| `7D` | `0.2983` | 19,810,000.00 USD | 0.00 USD | 19,810,000.00 USD | 170,390.00 USD | 15,470.00 USD | 39,660.00 USD |
| `1D` | `0.2987` | 14,200,000.00 USD | 0.00 USD | 14,200,000.00 USD | 43,060.00 USD | 7,050.00 USD | 3,020.00 USD |
| `7D` | `0.2989` | 19,580,000.00 USD | 0.00 USD | 19,580,000.00 USD | 109,910.00 USD | 18,720.00 USD | 23,920.00 USD |
| `1D` | `0.2991` | 14,150,000.00 USD | 0.00 USD | 14,150,000.00 USD | 56,620.00 USD | 0.00 USD | 8,790.00 USD |
| `1D` | `0.2995` | 14,080,000.00 USD | 0.00 USD | 14,080,000.00 USD | 13,470.00 USD | 57,880.00 USD | 85,870.00 USD |
| `7D` | `0.2995` | 19,430,000.00 USD | 0.00 USD | 19,430,000.00 USD | 6,450.00 USD | 62,740.00 USD | 80,320.00 USD |
| `1D` | `0.2999` | 13,920,000.00 USD | 0.00 USD | 13,920,000.00 USD | 8,760.00 USD | 9,870.00 USD | 17,040.00 USD |
| `7D` | `0.3001` | 19,280,000.00 USD | 0.00 USD | 19,280,000.00 USD | 2,360.00 USD | 15,390.00 USD | 62,490.00 USD |
| `1D` | `0.3003` | 13,890,000.00 USD | 0.00 USD | 13,890,000.00 USD | 15,600.00 USD | 15,540.00 USD | 24,520.00 USD |
| `1D` | `0.3007` | 13,830,000.00 USD | 0.00 USD | 13,830,000.00 USD | 14,390.00 USD | 10,200.00 USD | 24,520.00 USD |
| `7D` | `0.3007` | 19,200,000.00 USD | 0.00 USD | 19,200,000.00 USD | 13,780.00 USD | 2,960.00 USD | 22,100.00 USD |
| `1D` | `0.3011` | 13,780,000.00 USD | 0.00 USD | 13,780,000.00 USD | 38,060.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3013` | 19,160,000.00 USD | 0.00 USD | 19,160,000.00 USD | 4,100.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3015` | 13,750,000.00 USD | 0.00 USD | 13,750,000.00 USD | 1,010.00 USD | 5,010.00 USD | 0.00 USD |
| `1D` | `0.3019` | 13,740,000.00 USD | 0.00 USD | 13,740,000.00 USD | 14,850.00 USD | 6,650.00 USD | 16,590.00 USD |
| `7D` | `0.3019` | 19,160,000.00 USD | 0.00 USD | 19,160,000.00 USD | 0.00 USD | 8,660.00 USD | 0.00 USD |
| `1D` | `0.3023` | 13,700,000.00 USD | 0.00 USD | 13,700,000.00 USD | 1,330.00 USD | 6,590.00 USD | 0.00 USD |
| `7D` | `0.3025` | 19,150,000.00 USD | 0.00 USD | 19,150,000.00 USD | 0.00 USD | 9,860.00 USD | 0.00 USD |
| `1D` | `0.3027` | 13,690,000.00 USD | 0.00 USD | 13,690,000.00 USD | 23,690.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3031` | 13,670,000.00 USD | 0.00 USD | 13,670,000.00 USD | 2,480.00 USD | 8,320.00 USD | 6,190.00 USD |
| `7D` | `0.3031` | 19,140,000.00 USD | 0.00 USD | 19,140,000.00 USD | 50,940.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3035` | 13,650,000.00 USD | 0.00 USD | 13,650,000.00 USD | 742.30 USD | 3,230.00 USD | 12,600.00 USD |
| `7D` | `0.3037` | 19,090,000.00 USD | 0.00 USD | 19,090,000.00 USD | 2,700.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3039` | 13,640,000.00 USD | 0.00 USD | 13,640,000.00 USD | 1,060.00 USD | 0.00 USD | 44,700.00 USD |
| `1D` | `0.3043` | 13,590,000.00 USD | 0.00 USD | 13,590,000.00 USD | 0.00 USD | 20,130.00 USD | 11,650.00 USD |
| `7D` | `0.3043` | 19,080,000.00 USD | 0.00 USD | 19,080,000.00 USD | 1,880.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3047` | 13,560,000.00 USD | 0.00 USD | 13,560,000.00 USD | 31,710.00 USD | 13,780.00 USD | 49,740.00 USD |
| `7D` | `0.3049` | 19,080,000.00 USD | 0.00 USD | 19,080,000.00 USD | 18,020.00 USD | 0.00 USD | 66,870.00 USD |
| `1D` | `0.3051` | 13,460,000.00 USD | 0.00 USD | 13,460,000.00 USD | 18,730.00 USD | 2,510.00 USD | 11,570.00 USD |
| `1D` | `0.3055` | 13,430,000.00 USD | 0.00 USD | 13,430,000.00 USD | 28,250.00 USD | 13,380.00 USD | 37,740.00 USD |
| `7D` | `0.3055` | 19,000,000.00 USD | 0.00 USD | 19,000,000.00 USD | 1,760.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3061` | 19,000,000.00 USD | 0.00 USD | 19,000,000.00 USD | 32,680.00 USD | 7,690.00 USD | 37,210.00 USD |
| `1D` | `0.3063` | 13,350,000.00 USD | 0.00 USD | 13,350,000.00 USD | 885.25 USD | 16,530.00 USD | 56,460.00 USD |
| `1D` | `0.3067` | 13,280,000.00 USD | 0.00 USD | 13,280,000.00 USD | 31,110.00 USD | 15,440.00 USD | 35,690.00 USD |
| `7D` | `0.3067` | 18,920,000.00 USD | 0.00 USD | 18,920,000.00 USD | 6,500.00 USD | 8,110.00 USD | 0.00 USD |
| `1D` | `0.3071` | 13,200,000.00 USD | 0.00 USD | 13,200,000.00 USD | 67.24 USD | 0.00 USD | 12,760.00 USD |
| `7D` | `0.3073` | 18,900,000.00 USD | 0.00 USD | 18,900,000.00 USD | 7,350.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3075` | 13,180,000.00 USD | 0.00 USD | 13,180,000.00 USD | 23,570.00 USD | 1,940.00 USD | 0.00 USD |
| `1D` | `0.3079` | 13,160,000.00 USD | 0.00 USD | 13,160,000.00 USD | 15.29 USD | 0.00 USD | 12,250.00 USD |
| `7D` | `0.3079` | 18,900,000.00 USD | 0.00 USD | 18,900,000.00 USD | 38,320.00 USD | 10,270.00 USD | 50,200.00 USD |
| `1D` | `0.3083` | 13,150,000.00 USD | 0.00 USD | 13,150,000.00 USD | 18,620.00 USD | 0.00 USD | 15,810.00 USD |
| `7D` | `0.3085` | 18,800,000.00 USD | 0.00 USD | 18,800,000.00 USD | 2,360.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3087` | 13,110,000.00 USD | 0.00 USD | 13,110,000.00 USD | 623.99 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3091` | 13,110,000.00 USD | 0.00 USD | 13,110,000.00 USD | 31.03 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3091` | 18,790,000.00 USD | 0.00 USD | 18,790,000.00 USD | 8,030.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3095` | 13,110,000.00 USD | 0.00 USD | 13,110,000.00 USD | 17,320.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3097` | 18,790,000.00 USD | 0.00 USD | 18,790,000.00 USD | 75,040.00 USD | 3,620.00 USD | 54,360.00 USD |
| `1D` | `0.3099` | 13,090,000.00 USD | 0.00 USD | 13,090,000.00 USD | 8,120.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3103` | 13,080,000.00 USD | 0.00 USD | 13,080,000.00 USD | 58,110.00 USD | 15,820.00 USD | 46,470.00 USD |
| `7D` | `0.3103` | 18,650,000.00 USD | 0.00 USD | 18,650,000.00 USD | 67,180.00 USD | 0.00 USD | 63,310.00 USD |
| `1D` | `0.3107` | 12,960,000.00 USD | 0.00 USD | 12,960,000.00 USD | 1,350.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3109` | 18,520,000.00 USD | 0.00 USD | 18,520,000.00 USD | 6,400.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3115` | 12,960,000.00 USD | 0.00 USD | 12,960,000.00 USD | 977.81 USD | 9,110.00 USD | 17,620.00 USD |
| `7D` | `0.3115` | 18,520,000.00 USD | 0.00 USD | 18,520,000.00 USD | 10,340.00 USD | 0.00 USD | 37,490.00 USD |
| `1D` | `0.3119` | 12,940,000.00 USD | 0.00 USD | 12,940,000.00 USD | 26,060.00 USD | 10,650.00 USD | 17,440.00 USD |
| `7D` | `0.3121` | 18,470,000.00 USD | 0.00 USD | 18,470,000.00 USD | 162,580.00 USD | 19,620.00 USD | 0.00 USD |
| `1D` | `0.3123` | 12,880,000.00 USD | 0.00 USD | 12,880,000.00 USD | 12,740.00 USD | 0.00 USD | 16,390.00 USD |
| `1D` | `0.3127` | 12,850,000.00 USD | 0.00 USD | 12,850,000.00 USD | 2,050.00 USD | 39,470.00 USD | 7,580.00 USD |
| `7D` | `0.3127` | 18,290,000.00 USD | 0.00 USD | 18,290,000.00 USD | 21,180.00 USD | 54,460.00 USD | 57,690.00 USD |
| `1D` | `0.3131` | 12,800,000.00 USD | 0.00 USD | 12,800,000.00 USD | 3,600.00 USD | 2,520.00 USD | 21,520.00 USD |
| `7D` | `0.3133` | 18,150,000.00 USD | 0.00 USD | 18,150,000.00 USD | 5,070.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3135` | 12,780,000.00 USD | 0.00 USD | 12,780,000.00 USD | 5,830.00 USD | 23,940.00 USD | 9,590.00 USD |
| `1D` | `0.3139` | 12,740,000.00 USD | 0.00 USD | 12,740,000.00 USD | 4,710.00 USD | 10,610.00 USD | 0.00 USD |
| `7D` | `0.3139` | 18,150,000.00 USD | 0.00 USD | 18,150,000.00 USD | 2,240.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3143` | 12,720,000.00 USD | 0.00 USD | 12,720,000.00 USD | 3,210.00 USD | 3,580.00 USD | 9,540.00 USD |
| `7D` | `0.3145` | 18,150,000.00 USD | 0.00 USD | 18,150,000.00 USD | 247,810.00 USD | 51,270.00 USD | 17,870.00 USD |
| `1D` | `0.3147` | 12,700,000.00 USD | 0.00 USD | 12,700,000.00 USD | 2,670.00 USD | 2,330.00 USD | 0.00 USD |
| `1D` | `0.3151` | 12,700,000.00 USD | 0.00 USD | 12,700,000.00 USD | 4,850.00 USD | 23,750.00 USD | 0.00 USD |
| `7D` | `0.3151` | 17,830,000.00 USD | 0.00 USD | 17,830,000.00 USD | 196,920.00 USD | 23,130.00 USD | 49,320.00 USD |
| `1D` | `0.3155` | 12,670,000.00 USD | 0.00 USD | 12,670,000.00 USD | 33,260.00 USD | 3,680.00 USD | 10,790.00 USD |
| `7D` | `0.3157` | 17,560,000.00 USD | 0.00 USD | 17,560,000.00 USD | 392,580.00 USD | 93,740.00 USD | 60,300.00 USD |
| `1D` | `0.3159` | 12,620,000.00 USD | 0.00 USD | 12,620,000.00 USD | 5,120.00 USD | 0.00 USD | 5,450.00 USD |
| `1D` | `0.3163` | 12,610,000.00 USD | 0.00 USD | 12,610,000.00 USD | 3,780.00 USD | 33,960.00 USD | 0.00 USD |
| `7D` | `0.3163` | 17,010,000.00 USD | 0.00 USD | 17,010,000.00 USD | 478,060.00 USD | 182,370.00 USD | 192,840.00 USD |
| `1D` | `0.3167` | 12,570,000.00 USD | 0.00 USD | 12,570,000.00 USD | 43,210.00 USD | 6,270.00 USD | 17,210.00 USD |
| `7D` | `0.3169` | 16,160,000.00 USD | 0.00 USD | 16,160,000.00 USD | 417,380.00 USD | 106,680.00 USD | 135,950.00 USD |
| `1D` | `0.3171` | 12,510,000.00 USD | 0.00 USD | 12,510,000.00 USD | 8,020.00 USD | 35,130.00 USD | 35,030.00 USD |
| `1D` | `0.3175` | 12,430,000.00 USD | 0.00 USD | 12,430,000.00 USD | 19,750.00 USD | 7,370.00 USD | 14,490.00 USD |
| `7D` | `0.3175` | 15,500,000.00 USD | 0.00 USD | 15,500,000.00 USD | 140,810.00 USD | 53,470.00 USD | 69,280.00 USD |
| `1D` | `0.3179` | 12,390,000.00 USD | 0.00 USD | 12,390,000.00 USD | 62,280.00 USD | 25,310.00 USD | 43,110.00 USD |
| `7D` | `0.3181` | 15,240,000.00 USD | 0.00 USD | 15,240,000.00 USD | 751,290.00 USD | 76,910.00 USD | 182,330.00 USD |
| `1D` | `0.3183` | 12,260,000.00 USD | 0.00 USD | 12,260,000.00 USD | 363,000.00 USD | 39,030.00 USD | 73,930.00 USD |
| `1D` | `0.3187` | 11,780,000.00 USD | 0.00 USD | 11,780,000.00 USD | 92,220.00 USD | 41,750.00 USD | 77,560.00 USD |
| `7D` | `0.3187` | 14,230,000.00 USD | 0.00 USD | 14,230,000.00 USD | 408,400.00 USD | 97,820.00 USD | 24,770.00 USD |
| `1D` | `0.3191` | 11,570,000.00 USD | 0.00 USD | 11,570,000.00 USD | 203,200.00 USD | 13,910.00 USD | 45,560.00 USD |
| `7D` | `0.3193` | 13,690,000.00 USD | 0.00 USD | 13,690,000.00 USD | 118,210.00 USD | 104,710.00 USD | 247,300.00 USD |
| `1D` | `0.3195` | 11,310,000.00 USD | 0.00 USD | 11,310,000.00 USD | 93,760.00 USD | 169,840.00 USD | 242,890.00 USD |
| `1D` | `0.3199` | 10,800,000.00 USD | 0.00 USD | 10,800,000.00 USD | 82,300.00 USD | 60,220.00 USD | 102,370.00 USD |
| `7D` | `0.3199` | 13,220,000.00 USD | 0.00 USD | 13,220,000.00 USD | 0.00 USD | 127,390.00 USD | 190,470.00 USD |
| `1D` | `0.3203` | 10,560,000.00 USD | 0.00 USD | 10,560,000.00 USD | 246,790.00 USD | 56,790.00 USD | 109,780.00 USD |
| `7D` | `0.3205` | 12,910,000.00 USD | 0.00 USD | 12,910,000.00 USD | 100,160.00 USD | 59,200.00 USD | 130,760.00 USD |
| `1D` | `0.3207` | 10,140,000.00 USD | 0.00 USD | 10,140,000.00 USD | 133,880.00 USD | 25,490.00 USD | 108,030.00 USD |
| `1D` | `0.3211` | 9,870,000.00 USD | 0.00 USD | 9,870,000.00 USD | 108,130.00 USD | 27,010.00 USD | 99,450.00 USD |
| `7D` | `0.3211` | 12,620,000.00 USD | 0.00 USD | 12,620,000.00 USD | 569,720.00 USD | 117,230.00 USD | 244,340.00 USD |
| `1D` | `0.3215` | 9,640,000.00 USD | 0.00 USD | 9,640,000.00 USD | 0.00 USD | 33,650.00 USD | 78,920.00 USD |
| `7D` | `0.3217` | 11,690,000.00 USD | 0.00 USD | 11,690,000.00 USD | 286,830.00 USD | 58,690.00 USD | 107,900.00 USD |
| `1D` | `0.3219` | 9,530,000.00 USD | 0.00 USD | 9,530,000.00 USD | 5,550.00 USD | 23,450.00 USD | 72,520.00 USD |
| `1D` | `0.3223` | 9,430,000.00 USD | 0.00 USD | 9,430,000.00 USD | 154,560.00 USD | 41,870.00 USD | 120,750.00 USD |
| `7D` | `0.3223` | 11,230,000.00 USD | 0.00 USD | 11,230,000.00 USD | 643,460.00 USD | 196,690.00 USD | 103,370.00 USD |
| `1D` | `0.3227` | 9,110,000.00 USD | 0.00 USD | 9,110,000.00 USD | 52,010.00 USD | 50,480.00 USD | 81,740.00 USD |
| `7D` | `0.3229` | 10,290,000.00 USD | 0.00 USD | 10,290,000.00 USD | 858,070.00 USD | 299,190.00 USD | 385,680.00 USD |
| `1D` | `0.3231` | 8,920,000.00 USD | 0.00 USD | 8,920,000.00 USD | 54,440.00 USD | 17,630.00 USD | 120,280.00 USD |
| `1D` | `0.3235` | 8,730,000.00 USD | 0.00 USD | 8,730,000.00 USD | 61,120.00 USD | 97,560.00 USD | 151,550.00 USD |
| `7D` | `0.3235` | 8,750,000.00 USD | 0.00 USD | 8,750,000.00 USD | 709,160.00 USD | 213,370.00 USD | 359,100.00 USD |
| `1D` | `0.3239` | 8,420,000.00 USD | 0.00 USD | 8,420,000.00 USD | 0.00 USD | 32,340.00 USD | 65,220.00 USD |
| `7D` | `0.3241` | 7,460,000.00 USD | 0.00 USD | 7,460,000.00 USD | 433,820.00 USD | 149,860.00 USD | 138,560.00 USD |
| `1D` | `0.3243` | 8,320,000.00 USD | 0.00 USD | 8,320,000.00 USD | 125,350.00 USD | 41,210.00 USD | 223,350.00 USD |
| `1D` | `0.3247` | 7,930,000.00 USD | 0.00 USD | 7,930,000.00 USD | 331,430.00 USD | 76,120.00 USD | 207,260.00 USD |
| `7D` | `0.3247` | 6,740,000.00 USD | 0.00 USD | 6,740,000.00 USD | 846,180.00 USD | 127,310.00 USD | 353,590.00 USD |
| `1D` | `0.3251` | 7,320,000.00 USD | 0.00 USD | 7,320,000.00 USD | 683,170.00 USD | 89,590.00 USD | 300,060.00 USD |
| `7D` | `0.3253` | 5,410,000.00 USD | 0.00 USD | 5,410,000.00 USD | 1,220,000.00 USD | 137,440.00 USD | 241,690.00 USD |
| `1D` | `0.3255` | 6,250,000.00 USD | 0.00 USD | 6,250,000.00 USD | 428,540.00 USD | 89,190.00 USD | 271,020.00 USD |
| `1D` | `0.3259` | 5,460,000.00 USD | 0.00 USD | 5,460,000.00 USD | 346,750.00 USD | 215,120.00 USD | 414,300.00 USD |
| `7D` | `0.3259` | 3,810,000.00 USD | 0.00 USD | 3,810,000.00 USD | 182,240.00 USD | 250,110.00 USD | 503,650.00 USD |
| `1D` | `0.3263` | 4,480,000.00 USD | 0.00 USD | 4,480,000.00 USD | 27,080.00 USD | 240,230.00 USD | 320,610.00 USD |
| `7D` | `0.3265` | 2,880,000.00 USD | 0.00 USD | 2,880,000.00 USD | 80,160.00 USD | 197,270.00 USD | 347,150.00 USD |
| `1D` | `0.3267` | 3,890,000.00 USD | 0.00 USD | 3,890,000.00 USD | 44,720.00 USD | 159,870.00 USD | 341,370.00 USD |
| `1D` | `0.3271` | 3,350,000.00 USD | 0.00 USD | 3,350,000.00 USD | 237,730.00 USD | 81,010.00 USD | 340,330.00 USD |
| `7D` | `0.3271` | 2,250,000.00 USD | 0.00 USD | 2,250,000.00 USD | 192,500.00 USD | 138,680.00 USD | 261,530.00 USD |
| `1D` | `0.3275` | 2,690,000.00 USD | 0.00 USD | 2,690,000.00 USD | 259,200.00 USD | 54,310.00 USD | 140,050.00 USD |
| `7D` | `0.3277` | 1,660,000.00 USD | 0.00 USD | 1,660,000.00 USD | 0.00 USD | 29,390.00 USD | 85,620.00 USD |
| `1D` | `0.3279` | 2,240,000.00 USD | 0.00 USD | 2,240,000.00 USD | 164,690.00 USD | 55,350.00 USD | 133,800.00 USD |
| `1D` | `0.3283` | 1,880,000.00 USD | 0.00 USD | 1,880,000.00 USD | 0.00 USD | 29,070.00 USD | 16,760.00 USD |
| `7D` | `0.3283` | 1,550,000.00 USD | 0.00 USD | 1,550,000.00 USD | 89,030.00 USD | 25,670.00 USD | 275,050.00 USD |
| `1D` | `0.3287` | 1,840,000.00 USD | 0.00 USD | 1,840,000.00 USD | 117,140.00 USD | 39,260.00 USD | 146,190.00 USD |
| `7D` | `0.3289` | 1,160,000.00 USD | 0.00 USD | 1,160,000.00 USD | 0.00 USD | 43,290.00 USD | 0.00 USD |
| `1D` | `0.3291` | 1,530,000.00 USD | 0.00 USD | 1,530,000.00 USD | 38,710.00 USD | 66,400.00 USD | 119,580.00 USD |
| `1D` | `0.3295` | 1,310,000.00 USD | 0.00 USD | 1,310,000.00 USD | 61,960.00 USD | 15,860.00 USD | 0.00 USD |
| `7D` | `0.3295` | 1,110,000.00 USD | 0.00 USD | 1,110,000.00 USD | 255,850.00 USD | 83,080.00 USD | 0.00 USD |
| `1D` | `0.3299` | 1,230,000.00 USD | 0.00 USD | 1,230,000.00 USD | 141,790.00 USD | 18,090.00 USD | 30,950.00 USD |
| `7D` | `0.3301` | 774,520.00 USD | 0.00 USD | 774,520.00 USD | 184,120.00 USD | 9,050.00 USD | 0.00 USD |
| `1D` | `0.3303` | 1,040,000.00 USD | 0.00 USD | 1,040,000.00 USD | 1,210.00 USD | 58,700.00 USD | 74,690.00 USD |
| `1D` | `0.3307` | 905,630.00 USD | 0.00 USD | 905,630.00 USD | 121,770.00 USD | 37,920.00 USD | 87,100.00 USD |
| `7D` | `0.3307` | 581,350.00 USD | 0.00 USD | 581,350.00 USD | 167,950.00 USD | 10,690.00 USD | 294,170.00 USD |
| `1D` | `0.3311` | 658,840.00 USD | 0.00 USD | 658,840.00 USD | 644.45 USD | 100,700.00 USD | 416,060.00 USD |
| `7D` | `0.3313` | 108,550.00 USD | 0.00 USD | 108,550.00 USD | 0.00 USD | 50,650.00 USD | 0.00 USD |
| `1D` | `0.3315` | 141,440.00 USD | 0.00 USD | 141,440.00 USD | 0.00 USD | 65,830.00 USD | 28,340.00 USD |
| `1D` | `0.3319` | 47,270.00 USD | 0.00 USD | 47,270.00 USD | 0.00 USD | 47,270.00 USD | 0.00 USD |
| `7D` | `0.3319` | 57,890.00 USD | 0.00 USD | 57,890.00 USD | 0.00 USD | 57,890.00 USD | 0.00 USD |
| `7D` | `0.3323` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3355` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3359` | 144,280.00 USD | 144,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 144,280.00 USD |
| `1D` | `0.3367` | 217,200.00 USD | 217,200.00 USD | 0.00 USD | 72,920.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3375` | 546,840.00 USD | 546,840.00 USD | 0.00 USD | 329,640.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3379` | 21,390.00 USD | 21,390.00 USD | 0.00 USD | 0.00 USD | 21,390.00 USD | 0.00 USD |
| `1D` | `0.3383` | 646,770.00 USD | 646,770.00 USD | 0.00 USD | 71,900.00 USD | 0.00 USD | 28,030.00 USD |
| `7D` | `0.3385` | 147,040.00 USD | 147,040.00 USD | 0.00 USD | 125,650.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3387` | 822,450.00 USD | 822,450.00 USD | 0.00 USD | 137,130.00 USD | 11,160.00 USD | 27,380.00 USD |
| `1D` | `0.3391` | 1,160,000.00 USD | 1,160,000.00 USD | 0.00 USD | 258,550.00 USD | 27,820.00 USD | 49,390.00 USD |
| `7D` | `0.3391` | 381,700.00 USD | 381,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 234,660.00 USD |
| `1D` | `0.3395` | 2,090,000.00 USD | 2,090,000.00 USD | 0.00 USD | 115,280.00 USD | 333,450.00 USD | 485,780.00 USD |
| `7D` | `0.3397` | 1,640,000.00 USD | 1,640,000.00 USD | 0.00 USD | 262,880.00 USD | 586,760.00 USD | 410,790.00 USD |
| `1D` | `0.3399` | 2,480,000.00 USD | 2,480,000.00 USD | 0.00 USD | 43,780.00 USD | 120,440.00 USD | 218,200.00 USD |
| `1D` | `0.3403` | 3,080,000.00 USD | 3,080,000.00 USD | 0.00 USD | 209,800.00 USD | 61,580.00 USD | 336,240.00 USD |
| `7D` | `0.3403` | 3,040,000.00 USD | 3,040,000.00 USD | 0.00 USD | 1,070,000.00 USD | 103,630.00 USD | 223,390.00 USD |
| `1D` | `0.3407` | 3,250,000.00 USD | 3,250,000.00 USD | 0.00 USD | 71,510.00 USD | 0.00 USD | 100,230.00 USD |
| `7D` | `0.3409` | 3,510,000.00 USD | 3,510,000.00 USD | 0.00 USD | 0.00 USD | 29,390.00 USD | 446,990.00 USD |
| `1D` | `0.3411` | 3,610,000.00 USD | 3,610,000.00 USD | 0.00 USD | 265,070.00 USD | 39,790.00 USD | 45,840.00 USD |
| `1D` | `0.3415` | 4,410,000.00 USD | 4,410,000.00 USD | 0.00 USD | 672,650.00 USD | 21,540.00 USD | 107,320.00 USD |
| `7D` | `0.3415` | 3,600,000.00 USD | 3,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 85,620.00 USD |
| `1D` | `0.3419` | 4,490,000.00 USD | 4,490,000.00 USD | 0.00 USD | 39,640.00 USD | 48,460.00 USD | 0.00 USD |
| `7D` | `0.3421` | 3,640,000.00 USD | 3,640,000.00 USD | 0.00 USD | 0.00 USD | 43,290.00 USD | 0.00 USD |
| `1D` | `0.3423` | 4,600,000.00 USD | 4,600,000.00 USD | 0.00 USD | 71,180.00 USD | 33,440.00 USD | 0.00 USD |
| `1D` | `0.3427` | 4,790,000.00 USD | 4,790,000.00 USD | 0.00 USD | 0.00 USD | 195,320.00 USD | 0.00 USD |
| `7D` | `0.3427` | 3,730,000.00 USD | 3,730,000.00 USD | 0.00 USD | 0.00 USD | 92,380.00 USD | 0.00 USD |
| `1D` | `0.3431` | 5,160,000.00 USD | 5,160,000.00 USD | 0.00 USD | 166,310.00 USD | 193,980.00 USD | 0.00 USD |
| `7D` | `0.3433` | 3,990,000.00 USD | 3,990,000.00 USD | 0.00 USD | 254,700.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3435` | 5,300,000.00 USD | 5,300,000.00 USD | 0.00 USD | 0.00 USD | 117,530.00 USD | 30,950.00 USD |
| `1D` | `0.3439` | 5,400,000.00 USD | 5,400,000.00 USD | 0.00 USD | 0.00 USD | 31,310.00 USD | 62,980.00 USD |
| `1D` | `0.3443` | 5,450,000.00 USD | 5,450,000.00 USD | 0.00 USD | 0.00 USD | 38,110.00 USD | 18,140.00 USD |
| `7D` | `0.3445` | 4,090,000.00 USD | 4,090,000.00 USD | 0.00 USD | 103,130.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3447` | 5,680,000.00 USD | 5,680,000.00 USD | 0.00 USD | 22,420.00 USD | 57,000.00 USD | 146,340.00 USD |
| `1D` | `0.3451` | 5,910,000.00 USD | 5,910,000.00 USD | 0.00 USD | 70,130.00 USD | 63,000.00 USD | 99,020.00 USD |
| `7D` | `0.3451` | 4,180,000.00 USD | 4,180,000.00 USD | 0.00 USD | 62,830.00 USD | 28,550.00 USD | 0.00 USD |
| `1D` | `0.3455` | 6,240,000.00 USD | 6,240,000.00 USD | 0.00 USD | 169,370.00 USD | 37,860.00 USD | 116,160.00 USD |
| `7D` | `0.3457` | 4,540,000.00 USD | 4,540,000.00 USD | 0.00 USD | 0.00 USD | 29,340.00 USD | 332,190.00 USD |
| `1D` | `0.3459` | 7,070,000.00 USD | 7,070,000.00 USD | 0.00 USD | 214,990.00 USD | 131,290.00 USD | 485,400.00 USD |
| `1D` | `0.3463` | 7,360,000.00 USD | 7,360,000.00 USD | 0.00 USD | 13,540.00 USD | 118,340.00 USD | 160,310.00 USD |
| `7D` | `0.3463` | 4,920,000.00 USD | 4,920,000.00 USD | 0.00 USD | 0.00 USD | 167,950.00 USD | 205,390.00 USD |
| `1D` | `0.3467` | 7,530,000.00 USD | 7,530,000.00 USD | 0.00 USD | 21,890.00 USD | 48,850.00 USD | 100,110.00 USD |
| `7D` | `0.3469` | 5,110,000.00 USD | 5,110,000.00 USD | 0.00 USD | 60,310.00 USD | 51,820.00 USD | 75,520.00 USD |
| `1D` | `0.3471` | 7,630,000.00 USD | 7,630,000.00 USD | 0.00 USD | 37,620.00 USD | 38,220.00 USD | 25,030.00 USD |
| `1D` | `0.3475` | 7,740,000.00 USD | 7,740,000.00 USD | 0.00 USD | 0.00 USD | 59,710.00 USD | 45,010.00 USD |
| `7D` | `0.3475` | 5,150,000.00 USD | 5,150,000.00 USD | 0.00 USD | 0.00 USD | 40,540.00 USD | 0.00 USD |
| `1D` | `0.3479` | 7,980,000.00 USD | 7,980,000.00 USD | 0.00 USD | 105,220.00 USD | 16,550.00 USD | 120,420.00 USD |
| `7D` | `0.3481` | 5,210,000.00 USD | 5,210,000.00 USD | 0.00 USD | 6,440.00 USD | 14,700.00 USD | 42,810.00 USD |
| `1D` | `0.3483` | 8,010,000.00 USD | 8,010,000.00 USD | 0.00 USD | 3,430.00 USD | 22,220.00 USD | 8,380.00 USD |
| `1D` | `0.3487` | 8,050,000.00 USD | 8,050,000.00 USD | 0.00 USD | 8,610.00 USD | 27,650.00 USD | 0.00 USD |
| `7D` | `0.3487` | 5,230,000.00 USD | 5,230,000.00 USD | 0.00 USD | 0.00 USD | 21,650.00 USD | 0.00 USD |
| `1D` | `0.3491` | 8,180,000.00 USD | 8,180,000.00 USD | 0.00 USD | 40,710.00 USD | 28,080.00 USD | 61,240.00 USD |
| `7D` | `0.3493` | 5,260,000.00 USD | 5,260,000.00 USD | 0.00 USD | 0.00 USD | 24,660.00 USD | 0.00 USD |
| `1D` | `0.3495` | 8,300,000.00 USD | 8,300,000.00 USD | 0.00 USD | 34,020.00 USD | 13,050.00 USD | 79,030.00 USD |
| `1D` | `0.3499` | 8,740,000.00 USD | 8,740,000.00 USD | 0.00 USD | 52,670.00 USD | 9,040.00 USD | 375,650.00 USD |
| `7D` | `0.3499` | 5,390,000.00 USD | 5,390,000.00 USD | 0.00 USD | 133,490.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3503` | 8,820,000.00 USD | 8,820,000.00 USD | 0.00 USD | 0.00 USD | 29,350.00 USD | 50,760.00 USD |
| `7D` | `0.3505` | 5,400,000.00 USD | 5,400,000.00 USD | 0.00 USD | 12,030.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3507` | 8,940,000.00 USD | 8,940,000.00 USD | 0.00 USD | 75,920.00 USD | 8,080.00 USD | 31,490.00 USD |
| `1D` | `0.3511` | 8,980,000.00 USD | 8,980,000.00 USD | 0.00 USD | 1,090.00 USD | 4,320.00 USD | 32,490.00 USD |
| `7D` | `0.3511` | 6,360,000.00 USD | 6,360,000.00 USD | 0.00 USD | 690,500.00 USD | 0.00 USD | 271,800.00 USD |
| `1D` | `0.3515` | 9,080,000.00 USD | 9,080,000.00 USD | 0.00 USD | 21,910.00 USD | 0.00 USD | 87,340.00 USD |
| `7D` | `0.3517` | 6,380,000.00 USD | 6,380,000.00 USD | 0.00 USD | 12,290.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3519` | 9,170,000.00 USD | 9,170,000.00 USD | 0.00 USD | 30,510.00 USD | 23,960.00 USD | 28,330.00 USD |
| `1D` | `0.3523` | 9,170,000.00 USD | 9,170,000.00 USD | 0.00 USD | 3,190.00 USD | 3,730.00 USD | 0.00 USD |
| `7D` | `0.3523` | 6,790,000.00 USD | 6,790,000.00 USD | 0.00 USD | 277,410.00 USD | 28,950.00 USD | 107,430.00 USD |
| `1D` | `0.3527` | 9,340,000.00 USD | 9,340,000.00 USD | 0.00 USD | 102,610.00 USD | 38,340.00 USD | 28,910.00 USD |
| `1D` | `0.3531` | 9,500,000.00 USD | 9,500,000.00 USD | 0.00 USD | 6,270.00 USD | 61,120.00 USD | 88,110.00 USD |
| `1D` | `0.3535` | 9,750,000.00 USD | 9,750,000.00 USD | 0.00 USD | 125,280.00 USD | 16,340.00 USD | 113,320.00 USD |
| `7D` | `0.3535` | 7,060,000.00 USD | 7,060,000.00 USD | 0.00 USD | 4,830.00 USD | 77,960.00 USD | 187,450.00 USD |
| `1D` | `0.3539` | 9,930,000.00 USD | 9,930,000.00 USD | 0.00 USD | 57,460.00 USD | 33,520.00 USD | 81,960.00 USD |
| `7D` | `0.3541` | 7,980,000.00 USD | 7,980,000.00 USD | 0.00 USD | 799,020.00 USD | 118,370.00 USD | 0.00 USD |
| `1D` | `0.3543` | 10,100,000.00 USD | 10,100,000.00 USD | 0.00 USD | 28,820.00 USD | 107,380.00 USD | 37,920.00 USD |
| `1D` | `0.3547` | 10,170,000.00 USD | 10,170,000.00 USD | 0.00 USD | 5,090.00 USD | 28,920.00 USD | 31,910.00 USD |
| `7D` | `0.3547` | 8,280,000.00 USD | 8,280,000.00 USD | 0.00 USD | 11,040.00 USD | 0.00 USD | 288,450.00 USD |
| `1D` | `0.3551` | 10,250,000.00 USD | 10,250,000.00 USD | 0.00 USD | 4,060.00 USD | 29,900.00 USD | 47,950.00 USD |
| `7D` | `0.3553` | 8,390,000.00 USD | 8,390,000.00 USD | 0.00 USD | 0.00 USD | 117,050.00 USD | 0.00 USD |
| `1D` | `0.3555` | 10,310,000.00 USD | 10,310,000.00 USD | 0.00 USD | 20,180.00 USD | 44,130.00 USD | 0.00 USD |
| `1D` | `0.3559` | 10,410,000.00 USD | 10,410,000.00 USD | 0.00 USD | 331.60 USD | 21,340.00 USD | 78,340.00 USD |
| `7D` | `0.3559` | 8,410,000.00 USD | 8,410,000.00 USD | 0.00 USD | 13,630.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3563` | 10,510,000.00 USD | 10,510,000.00 USD | 0.00 USD | 977.81 USD | 29,510.00 USD | 67,310.00 USD |
| `7D` | `0.3565` | 8,450,000.00 USD | 8,450,000.00 USD | 0.00 USD | 0.00 USD | 43,060.00 USD | 0.00 USD |
| `1D` | `0.3567` | 10,510,000.00 USD | 10,510,000.00 USD | 0.00 USD | 3,540.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3571` | 10,520,000.00 USD | 10,520,000.00 USD | 0.00 USD | 1,770.00 USD | 6,920.00 USD | 0.00 USD |
| `7D` | `0.3571` | 8,460,000.00 USD | 8,460,000.00 USD | 0.00 USD | 9,210.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3575` | 10,690,000.00 USD | 10,690,000.00 USD | 0.00 USD | 161,360.00 USD | 9,250.00 USD | 0.00 USD |
| `7D` | `0.3577` | 8,590,000.00 USD | 8,590,000.00 USD | 0.00 USD | 124,630.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3579` | 10,740,000.00 USD | 10,740,000.00 USD | 0.00 USD | 1,690.00 USD | 9,130.00 USD | 38,950.00 USD |
| `1D` | `0.3583` | 10,770,000.00 USD | 10,770,000.00 USD | 0.00 USD | 14,980.00 USD | 14,930.00 USD | 0.00 USD |
| `7D` | `0.3583` | 8,720,000.00 USD | 8,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 135,900.00 USD |
| `1D` | `0.3587` | 10,780,000.00 USD | 10,780,000.00 USD | 0.00 USD | 5,760.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3589` | 9,090,000.00 USD | 9,090,000.00 USD | 0.00 USD | 0.00 USD | 50,650.00 USD | 320,430.00 USD |
| `1D` | `0.3591` | 10,850,000.00 USD | 10,850,000.00 USD | 0.00 USD | 22,510.00 USD | 15,750.00 USD | 33,590.00 USD |
| `1D` | `0.3595` | 11,040,000.00 USD | 11,040,000.00 USD | 0.00 USD | 93,010.00 USD | 0.00 USD | 99,590.00 USD |
| `7D` | `0.3595` | 9,240,000.00 USD | 9,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 146,290.00 USD |
| `1D` | `0.3599` | 11,220,000.00 USD | 11,220,000.00 USD | 0.00 USD | 47,370.00 USD | 22,780.00 USD | 108,510.00 USD |
| `7D` | `0.3601` | 9,740,000.00 USD | 9,740,000.00 USD | 0.00 USD | 4,040.00 USD | 161,200.00 USD | 338,540.00 USD |
| `1D` | `0.3603` | 11,390,000.00 USD | 11,390,000.00 USD | 0.00 USD | 32,230.00 USD | 41,780.00 USD | 92,600.00 USD |
| `1D` | `0.3607` | 11,600,000.00 USD | 11,600,000.00 USD | 0.00 USD | 28,890.00 USD | 22,500.00 USD | 157,390.00 USD |
| `7D` | `0.3607` | 10,140,000.00 USD | 10,140,000.00 USD | 0.00 USD | 330,200.00 USD | 68,030.00 USD | 0.00 USD |
| `1D` | `0.3611` | 11,930,000.00 USD | 11,930,000.00 USD | 0.00 USD | 86,030.00 USD | 54,830.00 USD | 190,770.00 USD |
| `7D` | `0.3613` | 10,840,000.00 USD | 10,840,000.00 USD | 0.00 USD | 77,710.00 USD | 330,040.00 USD | 288,930.00 USD |
| `1D` | `0.3615` | 12,110,000.00 USD | 12,110,000.00 USD | 0.00 USD | 0.00 USD | 31,910.00 USD | 150,170.00 USD |
| `1D` | `0.3619` | 12,590,000.00 USD | 12,590,000.00 USD | 0.00 USD | 368,610.00 USD | 110,060.00 USD | 0.00 USD |
| `7D` | `0.3619` | 11,050,000.00 USD | 11,050,000.00 USD | 0.00 USD | 3,500.00 USD | 209,940.00 USD | 0.00 USD |
| `1D` | `0.3623` | 12,770,000.00 USD | 12,770,000.00 USD | 0.00 USD | 83,390.00 USD | 20,060.00 USD | 71,510.00 USD |
| `7D` | `0.3625` | 11,240,000.00 USD | 11,240,000.00 USD | 0.00 USD | 2,410.00 USD | 191,880.00 USD | 0.00 USD |
| `1D` | `0.3627` | 13,140,000.00 USD | 13,140,000.00 USD | 0.00 USD | 337,420.00 USD | 39,070.00 USD | 0.00 USD |
| `1D` | `0.3631` | 14,280,000.00 USD | 14,280,000.00 USD | 0.00 USD | 941,740.00 USD | 102,260.00 USD | 93,510.00 USD |
| `7D` | `0.3631` | 11,360,000.00 USD | 11,360,000.00 USD | 0.00 USD | 678.26 USD | 114,740.00 USD | 0.00 USD |
| `1D` | `0.3635` | 14,510,000.00 USD | 14,510,000.00 USD | 0.00 USD | 0.00 USD | 48,500.00 USD | 185,880.00 USD |
| `7D` | `0.3637` | 11,380,000.00 USD | 11,380,000.00 USD | 0.00 USD | 937.01 USD | 21,530.00 USD | 0.00 USD |
| `1D` | `0.3639` | 14,930,000.00 USD | 14,930,000.00 USD | 0.00 USD | 183,690.00 USD | 152,650.00 USD | 76,240.00 USD |
| `1D` | `0.3643` | 15,210,000.00 USD | 15,210,000.00 USD | 0.00 USD | 167,490.00 USD | 81,220.00 USD | 35,280.00 USD |
| `7D` | `0.3643` | 12,180,000.00 USD | 12,180,000.00 USD | 0.00 USD | 4,830.00 USD | 0.00 USD | 789,140.00 USD |
| `1D` | `0.3647` | 15,620,000.00 USD | 15,620,000.00 USD | 0.00 USD | 268,930.00 USD | 27,770.00 USD | 110,900.00 USD |
| `7D` | `0.3649` | 12,350,000.00 USD | 12,350,000.00 USD | 0.00 USD | 177,470.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3651` | 15,800,000.00 USD | 15,800,000.00 USD | 0.00 USD | 2,860.00 USD | 55,980.00 USD | 123,070.00 USD |
| `1D` | `0.3655` | 16,550,000.00 USD | 16,550,000.00 USD | 0.00 USD | 411,730.00 USD | 107,280.00 USD | 227,180.00 USD |
| `7D` | `0.3655` | 13,140,000.00 USD | 13,140,000.00 USD | 0.00 USD | 677,860.00 USD | 112,770.00 USD | 0.00 USD |
| `1D` | `0.3659` | 17,010,000.00 USD | 17,010,000.00 USD | 0.00 USD | 233,580.00 USD | 113,780.00 USD | 113,740.00 USD |
| `7D` | `0.3661` | 14,130,000.00 USD | 14,130,000.00 USD | 0.00 USD | 685,520.00 USD | 60,550.00 USD | 238,480.00 USD |
| `1D` | `0.3663` | 17,620,000.00 USD | 17,620,000.00 USD | 0.00 USD | 449,010.00 USD | 99,370.00 USD | 62,910.00 USD |
| `1D` | `0.3667` | 18,010,000.00 USD | 18,010,000.00 USD | 0.00 USD | 187,870.00 USD | 62,870.00 USD | 137,570.00 USD |
| `7D` | `0.3667` | 14,700,000.00 USD | 14,700,000.00 USD | 0.00 USD | 422,610.00 USD | 15,390.00 USD | 135,630.00 USD |
| `1D` | `0.3671` | 18,510,000.00 USD | 18,510,000.00 USD | 0.00 USD | 94,630.00 USD | 79,940.00 USD | 324,560.00 USD |
| `7D` | `0.3673` | 15,390,000.00 USD | 15,390,000.00 USD | 0.00 USD | 512,420.00 USD | 53,040.00 USD | 122,410.00 USD |
| `1D` | `0.3675` | 18,740,000.00 USD | 18,740,000.00 USD | 0.00 USD | 54,730.00 USD | 53,460.00 USD | 126,530.00 USD |
| `1D` | `0.3679` | 19,630,000.00 USD | 19,630,000.00 USD | 0.00 USD | 772,390.00 USD | 25,610.00 USD | 92,020.00 USD |
| `7D` | `0.3679` | 15,650,000.00 USD | 15,650,000.00 USD | 0.00 USD | 259,160.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3683` | 19,900,000.00 USD | 19,900,000.00 USD | 0.00 USD | 18,610.00 USD | 84,920.00 USD | 161,850.00 USD |
| `7D` | `0.3685` | 15,830,000.00 USD | 15,830,000.00 USD | 0.00 USD | 4,100.00 USD | 102,650.00 USD | 72,350.00 USD |
| `1D` | `0.3687` | 20,560,000.00 USD | 20,560,000.00 USD | 0.00 USD | 440,130.00 USD | 153,070.00 USD | 68,010.00 USD |
| `1D` | `0.3691` | 20,990,000.00 USD | 20,990,000.00 USD | 0.00 USD | 363,130.00 USD | 49,680.00 USD | 23,760.00 USD |
| `7D` | `0.3691` | 16,240,000.00 USD | 16,240,000.00 USD | 0.00 USD | 147,650.00 USD | 261,530.00 USD | 0.00 USD |
| `1D` | `0.3695` | 21,240,000.00 USD | 21,240,000.00 USD | 0.00 USD | 162,690.00 USD | 88,200.00 USD | 0.00 USD |
| `7D` | `0.3697` | 16,400,000.00 USD | 16,400,000.00 USD | 0.00 USD | 0.00 USD | 163,180.00 USD | 0.00 USD |
| `1D` | `0.3699` | 21,780,000.00 USD | 21,780,000.00 USD | 0.00 USD | 487,980.00 USD | 15,920.00 USD | 27,870.00 USD |
| `1D` | `0.3703` | 22,310,000.00 USD | 22,310,000.00 USD | 0.00 USD | 287,950.00 USD | 180,250.00 USD | 63,170.00 USD |
| `7D` | `0.3703` | 16,450,000.00 USD | 16,450,000.00 USD | 0.00 USD | 50,940.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3707` | 22,850,000.00 USD | 22,850,000.00 USD | 0.00 USD | 1,640.00 USD | 29,660.00 USD | 510,340.00 USD |
| `1D` | `0.3709` | 22,960,000.00 USD | 22,960,000.00 USD | 0.00 USD | 109,050.00 USD | 3,230.00 USD | 0.00 USD |
| `7D` | `0.3709` | 16,450,000.00 USD | 16,450,000.00 USD | 0.00 USD | 1,540.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3715` | 16,850,000.00 USD | 16,850,000.00 USD | 0.00 USD | 4,580.00 USD | 0.00 USD | 394,570.00 USD |
| `7D` | `0.3721` | 17,600,000.00 USD | 17,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 747,740.00 USD |
| `7D` | `0.3727` | 17,880,000.00 USD | 17,880,000.00 USD | 0.00 USD | 212,850.00 USD | 0.00 USD | 66,870.00 USD |
| `7D` | `0.3733` | 18,070,000.00 USD | 18,070,000.00 USD | 0.00 USD | 188,670.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3739` | 18,540,000.00 USD | 18,540,000.00 USD | 0.00 USD | 242,460.00 USD | 7,690.00 USD | 218,010.00 USD |
| `7D` | `0.3745` | 18,940,000.00 USD | 18,940,000.00 USD | 0.00 USD | 248,660.00 USD | 115,430.00 USD | 37,210.00 USD |
| `7D` | `0.3751` | 18,940,000.00 USD | 18,940,000.00 USD | 0.00 USD | 5,330.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3757` | 19,250,000.00 USD | 19,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 302,240.00 USD |
| `7D` | `0.3763` | 19,420,000.00 USD | 19,420,000.00 USD | 0.00 USD | 35,610.00 USD | 92,380.00 USD | 50,200.00 USD |
| `7D` | `0.3769` | 19,430,000.00 USD | 19,430,000.00 USD | 0.00 USD | 1,150.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3781` | 19,450,000.00 USD | 19,450,000.00 USD | 0.00 USD | 23,800.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3787` | 19,600,000.00 USD | 19,600,000.00 USD | 0.00 USD | 90,150.00 USD | 3,620.00 USD | 54,360.00 USD |
| `7D` | `0.3793` | 20,060,000.00 USD | 20,060,000.00 USD | 0.00 USD | 27,760.00 USD | 0.00 USD | 437,170.00 USD |
| `7D` | `0.3811` | 20,100,000.00 USD | 20,100,000.00 USD | 0.00 USD | 4,000.00 USD | 0.00 USD | 37,490.00 USD |
| `7D` | `0.3817` | 20,280,000.00 USD | 20,280,000.00 USD | 0.00 USD | 156,690.00 USD | 19,620.00 USD | 0.00 USD |
| `7D` | `0.3823` | 20,390,000.00 USD | 20,390,000.00 USD | 0.00 USD | 0.00 USD | 54,460.00 USD | 57,690.00 USD |
| `7D` | `0.3853` | 20,390,000.00 USD | 20,390,000.00 USD | 0.00 USD | 535.97 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3859` | 20,460,000.00 USD | 20,460,000.00 USD | 0.00 USD | 70,850.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3865` | 20,620,000.00 USD | 20,620,000.00 USD | 0.00 USD | 112,700.00 USD | 45,110.00 USD | 0.00 USD |
| `7D` | `0.3877` | 20,750,000.00 USD | 20,750,000.00 USD | 0.00 USD | 123,270.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3883` | 20,790,000.00 USD | 20,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 48,960.00 USD |
| `7D` | `0.3889` | 20,900,000.00 USD | 20,900,000.00 USD | 0.00 USD | 103,790.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3895` | 20,940,000.00 USD | 20,940,000.00 USD | 0.00 USD | 0.00 USD | 41,060.00 USD | 0.00 USD |
| `7D` | `0.3901` | 21,000,000.00 USD | 21,000,000.00 USD | 0.00 USD | 59,060.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3907` | 21,110,000.00 USD | 21,110,000.00 USD | 0.00 USD | 0.00 USD | 50,210.00 USD | 63,420.00 USD |
| `7D` | `0.3925` | 21,270,000.00 USD | 21,270,000.00 USD | 0.00 USD | 342.70 USD | 1,190.00 USD | 157,830.00 USD |
| `7D` | `0.3931` | 21,300,000.00 USD | 21,300,000.00 USD | 0.00 USD | 27,520.00 USD | 2,840.00 USD | 2,800.00 USD |
| `7D` | `0.3937` | 21,330,000.00 USD | 21,330,000.00 USD | 0.00 USD | 21,970.00 USD | 1,070.00 USD | 5,410.00 USD |
| `7D` | `0.3943` | 21,360,000.00 USD | 21,360,000.00 USD | 0.00 USD | 24,790.00 USD | 3,090.00 USD | 784.19 USD |
| `7D` | `0.3949` | 21,500,000.00 USD | 21,500,000.00 USD | 0.00 USD | 109,810.00 USD | 8,290.00 USD | 18,490.00 USD |
| `7D` | `0.3955` | 21,730,000.00 USD | 21,730,000.00 USD | 0.00 USD | 107,070.00 USD | 10,160.00 USD | 110,780.00 USD |
| `7D` | `0.3961` | 21,910,000.00 USD | 21,910,000.00 USD | 0.00 USD | 122,550.00 USD | 54,030.00 USD | 7,040.00 USD |
| `7D` | `0.3967` | 21,930,000.00 USD | 21,930,000.00 USD | 0.00 USD | 12,300.00 USD | 6,010.00 USD | 4,840.00 USD |
| `7D` | `0.3973` | 22,070,000.00 USD | 22,070,000.00 USD | 0.00 USD | 16,660.00 USD | 1,440.00 USD | 123,860.00 USD |
| `7D` | `0.3979` | 22,180,000.00 USD | 22,180,000.00 USD | 0.00 USD | 57,690.00 USD | 38,460.00 USD | 11,500.00 USD |
| `7D` | `0.3985` | 22,220,000.00 USD | 22,220,000.00 USD | 0.00 USD | 23,360.00 USD | 3,160.00 USD | 10,200.00 USD |
| `7D` | `0.3991` | 22,260,000.00 USD | 22,260,000.00 USD | 0.00 USD | 0.00 USD | 16,880.00 USD | 24,490.00 USD |
| `7D` | `0.3997` | 22,270,000.00 USD | 22,270,000.00 USD | 0.00 USD | 0.00 USD | 8,610.00 USD | 0.00 USD |
| `7D` | `0.4001` | 22,280,000.00 USD | 22,280,000.00 USD | 0.00 USD | 0.00 USD | 7,690.00 USD | 0.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `421.75M` | Total OI Tokens: `1,258,093,983.2 TRX`
  * 1h OI Change: `+2.73%` | 4h OI Change: `+3.38%` | 24h OI Change: `+47.39%`
  * Exchange Breakdown: Binance=`106.56M` | Bybit=`83.67M` | OKX=`27.26M` | Hyperliquid=`18.84M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `-19.97K` | Last 24h: `-632.70K` | Last 3d: `-621.37K` | Last 7d: `-893.87K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `-0.0391%` | **USDT OKX** | `-0.3438%` |
| **USDT Bybit** | `0.1034%` | **USDT KuCoin** | `-0.0672%` |
| **USDT MEXC** | `-0.0375%` | **USDT BingX** | `0.1060%` |
| **USDT Gate** | `-0.1490%` | **USDT Bitget** | `-0.2051%` |
| **CoinM Binance** | `-0.0898%` | **CoinM OKX** | `-` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `TRX` | `37.63%` | `62.37%` | `0.60` | 24,870,000.00 USD |
| `15M` | `Binance` | `42.72%` | `57.28%` | `0.75` | 7,210,000.00 USD |
| `15M` | `OKX` | `33.24%` | `66.76%` | `0.50` | 2,100,000.00 USD |
| `15M` | `Bybit` | `23.19%` | `76.81%` | `0.30` | 3,290,000.00 USD |
| `15M` | `KuCoin` | `34.58%` | `65.42%` | `0.53` | 580,860.00 USD |
| `15M` | `Gate` | `48.17%` | `51.83%` | `0.93` | 1,360,000.00 USD |
| `15M` | `Bitget` | `51.08%` | `48.92%` | `1.04` | 1,540,000.00 USD |
| `15M` | `BingX` | `14.88%` | `85.12%` | `0.17` | 727,920.00 USD |
| `15M` | `MEXC` | `49.65%` | `50.35%` | `0.99` | 4,600,000.00 USD |
| `15M` | `Bitunix` | `29.81%` | `70.19%` | `0.42` | 594,830.00 USD |
| `15M` | `Hyperliquid` | `42.68%` | `57.32%` | `0.74` | 948,690.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `44.35%` | `55.65%` | `0.80` | 59,960.00 USD |
| `15M` | `Crypto.com` | `62.62%` | `37.38%` | `1.68` | 43,770.00 USD |
| `15M` | `WhiteBIT` | `0.28%` | `99.72%` | `0.00` | 1,420,000.00 USD |
| `15M` | `HTX` | `38.49%` | `61.51%` | `0.63` | 9,330.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `30.82%` | `69.18%` | `0.45` | 240,880.00 USD |
| `15M` | `Aster` | `47.38%` | `52.62%` | `0.90` | 97,590.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `40.87%` | `59.13%` | `0.69` | 58,000.00 USD |
| `15M` | `Whale Positions` | `42.72%` | `57.28%` | `0.75` | 7,210,000.00 USD |
| `15M` | `Global Accounts` | `37.63%` | `62.37%` | `0.60` | 24,870,000.00 USD |
| `1H` | `TRX` | `47.08%` | `52.92%` | `0.89` | 16,320,000.00 USD |
| `1H` | `Binance` | `47.14%` | `52.86%` | `0.89` | 4,840,000.00 USD |
| `1H` | `OKX` | `55.07%` | `44.93%` | `1.23` | 1,530,000.00 USD |
| `1H` | `Bybit` | `50.74%` | `49.26%` | `1.03` | 1,430,000.00 USD |
| `1H` | `KuCoin` | `46.63%` | `53.37%` | `0.87` | 155,160.00 USD |
| `1H` | `Gate` | `52.4%` | `47.6%` | `1.10` | 691,440.00 USD |
| `1H` | `Bitget` | `41.06%` | `58.94%` | `0.70` | 411,140.00 USD |
| `1H` | `BingX` | `55.84%` | `44.16%` | `1.26` | 1,420,000.00 USD |
| `1H` | `MEXC` | `43.98%` | `56.02%` | `0.79` | 1,600,000.00 USD |
| `1H` | `Bitunix` | `60.15%` | `39.85%` | `1.51` | 248,220.00 USD |
| `1H` | `Hyperliquid` | `33%` | `67%` | `0.49` | 214,930.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `51.01%` | `48.99%` | `1.04` | 2,390,000.00 USD |
| `1H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `WhiteBIT` | `8.87%` | `91.13%` | `0.10` | 1,090,000.00 USD |
| `1H` | `HTX` | `49.14%` | `50.86%` | `0.97` | 52,140.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `66.2%` | `33.8%` | `1.96` | 188,510.00 USD |
| `1H` | `Aster` | `55.29%` | `44.71%` | `1.24` | 2,060.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `85.98%` | `14.02%` | `6.13` | 52,640.00 USD |
| `1H` | `Whale Positions` | `47.14%` | `52.86%` | `0.89` | 4,840,000.00 USD |
| `1H` | `Global Accounts` | `47.08%` | `52.92%` | `0.89` | 16,320,000.00 USD |
| `4H` | `TRX` | `46.33%` | `53.67%` | `0.86` | 71,350,000.00 USD |
| `4H` | `Binance` | `50.74%` | `49.26%` | `1.03` | 22,310,000.00 USD |
| `4H` | `OKX` | `52.96%` | `47.04%` | `1.13` | 5,820,000.00 USD |
| `4H` | `Bybit` | `52.28%` | `47.72%` | `1.10` | 5,410,000.00 USD |
| `4H` | `KuCoin` | `46.94%` | `53.06%` | `0.88` | 996,720.00 USD |
| `4H` | `Gate` | `54.62%` | `45.38%` | `1.20` | 2,190,000.00 USD |
| `4H` | `Bitget` | `43.89%` | `56.11%` | `0.78` | 2,160,000.00 USD |
| `4H` | `BingX` | `34.2%` | `65.8%` | `0.52` | 9,120,000.00 USD |
| `4H` | `MEXC` | `45.82%` | `54.18%` | `0.85` | 6,420,000.00 USD |
| `4H` | `Bitunix` | `49.1%` | `50.9%` | `0.96` | 1,710,000.00 USD |
| `4H` | `Hyperliquid` | `35.06%` | `64.94%` | `0.54` | 845,880.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `50.88%` | `49.12%` | `1.04` | 10,610,000.00 USD |
| `4H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `WhiteBIT` | `4.5%` | `95.5%` | `0.05` | 2,930,000.00 USD |
| `4H` | `HTX` | `57.01%` | `42.99%` | `1.33` | 307,780.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `57.71%` | `42.29%` | `1.36` | 445,740.00 USD |
| `4H` | `Aster` | `29.43%` | `70.57%` | `0.42` | 29,500.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `83.71%` | `16.29%` | `5.14` | 70,740.00 USD |
| `4H` | `Whale Positions` | `50.74%` | `49.26%` | `1.03` | 22,310,000.00 USD |
| `4H` | `Global Accounts` | `46.33%` | `53.67%` | `0.86` | 71,350,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5:00 UTC` | `0.3370` | `0.3359` | `0.3370` | `0.3378` | `0.3316` | 5,309,391.96 USD | 3,078,017.12 USD | 2,231,374.84 USD | 846,642.29 USD | `+15.95%` | `35B / 9S` |
| `0:00 UTC` | `0.3368` | `0.3360` | `0.3368` | `0.3377` | `0.3336` | 2,717,916.28 USD | 1,271,599.87 USD | 1,446,316.41 USD | -174,716.54 USD | `-6.43%` | `5B / 15S` |
| `5:00 UTC` | `0.3312` | `0.3323` | `0.3312` | `0.3350` | `0.3309` | 3,615,541.77 USD | 1,824,507.31 USD | 1,791,034.46 USD | 33,472.85 USD | `+0.93%` | `10B / 13S` |
| `0:00 UTC` | `0.3320` | `0.3319` | `0.3320` | `0.3329` | `0.3307` | 3,613,244.76 USD | 2,074,143.60 USD | 1,539,101.16 USD | 535,042.44 USD | `+14.81%` | `13B / 9S` |
| `5:00 UTC` | `0.3320` | `0.3320` | `0.3320` | `0.3328` | `0.3316` | 3,173,620.42 USD | 1,545,938.41 USD | 1,627,682.01 USD | -81,743.60 USD | `-2.58%` | `29B / 18S` |
| `0:00 UTC` | `0.3323` | `0.3323` | `0.3323` | `0.3332` | `0.3318` | 1,965,395.58 USD | 930,788.45 USD | 1,034,607.13 USD | -103,818.67 USD | `-5.28%` | `16B / 20S` |
| `5:00 UTC` | `0.3320` | `0.3322` | `0.3320` | `0.3328` | `0.3319` | 2,011,353.25 USD | 833,950.97 USD | 1,177,402.29 USD | -343,451.32 USD | `-17.08%` | `9B / 10S` |
| `0:00 UTC` | `0.3339` | `0.3340` | `0.3339` | `0.3367` | `0.3319` | 3,824,828.40 USD | 1,984,762.45 USD | 1,840,065.95 USD | 144,696.50 USD | `+3.78%` | `20B / 6S` |
| `5:00 UTC` | `0.3351` | `0.3349` | `0.3351` | `0.3364` | `0.3341` | 1,965,380.04 USD | 899,735.78 USD | 1,065,644.26 USD | -165,908.48 USD | `-8.44%` | `11B / 14S` |
| `0:00 UTC` | `0.3347` | `0.3348` | `0.3347` | `0.3359` | `0.3335` | 994,672.60 USD | 513,864.23 USD | 480,808.37 USD | 33,055.85 USD | `+3.32%` | `26B / 28S` |

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
| `5m` | -140,600.00 USD | -177,590.00 USD | **`DISTRIBUTION`** |
| `15m` | -494,840.00 USD | 23,740.00 USD | **`DISTRIBUTION`** |
| `30m` | -2,140,000.00 USD | 325,160.00 USD | **`DISTRIBUTION`** |
| `1h` | -1,760,000.00 USD | 654,410.00 USD | **`DISTRIBUTION`** |
| `2h` | 469,930.00 USD | 1,590,000.00 USD | **`ACCUMULATION`** |
| `4h` | 3,200,000.00 USD | 2,450,000.00 USD | **`ACCUMULATION`** |
| `6h` | 7,980,000.00 USD | -6,320,000.00 USD | **`ACCUMULATION`** |
| `8h` | 13,600,000.00 USD | -5,310,000.00 USD | **`ACCUMULATION`** |
| `12h` | 24,490,000.00 USD | -1,920,000.00 USD | **`ACCUMULATION`** |
| `24h` | 19,920,000.00 USD | 5,630,000.00 USD | **`ACCUMULATION`** |
| `1w` | 13,620,000.00 USD | 4,330,000.00 USD | **`ACCUMULATION`** |
| `30d` | -10,220,000.00 USD | 5,260,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-140.60K` | 15m=`-494.84K` | 1h=`-1.76M` | 24h=`+19.92M`
* Futures Capital Netflows: 5m=`-177.59K` | 15m=`+23.74K` | 1h=`+654.41K` | 24h=`+5.63M`
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
  * `2026-10-30 15:33:00 IST`: [ec.europa.eu] - (Sentiment: `Neutral`)
  * `2026-10-30 15:32:00 IST`: [ec.europa.eu] - (Sentiment: `Neutral`)
  * `2026-10-30 15:19:00 IST`: [dailyforex.com] - (Sentiment: `Neutral`)
  * `2026-10-30 15:12:00 IST`: [breakingthenews.net] - (Sentiment: `Neutral`)
  * `2026-10-30 14:41:00 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 14:38:00 IST`: [@FirstSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 15:36:00 IST`: [destatis.de] - (Sentiment: `Neutral`)
  * `2026-10-30 15:36:00 IST`: [istat.it] - (Sentiment: `Neutral`)
  * `2026-10-30 15:36:00 IST`: [channelnewsasia.com] - (Sentiment: `Neutral`)
  * `2026-10-30 15:36:00 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 15:36:00 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 15:35:00 IST`: [kof.ethz.ch] - (Sentiment: `Neutral`)
  * `2026-10-30 15:35:00 IST`: [gerlachmacro.substack.com] - (Sentiment: `Neutral`)
  * `2026-10-30 15:35:00 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-30 15:35:00 IST`: [insee.fr] - (Sentiment: `Neutral`)


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
  * Execution Entry: `0.3404` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `0.3321` (Risk Distance: `0.0083` pts)
  * +2.5R Take Profit: `0.3611`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `0.3578` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `0.3661` (Risk Distance: `0.0083` pts)
  * +2.5R Take Profit: `0.3371`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`0.3377`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
