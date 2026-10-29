# 🏛️ SOVEREIGN CANDIDATE DOSSIER: ZECUSD
**Canonical Key**: `ZECUSD` | **Broker Instrument**: `ZECUSD.p` | **Asset Class**: `Crypto Altcoin`
**Timestamp**: `2026-10-30 01:57:19 IST` (`2026-10-29 20:27:19 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `1308.91` | **Live Ask Quote**: `1309.94` | **Mid Price**: `1309.43`
- **Spread Points**: `103.00` | **Spread BPS**: `7.87 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `1282.22` | VWAP Z-Score: `+0.64` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `16.40` (Volatility Regime: `HIGH_EXPANSION`)
  * 14-Period RSI: `45.14` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `1398.54` | Lower -3.00σ Band: `1165.90`
  * Upper +2.51σ Band: `1379.54` | Lower -2.51σ Band: `1184.90`
  * Upper +2.01σ Band: `1360.15` | Lower -2.01σ Band: `1204.29`
  * Upper +2.00σ Band: `1359.77` | Lower -2.00σ Band: `1204.68`
  * Upper +1.28σ Band: `1331.85` | Lower -1.28σ Band: `1232.59`
  * Upper +1.00σ Band: `1320.99` | Lower -1.00σ Band: `1243.45`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`1321.65` | EMA-20=`1321.23` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`1303.86` (Slope: `+0.0000`) | EMA-100=`1292.03`
  * Institutional Anchors: EMA-144=`1286.63` | EMA-200=`1281.62` (Slope: `+0.4345`) | EMA-233=`1279.58`
- **Range Boundaries**: 24H High=`1396.49` | 24H Low=`1230.00` | Weekly High=`1396.49` | Weekly Low=`1210.62`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `1309.36` (Distance: `-0.04%`)
  * Point of Control (POC) = `1247.20` (Distance: `+4.94%`)
  * Value Area Low (VAL) = `1230.55` (Distance: `+6.36%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BULLISH (Above Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`1320.44` | POC=`1312.10` | VAL=`1285.78`
  * Prior Day Extremes: PDH=`1328.99` | PDL=`1263.19` | PDC=`1296.46`
  * Monday Range Blueprint: High=`1267.53` | Mid=`1222.14` | Low=`1176.75`
  * Developing Weekly Value Area: Weekly VAH=`1296.14` | Weekly POC=`1239.01` | Weekly VAL=`1195.06`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`1318.68` | Low=`1230.00`
  * London Session (08:00-16:00 UTC): High=`1276.13` | Low=`1233.52`
  * New York Session (13:00-21:00 UTC): High=`1396.49` | Low=`1250.65`
  * Initial Balance (First Hour): IB High=`1255.79` | IB Low=`1245.43`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `1304.19` - `1314.66`
  * Optimal Trade Entry (OTE 0.705): `1312.04`
  * Structural Invalidation Anchor (0.786): `1319.90`

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
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 01:54:30 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `16` | `0xb83d...6e36` | `SHORT` | 68,751,644.90 USD | `52,582.52` | `1336.45` | `1307.90` | `3780.75` | 1,522,270.00 USD | `+2.21%` | `3X Cross` |
| `24` | `0x5b5d...c060` | `SHORT` | 53,210,622.47 USD | `40,727.61` | `1478.36` | `1307.90` | `5112.98` | 6,999,641.73 USD | `+13.15%` | `3X Cross` |
| `41` | `0x7fda...17d1` | `SHORT` | 29,391,459.36 USD | `22,492.89` | `1261.62` | `1307.90` | `2868.28` | -1,013,874.54 USD | `-3.45%` | `5X Cross` |
| `78` | `0x60b0...991e` | `LONG` | 21,926,086.26 USD | `16,779.74` | `1179.65` | `1307.90` | `898.73` | 2,131,839.24 USD | `+9.72%` | `10X Cross` |
| `84` | `0xbf73...5d58` | `LONG` | 20,907,200.00 USD | `16,000.00` | `1214.30` | `1307.90` | `737.18` | 1,478,367.75 USD | `+7.07%` | `10X Cross` |
| `135` | `0xc36a...105b` | `LONG` | 15,034,282.00 USD | `11,510.82` | `1215.14` | `1307.90` | `940.14` | 1,047,000.97 USD | `+6.96%` | `10X Cross` |
| `168` | `0x8742...8427` | `LONG` | 12,031,502.20 USD | `9,201.21` | `1286.37` | `1307.90` | `698.37` | 195,332.20 USD | `+1.62%` | `10X Cross` |
| `177` | `0x9071...5c0b` | `LONG` | 11,546,029.54 USD | `8,829.94` | `1370.53` | `1307.90` | `579.52` | -555,659.10 USD | `-4.81%` | `2X Cross` |
| `192` | `0xad59...ba81` | `SHORT` | 11,016,530.00 USD | `8,425.00` | `330.91` | `1307.90` | `2141.84` | -8,228,572.23 USD | `-74.69%` | `10X Cross` |
| `201` | `0x9ffd...ce40` | `LONG` | 10,808,569.98 USD | `8,272.92` | `1256.02` | `1307.90` | `579.10` | 417,643.78 USD | `+3.86%` | `5X Cross` |
| `203` | `0xdd53...2b13` | `SHORT` | 10,755,134.09 USD | `8,230.76` | `739.37` | `1307.90` | `8047.79` | -4,669,533.58 USD | `-43.42%` | `3X Cross` |
| `221` | `0xfc66...ca06` | `SHORT` | 10,113,903.93 USD | `7,741.22` | `1319.70` | `1307.90` | `5627.77` | 102,180.20 USD | `+1.01%` | `10X Cross` |
| `223` | `0x880a...311c` | `SHORT` | 10,090,148.41 USD | `7,707.11` | `1367.50` | `1307.90` | `2306.62` | 449,335.79 USD | `+4.45%` | `10X Cross` |
| `272` | `0x2b61...2f6c` | `LONG` | 8,911,724.40 USD | `6,807.00` | `1453.56` | `1307.90` | `620.61` | -982,626.82 USD | `-11.03%` | `10X Cross` |
| `288` | `0x2ae5...83e7` | `LONG` | 8,434,139.04 USD | `6,436.80` | `1391.82` | `1307.90` | `482.34` | -524,752.95 USD | `-6.22%` | `2X Cross` |
| `332` | `0x26b6...9a13` | `LONG` | 7,104,601.97 USD | `5,433.73` | `1282.23` | `1307.90` | `218.79` | 137,298.74 USD | `+1.93%` | `10X Cross` |
| `338` | `0xecb6...2b00` | `SHORT` | 7,000,017.96 USD | `5,357.84` | `1323.98` | `1307.90` | `6339.16` | 93,670.36 USD | `+1.34%` | `5X Cross` |
| `344` | `0x45d2...4029` | `SHORT` | 6,834,825.20 USD | `5,227.00` | `833.44` | `1307.90` | `8263.43` | -2,478,447.23 USD | `-36.26%` | `5X Cross` |
| `370` | `0xea00...a918` | `LONG` | 6,533,500.00 USD | `5,000.00` | `739.16` | `1307.90` | `0.000000` | 2,837,684.89 USD | `+43.43%` | `5X Cross` |
| `381` | `0xdd7a...8830` | `LONG` | 6,355,670.46 USD | `4,860.19` | `897.48` | `1307.90` | `784.73` | 1,993,766.79 USD | `+31.37%` | `10X Cross` |
| `388` | `0xf081...e39e` | `LONG` | 6,175,496.40 USD | `4,717.00` | `1195.70` | `1307.90` | `1200.11` | 535,372.35 USD | `+8.67%` | `10X Cross` |
| `438` | `0x4cae...7c34` | `LONG` | 5,242,508.11 USD | `4,004.36` | `999.34` | `1307.90` | `799.17` | 1,240,779.96 USD | `+23.67%` | `10X Cross` |
| `449` | `0xa61c...66b9` | `LONG` | 5,083,560.00 USD | `3,888.00` | `1148.34` | `1307.90` | `0.000000` | 618,817.86 USD | `+12.17%` | `10X Cross` |
| `471` | `0x9aa5...58af` | `SHORT` | 4,859,096.89 USD | `3,720.31` | `1205.51` | `1307.90` | `3396.73` | -374,210.09 USD | `-7.70%` | `10X Cross` |
| `475` | `0x0153...8052` | `SHORT` | 4,835,370.35 USD | `3,698.18` | `1307.82` | `1307.90` | `2504.70` | 1,200.40 USD | `+0.02%` | `1X Isolated` |
| `497` | `0x382b...3e39` | `LONG` | 4,565,877.81 USD | `3,494.74` | `1205.04` | `1307.90` | `0.000000` | 354,592.86 USD | `+7.77%` | `10X Cross` |
| `498` | `0xd4c1...3d1d` | `SHORT` | 4,530,720.91 USD | `3,467.30` | `1302.99` | `1307.90` | `2736.33` | -12,851.55 USD | `-0.28%` | `10X Cross` |
| `532` | `0xd21d...90f1` | `LONG` | 4,249,700.00 USD | `3,250.00` | `1253.64` | `1307.90` | `875.90` | 175,358.27 USD | `+4.13%` | `4X Isolated` |
| `552` | `0x27c9...d65d` | `SHORT` | 4,128,387.98 USD | `3,159.40` | `1253.94` | `1307.90` | `1782.76` | -166,690.78 USD | `-4.04%` | `10X Cross` |
| `555` | `0x1338...c48e` | `LONG` | 4,112,840.64 USD | `3,149.43` | `1018.52` | `1307.90` | `820.19` | 905,095.09 USD | `+22.01%` | `4X Isolated` |
| `560` | `0x456f...cdf1` | `LONG` | 4,093,458.88 USD | `3,134.11` | `1268.52` | `1307.90` | `493.53` | 117,769.24 USD | `+2.88%` | `10X Cross` |
| `570` | `0xdbe0...d6d5` | `LONG` | 4,034,121.27 USD | `3,085.37` | `422.97` | `1307.90` | `338.51` | 2,729,116.78 USD | `+67.65%` | `3X Isolated` |
| `593` | `0x9c06...0560` | `SHORT` | 3,906,771.66 USD | `2,989.80` | `786.00` | `1307.90` | `2400.42` | -1,556,776.66 USD | `-39.85%` | `10X Cross` |
| `644` | `0x2e30...4cb5` | `SHORT` | 3,562,048.40 USD | `2,724.32` | `1301.06` | `1307.90` | `2991.74` | -17,542.09 USD | `-0.49%` | `2X Cross` |
| `684` | `0xac48...3201` | `LONG` | 3,319,410.01 USD | `2,540.30` | `1393.86` | `1307.90` | `530.92` | -221,419.28 USD | `-6.67%` | `10X Cross` |
| `690` | `0xa183...0482` | `LONG` | 3,307,801.50 USD | `2,534.00` | `530.25` | `1307.90` | `444.43` | 1,964,138.78 USD | `+59.38%` | `5X Isolated` |
| `697` | `0x325e...9564` | `LONG` | 3,271,247.33 USD | `2,501.91` | `1306.24` | `1307.90` | `0.000000` | 3,153.42 USD | `+0.10%` | `10X Cross` |
| `700` | `0x0871...e927` | `LONG` | 3,265,250.00 USD | `2,500.00` | `1276.50` | `1307.90` | `0.000000` | 74,000.00 USD | `+2.27%` | `10X Cross` |
| `707` | `0x9b86...6e6e` | `LONG` | 3,226,241.48 USD | `2,467.30` | `637.58` | `1307.90` | `889.66` | 1,653,141.88 USD | `+51.24%` | `3X Cross` |
| `771` | `0xb2f7...af9f` | `SHORT` | 3,025,188.90 USD | `2,313.72` | `746.63` | `1307.90` | `4233.86` | -1,297,700.15 USD | `-42.90%` | `10X Cross` |
| `780` | `0x634f...6951` | `LONG` | 2,968,007.76 USD | `2,272.42` | `1281.94` | `1307.90` | `1250.04` | 54,907.30 USD | `+1.85%` | `10X Cross` |
| `794` | `0xf48f...10fe` | `LONG` | 2,900,675.67 USD | `2,218.49` | `1517.87` | `1307.90` | `919.88` | -466,711.15 USD | `-16.09%` | `3X Cross` |
| `829` | `0x5bc4...3b0c` | `SHORT` | 2,786,368.70 USD | `2,130.74` | `1089.65` | `1307.90` | `3594.28` | -464,611.12 USD | `-16.67%` | `5X Cross` |
| `841` | `0x8de4...b9aa` | `SHORT` | 2,732,270.38 USD | `2,091.29` | `1331.35` | `1307.90` | `1689.83` | 51,969.32 USD | `+1.90%` | `3X Cross` |
| `847` | `0x4fe2...ac59` | `SHORT` | 2,706,506.21 USD | `2,071.57` | `1478.56` | `1307.90` | `1824.42` | 356,440.01 USD | `+13.17%` | `10X Cross` |
| `866` | `0x668c...ea2e` | `SHORT` | 2,618,400.00 USD | `2,000.00` | `1406.98` | `1307.90` | `2702.66` | 195,563.99 USD | `+7.47%` | `10X Cross` |
| `884` | `0x4e23...20c3` | `LONG` | 2,556,448.88 USD | `1,954.92` | `1297.39` | `1307.90` | `0.000000` | 20,162.27 USD | `+0.79%` | `4X Cross` |
| `888` | `0x77ee...2902` | `SHORT` | 2,547,742.48 USD | `1,946.03` | `759.84` | `1307.90` | `5230.43` | -1,069,064.97 USD | `-41.96%` | `10X Cross` |
| `903` | `0x3e2f...b269` | `SHORT` | 2,513,498.37 USD | `1,925.51` | `1134.87` | `1307.90` | `2931.75` | -328,299.51 USD | `-13.06%` | `10X Cross` |
| `907` | `0xe097...d0fe` | `LONG` | 2,501,979.70 USD | `1,913.56` | `1261.17` | `1307.90` | `0.000000` | 88,653.54 USD | `+3.54%` | `10X Cross` |
| `918` | `0x4f12...618b` | `SHORT` | 2,477,489.82 USD | `1,896.28` | `1608.30` | `1307.90` | `2116.72` | 572,294.57 USD | `+23.10%` | `3X Cross` |
| `953` | `0x866d...d6e1` | `LONG` | 2,353,116.89 USD | `1,802.05` | `674.73` | `1307.90` | `116.77` | 1,137,215.58 USD | `+48.33%` | `10X Cross` |
| `989` | `0x2309...a2d9` | `LONG` | 2,286,158.26 USD | `1,750.37` | `1186.09` | `1307.90` | `807.18` | 210,064.15 USD | `+9.19%` | `8X Cross` |
| `1004` | `0x023a...2355` | `SHORT` | 2,226,014.70 USD | `1,703.80` | `1313.37` | `1307.90` | `5959.03` | 11,708.02 USD | `+0.53%` | `10X Cross` |
| `1008` | `0x2edd...8179` | `SHORT` | 2,224,829.10 USD | `1,701.46` | `1261.58` | `1307.90` | `3004.79` | -78,307.10 USD | `-3.52%` | `10X Cross` |
| `1024` | `0x58b2...11f3` | `LONG` | 2,172,814.02 USD | `1,663.08` | `1303.82` | `1307.90` | `0.000000` | 4,454.81 USD | `+0.21%` | `10X Cross` |
| `1038` | `0x3e47...aaf6` | `LONG` | 2,139,599.73 USD | `1,636.28` | `1279.54` | `1307.90` | `1039.82` | 45,907.64 USD | `+2.15%` | `10X Cross` |
| `1044` | `0xa271...a3f7` | `LONG` | 2,131,463.29 USD | `1,631.43` | `1190.60` | `1307.90` | `910.29` | 189,081.49 USD | `+8.87%` | `4X Cross` |
| `1057` | `0x7f75...9edf` | `LONG` | 2,098,272.73 USD | `1,605.78` | `1199.97` | `1307.90` | `973.97` | 171,380.83 USD | `+8.17%` | `10X Cross` |
| `1061` | `0x265e...7f70` | `LONG` | 2,092,673.31 USD | `1,601.74` | `1388.09` | `1307.90` | `0.000000` | -130,691.70 USD | `-6.25%` | `3X Cross` |
| `1063` | `0x6646...6de5` | `SHORT` | 2,092,000.00 USD | `1,600.00` | `660.64` | `1307.90` | `4720.93` | -1,034,975.03 USD | `-49.47%` | `10X Cross` |
| `1079` | `0xdf57...93f5` | `LONG` | 2,065,852.15 USD | `1,579.76` | `1218.38` | `1307.90` | `780.13` | 141,096.17 USD | `+6.83%` | `3X Isolated` |
| `1091` | `0xab59...59b5` | `LONG` | 2,045,090.58 USD | `1,565.32` | `1342.15` | `1307.90` | `801.21` | -55,804.64 USD | `-2.73%` | `10X Cross` |
| `1093` | `0xfe7c...b7ae` | `SHORT` | 2,041,705.68 USD | `1,562.49` | `1350.62` | `1307.90` | `6722.52` | 68,623.37 USD | `+3.36%` | `10X Cross` |
| `1157` | `0xcf67...eb24` | `LONG` | 1,959,750.00 USD | `1,500.00` | `887.05` | `1307.90` | `564.67` | 629,178.63 USD | `+32.11%` | `10X Cross` |
| `1180` | `0x039c...0ebd` | `SHORT` | 1,935,740.68 USD | `1,480.49` | `1238.67` | `1307.90` | `3175.75` | -101,909.35 USD | `-5.26%` | `10X Cross` |
| `1245` | `0xdf83...3cff` | `SHORT` | 1,836,581.58 USD | `1,406.48` | `1250.64` | `1307.90` | `1814.16` | -77,584.74 USD | `-4.22%` | `10X Cross` |
| `1248` | `0x2ab7...c2f8` | `LONG` | 1,831,166.82 USD | `1,400.51` | `813.26` | `1307.90` | `799.82` | 692,185.14 USD | `+37.80%` | `3X Cross` |
| `1254` | `0xfc27...9d9d` | `SHORT` | 1,817,593.57 USD | `1,390.98` | `1317.47` | `1307.90` | `11955.59` | 14,982.91 USD | `+0.82%` | `10X Cross` |
| `1267` | `0x11be...8b1d` | `LONG` | 1,796,970.60 USD | `1,375.83` | `1206.55` | `1307.90` | `1134.41` | 136,962.64 USD | `+7.62%` | `10X Isolated` |
| `1278` | `0x71d0...8c26` | `SHORT` | 1,778,039.76 USD | `1,360.71` | `1358.13` | `1307.90` | `6764.17` | 69,979.45 USD | `+3.94%` | `10X Cross` |
| `1316` | `0xef96...9383` | `SHORT` | 1,709,973.33 USD | `1,308.82` | `1249.96` | `1307.90` | `4284.26` | -74,006.91 USD | `-4.33%` | `10X Cross` |
| `1368` | `0xe065...0f85` | `SHORT` | 1,649,599.97 USD | `1,262.61` | `1087.02` | `1307.90` | `1771.17` | -277,123.84 USD | `-16.80%` | `10X Cross` |
| `1393` | `0x7277...0b98` | `SHORT` | 1,614,957.19 USD | `1,234.96` | `1298.48` | `1307.90` | `2382.23` | -11,387.77 USD | `-0.71%` | `10X Cross` |
| `1445` | `0x5975...9abd` | `LONG` | 1,567,319.16 USD | `1,200.00` | `1179.54` | `1307.90` | `407.83` | 151,876.37 USD | `+9.69%` | `5X Cross` |
| `1489` | `0x69cc...14fd` | `SHORT` | 1,518,710.47 USD | `1,161.36` | `675.33` | `1307.90` | `7944.31` | -734,404.94 USD | `-48.36%` | `10X Cross` |
| `1503` | `0x3fc5...c0c1` | `SHORT` | 1,499,976.68 USD | `1,148.44` | `1264.34` | `1307.90` | `3178.07` | -47,962.90 USD | `-3.20%` | `10X Cross` |
| `1525` | `0xe35c...a1d3` | `LONG` | 1,471,264.12 USD | `1,127.06` | `1318.20` | `1307.90` | `694.33` | -14,431.23 USD | `-0.98%` | `2X Isolated` |
| `1527` | `0x5f94...4b96` | `LONG` | 1,458,327.05 USD | `1,115.27` | `538.00` | `1307.90` | `0.000000` | 858,309.42 USD | `+58.86%` | `10X Cross` |
| `1552` | `0x71df...a23d` | `SHORT` | 1,434,134.02 USD | `1,098.28` | `513.50` | `1307.90` | `2549.25` | -870,163.83 USD | `-60.68%` | `2X Cross` |
| `1575` | `0xbfc7...80b4` | `SHORT` | 1,407,390.00 USD | `1,075.00` | `558.03` | `1307.90` | `5609.88` | -807,511.27 USD | `-57.38%` | `10X Cross` |
| `1619` | `0x51f6...2b39` | `SHORT` | 1,362,934.31 USD | `1,044.10` | `1302.75` | `1307.90` | `2690.08` | -2,736.16 USD | `-0.20%` | `10X Cross` |
| `1652` | `0x123d...3bff` | `SHORT` | 1,316,744.01 USD | `1,008.15` | `489.25` | `1307.90` | `4223.19` | -823,509.94 USD | `-62.54%` | `10X Cross` |
| `1660` | `0x0748...d4b2` | `LONG` | 1,307,600.00 USD | `1,000.00` | `1334.09` | `1307.90` | `0.000000` | -26,488.30 USD | `-2.03%` | `7X Cross` |
| `1661` | `0xb5ff...d912` | `LONG` | 1,307,500.00 USD | `1,000.00` | `1141.93` | `1307.90` | `400.45` | 165,569.70 USD | `+12.66%` | `2X Cross` |
| `1665` | `0xe282...df29` | `LONG` | 1,305,400.00 USD | `1,000.00` | `420.99` | `1307.90` | `125.45` | 884,413.14 USD | `+67.75%` | `10X Cross` |
| `1666` | `0x266b...efcb` | `LONG` | 1,305,367.60 USD | `1,000.00` | `826.11` | `1307.90` | `186.03` | 479,254.67 USD | `+36.71%` | `10X Cross` |
| `1687` | `0x17f0...094f` | `LONG` | 1,287,169.11 USD | `984.30` | `1287.23` | `1307.90` | `536.76` | 20,148.95 USD | `+1.57%` | `5X Cross` |
| `1756` | `0x757d...94ba` | `LONG` | 1,209,622.50 USD | `925.00` | `1558.31` | `1307.90` | `0.000000` | -231,818.08 USD | `-19.16%` | `10X Cross` |
| `1798` | `0x2847...d47b` | `LONG` | 1,175,518.87 USD | `899.54` | `1239.05` | `1307.90` | `0.000000` | 60,946.42 USD | `+5.18%` | `5X Cross` |
| `1824` | `0xf096...7553` | `SHORT` | 1,151,117.96 USD | `881.07` | `1240.34` | `1307.90` | `3582.64` | -58,287.87 USD | `-5.06%` | `10X Cross` |
| `1825` | `0xdf95...7d72` | `SHORT` | 1,150,810.69 USD | `880.70` | `1073.97` | `1307.90` | `42300.70` | -204,967.46 USD | `-17.81%` | `10X Cross` |
| `1834` | `0xcf0a...856f` | `LONG` | 1,138,331.71 USD | `871.15` | `1292.19` | `1307.90` | `938.47` | 12,636.86 USD | `+1.11%` | `4X Cross` |
| `1858` | `0x7a76...b16d` | `LONG` | 1,121,651.95 USD | `857.86` | `1358.50` | `1307.90` | `1208.26` | -43,751.02 USD | `-3.90%` | `10X Cross` |
| `1905` | `0x601c...4f54` | `SHORT` | 1,078,094.03 USD | `824.42` | `615.11` | `1307.90` | `2991.85` | -570,981.28 USD | `-52.96%` | `5X Cross` |
| `1916` | `0xae55...2236` | `LONG` | 1,068,923.77 USD | `817.47` | `1467.80` | `1307.90` | `0.000000` | -130,957.45 USD | `-12.25%` | `10X Cross` |
| `1927` | `0x71b1...79c8` | `LONG` | 1,062,369.90 USD | `812.52` | `1231.55` | `1307.90` | `720.78` | 61,714.45 USD | `+5.81%` | `10X Cross` |
| `1943` | `0x0f02...5384` | `LONG` | 1,047,180.01 USD | `800.78` | `1290.36` | `1307.90` | `295.38` | 13,885.94 USD | `+1.33%` | `3X Cross` |
| `1946` | `0x9b0f...db40` | `LONG` | 1,046,000.00 USD | `800.00` | `1268.86` | `1307.90` | `778.45` | 30,910.24 USD | `+2.96%` | `10X Cross` |
| `1959` | `0xabdb...84ac` | `LONG` | 1,036,638.51 USD | `793.69` | `711.79` | `1307.90` | `664.33` | 471,698.15 USD | `+45.50%` | `3X Cross` |
| `1965` | `0xfdf8...e381` | `LONG` | 1,033,017.08 USD | `790.01` | `1337.72` | `1307.90` | `551.23` | -23,792.61 USD | `-2.30%` | `10X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `1297.10` | 194.56 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Long: 0.19K USD at 1297.1000 USD [API] | `2026-10-27 15:46:39` |
| `ANNOUNCEMENT` | `INFO` | `1326.30` | 13.26 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Long: 0.01K USD at 1326.3000 USD [API] | `2026-10-27 23:06:56` |
| `ANNOUNCEMENT` | `INFO` | `1326.50` | 11,341.58 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Long: 11.34K USD at 1326.5000 USD [API] | `2026-10-27 23:06:49` |
| `ANNOUNCEMENT` | `INFO` | `1268.00` | 95,100.00 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Long: 95.10K USD at 1268.0000 USD [API] | `2026-10-22 08:34:05` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`1404.15` (Vol: 3,000,000.00 USD, Dist: `+7.59%`) | Long MP=`1287.60` (Vol: 2,300,000.00 USD, Dist: `--1.34%`)
  * 48H Horizon: Short MP=`1404.15` (Vol: 3,000,000.00 USD, Dist: `+7.59%`) | Long MP=`1287.60` (Vol: 2,300,000.00 USD, Dist: `--1.34%`)
  * 3D Horizon: Short MP=`1404.42` (Vol: 3,000,000.00 USD, Dist: `+7.61%`) | Long MP=`1228.81` (Vol: 2,600,000.00 USD, Dist: `--5.85%`)
  * 7D Horizon: Short MP=`1404.10` (Vol: 3,000,000.00 USD, Dist: `+7.58%`) | Long MP=`1200.46` (Vol: 3,000,000.00 USD, Dist: `--8.02%`)
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
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `0 USD` | Total OI Tokens: `-`
  * 1h OI Change: `0.00%` | 4h OI Change: `0.00%` | 24h OI Change: `0.00%`
  * Exchange Breakdown: Binance=`-` | Bybit=`-` | OKX=`-` | Hyperliquid=`-`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `52.23K` | Last 24h: `33.19K` | Last 3d: `283.86K` | Last 7d: `777.60K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0032%` | **USDT OKX** | `0.0100%` |
| **USDT Bybit** | `0.0100%` | **USDT KuCoin** | `0.0098%` |
| **USDT MEXC** | `0.0032%` | **USDT BingX** | `0.0026%` |
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
| `0:00 UTC` | `1324.05` | `1326.61` | `1324.05` | `1336.05` | `1320.15` | 35,175,848.19 USD | 15,805,961.43 USD | 19,369,886.76 USD | -3,563,925.33 USD | `-10.13%` | `1B / 10S` |
| `5:00 UTC` | `1321.35` | `1325.74` | `1321.35` | `1333.35` | `1318.35` | 26,289,288.34 USD | 11,537,630.34 USD | 14,751,657.99 USD | -3,214,027.65 USD | `-12.23%` | `3B / 5S` |
| `0:00 UTC` | `1315.95` | `1314.40` | `1315.95` | `1321.95` | `1307.85` | 50,919,152.62 USD | 22,517,005.07 USD | 28,402,147.55 USD | -5,885,142.49 USD | `-11.56%` | `2B / 5S` |
| `5:00 UTC` | `1315.95` | `1319.00` | `1315.95` | `1325.85` | `1312.05` | 22,246,351.59 USD | 13,151,982.06 USD | 9,094,369.53 USD | 4,057,612.52 USD | `+18.24%` | `9B / 1S` |
| `0:00 UTC` | `1320.75` | `1319.74` | `1320.75` | `1325.25` | `1315.95` | 11,564,611.33 USD | 5,754,638.99 USD | 5,809,972.34 USD | -55,333.35 USD | `-0.48%` | `1B / 2S` |
| `5:00 UTC` | `1322.85` | `1320.89` | `1322.85` | `1324.95` | `1316.85` | 7,868,027.33 USD | 4,223,932.72 USD | 3,644,094.61 USD | 579,838.11 USD | `+7.37%` | `3B / 0S` |
| `0:00 UTC` | `1324.95` | `1324.41` | `1324.95` | `1327.05` | `1319.85` | 12,000,472.36 USD | 6,714,467.49 USD | 5,286,004.87 USD | 1,428,462.62 USD | `+11.90%` | `2B / 1S` |
| `5:00 UTC` | `1325.25` | `1325.38` | `1325.25` | `1330.65` | `1320.75` | 11,021,893.68 USD | 5,577,839.59 USD | 5,444,054.10 USD | 133,785.49 USD | `+1.21%` | `3B / 1S` |
| `0:00 UTC` | `1294.05` | `1302.04` | `1294.05` | `1328.55` | `1286.25` | 68,949,402.59 USD | 35,232,633.05 USD | 33,716,769.55 USD | 1,515,863.50 USD | `+2.20%` | `6B / 24S` |
| `5:00 UTC` | `1308.15` | `1308.17` | `1308.15` | `1312.05` | `1303.65` | 8,794,264.52 USD | 4,981,138.55 USD | 3,813,125.97 USD | 1,168,012.58 USD | `+13.28%` | `5B / 2S` |

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
| `5m` | -91,860.00 USD | 1,150,000.00 USD | **`ACCUMULATION`** |
| `15m` | 486,720.00 USD | 5,400,000.00 USD | **`ACCUMULATION`** |
| `30m` | -2,550,000.00 USD | -9,500,000.00 USD | **`DISTRIBUTION`** |
| `1h` | -2,380,000.00 USD | -3,410,000.00 USD | **`DISTRIBUTION`** |
| `2h` | -2,280,000.00 USD | -4,340,000.00 USD | **`DISTRIBUTION`** |
| `4h` | 2,610,000.00 USD | -20,090,000.00 USD | **`DISTRIBUTION`** |
| `6h` | 24,020,000.00 USD | 78,860,000.00 USD | **`ACCUMULATION`** |
| `8h` | 27,470,000.00 USD | 88,930,000.00 USD | **`ACCUMULATION`** |
| `12h` | 25,320,000.00 USD | 103,950,000.00 USD | **`ACCUMULATION`** |
| `24h` | 11,130,000.00 USD | 57,610,000.00 USD | **`ACCUMULATION`** |
| `1w` | 46,890,000.00 USD | 253,270,000.00 USD | **`ACCUMULATION`** |
| `30d` | 67,780,000.00 USD | -507,800,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-91.86K` | 15m=`+486.72K` | 1h=`-2.38M` | 24h=`+11.13M`
* Futures Capital Netflows: 5m=`+1.15M` | 15m=`+5.40M` | 1h=`-3.41M` | 24h=`+57.61M`
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
  * `2026-10-30 01:36:09 IST`: [sec.gov] - (Sentiment: `Neutral`)
  * `2026-10-30 00:58:09 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 01:50:09 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 01:50:09 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 01:49:09 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 01:49:09 IST`: [@DeItaone] - (Sentiment: `Neutral`)
  * `2026-10-30 01:49:09 IST`: [@mb_ghalibaf] - (Sentiment: `Neutral`)
  * `2026-10-30 01:49:09 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-30 01:49:09 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-29 22:51:09 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:51:09 IST`: [fxstreet.com] - (Sentiment: `Neutral`)
  * `2026-10-29 21:51:09 IST`: [ForexFactory] - (Sentiment: `Neutral`)
  * `2026-10-29 21:51:09 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-29 21:51:09 IST`: [youtube.com/bankofcanadaofficial] - (Sentiment: `Neutral`)
  * `2026-10-29 20:51:09 IST`: [notayesmanseconomics.wordpress.com] - (Sentiment: `Neutral`)


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
  * Execution Entry: `1230.55` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `1209.33` (Risk Distance: `21.22` pts)
  * +2.5R Take Profit: `1283.61`
  * Mathematical Lot Sizing: **`0.47 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `1309.36` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `1330.58` (Risk Distance: `21.22` pts)
  * +2.5R Take Profit: `1256.30`
  * Mathematical Lot Sizing: **`0.47 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`1319.90`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
