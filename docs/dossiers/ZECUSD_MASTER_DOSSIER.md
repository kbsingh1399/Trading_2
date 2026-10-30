# 🏛️ SOVEREIGN CANDIDATE DOSSIER: ZECUSD
**Canonical Key**: `ZECUSD` | **Broker Instrument**: `ZECUSD.p` | **Asset Class**: `Crypto Altcoin`
**Timestamp**: `2026-10-30 16:03:29 IST` (`2026-10-30 10:33:29 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `1268.04` | **Live Ask Quote**: `1269.02` | **Mid Price**: `1268.53`
- **Spread Points**: `98.00` | **Spread BPS**: `7.73 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `1253.52` | VWAP Z-Score: `+0.45` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `12.31` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `53.57` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `1314.84` | Lower -3.00σ Band: `1192.19`
  * Upper +2.51σ Band: `1304.83` | Lower -2.51σ Band: `1202.21`
  * Upper +2.01σ Band: `1294.61` | Lower -2.01σ Band: `1212.43`
  * Upper +2.00σ Band: `1294.40` | Lower -2.00σ Band: `1212.63`
  * Upper +1.28σ Band: `1279.68` | Lower -1.28σ Band: `1227.35`
  * Upper +1.00σ Band: `1273.96` | Lower -1.00σ Band: `1233.07`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`1252.82` | EMA-20=`1255.47` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`1261.26` (Slope: `+0.0000`) | EMA-100=`1267.50`
  * Institutional Anchors: EMA-144=`1270.98` | EMA-200=`1275.76` (Slope: `-0.2646`) | EMA-233=`1275.77`
- **Range Boundaries**: 24H High=`1396.49` | 24H Low=`1180.03` | Weekly High=`1396.49` | Weekly Low=`1180.03`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `1280.15` (Distance: `-0.78%`)
  * Point of Control (POC) = `1247.68` (Distance: `+1.80%`)
  * Value Area Low (VAL) = `1239.95` (Distance: `+2.43%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`1309.91` | POC=`1246.71` | VAL=`1230.27`
  * Prior Day Extremes: PDH=`1396.49` | PDL=`1206.89` | PDC=`1244.38`
  * Monday Range Blueprint: High=`1267.53` | Mid=`1222.14` | Low=`1176.75`
  * Developing Weekly Value Area: Weekly VAH=`1293.21` | Weekly POC=`1240.47` | Weekly VAL=`1200.92`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`1296.00` | Low=`1180.03`
  * London Session (08:00-16:00 UTC): High=`1283.82` | Low=`1239.95`
  * New York Session (13:00-21:00 UTC): High=`1269.65` | Low=`1245.73`
  * Initial Balance (First Hour): IB High=`1283.82` | IB Low=`1264.92`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `1263.46` - `1273.60`
  * Optimal Trade Entry (OTE 0.705): `1271.07`
  * Structural Invalidation Anchor (0.786): `1278.68`

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
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 16:01:49 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `12` | `0xb83d...6e36` | `SHORT` | 65,806,627.41 USD | `52,385.47` | `1336.45` | `1257.60` | `3223.50` | 4,203,939.99 USD | `+6.39%` | `3X Cross` |
| `21` | `0x5b5d...c060` | `SHORT` | 50,412,513.97 USD | `40,121.38` | `1478.36` | `1257.60` | `4869.25` | 8,901,521.14 USD | `+17.66%` | `3X Cross` |
| `36` | `0x7fda...17d1` | `SHORT` | 33,460,030.14 USD | `26,635.91` | `1262.58` | `1257.60` | `2614.48` | 169,804.96 USD | `+0.51%` | `5X Cross` |
| `83` | `0x60b0...991e` | `LONG` | 21,078,709.39 USD | `16,779.74` | `1179.65` | `1257.60` | `916.66` | 1,284,462.37 USD | `+6.09%` | `10X Cross` |
| `140` | `0xc36a...105b` | `LONG` | 14,416,150.97 USD | `11,510.82` | `1215.14` | `1257.60` | `968.28` | 428,869.94 USD | `+2.97%` | `10X Cross` |
| `177` | `0x8742...8427` | `LONG` | 11,535,556.98 USD | `9,201.21` | `1286.37` | `1257.60` | `718.44` | -300,613.02 USD | `-2.61%` | `10X Cross` |
| `192` | `0x58b2...11f3` | `LONG` | 10,739,814.94 USD | `8,563.08` | `1246.56` | `1257.60` | `385.68` | 65,397.36 USD | `+0.61%` | `10X Cross` |
| `194` | `0x9071...5c0b` | `LONG` | 10,698,567.97 USD | `8,517.29` | `1353.83` | `1257.60` | `253.57` | -832,391.63 USD | `-7.78%` | `2X Cross` |
| `195` | `0x9ffd...ce40` | `LONG` | 10,668,149.90 USD | `8,490.37` | `1252.16` | `1257.60` | `602.91` | 36,855.24 USD | `+0.35%` | `5X Cross` |
| `199` | `0xad59...ba81` | `SHORT` | 10,577,587.50 USD | `8,425.00` | `330.91` | `1257.60` | `2147.46` | -7,789,629.73 USD | `-73.64%` | `10X Cross` |
| `203` | `0xdd53...2b13` | `SHORT` | 10,295,714.70 USD | `8,195.92` | `741.54` | `1257.60` | `8450.89` | -4,218,118.34 USD | `-40.97%` | `3X Cross` |
| `222` | `0x880a...311c` | `SHORT` | 9,652,384.56 USD | `7,707.11` | `1367.50` | `1257.60` | `2231.79` | 887,099.64 USD | `+9.19%` | `10X Cross` |
| `234` | `0xbf73...5d58` | `LONG` | 9,403,500.00 USD | `7,500.00` | `1248.78` | `1257.60` | `135.34` | 37,654.38 USD | `+0.40%` | `10X Cross` |
| `267` | `0x2b61...2f6c` | `LONG` | 8,553,676.20 USD | `6,807.00` | `1453.56` | `1257.60` | `564.85` | -1,340,675.02 USD | `-15.67%` | `10X Cross` |
| `287` | `0x2ae5...83e7` | `LONG` | 8,069,816.16 USD | `6,436.80` | `1391.82` | `1257.60` | `0.000000` | -889,075.83 USD | `-11.02%` | `1X Cross` |
| `319` | `0xecb6...2b00` | `SHORT` | 7,250,457.34 USD | `5,770.36` | `1277.61` | `1257.60` | `6122.19` | 121,805.74 USD | `+1.68%` | `5X Cross` |
| `335` | `0x26b6...9a13` | `LONG` | 6,825,308.25 USD | `5,433.73` | `1282.23` | `1257.60` | `233.26` | -141,994.98 USD | `-2.08%` | `10X Cross` |
| `349` | `0x45d2...4029` | `SHORT` | 6,565,634.70 USD | `5,227.00` | `833.44` | `1257.60` | `9134.15` | -2,209,256.73 USD | `-33.65%` | `5X Cross` |
| `365` | `0xea00...a918` | `LONG` | 6,281,000.00 USD | `5,000.00` | `739.16` | `1257.60` | `0.000000` | 2,585,184.89 USD | `+41.16%` | `5X Cross` |
| `377` | `0xdd7a...8830` | `LONG` | 6,099,538.45 USD | `4,860.19` | `897.48` | `1257.60` | `784.63` | 1,737,634.78 USD | `+28.49%` | `10X Cross` |
| `419` | `0x469e...58a5` | `SHORT` | 5,231,879.23 USD | `4,163.52` | `1242.31` | `1257.60` | `1954.41` | -59,494.58 USD | `-1.14%` | `10X Cross` |
| `429` | `0x4cae...7c34` | `LONG` | 5,092,082.48 USD | `4,052.27` | `1170.79` | `1257.60` | `973.46` | 347,706.39 USD | `+6.83%` | `10X Cross` |
| `440` | `0x382b...3e39` | `LONG` | 4,936,627.32 USD | `3,929.81` | `1220.71` | `1257.60` | `0.000000` | 139,463.56 USD | `+2.83%` | `10X Cross` |
| `441` | `0xd4c1...3d1d` | `SHORT` | 4,936,612.93 USD | `3,930.24` | `1291.66` | `1257.60` | `2354.84` | 139,923.17 USD | `+2.83%` | `10X Cross` |
| `447` | `0xa61c...66b9` | `LONG` | 4,875,940.80 USD | `3,888.00` | `1148.34` | `1257.60` | `0.000000` | 411,198.66 USD | `+8.43%` | `10X Cross` |
| `473` | `0x9aa5...58af` | `SHORT` | 4,662,664.52 USD | `3,720.31` | `1205.51` | `1257.60` | `3690.24` | -177,777.72 USD | `-3.81%` | `10X Cross` |
| `476` | `0x0153...8052` | `SHORT` | 4,635,298.81 USD | `3,698.18` | `1307.82` | `1257.60` | `2504.94` | 201,271.94 USD | `+4.34%` | `1X Isolated` |
| `506` | `0xb122...e4ba` | `LONG` | 4,387,781.07 USD | `3,498.47` | `1265.25` | `1257.60` | `1101.12` | -38,670.45 USD | `-0.88%` | `10X Cross` |
| `539` | `0xd21d...90f1` | `LONG` | 4,080,375.00 USD | `3,250.00` | `1253.64` | `1257.60` | `876.17` | 6,033.27 USD | `+0.15%` | `4X Isolated` |
| `541` | `0x456f...cdf1` | `LONG` | 4,063,957.74 USD | `3,235.12` | `1267.53` | `1257.60` | `518.58` | -36,654.81 USD | `-0.90%` | `10X Cross` |
| `559` | `0x1338...c48e` | `LONG` | 3,948,755.33 USD | `3,149.43` | `1018.52` | `1257.60` | `820.46` | 741,009.79 USD | `+18.77%` | `4X Isolated` |
| `576` | `0xdbe0...d6d5` | `LONG` | 3,867,511.29 USD | `3,085.37` | `422.97` | `1257.60` | `338.78` | 2,562,506.80 USD | `+66.26%` | `3X Isolated` |
| `592` | `0x325e...9564` | `LONG` | 3,763,441.23 USD | `3,000.91` | `1298.07` | `1257.60` | `152.09` | -131,963.93 USD | `-3.51%` | `10X Cross` |
| `594` | `0x9c06...0560` | `SHORT` | 3,756,683.70 USD | `2,989.80` | `786.00` | `1257.60` | `2570.05` | -1,406,688.70 USD | `-37.44%` | `10X Cross` |
| `596` | `0x2e30...4cb5` | `SHORT` | 3,740,975.60 USD | `2,983.71` | `1282.27` | `1257.60` | `2895.21` | 84,959.73 USD | `+2.27%` | `2X Cross` |
| `606` | `0x27c9...d65d` | `SHORT` | 3,690,765.85 USD | `2,938.04` | `1254.41` | `1257.60` | `1732.52` | -5,255.80 USD | `-0.14%` | `10X Cross` |
| `699` | `0xa183...0482` | `LONG` | 3,183,971.00 USD | `2,534.00` | `530.25` | `1257.60` | `444.70` | 1,840,308.28 USD | `+57.80%` | `5X Isolated` |
| `700` | `0xac48...3201` | `LONG` | 3,180,070.30 USD | `2,531.50` | `1378.58` | `1257.60` | `540.92` | -309,801.98 USD | `-9.74%` | `10X Cross` |
| `712` | `0x0871...e927` | `LONG` | 3,134,750.00 USD | `2,500.00` | `1276.50` | `1257.60` | `0.000000` | -56,500.00 USD | `-1.80%` | `10X Cross` |
| `731` | `0x9b86...6e6e` | `LONG` | 3,092,673.15 USD | `2,463.30` | `637.58` | `1257.60` | `882.63` | 1,522,123.87 USD | `+49.22%` | `3X Cross` |
| `807` | `0xf48f...10fe` | `LONG` | 2,785,314.19 USD | `2,218.49` | `1517.87` | `1257.60` | `987.64` | -582,072.63 USD | `-20.90%` | `3X Cross` |
| `829` | `0x71d0...8c26` | `SHORT` | 2,697,048.84 USD | `2,146.99` | `1265.96` | `1257.60` | `3809.30` | 20,954.00 USD | `+0.78%` | `10X Cross` |
| `839` | `0x5bc4...3b0c` | `SHORT` | 2,669,817.22 USD | `2,130.74` | `1089.65` | `1257.60` | `3682.79` | -348,059.64 USD | `-13.04%` | `5X Cross` |
| `851` | `0x8de4...b9aa` | `SHORT` | 2,622,477.66 USD | `2,091.29` | `1331.35` | `1257.60` | `1690.07` | 161,762.05 USD | `+6.17%` | `3X Cross` |
| `860` | `0x4fe2...ac59` | `SHORT` | 2,598,370.25 USD | `2,071.57` | `1478.56` | `1257.60` | `1845.11` | 464,575.96 USD | `+17.88%` | `10X Cross` |
| `864` | `0xdf57...93f5` | `LONG` | 2,574,511.42 USD | `2,054.35` | `1227.36` | `1257.60` | `897.41` | 53,089.38 USD | `+2.06%` | `4X Isolated` |
| `869` | `0xbcd4...0dd2` | `LONG` | 2,554,723.32 USD | `2,033.92` | `1228.20` | `1257.60` | `763.93` | 56,672.50 USD | `+2.22%` | `10X Cross` |
| `877` | `0x9a99...d21a` | `LONG` | 2,508,400.00 USD | `2,000.00` | `1278.44` | `1257.60` | `0.000000` | -48,473.67 USD | `-1.93%` | `10X Cross` |
| `878` | `0xf29c...9971` | `LONG` | 2,507,400.00 USD | `2,000.00` | `1254.95` | `1257.60` | `0.000000` | -2,497.07 USD | `-0.10%` | `10X Cross` |
| `900` | `0x77ee...2902` | `SHORT` | 2,445,381.30 USD | `1,946.03` | `759.84` | `1257.60` | `5738.77` | -966,703.79 USD | `-39.53%` | `10X Cross` |
| `912` | `0x3e2f...b269` | `SHORT` | 2,412,664.03 USD | `1,925.51` | `1134.87` | `1257.60` | `2977.34` | -227,465.17 USD | `-9.43%` | `10X Cross` |
| `930` | `0x4f12...618b` | `SHORT` | 2,382,675.82 USD | `1,896.28` | `1608.30` | `1257.60` | `2116.96` | 667,108.57 USD | `+28.00%` | `3X Cross` |
| `970` | `0x866d...d6e1` | `LONG` | 2,259,410.29 USD | `1,802.05` | `674.73` | `1257.60` | `122.42` | 1,043,508.98 USD | `+46.19%` | `10X Cross` |
| `991` | `0x2309...a2d9` | `LONG` | 2,199,514.94 USD | `1,750.37` | `1186.09` | `1257.60` | `807.72` | 123,420.83 USD | `+5.61%` | `8X Cross` |
| `1031` | `0x265e...7f70` | `LONG` | 2,071,612.31 USD | `1,651.74` | `1382.98` | `1257.60` | `0.000000` | -212,710.45 USD | `-10.27%` | `3X Cross` |
| `1035` | `0xfe7c...b7ae` | `SHORT` | 2,063,252.59 USD | `1,642.64` | `1346.92` | `1257.60` | `5702.83` | 149,256.03 USD | `+7.23%` | `10X Cross` |
| `1041` | `0x3e47...aaf6` | `LONG` | 2,055,264.06 USD | `1,636.28` | `1278.38` | `1257.60` | `1050.15` | -36,527.73 USD | `-1.78%` | `10X Cross` |
| `1043` | `0x2edd...8179` | `SHORT` | 2,054,887.24 USD | `1,635.98` | `1261.55` | `1257.60` | `2859.39` | 8,975.64 USD | `+0.44%` | `10X Cross` |
| `1064` | `0x7f75...9edf` | `LONG` | 2,021,338.75 USD | `1,612.17` | `1200.26` | `1257.60` | `987.14` | 86,317.67 USD | `+4.27%` | `10X Cross` |
| `1070` | `0xfc27...9d9d` | `SHORT` | 2,011,737.17 USD | `1,604.64` | `1295.09` | `1257.60` | `13042.82` | 66,408.64 USD | `+3.30%` | `10X Cross` |
| `1078` | `0x6646...6de5` | `SHORT` | 2,000,000.00 USD | `1,600.00` | `660.64` | `1257.60` | `4177.47` | -942,975.03 USD | `-47.15%` | `10X Cross` |
| `1080` | `0x023a...2355` | `SHORT` | 1,998,779.09 USD | `1,591.31` | `1310.00` | `1257.60` | `4418.38` | 85,830.16 USD | `+4.29%` | `10X Cross` |
| `1094` | `0xab59...59b5` | `LONG` | 1,966,134.12 USD | `1,565.32` | `1342.15` | `1257.60` | `838.67` | -134,761.10 USD | `-6.85%` | `10X Cross` |
| `1146` | `0x039c...0ebd` | `SHORT` | 1,909,344.45 USD | `1,521.39` | `1245.17` | `1257.60` | `3765.34` | -14,950.59 USD | `-0.78%` | `10X Cross` |
| `1161` | `0xcf67...eb24` | `LONG` | 1,881,300.00 USD | `1,500.00` | `887.05` | `1257.60` | `620.78` | 550,728.63 USD | `+29.27%` | `10X Cross` |
| `1174` | `0x7277...0b98` | `SHORT` | 1,849,384.84 USD | `1,475.73` | `1287.86` | `1257.60` | `2208.57` | 51,147.29 USD | `+2.77%` | `10X Cross` |
| `1233` | `0x3205...40bb` | `SHORT` | 1,778,416.11 USD | `1,415.87` | `1257.03` | `1257.60` | `2294.41` | 1,368.84 USD | `+0.08%` | `10X Cross` |
| `1247` | `0x2ab7...c2f8` | `LONG` | 1,759,040.56 USD | `1,400.51` | `813.26` | `1257.60` | `792.33` | 620,058.87 USD | `+35.25%` | `3X Cross` |
| `1248` | `0x926a...af36` | `LONG` | 1,757,846.89 USD | `1,401.68` | `1254.50` | `1257.60` | `1187.92` | -555.01 USD | `-0.03%` | `10X Isolated` |
| `1265` | `0x11be...8b1d` | `LONG` | 1,728,317.65 USD | `1,375.83` | `1206.55` | `1257.60` | `1134.68` | 68,309.69 USD | `+3.95%` | `10X Isolated` |
| `1324` | `0x5323...b23c` | `SHORT` | 1,626,741.32 USD | `1,298.07` | `1253.90` | `1257.60` | `5539.29` | 913.36 USD | `+0.06%` | `5X Cross` |
| `1337` | `0xdf83...3cff` | `SHORT` | 1,609,802.10 USD | `1,282.20` | `1260.35` | `1257.60` | `1858.30` | 6,221.25 USD | `+0.39%` | `10X Cross` |
| `1351` | `0xe065...0f85` | `SHORT` | 1,583,691.72 USD | `1,262.61` | `1087.02` | `1257.60` | `1548.60` | -211,215.60 USD | `-13.34%` | `10X Cross` |
| `1361` | `0x413c...886c` | `LONG` | 1,570,073.62 USD | `1,250.00` | `1237.51` | `1257.60` | `0.000000` | 23,184.17 USD | `+1.48%` | `10X Cross` |
| `1419` | `0x2847...d47b` | `LONG` | 1,519,120.83 USD | `1,211.71` | `1232.45` | `1257.60` | `0.000000` | 25,753.23 USD | `+1.70%` | `5X Cross` |
| `1438` | `0x5975...9abd` | `LONG` | 1,507,440.00 USD | `1,200.00` | `1179.54` | `1257.60` | `545.05` | 91,997.21 USD | `+6.10%` | `5X Cross` |
| `1442` | `0x266b...efcb` | `LONG` | 1,503,840.00 USD | `1,200.00` | `893.76` | `1257.60` | `416.83` | 431,330.30 USD | `+28.68%` | `10X Cross` |
| `1471` | `0x69cc...14fd` | `SHORT` | 1,455,416.35 USD | `1,161.36` | `675.33` | `1257.60` | `8104.33` | -671,110.82 USD | `-46.11%` | `10X Cross` |
| `1480` | `0x3fc5...c0c1` | `SHORT` | 1,442,508.28 USD | `1,148.44` | `1264.34` | `1257.60` | `2799.83` | 9,505.49 USD | `+0.66%` | `10X Cross` |
| `1526` | `0x5f94...4b96` | `LONG` | 1,400,221.49 USD | `1,115.27` | `538.00` | `1257.60` | `0.000000` | 800,203.85 USD | `+57.15%` | `10X Cross` |
| `1533` | `0xe35c...a1d3` | `LONG` | 1,393,756.58 USD | `1,111.36` | `1311.66` | `1257.60` | `690.98` | -63,967.57 USD | `-4.59%` | `2X Isolated` |
| `1552` | `0x71df...a23d` | `SHORT` | 1,377,133.29 USD | `1,098.28` | `513.50` | `1257.60` | `2561.67` | -813,163.10 USD | `-59.05%` | `2X Cross` |
| `1577` | `0xbfc7...80b4` | `SHORT` | 1,350,845.00 USD | `1,075.00` | `558.03` | `1257.60` | `2705.36` | -750,966.27 USD | `-55.59%` | `10X Cross` |
| `1604` | `0x123d...3bff` | `SHORT` | 1,311,899.91 USD | `1,044.34` | `519.62` | `1257.60` | `4104.49` | -769,241.70 USD | `-58.64%` | `10X Cross` |
| `1663` | `0x668c...ea2e` | `SHORT` | 1,256,600.00 USD | `1,000.00` | `1406.98` | `1257.60` | `4213.15` | 150,381.99 USD | `+11.97%` | `10X Cross` |
| `1667` | `0xe282...df29` | `LONG` | 1,254,100.00 USD | `1,000.00` | `420.99` | `1257.60` | `809.91` | 833,113.14 USD | `+66.43%` | `10X Cross` |
| `1686` | `0x17f0...094f` | `LONG` | 1,236,871.38 USD | `984.30` | `1287.23` | `1257.60` | `537.03` | -30,148.78 USD | `-2.44%` | `5X Cross` |
| `1709` | `0x51f6...2b39` | `SHORT` | 1,219,222.77 USD | `972.81` | `1299.77` | `1257.60` | `2515.71` | 45,204.93 USD | `+3.71%` | `10X Cross` |
| `1728` | `0xef96...9383` | `SHORT` | 1,194,750.67 USD | `951.19` | `1258.85` | `1257.60` | `4859.60` | 2,656.19 USD | `+0.22%` | `10X Cross` |
| `1729` | `0x38f9...cb04` | `SHORT` | 1,194,738.10 USD | `951.18` | `1253.73` | `1257.60` | `2159.07` | -2,216.48 USD | `-0.19%` | `10X Cross` |
| `1774` | `0x757d...94ba` | `LONG` | 1,159,025.00 USD | `925.00` | `1558.31` | `1257.60` | `0.000000` | -282,415.59 USD | `-24.37%` | `10X Cross` |
| `1816` | `0xb911...5525` | `LONG` | 1,130,453.01 USD | `900.00` | `1294.82` | `1257.60` | `1035.46` | -34,884.81 USD | `-3.09%` | `10X Cross` |
| `1858` | `0xcf0a...856f` | `LONG` | 1,094,599.98 USD | `871.15` | `1292.19` | `1257.60` | `1027.58` | -31,094.87 USD | `-2.84%` | `4X Cross` |
| `1883` | `0xdf95...7d72` | `SHORT` | 1,072,219.08 USD | `853.27` | `1074.39` | `1257.60` | `45382.74` | -155,471.64 USD | `-14.50%` | `10X Cross` |
| `1910` | `0xb2f7...af9f` | `SHORT` | 1,042,968.96 USD | `830.72` | `746.63` | `1257.60` | `8266.70` | -422,729.93 USD | `-40.53%` | `10X Cross` |
| `1922` | `0x601c...4f54` | `SHORT` | 1,035,966.17 USD | `824.42` | `615.11` | `1257.60` | `3138.41` | -528,853.42 USD | `-51.05%` | `5X Cross` |
| `1940` | `0xae55...2236` | `LONG` | 1,024,862.14 USD | `817.47` | `1467.80` | `1257.60` | `0.000000` | -175,019.08 USD | `-17.08%` | `10X Cross` |
| `1979` | `0x0f02...5384` | `LONG` | 1,003,937.89 USD | `800.78` | `1290.36` | `1257.60` | `305.87` | -29,356.18 USD | `-2.92%` | `3X Cross` |
| `1984` | `0x9b0f...db40` | `LONG` | 1,003,040.00 USD | `800.00` | `1268.86` | `1257.60` | `802.12` | -12,049.76 USD | `-1.20%` | `10X Cross` |

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
| `ANNOUNCEMENT` | `INFO` | `1017.00` | 10.17 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Long: 0.01K USD at 1017.0000 USD [API] | `2026-09-04 08:53:37` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`1404.55` (Vol: 3,000,000.00 USD, Dist: `+11.02%`) | Long MP=`1176.48` (Vol: 3,400,000.00 USD, Dist: `--7.01%`)
  * 48H Horizon: Short MP=`1404.55` (Vol: 3,000,000.00 USD, Dist: `+11.02%`) | Long MP=`1176.48` (Vol: 3,400,000.00 USD, Dist: `--7.01%`)
  * 3D Horizon: Short MP=`1404.55` (Vol: 3,000,000.00 USD, Dist: `+11.02%`) | Long MP=`1176.48` (Vol: 3,400,000.00 USD, Dist: `--7.01%`)
  * 7D Horizon: Short MP=`1404.10` (Vol: 3,000,000.00 USD, Dist: `+10.99%`) | Long MP=`1176.74` (Vol: 4,900,000.00 USD, Dist: `--6.98%`)
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
| `5m` | `BALANCED` | 0.00 USD | 1,750.00 USD | 1,750.00 USD | 1,750.00 USD | `1` | `2026-10-30 10:30:00 UTC - 2026-10-30 10:35:00 UTC` |
| `15m` | `BALANCED` | 0.00 USD | 1,750.00 USD | 1,750.00 USD | 1,750.00 USD | `1` | `2026-10-30 10:30:00 UTC - 2026-10-30 10:45:00 UTC` |
| `1h` | `BALANCED` | 0.00 USD | 1,750.00 USD | 1,750.00 USD | 1,750.00 USD | `1` | `2026-10-30 10:00:00 UTC - 2026-10-30 11:00:00 UTC` |
| `4h` | `BALANCED` | 0.00 USD | 1,750.00 USD | 1,750.00 USD | 1,750.00 USD | `1` | `2026-10-30 08:00:00 UTC - 2026-10-30 12:00:00 UTC` |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `0 USD` | Total OI Tokens: `-`
  * 1h OI Change: `0.00%` | 4h OI Change: `0.00%` | 24h OI Change: `0.00%`
  * Exchange Breakdown: Binance=`-` | Bybit=`-` | OKX=`-` | Hyperliquid=`-`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `84.92K` | Last 24h: `171.90K` | Last 3d: `285.15K` | Last 7d: `847.79K`
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
| `0:00 UTC` | `1245.75` | `1245.57` | `1245.75` | `1250.55` | `1240.05` | 17,224,192.69 USD | 9,235,789.14 USD | 7,988,403.55 USD | 1,247,385.58 USD | `+7.24%` | `1B / 6S` |
| `5:00 UTC` | `1251.45` | `1250.99` | `1251.45` | `1255.05` | `1246.35` | 13,619,576.55 USD | 6,741,413.50 USD | 6,878,163.05 USD | -136,749.55 USD | `-1.00%` | `2B / 0S` |
| `0:00 UTC` | `1249.95` | `1249.10` | `1249.95` | `1253.55` | `1244.55` | 10,263,783.49 USD | 5,117,369.60 USD | 5,146,413.89 USD | -29,044.29 USD | `-0.28%` | `1B / 4S` |
| `5:00 UTC` | `1246.65` | `1246.77` | `1246.65` | `1252.35` | `1243.95` | 13,017,000.97 USD | 7,727,648.32 USD | 5,289,352.64 USD | 2,438,295.68 USD | `+18.73%` | `8B / 5S` |
| `0:00 UTC` | `1244.55` | `1245.81` | `1244.55` | `1249.05` | `1243.65` | 9,717,386.64 USD | 3,914,194.68 USD | 5,803,191.96 USD | -1,888,997.28 USD | `-19.44%` | `0B / 1S` |
| `5:00 UTC` | `1242.15` | `1244.40` | `1242.15` | `1249.35` | `1241.25` | 8,638,502.97 USD | 4,533,952.89 USD | 4,104,550.08 USD | 429,402.82 USD | `+4.97%` | `4B / 2S` |
| `0:00 UTC` | `1251.15` | `1247.35` | `1251.15` | `1251.75` | `1240.05` | 9,977,652.60 USD | 4,992,881.35 USD | 4,984,771.25 USD | 8,110.10 USD | `+0.08%` | `3B / 5S` |
| `5:00 UTC` | `1243.95` | `1249.40` | `1243.95` | `1256.55` | `1243.35` | 15,678,426.53 USD | 9,268,825.46 USD | 6,409,601.07 USD | 2,859,224.38 USD | `+18.24%` | `10B / 2S` |
| `0:00 UTC` | `1249.95` | `1250.19` | `1249.95` | `1256.25` | `1246.35` | 11,248,393.80 USD | 4,953,252.73 USD | 6,295,141.07 USD | -1,341,888.34 USD | `-11.93%` | `1B / 7S` |
| `5:00 UTC` | `1264.05` | `1259.46` | `1264.05` | `1266.15` | `1247.85` | 17,817,119.53 USD | 9,795,980.05 USD | 8,021,139.48 USD | 1,774,840.58 USD | `+9.96%` | `11B / 4S` |

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
| `5m` | 462,240.00 USD | 2,420,000.00 USD | **`ACCUMULATION`** |
| `15m` | 642,450.00 USD | 3,880,000.00 USD | **`ACCUMULATION`** |
| `30m` | 91,860.00 USD | 3,490,000.00 USD | **`ACCUMULATION`** |
| `1h` | -437,220.00 USD | 7,290,000.00 USD | **`ACCUMULATION`** |
| `2h` | -2,590,000.00 USD | 9,960,000.00 USD | **`ACCUMULATION`** |
| `4h` | 728,700.00 USD | -11,170,000.00 USD | **`DISTRIBUTION`** |
| `6h` | -456,770.00 USD | -27,770,000.00 USD | **`DISTRIBUTION`** |
| `8h` | 877,270.00 USD | -8,730,000.00 USD | **`DISTRIBUTION`** |
| `12h` | 360,890.00 USD | -21,470,000.00 USD | **`DISTRIBUTION`** |
| `24h` | 22,930,000.00 USD | 79,410,000.00 USD | **`ACCUMULATION`** |
| `1w` | 35,710,000.00 USD | 226,880,000.00 USD | **`ACCUMULATION`** |
| `30d` | 61,300,000.00 USD | -568,060,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+462.24K` | 15m=`+642.45K` | 1h=`-437.22K` | 24h=`+22.93M`
* Futures Capital Netflows: 5m=`+2.42M` | 15m=`+3.88M` | 1h=`+7.29M` | 24h=`+79.41M`
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
  * `2026-10-30 15:49:55 IST`: [istat.it] - (Sentiment: `Neutral`)
  * `2026-10-30 15:32:55 IST`: [ec.europa.eu] - (Sentiment: `Neutral`)
  * `2026-10-30 15:31:55 IST`: [ec.europa.eu] - (Sentiment: `Neutral`)
  * `2026-10-30 15:18:55 IST`: [dailyforex.com] - (Sentiment: `Neutral`)
  * `2026-10-30 15:12:55 IST`: [breakingthenews.net] - (Sentiment: `Neutral`)
  * `2026-10-30 15:56:55 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 15:56:55 IST`: [@FirstSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 15:56:55 IST`: [destatis.de] - (Sentiment: `Neutral`)
  * `2026-10-30 15:56:55 IST`: [istat.it] - (Sentiment: `Neutral`)
  * `2026-10-30 15:56:55 IST`: [channelnewsasia.com] - (Sentiment: `Neutral`)
  * `2026-10-30 15:55:55 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 15:55:55 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 15:55:55 IST`: [kof.ethz.ch] - (Sentiment: `Neutral`)
  * `2026-10-30 15:55:55 IST`: [gerlachmacro.substack.com] - (Sentiment: `Neutral`)
  * `2026-10-30 15:55:55 IST`: [@financialjuice] - (Sentiment: `Neutral`)


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
  * Execution Entry: `1239.95` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `1223.71` (Risk Distance: `16.24` pts)
  * +2.5R Take Profit: `1280.55`
  * Mathematical Lot Sizing: **`0.61 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `1280.15` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `1296.39` (Risk Distance: `16.24` pts)
  * +2.5R Take Profit: `1239.55`
  * Mathematical Lot Sizing: **`0.61 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`1278.68`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
