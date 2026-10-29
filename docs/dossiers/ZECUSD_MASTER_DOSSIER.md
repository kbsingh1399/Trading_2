# 🏛️ SOVEREIGN CANDIDATE DOSSIER: ZECUSD
**Canonical Key**: `ZECUSD` | **Broker Instrument**: `ZECUSD.p` | **Asset Class**: `Crypto Altcoin`
**Timestamp**: `2026-10-30 04:47:08 IST` (`2026-10-29 23:17:08 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `1238.53` | **Live Ask Quote**: `1240.19` | **Mid Price**: `1239.36`
- **Spread Points**: `166.00` | **Spread BPS**: `13.39 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `1278.94` | VWAP Z-Score: `-1.02` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `21.73` (Volatility Regime: `HIGH_EXPANSION`)
  * 14-Period RSI: `32.96` (State: `OVERSOLD`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `1391.26` | Lower -3.00σ Band: `1166.63`
  * Upper +2.51σ Band: `1372.91` | Lower -2.51σ Band: `1184.97`
  * Upper +2.01σ Band: `1354.19` | Lower -2.01σ Band: `1203.69`
  * Upper +2.00σ Band: `1353.82` | Lower -2.00σ Band: `1204.07`
  * Upper +1.28σ Band: `1326.86` | Lower -1.28σ Band: `1231.02`
  * Upper +1.00σ Band: `1316.38` | Lower -1.00σ Band: `1241.50`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`1256.09` | EMA-20=`1274.50` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`1285.63` (Slope: `+0.0000`) | EMA-100=`1284.40`
  * Institutional Anchors: EMA-144=`1281.95` | EMA-200=`1279.20` (Slope: `-0.2219`) | EMA-233=`1279.28`
- **Range Boundaries**: 24H High=`1396.49` | 24H Low=`1206.89` | Weekly High=`1396.49` | Weekly Low=`1206.89`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `1272.04` (Distance: `-2.38%`)
  * Point of Control (POC) = `1252.78` (Distance: `-0.88%`)
  * Value Area Low (VAL) = `1240.92` (Distance: `+0.06%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`1309.91` | POC=`1246.71` | VAL=`1230.27`
  * Prior Day Extremes: PDH=`1396.49` | PDL=`1206.89` | PDC=`1244.38`
  * Monday Range Blueprint: High=`1267.53` | Mid=`1222.14` | Low=`1176.75`
  * Developing Weekly Value Area: Weekly VAH=`1297.61` | Weekly POC=`1239.01` | Weekly VAL=`1199.46`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`1296.00` | Low=`1221.90`
  * London Session (08:00-16:00 UTC): High=`1244.32` | Low=`1234.40`
  * New York Session (13:00-21:00 UTC): High=`1246.80` | Low=`1231.92`
  * Initial Balance (First Hour): IB High=`1243.08` | IB Low=`1235.64`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `1234.40` - `1244.32`
  * Optimal Trade Entry (OTE 0.705): `1241.84`
  * Structural Invalidation Anchor (0.786): `1249.27`

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
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 04:46:31 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `16` | `0xb83d...6e36` | `SHORT` | 64,151,246.56 USD | `52,385.47` | `1336.45` | `1227.50` | `4052.84` | 5,859,320.84 USD | `+9.13%` | `3X Cross` |
| `24` | `0x5b5d...c060` | `SHORT` | 49,293,127.47 USD | `40,121.38` | `1478.36` | `1227.50` | `5551.06` | 10,020,907.64 USD | `+20.33%` | `3X Cross` |
| `43` | `0x7fda...17d1` | `SHORT` | 28,341,564.99 USD | `23,085.09` | `1262.37` | `1227.50` | `2810.92` | 800,278.68 USD | `+2.82%` | `5X Cross` |
| `88` | `0x60b0...991e` | `LONG` | 20,805,199.63 USD | `16,779.74` | `1179.65` | `1227.50` | `930.94` | 1,010,952.61 USD | `+4.86%` | `10X Cross` |
| `143` | `0xc36a...105b` | `LONG` | 14,291,834.11 USD | `11,510.82` | `1215.14` | `1227.50` | `960.50` | 304,553.08 USD | `+2.13%` | `10X Cross` |
| `161` | `0x9071...5c0b` | `LONG` | 12,885,783.71 USD | `10,517.29` | `1353.83` | `1227.50` | `0.0327` | -1,352,835.16 USD | `-10.50%` | `1X Cross` |
| `184` | `0x8742...8427` | `LONG` | 11,273,322.49 USD | `9,201.21` | `1286.37` | `1227.50` | `710.92` | -562,847.50 USD | `-4.99%` | `10X Cross` |
| `203` | `0x9ffd...ce40` | `LONG` | 10,571,626.48 USD | `8,610.92` | `1255.81` | `1227.50` | `623.24` | -242,023.68 USD | `-2.29%` | `5X Cross` |
| `209` | `0xad59...ba81` | `SHORT` | 10,317,255.00 USD | `8,425.00` | `330.91` | `1227.50` | `2146.74` | -7,529,297.23 USD | `-72.98%` | `10X Cross` |
| `217` | `0xdd53...2b13` | `SHORT` | 10,006,861.82 USD | `8,168.20` | `739.52` | `1227.50` | `8770.96` | -3,966,351.63 USD | `-39.64%` | `3X Cross` |
| `238` | `0x880a...311c` | `SHORT` | 9,490,535.25 USD | `7,707.11` | `1367.50` | `1227.50` | `2272.99` | 1,048,948.95 USD | `+11.05%` | `10X Cross` |
| `278` | `0x2b61...2f6c` | `LONG` | 8,482,202.70 USD | `6,807.00` | `1453.56` | `1227.50` | `534.04` | -1,412,148.52 USD | `-16.65%` | `10X Cross` |
| `301` | `0x2ae5...83e7` | `LONG` | 7,899,240.96 USD | `6,436.80` | `1391.82` | `1227.50` | `0.000000` | -1,059,651.03 USD | `-13.41%` | `1X Cross` |
| `346` | `0x26b6...9a13` | `LONG` | 6,654,689.13 USD | `5,433.73` | `1282.23` | `1227.50` | `223.28` | -312,614.10 USD | `-4.70%` | `10X Cross` |
| `359` | `0x45d2...4029` | `SHORT` | 6,461,617.40 USD | `5,227.00` | `833.44` | `1227.50` | `9094.24` | -2,105,239.43 USD | `-32.58%` | `5X Cross` |
| `384` | `0xea00...a918` | `LONG` | 6,120,500.00 USD | `5,000.00` | `739.16` | `1227.50` | `0.000000` | 2,424,684.89 USD | `+39.62%` | `5X Cross` |
| `385` | `0x58b2...11f3` | `LONG` | 6,097,640.09 USD | `4,963.08` | `1257.17` | `1227.50` | `0.000000` | -141,771.10 USD | `-2.33%` | `10X Cross` |
| `388` | `0xdd7a...8830` | `LONG` | 5,989,698.16 USD | `4,860.19` | `897.48` | `1227.50` | `788.75` | 1,627,794.48 USD | `+27.18%` | `10X Cross` |
| `427` | `0xecb6...2b00` | `SHORT` | 5,137,685.76 USD | `4,181.74` | `1303.95` | `1227.50` | `7951.69` | 315,077.04 USD | `+6.13%` | `5X Cross` |
| `439` | `0x4cae...7c34` | `LONG` | 4,919,756.70 USD | `4,004.36` | `999.34` | `1227.50` | `1006.57` | 918,028.54 USD | `+18.66%` | `10X Cross` |
| `452` | `0xa61c...66b9` | `LONG` | 4,814,121.60 USD | `3,888.00` | `1148.34` | `1227.50` | `0.000000` | 349,379.46 USD | `+7.26%` | `10X Cross` |
| `478` | `0x9aa5...58af` | `SHORT` | 4,567,424.59 USD | `3,720.31` | `1205.51` | `1227.50` | `3690.46` | -82,537.79 USD | `-1.81%` | `10X Cross` |
| `485` | `0x0153...8052` | `SHORT` | 4,535,447.95 USD | `3,698.18` | `1307.82` | `1227.50` | `2504.75` | 301,122.80 USD | `+6.64%` | `1X Isolated` |
| `553` | `0xd21d...90f1` | `LONG` | 3,978,325.00 USD | `3,250.00` | `1253.64` | `1227.50` | `875.95` | -96,016.73 USD | `-2.41%` | `4X Isolated` |
| `577` | `0x1338...c48e` | `LONG` | 3,869,389.70 USD | `3,149.43` | `1018.52` | `1227.50` | `820.24` | 661,644.16 USD | `+17.10%` | `4X Isolated` |
| `580` | `0x456f...cdf1` | `LONG` | 3,853,153.19 USD | `3,134.11` | `1268.47` | `1227.50` | `493.84` | -122,356.28 USD | `-3.18%` | `10X Cross` |
| `589` | `0xdbe0...d6d5` | `LONG` | 3,815,985.62 USD | `3,085.37` | `422.97` | `1227.50` | `338.56` | 2,510,981.12 USD | `+65.80%` | `3X Isolated` |
| `591` | `0x382b...3e39` | `LONG` | 3,785,978.25 USD | `3,084.30` | `1211.32` | `1227.50` | `0.000000` | 49,894.91 USD | `+1.32%` | `10X Cross` |
| `595` | `0xd4c1...3d1d` | `SHORT` | 3,742,180.45 USD | `3,045.89` | `1299.23` | `1227.50` | `2914.94` | 215,127.16 USD | `+5.75%` | `10X Cross` |
| `599` | `0x27c9...d65d` | `SHORT` | 3,732,585.09 USD | `3,038.08` | `1254.41` | `1227.50` | `1779.01` | 78,416.24 USD | `+2.10%` | `10X Cross` |
| `613` | `0x325e...9564` | `LONG` | 3,677,039.56 USD | `3,001.91` | `1301.41` | `1227.50` | `187.69` | -229,669.65 USD | `-6.25%` | `10X Cross` |
| `614` | `0x9c06...0560` | `SHORT` | 3,673,268.28 USD | `2,989.80` | `786.00` | `1227.50` | `2554.92` | -1,323,273.28 USD | `-36.02%` | `10X Cross` |
| `628` | `0x2e30...4cb5` | `SHORT` | 3,608,872.48 USD | `2,946.74` | `1297.52` | `1227.50` | `2889.14` | 214,581.71 USD | `+5.95%` | `2X Cross` |
| `727` | `0xa183...0482` | `LONG` | 3,104,656.80 USD | `2,534.00` | `530.25` | `1227.50` | `444.48` | 1,760,994.08 USD | `+56.72%` | `5X Isolated` |
| `729` | `0xac48...3201` | `LONG` | 3,104,125.30 USD | `2,531.50` | `1378.58` | `1227.50` | `545.11` | -385,746.98 USD | `-12.43%` | `10X Cross` |
| `739` | `0x0871...e927` | `LONG` | 3,071,500.00 USD | `2,500.00` | `1276.50` | `1227.50` | `0.000000` | -119,750.00 USD | `-3.90%` | `10X Cross` |
| `748` | `0x9b86...6e6e` | `LONG` | 3,033,307.62 USD | `2,463.30` | `637.58` | `1227.50` | `882.41` | 1,462,758.34 USD | `+48.22%` | `3X Cross` |
| `801` | `0xb2f7...af9f` | `SHORT` | 2,849,114.81 USD | `2,313.72` | `746.63` | `1227.50` | `4400.82` | -1,121,626.06 USD | `-39.37%` | `10X Cross` |
| `829` | `0xf48f...10fe` | `LONG` | 2,731,848.59 USD | `2,218.49` | `1517.87` | `1227.50` | `997.05` | -635,538.24 USD | `-23.26%` | `3X Cross` |
| `861` | `0x5bc4...3b0c` | `SHORT` | 2,610,156.50 USD | `2,130.74` | `1089.65` | `1227.50` | `3694.21` | -288,398.92 USD | `-11.05%` | `5X Cross` |
| `863` | `0x8de4...b9aa` | `SHORT` | 2,602,094.27 USD | `2,091.29` | `1331.35` | `1227.50` | `1689.86` | 182,145.43 USD | `+7.00%` | `3X Cross` |
| `874` | `0x4fe2...ac59` | `SHORT` | 2,577,557.60 USD | `2,071.57` | `1478.56` | `1227.50` | `1846.96` | 485,388.61 USD | `+18.83%` | `10X Cross` |
| `923` | `0x9a99...d21a` | `LONG` | 2,449,600.00 USD | `2,000.00` | `1278.44` | `1227.50` | `0.000000` | -107,273.67 USD | `-4.38%` | `10X Cross` |
| `947` | `0x77ee...2902` | `SHORT` | 2,390,892.46 USD | `1,946.03` | `759.84` | `1227.50` | `5290.32` | -912,214.95 USD | `-38.15%` | `10X Cross` |
| `964` | `0x3e2f...b269` | `SHORT` | 2,358,749.75 USD | `1,925.51` | `1134.87` | `1227.50` | `2931.80` | -173,550.89 USD | `-7.36%` | `10X Cross` |
| `968` | `0xe097...d0fe` | `LONG` | 2,349,277.61 USD | `1,913.56` | `1261.17` | `1227.50` | `0.000000` | -64,048.55 USD | `-2.73%` | `10X Cross` |
| `969` | `0x5323...b23c` | `LONG` | 2,341,996.55 USD | `1,911.99` | `1235.11` | `1227.50` | `0.000000` | -19,520.43 USD | `-0.83%` | `5X Cross` |
| `979` | `0x4f12...618b` | `SHORT` | 2,321,236.35 USD | `1,896.28` | `1608.30` | `1227.50` | `2116.76` | 728,548.04 USD | `+31.39%` | `3X Cross` |
| `1011` | `0x866d...d6e1` | `LONG` | 2,213,998.63 USD | `1,802.05` | `674.73` | `1227.50` | `254.14` | 998,097.32 USD | `+45.08%` | `10X Cross` |
| `1029` | `0x2309...a2d9` | `LONG` | 2,173,165.05 USD | `1,750.37` | `1186.09` | `1227.50` | `816.28` | 97,070.94 USD | `+4.47%` | `8X Cross` |
| `1062` | `0x2edd...8179` | `SHORT` | 2,084,596.06 USD | `1,701.85` | `1261.58` | `1227.50` | `3135.96` | 62,422.79 USD | `+2.99%` | `10X Cross` |
| `1067` | `0x023a...2355` | `SHORT` | 2,077,895.86 USD | `1,696.38` | `1313.00` | `1227.50` | `5284.30` | 149,451.43 USD | `+7.19%` | `10X Cross` |
| `1094` | `0xfe7c...b7ae` | `SHORT` | 2,015,628.02 USD | `1,640.99` | `1347.05` | `1227.50` | `7073.03` | 194,861.17 USD | `+9.67%` | `10X Cross` |
| `1099` | `0x3e47...aaf6` | `LONG` | 2,011,969.89 USD | `1,636.28` | `1278.38` | `1227.50` | `1052.95` | -79,821.90 USD | `-3.97%` | `10X Cross` |
| `1114` | `0xa271...a3f7` | `LONG` | 1,998,175.46 USD | `1,631.43` | `1190.60` | `1227.50` | `910.34` | 55,793.66 USD | `+2.79%` | `4X Cross` |
| `1118` | `0x265e...7f70` | `LONG` | 1,992,970.12 USD | `1,601.74` | `1388.09` | `1227.50` | `0.000000` | -230,394.89 USD | `-11.56%` | `3X Cross` |
| `1127` | `0x6646...6de5` | `SHORT` | 1,978,880.00 USD | `1,600.00` | `660.64` | `1227.50` | `4431.38` | -921,855.03 USD | `-46.58%` | `10X Cross` |
| `1130` | `0x7f75...9edf` | `LONG` | 1,972,861.31 USD | `1,605.78` | `1199.97` | `1227.50` | `978.70` | 45,969.42 USD | `+2.33%` | `10X Cross` |
| `1157` | `0xdf57...93f5` | `LONG` | 1,934,574.10 USD | `1,579.76` | `1218.38` | `1227.50` | `780.18` | 9,818.12 USD | `+0.51%` | `3X Isolated` |
| `1166` | `0xab59...59b5` | `LONG` | 1,924,717.47 USD | `1,565.32` | `1342.15` | `1227.50` | `837.68` | -176,177.75 USD | `-9.15%` | `10X Cross` |
| `1202` | `0xcf67...eb24` | `LONG` | 1,866,379.80 USD | `1,500.00` | `887.05` | `1227.50` | `675.75` | 535,808.43 USD | `+28.71%` | `10X Cross` |
| `1239` | `0xb695...a92d` | `LONG` | 1,816,971.60 USD | `1,483.00` | `1249.80` | `1227.50` | `0.000000` | -36,487.25 USD | `-2.01%` | `10X Cross` |
| `1293` | `0x2ab7...c2f8` | `LONG` | 1,718,705.87 USD | `1,400.51` | `813.26` | `1227.50` | `793.29` | 579,724.19 USD | `+33.73%` | `3X Cross` |
| `1307` | `0x11be...8b1d` | `LONG` | 1,684,153.50 USD | `1,375.83` | `1206.55` | `1227.50` | `1134.46` | 24,145.55 USD | `+1.43%` | `10X Isolated` |
| `1402` | `0xe065...0f85` | `SHORT` | 1,571,006.53 USD | `1,262.61` | `1087.02` | `1227.50` | `1830.49` | -198,530.41 USD | `-12.64%` | `10X Cross` |
| `1438` | `0x039c...0ebd` | `SHORT` | 1,535,300.24 USD | `1,250.55` | `1239.86` | `1227.50` | `3653.08` | 15,211.05 USD | `+0.99%` | `10X Cross` |
| `1452` | `0x7277...0b98` | `SHORT` | 1,512,332.02 USD | `1,234.96` | `1298.48` | `1227.50` | `2430.95` | 91,237.40 USD | `+6.03%` | `10X Cross` |
| `1481` | `0x5975...9abd` | `LONG` | 1,475,310.00 USD | `1,200.00` | `1179.54` | `1227.50` | `597.76` | 59,867.21 USD | `+4.06%` | `5X Cross` |
| `1485` | `0x266b...efcb` | `LONG` | 1,472,280.00 USD | `1,200.00` | `893.76` | `1227.50` | `421.41` | 399,770.30 USD | `+27.15%` | `10X Cross` |
| `1527` | `0x69cc...14fd` | `SHORT` | 1,422,201.46 USD | `1,161.36` | `675.33` | `1227.50` | `8174.28` | -637,895.93 USD | `-44.85%` | `10X Cross` |
| `1547` | `0x3fc5...c0c1` | `SHORT` | 1,411,920.85 USD | `1,148.44` | `1264.34` | `1227.50` | `3152.88` | 40,092.93 USD | `+2.84%` | `10X Cross` |
| `1562` | `0x2847...d47b` | `LONG` | 1,395,835.82 USD | `1,139.83` | `1233.90` | `1227.50` | `0.000000` | -10,599.88 USD | `-0.76%` | `5X Cross` |
| `1563` | `0xe35c...a1d3` | `LONG` | 1,395,525.69 USD | `1,127.06` | `1318.20` | `1227.50` | `694.38` | -90,169.66 USD | `-6.46%` | `2X Isolated` |
| `1585` | `0x51f6...2b39` | `SHORT` | 1,369,769.44 USD | `1,115.72` | `1299.77` | `1227.50` | `2655.59` | 80,408.16 USD | `+5.87%` | `10X Cross` |
| `1589` | `0x5f94...4b96` | `LONG` | 1,365,759.64 USD | `1,115.27` | `538.00` | `1227.50` | `0.000000` | 765,742.01 USD | `+56.07%` | `10X Cross` |
| `1605` | `0x71df...a23d` | `SHORT` | 1,349,346.81 USD | `1,098.28` | `513.50` | `1227.50` | `2553.35` | -785,376.62 USD | `-58.20%` | `2X Cross` |
| `1606` | `0xfc27...9d9d` | `SHORT` | 1,348,494.68 USD | `1,098.57` | `1315.05` | `1227.50` | `16922.61` | 96,183.05 USD | `+7.13%` | `10X Cross` |
| `1627` | `0xef96...9383` | `SHORT` | 1,321,686.88 USD | `1,078.84` | `1259.08` | `1227.50` | `5178.01` | 36,660.89 USD | `+2.77%` | `10X Cross` |
| `1629` | `0xbfc7...80b4` | `SHORT` | 1,319,562.50 USD | `1,075.00` | `558.03` | `1227.50` | `4726.54` | -719,683.77 USD | `-54.54%` | `10X Cross` |
| `1679` | `0x71d0...8c26` | `SHORT` | 1,256,518.10 USD | `1,023.64` | `1289.25` | `1227.50` | `6303.18` | 63,212.82 USD | `+5.03%` | `10X Cross` |
| `1693` | `0xdf83...3cff` | `SHORT` | 1,247,793.92 USD | `1,018.94` | `1255.41` | `1227.50` | `1762.84` | 31,398.61 USD | `+2.52%` | `10X Cross` |
| `1699` | `0x668c...ea2e` | `SHORT` | 1,241,546.10 USD | `1,000.00` | `1406.98` | `1227.50` | `4181.31` | 165,435.89 USD | `+13.32%` | `10X Cross` |
| `1705` | `0xe282...df29` | `LONG` | 1,238,200.00 USD | `1,000.00` | `420.99` | `1227.50` | `212.78` | 817,213.14 USD | `+66.00%` | `10X Cross` |
| `1709` | `0x123d...3bff` | `SHORT` | 1,234,950.74 USD | `1,008.37` | `490.16` | `1227.50` | `4584.75` | -740,690.52 USD | `-59.98%` | `10X Cross` |
| `1737` | `0x17f0...094f` | `LONG` | 1,209,310.98 USD | `984.30` | `1287.23` | `1227.50` | `536.81` | -57,709.18 USD | `-4.77%` | `5X Cross` |
| `1822` | `0x757d...94ba` | `LONG` | 1,133,125.00 USD | `925.00` | `1558.31` | `1227.50` | `0.000000` | -308,315.59 USD | `-27.21%` | `10X Cross` |
| `1855` | `0xb911...5525` | `LONG` | 1,106,482.50 USD | `900.00` | `1294.82` | `1227.50` | `1070.33` | -58,855.32 USD | `-5.32%` | `10X Cross` |
| `1885` | `0xcf0a...856f` | `LONG` | 1,084,146.18 USD | `871.15` | `1292.19` | `1227.50` | `1004.89` | -41,548.67 USD | `-3.83%` | `4X Cross` |
| `1925` | `0xdf95...7d72` | `SHORT` | 1,049,678.14 USD | `857.16` | `1074.39` | `1227.50` | `46504.05` | -128,751.31 USD | `-12.27%` | `10X Cross` |
| `1949` | `0x601c...4f54` | `SHORT` | 1,027,639.53 USD | `824.42` | `615.11` | `1227.50` | `3118.68` | -520,526.78 USD | `-50.65%` | `5X Cross` |
| `2001` | `0xae55...2236` | `LONG` | 1,001,155.51 USD | `817.47` | `1467.80` | `1227.50` | `0.000000` | -198,725.71 USD | `-19.85%` | `10X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `1121.60` | 594.45 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 0.59K USD at 1121.6000 USD [API] | `2026-10-24 14:16:53` |
| `ANNOUNCEMENT` | `INFO` | `1121.60` | 179.46 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 0.18K USD at 1121.6000 USD [API] | `2026-10-24 14:16:53` |
| `ANNOUNCEMENT` | `INFO` | `1122.30` | 2,020.14 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 2.02K USD at 1122.3000 USD [API] | `2026-10-24 14:16:53` |
| `ANNOUNCEMENT` | `INFO` | `1131.50` | 2,036.70 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 2.04K USD at 1131.5000 USD [API] | `2026-10-24 14:16:43` |
| `ANNOUNCEMENT` | `INFO` | `1132.20` | 2,037.96 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 2.04K USD at 1132.2000 USD [API] | `2026-10-24 14:16:43` |
| `ANNOUNCEMENT` | `INFO` | `1133.60` | 2,040.48 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 2.04K USD at 1133.6000 USD [API] | `2026-10-24 14:16:30` |
| `ANNOUNCEMENT` | `INFO` | `1135.80` | 545.18 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 0.55K USD at 1135.8000 USD [API] | `2026-10-24 14:16:14` |
| `ANNOUNCEMENT` | `INFO` | `1297.50` | 1,699.73 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Long: 1.70K USD at 1297.5000 USD [API] | `2026-10-28 19:57:32` |
| `ANNOUNCEMENT` | `INFO` | `1297.70` | 7,708.34 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Long: 7.71K USD at 1297.7000 USD [API] | `2026-10-28 19:57:32` |
| `ANNOUNCEMENT` | `INFO` | `1297.60` | 2,141.04 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Long: 2.14K USD at 1297.6000 USD [API] | `2026-10-28 19:57:32` |
| `ANNOUNCEMENT` | `INFO` | `1297.60` | 2,141.04 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Long: 2.14K USD at 1297.6000 USD [API] | `2026-10-28 19:57:32` |
| `ANNOUNCEMENT` | `INFO` | `1297.60` | 2,141.04 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Long: 2.14K USD at 1297.6000 USD [API] | `2026-10-28 19:57:32` |
| `ANNOUNCEMENT` | `INFO` | `1297.60` | 13,650.75 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Long: 13.65K USD at 1297.6000 USD [API] | `2026-10-28 19:57:32` |
| `ANNOUNCEMENT` | `INFO` | `1297.50` | 2,140.88 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Long: 2.14K USD at 1297.5000 USD [API] | `2026-10-28 19:57:32` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`1403.54` (Vol: 3,000,000.00 USD, Dist: `+12.15%`) | Long MP=`1223.03` (Vol: 1,200,000.00 USD, Dist: `--2.28%`)
  * 48H Horizon: Short MP=`1403.54` (Vol: 3,000,000.00 USD, Dist: `+12.15%`) | Long MP=`1223.03` (Vol: 1,200,000.00 USD, Dist: `--2.28%`)
  * 3D Horizon: Short MP=`1403.54` (Vol: 3,000,000.00 USD, Dist: `+12.15%`) | Long MP=`1200.05` (Vol: 1,600,000.00 USD, Dist: `--4.11%`)
  * 7D Horizon: Short MP=`1404.10` (Vol: 3,000,000.00 USD, Dist: `+12.19%`) | Long MP=`1200.46` (Vol: 3,000,000.00 USD, Dist: `--4.08%`)
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
| `5m` | `BALANCED` | 0.00 USD | 1,750.00 USD | 1,750.00 USD | 1,750.00 USD | `1` | `2026-10-29 23:15:00 UTC - 2026-10-29 23:20:00 UTC` |
| `15m` | `BALANCED` | 0.00 USD | 1,750.00 USD | 1,750.00 USD | 1,750.00 USD | `1` | `2026-10-29 23:15:00 UTC - 2026-10-29 23:30:00 UTC` |
| `1h` | `BALANCED` | 0.00 USD | 1,750.00 USD | 1,750.00 USD | 1,750.00 USD | `1` | `2026-10-29 23:00:00 UTC - 2026-10-30 00:00:00 UTC` |
| `4h` | `BALANCED` | 0.00 USD | 1,750.00 USD | 1,750.00 USD | 1,750.00 USD | `1` | `2026-10-29 20:00:00 UTC - 2026-10-30 00:00:00 UTC` |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `0 USD` | Total OI Tokens: `-`
  * 1h OI Change: `0.00%` | 4h OI Change: `0.00%` | 24h OI Change: `0.00%`
  * Exchange Breakdown: Binance=`-` | Bybit=`-` | OKX=`-` | Hyperliquid=`-`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `16.05K` | Last 24h: `33.19K` | Last 3d: `283.86K` | Last 7d: `777.60K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `-0.0006%` | **USDT OKX** | `0.0032%` |
| **USDT Bybit** | `0.0100%` | **USDT KuCoin** | `-0.0033%` |
| **USDT MEXC** | `-0.0006%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `0.0069%` | **USDT Bitget** | `0.0100%` |
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
| `5:00 UTC` | `1229.25` | `1237.79` | `1229.25` | `1264.35` | `1206.75` | 149,162,484.89 USD | 77,012,548.38 USD | 72,149,936.51 USD | 4,862,611.87 USD | `+3.26%` | `9B / 11S` |
| `0:00 UTC` | `1249.95` | `1248.07` | `1249.95` | `1259.85` | `1233.15` | 61,152,789.32 USD | 32,267,997.87 USD | 28,884,791.45 USD | 3,383,206.41 USD | `+5.53%` | `6B / 4S` |
| `5:00 UTC` | `1273.95` | `1271.85` | `1273.95` | `1286.25` | `1253.25` | 67,607,862.35 USD | 37,234,359.13 USD | 30,373,503.22 USD | 6,860,855.91 USD | `+10.15%` | `6B / 2S` |
| `0:00 UTC` | `1294.65` | `1287.25` | `1294.65` | `1297.05` | `1269.15` | 47,983,765.84 USD | 24,978,907.15 USD | 23,004,858.69 USD | 1,974,048.46 USD | `+4.11%` | `4B / 9S` |
| `5:00 UTC` | `1264.05` | `1267.99` | `1264.05` | `1276.65` | `1260.75` | 31,349,361.20 USD | 15,100,777.24 USD | 16,248,583.96 USD | -1,147,806.72 USD | `-3.66%` | `0B / 1S` |
| `0:00 UTC` | `1261.05` | `1255.07` | `1261.05` | `1269.15` | `1241.25` | 60,510,539.13 USD | 31,467,084.85 USD | 29,043,454.28 USD | 2,423,630.57 USD | `+4.01%` | `3B / 5S` |
| `5:00 UTC` | `1259.85` | `1254.56` | `1259.85` | `1263.15` | `1242.15` | 22,141,749.31 USD | 11,943,317.16 USD | 10,198,432.15 USD | 1,744,885.01 USD | `+7.88%` | `3B / 3S` |
| `0:00 UTC` | `1257.15` | `1255.20` | `1257.15` | `1264.35` | `1245.45` | 28,871,970.63 USD | 12,578,804.66 USD | 16,293,165.97 USD | -3,714,361.32 USD | `-12.86%` | `7B / 2S` |
| `5:00 UTC` | `1241.25` | `1245.94` | `1241.25` | `1254.45` | `1236.15` | 26,347,049.74 USD | 11,469,285.37 USD | 14,877,764.37 USD | -3,408,478.99 USD | `-12.94%` | `1B / 6S` |
| `0:00 UTC` | `1224.15` | `1230.51` | `1224.15` | `1243.65` | `1222.05` | 36,854,164.51 USD | 16,245,634.04 USD | 20,608,530.47 USD | -4,362,896.43 USD | `-11.84%` | `1B / 6S` |

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
| `5m` | 1,280,000.00 USD | -8,040,000.00 USD | **`DISTRIBUTION`** |
| `15m` | -536,460.00 USD | -11,780,000.00 USD | **`DISTRIBUTION`** |
| `30m` | -1,110,000.00 USD | -14,800,000.00 USD | **`DISTRIBUTION`** |
| `1h` | -1,440,000.00 USD | -9,730,000.00 USD | **`DISTRIBUTION`** |
| `2h` | 6,460,000.00 USD | 5,990,000.00 USD | **`ACCUMULATION`** |
| `4h` | -13,840,000.00 USD | -17,780,000.00 USD | **`DISTRIBUTION`** |
| `6h` | -13,440,000.00 USD | -32,070,000.00 USD | **`DISTRIBUTION`** |
| `8h` | 5,360,000.00 USD | 77,780,000.00 USD | **`ACCUMULATION`** |
| `12h` | 20,310,000.00 USD | 74,020,000.00 USD | **`ACCUMULATION`** |
| `24h` | 172,690.00 USD | 53,390,000.00 USD | **`ACCUMULATION`** |
| `1w` | 35,140,000.00 USD | 230,440,000.00 USD | **`ACCUMULATION`** |
| `30d` | 56,930,000.00 USD | -551,300,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+1.28M` | 15m=`-536.46K` | 1h=`-1.44M` | 24h=`+172.69K`
* Futures Capital Netflows: 5m=`-8.04M` | 15m=`-11.78M` | 1h=`-9.73M` | 24h=`+53.39M`
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
  * `2026-10-30 04:15:34 IST`: [economics.td.com] - (Sentiment: `Neutral`)
  * `2026-10-30 04:41:34 IST`: [investinglive.com] - (Sentiment: `Neutral`)
  * `2026-10-30 04:41:34 IST`: [msn.com] - (Sentiment: `Neutral`)
  * `2026-10-30 04:40:34 IST`: [morningstar.com] - (Sentiment: `Neutral`)
  * `2026-10-30 01:42:34 IST`: [sec.gov] - (Sentiment: `Neutral`)
  * `2026-10-30 01:42:34 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 01:42:34 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 00:42:34 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:42:34 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:42:34 IST`: [@DeItaone] - (Sentiment: `Neutral`)
  * `2026-10-29 23:42:34 IST`: [@mb_ghalibaf] - (Sentiment: `Neutral`)
  * `2026-10-29 23:42:34 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-29 23:42:34 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-29 23:42:34 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:42:34 IST`: [fxstreet.com] - (Sentiment: `Neutral`)


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
  * Execution Entry: `1240.92` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `1212.36` (Risk Distance: `28.56` pts)
  * +2.5R Take Profit: `1312.33`
  * Mathematical Lot Sizing: **`0.35 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `1272.04` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `1300.60` (Risk Distance: `28.56` pts)
  * +2.5R Take Profit: `1200.63`
  * Mathematical Lot Sizing: **`0.35 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`1249.27`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
