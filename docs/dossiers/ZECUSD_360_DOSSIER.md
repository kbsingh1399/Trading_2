# 🏛️ SOVEREIGN CANDIDATE DOSSIER: ZECUSD
**Canonical Key**: `ZECUSD` | **Broker Instrument**: `ZECUSD.p` | **Asset Class**: `Crypto Altcoin`
**Timestamp**: `2026-10-30 04:16:49 IST` (`2026-10-29 22:46:49 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `1250.60` | **Live Ask Quote**: `1252.15` | **Mid Price**: `1251.38`
- **Spread Points**: `155.00` | **Spread BPS**: `12.39 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `1251.38` | VWAP Z-Score: `+0.00` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `3.13` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `50.00` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `1260.13` | Lower -3.00σ Band: `1242.62`
  * Upper +2.51σ Band: `1258.26` | Lower -2.51σ Band: `1244.49`
  * Upper +2.01σ Band: `1256.63` | Lower -2.01σ Band: `1246.12`
  * Upper +2.00σ Band: `1256.38` | Lower -2.00σ Band: `1246.37`
  * Upper +1.28σ Band: `1254.88` | Lower -1.28σ Band: `1247.87`
  * Upper +1.00σ Band: `1253.88` | Lower -1.00σ Band: `1248.87`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`1251.38` | EMA-20=`1251.38` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`1251.38` (Slope: `+0.0000`) | EMA-100=`1251.38`
  * Institutional Anchors: EMA-144=`1251.38` | EMA-200=`1251.38` (Slope: `+0.0000`) | EMA-233=`1251.38`
- **Range Boundaries**: 24H High=`1263.89` | 24H Low=`1238.86` | Weekly High=`1276.40` | Weekly Low=`1226.35`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `1271.11` (Distance: `-1.75%`)
  * Point of Control (POC) = `1260.05` (Distance: `-0.89%`)
  * Value Area Low (VAL) = `1244.56` (Distance: `+0.34%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`1309.91` | POC=`1246.71` | VAL=`1230.27`
  * Prior Day Extremes: PDH=`1396.49` | PDL=`1206.89` | PDC=`1244.38`
  * Monday Range Blueprint: High=`1267.53` | Mid=`1222.14` | Low=`1176.75`
  * Developing Weekly Value Area: Weekly VAH=`1297.61` | Weekly POC=`1239.01` | Weekly VAL=`1199.46`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`1296.00` | Low=`1240.69`
  * London Session (08:00-16:00 UTC): High=`1256.38` | Low=`1246.37`
  * New York Session (13:00-21:00 UTC): High=`1258.88` | Low=`1243.87`
  * Initial Balance (First Hour): IB High=`1255.13` | IB Low=`1247.62`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `1246.37` - `1256.38`
  * Optimal Trade Entry (OTE 0.705): `1253.88`
  * Structural Invalidation Anchor (0.786): `1261.39`

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
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 04:16:04 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `16` | `0xb83d...6e36` | `SHORT` | 65,565,654.25 USD | `52,385.47` | `1336.45` | `1255.80` | `3989.16` | 4,444,913.15 USD | `+6.78%` | `3X Cross` |
| `23` | `0x5b5d...c060` | `SHORT` | 50,324,246.93 USD | `40,121.38` | `1478.36` | `1255.80` | `5453.53` | 8,989,788.18 USD | `+17.86%` | `3X Cross` |
| `44` | `0x7fda...17d1` | `SHORT` | 29,214,165.15 USD | `23,352.65` | `1262.37` | `1255.80` | `2738.70` | 265,613.89 USD | `+0.91%` | `5X Cross` |
| `85` | `0x60b0...991e` | `LONG` | 21,025,014.22 USD | `16,779.74` | `1179.65` | `1255.80` | `928.98` | 1,230,767.21 USD | `+5.85%` | `10X Cross` |
| `142` | `0xc36a...105b` | `LONG` | 14,401,186.90 USD | `11,510.82` | `1215.14` | `1255.80` | `960.02` | 413,905.87 USD | `+2.87%` | `10X Cross` |
| `158` | `0x9071...5c0b` | `LONG` | 13,192,888.58 USD | `10,517.29` | `1353.83` | `1255.80` | `0.0163` | -1,045,730.30 USD | `-7.93%` | `1X Cross` |
| `182` | `0x8742...8427` | `LONG` | 11,533,716.73 USD | `9,201.21` | `1286.37` | `1255.80` | `707.52` | -302,453.26 USD | `-2.62%` | `10X Cross` |
| `203` | `0x9ffd...ce40` | `LONG` | 10,635,333.46 USD | `8,475.72` | `1256.47` | `1255.80` | `609.70` | -14,142.40 USD | `-0.13%` | `5X Cross` |
| `204` | `0xad59...ba81` | `SHORT` | 10,555,682.50 USD | `8,425.00` | `330.91` | `1255.80` | `2144.79` | -7,767,724.73 USD | `-73.59%` | `10X Cross` |
| `212` | `0xdd53...2b13` | `SHORT` | 10,247,823.72 USD | `8,168.20` | `739.52` | `1255.80` | `8607.17` | -4,207,313.53 USD | `-41.06%` | `3X Cross` |
| `219` | `0xbf73...5d58` | `LONG` | 10,009,600.00 USD | `8,000.00` | `1291.41` | `1255.80` | `295.69` | -321,656.76 USD | `-3.21%` | `10X Cross` |
| `236` | `0x880a...311c` | `SHORT` | 9,643,906.74 USD | `7,707.11` | `1367.50` | `1255.80` | `2263.26` | 895,577.46 USD | `+9.29%` | `10X Cross` |
| `279` | `0x2b61...2f6c` | `LONG` | 8,517,599.10 USD | `6,807.00` | `1453.56` | `1255.80` | `542.41` | -1,376,752.12 USD | `-16.16%` | `10X Cross` |
| `294` | `0x2ae5...83e7` | `LONG` | 8,074,321.92 USD | `6,436.80` | `1391.82` | `1255.80` | `0.000000` | -884,570.07 USD | `-10.96%` | `1X Cross` |
| `341` | `0x26b6...9a13` | `LONG` | 6,813,354.05 USD | `5,433.73` | `1282.23` | `1255.80` | `214.19` | -153,949.19 USD | `-2.26%` | `10X Cross` |
| `357` | `0x45d2...4029` | `SHORT` | 6,552,044.50 USD | `5,227.00` | `833.44` | `1255.80` | `8854.93` | -2,195,666.53 USD | `-33.51%` | `5X Cross` |
| `378` | `0x9321...d75a` | `SHORT` | 6,259,500.00 USD | `5,000.00` | `1252.00` | `1255.80` | `2210.49` | 489.19 USD | `+0.01%` | `10X Cross` |
| `380` | `0xea00...a918` | `LONG` | 6,253,000.00 USD | `5,000.00` | `739.16` | `1255.80` | `0.000000` | 2,557,184.89 USD | `+40.90%` | `5X Cross` |
| `382` | `0x58b2...11f3` | `LONG` | 6,218,739.24 USD | `4,963.08` | `1257.17` | `1255.80` | `0.000000` | -20,671.95 USD | `-0.33%` | `10X Cross` |
| `386` | `0xecb6...2b00` | `SHORT` | 6,103,203.66 USD | `4,878.66` | `1304.86` | `1255.80` | `6872.70` | 262,788.66 USD | `+4.31%` | `5X Cross` |
| `388` | `0xdd7a...8830` | `LONG` | 6,089,332.05 USD | `4,860.19` | `897.48` | `1255.80` | `790.69` | 1,727,428.38 USD | `+28.37%` | `10X Cross` |
| `440` | `0x4cae...7c34` | `LONG` | 5,014,259.59 USD | `4,004.36` | `999.34` | `1255.80` | `952.03` | 1,012,531.44 USD | `+20.19%` | `10X Cross` |
| `452` | `0xa61c...66b9` | `LONG` | 4,870,108.80 USD | `3,888.00` | `1148.34` | `1255.80` | `0.000000` | 405,366.66 USD | `+8.32%` | `10X Cross` |
| `473` | `0x9aa5...58af` | `SHORT` | 4,649,271.41 USD | `3,720.31` | `1205.51` | `1255.80` | `3638.98` | -164,384.61 USD | `-3.54%` | `10X Cross` |
| `475` | `0x0153...8052` | `SHORT` | 4,633,449.72 USD | `3,698.18` | `1307.82` | `1255.80` | `2504.73` | 203,121.03 USD | `+4.38%` | `1X Isolated` |
| `544` | `0xd21d...90f1` | `LONG` | 4,071,925.00 USD | `3,250.00` | `1253.64` | `1255.80` | `875.93` | -2,416.73 USD | `-0.06%` | `4X Isolated` |
| `562` | `0x1338...c48e` | `LONG` | 3,965,132.37 USD | `3,149.43` | `1018.52` | `1255.80` | `820.23` | 757,386.83 USD | `+19.10%` | `4X Isolated` |
| `575` | `0xd4c1...3d1d` | `SHORT` | 3,936,046.32 USD | `3,146.32` | `1299.23` | `1255.80` | `2820.01` | 151,742.83 USD | `+3.86%` | `10X Cross` |
| `576` | `0x456f...cdf1` | `LONG` | 3,927,039.83 USD | `3,134.11` | `1268.47` | `1255.80` | `493.71` | -48,469.64 USD | `-1.23%` | `10X Cross` |
| `581` | `0x382b...3e39` | `LONG` | 3,893,624.91 USD | `3,112.41` | `1211.32` | `1255.80` | `0.000000` | 123,491.28 USD | `+3.17%` | `10X Cross` |
| `585` | `0xdbe0...d6d5` | `LONG` | 3,868,745.44 USD | `3,085.37` | `422.97` | `1255.80` | `338.54` | 2,563,740.95 USD | `+66.27%` | `3X Isolated` |
| `592` | `0x27c9...d65d` | `SHORT` | 3,810,696.12 USD | `3,046.12` | `1254.41` | `1255.80` | `1756.59` | 10,390.68 USD | `+0.27%` | `10X Cross` |
| `602` | `0x325e...9564` | `LONG` | 3,760,192.47 USD | `3,001.91` | `1301.41` | `1255.80` | `162.26` | -146,516.74 USD | `-3.90%` | `10X Cross` |
| `604` | `0x9c06...0560` | `SHORT` | 3,750,106.14 USD | `2,989.80` | `786.00` | `1255.80` | `2545.08` | -1,400,111.14 USD | `-37.34%` | `10X Cross` |
| `619` | `0x2e30...4cb5` | `SHORT` | 3,684,359.45 USD | `2,938.32` | `1297.88` | `1255.80` | `2885.90` | 129,229.57 USD | `+3.51%` | `2X Cross` |
| `638` | `0xac48...3201` | `LONG` | 3,550,563.18 USD | `2,838.18` | `1378.58` | `1255.80` | `621.37` | -362,091.66 USD | `-10.20%` | `10X Cross` |
| `712` | `0xa183...0482` | `LONG` | 3,178,649.60 USD | `2,534.00` | `530.25` | `1255.80` | `444.47` | 1,834,986.88 USD | `+57.73%` | `5X Isolated` |
| `729` | `0x0871...e927` | `LONG` | 3,128,250.00 USD | `2,500.00` | `1276.50` | `1255.80` | `0.000000` | -63,000.00 USD | `-2.01%` | `10X Cross` |
| `742` | `0x9b86...6e6e` | `LONG` | 3,078,878.67 USD | `2,463.30` | `637.58` | `1255.80` | `882.40` | 1,508,329.39 USD | `+48.99%` | `3X Cross` |
| `782` | `0xb2f7...af9f` | `SHORT` | 2,898,859.79 USD | `2,313.72` | `746.63` | `1255.80` | `4377.79` | -1,171,371.04 USD | `-40.41%` | `10X Cross` |
| `809` | `0xf48f...10fe` | `LONG` | 2,779,546.12 USD | `2,218.49` | `1517.87` | `1255.80` | `973.51` | -587,840.70 USD | `-21.15%` | `3X Cross` |
| `841` | `0x5bc4...3b0c` | `SHORT` | 2,673,013.33 USD | `2,130.74` | `1089.65` | `1255.80` | `3666.92` | -351,255.75 USD | `-13.14%` | `5X Cross` |
| `856` | `0x8de4...b9aa` | `SHORT` | 2,624,150.69 USD | `2,091.29` | `1331.35` | `1255.80` | `1689.86` | 160,089.01 USD | `+6.10%` | `3X Cross` |
| `868` | `0x4fe2...ac59` | `SHORT` | 2,592,777.01 USD | `2,071.57` | `1478.56` | `1255.80` | `1838.91` | 470,169.20 USD | `+18.13%` | `10X Cross` |
| `892` | `0x9a99...d21a` | `LONG` | 2,506,000.00 USD | `2,000.00` | `1278.44` | `1255.80` | `0.000000` | -50,873.67 USD | `-2.03%` | `10X Cross` |
| `925` | `0x77ee...2902` | `SHORT` | 2,435,067.34 USD | `1,946.03` | `759.84` | `1255.80` | `5319.89` | -956,389.83 USD | `-39.28%` | `10X Cross` |
| `928` | `0x3e2f...b269` | `SHORT` | 2,415,744.85 USD | `1,925.51` | `1134.87` | `1255.80` | `2931.78` | -230,545.99 USD | `-9.54%` | `10X Cross` |
| `934` | `0xe097...d0fe` | `LONG` | 2,399,412.88 USD | `1,913.56` | `1261.17` | `1255.80` | `0.000000` | -13,913.28 USD | `-0.58%` | `10X Cross` |
| `941` | `0x4f12...618b` | `SHORT` | 2,376,038.84 USD | `1,896.28` | `1608.30` | `1255.80` | `2116.75` | 673,745.55 USD | `+28.36%` | `3X Cross` |
| `986` | `0x866d...d6e1` | `LONG` | 2,266,978.90 USD | `1,802.05` | `674.73` | `1255.80` | `225.68` | 1,051,077.59 USD | `+46.36%` | `10X Cross` |
| `1013` | `0x2309...a2d9` | `LONG` | 2,189,887.91 USD | `1,750.37` | `1186.09` | `1255.80` | `814.92` | 113,793.80 USD | `+5.20%` | `8X Cross` |
| `1032` | `0x2edd...8179` | `SHORT` | 2,131,737.31 USD | `1,701.85` | `1261.58` | `1255.80` | `3079.70` | 15,281.54 USD | `+0.72%` | `10X Cross` |
| `1033` | `0x023a...2355` | `SHORT` | 2,124,885.59 USD | `1,696.38` | `1313.00` | `1255.80` | `5209.87` | 102,461.71 USD | `+4.82%` | `10X Cross` |
| `1045` | `0x71d0...8c26` | `SHORT` | 2,108,535.48 USD | `1,685.48` | `1289.75` | `1255.80` | `4637.24` | 65,315.61 USD | `+3.10%` | `10X Cross` |
| `1065` | `0xfe7c...b7ae` | `SHORT` | 2,056,816.87 USD | `1,640.99` | `1347.05` | `1255.80` | `6955.94` | 153,672.32 USD | `+7.47%` | `10X Cross` |
| `1071` | `0x3e47...aaf6` | `LONG` | 2,047,968.05 USD | `1,636.28` | `1278.38` | `1255.80` | `1048.78` | -43,823.74 USD | `-2.14%` | `10X Cross` |
| `1074` | `0xa271...a3f7` | `LONG` | 2,039,940.07 USD | `1,631.43` | `1190.60` | `1255.80` | `910.32` | 97,558.27 USD | `+4.78%` | `4X Cross` |
| `1086` | `0x7f75...9edf` | `LONG` | 2,019,910.66 USD | `1,605.78` | `1199.97` | `1255.80` | `977.67` | 93,018.77 USD | `+4.61%` | `10X Cross` |
| `1098` | `0x265e...7f70` | `LONG` | 2,004,737.78 USD | `1,601.74` | `1388.09` | `1255.80` | `0.000000` | -218,627.22 USD | `-10.91%` | `3X Cross` |
| `1099` | `0x6646...6de5` | `SHORT` | 2,004,640.00 USD | `1,600.00` | `660.64` | `1255.80` | `4483.24` | -947,615.03 USD | `-47.27%` | `10X Cross` |
| `1118` | `0xdf57...93f5` | `LONG` | 1,981,966.90 USD | `1,579.76` | `1218.38` | `1255.80` | `780.17` | 57,210.92 USD | `+2.89%` | `3X Isolated` |
| `1135` | `0xab59...59b5` | `LONG` | 1,961,345.96 USD | `1,565.32` | `1342.15` | `1255.80` | `829.14` | -139,549.26 USD | `-7.11%` | `10X Cross` |
| `1189` | `0xcf67...eb24` | `LONG` | 1,879,500.00 USD | `1,500.00` | `887.05` | `1255.80` | `667.82` | 548,928.63 USD | `+29.21%` | `10X Cross` |
| `1195` | `0xb695...a92d` | `LONG` | 1,858,940.50 USD | `1,483.00` | `1249.80` | `1255.80` | `0.000000` | 5,481.65 USD | `+0.29%` | `10X Cross` |
| `1274` | `0x2ab7...c2f8` | `LONG` | 1,756,799.74 USD | `1,400.51` | `813.26` | `1255.80` | `791.17` | 617,818.06 USD | `+35.17%` | `3X Cross` |
| `1296` | `0x11be...8b1d` | `LONG` | 1,723,914.99 USD | `1,375.83` | `1206.55` | `1255.80` | `1134.45` | 63,907.03 USD | `+3.71%` | `10X Isolated` |
| `1392` | `0xe065...0f85` | `SHORT` | 1,582,050.33 USD | `1,262.61` | `1087.02` | `1255.80` | `1824.40` | -209,574.20 USD | `-13.25%` | `10X Cross` |
| `1413` | `0x039c...0ebd` | `SHORT` | 1,566,814.09 USD | `1,250.55` | `1239.86` | `1255.80` | `3642.61` | -16,302.81 USD | `-1.04%` | `10X Cross` |
| `1433` | `0x7277...0b98` | `SHORT` | 1,549,380.82 USD | `1,234.96` | `1298.48` | `1255.80` | `2414.20` | 54,188.60 USD | `+3.50%` | `10X Cross` |
| `1467` | `0x5975...9abd` | `LONG` | 1,503,600.00 USD | `1,200.00` | `1179.54` | `1255.80` | `544.46` | 88,157.21 USD | `+5.86%` | `5X Cross` |
| `1468` | `0xdf83...3cff` | `SHORT` | 1,502,264.10 USD | `1,198.36` | `1255.46` | `1255.80` | `1767.82` | 2,232.43 USD | `+0.15%` | `10X Cross` |
| `1500` | `0x69cc...14fd` | `SHORT` | 1,457,042.26 USD | `1,161.36` | `675.33` | `1255.80` | `8052.88` | -672,736.73 USD | `-46.17%` | `10X Cross` |
| `1521` | `0x3fc5...c0c1` | `SHORT` | 1,440,143.76 USD | `1,148.44` | `1264.34` | `1255.80` | `3078.54` | 11,870.02 USD | `+0.82%` | `10X Cross` |
| `1541` | `0x2847...d47b` | `LONG` | 1,420,677.65 USD | `1,133.64` | `1233.82` | `1255.80` | `0.000000` | 21,969.13 USD | `+1.55%` | `5X Cross` |
| `1550` | `0xe35c...a1d3` | `LONG` | 1,411,755.36 USD | `1,127.06` | `1318.20` | `1255.80` | `694.37` | -73,939.99 USD | `-5.24%` | `2X Isolated` |
| `1564` | `0x5f94...4b96` | `LONG` | 1,397,321.78 USD | `1,115.27` | `538.00` | `1255.80` | `0.000000` | 797,304.15 USD | `+57.06%` | `10X Cross` |
| `1565` | `0x51f6...2b39` | `SHORT` | 1,395,765.72 USD | `1,115.72` | `1299.77` | `1255.80` | `2682.71` | 54,411.89 USD | `+3.90%` | `10X Cross` |
| `1566` | `0xfc27...9d9d` | `SHORT` | 1,395,294.21 USD | `1,112.32` | `1315.10` | `1255.80` | `16306.19` | 67,517.55 USD | `+4.84%` | `10X Cross` |
| `1584` | `0x266b...efcb` | `LONG` | 1,378,190.00 USD | `1,100.00` | `863.84` | `1255.80` | `317.28` | 427,965.24 USD | `+31.05%` | `10X Cross` |
| `1587` | `0x71df...a23d` | `SHORT` | 1,374,277.76 USD | `1,098.28` | `513.50` | `1255.80` | `2551.11` | -810,307.57 USD | `-58.96%` | `2X Cross` |
| `1605` | `0xef96...9383` | `SHORT` | 1,350,707.68 USD | `1,078.84` | `1259.08` | `1255.80` | `5167.62` | 7,640.10 USD | `+0.57%` | `10X Cross` |
| `1609` | `0xbfc7...80b4` | `SHORT` | 1,344,932.50 USD | `1,075.00` | `558.03` | `1255.80` | `4465.22` | -745,053.77 USD | `-55.40%` | `10X Cross` |
| `1686` | `0x123d...3bff` | `SHORT` | 1,260,334.95 USD | `1,008.51` | `490.16` | `1255.80` | `4510.37` | -766,006.11 USD | `-60.78%` | `10X Cross` |
| `1691` | `0xb5ff...d912` | `LONG` | 1,254,400.00 USD | `1,000.00` | `1280.79` | `1255.80` | `452.80` | -26,387.44 USD | `-2.10%` | `2X Cross` |
| `1692` | `0xe282...df29` | `LONG` | 1,251,600.00 USD | `1,000.00` | `420.99` | `1255.80` | `192.40` | 830,613.14 USD | `+66.36%` | `10X Cross` |
| `1693` | `0x668c...ea2e` | `SHORT` | 1,251,100.00 USD | `1,000.00` | `1406.98` | `1255.80` | `4181.44` | 155,881.99 USD | `+12.46%` | `10X Cross` |
| `1708` | `0x17f0...094f` | `LONG` | 1,240,808.58 USD | `984.30` | `1287.23` | `1255.80` | `536.80` | -26,211.58 USD | `-2.11%` | `5X Cross` |
| `1792` | `0x757d...94ba` | `LONG` | 1,160,412.50 USD | `925.00` | `1558.31` | `1255.80` | `0.000000` | -281,028.09 USD | `-24.22%` | `10X Cross` |
| `1828` | `0xb911...5525` | `LONG` | 1,127,700.00 USD | `900.00` | `1294.82` | `1255.80` | `1070.32` | -37,637.82 USD | `-3.34%` | `10X Cross` |
| `1874` | `0xcf0a...856f` | `LONG` | 1,089,982.88 USD | `871.15` | `1292.19` | `1255.80` | `996.97` | -35,711.97 USD | `-3.28%` | `4X Cross` |
| `1895` | `0xdf95...7d72` | `SHORT` | 1,071,742.72 USD | `857.60` | `1074.38` | `1255.80` | `45711.07` | -150,351.68 USD | `-14.03%` | `10X Cross` |
| `1941` | `0x601c...4f54` | `SHORT` | 1,033,492.91 USD | `824.42` | `615.11` | `1255.80` | `3110.84` | -526,380.16 USD | `-50.93%` | `5X Cross` |
| `1956` | `0xae55...2236` | `LONG` | 1,024,698.65 USD | `817.47` | `1467.80` | `1255.80` | `0.000000` | -175,182.57 USD | `-17.10%` | `10X Cross` |
| `2003` | `0x0f02...5384` | `LONG` | 1,003,697.65 USD | `800.78` | `1290.36` | `1255.80` | `302.19` | -29,596.42 USD | `-2.95%` | `3X Cross` |
| `2004` | `0x7a76...b16d` | `LONG` | 1,003,272.20 USD | `800.76` | `1297.31` | `1255.80` | `1189.00` | -35,562.80 USD | `-3.54%` | `10X Cross` |
| `2005` | `0x9b0f...db40` | `LONG` | 1,002,960.00 USD | `800.00` | `1268.86` | `1255.80` | `788.62` | -12,129.76 USD | `-1.21%` | `10X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `1131.00` | 5,553.21 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 5.55K USD at 1131.0000 USD [API] | `2026-10-24 14:16:46` |
| `ANNOUNCEMENT` | `INFO` | `1351.00` | 13.51 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Long: 0.01K USD at 1351.0000 USD [API] | `2026-10-05 21:05:42` |
| `ANNOUNCEMENT` | `INFO` | `1183.40` | 3,928.89 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 3.93K USD at 1183.4000 USD [API] | `2026-10-20 13:59:40` |
| `ANNOUNCEMENT` | `INFO` | `1183.40` | 23.67 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 0.02K USD at 1183.4000 USD [API] | `2026-10-20 13:59:40` |
| `ANNOUNCEMENT` | `INFO` | `1183.40` | 11.83 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 0.01K USD at 1183.4000 USD [API] | `2026-10-20 13:59:40` |
| `ANNOUNCEMENT` | `INFO` | `1183.40` | 3,136.01 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 3.14K USD at 1183.4000 USD [API] | `2026-10-20 13:59:40` |
| `ANNOUNCEMENT` | `INFO` | `1248.70` | 3,671.18 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 3.67K USD at 1248.7000 USD [API] | `2026-10-14 00:30:06` |
| `ANNOUNCEMENT` | `INFO` | `1248.60` | 74.92 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 0.07K USD at 1248.6000 USD [API] | `2026-10-14 00:30:06` |
| `ANNOUNCEMENT` | `INFO` | `1314.50` | 302.34 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 0.30K USD at 1314.5000 USD [API] | `2026-10-12 04:36:03` |
| `ANNOUNCEMENT` | `INFO` | `1314.50` | 3,641.16 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 3.64K USD at 1314.5000 USD [API] | `2026-10-12 04:36:03` |
| `ANNOUNCEMENT` | `INFO` | `1284.20` | 1,887.77 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 1.89K USD at 1284.2000 USD [API] | `2026-10-11 16:30:00` |
| `ANNOUNCEMENT` | `INFO` | `1284.20` | 89.89 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 0.09K USD at 1284.2000 USD [API] | `2026-10-11 16:30:00` |
| `ANNOUNCEMENT` | `INFO` | `1284.20` | 179.79 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 0.18K USD at 1284.2000 USD [API] | `2026-10-11 16:30:00` |
| `ANNOUNCEMENT` | `INFO` | `1284.20` | 783.36 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 0.78K USD at 1284.2000 USD [API] | `2026-10-11 16:30:00` |
| `ANNOUNCEMENT` | `INFO` | `1284.10` | 975.92 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 0.98K USD at 1284.1000 USD [API] | `2026-10-11 16:30:00` |
| `ANNOUNCEMENT` | `INFO` | `1284.10` | 77.05 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 0.08K USD at 1284.1000 USD [API] | `2026-10-11 16:30:00` |
| `ANNOUNCEMENT` | `INFO` | `1284.10` | 1,284.10 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 1.28K USD at 1284.1000 USD [API] | `2026-10-11 16:30:00` |
| `ANNOUNCEMENT` | `INFO` | `1284.00` | 1,284.00 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 1.28K USD at 1284.0000 USD [API] | `2026-10-11 16:30:00` |
| `ANNOUNCEMENT` | `INFO` | `1284.00` | 975.84 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 0.98K USD at 1284.0000 USD [API] | `2026-10-11 16:30:00` |
| `ANNOUNCEMENT` | `INFO` | `1284.00` | 102.72 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 0.10K USD at 1284.0000 USD [API] | `2026-10-11 16:30:00` |
| `ANNOUNCEMENT` | `INFO` | `1284.00` | 12.84 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 0.01K USD at 1284.0000 USD [API] | `2026-10-11 16:30:00` |
| `ANNOUNCEMENT` | `INFO` | `1283.90` | 12.84 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 0.01K USD at 1283.9000 USD [API] | `2026-10-11 16:30:00` |
| `ANNOUNCEMENT` | `INFO` | `1283.80` | 12.84 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 0.01K USD at 1283.8000 USD [API] | `2026-10-11 16:30:00` |
| `ANNOUNCEMENT` | `INFO` | `1283.80` | 12.84 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 0.01K USD at 1283.8000 USD [API] | `2026-10-11 16:30:00` |
| `ANNOUNCEMENT` | `INFO` | `1283.80` | 12.84 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 0.01K USD at 1283.8000 USD [API] | `2026-10-11 16:30:00` |
| `ANNOUNCEMENT` | `INFO` | `1536.50` | 4,609.50 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 4.61K USD at 1536.5000 USD [API] | `2026-09-24 16:28:40` |
| `ANNOUNCEMENT` | `INFO` | `1522.40` | 4,567.20 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 4.57K USD at 1522.4000 USD [API] | `2026-09-22 05:43:11` |
| `ANNOUNCEMENT` | `INFO` | `1509.70` | 332.13 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 0.33K USD at 1509.7000 USD [API] | `2026-09-20 19:32:55` |
| `ANNOUNCEMENT` | `INFO` | `1509.70` | 1,992.80 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 1.99K USD at 1509.7000 USD [API] | `2026-09-20 19:32:55` |
| `ANNOUNCEMENT` | `INFO` | `1509.70` | 105.68 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 0.11K USD at 1509.7000 USD [API] | `2026-09-20 19:32:55` |
| `ANNOUNCEMENT` | `INFO` | `1509.70` | 105.68 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 0.11K USD at 1509.7000 USD [API] | `2026-09-20 19:32:55` |
| `ANNOUNCEMENT` | `INFO` | `1509.70` | 1,992.80 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 1.99K USD at 1509.7000 USD [API] | `2026-09-20 19:32:55` |
| `ANNOUNCEMENT` | `INFO` | `1509.70` | 3,019.40 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 3.02K USD at 1509.7000 USD [API] | `2026-09-20 19:32:55` |
| `ANNOUNCEMENT` | `INFO` | `1536.40` | 3,917.82 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 3.92K USD at 1536.4000 USD [API] | `2026-09-18 22:58:29` |
| `ANNOUNCEMENT` | `INFO` | `1536.40` | 1,628.58 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 1.63K USD at 1536.4000 USD [API] | `2026-09-18 22:58:29` |
| `ANNOUNCEMENT` | `INFO` | `1536.40` | 1,966.59 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 1.97K USD at 1536.4000 USD [API] | `2026-09-18 22:58:29` |
| `ANNOUNCEMENT` | `INFO` | `1536.40` | 169.00 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 0.17K USD at 1536.4000 USD [API] | `2026-09-18 22:58:29` |
| `ANNOUNCEMENT` | `INFO` | `1172.70` | 3,518.10 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 3.52K USD at 1172.7000 USD [API] | `2026-09-14 18:22:41` |
| `ANNOUNCEMENT` | `INFO` | `1124.90` | 3,374.70 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 3.37K USD at 1124.9000 USD [API] | `2026-09-14 04:10:24` |
| `ANNOUNCEMENT` | `INFO` | `1151.40` | 3,454.20 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 3.45K USD at 1151.4000 USD [API] | `2026-09-11 12:29:35` |
| `ANNOUNCEMENT` | `INFO` | `1176.90` | 3,530.70 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 3.53K USD at 1176.9000 USD [API] | `2026-09-08 14:39:00` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`1403.54` (Vol: 3,000,000.00 USD, Dist: `+11.94%`) | Long MP=`0.000000` (Vol: 0.00 USD, Dist: `-0.00%`)
  * 48H Horizon: Short MP=`1403.54` (Vol: 3,000,000.00 USD, Dist: `+11.94%`) | Long MP=`0.000000` (Vol: 0.00 USD, Dist: `-0.00%`)
  * 3D Horizon: Short MP=`1403.54` (Vol: 3,000,000.00 USD, Dist: `+11.94%`) | Long MP=`0.000000` (Vol: 0.00 USD, Dist: `-0.00%`)
  * 7D Horizon: Short MP=`1404.10` (Vol: 3,000,000.00 USD, Dist: `+11.98%`) | Long MP=`1200.46` (Vol: 3,000,000.00 USD, Dist: `--4.26%`)
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
| `5m` | `BALANCED` | 0.00 USD | 1,750.00 USD | 1,750.00 USD | 1,750.00 USD | `1` | `2026-10-29 22:45:00 UTC - 2026-10-29 22:50:00 UTC` |
| `15m` | `BALANCED` | 0.00 USD | 1,750.00 USD | 1,750.00 USD | 1,750.00 USD | `1` | `2026-10-29 22:45:00 UTC - 2026-10-29 23:00:00 UTC` |
| `1h` | `BALANCED` | 0.00 USD | 1,750.00 USD | 1,750.00 USD | 1,750.00 USD | `1` | `2026-10-29 22:00:00 UTC - 2026-10-29 23:00:00 UTC` |
| `4h` | `BALANCED` | 0.00 USD | 1,750.00 USD | 1,750.00 USD | 1,750.00 USD | `1` | `2026-10-29 20:00:00 UTC - 2026-10-30 00:00:00 UTC` |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `0 USD` | Total OI Tokens: `-`
  * 1h OI Change: `0.00%` | 4h OI Change: `0.00%` | 24h OI Change: `0.00%`
  * Exchange Breakdown: Binance=`-` | Bybit=`-` | OKX=`-` | Hyperliquid=`-`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `9.79K` | Last 24h: `33.19K` | Last 3d: `283.86K` | Last 7d: `777.60K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `-0.0014%` | **USDT OKX** | `0.0012%` |
| **USDT Bybit** | `0.0100%` | **USDT KuCoin** | `-0.0055%` |
| **USDT MEXC** | `-0.0014%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `0.0015%` | **USDT Bitget** | `0.0100%` |
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
| `5:00 UTC` | `1306.05` | `1306.88` | `1306.05` | `1312.05` | `1300.05` | 17,712,248.68 USD | 9,074,345.66 USD | 8,637,903.02 USD | 436,442.64 USD | `+2.46%` | `3B / 5S` |
| `0:00 UTC` | `1249.20` | `1269.32` | `1249.20` | `1308.60` | `1241.40` | 130,590,816.99 USD | 58,796,845.15 USD | 71,793,971.84 USD | -12,997,126.69 USD | `-9.95%` | `4B / 19S` |
| `5:00 UTC` | `1229.25` | `1237.79` | `1229.25` | `1264.35` | `1206.75` | 149,162,484.89 USD | 77,012,548.38 USD | 72,149,936.51 USD | 4,862,611.87 USD | `+3.26%` | `9B / 11S` |
| `0:00 UTC` | `1249.95` | `1248.07` | `1249.95` | `1259.85` | `1233.15` | 61,152,789.32 USD | 32,267,997.87 USD | 28,884,791.45 USD | 3,383,206.41 USD | `+5.53%` | `6B / 4S` |
| `5:00 UTC` | `1273.95` | `1271.85` | `1273.95` | `1286.25` | `1253.25` | 67,607,862.35 USD | 37,234,359.13 USD | 30,373,503.22 USD | 6,860,855.91 USD | `+10.15%` | `6B / 2S` |
| `0:00 UTC` | `1294.65` | `1287.25` | `1294.65` | `1297.05` | `1269.15` | 47,983,765.84 USD | 24,978,907.15 USD | 23,004,858.69 USD | 1,974,048.46 USD | `+4.11%` | `4B / 9S` |
| `5:00 UTC` | `1264.05` | `1267.99` | `1264.05` | `1276.65` | `1260.75` | 31,349,361.20 USD | 15,100,777.24 USD | 16,248,583.96 USD | -1,147,806.72 USD | `-3.66%` | `0B / 1S` |
| `0:00 UTC` | `1261.05` | `1255.07` | `1261.05` | `1269.15` | `1241.25` | 60,510,539.13 USD | 31,467,084.85 USD | 29,043,454.28 USD | 2,423,630.57 USD | `+4.01%` | `3B / 5S` |
| `5:00 UTC` | `1259.85` | `1254.56` | `1259.85` | `1263.15` | `1242.15` | 22,141,749.31 USD | 11,943,317.16 USD | 10,198,432.15 USD | 1,744,885.01 USD | `+7.88%` | `3B / 3S` |
| `0:00 UTC` | `1257.15` | `1255.21` | `1257.15` | `1264.35` | `1245.45` | 26,228,868.78 USD | 11,671,225.80 USD | 14,557,642.98 USD | -2,886,417.18 USD | `-11.00%` | `7B / 2S` |

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
| `5m` | 54,980.00 USD | -868,020.00 USD | **`DISTRIBUTION`** |
| `15m` | -84,720.00 USD | 4,620,000.00 USD | **`ACCUMULATION`** |
| `30m` | 177,350.00 USD | 6,440,000.00 USD | **`ACCUMULATION`** |
| `1h` | 1,540,000.00 USD | 614,040.00 USD | **`ACCUMULATION`** |
| `2h` | -4,470,000.00 USD | 5,320,000.00 USD | **`ACCUMULATION`** |
| `4h` | -9,970,000.00 USD | -243,950.00 USD | **`DISTRIBUTION`** |
| `6h` | -7,080,000.00 USD | -15,120,000.00 USD | **`DISTRIBUTION`** |
| `8h` | 8,550,000.00 USD | 83,630,000.00 USD | **`ACCUMULATION`** |
| `12h` | 22,050,000.00 USD | 101,060,000.00 USD | **`ACCUMULATION`** |
| `24h` | 3,290,000.00 USD | 66,610,000.00 USD | **`ACCUMULATION`** |
| `1w` | 36,370,000.00 USD | 253,700,000.00 USD | **`ACCUMULATION`** |
| `30d` | 58,640,000.00 USD | -534,500,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+54.98K` | 15m=`-84.72K` | 1h=`+1.54M` | 24h=`+3.29M`
* Futures Capital Netflows: 5m=`-868.02K` | 15m=`+4.62M` | 1h=`+614.04K` | 24h=`+66.61M`
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
  * `2026-10-30 03:30:16 IST`: [investinglive.com] - (Sentiment: `Neutral`)
  * `2026-10-30 04:11:16 IST`: [msn.com] - (Sentiment: `Neutral`)
  * `2026-10-30 04:11:16 IST`: [morningstar.com] - (Sentiment: `Neutral`)
  * `2026-10-30 04:10:16 IST`: [sec.gov] - (Sentiment: `Neutral`)
  * `2026-10-30 01:12:17 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 01:12:17 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 01:12:17 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 00:12:17 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 00:12:17 IST`: [@DeItaone] - (Sentiment: `Neutral`)
  * `2026-10-29 23:12:17 IST`: [@mb_ghalibaf] - (Sentiment: `Neutral`)
  * `2026-10-29 23:12:17 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-29 23:12:17 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-29 23:12:17 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:12:17 IST`: [fxstreet.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:12:17 IST`: [ForexFactory] - (Sentiment: `Neutral`)


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
  * Execution Entry: `1244.56` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `1238.48` (Risk Distance: `6.08` pts)
  * +2.5R Take Profit: `1259.76`
  * Mathematical Lot Sizing: **`1.64 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `1271.11` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `1277.19` (Risk Distance: `6.08` pts)
  * +2.5R Take Profit: `1255.91`
  * Mathematical Lot Sizing: **`1.64 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`1261.39`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
