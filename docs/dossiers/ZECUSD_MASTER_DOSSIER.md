# 🏛️ SOVEREIGN CANDIDATE DOSSIER: ZECUSD
**Canonical Key**: `ZECUSD` | **Broker Instrument**: `ZECUSD.p` | **Asset Class**: `Crypto Altcoin`
**Timestamp**: `2026-10-30 10:28:45 IST` (`2026-10-30 04:58:45 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `1276.94` | **Live Ask Quote**: `1278.17` | **Mid Price**: `1277.56`
- **Spread Points**: `123.00` | **Spread BPS**: `9.63 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `1247.03` | VWAP Z-Score: `+1.44` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `17.75` (Volatility Regime: `HIGH_EXPANSION`)
  * 14-Period RSI: `58.78` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `1322.01` | Lower -3.00σ Band: `1172.05`
  * Upper +2.51σ Band: `1309.77` | Lower -2.51σ Band: `1184.30`
  * Upper +2.01σ Band: `1297.27` | Lower -2.01σ Band: `1196.79`
  * Upper +2.00σ Band: `1297.02` | Lower -2.00σ Band: `1197.04`
  * Upper +1.28σ Band: `1279.02` | Lower -1.28σ Band: `1215.04`
  * Upper +1.00σ Band: `1272.02` | Lower -1.00σ Band: `1222.04`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`1272.91` | EMA-20=`1263.57` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`1267.40` (Slope: `+0.0000`) | EMA-100=`1272.73`
  * Institutional Anchors: EMA-144=`1274.07` | EMA-200=`1275.36` (Slope: `-0.0750`) | EMA-233=`1277.75`
- **Range Boundaries**: 24H High=`1396.49` | 24H Low=`1180.03` | Weekly High=`1396.49` | Weekly Low=`1180.03`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `1270.87` (Distance: `+0.52%`)
  * Point of Control (POC) = `1229.90` (Distance: `+3.87%`)
  * Value Area Low (VAL) = `1220.62` (Distance: `+4.66%`)
  * Auction Positioning: `ABOVE_VALUE (Imbalance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `RANGE_EXPANSION`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`1309.91` | POC=`1246.71` | VAL=`1230.27`
  * Prior Day Extremes: PDH=`1396.49` | PDL=`1206.89` | PDC=`1244.38`
  * Monday Range Blueprint: High=`1267.53` | Mid=`1222.14` | Low=`1176.75`
  * Developing Weekly Value Area: Weekly VAH=`1296.14` | Weekly POC=`1239.01` | Weekly VAL=`1200.92`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`1296.00` | Low=`1180.03`
  * London Session (08:00-16:00 UTC): High=`1282.67` | Low=`1272.44`
  * New York Session (13:00-21:00 UTC): High=`1285.22` | Low=`1269.89`
  * Initial Balance (First Hour): IB High=`1281.39` | IB Low=`1273.72`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `1272.44` - `1282.67`
  * Optimal Trade Entry (OTE 0.705): `1280.11`
  * Structural Invalidation Anchor (0.786): `1287.78`

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
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 10:24:51 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `13` | `0xb83d...6e36` | `SHORT` | 66,932,915.02 USD | `52,385.47` | `1336.45` | `1277.70` | `3701.24` | 3,077,652.38 USD | `+4.60%` | `3X Cross` |
| `22` | `0x5b5d...c060` | `SHORT` | 51,226,977.98 USD | `40,121.38` | `1478.36` | `1277.70` | `5135.93` | 8,087,057.13 USD | `+15.79%` | `3X Cross` |
| `39` | `0x7fda...17d1` | `SHORT` | 33,082,906.46 USD | `25,890.52` | `1262.49` | `1277.70` | `2627.29` | -396,319.28 USD | `-1.20%` | `5X Cross` |
| `80` | `0x60b0...991e` | `LONG` | 21,433,317.31 USD | `16,779.74` | `1179.65` | `1277.70` | `921.21` | 1,639,070.30 USD | `+7.65%` | `10X Cross` |
| `139` | `0xc36a...105b` | `LONG` | 14,697,014.98 USD | `11,510.82` | `1215.14` | `1277.70` | `961.18` | 709,733.95 USD | `+4.83%` | `10X Cross` |
| `153` | `0x9071...5c0b` | `LONG` | 13,453,417.63 USD | `10,517.29` | `1353.83` | `1277.70` | `0.1437` | -785,201.25 USD | `-5.84%` | `1X Cross` |
| `175` | `0x8742...8427` | `LONG` | 11,769,925.60 USD | `9,201.21` | `1286.37` | `1277.70` | `701.88` | -66,244.40 USD | `-0.56%` | `10X Cross` |
| `191` | `0x58b2...11f3` | `LONG` | 10,933,340.54 USD | `8,563.08` | `1246.56` | `1277.70` | `381.44` | 258,922.97 USD | `+2.37%` | `10X Cross` |
| `196` | `0xad59...ba81` | `SHORT` | 10,764,622.50 USD | `8,425.00` | `330.91` | `1277.70` | `2145.20` | -7,976,664.73 USD | `-74.10%` | `10X Cross` |
| `198` | `0x9ffd...ce40` | `LONG` | 10,704,780.58 USD | `8,384.07` | `1251.51` | `1277.70` | `594.48` | 212,051.89 USD | `+1.98%` | `5X Cross` |
| `203` | `0xdd53...2b13` | `SHORT` | 10,468,919.90 USD | `8,195.92` | `741.54` | `1277.70` | `8502.84` | -4,391,323.54 USD | `-41.95%` | `3X Cross` |
| `222` | `0x880a...311c` | `SHORT` | 9,840,438.05 USD | `7,707.11` | `1367.50` | `1277.70` | `2257.13` | 699,046.15 USD | `+7.10%` | `10X Cross` |
| `235` | `0xbf73...5d58` | `LONG` | 9,576,000.00 USD | `7,500.00` | `1248.78` | `1277.70` | `126.22` | 210,154.38 USD | `+2.19%` | `10X Cross` |
| `269` | `0x2b61...2f6c` | `LONG` | 8,691,177.60 USD | `6,807.00` | `1453.56` | `1277.70` | `570.58` | -1,203,173.62 USD | `-13.84%` | `10X Cross` |
| `285` | `0x2ae5...83e7` | `LONG` | 8,233,771.11 USD | `6,436.80` | `1391.82` | `1277.70` | `0.000000` | -725,120.88 USD | `-8.81%` | `1X Cross` |
| `331` | `0x26b6...9a13` | `LONG` | 6,950,672.55 USD | `5,433.73` | `1282.23` | `1277.70` | `223.65` | -16,630.68 USD | `-0.24%` | `10X Cross` |
| `342` | `0x45d2...4029` | `SHORT` | 6,683,764.90 USD | `5,227.00` | `833.44` | `1277.70` | `8900.46` | -2,327,386.93 USD | `-34.82%` | `5X Cross` |
| `350` | `0xecb6...2b00` | `SHORT` | 6,640,554.57 USD | `5,194.02` | `1279.14` | `1277.70` | `6327.30` | 3,330.31 USD | `+0.05%` | `5X Cross` |
| `363` | `0xea00...a918` | `LONG` | 6,386,665.50 USD | `5,000.00` | `739.16` | `1277.70` | `0.000000` | 2,690,850.39 USD | `+42.13%` | `5X Cross` |
| `375` | `0xdd7a...8830` | `LONG` | 6,209,378.74 USD | `4,860.19` | `897.48` | `1277.70` | `786.05` | 1,847,475.07 USD | `+29.75%` | `10X Cross` |
| `419` | `0x469e...58a5` | `SHORT` | 5,316,010.23 USD | `4,163.52` | `1242.31` | `1277.70` | `1967.06` | -143,625.58 USD | `-2.70%` | `10X Cross` |
| `428` | `0x4cae...7c34` | `LONG` | 5,110,098.34 USD | `4,002.27` | `1169.72` | `1277.70` | `968.85` | 428,548.99 USD | `+8.39%` | `10X Cross` |
| `440` | `0xa61c...66b9` | `LONG` | 4,966,142.40 USD | `3,888.00` | `1148.34` | `1277.70` | `0.000000` | 501,400.26 USD | `+10.10%` | `10X Cross` |
| `463` | `0x9aa5...58af` | `SHORT` | 4,756,416.33 USD | `3,720.31` | `1205.51` | `1277.70` | `3678.25` | -271,529.54 USD | `-5.71%` | `10X Cross` |
| `467` | `0x0153...8052` | `SHORT` | 4,730,711.86 USD | `3,698.18` | `1307.82` | `1277.70` | `2504.85` | 105,858.89 USD | `+2.24%` | `1X Isolated` |
| `479` | `0xd4c1...3d1d` | `SHORT` | 4,648,152.96 USD | `3,635.63` | `1293.28` | `1277.70` | `2419.78` | 53,727.44 USD | `+1.16%` | `10X Cross` |
| `531` | `0x382b...3e39` | `LONG` | 4,180,375.38 USD | `3,269.75` | `1215.08` | `1277.70` | `0.000000` | 207,368.70 USD | `+4.96%` | `10X Cross` |
| `537` | `0xd21d...90f1` | `LONG` | 4,151,225.00 USD | `3,250.00` | `1253.64` | `1277.70` | `876.06` | 76,883.27 USD | `+1.85%` | `4X Isolated` |
| `551` | `0x456f...cdf1` | `LONG` | 4,041,290.33 USD | `3,163.85` | `1267.75` | `1277.70` | `499.99` | 30,329.46 USD | `+0.75%` | `10X Cross` |
| `555` | `0x1338...c48e` | `LONG` | 4,021,192.22 USD | `3,149.43` | `1018.52` | `1277.70` | `820.35` | 813,446.68 USD | `+20.23%` | `4X Isolated` |
| `566` | `0x325e...9564` | `LONG` | 3,962,069.64 USD | `3,101.91` | `1298.07` | `1277.70` | `160.07` | -64,441.06 USD | `-1.63%` | `10X Cross` |
| `570` | `0xdbe0...d6d5` | `LONG` | 3,946,805.30 USD | `3,085.37` | `422.97` | `1277.70` | `338.67` | 2,641,800.81 USD | `+66.94%` | `3X Isolated` |
| `596` | `0x2e30...4cb5` | `SHORT` | 3,823,290.33 USD | `2,990.45` | `1287.29` | `1277.70` | `2877.87` | 26,290.87 USD | `+0.69%` | `2X Cross` |
| `597` | `0x9c06...0560` | `SHORT` | 3,817,396.67 USD | `2,989.80` | `786.00` | `1277.70` | `2586.23` | -1,467,401.67 USD | `-38.44%` | `10X Cross` |
| `601` | `0x27c9...d65d` | `SHORT` | 3,783,307.36 USD | `2,961.88` | `1254.41` | `1277.70` | `1734.16` | -67,892.16 USD | `-1.79%` | `10X Cross` |
| `626` | `0x5323...b23c` | `SHORT` | 3,589,120.27 USD | `2,807.29` | `1266.09` | `1277.70` | `3200.20` | -34,828.54 USD | `-0.97%` | `5X Cross` |
| `682` | `0x71d0...8c26` | `SHORT` | 3,310,662.96 USD | `2,589.49` | `1265.67` | `1277.70` | `3600.78` | -33,230.34 USD | `-1.00%` | `10X Cross` |
| `693` | `0xa183...0482` | `LONG` | 3,241,420.58 USD | `2,534.00` | `530.25` | `1277.70` | `444.59` | 1,897,757.86 USD | `+58.55%` | `5X Isolated` |
| `698` | `0xac48...3201` | `LONG` | 3,233,568.74 USD | `2,531.50` | `1378.58` | `1277.70` | `541.59` | -256,303.54 USD | `-7.93%` | `10X Cross` |
| `710` | `0x0871...e927` | `LONG` | 3,192,000.00 USD | `2,500.00` | `1276.50` | `1277.70` | `0.000000` | 750.00 USD | `+0.02%` | `10X Cross` |
| `718` | `0x9b86...6e6e` | `LONG` | 3,146,373.09 USD | `2,463.30` | `637.58` | `1277.70` | `882.52` | 1,575,823.81 USD | `+50.08%` | `3X Cross` |
| `749` | `0xb122...e4ba` | `LONG` | 3,070,676.35 USD | `2,404.79` | `1259.16` | `1277.70` | `989.96` | 42,657.90 USD | `+1.39%` | `10X Cross` |
| `777` | `0xb2f7...af9f` | `SHORT` | 2,956,240.04 USD | `2,313.72` | `746.63` | `1277.70` | `4459.17` | -1,228,751.30 USD | `-41.56%` | `10X Cross` |
| `794` | `0x413c...886c` | `LONG` | 2,873,925.00 USD | `2,250.00` | `1237.51` | `1277.70` | `0.000000` | 89,523.97 USD | `+3.12%` | `10X Cross` |
| `806` | `0xf48f...10fe` | `LONG` | 2,834,564.67 USD | `2,218.49` | `1517.87` | `1277.70` | `969.52` | -532,822.15 USD | `-18.80%` | `3X Cross` |
| `840` | `0x5bc4...3b0c` | `SHORT` | 2,725,216.46 USD | `2,130.74` | `1089.65` | `1277.70` | `3691.52` | -403,458.88 USD | `-14.80%` | `5X Cross` |
| `857` | `0x8de4...b9aa` | `SHORT` | 2,670,159.07 USD | `2,091.29` | `1331.35` | `1277.70` | `1689.97` | 114,080.63 USD | `+4.27%` | `3X Cross` |
| `862` | `0x4fe2...ac59` | `SHORT` | 2,645,187.73 USD | `2,071.57` | `1478.56` | `1277.70` | `1838.02` | 417,758.48 USD | `+15.79%` | `10X Cross` |
| `866` | `0xdf57...93f5` | `LONG` | 2,627,513.65 USD | `2,054.35` | `1227.36` | `1277.70` | `897.30` | 106,091.61 USD | `+4.04%` | `4X Isolated` |
| `874` | `0xbcd4...0dd2` | `LONG` | 2,598,739.58 USD | `2,033.92` | `1228.20` | `1277.70` | `760.56` | 100,688.77 USD | `+3.87%` | `10X Cross` |
| `886` | `0xf29c...9971` | `LONG` | 2,558,343.00 USD | `2,000.00` | `1254.95` | `1277.70` | `0.000000` | 48,445.93 USD | `+1.89%` | `10X Cross` |
| `888` | `0x9a99...d21a` | `LONG` | 2,553,800.00 USD | `2,000.00` | `1278.44` | `1277.70` | `0.000000` | -3,073.67 USD | `-0.12%` | `10X Cross` |
| `911` | `0x77ee...2902` | `SHORT` | 2,484,691.10 USD | `1,946.03` | `759.84` | `1277.70` | `5488.65` | -1,006,013.60 USD | `-40.49%` | `10X Cross` |
| `922` | `0x3e2f...b269` | `SHORT` | 2,461,764.54 USD | `1,925.51` | `1134.87` | `1277.70` | `2977.24` | -276,565.68 USD | `-11.23%` | `10X Cross` |
| `932` | `0x4f12...618b` | `SHORT` | 2,421,170.30 USD | `1,896.28` | `1608.30` | `1277.70` | `2116.86` | 628,614.08 USD | `+25.96%` | `3X Cross` |
| `974` | `0x866d...d6e1` | `LONG` | 2,300,857.44 USD | `1,802.05` | `674.73` | `1277.70` | `171.06` | 1,084,956.13 USD | `+47.15%` | `10X Cross` |
| `999` | `0x2309...a2d9` | `LONG` | 2,234,884.14 USD | `1,750.37` | `1186.09` | `1277.70` | `811.60` | 158,790.03 USD | `+7.11%` | `8X Cross` |
| `1005` | `0x3205...40bb` | `SHORT` | 2,206,435.30 USD | `1,725.80` | `1255.41` | `1277.70` | `2075.08` | -39,852.66 USD | `-1.81%` | `10X Cross` |
| `1036` | `0x265e...7f70` | `LONG` | 2,108,941.63 USD | `1,651.74` | `1382.98` | `1277.70` | `0.000000` | -175,381.13 USD | `-8.32%` | `3X Cross` |
| `1041` | `0xfe7c...b7ae` | `SHORT` | 2,098,198.44 USD | `1,642.64` | `1346.92` | `1277.70` | `5682.38` | 114,310.18 USD | `+5.45%` | `10X Cross` |
| `1049` | `0x3e47...aaf6` | `LONG` | 2,090,020.44 USD | `1,636.28` | `1278.38` | `1277.70` | `1048.47` | -1,771.34 USD | `-0.08%` | `10X Cross` |
| `1051` | `0x2edd...8179` | `SHORT` | 2,086,967.70 USD | `1,633.89` | `1261.58` | `1277.70` | `2895.23` | -25,685.78 USD | `-1.23%` | `10X Cross` |
| `1058` | `0x7f75...9edf` | `LONG` | 2,057,780.26 USD | `1,611.67` | `1200.24` | `1277.70` | `982.95` | 123,396.28 USD | `+6.00%` | `10X Cross` |
| `1066` | `0x6646...6de5` | `SHORT` | 2,046,720.00 USD | `1,600.00` | `660.64` | `1277.70` | `4313.48` | -989,695.03 USD | `-48.36%` | `10X Cross` |
| `1071` | `0x023a...2355` | `SHORT` | 2,039,079.65 USD | `1,594.90` | `1310.00` | `1277.70` | `4438.76` | 50,232.49 USD | `+2.46%` | `10X Cross` |
| `1099` | `0xab59...59b5` | `LONG` | 1,999,383.24 USD | `1,565.32` | `1342.15` | `1277.70` | `834.41` | -101,511.98 USD | `-5.08%` | `10X Cross` |
| `1161` | `0xcf67...eb24` | `LONG` | 1,915,350.00 USD | `1,500.00` | `887.05` | `1277.70` | `633.39` | 584,778.63 USD | `+30.53%` | `10X Cross` |
| `1168` | `0xfc27...9d9d` | `SHORT` | 1,907,650.29 USD | `1,493.97` | `1297.02` | `1277.70` | `13206.69` | 30,051.97 USD | `+1.58%` | `10X Cross` |
| `1173` | `0xb695...a92d` | `LONG` | 1,897,011.33 USD | `1,483.00` | `1249.80` | `1277.70` | `0.000000` | 43,552.48 USD | `+2.30%` | `10X Cross` |
| `1178` | `0x7277...0b98` | `SHORT` | 1,887,458.67 USD | `1,475.73` | `1287.86` | `1277.70` | `2179.54` | 13,073.45 USD | `+0.69%` | `10X Cross` |
| `1244` | `0x2ab7...c2f8` | `LONG` | 1,791,492.48 USD | `1,400.51` | `813.26` | `1277.70` | `790.79` | 652,510.79 USD | `+36.42%` | `3X Cross` |
| `1250` | `0xe35c...a1d3` | `LONG` | 1,774,790.82 USD | `1,389.16` | `1311.66` | `1277.70` | `690.77` | -47,311.90 USD | `-2.67%` | `2X Isolated` |
| `1259` | `0x11be...8b1d` | `LONG` | 1,757,393.20 USD | `1,375.83` | `1206.55` | `1277.70` | `1134.57` | 97,385.24 USD | `+5.54%` | `10X Isolated` |
| `1332` | `0x039c...0ebd` | `SHORT` | 1,635,187.68 USD | `1,279.79` | `1239.81` | `1277.70` | `3621.17` | -48,485.85 USD | `-2.97%` | `10X Cross` |
| `1342` | `0x38f9...cb04` | `SHORT` | 1,619,148.38 USD | `1,268.13` | `1252.68` | `1277.70` | `1913.71` | -30,593.03 USD | `-1.89%` | `10X Cross` |
| `1346` | `0xe065...0f85` | `SHORT` | 1,612,226.71 USD | `1,262.61` | `1087.02` | `1277.70` | `1579.38` | -239,750.58 USD | `-14.87%` | `10X Cross` |
| `1429` | `0x266b...efcb` | `LONG` | 1,534,440.00 USD | `1,200.00` | `893.76` | `1277.70` | `388.17` | 461,930.30 USD | `+30.10%` | `10X Cross` |
| `1431` | `0x5975...9abd` | `LONG` | 1,532,799.72 USD | `1,200.00` | `1179.54` | `1277.70` | `481.75` | 117,356.93 USD | `+7.66%` | `5X Cross` |
| `1448` | `0x2847...d47b` | `LONG` | 1,514,629.54 USD | `1,186.27` | `1232.07` | `1277.70` | `0.000000` | 53,061.04 USD | `+3.50%` | `5X Cross` |
| `1467` | `0x69cc...14fd` | `SHORT` | 1,485,379.44 USD | `1,161.36` | `675.33` | `1277.70` | `8009.72` | -701,073.91 USD | `-47.20%` | `10X Cross` |
| `1484` | `0x3fc5...c0c1` | `SHORT` | 1,466,902.41 USD | `1,148.44` | `1264.34` | `1277.70` | `2727.22` | -14,888.64 USD | `-1.01%` | `10X Cross` |
| `1522` | `0x5f94...4b96` | `LONG` | 1,424,980.48 USD | `1,115.27` | `538.00` | `1277.70` | `0.000000` | 824,962.84 USD | `+57.89%` | `10X Cross` |
| `1540` | `0x71df...a23d` | `SHORT` | 1,402,283.90 USD | `1,098.28` | `513.50` | `1277.70` | `2558.00` | -838,313.71 USD | `-59.78%` | `2X Cross` |
| `1572` | `0xbfc7...80b4` | `SHORT` | 1,374,387.50 USD | `1,075.00` | `558.03` | `1277.70` | `2700.82` | -774,508.77 USD | `-56.35%` | `10X Cross` |
| `1640` | `0x123d...3bff` | `SHORT` | 1,296,322.29 USD | `1,013.94` | `494.46` | `1277.70` | `4301.76` | -794,970.98 USD | `-61.33%` | `10X Cross` |
| `1661` | `0xe282...df29` | `LONG` | 1,277,600.00 USD | `1,000.00` | `420.99` | `1277.70` | `806.01` | 856,613.14 USD | `+67.05%` | `10X Cross` |
| `1662` | `0x668c...ea2e` | `SHORT` | 1,276,806.70 USD | `1,000.00` | `1406.98` | `1277.70` | `4196.80` | 130,175.29 USD | `+10.20%` | `10X Cross` |
| `1688` | `0x17f0...094f` | `LONG` | 1,256,754.24 USD | `984.30` | `1287.23` | `1277.70` | `536.92` | -10,265.92 USD | `-0.82%` | `5X Cross` |
| `1700` | `0x51f6...2b39` | `SHORT` | 1,243,737.58 USD | `972.81` | `1299.77` | `1277.70` | `2531.82` | 20,690.12 USD | `+1.66%` | `10X Cross` |
| `1759` | `0x757d...94ba` | `LONG` | 1,183,075.00 USD | `925.00` | `1558.31` | `1277.70` | `0.000000` | -258,365.58 USD | `-21.84%` | `10X Cross` |
| `1761` | `0xaa82...9556` | `LONG` | 1,181,962.27 USD | `924.13` | `1254.72` | `1277.70` | `182.21` | 22,435.59 USD | `+1.90%` | `10X Cross` |
| `1789` | `0xdf83...3cff` | `SHORT` | 1,165,620.16 USD | `912.28` | `1258.55` | `1277.70` | `1913.65` | -17,473.57 USD | `-1.50%` | `10X Cross` |
| `1809` | `0xb911...5525` | `LONG` | 1,149,570.00 USD | `900.00` | `1294.82` | `1277.70` | `1035.36` | -15,767.82 USD | `-1.37%` | `10X Cross` |
| `1859` | `0xcf0a...856f` | `LONG` | 1,112,290.16 USD | `871.15` | `1292.19` | `1277.70` | `1004.27` | -13,404.69 USD | `-1.21%` | `4X Cross` |
| `1860` | `0x9e7e...0047` | `LONG` | 1,111,365.96 USD | `870.09` | `1284.68` | `1277.70` | `1179.13` | -6,419.46 USD | `-0.58%` | `10X Cross` |
| `1862` | `0xef96...9383` | `SHORT` | 1,108,885.50 USD | `868.42` | `1259.08` | `1277.70` | `5358.56` | -15,473.71 USD | `-1.40%` | `10X Cross` |
| `1882` | `0xdf95...7d72` | `SHORT` | 1,090,905.70 USD | `853.27` | `1074.39` | `1277.70` | `44477.59` | -174,158.25 USD | `-15.96%` | `10X Cross` |
| `1885` | `0x2577...4897` | `SHORT` | 1,089,716.69 USD | `852.34` | `1270.97` | `1277.70` | `5053.76` | -6,414.69 USD | `-0.59%` | `10X Cross` |
| `1926` | `0x601c...4f54` | `SHORT` | 1,052,619.46 USD | `824.42` | `615.11` | `1277.70` | `3079.65` | -545,506.70 USD | `-51.82%` | `5X Cross` |
| `1936` | `0xae55...2236` | `LONG` | 1,045,684.33 USD | `817.47` | `1467.80` | `1277.70` | `0.000000` | -154,196.89 USD | `-14.75%` | `10X Cross` |
| `1982` | `0x0f02...5384` | `LONG` | 1,024,197.62 USD | `800.78` | `1290.36` | `1277.70` | `300.55` | -9,096.45 USD | `-0.89%` | `3X Cross` |
| `1983` | `0x9b0f...db40` | `LONG` | 1,023,360.00 USD | `800.00` | `1268.86` | `1277.70` | `794.32` | 8,270.24 USD | `+0.81%` | `10X Cross` |
| `1984` | `0x11ee...1d1d` | `SHORT` | 1,021,445.36 USD | `800.00` | `1269.65` | `1277.70` | `1602.09` | -5,722.35 USD | `-0.56%` | `5X Cross` |
| `1999` | `0x6e8f...4364` | `LONG` | 1,013,967.24 USD | `793.65` | `1260.00` | `1277.70` | `944.06` | 13,968.24 USD | `+1.38%` | `10X Cross` |
| `2000` | `0xabdb...84ac` | `LONG` | 1,013,383.39 USD | `793.69` | `711.79` | `1277.70` | `664.49` | 448,443.03 USD | `+44.25%` | `3X Cross` |

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


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`1404.55` (Vol: 3,000,000.00 USD, Dist: `+9.99%`) | Long MP=`1176.48` (Vol: 3,400,000.00 USD, Dist: `--7.87%`)
  * 48H Horizon: Short MP=`1404.55` (Vol: 3,000,000.00 USD, Dist: `+9.99%`) | Long MP=`1176.48` (Vol: 3,400,000.00 USD, Dist: `--7.87%`)
  * 3D Horizon: Short MP=`1404.55` (Vol: 3,000,000.00 USD, Dist: `+9.99%`) | Long MP=`1176.48` (Vol: 3,000,000.00 USD, Dist: `--7.87%`)
  * 7D Horizon: Short MP=`1404.10` (Vol: 3,000,000.00 USD, Dist: `+9.95%`) | Long MP=`1176.74` (Vol: 4,900,000.00 USD, Dist: `--7.85%`)
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
| `5m` | `BALANCED` | 0.00 USD | 1,750.00 USD | 1,750.00 USD | 1,750.00 USD | `1` | `2026-10-30 04:50:00 UTC - 2026-10-30 04:55:00 UTC` |
| `15m` | `BALANCED` | 0.00 USD | 1,750.00 USD | 1,750.00 USD | 1,750.00 USD | `1` | `2026-10-30 04:45:00 UTC - 2026-10-30 05:00:00 UTC` |
| `1h` | `BALANCED` | 0.00 USD | 1,750.00 USD | 1,750.00 USD | 1,750.00 USD | `1` | `2026-10-30 04:00:00 UTC - 2026-10-30 05:00:00 UTC` |
| `4h` | `BALANCED` | 0.00 USD | 1,750.00 USD | 1,750.00 USD | 1,750.00 USD | `1` | `2026-10-30 04:00:00 UTC - 2026-10-30 08:00:00 UTC` |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `0 USD` | Total OI Tokens: `-`
  * 1h OI Change: `0.00%` | 4h OI Change: `0.00%` | 24h OI Change: `0.00%`
  * Exchange Breakdown: Binance=`-` | Bybit=`-` | OKX=`-` | Hyperliquid=`-`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `84.90K` | Last 24h: `134.73K` | Last 3d: `246.48K` | Last 7d: `772.71K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0097%` | **USDT OKX** | `0.0100%` |
| **USDT Bybit** | `0.0100%` | **USDT KuCoin** | `0.0100%` |
| **USDT MEXC** | `0.0097%` | **USDT BingX** | `0.0100%` |
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
| `0:00 UTC` | `1263.45` | `1263.47` | `1263.45` | `1267.65` | `1258.35` | 21,490,941.27 USD | 11,626,504.00 USD | 9,864,437.27 USD | 1,762,066.74 USD | `+8.20%` | `2B / 3S` |
| `5:00 UTC` | `1257.45` | `1259.53` | `1257.45` | `1270.05` | `1249.95` | 34,915,865.69 USD | 14,880,758.20 USD | 20,035,107.50 USD | -5,154,349.30 USD | `-14.76%` | `1B / 7S` |
| `0:00 UTC` | `1260.15` | `1262.58` | `1260.15` | `1267.95` | `1257.15` | 13,992,732.07 USD | 6,287,729.60 USD | 7,705,002.47 USD | -1,417,272.88 USD | `-10.13%` | `0B / 2S` |
| `5:00 UTC` | `1265.55` | `1265.89` | `1265.55` | `1274.25` | `1259.25` | 13,172,642.30 USD | 7,854,309.17 USD | 5,318,333.13 USD | 2,535,976.04 USD | `+19.25%` | `13B / 1S` |
| `0:00 UTC` | `1282.05` | `1279.57` | `1282.05` | `1285.35` | `1269.15` | 31,465,166.07 USD | 16,761,441.58 USD | 14,703,724.48 USD | 2,057,717.10 USD | `+6.54%` | `8B / 5S` |
| `5:00 UTC` | `1279.95` | `1280.45` | `1279.95` | `1287.45` | `1275.15` | 19,925,691.14 USD | 8,662,599.23 USD | 11,263,091.92 USD | -2,600,492.69 USD | `-13.05%` | `1B / 6S` |
| `0:00 UTC` | `1275.15` | `1271.95` | `1275.15` | `1279.35` | `1264.95` | 23,738,198.29 USD | 11,363,344.84 USD | 12,374,853.45 USD | -1,011,508.62 USD | `-4.26%` | `3B / 3S` |
| `5:00 UTC` | `1279.05` | `1280.95` | `1279.05` | `1287.45` | `1274.25` | 14,930,858.33 USD | 7,292,403.22 USD | 7,638,455.11 USD | -346,051.88 USD | `-2.32%` | `2B / 4S` |
| `0:00 UTC` | `1285.05` | `1286.06` | `1285.05` | `1289.85` | `1282.05` | 15,953,463.93 USD | 6,542,642.51 USD | 9,410,821.42 USD | -2,868,178.91 USD | `-17.98%` | `1B / 3S` |
| `5:00 UTC` | `1279.95` | `1281.97` | `1279.95` | `1286.25` | `1278.15` | 6,689,304.17 USD | 2,644,898.70 USD | 4,044,405.47 USD | -1,399,506.76 USD | `-20.92%` | `0B / 8S` |

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
| `5m` | -193,800.00 USD | -2,350,000.00 USD | **`DISTRIBUTION`** |
| `15m` | -358,280.00 USD | -5,950,000.00 USD | **`DISTRIBUTION`** |
| `30m` | 242,360.00 USD | -3,390,000.00 USD | **`DISTRIBUTION`** |
| `1h` | 150,890.00 USD | -6,720,000.00 USD | **`DISTRIBUTION`** |
| `2h` | -462,700.00 USD | -11,280,000.00 USD | **`DISTRIBUTION`** |
| `4h` | 5,120,000.00 USD | 15,990,000.00 USD | **`ACCUMULATION`** |
| `6h` | 392,380.00 USD | 6,680,000.00 USD | **`ACCUMULATION`** |
| `8h` | 5,730,000.00 USD | -1,860,000.00 USD | **`ACCUMULATION`** |
| `12h` | -4,610,000.00 USD | -12,590,000.00 USD | **`DISTRIBUTION`** |
| `24h` | 17,280,000.00 USD | 104,080,000.00 USD | **`ACCUMULATION`** |
| `1w` | 38,380,000.00 USD | 236,260,000.00 USD | **`ACCUMULATION`** |
| `30d` | 62,140,000.00 USD | -523,020,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-193.80K` | 15m=`-358.28K` | 1h=`+150.89K` | 24h=`+17.28M`
* Futures Capital Netflows: 5m=`-2.35M` | 15m=`-5.95M` | 1h=`-6.72M` | 24h=`+104.08M`
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
  * `2026-10-30 09:51:07 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 10:20:07 IST`: [forex.com] - (Sentiment: `Neutral`)
  * `2026-10-30 10:20:07 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 10:20:07 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 10:19:07 IST`: [financemagnates.com] - (Sentiment: `Neutral`)
  * `2026-10-30 07:21:07 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-30 07:21:07 IST`: [kathleenhays.substack.com] - (Sentiment: `Neutral`)
  * `2026-10-30 06:21:07 IST`: [rba.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 06:21:07 IST`: [abs.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 06:21:07 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 06:21:07 IST`: [@NodeWire] - (Sentiment: `Neutral`)
  * `2026-10-30 05:21:07 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 05:21:07 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 05:21:07 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-30 05:21:07 IST`: [media.rabobank.com] - (Sentiment: `Neutral`)


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
  * Execution Entry: `1220.62` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `1197.48` (Risk Distance: `23.14` pts)
  * +2.5R Take Profit: `1278.47`
  * Mathematical Lot Sizing: **`0.43 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `1270.87` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `1294.01` (Risk Distance: `23.14` pts)
  * +2.5R Take Profit: `1213.02`
  * Mathematical Lot Sizing: **`0.43 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`1287.78`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
