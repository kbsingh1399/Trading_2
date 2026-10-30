# 🏛️ SOVEREIGN CANDIDATE DOSSIER: ZECUSD
**Canonical Key**: `ZECUSD` | **Broker Instrument**: `ZECUSD.p` | **Asset Class**: `Crypto Altcoin`
**Timestamp**: `2026-10-30 15:27:10 IST` (`2026-10-30 09:57:10 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `1247.51` | **Live Ask Quote**: `1248.39` | **Mid Price**: `1247.95`
- **Spread Points**: `88.00` | **Spread BPS**: `7.05 bps` (Charter Threshold: `25.00 bps`)
- **Gate 1 Clearance**: **`PASS`** | **Execution Posture**: `PASSIVE LIMIT ONLY` | **Order Type Allowed**: `BUY_LIMIT / SELL_LIMIT`
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
  * Session VWAP: `1253.52` | VWAP Z-Score: `-0.31` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `11.94` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `42.41` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `1317.10` | Lower -3.00σ Band: `1189.95`
  * Upper +2.51σ Band: `1306.71` | Lower -2.51σ Band: `1200.34`
  * Upper +2.01σ Band: `1296.12` | Lower -2.01σ Band: `1210.93`
  * Upper +2.00σ Band: `1295.91` | Lower -2.00σ Band: `1211.14`
  * Upper +1.28σ Band: `1280.65` | Lower -1.28σ Band: `1226.40`
  * Upper +1.00σ Band: `1274.72` | Lower -1.00σ Band: `1232.33`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`1249.63` | EMA-20=`1255.34` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`1261.97` (Slope: `+0.0000`) | EMA-100=`1268.22`
  * Institutional Anchors: EMA-144=`1271.46` | EMA-200=`1275.82` (Slope: `-0.2396`) | EMA-233=`1276.27`
- **Range Boundaries**: 24H High=`1396.49` | 24H Low=`1180.03` | Weekly High=`1396.49` | Weekly Low=`1180.03`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `1279.38` (Distance: `-2.39%`)
  * Point of Control (POC) = `1247.68` (Distance: `+0.09%`)
  * Value Area Low (VAL) = `1237.63` (Distance: `+0.91%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`1309.91` | POC=`1246.71` | VAL=`1230.27`
  * Prior Day Extremes: PDH=`1396.49` | PDL=`1206.89` | PDC=`1244.38`
  * Monday Range Blueprint: High=`1267.53` | Mid=`1222.14` | Low=`1176.75`
  * Developing Weekly Value Area: Weekly VAH=`1293.21` | Weekly POC=`1240.47` | Weekly VAL=`1200.92`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`1296.00` | Low=`1180.03`
  * London Session (08:00-16:00 UTC): High=`1283.82` | Low=`1239.95`
  * New York Session (13:00-21:00 UTC): High=`1255.44` | Low=`1240.46`
  * Initial Balance (First Hour): IB High=`1283.82` | IB Low=`1264.92`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `1242.96` - `1252.94`
  * Optimal Trade Entry (OTE 0.705): `1250.45`
  * Structural Invalidation Anchor (0.786): `1257.93`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `15m` | - | - | - | - | - | 0.00 USD | 0.00 USD | `+0.00%` | 0.00 USD | `0.00` | **`BALANCED`** | Interbank Volume |

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
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 15:20:42 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `12` | `0xb83d...6e36` | `SHORT` | 65,413,736.39 USD | `52,385.47` | `1336.45` | `1249.30` | `3380.02` | 4,596,831.01 USD | `+7.03%` | `3X Cross` |
| `21` | `0x5b5d...c060` | `SHORT` | 50,079,506.52 USD | `40,121.38` | `1478.36` | `1249.30` | `4842.40` | 9,234,528.60 USD | `+18.44%` | `3X Cross` |
| `36` | `0x7fda...17d1` | `SHORT` | 33,216,811.31 USD | `26,611.77` | `1262.59` | `1249.30` | `2621.69` | 382,813.81 USD | `+1.15%` | `5X Cross` |
| `82` | `0x60b0...991e` | `LONG` | 20,946,149.44 USD | `16,779.74` | `1179.65` | `1249.30` | `915.83` | 1,151,902.43 USD | `+5.50%` | `10X Cross` |
| `140` | `0xc36a...105b` | `LONG` | 14,367,805.52 USD | `11,510.82` | `1215.14` | `1249.30` | `967.78` | 380,524.50 USD | `+2.65%` | `10X Cross` |
| `178` | `0x8742...8427` | `LONG` | 11,493,231.41 USD | `9,201.21` | `1286.37` | `1249.30` | `712.71` | -342,938.58 USD | `-2.98%` | `10X Cross` |
| `192` | `0x58b2...11f3` | `LONG` | 10,688,436.46 USD | `8,563.08` | `1246.56` | `1249.30` | `385.66` | 14,018.88 USD | `+0.13%` | `10X Cross` |
| `193` | `0x9071...5c0b` | `LONG` | 10,640,612.92 USD | `8,517.29` | `1353.83` | `1249.30` | `102.53` | -890,346.68 USD | `-8.37%` | `2X Cross` |
| `194` | `0x9ffd...ce40` | `LONG` | 10,633,752.81 USD | `8,519.27` | `1252.16` | `1249.30` | `605.87` | -33,763.12 USD | `-0.32%` | `5X Cross` |
| `199` | `0xad59...ba81` | `SHORT` | 10,518,612.50 USD | `8,425.00` | `330.91` | `1249.30` | `2147.94` | -7,730,654.73 USD | `-73.50%` | `10X Cross` |
| `204` | `0xdd53...2b13` | `SHORT` | 10,237,737.59 USD | `8,195.92` | `741.54` | `1249.30` | `8463.84` | -4,160,141.22 USD | `-40.64%` | `3X Cross` |
| `225` | `0x880a...311c` | `SHORT` | 9,620,014.70 USD | `7,707.11` | `1367.50` | `1249.30` | `2235.44` | 919,469.50 USD | `+9.56%` | `10X Cross` |
| `237` | `0xbf73...5d58` | `LONG` | 9,361,500.00 USD | `7,500.00` | `1248.78` | `1249.30` | `145.35` | -4,345.62 USD | `-0.05%` | `10X Cross` |
| `271` | `0x2b61...2f6c` | `LONG` | 8,496,497.40 USD | `6,807.00` | `1453.56` | `1249.30` | `558.21` | -1,397,853.82 USD | `-16.45%` | `10X Cross` |
| `290` | `0x2ae5...83e7` | `LONG` | 8,041,465.92 USD | `6,436.80` | `1391.82` | `1249.30` | `0.000000` | -917,426.07 USD | `-11.41%` | `1X Cross` |
| `325` | `0xecb6...2b00` | `SHORT` | 7,064,091.84 USD | `5,660.33` | `1278.08` | `1249.30` | `6541.68` | 170,275.76 USD | `+2.41%` | `5X Cross` |
| `334` | `0x26b6...9a13` | `LONG` | 6,788,902.26 USD | `5,433.73` | `1282.23` | `1249.30` | `229.48` | -178,400.97 USD | `-2.63%` | `10X Cross` |
| `353` | `0x45d2...4029` | `SHORT` | 6,530,091.10 USD | `5,227.00` | `833.44` | `1249.30` | `9128.51` | -2,173,713.13 USD | `-33.29%` | `5X Cross` |
| `368` | `0xea00...a918` | `LONG` | 6,241,500.00 USD | `5,000.00` | `739.16` | `1249.30` | `0.000000` | 2,545,684.89 USD | `+40.79%` | `5X Cross` |
| `379` | `0xdd7a...8830` | `LONG` | 6,069,707.09 USD | `4,860.19` | `897.48` | `1249.30` | `787.96` | 1,707,803.42 USD | `+28.14%` | `10X Cross` |
| `422` | `0x469e...58a5` | `SHORT` | 5,196,905.66 USD | `4,163.52` | `1242.31` | `1249.30` | `1951.24` | -24,521.01 USD | `-0.47%` | `10X Cross` |
| `436` | `0x4cae...7c34` | `LONG` | 4,995,633.41 USD | `4,002.27` | `1169.72` | `1249.30` | `975.95` | 314,084.07 USD | `+6.29%` | `10X Cross` |
| `442` | `0xd4c1...3d1d` | `SHORT` | 4,902,718.08 USD | `3,928.46` | `1291.68` | `1249.30` | `2369.05` | 171,593.31 USD | `+3.50%` | `10X Cross` |
| `449` | `0x382b...3e39` | `LONG` | 4,856,919.72 USD | `3,891.66` | `1220.36` | `1249.30` | `0.000000` | 107,689.16 USD | `+2.22%` | `10X Cross` |
| `450` | `0xa61c...66b9` | `LONG` | 4,856,538.12 USD | `3,888.00` | `1148.34` | `1249.30` | `0.000000` | 391,795.98 USD | `+8.07%` | `10X Cross` |
| `476` | `0x9aa5...58af` | `SHORT` | 4,643,690.94 USD | `3,720.31` | `1205.51` | `1249.30` | `3705.38` | -158,804.14 USD | `-3.42%` | `10X Cross` |
| `477` | `0x0153...8052` | `SHORT` | 4,622,725.00 USD | `3,698.18` | `1307.82` | `1249.30` | `2504.93` | 213,845.75 USD | `+4.63%` | `1X Isolated` |
| `507` | `0xb122...e4ba` | `LONG` | 4,366,205.66 USD | `3,498.47` | `1265.25` | `1249.30` | `1126.35` | -60,245.87 USD | `-1.38%` | `10X Cross` |
| `544` | `0xd21d...90f1` | `LONG` | 4,057,625.00 USD | `3,250.00` | `1253.64` | `1249.30` | `876.15` | -16,716.73 USD | `-0.41%` | `4X Isolated` |
| `548` | `0x456f...cdf1` | `LONG` | 4,038,400.30 USD | `3,235.12` | `1267.53` | `1249.30` | `518.49` | -62,212.26 USD | `-1.54%` | `10X Cross` |
| `566` | `0x1338...c48e` | `LONG` | 3,930,271.64 USD | `3,149.43` | `1018.52` | `1249.30` | `820.45` | 722,526.10 USD | `+18.38%` | `4X Isolated` |
| `583` | `0xdbe0...d6d5` | `LONG` | 3,856,712.50 USD | `3,085.37` | `422.97` | `1249.30` | `338.76` | 2,551,708.01 USD | `+66.16%` | `3X Isolated` |
| `596` | `0x325e...9564` | `LONG` | 3,748,465.49 USD | `3,000.91` | `1298.07` | `1249.30` | `134.22` | -146,939.67 USD | `-3.92%` | `10X Cross` |
| `599` | `0x2e30...4cb5` | `SHORT` | 3,735,881.73 USD | `2,990.38` | `1282.39` | `1249.30` | `2889.57` | 98,966.90 USD | `+2.65%` | `2X Cross` |
| `604` | `0x9c06...0560` | `SHORT` | 3,731,868.36 USD | `2,989.80` | `786.00` | `1249.30` | `2575.08` | -1,381,873.36 USD | `-37.03%` | `10X Cross` |
| `612` | `0x27c9...d65d` | `SHORT` | 3,667,555.33 USD | `2,938.04` | `1254.41` | `1249.30` | `1741.86` | 17,954.71 USD | `+0.49%` | `10X Cross` |
| `710` | `0xa183...0482` | `LONG` | 3,165,219.40 USD | `2,534.00` | `530.25` | `1249.30` | `444.69` | 1,821,556.68 USD | `+57.55%` | `5X Isolated` |
| `711` | `0xac48...3201` | `LONG` | 3,160,071.45 USD | `2,531.50` | `1378.58` | `1249.30` | `538.08` | -329,800.83 USD | `-10.44%` | `10X Cross` |
| `719` | `0x0871...e927` | `LONG` | 3,120,500.00 USD | `2,500.00` | `1276.50` | `1249.30` | `0.000000` | -70,750.00 USD | `-2.27%` | `10X Cross` |
| `744` | `0x9b86...6e6e` | `LONG` | 3,075,430.05 USD | `2,463.30` | `637.58` | `1249.30` | `882.62` | 1,504,880.77 USD | `+48.93%` | `3X Cross` |
| `818` | `0xf48f...10fe` | `LONG` | 2,770,228.46 USD | `2,218.49` | `1517.87` | `1249.30` | `979.31` | -597,158.36 USD | `-21.56%` | `3X Cross` |
| `845` | `0x5bc4...3b0c` | `SHORT` | 2,661,507.33 USD | `2,130.74` | `1089.65` | `1249.30` | `3681.69` | -339,749.76 USD | `-12.77%` | `5X Cross` |
| `861` | `0x8de4...b9aa` | `SHORT` | 2,610,348.18 USD | `2,091.29` | `1331.35` | `1249.30` | `1690.05` | 173,891.53 USD | `+6.66%` | `3X Cross` |
| `867` | `0x4fe2...ac59` | `SHORT` | 2,585,387.51 USD | `2,071.57` | `1478.56` | `1249.30` | `1853.68` | 477,558.70 USD | `+18.47%` | `10X Cross` |
| `870` | `0xdf57...93f5` | `LONG` | 2,565,883.15 USD | `2,054.35` | `1227.36` | `1249.30` | `897.39` | 44,461.11 USD | `+1.73%` | `4X Isolated` |
| `876` | `0xbcd4...0dd2` | `LONG` | 2,538,332.16 USD | `2,033.92` | `1228.20` | `1249.30` | `766.50` | 40,281.35 USD | `+1.59%` | `10X Cross` |
| `886` | `0x71d0...8c26` | `SHORT` | 2,505,684.48 USD | `2,007.76` | `1266.91` | `1249.30` | `3985.65` | 37,958.47 USD | `+1.51%` | `10X Cross` |
| `890` | `0xf29c...9971` | `LONG` | 2,498,200.00 USD | `2,000.00` | `1254.95` | `1249.30` | `0.000000` | -11,697.07 USD | `-0.47%` | `10X Cross` |
| `892` | `0x9a99...d21a` | `LONG` | 2,496,065.80 USD | `2,000.00` | `1278.44` | `1249.30` | `0.000000` | -60,807.87 USD | `-2.44%` | `10X Cross` |
| `913` | `0x77ee...2902` | `SHORT` | 2,429,034.65 USD | `1,946.03` | `759.84` | `1249.30` | `5744.79` | -950,357.14 USD | `-39.12%` | `10X Cross` |
| `919` | `0x3e2f...b269` | `SHORT` | 2,404,961.99 USD | `1,925.51` | `1134.87` | `1249.30` | `2977.33` | -219,763.13 USD | `-9.14%` | `10X Cross` |
| `934` | `0x4f12...618b` | `SHORT` | 2,366,936.70 USD | `1,896.28` | `1608.30` | `1249.30` | `2116.94` | 682,847.69 USD | `+28.85%` | `3X Cross` |
| `977` | `0x866d...d6e1` | `LONG` | 2,249,318.81 USD | `1,802.05` | `674.73` | `1249.30` | `134.45` | 1,033,417.50 USD | `+45.94%` | `10X Cross` |
| `1002` | `0x2309...a2d9` | `LONG` | 2,184,811.83 USD | `1,750.37` | `1186.09` | `1249.30` | `807.00` | 108,717.72 USD | `+4.98%` | `8X Cross` |
| `1047` | `0x265e...7f70` | `LONG` | 2,061,701.87 USD | `1,651.74` | `1382.98` | `1249.30` | `0.000000` | -222,620.89 USD | `-10.80%` | `3X Cross` |
| `1052` | `0xfe7c...b7ae` | `SHORT` | 2,050,507.51 USD | `1,642.64` | `1346.92` | `1249.30` | `5741.58` | 162,001.11 USD | `+7.90%` | `10X Cross` |
| `1057` | `0x3e47...aaf6` | `LONG` | 2,042,632.14 USD | `1,636.28` | `1278.38` | `1249.30` | `1052.44` | -49,159.65 USD | `-2.41%` | `10X Cross` |
| `1060` | `0x2edd...8179` | `SHORT` | 2,041,703.04 USD | `1,635.98` | `1261.55` | `1249.30` | `2882.12` | 22,159.84 USD | `+1.09%` | `10X Cross` |
| `1081` | `0x7f75...9edf` | `LONG` | 2,012,310.59 USD | `1,612.17` | `1200.26` | `1249.30` | `987.04` | 77,289.51 USD | `+3.84%` | `10X Cross` |
| `1089` | `0x6646...6de5` | `SHORT` | 1,996,800.00 USD | `1,600.00` | `660.64` | `1249.30` | `4212.77` | -939,775.03 USD | `-47.06%` | `10X Cross` |
| `1091` | `0x023a...2355` | `SHORT` | 1,987,720.60 USD | `1,591.31` | `1310.00` | `1249.30` | `4443.33` | 96,888.65 USD | `+4.87%` | `10X Cross` |
| `1101` | `0xfc27...9d9d` | `SHORT` | 1,971,471.56 USD | `1,578.44` | `1295.79` | `1249.30` | `12993.98` | 73,852.65 USD | `+3.75%` | `10X Cross` |
| `1113` | `0xab59...59b5` | `LONG` | 1,954,050.00 USD | `1,565.32` | `1342.15` | `1249.30` | `838.58` | -146,845.21 USD | `-7.51%` | `10X Cross` |
| `1161` | `0x039c...0ebd` | `SHORT` | 1,898,694.72 USD | `1,521.39` | `1245.17` | `1249.30` | `3734.94` | -4,300.86 USD | `-0.23%` | `10X Cross` |
| `1173` | `0xcf67...eb24` | `LONG` | 1,872,049.35 USD | `1,500.00` | `887.05` | `1249.30` | `616.56` | 541,477.98 USD | `+28.92%` | `10X Cross` |
| `1187` | `0x7277...0b98` | `SHORT` | 1,843,039.20 USD | `1,475.73` | `1287.86` | `1249.30` | `2194.11` | 57,492.93 USD | `+3.12%` | `10X Cross` |
| `1252` | `0x2ab7...c2f8` | `LONG` | 1,749,431.80 USD | `1,400.51` | `813.26` | `1249.30` | `793.38` | 610,450.11 USD | `+34.89%` | `3X Cross` |
| `1269` | `0x11be...8b1d` | `LONG` | 1,717,448.59 USD | `1,375.83` | `1206.55` | `1249.30` | `1134.67` | 57,440.63 USD | `+3.34%` | `10X Isolated` |
| `1347` | `0x3205...40bb` | `SHORT` | 1,591,524.06 USD | `1,274.11` | `1257.43` | `1249.30` | `2420.87` | 10,578.02 USD | `+0.66%` | `10X Cross` |
| `1358` | `0xe065...0f85` | `SHORT` | 1,575,778.82 USD | `1,262.61` | `1087.02` | `1249.30` | `1541.81` | -203,302.69 USD | `-12.90%` | `10X Cross` |
| `1373` | `0x413c...886c` | `LONG` | 1,560,423.75 USD | `1,250.00` | `1237.51` | `1249.30` | `0.000000` | 13,534.29 USD | `+0.87%` | `10X Cross` |
| `1378` | `0xdf83...3cff` | `SHORT` | 1,558,377.60 USD | `1,248.00` | `1260.55` | `1249.30` | `1851.92` | 14,792.70 USD | `+0.95%` | `10X Cross` |
| `1437` | `0x2847...d47b` | `LONG` | 1,512,456.42 USD | `1,211.71` | `1232.45` | `1249.30` | `0.000000` | 19,088.82 USD | `+1.26%` | `5X Cross` |
| `1446` | `0x5975...9abd` | `LONG` | 1,497,960.00 USD | `1,200.00` | `1179.54` | `1249.30` | `557.75` | 82,517.21 USD | `+5.51%` | `5X Cross` |
| `1447` | `0x266b...efcb` | `LONG` | 1,497,600.00 USD | `1,200.00` | `893.76` | `1249.30` | `426.84` | 425,090.30 USD | `+28.38%` | `10X Cross` |
| `1478` | `0x69cc...14fd` | `SHORT` | 1,449,957.96 USD | `1,161.36` | `675.33` | `1249.30` | `8137.83` | -665,652.43 USD | `-45.91%` | `10X Cross` |
| `1491` | `0x3fc5...c0c1` | `SHORT` | 1,433,642.44 USD | `1,148.44` | `1264.34` | `1249.30` | `2790.16` | 18,371.33 USD | `+1.28%` | `10X Cross` |
| `1535` | `0x5f94...4b96` | `LONG` | 1,392,637.65 USD | `1,115.27` | `538.00` | `1249.30` | `0.000000` | 792,620.01 USD | `+56.92%` | `10X Cross` |
| `1542` | `0xe35c...a1d3` | `LONG` | 1,388,210.45 USD | `1,111.36` | `1311.66` | `1249.30` | `690.96` | -69,513.70 USD | `-5.01%` | `2X Isolated` |
| `1562` | `0x71df...a23d` | `SHORT` | 1,370,873.10 USD | `1,098.28` | `513.50` | `1249.30` | `2560.72` | -806,902.91 USD | `-58.86%` | `2X Cross` |
| `1582` | `0xbfc7...80b4` | `SHORT` | 1,341,815.00 USD | `1,075.00` | `558.03` | `1249.30` | `2688.86` | -741,936.27 USD | `-55.29%` | `10X Cross` |
| `1612` | `0x5323...b23c` | `SHORT` | 1,307,379.26 USD | `1,047.16` | `1254.18` | `1249.30` | `6577.16` | 5,947.65 USD | `+0.45%` | `5X Cross` |
| `1619` | `0x123d...3bff` | `SHORT` | 1,303,649.62 USD | `1,044.34` | `519.62` | `1249.30` | `4111.91` | -760,991.41 USD | `-58.37%` | `10X Cross` |
| `1685` | `0xe282...df29` | `LONG` | 1,248,862.10 USD | `1,000.00` | `420.99` | `1249.30` | `809.24` | 827,875.24 USD | `+66.29%` | `10X Cross` |
| `1687` | `0x668c...ea2e` | `SHORT` | 1,248,200.00 USD | `1,000.00` | `1406.98` | `1249.30` | `4212.77` | 158,781.99 USD | `+12.72%` | `10X Cross` |
| `1710` | `0x17f0...094f` | `LONG` | 1,228,603.26 USD | `984.30` | `1287.23` | `1249.30` | `537.02` | -38,416.90 USD | `-3.13%` | `5X Cross` |
| `1725` | `0x51f6...2b39` | `SHORT` | 1,215,136.97 USD | `972.81` | `1299.77` | `1249.30` | `2513.77` | 49,290.73 USD | `+4.06%` | `10X Cross` |
| `1786` | `0x757d...94ba` | `LONG` | 1,155,417.50 USD | `925.00` | `1558.31` | `1249.30` | `0.000000` | -286,023.09 USD | `-24.75%` | `10X Cross` |
| `1829` | `0xb911...5525` | `LONG` | 1,123,470.00 USD | `900.00` | `1294.82` | `1249.30` | `1035.45` | -41,867.82 USD | `-3.73%` | `10X Cross` |
| `1851` | `0xef96...9383` | `SHORT` | 1,107,966.17 USD | `887.77` | `1259.32` | `1249.30` | `5114.83` | 10,020.71 USD | `+0.90%` | `10X Cross` |
| `1878` | `0xcf0a...856f` | `LONG` | 1,087,369.43 USD | `871.15` | `1292.19` | `1249.30` | `1029.02` | -38,325.42 USD | `-3.52%` | `4X Cross` |
| `1894` | `0xdf95...7d72` | `SHORT` | 1,065,051.61 USD | `853.27` | `1074.39` | `1249.30` | `45195.42` | -148,304.17 USD | `-13.92%` | `10X Cross` |
| `1930` | `0xb2f7...af9f` | `SHORT` | 1,037,320.06 USD | `830.72` | `746.63` | `1249.30` | `8185.43` | -417,081.03 USD | `-40.21%` | `10X Cross` |
| `1941` | `0x601c...4f54` | `SHORT` | 1,028,819.36 USD | `824.42` | `615.11` | `1249.30` | `3140.11` | -521,706.61 USD | `-50.71%` | `5X Cross` |
| `1957` | `0xae55...2236` | `LONG` | 1,021,261.67 USD | `817.47` | `1467.80` | `1249.30` | `0.000000` | -178,619.54 USD | `-17.49%` | `10X Cross` |
| `1996` | `0x0f02...5384` | `LONG` | 1,000,211.78 USD | `800.78` | `1290.36` | `1249.30` | `309.54` | -33,082.29 USD | `-3.31%` | `3X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `1251.50` | 3,191.32 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 3.19K USD at 1251.5000 USD [API] | `2026-10-29 01:59:43` |
| `ANNOUNCEMENT` | `INFO` | `1251.50` | 1,151.38 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 1.15K USD at 1251.5000 USD [API] | `2026-10-29 01:59:43` |
| `ANNOUNCEMENT` | `INFO` | `1251.50` | 37.55 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 0.04K USD at 1251.5000 USD [API] | `2026-10-29 01:59:43` |
| `ANNOUNCEMENT` | `INFO` | `1251.50` | 25.03 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 0.03K USD at 1251.5000 USD [API] | `2026-10-29 01:59:43` |
| `ANNOUNCEMENT` | `INFO` | `1251.50` | 87.61 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 0.09K USD at 1251.5000 USD [API] | `2026-10-29 01:59:43` |
| `ANNOUNCEMENT` | `INFO` | `1251.50` | 200.24 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 0.20K USD at 1251.5000 USD [API] | `2026-10-29 01:59:43` |
| `ANNOUNCEMENT` | `INFO` | `1251.50` | 638.26 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 0.64K USD at 1251.5000 USD [API] | `2026-10-29 01:59:43` |
| `ANNOUNCEMENT` | `INFO` | `1251.50` | 47,419.33 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 47.42K USD at 1251.5000 USD [API] | `2026-10-29 01:59:43` |
| `ANNOUNCEMENT` | `INFO` | `1254.20` | 37.63 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 0.04K USD at 1254.2000 USD [API] | `2026-10-29 01:59:40` |
| `ANNOUNCEMENT` | `INFO` | `1254.20` | 12.54 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 0.01K USD at 1254.2000 USD [API] | `2026-10-29 01:59:40` |
| `ANNOUNCEMENT` | `INFO` | `1254.20` | 2,872.12 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 2.87K USD at 1254.2000 USD [API] | `2026-10-29 01:59:40` |
| `ANNOUNCEMENT` | `INFO` | `1254.20` | 50.17 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 0.05K USD at 1254.2000 USD [API] | `2026-10-29 01:59:40` |
| `ANNOUNCEMENT` | `INFO` | `1254.20` | 2,031.80 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 2.03K USD at 1254.2000 USD [API] | `2026-10-29 01:59:40` |
| `ANNOUNCEMENT` | `INFO` | `1254.20` | 1,944.01 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 1.94K USD at 1254.2000 USD [API] | `2026-10-29 01:59:40` |
| `ANNOUNCEMENT` | `INFO` | `1268.60` | 3,247.62 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Long: 3.25K USD at 1268.6000 USD [API] | `2026-10-29 10:47:00` |
| `ANNOUNCEMENT` | `INFO` | `1266.10` | 3,456.45 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Long: 3.46K USD at 1266.1000 USD [API] | `2026-10-29 10:49:57` |
| `ANNOUNCEMENT` | `INFO` | `1241.60` | 24.83 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Long: 0.02K USD at 1241.6000 USD [API] | `2026-10-26 09:56:17` |
| `ANNOUNCEMENT` | `INFO` | `1241.60` | 62.08 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Long: 0.06K USD at 1241.6000 USD [API] | `2026-10-26 09:56:17` |
| `ANNOUNCEMENT` | `INFO` | `1266.50` | 937.21 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Long: 0.94K USD at 1266.5000 USD [API] | `2026-10-29 10:49:57` |
| `ANNOUNCEMENT` | `INFO` | `1267.40` | 1,368.79 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Long: 1.37K USD at 1267.4000 USD [API] | `2026-10-29 10:44:46` |
| `ANNOUNCEMENT` | `INFO` | `1266.40` | 1,139.76 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Long: 1.14K USD at 1266.4000 USD [API] | `2026-10-29 10:49:57` |
| `ANNOUNCEMENT` | `INFO` | `1266.40` | 10,333.82 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Long: 10.33K USD at 1266.4000 USD [API] | `2026-10-29 10:49:57` |
| `ANNOUNCEMENT` | `INFO` | `1266.30` | 1,139.67 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Long: 1.14K USD at 1266.3000 USD [API] | `2026-10-29 10:49:57` |
| `ANNOUNCEMENT` | `INFO` | `1268.60` | 10,491.32 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Long: 10.49K USD at 1268.6000 USD [API] | `2026-10-29 10:47:00` |
| `ANNOUNCEMENT` | `INFO` | `1239.10` | 2,007.34 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 2.01K USD at 1239.1000 USD [API] | `2026-10-29 02:30:54` |
| `ANNOUNCEMENT` | `INFO` | `1266.30` | 7,990.35 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Long: 7.99K USD at 1266.3000 USD [API] | `2026-10-29 10:49:57` |
| `ANNOUNCEMENT` | `INFO` | `1238.40` | 3,987.65 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 3.99K USD at 1238.4000 USD [API] | `2026-10-29 02:30:57` |
| `ANNOUNCEMENT` | `INFO` | `1239.00` | 3,989.58 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 3.99K USD at 1239.0000 USD [API] | `2026-10-29 02:30:54` |
| `ANNOUNCEMENT` | `INFO` | `1248.40` | 37.45 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 0.04K USD at 1248.4000 USD [API] | `2026-10-29 02:05:52` |
| `ANNOUNCEMENT` | `INFO` | `1087.00` | 239.14 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Long: 0.24K USD at 1087.0000 USD [API] | `2026-10-15 02:24:27` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`1404.55` (Vol: 3,000,000.00 USD, Dist: `+12.62%`) | Long MP=`1176.48` (Vol: 3,400,000.00 USD, Dist: `--5.67%`)
  * 48H Horizon: Short MP=`1404.55` (Vol: 3,000,000.00 USD, Dist: `+12.62%`) | Long MP=`1176.48` (Vol: 3,400,000.00 USD, Dist: `--5.67%`)
  * 3D Horizon: Short MP=`1404.55` (Vol: 3,000,000.00 USD, Dist: `+12.62%`) | Long MP=`1176.48` (Vol: 3,400,000.00 USD, Dist: `--5.67%`)
  * 7D Horizon: Short MP=`1404.10` (Vol: 3,000,000.00 USD, Dist: `+12.58%`) | Long MP=`1176.74` (Vol: 4,900,000.00 USD, Dist: `--5.65%`)
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
| `5m` | `BALANCED` | 0.00 USD | 1,750.00 USD | 1,750.00 USD | 1,750.00 USD | `1` | `2026-10-30 09:50:00 UTC - 2026-10-30 09:55:00 UTC` |
| `15m` | `BALANCED` | 0.00 USD | 1,750.00 USD | 1,750.00 USD | 1,750.00 USD | `1` | `2026-10-30 09:45:00 UTC - 2026-10-30 10:00:00 UTC` |
| `1h` | `BALANCED` | 0.00 USD | 1,750.00 USD | 1,750.00 USD | 1,750.00 USD | `1` | `2026-10-30 09:00:00 UTC - 2026-10-30 10:00:00 UTC` |
| `4h` | `BALANCED` | 0.00 USD | 1,750.00 USD | 1,750.00 USD | 1,750.00 USD | `1` | `2026-10-30 08:00:00 UTC - 2026-10-30 12:00:00 UTC` |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `0 USD` | Total OI Tokens: `-`
  * 1h OI Change: `0.00%` | 4h OI Change: `0.00%` | 24h OI Change: `0.00%`
  * Exchange Breakdown: Binance=`-` | Bybit=`-` | OKX=`-` | Hyperliquid=`-`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `84.54K` | Last 24h: `171.90K` | Last 3d: `285.15K` | Last 7d: `847.79K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0100%` | **USDT OKX** | `0.0100%` |
| **USDT Bybit** | `0.0100%` | **USDT KuCoin** | `0.0100%` |
| **USDT MEXC** | `0.0100%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `0.0100%` | **USDT Bitget** | `0.0100%` |
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
| `0:00 UTC` | `1255.05` | `1256.16` | `1255.05` | `1269.15` | `1247.25` | 26,236,011.28 USD | 8,922,234.21 USD | 17,313,777.08 USD | -8,391,542.87 USD | `-31.98%` | `2B / 24S` |
| `5:00 UTC` | `1248.15` | `1248.05` | `1248.15` | `1253.25` | `1244.25` | 21,008,122.73 USD | 11,395,427.09 USD | 9,612,695.64 USD | 1,782,731.45 USD | `+8.49%` | `1B / 0S` |
| `0:00 UTC` | `1245.75` | `1245.57` | `1245.75` | `1250.55` | `1240.05` | 17,224,192.69 USD | 9,235,789.14 USD | 7,988,403.55 USD | 1,247,385.58 USD | `+7.24%` | `1B / 6S` |
| `5:00 UTC` | `1251.45` | `1250.99` | `1251.45` | `1255.05` | `1246.35` | 13,619,576.55 USD | 6,741,413.50 USD | 6,878,163.05 USD | -136,749.55 USD | `-1.00%` | `2B / 0S` |
| `0:00 UTC` | `1249.95` | `1249.10` | `1249.95` | `1253.55` | `1244.55` | 10,263,783.49 USD | 5,117,369.60 USD | 5,146,413.89 USD | -29,044.29 USD | `-0.28%` | `1B / 4S` |
| `5:00 UTC` | `1246.65` | `1246.77` | `1246.65` | `1252.35` | `1243.95` | 13,017,000.97 USD | 7,727,648.32 USD | 5,289,352.64 USD | 2,438,295.68 USD | `+18.73%` | `8B / 5S` |
| `0:00 UTC` | `1244.55` | `1245.81` | `1244.55` | `1249.05` | `1243.65` | 9,717,386.64 USD | 3,914,194.68 USD | 5,803,191.96 USD | -1,888,997.28 USD | `-19.44%` | `0B / 1S` |
| `5:00 UTC` | `1242.15` | `1244.40` | `1242.15` | `1249.35` | `1241.25` | 8,638,502.97 USD | 4,533,952.89 USD | 4,104,550.08 USD | 429,402.82 USD | `+4.97%` | `4B / 2S` |
| `0:00 UTC` | `1251.15` | `1247.35` | `1251.15` | `1251.75` | `1240.05` | 9,977,652.60 USD | 4,992,881.35 USD | 4,984,771.25 USD | 8,110.10 USD | `+0.08%` | `3B / 5S` |
| `5:00 UTC` | `1243.95` | `1247.47` | `1243.95` | `1252.65` | `1243.35` | 11,017,036.23 USD | 6,254,046.22 USD | 4,762,990.01 USD | 1,491,056.21 USD | `+13.53%` | `6B / 2S` |

- **CoinGlass Algorithmic Footprint Signals Table (25_CoinGlass_Footprint_Signals.parquet)**:
| Time | Timeframe | Signal Type | Bias | Headline | Price Level | Absorbed Vol (USD) | Bar Delta (USD) |
|:---:|:---:|:---:|:---:|:---|:---:|:---:|:---:|
| `10-28 20:01` | `Range 5` | `Divergence` | **`BEARISH`** | Rally without taker buying | `1275.90` | 0.00 USD | 0.00 USD |
| `10-28 19:07` | `Range 5` | `Absorption` | **`BEARISH`** | Buying absorbed at the high | `1292.50` | 5,000.00 USD | 0.00 USD |
| `10-28 18:18` | `Range 5` | `Exhaustion` | **`BULLISH`** | Seller exhaustion | `1281.00` | 0.00 USD | 0.00 USD |
| `10-28 18:07` | `Volume 25K ZEC` | `Exhaustion` | **`BULLISH`** | Seller exhaustion | `1284.10` | 0.00 USD | 0.00 USD |
| `10-28 17:42` | `Range 5` | `Divergence` | **`BEARISH`** | Rally without taker buying | `1298.10` | 0.00 USD | 0.00 USD |
| `10-28 17:42` | `Range 5` | `Exhaustion` | **`BULLISH`** | Seller exhaustion | `1288.30` | 0.00 USD | 0.00 USD |
| `10-28 16:40` | `Range 5` | `Exhaustion` | **`BULLISH`** | Seller exhaustion | `1301.20` | 0.00 USD | 0.00 USD |
| `10-28 16:38` | `Volume 25K ZEC` | `Exhaustion` | **`BULLISH`** | Seller exhaustion | `1301.20` | 0.00 USD | 0.00 USD |
| `10-28 12:02` | `Range 5` | `Exhaustion` | **`BULLISH`** | Seller exhaustion | `1304.50` | 0.00 USD | 0.00 USD |
| `10-28 10:02` | `Range 5` | `Absorption` | **`BEARISH`** | Buying absorbed at the high | `1329.60` | 1,200.00 USD | 0.00 USD |
| `10-28 08:34` | `Volume 25K ZEC` | `Absorption` | **`BULLISH`** | Selling absorbed at the low | `1308.00` | 5,000.00 USD | 0.00 USD |
| `10-28 06:52` | `Range 5` | `Absorption` | **`BEARISH`** | Buying absorbed at the high | `1309.20` | 1,800.00 USD | 0.00 USD |
| `10-28 06:52` | `Range 5` | `Trapped longs` | **`BEARISH`** | Failed breakout | `1309.20` | 1,800.00 USD | 0.00 USD |

- **12-Horizon Macro Capital Netflows Table (2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet)**:
| Horizon | Spot Netflow (USD) | Futures Netflow (USD) | Institutional Bias |
|:---:|:---:|:---:|:---:|
| `5m` | 77,710.00 USD | 773,870.00 USD | **`ACCUMULATION`** |
| `15m` | -252,050.00 USD | 1,360,000.00 USD | **`ACCUMULATION`** |
| `30m` | -1,140,000.00 USD | 2,600,000.00 USD | **`ACCUMULATION`** |
| `1h` | -2,410,000.00 USD | 3,630,000.00 USD | **`ACCUMULATION`** |
| `2h` | -639,560.00 USD | 5,450,000.00 USD | **`ACCUMULATION`** |
| `4h` | 646,940.00 USD | -21,300,000.00 USD | **`DISTRIBUTION`** |
| `6h` | -464,610.00 USD | -35,010,000.00 USD | **`DISTRIBUTION`** |
| `8h` | 5,950,000.00 USD | 11,210,000.00 USD | **`ACCUMULATION`** |
| `12h` | -437,140.00 USD | -22,130,000.00 USD | **`DISTRIBUTION`** |
| `24h` | 20,780,000.00 USD | 75,380,000.00 USD | **`ACCUMULATION`** |
| `1w` | 35,230,000.00 USD | 203,420,000.00 USD | **`ACCUMULATION`** |
| `30d` | 62,280,000.00 USD | -542,170,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+77.71K` | 15m=`-252.05K` | 1h=`-2.41M` | 24h=`+20.78M`
* Futures Capital Netflows: 5m=`+773.87K` | 15m=`+1.36M` | 1h=`+3.63M` | 24h=`+75.38M`
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
  * `2026-10-30 15:18:36 IST`: [dailyforex.com] - (Sentiment: `Neutral`)
  * `2026-10-30 15:12:36 IST`: [breakingthenews.net] - (Sentiment: `Neutral`)
  * `2026-10-30 14:41:36 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 14:37:36 IST`: [@FirstSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 14:33:36 IST`: [destatis.de] - (Sentiment: `Neutral`)
  * `2026-10-30 14:32:36 IST`: [istat.it] - (Sentiment: `Neutral`)
  * `2026-10-30 15:25:36 IST`: [channelnewsasia.com] - (Sentiment: `Neutral`)
  * `2026-10-30 15:25:36 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 15:25:36 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 15:25:36 IST`: [kof.ethz.ch] - (Sentiment: `Neutral`)
  * `2026-10-30 15:24:36 IST`: [gerlachmacro.substack.com] - (Sentiment: `Neutral`)
  * `2026-10-30 15:24:36 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-30 15:24:36 IST`: [insee.fr] - (Sentiment: `Neutral`)
  * `2026-10-30 15:24:36 IST`: [insee.fr] - (Sentiment: `Neutral`)
  * `2026-10-30 15:24:36 IST`: [@FirstSquawk] - (Sentiment: `Neutral`)


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
  * Execution Entry: `1237.63` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `1221.98` (Risk Distance: `15.65` pts)
  * +2.5R Take Profit: `1276.75`
  * Mathematical Lot Sizing: **`0.63 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `1279.38` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `1295.03` (Risk Distance: `15.65` pts)
  * +2.5R Take Profit: `1240.26`
  * Mathematical Lot Sizing: **`0.63 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`1257.93`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
