# 🏛️ SOVEREIGN CANDIDATE DOSSIER: BCH
**Canonical Key**: `BCH` | **Broker Instrument**: `BCHUSD.p` | **Asset Class**: `Crypto PoW`
**Timestamp**: `2026-10-29 23:37:48 IST` (`2026-10-29 18:07:48 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `288.76` | **Live Ask Quote**: `289.44` | **Mid Price**: `289.10`
- **Spread Points**: `680.00` | **Spread BPS**: `23.52 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `282.36` | VWAP Z-Score: `+1.46` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `2.34` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `62.75` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `294.71` | Lower -3.00σ Band: `270.01`
  * Upper +2.51σ Band: `292.69` | Lower -2.51σ Band: `272.03`
  * Upper +2.01σ Band: `290.63` | Lower -2.01σ Band: `274.08`
  * Upper +2.00σ Band: `290.59` | Lower -2.00σ Band: `274.13`
  * Upper +1.28σ Band: `287.63` | Lower -1.28σ Band: `277.09`
  * Upper +1.00σ Band: `286.47` | Lower -1.00σ Band: `278.24`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`287.83` | EMA-20=`285.44` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`283.27` (Slope: `+0.0000`) | EMA-100=`284.05`
  * Institutional Anchors: EMA-144=`284.61` | EMA-200=`284.45` (Slope: `+0.1351`) | EMA-233=`284.71`
- **Range Boundaries**: 24H High=`292.96` | 24H Low=`274.76` | Weekly High=`304.16` | Weekly Low=`274.76`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `287.44` (Distance: `+0.61%`)
  * Point of Control (POC) = `278.70` (Distance: `+3.77%`)
  * Value Area Low (VAL) = `276.52` (Distance: `+4.59%`)
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
  * Golden Pocket Zone (0.618 - 0.650): `287.94` - `290.26`
  * Optimal Trade Entry (OTE 0.705): `289.68`
  * Structural Invalidation Anchor (0.786): `291.41`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `287.12` | `288.90` | `287.12` | `288.89` | `987` | 284,210.67 USD | 106,063.13 USD | `+37.32%` | -3,829,285.17 USD | `+0.88` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `5m` | `288.88` | `289.41` | `288.28` | `289.05` | `1,761` | 508,853.59 USD | 168,134.44 USD | `+33.04%` | -3,661,150.73 USD | `+1.25` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `5m` | `289.05` | `289.23` | `288.93` | `289.18` | `96` | 27,862.34 USD | 406.01 USD | `+1.46%` | -3,660,744.72 USD | `-0.09` | **`BULLISH`** | `NEUTRAL CHOP` |
| `15m` | `291.01` | `291.58` | `287.80` | `288.74` | `6,559` | 1,897,766.44 USD | -242,155.26 USD | `-12.76%` | -3,550,543.72 USD | `-0.50` | **`BEARISH`** | `DELTA ALIGNED` |
| `15m` | `288.74` | `289.31` | `286.48` | `288.89` | `6,651` | 1,912,559.47 USD | -50,347.76 USD | `-2.63%` | -3,600,891.48 USD | `-0.05` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `15m` | `288.88` | `289.41` | `288.28` | `289.08` | `1,855` | 536,094.84 USD | 168,252.43 USD | `+31.38%` | -3,432,639.04 USD | `+0.44` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `1h` | `287.97` | `293.41` | `286.92` | `288.48` | `47,822` | 13,869,157.35 USD | -2,291,446.03 USD | `-16.52%` | -3,009,893.89 USD | `-2.84` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `1h` | `288.48` | `291.58` | `286.48` | `288.89` | `23,176` | 6,696,574.59 USD | 177,926.21 USD | `+2.66%` | -2,831,967.68 USD | `+0.54` | **`BULLISH`** | `NEUTRAL CHOP` |
| `1h` | `288.88` | `289.41` | `288.28` | `289.18` | `1,858` | 536,715.93 USD | 168,540.45 USD | `+31.40%` | -2,663,427.23 USD | `+0.51` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `4h` | `278.88` | `282.00` | `277.22` | `279.37` | `40,922` | 11,454,296.89 USD | -658,851.13 USD | `-5.75%` | -2,731,740.69 USD | `+0.02` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `279.38` | `288.24` | `277.49` | `287.96` | `74,069` | 20,847,128.37 USD | 1,744,736.30 USD | `+8.37%` | -987,004.39 USD | `+1.23` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `287.97` | `293.41` | `286.48` | `289.18` | `72,855` | 21,102,447.87 USD | -1,944,979.36 USD | `-9.22%` | -2,931,983.76 USD | `-0.92` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `288.93` | `289.90` | `275.10` | `277.35` | `99,418` | 27,984,350.92 USD | -2,870,393.66 USD | `-10.26%` | -1,919,042.18 USD | `-1.00` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `277.35` | `282.39` | `276.59` | `278.88` | `47,861` | 13,383,109.09 USD | -153,847.38 USD | `-1.15%` | -2,072,889.56 USD | `+0.33` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `278.88` | `282.00` | `277.22` | `279.37` | `40,922` | 11,454,296.89 USD | -658,851.13 USD | `-5.75%` | -2,731,740.69 USD | `+0.02` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `279.38` | `288.24` | `277.49` | `287.96` | `74,069` | 20,847,128.37 USD | 1,744,736.30 USD | `+8.37%` | -987,004.39 USD | `+1.23` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `287.97` | `293.41` | `286.48` | `289.18` | `72,855` | 21,102,447.87 USD | -1,944,979.36 USD | `-9.22%` | -2,931,983.76 USD | `-0.92` | **`BEARISH`** | `BEARISH ABSORPTION` |

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
| --- | **`289.10`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

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
| `1952` | `0x12d2...f97f` | `LONG` | 1,049,807.55 USD | `3,627,243,000,000.00` | `303.26` | `289.50` | `0.000000` | -50,191.79 USD | `-4.78%` | `10X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `291.49` | 12,466.74 USD | `-` | `NEWS_INTEL` | `-` | #BCH Whale BUY: 12.47K USD at 291.4900 USD [API] | `2026-10-27 22:29:58` |
| `ANNOUNCEMENT` | `INFO` | `291.47` | 5,973.09 USD | `-` | `NEWS_INTEL` | `-` | #BCH Whale BUY: 5.97K USD at 291.4700 USD [API] | `2026-10-27 22:29:58` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`295.70` (Vol: 152,600.00 USD, Dist: `+2.32%`) | Long MP=`271.76` (Vol: 159,600.00 USD, Dist: `--5.96%`)
  * 48H Horizon: Short MP=`295.64` (Vol: 196,600.00 USD, Dist: `+2.30%`) | Long MP=`271.85` (Vol: 166,000.00 USD, Dist: `--5.93%`)
  * 3D Horizon: Short MP=`295.64` (Vol: 196,600.00 USD, Dist: `+2.30%`) | Long MP=`274.36` (Vol: 203,100.00 USD, Dist: `--5.06%`)
  * 7D Horizon: Short MP=`294.37` (Vol: 208,300.00 USD, Dist: `+1.86%`) | Long MP=`263.68` (Vol: 297,200.00 USD, Dist: `--8.76%`)
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
| `7D` | `Long Liquidation` | `248.30` | 18,760,000.00 USD | 18,760,000.00 USD | 8,700.00 USD | 3,270.00 USD | 10,110.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `248.70` | 18,740,000.00 USD | 18,740,000.00 USD | 43,550.00 USD | 17,040.00 USD | 28,350.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `249.10` | 18,650,000.00 USD | 18,650,000.00 USD | 16,180.00 USD | 29,320.00 USD | 11,540.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `249.50` | 18,600,000.00 USD | 18,600,000.00 USD | 42,290.00 USD | 32,910.00 USD | 8,340.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `249.90` | 18,510,000.00 USD | 18,510,000.00 USD | 44,840.00 USD | 14,160.00 USD | 35,630.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `250.30` | 18,420,000.00 USD | 18,420,000.00 USD | 18,520.00 USD | 38,250.00 USD | 3,480.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `250.50` | 1,330.00 USD | 188,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `250.70` | 18,360,000.00 USD | 18,360,000.00 USD | 31,550.00 USD | 36,830.00 USD | 21,190.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `251.10` | 18,270,000.00 USD | 18,270,000.00 USD | 29,390.00 USD | 49,280.00 USD | 12,010.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `251.50` | 18,180,000.00 USD | 18,180,000.00 USD | 17,130.00 USD | 61,120.00 USD | 22,920.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `251.50` | 268.35 USD | 187,380.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `251.90` | 18,080,000.00 USD | 18,080,000.00 USD | 74,710.00 USD | 48,150.00 USD | 43,130.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `252.30` | 17,910,000.00 USD | 17,910,000.00 USD | 51,600.00 USD | 23,430.00 USD | 12,750.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `252.50` | 1,030.00 USD | 187,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `252.70` | 17,820,000.00 USD | 17,820,000.00 USD | 43,080.00 USD | 19,890.00 USD | 15,320.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `253.10` | 17,740,000.00 USD | 17,740,000.00 USD | 13,370.00 USD | 25,630.00 USD | 4,290.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `253.50` | 17,700,000.00 USD | 17,700,000.00 USD | 24,970.00 USD | 34,890.00 USD | 50,520.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `253.90` | 17,590,000.00 USD | 17,590,000.00 USD | 4,930.00 USD | 29,760.00 USD | 21,980.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `254.30` | 17,530,000.00 USD | 17,530,000.00 USD | 44,770.00 USD | 28,990.00 USD | 3,830.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `254.50` | 11,650.00 USD | 186,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `254.70` | 17,460,000.00 USD | 17,460,000.00 USD | 23,800.00 USD | 12,800.00 USD | 12,580.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `255.10` | 17,410,000.00 USD | 17,410,000.00 USD | 14,770.00 USD | 11,150.00 USD | 31,750.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `255.50` | 17,350,000.00 USD | 17,350,000.00 USD | 51,410.00 USD | 978.50 USD | 26,290.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `255.50` | 3,660.00 USD | 174,440.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `255.90` | 17,270,000.00 USD | 17,270,000.00 USD | 16,050.00 USD | 30,780.00 USD | 39,360.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `256.30` | 17,190,000.00 USD | 17,190,000.00 USD | 88,910.00 USD | 21,560.00 USD | 29,760.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `256.50` | 2,480.00 USD | 170,780.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `256.70` | 17,040,000.00 USD | 17,040,000.00 USD | 31,480.00 USD | 14,630.00 USD | 23,090.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `257.10` | 16,980,000.00 USD | 16,980,000.00 USD | 27,360.00 USD | 3,120.00 USD | 47,830.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `257.50` | 8,100,000.00 USD | 8,100,000.00 USD | 4,510.00 USD | 5,710.00 USD | 8,410.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `257.50` | 16,900,000.00 USD | 16,900,000.00 USD | 27,690.00 USD | 1,950.00 USD | 10,260.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `257.50` | 366.42 USD | 168,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `257.90` | 8,080,000.00 USD | 8,080,000.00 USD | 161.87 USD | 991.50 USD | 16,890.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `257.90` | 16,860,000.00 USD | 16,860,000.00 USD | 35,520.00 USD | 5,470.00 USD | 7,940.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `258.30` | 8,060,000.00 USD | 8,060,000.00 USD | 1,370.00 USD | 8,380.00 USD | 13,230.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `258.30` | 16,810,000.00 USD | 16,810,000.00 USD | 102,130.00 USD | 52,010.00 USD | 30,830.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `258.50` | 176.56 USD | 167,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `258.70` | 8,040,000.00 USD | 8,040,000.00 USD | 5,020.00 USD | 5,060.00 USD | 11,840.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `258.70` | 16,620,000.00 USD | 16,620,000.00 USD | 76,500.00 USD | 4,180.00 USD | 36,910.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `259.10` | 8,020,000.00 USD | 8,020,000.00 USD | 24,070.00 USD | 9,900.00 USD | 10,720.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `259.10` | 16,510,000.00 USD | 16,510,000.00 USD | 19,700.00 USD | 15,870.00 USD | 26,410.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `259.50` | 7,970,000.00 USD | 7,970,000.00 USD | 4,620.00 USD | 2,470.00 USD | 3,360.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `259.50` | 16,440,000.00 USD | 16,440,000.00 USD | 2,100.00 USD | 34,490.00 USD | 91.84 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `259.90` | 7,960,000.00 USD | 7,960,000.00 USD | 12,820.00 USD | 17,870.00 USD | 23,400.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `259.90` | 16,410,000.00 USD | 16,410,000.00 USD | 18,950.00 USD | 9,160.00 USD | 57.42 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `260.30` | 7,910,000.00 USD | 7,910,000.00 USD | 3,100.00 USD | 9,440.00 USD | 822.76 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `260.30` | 16,380,000.00 USD | 16,380,000.00 USD | 23,380.00 USD | 9,140.00 USD | 8,920.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `260.50` | 3,860.00 USD | 167,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `260.70` | 7,890,000.00 USD | 7,890,000.00 USD | 5,040.00 USD | 15,040.00 USD | 7,760.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `260.70` | 16,340,000.00 USD | 16,340,000.00 USD | 15,620.00 USD | 47,200.00 USD | 60,210.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `261.10` | 7,870,000.00 USD | 7,870,000.00 USD | 12,720.00 USD | 6,900.00 USD | 6,670.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `261.10` | 16,210,000.00 USD | 16,210,000.00 USD | 6,540.00 USD | 33,150.00 USD | 16,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `261.50` | 7,840,000.00 USD | 7,840,000.00 USD | 8,750.00 USD | 14,260.00 USD | 2.10 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `261.50` | 16,160,000.00 USD | 16,160,000.00 USD | 16,390.00 USD | 36,570.00 USD | 6,560.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `261.90` | 7,820,000.00 USD | 7,820,000.00 USD | 4,920.00 USD | 4,330.00 USD | 10,920.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `261.90` | 16,100,000.00 USD | 16,100,000.00 USD | 54,070.00 USD | 37,990.00 USD | 46,200.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `262.30` | 7,800,000.00 USD | 7,800,000.00 USD | 8,640.00 USD | 626.24 USD | 5,590.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `262.30` | 15,960,000.00 USD | 15,960,000.00 USD | 43,400.00 USD | 47,100.00 USD | 1.95 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `262.50` | 1,970.00 USD | 163,890.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `262.70` | 7,780,000.00 USD | 7,780,000.00 USD | 150.60 USD | 1,190.00 USD | 12.23 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `262.70` | 15,870,000.00 USD | 15,870,000.00 USD | 56,340.00 USD | 37,260.00 USD | 26,770.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `263.10` | 7,780,000.00 USD | 7,780,000.00 USD | 8,670.00 USD | 571.81 USD | 7,500.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `263.10` | 15,750,000.00 USD | 15,750,000.00 USD | 37,610.00 USD | 14,780.00 USD | 37,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `263.50` | 7,760,000.00 USD | 7,760,000.00 USD | 560.34 USD | 839.81 USD | 24,820.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `263.50` | 15,660,000.00 USD | 15,660,000.00 USD | 177,230.00 USD | 82,460.00 USD | 25,270.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `263.90` | 7,740,000.00 USD | 7,740,000.00 USD | 746.44 USD | 825.92 USD | 3.09 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `263.90` | 15,380,000.00 USD | 15,380,000.00 USD | 198,210.00 USD | 33,270.00 USD | 51,730.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `264.30` | 7,740,000.00 USD | 7,740,000.00 USD | 1,860.00 USD | 647.93 USD | 9.06 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `264.30` | 15,090,000.00 USD | 15,090,000.00 USD | 41,340.00 USD | 44,170.00 USD | 10,240.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `264.50` | 280.37 USD | 161,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `264.70` | 7,730,000.00 USD | 7,730,000.00 USD | 28,300.00 USD | 615.20 USD | 36,650.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `264.70` | 15,000,000.00 USD | 15,000,000.00 USD | 54,310.00 USD | 68,740.00 USD | 43,280.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `265.10` | 7,670,000.00 USD | 7,670,000.00 USD | 20,980.00 USD | 8,870.00 USD | 15,700.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `265.10` | 14,830,000.00 USD | 14,830,000.00 USD | 104,580.00 USD | 58,410.00 USD | 87,140.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `265.50` | 7,620,000.00 USD | 7,620,000.00 USD | 10,540.00 USD | 11,920.00 USD | 67,100.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `265.50` | 14,580,000.00 USD | 14,580,000.00 USD | 65,360.00 USD | 53,690.00 USD | 79,040.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `265.50` | 121,910.00 USD | 161,640.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `265.90` | 7,530,000.00 USD | 7,530,000.00 USD | 14,110.00 USD | 11,970.00 USD | 19.98 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `265.90` | 14,380,000.00 USD | 14,380,000.00 USD | 60,500.00 USD | 86,890.00 USD | 29,610.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `266.30` | 7,510,000.00 USD | 7,510,000.00 USD | 32,850.00 USD | 245.13 USD | 5,010.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `266.30` | 14,210,000.00 USD | 14,210,000.00 USD | 197,950.00 USD | 158,200.00 USD | 71,060.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `266.70` | 7,470,000.00 USD | 7,470,000.00 USD | 14,960.00 USD | 3,340.00 USD | 3,710.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `266.70` | 13,780,000.00 USD | 13,780,000.00 USD | 91,720.00 USD | 53,860.00 USD | 135,810.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `267.10` | 7,450,000.00 USD | 7,450,000.00 USD | 29,020.00 USD | 6,580.00 USD | 10,110.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `267.10` | 13,500,000.00 USD | 13,500,000.00 USD | 122,460.00 USD | 177,330.00 USD | 68,830.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `267.50` | 7,400,000.00 USD | 7,400,000.00 USD | 12,110.00 USD | 26,590.00 USD | 21.49 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `267.50` | 13,130,000.00 USD | 13,130,000.00 USD | 106,550.00 USD | 176,700.00 USD | 65,720.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `267.50` | 1,490.00 USD | 39,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `267.90` | 7,360,000.00 USD | 7,360,000.00 USD | 113,380.00 USD | 120,840.00 USD | 45,380.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `267.90` | 12,780,000.00 USD | 12,780,000.00 USD | 202,290.00 USD | 214,120.00 USD | 99,040.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `268.30` | 7,080,000.00 USD | 7,080,000.00 USD | 39,130.00 USD | 98,350.00 USD | 26,540.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `268.30` | 12,260,000.00 USD | 12,260,000.00 USD | 118,790.00 USD | 256,410.00 USD | 74,420.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `268.50` | 7,020.00 USD | 38,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `268.70` | 6,920,000.00 USD | 6,920,000.00 USD | 97,080.00 USD | 84,960.00 USD | 58,760.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `268.70` | 11,810,000.00 USD | 11,810,000.00 USD | 190,630.00 USD | 159,680.00 USD | 85,850.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `269.10` | 6,680,000.00 USD | 6,680,000.00 USD | 50,070.00 USD | 22,910.00 USD | 16,360.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `269.10` | 11,380,000.00 USD | 11,380,000.00 USD | 285,230.00 USD | 182,200.00 USD | 89,950.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `269.50` | 6,590,000.00 USD | 6,590,000.00 USD | 31,660.00 USD | 6,030.00 USD | 8,780.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `269.50` | 10,820,000.00 USD | 10,820,000.00 USD | 145,740.00 USD | 91,670.00 USD | 41,400.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `269.50` | 11,700.00 USD | 31,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `269.90` | 6,540,000.00 USD | 6,540,000.00 USD | 33,840.00 USD | 43,640.00 USD | 13,070.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `269.90` | 10,540,000.00 USD | 10,540,000.00 USD | 79,230.00 USD | 94,580.00 USD | 13,190.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `270.30` | 6,450,000.00 USD | 6,450,000.00 USD | 109,220.00 USD | 64,910.00 USD | 128,910.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `270.30` | 10,350,000.00 USD | 10,350,000.00 USD | 121,790.00 USD | 159,170.00 USD | 175,150.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `270.70` | 6,150,000.00 USD | 6,150,000.00 USD | 52,010.00 USD | 39,890.00 USD | 1,670.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `270.70` | 9,900,000.00 USD | 9,900,000.00 USD | 286,050.00 USD | 119,110.00 USD | 158,400.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `271.10` | 6,060,000.00 USD | 6,060,000.00 USD | 40,150.00 USD | 34,010.00 USD | 139,870.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `271.10` | 9,340,000.00 USD | 9,340,000.00 USD | 168,820.00 USD | 123,340.00 USD | 81,840.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `271.50` | 5,840,000.00 USD | 5,840,000.00 USD | 28,220.00 USD | 37,420.00 USD | 15,540.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `271.50` | 8,960,000.00 USD | 8,960,000.00 USD | 170,160.00 USD | 103,050.00 USD | 86,690.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `271.50` | 1,000.00 USD | 19,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `271.90` | 5,760,000.00 USD | 5,760,000.00 USD | 139,230.00 USD | 37,570.00 USD | 55,780.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `271.90` | 8,600,000.00 USD | 8,600,000.00 USD | 394,890.00 USD | 60,710.00 USD | 41,630.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `272.30` | 5,530,000.00 USD | 5,530,000.00 USD | 66,650.00 USD | 15,920.00 USD | 17,040.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `272.30` | 8,100,000.00 USD | 8,100,000.00 USD | 240,200.00 USD | 100,770.00 USD | 128,120.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `272.70` | 5,430,000.00 USD | 5,430,000.00 USD | 76,380.00 USD | 36,390.00 USD | 43,960.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `272.70` | 7,630,000.00 USD | 7,630,000.00 USD | 107,310.00 USD | 286,440.00 USD | 67,210.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `273.10` | 5,270,000.00 USD | 5,270,000.00 USD | 89,480.00 USD | 87,000.00 USD | 6,990.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `273.10` | 7,170,000.00 USD | 7,170,000.00 USD | 223,720.00 USD | 79,710.00 USD | 86,920.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `273.50` | 5,090,000.00 USD | 5,090,000.00 USD | 225,140.00 USD | 234,890.00 USD | 95,400.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `273.50` | 6,780,000.00 USD | 6,780,000.00 USD | 255,770.00 USD | 331,010.00 USD | 212,650.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `273.90` | 4,530,000.00 USD | 4,530,000.00 USD | 95,740.00 USD | 221,690.00 USD | 85,050.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `273.90` | 5,980,000.00 USD | 5,980,000.00 USD | 296,240.00 USD | 414,010.00 USD | 210,140.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `274.30` | 4,130,000.00 USD | 4,130,000.00 USD | 204,120.00 USD | 190,610.00 USD | 145,490.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `274.30` | 5,060,000.00 USD | 5,060,000.00 USD | 382,210.00 USD | 250,340.00 USD | 118,730.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `274.50` | 567.94 USD | 18,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `274.70` | 3,590,000.00 USD | 3,590,000.00 USD | 101,590.00 USD | 42,950.00 USD | 53,520.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `274.70` | 4,310,000.00 USD | 4,310,000.00 USD | 325,110.00 USD | 141,540.00 USD | 105,710.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `275.10` | 3,390,000.00 USD | 3,390,000.00 USD | 62,250.00 USD | 19,440.00 USD | 65,700.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `275.10` | 3,740,000.00 USD | 3,740,000.00 USD | 139,440.00 USD | 114,270.00 USD | 37,050.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `275.50` | 3,240,000.00 USD | 3,240,000.00 USD | 59,520.00 USD | 65,680.00 USD | 39,110.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `275.50` | 3,450,000.00 USD | 3,450,000.00 USD | 2,590.00 USD | 101,070.00 USD | 40,460.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `275.90` | 3,080,000.00 USD | 3,080,000.00 USD | 47,640.00 USD | 51,470.00 USD | 22,040.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `275.90` | 3,310,000.00 USD | 3,310,000.00 USD | 1,950.00 USD | 0.00 USD | 65.70 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `276.30` | 2,960,000.00 USD | 2,960,000.00 USD | 62,820.00 USD | 42,520.00 USD | 3,230.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `276.30` | 3,300,000.00 USD | 3,300,000.00 USD | 2,290.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `276.50` | 205.44 USD | 17,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `276.70` | 2,850,000.00 USD | 2,850,000.00 USD | 10,750.00 USD | 16,180.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `276.70` | 3,300,000.00 USD | 3,300,000.00 USD | 569.60 USD | 233.30 USD | 19,830.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `277.10` | 2,820,000.00 USD | 2,820,000.00 USD | 13,560.00 USD | 64,370.00 USD | 45,110.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `277.10` | 3,280,000.00 USD | 3,280,000.00 USD | 44,990.00 USD | 22,950.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `277.50` | 2,700,000.00 USD | 2,700,000.00 USD | 57,940.00 USD | 63,410.00 USD | 5.52 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `277.50` | 3,210,000.00 USD | 3,210,000.00 USD | 0.00 USD | 90,480.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `277.90` | 2,580,000.00 USD | 2,580,000.00 USD | 12,650.00 USD | 9,490.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `277.90` | 3,120,000.00 USD | 3,120,000.00 USD | 0.00 USD | 0.00 USD | 55,760.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `278.30` | 2,560,000.00 USD | 2,560,000.00 USD | 61,240.00 USD | 25,470.00 USD | 57,330.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `278.30` | 3,070,000.00 USD | 3,070,000.00 USD | 24,750.00 USD | 0.00 USD | 59,410.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `278.70` | 2,410,000.00 USD | 2,410,000.00 USD | 26,540.00 USD | 35,300.00 USD | 10,340.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `278.70` | 2,980,000.00 USD | 2,980,000.00 USD | 30,510.00 USD | 72,160.00 USD | 17,090.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `279.10` | 2,340,000.00 USD | 2,340,000.00 USD | 29,260.00 USD | 23,330.00 USD | 23,180.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `279.10` | 2,860,000.00 USD | 2,860,000.00 USD | 29,880.00 USD | 31,760.00 USD | 49.12 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `279.50` | 2,260,000.00 USD | 2,260,000.00 USD | 28,380.00 USD | 10,290.00 USD | 34,800.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `279.50` | 2,800,000.00 USD | 2,800,000.00 USD | 78,130.00 USD | 0.00 USD | 95,990.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `279.90` | 2,190,000.00 USD | 2,190,000.00 USD | 20,320.00 USD | 0.00 USD | 17,110.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `280.30` | 2,150,000.00 USD | 2,150,000.00 USD | 29,750.00 USD | 0.00 USD | 41,630.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `280.30` | 2,630,000.00 USD | 2,630,000.00 USD | 0.00 USD | 0.00 USD | 53.16 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `280.70` | 2,080,000.00 USD | 2,080,000.00 USD | 21,670.00 USD | 0.00 USD | 64,530.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `281.10` | 2,000,000.00 USD | 2,000,000.00 USD | 8,920.00 USD | 0.00 USD | 66,500.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `281.10` | 2,630,000.00 USD | 2,630,000.00 USD | 0.00 USD | 0.00 USD | 62,810.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `281.50` | 2,560,000.00 USD | 2,560,000.00 USD | 565.82 USD | 0.00 USD | 122,390.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `281.90` | 1,920,000.00 USD | 1,920,000.00 USD | 9,360.00 USD | 16,510.00 USD | 94,830.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `281.90` | 2,440,000.00 USD | 2,440,000.00 USD | 0.00 USD | 0.00 USD | 117,140.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `282.30` | 1,800,000.00 USD | 1,800,000.00 USD | 55,330.00 USD | 22,600.00 USD | 124,480.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `282.30` | 2,320,000.00 USD | 2,320,000.00 USD | 0.00 USD | 0.00 USD | 56,220.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `282.70` | 1,600,000.00 USD | 1,600,000.00 USD | 0.00 USD | 23,250.00 USD | 3,080.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `282.70` | 2,270,000.00 USD | 2,270,000.00 USD | 32,190.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `283.10` | 1,570,000.00 USD | 1,570,000.00 USD | 27,120.00 USD | 44,720.00 USD | 126,930.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `283.10` | 2,240,000.00 USD | 2,240,000.00 USD | 0.00 USD | 37,310.00 USD | 89,260.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `283.50` | 1,370,000.00 USD | 1,370,000.00 USD | 0.00 USD | 0.00 USD | 32,960.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `283.50` | 2,110,000.00 USD | 2,110,000.00 USD | 0.00 USD | 0.00 USD | 111,520.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `283.90` | 1,340,000.00 USD | 1,340,000.00 USD | 0.00 USD | 30,480.00 USD | 38,790.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `283.90` | 2,000,000.00 USD | 2,000,000.00 USD | 49,500.00 USD | 0.00 USD | 197,520.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `284.30` | 1,270,000.00 USD | 1,270,000.00 USD | 37,810.00 USD | 46,830.00 USD | 30,860.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `284.30` | 1,750,000.00 USD | 1,750,000.00 USD | 0.00 USD | 89,730.00 USD | 8,610.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `284.70` | 1,150,000.00 USD | 1,150,000.00 USD | 48,190.00 USD | 54,540.00 USD | 20,690.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `284.70` | 1,650,000.00 USD | 1,650,000.00 USD | 26,130.00 USD | 254,620.00 USD | 34,150.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `285.10` | 1,030,000.00 USD | 1,030,000.00 USD | 20,960.00 USD | 20,580.00 USD | 62,250.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `285.10` | 1,340,000.00 USD | 1,340,000.00 USD | 62,660.00 USD | 190,390.00 USD | 83,240.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `285.50` | 927,560.00 USD | 927,560.00 USD | 91,500.00 USD | 95,280.00 USD | 52,020.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `285.50` | 1,000,000.00 USD | 1,000,000.00 USD | 0.00 USD | 185,240.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `285.50` | 17,750.00 USD | 17,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `285.90` | 688,760.00 USD | 688,760.00 USD | 0.00 USD | 42,840.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `285.90` | 815,200.00 USD | 815,200.00 USD | 0.00 USD | 52,670.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `286.30` | 645,920.00 USD | 645,920.00 USD | 20,960.00 USD | 11,620.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `286.30` | 762,530.00 USD | 762,530.00 USD | 0.00 USD | 40,670.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `286.70` | 613,330.00 USD | 613,330.00 USD | 134,800.00 USD | 85,750.00 USD | 80,840.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `286.70` | 721,860.00 USD | 721,860.00 USD | 23,860.00 USD | 146,630.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `287.10` | 311,950.00 USD | 311,950.00 USD | 38,480.00 USD | 136,750.00 USD | 80,690.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `287.10` | 551,370.00 USD | 551,370.00 USD | 81,140.00 USD | 138,810.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `287.50` | 56,020.00 USD | 56,020.00 USD | 0.00 USD | 11,010.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `287.50` | 331,410.00 USD | 331,410.00 USD | 0.00 USD | 53,560.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `287.90` | 45,010.00 USD | 45,010.00 USD | 0.00 USD | 0.00 USD | 33,650.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `287.90` | 277,850.00 USD | 277,850.00 USD | 0.00 USD | 277,850.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `288.30` | 11,360.00 USD | 11,360.00 USD | 0.00 USD | 0.00 USD | 11,360.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `289.10` | 11,990.00 USD | 11,990.00 USD | 0.00 USD | 11,990.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `289.50` | 927.80 USD | 927.80 USD | 0.00 USD | 927.80 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `289.90` | 1,870.00 USD | 1,870.00 USD | 0.00 USD | 947.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `291.10` | 12,000.00 USD | 12,000.00 USD | 0.00 USD | 0.00 USD | 5.82 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `291.50` | 62,320.00 USD | 62,320.00 USD | 0.00 USD | 50,320.00 USD | 5.34 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `291.50` | 57,600.00 USD | 57,600.00 USD | 0.00 USD | 55,720.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `291.90` | 90,370.00 USD | 90,370.00 USD | 0.00 USD | 5,920.00 USD | 22,130.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `291.90` | 178,330.00 USD | 178,330.00 USD | 0.00 USD | 120,730.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `292.30` | 148,090.00 USD | 148,090.00 USD | 0.00 USD | 57,710.00 USD | 7.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `292.30` | 249,420.00 USD | 249,420.00 USD | 0.00 USD | 71,060.00 USD | 22.46 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `292.70` | 246,700.00 USD | 246,700.00 USD | 606.80 USD | 98,000.00 USD | 9.69 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `292.70` | 336,640.00 USD | 336,640.00 USD | 0.00 USD | 87,160.00 USD | 62.48 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `293.10` | 298,370.00 USD | 298,370.00 USD | 857.50 USD | 50,810.00 USD | 0.42 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `293.10` | 481,670.00 USD | 481,670.00 USD | 0.00 USD | 144,960.00 USD | 77.95 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `293.50` | 373,550.00 USD | 373,550.00 USD | 8,580.00 USD | 64,440.00 USD | 2,150.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `293.50` | 482,270.00 USD | 482,270.00 USD | 534.50 USD | 0.00 USD | 60.43 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `293.90` | 556,300.00 USD | 556,300.00 USD | 73,070.00 USD | 31,360.00 USD | 78,330.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `293.90` | 599,820.00 USD | 599,820.00 USD | 51,570.00 USD | 20,910.00 USD | 45,080.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `294.30` | 743,570.00 USD | 743,570.00 USD | 62,310.00 USD | 76,770.00 USD | 48,190.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `294.30` | 814,100.00 USD | 814,100.00 USD | 139,780.00 USD | 13,840.00 USD | 60,660.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `294.70` | 1,090,000.00 USD | 1,090,000.00 USD | 115,590.00 USD | 103,120.00 USD | 132,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `294.70` | 981,610.00 USD | 981,610.00 USD | 16,110.00 USD | 92,170.00 USD | 59,220.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `295.10` | 1,220,000.00 USD | 1,220,000.00 USD | 32,330.00 USD | 64,510.00 USD | 25,530.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `295.10` | 1,200,000.00 USD | 1,200,000.00 USD | 48,390.00 USD | 16,140.00 USD | 157,160.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `295.50` | 1,540,000.00 USD | 1,540,000.00 USD | 110,930.00 USD | 118,390.00 USD | 90,360.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `295.50` | 1,690,000.00 USD | 1,690,000.00 USD | 142,280.00 USD | 137,630.00 USD | 202,350.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `295.50` | 612.57 USD | 612.57 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `295.90` | 1,720,000.00 USD | 1,720,000.00 USD | 105,070.00 USD | 48,120.00 USD | 33,310.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `295.90` | 1,870,000.00 USD | 1,870,000.00 USD | 58,330.00 USD | 89,730.00 USD | 31,980.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `296.30` | 1,960,000.00 USD | 1,960,000.00 USD | 108,090.00 USD | 95,560.00 USD | 32,400.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `296.30` | 2,090,000.00 USD | 2,090,000.00 USD | 26,350.00 USD | 77,570.00 USD | 120,790.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `296.70` | 2,160,000.00 USD | 2,160,000.00 USD | 41,440.00 USD | 64,890.00 USD | 94,290.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `296.70` | 2,350,000.00 USD | 2,350,000.00 USD | 118,130.00 USD | 1,060.00 USD | 144,600.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `297.10` | 2,300,000.00 USD | 2,300,000.00 USD | 52,650.00 USD | 20,560.00 USD | 68,850.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `297.10` | 2,520,000.00 USD | 2,520,000.00 USD | 89,710.00 USD | 51,160.00 USD | 27,790.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `297.50` | 2,330,000.00 USD | 2,330,000.00 USD | 6,280.00 USD | 939.55 USD | 20,820.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `297.50` | 2,620,000.00 USD | 2,620,000.00 USD | 3,940.00 USD | 58,600.00 USD | 34,690.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `297.90` | 2,370,000.00 USD | 2,370,000.00 USD | 1,150.00 USD | 7,600.00 USD | 32,940.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `297.90` | 2,730,000.00 USD | 2,730,000.00 USD | 16,990.00 USD | 39,840.00 USD | 54,850.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `298.30` | 2,560,000.00 USD | 2,560,000.00 USD | 44,780.00 USD | 8,520.00 USD | 137,760.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `298.30` | 2,850,000.00 USD | 2,850,000.00 USD | 32,250.00 USD | 41,860.00 USD | 48,020.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `298.70` | 2,680,000.00 USD | 2,680,000.00 USD | 25,530.00 USD | 13,400.00 USD | 80,710.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `298.70` | 2,940,000.00 USD | 2,940,000.00 USD | 69,820.00 USD | 11,780.00 USD | 112.32 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `299.10` | 2,790,000.00 USD | 2,790,000.00 USD | 48,760.00 USD | 22,810.00 USD | 38,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `299.10` | 3,020,000.00 USD | 3,020,000.00 USD | 1,100.00 USD | 993.25 USD | 85,820.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `299.50` | 2,880,000.00 USD | 2,880,000.00 USD | 28,240.00 USD | 29,040.00 USD | 29,670.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `299.50` | 3,030,000.00 USD | 3,030,000.00 USD | 3,330.00 USD | 2,700.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `299.50` | 1,220.00 USD | 1,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `299.90` | 2,920,000.00 USD | 2,920,000.00 USD | 17,990.00 USD | 17,070.00 USD | 7,710.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `299.90` | 3,110,000.00 USD | 3,110,000.00 USD | 55,220.00 USD | 8,330.00 USD | 19,830.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `300.30` | 3,020,000.00 USD | 3,020,000.00 USD | 35,780.00 USD | 32,740.00 USD | 34,860.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `300.30` | 3,110,000.00 USD | 3,110,000.00 USD | 866.20 USD | 1,190.00 USD | 16.16 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `300.70` | 3,110,000.00 USD | 3,110,000.00 USD | 10,820.00 USD | 37,840.00 USD | 35,450.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `300.70` | 3,230,000.00 USD | 3,230,000.00 USD | 24,140.00 USD | 70,210.00 USD | 19,730.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `301.10` | 3,180,000.00 USD | 3,180,000.00 USD | 36,200.00 USD | 28,610.00 USD | 2,060.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `301.10` | 3,380,000.00 USD | 3,380,000.00 USD | 23,380.00 USD | 32,100.00 USD | 90,900.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `301.50` | 3,280,000.00 USD | 3,280,000.00 USD | 31,870.00 USD | 27,310.00 USD | 44,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `301.50` | 3,610,000.00 USD | 3,610,000.00 USD | 85,980.00 USD | 85,500.00 USD | 59,610.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `301.50` | 2,380.00 USD | 4,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `301.90` | 3,380,000.00 USD | 3,380,000.00 USD | 39,820.00 USD | 51,210.00 USD | 11,590.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `301.90` | 3,810,000.00 USD | 3,810,000.00 USD | 51,660.00 USD | 123,250.00 USD | 26,220.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `302.30` | 3,410,000.00 USD | 3,410,000.00 USD | 5,320.00 USD | 12,080.00 USD | 10,300.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `302.30` | 3,930,000.00 USD | 3,930,000.00 USD | 1,560.00 USD | 125,480.00 USD | 5.75 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `302.70` | 3,470,000.00 USD | 3,470,000.00 USD | 11,520.00 USD | 11,290.00 USD | 41,320.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `302.70` | 4,120,000.00 USD | 4,120,000.00 USD | 71,700.00 USD | 70,100.00 USD | 41,770.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `303.10` | 3,510,000.00 USD | 3,510,000.00 USD | 21,200.00 USD | 1,360.00 USD | 14,740.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `303.10` | 4,160,000.00 USD | 4,160,000.00 USD | 0.00 USD | 39,740.00 USD | 163.74 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `303.50` | 3,530,000.00 USD | 3,530,000.00 USD | 12,100.00 USD | 248.89 USD | 6,250.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `303.50` | 4,160,000.00 USD | 4,160,000.00 USD | 0.00 USD | 173.09 USD | 152.72 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `303.90` | 3,580,000.00 USD | 3,580,000.00 USD | 29,930.00 USD | 3,780.00 USD | 18,760.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `303.90` | 4,210,000.00 USD | 4,210,000.00 USD | 21,140.00 USD | 10,490.00 USD | 24,580.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `304.30` | 3,640,000.00 USD | 3,640,000.00 USD | 4,310.00 USD | 5,410.00 USD | 48,560.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `304.30` | 4,220,000.00 USD | 4,220,000.00 USD | 2,070.00 USD | 174.44 USD | 99.53 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `304.70` | 3,700,000.00 USD | 3,700,000.00 USD | 9,700.00 USD | 5,010.00 USD | 40,350.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `304.70` | 4,230,000.00 USD | 4,230,000.00 USD | 3,610.00 USD | 11,790.00 USD | 2,060.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `305.10` | 3,710,000.00 USD | 3,710,000.00 USD | 9,360.00 USD | 236.66 USD | 2,010.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `305.10` | 4,580,000.00 USD | 4,580,000.00 USD | 127,730.00 USD | 131,900.00 USD | 84,440.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `305.50` | 3,720,000.00 USD | 3,720,000.00 USD | 5,430.00 USD | 1,760.00 USD | 1,500.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `305.50` | 4,740,000.00 USD | 4,740,000.00 USD | 94,240.00 USD | 19,010.00 USD | 52,970.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `305.90` | 3,730,000.00 USD | 3,730,000.00 USD | 9,650.00 USD | 2,750.00 USD | 1,930.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `305.90` | 4,860,000.00 USD | 4,860,000.00 USD | 58,070.00 USD | 53,970.00 USD | 3,520.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `306.30` | 3,740,000.00 USD | 3,740,000.00 USD | 4,260.00 USD | 3,210.00 USD | 1,390.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `306.30` | 5,000,000.00 USD | 5,000,000.00 USD | 29,420.00 USD | 47,840.00 USD | 63,790.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `306.70` | 3,770,000.00 USD | 3,770,000.00 USD | 4,420.00 USD | 21,850.00 USD | 3,850.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `306.70` | 5,110,000.00 USD | 5,110,000.00 USD | 27,190.00 USD | 29,850.00 USD | 54,570.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `307.10` | 3,860,000.00 USD | 3,860,000.00 USD | 33,050.00 USD | 42,000.00 USD | 13,710.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `307.10` | 5,360,000.00 USD | 5,360,000.00 USD | 60,720.00 USD | 90,210.00 USD | 98,880.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `307.50` | 3,900,000.00 USD | 3,900,000.00 USD | 6,340.00 USD | 22,140.00 USD | 9,430.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `307.50` | 5,580,000.00 USD | 5,580,000.00 USD | 57,330.00 USD | 114,040.00 USD | 41,580.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `307.90` | 3,980,000.00 USD | 3,980,000.00 USD | 33,320.00 USD | 30,510.00 USD | 21,640.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `307.90` | 5,860,000.00 USD | 5,860,000.00 USD | 125,550.00 USD | 94,530.00 USD | 65,460.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `308.30` | 4,010,000.00 USD | 4,010,000.00 USD | 13,820.00 USD | 7,420.00 USD | 5,640.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `308.30` | 6,140,000.00 USD | 6,140,000.00 USD | 129,220.00 USD | 40,480.00 USD | 109,540.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `308.70` | 4,020,000.00 USD | 4,020,000.00 USD | 5,550.00 USD | 298.40 USD | 3,480.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `308.70` | 6,250,000.00 USD | 6,250,000.00 USD | 67,430.00 USD | 31,490.00 USD | 15,420.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `309.10` | 4,040,000.00 USD | 4,040,000.00 USD | 12,160.00 USD | 6,430.00 USD | 2,980.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `309.10` | 6,370,000.00 USD | 6,370,000.00 USD | 38,660.00 USD | 39,620.00 USD | 39,810.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `309.50` | 4,080,000.00 USD | 4,080,000.00 USD | 12,390.00 USD | 22,900.00 USD | 8,280.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `309.50` | 6,570,000.00 USD | 6,570,000.00 USD | 47,540.00 USD | 51,380.00 USD | 101,860.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `309.90` | 4,090,000.00 USD | 4,090,000.00 USD | 8,500.00 USD | 2,590.00 USD | 978.51 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `309.90` | 6,780,000.00 USD | 6,780,000.00 USD | 19,540.00 USD | 106,330.00 USD | 75,880.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `310.30` | 4,100,000.00 USD | 4,100,000.00 USD | 232.38 USD | 7,040.00 USD | 2.37 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `310.30` | 7,010,000.00 USD | 7,010,000.00 USD | 47,320.00 USD | 107,890.00 USD | 76,830.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `310.50` | 517.91 USD | 4,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `310.70` | 4,100,000.00 USD | 4,100,000.00 USD | 144.00 USD | 421.81 USD | 2.98 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `310.70` | 7,130,000.00 USD | 7,130,000.00 USD | 65,370.00 USD | 50,820.00 USD | 3,850.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `311.10` | 4,110,000.00 USD | 4,110,000.00 USD | 134.35 USD | 2,050.00 USD | 4,090.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `311.10` | 7,290,000.00 USD | 7,290,000.00 USD | 59,270.00 USD | 59,630.00 USD | 47,640.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `311.50` | 4,160,000.00 USD | 4,160,000.00 USD | 25,300.00 USD | 6,590.00 USD | 18,300.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `311.50` | 7,340,000.00 USD | 7,340,000.00 USD | 37,540.00 USD | 6,860.00 USD | 5,690.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `311.90` | 4,160,000.00 USD | 4,160,000.00 USD | 2,810.00 USD | 0.00 USD | 4.48 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `311.90` | 7,430,000.00 USD | 7,430,000.00 USD | 48,410.00 USD | 10,970.00 USD | 26,180.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `312.30` | 4,180,000.00 USD | 4,180,000.00 USD | 6,410.00 USD | 5,330.00 USD | 8,690.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `312.30` | 7,510,000.00 USD | 7,510,000.00 USD | 30,350.00 USD | 11,070.00 USD | 34,540.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `312.70` | 4,200,000.00 USD | 4,200,000.00 USD | 14,010.00 USD | 2,180.00 USD | 39.02 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `312.70` | 7,590,000.00 USD | 7,590,000.00 USD | 16,880.00 USD | 30,630.00 USD | 39,500.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `313.10` | 4,210,000.00 USD | 4,210,000.00 USD | 5,080.00 USD | 1,940.00 USD | 0.96 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `313.10` | 7,700,000.00 USD | 7,700,000.00 USD | 52,780.00 USD | 16,920.00 USD | 37,170.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `313.50` | 4,220,000.00 USD | 4,220,000.00 USD | 7,160.00 USD | 4,770.00 USD | 2,580.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `313.50` | 7,780,000.00 USD | 7,780,000.00 USD | 34,410.00 USD | 14,970.00 USD | 27,720.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `313.90` | 4,240,000.00 USD | 4,240,000.00 USD | 4,760.00 USD | 10,330.00 USD | 10,050.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `313.90` | 7,870,000.00 USD | 7,870,000.00 USD | 44,540.00 USD | 15,260.00 USD | 31,470.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `314.30` | 4,260,000.00 USD | 4,260,000.00 USD | 4,210.00 USD | 5,710.00 USD | 3,420.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `314.30` | 7,970,000.00 USD | 7,970,000.00 USD | 51,980.00 USD | 307.60 USD | 51,780.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `314.70` | 4,270,000.00 USD | 4,270,000.00 USD | 303.95 USD | 0.00 USD | 8,330.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `314.70` | 7,990,000.00 USD | 7,990,000.00 USD | 9,830.00 USD | 0.00 USD | 10,290.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `315.10` | 4,280,000.00 USD | 4,280,000.00 USD | 32.50 USD | 0.00 USD | 10,730.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `315.10` | 8,020,000.00 USD | 8,020,000.00 USD | 29,590.00 USD | 547.95 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `315.50` | 4,300,000.00 USD | 4,300,000.00 USD | 129.37 USD | 3,270.00 USD | 19,390.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `315.50` | 8,080,000.00 USD | 8,080,000.00 USD | 13,690.00 USD | 9,550.00 USD | 30,790.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `315.90` | 4,310,000.00 USD | 4,310,000.00 USD | 1,470.00 USD | 5,260.00 USD | 43.23 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `315.90` | 8,170,000.00 USD | 8,170,000.00 USD | 39,580.00 USD | 41,220.00 USD | 17,430.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `316.30` | 4,340,000.00 USD | 4,340,000.00 USD | 12,450.00 USD | 5,050.00 USD | 11,800.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `316.30` | 8,240,000.00 USD | 8,240,000.00 USD | 451.45 USD | 19,940.00 USD | 43,430.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `316.70` | 4,370,000.00 USD | 4,370,000.00 USD | 16,490.00 USD | 8,870.00 USD | 10,710.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `316.70` | 8,310,000.00 USD | 8,310,000.00 USD | 18,110.00 USD | 30,550.00 USD | 18,380.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `317.10` | 4,380,000.00 USD | 4,380,000.00 USD | 3,940.00 USD | 2,260.00 USD | 3,360.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `317.10` | 8,310,000.00 USD | 8,310,000.00 USD | 1,810.00 USD | 1,110.00 USD | 69.80 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `317.50` | 4,420,000.00 USD | 4,420,000.00 USD | 11,570.00 USD | 14,470.00 USD | 13,510.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `317.50` | 8,320,000.00 USD | 8,320,000.00 USD | 14,400.00 USD | 574.27 USD | 29.51 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `317.90` | 4,440,000.00 USD | 4,440,000.00 USD | 326.88 USD | 9,140.00 USD | 9,880.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `317.90` | 8,350,000.00 USD | 8,350,000.00 USD | 21,020.00 USD | 8,200.00 USD | 193.76 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `318.30` | 4,450,000.00 USD | 4,450,000.00 USD | 2,200.00 USD | 8,430.00 USD | 820.17 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `318.30` | 8,410,000.00 USD | 8,410,000.00 USD | 3,320.00 USD | 26,930.00 USD | 22,340.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `318.50` | 114.34 USD | 4,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `318.70` | 4,470,000.00 USD | 4,470,000.00 USD | 4,470.00 USD | 9,400.00 USD | 7,760.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `318.70` | 8,470,000.00 USD | 8,470,000.00 USD | 10,810.00 USD | 18,570.00 USD | 37,840.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `319.10` | 4,500,000.00 USD | 4,500,000.00 USD | 12,470.00 USD | 6,810.00 USD | 6,660.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `319.10` | 8,490,000.00 USD | 8,490,000.00 USD | 366.90 USD | 18,060.00 USD | 49.12 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `319.50` | 4,520,000.00 USD | 4,520,000.00 USD | 8,590.00 USD | 10,950.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `319.50` | 8,490,000.00 USD | 8,490,000.00 USD | 733.55 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `319.50` | 6,600.00 USD | 11,440.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `319.90` | 4,530,000.00 USD | 4,530,000.00 USD | 4,350.00 USD | 2,370.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `319.90` | 8,520,000.00 USD | 8,520,000.00 USD | 446.22 USD | 22,230.00 USD | 5,330.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `320.30` | 4,550,000.00 USD | 4,550,000.00 USD | 0.00 USD | 4,210.00 USD | 16,510.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `320.30` | 8,600,000.00 USD | 8,600,000.00 USD | 49,430.00 USD | 10,080.00 USD | 25,260.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `320.50` | 1,110.00 USD | 12,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `320.70` | 4,560,000.00 USD | 4,560,000.00 USD | 8,130.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `320.70` | 8,600,000.00 USD | 8,600,000.00 USD | 189.87 USD | 0.00 USD | 53.16 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `321.10` | 4,560,000.00 USD | 4,560,000.00 USD | 150.60 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `321.10` | 8,620,000.00 USD | 8,620,000.00 USD | 9,210.00 USD | 8,300.00 USD | 31.64 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `321.50` | 4,570,000.00 USD | 4,570,000.00 USD | 8,670.00 USD | 0.00 USD | 7,500.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `321.50` | 8,660,000.00 USD | 8,660,000.00 USD | 4,440.00 USD | 9,730.00 USD | 21,040.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `321.90` | 4,580,000.00 USD | 4,580,000.00 USD | 0.00 USD | 0.00 USD | 8,660.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `321.90` | 8,660,000.00 USD | 8,660,000.00 USD | 910.57 USD | 500.60 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `322.30` | 4,600,000.00 USD | 4,600,000.00 USD | 0.00 USD | 0.00 USD | 16,140.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `322.30` | 8,700,000.00 USD | 8,700,000.00 USD | 22,930.00 USD | 7,790.00 USD | 6,150.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `322.70` | 8,710,000.00 USD | 8,710,000.00 USD | 9,620.00 USD | 6,000.00 USD | 3.32 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `323.10` | 8,750,000.00 USD | 8,750,000.00 USD | 21,120.00 USD | 5,860.00 USD | 11,480.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `323.50` | 8,760,000.00 USD | 8,760,000.00 USD | 269.10 USD | 6,780.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `324.30` | 8,790,000.00 USD | 8,790,000.00 USD | 0.00 USD | 4,960.00 USD | 23,350.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `324.50` | 8,800,000.00 USD | 8,800,000.00 USD | 11,060.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
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
| `Live` | `Long` | `95.50` | 469,140.00 USD | 0.00 USD | 920.05 USD | `-66.96%` | `9,634,000,000.00` |
| `Live` | `Long` | `101.50` | 468,220.00 USD | 0.00 USD | 6,240.00 USD | `-64.88%` | `61,439,000,000.00` |
| `Live` | `Long` | `102.50` | 461,980.00 USD | 0.00 USD | 4,080.00 USD | `-64.54%` | `39,797,000,000.00` |
| `Live` | `Long` | `109.50` | 457,910.00 USD | 0.00 USD | 212.76 USD | `-62.11%` | `1,943,000,000.00` |
| `Live` | `Long` | `115.50` | 457,690.00 USD | 0.00 USD | 50,900.00 USD | `-60.04%` | `440,704,000,000.00` |
| `Live` | `Long` | `116.50` | 406,790.00 USD | 0.00 USD | 171.25 USD | `-59.69%` | `1,470,000,000.00` |
| `Live` | `Long` | `118.50` | 406,620.00 USD | 0.00 USD | 212.35 USD | `-59.00%` | `1,792,000,000.00` |
| `Live` | `Long` | `122.50` | 406,410.00 USD | 0.00 USD | 124.46 USD | `-57.62%` | `1,016,000,000.00` |
| `Live` | `Long` | `126.50` | 406,280.00 USD | 0.00 USD | 658.18 USD | `-56.23%` | `5,203,000,000.00` |
| `Live` | `Long` | `141.50` | 405,620.00 USD | 0.00 USD | 2,120.00 USD | `-51.04%` | `15,000,000,000.00` |
| `Live` | `Long` | `143.50` | 403,500.00 USD | 0.00 USD | 7,170.00 USD | `-50.35%` | `50,000,000,000.00` |
| `Live` | `Long` | `145.50` | 396,330.00 USD | 0.00 USD | 2,070.00 USD | `-49.66%` | `14,200,000,000.00` |
| `Live` | `Long` | `147.50` | 394,260.00 USD | 0.00 USD | 895.47 USD | `-48.97%` | `6,071,000,000.00` |
| `Live` | `Long` | `148.50` | 393,370.00 USD | 0.00 USD | 1,270.00 USD | `-48.62%` | `8,528,000,000.00` |
| `Live` | `Long` | `149.50` | 392,100.00 USD | 0.00 USD | 2,370.00 USD | `-48.27%` | `15,823,000,000.00` |
| `Live` | `Long` | `152.50` | 389,730.00 USD | 0.00 USD | 303.78 USD | `-47.24%` | `1,992,000,000.00` |
| `Live` | `Long` | `162.50` | 389,430.00 USD | 0.00 USD | 958.26 USD | `-43.78%` | `5,897,000,000.00` |
| `Live` | `Long` | `167.50` | 388,470.00 USD | 0.00 USD | 285.75 USD | `-42.05%` | `1,706,000,000.00` |
| `Live` | `Long` | `170.50` | 388,190.00 USD | 0.00 USD | 426.25 USD | `-41.01%` | `2,500,000,000.00` |
| `Live` | `Long` | `174.50` | 387,760.00 USD | 0.00 USD | 169.96 USD | `-39.62%` | `974,000,000.00` |
| `Live` | `Long` | `175.50` | 387,590.00 USD | 0.00 USD | 516.67 USD | `-39.28%` | `2,944,000,000.00` |
| `Live` | `Long` | `176.50` | 387,070.00 USD | 0.00 USD | 373.83 USD | `-38.93%` | `2,118,000,000.00` |
| `Live` | `Long` | `183.50` | 386,700.00 USD | 0.00 USD | 742.07 USD | `-36.51%` | `4,044,000,000.00` |
| `Live` | `Long` | `184.50` | 385,960.00 USD | 0.00 USD | 616.05 USD | `-36.16%` | `3,339,000,000.00` |
| `Live` | `Long` | `185.50` | 385,340.00 USD | 0.00 USD | 5,840.00 USD | `-35.82%` | `31,500,000,000.00` |
| `Live` | `Long` | `188.50` | 379,500.00 USD | 0.00 USD | 782.09 USD | `-34.78%` | `4,149,000,000.00` |
| `Live` | `Long` | `191.50` | 378,720.00 USD | 0.00 USD | 1,340.00 USD | `-33.74%` | `6,983,000,000.00` |
| `Live` | `Long` | `192.50` | 377,380.00 USD | 0.00 USD | 1,490.00 USD | `-33.40%` | `7,715,000,000.00` |
| `Live` | `Long` | `193.50` | 375,890.00 USD | 0.00 USD | 786.96 USD | `-33.05%` | `4,067,000,000.00` |
| `Live` | `Long` | `195.50` | 375,110.00 USD | 0.00 USD | 370.47 USD | `-32.36%` | `1,895,000,000.00` |
| `Live` | `Long` | `199.50` | 374,740.00 USD | 0.00 USD | 765.08 USD | `-30.97%` | `3,835,000,000.00` |
| `Live` | `Long` | `200.50` | 373,970.00 USD | 0.00 USD | 293.13 USD | `-30.63%` | `1,462,000,000.00` |
| `Live` | `Long` | `202.50` | 373,680.00 USD | 0.00 USD | 420.39 USD | `-29.94%` | `2,076,000,000.00` |
| `Live` | `Long` | `204.50` | 373,260.00 USD | 0.00 USD | 39,880.00 USD | `-29.24%` | `195,028,000,000.00` |
| `Live` | `Long` | `205.50` | 333,370.00 USD | 0.00 USD | 191.53 USD | `-28.90%` | `932,000,000.00` |
| `Live` | `Long` | `210.50` | 333,180.00 USD | 0.00 USD | 108.83 USD | `-27.17%` | `517,000,000.00` |
| `Live` | `Long` | `211.50` | 333,070.00 USD | 0.00 USD | 1,110.00 USD | `-26.82%` | `5,260,000,000.00` |
| `Live` | `Long` | `212.50` | 331,960.00 USD | 0.00 USD | 106.25 USD | `-26.48%` | `500,000,000.00` |
| `Live` | `Long` | `213.50` | 331,860.00 USD | 0.00 USD | 4,420.00 USD | `-26.13%` | `20,686,000,000.00` |
| `Live` | `Long` | `215.50` | 327,440.00 USD | 0.00 USD | 239.85 USD | `-25.44%` | `1,113,000,000.00` |
| `Live` | `Long` | `219.50` | 327,200.00 USD | 0.00 USD | 5,690.00 USD | `-24.05%` | `25,931,000,000.00` |
| `Live` | `Long` | `220.50` | 321,510.00 USD | 0.00 USD | 1,010.00 USD | `-23.71%` | `4,592,000,000.00` |
| `Live` | `Long` | `223.50` | 320,490.00 USD | 0.00 USD | 32,860.00 USD | `-22.67%` | `147,023,000,000.00` |
| `Live` | `Long` | `224.50` | 287,630.00 USD | 0.00 USD | 610.42 USD | `-22.32%` | `2,719,000,000.00` |
| `Live` | `Long` | `226.50` | 287,020.00 USD | 0.00 USD | 1,240.00 USD | `-21.63%` | `5,455,000,000.00` |
| `Live` | `Long` | `227.50` | 285,790.00 USD | 0.00 USD | 174.49 USD | `-21.29%` | `767,000,000.00` |
| `Live` | `Long` | `228.50` | 285,610.00 USD | 0.00 USD | 642.77 USD | `-20.94%` | `2,813,000,000.00` |
| `Live` | `Long` | `229.50` | 284,970.00 USD | 0.00 USD | 47,090.00 USD | `-20.59%` | `205,171,000,000.00` |
| `Live` | `Long` | `231.50` | 237,880.00 USD | 0.00 USD | 295.86 USD | `-19.90%` | `1,278,000,000.00` |
| `Live` | `Long` | `232.50` | 237,590.00 USD | 0.00 USD | 429.66 USD | `-19.56%` | `1,848,000,000.00` |
| `Live` | `Long` | `234.50` | 237,160.00 USD | 0.00 USD | 217.85 USD | `-18.86%` | `929,000,000.00` |
| `Live` | `Long` | `235.50` | 236,940.00 USD | 0.00 USD | 1,480.00 USD | `-18.52%` | `6,274,000,000.00` |
| `Live` | `Long` | `239.50` | 235,460.00 USD | 0.00 USD | 1,030.00 USD | `-17.13%` | `4,281,000,000.00` |
| `Live` | `Long` | `241.50` | 234,440.00 USD | 0.00 USD | 367.32 USD | `-16.44%` | `1,521,000,000.00` |
| `Live` | `Long` | `243.50` | 234,070.00 USD | 0.00 USD | 9,700.00 USD | `-15.75%` | `39,821,000,000.00` |
| `Live` | `Long` | `244.50` | 224,370.00 USD | 0.00 USD | 4,220.00 USD | `-15.40%` | `17,277,000,000.00` |
| `Live` | `Long` | `245.50` | 220,150.00 USD | 0.00 USD | 1,030.00 USD | `-15.06%` | `4,182,000,000.00` |
| `Live` | `Long` | `247.50` | 219,120.00 USD | 0.00 USD | 6,480.00 USD | `-14.37%` | `26,178,000,000.00` |
| `Live` | `Long` | `250.50` | 212,640.00 USD | 0.00 USD | 1,330.00 USD | `-13.33%` | `5,292,000,000.00` |
| `Live` | `Long` | `251.50` | 211,320.00 USD | 0.00 USD | 268.35 USD | `-12.98%` | `1,067,000,000.00` |
| `Live` | `Long` | `252.50` | 211,050.00 USD | 0.00 USD | 1,030.00 USD | `-12.64%` | `4,088,000,000.00` |
| `Live` | `Long` | `254.50` | 210,020.00 USD | 0.00 USD | 362.92 USD | `-11.94%` | `1,426,000,000.00` |
| `Live` | `Long` | `255.50` | 209,660.00 USD | 0.00 USD | 3,660.00 USD | `-11.60%` | `14,337,000,000.00` |
| `Live` | `Long` | `256.50` | 205,990.00 USD | 0.00 USD | 2,480.00 USD | `-11.25%` | `9,686,000,000.00` |
| `Live` | `Long` | `257.50` | 203,510.00 USD | 0.00 USD | 14,580.00 USD | `-10.91%` | `56,622,000,000.00` |
| `Live` | `Long` | `258.50` | 188,930.00 USD | 0.00 USD | 176.56 USD | `-10.56%` | `683,000,000.00` |
| `Live` | `Long` | `260.50` | 188,750.00 USD | 0.00 USD | 3,860.00 USD | `-9.87%` | `14,816,000,000.00` |
| `Live` | `Long` | `264.50` | 184,890.00 USD | 0.00 USD | 280.37 USD | `-8.48%` | `1,060,000,000.00` |
| `Live` | `Long` | `265.50` | 184,610.00 USD | 0.00 USD | 121,910.00 USD | `-8.14%` | `459,161,000,000.00` |
| `Live` | `Long` | `266.50` | 62,700.00 USD | 0.00 USD | 15,210.00 USD | `-7.79%` | `57,069,000,000.00` |
| `Live` | `Long` | `267.50` | 47,500.00 USD | 0.00 USD | 684.00 USD | `-7.45%` | `2,557,000,000.00` |
| `Live` | `Long` | `268.50` | 46,810.00 USD | 0.00 USD | 7,020.00 USD | `-7.10%` | `26,129,000,000.00` |
| `Live` | `Long` | `269.50` | 39,800.00 USD | 0.00 USD | 37,920.00 USD | `-6.75%` | `140,689,000,000.00` |
| `Live` | `Long` | `270.50` | 1,880.00 USD | 0.00 USD | 106.31 USD | `-6.41%` | `393,000,000.00` |
| `Live` | `Long` | `271.50` | 1,770.00 USD | 0.00 USD | 1,000.00 USD | `-6.06%` | `3,685,000,000.00` |
| `Live` | `Long` | `274.50` | 773.38 USD | 0.00 USD | 567.94 USD | `-5.02%` | `2,069,000,000.00` |
| `Live` | `Long` | `276.50` | 205.44 USD | 0.00 USD | 205.44 USD | `-4.33%` | `743,000,000.00` |
| `Live` | `Short` | `290.50` | 1,210.00 USD | 1,210.00 USD | 0.00 USD | `+0.51%` | `4,156,000,000.00` |
| `Live` | `Short` | `301.50` | 3,580.00 USD | 2,380.00 USD | 0.00 USD | `+4.32%` | `7,885,000,000.00` |
| `Live` | `Short` | `304.50` | 4,620.00 USD | 1,040.00 USD | 0.00 USD | `+5.36%` | `3,411,000,000.00` |
| `Live` | `Short` | `310.50` | 5,140.00 USD | 517.91 USD | 0.00 USD | `+7.43%` | `1,668,000,000.00` |
| `Live` | `Short` | `311.50` | 5,680.00 USD | 539.21 USD | 0.00 USD | `+7.78%` | `1,731,000,000.00` |
| `Live` | `Short` | `315.50` | 12,200.00 USD | 6,520.00 USD | 0.00 USD | `+9.16%` | `20,668,000,000.00` |
| `Live` | `Short` | `318.50` | 12,320.00 USD | 114.34 USD | 0.00 USD | `+10.20%` | `359,000,000.00` |
| `Live` | `Short` | `320.50` | 13,420.00 USD | 1,110.00 USD | 0.00 USD | `+10.89%` | `3,452,000,000.00` |
| `Live` | `Short` | `330.50` | 13,700.00 USD | 276.63 USD | 0.00 USD | `+14.35%` | `837,000,000.00` |
| `Live` | `Short` | `340.50` | 15,060.00 USD | 1,360.00 USD | 0.00 USD | `+17.81%` | `4,000,000,000.00` |
| `Live` | `Short` | `356.50` | 54,280.00 USD | 39,220.00 USD | 0.00 USD | `+23.35%` | `110,000,000,000.00` |
| `Live` | `Short` | `358.50` | 55,280.00 USD | 1,010.00 USD | 0.00 USD | `+24.04%` | `2,812,000,000.00` |
| `Live` | `Short` | `368.50` | 55,730.00 USD | 445.52 USD | 0.00 USD | `+27.50%` | `1,209,000,000.00` |
| `Live` | `Short` | `395.50` | 59,160.00 USD | 3,430.00 USD | 0.00 USD | `+36.84%` | `8,681,000,000.00` |
| `Live` | `Short` | `427.50` | 68,640.00 USD | 9,480.00 USD | 0.00 USD | `+47.91%` | `22,172,000,000.00` |
| `Live` | `Short` | `432.50` | 77,450.00 USD | 8,810.00 USD | 0.00 USD | `+49.64%` | `20,366,000,000.00` |
| `Live` | `Short` | `459.50` | 123,700.00 USD | 46,250.00 USD | 0.00 USD | `+58.99%` | `100,662,000,000.00` |
| `Live` | `Short` | `498.50` | 124,750.00 USD | 1,040.00 USD | 0.00 USD | `+72.48%` | `2,093,000,000.00` |
| `Live` | `Short` | `533.50` | 124,920.00 USD | 177.66 USD | 0.00 USD | `+84.59%` | `333,000,000.00` |
| `Live` | `Short` | `560.50` | 125,770.00 USD | 842.43 USD | 0.00 USD | `+93.93%` | `1,503,000,000.00` |
| `Live` | `Short` | `565.50` | 127,220.00 USD | 1,450.00 USD | 0.00 USD | `+95.66%` | `2,572,000,000.00` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `143.50` | 209,970.00 USD | 0.00 USD | 210.94 USD | `-50.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `145.50` | 209,760.00 USD | 0.00 USD | 2,070.00 USD | `-49.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `178.50` | 207,690.00 USD | 0.00 USD | 2,530.00 USD | `-38.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `184.50` | 205,160.00 USD | 0.00 USD | 490.59 USD | `-36.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `196.50` | 204,670.00 USD | 0.00 USD | 482.01 USD | `-32.01%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `200.50` | 204,190.00 USD | 0.00 USD | 189.07 USD | `-30.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `208.50` | 204,000.00 USD | 0.00 USD | 441.60 USD | `-27.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `210.50` | 203,560.00 USD | 0.00 USD | 703.49 USD | `-27.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `221.50` | 202,850.00 USD | 0.00 USD | 638.36 USD | `-23.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `224.50` | 202,220.00 USD | 0.00 USD | 740.85 USD | `-22.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `228.50` | 201,480.00 USD | 0.00 USD | 1,050.00 USD | `-20.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `233.50` | 200,430.00 USD | 0.00 USD | 389.48 USD | `-19.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `237.50` | 200,040.00 USD | 0.00 USD | 220.64 USD | `-17.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `238.50` | 199,820.00 USD | 0.00 USD | 429.30 USD | `-17.48%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `239.50` | 199,390.00 USD | 0.00 USD | 296.50 USD | `-17.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `240.50` | 199,090.00 USD | 0.00 USD | 216.45 USD | `-16.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `242.50` | 198,870.00 USD | 0.00 USD | 101.61 USD | `-16.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `244.50` | 198,770.00 USD | 0.00 USD | 366.75 USD | `-15.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `246.50` | 198,400.00 USD | 0.00 USD | 1,630.00 USD | `-14.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `249.50` | 196,780.00 USD | 0.00 USD | 2,940.00 USD | `-13.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `250.50` | 193,840.00 USD | 0.00 USD | 4,560.00 USD | `-13.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `251.50` | 189,280.00 USD | 0.00 USD | 7,080.00 USD | `-12.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `252.50` | 182,200.00 USD | 0.00 USD | 231.54 USD | `-12.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `253.50` | 181,970.00 USD | 0.00 USD | 109.26 USD | `-12.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `255.50` | 181,860.00 USD | 0.00 USD | 1,780.00 USD | `-11.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `256.50` | 180,080.00 USD | 0.00 USD | 51,300.00 USD | `-11.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `257.50` | 128,780.00 USD | 0.00 USD | 250.81 USD | `-10.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `259.50` | 128,530.00 USD | 0.00 USD | 386.14 USD | `-10.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `260.50` | 128,140.00 USD | 0.00 USD | 707.78 USD | `-9.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `262.50` | 127,430.00 USD | 0.00 USD | 857.85 USD | `-9.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `263.50` | 126,580.00 USD | 0.00 USD | 7,790.00 USD | `-8.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `264.50` | 118,780.00 USD | 0.00 USD | 122.99 USD | `-8.48%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `265.50` | 118,660.00 USD | 0.00 USD | 455.86 USD | `-8.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `266.50` | 118,200.00 USD | 0.00 USD | 10,490.00 USD | `-7.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `267.50` | 107,720.00 USD | 0.00 USD | 1,110.00 USD | `-7.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `268.50` | 106,610.00 USD | 0.00 USD | 877.46 USD | `-7.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `269.50` | 105,730.00 USD | 0.00 USD | 498.04 USD | `-6.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `270.50` | 105,240.00 USD | 0.00 USD | 1,180.00 USD | `-6.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `271.50` | 104,060.00 USD | 0.00 USD | 269.60 USD | `-6.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `272.50` | 103,790.00 USD | 0.00 USD | 13,500.00 USD | `-5.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `273.50` | 90,290.00 USD | 0.00 USD | 1,470.00 USD | `-5.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `274.50` | 88,820.00 USD | 0.00 USD | 336.54 USD | `-5.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `275.50` | 88,490.00 USD | 0.00 USD | 681.31 USD | `-4.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `276.50` | 87,810.00 USD | 0.00 USD | 105.35 USD | `-4.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `277.50` | 87,700.00 USD | 0.00 USD | 14,500.00 USD | `-3.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `278.50` | 73,200.00 USD | 0.00 USD | 125.88 USD | `-3.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `279.50` | 73,070.00 USD | 0.00 USD | 25,690.00 USD | `-3.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `280.50` | 47,380.00 USD | 0.00 USD | 20,810.00 USD | `-2.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `281.50` | 26,570.00 USD | 0.00 USD | 2,880.00 USD | `-2.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `282.50` | 23,690.00 USD | 0.00 USD | 290.13 USD | `-2.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `283.50` | 23,400.00 USD | 0.00 USD | 11,620.00 USD | `-1.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `284.50` | 11,780.00 USD | 0.00 USD | 3,690.00 USD | `-1.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `285.50` | 8,090.00 USD | 0.00 USD | 2,600.00 USD | `-1.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `286.50` | 5,480.00 USD | 0.00 USD | 5,080.00 USD | `-0.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `287.50` | 400.62 USD | 0.00 USD | 280.02 USD | `-0.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `288.50` | 120.59 USD | 0.00 USD | 120.59 USD | `-0.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `289.50` | 153.44 USD | 153.44 USD | 0.00 USD | `+0.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `290.50` | 1,470.00 USD | 1,320.00 USD | 0.00 USD | `+0.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `291.50` | 1,590.00 USD | 115.73 USD | 0.00 USD | `+0.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `292.50` | 2,000.00 USD | 409.21 USD | 0.00 USD | `+1.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `293.50` | 20,250.00 USD | 18,250.00 USD | 0.00 USD | `+1.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `294.50` | 20,650.00 USD | 407.88 USD | 0.00 USD | `+1.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `295.50` | 25,380.00 USD | 4,730.00 USD | 0.00 USD | `+2.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `296.50` | 25,960.00 USD | 581.14 USD | 0.00 USD | `+2.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `298.50` | 26,500.00 USD | 535.51 USD | 0.00 USD | `+3.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `300.50` | 36,190.00 USD | 9,690.00 USD | 0.00 USD | `+3.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `304.50` | 46,910.00 USD | 10,730.00 USD | 0.00 USD | `+5.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `305.50` | 49,560.00 USD | 2,650.00 USD | 0.00 USD | `+5.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `306.50` | 50,620.00 USD | 1,060.00 USD | 0.00 USD | `+6.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `308.50` | 50,720.00 USD | 102.73 USD | 0.00 USD | `+6.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `309.50` | 65,220.00 USD | 14,500.00 USD | 0.00 USD | `+7.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `310.50` | 65,850.00 USD | 634.04 USD | 0.00 USD | `+7.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `312.50` | 66,170.00 USD | 317.19 USD | 0.00 USD | `+8.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `316.50` | 67,210.00 USD | 1,030.00 USD | 0.00 USD | `+9.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `318.50` | 72,850.00 USD | 5,650.00 USD | 0.00 USD | `+10.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `319.50` | 72,970.00 USD | 118.85 USD | 0.00 USD | `+10.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `320.50` | 73,510.00 USD | 534.59 USD | 0.00 USD | `+10.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `321.50` | 73,830.00 USD | 321.50 USD | 0.00 USD | `+11.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `325.50` | 138,750.00 USD | 64,920.00 USD | 0.00 USD | `+12.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `340.50` | 139,300.00 USD | 547.52 USD | 0.00 USD | `+17.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `345.50` | 139,440.00 USD | 138.20 USD | 0.00 USD | `+19.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `346.50` | 139,700.00 USD | 257.45 USD | 0.00 USD | `+19.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `348.50` | 139,870.00 USD | 174.25 USD | 0.00 USD | `+20.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `351.50` | 140,020.00 USD | 151.50 USD | 0.00 USD | `+21.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `357.50` | 141,480.00 USD | 1,450.00 USD | 0.00 USD | `+23.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `359.50` | 143,250.00 USD | 1,770.00 USD | 0.00 USD | `+24.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `361.50` | 143,580.00 USD | 326.07 USD | 0.00 USD | `+25.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `363.50` | 144,400.00 USD | 826.60 USD | 0.00 USD | `+25.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `364.50` | 148,130.00 USD | 3,730.00 USD | 0.00 USD | `+26.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `365.50` | 155,580.00 USD | 7,440.00 USD | 0.00 USD | `+26.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `369.50` | 156,260.00 USD | 682.84 USD | 0.00 USD | `+27.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `381.50` | 157,360.00 USD | 1,100.00 USD | 0.00 USD | `+32.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `396.50` | 158,040.00 USD | 683.96 USD | 0.00 USD | `+37.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `399.50` | 158,240.00 USD | 199.75 USD | 0.00 USD | `+38.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `400.50` | 161,740.00 USD | 3,500.00 USD | 0.00 USD | `+38.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `404.50` | 162,780.00 USD | 1,040.00 USD | 0.00 USD | `+39.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `405.50` | 163,160.00 USD | 376.71 USD | 0.00 USD | `+40.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `410.50` | 351,800.00 USD | 188,640.00 USD | 0.00 USD | `+42.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `415.50` | 357,700.00 USD | 5,900.00 USD | 0.00 USD | `+43.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `423.50` | 358,600.00 USD | 901.21 USD | 0.00 USD | `+46.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `425.50` | 366,400.00 USD | 7,800.00 USD | 0.00 USD | `+47.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `430.50` | 367,960.00 USD | 1,550.00 USD | 0.00 USD | `+48.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `435.50` | 369,340.00 USD | 1,380.00 USD | 0.00 USD | `+50.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `436.50` | 369,960.00 USD | 621.14 USD | 0.00 USD | `+51.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `440.50` | 373,340.00 USD | 3,380.00 USD | 0.00 USD | `+52.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `445.50` | 373,560.00 USD | 222.75 USD | 0.00 USD | `+54.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `450.50` | 379,160.00 USD | 5,590.00 USD | 0.00 USD | `+55.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `451.50` | 385,070.00 USD | 5,920.00 USD | 0.00 USD | `+56.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `460.50` | 386,200.00 USD | 1,130.00 USD | 0.00 USD | `+59.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `482.50` | 393,840.00 USD | 7,630.00 USD | 0.00 USD | `+66.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `487.50` | 492,310.00 USD | 98,470.00 USD | 0.00 USD | `+68.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `490.50` | 493,290.00 USD | 981.00 USD | 0.00 USD | `+69.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `499.50` | 493,790.00 USD | 499.50 USD | 0.00 USD | `+72.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `500.50` | 2,380,000.00 USD | 1,890,000.00 USD | 0.00 USD | `+73.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `501.50` | 2,380,000.00 USD | 1,000.00 USD | 0.00 USD | `+73.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `518.50` | 2,380,000.00 USD | 1,040.00 USD | 0.00 USD | `+79.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `522.50` | 2,380,000.00 USD | 340.67 USD | 0.00 USD | `+80.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `556.50` | 2,380,000.00 USD | 638.86 USD | 0.00 USD | `+92.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `575.50` | 2,390,000.00 USD | 2,590.00 USD | 0.00 USD | `+99.12%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `248.30` | 18,760,000.00 USD | 0.00 USD | 18,760,000.00 USD | 8,700.00 USD | 3,270.00 USD | 10,110.00 USD |
| `7D` | `248.70` | 18,740,000.00 USD | 0.00 USD | 18,740,000.00 USD | 43,550.00 USD | 17,040.00 USD | 28,350.00 USD |
| `7D` | `249.10` | 18,650,000.00 USD | 0.00 USD | 18,650,000.00 USD | 16,180.00 USD | 29,320.00 USD | 11,540.00 USD |
| `7D` | `249.50` | 18,600,000.00 USD | 0.00 USD | 18,600,000.00 USD | 42,290.00 USD | 32,910.00 USD | 8,340.00 USD |
| `7D` | `249.90` | 18,510,000.00 USD | 0.00 USD | 18,510,000.00 USD | 44,840.00 USD | 14,160.00 USD | 35,630.00 USD |
| `7D` | `250.30` | 18,420,000.00 USD | 0.00 USD | 18,420,000.00 USD | 18,520.00 USD | 38,250.00 USD | 3,480.00 USD |
| `7D` | `250.70` | 18,360,000.00 USD | 0.00 USD | 18,360,000.00 USD | 31,550.00 USD | 36,830.00 USD | 21,190.00 USD |
| `7D` | `251.10` | 18,270,000.00 USD | 0.00 USD | 18,270,000.00 USD | 29,390.00 USD | 49,280.00 USD | 12,010.00 USD |
| `7D` | `251.50` | 18,180,000.00 USD | 0.00 USD | 18,180,000.00 USD | 17,130.00 USD | 61,120.00 USD | 22,920.00 USD |
| `7D` | `251.90` | 18,080,000.00 USD | 0.00 USD | 18,080,000.00 USD | 74,710.00 USD | 48,150.00 USD | 43,130.00 USD |
| `7D` | `252.30` | 17,910,000.00 USD | 0.00 USD | 17,910,000.00 USD | 51,600.00 USD | 23,430.00 USD | 12,750.00 USD |
| `7D` | `252.70` | 17,820,000.00 USD | 0.00 USD | 17,820,000.00 USD | 43,080.00 USD | 19,890.00 USD | 15,320.00 USD |
| `7D` | `253.10` | 17,740,000.00 USD | 0.00 USD | 17,740,000.00 USD | 13,370.00 USD | 25,630.00 USD | 4,290.00 USD |
| `7D` | `253.50` | 17,700,000.00 USD | 0.00 USD | 17,700,000.00 USD | 24,970.00 USD | 34,890.00 USD | 50,520.00 USD |
| `7D` | `253.90` | 17,590,000.00 USD | 0.00 USD | 17,590,000.00 USD | 4,930.00 USD | 29,760.00 USD | 21,980.00 USD |
| `7D` | `254.30` | 17,530,000.00 USD | 0.00 USD | 17,530,000.00 USD | 44,770.00 USD | 28,990.00 USD | 3,830.00 USD |
| `7D` | `254.70` | 17,460,000.00 USD | 0.00 USD | 17,460,000.00 USD | 23,800.00 USD | 12,800.00 USD | 12,580.00 USD |
| `7D` | `255.10` | 17,410,000.00 USD | 0.00 USD | 17,410,000.00 USD | 14,770.00 USD | 11,150.00 USD | 31,750.00 USD |
| `7D` | `255.50` | 17,350,000.00 USD | 0.00 USD | 17,350,000.00 USD | 51,410.00 USD | 978.50 USD | 26,290.00 USD |
| `7D` | `255.90` | 17,270,000.00 USD | 0.00 USD | 17,270,000.00 USD | 16,050.00 USD | 30,780.00 USD | 39,360.00 USD |
| `7D` | `256.30` | 17,190,000.00 USD | 0.00 USD | 17,190,000.00 USD | 88,910.00 USD | 21,560.00 USD | 29,760.00 USD |
| `7D` | `256.70` | 17,040,000.00 USD | 0.00 USD | 17,040,000.00 USD | 31,480.00 USD | 14,630.00 USD | 23,090.00 USD |
| `7D` | `257.10` | 16,980,000.00 USD | 0.00 USD | 16,980,000.00 USD | 27,360.00 USD | 3,120.00 USD | 47,830.00 USD |
| `1D` | `257.50` | 8,100,000.00 USD | 0.00 USD | 8,100,000.00 USD | 4,510.00 USD | 5,710.00 USD | 8,410.00 USD |
| `7D` | `257.50` | 16,900,000.00 USD | 0.00 USD | 16,900,000.00 USD | 27,690.00 USD | 1,950.00 USD | 10,260.00 USD |
| `1D` | `257.90` | 8,080,000.00 USD | 0.00 USD | 8,080,000.00 USD | 161.87 USD | 991.50 USD | 16,890.00 USD |
| `7D` | `257.90` | 16,860,000.00 USD | 0.00 USD | 16,860,000.00 USD | 35,520.00 USD | 5,470.00 USD | 7,940.00 USD |
| `1D` | `258.30` | 8,060,000.00 USD | 0.00 USD | 8,060,000.00 USD | 1,370.00 USD | 8,380.00 USD | 13,230.00 USD |
| `7D` | `258.30` | 16,810,000.00 USD | 0.00 USD | 16,810,000.00 USD | 102,130.00 USD | 52,010.00 USD | 30,830.00 USD |
| `1D` | `258.70` | 8,040,000.00 USD | 0.00 USD | 8,040,000.00 USD | 5,020.00 USD | 5,060.00 USD | 11,840.00 USD |
| `7D` | `258.70` | 16,620,000.00 USD | 0.00 USD | 16,620,000.00 USD | 76,500.00 USD | 4,180.00 USD | 36,910.00 USD |
| `1D` | `259.10` | 8,020,000.00 USD | 0.00 USD | 8,020,000.00 USD | 24,070.00 USD | 9,900.00 USD | 10,720.00 USD |
| `7D` | `259.10` | 16,510,000.00 USD | 0.00 USD | 16,510,000.00 USD | 19,700.00 USD | 15,870.00 USD | 26,410.00 USD |
| `1D` | `259.50` | 7,970,000.00 USD | 0.00 USD | 7,970,000.00 USD | 4,620.00 USD | 2,470.00 USD | 3,360.00 USD |
| `7D` | `259.50` | 16,440,000.00 USD | 0.00 USD | 16,440,000.00 USD | 2,100.00 USD | 34,490.00 USD | 91.84 USD |
| `1D` | `259.90` | 7,960,000.00 USD | 0.00 USD | 7,960,000.00 USD | 12,820.00 USD | 17,870.00 USD | 23,400.00 USD |
| `7D` | `259.90` | 16,410,000.00 USD | 0.00 USD | 16,410,000.00 USD | 18,950.00 USD | 9,160.00 USD | 57.42 USD |
| `1D` | `260.30` | 7,910,000.00 USD | 0.00 USD | 7,910,000.00 USD | 3,100.00 USD | 9,440.00 USD | 822.76 USD |
| `7D` | `260.30` | 16,380,000.00 USD | 0.00 USD | 16,380,000.00 USD | 23,380.00 USD | 9,140.00 USD | 8,920.00 USD |
| `1D` | `260.70` | 7,890,000.00 USD | 0.00 USD | 7,890,000.00 USD | 5,040.00 USD | 15,040.00 USD | 7,760.00 USD |
| `7D` | `260.70` | 16,340,000.00 USD | 0.00 USD | 16,340,000.00 USD | 15,620.00 USD | 47,200.00 USD | 60,210.00 USD |
| `1D` | `261.10` | 7,870,000.00 USD | 0.00 USD | 7,870,000.00 USD | 12,720.00 USD | 6,900.00 USD | 6,670.00 USD |
| `7D` | `261.10` | 16,210,000.00 USD | 0.00 USD | 16,210,000.00 USD | 6,540.00 USD | 33,150.00 USD | 16,000.00 USD |
| `1D` | `261.50` | 7,840,000.00 USD | 0.00 USD | 7,840,000.00 USD | 8,750.00 USD | 14,260.00 USD | 2.10 USD |
| `7D` | `261.50` | 16,160,000.00 USD | 0.00 USD | 16,160,000.00 USD | 16,390.00 USD | 36,570.00 USD | 6,560.00 USD |
| `1D` | `261.90` | 7,820,000.00 USD | 0.00 USD | 7,820,000.00 USD | 4,920.00 USD | 4,330.00 USD | 10,920.00 USD |
| `7D` | `261.90` | 16,100,000.00 USD | 0.00 USD | 16,100,000.00 USD | 54,070.00 USD | 37,990.00 USD | 46,200.00 USD |
| `1D` | `262.30` | 7,800,000.00 USD | 0.00 USD | 7,800,000.00 USD | 8,640.00 USD | 626.24 USD | 5,590.00 USD |
| `7D` | `262.30` | 15,960,000.00 USD | 0.00 USD | 15,960,000.00 USD | 43,400.00 USD | 47,100.00 USD | 1.95 USD |
| `1D` | `262.70` | 7,780,000.00 USD | 0.00 USD | 7,780,000.00 USD | 150.60 USD | 1,190.00 USD | 12.23 USD |
| `7D` | `262.70` | 15,870,000.00 USD | 0.00 USD | 15,870,000.00 USD | 56,340.00 USD | 37,260.00 USD | 26,770.00 USD |
| `1D` | `263.10` | 7,780,000.00 USD | 0.00 USD | 7,780,000.00 USD | 8,670.00 USD | 571.81 USD | 7,500.00 USD |
| `7D` | `263.10` | 15,750,000.00 USD | 0.00 USD | 15,750,000.00 USD | 37,610.00 USD | 14,780.00 USD | 37,000.00 USD |
| `1D` | `263.50` | 7,760,000.00 USD | 0.00 USD | 7,760,000.00 USD | 560.34 USD | 839.81 USD | 24,820.00 USD |
| `7D` | `263.50` | 15,660,000.00 USD | 0.00 USD | 15,660,000.00 USD | 177,230.00 USD | 82,460.00 USD | 25,270.00 USD |
| `1D` | `263.90` | 7,740,000.00 USD | 0.00 USD | 7,740,000.00 USD | 746.44 USD | 825.92 USD | 3.09 USD |
| `7D` | `263.90` | 15,380,000.00 USD | 0.00 USD | 15,380,000.00 USD | 198,210.00 USD | 33,270.00 USD | 51,730.00 USD |
| `1D` | `264.30` | 7,740,000.00 USD | 0.00 USD | 7,740,000.00 USD | 1,860.00 USD | 647.93 USD | 9.06 USD |
| `7D` | `264.30` | 15,090,000.00 USD | 0.00 USD | 15,090,000.00 USD | 41,340.00 USD | 44,170.00 USD | 10,240.00 USD |
| `1D` | `264.70` | 7,730,000.00 USD | 0.00 USD | 7,730,000.00 USD | 28,300.00 USD | 615.20 USD | 36,650.00 USD |
| `7D` | `264.70` | 15,000,000.00 USD | 0.00 USD | 15,000,000.00 USD | 54,310.00 USD | 68,740.00 USD | 43,280.00 USD |
| `1D` | `265.10` | 7,670,000.00 USD | 0.00 USD | 7,670,000.00 USD | 20,980.00 USD | 8,870.00 USD | 15,700.00 USD |
| `7D` | `265.10` | 14,830,000.00 USD | 0.00 USD | 14,830,000.00 USD | 104,580.00 USD | 58,410.00 USD | 87,140.00 USD |
| `1D` | `265.50` | 7,620,000.00 USD | 0.00 USD | 7,620,000.00 USD | 10,540.00 USD | 11,920.00 USD | 67,100.00 USD |
| `7D` | `265.50` | 14,580,000.00 USD | 0.00 USD | 14,580,000.00 USD | 65,360.00 USD | 53,690.00 USD | 79,040.00 USD |
| `1D` | `265.90` | 7,530,000.00 USD | 0.00 USD | 7,530,000.00 USD | 14,110.00 USD | 11,970.00 USD | 19.98 USD |
| `7D` | `265.90` | 14,380,000.00 USD | 0.00 USD | 14,380,000.00 USD | 60,500.00 USD | 86,890.00 USD | 29,610.00 USD |
| `1D` | `266.30` | 7,510,000.00 USD | 0.00 USD | 7,510,000.00 USD | 32,850.00 USD | 245.13 USD | 5,010.00 USD |
| `7D` | `266.30` | 14,210,000.00 USD | 0.00 USD | 14,210,000.00 USD | 197,950.00 USD | 158,200.00 USD | 71,060.00 USD |
| `1D` | `266.70` | 7,470,000.00 USD | 0.00 USD | 7,470,000.00 USD | 14,960.00 USD | 3,340.00 USD | 3,710.00 USD |
| `7D` | `266.70` | 13,780,000.00 USD | 0.00 USD | 13,780,000.00 USD | 91,720.00 USD | 53,860.00 USD | 135,810.00 USD |
| `1D` | `267.10` | 7,450,000.00 USD | 0.00 USD | 7,450,000.00 USD | 29,020.00 USD | 6,580.00 USD | 10,110.00 USD |
| `7D` | `267.10` | 13,500,000.00 USD | 0.00 USD | 13,500,000.00 USD | 122,460.00 USD | 177,330.00 USD | 68,830.00 USD |
| `1D` | `267.50` | 7,400,000.00 USD | 0.00 USD | 7,400,000.00 USD | 12,110.00 USD | 26,590.00 USD | 21.49 USD |
| `7D` | `267.50` | 13,130,000.00 USD | 0.00 USD | 13,130,000.00 USD | 106,550.00 USD | 176,700.00 USD | 65,720.00 USD |
| `1D` | `267.90` | 7,360,000.00 USD | 0.00 USD | 7,360,000.00 USD | 113,380.00 USD | 120,840.00 USD | 45,380.00 USD |
| `7D` | `267.90` | 12,780,000.00 USD | 0.00 USD | 12,780,000.00 USD | 202,290.00 USD | 214,120.00 USD | 99,040.00 USD |
| `1D` | `268.30` | 7,080,000.00 USD | 0.00 USD | 7,080,000.00 USD | 39,130.00 USD | 98,350.00 USD | 26,540.00 USD |
| `7D` | `268.30` | 12,260,000.00 USD | 0.00 USD | 12,260,000.00 USD | 118,790.00 USD | 256,410.00 USD | 74,420.00 USD |
| `1D` | `268.70` | 6,920,000.00 USD | 0.00 USD | 6,920,000.00 USD | 97,080.00 USD | 84,960.00 USD | 58,760.00 USD |
| `7D` | `268.70` | 11,810,000.00 USD | 0.00 USD | 11,810,000.00 USD | 190,630.00 USD | 159,680.00 USD | 85,850.00 USD |
| `1D` | `269.10` | 6,680,000.00 USD | 0.00 USD | 6,680,000.00 USD | 50,070.00 USD | 22,910.00 USD | 16,360.00 USD |
| `7D` | `269.10` | 11,380,000.00 USD | 0.00 USD | 11,380,000.00 USD | 285,230.00 USD | 182,200.00 USD | 89,950.00 USD |
| `1D` | `269.50` | 6,590,000.00 USD | 0.00 USD | 6,590,000.00 USD | 31,660.00 USD | 6,030.00 USD | 8,780.00 USD |
| `7D` | `269.50` | 10,820,000.00 USD | 0.00 USD | 10,820,000.00 USD | 145,740.00 USD | 91,670.00 USD | 41,400.00 USD |
| `1D` | `269.90` | 6,540,000.00 USD | 0.00 USD | 6,540,000.00 USD | 33,840.00 USD | 43,640.00 USD | 13,070.00 USD |
| `7D` | `269.90` | 10,540,000.00 USD | 0.00 USD | 10,540,000.00 USD | 79,230.00 USD | 94,580.00 USD | 13,190.00 USD |
| `1D` | `270.30` | 6,450,000.00 USD | 0.00 USD | 6,450,000.00 USD | 109,220.00 USD | 64,910.00 USD | 128,910.00 USD |
| `7D` | `270.30` | 10,350,000.00 USD | 0.00 USD | 10,350,000.00 USD | 121,790.00 USD | 159,170.00 USD | 175,150.00 USD |
| `1D` | `270.70` | 6,150,000.00 USD | 0.00 USD | 6,150,000.00 USD | 52,010.00 USD | 39,890.00 USD | 1,670.00 USD |
| `7D` | `270.70` | 9,900,000.00 USD | 0.00 USD | 9,900,000.00 USD | 286,050.00 USD | 119,110.00 USD | 158,400.00 USD |
| `1D` | `271.10` | 6,060,000.00 USD | 0.00 USD | 6,060,000.00 USD | 40,150.00 USD | 34,010.00 USD | 139,870.00 USD |
| `7D` | `271.10` | 9,340,000.00 USD | 0.00 USD | 9,340,000.00 USD | 168,820.00 USD | 123,340.00 USD | 81,840.00 USD |
| `1D` | `271.50` | 5,840,000.00 USD | 0.00 USD | 5,840,000.00 USD | 28,220.00 USD | 37,420.00 USD | 15,540.00 USD |
| `7D` | `271.50` | 8,960,000.00 USD | 0.00 USD | 8,960,000.00 USD | 170,160.00 USD | 103,050.00 USD | 86,690.00 USD |
| `1D` | `271.90` | 5,760,000.00 USD | 0.00 USD | 5,760,000.00 USD | 139,230.00 USD | 37,570.00 USD | 55,780.00 USD |
| `7D` | `271.90` | 8,600,000.00 USD | 0.00 USD | 8,600,000.00 USD | 394,890.00 USD | 60,710.00 USD | 41,630.00 USD |
| `1D` | `272.30` | 5,530,000.00 USD | 0.00 USD | 5,530,000.00 USD | 66,650.00 USD | 15,920.00 USD | 17,040.00 USD |
| `7D` | `272.30` | 8,100,000.00 USD | 0.00 USD | 8,100,000.00 USD | 240,200.00 USD | 100,770.00 USD | 128,120.00 USD |
| `1D` | `272.70` | 5,430,000.00 USD | 0.00 USD | 5,430,000.00 USD | 76,380.00 USD | 36,390.00 USD | 43,960.00 USD |
| `7D` | `272.70` | 7,630,000.00 USD | 0.00 USD | 7,630,000.00 USD | 107,310.00 USD | 286,440.00 USD | 67,210.00 USD |
| `1D` | `273.10` | 5,270,000.00 USD | 0.00 USD | 5,270,000.00 USD | 89,480.00 USD | 87,000.00 USD | 6,990.00 USD |
| `7D` | `273.10` | 7,170,000.00 USD | 0.00 USD | 7,170,000.00 USD | 223,720.00 USD | 79,710.00 USD | 86,920.00 USD |
| `1D` | `273.50` | 5,090,000.00 USD | 0.00 USD | 5,090,000.00 USD | 225,140.00 USD | 234,890.00 USD | 95,400.00 USD |
| `7D` | `273.50` | 6,780,000.00 USD | 0.00 USD | 6,780,000.00 USD | 255,770.00 USD | 331,010.00 USD | 212,650.00 USD |
| `1D` | `273.90` | 4,530,000.00 USD | 0.00 USD | 4,530,000.00 USD | 95,740.00 USD | 221,690.00 USD | 85,050.00 USD |
| `7D` | `273.90` | 5,980,000.00 USD | 0.00 USD | 5,980,000.00 USD | 296,240.00 USD | 414,010.00 USD | 210,140.00 USD |
| `1D` | `274.30` | 4,130,000.00 USD | 0.00 USD | 4,130,000.00 USD | 204,120.00 USD | 190,610.00 USD | 145,490.00 USD |
| `7D` | `274.30` | 5,060,000.00 USD | 0.00 USD | 5,060,000.00 USD | 382,210.00 USD | 250,340.00 USD | 118,730.00 USD |
| `1D` | `274.70` | 3,590,000.00 USD | 0.00 USD | 3,590,000.00 USD | 101,590.00 USD | 42,950.00 USD | 53,520.00 USD |
| `7D` | `274.70` | 4,310,000.00 USD | 0.00 USD | 4,310,000.00 USD | 325,110.00 USD | 141,540.00 USD | 105,710.00 USD |
| `1D` | `275.10` | 3,390,000.00 USD | 0.00 USD | 3,390,000.00 USD | 62,250.00 USD | 19,440.00 USD | 65,700.00 USD |
| `7D` | `275.10` | 3,740,000.00 USD | 0.00 USD | 3,740,000.00 USD | 139,440.00 USD | 114,270.00 USD | 37,050.00 USD |
| `1D` | `275.50` | 3,240,000.00 USD | 0.00 USD | 3,240,000.00 USD | 59,520.00 USD | 65,680.00 USD | 39,110.00 USD |
| `7D` | `275.50` | 3,450,000.00 USD | 0.00 USD | 3,450,000.00 USD | 2,590.00 USD | 101,070.00 USD | 40,460.00 USD |
| `1D` | `275.90` | 3,080,000.00 USD | 0.00 USD | 3,080,000.00 USD | 47,640.00 USD | 51,470.00 USD | 22,040.00 USD |
| `7D` | `275.90` | 3,310,000.00 USD | 0.00 USD | 3,310,000.00 USD | 1,950.00 USD | 0.00 USD | 65.70 USD |
| `1D` | `276.30` | 2,960,000.00 USD | 0.00 USD | 2,960,000.00 USD | 62,820.00 USD | 42,520.00 USD | 3,230.00 USD |
| `7D` | `276.30` | 3,300,000.00 USD | 0.00 USD | 3,300,000.00 USD | 2,290.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `276.70` | 2,850,000.00 USD | 0.00 USD | 2,850,000.00 USD | 10,750.00 USD | 16,180.00 USD | 0.00 USD |
| `7D` | `276.70` | 3,300,000.00 USD | 0.00 USD | 3,300,000.00 USD | 569.60 USD | 233.30 USD | 19,830.00 USD |
| `1D` | `277.10` | 2,820,000.00 USD | 0.00 USD | 2,820,000.00 USD | 13,560.00 USD | 64,370.00 USD | 45,110.00 USD |
| `7D` | `277.10` | 3,280,000.00 USD | 0.00 USD | 3,280,000.00 USD | 44,990.00 USD | 22,950.00 USD | 0.00 USD |
| `1D` | `277.50` | 2,700,000.00 USD | 0.00 USD | 2,700,000.00 USD | 57,940.00 USD | 63,410.00 USD | 5.52 USD |
| `7D` | `277.50` | 3,210,000.00 USD | 0.00 USD | 3,210,000.00 USD | 0.00 USD | 90,480.00 USD | 0.00 USD |
| `1D` | `277.90` | 2,580,000.00 USD | 0.00 USD | 2,580,000.00 USD | 12,650.00 USD | 9,490.00 USD | 0.00 USD |
| `7D` | `277.90` | 3,120,000.00 USD | 0.00 USD | 3,120,000.00 USD | 0.00 USD | 0.00 USD | 55,760.00 USD |
| `1D` | `278.30` | 2,560,000.00 USD | 0.00 USD | 2,560,000.00 USD | 61,240.00 USD | 25,470.00 USD | 57,330.00 USD |
| `7D` | `278.30` | 3,070,000.00 USD | 0.00 USD | 3,070,000.00 USD | 24,750.00 USD | 0.00 USD | 59,410.00 USD |
| `1D` | `278.70` | 2,410,000.00 USD | 0.00 USD | 2,410,000.00 USD | 26,540.00 USD | 35,300.00 USD | 10,340.00 USD |
| `7D` | `278.70` | 2,980,000.00 USD | 0.00 USD | 2,980,000.00 USD | 30,510.00 USD | 72,160.00 USD | 17,090.00 USD |
| `1D` | `279.10` | 2,340,000.00 USD | 0.00 USD | 2,340,000.00 USD | 29,260.00 USD | 23,330.00 USD | 23,180.00 USD |
| `7D` | `279.10` | 2,860,000.00 USD | 0.00 USD | 2,860,000.00 USD | 29,880.00 USD | 31,760.00 USD | 49.12 USD |
| `1D` | `279.50` | 2,260,000.00 USD | 0.00 USD | 2,260,000.00 USD | 28,380.00 USD | 10,290.00 USD | 34,800.00 USD |
| `7D` | `279.50` | 2,800,000.00 USD | 0.00 USD | 2,800,000.00 USD | 78,130.00 USD | 0.00 USD | 95,990.00 USD |
| `1D` | `279.90` | 2,190,000.00 USD | 0.00 USD | 2,190,000.00 USD | 20,320.00 USD | 0.00 USD | 17,110.00 USD |
| `1D` | `280.30` | 2,150,000.00 USD | 0.00 USD | 2,150,000.00 USD | 29,750.00 USD | 0.00 USD | 41,630.00 USD |
| `7D` | `280.30` | 2,630,000.00 USD | 0.00 USD | 2,630,000.00 USD | 0.00 USD | 0.00 USD | 53.16 USD |
| `1D` | `280.70` | 2,080,000.00 USD | 0.00 USD | 2,080,000.00 USD | 21,670.00 USD | 0.00 USD | 64,530.00 USD |
| `1D` | `281.10` | 2,000,000.00 USD | 0.00 USD | 2,000,000.00 USD | 8,920.00 USD | 0.00 USD | 66,500.00 USD |
| `7D` | `281.10` | 2,630,000.00 USD | 0.00 USD | 2,630,000.00 USD | 0.00 USD | 0.00 USD | 62,810.00 USD |
| `7D` | `281.50` | 2,560,000.00 USD | 0.00 USD | 2,560,000.00 USD | 565.82 USD | 0.00 USD | 122,390.00 USD |
| `1D` | `281.90` | 1,920,000.00 USD | 0.00 USD | 1,920,000.00 USD | 9,360.00 USD | 16,510.00 USD | 94,830.00 USD |
| `7D` | `281.90` | 2,440,000.00 USD | 0.00 USD | 2,440,000.00 USD | 0.00 USD | 0.00 USD | 117,140.00 USD |
| `1D` | `282.30` | 1,800,000.00 USD | 0.00 USD | 1,800,000.00 USD | 55,330.00 USD | 22,600.00 USD | 124,480.00 USD |
| `7D` | `282.30` | 2,320,000.00 USD | 0.00 USD | 2,320,000.00 USD | 0.00 USD | 0.00 USD | 56,220.00 USD |
| `1D` | `282.70` | 1,600,000.00 USD | 0.00 USD | 1,600,000.00 USD | 0.00 USD | 23,250.00 USD | 3,080.00 USD |
| `7D` | `282.70` | 2,270,000.00 USD | 0.00 USD | 2,270,000.00 USD | 32,190.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `283.10` | 1,570,000.00 USD | 0.00 USD | 1,570,000.00 USD | 27,120.00 USD | 44,720.00 USD | 126,930.00 USD |
| `7D` | `283.10` | 2,240,000.00 USD | 0.00 USD | 2,240,000.00 USD | 0.00 USD | 37,310.00 USD | 89,260.00 USD |
| `1D` | `283.50` | 1,370,000.00 USD | 0.00 USD | 1,370,000.00 USD | 0.00 USD | 0.00 USD | 32,960.00 USD |
| `7D` | `283.50` | 2,110,000.00 USD | 0.00 USD | 2,110,000.00 USD | 0.00 USD | 0.00 USD | 111,520.00 USD |
| `1D` | `283.90` | 1,340,000.00 USD | 0.00 USD | 1,340,000.00 USD | 0.00 USD | 30,480.00 USD | 38,790.00 USD |
| `7D` | `283.90` | 2,000,000.00 USD | 0.00 USD | 2,000,000.00 USD | 49,500.00 USD | 0.00 USD | 197,520.00 USD |
| `1D` | `284.30` | 1,270,000.00 USD | 0.00 USD | 1,270,000.00 USD | 37,810.00 USD | 46,830.00 USD | 30,860.00 USD |
| `7D` | `284.30` | 1,750,000.00 USD | 0.00 USD | 1,750,000.00 USD | 0.00 USD | 89,730.00 USD | 8,610.00 USD |
| `1D` | `284.70` | 1,150,000.00 USD | 0.00 USD | 1,150,000.00 USD | 48,190.00 USD | 54,540.00 USD | 20,690.00 USD |
| `7D` | `284.70` | 1,650,000.00 USD | 0.00 USD | 1,650,000.00 USD | 26,130.00 USD | 254,620.00 USD | 34,150.00 USD |
| `1D` | `285.10` | 1,030,000.00 USD | 0.00 USD | 1,030,000.00 USD | 20,960.00 USD | 20,580.00 USD | 62,250.00 USD |
| `7D` | `285.10` | 1,340,000.00 USD | 0.00 USD | 1,340,000.00 USD | 62,660.00 USD | 190,390.00 USD | 83,240.00 USD |
| `1D` | `285.50` | 927,560.00 USD | 0.00 USD | 927,560.00 USD | 91,500.00 USD | 95,280.00 USD | 52,020.00 USD |
| `7D` | `285.50` | 1,000,000.00 USD | 0.00 USD | 1,000,000.00 USD | 0.00 USD | 185,240.00 USD | 0.00 USD |
| `1D` | `285.90` | 688,760.00 USD | 0.00 USD | 688,760.00 USD | 0.00 USD | 42,840.00 USD | 0.00 USD |
| `7D` | `285.90` | 815,200.00 USD | 0.00 USD | 815,200.00 USD | 0.00 USD | 52,670.00 USD | 0.00 USD |
| `1D` | `286.30` | 645,920.00 USD | 0.00 USD | 645,920.00 USD | 20,960.00 USD | 11,620.00 USD | 0.00 USD |
| `7D` | `286.30` | 762,530.00 USD | 0.00 USD | 762,530.00 USD | 0.00 USD | 40,670.00 USD | 0.00 USD |
| `1D` | `286.70` | 613,330.00 USD | 0.00 USD | 613,330.00 USD | 134,800.00 USD | 85,750.00 USD | 80,840.00 USD |
| `7D` | `286.70` | 721,860.00 USD | 0.00 USD | 721,860.00 USD | 23,860.00 USD | 146,630.00 USD | 0.00 USD |
| `1D` | `287.10` | 311,950.00 USD | 0.00 USD | 311,950.00 USD | 38,480.00 USD | 136,750.00 USD | 80,690.00 USD |
| `7D` | `287.10` | 551,370.00 USD | 0.00 USD | 551,370.00 USD | 81,140.00 USD | 138,810.00 USD | 0.00 USD |
| `1D` | `287.50` | 56,020.00 USD | 0.00 USD | 56,020.00 USD | 0.00 USD | 11,010.00 USD | 0.00 USD |
| `7D` | `287.50` | 331,410.00 USD | 0.00 USD | 331,410.00 USD | 0.00 USD | 53,560.00 USD | 0.00 USD |
| `1D` | `287.90` | 45,010.00 USD | 0.00 USD | 45,010.00 USD | 0.00 USD | 0.00 USD | 33,650.00 USD |
| `7D` | `287.90` | 277,850.00 USD | 0.00 USD | 277,850.00 USD | 0.00 USD | 277,850.00 USD | 0.00 USD |
| `1D` | `288.30` | 11,360.00 USD | 0.00 USD | 11,360.00 USD | 0.00 USD | 0.00 USD | 11,360.00 USD |
| `1D` | `288.70` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `289.10` | 11,990.00 USD | 11,990.00 USD | 0.00 USD | 0.00 USD | 11,990.00 USD | 0.00 USD |
| `7D` | `289.10` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `289.50` | 927.80 USD | 927.80 USD | 0.00 USD | 0.00 USD | 927.80 USD | 0.00 USD |
| `7D` | `289.90` | 1,870.00 USD | 1,870.00 USD | 0.00 USD | 0.00 USD | 947.00 USD | 0.00 USD |
| `1D` | `291.10` | 12,000.00 USD | 12,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 5.82 USD |
| `1D` | `291.50` | 62,320.00 USD | 62,320.00 USD | 0.00 USD | 0.00 USD | 50,320.00 USD | 5.34 USD |
| `7D` | `291.50` | 57,600.00 USD | 57,600.00 USD | 0.00 USD | 0.00 USD | 55,720.00 USD | 0.00 USD |
| `1D` | `291.90` | 90,370.00 USD | 90,370.00 USD | 0.00 USD | 0.00 USD | 5,920.00 USD | 22,130.00 USD |
| `7D` | `291.90` | 178,330.00 USD | 178,330.00 USD | 0.00 USD | 0.00 USD | 120,730.00 USD | 0.00 USD |
| `1D` | `292.30` | 148,090.00 USD | 148,090.00 USD | 0.00 USD | 0.00 USD | 57,710.00 USD | 7.00 USD |
| `7D` | `292.30` | 249,420.00 USD | 249,420.00 USD | 0.00 USD | 0.00 USD | 71,060.00 USD | 22.46 USD |
| `1D` | `292.70` | 246,700.00 USD | 246,700.00 USD | 0.00 USD | 606.80 USD | 98,000.00 USD | 9.69 USD |
| `7D` | `292.70` | 336,640.00 USD | 336,640.00 USD | 0.00 USD | 0.00 USD | 87,160.00 USD | 62.48 USD |
| `1D` | `293.10` | 298,370.00 USD | 298,370.00 USD | 0.00 USD | 857.50 USD | 50,810.00 USD | 0.42 USD |
| `7D` | `293.10` | 481,670.00 USD | 481,670.00 USD | 0.00 USD | 0.00 USD | 144,960.00 USD | 77.95 USD |
| `1D` | `293.50` | 373,550.00 USD | 373,550.00 USD | 0.00 USD | 8,580.00 USD | 64,440.00 USD | 2,150.00 USD |
| `7D` | `293.50` | 482,270.00 USD | 482,270.00 USD | 0.00 USD | 534.50 USD | 0.00 USD | 60.43 USD |
| `1D` | `293.90` | 556,300.00 USD | 556,300.00 USD | 0.00 USD | 73,070.00 USD | 31,360.00 USD | 78,330.00 USD |
| `7D` | `293.90` | 599,820.00 USD | 599,820.00 USD | 0.00 USD | 51,570.00 USD | 20,910.00 USD | 45,080.00 USD |
| `1D` | `294.30` | 743,570.00 USD | 743,570.00 USD | 0.00 USD | 62,310.00 USD | 76,770.00 USD | 48,190.00 USD |
| `7D` | `294.30` | 814,100.00 USD | 814,100.00 USD | 0.00 USD | 139,780.00 USD | 13,840.00 USD | 60,660.00 USD |
| `1D` | `294.70` | 1,090,000.00 USD | 1,090,000.00 USD | 0.00 USD | 115,590.00 USD | 103,120.00 USD | 132,210.00 USD |
| `7D` | `294.70` | 981,610.00 USD | 981,610.00 USD | 0.00 USD | 16,110.00 USD | 92,170.00 USD | 59,220.00 USD |
| `1D` | `295.10` | 1,220,000.00 USD | 1,220,000.00 USD | 0.00 USD | 32,330.00 USD | 64,510.00 USD | 25,530.00 USD |
| `7D` | `295.10` | 1,200,000.00 USD | 1,200,000.00 USD | 0.00 USD | 48,390.00 USD | 16,140.00 USD | 157,160.00 USD |
| `1D` | `295.50` | 1,540,000.00 USD | 1,540,000.00 USD | 0.00 USD | 110,930.00 USD | 118,390.00 USD | 90,360.00 USD |
| `7D` | `295.50` | 1,690,000.00 USD | 1,690,000.00 USD | 0.00 USD | 142,280.00 USD | 137,630.00 USD | 202,350.00 USD |
| `1D` | `295.90` | 1,720,000.00 USD | 1,720,000.00 USD | 0.00 USD | 105,070.00 USD | 48,120.00 USD | 33,310.00 USD |
| `7D` | `295.90` | 1,870,000.00 USD | 1,870,000.00 USD | 0.00 USD | 58,330.00 USD | 89,730.00 USD | 31,980.00 USD |
| `1D` | `296.30` | 1,960,000.00 USD | 1,960,000.00 USD | 0.00 USD | 108,090.00 USD | 95,560.00 USD | 32,400.00 USD |
| `7D` | `296.30` | 2,090,000.00 USD | 2,090,000.00 USD | 0.00 USD | 26,350.00 USD | 77,570.00 USD | 120,790.00 USD |
| `1D` | `296.70` | 2,160,000.00 USD | 2,160,000.00 USD | 0.00 USD | 41,440.00 USD | 64,890.00 USD | 94,290.00 USD |
| `7D` | `296.70` | 2,350,000.00 USD | 2,350,000.00 USD | 0.00 USD | 118,130.00 USD | 1,060.00 USD | 144,600.00 USD |
| `1D` | `297.10` | 2,300,000.00 USD | 2,300,000.00 USD | 0.00 USD | 52,650.00 USD | 20,560.00 USD | 68,850.00 USD |
| `7D` | `297.10` | 2,520,000.00 USD | 2,520,000.00 USD | 0.00 USD | 89,710.00 USD | 51,160.00 USD | 27,790.00 USD |
| `1D` | `297.50` | 2,330,000.00 USD | 2,330,000.00 USD | 0.00 USD | 6,280.00 USD | 939.55 USD | 20,820.00 USD |
| `7D` | `297.50` | 2,620,000.00 USD | 2,620,000.00 USD | 0.00 USD | 3,940.00 USD | 58,600.00 USD | 34,690.00 USD |
| `1D` | `297.90` | 2,370,000.00 USD | 2,370,000.00 USD | 0.00 USD | 1,150.00 USD | 7,600.00 USD | 32,940.00 USD |
| `7D` | `297.90` | 2,730,000.00 USD | 2,730,000.00 USD | 0.00 USD | 16,990.00 USD | 39,840.00 USD | 54,850.00 USD |
| `1D` | `298.30` | 2,560,000.00 USD | 2,560,000.00 USD | 0.00 USD | 44,780.00 USD | 8,520.00 USD | 137,760.00 USD |
| `7D` | `298.30` | 2,850,000.00 USD | 2,850,000.00 USD | 0.00 USD | 32,250.00 USD | 41,860.00 USD | 48,020.00 USD |
| `1D` | `298.70` | 2,680,000.00 USD | 2,680,000.00 USD | 0.00 USD | 25,530.00 USD | 13,400.00 USD | 80,710.00 USD |
| `7D` | `298.70` | 2,940,000.00 USD | 2,940,000.00 USD | 0.00 USD | 69,820.00 USD | 11,780.00 USD | 112.32 USD |
| `1D` | `299.10` | 2,790,000.00 USD | 2,790,000.00 USD | 0.00 USD | 48,760.00 USD | 22,810.00 USD | 38,000.00 USD |
| `7D` | `299.10` | 3,020,000.00 USD | 3,020,000.00 USD | 0.00 USD | 1,100.00 USD | 993.25 USD | 85,820.00 USD |
| `1D` | `299.50` | 2,880,000.00 USD | 2,880,000.00 USD | 0.00 USD | 28,240.00 USD | 29,040.00 USD | 29,670.00 USD |
| `7D` | `299.50` | 3,030,000.00 USD | 3,030,000.00 USD | 0.00 USD | 3,330.00 USD | 2,700.00 USD | 0.00 USD |
| `1D` | `299.90` | 2,920,000.00 USD | 2,920,000.00 USD | 0.00 USD | 17,990.00 USD | 17,070.00 USD | 7,710.00 USD |
| `7D` | `299.90` | 3,110,000.00 USD | 3,110,000.00 USD | 0.00 USD | 55,220.00 USD | 8,330.00 USD | 19,830.00 USD |
| `1D` | `300.30` | 3,020,000.00 USD | 3,020,000.00 USD | 0.00 USD | 35,780.00 USD | 32,740.00 USD | 34,860.00 USD |
| `7D` | `300.30` | 3,110,000.00 USD | 3,110,000.00 USD | 0.00 USD | 866.20 USD | 1,190.00 USD | 16.16 USD |
| `1D` | `300.70` | 3,110,000.00 USD | 3,110,000.00 USD | 0.00 USD | 10,820.00 USD | 37,840.00 USD | 35,450.00 USD |
| `7D` | `300.70` | 3,230,000.00 USD | 3,230,000.00 USD | 0.00 USD | 24,140.00 USD | 70,210.00 USD | 19,730.00 USD |
| `1D` | `301.10` | 3,180,000.00 USD | 3,180,000.00 USD | 0.00 USD | 36,200.00 USD | 28,610.00 USD | 2,060.00 USD |
| `7D` | `301.10` | 3,380,000.00 USD | 3,380,000.00 USD | 0.00 USD | 23,380.00 USD | 32,100.00 USD | 90,900.00 USD |
| `1D` | `301.50` | 3,280,000.00 USD | 3,280,000.00 USD | 0.00 USD | 31,870.00 USD | 27,310.00 USD | 44,030.00 USD |
| `7D` | `301.50` | 3,610,000.00 USD | 3,610,000.00 USD | 0.00 USD | 85,980.00 USD | 85,500.00 USD | 59,610.00 USD |
| `1D` | `301.90` | 3,380,000.00 USD | 3,380,000.00 USD | 0.00 USD | 39,820.00 USD | 51,210.00 USD | 11,590.00 USD |
| `7D` | `301.90` | 3,810,000.00 USD | 3,810,000.00 USD | 0.00 USD | 51,660.00 USD | 123,250.00 USD | 26,220.00 USD |
| `1D` | `302.30` | 3,410,000.00 USD | 3,410,000.00 USD | 0.00 USD | 5,320.00 USD | 12,080.00 USD | 10,300.00 USD |
| `7D` | `302.30` | 3,930,000.00 USD | 3,930,000.00 USD | 0.00 USD | 1,560.00 USD | 125,480.00 USD | 5.75 USD |
| `1D` | `302.70` | 3,470,000.00 USD | 3,470,000.00 USD | 0.00 USD | 11,520.00 USD | 11,290.00 USD | 41,320.00 USD |
| `7D` | `302.70` | 4,120,000.00 USD | 4,120,000.00 USD | 0.00 USD | 71,700.00 USD | 70,100.00 USD | 41,770.00 USD |
| `1D` | `303.10` | 3,510,000.00 USD | 3,510,000.00 USD | 0.00 USD | 21,200.00 USD | 1,360.00 USD | 14,740.00 USD |
| `7D` | `303.10` | 4,160,000.00 USD | 4,160,000.00 USD | 0.00 USD | 0.00 USD | 39,740.00 USD | 163.74 USD |
| `1D` | `303.50` | 3,530,000.00 USD | 3,530,000.00 USD | 0.00 USD | 12,100.00 USD | 248.89 USD | 6,250.00 USD |
| `7D` | `303.50` | 4,160,000.00 USD | 4,160,000.00 USD | 0.00 USD | 0.00 USD | 173.09 USD | 152.72 USD |
| `1D` | `303.90` | 3,580,000.00 USD | 3,580,000.00 USD | 0.00 USD | 29,930.00 USD | 3,780.00 USD | 18,760.00 USD |
| `7D` | `303.90` | 4,210,000.00 USD | 4,210,000.00 USD | 0.00 USD | 21,140.00 USD | 10,490.00 USD | 24,580.00 USD |
| `1D` | `304.30` | 3,640,000.00 USD | 3,640,000.00 USD | 0.00 USD | 4,310.00 USD | 5,410.00 USD | 48,560.00 USD |
| `7D` | `304.30` | 4,220,000.00 USD | 4,220,000.00 USD | 0.00 USD | 2,070.00 USD | 174.44 USD | 99.53 USD |
| `1D` | `304.70` | 3,700,000.00 USD | 3,700,000.00 USD | 0.00 USD | 9,700.00 USD | 5,010.00 USD | 40,350.00 USD |
| `7D` | `304.70` | 4,230,000.00 USD | 4,230,000.00 USD | 0.00 USD | 3,610.00 USD | 11,790.00 USD | 2,060.00 USD |
| `1D` | `305.10` | 3,710,000.00 USD | 3,710,000.00 USD | 0.00 USD | 9,360.00 USD | 236.66 USD | 2,010.00 USD |
| `7D` | `305.10` | 4,580,000.00 USD | 4,580,000.00 USD | 0.00 USD | 127,730.00 USD | 131,900.00 USD | 84,440.00 USD |
| `1D` | `305.50` | 3,720,000.00 USD | 3,720,000.00 USD | 0.00 USD | 5,430.00 USD | 1,760.00 USD | 1,500.00 USD |
| `7D` | `305.50` | 4,740,000.00 USD | 4,740,000.00 USD | 0.00 USD | 94,240.00 USD | 19,010.00 USD | 52,970.00 USD |
| `1D` | `305.90` | 3,730,000.00 USD | 3,730,000.00 USD | 0.00 USD | 9,650.00 USD | 2,750.00 USD | 1,930.00 USD |
| `7D` | `305.90` | 4,860,000.00 USD | 4,860,000.00 USD | 0.00 USD | 58,070.00 USD | 53,970.00 USD | 3,520.00 USD |
| `1D` | `306.30` | 3,740,000.00 USD | 3,740,000.00 USD | 0.00 USD | 4,260.00 USD | 3,210.00 USD | 1,390.00 USD |
| `7D` | `306.30` | 5,000,000.00 USD | 5,000,000.00 USD | 0.00 USD | 29,420.00 USD | 47,840.00 USD | 63,790.00 USD |
| `1D` | `306.70` | 3,770,000.00 USD | 3,770,000.00 USD | 0.00 USD | 4,420.00 USD | 21,850.00 USD | 3,850.00 USD |
| `7D` | `306.70` | 5,110,000.00 USD | 5,110,000.00 USD | 0.00 USD | 27,190.00 USD | 29,850.00 USD | 54,570.00 USD |
| `1D` | `307.10` | 3,860,000.00 USD | 3,860,000.00 USD | 0.00 USD | 33,050.00 USD | 42,000.00 USD | 13,710.00 USD |
| `7D` | `307.10` | 5,360,000.00 USD | 5,360,000.00 USD | 0.00 USD | 60,720.00 USD | 90,210.00 USD | 98,880.00 USD |
| `1D` | `307.50` | 3,900,000.00 USD | 3,900,000.00 USD | 0.00 USD | 6,340.00 USD | 22,140.00 USD | 9,430.00 USD |
| `7D` | `307.50` | 5,580,000.00 USD | 5,580,000.00 USD | 0.00 USD | 57,330.00 USD | 114,040.00 USD | 41,580.00 USD |
| `1D` | `307.90` | 3,980,000.00 USD | 3,980,000.00 USD | 0.00 USD | 33,320.00 USD | 30,510.00 USD | 21,640.00 USD |
| `7D` | `307.90` | 5,860,000.00 USD | 5,860,000.00 USD | 0.00 USD | 125,550.00 USD | 94,530.00 USD | 65,460.00 USD |
| `1D` | `308.30` | 4,010,000.00 USD | 4,010,000.00 USD | 0.00 USD | 13,820.00 USD | 7,420.00 USD | 5,640.00 USD |
| `7D` | `308.30` | 6,140,000.00 USD | 6,140,000.00 USD | 0.00 USD | 129,220.00 USD | 40,480.00 USD | 109,540.00 USD |
| `1D` | `308.70` | 4,020,000.00 USD | 4,020,000.00 USD | 0.00 USD | 5,550.00 USD | 298.40 USD | 3,480.00 USD |
| `7D` | `308.70` | 6,250,000.00 USD | 6,250,000.00 USD | 0.00 USD | 67,430.00 USD | 31,490.00 USD | 15,420.00 USD |
| `1D` | `309.10` | 4,040,000.00 USD | 4,040,000.00 USD | 0.00 USD | 12,160.00 USD | 6,430.00 USD | 2,980.00 USD |
| `7D` | `309.10` | 6,370,000.00 USD | 6,370,000.00 USD | 0.00 USD | 38,660.00 USD | 39,620.00 USD | 39,810.00 USD |
| `1D` | `309.50` | 4,080,000.00 USD | 4,080,000.00 USD | 0.00 USD | 12,390.00 USD | 22,900.00 USD | 8,280.00 USD |
| `7D` | `309.50` | 6,570,000.00 USD | 6,570,000.00 USD | 0.00 USD | 47,540.00 USD | 51,380.00 USD | 101,860.00 USD |
| `1D` | `309.90` | 4,090,000.00 USD | 4,090,000.00 USD | 0.00 USD | 8,500.00 USD | 2,590.00 USD | 978.51 USD |
| `7D` | `309.90` | 6,780,000.00 USD | 6,780,000.00 USD | 0.00 USD | 19,540.00 USD | 106,330.00 USD | 75,880.00 USD |
| `1D` | `310.30` | 4,100,000.00 USD | 4,100,000.00 USD | 0.00 USD | 232.38 USD | 7,040.00 USD | 2.37 USD |
| `7D` | `310.30` | 7,010,000.00 USD | 7,010,000.00 USD | 0.00 USD | 47,320.00 USD | 107,890.00 USD | 76,830.00 USD |
| `1D` | `310.70` | 4,100,000.00 USD | 4,100,000.00 USD | 0.00 USD | 144.00 USD | 421.81 USD | 2.98 USD |
| `7D` | `310.70` | 7,130,000.00 USD | 7,130,000.00 USD | 0.00 USD | 65,370.00 USD | 50,820.00 USD | 3,850.00 USD |
| `1D` | `311.10` | 4,110,000.00 USD | 4,110,000.00 USD | 0.00 USD | 134.35 USD | 2,050.00 USD | 4,090.00 USD |
| `7D` | `311.10` | 7,290,000.00 USD | 7,290,000.00 USD | 0.00 USD | 59,270.00 USD | 59,630.00 USD | 47,640.00 USD |
| `1D` | `311.50` | 4,160,000.00 USD | 4,160,000.00 USD | 0.00 USD | 25,300.00 USD | 6,590.00 USD | 18,300.00 USD |
| `7D` | `311.50` | 7,340,000.00 USD | 7,340,000.00 USD | 0.00 USD | 37,540.00 USD | 6,860.00 USD | 5,690.00 USD |
| `1D` | `311.90` | 4,160,000.00 USD | 4,160,000.00 USD | 0.00 USD | 2,810.00 USD | 0.00 USD | 4.48 USD |
| `7D` | `311.90` | 7,430,000.00 USD | 7,430,000.00 USD | 0.00 USD | 48,410.00 USD | 10,970.00 USD | 26,180.00 USD |
| `1D` | `312.30` | 4,180,000.00 USD | 4,180,000.00 USD | 0.00 USD | 6,410.00 USD | 5,330.00 USD | 8,690.00 USD |
| `7D` | `312.30` | 7,510,000.00 USD | 7,510,000.00 USD | 0.00 USD | 30,350.00 USD | 11,070.00 USD | 34,540.00 USD |
| `1D` | `312.70` | 4,200,000.00 USD | 4,200,000.00 USD | 0.00 USD | 14,010.00 USD | 2,180.00 USD | 39.02 USD |
| `7D` | `312.70` | 7,590,000.00 USD | 7,590,000.00 USD | 0.00 USD | 16,880.00 USD | 30,630.00 USD | 39,500.00 USD |
| `1D` | `313.10` | 4,210,000.00 USD | 4,210,000.00 USD | 0.00 USD | 5,080.00 USD | 1,940.00 USD | 0.96 USD |
| `7D` | `313.10` | 7,700,000.00 USD | 7,700,000.00 USD | 0.00 USD | 52,780.00 USD | 16,920.00 USD | 37,170.00 USD |
| `1D` | `313.50` | 4,220,000.00 USD | 4,220,000.00 USD | 0.00 USD | 7,160.00 USD | 4,770.00 USD | 2,580.00 USD |
| `7D` | `313.50` | 7,780,000.00 USD | 7,780,000.00 USD | 0.00 USD | 34,410.00 USD | 14,970.00 USD | 27,720.00 USD |
| `1D` | `313.90` | 4,240,000.00 USD | 4,240,000.00 USD | 0.00 USD | 4,760.00 USD | 10,330.00 USD | 10,050.00 USD |
| `7D` | `313.90` | 7,870,000.00 USD | 7,870,000.00 USD | 0.00 USD | 44,540.00 USD | 15,260.00 USD | 31,470.00 USD |
| `1D` | `314.30` | 4,260,000.00 USD | 4,260,000.00 USD | 0.00 USD | 4,210.00 USD | 5,710.00 USD | 3,420.00 USD |
| `7D` | `314.30` | 7,970,000.00 USD | 7,970,000.00 USD | 0.00 USD | 51,980.00 USD | 307.60 USD | 51,780.00 USD |
| `1D` | `314.70` | 4,270,000.00 USD | 4,270,000.00 USD | 0.00 USD | 303.95 USD | 0.00 USD | 8,330.00 USD |
| `7D` | `314.70` | 7,990,000.00 USD | 7,990,000.00 USD | 0.00 USD | 9,830.00 USD | 0.00 USD | 10,290.00 USD |
| `1D` | `315.10` | 4,280,000.00 USD | 4,280,000.00 USD | 0.00 USD | 32.50 USD | 0.00 USD | 10,730.00 USD |
| `7D` | `315.10` | 8,020,000.00 USD | 8,020,000.00 USD | 0.00 USD | 29,590.00 USD | 547.95 USD | 0.00 USD |
| `1D` | `315.50` | 4,300,000.00 USD | 4,300,000.00 USD | 0.00 USD | 129.37 USD | 3,270.00 USD | 19,390.00 USD |
| `7D` | `315.50` | 8,080,000.00 USD | 8,080,000.00 USD | 0.00 USD | 13,690.00 USD | 9,550.00 USD | 30,790.00 USD |
| `1D` | `315.90` | 4,310,000.00 USD | 4,310,000.00 USD | 0.00 USD | 1,470.00 USD | 5,260.00 USD | 43.23 USD |
| `7D` | `315.90` | 8,170,000.00 USD | 8,170,000.00 USD | 0.00 USD | 39,580.00 USD | 41,220.00 USD | 17,430.00 USD |
| `1D` | `316.30` | 4,340,000.00 USD | 4,340,000.00 USD | 0.00 USD | 12,450.00 USD | 5,050.00 USD | 11,800.00 USD |
| `7D` | `316.30` | 8,240,000.00 USD | 8,240,000.00 USD | 0.00 USD | 451.45 USD | 19,940.00 USD | 43,430.00 USD |
| `1D` | `316.70` | 4,370,000.00 USD | 4,370,000.00 USD | 0.00 USD | 16,490.00 USD | 8,870.00 USD | 10,710.00 USD |
| `7D` | `316.70` | 8,310,000.00 USD | 8,310,000.00 USD | 0.00 USD | 18,110.00 USD | 30,550.00 USD | 18,380.00 USD |
| `1D` | `317.10` | 4,380,000.00 USD | 4,380,000.00 USD | 0.00 USD | 3,940.00 USD | 2,260.00 USD | 3,360.00 USD |
| `7D` | `317.10` | 8,310,000.00 USD | 8,310,000.00 USD | 0.00 USD | 1,810.00 USD | 1,110.00 USD | 69.80 USD |
| `1D` | `317.50` | 4,420,000.00 USD | 4,420,000.00 USD | 0.00 USD | 11,570.00 USD | 14,470.00 USD | 13,510.00 USD |
| `7D` | `317.50` | 8,320,000.00 USD | 8,320,000.00 USD | 0.00 USD | 14,400.00 USD | 574.27 USD | 29.51 USD |
| `1D` | `317.90` | 4,440,000.00 USD | 4,440,000.00 USD | 0.00 USD | 326.88 USD | 9,140.00 USD | 9,880.00 USD |
| `7D` | `317.90` | 8,350,000.00 USD | 8,350,000.00 USD | 0.00 USD | 21,020.00 USD | 8,200.00 USD | 193.76 USD |
| `1D` | `318.30` | 4,450,000.00 USD | 4,450,000.00 USD | 0.00 USD | 2,200.00 USD | 8,430.00 USD | 820.17 USD |
| `7D` | `318.30` | 8,410,000.00 USD | 8,410,000.00 USD | 0.00 USD | 3,320.00 USD | 26,930.00 USD | 22,340.00 USD |
| `1D` | `318.70` | 4,470,000.00 USD | 4,470,000.00 USD | 0.00 USD | 4,470.00 USD | 9,400.00 USD | 7,760.00 USD |
| `7D` | `318.70` | 8,470,000.00 USD | 8,470,000.00 USD | 0.00 USD | 10,810.00 USD | 18,570.00 USD | 37,840.00 USD |
| `1D` | `319.10` | 4,500,000.00 USD | 4,500,000.00 USD | 0.00 USD | 12,470.00 USD | 6,810.00 USD | 6,660.00 USD |
| `7D` | `319.10` | 8,490,000.00 USD | 8,490,000.00 USD | 0.00 USD | 366.90 USD | 18,060.00 USD | 49.12 USD |
| `1D` | `319.50` | 4,520,000.00 USD | 4,520,000.00 USD | 0.00 USD | 8,590.00 USD | 10,950.00 USD | 0.00 USD |
| `7D` | `319.50` | 8,490,000.00 USD | 8,490,000.00 USD | 0.00 USD | 733.55 USD | 0.00 USD | 0.00 USD |
| `1D` | `319.90` | 4,530,000.00 USD | 4,530,000.00 USD | 0.00 USD | 4,350.00 USD | 2,370.00 USD | 0.00 USD |
| `7D` | `319.90` | 8,520,000.00 USD | 8,520,000.00 USD | 0.00 USD | 446.22 USD | 22,230.00 USD | 5,330.00 USD |
| `1D` | `320.30` | 4,550,000.00 USD | 4,550,000.00 USD | 0.00 USD | 0.00 USD | 4,210.00 USD | 16,510.00 USD |
| `7D` | `320.30` | 8,600,000.00 USD | 8,600,000.00 USD | 0.00 USD | 49,430.00 USD | 10,080.00 USD | 25,260.00 USD |
| `1D` | `320.70` | 4,560,000.00 USD | 4,560,000.00 USD | 0.00 USD | 8,130.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `320.70` | 8,600,000.00 USD | 8,600,000.00 USD | 0.00 USD | 189.87 USD | 0.00 USD | 53.16 USD |
| `1D` | `321.10` | 4,560,000.00 USD | 4,560,000.00 USD | 0.00 USD | 150.60 USD | 0.00 USD | 0.00 USD |
| `7D` | `321.10` | 8,620,000.00 USD | 8,620,000.00 USD | 0.00 USD | 9,210.00 USD | 8,300.00 USD | 31.64 USD |
| `1D` | `321.50` | 4,570,000.00 USD | 4,570,000.00 USD | 0.00 USD | 8,670.00 USD | 0.00 USD | 7,500.00 USD |
| `7D` | `321.50` | 8,660,000.00 USD | 8,660,000.00 USD | 0.00 USD | 4,440.00 USD | 9,730.00 USD | 21,040.00 USD |
| `1D` | `321.90` | 4,580,000.00 USD | 4,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 8,660.00 USD |
| `7D` | `321.90` | 8,660,000.00 USD | 8,660,000.00 USD | 0.00 USD | 910.57 USD | 500.60 USD | 0.00 USD |
| `1D` | `322.30` | 4,600,000.00 USD | 4,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 16,140.00 USD |
| `7D` | `322.30` | 8,700,000.00 USD | 8,700,000.00 USD | 0.00 USD | 22,930.00 USD | 7,790.00 USD | 6,150.00 USD |
| `7D` | `322.70` | 8,710,000.00 USD | 8,710,000.00 USD | 0.00 USD | 9,620.00 USD | 6,000.00 USD | 3.32 USD |
| `7D` | `323.10` | 8,750,000.00 USD | 8,750,000.00 USD | 0.00 USD | 21,120.00 USD | 5,860.00 USD | 11,480.00 USD |
| `7D` | `323.50` | 8,760,000.00 USD | 8,760,000.00 USD | 0.00 USD | 269.10 USD | 6,780.00 USD | 0.00 USD |
| `7D` | `324.30` | 8,790,000.00 USD | 8,790,000.00 USD | 0.00 USD | 0.00 USD | 4,960.00 USD | 23,350.00 USD |
| `7D` | `324.50` | 8,800,000.00 USD | 8,800,000.00 USD | 0.00 USD | 11,060.00 USD | 0.00 USD | 0.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `318.71M` | Total OI Tokens: `1,100,355.3 BCH`
  * 1h OI Change: `+0.44%` | 4h OI Change: `+4.54%` | 24h OI Change: `-1.38%`
  * Exchange Breakdown: Binance=`94.62M` | Bybit=`41.22M` | OKX=`25.07M` | Hyperliquid=`8.20M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `3.74K` | Last 24h: `4.21K` | Last 3d: `81.66K` | Last 7d: `135.21K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0007%` | **USDT OKX** | `-0.0028%` |
| **USDT Bybit** | `0.0100%` | **USDT KuCoin** | `0.0057%` |
| **USDT MEXC** | `0.0005%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `-0.0019%` | **USDT Bitget** | `0.0066%` |
| **CoinM Binance** | `-0.0011%` | **CoinM OKX** | `0.0100%` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `BCH` | `53.08%` | `46.92%` | `1.13` | 5,620,000.00 USD |
| `15M` | `Binance` | `57.68%` | `42.32%` | `1.36` | 1,920,000.00 USD |
| `15M` | `OKX` | `56.84%` | `43.16%` | `1.32` | 1,100,000.00 USD |
| `15M` | `Bybit` | `51.32%` | `48.68%` | `1.05` | 530,260.00 USD |
| `15M` | `KuCoin` | `51.37%` | `48.63%` | `1.06` | 179,520.00 USD |
| `15M` | `Gate` | `34.39%` | `65.61%` | `0.52` | 101,580.00 USD |
| `15M` | `Bitget` | `28.84%` | `71.16%` | `0.41` | 225,610.00 USD |
| `15M` | `BingX` | `37.14%` | `62.86%` | `0.59` | 149,730.00 USD |
| `15M` | `MEXC` | `62.82%` | `37.18%` | `1.69` | 149,150.00 USD |
| `15M` | `Bitunix` | `79.33%` | `20.67%` | `3.84` | 191,490.00 USD |
| `15M` | `Hyperliquid` | `28.77%` | `71.23%` | `0.40` | 11,550.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `56.52%` | `43.48%` | `1.30` | 856,200.00 USD |
| `15M` | `Crypto.com` | `33.33%` | `66.67%` | `0.50` | 8.65 USD |
| `15M` | `WhiteBIT` | `0%` | `100%` | `0.00` | 208,960.00 USD |
| `15M` | `HTX` | `64.1%` | `35.9%` | `1.79` | 895.33 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `56.86%` | `43.14%` | `1.32` | 1,160.00 USD |
| `15M` | `Aster` | `21.38%` | `78.62%` | `0.27` | 747.74 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `57.13%` | `42.87%` | `1.33` | 698.98 USD |
| `15M` | `Whale Positions` | `57.68%` | `42.32%` | `1.36` | 1,920,000.00 USD |
| `15M` | `Global Accounts` | `53.08%` | `46.92%` | `1.13` | 5,620,000.00 USD |
| `1H` | `BCH` | `48.85%` | `51.15%` | `0.96` | 20,340,000.00 USD |
| `1H` | `Binance` | `52.17%` | `47.83%` | `1.09` | 7,220,000.00 USD |
| `1H` | `OKX` | `55.56%` | `44.44%` | `1.25` | 3,370,000.00 USD |
| `1H` | `Bybit` | `52.8%` | `47.2%` | `1.12` | 2,270,000.00 USD |
| `1H` | `KuCoin` | `51.47%` | `48.53%` | `1.06` | 608,200.00 USD |
| `1H` | `Gate` | `42.56%` | `57.44%` | `0.74` | 335,330.00 USD |
| `1H` | `Bitget` | `25.63%` | `74.37%` | `0.34` | 640,450.00 USD |
| `1H` | `BingX` | `39.15%` | `60.85%` | `0.64` | 507,660.00 USD |
| `1H` | `MEXC` | `47.2%` | `52.8%` | `0.89` | 374,860.00 USD |
| `1H` | `Bitunix` | `50.4%` | `49.6%` | `1.02` | 776,380.00 USD |
| `1H` | `Hyperliquid` | `38.15%` | `61.85%` | `0.62` | 51,040.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `51.12%` | `48.88%` | `1.05` | 3,230,000.00 USD |
| `1H` | `Crypto.com` | `50.03%` | `49.97%` | `1.00` | 86.72 USD |
| `1H` | `WhiteBIT` | `0.27%` | `99.73%` | `0.00` | 812,130.00 USD |
| `1H` | `HTX` | `61.73%` | `38.27%` | `1.61` | 4,800.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `61.39%` | `38.61%` | `1.59` | 25,930.00 USD |
| `1H` | `Aster` | `12.7%` | `87.3%` | `0.15` | 97,560.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `52.92%` | `47.08%` | `1.12` | 12,000.00 USD |
| `1H` | `Whale Positions` | `52.17%` | `47.83%` | `1.09` | 7,220,000.00 USD |
| `1H` | `Global Accounts` | `48.85%` | `51.15%` | `0.96` | 20,340,000.00 USD |
| `4H` | `BCH` | `46.86%` | `53.14%` | `0.88` | 103,550,000.00 USD |
| `4H` | `Binance` | `47.82%` | `52.18%` | `0.92` | 37,020,000.00 USD |
| `4H` | `OKX` | `48.55%` | `51.45%` | `0.94` | 21,990,000.00 USD |
| `4H` | `Bybit` | `49.36%` | `50.64%` | `0.97` | 8,530,000.00 USD |
| `4H` | `KuCoin` | `49.6%` | `50.4%` | `0.98` | 2,610,000.00 USD |
| `4H` | `Gate` | `51.99%` | `48.01%` | `1.08` | 1,980,000.00 USD |
| `4H` | `Bitget` | `49.36%` | `50.64%` | `0.97` | 3,040,000.00 USD |
| `4H` | `BingX` | `36.15%` | `63.85%` | `0.57` | 2,690,000.00 USD |
| `4H` | `MEXC` | `52.33%` | `47.67%` | `1.10` | 1,580,000.00 USD |
| `4H` | `Bitunix` | `49.78%` | `50.22%` | `0.99` | 2,910,000.00 USD |
| `4H` | `Hyperliquid` | `60.99%` | `39.01%` | `1.56` | 650,480.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `49.74%` | `50.26%` | `0.99` | 16,650,000.00 USD |
| `4H` | `Crypto.com` | `28.25%` | `71.75%` | `0.39` | 425.33 USD |
| `4H` | `WhiteBIT` | `0.3%` | `99.7%` | `0.00` | 3,340,000.00 USD |
| `4H` | `HTX` | `45.84%` | `54.16%` | `0.85` | 56,000.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `24.92%` | `75.08%` | `0.33` | 208,910.00 USD |
| `4H` | `Aster` | `23.88%` | `76.12%` | `0.31` | 194,220.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `51.23%` | `48.77%` | `1.05` | 108,490.00 USD |
| `4H` | `Whale Positions` | `47.82%` | `52.18%` | `0.92` | 37,020,000.00 USD |
| `4H` | `Global Accounts` | `46.86%` | `53.14%` | `0.88` | 103,550,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5:00 UTC` | `287.25` | `286.10` | `287.25` | `288.25` | `284.09` | 2,685,023.61 USD | 1,441,619.22 USD | 1,243,404.38 USD | 198,214.84 USD | `+7.38%` | `22B / 9S` |
| `0:00 UTC` | `290.18` | `290.75` | `290.18` | `293.42` | `286.94` | 7,434,288.46 USD | 2,860,219.97 USD | 4,574,068.49 USD | -1,713,848.52 USD | `-23.05%` | `22B / 26S` |
| `5:00 UTC` | `290.33` | `290.07` | `290.33` | `290.97` | `289.12` | 2,596,782.25 USD | 1,062,961.61 USD | 1,533,820.64 USD | -470,859.04 USD | `-18.13%` | `12B / 36S` |
| `0:00 UTC` | `287.31` | `288.38` | `287.31` | `290.09` | `287.09` | 2,309,907.78 USD | 1,171,627.08 USD | 1,138,280.70 USD | 33,346.39 USD | `+1.44%` | `26B / 14S` |
| `5:00 UTC` | `288.66` | `288.97` | `288.66` | `290.08` | `287.98` | 1,528,178.86 USD | 694,047.00 USD | 834,131.86 USD | -140,084.86 USD | `-9.17%` | `9B / 26S` |
| `0:00 UTC` | `290.00` | `289.14` | `290.00` | `290.24` | `288.04` | 1,415,488.00 USD | 804,419.88 USD | 611,068.12 USD | 193,351.76 USD | `+13.66%` | `22B / 10S` |
| `5:00 UTC` | `291.01` | `290.07` | `291.01` | `291.25` | `288.53` | 1,470,760.68 USD | 873,919.07 USD | 596,841.60 USD | 277,077.47 USD | `+18.84%` | `36B / 9S` |
| `0:00 UTC` | `290.49` | `289.33` | `290.49` | `291.59` | `287.81` | 1,897,766.44 USD | 827,805.59 USD | 1,069,960.85 USD | -242,155.26 USD | `-12.76%` | `25B / 40S` |
| `5:00 UTC` | `288.09` | `287.57` | `288.09` | `289.31` | `286.49` | 1,912,559.47 USD | 931,105.86 USD | 981,453.62 USD | -50,347.76 USD | `-2.63%` | `25B / 19S` |
| `0:00 UTC` | `289.00` | `288.79` | `289.00` | `289.20` | `288.28` | 261,990.43 USD | 155,743.80 USD | 106,246.63 USD | 49,497.16 USD | `+18.89%` | `23B / 18S` |

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
| `5m` | 28,640.00 USD | 227,700.00 USD | **`ACCUMULATION`** |
| `15m` | 62,590.00 USD | 464,950.00 USD | **`ACCUMULATION`** |
| `30m` | -34,010.00 USD | -276,730.00 USD | **`DISTRIBUTION`** |
| `1h` | 72,590.00 USD | 882,210.00 USD | **`ACCUMULATION`** |
| `2h` | -267,380.00 USD | -2,920,000.00 USD | **`DISTRIBUTION`** |
| `4h` | 260,860.00 USD | -2,410,000.00 USD | **`DISTRIBUTION`** |
| `6h` | 314,330.00 USD | -708,740.00 USD | **`DISTRIBUTION`** |
| `8h` | 261,680.00 USD | -705,380.00 USD | **`DISTRIBUTION`** |
| `12h` | 230,490.00 USD | -3,010,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -950,310.00 USD | -9,090,000.00 USD | **`DISTRIBUTION`** |
| `1w` | 284,930.00 USD | -12,210,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -13,130,000.00 USD | -136,720,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+28.64K` | 15m=`+62.59K` | 1h=`+72.59K` | 24h=`-950.31K`
* Futures Capital Netflows: 5m=`+227.70K` | 15m=`+464.95K` | 1h=`+882.21K` | 24h=`-9.09M`
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
  * Execution Entry: `276.52` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `272.69` (Risk Distance: `3.83` pts)
  * +2.5R Take Profit: `286.10`
  * Mathematical Lot Sizing: **`2.61 lots`** (Nominal Risk = `0.10 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `287.44` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `291.27` (Risk Distance: `3.83` pts)
  * +2.5R Take Profit: `277.86`
  * Mathematical Lot Sizing: **`2.61 lots`** (Nominal Risk = `0.10 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`PASSIVE_MAKER_LIMIT_ARMED`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`291.41`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
