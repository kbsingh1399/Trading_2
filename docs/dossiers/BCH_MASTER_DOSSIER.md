# 🏛️ SOVEREIGN CANDIDATE DOSSIER: BCH
**Canonical Key**: `BCH` | **Broker Instrument**: `BCHUSD.p` | **Asset Class**: `Crypto PoW`
**Timestamp**: `2026-10-29 22:49:01 IST` (`2026-10-29 17:19:01 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `289.16` | **Live Ask Quote**: `289.74` | **Mid Price**: `289.45`
- **Spread Points**: `580.00` | **Spread BPS**: `20.04 bps` (Charter Threshold: `25.00 bps`)
- **Gate 1 Clearance**: **`PASS`** | **Execution Posture**: `PASSIVE LIMIT ONLY` | **Order Type Allowed**: `BUY_LIMIT / SELL_LIMIT`
- **True Broker Contract Specifications**:
  * Contract Size: `1.0` | Digits: `2` | Point: `0.01`
  * Point Value (1.0 Lot): `0.01 USD` | Point Value (0.01 Lot): `0.0001 USD`
  * Allowed Lot Sizing: Min Lot=`0.01` | Step Lot=`0.01` | Max Lot=`20.00`
- **Solvency Defense Ladder**:
  * Hard Floor Stop: `4,775.00 USD` (Zero Open Risk) | Operating Defense Buffer: `4,795.00 USD` (Capital Preservation Mode)
  * Kernel Admission Floor: `4,795.00 USD` (`min(balance, equity) - StressedLoss - 2.00 >= 4,795.00 USD`)
- **Pipeline Health (23_Master_Pipeline_Telemetry.parquet)**: Status=`HEALTHY` | Latency=`4.2 ms` | RAM Usage=`385.0 MB`

---

## 2. Technical Profile, VWAP Dispersion Grid & BTC Ribbon
*(Sources: 11_Technical.parquet, 11_Technical_BTC_Ribbon.parquet)*
- **Session Anchor & Volatility**:
  * Session VWAP: `281.59` | VWAP Z-Score: `+1.77` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `2.18` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `67.01` (State: `OVERBOUGHT`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `292.58` | Lower -3.00σ Band: `270.60`
  * Upper +2.51σ Band: `290.79` | Lower -2.51σ Band: `272.39`
  * Upper +2.01σ Band: `288.95` | Lower -2.01σ Band: `274.23`
  * Upper +2.00σ Band: `288.92` | Lower -2.00σ Band: `274.26`
  * Upper +1.28σ Band: `286.28` | Lower -1.28σ Band: `276.90`
  * Upper +1.00σ Band: `285.25` | Lower -1.00σ Band: `277.93`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`286.36` | EMA-20=`283.74` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`282.29` (Slope: `+0.0000`) | EMA-100=`283.65`
  * Institutional Anchors: EMA-144=`284.38` | EMA-200=`284.21` (Slope: `+0.0267`) | EMA-233=`284.47`
- **Range Boundaries**: 24H High=`292.96` | 24H Low=`274.76` | Weekly High=`304.16` | Weekly Low=`274.16`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `286.47` (Distance: `+1.13%`)
  * Point of Control (POC) = `278.70` (Distance: `+3.95%`)
  * Value Area Low (VAL) = `276.52` (Distance: `+4.77%`)
  * Auction Positioning: `ABOVE_VALUE (Imbalance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `RANGE_EXPANSION`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`299.16` | POC=`296.76` | VAL=`289.44`
  * Prior Day Extremes: PDH=`304.16` | PDL=`281.75` | PDC=`288.90`
  * Monday Range Blueprint: High=`283.95` | Mid=`278.61` | Low=`273.26`
  * Developing Weekly Value Area: Weekly VAH=`289.22` | Weekly POC=`278.72` | Weekly VAL=`275.22`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`290.60` | Low=`274.76`
  * London Session (08:00-16:00 UTC): High=`281.86` | Low=`276.86`
  * New York Session (13:00-21:00 UTC): High=`292.96` | Low=`277.16`
  * Initial Balance (First Hour): IB High=`281.86` | IB Low=`279.31`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `288.29` - `290.61`
  * Optimal Trade Entry (OTE 0.705): `290.03`
  * Structural Invalidation Anchor (0.786): `291.77`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `288.48` | `289.03` | `288.04` | `289.01` | `1,225` | 353,611.87 USD | 100,593.58 USD | `+28.45%` | -3,903,229.21 USD | `+0.64` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `5m` | `289.01` | `289.56` | `288.03` | `289.31` | `1,585` | 457,658.93 USD | 19,345.44 USD | `+4.23%` | -3,883,883.77 USD | `+0.35` | **`BULLISH`** | `NEUTRAL CHOP` |
| `5m` | `289.31` | `290.23` | `289.31` | `289.82` | `1,794` | 520,014.78 USD | 115,720.04 USD | `+22.25%` | -3,768,163.73 USD | `+0.66` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `289.20` | `290.08` | `287.08` | `289.59` | `8,010` | 2,309,907.78 USD | 33,346.39 USD | `+1.44%` | -3,863,737.93 USD | `+0.12` | **`BULLISH`** | `NEUTRAL CHOP` |
| `15m` | `289.60` | `290.07` | `287.97` | `288.48` | `5,289` | 1,528,178.86 USD | -140,084.86 USD | `-9.17%` | -4,003,822.79 USD | `-0.26` | **`BEARISH`** | `DELTA ALIGNED` |
| `15m` | `288.48` | `290.23` | `288.03` | `289.82` | `4,604` | 1,331,285.57 USD | 235,659.06 USD | `+17.70%` | -3,768,163.73 USD | `+0.57` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `1h` | `282.43` | `288.24` | `282.14` | `287.96` | `22,353` | 6,361,302.26 USD | 275,075.91 USD | `+4.32%` | -1,829,450.48 USD | `+0.48` | **`BULLISH`** | `NEUTRAL CHOP` |
| `1h` | `287.97` | `293.41` | `286.92` | `288.48` | `47,822` | 13,869,157.35 USD | -2,291,446.03 USD | `-16.52%` | -4,120,896.51 USD | `-2.84` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `1h` | `288.48` | `290.23` | `288.03` | `289.81` | `4,601` | 1,330,173.16 USD | 235,032.99 USD | `+17.67%` | -3,885,863.52 USD | `+0.61` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `4h` | `278.88` | `282.00` | `277.22` | `279.37` | `40,922` | 11,454,296.89 USD | -658,851.13 USD | `-5.75%` | -2,731,740.69 USD | `+0.02` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `279.38` | `288.24` | `277.49` | `287.96` | `74,069` | 20,847,128.37 USD | 1,744,736.30 USD | `+8.37%` | -987,004.39 USD | `+1.23` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `287.97` | `293.41` | `286.92` | `289.85` | `52,429` | 15,201,195.92 USD | -2,055,033.98 USD | `-13.52%` | -3,042,038.37 USD | `-0.97` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `288.93` | `289.90` | `275.10` | `277.35` | `99,418` | 27,984,350.92 USD | -2,870,393.66 USD | `-10.26%` | -1,919,042.18 USD | `-1.00` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `277.35` | `282.39` | `276.59` | `278.88` | `47,861` | 13,383,109.09 USD | -153,847.38 USD | `-1.15%` | -2,072,889.56 USD | `+0.33` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `278.88` | `282.00` | `277.22` | `279.37` | `40,922` | 11,454,296.89 USD | -658,851.13 USD | `-5.75%` | -2,731,740.69 USD | `+0.02` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `279.38` | `288.24` | `277.49` | `287.96` | `74,069` | 20,847,128.37 USD | 1,744,736.30 USD | `+8.37%` | -987,004.39 USD | `+1.23` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `287.97` | `293.41` | `286.92` | `289.85` | `52,429` | 15,201,195.92 USD | -2,055,033.98 USD | `-13.52%` | -3,042,038.37 USD | `-0.97` | **`BEARISH`** | `BEARISH ABSORPTION` |

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
| --- | **`289.45`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

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
| `1987` | `0x12d2...f97f` | `LONG` | 1,048,853.59 USD | `3,627,243,000,000.00` | `303.26` | `289.17` | `0.000000` | -51,145.75 USD | `-4.88%` | `10X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| Intel | Baseline | - | - | - | Neutral | - | No anomalous telegram alerts in current window | - |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`290.27` (Vol: 199,700.00 USD, Dist: `+3.69%`) | Long MP=`271.71` (Vol: 159,600.00 USD, Dist: `--2.94%`)
  * 48H Horizon: Short MP=`290.32` (Vol: 213,700.00 USD, Dist: `+3.71%`) | Long MP=`271.85` (Vol: 166,000.00 USD, Dist: `--2.89%`)
  * 3D Horizon: Short MP=`290.32` (Vol: 213,700.00 USD, Dist: `+3.71%`) | Long MP=`274.67` (Vol: 204,600.00 USD, Dist: `--1.88%`)
  * 7D Horizon: Short MP=`290.28` (Vol: 199,700.00 USD, Dist: `+3.69%`) | Long MP=`263.68` (Vol: 297,200.00 USD, Dist: `--5.81%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long Liquidation` | `95.50` | 920.05 USD | 449,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `101.50` | 6,240.00 USD | 448,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `102.50` | 4,080.00 USD | 442,540.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `109.50` | 48,470.00 USD | 438,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `115.50` | 169.78 USD | 389,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `118.50` | 212.35 USD | 389,820.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `122.50` | 124.46 USD | 389,610.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `126.50` | 658.18 USD | 389,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `137.50` | 6,880.00 USD | 388,820.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `142.50` | 2,140.00 USD | 381,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `145.50` | 2,070.00 USD | 379,810.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `147.50` | 895.47 USD | 377,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `148.50` | 1,270.00 USD | 376,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `149.50` | 2,370.00 USD | 375,580.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `150.50` | 586.50 USD | 373,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `152.50` | 303.78 USD | 372,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `161.50` | 656.82 USD | 372,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `162.50` | 325.00 USD | 371,670.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `167.50` | 285.75 USD | 371,340.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `169.50` | 5,340.00 USD | 371,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `170.50` | 426.25 USD | 365,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `174.50` | 169.96 USD | 365,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `175.50` | 516.67 USD | 365,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `176.50` | 373.83 USD | 364,610.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `178.50` | 535.50 USD | 364,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `181.50` | 804.04 USD | 363,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `183.50` | 191.57 USD | 362,890.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `184.50` | 616.05 USD | 362,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `188.50` | 418.28 USD | 362,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `191.50` | 858.49 USD | 361,670.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `192.50` | 1,490.00 USD | 360,810.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `195.50` | 370.47 USD | 359,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `198.50` | 1,610.00 USD | 358,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `199.50` | 765.08 USD | 357,340.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `200.50` | 293.13 USD | 356,570.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `202.50` | 420.39 USD | 356,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `204.50` | 39,880.00 USD | 355,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `205.50` | 191.53 USD | 315,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `210.50` | 42,310.00 USD | 315,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `213.50` | 3,800.00 USD | 273,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `215.50` | 239.85 USD | 269,670.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `219.50` | 5,690.00 USD | 269,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `220.50` | 1,010.00 USD | 263,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `223.50` | 32,860.00 USD | 262,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `224.50` | 1,630.00 USD | 229,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `226.50` | 1,240.00 USD | 228,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `227.50` | 174.49 USD | 227,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `228.50` | 642.77 USD | 226,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `229.50` | 1,190.00 USD | 226,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `230.50` | 8,040.00 USD | 225,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `231.50` | 295.86 USD | 216,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `232.50` | 1,890.00 USD | 216,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `234.50` | 217.85 USD | 214,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `239.50` | 1,030.00 USD | 214,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `241.50` | 367.32 USD | 213,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `242.50` | 5,660.00 USD | 213,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `243.50` | 1,200.00 USD | 207,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `244.50` | 4,220.00 USD | 206,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `245.50` | 1,030.00 USD | 202,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `247.50` | 12,340.00 USD | 201,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `250.50` | 1,330.00 USD | 188,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `251.50` | 268.35 USD | 187,380.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `252.50` | 1,030.00 USD | 187,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `253.20` | 8,040,000.00 USD | 8,040,000.00 USD | 9,620.00 USD | 19,920.00 USD | 6,250.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `253.20` | 8,040,000.00 USD | 8,040,000.00 USD | 9,620.00 USD | 19,920.00 USD | 6,250.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `253.60` | 8,000,000.00 USD | 8,000,000.00 USD | 14,720.00 USD | 13,380.00 USD | 5,280.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `253.60` | 8,000,000.00 USD | 8,000,000.00 USD | 14,720.00 USD | 13,380.00 USD | 5,280.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `254.00` | 7,970,000.00 USD | 7,970,000.00 USD | 144.00 USD | 5,000.00 USD | 3.86 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `254.00` | 7,970,000.00 USD | 7,970,000.00 USD | 144.00 USD | 5,000.00 USD | 3.86 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `254.40` | 7,960,000.00 USD | 7,960,000.00 USD | 134.35 USD | 48.50 USD | 4,090.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `254.40` | 7,960,000.00 USD | 7,960,000.00 USD | 134.35 USD | 48.50 USD | 4,090.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `254.50` | 11,650.00 USD | 186,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `254.80` | 7,960,000.00 USD | 7,960,000.00 USD | 14,480.00 USD | 2,050.00 USD | 18,300.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `254.80` | 7,960,000.00 USD | 7,960,000.00 USD | 14,480.00 USD | 2,050.00 USD | 18,300.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `255.20` | 7,920,000.00 USD | 7,920,000.00 USD | 13,640.00 USD | 6,590.00 USD | 0.34 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `255.20` | 7,920,000.00 USD | 7,920,000.00 USD | 13,640.00 USD | 6,590.00 USD | 0.34 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `255.50` | 3,660.00 USD | 174,440.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `255.60` | 7,900,000.00 USD | 7,900,000.00 USD | 13,950.00 USD | 7,480.00 USD | 8,710.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `255.60` | 7,900,000.00 USD | 7,900,000.00 USD | 13,950.00 USD | 7,480.00 USD | 8,710.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `256.00` | 7,870,000.00 USD | 7,870,000.00 USD | 11,710.00 USD | 23.27 USD | 27.52 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `256.00` | 7,870,000.00 USD | 7,870,000.00 USD | 11,710.00 USD | 23.27 USD | 27.52 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `256.40` | 7,860,000.00 USD | 7,860,000.00 USD | 12,240.00 USD | 6,960.00 USD | 8,970.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `256.40` | 7,860,000.00 USD | 7,860,000.00 USD | 12,240.00 USD | 6,960.00 USD | 8,970.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `256.50` | 2,480.00 USD | 170,780.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `256.80` | 7,830,000.00 USD | 7,830,000.00 USD | 9,170.00 USD | 11,170.00 USD | 10,050.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `256.80` | 7,830,000.00 USD | 7,830,000.00 USD | 9,170.00 USD | 11,170.00 USD | 10,050.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `257.20` | 7,800,000.00 USD | 7,800,000.00 USD | 4,320.00 USD | 10,960.00 USD | 7,320.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `257.20` | 7,800,000.00 USD | 7,800,000.00 USD | 4,320.00 USD | 10,960.00 USD | 7,320.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `257.50` | 366.42 USD | 168,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `257.60` | 7,780,000.00 USD | 7,780,000.00 USD | 479.45 USD | 0.00 USD | 9,250.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `257.60` | 7,780,000.00 USD | 7,780,000.00 USD | 479.45 USD | 0.00 USD | 9,250.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `258.00` | 7,770,000.00 USD | 7,770,000.00 USD | 3,740.00 USD | 991.50 USD | 20,060.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `258.00` | 7,770,000.00 USD | 7,770,000.00 USD | 3,740.00 USD | 991.50 USD | 20,060.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `258.40` | 7,740,000.00 USD | 7,740,000.00 USD | 8,100.00 USD | 8,380.00 USD | 5,270.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `258.40` | 7,740,000.00 USD | 7,740,000.00 USD | 8,100.00 USD | 8,380.00 USD | 5,270.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `258.50` | 176.56 USD | 167,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `258.80` | 7,720,000.00 USD | 7,720,000.00 USD | 17,870.00 USD | 10,540.00 USD | 11,820.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `258.80` | 7,720,000.00 USD | 7,720,000.00 USD | 17,870.00 USD | 10,540.00 USD | 11,820.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `259.20` | 7,680,000.00 USD | 7,680,000.00 USD | 5,410.00 USD | 9,350.00 USD | 11,440.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `259.20` | 7,680,000.00 USD | 7,680,000.00 USD | 5,410.00 USD | 9,350.00 USD | 11,440.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `259.60` | 7,660,000.00 USD | 7,660,000.00 USD | 4,840.00 USD | 4,550.00 USD | 2,640.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `259.60` | 7,660,000.00 USD | 7,660,000.00 USD | 4,840.00 USD | 4,550.00 USD | 2,640.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `260.00` | 7,640,000.00 USD | 7,640,000.00 USD | 7,850.00 USD | 17,100.00 USD | 18,370.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `260.00` | 7,640,000.00 USD | 7,640,000.00 USD | 7,850.00 USD | 17,100.00 USD | 18,370.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `260.40` | 7,600,000.00 USD | 7,600,000.00 USD | 2,680.00 USD | 10,080.00 USD | 825.30 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `260.40` | 7,600,000.00 USD | 7,600,000.00 USD | 2,680.00 USD | 10,080.00 USD | 825.30 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `260.50` | 3,860.00 USD | 167,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `260.80` | 7,590,000.00 USD | 7,590,000.00 USD | 9,630.00 USD | 14,540.00 USD | 6,170.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `260.80` | 7,590,000.00 USD | 7,590,000.00 USD | 9,630.00 USD | 14,540.00 USD | 6,170.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `261.20` | 7,560,000.00 USD | 7,560,000.00 USD | 7,970.00 USD | 11,470.00 USD | 503.44 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `261.20` | 7,560,000.00 USD | 7,560,000.00 USD | 7,970.00 USD | 11,470.00 USD | 503.44 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `261.60` | 7,540,000.00 USD | 7,540,000.00 USD | 8,930.00 USD | 5,020.00 USD | 2.10 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `261.60` | 7,540,000.00 USD | 7,540,000.00 USD | 8,930.00 USD | 5,020.00 USD | 2.10 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `262.00` | 7,520,000.00 USD | 7,520,000.00 USD | 367.62 USD | 213.04 USD | 2,590.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `262.00` | 7,520,000.00 USD | 7,520,000.00 USD | 367.62 USD | 213.04 USD | 2,590.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `262.40` | 7,520,000.00 USD | 7,520,000.00 USD | 8,640.00 USD | 626.24 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `262.40` | 7,520,000.00 USD | 7,520,000.00 USD | 8,640.00 USD | 626.24 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `262.50` | 1,970.00 USD | 163,890.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `262.80` | 7,510,000.00 USD | 7,510,000.00 USD | 150.60 USD | 1,190.00 USD | 12.23 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `262.80` | 7,510,000.00 USD | 7,510,000.00 USD | 150.60 USD | 1,190.00 USD | 12.23 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `263.20` | 7,510,000.00 USD | 7,510,000.00 USD | 8,670.00 USD | 571.81 USD | 16,170.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `263.20` | 7,510,000.00 USD | 7,510,000.00 USD | 8,670.00 USD | 571.81 USD | 16,170.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `263.60` | 7,480,000.00 USD | 7,480,000.00 USD | 630.84 USD | 939.44 USD | 16,150.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `263.60` | 7,480,000.00 USD | 7,480,000.00 USD | 630.84 USD | 939.44 USD | 16,150.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `264.00` | 7,470,000.00 USD | 7,470,000.00 USD | 1,210.00 USD | 726.29 USD | 6.19 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `264.00` | 7,470,000.00 USD | 7,470,000.00 USD | 1,210.00 USD | 726.29 USD | 6.19 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `264.40` | 7,460,000.00 USD | 7,460,000.00 USD | 1,660.00 USD | 724.53 USD | 9.17 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `264.40` | 7,460,000.00 USD | 7,460,000.00 USD | 1,660.00 USD | 724.53 USD | 9.17 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `264.50` | 280.37 USD | 161,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `264.80` | 7,460,000.00 USD | 7,460,000.00 USD | 28,700.00 USD | 957.20 USD | 52,290.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `264.80` | 7,460,000.00 USD | 7,460,000.00 USD | 28,700.00 USD | 957.20 USD | 52,290.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `265.20` | 7,380,000.00 USD | 7,380,000.00 USD | 20,770.00 USD | 8,760.00 USD | 70.26 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `265.20` | 7,380,000.00 USD | 7,380,000.00 USD | 20,770.00 USD | 8,760.00 USD | 70.26 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `265.50` | 121,910.00 USD | 161,640.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `265.60` | 7,350,000.00 USD | 7,350,000.00 USD | 16,150.00 USD | 23,430.00 USD | 67,100.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `265.60` | 7,350,000.00 USD | 7,350,000.00 USD | 16,150.00 USD | 23,430.00 USD | 67,100.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `266.00` | 7,240,000.00 USD | 7,240,000.00 USD | 8,550.00 USD | 862.64 USD | 14.54 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `266.00` | 7,240,000.00 USD | 7,240,000.00 USD | 8,550.00 USD | 862.64 USD | 14.54 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `266.40` | 7,230,000.00 USD | 7,230,000.00 USD | 37,680.00 USD | 287.83 USD | 5,010.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `266.40` | 7,230,000.00 USD | 7,230,000.00 USD | 37,680.00 USD | 287.83 USD | 5,010.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `266.80` | 7,190,000.00 USD | 7,190,000.00 USD | 23,390.00 USD | 3,250.00 USD | 8,520.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `266.80` | 7,190,000.00 USD | 7,190,000.00 USD | 23,390.00 USD | 3,250.00 USD | 8,520.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `267.20` | 7,160,000.00 USD | 7,160,000.00 USD | 16,540.00 USD | 6,600.00 USD | 5,300.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `267.20` | 7,160,000.00 USD | 7,160,000.00 USD | 16,540.00 USD | 6,600.00 USD | 5,300.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `267.50` | 1,490.00 USD | 39,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `267.60` | 7,130,000.00 USD | 7,130,000.00 USD | 30,700.00 USD | 70,890.00 USD | 9,570.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `267.60` | 7,130,000.00 USD | 7,130,000.00 USD | 30,700.00 USD | 70,890.00 USD | 9,570.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `268.00` | 7,020,000.00 USD | 7,020,000.00 USD | 104,910.00 USD | 112,850.00 USD | 35,850.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `268.00` | 7,020,000.00 USD | 7,020,000.00 USD | 104,910.00 USD | 112,850.00 USD | 35,850.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `268.40` | 6,760,000.00 USD | 6,760,000.00 USD | 57,930.00 USD | 99,140.00 USD | 32,080.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `268.40` | 6,760,000.00 USD | 6,760,000.00 USD | 57,930.00 USD | 99,140.00 USD | 32,080.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `268.50` | 7,020.00 USD | 38,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `268.80` | 6,570,000.00 USD | 6,570,000.00 USD | 100,660.00 USD | 58,170.00 USD | 56,650.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `268.80` | 6,570,000.00 USD | 6,570,000.00 USD | 100,660.00 USD | 58,170.00 USD | 56,650.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `269.20` | 6,360,000.00 USD | 6,360,000.00 USD | 21,700.00 USD | 15,790.00 USD | 12,930.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `269.20` | 6,360,000.00 USD | 6,360,000.00 USD | 21,700.00 USD | 16,130.00 USD | 12,930.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `269.50` | 11,700.00 USD | 31,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `269.60` | 6,310,000.00 USD | 6,310,000.00 USD | 35,340.00 USD | 20,780.00 USD | 10,410.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `269.60` | 6,310,000.00 USD | 6,310,000.00 USD | 35,340.00 USD | 20,780.00 USD | 10,410.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `270.00` | 6,240,000.00 USD | 6,240,000.00 USD | 37,260.00 USD | 48,490.00 USD | 94,440.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `270.00` | 6,240,000.00 USD | 6,240,000.00 USD | 37,260.00 USD | 48,490.00 USD | 94,440.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `270.40` | 6,060,000.00 USD | 6,060,000.00 USD | 109,620.00 USD | 47,480.00 USD | 45,950.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `270.40` | 6,060,000.00 USD | 6,060,000.00 USD | 109,620.00 USD | 47,480.00 USD | 45,950.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `270.80` | 5,860,000.00 USD | 5,860,000.00 USD | 44,260.00 USD | 38,250.00 USD | 1,620.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `270.80` | 5,860,000.00 USD | 5,860,000.00 USD | 44,260.00 USD | 38,250.00 USD | 1,620.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `271.20` | 5,770,000.00 USD | 5,770,000.00 USD | 48,420.00 USD | 54,420.00 USD | 139,870.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `271.20` | 5,770,000.00 USD | 5,770,000.00 USD | 48,420.00 USD | 54,420.00 USD | 139,870.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `271.50` | 1,000.00 USD | 19,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `271.60` | 5,530,000.00 USD | 5,530,000.00 USD | 17,150.00 USD | 18,090.00 USD | 36,920.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `271.60` | 5,530,000.00 USD | 5,530,000.00 USD | 17,150.00 USD | 18,090.00 USD | 36,920.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `272.00` | 5,460,000.00 USD | 5,460,000.00 USD | 155,850.00 USD | 48,800.00 USD | 41,810.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `272.00` | 5,460,000.00 USD | 5,460,000.00 USD | 155,850.00 USD | 48,800.00 USD | 41,810.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `272.40` | 5,210,000.00 USD | 5,210,000.00 USD | 89,460.00 USD | 11,900.00 USD | 32,640.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `272.40` | 5,210,000.00 USD | 5,210,000.00 USD | 89,460.00 USD | 11,900.00 USD | 32,640.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `272.80` | 5,080,000.00 USD | 5,080,000.00 USD | 95,440.00 USD | 46,670.00 USD | 20,950.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `272.80` | 5,080,000.00 USD | 5,080,000.00 USD | 95,440.00 USD | 46,670.00 USD | 20,950.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `273.20` | 4,920,000.00 USD | 4,920,000.00 USD | 66,160.00 USD | 132,260.00 USD | 35,090.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `273.20` | 4,920,000.00 USD | 4,920,000.00 USD | 66,160.00 USD | 132,260.00 USD | 35,090.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `273.60` | 4,680,000.00 USD | 4,680,000.00 USD | 236,160.00 USD | 240,340.00 USD | 90,160.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `273.60` | 4,680,000.00 USD | 4,680,000.00 USD | 236,160.00 USD | 240,340.00 USD | 90,160.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `274.00` | 4,120,000.00 USD | 4,120,000.00 USD | 144,320.00 USD | 229,740.00 USD | 95,270.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `274.00` | 4,120,000.00 USD | 4,120,000.00 USD | 144,320.00 USD | 230,200.00 USD | 95,270.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `274.40` | 3,650,000.00 USD | 3,650,000.00 USD | 216,260.00 USD | 142,650.00 USD | 145,010.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `274.40` | 3,650,000.00 USD | 3,650,000.00 USD | 216,260.00 USD | 142,650.00 USD | 145,010.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `274.50` | 567.94 USD | 18,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `274.80` | 3,140,000.00 USD | 3,140,000.00 USD | 51,320.00 USD | 33,360.00 USD | 58,350.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `274.80` | 3,140,000.00 USD | 3,140,000.00 USD | 51,320.00 USD | 33,360.00 USD | 58,350.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `275.20` | 3,000,000.00 USD | 3,000,000.00 USD | 77,850.00 USD | 44,580.00 USD | 56,930.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `275.20` | 3,000,000.00 USD | 3,000,000.00 USD | 77,850.00 USD | 44,580.00 USD | 56,930.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `275.60` | 2,820,000.00 USD | 2,820,000.00 USD | 44,240.00 USD | 44,510.00 USD | 35,830.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `275.60` | 2,820,000.00 USD | 2,820,000.00 USD | 44,240.00 USD | 44,510.00 USD | 35,830.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `276.00` | 2,690,000.00 USD | 2,690,000.00 USD | 59,560.00 USD | 37,170.00 USD | 22,040.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `276.00` | 2,690,000.00 USD | 2,690,000.00 USD | 59,560.00 USD | 37,170.00 USD | 22,040.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `276.40` | 2,580,000.00 USD | 2,580,000.00 USD | 36,470.00 USD | 42,830.00 USD | 3,230.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `276.40` | 2,580,000.00 USD | 2,580,000.00 USD | 36,470.00 USD | 42,830.00 USD | 3,230.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `276.50` | 205.44 USD | 17,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `276.80` | 2,490,000.00 USD | 2,490,000.00 USD | 10,750.00 USD | 15,870.00 USD | 11,360.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `276.80` | 2,490,000.00 USD | 2,490,000.00 USD | 10,750.00 USD | 15,870.00 USD | 11,360.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `277.20` | 2,460,000.00 USD | 2,460,000.00 USD | 301.20 USD | 80,120.00 USD | 21,180.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `277.20` | 2,460,000.00 USD | 2,460,000.00 USD | 301.20 USD | 80,120.00 USD | 21,180.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `277.60` | 2,350,000.00 USD | 2,350,000.00 USD | 57,640.00 USD | 47,660.00 USD | 5.52 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `277.60` | 2,350,000.00 USD | 2,350,000.00 USD | 57,640.00 USD | 47,660.00 USD | 5.52 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `278.00` | 2,250,000.00 USD | 2,250,000.00 USD | 12,650.00 USD | 9,490.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `278.00` | 2,250,000.00 USD | 2,250,000.00 USD | 12,650.00 USD | 9,490.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `278.40` | 2,230,000.00 USD | 2,230,000.00 USD | 61,240.00 USD | 25,470.00 USD | 37,930.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `278.40` | 2,230,000.00 USD | 2,230,000.00 USD | 61,240.00 USD | 25,470.00 USD | 37,930.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `278.80` | 2,100,000.00 USD | 2,100,000.00 USD | 22,630.00 USD | 22,990.00 USD | 10,340.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `278.80` | 2,100,000.00 USD | 2,100,000.00 USD | 22,630.00 USD | 22,990.00 USD | 10,340.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `279.20` | 2,050,000.00 USD | 2,050,000.00 USD | 42,910.00 USD | 23,330.00 USD | 23,180.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `279.20` | 2,050,000.00 USD | 2,050,000.00 USD | 42,910.00 USD | 23,330.00 USD | 23,180.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `279.60` | 1,960,000.00 USD | 1,960,000.00 USD | 20,320.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `279.60` | 1,960,000.00 USD | 1,960,000.00 USD | 20,320.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `280.00` | 1,940,000.00 USD | 1,940,000.00 USD | 21,040.00 USD | 0.00 USD | 17,110.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `280.00` | 1,940,000.00 USD | 1,940,000.00 USD | 21,040.00 USD | 0.00 USD | 17,110.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `280.40` | 1,900,000.00 USD | 1,900,000.00 USD | 8,720.00 USD | 0.00 USD | 41,630.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `280.40` | 1,900,000.00 USD | 1,900,000.00 USD | 8,720.00 USD | 0.00 USD | 41,630.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `280.80` | 1,850,000.00 USD | 1,850,000.00 USD | 21,670.00 USD | 0.00 USD | 64,530.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `280.80` | 1,850,000.00 USD | 1,850,000.00 USD | 21,670.00 USD | 0.00 USD | 64,530.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `281.20` | 1,760,000.00 USD | 1,760,000.00 USD | 8,920.00 USD | 0.00 USD | 66,500.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `281.20` | 1,760,000.00 USD | 1,760,000.00 USD | 8,920.00 USD | 0.00 USD | 66,500.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `281.60` | 1,690,000.00 USD | 1,690,000.00 USD | 0.00 USD | 0.00 USD | 27,950.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `281.60` | 1,690,000.00 USD | 1,690,000.00 USD | 0.00 USD | 0.00 USD | 27,950.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `282.00` | 1,660,000.00 USD | 1,660,000.00 USD | 36,030.00 USD | 39,110.00 USD | 120,430.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `282.00` | 1,660,000.00 USD | 1,660,000.00 USD | 36,030.00 USD | 39,110.00 USD | 120,430.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `282.40` | 1,460,000.00 USD | 1,460,000.00 USD | 0.00 USD | 0.00 USD | 70,940.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `282.40` | 1,460,000.00 USD | 1,460,000.00 USD | 0.00 USD | 0.00 USD | 70,940.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `282.80` | 1,390,000.00 USD | 1,390,000.00 USD | 0.00 USD | 67,970.00 USD | 51,860.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `282.80` | 1,390,000.00 USD | 1,390,000.00 USD | 0.00 USD | 67,970.00 USD | 51,860.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `283.20` | 1,270,000.00 USD | 1,270,000.00 USD | 0.00 USD | 0.00 USD | 81,880.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `283.20` | 1,270,000.00 USD | 1,270,000.00 USD | 0.00 USD | 0.00 USD | 81,880.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `283.60` | 1,190,000.00 USD | 1,190,000.00 USD | 0.00 USD | 11,490.00 USD | 4,100.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `283.60` | 1,190,000.00 USD | 1,190,000.00 USD | 0.00 USD | 11,490.00 USD | 4,100.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `284.00` | 1,170,000.00 USD | 1,170,000.00 USD | 0.00 USD | 18,990.00 USD | 30,860.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `284.00` | 1,170,000.00 USD | 1,170,000.00 USD | 0.00 USD | 18,990.00 USD | 30,860.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `284.40` | 1,120,000.00 USD | 1,120,000.00 USD | 37,810.00 USD | 76,740.00 USD | 20,690.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `284.40` | 1,120,000.00 USD | 1,120,000.00 USD | 37,810.00 USD | 76,740.00 USD | 20,690.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `284.80` | 989,150.00 USD | 989,150.00 USD | 31,830.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `284.80` | 989,150.00 USD | 989,150.00 USD | 31,830.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `285.20` | 957,320.00 USD | 957,320.00 USD | 0.00 USD | 0.00 USD | 44,680.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `285.20` | 957,320.00 USD | 957,320.00 USD | 0.00 USD | 0.00 USD | 44,680.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `285.50` | 17,750.00 USD | 17,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `285.60` | 912,640.00 USD | 912,640.00 USD | 91,500.00 USD | 115,180.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `285.60` | 912,640.00 USD | 912,640.00 USD | 91,500.00 USD | 115,180.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `286.00` | 705,960.00 USD | 705,960.00 USD | 0.00 USD | 30,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `286.00` | 705,960.00 USD | 705,960.00 USD | 0.00 USD | 30,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `286.40` | 675,960.00 USD | 675,960.00 USD | 79,480.00 USD | 40,040.00 USD | 37,510.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `286.40` | 675,960.00 USD | 675,960.00 USD | 79,480.00 USD | 40,040.00 USD | 37,510.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `286.80` | 518,930.00 USD | 518,930.00 USD | 114,760.00 USD | 69,490.00 USD | 91,300.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `286.80` | 518,930.00 USD | 518,930.00 USD | 114,760.00 USD | 69,490.00 USD | 91,300.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `287.20` | 243,380.00 USD | 243,380.00 USD | 0.00 USD | 117,540.00 USD | 32,710.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `287.20` | 243,380.00 USD | 243,380.00 USD | 0.00 USD | 117,540.00 USD | 32,710.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `287.60` | 93,120.00 USD | 93,120.00 USD | 0.00 USD | 11,010.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `287.60` | 93,120.00 USD | 93,120.00 USD | 0.00 USD | 11,010.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `288.00` | 82,110.00 USD | 82,110.00 USD | 0.00 USD | 0.00 USD | 45,010.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `288.00` | 82,110.00 USD | 82,110.00 USD | 0.00 USD | 0.00 USD | 45,010.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `288.40` | 37,100.00 USD | 37,100.00 USD | 10,110.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `288.40` | 37,100.00 USD | 37,100.00 USD | 10,110.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `288.80` | 26,990.00 USD | 26,990.00 USD | 26,990.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `288.80` | 26,990.00 USD | 26,990.00 USD | 26,990.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `289.20` | 11,990.00 USD | 11,990.00 USD | 0.00 USD | 11,990.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `289.20` | 11,990.00 USD | 11,990.00 USD | 0.00 USD | 11,990.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `291.20` | 186,300.00 USD | 186,300.00 USD | 0.00 USD | 128,140.00 USD | 46,160.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `291.20` | 186,300.00 USD | 186,300.00 USD | 0.00 USD | 128,140.00 USD | 46,160.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `291.60` | 282,700.00 USD | 282,700.00 USD | 0.00 USD | 41,860.00 USD | 54,540.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `291.60` | 282,700.00 USD | 282,700.00 USD | 0.00 USD | 41,860.00 USD | 54,540.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `292.00` | 309,090.00 USD | 309,090.00 USD | 0.00 USD | 26,380.00 USD | 7.32 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `292.00` | 309,090.00 USD | 309,090.00 USD | 0.00 USD | 26,380.00 USD | 7.32 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `292.40` | 352,360.00 USD | 352,360.00 USD | 0.00 USD | 43,260.00 USD | 8.42 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `292.40` | 352,360.00 USD | 352,360.00 USD | 0.00 USD | 43,260.00 USD | 8.42 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `292.80` | 450,720.00 USD | 450,720.00 USD | 1,040.00 USD | 97,310.00 USD | 6.65 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `292.80` | 450,720.00 USD | 450,720.00 USD | 1,040.00 USD | 97,310.00 USD | 6.65 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `293.20` | 524,280.00 USD | 524,280.00 USD | 443.30 USD | 73,120.00 USD | 0.42 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `293.20` | 524,280.00 USD | 524,280.00 USD | 443.30 USD | 73,120.00 USD | 0.42 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `293.60` | 689,800.00 USD | 689,800.00 USD | 44,620.00 USD | 65,190.00 USD | 55,700.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `293.60` | 689,800.00 USD | 689,800.00 USD | 44,620.00 USD | 65,190.00 USD | 55,700.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `294.00` | 774,020.00 USD | 774,020.00 USD | 8,430.00 USD | 41,700.00 USD | 34,090.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `294.00` | 774,020.00 USD | 774,020.00 USD | 8,430.00 USD | 41,700.00 USD | 34,090.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `294.40` | 1,100,000.00 USD | 1,100,000.00 USD | 112,960.00 USD | 115,230.00 USD | 96,530.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `294.40` | 1,100,000.00 USD | 1,100,000.00 USD | 112,960.00 USD | 115,230.00 USD | 96,530.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `294.80` | 1,310,000.00 USD | 1,310,000.00 USD | 56,500.00 USD | 79,340.00 USD | 70,850.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `294.80` | 1,310,000.00 USD | 1,310,000.00 USD | 56,500.00 USD | 79,340.00 USD | 70,850.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `295.20` | 1,460,000.00 USD | 1,460,000.00 USD | 77,470.00 USD | 49,290.00 USD | 23,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `295.20` | 1,460,000.00 USD | 1,460,000.00 USD | 77,470.00 USD | 49,290.00 USD | 23,210.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `295.50` | 612.57 USD | 612.57 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `295.60` | 1,730,000.00 USD | 1,730,000.00 USD | 105,500.00 USD | 108,340.00 USD | 63,330.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `295.60` | 1,730,000.00 USD | 1,730,000.00 USD | 105,500.00 USD | 108,340.00 USD | 63,330.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `296.00` | 1,930,000.00 USD | 1,930,000.00 USD | 85,930.00 USD | 76,170.00 USD | 39,110.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `296.00` | 1,930,000.00 USD | 1,930,000.00 USD | 85,930.00 USD | 76,170.00 USD | 39,110.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `296.40` | 2,080,000.00 USD | 2,080,000.00 USD | 77,790.00 USD | 50,830.00 USD | 18,610.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `296.40` | 2,080,000.00 USD | 2,080,000.00 USD | 77,790.00 USD | 50,830.00 USD | 18,610.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `296.80` | 2,210,000.00 USD | 2,210,000.00 USD | 32,000.00 USD | 35,500.00 USD | 64,680.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `296.80` | 2,210,000.00 USD | 2,210,000.00 USD | 32,000.00 USD | 35,500.00 USD | 64,680.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `297.20` | 2,330,000.00 USD | 2,330,000.00 USD | 59,030.00 USD | 27,370.00 USD | 31,730.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `297.20` | 2,330,000.00 USD | 2,330,000.00 USD | 59,030.00 USD | 27,370.00 USD | 31,730.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `297.60` | 2,370,000.00 USD | 2,370,000.00 USD | 5,970.00 USD | 1,010.00 USD | 32,550.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `297.60` | 2,370,000.00 USD | 2,370,000.00 USD | 5,970.00 USD | 1,010.00 USD | 32,550.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `298.00` | 2,500,000.00 USD | 2,500,000.00 USD | 58,630.00 USD | 8,080.00 USD | 58,410.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `298.00` | 2,500,000.00 USD | 2,500,000.00 USD | 58,630.00 USD | 8,080.00 USD | 58,410.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `298.40` | 2,620,000.00 USD | 2,620,000.00 USD | 5,480.00 USD | 15,780.00 USD | 100,250.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `298.40` | 2,620,000.00 USD | 2,620,000.00 USD | 5,480.00 USD | 15,780.00 USD | 100,250.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `298.80` | 2,800,000.00 USD | 2,800,000.00 USD | 56,580.00 USD | 18,110.00 USD | 107,460.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `298.80` | 2,800,000.00 USD | 2,800,000.00 USD | 56,580.00 USD | 18,110.00 USD | 107,460.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `299.20` | 2,890,000.00 USD | 2,890,000.00 USD | 37,170.00 USD | 36,500.00 USD | 12,310.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `299.20` | 2,890,000.00 USD | 2,890,000.00 USD | 37,170.00 USD | 36,500.00 USD | 12,310.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `299.50` | 1,220.00 USD | 1,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `299.60` | 2,950,000.00 USD | 2,950,000.00 USD | 18,100.00 USD | 16,000.00 USD | 31,200.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `299.60` | 2,950,000.00 USD | 2,950,000.00 USD | 18,100.00 USD | 16,000.00 USD | 31,200.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `300.00` | 3,010,000.00 USD | 3,010,000.00 USD | 22,390.00 USD | 25,550.00 USD | 6,200.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `300.00` | 3,010,000.00 USD | 3,010,000.00 USD | 22,390.00 USD | 25,550.00 USD | 6,200.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `300.40` | 3,100,000.00 USD | 3,100,000.00 USD | 14,470.00 USD | 31,680.00 USD | 45,920.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `300.40` | 3,100,000.00 USD | 3,100,000.00 USD | 14,470.00 USD | 31,680.00 USD | 45,920.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `300.80` | 3,150,000.00 USD | 3,150,000.00 USD | 11,300.00 USD | 30,510.00 USD | 12,770.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `300.80` | 3,150,000.00 USD | 3,150,000.00 USD | 11,300.00 USD | 30,510.00 USD | 12,770.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `301.20` | 3,240,000.00 USD | 3,240,000.00 USD | 35,650.00 USD | 49,010.00 USD | 22.51 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `301.20` | 3,240,000.00 USD | 3,240,000.00 USD | 35,650.00 USD | 49,010.00 USD | 22.51 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `301.50` | 2,380.00 USD | 4,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `301.60` | 3,310,000.00 USD | 3,310,000.00 USD | 32,070.00 USD | 12,240.00 USD | 24,640.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `301.60` | 3,310,000.00 USD | 3,310,000.00 USD | 32,070.00 USD | 12,240.00 USD | 24,640.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `302.00` | 3,390,000.00 USD | 3,390,000.00 USD | 36,140.00 USD | 35,930.00 USD | 11,570.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `302.00` | 3,390,000.00 USD | 3,390,000.00 USD | 36,140.00 USD | 35,930.00 USD | 11,570.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `302.40` | 3,410,000.00 USD | 3,410,000.00 USD | 667.34 USD | 9,620.00 USD | 10,300.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `302.40` | 3,410,000.00 USD | 3,410,000.00 USD | 667.34 USD | 9,620.00 USD | 10,300.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `302.80` | 3,420,000.00 USD | 3,420,000.00 USD | 1,230.00 USD | 1,730.00 USD | 6,540.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `302.80` | 3,420,000.00 USD | 3,420,000.00 USD | 1,230.00 USD | 2,200.00 USD | 6,540.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `303.20` | 3,470,000.00 USD | 3,470,000.00 USD | 32,120.00 USD | 348.99 USD | 14,740.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `303.20` | 3,470,000.00 USD | 3,470,000.00 USD | 32,120.00 USD | 348.99 USD | 14,740.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `303.60` | 3,480,000.00 USD | 3,480,000.00 USD | 9,000.00 USD | 3,300.00 USD | 6,250.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `303.60` | 3,490,000.00 USD | 3,490,000.00 USD | 9,000.00 USD | 3,300.00 USD | 6,250.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `304.00` | 3,540,000.00 USD | 3,540,000.00 USD | 22,400.00 USD | 1,170.00 USD | 32,130.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `304.00` | 3,540,000.00 USD | 3,540,000.00 USD | 22,400.00 USD | 1,170.00 USD | 32,130.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `304.40` | 3,620,000.00 USD | 3,620,000.00 USD | 13,620.00 USD | 10,140.00 USD | 59,180.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `304.40` | 3,620,000.00 USD | 3,620,000.00 USD | 13,620.00 USD | 10,140.00 USD | 59,180.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `304.80` | 3,640,000.00 USD | 3,640,000.00 USD | 592.20 USD | 318.60 USD | 16,360.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `304.80` | 3,640,000.00 USD | 3,640,000.00 USD | 592.20 USD | 318.60 USD | 16,360.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `305.20` | 3,650,000.00 USD | 3,650,000.00 USD | 10,560.00 USD | 236.66 USD | 2,010.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `305.20` | 3,650,000.00 USD | 3,650,000.00 USD | 10,560.00 USD | 236.66 USD | 2,010.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `305.60` | 3,660,000.00 USD | 3,660,000.00 USD | 4,670.00 USD | 1,770.00 USD | 1,490.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `305.60` | 3,660,000.00 USD | 3,660,000.00 USD | 4,670.00 USD | 1,770.00 USD | 1,490.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `306.00` | 3,680,000.00 USD | 3,680,000.00 USD | 9,590.00 USD | 2,740.00 USD | 3,270.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `306.00` | 3,680,000.00 USD | 3,680,000.00 USD | 9,590.00 USD | 2,740.00 USD | 3,270.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `306.40` | 3,690,000.00 USD | 3,690,000.00 USD | 4,560.00 USD | 9,460.00 USD | 68.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `306.40` | 3,690,000.00 USD | 3,690,000.00 USD | 4,560.00 USD | 9,460.00 USD | 68.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `306.80` | 3,760,000.00 USD | 3,760,000.00 USD | 28,610.00 USD | 35,400.00 USD | 5,490.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `306.80` | 3,760,000.00 USD | 3,760,000.00 USD | 28,610.00 USD | 35,400.00 USD | 5,490.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `307.20` | 3,820,000.00 USD | 3,820,000.00 USD | 11,550.00 USD | 27,080.00 USD | 18,140.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `307.20` | 3,820,000.00 USD | 3,820,000.00 USD | 11,550.00 USD | 27,080.00 USD | 18,140.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `307.60` | 3,870,000.00 USD | 3,870,000.00 USD | 15,000.00 USD | 30,960.00 USD | 3,670.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `307.60` | 3,870,000.00 USD | 3,870,000.00 USD | 15,000.00 USD | 30,960.00 USD | 3,670.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `308.00` | 3,940,000.00 USD | 3,940,000.00 USD | 30,270.00 USD | 20,480.00 USD | 22,690.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `308.00` | 3,940,000.00 USD | 3,940,000.00 USD | 30,270.00 USD | 20,830.00 USD | 22,690.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `308.40` | 3,950,000.00 USD | 3,950,000.00 USD | 5,350.00 USD | 3,460.00 USD | 4,260.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `308.40` | 3,950,000.00 USD | 3,950,000.00 USD | 5,350.00 USD | 3,460.00 USD | 4,260.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `308.80` | 3,970,000.00 USD | 3,970,000.00 USD | 9,910.00 USD | 280.94 USD | 3,480.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `308.80` | 3,970,000.00 USD | 3,970,000.00 USD | 9,910.00 USD | 280.94 USD | 3,480.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `309.20` | 4,000,000.00 USD | 4,000,000.00 USD | 9,930.00 USD | 15,050.00 USD | 3,020.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `309.20` | 4,000,000.00 USD | 4,000,000.00 USD | 9,930.00 USD | 15,050.00 USD | 3,020.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `309.60` | 4,030,000.00 USD | 4,030,000.00 USD | 10,210.00 USD | 14,260.00 USD | 8,230.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `309.60` | 4,030,000.00 USD | 4,030,000.00 USD | 10,210.00 USD | 14,260.00 USD | 8,230.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `310.00` | 4,040,000.00 USD | 4,040,000.00 USD | 8,210.00 USD | 4,640.00 USD | 978.51 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `310.00` | 4,040,000.00 USD | 4,040,000.00 USD | 8,210.00 USD | 4,640.00 USD | 978.51 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `310.40` | 4,050,000.00 USD | 4,050,000.00 USD | 376.38 USD | 5,370.00 USD | 3.86 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `310.40` | 4,050,000.00 USD | 4,050,000.00 USD | 376.38 USD | 5,370.00 USD | 3.86 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `310.50` | 517.91 USD | 4,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `310.80` | 4,050,000.00 USD | 4,050,000.00 USD | 0.00 USD | 48.50 USD | 1.49 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `310.80` | 4,050,000.00 USD | 4,050,000.00 USD | 0.00 USD | 48.50 USD | 1.49 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `311.20` | 4,060,000.00 USD | 4,060,000.00 USD | 431.32 USD | 2,050.00 USD | 12,640.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `311.20` | 4,060,000.00 USD | 4,060,000.00 USD | 431.32 USD | 2,050.00 USD | 12,640.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `311.60` | 4,110,000.00 USD | 4,110,000.00 USD | 27,810.00 USD | 6,590.00 USD | 9,750.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `311.60` | 4,110,000.00 USD | 4,110,000.00 USD | 27,810.00 USD | 6,590.00 USD | 9,750.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `312.00` | 4,110,000.00 USD | 4,110,000.00 USD | 244.00 USD | 0.00 USD | 4.48 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `312.00` | 4,110,000.00 USD | 4,110,000.00 USD | 244.00 USD | 0.00 USD | 4.48 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `312.40` | 4,140,000.00 USD | 4,140,000.00 USD | 13,950.00 USD | 7,480.00 USD | 8,710.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `312.40` | 4,140,000.00 USD | 4,140,000.00 USD | 13,950.00 USD | 7,480.00 USD | 8,710.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `312.80` | 4,150,000.00 USD | 4,150,000.00 USD | 11,710.00 USD | 23.27 USD | 23.91 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `312.80` | 4,150,000.00 USD | 4,150,000.00 USD | 11,710.00 USD | 23.27 USD | 23.91 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `313.20` | 4,170,000.00 USD | 4,170,000.00 USD | 5,080.00 USD | 3,820.00 USD | 8,970.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `313.20` | 4,170,000.00 USD | 4,170,000.00 USD | 5,080.00 USD | 3,820.00 USD | 8,970.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `313.60` | 4,200,000.00 USD | 4,200,000.00 USD | 11,920.00 USD | 7,620.00 USD | 10,050.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `313.60` | 4,200,000.00 USD | 4,200,000.00 USD | 11,920.00 USD | 7,620.00 USD | 10,050.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `314.00` | 4,210,000.00 USD | 4,210,000.00 USD | 4,410.00 USD | 6,040.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `314.00` | 4,210,000.00 USD | 4,210,000.00 USD | 4,410.00 USD | 6,040.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `314.40` | 4,230,000.00 USD | 4,230,000.00 USD | 4,320.00 USD | 10,960.00 USD | 7,320.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `314.40` | 4,230,000.00 USD | 4,230,000.00 USD | 4,320.00 USD | 10,960.00 USD | 7,320.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `314.80` | 4,240,000.00 USD | 4,240,000.00 USD | 479.45 USD | 0.00 USD | 9,250.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `314.80` | 4,240,000.00 USD | 4,240,000.00 USD | 479.45 USD | 0.00 USD | 9,250.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `315.20` | 4,250,000.00 USD | 4,250,000.00 USD | 3,740.00 USD | 0.00 USD | 5,900.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `315.20` | 4,250,000.00 USD | 4,250,000.00 USD | 3,740.00 USD | 0.00 USD | 5,900.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `315.60` | 4,270,000.00 USD | 4,270,000.00 USD | 0.00 USD | 6,310.00 USD | 19,390.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `315.60` | 4,280,000.00 USD | 4,280,000.00 USD | 0.00 USD | 6,310.00 USD | 19,390.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `316.00` | 4,310,000.00 USD | 4,310,000.00 USD | 13,020.00 USD | 7,180.00 USD | 10,740.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `316.00` | 4,310,000.00 USD | 4,310,000.00 USD | 13,020.00 USD | 7,180.00 USD | 10,740.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `316.40` | 4,320,000.00 USD | 4,320,000.00 USD | 12,950.00 USD | 5,010.00 USD | 1,100.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `316.40` | 4,330,000.00 USD | 4,330,000.00 USD | 12,950.00 USD | 5,010.00 USD | 1,100.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `316.80` | 4,350,000.00 USD | 4,350,000.00 USD | 5,360.00 USD | 8,870.00 USD | 11,440.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `316.80` | 4,350,000.00 USD | 4,350,000.00 USD | 5,360.00 USD | 8,870.00 USD | 11,440.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `317.20` | 4,360,000.00 USD | 4,360,000.00 USD | 3,920.00 USD | 4,340.00 USD | 2,630.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `317.20` | 4,360,000.00 USD | 4,360,000.00 USD | 3,920.00 USD | 4,340.00 USD | 2,630.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `317.60` | 4,390,000.00 USD | 4,390,000.00 USD | 6,150.00 USD | 12,380.00 USD | 8,480.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `317.60` | 4,390,000.00 USD | 4,390,000.00 USD | 6,150.00 USD | 12,380.00 USD | 8,480.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `318.00` | 4,410,000.00 USD | 4,410,000.00 USD | 2,290.00 USD | 12,210.00 USD | 9,880.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `318.00` | 4,410,000.00 USD | 4,410,000.00 USD | 2,290.00 USD | 12,210.00 USD | 9,880.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `318.40` | 4,420,000.00 USD | 4,420,000.00 USD | 234.70 USD | 5,370.00 USD | 820.17 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `318.40` | 4,420,000.00 USD | 4,420,000.00 USD | 234.70 USD | 5,370.00 USD | 820.17 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `318.50` | 114.34 USD | 4,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `318.80` | 4,450,000.00 USD | 4,450,000.00 USD | 9,170.00 USD | 10,850.00 USD | 6,170.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `318.80` | 4,450,000.00 USD | 4,450,000.00 USD | 9,170.00 USD | 10,850.00 USD | 6,170.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `319.20` | 4,460,000.00 USD | 4,460,000.00 USD | 7,830.00 USD | 11,350.00 USD | 488.47 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `319.20` | 4,470,000.00 USD | 4,470,000.00 USD | 7,830.00 USD | 11,350.00 USD | 488.47 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `319.50` | 6,600.00 USD | 11,440.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `319.60` | 4,470,000.00 USD | 4,470,000.00 USD | 8,460.00 USD | 1,760.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `319.60` | 4,480,000.00 USD | 4,480,000.00 USD | 8,460.00 USD | 1,760.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `320.00` | 4,480,000.00 USD | 4,480,000.00 USD | 155.00 USD | 2,460.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `320.00` | 4,480,000.00 USD | 4,480,000.00 USD | 155.00 USD | 2,460.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `320.40` | 4,490,000.00 USD | 4,490,000.00 USD | 8,130.00 USD | 0.00 USD | 2,590.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `320.40` | 4,490,000.00 USD | 4,490,000.00 USD | 8,130.00 USD | 0.00 USD | 2,590.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `320.50` | 1,110.00 USD | 12,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `321.20` | 4,490,000.00 USD | 4,490,000.00 USD | 150.60 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `321.20` | 4,490,000.00 USD | 4,490,000.00 USD | 150.60 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `321.60` | 4,510,000.00 USD | 4,510,000.00 USD | 8,670.00 USD | 0.00 USD | 16,170.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `321.60` | 4,510,000.00 USD | 4,510,000.00 USD | 8,670.00 USD | 0.00 USD | 16,170.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `322.00` | 4,520,000.00 USD | 4,520,000.00 USD | 0.00 USD | 0.00 USD | 9,600.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `322.00` | 4,520,000.00 USD | 4,520,000.00 USD | 0.00 USD | 0.00 USD | 9,600.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `322.40` | 4,530,000.00 USD | 4,530,000.00 USD | 0.00 USD | 0.00 USD | 6,540.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `322.40` | 4,530,000.00 USD | 4,530,000.00 USD | 0.00 USD | 0.00 USD | 6,540.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `330.50` | 276.63 USD | 12,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `341.50` | 1,370.00 USD | 14,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `351.50` | 38,660.00 USD | 52,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `358.50` | 1,010.00 USD | 53,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `368.50` | 445.52 USD | 54,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `395.50` | 3,430.00 USD | 57,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `427.50` | 9,480.00 USD | 67,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `432.50` | 8,810.00 USD | 76,030.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `459.50` | 46,250.00 USD | 122,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `498.50` | 1,040.00 USD | 123,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `533.50` | 177.66 USD | 123,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `560.50` | 842.43 USD | 124,350.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `565.50` | 1,450.00 USD | 125,800.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `95.50` | 449,690.00 USD | 0.00 USD | 920.05 USD | `-66.89%` | `9,634,000,000.00` |
| `Live` | `Long` | `101.50` | 448,770.00 USD | 0.00 USD | 6,240.00 USD | `-64.81%` | `61,439,000,000.00` |
| `Live` | `Long` | `102.50` | 442,540.00 USD | 0.00 USD | 4,080.00 USD | `-64.47%` | `39,797,000,000.00` |
| `Live` | `Long` | `109.50` | 438,460.00 USD | 0.00 USD | 48,470.00 USD | `-62.04%` | `442,647,000,000.00` |
| `Live` | `Long` | `115.50` | 389,990.00 USD | 0.00 USD | 169.78 USD | `-59.96%` | `1,470,000,000.00` |
| `Live` | `Long` | `118.50` | 389,820.00 USD | 0.00 USD | 212.35 USD | `-58.92%` | `1,792,000,000.00` |
| `Live` | `Long` | `122.50` | 389,610.00 USD | 0.00 USD | 124.46 USD | `-57.53%` | `1,016,000,000.00` |
| `Live` | `Long` | `126.50` | 389,480.00 USD | 0.00 USD | 658.18 USD | `-56.15%` | `5,203,000,000.00` |
| `Live` | `Long` | `137.50` | 388,820.00 USD | 0.00 USD | 6,880.00 USD | `-52.33%` | `50,000,000,000.00` |
| `Live` | `Long` | `142.50` | 381,950.00 USD | 0.00 USD | 2,140.00 USD | `-50.60%` | `15,000,000,000.00` |
| `Live` | `Long` | `145.50` | 379,810.00 USD | 0.00 USD | 2,070.00 USD | `-49.56%` | `14,200,000,000.00` |
| `Live` | `Long` | `147.50` | 377,740.00 USD | 0.00 USD | 895.47 USD | `-48.87%` | `6,071,000,000.00` |
| `Live` | `Long` | `148.50` | 376,850.00 USD | 0.00 USD | 1,270.00 USD | `-48.52%` | `8,528,000,000.00` |
| `Live` | `Long` | `149.50` | 375,580.00 USD | 0.00 USD | 2,370.00 USD | `-48.17%` | `15,823,000,000.00` |
| `Live` | `Long` | `150.50` | 373,220.00 USD | 0.00 USD | 586.50 USD | `-47.83%` | `3,897,000,000.00` |
| `Live` | `Long` | `152.50` | 372,630.00 USD | 0.00 USD | 303.78 USD | `-47.13%` | `1,992,000,000.00` |
| `Live` | `Long` | `161.50` | 372,330.00 USD | 0.00 USD | 656.82 USD | `-44.01%` | `4,067,000,000.00` |
| `Live` | `Long` | `162.50` | 371,670.00 USD | 0.00 USD | 325.00 USD | `-43.67%` | `2,000,000,000.00` |
| `Live` | `Long` | `167.50` | 371,340.00 USD | 0.00 USD | 285.75 USD | `-41.94%` | `1,706,000,000.00` |
| `Live` | `Long` | `169.50` | 371,060.00 USD | 0.00 USD | 5,340.00 USD | `-41.24%` | `31,500,000,000.00` |
| `Live` | `Long` | `170.50` | 365,720.00 USD | 0.00 USD | 426.25 USD | `-40.90%` | `2,500,000,000.00` |
| `Live` | `Long` | `174.50` | 365,290.00 USD | 0.00 USD | 169.96 USD | `-39.51%` | `974,000,000.00` |
| `Live` | `Long` | `175.50` | 365,120.00 USD | 0.00 USD | 516.67 USD | `-39.16%` | `2,944,000,000.00` |
| `Live` | `Long` | `176.50` | 364,610.00 USD | 0.00 USD | 373.83 USD | `-38.82%` | `2,118,000,000.00` |
| `Live` | `Long` | `178.50` | 364,230.00 USD | 0.00 USD | 535.50 USD | `-38.12%` | `3,000,000,000.00` |
| `Live` | `Long` | `181.50` | 363,700.00 USD | 0.00 USD | 804.04 USD | `-37.08%` | `4,430,000,000.00` |
| `Live` | `Long` | `183.50` | 362,890.00 USD | 0.00 USD | 191.57 USD | `-36.39%` | `1,044,000,000.00` |
| `Live` | `Long` | `184.50` | 362,700.00 USD | 0.00 USD | 616.05 USD | `-36.04%` | `3,339,000,000.00` |
| `Live` | `Long` | `188.50` | 362,090.00 USD | 0.00 USD | 418.28 USD | `-34.66%` | `2,219,000,000.00` |
| `Live` | `Long` | `191.50` | 361,670.00 USD | 0.00 USD | 858.49 USD | `-33.62%` | `4,483,000,000.00` |
| `Live` | `Long` | `192.50` | 360,810.00 USD | 0.00 USD | 1,490.00 USD | `-33.27%` | `7,715,000,000.00` |
| `Live` | `Long` | `195.50` | 359,320.00 USD | 0.00 USD | 370.47 USD | `-32.23%` | `1,895,000,000.00` |
| `Live` | `Long` | `198.50` | 358,950.00 USD | 0.00 USD | 1,610.00 USD | `-31.19%` | `8,129,000,000.00` |
| `Live` | `Long` | `199.50` | 357,340.00 USD | 0.00 USD | 765.08 USD | `-30.84%` | `3,835,000,000.00` |
| `Live` | `Long` | `200.50` | 356,570.00 USD | 0.00 USD | 293.13 USD | `-30.50%` | `1,462,000,000.00` |
| `Live` | `Long` | `202.50` | 356,280.00 USD | 0.00 USD | 420.39 USD | `-29.80%` | `2,076,000,000.00` |
| `Live` | `Long` | `204.50` | 355,860.00 USD | 0.00 USD | 39,880.00 USD | `-29.11%` | `195,028,000,000.00` |
| `Live` | `Long` | `205.50` | 315,980.00 USD | 0.00 USD | 191.53 USD | `-28.76%` | `932,000,000.00` |
| `Live` | `Long` | `210.50` | 315,790.00 USD | 0.00 USD | 42,310.00 USD | `-27.03%` | `201,017,000,000.00` |
| `Live` | `Long` | `213.50` | 273,470.00 USD | 0.00 USD | 3,800.00 USD | `-25.99%` | `17,817,000,000.00` |
| `Live` | `Long` | `215.50` | 269,670.00 USD | 0.00 USD | 239.85 USD | `-25.30%` | `1,113,000,000.00` |
| `Live` | `Long` | `219.50` | 269,430.00 USD | 0.00 USD | 5,690.00 USD | `-23.91%` | `25,931,000,000.00` |
| `Live` | `Long` | `220.50` | 263,740.00 USD | 0.00 USD | 1,010.00 USD | `-23.56%` | `4,592,000,000.00` |
| `Live` | `Long` | `223.50` | 262,720.00 USD | 0.00 USD | 32,860.00 USD | `-22.52%` | `147,023,000,000.00` |
| `Live` | `Long` | `224.50` | 229,860.00 USD | 0.00 USD | 1,630.00 USD | `-22.18%` | `7,243,000,000.00` |
| `Live` | `Long` | `226.50` | 228,240.00 USD | 0.00 USD | 1,240.00 USD | `-21.48%` | `5,455,000,000.00` |
| `Live` | `Long` | `227.50` | 227,000.00 USD | 0.00 USD | 174.49 USD | `-21.14%` | `767,000,000.00` |
| `Live` | `Long` | `228.50` | 226,830.00 USD | 0.00 USD | 642.77 USD | `-20.79%` | `2,813,000,000.00` |
| `Live` | `Long` | `229.50` | 226,190.00 USD | 0.00 USD | 1,190.00 USD | `-20.44%` | `5,171,000,000.00` |
| `Live` | `Long` | `230.50` | 225,000.00 USD | 0.00 USD | 8,040.00 USD | `-20.10%` | `34,884,000,000.00` |
| `Live` | `Long` | `231.50` | 216,960.00 USD | 0.00 USD | 295.86 USD | `-19.75%` | `1,278,000,000.00` |
| `Live` | `Long` | `232.50` | 216,660.00 USD | 0.00 USD | 1,890.00 USD | `-19.40%` | `8,122,000,000.00` |
| `Live` | `Long` | `234.50` | 214,770.00 USD | 0.00 USD | 217.85 USD | `-18.71%` | `929,000,000.00` |
| `Live` | `Long` | `239.50` | 214,560.00 USD | 0.00 USD | 1,030.00 USD | `-16.98%` | `4,281,000,000.00` |
| `Live` | `Long` | `241.50` | 213,530.00 USD | 0.00 USD | 367.32 USD | `-16.28%` | `1,521,000,000.00` |
| `Live` | `Long` | `242.50` | 213,160.00 USD | 0.00 USD | 5,660.00 USD | `-15.94%` | `23,352,000,000.00` |
| `Live` | `Long` | `243.50` | 207,500.00 USD | 0.00 USD | 1,200.00 USD | `-15.59%` | `4,937,000,000.00` |
| `Live` | `Long` | `244.50` | 206,300.00 USD | 0.00 USD | 4,220.00 USD | `-15.24%` | `17,277,000,000.00` |
| `Live` | `Long` | `245.50` | 202,070.00 USD | 0.00 USD | 1,030.00 USD | `-14.90%` | `4,182,000,000.00` |
| `Live` | `Long` | `247.50` | 201,050.00 USD | 0.00 USD | 12,340.00 USD | `-14.20%` | `49,849,000,000.00` |
| `Live` | `Long` | `250.50` | 188,710.00 USD | 0.00 USD | 1,330.00 USD | `-13.16%` | `5,292,000,000.00` |
| `Live` | `Long` | `251.50` | 187,380.00 USD | 0.00 USD | 268.35 USD | `-12.82%` | `1,067,000,000.00` |
| `Live` | `Long` | `252.50` | 187,120.00 USD | 0.00 USD | 1,030.00 USD | `-12.47%` | `4,088,000,000.00` |
| `Live` | `Long` | `254.50` | 186,080.00 USD | 0.00 USD | 11,650.00 USD | `-11.78%` | `45,758,000,000.00` |
| `Live` | `Long` | `255.50` | 174,440.00 USD | 0.00 USD | 3,660.00 USD | `-11.43%` | `14,337,000,000.00` |
| `Live` | `Long` | `256.50` | 170,780.00 USD | 0.00 USD | 2,480.00 USD | `-11.08%` | `9,686,000,000.00` |
| `Live` | `Long` | `257.50` | 168,290.00 USD | 0.00 USD | 366.42 USD | `-10.74%` | `1,423,000,000.00` |
| `Live` | `Long` | `258.50` | 167,920.00 USD | 0.00 USD | 176.56 USD | `-10.39%` | `683,000,000.00` |
| `Live` | `Long` | `260.50` | 167,750.00 USD | 0.00 USD | 3,860.00 USD | `-9.70%` | `14,816,000,000.00` |
| `Live` | `Long` | `262.50` | 163,890.00 USD | 0.00 USD | 1,970.00 USD | `-9.00%` | `7,495,000,000.00` |
| `Live` | `Long` | `264.50` | 161,920.00 USD | 0.00 USD | 280.37 USD | `-8.31%` | `1,060,000,000.00` |
| `Live` | `Long` | `265.50` | 161,640.00 USD | 0.00 USD | 121,910.00 USD | `-7.96%` | `459,161,000,000.00` |
| `Live` | `Long` | `267.50` | 39,730.00 USD | 0.00 USD | 1,490.00 USD | `-7.27%` | `5,578,000,000.00` |
| `Live` | `Long` | `268.50` | 38,240.00 USD | 0.00 USD | 7,020.00 USD | `-6.92%` | `26,129,000,000.00` |
| `Live` | `Long` | `269.50` | 31,230.00 USD | 0.00 USD | 11,700.00 USD | `-6.58%` | `43,411,000,000.00` |
| `Live` | `Long` | `271.50` | 19,530.00 USD | 0.00 USD | 1,000.00 USD | `-5.88%` | `3,685,000,000.00` |
| `Live` | `Long` | `274.50` | 18,530.00 USD | 0.00 USD | 567.94 USD | `-4.84%` | `2,069,000,000.00` |
| `Live` | `Long` | `276.50` | 17,960.00 USD | 0.00 USD | 205.44 USD | `-4.15%` | `743,000,000.00` |
| `Live` | `Long` | `285.50` | 17,750.00 USD | 0.00 USD | 17,750.00 USD | `-1.03%` | `62,179,000,000.00` |
| `Live` | `Short` | `295.50` | 612.57 USD | 612.57 USD | 0.00 USD | `+2.44%` | `2,073,000,000.00` |
| `Live` | `Short` | `299.50` | 1,830.00 USD | 1,220.00 USD | 0.00 USD | `+3.82%` | `4,068,000,000.00` |
| `Live` | `Short` | `301.50` | 4,210.00 USD | 2,380.00 USD | 0.00 USD | `+4.52%` | `7,885,000,000.00` |
| `Live` | `Short` | `310.50` | 4,730.00 USD | 517.91 USD | 0.00 USD | `+7.64%` | `1,668,000,000.00` |
| `Live` | `Short` | `318.50` | 4,840.00 USD | 114.34 USD | 0.00 USD | `+10.41%` | `359,000,000.00` |
| `Live` | `Short` | `319.50` | 11,440.00 USD | 6,600.00 USD | 0.00 USD | `+10.76%` | `20,668,000,000.00` |
| `Live` | `Short` | `320.50` | 12,550.00 USD | 1,110.00 USD | 0.00 USD | `+11.10%` | `3,452,000,000.00` |
| `Live` | `Short` | `330.50` | 12,830.00 USD | 276.63 USD | 0.00 USD | `+14.57%` | `837,000,000.00` |
| `Live` | `Short` | `341.50` | 14,190.00 USD | 1,370.00 USD | 0.00 USD | `+18.38%` | `4,000,000,000.00` |
| `Live` | `Short` | `351.50` | 52,860.00 USD | 38,660.00 USD | 0.00 USD | `+21.85%` | `110,000,000,000.00` |
| `Live` | `Short` | `358.50` | 53,870.00 USD | 1,010.00 USD | 0.00 USD | `+24.28%` | `2,812,000,000.00` |
| `Live` | `Short` | `368.50` | 54,310.00 USD | 445.52 USD | 0.00 USD | `+27.74%` | `1,209,000,000.00` |
| `Live` | `Short` | `395.50` | 57,740.00 USD | 3,430.00 USD | 0.00 USD | `+37.10%` | `8,681,000,000.00` |
| `Live` | `Short` | `427.50` | 67,220.00 USD | 9,480.00 USD | 0.00 USD | `+48.20%` | `22,172,000,000.00` |
| `Live` | `Short` | `432.50` | 76,030.00 USD | 8,810.00 USD | 0.00 USD | `+49.93%` | `20,366,000,000.00` |
| `Live` | `Short` | `459.50` | 122,290.00 USD | 46,250.00 USD | 0.00 USD | `+59.29%` | `100,662,000,000.00` |
| `Live` | `Short` | `498.50` | 123,330.00 USD | 1,040.00 USD | 0.00 USD | `+72.81%` | `2,093,000,000.00` |
| `Live` | `Short` | `533.50` | 123,510.00 USD | 177.66 USD | 0.00 USD | `+84.94%` | `333,000,000.00` |
| `Live` | `Short` | `560.50` | 124,350.00 USD | 842.43 USD | 0.00 USD | `+94.30%` | `1,503,000,000.00` |
| `Live` | `Short` | `565.50` | 125,800.00 USD | 1,450.00 USD | 0.00 USD | `+96.03%` | `2,572,000,000.00` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `143.50` | 209,850.00 USD | 0.00 USD | 210.94 USD | `-50.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `145.50` | 209,640.00 USD | 0.00 USD | 2,070.00 USD | `-49.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `178.50` | 207,570.00 USD | 0.00 USD | 2,530.00 USD | `-38.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `184.50` | 205,040.00 USD | 0.00 USD | 490.59 USD | `-36.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `196.50` | 204,550.00 USD | 0.00 USD | 482.01 USD | `-31.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `200.50` | 204,070.00 USD | 0.00 USD | 189.07 USD | `-30.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `208.50` | 203,880.00 USD | 0.00 USD | 441.60 USD | `-27.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `210.50` | 203,440.00 USD | 0.00 USD | 703.49 USD | `-27.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `221.50` | 202,730.00 USD | 0.00 USD | 638.36 USD | `-23.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `224.50` | 202,100.00 USD | 0.00 USD | 740.85 USD | `-22.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `228.50` | 201,350.00 USD | 0.00 USD | 1,050.00 USD | `-20.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `233.50` | 200,300.00 USD | 0.00 USD | 389.48 USD | `-19.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `237.50` | 199,920.00 USD | 0.00 USD | 220.64 USD | `-17.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `238.50` | 199,690.00 USD | 0.00 USD | 429.30 USD | `-17.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `239.50` | 199,270.00 USD | 0.00 USD | 296.50 USD | `-16.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `240.50` | 198,970.00 USD | 0.00 USD | 216.45 USD | `-16.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `242.50` | 198,750.00 USD | 0.00 USD | 101.61 USD | `-15.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `244.50` | 198,650.00 USD | 0.00 USD | 366.75 USD | `-15.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `246.50` | 198,280.00 USD | 0.00 USD | 1,630.00 USD | `-14.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `249.50` | 196,660.00 USD | 0.00 USD | 2,940.00 USD | `-13.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `250.50` | 193,710.00 USD | 0.00 USD | 4,560.00 USD | `-13.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `251.50` | 189,160.00 USD | 0.00 USD | 7,080.00 USD | `-12.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `252.50` | 182,080.00 USD | 0.00 USD | 231.54 USD | `-12.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `253.50` | 181,850.00 USD | 0.00 USD | 109.26 USD | `-12.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `255.50` | 181,740.00 USD | 0.00 USD | 1,780.00 USD | `-11.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `256.50` | 179,960.00 USD | 0.00 USD | 51,300.00 USD | `-11.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `257.50` | 128,660.00 USD | 0.00 USD | 250.81 USD | `-10.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `259.50` | 128,410.00 USD | 0.00 USD | 386.14 USD | `-10.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `260.50` | 128,020.00 USD | 0.00 USD | 707.78 USD | `-9.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `262.50` | 127,310.00 USD | 0.00 USD | 857.85 USD | `-9.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `263.50` | 126,460.00 USD | 0.00 USD | 7,790.00 USD | `-8.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `264.50` | 118,660.00 USD | 0.00 USD | 122.99 USD | `-8.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `265.50` | 118,540.00 USD | 0.00 USD | 455.86 USD | `-7.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `266.50` | 118,080.00 USD | 0.00 USD | 10,490.00 USD | `-7.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `267.50` | 107,600.00 USD | 0.00 USD | 1,110.00 USD | `-7.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `268.50` | 106,490.00 USD | 0.00 USD | 877.46 USD | `-6.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `269.50` | 105,610.00 USD | 0.00 USD | 498.04 USD | `-6.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `270.50` | 105,110.00 USD | 0.00 USD | 1,180.00 USD | `-6.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `271.50` | 103,940.00 USD | 0.00 USD | 269.60 USD | `-5.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `272.50` | 103,670.00 USD | 0.00 USD | 13,500.00 USD | `-5.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `273.50` | 90,170.00 USD | 0.00 USD | 1,470.00 USD | `-5.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `274.50` | 88,700.00 USD | 0.00 USD | 336.54 USD | `-4.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `275.50` | 88,370.00 USD | 0.00 USD | 681.31 USD | `-4.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `276.50` | 87,680.00 USD | 0.00 USD | 105.35 USD | `-4.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `277.50` | 87,580.00 USD | 0.00 USD | 14,500.00 USD | `-3.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `278.50` | 73,080.00 USD | 0.00 USD | 125.88 USD | `-3.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `279.50` | 72,950.00 USD | 0.00 USD | 25,690.00 USD | `-3.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `280.50` | 47,260.00 USD | 0.00 USD | 20,810.00 USD | `-2.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `281.50` | 26,450.00 USD | 0.00 USD | 2,880.00 USD | `-2.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `282.50` | 23,570.00 USD | 0.00 USD | 290.13 USD | `-2.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `283.50` | 23,280.00 USD | 0.00 USD | 11,620.00 USD | `-1.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `284.50` | 11,660.00 USD | 0.00 USD | 3,690.00 USD | `-1.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `285.50` | 7,970.00 USD | 0.00 USD | 2,600.00 USD | `-1.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `286.50` | 5,360.00 USD | 0.00 USD | 5,080.00 USD | `-0.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `287.50` | 280.02 USD | 0.00 USD | 280.02 USD | `-0.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `288.50` | 120.59 USD | 120.59 USD | 0.00 USD | `+0.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `289.50` | 274.03 USD | 153.44 USD | 0.00 USD | `+0.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `290.50` | 1,590.00 USD | 1,320.00 USD | 0.00 USD | `+0.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `291.50` | 1,710.00 USD | 115.73 USD | 0.00 USD | `+1.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `292.50` | 2,120.00 USD | 409.21 USD | 0.00 USD | `+1.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `293.50` | 20,370.00 USD | 18,250.00 USD | 0.00 USD | `+1.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `294.50` | 20,780.00 USD | 407.88 USD | 0.00 USD | `+2.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `295.50` | 25,500.00 USD | 4,730.00 USD | 0.00 USD | `+2.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `296.50` | 26,080.00 USD | 581.14 USD | 0.00 USD | `+2.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `298.50` | 26,620.00 USD | 535.51 USD | 0.00 USD | `+3.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `300.50` | 36,310.00 USD | 9,690.00 USD | 0.00 USD | `+4.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `304.50` | 47,030.00 USD | 10,730.00 USD | 0.00 USD | `+5.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `305.50` | 49,690.00 USD | 2,650.00 USD | 0.00 USD | `+5.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `306.50` | 50,740.00 USD | 1,060.00 USD | 0.00 USD | `+6.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `308.50` | 50,850.00 USD | 102.73 USD | 0.00 USD | `+6.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `309.50` | 65,340.00 USD | 14,500.00 USD | 0.00 USD | `+7.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `310.50` | 65,970.00 USD | 634.04 USD | 0.00 USD | `+7.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `312.50` | 66,290.00 USD | 317.19 USD | 0.00 USD | `+8.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `316.50` | 67,330.00 USD | 1,030.00 USD | 0.00 USD | `+9.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `318.50` | 72,980.00 USD | 5,650.00 USD | 0.00 USD | `+10.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `319.50` | 73,090.00 USD | 118.85 USD | 0.00 USD | `+10.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `320.50` | 73,630.00 USD | 534.59 USD | 0.00 USD | `+11.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `321.50` | 73,950.00 USD | 321.50 USD | 0.00 USD | `+11.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `325.50` | 138,880.00 USD | 64,920.00 USD | 0.00 USD | `+12.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `340.50` | 139,420.00 USD | 547.52 USD | 0.00 USD | `+18.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `345.50` | 139,560.00 USD | 138.20 USD | 0.00 USD | `+19.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `346.50` | 139,820.00 USD | 257.45 USD | 0.00 USD | `+20.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `348.50` | 139,990.00 USD | 174.25 USD | 0.00 USD | `+20.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `351.50` | 140,140.00 USD | 151.50 USD | 0.00 USD | `+21.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `357.50` | 141,600.00 USD | 1,450.00 USD | 0.00 USD | `+23.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `359.50` | 143,370.00 USD | 1,770.00 USD | 0.00 USD | `+24.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `361.50` | 143,700.00 USD | 326.07 USD | 0.00 USD | `+25.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `363.50` | 144,520.00 USD | 826.60 USD | 0.00 USD | `+26.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `364.50` | 148,250.00 USD | 3,730.00 USD | 0.00 USD | `+26.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `365.50` | 155,700.00 USD | 7,440.00 USD | 0.00 USD | `+26.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `369.50` | 156,380.00 USD | 682.84 USD | 0.00 USD | `+28.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `381.50` | 157,480.00 USD | 1,100.00 USD | 0.00 USD | `+32.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `396.50` | 158,160.00 USD | 683.96 USD | 0.00 USD | `+37.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `399.50` | 158,360.00 USD | 199.75 USD | 0.00 USD | `+38.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `400.50` | 161,860.00 USD | 3,500.00 USD | 0.00 USD | `+38.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `404.50` | 162,900.00 USD | 1,040.00 USD | 0.00 USD | `+40.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `405.50` | 163,280.00 USD | 376.71 USD | 0.00 USD | `+40.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `410.50` | 351,920.00 USD | 188,640.00 USD | 0.00 USD | `+42.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `415.50` | 357,820.00 USD | 5,900.00 USD | 0.00 USD | `+44.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `423.50` | 358,720.00 USD | 901.21 USD | 0.00 USD | `+46.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `425.50` | 366,530.00 USD | 7,800.00 USD | 0.00 USD | `+47.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `430.50` | 368,080.00 USD | 1,550.00 USD | 0.00 USD | `+49.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `435.50` | 369,460.00 USD | 1,380.00 USD | 0.00 USD | `+50.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `436.50` | 370,080.00 USD | 621.14 USD | 0.00 USD | `+51.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `440.50` | 373,460.00 USD | 3,380.00 USD | 0.00 USD | `+52.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `445.50` | 373,680.00 USD | 222.75 USD | 0.00 USD | `+54.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `450.50` | 379,280.00 USD | 5,590.00 USD | 0.00 USD | `+56.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `451.50` | 385,190.00 USD | 5,920.00 USD | 0.00 USD | `+56.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `460.50` | 386,320.00 USD | 1,130.00 USD | 0.00 USD | `+59.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `482.50` | 393,960.00 USD | 7,630.00 USD | 0.00 USD | `+67.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `487.50` | 492,430.00 USD | 98,470.00 USD | 0.00 USD | `+69.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `490.50` | 493,410.00 USD | 981.00 USD | 0.00 USD | `+70.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `499.50` | 493,910.00 USD | 499.50 USD | 0.00 USD | `+73.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `500.50` | 2,380,000.00 USD | 1,890,000.00 USD | 0.00 USD | `+73.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `501.50` | 2,380,000.00 USD | 1,000.00 USD | 0.00 USD | `+73.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `518.50` | 2,380,000.00 USD | 1,040.00 USD | 0.00 USD | `+79.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `522.50` | 2,380,000.00 USD | 340.67 USD | 0.00 USD | `+81.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `556.50` | 2,380,000.00 USD | 638.86 USD | 0.00 USD | `+92.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `575.50` | 2,390,000.00 USD | 2,590.00 USD | 0.00 USD | `+99.50%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `1D` | `253.20` | 8,090,000.00 USD | 0.00 USD | 8,090,000.00 USD | 9,620.00 USD | 19,920.00 USD | 6,250.00 USD |
| `7D` | `253.20` | 8,040,000.00 USD | 0.00 USD | 8,040,000.00 USD | 9,620.00 USD | 19,920.00 USD | 6,250.00 USD |
| `1D` | `253.60` | 8,050,000.00 USD | 0.00 USD | 8,050,000.00 USD | 14,720.00 USD | 13,380.00 USD | 5,280.00 USD |
| `7D` | `253.60` | 8,000,000.00 USD | 0.00 USD | 8,000,000.00 USD | 14,720.00 USD | 13,380.00 USD | 5,280.00 USD |
| `1D` | `254.00` | 8,020,000.00 USD | 0.00 USD | 8,020,000.00 USD | 144.00 USD | 5,000.00 USD | 3.86 USD |
| `7D` | `254.00` | 7,970,000.00 USD | 0.00 USD | 7,970,000.00 USD | 144.00 USD | 5,000.00 USD | 3.86 USD |
| `1D` | `254.40` | 8,010,000.00 USD | 0.00 USD | 8,010,000.00 USD | 134.35 USD | 48.50 USD | 4,090.00 USD |
| `7D` | `254.40` | 7,960,000.00 USD | 0.00 USD | 7,960,000.00 USD | 134.35 USD | 48.50 USD | 4,090.00 USD |
| `1D` | `254.80` | 8,010,000.00 USD | 0.00 USD | 8,010,000.00 USD | 14,480.00 USD | 2,050.00 USD | 18,300.00 USD |
| `7D` | `254.80` | 7,960,000.00 USD | 0.00 USD | 7,960,000.00 USD | 14,480.00 USD | 2,050.00 USD | 18,300.00 USD |
| `1D` | `255.20` | 7,980,000.00 USD | 0.00 USD | 7,980,000.00 USD | 13,640.00 USD | 6,590.00 USD | 0.34 USD |
| `7D` | `255.20` | 7,920,000.00 USD | 0.00 USD | 7,920,000.00 USD | 13,640.00 USD | 6,590.00 USD | 0.34 USD |
| `1D` | `255.60` | 7,950,000.00 USD | 0.00 USD | 7,950,000.00 USD | 13,950.00 USD | 7,480.00 USD | 8,710.00 USD |
| `7D` | `255.60` | 7,900,000.00 USD | 0.00 USD | 7,900,000.00 USD | 13,950.00 USD | 7,480.00 USD | 8,710.00 USD |
| `1D` | `256.00` | 7,920,000.00 USD | 0.00 USD | 7,920,000.00 USD | 11,710.00 USD | 23.27 USD | 27.52 USD |
| `7D` | `256.00` | 7,870,000.00 USD | 0.00 USD | 7,870,000.00 USD | 11,710.00 USD | 23.27 USD | 27.52 USD |
| `1D` | `256.40` | 7,910,000.00 USD | 0.00 USD | 7,910,000.00 USD | 12,240.00 USD | 6,710.00 USD | 8,970.00 USD |
| `7D` | `256.40` | 7,860,000.00 USD | 0.00 USD | 7,860,000.00 USD | 12,240.00 USD | 6,960.00 USD | 8,970.00 USD |
| `1D` | `256.80` | 7,890,000.00 USD | 0.00 USD | 7,890,000.00 USD | 9,170.00 USD | 10,970.00 USD | 10,050.00 USD |
| `7D` | `256.80` | 7,830,000.00 USD | 0.00 USD | 7,830,000.00 USD | 9,170.00 USD | 11,170.00 USD | 10,050.00 USD |
| `1D` | `257.20` | 7,850,000.00 USD | 0.00 USD | 7,850,000.00 USD | 4,320.00 USD | 10,960.00 USD | 7,320.00 USD |
| `7D` | `257.20` | 7,800,000.00 USD | 0.00 USD | 7,800,000.00 USD | 4,320.00 USD | 10,960.00 USD | 7,320.00 USD |
| `1D` | `257.60` | 7,830,000.00 USD | 0.00 USD | 7,830,000.00 USD | 479.45 USD | 0.00 USD | 9,250.00 USD |
| `7D` | `257.60` | 7,780,000.00 USD | 0.00 USD | 7,780,000.00 USD | 479.45 USD | 0.00 USD | 9,250.00 USD |
| `1D` | `258.00` | 7,820,000.00 USD | 0.00 USD | 7,820,000.00 USD | 3,740.00 USD | 991.50 USD | 20,060.00 USD |
| `7D` | `258.00` | 7,770,000.00 USD | 0.00 USD | 7,770,000.00 USD | 3,740.00 USD | 991.50 USD | 20,060.00 USD |
| `1D` | `258.40` | 7,800,000.00 USD | 0.00 USD | 7,800,000.00 USD | 1,470.00 USD | 8,380.00 USD | 5,270.00 USD |
| `7D` | `258.40` | 7,740,000.00 USD | 0.00 USD | 7,740,000.00 USD | 8,100.00 USD | 8,380.00 USD | 5,270.00 USD |
| `1D` | `258.80` | 7,780,000.00 USD | 0.00 USD | 7,780,000.00 USD | 17,870.00 USD | 5,620.00 USD | 11,820.00 USD |
| `7D` | `258.80` | 7,720,000.00 USD | 0.00 USD | 7,720,000.00 USD | 17,870.00 USD | 10,540.00 USD | 11,820.00 USD |
| `1D` | `259.20` | 7,750,000.00 USD | 0.00 USD | 7,750,000.00 USD | 5,410.00 USD | 9,350.00 USD | 11,440.00 USD |
| `7D` | `259.20` | 7,680,000.00 USD | 0.00 USD | 7,680,000.00 USD | 5,410.00 USD | 9,350.00 USD | 11,440.00 USD |
| `1D` | `259.60` | 7,720,000.00 USD | 0.00 USD | 7,720,000.00 USD | 4,840.00 USD | 4,550.00 USD | 2,640.00 USD |
| `7D` | `259.60` | 7,660,000.00 USD | 0.00 USD | 7,660,000.00 USD | 4,840.00 USD | 4,550.00 USD | 2,640.00 USD |
| `1D` | `260.00` | 7,710,000.00 USD | 0.00 USD | 7,710,000.00 USD | 7,850.00 USD | 17,100.00 USD | 18,370.00 USD |
| `7D` | `260.00` | 7,640,000.00 USD | 0.00 USD | 7,640,000.00 USD | 7,850.00 USD | 17,100.00 USD | 18,370.00 USD |
| `1D` | `260.40` | 7,670,000.00 USD | 0.00 USD | 7,670,000.00 USD | 2,680.00 USD | 10,080.00 USD | 825.30 USD |
| `7D` | `260.40` | 7,600,000.00 USD | 0.00 USD | 7,600,000.00 USD | 2,680.00 USD | 10,080.00 USD | 825.30 USD |
| `1D` | `260.80` | 7,650,000.00 USD | 0.00 USD | 7,650,000.00 USD | 9,630.00 USD | 14,540.00 USD | 13,930.00 USD |
| `7D` | `260.80` | 7,590,000.00 USD | 0.00 USD | 7,590,000.00 USD | 9,630.00 USD | 14,540.00 USD | 6,170.00 USD |
| `1D` | `261.20` | 7,610,000.00 USD | 0.00 USD | 7,610,000.00 USD | 7,970.00 USD | 11,470.00 USD | 503.44 USD |
| `7D` | `261.20` | 7,560,000.00 USD | 0.00 USD | 7,560,000.00 USD | 7,970.00 USD | 11,470.00 USD | 503.44 USD |
| `1D` | `261.60` | 7,590,000.00 USD | 0.00 USD | 7,590,000.00 USD | 8,930.00 USD | 5,020.00 USD | 2.10 USD |
| `7D` | `261.60` | 7,540,000.00 USD | 0.00 USD | 7,540,000.00 USD | 8,930.00 USD | 5,020.00 USD | 2.10 USD |
| `1D` | `262.00` | 7,580,000.00 USD | 0.00 USD | 7,580,000.00 USD | 367.62 USD | 213.04 USD | 2,590.00 USD |
| `7D` | `262.00` | 7,520,000.00 USD | 0.00 USD | 7,520,000.00 USD | 367.62 USD | 213.04 USD | 2,590.00 USD |
| `1D` | `262.40` | 7,580,000.00 USD | 0.00 USD | 7,580,000.00 USD | 8,640.00 USD | 626.24 USD | 0.00 USD |
| `7D` | `262.40` | 7,520,000.00 USD | 0.00 USD | 7,520,000.00 USD | 8,640.00 USD | 626.24 USD | 0.00 USD |
| `1D` | `262.80` | 7,570,000.00 USD | 0.00 USD | 7,570,000.00 USD | 150.60 USD | 1,190.00 USD | 12.23 USD |
| `7D` | `262.80` | 7,510,000.00 USD | 0.00 USD | 7,510,000.00 USD | 150.60 USD | 1,190.00 USD | 12.23 USD |
| `1D` | `263.20` | 7,570,000.00 USD | 0.00 USD | 7,570,000.00 USD | 8,670.00 USD | 571.81 USD | 16,170.00 USD |
| `7D` | `263.20` | 7,510,000.00 USD | 0.00 USD | 7,510,000.00 USD | 8,670.00 USD | 571.81 USD | 16,170.00 USD |
| `1D` | `263.60` | 7,540,000.00 USD | 0.00 USD | 7,540,000.00 USD | 630.84 USD | 939.44 USD | 16,150.00 USD |
| `7D` | `263.60` | 7,480,000.00 USD | 0.00 USD | 7,480,000.00 USD | 630.84 USD | 939.44 USD | 16,150.00 USD |
| `1D` | `264.00` | 7,520,000.00 USD | 0.00 USD | 7,520,000.00 USD | 1,210.00 USD | 726.29 USD | 6.19 USD |
| `7D` | `264.00` | 7,470,000.00 USD | 0.00 USD | 7,470,000.00 USD | 1,210.00 USD | 726.29 USD | 6.19 USD |
| `1D` | `264.40` | 7,520,000.00 USD | 0.00 USD | 7,520,000.00 USD | 1,660.00 USD | 724.53 USD | 9.17 USD |
| `7D` | `264.40` | 7,460,000.00 USD | 0.00 USD | 7,460,000.00 USD | 1,660.00 USD | 724.53 USD | 9.17 USD |
| `1D` | `264.80` | 7,520,000.00 USD | 0.00 USD | 7,520,000.00 USD | 28,700.00 USD | 957.20 USD | 52,280.00 USD |
| `7D` | `264.80` | 7,460,000.00 USD | 0.00 USD | 7,460,000.00 USD | 28,700.00 USD | 957.20 USD | 52,290.00 USD |
| `1D` | `265.20` | 7,440,000.00 USD | 0.00 USD | 7,440,000.00 USD | 20,770.00 USD | 8,760.00 USD | 70.26 USD |
| `7D` | `265.20` | 7,380,000.00 USD | 0.00 USD | 7,380,000.00 USD | 20,770.00 USD | 8,760.00 USD | 70.26 USD |
| `1D` | `265.60` | 7,410,000.00 USD | 0.00 USD | 7,410,000.00 USD | 16,150.00 USD | 23,430.00 USD | 67,100.00 USD |
| `7D` | `265.60` | 7,350,000.00 USD | 0.00 USD | 7,350,000.00 USD | 16,150.00 USD | 23,430.00 USD | 67,100.00 USD |
| `1D` | `266.00` | 7,300,000.00 USD | 0.00 USD | 7,300,000.00 USD | 8,550.00 USD | 204.92 USD | 14.54 USD |
| `7D` | `266.00` | 7,240,000.00 USD | 0.00 USD | 7,240,000.00 USD | 8,550.00 USD | 862.64 USD | 14.54 USD |
| `1D` | `266.40` | 7,290,000.00 USD | 0.00 USD | 7,290,000.00 USD | 37,680.00 USD | 287.83 USD | 5,010.00 USD |
| `7D` | `266.40` | 7,230,000.00 USD | 0.00 USD | 7,230,000.00 USD | 37,680.00 USD | 287.83 USD | 5,010.00 USD |
| `1D` | `266.80` | 7,250,000.00 USD | 0.00 USD | 7,250,000.00 USD | 23,390.00 USD | 3,250.00 USD | 8,520.00 USD |
| `7D` | `266.80` | 7,190,000.00 USD | 0.00 USD | 7,190,000.00 USD | 23,390.00 USD | 3,250.00 USD | 8,520.00 USD |
| `1D` | `267.20` | 7,210,000.00 USD | 0.00 USD | 7,210,000.00 USD | 16,540.00 USD | 6,600.00 USD | 5,300.00 USD |
| `7D` | `267.20` | 7,160,000.00 USD | 0.00 USD | 7,160,000.00 USD | 16,540.00 USD | 6,600.00 USD | 5,300.00 USD |
| `1D` | `267.60` | 7,190,000.00 USD | 0.00 USD | 7,190,000.00 USD | 30,700.00 USD | 70,890.00 USD | 9,570.00 USD |
| `7D` | `267.60` | 7,130,000.00 USD | 0.00 USD | 7,130,000.00 USD | 30,700.00 USD | 70,890.00 USD | 9,570.00 USD |
| `1D` | `268.00` | 7,070,000.00 USD | 0.00 USD | 7,070,000.00 USD | 104,910.00 USD | 112,850.00 USD | 35,850.00 USD |
| `7D` | `268.00` | 7,020,000.00 USD | 0.00 USD | 7,020,000.00 USD | 104,910.00 USD | 112,850.00 USD | 35,850.00 USD |
| `1D` | `268.40` | 6,820,000.00 USD | 0.00 USD | 6,820,000.00 USD | 57,930.00 USD | 99,140.00 USD | 32,080.00 USD |
| `7D` | `268.40` | 6,760,000.00 USD | 0.00 USD | 6,760,000.00 USD | 57,930.00 USD | 99,140.00 USD | 32,080.00 USD |
| `1D` | `268.80` | 6,630,000.00 USD | 0.00 USD | 6,630,000.00 USD | 100,660.00 USD | 58,170.00 USD | 56,650.00 USD |
| `7D` | `268.80` | 6,570,000.00 USD | 0.00 USD | 6,570,000.00 USD | 100,660.00 USD | 58,170.00 USD | 56,650.00 USD |
| `1D` | `269.20` | 6,420,000.00 USD | 0.00 USD | 6,420,000.00 USD | 21,700.00 USD | 16,130.00 USD | 12,930.00 USD |
| `7D` | `269.20` | 6,360,000.00 USD | 0.00 USD | 6,360,000.00 USD | 21,700.00 USD | 16,130.00 USD | 12,930.00 USD |
| `1D` | `269.60` | 6,370,000.00 USD | 0.00 USD | 6,370,000.00 USD | 35,340.00 USD | 20,780.00 USD | 10,400.00 USD |
| `7D` | `269.60` | 6,310,000.00 USD | 0.00 USD | 6,310,000.00 USD | 35,340.00 USD | 20,780.00 USD | 10,410.00 USD |
| `1D` | `270.00` | 6,300,000.00 USD | 0.00 USD | 6,300,000.00 USD | 37,260.00 USD | 48,490.00 USD | 94,440.00 USD |
| `7D` | `270.00` | 6,240,000.00 USD | 0.00 USD | 6,240,000.00 USD | 37,260.00 USD | 48,490.00 USD | 94,440.00 USD |
| `1D` | `270.40` | 6,120,000.00 USD | 0.00 USD | 6,120,000.00 USD | 109,620.00 USD | 47,480.00 USD | 45,950.00 USD |
| `7D` | `270.40` | 6,060,000.00 USD | 0.00 USD | 6,060,000.00 USD | 109,620.00 USD | 47,480.00 USD | 45,950.00 USD |
| `1D` | `270.80` | 5,920,000.00 USD | 0.00 USD | 5,920,000.00 USD | 44,260.00 USD | 37,370.00 USD | 1,620.00 USD |
| `7D` | `270.80` | 5,860,000.00 USD | 0.00 USD | 5,860,000.00 USD | 44,260.00 USD | 38,250.00 USD | 1,620.00 USD |
| `1D` | `271.20` | 5,830,000.00 USD | 0.00 USD | 5,830,000.00 USD | 48,420.00 USD | 54,420.00 USD | 139,870.00 USD |
| `7D` | `271.20` | 5,770,000.00 USD | 0.00 USD | 5,770,000.00 USD | 48,420.00 USD | 54,420.00 USD | 139,870.00 USD |
| `1D` | `271.60` | 5,590,000.00 USD | 0.00 USD | 5,590,000.00 USD | 17,150.00 USD | 18,090.00 USD | 36,920.00 USD |
| `7D` | `271.60` | 5,530,000.00 USD | 0.00 USD | 5,530,000.00 USD | 17,150.00 USD | 18,090.00 USD | 36,920.00 USD |
| `1D` | `272.00` | 5,520,000.00 USD | 0.00 USD | 5,520,000.00 USD | 155,850.00 USD | 48,800.00 USD | 41,810.00 USD |
| `7D` | `272.00` | 5,460,000.00 USD | 0.00 USD | 5,460,000.00 USD | 155,850.00 USD | 48,800.00 USD | 41,810.00 USD |
| `1D` | `272.40` | 5,270,000.00 USD | 0.00 USD | 5,270,000.00 USD | 89,460.00 USD | 11,900.00 USD | 32,640.00 USD |
| `7D` | `272.40` | 5,210,000.00 USD | 0.00 USD | 5,210,000.00 USD | 89,460.00 USD | 11,900.00 USD | 32,640.00 USD |
| `1D` | `272.80` | 5,140,000.00 USD | 0.00 USD | 5,140,000.00 USD | 95,440.00 USD | 46,670.00 USD | 20,950.00 USD |
| `7D` | `272.80` | 5,080,000.00 USD | 0.00 USD | 5,080,000.00 USD | 95,440.00 USD | 46,670.00 USD | 20,950.00 USD |
| `1D` | `273.20` | 4,970,000.00 USD | 0.00 USD | 4,970,000.00 USD | 66,160.00 USD | 132,260.00 USD | 35,090.00 USD |
| `7D` | `273.20` | 4,920,000.00 USD | 0.00 USD | 4,920,000.00 USD | 66,160.00 USD | 132,260.00 USD | 35,090.00 USD |
| `1D` | `273.60` | 4,740,000.00 USD | 0.00 USD | 4,740,000.00 USD | 236,160.00 USD | 240,340.00 USD | 90,160.00 USD |
| `7D` | `273.60` | 4,680,000.00 USD | 0.00 USD | 4,680,000.00 USD | 236,160.00 USD | 240,340.00 USD | 90,160.00 USD |
| `1D` | `274.00` | 4,170,000.00 USD | 0.00 USD | 4,170,000.00 USD | 144,320.00 USD | 230,200.00 USD | 95,270.00 USD |
| `7D` | `274.00` | 4,120,000.00 USD | 0.00 USD | 4,120,000.00 USD | 144,320.00 USD | 230,200.00 USD | 95,270.00 USD |
| `1D` | `274.40` | 3,700,000.00 USD | 0.00 USD | 3,700,000.00 USD | 216,260.00 USD | 142,650.00 USD | 145,010.00 USD |
| `7D` | `274.40` | 3,650,000.00 USD | 0.00 USD | 3,650,000.00 USD | 216,260.00 USD | 142,650.00 USD | 145,010.00 USD |
| `1D` | `274.80` | 3,200,000.00 USD | 0.00 USD | 3,200,000.00 USD | 51,320.00 USD | 33,360.00 USD | 58,350.00 USD |
| `7D` | `274.80` | 3,140,000.00 USD | 0.00 USD | 3,140,000.00 USD | 51,320.00 USD | 33,360.00 USD | 58,350.00 USD |
| `1D` | `275.20` | 3,060,000.00 USD | 0.00 USD | 3,060,000.00 USD | 77,850.00 USD | 44,580.00 USD | 56,930.00 USD |
| `7D` | `275.20` | 3,000,000.00 USD | 0.00 USD | 3,000,000.00 USD | 77,850.00 USD | 44,580.00 USD | 56,930.00 USD |
| `1D` | `275.60` | 2,880,000.00 USD | 0.00 USD | 2,880,000.00 USD | 44,240.00 USD | 44,510.00 USD | 35,830.00 USD |
| `7D` | `275.60` | 2,820,000.00 USD | 0.00 USD | 2,820,000.00 USD | 44,240.00 USD | 44,510.00 USD | 35,830.00 USD |
| `1D` | `276.00` | 2,750,000.00 USD | 0.00 USD | 2,750,000.00 USD | 59,560.00 USD | 37,170.00 USD | 22,040.00 USD |
| `7D` | `276.00` | 2,690,000.00 USD | 0.00 USD | 2,690,000.00 USD | 59,560.00 USD | 37,170.00 USD | 22,040.00 USD |
| `1D` | `276.40` | 2,630,000.00 USD | 0.00 USD | 2,630,000.00 USD | 36,470.00 USD | 42,830.00 USD | 3,230.00 USD |
| `7D` | `276.40` | 2,580,000.00 USD | 0.00 USD | 2,580,000.00 USD | 36,470.00 USD | 42,830.00 USD | 3,230.00 USD |
| `1D` | `276.80` | 2,550,000.00 USD | 0.00 USD | 2,550,000.00 USD | 10,750.00 USD | 15,870.00 USD | 11,360.00 USD |
| `7D` | `276.80` | 2,490,000.00 USD | 0.00 USD | 2,490,000.00 USD | 10,750.00 USD | 15,870.00 USD | 11,360.00 USD |
| `1D` | `277.20` | 2,510,000.00 USD | 0.00 USD | 2,510,000.00 USD | 301.20 USD | 80,120.00 USD | 21,180.00 USD |
| `7D` | `277.20` | 2,460,000.00 USD | 0.00 USD | 2,460,000.00 USD | 301.20 USD | 80,120.00 USD | 21,180.00 USD |
| `1D` | `277.60` | 2,410,000.00 USD | 0.00 USD | 2,410,000.00 USD | 57,640.00 USD | 47,660.00 USD | 5.52 USD |
| `7D` | `277.60` | 2,350,000.00 USD | 0.00 USD | 2,350,000.00 USD | 57,640.00 USD | 47,660.00 USD | 5.52 USD |
| `1D` | `278.00` | 2,310,000.00 USD | 0.00 USD | 2,310,000.00 USD | 12,650.00 USD | 9,490.00 USD | 0.00 USD |
| `7D` | `278.00` | 2,250,000.00 USD | 0.00 USD | 2,250,000.00 USD | 12,650.00 USD | 9,490.00 USD | 0.00 USD |
| `1D` | `278.40` | 2,280,000.00 USD | 0.00 USD | 2,280,000.00 USD | 61,240.00 USD | 25,470.00 USD | 57,330.00 USD |
| `7D` | `278.40` | 2,230,000.00 USD | 0.00 USD | 2,230,000.00 USD | 61,240.00 USD | 25,470.00 USD | 37,930.00 USD |
| `1D` | `278.80` | 2,140,000.00 USD | 0.00 USD | 2,140,000.00 USD | 22,630.00 USD | 22,990.00 USD | 10,340.00 USD |
| `7D` | `278.80` | 2,100,000.00 USD | 0.00 USD | 2,100,000.00 USD | 22,630.00 USD | 22,990.00 USD | 10,340.00 USD |
| `1D` | `279.20` | 2,080,000.00 USD | 0.00 USD | 2,080,000.00 USD | 42,910.00 USD | 23,330.00 USD | 23,180.00 USD |
| `7D` | `279.20` | 2,050,000.00 USD | 0.00 USD | 2,050,000.00 USD | 42,910.00 USD | 23,330.00 USD | 23,180.00 USD |
| `1D` | `279.60` | 2,000,000.00 USD | 0.00 USD | 2,000,000.00 USD | 20,320.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `279.60` | 1,960,000.00 USD | 0.00 USD | 1,960,000.00 USD | 20,320.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `280.00` | 1,970,000.00 USD | 0.00 USD | 1,970,000.00 USD | 21,040.00 USD | 0.00 USD | 17,110.00 USD |
| `7D` | `280.00` | 1,940,000.00 USD | 0.00 USD | 1,940,000.00 USD | 21,040.00 USD | 0.00 USD | 17,110.00 USD |
| `1D` | `280.40` | 1,940,000.00 USD | 0.00 USD | 1,940,000.00 USD | 8,720.00 USD | 0.00 USD | 41,630.00 USD |
| `7D` | `280.40` | 1,900,000.00 USD | 0.00 USD | 1,900,000.00 USD | 8,720.00 USD | 0.00 USD | 41,630.00 USD |
| `1D` | `280.80` | 1,890,000.00 USD | 0.00 USD | 1,890,000.00 USD | 21,670.00 USD | 0.00 USD | 64,530.00 USD |
| `7D` | `280.80` | 1,850,000.00 USD | 0.00 USD | 1,850,000.00 USD | 21,670.00 USD | 0.00 USD | 64,530.00 USD |
| `1D` | `281.20` | 1,800,000.00 USD | 0.00 USD | 1,800,000.00 USD | 8,920.00 USD | 0.00 USD | 66,500.00 USD |
| `7D` | `281.20` | 1,760,000.00 USD | 0.00 USD | 1,760,000.00 USD | 8,920.00 USD | 0.00 USD | 66,500.00 USD |
| `1D` | `281.60` | 1,720,000.00 USD | 0.00 USD | 1,720,000.00 USD | 0.00 USD | 0.00 USD | 27,950.00 USD |
| `7D` | `281.60` | 1,690,000.00 USD | 0.00 USD | 1,690,000.00 USD | 0.00 USD | 0.00 USD | 27,950.00 USD |
| `1D` | `282.00` | 1,700,000.00 USD | 0.00 USD | 1,700,000.00 USD | 36,030.00 USD | 39,110.00 USD | 120,430.00 USD |
| `7D` | `282.00` | 1,660,000.00 USD | 0.00 USD | 1,660,000.00 USD | 36,030.00 USD | 39,110.00 USD | 120,430.00 USD |
| `1D` | `282.40` | 1,500,000.00 USD | 0.00 USD | 1,500,000.00 USD | 0.00 USD | 0.00 USD | 70,940.00 USD |
| `7D` | `282.40` | 1,460,000.00 USD | 0.00 USD | 1,460,000.00 USD | 0.00 USD | 0.00 USD | 70,940.00 USD |
| `1D` | `282.80` | 1,430,000.00 USD | 0.00 USD | 1,430,000.00 USD | 0.00 USD | 67,970.00 USD | 51,860.00 USD |
| `7D` | `282.80` | 1,390,000.00 USD | 0.00 USD | 1,390,000.00 USD | 0.00 USD | 67,970.00 USD | 51,860.00 USD |
| `1D` | `283.20` | 1,310,000.00 USD | 0.00 USD | 1,310,000.00 USD | 0.00 USD | 0.00 USD | 81,880.00 USD |
| `7D` | `283.20` | 1,270,000.00 USD | 0.00 USD | 1,270,000.00 USD | 0.00 USD | 0.00 USD | 81,880.00 USD |
| `1D` | `283.60` | 1,230,000.00 USD | 0.00 USD | 1,230,000.00 USD | 0.00 USD | 11,490.00 USD | 4,100.00 USD |
| `7D` | `283.60` | 1,190,000.00 USD | 0.00 USD | 1,190,000.00 USD | 0.00 USD | 11,490.00 USD | 4,100.00 USD |
| `1D` | `284.00` | 1,210,000.00 USD | 0.00 USD | 1,210,000.00 USD | 0.00 USD | 18,990.00 USD | 69,640.00 USD |
| `7D` | `284.00` | 1,170,000.00 USD | 0.00 USD | 1,170,000.00 USD | 0.00 USD | 18,990.00 USD | 30,860.00 USD |
| `1D` | `284.40` | 1,120,000.00 USD | 0.00 USD | 1,120,000.00 USD | 37,810.00 USD | 76,740.00 USD | 20,690.00 USD |
| `7D` | `284.40` | 1,120,000.00 USD | 0.00 USD | 1,120,000.00 USD | 37,810.00 USD | 76,740.00 USD | 20,690.00 USD |
| `1D` | `284.80` | 989,150.00 USD | 0.00 USD | 989,150.00 USD | 31,830.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `284.80` | 989,150.00 USD | 0.00 USD | 989,150.00 USD | 31,830.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `285.20` | 957,320.00 USD | 0.00 USD | 957,320.00 USD | 0.00 USD | 0.00 USD | 44,680.00 USD |
| `7D` | `285.20` | 957,320.00 USD | 0.00 USD | 957,320.00 USD | 0.00 USD | 0.00 USD | 44,680.00 USD |
| `1D` | `285.60` | 912,640.00 USD | 0.00 USD | 912,640.00 USD | 91,500.00 USD | 115,180.00 USD | 0.00 USD |
| `7D` | `285.60` | 912,640.00 USD | 0.00 USD | 912,640.00 USD | 91,500.00 USD | 115,180.00 USD | 0.00 USD |
| `1D` | `286.00` | 705,960.00 USD | 0.00 USD | 705,960.00 USD | 0.00 USD | 30,000.00 USD | 0.00 USD |
| `7D` | `286.00` | 705,960.00 USD | 0.00 USD | 705,960.00 USD | 0.00 USD | 30,000.00 USD | 0.00 USD |
| `1D` | `286.40` | 675,960.00 USD | 0.00 USD | 675,960.00 USD | 79,480.00 USD | 40,040.00 USD | 37,510.00 USD |
| `7D` | `286.40` | 675,960.00 USD | 0.00 USD | 675,960.00 USD | 79,480.00 USD | 40,040.00 USD | 37,510.00 USD |
| `1D` | `286.80` | 518,930.00 USD | 0.00 USD | 518,930.00 USD | 114,760.00 USD | 69,490.00 USD | 91,300.00 USD |
| `7D` | `286.80` | 518,930.00 USD | 0.00 USD | 518,930.00 USD | 114,760.00 USD | 69,490.00 USD | 91,300.00 USD |
| `1D` | `287.20` | 243,380.00 USD | 0.00 USD | 243,380.00 USD | 0.00 USD | 117,540.00 USD | 32,710.00 USD |
| `7D` | `287.20` | 243,380.00 USD | 0.00 USD | 243,380.00 USD | 0.00 USD | 117,540.00 USD | 32,710.00 USD |
| `1D` | `287.60` | 93,120.00 USD | 0.00 USD | 93,120.00 USD | 0.00 USD | 11,010.00 USD | 0.00 USD |
| `7D` | `287.60` | 93,120.00 USD | 0.00 USD | 93,120.00 USD | 0.00 USD | 11,010.00 USD | 0.00 USD |
| `1D` | `288.00` | 82,110.00 USD | 0.00 USD | 82,110.00 USD | 0.00 USD | 0.00 USD | 45,010.00 USD |
| `7D` | `288.00` | 82,110.00 USD | 0.00 USD | 82,110.00 USD | 0.00 USD | 0.00 USD | 45,010.00 USD |
| `1D` | `288.40` | 37,100.00 USD | 0.00 USD | 37,100.00 USD | 10,110.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `288.40` | 37,100.00 USD | 0.00 USD | 37,100.00 USD | 10,110.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `288.80` | 26,990.00 USD | 0.00 USD | 26,990.00 USD | 26,990.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `288.80` | 26,990.00 USD | 0.00 USD | 26,990.00 USD | 26,990.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `289.00` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `289.10` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `289.20` | 11,990.00 USD | 11,990.00 USD | 0.00 USD | 0.00 USD | 11,990.00 USD | 0.00 USD |
| `7D` | `289.20` | 11,990.00 USD | 11,990.00 USD | 0.00 USD | 0.00 USD | 11,990.00 USD | 0.00 USD |
| `1D` | `291.20` | 186,300.00 USD | 186,300.00 USD | 0.00 USD | 0.00 USD | 128,140.00 USD | 46,160.00 USD |
| `7D` | `291.20` | 186,300.00 USD | 186,300.00 USD | 0.00 USD | 0.00 USD | 128,140.00 USD | 46,160.00 USD |
| `1D` | `291.60` | 282,700.00 USD | 282,700.00 USD | 0.00 USD | 0.00 USD | 41,860.00 USD | 54,540.00 USD |
| `7D` | `291.60` | 282,700.00 USD | 282,700.00 USD | 0.00 USD | 0.00 USD | 41,860.00 USD | 54,540.00 USD |
| `1D` | `292.00` | 309,090.00 USD | 309,090.00 USD | 0.00 USD | 0.00 USD | 26,380.00 USD | 7.32 USD |
| `7D` | `292.00` | 309,090.00 USD | 309,090.00 USD | 0.00 USD | 0.00 USD | 26,380.00 USD | 7.32 USD |
| `1D` | `292.40` | 352,360.00 USD | 352,360.00 USD | 0.00 USD | 0.00 USD | 43,260.00 USD | 8.42 USD |
| `7D` | `292.40` | 352,360.00 USD | 352,360.00 USD | 0.00 USD | 0.00 USD | 43,260.00 USD | 8.42 USD |
| `1D` | `292.80` | 450,720.00 USD | 450,720.00 USD | 0.00 USD | 1,040.00 USD | 97,310.00 USD | 6.65 USD |
| `7D` | `292.80` | 450,720.00 USD | 450,720.00 USD | 0.00 USD | 1,040.00 USD | 97,310.00 USD | 6.65 USD |
| `1D` | `293.20` | 499,690.00 USD | 499,690.00 USD | 0.00 USD | 443.30 USD | 48,530.00 USD | 0.42 USD |
| `7D` | `293.20` | 524,280.00 USD | 524,280.00 USD | 0.00 USD | 443.30 USD | 73,120.00 USD | 0.42 USD |
| `1D` | `293.60` | 665,210.00 USD | 665,210.00 USD | 0.00 USD | 44,620.00 USD | 65,190.00 USD | 55,700.00 USD |
| `7D` | `293.60` | 689,800.00 USD | 689,800.00 USD | 0.00 USD | 44,620.00 USD | 65,190.00 USD | 55,700.00 USD |
| `1D` | `294.00` | 749,430.00 USD | 749,430.00 USD | 0.00 USD | 8,430.00 USD | 41,700.00 USD | 34,090.00 USD |
| `7D` | `294.00` | 774,020.00 USD | 774,020.00 USD | 0.00 USD | 8,430.00 USD | 41,700.00 USD | 34,090.00 USD |
| `1D` | `294.40` | 1,070,000.00 USD | 1,070,000.00 USD | 0.00 USD | 112,960.00 USD | 115,230.00 USD | 96,530.00 USD |
| `7D` | `294.40` | 1,100,000.00 USD | 1,100,000.00 USD | 0.00 USD | 112,960.00 USD | 115,230.00 USD | 96,530.00 USD |
| `1D` | `294.80` | 1,280,000.00 USD | 1,280,000.00 USD | 0.00 USD | 56,500.00 USD | 79,340.00 USD | 70,850.00 USD |
| `7D` | `294.80` | 1,310,000.00 USD | 1,310,000.00 USD | 0.00 USD | 56,500.00 USD | 79,340.00 USD | 70,850.00 USD |
| `1D` | `295.20` | 1,430,000.00 USD | 1,430,000.00 USD | 0.00 USD | 77,470.00 USD | 49,290.00 USD | 23,210.00 USD |
| `7D` | `295.20` | 1,460,000.00 USD | 1,460,000.00 USD | 0.00 USD | 77,470.00 USD | 49,290.00 USD | 23,210.00 USD |
| `1D` | `295.60` | 1,750,000.00 USD | 1,750,000.00 USD | 0.00 USD | 105,500.00 USD | 108,340.00 USD | 102,120.00 USD |
| `7D` | `295.60` | 1,730,000.00 USD | 1,730,000.00 USD | 0.00 USD | 105,500.00 USD | 108,340.00 USD | 63,330.00 USD |
| `1D` | `296.00` | 1,950,000.00 USD | 1,950,000.00 USD | 0.00 USD | 85,930.00 USD | 76,170.00 USD | 39,110.00 USD |
| `7D` | `296.00` | 1,930,000.00 USD | 1,930,000.00 USD | 0.00 USD | 85,930.00 USD | 76,170.00 USD | 39,110.00 USD |
| `1D` | `296.40` | 2,100,000.00 USD | 2,100,000.00 USD | 0.00 USD | 77,790.00 USD | 50,830.00 USD | 18,610.00 USD |
| `7D` | `296.40` | 2,080,000.00 USD | 2,080,000.00 USD | 0.00 USD | 77,790.00 USD | 50,830.00 USD | 18,610.00 USD |
| `1D` | `296.80` | 2,230,000.00 USD | 2,230,000.00 USD | 0.00 USD | 32,000.00 USD | 35,500.00 USD | 64,680.00 USD |
| `7D` | `296.80` | 2,210,000.00 USD | 2,210,000.00 USD | 0.00 USD | 32,000.00 USD | 35,500.00 USD | 64,680.00 USD |
| `1D` | `297.20` | 2,350,000.00 USD | 2,350,000.00 USD | 0.00 USD | 59,030.00 USD | 27,370.00 USD | 31,730.00 USD |
| `7D` | `297.20` | 2,330,000.00 USD | 2,330,000.00 USD | 0.00 USD | 59,030.00 USD | 27,370.00 USD | 31,730.00 USD |
| `1D` | `297.60` | 2,390,000.00 USD | 2,390,000.00 USD | 0.00 USD | 5,970.00 USD | 1,010.00 USD | 32,550.00 USD |
| `7D` | `297.60` | 2,370,000.00 USD | 2,370,000.00 USD | 0.00 USD | 5,970.00 USD | 1,010.00 USD | 32,550.00 USD |
| `1D` | `298.00` | 2,510,000.00 USD | 2,510,000.00 USD | 0.00 USD | 58,630.00 USD | 8,080.00 USD | 58,400.00 USD |
| `7D` | `298.00` | 2,500,000.00 USD | 2,500,000.00 USD | 0.00 USD | 58,630.00 USD | 8,080.00 USD | 58,410.00 USD |
| `1D` | `298.40` | 2,630,000.00 USD | 2,630,000.00 USD | 0.00 USD | 5,480.00 USD | 15,780.00 USD | 100,250.00 USD |
| `7D` | `298.40` | 2,620,000.00 USD | 2,620,000.00 USD | 0.00 USD | 5,480.00 USD | 15,780.00 USD | 100,250.00 USD |
| `1D` | `298.80` | 2,780,000.00 USD | 2,780,000.00 USD | 0.00 USD | 33,630.00 USD | 5,810.00 USD | 107,460.00 USD |
| `7D` | `298.80` | 2,800,000.00 USD | 2,800,000.00 USD | 0.00 USD | 56,580.00 USD | 18,110.00 USD | 107,460.00 USD |
| `1D` | `299.20` | 2,860,000.00 USD | 2,860,000.00 USD | 0.00 USD | 37,170.00 USD | 36,020.00 USD | 12,310.00 USD |
| `7D` | `299.20` | 2,890,000.00 USD | 2,890,000.00 USD | 0.00 USD | 37,170.00 USD | 36,500.00 USD | 12,310.00 USD |
| `1D` | `299.60` | 2,930,000.00 USD | 2,930,000.00 USD | 0.00 USD | 18,100.00 USD | 15,600.00 USD | 31,200.00 USD |
| `7D` | `299.60` | 2,950,000.00 USD | 2,950,000.00 USD | 0.00 USD | 18,100.00 USD | 16,000.00 USD | 31,200.00 USD |
| `1D` | `300.00` | 2,980,000.00 USD | 2,980,000.00 USD | 0.00 USD | 22,390.00 USD | 25,550.00 USD | 6,200.00 USD |
| `7D` | `300.00` | 3,010,000.00 USD | 3,010,000.00 USD | 0.00 USD | 22,390.00 USD | 25,550.00 USD | 6,200.00 USD |
| `1D` | `300.40` | 3,080,000.00 USD | 3,080,000.00 USD | 0.00 USD | 14,470.00 USD | 31,680.00 USD | 45,920.00 USD |
| `7D` | `300.40` | 3,100,000.00 USD | 3,100,000.00 USD | 0.00 USD | 14,470.00 USD | 31,680.00 USD | 45,920.00 USD |
| `1D` | `300.80` | 3,130,000.00 USD | 3,130,000.00 USD | 0.00 USD | 11,300.00 USD | 30,510.00 USD | 12,770.00 USD |
| `7D` | `300.80` | 3,150,000.00 USD | 3,150,000.00 USD | 0.00 USD | 11,300.00 USD | 30,510.00 USD | 12,770.00 USD |
| `1D` | `301.20` | 3,210,000.00 USD | 3,210,000.00 USD | 0.00 USD | 35,650.00 USD | 49,010.00 USD | 22.51 USD |
| `7D` | `301.20` | 3,240,000.00 USD | 3,240,000.00 USD | 0.00 USD | 35,650.00 USD | 49,010.00 USD | 22.51 USD |
| `1D` | `301.60` | 3,300,000.00 USD | 3,300,000.00 USD | 0.00 USD | 32,070.00 USD | 12,240.00 USD | 44,040.00 USD |
| `7D` | `301.60` | 3,310,000.00 USD | 3,310,000.00 USD | 0.00 USD | 32,070.00 USD | 12,240.00 USD | 24,640.00 USD |
| `1D` | `302.00` | 3,390,000.00 USD | 3,390,000.00 USD | 0.00 USD | 36,140.00 USD | 35,930.00 USD | 11,570.00 USD |
| `7D` | `302.00` | 3,390,000.00 USD | 3,390,000.00 USD | 0.00 USD | 36,140.00 USD | 35,930.00 USD | 11,570.00 USD |
| `1D` | `302.40` | 3,410,000.00 USD | 3,410,000.00 USD | 0.00 USD | 667.34 USD | 9,620.00 USD | 10,300.00 USD |
| `7D` | `302.40` | 3,410,000.00 USD | 3,410,000.00 USD | 0.00 USD | 667.34 USD | 9,620.00 USD | 10,300.00 USD |
| `1D` | `302.80` | 3,420,000.00 USD | 3,420,000.00 USD | 0.00 USD | 1,230.00 USD | 2,200.00 USD | 6,530.00 USD |
| `7D` | `302.80` | 3,420,000.00 USD | 3,420,000.00 USD | 0.00 USD | 1,230.00 USD | 2,200.00 USD | 6,540.00 USD |
| `1D` | `303.20` | 3,460,000.00 USD | 3,460,000.00 USD | 0.00 USD | 32,120.00 USD | 348.99 USD | 14,740.00 USD |
| `7D` | `303.20` | 3,470,000.00 USD | 3,470,000.00 USD | 0.00 USD | 32,120.00 USD | 348.99 USD | 14,740.00 USD |
| `1D` | `303.60` | 3,480,000.00 USD | 3,480,000.00 USD | 0.00 USD | 9,000.00 USD | 3,300.00 USD | 6,250.00 USD |
| `7D` | `303.60` | 3,490,000.00 USD | 3,490,000.00 USD | 0.00 USD | 9,000.00 USD | 3,300.00 USD | 6,250.00 USD |
| `1D` | `304.00` | 3,540,000.00 USD | 3,540,000.00 USD | 0.00 USD | 22,400.00 USD | 807.39 USD | 32,130.00 USD |
| `7D` | `304.00` | 3,540,000.00 USD | 3,540,000.00 USD | 0.00 USD | 22,400.00 USD | 1,170.00 USD | 32,130.00 USD |
| `1D` | `304.40` | 3,620,000.00 USD | 3,620,000.00 USD | 0.00 USD | 13,620.00 USD | 9,840.00 USD | 59,180.00 USD |
| `7D` | `304.40` | 3,620,000.00 USD | 3,620,000.00 USD | 0.00 USD | 13,620.00 USD | 10,140.00 USD | 59,180.00 USD |
| `1D` | `304.80` | 3,640,000.00 USD | 3,640,000.00 USD | 0.00 USD | 592.20 USD | 318.60 USD | 16,360.00 USD |
| `7D` | `304.80` | 3,640,000.00 USD | 3,640,000.00 USD | 0.00 USD | 592.20 USD | 318.60 USD | 16,360.00 USD |
| `1D` | `305.20` | 3,650,000.00 USD | 3,650,000.00 USD | 0.00 USD | 10,560.00 USD | 236.66 USD | 2,010.00 USD |
| `7D` | `305.20` | 3,650,000.00 USD | 3,650,000.00 USD | 0.00 USD | 10,560.00 USD | 236.66 USD | 2,010.00 USD |
| `1D` | `305.60` | 3,660,000.00 USD | 3,660,000.00 USD | 0.00 USD | 4,670.00 USD | 1,770.00 USD | 1,490.00 USD |
| `7D` | `305.60` | 3,660,000.00 USD | 3,660,000.00 USD | 0.00 USD | 4,670.00 USD | 1,770.00 USD | 1,490.00 USD |
| `1D` | `306.00` | 3,670,000.00 USD | 3,670,000.00 USD | 0.00 USD | 9,590.00 USD | 2,740.00 USD | 3,270.00 USD |
| `7D` | `306.00` | 3,680,000.00 USD | 3,680,000.00 USD | 0.00 USD | 9,590.00 USD | 2,740.00 USD | 3,270.00 USD |
| `1D` | `306.40` | 3,690,000.00 USD | 3,690,000.00 USD | 0.00 USD | 4,560.00 USD | 9,460.00 USD | 68.00 USD |
| `7D` | `306.40` | 3,690,000.00 USD | 3,690,000.00 USD | 0.00 USD | 4,560.00 USD | 9,460.00 USD | 68.00 USD |
| `1D` | `306.80` | 3,760,000.00 USD | 3,760,000.00 USD | 0.00 USD | 28,610.00 USD | 35,400.00 USD | 5,490.00 USD |
| `7D` | `306.80` | 3,760,000.00 USD | 3,760,000.00 USD | 0.00 USD | 28,610.00 USD | 35,400.00 USD | 5,490.00 USD |
| `1D` | `307.20` | 3,810,000.00 USD | 3,810,000.00 USD | 0.00 USD | 11,550.00 USD | 27,080.00 USD | 18,140.00 USD |
| `7D` | `307.20` | 3,820,000.00 USD | 3,820,000.00 USD | 0.00 USD | 11,550.00 USD | 27,080.00 USD | 18,140.00 USD |
| `1D` | `307.60` | 3,860,000.00 USD | 3,860,000.00 USD | 0.00 USD | 15,000.00 USD | 30,960.00 USD | 3,670.00 USD |
| `7D` | `307.60` | 3,870,000.00 USD | 3,870,000.00 USD | 0.00 USD | 15,000.00 USD | 30,960.00 USD | 3,670.00 USD |
| `1D` | `308.00` | 3,940,000.00 USD | 3,940,000.00 USD | 0.00 USD | 30,270.00 USD | 20,830.00 USD | 22,690.00 USD |
| `7D` | `308.00` | 3,940,000.00 USD | 3,940,000.00 USD | 0.00 USD | 30,270.00 USD | 20,830.00 USD | 22,690.00 USD |
| `1D` | `308.40` | 3,950,000.00 USD | 3,950,000.00 USD | 0.00 USD | 5,350.00 USD | 3,460.00 USD | 4,260.00 USD |
| `7D` | `308.40` | 3,950,000.00 USD | 3,950,000.00 USD | 0.00 USD | 5,350.00 USD | 3,460.00 USD | 4,260.00 USD |
| `1D` | `308.80` | 3,960,000.00 USD | 3,960,000.00 USD | 0.00 USD | 9,910.00 USD | 280.94 USD | 3,480.00 USD |
| `7D` | `308.80` | 3,970,000.00 USD | 3,970,000.00 USD | 0.00 USD | 9,910.00 USD | 280.94 USD | 3,480.00 USD |
| `1D` | `309.20` | 3,990,000.00 USD | 3,990,000.00 USD | 0.00 USD | 9,930.00 USD | 15,050.00 USD | 3,020.00 USD |
| `7D` | `309.20` | 4,000,000.00 USD | 4,000,000.00 USD | 0.00 USD | 9,930.00 USD | 15,050.00 USD | 3,020.00 USD |
| `1D` | `309.60` | 4,030,000.00 USD | 4,030,000.00 USD | 0.00 USD | 10,210.00 USD | 14,260.00 USD | 8,230.00 USD |
| `7D` | `309.60` | 4,030,000.00 USD | 4,030,000.00 USD | 0.00 USD | 10,210.00 USD | 14,260.00 USD | 8,230.00 USD |
| `1D` | `310.00` | 4,040,000.00 USD | 4,040,000.00 USD | 0.00 USD | 8,210.00 USD | 4,640.00 USD | 978.51 USD |
| `7D` | `310.00` | 4,040,000.00 USD | 4,040,000.00 USD | 0.00 USD | 8,210.00 USD | 4,640.00 USD | 978.51 USD |
| `1D` | `310.40` | 4,050,000.00 USD | 4,050,000.00 USD | 0.00 USD | 376.38 USD | 5,370.00 USD | 3.86 USD |
| `7D` | `310.40` | 4,050,000.00 USD | 4,050,000.00 USD | 0.00 USD | 376.38 USD | 5,370.00 USD | 3.86 USD |
| `1D` | `310.80` | 4,050,000.00 USD | 4,050,000.00 USD | 0.00 USD | 0.00 USD | 48.50 USD | 1.49 USD |
| `7D` | `310.80` | 4,050,000.00 USD | 4,050,000.00 USD | 0.00 USD | 0.00 USD | 48.50 USD | 1.49 USD |
| `1D` | `311.20` | 4,060,000.00 USD | 4,060,000.00 USD | 0.00 USD | 431.32 USD | 2,050.00 USD | 12,640.00 USD |
| `7D` | `311.20` | 4,060,000.00 USD | 4,060,000.00 USD | 0.00 USD | 431.32 USD | 2,050.00 USD | 12,640.00 USD |
| `1D` | `311.60` | 4,100,000.00 USD | 4,100,000.00 USD | 0.00 USD | 27,810.00 USD | 6,590.00 USD | 9,750.00 USD |
| `7D` | `311.60` | 4,110,000.00 USD | 4,110,000.00 USD | 0.00 USD | 27,810.00 USD | 6,590.00 USD | 9,750.00 USD |
| `1D` | `312.00` | 4,100,000.00 USD | 4,100,000.00 USD | 0.00 USD | 244.00 USD | 0.00 USD | 4.48 USD |
| `7D` | `312.00` | 4,110,000.00 USD | 4,110,000.00 USD | 0.00 USD | 244.00 USD | 0.00 USD | 4.48 USD |
| `1D` | `312.40` | 4,130,000.00 USD | 4,130,000.00 USD | 0.00 USD | 13,950.00 USD | 7,480.00 USD | 8,710.00 USD |
| `7D` | `312.40` | 4,140,000.00 USD | 4,140,000.00 USD | 0.00 USD | 13,950.00 USD | 7,480.00 USD | 8,710.00 USD |
| `1D` | `312.80` | 4,150,000.00 USD | 4,150,000.00 USD | 0.00 USD | 11,710.00 USD | 23.27 USD | 23.91 USD |
| `7D` | `312.80` | 4,150,000.00 USD | 4,150,000.00 USD | 0.00 USD | 11,710.00 USD | 23.27 USD | 23.91 USD |
| `1D` | `313.20` | 4,160,000.00 USD | 4,160,000.00 USD | 0.00 USD | 5,080.00 USD | 3,820.00 USD | 8,970.00 USD |
| `7D` | `313.20` | 4,170,000.00 USD | 4,170,000.00 USD | 0.00 USD | 5,080.00 USD | 3,820.00 USD | 8,970.00 USD |
| `1D` | `313.60` | 4,190,000.00 USD | 4,190,000.00 USD | 0.00 USD | 11,920.00 USD | 7,180.00 USD | 10,050.00 USD |
| `7D` | `313.60` | 4,200,000.00 USD | 4,200,000.00 USD | 0.00 USD | 11,920.00 USD | 7,620.00 USD | 10,050.00 USD |
| `1D` | `314.00` | 4,200,000.00 USD | 4,200,000.00 USD | 0.00 USD | 4,410.00 USD | 6,040.00 USD | 0.00 USD |
| `7D` | `314.00` | 4,210,000.00 USD | 4,210,000.00 USD | 0.00 USD | 4,410.00 USD | 6,040.00 USD | 0.00 USD |
| `1D` | `314.40` | 4,230,000.00 USD | 4,230,000.00 USD | 0.00 USD | 4,320.00 USD | 10,960.00 USD | 7,320.00 USD |
| `7D` | `314.40` | 4,230,000.00 USD | 4,230,000.00 USD | 0.00 USD | 4,320.00 USD | 10,960.00 USD | 7,320.00 USD |
| `1D` | `314.80` | 4,240,000.00 USD | 4,240,000.00 USD | 0.00 USD | 479.45 USD | 0.00 USD | 9,250.00 USD |
| `7D` | `314.80` | 4,240,000.00 USD | 4,240,000.00 USD | 0.00 USD | 479.45 USD | 0.00 USD | 9,250.00 USD |
| `1D` | `315.20` | 4,250,000.00 USD | 4,250,000.00 USD | 0.00 USD | 3,740.00 USD | 0.00 USD | 5,900.00 USD |
| `7D` | `315.20` | 4,250,000.00 USD | 4,250,000.00 USD | 0.00 USD | 3,740.00 USD | 0.00 USD | 5,900.00 USD |
| `1D` | `315.60` | 4,270,000.00 USD | 4,270,000.00 USD | 0.00 USD | 0.00 USD | 6,310.00 USD | 19,390.00 USD |
| `7D` | `315.60` | 4,280,000.00 USD | 4,280,000.00 USD | 0.00 USD | 0.00 USD | 6,310.00 USD | 19,390.00 USD |
| `1D` | `316.00` | 4,290,000.00 USD | 4,290,000.00 USD | 0.00 USD | 6,390.00 USD | 2,260.00 USD | 10,740.00 USD |
| `7D` | `316.00` | 4,310,000.00 USD | 4,310,000.00 USD | 0.00 USD | 13,020.00 USD | 7,180.00 USD | 10,740.00 USD |
| `1D` | `316.40` | 4,310,000.00 USD | 4,310,000.00 USD | 0.00 USD | 12,950.00 USD | 5,010.00 USD | 1,100.00 USD |
| `7D` | `316.40` | 4,330,000.00 USD | 4,330,000.00 USD | 0.00 USD | 12,950.00 USD | 5,010.00 USD | 1,100.00 USD |
| `1D` | `316.80` | 4,340,000.00 USD | 4,340,000.00 USD | 0.00 USD | 5,360.00 USD | 8,870.00 USD | 11,440.00 USD |
| `7D` | `316.80` | 4,350,000.00 USD | 4,350,000.00 USD | 0.00 USD | 5,360.00 USD | 8,870.00 USD | 11,440.00 USD |
| `1D` | `317.20` | 4,350,000.00 USD | 4,350,000.00 USD | 0.00 USD | 3,920.00 USD | 4,340.00 USD | 2,630.00 USD |
| `7D` | `317.20` | 4,360,000.00 USD | 4,360,000.00 USD | 0.00 USD | 3,920.00 USD | 4,340.00 USD | 2,630.00 USD |
| `1D` | `317.60` | 4,370,000.00 USD | 4,370,000.00 USD | 0.00 USD | 6,150.00 USD | 12,380.00 USD | 8,480.00 USD |
| `7D` | `317.60` | 4,390,000.00 USD | 4,390,000.00 USD | 0.00 USD | 6,150.00 USD | 12,380.00 USD | 8,480.00 USD |
| `1D` | `318.00` | 4,400,000.00 USD | 4,400,000.00 USD | 0.00 USD | 2,290.00 USD | 12,210.00 USD | 9,880.00 USD |
| `7D` | `318.00` | 4,410,000.00 USD | 4,410,000.00 USD | 0.00 USD | 2,290.00 USD | 12,210.00 USD | 9,880.00 USD |
| `1D` | `318.40` | 4,400,000.00 USD | 4,400,000.00 USD | 0.00 USD | 234.70 USD | 5,370.00 USD | 820.17 USD |
| `7D` | `318.40` | 4,420,000.00 USD | 4,420,000.00 USD | 0.00 USD | 234.70 USD | 5,370.00 USD | 820.17 USD |
| `1D` | `318.80` | 4,440,000.00 USD | 4,440,000.00 USD | 0.00 USD | 9,170.00 USD | 10,850.00 USD | 13,930.00 USD |
| `7D` | `318.80` | 4,450,000.00 USD | 4,450,000.00 USD | 0.00 USD | 9,170.00 USD | 10,850.00 USD | 6,170.00 USD |
| `1D` | `319.20` | 4,460,000.00 USD | 4,460,000.00 USD | 0.00 USD | 7,830.00 USD | 11,350.00 USD | 488.47 USD |
| `7D` | `319.20` | 4,470,000.00 USD | 4,470,000.00 USD | 0.00 USD | 7,830.00 USD | 11,350.00 USD | 488.47 USD |
| `1D` | `319.60` | 4,470,000.00 USD | 4,470,000.00 USD | 0.00 USD | 8,460.00 USD | 1,760.00 USD | 0.00 USD |
| `7D` | `319.60` | 4,480,000.00 USD | 4,480,000.00 USD | 0.00 USD | 8,460.00 USD | 1,760.00 USD | 0.00 USD |
| `1D` | `320.00` | 4,470,000.00 USD | 4,470,000.00 USD | 0.00 USD | 155.00 USD | 2,460.00 USD | 0.00 USD |
| `7D` | `320.00` | 4,480,000.00 USD | 4,480,000.00 USD | 0.00 USD | 155.00 USD | 2,460.00 USD | 0.00 USD |
| `1D` | `320.40` | 4,480,000.00 USD | 4,480,000.00 USD | 0.00 USD | 8,130.00 USD | 0.00 USD | 2,590.00 USD |
| `7D` | `320.40` | 4,490,000.00 USD | 4,490,000.00 USD | 0.00 USD | 8,130.00 USD | 0.00 USD | 2,590.00 USD |
| `1D` | `321.20` | 4,480,000.00 USD | 4,480,000.00 USD | 0.00 USD | 150.60 USD | 0.00 USD | 0.00 USD |
| `7D` | `321.20` | 4,490,000.00 USD | 4,490,000.00 USD | 0.00 USD | 150.60 USD | 0.00 USD | 0.00 USD |
| `1D` | `321.60` | 4,510,000.00 USD | 4,510,000.00 USD | 0.00 USD | 8,670.00 USD | 0.00 USD | 16,170.00 USD |
| `7D` | `321.60` | 4,510,000.00 USD | 4,510,000.00 USD | 0.00 USD | 8,670.00 USD | 0.00 USD | 16,170.00 USD |
| `1D` | `322.00` | 4,520,000.00 USD | 4,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 9,600.00 USD |
| `7D` | `322.00` | 4,520,000.00 USD | 4,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 9,600.00 USD |
| `1D` | `322.40` | 4,520,000.00 USD | 4,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 6,540.00 USD |
| `7D` | `322.40` | 4,530,000.00 USD | 4,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 6,540.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `LONGS_FLUSHED` | 16,500.00 USD | 0.00 USD | 16,500.00 USD | -16,500.00 USD | `2` | `2026-10-29 17:10:00 UTC - 2026-10-29 17:15:00 UTC` |
| `15m` | `LONGS_FLUSHED` | 16,500.00 USD | 0.00 USD | 16,500.00 USD | -16,500.00 USD | `2` | `2026-10-29 17:00:00 UTC - 2026-10-29 17:15:00 UTC` |
| `1h` | `LONGS_FLUSHED` | 16,500.00 USD | 0.00 USD | 16,500.00 USD | -16,500.00 USD | `2` | `2026-10-29 17:00:00 UTC - 2026-10-29 18:00:00 UTC` |
| `4h` | `LONGS_FLUSHED` | 16,500.00 USD | 0.00 USD | 16,500.00 USD | -16,500.00 USD | `2` | `2026-10-29 16:00:00 UTC - 2026-10-29 20:00:00 UTC` |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `317.59M` | Total OI Tokens: `1,099,268.6 BCH`
  * 1h OI Change: `-0.57%` | 4h OI Change: `+3.71%` | 24h OI Change: `-2.78%`
  * Exchange Breakdown: Binance=`94.27M` | Bybit=`40.77M` | OKX=`24.89M` | Hyperliquid=`8.18M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `3.38K` | Last 24h: `4.21K` | Last 3d: `81.66K` | Last 7d: `135.21K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `-0.0007%` | **USDT OKX** | `0.0002%` |
| **USDT Bybit** | `0.0100%` | **USDT KuCoin** | `0.0071%` |
| **USDT MEXC** | `-0.0006%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `0.0038%` | **USDT Bitget** | `0.0062%` |
| **CoinM Binance** | `0.0063%` | **CoinM OKX** | `0.0100%` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `BCH` | `43.94%` | `56.06%` | `0.78` | 3,640,000.00 USD |
| `15M` | `Binance` | `40.77%` | `59.23%` | `0.69` | 1,020,000.00 USD |
| `15M` | `OKX` | `28.01%` | `71.99%` | `0.39` | 463,170.00 USD |
| `15M` | `Bybit` | `27.88%` | `72.12%` | `0.39` | 362,090.00 USD |
| `15M` | `KuCoin` | `34.39%` | `65.61%` | `0.52` | 35,920.00 USD |
| `15M` | `Gate` | `50.84%` | `49.16%` | `1.03` | 529,610.00 USD |
| `15M` | `Bitget` | `39.2%` | `60.8%` | `0.64` | 54,190.00 USD |
| `15M` | `BingX` | `48.49%` | `51.51%` | `0.94` | 590,420.00 USD |
| `15M` | `MEXC` | `29.7%` | `70.3%` | `0.42` | 69,690.00 USD |
| `15M` | `Bitunix` | `33.23%` | `66.77%` | `0.50` | 57,520.00 USD |
| `15M` | `Hyperliquid` | `12.33%` | `87.67%` | `0.14` | 38,890.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `49.76%` | `50.24%` | `0.99` | 104,710.00 USD |
| `15M` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `WhiteBIT` | `90.24%` | `9.76%` | `9.25` | 294,160.00 USD |
| `15M` | `HTX` | `8.5%` | `91.5%` | `0.09` | 5,080.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `2.58%` | `97.42%` | `0.03` | 11,120.00 USD |
| `15M` | `Aster` | `0.69%` | `99.31%` | `0.01` | 1,590.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `0%` | `100%` | `0.00` | 228.39 USD |
| `15M` | `Whale Positions` | `40.77%` | `59.23%` | `0.69` | 1,020,000.00 USD |
| `15M` | `Global Accounts` | `43.94%` | `56.06%` | `0.78` | 3,640,000.00 USD |
| `1H` | `BCH` | `45.89%` | `54.11%` | `0.85` | 13,880,000.00 USD |
| `1H` | `Binance` | `39.04%` | `60.96%` | `0.64` | 4,050,000.00 USD |
| `1H` | `OKX` | `38.84%` | `61.16%` | `0.64` | 1,390,000.00 USD |
| `1H` | `Bybit` | `41.03%` | `58.97%` | `0.70` | 1,020,000.00 USD |
| `1H` | `KuCoin` | `41.59%` | `58.41%` | `0.71` | 145,220.00 USD |
| `1H` | `Gate` | `49.68%` | `50.32%` | `0.99` | 2,050,000.00 USD |
| `1H` | `Bitget` | `37.32%` | `62.68%` | `0.60` | 173,300.00 USD |
| `1H` | `BingX` | `39.93%` | `60.07%` | `0.66` | 2,420,000.00 USD |
| `1H` | `MEXC` | `33.67%` | `66.33%` | `0.51` | 281,010.00 USD |
| `1H` | `Bitunix` | `28.9%` | `71.1%` | `0.41` | 229,570.00 USD |
| `1H` | `Hyperliquid` | `19.79%` | `80.21%` | `0.25` | 88,010.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `49.62%` | `50.38%` | `0.98` | 526,450.00 USD |
| `1H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `WhiteBIT` | `92.31%` | `7.69%` | `12.00` | 1,340,000.00 USD |
| `1H` | `HTX` | `12.95%` | `87.05%` | `0.15` | 8,580.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `8.81%` | `91.19%` | `0.10` | 121,030.00 USD |
| `1H` | `Aster` | `78.21%` | `21.79%` | `3.59` | 47,200.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `38.29%` | `61.71%` | `0.62` | 2,260.00 USD |
| `1H` | `Whale Positions` | `39.04%` | `60.96%` | `0.64` | 4,050,000.00 USD |
| `1H` | `Global Accounts` | `45.89%` | `54.11%` | `0.85` | 13,880,000.00 USD |
| `4H` | `BCH` | `47.34%` | `52.66%` | `0.90` | 62,280,000.00 USD |
| `4H` | `Binance` | `48.98%` | `51.02%` | `0.96` | 19,000,000.00 USD |
| `4H` | `OKX` | `47.15%` | `52.85%` | `0.89` | 7,210,000.00 USD |
| `4H` | `Bybit` | `50.98%` | `49.02%` | `1.04` | 4,960,000.00 USD |
| `4H` | `KuCoin` | `49.82%` | `50.18%` | `0.99` | 491,340.00 USD |
| `4H` | `Gate` | `53.61%` | `46.39%` | `1.16` | 8,430,000.00 USD |
| `4H` | `Bitget` | `56.6%` | `43.4%` | `1.30` | 1,250,000.00 USD |
| `4H` | `BingX` | `36.47%` | `63.53%` | `0.57` | 9,830,000.00 USD |
| `4H` | `MEXC` | `51.85%` | `48.15%` | `1.08` | 1,160,000.00 USD |
| `4H` | `Bitunix` | `48.68%` | `51.32%` | `0.95` | 1,090,000.00 USD |
| `4H` | `Hyperliquid` | `66.29%` | `33.71%` | `1.97` | 389,650.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `49.4%` | `50.6%` | `0.98` | 2,390,000.00 USD |
| `4H` | `Crypto.com` | `25.18%` | `74.82%` | `0.34` | 0.00 USD |
| `4H` | `WhiteBIT` | `0.23%` | `99.77%` | `0.00` | 5,560,000.00 USD |
| `4H` | `HTX` | `43.95%` | `56.05%` | `0.78` | 104,090.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `46.72%` | `53.28%` | `0.88` | 264,070.00 USD |
| `4H` | `Aster` | `52.52%` | `47.48%` | `1.11` | 125,850.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `48.7%` | `51.3%` | `0.95` | 23,310.00 USD |
| `4H` | `Whale Positions` | `48.98%` | `51.02%` | `0.96` | 19,000,000.00 USD |
| `4H` | `Global Accounts` | `47.34%` | `52.66%` | `0.90` | 62,280,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5:00 UTC` | `282.37` | `282.12` | `282.37` | `283.59` | `281.01` | 1,480,281.16 USD | 655,283.20 USD | 824,997.96 USD | -169,714.77 USD | `-11.47%` | `11B / 29S` |
| `0:00 UTC` | `284.01` | `283.28` | `284.01` | `284.37` | `282.31` | 1,263,881.44 USD | 616,993.98 USD | 646,887.46 USD | -29,893.48 USD | `-2.37%` | `20B / 16S` |
| `5:00 UTC` | `283.25` | `283.21` | `283.25` | `284.31` | `282.15` | 1,057,540.43 USD | 470,059.99 USD | 587,480.45 USD | -117,420.46 USD | `-11.10%` | `22B / 38S` |
| `0:00 UTC` | `283.98` | `283.94` | `283.98` | `284.82` | `282.24` | 1,354,856.78 USD | 789,515.89 USD | 565,340.89 USD | 224,175.00 USD | `+16.55%` | `34B / 15S` |
| `5:00 UTC` | `287.25` | `286.10` | `287.25` | `288.25` | `284.09` | 2,685,023.61 USD | 1,441,619.22 USD | 1,243,404.38 USD | 198,214.84 USD | `+7.38%` | `22B / 9S` |
| `0:00 UTC` | `290.18` | `290.75` | `290.18` | `293.42` | `286.94` | 7,434,288.46 USD | 2,860,219.97 USD | 4,574,068.49 USD | -1,713,848.52 USD | `-23.05%` | `22B / 26S` |
| `5:00 UTC` | `290.33` | `290.07` | `290.33` | `290.97` | `289.12` | 2,596,782.25 USD | 1,062,961.61 USD | 1,533,820.64 USD | -470,859.04 USD | `-18.13%` | `12B / 36S` |
| `0:00 UTC` | `287.31` | `288.38` | `287.31` | `290.09` | `287.09` | 2,309,907.78 USD | 1,171,627.08 USD | 1,138,280.70 USD | 33,346.39 USD | `+1.44%` | `26B / 14S` |
| `5:00 UTC` | `288.66` | `288.97` | `288.66` | `290.08` | `287.98` | 1,528,178.86 USD | 694,047.00 USD | 834,131.86 USD | -140,084.86 USD | `-9.17%` | `9B / 26S` |
| `0:00 UTC` | `288.24` | `289.03` | `288.24` | `290.24` | `288.04` | 1,130,887.04 USD | 694,692.32 USD | 436,194.72 USD | 258,497.61 USD | `+22.86%` | `28B / 7S` |

- **CoinGlass Algorithmic Footprint Signals Table (25_CoinGlass_Footprint_Signals.parquet)**:
| Time | Timeframe | Signal Type | Bias | Headline | Price Level | Absorbed Vol (USD) | Bar Delta (USD) |
|:---:|:---:|:---:|:---:|:---|:---:|:---:|:---:|
| `10-28 19:52` | `Range 1` | `Divergence` | **`BEARISH`** | Rally without taker buying | `294.56` | 0.00 USD | 0.00 USD |
| `10-28 19:31` | `Range 1` | `Bull div` | **`BULLISH`** | Lower low, higher Cumulative Delta | `293.50` | 3,900.00 USD | 0.00 USD |
| `10-28 18:42` | `Range 1` | `Divergence` | **`BULLISH`** | Drop without taker selling | `295.29` | 0.00 USD | 0.00 USD |
| `10-28 16:40` | `Range 1` | `Trapped shorts` | **`BULLISH`** | Failed breakdown | `296.45` | 2,100.00 USD | 0.00 USD |
| `10-28 16:31` | `Range 1` | `Absorption` | **`BEARISH`** | Buying absorbed at the high | `299.73` | 1,000.00 USD | 0.00 USD |
| `10-28 15:58` | `Range 1` | `Absorption` | **`BEARISH`** | Buying absorbed at the high | `300.99` | 0.00 USD | 0.00 USD |
| `10-28 15:25` | `Volume 10K BCH` | `Exhaustion` | **`BEARISH`** | Buyer exhaustion | `304.75` | 0.00 USD | 0.00 USD |
| `10-28 12:36` | `Range 1` | `Absorption` | **`BULLISH`** | Selling absorbed at the low | `297.11` | 0.00 USD | 0.00 USD |
| `10-28 11:50` | `Volume 10K BCH` | `Absorption` | **`BEARISH`** | Buying absorbed at the high | `299.58` | 1,500.00 USD | 0.00 USD |
| `10-28 11:49` | `Range 1` | `Divergence` | **`BULLISH`** | Drop without taker selling | `298.39` | 0.00 USD | 0.00 USD |
| `10-28 11:49` | `Range 1` | `Absorption` | **`BEARISH`** | Buying absorbed at the high | `299.58` | 1,100.00 USD | 0.00 USD |
| `10-28 11:32` | `Range 1` | `Absorption` | **`BULLISH`** | Selling absorbed at the low | `298.10` | 0.00 USD | 0.00 USD |
| `10-28 11:24` | `Range 1` | `Absorption` | **`BEARISH`** | Buying absorbed at the high | `299.42` | 0.00 USD | 0.00 USD |
| `10-28 10:10` | `Range 1` | `Absorption` | **`BULLISH`** | Selling absorbed at the low | `297.64` | 1,000.00 USD | 0.00 USD |
| `10-28 10:10` | `Range 1` | `Bear div` | **`BEARISH`** | Higher high, lower Cumulative Delta | `299.34` | 1,200.00 USD | 0.00 USD |
| `10-28 09:12` | `Range 1` | `Absorption` | **`BULLISH`** | Selling absorbed at the low | `297.13` | 0.00 USD | 0.00 USD |
| `10-28 08:27` | `Range 1` | `Exhaustion` | **`BEARISH`** | Buyer exhaustion | `297.20` | 0.00 USD | 0.00 USD |
| `10-28 07:51` | `Range 1` | `Bull div` | **`BULLISH`** | Lower low, higher Cumulative Delta | `293.25` | 2,500.00 USD | 0.00 USD |
| `10-28 07:41` | `Range 1` | `Absorption` | **`BEARISH`** | Buying absorbed at the high | `295.18` | 0.00 USD | 0.00 USD |
| `10-28 06:40` | `Volume 10K BCH` | `Absorption` | **`BULLISH`** | Selling absorbed at the low | `293.94` | 2,400.00 USD | 0.00 USD |
| `10-28 06:32` | `Range 1` | `Exhaustion` | **`BULLISH`** | Seller exhaustion | `293.42` | 0.00 USD | 0.00 USD |
| `10-28 06:21` | `Range 1` | `Exhaustion` | **`BULLISH`** | Seller exhaustion | `293.97` | 0.00 USD | 0.00 USD |

- **12-Horizon Macro Capital Netflows Table (2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet)**:
| Horizon | Spot Netflow (USD) | Futures Netflow (USD) | Institutional Bias |
|:---:|:---:|:---:|:---:|
| `5m` | 92,040.00 USD | -48,510.00 USD | **`ACCUMULATION`** |
| `15m` | 132,550.00 USD | 455,740.00 USD | **`ACCUMULATION`** |
| `30m` | 68,810.00 USD | 55,640.00 USD | **`ACCUMULATION`** |
| `1h` | -49,090.00 USD | -1,860,000.00 USD | **`DISTRIBUTION`** |
| `2h` | -43,510.00 USD | -3,390,000.00 USD | **`DISTRIBUTION`** |
| `4h` | 392,660.00 USD | -1,900,000.00 USD | **`DISTRIBUTION`** |
| `6h` | 217,930.00 USD | -1,130,000.00 USD | **`DISTRIBUTION`** |
| `8h` | 248,700.00 USD | -2,420,000.00 USD | **`DISTRIBUTION`** |
| `12h` | 269,340.00 USD | -3,960,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -1,100,000.00 USD | -8,080,000.00 USD | **`DISTRIBUTION`** |
| `1w` | 351,450.00 USD | -12,350,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -13,450,000.00 USD | -136,340,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+92.04K` | 15m=`+132.55K` | 1h=`-49.09K` | 24h=`-1.10M`
* Futures Capital Netflows: 5m=`-48.51K` | 15m=`+455.74K` | 1h=`-1.86M` | 24h=`-8.08M`
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
  * `2026-10-29 22:05:54 IST`: [fxstreet.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:39:54 IST`: [ForexFactory] - (Sentiment: `Neutral`)
  * `2026-10-29 22:39:54 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-29 22:39:54 IST`: [youtube.com/bankofcanadaofficial] - (Sentiment: `Neutral`)
  * `2026-10-29 22:39:54 IST`: [notayesmanseconomics.wordpress.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:38:54 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:38:54 IST`: [breakingthenews.net] - (Sentiment: `Neutral`)
  * `2026-10-29 22:38:54 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-29 19:40:54 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-29 19:40:54 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-29 19:40:54 IST`: [youtube.com/ecbeuro] - (Sentiment: `Neutral`)
  * `2026-10-29 19:40:54 IST`: [ecb.europa.eu] - (Sentiment: `Neutral`)
  * `2026-10-29 18:40:54 IST`: [zerohedge.com] - (Sentiment: `Neutral`)
  * `2026-10-29 18:40:54 IST`: [dol.gov] - (Sentiment: `Neutral`)
  * `2026-10-29 18:40:54 IST`: [bea.gov] - (Sentiment: `Neutral`)


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
  * Execution Entry: `276.52` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `273.04` (Risk Distance: `3.48` pts)
  * +2.5R Take Profit: `285.22`
  * Mathematical Lot Sizing: **`2.87 lots`** (Nominal Risk = `0.10 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `286.47` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `289.95` (Risk Distance: `3.48` pts)
  * +2.5R Take Profit: `277.77`
  * Mathematical Lot Sizing: **`2.87 lots`** (Nominal Risk = `0.10 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`PASSIVE_MAKER_LIMIT_ARMED`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`291.77`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
