# 🏛️ SOVEREIGN CANDIDATE DOSSIER: ZECUSD
**Canonical Key**: `ZECUSD` | **Broker Instrument**: `ZECUSD.p` | **Asset Class**: `Crypto Altcoin`
**Timestamp**: `2026-10-30 10:52:59 IST` (`2026-10-30 05:22:59 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `1273.90` | **Live Ask Quote**: `1275.42` | **Mid Price**: `1274.66`
- **Spread Points**: `152.00` | **Spread BPS**: `11.92 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `1249.44` | VWAP Z-Score: `+1.07` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `16.88` (Volatility Regime: `HIGH_EXPANSION`)
  * 14-Period RSI: `55.49` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `1325.60` | Lower -3.00σ Band: `1173.28`
  * Upper +2.51σ Band: `1313.16` | Lower -2.51σ Band: `1185.72`
  * Upper +2.01σ Band: `1300.47` | Lower -2.01σ Band: `1198.42`
  * Upper +2.00σ Band: `1300.21` | Lower -2.00σ Band: `1198.67`
  * Upper +1.28σ Band: `1281.94` | Lower -1.28σ Band: `1216.95`
  * Upper +1.00σ Band: `1274.83` | Lower -1.00σ Band: `1224.06`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`1273.98` | EMA-20=`1265.80` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`1268.04` (Slope: `+0.0000`) | EMA-100=`1272.85`
  * Institutional Anchors: EMA-144=`1274.20` | EMA-200=`1275.72` (Slope: `-0.0260`) | EMA-233=`1278.00`
- **Range Boundaries**: 24H High=`1396.49` | 24H Low=`1180.03` | Weekly High=`1396.49` | Weekly Low=`1180.03`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `1273.97` (Distance: `+0.11%`)
  * Point of Control (POC) = `1229.90` (Distance: `+3.70%`)
  * Value Area Low (VAL) = `1222.17` (Distance: `+4.36%`)
  * Auction Positioning: `ABOVE_VALUE (Imbalance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `RANGE_EXPANSION`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`1309.91` | POC=`1246.71` | VAL=`1230.27`
  * Prior Day Extremes: PDH=`1396.49` | PDL=`1206.89` | PDC=`1244.38`
  * Monday Range Blueprint: High=`1267.53` | Mid=`1222.14` | Low=`1176.75`
  * Developing Weekly Value Area: Weekly VAH=`1296.14` | Weekly POC=`1239.01` | Weekly VAL=`1200.92`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`1296.00` | Low=`1180.03`
  * London Session (08:00-16:00 UTC): High=`1283.82` | Low=`1270.11`
  * New York Session (13:00-21:00 UTC): High=`1282.31` | Low=`1267.01`
  * Initial Balance (First Hour): IB High=`1283.82` | IB Low=`1270.11`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `1269.56` - `1279.76`
  * Optimal Trade Entry (OTE 0.705): `1277.21`
  * Structural Invalidation Anchor (0.786): `1284.86`

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
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 10:43:23 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `13` | `0xb83d...6e36` | `SHORT` | 67,090,071.43 USD | `52,385.47` | `1336.45` | `1278.90` | `3657.62` | 2,920,495.97 USD | `+4.35%` | `3X Cross` |
| `22` | `0x5b5d...c060` | `SHORT` | 51,343,329.99 USD | `40,121.38` | `1478.36` | `1278.90` | `5076.88` | 7,970,705.13 USD | `+15.52%` | `3X Cross` |
| `38` | `0x7fda...17d1` | `SHORT` | 33,329,863.39 USD | `26,020.66` | `1262.58` | `1278.90` | `2606.81` | -476,774.85 USD | `-1.43%` | `5X Cross` |
| `81` | `0x60b0...991e` | `LONG` | 21,485,710.37 USD | `16,779.74` | `1179.65` | `1278.90` | `915.31` | 1,691,463.36 USD | `+7.87%` | `10X Cross` |
| `140` | `0xc36a...105b` | `LONG` | 14,766,686.52 USD | `11,510.82` | `1215.14` | `1278.90` | `956.75` | 779,405.49 USD | `+5.28%` | `10X Cross` |
| `156` | `0x9071...5c0b` | `LONG` | 13,473,700.22 USD | `10,517.29` | `1353.83` | `1278.90` | `0.1605` | -764,918.65 USD | `-5.68%` | `1X Cross` |
| `177` | `0x8742...8427` | `LONG` | 11,783,989.65 USD | `9,201.21` | `1286.37` | `1278.90` | `697.15` | -52,180.35 USD | `-0.44%` | `10X Cross` |
| `191` | `0x58b2...11f3` | `LONG` | 10,963,311.32 USD | `8,563.08` | `1246.56` | `1278.90` | `381.99` | 288,893.75 USD | `+2.64%` | `10X Cross` |
| `196` | `0xad59...ba81` | `SHORT` | 10,789,055.00 USD | `8,425.00` | `330.91` | `1278.90` | `2144.32` | -8,001,097.23 USD | `-74.16%` | `10X Cross` |
| `198` | `0x9ffd...ce40` | `LONG` | 10,707,467.45 USD | `8,367.17` | `1251.60` | `1278.90` | `592.07` | 235,075.65 USD | `+2.20%` | `5X Cross` |
| `203` | `0xdd53...2b13` | `SHORT` | 10,496,514.74 USD | `8,195.92` | `741.54` | `1278.90` | `8403.82` | -4,418,918.38 USD | `-42.10%` | `3X Cross` |
| `222` | `0x880a...311c` | `SHORT` | 9,872,037.20 USD | `7,707.11` | `1367.50` | `1278.90` | `2272.24` | 667,447.00 USD | `+6.76%` | `10X Cross` |
| `235` | `0xbf73...5d58` | `LONG` | 9,597,750.00 USD | `7,500.00` | `1248.78` | `1278.90` | `112.90` | 231,904.38 USD | `+2.42%` | `10X Cross` |
| `270` | `0x2b61...2f6c` | `LONG` | 8,732,378.33 USD | `6,807.00` | `1453.56` | `1278.90` | `580.77` | -1,161,972.89 USD | `-13.31%` | `10X Cross` |
| `284` | `0x2ae5...83e7` | `LONG` | 8,246,184.48 USD | `6,436.80` | `1391.82` | `1278.90` | `0.000000` | -712,707.51 USD | `-8.64%` | `1X Cross` |
| `330` | `0x26b6...9a13` | `LONG` | 6,961,151.50 USD | `5,433.73` | `1282.23` | `1278.90` | `226.67` | -6,151.73 USD | `-0.09%` | `10X Cross` |
| `342` | `0xecb6...2b00` | `SHORT` | 6,703,350.13 USD | `5,238.22` | `1279.15` | `1278.90` | `6789.31` | -2,869.43 USD | `-0.04%` | `5X Cross` |
| `343` | `0x45d2...4029` | `SHORT` | 6,696,309.70 USD | `5,227.00` | `833.44` | `1278.90` | `8767.98` | -2,339,931.73 USD | `-34.94%` | `5X Cross` |
| `363` | `0xea00...a918` | `LONG` | 6,402,277.50 USD | `5,000.00` | `739.16` | `1278.90` | `0.000000` | 2,706,462.39 USD | `+42.27%` | `5X Cross` |
| `375` | `0xdd7a...8830` | `LONG` | 6,224,445.33 USD | `4,860.19` | `897.48` | `1278.90` | `782.33` | 1,862,541.66 USD | `+29.92%` | `10X Cross` |
| `421` | `0x469e...58a5` | `SHORT` | 5,334,718.18 USD | `4,163.52` | `1242.31` | `1278.90` | `1976.03` | -162,333.52 USD | `-3.04%` | `10X Cross` |
| `430` | `0x4cae...7c34` | `LONG` | 5,138,914.68 USD | `4,002.27` | `1169.72` | `1278.90` | `946.84` | 457,365.33 USD | `+8.90%` | `10X Cross` |
| `442` | `0xa61c...66b9` | `LONG` | 4,979,361.60 USD | `3,888.00` | `1148.34` | `1278.90` | `0.000000` | 514,619.46 USD | `+10.34%` | `10X Cross` |
| `465` | `0x9aa5...58af` | `SHORT` | 4,764,601.02 USD | `3,720.31` | `1205.51` | `1278.90` | `3654.38` | -279,714.22 USD | `-5.87%` | `10X Cross` |
| `472` | `0x0153...8052` | `SHORT` | 4,737,738.40 USD | `3,698.18` | `1307.82` | `1278.90` | `2504.86` | 98,832.35 USD | `+2.09%` | `1X Isolated` |
| `480` | `0xd4c1...3d1d` | `SHORT` | 4,693,791.11 USD | `3,665.02` | `1293.18` | `1278.90` | `2377.28` | 45,749.83 USD | `+0.97%` | `10X Cross` |
| `536` | `0x382b...3e39` | `LONG` | 4,186,260.92 USD | `3,269.75` | `1215.08` | `1278.90` | `0.000000` | 213,254.25 USD | `+5.09%` | `10X Cross` |
| `540` | `0xd21d...90f1` | `LONG` | 4,161,950.00 USD | `3,250.00` | `1253.64` | `1278.90` | `876.08` | 87,608.27 USD | `+2.10%` | `4X Isolated` |
| `555` | `0x456f...cdf1` | `LONG` | 4,071,195.46 USD | `3,179.49` | `1267.80` | `1278.90` | `504.11` | 40,240.54 USD | `+0.99%` | `10X Cross` |
| `556` | `0xb122...e4ba` | `LONG` | 4,056,643.35 USD | `3,168.51` | `1263.96` | `1278.90` | `1060.17` | 51,760.72 USD | `+1.28%` | `10X Cross` |
| `563` | `0x1338...c48e` | `LONG` | 4,040,718.69 USD | `3,149.43` | `1018.52` | `1278.90` | `820.37` | 832,973.15 USD | `+20.61%` | `4X Isolated` |
| `571` | `0x325e...9564` | `LONG` | 3,972,616.14 USD | `3,101.91` | `1298.07` | `1278.90` | `140.65` | -53,894.56 USD | `-1.36%` | `10X Cross` |
| `573` | `0xdbe0...d6d5` | `LONG` | 3,952,667.51 USD | `3,085.37` | `422.97` | `1278.90` | `338.69` | 2,647,663.01 USD | `+66.98%` | `3X Isolated` |
| `598` | `0x9c06...0560` | `SHORT` | 3,830,830.74 USD | `2,989.80` | `786.00` | `1278.90` | `2559.81` | -1,480,835.74 USD | `-38.66%` | `10X Cross` |
| `602` | `0x2e30...4cb5` | `SHORT` | 3,800,400.41 USD | `2,967.44` | `1287.28` | `1278.90` | `2887.54` | 19,524.39 USD | `+0.51%` | `2X Cross` |
| `603` | `0x27c9...d65d` | `SHORT` | 3,792,555.54 USD | `2,961.88` | `1254.41` | `1278.90` | `1734.01` | -77,140.33 USD | `-2.03%` | `10X Cross` |
| `632` | `0x5323...b23c` | `SHORT` | 3,584,569.04 USD | `2,798.04` | `1267.04` | `1278.90` | `3205.27` | -39,332.24 USD | `-1.10%` | `5X Cross` |
| `683` | `0x71d0...8c26` | `SHORT` | 3,314,645.49 USD | `2,588.96` | `1266.50` | `1278.90` | `3599.07` | -35,723.25 USD | `-1.08%` | `10X Cross` |
| `695` | `0xa183...0482` | `LONG` | 3,245,293.80 USD | `2,534.00` | `530.25` | `1278.90` | `444.61` | 1,901,631.08 USD | `+58.60%` | `5X Isolated` |
| `698` | `0xac48...3201` | `LONG` | 3,241,473.10 USD | `2,531.50` | `1378.58` | `1278.90` | `555.44` | -248,399.18 USD | `-7.66%` | `10X Cross` |
| `704` | `0x0871...e927` | `LONG` | 3,210,000.00 USD | `2,500.00` | `1276.50` | `1278.90` | `0.000000` | 18,750.00 USD | `+0.58%` | `10X Cross` |
| `716` | `0x9b86...6e6e` | `LONG` | 3,154,501.98 USD | `2,463.30` | `637.58` | `1278.90` | `882.54` | 1,583,952.70 USD | `+50.21%` | `3X Cross` |
| `774` | `0xb2f7...af9f` | `SHORT` | 2,962,949.83 USD | `2,313.72` | `746.63` | `1278.90` | `4422.47` | -1,235,461.09 USD | `-41.70%` | `10X Cross` |
| `794` | `0x413c...886c` | `LONG` | 2,881,350.00 USD | `2,250.00` | `1237.51` | `1278.90` | `0.000000` | 96,948.97 USD | `+3.36%` | `10X Cross` |
| `804` | `0xf48f...10fe` | `LONG` | 2,840,998.29 USD | `2,218.49` | `1517.87` | `1278.90` | `957.22` | -526,388.53 USD | `-18.53%` | `3X Cross` |
| `838` | `0x5bc4...3b0c` | `SHORT` | 2,728,838.72 USD | `2,130.74` | `1089.65` | `1278.90` | `3683.35` | -407,081.14 USD | `-14.92%` | `5X Cross` |
| `856` | `0x8de4...b9aa` | `SHORT` | 2,676,223.81 USD | `2,091.29` | `1331.35` | `1278.90` | `1689.99` | 108,015.89 USD | `+4.04%` | `3X Cross` |
| `859` | `0x4fe2...ac59` | `SHORT` | 2,652,231.07 USD | `2,071.57` | `1478.56` | `1278.90` | `1826.47` | 410,715.14 USD | `+15.49%` | `10X Cross` |
| `864` | `0xdf57...93f5` | `LONG` | 2,631,006.04 USD | `2,054.35` | `1227.36` | `1278.90` | `897.32` | 109,584.00 USD | `+4.17%` | `4X Isolated` |
| `871` | `0xbcd4...0dd2` | `LONG` | 2,604,637.95 USD | `2,033.92` | `1228.20` | `1278.90` | `789.41` | 106,587.14 USD | `+4.09%` | `10X Cross` |
| `883` | `0xf29c...9971` | `LONG` | 2,561,400.00 USD | `2,000.00` | `1254.95` | `1278.90` | `0.000000` | 51,502.93 USD | `+2.01%` | `10X Cross` |
| `884` | `0x9a99...d21a` | `LONG` | 2,560,600.00 USD | `2,000.00` | `1278.44` | `1278.90` | `0.000000` | 3,726.33 USD | `+0.15%` | `10X Cross` |
| `906` | `0x77ee...2902` | `SHORT` | 2,498,702.52 USD | `1,946.03` | `759.84` | `1278.90` | `5488.88` | -1,020,025.01 USD | `-40.82%` | `10X Cross` |
| `918` | `0x3e2f...b269` | `SHORT` | 2,466,000.66 USD | `1,925.51` | `1134.87` | `1278.90` | `2977.26` | -280,801.80 USD | `-11.39%` | `10X Cross` |
| `929` | `0x4f12...618b` | `SHORT` | 2,427,807.28 USD | `1,896.28` | `1608.30` | `1278.90` | `2116.88` | 621,977.10 USD | `+25.62%` | `3X Cross` |
| `970` | `0x866d...d6e1` | `LONG` | 2,313,832.20 USD | `1,802.05` | `674.73` | `1278.90` | `160.98` | 1,097,930.89 USD | `+47.45%` | `10X Cross` |
| `991` | `0x2309...a2d9` | `LONG` | 2,247,125.01 USD | `1,750.37` | `1186.09` | `1278.90` | `810.02` | 171,030.90 USD | `+7.61%` | `8X Cross` |
| `1022` | `0x3205...40bb` | `SHORT` | 2,133,620.59 USD | `1,665.98` | `1256.10` | `1278.90` | `2098.46` | -40,983.23 USD | `-1.92%` | `10X Cross` |
| `1034` | `0x265e...7f70` | `LONG` | 2,113,731.68 USD | `1,651.74` | `1382.98` | `1278.90` | `0.000000` | -170,591.08 USD | `-8.07%` | `3X Cross` |
| `1036` | `0xfe7c...b7ae` | `SHORT` | 2,103,327.42 USD | `1,642.64` | `1346.92` | `1278.90` | `5602.40` | 109,181.20 USD | `+5.19%` | `10X Cross` |
| `1041` | `0x3e47...aaf6` | `LONG` | 2,095,420.17 USD | `1,636.28` | `1278.38` | `1278.90` | `1045.91` | 3,628.38 USD | `+0.17%` | `10X Cross` |
| `1043` | `0x2edd...8179` | `SHORT` | 2,092,522.92 USD | `1,633.89` | `1261.58` | `1278.90` | `2890.07` | -31,241.00 USD | `-1.49%` | `10X Cross` |
| `1059` | `0x7f75...9edf` | `LONG` | 2,062,454.10 USD | `1,611.67` | `1200.24` | `1278.90` | `982.15` | 128,070.12 USD | `+6.21%` | `10X Cross` |
| `1068` | `0x6646...6de5` | `SHORT` | 2,049,440.00 USD | `1,600.00` | `660.64` | `1278.90` | `4336.27` | -992,415.03 USD | `-48.42%` | `10X Cross` |
| `1070` | `0x023a...2355` | `SHORT` | 2,042,588.43 USD | `1,594.90` | `1310.00` | `1278.90` | `4408.12` | 46,723.71 USD | `+2.29%` | `10X Cross` |
| `1093` | `0xab59...59b5` | `LONG` | 2,004,548.79 USD | `1,565.32` | `1342.15` | `1278.90` | `827.42` | -96,346.43 USD | `-4.81%` | `10X Cross` |
| `1123` | `0xfc27...9d9d` | `SHORT` | 1,972,303.61 USD | `1,540.02` | `1296.50` | `1278.90` | `12519.60` | 24,333.57 USD | `+1.23%` | `10X Cross` |
| `1159` | `0xcf67...eb24` | `LONG` | 1,920,450.00 USD | `1,500.00` | `887.05` | `1278.90` | `612.27` | 589,878.63 USD | `+30.72%` | `10X Cross` |
| `1172` | `0xb695...a92d` | `LONG` | 1,899,278.10 USD | `1,483.00` | `1249.80` | `1278.90` | `0.000000` | 45,819.25 USD | `+2.41%` | `10X Cross` |
| `1174` | `0x7277...0b98` | `SHORT` | 1,889,967.41 USD | `1,475.73` | `1287.86` | `1278.90` | `2168.99` | 10,564.71 USD | `+0.56%` | `10X Cross` |
| `1235` | `0x2ab7...c2f8` | `LONG` | 1,794,193.36 USD | `1,400.51` | `813.26` | `1278.90` | `789.71` | 655,211.68 USD | `+36.52%` | `3X Cross` |
| `1247` | `0xe35c...a1d3` | `LONG` | 1,779,097.21 USD | `1,389.16` | `1311.66` | `1278.90` | `690.78` | -43,005.50 USD | `-2.42%` | `2X Isolated` |
| `1258` | `0x11be...8b1d` | `LONG` | 1,763,676.48 USD | `1,375.83` | `1206.55` | `1278.90` | `1134.59` | 103,668.52 USD | `+5.88%` | `10X Isolated` |
| `1325` | `0x039c...0ebd` | `SHORT` | 1,639,039.86 USD | `1,279.80` | `1239.81` | `1278.90` | `3607.04` | -52,325.22 USD | `-3.19%` | `10X Cross` |
| `1339` | `0xe065...0f85` | `SHORT` | 1,616,519.58 USD | `1,262.61` | `1087.02` | `1278.90` | `1571.33` | -244,043.46 USD | `-15.10%` | `10X Cross` |
| `1419` | `0x266b...efcb` | `LONG` | 1,537,080.00 USD | `1,200.00` | `893.76` | `1278.90` | `379.15` | 464,570.30 USD | `+30.22%` | `10X Cross` |
| `1420` | `0x5975...9abd` | `LONG` | 1,536,546.60 USD | `1,200.00` | `1179.54` | `1278.90` | `450.16` | 121,103.81 USD | `+7.88%` | `5X Cross` |
| `1444` | `0x2847...d47b` | `LONG` | 1,519,967.75 USD | `1,186.27` | `1232.07` | `1278.90` | `0.000000` | 58,399.25 USD | `+3.84%` | `5X Cross` |
| `1468` | `0x69cc...14fd` | `SHORT` | 1,487,353.75 USD | `1,161.36` | `675.33` | `1278.90` | `7946.10` | -703,048.22 USD | `-47.27%` | `10X Cross` |
| `1481` | `0x3fc5...c0c1` | `SHORT` | 1,470,692.26 USD | `1,148.44` | `1264.34` | `1278.90` | `2672.64` | -18,678.49 USD | `-1.27%` | `10X Cross` |
| `1493` | `0x38f9...cb04` | `SHORT` | 1,458,745.76 USD | `1,138.40` | `1252.73` | `1278.90` | `1988.92` | -32,642.81 USD | `-2.24%` | `10X Cross` |
| `1517` | `0x5f94...4b96` | `LONG` | 1,428,214.76 USD | `1,115.27` | `538.00` | `1278.90` | `0.000000` | 828,197.13 USD | `+57.99%` | `10X Cross` |
| `1533` | `0x71df...a23d` | `SHORT` | 1,408,931.46 USD | `1,098.28` | `513.50` | `1278.90` | `2558.32` | -844,961.27 USD | `-59.97%` | `2X Cross` |
| `1569` | `0xbfc7...80b4` | `SHORT` | 1,376,752.50 USD | `1,075.00` | `558.03` | `1278.90` | `2602.49` | -776,873.77 USD | `-56.43%` | `10X Cross` |
| `1638` | `0x123d...3bff` | `SHORT` | 1,297,536.78 USD | `1,013.34` | `494.46` | `1278.90` | `4287.37` | -796,482.15 USD | `-61.38%` | `10X Cross` |
| `1653` | `0x668c...ea2e` | `SHORT` | 1,281,300.00 USD | `1,000.00` | `1406.98` | `1278.90` | `4198.68` | 125,681.99 USD | `+9.81%` | `10X Cross` |
| `1654` | `0xe282...df29` | `LONG` | 1,280,700.00 USD | `1,000.00` | `420.99` | `1278.90` | `789.58` | 859,713.14 USD | `+67.13%` | `10X Cross` |
| `1674` | `0x17f0...094f` | `LONG` | 1,262,856.90 USD | `984.30` | `1287.23` | `1278.90` | `536.94` | -4,163.26 USD | `-0.33%` | `5X Cross` |
| `1692` | `0x51f6...2b39` | `SHORT` | 1,245,877.77 USD | `972.81` | `1299.77` | `1278.90` | `2531.15` | 18,549.94 USD | `+1.49%` | `10X Cross` |
| `1720` | `0xdf83...3cff` | `SHORT` | 1,222,704.07 USD | `954.79` | `1259.51` | `1278.90` | `1916.32` | -20,132.72 USD | `-1.65%` | `10X Cross` |
| `1753` | `0x757d...94ba` | `LONG` | 1,184,647.50 USD | `925.00` | `1558.31` | `1278.90` | `0.000000` | -256,793.08 USD | `-21.68%` | `10X Cross` |
| `1756` | `0xaa82...9556` | `LONG` | 1,183,533.29 USD | `924.13` | `1254.72` | `1278.90` | `180.54` | 24,006.61 USD | `+2.03%` | `10X Cross` |
| `1804` | `0xb911...5525` | `LONG` | 1,152,540.00 USD | `900.00` | `1294.82` | `1278.90` | `1035.37` | -12,797.82 USD | `-1.11%` | `10X Cross` |
| `1858` | `0xcf0a...856f` | `LONG` | 1,114,810.66 USD | `871.15` | `1292.19` | `1278.90` | `1005.28` | -10,884.19 USD | `-0.98%` | `4X Cross` |
| `1859` | `0x2577...4897` | `SHORT` | 1,114,247.42 USD | `870.03` | `1271.91` | `1278.90` | `4963.41` | -7,651.40 USD | `-0.69%` | `10X Cross` |
| `1860` | `0x9e7e...0047` | `LONG` | 1,114,237.25 USD | `870.09` | `1284.68` | `1278.90` | `1174.58` | -3,548.16 USD | `-0.32%` | `10X Cross` |
| `1862` | `0xef96...9383` | `SHORT` | 1,111,838.13 USD | `868.42` | `1259.08` | `1278.90` | `5306.55` | -18,426.33 USD | `-1.66%` | `10X Cross` |
| `1881` | `0xdf95...7d72` | `SHORT` | 1,091,929.62 USD | `853.27` | `1074.39` | `1278.90` | `44120.41` | -175,182.18 USD | `-16.04%` | `10X Cross` |
| `1916` | `0x601c...4f54` | `SHORT` | 1,057,730.86 USD | `824.42` | `615.11` | `1278.90` | `3057.72` | -550,618.11 USD | `-52.06%` | `5X Cross` |
| `1936` | `0xae55...2236` | `LONG` | 1,047,260.82 USD | `817.47` | `1467.80` | `1278.90` | `0.000000` | -152,620.40 USD | `-14.57%` | `10X Cross` |
| `1979` | `0x0f02...5384` | `LONG` | 1,025,558.95 USD | `800.78` | `1290.36` | `1278.90` | `296.54` | -7,735.12 USD | `-0.75%` | `3X Cross` |
| `1981` | `0x9b0f...db40` | `LONG` | 1,024,880.00 USD | `800.00` | `1268.86` | `1278.90` | `792.05` | 9,790.24 USD | `+0.96%` | `10X Cross` |
| `1982` | `0x11ee...1d1d` | `SHORT` | 1,023,760.00 USD | `800.00` | `1269.65` | `1278.90` | `1592.98` | -8,036.99 USD | `-0.79%` | `5X Cross` |
| `1993` | `0xabdb...84ac` | `LONG` | 1,018,939.22 USD | `793.69` | `711.79` | `1278.90` | `664.51` | 453,998.86 USD | `+44.56%` | `3X Cross` |
| `1995` | `0x6e8f...4364` | `LONG` | 1,016,427.56 USD | `793.65` | `1260.00` | `1278.90` | `929.81` | 16,428.56 USD | `+1.62%` | `10X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `873.68` | 6,203.13 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 6.20K USD at 873.6800 USD [API] | `2026-08-23 14:08:41` |
| `ANNOUNCEMENT` | `INFO` | `873.59` | 8,727.16 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 8.73K USD at 873.5900 USD [API] | `2026-08-23 14:08:41` |
| `ANNOUNCEMENT` | `INFO` | `1257.50` | 12.58 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 0.01K USD at 1257.5000 USD [API] | `2026-10-29 01:59:34` |
| `ANNOUNCEMENT` | `INFO` | `1256.60` | 992.71 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 0.99K USD at 1256.6000 USD [API] | `2026-10-29 01:59:31` |
| `ANNOUNCEMENT` | `INFO` | `1290.00` | 309.60 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Long: 0.31K USD at 1290.0000 USD [API] | `2026-10-27 15:21:38` |
| `ANNOUNCEMENT` | `INFO` | `1290.00` | 516.00 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Long: 0.52K USD at 1290.0000 USD [API] | `2026-10-27 15:21:38` |
| `ANNOUNCEMENT` | `INFO` | `1238.70` | 1,350.18 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 1.35K USD at 1238.7000 USD [API] | `2026-10-29 02:30:54` |
| `ANNOUNCEMENT` | `INFO` | `1234.10` | 1,814.13 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 1.81K USD at 1234.1000 USD [API] | `2026-10-29 02:35:53` |
| `ANNOUNCEMENT` | `INFO` | `1234.10` | 222.14 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 0.22K USD at 1234.1000 USD [API] | `2026-10-29 02:35:53` |
| `ANNOUNCEMENT` | `INFO` | `1234.10` | 12.34 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 0.01K USD at 1234.1000 USD [API] | `2026-10-29 02:35:53` |
| `ANNOUNCEMENT` | `INFO` | `1234.10` | 12.34 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 0.01K USD at 1234.1000 USD [API] | `2026-10-29 02:35:53` |
| `ANNOUNCEMENT` | `INFO` | `1234.80` | 3,346.31 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 3.35K USD at 1234.8000 USD [API] | `2026-10-29 02:35:52` |
| `ANNOUNCEMENT` | `INFO` | `1234.70` | 3,481.85 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 3.48K USD at 1234.7000 USD [API] | `2026-10-29 02:35:52` |
| `ANNOUNCEMENT` | `INFO` | `1190.50` | 35.71 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 0.04K USD at 1190.5000 USD [API] | `2026-10-22 18:01:21` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`1404.55` (Vol: 3,000,000.00 USD, Dist: `+9.91%`) | Long MP=`1176.48` (Vol: 3,400,000.00 USD, Dist: `--7.94%`)
  * 48H Horizon: Short MP=`1404.55` (Vol: 3,000,000.00 USD, Dist: `+9.91%`) | Long MP=`1176.48` (Vol: 3,400,000.00 USD, Dist: `--7.94%`)
  * 3D Horizon: Short MP=`1404.55` (Vol: 3,000,000.00 USD, Dist: `+9.91%`) | Long MP=`1176.48` (Vol: 3,000,000.00 USD, Dist: `--7.94%`)
  * 7D Horizon: Short MP=`1404.10` (Vol: 3,000,000.00 USD, Dist: `+9.87%`) | Long MP=`1176.74` (Vol: 4,900,000.00 USD, Dist: `--7.92%`)
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
| `5m` | `BALANCED` | 0.00 USD | 1,750.00 USD | 1,750.00 USD | 1,750.00 USD | `1` | `2026-10-30 05:20:00 UTC - 2026-10-30 05:25:00 UTC` |
| `15m` | `BALANCED` | 0.00 USD | 1,750.00 USD | 1,750.00 USD | 1,750.00 USD | `1` | `2026-10-30 05:15:00 UTC - 2026-10-30 05:30:00 UTC` |
| `1h` | `BALANCED` | 0.00 USD | 1,750.00 USD | 1,750.00 USD | 1,750.00 USD | `1` | `2026-10-30 05:00:00 UTC - 2026-10-30 06:00:00 UTC` |
| `4h` | `BALANCED` | 0.00 USD | 1,750.00 USD | 1,750.00 USD | 1,750.00 USD | `1` | `2026-10-30 04:00:00 UTC - 2026-10-30 08:00:00 UTC` |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `0 USD` | Total OI Tokens: `-`
  * 1h OI Change: `0.00%` | 4h OI Change: `0.00%` | 24h OI Change: `0.00%`
  * Exchange Breakdown: Binance=`-` | Bybit=`-` | OKX=`-` | Hyperliquid=`-`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `83.27K` | Last 24h: `134.73K` | Last 3d: `246.48K` | Last 7d: `772.71K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0094%` | **USDT OKX** | `0.0100%` |
| **USDT Bybit** | `0.0100%` | **USDT KuCoin** | `0.0100%` |
| **USDT MEXC** | `0.0094%` | **USDT BingX** | `0.0100%` |
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
| `0:00 UTC` | `1260.15` | `1262.58` | `1260.15` | `1267.95` | `1257.15` | 13,992,732.07 USD | 6,287,729.60 USD | 7,705,002.47 USD | -1,417,272.88 USD | `-10.13%` | `0B / 2S` |
| `5:00 UTC` | `1265.55` | `1265.89` | `1265.55` | `1274.25` | `1259.25` | 13,172,642.30 USD | 7,854,309.17 USD | 5,318,333.13 USD | 2,535,976.04 USD | `+19.25%` | `13B / 1S` |
| `0:00 UTC` | `1282.05` | `1279.57` | `1282.05` | `1285.35` | `1269.15` | 31,465,166.07 USD | 16,761,441.58 USD | 14,703,724.48 USD | 2,057,717.10 USD | `+6.54%` | `8B / 5S` |
| `5:00 UTC` | `1279.95` | `1280.45` | `1279.95` | `1287.45` | `1275.15` | 19,925,691.14 USD | 8,662,599.23 USD | 11,263,091.92 USD | -2,600,492.69 USD | `-13.05%` | `1B / 6S` |
| `0:00 UTC` | `1275.15` | `1271.95` | `1275.15` | `1279.35` | `1264.95` | 23,738,198.29 USD | 11,363,344.84 USD | 12,374,853.45 USD | -1,011,508.62 USD | `-4.26%` | `3B / 3S` |
| `5:00 UTC` | `1279.05` | `1280.95` | `1279.05` | `1287.45` | `1274.25` | 14,930,858.33 USD | 7,292,403.22 USD | 7,638,455.11 USD | -346,051.88 USD | `-2.32%` | `2B / 4S` |
| `0:00 UTC` | `1285.05` | `1286.06` | `1285.05` | `1289.85` | `1282.05` | 15,953,463.93 USD | 6,542,642.51 USD | 9,410,821.42 USD | -2,868,178.91 USD | `-17.98%` | `1B / 3S` |
| `5:00 UTC` | `1276.95` | `1279.23` | `1276.95` | `1286.25` | `1275.15` | 15,449,899.62 USD | 6,063,485.10 USD | 9,386,414.52 USD | -3,322,929.42 USD | `-21.51%` | `0B / 8S` |
| `0:00 UTC` | `1275.15` | `1278.02` | `1275.15` | `1285.05` | `1272.15` | 16,039,119.46 USD | 6,719,465.52 USD | 9,319,653.95 USD | -2,600,188.43 USD | `-16.21%` | `2B / 3S` |
| `5:00 UTC` | `1276.95` | `1276.77` | `1276.95` | `1278.75` | `1273.95` | 3,673,900.93 USD | 1,334,869.32 USD | 2,339,031.61 USD | -1,004,162.29 USD | `-27.33%` | `0B / 6S` |

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
| `5m` | -297,020.00 USD | 567,590.00 USD | **`ACCUMULATION`** |
| `15m` | -785,070.00 USD | -2,730,000.00 USD | **`DISTRIBUTION`** |
| `30m` | -1,560,000.00 USD | -7,780,000.00 USD | **`DISTRIBUTION`** |
| `1h` | -769,250.00 USD | -5,840,000.00 USD | **`DISTRIBUTION`** |
| `2h` | -572,820.00 USD | -8,750,000.00 USD | **`DISTRIBUTION`** |
| `4h` | 6,300,000.00 USD | 9,420,000.00 USD | **`ACCUMULATION`** |
| `6h` | 795,440.00 USD | 11,790,000.00 USD | **`ACCUMULATION`** |
| `8h` | 5,450,000.00 USD | -9,830,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -10,990,000.00 USD | -16,860,000.00 USD | **`DISTRIBUTION`** |
| `24h` | 15,820,000.00 USD | 95,140,000.00 USD | **`ACCUMULATION`** |
| `1w` | 35,120,000.00 USD | 231,290,000.00 USD | **`ACCUMULATION`** |
| `30d` | 61,020,000.00 USD | -528,130,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-297.02K` | 15m=`-785.07K` | 1h=`-769.25K` | 24h=`+15.82M`
* Futures Capital Netflows: 5m=`+567.59K` | 15m=`-2.73M` | 1h=`-5.84M` | 24h=`+95.14M`
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
  * `2026-10-30 09:50:40 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 10:48:40 IST`: [forex.com] - (Sentiment: `Neutral`)
  * `2026-10-30 10:47:40 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 10:47:40 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 10:47:40 IST`: [financemagnates.com] - (Sentiment: `Neutral`)
  * `2026-10-30 07:49:40 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-30 06:49:40 IST`: [kathleenhays.substack.com] - (Sentiment: `Neutral`)
  * `2026-10-30 06:49:40 IST`: [rba.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 06:49:40 IST`: [abs.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 05:49:40 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 05:49:40 IST`: [@NodeWire] - (Sentiment: `Neutral`)
  * `2026-10-30 05:49:40 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 05:49:40 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 05:49:40 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-30 05:49:40 IST`: [media.rabobank.com] - (Sentiment: `Neutral`)


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
  * Execution Entry: `1222.17` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `1199.64` (Risk Distance: `22.53` pts)
  * +2.5R Take Profit: `1278.51`
  * Mathematical Lot Sizing: **`0.44 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `1273.97` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `1296.50` (Risk Distance: `22.53` pts)
  * +2.5R Take Profit: `1217.63`
  * Mathematical Lot Sizing: **`0.44 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`1284.86`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
