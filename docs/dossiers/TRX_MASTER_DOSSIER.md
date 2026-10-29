# 🏛️ SOVEREIGN CANDIDATE DOSSIER: TRX
**Canonical Key**: `TRX` | **Broker Instrument**: `TRXUSD.p` | **Asset Class**: `Crypto Alt L1`
**Timestamp**: `2026-10-29 22:52:02 IST` (`2026-10-29 17:22:02 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `0.3306` | **Live Ask Quote**: `0.3317` | **Mid Price**: `0.3311`
- **Spread Points**: `11.00` | **Spread BPS**: `33.22 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `0.3302` | VWAP Z-Score: `+0.52` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `0.000367` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `46.96` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `0.3326` | Lower -3.00σ Band: `0.3278`
  * Upper +2.51σ Band: `0.3322` | Lower -2.51σ Band: `0.3282`
  * Upper +2.01σ Band: `0.3318` | Lower -2.01σ Band: `0.3286`
  * Upper +2.00σ Band: `0.3318` | Lower -2.00σ Band: `0.3286`
  * Upper +1.28σ Band: `0.3312` | Lower -1.28σ Band: `0.3292`
  * Upper +1.00σ Band: `0.3310` | Lower -1.00σ Band: `0.3294`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`0.3307` | EMA-20=`0.3307` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`0.3306` (Slope: `+0.0000`) | EMA-100=`0.3304`
  * Institutional Anchors: EMA-144=`0.3302` | EMA-200=`0.3299` (Slope: `+0.0299`) | EMA-233=`0.3299`
- **Range Boundaries**: 24H High=`0.3313` | 24H Low=`0.3285` | Weekly High=`0.3319` | Weekly Low=`0.3266`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `0.3312` (Distance: `-0.02%`)
  * Point of Control (POC) = `0.3307` (Distance: `+0.14%`)
  * Value Area Low (VAL) = `0.3293` (Distance: `+0.58%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BULLISH (Above Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`0.3314` | POC=`0.3309` | VAL=`0.3304`
  * Prior Day Extremes: PDH=`0.3319` | PDL=`0.3288` | PDC=`0.3289`
  * Monday Range Blueprint: High=`0.3310` | Mid=`0.3300` | Low=`0.3289`
  * Developing Weekly Value Area: Weekly VAH=`0.3312` | Weekly POC=`0.3307` | Weekly VAL=`0.3289`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`0.3306` | Low=`0.3285`
  * London Session (08:00-16:00 UTC): High=`0.3311` | Low=`0.3303`
  * New York Session (13:00-21:00 UTC): High=`0.3313` | Low=`0.3301`
  * Initial Balance (First Hour): IB High=`0.3311` | IB Low=`0.3303`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `0.3298` - `0.3325`
  * Optimal Trade Entry (OTE 0.705): `0.3318`
  * Structural Invalidation Anchor (0.786): `0.3338`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `0.3311` | `0.3312` | `0.3311` | `0.3312` | `151,637` | 50,215.17 USD | 29,423.39 USD | `+58.59%` | 2,439,060.76 USD | `+0.69` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `5m` | `0.3312` | `0.3312` | `0.3310` | `0.3311` | `568,873` | 188,354.13 USD | -89,145.63 USD | `-47.33%` | 2,349,915.13 USD | `-1.96` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `5m` | `0.3311` | `0.3312` | `0.3311` | `0.3311` | `140,492` | 46,516.46 USD | -2,198.48 USD | `-4.73%` | 2,347,716.64 USD | `-0.00` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `15m` | `0.3313` | `0.3313` | `0.3312` | `0.3312` | `542,963` | 179,833.13 USD | -79,140.40 USD | `-44.01%` | 2,461,450.28 USD | `-0.81` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `0.3312` | `0.3312` | `0.3311` | `0.3311` | `438,344` | 145,155.84 USD | -51,812.92 USD | `-35.69%` | 2,409,637.37 USD | `-0.55` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `0.3311` | `0.3312` | `0.3310` | `0.3311` | `861,002` | 285,085.76 USD | -61,920.72 USD | `-21.72%` | 2,347,716.64 USD | `-0.60` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `0.3311` | `0.3315` | `0.3311` | `0.3314` | `2,995,760` | 992,405.40 USD | 52,187.57 USD | `+5.26%` | 2,115,366.31 USD | `-0.30` | **`BULLISH`** | `DELTA ALIGNED` |
| `1h` | `0.3314` | `0.3316` | `0.3311` | `0.3311` | `3,106,966` | 1,029,390.94 USD | -31,067.74 USD | `-3.02%` | 2,084,298.57 USD | `-0.64` | **`BEARISH`** | `NEUTRAL CHOP` |
| `1h` | `0.3311` | `0.3312` | `0.3310` | `0.3312` | `861,058` | 285,104.31 USD | -61,902.18 USD | `-21.71%` | 2,022,396.39 USD | `-0.72` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.3311` | `0.3316` | `0.3311` | `0.3315` | `11,939,433` | 3,956,492.73 USD | 16,254.19 USD | `+0.41%` | 2,010,591.01 USD | `-1.70` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `0.3315` | `0.3318` | `0.3306` | `0.3314` | `23,511,075` | 7,789,850.35 USD | 369,308.17 USD | `+4.74%` | 2,379,899.18 USD | `-0.41` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `0.3314` | `0.3316` | `0.3310` | `0.3311` | `3,967,968` | 1,314,476.70 USD | -92,988.46 USD | `-7.07%` | 2,286,910.72 USD | `-1.49` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.3296` | `0.3308` | `0.3290` | `0.3307` | `23,140,787` | 7,631,473.08 USD | 600,887.06 USD | `+7.87%` | 1,347,651.40 USD | `-1.00` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `0.3307` | `0.3316` | `0.3306` | `0.3311` | `18,393,472` | 6,092,518.66 USD | 646,685.42 USD | `+10.61%` | 1,994,336.82 USD | `-0.30` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `0.3311` | `0.3316` | `0.3311` | `0.3315` | `11,939,433` | 3,956,492.73 USD | 16,254.19 USD | `+0.41%` | 2,010,591.01 USD | `-1.70` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `0.3315` | `0.3318` | `0.3306` | `0.3314` | `23,511,075` | 7,789,850.35 USD | 369,308.17 USD | `+4.74%` | 2,379,899.18 USD | `-0.41` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `0.3314` | `0.3316` | `0.3310` | `0.3311` | `3,967,968` | 1,314,476.70 USD | -92,988.46 USD | `-7.07%` | 2,286,910.72 USD | `-1.49` | **`BEARISH`** | `DELTA ALIGNED` |

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
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-29 22:44:58 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `1678` | `0xeadc...9d55` | `LONG` | 1,325,240.00 USD | `4,000,000.00` | `0.3421` | `0.3314` | `0.000000` | -43,238.09 USD | `-3.26%` | `10X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `0.3301` | 8,066.50 USD | `-` | `NEWS_INTEL` | `-` | #TRX Whale SELL: 8.07K USD at 0.3301 USD [API] | `2026-10-27 20:00:26` |
| `ANNOUNCEMENT` | `INFO` | `0.3314` | 5,097.11 USD | `-` | `NEWS_INTEL` | `-` | #TRX Whale SELL: 5.10K USD at 0.3314 USD [API] | `2026-10-27 20:57:45` |
| `ANNOUNCEMENT` | `INFO` | `0.3314` | 8,099.73 USD | `-` | `NEWS_INTEL` | `-` | #TRX Whale SELL: 8.10K USD at 0.3314 USD [API] | `2026-10-27 20:58:48` |
| `ANNOUNCEMENT` | `INFO` | `0.3315` | 8,100.46 USD | `-` | `NEWS_INTEL` | `-` | #TRX Whale SELL: 8.10K USD at 0.3315 USD [API] | `2026-10-27 21:38:06` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`0.3380` (Vol: 384,800.00 USD, Dist: `+2.06%`) | Long MP=`0.3248` (Vol: 434,200.00 USD, Dist: `--1.93%`)
  * 48H Horizon: Short MP=`0.3382` (Vol: 549,200.00 USD, Dist: `+2.11%`) | Long MP=`0.3250` (Vol: 549,200.00 USD, Dist: `--1.89%`)
  * 3D Horizon: Short MP=`0.3383` (Vol: 512,000.00 USD, Dist: `+2.14%`) | Long MP=`0.3250` (Vol: 602,700.00 USD, Dist: `--1.88%`)
  * 7D Horizon: Short MP=`0.3381` (Vol: 606,000.00 USD, Dist: `+2.07%`) | Long MP=`0.3250` (Vol: 663,500.00 USD, Dist: `--1.88%`)
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
| `7D` | `Long Liquidation` | `0.2979` | 12,950,000.00 USD | 12,950,000.00 USD | 65,800.00 USD | 8,600.00 USD | 10,570.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.2983` | 2,960,000.00 USD | 2,960,000.00 USD | 80,870.00 USD | 15,850.00 USD | 26,180.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.2983` | 12,870,000.00 USD | 12,870,000.00 USD | 99,280.00 USD | 9,990.00 USD | 27,500.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.2987` | 2,840,000.00 USD | 2,840,000.00 USD | 44,390.00 USD | 4,220.00 USD | 2,890.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.2987` | 12,730,000.00 USD | 12,730,000.00 USD | 76,610.00 USD | 9,860.00 USD | 6,170.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.2991` | 12,640,000.00 USD | 12,640,000.00 USD | 23,720.00 USD | 6,910.00 USD | 3,870.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.2995` | 127.89 USD | 129,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3005` | 7,130.00 USD | 129,610.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3015` | 10,330.00 USD | 122,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3025` | 694.54 USD | 112,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3035` | 942.06 USD | 111,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3045` | 5,290.00 USD | 110,520.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.3051` | 12,600,000.00 USD | 12,600,000.00 USD | 380.73 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3055` | 12,600,000.00 USD | 12,600,000.00 USD | 1,380.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3055` | 5,300.00 USD | 105,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.3059` | 12,600,000.00 USD | 12,600,000.00 USD | 212.37 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3063` | 12,600,000.00 USD | 12,600,000.00 USD | 1,990.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3065` | 14,720.00 USD | 99,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3067` | 2,790,000.00 USD | 2,790,000.00 USD | 57.95 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3067` | 12,600,000.00 USD | 12,600,000.00 USD | 5,660.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3071` | 2,790,000.00 USD | 2,790,000.00 USD | 2,980.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3071` | 12,590,000.00 USD | 12,590,000.00 USD | 6,280.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3075` | 2,780,000.00 USD | 2,780,000.00 USD | 1,410.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3075` | 12,590,000.00 USD | 12,590,000.00 USD | 2,850.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3079` | 2,780,000.00 USD | 2,780,000.00 USD | 135.83 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3079` | 12,580,000.00 USD | 12,580,000.00 USD | 2,180.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3083` | 2,780,000.00 USD | 2,780,000.00 USD | 221.36 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3083` | 12,580,000.00 USD | 12,580,000.00 USD | 1,200.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3085` | 6,670.00 USD | 85,200.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3087` | 2,780,000.00 USD | 2,780,000.00 USD | 506.09 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3087` | 12,580,000.00 USD | 12,580,000.00 USD | 1,860.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3091` | 2,780,000.00 USD | 2,780,000.00 USD | 61.02 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3091` | 12,580,000.00 USD | 12,580,000.00 USD | 1,320.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3107` | 12,580,000.00 USD | 12,580,000.00 USD | 1,790.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3111` | 12,580,000.00 USD | 12,580,000.00 USD | 554.30 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3115` | 12,580,000.00 USD | 12,580,000.00 USD | 283.30 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3115` | 824.85 USD | 78,540.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.3119` | 12,570,000.00 USD | 12,570,000.00 USD | 2,650.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3123` | 2,780,000.00 USD | 2,780,000.00 USD | 77.30 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3123` | 12,570,000.00 USD | 12,570,000.00 USD | 7,550.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3125` | 17,140.00 USD | 77,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3127` | 2,780,000.00 USD | 2,780,000.00 USD | 3,970.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3127` | 12,560,000.00 USD | 12,560,000.00 USD | 8,380.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3131` | 2,780,000.00 USD | 2,780,000.00 USD | 1,880.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3131` | 12,560,000.00 USD | 12,560,000.00 USD | 3,800.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3135` | 2,780,000.00 USD | 2,780,000.00 USD | 181.20 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3135` | 12,550,000.00 USD | 12,550,000.00 USD | 2,910.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3135` | 44,390.00 USD | 60,570.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3139` | 2,780,000.00 USD | 2,780,000.00 USD | 295.30 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3139` | 12,550,000.00 USD | 12,550,000.00 USD | 1,600.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3143` | 2,770,000.00 USD | 2,770,000.00 USD | 429.90 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3143` | 12,550,000.00 USD | 12,550,000.00 USD | 183,810.00 USD | 34,890.00 USD | 11,170.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3145` | 2,140.00 USD | 16,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3147` | 2,770,000.00 USD | 2,770,000.00 USD | 326.60 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3147` | 12,320,000.00 USD | 12,320,000.00 USD | 170,840.00 USD | 16,380.00 USD | 21,590.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3151` | 12,110,000.00 USD | 12,110,000.00 USD | 187,500.00 USD | 29,590.00 USD | 61,120.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3155` | 11,830,000.00 USD | 11,830,000.00 USD | 157,220.00 USD | 40,480.00 USD | 22,590.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3155` | 142.29 USD | 14,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3159` | 2,770,000.00 USD | 2,770,000.00 USD | 5,750.00 USD | 5,600.00 USD | 27,350.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3159` | 11,610,000.00 USD | 11,610,000.00 USD | 353,770.00 USD | 101,710.00 USD | 112,500.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3163` | 2,740,000.00 USD | 2,740,000.00 USD | 98,530.00 USD | 32,280.00 USD | 30,960.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3163` | 11,040,000.00 USD | 11,040,000.00 USD | 225,120.00 USD | 116,130.00 USD | 134,250.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3165` | 1,490.00 USD | 13,890.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3167` | 2,570,000.00 USD | 2,570,000.00 USD | 50,820.00 USD | 14,920.00 USD | 20,330.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3167` | 10,570,000.00 USD | 10,570,000.00 USD | 328,930.00 USD | 75,090.00 USD | 95,630.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3171` | 2,490,000.00 USD | 2,490,000.00 USD | 7,710.00 USD | 13,460.00 USD | 9,490.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3171` | 10,070,000.00 USD | 10,070,000.00 USD | 293,450.00 USD | 89,970.00 USD | 96,960.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3175` | 2,460,000.00 USD | 2,460,000.00 USD | 16,390.00 USD | 5,630.00 USD | 3,360.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3175` | 9,590,000.00 USD | 9,590,000.00 USD | 28,570.00 USD | 12,370.00 USD | 39,210.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3175` | 1,400.00 USD | 12,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3179` | 2,430,000.00 USD | 2,430,000.00 USD | 39,170.00 USD | 19,460.00 USD | 25,060.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3179` | 9,510,000.00 USD | 9,510,000.00 USD | 231,050.00 USD | 33,640.00 USD | 39,970.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3183` | 2,350,000.00 USD | 2,350,000.00 USD | 362,180.00 USD | 45,610.00 USD | 64,720.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3183` | 9,200,000.00 USD | 9,200,000.00 USD | 477,670.00 USD | 49,030.00 USD | 70,140.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3187` | 1,880,000.00 USD | 1,880,000.00 USD | 23,690.00 USD | 2,240.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3187` | 8,610,000.00 USD | 8,610,000.00 USD | 117,850.00 USD | 29,330.00 USD | 11,120.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3191` | 8,450,000.00 USD | 8,450,000.00 USD | 59,160.00 USD | 13,950.00 USD | 11,780.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3207` | 8,360,000.00 USD | 8,360,000.00 USD | 158,770.00 USD | 34,380.00 USD | 7,770.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3211` | 8,160,000.00 USD | 8,160,000.00 USD | 403,080.00 USD | 68,150.00 USD | 57,740.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3215` | 7,630,000.00 USD | 7,630,000.00 USD | 413,850.00 USD | 47,610.00 USD | 100,600.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3219` | 7,070,000.00 USD | 7,070,000.00 USD | 324,100.00 USD | 67,660.00 USD | 63,030.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3223` | 1,850,000.00 USD | 1,850,000.00 USD | 0.00 USD | 0.00 USD | 20,260.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3223` | 6,620,000.00 USD | 6,620,000.00 USD | 435,620.00 USD | 137,210.00 USD | 89,860.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3227` | 1,830,000.00 USD | 1,830,000.00 USD | 101,660.00 USD | 43,840.00 USD | 51,780.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3227` | 5,950,000.00 USD | 5,950,000.00 USD | 638,380.00 USD | 208,030.00 USD | 227,150.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3231` | 1,630,000.00 USD | 1,630,000.00 USD | 161,500.00 USD | 49,860.00 USD | 72,280.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3231` | 4,880,000.00 USD | 4,880,000.00 USD | 589,500.00 USD | 180,670.00 USD | 295,130.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3235` | 1,350,000.00 USD | 1,350,000.00 USD | 54,750.00 USD | 32,080.00 USD | 31,960.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3235` | 3,810,000.00 USD | 3,810,000.00 USD | 507,910.00 USD | 168,260.00 USD | 205,040.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3235` | 11,000.00 USD | 11,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3239` | 1,230,000.00 USD | 1,230,000.00 USD | 15,020.00 USD | 10,730.00 USD | 3,870.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3239` | 2,930,000.00 USD | 2,930,000.00 USD | 354,650.00 USD | 119,100.00 USD | 114,090.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3243` | 1,200,000.00 USD | 1,200,000.00 USD | 80,740.00 USD | 20,910.00 USD | 19,290.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3243` | 2,350,000.00 USD | 2,350,000.00 USD | 265,190.00 USD | 39,180.00 USD | 42,580.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3247` | 1,080,000.00 USD | 1,080,000.00 USD | 189,030.00 USD | 68,180.00 USD | 113,670.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3247` | 2,000,000.00 USD | 2,000,000.00 USD | 559,960.00 USD | 72,190.00 USD | 145,960.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3251` | 708,010.00 USD | 708,010.00 USD | 585,700.00 USD | 52,790.00 USD | 49,450.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3251` | 1,220,000.00 USD | 1,220,000.00 USD | 667,020.00 USD | 65,250.00 USD | 61,340.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3255` | 20,070.00 USD | 20,070.00 USD | 20,070.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3255` | 426,520.00 USD | 426,520.00 USD | 251,380.00 USD | 60,580.00 USD | 35,520.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3259` | 79,040.00 USD | 79,040.00 USD | 51,940.00 USD | 16,810.00 USD | 10,280.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3339` | 455,400.00 USD | 455,400.00 USD | 363,280.00 USD | 69,780.00 USD | 22,330.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3343` | 729,900.00 USD | 729,900.00 USD | 198,570.00 USD | 32,750.00 USD | 43,180.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3347` | 1,290,000.00 USD | 1,290,000.00 USD | 413,850.00 USD | 47,610.00 USD | 100,600.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3351` | 1,750,000.00 USD | 1,750,000.00 USD | 324,100.00 USD | 67,660.00 USD | 63,030.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3355` | 20,260.00 USD | 20,260.00 USD | 0.00 USD | 0.00 USD | 20,260.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3355` | 2,410,000.00 USD | 2,410,000.00 USD | 435,620.00 USD | 137,210.00 USD | 89,860.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3359` | 217,540.00 USD | 217,540.00 USD | 101,660.00 USD | 43,840.00 USD | 51,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3359` | 3,480,000.00 USD | 3,480,000.00 USD | 638,380.00 USD | 208,030.00 USD | 227,150.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3363` | 501,180.00 USD | 501,180.00 USD | 161,500.00 USD | 49,860.00 USD | 72,280.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3363` | 4,550,000.00 USD | 4,550,000.00 USD | 589,500.00 USD | 180,670.00 USD | 295,130.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3367` | 619,960.00 USD | 619,960.00 USD | 54,750.00 USD | 32,080.00 USD | 31,960.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3367` | 5,430,000.00 USD | 5,430,000.00 USD | 507,910.00 USD | 168,260.00 USD | 205,040.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3371` | 649,590.00 USD | 649,590.00 USD | 15,020.00 USD | 10,730.00 USD | 3,870.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3371` | 6,020,000.00 USD | 6,020,000.00 USD | 354,650.00 USD | 119,100.00 USD | 114,090.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3375` | 770,530.00 USD | 770,530.00 USD | 80,740.00 USD | 20,910.00 USD | 19,290.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3375` | 6,360,000.00 USD | 6,360,000.00 USD | 265,190.00 USD | 39,180.00 USD | 42,580.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3379` | 1,140,000.00 USD | 1,140,000.00 USD | 189,030.00 USD | 68,180.00 USD | 113,670.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3379` | 7,140,000.00 USD | 7,140,000.00 USD | 559,960.00 USD | 72,190.00 USD | 145,960.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3383` | 1,830,000.00 USD | 1,830,000.00 USD | 585,700.00 USD | 52,790.00 USD | 49,450.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3383` | 7,940,000.00 USD | 7,940,000.00 USD | 667,020.00 USD | 65,250.00 USD | 61,340.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3387` | 1,850,000.00 USD | 1,850,000.00 USD | 20,070.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3387` | 8,280,000.00 USD | 8,280,000.00 USD | 251,380.00 USD | 60,580.00 USD | 35,520.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3391` | 8,360,000.00 USD | 8,360,000.00 USD | 51,940.00 USD | 16,810.00 USD | 10,280.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3403` | 8,460,000.00 USD | 8,460,000.00 USD | 79,380.00 USD | 17,190.00 USD | 3,890.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3407` | 8,670,000.00 USD | 8,670,000.00 USD | 162,870.00 USD | 34,080.00 USD | 13,980.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3411` | 8,990,000.00 USD | 8,990,000.00 USD | 236,810.00 USD | 19,270.00 USD | 60,150.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3415` | 9,120,000.00 USD | 9,120,000.00 USD | 75,860.00 USD | 24,680.00 USD | 30,770.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3419` | 9,350,000.00 USD | 9,350,000.00 USD | 162,450.00 USD | 45,810.00 USD | 19,490.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3423` | 1,890,000.00 USD | 1,890,000.00 USD | 5,750.00 USD | 5,600.00 USD | 27,350.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3423` | 9,860,000.00 USD | 9,860,000.00 USD | 331,520.00 USD | 82,020.00 USD | 100,690.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3425` | 456.55 USD | 456.55 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.3427` | 2,050,000.00 USD | 2,050,000.00 USD | 98,530.00 USD | 32,280.00 USD | 30,960.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3427` | 10,340,000.00 USD | 10,340,000.00 USD | 225,120.00 USD | 116,130.00 USD | 134,250.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3431` | 2,140,000.00 USD | 2,140,000.00 USD | 50,820.00 USD | 14,920.00 USD | 20,330.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3431` | 10,840,000.00 USD | 10,840,000.00 USD | 328,930.00 USD | 75,090.00 USD | 95,630.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3435` | 2,170,000.00 USD | 2,170,000.00 USD | 7,710.00 USD | 13,460.00 USD | 9,490.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3435` | 11,320,000.00 USD | 11,320,000.00 USD | 295,240.00 USD | 89,970.00 USD | 96,960.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3435` | 153.89 USD | 610.44 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.3439` | 2,190,000.00 USD | 2,190,000.00 USD | 16,390.00 USD | 5,630.00 USD | 3,360.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3439` | 11,400,000.00 USD | 11,400,000.00 USD | 29,120.00 USD | 12,370.00 USD | 39,210.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3443` | 2,280,000.00 USD | 2,280,000.00 USD | 39,170.00 USD | 19,460.00 USD | 25,060.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3443` | 11,710,000.00 USD | 11,710,000.00 USD | 231,330.00 USD | 33,640.00 USD | 39,970.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3445` | 5,290.00 USD | 5,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.3447` | 2,600,000.00 USD | 2,600,000.00 USD | 235,910.00 USD | 35,600.00 USD | 54,570.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3447` | 12,110,000.00 USD | 12,110,000.00 USD | 310,260.00 USD | 31,970.00 USD | 56,490.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3451` | 2,770,000.00 USD | 2,770,000.00 USD | 150,040.00 USD | 12,250.00 USD | 10,150.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3451` | 12,400,000.00 USD | 12,400,000.00 USD | 245,650.00 USD | 26,900.00 USD | 20,240.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3455` | 2,780,000.00 USD | 2,780,000.00 USD | 1,320.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3455` | 12,550,000.00 USD | 12,550,000.00 USD | 97,690.00 USD | 33,430.00 USD | 16,310.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3455` | 486.46 USD | 6,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.3459` | 2,780,000.00 USD | 2,780,000.00 USD | 4,260.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3459` | 12,570,000.00 USD | 12,570,000.00 USD | 22,340.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3463` | 2,780,000.00 USD | 2,780,000.00 USD | 397.30 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3463` | 12,570,000.00 USD | 12,570,000.00 USD | 3,330.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3467` | 2,780,000.00 USD | 2,780,000.00 USD | 57.70 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3467` | 12,570,000.00 USD | 12,570,000.00 USD | 1,130.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3471` | 2,780,000.00 USD | 2,780,000.00 USD | 307.20 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3471` | 12,570,000.00 USD | 12,570,000.00 USD | 1,500.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3475` | 2,780,000.00 USD | 2,780,000.00 USD | 663.20 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3475` | 12,580,000.00 USD | 12,580,000.00 USD | 2,180.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3475` | 10,210.00 USD | 16,590.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.3479` | 2,780,000.00 USD | 2,780,000.00 USD | 81.40 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3479` | 12,580,000.00 USD | 12,580,000.00 USD | 1,770.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3485` | 223.04 USD | 16,820.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.3491` | 12,580,000.00 USD | 12,580,000.00 USD | 1,340.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3495` | 12,580,000.00 USD | 12,580,000.00 USD | 415.52 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3499` | 12,580,000.00 USD | 12,580,000.00 USD | 212.37 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3503` | 12,580,000.00 USD | 12,580,000.00 USD | 1,990.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3505` | 177,540.00 USD | 194,350.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.3507` | 2,780,000.00 USD | 2,780,000.00 USD | 57.95 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3507` | 12,590,000.00 USD | 12,590,000.00 USD | 5,660.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3511` | 2,780,000.00 USD | 2,780,000.00 USD | 1,880.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3511` | 12,590,000.00 USD | 12,590,000.00 USD | 4,590.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3515` | 2,790,000.00 USD | 2,790,000.00 USD | 2,300.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3515` | 12,600,000.00 USD | 12,600,000.00 USD | 3,690.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3519` | 2,790,000.00 USD | 2,790,000.00 USD | 297.83 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3519` | 12,600,000.00 USD | 12,600,000.00 USD | 2,490.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3523` | 2,790,000.00 USD | 2,790,000.00 USD | 43.25 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3523` | 12,600,000.00 USD | 12,600,000.00 USD | 846.39 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3527` | 2,790,000.00 USD | 2,790,000.00 USD | 221.36 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3527` | 12,600,000.00 USD | 12,600,000.00 USD | 1,120.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3531` | 2,790,000.00 USD | 2,790,000.00 USD | 506.09 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3531` | 12,600,000.00 USD | 12,600,000.00 USD | 1,640.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3535` | 2,790,000.00 USD | 2,790,000.00 USD | 61.02 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3535` | 12,600,000.00 USD | 12,600,000.00 USD | 1,320.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3535` | 223.06 USD | 194,580.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3555` | 5,510.00 USD | 200,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.3599` | 12,630,000.00 USD | 12,630,000.00 USD | 18,580.00 USD | 6,010.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3603` | 12,690,000.00 USD | 12,690,000.00 USD | 48,320.00 USD | 6,290.00 USD | 2,910.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3607` | 12,750,000.00 USD | 12,750,000.00 USD | 52,620.00 USD | 4,710.00 USD | 6,550.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3611` | 12,800,000.00 USD | 12,800,000.00 USD | 35,490.00 USD | 4,040.00 USD | 14,500.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3615` | 12,880,000.00 USD | 12,880,000.00 USD | 61,190.00 USD | 9,240.00 USD | 1,960.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3619` | 2,790,000.00 USD | 2,790,000.00 USD | 501.40 USD | 654.45 USD | 5,890.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3619` | 13,010,000.00 USD | 13,010,000.00 USD | 82,550.00 USD | 20,630.00 USD | 33,010.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3623` | 2,840,000.00 USD | 2,840,000.00 USD | 24,780.00 USD | 8,270.00 USD | 8,880.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3623` | 13,170,000.00 USD | 13,170,000.00 USD | 89,280.00 USD | 33,600.00 USD | 36,370.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3627` | 2,870,000.00 USD | 2,870,000.00 USD | 15,110.00 USD | 5,590.00 USD | 9,070.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3627` | 13,300,000.00 USD | 13,300,000.00 USD | 77,830.00 USD | 18,040.00 USD | 36,410.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3631` | 2,880,000.00 USD | 2,880,000.00 USD | 7,150.00 USD | 4,680.00 USD | 5,260.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3631` | 13,430,000.00 USD | 13,430,000.00 USD | 76,220.00 USD | 25,590.00 USD | 26,610.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3635` | 2,880,000.00 USD | 2,880,000.00 USD | 147.65 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3635` | 13,500,000.00 USD | 13,500,000.00 USD | 44,080.00 USD | 16,220.00 USD | 6,560.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3639` | 2,900,000.00 USD | 2,900,000.00 USD | 9,160.00 USD | 2,950.00 USD | 2,470.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3639` | 13,540,000.00 USD | 13,540,000.00 USD | 24,540.00 USD | 2,960.00 USD | 9,300.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3643` | 2,940,000.00 USD | 2,940,000.00 USD | 19,870.00 USD | 6,710.00 USD | 14,160.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3643` | 13,650,000.00 USD | 13,650,000.00 USD | 89,610.00 USD | 8,430.00 USD | 14,840.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3645` | 376.53 USD | 200,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.3647` | 3,060,000.00 USD | 3,060,000.00 USD | 98,340.00 USD | 11,560.00 USD | 14,430.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3647` | 13,740,000.00 USD | 13,740,000.00 USD | 66,060.00 USD | 11,120.00 USD | 17,470.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3648` | 3,070,000.00 USD | 3,070,000.00 USD | 4,900.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3651` | 13,810,000.00 USD | 13,810,000.00 USD | 60,980.00 USD | 4,810.00 USD | 2,640.00 USD | `Tier 1 CEX` |
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
| `Live` | `Long` | `0.0685` | 503,290.00 USD | 0.00 USD | 8,780.00 USD | `-79.33%` | `128,233.00` |
| `Live` | `Long` | `0.0705` | 494,510.00 USD | 0.00 USD | 482.64 USD | `-78.73%` | `6,846.00` |
| `Live` | `Long` | `0.0825` | 494,030.00 USD | 0.00 USD | 1,050.00 USD | `-75.11%` | `12,781.00` |
| `Live` | `Long` | `0.1035` | 492,970.00 USD | 0.00 USD | 4,090.00 USD | `-68.77%` | `39,551.00` |
| `Live` | `Long` | `0.1075` | 488,880.00 USD | 0.00 USD | 23,520.00 USD | `-67.56%` | `218,745.00` |
| `Live` | `Long` | `0.1095` | 465,360.00 USD | 0.00 USD | 4,580.00 USD | `-66.96%` | `41,871.00` |
| `Live` | `Long` | `0.1115` | 460,780.00 USD | 0.00 USD | 531.74 USD | `-66.35%` | `4,769.00` |
| `Live` | `Long` | `0.1155` | 460,250.00 USD | 0.00 USD | 881.38 USD | `-65.15%` | `7,631.00` |
| `Live` | `Long` | `0.1175` | 459,370.00 USD | 0.00 USD | 394.80 USD | `-64.54%` | `3,360.00` |
| `Live` | `Long` | `0.1325` | 458,970.00 USD | 0.00 USD | 119.78 USD | `-60.02%` | `904.00` |
| `Live` | `Long` | `0.1345` | 458,850.00 USD | 0.00 USD | 1,530.00 USD | `-59.41%` | `11,352.00` |
| `Live` | `Long` | `0.1405` | 457,330.00 USD | 0.00 USD | 429.65 USD | `-57.60%` | `3,058.00` |
| `Live` | `Long` | `0.1535` | 456,900.00 USD | 0.00 USD | 463.72 USD | `-53.68%` | `3,021.00` |
| `Live` | `Long` | `0.1575` | 456,430.00 USD | 0.00 USD | 394.06 USD | `-52.47%` | `2,502.00` |
| `Live` | `Long` | `0.1595` | 456,040.00 USD | 0.00 USD | 390.46 USD | `-51.87%` | `2,448.00` |
| `Live` | `Long` | `0.1695` | 455,650.00 USD | 0.00 USD | 13,020.00 USD | `-48.85%` | `76,797.00` |
| `Live` | `Long` | `0.1705` | 442,630.00 USD | 0.00 USD | 20,360.00 USD | `-48.55%` | `119,400.00` |
| `Live` | `Long` | `0.1715` | 422,270.00 USD | 0.00 USD | 3,430.00 USD | `-48.25%` | `20,000.00` |
| `Live` | `Long` | `0.1735` | 418,840.00 USD | 0.00 USD | 11,160.00 USD | `-47.65%` | `64,322.00` |
| `Live` | `Long` | `0.1745` | 407,680.00 USD | 0.00 USD | 471.50 USD | `-47.34%` | `2,702.00` |
| `Live` | `Long` | `0.1755` | 407,210.00 USD | 0.00 USD | 2,390.00 USD | `-47.04%` | `13,619.00` |
| `Live` | `Long` | `0.1765` | 404,820.00 USD | 0.00 USD | 4,200.00 USD | `-46.74%` | `23,777.00` |
| `Live` | `Long` | `0.1775` | 400,620.00 USD | 0.00 USD | 433.81 USD | `-46.44%` | `2,444.00` |
| `Live` | `Long` | `0.1795` | 400,190.00 USD | 0.00 USD | 209.84 USD | `-45.84%` | `1,169.00` |
| `Live` | `Long` | `0.1895` | 399,980.00 USD | 0.00 USD | 1,350.00 USD | `-42.82%` | `7,104.00` |
| `Live` | `Long` | `0.1965` | 398,630.00 USD | 0.00 USD | 3,560.00 USD | `-40.71%` | `18,121.00` |
| `Live` | `Long` | `0.2045` | 395,070.00 USD | 0.00 USD | 6,130.00 USD | `-38.29%` | `30,000.00` |
| `Live` | `Long` | `0.2145` | 388,940.00 USD | 0.00 USD | 3,330.00 USD | `-35.27%` | `15,528.00` |
| `Live` | `Long` | `0.2175` | 385,610.00 USD | 0.00 USD | 1,520.00 USD | `-34.37%` | `7,003.00` |
| `Live` | `Long` | `0.2195` | 384,090.00 USD | 0.00 USD | 515.17 USD | `-33.76%` | `2,347.00` |
| `Live` | `Long` | `0.2225` | 383,570.00 USD | 0.00 USD | 272.79 USD | `-32.86%` | `1,226.00` |
| `Live` | `Long` | `0.2255` | 383,300.00 USD | 0.00 USD | 4,590.00 USD | `-31.95%` | `20,360.00` |
| `Live` | `Long` | `0.2265` | 378,710.00 USD | 0.00 USD | 2,390.00 USD | `-31.65%` | `10,560.00` |
| `Live` | `Long` | `0.2275` | 376,310.00 USD | 0.00 USD | 266.63 USD | `-31.35%` | `1,172.00` |
| `Live` | `Long` | `0.2305` | 376,050.00 USD | 0.00 USD | 4,180.00 USD | `-30.45%` | `18,150.00` |
| `Live` | `Long` | `0.2315` | 371,860.00 USD | 0.00 USD | 2,730.00 USD | `-30.14%` | `11,792.00` |
| `Live` | `Long` | `0.2325` | 369,130.00 USD | 0.00 USD | 308.30 USD | `-29.84%` | `1,326.00` |
| `Live` | `Long` | `0.2335` | 368,830.00 USD | 0.00 USD | 2,690.00 USD | `-29.54%` | `11,520.00` |
| `Live` | `Long` | `0.2345` | 366,140.00 USD | 0.00 USD | 1,060.00 USD | `-29.24%` | `4,522.00` |
| `Live` | `Long` | `0.2355` | 365,080.00 USD | 0.00 USD | 6,140.00 USD | `-28.94%` | `26,082.00` |
| `Live` | `Long` | `0.2365` | 358,930.00 USD | 0.00 USD | 344.11 USD | `-28.64%` | `1,455.00` |
| `Live` | `Long` | `0.2385` | 358,590.00 USD | 0.00 USD | 1,260.00 USD | `-28.03%` | `5,298.00` |
| `Live` | `Long` | `0.2405` | 357,330.00 USD | 0.00 USD | 181.58 USD | `-27.43%` | `755.00` |
| `Live` | `Long` | `0.2445` | 357,140.00 USD | 0.00 USD | 889.49 USD | `-26.22%` | `3,638.00` |
| `Live` | `Long` | `0.2455` | 356,250.00 USD | 0.00 USD | 466.70 USD | `-25.92%` | `1,901.00` |
| `Live` | `Long` | `0.2465` | 355,790.00 USD | 0.00 USD | 276.57 USD | `-25.62%` | `1,122.00` |
| `Live` | `Long` | `0.2475` | 355,510.00 USD | 0.00 USD | 2,420.00 USD | `-25.32%` | `9,797.00` |
| `Live` | `Long` | `0.2565` | 353,090.00 USD | 0.00 USD | 1,230.00 USD | `-22.60%` | `4,794.00` |
| `Live` | `Long` | `0.2585` | 351,860.00 USD | 0.00 USD | 1,580.00 USD | `-22.00%` | `6,097.00` |
| `Live` | `Long` | `0.2595` | 350,280.00 USD | 0.00 USD | 23,040.00 USD | `-21.69%` | `88,790.00` |
| `Live` | `Long` | `0.2605` | 327,240.00 USD | 0.00 USD | 8,940.00 USD | `-21.39%` | `34,333.00` |
| `Live` | `Long` | `0.2615` | 318,300.00 USD | 0.00 USD | 466.78 USD | `-21.09%` | `1,785.00` |
| `Live` | `Long` | `0.2635` | 317,830.00 USD | 0.00 USD | 108.56 USD | `-20.49%` | `412.00` |
| `Live` | `Long` | `0.2655` | 317,720.00 USD | 0.00 USD | 7,520.00 USD | `-19.88%` | `28,325.00` |
| `Live` | `Long` | `0.2665` | 310,200.00 USD | 0.00 USD | 450.92 USD | `-19.58%` | `1,692.00` |
| `Live` | `Long` | `0.2675` | 309,750.00 USD | 0.00 USD | 194.47 USD | `-19.28%` | `727.00` |
| `Live` | `Long` | `0.2685` | 309,550.00 USD | 0.00 USD | 322.74 USD | `-18.98%` | `1,202.00` |
| `Live` | `Long` | `0.2725` | 309,230.00 USD | 0.00 USD | 412.84 USD | `-17.77%` | `1,515.00` |
| `Live` | `Long` | `0.2735` | 308,820.00 USD | 0.00 USD | 5,500.00 USD | `-17.47%` | `20,120.00` |
| `Live` | `Long` | `0.2745` | 303,320.00 USD | 0.00 USD | 40,290.00 USD | `-17.17%` | `146,785.00` |
| `Live` | `Long` | `0.2755` | 263,020.00 USD | 0.00 USD | 84,780.00 USD | `-16.87%` | `307,728.00` |
| `Live` | `Long` | `0.2775` | 178,240.00 USD | 0.00 USD | 487.29 USD | `-16.26%` | `1,756.00` |
| `Live` | `Long` | `0.2785` | 177,760.00 USD | 0.00 USD | 2,130.00 USD | `-15.96%` | `7,634.00` |
| `Live` | `Long` | `0.2795` | 175,630.00 USD | 0.00 USD | 14,450.00 USD | `-15.66%` | `51,684.00` |
| `Live` | `Long` | `0.2805` | 161,190.00 USD | 0.00 USD | 6,280.00 USD | `-15.36%` | `22,380.00` |
| `Live` | `Long` | `0.2815` | 154,910.00 USD | 0.00 USD | 1,310.00 USD | `-15.06%` | `4,642.00` |
| `Live` | `Long` | `0.2825` | 153,600.00 USD | 0.00 USD | 16,640.00 USD | `-14.75%` | `58,893.00` |
| `Live` | `Long` | `0.2835` | 136,960.00 USD | 0.00 USD | 1,430.00 USD | `-14.45%` | `5,038.00` |
| `Live` | `Long` | `0.2865` | 135,540.00 USD | 0.00 USD | 360.42 USD | `-13.55%` | `1,258.00` |
| `Live` | `Long` | `0.2915` | 135,180.00 USD | 0.00 USD | 591.45 USD | `-12.04%` | `2,029.00` |
| `Live` | `Long` | `0.2925` | 134,580.00 USD | 0.00 USD | 957.64 USD | `-11.74%` | `3,274.00` |
| `Live` | `Long` | `0.2945` | 133,630.00 USD | 0.00 USD | 3,760.00 USD | `-11.13%` | `12,780.00` |
| `Live` | `Long` | `0.2955` | 129,860.00 USD | 0.00 USD | 125.29 USD | `-10.83%` | `424.00` |
| `Live` | `Long` | `0.2995` | 129,740.00 USD | 0.00 USD | 127.89 USD | `-9.62%` | `427.00` |
| `Live` | `Long` | `0.3005` | 129,610.00 USD | 0.00 USD | 7,130.00 USD | `-9.32%` | `23,720.00` |
| `Live` | `Long` | `0.3015` | 122,480.00 USD | 0.00 USD | 10,330.00 USD | `-9.02%` | `34,248.00` |
| `Live` | `Long` | `0.3025` | 112,160.00 USD | 0.00 USD | 694.54 USD | `-8.72%` | `2,296.00` |
| `Live` | `Long` | `0.3035` | 111,460.00 USD | 0.00 USD | 942.06 USD | `-8.42%` | `3,104.00` |
| `Live` | `Long` | `0.3045` | 110,520.00 USD | 0.00 USD | 5,290.00 USD | `-8.12%` | `17,387.00` |
| `Live` | `Long` | `0.3055` | 105,220.00 USD | 0.00 USD | 5,300.00 USD | `-7.81%` | `17,354.00` |
| `Live` | `Long` | `0.3065` | 99,920.00 USD | 0.00 USD | 14,720.00 USD | `-7.51%` | `48,026.00` |
| `Live` | `Long` | `0.3085` | 85,200.00 USD | 0.00 USD | 6,670.00 USD | `-6.91%` | `21,612.00` |
| `Live` | `Long` | `0.3115` | 78,540.00 USD | 0.00 USD | 824.85 USD | `-6.00%` | `2,648.00` |
| `Live` | `Long` | `0.3125` | 77,710.00 USD | 0.00 USD | 17,140.00 USD | `-5.70%` | `54,861.00` |
| `Live` | `Long` | `0.3135` | 60,570.00 USD | 0.00 USD | 44,390.00 USD | `-5.40%` | `141,602.00` |
| `Live` | `Long` | `0.3145` | 16,170.00 USD | 0.00 USD | 2,140.00 USD | `-5.10%` | `6,799.00` |
| `Live` | `Long` | `0.3155` | 14,040.00 USD | 0.00 USD | 142.29 USD | `-4.80%` | `451.00` |
| `Live` | `Long` | `0.3165` | 13,890.00 USD | 0.00 USD | 1,490.00 USD | `-4.49%` | `4,723.00` |
| `Live` | `Long` | `0.3175` | 12,400.00 USD | 0.00 USD | 1,400.00 USD | `-4.19%` | `4,408.00` |
| `Live` | `Long` | `0.3235` | 11,000.00 USD | 0.00 USD | 11,000.00 USD | `-2.38%` | `34,003.00` |
| `Live` | `Short` | `0.3425` | 456.55 USD | 456.55 USD | 0.00 USD | `+3.35%` | `1,333.00` |
| `Live` | `Short` | `0.3435` | 610.44 USD | 153.89 USD | 0.00 USD | `+3.65%` | `448.00` |
| `Live` | `Short` | `0.3445` | 5,900.00 USD | 5,290.00 USD | 0.00 USD | `+3.95%` | `15,355.00` |
| `Live` | `Short` | `0.3455` | 6,390.00 USD | 486.46 USD | 0.00 USD | `+4.26%` | `1,408.00` |
| `Live` | `Short` | `0.3475` | 16,590.00 USD | 10,210.00 USD | 0.00 USD | `+4.86%` | `29,369.00` |
| `Live` | `Short` | `0.3485` | 16,820.00 USD | 223.04 USD | 0.00 USD | `+5.16%` | `640.00` |
| `Live` | `Short` | `0.3505` | 194,350.00 USD | 177,540.00 USD | 0.00 USD | `+5.77%` | `506,529.00` |
| `Live` | `Short` | `0.3535` | 194,580.00 USD | 223.06 USD | 0.00 USD | `+6.67%` | `631.00` |
| `Live` | `Short` | `0.3555` | 200,090.00 USD | 5,510.00 USD | 0.00 USD | `+7.27%` | `15,503.00` |
| `Live` | `Short` | `0.3645` | 200,460.00 USD | 376.53 USD | 0.00 USD | `+9.99%` | `1,033.00` |
| `Live` | `Short` | `0.3665` | 200,730.00 USD | 262.78 USD | 0.00 USD | `+10.59%` | `717.00` |
| `Live` | `Short` | `0.3745` | 207,420.00 USD | 6,690.00 USD | 0.00 USD | `+13.01%` | `17,870.00` |
| `Live` | `Short` | `0.3785` | 207,960.00 USD | 537.85 USD | 0.00 USD | `+14.21%` | `1,421.00` |
| `Live` | `Short` | `0.3795` | 765,850.00 USD | 557,900.00 USD | 0.00 USD | `+14.52%` | `1,470,083.00` |
| `Live` | `Short` | `0.3815` | 766,140.00 USD | 285.74 USD | 0.00 USD | `+15.12%` | `749.00` |
| `Live` | `Short` | `0.3845` | 766,260.00 USD | 115.35 USD | 0.00 USD | `+16.02%` | `300.00` |
| `Live` | `Short` | `0.3895` | 772,540.00 USD | 6,280.00 USD | 0.00 USD | `+17.53%` | `16,133.00` |
| `Live` | `Short` | `0.3905` | 777,310.00 USD | 4,770.00 USD | 0.00 USD | `+17.84%` | `12,210.00` |
| `Live` | `Short` | `0.3915` | 777,790.00 USD | 487.42 USD | 0.00 USD | `+18.14%` | `1,245.00` |
| `Live` | `Short` | `0.3945` | 779,280.00 USD | 1,490.00 USD | 0.00 USD | `+19.04%` | `3,770.00` |
| `Live` | `Short` | `0.3955` | 897,710.00 USD | 118,430.00 USD | 0.00 USD | `+19.34%` | `299,436.00` |
| `Live` | `Short` | `0.4185` | 897,880.00 USD | 167.40 USD | 0.00 USD | `+26.28%` | `400.00` |
| `Live` | `Short` | `0.4205` | 902,360.00 USD | 4,480.00 USD | 0.00 USD | `+26.89%` | `10,665.00` |
| `Live` | `Short` | `0.4245` | 954,190.00 USD | 51,830.00 USD | 0.00 USD | `+28.09%` | `122,096.00` |
| `Live` | `Short` | `0.4475` | 1,030,000.00 USD | 73,860.00 USD | 0.00 USD | `+35.04%` | `165,059.00` |
| `Live` | `Short` | `0.4705` | 1,030,000.00 USD | 203.26 USD | 0.00 USD | `+41.98%` | `432.00` |
| `Live` | `Short` | `0.4905` | 1,030,000.00 USD | 841.21 USD | 0.00 USD | `+48.01%` | `1,715.00` |
| `Live` | `Short` | `0.4915` | 1,030,000.00 USD | 5,130.00 USD | 0.00 USD | `+48.31%` | `10,430.00` |
| `Live` | `Short` | `0.5345` | 1,030,000.00 USD | 669.73 USD | 0.00 USD | `+61.29%` | `1,253.00` |
| `Live` | `Short` | `0.5365` | 1,730,000.00 USD | 695,970.00 USD | 0.00 USD | `+61.89%` | `1,297,248.00` |
| `Live` | `Short` | `0.5395` | 1,750,000.00 USD | 18,560.00 USD | 0.00 USD | `+62.80%` | `34,396.00` |
| `Live` | `Short` | `0.5585` | 1,750,000.00 USD | 742.25 USD | 0.00 USD | `+68.53%` | `1,329.00` |
| `Live` | `Short` | `0.5625` | 1,750,000.00 USD | 140.62 USD | 0.00 USD | `+69.74%` | `250.00` |
| `Live` | `Short` | `0.6145` | 1,790,000.00 USD | 36,870.00 USD | 0.00 USD | `+85.43%` | `60,000.00` |
| `Live` | `Short` | `0.6275` | 1,790,000.00 USD | 275.47 USD | 0.00 USD | `+89.35%` | `439.00` |
| `Live` | `Short` | `0.6285` | 1,790,000.00 USD | 7,390.00 USD | 0.00 USD | `+89.65%` | `11,753.00` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `0.1805` | 819,350.00 USD | 0.00 USD | 6,100.00 USD | `-45.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2035` | 813,260.00 USD | 0.00 USD | 1,750.00 USD | `-38.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2105` | 811,500.00 USD | 0.00 USD | 579.72 USD | `-36.48%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2345` | 810,920.00 USD | 0.00 USD | 705.61 USD | `-29.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2405` | 810,220.00 USD | 0.00 USD | 1,200.00 USD | `-27.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2415` | 809,020.00 USD | 0.00 USD | 127.51 USD | `-27.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2505` | 808,890.00 USD | 0.00 USD | 1,850.00 USD | `-24.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2565` | 807,030.00 USD | 0.00 USD | 1,920.00 USD | `-22.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2605` | 805,110.00 USD | 0.00 USD | 4,200.00 USD | `-21.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2625` | 800,910.00 USD | 0.00 USD | 954.98 USD | `-20.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2675` | 799,950.00 USD | 0.00 USD | 695.50 USD | `-19.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2685` | 799,260.00 USD | 0.00 USD | 1,630.00 USD | `-18.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2815` | 797,630.00 USD | 0.00 USD | 2,550.00 USD | `-15.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2835` | 795,080.00 USD | 0.00 USD | 229.92 USD | `-14.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2935` | 794,850.00 USD | 0.00 USD | 15,940.00 USD | `-11.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2965` | 778,910.00 USD | 0.00 USD | 111.19 USD | `-10.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2985` | 778,800.00 USD | 0.00 USD | 685.95 USD | `-9.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3005` | 778,110.00 USD | 0.00 USD | 2,710.00 USD | `-9.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3065` | 775,410.00 USD | 0.00 USD | 919.50 USD | `-7.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3075` | 774,490.00 USD | 0.00 USD | 193.11 USD | `-7.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3085` | 774,290.00 USD | 0.00 USD | 16,070.00 USD | `-6.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3095` | 758,230.00 USD | 0.00 USD | 147.32 USD | `-6.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3105` | 758,080.00 USD | 0.00 USD | 25,820.00 USD | `-6.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3115` | 732,260.00 USD | 0.00 USD | 6,530.00 USD | `-6.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3125` | 725,740.00 USD | 0.00 USD | 524,570.00 USD | `-5.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3135` | 201,160.00 USD | 0.00 USD | 1,270.00 USD | `-5.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3145` | 199,900.00 USD | 0.00 USD | 25,790.00 USD | `-5.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3155` | 174,110.00 USD | 0.00 USD | 3,600.00 USD | `-4.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3165` | 170,510.00 USD | 0.00 USD | 6,100.00 USD | `-4.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3185` | 164,410.00 USD | 0.00 USD | 2,010.00 USD | `-3.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3195` | 162,400.00 USD | 0.00 USD | 15,160.00 USD | `-3.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3205` | 147,240.00 USD | 0.00 USD | 21,270.00 USD | `-3.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3215` | 125,970.00 USD | 0.00 USD | 55,600.00 USD | `-2.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3225` | 70,370.00 USD | 0.00 USD | 174.47 USD | `-2.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3235` | 70,190.00 USD | 0.00 USD | 845.95 USD | `-2.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3245` | 69,350.00 USD | 0.00 USD | 14,470.00 USD | `-2.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3255` | 54,880.00 USD | 0.00 USD | 8,410.00 USD | `-1.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3265` | 46,460.00 USD | 0.00 USD | 25,740.00 USD | `-1.48%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3275` | 20,720.00 USD | 0.00 USD | 13,320.00 USD | `-1.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3285` | 7,400.00 USD | 0.00 USD | 3,730.00 USD | `-0.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3295` | 3,670.00 USD | 0.00 USD | 1,830.00 USD | `-0.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3305` | 1,840.00 USD | 0.00 USD | 1,840.00 USD | `-0.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3315` | 496.92 USD | 496.92 USD | 0.00 USD | `+0.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3325` | 41,090.00 USD | 40,600.00 USD | 0.00 USD | `+0.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3335` | 42,580.00 USD | 1,480.00 USD | 0.00 USD | `+0.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3345` | 43,800.00 USD | 1,220.00 USD | 0.00 USD | `+0.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3355` | 218,660.00 USD | 174,860.00 USD | 0.00 USD | `+1.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3365` | 219,040.00 USD | 379.57 USD | 0.00 USD | `+1.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3375` | 219,200.00 USD | 162.00 USD | 0.00 USD | `+1.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3385` | 230,850.00 USD | 11,640.00 USD | 0.00 USD | `+2.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3395` | 230,950.00 USD | 102.87 USD | 0.00 USD | `+2.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3405` | 234,040.00 USD | 3,090.00 USD | 0.00 USD | `+2.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3415` | 234,940.00 USD | 904.63 USD | 0.00 USD | `+3.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3425` | 240,460.00 USD | 5,520.00 USD | 0.00 USD | `+3.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3435` | 248,080.00 USD | 7,610.00 USD | 0.00 USD | `+3.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3455` | 250,960.00 USD | 2,880.00 USD | 0.00 USD | `+4.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3465` | 258,890.00 USD | 7,930.00 USD | 0.00 USD | `+4.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3475` | 262,040.00 USD | 3,150.00 USD | 0.00 USD | `+4.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3485` | 263,100.00 USD | 1,060.00 USD | 0.00 USD | `+5.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3495` | 288,850.00 USD | 25,750.00 USD | 0.00 USD | `+5.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3505` | 307,430.00 USD | 18,580.00 USD | 0.00 USD | `+5.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3535` | 320,850.00 USD | 13,420.00 USD | 0.00 USD | `+6.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3545` | 321,620.00 USD | 769.97 USD | 0.00 USD | `+6.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3555` | 321,850.00 USD | 226.10 USD | 0.00 USD | `+7.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3575` | 326,030.00 USD | 4,180.00 USD | 0.00 USD | `+7.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3585` | 332,010.00 USD | 5,990.00 USD | 0.00 USD | `+8.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3595` | 338,200.00 USD | 6,180.00 USD | 0.00 USD | `+8.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3605` | 338,680.00 USD | 485.59 USD | 0.00 USD | `+8.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3635` | 339,070.00 USD | 390.40 USD | 0.00 USD | `+9.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3655` | 339,510.00 USD | 433.85 USD | 0.00 USD | `+10.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3665` | 339,970.00 USD | 463.99 USD | 0.00 USD | `+10.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3695` | 340,130.00 USD | 159.62 USD | 0.00 USD | `+11.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3705` | 341,060.00 USD | 926.99 USD | 0.00 USD | `+11.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3755` | 343,820.00 USD | 2,760.00 USD | 0.00 USD | `+13.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3785` | 344,090.00 USD | 275.17 USD | 0.00 USD | `+14.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3795` | 344,550.00 USD | 463.37 USD | 0.00 USD | `+14.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3805` | 344,890.00 USD | 337.12 USD | 0.00 USD | `+14.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3815` | 345,010.00 USD | 114.83 USD | 0.00 USD | `+15.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3835` | 345,230.00 USD | 224.73 USD | 0.00 USD | `+15.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3855` | 345,750.00 USD | 514.64 USD | 0.00 USD | `+16.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3895` | 346,100.00 USD | 352.11 USD | 0.00 USD | `+17.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3965` | 348,500.00 USD | 2,400.00 USD | 0.00 USD | `+19.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3975` | 349,070.00 USD | 572.00 USD | 0.00 USD | `+19.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3985` | 350,270.00 USD | 1,200.00 USD | 0.00 USD | `+20.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3995` | 403,150.00 USD | 52,880.00 USD | 0.00 USD | `+20.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4015` | 405,550.00 USD | 2,400.00 USD | 0.00 USD | `+21.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4035` | 406,750.00 USD | 1,200.00 USD | 0.00 USD | `+21.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4055` | 407,950.00 USD | 1,200.00 USD | 0.00 USD | `+22.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4065` | 409,150.00 USD | 1,200.00 USD | 0.00 USD | `+22.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4205` | 409,330.00 USD | 186.70 USD | 0.00 USD | `+26.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4405` | 447,910.00 USD | 38,580.00 USD | 0.00 USD | `+32.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4445` | 448,080.00 USD | 170.69 USD | 0.00 USD | `+34.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4495` | 449,470.00 USD | 1,390.00 USD | 0.00 USD | `+35.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.5005` | 460,620.00 USD | 11,150.00 USD | 0.00 USD | `+51.03%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `0.2979` | 12,950,000.00 USD | 0.00 USD | 12,950,000.00 USD | 65,800.00 USD | 8,600.00 USD | 10,570.00 USD |
| `1D` | `0.2983` | 2,960,000.00 USD | 0.00 USD | 2,960,000.00 USD | 80,870.00 USD | 15,850.00 USD | 26,180.00 USD |
| `7D` | `0.2983` | 12,870,000.00 USD | 0.00 USD | 12,870,000.00 USD | 99,280.00 USD | 9,990.00 USD | 27,500.00 USD |
| `1D` | `0.2987` | 2,840,000.00 USD | 0.00 USD | 2,840,000.00 USD | 44,390.00 USD | 4,220.00 USD | 2,890.00 USD |
| `7D` | `0.2987` | 12,730,000.00 USD | 0.00 USD | 12,730,000.00 USD | 76,610.00 USD | 9,860.00 USD | 6,170.00 USD |
| `7D` | `0.2991` | 12,640,000.00 USD | 0.00 USD | 12,640,000.00 USD | 23,720.00 USD | 6,910.00 USD | 3,870.00 USD |
| `7D` | `0.3051` | 12,600,000.00 USD | 0.00 USD | 12,600,000.00 USD | 380.73 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3055` | 12,600,000.00 USD | 0.00 USD | 12,600,000.00 USD | 1,380.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3059` | 12,600,000.00 USD | 0.00 USD | 12,600,000.00 USD | 212.37 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3063` | 12,600,000.00 USD | 0.00 USD | 12,600,000.00 USD | 1,990.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3067` | 2,790,000.00 USD | 0.00 USD | 2,790,000.00 USD | 57.95 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3067` | 12,600,000.00 USD | 0.00 USD | 12,600,000.00 USD | 5,660.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3071` | 2,790,000.00 USD | 0.00 USD | 2,790,000.00 USD | 2,980.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3071` | 12,590,000.00 USD | 0.00 USD | 12,590,000.00 USD | 6,280.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3075` | 2,780,000.00 USD | 0.00 USD | 2,780,000.00 USD | 1,410.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3075` | 12,590,000.00 USD | 0.00 USD | 12,590,000.00 USD | 2,850.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3079` | 2,780,000.00 USD | 0.00 USD | 2,780,000.00 USD | 135.83 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3079` | 12,580,000.00 USD | 0.00 USD | 12,580,000.00 USD | 2,180.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3083` | 2,780,000.00 USD | 0.00 USD | 2,780,000.00 USD | 221.36 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3083` | 12,580,000.00 USD | 0.00 USD | 12,580,000.00 USD | 1,200.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3087` | 2,780,000.00 USD | 0.00 USD | 2,780,000.00 USD | 506.09 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3087` | 12,580,000.00 USD | 0.00 USD | 12,580,000.00 USD | 1,860.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3091` | 2,780,000.00 USD | 0.00 USD | 2,780,000.00 USD | 61.02 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3091` | 12,580,000.00 USD | 0.00 USD | 12,580,000.00 USD | 1,320.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3107` | 12,580,000.00 USD | 0.00 USD | 12,580,000.00 USD | 1,790.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3111` | 12,580,000.00 USD | 0.00 USD | 12,580,000.00 USD | 554.30 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3115` | 12,580,000.00 USD | 0.00 USD | 12,580,000.00 USD | 283.30 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3119` | 12,570,000.00 USD | 0.00 USD | 12,570,000.00 USD | 2,650.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3123` | 2,780,000.00 USD | 0.00 USD | 2,780,000.00 USD | 77.30 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3123` | 12,570,000.00 USD | 0.00 USD | 12,570,000.00 USD | 7,550.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3127` | 2,780,000.00 USD | 0.00 USD | 2,780,000.00 USD | 3,970.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3127` | 12,560,000.00 USD | 0.00 USD | 12,560,000.00 USD | 8,380.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3131` | 2,780,000.00 USD | 0.00 USD | 2,780,000.00 USD | 1,880.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3131` | 12,560,000.00 USD | 0.00 USD | 12,560,000.00 USD | 3,800.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3135` | 2,780,000.00 USD | 0.00 USD | 2,780,000.00 USD | 181.20 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3135` | 12,550,000.00 USD | 0.00 USD | 12,550,000.00 USD | 2,910.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3139` | 2,780,000.00 USD | 0.00 USD | 2,780,000.00 USD | 295.30 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3139` | 12,550,000.00 USD | 0.00 USD | 12,550,000.00 USD | 1,600.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3143` | 2,770,000.00 USD | 0.00 USD | 2,770,000.00 USD | 429.90 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3143` | 12,550,000.00 USD | 0.00 USD | 12,550,000.00 USD | 183,810.00 USD | 34,890.00 USD | 11,170.00 USD |
| `1D` | `0.3147` | 2,770,000.00 USD | 0.00 USD | 2,770,000.00 USD | 326.60 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3147` | 12,320,000.00 USD | 0.00 USD | 12,320,000.00 USD | 170,840.00 USD | 16,380.00 USD | 21,590.00 USD |
| `7D` | `0.3151` | 12,110,000.00 USD | 0.00 USD | 12,110,000.00 USD | 187,500.00 USD | 29,590.00 USD | 61,120.00 USD |
| `7D` | `0.3155` | 11,830,000.00 USD | 0.00 USD | 11,830,000.00 USD | 157,220.00 USD | 40,480.00 USD | 22,590.00 USD |
| `1D` | `0.3159` | 2,770,000.00 USD | 0.00 USD | 2,770,000.00 USD | 5,750.00 USD | 5,600.00 USD | 27,350.00 USD |
| `7D` | `0.3159` | 11,610,000.00 USD | 0.00 USD | 11,610,000.00 USD | 353,770.00 USD | 101,710.00 USD | 112,500.00 USD |
| `1D` | `0.3163` | 2,740,000.00 USD | 0.00 USD | 2,740,000.00 USD | 98,530.00 USD | 32,280.00 USD | 30,960.00 USD |
| `7D` | `0.3163` | 11,040,000.00 USD | 0.00 USD | 11,040,000.00 USD | 225,120.00 USD | 116,130.00 USD | 134,250.00 USD |
| `1D` | `0.3167` | 2,570,000.00 USD | 0.00 USD | 2,570,000.00 USD | 50,820.00 USD | 14,920.00 USD | 20,330.00 USD |
| `7D` | `0.3167` | 10,570,000.00 USD | 0.00 USD | 10,570,000.00 USD | 328,930.00 USD | 75,090.00 USD | 95,630.00 USD |
| `1D` | `0.3171` | 2,490,000.00 USD | 0.00 USD | 2,490,000.00 USD | 7,710.00 USD | 13,460.00 USD | 9,490.00 USD |
| `7D` | `0.3171` | 10,070,000.00 USD | 0.00 USD | 10,070,000.00 USD | 293,450.00 USD | 89,970.00 USD | 96,960.00 USD |
| `1D` | `0.3175` | 2,460,000.00 USD | 0.00 USD | 2,460,000.00 USD | 16,390.00 USD | 5,630.00 USD | 3,360.00 USD |
| `7D` | `0.3175` | 9,590,000.00 USD | 0.00 USD | 9,590,000.00 USD | 28,570.00 USD | 12,370.00 USD | 39,210.00 USD |
| `1D` | `0.3179` | 2,430,000.00 USD | 0.00 USD | 2,430,000.00 USD | 39,170.00 USD | 19,460.00 USD | 25,060.00 USD |
| `7D` | `0.3179` | 9,510,000.00 USD | 0.00 USD | 9,510,000.00 USD | 231,050.00 USD | 33,640.00 USD | 39,970.00 USD |
| `1D` | `0.3183` | 2,350,000.00 USD | 0.00 USD | 2,350,000.00 USD | 362,180.00 USD | 45,610.00 USD | 64,720.00 USD |
| `7D` | `0.3183` | 9,200,000.00 USD | 0.00 USD | 9,200,000.00 USD | 477,670.00 USD | 49,030.00 USD | 70,140.00 USD |
| `1D` | `0.3187` | 1,880,000.00 USD | 0.00 USD | 1,880,000.00 USD | 23,690.00 USD | 2,240.00 USD | 0.00 USD |
| `7D` | `0.3187` | 8,610,000.00 USD | 0.00 USD | 8,610,000.00 USD | 117,850.00 USD | 29,330.00 USD | 11,120.00 USD |
| `7D` | `0.3191` | 8,450,000.00 USD | 0.00 USD | 8,450,000.00 USD | 59,160.00 USD | 13,950.00 USD | 11,780.00 USD |
| `7D` | `0.3207` | 8,360,000.00 USD | 0.00 USD | 8,360,000.00 USD | 158,770.00 USD | 34,380.00 USD | 7,770.00 USD |
| `7D` | `0.3211` | 8,160,000.00 USD | 0.00 USD | 8,160,000.00 USD | 403,080.00 USD | 68,150.00 USD | 57,740.00 USD |
| `7D` | `0.3215` | 7,630,000.00 USD | 0.00 USD | 7,630,000.00 USD | 413,850.00 USD | 47,610.00 USD | 100,600.00 USD |
| `7D` | `0.3219` | 7,070,000.00 USD | 0.00 USD | 7,070,000.00 USD | 324,100.00 USD | 67,660.00 USD | 63,030.00 USD |
| `1D` | `0.3223` | 1,850,000.00 USD | 0.00 USD | 1,850,000.00 USD | 0.00 USD | 0.00 USD | 20,260.00 USD |
| `7D` | `0.3223` | 6,620,000.00 USD | 0.00 USD | 6,620,000.00 USD | 435,620.00 USD | 137,210.00 USD | 89,860.00 USD |
| `1D` | `0.3227` | 1,830,000.00 USD | 0.00 USD | 1,830,000.00 USD | 101,660.00 USD | 43,840.00 USD | 51,780.00 USD |
| `7D` | `0.3227` | 5,950,000.00 USD | 0.00 USD | 5,950,000.00 USD | 638,380.00 USD | 208,030.00 USD | 227,150.00 USD |
| `1D` | `0.3231` | 1,630,000.00 USD | 0.00 USD | 1,630,000.00 USD | 161,500.00 USD | 49,860.00 USD | 72,280.00 USD |
| `7D` | `0.3231` | 4,880,000.00 USD | 0.00 USD | 4,880,000.00 USD | 589,500.00 USD | 180,670.00 USD | 295,130.00 USD |
| `1D` | `0.3235` | 1,350,000.00 USD | 0.00 USD | 1,350,000.00 USD | 54,750.00 USD | 32,080.00 USD | 31,960.00 USD |
| `7D` | `0.3235` | 3,810,000.00 USD | 0.00 USD | 3,810,000.00 USD | 507,910.00 USD | 168,260.00 USD | 205,040.00 USD |
| `1D` | `0.3239` | 1,230,000.00 USD | 0.00 USD | 1,230,000.00 USD | 15,020.00 USD | 10,730.00 USD | 3,870.00 USD |
| `7D` | `0.3239` | 2,930,000.00 USD | 0.00 USD | 2,930,000.00 USD | 354,650.00 USD | 119,100.00 USD | 114,090.00 USD |
| `1D` | `0.3243` | 1,200,000.00 USD | 0.00 USD | 1,200,000.00 USD | 80,740.00 USD | 20,910.00 USD | 19,290.00 USD |
| `7D` | `0.3243` | 2,350,000.00 USD | 0.00 USD | 2,350,000.00 USD | 265,190.00 USD | 39,180.00 USD | 42,580.00 USD |
| `1D` | `0.3247` | 1,080,000.00 USD | 0.00 USD | 1,080,000.00 USD | 189,030.00 USD | 68,180.00 USD | 113,670.00 USD |
| `7D` | `0.3247` | 2,000,000.00 USD | 0.00 USD | 2,000,000.00 USD | 559,960.00 USD | 72,190.00 USD | 145,960.00 USD |
| `1D` | `0.3251` | 708,010.00 USD | 0.00 USD | 708,010.00 USD | 585,700.00 USD | 52,790.00 USD | 49,450.00 USD |
| `7D` | `0.3251` | 1,220,000.00 USD | 0.00 USD | 1,220,000.00 USD | 667,020.00 USD | 65,250.00 USD | 61,340.00 USD |
| `1D` | `0.3255` | 20,070.00 USD | 0.00 USD | 20,070.00 USD | 20,070.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3255` | 426,520.00 USD | 0.00 USD | 426,520.00 USD | 251,380.00 USD | 60,580.00 USD | 35,520.00 USD |
| `7D` | `0.3259` | 79,040.00 USD | 0.00 USD | 79,040.00 USD | 51,940.00 USD | 16,810.00 USD | 10,280.00 USD |
| `1D` | `0.3312` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3314` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3339` | 455,400.00 USD | 455,400.00 USD | 0.00 USD | 363,280.00 USD | 69,780.00 USD | 22,330.00 USD |
| `7D` | `0.3343` | 729,900.00 USD | 729,900.00 USD | 0.00 USD | 198,570.00 USD | 32,750.00 USD | 43,180.00 USD |
| `7D` | `0.3347` | 1,290,000.00 USD | 1,290,000.00 USD | 0.00 USD | 413,850.00 USD | 47,610.00 USD | 100,600.00 USD |
| `7D` | `0.3351` | 1,750,000.00 USD | 1,750,000.00 USD | 0.00 USD | 324,100.00 USD | 67,660.00 USD | 63,030.00 USD |
| `1D` | `0.3355` | 20,260.00 USD | 20,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 20,260.00 USD |
| `7D` | `0.3355` | 2,410,000.00 USD | 2,410,000.00 USD | 0.00 USD | 435,620.00 USD | 137,210.00 USD | 89,860.00 USD |
| `1D` | `0.3359` | 217,540.00 USD | 217,540.00 USD | 0.00 USD | 101,660.00 USD | 43,840.00 USD | 51,780.00 USD |
| `7D` | `0.3359` | 3,480,000.00 USD | 3,480,000.00 USD | 0.00 USD | 638,380.00 USD | 208,030.00 USD | 227,150.00 USD |
| `1D` | `0.3363` | 501,180.00 USD | 501,180.00 USD | 0.00 USD | 161,500.00 USD | 49,860.00 USD | 72,280.00 USD |
| `7D` | `0.3363` | 4,550,000.00 USD | 4,550,000.00 USD | 0.00 USD | 589,500.00 USD | 180,670.00 USD | 295,130.00 USD |
| `1D` | `0.3367` | 619,960.00 USD | 619,960.00 USD | 0.00 USD | 54,750.00 USD | 32,080.00 USD | 31,960.00 USD |
| `7D` | `0.3367` | 5,430,000.00 USD | 5,430,000.00 USD | 0.00 USD | 507,910.00 USD | 168,260.00 USD | 205,040.00 USD |
| `1D` | `0.3371` | 649,590.00 USD | 649,590.00 USD | 0.00 USD | 15,020.00 USD | 10,730.00 USD | 3,870.00 USD |
| `7D` | `0.3371` | 6,020,000.00 USD | 6,020,000.00 USD | 0.00 USD | 354,650.00 USD | 119,100.00 USD | 114,090.00 USD |
| `1D` | `0.3375` | 770,530.00 USD | 770,530.00 USD | 0.00 USD | 80,740.00 USD | 20,910.00 USD | 19,290.00 USD |
| `7D` | `0.3375` | 6,360,000.00 USD | 6,360,000.00 USD | 0.00 USD | 265,190.00 USD | 39,180.00 USD | 42,580.00 USD |
| `1D` | `0.3379` | 1,140,000.00 USD | 1,140,000.00 USD | 0.00 USD | 189,030.00 USD | 68,180.00 USD | 113,670.00 USD |
| `7D` | `0.3379` | 7,140,000.00 USD | 7,140,000.00 USD | 0.00 USD | 559,960.00 USD | 72,190.00 USD | 145,960.00 USD |
| `1D` | `0.3383` | 1,830,000.00 USD | 1,830,000.00 USD | 0.00 USD | 585,700.00 USD | 52,790.00 USD | 49,450.00 USD |
| `7D` | `0.3383` | 7,940,000.00 USD | 7,940,000.00 USD | 0.00 USD | 667,020.00 USD | 65,250.00 USD | 61,340.00 USD |
| `1D` | `0.3387` | 1,850,000.00 USD | 1,850,000.00 USD | 0.00 USD | 20,070.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3387` | 8,280,000.00 USD | 8,280,000.00 USD | 0.00 USD | 251,380.00 USD | 60,580.00 USD | 35,520.00 USD |
| `7D` | `0.3391` | 8,360,000.00 USD | 8,360,000.00 USD | 0.00 USD | 51,940.00 USD | 16,810.00 USD | 10,280.00 USD |
| `7D` | `0.3403` | 8,460,000.00 USD | 8,460,000.00 USD | 0.00 USD | 79,380.00 USD | 17,190.00 USD | 3,890.00 USD |
| `7D` | `0.3407` | 8,670,000.00 USD | 8,670,000.00 USD | 0.00 USD | 162,870.00 USD | 34,080.00 USD | 13,980.00 USD |
| `7D` | `0.3411` | 8,990,000.00 USD | 8,990,000.00 USD | 0.00 USD | 236,810.00 USD | 19,270.00 USD | 60,150.00 USD |
| `7D` | `0.3415` | 9,120,000.00 USD | 9,120,000.00 USD | 0.00 USD | 75,860.00 USD | 24,680.00 USD | 30,770.00 USD |
| `7D` | `0.3419` | 9,350,000.00 USD | 9,350,000.00 USD | 0.00 USD | 162,450.00 USD | 45,810.00 USD | 19,490.00 USD |
| `1D` | `0.3423` | 1,890,000.00 USD | 1,890,000.00 USD | 0.00 USD | 5,750.00 USD | 5,600.00 USD | 27,350.00 USD |
| `7D` | `0.3423` | 9,860,000.00 USD | 9,860,000.00 USD | 0.00 USD | 331,520.00 USD | 82,020.00 USD | 100,690.00 USD |
| `1D` | `0.3427` | 2,050,000.00 USD | 2,050,000.00 USD | 0.00 USD | 98,530.00 USD | 32,280.00 USD | 30,960.00 USD |
| `7D` | `0.3427` | 10,340,000.00 USD | 10,340,000.00 USD | 0.00 USD | 225,120.00 USD | 116,130.00 USD | 134,250.00 USD |
| `1D` | `0.3431` | 2,140,000.00 USD | 2,140,000.00 USD | 0.00 USD | 50,820.00 USD | 14,920.00 USD | 20,330.00 USD |
| `7D` | `0.3431` | 10,840,000.00 USD | 10,840,000.00 USD | 0.00 USD | 328,930.00 USD | 75,090.00 USD | 95,630.00 USD |
| `1D` | `0.3435` | 2,170,000.00 USD | 2,170,000.00 USD | 0.00 USD | 7,710.00 USD | 13,460.00 USD | 9,490.00 USD |
| `7D` | `0.3435` | 11,320,000.00 USD | 11,320,000.00 USD | 0.00 USD | 295,240.00 USD | 89,970.00 USD | 96,960.00 USD |
| `1D` | `0.3439` | 2,190,000.00 USD | 2,190,000.00 USD | 0.00 USD | 16,390.00 USD | 5,630.00 USD | 3,360.00 USD |
| `7D` | `0.3439` | 11,400,000.00 USD | 11,400,000.00 USD | 0.00 USD | 29,120.00 USD | 12,370.00 USD | 39,210.00 USD |
| `1D` | `0.3443` | 2,280,000.00 USD | 2,280,000.00 USD | 0.00 USD | 39,170.00 USD | 19,460.00 USD | 25,060.00 USD |
| `7D` | `0.3443` | 11,710,000.00 USD | 11,710,000.00 USD | 0.00 USD | 231,330.00 USD | 33,640.00 USD | 39,970.00 USD |
| `1D` | `0.3447` | 2,600,000.00 USD | 2,600,000.00 USD | 0.00 USD | 235,910.00 USD | 35,600.00 USD | 54,570.00 USD |
| `7D` | `0.3447` | 12,110,000.00 USD | 12,110,000.00 USD | 0.00 USD | 310,260.00 USD | 31,970.00 USD | 56,490.00 USD |
| `1D` | `0.3451` | 2,770,000.00 USD | 2,770,000.00 USD | 0.00 USD | 150,040.00 USD | 12,250.00 USD | 10,150.00 USD |
| `7D` | `0.3451` | 12,400,000.00 USD | 12,400,000.00 USD | 0.00 USD | 245,650.00 USD | 26,900.00 USD | 20,240.00 USD |
| `1D` | `0.3455` | 2,780,000.00 USD | 2,780,000.00 USD | 0.00 USD | 1,320.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3455` | 12,550,000.00 USD | 12,550,000.00 USD | 0.00 USD | 97,690.00 USD | 33,430.00 USD | 16,310.00 USD |
| `1D` | `0.3459` | 2,780,000.00 USD | 2,780,000.00 USD | 0.00 USD | 4,260.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3459` | 12,570,000.00 USD | 12,570,000.00 USD | 0.00 USD | 22,340.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3463` | 2,780,000.00 USD | 2,780,000.00 USD | 0.00 USD | 397.30 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3463` | 12,570,000.00 USD | 12,570,000.00 USD | 0.00 USD | 3,330.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3467` | 2,780,000.00 USD | 2,780,000.00 USD | 0.00 USD | 57.70 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3467` | 12,570,000.00 USD | 12,570,000.00 USD | 0.00 USD | 1,130.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3471` | 2,780,000.00 USD | 2,780,000.00 USD | 0.00 USD | 307.20 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3471` | 12,570,000.00 USD | 12,570,000.00 USD | 0.00 USD | 1,500.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3475` | 2,780,000.00 USD | 2,780,000.00 USD | 0.00 USD | 663.20 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3475` | 12,580,000.00 USD | 12,580,000.00 USD | 0.00 USD | 2,180.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3479` | 2,780,000.00 USD | 2,780,000.00 USD | 0.00 USD | 81.40 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3479` | 12,580,000.00 USD | 12,580,000.00 USD | 0.00 USD | 1,770.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3491` | 12,580,000.00 USD | 12,580,000.00 USD | 0.00 USD | 1,340.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3495` | 12,580,000.00 USD | 12,580,000.00 USD | 0.00 USD | 415.52 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3499` | 12,580,000.00 USD | 12,580,000.00 USD | 0.00 USD | 212.37 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3503` | 12,580,000.00 USD | 12,580,000.00 USD | 0.00 USD | 1,990.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3507` | 2,780,000.00 USD | 2,780,000.00 USD | 0.00 USD | 57.95 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3507` | 12,590,000.00 USD | 12,590,000.00 USD | 0.00 USD | 5,660.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3511` | 2,780,000.00 USD | 2,780,000.00 USD | 0.00 USD | 1,880.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3511` | 12,590,000.00 USD | 12,590,000.00 USD | 0.00 USD | 4,590.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3515` | 2,790,000.00 USD | 2,790,000.00 USD | 0.00 USD | 2,300.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3515` | 12,600,000.00 USD | 12,600,000.00 USD | 0.00 USD | 3,690.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3519` | 2,790,000.00 USD | 2,790,000.00 USD | 0.00 USD | 297.83 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3519` | 12,600,000.00 USD | 12,600,000.00 USD | 0.00 USD | 2,490.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3523` | 2,790,000.00 USD | 2,790,000.00 USD | 0.00 USD | 43.25 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3523` | 12,600,000.00 USD | 12,600,000.00 USD | 0.00 USD | 846.39 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3527` | 2,790,000.00 USD | 2,790,000.00 USD | 0.00 USD | 221.36 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3527` | 12,600,000.00 USD | 12,600,000.00 USD | 0.00 USD | 1,120.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3531` | 2,790,000.00 USD | 2,790,000.00 USD | 0.00 USD | 506.09 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3531` | 12,600,000.00 USD | 12,600,000.00 USD | 0.00 USD | 1,640.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3535` | 2,790,000.00 USD | 2,790,000.00 USD | 0.00 USD | 61.02 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3535` | 12,600,000.00 USD | 12,600,000.00 USD | 0.00 USD | 1,320.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3599` | 12,630,000.00 USD | 12,630,000.00 USD | 0.00 USD | 18,580.00 USD | 6,010.00 USD | 0.00 USD |
| `7D` | `0.3603` | 12,690,000.00 USD | 12,690,000.00 USD | 0.00 USD | 48,320.00 USD | 6,290.00 USD | 2,910.00 USD |
| `7D` | `0.3607` | 12,750,000.00 USD | 12,750,000.00 USD | 0.00 USD | 52,620.00 USD | 4,710.00 USD | 6,550.00 USD |
| `7D` | `0.3611` | 12,800,000.00 USD | 12,800,000.00 USD | 0.00 USD | 35,490.00 USD | 4,040.00 USD | 14,500.00 USD |
| `7D` | `0.3615` | 12,880,000.00 USD | 12,880,000.00 USD | 0.00 USD | 61,190.00 USD | 9,240.00 USD | 1,960.00 USD |
| `1D` | `0.3619` | 2,790,000.00 USD | 2,790,000.00 USD | 0.00 USD | 501.40 USD | 654.45 USD | 5,890.00 USD |
| `7D` | `0.3619` | 13,010,000.00 USD | 13,010,000.00 USD | 0.00 USD | 82,550.00 USD | 20,630.00 USD | 33,010.00 USD |
| `1D` | `0.3623` | 2,840,000.00 USD | 2,840,000.00 USD | 0.00 USD | 24,780.00 USD | 8,270.00 USD | 8,880.00 USD |
| `7D` | `0.3623` | 13,170,000.00 USD | 13,170,000.00 USD | 0.00 USD | 89,280.00 USD | 33,600.00 USD | 36,370.00 USD |
| `1D` | `0.3627` | 2,870,000.00 USD | 2,870,000.00 USD | 0.00 USD | 15,110.00 USD | 5,590.00 USD | 9,070.00 USD |
| `7D` | `0.3627` | 13,300,000.00 USD | 13,300,000.00 USD | 0.00 USD | 77,830.00 USD | 18,040.00 USD | 36,410.00 USD |
| `1D` | `0.3631` | 2,880,000.00 USD | 2,880,000.00 USD | 0.00 USD | 7,150.00 USD | 4,680.00 USD | 5,260.00 USD |
| `7D` | `0.3631` | 13,430,000.00 USD | 13,430,000.00 USD | 0.00 USD | 76,220.00 USD | 25,590.00 USD | 26,610.00 USD |
| `1D` | `0.3635` | 2,880,000.00 USD | 2,880,000.00 USD | 0.00 USD | 147.65 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3635` | 13,500,000.00 USD | 13,500,000.00 USD | 0.00 USD | 44,080.00 USD | 16,220.00 USD | 6,560.00 USD |
| `1D` | `0.3639` | 2,900,000.00 USD | 2,900,000.00 USD | 0.00 USD | 9,160.00 USD | 2,950.00 USD | 2,470.00 USD |
| `7D` | `0.3639` | 13,540,000.00 USD | 13,540,000.00 USD | 0.00 USD | 24,540.00 USD | 2,960.00 USD | 9,300.00 USD |
| `1D` | `0.3643` | 2,940,000.00 USD | 2,940,000.00 USD | 0.00 USD | 19,870.00 USD | 6,710.00 USD | 14,160.00 USD |
| `7D` | `0.3643` | 13,650,000.00 USD | 13,650,000.00 USD | 0.00 USD | 89,610.00 USD | 8,430.00 USD | 14,840.00 USD |
| `1D` | `0.3647` | 3,060,000.00 USD | 3,060,000.00 USD | 0.00 USD | 98,340.00 USD | 11,560.00 USD | 14,430.00 USD |
| `7D` | `0.3647` | 13,740,000.00 USD | 13,740,000.00 USD | 0.00 USD | 66,060.00 USD | 11,120.00 USD | 17,470.00 USD |
| `1D` | `0.3648` | 3,070,000.00 USD | 3,070,000.00 USD | 0.00 USD | 4,900.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3651` | 13,810,000.00 USD | 13,810,000.00 USD | 0.00 USD | 60,980.00 USD | 4,810.00 USD | 2,640.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `298.63M` | Total OI Tokens: `901,787,406.0 TRX`
  * 1h OI Change: `-0.17%` | 4h OI Change: `+4.09%` | 24h OI Change: `+1.04%`
  * Exchange Breakdown: Binance=`90.54M` | Bybit=`49.81M` | OKX=`13.79M` | Hyperliquid=`11.64M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `7.65K` | Last 24h: `9.21K` | Last 3d: `-51.81K` | Last 7d: `-271.18K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0100%` | **USDT OKX** | `0.0016%` |
| **USDT Bybit** | `-0.0025%` | **USDT KuCoin** | `0.0100%` |
| **USDT MEXC** | `0.0100%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `-0.0014%` | **USDT Bitget** | `0.0100%` |
| **CoinM Binance** | `0.0100%` | **CoinM OKX** | `-` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `TRX` | `47.17%` | `52.83%` | `0.89` | 8,060,000.00 USD |
| `15M` | `Binance` | `51.48%` | `48.52%` | `1.06` | 2,900,000.00 USD |
| `15M` | `OKX` | `27.43%` | `72.57%` | `0.38` | 583,670.00 USD |
| `15M` | `Bybit` | `34.68%` | `65.32%` | `0.53` | 664,840.00 USD |
| `15M` | `KuCoin` | `35.96%` | `64.04%` | `0.56` | 45,640.00 USD |
| `15M` | `Gate` | `60.22%` | `39.78%` | `1.51` | 546,950.00 USD |
| `15M` | `Bitget` | `35.43%` | `64.57%` | `0.55` | 285,940.00 USD |
| `15M` | `BingX` | `54.2%` | `45.8%` | `1.18` | 578,950.00 USD |
| `15M` | `MEXC` | `47.25%` | `52.75%` | `0.90` | 615,970.00 USD |
| `15M` | `Bitunix` | `37.27%` | `62.73%` | `0.59` | 166,090.00 USD |
| `15M` | `Hyperliquid` | `17.26%` | `82.74%` | `0.21` | 20,810.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `52.91%` | `47.09%` | `1.12` | 1,460,000.00 USD |
| `15M` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `WhiteBIT` | `4.22%` | `95.78%` | `0.04` | 111,620.00 USD |
| `15M` | `HTX` | `47.58%` | `52.42%` | `0.91` | 19,860.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `21.95%` | `78.05%` | `0.28` | 53,590.00 USD |
| `15M` | `Aster` | `7.45%` | `92.55%` | `0.08` | 419.88 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `3.18%` | `96.82%` | `0.03` | 965.23 USD |
| `15M` | `Whale Positions` | `51.48%` | `48.52%` | `1.06` | 2,900,000.00 USD |
| `15M` | `Global Accounts` | `47.17%` | `52.83%` | `0.89` | 8,060,000.00 USD |
| `1H` | `TRX` | `46.35%` | `53.65%` | `0.86` | 79,690,000.00 USD |
| `1H` | `Binance` | `51.44%` | `48.56%` | `1.06` | 28,040,000.00 USD |
| `1H` | `OKX` | `38.04%` | `61.96%` | `0.61` | 15,990,000.00 USD |
| `1H` | `Bybit` | `41.03%` | `58.97%` | `0.70` | 5,850,000.00 USD |
| `1H` | `KuCoin` | `42.15%` | `57.85%` | `0.73` | 439,830.00 USD |
| `1H` | `Gate` | `51.86%` | `48.14%` | `1.08` | 10,930,000.00 USD |
| `1H` | `Bitget` | `38.31%` | `61.69%` | `0.62` | 2,150,000.00 USD |
| `1H` | `BingX` | `26.76%` | `73.24%` | `0.37` | 4,130,000.00 USD |
| `1H` | `MEXC` | `50.71%` | `49.29%` | `1.03` | 5,230,000.00 USD |
| `1H` | `Bitunix` | `45.59%` | `54.41%` | `0.84` | 2,050,000.00 USD |
| `1H` | `Hyperliquid` | `42.85%` | `57.15%` | `0.75` | 1,910,000.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `51.74%` | `48.26%` | `1.07` | 251,860.00 USD |
| `1H` | `Crypto.com` | `0%` | `0%` | `1.00` | 104,670.00 USD |
| `1H` | `WhiteBIT` | `8.45%` | `91.55%` | `0.09` | 1,310,000.00 USD |
| `1H` | `HTX` | `47.19%` | `52.81%` | `0.89` | 337,490.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `35.42%` | `64.58%` | `0.55` | 341,800.00 USD |
| `1H` | `Aster` | `49.51%` | `50.49%` | `0.98` | 546,130.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `31.88%` | `68.12%` | `0.47` | 78,940.00 USD |
| `1H` | `Whale Positions` | `51.44%` | `48.56%` | `1.06` | 28,040,000.00 USD |
| `1H` | `Global Accounts` | `46.35%` | `53.65%` | `0.86` | 79,690,000.00 USD |
| `4H` | `TRX` | `49.88%` | `50.12%` | `1.00` | 135,980,000.00 USD |
| `4H` | `Binance` | `53.18%` | `46.82%` | `1.14` | 48,020,000.00 USD |
| `4H` | `OKX` | `47.56%` | `52.44%` | `0.91` | 12,490,000.00 USD |
| `4H` | `Bybit` | `52.39%` | `47.61%` | `1.10` | 10,670,000.00 USD |
| `4H` | `KuCoin` | `44.88%` | `55.12%` | `0.81` | 1,020,000.00 USD |
| `4H` | `Gate` | `44.63%` | `55.37%` | `0.81` | 7,660,000.00 USD |
| `4H` | `Bitget` | `45.38%` | `54.62%` | `0.83` | 5,820,000.00 USD |
| `4H` | `BingX` | `37.11%` | `62.89%` | `0.59` | 6,550,000.00 USD |
| `4H` | `MEXC` | `50.93%` | `49.07%` | `1.04` | 13,390,000.00 USD |
| `4H` | `Bitunix` | `56.53%` | `43.47%` | `1.30` | 3,560,000.00 USD |
| `4H` | `Hyperliquid` | `63.57%` | `36.43%` | `1.74` | 1,320,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `51.25%` | `48.75%` | `1.05` | 22,630,000.00 USD |
| `4H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `WhiteBIT` | `3.14%` | `96.86%` | `0.03` | 1,860,000.00 USD |
| `4H` | `HTX` | `49.71%` | `50.29%` | `0.99` | 424,490.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `48.69%` | `51.31%` | `0.95` | 488,570.00 USD |
| `4H` | `Aster` | `62.6%` | `37.4%` | `1.67` | 38,150.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `40.43%` | `59.57%` | `0.68` | 45,760.00 USD |
| `4H` | `Whale Positions` | `53.18%` | `46.82%` | `1.14` | 48,020,000.00 USD |
| `4H` | `Global Accounts` | `49.88%` | `50.12%` | `1.00` | 135,980,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `0:00 UTC` | `0.3313` | `0.3313` | `0.3313` | `0.3314` | `0.3311` | 227,097.79 USD | 135,693.64 USD | 91,404.16 USD | 44,289.48 USD | `+19.50%` | `7B / 7S` |
| `5:00 UTC` | `0.3313` | `0.3313` | `0.3313` | `0.3314` | `0.3312` | 291,403.53 USD | 122,949.99 USD | 168,453.54 USD | -45,503.55 USD | `-15.62%` | `6B / 8S` |
| `0:00 UTC` | `0.3312` | `0.3312` | `0.3312` | `0.3313` | `0.3311` | 269,940.33 USD | 150,060.53 USD | 119,879.80 USD | 30,180.73 USD | `+11.18%` | `8B / 5S` |
| `5:00 UTC` | `0.3313` | `0.3314` | `0.3313` | `0.3315` | `0.3312` | 203,963.74 USD | 113,592.33 USD | 90,371.41 USD | 23,220.91 USD | `+11.38%` | `7B / 2S` |
| `0:00 UTC` | `0.3315` | `0.3314` | `0.3315` | `0.3316` | `0.3313` | 521,667.70 USD | 331,816.53 USD | 189,851.17 USD | 141,965.36 USD | `+27.21%` | `14B / 7S` |
| `5:00 UTC` | `0.3313` | `0.3313` | `0.3313` | `0.3314` | `0.3312` | 182,734.27 USD | 70,327.25 USD | 112,407.03 USD | -42,079.78 USD | `-23.03%` | `4B / 3S` |
| `0:00 UTC` | `0.3312` | `0.3312` | `0.3312` | `0.3313` | `0.3312` | 179,833.13 USD | 50,346.37 USD | 129,486.77 USD | -79,140.40 USD | `-44.01%` | `3B / 3S` |
| `5:00 UTC` | `0.3312` | `0.3312` | `0.3312` | `0.3312` | `0.3311` | 145,155.84 USD | 46,671.46 USD | 98,484.38 USD | -51,812.92 USD | `-35.69%` | `2B / 3S` |
| `0:00 UTC` | `0.3312` | `0.3311` | `0.3312` | `0.3312` | `0.3310` | 301,237.68 USD | 114,043.04 USD | 187,194.64 USD | -73,151.60 USD | `-24.28%` | `3B / 9S` |
| `5:00 UTC` | `0.3312` | `0.3312` | `0.3312` | `0.3312` | `0.3311` | 167,586.30 USD | 65,507.43 USD | 102,078.87 USD | -36,571.45 USD | `-21.82%` | `3B / 11S` |

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
| `5m` | -1,080.00 USD | -41,930.00 USD | **`DISTRIBUTION`** |
| `15m` | 5,500.00 USD | -124,500.00 USD | **`DISTRIBUTION`** |
| `30m` | 17,750.00 USD | -184,690.00 USD | **`DISTRIBUTION`** |
| `1h` | -369.74 USD | -348,370.00 USD | **`DISTRIBUTION`** |
| `2h` | 473,870.00 USD | -230,760.00 USD | **`ACCUMULATION`** |
| `4h` | -13,380.00 USD | -215,470.00 USD | **`DISTRIBUTION`** |
| `6h` | -16,280.00 USD | -59,220.00 USD | **`DISTRIBUTION`** |
| `8h` | 34,500.00 USD | 352,370.00 USD | **`ACCUMULATION`** |
| `12h` | 267,010.00 USD | 129,180.00 USD | **`ACCUMULATION`** |
| `24h` | 4,400,000.00 USD | 3,490,000.00 USD | **`ACCUMULATION`** |
| `1w` | -4,750,000.00 USD | 964,120.00 USD | **`DISTRIBUTION`** |
| `30d` | -22,840,000.00 USD | 3,620,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-1.08K` | 15m=`+5.50K` | 1h=`-369.74` | 24h=`+4.40M`
* Futures Capital Netflows: 5m=`-41.93K` | 15m=`-124.50K` | 1h=`-348.37K` | 24h=`+3.49M`
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
  * `2026-10-29 22:45:14 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:06:14 IST`: [fxstreet.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:50:14 IST`: [ForexFactory] - (Sentiment: `Neutral`)
  * `2026-10-29 22:50:14 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-29 22:50:14 IST`: [youtube.com/bankofcanadaofficial] - (Sentiment: `Neutral`)
  * `2026-10-29 22:49:14 IST`: [notayesmanseconomics.wordpress.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:49:14 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:49:14 IST`: [breakingthenews.net] - (Sentiment: `Neutral`)
  * `2026-10-29 19:51:14 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-29 19:51:14 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-29 19:51:14 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-29 19:51:14 IST`: [youtube.com/ecbeuro] - (Sentiment: `Neutral`)
  * `2026-10-29 18:51:14 IST`: [ecb.europa.eu] - (Sentiment: `Neutral`)
  * `2026-10-29 18:51:14 IST`: [zerohedge.com] - (Sentiment: `Neutral`)
  * `2026-10-29 18:51:14 IST`: [dol.gov] - (Sentiment: `Neutral`)


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
  * Spread-Padded Stop Loss: `0.3272` (Risk Distance: `0.0022` pts)
  * +2.5R Take Profit: `0.3348`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `0.3312` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `0.3333` (Risk Distance: `0.0022` pts)
  * +2.5R Take Profit: `0.3257`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`0.3338`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
