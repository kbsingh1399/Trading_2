# 🏛️ SOVEREIGN CANDIDATE DOSSIER: BCH
**Canonical Key**: `BCH` | **Broker Instrument**: `BCHUSD.p` | **Asset Class**: `Crypto PoW`
**Timestamp**: `2026-10-29 23:07:13 IST` (`2026-10-29 17:37:13 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `289.76` | **Live Ask Quote**: `290.34` | **Mid Price**: `290.05`
- **Spread Points**: `580.00` | **Spread BPS**: `20.00 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `290.05` | VWAP Z-Score: `+0.00` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `1.00` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `50.00` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `292.08` | Lower -3.00σ Band: `288.02`
  * Upper +2.51σ Band: `291.65` | Lower -2.51σ Band: `288.45`
  * Upper +2.01σ Band: `291.27` | Lower -2.01σ Band: `288.83`
  * Upper +2.00σ Band: `291.21` | Lower -2.00σ Band: `288.89`
  * Upper +1.28σ Band: `290.86` | Lower -1.28σ Band: `289.24`
  * Upper +1.00σ Band: `290.63` | Lower -1.00σ Band: `289.47`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`290.05` | EMA-20=`290.05` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`290.05` (Slope: `+0.0000`) | EMA-100=`290.05`
  * Institutional Anchors: EMA-144=`290.05` | EMA-200=`290.05` (Slope: `+0.0000`) | EMA-233=`290.05`
- **Range Boundaries**: 24H High=`292.95` | 24H Low=`287.15` | Weekly High=`295.85` | Weekly Low=`284.25`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `286.95` (Distance: `+1.10%`)
  * Point of Control (POC) = `278.70` (Distance: `+4.09%`)
  * Value Area Low (VAL) = `276.52` (Distance: `+4.91%`)
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
  * Golden Pocket Zone (0.618 - 0.650): `288.89` - `291.21`
  * Optimal Trade Entry (OTE 0.705): `290.63`
  * Structural Invalidation Anchor (0.786): `292.37`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `289.31` | `290.23` | `288.90` | `289.01` | `2,085` | 604,217.20 USD | 73,412.74 USD | `+12.15%` | -3,363,595.82 USD | `+0.53` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `5m` | `289.01` | `289.43` | `288.52` | `288.81` | `1,168` | 337,470.78 USD | 36,657.77 USD | `+10.86%` | -3,326,938.04 USD | `+0.44` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `5m` | `288.80` | `291.12` | `288.64` | `290.66` | `2,231` | 647,904.28 USD | 326,505.87 USD | `+50.39%` | -3,000,432.17 USD | `+1.28` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `289.60` | `290.07` | `287.97` | `288.48` | `5,289` | 1,528,178.86 USD | -140,084.86 USD | `-9.17%` | -3,393,913.22 USD | `-0.26` | **`BEARISH`** | `DELTA ALIGNED` |
| `15m` | `288.48` | `290.23` | `288.03` | `289.01` | `4,896` | 1,415,488.00 USD | 193,351.76 USD | `+13.66%` | -3,200,561.46 USD | `+0.48` | **`BULLISH`** | `DELTA ALIGNED` |
| `15m` | `289.01` | `291.12` | `288.52` | `290.70` | `3,388` | 982,264.13 USD | 366,249.00 USD | `+37.29%` | -2,834,312.46 USD | `+0.83` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `1h` | `282.43` | `288.24` | `282.14` | `287.96` | `22,353` | 6,361,302.26 USD | 275,075.91 USD | `+4.32%` | -1,829,450.48 USD | `+0.48` | **`BULLISH`** | `NEUTRAL CHOP` |
| `1h` | `287.97` | `293.41` | `286.92` | `288.48` | `47,822` | 13,869,157.35 USD | -2,291,446.03 USD | `-16.52%` | -4,120,896.51 USD | `-2.84` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `1h` | `288.48` | `291.12` | `288.03` | `290.65` | `8,256` | 2,389,766.74 USD | 557,618.44 USD | `+23.33%` | -3,563,278.06 USD | `+1.02` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `4h` | `278.88` | `282.00` | `277.22` | `279.37` | `40,922` | 11,454,296.89 USD | -658,851.13 USD | `-5.75%` | -2,731,740.69 USD | `+0.02` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `279.38` | `288.24` | `277.49` | `287.96` | `74,069` | 20,847,128.37 USD | 1,744,736.30 USD | `+8.37%` | -987,004.39 USD | `+1.23` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `287.97` | `293.41` | `286.92` | `290.71` | `56,090` | 16,262,313.05 USD | -1,732,285.35 USD | `-10.65%` | -2,719,289.74 USD | `-0.83` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `288.93` | `289.90` | `275.10` | `277.35` | `99,418` | 27,984,350.92 USD | -2,870,393.66 USD | `-10.26%` | -1,919,042.18 USD | `-1.00` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `277.35` | `282.39` | `276.59` | `278.88` | `47,861` | 13,383,109.09 USD | -153,847.38 USD | `-1.15%` | -2,072,889.56 USD | `+0.33` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `278.88` | `282.00` | `277.22` | `279.37` | `40,922` | 11,454,296.89 USD | -658,851.13 USD | `-5.75%` | -2,731,740.69 USD | `+0.02` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `279.38` | `288.24` | `277.49` | `287.96` | `74,069` | 20,847,128.37 USD | 1,744,736.30 USD | `+8.37%` | -987,004.39 USD | `+1.23` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `287.97` | `293.41` | `286.92` | `290.71` | `56,090` | 16,262,313.05 USD | -1,732,285.35 USD | `-10.65%` | -2,719,289.74 USD | `-0.83` | **`BEARISH`** | `BEARISH ABSORPTION` |

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
| `BID/ASK` | None | `0.0000` | 0.00 USD | `0.00%` | Unarmored | `0.0%` | Interbank L2 | NONE |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `MID` | Regular L2 Book | - | - | - | Interbank L2 | 0.00% | Interbank |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-29 23:06:38 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `1983` | `0x12d2...f97f` | `LONG` | 1,052,698.46 USD | `3,627,243,000,000.00` | `303.26` | `290.09` | `0.000000` | -47,300.87 USD | `-4.49%` | `10X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `291.49` | 12,466.74 USD | `-` | `NEWS_INTEL` | `-` | #BCH Whale BUY: 12.47K USD at 291.4900 USD [API] | `2026-10-27 22:29:58` |
| `ANNOUNCEMENT` | `INFO` | `291.47` | 5,973.09 USD | `-` | `NEWS_INTEL` | `-` | #BCH Whale BUY: 5.97K USD at 291.4700 USD [API] | `2026-10-27 22:29:58` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`296.76` (Vol: 148,100.00 USD, Dist: `+2.02%`) | Long MP=`271.76` (Vol: 159,600.00 USD, Dist: `--6.58%`)
  * 48H Horizon: Short MP=`294.39` (Vol: 176,100.00 USD, Dist: `+1.20%`) | Long MP=`271.85` (Vol: 166,000.00 USD, Dist: `--6.55%`)
  * 3D Horizon: Short MP=`294.39` (Vol: 176,100.00 USD, Dist: `+1.20%`) | Long MP=`274.36` (Vol: 203,100.00 USD, Dist: `--5.68%`)
  * 7D Horizon: Short MP=`294.37` (Vol: 176,100.00 USD, Dist: `+1.20%`) | Long MP=`263.68` (Vol: 297,200.00 USD, Dist: `--9.35%`)
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
| `7D` | `Long Liquidation` | `248.30` | 18,730,000.00 USD | 18,730,000.00 USD | 8,700.00 USD | 3,270.00 USD | 10,090.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `248.70` | 18,710,000.00 USD | 18,710,000.00 USD | 43,550.00 USD | 17,040.00 USD | 28,350.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `249.10` | 18,620,000.00 USD | 18,620,000.00 USD | 16,180.00 USD | 29,320.00 USD | 11,560.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `249.50` | 18,560,000.00 USD | 18,560,000.00 USD | 42,290.00 USD | 32,910.00 USD | 8,340.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `249.90` | 18,480,000.00 USD | 18,480,000.00 USD | 44,840.00 USD | 14,160.00 USD | 35,610.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `250.30` | 18,390,000.00 USD | 18,390,000.00 USD | 18,520.00 USD | 38,250.00 USD | 3,480.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `250.50` | 1,330.00 USD | 188,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `250.70` | 18,320,000.00 USD | 18,320,000.00 USD | 31,550.00 USD | 36,830.00 USD | 21,190.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `251.10` | 18,240,000.00 USD | 18,240,000.00 USD | 29,390.00 USD | 49,280.00 USD | 12,010.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `251.50` | 18,140,000.00 USD | 18,140,000.00 USD | 17,130.00 USD | 61,120.00 USD | 22,910.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `251.50` | 268.35 USD | 187,380.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `251.90` | 18,040,000.00 USD | 18,040,000.00 USD | 74,710.00 USD | 48,150.00 USD | 43,110.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `252.30` | 17,880,000.00 USD | 17,880,000.00 USD | 51,600.00 USD | 23,430.00 USD | 12,810.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `252.50` | 1,030.00 USD | 187,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `252.70` | 17,790,000.00 USD | 17,790,000.00 USD | 43,080.00 USD | 19,890.00 USD | 15,320.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `253.10` | 17,710,000.00 USD | 17,710,000.00 USD | 13,370.00 USD | 25,630.00 USD | 4,300.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `253.30` | 8,210,000.00 USD | 8,210,000.00 USD | 12,160.00 USD | 22,710.00 USD | 10,550.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `253.50` | 17,670,000.00 USD | 17,670,000.00 USD | 24,970.00 USD | 34,890.00 USD | 50,520.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `253.70` | 8,160,000.00 USD | 8,160,000.00 USD | 7,980.00 USD | 7,140.00 USD | 978.51 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `253.90` | 17,560,000.00 USD | 17,560,000.00 USD | 4,930.00 USD | 29,760.00 USD | 21,970.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `254.10` | 8,150,000.00 USD | 8,150,000.00 USD | 144.00 USD | 2,440.00 USD | 3.86 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `254.30` | 17,500,000.00 USD | 17,500,000.00 USD | 44,770.00 USD | 28,990.00 USD | 3,840.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `254.50` | 8,140,000.00 USD | 8,140,000.00 USD | 134.35 USD | 2,050.00 USD | 4,090.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `254.50` | 11,650.00 USD | 186,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `254.70` | 17,420,000.00 USD | 17,420,000.00 USD | 23,800.00 USD | 12,800.00 USD | 12,610.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `254.90` | 8,140,000.00 USD | 8,140,000.00 USD | 25,070.00 USD | 6,590.00 USD | 18,300.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `255.10` | 17,370,000.00 USD | 17,370,000.00 USD | 14,770.00 USD | 11,150.00 USD | 31,750.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `255.30` | 8,090,000.00 USD | 8,090,000.00 USD | 3,050.00 USD | 39.75 USD | 29.85 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `255.50` | 17,320,000.00 USD | 17,320,000.00 USD | 51,410.00 USD | 978.50 USD | 26,250.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `255.50` | 3,660.00 USD | 174,440.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `255.70` | 8,080,000.00 USD | 8,080,000.00 USD | 14,240.00 USD | 7,440.00 USD | 8,700.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `255.90` | 17,240,000.00 USD | 17,240,000.00 USD | 16,050.00 USD | 30,780.00 USD | 39,400.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `256.10` | 8,050,000.00 USD | 8,050,000.00 USD | 16,500.00 USD | 1,970.00 USD | 1.44 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `256.30` | 17,150,000.00 USD | 17,150,000.00 USD | 88,910.00 USD | 21,560.00 USD | 29,700.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `256.50` | 8,030,000.00 USD | 8,030,000.00 USD | 7,160.00 USD | 4,770.00 USD | 2,580.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `256.50` | 2,480.00 USD | 170,780.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `256.70` | 17,010,000.00 USD | 17,010,000.00 USD | 31,480.00 USD | 14,630.00 USD | 23,090.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `256.90` | 8,020,000.00 USD | 8,020,000.00 USD | 4,760.00 USD | 10,970.00 USD | 10,050.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `257.10` | 16,940,000.00 USD | 16,940,000.00 USD | 27,360.00 USD | 3,120.00 USD | 47,810.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `257.30` | 7,990,000.00 USD | 7,990,000.00 USD | 4,320.00 USD | 10,960.00 USD | 11,750.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `257.50` | 16,860,000.00 USD | 16,860,000.00 USD | 27,690.00 USD | 1,950.00 USD | 10,280.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `257.50` | 366.42 USD | 168,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `257.70` | 7,970,000.00 USD | 7,970,000.00 USD | 479.45 USD | 0.00 USD | 4,830.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `257.90` | 16,820,000.00 USD | 16,820,000.00 USD | 35,520.00 USD | 5,470.00 USD | 7,970.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `258.10` | 7,960,000.00 USD | 7,960,000.00 USD | 3,740.00 USD | 4,120.00 USD | 25,290.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `258.30` | 16,780,000.00 USD | 16,780,000.00 USD | 102,130.00 USD | 52,010.00 USD | 30,840.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `258.50` | 7,930,000.00 USD | 7,930,000.00 USD | 1,470.00 USD | 5,260.00 USD | 45.78 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `258.50` | 176.56 USD | 167,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `258.70` | 16,590,000.00 USD | 16,590,000.00 USD | 76,500.00 USD | 4,180.00 USD | 36,890.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `258.90` | 7,920,000.00 USD | 7,920,000.00 USD | 17,930.00 USD | 11,000.00 USD | 11,810.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `259.10` | 16,470,000.00 USD | 16,470,000.00 USD | 19,700.00 USD | 15,870.00 USD | 26,350.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `259.30` | 7,880,000.00 USD | 7,880,000.00 USD | 7,430.00 USD | 4,150.00 USD | 12,490.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `259.50` | 16,410,000.00 USD | 16,410,000.00 USD | 2,100.00 USD | 34,490.00 USD | 78.88 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `259.70` | 7,860,000.00 USD | 7,860,000.00 USD | 9,280.00 USD | 16,830.00 USD | 10,080.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `259.90` | 16,370,000.00 USD | 16,370,000.00 USD | 18,950.00 USD | 9,160.00 USD | 95.87 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `260.10` | 7,820,000.00 USD | 7,820,000.00 USD | 1,420.00 USD | 9,580.00 USD | 9,890.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `260.30` | 16,350,000.00 USD | 16,350,000.00 USD | 23,380.00 USD | 9,140.00 USD | 8,940.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `260.50` | 7,800,000.00 USD | 7,800,000.00 USD | 2,850.00 USD | 8,720.00 USD | 825.30 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `260.50` | 3,860.00 USD | 167,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `260.70` | 16,300,000.00 USD | 16,300,000.00 USD | 15,620.00 USD | 47,200.00 USD | 60,150.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `260.90` | 7,790,000.00 USD | 7,790,000.00 USD | 17,240.00 USD | 11,030.00 USD | 13,930.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `261.10` | 16,180,000.00 USD | 16,180,000.00 USD | 6,540.00 USD | 33,150.00 USD | 16,040.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `261.30` | 7,750,000.00 USD | 7,750,000.00 USD | 8,630.00 USD | 13,150.00 USD | 500.69 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `261.50` | 16,130,000.00 USD | 16,130,000.00 USD | 16,390.00 USD | 23,870.00 USD | 6,590.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `261.70` | 7,720,000.00 USD | 7,720,000.00 USD | 4,750.00 USD | 3,280.00 USD | 0.78 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `261.90` | 16,080,000.00 USD | 16,080,000.00 USD | 54,070.00 USD | 37,990.00 USD | 46,200.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `262.10` | 7,720,000.00 USD | 7,720,000.00 USD | 517.32 USD | 676.61 USD | 10,920.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `262.30` | 15,940,000.00 USD | 15,940,000.00 USD | 43,400.00 USD | 47,100.00 USD | 34.49 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `262.50` | 7,700,000.00 USD | 7,700,000.00 USD | 8,380.00 USD | 850.29 USD | 5.26 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `262.50` | 1,970.00 USD | 163,890.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `262.70` | 15,850,000.00 USD | 15,850,000.00 USD | 56,340.00 USD | 37,260.00 USD | 26,790.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `262.90` | 7,690,000.00 USD | 7,690,000.00 USD | 150.60 USD | 976.53 USD | 6.97 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `263.10` | 15,730,000.00 USD | 15,730,000.00 USD | 37,610.00 USD | 14,780.00 USD | 36,950.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `263.30` | 7,690,000.00 USD | 7,690,000.00 USD | 8,890.00 USD | 116.15 USD | 16,180.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `263.50` | 15,640,000.00 USD | 15,640,000.00 USD | 177,230.00 USD | 84,800.00 USD | 25,240.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `263.70` | 7,670,000.00 USD | 7,670,000.00 USD | 414.95 USD | 1,470.00 USD | 16,150.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `263.90` | 15,350,000.00 USD | 15,350,000.00 USD | 214,570.00 USD | 41,490.00 USD | 51,710.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `264.10` | 7,650,000.00 USD | 7,650,000.00 USD | 2,210.00 USD | 184.09 USD | 7.56 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `264.30` | 15,050,000.00 USD | 15,050,000.00 USD | 41,340.00 USD | 44,170.00 USD | 10,230.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `264.50` | 7,650,000.00 USD | 7,650,000.00 USD | 800.20 USD | 733.03 USD | 36,610.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `264.50` | 280.37 USD | 161,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `264.70` | 14,950,000.00 USD | 14,950,000.00 USD | 54,310.00 USD | 68,740.00 USD | 43,320.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `264.90` | 7,610,000.00 USD | 7,610,000.00 USD | 28,630.00 USD | 1,040.00 USD | 15,670.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `265.10` | 14,780,000.00 USD | 14,780,000.00 USD | 104,580.00 USD | 58,410.00 USD | 87,170.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `265.30` | 7,560,000.00 USD | 7,560,000.00 USD | 21,010.00 USD | 8,710.00 USD | 33,520.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `265.50` | 14,530,000.00 USD | 14,530,000.00 USD | 65,360.00 USD | 53,690.00 USD | 78,900.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `265.50` | 121,910.00 USD | 161,640.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `265.70` | 7,500,000.00 USD | 7,500,000.00 USD | 24,070.00 USD | 23,390.00 USD | 33,670.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `265.90` | 14,340,000.00 USD | 14,340,000.00 USD | 60,500.00 USD | 86,890.00 USD | 29,610.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `266.10` | 7,420,000.00 USD | 7,420,000.00 USD | 10,460.00 USD | 335.05 USD | 7.04 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `266.30` | 14,160,000.00 USD | 14,160,000.00 USD | 197,950.00 USD | 158,200.00 USD | 71,190.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `266.50` | 7,410,000.00 USD | 7,410,000.00 USD | 27,700.00 USD | 3,150.00 USD | 8,720.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `266.70` | 13,730,000.00 USD | 13,730,000.00 USD | 91,720.00 USD | 53,860.00 USD | 135,830.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `266.90` | 7,370,000.00 USD | 7,370,000.00 USD | 33,550.00 USD | 6,620.00 USD | 6,770.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `267.10` | 13,450,000.00 USD | 13,450,000.00 USD | 122,460.00 USD | 177,330.00 USD | 68,840.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `267.30` | 7,320,000.00 USD | 7,320,000.00 USD | 18,230.00 USD | 11,070.00 USD | 3,350.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `267.50` | 13,080,000.00 USD | 13,080,000.00 USD | 106,550.00 USD | 176,700.00 USD | 65,790.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `267.50` | 1,490.00 USD | 39,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `267.70` | 7,290,000.00 USD | 7,290,000.00 USD | 83,350.00 USD | 112,140.00 USD | 14,410.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `267.90` | 12,730,000.00 USD | 12,730,000.00 USD | 202,290.00 USD | 214,120.00 USD | 98,960.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `268.10` | 7,080,000.00 USD | 7,080,000.00 USD | 55,490.00 USD | 80,400.00 USD | 47,150.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `268.30` | 12,220,000.00 USD | 12,220,000.00 USD | 118,790.00 USD | 256,410.00 USD | 74,450.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `268.50` | 6,900,000.00 USD | 6,900,000.00 USD | 57,190.00 USD | 101,540.00 USD | 31,670.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `268.50` | 7,020.00 USD | 38,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `268.70` | 11,770,000.00 USD | 11,770,000.00 USD | 190,630.00 USD | 159,680.00 USD | 85,870.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `268.90` | 6,710,000.00 USD | 6,710,000.00 USD | 92,000.00 USD | 36,140.00 USD | 41,690.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `269.10` | 11,330,000.00 USD | 11,330,000.00 USD | 285,230.00 USD | 182,200.00 USD | 89,970.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `269.30` | 6,540,000.00 USD | 6,540,000.00 USD | 28,630.00 USD | 16,230.00 USD | 20,850.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `269.50` | 10,770,000.00 USD | 10,770,000.00 USD | 145,740.00 USD | 91,670.00 USD | 41,400.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `269.50` | 11,700.00 USD | 31,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `269.70` | 6,470,000.00 USD | 6,470,000.00 USD | 39,010.00 USD | 24,270.00 USD | 8,680.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `269.90` | 10,490,000.00 USD | 10,490,000.00 USD | 79,230.00 USD | 94,580.00 USD | 13,270.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `270.10` | 6,400,000.00 USD | 6,400,000.00 USD | 98,640.00 USD | 77,480.00 USD | 98,230.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `270.30` | 10,310,000.00 USD | 10,310,000.00 USD | 121,790.00 USD | 159,170.00 USD | 175,050.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `270.50` | 6,120,000.00 USD | 6,120,000.00 USD | 72,430.00 USD | 36,250.00 USD | 36,810.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `270.70` | 9,850,000.00 USD | 9,850,000.00 USD | 286,050.00 USD | 119,110.00 USD | 158,340.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `270.90` | 5,980,000.00 USD | 5,980,000.00 USD | 12,030.00 USD | 24,230.00 USD | 66,890.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `271.10` | 9,290,000.00 USD | 9,290,000.00 USD | 168,820.00 USD | 123,340.00 USD | 81,880.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `271.30` | 5,880,000.00 USD | 5,880,000.00 USD | 56,610.00 USD | 46,210.00 USD | 83,200.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `271.50` | 8,910,000.00 USD | 8,910,000.00 USD | 170,160.00 USD | 103,050.00 USD | 86,690.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `271.50` | 1,000.00 USD | 19,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `271.70` | 5,690,000.00 USD | 5,690,000.00 USD | 40,290.00 USD | 27,540.00 USD | 35,800.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `271.90` | 8,550,000.00 USD | 8,550,000.00 USD | 394,890.00 USD | 60,710.00 USD | 41,650.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `272.10` | 5,590,000.00 USD | 5,590,000.00 USD | 135,480.00 USD | 39,350.00 USD | 32,720.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `272.30` | 8,060,000.00 USD | 8,060,000.00 USD | 240,200.00 USD | 100,770.00 USD | 128,110.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `272.50` | 5,380,000.00 USD | 5,380,000.00 USD | 101,210.00 USD | 31,310.00 USD | 46,830.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `272.70` | 7,590,000.00 USD | 7,590,000.00 USD | 107,310.00 USD | 286,440.00 USD | 67,280.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `272.90` | 5,200,000.00 USD | 5,200,000.00 USD | 80,060.00 USD | 58,140.00 USD | 6,760.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `273.10` | 7,130,000.00 USD | 7,130,000.00 USD | 223,720.00 USD | 79,710.00 USD | 86,920.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `273.30` | 5,050,000.00 USD | 5,050,000.00 USD | 179,830.00 USD | 208,970.00 USD | 35,220.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `273.50` | 6,740,000.00 USD | 6,740,000.00 USD | 255,770.00 USD | 331,010.00 USD | 212,650.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `273.70` | 4,630,000.00 USD | 4,630,000.00 USD | 148,250.00 USD | 182,920.00 USD | 131,450.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `273.90` | 5,940,000.00 USD | 5,940,000.00 USD | 296,240.00 USD | 414,010.00 USD | 210,040.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `274.10` | 4,170,000.00 USD | 4,170,000.00 USD | 120,870.00 USD | 238,300.00 USD | 77,880.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `274.30` | 5,020,000.00 USD | 5,020,000.00 USD | 382,210.00 USD | 250,340.00 USD | 118,730.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `274.50` | 3,730,000.00 USD | 3,730,000.00 USD | 201,380.00 USD | 84,390.00 USD | 122,290.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `274.50` | 567.94 USD | 18,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `274.70` | 4,260,000.00 USD | 4,260,000.00 USD | 325,110.00 USD | 141,540.00 USD | 105,700.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `274.90` | 3,320,000.00 USD | 3,320,000.00 USD | 72,100.00 USD | 37,590.00 USD | 79,280.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `275.10` | 3,690,000.00 USD | 3,690,000.00 USD | 139,440.00 USD | 114,270.00 USD | 37,020.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `275.30` | 3,130,000.00 USD | 3,130,000.00 USD | 75,490.00 USD | 47,550.00 USD | 45,800.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `275.50` | 3,400,000.00 USD | 3,400,000.00 USD | 2,590.00 USD | 101,070.00 USD | 40,400.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `275.70` | 2,960,000.00 USD | 2,960,000.00 USD | 12,170.00 USD | 37,310.00 USD | 8,730.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `275.90` | 3,260,000.00 USD | 3,260,000.00 USD | 1,950.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `276.10` | 2,910,000.00 USD | 2,910,000.00 USD | 82,100.00 USD | 48,180.00 USD | 22,040.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `276.30` | 3,260,000.00 USD | 3,260,000.00 USD | 2,290.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `276.50` | 2,750,000.00 USD | 2,750,000.00 USD | 13,650.00 USD | 31,830.00 USD | 3,230.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `276.50` | 205.44 USD | 17,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `276.70` | 3,250,000.00 USD | 3,250,000.00 USD | 569.60 USD | 233.30 USD | 19,870.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `276.90` | 2,710,000.00 USD | 2,710,000.00 USD | 10,750.00 USD | 20,770.00 USD | 11,360.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `277.10` | 3,230,000.00 USD | 3,230,000.00 USD | 28,890.00 USD | 22,950.00 USD | 42.47 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `277.30` | 2,660,000.00 USD | 2,660,000.00 USD | 301.20 USD | 75,230.00 USD | 21,180.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `277.50` | 3,180,000.00 USD | 3,180,000.00 USD | 0.00 USD | 90,480.00 USD | 85.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `277.70` | 2,570,000.00 USD | 2,570,000.00 USD | 57,640.00 USD | 47,660.00 USD | 5.52 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `277.90` | 3,090,000.00 USD | 3,090,000.00 USD | 0.00 USD | 0.00 USD | 55,850.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `278.10` | 2,460,000.00 USD | 2,460,000.00 USD | 12,650.00 USD | 9,490.00 USD | 28,100.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `278.30` | 3,030,000.00 USD | 3,030,000.00 USD | 24,750.00 USD | 0.00 USD | 59,450.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `278.50` | 2,410,000.00 USD | 2,410,000.00 USD | 67,950.00 USD | 25,470.00 USD | 29,220.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `278.70` | 2,950,000.00 USD | 2,950,000.00 USD | 30,510.00 USD | 72,160.00 USD | 17,080.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `278.90` | 2,290,000.00 USD | 2,290,000.00 USD | 20,180.00 USD | 27,270.00 USD | 10,340.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `279.10` | 2,830,000.00 USD | 2,830,000.00 USD | 29,880.00 USD | 0.00 USD | 9.96 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `279.30` | 2,230,000.00 USD | 2,230,000.00 USD | 53,390.00 USD | 23,330.00 USD | 44,020.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `279.50` | 2,800,000.00 USD | 2,800,000.00 USD | 78,130.00 USD | 0.00 USD | 96,030.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `279.70` | 2,110,000.00 USD | 2,110,000.00 USD | 20,320.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `280.10` | 2,090,000.00 USD | 2,090,000.00 USD | 21,040.00 USD | 0.00 USD | 36,620.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `280.30` | 2,630,000.00 USD | 2,630,000.00 USD | 0.00 USD | 0.00 USD | 55.04 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `280.50` | 2,030,000.00 USD | 2,030,000.00 USD | 30,390.00 USD | 0.00 USD | 64,990.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `280.90` | 1,940,000.00 USD | 1,940,000.00 USD | 0.00 USD | 0.00 USD | 21,660.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `281.10` | 2,630,000.00 USD | 2,630,000.00 USD | 0.00 USD | 0.00 USD | 62,810.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `281.30` | 1,910,000.00 USD | 1,910,000.00 USD | 8,920.00 USD | 0.00 USD | 66,500.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `281.50` | 2,560,000.00 USD | 2,560,000.00 USD | 565.82 USD | 0.00 USD | 122,390.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `281.70` | 1,840,000.00 USD | 1,840,000.00 USD | 9,360.00 USD | 0.00 USD | 27,950.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `281.90` | 2,440,000.00 USD | 2,440,000.00 USD | 0.00 USD | 0.00 USD | 117,140.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `282.10` | 1,800,000.00 USD | 1,800,000.00 USD | 26,680.00 USD | 39,110.00 USD | 187,730.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `282.30` | 2,320,000.00 USD | 2,320,000.00 USD | 0.00 USD | 0.00 USD | 56,220.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `282.50` | 1,550,000.00 USD | 1,550,000.00 USD | 0.00 USD | 13,450.00 USD | 3,640.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `282.70` | 2,270,000.00 USD | 2,270,000.00 USD | 0.00 USD | 0.00 USD | 7.78 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `282.90` | 1,530,000.00 USD | 1,530,000.00 USD | 0.00 USD | 54,510.00 USD | 55,460.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `283.10` | 2,270,000.00 USD | 2,270,000.00 USD | 0.00 USD | 37,310.00 USD | 89,480.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `283.30` | 1,420,000.00 USD | 1,420,000.00 USD | 0.00 USD | 0.00 USD | 78,280.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `283.50` | 2,140,000.00 USD | 2,140,000.00 USD | 0.00 USD | 0.00 USD | 111,520.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `283.70` | 1,340,000.00 USD | 1,340,000.00 USD | 0.00 USD | 30,480.00 USD | 4,100.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `283.90` | 2,030,000.00 USD | 2,030,000.00 USD | 49,500.00 USD | 0.00 USD | 197,520.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `284.10` | 1,310,000.00 USD | 1,310,000.00 USD | 37,810.00 USD | 30,760.00 USD | 69,640.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `284.30` | 1,780,000.00 USD | 1,780,000.00 USD | 0.00 USD | 89,730.00 USD | 8,610.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `284.50` | 1,170,000.00 USD | 1,170,000.00 USD | 31,830.00 USD | 54,540.00 USD | 20,690.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `284.70` | 1,680,000.00 USD | 1,680,000.00 USD | 26,130.00 USD | 191,100.00 USD | 34,230.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `284.90` | 1,060,000.00 USD | 1,060,000.00 USD | 8,520.00 USD | 0.00 USD | 20,590.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `285.10` | 1,430,000.00 USD | 1,430,000.00 USD | 62,660.00 USD | 190,390.00 USD | 83,240.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `285.30` | 1,030,000.00 USD | 1,030,000.00 USD | 20,960.00 USD | 44,060.00 USD | 65,750.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `285.50` | 1,100,000.00 USD | 1,100,000.00 USD | 0.00 USD | 185,240.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `285.50` | 17,750.00 USD | 17,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `285.70` | 902,610.00 USD | 902,610.00 USD | 91,500.00 USD | 71,120.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `285.90` | 910,790.00 USD | 910,790.00 USD | 0.00 USD | 52,670.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `286.10` | 739,990.00 USD | 739,990.00 USD | 0.00 USD | 30,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `286.30` | 858,120.00 USD | 858,120.00 USD | 0.00 USD | 40,670.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `286.50` | 709,990.00 USD | 709,990.00 USD | 111,830.00 USD | 47,210.00 USD | 37,510.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `286.70` | 817,450.00 USD | 817,450.00 USD | 23,860.00 USD | 146,630.00 USD | 1.44 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `286.90` | 513,430.00 USD | 513,430.00 USD | 82,410.00 USD | 88,910.00 USD | 124,010.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `287.10` | 646,960.00 USD | 646,960.00 USD | 81,140.00 USD | 138,810.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `287.30` | 218,090.00 USD | 218,090.00 USD | 0.00 USD | 101,950.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `287.50` | 427,000.00 USD | 427,000.00 USD | 23,560.00 USD | 53,560.00 USD | 70.92 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `287.70` | 116,140.00 USD | 116,140.00 USD | 0.00 USD | 0.00 USD | 33,650.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `287.90` | 349,800.00 USD | 349,800.00 USD | 0.00 USD | 277,850.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `288.10` | 82,490.00 USD | 82,490.00 USD | 0.00 USD | 0.00 USD | 11,360.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `288.30` | 71,950.00 USD | 71,950.00 USD | 70,080.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `288.50` | 71,130.00 USD | 71,130.00 USD | 32,470.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `288.90` | 38,650.00 USD | 38,650.00 USD | 4,630.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `289.30` | 34,020.00 USD | 34,020.00 USD | 0.00 USD | 11,990.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `289.50` | 1,870.00 USD | 1,870.00 USD | 0.00 USD | 927.80 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `289.90` | 947.00 USD | 947.00 USD | 0.00 USD | 947.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `290.90` | 22,030.00 USD | 22,030.00 USD | 0.00 USD | 22,030.00 USD | 3.40 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `291.10` | 57,860.00 USD | 57,860.00 USD | 0.00 USD | 57,860.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `291.10` | 115,720.00 USD | 115,720.00 USD | 0.00 USD | 57,860.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `291.30` | 106,900.00 USD | 106,900.00 USD | 0.00 USD | 106,120.00 USD | 783.02 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `291.50` | 171,450.00 USD | 171,450.00 USD | 0.00 USD | 55,720.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `291.70` | 202,540.00 USD | 202,540.00 USD | 0.00 USD | 41,880.00 USD | 53,760.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `291.90` | 292,180.00 USD | 292,180.00 USD | 0.00 USD | 120,730.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `292.10` | 240,910.00 USD | 240,910.00 USD | 0.00 USD | 38,360.00 USD | 9.06 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `292.30` | 363,330.00 USD | 363,330.00 USD | 0.00 USD | 71,060.00 USD | 88.06 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `292.50` | 288,280.00 USD | 288,280.00 USD | 21.70 USD | 47,340.00 USD | 10.29 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `292.70` | 450,590.00 USD | 450,590.00 USD | 0.00 USD | 87,160.00 USD | 102.79 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `292.90` | 370,540.00 USD | 370,540.00 USD | 1,020.00 USD | 81,240.00 USD | 3.04 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `293.10` | 595,610.00 USD | 595,610.00 USD | 0.00 USD | 144,960.00 USD | 65.31 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `293.30` | 431,610.00 USD | 431,610.00 USD | 476.80 USD | 60,590.00 USD | 1.58 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `293.50` | 596,170.00 USD | 596,170.00 USD | 534.50 USD | 0.00 USD | 20.19 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `293.70` | 614,640.00 USD | 614,640.00 USD | 44,580.00 USD | 77,060.00 USD | 61,390.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `293.90` | 713,700.00 USD | 713,700.00 USD | 51,570.00 USD | 20,910.00 USD | 45,050.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `294.10` | 715,510.00 USD | 715,510.00 USD | 30,790.00 USD | 36,360.00 USD | 33,720.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `294.30` | 895,800.00 USD | 895,800.00 USD | 107,580.00 USD | 13,840.00 USD | 60,680.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `294.50` | 1,040,000.00 USD | 1,040,000.00 USD | 121,000.00 USD | 112,510.00 USD | 91,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `294.70` | 1,060,000.00 USD | 1,060,000.00 USD | 16,110.00 USD | 92,170.00 USD | 59,220.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `294.90` | 1,240,000.00 USD | 1,240,000.00 USD | 41,000.00 USD | 85,800.00 USD | 70,850.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `295.10` | 1,290,000.00 USD | 1,290,000.00 USD | 48,390.00 USD | 16,140.00 USD | 157,180.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `295.30` | 1,460,000.00 USD | 1,460,000.00 USD | 108,980.00 USD | 75,850.00 USD | 37,400.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `295.50` | 1,770,000.00 USD | 1,770,000.00 USD | 142,280.00 USD | 137,630.00 USD | 202,350.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `295.50` | 612.57 USD | 612.57 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `295.70` | 1,720,000.00 USD | 1,720,000.00 USD | 112,240.00 USD | 59,530.00 USD | 87,930.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `295.90` | 1,950,000.00 USD | 1,950,000.00 USD | 58,330.00 USD | 89,730.00 USD | 31,970.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `296.10` | 1,940,000.00 USD | 1,940,000.00 USD | 82,690.00 USD | 103,910.00 USD | 29,580.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `296.30` | 2,110,000.00 USD | 2,110,000.00 USD | 26,350.00 USD | 14,050.00 USD | 120,850.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `296.50` | 2,090,000.00 USD | 2,090,000.00 USD | 49,180.00 USD | 45,550.00 USD | 57,880.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `296.70` | 2,370,000.00 USD | 2,370,000.00 USD | 118,130.00 USD | 1,060.00 USD | 144,650.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `296.90` | 2,220,000.00 USD | 2,220,000.00 USD | 29,430.00 USD | 35,780.00 USD | 69,180.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `297.10` | 2,540,000.00 USD | 2,540,000.00 USD | 89,710.00 USD | 51,160.00 USD | 27,820.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `297.30` | 2,340,000.00 USD | 2,340,000.00 USD | 63,980.00 USD | 13,480.00 USD | 38,920.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `297.50` | 2,640,000.00 USD | 2,640,000.00 USD | 3,940.00 USD | 58,600.00 USD | 34,690.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `297.70` | 2,360,000.00 USD | 2,360,000.00 USD | 807.94 USD | 723.06 USD | 16,800.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `297.90` | 2,750,000.00 USD | 2,750,000.00 USD | 16,990.00 USD | 39,840.00 USD | 54,850.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `298.10` | 2,500,000.00 USD | 2,500,000.00 USD | 58,610.00 USD | 8,120.00 USD | 73,820.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `298.30` | 2,870,000.00 USD | 2,870,000.00 USD | 32,250.00 USD | 41,860.00 USD | 48,080.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `298.50` | 2,610,000.00 USD | 2,610,000.00 USD | 8,410.00 USD | 21,250.00 USD | 84,830.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `298.70` | 2,950,000.00 USD | 2,950,000.00 USD | 69,820.00 USD | 11,780.00 USD | 17.54 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `298.90` | 2,780,000.00 USD | 2,780,000.00 USD | 35,380.00 USD | 15,820.00 USD | 118,690.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `299.10` | 3,040,000.00 USD | 3,040,000.00 USD | 1,100.00 USD | 993.25 USD | 85,830.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `299.30` | 2,880,000.00 USD | 2,880,000.00 USD | 45,920.00 USD | 23,800.00 USD | 27,850.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `299.50` | 3,050,000.00 USD | 3,050,000.00 USD | 3,330.00 USD | 2,700.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `299.50` | 1,220.00 USD | 1,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `299.70` | 2,910,000.00 USD | 2,910,000.00 USD | 4,910.00 USD | 17,410.00 USD | 9,090.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `299.90` | 3,120,000.00 USD | 3,120,000.00 USD | 39,130.00 USD | 8,330.00 USD | 19,840.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `300.10` | 3,010,000.00 USD | 3,010,000.00 USD | 33,660.00 USD | 44,530.00 USD | 22,730.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `300.30` | 3,120,000.00 USD | 3,120,000.00 USD | 866.20 USD | 1,190.00 USD | 6.52 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `300.50` | 3,050,000.00 USD | 3,050,000.00 USD | 2,940.00 USD | 10,850.00 USD | 24,730.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `300.70` | 3,230,000.00 USD | 3,230,000.00 USD | 24,140.00 USD | 70,210.00 USD | 19,740.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `300.90` | 3,110,000.00 USD | 3,110,000.00 USD | 13,240.00 USD | 32,390.00 USD | 12,770.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `301.10` | 3,380,000.00 USD | 3,380,000.00 USD | 23,380.00 USD | 32,100.00 USD | 91,130.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `301.30` | 3,220,000.00 USD | 3,220,000.00 USD | 34,050.00 USD | 46,860.00 USD | 28,550.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `301.50` | 3,610,000.00 USD | 3,610,000.00 USD | 85,980.00 USD | 85,500.00 USD | 59,580.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `301.50` | 2,380.00 USD | 4,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `301.70` | 3,280,000.00 USD | 3,280,000.00 USD | 31,990.00 USD | 12,330.00 USD | 16,730.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `301.90` | 3,810,000.00 USD | 3,810,000.00 USD | 51,660.00 USD | 123,250.00 USD | 26,240.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `302.10` | 3,370,000.00 USD | 3,370,000.00 USD | 40,760.00 USD | 37,100.00 USD | 10,340.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `302.30` | 3,910,000.00 USD | 3,910,000.00 USD | 1,560.00 USD | 93,720.00 USD | 19.74 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `302.50` | 3,420,000.00 USD | 3,420,000.00 USD | 10,520.00 USD | 10,130.00 USD | 31,130.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `302.70` | 4,090,000.00 USD | 4,090,000.00 USD | 71,700.00 USD | 72,440.00 USD | 41,620.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `302.90` | 3,430,000.00 USD | 3,430,000.00 USD | 1,230.00 USD | 1,720.00 USD | 6,560.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `303.10` | 4,130,000.00 USD | 4,130,000.00 USD | 0.00 USD | 39,740.00 USD | 211.16 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `303.30` | 3,480,000.00 USD | 3,480,000.00 USD | 32,730.00 USD | 315.99 USD | 14,710.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `303.50` | 4,130,000.00 USD | 4,130,000.00 USD | 0.00 USD | 173.09 USD | 159.88 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `303.70` | 3,500,000.00 USD | 3,500,000.00 USD | 8,390.00 USD | 3,470.00 USD | 6,250.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `303.90` | 4,190,000.00 USD | 4,190,000.00 USD | 21,140.00 USD | 10,490.00 USD | 24,480.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `304.10` | 3,570,000.00 USD | 3,570,000.00 USD | 22,810.00 USD | 980.72 USD | 53,800.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `304.30` | 4,190,000.00 USD | 4,190,000.00 USD | 2,070.00 USD | 174.44 USD | 151.22 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `304.50` | 3,650,000.00 USD | 3,650,000.00 USD | 13,310.00 USD | 9,720.00 USD | 53,870.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `304.70` | 4,210,000.00 USD | 4,210,000.00 USD | 3,610.00 USD | 11,790.00 USD | 2,060.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `304.90` | 3,650,000.00 USD | 3,650,000.00 USD | 1,110.00 USD | 240.63 USD | 2.91 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `305.10` | 4,550,000.00 USD | 4,550,000.00 USD | 127,730.00 USD | 131,900.00 USD | 84,440.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `305.30` | 3,670,000.00 USD | 3,670,000.00 USD | 11,930.00 USD | 90.03 USD | 2,010.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `305.50` | 4,720,000.00 USD | 4,720,000.00 USD | 94,240.00 USD | 19,010.00 USD | 52,950.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `305.70` | 3,680,000.00 USD | 3,680,000.00 USD | 8,200.00 USD | 1,770.00 USD | 3,410.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `305.90` | 4,830,000.00 USD | 4,830,000.00 USD | 58,070.00 USD | 53,970.00 USD | 3,580.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `306.10` | 3,690,000.00 USD | 3,690,000.00 USD | 4,210.00 USD | 2,750.00 USD | 1,350.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `306.30` | 4,970,000.00 USD | 4,970,000.00 USD | 29,420.00 USD | 47,840.00 USD | 63,810.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `306.50` | 3,700,000.00 USD | 3,700,000.00 USD | 4,740.00 USD | 9,750.00 USD | 58.13 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `306.70` | 5,090,000.00 USD | 5,090,000.00 USD | 27,190.00 USD | 29,850.00 USD | 54,510.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `306.90` | 3,790,000.00 USD | 3,790,000.00 USD | 32,060.00 USD | 40,210.00 USD | 13,060.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `307.10` | 5,340,000.00 USD | 5,340,000.00 USD | 60,720.00 USD | 90,210.00 USD | 98,860.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `307.30` | 3,840,000.00 USD | 3,840,000.00 USD | 7,930.00 USD | 34,450.00 USD | 10,930.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `307.50` | 5,550,000.00 USD | 5,550,000.00 USD | 57,330.00 USD | 114,040.00 USD | 41,560.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `307.70` | 3,900,000.00 USD | 3,900,000.00 USD | 19,670.00 USD | 27,890.00 USD | 9,610.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `307.90` | 5,830,000.00 USD | 5,830,000.00 USD | 125,550.00 USD | 94,530.00 USD | 65,370.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `308.10` | 3,950,000.00 USD | 3,950,000.00 USD | 25,570.00 USD | 11,430.00 USD | 16,390.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `308.30` | 6,110,000.00 USD | 6,110,000.00 USD | 129,220.00 USD | 40,480.00 USD | 109,680.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `308.50` | 3,960,000.00 USD | 3,960,000.00 USD | 5,570.00 USD | 3,440.00 USD | 4,260.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `308.70` | 6,230,000.00 USD | 6,230,000.00 USD | 67,430.00 USD | 31,490.00 USD | 15,430.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `308.90` | 3,990,000.00 USD | 3,990,000.00 USD | 12,710.00 USD | 5,940.00 USD | 4,140.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `309.10` | 6,350,000.00 USD | 6,350,000.00 USD | 38,660.00 USD | 39,620.00 USD | 39,820.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `309.30` | 4,010,000.00 USD | 4,010,000.00 USD | 10,230.00 USD | 12,250.00 USD | 2,370.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `309.50` | 6,550,000.00 USD | 6,550,000.00 USD | 47,540.00 USD | 51,380.00 USD | 101,820.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `309.70` | 4,050,000.00 USD | 4,050,000.00 USD | 10,860.00 USD | 13,870.00 USD | 9,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `309.90` | 6,750,000.00 USD | 6,750,000.00 USD | 19,540.00 USD | 106,330.00 USD | 75,930.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `310.10` | 4,050,000.00 USD | 4,050,000.00 USD | 4,310.00 USD | 4,770.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `310.30` | 6,980,000.00 USD | 6,980,000.00 USD | 47,320.00 USD | 107,890.00 USD | 76,820.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `310.50` | 4,060,000.00 USD | 4,060,000.00 USD | 376.38 USD | 2,810.00 USD | 3.86 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `310.50` | 517.91 USD | 4,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `310.70` | 7,100,000.00 USD | 7,100,000.00 USD | 65,370.00 USD | 50,820.00 USD | 3,850.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `310.90` | 4,060,000.00 USD | 4,060,000.00 USD | 0.00 USD | 0.00 USD | 4,090.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `311.10` | 7,270,000.00 USD | 7,270,000.00 USD | 59,270.00 USD | 59,630.00 USD | 47,610.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `311.30` | 4,080,000.00 USD | 4,080,000.00 USD | 7,760.00 USD | 2,050.00 USD | 12,190.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `311.50` | 7,320,000.00 USD | 7,320,000.00 USD | 37,540.00 USD | 6,860.00 USD | 5,630.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `311.70` | 4,120,000.00 USD | 4,120,000.00 USD | 20,470.00 USD | 6,590.00 USD | 6,120.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `311.90` | 7,400,000.00 USD | 7,400,000.00 USD | 48,410.00 USD | 10,970.00 USD | 26,190.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `312.10` | 4,120,000.00 USD | 4,120,000.00 USD | 244.00 USD | 39.75 USD | 29.51 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `312.30` | 7,480,000.00 USD | 7,480,000.00 USD | 30,350.00 USD | 11,070.00 USD | 34,640.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `312.50` | 4,150,000.00 USD | 4,150,000.00 USD | 14,240.00 USD | 7,440.00 USD | 8,700.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `312.70` | 7,570,000.00 USD | 7,570,000.00 USD | 16,880.00 USD | 30,630.00 USD | 39,510.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `312.90` | 4,160,000.00 USD | 4,160,000.00 USD | 11,420.00 USD | 23.27 USD | 1.44 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `313.10` | 7,670,000.00 USD | 7,670,000.00 USD | 52,780.00 USD | 16,920.00 USD | 37,070.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `313.30` | 4,180,000.00 USD | 4,180,000.00 USD | 8,660.00 USD | 6,710.00 USD | 2,580.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `313.50` | 7,750,000.00 USD | 7,750,000.00 USD | 34,410.00 USD | 14,970.00 USD | 27,700.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `313.70` | 4,200,000.00 USD | 4,200,000.00 USD | 8,340.00 USD | 4,380.00 USD | 10,050.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `313.90` | 7,840,000.00 USD | 7,840,000.00 USD | 44,540.00 USD | 15,260.00 USD | 31,430.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `314.10` | 4,210,000.00 USD | 4,210,000.00 USD | 0.00 USD | 11,670.00 USD | 3,420.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `314.30` | 7,940,000.00 USD | 7,940,000.00 USD | 51,980.00 USD | 307.60 USD | 51,780.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `314.50` | 4,230,000.00 USD | 4,230,000.00 USD | 4,320.00 USD | 5,250.00 USD | 8,330.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `314.70` | 7,960,000.00 USD | 7,960,000.00 USD | 9,830.00 USD | 0.00 USD | 10,330.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `314.90` | 4,240,000.00 USD | 4,240,000.00 USD | 479.45 USD | 0.00 USD | 4,830.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `315.10` | 8,000,000.00 USD | 8,000,000.00 USD | 29,590.00 USD | 547.95 USD | 41.26 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `315.30` | 4,250,000.00 USD | 4,250,000.00 USD | 3,740.00 USD | 144.50 USD | 12,070.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `315.50` | 8,050,000.00 USD | 8,050,000.00 USD | 13,690.00 USD | 9,550.00 USD | 30,770.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `315.70` | 4,280,000.00 USD | 4,280,000.00 USD | 1,370.00 USD | 8,380.00 USD | 13,230.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `315.90` | 8,150,000.00 USD | 8,150,000.00 USD | 39,580.00 USD | 41,220.00 USD | 17,390.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `316.10` | 4,300,000.00 USD | 4,300,000.00 USD | 5,020.00 USD | 5,050.00 USD | 11,840.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `316.30` | 8,210,000.00 USD | 8,210,000.00 USD | 451.45 USD | 19,940.00 USD | 43,400.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `316.50` | 4,320,000.00 USD | 4,320,000.00 USD | 12,950.00 USD | 5,380.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `316.70` | 8,280,000.00 USD | 8,280,000.00 USD | 18,110.00 USD | 30,550.00 USD | 18,370.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `316.90` | 4,340,000.00 USD | 4,340,000.00 USD | 7,030.00 USD | 3,660.00 USD | 12,480.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `317.10` | 8,280,000.00 USD | 8,280,000.00 USD | 1,810.00 USD | 1,110.00 USD | 157.61 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `317.30` | 4,350,000.00 USD | 4,350,000.00 USD | 2,250.00 USD | 4,170.00 USD | 1,590.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `317.50` | 8,300,000.00 USD | 8,300,000.00 USD | 14,400.00 USD | 574.27 USD | 76.75 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `317.70` | 4,390,000.00 USD | 4,390,000.00 USD | 6,150.00 USD | 15,360.00 USD | 18,370.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `317.90` | 8,330,000.00 USD | 8,330,000.00 USD | 21,020.00 USD | 8,200.00 USD | 187.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `318.10` | 4,400,000.00 USD | 4,400,000.00 USD | 2,290.00 USD | 9,220.00 USD | 820.17 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `318.30` | 8,380,000.00 USD | 8,380,000.00 USD | 3,320.00 USD | 26,930.00 USD | 22,340.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `318.50` | 4,410,000.00 USD | 4,410,000.00 USD | 4,700.00 USD | 7,460.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `318.50` | 114.34 USD | 4,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `318.70` | 8,450,000.00 USD | 8,450,000.00 USD | 10,810.00 USD | 18,570.00 USD | 37,820.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `318.90` | 4,450,000.00 USD | 4,450,000.00 USD | 12,470.00 USD | 8,760.00 USD | 13,930.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `319.10` | 8,460,000.00 USD | 8,460,000.00 USD | 366.90 USD | 18,060.00 USD | 36.86 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `319.30` | 4,470,000.00 USD | 4,470,000.00 USD | 8,560.00 USD | 13,080.00 USD | 488.47 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `319.50` | 8,460,000.00 USD | 8,460,000.00 USD | 733.55 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `319.50` | 6,600.00 USD | 11,440.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `319.70` | 4,470,000.00 USD | 4,470,000.00 USD | 0.00 USD | 2,390.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `319.90` | 8,480,000.00 USD | 8,480,000.00 USD | 446.22 USD | 9,520.00 USD | 5,370.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `320.10` | 4,490,000.00 USD | 4,490,000.00 USD | 4,350.00 USD | 91.90 USD | 10,920.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `320.30` | 8,560,000.00 USD | 8,560,000.00 USD | 49,430.00 USD | 10,080.00 USD | 25,260.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `320.50` | 4,500,000.00 USD | 4,500,000.00 USD | 8,130.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `320.50` | 1,110.00 USD | 12,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `320.70` | 8,570,000.00 USD | 8,570,000.00 USD | 189.87 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `321.10` | 8,580,000.00 USD | 8,580,000.00 USD | 9,210.00 USD | 8,300.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `321.30` | 4,500,000.00 USD | 4,500,000.00 USD | 150.60 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `321.50` | 8,620,000.00 USD | 8,620,000.00 USD | 4,440.00 USD | 9,730.00 USD | 21,040.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `321.70` | 4,520,000.00 USD | 4,520,000.00 USD | 8,670.00 USD | 0.00 USD | 16,170.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `321.90` | 8,620,000.00 USD | 8,620,000.00 USD | 910.57 USD | 500.60 USD | 2.45 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `322.10` | 4,540,000.00 USD | 4,540,000.00 USD | 0.00 USD | 0.00 USD | 16,140.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `322.30` | 8,660,000.00 USD | 8,660,000.00 USD | 22,930.00 USD | 7,790.00 USD | 6,150.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `322.70` | 8,670,000.00 USD | 8,670,000.00 USD | 9,620.00 USD | 6,000.00 USD | 53.16 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `323.10` | 8,710,000.00 USD | 8,710,000.00 USD | 21,120.00 USD | 5,860.00 USD | 11,480.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `323.50` | 8,720,000.00 USD | 8,720,000.00 USD | 269.10 USD | 6,780.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `324.30` | 8,750,000.00 USD | 8,750,000.00 USD | 0.00 USD | 4,960.00 USD | 23,350.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `324.50` | 8,760,000.00 USD | 8,760,000.00 USD | 11,060.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
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
| `7D` | `248.30` | 18,730,000.00 USD | 0.00 USD | 18,730,000.00 USD | 8,700.00 USD | 3,270.00 USD | 10,090.00 USD |
| `7D` | `248.70` | 18,710,000.00 USD | 0.00 USD | 18,710,000.00 USD | 43,550.00 USD | 17,040.00 USD | 28,350.00 USD |
| `7D` | `249.10` | 18,620,000.00 USD | 0.00 USD | 18,620,000.00 USD | 16,180.00 USD | 29,320.00 USD | 11,560.00 USD |
| `7D` | `249.50` | 18,560,000.00 USD | 0.00 USD | 18,560,000.00 USD | 42,290.00 USD | 32,910.00 USD | 8,340.00 USD |
| `7D` | `249.90` | 18,480,000.00 USD | 0.00 USD | 18,480,000.00 USD | 44,840.00 USD | 14,160.00 USD | 35,610.00 USD |
| `7D` | `250.30` | 18,390,000.00 USD | 0.00 USD | 18,390,000.00 USD | 18,520.00 USD | 38,250.00 USD | 3,480.00 USD |
| `7D` | `250.70` | 18,320,000.00 USD | 0.00 USD | 18,320,000.00 USD | 31,550.00 USD | 36,830.00 USD | 21,190.00 USD |
| `7D` | `251.10` | 18,240,000.00 USD | 0.00 USD | 18,240,000.00 USD | 29,390.00 USD | 49,280.00 USD | 12,010.00 USD |
| `7D` | `251.50` | 18,140,000.00 USD | 0.00 USD | 18,140,000.00 USD | 17,130.00 USD | 61,120.00 USD | 22,910.00 USD |
| `7D` | `251.90` | 18,040,000.00 USD | 0.00 USD | 18,040,000.00 USD | 74,710.00 USD | 48,150.00 USD | 43,110.00 USD |
| `7D` | `252.30` | 17,880,000.00 USD | 0.00 USD | 17,880,000.00 USD | 51,600.00 USD | 23,430.00 USD | 12,810.00 USD |
| `7D` | `252.70` | 17,790,000.00 USD | 0.00 USD | 17,790,000.00 USD | 43,080.00 USD | 19,890.00 USD | 15,320.00 USD |
| `7D` | `253.10` | 17,710,000.00 USD | 0.00 USD | 17,710,000.00 USD | 13,370.00 USD | 25,630.00 USD | 4,300.00 USD |
| `1D` | `253.30` | 8,210,000.00 USD | 0.00 USD | 8,210,000.00 USD | 12,160.00 USD | 22,710.00 USD | 10,550.00 USD |
| `7D` | `253.50` | 17,670,000.00 USD | 0.00 USD | 17,670,000.00 USD | 24,970.00 USD | 34,890.00 USD | 50,520.00 USD |
| `1D` | `253.70` | 8,160,000.00 USD | 0.00 USD | 8,160,000.00 USD | 7,980.00 USD | 7,140.00 USD | 978.51 USD |
| `7D` | `253.90` | 17,560,000.00 USD | 0.00 USD | 17,560,000.00 USD | 4,930.00 USD | 29,760.00 USD | 21,970.00 USD |
| `1D` | `254.10` | 8,150,000.00 USD | 0.00 USD | 8,150,000.00 USD | 144.00 USD | 2,440.00 USD | 3.86 USD |
| `7D` | `254.30` | 17,500,000.00 USD | 0.00 USD | 17,500,000.00 USD | 44,770.00 USD | 28,990.00 USD | 3,840.00 USD |
| `1D` | `254.50` | 8,140,000.00 USD | 0.00 USD | 8,140,000.00 USD | 134.35 USD | 2,050.00 USD | 4,090.00 USD |
| `7D` | `254.70` | 17,420,000.00 USD | 0.00 USD | 17,420,000.00 USD | 23,800.00 USD | 12,800.00 USD | 12,610.00 USD |
| `1D` | `254.90` | 8,140,000.00 USD | 0.00 USD | 8,140,000.00 USD | 25,070.00 USD | 6,590.00 USD | 18,300.00 USD |
| `7D` | `255.10` | 17,370,000.00 USD | 0.00 USD | 17,370,000.00 USD | 14,770.00 USD | 11,150.00 USD | 31,750.00 USD |
| `1D` | `255.30` | 8,090,000.00 USD | 0.00 USD | 8,090,000.00 USD | 3,050.00 USD | 39.75 USD | 29.85 USD |
| `7D` | `255.50` | 17,320,000.00 USD | 0.00 USD | 17,320,000.00 USD | 51,410.00 USD | 978.50 USD | 26,250.00 USD |
| `1D` | `255.70` | 8,080,000.00 USD | 0.00 USD | 8,080,000.00 USD | 14,240.00 USD | 7,440.00 USD | 8,700.00 USD |
| `7D` | `255.90` | 17,240,000.00 USD | 0.00 USD | 17,240,000.00 USD | 16,050.00 USD | 30,780.00 USD | 39,400.00 USD |
| `1D` | `256.10` | 8,050,000.00 USD | 0.00 USD | 8,050,000.00 USD | 16,500.00 USD | 1,970.00 USD | 1.44 USD |
| `7D` | `256.30` | 17,150,000.00 USD | 0.00 USD | 17,150,000.00 USD | 88,910.00 USD | 21,560.00 USD | 29,700.00 USD |
| `1D` | `256.50` | 8,030,000.00 USD | 0.00 USD | 8,030,000.00 USD | 7,160.00 USD | 4,770.00 USD | 2,580.00 USD |
| `7D` | `256.70` | 17,010,000.00 USD | 0.00 USD | 17,010,000.00 USD | 31,480.00 USD | 14,630.00 USD | 23,090.00 USD |
| `1D` | `256.90` | 8,020,000.00 USD | 0.00 USD | 8,020,000.00 USD | 4,760.00 USD | 10,970.00 USD | 10,050.00 USD |
| `7D` | `257.10` | 16,940,000.00 USD | 0.00 USD | 16,940,000.00 USD | 27,360.00 USD | 3,120.00 USD | 47,810.00 USD |
| `1D` | `257.30` | 7,990,000.00 USD | 0.00 USD | 7,990,000.00 USD | 4,320.00 USD | 10,960.00 USD | 11,750.00 USD |
| `7D` | `257.50` | 16,860,000.00 USD | 0.00 USD | 16,860,000.00 USD | 27,690.00 USD | 1,950.00 USD | 10,280.00 USD |
| `1D` | `257.70` | 7,970,000.00 USD | 0.00 USD | 7,970,000.00 USD | 479.45 USD | 0.00 USD | 4,830.00 USD |
| `7D` | `257.90` | 16,820,000.00 USD | 0.00 USD | 16,820,000.00 USD | 35,520.00 USD | 5,470.00 USD | 7,970.00 USD |
| `1D` | `258.10` | 7,960,000.00 USD | 0.00 USD | 7,960,000.00 USD | 3,740.00 USD | 4,120.00 USD | 25,290.00 USD |
| `7D` | `258.30` | 16,780,000.00 USD | 0.00 USD | 16,780,000.00 USD | 102,130.00 USD | 52,010.00 USD | 30,840.00 USD |
| `1D` | `258.50` | 7,930,000.00 USD | 0.00 USD | 7,930,000.00 USD | 1,470.00 USD | 5,260.00 USD | 45.78 USD |
| `7D` | `258.70` | 16,590,000.00 USD | 0.00 USD | 16,590,000.00 USD | 76,500.00 USD | 4,180.00 USD | 36,890.00 USD |
| `1D` | `258.90` | 7,920,000.00 USD | 0.00 USD | 7,920,000.00 USD | 17,930.00 USD | 11,000.00 USD | 11,810.00 USD |
| `7D` | `259.10` | 16,470,000.00 USD | 0.00 USD | 16,470,000.00 USD | 19,700.00 USD | 15,870.00 USD | 26,350.00 USD |
| `1D` | `259.30` | 7,880,000.00 USD | 0.00 USD | 7,880,000.00 USD | 7,430.00 USD | 4,150.00 USD | 12,490.00 USD |
| `7D` | `259.50` | 16,410,000.00 USD | 0.00 USD | 16,410,000.00 USD | 2,100.00 USD | 34,490.00 USD | 78.88 USD |
| `1D` | `259.70` | 7,860,000.00 USD | 0.00 USD | 7,860,000.00 USD | 9,280.00 USD | 16,830.00 USD | 10,080.00 USD |
| `7D` | `259.90` | 16,370,000.00 USD | 0.00 USD | 16,370,000.00 USD | 18,950.00 USD | 9,160.00 USD | 95.87 USD |
| `1D` | `260.10` | 7,820,000.00 USD | 0.00 USD | 7,820,000.00 USD | 1,420.00 USD | 9,580.00 USD | 9,890.00 USD |
| `7D` | `260.30` | 16,350,000.00 USD | 0.00 USD | 16,350,000.00 USD | 23,380.00 USD | 9,140.00 USD | 8,940.00 USD |
| `1D` | `260.50` | 7,800,000.00 USD | 0.00 USD | 7,800,000.00 USD | 2,850.00 USD | 8,720.00 USD | 825.30 USD |
| `7D` | `260.70` | 16,300,000.00 USD | 0.00 USD | 16,300,000.00 USD | 15,620.00 USD | 47,200.00 USD | 60,150.00 USD |
| `1D` | `260.90` | 7,790,000.00 USD | 0.00 USD | 7,790,000.00 USD | 17,240.00 USD | 11,030.00 USD | 13,930.00 USD |
| `7D` | `261.10` | 16,180,000.00 USD | 0.00 USD | 16,180,000.00 USD | 6,540.00 USD | 33,150.00 USD | 16,040.00 USD |
| `1D` | `261.30` | 7,750,000.00 USD | 0.00 USD | 7,750,000.00 USD | 8,630.00 USD | 13,150.00 USD | 500.69 USD |
| `7D` | `261.50` | 16,130,000.00 USD | 0.00 USD | 16,130,000.00 USD | 16,390.00 USD | 23,870.00 USD | 6,590.00 USD |
| `1D` | `261.70` | 7,720,000.00 USD | 0.00 USD | 7,720,000.00 USD | 4,750.00 USD | 3,280.00 USD | 0.78 USD |
| `7D` | `261.90` | 16,080,000.00 USD | 0.00 USD | 16,080,000.00 USD | 54,070.00 USD | 37,990.00 USD | 46,200.00 USD |
| `1D` | `262.10` | 7,720,000.00 USD | 0.00 USD | 7,720,000.00 USD | 517.32 USD | 676.61 USD | 10,920.00 USD |
| `7D` | `262.30` | 15,940,000.00 USD | 0.00 USD | 15,940,000.00 USD | 43,400.00 USD | 47,100.00 USD | 34.49 USD |
| `1D` | `262.50` | 7,700,000.00 USD | 0.00 USD | 7,700,000.00 USD | 8,380.00 USD | 850.29 USD | 5.26 USD |
| `7D` | `262.70` | 15,850,000.00 USD | 0.00 USD | 15,850,000.00 USD | 56,340.00 USD | 37,260.00 USD | 26,790.00 USD |
| `1D` | `262.90` | 7,690,000.00 USD | 0.00 USD | 7,690,000.00 USD | 150.60 USD | 976.53 USD | 6.97 USD |
| `7D` | `263.10` | 15,730,000.00 USD | 0.00 USD | 15,730,000.00 USD | 37,610.00 USD | 14,780.00 USD | 36,950.00 USD |
| `1D` | `263.30` | 7,690,000.00 USD | 0.00 USD | 7,690,000.00 USD | 8,890.00 USD | 116.15 USD | 16,180.00 USD |
| `7D` | `263.50` | 15,640,000.00 USD | 0.00 USD | 15,640,000.00 USD | 177,230.00 USD | 84,800.00 USD | 25,240.00 USD |
| `1D` | `263.70` | 7,670,000.00 USD | 0.00 USD | 7,670,000.00 USD | 414.95 USD | 1,470.00 USD | 16,150.00 USD |
| `7D` | `263.90` | 15,350,000.00 USD | 0.00 USD | 15,350,000.00 USD | 214,570.00 USD | 41,490.00 USD | 51,710.00 USD |
| `1D` | `264.10` | 7,650,000.00 USD | 0.00 USD | 7,650,000.00 USD | 2,210.00 USD | 184.09 USD | 7.56 USD |
| `7D` | `264.30` | 15,050,000.00 USD | 0.00 USD | 15,050,000.00 USD | 41,340.00 USD | 44,170.00 USD | 10,230.00 USD |
| `1D` | `264.50` | 7,650,000.00 USD | 0.00 USD | 7,650,000.00 USD | 800.20 USD | 733.03 USD | 36,610.00 USD |
| `7D` | `264.70` | 14,950,000.00 USD | 0.00 USD | 14,950,000.00 USD | 54,310.00 USD | 68,740.00 USD | 43,320.00 USD |
| `1D` | `264.90` | 7,610,000.00 USD | 0.00 USD | 7,610,000.00 USD | 28,630.00 USD | 1,040.00 USD | 15,670.00 USD |
| `7D` | `265.10` | 14,780,000.00 USD | 0.00 USD | 14,780,000.00 USD | 104,580.00 USD | 58,410.00 USD | 87,170.00 USD |
| `1D` | `265.30` | 7,560,000.00 USD | 0.00 USD | 7,560,000.00 USD | 21,010.00 USD | 8,710.00 USD | 33,520.00 USD |
| `7D` | `265.50` | 14,530,000.00 USD | 0.00 USD | 14,530,000.00 USD | 65,360.00 USD | 53,690.00 USD | 78,900.00 USD |
| `1D` | `265.70` | 7,500,000.00 USD | 0.00 USD | 7,500,000.00 USD | 24,070.00 USD | 23,390.00 USD | 33,670.00 USD |
| `7D` | `265.90` | 14,340,000.00 USD | 0.00 USD | 14,340,000.00 USD | 60,500.00 USD | 86,890.00 USD | 29,610.00 USD |
| `1D` | `266.10` | 7,420,000.00 USD | 0.00 USD | 7,420,000.00 USD | 10,460.00 USD | 335.05 USD | 7.04 USD |
| `7D` | `266.30` | 14,160,000.00 USD | 0.00 USD | 14,160,000.00 USD | 197,950.00 USD | 158,200.00 USD | 71,190.00 USD |
| `1D` | `266.50` | 7,410,000.00 USD | 0.00 USD | 7,410,000.00 USD | 27,700.00 USD | 3,150.00 USD | 8,720.00 USD |
| `7D` | `266.70` | 13,730,000.00 USD | 0.00 USD | 13,730,000.00 USD | 91,720.00 USD | 53,860.00 USD | 135,830.00 USD |
| `1D` | `266.90` | 7,370,000.00 USD | 0.00 USD | 7,370,000.00 USD | 33,550.00 USD | 6,620.00 USD | 6,770.00 USD |
| `7D` | `267.10` | 13,450,000.00 USD | 0.00 USD | 13,450,000.00 USD | 122,460.00 USD | 177,330.00 USD | 68,840.00 USD |
| `1D` | `267.30` | 7,320,000.00 USD | 0.00 USD | 7,320,000.00 USD | 18,230.00 USD | 11,070.00 USD | 3,350.00 USD |
| `7D` | `267.50` | 13,080,000.00 USD | 0.00 USD | 13,080,000.00 USD | 106,550.00 USD | 176,700.00 USD | 65,790.00 USD |
| `1D` | `267.70` | 7,290,000.00 USD | 0.00 USD | 7,290,000.00 USD | 83,350.00 USD | 112,140.00 USD | 14,410.00 USD |
| `7D` | `267.90` | 12,730,000.00 USD | 0.00 USD | 12,730,000.00 USD | 202,290.00 USD | 214,120.00 USD | 98,960.00 USD |
| `1D` | `268.10` | 7,080,000.00 USD | 0.00 USD | 7,080,000.00 USD | 55,490.00 USD | 80,400.00 USD | 47,150.00 USD |
| `7D` | `268.30` | 12,220,000.00 USD | 0.00 USD | 12,220,000.00 USD | 118,790.00 USD | 256,410.00 USD | 74,450.00 USD |
| `1D` | `268.50` | 6,900,000.00 USD | 0.00 USD | 6,900,000.00 USD | 57,190.00 USD | 101,540.00 USD | 31,670.00 USD |
| `7D` | `268.70` | 11,770,000.00 USD | 0.00 USD | 11,770,000.00 USD | 190,630.00 USD | 159,680.00 USD | 85,870.00 USD |
| `1D` | `268.90` | 6,710,000.00 USD | 0.00 USD | 6,710,000.00 USD | 92,000.00 USD | 36,140.00 USD | 41,690.00 USD |
| `7D` | `269.10` | 11,330,000.00 USD | 0.00 USD | 11,330,000.00 USD | 285,230.00 USD | 182,200.00 USD | 89,970.00 USD |
| `1D` | `269.30` | 6,540,000.00 USD | 0.00 USD | 6,540,000.00 USD | 28,630.00 USD | 16,230.00 USD | 20,850.00 USD |
| `7D` | `269.50` | 10,770,000.00 USD | 0.00 USD | 10,770,000.00 USD | 145,740.00 USD | 91,670.00 USD | 41,400.00 USD |
| `1D` | `269.70` | 6,470,000.00 USD | 0.00 USD | 6,470,000.00 USD | 39,010.00 USD | 24,270.00 USD | 8,680.00 USD |
| `7D` | `269.90` | 10,490,000.00 USD | 0.00 USD | 10,490,000.00 USD | 79,230.00 USD | 94,580.00 USD | 13,270.00 USD |
| `1D` | `270.10` | 6,400,000.00 USD | 0.00 USD | 6,400,000.00 USD | 98,640.00 USD | 77,480.00 USD | 98,230.00 USD |
| `7D` | `270.30` | 10,310,000.00 USD | 0.00 USD | 10,310,000.00 USD | 121,790.00 USD | 159,170.00 USD | 175,050.00 USD |
| `1D` | `270.50` | 6,120,000.00 USD | 0.00 USD | 6,120,000.00 USD | 72,430.00 USD | 36,250.00 USD | 36,810.00 USD |
| `7D` | `270.70` | 9,850,000.00 USD | 0.00 USD | 9,850,000.00 USD | 286,050.00 USD | 119,110.00 USD | 158,340.00 USD |
| `1D` | `270.90` | 5,980,000.00 USD | 0.00 USD | 5,980,000.00 USD | 12,030.00 USD | 24,230.00 USD | 66,890.00 USD |
| `7D` | `271.10` | 9,290,000.00 USD | 0.00 USD | 9,290,000.00 USD | 168,820.00 USD | 123,340.00 USD | 81,880.00 USD |
| `1D` | `271.30` | 5,880,000.00 USD | 0.00 USD | 5,880,000.00 USD | 56,610.00 USD | 46,210.00 USD | 83,200.00 USD |
| `7D` | `271.50` | 8,910,000.00 USD | 0.00 USD | 8,910,000.00 USD | 170,160.00 USD | 103,050.00 USD | 86,690.00 USD |
| `1D` | `271.70` | 5,690,000.00 USD | 0.00 USD | 5,690,000.00 USD | 40,290.00 USD | 27,540.00 USD | 35,800.00 USD |
| `7D` | `271.90` | 8,550,000.00 USD | 0.00 USD | 8,550,000.00 USD | 394,890.00 USD | 60,710.00 USD | 41,650.00 USD |
| `1D` | `272.10` | 5,590,000.00 USD | 0.00 USD | 5,590,000.00 USD | 135,480.00 USD | 39,350.00 USD | 32,720.00 USD |
| `7D` | `272.30` | 8,060,000.00 USD | 0.00 USD | 8,060,000.00 USD | 240,200.00 USD | 100,770.00 USD | 128,110.00 USD |
| `1D` | `272.50` | 5,380,000.00 USD | 0.00 USD | 5,380,000.00 USD | 101,210.00 USD | 31,310.00 USD | 46,830.00 USD |
| `7D` | `272.70` | 7,590,000.00 USD | 0.00 USD | 7,590,000.00 USD | 107,310.00 USD | 286,440.00 USD | 67,280.00 USD |
| `1D` | `272.90` | 5,200,000.00 USD | 0.00 USD | 5,200,000.00 USD | 80,060.00 USD | 58,140.00 USD | 6,760.00 USD |
| `7D` | `273.10` | 7,130,000.00 USD | 0.00 USD | 7,130,000.00 USD | 223,720.00 USD | 79,710.00 USD | 86,920.00 USD |
| `1D` | `273.30` | 5,050,000.00 USD | 0.00 USD | 5,050,000.00 USD | 179,830.00 USD | 208,970.00 USD | 35,220.00 USD |
| `7D` | `273.50` | 6,740,000.00 USD | 0.00 USD | 6,740,000.00 USD | 255,770.00 USD | 331,010.00 USD | 212,650.00 USD |
| `1D` | `273.70` | 4,630,000.00 USD | 0.00 USD | 4,630,000.00 USD | 148,250.00 USD | 182,920.00 USD | 131,450.00 USD |
| `7D` | `273.90` | 5,940,000.00 USD | 0.00 USD | 5,940,000.00 USD | 296,240.00 USD | 414,010.00 USD | 210,040.00 USD |
| `1D` | `274.10` | 4,170,000.00 USD | 0.00 USD | 4,170,000.00 USD | 120,870.00 USD | 238,300.00 USD | 77,880.00 USD |
| `7D` | `274.30` | 5,020,000.00 USD | 0.00 USD | 5,020,000.00 USD | 382,210.00 USD | 250,340.00 USD | 118,730.00 USD |
| `1D` | `274.50` | 3,730,000.00 USD | 0.00 USD | 3,730,000.00 USD | 201,380.00 USD | 84,390.00 USD | 122,290.00 USD |
| `7D` | `274.70` | 4,260,000.00 USD | 0.00 USD | 4,260,000.00 USD | 325,110.00 USD | 141,540.00 USD | 105,700.00 USD |
| `1D` | `274.90` | 3,320,000.00 USD | 0.00 USD | 3,320,000.00 USD | 72,100.00 USD | 37,590.00 USD | 79,280.00 USD |
| `7D` | `275.10` | 3,690,000.00 USD | 0.00 USD | 3,690,000.00 USD | 139,440.00 USD | 114,270.00 USD | 37,020.00 USD |
| `1D` | `275.30` | 3,130,000.00 USD | 0.00 USD | 3,130,000.00 USD | 75,490.00 USD | 47,550.00 USD | 45,800.00 USD |
| `7D` | `275.50` | 3,400,000.00 USD | 0.00 USD | 3,400,000.00 USD | 2,590.00 USD | 101,070.00 USD | 40,400.00 USD |
| `1D` | `275.70` | 2,960,000.00 USD | 0.00 USD | 2,960,000.00 USD | 12,170.00 USD | 37,310.00 USD | 8,730.00 USD |
| `7D` | `275.90` | 3,260,000.00 USD | 0.00 USD | 3,260,000.00 USD | 1,950.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `276.10` | 2,910,000.00 USD | 0.00 USD | 2,910,000.00 USD | 82,100.00 USD | 48,180.00 USD | 22,040.00 USD |
| `7D` | `276.30` | 3,260,000.00 USD | 0.00 USD | 3,260,000.00 USD | 2,290.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `276.50` | 2,750,000.00 USD | 0.00 USD | 2,750,000.00 USD | 13,650.00 USD | 31,830.00 USD | 3,230.00 USD |
| `7D` | `276.70` | 3,250,000.00 USD | 0.00 USD | 3,250,000.00 USD | 569.60 USD | 233.30 USD | 19,870.00 USD |
| `1D` | `276.90` | 2,710,000.00 USD | 0.00 USD | 2,710,000.00 USD | 10,750.00 USD | 20,770.00 USD | 11,360.00 USD |
| `7D` | `277.10` | 3,230,000.00 USD | 0.00 USD | 3,230,000.00 USD | 28,890.00 USD | 22,950.00 USD | 42.47 USD |
| `1D` | `277.30` | 2,660,000.00 USD | 0.00 USD | 2,660,000.00 USD | 301.20 USD | 75,230.00 USD | 21,180.00 USD |
| `7D` | `277.50` | 3,180,000.00 USD | 0.00 USD | 3,180,000.00 USD | 0.00 USD | 90,480.00 USD | 85.00 USD |
| `1D` | `277.70` | 2,570,000.00 USD | 0.00 USD | 2,570,000.00 USD | 57,640.00 USD | 47,660.00 USD | 5.52 USD |
| `7D` | `277.90` | 3,090,000.00 USD | 0.00 USD | 3,090,000.00 USD | 0.00 USD | 0.00 USD | 55,850.00 USD |
| `1D` | `278.10` | 2,460,000.00 USD | 0.00 USD | 2,460,000.00 USD | 12,650.00 USD | 9,490.00 USD | 28,100.00 USD |
| `7D` | `278.30` | 3,030,000.00 USD | 0.00 USD | 3,030,000.00 USD | 24,750.00 USD | 0.00 USD | 59,450.00 USD |
| `1D` | `278.50` | 2,410,000.00 USD | 0.00 USD | 2,410,000.00 USD | 67,950.00 USD | 25,470.00 USD | 29,220.00 USD |
| `7D` | `278.70` | 2,950,000.00 USD | 0.00 USD | 2,950,000.00 USD | 30,510.00 USD | 72,160.00 USD | 17,080.00 USD |
| `1D` | `278.90` | 2,290,000.00 USD | 0.00 USD | 2,290,000.00 USD | 20,180.00 USD | 27,270.00 USD | 10,340.00 USD |
| `7D` | `279.10` | 2,830,000.00 USD | 0.00 USD | 2,830,000.00 USD | 29,880.00 USD | 0.00 USD | 9.96 USD |
| `1D` | `279.30` | 2,230,000.00 USD | 0.00 USD | 2,230,000.00 USD | 53,390.00 USD | 23,330.00 USD | 44,020.00 USD |
| `7D` | `279.50` | 2,800,000.00 USD | 0.00 USD | 2,800,000.00 USD | 78,130.00 USD | 0.00 USD | 96,030.00 USD |
| `1D` | `279.70` | 2,110,000.00 USD | 0.00 USD | 2,110,000.00 USD | 20,320.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `280.10` | 2,090,000.00 USD | 0.00 USD | 2,090,000.00 USD | 21,040.00 USD | 0.00 USD | 36,620.00 USD |
| `7D` | `280.30` | 2,630,000.00 USD | 0.00 USD | 2,630,000.00 USD | 0.00 USD | 0.00 USD | 55.04 USD |
| `1D` | `280.50` | 2,030,000.00 USD | 0.00 USD | 2,030,000.00 USD | 30,390.00 USD | 0.00 USD | 64,990.00 USD |
| `1D` | `280.90` | 1,940,000.00 USD | 0.00 USD | 1,940,000.00 USD | 0.00 USD | 0.00 USD | 21,660.00 USD |
| `7D` | `281.10` | 2,630,000.00 USD | 0.00 USD | 2,630,000.00 USD | 0.00 USD | 0.00 USD | 62,810.00 USD |
| `1D` | `281.30` | 1,910,000.00 USD | 0.00 USD | 1,910,000.00 USD | 8,920.00 USD | 0.00 USD | 66,500.00 USD |
| `7D` | `281.50` | 2,560,000.00 USD | 0.00 USD | 2,560,000.00 USD | 565.82 USD | 0.00 USD | 122,390.00 USD |
| `1D` | `281.70` | 1,840,000.00 USD | 0.00 USD | 1,840,000.00 USD | 9,360.00 USD | 0.00 USD | 27,950.00 USD |
| `7D` | `281.90` | 2,440,000.00 USD | 0.00 USD | 2,440,000.00 USD | 0.00 USD | 0.00 USD | 117,140.00 USD |
| `1D` | `282.10` | 1,800,000.00 USD | 0.00 USD | 1,800,000.00 USD | 26,680.00 USD | 39,110.00 USD | 187,730.00 USD |
| `7D` | `282.30` | 2,320,000.00 USD | 0.00 USD | 2,320,000.00 USD | 0.00 USD | 0.00 USD | 56,220.00 USD |
| `1D` | `282.50` | 1,550,000.00 USD | 0.00 USD | 1,550,000.00 USD | 0.00 USD | 13,450.00 USD | 3,640.00 USD |
| `7D` | `282.70` | 2,270,000.00 USD | 0.00 USD | 2,270,000.00 USD | 0.00 USD | 0.00 USD | 7.78 USD |
| `1D` | `282.90` | 1,530,000.00 USD | 0.00 USD | 1,530,000.00 USD | 0.00 USD | 54,510.00 USD | 55,460.00 USD |
| `7D` | `283.10` | 2,270,000.00 USD | 0.00 USD | 2,270,000.00 USD | 0.00 USD | 37,310.00 USD | 89,480.00 USD |
| `1D` | `283.30` | 1,420,000.00 USD | 0.00 USD | 1,420,000.00 USD | 0.00 USD | 0.00 USD | 78,280.00 USD |
| `7D` | `283.50` | 2,140,000.00 USD | 0.00 USD | 2,140,000.00 USD | 0.00 USD | 0.00 USD | 111,520.00 USD |
| `1D` | `283.70` | 1,340,000.00 USD | 0.00 USD | 1,340,000.00 USD | 0.00 USD | 30,480.00 USD | 4,100.00 USD |
| `7D` | `283.90` | 2,030,000.00 USD | 0.00 USD | 2,030,000.00 USD | 49,500.00 USD | 0.00 USD | 197,520.00 USD |
| `1D` | `284.10` | 1,310,000.00 USD | 0.00 USD | 1,310,000.00 USD | 37,810.00 USD | 30,760.00 USD | 69,640.00 USD |
| `7D` | `284.30` | 1,780,000.00 USD | 0.00 USD | 1,780,000.00 USD | 0.00 USD | 89,730.00 USD | 8,610.00 USD |
| `1D` | `284.50` | 1,170,000.00 USD | 0.00 USD | 1,170,000.00 USD | 31,830.00 USD | 54,540.00 USD | 20,690.00 USD |
| `7D` | `284.70` | 1,680,000.00 USD | 0.00 USD | 1,680,000.00 USD | 26,130.00 USD | 191,100.00 USD | 34,230.00 USD |
| `1D` | `284.90` | 1,060,000.00 USD | 0.00 USD | 1,060,000.00 USD | 8,520.00 USD | 0.00 USD | 20,590.00 USD |
| `7D` | `285.10` | 1,430,000.00 USD | 0.00 USD | 1,430,000.00 USD | 62,660.00 USD | 190,390.00 USD | 83,240.00 USD |
| `1D` | `285.30` | 1,030,000.00 USD | 0.00 USD | 1,030,000.00 USD | 20,960.00 USD | 44,060.00 USD | 65,750.00 USD |
| `7D` | `285.50` | 1,100,000.00 USD | 0.00 USD | 1,100,000.00 USD | 0.00 USD | 185,240.00 USD | 0.00 USD |
| `1D` | `285.70` | 902,610.00 USD | 0.00 USD | 902,610.00 USD | 91,500.00 USD | 71,120.00 USD | 0.00 USD |
| `7D` | `285.90` | 910,790.00 USD | 0.00 USD | 910,790.00 USD | 0.00 USD | 52,670.00 USD | 0.00 USD |
| `1D` | `286.10` | 739,990.00 USD | 0.00 USD | 739,990.00 USD | 0.00 USD | 30,000.00 USD | 0.00 USD |
| `7D` | `286.30` | 858,120.00 USD | 0.00 USD | 858,120.00 USD | 0.00 USD | 40,670.00 USD | 0.00 USD |
| `1D` | `286.50` | 709,990.00 USD | 0.00 USD | 709,990.00 USD | 111,830.00 USD | 47,210.00 USD | 37,510.00 USD |
| `7D` | `286.70` | 817,450.00 USD | 0.00 USD | 817,450.00 USD | 23,860.00 USD | 146,630.00 USD | 1.44 USD |
| `1D` | `286.90` | 513,430.00 USD | 0.00 USD | 513,430.00 USD | 82,410.00 USD | 88,910.00 USD | 124,010.00 USD |
| `7D` | `287.10` | 646,960.00 USD | 0.00 USD | 646,960.00 USD | 81,140.00 USD | 138,810.00 USD | 0.00 USD |
| `1D` | `287.30` | 218,090.00 USD | 0.00 USD | 218,090.00 USD | 0.00 USD | 101,950.00 USD | 0.00 USD |
| `7D` | `287.50` | 427,000.00 USD | 0.00 USD | 427,000.00 USD | 23,560.00 USD | 53,560.00 USD | 70.92 USD |
| `1D` | `287.70` | 116,140.00 USD | 0.00 USD | 116,140.00 USD | 0.00 USD | 0.00 USD | 33,650.00 USD |
| `7D` | `287.90` | 349,800.00 USD | 0.00 USD | 349,800.00 USD | 0.00 USD | 277,850.00 USD | 0.00 USD |
| `1D` | `288.10` | 82,490.00 USD | 0.00 USD | 82,490.00 USD | 0.00 USD | 0.00 USD | 11,360.00 USD |
| `7D` | `288.30` | 71,950.00 USD | 0.00 USD | 71,950.00 USD | 70,080.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `288.50` | 71,130.00 USD | 0.00 USD | 71,130.00 USD | 32,470.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `288.90` | 38,650.00 USD | 0.00 USD | 38,650.00 USD | 4,630.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `289.30` | 34,020.00 USD | 0.00 USD | 34,020.00 USD | 0.00 USD | 11,990.00 USD | 0.00 USD |
| `7D` | `289.50` | 1,870.00 USD | 0.00 USD | 1,870.00 USD | 0.00 USD | 927.80 USD | 0.00 USD |
| `7D` | `289.90` | 947.00 USD | 0.00 USD | 947.00 USD | 0.00 USD | 947.00 USD | 0.00 USD |
| `1D` | `290.90` | 22,030.00 USD | 0.00 USD | 22,030.00 USD | 0.00 USD | 22,030.00 USD | 3.40 USD |
| `7D` | `291.10` | 57,860.00 USD | 57,860.00 USD | 0.00 USD | 0.00 USD | 57,860.00 USD | 0.00 USD |
| `7D` | `291.10` | 115,720.00 USD | 115,720.00 USD | 0.00 USD | 0.00 USD | 57,860.00 USD | 0.00 USD |
| `1D` | `291.20` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `291.30` | 106,900.00 USD | 106,900.00 USD | 0.00 USD | 0.00 USD | 106,120.00 USD | 783.02 USD |
| `7D` | `291.50` | 171,450.00 USD | 171,450.00 USD | 0.00 USD | 0.00 USD | 55,720.00 USD | 0.00 USD |
| `1D` | `291.70` | 202,540.00 USD | 202,540.00 USD | 0.00 USD | 0.00 USD | 41,880.00 USD | 53,760.00 USD |
| `7D` | `291.90` | 292,180.00 USD | 292,180.00 USD | 0.00 USD | 0.00 USD | 120,730.00 USD | 0.00 USD |
| `1D` | `292.10` | 240,910.00 USD | 240,910.00 USD | 0.00 USD | 0.00 USD | 38,360.00 USD | 9.06 USD |
| `7D` | `292.30` | 363,330.00 USD | 363,330.00 USD | 0.00 USD | 0.00 USD | 71,060.00 USD | 88.06 USD |
| `1D` | `292.50` | 288,280.00 USD | 288,280.00 USD | 0.00 USD | 21.70 USD | 47,340.00 USD | 10.29 USD |
| `7D` | `292.70` | 450,590.00 USD | 450,590.00 USD | 0.00 USD | 0.00 USD | 87,160.00 USD | 102.79 USD |
| `1D` | `292.90` | 370,540.00 USD | 370,540.00 USD | 0.00 USD | 1,020.00 USD | 81,240.00 USD | 3.04 USD |
| `7D` | `293.10` | 595,610.00 USD | 595,610.00 USD | 0.00 USD | 0.00 USD | 144,960.00 USD | 65.31 USD |
| `1D` | `293.30` | 431,610.00 USD | 431,610.00 USD | 0.00 USD | 476.80 USD | 60,590.00 USD | 1.58 USD |
| `7D` | `293.50` | 596,170.00 USD | 596,170.00 USD | 0.00 USD | 534.50 USD | 0.00 USD | 20.19 USD |
| `1D` | `293.70` | 614,640.00 USD | 614,640.00 USD | 0.00 USD | 44,580.00 USD | 77,060.00 USD | 61,390.00 USD |
| `7D` | `293.90` | 713,700.00 USD | 713,700.00 USD | 0.00 USD | 51,570.00 USD | 20,910.00 USD | 45,050.00 USD |
| `1D` | `294.10` | 715,510.00 USD | 715,510.00 USD | 0.00 USD | 30,790.00 USD | 36,360.00 USD | 33,720.00 USD |
| `7D` | `294.30` | 895,800.00 USD | 895,800.00 USD | 0.00 USD | 107,580.00 USD | 13,840.00 USD | 60,680.00 USD |
| `1D` | `294.50` | 1,040,000.00 USD | 1,040,000.00 USD | 0.00 USD | 121,000.00 USD | 112,510.00 USD | 91,210.00 USD |
| `7D` | `294.70` | 1,060,000.00 USD | 1,060,000.00 USD | 0.00 USD | 16,110.00 USD | 92,170.00 USD | 59,220.00 USD |
| `1D` | `294.90` | 1,240,000.00 USD | 1,240,000.00 USD | 0.00 USD | 41,000.00 USD | 85,800.00 USD | 70,850.00 USD |
| `7D` | `295.10` | 1,290,000.00 USD | 1,290,000.00 USD | 0.00 USD | 48,390.00 USD | 16,140.00 USD | 157,180.00 USD |
| `1D` | `295.30` | 1,460,000.00 USD | 1,460,000.00 USD | 0.00 USD | 108,980.00 USD | 75,850.00 USD | 37,400.00 USD |
| `7D` | `295.50` | 1,770,000.00 USD | 1,770,000.00 USD | 0.00 USD | 142,280.00 USD | 137,630.00 USD | 202,350.00 USD |
| `1D` | `295.70` | 1,720,000.00 USD | 1,720,000.00 USD | 0.00 USD | 112,240.00 USD | 59,530.00 USD | 87,930.00 USD |
| `7D` | `295.90` | 1,950,000.00 USD | 1,950,000.00 USD | 0.00 USD | 58,330.00 USD | 89,730.00 USD | 31,970.00 USD |
| `1D` | `296.10` | 1,940,000.00 USD | 1,940,000.00 USD | 0.00 USD | 82,690.00 USD | 103,910.00 USD | 29,580.00 USD |
| `7D` | `296.30` | 2,110,000.00 USD | 2,110,000.00 USD | 0.00 USD | 26,350.00 USD | 14,050.00 USD | 120,850.00 USD |
| `1D` | `296.50` | 2,090,000.00 USD | 2,090,000.00 USD | 0.00 USD | 49,180.00 USD | 45,550.00 USD | 57,880.00 USD |
| `7D` | `296.70` | 2,370,000.00 USD | 2,370,000.00 USD | 0.00 USD | 118,130.00 USD | 1,060.00 USD | 144,650.00 USD |
| `1D` | `296.90` | 2,220,000.00 USD | 2,220,000.00 USD | 0.00 USD | 29,430.00 USD | 35,780.00 USD | 69,180.00 USD |
| `7D` | `297.10` | 2,540,000.00 USD | 2,540,000.00 USD | 0.00 USD | 89,710.00 USD | 51,160.00 USD | 27,820.00 USD |
| `1D` | `297.30` | 2,340,000.00 USD | 2,340,000.00 USD | 0.00 USD | 63,980.00 USD | 13,480.00 USD | 38,920.00 USD |
| `7D` | `297.50` | 2,640,000.00 USD | 2,640,000.00 USD | 0.00 USD | 3,940.00 USD | 58,600.00 USD | 34,690.00 USD |
| `1D` | `297.70` | 2,360,000.00 USD | 2,360,000.00 USD | 0.00 USD | 807.94 USD | 723.06 USD | 16,800.00 USD |
| `7D` | `297.90` | 2,750,000.00 USD | 2,750,000.00 USD | 0.00 USD | 16,990.00 USD | 39,840.00 USD | 54,850.00 USD |
| `1D` | `298.10` | 2,500,000.00 USD | 2,500,000.00 USD | 0.00 USD | 58,610.00 USD | 8,120.00 USD | 73,820.00 USD |
| `7D` | `298.30` | 2,870,000.00 USD | 2,870,000.00 USD | 0.00 USD | 32,250.00 USD | 41,860.00 USD | 48,080.00 USD |
| `1D` | `298.50` | 2,610,000.00 USD | 2,610,000.00 USD | 0.00 USD | 8,410.00 USD | 21,250.00 USD | 84,830.00 USD |
| `7D` | `298.70` | 2,950,000.00 USD | 2,950,000.00 USD | 0.00 USD | 69,820.00 USD | 11,780.00 USD | 17.54 USD |
| `1D` | `298.90` | 2,780,000.00 USD | 2,780,000.00 USD | 0.00 USD | 35,380.00 USD | 15,820.00 USD | 118,690.00 USD |
| `7D` | `299.10` | 3,040,000.00 USD | 3,040,000.00 USD | 0.00 USD | 1,100.00 USD | 993.25 USD | 85,830.00 USD |
| `1D` | `299.30` | 2,880,000.00 USD | 2,880,000.00 USD | 0.00 USD | 45,920.00 USD | 23,800.00 USD | 27,850.00 USD |
| `7D` | `299.50` | 3,050,000.00 USD | 3,050,000.00 USD | 0.00 USD | 3,330.00 USD | 2,700.00 USD | 0.00 USD |
| `1D` | `299.70` | 2,910,000.00 USD | 2,910,000.00 USD | 0.00 USD | 4,910.00 USD | 17,410.00 USD | 9,090.00 USD |
| `7D` | `299.90` | 3,120,000.00 USD | 3,120,000.00 USD | 0.00 USD | 39,130.00 USD | 8,330.00 USD | 19,840.00 USD |
| `1D` | `300.10` | 3,010,000.00 USD | 3,010,000.00 USD | 0.00 USD | 33,660.00 USD | 44,530.00 USD | 22,730.00 USD |
| `7D` | `300.30` | 3,120,000.00 USD | 3,120,000.00 USD | 0.00 USD | 866.20 USD | 1,190.00 USD | 6.52 USD |
| `1D` | `300.50` | 3,050,000.00 USD | 3,050,000.00 USD | 0.00 USD | 2,940.00 USD | 10,850.00 USD | 24,730.00 USD |
| `7D` | `300.70` | 3,230,000.00 USD | 3,230,000.00 USD | 0.00 USD | 24,140.00 USD | 70,210.00 USD | 19,740.00 USD |
| `1D` | `300.90` | 3,110,000.00 USD | 3,110,000.00 USD | 0.00 USD | 13,240.00 USD | 32,390.00 USD | 12,770.00 USD |
| `7D` | `301.10` | 3,380,000.00 USD | 3,380,000.00 USD | 0.00 USD | 23,380.00 USD | 32,100.00 USD | 91,130.00 USD |
| `1D` | `301.30` | 3,220,000.00 USD | 3,220,000.00 USD | 0.00 USD | 34,050.00 USD | 46,860.00 USD | 28,550.00 USD |
| `7D` | `301.50` | 3,610,000.00 USD | 3,610,000.00 USD | 0.00 USD | 85,980.00 USD | 85,500.00 USD | 59,580.00 USD |
| `1D` | `301.70` | 3,280,000.00 USD | 3,280,000.00 USD | 0.00 USD | 31,990.00 USD | 12,330.00 USD | 16,730.00 USD |
| `7D` | `301.90` | 3,810,000.00 USD | 3,810,000.00 USD | 0.00 USD | 51,660.00 USD | 123,250.00 USD | 26,240.00 USD |
| `1D` | `302.10` | 3,370,000.00 USD | 3,370,000.00 USD | 0.00 USD | 40,760.00 USD | 37,100.00 USD | 10,340.00 USD |
| `7D` | `302.30` | 3,910,000.00 USD | 3,910,000.00 USD | 0.00 USD | 1,560.00 USD | 93,720.00 USD | 19.74 USD |
| `1D` | `302.50` | 3,420,000.00 USD | 3,420,000.00 USD | 0.00 USD | 10,520.00 USD | 10,130.00 USD | 31,130.00 USD |
| `7D` | `302.70` | 4,090,000.00 USD | 4,090,000.00 USD | 0.00 USD | 71,700.00 USD | 72,440.00 USD | 41,620.00 USD |
| `1D` | `302.90` | 3,430,000.00 USD | 3,430,000.00 USD | 0.00 USD | 1,230.00 USD | 1,720.00 USD | 6,560.00 USD |
| `7D` | `303.10` | 4,130,000.00 USD | 4,130,000.00 USD | 0.00 USD | 0.00 USD | 39,740.00 USD | 211.16 USD |
| `1D` | `303.30` | 3,480,000.00 USD | 3,480,000.00 USD | 0.00 USD | 32,730.00 USD | 315.99 USD | 14,710.00 USD |
| `7D` | `303.50` | 4,130,000.00 USD | 4,130,000.00 USD | 0.00 USD | 0.00 USD | 173.09 USD | 159.88 USD |
| `1D` | `303.70` | 3,500,000.00 USD | 3,500,000.00 USD | 0.00 USD | 8,390.00 USD | 3,470.00 USD | 6,250.00 USD |
| `7D` | `303.90` | 4,190,000.00 USD | 4,190,000.00 USD | 0.00 USD | 21,140.00 USD | 10,490.00 USD | 24,480.00 USD |
| `1D` | `304.10` | 3,570,000.00 USD | 3,570,000.00 USD | 0.00 USD | 22,810.00 USD | 980.72 USD | 53,800.00 USD |
| `7D` | `304.30` | 4,190,000.00 USD | 4,190,000.00 USD | 0.00 USD | 2,070.00 USD | 174.44 USD | 151.22 USD |
| `1D` | `304.50` | 3,650,000.00 USD | 3,650,000.00 USD | 0.00 USD | 13,310.00 USD | 9,720.00 USD | 53,870.00 USD |
| `7D` | `304.70` | 4,210,000.00 USD | 4,210,000.00 USD | 0.00 USD | 3,610.00 USD | 11,790.00 USD | 2,060.00 USD |
| `1D` | `304.90` | 3,650,000.00 USD | 3,650,000.00 USD | 0.00 USD | 1,110.00 USD | 240.63 USD | 2.91 USD |
| `7D` | `305.10` | 4,550,000.00 USD | 4,550,000.00 USD | 0.00 USD | 127,730.00 USD | 131,900.00 USD | 84,440.00 USD |
| `1D` | `305.30` | 3,670,000.00 USD | 3,670,000.00 USD | 0.00 USD | 11,930.00 USD | 90.03 USD | 2,010.00 USD |
| `7D` | `305.50` | 4,720,000.00 USD | 4,720,000.00 USD | 0.00 USD | 94,240.00 USD | 19,010.00 USD | 52,950.00 USD |
| `1D` | `305.70` | 3,680,000.00 USD | 3,680,000.00 USD | 0.00 USD | 8,200.00 USD | 1,770.00 USD | 3,410.00 USD |
| `7D` | `305.90` | 4,830,000.00 USD | 4,830,000.00 USD | 0.00 USD | 58,070.00 USD | 53,970.00 USD | 3,580.00 USD |
| `1D` | `306.10` | 3,690,000.00 USD | 3,690,000.00 USD | 0.00 USD | 4,210.00 USD | 2,750.00 USD | 1,350.00 USD |
| `7D` | `306.30` | 4,970,000.00 USD | 4,970,000.00 USD | 0.00 USD | 29,420.00 USD | 47,840.00 USD | 63,810.00 USD |
| `1D` | `306.50` | 3,700,000.00 USD | 3,700,000.00 USD | 0.00 USD | 4,740.00 USD | 9,750.00 USD | 58.13 USD |
| `7D` | `306.70` | 5,090,000.00 USD | 5,090,000.00 USD | 0.00 USD | 27,190.00 USD | 29,850.00 USD | 54,510.00 USD |
| `1D` | `306.90` | 3,790,000.00 USD | 3,790,000.00 USD | 0.00 USD | 32,060.00 USD | 40,210.00 USD | 13,060.00 USD |
| `7D` | `307.10` | 5,340,000.00 USD | 5,340,000.00 USD | 0.00 USD | 60,720.00 USD | 90,210.00 USD | 98,860.00 USD |
| `1D` | `307.30` | 3,840,000.00 USD | 3,840,000.00 USD | 0.00 USD | 7,930.00 USD | 34,450.00 USD | 10,930.00 USD |
| `7D` | `307.50` | 5,550,000.00 USD | 5,550,000.00 USD | 0.00 USD | 57,330.00 USD | 114,040.00 USD | 41,560.00 USD |
| `1D` | `307.70` | 3,900,000.00 USD | 3,900,000.00 USD | 0.00 USD | 19,670.00 USD | 27,890.00 USD | 9,610.00 USD |
| `7D` | `307.90` | 5,830,000.00 USD | 5,830,000.00 USD | 0.00 USD | 125,550.00 USD | 94,530.00 USD | 65,370.00 USD |
| `1D` | `308.10` | 3,950,000.00 USD | 3,950,000.00 USD | 0.00 USD | 25,570.00 USD | 11,430.00 USD | 16,390.00 USD |
| `7D` | `308.30` | 6,110,000.00 USD | 6,110,000.00 USD | 0.00 USD | 129,220.00 USD | 40,480.00 USD | 109,680.00 USD |
| `1D` | `308.50` | 3,960,000.00 USD | 3,960,000.00 USD | 0.00 USD | 5,570.00 USD | 3,440.00 USD | 4,260.00 USD |
| `7D` | `308.70` | 6,230,000.00 USD | 6,230,000.00 USD | 0.00 USD | 67,430.00 USD | 31,490.00 USD | 15,430.00 USD |
| `1D` | `308.90` | 3,990,000.00 USD | 3,990,000.00 USD | 0.00 USD | 12,710.00 USD | 5,940.00 USD | 4,140.00 USD |
| `7D` | `309.10` | 6,350,000.00 USD | 6,350,000.00 USD | 0.00 USD | 38,660.00 USD | 39,620.00 USD | 39,820.00 USD |
| `1D` | `309.30` | 4,010,000.00 USD | 4,010,000.00 USD | 0.00 USD | 10,230.00 USD | 12,250.00 USD | 2,370.00 USD |
| `7D` | `309.50` | 6,550,000.00 USD | 6,550,000.00 USD | 0.00 USD | 47,540.00 USD | 51,380.00 USD | 101,820.00 USD |
| `1D` | `309.70` | 4,050,000.00 USD | 4,050,000.00 USD | 0.00 USD | 10,860.00 USD | 13,870.00 USD | 9,210.00 USD |
| `7D` | `309.90` | 6,750,000.00 USD | 6,750,000.00 USD | 0.00 USD | 19,540.00 USD | 106,330.00 USD | 75,930.00 USD |
| `1D` | `310.10` | 4,050,000.00 USD | 4,050,000.00 USD | 0.00 USD | 4,310.00 USD | 4,770.00 USD | 0.00 USD |
| `7D` | `310.30` | 6,980,000.00 USD | 6,980,000.00 USD | 0.00 USD | 47,320.00 USD | 107,890.00 USD | 76,820.00 USD |
| `1D` | `310.50` | 4,060,000.00 USD | 4,060,000.00 USD | 0.00 USD | 376.38 USD | 2,810.00 USD | 3.86 USD |
| `7D` | `310.70` | 7,100,000.00 USD | 7,100,000.00 USD | 0.00 USD | 65,370.00 USD | 50,820.00 USD | 3,850.00 USD |
| `1D` | `310.90` | 4,060,000.00 USD | 4,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 4,090.00 USD |
| `7D` | `311.10` | 7,270,000.00 USD | 7,270,000.00 USD | 0.00 USD | 59,270.00 USD | 59,630.00 USD | 47,610.00 USD |
| `1D` | `311.30` | 4,080,000.00 USD | 4,080,000.00 USD | 0.00 USD | 7,760.00 USD | 2,050.00 USD | 12,190.00 USD |
| `7D` | `311.50` | 7,320,000.00 USD | 7,320,000.00 USD | 0.00 USD | 37,540.00 USD | 6,860.00 USD | 5,630.00 USD |
| `1D` | `311.70` | 4,120,000.00 USD | 4,120,000.00 USD | 0.00 USD | 20,470.00 USD | 6,590.00 USD | 6,120.00 USD |
| `7D` | `311.90` | 7,400,000.00 USD | 7,400,000.00 USD | 0.00 USD | 48,410.00 USD | 10,970.00 USD | 26,190.00 USD |
| `1D` | `312.10` | 4,120,000.00 USD | 4,120,000.00 USD | 0.00 USD | 244.00 USD | 39.75 USD | 29.51 USD |
| `7D` | `312.30` | 7,480,000.00 USD | 7,480,000.00 USD | 0.00 USD | 30,350.00 USD | 11,070.00 USD | 34,640.00 USD |
| `1D` | `312.50` | 4,150,000.00 USD | 4,150,000.00 USD | 0.00 USD | 14,240.00 USD | 7,440.00 USD | 8,700.00 USD |
| `7D` | `312.70` | 7,570,000.00 USD | 7,570,000.00 USD | 0.00 USD | 16,880.00 USD | 30,630.00 USD | 39,510.00 USD |
| `1D` | `312.90` | 4,160,000.00 USD | 4,160,000.00 USD | 0.00 USD | 11,420.00 USD | 23.27 USD | 1.44 USD |
| `7D` | `313.10` | 7,670,000.00 USD | 7,670,000.00 USD | 0.00 USD | 52,780.00 USD | 16,920.00 USD | 37,070.00 USD |
| `1D` | `313.30` | 4,180,000.00 USD | 4,180,000.00 USD | 0.00 USD | 8,660.00 USD | 6,710.00 USD | 2,580.00 USD |
| `7D` | `313.50` | 7,750,000.00 USD | 7,750,000.00 USD | 0.00 USD | 34,410.00 USD | 14,970.00 USD | 27,700.00 USD |
| `1D` | `313.70` | 4,200,000.00 USD | 4,200,000.00 USD | 0.00 USD | 8,340.00 USD | 4,380.00 USD | 10,050.00 USD |
| `7D` | `313.90` | 7,840,000.00 USD | 7,840,000.00 USD | 0.00 USD | 44,540.00 USD | 15,260.00 USD | 31,430.00 USD |
| `1D` | `314.10` | 4,210,000.00 USD | 4,210,000.00 USD | 0.00 USD | 0.00 USD | 11,670.00 USD | 3,420.00 USD |
| `7D` | `314.30` | 7,940,000.00 USD | 7,940,000.00 USD | 0.00 USD | 51,980.00 USD | 307.60 USD | 51,780.00 USD |
| `1D` | `314.50` | 4,230,000.00 USD | 4,230,000.00 USD | 0.00 USD | 4,320.00 USD | 5,250.00 USD | 8,330.00 USD |
| `7D` | `314.70` | 7,960,000.00 USD | 7,960,000.00 USD | 0.00 USD | 9,830.00 USD | 0.00 USD | 10,330.00 USD |
| `1D` | `314.90` | 4,240,000.00 USD | 4,240,000.00 USD | 0.00 USD | 479.45 USD | 0.00 USD | 4,830.00 USD |
| `7D` | `315.10` | 8,000,000.00 USD | 8,000,000.00 USD | 0.00 USD | 29,590.00 USD | 547.95 USD | 41.26 USD |
| `1D` | `315.30` | 4,250,000.00 USD | 4,250,000.00 USD | 0.00 USD | 3,740.00 USD | 144.50 USD | 12,070.00 USD |
| `7D` | `315.50` | 8,050,000.00 USD | 8,050,000.00 USD | 0.00 USD | 13,690.00 USD | 9,550.00 USD | 30,770.00 USD |
| `1D` | `315.70` | 4,280,000.00 USD | 4,280,000.00 USD | 0.00 USD | 1,370.00 USD | 8,380.00 USD | 13,230.00 USD |
| `7D` | `315.90` | 8,150,000.00 USD | 8,150,000.00 USD | 0.00 USD | 39,580.00 USD | 41,220.00 USD | 17,390.00 USD |
| `1D` | `316.10` | 4,300,000.00 USD | 4,300,000.00 USD | 0.00 USD | 5,020.00 USD | 5,050.00 USD | 11,840.00 USD |
| `7D` | `316.30` | 8,210,000.00 USD | 8,210,000.00 USD | 0.00 USD | 451.45 USD | 19,940.00 USD | 43,400.00 USD |
| `1D` | `316.50` | 4,320,000.00 USD | 4,320,000.00 USD | 0.00 USD | 12,950.00 USD | 5,380.00 USD | 0.00 USD |
| `7D` | `316.70` | 8,280,000.00 USD | 8,280,000.00 USD | 0.00 USD | 18,110.00 USD | 30,550.00 USD | 18,370.00 USD |
| `1D` | `316.90` | 4,340,000.00 USD | 4,340,000.00 USD | 0.00 USD | 7,030.00 USD | 3,660.00 USD | 12,480.00 USD |
| `7D` | `317.10` | 8,280,000.00 USD | 8,280,000.00 USD | 0.00 USD | 1,810.00 USD | 1,110.00 USD | 157.61 USD |
| `1D` | `317.30` | 4,350,000.00 USD | 4,350,000.00 USD | 0.00 USD | 2,250.00 USD | 4,170.00 USD | 1,590.00 USD |
| `7D` | `317.50` | 8,300,000.00 USD | 8,300,000.00 USD | 0.00 USD | 14,400.00 USD | 574.27 USD | 76.75 USD |
| `1D` | `317.70` | 4,390,000.00 USD | 4,390,000.00 USD | 0.00 USD | 6,150.00 USD | 15,360.00 USD | 18,370.00 USD |
| `7D` | `317.90` | 8,330,000.00 USD | 8,330,000.00 USD | 0.00 USD | 21,020.00 USD | 8,200.00 USD | 187.00 USD |
| `1D` | `318.10` | 4,400,000.00 USD | 4,400,000.00 USD | 0.00 USD | 2,290.00 USD | 9,220.00 USD | 820.17 USD |
| `7D` | `318.30` | 8,380,000.00 USD | 8,380,000.00 USD | 0.00 USD | 3,320.00 USD | 26,930.00 USD | 22,340.00 USD |
| `1D` | `318.50` | 4,410,000.00 USD | 4,410,000.00 USD | 0.00 USD | 4,700.00 USD | 7,460.00 USD | 0.00 USD |
| `7D` | `318.70` | 8,450,000.00 USD | 8,450,000.00 USD | 0.00 USD | 10,810.00 USD | 18,570.00 USD | 37,820.00 USD |
| `1D` | `318.90` | 4,450,000.00 USD | 4,450,000.00 USD | 0.00 USD | 12,470.00 USD | 8,760.00 USD | 13,930.00 USD |
| `7D` | `319.10` | 8,460,000.00 USD | 8,460,000.00 USD | 0.00 USD | 366.90 USD | 18,060.00 USD | 36.86 USD |
| `1D` | `319.30` | 4,470,000.00 USD | 4,470,000.00 USD | 0.00 USD | 8,560.00 USD | 13,080.00 USD | 488.47 USD |
| `7D` | `319.50` | 8,460,000.00 USD | 8,460,000.00 USD | 0.00 USD | 733.55 USD | 0.00 USD | 0.00 USD |
| `1D` | `319.70` | 4,470,000.00 USD | 4,470,000.00 USD | 0.00 USD | 0.00 USD | 2,390.00 USD | 0.00 USD |
| `7D` | `319.90` | 8,480,000.00 USD | 8,480,000.00 USD | 0.00 USD | 446.22 USD | 9,520.00 USD | 5,370.00 USD |
| `1D` | `320.10` | 4,490,000.00 USD | 4,490,000.00 USD | 0.00 USD | 4,350.00 USD | 91.90 USD | 10,920.00 USD |
| `7D` | `320.30` | 8,560,000.00 USD | 8,560,000.00 USD | 0.00 USD | 49,430.00 USD | 10,080.00 USD | 25,260.00 USD |
| `1D` | `320.50` | 4,500,000.00 USD | 4,500,000.00 USD | 0.00 USD | 8,130.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `320.70` | 8,570,000.00 USD | 8,570,000.00 USD | 0.00 USD | 189.87 USD | 0.00 USD | 0.00 USD |
| `7D` | `321.10` | 8,580,000.00 USD | 8,580,000.00 USD | 0.00 USD | 9,210.00 USD | 8,300.00 USD | 0.00 USD |
| `1D` | `321.30` | 4,500,000.00 USD | 4,500,000.00 USD | 0.00 USD | 150.60 USD | 0.00 USD | 0.00 USD |
| `7D` | `321.50` | 8,620,000.00 USD | 8,620,000.00 USD | 0.00 USD | 4,440.00 USD | 9,730.00 USD | 21,040.00 USD |
| `1D` | `321.70` | 4,520,000.00 USD | 4,520,000.00 USD | 0.00 USD | 8,670.00 USD | 0.00 USD | 16,170.00 USD |
| `7D` | `321.90` | 8,620,000.00 USD | 8,620,000.00 USD | 0.00 USD | 910.57 USD | 500.60 USD | 2.45 USD |
| `1D` | `322.10` | 4,540,000.00 USD | 4,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 16,140.00 USD |
| `7D` | `322.30` | 8,660,000.00 USD | 8,660,000.00 USD | 0.00 USD | 22,930.00 USD | 7,790.00 USD | 6,150.00 USD |
| `7D` | `322.70` | 8,670,000.00 USD | 8,670,000.00 USD | 0.00 USD | 9,620.00 USD | 6,000.00 USD | 53.16 USD |
| `7D` | `323.10` | 8,710,000.00 USD | 8,710,000.00 USD | 0.00 USD | 21,120.00 USD | 5,860.00 USD | 11,480.00 USD |
| `7D` | `323.50` | 8,720,000.00 USD | 8,720,000.00 USD | 0.00 USD | 269.10 USD | 6,780.00 USD | 0.00 USD |
| `7D` | `324.30` | 8,750,000.00 USD | 8,750,000.00 USD | 0.00 USD | 0.00 USD | 4,960.00 USD | 23,350.00 USD |
| `7D` | `324.50` | 8,760,000.00 USD | 8,760,000.00 USD | 0.00 USD | 11,060.00 USD | 0.00 USD | 0.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `LONGS_FLUSHED` | 16,500.00 USD | 0.00 USD | 16,500.00 USD | -16,500.00 USD | `2` | `2026-10-29 17:35:00 UTC - 2026-10-29 17:40:00 UTC` |
| `15m` | `LONGS_FLUSHED` | 16,500.00 USD | 0.00 USD | 16,500.00 USD | -16,500.00 USD | `2` | `2026-10-29 17:30:00 UTC - 2026-10-29 17:45:00 UTC` |
| `1h` | `LONGS_FLUSHED` | 16,500.00 USD | 0.00 USD | 16,500.00 USD | -16,500.00 USD | `2` | `2026-10-29 17:00:00 UTC - 2026-10-29 18:00:00 UTC` |
| `4h` | `LONGS_FLUSHED` | 16,500.00 USD | 0.00 USD | 16,500.00 USD | -16,500.00 USD | `2` | `2026-10-29 16:00:00 UTC - 2026-10-29 20:00:00 UTC` |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `319.19M` | Total OI Tokens: `1,100,314.0 BCH`
  * 1h OI Change: `+0.12%` | 4h OI Change: `+4.29%` | 24h OI Change: `-1.45%`
  * Exchange Breakdown: Binance=`94.83M` | Bybit=`41.21M` | OKX=`25.00M` | Hyperliquid=`8.21M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `3.59K` | Last 24h: `4.21K` | Last 3d: `81.66K` | Last 7d: `135.21K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `-0.0002%` | **USDT OKX** | `-0.0004%` |
| **USDT Bybit** | `0.0100%` | **USDT KuCoin** | `0.0071%` |
| **USDT MEXC** | `-0.0002%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `0.0041%` | **USDT Bitget** | `0.0065%` |
| **CoinM Binance** | `0.0044%` | **CoinM OKX** | `0.0100%` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `BCH` | `50.81%` | `49.19%` | `1.03` | 2,690,000.00 USD |
| `15M` | `Binance` | `57.29%` | `42.71%` | `1.34` | 1,010,000.00 USD |
| `15M` | `OKX` | `54.1%` | `45.9%` | `1.18` | 150,290.00 USD |
| `15M` | `Bybit` | `56.87%` | `43.13%` | `1.32` | 242,540.00 USD |
| `15M` | `KuCoin` | `48.05%` | `51.95%` | `0.92` | 123,520.00 USD |
| `15M` | `Gate` | `66.72%` | `33.28%` | `2.00` | 99,150.00 USD |
| `15M` | `Bitget` | `40.26%` | `59.74%` | `0.67` | 102,770.00 USD |
| `15M` | `BingX` | `45.96%` | `54.04%` | `0.85` | 107,770.00 USD |
| `15M` | `MEXC` | `33.3%` | `66.7%` | `0.50` | 145,400.00 USD |
| `15M` | `Bitunix` | `55.09%` | `44.91%` | `1.23` | 46,140.00 USD |
| `15M` | `Hyperliquid` | `9.41%` | `90.59%` | `0.10` | 67,980.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `49.87%` | `50.13%` | `0.99` | 513,630.00 USD |
| `15M` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `WhiteBIT` | `12.15%` | `87.85%` | `0.14` | 70,420.00 USD |
| `15M` | `HTX` | `63.49%` | `36.51%` | `1.74` | 474.65 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `70.65%` | `29.35%` | `2.41` | 13,400.00 USD |
| `15M` | `Aster` | `62.06%` | `37.94%` | `1.64` | 171.43 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Whale Positions` | `57.29%` | `42.71%` | `1.34` | 1,010,000.00 USD |
| `15M` | `Global Accounts` | `50.81%` | `49.19%` | `1.03` | 2,690,000.00 USD |
| `1H` | `BCH` | `43.89%` | `56.11%` | `0.78` | 7,490,000.00 USD |
| `1H` | `Binance` | `45.36%` | `54.64%` | `0.83` | 2,560,000.00 USD |
| `1H` | `OKX` | `33.31%` | `66.69%` | `0.50` | 755,660.00 USD |
| `1H` | `Bybit` | `51.58%` | `48.42%` | `1.07` | 603,540.00 USD |
| `1H` | `KuCoin` | `49.24%` | `50.76%` | `0.97` | 526,550.00 USD |
| `1H` | `Gate` | `53.96%` | `46.04%` | `1.17` | 209,680.00 USD |
| `1H` | `Bitget` | `45.76%` | `54.24%` | `0.84` | 236,010.00 USD |
| `1H` | `BingX` | `42.76%` | `57.24%` | `0.75` | 463,500.00 USD |
| `1H` | `MEXC` | `39.88%` | `60.12%` | `0.66` | 478,180.00 USD |
| `1H` | `Bitunix` | `40.46%` | `59.54%` | `0.68` | 182,390.00 USD |
| `1H` | `Hyperliquid` | `19.12%` | `80.88%` | `0.24` | 142,930.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `50.2%` | `49.8%` | `1.01` | 1,080,000.00 USD |
| `1H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `WhiteBIT` | `5.53%` | `94.47%` | `0.06` | 186,810.00 USD |
| `1H` | `HTX` | `76.41%` | `23.59%` | `3.24` | 20,430.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `56.48%` | `43.52%` | `1.30` | 38,290.00 USD |
| `1H` | `Aster` | `39.99%` | `60.01%` | `0.67` | 407.75 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Whale Positions` | `45.36%` | `54.64%` | `0.83` | 2,560,000.00 USD |
| `1H` | `Global Accounts` | `43.89%` | `56.11%` | `0.78` | 7,490,000.00 USD |
| `4H` | `BCH` | `46.90%` | `53.10%` | `0.88` | 36,350,000.00 USD |
| `4H` | `Binance` | `46.58%` | `53.42%` | `0.87` | 13,120,000.00 USD |
| `4H` | `OKX` | `47.3%` | `52.7%` | `0.90` | 3,910,000.00 USD |
| `4H` | `Bybit` | `48.96%` | `51.04%` | `0.96` | 2,250,000.00 USD |
| `4H` | `KuCoin` | `49.87%` | `50.13%` | `0.99` | 2,130,000.00 USD |
| `4H` | `Gate` | `56.18%` | `43.82%` | `1.28` | 1,480,000.00 USD |
| `4H` | `Bitget` | `49.45%` | `50.55%` | `0.98` | 1,220,000.00 USD |
| `4H` | `BingX` | `37.2%` | `62.8%` | `0.59` | 2,640,000.00 USD |
| `4H` | `MEXC` | `51.28%` | `48.72%` | `1.05` | 2,210,000.00 USD |
| `4H` | `Bitunix` | `51.51%` | `48.49%` | `1.06` | 1,200,000.00 USD |
| `4H` | `Hyperliquid` | `45.37%` | `54.63%` | `0.83` | 992,020.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `50.13%` | `49.87%` | `1.01` | 3,890,000.00 USD |
| `4H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `WhiteBIT` | `21.06%` | `78.94%` | `0.27` | 961,780.00 USD |
| `4H` | `HTX` | `46.96%` | `53.04%` | `0.89` | 55,670.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `52.83%` | `47.17%` | `1.12` | 171,820.00 USD |
| `4H` | `Aster` | `32.89%` | `67.11%` | `0.49` | 130,880.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Whale Positions` | `46.58%` | `53.42%` | `0.87` | 13,120,000.00 USD |
| `4H` | `Global Accounts` | `46.90%` | `53.10%` | `0.88` | 36,350,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5:00 UTC` | `283.25` | `283.21` | `283.25` | `284.31` | `282.15` | 1,057,540.43 USD | 470,059.99 USD | 587,480.45 USD | -117,420.46 USD | `-11.10%` | `22B / 38S` |
| `0:00 UTC` | `283.98` | `283.94` | `283.98` | `284.82` | `282.24` | 1,354,856.78 USD | 789,515.89 USD | 565,340.89 USD | 224,175.00 USD | `+16.55%` | `34B / 15S` |
| `5:00 UTC` | `287.25` | `286.10` | `287.25` | `288.25` | `284.09` | 2,685,023.61 USD | 1,441,619.22 USD | 1,243,404.38 USD | 198,214.84 USD | `+7.38%` | `22B / 9S` |
| `0:00 UTC` | `290.18` | `290.75` | `290.18` | `293.42` | `286.94` | 7,434,288.46 USD | 2,860,219.97 USD | 4,574,068.49 USD | -1,713,848.52 USD | `-23.05%` | `22B / 26S` |
| `5:00 UTC` | `290.33` | `290.07` | `290.33` | `290.97` | `289.12` | 2,596,782.25 USD | 1,062,961.61 USD | 1,533,820.64 USD | -470,859.04 USD | `-18.13%` | `12B / 36S` |
| `0:00 UTC` | `287.31` | `288.38` | `287.31` | `290.09` | `287.09` | 2,309,907.78 USD | 1,171,627.08 USD | 1,138,280.70 USD | 33,346.39 USD | `+1.44%` | `26B / 14S` |
| `5:00 UTC` | `288.66` | `288.97` | `288.66` | `290.08` | `287.98` | 1,528,178.86 USD | 694,047.00 USD | 834,131.86 USD | -140,084.86 USD | `-9.17%` | `9B / 26S` |
| `0:00 UTC` | `290.00` | `289.14` | `290.00` | `290.24` | `288.04` | 1,415,488.00 USD | 804,419.88 USD | 611,068.12 USD | 193,351.76 USD | `+13.66%` | `22B / 10S` |
| `5:00 UTC` | `291.01` | `290.07` | `291.01` | `291.25` | `288.53` | 1,470,760.68 USD | 873,919.07 USD | 596,841.60 USD | 277,077.47 USD | `+18.84%` | `36B / 9S` |
| `0:00 UTC` | `291.13` | `291.13` | `291.13` | `291.58` | `290.50` | 201,302.15 USD | 114,374.35 USD | 86,927.80 USD | 27,446.55 USD | `+13.63%` | `43B / 23S` |

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
| `5m` | 33,490.00 USD | 492,350.00 USD | **`ACCUMULATION`** |
| `15m` | 108,600.00 USD | 961,970.00 USD | **`ACCUMULATION`** |
| `30m` | 145,970.00 USD | 1,040,000.00 USD | **`ACCUMULATION`** |
| `1h` | 92,350.00 USD | 523,920.00 USD | **`ACCUMULATION`** |
| `2h` | -44,970.00 USD | -2,570,000.00 USD | **`DISTRIBUTION`** |
| `4h` | 431,300.00 USD | -1,710,000.00 USD | **`DISTRIBUTION`** |
| `6h` | 243,180.00 USD | -469,490.00 USD | **`DISTRIBUTION`** |
| `8h` | 263,840.00 USD | -1,650,000.00 USD | **`DISTRIBUTION`** |
| `12h` | 303,730.00 USD | -2,960,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -933,750.00 USD | -7,550,000.00 USD | **`DISTRIBUTION`** |
| `1w` | 346,680.00 USD | -11,900,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -13,420,000.00 USD | -135,890,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+33.49K` | 15m=`+108.60K` | 1h=`+92.35K` | 24h=`-933.75K`
* Futures Capital Netflows: 5m=`+492.35K` | 15m=`+961.97K` | 1h=`+523.92K` | 24h=`-7.55M`
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
  * `2026-10-29 23:01:06 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-29 22:55:06 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-29 22:45:06 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:06:06 IST`: [fxstreet.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:01:06 IST`: [ForexFactory] - (Sentiment: `Neutral`)
  * `2026-10-29 23:01:06 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-29 23:01:06 IST`: [youtube.com/bankofcanadaofficial] - (Sentiment: `Neutral`)
  * `2026-10-29 23:00:06 IST`: [notayesmanseconomics.wordpress.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:00:06 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:00:06 IST`: [breakingthenews.net] - (Sentiment: `Neutral`)
  * `2026-10-29 20:02:06 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-29 20:02:06 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-29 20:02:06 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-29 20:02:06 IST`: [youtube.com/ecbeuro] - (Sentiment: `Neutral`)
  * `2026-10-29 19:02:06 IST`: [ecb.europa.eu] - (Sentiment: `Neutral`)


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
  * Spread-Padded Stop Loss: `274.45` (Risk Distance: `2.07` pts)
  * +2.5R Take Profit: `281.69`
  * Mathematical Lot Sizing: **`4.83 lots`** (Nominal Risk = `0.10 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `286.95` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `289.02` (Risk Distance: `2.07` pts)
  * +2.5R Take Profit: `281.77`
  * Mathematical Lot Sizing: **`4.83 lots`** (Nominal Risk = `0.10 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`PASSIVE_MAKER_LIMIT_ARMED`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`292.37`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
