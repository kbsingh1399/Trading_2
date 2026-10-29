# 🏛️ SOVEREIGN CANDIDATE DOSSIER: USWTI
**Canonical Key**: `USWTI` | **Broker Instrument**: `USWTI.p` | **Asset Class**: `Energy Commodity`
**Timestamp**: `2026-10-29 22:33:52 IST` (`2026-10-29 17:03:52 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `102.01` | **Live Ask Quote**: `102.04` | **Mid Price**: `102.02`
- **Spread Points**: `30.00` | **Spread BPS**: `2.94 bps` (Charter Threshold: `5.00 bps`)
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
  * Session VWAP: `101.95` | VWAP Z-Score: `-1.85` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `0.4753` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `38.78` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `103.47` | Lower -3.00σ Band: `100.44`
  * Upper +2.51σ Band: `103.22` | Lower -2.51σ Band: `100.68`
  * Upper +2.01σ Band: `102.97` | Lower -2.01σ Band: `100.94`
  * Upper +2.00σ Band: `102.96` | Lower -2.00σ Band: `100.94`
  * Upper +1.28σ Band: `102.60` | Lower -1.28σ Band: `101.31`
  * Upper +1.00σ Band: `102.46` | Lower -1.00σ Band: `101.45`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`101.46` | EMA-20=`101.72` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`102.02` (Slope: `+0.0000`) | EMA-100=`102.17`
  * Institutional Anchors: EMA-144=`102.21` | EMA-200=`102.18` (Slope: `-0.0607`) | EMA-233=`102.09`
- **Range Boundaries**: 24H High=`104.23` | 24H Low=`100.46` | Weekly High=`104.23` | Weekly Low=`100.17`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `102.71` (Distance: `-0.63%`)
  * Point of Control (POC) = `102.03` (Distance: `+0.03%`)
  * Value Area Low (VAL) = `101.46` (Distance: `+0.59%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`103.28` | POC=`102.40` | VAL=`101.64`
  * Prior Day Extremes: PDH=`104.23` | PDL=`100.44` | PDC=`102.65`
  * Monday Range Blueprint: High=`103.88` | Mid=`102.48` | Low=`101.08`
  * Developing Weekly Value Area: Weekly VAH=`103.03` | Weekly POC=`102.03` | Weekly VAL=`101.40`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`102.95` | Low=`101.92`
  * London Session (08:00-16:00 UTC): High=`102.75` | Low=`101.25`
  * New York Session (13:00-21:00 UTC): High=`102.75` | Low=`100.46`
  * Initial Balance (First Hour): IB High=`102.04` | IB Low=`101.67`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `101.61` - `102.43`
  * Optimal Trade Entry (OTE 0.705): `102.23`
  * Structural Invalidation Anchor (0.786): `102.84`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `100.53` | `101.09` | `100.46` | `101.02` | `911` | 92,024.66 USD | 70,069.17 USD | `+76.14%` | -31,181.81 USD | `+2.07` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `5m` | `101.01` | `101.19` | `100.92` | `101.17` | `737` | 74,560.08 USD | 53,650.24 USD | `+71.96%` | 22,468.43 USD | `+1.50` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `5m` | `101.16` | `101.59` | `101.15` | `101.56` | `867` | 88,049.92 USD | 78,435.27 USD | `+89.08%` | 100,903.70 USD | `+1.78` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `101.07` | `101.15` | `100.55` | `100.72` | `2,711` | 273,057.34 USD | -134,256.98 USD | `-49.17%` | -17,428.78 USD | `-1.42` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `100.72` | `101.19` | `100.46` | `101.17` | `2,459` | 248,769.65 USD | 194,585.58 USD | `+78.22%` | 177,156.80 USD | `+2.00` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `101.16` | `101.85` | `101.15` | `101.71` | `2,389` | 242,975.63 USD | 168,160.12 USD | `+69.21%` | 345,316.91 USD | `+1.65` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `1h` | `102.68` | `102.69` | `101.88` | `101.97` | `4,809` | 490,368.92 USD | -410,972.96 USD | `-83.81%` | -614,050.18 USD | `-1.44` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `1h` | `101.97` | `101.98` | `100.46` | `101.17` | `10,331` | 1,045,156.28 USD | -311,556.76 USD | `-29.81%` | -925,606.94 USD | `-0.96` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `1h` | `101.16` | `101.85` | `100.81` | `100.95` | `8,946` | 903,080.81 USD | -425,750.58 USD | `-47.14%` | -1,351,357.52 USD | `-1.35` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `101.95` | `102.70` | `101.37` | `101.72` | `16,018` | 1,629,350.96 USD | -529,416.37 USD | `-32.49%` | -2,178,472.68 USD | `+0.05` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `101.72` | `102.75` | `101.25` | `101.97` | `20,456` | 2,085,877.86 USD | 137,301.80 USD | `+6.58%` | -2,041,170.88 USD | `+1.38` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `101.97` | `102.01` | `100.46` | `101.98` | `32,502` | 3,314,488.96 USD | 1,586,995.19 USD | `+47.88%` | -454,175.69 USD | `+2.01` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `4h` | `102.70` | `102.95` | `102.42` | `102.61` | `2,667` | 273,647.54 USD | -65,371.36 USD | `-23.89%` | -687,419.76 USD | `+1.00` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `102.59` | `102.87` | `101.92` | `101.96` | `11,805` | 1,203,637.80 USD | -961,636.55 USD | `-79.89%` | -1,649,056.31 USD | `-1.12` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `101.95` | `102.70` | `101.37` | `101.72` | `16,018` | 1,629,350.96 USD | -529,416.37 USD | `-32.49%` | -2,178,472.68 USD | `+0.05` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `101.72` | `102.75` | `101.25` | `101.97` | `20,456` | 2,085,877.86 USD | 137,301.80 USD | `+6.58%` | -2,041,170.88 USD | `+1.38` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `101.97` | `102.01` | `100.46` | `101.98` | `32,502` | 3,314,488.96 USD | 1,586,995.19 USD | `+47.88%` | -454,175.69 USD | `+2.01` | **`BULLISH`** | `AGGRESSIVE BUYING` |

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
| `42` | `0x0cc1...c7cb` | `LONG` | 30,406,608.24 USD | `300,817.26` | `98.89` | `101.00` | `32.53` | 657,107.20 USD | `+2.16%` | `3X Cross` |
| `115` | `0x30af...393e` | `LONG` | 17,947,179.01 USD | `177,712.44` | `100.98` | `101.00` | `93.19` | 1,777.12 USD | `+0.01%` | `10X Isolated` |
| `126` | `0xebe1...4070` | `LONG` | 16,273,874.24 USD | `160,999.94` | `101.87` | `101.00` | `31.22` | -127,453.76 USD | `-0.78%` | `20X Cross` |
| `172` | `0x58f0...0d20` | `SHORT` | 12,762,412.76 USD | `126,260.51` | `96.77` | `101.00` | `104.90` | -544,320.33 USD | `-4.27%` | `20X Cross` |
| `222` | `0x0c4a...1b19` | `SHORT` | 10,445,855.81 USD | `103,434.56` | `102.08` | `101.00` | `106.89` | 113,268.15 USD | `+1.08%` | `20X Isolated` |
| `310` | `0x9e2c...5508` | `LONG` | 8,084,000.00 USD | `80,000.00` | `101.05` | `101.00` | `72.98` | 85.05 USD | `+0.00%` | `20X Cross` |
| `320` | `0x7fda...17d1` | `SHORT` | 7,954,275.88 USD | `78,763.01` | `100.15` | `101.00` | `186.46` | -66,094.01 USD | `-0.83%` | `20X Cross` |
| `353` | `0x10e1...f4bd` | `LONG` | 6,833,594.87 USD | `67,625.88` | `84.36` | `101.00` | `58.54` | 1,128,364.49 USD | `+16.51%` | `3X Isolated` |
| `431` | `0xea00...a918` | `SHORT` | 5,573,588.86 USD | `55,151.29` | `89.22` | `101.00` | `265.15` | -652,864.37 USD | `-11.71%` | `20X Cross` |
| `433` | `0x4692...164f` | `SHORT` | 5,497,628.77 USD | `54,431.97` | `101.28` | `101.00` | `1158.86` | 15,397.69 USD | `+0.28%` | `5X Cross` |
| `562` | `0x5989...bc29` | `SHORT` | 4,103,010.96 USD | `40,591.72` | `99.23` | `101.00` | `111.59` | -75,076.28 USD | `-1.83%` | `10X Cross` |
| `576` | `0xd507...c948` | `LONG` | 4,022,648.62 USD | `39,808.50` | `93.57` | `101.00` | `81.35` | 297,573.21 USD | `+7.40%` | `7X Isolated` |
| `617` | `0x354b...6425` | `SHORT` | 3,800,962.90 USD | `37,633.30` | `100.94` | `101.00` | `381.99` | -2,177.33 USD | `-0.06%` | `8X Cross` |
| `742` | `0xb5e7...eff1` | `SHORT` | 3,145,295.06 USD | `31,132.29` | `91.71` | `101.00` | `144.33` | -290,086.41 USD | `-9.22%` | `20X Cross` |
| `775` | `0xd84a...c8a5` | `SHORT` | 3,030,900.00 USD | `30,000.00` | `101.76` | `101.00` | `126.62` | 21,950.00 USD | `+0.72%` | `20X Cross` |
| `838` | `0x61d7...7dee` | `LONG` | 2,815,895.23 USD | `27,858.08` | `88.25` | `101.00` | `83.50` | 357,419.23 USD | `+12.69%` | `20X Cross` |
| `908` | `0xf0ae...2f74` | `SHORT` | 2,526,000.00 USD | `25,000.00` | `100.78` | `101.00` | `175.03` | -6,481.39 USD | `-0.26%` | `20X Cross` |
| `921` | `0xb8f3...04ea` | `SHORT` | 2,481,819.93 USD | `24,560.32` | `102.91` | `101.00` | `114.77` | 45,687.06 USD | `+1.84%` | `7X Isolated` |
| `929` | `0x645b...87b8` | `SHORT` | 2,456,531.47 USD | `24,302.84` | `101.22` | `101.00` | `134.76` | 3,430.09 USD | `+0.14%` | `3X Isolated` |
| `1157` | `0x9aa5...58af` | `SHORT` | 1,987,754.55 USD | `19,671.00` | `101.76` | `101.00` | `497.88` | 13,996.38 USD | `+0.70%` | `20X Cross` |
| `1319` | `0x4169...6f06` | `LONG` | 1,734,522.44 USD | `17,175.19` | `76.61` | `101.00` | `82.99` | 418,754.44 USD | `+24.14%` | `12X Isolated` |
| `1327` | `0x6788...98d4` | `SHORT` | 1,718,360.00 USD | `17,000.00` | `99.31` | `101.00` | `192.95` | -30,035.41 USD | `-1.75%` | `20X Cross` |
| `1391` | `0xa99c...40d5` | `SHORT` | 1,627,388.00 USD | `16,100.00` | `101.02` | `101.00` | `153.64` | -930.63 USD | `-0.06%` | `20X Cross` |
| `1404` | `0x1bf6...5bfa` | `SHORT` | 1,616,800.00 USD | `16,000.00` | `99.60` | `101.00` | `225.11` | -23,177.69 USD | `-1.43%` | `20X Cross` |
| `1468` | `0xe1d3...7766` | `SHORT` | 1,550,677.05 USD | `15,347.16` | `101.53` | `101.00` | `165.64` | 7,517.96 USD | `+0.48%` | `20X Cross` |
| `1489` | `0x91fd...9841` | `LONG` | 1,529,086.83 USD | `15,134.98` | `101.16` | `101.00` | `95.58` | -1,988.67 USD | `-0.13%` | `13X Isolated` |
| `1494` | `0x17c3...a868` | `LONG` | 1,516,703.86 USD | `15,010.92` | `95.13` | `101.00` | `64.99` | 88,647.79 USD | `+5.84%` | `3X Isolated` |
| `1495` | `0x34ea...2f47` | `SHORT` | 1,516,200.00 USD | `15,000.00` | `99.80` | `101.00` | `194.62` | -19,198.69 USD | `-1.27%` | `20X Cross` |
| `1608` | `0xfb29...21dd` | `LONG` | 1,389,297.19 USD | `13,744.53` | `89.85` | `101.00` | `84.73` | 154,303.23 USD | `+11.11%` | `20X Cross` |
| `1622` | `0x6fa6...825e` | `SHORT` | 1,364,580.00 USD | `13,500.00` | `102.95` | `101.00` | `135.50` | 25,194.27 USD | `+1.85%` | `20X Isolated` |
| `1636` | `0xa9d9...b48e` | `SHORT` | 1,347,066.63 USD | `13,333.33` | `96.39` | `101.00` | `175.81` | -61,819.45 USD | `-4.59%` | `20X Cross` |
| `1685` | `0xfc27...9d9d` | `LONG` | 1,297,361.97 USD | `12,845.17` | `101.58` | `101.00` | `0.000000` | -7,444.80 USD | `-0.57%` | `20X Cross` |
| `1737` | `0x89c2...c94b` | `LONG` | 1,249,822.97 USD | `12,364.69` | `75.25` | `101.00` | `45.76` | 319,339.81 USD | `+25.55%` | `3X Isolated` |
| `1760` | `0xcd81...36e3` | `SHORT` | 1,219,425.48 USD | `12,063.96` | `97.96` | `101.00` | `112.03` | -37,586.56 USD | `-3.08%` | `20X Cross` |
| `1770` | `0x436c...b3d1` | `SHORT` | 1,212,960.00 USD | `12,000.00` | `101.05` | `101.00` | `205.93` | -300.17 USD | `-0.02%` | `20X Cross` |
| `1781` | `0xfdfb...dbb9` | `SHORT` | 1,206,125.27 USD | `11,932.38` | `100.90` | `101.00` | `111.13` | -2,142.65 USD | `-0.18%` | `20X Cross` |
| `1839` | `0x9dea...d617` | `LONG` | 1,152,050.64 USD | `11,400.80` | `90.37` | `101.00` | `4.19` | 121,776.91 USD | `+10.57%` | `20X Cross` |
| `1876` | `0x8afa...8113` | `SHORT` | 1,121,825.98 USD | `11,101.69` | `100.52` | `101.00` | `107.78` | -5,881.47 USD | `-0.52%` | `10X Isolated` |
| `1887` | `0x8607...08d5` | `SHORT` | 1,111,688.15 USD | `10,998.10` | `92.18` | `101.00` | `135.02` | -97,898.45 USD | `-8.81%` | `4X Isolated` |
| `2029` | `0xf29c...9971` | `SHORT` | 1,010,800.00 USD | `10,000.00` | `101.10` | `101.00` | `118.37` | 196.03 USD | `+0.02%` | `5X Isolated` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| Intel | Baseline | - | - | - | Neutral | - | No anomalous telegram alerts in current window | - |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`103.96` (Vol: 6,300,000.00 USD, Dist: `+3.00%`) | Long MP=`99.15` (Vol: 4,000,000.00 USD, Dist: `--1.77%`)
  * 48H Horizon: Short MP=`0.000000` (Vol: 0.00 USD, Dist: `+0.00%`) | Long MP=`99.25` (Vol: 11,700,000.00 USD, Dist: `--1.66%`)
  * 3D Horizon: Short MP=`103.95` (Vol: 7,900,000.00 USD, Dist: `+3.00%`) | Long MP=`99.25` (Vol: 9,800,000.00 USD, Dist: `--1.66%`)
  * 7D Horizon: Short MP=`104.02` (Vol: 12,400,000.00 USD, Dist: `+3.06%`) | Long MP=`99.18` (Vol: 15,700,000.00 USD, Dist: `--1.74%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Envelope` | `Long Liquidation` | `99.83` | 25,000,000.00 USD | 50,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 4 Macro Envelope` |
| `Envelope` | `Short Liquidation` | `102.20` | 25,000,000.00 USD | 50,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 4 Macro Envelope` |

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
  * Current Rate: `-13.92K` | Last 24h: `-159.23K` | Last 3d: `-426.22K` | Last 7d: `-798.78K`
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
| `13:30:00` | `102.06` | `102.06` | `102.06` | `102.23` | `102.00` | 39,907.42 USD | 12,145.73 USD | 27,761.68 USD | -15,615.95 USD | `-39.13%` | `0B / 1S` |
| `13:35:00` | `102.04` | `102.04` | `102.04` | `102.09` | `101.82` | 55,611.80 USD | 35,506.79 USD | 20,105.01 USD | 15,401.78 USD | `+27.70%` | `1B / 0S` |
| `13:40:00` | `102.18` | `102.18` | `102.18` | `102.19` | `102.03` | 41,075.56 USD | 38,104.68 USD | 2,970.87 USD | 35,133.81 USD | `+85.53%` | `1B / 0S` |
| `13:45:00` | `102.14` | `102.14` | `102.14` | `102.22` | `102.12` | 33,094.98 USD | 8,618.48 USD | 24,476.50 USD | -15,858.01 USD | `-47.92%` | `0B / 1S` |
| `13:45:00` | `101.86` | `101.86` | `101.86` | `102.22` | `101.82` | 100,225.32 USD | 8,895.00 USD | 91,330.32 USD | -82,435.33 USD | `-82.25%` | `0B / 1S` |
| `13:50:00` | `101.94` | `101.94` | `101.94` | `102.14` | `101.94` | 34,149.90 USD | 1,707.50 USD | 32,442.40 USD | -30,734.91 USD | `-90.00%` | `0B / 1S` |
| `13:55:00` | `101.86` | `101.86` | `101.86` | `101.98` | `101.82` | 33,102.88 USD | 7,758.49 USD | 25,344.39 USD | -17,585.90 USD | `-53.12%` | `0B / 1S` |
| `14:00:00` | `101.92` | `101.92` | `101.92` | `101.98` | `101.81` | 36,181.24 USD | 24,053.45 USD | 12,127.79 USD | 11,925.66 USD | `+32.96%` | `1B / 0S` |
| `14:00:00` | `102.69` | `102.69` | `102.69` | `102.75` | `101.76` | 443,308.41 USD | 413,052.28 USD | 30,256.14 USD | 382,796.14 USD | `+86.35%` | `1B / 0S` |
| `14:00:00` | `101.97` | `101.97` | `101.97` | `101.98` | `101.81` | 91,161.18 USD | 79,766.03 USD | 11,395.15 USD | 68,370.89 USD | `+75.00%` | `1B / 0S` |
| `5:00 UTC` | `102.00` | `102.00` | `102.00` | `102.18` | `101.84` | 11,560,167.11 USD | 6,994,163.38 USD | 4,566,003.73 USD | 2,428,159.66 USD | `+21.00%` | `7B / 1S` |
| `0:00 UTC` | `102.03` | `102.02` | `102.03` | `102.12` | `101.91` | 6,078,725.95 USD | 3,562,566.38 USD | 2,516,159.57 USD | 1,046,406.82 USD | `+17.21%` | `1B / 2S` |
| `5:00 UTC` | `101.88` | `101.92` | `101.88` | `102.06` | `101.81` | 4,847,301.58 USD | 1,901,895.37 USD | 2,945,406.21 USD | -1,043,510.84 USD | `-21.53%` | `3B / 5S` |
| `0:00 UTC` | `101.85` | `101.81` | `101.85` | `102.05` | `101.60` | 9,275,521.74 USD | 3,861,659.26 USD | 5,413,862.48 USD | -1,552,203.21 USD | `-16.73%` | `5B / 10S` |
| `5:00 UTC` | `101.45` | `101.48` | `101.45` | `101.66` | `101.34` | 10,009,536.75 USD | 4,872,743.82 USD | 5,136,792.93 USD | -264,049.11 USD | `-2.64%` | `6B / 5S` |
| `0:00 UTC` | `100.93` | `100.87` | `100.93` | `101.44` | `100.56` | 67,791,458.08 USD | 34,390,131.97 USD | 33,401,326.11 USD | 988,805.85 USD | `+1.46%` | `16B / 18S` |
| `5:00 UTC` | `100.62` | `100.60` | `100.62` | `100.94` | `100.38` | 32,174,644.58 USD | 18,148,276.98 USD | 14,026,367.61 USD | 4,121,909.37 USD | `+12.81%` | `9B / 5S` |
| `0:00 UTC` | `100.00` | `100.15` | `100.00` | `100.59` | `99.98` | 90,640,598.12 USD | 53,162,348.18 USD | 37,478,249.94 USD | 15,684,098.24 USD | `+17.30%` | `8B / 7S` |
| `5:00 UTC` | `99.97` | `100.27` | `99.97` | `100.66` | `99.88` | 46,232,592.72 USD | 24,620,029.24 USD | 21,612,563.48 USD | 3,007,465.75 USD | `+6.51%` | `9B / 8S` |
| `0:00 UTC` | `100.93` | `100.95` | `100.93` | `101.28` | `100.62` | 27,341,029.63 USD | 14,689,132.99 USD | 12,651,896.64 USD | 2,037,236.35 USD | `+7.45%` | `22B / 6S` |

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
  * Execution Entry: `101.46` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `100.85` (Risk Distance: `0.6153` pts)
  * +2.5R Take Profit: `103.00`
  * Mathematical Lot Sizing: **`0.10 lots`** (Nominal Risk = `0.62 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `102.71` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `103.33` (Risk Distance: `0.6153` pts)
  * +2.5R Take Profit: `101.17`
  * Mathematical Lot Sizing: **`0.10 lots`** (Nominal Risk = `0.62 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`PASSIVE_MAKER_LIMIT_ARMED`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`102.84`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
