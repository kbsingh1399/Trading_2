# 🏛️ SOVEREIGN CANDIDATE DOSSIER: ZECUSD
**Canonical Key**: `ZECUSD` | **Broker Instrument**: `ZECUSD.p` | **Asset Class**: `Crypto Altcoin`
**Timestamp**: `2026-10-30 04:01:40 IST` (`2026-10-29 22:31:40 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `1258.35` | **Live Ask Quote**: `1260.19` | **Mid Price**: `1259.27`
- **Spread Points**: `184.00` | **Spread BPS**: `14.61 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `1280.70` | VWAP Z-Score: `-0.75` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `22.75` (Volatility Regime: `HIGH_EXPANSION`)
  * 14-Period RSI: `35.80` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `1393.56` | Lower -3.00σ Band: `1167.85`
  * Upper +2.51σ Band: `1375.12` | Lower -2.51σ Band: `1186.29`
  * Upper +2.01σ Band: `1356.31` | Lower -2.01σ Band: `1205.09`
  * Upper +2.00σ Band: `1355.94` | Lower -2.00σ Band: `1205.47`
  * Upper +1.28σ Band: `1328.85` | Lower -1.28σ Band: `1232.55`
  * Upper +1.00σ Band: `1318.32` | Lower -1.00σ Band: `1243.09`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`1270.79` | EMA-20=`1288.21` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`1292.33` (Slope: `+0.0000`) | EMA-100=`1287.53`
  * Institutional Anchors: EMA-144=`1283.94` | EMA-200=`1280.33` (Slope: `-0.0006`) | EMA-233=`1279.70`
- **Range Boundaries**: 24H High=`1396.49` | 24H Low=`1206.89` | Weekly High=`1396.49` | Weekly Low=`1206.89`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `1276.64` (Distance: `-1.23%`)
  * Point of Control (POC) = `1260.05` (Distance: `+0.07%`)
  * Value Area Low (VAL) = `1247.88` (Distance: `+1.05%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`1309.91` | POC=`1246.71` | VAL=`1230.27`
  * Prior Day Extremes: PDH=`1396.49` | PDL=`1206.89` | PDC=`1244.38`
  * Monday Range Blueprint: High=`1267.53` | Mid=`1222.14` | Low=`1176.75`
  * Developing Weekly Value Area: Weekly VAH=`1296.14` | Weekly POC=`1239.01` | Weekly VAL=`1196.53`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`1296.00` | Low=`1240.69`
  * London Session (08:00-16:00 UTC): High=`1264.31` | Low=`1254.23`
  * New York Session (13:00-21:00 UTC): High=`1266.83` | Low=`1251.71`
  * Initial Balance (First Hour): IB High=`1263.05` | IB Low=`1255.49`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `1254.23` - `1264.31`
  * Optimal Trade Entry (OTE 0.705): `1261.79`
  * Structural Invalidation Anchor (0.786): `1269.34`

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
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 03:55:39 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `16` | `0xb83d...6e36` | `SHORT` | 66,105,224.59 USD | `52,385.47` | `1336.45` | `1261.30` | `3963.79` | 3,905,342.81 USD | `+5.91%` | `3X Cross` |
| `23` | `0x5b5d...c060` | `SHORT` | 50,601,084.46 USD | `40,121.38` | `1478.36` | `1261.30` | `5423.92` | 8,712,950.66 USD | `+17.22%` | `3X Cross` |
| `44` | `0x7fda...17d1` | `SHORT` | 29,413,845.13 USD | `23,322.11` | `1262.38` | `1261.30` | `2723.34` | 27,526.22 USD | `+0.09%` | `5X Cross` |
| `83` | `0x60b0...991e` | `LONG` | 21,137,438.48 USD | `16,779.74` | `1179.65` | `1261.30` | `927.44` | 1,343,191.46 USD | `+6.35%` | `10X Cross` |
| `141` | `0xc36a...105b` | `LONG` | 14,510,539.69 USD | `11,510.82` | `1215.14` | `1261.30` | `958.92` | 523,258.66 USD | `+3.61%` | `10X Cross` |
| `159` | `0x9071...5c0b` | `LONG` | 13,281,118.12 USD | `10,517.29` | `1353.83` | `1261.30` | `0.0163` | -957,500.75 USD | `-7.21%` | `1X Cross` |
| `181` | `0x8742...8427` | `LONG` | 11,599,965.45 USD | `9,201.21` | `1286.37` | `1261.30` | `705.43` | -236,204.55 USD | `-2.04%` | `10X Cross` |
| `204` | `0x9ffd...ce40` | `LONG` | 10,651,170.46 USD | `8,441.92` | `1256.51` | `1261.30` | `606.80` | 43,801.82 USD | `+0.41%` | `5X Cross` |
| `205` | `0xad59...ba81` | `SHORT` | 10,617,185.00 USD | `8,425.00` | `330.91` | `1261.30` | `2143.70` | -7,829,227.23 USD | `-73.74%` | `10X Cross` |
| `212` | `0xdd53...2b13` | `SHORT` | 10,302,550.66 USD | `8,168.20` | `739.52` | `1261.30` | `8569.47` | -4,262,040.47 USD | `-41.37%` | `3X Cross` |
| `218` | `0xbf73...5d58` | `LONG` | 10,092,800.00 USD | `8,000.00` | `1291.41` | `1261.30` | `277.95` | -238,456.76 USD | `-2.36%` | `10X Cross` |
| `234` | `0x880a...311c` | `SHORT` | 9,725,602.11 USD | `7,707.11` | `1367.50` | `1261.30` | `2262.80` | 813,882.09 USD | `+8.37%` | `10X Cross` |
| `278` | `0x2b61...2f6c` | `LONG` | 8,580,904.20 USD | `6,807.00` | `1453.56` | `1261.30` | `537.41` | -1,313,447.02 USD | `-15.31%` | `10X Cross` |
| `292` | `0x2ae5...83e7` | `LONG` | 8,128,320.24 USD | `6,436.80` | `1391.82` | `1261.30` | `0.000000` | -830,571.76 USD | `-10.22%` | `1X Cross` |
| `340` | `0x26b6...9a13` | `LONG` | 6,853,020.28 USD | `5,433.73` | `1282.23` | `1261.30` | `211.21` | -114,282.96 USD | `-1.67%` | `10X Cross` |
| `356` | `0x45d2...4029` | `SHORT` | 6,600,598.10 USD | `5,227.00` | `833.44` | `1261.30` | `8764.81` | -2,244,220.13 USD | `-34.00%` | `5X Cross` |
| `373` | `0xecb6...2b00` | `SHORT` | 6,350,293.34 USD | `5,035.12` | `1304.94` | `1261.30` | `6653.88` | 220,242.53 USD | `+3.47%` | `5X Cross` |
| `378` | `0xea00...a918` | `LONG` | 6,309,500.00 USD | `5,000.00` | `739.16` | `1261.30` | `0.000000` | 2,613,684.89 USD | `+41.42%` | `5X Cross` |
| `380` | `0x58b2...11f3` | `LONG` | 6,261,918.04 USD | `4,963.08` | `1257.17` | `1261.30` | `0.000000` | 22,506.85 USD | `+0.36%` | `10X Cross` |
| `386` | `0xdd7a...8830` | `LONG` | 6,131,615.70 USD | `4,860.19` | `897.48` | `1261.30` | `790.38` | 1,769,712.03 USD | `+28.86%` | `10X Cross` |
| `438` | `0x4cae...7c34` | `LONG` | 5,047,896.22 USD | `4,004.36` | `999.34` | `1261.30` | `936.01` | 1,046,168.06 USD | `+20.72%` | `10X Cross` |
| `449` | `0xa61c...66b9` | `LONG` | 4,898,880.00 USD | `3,888.00` | `1148.34` | `1261.30` | `0.000000` | 434,137.86 USD | `+8.86%` | `10X Cross` |
| `468` | `0x9aa5...58af` | `SHORT` | 4,692,054.97 USD | `3,720.31` | `1205.51` | `1261.30` | `3621.22` | -207,168.17 USD | `-4.42%` | `10X Cross` |
| `470` | `0x0153...8052` | `SHORT` | 4,662,295.53 USD | `3,698.18` | `1307.82` | `1261.30` | `2504.73` | 174,275.22 USD | `+3.74%` | `1X Isolated` |
| `538` | `0xd21d...90f1` | `LONG` | 4,095,650.00 USD | `3,250.00` | `1253.64` | `1261.30` | `875.93` | 21,308.27 USD | `+0.52%` | `4X Isolated` |
| `562` | `0x1338...c48e` | `LONG` | 3,973,005.94 USD | `3,149.43` | `1018.52` | `1261.30` | `820.23` | 765,260.40 USD | `+19.26%` | `4X Isolated` |
| `571` | `0x456f...cdf1` | `LONG` | 3,952,739.53 USD | `3,134.11` | `1268.47` | `1261.30` | `493.67` | -22,769.93 USD | `-0.58%` | `10X Cross` |
| `573` | `0xd4c1...3d1d` | `SHORT` | 3,946,486.66 USD | `3,128.16` | `1299.47` | `1261.30` | `2825.70` | 118,450.65 USD | `+3.00%` | `10X Cross` |
| `576` | `0x382b...3e39` | `LONG` | 3,929,719.99 USD | `3,114.87` | `1211.32` | `1261.30` | `0.000000` | 156,606.51 USD | `+3.99%` | `10X Cross` |
| `582` | `0xdbe0...d6d5` | `LONG` | 3,896,513.77 USD | `3,085.37` | `422.97` | `1261.30` | `338.54` | 2,591,509.28 USD | `+66.51%` | `3X Isolated` |
| `589` | `0x27c9...d65d` | `SHORT` | 3,842,737.67 USD | `3,046.89` | `1254.41` | `1261.30` | `1744.58` | -20,684.97 USD | `-0.54%` | `10X Cross` |
| `596` | `0x325e...9564` | `LONG` | 3,784,507.94 USD | `3,001.91` | `1301.41` | `1261.30` | `144.46` | -122,201.27 USD | `-3.23%` | `10X Cross` |
| `601` | `0x9c06...0560` | `SHORT` | 3,771,931.68 USD | `2,989.80` | `786.00` | `1261.30` | `2534.04` | -1,421,936.68 USD | `-37.70%` | `10X Cross` |
| `612` | `0x2e30...4cb5` | `SHORT` | 3,710,478.17 USD | `2,938.32` | `1297.88` | `1261.30` | `2884.99` | 103,110.85 USD | `+2.78%` | `2X Cross` |
| `620` | `0xac48...3201` | `LONG` | 3,694,710.62 USD | `2,929.52` | `1378.58` | `1261.30` | `638.80` | -343,863.60 USD | `-9.31%` | `10X Cross` |
| `711` | `0xa183...0482` | `LONG` | 3,194,613.80 USD | `2,534.00` | `530.25` | `1261.30` | `444.47` | 1,850,951.08 USD | `+57.94%` | `5X Isolated` |
| `724` | `0x0871...e927` | `LONG` | 3,151,500.00 USD | `2,500.00` | `1276.50` | `1261.30` | `0.000000` | -39,750.00 USD | `-1.26%` | `10X Cross` |
| `735` | `0x9b86...6e6e` | `LONG` | 3,106,960.29 USD | `2,463.30` | `637.58` | `1261.30` | `882.40` | 1,536,411.01 USD | `+49.45%` | `3X Cross` |
| `782` | `0xb2f7...af9f` | `SHORT` | 2,914,593.08 USD | `2,313.72` | `746.63` | `1261.30` | `4365.14` | -1,187,104.34 USD | `-40.73%` | `10X Cross` |
| `807` | `0xf48f...10fe` | `LONG` | 2,799,512.53 USD | `2,218.49` | `1517.87` | `1261.30` | `969.16` | -567,874.29 USD | `-20.28%` | `3X Cross` |
| `840` | `0x5bc4...3b0c` | `SHORT` | 2,686,223.92 USD | `2,130.74` | `1089.65` | `1261.30` | `3668.24` | -364,466.34 USD | `-13.57%` | `5X Cross` |
| `856` | `0x8de4...b9aa` | `SHORT` | 2,638,580.59 USD | `2,091.29` | `1331.35` | `1261.30` | `1689.86` | 145,659.11 USD | `+5.52%` | `3X Cross` |
| `862` | `0x4fe2...ac59` | `SHORT` | 2,614,114.18 USD | `2,071.57` | `1478.56` | `1261.30` | `1828.89` | 448,832.03 USD | `+17.17%` | `10X Cross` |
| `890` | `0x9a99...d21a` | `LONG` | 2,523,400.00 USD | `2,000.00` | `1278.44` | `1261.30` | `0.000000` | -33,473.67 USD | `-1.33%` | `10X Cross` |
| `914` | `0x71d0...8c26` | `SHORT` | 2,468,194.24 USD | `1,956.40` | `1289.75` | `1261.30` | `4157.84` | 55,076.44 USD | `+2.23%` | `10X Cross` |
| `925` | `0x77ee...2902` | `SHORT` | 2,449,078.75 USD | `1,946.03` | `759.84` | `1261.30` | `5313.19` | -970,401.25 USD | `-39.62%` | `10X Cross` |
| `927` | `0x3e2f...b269` | `SHORT` | 2,430,571.27 USD | `1,925.51` | `1134.87` | `1261.30` | `2931.78` | -245,372.42 USD | `-10.10%` | `10X Cross` |
| `931` | `0xe097...d0fe` | `LONG` | 2,416,443.57 USD | `1,913.56` | `1261.17` | `1261.30` | `0.000000` | 3,117.40 USD | `+0.13%` | `10X Cross` |
| `940` | `0x4f12...618b` | `SHORT` | 2,392,536.48 USD | `1,896.28` | `1608.30` | `1261.30` | `2116.75` | 657,247.91 USD | `+27.47%` | `3X Cross` |
| `942` | `0x5323...b23c` | `SHORT` | 2,389,267.73 USD | `1,894.44` | `1282.67` | `1261.30` | `4185.96` | 40,665.50 USD | `+1.70%` | `5X Cross` |
| `990` | `0x866d...d6e1` | `LONG` | 2,271,664.23 USD | `1,802.05` | `674.73` | `1261.30` | `223.17` | 1,055,762.92 USD | `+46.48%` | `10X Cross` |
| `1011` | `0x2309...a2d9` | `LONG` | 2,206,516.42 USD | `1,750.37` | `1186.09` | `1261.30` | `814.37` | 130,422.31 USD | `+5.91%` | `8X Cross` |
| `1030` | `0x2edd...8179` | `SHORT` | 2,144,331.00 USD | `1,701.85` | `1261.58` | `1261.30` | `3075.51` | 2,687.85 USD | `+0.13%` | `10X Cross` |
| `1033` | `0x023a...2355` | `SHORT` | 2,140,153.01 USD | `1,696.38` | `1313.00` | `1261.30` | `5191.84` | 87,194.29 USD | `+4.07%` | `10X Cross` |
| `1063` | `0xfe7c...b7ae` | `SHORT` | 2,069,616.59 USD | `1,640.99` | `1347.05` | `1261.30` | `6880.93` | 140,872.60 USD | `+6.81%` | `10X Cross` |
| `1066` | `0x3e47...aaf6` | `LONG` | 2,062,530.94 USD | `1,636.28` | `1278.38` | `1261.30` | `1046.59` | -29,260.85 USD | `-1.42%` | `10X Cross` |
| `1067` | `0xa271...a3f7` | `LONG` | 2,058,375.23 USD | `1,631.43` | `1190.60` | `1261.30` | `910.32` | 115,993.43 USD | `+5.64%` | `4X Cross` |
| `1084` | `0x7f75...9edf` | `LONG` | 2,025,852.05 USD | `1,605.78` | `1199.97` | `1261.30` | `977.34` | 98,960.16 USD | `+4.88%` | `10X Cross` |
| `1090` | `0x6646...6de5` | `SHORT` | 2,021,440.00 USD | `1,600.00` | `660.64` | `1261.30` | `4507.66` | -964,415.03 USD | `-47.71%` | `10X Cross` |
| `1096` | `0x265e...7f70` | `LONG` | 2,015,309.27 USD | `1,601.74` | `1388.09` | `1261.30` | `0.000000` | -208,055.74 USD | `-10.32%` | `3X Cross` |
| `1112` | `0xdf57...93f5` | `LONG` | 1,993,025.22 USD | `1,579.76` | `1218.38` | `1261.30` | `780.17` | 68,269.24 USD | `+3.43%` | `3X Isolated` |
| `1132` | `0xab59...59b5` | `LONG` | 1,974,181.58 USD | `1,565.32` | `1342.15` | `1261.30` | `827.01` | -126,713.63 USD | `-6.42%` | `10X Cross` |
| `1185` | `0xcf67...eb24` | `LONG` | 1,892,850.00 USD | `1,500.00` | `887.05` | `1261.30` | `657.11` | 562,278.63 USD | `+29.71%` | `10X Cross` |
| `1195` | `0xb695...a92d` | `LONG` | 1,872,716.09 USD | `1,483.00` | `1249.80` | `1261.30` | `0.000000` | 19,257.23 USD | `+1.03%` | `10X Cross` |
| `1276` | `0x2ab7...c2f8` | `LONG` | 1,768,548.62 USD | `1,400.51` | `813.26` | `1261.30` | `797.87` | 629,566.94 USD | `+35.60%` | `3X Cross` |
| `1298` | `0x11be...8b1d` | `LONG` | 1,735,196.80 USD | `1,375.83` | `1206.55` | `1261.30` | `1134.45` | 75,188.84 USD | `+4.33%` | `10X Isolated` |
| `1391` | `0xe065...0f85` | `SHORT` | 1,593,035.04 USD | `1,262.61` | `1087.02` | `1261.30` | `1819.37` | -220,558.91 USD | `-13.85%` | `10X Cross` |
| `1410` | `0x039c...0ebd` | `SHORT` | 1,577,693.88 USD | `1,250.55` | `1239.86` | `1261.30` | `3625.14` | -27,182.60 USD | `-1.72%` | `10X Cross` |
| `1426` | `0x7277...0b98` | `SHORT` | 1,558,025.54 USD | `1,234.96` | `1298.48` | `1261.30` | `2415.31` | 45,543.88 USD | `+2.92%` | `10X Cross` |
| `1464` | `0x5975...9abd` | `LONG` | 1,513,440.00 USD | `1,200.00` | `1179.54` | `1261.30` | `513.24` | 97,997.21 USD | `+6.48%` | `5X Cross` |
| `1468` | `0xdf83...3cff` | `SHORT` | 1,501,544.13 USD | `1,191.04` | `1255.46` | `1261.30` | `1774.43` | -6,237.23 USD | `-0.42%` | `10X Cross` |
| `1495` | `0x69cc...14fd` | `SHORT` | 1,465,171.78 USD | `1,161.36` | `675.33` | `1261.30` | `8011.10` | -680,866.25 USD | `-46.47%` | `10X Cross` |
| `1518` | `0x3fc5...c0c1` | `SHORT` | 1,448,412.53 USD | `1,148.44` | `1264.34` | `1261.30` | `3056.04` | 3,601.25 USD | `+0.25%` | `10X Cross` |
| `1532` | `0x2847...d47b` | `LONG` | 1,428,946.78 USD | `1,131.58` | `1233.78` | `1261.30` | `0.000000` | 32,827.04 USD | `+2.30%` | `5X Cross` |
| `1544` | `0xe35c...a1d3` | `LONG` | 1,421,898.90 USD | `1,127.06` | `1318.20` | `1261.30` | `694.37` | -63,796.45 USD | `-4.49%` | `2X Isolated` |
| `1547` | `0x3205...40bb` | `SHORT` | 1,419,426.16 USD | `1,125.10` | `1266.84` | `1261.30` | `2570.04` | 5,900.38 USD | `+0.42%` | `10X Cross` |
| `1559` | `0x51f6...2b39` | `SHORT` | 1,407,146.06 USD | `1,115.72` | `1299.77` | `1261.30` | `2675.54` | 43,031.54 USD | `+3.06%` | `10X Cross` |
| `1561` | `0x5f94...4b96` | `LONG` | 1,406,690.05 USD | `1,115.27` | `538.00` | `1261.30` | `0.000000` | 806,672.41 USD | `+57.35%` | `10X Cross` |
| `1564` | `0xfc27...9d9d` | `SHORT` | 1,404,625.46 USD | `1,112.32` | `1315.10` | `1261.30` | `16092.26` | 58,186.30 USD | `+4.14%` | `10X Cross` |
| `1577` | `0x266b...efcb` | `LONG` | 1,389,740.00 USD | `1,100.00` | `863.84` | `1261.30` | `303.76` | 439,515.24 USD | `+31.63%` | `10X Cross` |
| `1583` | `0x71df...a23d` | `SHORT` | 1,384,491.77 USD | `1,098.28` | `513.50` | `1261.30` | `2550.73` | -820,521.58 USD | `-59.27%` | `2X Cross` |
| `1600` | `0xef96...9383` | `SHORT` | 1,361,064.54 USD | `1,078.84` | `1259.08` | `1261.30` | `5151.24` | -2,716.77 USD | `-0.20%` | `10X Cross` |
| `1604` | `0xbfc7...80b4` | `SHORT` | 1,356,220.00 USD | `1,075.00` | `558.03` | `1261.30` | `4444.08` | -756,341.27 USD | `-55.77%` | `10X Cross` |
| `1677` | `0x123d...3bff` | `SHORT` | 1,272,954.38 USD | `1,009.32` | `490.16` | `1261.30` | `4473.55` | -778,228.52 USD | `-61.14%` | `10X Cross` |
| `1688` | `0xb5ff...d912` | `LONG` | 1,262,789.00 USD | `1,000.00` | `1280.79` | `1261.30` | `452.80` | -17,998.44 USD | `-1.43%` | `2X Cross` |
| `1692` | `0xe282...df29` | `LONG` | 1,261,600.00 USD | `1,000.00` | `420.99` | `1261.30` | `187.23` | 840,613.14 USD | `+66.63%` | `10X Cross` |
| `1695` | `0x668c...ea2e` | `SHORT` | 1,260,600.00 USD | `1,000.00` | `1406.98` | `1261.30` | `4181.39` | 146,381.99 USD | `+11.61%` | `10X Cross` |
| `1715` | `0x17f0...094f` | `LONG` | 1,240,808.58 USD | `984.30` | `1287.23` | `1261.30` | `536.80` | -26,211.58 USD | `-2.11%` | `5X Cross` |
| `1788` | `0x757d...94ba` | `LONG` | 1,167,627.50 USD | `925.00` | `1558.31` | `1261.30` | `0.000000` | -273,813.09 USD | `-23.45%` | `10X Cross` |
| `1823` | `0xb911...5525` | `LONG` | 1,135,080.00 USD | `900.00` | `1294.82` | `1261.30` | `1070.32` | -30,257.82 USD | `-2.67%` | `10X Cross` |
| `1869` | `0x7a76...b16d` | `LONG` | 1,105,857.39 USD | `876.76` | `1297.31` | `1261.30` | `1198.83` | -31,573.27 USD | `-2.86%` | `10X Cross` |
| `1873` | `0xcf0a...856f` | `LONG` | 1,099,042.84 USD | `871.15` | `1292.19` | `1261.30` | `988.46` | -26,652.01 USD | `-2.43%` | `4X Cross` |
| `1889` | `0xdf95...7d72` | `SHORT` | 1,081,922.93 USD | `857.58` | `1074.37` | `1261.30` | `45437.56` | -160,567.55 USD | `-14.84%` | `10X Cross` |
| `1943` | `0x601c...4f54` | `SHORT` | 1,039,263.85 USD | `824.42` | `615.11` | `1261.30` | `3087.77` | -532,151.10 USD | `-51.20%` | `5X Cross` |
| `1952` | `0xae55...2236` | `LONG` | 1,030,584.43 USD | `817.47` | `1467.80` | `1261.30` | `0.000000` | -169,296.79 USD | `-16.43%` | `10X Cross` |
| `1994` | `0x9b0f...db40` | `LONG` | 1,010,320.00 USD | `800.00` | `1268.86` | `1261.30` | `787.17` | -4,769.76 USD | `-0.47%` | `10X Cross` |
| `1995` | `0x0f02...5384` | `LONG` | 1,009,783.58 USD | `800.78` | `1290.36` | `1261.30` | `298.96` | -23,510.49 USD | `-2.33%` | `3X Cross` |
| `2013` | `0x6e8f...4364` | `LONG` | 1,001,268.84 USD | `793.65` | `1260.00` | `1261.30` | `979.91` | 1,269.84 USD | `+0.13%` | `10X Cross` |
| `2016` | `0xabdb...84ac` | `LONG` | 1,000,525.61 USD | `793.69` | `711.79` | `1261.30` | `664.37` | 435,585.25 USD | `+43.54%` | `3X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `1092.10` | 8,889.69 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Long: 8.89K USD at 1092.1000 USD [API] | `2026-10-18 14:31:53` |
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
| `5m` | `BALANCED` | 0.00 USD | 1,750.00 USD | 1,750.00 USD | 1,750.00 USD | `1` | `2026-10-29 22:25:00 UTC - 2026-10-29 22:30:00 UTC` |
| `15m` | `BALANCED` | 0.00 USD | 1,750.00 USD | 1,750.00 USD | 1,750.00 USD | `1` | `2026-10-29 22:15:00 UTC - 2026-10-29 22:30:00 UTC` |
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
  * Current Rate: `8.02K` | Last 24h: `33.19K` | Last 3d: `283.86K` | Last 7d: `777.60K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `-0.0016%` | **USDT OKX** | `0.0008%` |
| **USDT Bybit** | `0.0100%` | **USDT KuCoin** | `-0.0045%` |
| **USDT MEXC** | `-0.0015%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `0.0006%` | **USDT Bitget** | `0.0100%` |
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
| `0:00 UTC` | `1294.05` | `1302.04` | `1294.05` | `1328.55` | `1286.25` | 68,949,402.59 USD | 35,232,633.05 USD | 33,716,769.55 USD | 1,515,863.50 USD | `+2.20%` | `6B / 24S` |
| `5:00 UTC` | `1306.05` | `1306.88` | `1306.05` | `1312.05` | `1300.05` | 17,712,248.68 USD | 9,074,345.66 USD | 8,637,903.02 USD | 436,442.64 USD | `+2.46%` | `3B / 5S` |
| `0:00 UTC` | `1249.20` | `1269.32` | `1249.20` | `1308.60` | `1241.40` | 130,590,816.99 USD | 58,796,845.15 USD | 71,793,971.84 USD | -12,997,126.69 USD | `-9.95%` | `4B / 19S` |
| `5:00 UTC` | `1229.25` | `1237.79` | `1229.25` | `1264.35` | `1206.75` | 149,162,484.89 USD | 77,012,548.38 USD | 72,149,936.51 USD | 4,862,611.87 USD | `+3.26%` | `9B / 11S` |
| `0:00 UTC` | `1249.95` | `1248.07` | `1249.95` | `1259.85` | `1233.15` | 61,152,789.32 USD | 32,267,997.87 USD | 28,884,791.45 USD | 3,383,206.41 USD | `+5.53%` | `6B / 4S` |
| `5:00 UTC` | `1273.95` | `1271.85` | `1273.95` | `1286.25` | `1253.25` | 67,607,862.35 USD | 37,234,359.13 USD | 30,373,503.22 USD | 6,860,855.91 USD | `+10.15%` | `6B / 2S` |
| `0:00 UTC` | `1294.65` | `1287.25` | `1294.65` | `1297.05` | `1269.15` | 47,983,765.84 USD | 24,978,907.15 USD | 23,004,858.69 USD | 1,974,048.46 USD | `+4.11%` | `4B / 9S` |
| `5:00 UTC` | `1264.05` | `1267.99` | `1264.05` | `1276.65` | `1260.75` | 31,349,361.20 USD | 15,100,777.24 USD | 16,248,583.96 USD | -1,147,806.72 USD | `-3.66%` | `0B / 1S` |
| `0:00 UTC` | `1261.05` | `1255.07` | `1261.05` | `1269.15` | `1241.25` | 60,510,539.13 USD | 31,467,084.85 USD | 29,043,454.28 USD | 2,423,630.57 USD | `+4.01%` | `3B / 5S` |
| `5:00 UTC` | `1247.55` | `1250.72` | `1247.55` | `1257.45` | `1242.15` | 11,977,950.07 USD | 6,539,390.12 USD | 5,438,559.95 USD | 1,100,830.17 USD | `+9.19%` | `3B / 3S` |

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
| `5m` | 513,240.00 USD | 1,780,000.00 USD | **`ACCUMULATION`** |
| `15m` | 1,070,000.00 USD | 9,180,000.00 USD | **`ACCUMULATION`** |
| `30m` | -267,860.00 USD | 3,020,000.00 USD | **`ACCUMULATION`** |
| `1h` | 3,020,000.00 USD | 2,290,000.00 USD | **`ACCUMULATION`** |
| `2h` | -8,820,000.00 USD | 1,930,000.00 USD | **`DISTRIBUTION`** |
| `4h` | -11,080,000.00 USD | -2,460,000.00 USD | **`DISTRIBUTION`** |
| `6h` | -5,130,000.00 USD | -18,210,000.00 USD | **`DISTRIBUTION`** |
| `8h` | 15,770,000.00 USD | 83,790,000.00 USD | **`ACCUMULATION`** |
| `12h` | 22,740,000.00 USD | 99,710,000.00 USD | **`ACCUMULATION`** |
| `24h` | 3,040,000.00 USD | 63,980,000.00 USD | **`ACCUMULATION`** |
| `1w` | 36,530,000.00 USD | 252,530,000.00 USD | **`ACCUMULATION`** |
| `30d` | 58,490,000.00 USD | -535,670,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+513.24K` | 15m=`+1.07M` | 1h=`+3.02M` | 24h=`+3.04M`
* Futures Capital Netflows: 5m=`+1.78M` | 15m=`+9.18M` | 1h=`+2.29M` | 24h=`+63.98M`
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
  * `2026-10-30 03:29:36 IST`: [investinglive.com] - (Sentiment: `Neutral`)
  * `2026-10-30 04:00:36 IST`: [msn.com] - (Sentiment: `Neutral`)
  * `2026-10-30 04:00:36 IST`: [morningstar.com] - (Sentiment: `Neutral`)
  * `2026-10-30 03:59:36 IST`: [sec.gov] - (Sentiment: `Neutral`)
  * `2026-10-30 01:01:36 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 01:01:36 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 01:01:36 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 00:01:36 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 00:01:36 IST`: [@DeItaone] - (Sentiment: `Neutral`)
  * `2026-10-30 00:01:36 IST`: [@mb_ghalibaf] - (Sentiment: `Neutral`)
  * `2026-10-29 23:01:36 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-29 23:01:36 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-29 23:01:36 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:01:36 IST`: [fxstreet.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:01:36 IST`: [ForexFactory] - (Sentiment: `Neutral`)


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
  * Execution Entry: `1247.88` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `1217.82` (Risk Distance: `30.06` pts)
  * +2.5R Take Profit: `1323.02`
  * Mathematical Lot Sizing: **`0.33 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `1276.64` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `1306.70` (Risk Distance: `30.06` pts)
  * +2.5R Take Profit: `1201.50`
  * Mathematical Lot Sizing: **`0.33 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`1269.34`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
