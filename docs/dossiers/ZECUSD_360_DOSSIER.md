# 🏛️ SOVEREIGN CANDIDATE DOSSIER: ZECUSD
**Canonical Key**: `ZECUSD` | **Broker Instrument**: `ZECUSD.p` | **Asset Class**: `Crypto Altcoin`
**Timestamp**: `2026-10-30 15:12:02 IST` (`2026-10-30 09:42:02 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `1248.71` | **Live Ask Quote**: `1249.79` | **Mid Price**: `1249.25`
- **Spread Points**: `108.00` | **Spread BPS**: `8.65 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `1253.69` | VWAP Z-Score: `-0.36` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `11.99` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `41.57` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `1317.89` | Lower -3.00σ Band: `1189.49`
  * Upper +2.51σ Band: `1307.41` | Lower -2.51σ Band: `1199.98`
  * Upper +2.01σ Band: `1296.71` | Lower -2.01σ Band: `1210.68`
  * Upper +2.00σ Band: `1296.49` | Lower -2.00σ Band: `1210.89`
  * Upper +1.28σ Band: `1281.09` | Lower -1.28σ Band: `1226.30`
  * Upper +1.00σ Band: `1275.09` | Lower -1.00σ Band: `1232.29`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`1250.28` | EMA-20=`1256.21` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`1262.58` (Slope: `+0.0000`) | EMA-100=`1268.63`
  * Institutional Anchors: EMA-144=`1271.75` | EMA-200=`1275.91` (Slope: `-0.2231`) | EMA-233=`1276.51`
- **Range Boundaries**: 24H High=`1396.49` | 24H Low=`1180.03` | Weekly High=`1396.49` | Weekly Low=`1180.03`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `1280.15` (Distance: `-2.45%`)
  * Point of Control (POC) = `1247.68` (Distance: `+0.09%`)
  * Value Area Low (VAL) = `1237.63` (Distance: `+0.90%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`1309.91` | POC=`1246.71` | VAL=`1230.27`
  * Prior Day Extremes: PDH=`1396.49` | PDL=`1206.89` | PDC=`1244.38`
  * Monday Range Blueprint: High=`1267.53` | Mid=`1222.14` | Low=`1176.75`
  * Developing Weekly Value Area: Weekly VAH=`1294.68` | Weekly POC=`1240.47` | Weekly VAL=`1200.92`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`1296.00` | Low=`1180.03`
  * London Session (08:00-16:00 UTC): High=`1283.82` | Low=`1239.95`
  * New York Session (13:00-21:00 UTC): High=`1256.75` | Low=`1241.75`
  * Initial Balance (First Hour): IB High=`1283.82` | IB Low=`1264.92`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `1244.25` - `1254.25`
  * Optimal Trade Entry (OTE 0.705): `1251.75`
  * Structural Invalidation Anchor (0.786): `1259.24`

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
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 15:10:55 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `12` | `0xb83d...6e36` | `SHORT` | 65,198,955.96 USD | `52,385.47` | `1336.45` | `1243.60` | `3385.88` | 4,811,611.44 USD | `+7.38%` | `3X Cross` |
| `21` | `0x5b5d...c060` | `SHORT` | 49,935,069.55 USD | `40,121.38` | `1478.36` | `1243.60` | `4853.68` | 9,378,965.56 USD | `+18.78%` | `3X Cross` |
| `36` | `0x7fda...17d1` | `SHORT` | 33,103,431.30 USD | `26,595.51` | `1262.59` | `1243.60` | `2622.69` | 475,905.80 USD | `+1.44%` | `5X Cross` |
| `83` | `0x60b0...991e` | `LONG` | 20,889,098.33 USD | `16,779.74` | `1179.65` | `1243.60` | `921.07` | 1,094,851.31 USD | `+5.24%` | `10X Cross` |
| `140` | `0xc36a...105b` | `LONG` | 14,330,970.90 USD | `11,510.82` | `1215.14` | `1243.60` | `968.18` | 343,689.87 USD | `+2.40%` | `10X Cross` |
| `178` | `0x8742...8427` | `LONG` | 11,456,426.57 USD | `9,201.21` | `1286.37` | `1243.60` | `713.55` | -379,743.42 USD | `-3.31%` | `10X Cross` |
| `192` | `0x58b2...11f3` | `LONG` | 10,660,178.29 USD | `8,563.08` | `1246.56` | `1243.60` | `383.90` | -14,239.28 USD | `-0.13%` | `10X Cross` |
| `195` | `0x9ffd...ce40` | `LONG` | 10,626,678.03 USD | `8,536.17` | `1252.20` | `1243.60` | `608.18` | -62,289.34 USD | `-0.59%` | `5X Cross` |
| `196` | `0x9071...5c0b` | `LONG` | 10,604,877.78 USD | `8,517.29` | `1353.83` | `1243.60` | `0.000000` | -926,081.82 USD | `-8.73%` | `2X Cross` |
| `200` | `0xad59...ba81` | `SHORT` | 10,485,755.00 USD | `8,425.00` | `330.91` | `1243.60` | `2147.69` | -7,697,797.23 USD | `-73.41%` | `10X Cross` |
| `205` | `0xdd53...2b13` | `SHORT` | 10,203,100.81 USD | `8,195.92` | `741.54` | `1243.60` | `8521.35` | -4,125,504.44 USD | `-40.43%` | `3X Cross` |
| `226` | `0x880a...311c` | `SHORT` | 9,593,623.25 USD | `7,707.11` | `1367.50` | `1243.60` | `2226.51` | 945,860.96 USD | `+9.86%` | `10X Cross` |
| `237` | `0xbf73...5d58` | `LONG` | 9,339,000.00 USD | `7,500.00` | `1248.78` | `1243.60` | `144.76` | -26,845.62 USD | `-0.29%` | `10X Cross` |
| `272` | `0x2b61...2f6c` | `LONG` | 8,479,479.90 USD | `6,807.00` | `1453.56` | `1243.60` | `556.52` | -1,414,871.32 USD | `-16.69%` | `10X Cross` |
| `292` | `0x2ae5...83e7` | `LONG` | 8,014,459.68 USD | `6,436.80` | `1391.82` | `1243.60` | `0.000000` | -944,432.31 USD | `-11.78%` | `1X Cross` |
| `325` | `0xecb6...2b00` | `SHORT` | 7,040,732.68 USD | `5,656.57` | `1278.10` | `1243.60` | `6543.64` | 188,934.73 USD | `+2.68%` | `5X Cross` |
| `333` | `0x26b6...9a13` | `LONG` | 6,766,080.60 USD | `5,433.73` | `1282.23` | `1243.60` | `227.82` | -201,222.64 USD | `-2.97%` | `10X Cross` |
| `354` | `0x45d2...4029` | `SHORT` | 6,508,137.70 USD | `5,227.00` | `833.44` | `1243.60` | `9169.69` | -2,151,759.73 USD | `-33.06%` | `5X Cross` |
| `367` | `0xea00...a918` | `LONG` | 6,226,000.00 USD | `5,000.00` | `739.16` | `1243.60` | `0.000000` | 2,530,184.89 USD | `+40.64%` | `5X Cross` |
| `380` | `0xdd7a...8830` | `LONG` | 6,048,992.47 USD | `4,860.19` | `897.48` | `1243.60` | `790.19` | 1,687,088.80 USD | `+27.89%` | `10X Cross` |
| `423` | `0x469e...58a5` | `SHORT` | 5,183,582.40 USD | `4,163.52` | `1242.31` | `1243.60` | `1955.59` | -11,197.75 USD | `-0.22%` | `10X Cross` |
| `436` | `0x4cae...7c34` | `LONG` | 4,985,627.74 USD | `4,002.27` | `1169.72` | `1243.60` | `989.04` | 304,078.39 USD | `+6.10%` | `10X Cross` |
| `443` | `0xd4c1...3d1d` | `SHORT` | 4,892,111.24 USD | `3,928.46` | `1291.68` | `1243.60` | `2372.08` | 182,200.15 USD | `+3.72%` | `10X Cross` |
| `449` | `0xa61c...66b9` | `LONG` | 4,840,560.00 USD | `3,888.00` | `1148.34` | `1243.60` | `0.000000` | 375,817.86 USD | `+7.76%` | `10X Cross` |
| `470` | `0x382b...3e39` | `LONG` | 4,662,238.25 USD | `3,743.94` | `1219.28` | `1243.60` | `0.000000` | 97,325.60 USD | `+2.09%` | `10X Cross` |
| `477` | `0x9aa5...58af` | `SHORT` | 4,631,785.95 USD | `3,720.31` | `1205.51` | `1243.60` | `3723.91` | -146,899.15 USD | `-3.17%` | `10X Cross` |
| `481` | `0x0153...8052` | `SHORT` | 4,592,769.74 USD | `3,698.18` | `1307.82` | `1243.60` | `2504.93` | 243,801.01 USD | `+5.31%` | `1X Isolated` |
| `513` | `0xb122...e4ba` | `LONG` | 4,356,560.38 USD | `3,498.47` | `1265.25` | `1243.60` | `1128.94` | -69,891.15 USD | `-1.60%` | `10X Cross` |
| `550` | `0xd21d...90f1` | `LONG` | 4,046,575.00 USD | `3,250.00` | `1253.64` | `1243.60` | `876.15` | -27,766.73 USD | `-0.69%` | `4X Isolated` |
| `551` | `0x456f...cdf1` | `LONG` | 4,046,431.07 USD | `3,251.19` | `1267.53` | `1243.60` | `522.43` | -74,550.69 USD | `-1.84%` | `10X Cross` |
| `573` | `0x1338...c48e` | `LONG` | 3,921,985.18 USD | `3,149.43` | `1018.52` | `1243.60` | `820.45` | 714,239.64 USD | `+18.21%` | `4X Isolated` |
| `594` | `0xdbe0...d6d5` | `LONG` | 3,831,721.00 USD | `3,085.37` | `422.97` | `1243.60` | `338.76` | 2,526,716.51 USD | `+65.94%` | `3X Isolated` |
| `606` | `0x2e30...4cb5` | `SHORT` | 3,751,283.14 USD | `3,020.60` | `1282.40` | `1243.60` | `2874.10` | 122,324.90 USD | `+3.26%` | `2X Cross` |
| `612` | `0x325e...9564` | `LONG` | 3,736,132.95 USD | `3,000.91` | `1298.07` | `1243.60` | `154.82` | -159,272.21 USD | `-4.26%` | `10X Cross` |
| `614` | `0x9c06...0560` | `SHORT` | 3,728,579.58 USD | `2,989.80` | `786.00` | `1243.60` | `2584.85` | -1,378,584.58 USD | `-36.97%` | `10X Cross` |
| `622` | `0x27c9...d65d` | `SHORT` | 3,658,676.28 USD | `2,938.04` | `1254.41` | `1243.60` | `1741.24` | 26,833.76 USD | `+0.73%` | `10X Cross` |
| `713` | `0xa183...0482` | `LONG` | 3,154,576.60 USD | `2,534.00` | `530.25` | `1243.60` | `444.69` | 1,810,913.88 USD | `+57.41%` | `5X Isolated` |
| `716` | `0xac48...3201` | `LONG` | 3,151,464.35 USD | `2,531.50` | `1378.58` | `1243.60` | `527.68` | -338,407.93 USD | `-10.74%` | `10X Cross` |
| `723` | `0x0871...e927` | `LONG` | 3,112,500.00 USD | `2,500.00` | `1276.50` | `1243.60` | `0.000000` | -78,750.00 USD | `-2.53%` | `10X Cross` |
| `748` | `0x9b86...6e6e` | `LONG` | 3,065,823.18 USD | `2,463.30` | `637.58` | `1243.60` | `882.62` | 1,495,273.90 USD | `+48.77%` | `3X Cross` |
| `821` | `0xf48f...10fe` | `LONG` | 2,761,132.65 USD | `2,218.49` | `1517.87` | `1243.60` | `974.84` | -606,254.17 USD | `-21.96%` | `3X Cross` |
| `852` | `0x5bc4...3b0c` | `SHORT` | 2,652,293.38 USD | `2,130.74` | `1089.65` | `1243.60` | `3684.81` | -330,535.80 USD | `-12.46%` | `5X Cross` |
| `865` | `0x8de4...b9aa` | `SHORT` | 2,604,074.31 USD | `2,091.29` | `1331.35` | `1243.60` | `1690.05` | 180,165.40 USD | `+6.92%` | `3X Cross` |
| `870` | `0x4fe2...ac59` | `SHORT` | 2,578,897.49 USD | `2,071.57` | `1478.56` | `1243.60` | `1853.26` | 484,048.72 USD | `+18.77%` | `10X Cross` |
| `872` | `0xdf57...93f5` | `LONG` | 2,558,642.80 USD | `2,054.35` | `1227.36` | `1243.60` | `897.39` | 37,220.75 USD | `+1.45%` | `4X Isolated` |
| `879` | `0xbcd4...0dd2` | `LONG` | 2,531,620.22 USD | `2,033.92` | `1228.20` | `1243.60` | `742.43` | 33,569.41 USD | `+1.33%` | `10X Cross` |
| `888` | `0x71d0...8c26` | `SHORT` | 2,500,263.53 USD | `2,007.76` | `1266.91` | `1243.60` | `3972.41` | 43,379.42 USD | `+1.73%` | `10X Cross` |
| `891` | `0x9a99...d21a` | `LONG` | 2,490,551.80 USD | `2,000.00` | `1278.44` | `1243.60` | `0.000000` | -66,321.87 USD | `-2.66%` | `10X Cross` |
| `892` | `0xf29c...9971` | `LONG` | 2,489,800.00 USD | `2,000.00` | `1254.95` | `1243.60` | `0.000000` | -20,097.07 USD | `-0.81%` | `10X Cross` |
| `917` | `0x77ee...2902` | `SHORT` | 2,424,169.57 USD | `1,946.03` | `759.84` | `1243.60` | `5681.78` | -945,492.06 USD | `-39.00%` | `10X Cross` |
| `924` | `0x3e2f...b269` | `SHORT` | 2,396,828.06 USD | `1,925.51` | `1134.87` | `1243.60` | `2977.33` | -211,629.20 USD | `-8.83%` | `10X Cross` |
| `939` | `0x4f12...618b` | `SHORT` | 2,361,247.86 USD | `1,896.28` | `1608.30` | `1243.60` | `2116.94` | 688,536.53 USD | `+29.16%` | `3X Cross` |
| `982` | `0x866d...d6e1` | `LONG` | 2,244,092.87 USD | `1,802.05` | `674.73` | `1243.60` | `155.86` | 1,028,191.55 USD | `+45.82%` | `10X Cross` |
| `1013` | `0x2309...a2d9` | `LONG` | 2,180,435.91 USD | `1,750.37` | `1186.09` | `1243.60` | `809.09` | 104,341.80 USD | `+4.79%` | `8X Cross` |
| `1055` | `0x265e...7f70` | `LONG` | 2,056,746.65 USD | `1,651.74` | `1382.98` | `1243.60` | `0.000000` | -227,576.11 USD | `-11.06%` | `3X Cross` |
| `1060` | `0xfe7c...b7ae` | `SHORT` | 2,044,922.54 USD | `1,642.64` | `1346.92` | `1243.60` | `5756.29` | 167,586.08 USD | `+8.20%` | `10X Cross` |
| `1064` | `0x3e47...aaf6` | `LONG` | 2,037,332.23 USD | `1,636.28` | `1278.38` | `1243.60` | `1052.53` | -54,459.56 USD | `-2.67%` | `10X Cross` |
| `1065` | `0x2edd...8179` | `SHORT` | 2,036,795.10 USD | `1,635.98` | `1261.55` | `1243.60` | `2886.44` | 27,067.78 USD | `+1.33%` | `10X Cross` |
| `1090` | `0x7f75...9edf` | `LONG` | 2,007,474.08 USD | `1,612.17` | `1200.26` | `1243.60` | `987.06` | 72,453.00 USD | `+3.61%` | `10X Cross` |
| `1099` | `0x6646...6de5` | `SHORT` | 1,987,040.00 USD | `1,600.00` | `660.64` | `1243.60` | `4167.51` | -930,015.03 USD | `-46.80%` | `10X Cross` |
| `1106` | `0x023a...2355` | `SHORT` | 1,981,180.95 USD | `1,591.31` | `1310.00` | `1243.60` | `4431.70` | 103,428.30 USD | `+5.22%` | `10X Cross` |
| `1115` | `0xfc27...9d9d` | `SHORT` | 1,965,315.64 USD | `1,578.44` | `1295.79` | `1243.60` | `13012.31` | 80,008.56 USD | `+4.07%` | `10X Cross` |
| `1127` | `0xab59...59b5` | `LONG` | 1,948,979.93 USD | `1,565.32` | `1342.15` | `1243.60` | `837.67` | -151,915.29 USD | `-7.79%` | `10X Cross` |
| `1171` | `0x039c...0ebd` | `SHORT` | 1,894,434.83 USD | `1,521.39` | `1245.17` | `1243.60` | `3734.61` | -40.97 USD | `-0.00%` | `10X Cross` |
| `1181` | `0xcf67...eb24` | `LONG` | 1,867,913.85 USD | `1,500.00` | `887.05` | `1243.60` | `632.98` | 537,342.48 USD | `+28.77%` | `10X Cross` |
| `1197` | `0x7277...0b98` | `SHORT` | 1,836,952.84 USD | `1,475.73` | `1287.86` | `1243.60` | `2200.31` | 63,579.28 USD | `+3.46%` | `10X Cross` |
| `1262` | `0x2ab7...c2f8` | `LONG` | 1,744,755.36 USD | `1,400.51` | `813.26` | `1243.60` | `793.23` | 605,773.67 USD | `+34.72%` | `3X Cross` |
| `1278` | `0x11be...8b1d` | `LONG` | 1,712,358.02 USD | `1,375.83` | `1206.55` | `1243.60` | `1134.67` | 52,350.06 USD | `+3.06%` | `10X Isolated` |
| `1332` | `0x3205...40bb` | `SHORT` | 1,622,207.04 USD | `1,306.23` | `1257.43` | `1243.60` | `2392.51` | 20,283.64 USD | `+1.25%` | `10X Cross` |
| `1364` | `0xe065...0f85` | `SHORT` | 1,572,297.80 USD | `1,262.61` | `1087.02` | `1243.60` | `1555.57` | -199,821.68 USD | `-12.71%` | `10X Cross` |
| `1380` | `0x413c...886c` | `LONG` | 1,556,375.00 USD | `1,250.00` | `1237.51` | `1243.60` | `0.000000` | 9,485.54 USD | `+0.61%` | `10X Cross` |
| `1407` | `0xdf83...3cff` | `SHORT` | 1,545,282.91 USD | `1,241.59` | `1260.63` | `1243.60` | `1840.57` | 19,899.24 USD | `+1.29%` | `10X Cross` |
| `1442` | `0x2847...d47b` | `LONG` | 1,508,215.44 USD | `1,211.71` | `1232.45` | `1243.60` | `0.000000` | 14,847.84 USD | `+0.98%` | `5X Cross` |
| `1456` | `0x5975...9abd` | `LONG` | 1,494,333.48 USD | `1,200.00` | `1179.54` | `1243.60` | `560.23` | 78,890.69 USD | `+5.28%` | `5X Cross` |
| `1458` | `0x266b...efcb` | `LONG` | 1,490,280.00 USD | `1,200.00` | `893.76` | `1243.60` | `422.00` | 417,770.30 USD | `+28.03%` | `10X Cross` |
| `1490` | `0x69cc...14fd` | `SHORT` | 1,446,241.61 USD | `1,161.36` | `675.33` | `1243.60` | `8140.55` | -661,936.08 USD | `-45.77%` | `10X Cross` |
| `1504` | `0x3fc5...c0c1` | `SHORT` | 1,429,348.42 USD | `1,148.44` | `1264.34` | `1243.60` | `2793.43` | 22,665.35 USD | `+1.59%` | `10X Cross` |
| `1547` | `0x5f94...4b96` | `LONG` | 1,388,065.04 USD | `1,115.27` | `538.00` | `1243.60` | `0.000000` | 788,047.41 USD | `+56.77%` | `10X Cross` |
| `1550` | `0xe35c...a1d3` | `LONG` | 1,383,643.20 USD | `1,111.36` | `1311.66` | `1243.60` | `690.96` | -74,080.94 USD | `-5.35%` | `2X Isolated` |
| `1570` | `0x71df...a23d` | `SHORT` | 1,368,127.40 USD | `1,098.28` | `513.50` | `1243.60` | `2560.21` | -804,157.21 USD | `-58.78%` | `2X Cross` |
| `1590` | `0xbfc7...80b4` | `SHORT` | 1,338,375.00 USD | `1,075.00` | `558.03` | `1243.60` | `2724.82` | -738,496.27 USD | `-55.18%` | `10X Cross` |
| `1631` | `0x123d...3bff` | `SHORT` | 1,300,493.52 USD | `1,044.34` | `519.62` | `1243.60` | `4151.63` | -757,835.31 USD | `-58.27%` | `10X Cross` |
| `1691` | `0xe282...df29` | `LONG` | 1,245,000.00 USD | `1,000.00` | `420.99` | `1243.60` | `814.00` | 824,013.14 USD | `+66.19%` | `10X Cross` |
| `1692` | `0x668c...ea2e` | `SHORT` | 1,245,000.00 USD | `1,000.00` | `1406.98` | `1243.60` | `4211.45` | 161,981.99 USD | `+13.01%` | `10X Cross` |
| `1705` | `0x5323...b23c` | `SHORT` | 1,237,206.07 USD | `993.66` | `1254.62` | `1243.60` | `6834.46` | 9,456.34 USD | `+0.76%` | `5X Cross` |
| `1717` | `0x17f0...094f` | `LONG` | 1,226,142.51 USD | `984.30` | `1287.23` | `1243.60` | `537.02` | -40,877.65 USD | `-3.33%` | `5X Cross` |
| `1733` | `0x51f6...2b39` | `SHORT` | 1,210,856.61 USD | `972.81` | `1299.77` | `1243.60` | `2517.41` | 53,571.10 USD | `+4.42%` | `10X Cross` |
| `1803` | `0x757d...94ba` | `LONG` | 1,151,417.52 USD | `925.00` | `1558.31` | `1243.60` | `0.000000` | -290,023.06 USD | `-25.19%` | `10X Cross` |
| `1843` | `0xb911...5525` | `LONG` | 1,120,750.11 USD | `900.00` | `1294.82` | `1243.60` | `1035.45` | -44,587.71 USD | `-3.98%` | `10X Cross` |
| `1865` | `0xef96...9383` | `SHORT` | 1,105,518.59 USD | `887.77` | `1259.32` | `1243.60` | `5141.78` | 12,468.29 USD | `+1.13%` | `10X Cross` |
| `1886` | `0xcf0a...856f` | `LONG` | 1,084,581.75 USD | `871.15` | `1292.19` | `1243.60` | `1027.91` | -41,113.10 USD | `-3.79%` | `4X Cross` |
| `1906` | `0xdf95...7d72` | `SHORT` | 1,062,065.17 USD | `853.27` | `1074.39` | `1243.60` | `45430.32` | -145,317.73 USD | `-13.68%` | `10X Cross` |
| `1939` | `0xb2f7...af9f` | `SHORT` | 1,034,329.47 USD | `830.72` | `746.63` | `1243.60` | `8186.94` | -414,090.44 USD | `-40.03%` | `10X Cross` |
| `1958` | `0x601c...4f54` | `SHORT` | 1,026,650.23 USD | `824.42` | `615.11` | `1243.60` | `3140.60` | -519,537.47 USD | `-50.61%` | `5X Cross` |
| `1974` | `0xae55...2236` | `LONG` | 1,017,831.90 USD | `817.47` | `1467.80` | `1243.60` | `0.000000` | -182,049.32 USD | `-17.89%` | `10X Cross` |

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
  * 24H Horizon: Short MP=`1404.55` (Vol: 3,000,000.00 USD, Dist: `+12.89%`) | Long MP=`1176.48` (Vol: 3,400,000.00 USD, Dist: `--5.44%`)
  * 48H Horizon: Short MP=`1404.55` (Vol: 3,000,000.00 USD, Dist: `+12.89%`) | Long MP=`1176.48` (Vol: 3,400,000.00 USD, Dist: `--5.44%`)
  * 3D Horizon: Short MP=`1404.55` (Vol: 3,000,000.00 USD, Dist: `+12.89%`) | Long MP=`1176.48` (Vol: 3,400,000.00 USD, Dist: `--5.44%`)
  * 7D Horizon: Short MP=`1404.10` (Vol: 3,000,000.00 USD, Dist: `+12.85%`) | Long MP=`1176.74` (Vol: 4,900,000.00 USD, Dist: `--5.42%`)
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
| `5m` | `BALANCED` | 0.00 USD | 1,750.00 USD | 1,750.00 USD | 1,750.00 USD | `1` | `2026-10-30 09:40:00 UTC - 2026-10-30 09:45:00 UTC` |
| `15m` | `BALANCED` | 0.00 USD | 1,750.00 USD | 1,750.00 USD | 1,750.00 USD | `1` | `2026-10-30 09:30:00 UTC - 2026-10-30 09:45:00 UTC` |
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
  * Current Rate: `84.13K` | Last 24h: `171.90K` | Last 3d: `285.15K` | Last 7d: `847.79K`
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
| `5:00 UTC` | `1263.15` | `1263.66` | `1263.15` | `1267.05` | `1260.45` | 8,382,487.91 USD | 4,193,725.38 USD | 4,188,762.53 USD | 4,962.85 USD | `+0.06%` | `3B / 2S` |
| `0:00 UTC` | `1255.05` | `1256.16` | `1255.05` | `1269.15` | `1247.25` | 26,236,011.28 USD | 8,922,234.21 USD | 17,313,777.08 USD | -8,391,542.87 USD | `-31.98%` | `2B / 24S` |
| `5:00 UTC` | `1248.15` | `1248.05` | `1248.15` | `1253.25` | `1244.25` | 21,008,122.73 USD | 11,395,427.09 USD | 9,612,695.64 USD | 1,782,731.45 USD | `+8.49%` | `1B / 0S` |
| `0:00 UTC` | `1245.75` | `1245.57` | `1245.75` | `1250.55` | `1240.05` | 17,224,192.69 USD | 9,235,789.14 USD | 7,988,403.55 USD | 1,247,385.58 USD | `+7.24%` | `1B / 6S` |
| `5:00 UTC` | `1251.45` | `1250.99` | `1251.45` | `1255.05` | `1246.35` | 13,619,576.55 USD | 6,741,413.50 USD | 6,878,163.05 USD | -136,749.55 USD | `-1.00%` | `2B / 0S` |
| `0:00 UTC` | `1249.95` | `1249.10` | `1249.95` | `1253.55` | `1244.55` | 10,263,783.49 USD | 5,117,369.60 USD | 5,146,413.89 USD | -29,044.29 USD | `-0.28%` | `1B / 4S` |
| `5:00 UTC` | `1246.65` | `1246.77` | `1246.65` | `1252.35` | `1243.95` | 13,017,000.97 USD | 7,727,648.32 USD | 5,289,352.64 USD | 2,438,295.68 USD | `+18.73%` | `8B / 5S` |
| `0:00 UTC` | `1244.55` | `1245.81` | `1244.55` | `1249.05` | `1243.65` | 9,717,386.64 USD | 3,914,194.68 USD | 5,803,191.96 USD | -1,888,997.28 USD | `-19.44%` | `0B / 1S` |
| `5:00 UTC` | `1242.15` | `1244.40` | `1242.15` | `1249.35` | `1241.25` | 8,638,502.97 USD | 4,533,952.89 USD | 4,104,550.08 USD | 429,402.82 USD | `+4.97%` | `4B / 2S` |
| `0:00 UTC` | `1245.75` | `1244.36` | `1245.75` | `1246.95` | `1240.05` | 3,381,121.79 USD | 1,725,659.73 USD | 1,655,462.07 USD | 70,197.66 USD | `+2.08%` | `0B / 3S` |

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
| `5m` | -147,980.00 USD | 574,330.00 USD | **`ACCUMULATION`** |
| `15m` | -708,230.00 USD | 1,700,000.00 USD | **`ACCUMULATION`** |
| `30m` | -1,750,000.00 USD | 473,720.00 USD | **`DISTRIBUTION`** |
| `1h` | -2,730,000.00 USD | 4,210,000.00 USD | **`ACCUMULATION`** |
| `2h` | 202,640.00 USD | -4,690,000.00 USD | **`DISTRIBUTION`** |
| `4h` | 1,430,000.00 USD | -22,190,000.00 USD | **`DISTRIBUTION`** |
| `6h` | -1,910,000.00 USD | -41,350,000.00 USD | **`DISTRIBUTION`** |
| `8h` | 7,560,000.00 USD | 4,290,000.00 USD | **`ACCUMULATION`** |
| `12h` | 626,250.00 USD | -31,420,000.00 USD | **`DISTRIBUTION`** |
| `24h` | 19,380,000.00 USD | 73,890,000.00 USD | **`ACCUMULATION`** |
| `1w` | 34,900,000.00 USD | 203,700,000.00 USD | **`ACCUMULATION`** |
| `30d` | 62,180,000.00 USD | -541,890,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-147.98K` | 15m=`-708.23K` | 1h=`-2.73M` | 24h=`+19.38M`
* Futures Capital Netflows: 5m=`+574.33K` | 15m=`+1.70M` | 1h=`+4.21M` | 24h=`+73.89M`
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
  * `2026-10-30 14:41:27 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 14:38:27 IST`: [@FirstSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 14:33:27 IST`: [destatis.de] - (Sentiment: `Neutral`)
  * `2026-10-30 14:33:27 IST`: [istat.it] - (Sentiment: `Neutral`)
  * `2026-10-30 14:09:27 IST`: [channelnewsasia.com] - (Sentiment: `Neutral`)
  * `2026-10-30 15:06:27 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 15:06:27 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 15:06:27 IST`: [kof.ethz.ch] - (Sentiment: `Neutral`)
  * `2026-10-30 15:06:27 IST`: [gerlachmacro.substack.com] - (Sentiment: `Neutral`)
  * `2026-10-30 15:06:27 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-30 15:06:27 IST`: [insee.fr] - (Sentiment: `Neutral`)
  * `2026-10-30 15:06:27 IST`: [insee.fr] - (Sentiment: `Neutral`)
  * `2026-10-30 15:05:27 IST`: [@FirstSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 15:05:27 IST`: [nationwide.co.uk] - (Sentiment: `Neutral`)
  * `2026-10-30 15:05:27 IST`: [destatis.de] - (Sentiment: `Neutral`)


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
  * Spread-Padded Stop Loss: `1221.62` (Risk Distance: `16.01` pts)
  * +2.5R Take Profit: `1277.66`
  * Mathematical Lot Sizing: **`0.62 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `1280.15` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `1296.16` (Risk Distance: `16.01` pts)
  * +2.5R Take Profit: `1240.12`
  * Mathematical Lot Sizing: **`0.62 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`1259.24`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
