# 🏛️ SOVEREIGN CANDIDATE DOSSIER: USWTI
**Canonical Key**: `USWTI` | **Broker Instrument**: `USWTI.p` | **Asset Class**: `Energy Commodity`
**Timestamp**: `2026-10-30 01:05:40 IST` (`2026-10-29 19:35:40 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `102.90` | **Live Ask Quote**: `102.95` | **Mid Price**: `102.92`
- **Spread Points**: `46.00` | **Spread BPS**: `4.47 bps` (Charter Threshold: `5.00 bps`)
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
  * Session VWAP: `102.92` | VWAP Z-Score: `+0.00` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `1.00` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `50.00` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `103.64` | Lower -3.00σ Band: `102.20`
  * Upper +2.51σ Band: `103.49` | Lower -2.51σ Band: `102.36`
  * Upper +2.01σ Band: `103.36` | Lower -2.01σ Band: `102.49`
  * Upper +2.00σ Band: `103.33` | Lower -2.00σ Band: `102.51`
  * Upper +1.28σ Band: `103.21` | Lower -1.28σ Band: `102.63`
  * Upper +1.00σ Band: `103.13` | Lower -1.00σ Band: `102.72`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`102.92` | EMA-20=`102.92` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`102.92` (Slope: `+0.0000`) | EMA-100=`102.92`
  * Institutional Anchors: EMA-144=`102.92` | EMA-200=`102.92` (Slope: `+0.0000`) | EMA-233=`102.92`
- **Range Boundaries**: 24H High=`103.95` | 24H Low=`101.89` | Weekly High=`104.98` | Weekly Low=`100.86`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `102.76` (Distance: `+0.17%`)
  * Point of Control (POC) = `102.03` (Distance: `+0.89%`)
  * Value Area Low (VAL) = `101.51` (Distance: `+1.40%`)
  * Auction Positioning: `ABOVE_VALUE (Imbalance)` | Session Bias: **`BULLISH (Above Pivot)`** | Market Regime: `RANGE_EXPANSION`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`103.28` | POC=`102.40` | VAL=`101.64`
  * Prior Day Extremes: PDH=`104.23` | PDL=`100.44` | PDC=`102.65`
  * Monday Range Blueprint: High=`103.88` | Mid=`102.48` | Low=`101.08`
  * Developing Weekly Value Area: Weekly VAH=`103.00` | Weekly POC=`102.03` | Weekly VAL=`101.43`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`102.95` | Low=`101.92`
  * London Session (08:00-16:00 UTC): High=`102.75` | Low=`101.25`
  * New York Session (13:00-21:00 UTC): High=`102.75` | Low=`100.46`
  * Initial Balance (First Hour): IB High=`102.04` | IB Low=`101.67`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `102.51` - `103.33`
  * Optimal Trade Entry (OTE 0.705): `103.13`
  * Structural Invalidation Anchor (0.786): `103.75`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `101.57` | `101.65` | `101.47` | `101.61` | `538` | 54,665.10 USD | 21,258.65 USD | `+38.89%` | -106,639.90 USD | `+0.44` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `5m` | `101.60` | `101.87` | `101.57` | `101.86` | `687` | 69,976.45 USD | 61,812.53 USD | `+88.33%` | -44,827.38 USD | `+1.63` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `5m` | `101.87` | `101.88` | `101.75` | `101.81` | `487` | 49,580.50 USD | -14,874.15 USD | `-30.00%` | -59,701.53 USD | `-1.00` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `101.36` | `101.69` | `101.32` | `101.52` | `1,669` | 169,441.89 USD | 46,939.98 USD | `+27.70%` | -133,778.07 USD | `+0.49` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `101.53` | `101.87` | `101.46` | `101.86` | `1,646` | 167,658.27 USD | 145,167.52 USD | `+86.59%` | 11,389.46 USD | `+1.34` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `101.87` | `101.88` | `101.58` | `101.70` | `1,364` | 138,716.07 USD | -53,174.49 USD | `-38.33%` | -41,785.04 USD | `-0.43` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `1h` | `101.16` | `101.85` | `100.81` | `100.95` | `8,946` | 903,080.81 USD | -425,750.58 USD | `-47.14%` | -1,764,218.73 USD | `-1.35` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `1h` | `100.94` | `101.53` | `100.68` | `101.35` | `7,439` | 753,964.97 USD | 405,912.66 USD | `+53.84%` | -1,358,306.06 USD | `+1.75` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `1h` | `101.36` | `102.01` | `101.32` | `101.98` | `5,786` | 590,044.71 USD | 528,493.28 USD | `+89.57%` | -829,812.78 USD | `+1.93` | **`BULLISH`** | `AGGRESSIVE BUYING` |
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
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 01:03:14 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `39` | `0x0cc1...c7cb` | `LONG` | 30,743,523.56 USD | `300,817.26` | `98.89` | `102.20` | `32.24` | 994,022.53 USD | `+3.23%` | `3X Cross` |
| `112` | `0x30af...393e` | `LONG` | 18,163,988.19 USD | `177,712.44` | `100.98` | `102.20` | `93.19` | 218,586.30 USD | `+1.20%` | `10X Isolated` |
| `161` | `0x58f0...0d20` | `SHORT` | 12,903,824.53 USD | `126,260.51` | `96.77` | `102.20` | `104.20` | -685,732.11 USD | `-5.31%` | `20X Cross` |
| `219` | `0x9e2c...5508` | `LONG` | 10,221,000.00 USD | `100,000.00` | `100.89` | `102.20` | `78.95` | 131,761.86 USD | `+1.29%` | `20X Cross` |
| `235` | `0xebe1...4070` | `LONG` | 9,914,365.91 USD | `96,999.96` | `101.87` | `102.20` | `0.000000` | 32,848.12 USD | `+0.33%` | `20X Cross` |
| `306` | `0x7fda...17d1` | `SHORT` | 8,050,366.74 USD | `78,763.01` | `100.15` | `102.20` | `210.91` | -162,184.88 USD | `-2.01%` | `20X Cross` |
| `344` | `0x10e1...f4bd` | `LONG` | 6,912,040.89 USD | `67,625.88` | `84.36` | `102.20` | `58.54` | 1,206,810.51 USD | `+17.46%` | `3X Isolated` |
| `378` | `0x4692...164f` | `SHORT` | 6,382,984.86 USD | `62,449.71` | `101.56` | `102.20` | `1034.27` | -40,787.83 USD | `-0.64%` | `5X Cross` |
| `409` | `0x0c4a...1b19` | `SHORT` | 5,703,618.80 USD | `55,802.94` | `102.08` | `102.20` | `106.83` | -6,971.42 USD | `-0.12%` | `20X Isolated` |
| `419` | `0xea00...a918` | `SHORT` | 5,636,461.33 USD | `55,151.29` | `89.22` | `102.20` | `274.06` | -715,736.83 USD | `-12.70%` | `20X Cross` |
| `553` | `0x5989...bc29` | `SHORT` | 4,148,473.68 USD | `40,591.72` | `99.23` | `102.20` | `111.59` | -120,539.00 USD | `-2.91%` | `10X Cross` |
| `566` | `0xd507...c948` | `LONG` | 4,068,826.48 USD | `39,808.50` | `93.57` | `102.20` | `81.35` | 343,751.07 USD | `+8.45%` | `7X Isolated` |
| `739` | `0xb5e7...eff1` | `SHORT` | 3,182,031.16 USD | `31,132.29` | `91.71` | `102.20` | `145.23` | -326,822.51 USD | `-10.27%` | `20X Cross` |
| `769` | `0xd84a...c8a5` | `SHORT` | 3,066,300.00 USD | `30,000.00` | `101.76` | `102.20` | `126.31` | -13,450.00 USD | `-0.44%` | `20X Cross` |
| `818` | `0x61d7...7dee` | `LONG` | 2,847,096.29 USD | `27,858.08` | `88.25` | `102.20` | `83.51` | 388,620.29 USD | `+13.65%` | `20X Cross` |
| `860` | `0x354b...6425` | `SHORT` | 2,659,782.62 USD | `26,022.72` | `101.24` | `102.20` | `520.89` | -25,337.00 USD | `-0.95%` | `8X Cross` |
| `897` | `0xf0ae...2f74` | `SHORT` | 2,555,250.00 USD | `25,000.00` | `100.78` | `102.20` | `173.61` | -35,731.39 USD | `-1.40%` | `20X Cross` |
| `917` | `0xb8f3...04ea` | `SHORT` | 2,510,309.90 USD | `24,560.32` | `102.91` | `102.20` | `114.78` | 17,197.09 USD | `+0.69%` | `7X Isolated` |
| `923` | `0x645b...87b8` | `SHORT` | 2,483,750.66 USD | `24,302.84` | `101.22` | `102.20` | `134.77` | -23,789.10 USD | `-0.96%` | `3X Isolated` |
| `1098` | `0xfc66...ca06` | `SHORT` | 2,061,781.86 USD | `20,172.02` | `101.16` | `102.20` | `2155.39` | -21,263.67 USD | `-1.03%` | `3X Cross` |
| `1122` | `0x9aa5...58af` | `SHORT` | 2,010,572.91 USD | `19,671.00` | `101.76` | `102.20` | `489.47` | -8,821.98 USD | `-0.44%` | `20X Cross` |
| `1301` | `0x4169...6f06` | `LONG` | 1,755,476.17 USD | `17,175.19` | `76.61` | `102.20` | `82.99` | 439,708.17 USD | `+25.05%` | `12X Isolated` |
| `1316` | `0x6788...98d4` | `SHORT` | 1,737,400.00 USD | `17,000.00` | `99.31` | `102.20` | `192.36` | -49,075.41 USD | `-2.82%` | `20X Cross` |
| `1320` | `0xe1d3...7766` | `SHORT` | 1,732,763.80 USD | `16,954.64` | `102.20` | `102.20` | `159.64` | -43.62 USD | `-0.00%` | `20X Cross` |
| `1382` | `0xa99c...40d5` | `SHORT` | 1,645,420.00 USD | `16,100.00` | `101.02` | `102.20` | `156.69` | -18,962.63 USD | `-1.15%` | `20X Cross` |
| `1392` | `0x1bf6...5bfa` | `SHORT` | 1,635,200.00 USD | `16,000.00` | `99.60` | `102.20` | `224.19` | -41,577.69 USD | `-2.54%` | `20X Cross` |
| `1395` | `0xfdfb...dbb9` | `SHORT` | 1,631,796.64 USD | `15,966.70` | `101.16` | `102.20` | `107.42` | -16,567.13 USD | `-1.02%` | `20X Cross` |
| `1482` | `0x17c3...a868` | `LONG` | 1,534,116.53 USD | `15,010.92` | `95.13` | `102.20` | `64.99` | 106,060.47 USD | `+6.91%` | `3X Isolated` |
| `1483` | `0x34ea...2f47` | `SHORT` | 1,533,000.00 USD | `15,000.00` | `99.80` | `102.20` | `193.20` | -35,998.69 USD | `-2.35%` | `20X Cross` |
| `1589` | `0xfb29...21dd` | `LONG` | 1,404,691.07 USD | `13,744.53` | `89.85` | `102.20` | `84.59` | 169,697.11 USD | `+12.08%` | `20X Cross` |
| `1611` | `0x5d6f...6f8a` | `LONG` | 1,379,835.00 USD | `13,500.00` | `101.84` | `102.20` | `21.54` | 5,030.00 USD | `+0.36%` | `20X Cross` |
| `1612` | `0x6fa6...825e` | `SHORT` | 1,379,700.00 USD | `13,500.00` | `102.95` | `102.20` | `135.50` | 10,074.27 USD | `+0.73%` | `20X Isolated` |
| `1623` | `0xa9d9...b48e` | `SHORT` | 1,362,799.97 USD | `13,333.33` | `96.39` | `102.20` | `175.44` | -77,552.78 USD | `-5.69%` | `20X Cross` |
| `1729` | `0x89c2...c94b` | `LONG` | 1,263,671.42 USD | `12,364.69` | `75.25` | `102.20` | `45.77` | 333,188.27 USD | `+26.37%` | `3X Isolated` |
| `1735` | `0x91fd...9841` | `LONG` | 1,252,569.13 USD | `12,253.66` | `101.16` | `102.20` | `95.59` | 12,971.78 USD | `+1.04%` | `13X Isolated` |
| `1746` | `0xcd81...36e3` | `SHORT` | 1,232,937.12 USD | `12,063.96` | `97.96` | `102.20` | `111.43` | -51,098.20 USD | `-4.14%` | `20X Cross` |
| `1750` | `0x436c...b3d1` | `SHORT` | 1,226,400.00 USD | `12,000.00` | `101.05` | `102.20` | `203.29` | -13,740.17 USD | `-1.12%` | `20X Cross` |
| `1822` | `0x9dea...d617` | `LONG` | 1,165,161.56 USD | `11,400.80` | `90.37` | `102.20` | `0.000000` | 134,887.83 USD | `+11.58%` | `20X Cross` |
| `1855` | `0x8afa...8113` | `SHORT` | 1,134,703.94 USD | `11,101.69` | `100.52` | `102.20` | `107.79` | -18,759.43 USD | `-1.65%` | `10X Isolated` |
| `1865` | `0x8607...08d5` | `SHORT` | 1,124,006.02 USD | `10,998.10` | `92.18` | `102.20` | `135.03` | -110,216.32 USD | `-9.81%` | `4X Isolated` |
| `1930` | `0xfc27...9d9d` | `LONG` | 1,064,677.60 USD | `10,417.59` | `101.61` | `102.20` | `0.000000` | 6,143.63 USD | `+0.58%` | `20X Cross` |
| `1997` | `0xf29c...9971` | `SHORT` | 1,022,000.00 USD | `10,000.00` | `101.10` | `102.20` | `118.37` | -11,003.97 USD | `-1.08%` | `5X Isolated` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| Intel | Baseline | - | - | - | Neutral | - | No anomalous telegram alerts in current window | - |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`103.09` (Vol: 2,100,000.00 USD, Dist: `+0.86%`) | Long MP=`99.17` (Vol: 6,700,000.00 USD, Dist: `--2.97%`)
  * 48H Horizon: Short MP=`104.04` (Vol: 5,700,000.00 USD, Dist: `+1.79%`) | Long MP=`99.17` (Vol: 4,000,000.00 USD, Dist: `--2.98%`)
  * 3D Horizon: Short MP=`104.04` (Vol: 5,700,000.00 USD, Dist: `+1.79%`) | Long MP=`99.25` (Vol: 9,800,000.00 USD, Dist: `--2.90%`)
  * 7D Horizon: Short MP=`103.98` (Vol: 10,300,000.00 USD, Dist: `+1.73%`) | Long MP=`99.25` (Vol: 12,300,000.00 USD, Dist: `--2.90%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Envelope` | `Long Liquidation` | `101.91` | 25,000,000.00 USD | 50,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 4 Macro Envelope` |
| `Envelope` | `Short Liquidation` | `103.96` | 25,000,000.00 USD | 50,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 4 Macro Envelope` |

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
  * Current Rate: `-44.66K` | Last 24h: `-97.14K` | Last 3d: `-389.48K` | Last 7d: `-816.28K`
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
| `18:50:00` | `101.32` | `101.32` | `101.32` | `101.34` | `101.10` | 65,654.06 USD | 57,033.52 USD | 8,620.54 USD | 48,412.98 USD | `+73.74%` | `1B / 0S` |
| `18:55:00` | `101.35` | `101.35` | `101.35` | `101.53` | `101.27` | 48,852.15 USD | 21,607.68 USD | 27,244.47 USD | -5,636.79 USD | `-11.54%` | `0B / 1S` |
| `19:00:00` | `101.61` | `101.61` | `101.61` | `101.63` | `101.32` | 67,368.76 USD | 62,587.75 USD | 4,781.01 USD | 57,806.74 USD | `+85.81%` | `1B / 0S` |
| `19:00:00` | `101.98` | `101.98` | `101.98` | `102.01` | `101.32` | 590,044.71 USD | 559,268.99 USD | 30,775.71 USD | 528,493.28 USD | `+89.57%` | `1B / 0S` |
| `19:00:00` | `101.52` | `101.52` | `101.52` | `101.69` | `101.32` | 169,441.89 USD | 108,190.93 USD | 61,250.95 USD | 46,939.98 USD | `+27.70%` | `1B / 0S` |
| `19:05:00` | `101.60` | `101.60` | `101.60` | `101.69` | `101.47` | 52,729.36 USD | 28,521.79 USD | 24,207.57 USD | 4,314.22 USD | `+8.18%` | `1B / 0S` |
| `19:10:00` | `101.52` | `101.52` | `101.52` | `101.61` | `101.39` | 49,441.70 USD | 23,878.09 USD | 25,563.61 USD | -1,685.51 USD | `-3.41%` | `0B / 1S` |
| `19:15:00` | `101.58` | `101.58` | `101.58` | `101.61` | `101.46` | 42,764.34 USD | 31,335.94 USD | 11,428.40 USD | 19,907.54 USD | `+46.55%` | `1B / 0S` |
| `19:15:00` | `101.86` | `101.86` | `101.86` | `101.87` | `101.46` | 167,658.27 USD | 156,412.90 USD | 11,245.37 USD | 145,167.52 USD | `+86.59%` | `1B / 0S` |
| `19:20:00` | `101.61` | `101.61` | `101.61` | `101.65` | `101.47` | 54,665.10 USD | 37,961.88 USD | 16,703.23 USD | 21,258.65 USD | `+38.89%` | `1B / 0S` |
| `5:00 UTC` | `101.68` | `101.64` | `101.68` | `101.91` | `101.38` | 9,829,156.63 USD | 4,338,777.97 USD | 5,490,378.67 USD | -1,151,600.70 USD | `-11.72%` | `10B / 10S` |
| `0:00 UTC` | `102.41` | `102.23` | `102.41` | `102.50` | `101.82` | 76,189,579.98 USD | 39,225,207.15 USD | 36,964,372.83 USD | 2,260,834.33 USD | `+2.97%` | `20B / 3S` |
| `5:00 UTC` | `102.02` | `102.01` | `102.02` | `102.13` | `101.85` | 13,174,401.35 USD | 6,982,040.79 USD | 6,192,360.55 USD | 789,680.24 USD | `+5.99%` | `1B / 6S` |
| `0:00 UTC` | `101.95` | `101.91` | `101.95` | `102.02` | `101.77` | 7,849,002.75 USD | 3,456,195.71 USD | 4,392,807.03 USD | -936,611.32 USD | `-11.93%` | `2B / 3S` |
| `5:00 UTC` | `102.00` | `102.03` | `102.00` | `102.18` | `101.80` | 13,778,364.28 USD | 6,276,241.74 USD | 7,502,122.54 USD | -1,225,880.80 USD | `-8.90%` | `6B / 5S` |
| `0:00 UTC` | `102.25` | `102.23` | `102.25` | `102.41` | `102.00` | 12,832,227.15 USD | 6,368,450.04 USD | 6,463,777.11 USD | -95,327.07 USD | `-0.74%` | `9B / 6S` |
| `5:00 UTC` | `102.22` | `102.29` | `102.22` | `102.44` | `102.12` | 5,679,150.43 USD | 2,485,492.20 USD | 3,193,658.23 USD | -708,166.03 USD | `-12.47%` | `5B / 11S` |
| `0:00 UTC` | `102.37` | `102.32` | `102.37` | `102.44` | `102.16` | 7,394,503.21 USD | 3,870,700.86 USD | 3,523,802.35 USD | 346,898.52 USD | `+4.69%` | `5B / 3S` |
| `5:00 UTC` | `102.37` | `102.38` | `102.37` | `102.44` | `102.30` | 4,333,204.12 USD | 1,824,676.12 USD | 2,508,528.00 USD | -683,851.88 USD | `-15.78%` | `1B / 3S` |
| `0:00 UTC` | `102.38` | `102.38` | `102.38` | `102.38` | `102.38` | 20.48 USD | 0.00 USD | 20.48 USD | -20.48 USD | `-100.00%` | `0B / 0S` |

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
  * `2026-10-30 00:57:49 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 00:47:49 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 00:16:49 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 00:58:49 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 00:58:49 IST`: [@DeItaone] - (Sentiment: `Neutral`)
  * `2026-10-30 00:58:49 IST`: [@mb_ghalibaf] - (Sentiment: `Neutral`)
  * `2026-10-30 00:58:49 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-30 00:57:49 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-30 00:57:49 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-30 00:57:49 IST`: [fxstreet.com] - (Sentiment: `Neutral`)
  * `2026-10-29 21:59:49 IST`: [ForexFactory] - (Sentiment: `Neutral`)
  * `2026-10-29 21:59:49 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-29 21:59:49 IST`: [youtube.com/bankofcanadaofficial] - (Sentiment: `Neutral`)
  * `2026-10-29 20:59:49 IST`: [notayesmanseconomics.wordpress.com] - (Sentiment: `Neutral`)
  * `2026-10-29 20:59:49 IST`: [think.ing.com] - (Sentiment: `Neutral`)


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
  * Execution Entry: `101.51` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `100.24` (Risk Distance: `1.27` pts)
  * +2.5R Take Profit: `104.68`
  * Mathematical Lot Sizing: **`0.10 lots`** (Nominal Risk = `1.27 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `102.76` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `104.03` (Risk Distance: `1.27` pts)
  * +2.5R Take Profit: `99.59`
  * Mathematical Lot Sizing: **`0.10 lots`** (Nominal Risk = `1.27 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`PASSIVE_MAKER_LIMIT_ARMED`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`103.75`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
