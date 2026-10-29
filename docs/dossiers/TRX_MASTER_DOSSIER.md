# 🏛️ SOVEREIGN CANDIDATE DOSSIER: TRX
**Canonical Key**: `TRX` | **Broker Instrument**: `TRXUSD.p` | **Asset Class**: `Crypto Alt L1`
**Timestamp**: `2026-10-29 22:30:50 IST` (`2026-10-29 17:00:50 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `0.3307` | **Live Ask Quote**: `0.3318` | **Mid Price**: `0.3312`
- **Spread Points**: `11.00` | **Spread BPS**: `33.21 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `0.3300` | VWAP Z-Score: `+1.36` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `0.000345` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `61.37` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `0.3326` | Lower -3.00σ Band: `0.3275`
  * Upper +2.51σ Band: `0.3322` | Lower -2.51σ Band: `0.3279`
  * Upper +2.01σ Band: `0.3318` | Lower -2.01σ Band: `0.3283`
  * Upper +2.00σ Band: `0.3317` | Lower -2.00σ Band: `0.3284`
  * Upper +1.28σ Band: `0.3311` | Lower -1.28σ Band: `0.3290`
  * Upper +1.00σ Band: `0.3309` | Lower -1.00σ Band: `0.3292`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`0.3309` | EMA-20=`0.3308` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`0.3305` (Slope: `+0.0000`) | EMA-100=`0.3303`
  * Institutional Anchors: EMA-144=`0.3301` | EMA-200=`0.3299` (Slope: `+0.0391`) | EMA-233=`0.3298`
- **Range Boundaries**: 24H High=`0.3315` | 24H Low=`0.3285` | Weekly High=`0.3319` | Weekly Low=`0.3266`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `0.3312` (Distance: `+0.04%`)
  * Point of Control (POC) = `0.3308` (Distance: `+0.16%`)
  * Value Area Low (VAL) = `0.3291` (Distance: `+0.69%`)
  * Auction Positioning: `ABOVE_VALUE (Imbalance)` | Session Bias: **`BULLISH (Above Pivot)`** | Market Regime: `RANGE_EXPANSION`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`0.3314` | POC=`0.3309` | VAL=`0.3304`
  * Prior Day Extremes: PDH=`0.3319` | PDL=`0.3288` | PDC=`0.3289`
  * Monday Range Blueprint: High=`0.3310` | Mid=`0.3300` | Low=`0.3289`
  * Developing Weekly Value Area: Weekly VAH=`0.3312` | Weekly POC=`0.3308` | Weekly VAL=`0.3289`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`0.3306` | Low=`0.3285`
  * London Session (08:00-16:00 UTC): High=`0.3311` | Low=`0.3303`
  * New York Session (13:00-21:00 UTC): High=`0.3313` | Low=`0.3301`
  * Initial Balance (First Hour): IB High=`0.3311` | IB Low=`0.3303`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `0.3299` - `0.3326`
  * Optimal Trade Entry (OTE 0.705): `0.3319`
  * Structural Invalidation Anchor (0.786): `0.3339`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `0.3317` | `0.3317` | `0.3317` | `0.3317` | `612,606` | 203,216.95 USD | -145,090.15 USD | `-71.40%` | 315,793.07 USD | `-2.79` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `5m` | `0.3317` | `0.3317` | `0.3306` | `0.3309` | `6,474,084` | 2,143,535.70 USD | -531,954.89 USD | `-24.82%` | -216,161.82 USD | `-3.94` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `5m` | `0.3309` | `0.3314` | `0.3308` | `0.3314` | `1,292,087` | 427,984.34 USD | 288,459.44 USD | `+67.40%` | 72,297.63 USD | `+1.97` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `0.3316` | `0.3318` | `0.3316` | `0.3317` | `949,128` | 314,809.77 USD | 118,663.38 USD | `+37.69%` | 460,323.74 USD | `+1.52` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `0.3317` | `0.3318` | `0.3316` | `0.3317` | `753,170` | 249,844.27 USD | 559.48 USD | `+0.22%` | 460,883.22 USD | `-0.05` | **`BULLISH`** | `NEUTRAL CHOP` |
| `15m` | `0.3317` | `0.3317` | `0.3306` | `0.3314` | `8,380,257` | 2,775,227.48 USD | -388,095.11 USD | `-13.98%` | 72,788.11 USD | `-3.31` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `0.3315` | `0.3315` | `0.3312` | `0.3315` | `3,116,339` | 1,032,802.27 USD | 153,016.11 USD | `+14.82%` | 118,826.89 USD | `+0.12` | **`BULLISH`** | `DELTA ALIGNED` |
| `1h` | `0.3315` | `0.3318` | `0.3313` | `0.3317` | `3,447,199` | 1,143,159.79 USD | 322,125.82 USD | `+28.18%` | 440,952.71 USD | `+0.91` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `1h` | `0.3317` | `0.3317` | `0.3306` | `0.3314` | `8,380,257` | 2,775,227.48 USD | -388,095.11 USD | `-13.98%` | 52,857.60 USD | `-1.86` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.3307` | `0.3316` | `0.3306` | `0.3311` | `18,393,472` | 6,092,518.66 USD | 646,685.42 USD | `+10.61%` | 399,235.98 USD | `+0.56` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `0.3311` | `0.3316` | `0.3311` | `0.3315` | `11,939,433` | 3,956,492.73 USD | 16,254.19 USD | `+0.41%` | 415,490.17 USD | `-0.08` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `0.3315` | `0.3318` | `0.3306` | `0.3314` | `14,942,281` | 4,950,687.79 USD | 86,567.60 USD | `+1.75%` | 502,057.77 USD | `+0.00` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `0.3295` | `0.3299` | `0.3291` | `0.3296` | `11,620,721` | 3,828,700.92 USD | 746,764.34 USD | `+19.50%` | -848,336.50 USD | `+1.00` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `4h` | `0.3296` | `0.3308` | `0.3290` | `0.3307` | `23,140,787` | 7,631,473.08 USD | 600,887.06 USD | `+7.87%` | -247,449.44 USD | `+0.64` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `0.3307` | `0.3316` | `0.3306` | `0.3311` | `18,393,472` | 6,092,518.66 USD | 646,685.42 USD | `+10.61%` | 399,235.98 USD | `+0.56` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `0.3311` | `0.3316` | `0.3311` | `0.3315` | `11,939,433` | 3,956,492.73 USD | 16,254.19 USD | `+0.41%` | 415,490.17 USD | `-0.08` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `0.3315` | `0.3318` | `0.3306` | `0.3314` | `14,942,281` | 4,950,687.79 USD | 86,567.60 USD | `+1.75%` | 502,057.77 USD | `+0.00` | **`BULLISH`** | `BULLISH ABSORPTION` |

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
| --- | **`0.3312`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `MID` | Regular L2 Book | - | - | - | Interbank L2 | 0.00% | Interbank |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-29 19:44:05 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `1653` | `0xeadc...9d55` | `LONG` | 1,326,320.00 USD | `4,000,000.00` | `0.3421` | `0.3316` | `0.000000` | -42,158.09 USD | `-3.18%` | `10X Cross` |
| `1926` | `0xecb6...2b00` | `LONG` | 1,085,865.63 USD | `3,275,020.00` | `0.3306` | `0.3316` | `0.000000` | 3,014.01 USD | `+0.28%` | `10X Cross` |

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
  * 24H Horizon: Short MP=`0.3383` (Vol: 341,600.00 USD, Dist: `+2.08%`) | Long MP=`0.3250` (Vol: 314,500.00 USD, Dist: `--1.91%`)
  * 48H Horizon: Short MP=`0.3382` (Vol: 425,500.00 USD, Dist: `+2.06%`) | Long MP=`0.3249` (Vol: 425,500.00 USD, Dist: `--1.94%`)
  * 3D Horizon: Short MP=`0.3383` (Vol: 453,400.00 USD, Dist: `+2.10%`) | Long MP=`0.3250` (Vol: 454,200.00 USD, Dist: `--1.92%`)
  * 7D Horizon: Short MP=`0.3368` (Vol: 499,100.00 USD, Dist: `+1.66%`) | Long MP=`0.3250` (Vol: 515,000.00 USD, Dist: `--1.92%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long Liquidation` | `0.0685` | 3,070.00 USD | 511,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0715` | 6,310.00 USD | 508,250.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0805` | 167.36 USD | 501,940.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0965` | 449.21 USD | 501,780.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0985` | 295.50 USD | 501,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1025` | 4,190.00 USD | 501,030.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1115` | 1,430.00 USD | 496,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1155` | 274.54 USD | 495,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1175` | 394.80 USD | 495,140.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1195` | 4,730.00 USD | 494,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1275` | 1,450.00 USD | 490,020.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1375` | 30,210.00 USD | 488,580.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1405` | 429.65 USD | 458,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1465` | 698.66 USD | 457,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1525` | 137.86 USD | 457,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1595` | 390.46 USD | 457,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1605` | 12,330.00 USD | 456,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1685` | 509.04 USD | 444,380.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1705` | 20,360.00 USD | 443,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1735` | 11,160.00 USD | 423,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1745` | 3,960.00 USD | 412,350.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1755` | 1,030.00 USD | 408,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1765` | 4,200.00 USD | 407,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1775` | 1,320.00 USD | 403,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1795` | 209.84 USD | 401,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1805` | 451.61 USD | 401,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1895` | 1,150.00 USD | 401,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1905` | 527.11 USD | 400,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1975` | 632.00 USD | 399,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1995` | 2,980.00 USD | 398,880.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2045` | 6,130.00 USD | 395,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2115` | 221.02 USD | 389,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2145` | 3,330.00 USD | 389,540.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2175` | 1,520.00 USD | 386,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2195` | 515.17 USD | 384,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2255` | 4,590.00 USD | 384,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2265` | 2,390.00 USD | 379,580.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2305` | 4,180.00 USD | 377,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2315` | 2,730.00 USD | 373,010.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2325` | 636.35 USD | 370,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2335` | 2,370.00 USD | 369,640.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2345` | 729.53 USD | 367,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2355` | 6,430.00 USD | 366,540.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2365` | 344.11 USD | 360,110.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2385` | 1,260.00 USD | 359,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2405` | 181.58 USD | 358,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2445` | 1,220.00 USD | 358,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2455` | 466.70 USD | 357,100.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2465` | 461.45 USD | 356,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2475` | 2,420.00 USD | 356,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2565` | 1,230.00 USD | 353,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2585` | 1,580.00 USD | 352,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2595` | 315.81 USD | 350,940.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2605` | 8,650.00 USD | 350,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2615` | 760.97 USD | 341,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2635` | 108.56 USD | 341,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2645` | 23,160.00 USD | 341,100.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2655` | 7,970.00 USD | 317,940.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2675` | 194.47 USD | 309,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2685` | 637.42 USD | 309,780.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2725` | 412.84 USD | 309,140.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2735` | 5,500.00 USD | 308,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2745` | 40,290.00 USD | 303,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2755` | 84,780.00 USD | 262,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2775` | 487.29 USD | 178,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2785` | 2,130.00 USD | 177,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2795` | 14,320.00 USD | 175,540.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2805` | 6,280.00 USD | 161,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2815` | 1,310.00 USD | 154,940.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2825` | 15,060.00 USD | 153,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2835` | 1,430.00 USD | 138,570.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2865` | 360.42 USD | 137,140.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2905` | 1,620.00 USD | 136,780.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2915` | 591.45 USD | 135,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2925` | 957.64 USD | 134,570.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2945` | 3,760.00 USD | 133,610.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2955` | 125.29 USD | 129,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.2977` | 12,690,000.00 USD | 12,690,000.00 USD | 30,050.00 USD | 19,180.00 USD | 21,350.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.2981` | 2,620,000.00 USD | 2,620,000.00 USD | 9,650.00 USD | 4,860.00 USD | 6,630.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.2981` | 12,620,000.00 USD | 12,620,000.00 USD | 70,680.00 USD | 6,250.00 USD | 10,090.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.2985` | 2,600,000.00 USD | 2,600,000.00 USD | 83,020.00 USD | 12,430.00 USD | 15,260.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.2985` | 12,530,000.00 USD | 12,530,000.00 USD | 94,540.00 USD | 14,030.00 USD | 16,270.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.2989` | 2,490,000.00 USD | 2,490,000.00 USD | 6,700.00 USD | 560.05 USD | 2,050.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.2989` | 12,400,000.00 USD | 12,400,000.00 USD | 41,940.00 USD | 6,610.00 USD | 4,450.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.2993` | 12,350,000.00 USD | 12,350,000.00 USD | 6,450.00 USD | 2,190.00 USD | 2,060.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.2995` | 127.89 USD | 129,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3005` | 7,130.00 USD | 129,600.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3015` | 10,330.00 USD | 122,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3025` | 694.54 USD | 112,140.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3035` | 693.50 USD | 111,450.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3045` | 5,540.00 USD | 110,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.3053` | 12,340,000.00 USD | 12,340,000.00 USD | 1,340.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3055` | 5,300.00 USD | 105,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.3057` | 12,340,000.00 USD | 12,340,000.00 USD | 627.89 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3061` | 12,340,000.00 USD | 12,340,000.00 USD | 1,150.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3065` | 12,340,000.00 USD | 12,340,000.00 USD | 3,330.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3065` | 14,720.00 USD | 99,910.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3069` | 2,480,000.00 USD | 2,480,000.00 USD | 779.46 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3069` | 12,330,000.00 USD | 12,330,000.00 USD | 5,980.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3073` | 2,480,000.00 USD | 2,480,000.00 USD | 3,750.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3073` | 12,330,000.00 USD | 12,330,000.00 USD | 5,470.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3077` | 2,480,000.00 USD | 2,480,000.00 USD | 419.87 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3077` | 12,320,000.00 USD | 12,320,000.00 USD | 2,490.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3081` | 2,480,000.00 USD | 2,480,000.00 USD | 165.29 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3081` | 12,320,000.00 USD | 12,320,000.00 USD | 846.39 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3085` | 2,480,000.00 USD | 2,480,000.00 USD | 82.53 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3085` | 12,320,000.00 USD | 12,320,000.00 USD | 1,950.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3085` | 6,670.00 USD | 85,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3089` | 2,480,000.00 USD | 2,480,000.00 USD | 169.88 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3089` | 12,320,000.00 USD | 12,320,000.00 USD | 1,610.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3093` | 2,480,000.00 USD | 2,480,000.00 USD | 11.77 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3109` | 12,320,000.00 USD | 12,320,000.00 USD | 1,790.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3113` | 12,310,000.00 USD | 12,310,000.00 USD | 837.60 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3115` | 824.85 USD | 78,520.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.3117` | 12,310,000.00 USD | 12,310,000.00 USD | 1,530.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3121` | 12,310,000.00 USD | 12,310,000.00 USD | 4,450.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3125` | 2,480,000.00 USD | 2,480,000.00 USD | 1,040.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3125` | 12,310,000.00 USD | 12,310,000.00 USD | 7,970.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3125` | 17,130.00 USD | 77,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3129` | 2,480,000.00 USD | 2,480,000.00 USD | 5,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3129` | 12,300,000.00 USD | 12,300,000.00 USD | 7,300.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3133` | 2,470,000.00 USD | 2,470,000.00 USD | 560.10 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3133` | 12,290,000.00 USD | 12,290,000.00 USD | 3,330.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3135` | 44,390.00 USD | 60,570.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3137` | 2,470,000.00 USD | 2,470,000.00 USD | 220.50 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3137` | 12,290,000.00 USD | 12,290,000.00 USD | 1,130.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3141` | 2,470,000.00 USD | 2,470,000.00 USD | 68.20 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3141` | 12,290,000.00 USD | 12,290,000.00 USD | 80,880.00 USD | 17,190.00 USD | 3,890.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3145` | 2,470,000.00 USD | 2,470,000.00 USD | 268.50 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3145` | 12,190,000.00 USD | 12,190,000.00 USD | 166,120.00 USD | 34,080.00 USD | 13,980.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3145` | 2,140.00 USD | 16,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3149` | 2,470,000.00 USD | 2,470,000.00 USD | 15.70 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3149` | 11,970,000.00 USD | 11,970,000.00 USD | 236,810.00 USD | 21,430.00 USD | 70,440.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3153` | 11,640,000.00 USD | 11,640,000.00 USD | 75,860.00 USD | 24,680.00 USD | 30,770.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3155` | 142.29 USD | 14,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3157` | 2,470,000.00 USD | 2,470,000.00 USD | 0.00 USD | 0.00 USD | 10,130.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3157` | 11,510,000.00 USD | 11,510,000.00 USD | 312,790.00 USD | 82,280.00 USD | 50,710.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3161` | 2,460,000.00 USD | 2,460,000.00 USD | 50,830.00 USD | 27,400.00 USD | 29,700.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3161` | 11,070,000.00 USD | 11,070,000.00 USD | 319,190.00 USD | 104,020.00 USD | 113,580.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3165` | 2,350,000.00 USD | 2,350,000.00 USD | 80,750.00 USD | 25,700.00 USD | 41,090.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3165` | 10,530,000.00 USD | 10,530,000.00 USD | 294,750.00 USD | 90,340.00 USD | 147,570.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3165` | 1,490.00 USD | 13,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3169` | 2,200,000.00 USD | 2,200,000.00 USD | 31,910.00 USD | 17,870.00 USD | 17,650.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3169` | 10,000,000.00 USD | 10,000,000.00 USD | 253,960.00 USD | 84,130.00 USD | 102,520.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3173` | 2,140,000.00 USD | 2,140,000.00 USD | 13,380.00 USD | 5,370.00 USD | 3,660.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3173` | 9,560,000.00 USD | 9,560,000.00 USD | 177,330.00 USD | 59,550.00 USD | 57,040.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3175` | 938.85 USD | 12,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3177` | 2,110,000.00 USD | 2,110,000.00 USD | 24,040.00 USD | 6,720.00 USD | 4,570.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3177` | 9,260,000.00 USD | 9,260,000.00 USD | 132,600.00 USD | 19,590.00 USD | 21,290.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3181` | 2,080,000.00 USD | 2,080,000.00 USD | 167,760.00 USD | 38,060.00 USD | 44,870.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3181` | 9,090,000.00 USD | 9,090,000.00 USD | 371,010.00 USD | 41,640.00 USD | 75,140.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3185` | 1,830,000.00 USD | 1,830,000.00 USD | 143,440.00 USD | 15,020.00 USD | 14,300.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3185` | 8,600,000.00 USD | 8,600,000.00 USD | 206,150.00 USD | 26,900.00 USD | 20,240.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3185` | 335.70 USD | 11,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3189` | 1,660,000.00 USD | 1,660,000.00 USD | 6,040.00 USD | 1,400.00 USD | 1,420.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3189` | 8,350,000.00 USD | 8,350,000.00 USD | 92,860.00 USD | 33,430.00 USD | 16,310.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3193` | 8,200,000.00 USD | 8,200,000.00 USD | 16,110.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3195` | 126.84 USD | 11,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.3209` | 8,190,000.00 USD | 8,190,000.00 USD | 363,280.00 USD | 69,780.00 USD | 22,330.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3213` | 7,730,000.00 USD | 7,730,000.00 USD | 476,650.00 USD | 53,810.00 USD | 68,550.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3217` | 7,130,000.00 USD | 7,130,000.00 USD | 235,850.00 USD | 54,870.00 USD | 134,680.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3221` | 6,710,000.00 USD | 6,710,000.00 USD | 358,940.00 USD | 107,910.00 USD | 51,580.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3225` | 1,650,000.00 USD | 1,650,000.00 USD | 11,490.00 USD | 11,200.00 USD | 54,710.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3225` | 6,190,000.00 USD | 6,190,000.00 USD | 663,050.00 USD | 164,030.00 USD | 201,380.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3229` | 1,570,000.00 USD | 1,570,000.00 USD | 197,060.00 USD | 77,040.00 USD | 79,440.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3229` | 5,160,000.00 USD | 5,160,000.00 USD | 450,240.00 USD | 232,250.00 USD | 268,490.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3233` | 1,220,000.00 USD | 1,220,000.00 USD | 110,720.00 USD | 29,850.00 USD | 40,650.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3233` | 4,210,000.00 USD | 4,210,000.00 USD | 657,850.00 USD | 150,180.00 USD | 191,270.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.3235` | 11,000.00 USD | 11,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.3237` | 1,030,000.00 USD | 1,030,000.00 USD | 27,140.00 USD | 30,580.00 USD | 22,330.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3237` | 3,210,000.00 USD | 3,210,000.00 USD | 586,900.00 USD | 179,940.00 USD | 193,930.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3241` | 953,920.00 USD | 953,920.00 USD | 45,320.00 USD | 12,340.00 USD | 10,170.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3241` | 2,250,000.00 USD | 2,250,000.00 USD | 57,140.00 USD | 24,740.00 USD | 78,420.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3245` | 886,090.00 USD | 886,090.00 USD | 35,940.00 USD | 19,510.00 USD | 17,390.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3245` | 2,090,000.00 USD | 2,090,000.00 USD | 413,730.00 USD | 67,270.00 USD | 67,700.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3249` | 813,260.00 USD | 813,260.00 USD | 503,860.00 USD | 76,880.00 USD | 92,820.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3249` | 1,540,000.00 USD | 1,540,000.00 USD | 706,180.00 USD | 78,280.00 USD | 122,810.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3253` | 139,710.00 USD | 139,710.00 USD | 97,610.00 USD | 14,870.00 USD | 14,430.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3253` | 634,740.00 USD | 634,740.00 USD | 355,210.00 USD | 46,110.00 USD | 13,180.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.3257` | 12,790.00 USD | 12,790.00 USD | 7,150.00 USD | 2,800.00 USD | 2,850.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.3257` | 220,240.00 USD | 220,240.00 USD | 138,300.00 USD | 49,320.00 USD | 32,610.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3337` | 200,920.00 USD | 200,920.00 USD | 158,770.00 USD | 34,380.00 USD | 7,770.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3341` | 598,740.00 USD | 598,740.00 USD | 325,740.00 USD | 57,520.00 USD | 14,560.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3345` | 1,050,000.00 USD | 1,050,000.00 USD | 355,430.00 USD | 31,690.00 USD | 68,550.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3349` | 1,480,000.00 USD | 1,480,000.00 USD | 235,850.00 USD | 54,870.00 USD | 134,680.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3353` | 2,000,000.00 USD | 2,000,000.00 USD | 358,940.00 USD | 107,910.00 USD | 51,580.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3357` | 77,410.00 USD | 77,410.00 USD | 11,490.00 USD | 11,200.00 USD | 54,710.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3357` | 3,030,000.00 USD | 3,030,000.00 USD | 663,050.00 USD | 164,030.00 USD | 201,380.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3361` | 430,960.00 USD | 430,960.00 USD | 197,060.00 USD | 77,040.00 USD | 79,440.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3361` | 3,980,000.00 USD | 3,980,000.00 USD | 450,240.00 USD | 232,250.00 USD | 268,490.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3365` | 612,170.00 USD | 612,170.00 USD | 110,720.00 USD | 29,850.00 USD | 40,650.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3365` | 4,980,000.00 USD | 4,980,000.00 USD | 657,850.00 USD | 150,180.00 USD | 191,270.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3369` | 692,220.00 USD | 692,220.00 USD | 27,140.00 USD | 30,580.00 USD | 22,330.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3369` | 5,940,000.00 USD | 5,940,000.00 USD | 586,900.00 USD | 179,940.00 USD | 193,930.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3373` | 760,050.00 USD | 760,050.00 USD | 45,320.00 USD | 12,340.00 USD | 10,170.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3373` | 6,100,000.00 USD | 6,100,000.00 USD | 57,140.00 USD | 24,740.00 USD | 78,420.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3377` | 832,880.00 USD | 832,880.00 USD | 35,940.00 USD | 19,510.00 USD | 17,390.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3377` | 6,650,000.00 USD | 6,650,000.00 USD | 413,730.00 USD | 67,270.00 USD | 67,700.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3381` | 1,510,000.00 USD | 1,510,000.00 USD | 503,860.00 USD | 76,880.00 USD | 92,820.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3381` | 7,550,000.00 USD | 7,550,000.00 USD | 706,180.00 USD | 78,280.00 USD | 122,810.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3385` | 1,630,000.00 USD | 1,630,000.00 USD | 97,610.00 USD | 14,870.00 USD | 14,430.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3385` | 7,970,000.00 USD | 7,970,000.00 USD | 355,210.00 USD | 46,110.00 USD | 13,180.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3389` | 1,650,000.00 USD | 1,650,000.00 USD | 7,150.00 USD | 2,800.00 USD | 2,850.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3389` | 8,190,000.00 USD | 8,190,000.00 USD | 138,300.00 USD | 49,320.00 USD | 32,610.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3405` | 8,420,000.00 USD | 8,420,000.00 USD | 181,640.00 USD | 34,890.00 USD | 11,170.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3409` | 8,620,000.00 USD | 8,620,000.00 USD | 168,750.00 USD | 16,380.00 USD | 21,590.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3413` | 8,910,000.00 USD | 8,910,000.00 USD | 187,500.00 USD | 31,750.00 USD | 71,410.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3417` | 9,130,000.00 USD | 9,130,000.00 USD | 157,220.00 USD | 40,480.00 USD | 22,590.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3421` | 1,660,000.00 USD | 1,660,000.00 USD | 0.00 USD | 0.00 USD | 10,130.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3421` | 9,410,000.00 USD | 9,410,000.00 USD | 172,590.00 USD | 56,170.00 USD | 43,020.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3425` | 1,760,000.00 USD | 1,760,000.00 USD | 50,830.00 USD | 27,400.00 USD | 29,700.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3425` | 9,940,000.00 USD | 9,940,000.00 USD | 319,190.00 USD | 104,020.00 USD | 113,580.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3425` | 456.55 USD | 456.55 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.3429` | 1,910,000.00 USD | 1,910,000.00 USD | 80,750.00 USD | 25,700.00 USD | 41,090.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3429` | 10,480,000.00 USD | 10,480,000.00 USD | 294,750.00 USD | 90,340.00 USD | 147,570.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3433` | 1,980,000.00 USD | 1,980,000.00 USD | 31,910.00 USD | 17,870.00 USD | 17,650.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3433` | 10,920,000.00 USD | 10,920,000.00 USD | 253,960.00 USD | 84,130.00 USD | 102,520.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3435` | 153.89 USD | 610.44 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.3437` | 2,000,000.00 USD | 2,000,000.00 USD | 13,380.00 USD | 5,370.00 USD | 3,660.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3437` | 11,210,000.00 USD | 11,210,000.00 USD | 179,120.00 USD | 59,550.00 USD | 57,040.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3441` | 2,040,000.00 USD | 2,040,000.00 USD | 24,040.00 USD | 6,720.00 USD | 4,570.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3441` | 11,390,000.00 USD | 11,390,000.00 USD | 133,430.00 USD | 19,590.00 USD | 21,290.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3445` | 2,090,000.00 USD | 2,090,000.00 USD | 27,290.00 USD | 12,310.00 USD | 11,070.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3445` | 11,610,000.00 USD | 11,610,000.00 USD | 170,920.00 USD | 19,470.00 USD | 38,400.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3445` | 5,290.00 USD | 5,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.3449` | 2,430,000.00 USD | 2,430,000.00 USD | 257,620.00 USD | 36,750.00 USD | 44,400.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3449` | 12,060,000.00 USD | 12,060,000.00 USD | 356,540.00 USD | 39,230.00 USD | 50,390.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3453` | 2,470,000.00 USD | 2,470,000.00 USD | 33,370.00 USD | 5,410.00 USD | 5,120.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3453` | 12,210,000.00 USD | 12,210,000.00 USD | 113,470.00 USD | 29,330.00 USD | 11,120.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3455` | 486.46 USD | 6,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.3457` | 2,470,000.00 USD | 2,470,000.00 USD | 3,400.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3457` | 12,300,000.00 USD | 12,300,000.00 USD | 63,790.00 USD | 13,950.00 USD | 11,780.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3461` | 2,480,000.00 USD | 2,480,000.00 USD | 2,040.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3461` | 12,310,000.00 USD | 12,310,000.00 USD | 3,800.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3465` | 2,480,000.00 USD | 2,480,000.00 USD | 344.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3465` | 12,310,000.00 USD | 12,310,000.00 USD | 2,910.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3469` | 2,480,000.00 USD | 2,480,000.00 USD | 68.20 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3469` | 12,310,000.00 USD | 12,310,000.00 USD | 1,600.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3473` | 2,480,000.00 USD | 2,480,000.00 USD | 144.30 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3473` | 12,310,000.00 USD | 12,310,000.00 USD | 1,790.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3475` | 11,520.00 USD | 17,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.3477` | 2,480,000.00 USD | 2,480,000.00 USD | 124.20 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3477` | 12,320,000.00 USD | 12,320,000.00 USD | 1,770.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3481` | 2,480,000.00 USD | 2,480,000.00 USD | 15.70 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3485` | 223.04 USD | 18,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.3489` | 12,320,000.00 USD | 12,320,000.00 USD | 380.73 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3493` | 12,320,000.00 USD | 12,320,000.00 USD | 1,380.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3497` | 12,320,000.00 USD | 12,320,000.00 USD | 212.37 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3501` | 12,320,000.00 USD | 12,320,000.00 USD | 1,150.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3505` | 12,320,000.00 USD | 12,320,000.00 USD | 3,330.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3505` | 177,540.00 USD | 195,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.3509` | 2,480,000.00 USD | 2,480,000.00 USD | 779.46 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3509` | 12,330,000.00 USD | 12,330,000.00 USD | 5,980.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3513` | 2,480,000.00 USD | 2,480,000.00 USD | 2,550.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3513` | 12,330,000.00 USD | 12,330,000.00 USD | 3,470.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3517` | 2,480,000.00 USD | 2,480,000.00 USD | 1,530.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3517` | 12,340,000.00 USD | 12,340,000.00 USD | 2,850.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3521` | 2,480,000.00 USD | 2,480,000.00 USD | 257.87 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3521` | 12,340,000.00 USD | 12,340,000.00 USD | 2,180.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3525` | 2,480,000.00 USD | 2,480,000.00 USD | 51.12 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3525` | 12,340,000.00 USD | 12,340,000.00 USD | 1,200.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3529` | 2,480,000.00 USD | 2,480,000.00 USD | 31.41 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3529` | 12,340,000.00 USD | 12,340,000.00 USD | 1,050.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3533` | 2,480,000.00 USD | 2,480,000.00 USD | 169.88 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3533` | 12,340,000.00 USD | 12,340,000.00 USD | 1,610.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3535` | 223.06 USD | 195,890.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.3537` | 2,480,000.00 USD | 2,480,000.00 USD | 11.77 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3575` | 193.41 USD | 196,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.3597` | 12,340,000.00 USD | 12,340,000.00 USD | 253.95 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3601` | 12,400,000.00 USD | 12,400,000.00 USD | 45,620.00 USD | 8,790.00 USD | 2,910.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3605` | 12,440,000.00 USD | 12,440,000.00 USD | 36,500.00 USD | 4,770.00 USD | 4,480.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3609` | 12,530,000.00 USD | 12,530,000.00 USD | 61,140.00 USD | 4,530.00 USD | 19,330.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3613` | 12,560,000.00 USD | 12,560,000.00 USD | 18,630.00 USD | 6,220.00 USD | 1,750.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3617` | 2,480,000.00 USD | 2,480,000.00 USD | 147.90 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3617` | 12,670,000.00 USD | 12,670,000.00 USD | 90,720.00 USD | 17,690.00 USD | 7,950.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3621` | 2,500,000.00 USD | 2,500,000.00 USD | 5,430.00 USD | 4,190.00 USD | 12,470.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3621` | 12,850,000.00 USD | 12,850,000.00 USD | 100,270.00 USD | 25,060.00 USD | 49,710.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3625` | 2,550,000.00 USD | 2,550,000.00 USD | 27,340.00 USD | 9,180.00 USD | 9,830.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3625` | 12,950,000.00 USD | 12,950,000.00 USD | 47,030.00 USD | 26,380.00 USD | 31,910.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3629` | 2,580,000.00 USD | 2,580,000.00 USD | 14,890.00 USD | 4,050.00 USD | 5,930.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3629` | 13,110,000.00 USD | 13,110,000.00 USD | 100,040.00 USD | 23,970.00 USD | 28,680.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3633` | 2,580,000.00 USD | 2,580,000.00 USD | 58.95 USD | 4,320.00 USD | 4,470.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3633` | 13,240,000.00 USD | 13,240,000.00 USD | 85,560.00 USD | 25,840.00 USD | 22,280.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3637` | 2,590,000.00 USD | 2,590,000.00 USD | 4,730.00 USD | 799.58 USD | 1,460.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3637` | 13,250,000.00 USD | 13,250,000.00 USD | 7,160.00 USD | 3,030.00 USD | 5,680.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3641` | 2,600,000.00 USD | 2,600,000.00 USD | 6,770.00 USD | 3,200.00 USD | 2,370.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3641` | 13,320,000.00 USD | 13,320,000.00 USD | 58,240.00 USD | 5,560.00 USD | 4,890.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3645` | 2,680,000.00 USD | 2,680,000.00 USD | 50,400.00 USD | 9,160.00 USD | 14,390.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3645` | 13,430,000.00 USD | 13,430,000.00 USD | 80,460.00 USD | 7,810.00 USD | 21,560.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3645` | 376.53 USD | 196,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.3649` | 2,720,000.00 USD | 2,720,000.00 USD | 37,500.00 USD | 4,930.00 USD | 3,670.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.3649` | 13,490,000.00 USD | 13,490,000.00 USD | 44,110.00 USD | 7,960.00 USD | 3,530.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.3651` | 2,730,000.00 USD | 2,730,000.00 USD | 5,270.00 USD | 0.00 USD | 1,480.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.3665` | 262.78 USD | 196,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3745` | 6,690.00 USD | 203,410.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3785` | 537.85 USD | 203,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3795` | 557,900.00 USD | 761,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3815` | 285.74 USD | 762,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3845` | 115.35 USD | 762,250.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3895` | 6,280.00 USD | 768,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3905` | 4,770.00 USD | 773,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3915` | 487.42 USD | 773,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3945` | 1,490.00 USD | 775,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3955` | 118,430.00 USD | 893,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4165` | 4,440.00 USD | 898,140.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4185` | 167.40 USD | 898,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4255` | 51,950.00 USD | 950,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4445` | 72,350.00 USD | 1,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4475` | 1,020.00 USD | 1,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4705` | 203.26 USD | 1,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4875` | 2,810.00 USD | 1,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4905` | 841.21 USD | 1,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4915` | 5,130.00 USD | 1,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.5345` | 669.73 USD | 1,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.5415` | 18,630.00 USD | 1,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.5485` | 711,540.00 USD | 1,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.5585` | 742.25 USD | 1,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.5625` | 140.62 USD | 1,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.5655` | 209.80 USD | 1,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.6145` | 36,870.00 USD | 1,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.6275` | 275.47 USD | 1,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.6285` | 7,390.00 USD | 1,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.6315` | 340.38 USD | 1,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `0.0685` | 511,320.00 USD | 0.00 USD | 3,070.00 USD | `-79.36%` | `44,767.00` |
| `Live` | `Long` | `0.0715` | 508,250.00 USD | 0.00 USD | 6,310.00 USD | `-78.46%` | `88,233.00` |
| `Live` | `Long` | `0.0805` | 501,940.00 USD | 0.00 USD | 167.36 USD | `-75.75%` | `2,079.00` |
| `Live` | `Long` | `0.0965` | 501,780.00 USD | 0.00 USD | 449.21 USD | `-70.93%` | `4,655.00` |
| `Live` | `Long` | `0.0985` | 501,330.00 USD | 0.00 USD | 295.50 USD | `-70.33%` | `3,000.00` |
| `Live` | `Long` | `0.1025` | 501,030.00 USD | 0.00 USD | 4,190.00 USD | `-69.12%` | `40,871.00` |
| `Live` | `Long` | `0.1115` | 496,840.00 USD | 0.00 USD | 1,430.00 USD | `-66.41%` | `12,781.00` |
| `Live` | `Long` | `0.1155` | 495,420.00 USD | 0.00 USD | 274.54 USD | `-65.21%` | `2,377.00` |
| `Live` | `Long` | `0.1175` | 495,140.00 USD | 0.00 USD | 394.80 USD | `-64.60%` | `3,360.00` |
| `Live` | `Long` | `0.1195` | 494,750.00 USD | 0.00 USD | 4,730.00 USD | `-64.00%` | `39,551.00` |
| `Live` | `Long` | `0.1275` | 490,020.00 USD | 0.00 USD | 1,450.00 USD | `-61.59%` | `11,352.00` |
| `Live` | `Long` | `0.1375` | 488,580.00 USD | 0.00 USD | 30,210.00 USD | `-58.58%` | `219,745.00` |
| `Live` | `Long` | `0.1405` | 458,360.00 USD | 0.00 USD | 429.65 USD | `-57.68%` | `3,058.00` |
| `Live` | `Long` | `0.1465` | 457,930.00 USD | 0.00 USD | 698.66 USD | `-55.87%` | `4,769.00` |
| `Live` | `Long` | `0.1525` | 457,230.00 USD | 0.00 USD | 137.86 USD | `-54.06%` | `904.00` |
| `Live` | `Long` | `0.1595` | 457,090.00 USD | 0.00 USD | 390.46 USD | `-51.95%` | `2,448.00` |
| `Live` | `Long` | `0.1605` | 456,700.00 USD | 0.00 USD | 12,330.00 USD | `-51.65%` | `76,797.00` |
| `Live` | `Long` | `0.1685` | 444,380.00 USD | 0.00 USD | 509.04 USD | `-49.24%` | `3,021.00` |
| `Live` | `Long` | `0.1705` | 443,870.00 USD | 0.00 USD | 20,360.00 USD | `-48.64%` | `119,400.00` |
| `Live` | `Long` | `0.1735` | 423,510.00 USD | 0.00 USD | 11,160.00 USD | `-47.73%` | `64,322.00` |
| `Live` | `Long` | `0.1745` | 412,350.00 USD | 0.00 USD | 3,960.00 USD | `-47.43%` | `22,702.00` |
| `Live` | `Long` | `0.1755` | 408,390.00 USD | 0.00 USD | 1,030.00 USD | `-47.13%` | `5,865.00` |
| `Live` | `Long` | `0.1765` | 407,360.00 USD | 0.00 USD | 4,200.00 USD | `-46.83%` | `23,777.00` |
| `Live` | `Long` | `0.1775` | 403,160.00 USD | 0.00 USD | 1,320.00 USD | `-46.53%` | `7,431.00` |
| `Live` | `Long` | `0.1795` | 401,840.00 USD | 0.00 USD | 209.84 USD | `-45.93%` | `1,169.00` |
| `Live` | `Long` | `0.1805` | 401,630.00 USD | 0.00 USD | 451.61 USD | `-45.63%` | `2,502.00` |
| `Live` | `Long` | `0.1895` | 401,180.00 USD | 0.00 USD | 1,150.00 USD | `-42.91%` | `6,059.00` |
| `Live` | `Long` | `0.1905` | 400,040.00 USD | 0.00 USD | 527.11 USD | `-42.61%` | `2,767.00` |
| `Live` | `Long` | `0.1975` | 399,510.00 USD | 0.00 USD | 632.00 USD | `-40.50%` | `3,200.00` |
| `Live` | `Long` | `0.1995` | 398,880.00 USD | 0.00 USD | 2,980.00 USD | `-39.90%` | `14,921.00` |
| `Live` | `Long` | `0.2045` | 395,900.00 USD | 0.00 USD | 6,130.00 USD | `-38.40%` | `30,000.00` |
| `Live` | `Long` | `0.2115` | 389,760.00 USD | 0.00 USD | 221.02 USD | `-36.29%` | `1,045.00` |
| `Live` | `Long` | `0.2145` | 389,540.00 USD | 0.00 USD | 3,330.00 USD | `-35.38%` | `15,528.00` |
| `Live` | `Long` | `0.2175` | 386,210.00 USD | 0.00 USD | 1,520.00 USD | `-34.48%` | `7,003.00` |
| `Live` | `Long` | `0.2195` | 384,690.00 USD | 0.00 USD | 515.17 USD | `-33.88%` | `2,347.00` |
| `Live` | `Long` | `0.2255` | 384,170.00 USD | 0.00 USD | 4,590.00 USD | `-32.07%` | `20,360.00` |
| `Live` | `Long` | `0.2265` | 379,580.00 USD | 0.00 USD | 2,390.00 USD | `-31.77%` | `10,560.00` |
| `Live` | `Long` | `0.2305` | 377,190.00 USD | 0.00 USD | 4,180.00 USD | `-30.56%` | `18,150.00` |
| `Live` | `Long` | `0.2315` | 373,010.00 USD | 0.00 USD | 2,730.00 USD | `-30.26%` | `11,792.00` |
| `Live` | `Long` | `0.2325` | 370,280.00 USD | 0.00 USD | 636.35 USD | `-29.96%` | `2,737.00` |
| `Live` | `Long` | `0.2335` | 369,640.00 USD | 0.00 USD | 2,370.00 USD | `-29.66%` | `10,154.00` |
| `Live` | `Long` | `0.2345` | 367,270.00 USD | 0.00 USD | 729.53 USD | `-29.36%` | `3,111.00` |
| `Live` | `Long` | `0.2355` | 366,540.00 USD | 0.00 USD | 6,430.00 USD | `-29.06%` | `27,308.00` |
| `Live` | `Long` | `0.2365` | 360,110.00 USD | 0.00 USD | 344.11 USD | `-28.76%` | `1,455.00` |
| `Live` | `Long` | `0.2385` | 359,770.00 USD | 0.00 USD | 1,260.00 USD | `-28.15%` | `5,298.00` |
| `Live` | `Long` | `0.2405` | 358,500.00 USD | 0.00 USD | 181.58 USD | `-27.55%` | `755.00` |
| `Live` | `Long` | `0.2445` | 358,320.00 USD | 0.00 USD | 1,220.00 USD | `-26.35%` | `5,004.00` |
| `Live` | `Long` | `0.2455` | 357,100.00 USD | 0.00 USD | 466.70 USD | `-26.05%` | `1,901.00` |
| `Live` | `Long` | `0.2465` | 356,630.00 USD | 0.00 USD | 461.45 USD | `-25.74%` | `1,872.00` |
| `Live` | `Long` | `0.2475` | 356,170.00 USD | 0.00 USD | 2,420.00 USD | `-25.44%` | `9,797.00` |
| `Live` | `Long` | `0.2565` | 353,740.00 USD | 0.00 USD | 1,230.00 USD | `-22.73%` | `4,794.00` |
| `Live` | `Long` | `0.2585` | 352,510.00 USD | 0.00 USD | 1,580.00 USD | `-22.13%` | `6,097.00` |
| `Live` | `Long` | `0.2595` | 350,940.00 USD | 0.00 USD | 315.81 USD | `-21.83%` | `1,217.00` |
| `Live` | `Long` | `0.2605` | 350,620.00 USD | 0.00 USD | 8,650.00 USD | `-21.53%` | `33,208.00` |
| `Live` | `Long` | `0.2615` | 341,970.00 USD | 0.00 USD | 760.97 USD | `-21.23%` | `2,910.00` |
| `Live` | `Long` | `0.2635` | 341,210.00 USD | 0.00 USD | 108.56 USD | `-20.62%` | `412.00` |
| `Live` | `Long` | `0.2645` | 341,100.00 USD | 0.00 USD | 23,160.00 USD | `-20.32%` | `87,573.00` |
| `Live` | `Long` | `0.2655` | 317,940.00 USD | 0.00 USD | 7,970.00 USD | `-20.02%` | `30,017.00` |
| `Live` | `Long` | `0.2675` | 309,970.00 USD | 0.00 USD | 194.47 USD | `-19.42%` | `727.00` |
| `Live` | `Long` | `0.2685` | 309,780.00 USD | 0.00 USD | 637.42 USD | `-19.12%` | `2,374.00` |
| `Live` | `Long` | `0.2725` | 309,140.00 USD | 0.00 USD | 412.84 USD | `-17.91%` | `1,515.00` |
| `Live` | `Long` | `0.2735` | 308,730.00 USD | 0.00 USD | 5,500.00 USD | `-17.61%` | `20,120.00` |
| `Live` | `Long` | `0.2745` | 303,220.00 USD | 0.00 USD | 40,290.00 USD | `-17.31%` | `146,785.00` |
| `Live` | `Long` | `0.2755` | 262,930.00 USD | 0.00 USD | 84,780.00 USD | `-17.01%` | `307,728.00` |
| `Live` | `Long` | `0.2775` | 178,150.00 USD | 0.00 USD | 487.29 USD | `-16.41%` | `1,756.00` |
| `Live` | `Long` | `0.2785` | 177,660.00 USD | 0.00 USD | 2,130.00 USD | `-16.10%` | `7,634.00` |
| `Live` | `Long` | `0.2795` | 175,540.00 USD | 0.00 USD | 14,320.00 USD | `-15.80%` | `51,232.00` |
| `Live` | `Long` | `0.2805` | 161,220.00 USD | 0.00 USD | 6,280.00 USD | `-15.50%` | `22,380.00` |
| `Live` | `Long` | `0.2815` | 154,940.00 USD | 0.00 USD | 1,310.00 USD | `-15.20%` | `4,642.00` |
| `Live` | `Long` | `0.2825` | 153,630.00 USD | 0.00 USD | 15,060.00 USD | `-14.90%` | `53,321.00` |
| `Live` | `Long` | `0.2835` | 138,570.00 USD | 0.00 USD | 1,430.00 USD | `-14.60%` | `5,038.00` |
| `Live` | `Long` | `0.2865` | 137,140.00 USD | 0.00 USD | 360.42 USD | `-13.69%` | `1,258.00` |
| `Live` | `Long` | `0.2905` | 136,780.00 USD | 0.00 USD | 1,620.00 USD | `-12.49%` | `5,572.00` |
| `Live` | `Long` | `0.2915` | 135,160.00 USD | 0.00 USD | 591.45 USD | `-12.19%` | `2,029.00` |
| `Live` | `Long` | `0.2925` | 134,570.00 USD | 0.00 USD | 957.64 USD | `-11.89%` | `3,274.00` |
| `Live` | `Long` | `0.2945` | 133,610.00 USD | 0.00 USD | 3,760.00 USD | `-11.28%` | `12,780.00` |
| `Live` | `Long` | `0.2955` | 129,850.00 USD | 0.00 USD | 125.29 USD | `-10.98%` | `424.00` |
| `Live` | `Long` | `0.2995` | 129,730.00 USD | 0.00 USD | 127.89 USD | `-9.78%` | `427.00` |
| `Live` | `Long` | `0.3005` | 129,600.00 USD | 0.00 USD | 7,130.00 USD | `-9.48%` | `23,720.00` |
| `Live` | `Long` | `0.3015` | 122,470.00 USD | 0.00 USD | 10,330.00 USD | `-9.18%` | `34,248.00` |
| `Live` | `Long` | `0.3025` | 112,140.00 USD | 0.00 USD | 694.54 USD | `-8.87%` | `2,296.00` |
| `Live` | `Long` | `0.3035` | 111,450.00 USD | 0.00 USD | 693.50 USD | `-8.57%` | `2,285.00` |
| `Live` | `Long` | `0.3045` | 110,760.00 USD | 0.00 USD | 5,540.00 USD | `-8.27%` | `18,206.00` |
| `Live` | `Long` | `0.3055` | 105,210.00 USD | 0.00 USD | 5,300.00 USD | `-7.97%` | `17,354.00` |
| `Live` | `Long` | `0.3065` | 99,910.00 USD | 0.00 USD | 14,720.00 USD | `-7.67%` | `48,026.00` |
| `Live` | `Long` | `0.3085` | 85,190.00 USD | 0.00 USD | 6,670.00 USD | `-7.07%` | `21,612.00` |
| `Live` | `Long` | `0.3115` | 78,520.00 USD | 0.00 USD | 824.85 USD | `-6.16%` | `2,648.00` |
| `Live` | `Long` | `0.3125` | 77,700.00 USD | 0.00 USD | 17,130.00 USD | `-5.86%` | `54,813.00` |
| `Live` | `Long` | `0.3135` | 60,570.00 USD | 0.00 USD | 44,390.00 USD | `-5.56%` | `141,602.00` |
| `Live` | `Long` | `0.3145` | 16,180.00 USD | 0.00 USD | 2,140.00 USD | `-5.26%` | `6,799.00` |
| `Live` | `Long` | `0.3155` | 14,040.00 USD | 0.00 USD | 142.29 USD | `-4.96%` | `451.00` |
| `Live` | `Long` | `0.3165` | 13,900.00 USD | 0.00 USD | 1,490.00 USD | `-4.66%` | `4,723.00` |
| `Live` | `Long` | `0.3175` | 12,400.00 USD | 0.00 USD | 938.85 USD | `-4.36%` | `2,957.00` |
| `Live` | `Long` | `0.3185` | 11,460.00 USD | 0.00 USD | 335.70 USD | `-4.05%` | `1,054.00` |
| `Live` | `Long` | `0.3195` | 11,130.00 USD | 0.00 USD | 126.84 USD | `-3.75%` | `397.00` |
| `Live` | `Long` | `0.3235` | 11,000.00 USD | 0.00 USD | 11,000.00 USD | `-2.55%` | `34,003.00` |
| `Live` | `Short` | `0.3425` | 456.55 USD | 456.55 USD | 0.00 USD | `+3.18%` | `1,333.00` |
| `Live` | `Short` | `0.3435` | 610.44 USD | 153.89 USD | 0.00 USD | `+3.48%` | `448.00` |
| `Live` | `Short` | `0.3445` | 5,900.00 USD | 5,290.00 USD | 0.00 USD | `+3.78%` | `15,355.00` |
| `Live` | `Short` | `0.3455` | 6,390.00 USD | 486.46 USD | 0.00 USD | `+4.08%` | `1,408.00` |
| `Live` | `Short` | `0.3475` | 17,900.00 USD | 11,520.00 USD | 0.00 USD | `+4.68%` | `33,140.00` |
| `Live` | `Short` | `0.3485` | 18,130.00 USD | 223.04 USD | 0.00 USD | `+4.98%` | `640.00` |
| `Live` | `Short` | `0.3505` | 195,660.00 USD | 177,540.00 USD | 0.00 USD | `+5.59%` | `506,529.00` |
| `Live` | `Short` | `0.3535` | 195,890.00 USD | 223.06 USD | 0.00 USD | `+6.49%` | `631.00` |
| `Live` | `Short` | `0.3575` | 196,080.00 USD | 193.41 USD | 0.00 USD | `+7.69%` | `541.00` |
| `Live` | `Short` | `0.3645` | 196,460.00 USD | 376.53 USD | 0.00 USD | `+9.80%` | `1,033.00` |
| `Live` | `Short` | `0.3665` | 196,720.00 USD | 262.78 USD | 0.00 USD | `+10.40%` | `717.00` |
| `Live` | `Short` | `0.3745` | 203,410.00 USD | 6,690.00 USD | 0.00 USD | `+12.81%` | `17,870.00` |
| `Live` | `Short` | `0.3785` | 203,950.00 USD | 537.85 USD | 0.00 USD | `+14.02%` | `1,421.00` |
| `Live` | `Short` | `0.3795` | 761,850.00 USD | 557,900.00 USD | 0.00 USD | `+14.32%` | `1,470,083.00` |
| `Live` | `Short` | `0.3815` | 762,130.00 USD | 285.74 USD | 0.00 USD | `+14.92%` | `749.00` |
| `Live` | `Short` | `0.3845` | 762,250.00 USD | 115.35 USD | 0.00 USD | `+15.83%` | `300.00` |
| `Live` | `Short` | `0.3895` | 768,530.00 USD | 6,280.00 USD | 0.00 USD | `+17.33%` | `16,133.00` |
| `Live` | `Short` | `0.3905` | 773,300.00 USD | 4,770.00 USD | 0.00 USD | `+17.63%` | `12,210.00` |
| `Live` | `Short` | `0.3915` | 773,790.00 USD | 487.42 USD | 0.00 USD | `+17.94%` | `1,245.00` |
| `Live` | `Short` | `0.3945` | 775,270.00 USD | 1,490.00 USD | 0.00 USD | `+18.84%` | `3,770.00` |
| `Live` | `Short` | `0.3955` | 893,700.00 USD | 118,430.00 USD | 0.00 USD | `+19.14%` | `299,436.00` |
| `Live` | `Short` | `0.4165` | 898,140.00 USD | 4,440.00 USD | 0.00 USD | `+25.47%` | `10,665.00` |
| `Live` | `Short` | `0.4185` | 898,310.00 USD | 167.40 USD | 0.00 USD | `+26.07%` | `400.00` |
| `Live` | `Short` | `0.4255` | 950,260.00 USD | 51,950.00 USD | 0.00 USD | `+28.18%` | `122,096.00` |
| `Live` | `Short` | `0.4445` | 1,020,000.00 USD | 72,350.00 USD | 0.00 USD | `+33.90%` | `162,775.00` |
| `Live` | `Short` | `0.4475` | 1,020,000.00 USD | 1,020.00 USD | 0.00 USD | `+34.81%` | `2,284.00` |
| `Live` | `Short` | `0.4705` | 1,020,000.00 USD | 203.26 USD | 0.00 USD | `+41.73%` | `432.00` |
| `Live` | `Short` | `0.4875` | 1,030,000.00 USD | 2,810.00 USD | 0.00 USD | `+46.86%` | `5,769.00` |
| `Live` | `Short` | `0.4905` | 1,030,000.00 USD | 841.21 USD | 0.00 USD | `+47.76%` | `1,715.00` |
| `Live` | `Short` | `0.4915` | 1,030,000.00 USD | 5,130.00 USD | 0.00 USD | `+48.06%` | `10,430.00` |
| `Live` | `Short` | `0.5345` | 1,030,000.00 USD | 669.73 USD | 0.00 USD | `+61.01%` | `1,253.00` |
| `Live` | `Short` | `0.5415` | 1,050,000.00 USD | 18,630.00 USD | 0.00 USD | `+63.12%` | `34,396.00` |
| `Live` | `Short` | `0.5485` | 1,760,000.00 USD | 711,540.00 USD | 0.00 USD | `+65.23%` | `1,297,248.00` |
| `Live` | `Short` | `0.5585` | 1,760,000.00 USD | 742.25 USD | 0.00 USD | `+68.24%` | `1,329.00` |
| `Live` | `Short` | `0.5625` | 1,760,000.00 USD | 140.62 USD | 0.00 USD | `+69.45%` | `250.00` |
| `Live` | `Short` | `0.5655` | 1,760,000.00 USD | 209.80 USD | 0.00 USD | `+70.35%` | `371.00` |
| `Live` | `Short` | `0.6145` | 1,800,000.00 USD | 36,870.00 USD | 0.00 USD | `+85.11%` | `60,000.00` |
| `Live` | `Short` | `0.6275` | 1,800,000.00 USD | 275.47 USD | 0.00 USD | `+89.03%` | `439.00` |
| `Live` | `Short` | `0.6285` | 1,810,000.00 USD | 7,390.00 USD | 0.00 USD | `+89.33%` | `11,753.00` |
| `Live` | `Short` | `0.6315` | 1,810,000.00 USD | 340.38 USD | 0.00 USD | `+90.23%` | `539.00` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `0.1805` | 826,950.00 USD | 0.00 USD | 6,100.00 USD | `-45.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2035` | 820,850.00 USD | 0.00 USD | 1,750.00 USD | `-38.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2105` | 819,100.00 USD | 0.00 USD | 579.72 USD | `-36.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2345` | 818,520.00 USD | 0.00 USD | 705.61 USD | `-29.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2405` | 817,810.00 USD | 0.00 USD | 1,200.00 USD | `-27.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2415` | 816,610.00 USD | 0.00 USD | 127.51 USD | `-27.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2505` | 816,480.00 USD | 0.00 USD | 1,850.00 USD | `-24.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2565` | 814,630.00 USD | 0.00 USD | 1,920.00 USD | `-22.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2605` | 812,700.00 USD | 0.00 USD | 4,200.00 USD | `-21.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2625` | 808,500.00 USD | 0.00 USD | 954.98 USD | `-20.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2675` | 807,550.00 USD | 0.00 USD | 695.50 USD | `-19.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2685` | 806,850.00 USD | 0.00 USD | 1,630.00 USD | `-19.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2815` | 805,220.00 USD | 0.00 USD | 2,550.00 USD | `-15.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2835` | 802,670.00 USD | 0.00 USD | 229.92 USD | `-14.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2935` | 802,440.00 USD | 0.00 USD | 15,940.00 USD | `-11.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2965` | 786,500.00 USD | 0.00 USD | 111.19 USD | `-10.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2975` | 786,390.00 USD | 0.00 USD | 178.80 USD | `-10.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2985` | 786,210.00 USD | 0.00 USD | 685.95 USD | `-10.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3005` | 785,530.00 USD | 0.00 USD | 2,710.00 USD | `-9.48%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3065` | 782,820.00 USD | 0.00 USD | 919.50 USD | `-7.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3075` | 781,900.00 USD | 0.00 USD | 193.11 USD | `-7.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3085` | 781,710.00 USD | 0.00 USD | 16,070.00 USD | `-7.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3095` | 765,640.00 USD | 0.00 USD | 147.32 USD | `-6.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3105` | 765,490.00 USD | 0.00 USD | 25,820.00 USD | `-6.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3115` | 739,680.00 USD | 0.00 USD | 6,530.00 USD | `-6.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3125` | 733,150.00 USD | 0.00 USD | 524,570.00 USD | `-5.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3135` | 208,580.00 USD | 0.00 USD | 1,270.00 USD | `-5.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3145` | 207,310.00 USD | 0.00 USD | 25,790.00 USD | `-5.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3155` | 181,520.00 USD | 0.00 USD | 9,290.00 USD | `-4.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3165` | 172,230.00 USD | 0.00 USD | 6,100.00 USD | `-4.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3185` | 166,140.00 USD | 0.00 USD | 2,010.00 USD | `-4.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3195` | 164,120.00 USD | 0.00 USD | 15,160.00 USD | `-3.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3205` | 148,960.00 USD | 0.00 USD | 21,790.00 USD | `-3.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3215` | 127,170.00 USD | 0.00 USD | 55,600.00 USD | `-3.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3225` | 71,570.00 USD | 0.00 USD | 174.47 USD | `-2.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3235` | 71,400.00 USD | 0.00 USD | 845.95 USD | `-2.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3245` | 70,550.00 USD | 0.00 USD | 14,470.00 USD | `-2.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3255` | 56,080.00 USD | 0.00 USD | 8,410.00 USD | `-1.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3265` | 47,660.00 USD | 0.00 USD | 25,740.00 USD | `-1.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3275` | 21,930.00 USD | 0.00 USD | 13,320.00 USD | `-1.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3285` | 8,600.00 USD | 0.00 USD | 4,580.00 USD | `-1.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3295` | 4,020.00 USD | 0.00 USD | 1,830.00 USD | `-0.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3305` | 2,190.00 USD | 0.00 USD | 1,690.00 USD | `-0.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.3315` | 496.92 USD | 0.00 USD | 496.92 USD | `-0.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3325` | 40,600.00 USD | 40,600.00 USD | 0.00 USD | `+0.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3335` | 42,080.00 USD | 1,480.00 USD | 0.00 USD | `+0.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3345` | 43,300.00 USD | 1,220.00 USD | 0.00 USD | `+0.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3355` | 218,160.00 USD | 174,860.00 USD | 0.00 USD | `+1.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3365` | 218,540.00 USD | 379.57 USD | 0.00 USD | `+1.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3375` | 219,250.00 USD | 711.11 USD | 0.00 USD | `+1.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3385` | 230,900.00 USD | 11,640.00 USD | 0.00 USD | `+1.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3395` | 231,000.00 USD | 102.87 USD | 0.00 USD | `+2.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3405` | 234,090.00 USD | 3,090.00 USD | 0.00 USD | `+2.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3415` | 234,990.00 USD | 904.63 USD | 0.00 USD | `+2.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3425` | 240,520.00 USD | 5,520.00 USD | 0.00 USD | `+3.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3435` | 248,130.00 USD | 7,610.00 USD | 0.00 USD | `+3.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3445` | 248,840.00 USD | 709.67 USD | 0.00 USD | `+3.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3455` | 251,720.00 USD | 2,880.00 USD | 0.00 USD | `+4.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3465` | 259,650.00 USD | 7,930.00 USD | 0.00 USD | `+4.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3475` | 262,800.00 USD | 3,150.00 USD | 0.00 USD | `+4.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3485` | 263,860.00 USD | 1,060.00 USD | 0.00 USD | `+4.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3495` | 289,610.00 USD | 25,750.00 USD | 0.00 USD | `+5.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3505` | 308,190.00 USD | 18,580.00 USD | 0.00 USD | `+5.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3535` | 321,610.00 USD | 13,420.00 USD | 0.00 USD | `+6.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3545` | 322,380.00 USD | 769.97 USD | 0.00 USD | `+6.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3555` | 322,610.00 USD | 226.10 USD | 0.00 USD | `+7.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3575` | 326,790.00 USD | 4,180.00 USD | 0.00 USD | `+7.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3585` | 332,780.00 USD | 5,990.00 USD | 0.00 USD | `+7.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3595` | 338,960.00 USD | 6,180.00 USD | 0.00 USD | `+8.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3605` | 339,440.00 USD | 485.59 USD | 0.00 USD | `+8.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3615` | 339,570.00 USD | 129.42 USD | 0.00 USD | `+8.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3635` | 339,960.00 USD | 390.40 USD | 0.00 USD | `+9.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3645` | 340,100.00 USD | 131.95 USD | 0.00 USD | `+9.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3655` | 340,530.00 USD | 433.85 USD | 0.00 USD | `+10.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3665` | 340,990.00 USD | 463.99 USD | 0.00 USD | `+10.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3695` | 341,150.00 USD | 159.62 USD | 0.00 USD | `+11.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3705` | 342,080.00 USD | 926.99 USD | 0.00 USD | `+11.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3755` | 344,820.00 USD | 2,740.00 USD | 0.00 USD | `+13.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3785` | 345,100.00 USD | 275.17 USD | 0.00 USD | `+14.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3795` | 345,560.00 USD | 463.37 USD | 0.00 USD | `+14.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3805` | 345,900.00 USD | 337.12 USD | 0.00 USD | `+14.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3815` | 346,010.00 USD | 114.83 USD | 0.00 USD | `+14.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3835` | 346,240.00 USD | 224.73 USD | 0.00 USD | `+15.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3855` | 346,750.00 USD | 514.64 USD | 0.00 USD | `+16.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3895` | 347,100.00 USD | 352.11 USD | 0.00 USD | `+17.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3965` | 349,510.00 USD | 2,400.00 USD | 0.00 USD | `+19.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3975` | 350,080.00 USD | 572.00 USD | 0.00 USD | `+19.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3985` | 351,280.00 USD | 1,200.00 USD | 0.00 USD | `+20.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3995` | 404,150.00 USD | 52,880.00 USD | 0.00 USD | `+20.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4015` | 406,550.00 USD | 2,400.00 USD | 0.00 USD | `+20.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4035` | 407,750.00 USD | 1,200.00 USD | 0.00 USD | `+21.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4055` | 408,950.00 USD | 1,200.00 USD | 0.00 USD | `+22.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4065` | 410,150.00 USD | 1,200.00 USD | 0.00 USD | `+22.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4205` | 410,340.00 USD | 186.70 USD | 0.00 USD | `+26.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4405` | 448,920.00 USD | 38,580.00 USD | 0.00 USD | `+32.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4445` | 449,090.00 USD | 170.69 USD | 0.00 USD | `+33.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.4495` | 450,480.00 USD | 1,390.00 USD | 0.00 USD | `+35.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.5005` | 461,630.00 USD | 11,150.00 USD | 0.00 USD | `+50.77%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `1D` | `0.2979` | 2,840,000.00 USD | 0.00 USD | 2,840,000.00 USD | 20,670.00 USD | 5,710.00 USD | 5,870.00 USD |
| `7D` | `0.2979` | 12,950,000.00 USD | 0.00 USD | 12,950,000.00 USD | 65,800.00 USD | 8,600.00 USD | 10,570.00 USD |
| `1D` | `0.2983` | 2,810,000.00 USD | 0.00 USD | 2,810,000.00 USD | 63,060.00 USD | 10,010.00 USD | 16,430.00 USD |
| `7D` | `0.2983` | 12,870,000.00 USD | 0.00 USD | 12,870,000.00 USD | 99,280.00 USD | 9,990.00 USD | 27,500.00 USD |
| `1D` | `0.2987` | 2,720,000.00 USD | 0.00 USD | 2,720,000.00 USD | 41,780.00 USD | 4,930.00 USD | 5,150.00 USD |
| `7D` | `0.2987` | 12,730,000.00 USD | 0.00 USD | 12,730,000.00 USD | 76,610.00 USD | 9,860.00 USD | 6,170.00 USD |
| `7D` | `0.2991` | 12,640,000.00 USD | 0.00 USD | 12,640,000.00 USD | 23,720.00 USD | 6,910.00 USD | 3,870.00 USD |
| `7D` | `0.3051` | 12,600,000.00 USD | 0.00 USD | 12,600,000.00 USD | 380.73 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3055` | 12,600,000.00 USD | 0.00 USD | 12,600,000.00 USD | 1,380.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3059` | 12,600,000.00 USD | 0.00 USD | 12,600,000.00 USD | 212.37 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3063` | 12,600,000.00 USD | 0.00 USD | 12,600,000.00 USD | 1,990.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3067` | 2,670,000.00 USD | 0.00 USD | 2,670,000.00 USD | 57.95 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3067` | 12,600,000.00 USD | 0.00 USD | 12,600,000.00 USD | 5,660.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3071` | 2,670,000.00 USD | 0.00 USD | 2,670,000.00 USD | 3,270.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3071` | 12,590,000.00 USD | 0.00 USD | 12,590,000.00 USD | 6,280.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3075` | 2,660,000.00 USD | 0.00 USD | 2,660,000.00 USD | 1,530.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3075` | 12,590,000.00 USD | 0.00 USD | 12,590,000.00 USD | 2,850.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3079` | 2,660,000.00 USD | 0.00 USD | 2,660,000.00 USD | 257.87 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3079` | 12,580,000.00 USD | 0.00 USD | 12,580,000.00 USD | 2,180.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3083` | 2,660,000.00 USD | 0.00 USD | 2,660,000.00 USD | 51.12 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3083` | 12,580,000.00 USD | 0.00 USD | 12,580,000.00 USD | 1,200.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3087` | 2,660,000.00 USD | 0.00 USD | 2,660,000.00 USD | 366.88 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3087` | 12,580,000.00 USD | 0.00 USD | 12,580,000.00 USD | 1,860.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3091` | 2,660,000.00 USD | 0.00 USD | 2,660,000.00 USD | 29.99 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3091` | 12,580,000.00 USD | 0.00 USD | 12,580,000.00 USD | 1,320.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3107` | 12,580,000.00 USD | 0.00 USD | 12,580,000.00 USD | 1,790.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3111` | 12,580,000.00 USD | 0.00 USD | 12,580,000.00 USD | 554.30 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3115` | 12,580,000.00 USD | 0.00 USD | 12,580,000.00 USD | 283.30 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3119` | 12,570,000.00 USD | 0.00 USD | 12,570,000.00 USD | 2,650.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3123` | 2,660,000.00 USD | 0.00 USD | 2,660,000.00 USD | 77.30 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3123` | 12,570,000.00 USD | 0.00 USD | 12,570,000.00 USD | 7,550.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3127` | 2,660,000.00 USD | 0.00 USD | 2,660,000.00 USD | 4,360.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3127` | 12,560,000.00 USD | 0.00 USD | 12,560,000.00 USD | 8,380.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3131` | 2,660,000.00 USD | 0.00 USD | 2,660,000.00 USD | 2,040.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3131` | 12,560,000.00 USD | 0.00 USD | 12,560,000.00 USD | 3,800.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3135` | 2,660,000.00 USD | 0.00 USD | 2,660,000.00 USD | 344.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3135` | 12,550,000.00 USD | 0.00 USD | 12,550,000.00 USD | 2,910.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3139` | 2,660,000.00 USD | 0.00 USD | 2,660,000.00 USD | 68.20 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3139` | 12,550,000.00 USD | 0.00 USD | 12,550,000.00 USD | 1,600.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3143` | 2,660,000.00 USD | 0.00 USD | 2,660,000.00 USD | 405.20 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3143` | 12,550,000.00 USD | 0.00 USD | 12,550,000.00 USD | 183,810.00 USD | 34,890.00 USD | 11,170.00 USD |
| `1D` | `0.3147` | 2,660,000.00 USD | 0.00 USD | 2,660,000.00 USD | 124.20 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3147` | 12,320,000.00 USD | 0.00 USD | 12,320,000.00 USD | 170,840.00 USD | 16,380.00 USD | 21,590.00 USD |
| `7D` | `0.3151` | 12,110,000.00 USD | 0.00 USD | 12,110,000.00 USD | 187,500.00 USD | 29,590.00 USD | 61,120.00 USD |
| `7D` | `0.3155` | 11,830,000.00 USD | 0.00 USD | 11,830,000.00 USD | 157,220.00 USD | 40,480.00 USD | 22,590.00 USD |
| `1D` | `0.3159` | 2,660,000.00 USD | 0.00 USD | 2,660,000.00 USD | 5,750.00 USD | 5,600.00 USD | 27,350.00 USD |
| `7D` | `0.3159` | 11,610,000.00 USD | 0.00 USD | 11,610,000.00 USD | 353,770.00 USD | 101,710.00 USD | 112,500.00 USD |
| `1D` | `0.3163` | 2,620,000.00 USD | 0.00 USD | 2,620,000.00 USD | 98,530.00 USD | 38,520.00 USD | 39,720.00 USD |
| `7D` | `0.3163` | 11,040,000.00 USD | 0.00 USD | 11,040,000.00 USD | 225,120.00 USD | 116,130.00 USD | 134,250.00 USD |
| `1D` | `0.3167` | 2,440,000.00 USD | 0.00 USD | 2,440,000.00 USD | 55,360.00 USD | 14,920.00 USD | 20,330.00 USD |
| `7D` | `0.3167` | 10,570,000.00 USD | 0.00 USD | 10,570,000.00 USD | 328,930.00 USD | 75,090.00 USD | 95,630.00 USD |
| `1D` | `0.3171` | 2,350,000.00 USD | 0.00 USD | 2,350,000.00 USD | 13,570.00 USD | 15,290.00 USD | 11,160.00 USD |
| `7D` | `0.3171` | 10,070,000.00 USD | 0.00 USD | 10,070,000.00 USD | 293,450.00 USD | 89,970.00 USD | 96,960.00 USD |
| `1D` | `0.3175` | 2,310,000.00 USD | 0.00 USD | 2,310,000.00 USD | 22,660.00 USD | 6,170.00 USD | 5,090.00 USD |
| `7D` | `0.3175` | 9,590,000.00 USD | 0.00 USD | 9,590,000.00 USD | 28,570.00 USD | 12,370.00 USD | 39,210.00 USD |
| `1D` | `0.3179` | 2,280,000.00 USD | 0.00 USD | 2,280,000.00 USD | 40,570.00 USD | 14,030.00 USD | 16,730.00 USD |
| `7D` | `0.3179` | 9,510,000.00 USD | 0.00 USD | 9,510,000.00 USD | 231,050.00 USD | 33,640.00 USD | 39,970.00 USD |
| `1D` | `0.3183` | 2,200,000.00 USD | 0.00 USD | 2,200,000.00 USD | 303,640.00 USD | 44,010.00 USD | 52,060.00 USD |
| `7D` | `0.3183` | 9,200,000.00 USD | 0.00 USD | 9,200,000.00 USD | 477,670.00 USD | 49,030.00 USD | 70,140.00 USD |
| `1D` | `0.3187` | 1,800,000.00 USD | 0.00 USD | 1,800,000.00 USD | 26,290.00 USD | 4,010.00 USD | 3,700.00 USD |
| `7D` | `0.3187` | 8,610,000.00 USD | 0.00 USD | 8,610,000.00 USD | 117,850.00 USD | 29,330.00 USD | 11,120.00 USD |
| `7D` | `0.3191` | 8,450,000.00 USD | 0.00 USD | 8,450,000.00 USD | 59,160.00 USD | 13,950.00 USD | 11,780.00 USD |
| `7D` | `0.3207` | 8,360,000.00 USD | 0.00 USD | 8,360,000.00 USD | 158,770.00 USD | 34,380.00 USD | 7,770.00 USD |
| `7D` | `0.3211` | 8,160,000.00 USD | 0.00 USD | 8,160,000.00 USD | 403,080.00 USD | 68,150.00 USD | 57,740.00 USD |
| `7D` | `0.3215` | 7,630,000.00 USD | 0.00 USD | 7,630,000.00 USD | 413,850.00 USD | 47,610.00 USD | 100,600.00 USD |
| `7D` | `0.3219` | 7,070,000.00 USD | 0.00 USD | 7,070,000.00 USD | 324,100.00 USD | 67,660.00 USD | 63,030.00 USD |
| `1D` | `0.3223` | 1,770,000.00 USD | 0.00 USD | 1,770,000.00 USD | 0.00 USD | 0.00 USD | 20,260.00 USD |
| `7D` | `0.3223` | 6,620,000.00 USD | 0.00 USD | 6,620,000.00 USD | 435,620.00 USD | 137,210.00 USD | 89,860.00 USD |
| `1D` | `0.3227` | 1,750,000.00 USD | 0.00 USD | 1,750,000.00 USD | 101,660.00 USD | 54,790.00 USD | 59,400.00 USD |
| `7D` | `0.3227` | 5,950,000.00 USD | 0.00 USD | 5,950,000.00 USD | 638,380.00 USD | 208,030.00 USD | 227,150.00 USD |
| `1D` | `0.3231` | 1,530,000.00 USD | 0.00 USD | 1,530,000.00 USD | 161,500.00 USD | 51,400.00 USD | 82,170.00 USD |
| `7D` | `0.3231` | 4,880,000.00 USD | 0.00 USD | 4,880,000.00 USD | 589,500.00 USD | 180,670.00 USD | 295,130.00 USD |
| `1D` | `0.3235` | 1,240,000.00 USD | 0.00 USD | 1,240,000.00 USD | 63,830.00 USD | 35,740.00 USD | 35,300.00 USD |
| `7D` | `0.3235` | 3,810,000.00 USD | 0.00 USD | 3,810,000.00 USD | 507,910.00 USD | 168,260.00 USD | 205,040.00 USD |
| `1D` | `0.3239` | 1,100,000.00 USD | 0.00 USD | 1,100,000.00 USD | 26,750.00 USD | 10,730.00 USD | 7,320.00 USD |
| `7D` | `0.3239` | 2,930,000.00 USD | 0.00 USD | 2,930,000.00 USD | 354,650.00 USD | 119,100.00 USD | 114,090.00 USD |
| `1D` | `0.3243` | 1,060,000.00 USD | 0.00 USD | 1,060,000.00 USD | 93,280.00 USD | 21,990.00 USD | 19,290.00 USD |
| `7D` | `0.3243` | 2,350,000.00 USD | 0.00 USD | 2,350,000.00 USD | 265,190.00 USD | 39,180.00 USD | 42,580.00 USD |
| `1D` | `0.3247` | 924,730.00 USD | 0.00 USD | 924,730.00 USD | 183,070.00 USD | 49,560.00 USD | 63,280.00 USD |
| `7D` | `0.3247` | 2,000,000.00 USD | 0.00 USD | 2,000,000.00 USD | 559,960.00 USD | 72,190.00 USD | 145,960.00 USD |
| `1D` | `0.3251` | 628,820.00 USD | 0.00 USD | 628,820.00 USD | 477,390.00 USD | 60,890.00 USD | 57,870.00 USD |
| `7D` | `0.3251` | 1,220,000.00 USD | 0.00 USD | 1,220,000.00 USD | 667,020.00 USD | 65,250.00 USD | 61,340.00 USD |
| `1D` | `0.3255` | 32,670.00 USD | 0.00 USD | 32,670.00 USD | 25,270.00 USD | 0.00 USD | 7,400.00 USD |
| `7D` | `0.3255` | 426,520.00 USD | 0.00 USD | 426,520.00 USD | 251,380.00 USD | 60,580.00 USD | 35,520.00 USD |
| `7D` | `0.3259` | 79,040.00 USD | 0.00 USD | 79,040.00 USD | 51,940.00 USD | 16,810.00 USD | 10,280.00 USD |
| `1D` | `0.3314` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3314` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3339` | 455,400.00 USD | 455,400.00 USD | 0.00 USD | 363,280.00 USD | 69,780.00 USD | 22,330.00 USD |
| `7D` | `0.3343` | 729,900.00 USD | 729,900.00 USD | 0.00 USD | 198,570.00 USD | 32,750.00 USD | 43,180.00 USD |
| `7D` | `0.3347` | 1,290,000.00 USD | 1,290,000.00 USD | 0.00 USD | 413,850.00 USD | 47,610.00 USD | 100,600.00 USD |
| `7D` | `0.3351` | 1,750,000.00 USD | 1,750,000.00 USD | 0.00 USD | 324,100.00 USD | 67,660.00 USD | 63,030.00 USD |
| `1D` | `0.3355` | 20,260.00 USD | 20,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 20,260.00 USD |
| `7D` | `0.3355` | 2,410,000.00 USD | 2,410,000.00 USD | 0.00 USD | 435,620.00 USD | 137,210.00 USD | 89,860.00 USD |
| `1D` | `0.3359` | 236,110.00 USD | 236,110.00 USD | 0.00 USD | 101,660.00 USD | 54,790.00 USD | 59,400.00 USD |
| `7D` | `0.3359` | 3,480,000.00 USD | 3,480,000.00 USD | 0.00 USD | 638,380.00 USD | 208,030.00 USD | 227,150.00 USD |
| `1D` | `0.3363` | 531,180.00 USD | 531,180.00 USD | 0.00 USD | 161,500.00 USD | 51,400.00 USD | 82,170.00 USD |
| `7D` | `0.3363` | 4,550,000.00 USD | 4,550,000.00 USD | 0.00 USD | 589,500.00 USD | 180,670.00 USD | 295,130.00 USD |
| `1D` | `0.3367` | 666,050.00 USD | 666,050.00 USD | 0.00 USD | 63,830.00 USD | 35,740.00 USD | 35,300.00 USD |
| `7D` | `0.3367` | 5,430,000.00 USD | 5,430,000.00 USD | 0.00 USD | 507,910.00 USD | 168,260.00 USD | 205,040.00 USD |
| `1D` | `0.3371` | 710,860.00 USD | 710,860.00 USD | 0.00 USD | 26,750.00 USD | 10,730.00 USD | 7,320.00 USD |
| `7D` | `0.3371` | 6,020,000.00 USD | 6,020,000.00 USD | 0.00 USD | 354,650.00 USD | 119,100.00 USD | 114,090.00 USD |
| `1D` | `0.3375` | 845,420.00 USD | 845,420.00 USD | 0.00 USD | 93,280.00 USD | 21,990.00 USD | 19,290.00 USD |
| `7D` | `0.3375` | 6,360,000.00 USD | 6,360,000.00 USD | 0.00 USD | 265,190.00 USD | 39,180.00 USD | 42,580.00 USD |
| `1D` | `0.3379` | 1,140,000.00 USD | 1,140,000.00 USD | 0.00 USD | 183,070.00 USD | 49,560.00 USD | 63,280.00 USD |
| `7D` | `0.3379` | 7,140,000.00 USD | 7,140,000.00 USD | 0.00 USD | 559,960.00 USD | 72,190.00 USD | 145,960.00 USD |
| `1D` | `0.3383` | 1,740,000.00 USD | 1,740,000.00 USD | 0.00 USD | 477,390.00 USD | 60,890.00 USD | 57,870.00 USD |
| `7D` | `0.3383` | 7,940,000.00 USD | 7,940,000.00 USD | 0.00 USD | 667,020.00 USD | 65,250.00 USD | 61,340.00 USD |
| `1D` | `0.3387` | 1,770,000.00 USD | 1,770,000.00 USD | 0.00 USD | 25,270.00 USD | 0.00 USD | 7,400.00 USD |
| `7D` | `0.3387` | 8,280,000.00 USD | 8,280,000.00 USD | 0.00 USD | 251,380.00 USD | 60,580.00 USD | 35,520.00 USD |
| `7D` | `0.3391` | 8,360,000.00 USD | 8,360,000.00 USD | 0.00 USD | 51,940.00 USD | 16,810.00 USD | 10,280.00 USD |
| `7D` | `0.3403` | 8,460,000.00 USD | 8,460,000.00 USD | 0.00 USD | 79,380.00 USD | 17,190.00 USD | 3,890.00 USD |
| `7D` | `0.3407` | 8,670,000.00 USD | 8,670,000.00 USD | 0.00 USD | 162,870.00 USD | 34,080.00 USD | 13,980.00 USD |
| `7D` | `0.3411` | 8,990,000.00 USD | 8,990,000.00 USD | 0.00 USD | 236,810.00 USD | 19,270.00 USD | 60,150.00 USD |
| `7D` | `0.3415` | 9,120,000.00 USD | 9,120,000.00 USD | 0.00 USD | 75,860.00 USD | 24,680.00 USD | 30,770.00 USD |
| `7D` | `0.3419` | 9,350,000.00 USD | 9,350,000.00 USD | 0.00 USD | 162,450.00 USD | 45,810.00 USD | 19,490.00 USD |
| `1D` | `0.3423` | 1,810,000.00 USD | 1,810,000.00 USD | 0.00 USD | 5,750.00 USD | 5,600.00 USD | 27,350.00 USD |
| `7D` | `0.3423` | 9,860,000.00 USD | 9,860,000.00 USD | 0.00 USD | 331,520.00 USD | 82,020.00 USD | 100,690.00 USD |
| `1D` | `0.3427` | 1,990,000.00 USD | 1,990,000.00 USD | 0.00 USD | 98,530.00 USD | 38,520.00 USD | 39,720.00 USD |
| `7D` | `0.3427` | 10,340,000.00 USD | 10,340,000.00 USD | 0.00 USD | 225,120.00 USD | 116,130.00 USD | 134,250.00 USD |
| `1D` | `0.3431` | 2,080,000.00 USD | 2,080,000.00 USD | 0.00 USD | 55,360.00 USD | 14,920.00 USD | 20,330.00 USD |
| `7D` | `0.3431` | 10,840,000.00 USD | 10,840,000.00 USD | 0.00 USD | 328,930.00 USD | 75,090.00 USD | 95,630.00 USD |
| `1D` | `0.3435` | 2,120,000.00 USD | 2,120,000.00 USD | 0.00 USD | 13,570.00 USD | 15,290.00 USD | 11,160.00 USD |
| `7D` | `0.3435` | 11,320,000.00 USD | 11,320,000.00 USD | 0.00 USD | 295,240.00 USD | 89,970.00 USD | 96,960.00 USD |
| `1D` | `0.3439` | 2,150,000.00 USD | 2,150,000.00 USD | 0.00 USD | 22,660.00 USD | 6,170.00 USD | 5,090.00 USD |
| `7D` | `0.3439` | 11,400,000.00 USD | 11,400,000.00 USD | 0.00 USD | 29,120.00 USD | 12,370.00 USD | 39,210.00 USD |
| `1D` | `0.3443` | 2,220,000.00 USD | 2,220,000.00 USD | 0.00 USD | 40,570.00 USD | 14,030.00 USD | 16,730.00 USD |
| `7D` | `0.3443` | 11,710,000.00 USD | 11,710,000.00 USD | 0.00 USD | 231,330.00 USD | 33,640.00 USD | 39,970.00 USD |
| `1D` | `0.3447` | 2,480,000.00 USD | 2,480,000.00 USD | 0.00 USD | 186,490.00 USD | 33,000.00 USD | 41,460.00 USD |
| `7D` | `0.3447` | 12,110,000.00 USD | 12,110,000.00 USD | 0.00 USD | 310,260.00 USD | 31,970.00 USD | 56,490.00 USD |
| `1D` | `0.3451` | 2,660,000.00 USD | 2,660,000.00 USD | 0.00 USD | 143,520.00 USD | 15,020.00 USD | 14,300.00 USD |
| `7D` | `0.3451` | 12,400,000.00 USD | 12,400,000.00 USD | 0.00 USD | 245,650.00 USD | 26,900.00 USD | 20,240.00 USD |
| `1D` | `0.3455` | 2,660,000.00 USD | 2,660,000.00 USD | 0.00 USD | 1,710.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3455` | 12,550,000.00 USD | 12,550,000.00 USD | 0.00 USD | 97,690.00 USD | 33,430.00 USD | 16,310.00 USD |
| `1D` | `0.3459` | 2,660,000.00 USD | 2,660,000.00 USD | 0.00 USD | 4,260.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3459` | 12,570,000.00 USD | 12,570,000.00 USD | 0.00 USD | 22,340.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3463` | 2,660,000.00 USD | 2,660,000.00 USD | 0.00 USD | 560.10 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3463` | 12,570,000.00 USD | 12,570,000.00 USD | 0.00 USD | 3,330.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3467` | 2,660,000.00 USD | 2,660,000.00 USD | 0.00 USD | 220.50 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3467` | 12,570,000.00 USD | 12,570,000.00 USD | 0.00 USD | 1,130.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3471` | 2,660,000.00 USD | 2,660,000.00 USD | 0.00 USD | 68.20 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3471` | 12,570,000.00 USD | 12,570,000.00 USD | 0.00 USD | 1,500.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3475` | 2,660,000.00 USD | 2,660,000.00 USD | 0.00 USD | 489.40 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3475` | 12,580,000.00 USD | 12,580,000.00 USD | 0.00 USD | 2,180.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3479` | 2,660,000.00 USD | 2,660,000.00 USD | 0.00 USD | 40.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3479` | 12,580,000.00 USD | 12,580,000.00 USD | 0.00 USD | 1,770.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3491` | 12,580,000.00 USD | 12,580,000.00 USD | 0.00 USD | 1,340.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3495` | 12,580,000.00 USD | 12,580,000.00 USD | 0.00 USD | 415.52 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3499` | 12,580,000.00 USD | 12,580,000.00 USD | 0.00 USD | 212.37 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3503` | 12,580,000.00 USD | 12,580,000.00 USD | 0.00 USD | 1,990.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3507` | 2,660,000.00 USD | 2,660,000.00 USD | 0.00 USD | 57.95 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3507` | 12,590,000.00 USD | 12,590,000.00 USD | 0.00 USD | 5,660.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3511` | 2,660,000.00 USD | 2,660,000.00 USD | 0.00 USD | 2,170.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3511` | 12,590,000.00 USD | 12,590,000.00 USD | 0.00 USD | 4,590.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3515` | 2,670,000.00 USD | 2,670,000.00 USD | 0.00 USD | 2,300.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3515` | 12,600,000.00 USD | 12,600,000.00 USD | 0.00 USD | 3,690.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3519` | 2,670,000.00 USD | 2,670,000.00 USD | 0.00 USD | 419.87 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3519` | 12,600,000.00 USD | 12,600,000.00 USD | 0.00 USD | 2,490.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3523` | 2,670,000.00 USD | 2,670,000.00 USD | 0.00 USD | 165.29 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3523` | 12,600,000.00 USD | 12,600,000.00 USD | 0.00 USD | 846.39 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3527` | 2,670,000.00 USD | 2,670,000.00 USD | 0.00 USD | 51.12 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3527` | 12,600,000.00 USD | 12,600,000.00 USD | 0.00 USD | 1,120.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3531` | 2,670,000.00 USD | 2,670,000.00 USD | 0.00 USD | 366.88 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3531` | 12,600,000.00 USD | 12,600,000.00 USD | 0.00 USD | 1,640.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.3535` | 2,670,000.00 USD | 2,670,000.00 USD | 0.00 USD | 29.99 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3535` | 12,600,000.00 USD | 12,600,000.00 USD | 0.00 USD | 1,320.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3599` | 12,630,000.00 USD | 12,630,000.00 USD | 0.00 USD | 18,580.00 USD | 6,010.00 USD | 0.00 USD |
| `7D` | `0.3603` | 12,690,000.00 USD | 12,690,000.00 USD | 0.00 USD | 48,320.00 USD | 6,290.00 USD | 2,910.00 USD |
| `7D` | `0.3607` | 12,750,000.00 USD | 12,750,000.00 USD | 0.00 USD | 52,620.00 USD | 4,710.00 USD | 6,550.00 USD |
| `7D` | `0.3611` | 12,800,000.00 USD | 12,800,000.00 USD | 0.00 USD | 35,490.00 USD | 4,040.00 USD | 14,500.00 USD |
| `7D` | `0.3615` | 12,880,000.00 USD | 12,880,000.00 USD | 0.00 USD | 61,190.00 USD | 9,240.00 USD | 1,960.00 USD |
| `1D` | `0.3619` | 2,680,000.00 USD | 2,680,000.00 USD | 0.00 USD | 662.47 USD | 654.45 USD | 5,890.00 USD |
| `7D` | `0.3619` | 13,010,000.00 USD | 13,010,000.00 USD | 0.00 USD | 82,550.00 USD | 20,630.00 USD | 33,010.00 USD |
| `1D` | `0.3623` | 2,720,000.00 USD | 2,720,000.00 USD | 0.00 USD | 24,780.00 USD | 10,080.00 USD | 10,400.00 USD |
| `7D` | `0.3623` | 13,170,000.00 USD | 13,170,000.00 USD | 0.00 USD | 89,280.00 USD | 33,600.00 USD | 36,370.00 USD |
| `1D` | `0.3627` | 2,750,000.00 USD | 2,750,000.00 USD | 0.00 USD | 15,190.00 USD | 5,590.00 USD | 10,470.00 USD |
| `7D` | `0.3627` | 13,300,000.00 USD | 13,300,000.00 USD | 0.00 USD | 77,830.00 USD | 18,040.00 USD | 36,410.00 USD |
| `1D` | `0.3631` | 2,770,000.00 USD | 2,770,000.00 USD | 0.00 USD | 7,230.00 USD | 5,410.00 USD | 5,930.00 USD |
| `7D` | `0.3631` | 13,430,000.00 USD | 13,430,000.00 USD | 0.00 USD | 76,220.00 USD | 25,590.00 USD | 26,610.00 USD |
| `1D` | `0.3635` | 2,770,000.00 USD | 2,770,000.00 USD | 0.00 USD | 34.10 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.3635` | 13,500,000.00 USD | 13,500,000.00 USD | 0.00 USD | 44,080.00 USD | 16,220.00 USD | 6,560.00 USD |
| `1D` | `0.3639` | 2,790,000.00 USD | 2,790,000.00 USD | 0.00 USD | 11,660.00 USD | 2,950.00 USD | 3,160.00 USD |
| `7D` | `0.3639` | 13,540,000.00 USD | 13,540,000.00 USD | 0.00 USD | 24,540.00 USD | 2,960.00 USD | 9,300.00 USD |
| `1D` | `0.3643` | 2,820,000.00 USD | 2,820,000.00 USD | 0.00 USD | 17,200.00 USD | 4,420.00 USD | 7,540.00 USD |
| `7D` | `0.3643` | 13,650,000.00 USD | 13,650,000.00 USD | 0.00 USD | 89,610.00 USD | 8,430.00 USD | 14,840.00 USD |
| `1D` | `0.3647` | 2,930,000.00 USD | 2,930,000.00 USD | 0.00 USD | 83,310.00 USD | 10,780.00 USD | 14,000.00 USD |
| `7D` | `0.3647` | 13,740,000.00 USD | 13,740,000.00 USD | 0.00 USD | 66,060.00 USD | 11,120.00 USD | 17,470.00 USD |
| `1D` | `0.3651` | 2,940,000.00 USD | 2,940,000.00 USD | 0.00 USD | 13,310.00 USD | 2,510.00 USD | 2,740.00 USD |
| `7D` | `0.3651` | 13,810,000.00 USD | 13,810,000.00 USD | 0.00 USD | 60,980.00 USD | 4,810.00 USD | 2,640.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `299.84M` | Total OI Tokens: `904,904,332.4 TRX`
  * 1h OI Change: `+4.51%` | 4h OI Change: `+4.79%` | 24h OI Change: `+0.66%`
  * Exchange Breakdown: Binance=`90.29M` | Bybit=`49.83M` | OKX=`13.89M` | Hyperliquid=`11.42M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `12.75K` | Last 24h: `8.30K` | Last 3d: `-75.25K` | Last 7d: `-283.91K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0100%` | **USDT OKX** | `0.0100%` |
| **USDT Bybit** | `0.0059%` | **USDT KuCoin** | `0.0100%` |
| **USDT MEXC** | `0.0100%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `0.0099%` | **USDT Bitget** | `0.0100%` |
| **CoinM Binance** | `0.0100%` | **CoinM OKX** | `-` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `TRX` | `48.95%` | `51.05%` | `0.96` | 10,740,000.00 USD |
| `15M` | `Binance` | `44.61%` | `55.39%` | `0.81` | 3,420,000.00 USD |
| `15M` | `OKX` | `48.75%` | `51.25%` | `0.95` | 2,180,000.00 USD |
| `15M` | `Bybit` | `42.42%` | `57.58%` | `0.74` | 501,030.00 USD |
| `15M` | `KuCoin` | `68.85%` | `31.15%` | `2.21` | 44,430.00 USD |
| `15M` | `Gate` | `50.07%` | `49.93%` | `1.00` | 2,130,000.00 USD |
| `15M` | `Bitget` | `61.13%` | `38.87%` | `1.57` | 213,250.00 USD |
| `15M` | `BingX` | `45.66%` | `54.34%` | `0.84` | 270,690.00 USD |
| `15M` | `MEXC` | `58.18%` | `41.82%` | `1.39` | 638,350.00 USD |
| `15M` | `Bitunix` | `66.14%` | `33.86%` | `1.95` | 541,200.00 USD |
| `15M` | `Hyperliquid` | `57.3%` | `42.7%` | `1.34` | 14,740.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `44.93%` | `55.07%` | `0.82` | 73,710.00 USD |
| `15M` | `Crypto.com` | `34.03%` | `65.97%` | `0.52` | 3,340.00 USD |
| `15M` | `WhiteBIT` | `65.09%` | `34.91%` | `1.86` | 415,730.00 USD |
| `15M` | `HTX` | `58.92%` | `41.08%` | `1.43` | 12,340.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `55.76%` | `44.24%` | `1.26` | 72,200.00 USD |
| `15M` | `Aster` | `7.3%` | `92.7%` | `0.08` | 209,720.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `94.07%` | `5.93%` | `15.86` | 192.14 USD |
| `15M` | `Whale Positions` | `44.61%` | `55.39%` | `0.81` | 3,420,000.00 USD |
| `15M` | `Global Accounts` | `48.95%` | `51.05%` | `0.96` | 10,740,000.00 USD |
| `1H` | `TRX` | `50.69%` | `49.31%` | `1.03` | 54,520,000.00 USD |
| `1H` | `Binance` | `52.14%` | `47.86%` | `1.09` | 19,300,000.00 USD |
| `1H` | `OKX` | `45.72%` | `54.28%` | `0.84` | 9,670,000.00 USD |
| `1H` | `Bybit` | `54.72%` | `45.28%` | `1.21` | 2,290,000.00 USD |
| `1H` | `KuCoin` | `22.03%` | `77.97%` | `0.28` | 767,440.00 USD |
| `1H` | `Gate` | `49.99%` | `50.01%` | `1.00` | 9,640,000.00 USD |
| `1H` | `Bitget` | `53.91%` | `46.09%` | `1.17` | 1,870,000.00 USD |
| `1H` | `BingX` | `44.61%` | `55.39%` | `0.81` | 727,270.00 USD |
| `1H` | `MEXC` | `48.84%` | `51.16%` | `0.95` | 4,480,000.00 USD |
| `1H` | `Bitunix` | `57.48%` | `42.52%` | `1.35` | 2,040,000.00 USD |
| `1H` | `Hyperliquid` | `14.7%` | `85.3%` | `0.17` | 470,900.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `54.49%` | `45.51%` | `1.20` | 335,030.00 USD |
| `1H` | `Crypto.com` | `49.65%` | `50.35%` | `0.99` | 50,680.00 USD |
| `1H` | `WhiteBIT` | `76.88%` | `23.12%` | `3.33` | 1,720,000.00 USD |
| `1H` | `HTX` | `34.86%` | `65.14%` | `0.54` | 266,030.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `46.09%` | `53.91%` | `0.85` | 250,250.00 USD |
| `1H` | `Aster` | `63.72%` | `36.28%` | `1.76` | 664,810.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `68.86%` | `31.14%` | `2.21` | 5,710.00 USD |
| `1H` | `Whale Positions` | `52.14%` | `47.86%` | `1.09` | 19,300,000.00 USD |
| `1H` | `Global Accounts` | `50.69%` | `49.31%` | `1.03` | 54,520,000.00 USD |
| `4H` | `TRX` | `50.53%` | `49.47%` | `1.02` | 176,770,000.00 USD |
| `4H` | `Binance` | `50%` | `50%` | `1.00` | 61,980,000.00 USD |
| `4H` | `OKX` | `46.36%` | `53.64%` | `0.86` | 31,650,000.00 USD |
| `4H` | `Bybit` | `50.02%` | `49.98%` | `1.00` | 10,800,000.00 USD |
| `4H` | `KuCoin` | `47.42%` | `52.58%` | `0.90` | 1,940,000.00 USD |
| `4H` | `Gate` | `49.55%` | `50.45%` | `0.98` | 26,260,000.00 USD |
| `4H` | `Bitget` | `56.25%` | `43.75%` | `1.29` | 3,910,000.00 USD |
| `4H` | `BingX` | `42.5%` | `57.5%` | `0.74` | 3,600,000.00 USD |
| `4H` | `MEXC` | `48.87%` | `51.13%` | `0.96` | 15,450,000.00 USD |
| `4H` | `Bitunix` | `44.08%` | `55.92%` | `0.79` | 7,950,000.00 USD |
| `4H` | `Hyperliquid` | `48.09%` | `51.91%` | `0.93` | 924,220.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `55.09%` | `44.91%` | `1.23` | 1,320,000.00 USD |
| `4H` | `Crypto.com` | `45.36%` | `54.64%` | `0.83` | 214,160.00 USD |
| `4H` | `WhiteBIT` | `84.81%` | `15.19%` | `5.58` | 7,350,000.00 USD |
| `4H` | `HTX` | `43.64%` | `56.36%` | `0.77` | 723,020.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `48%` | `52%` | `0.92` | 696,060.00 USD |
| `4H` | `Aster` | `69.25%` | `30.75%` | `2.25` | 1,980,000.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `69.87%` | `30.13%` | `2.32` | 32,330.00 USD |
| `4H` | `Whale Positions` | `50%` | `50%` | `1.00` | 61,980,000.00 USD |
| `4H` | `Global Accounts` | `50.53%` | `49.47%` | `1.02` | 176,770,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5:00 UTC` | `0.3314` | `0.3315` | `0.3314` | `0.3316` | `0.3314` | 195,283.39 USD | 125,552.10 USD | 69,731.29 USD | 55,820.81 USD | `+28.58%` | `9B / 10S` |
| `0:00 UTC` | `0.3314` | `0.3315` | `0.3314` | `0.3315` | `0.3314` | 209,471.50 USD | 106,422.39 USD | 103,049.11 USD | 3,373.28 USD | `+1.61%` | `4B / 6S` |
| `5:00 UTC` | `0.3314` | `0.3314` | `0.3314` | `0.3315` | `0.3313` | 340,051.51 USD | 230,419.78 USD | 109,631.73 USD | 120,788.06 USD | `+35.52%` | `11B / 4S` |
| `0:00 UTC` | `0.3315` | `0.3314` | `0.3315` | `0.3315` | `0.3313` | 236,795.17 USD | 107,521.19 USD | 129,273.97 USD | -21,752.78 USD | `-9.19%` | `3B / 4S` |
| `5:00 UTC` | `0.3314` | `0.3314` | `0.3314` | `0.3315` | `0.3313` | 246,484.09 USD | 148,545.82 USD | 97,938.27 USD | 50,607.55 USD | `+20.53%` | `8B / 5S` |
| `0:00 UTC` | `0.3315` | `0.3315` | `0.3315` | `0.3316` | `0.3314` | 273,399.41 USD | 157,552.59 USD | 115,846.82 USD | 41,705.77 USD | `+15.25%` | `13B / 8S` |
| `5:00 UTC` | `0.3316` | `0.3316` | `0.3316` | `0.3318` | `0.3314` | 305,106.34 USD | 233,151.76 USD | 71,954.58 USD | 161,197.18 USD | `+52.83%` | `24B / 4S` |
| `0:00 UTC` | `0.3317` | `0.3317` | `0.3317` | `0.3318` | `0.3316` | 314,809.77 USD | 216,736.58 USD | 98,073.19 USD | 118,663.38 USD | `+37.69%` | `10B / 6S` |
| `5:00 UTC` | `0.3317` | `0.3317` | `0.3317` | `0.3318` | `0.3316` | 249,844.27 USD | 125,201.88 USD | 124,642.40 USD | 559.48 USD | `+0.22%` | `6B / 6S` |
| `0:00 UTC` | `0.3317` | `0.3311` | `0.3317` | `0.3318` | `0.3306` | 2,412,422.91 USD | 899,769.26 USD | 1,512,653.64 USD | -612,884.38 USD | `-25.41%` | `12B / 29S` |

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
| `5m` | 304,870.00 USD | -757,870.00 USD | **`DISTRIBUTION`** |
| `15m` | -832,470.00 USD | -866,170.00 USD | **`DISTRIBUTION`** |
| `30m` | -851,110.00 USD | -858,660.00 USD | **`DISTRIBUTION`** |
| `1h` | -825,230.00 USD | -547,360.00 USD | **`DISTRIBUTION`** |
| `2h` | -878,320.00 USD | -378,610.00 USD | **`DISTRIBUTION`** |
| `4h` | -726,290.00 USD | -368,950.00 USD | **`DISTRIBUTION`** |
| `6h` | -836,750.00 USD | -198,970.00 USD | **`DISTRIBUTION`** |
| `8h` | -639,640.00 USD | 445,140.00 USD | **`DISTRIBUTION`** |
| `12h` | 2,120,000.00 USD | 1,710,000.00 USD | **`ACCUMULATION`** |
| `24h` | -226,320.00 USD | 441,210.00 USD | **`ACCUMULATION`** |
| `1w` | -9,330,000.00 USD | -2,930,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -23,310,000.00 USD | 3,660,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+304.87K` | 15m=`-832.47K` | 1h=`-825.23K` | 24h=`-226.32K`
* Futures Capital Netflows: 5m=`-757.87K` | 15m=`-866.17K` | 1h=`-547.36K` | 24h=`+441.21K`
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
  * `2026-10-29 19:41:49 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-29 19:40:49 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-29 19:20:49 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-29 19:09:49 IST`: [youtube.com/ecbeuro] - (Sentiment: `Neutral`)
  * `2026-10-29 19:49:49 IST`: [ecb.europa.eu] - (Sentiment: `Neutral`)
  * `2026-10-29 19:49:49 IST`: [zerohedge.com] - (Sentiment: `Neutral`)
  * `2026-10-29 19:49:49 IST`: [dol.gov] - (Sentiment: `Neutral`)
  * `2026-10-29 19:49:49 IST`: [bea.gov] - (Sentiment: `Neutral`)
  * `2026-10-29 19:49:49 IST`: [bea.gov] - (Sentiment: `Neutral`)
  * `2026-10-29 19:48:49 IST`: [financemagnates.com] - (Sentiment: `Neutral`)
  * `2026-10-29 19:48:49 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-29 16:50:49 IST`: [marctomarket.com] - (Sentiment: `Neutral`)
  * `2026-10-29 15:50:49 IST`: [ecb.europa.eu] - (Sentiment: `Neutral`)
  * `2026-10-29 15:50:49 IST`: [dailyforex.com] - (Sentiment: `Neutral`)
  * `2026-10-29 15:50:49 IST`: [bankofengland.co.uk] - (Sentiment: `Neutral`)


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
  * Execution Entry: `0.3291` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `0.3270` (Risk Distance: `0.0022` pts)
  * +2.5R Take Profit: `0.3346`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `0.3312` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `0.3333` (Risk Distance: `0.0022` pts)
  * +2.5R Take Profit: `0.3257`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`0.3339`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
