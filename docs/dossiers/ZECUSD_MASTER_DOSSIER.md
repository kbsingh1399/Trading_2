# 🏛️ SOVEREIGN CANDIDATE DOSSIER: ZECUSD
**Canonical Key**: `ZECUSD` | **Broker Instrument**: `ZECUSD.p` | **Asset Class**: `Crypto Altcoin`
**Timestamp**: `2026-10-30 11:05:06 IST` (`2026-10-30 05:35:06 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `1272.21` | **Live Ask Quote**: `1273.83` | **Mid Price**: `1273.02`
- **Spread Points**: `162.00` | **Spread BPS**: `12.73 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `1250.41` | VWAP Z-Score: `+0.84` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `16.24` (Volatility Regime: `HIGH_EXPANSION`)
  * 14-Period RSI: `53.05` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `1326.33` | Lower -3.00σ Band: `1174.48`
  * Upper +2.51σ Band: `1313.93` | Lower -2.51σ Band: `1186.88`
  * Upper +2.01σ Band: `1301.28` | Lower -2.01σ Band: `1199.54`
  * Upper +2.00σ Band: `1301.02` | Lower -2.00σ Band: `1199.79`
  * Upper +1.28σ Band: `1282.80` | Lower -1.28σ Band: `1218.01`
  * Upper +1.00σ Band: `1275.71` | Lower -1.00σ Band: `1225.10`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`1273.54` | EMA-20=`1266.36` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`1268.19` (Slope: `+0.0000`) | EMA-100=`1272.83`
  * Institutional Anchors: EMA-144=`1274.22` | EMA-200=`1275.86` (Slope: `-0.0168`) | EMA-233=`1278.10`
- **Range Boundaries**: 24H High=`1396.49` | 24H Low=`1180.03` | Weekly High=`1396.49` | Weekly Low=`1180.03`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `1285.56` (Distance: `-0.99%`)
  * Point of Control (POC) = `1275.51` (Distance: `-0.21%`)
  * Value Area Low (VAL) = `1233.76` (Distance: `+3.17%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`1309.91` | POC=`1246.71` | VAL=`1230.27`
  * Prior Day Extremes: PDH=`1396.49` | PDL=`1206.89` | PDC=`1244.38`
  * Monday Range Blueprint: High=`1267.53` | Mid=`1222.14` | Low=`1176.75`
  * Developing Weekly Value Area: Weekly VAH=`1296.14` | Weekly POC=`1239.01` | Weekly VAL=`1200.92`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`1296.00` | Low=`1180.03`
  * London Session (08:00-16:00 UTC): High=`1283.82` | Low=`1268.20`
  * New York Session (13:00-21:00 UTC): High=`1280.66` | Low=`1265.38`
  * Initial Balance (First Hour): IB High=`1283.82` | IB Low=`1268.20`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `1267.93` - `1278.11`
  * Optimal Trade Entry (OTE 0.705): `1275.57`
  * Structural Invalidation Anchor (0.786): `1283.20`

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
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 11:04:06 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `13` | `0xb83d...6e36` | `SHORT` | 66,849,098.27 USD | `52,385.47` | `1336.45` | `1274.10` | `3655.06` | 3,161,469.13 USD | `+4.73%` | `3X Cross` |
| `22` | `0x5b5d...c060` | `SHORT` | 51,198,893.02 USD | `40,121.38` | `1478.36` | `1274.10` | `5072.17` | 8,115,142.09 USD | `+15.85%` | `3X Cross` |
| `38` | `0x7fda...17d1` | `SHORT` | 33,337,879.22 USD | `26,067.62` | `1262.60` | `1274.10` | `2599.61` | -424,825.98 USD | `-1.27%` | `5X Cross` |
| `81` | `0x60b0...991e` | `LONG` | 21,390,812.55 USD | `16,779.74` | `1179.65` | `1274.10` | `913.42` | 1,596,565.54 USD | `+7.46%` | `10X Cross` |
| `141` | `0xc36a...105b` | `LONG` | 14,683,201.99 USD | `11,510.82` | `1215.14` | `1274.10` | `955.21` | 695,920.96 USD | `+4.74%` | `10X Cross` |
| `156` | `0x9071...5c0b` | `LONG` | 13,431,631.06 USD | `10,517.29` | `1353.83` | `1274.10` | `0.1605` | -806,987.81 USD | `-6.01%` | `1X Cross` |
| `177` | `0x8742...8427` | `LONG` | 11,750,865.29 USD | `9,201.21` | `1286.37` | `1274.10` | `696.71` | -85,304.70 USD | `-0.73%` | `10X Cross` |
| `192` | `0x58b2...11f3` | `LONG` | 10,927,346.39 USD | `8,563.08` | `1246.56` | `1274.10` | `382.23` | 252,928.81 USD | `+2.31%` | `10X Cross` |
| `196` | `0xad59...ba81` | `SHORT` | 10,747,772.50 USD | `8,425.00` | `330.91` | `1274.10` | `2144.39` | -7,959,814.73 USD | `-74.06%` | `10X Cross` |
| `197` | `0x9ffd...ce40` | `LONG` | 10,727,417.56 USD | `8,384.07` | `1251.71` | `1274.10` | `593.39` | 232,996.78 USD | `+2.17%` | `5X Cross` |
| `204` | `0xdd53...2b13` | `SHORT` | 10,467,009.43 USD | `8,195.92` | `741.54` | `1274.10` | `8377.53` | -4,389,413.07 USD | `-41.94%` | `3X Cross` |
| `222` | `0x880a...311c` | `SHORT` | 9,861,247.24 USD | `7,707.11` | `1367.50` | `1274.10` | `2271.50` | 678,236.96 USD | `+6.88%` | `10X Cross` |
| `235` | `0xbf73...5d58` | `LONG` | 9,574,500.00 USD | `7,500.00` | `1248.78` | `1274.10` | `111.66` | 208,654.38 USD | `+2.18%` | `10X Cross` |
| `270` | `0x2b61...2f6c` | `LONG` | 8,686,412.70 USD | `6,807.00` | `1453.56` | `1274.10` | `580.55` | -1,207,938.52 USD | `-13.91%` | `10X Cross` |
| `286` | `0x2ae5...83e7` | `LONG` | 8,220,437.28 USD | `6,436.80` | `1391.82` | `1274.10` | `0.000000` | -738,454.71 USD | `-8.98%` | `1X Cross` |
| `331` | `0x26b6...9a13` | `LONG` | 6,942,133.45 USD | `5,433.73` | `1282.23` | `1274.10` | `226.57` | -25,169.79 USD | `-0.36%` | `10X Cross` |
| `342` | `0xecb6...2b00` | `SHORT` | 6,698,704.31 USD | `5,254.71` | `1279.15` | `1274.10` | `6761.39` | 22,846.73 USD | `+0.34%` | `5X Cross` |
| `345` | `0x45d2...4029` | `SHORT` | 6,675,401.70 USD | `5,227.00` | `833.44` | `1274.10` | `8750.66` | -2,319,023.73 USD | `-34.74%` | `5X Cross` |
| `363` | `0xea00...a918` | `LONG` | 6,374,000.00 USD | `5,000.00` | `739.16` | `1274.10` | `0.000000` | 2,678,184.89 USD | `+42.02%` | `5X Cross` |
| `376` | `0xdd7a...8830` | `LONG` | 6,202,088.46 USD | `4,860.19` | `897.48` | `1274.10` | `782.49` | 1,840,184.79 USD | `+29.67%` | `10X Cross` |
| `421` | `0x469e...58a5` | `SHORT` | 5,325,142.08 USD | `4,163.52` | `1242.31` | `1274.10` | `1978.42` | -152,757.42 USD | `-2.87%` | `10X Cross` |
| `432` | `0x4cae...7c34` | `LONG` | 5,116,501.97 USD | `4,002.27` | `1169.72` | `1274.10` | `947.85` | 434,952.62 USD | `+8.50%` | `10X Cross` |
| `445` | `0xa61c...66b9` | `LONG` | 4,963,420.80 USD | `3,888.00` | `1148.34` | `1274.10` | `0.000000` | 498,678.66 USD | `+10.05%` | `10X Cross` |
| `471` | `0x9aa5...58af` | `SHORT` | 4,740,419.00 USD | `3,720.31` | `1205.51` | `1274.10` | `3651.02` | -255,532.20 USD | `-5.39%` | `10X Cross` |
| `473` | `0x0153...8052` | `SHORT` | 4,724,794.77 USD | `3,698.18` | `1307.82` | `1274.10` | `2504.86` | 111,775.98 USD | `+2.37%` | `1X Isolated` |
| `481` | `0xd4c1...3d1d` | `SHORT` | 4,690,215.52 USD | `3,680.91` | `1293.12` | `1274.10` | `2369.63` | 69,628.85 USD | `+1.48%` | `10X Cross` |
| `540` | `0x382b...3e39` | `LONG` | 4,165,593.50 USD | `3,269.44` | `1215.08` | `1274.10` | `0.000000` | 192,963.50 USD | `+4.63%` | `10X Cross` |
| `543` | `0xd21d...90f1` | `LONG` | 4,146,025.00 USD | `3,250.00` | `1253.64` | `1274.10` | `876.08` | 71,683.27 USD | `+1.73%` | `4X Isolated` |
| `552` | `0xb122...e4ba` | `LONG` | 4,104,720.62 USD | `3,221.41` | `1264.20` | `1274.10` | `1061.93` | 32,200.13 USD | `+0.78%` | `10X Cross` |
| `558` | `0x456f...cdf1` | `LONG` | 4,053,213.85 USD | `3,179.49` | `1267.80` | `1274.10` | `504.11` | 22,258.93 USD | `+0.55%` | `10X Cross` |
| `564` | `0x1338...c48e` | `LONG` | 4,026,861.20 USD | `3,149.43` | `1018.52` | `1274.10` | `820.37` | 819,115.66 USD | `+20.34%` | `4X Isolated` |
| `572` | `0x325e...9564` | `LONG` | 3,959,898.31 USD | `3,101.91` | `1298.07` | `1274.10` | `140.71` | -66,612.39 USD | `-1.68%` | `10X Cross` |
| `575` | `0xdbe0...d6d5` | `LONG` | 3,941,868.71 USD | `3,085.37` | `422.97` | `1274.10` | `338.69` | 2,636,864.22 USD | `+66.89%` | `3X Isolated` |
| `600` | `0x9c06...0560` | `SHORT` | 3,824,851.14 USD | `2,989.80` | `786.00` | `1274.10` | `2556.01` | -1,474,856.14 USD | `-38.56%` | `10X Cross` |
| `602` | `0x2e30...4cb5` | `SHORT` | 3,790,077.06 USD | `2,966.56` | `1287.28` | `1274.10` | `2887.98` | 28,712.23 USD | `+0.76%` | `2X Cross` |
| `604` | `0x27c9...d65d` | `SHORT` | 3,775,804.62 USD | `2,961.88` | `1254.41` | `1274.10` | `1735.24` | -60,389.42 USD | `-1.60%` | `10X Cross` |
| `635` | `0x5323...b23c` | `SHORT` | 3,562,508.76 USD | `2,789.53` | `1267.04` | `1274.10` | `3209.52` | -28,054.49 USD | `-0.79%` | `5X Cross` |
| `685` | `0x71d0...8c26` | `SHORT` | 3,300,406.21 USD | `2,588.96` | `1266.50` | `1274.10` | `3599.50` | -21,483.97 USD | `-0.65%` | `10X Cross` |
| `699` | `0xa183...0482` | `LONG` | 3,236,171.40 USD | `2,534.00` | `530.25` | `1274.10` | `444.61` | 1,892,508.68 USD | `+58.48%` | `5X Isolated` |
| `703` | `0xac48...3201` | `LONG` | 3,227,156.20 USD | `2,531.50` | `1378.58` | `1274.10` | `554.60` | -262,716.08 USD | `-8.14%` | `10X Cross` |
| `711` | `0x0871...e927` | `LONG` | 3,197,000.00 USD | `2,500.00` | `1276.50` | `1274.10` | `0.000000` | 5,750.00 USD | `+0.18%` | `10X Cross` |
| `727` | `0x9b86...6e6e` | `LONG` | 3,142,431.81 USD | `2,463.30` | `637.58` | `1274.10` | `882.54` | 1,571,882.53 USD | `+50.02%` | `3X Cross` |
| `781` | `0xb2f7...af9f` | `SHORT` | 2,951,612.60 USD | `2,313.72` | `746.63` | `1274.10` | `4420.58` | -1,224,123.86 USD | `-41.47%` | `10X Cross` |
| `799` | `0x413c...886c` | `LONG` | 2,870,100.00 USD | `2,250.00` | `1237.51` | `1274.10` | `0.000000` | 85,698.97 USD | `+2.99%` | `10X Cross` |
| `807` | `0xf48f...10fe` | `LONG` | 2,831,015.09 USD | `2,218.49` | `1517.87` | `1274.10` | `955.96` | -536,371.73 USD | `-18.95%` | `3X Cross` |
| `843` | `0x5bc4...3b0c` | `SHORT` | 2,721,168.05 USD | `2,130.74` | `1089.65` | `1274.10` | `3677.44` | -399,410.48 USD | `-14.68%` | `5X Cross` |
| `856` | `0x8de4...b9aa` | `SHORT` | 2,675,805.56 USD | `2,091.29` | `1331.35` | `1274.10` | `1689.99` | 108,434.15 USD | `+4.05%` | `3X Cross` |
| `864` | `0x4fe2...ac59` | `SHORT` | 2,639,594.49 USD | `2,071.57` | `1478.56` | `1274.10` | `1827.53` | 423,351.72 USD | `+16.04%` | `10X Cross` |
| `869` | `0xdf57...93f5` | `LONG` | 2,623,610.38 USD | `2,054.35` | `1227.36` | `1274.10` | `897.32` | 102,188.34 USD | `+3.89%` | `4X Isolated` |
| `877` | `0xbcd4...0dd2` | `LONG` | 2,594,671.74 USD | `2,033.92` | `1228.20` | `1274.10` | `787.19` | 96,620.93 USD | `+3.72%` | `10X Cross` |
| `883` | `0x9a99...d21a` | `LONG` | 2,559,000.00 USD | `2,000.00` | `1278.44` | `1274.10` | `0.000000` | 2,126.33 USD | `+0.08%` | `10X Cross` |
| `884` | `0xf29c...9971` | `LONG` | 2,554,200.00 USD | `2,000.00` | `1254.95` | `1274.10` | `0.000000` | 44,302.93 USD | `+1.73%` | `10X Cross` |
| `908` | `0x77ee...2902` | `SHORT` | 2,488,583.16 USD | `1,946.03` | `759.84` | `1274.10` | `5493.01` | -1,009,905.66 USD | `-40.58%` | `10X Cross` |
| `924` | `0x3e2f...b269` | `SHORT` | 2,459,068.82 USD | `1,925.51` | `1134.87` | `1274.10` | `2977.26` | -273,869.96 USD | `-11.14%` | `10X Cross` |
| `930` | `0x4f12...618b` | `SHORT` | 2,426,290.26 USD | `1,896.28` | `1608.30` | `1274.10` | `2116.88` | 623,494.13 USD | `+25.70%` | `3X Cross` |
| `976` | `0x866d...d6e1` | `LONG` | 2,303,740.72 USD | `1,802.05` | `674.73` | `1274.10` | `161.70` | 1,087,839.41 USD | `+47.22%` | `10X Cross` |
| `996` | `0x2309...a2d9` | `LONG` | 2,238,723.23 USD | `1,750.37` | `1186.09` | `1274.10` | `810.07` | 162,629.12 USD | `+7.26%` | `8X Cross` |
| `1027` | `0x3205...40bb` | `SHORT` | 2,128,456.05 USD | `1,665.98` | `1256.10` | `1274.10` | `2094.49` | -35,818.69 USD | `-1.68%` | `10X Cross` |
| `1033` | `0x265e...7f70` | `LONG` | 2,113,401.33 USD | `1,651.74` | `1382.98` | `1274.10` | `0.000000` | -170,921.43 USD | `-8.09%` | `3X Cross` |
| `1043` | `0xfe7c...b7ae` | `SHORT` | 2,094,037.47 USD | `1,642.64` | `1346.92` | `1274.10` | `5579.86` | 118,471.15 USD | `+5.66%` | `10X Cross` |
| `1049` | `0x3e47...aaf6` | `LONG` | 2,087,238.77 USD | `1,636.28` | `1278.38` | `1274.10` | `1046.10` | -4,553.02 USD | `-0.22%` | `10X Cross` |
| `1051` | `0x2edd...8179` | `SHORT` | 2,085,823.97 USD | `1,633.89` | `1261.58` | `1274.10` | `2888.32` | -24,542.05 USD | `-1.18%` | `10X Cross` |
| `1063` | `0x7f75...9edf` | `LONG` | 2,057,457.92 USD | `1,611.67` | `1200.24` | `1274.10` | `982.24` | 123,073.94 USD | `+5.98%` | `10X Cross` |
| `1071` | `0x6646...6de5` | `SHORT` | 2,044,160.00 USD | `1,600.00` | `660.64` | `1274.10` | `4331.10` | -987,135.03 USD | `-48.29%` | `10X Cross` |
| `1078` | `0x023a...2355` | `SHORT` | 2,033,178.52 USD | `1,594.90` | `1310.00` | `1274.10` | `4405.00` | 56,133.62 USD | `+2.76%` | `10X Cross` |
| `1100` | `0xab59...59b5` | `LONG` | 1,996,722.19 USD | `1,565.32` | `1342.15` | `1274.10` | `827.16` | -104,173.03 USD | `-5.22%` | `10X Cross` |
| `1132` | `0xfc27...9d9d` | `SHORT` | 1,963,931.38 USD | `1,540.58` | `1296.49` | `1274.10` | `12519.58` | 33,422.05 USD | `+1.70%` | `10X Cross` |
| `1163` | `0xcf67...eb24` | `LONG` | 1,911,150.00 USD | `1,500.00` | `887.05` | `1274.10` | `607.82` | 580,578.63 USD | `+30.38%` | `10X Cross` |
| `1172` | `0xb695...a92d` | `LONG` | 1,893,939.30 USD | `1,483.00` | `1249.80` | `1274.10` | `0.000000` | 40,480.44 USD | `+2.14%` | `10X Cross` |
| `1178` | `0x7277...0b98` | `SHORT` | 1,884,359.64 USD | `1,475.73` | `1287.86` | `1274.10` | `2152.56` | 16,172.49 USD | `+0.86%` | `10X Cross` |
| `1237` | `0x2ab7...c2f8` | `LONG` | 1,789,291.58 USD | `1,400.51` | `813.26` | `1274.10` | `789.56` | 650,309.89 USD | `+36.34%` | `3X Cross` |
| `1252` | `0xe35c...a1d3` | `LONG` | 1,773,401.66 USD | `1,389.16` | `1311.66` | `1274.10` | `690.78` | -48,701.06 USD | `-2.75%` | `2X Isolated` |
| `1260` | `0x11be...8b1d` | `LONG` | 1,755,008.75 USD | `1,375.83` | `1206.55` | `1274.10` | `1134.59` | 95,000.79 USD | `+5.41%` | `10X Isolated` |
| `1282` | `0x039c...0ebd` | `SHORT` | 1,705,686.30 USD | `1,336.64` | `1241.40` | `1274.10` | `3494.49` | -46,374.99 USD | `-2.72%` | `10X Cross` |
| `1342` | `0xe065...0f85` | `SHORT` | 1,615,509.50 USD | `1,262.61` | `1087.02` | `1274.10` | `1568.42` | -243,033.37 USD | `-15.04%` | `10X Cross` |
| `1423` | `0x266b...efcb` | `LONG` | 1,533,120.00 USD | `1,200.00` | `893.76` | `1274.10` | `377.75` | 460,610.30 USD | `+30.04%` | `10X Cross` |
| `1427` | `0x5975...9abd` | `LONG` | 1,530,720.00 USD | `1,200.00` | `1179.54` | `1274.10` | `447.42` | 115,277.21 USD | `+7.53%` | `5X Cross` |
| `1447` | `0x2847...d47b` | `LONG` | 1,513,799.15 USD | `1,186.27` | `1232.07` | `1274.10` | `0.000000` | 52,230.65 USD | `+3.45%` | `5X Cross` |
| `1468` | `0x69cc...14fd` | `SHORT` | 1,482,592.18 USD | `1,161.36` | `675.33` | `1274.10` | `7938.95` | -698,286.65 USD | `-47.10%` | `10X Cross` |
| `1488` | `0x3fc5...c0c1` | `SHORT` | 1,464,950.06 USD | `1,148.44` | `1264.34` | `1274.10` | `2665.77` | -12,936.29 USD | `-0.88%` | `10X Cross` |
| `1501` | `0x38f9...cb04` | `SHORT` | 1,450,006.91 USD | `1,136.28` | `1252.73` | `1274.10` | `1991.06` | -26,559.74 USD | `-1.83%` | `10X Cross` |
| `1520` | `0x5f94...4b96` | `LONG` | 1,422,749.94 USD | `1,115.27` | `538.00` | `1274.10` | `0.000000` | 822,732.30 USD | `+57.83%` | `10X Cross` |
| `1536` | `0x71df...a23d` | `SHORT` | 1,404,041.15 USD | `1,098.28` | `513.50` | `1274.10` | `2558.44` | -840,070.96 USD | `-59.83%` | `2X Cross` |
| `1567` | `0xbfc7...80b4` | `SHORT` | 1,374,817.50 USD | `1,075.00` | `558.03` | `1274.10` | `2586.45` | -774,938.77 USD | `-56.37%` | `10X Cross` |
| `1646` | `0x123d...3bff` | `SHORT` | 1,290,008.36 USD | `1,011.93` | `494.46` | `1274.10` | `4296.60` | -789,650.92 USD | `-61.21%` | `10X Cross` |
| `1657` | `0x668c...ea2e` | `SHORT` | 1,276,600.00 USD | `1,000.00` | `1406.98` | `1274.10` | `4197.97` | 130,381.99 USD | `+10.21%` | `10X Cross` |
| `1658` | `0xe282...df29` | `LONG` | 1,276,100.00 USD | `1,000.00` | `420.99` | `1274.10` | `790.28` | 855,113.14 USD | `+67.01%` | `10X Cross` |
| `1680` | `0x17f0...094f` | `LONG` | 1,258,329.12 USD | `984.30` | `1287.23` | `1274.10` | `536.94` | -8,691.04 USD | `-0.69%` | `5X Cross` |
| `1696` | `0x51f6...2b39` | `SHORT` | 1,242,375.65 USD | `972.81` | `1299.77` | `1274.10` | `2523.42` | 22,052.05 USD | `+1.77%` | `10X Cross` |
| `1724` | `0xdf83...3cff` | `SHORT` | 1,218,676.21 USD | `955.30` | `1259.52` | `1274.10` | `1919.28` | -15,452.62 USD | `-1.27%` | `10X Cross` |
| `1757` | `0x757d...94ba` | `LONG` | 1,181,317.50 USD | `925.00` | `1558.31` | `1274.10` | `0.000000` | -260,123.08 USD | `-22.02%` | `10X Cross` |
| `1758` | `0xaa82...9556` | `LONG` | 1,180,021.60 USD | `924.13` | `1254.72` | `1274.10` | `180.45` | 20,494.92 USD | `+1.74%` | `10X Cross` |
| `1811` | `0xb911...5525` | `LONG` | 1,148,040.00 USD | `900.00` | `1294.82` | `1274.10` | `1035.37` | -17,297.82 USD | `-1.51%` | `10X Cross` |
| `1847` | `0x2577...4897` | `SHORT` | 1,120,633.42 USD | `879.48` | `1271.98` | `1274.10` | `4931.47` | -1,949.80 USD | `-0.17%` | `10X Cross` |
| `1856` | `0xcf0a...856f` | `LONG` | 1,114,462.20 USD | `871.15` | `1292.19` | `1274.10` | `1006.08` | -11,232.65 USD | `-1.01%` | `4X Cross` |
| `1863` | `0x9e7e...0047` | `LONG` | 1,109,886.80 USD | `870.09` | `1284.68` | `1274.10` | `1175.12` | -7,898.61 USD | `-0.71%` | `10X Cross` |
| `1868` | `0xef96...9383` | `SHORT` | 1,106,540.76 USD | `868.42` | `1259.08` | `1274.10` | `5295.05` | -13,128.97 USD | `-1.19%` | `10X Cross` |
| `1883` | `0xdf95...7d72` | `SHORT` | 1,090,991.02 USD | `853.27` | `1074.39` | `1274.10` | `44010.70` | -174,243.58 USD | `-15.97%` | `10X Cross` |
| `1925` | `0x601c...4f54` | `SHORT` | 1,052,289.69 USD | `824.42` | `615.11` | `1274.10` | `3062.56` | -545,176.94 USD | `-51.81%` | `5X Cross` |
| `1942` | `0xae55...2236` | `LONG` | 1,043,990.94 USD | `817.47` | `1467.80` | `1274.10` | `0.000000` | -155,890.28 USD | `-14.93%` | `10X Cross` |
| `1980` | `0x11ee...1d1d` | `SHORT` | 1,023,440.00 USD | `800.00` | `1269.65` | `1274.10` | `1591.04` | -7,716.99 USD | `-0.75%` | `5X Cross` |
| `1982` | `0x0f02...5384` | `LONG` | 1,022,275.75 USD | `800.78` | `1290.36` | `1274.10` | `296.57` | -11,018.32 USD | `-1.08%` | `3X Cross` |
| `1984` | `0x9b0f...db40` | `LONG` | 1,022,080.00 USD | `800.00` | `1268.86` | `1274.10` | `791.96` | 6,990.24 USD | `+0.68%` | `10X Cross` |
| `1998` | `0xabdb...84ac` | `LONG` | 1,012,827.81 USD | `793.69` | `711.79` | `1274.10` | `664.51` | 447,887.45 USD | `+44.22%` | `3X Cross` |
| `1999` | `0x6e8f...4364` | `LONG` | 1,012,776.77 USD | `793.65` | `1260.00` | `1274.10` | `927.44` | 12,777.76 USD | `+1.26%` | `10X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
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
| `ANNOUNCEMENT` | `INFO` | `1615.00` | 500.65 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 0.50K USD at 1615.0000 USD [API] | `2026-09-26 21:18:11` |
| `ANNOUNCEMENT` | `INFO` | `1615.00` | 8,075.00 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 8.07K USD at 1615.0000 USD [API] | `2026-09-26 21:18:11` |
| `ANNOUNCEMENT` | `INFO` | `1615.00` | 403.75 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 0.40K USD at 1615.0000 USD [API] | `2026-09-26 21:18:11` |
| `ANNOUNCEMENT` | `INFO` | `1615.00` | 18,766.30 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 18.77K USD at 1615.0000 USD [API] | `2026-09-26 21:18:11` |
| `ANNOUNCEMENT` | `INFO` | `1615.00` | 40,375.00 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 40.38K USD at 1615.0000 USD [API] | `2026-09-26 21:18:11` |
| `ANNOUNCEMENT` | `INFO` | `1615.00` | 161.50 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 0.16K USD at 1615.0000 USD [API] | `2026-09-26 21:18:11` |
| `ANNOUNCEMENT` | `INFO` | `1614.90` | 3,100.61 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 3.10K USD at 1614.9000 USD [API] | `2026-09-26 21:18:11` |
| `ANNOUNCEMENT` | `INFO` | `1614.90` | 6,411.15 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 6.41K USD at 1614.9000 USD [API] | `2026-09-26 21:18:11` |
| `ANNOUNCEMENT` | `INFO` | `1614.90` | 209.94 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 0.21K USD at 1614.9000 USD [API] | `2026-09-26 21:18:11` |
| `ANNOUNCEMENT` | `INFO` | `1614.90` | 161.49 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 0.16K USD at 1614.9000 USD [API] | `2026-09-26 21:18:11` |
| `ANNOUNCEMENT` | `INFO` | `1614.80` | 500.59 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 0.50K USD at 1614.8000 USD [API] | `2026-09-26 21:18:11` |
| `ANNOUNCEMENT` | `INFO` | `1233.00` | 17,249.67 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 17.25K USD at 1233.0000 USD [API] | `2026-10-29 03:25:29` |
| `ANNOUNCEMENT` | `INFO` | `1233.10` | 2,638.83 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 2.64K USD at 1233.1000 USD [API] | `2026-10-29 03:25:29` |
| `ANNOUNCEMENT` | `INFO` | `1237.60` | 284.65 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 0.28K USD at 1237.6000 USD [API] | `2026-10-29 02:31:04` |
| `ANNOUNCEMENT` | `INFO` | `1237.60` | 185.64 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 0.19K USD at 1237.6000 USD [API] | `2026-10-29 02:31:04` |
| `ANNOUNCEMENT` | `INFO` | `1237.60` | 61.88 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 0.06K USD at 1237.6000 USD [API] | `2026-10-29 02:31:04` |


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
| `5m` | `BALANCED` | 0.00 USD | 1,750.00 USD | 1,750.00 USD | 1,750.00 USD | `1` | `2026-10-30 05:30:00 UTC - 2026-10-30 05:35:00 UTC` |
| `15m` | `BALANCED` | 0.00 USD | 1,750.00 USD | 1,750.00 USD | 1,750.00 USD | `1` | `2026-10-30 05:30:00 UTC - 2026-10-30 05:45:00 UTC` |
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
  * Current Rate: `81.72K` | Last 24h: `134.73K` | Last 3d: `246.48K` | Last 7d: `772.71K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0092%` | **USDT OKX** | `0.0100%` |
| **USDT Bybit** | `0.0100%` | **USDT KuCoin** | `0.0100%` |
| **USDT MEXC** | `0.0092%` | **USDT BingX** | `0.0100%` |
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
| `5:00 UTC` | `1265.55` | `1265.89` | `1265.55` | `1274.25` | `1259.25` | 13,172,642.30 USD | 7,854,309.17 USD | 5,318,333.13 USD | 2,535,976.04 USD | `+19.25%` | `13B / 1S` |
| `0:00 UTC` | `1282.05` | `1279.57` | `1282.05` | `1285.35` | `1269.15` | 31,465,166.07 USD | 16,761,441.58 USD | 14,703,724.48 USD | 2,057,717.10 USD | `+6.54%` | `8B / 5S` |
| `5:00 UTC` | `1279.95` | `1280.45` | `1279.95` | `1287.45` | `1275.15` | 19,925,691.14 USD | 8,662,599.23 USD | 11,263,091.92 USD | -2,600,492.69 USD | `-13.05%` | `1B / 6S` |
| `0:00 UTC` | `1275.15` | `1271.95` | `1275.15` | `1279.35` | `1264.95` | 23,738,198.29 USD | 11,363,344.84 USD | 12,374,853.45 USD | -1,011,508.62 USD | `-4.26%` | `3B / 3S` |
| `5:00 UTC` | `1279.05` | `1280.95` | `1279.05` | `1287.45` | `1274.25` | 14,930,858.33 USD | 7,292,403.22 USD | 7,638,455.11 USD | -346,051.88 USD | `-2.32%` | `2B / 4S` |
| `0:00 UTC` | `1285.05` | `1286.06` | `1285.05` | `1289.85` | `1282.05` | 15,953,463.93 USD | 6,542,642.51 USD | 9,410,821.42 USD | -2,868,178.91 USD | `-17.98%` | `1B / 3S` |
| `5:00 UTC` | `1276.95` | `1279.23` | `1276.95` | `1286.25` | `1275.15` | 15,449,899.62 USD | 6,063,485.10 USD | 9,386,414.52 USD | -3,322,929.42 USD | `-21.51%` | `0B / 8S` |
| `0:00 UTC` | `1275.15` | `1278.02` | `1275.15` | `1285.05` | `1272.15` | 16,039,119.46 USD | 6,719,465.52 USD | 9,319,653.95 USD | -2,600,188.43 USD | `-16.21%` | `2B / 3S` |
| `5:00 UTC` | `1272.15` | `1274.44` | `1272.15` | `1278.75` | `1270.65` | 10,354,318.48 USD | 4,552,930.99 USD | 5,801,387.50 USD | -1,248,456.51 USD | `-12.06%` | `0B / 2S` |
| `0:00 UTC` | `1272.15` | `1271.94` | `1272.15` | `1272.45` | `1270.95` | 145,629.27 USD | 24,286.15 USD | 121,343.12 USD | -97,056.97 USD | `-66.65%` | `0B / 4S` |

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
| `5m` | 129,850.00 USD | 98,250.00 USD | **`ACCUMULATION`** |
| `15m` | -89,210.00 USD | -614,320.00 USD | **`DISTRIBUTION`** |
| `30m` | -364,560.00 USD | -1,560,000.00 USD | **`DISTRIBUTION`** |
| `1h` | -2,380,000.00 USD | -12,030,000.00 USD | **`DISTRIBUTION`** |
| `2h` | -1,640,000.00 USD | -13,970,000.00 USD | **`DISTRIBUTION`** |
| `4h` | 7,060,000.00 USD | 13,140,000.00 USD | **`ACCUMULATION`** |
| `6h` | -1,160,000.00 USD | 8,770,000.00 USD | **`ACCUMULATION`** |
| `8h` | 195,000.00 USD | -58,400.00 USD | **`ACCUMULATION`** |
| `12h` | -13,280,000.00 USD | -28,130,000.00 USD | **`DISTRIBUTION`** |
| `24h` | 15,470,000.00 USD | 101,590,000.00 USD | **`ACCUMULATION`** |
| `1w` | 34,910,000.00 USD | 229,980,000.00 USD | **`ACCUMULATION`** |
| `30d` | 60,650,000.00 USD | -529,430,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+129.85K` | 15m=`-89.21K` | 1h=`-2.38M` | 24h=`+15.47M`
* Futures Capital Netflows: 5m=`+98.25K` | 15m=`-614.32K` | 1h=`-12.03M` | 24h=`+101.59M`
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
  * `2026-10-30 10:58:46 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 10:58:46 IST`: [forex.com] - (Sentiment: `Neutral`)
  * `2026-10-30 10:57:46 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 10:57:46 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 10:57:46 IST`: [financemagnates.com] - (Sentiment: `Neutral`)
  * `2026-10-30 07:59:46 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-30 06:59:46 IST`: [kathleenhays.substack.com] - (Sentiment: `Neutral`)
  * `2026-10-30 06:59:46 IST`: [rba.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 06:59:46 IST`: [abs.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 05:59:46 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 05:59:46 IST`: [@NodeWire] - (Sentiment: `Neutral`)
  * `2026-10-30 05:59:46 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 05:59:46 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 05:59:46 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-30 05:59:46 IST`: [media.rabobank.com] - (Sentiment: `Neutral`)


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
  * Execution Entry: `1233.76` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `1211.84` (Risk Distance: `21.92` pts)
  * +2.5R Take Profit: `1288.57`
  * Mathematical Lot Sizing: **`0.45 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `1285.56` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `1307.48` (Risk Distance: `21.92` pts)
  * +2.5R Take Profit: `1230.75`
  * Mathematical Lot Sizing: **`0.45 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`1283.20`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
