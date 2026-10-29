# 🏛️ SOVEREIGN CANDIDATE DOSSIER: TRX
**Canonical Key**: `TRX` | **Broker Instrument**: `TRXUSD.p` | **Asset Class**: `Crypto Alt L1`
**Timestamp**: `2026-10-29 23:40:50 IST` (`2026-10-29 18:10:50 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `0.3305` | **Live Ask Quote**: `0.3317` | **Mid Price**: `0.3311`
- **Spread Points**: `12.00` | **Spread BPS**: `36.24 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `0.3302` | VWAP Z-Score: `+0.63` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `0.000362` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `50.41` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `0.3325` | Lower -3.00σ Band: `0.3279`
  * Upper +2.51σ Band: `0.3321` | Lower -2.51σ Band: `0.3283`
  * Upper +2.01σ Band: `0.3318` | Lower -2.01σ Band: `0.3287`
  * Upper +2.00σ Band: `0.3318` | Lower -2.00σ Band: `0.3287`
  * Upper +1.28σ Band: `0.3312` | Lower -1.28σ Band: `0.3292`
  * Upper +1.00σ Band: `0.3310` | Lower -1.00σ Band: `0.3294`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`0.3306` | EMA-20=`0.3307` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`0.3306` (Slope: `+0.0000`) | EMA-100=`0.3304`
  * Institutional Anchors: EMA-144=`0.3302` | EMA-200=`0.3299` (Slope: `+0.0270`) | EMA-233=`0.3299`
- **Range Boundaries**: 24H High=`0.3313` | 24H Low=`0.3285` | Weekly High=`0.3319` | Weekly Low=`0.3266`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `0.3312` (Distance: `-0.05%`)
  * Point of Control (POC) = `0.3307` (Distance: `+0.11%`)
  * Value Area Low (VAL) = `0.3293` (Distance: `+0.52%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BULLISH (Above Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`0.3314` | POC=`0.3309` | VAL=`0.3304`
  * Prior Day Extremes: PDH=`0.3319` | PDL=`0.3288` | PDC=`0.3289`
  * Monday Range Blueprint: High=`0.3310` | Mid=`0.3300` | Low=`0.3289`
  * Developing Weekly Value Area: Weekly VAH=`0.3312` | Weekly POC=`0.3307` | Weekly VAL=`0.3290`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`0.3306` | Low=`0.3285`
  * London Session (08:00-16:00 UTC): High=`0.3311` | Low=`0.3303`
  * New York Session (13:00-21:00 UTC): High=`0.3313` | Low=`0.3301`
  * Initial Balance (First Hour): IB High=`0.3311` | IB Low=`0.3303`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `0.3298` - `0.3324`
  * Optimal Trade Entry (OTE 0.705): `0.3318`
  * Structural Invalidation Anchor (0.786): `0.3337`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `0.3312` | `0.3312` | `0.3312` | `0.3312` | `174,647` | 57,843.00 USD | 35,448.53 USD | `+61.28%` | 1,915,890.36 USD | `+1.26` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `5m` | `0.3312` | `0.3312` | `0.3311` | `0.3311` | `182,534` | 60,455.50 USD | -44,523.19 USD | `-73.65%` | 1,871,367.16 USD | `-0.89` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `5m` | `0.3311` | `0.3312` | `0.3311` | `0.3311` | `6,903` | 2,285.93 USD | -1,740.25 USD | `-76.13%` | 1,869,626.92 USD | `+0.25` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `0.3311` | `0.3313` | `0.3311` | `0.3313` | `980,387` | 324,753.86 USD | 49,516.62 USD | `+15.25%` | 1,858,340.53 USD | `+0.32` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `0.3313` | `0.3313` | `0.3311` | `0.3312` | `777,819` | 257,613.17 USD | 1,993.62 USD | `+0.77%` | 1,860,334.15 USD | `-0.04` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `15m` | `0.3312` | `0.3312` | `0.3311` | `0.3311` | `189,180` | 62,656.34 USD | -46,178.34 USD | `-73.70%` | 1,814,155.80 USD | `-0.39` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `1h` | `0.3314` | `0.3316` | `0.3311` | `0.3311` | `3,106,966` | 1,029,390.94 USD | -31,067.74 USD | `-3.02%` | 2,031,724.83 USD | `-0.64` | **`BEARISH`** | `NEUTRAL CHOP` |
| `1h` | `0.3311` | `0.3313` | `0.3310` | `0.3312` | `3,301,362` | 1,093,342.85 USD | -39,208.85 USD | `-3.59%` | 1,992,515.98 USD | `-0.63` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `1h` | `0.3312` | `0.3312` | `0.3311` | `0.3311` | `189,148` | 62,645.74 USD | -46,167.75 USD | `-73.70%` | 1,946,348.23 USD | `-0.59` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `0.3311` | `0.3316` | `0.3311` | `0.3315` | `11,939,433` | 3,956,492.73 USD | 16,254.19 USD | `+0.41%` | 2,010,591.01 USD | `-1.70` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `0.3315` | `0.3318` | `0.3306` | `0.3314` | `23,511,075` | 7,789,850.35 USD | 369,308.17 USD | `+4.74%` | 2,379,899.18 USD | `-0.41` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `0.3314` | `0.3316` | `0.3310` | `0.3311` | `6,597,508` | 2,185,390.12 USD | -116,454.94 USD | `-5.33%` | 2,263,444.25 USD | `-1.52` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.3296` | `0.3308` | `0.3290` | `0.3307` | `23,140,787` | 7,631,473.08 USD | 600,887.06 USD | `+7.87%` | 1,347,651.40 USD | `-1.00` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `0.3307` | `0.3316` | `0.3306` | `0.3311` | `18,393,472` | 6,092,518.66 USD | 646,685.42 USD | `+10.61%` | 1,994,336.82 USD | `-0.30` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `0.3311` | `0.3316` | `0.3311` | `0.3315` | `11,939,433` | 3,956,492.73 USD | 16,254.19 USD | `+0.41%` | 2,010,591.01 USD | `-1.70` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `0.3315` | `0.3318` | `0.3306` | `0.3314` | `23,511,075` | 7,789,850.35 USD | 369,308.17 USD | `+4.74%` | 2,379,899.18 USD | `-0.41` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `0.3314` | `0.3316` | `0.3310` | `0.3311` | `6,597,508` | 2,185,390.12 USD | -116,454.94 USD | `-5.33%` | 2,263,444.25 USD | `-1.52` | **`BEARISH`** | `DELTA ALIGNED` |

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
| --- | **`0.3311`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `MID` | Regular L2 Book | - | - | - | Interbank L2 | 0.00% | Interbank |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-29 23:36:01 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `1648` | `0xeadc...9d55` | `LONG` | 1,325,200.00 USD | `4,000,000.00` | `0.3421` | `0.3313` | `0.000000` | -43,278.09 USD | `-3.27%` | `10X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `0.3315` | 8,100.46 USD | `-` | `NEWS_INTEL` | `-` | #TRX Whale SELL: 8.10K USD at 0.3315 USD [API] | `2026-10-27 21:38:06` |
| `ANNOUNCEMENT` | `INFO` | `0.3312` | 6,465.75 USD | `-` | `NEWS_INTEL` | `-` | #TRX Whale SELL: 6.47K USD at 0.3312 USD [API] | `2026-10-27 22:40:07` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`0.3380` (Vol: 384,800.00 USD, Dist: `+2.11%`) | Long MP=`0.3248` (Vol: 434,200.00 USD, Dist: `--1.88%`)
  * 48H Horizon: Short MP=`0.3381` (Vol: 549,300.00 USD, Dist: `+2.13%`) | Long MP=`0.3248` (Vol: 637,300.00 USD, Dist: `--1.88%`)
  * 3D Horizon: Short MP=`0.3383` (Vol: 512,000.00 USD, Dist: `+2.19%`) | Long MP=`0.3250` (Vol: 602,700.00 USD, Dist: `--1.83%`)
  * 7D Horizon: Short MP=`0.3381` (Vol: 606,000.00 USD, Dist: `+2.11%`) | Long MP=`0.3250` (Vol: 663,500.00 USD, Dist: `--1.83%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long Liquidation` | `0.0685` | 8,780.00 USD | 503,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0705` | 482.64 USD | 494,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0825` | 1,050.00 USD | 494,030.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1035` | 4,090.00 USD | 492,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1075` | 23,520.00 USD | 488,880.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1095` | 4,580.00 USD | 465,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1115` | 531.74 USD | 460,780.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1155` | 881.38 USD | 460,250.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1175` | 394.80 USD | 459,370.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1325` | 119.78 USD | 458,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1345` | 1,530.00 USD | 458,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1405` | 429.65 USD | 457,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1535` | 463.72 USD | 456,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1575` | 394.06 USD | 456,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1595` | 390.46 USD | 456,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1695` | 13,020.00 USD | 455,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1705` | 20,360.00 USD | 442,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1715` | 3,430.00 USD | 422,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1735` | 11,160.00 USD | 418,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1745` | 471.50 USD | 407,680.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1755` | 2,390.00 USD | 407,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1765` | 4,200.00 USD | 404,820.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1775` | 433.81 USD | 400,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1795` | 209.84 USD | 400,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1895` | 1,350.00 USD | 399,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1965` | 3,560.00 USD | 398,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2045` | 6,130.00 USD | 395,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2145` | 3,330.00 USD | 388,940.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2175` | 1,520.00 USD | 385,610.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2195` | 515.17 USD | 384,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2225` | 272.79 USD | 383,570.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2255` | 4,590.00 USD | 383,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2265` | 2,390.00 USD | 378,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2275` | 266.63 USD | 376,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2305` | 4,180.00 USD | 376,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2315` | 2,730.00 USD | 371,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2325` | 308.30 USD | 369,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2335` | 2,690.00 USD | 368,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2345` | 1,060.00 USD | 366,140.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2355` | 6,140.00 USD | 365,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2365` | 344.11 USD | 358,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2385` | 1,260.00 USD | 358,590.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2405` | 181.58 USD | 357,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2445` | 889.49 USD | 357,140.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2455` | 466.70 USD | 356,250.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2465` | 276.57 USD | 355,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2475` | 2,420.00 USD | 355,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2565` | 1,230.00 USD | 353,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2585` | 1,580.00 USD | 351,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2595` | 23,040.00 USD | 350,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2605` | 8,940.00 USD | 327,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2615` | 466.78 USD | 318,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2635` | 108.56 USD | 317,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2655` | 7,520.00 USD | 317,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2665` | 450.92 USD | 310,200.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2675` | 194.47 USD | 309,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2685` | 322.74 USD | 309,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2725` | 412.84 USD | 309,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2735` | 5,500.00 USD | 308,820.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2745` | 40,290.00 USD | 303,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2755` | 84,780.00 USD | 263,020.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2775` | 487.29 USD | 178,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2785` | 2,130.00 USD | 177,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2795` | 14,450.00 USD | 175,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2805` | 6,280.00 USD | 161,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2815` | 1,310.00 USD | 154,910.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2825` | 16,640.00 USD | 153,600.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2835` | 1,430.00 USD | 136,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2865` | 360.42 USD | 135,540.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2915` | 591.45 USD | 135,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2925` | 957.64 USD | 134,580.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2945` | 3,760.00 USD | 133,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2955` | 125.29 USD | 129,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.2979` | 12,850,000.00 USD | 12,850,000.00 USD | 69,830.00 USD | 8,600.00 USD | 10,570.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.2983` | 2,960,000.00 USD | 2,960,000.00 USD | 80,870.00 USD | 15,850.00 USD | 27,140.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.2983` | 12,760,000.00 USD | 12,760,000.00 USD | 117,250.00 USD | 9,990.00 USD | 36,400.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.2987` | 2,840,000.00 USD | 2,840,000.00 USD | 44,390.00 USD | 4,220.00 USD | 2,890.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.2987` | 12,600,000.00 USD | 12,600,000.00 USD | 83,850.00 USD | 9,860.00 USD | 6,170.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.2991` | 12,500,000.00 USD | 12,500,000.00 USD | 23,720.00 USD | 6,910.00 USD | 3,870.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.2995` | 127.89 USD | 129,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3005` | 7,130.00 USD | 129,610.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3015` | 10,330.00 USD | 122,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3025` | 694.54 USD | 112,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3035` | 942.06 USD | 111,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3045` | 5,290.00 USD | 110,520.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.3051` | 12,460,000.00 USD | 12,460,000.00 USD | 380.73 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3055` | 12,460,000.00 USD | 12,460,000.00 USD | 1,380.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3055` | 5,300.00 USD | 105,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.3063` | 12,460,000.00 USD | 12,460,000.00 USD | 1,990.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3065` | 14,720.00 USD | 99,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3067` | 2,780,000.00 USD | 2,780,000.00 USD | 57.95 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3067` | 12,460,000.00 USD | 12,460,000.00 USD | 5,660.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3071` | 2,780,000.00 USD | 2,780,000.00 USD | 2,980.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3071` | 12,450,000.00 USD | 12,450,000.00 USD | 6,280.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3075` | 2,780,000.00 USD | 2,780,000.00 USD | 1,410.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3075` | 12,450,000.00 USD | 12,450,000.00 USD | 2,850.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3079` | 2,780,000.00 USD | 2,780,000.00 USD | 135.83 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3079` | 12,450,000.00 USD | 12,450,000.00 USD | 2,180.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3083` | 2,780,000.00 USD | 2,780,000.00 USD | 221.36 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3083` | 12,440,000.00 USD | 12,440,000.00 USD | 1,680.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3085` | 6,670.00 USD | 85,200.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3087` | 2,780,000.00 USD | 2,780,000.00 USD | 506.09 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3087` | 12,440,000.00 USD | 12,440,000.00 USD | 2,200.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3091` | 2,780,000.00 USD | 2,780,000.00 USD | 61.02 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3091` | 12,440,000.00 USD | 12,440,000.00 USD | 1,320.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3107` | 12,440,000.00 USD | 12,440,000.00 USD | 1,790.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3111` | 12,440,000.00 USD | 12,440,000.00 USD | 554.30 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3115` | 824.85 USD | 78,540.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.3119` | 12,440,000.00 USD | 12,440,000.00 USD | 2,650.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3123` | 2,780,000.00 USD | 2,780,000.00 USD | 77.30 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3123` | 12,430,000.00 USD | 12,430,000.00 USD | 7,550.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3125` | 17,140.00 USD | 77,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3127` | 2,780,000.00 USD | 2,780,000.00 USD | 3,970.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3127` | 12,430,000.00 USD | 12,430,000.00 USD | 8,380.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3131` | 2,780,000.00 USD | 2,780,000.00 USD | 1,880.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3131` | 12,420,000.00 USD | 12,420,000.00 USD | 3,800.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3135` | 2,770,000.00 USD | 2,770,000.00 USD | 181.20 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3135` | 12,410,000.00 USD | 12,410,000.00 USD | 2,910.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3135` | 44,390.00 USD | 60,570.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3139` | 2,770,000.00 USD | 2,770,000.00 USD | 295.30 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3139` | 12,410,000.00 USD | 12,410,000.00 USD | 2,250.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3143` | 2,770,000.00 USD | 2,770,000.00 USD | 429.90 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3143` | 12,410,000.00 USD | 12,410,000.00 USD | 184,260.00 USD | 34,890.00 USD | 11,170.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3145` | 2,140.00 USD | 16,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3147` | 2,770,000.00 USD | 2,770,000.00 USD | 326.60 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3147` | 12,180,000.00 USD | 12,180,000.00 USD | 101,370.00 USD | 16,380.00 USD | 10,680.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3151` | 12,050,000.00 USD | 12,050,000.00 USD | 142,080.00 USD | 23,130.00 USD | 45,340.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3155` | 11,840,000.00 USD | 11,840,000.00 USD | 157,220.00 USD | 37,570.00 USD | 20,330.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3155` | 142.29 USD | 14,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3159` | 2,770,000.00 USD | 2,770,000.00 USD | 5,750.00 USD | 5,600.00 USD | 27,350.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3159` | 11,620,000.00 USD | 11,620,000.00 USD | 353,770.00 USD | 101,710.00 USD | 112,500.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3163` | 2,730,000.00 USD | 2,730,000.00 USD | 98,530.00 USD | 32,280.00 USD | 30,960.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3163` | 11,060,000.00 USD | 11,060,000.00 USD | 225,120.00 USD | 116,130.00 USD | 134,250.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3165` | 1,490.00 USD | 13,890.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3167` | 2,570,000.00 USD | 2,570,000.00 USD | 50,820.00 USD | 13,150.00 USD | 18,430.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3167` | 10,580,000.00 USD | 10,580,000.00 USD | 328,930.00 USD | 75,090.00 USD | 95,630.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3171` | 2,490,000.00 USD | 2,490,000.00 USD | 7,710.00 USD | 13,460.00 USD | 9,490.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3171` | 10,080,000.00 USD | 10,080,000.00 USD | 293,450.00 USD | 89,970.00 USD | 96,960.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3175` | 2,460,000.00 USD | 2,460,000.00 USD | 16,390.00 USD | 5,630.00 USD | 3,360.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3175` | 9,600,000.00 USD | 9,600,000.00 USD | 28,570.00 USD | 12,370.00 USD | 39,210.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3175` | 1,400.00 USD | 12,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3179` | 2,430,000.00 USD | 2,430,000.00 USD | 39,170.00 USD | 19,900.00 USD | 26,480.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3179` | 9,520,000.00 USD | 9,520,000.00 USD | 231,050.00 USD | 38,200.00 USD | 53,150.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3183` | 2,350,000.00 USD | 2,350,000.00 USD | 362,180.00 USD | 45,830.00 USD | 65,710.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3183` | 9,200,000.00 USD | 9,200,000.00 USD | 551,920.00 USD | 51,290.00 USD | 82,240.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3187` | 1,870,000.00 USD | 1,870,000.00 USD | 23,690.00 USD | 2,240.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3187` | 8,510,000.00 USD | 8,510,000.00 USD | 117,850.00 USD | 29,330.00 USD | 11,120.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3191` | 8,350,000.00 USD | 8,350,000.00 USD | 59,160.00 USD | 13,950.00 USD | 11,780.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3207` | 8,270,000.00 USD | 8,270,000.00 USD | 158,770.00 USD | 34,380.00 USD | 7,770.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3211` | 8,070,000.00 USD | 8,070,000.00 USD | 403,080.00 USD | 68,150.00 USD | 35,920.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3215` | 7,560,000.00 USD | 7,560,000.00 USD | 184,080.00 USD | 34,690.00 USD | 73,480.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3219` | 7,270,000.00 USD | 7,270,000.00 USD | 324,100.00 USD | 61,830.00 USD | 54,040.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3223` | 1,850,000.00 USD | 1,850,000.00 USD | 0.00 USD | 0.00 USD | 20,260.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3223` | 6,830,000.00 USD | 6,830,000.00 USD | 435,620.00 USD | 137,210.00 USD | 89,860.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3227` | 1,830,000.00 USD | 1,830,000.00 USD | 101,660.00 USD | 43,840.00 USD | 51,780.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3227` | 6,170,000.00 USD | 6,170,000.00 USD | 638,380.00 USD | 208,030.00 USD | 227,150.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3231` | 1,630,000.00 USD | 1,630,000.00 USD | 161,500.00 USD | 49,860.00 USD | 68,490.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3231` | 5,090,000.00 USD | 5,090,000.00 USD | 589,500.00 USD | 180,670.00 USD | 295,130.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3235` | 1,350,000.00 USD | 1,350,000.00 USD | 54,750.00 USD | 28,520.00 USD | 31,960.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3235` | 4,030,000.00 USD | 4,030,000.00 USD | 507,910.00 USD | 168,260.00 USD | 205,040.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3235` | 11,000.00 USD | 11,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3239` | 1,240,000.00 USD | 1,240,000.00 USD | 15,020.00 USD | 10,730.00 USD | 3,870.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3239` | 3,150,000.00 USD | 3,150,000.00 USD | 354,650.00 USD | 119,100.00 USD | 114,090.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3243` | 1,210,000.00 USD | 1,210,000.00 USD | 80,740.00 USD | 20,910.00 USD | 19,290.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3243` | 2,560,000.00 USD | 2,560,000.00 USD | 265,190.00 USD | 39,180.00 USD | 42,580.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3247` | 1,090,000.00 USD | 1,090,000.00 USD | 189,030.00 USD | 69,510.00 USD | 116,500.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3247` | 2,210,000.00 USD | 2,210,000.00 USD | 559,960.00 USD | 81,310.00 USD | 196,520.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3251` | 710,000.00 USD | 710,000.00 USD | 585,700.00 USD | 52,790.00 USD | 51,440.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3251` | 1,370,000.00 USD | 1,370,000.00 USD | 815,520.00 USD | 69,770.00 USD | 61,340.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3255` | 20,070.00 USD | 20,070.00 USD | 20,070.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3255` | 426,520.00 USD | 426,520.00 USD | 251,380.00 USD | 60,580.00 USD | 35,520.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3259` | 79,040.00 USD | 79,040.00 USD | 51,940.00 USD | 16,810.00 USD | 10,280.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3339` | 455,400.00 USD | 455,400.00 USD | 363,280.00 USD | 69,780.00 USD | 22,330.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3343` | 708,090.00 USD | 708,090.00 USD | 198,570.00 USD | 32,750.00 USD | 21,370.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3347` | 1,000,000.00 USD | 1,000,000.00 USD | 184,080.00 USD | 34,690.00 USD | 73,480.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3351` | 1,440,000.00 USD | 1,440,000.00 USD | 324,100.00 USD | 61,830.00 USD | 54,040.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3355` | 20,260.00 USD | 20,260.00 USD | 0.00 USD | 0.00 USD | 20,260.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3355` | 2,100,000.00 USD | 2,100,000.00 USD | 435,620.00 USD | 137,210.00 USD | 89,860.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3359` | 217,540.00 USD | 217,540.00 USD | 101,660.00 USD | 43,840.00 USD | 51,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3359` | 3,180,000.00 USD | 3,180,000.00 USD | 638,380.00 USD | 208,030.00 USD | 227,150.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3363` | 497,390.00 USD | 497,390.00 USD | 161,500.00 USD | 49,860.00 USD | 68,490.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3363` | 4,240,000.00 USD | 4,240,000.00 USD | 589,500.00 USD | 180,670.00 USD | 295,130.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3367` | 612,620.00 USD | 612,620.00 USD | 54,750.00 USD | 28,520.00 USD | 31,960.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3367` | 5,120,000.00 USD | 5,120,000.00 USD | 507,910.00 USD | 168,260.00 USD | 205,040.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3371` | 642,240.00 USD | 642,240.00 USD | 15,020.00 USD | 10,730.00 USD | 3,870.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3371` | 5,710,000.00 USD | 5,710,000.00 USD | 354,650.00 USD | 119,100.00 USD | 114,090.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3375` | 763,180.00 USD | 763,180.00 USD | 80,740.00 USD | 20,910.00 USD | 19,290.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3375` | 6,060,000.00 USD | 6,060,000.00 USD | 265,190.00 USD | 39,180.00 USD | 42,580.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3379` | 1,140,000.00 USD | 1,140,000.00 USD | 189,030.00 USD | 69,510.00 USD | 116,500.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3379` | 6,900,000.00 USD | 6,900,000.00 USD | 559,960.00 USD | 81,310.00 USD | 196,520.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3383` | 1,830,000.00 USD | 1,830,000.00 USD | 585,700.00 USD | 52,790.00 USD | 51,440.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3383` | 7,840,000.00 USD | 7,840,000.00 USD | 815,520.00 USD | 69,770.00 USD | 61,340.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3387` | 1,850,000.00 USD | 1,850,000.00 USD | 20,070.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3387` | 8,190,000.00 USD | 8,190,000.00 USD | 251,380.00 USD | 60,580.00 USD | 35,520.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3391` | 8,270,000.00 USD | 8,270,000.00 USD | 51,940.00 USD | 16,810.00 USD | 10,280.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3403` | 8,370,000.00 USD | 8,370,000.00 USD | 79,380.00 USD | 17,190.00 USD | 3,890.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3407` | 8,580,000.00 USD | 8,580,000.00 USD | 162,870.00 USD | 34,080.00 USD | 13,980.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3411` | 8,760,000.00 USD | 8,760,000.00 USD | 121,920.00 USD | 17,350.00 USD | 35,690.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3415` | 8,870,000.00 USD | 8,870,000.00 USD | 75,860.00 USD | 17,240.00 USD | 26,270.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3419` | 9,100,000.00 USD | 9,100,000.00 USD | 162,450.00 USD | 45,810.00 USD | 19,490.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3423` | 1,890,000.00 USD | 1,890,000.00 USD | 5,750.00 USD | 5,600.00 USD | 27,350.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3423` | 9,620,000.00 USD | 9,620,000.00 USD | 331,520.00 USD | 82,020.00 USD | 100,690.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3425` | 456.55 USD | 456.55 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.3427` | 2,050,000.00 USD | 2,050,000.00 USD | 98,530.00 USD | 32,280.00 USD | 30,960.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3427` | 10,090,000.00 USD | 10,090,000.00 USD | 225,120.00 USD | 116,130.00 USD | 134,250.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3431` | 2,130,000.00 USD | 2,130,000.00 USD | 50,820.00 USD | 13,150.00 USD | 18,430.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3431` | 10,590,000.00 USD | 10,590,000.00 USD | 328,930.00 USD | 75,090.00 USD | 95,630.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3435` | 2,160,000.00 USD | 2,160,000.00 USD | 7,710.00 USD | 13,460.00 USD | 9,490.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3435` | 11,070,000.00 USD | 11,070,000.00 USD | 295,240.00 USD | 89,970.00 USD | 96,960.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3435` | 153.89 USD | 610.44 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.3439` | 2,190,000.00 USD | 2,190,000.00 USD | 16,390.00 USD | 5,630.00 USD | 3,360.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3439` | 11,150,000.00 USD | 11,150,000.00 USD | 29,120.00 USD | 12,370.00 USD | 39,210.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3443` | 2,270,000.00 USD | 2,270,000.00 USD | 39,170.00 USD | 19,900.00 USD | 26,480.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3443` | 11,480,000.00 USD | 11,480,000.00 USD | 231,050.00 USD | 38,200.00 USD | 53,150.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3445` | 5,290.00 USD | 5,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.3447` | 2,600,000.00 USD | 2,600,000.00 USD | 235,910.00 USD | 35,820.00 USD | 55,570.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3447` | 11,930,000.00 USD | 11,930,000.00 USD | 355,170.00 USD | 34,230.00 USD | 68,590.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3451` | 2,770,000.00 USD | 2,770,000.00 USD | 150,040.00 USD | 12,250.00 USD | 10,150.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3451` | 12,260,000.00 USD | 12,260,000.00 USD | 274,980.00 USD | 26,900.00 USD | 20,240.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3455` | 2,770,000.00 USD | 2,770,000.00 USD | 1,320.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3455` | 12,400,000.00 USD | 12,400,000.00 USD | 97,690.00 USD | 33,430.00 USD | 16,310.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3455` | 486.46 USD | 6,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.3459` | 2,780,000.00 USD | 2,780,000.00 USD | 4,260.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3459` | 12,430,000.00 USD | 12,430,000.00 USD | 22,340.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3463` | 2,780,000.00 USD | 2,780,000.00 USD | 397.30 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3463` | 12,430,000.00 USD | 12,430,000.00 USD | 3,330.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3467` | 2,780,000.00 USD | 2,780,000.00 USD | 57.70 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3467` | 12,430,000.00 USD | 12,430,000.00 USD | 1,130.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3471` | 2,780,000.00 USD | 2,780,000.00 USD | 307.20 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3471` | 12,430,000.00 USD | 12,430,000.00 USD | 2,140.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3475` | 2,780,000.00 USD | 2,780,000.00 USD | 663.20 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3475` | 12,440,000.00 USD | 12,440,000.00 USD | 2,640.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3475` | 10,210.00 USD | 16,590.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.3479` | 2,780,000.00 USD | 2,780,000.00 USD | 81.40 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3479` | 12,440,000.00 USD | 12,440,000.00 USD | 1,770.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3485` | 223.04 USD | 16,820.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.3491` | 12,440,000.00 USD | 12,440,000.00 USD | 1,340.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3495` | 12,440,000.00 USD | 12,440,000.00 USD | 415.52 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3503` | 12,440,000.00 USD | 12,440,000.00 USD | 1,990.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3505` | 177,540.00 USD | 194,350.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.3507` | 2,780,000.00 USD | 2,780,000.00 USD | 57.95 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3507` | 12,450,000.00 USD | 12,450,000.00 USD | 5,660.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3511` | 2,780,000.00 USD | 2,780,000.00 USD | 1,880.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3511` | 12,450,000.00 USD | 12,450,000.00 USD | 4,590.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3515` | 2,780,000.00 USD | 2,780,000.00 USD | 2,300.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3515` | 12,460,000.00 USD | 12,460,000.00 USD | 3,690.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3519` | 2,780,000.00 USD | 2,780,000.00 USD | 297.83 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3519` | 12,460,000.00 USD | 12,460,000.00 USD | 2,490.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3523` | 2,780,000.00 USD | 2,780,000.00 USD | 43.25 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3523` | 12,460,000.00 USD | 12,460,000.00 USD | 846.39 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3527` | 2,780,000.00 USD | 2,780,000.00 USD | 221.36 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3527` | 12,460,000.00 USD | 12,460,000.00 USD | 1,610.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3531` | 2,780,000.00 USD | 2,780,000.00 USD | 506.09 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3531` | 12,460,000.00 USD | 12,460,000.00 USD | 1,980.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3535` | 2,780,000.00 USD | 2,780,000.00 USD | 61.02 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3535` | 12,460,000.00 USD | 12,460,000.00 USD | 1,320.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3535` | 223.06 USD | 194,580.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3555` | 5,510.00 USD | 200,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.3599` | 12,490,000.00 USD | 12,490,000.00 USD | 18,580.00 USD | 6,010.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3603` | 12,550,000.00 USD | 12,550,000.00 USD | 48,320.00 USD | 6,290.00 USD | 2,910.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3607` | 12,590,000.00 USD | 12,590,000.00 USD | 31,470.00 USD | 4,710.00 USD | 4,750.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3611` | 12,620,000.00 USD | 12,620,000.00 USD | 24,060.00 USD | 2,960.00 USD | 10,110.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3615` | 12,700,000.00 USD | 12,700,000.00 USD | 61,190.00 USD | 8,080.00 USD | 1,960.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3619` | 2,790,000.00 USD | 2,790,000.00 USD | 501.40 USD | 654.45 USD | 5,890.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3619` | 12,830,000.00 USD | 12,830,000.00 USD | 82,550.00 USD | 20,630.00 USD | 33,010.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3623` | 2,830,000.00 USD | 2,830,000.00 USD | 24,780.00 USD | 8,270.00 USD | 8,880.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3623` | 12,990,000.00 USD | 12,990,000.00 USD | 89,280.00 USD | 33,600.00 USD | 36,370.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3627` | 2,860,000.00 USD | 2,860,000.00 USD | 15,110.00 USD | 5,590.00 USD | 8,310.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3627` | 13,120,000.00 USD | 13,120,000.00 USD | 77,830.00 USD | 18,040.00 USD | 36,410.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3631` | 2,880,000.00 USD | 2,880,000.00 USD | 7,150.00 USD | 4,680.00 USD | 5,260.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3631` | 13,250,000.00 USD | 13,250,000.00 USD | 76,220.00 USD | 25,590.00 USD | 26,610.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3635` | 2,880,000.00 USD | 2,880,000.00 USD | 147.65 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3635` | 13,320,000.00 USD | 13,320,000.00 USD | 44,400.00 USD | 16,220.00 USD | 6,560.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3639` | 2,890,000.00 USD | 2,890,000.00 USD | 9,160.00 USD | 2,950.00 USD | 2,470.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3639` | 13,360,000.00 USD | 13,360,000.00 USD | 24,690.00 USD | 2,960.00 USD | 9,300.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3643` | 2,940,000.00 USD | 2,940,000.00 USD | 19,870.00 USD | 6,710.00 USD | 14,730.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3643` | 13,480,000.00 USD | 13,480,000.00 USD | 89,610.00 USD | 8,430.00 USD | 22,010.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3645` | 376.53 USD | 200,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.3647` | 3,060,000.00 USD | 3,060,000.00 USD | 98,340.00 USD | 11,560.00 USD | 14,830.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3647` | 13,600,000.00 USD | 13,600,000.00 USD | 91,260.00 USD | 11,120.00 USD | 19,200.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3648` | 3,070,000.00 USD | 3,070,000.00 USD | 4,900.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3651` | 13,670,000.00 USD | 13,670,000.00 USD | 60,980.00 USD | 4,810.00 USD | 2,640.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3665` | 262.78 USD | 200,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3745` | 6,690.00 USD | 207,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3785` | 537.85 USD | 207,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3795` | 557,900.00 USD | 765,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3815` | 285.74 USD | 766,140.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3845` | 115.35 USD | 766,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3895` | 6,280.00 USD | 772,540.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3905` | 4,770.00 USD | 777,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3915` | 487.42 USD | 777,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3945` | 1,490.00 USD | 779,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3955` | 118,430.00 USD | 897,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4185` | 167.40 USD | 897,880.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4205` | 4,480.00 USD | 902,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4245` | 51,830.00 USD | 954,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4475` | 73,860.00 USD | 1,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4705` | 203.26 USD | 1,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4905` | 841.21 USD | 1,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4915` | 5,130.00 USD | 1,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.5345` | 669.73 USD | 1,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.5365` | 695,970.00 USD | 1,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.5395` | 18,560.00 USD | 1,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.5585` | 742.25 USD | 1,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.5625` | 140.62 USD | 1,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.6145` | 36,870.00 USD | 1,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.6275` | 275.47 USD | 1,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.6285` | 7,390.00 USD | 1,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `0.0685` | 500,240.00 USD | 0.00 USD | 2,740.00 USD | `-79.33%` | `40,000.00` |
| `Live` | `Long` | `0.0695` | 497,500.00 USD | 0.00 USD | 331.31 USD | `-79.03%` | `4,767.00` |
| `Live` | `Long` | `0.0725` | 497,170.00 USD | 0.00 USD | 150.73 USD | `-78.13%` | `2,079.00` |
| `Live` | `Long` | `0.0825` | 497,020.00 USD | 0.00 USD | 1,050.00 USD | `-75.11%` | `12,781.00` |
| `Live` | `Long` | `0.1035` | 495,970.00 USD | 0.00 USD | 4,230.00 USD | `-68.77%` | `40,871.00` |
| `Live` | `Long` | `0.1105` | 491,740.00 USD | 0.00 USD | 4,370.00 USD | `-66.66%` | `39,551.00` |
| `Live` | `Long` | `0.1125` | 487,370.00 USD | 0.00 USD | 803.93 USD | `-66.06%` | `7,146.00` |
| `Live` | `Long` | `0.1135` | 486,560.00 USD | 0.00 USD | 113.50 USD | `-65.75%` | `1,000.00` |
| `Live` | `Long` | `0.1175` | 486,450.00 USD | 0.00 USD | 394.80 USD | `-64.55%` | `3,360.00` |
| `Live` | `Long` | `0.1225` | 486,060.00 USD | 0.00 USD | 643.62 USD | `-63.04%` | `5,254.00` |
| `Live` | `Long` | `0.1235` | 485,410.00 USD | 0.00 USD | 27,020.00 USD | `-62.74%` | `218,745.00` |
| `Live` | `Long` | `0.1375` | 458,400.00 USD | 0.00 USD | 1,560.00 USD | `-58.51%` | `11,352.00` |
| `Live` | `Long` | `0.1405` | 456,840.00 USD | 0.00 USD | 429.65 USD | `-57.61%` | `3,058.00` |
| `Live` | `Long` | `0.1445` | 456,410.00 USD | 0.00 USD | 130.63 USD | `-56.40%` | `904.00` |
| `Live` | `Long` | `0.1485` | 456,280.00 USD | 0.00 USD | 371.55 USD | `-55.19%` | `2,502.00` |
| `Live` | `Long` | `0.1555` | 455,900.00 USD | 0.00 USD | 469.77 USD | `-53.08%` | `3,021.00` |
| `Live` | `Long` | `0.1595` | 455,430.00 USD | 0.00 USD | 390.46 USD | `-51.88%` | `2,448.00` |
| `Live` | `Long` | `0.1615` | 455,040.00 USD | 0.00 USD | 12,400.00 USD | `-51.27%` | `76,797.00` |
| `Live` | `Long` | `0.1705` | 442,640.00 USD | 0.00 USD | 20,360.00 USD | `-48.56%` | `119,400.00` |
| `Live` | `Long` | `0.1725` | 422,280.00 USD | 0.00 USD | 3,930.00 USD | `-47.95%` | `22,767.00` |
| `Live` | `Long` | `0.1735` | 418,360.00 USD | 0.00 USD | 11,160.00 USD | `-47.65%` | `64,322.00` |
| `Live` | `Long` | `0.1745` | 407,200.00 USD | 0.00 USD | 471.50 USD | `-47.35%` | `2,702.00` |
| `Live` | `Long` | `0.1755` | 406,720.00 USD | 0.00 USD | 1,030.00 USD | `-47.05%` | `5,865.00` |
| `Live` | `Long` | `0.1765` | 405,700.00 USD | 0.00 USD | 5,080.00 USD | `-46.75%` | `28,764.00` |
| `Live` | `Long` | `0.1775` | 400,620.00 USD | 0.00 USD | 433.81 USD | `-46.44%` | `2,444.00` |
| `Live` | `Long` | `0.1795` | 400,180.00 USD | 0.00 USD | 209.84 USD | `-45.84%` | `1,169.00` |
| `Live` | `Long` | `0.1895` | 399,970.00 USD | 0.00 USD | 1,150.00 USD | `-42.82%` | `6,059.00` |
| `Live` | `Long` | `0.1975` | 398,830.00 USD | 0.00 USD | 838.39 USD | `-40.41%` | `4,245.00` |
| `Live` | `Long` | `0.2025` | 397,990.00 USD | 0.00 USD | 3,020.00 USD | `-38.90%` | `14,921.00` |
| `Live` | `Long` | `0.2045` | 394,970.00 USD | 0.00 USD | 6,130.00 USD | `-38.30%` | `30,000.00` |
| `Live` | `Long` | `0.2145` | 388,830.00 USD | 0.00 USD | 3,330.00 USD | `-35.28%` | `15,528.00` |
| `Live` | `Long` | `0.2175` | 385,500.00 USD | 0.00 USD | 1,520.00 USD | `-34.38%` | `7,003.00` |
| `Live` | `Long` | `0.2195` | 383,980.00 USD | 0.00 USD | 515.17 USD | `-33.77%` | `2,347.00` |
| `Live` | `Long` | `0.2235` | 383,460.00 USD | 0.00 USD | 2,360.00 USD | `-32.56%` | `10,560.00` |
| `Live` | `Long` | `0.2255` | 381,100.00 USD | 0.00 USD | 4,590.00 USD | `-31.96%` | `20,360.00` |
| `Live` | `Long` | `0.2265` | 376,510.00 USD | 0.00 USD | 319.59 USD | `-31.66%` | `1,411.00` |
| `Live` | `Long` | `0.2305` | 376,190.00 USD | 0.00 USD | 4,180.00 USD | `-30.45%` | `18,150.00` |
| `Live` | `Long` | `0.2315` | 372,010.00 USD | 0.00 USD | 3,010.00 USD | `-30.15%` | `13,018.00` |
| `Live` | `Long` | `0.2325` | 368,990.00 USD | 0.00 USD | 308.30 USD | `-29.85%` | `1,326.00` |
| `Live` | `Long` | `0.2335` | 368,690.00 USD | 0.00 USD | 2,370.00 USD | `-29.55%` | `10,154.00` |
| `Live` | `Long` | `0.2345` | 366,320.00 USD | 0.00 USD | 1,000.00 USD | `-29.25%` | `4,283.00` |
| `Live` | `Long` | `0.2355` | 365,310.00 USD | 0.00 USD | 6,140.00 USD | `-28.94%` | `26,082.00` |
| `Live` | `Long` | `0.2365` | 359,170.00 USD | 0.00 USD | 344.11 USD | `-28.64%` | `1,455.00` |
| `Live` | `Long` | `0.2385` | 358,820.00 USD | 0.00 USD | 1,260.00 USD | `-28.04%` | `5,298.00` |
| `Live` | `Long` | `0.2405` | 357,560.00 USD | 0.00 USD | 510.10 USD | `-27.44%` | `2,121.00` |
| `Live` | `Long` | `0.2445` | 357,050.00 USD | 0.00 USD | 889.49 USD | `-26.23%` | `3,638.00` |
| `Live` | `Long` | `0.2455` | 356,160.00 USD | 0.00 USD | 466.70 USD | `-25.93%` | `1,901.00` |
| `Live` | `Long` | `0.2465` | 355,690.00 USD | 0.00 USD | 276.57 USD | `-25.63%` | `1,122.00` |
| `Live` | `Long` | `0.2475` | 355,420.00 USD | 0.00 USD | 2,420.00 USD | `-25.32%` | `9,797.00` |
| `Live` | `Long` | `0.2565` | 352,990.00 USD | 0.00 USD | 1,230.00 USD | `-22.61%` | `4,794.00` |
| `Live` | `Long` | `0.2585` | 351,760.00 USD | 0.00 USD | 1,580.00 USD | `-22.00%` | `6,097.00` |
| `Live` | `Long` | `0.2595` | 350,190.00 USD | 0.00 USD | 315.81 USD | `-21.70%` | `1,217.00` |
| `Live` | `Long` | `0.2605` | 349,870.00 USD | 0.00 USD | 8,650.00 USD | `-21.40%` | `33,208.00` |
| `Live` | `Long` | `0.2615` | 341,220.00 USD | 0.00 USD | 466.78 USD | `-21.10%` | `1,785.00` |
| `Live` | `Long` | `0.2625` | 340,750.00 USD | 0.00 USD | 22,990.00 USD | `-20.80%` | `87,573.00` |
| `Live` | `Long` | `0.2635` | 317,770.00 USD | 0.00 USD | 405.00 USD | `-20.50%` | `1,537.00` |
| `Live` | `Long` | `0.2655` | 317,360.00 USD | 0.00 USD | 7,520.00 USD | `-19.89%` | `28,325.00` |
| `Live` | `Long` | `0.2665` | 309,840.00 USD | 0.00 USD | 450.92 USD | `-19.59%` | `1,692.00` |
| `Live` | `Long` | `0.2675` | 309,390.00 USD | 0.00 USD | 194.47 USD | `-19.29%` | `727.00` |
| `Live` | `Long` | `0.2685` | 309,200.00 USD | 0.00 USD | 322.74 USD | `-18.99%` | `1,202.00` |
| `Live` | `Long` | `0.2725` | 308,870.00 USD | 0.00 USD | 412.84 USD | `-17.78%` | `1,515.00` |
| `Live` | `Long` | `0.2735` | 308,460.00 USD | 0.00 USD | 5,500.00 USD | `-17.48%` | `20,120.00` |
| `Live` | `Long` | `0.2755` | 302,960.00 USD | 0.00 USD | 84,780.00 USD | `-16.88%` | `307,728.00` |
| `Live` | `Long` | `0.2775` | 218,180.00 USD | 0.00 USD | 41,220.00 USD | `-16.27%` | `148,541.00` |
| `Live` | `Long` | `0.2785` | 176,960.00 USD | 0.00 USD | 2,130.00 USD | `-15.97%` | `7,634.00` |
| `Live` | `Long` | `0.2795` | 174,830.00 USD | 0.00 USD | 13,720.00 USD | `-15.67%` | `49,085.00` |
| `Live` | `Long` | `0.2805` | 161,110.00 USD | 0.00 USD | 6,280.00 USD | `-15.37%` | `22,380.00` |
| `Live` | `Long` | `0.2815` | 154,830.00 USD | 0.00 USD | 1,310.00 USD | `-15.07%` | `4,642.00` |
| `Live` | `Long` | `0.2825` | 153,530.00 USD | 0.00 USD | 15,060.00 USD | `-14.76%` | `53,321.00` |
| `Live` | `Long` | `0.2835` | 138,470.00 USD | 0.00 USD | 1,430.00 USD | `-14.46%` | `5,038.00` |
| `Live` | `Long` | `0.2865` | 137,040.00 USD | 0.00 USD | 482.75 USD | `-13.56%` | `1,685.00` |
| `Live` | `Long` | `0.2875` | 136,550.00 USD | 0.00 USD | 1,600.00 USD | `-13.25%` | `5,572.00` |
| `Live` | `Long` | `0.2915` | 134,950.00 USD | 0.00 USD | 591.45 USD | `-12.05%` | `2,029.00` |
| `Live` | `Long` | `0.2925` | 134,360.00 USD | 0.00 USD | 957.64 USD | `-11.75%` | `3,274.00` |
| `Live` | `Long` | `0.2945` | 133,400.00 USD | 0.00 USD | 3,760.00 USD | `-11.14%` | `12,780.00` |
| `Live` | `Long` | `0.2955` | 129,640.00 USD | 0.00 USD | 125.29 USD | `-10.84%` | `424.00` |
| `Live` | `Long` | `0.2995` | 129,510.00 USD | 0.00 USD | 127.89 USD | `-9.63%` | `427.00` |
| `Live` | `Long` | `0.3005` | 129,390.00 USD | 0.00 USD | 7,130.00 USD | `-9.33%` | `23,720.00` |
| `Live` | `Long` | `0.3015` | 122,260.00 USD | 0.00 USD | 10,330.00 USD | `-9.03%` | `34,248.00` |
| `Live` | `Long` | `0.3025` | 111,930.00 USD | 0.00 USD | 694.54 USD | `-8.73%` | `2,296.00` |
| `Live` | `Long` | `0.3035` | 111,240.00 USD | 0.00 USD | 693.50 USD | `-8.43%` | `2,285.00` |
| `Live` | `Long` | `0.3045` | 110,540.00 USD | 0.00 USD | 5,540.00 USD | `-8.13%` | `18,206.00` |
| `Live` | `Long` | `0.3055` | 105,000.00 USD | 0.00 USD | 5,300.00 USD | `-7.82%` | `17,354.00` |
| `Live` | `Long` | `0.3065` | 99,700.00 USD | 0.00 USD | 14,720.00 USD | `-7.52%` | `48,026.00` |
| `Live` | `Long` | `0.3085` | 84,980.00 USD | 0.00 USD | 6,670.00 USD | `-6.92%` | `21,612.00` |
| `Live` | `Long` | `0.3115` | 78,310.00 USD | 0.00 USD | 304.34 USD | `-6.01%` | `977.00` |
| `Live` | `Long` | `0.3125` | 78,010.00 USD | 0.00 USD | 17,680.00 USD | `-5.71%` | `56,580.00` |
| `Live` | `Long` | `0.3135` | 60,330.00 USD | 0.00 USD | 44,390.00 USD | `-5.41%` | `141,602.00` |
| `Live` | `Long` | `0.3145` | 15,930.00 USD | 0.00 USD | 1,900.00 USD | `-5.11%` | `6,027.00` |
| `Live` | `Long` | `0.3155` | 14,040.00 USD | 0.00 USD | 142.29 USD | `-4.81%` | `451.00` |
| `Live` | `Long` | `0.3165` | 13,900.00 USD | 0.00 USD | 1,490.00 USD | `-4.50%` | `4,723.00` |
| `Live` | `Long` | `0.3175` | 12,400.00 USD | 0.00 USD | 938.85 USD | `-4.20%` | `2,957.00` |
| `Live` | `Long` | `0.3185` | 11,460.00 USD | 0.00 USD | 335.70 USD | `-3.90%` | `1,054.00` |
| `Live` | `Long` | `0.3195` | 11,130.00 USD | 0.00 USD | 126.84 USD | `-3.60%` | `397.00` |
| `Live` | `Long` | `0.3235` | 11,000.00 USD | 0.00 USD | 11,000.00 USD | `-2.39%` | `34,003.00` |
| `Live` | `Short` | `0.3425` | 456.55 USD | 456.55 USD | 0.00 USD | `+3.34%` | `1,333.00` |
| `Live` | `Short` | `0.3435` | 610.44 USD | 153.89 USD | 0.00 USD | `+3.64%` | `448.00` |
| `Live` | `Short` | `0.3445` | 5,900.00 USD | 5,290.00 USD | 0.00 USD | `+3.94%` | `15,355.00` |
| `Live` | `Short` | `0.3455` | 6,390.00 USD | 486.46 USD | 0.00 USD | `+4.25%` | `1,408.00` |
| `Live` | `Short` | `0.3475` | 16,590.00 USD | 10,210.00 USD | 0.00 USD | `+4.85%` | `29,369.00` |
| `Live` | `Short` | `0.3485` | 16,820.00 USD | 223.04 USD | 0.00 USD | `+5.15%` | `640.00` |
| `Live` | `Short` | `0.3505` | 194,350.00 USD | 177,540.00 USD | 0.00 USD | `+5.75%` | `506,529.00` |
| `Live` | `Short` | `0.3535` | 194,580.00 USD | 223.06 USD | 0.00 USD | `+6.66%` | `631.00` |
| `Live` | `Short` | `0.3645` | 194,950.00 USD | 376.53 USD | 0.00 USD | `+9.98%` | `1,033.00` |
| `Live` | `Short` | `0.3665` | 195,220.00 USD | 262.78 USD | 0.00 USD | `+10.58%` | `717.00` |
| `Live` | `Short` | `0.3745` | 201,910.00 USD | 6,690.00 USD | 0.00 USD | `+13.00%` | `17,870.00` |
| `Live` | `Short` | `0.3785` | 202,560.00 USD | 652.16 USD | 0.00 USD | `+14.20%` | `1,723.00` |
| `Live` | `Short` | `0.3795` | 760,460.00 USD | 557,900.00 USD | 0.00 USD | `+14.50%` | `1,470,083.00` |
| `Live` | `Short` | `0.3815` | 760,740.00 USD | 285.74 USD | 0.00 USD | `+15.11%` | `749.00` |
| `Live` | `Short` | `0.3845` | 760,860.00 USD | 115.35 USD | 0.00 USD | `+16.01%` | `300.00` |
| `Live` | `Short` | `0.3895` | 767,140.00 USD | 6,280.00 USD | 0.00 USD | `+17.52%` | `16,133.00` |
| `Live` | `Short` | `0.3905` | 771,910.00 USD | 4,770.00 USD | 0.00 USD | `+17.82%` | `12,210.00` |
| `Live` | `Short` | `0.3915` | 772,400.00 USD | 487.42 USD | 0.00 USD | `+18.12%` | `1,245.00` |
| `Live` | `Short` | `0.3945` | 773,880.00 USD | 1,490.00 USD | 0.00 USD | `+19.03%` | `3,770.00` |
| `Live` | `Short` | `0.3955` | 892,310.00 USD | 118,430.00 USD | 0.00 USD | `+19.33%` | `299,436.00` |
| `Live` | `Short` | `0.4185` | 896,940.00 USD | 4,630.00 USD | 0.00 USD | `+26.27%` | `11,065.00` |
| `Live` | `Short` | `0.4255` | 948,890.00 USD | 51,950.00 USD | 0.00 USD | `+28.38%` | `122,096.00` |
| `Live` | `Short` | `0.4455` | 1,020,000.00 USD | 72,520.00 USD | 0.00 USD | `+34.42%` | `162,775.00` |
| `Live` | `Short` | `0.4475` | 1,020,000.00 USD | 1,020.00 USD | 0.00 USD | `+35.02%` | `2,284.00` |
| `Live` | `Short` | `0.4705` | 1,020,000.00 USD | 203.26 USD | 0.00 USD | `+41.96%` | `432.00` |
| `Live` | `Short` | `0.4905` | 1,020,000.00 USD | 841.21 USD | 0.00 USD | `+48.00%` | `1,715.00` |
| `Live` | `Short` | `0.4915` | 1,030,000.00 USD | 5,130.00 USD | 0.00 USD | `+48.30%` | `10,430.00` |
| `Live` | `Short` | `0.5345` | 1,030,000.00 USD | 669.73 USD | 0.00 USD | `+61.27%` | `1,253.00` |
| `Live` | `Short` | `0.5375` | 1,030,000.00 USD | 194.58 USD | 0.00 USD | `+62.18%` | `362.00` |
| `Live` | `Short` | `0.5405` | 1,050,000.00 USD | 18,590.00 USD | 0.00 USD | `+63.08%` | `34,396.00` |
| `Live` | `Short` | `0.5415` | 1,750,000.00 USD | 702,460.00 USD | 0.00 USD | `+63.38%` | `1,297,248.00` |
| `Live` | `Short` | `0.5585` | 1,750,000.00 USD | 742.25 USD | 0.00 USD | `+68.51%` | `1,329.00` |
| `Live` | `Short` | `0.5625` | 1,750,000.00 USD | 140.62 USD | 0.00 USD | `+69.72%` | `250.00` |
| `Live` | `Short` | `0.6145` | 1,790,000.00 USD | 36,870.00 USD | 0.00 USD | `+85.41%` | `60,000.00` |
| `Live` | `Short` | `0.6275` | 1,790,000.00 USD | 275.47 USD | 0.00 USD | `+89.33%` | `439.00` |
| `Live` | `Short` | `0.6285` | 1,800,000.00 USD | 7,390.00 USD | 0.00 USD | `+89.63%` | `11,753.00` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `0.1805` | 819,350.00 USD | 0.00 USD | 6,100.00 USD | `-45.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2035` | 813,260.00 USD | 0.00 USD | 1,750.00 USD | `-38.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2105` | 811,500.00 USD | 0.00 USD | 579.72 USD | `-36.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2345` | 810,920.00 USD | 0.00 USD | 705.61 USD | `-29.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2405` | 810,220.00 USD | 0.00 USD | 1,200.00 USD | `-27.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2415` | 809,020.00 USD | 0.00 USD | 127.51 USD | `-27.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2505` | 808,890.00 USD | 0.00 USD | 1,850.00 USD | `-24.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2565` | 807,030.00 USD | 0.00 USD | 1,920.00 USD | `-22.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2605` | 805,110.00 USD | 0.00 USD | 4,200.00 USD | `-21.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2625` | 800,910.00 USD | 0.00 USD | 954.98 USD | `-20.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2675` | 799,950.00 USD | 0.00 USD | 695.50 USD | `-19.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2685` | 799,260.00 USD | 0.00 USD | 1,630.00 USD | `-18.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2815` | 797,630.00 USD | 0.00 USD | 2,550.00 USD | `-15.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2835` | 795,080.00 USD | 0.00 USD | 229.92 USD | `-14.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2935` | 794,850.00 USD | 0.00 USD | 15,940.00 USD | `-11.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2965` | 778,910.00 USD | 0.00 USD | 111.19 USD | `-10.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2985` | 778,800.00 USD | 0.00 USD | 685.95 USD | `-9.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3005` | 778,110.00 USD | 0.00 USD | 2,710.00 USD | `-9.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3065` | 775,410.00 USD | 0.00 USD | 919.50 USD | `-7.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3075` | 774,490.00 USD | 0.00 USD | 193.11 USD | `-7.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3085` | 774,290.00 USD | 0.00 USD | 16,070.00 USD | `-6.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3095` | 758,230.00 USD | 0.00 USD | 147.32 USD | `-6.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3105` | 758,080.00 USD | 0.00 USD | 25,820.00 USD | `-6.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3115` | 732,260.00 USD | 0.00 USD | 6,530.00 USD | `-6.01%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3125` | 725,740.00 USD | 0.00 USD | 524,570.00 USD | `-5.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3135` | 201,160.00 USD | 0.00 USD | 1,270.00 USD | `-5.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3145` | 199,900.00 USD | 0.00 USD | 25,790.00 USD | `-5.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3155` | 174,110.00 USD | 0.00 USD | 3,600.00 USD | `-4.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3165` | 170,510.00 USD | 0.00 USD | 6,100.00 USD | `-4.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3185` | 164,410.00 USD | 0.00 USD | 2,010.00 USD | `-3.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3195` | 162,400.00 USD | 0.00 USD | 15,160.00 USD | `-3.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3205` | 147,240.00 USD | 0.00 USD | 21,270.00 USD | `-3.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3215` | 125,970.00 USD | 0.00 USD | 55,600.00 USD | `-3.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3225` | 70,370.00 USD | 0.00 USD | 174.47 USD | `-2.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3235` | 70,190.00 USD | 0.00 USD | 845.95 USD | `-2.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3245` | 69,350.00 USD | 0.00 USD | 14,470.00 USD | `-2.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3255` | 54,880.00 USD | 0.00 USD | 8,410.00 USD | `-1.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3265` | 46,460.00 USD | 0.00 USD | 25,740.00 USD | `-1.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3275` | 20,720.00 USD | 0.00 USD | 13,320.00 USD | `-1.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3285` | 7,400.00 USD | 0.00 USD | 3,730.00 USD | `-0.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3295` | 3,670.00 USD | 0.00 USD | 1,830.00 USD | `-0.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3305` | 1,840.00 USD | 0.00 USD | 1,840.00 USD | `-0.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3315` | 496.92 USD | 496.92 USD | 0.00 USD | `+0.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3325` | 41,090.00 USD | 40,600.00 USD | 0.00 USD | `+0.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3335` | 42,580.00 USD | 1,480.00 USD | 0.00 USD | `+0.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3345` | 43,800.00 USD | 1,220.00 USD | 0.00 USD | `+0.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3355` | 218,660.00 USD | 174,860.00 USD | 0.00 USD | `+1.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3365` | 219,040.00 USD | 379.57 USD | 0.00 USD | `+1.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3375` | 219,200.00 USD | 162.00 USD | 0.00 USD | `+1.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3385` | 230,850.00 USD | 11,640.00 USD | 0.00 USD | `+2.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3395` | 230,950.00 USD | 102.87 USD | 0.00 USD | `+2.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3405` | 234,040.00 USD | 3,090.00 USD | 0.00 USD | `+2.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3415` | 234,940.00 USD | 904.63 USD | 0.00 USD | `+3.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3425` | 240,460.00 USD | 5,520.00 USD | 0.00 USD | `+3.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3435` | 248,080.00 USD | 7,610.00 USD | 0.00 USD | `+3.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3455` | 250,960.00 USD | 2,880.00 USD | 0.00 USD | `+4.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3465` | 258,890.00 USD | 7,930.00 USD | 0.00 USD | `+4.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3475` | 262,040.00 USD | 3,150.00 USD | 0.00 USD | `+4.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3485` | 263,100.00 USD | 1,060.00 USD | 0.00 USD | `+5.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3495` | 288,850.00 USD | 25,750.00 USD | 0.00 USD | `+5.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3505` | 307,430.00 USD | 18,580.00 USD | 0.00 USD | `+5.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3535` | 320,850.00 USD | 13,420.00 USD | 0.00 USD | `+6.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3545` | 321,620.00 USD | 769.97 USD | 0.00 USD | `+6.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3555` | 321,850.00 USD | 226.10 USD | 0.00 USD | `+7.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3575` | 326,030.00 USD | 4,180.00 USD | 0.00 USD | `+7.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3585` | 332,010.00 USD | 5,990.00 USD | 0.00 USD | `+8.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3595` | 338,200.00 USD | 6,180.00 USD | 0.00 USD | `+8.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3605` | 338,680.00 USD | 485.59 USD | 0.00 USD | `+8.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3635` | 339,070.00 USD | 390.40 USD | 0.00 USD | `+9.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3655` | 339,510.00 USD | 433.85 USD | 0.00 USD | `+10.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3665` | 339,970.00 USD | 463.99 USD | 0.00 USD | `+10.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3695` | 340,130.00 USD | 159.62 USD | 0.00 USD | `+11.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3705` | 341,060.00 USD | 926.99 USD | 0.00 USD | `+11.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3755` | 343,820.00 USD | 2,760.00 USD | 0.00 USD | `+13.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3785` | 344,090.00 USD | 275.17 USD | 0.00 USD | `+14.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3795` | 344,550.00 USD | 463.37 USD | 0.00 USD | `+14.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3805` | 344,890.00 USD | 337.12 USD | 0.00 USD | `+14.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3815` | 345,010.00 USD | 114.83 USD | 0.00 USD | `+15.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3835` | 345,230.00 USD | 224.73 USD | 0.00 USD | `+15.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3855` | 345,750.00 USD | 514.64 USD | 0.00 USD | `+16.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3895` | 346,100.00 USD | 352.11 USD | 0.00 USD | `+17.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3965` | 348,500.00 USD | 2,400.00 USD | 0.00 USD | `+19.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3975` | 349,070.00 USD | 572.00 USD | 0.00 USD | `+19.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3985` | 350,270.00 USD | 1,200.00 USD | 0.00 USD | `+20.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3995` | 403,150.00 USD | 52,880.00 USD | 0.00 USD | `+20.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4015` | 405,550.00 USD | 2,400.00 USD | 0.00 USD | `+21.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4035` | 406,750.00 USD | 1,200.00 USD | 0.00 USD | `+21.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4055` | 407,950.00 USD | 1,200.00 USD | 0.00 USD | `+22.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4065` | 409,150.00 USD | 1,200.00 USD | 0.00 USD | `+22.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4205` | 409,330.00 USD | 186.70 USD | 0.00 USD | `+26.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4405` | 447,910.00 USD | 38,580.00 USD | 0.00 USD | `+32.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4445` | 448,080.00 USD | 170.69 USD | 0.00 USD | `+34.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4495` | 449,470.00 USD | 1,390.00 USD | 0.00 USD | `+35.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.5005` | 460,620.00 USD | 11,150.00 USD | 0.00 USD | `+51.01%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `0.2979` | 12,850,000.00 USD | 0.00 USD | 12,850,000.00 USD | 69,830.00 USD | 8,600.00 USD | 10,570.00 USD |
| `1D` | `0.2983` | 2,960,000.00 USD | 0.00 USD | 2,960,000.00 USD | 80,810.00 USD | 16,310.00 USD | 27,140.00 USD |
| `7D` | `0.2983` | 12,760,000.00 USD | 0.00 USD | 12,760,000.00 USD | 117,250.00 USD | 9,990.00 USD | 36,400.00 USD |
| `1D` | `0.2987` | 2,830,000.00 USD | 0.00 USD | 2,830,000.00 USD | 44,390.00 USD | 4,220.00 USD | 2,890.00 USD |
| `7D` | `0.2987` | 12,600,000.00 USD | 0.00 USD | 12,600,000.00 USD | 83,850.00 USD | 9,860.00 USD | 6,170.00 USD |
| `7D` | `0.2991` | 12,500,000.00 USD | 0.00 USD | 12,500,000.00 USD | 23,720.00 USD | 6,910.00 USD | 3,870.00 USD |
| `7D` | `0.3051` | 12,460,000.00 USD | 0.00 USD | 12,460,000.00 USD | 380.73 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3055` | 12,460,000.00 USD | 0.00 USD | 12,460,000.00 USD | 1,380.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3063` | 12,460,000.00 USD | 0.00 USD | 12,460,000.00 USD | 1,990.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3067` | 2,780,000.00 USD | 0.00 USD | 2,780,000.00 USD | 57.95 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3067` | 12,460,000.00 USD | 0.00 USD | 12,460,000.00 USD | 5,660.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3071` | 2,780,000.00 USD | 0.00 USD | 2,780,000.00 USD | 2,980.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3071` | 12,450,000.00 USD | 0.00 USD | 12,450,000.00 USD | 6,280.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3075` | 2,780,000.00 USD | 0.00 USD | 2,780,000.00 USD | 1,340.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3075` | 12,450,000.00 USD | 0.00 USD | 12,450,000.00 USD | 2,850.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3079` | 2,770,000.00 USD | 0.00 USD | 2,770,000.00 USD | 43.25 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3079` | 12,450,000.00 USD | 0.00 USD | 12,450,000.00 USD | 2,180.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3083` | 2,770,000.00 USD | 0.00 USD | 2,770,000.00 USD | 221.36 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3083` | 12,440,000.00 USD | 0.00 USD | 12,440,000.00 USD | 1,680.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3087` | 2,770,000.00 USD | 0.00 USD | 2,770,000.00 USD | 506.09 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3087` | 12,440,000.00 USD | 0.00 USD | 12,440,000.00 USD | 2,200.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3091` | 2,770,000.00 USD | 0.00 USD | 2,770,000.00 USD | 61.02 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3091` | 12,440,000.00 USD | 0.00 USD | 12,440,000.00 USD | 1,320.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3107` | 12,440,000.00 USD | 0.00 USD | 12,440,000.00 USD | 1,790.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3111` | 12,440,000.00 USD | 0.00 USD | 12,440,000.00 USD | 554.30 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3119` | 12,440,000.00 USD | 0.00 USD | 12,440,000.00 USD | 2,650.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3123` | 2,770,000.00 USD | 0.00 USD | 2,770,000.00 USD | 77.30 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3123` | 12,430,000.00 USD | 0.00 USD | 12,430,000.00 USD | 7,550.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3127` | 2,770,000.00 USD | 0.00 USD | 2,770,000.00 USD | 3,970.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3127` | 12,430,000.00 USD | 0.00 USD | 12,430,000.00 USD | 8,380.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3131` | 2,770,000.00 USD | 0.00 USD | 2,770,000.00 USD | 1,790.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3131` | 12,420,000.00 USD | 0.00 USD | 12,420,000.00 USD | 3,800.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3135` | 2,770,000.00 USD | 0.00 USD | 2,770,000.00 USD | 57.70 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3135` | 12,410,000.00 USD | 0.00 USD | 12,410,000.00 USD | 2,910.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3139` | 2,770,000.00 USD | 0.00 USD | 2,770,000.00 USD | 295.30 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3139` | 12,410,000.00 USD | 0.00 USD | 12,410,000.00 USD | 2,250.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3143` | 2,770,000.00 USD | 0.00 USD | 2,770,000.00 USD | 429.90 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3143` | 12,410,000.00 USD | 0.00 USD | 12,410,000.00 USD | 184,260.00 USD | 34,890.00 USD | 11,170.00 USD |
| `1D` | `0.3147` | 2,770,000.00 USD | 0.00 USD | 2,770,000.00 USD | 326.60 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3147` | 12,180,000.00 USD | 0.00 USD | 12,180,000.00 USD | 101,370.00 USD | 16,380.00 USD | 10,680.00 USD |
| `7D` | `0.3151` | 12,050,000.00 USD | 0.00 USD | 12,050,000.00 USD | 142,080.00 USD | 23,130.00 USD | 45,340.00 USD |
| `7D` | `0.3155` | 11,840,000.00 USD | 0.00 USD | 11,840,000.00 USD | 157,220.00 USD | 37,570.00 USD | 20,330.00 USD |
| `1D` | `0.3159` | 2,770,000.00 USD | 0.00 USD | 2,770,000.00 USD | 5,750.00 USD | 5,600.00 USD | 27,350.00 USD |
| `7D` | `0.3159` | 11,620,000.00 USD | 0.00 USD | 11,620,000.00 USD | 353,770.00 USD | 101,710.00 USD | 112,500.00 USD |
| `1D` | `0.3163` | 2,730,000.00 USD | 0.00 USD | 2,730,000.00 USD | 98,530.00 USD | 32,280.00 USD | 30,960.00 USD |
| `7D` | `0.3163` | 11,060,000.00 USD | 0.00 USD | 11,060,000.00 USD | 225,120.00 USD | 116,130.00 USD | 134,250.00 USD |
| `1D` | `0.3167` | 2,570,000.00 USD | 0.00 USD | 2,570,000.00 USD | 50,820.00 USD | 13,150.00 USD | 18,430.00 USD |
| `7D` | `0.3167` | 10,580,000.00 USD | 0.00 USD | 10,580,000.00 USD | 328,930.00 USD | 75,090.00 USD | 95,630.00 USD |
| `1D` | `0.3171` | 2,480,000.00 USD | 0.00 USD | 2,480,000.00 USD | 7,710.00 USD | 10,200.00 USD | 7,650.00 USD |
| `7D` | `0.3171` | 10,080,000.00 USD | 0.00 USD | 10,080,000.00 USD | 293,450.00 USD | 89,970.00 USD | 96,960.00 USD |
| `1D` | `0.3175` | 2,460,000.00 USD | 0.00 USD | 2,460,000.00 USD | 16,390.00 USD | 5,630.00 USD | 3,360.00 USD |
| `7D` | `0.3175` | 9,600,000.00 USD | 0.00 USD | 9,600,000.00 USD | 28,570.00 USD | 12,370.00 USD | 39,210.00 USD |
| `1D` | `0.3179` | 2,430,000.00 USD | 0.00 USD | 2,430,000.00 USD | 39,170.00 USD | 21,300.00 USD | 26,480.00 USD |
| `7D` | `0.3179` | 9,520,000.00 USD | 0.00 USD | 9,520,000.00 USD | 231,050.00 USD | 38,200.00 USD | 53,150.00 USD |
| `1D` | `0.3183` | 2,350,000.00 USD | 0.00 USD | 2,350,000.00 USD | 364,130.00 USD | 45,830.00 USD | 65,710.00 USD |
| `7D` | `0.3183` | 9,200,000.00 USD | 0.00 USD | 9,200,000.00 USD | 551,920.00 USD | 51,290.00 USD | 82,240.00 USD |
| `1D` | `0.3187` | 1,870,000.00 USD | 0.00 USD | 1,870,000.00 USD | 23,690.00 USD | 2,240.00 USD | 0.00 USD |
| `7D` | `0.3187` | 8,510,000.00 USD | 0.00 USD | 8,510,000.00 USD | 117,850.00 USD | 29,330.00 USD | 11,120.00 USD |
| `7D` | `0.3191` | 8,350,000.00 USD | 0.00 USD | 8,350,000.00 USD | 59,160.00 USD | 13,950.00 USD | 11,780.00 USD |
| `7D` | `0.3207` | 8,270,000.00 USD | 0.00 USD | 8,270,000.00 USD | 158,770.00 USD | 34,380.00 USD | 7,770.00 USD |
| `7D` | `0.3211` | 8,070,000.00 USD | 0.00 USD | 8,070,000.00 USD | 403,080.00 USD | 68,150.00 USD | 35,920.00 USD |
| `7D` | `0.3215` | 7,560,000.00 USD | 0.00 USD | 7,560,000.00 USD | 184,080.00 USD | 34,690.00 USD | 73,480.00 USD |
| `7D` | `0.3219` | 7,270,000.00 USD | 0.00 USD | 7,270,000.00 USD | 324,100.00 USD | 61,830.00 USD | 54,040.00 USD |
| `1D` | `0.3223` | 1,840,000.00 USD | 0.00 USD | 1,840,000.00 USD | 0.00 USD | 0.00 USD | 20,260.00 USD |
| `7D` | `0.3223` | 6,830,000.00 USD | 0.00 USD | 6,830,000.00 USD | 435,620.00 USD | 137,210.00 USD | 89,860.00 USD |
| `1D` | `0.3227` | 1,820,000.00 USD | 0.00 USD | 1,820,000.00 USD | 101,660.00 USD | 43,840.00 USD | 51,780.00 USD |
| `7D` | `0.3227` | 6,170,000.00 USD | 0.00 USD | 6,170,000.00 USD | 638,380.00 USD | 208,030.00 USD | 227,150.00 USD |
| `1D` | `0.3231` | 1,630,000.00 USD | 0.00 USD | 1,630,000.00 USD | 161,500.00 USD | 49,860.00 USD | 68,490.00 USD |
| `7D` | `0.3231` | 5,090,000.00 USD | 0.00 USD | 5,090,000.00 USD | 589,500.00 USD | 180,670.00 USD | 295,130.00 USD |
| `1D` | `0.3235` | 1,350,000.00 USD | 0.00 USD | 1,350,000.00 USD | 54,750.00 USD | 22,020.00 USD | 28,270.00 USD |
| `7D` | `0.3235` | 4,030,000.00 USD | 0.00 USD | 4,030,000.00 USD | 507,910.00 USD | 168,260.00 USD | 205,040.00 USD |
| `1D` | `0.3239` | 1,240,000.00 USD | 0.00 USD | 1,240,000.00 USD | 15,020.00 USD | 10,730.00 USD | 3,870.00 USD |
| `7D` | `0.3239` | 3,150,000.00 USD | 0.00 USD | 3,150,000.00 USD | 354,650.00 USD | 119,100.00 USD | 114,090.00 USD |
| `1D` | `0.3243` | 1,210,000.00 USD | 0.00 USD | 1,210,000.00 USD | 80,740.00 USD | 20,910.00 USD | 19,290.00 USD |
| `7D` | `0.3243` | 2,560,000.00 USD | 0.00 USD | 2,560,000.00 USD | 265,190.00 USD | 39,180.00 USD | 42,580.00 USD |
| `1D` | `0.3247` | 1,090,000.00 USD | 0.00 USD | 1,090,000.00 USD | 192,930.00 USD | 72,300.00 USD | 116,500.00 USD |
| `7D` | `0.3247` | 2,210,000.00 USD | 0.00 USD | 2,210,000.00 USD | 559,960.00 USD | 81,310.00 USD | 196,520.00 USD |
| `1D` | `0.3251` | 710,000.00 USD | 0.00 USD | 710,000.00 USD | 585,700.00 USD | 52,790.00 USD | 51,440.00 USD |
| `7D` | `0.3251` | 1,370,000.00 USD | 0.00 USD | 1,370,000.00 USD | 815,520.00 USD | 69,770.00 USD | 61,340.00 USD |
| `1D` | `0.3255` | 20,070.00 USD | 0.00 USD | 20,070.00 USD | 20,070.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3255` | 426,520.00 USD | 0.00 USD | 426,520.00 USD | 251,380.00 USD | 60,580.00 USD | 35,520.00 USD |
| `7D` | `0.3259` | 79,040.00 USD | 0.00 USD | 79,040.00 USD | 51,940.00 USD | 16,810.00 USD | 10,280.00 USD |
| `1D` | `0.3311` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3312` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3339` | 455,400.00 USD | 455,400.00 USD | 0.00 USD | 363,280.00 USD | 69,780.00 USD | 22,330.00 USD |
| `7D` | `0.3343` | 708,090.00 USD | 708,090.00 USD | 0.00 USD | 198,570.00 USD | 32,750.00 USD | 21,370.00 USD |
| `7D` | `0.3347` | 1,000,000.00 USD | 1,000,000.00 USD | 0.00 USD | 184,080.00 USD | 34,690.00 USD | 73,480.00 USD |
| `7D` | `0.3351` | 1,440,000.00 USD | 1,440,000.00 USD | 0.00 USD | 324,100.00 USD | 61,830.00 USD | 54,040.00 USD |
| `1D` | `0.3355` | 20,260.00 USD | 20,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 20,260.00 USD |
| `7D` | `0.3355` | 2,100,000.00 USD | 2,100,000.00 USD | 0.00 USD | 435,620.00 USD | 137,210.00 USD | 89,860.00 USD |
| `1D` | `0.3359` | 217,540.00 USD | 217,540.00 USD | 0.00 USD | 101,660.00 USD | 43,840.00 USD | 51,780.00 USD |
| `7D` | `0.3359` | 3,180,000.00 USD | 3,180,000.00 USD | 0.00 USD | 638,380.00 USD | 208,030.00 USD | 227,150.00 USD |
| `1D` | `0.3363` | 497,390.00 USD | 497,390.00 USD | 0.00 USD | 161,500.00 USD | 49,860.00 USD | 68,490.00 USD |
| `7D` | `0.3363` | 4,240,000.00 USD | 4,240,000.00 USD | 0.00 USD | 589,500.00 USD | 180,670.00 USD | 295,130.00 USD |
| `1D` | `0.3367` | 602,430.00 USD | 602,430.00 USD | 0.00 USD | 54,750.00 USD | 22,020.00 USD | 28,270.00 USD |
| `7D` | `0.3367` | 5,120,000.00 USD | 5,120,000.00 USD | 0.00 USD | 507,910.00 USD | 168,260.00 USD | 205,040.00 USD |
| `1D` | `0.3371` | 632,050.00 USD | 632,050.00 USD | 0.00 USD | 15,020.00 USD | 10,730.00 USD | 3,870.00 USD |
| `7D` | `0.3371` | 5,710,000.00 USD | 5,710,000.00 USD | 0.00 USD | 354,650.00 USD | 119,100.00 USD | 114,090.00 USD |
| `1D` | `0.3375` | 753,000.00 USD | 753,000.00 USD | 0.00 USD | 80,740.00 USD | 20,910.00 USD | 19,290.00 USD |
| `7D` | `0.3375` | 6,060,000.00 USD | 6,060,000.00 USD | 0.00 USD | 265,190.00 USD | 39,180.00 USD | 42,580.00 USD |
| `1D` | `0.3379` | 1,130,000.00 USD | 1,130,000.00 USD | 0.00 USD | 192,930.00 USD | 72,300.00 USD | 116,500.00 USD |
| `7D` | `0.3379` | 6,900,000.00 USD | 6,900,000.00 USD | 0.00 USD | 559,960.00 USD | 81,310.00 USD | 196,520.00 USD |
| `1D` | `0.3383` | 1,820,000.00 USD | 1,820,000.00 USD | 0.00 USD | 585,700.00 USD | 52,790.00 USD | 51,440.00 USD |
| `7D` | `0.3383` | 7,840,000.00 USD | 7,840,000.00 USD | 0.00 USD | 815,520.00 USD | 69,770.00 USD | 61,340.00 USD |
| `1D` | `0.3387` | 1,840,000.00 USD | 1,840,000.00 USD | 0.00 USD | 20,070.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3387` | 8,190,000.00 USD | 8,190,000.00 USD | 0.00 USD | 251,380.00 USD | 60,580.00 USD | 35,520.00 USD |
| `7D` | `0.3391` | 8,270,000.00 USD | 8,270,000.00 USD | 0.00 USD | 51,940.00 USD | 16,810.00 USD | 10,280.00 USD |
| `7D` | `0.3403` | 8,370,000.00 USD | 8,370,000.00 USD | 0.00 USD | 79,380.00 USD | 17,190.00 USD | 3,890.00 USD |
| `7D` | `0.3407` | 8,580,000.00 USD | 8,580,000.00 USD | 0.00 USD | 162,870.00 USD | 34,080.00 USD | 13,980.00 USD |
| `7D` | `0.3411` | 8,760,000.00 USD | 8,760,000.00 USD | 0.00 USD | 121,920.00 USD | 17,350.00 USD | 35,690.00 USD |
| `7D` | `0.3415` | 8,870,000.00 USD | 8,870,000.00 USD | 0.00 USD | 75,860.00 USD | 17,240.00 USD | 26,270.00 USD |
| `7D` | `0.3419` | 9,100,000.00 USD | 9,100,000.00 USD | 0.00 USD | 162,450.00 USD | 45,810.00 USD | 19,490.00 USD |
| `1D` | `0.3423` | 1,880,000.00 USD | 1,880,000.00 USD | 0.00 USD | 5,750.00 USD | 5,600.00 USD | 27,350.00 USD |
| `7D` | `0.3423` | 9,620,000.00 USD | 9,620,000.00 USD | 0.00 USD | 331,520.00 USD | 82,020.00 USD | 100,690.00 USD |
| `1D` | `0.3427` | 2,050,000.00 USD | 2,050,000.00 USD | 0.00 USD | 98,530.00 USD | 32,280.00 USD | 30,960.00 USD |
| `7D` | `0.3427` | 10,090,000.00 USD | 10,090,000.00 USD | 0.00 USD | 225,120.00 USD | 116,130.00 USD | 134,250.00 USD |
| `1D` | `0.3431` | 2,130,000.00 USD | 2,130,000.00 USD | 0.00 USD | 50,820.00 USD | 13,150.00 USD | 18,430.00 USD |
| `7D` | `0.3431` | 10,590,000.00 USD | 10,590,000.00 USD | 0.00 USD | 328,930.00 USD | 75,090.00 USD | 95,630.00 USD |
| `1D` | `0.3435` | 2,150,000.00 USD | 2,150,000.00 USD | 0.00 USD | 7,710.00 USD | 10,200.00 USD | 7,650.00 USD |
| `7D` | `0.3435` | 11,070,000.00 USD | 11,070,000.00 USD | 0.00 USD | 295,240.00 USD | 89,970.00 USD | 96,960.00 USD |
| `1D` | `0.3439` | 2,180,000.00 USD | 2,180,000.00 USD | 0.00 USD | 16,390.00 USD | 5,630.00 USD | 3,360.00 USD |
| `7D` | `0.3439` | 11,150,000.00 USD | 11,150,000.00 USD | 0.00 USD | 29,120.00 USD | 12,370.00 USD | 39,210.00 USD |
| `1D` | `0.3443` | 2,270,000.00 USD | 2,270,000.00 USD | 0.00 USD | 39,170.00 USD | 21,300.00 USD | 26,480.00 USD |
| `7D` | `0.3443` | 11,480,000.00 USD | 11,480,000.00 USD | 0.00 USD | 231,050.00 USD | 38,200.00 USD | 53,150.00 USD |
| `1D` | `0.3447` | 2,590,000.00 USD | 2,590,000.00 USD | 0.00 USD | 237,860.00 USD | 35,820.00 USD | 55,570.00 USD |
| `7D` | `0.3447` | 11,930,000.00 USD | 11,930,000.00 USD | 0.00 USD | 355,170.00 USD | 34,230.00 USD | 68,590.00 USD |
| `1D` | `0.3451` | 2,770,000.00 USD | 2,770,000.00 USD | 0.00 USD | 150,040.00 USD | 12,250.00 USD | 10,150.00 USD |
| `7D` | `0.3451` | 12,260,000.00 USD | 12,260,000.00 USD | 0.00 USD | 274,980.00 USD | 26,900.00 USD | 20,240.00 USD |
| `1D` | `0.3455` | 2,770,000.00 USD | 2,770,000.00 USD | 0.00 USD | 1,320.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3455` | 12,400,000.00 USD | 12,400,000.00 USD | 0.00 USD | 97,690.00 USD | 33,430.00 USD | 16,310.00 USD |
| `1D` | `0.3459` | 2,770,000.00 USD | 2,770,000.00 USD | 0.00 USD | 4,260.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3459` | 12,430,000.00 USD | 12,430,000.00 USD | 0.00 USD | 22,340.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3463` | 2,770,000.00 USD | 2,770,000.00 USD | 0.00 USD | 186.80 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3463` | 12,430,000.00 USD | 12,430,000.00 USD | 0.00 USD | 3,330.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3467` | 2,770,000.00 USD | 2,770,000.00 USD | 0.00 USD | 57.70 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3467` | 12,430,000.00 USD | 12,430,000.00 USD | 0.00 USD | 1,130.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3471` | 2,770,000.00 USD | 2,770,000.00 USD | 0.00 USD | 307.20 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3471` | 12,430,000.00 USD | 12,430,000.00 USD | 0.00 USD | 2,140.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3475` | 2,770,000.00 USD | 2,770,000.00 USD | 0.00 USD | 663.20 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3475` | 12,440,000.00 USD | 12,440,000.00 USD | 0.00 USD | 2,640.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3479` | 2,770,000.00 USD | 2,770,000.00 USD | 0.00 USD | 81.40 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3479` | 12,440,000.00 USD | 12,440,000.00 USD | 0.00 USD | 1,770.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3491` | 12,440,000.00 USD | 12,440,000.00 USD | 0.00 USD | 1,340.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3495` | 12,440,000.00 USD | 12,440,000.00 USD | 0.00 USD | 415.52 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3503` | 12,440,000.00 USD | 12,440,000.00 USD | 0.00 USD | 1,990.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3507` | 2,770,000.00 USD | 2,770,000.00 USD | 0.00 USD | 57.95 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3507` | 12,450,000.00 USD | 12,450,000.00 USD | 0.00 USD | 5,660.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3511` | 2,780,000.00 USD | 2,780,000.00 USD | 0.00 USD | 1,880.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3511` | 12,450,000.00 USD | 12,450,000.00 USD | 0.00 USD | 4,590.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3515` | 2,780,000.00 USD | 2,780,000.00 USD | 0.00 USD | 2,300.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3515` | 12,460,000.00 USD | 12,460,000.00 USD | 0.00 USD | 3,690.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3519` | 2,780,000.00 USD | 2,780,000.00 USD | 0.00 USD | 140.03 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3519` | 12,460,000.00 USD | 12,460,000.00 USD | 0.00 USD | 2,490.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3523` | 2,780,000.00 USD | 2,780,000.00 USD | 0.00 USD | 43.25 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3523` | 12,460,000.00 USD | 12,460,000.00 USD | 0.00 USD | 846.39 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3527` | 2,780,000.00 USD | 2,780,000.00 USD | 0.00 USD | 221.36 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3527` | 12,460,000.00 USD | 12,460,000.00 USD | 0.00 USD | 1,610.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3531` | 2,780,000.00 USD | 2,780,000.00 USD | 0.00 USD | 506.09 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3531` | 12,460,000.00 USD | 12,460,000.00 USD | 0.00 USD | 1,980.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3535` | 2,780,000.00 USD | 2,780,000.00 USD | 0.00 USD | 61.02 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3535` | 12,460,000.00 USD | 12,460,000.00 USD | 0.00 USD | 1,320.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3599` | 12,490,000.00 USD | 12,490,000.00 USD | 0.00 USD | 18,580.00 USD | 6,010.00 USD | 0.00 USD |
| `7D` | `0.3603` | 12,550,000.00 USD | 12,550,000.00 USD | 0.00 USD | 48,320.00 USD | 6,290.00 USD | 2,910.00 USD |
| `7D` | `0.3607` | 12,590,000.00 USD | 12,590,000.00 USD | 0.00 USD | 31,470.00 USD | 4,710.00 USD | 4,750.00 USD |
| `7D` | `0.3611` | 12,620,000.00 USD | 12,620,000.00 USD | 0.00 USD | 24,060.00 USD | 2,960.00 USD | 10,110.00 USD |
| `7D` | `0.3615` | 12,700,000.00 USD | 12,700,000.00 USD | 0.00 USD | 61,190.00 USD | 8,080.00 USD | 1,960.00 USD |
| `1D` | `0.3619` | 2,790,000.00 USD | 2,790,000.00 USD | 0.00 USD | 501.40 USD | 654.45 USD | 5,890.00 USD |
| `7D` | `0.3619` | 12,830,000.00 USD | 12,830,000.00 USD | 0.00 USD | 82,550.00 USD | 20,630.00 USD | 33,010.00 USD |
| `1D` | `0.3623` | 2,830,000.00 USD | 2,830,000.00 USD | 0.00 USD | 24,780.00 USD | 8,270.00 USD | 8,880.00 USD |
| `7D` | `0.3623` | 12,990,000.00 USD | 12,990,000.00 USD | 0.00 USD | 89,280.00 USD | 33,600.00 USD | 36,370.00 USD |
| `1D` | `0.3627` | 2,860,000.00 USD | 2,860,000.00 USD | 0.00 USD | 15,050.00 USD | 5,590.00 USD | 8,310.00 USD |
| `7D` | `0.3627` | 13,120,000.00 USD | 13,120,000.00 USD | 0.00 USD | 77,830.00 USD | 18,040.00 USD | 36,410.00 USD |
| `1D` | `0.3631` | 2,870,000.00 USD | 2,870,000.00 USD | 0.00 USD | 7,150.00 USD | 3,380.00 USD | 4,520.00 USD |
| `7D` | `0.3631` | 13,250,000.00 USD | 13,250,000.00 USD | 0.00 USD | 76,220.00 USD | 25,590.00 USD | 26,610.00 USD |
| `1D` | `0.3635` | 2,870,000.00 USD | 2,870,000.00 USD | 0.00 USD | 147.65 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3635` | 13,320,000.00 USD | 13,320,000.00 USD | 0.00 USD | 44,400.00 USD | 16,220.00 USD | 6,560.00 USD |
| `1D` | `0.3639` | 2,890,000.00 USD | 2,890,000.00 USD | 0.00 USD | 9,160.00 USD | 2,950.00 USD | 2,470.00 USD |
| `7D` | `0.3639` | 13,360,000.00 USD | 13,360,000.00 USD | 0.00 USD | 24,690.00 USD | 2,960.00 USD | 9,300.00 USD |
| `1D` | `0.3643` | 2,930,000.00 USD | 2,930,000.00 USD | 0.00 USD | 19,870.00 USD | 7,170.00 USD | 14,730.00 USD |
| `7D` | `0.3643` | 13,480,000.00 USD | 13,480,000.00 USD | 0.00 USD | 89,610.00 USD | 8,430.00 USD | 22,010.00 USD |
| `1D` | `0.3647` | 3,050,000.00 USD | 3,050,000.00 USD | 0.00 USD | 98,340.00 USD | 9,140.00 USD | 12,420.00 USD |
| `7D` | `0.3647` | 13,600,000.00 USD | 13,600,000.00 USD | 0.00 USD | 91,260.00 USD | 11,120.00 USD | 19,200.00 USD |
| `7D` | `0.3651` | 13,670,000.00 USD | 13,670,000.00 USD | 0.00 USD | 60,980.00 USD | 4,810.00 USD | 2,640.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `297.90M` | Total OI Tokens: `899,773,854.4 TRX`
  * 1h OI Change: `-0.27%` | 4h OI Change: `-0.37%` | 24h OI Change: `+1.12%`
  * Exchange Breakdown: Binance=`90.27M` | Bybit=`49.78M` | OKX=`13.77M` | Hyperliquid=`11.63M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `10.00K` | Last 24h: `9.21K` | Last 3d: `-51.81K` | Last 7d: `-271.18K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0100%` | **USDT OKX** | `-0.0006%` |
| **USDT Bybit** | `0.0030%` | **USDT KuCoin** | `0.0100%` |
| **USDT MEXC** | `0.0100%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `0.0004%` | **USDT Bitget** | `0.0100%` |
| **CoinM Binance** | `0.0100%` | **CoinM OKX** | `-` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `TRX` | `55.31%` | `44.69%` | `1.24` | 7,470,000.00 USD |
| `15M` | `Binance` | `55.99%` | `44.01%` | `1.27` | 2,800,000.00 USD |
| `15M` | `OKX` | `56.9%` | `43.1%` | `1.32` | 578,780.00 USD |
| `15M` | `Bybit` | `50.87%` | `49.13%` | `1.04` | 623,070.00 USD |
| `15M` | `KuCoin` | `50.13%` | `49.87%` | `1.01` | 46,140.00 USD |
| `15M` | `Gate` | `61.13%` | `38.87%` | `1.57` | 627,450.00 USD |
| `15M` | `Bitget` | `68.92%` | `31.08%` | `2.22` | 238,780.00 USD |
| `15M` | `BingX` | `86.5%` | `13.5%` | `6.41` | 371,560.00 USD |
| `15M` | `MEXC` | `58.63%` | `41.37%` | `1.42` | 412,880.00 USD |
| `15M` | `Bitunix` | `63.18%` | `36.82%` | `1.72` | 167,760.00 USD |
| `15M` | `Hyperliquid` | `27.06%` | `72.94%` | `0.37` | 29,640.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `43.27%` | `56.73%` | `0.76` | 1,420,000.00 USD |
| `15M` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `WhiteBIT` | `3.57%` | `96.43%` | `0.04` | 79,410.00 USD |
| `15M` | `HTX` | `71.3%` | `28.7%` | `2.48` | 28,430.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `66.63%` | `33.37%` | `2.00` | 46,500.00 USD |
| `15M` | `Aster` | `80.35%` | `19.65%` | `4.09` | 827.57 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `0%` | `100%` | `0.00` | 5.00 USD |
| `15M` | `Whale Positions` | `55.99%` | `44.01%` | `1.27` | 2,800,000.00 USD |
| `15M` | `Global Accounts` | `55.31%` | `44.69%` | `1.24` | 7,470,000.00 USD |
| `1H` | `TRX` | `45.40%` | `54.60%` | `0.83` | 2,600,000.00 USD |
| `1H` | `Binance` | `49.75%` | `50.25%` | `0.99` | 1,070,000.00 USD |
| `1H` | `OKX` | `52.42%` | `47.58%` | `1.10` | 130,410.00 USD |
| `1H` | `Bybit` | `62.97%` | `37.03%` | `1.70` | 111,540.00 USD |
| `1H` | `KuCoin` | `53.33%` | `46.67%` | `1.14` | 60,670.00 USD |
| `1H` | `Gate` | `60.3%` | `39.7%` | `1.52` | 82,010.00 USD |
| `1H` | `Bitget` | `67.97%` | `32.03%` | `2.12` | 39,990.00 USD |
| `1H` | `BingX` | `50.97%` | `49.03%` | `1.04` | 129,650.00 USD |
| `1H` | `MEXC` | `39.49%` | `60.51%` | `0.65` | 21,930.00 USD |
| `1H` | `Bitunix` | `44.94%` | `55.06%` | `0.82` | 28,150.00 USD |
| `1H` | `Hyperliquid` | `56.47%` | `43.53%` | `1.30` | 50,340.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `50%` | `50%` | `1.00` | 424,450.00 USD |
| `1H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `WhiteBIT` | `2.54%` | `97.46%` | `0.03` | 361,950.00 USD |
| `1H` | `HTX` | `52.18%` | `47.82%` | `1.09` | 49,640.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `83.58%` | `16.42%` | `5.09` | 29,000.00 USD |
| `1H` | `Aster` | `4.4%` | `95.6%` | `0.05` | 1,050.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `98.34%` | `1.66%` | `59.24` | 16,470.00 USD |
| `1H` | `Whale Positions` | `49.75%` | `50.25%` | `0.99` | 1,070,000.00 USD |
| `1H` | `Global Accounts` | `45.40%` | `54.60%` | `0.83` | 2,600,000.00 USD |
| `4H` | `TRX` | `43.57%` | `56.43%` | `0.77` | 21,090,000.00 USD |
| `4H` | `Binance` | `49.6%` | `50.4%` | `0.98` | 7,780,000.00 USD |
| `4H` | `OKX` | `44.84%` | `55.16%` | `0.81` | 1,530,000.00 USD |
| `4H` | `Bybit` | `45.6%` | `54.4%` | `0.84` | 1,180,000.00 USD |
| `4H` | `KuCoin` | `48.59%` | `51.41%` | `0.95` | 316,650.00 USD |
| `4H` | `Gate` | `32.54%` | `67.46%` | `0.48` | 2,830,000.00 USD |
| `4H` | `Bitget` | `32.29%` | `67.71%` | `0.48` | 671,940.00 USD |
| `4H` | `BingX` | `24.52%` | `75.48%` | `0.32` | 1,100,000.00 USD |
| `4H` | `MEXC` | `75.03%` | `24.97%` | `3.00` | 279,120.00 USD |
| `4H` | `Bitunix` | `43.42%` | `56.58%` | `0.77` | 227,710.00 USD |
| `4H` | `Hyperliquid` | `69.38%` | `30.62%` | `2.27` | 626,320.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `50.03%` | `49.97%` | `1.00` | 2,400,000.00 USD |
| `4H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `WhiteBIT` | `18.5%` | `81.5%` | `0.23` | 1,600,000.00 USD |
| `4H` | `HTX` | `52.39%` | `47.61%` | `1.10` | 207,710.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `65.68%` | `34.32%` | `1.91` | 243,270.00 USD |
| `4H` | `Aster` | `49.38%` | `50.62%` | `0.98` | 38,330.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `31.31%` | `68.69%` | `0.46` | 74,690.00 USD |
| `4H` | `Whale Positions` | `49.6%` | `50.4%` | `0.98` | 7,780,000.00 USD |
| `4H` | `Global Accounts` | `43.57%` | `56.43%` | `0.77` | 21,090,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5:00 UTC` | `0.3313` | `0.3314` | `0.3313` | `0.3315` | `0.3312` | 203,963.74 USD | 113,592.33 USD | 90,371.41 USD | 23,220.91 USD | `+11.38%` | `7B / 2S` |
| `0:00 UTC` | `0.3315` | `0.3314` | `0.3315` | `0.3316` | `0.3313` | 521,667.70 USD | 331,816.53 USD | 189,851.17 USD | 141,965.36 USD | `+27.21%` | `14B / 7S` |
| `5:00 UTC` | `0.3313` | `0.3313` | `0.3313` | `0.3314` | `0.3312` | 182,734.27 USD | 70,327.25 USD | 112,407.03 USD | -42,079.78 USD | `-23.03%` | `4B / 3S` |
| `0:00 UTC` | `0.3312` | `0.3312` | `0.3312` | `0.3313` | `0.3312` | 179,833.13 USD | 50,346.37 USD | 129,486.77 USD | -79,140.40 USD | `-44.01%` | `3B / 3S` |
| `5:00 UTC` | `0.3312` | `0.3312` | `0.3312` | `0.3312` | `0.3311` | 145,155.84 USD | 46,671.46 USD | 98,484.38 USD | -51,812.92 USD | `-35.69%` | `2B / 3S` |
| `0:00 UTC` | `0.3312` | `0.3311` | `0.3312` | `0.3312` | `0.3310` | 301,237.68 USD | 114,043.04 USD | 187,194.64 USD | -73,151.60 USD | `-24.28%` | `3B / 9S` |
| `5:00 UTC` | `0.3312` | `0.3311` | `0.3312` | `0.3312` | `0.3311` | 209,738.14 USD | 96,085.33 USD | 113,652.81 USD | -17,567.48 USD | `-8.38%` | `4B / 10S` |
| `0:00 UTC` | `0.3313` | `0.3313` | `0.3313` | `0.3313` | `0.3311` | 324,753.86 USD | 187,135.24 USD | 137,618.62 USD | 49,516.62 USD | `+15.25%` | `5B / 7S` |
| `5:00 UTC` | `0.3313` | `0.3312` | `0.3313` | `0.3313` | `0.3311` | 257,613.17 USD | 129,803.39 USD | 127,809.78 USD | 1,993.62 USD | `+0.77%` | `7B / 11S` |
| `0:00 UTC` | `0.3312` | `0.3312` | `0.3312` | `0.3312` | `0.3312` | 22,669.52 USD | 5,477.88 USD | 17,191.64 USD | -11,713.76 USD | `-51.67%` | `0B / 0S` |

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
| `5m` | -37,760.00 USD | -41,300.00 USD | **`DISTRIBUTION`** |
| `15m` | -47,800.00 USD | -50,990.00 USD | **`DISTRIBUTION`** |
| `30m` | -43,330.00 USD | 7,780.00 USD | **`DISTRIBUTION`** |
| `1h` | -31,480.00 USD | 44,640.00 USD | **`ACCUMULATION`** |
| `2h` | 484,970.00 USD | -164,200.00 USD | **`ACCUMULATION`** |
| `4h` | -1,210,000.00 USD | -251,730.00 USD | **`DISTRIBUTION`** |
| `6h` | -62,380.00 USD | 76,900.00 USD | **`ACCUMULATION`** |
| `8h` | 23,190.00 USD | -44,160.00 USD | **`DISTRIBUTION`** |
| `12h` | 250,120.00 USD | 456,960.00 USD | **`ACCUMULATION`** |
| `24h` | 3,370,000.00 USD | 3,020,000.00 USD | **`ACCUMULATION`** |
| `1w` | -4,810,000.00 USD | 1,650,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -23,090,000.00 USD | 2,980,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-37.76K` | 15m=`-47.80K` | 1h=`-31.48K` | 24h=`+3.37M`
* Futures Capital Netflows: 5m=`-41.30K` | 15m=`-50.99K` | 1h=`+44.64K` | 24h=`+3.02M`
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
  * `2026-10-29 23:31:35 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:25:35 IST`: [@DeItaone] - (Sentiment: `Neutral`)
  * `2026-10-29 23:03:35 IST`: [@mb_ghalibaf] - (Sentiment: `Neutral`)
  * `2026-10-29 23:01:35 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-29 22:55:35 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-29 22:45:35 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:31:35 IST`: [fxstreet.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:30:35 IST`: [ForexFactory] - (Sentiment: `Neutral`)
  * `2026-10-29 23:30:35 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-29 23:30:35 IST`: [youtube.com/bankofcanadaofficial] - (Sentiment: `Neutral`)
  * `2026-10-29 23:30:35 IST`: [notayesmanseconomics.wordpress.com] - (Sentiment: `Neutral`)
  * `2026-10-29 20:32:35 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 20:32:35 IST`: [breakingthenews.net] - (Sentiment: `Neutral`)
  * `2026-10-29 20:32:35 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-29 20:32:35 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)


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
  * Execution Entry: `0.3293` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `0.3271` (Risk Distance: `0.0024` pts)
  * +2.5R Take Profit: `0.3353`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `0.3312` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `0.3334` (Risk Distance: `0.0024` pts)
  * +2.5R Take Profit: `0.3252`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`0.3337`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
