# 🏛️ SOVEREIGN CANDIDATE DOSSIER: BCH
**Canonical Key**: `BCH` | **Broker Instrument**: `BCHUSD.p` | **Asset Class**: `Crypto PoW`
**Timestamp**: `2026-10-29 22:33:52 IST` (`2026-10-29 17:03:52 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `287.86` | **Live Ask Quote**: `288.44` | **Mid Price**: `288.15`
- **Spread Points**: `580.00` | **Spread BPS**: `20.13 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `280.64` | VWAP Z-Score: `+0.75` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `1.47` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `67.64` (State: `OVERBOUGHT`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `289.49` | Lower -3.00σ Band: `271.79`
  * Upper +2.51σ Band: `288.04` | Lower -2.51σ Band: `273.23`
  * Upper +2.01σ Band: `286.57` | Lower -2.01σ Band: `274.71`
  * Upper +2.00σ Band: `286.54` | Lower -2.00σ Band: `274.74`
  * Upper +1.28σ Band: `284.42` | Lower -1.28σ Band: `276.86`
  * Upper +1.00σ Band: `283.59` | Lower -1.00σ Band: `277.69`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`279.56` | EMA-20=`279.32` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`280.51` (Slope: `+0.0000`) | EMA-100=`283.14`
  * Institutional Anchors: EMA-144=`284.18` | EMA-200=`283.97` (Slope: `-0.2257`) | EMA-233=`284.17`
- **Range Boundaries**: 24H High=`293.86` | 24H Low=`274.76` | Weekly High=`304.16` | Weekly Low=`274.16`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `285.98` (Distance: `+0.72%`)
  * Point of Control (POC) = `278.70` (Distance: `+3.35%`)
  * Value Area Low (VAL) = `276.52` (Distance: `+4.17%`)
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
  * Golden Pocket Zone (0.618 - 0.650): `287.00` - `289.30`
  * Optimal Trade Entry (OTE 0.705): `288.73`
  * Structural Invalidation Anchor (0.786): `290.46`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `288.90` | `289.00` | `288.08` | `288.62` | `1,648` | 475,461.26 USD | -51,511.59 USD | `-10.83%` | -3,598,439.29 USD | `+0.15` | **`BEARISH`** | `DELTA ALIGNED` |
| `5m` | `288.62` | `288.78` | `287.97` | `288.48` | `1,183` | 341,156.90 USD | -41,132.00 USD | `-12.06%` | -3,639,571.28 USD | `+0.20` | **`BEARISH`** | `DELTA ALIGNED` |
| `5m` | `288.48` | `288.56` | `288.13` | `288.25` | `333` | 95,971.27 USD | -8,273.95 USD | `-8.62%` | -3,647,845.24 USD | `+0.30` | **`BEARISH`** | `DELTA ALIGNED` |
| `15m` | `289.20` | `290.08` | `287.08` | `289.59` | `8,010` | 2,309,907.78 USD | 33,346.39 USD | `+1.44%` | -3,863,737.93 USD | `+0.12` | **`BULLISH`** | `NEUTRAL CHOP` |
| `15m` | `289.60` | `290.07` | `287.97` | `288.48` | `5,289` | 1,528,178.86 USD | -140,084.86 USD | `-9.17%` | -4,003,822.79 USD | `-0.26` | **`BEARISH`** | `DELTA ALIGNED` |
| `15m` | `288.48` | `288.56` | `288.13` | `288.17` | `317` | 91,381.88 USD | -12,863.33 USD | `-14.08%` | -4,016,686.13 USD | `+0.03` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `282.43` | `288.24` | `282.14` | `287.96` | `22,353` | 6,361,302.26 USD | 275,075.91 USD | `+4.32%` | -1,829,450.48 USD | `+0.48` | **`BULLISH`** | `NEUTRAL CHOP` |
| `1h` | `287.97` | `293.41` | `286.92` | `288.48` | `47,822` | 13,869,157.35 USD | -2,291,446.03 USD | `-16.52%` | -4,120,896.51 USD | `-2.84` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `1h` | `288.48` | `288.56` | `288.13` | `288.28` | `288` | 83,018.70 USD | -10,656.89 USD | `-12.84%` | -4,131,553.40 USD | `+0.29` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `278.88` | `282.00` | `277.22` | `279.37` | `40,922` | 11,454,296.89 USD | -658,851.13 USD | `-5.75%` | -2,731,740.69 USD | `+0.02` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `279.38` | `288.24` | `277.49` | `287.96` | `74,069` | 20,847,128.37 USD | 1,744,736.30 USD | `+8.37%` | -987,004.39 USD | `+1.23` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `287.97` | `293.41` | `286.92` | `288.25` | `48,155` | 13,965,128.62 USD | -2,299,719.98 USD | `-16.47%` | -3,286,724.37 USD | `-1.07` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `288.93` | `289.90` | `275.10` | `277.35` | `99,418` | 27,984,350.92 USD | -2,870,393.66 USD | `-10.26%` | -1,919,042.18 USD | `-1.00` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `277.35` | `282.39` | `276.59` | `278.88` | `47,861` | 13,383,109.09 USD | -153,847.38 USD | `-1.15%` | -2,072,889.56 USD | `+0.33` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `278.88` | `282.00` | `277.22` | `279.37` | `40,922` | 11,454,296.89 USD | -658,851.13 USD | `-5.75%` | -2,731,740.69 USD | `+0.02` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `279.38` | `288.24` | `277.49` | `287.96` | `74,069` | 20,847,128.37 USD | 1,744,736.30 USD | `+8.37%` | -987,004.39 USD | `+1.23` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `287.97` | `293.41` | `286.92` | `288.25` | `48,155` | 13,965,128.62 USD | -2,299,719.98 USD | `-16.47%` | -3,286,724.37 USD | `-1.07` | **`BEARISH`** | `BEARISH ABSORPTION` |

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
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-29 22:31:36 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `2020` | `0x12d2...f97f` | `LONG` | 1,014,721.23 USD | `3,627,243,000,000.00` | `303.26` | `279.42` | `0.000000` | -85,278.11 USD | `-8.40%` | `10X Cross` |

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
| `7D` | `Long Liquidation` | `249.40` | 14,810,000.00 USD | 14,810,000.00 USD | 50,130.00 USD | 28,020.00 USD | 15,520.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `249.80` | 5,070,000.00 USD | 5,070,000.00 USD | 10,830.00 USD | 1,230.00 USD | 3,490.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `249.80` | 14,710,000.00 USD | 14,710,000.00 USD | 21,060.00 USD | 30,960.00 USD | 32,870.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `250.10` | 5,060,000.00 USD | 5,060,000.00 USD | 7,770.00 USD | 47.40 USD | 1,920.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `250.20` | 14,630,000.00 USD | 14,630,000.00 USD | 42,320.00 USD | 33,800.00 USD | 10,590.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `250.40` | 5,050,000.00 USD | 5,050,000.00 USD | 4,180.00 USD | 2,430.00 USD | 1,340.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `250.50` | 1,330.00 USD | 188,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `250.60` | 14,540,000.00 USD | 14,540,000.00 USD | 18,400.00 USD | 33,950.00 USD | 13,800.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `250.70` | 5,040,000.00 USD | 5,040,000.00 USD | 3,620.00 USD | 9,520.00 USD | 1.83 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `251.00` | 5,030,000.00 USD | 5,030,000.00 USD | 28,400.00 USD | 35,020.00 USD | 5,480.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `251.00` | 14,480,000.00 USD | 14,480,000.00 USD | 42,670.00 USD | 45,820.00 USD | 13,880.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `251.30` | 4,960,000.00 USD | 4,960,000.00 USD | 8,000.00 USD | 21,950.00 USD | 12,050.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `251.40` | 14,370,000.00 USD | 14,370,000.00 USD | 10,060.00 USD | 69,300.00 USD | 22,210.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `251.50` | 268.35 USD | 187,380.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `251.60` | 4,920,000.00 USD | 4,920,000.00 USD | 10,130.00 USD | 30,750.00 USD | 5,130.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `251.80` | 14,270,000.00 USD | 14,270,000.00 USD | 55,620.00 USD | 45,720.00 USD | 35,820.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `251.90` | 4,870,000.00 USD | 4,870,000.00 USD | 21,580.00 USD | 16,100.00 USD | 9,010.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `252.20` | 4,820,000.00 USD | 4,820,000.00 USD | 9,410.00 USD | 7,370.00 USD | 5,650.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `252.20` | 14,140,000.00 USD | 14,140,000.00 USD | 53,090.00 USD | 22,620.00 USD | 17,360.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `252.50` | 4,800,000.00 USD | 4,800,000.00 USD | 186.30 USD | 92.40 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `252.50` | 1,030.00 USD | 187,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `252.60` | 14,040,000.00 USD | 14,040,000.00 USD | 46,110.00 USD | 17,160.00 USD | 7,910.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `252.80` | 4,800,000.00 USD | 4,800,000.00 USD | 11,380.00 USD | 5,970.00 USD | 2,180.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `253.00` | 13,970,000.00 USD | 13,970,000.00 USD | 18,270.00 USD | 19,290.00 USD | 7.83 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `253.10` | 4,780,000.00 USD | 4,780,000.00 USD | 5,420.00 USD | 11,520.00 USD | 796.24 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `253.40` | 4,760,000.00 USD | 4,760,000.00 USD | 13,050.00 USD | 8,570.00 USD | 9,210.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `253.40` | 13,930,000.00 USD | 13,930,000.00 USD | 25,510.00 USD | 49,680.00 USD | 50,850.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `253.70` | 4,730,000.00 USD | 4,730,000.00 USD | 1,670.00 USD | 4,650.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `253.80` | 13,810,000.00 USD | 13,810,000.00 USD | 4,550.00 USD | 19,600.00 USD | 4,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `254.00` | 4,730,000.00 USD | 4,730,000.00 USD | 144.00 USD | 2,390.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `254.20` | 13,780,000.00 USD | 13,780,000.00 USD | 38,950.00 USD | 38,390.00 USD | 25,760.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `254.30` | 4,720,000.00 USD | 4,720,000.00 USD | 0.00 USD | 48.50 USD | 4,090.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `254.50` | 11,650.00 USD | 186,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `254.60` | 4,720,000.00 USD | 4,720,000.00 USD | 173.42 USD | 2,050.00 USD | 8,550.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `254.60` | 13,680,000.00 USD | 13,680,000.00 USD | 23,730.00 USD | 15,110.00 USD | 12,590.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `254.90` | 4,710,000.00 USD | 4,710,000.00 USD | 17,900.00 USD | 189.05 USD | 9,750.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `255.00` | 13,630,000.00 USD | 13,630,000.00 USD | 15,150.00 USD | 11,150.00 USD | 23,850.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `255.20` | 4,680,000.00 USD | 4,680,000.00 USD | 2,810.00 USD | 0.00 USD | 1.53 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `255.40` | 13,580,000.00 USD | 13,580,000.00 USD | 51,160.00 USD | 865.65 USD | 23,840.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `255.50` | 4,680,000.00 USD | 4,680,000.00 USD | 5,490.00 USD | 194.85 USD | 5,900.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `255.50` | 3,660.00 USD | 174,440.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `255.80` | 4,670,000.00 USD | 4,670,000.00 USD | 5,580.00 USD | 2,150.00 USD | 74.53 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `255.80` | 13,500,000.00 USD | 13,500,000.00 USD | 16,010.00 USD | 13,040.00 USD | 49,720.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `256.10` | 4,660,000.00 USD | 4,660,000.00 USD | 11,210.00 USD | 1,850.00 USD | 6,390.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `256.20` | 13,420,000.00 USD | 13,420,000.00 USD | 72,170.00 USD | 38,920.00 USD | 29,750.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `256.40` | 4,640,000.00 USD | 4,640,000.00 USD | 0.00 USD | 2,120.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `256.50` | 2,480.00 USD | 170,780.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `256.60` | 13,280,000.00 USD | 13,280,000.00 USD | 20,630.00 USD | 7,850.00 USD | 12,190.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `256.70` | 4,640,000.00 USD | 4,640,000.00 USD | 4,760.00 USD | 4,570.00 USD | 10,050.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `257.00` | 4,620,000.00 USD | 4,620,000.00 USD | 4,410.00 USD | 12,310.00 USD | 3.61 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `257.00` | 13,240,000.00 USD | 13,240,000.00 USD | 39,780.00 USD | 9,470.00 USD | 47,860.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `257.30` | 4,600,000.00 USD | 4,600,000.00 USD | 113.97 USD | 5,250.00 USD | 0.90 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `257.40` | 13,140,000.00 USD | 13,140,000.00 USD | 27,690.00 USD | 2,250.00 USD | 10.02 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `257.50` | 366.42 USD | 168,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `257.60` | 4,600,000.00 USD | 4,600,000.00 USD | 479.45 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `257.80` | 13,110,000.00 USD | 13,110,000.00 USD | 29,320.00 USD | 5,870.00 USD | 18,190.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `257.90` | 4,600,000.00 USD | 4,600,000.00 USD | 3,740.00 USD | 847.00 USD | 12,070.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `258.20` | 4,580,000.00 USD | 4,580,000.00 USD | 0.00 USD | 6,210.00 USD | 8,030.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `258.20` | 13,060,000.00 USD | 13,060,000.00 USD | 107,190.00 USD | 47,210.00 USD | 18,210.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `258.50` | 4,560,000.00 USD | 4,560,000.00 USD | 7,980.00 USD | 7,140.00 USD | 2.15 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `258.50` | 176.56 USD | 167,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `258.60` | 12,890,000.00 USD | 12,890,000.00 USD | 74,820.00 USD | 7,510.00 USD | 20,990.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `258.80` | 4,550,000.00 USD | 4,550,000.00 USD | 17,830.00 USD | 5,620.00 USD | 11,360.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `259.00` | 12,780,000.00 USD | 12,780,000.00 USD | 21,380.00 USD | 14,730.00 USD | 42,370.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `259.10` | 4,510,000.00 USD | 4,510,000.00 USD | 105.75 USD | 6,040.00 USD | 10,720.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `259.40` | 4,500,000.00 USD | 4,500,000.00 USD | 2,660.00 USD | 31.48 USD | 3,360.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `259.40` | 12,700,000.00 USD | 12,700,000.00 USD | 3,040.00 USD | 32,950.00 USD | 92.22 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `259.70` | 4,490,000.00 USD | 4,490,000.00 USD | 17,120.00 USD | 13,310.00 USD | 3.21 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `259.80` | 12,670,000.00 USD | 12,670,000.00 USD | 18,420.00 USD | 11,850.00 USD | 56.32 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `260.00` | 4,460,000.00 USD | 4,460,000.00 USD | 1,340.00 USD | 4,650.00 USD | 9,890.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `260.20` | 12,640,000.00 USD | 12,640,000.00 USD | 23,100.00 USD | 10,140.00 USD | 8,870.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `260.30` | 4,450,000.00 USD | 4,450,000.00 USD | 2,410.00 USD | 8,120.00 USD | 820.48 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `260.50` | 3,860.00 USD | 167,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `260.60` | 4,430,000.00 USD | 4,430,000.00 USD | 4,750.00 USD | 14,900.00 USD | 2.89 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `260.60` | 12,600,000.00 USD | 12,600,000.00 USD | 5,710.00 USD | 40,460.00 USD | 14,130.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `260.90` | 4,410,000.00 USD | 4,410,000.00 USD | 9,850.00 USD | 1,560.00 USD | 0.67 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `261.00` | 12,540,000.00 USD | 12,540,000.00 USD | 7,110.00 USD | 20,590.00 USD | 16,040.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `261.20` | 4,400,000.00 USD | 4,400,000.00 USD | 95.62 USD | 2,220.00 USD | 2,830.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `261.40` | 12,490,000.00 USD | 12,490,000.00 USD | 15,870.00 USD | 25,100.00 USD | 2,470.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `261.50` | 4,400,000.00 USD | 4,400,000.00 USD | 2,050.00 USD | 6,940.00 USD | 1,630.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `261.80` | 4,390,000.00 USD | 4,390,000.00 USD | 10,920.00 USD | 4,220.00 USD | 4.82 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `261.80` | 12,450,000.00 USD | 12,450,000.00 USD | 41,470.00 USD | 29,410.00 USD | 26,100.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `262.10` | 4,370,000.00 USD | 4,370,000.00 USD | 556.87 USD | 6,260.00 USD | 2,590.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `262.20` | 12,350,000.00 USD | 12,350,000.00 USD | 17,460.00 USD | 35,160.00 USD | 7,560.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `262.40` | 4,360,000.00 USD | 4,360,000.00 USD | 6,980.00 USD | 3,770.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `262.50` | 1,970.00 USD | 163,890.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `262.60` | 12,290,000.00 USD | 12,290,000.00 USD | 37,090.00 USD | 26,170.00 USD | 19,300.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `262.70` | 4,350,000.00 USD | 4,350,000.00 USD | 0.00 USD | 1,220.00 USD | 1,390.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `263.00` | 4,350,000.00 USD | 4,350,000.00 USD | 24.70 USD | 486.36 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `263.00` | 12,210,000.00 USD | 12,210,000.00 USD | 82,070.00 USD | 46,390.00 USD | 39,220.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `263.30` | 4,350,000.00 USD | 4,350,000.00 USD | 4,240.00 USD | 39.48 USD | 2,190.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `263.40` | 12,040,000.00 USD | 12,040,000.00 USD | 96,280.00 USD | 32,090.00 USD | 32,340.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `263.60` | 4,340,000.00 USD | 4,340,000.00 USD | 1,720.00 USD | 830.11 USD | 5.81 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `263.80` | 11,880,000.00 USD | 11,880,000.00 USD | 304,420.00 USD | 100,810.00 USD | 57,890.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `263.90` | 4,340,000.00 USD | 4,340,000.00 USD | 333.33 USD | 2,140.00 USD | 2,720.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `264.20` | 4,330,000.00 USD | 4,330,000.00 USD | 7,740.00 USD | 566.30 USD | 1,780.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `264.20` | 11,420,000.00 USD | 11,420,000.00 USD | 49,040.00 USD | 50,840.00 USD | 7,370.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `264.50` | 4,320,000.00 USD | 4,320,000.00 USD | 2,160.00 USD | 99.53 USD | 36,600.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `264.50` | 280.37 USD | 161,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `264.60` | 11,310,000.00 USD | 11,310,000.00 USD | 25,480.00 USD | 71,630.00 USD | 36,970.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `264.80` | 4,290,000.00 USD | 4,290,000.00 USD | 28,200.00 USD | 777.03 USD | 15,630.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `265.00` | 11,180,000.00 USD | 11,180,000.00 USD | 53,060.00 USD | 23,600.00 USD | 79,530.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `265.10` | 4,240,000.00 USD | 4,240,000.00 USD | 19,700.00 USD | 8,450.00 USD | 10.14 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `265.40` | 4,210,000.00 USD | 4,210,000.00 USD | 1,130.00 USD | 11,640.00 USD | 33,560.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `265.40` | 11,020,000.00 USD | 11,020,000.00 USD | 133,460.00 USD | 54,660.00 USD | 91,640.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `265.50` | 121,910.00 USD | 161,640.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `265.70` | 4,170,000.00 USD | 4,170,000.00 USD | 23,780.00 USD | 12,140.00 USD | 33,660.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `265.80` | 10,740,000.00 USD | 10,740,000.00 USD | 50,530.00 USD | 93,230.00 USD | 28,830.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `266.00` | 4,100,000.00 USD | 4,100,000.00 USD | 323.40 USD | 500.72 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `266.20` | 10,570,000.00 USD | 10,570,000.00 USD | 168,970.00 USD | 158,090.00 USD | 68,240.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `266.30` | 4,100,000.00 USD | 4,100,000.00 USD | 32,620.00 USD | 193.83 USD | 5,030.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `266.60` | 4,060,000.00 USD | 4,060,000.00 USD | 14,610.00 USD | 3,250.00 USD | 3,710.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `266.60` | 10,170,000.00 USD | 10,170,000.00 USD | 141,550.00 USD | 54,870.00 USD | 119,920.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `266.90` | 4,040,000.00 USD | 4,040,000.00 USD | 23,980.00 USD | 6,460.00 USD | 6,760.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `267.00` | 9,860,000.00 USD | 9,860,000.00 USD | 89,220.00 USD | 165,740.00 USD | 49,630.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `267.20` | 4,000,000.00 USD | 4,000,000.00 USD | 6,240.00 USD | 130.70 USD | 3,340.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `267.40` | 9,550,000.00 USD | 9,550,000.00 USD | 107,800.00 USD | 202,150.00 USD | 88,200.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `267.50` | 3,990,000.00 USD | 3,990,000.00 USD | 11,990.00 USD | 26,360.00 USD | 46.69 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `267.50` | 1,490.00 USD | 39,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `267.80` | 3,950,000.00 USD | 3,950,000.00 USD | 96,470.00 USD | 108,630.00 USD | 33,350.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `267.80` | 9,150,000.00 USD | 9,150,000.00 USD | 179,590.00 USD | 209,540.00 USD | 94,090.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `268.10` | 3,710,000.00 USD | 3,710,000.00 USD | 29,710.00 USD | 68,110.00 USD | 16,580.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `268.20` | 8,670,000.00 USD | 8,670,000.00 USD | 124,430.00 USD | 247,680.00 USD | 84,790.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `268.40` | 3,600,000.00 USD | 3,600,000.00 USD | 31,470.00 USD | 67,680.00 USD | 11,200.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `268.50` | 7,020.00 USD | 38,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `268.60` | 8,210,000.00 USD | 8,210,000.00 USD | 175,020.00 USD | 137,470.00 USD | 50,840.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `268.70` | 3,490,000.00 USD | 3,490,000.00 USD | 68,110.00 USD | 47,730.00 USD | 22,530.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `269.00` | 3,350,000.00 USD | 3,350,000.00 USD | 34,110.00 USD | 21,820.00 USD | 16,400.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `269.00` | 7,850,000.00 USD | 7,850,000.00 USD | 207,700.00 USD | 143,940.00 USD | 80,400.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `269.30` | 3,280,000.00 USD | 3,280,000.00 USD | 4,290.00 USD | 3,900.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `269.40` | 7,420,000.00 USD | 7,420,000.00 USD | 246,990.00 USD | 118,760.00 USD | 59,990.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `269.50` | 11,700.00 USD | 31,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `269.60` | 3,270,000.00 USD | 3,270,000.00 USD | 22,180.00 USD | 20,470.00 USD | 1,640.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `269.80` | 6,990,000.00 USD | 6,990,000.00 USD | 52,590.00 USD | 129,880.00 USD | 13,210.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `269.90` | 3,220,000.00 USD | 3,220,000.00 USD | 25,660.00 USD | 25,330.00 USD | 11,350.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `270.20` | 3,160,000.00 USD | 3,160,000.00 USD | 97,940.00 USD | 51,650.00 USD | 96,360.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `270.20` | 6,800,000.00 USD | 6,800,000.00 USD | 140,940.00 USD | 137,560.00 USD | 147,130.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `270.50` | 2,920,000.00 USD | 2,920,000.00 USD | 58,030.00 USD | 27,020.00 USD | 34,320.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `270.60` | 6,370,000.00 USD | 6,370,000.00 USD | 240,990.00 USD | 153,950.00 USD | 182,640.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `270.80` | 2,800,000.00 USD | 2,800,000.00 USD | 3,370.00 USD | 16,950.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `271.00` | 5,790,000.00 USD | 5,790,000.00 USD | 197,440.00 USD | 99,980.00 USD | 67,740.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `271.10` | 2,780,000.00 USD | 2,780,000.00 USD | 31,070.00 USD | 22,900.00 USD | 134,200.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `271.40` | 2,590,000.00 USD | 2,590,000.00 USD | 28,220.00 USD | 23,780.00 USD | 10,220.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `271.40` | 5,430,000.00 USD | 5,430,000.00 USD | 96,260.00 USD | 114,640.00 USD | 63,240.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `271.50` | 1,000.00 USD | 19,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `271.70` | 2,530,000.00 USD | 2,530,000.00 USD | 40,350.00 USD | 18,860.00 USD | 35,790.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `271.80` | 5,150,000.00 USD | 5,150,000.00 USD | 427,350.00 USD | 47,340.00 USD | 53,290.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `272.00` | 2,430,000.00 USD | 2,430,000.00 USD | 87,430.00 USD | 15,560.00 USD | 32,720.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `272.20` | 4,630,000.00 USD | 4,630,000.00 USD | 218,980.00 USD | 49,070.00 USD | 157,760.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `272.30` | 2,300,000.00 USD | 2,300,000.00 USD | 49,280.00 USD | 228.77 USD | 9,620.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `272.60` | 2,240,000.00 USD | 2,240,000.00 USD | 54,020.00 USD | 23,670.00 USD | 32,720.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `272.60` | 4,200,000.00 USD | 4,200,000.00 USD | 139,010.00 USD | 196,770.00 USD | 30,450.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `272.90` | 2,130,000.00 USD | 2,130,000.00 USD | 65,700.00 USD | 52,790.00 USD | 4.88 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `273.00` | 3,830,000.00 USD | 3,830,000.00 USD | 211,830.00 USD | 189,410.00 USD | 123,670.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `273.20` | 2,010,000.00 USD | 2,010,000.00 USD | 50,860.00 USD | 101,090.00 USD | 35,090.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `273.40` | 3,310,000.00 USD | 3,310,000.00 USD | 199,880.00 USD | 303,570.00 USD | 142,390.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `273.50` | 1,820,000.00 USD | 1,820,000.00 USD | 188,260.00 USD | 156,220.00 USD | 76,810.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `273.80` | 1,400,000.00 USD | 1,400,000.00 USD | 44,050.00 USD | 184,350.00 USD | 45,090.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `273.80` | 2,660,000.00 USD | 2,660,000.00 USD | 259,450.00 USD | 405,750.00 USD | 199,690.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `274.10` | 1,130,000.00 USD | 1,130,000.00 USD | 109,520.00 USD | 152,730.00 USD | 37,400.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `274.20` | 1,800,000.00 USD | 1,800,000.00 USD | 348,580.00 USD | 204,690.00 USD | 127,490.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `274.40` | 826,260.00 USD | 826,260.00 USD | 147,600.00 USD | 84,390.00 USD | 52,490.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `274.50` | 567.94 USD | 18,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `274.60` | 1,120,000.00 USD | 1,120,000.00 USD | 334,810.00 USD | 183,210.00 USD | 71,130.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `274.70` | 541,780.00 USD | 541,780.00 USD | 33,340.00 USD | 23,030.00 USD | 35,230.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `275.00` | 450,180.00 USD | 450,180.00 USD | 29,690.00 USD | 19,130.00 USD | 20,830.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `275.00` | 527,720.00 USD | 527,720.00 USD | 180,050.00 USD | 99,570.00 USD | 34,620.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `275.30` | 380,530.00 USD | 380,530.00 USD | 68,900.00 USD | 42,670.00 USD | 32,660.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `275.40` | 213,480.00 USD | 213,480.00 USD | 1,240.00 USD | 126,890.00 USD | 9,040.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `275.60` | 236,310.00 USD | 236,310.00 USD | 11,630.00 USD | 37,380.00 USD | 8,730.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `275.80` | 76,310.00 USD | 76,310.00 USD | 1,090.00 USD | 25,250.00 USD | 65.70 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `275.90` | 178,560.00 USD | 178,560.00 USD | 31,610.00 USD | 11,430.00 USD | 8,060.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `276.20` | 127,460.00 USD | 127,460.00 USD | 35,160.00 USD | 21,250.00 USD | 3,230.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `276.20` | 49,900.00 USD | 49,900.00 USD | 2,660.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `276.50` | 67,820.00 USD | 67,820.00 USD | 79.10 USD | 13,020.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `276.50` | 205.44 USD | 17,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `276.60` | 47,230.00 USD | 47,230.00 USD | 485.90 USD | 233.30 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `277.00` | 46,510.00 USD | 46,510.00 USD | 883.77 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `277.10` | 54,720.00 USD | 54,720.00 USD | 0.00 USD | 38,970.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `277.40` | 15,760.00 USD | 15,760.00 USD | 0.00 USD | 15,750.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `277.40` | 45,630.00 USD | 45,630.00 USD | 0.00 USD | 44,640.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `278.00` | 4.50 USD | 4.50 USD | 0.00 USD | 0.00 USD | 4.50 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `278.60` | 992.27 USD | 992.27 USD | 0.00 USD | 0.00 USD | 9.96 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `279.00` | 982.31 USD | 982.31 USD | 0.00 USD | 933.19 USD | 49.12 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `280.60` | 66,170.00 USD | 66,170.00 USD | 0.00 USD | 0.00 USD | 66,170.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `280.70` | 46,700.00 USD | 46,700.00 USD | 0.00 USD | 0.00 USD | 46,700.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `281.40` | 66,770.00 USD | 66,770.00 USD | 565.82 USD | 0.00 USD | 33.20 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `281.80` | 438,830.00 USD | 438,830.00 USD | 107,230.00 USD | 43,540.00 USD | 221,290.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `281.90` | 113,590.00 USD | 113,590.00 USD | 0.00 USD | 0.00 USD | 66,890.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `282.20` | 316,880.00 USD | 316,880.00 USD | 30,440.00 USD | 46,080.00 USD | 126,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `282.20` | 525,110.00 USD | 525,110.00 USD | 0.00 USD | 51,480.00 USD | 34,800.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `282.50` | 361,330.00 USD | 361,330.00 USD | 16,460.00 USD | 13,450.00 USD | 14,540.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `282.60` | 608,120.00 USD | 608,120.00 USD | 83,010.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `282.80` | 482,170.00 USD | 482,170.00 USD | 101,550.00 USD | 9,800.00 USD | 9,490.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `283.10` | 607,800.00 USD | 607,800.00 USD | 57,750.00 USD | 14,850.00 USD | 53,030.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `283.40` | 665,870.00 USD | 665,870.00 USD | 19,130.00 USD | 5,990.00 USD | 32,960.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `283.40` | 794,200.00 USD | 794,200.00 USD | 47,330.00 USD | 49,490.00 USD | 89,260.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `283.70` | 808,760.00 USD | 808,760.00 USD | 117,870.00 USD | 11,490.00 USD | 13,520.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `283.80` | 967,440.00 USD | 967,440.00 USD | 13,900.00 USD | 80,650.00 USD | 78,690.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `284.00` | 883,370.00 USD | 883,370.00 USD | 28,000.00 USD | 21,660.00 USD | 24,950.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `284.20` | 1,090,000.00 USD | 1,090,000.00 USD | 60,830.00 USD | 56,980.00 USD | 8,610.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `284.30` | 972,270.00 USD | 972,270.00 USD | 22,210.00 USD | 57,290.00 USD | 9,410.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `284.60` | 1,390,000.00 USD | 1,390,000.00 USD | 170,510.00 USD | 189,320.00 USD | 59,680.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `284.60` | 1,420,000.00 USD | 1,420,000.00 USD | 71,990.00 USD | 191,100.00 USD | 64,370.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `284.90` | 1,620,000.00 USD | 1,620,000.00 USD | 58,130.00 USD | 138,810.00 USD | 33,160.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `285.00` | 1,680,000.00 USD | 1,680,000.00 USD | 101,800.00 USD | 136,560.00 USD | 16,680.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `285.20` | 1,850,000.00 USD | 1,850,000.00 USD | 62,110.00 USD | 135,170.00 USD | 35,360.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `285.40` | 1,890,000.00 USD | 1,890,000.00 USD | 0.00 USD | 173,140.00 USD | 41,910.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `285.50` | 2,130,000.00 USD | 2,130,000.00 USD | 135,460.00 USD | 95,280.00 USD | 45,030.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `285.50` | 17,750.00 USD | 17,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `285.80` | 2,270,000.00 USD | 2,270,000.00 USD | 67,030.00 USD | 42,840.00 USD | 32,710.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `285.80` | 2,080,000.00 USD | 2,080,000.00 USD | 87,960.00 USD | 97,960.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `286.10` | 2,290,000.00 USD | 2,290,000.00 USD | 8,520.00 USD | 7,060.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `286.20` | 2,120,000.00 USD | 2,120,000.00 USD | 0.00 USD | 40,670.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `286.40` | 2,370,000.00 USD | 2,370,000.00 USD | 42,610.00 USD | 40,040.00 USD | 3,280.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `286.60` | 2,270,000.00 USD | 2,270,000.00 USD | 23,860.00 USD | 121,370.00 USD | 8,970.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `286.70` | 2,590,000.00 USD | 2,590,000.00 USD | 103,130.00 USD | 50,280.00 USD | 59,280.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `287.00` | 2,820,000.00 USD | 2,820,000.00 USD | 77,890.00 USD | 93,350.00 USD | 56,770.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `287.00` | 2,510,000.00 USD | 2,510,000.00 USD | 27,530.00 USD | 115,360.00 USD | 96,530.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `287.30` | 2,910,000.00 USD | 2,910,000.00 USD | 61,620.00 USD | 28,670.00 USD | 7,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `287.40` | 2,690,000.00 USD | 2,690,000.00 USD | 77,180.00 USD | 102,270.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `287.60` | 3,000,000.00 USD | 3,000,000.00 USD | 5,760.00 USD | 46,520.00 USD | 36,680.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `287.80` | 2,940,000.00 USD | 2,940,000.00 USD | 0.00 USD | 244,170.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `287.90` | 3,110,000.00 USD | 3,110,000.00 USD | 53,720.00 USD | 18,140.00 USD | 33,650.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `288.20` | 3,050,000.00 USD | 3,050,000.00 USD | 41,500.00 USD | 75,540.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `288.50` | 3,160,000.00 USD | 3,160,000.00 USD | 32,470.00 USD | 10,250.00 USD | 5,010.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `288.60` | 3,150,000.00 USD | 3,150,000.00 USD | 0.00 USD | 58,240.00 USD | 35,560.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `288.80` | 3,190,000.00 USD | 3,190,000.00 USD | 14,190.00 USD | 3,000.00 USD | 17,530.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `289.00` | 3,180,000.00 USD | 3,180,000.00 USD | 23,660.00 USD | 6,610.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `289.10` | 3,250,000.00 USD | 3,250,000.00 USD | 36,020.00 USD | 12,850.00 USD | 6,760.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `289.40` | 3,250,000.00 USD | 3,250,000.00 USD | 5,830.00 USD | 0.00 USD | 3,340.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `289.40` | 3,240,000.00 USD | 3,240,000.00 USD | 46,870.00 USD | 14,830.00 USD | 4,230.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `289.70` | 3,300,000.00 USD | 3,300,000.00 USD | 11,630.00 USD | 36,980.00 USD | 1.20 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `289.80` | 3,270,000.00 USD | 3,270,000.00 USD | 18,500.00 USD | 947.00 USD | 4,310.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `290.00` | 3,460,000.00 USD | 3,460,000.00 USD | 102,350.00 USD | 44,320.00 USD | 9,560.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `290.20` | 3,620,000.00 USD | 3,620,000.00 USD | 146,360.00 USD | 173,970.00 USD | 32,180.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `290.30` | 3,740,000.00 USD | 3,740,000.00 USD | 119,420.00 USD | 91,590.00 USD | 67,720.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `290.60` | 3,850,000.00 USD | 3,850,000.00 USD | 12,690.00 USD | 96,190.00 USD | 6,500.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `290.60` | 3,810,000.00 USD | 3,810,000.00 USD | 50,900.00 USD | 127,830.00 USD | 8,340.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `290.90` | 4,030,000.00 USD | 4,030,000.00 USD | 81,620.00 USD | 79,980.00 USD | 15,700.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `291.00` | 4,020,000.00 USD | 4,020,000.00 USD | 62,080.00 USD | 127,160.00 USD | 20,930.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `291.20` | 4,260,000.00 USD | 4,260,000.00 USD | 107,540.00 USD | 106,130.00 USD | 19,540.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `291.40` | 4,170,000.00 USD | 4,170,000.00 USD | 73,050.00 USD | 78,370.00 USD | 69.78 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `291.50` | 4,340,000.00 USD | 4,340,000.00 USD | 28,700.00 USD | 39,010.00 USD | 12,910.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `291.80` | 4,370,000.00 USD | 4,370,000.00 USD | 8,030.00 USD | 5,910.00 USD | 9,490.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `291.80` | 4,320,000.00 USD | 4,320,000.00 USD | 32,220.00 USD | 119,880.00 USD | 33.90 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `292.10` | 4,520,000.00 USD | 4,520,000.00 USD | 63,210.00 USD | 36,070.00 USD | 50,270.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `292.20` | 4,490,000.00 USD | 4,490,000.00 USD | 110,850.00 USD | 59,290.00 USD | 4,530.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `292.40` | 4,640,000.00 USD | 4,640,000.00 USD | 20,320.00 USD | 31,270.00 USD | 75,150.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `292.60` | 4,600,000.00 USD | 4,600,000.00 USD | 34,100.00 USD | 26,820.00 USD | 45,930.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `292.70` | 4,790,000.00 USD | 4,790,000.00 USD | 33,180.00 USD | 75,500.00 USD | 37,280.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `293.00` | 4,970,000.00 USD | 4,970,000.00 USD | 113,850.00 USD | 39,090.00 USD | 29,460.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `293.00` | 5,030,000.00 USD | 5,030,000.00 USD | 229,100.00 USD | 150,380.00 USD | 47,160.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `293.30` | 5,120,000.00 USD | 5,120,000.00 USD | 40,580.00 USD | 54,940.00 USD | 49,820.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `293.40` | 5,370,000.00 USD | 5,370,000.00 USD | 78,760.00 USD | 67,380.00 USD | 199,530.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `293.60` | 5,240,000.00 USD | 5,240,000.00 USD | 41,540.00 USD | 28,650.00 USD | 55,700.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `293.80` | 5,410,000.00 USD | 5,410,000.00 USD | 37,280.00 USD | 1,170.00 USD | 116.86 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `293.90` | 5,300,000.00 USD | 5,300,000.00 USD | 8,360.00 USD | 23,960.00 USD | 19,090.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `294.20` | 5,400,000.00 USD | 5,400,000.00 USD | 26,380.00 USD | 41,970.00 USD | 36,910.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `294.20` | 5,610,000.00 USD | 5,610,000.00 USD | 107,580.00 USD | 22,110.00 USD | 66,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `294.50` | 5,610,000.00 USD | 5,610,000.00 USD | 130,280.00 USD | 57,150.00 USD | 26,570.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `294.60` | 5,610,000.00 USD | 5,610,000.00 USD | 2,110.00 USD | 3,950.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `294.80` | 5,770,000.00 USD | 5,770,000.00 USD | 19,780.00 USD | 63,490.00 USD | 70,850.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `295.00` | 5,830,000.00 USD | 5,830,000.00 USD | 62,390.00 USD | 52,950.00 USD | 104,870.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `295.10` | 5,820,000.00 USD | 5,820,000.00 USD | 19,100.00 USD | 31,970.00 USD | 4,100.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `295.40` | 6,020,000.00 USD | 6,020,000.00 USD | 89,360.00 USD | 80,620.00 USD | 22,040.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `295.40` | 6,100,000.00 USD | 6,100,000.00 USD | 92,780.00 USD | 94,780.00 USD | 83,510.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `295.50` | 612.57 USD | 612.57 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `295.70` | 6,140,000.00 USD | 6,140,000.00 USD | 89,710.00 USD | 13,280.00 USD | 18,270.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `295.80` | 6,200,000.00 USD | 6,200,000.00 USD | 34,250.00 USD | 30,180.00 USD | 31,980.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `296.00` | 6,240,000.00 USD | 6,240,000.00 USD | 32,780.00 USD | 39,150.00 USD | 30,110.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `296.20` | 6,270,000.00 USD | 6,270,000.00 USD | 0.00 USD | 744.75 USD | 67,350.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `296.30` | 6,300,000.00 USD | 6,300,000.00 USD | 18,360.00 USD | 33,370.00 USD | 13,350.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `296.60` | 6,410,000.00 USD | 6,410,000.00 USD | 36,570.00 USD | 38,050.00 USD | 34,560.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `296.60` | 6,350,000.00 USD | 6,350,000.00 USD | 32,100.00 USD | 14,060.00 USD | 29,840.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `296.90` | 6,560,000.00 USD | 6,560,000.00 USD | 53,630.00 USD | 75,460.00 USD | 18,960.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `297.00` | 6,540,000.00 USD | 6,540,000.00 USD | 89,750.00 USD | 51,270.00 USD | 51,390.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `297.20` | 6,600,000.00 USD | 6,600,000.00 USD | 7,110.00 USD | 13,140.00 USD | 13,420.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `297.40` | 6,630,000.00 USD | 6,630,000.00 USD | 3,560.00 USD | 58,390.00 USD | 34,710.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `297.50` | 6,660,000.00 USD | 6,660,000.00 USD | 34,110.00 USD | 18,960.00 USD | 9,430.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `297.80` | 6,670,000.00 USD | 6,670,000.00 USD | 5,570.00 USD | 3,210.00 USD | 6,920.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `297.80` | 6,750,000.00 USD | 6,750,000.00 USD | 16,080.00 USD | 39,720.00 USD | 54,850.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `298.10` | 6,730,000.00 USD | 6,730,000.00 USD | 16,550.00 USD | 4,760.00 USD | 39,750.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `298.20` | 6,830,000.00 USD | 6,830,000.00 USD | 32,390.00 USD | 40,760.00 USD | 16,600.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `298.40` | 6,810,000.00 USD | 6,810,000.00 USD | 22,430.00 USD | 15,590.00 USD | 39,410.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `298.60` | 6,850,000.00 USD | 6,850,000.00 USD | 0.00 USD | 12,430.00 USD | 114.26 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `298.70` | 6,880,000.00 USD | 6,880,000.00 USD | 43,790.00 USD | 21,330.00 USD | 5,670.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `299.00` | 6,980,000.00 USD | 6,980,000.00 USD | 37,310.00 USD | 19,100.00 USD | 36,900.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `299.00` | 6,960,000.00 USD | 6,960,000.00 USD | 70,090.00 USD | 993.25 USD | 39,940.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `299.30` | 7,090,000.00 USD | 7,090,000.00 USD | 39,150.00 USD | 25,770.00 USD | 50,280.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `299.40` | 7,010,000.00 USD | 7,010,000.00 USD | 3,200.00 USD | 1,150.00 USD | 45,890.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `299.50` | 1,220.00 USD | 1,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `299.60` | 7,160,000.00 USD | 7,160,000.00 USD | 34,750.00 USD | 26,920.00 USD | 9,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `299.80` | 7,020,000.00 USD | 7,020,000.00 USD | 5,060.00 USD | 7,930.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `299.90` | 7,200,000.00 USD | 7,200,000.00 USD | 13,590.00 USD | 20,510.00 USD | 5,090.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `300.20` | 7,280,000.00 USD | 7,280,000.00 USD | 52,870.00 USD | 23,950.00 USD | 1,100.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `300.20` | 7,060,000.00 USD | 7,060,000.00 USD | 35,320.00 USD | 2,260.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `300.50` | 7,320,000.00 USD | 7,320,000.00 USD | 1,050.00 USD | 10,730.00 USD | 24,710.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `300.60` | 7,150,000.00 USD | 7,150,000.00 USD | 23,830.00 USD | 52,200.00 USD | 19,730.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `300.80` | 7,370,000.00 USD | 7,370,000.00 USD | 11,300.00 USD | 27,110.00 USD | 12,770.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `301.00` | 7,190,000.00 USD | 7,190,000.00 USD | 0.00 USD | 31,740.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `301.10` | 7,420,000.00 USD | 7,420,000.00 USD | 35,650.00 USD | 18,740.00 USD | 55.50 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `301.40` | 7,470,000.00 USD | 7,470,000.00 USD | 11,900.00 USD | 27,210.00 USD | 9,170.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `301.40` | 7,290,000.00 USD | 7,290,000.00 USD | 46,390.00 USD | 23,180.00 USD | 35,310.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `301.50` | 2,380.00 USD | 4,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `301.70` | 7,500,000.00 USD | 7,500,000.00 USD | 12,880.00 USD | 13,140.00 USD | 7,070.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `301.80` | 7,460,000.00 USD | 7,460,000.00 USD | 76,230.00 USD | 85,660.00 USD | 9,150.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `302.00` | 7,540,000.00 USD | 7,540,000.00 USD | 19,690.00 USD | 14,190.00 USD | 4,050.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `302.20` | 7,590,000.00 USD | 7,590,000.00 USD | 1,160.00 USD | 124,660.00 USD | 2.49 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `302.30` | 7,570,000.00 USD | 7,570,000.00 USD | 9,030.00 USD | 14,010.00 USD | 1,280.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `302.60` | 7,610,000.00 USD | 7,610,000.00 USD | 17,830.00 USD | 19,990.00 USD | 6,540.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `302.60` | 7,660,000.00 USD | 7,660,000.00 USD | 2,480.00 USD | 71,350.00 USD | 109.38 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `302.90` | 7,610,000.00 USD | 7,610,000.00 USD | 286.84 USD | 1,090.00 USD | 2.41 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `303.00` | 7,760,000.00 USD | 7,760,000.00 USD | 37,510.00 USD | 63,670.00 USD | 191.68 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `303.20` | 7,640,000.00 USD | 7,640,000.00 USD | 11,620.00 USD | 263.67 USD | 14,760.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `303.40` | 7,760,000.00 USD | 7,760,000.00 USD | 0.00 USD | 0.00 USD | 33.35 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `303.50` | 7,670,000.00 USD | 7,670,000.00 USD | 17,870.00 USD | 9,140.00 USD | 6,250.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `303.80` | 7,690,000.00 USD | 7,690,000.00 USD | 8,040.00 USD | 3,510.00 USD | 3,460.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `303.80` | 7,820,000.00 USD | 7,820,000.00 USD | 20,720.00 USD | 9,650.00 USD | 24,710.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `304.10` | 7,720,000.00 USD | 7,720,000.00 USD | 11,280.00 USD | 1,100.00 USD | 18,440.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `304.20` | 7,820,000.00 USD | 7,820,000.00 USD | 1,670.00 USD | 839.60 USD | 86.46 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `304.40` | 7,760,000.00 USD | 7,760,000.00 USD | 14,550.00 USD | 11,300.00 USD | 18,460.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `304.60` | 7,840,000.00 USD | 7,840,000.00 USD | 2,960.00 USD | 11,330.00 USD | 72.30 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `304.70` | 7,760,000.00 USD | 7,760,000.00 USD | 83.90 USD | 318.60 USD | 0.93 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `305.00` | 7,790,000.00 USD | 7,790,000.00 USD | 9,110.00 USD | 6,650.00 USD | 8,060.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `305.00` | 8,060,000.00 USD | 8,060,000.00 USD | 95,550.00 USD | 73,310.00 USD | 58,540.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `305.30` | 7,830,000.00 USD | 7,830,000.00 USD | 27,840.00 USD | 7,500.00 USD | 5,160.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `305.40` | 8,320,000.00 USD | 8,320,000.00 USD | 102,210.00 USD | 76,550.00 USD | 73,740.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `305.60` | 7,840,000.00 USD | 7,840,000.00 USD | 6,180.00 USD | 3,220.00 USD | 3,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `305.80` | 8,460,000.00 USD | 8,460,000.00 USD | 80,350.00 USD | 49,520.00 USD | 10,620.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `305.90` | 7,860,000.00 USD | 7,860,000.00 USD | 14,420.00 USD | 2,580.00 USD | 1,970.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `306.20` | 7,870,000.00 USD | 7,870,000.00 USD | 3,720.00 USD | 3,290.00 USD | 1,360.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `306.20` | 8,590,000.00 USD | 8,590,000.00 USD | 30,620.00 USD | 52,500.00 USD | 46,040.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `306.50` | 7,870,000.00 USD | 7,870,000.00 USD | 431.00 USD | 6,700.00 USD | 1.52 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `306.60` | 8,700,000.00 USD | 8,700,000.00 USD | 25,430.00 USD | 23,280.00 USD | 65,860.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `306.80` | 7,940,000.00 USD | 7,940,000.00 USD | 28,600.00 USD | 35,110.00 USD | 5,480.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `307.00` | 8,940,000.00 USD | 8,940,000.00 USD | 61,110.00 USD | 73,890.00 USD | 102,380.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `307.10` | 7,980,000.00 USD | 7,980,000.00 USD | 8,400.00 USD | 22,000.00 USD | 12,050.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `307.40` | 8,000,000.00 USD | 8,000,000.00 USD | 259.96 USD | 17,400.00 USD | 1,820.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `307.40` | 9,150,000.00 USD | 9,150,000.00 USD | 47,700.00 USD | 131,290.00 USD | 38,470.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `307.70` | 8,050,000.00 USD | 8,050,000.00 USD | 15,390.00 USD | 22,570.00 USD | 5,880.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `307.80` | 9,380,000.00 USD | 9,380,000.00 USD | 88,520.00 USD | 81,640.00 USD | 57,870.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `308.00` | 8,090,000.00 USD | 8,090,000.00 USD | 21,620.00 USD | 11,290.00 USD | 7,820.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `308.20` | 9,700,000.00 USD | 9,700,000.00 USD | 152,190.00 USD | 52,080.00 USD | 114,230.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `308.30` | 8,100,000.00 USD | 8,100,000.00 USD | 4,640.00 USD | 3,360.00 USD | 4,260.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `308.60` | 9,810,000.00 USD | 9,810,000.00 USD | 67,700.00 USD | 37,160.00 USD | 8,020.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `309.00` | 9,890,000.00 USD | 9,890,000.00 USD | 26,920.00 USD | 31,940.00 USD | 19,670.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `309.40` | 10,000,000.00 USD | 10,000,000.00 USD | 27,470.00 USD | 35,530.00 USD | 46,500.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `309.80` | 10,340,000.00 USD | 10,340,000.00 USD | 58,300.00 USD | 130,940.00 USD | 147,330.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `310.20` | 10,470,000.00 USD | 10,470,000.00 USD | 15,450.00 USD | 55,950.00 USD | 58,800.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `310.50` | 517.91 USD | 4,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `310.60` | 10,690,000.00 USD | 10,690,000.00 USD | 96,060.00 USD | 103,110.00 USD | 25,750.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `311.00` | 10,770,000.00 USD | 10,770,000.00 USD | 27,060.00 USD | 29,540.00 USD | 21,100.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `311.20` | 10,810,000.00 USD | 10,810,000.00 USD | 40,670.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `318.50` | 114.34 USD | 4,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `319.50` | 6,600.00 USD | 11,440.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `320.50` | 1,110.00 USD | 12,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
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
| `Sell Stop` | `143.50` | 193,090.00 USD | 0.00 USD | 210.94 USD | `-50.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `145.50` | 192,880.00 USD | 0.00 USD | 2,070.00 USD | `-49.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `178.50` | 190,810.00 USD | 0.00 USD | 2,530.00 USD | `-38.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `184.50` | 188,280.00 USD | 0.00 USD | 490.59 USD | `-36.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `196.50` | 187,790.00 USD | 0.00 USD | 482.01 USD | `-31.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `200.50` | 187,310.00 USD | 0.00 USD | 189.07 USD | `-30.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `208.50` | 187,120.00 USD | 0.00 USD | 441.60 USD | `-27.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `210.50` | 186,680.00 USD | 0.00 USD | 703.49 USD | `-27.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `221.50` | 185,980.00 USD | 0.00 USD | 638.36 USD | `-23.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `224.50` | 185,340.00 USD | 0.00 USD | 740.85 USD | `-22.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `228.50` | 184,600.00 USD | 0.00 USD | 1,050.00 USD | `-20.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `233.50` | 183,550.00 USD | 0.00 USD | 389.48 USD | `-19.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `237.50` | 183,160.00 USD | 0.00 USD | 220.64 USD | `-17.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `238.50` | 182,940.00 USD | 0.00 USD | 429.30 USD | `-17.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `239.50` | 182,510.00 USD | 0.00 USD | 296.50 USD | `-16.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `240.50` | 182,210.00 USD | 0.00 USD | 216.45 USD | `-16.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `242.50` | 181,990.00 USD | 0.00 USD | 101.61 USD | `-15.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `244.50` | 181,890.00 USD | 0.00 USD | 366.75 USD | `-15.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `246.50` | 181,530.00 USD | 0.00 USD | 1,630.00 USD | `-14.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `249.50` | 179,900.00 USD | 0.00 USD | 2,940.00 USD | `-13.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `250.50` | 176,960.00 USD | 0.00 USD | 4,560.00 USD | `-13.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `251.50` | 172,400.00 USD | 0.00 USD | 7,080.00 USD | `-12.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `252.50` | 165,320.00 USD | 0.00 USD | 231.54 USD | `-12.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `253.50` | 165,090.00 USD | 0.00 USD | 109.26 USD | `-12.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `255.50` | 164,980.00 USD | 0.00 USD | 1,880.00 USD | `-11.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `256.50` | 163,100.00 USD | 0.00 USD | 51,300.00 USD | `-11.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `257.50` | 111,800.00 USD | 0.00 USD | 250.81 USD | `-10.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `259.50` | 111,550.00 USD | 0.00 USD | 386.14 USD | `-10.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `260.50` | 111,160.00 USD | 0.00 USD | 707.78 USD | `-9.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `262.50` | 110,450.00 USD | 0.00 USD | 857.85 USD | `-9.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `263.50` | 109,600.00 USD | 0.00 USD | 7,790.00 USD | `-8.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `264.50` | 101,800.00 USD | 0.00 USD | 122.99 USD | `-8.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `265.50` | 101,680.00 USD | 0.00 USD | 455.86 USD | `-7.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `266.50` | 101,220.00 USD | 0.00 USD | 10,490.00 USD | `-7.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `267.50` | 90,740.00 USD | 0.00 USD | 1,280.00 USD | `-7.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `268.50` | 89,460.00 USD | 0.00 USD | 9,310.00 USD | `-6.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `269.50` | 80,150.00 USD | 0.00 USD | 605.03 USD | `-6.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `270.50` | 79,540.00 USD | 0.00 USD | 1,180.00 USD | `-6.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `271.50` | 78,360.00 USD | 0.00 USD | 269.60 USD | `-5.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `272.50` | 78,090.00 USD | 0.00 USD | 13,500.00 USD | `-5.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `273.50` | 64,600.00 USD | 0.00 USD | 2,590.00 USD | `-5.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `274.50` | 62,000.00 USD | 0.00 USD | 336.54 USD | `-4.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `275.50` | 61,670.00 USD | 0.00 USD | 3,560.00 USD | `-4.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `276.50` | 58,110.00 USD | 0.00 USD | 105.35 USD | `-4.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `277.50` | 58,000.00 USD | 0.00 USD | 14,500.00 USD | `-3.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `278.50` | 43,500.00 USD | 0.00 USD | 125.88 USD | `-3.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `279.50` | 43,370.00 USD | 0.00 USD | 25,690.00 USD | `-3.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `280.50` | 17,680.00 USD | 0.00 USD | 3,480.00 USD | `-2.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `281.50` | 14,200.00 USD | 0.00 USD | 2,880.00 USD | `-2.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `282.50` | 11,320.00 USD | 0.00 USD | 3,930.00 USD | `-2.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `283.50` | 7,390.00 USD | 0.00 USD | 957.10 USD | `-1.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `284.50` | 6,430.00 USD | 0.00 USD | 644.96 USD | `-1.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `285.50` | 5,780.00 USD | 0.00 USD | 422.54 USD | `-1.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `286.50` | 5,360.00 USD | 0.00 USD | 5,080.00 USD | `-0.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `287.50` | 280.02 USD | 0.00 USD | 280.02 USD | `-0.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `288.50` | 120.59 USD | 120.59 USD | 0.00 USD | `+0.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `289.50` | 274.03 USD | 153.44 USD | 0.00 USD | `+0.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `290.50` | 1,590.00 USD | 1,320.00 USD | 0.00 USD | `+0.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `291.50` | 1,710.00 USD | 115.73 USD | 0.00 USD | `+1.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `292.50` | 2,120.00 USD | 409.21 USD | 0.00 USD | `+1.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `293.50` | 3,520.00 USD | 1,400.00 USD | 0.00 USD | `+1.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `294.50` | 3,930.00 USD | 412.01 USD | 0.00 USD | `+2.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `295.50` | 8,660.00 USD | 4,730.00 USD | 0.00 USD | `+2.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `296.50` | 9,240.00 USD | 581.14 USD | 0.00 USD | `+2.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `298.50` | 9,630.00 USD | 388.95 USD | 0.00 USD | `+3.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `300.50` | 19,320.00 USD | 9,690.00 USD | 0.00 USD | `+4.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `304.50` | 33,340.00 USD | 14,020.00 USD | 0.00 USD | `+5.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `305.50` | 35,990.00 USD | 2,650.00 USD | 0.00 USD | `+5.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `306.50` | 37,050.00 USD | 1,060.00 USD | 0.00 USD | `+6.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `308.50` | 37,150.00 USD | 102.73 USD | 0.00 USD | `+6.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `309.50` | 51,650.00 USD | 14,500.00 USD | 0.00 USD | `+7.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `310.50` | 52,280.00 USD | 634.04 USD | 0.00 USD | `+7.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `312.50` | 52,600.00 USD | 317.19 USD | 0.00 USD | `+8.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `316.50` | 53,630.00 USD | 1,030.00 USD | 0.00 USD | `+9.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `318.50` | 59,280.00 USD | 5,650.00 USD | 0.00 USD | `+10.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `319.50` | 59,400.00 USD | 118.85 USD | 0.00 USD | `+10.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `320.50` | 59,940.00 USD | 534.59 USD | 0.00 USD | `+11.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `321.50` | 60,260.00 USD | 321.50 USD | 0.00 USD | `+11.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `325.50` | 125,180.00 USD | 64,920.00 USD | 0.00 USD | `+12.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `340.50` | 125,730.00 USD | 547.52 USD | 0.00 USD | `+18.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `345.50` | 125,870.00 USD | 138.20 USD | 0.00 USD | `+19.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `348.50` | 126,040.00 USD | 174.25 USD | 0.00 USD | `+20.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `351.50` | 126,200.00 USD | 151.50 USD | 0.00 USD | `+21.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `357.50` | 127,650.00 USD | 1,450.00 USD | 0.00 USD | `+23.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `359.50` | 129,420.00 USD | 1,770.00 USD | 0.00 USD | `+24.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `361.50` | 129,750.00 USD | 326.07 USD | 0.00 USD | `+25.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `363.50` | 130,580.00 USD | 826.60 USD | 0.00 USD | `+26.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `364.50` | 134,300.00 USD | 3,730.00 USD | 0.00 USD | `+26.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `365.50` | 141,750.00 USD | 7,440.00 USD | 0.00 USD | `+26.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `369.50` | 142,430.00 USD | 682.84 USD | 0.00 USD | `+28.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `381.50` | 143,530.00 USD | 1,100.00 USD | 0.00 USD | `+32.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `396.50` | 144,210.00 USD | 683.96 USD | 0.00 USD | `+37.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `399.50` | 144,410.00 USD | 199.75 USD | 0.00 USD | `+38.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `400.50` | 147,910.00 USD | 3,500.00 USD | 0.00 USD | `+38.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `404.50` | 148,950.00 USD | 1,040.00 USD | 0.00 USD | `+40.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `405.50` | 149,330.00 USD | 376.71 USD | 0.00 USD | `+40.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `410.50` | 337,970.00 USD | 188,640.00 USD | 0.00 USD | `+42.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `415.50` | 343,870.00 USD | 5,900.00 USD | 0.00 USD | `+44.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `423.50` | 344,770.00 USD | 901.21 USD | 0.00 USD | `+46.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `425.50` | 352,580.00 USD | 7,800.00 USD | 0.00 USD | `+47.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `430.50` | 354,130.00 USD | 1,550.00 USD | 0.00 USD | `+49.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `435.50` | 355,510.00 USD | 1,380.00 USD | 0.00 USD | `+50.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `436.50` | 356,130.00 USD | 621.14 USD | 0.00 USD | `+51.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `440.50` | 359,510.00 USD | 3,380.00 USD | 0.00 USD | `+52.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `445.50` | 359,730.00 USD | 222.75 USD | 0.00 USD | `+54.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `450.50` | 365,330.00 USD | 5,590.00 USD | 0.00 USD | `+56.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `451.50` | 371,250.00 USD | 5,920.00 USD | 0.00 USD | `+56.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `460.50` | 372,370.00 USD | 1,130.00 USD | 0.00 USD | `+59.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `482.50` | 380,010.00 USD | 7,630.00 USD | 0.00 USD | `+67.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `487.50` | 478,480.00 USD | 98,470.00 USD | 0.00 USD | `+69.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `490.50` | 479,470.00 USD | 981.00 USD | 0.00 USD | `+70.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `499.50` | 479,960.00 USD | 499.50 USD | 0.00 USD | `+73.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `500.50` | 2,370,000.00 USD | 1,890,000.00 USD | 0.00 USD | `+73.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `501.50` | 2,370,000.00 USD | 1,000.00 USD | 0.00 USD | `+73.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `518.50` | 2,370,000.00 USD | 1,040.00 USD | 0.00 USD | `+79.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `522.50` | 2,370,000.00 USD | 340.67 USD | 0.00 USD | `+81.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `556.50` | 2,370,000.00 USD | 638.86 USD | 0.00 USD | `+92.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `575.50` | 2,370,000.00 USD | 2,590.00 USD | 0.00 USD | `+99.50%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `249.40` | 14,810,000.00 USD | 0.00 USD | 14,810,000.00 USD | 50,130.00 USD | 28,020.00 USD | 15,520.00 USD |
| `1D` | `249.80` | 5,070,000.00 USD | 0.00 USD | 5,070,000.00 USD | 10,830.00 USD | 1,230.00 USD | 3,490.00 USD |
| `7D` | `249.80` | 14,710,000.00 USD | 0.00 USD | 14,710,000.00 USD | 21,060.00 USD | 30,960.00 USD | 32,870.00 USD |
| `1D` | `250.10` | 5,060,000.00 USD | 0.00 USD | 5,060,000.00 USD | 7,770.00 USD | 47.40 USD | 1,920.00 USD |
| `7D` | `250.20` | 14,630,000.00 USD | 0.00 USD | 14,630,000.00 USD | 42,320.00 USD | 33,800.00 USD | 10,590.00 USD |
| `1D` | `250.40` | 5,050,000.00 USD | 0.00 USD | 5,050,000.00 USD | 4,180.00 USD | 2,430.00 USD | 1,340.00 USD |
| `7D` | `250.60` | 14,540,000.00 USD | 0.00 USD | 14,540,000.00 USD | 18,400.00 USD | 33,950.00 USD | 13,800.00 USD |
| `1D` | `250.70` | 5,040,000.00 USD | 0.00 USD | 5,040,000.00 USD | 3,620.00 USD | 9,520.00 USD | 1.83 USD |
| `1D` | `251.00` | 5,030,000.00 USD | 0.00 USD | 5,030,000.00 USD | 28,400.00 USD | 35,020.00 USD | 5,480.00 USD |
| `7D` | `251.00` | 14,480,000.00 USD | 0.00 USD | 14,480,000.00 USD | 42,670.00 USD | 45,820.00 USD | 13,880.00 USD |
| `1D` | `251.30` | 4,960,000.00 USD | 0.00 USD | 4,960,000.00 USD | 8,000.00 USD | 21,950.00 USD | 12,050.00 USD |
| `7D` | `251.40` | 14,370,000.00 USD | 0.00 USD | 14,370,000.00 USD | 10,060.00 USD | 69,300.00 USD | 22,210.00 USD |
| `1D` | `251.60` | 4,920,000.00 USD | 0.00 USD | 4,920,000.00 USD | 10,130.00 USD | 30,750.00 USD | 5,130.00 USD |
| `7D` | `251.80` | 14,270,000.00 USD | 0.00 USD | 14,270,000.00 USD | 55,620.00 USD | 45,720.00 USD | 35,820.00 USD |
| `1D` | `251.90` | 4,870,000.00 USD | 0.00 USD | 4,870,000.00 USD | 21,580.00 USD | 16,100.00 USD | 9,010.00 USD |
| `1D` | `252.20` | 4,820,000.00 USD | 0.00 USD | 4,820,000.00 USD | 9,410.00 USD | 7,370.00 USD | 5,650.00 USD |
| `7D` | `252.20` | 14,140,000.00 USD | 0.00 USD | 14,140,000.00 USD | 53,090.00 USD | 22,620.00 USD | 17,360.00 USD |
| `1D` | `252.50` | 4,800,000.00 USD | 0.00 USD | 4,800,000.00 USD | 186.30 USD | 92.40 USD | 0.00 USD |
| `7D` | `252.60` | 14,040,000.00 USD | 0.00 USD | 14,040,000.00 USD | 46,110.00 USD | 17,160.00 USD | 7,910.00 USD |
| `1D` | `252.80` | 4,800,000.00 USD | 0.00 USD | 4,800,000.00 USD | 11,380.00 USD | 5,970.00 USD | 2,180.00 USD |
| `7D` | `253.00` | 13,970,000.00 USD | 0.00 USD | 13,970,000.00 USD | 18,270.00 USD | 19,290.00 USD | 7.83 USD |
| `1D` | `253.10` | 4,780,000.00 USD | 0.00 USD | 4,780,000.00 USD | 5,420.00 USD | 11,520.00 USD | 796.24 USD |
| `1D` | `253.40` | 4,760,000.00 USD | 0.00 USD | 4,760,000.00 USD | 13,050.00 USD | 8,570.00 USD | 9,210.00 USD |
| `7D` | `253.40` | 13,930,000.00 USD | 0.00 USD | 13,930,000.00 USD | 25,510.00 USD | 49,680.00 USD | 50,850.00 USD |
| `1D` | `253.70` | 4,730,000.00 USD | 0.00 USD | 4,730,000.00 USD | 1,670.00 USD | 4,650.00 USD | 0.00 USD |
| `7D` | `253.80` | 13,810,000.00 USD | 0.00 USD | 13,810,000.00 USD | 4,550.00 USD | 19,600.00 USD | 4,000.00 USD |
| `1D` | `254.00` | 4,730,000.00 USD | 0.00 USD | 4,730,000.00 USD | 144.00 USD | 2,390.00 USD | 0.00 USD |
| `7D` | `254.20` | 13,780,000.00 USD | 0.00 USD | 13,780,000.00 USD | 38,950.00 USD | 38,390.00 USD | 25,760.00 USD |
| `1D` | `254.30` | 4,720,000.00 USD | 0.00 USD | 4,720,000.00 USD | 0.00 USD | 48.50 USD | 4,090.00 USD |
| `1D` | `254.60` | 4,720,000.00 USD | 0.00 USD | 4,720,000.00 USD | 173.42 USD | 2,050.00 USD | 8,550.00 USD |
| `7D` | `254.60` | 13,680,000.00 USD | 0.00 USD | 13,680,000.00 USD | 23,730.00 USD | 15,110.00 USD | 12,590.00 USD |
| `1D` | `254.90` | 4,710,000.00 USD | 0.00 USD | 4,710,000.00 USD | 17,900.00 USD | 189.05 USD | 9,750.00 USD |
| `7D` | `255.00` | 13,630,000.00 USD | 0.00 USD | 13,630,000.00 USD | 15,150.00 USD | 11,150.00 USD | 23,850.00 USD |
| `1D` | `255.20` | 4,680,000.00 USD | 0.00 USD | 4,680,000.00 USD | 2,810.00 USD | 0.00 USD | 1.53 USD |
| `7D` | `255.40` | 13,580,000.00 USD | 0.00 USD | 13,580,000.00 USD | 51,160.00 USD | 865.65 USD | 23,840.00 USD |
| `1D` | `255.50` | 4,680,000.00 USD | 0.00 USD | 4,680,000.00 USD | 5,490.00 USD | 194.85 USD | 5,900.00 USD |
| `1D` | `255.80` | 4,670,000.00 USD | 0.00 USD | 4,670,000.00 USD | 5,580.00 USD | 2,150.00 USD | 74.53 USD |
| `7D` | `255.80` | 13,500,000.00 USD | 0.00 USD | 13,500,000.00 USD | 16,010.00 USD | 13,040.00 USD | 49,720.00 USD |
| `1D` | `256.10` | 4,660,000.00 USD | 0.00 USD | 4,660,000.00 USD | 11,210.00 USD | 1,850.00 USD | 6,390.00 USD |
| `7D` | `256.20` | 13,420,000.00 USD | 0.00 USD | 13,420,000.00 USD | 72,170.00 USD | 38,920.00 USD | 29,750.00 USD |
| `1D` | `256.40` | 4,640,000.00 USD | 0.00 USD | 4,640,000.00 USD | 0.00 USD | 2,120.00 USD | 0.00 USD |
| `7D` | `256.60` | 13,280,000.00 USD | 0.00 USD | 13,280,000.00 USD | 20,630.00 USD | 7,850.00 USD | 12,190.00 USD |
| `1D` | `256.70` | 4,640,000.00 USD | 0.00 USD | 4,640,000.00 USD | 4,760.00 USD | 4,570.00 USD | 10,050.00 USD |
| `1D` | `257.00` | 4,620,000.00 USD | 0.00 USD | 4,620,000.00 USD | 4,410.00 USD | 12,310.00 USD | 3.61 USD |
| `7D` | `257.00` | 13,240,000.00 USD | 0.00 USD | 13,240,000.00 USD | 39,780.00 USD | 9,470.00 USD | 47,860.00 USD |
| `1D` | `257.30` | 4,600,000.00 USD | 0.00 USD | 4,600,000.00 USD | 113.97 USD | 5,250.00 USD | 0.90 USD |
| `7D` | `257.40` | 13,140,000.00 USD | 0.00 USD | 13,140,000.00 USD | 27,690.00 USD | 2,250.00 USD | 10.02 USD |
| `1D` | `257.60` | 4,600,000.00 USD | 0.00 USD | 4,600,000.00 USD | 479.45 USD | 0.00 USD | 0.00 USD |
| `7D` | `257.80` | 13,110,000.00 USD | 0.00 USD | 13,110,000.00 USD | 29,320.00 USD | 5,870.00 USD | 18,190.00 USD |
| `1D` | `257.90` | 4,600,000.00 USD | 0.00 USD | 4,600,000.00 USD | 3,740.00 USD | 847.00 USD | 12,070.00 USD |
| `1D` | `258.20` | 4,580,000.00 USD | 0.00 USD | 4,580,000.00 USD | 0.00 USD | 6,210.00 USD | 8,030.00 USD |
| `7D` | `258.20` | 13,060,000.00 USD | 0.00 USD | 13,060,000.00 USD | 107,190.00 USD | 47,210.00 USD | 18,210.00 USD |
| `1D` | `258.50` | 4,560,000.00 USD | 0.00 USD | 4,560,000.00 USD | 7,980.00 USD | 7,140.00 USD | 2.15 USD |
| `7D` | `258.60` | 12,890,000.00 USD | 0.00 USD | 12,890,000.00 USD | 74,820.00 USD | 7,510.00 USD | 20,990.00 USD |
| `1D` | `258.80` | 4,550,000.00 USD | 0.00 USD | 4,550,000.00 USD | 17,830.00 USD | 5,620.00 USD | 11,360.00 USD |
| `7D` | `259.00` | 12,780,000.00 USD | 0.00 USD | 12,780,000.00 USD | 21,380.00 USD | 14,730.00 USD | 42,370.00 USD |
| `1D` | `259.10` | 4,510,000.00 USD | 0.00 USD | 4,510,000.00 USD | 105.75 USD | 6,040.00 USD | 10,720.00 USD |
| `1D` | `259.40` | 4,500,000.00 USD | 0.00 USD | 4,500,000.00 USD | 2,660.00 USD | 31.48 USD | 3,360.00 USD |
| `7D` | `259.40` | 12,700,000.00 USD | 0.00 USD | 12,700,000.00 USD | 3,040.00 USD | 32,950.00 USD | 92.22 USD |
| `1D` | `259.70` | 4,490,000.00 USD | 0.00 USD | 4,490,000.00 USD | 17,120.00 USD | 13,310.00 USD | 3.21 USD |
| `7D` | `259.80` | 12,670,000.00 USD | 0.00 USD | 12,670,000.00 USD | 18,420.00 USD | 11,850.00 USD | 56.32 USD |
| `1D` | `260.00` | 4,460,000.00 USD | 0.00 USD | 4,460,000.00 USD | 1,340.00 USD | 4,650.00 USD | 9,890.00 USD |
| `7D` | `260.20` | 12,640,000.00 USD | 0.00 USD | 12,640,000.00 USD | 23,100.00 USD | 10,140.00 USD | 8,870.00 USD |
| `1D` | `260.30` | 4,450,000.00 USD | 0.00 USD | 4,450,000.00 USD | 2,410.00 USD | 8,120.00 USD | 820.48 USD |
| `1D` | `260.60` | 4,430,000.00 USD | 0.00 USD | 4,430,000.00 USD | 4,750.00 USD | 14,900.00 USD | 2.89 USD |
| `7D` | `260.60` | 12,600,000.00 USD | 0.00 USD | 12,600,000.00 USD | 5,710.00 USD | 40,460.00 USD | 14,130.00 USD |
| `1D` | `260.90` | 4,410,000.00 USD | 0.00 USD | 4,410,000.00 USD | 9,850.00 USD | 1,560.00 USD | 0.67 USD |
| `7D` | `261.00` | 12,540,000.00 USD | 0.00 USD | 12,540,000.00 USD | 7,110.00 USD | 20,590.00 USD | 16,040.00 USD |
| `1D` | `261.20` | 4,400,000.00 USD | 0.00 USD | 4,400,000.00 USD | 95.62 USD | 2,220.00 USD | 2,830.00 USD |
| `7D` | `261.40` | 12,490,000.00 USD | 0.00 USD | 12,490,000.00 USD | 15,870.00 USD | 25,100.00 USD | 2,470.00 USD |
| `1D` | `261.50` | 4,400,000.00 USD | 0.00 USD | 4,400,000.00 USD | 2,050.00 USD | 6,940.00 USD | 1,630.00 USD |
| `1D` | `261.80` | 4,390,000.00 USD | 0.00 USD | 4,390,000.00 USD | 10,920.00 USD | 4,220.00 USD | 4.82 USD |
| `7D` | `261.80` | 12,450,000.00 USD | 0.00 USD | 12,450,000.00 USD | 41,470.00 USD | 29,410.00 USD | 26,100.00 USD |
| `1D` | `262.10` | 4,370,000.00 USD | 0.00 USD | 4,370,000.00 USD | 556.87 USD | 6,260.00 USD | 2,590.00 USD |
| `7D` | `262.20` | 12,350,000.00 USD | 0.00 USD | 12,350,000.00 USD | 17,460.00 USD | 35,160.00 USD | 7,560.00 USD |
| `1D` | `262.40` | 4,360,000.00 USD | 0.00 USD | 4,360,000.00 USD | 6,980.00 USD | 3,770.00 USD | 0.00 USD |
| `7D` | `262.60` | 12,290,000.00 USD | 0.00 USD | 12,290,000.00 USD | 37,090.00 USD | 26,170.00 USD | 19,300.00 USD |
| `1D` | `262.70` | 4,350,000.00 USD | 0.00 USD | 4,350,000.00 USD | 0.00 USD | 1,220.00 USD | 1,390.00 USD |
| `1D` | `263.00` | 4,350,000.00 USD | 0.00 USD | 4,350,000.00 USD | 24.70 USD | 486.36 USD | 0.00 USD |
| `7D` | `263.00` | 12,210,000.00 USD | 0.00 USD | 12,210,000.00 USD | 82,070.00 USD | 46,390.00 USD | 39,220.00 USD |
| `1D` | `263.30` | 4,350,000.00 USD | 0.00 USD | 4,350,000.00 USD | 4,240.00 USD | 39.48 USD | 2,190.00 USD |
| `7D` | `263.40` | 12,040,000.00 USD | 0.00 USD | 12,040,000.00 USD | 96,280.00 USD | 32,090.00 USD | 32,340.00 USD |
| `1D` | `263.60` | 4,340,000.00 USD | 0.00 USD | 4,340,000.00 USD | 1,720.00 USD | 830.11 USD | 5.81 USD |
| `7D` | `263.80` | 11,880,000.00 USD | 0.00 USD | 11,880,000.00 USD | 304,420.00 USD | 100,810.00 USD | 57,890.00 USD |
| `1D` | `263.90` | 4,340,000.00 USD | 0.00 USD | 4,340,000.00 USD | 333.33 USD | 2,140.00 USD | 2,720.00 USD |
| `1D` | `264.20` | 4,330,000.00 USD | 0.00 USD | 4,330,000.00 USD | 7,740.00 USD | 566.30 USD | 1,780.00 USD |
| `7D` | `264.20` | 11,420,000.00 USD | 0.00 USD | 11,420,000.00 USD | 49,040.00 USD | 50,840.00 USD | 7,370.00 USD |
| `1D` | `264.50` | 4,320,000.00 USD | 0.00 USD | 4,320,000.00 USD | 2,160.00 USD | 99.53 USD | 36,600.00 USD |
| `7D` | `264.60` | 11,310,000.00 USD | 0.00 USD | 11,310,000.00 USD | 25,480.00 USD | 71,630.00 USD | 36,970.00 USD |
| `1D` | `264.80` | 4,290,000.00 USD | 0.00 USD | 4,290,000.00 USD | 28,200.00 USD | 777.03 USD | 15,630.00 USD |
| `7D` | `265.00` | 11,180,000.00 USD | 0.00 USD | 11,180,000.00 USD | 53,060.00 USD | 23,600.00 USD | 79,530.00 USD |
| `1D` | `265.10` | 4,240,000.00 USD | 0.00 USD | 4,240,000.00 USD | 19,700.00 USD | 8,450.00 USD | 10.14 USD |
| `1D` | `265.40` | 4,210,000.00 USD | 0.00 USD | 4,210,000.00 USD | 1,130.00 USD | 11,640.00 USD | 33,560.00 USD |
| `7D` | `265.40` | 11,020,000.00 USD | 0.00 USD | 11,020,000.00 USD | 133,460.00 USD | 54,660.00 USD | 91,640.00 USD |
| `1D` | `265.70` | 4,170,000.00 USD | 0.00 USD | 4,170,000.00 USD | 23,780.00 USD | 12,140.00 USD | 33,660.00 USD |
| `7D` | `265.80` | 10,740,000.00 USD | 0.00 USD | 10,740,000.00 USD | 50,530.00 USD | 93,230.00 USD | 28,830.00 USD |
| `1D` | `266.00` | 4,100,000.00 USD | 0.00 USD | 4,100,000.00 USD | 323.40 USD | 500.72 USD | 0.00 USD |
| `7D` | `266.20` | 10,570,000.00 USD | 0.00 USD | 10,570,000.00 USD | 168,970.00 USD | 158,090.00 USD | 68,240.00 USD |
| `1D` | `266.30` | 4,100,000.00 USD | 0.00 USD | 4,100,000.00 USD | 32,620.00 USD | 193.83 USD | 5,030.00 USD |
| `1D` | `266.60` | 4,060,000.00 USD | 0.00 USD | 4,060,000.00 USD | 14,610.00 USD | 3,250.00 USD | 3,710.00 USD |
| `7D` | `266.60` | 10,170,000.00 USD | 0.00 USD | 10,170,000.00 USD | 141,550.00 USD | 54,870.00 USD | 119,920.00 USD |
| `1D` | `266.90` | 4,040,000.00 USD | 0.00 USD | 4,040,000.00 USD | 23,980.00 USD | 6,460.00 USD | 6,760.00 USD |
| `7D` | `267.00` | 9,860,000.00 USD | 0.00 USD | 9,860,000.00 USD | 89,220.00 USD | 165,740.00 USD | 49,630.00 USD |
| `1D` | `267.20` | 4,000,000.00 USD | 0.00 USD | 4,000,000.00 USD | 6,240.00 USD | 130.70 USD | 3,340.00 USD |
| `7D` | `267.40` | 9,550,000.00 USD | 0.00 USD | 9,550,000.00 USD | 107,800.00 USD | 202,150.00 USD | 88,200.00 USD |
| `1D` | `267.50` | 3,990,000.00 USD | 0.00 USD | 3,990,000.00 USD | 11,990.00 USD | 26,360.00 USD | 46.69 USD |
| `1D` | `267.80` | 3,950,000.00 USD | 0.00 USD | 3,950,000.00 USD | 96,470.00 USD | 108,630.00 USD | 33,350.00 USD |
| `7D` | `267.80` | 9,150,000.00 USD | 0.00 USD | 9,150,000.00 USD | 179,590.00 USD | 209,540.00 USD | 94,090.00 USD |
| `1D` | `268.10` | 3,710,000.00 USD | 0.00 USD | 3,710,000.00 USD | 29,710.00 USD | 68,110.00 USD | 16,580.00 USD |
| `7D` | `268.20` | 8,670,000.00 USD | 0.00 USD | 8,670,000.00 USD | 124,430.00 USD | 247,680.00 USD | 84,790.00 USD |
| `1D` | `268.40` | 3,600,000.00 USD | 0.00 USD | 3,600,000.00 USD | 31,470.00 USD | 67,680.00 USD | 11,200.00 USD |
| `7D` | `268.60` | 8,210,000.00 USD | 0.00 USD | 8,210,000.00 USD | 175,020.00 USD | 137,470.00 USD | 50,840.00 USD |
| `1D` | `268.70` | 3,490,000.00 USD | 0.00 USD | 3,490,000.00 USD | 68,110.00 USD | 47,730.00 USD | 22,530.00 USD |
| `1D` | `269.00` | 3,350,000.00 USD | 0.00 USD | 3,350,000.00 USD | 34,110.00 USD | 21,820.00 USD | 16,400.00 USD |
| `7D` | `269.00` | 7,850,000.00 USD | 0.00 USD | 7,850,000.00 USD | 207,700.00 USD | 143,940.00 USD | 80,400.00 USD |
| `1D` | `269.30` | 3,280,000.00 USD | 0.00 USD | 3,280,000.00 USD | 4,290.00 USD | 3,900.00 USD | 0.00 USD |
| `7D` | `269.40` | 7,420,000.00 USD | 0.00 USD | 7,420,000.00 USD | 246,990.00 USD | 118,760.00 USD | 59,990.00 USD |
| `1D` | `269.60` | 3,270,000.00 USD | 0.00 USD | 3,270,000.00 USD | 22,180.00 USD | 20,470.00 USD | 1,640.00 USD |
| `7D` | `269.80` | 6,990,000.00 USD | 0.00 USD | 6,990,000.00 USD | 52,590.00 USD | 129,880.00 USD | 13,210.00 USD |
| `1D` | `269.90` | 3,220,000.00 USD | 0.00 USD | 3,220,000.00 USD | 25,660.00 USD | 25,330.00 USD | 11,350.00 USD |
| `1D` | `270.20` | 3,160,000.00 USD | 0.00 USD | 3,160,000.00 USD | 97,940.00 USD | 51,650.00 USD | 96,360.00 USD |
| `7D` | `270.20` | 6,800,000.00 USD | 0.00 USD | 6,800,000.00 USD | 140,940.00 USD | 137,560.00 USD | 147,130.00 USD |
| `1D` | `270.50` | 2,920,000.00 USD | 0.00 USD | 2,920,000.00 USD | 58,030.00 USD | 27,020.00 USD | 34,320.00 USD |
| `7D` | `270.60` | 6,370,000.00 USD | 0.00 USD | 6,370,000.00 USD | 240,990.00 USD | 153,950.00 USD | 182,640.00 USD |
| `1D` | `270.80` | 2,800,000.00 USD | 0.00 USD | 2,800,000.00 USD | 3,370.00 USD | 16,950.00 USD | 0.00 USD |
| `7D` | `271.00` | 5,790,000.00 USD | 0.00 USD | 5,790,000.00 USD | 197,440.00 USD | 99,980.00 USD | 67,740.00 USD |
| `1D` | `271.10` | 2,780,000.00 USD | 0.00 USD | 2,780,000.00 USD | 31,070.00 USD | 22,900.00 USD | 134,200.00 USD |
| `1D` | `271.40` | 2,590,000.00 USD | 0.00 USD | 2,590,000.00 USD | 28,220.00 USD | 23,780.00 USD | 10,220.00 USD |
| `7D` | `271.40` | 5,430,000.00 USD | 0.00 USD | 5,430,000.00 USD | 96,260.00 USD | 114,640.00 USD | 63,240.00 USD |
| `1D` | `271.70` | 2,530,000.00 USD | 0.00 USD | 2,530,000.00 USD | 40,350.00 USD | 18,860.00 USD | 35,790.00 USD |
| `7D` | `271.80` | 5,150,000.00 USD | 0.00 USD | 5,150,000.00 USD | 427,350.00 USD | 47,340.00 USD | 53,290.00 USD |
| `1D` | `272.00` | 2,430,000.00 USD | 0.00 USD | 2,430,000.00 USD | 87,430.00 USD | 15,560.00 USD | 32,720.00 USD |
| `7D` | `272.20` | 4,630,000.00 USD | 0.00 USD | 4,630,000.00 USD | 218,980.00 USD | 49,070.00 USD | 157,760.00 USD |
| `1D` | `272.30` | 2,300,000.00 USD | 0.00 USD | 2,300,000.00 USD | 49,280.00 USD | 228.77 USD | 9,620.00 USD |
| `1D` | `272.60` | 2,240,000.00 USD | 0.00 USD | 2,240,000.00 USD | 54,020.00 USD | 23,670.00 USD | 32,720.00 USD |
| `7D` | `272.60` | 4,200,000.00 USD | 0.00 USD | 4,200,000.00 USD | 139,010.00 USD | 196,770.00 USD | 30,450.00 USD |
| `1D` | `272.90` | 2,130,000.00 USD | 0.00 USD | 2,130,000.00 USD | 65,700.00 USD | 52,790.00 USD | 4.88 USD |
| `7D` | `273.00` | 3,830,000.00 USD | 0.00 USD | 3,830,000.00 USD | 211,830.00 USD | 189,410.00 USD | 123,670.00 USD |
| `1D` | `273.20` | 2,010,000.00 USD | 0.00 USD | 2,010,000.00 USD | 50,860.00 USD | 101,090.00 USD | 35,090.00 USD |
| `7D` | `273.40` | 3,310,000.00 USD | 0.00 USD | 3,310,000.00 USD | 199,880.00 USD | 303,570.00 USD | 142,390.00 USD |
| `1D` | `273.50` | 1,820,000.00 USD | 0.00 USD | 1,820,000.00 USD | 188,260.00 USD | 156,220.00 USD | 76,810.00 USD |
| `1D` | `273.80` | 1,400,000.00 USD | 0.00 USD | 1,400,000.00 USD | 44,050.00 USD | 184,350.00 USD | 45,090.00 USD |
| `7D` | `273.80` | 2,660,000.00 USD | 0.00 USD | 2,660,000.00 USD | 259,450.00 USD | 405,750.00 USD | 199,690.00 USD |
| `1D` | `274.10` | 1,130,000.00 USD | 0.00 USD | 1,130,000.00 USD | 109,520.00 USD | 152,730.00 USD | 37,400.00 USD |
| `7D` | `274.20` | 1,800,000.00 USD | 0.00 USD | 1,800,000.00 USD | 348,580.00 USD | 204,690.00 USD | 127,490.00 USD |
| `1D` | `274.40` | 826,260.00 USD | 0.00 USD | 826,260.00 USD | 147,600.00 USD | 84,390.00 USD | 52,490.00 USD |
| `7D` | `274.60` | 1,120,000.00 USD | 0.00 USD | 1,120,000.00 USD | 334,810.00 USD | 183,210.00 USD | 71,130.00 USD |
| `1D` | `274.70` | 541,780.00 USD | 0.00 USD | 541,780.00 USD | 33,340.00 USD | 23,030.00 USD | 35,230.00 USD |
| `1D` | `275.00` | 450,180.00 USD | 0.00 USD | 450,180.00 USD | 29,690.00 USD | 19,130.00 USD | 20,830.00 USD |
| `7D` | `275.00` | 527,720.00 USD | 0.00 USD | 527,720.00 USD | 180,050.00 USD | 99,570.00 USD | 34,620.00 USD |
| `1D` | `275.30` | 380,530.00 USD | 0.00 USD | 380,530.00 USD | 68,900.00 USD | 42,670.00 USD | 32,660.00 USD |
| `7D` | `275.40` | 213,480.00 USD | 0.00 USD | 213,480.00 USD | 1,240.00 USD | 126,890.00 USD | 9,040.00 USD |
| `1D` | `275.60` | 236,310.00 USD | 0.00 USD | 236,310.00 USD | 11,630.00 USD | 37,380.00 USD | 8,730.00 USD |
| `7D` | `275.80` | 76,310.00 USD | 0.00 USD | 76,310.00 USD | 1,090.00 USD | 25,250.00 USD | 65.70 USD |
| `1D` | `275.90` | 178,560.00 USD | 0.00 USD | 178,560.00 USD | 31,610.00 USD | 11,430.00 USD | 8,060.00 USD |
| `1D` | `276.20` | 127,460.00 USD | 0.00 USD | 127,460.00 USD | 35,160.00 USD | 21,250.00 USD | 3,230.00 USD |
| `7D` | `276.20` | 49,900.00 USD | 0.00 USD | 49,900.00 USD | 2,660.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `276.50` | 67,820.00 USD | 0.00 USD | 67,820.00 USD | 79.10 USD | 13,020.00 USD | 0.00 USD |
| `7D` | `276.60` | 47,230.00 USD | 0.00 USD | 47,230.00 USD | 485.90 USD | 233.30 USD | 0.00 USD |
| `7D` | `277.00` | 46,510.00 USD | 0.00 USD | 46,510.00 USD | 883.77 USD | 0.00 USD | 0.00 USD |
| `1D` | `277.10` | 54,720.00 USD | 0.00 USD | 54,720.00 USD | 0.00 USD | 38,970.00 USD | 0.00 USD |
| `1D` | `277.40` | 15,760.00 USD | 0.00 USD | 15,760.00 USD | 0.00 USD | 15,750.00 USD | 0.00 USD |
| `7D` | `277.40` | 45,630.00 USD | 0.00 USD | 45,630.00 USD | 0.00 USD | 44,640.00 USD | 0.00 USD |
| `1D` | `278.00` | 4.50 USD | 0.00 USD | 4.50 USD | 0.00 USD | 0.00 USD | 4.50 USD |
| `7D` | `278.60` | 992.27 USD | 0.00 USD | 992.27 USD | 0.00 USD | 0.00 USD | 9.96 USD |
| `7D` | `279.00` | 982.31 USD | 0.00 USD | 982.31 USD | 0.00 USD | 933.19 USD | 49.12 USD |
| `7D` | `279.80` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `279.90` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `280.60` | 66,170.00 USD | 66,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 66,170.00 USD |
| `1D` | `280.70` | 46,700.00 USD | 46,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 46,700.00 USD |
| `7D` | `281.40` | 66,770.00 USD | 66,770.00 USD | 0.00 USD | 565.82 USD | 0.00 USD | 33.20 USD |
| `7D` | `281.80` | 438,830.00 USD | 438,830.00 USD | 0.00 USD | 107,230.00 USD | 43,540.00 USD | 221,290.00 USD |
| `1D` | `281.90` | 113,590.00 USD | 113,590.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 66,890.00 USD |
| `1D` | `282.20` | 316,880.00 USD | 316,880.00 USD | 0.00 USD | 30,440.00 USD | 46,080.00 USD | 126,780.00 USD |
| `7D` | `282.20` | 525,110.00 USD | 525,110.00 USD | 0.00 USD | 0.00 USD | 51,480.00 USD | 34,800.00 USD |
| `1D` | `282.50` | 361,330.00 USD | 361,330.00 USD | 0.00 USD | 16,460.00 USD | 13,450.00 USD | 14,540.00 USD |
| `7D` | `282.60` | 608,120.00 USD | 608,120.00 USD | 0.00 USD | 83,010.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `282.80` | 482,170.00 USD | 482,170.00 USD | 0.00 USD | 101,550.00 USD | 9,800.00 USD | 9,490.00 USD |
| `1D` | `283.10` | 607,800.00 USD | 607,800.00 USD | 0.00 USD | 57,750.00 USD | 14,850.00 USD | 53,030.00 USD |
| `1D` | `283.40` | 665,870.00 USD | 665,870.00 USD | 0.00 USD | 19,130.00 USD | 5,990.00 USD | 32,960.00 USD |
| `7D` | `283.40` | 794,200.00 USD | 794,200.00 USD | 0.00 USD | 47,330.00 USD | 49,490.00 USD | 89,260.00 USD |
| `1D` | `283.70` | 808,760.00 USD | 808,760.00 USD | 0.00 USD | 117,870.00 USD | 11,490.00 USD | 13,520.00 USD |
| `7D` | `283.80` | 967,440.00 USD | 967,440.00 USD | 0.00 USD | 13,900.00 USD | 80,650.00 USD | 78,690.00 USD |
| `1D` | `284.00` | 883,370.00 USD | 883,370.00 USD | 0.00 USD | 28,000.00 USD | 21,660.00 USD | 24,950.00 USD |
| `7D` | `284.20` | 1,090,000.00 USD | 1,090,000.00 USD | 0.00 USD | 60,830.00 USD | 56,980.00 USD | 8,610.00 USD |
| `1D` | `284.30` | 972,270.00 USD | 972,270.00 USD | 0.00 USD | 22,210.00 USD | 57,290.00 USD | 9,410.00 USD |
| `1D` | `284.60` | 1,390,000.00 USD | 1,390,000.00 USD | 0.00 USD | 170,510.00 USD | 189,320.00 USD | 59,680.00 USD |
| `7D` | `284.60` | 1,420,000.00 USD | 1,420,000.00 USD | 0.00 USD | 71,990.00 USD | 191,100.00 USD | 64,370.00 USD |
| `1D` | `284.90` | 1,620,000.00 USD | 1,620,000.00 USD | 0.00 USD | 58,130.00 USD | 138,810.00 USD | 33,160.00 USD |
| `7D` | `285.00` | 1,680,000.00 USD | 1,680,000.00 USD | 0.00 USD | 101,800.00 USD | 136,560.00 USD | 16,680.00 USD |
| `1D` | `285.20` | 1,850,000.00 USD | 1,850,000.00 USD | 0.00 USD | 62,110.00 USD | 135,170.00 USD | 35,360.00 USD |
| `7D` | `285.40` | 1,890,000.00 USD | 1,890,000.00 USD | 0.00 USD | 0.00 USD | 173,140.00 USD | 41,910.00 USD |
| `1D` | `285.50` | 2,130,000.00 USD | 2,130,000.00 USD | 0.00 USD | 135,460.00 USD | 95,280.00 USD | 45,030.00 USD |
| `1D` | `285.80` | 2,270,000.00 USD | 2,270,000.00 USD | 0.00 USD | 67,030.00 USD | 42,840.00 USD | 32,710.00 USD |
| `7D` | `285.80` | 2,080,000.00 USD | 2,080,000.00 USD | 0.00 USD | 87,960.00 USD | 97,960.00 USD | 0.00 USD |
| `1D` | `286.10` | 2,290,000.00 USD | 2,290,000.00 USD | 0.00 USD | 8,520.00 USD | 7,060.00 USD | 0.00 USD |
| `7D` | `286.20` | 2,120,000.00 USD | 2,120,000.00 USD | 0.00 USD | 0.00 USD | 40,670.00 USD | 0.00 USD |
| `1D` | `286.40` | 2,370,000.00 USD | 2,370,000.00 USD | 0.00 USD | 42,610.00 USD | 40,040.00 USD | 3,280.00 USD |
| `7D` | `286.60` | 2,270,000.00 USD | 2,270,000.00 USD | 0.00 USD | 23,860.00 USD | 121,370.00 USD | 8,970.00 USD |
| `1D` | `286.70` | 2,590,000.00 USD | 2,590,000.00 USD | 0.00 USD | 103,130.00 USD | 50,280.00 USD | 59,280.00 USD |
| `1D` | `287.00` | 2,820,000.00 USD | 2,820,000.00 USD | 0.00 USD | 77,890.00 USD | 93,350.00 USD | 56,770.00 USD |
| `7D` | `287.00` | 2,510,000.00 USD | 2,510,000.00 USD | 0.00 USD | 27,530.00 USD | 115,360.00 USD | 96,530.00 USD |
| `1D` | `287.30` | 2,910,000.00 USD | 2,910,000.00 USD | 0.00 USD | 61,620.00 USD | 28,670.00 USD | 7,780.00 USD |
| `7D` | `287.40` | 2,690,000.00 USD | 2,690,000.00 USD | 0.00 USD | 77,180.00 USD | 102,270.00 USD | 0.00 USD |
| `1D` | `287.60` | 3,000,000.00 USD | 3,000,000.00 USD | 0.00 USD | 5,760.00 USD | 46,520.00 USD | 36,680.00 USD |
| `7D` | `287.80` | 2,940,000.00 USD | 2,940,000.00 USD | 0.00 USD | 0.00 USD | 244,170.00 USD | 0.00 USD |
| `1D` | `287.90` | 3,110,000.00 USD | 3,110,000.00 USD | 0.00 USD | 53,720.00 USD | 18,140.00 USD | 33,650.00 USD |
| `7D` | `288.20` | 3,050,000.00 USD | 3,050,000.00 USD | 0.00 USD | 41,500.00 USD | 75,540.00 USD | 0.00 USD |
| `1D` | `288.50` | 3,160,000.00 USD | 3,160,000.00 USD | 0.00 USD | 32,470.00 USD | 10,250.00 USD | 5,010.00 USD |
| `7D` | `288.60` | 3,150,000.00 USD | 3,150,000.00 USD | 0.00 USD | 0.00 USD | 58,240.00 USD | 35,560.00 USD |
| `1D` | `288.80` | 3,190,000.00 USD | 3,190,000.00 USD | 0.00 USD | 14,190.00 USD | 3,000.00 USD | 17,530.00 USD |
| `7D` | `289.00` | 3,180,000.00 USD | 3,180,000.00 USD | 0.00 USD | 23,660.00 USD | 6,610.00 USD | 0.00 USD |
| `1D` | `289.10` | 3,250,000.00 USD | 3,250,000.00 USD | 0.00 USD | 36,020.00 USD | 12,850.00 USD | 6,760.00 USD |
| `1D` | `289.40` | 3,250,000.00 USD | 3,250,000.00 USD | 0.00 USD | 5,830.00 USD | 0.00 USD | 3,340.00 USD |
| `7D` | `289.40` | 3,240,000.00 USD | 3,240,000.00 USD | 0.00 USD | 46,870.00 USD | 14,830.00 USD | 4,230.00 USD |
| `1D` | `289.70` | 3,300,000.00 USD | 3,300,000.00 USD | 0.00 USD | 11,630.00 USD | 36,980.00 USD | 1.20 USD |
| `7D` | `289.80` | 3,270,000.00 USD | 3,270,000.00 USD | 0.00 USD | 18,500.00 USD | 947.00 USD | 4,310.00 USD |
| `1D` | `290.00` | 3,460,000.00 USD | 3,460,000.00 USD | 0.00 USD | 102,350.00 USD | 44,320.00 USD | 9,560.00 USD |
| `7D` | `290.20` | 3,620,000.00 USD | 3,620,000.00 USD | 0.00 USD | 146,360.00 USD | 173,970.00 USD | 32,180.00 USD |
| `1D` | `290.30` | 3,740,000.00 USD | 3,740,000.00 USD | 0.00 USD | 119,420.00 USD | 91,590.00 USD | 67,720.00 USD |
| `1D` | `290.60` | 3,850,000.00 USD | 3,850,000.00 USD | 0.00 USD | 12,690.00 USD | 96,190.00 USD | 6,500.00 USD |
| `7D` | `290.60` | 3,810,000.00 USD | 3,810,000.00 USD | 0.00 USD | 50,900.00 USD | 127,830.00 USD | 8,340.00 USD |
| `1D` | `290.90` | 4,030,000.00 USD | 4,030,000.00 USD | 0.00 USD | 81,620.00 USD | 79,980.00 USD | 15,700.00 USD |
| `7D` | `291.00` | 4,020,000.00 USD | 4,020,000.00 USD | 0.00 USD | 62,080.00 USD | 127,160.00 USD | 20,930.00 USD |
| `1D` | `291.20` | 4,260,000.00 USD | 4,260,000.00 USD | 0.00 USD | 107,540.00 USD | 106,130.00 USD | 19,540.00 USD |
| `7D` | `291.40` | 4,170,000.00 USD | 4,170,000.00 USD | 0.00 USD | 73,050.00 USD | 78,370.00 USD | 69.78 USD |
| `1D` | `291.50` | 4,340,000.00 USD | 4,340,000.00 USD | 0.00 USD | 28,700.00 USD | 39,010.00 USD | 12,910.00 USD |
| `1D` | `291.80` | 4,370,000.00 USD | 4,370,000.00 USD | 0.00 USD | 8,030.00 USD | 5,910.00 USD | 9,490.00 USD |
| `7D` | `291.80` | 4,320,000.00 USD | 4,320,000.00 USD | 0.00 USD | 32,220.00 USD | 119,880.00 USD | 33.90 USD |
| `1D` | `292.10` | 4,520,000.00 USD | 4,520,000.00 USD | 0.00 USD | 63,210.00 USD | 36,070.00 USD | 50,270.00 USD |
| `7D` | `292.20` | 4,490,000.00 USD | 4,490,000.00 USD | 0.00 USD | 110,850.00 USD | 59,290.00 USD | 4,530.00 USD |
| `1D` | `292.40` | 4,640,000.00 USD | 4,640,000.00 USD | 0.00 USD | 20,320.00 USD | 31,270.00 USD | 75,150.00 USD |
| `7D` | `292.60` | 4,600,000.00 USD | 4,600,000.00 USD | 0.00 USD | 34,100.00 USD | 26,820.00 USD | 45,930.00 USD |
| `1D` | `292.70` | 4,790,000.00 USD | 4,790,000.00 USD | 0.00 USD | 33,180.00 USD | 75,500.00 USD | 37,280.00 USD |
| `1D` | `293.00` | 4,970,000.00 USD | 4,970,000.00 USD | 0.00 USD | 113,850.00 USD | 39,090.00 USD | 29,460.00 USD |
| `7D` | `293.00` | 5,030,000.00 USD | 5,030,000.00 USD | 0.00 USD | 229,100.00 USD | 150,380.00 USD | 47,160.00 USD |
| `1D` | `293.30` | 5,120,000.00 USD | 5,120,000.00 USD | 0.00 USD | 40,580.00 USD | 54,940.00 USD | 49,820.00 USD |
| `7D` | `293.40` | 5,370,000.00 USD | 5,370,000.00 USD | 0.00 USD | 78,760.00 USD | 67,380.00 USD | 199,530.00 USD |
| `1D` | `293.60` | 5,240,000.00 USD | 5,240,000.00 USD | 0.00 USD | 41,540.00 USD | 28,650.00 USD | 55,700.00 USD |
| `7D` | `293.80` | 5,410,000.00 USD | 5,410,000.00 USD | 0.00 USD | 37,280.00 USD | 1,170.00 USD | 116.86 USD |
| `1D` | `293.90` | 5,300,000.00 USD | 5,300,000.00 USD | 0.00 USD | 8,360.00 USD | 23,960.00 USD | 19,090.00 USD |
| `1D` | `294.20` | 5,400,000.00 USD | 5,400,000.00 USD | 0.00 USD | 26,380.00 USD | 41,970.00 USD | 36,910.00 USD |
| `7D` | `294.20` | 5,610,000.00 USD | 5,610,000.00 USD | 0.00 USD | 107,580.00 USD | 22,110.00 USD | 66,000.00 USD |
| `1D` | `294.50` | 5,610,000.00 USD | 5,610,000.00 USD | 0.00 USD | 130,280.00 USD | 57,150.00 USD | 26,570.00 USD |
| `7D` | `294.60` | 5,610,000.00 USD | 5,610,000.00 USD | 0.00 USD | 2,110.00 USD | 3,950.00 USD | 0.00 USD |
| `1D` | `294.80` | 5,770,000.00 USD | 5,770,000.00 USD | 0.00 USD | 19,780.00 USD | 63,490.00 USD | 70,850.00 USD |
| `7D` | `295.00` | 5,830,000.00 USD | 5,830,000.00 USD | 0.00 USD | 62,390.00 USD | 52,950.00 USD | 104,870.00 USD |
| `1D` | `295.10` | 5,820,000.00 USD | 5,820,000.00 USD | 0.00 USD | 19,100.00 USD | 31,970.00 USD | 4,100.00 USD |
| `1D` | `295.40` | 6,020,000.00 USD | 6,020,000.00 USD | 0.00 USD | 89,360.00 USD | 80,620.00 USD | 22,040.00 USD |
| `7D` | `295.40` | 6,100,000.00 USD | 6,100,000.00 USD | 0.00 USD | 92,780.00 USD | 94,780.00 USD | 83,510.00 USD |
| `1D` | `295.70` | 6,140,000.00 USD | 6,140,000.00 USD | 0.00 USD | 89,710.00 USD | 13,280.00 USD | 18,270.00 USD |
| `7D` | `295.80` | 6,200,000.00 USD | 6,200,000.00 USD | 0.00 USD | 34,250.00 USD | 30,180.00 USD | 31,980.00 USD |
| `1D` | `296.00` | 6,240,000.00 USD | 6,240,000.00 USD | 0.00 USD | 32,780.00 USD | 39,150.00 USD | 30,110.00 USD |
| `7D` | `296.20` | 6,270,000.00 USD | 6,270,000.00 USD | 0.00 USD | 0.00 USD | 744.75 USD | 67,350.00 USD |
| `1D` | `296.30` | 6,300,000.00 USD | 6,300,000.00 USD | 0.00 USD | 18,360.00 USD | 33,370.00 USD | 13,350.00 USD |
| `1D` | `296.60` | 6,410,000.00 USD | 6,410,000.00 USD | 0.00 USD | 36,570.00 USD | 38,050.00 USD | 34,560.00 USD |
| `7D` | `296.60` | 6,350,000.00 USD | 6,350,000.00 USD | 0.00 USD | 32,100.00 USD | 14,060.00 USD | 29,840.00 USD |
| `1D` | `296.90` | 6,560,000.00 USD | 6,560,000.00 USD | 0.00 USD | 53,630.00 USD | 75,460.00 USD | 18,960.00 USD |
| `7D` | `297.00` | 6,540,000.00 USD | 6,540,000.00 USD | 0.00 USD | 89,750.00 USD | 51,270.00 USD | 51,390.00 USD |
| `1D` | `297.20` | 6,600,000.00 USD | 6,600,000.00 USD | 0.00 USD | 7,110.00 USD | 13,140.00 USD | 13,420.00 USD |
| `7D` | `297.40` | 6,630,000.00 USD | 6,630,000.00 USD | 0.00 USD | 3,560.00 USD | 58,390.00 USD | 34,710.00 USD |
| `1D` | `297.50` | 6,660,000.00 USD | 6,660,000.00 USD | 0.00 USD | 34,110.00 USD | 18,960.00 USD | 9,430.00 USD |
| `1D` | `297.80` | 6,670,000.00 USD | 6,670,000.00 USD | 0.00 USD | 5,570.00 USD | 3,210.00 USD | 6,920.00 USD |
| `7D` | `297.80` | 6,750,000.00 USD | 6,750,000.00 USD | 0.00 USD | 16,080.00 USD | 39,720.00 USD | 54,850.00 USD |
| `1D` | `298.10` | 6,730,000.00 USD | 6,730,000.00 USD | 0.00 USD | 16,550.00 USD | 4,760.00 USD | 39,750.00 USD |
| `7D` | `298.20` | 6,830,000.00 USD | 6,830,000.00 USD | 0.00 USD | 32,390.00 USD | 40,760.00 USD | 16,600.00 USD |
| `1D` | `298.40` | 6,810,000.00 USD | 6,810,000.00 USD | 0.00 USD | 22,430.00 USD | 15,590.00 USD | 39,410.00 USD |
| `7D` | `298.60` | 6,850,000.00 USD | 6,850,000.00 USD | 0.00 USD | 0.00 USD | 12,430.00 USD | 114.26 USD |
| `1D` | `298.70` | 6,880,000.00 USD | 6,880,000.00 USD | 0.00 USD | 43,790.00 USD | 21,330.00 USD | 5,670.00 USD |
| `1D` | `299.00` | 6,980,000.00 USD | 6,980,000.00 USD | 0.00 USD | 37,310.00 USD | 19,100.00 USD | 36,900.00 USD |
| `7D` | `299.00` | 6,960,000.00 USD | 6,960,000.00 USD | 0.00 USD | 70,090.00 USD | 993.25 USD | 39,940.00 USD |
| `1D` | `299.30` | 7,090,000.00 USD | 7,090,000.00 USD | 0.00 USD | 39,150.00 USD | 25,770.00 USD | 50,280.00 USD |
| `7D` | `299.40` | 7,010,000.00 USD | 7,010,000.00 USD | 0.00 USD | 3,200.00 USD | 1,150.00 USD | 45,890.00 USD |
| `1D` | `299.60` | 7,160,000.00 USD | 7,160,000.00 USD | 0.00 USD | 34,750.00 USD | 26,920.00 USD | 9,030.00 USD |
| `7D` | `299.80` | 7,020,000.00 USD | 7,020,000.00 USD | 0.00 USD | 5,060.00 USD | 7,930.00 USD | 0.00 USD |
| `1D` | `299.90` | 7,200,000.00 USD | 7,200,000.00 USD | 0.00 USD | 13,590.00 USD | 20,510.00 USD | 5,090.00 USD |
| `1D` | `300.20` | 7,280,000.00 USD | 7,280,000.00 USD | 0.00 USD | 52,870.00 USD | 23,950.00 USD | 1,100.00 USD |
| `7D` | `300.20` | 7,060,000.00 USD | 7,060,000.00 USD | 0.00 USD | 35,320.00 USD | 2,260.00 USD | 0.00 USD |
| `1D` | `300.50` | 7,320,000.00 USD | 7,320,000.00 USD | 0.00 USD | 1,050.00 USD | 10,730.00 USD | 24,710.00 USD |
| `7D` | `300.60` | 7,150,000.00 USD | 7,150,000.00 USD | 0.00 USD | 23,830.00 USD | 52,200.00 USD | 19,730.00 USD |
| `1D` | `300.80` | 7,370,000.00 USD | 7,370,000.00 USD | 0.00 USD | 11,300.00 USD | 27,110.00 USD | 12,770.00 USD |
| `7D` | `301.00` | 7,190,000.00 USD | 7,190,000.00 USD | 0.00 USD | 0.00 USD | 31,740.00 USD | 0.00 USD |
| `1D` | `301.10` | 7,420,000.00 USD | 7,420,000.00 USD | 0.00 USD | 35,650.00 USD | 18,740.00 USD | 55.50 USD |
| `1D` | `301.40` | 7,470,000.00 USD | 7,470,000.00 USD | 0.00 USD | 11,900.00 USD | 27,210.00 USD | 9,170.00 USD |
| `7D` | `301.40` | 7,290,000.00 USD | 7,290,000.00 USD | 0.00 USD | 46,390.00 USD | 23,180.00 USD | 35,310.00 USD |
| `1D` | `301.70` | 7,500,000.00 USD | 7,500,000.00 USD | 0.00 USD | 12,880.00 USD | 13,140.00 USD | 7,070.00 USD |
| `7D` | `301.80` | 7,460,000.00 USD | 7,460,000.00 USD | 0.00 USD | 76,230.00 USD | 85,660.00 USD | 9,150.00 USD |
| `1D` | `302.00` | 7,540,000.00 USD | 7,540,000.00 USD | 0.00 USD | 19,690.00 USD | 14,190.00 USD | 4,050.00 USD |
| `7D` | `302.20` | 7,590,000.00 USD | 7,590,000.00 USD | 0.00 USD | 1,160.00 USD | 124,660.00 USD | 2.49 USD |
| `1D` | `302.30` | 7,570,000.00 USD | 7,570,000.00 USD | 0.00 USD | 9,030.00 USD | 14,010.00 USD | 1,280.00 USD |
| `1D` | `302.60` | 7,610,000.00 USD | 7,610,000.00 USD | 0.00 USD | 17,830.00 USD | 19,990.00 USD | 6,540.00 USD |
| `7D` | `302.60` | 7,660,000.00 USD | 7,660,000.00 USD | 0.00 USD | 2,480.00 USD | 71,350.00 USD | 109.38 USD |
| `1D` | `302.90` | 7,610,000.00 USD | 7,610,000.00 USD | 0.00 USD | 286.84 USD | 1,090.00 USD | 2.41 USD |
| `7D` | `303.00` | 7,760,000.00 USD | 7,760,000.00 USD | 0.00 USD | 37,510.00 USD | 63,670.00 USD | 191.68 USD |
| `1D` | `303.20` | 7,640,000.00 USD | 7,640,000.00 USD | 0.00 USD | 11,620.00 USD | 263.67 USD | 14,760.00 USD |
| `7D` | `303.40` | 7,760,000.00 USD | 7,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 33.35 USD |
| `1D` | `303.50` | 7,670,000.00 USD | 7,670,000.00 USD | 0.00 USD | 17,870.00 USD | 9,140.00 USD | 6,250.00 USD |
| `1D` | `303.80` | 7,690,000.00 USD | 7,690,000.00 USD | 0.00 USD | 8,040.00 USD | 3,510.00 USD | 3,460.00 USD |
| `7D` | `303.80` | 7,820,000.00 USD | 7,820,000.00 USD | 0.00 USD | 20,720.00 USD | 9,650.00 USD | 24,710.00 USD |
| `1D` | `304.10` | 7,720,000.00 USD | 7,720,000.00 USD | 0.00 USD | 11,280.00 USD | 1,100.00 USD | 18,440.00 USD |
| `7D` | `304.20` | 7,820,000.00 USD | 7,820,000.00 USD | 0.00 USD | 1,670.00 USD | 839.60 USD | 86.46 USD |
| `1D` | `304.40` | 7,760,000.00 USD | 7,760,000.00 USD | 0.00 USD | 14,550.00 USD | 11,300.00 USD | 18,460.00 USD |
| `7D` | `304.60` | 7,840,000.00 USD | 7,840,000.00 USD | 0.00 USD | 2,960.00 USD | 11,330.00 USD | 72.30 USD |
| `1D` | `304.70` | 7,760,000.00 USD | 7,760,000.00 USD | 0.00 USD | 83.90 USD | 318.60 USD | 0.93 USD |
| `1D` | `305.00` | 7,790,000.00 USD | 7,790,000.00 USD | 0.00 USD | 9,110.00 USD | 6,650.00 USD | 8,060.00 USD |
| `7D` | `305.00` | 8,060,000.00 USD | 8,060,000.00 USD | 0.00 USD | 95,550.00 USD | 73,310.00 USD | 58,540.00 USD |
| `1D` | `305.30` | 7,830,000.00 USD | 7,830,000.00 USD | 0.00 USD | 27,840.00 USD | 7,500.00 USD | 5,160.00 USD |
| `7D` | `305.40` | 8,320,000.00 USD | 8,320,000.00 USD | 0.00 USD | 102,210.00 USD | 76,550.00 USD | 73,740.00 USD |
| `1D` | `305.60` | 7,840,000.00 USD | 7,840,000.00 USD | 0.00 USD | 6,180.00 USD | 3,220.00 USD | 3,780.00 USD |
| `7D` | `305.80` | 8,460,000.00 USD | 8,460,000.00 USD | 0.00 USD | 80,350.00 USD | 49,520.00 USD | 10,620.00 USD |
| `1D` | `305.90` | 7,860,000.00 USD | 7,860,000.00 USD | 0.00 USD | 14,420.00 USD | 2,580.00 USD | 1,970.00 USD |
| `1D` | `306.20` | 7,870,000.00 USD | 7,870,000.00 USD | 0.00 USD | 3,720.00 USD | 3,290.00 USD | 1,360.00 USD |
| `7D` | `306.20` | 8,590,000.00 USD | 8,590,000.00 USD | 0.00 USD | 30,620.00 USD | 52,500.00 USD | 46,040.00 USD |
| `1D` | `306.50` | 7,870,000.00 USD | 7,870,000.00 USD | 0.00 USD | 431.00 USD | 6,700.00 USD | 1.52 USD |
| `7D` | `306.60` | 8,700,000.00 USD | 8,700,000.00 USD | 0.00 USD | 25,430.00 USD | 23,280.00 USD | 65,860.00 USD |
| `1D` | `306.80` | 7,940,000.00 USD | 7,940,000.00 USD | 0.00 USD | 28,600.00 USD | 35,110.00 USD | 5,480.00 USD |
| `7D` | `307.00` | 8,940,000.00 USD | 8,940,000.00 USD | 0.00 USD | 61,110.00 USD | 73,890.00 USD | 102,380.00 USD |
| `1D` | `307.10` | 7,980,000.00 USD | 7,980,000.00 USD | 0.00 USD | 8,400.00 USD | 22,000.00 USD | 12,050.00 USD |
| `1D` | `307.40` | 8,000,000.00 USD | 8,000,000.00 USD | 0.00 USD | 259.96 USD | 17,400.00 USD | 1,820.00 USD |
| `7D` | `307.40` | 9,150,000.00 USD | 9,150,000.00 USD | 0.00 USD | 47,700.00 USD | 131,290.00 USD | 38,470.00 USD |
| `1D` | `307.70` | 8,050,000.00 USD | 8,050,000.00 USD | 0.00 USD | 15,390.00 USD | 22,570.00 USD | 5,880.00 USD |
| `7D` | `307.80` | 9,380,000.00 USD | 9,380,000.00 USD | 0.00 USD | 88,520.00 USD | 81,640.00 USD | 57,870.00 USD |
| `1D` | `308.00` | 8,090,000.00 USD | 8,090,000.00 USD | 0.00 USD | 21,620.00 USD | 11,290.00 USD | 7,820.00 USD |
| `7D` | `308.20` | 9,700,000.00 USD | 9,700,000.00 USD | 0.00 USD | 152,190.00 USD | 52,080.00 USD | 114,230.00 USD |
| `1D` | `308.30` | 8,100,000.00 USD | 8,100,000.00 USD | 0.00 USD | 4,640.00 USD | 3,360.00 USD | 4,260.00 USD |
| `7D` | `308.60` | 9,810,000.00 USD | 9,810,000.00 USD | 0.00 USD | 67,700.00 USD | 37,160.00 USD | 8,020.00 USD |
| `7D` | `309.00` | 9,890,000.00 USD | 9,890,000.00 USD | 0.00 USD | 26,920.00 USD | 31,940.00 USD | 19,670.00 USD |
| `7D` | `309.40` | 10,000,000.00 USD | 10,000,000.00 USD | 0.00 USD | 27,470.00 USD | 35,530.00 USD | 46,500.00 USD |
| `7D` | `309.80` | 10,340,000.00 USD | 10,340,000.00 USD | 0.00 USD | 58,300.00 USD | 130,940.00 USD | 147,330.00 USD |
| `7D` | `310.20` | 10,470,000.00 USD | 10,470,000.00 USD | 0.00 USD | 15,450.00 USD | 55,950.00 USD | 58,800.00 USD |
| `7D` | `310.60` | 10,690,000.00 USD | 10,690,000.00 USD | 0.00 USD | 96,060.00 USD | 103,110.00 USD | 25,750.00 USD |
| `7D` | `311.00` | 10,770,000.00 USD | 10,770,000.00 USD | 0.00 USD | 27,060.00 USD | 29,540.00 USD | 21,100.00 USD |
| `7D` | `311.20` | 10,810,000.00 USD | 10,810,000.00 USD | 0.00 USD | 40,670.00 USD | 0.00 USD | 0.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `LONGS_FLUSHED` | 16,500.00 USD | 0.00 USD | 16,500.00 USD | -16,500.00 USD | `2` | `2026-10-29 17:00:00 UTC - 2026-10-29 17:05:00 UTC` |
| `15m` | `LONGS_FLUSHED` | 16,500.00 USD | 0.00 USD | 16,500.00 USD | -16,500.00 USD | `2` | `2026-10-29 17:00:00 UTC - 2026-10-29 17:15:00 UTC` |
| `1h` | `LONGS_FLUSHED` | 16,500.00 USD | 0.00 USD | 16,500.00 USD | -16,500.00 USD | `2` | `2026-10-29 17:00:00 UTC - 2026-10-29 18:00:00 UTC` |
| `4h` | `LONGS_FLUSHED` | 16,500.00 USD | 0.00 USD | 16,500.00 USD | -16,500.00 USD | `2` | `2026-10-29 16:00:00 UTC - 2026-10-29 20:00:00 UTC` |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `307.70M` | Total OI Tokens: `1,101,520.6 BCH`
  * 1h OI Change: `+0.64%` | 4h OI Change: `+0.87%` | 24h OI Change: `-8.73%`
  * Exchange Breakdown: Binance=`90.84M` | Bybit=`38.13M` | OKX=`24.52M` | Hyperliquid=`7.75M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `8.92K` | Last 24h: `10.97K` | Last 3d: `85.53K` | Last 7d: `126.00K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0034%` | **USDT OKX** | `0.0100%` |
| **USDT Bybit** | `0.0100%` | **USDT KuCoin** | `0.0084%` |
| **USDT MEXC** | `0.0034%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `0.0100%` | **USDT Bitget** | `0.0060%` |
| **CoinM Binance** | `0.0050%` | **CoinM OKX** | `0.0100%` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `BCH` | `40.57%` | `59.43%` | `0.68` | 3,650,000.00 USD |
| `15M` | `Binance` | `48.28%` | `51.72%` | `0.93` | 1,150,000.00 USD |
| `15M` | `OKX` | `59.25%` | `40.75%` | `1.45` | 174,680.00 USD |
| `15M` | `Bybit` | `43.36%` | `56.64%` | `0.77` | 93,100.00 USD |
| `15M` | `KuCoin` | `50.58%` | `49.42%` | `1.02` | 16,350.00 USD |
| `15M` | `Gate` | `48%` | `52%` | `0.92` | 33,910.00 USD |
| `15M` | `Bitget` | `50.61%` | `49.39%` | `1.02` | 76,240.00 USD |
| `15M` | `BingX` | `38.79%` | `61.21%` | `0.63` | 848,590.00 USD |
| `15M` | `MEXC` | `41.2%` | `58.8%` | `0.70` | 148,240.00 USD |
| `15M` | `Bitunix` | `46.16%` | `53.84%` | `0.86` | 53,320.00 USD |
| `15M` | `Hyperliquid` | `23.03%` | `76.97%` | `0.30` | 121,100.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `48.93%` | `51.07%` | `0.96` | 555,850.00 USD |
| `15M` | `Crypto.com` | `100%` | `0%` | `1.00` | 0.88 USD |
| `15M` | `WhiteBIT` | `0%` | `100%` | `0.00` | 371,170.00 USD |
| `15M` | `HTX` | `42.86%` | `57.14%` | `0.75` | 740.61 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `85.8%` | `14.2%` | `6.04` | 1,380.00 USD |
| `15M` | `Aster` | `99.08%` | `0.92%` | `107.70` | 1,910.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `26.45%` | `73.55%` | `0.36` | 5,250.00 USD |
| `15M` | `Whale Positions` | `48.28%` | `51.72%` | `0.93` | 1,150,000.00 USD |
| `15M` | `Global Accounts` | `40.57%` | `59.43%` | `0.68` | 3,650,000.00 USD |
| `1H` | `BCH` | `45.58%` | `54.42%` | `0.84` | 16,870,000.00 USD |
| `1H` | `Binance` | `49.31%` | `50.69%` | `0.97` | 5,760,000.00 USD |
| `1H` | `OKX` | `53.93%` | `46.07%` | `1.17` | 741,710.00 USD |
| `1H` | `Bybit` | `50.78%` | `49.22%` | `1.03` | 612,510.00 USD |
| `1H` | `KuCoin` | `71.53%` | `28.47%` | `2.51` | 177,710.00 USD |
| `1H` | `Gate` | `50.78%` | `49.22%` | `1.03` | 228,630.00 USD |
| `1H` | `Bitget` | `43.89%` | `56.11%` | `0.78` | 302,140.00 USD |
| `1H` | `BingX` | `45.99%` | `54.01%` | `0.85` | 3,240,000.00 USD |
| `1H` | `MEXC` | `51.67%` | `48.33%` | `1.07` | 994,920.00 USD |
| `1H` | `Bitunix` | `57.72%` | `42.28%` | `1.37` | 361,900.00 USD |
| `1H` | `Hyperliquid` | `48.13%` | `51.87%` | `0.93` | 260,400.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `47.86%` | `52.14%` | `0.92` | 2,880,000.00 USD |
| `1H` | `Crypto.com` | `60%` | `40%` | `1.50` | 4.40 USD |
| `1H` | `WhiteBIT` | `0.91%` | `99.09%` | `0.01` | 1,250,000.00 USD |
| `1H` | `HTX` | `40.15%` | `59.85%` | `0.67` | 3,400.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `62.82%` | `37.18%` | `1.69` | 33,510.00 USD |
| `1H` | `Aster` | `94.33%` | `5.67%` | `16.64` | 4,190.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `42.3%` | `57.7%` | `0.73` | 18,670.00 USD |
| `1H` | `Whale Positions` | `49.31%` | `50.69%` | `0.97` | 5,760,000.00 USD |
| `1H` | `Global Accounts` | `45.58%` | `54.42%` | `0.84` | 16,870,000.00 USD |
| `4H` | `BCH` | `48.15%` | `51.85%` | `0.93` | 101,210,000.00 USD |
| `4H` | `Binance` | `50.9%` | `49.1%` | `1.04` | 40,330,000.00 USD |
| `4H` | `OKX` | `49.43%` | `50.57%` | `0.98` | 13,810,000.00 USD |
| `4H` | `Bybit` | `47.7%` | `52.3%` | `0.91` | 12,010,000.00 USD |
| `4H` | `KuCoin` | `48.68%` | `51.32%` | `0.95` | 1,330,000.00 USD |
| `4H` | `Gate` | `47.16%` | `52.84%` | `0.89` | 3,160,000.00 USD |
| `4H` | `Bitget` | `47.35%` | `52.65%` | `0.90` | 3,160,000.00 USD |
| `4H` | `BingX` | `46.45%` | `53.55%` | `0.87` | 5,690,000.00 USD |
| `4H` | `MEXC` | `48.73%` | `51.27%` | `0.95` | 8,270,000.00 USD |
| `4H` | `Bitunix` | `52.72%` | `47.28%` | `1.12` | 3,430,000.00 USD |
| `4H` | `Hyperliquid` | `51.32%` | `48.68%` | `1.05` | 1,590,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `50.2%` | `49.8%` | `1.01` | 3,030,000.00 USD |
| `4H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `WhiteBIT` | `17.04%` | `82.96%` | `0.21` | 4,240,000.00 USD |
| `4H` | `HTX` | `36.88%` | `63.12%` | `0.58` | 134,110.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `36.68%` | `63.32%` | `0.58` | 706,840.00 USD |
| `4H` | `Aster` | `55.94%` | `44.06%` | `1.27` | 246,300.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `50.72%` | `49.28%` | `1.03` | 57,270.00 USD |
| `4H` | `Whale Positions` | `50.9%` | `49.1%` | `1.04` | 40,330,000.00 USD |
| `4H` | `Global Accounts` | `48.15%` | `51.85%` | `0.93` | 101,210,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5:00 UTC` | `280.07` | `279.89` | `280.07` | `280.24` | `279.38` | 446,809.90 USD | 218,581.13 USD | 228,228.77 USD | -9,647.64 USD | `-2.16%` | `21B / 13S` |
| `0:00 UTC` | `278.69` | `278.87` | `278.69` | `279.52` | `278.28` | 721,443.84 USD | 361,462.84 USD | 359,981.00 USD | 1,481.84 USD | `+0.21%` | `19B / 31S` |
| `5:00 UTC` | `279.05` | `279.00` | `279.05` | `279.40` | `278.53` | 432,899.21 USD | 250,727.14 USD | 182,172.07 USD | 68,555.07 USD | `+15.84%` | `23B / 13S` |
| `0:00 UTC` | `278.85` | `278.85` | `278.85` | `279.68` | `278.13` | 764,913.60 USD | 406,779.55 USD | 358,134.06 USD | 48,645.49 USD | `+6.36%` | `34B / 28S` |
| `5:00 UTC` | `278.42` | `278.53` | `278.42` | `278.83` | `278.33` | 354,540.52 USD | 213,514.70 USD | 141,025.82 USD | 72,488.88 USD | `+20.45%` | `16B / 7S` |
| `0:00 UTC` | `279.88` | `279.45` | `279.88` | `280.00` | `278.62` | 1,014,035.79 USD | 572,077.14 USD | 441,958.65 USD | 130,118.50 USD | `+12.83%` | `34B / 21S` |
| `5:00 UTC` | `279.00` | `279.04` | `279.00` | `279.83` | `278.56` | 1,175,579.28 USD | 812,670.57 USD | 362,908.71 USD | 449,761.85 USD | `+38.26%` | `39B / 22S` |
| `0:00 UTC` | `278.16` | `278.38` | `278.16` | `279.50` | `277.50` | 1,721,769.94 USD | 1,077,317.89 USD | 644,452.05 USD | 432,865.85 USD | `+25.14%` | `14B / 23S` |
| `5:00 UTC` | `278.03` | `278.32` | `278.03` | `279.25` | `277.75` | 1,063,430.17 USD | 555,927.53 USD | 507,502.64 USD | 48,424.89 USD | `+4.55%` | `33B / 35S` |
| `0:00 UTC` | `278.76` | `278.96` | `278.76` | `279.37` | `278.47` | 807,924.95 USD | 459,310.58 USD | 348,614.37 USD | 110,696.21 USD | `+13.70%` | `24B / 21S` |

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
| `5m` | -1,810.00 USD | -85,500.00 USD | **`DISTRIBUTION`** |
| `15m` | 2,780.00 USD | 243,230.00 USD | **`ACCUMULATION`** |
| `30m` | 6,530.00 USD | 21,070.00 USD | **`ACCUMULATION`** |
| `1h` | 50,730.00 USD | 901,480.00 USD | **`ACCUMULATION`** |
| `2h` | 30,260.00 USD | 1,580,000.00 USD | **`ACCUMULATION`** |
| `4h` | -93,180.00 USD | 1,530,000.00 USD | **`ACCUMULATION`** |
| `6h` | -48,180.00 USD | 1,240,000.00 USD | **`ACCUMULATION`** |
| `8h` | -72,990.00 USD | -681,930.00 USD | **`DISTRIBUTION`** |
| `12h` | -614,720.00 USD | -1,180,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -2,340,000.00 USD | -8,110,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -257,030.00 USD | -11,040,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -14,400,000.00 USD | -138,380,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-1.81K` | 15m=`+2.78K` | 1h=`+50.73K` | 24h=`-2.34M`
* Futures Capital Netflows: 5m=`-85.50K` | 15m=`+243.23K` | 1h=`+901.48K` | 24h=`-8.11M`
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
  * Execution Entry: `276.52` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `273.89` (Risk Distance: `2.63` pts)
  * +2.5R Take Profit: `283.10`
  * Mathematical Lot Sizing: **`3.80 lots`** (Nominal Risk = `0.10 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `285.98` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `288.61` (Risk Distance: `2.63` pts)
  * +2.5R Take Profit: `279.40`
  * Mathematical Lot Sizing: **`3.80 lots`** (Nominal Risk = `0.10 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`PASSIVE_MAKER_LIMIT_ARMED`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`290.46`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
