# 🏛️ SOVEREIGN CANDIDATE DOSSIER: ZECUSD
**Canonical Key**: `ZECUSD` | **Broker Instrument**: `ZECUSD.p` | **Asset Class**: `Crypto Altcoin`
**Timestamp**: `2026-10-30 03:40:27 IST` (`2026-10-29 22:10:27 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `1254.43` | **Live Ask Quote**: `1255.47` | **Mid Price**: `1254.95`
- **Spread Points**: `104.00` | **Spread BPS**: `8.29 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `1281.09` | VWAP Z-Score: `-0.55` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `22.38` (Volatility Regime: `HIGH_EXPANSION`)
  * 14-Period RSI: `37.75` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `1394.32` | Lower -3.00σ Band: `1167.85`
  * Upper +2.51σ Band: `1375.83` | Lower -2.51σ Band: `1186.34`
  * Upper +2.01σ Band: `1356.95` | Lower -2.01σ Band: `1205.22`
  * Upper +2.00σ Band: `1356.58` | Lower -2.00σ Band: `1205.59`
  * Upper +1.28σ Band: `1329.40` | Lower -1.28σ Band: `1232.77`
  * Upper +1.00σ Band: `1318.83` | Lower -1.00σ Band: `1243.34`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`1275.32` | EMA-20=`1291.96` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`1293.95` (Slope: `+0.0000`) | EMA-100=`1288.24`
  * Institutional Anchors: EMA-144=`1284.39` | EMA-200=`1280.59` (Slope: `+0.0510`) | EMA-233=`1279.78`
- **Range Boundaries**: 24H High=`1396.49` | 24H Low=`1206.89` | Weekly High=`1396.49` | Weekly Low=`1206.89`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `1285.20` (Distance: `-2.13%`)
  * Point of Control (POC) = `1268.59` (Distance: `-0.85%`)
  * Value Area Low (VAL) = `1259.96` (Distance: `-0.17%`)
  * Auction Positioning: `BELOW_VALUE (Imbalance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `RANGE_EXPANSION`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`1309.91` | POC=`1246.71` | VAL=`1230.27`
  * Prior Day Extremes: PDH=`1396.49` | PDL=`1206.89` | PDC=`1244.38`
  * Monday Range Blueprint: High=`1267.53` | Mid=`1222.14` | Low=`1176.75`
  * Developing Weekly Value Area: Weekly VAH=`1296.14` | Weekly POC=`1239.01` | Weekly VAL=`1196.53`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`1296.00` | Low=`1246.17`
  * London Session (08:00-16:00 UTC): High=`1259.97` | Low=`1249.93`
  * New York Session (13:00-21:00 UTC): High=`1262.48` | Low=`1247.42`
  * Initial Balance (First Hour): IB High=`1258.71` | IB Low=`1251.19`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `1249.93` - `1259.97`
  * Optimal Trade Entry (OTE 0.705): `1257.46`
  * Structural Invalidation Anchor (0.786): `1264.99`

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
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 03:35:39 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `16` | `0xb83d...6e36` | `SHORT` | 66,458,449.34 USD | `52,385.47` | `1336.45` | `1252.30` | `3970.17` | 3,552,118.06 USD | `+5.34%` | `3X Cross` |
| `22` | `0x5b5d...c060` | `SHORT` | 51,154,759.50 USD | `40,121.38` | `1478.36` | `1252.30` | `5430.66` | 8,159,275.61 USD | `+15.95%` | `3X Cross` |
| `43` | `0x7fda...17d1` | `SHORT` | 28,994,156.63 USD | `23,117.65` | `1262.46` | `1252.30` | `2979.54` | 190,870.26 USD | `+0.66%` | `5X Cross` |
| `84` | `0x60b0...991e` | `LONG` | 21,118,980.76 USD | `16,779.74` | `1179.65` | `1252.30` | `930.83` | 1,324,733.75 USD | `+6.27%` | `10X Cross` |
| `140` | `0xc36a...105b` | `LONG` | 14,553,129.73 USD | `11,510.82` | `1215.14` | `1252.30` | `959.27` | 565,848.70 USD | `+3.89%` | `10X Cross` |
| `158` | `0x9071...5c0b` | `LONG` | 13,244,423.30 USD | `10,517.29` | `1353.83` | `1252.30` | `0.0163` | -994,195.57 USD | `-7.51%` | `1X Cross` |
| `180` | `0x8742...8427` | `LONG` | 11,595,364.84 USD | `9,201.21` | `1286.37` | `1252.30` | `709.41` | -240,805.15 USD | `-2.08%` | `10X Cross` |
| `204` | `0xad59...ba81` | `SHORT` | 10,688,315.59 USD | `8,425.00` | `330.91` | `1252.30` | `2143.91` | -7,900,357.82 USD | `-73.92%` | `10X Cross` |
| `205` | `0x58b2...11f3` | `LONG` | 10,643,169.41 USD | `8,463.08` | `1257.17` | `1252.30` | `427.08` | 3,680.22 USD | `+0.03%` | `10X Cross` |
| `206` | `0x9ffd...ce40` | `LONG` | 10,621,520.44 USD | `8,443.18` | `1256.59` | `1252.30` | `609.10` | 11,903.09 USD | `+0.11%` | `5X Cross` |
| `214` | `0xdd53...2b13` | `SHORT` | 10,245,373.26 USD | `8,168.20` | `739.52` | `1252.30` | `8695.47` | -4,204,863.07 USD | `-41.04%` | `3X Cross` |
| `219` | `0xbf73...5d58` | `LONG` | 10,060,000.00 USD | `8,000.00` | `1291.41` | `1252.30` | `293.17` | -271,256.76 USD | `-2.70%` | `10X Cross` |
| `232` | `0x880a...311c` | `SHORT` | 9,737,162.77 USD | `7,707.11` | `1367.50` | `1252.30` | `2271.74` | 802,321.43 USD | `+8.24%` | `10X Cross` |
| `280` | `0x2b61...2f6c` | `LONG` | 8,559,802.50 USD | `6,807.00` | `1453.56` | `1252.30` | `525.49` | -1,334,548.72 USD | `-15.59%` | `10X Cross` |
| `290` | `0x2ae5...83e7` | `LONG` | 8,102,495.15 USD | `6,436.80` | `1391.82` | `1252.30` | `0.000000` | -856,396.84 USD | `-10.57%` | `1X Cross` |
| `339` | `0x26b6...9a13` | `LONG` | 6,834,545.59 USD | `5,433.73` | `1282.23` | `1252.30` | `217.38` | -132,757.64 USD | `-1.94%` | `10X Cross` |
| `355` | `0x45d2...4029` | `SHORT` | 6,579,626.86 USD | `5,227.00` | `833.44` | `1252.30` | `8925.76` | -2,223,248.88 USD | `-33.79%` | `5X Cross` |
| `371` | `0xea00...a918` | `LONG` | 6,320,000.00 USD | `5,000.00` | `739.16` | `1252.30` | `0.000000` | 2,624,184.89 USD | `+41.52%` | `5X Cross` |
| `377` | `0xecb6...2b00` | `SHORT` | 6,295,105.72 USD | `5,019.22` | `1305.21` | `1252.30` | `6815.34` | 256,007.32 USD | `+4.07%` | `5X Cross` |
| `385` | `0xdd7a...8830` | `LONG` | 6,142,702.28 USD | `4,860.19` | `897.48` | `1252.30` | `777.34` | 1,780,798.61 USD | `+28.99%` | `10X Cross` |
| `435` | `0x4cae...7c34` | `LONG` | 5,059,108.42 USD | `4,004.36` | `999.34` | `1252.30` | `929.40` | 1,057,380.27 USD | `+20.90%` | `10X Cross` |
| `446` | `0xa61c...66b9` | `LONG` | 4,924,540.80 USD | `3,888.00` | `1148.34` | `1252.30` | `0.000000` | 459,798.66 USD | `+9.34%` | `10X Cross` |
| `451` | `0x5323...b23c` | `SHORT` | 4,896,239.72 USD | `3,893.63` | `1287.34` | `1252.30` | `2683.80` | 116,174.76 USD | `+2.37%` | `5X Cross` |
| `463` | `0x9aa5...58af` | `SHORT` | 4,725,537.76 USD | `3,720.31` | `1205.51` | `1252.30` | `3632.91` | -240,650.96 USD | `-5.09%` | `10X Cross` |
| `473` | `0x0153...8052` | `SHORT` | 4,638,627.17 USD | `3,698.18` | `1307.82` | `1252.30` | `2504.73` | 197,943.57 USD | `+4.27%` | `1X Isolated` |
| `511` | `0xfc66...ca06` | `SHORT` | 4,333,092.94 USD | `3,444.43` | `1319.65` | `1252.30` | `9210.18` | 212,358.27 USD | `+4.90%` | `10X Cross` |
| `540` | `0xd21d...90f1` | `LONG` | 4,107,123.48 USD | `3,250.00` | `1253.64` | `1252.30` | `875.93` | 32,781.74 USD | `+0.80%` | `4X Isolated` |
| `562` | `0x1338...c48e` | `LONG` | 3,977,730.09 USD | `3,149.43` | `1018.52` | `1252.30` | `820.23` | 769,984.55 USD | `+19.36%` | `4X Isolated` |
| `568` | `0x456f...cdf1` | `LONG` | 3,963,082.10 USD | `3,134.11` | `1268.47` | `1252.30` | `493.65` | -12,427.37 USD | `-0.31%` | `10X Cross` |
| `582` | `0x382b...3e39` | `LONG` | 3,908,789.55 USD | `3,116.56` | `1211.32` | `1252.30` | `0.000000` | 133,628.93 USD | `+3.42%` | `10X Cross` |
| `586` | `0xdbe0...d6d5` | `LONG` | 3,883,735.40 USD | `3,085.37` | `422.97` | `1252.30` | `338.54` | 2,578,730.91 USD | `+66.40%` | `3X Isolated` |
| `589` | `0xd4c1...3d1d` | `SHORT` | 3,875,302.41 USD | `3,089.86` | `1300.01` | `1252.30` | `2900.90` | 141,536.03 USD | `+3.65%` | `10X Cross` |
| `594` | `0x27c9...d65d` | `SHORT` | 3,834,094.66 USD | `3,047.77` | `1254.41` | `1252.30` | `1766.60` | -10,938.08 USD | `-0.29%` | `10X Cross` |
| `600` | `0x325e...9564` | `LONG` | 3,802,219.21 USD | `3,001.91` | `1301.41` | `1252.30` | `152.51` | -104,490.00 USD | `-2.75%` | `10X Cross` |
| `603` | `0x9c06...0560` | `SHORT` | 3,779,705.16 USD | `2,989.80` | `786.00` | `1252.30` | `2544.00` | -1,429,710.16 USD | `-37.83%` | `10X Cross` |
| `621` | `0xac48...3201` | `LONG` | 3,687,093.87 USD | `2,929.52` | `1378.58` | `1252.30` | `649.57` | -351,480.35 USD | `-9.53%` | `10X Cross` |
| `624` | `0x2e30...4cb5` | `SHORT` | 3,684,551.13 USD | `2,937.77` | `1297.89` | `1252.30` | `2897.39` | 128,351.34 USD | `+3.48%` | `2X Cross` |
| `718` | `0xa183...0482` | `LONG` | 3,189,039.00 USD | `2,534.00` | `530.25` | `1252.30` | `444.47` | 1,845,376.28 USD | `+57.87%` | `5X Isolated` |
| `722` | `0x0871...e927` | `LONG` | 3,160,750.00 USD | `2,500.00` | `1276.50` | `1252.30` | `0.000000` | -30,500.00 USD | `-0.96%` | `10X Cross` |
| `724` | `0x413c...886c` | `LONG` | 3,160,000.00 USD | `2,500.00` | `1268.64` | `1252.30` | `0.000000` | -11,611.64 USD | `-0.37%` | `10X Cross` |
| `739` | `0x9b86...6e6e` | `LONG` | 3,130,122.38 USD | `2,467.30` | `637.58` | `1252.30` | `889.67` | 1,557,022.78 USD | `+49.74%` | `3X Cross` |
| `787` | `0xb2f7...af9f` | `SHORT` | 2,923,918.07 USD | `2,313.72` | `746.63` | `1252.30` | `4379.13` | -1,196,429.32 USD | `-40.92%` | `10X Cross` |
| `819` | `0xf48f...10fe` | `LONG` | 2,803,573.03 USD | `2,218.49` | `1517.87` | `1252.30` | `965.67` | -563,813.79 USD | `-20.11%` | `3X Cross` |
| `852` | `0x5bc4...3b0c` | `SHORT` | 2,680,530.58 USD | `2,130.74` | `1089.65` | `1252.30` | `3682.47` | -358,773.00 USD | `-13.38%` | `5X Cross` |
| `864` | `0x8de4...b9aa` | `SHORT` | 2,630,842.82 USD | `2,091.29` | `1331.35` | `1252.30` | `1689.86` | 153,396.89 USD | `+5.83%` | `3X Cross` |
| `869` | `0x4fe2...ac59` | `SHORT` | 2,618,464.48 USD | `2,071.57` | `1478.56` | `1252.30` | `1831.40` | 444,481.73 USD | `+16.97%` | `10X Cross` |
| `890` | `0x71d0...8c26` | `SHORT` | 2,545,806.19 USD | `2,024.82` | `1289.75` | `1252.30` | `4051.37` | 65,709.32 USD | `+2.58%` | `10X Cross` |
| `902` | `0x9a99...d21a` | `LONG` | 2,514,600.00 USD | `2,000.00` | `1278.44` | `1252.30` | `0.000000` | -42,273.67 USD | `-1.68%` | `10X Cross` |
| `924` | `0x77ee...2902` | `SHORT` | 2,458,614.30 USD | `1,946.03` | `759.84` | `1252.30` | `5334.02` | -979,936.80 USD | `-39.86%` | `10X Cross` |
| `939` | `0x3e2f...b269` | `SHORT` | 2,422,345.49 USD | `1,925.51` | `1134.87` | `1252.30` | `2931.78` | -237,146.64 USD | `-9.79%` | `10X Cross` |
| `946` | `0xe097...d0fe` | `LONG` | 2,405,727.63 USD | `1,913.56` | `1261.17` | `1252.30` | `0.000000` | -7,598.53 USD | `-0.32%` | `10X Cross` |
| `953` | `0x4f12...618b` | `SHORT` | 2,385,520.24 USD | `1,896.28` | `1608.30` | `1252.30` | `2116.75` | 664,264.15 USD | `+27.85%` | `3X Cross` |
| `1000` | `0x866d...d6e1` | `LONG` | 2,266,077.88 USD | `1,802.05` | `674.73` | `1252.30` | `228.38` | 1,050,176.56 USD | `+46.34%` | `10X Cross` |
| `1014` | `0x2309...a2d9` | `LONG` | 2,229,271.23 USD | `1,750.37` | `1186.09` | `1252.30` | `813.20` | 153,177.12 USD | `+6.87%` | `8X Cross` |
| `1037` | `0x2edd...8179` | `SHORT` | 2,159,477.46 USD | `1,701.85` | `1261.58` | `1252.30` | `3069.26` | -12,458.61 USD | `-0.58%` | `10X Cross` |
| `1039` | `0x023a...2355` | `SHORT` | 2,148,634.91 USD | `1,696.38` | `1313.00` | `1252.30` | `5705.08` | 78,712.39 USD | `+3.66%` | `10X Cross` |
| `1069` | `0x3e47...aaf6` | `LONG` | 2,084,293.46 USD | `1,636.28` | `1278.38` | `1252.30` | `1045.67` | -7,498.32 USD | `-0.36%` | `10X Cross` |
| `1076` | `0xa271...a3f7` | `LONG` | 2,059,027.80 USD | `1,631.43` | `1190.60` | `1252.30` | `910.31` | 116,646.00 USD | `+5.67%` | `4X Cross` |
| `1078` | `0xfe7c...b7ae` | `SHORT` | 2,058,129.66 USD | `1,640.99` | `1347.05` | `1252.30` | `7147.04` | 152,359.53 USD | `+7.40%` | `10X Cross` |
| `1098` | `0x7f75...9edf` | `LONG` | 2,019,268.35 USD | `1,605.78` | `1199.97` | `1252.30` | `977.80` | 92,376.46 USD | `+4.57%` | `10X Cross` |
| `1103` | `0x265e...7f70` | `LONG` | 2,014,988.92 USD | `1,601.74` | `1388.09` | `1252.30` | `0.000000` | -208,376.09 USD | `-10.34%` | `3X Cross` |
| `1112` | `0x6646...6de5` | `SHORT` | 2,007,680.00 USD | `1,600.00` | `660.64` | `1252.30` | `4356.48` | -950,655.03 USD | `-47.35%` | `10X Cross` |
| `1130` | `0xdf57...93f5` | `LONG` | 1,985,758.32 USD | `1,579.76` | `1218.38` | `1252.30` | `780.17` | 61,002.34 USD | `+3.07%` | `3X Isolated` |
| `1133` | `0xab59...59b5` | `LONG` | 1,980,599.40 USD | `1,565.32` | `1342.15` | `1252.30` | `827.16` | -120,295.82 USD | `-6.07%` | `10X Cross` |
| `1195` | `0xcf67...eb24` | `LONG` | 1,893,150.00 USD | `1,500.00` | `887.05` | `1252.30` | `658.74` | 562,578.63 USD | `+29.72%` | `10X Cross` |
| `1206` | `0xb695...a92d` | `LONG` | 1,866,800.40 USD | `1,483.00` | `1249.80` | `1252.30` | `0.000000` | 13,341.55 USD | `+0.71%` | `10X Cross` |
| `1275` | `0x3205...40bb` | `SHORT` | 1,778,835.72 USD | `1,418.19` | `1269.66` | `1252.30` | `2287.70` | 21,784.47 USD | `+1.22%` | `10X Cross` |
| `1291` | `0x2ab7...c2f8` | `LONG` | 1,756,519.64 USD | `1,400.51` | `813.26` | `1252.30` | `804.42` | 617,537.96 USD | `+35.16%` | `3X Cross` |
| `1302` | `0x11be...8b1d` | `LONG` | 1,739,737.03 USD | `1,375.83` | `1206.55` | `1252.30` | `1134.43` | 79,729.08 USD | `+4.58%` | `10X Isolated` |
| `1394` | `0xe065...0f85` | `SHORT` | 1,593,540.08 USD | `1,262.61` | `1087.02` | `1252.30` | `1819.54` | -221,063.95 USD | `-13.87%` | `10X Cross` |
| `1426` | `0x039c...0ebd` | `SHORT` | 1,572,566.62 USD | `1,250.55` | `1239.86` | `1252.30` | `3643.18` | -22,055.34 USD | `-1.40%` | `10X Cross` |
| `1444` | `0x7277...0b98` | `SHORT` | 1,552,344.72 USD | `1,234.96` | `1298.48` | `1252.30` | `2428.76` | 51,224.70 USD | `+3.30%` | `10X Cross` |
| `1476` | `0x5975...9abd` | `LONG` | 1,516,800.00 USD | `1,200.00` | `1179.54` | `1252.30` | `480.01` | 101,357.21 USD | `+6.68%` | `5X Cross` |
| `1504` | `0xdf83...3cff` | `SHORT` | 1,473,543.39 USD | `1,172.27` | `1255.30` | `1252.30` | `1765.18` | -1,996.01 USD | `-0.14%` | `10X Cross` |
| `1513` | `0x69cc...14fd` | `SHORT` | 1,460,758.61 USD | `1,161.36` | `675.33` | `1252.30` | `8053.90` | -676,453.08 USD | `-46.31%` | `10X Cross` |
| `1536` | `0x3fc5...c0c1` | `SHORT` | 1,445,426.58 USD | `1,148.44` | `1264.34` | `1252.30` | `3115.86` | 6,587.19 USD | `+0.46%` | `10X Cross` |
| `1551` | `0xe35c...a1d3` | `LONG` | 1,427,534.20 USD | `1,127.06` | `1318.20` | `1252.30` | `694.37` | -58,161.15 USD | `-4.07%` | `2X Isolated` |
| `1564` | `0x2847...d47b` | `LONG` | 1,417,856.40 USD | `1,127.52` | `1233.70` | `1252.30` | `0.000000` | 26,831.57 USD | `+1.89%` | `5X Cross` |
| `1569` | `0x5f94...4b96` | `LONG` | 1,414,879.26 USD | `1,115.27` | `538.00` | `1252.30` | `0.000000` | 814,861.62 USD | `+57.59%` | `10X Cross` |
| `1579` | `0xfc27...9d9d` | `SHORT` | 1,400,162.72 USD | `1,112.32` | `1315.10` | `1252.30` | `16608.24` | 62,649.04 USD | `+4.47%` | `10X Cross` |
| `1587` | `0x51f6...2b39` | `SHORT` | 1,389,399.18 USD | `1,104.89` | `1300.30` | `1252.30` | `2745.65` | 47,286.48 USD | `+3.40%` | `10X Cross` |
| `1590` | `0x71df...a23d` | `SHORT` | 1,387,566.95 USD | `1,098.28` | `513.50` | `1252.30` | `2551.62` | -823,596.76 USD | `-59.36%` | `2X Cross` |
| `1599` | `0x266b...efcb` | `LONG` | 1,380,280.00 USD | `1,100.00` | `863.84` | `1252.30` | `315.14` | 430,055.24 USD | `+31.16%` | `10X Cross` |
| `1612` | `0xbfc7...80b4` | `SHORT` | 1,357,832.50 USD | `1,075.00` | `558.03` | `1252.30` | `5332.06` | -757,953.77 USD | `-55.82%` | `10X Cross` |
| `1614` | `0xef96...9383` | `SHORT` | 1,356,276.62 USD | `1,078.55` | `1259.08` | `1252.30` | `5179.41` | 1,708.68 USD | `+0.13%` | `10X Cross` |
| `1679` | `0x123d...3bff` | `SHORT` | 1,275,780.48 USD | `1,009.32` | `490.16` | `1252.30` | `4447.16` | -781,054.61 USD | `-61.22%` | `10X Cross` |
| `1682` | `0xe282...df29` | `LONG` | 1,273,200.00 USD | `1,000.00` | `420.99` | `1252.30` | `178.75` | 852,213.14 USD | `+66.93%` | `10X Cross` |
| `1690` | `0x668c...ea2e` | `SHORT` | 1,266,800.00 USD | `1,000.00` | `1406.98` | `1252.30` | `4180.89` | 140,181.99 USD | `+11.07%` | `10X Cross` |
| `1701` | `0xb5ff...d912` | `LONG` | 1,258,776.90 USD | `1,000.00` | `1280.79` | `1252.30` | `452.80` | -22,010.54 USD | `-1.75%` | `2X Cross` |
| `1709` | `0x38f9...cb04` | `SHORT` | 1,254,148.54 USD | `996.17` | `1269.09` | `1252.30` | `2146.04` | 10,080.35 USD | `+0.80%` | `10X Cross` |
| `1719` | `0x17f0...094f` | `LONG` | 1,243,170.90 USD | `984.30` | `1287.23` | `1252.30` | `536.80` | -23,849.26 USD | `-1.92%` | `5X Cross` |
| `1800` | `0x757d...94ba` | `LONG` | 1,163,675.90 USD | `925.00` | `1558.31` | `1252.30` | `0.000000` | -277,764.68 USD | `-23.87%` | `10X Cross` |
| `1823` | `0xb911...5525` | `LONG` | 1,144,440.00 USD | `900.00` | `1294.82` | `1252.30` | `1070.30` | -20,897.82 USD | `-1.83%` | `10X Cross` |
| `1868` | `0x7a76...b16d` | `LONG` | 1,107,988.18 USD | `876.76` | `1297.31` | `1252.30` | `1199.04` | -29,442.48 USD | `-2.66%` | `10X Cross` |
| `1880` | `0xcf0a...856f` | `LONG` | 1,095,471.12 USD | `871.15` | `1292.19` | `1252.30` | `992.86` | -30,223.72 USD | `-2.76%` | `4X Cross` |
| `1901` | `0xdf95...7d72` | `SHORT` | 1,075,514.13 USD | `857.53` | `1074.36` | `1252.30` | `46636.74` | -154,221.33 USD | `-14.34%` | `10X Cross` |
| `1949` | `0x601c...4f54` | `SHORT` | 1,036,708.15 USD | `824.42` | `615.11` | `1252.30` | `3092.58` | -529,595.40 USD | `-51.08%` | `5X Cross` |
| `1960` | `0xae55...2236` | `LONG` | 1,029,012.35 USD | `817.47` | `1467.80` | `1252.30` | `0.000000` | -170,868.86 USD | `-16.61%` | `10X Cross` |
| `2010` | `0x0f02...5384` | `LONG` | 1,007,221.08 USD | `800.78` | `1290.36` | `1252.30` | `301.21` | -26,072.99 USD | `-2.59%` | `3X Cross` |
| `2012` | `0x9b0f...db40` | `LONG` | 1,007,006.72 USD | `800.00` | `1268.86` | `1252.30` | `790.39` | -8,083.04 USD | `-0.80%` | `10X Cross` |

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
  * 24H Horizon: Short MP=`1403.54` (Vol: 3,000,000.00 USD, Dist: `+10.01%`) | Long MP=`1200.05` (Vol: 597,500.00 USD, Dist: `--5.94%`)
  * 48H Horizon: Short MP=`1403.54` (Vol: 3,000,000.00 USD, Dist: `+10.01%`) | Long MP=`1246.00` (Vol: 2,300,000.00 USD, Dist: `--2.34%`)
  * 3D Horizon: Short MP=`1403.54` (Vol: 3,000,000.00 USD, Dist: `+10.01%`) | Long MP=`1247.64` (Vol: 2,400,000.00 USD, Dist: `--2.21%`)
  * 7D Horizon: Short MP=`1404.10` (Vol: 3,000,000.00 USD, Dist: `+10.05%`) | Long MP=`1200.46` (Vol: 3,000,000.00 USD, Dist: `--5.91%`)
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
| `5m` | `BALANCED` | 0.00 USD | 1,750.00 USD | 1,750.00 USD | 1,750.00 USD | `1` | `2026-10-29 22:05:00 UTC - 2026-10-29 22:10:00 UTC` |
| `15m` | `BALANCED` | 0.00 USD | 1,750.00 USD | 1,750.00 USD | 1,750.00 USD | `1` | `2026-10-29 22:00:00 UTC - 2026-10-29 22:15:00 UTC` |
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
  * Current Rate: `6.11K` | Last 24h: `33.19K` | Last 3d: `283.86K` | Last 7d: `777.60K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `-0.0016%` | **USDT OKX** | `0.0007%` |
| **USDT Bybit** | `0.0100%` | **USDT KuCoin** | `-0.0055%` |
| **USDT MEXC** | `-0.0016%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `-0.0057%` | **USDT Bitget** | `0.0100%` |
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
| `5:00 UTC` | `1325.25` | `1325.38` | `1325.25` | `1330.65` | `1320.75` | 11,021,893.68 USD | 5,577,839.59 USD | 5,444,054.10 USD | 133,785.49 USD | `+1.21%` | `3B / 1S` |
| `0:00 UTC` | `1294.05` | `1302.04` | `1294.05` | `1328.55` | `1286.25` | 68,949,402.59 USD | 35,232,633.05 USD | 33,716,769.55 USD | 1,515,863.50 USD | `+2.20%` | `6B / 24S` |
| `5:00 UTC` | `1306.05` | `1306.88` | `1306.05` | `1312.05` | `1300.05` | 17,712,248.68 USD | 9,074,345.66 USD | 8,637,903.02 USD | 436,442.64 USD | `+2.46%` | `3B / 5S` |
| `0:00 UTC` | `1249.20` | `1269.32` | `1249.20` | `1308.60` | `1241.40` | 130,590,816.99 USD | 58,796,845.15 USD | 71,793,971.84 USD | -12,997,126.69 USD | `-9.95%` | `4B / 19S` |
| `5:00 UTC` | `1229.25` | `1237.79` | `1229.25` | `1264.35` | `1206.75` | 149,162,484.89 USD | 77,012,548.38 USD | 72,149,936.51 USD | 4,862,611.87 USD | `+3.26%` | `9B / 11S` |
| `0:00 UTC` | `1249.95` | `1248.07` | `1249.95` | `1259.85` | `1233.15` | 61,152,789.32 USD | 32,267,997.87 USD | 28,884,791.45 USD | 3,383,206.41 USD | `+5.53%` | `6B / 4S` |
| `5:00 UTC` | `1273.95` | `1271.85` | `1273.95` | `1286.25` | `1253.25` | 67,607,862.35 USD | 37,234,359.13 USD | 30,373,503.22 USD | 6,860,855.91 USD | `+10.15%` | `6B / 2S` |
| `0:00 UTC` | `1294.65` | `1287.25` | `1294.65` | `1297.05` | `1269.15` | 47,983,765.84 USD | 24,978,907.15 USD | 23,004,858.69 USD | 1,974,048.46 USD | `+4.11%` | `4B / 9S` |
| `5:00 UTC` | `1264.05` | `1267.99` | `1264.05` | `1276.65` | `1260.75` | 31,349,361.20 USD | 15,100,777.24 USD | 16,248,583.96 USD | -1,147,806.72 USD | `-3.66%` | `0B / 1S` |
| `0:00 UTC` | `1261.95` | `1262.96` | `1261.95` | `1269.15` | `1258.95` | 6,881,925.29 USD | 3,378,791.27 USD | 3,503,134.02 USD | -124,342.74 USD | `-1.81%` | `3B / 5S` |

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
| `5m` | -734,770.00 USD | -1,570,000.00 USD | **`DISTRIBUTION`** |
| `15m` | -760,070.00 USD | -4,630,000.00 USD | **`DISTRIBUTION`** |
| `30m` | 619,510.00 USD | -11,580,000.00 USD | **`DISTRIBUTION`** |
| `1h` | 5,590,000.00 USD | 17,350,000.00 USD | **`ACCUMULATION`** |
| `2h` | -8,370,000.00 USD | 2,350,000.00 USD | **`DISTRIBUTION`** |
| `4h` | -10,420,000.00 USD | -16,670,000.00 USD | **`DISTRIBUTION`** |
| `6h` | 7,110,000.00 USD | -4,400,000.00 USD | **`ACCUMULATION`** |
| `8h` | 17,010,000.00 USD | 83,400,000.00 USD | **`ACCUMULATION`** |
| `12h` | 21,840,000.00 USD | 93,760,000.00 USD | **`ACCUMULATION`** |
| `24h` | 2,680,000.00 USD | 58,330,000.00 USD | **`ACCUMULATION`** |
| `1w` | 35,580,000.00 USD | 244,880,000.00 USD | **`ACCUMULATION`** |
| `30d` | 57,860,000.00 USD | -543,320,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-734.77K` | 15m=`-760.07K` | 1h=`+5.59M` | 24h=`+2.68M`
* Futures Capital Netflows: 5m=`-1.57M` | 15m=`-4.63M` | 1h=`+17.35M` | 24h=`+58.33M`
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
  * `2026-10-30 03:29:54 IST`: [investinglive.com] - (Sentiment: `Neutral`)
  * `2026-10-30 02:53:54 IST`: [msn.com] - (Sentiment: `Neutral`)
  * `2026-10-30 03:30:54 IST`: [morningstar.com] - (Sentiment: `Neutral`)
  * `2026-10-30 03:30:54 IST`: [sec.gov] - (Sentiment: `Neutral`)
  * `2026-10-30 03:29:54 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 03:29:54 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 00:31:54 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:31:54 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:31:54 IST`: [@DeItaone] - (Sentiment: `Neutral`)
  * `2026-10-29 23:31:54 IST`: [@mb_ghalibaf] - (Sentiment: `Neutral`)
  * `2026-10-29 23:31:54 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-29 23:31:54 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-29 23:31:54 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:31:54 IST`: [fxstreet.com] - (Sentiment: `Neutral`)
  * `2026-10-29 21:31:54 IST`: [ForexFactory] - (Sentiment: `Neutral`)


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
  * Execution Entry: `1259.96` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `1231.54` (Risk Distance: `28.42` pts)
  * +2.5R Take Profit: `1331.01`
  * Mathematical Lot Sizing: **`0.35 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `1285.20` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `1313.62` (Risk Distance: `28.42` pts)
  * +2.5R Take Profit: `1214.15`
  * Mathematical Lot Sizing: **`0.35 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`1264.99`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
