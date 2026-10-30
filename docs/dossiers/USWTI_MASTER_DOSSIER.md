# 🏛️ SOVEREIGN CANDIDATE DOSSIER: USWTI
**Canonical Key**: `USWTI` | **Broker Instrument**: `USWTI.p` | **Asset Class**: `Energy Commodity`
**Timestamp**: `2026-10-30 10:19:40 IST` (`2026-10-30 04:49:40 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `103.78` | **Live Ask Quote**: `103.83` | **Mid Price**: `103.80`
- **Spread Points**: `46.00` | **Spread BPS**: `4.43 bps` (Charter Threshold: `5.00 bps`)
- **Gate 1 Clearance**: **`PASS`** | **Execution Posture**: `PASSIVE LIMIT ONLY` | **Order Type Allowed**: `BUY_LIMIT / SELL_LIMIT`
- **True Broker Contract Specifications**:
  * Contract Size: `1,000.0` | Digits: `2` | Point: `0.01`
  * Point Value (1.0 Lot): `10.00 USD` | Point Value (0.01 Lot): `0.1000 USD`
  * Allowed Lot Sizing: Min Lot=`0.10` | Step Lot=`0.10` | Max Lot=`50.00`
- **Solvency Defense Ladder**:
  * Hard Floor Stop: `4,775.00 USD` (Zero Open Risk) | Operating Defense Buffer: `4,795.00 USD` (Capital Preservation Mode)
  * Kernel Admission Floor: `4,795.00 USD` (`min(balance, equity) - StressedLoss - 2.00 >= 4,795.00 USD`)
- **Pipeline Health (23_Master_Pipeline_Telemetry.parquet)**: Status=`HEALTHY` | Latency=`4.2 ms` | RAM Usage=`385.0 MB`

---

## 2. Technical Profile, VWAP Dispersion Grid & BTC Ribbon
*(Sources: 11_Technical.parquet, 11_Technical_BTC_Ribbon.parquet)*
- **Session Anchor & Volatility**:
  * Session VWAP: `104.20` | VWAP Z-Score: `-0.68` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `0.3189` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `51.72` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `106.13` | Lower -3.00σ Band: `102.27`
  * Upper +2.51σ Band: `105.81` | Lower -2.51σ Band: `102.58`
  * Upper +2.01σ Band: `105.49` | Lower -2.01σ Band: `102.90`
  * Upper +2.00σ Band: `105.49` | Lower -2.00σ Band: `102.91`
  * Upper +1.28σ Band: `105.02` | Lower -1.28σ Band: `103.37`
  * Upper +1.00σ Band: `104.84` | Lower -1.00σ Band: `103.55`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`103.91` | EMA-20=`103.81` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`103.31` (Slope: `+0.0000`) | EMA-100=`102.90`
  * Institutional Anchors: EMA-144=`102.71` | EMA-200=`102.49` (Slope: `+0.2099`) | EMA-233=`102.43`
- **Range Boundaries**: 24H High=`105.59` | 24H Low=`100.46` | Weekly High=`105.59` | Weekly Low=`100.17`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `104.60` (Distance: `-0.76%`)
  * Point of Control (POC) = `103.38` (Distance: `+0.41%`)
  * Value Area Low (VAL) = `103.05` (Distance: `+0.73%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BULLISH (Above Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`102.76` | POC=`102.02` | VAL=`101.40`
  * Prior Day Extremes: PDH=`103.64` | PDL=`100.46` | PDC=`103.54`
  * Monday Range Blueprint: High=`103.88` | Mid=`102.48` | Low=`101.08`
  * Developing Weekly Value Area: Weekly VAH=`103.19` | Weekly POC=`102.03` | Weekly VAL=`101.42`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`105.59` | Low=`103.05`
  * London Session (08:00-16:00 UTC): High=`104.22` | Low=`103.39`
  * New York Session (13:00-21:00 UTC): High=`104.43` | Low=`103.18`
  * Initial Balance (First Hour): IB High=`104.11` | IB Low=`103.49`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `103.39` - `104.22`
  * Optimal Trade Entry (OTE 0.705): `104.01`
  * Structural Invalidation Anchor (0.786): `104.63`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `103.41` | `103.69` | `103.34` | `103.69` | `360` | 37,328.40 USD | 33,595.56 USD | `+90.00%` | 221,251.81 USD | `+1.98` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `5m` | `103.69` | `104.83` | `103.63` | `104.59` | `869` | 90,893.05 USD | 62,110.25 USD | `+68.33%` | 283,362.06 USD | `+2.82` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `5m` | `104.61` | `105.19` | `104.60` | `105.01` | `1,198` | 125,801.98 USD | 66,601.05 USD | `+52.94%` | 349,963.11 USD | `+2.41` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `103.06` | `103.49` | `103.05` | `103.37` | `1,876` | 193,918.37 USD | 112,314.71 USD | `+57.92%` | 643,742.44 USD | `+2.88` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `103.37` | `103.42` | `103.27` | `103.42` | `910` | 94,107.65 USD | 55,197.76 USD | `+58.65%` | 698,940.19 USD | `+1.20` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `103.41` | `105.19` | `103.34` | `105.01` | `2,427` | 254,859.27 USD | 211,924.76 USD | `+83.15%` | 910,864.95 USD | `+3.32` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `1h` | `103.46` | `103.48` | `103.24` | `103.48` | `567` | 58,673.16 USD | 30,533.99 USD | `+52.04%` | 557,457.58 USD | `-0.03` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `1h` | `103.46` | `103.53` | `103.06` | `103.07` | `1,416` | 145,947.12 USD | -131,352.41 USD | `-90.00%` | 426,105.17 USD | `-0.60` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `1h` | `103.06` | `105.59` | `103.05` | `104.94` | `7,807` | 819,305.61 USD | 505,426.25 USD | `+61.69%` | 931,531.43 USD | `+1.48` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `4h` | `101.97` | `103.64` | `101.90` | `103.54` | `17,042` | 1,764,579.81 USD | 1,581,740.16 USD | `+89.64%` | 2,776,620.79 USD | `+0.96` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `4h` | `103.47` | `103.54` | `103.06` | `103.07` | `2,890` | 297,872.30 USD | -268,085.07 USD | `-90.00%` | 2,508,535.72 USD | `-0.85` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `103.06` | `105.59` | `103.05` | `103.78` | `15,287` | 1,586,484.86 USD | -110,648.75 USD | `-6.97%` | 2,397,886.97 USD | `-0.59` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `101.72` | `102.75` | `101.25` | `101.97` | `20,456` | 2,085,877.86 USD | 137,301.80 USD | `+6.58%` | -392,114.57 USD | `+1.00` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `101.97` | `102.01` | `100.46` | `101.98` | `32,502` | 3,314,488.96 USD | 1,586,995.19 USD | `+47.88%` | 1,194,880.62 USD | `+1.35` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `4h` | `101.97` | `103.64` | `101.90` | `103.54` | `17,042` | 1,764,579.81 USD | 1,581,740.16 USD | `+89.64%` | 2,776,620.79 USD | `+0.96` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `4h` | `103.47` | `103.54` | `103.06` | `103.07` | `2,890` | 297,872.30 USD | -268,085.07 USD | `-90.00%` | 2,508,535.72 USD | `-0.85` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `103.06` | `105.59` | `103.05` | `103.78` | `15,287` | 1,586,484.86 USD | -110,648.75 USD | `-6.97%` | 2,397,886.97 USD | `-0.59` | **`BEARISH`** | `BEARISH ABSORPTION` |

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
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 10:14:44 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `42` | `0x0cc1...c7cb` | `LONG` | 31,047,348.99 USD | `300,817.26` | `98.89` | `103.21` | `31.50` | 1,297,847.96 USD | `+4.18%` | `3X Cross` |
| `113` | `0x30af...393e` | `LONG` | 18,343,477.75 USD | `177,712.44` | `100.98` | `103.21` | `93.19` | 398,075.86 USD | `+2.17%` | `10X Isolated` |
| `290` | `0x7fda...17d1` | `SHORT` | 8,117,216.63 USD | `78,647.58` | `100.15` | `103.21` | `212.12` | -240,594.78 USD | `-2.96%` | `20X Cross` |
| `332` | `0x10e1...f4bd` | `LONG` | 6,981,019.28 USD | `67,625.88` | `84.36` | `103.21` | `58.53` | 1,275,788.90 USD | `+18.28%` | `3X Isolated` |
| `394` | `0xea00...a918` | `SHORT` | 5,692,715.64 USD | `55,151.29` | `89.22` | `103.21` | `241.82` | -771,991.14 USD | `-13.56%` | `20X Cross` |
| `416` | `0x354b...6425` | `SHORT` | 5,347,207.92 USD | `51,809.01` | `102.87` | `103.21` | `307.43` | -17,471.27 USD | `-0.33%` | `8X Cross` |
| `490` | `0x4692...164f` | `SHORT` | 4,571,008.65 USD | `44,288.43` | `103.56` | `103.21` | `1510.58` | 15,351.29 USD | `+0.34%` | `5X Cross` |
| `496` | `0x5989...bc29` | `SHORT` | 4,509,422.32 USD | `43,691.72` | `99.48` | `103.21` | `113.23` | -163,115.42 USD | `-3.62%` | `10X Cross` |
| `540` | `0xd84a...c8a5` | `SHORT` | 4,128,800.00 USD | `40,000.00` | `101.97` | `103.21` | `119.21` | -50,170.00 USD | `-1.22%` | `20X Cross` |
| `543` | `0xd507...c948` | `LONG` | 4,108,634.98 USD | `39,808.50` | `93.57` | `103.21` | `82.63` | 383,559.56 USD | `+9.34%` | `7X Isolated` |
| `705` | `0xb5e7...eff1` | `SHORT` | 3,213,474.77 USD | `31,132.29` | `91.71` | `103.21` | `144.56` | -358,266.12 USD | `-11.15%` | `20X Cross` |
| `738` | `0xebe1...4070` | `LONG` | 3,096,297.21 USD | `29,999.97` | `101.87` | `103.21` | `0.000000` | 40,159.18 USD | `+1.30%` | `20X Cross` |
| `739` | `0xbd33...4200` | `SHORT` | 3,094,813.78 USD | `29,982.69` | `104.89` | `103.21` | `403.27` | 50,071.10 USD | `+1.62%` | `20X Cross` |
| `798` | `0x61d7...7dee` | `LONG` | 2,875,232.95 USD | `27,858.08` | `88.25` | `103.21` | `83.50` | 416,756.95 USD | `+14.49%` | `20X Cross` |
| `881` | `0xf0ae...2f74` | `SHORT` | 2,580,500.00 USD | `25,000.00` | `100.78` | `103.21` | `176.67` | -60,981.39 USD | `-2.36%` | `20X Cross` |
| `898` | `0x645b...87b8` | `SHORT` | 2,523,668.42 USD | `24,451.78` | `101.23` | `103.21` | `134.76` | -48,324.16 USD | `-1.91%` | `3X Isolated` |
| `993` | `0x40f2...6a9e` | `LONG` | 2,243,100.91 USD | `21,733.37` | `103.34` | `103.21` | `100.57` | -2,909.05 USD | `-0.13%` | `20X Cross` |
| `1078` | `0x9aa5...58af` | `SHORT` | 2,030,243.91 USD | `19,671.00` | `101.76` | `103.21` | `566.65` | -28,492.98 USD | `-1.40%` | `20X Cross` |
| `1252` | `0x4169...6f06` | `LONG` | 1,772,823.11 USD | `17,175.19` | `76.61` | `103.21` | `82.98` | 457,055.11 USD | `+25.78%` | `12X Isolated` |
| `1260` | `0x6788...98d4` | `SHORT` | 1,754,570.00 USD | `17,000.00` | `99.31` | `103.21` | `198.82` | -66,245.41 USD | `-3.78%` | `20X Cross` |
| `1307` | `0xa99c...40d5` | `SHORT` | 1,661,681.00 USD | `16,100.00` | `101.02` | `103.21` | `152.89` | -35,223.63 USD | `-2.12%` | `20X Cross` |
| `1319` | `0x1bf6...5bfa` | `SHORT` | 1,651,360.00 USD | `16,000.00` | `99.60` | `103.21` | `227.46` | -57,737.69 USD | `-3.50%` | `20X Cross` |
| `1353` | `0xe5dd...ecba` | `SHORT` | 1,607,706.21 USD | `15,575.53` | `102.71` | `103.21` | `145.00` | -7,950.83 USD | `-0.49%` | `20X Cross` |
| `1416` | `0x5d6f...6f8a` | `LONG` | 1,548,300.00 USD | `15,000.00` | `101.91` | `103.21` | `27.47` | 19,645.00 USD | `+1.27%` | `20X Cross` |
| `1418` | `0x34ea...2f47` | `SHORT` | 1,548,150.00 USD | `15,000.00` | `99.80` | `103.21` | `200.22` | -51,148.69 USD | `-3.30%` | `20X Cross` |
| `1476` | `0xfc27...9d9d` | `LONG` | 1,474,395.31 USD | `14,285.39` | `102.69` | `103.21` | `0.000000` | 7,495.03 USD | `+0.51%` | `20X Cross` |
| `1527` | `0xfb29...21dd` | `LONG` | 1,418,710.49 USD | `13,744.53` | `89.85` | `103.21` | `84.66` | 183,716.53 USD | `+12.95%` | `20X Cross` |
| `1545` | `0x6fa6...825e` | `SHORT` | 1,393,335.00 USD | `13,500.00` | `102.95` | `103.21` | `135.50` | -3,560.73 USD | `-0.26%` | `20X Isolated` |
| `1572` | `0xa9d9...b48e` | `SHORT` | 1,376,266.63 USD | `13,333.33` | `96.39` | `103.21` | `174.17` | -91,019.45 USD | `-6.61%` | `20X Cross` |
| `1624` | `0x936c...bb0f` | `SHORT` | 1,309,518.98 USD | `12,687.91` | `101.39` | `103.21` | `163.64` | -23,046.11 USD | `-1.76%` | `2X Isolated` |
| `1658` | `0x89c2...c94b` | `LONG` | 1,276,159.76 USD | `12,364.69` | `75.25` | `103.21` | `45.76` | 345,676.61 USD | `+27.09%` | `3X Isolated` |
| `1697` | `0xcd81...36e3` | `SHORT` | 1,245,121.72 USD | `12,063.96` | `97.96` | `103.21` | `109.14` | -63,282.80 USD | `-5.08%` | `20X Cross` |
| `1701` | `0x436c...b3d1` | `SHORT` | 1,238,520.00 USD | `12,000.00` | `101.05` | `103.21` | `208.42` | -25,860.17 USD | `-2.09%` | `20X Cross` |
| `1766` | `0x9dea...d617` | `LONG` | 1,176,676.36 USD | `11,400.80` | `90.37` | `103.21` | `4.93` | 146,402.64 USD | `+12.44%` | `20X Cross` |
| `1785` | `0x17c3...a868` | `LONG` | 1,167,066.94 USD | `11,306.60` | `95.13` | `103.21` | `64.99` | 91,420.07 USD | `+7.83%` | `3X Isolated` |
| `1835` | `0x8607...08d5` | `SHORT` | 1,135,114.11 USD | `10,998.10` | `92.18` | `103.21` | `135.02` | -121,324.40 USD | `-10.69%` | `4X Isolated` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| Intel | Baseline | - | - | - | Neutral | - | No anomalous telegram alerts in current window | - |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`105.84` (Vol: 3,800,000.00 USD, Dist: `+2.40%`) | Long MP=`99.16` (Vol: 6,700,000.00 USD, Dist: `--4.05%`)
  * 48H Horizon: Short MP=`105.84` (Vol: 2,400,000.00 USD, Dist: `+2.40%`) | Long MP=`99.16` (Vol: 4,000,000.00 USD, Dist: `--4.05%`)
  * 3D Horizon: Short MP=`105.86` (Vol: 2,700,000.00 USD, Dist: `+2.42%`) | Long MP=`99.12` (Vol: 9,700,000.00 USD, Dist: `--4.09%`)
  * 7D Horizon: Short MP=`105.58` (Vol: 4,200,000.00 USD, Dist: `+2.16%`) | Long MP=`99.12` (Vol: 8,700,000.00 USD, Dist: `--4.09%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Matrix | Interbank Flow | - | - | - | - | - | - | Interbank Tier |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Map | Near Money | - | - | - | - | 0.00% | - |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Stops | Clear | - | - | - | 0.00% | SAFE (No Un-Swept Clusters) |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Exchange | Baseline | - | - | - | - | - | - |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `0 USD` | Total OI Tokens: `-`
  * 1h OI Change: `0.00%` | 4h OI Change: `0.00%` | 24h OI Change: `0.00%`
  * Exchange Breakdown: Binance=`-` | Bybit=`-` | OKX=`-` | Hyperliquid=`-`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `-206.15K` | Last 24h: `-501.60K` | Last 3d: `-815.84K` | Last 7d: `-1.22M`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `-` | **USDT OKX** | `-` |
| **USDT Bybit** | `-` | **USDT KuCoin** | `-` |
| **USDT MEXC** | `-` | **USDT BingX** | `-` |
| **USDT Gate** | `-` | **USDT Bitget** | `-` |
| **CoinM Binance** | `-` | **CoinM OKX** | `-` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| Multi-TF | Interbank Desk | 50.0% | 50.0% | 1.00 | Normal Balanced Liquidity |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `04:00:00` | `103.23` | `103.23` | `103.23` | `103.35` | `103.05` | 87,852.99 USD | 62,060.62 USD | 25,792.36 USD | 36,268.26 USD | `+41.28%` | `1B / 0S` |
| `04:00:00` | `103.75` | `103.75` | `103.75` | `105.59` | `103.05` | 1,571,916.25 USD | 717,244.69 USD | 854,671.56 USD | -137,426.86 USD | `-8.74%` | `0B / 1S` |
| `04:05:00` | `103.39` | `103.39` | `103.39` | `103.47` | `103.09` | 55,105.27 USD | 40,316.52 USD | 14,788.75 USD | 25,527.77 USD | `+46.33%` | `1B / 0S` |
| `04:10:00` | `103.37` | `103.37` | `103.37` | `103.49` | `103.28` | 50,857.06 USD | 23,491.12 USD | 27,365.94 USD | -3,874.82 USD | `-7.62%` | `0B / 1S` |
| `04:15:00` | `103.42` | `103.42` | `103.42` | `103.42` | `103.27` | 94,107.65 USD | 74,652.70 USD | 19,454.95 USD | 55,197.76 USD | `+58.65%` | `1B / 0S` |
| `04:15:00` | `103.32` | `103.32` | `103.32` | `103.40` | `103.28` | 34,198.59 USD | 10,806.75 USD | 23,391.83 USD | -12,585.08 USD | `-36.80%` | `0B / 1S` |
| `04:20:00` | `103.40` | `103.40` | `103.40` | `103.41` | `103.27` | 33,087.68 USD | 28,951.72 USD | 4,135.96 USD | 24,815.76 USD | `+75.00%` | `1B / 0S` |
| `04:25:00` | `103.42` | `103.42` | `103.42` | `103.42` | `103.31` | 26,784.49 USD | 20,437.73 USD | 6,346.76 USD | 14,090.97 USD | `+52.61%` | `1B / 0S` |
| `04:30:00` | `103.69` | `103.69` | `103.69` | `103.69` | `103.34` | 37,328.40 USD | 35,461.98 USD | 1,866.42 USD | 33,595.56 USD | `+90.00%` | `1B / 0S` |
| `04:30:00` | `105.01` | `105.01` | `105.01` | `105.19` | `103.34` | 254,859.27 USD | 233,392.01 USD | 21,467.26 USD | 211,924.76 USD | `+83.15%` | `1B / 0S` |
| `5:00 UTC` | `104.16` | `104.05` | `104.16` | `104.37` | `103.80` | 17,456,844.99 USD | 6,372,777.32 USD | 11,084,067.66 USD | -4,711,290.34 USD | `-26.99%` | `4B / 16S` |
| `0:00 UTC` | `103.73` | `103.70` | `103.73` | `103.94` | `103.56` | 19,737,902.95 USD | 10,509,099.07 USD | 9,228,803.87 USD | 1,280,295.20 USD | `+6.49%` | `3B / 4S` |
| `5:00 UTC` | `103.41` | `103.50` | `103.41` | `103.72` | `103.38` | 17,811,792.57 USD | 9,252,258.83 USD | 8,559,533.74 USD | 692,725.09 USD | `+3.89%` | `4B / 5S` |
| `0:00 UTC` | `103.60` | `103.57` | `103.60` | `103.66` | `103.45` | 4,757,917.11 USD | 2,812,614.52 USD | 1,945,302.59 USD | 867,311.92 USD | `+18.23%` | `3B / 2S` |
| `5:00 UTC` | `103.53` | `103.52` | `103.53` | `103.59` | `103.44` | 3,389,658.00 USD | 1,302,314.80 USD | 2,087,343.19 USD | -785,028.39 USD | `-23.16%` | `2B / 3S` |
| `0:00 UTC` | `103.50` | `103.53` | `103.50` | `103.66` | `103.41` | 4,898,115.03 USD | 2,100,565.02 USD | 2,797,550.01 USD | -696,984.99 USD | `-14.23%` | `4B / 8S` |
| `5:00 UTC` | `103.32` | `103.37` | `103.32` | `103.50` | `103.30` | 5,800,580.27 USD | 3,315,920.42 USD | 2,484,659.85 USD | 831,260.57 USD | `+14.33%` | `4B / 1S` |
| `0:00 UTC` | `103.38` | `103.38` | `103.38` | `103.44` | `103.31` | 5,199,824.51 USD | 3,341,152.42 USD | 1,858,672.10 USD | 1,482,480.32 USD | `+28.51%` | `3B / 2S` |
| `5:00 UTC` | `103.31` | `103.30` | `103.31` | `103.34` | `103.23` | 3,756,770.69 USD | 2,127,360.29 USD | 1,629,410.40 USD | 497,949.89 USD | `+13.25%` | `2B / 1S` |
| `0:00 UTC` | `103.25` | `103.27` | `103.25` | `103.37` | `103.23` | 1,909,565.38 USD | 835,142.54 USD | 1,074,422.84 USD | -239,280.31 USD | `-12.53%` | `3B / 3S` |

- **CoinGlass Algorithmic Footprint Signals Table (25_CoinGlass_Footprint_Signals.parquet)**:
| Time | Timeframe | Signal Type | Bias | Headline | Price Level | Absorbed Vol (USD) | Bar Delta (USD) |
|:---:|:---:|:---:|:---:|:---|:---:|:---:|:---:|
| `2026-10-28 17:30:00 IST` | `4h` | `AGGRESSIVE BUYING` | **`BULLISH`** | WTI_OIL Macro Delta Flow: AGGRESSIVE BUY | `102.68` | 803,986.89 USD | 803,986.89 USD |
| `10-28 18:20` | `Volume 200K CL` | `Absorption` | **`BEARISH`** | Buying absorbed at the high | `102.21` | 51,000.00 USD | 0.00 USD |
| `10-28 11:54` | `Volume 200K CL` | `Divergence` | **`BEARISH`** | Rally without taker buying | `101.96` | 0.00 USD | 0.00 USD |
| `10-28 07:12` | `Volume 200K CL` | `Divergence` | **`BEARISH`** | Rally without taker buying | `101.50` | 0.00 USD | 0.00 USD |

- **12-Horizon Macro Capital Netflows Table (2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet)**:
| Horizon | Spot Netflow (USD) | Futures Netflow (USD) | Institutional Bias |
|:---:|:---:|:---:|:---:|
| `5m` | 0.00 USD | 0.00 USD | **`NEUTRAL`** |
| `15m` | 0.00 USD | 0.00 USD | **`NEUTRAL`** |
| `30m` | 0.00 USD | 0.00 USD | **`NEUTRAL`** |
| `1h` | 0.00 USD | 0.00 USD | **`NEUTRAL`** |
| `2h` | 0.00 USD | 0.00 USD | **`NEUTRAL`** |
| `4h` | 0.00 USD | 0.00 USD | **`NEUTRAL`** |
| `6h` | 0.00 USD | 0.00 USD | **`NEUTRAL`** |
| `8h` | 0.00 USD | 0.00 USD | **`NEUTRAL`** |
| `12h` | 0.00 USD | 0.00 USD | **`NEUTRAL`** |
| `24h` | 0.00 USD | 0.00 USD | **`NEUTRAL`** |
| `1w` | 0.00 USD | 0.00 USD | **`NEUTRAL`** |
| `30d` | 0.00 USD | 0.00 USD | **`NEUTRAL`** |

* Spot Capital Netflows: 5m=`-` | 15m=`-` | 1h=`-` | 24h=`-`
* Futures Capital Netflows: 5m=`-` | 15m=`-` | 1h=`-` | 24h=`-`
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
  * `2026-10-30 09:50:55 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 10:09:55 IST`: [forex.com] - (Sentiment: `Neutral`)
  * `2026-10-30 10:09:55 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 10:09:55 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 10:08:55 IST`: [financemagnates.com] - (Sentiment: `Neutral`)
  * `2026-10-30 10:08:55 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-30 07:10:55 IST`: [kathleenhays.substack.com] - (Sentiment: `Neutral`)
  * `2026-10-30 06:10:55 IST`: [rba.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 06:10:55 IST`: [abs.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 06:10:55 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 06:10:55 IST`: [@NodeWire] - (Sentiment: `Neutral`)
  * `2026-10-30 06:10:55 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 06:10:55 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 06:10:55 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-30 05:10:55 IST`: [media.rabobank.com] - (Sentiment: `Neutral`)


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
  * Execution Entry: `103.05` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `102.60` (Risk Distance: `0.4517` pts)
  * +2.5R Take Profit: `104.18`
  * Mathematical Lot Sizing: **`0.10 lots`** (Nominal Risk = `0.45 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `104.60` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `105.05` (Risk Distance: `0.4517` pts)
  * +2.5R Take Profit: `103.47`
  * Mathematical Lot Sizing: **`0.10 lots`** (Nominal Risk = `0.45 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`PASSIVE_MAKER_LIMIT_ARMED`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`104.63`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
