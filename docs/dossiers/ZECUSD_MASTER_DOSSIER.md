# 🏛️ SOVEREIGN CANDIDATE DOSSIER: ZECUSD
**Canonical Key**: `ZECUSD` | **Broker Instrument**: `ZECUSD.p` | **Asset Class**: `Crypto Altcoin`
**Timestamp**: `2026-10-30 01:29:57 IST` (`2026-10-29 19:59:57 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `1324.42` | **Live Ask Quote**: `1325.65` | **Mid Price**: `1325.04`
- **Spread Points**: `123.00` | **Spread BPS**: `9.28 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `1325.04` | VWAP Z-Score: `+0.00` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `3.31` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `50.00` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `1334.31` | Lower -3.00σ Band: `1315.76`
  * Upper +2.51σ Band: `1332.32` | Lower -2.51σ Band: `1317.75`
  * Upper +2.01σ Band: `1330.60` | Lower -2.01σ Band: `1319.47`
  * Upper +2.00σ Band: `1330.34` | Lower -2.00σ Band: `1319.73`
  * Upper +1.28σ Band: `1328.75` | Lower -1.28σ Band: `1321.32`
  * Upper +1.00σ Band: `1327.69` | Lower -1.00σ Band: `1322.38`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`1325.04` | EMA-20=`1325.04` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`1325.04` (Slope: `+0.0000`) | EMA-100=`1325.04`
  * Institutional Anchors: EMA-144=`1325.04` | EMA-200=`1325.04` (Slope: `+0.0000`) | EMA-233=`1325.04`
- **Range Boundaries**: 24H High=`1338.29` | 24H Low=`1311.78` | Weekly High=`1351.54` | Weekly Low=`1298.53`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `1309.36` (Distance: `+1.22%`)
  * Point of Control (POC) = `1247.20` (Distance: `+6.26%`)
  * Value Area Low (VAL) = `1230.55` (Distance: `+7.70%`)
  * Auction Positioning: `ABOVE_VALUE (Imbalance)` | Session Bias: **`BULLISH (Above Pivot)`** | Market Regime: `RANGE_EXPANSION`
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
  * Golden Pocket Zone (0.618 - 0.650): `1319.73` - `1330.34`
  * Optimal Trade Entry (OTE 0.705): `1327.69`
  * Structural Invalidation Anchor (0.786): `1335.64`

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
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 01:23:08 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `16` | `0xb83d...6e36` | `SHORT` | 69,745,454.53 USD | `52,582.52` | `1336.45` | `1325.90` | `3706.30` | 528,460.37 USD | `+0.76%` | `3X Cross` |
| `23` | `0x5b5d...c060` | `SHORT` | 53,984,447.05 USD | `40,727.61` | `1478.36` | `1325.90` | `4990.24` | 6,225,817.14 USD | `+11.53%` | `3X Cross` |
| `41` | `0x7fda...17d1` | `SHORT` | 29,724,352.99 USD | `22,423.32` | `1261.42` | `1325.90` | `2817.24` | -1,439,142.36 USD | `-4.84%` | `5X Cross` |
| `77` | `0x60b0...991e` | `LONG` | 22,258,325.11 USD | `16,779.74` | `1179.65` | `1325.90` | `890.51` | 2,464,078.10 USD | `+11.07%` | `10X Cross` |
| `82` | `0xbf73...5d58` | `LONG` | 21,206,400.00 USD | `16,000.00` | `1214.30` | `1325.90` | `728.80` | 1,777,567.75 USD | `+8.38%` | `10X Cross` |
| `132` | `0xc36a...105b` | `LONG` | 15,258,742.99 USD | `11,510.82` | `1215.14` | `1325.90` | `932.85` | 1,271,461.96 USD | `+8.33%` | `10X Cross` |
| `169` | `0x8742...8427` | `LONG` | 12,196,714.52 USD | `9,201.21` | `1286.37` | `1325.90` | `698.35` | 360,544.53 USD | `+2.96%` | `10X Cross` |
| `176` | `0x9071...5c0b` | `LONG` | 11,704,575.53 USD | `8,829.94` | `1370.53` | `1325.90` | `579.50` | -397,113.12 USD | `-3.39%` | `2X Cross` |
| `190` | `0xad59...ba81` | `SHORT` | 11,174,920.00 USD | `8,425.00` | `330.91` | `1325.90` | `2140.59` | -8,386,962.23 USD | `-75.05%` | `10X Cross` |
| `199` | `0xdd53...2b13` | `SHORT` | 10,912,022.30 USD | `8,231.14` | `739.37` | `1325.90` | `7878.09` | -4,826,140.82 USD | `-44.23%` | `3X Cross` |
| `201` | `0x9ffd...ce40` | `LONG` | 10,861,729.51 USD | `8,188.42` | `1254.38` | `1325.90` | `568.55` | 590,343.33 USD | `+5.44%` | `5X Cross` |
| `215` | `0xfc66...ca06` | `SHORT` | 10,290,034.49 USD | `7,763.72` | `1319.73` | `1325.90` | `5601.92` | -44,017.64 USD | `-0.43%` | `10X Cross` |
| `223` | `0x880a...311c` | `SHORT` | 10,215,003.59 USD | `7,707.11` | `1367.50` | `1325.90` | `2308.83` | 324,480.61 USD | `+3.18%` | `10X Cross` |
| `267` | `0x2b61...2f6c` | `LONG` | 9,021,997.80 USD | `6,807.00` | `1453.56` | `1325.90` | `635.86` | -872,353.42 USD | `-9.67%` | `10X Cross` |
| `284` | `0x2ae5...83e7` | `LONG` | 8,532,335.64 USD | `6,436.80` | `1391.82` | `1325.90` | `385.57` | -426,556.35 USD | `-5.00%` | `2X Cross` |
| `330` | `0x26b6...9a13` | `LONG` | 7,202,952.49 USD | `5,433.73` | `1282.23` | `1325.90` | `208.22` | 235,649.25 USD | `+3.27%` | `10X Cross` |
| `331` | `0xecb6...2b00` | `SHORT` | 7,172,145.54 USD | `5,410.49` | `1324.05` | `1325.90` | `6157.93` | -8,364.02 USD | `-0.12%` | `5X Cross` |
| `343` | `0x45d2...4029` | `SHORT` | 6,928,678.60 USD | `5,227.00` | `833.44` | `1325.90` | `8047.19` | -2,572,300.63 USD | `-37.13%` | `5X Cross` |
| `361` | `0xea00...a918` | `LONG` | 6,633,000.00 USD | `5,000.00` | `739.16` | `1325.90` | `0.000000` | 2,937,184.89 USD | `+44.28%` | `5X Cross` |
| `377` | `0xdd7a...8830` | `LONG` | 6,446,556.02 USD | `4,860.19` | `897.48` | `1325.90` | `783.97` | 2,084,652.34 USD | `+32.34%` | `10X Cross` |
| `383` | `0xf081...e39e` | `LONG` | 6,251,911.80 USD | `4,717.00` | `1195.70` | `1325.90` | `1200.09` | 611,787.76 USD | `+9.79%` | `10X Cross` |
| `434` | `0x382b...3e39` | `LONG` | 5,331,335.59 USD | `4,021.98` | `1204.44` | `1325.90` | `0.000000` | 487,093.58 USD | `+9.14%` | `10X Cross` |
| `436` | `0x4cae...7c34` | `LONG` | 5,307,378.74 USD | `4,004.36` | `999.34` | `1325.90` | `769.13` | 1,305,650.59 USD | `+24.60%` | `10X Cross` |
| `447` | `0xa61c...66b9` | `LONG` | 5,157,043.20 USD | `3,888.00` | `1148.34` | `1325.90` | `0.000000` | 692,301.06 USD | `+13.42%` | `10X Cross` |
| `470` | `0x9aa5...58af` | `SHORT` | 4,931,456.92 USD | `3,720.31` | `1205.51` | `1325.90` | `3332.72` | -446,570.12 USD | `-9.06%` | `10X Cross` |
| `474` | `0x0153...8052` | `SHORT` | 4,902,307.41 USD | `3,698.18` | `1307.82` | `1325.90` | `2504.69` | -65,736.66 USD | `-1.34%` | `1X Isolated` |
| `501` | `0xd4c1...3d1d` | `SHORT` | 4,588,774.71 USD | `3,459.31` | `1302.98` | `1325.90` | `2690.08` | -81,347.68 USD | `-1.77%` | `10X Cross` |
| `528` | `0xd21d...90f1` | `LONG` | 4,310,800.00 USD | `3,250.00` | `1253.64` | `1325.90` | `875.88` | 236,458.27 USD | `+5.49%` | `4X Isolated` |
| `547` | `0x1338...c48e` | `LONG` | 4,174,254.52 USD | `3,149.43` | `1018.52` | `1325.90` | `820.17` | 966,508.98 USD | `+23.15%` | `4X Isolated` |
| `553` | `0x456f...cdf1` | `LONG` | 4,157,710.33 USD | `3,134.11` | `1268.52` | `1325.90` | `493.29` | 182,020.69 USD | `+4.38%` | `10X Cross` |
| `556` | `0x27c9...d65d` | `SHORT` | 4,141,413.01 USD | `3,124.18` | `1253.28` | `1325.90` | `1800.49` | -225,954.35 USD | `-5.46%` | `10X Cross` |
| `563` | `0xdbe0...d6d5` | `LONG` | 4,089,966.47 USD | `3,085.37` | `422.97` | `1325.90` | `338.49` | 2,784,961.98 USD | `+68.09%` | `3X Isolated` |
| `587` | `0x9c06...0560` | `SHORT` | 3,962,680.92 USD | `2,989.80` | `786.00` | `1325.90` | `2372.87` | -1,612,685.92 USD | `-40.70%` | `10X Cross` |
| `646` | `0x2e30...4cb5` | `SHORT` | 3,585,827.54 USD | `2,705.06` | `1301.01` | `1325.90` | `2990.72` | -66,530.68 USD | `-1.86%` | `2X Cross` |
| `688` | `0xac48...3201` | `LONG` | 3,369,961.98 USD | `2,540.30` | `1393.86` | `1325.90` | `535.74` | -170,867.31 USD | `-5.07%` | `10X Cross` |
| `691` | `0xa183...0482` | `LONG` | 3,358,957.64 USD | `2,534.00` | `530.25` | `1325.90` | `444.42` | 2,015,294.92 USD | `+60.00%` | `5X Isolated` |
| `699` | `0x325e...9564` | `LONG` | 3,318,533.42 USD | `2,501.91` | `1306.24` | `1325.90` | `0.000000` | 50,439.52 USD | `+1.52%` | `10X Cross` |
| `701` | `0x0871...e927` | `LONG` | 3,313,500.00 USD | `2,500.00` | `1276.50` | `1325.90` | `0.000000` | 122,250.00 USD | `+3.69%` | `10X Cross` |
| `709` | `0x9b86...6e6e` | `LONG` | 3,272,626.72 USD | `2,467.30` | `637.58` | `1325.90` | `889.64` | 1,699,527.12 USD | `+51.93%` | `3X Cross` |
| `770` | `0xb2f7...af9f` | `SHORT` | 3,068,918.21 USD | `2,313.72` | `746.63` | `1325.90` | `4175.84` | -1,341,429.46 USD | `-43.71%` | `10X Cross` |
| `784` | `0x634f...6951` | `LONG` | 3,012,092.71 USD | `2,272.42` | `1281.94` | `1325.90` | `1250.03` | 98,992.25 USD | `+3.29%` | `10X Cross` |
| `798` | `0xf48f...10fe` | `LONG` | 2,942,605.14 USD | `2,218.49` | `1517.87` | `1325.90` | `892.76` | -424,781.69 USD | `-14.44%` | `3X Cross` |
| `828` | `0x5bc4...3b0c` | `SHORT` | 2,824,414.13 USD | `2,130.74` | `1089.65` | `1325.90` | `3568.08` | -502,656.55 USD | `-17.80%` | `5X Cross` |
| `840` | `0x8de4...b9aa` | `SHORT` | 2,772,004.90 USD | `2,091.29` | `1331.35` | `1325.90` | `1689.81` | 12,234.81 USD | `+0.44%` | `3X Cross` |
| `844` | `0x4fe2...ac59` | `SHORT` | 2,747,609.05 USD | `2,071.57` | `1478.56` | `1325.90` | `1817.37` | 315,337.16 USD | `+11.48%` | `10X Cross` |
| `862` | `0x668c...ea2e` | `SHORT` | 2,651,000.00 USD | `2,000.00` | `1406.98` | `1325.90` | `2702.47` | 162,963.99 USD | `+6.15%` | `10X Cross` |
| `886` | `0x77ee...2902` | `SHORT` | 2,579,268.16 USD | `1,946.03` | `759.84` | `1325.90` | `5161.85` | -1,100,590.66 USD | `-42.67%` | `10X Cross` |
| `897` | `0x3e2f...b269` | `SHORT` | 2,552,648.61 USD | `1,925.51` | `1134.87` | `1325.90` | `2931.74` | -367,449.75 USD | `-14.39%` | `10X Cross` |
| `904` | `0xe097...d0fe` | `LONG` | 2,536,997.85 USD | `1,913.56` | `1261.17` | `1325.90` | `0.000000` | 123,671.68 USD | `+4.87%` | `10X Cross` |
| `914` | `0x4f12...618b` | `SHORT` | 2,513,519.14 USD | `1,896.28` | `1608.30` | `1325.90` | `2116.70` | 536,265.25 USD | `+21.34%` | `3X Cross` |
| `955` | `0x866d...d6e1` | `LONG` | 2,388,437.07 USD | `1,802.05` | `674.73` | `1325.90` | `86.55` | 1,172,535.76 USD | `+49.09%` | `10X Cross` |
| `991` | `0x2309...a2d9` | `LONG` | 2,320,202.95 USD | `1,750.37` | `1186.09` | `1325.90` | `805.47` | 244,108.84 USD | `+10.52%` | `8X Cross` |
| `1008` | `0x023a...2355` | `SHORT` | 2,260,426.38 USD | `1,705.21` | `1313.37` | `1325.90` | `6097.63` | -20,859.14 USD | `-0.92%` | `10X Cross` |
| `1010` | `0x2edd...8179` | `SHORT` | 2,256,816.54 USD | `1,701.46` | `1261.58` | `1325.90` | `2982.54` | -110,294.55 USD | `-4.89%` | `10X Cross` |
| `1039` | `0x3e47...aaf6` | `LONG` | 2,170,361.79 USD | `1,636.28` | `1279.54` | `1325.90` | `1038.18` | 76,669.71 USD | `+3.53%` | `10X Cross` |
| `1040` | `0xa271...a3f7` | `LONG` | 2,163,833.15 USD | `1,631.43` | `1190.60` | `1325.90` | `910.27` | 221,451.35 USD | `+10.23%` | `4X Cross` |
| `1054` | `0x7f75...9edf` | `LONG` | 2,128,300.81 USD | `1,605.78` | `1199.97` | `1325.90` | `973.82` | 201,408.92 USD | `+9.46%` | `10X Cross` |
| `1058` | `0x265e...7f70` | `LONG` | 2,123,106.37 USD | `1,601.74` | `1388.09` | `1325.90` | `0.000000` | -100,258.64 USD | `-4.72%` | `3X Cross` |
| `1059` | `0x6646...6de5` | `SHORT` | 2,121,280.00 USD | `1,600.00` | `660.64` | `1325.90` | `4850.80` | -1,064,255.03 USD | `-50.17%` | `10X Cross` |
| `1075` | `0xdf57...93f5` | `LONG` | 2,094,287.83 USD | `1,579.76` | `1218.38` | `1325.90` | `780.12` | 169,531.85 USD | `+8.09%` | `3X Isolated` |
| `1090` | `0xab59...59b5` | `LONG` | 2,076,240.45 USD | `1,565.32` | `1342.15` | `1325.90` | `792.27` | -24,654.77 USD | `-1.19%` | `10X Cross` |
| `1092` | `0xfe7c...b7ae` | `SHORT` | 2,072,799.23 USD | `1,562.49` | `1350.62` | `1325.90` | `6503.57` | 37,529.81 USD | `+1.81%` | `10X Cross` |
| `1097` | `0x71d0...8c26` | `SHORT` | 2,060,882.53 USD | `1,553.81` | `1358.60` | `1325.90` | `6120.64` | 50,121.25 USD | `+2.43%` | `10X Cross` |
| `1149` | `0xcf67...eb24` | `LONG` | 1,989,750.00 USD | `1,500.00` | `887.05` | `1325.90` | `551.85` | 659,178.63 USD | `+33.13%` | `10X Cross` |
| `1170` | `0x039c...0ebd` | `SHORT` | 1,963,721.94 USD | `1,480.49` | `1238.67` | `1325.90` | `3183.94` | -129,890.62 USD | `-6.61%` | `10X Cross` |
| `1242` | `0xfc27...9d9d` | `SHORT` | 1,862,047.58 USD | `1,404.73` | `1317.51` | `1325.90` | `11291.65` | -11,308.77 USD | `-0.61%` | `10X Cross` |
| `1246` | `0x2ab7...c2f8` | `LONG` | 1,856,516.06 USD | `1,400.51` | `813.26` | `1325.90` | `797.99` | 717,534.37 USD | `+38.65%` | `3X Cross` |
| `1263` | `0x11be...8b1d` | `LONG` | 1,825,176.08 USD | `1,375.83` | `1206.55` | `1325.90` | `1134.40` | 165,168.12 USD | `+9.05%` | `10X Isolated` |
| `1299` | `0xdf83...3cff` | `SHORT` | 1,758,076.88 USD | `1,325.45` | `1247.44` | `1325.90` | `1850.73` | -104,656.13 USD | `-5.95%` | `10X Cross` |
| `1314` | `0xef96...9383` | `SHORT` | 1,736,149.73 USD | `1,308.82` | `1249.96` | `1325.90` | `4255.24` | -100,183.31 USD | `-5.77%` | `10X Cross` |
| `1360` | `0xe065...0f85` | `SHORT` | 1,674,852.17 USD | `1,262.61` | `1087.02` | `1325.90` | `1758.43` | -302,376.04 USD | `-18.05%` | `10X Cross` |
| `1387` | `0x7277...0b98` | `SHORT` | 1,637,186.47 USD | `1,234.96` | `1298.48` | `1325.90` | `2363.46` | -33,617.05 USD | `-2.05%` | `10X Cross` |
| `1430` | `0x5975...9abd` | `LONG` | 1,591,920.00 USD | `1,200.00` | `1179.54` | `1325.90` | `381.52` | 176,477.21 USD | `+11.09%` | `5X Cross` |
| `1476` | `0x69cc...14fd` | `SHORT` | 1,539,963.36 USD | `1,161.36` | `675.33` | `1325.90` | `7906.34` | -755,657.83 USD | `-49.07%` | `10X Cross` |
| `1478` | `0x7a76...b16d` | `LONG` | 1,537,655.73 USD | `1,159.27` | `1358.50` | `1325.90` | `1237.85` | -37,212.78 USD | `-2.42%` | `10X Cross` |
| `1488` | `0x3fc5...c0c1` | `SHORT` | 1,523,520.50 USD | `1,148.44` | `1264.34` | `1325.90` | `3095.16` | -71,506.73 USD | `-4.69%` | `10X Cross` |
| `1510` | `0xe35c...a1d3` | `LONG` | 1,494,932.38 USD | `1,127.06` | `1318.20` | `1325.90` | `694.32` | 9,237.03 USD | `+0.62%` | `2X Isolated` |
| `1517` | `0x5f94...4b96` | `LONG` | 1,479,294.13 USD | `1,115.27` | `538.00` | `1325.90` | `0.000000` | 879,276.49 USD | `+59.44%` | `10X Cross` |
| `1533` | `0x71df...a23d` | `SHORT` | 1,455,660.31 USD | `1,098.28` | `513.50` | `1325.90` | `2546.54` | -891,690.12 USD | `-61.26%` | `2X Cross` |
| `1564` | `0xbfc7...80b4` | `SHORT` | 1,425,020.00 USD | `1,075.00` | `558.03` | `1325.90` | `5443.66` | -825,141.27 USD | `-57.90%` | `10X Cross` |
| `1611` | `0x51f6...2b39` | `SHORT` | 1,378,418.65 USD | `1,039.88` | `1302.72` | `1325.90` | `2851.52` | -23,741.84 USD | `-1.72%` | `10X Cross` |
| `1641` | `0x123d...3bff` | `SHORT` | 1,337,411.79 USD | `1,008.15` | `489.25` | `1325.90` | `4207.46` | -844,177.72 USD | `-63.12%` | `10X Cross` |
| `1650` | `0xe282...df29` | `LONG` | 1,326,400.00 USD | `1,000.00` | `420.99` | `1325.90` | `107.80` | 905,413.14 USD | `+68.26%` | `10X Cross` |
| `1651` | `0x266b...efcb` | `LONG` | 1,325,800.00 USD | `1,000.00` | `826.11` | `1325.90` | `162.34` | 499,687.07 USD | `+37.69%` | `10X Cross` |
| `1653` | `0xb5ff...d912` | `LONG` | 1,325,555.50 USD | `1,000.00` | `1141.93` | `1325.90` | `400.44` | 183,625.20 USD | `+13.85%` | `2X Cross` |
| `1654` | `0x0748...d4b2` | `LONG` | 1,325,555.50 USD | `1,000.00` | `1334.09` | `1325.90` | `0.000000` | -8,532.80 USD | `-0.64%` | `7X Cross` |
| `1680` | `0x17f0...094f` | `LONG` | 1,304,591.22 USD | `984.30` | `1287.23` | `1325.90` | `536.75` | 37,571.06 USD | `+2.88%` | `5X Cross` |
| `1752` | `0x757d...94ba` | `LONG` | 1,226,138.84 USD | `925.00` | `1558.31` | `1325.90` | `0.000000` | -215,301.75 USD | `-17.56%` | `10X Cross` |
| `1801` | `0x2847...d47b` | `LONG` | 1,183,787.31 USD | `893.02` | `1238.53` | `1325.90` | `0.000000` | 77,759.24 USD | `+6.57%` | `5X Cross` |
| `1819` | `0xf096...7553` | `SHORT` | 1,167,858.28 USD | `881.07` | `1240.34` | `1325.90` | `3564.04` | -75,028.20 USD | `-6.42%` | `10X Cross` |
| `1820` | `0xdf95...7d72` | `SHORT` | 1,166,978.70 USD | `880.34` | `1073.83` | `1325.90` | `41279.58` | -221,640.60 USD | `-18.99%` | `10X Cross` |
| `1831` | `0xcf0a...856f` | `LONG` | 1,154,622.21 USD | `871.15` | `1292.19` | `1325.90` | `938.45` | 28,927.36 USD | `+2.51%` | `4X Cross` |
| `1861` | `0x7d0f...ea35` | `LONG` | 1,126,675.00 USD | `850.00` | `1317.57` | `1325.90` | `1255.64` | 6,739.42 USD | `+0.60%` | `10X Cross` |
| `1900` | `0x601c...4f54` | `SHORT` | 1,092,686.27 USD | `824.42` | `615.11` | `1325.90` | `2972.28` | -585,573.52 USD | `-53.59%` | `5X Cross` |
| `1910` | `0xae55...2236` | `LONG` | 1,083,601.85 USD | `817.47` | `1467.80` | `1325.90` | `0.000000` | -116,279.36 USD | `-10.73%` | `10X Cross` |
| `1916` | `0x71b1...79c8` | `LONG` | 1,077,726.53 USD | `812.52` | `1231.55` | `1325.90` | `699.46` | 77,071.07 USD | `+7.15%` | `10X Cross` |
| `1935` | `0x0f02...5384` | `LONG` | 1,061,834.28 USD | `800.78` | `1290.36` | `1325.90` | `292.92` | 28,540.21 USD | `+2.69%` | `3X Cross` |
| `1938` | `0x9b0f...db40` | `LONG` | 1,060,480.00 USD | `800.00` | `1268.86` | `1325.90` | `774.21` | 45,390.24 USD | `+4.28%` | `10X Cross` |
| `1948` | `0xabdb...84ac` | `LONG` | 1,052,115.46 USD | `793.69` | `711.79` | `1325.90` | `664.32` | 487,175.10 USD | `+46.30%` | `3X Cross` |
| `1954` | `0xfdf8...e381` | `LONG` | 1,047,202.10 USD | `790.01` | `1337.72` | `1325.90` | `382.46` | -9,607.58 USD | `-0.92%` | `10X Cross` |
| `1987` | `0x3205...40bb` | `SHORT` | 1,027,194.18 USD | `774.89` | `1332.37` | `1325.90` | `3042.66` | 5,243.68 USD | `+0.51%` | `10X Cross` |
| `2012` | `0x0c1f...1d39` | `SHORT` | 1,011,724.74 USD | `762.99` | `1299.17` | `1325.90` | `4931.26` | -20,473.65 USD | `-2.02%` | `10X Cross` |
| `2017` | `0xf6f3...47f8` | `SHORT` | 1,009,689.51 USD | `761.57` | `1253.10` | `1325.90` | `2392.68` | -55,366.51 USD | `-5.48%` | `5X Cross` |

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
  * 24H Horizon: Short MP=`1404.15` (Vol: 3,000,000.00 USD, Dist: `+6.21%`) | Long MP=`1287.60` (Vol: 2,300,000.00 USD, Dist: `--2.61%`)
  * 48H Horizon: Short MP=`1404.15` (Vol: 3,000,000.00 USD, Dist: `+6.21%`) | Long MP=`1287.60` (Vol: 2,300,000.00 USD, Dist: `--2.61%`)
  * 3D Horizon: Short MP=`1404.42` (Vol: 3,000,000.00 USD, Dist: `+6.23%`) | Long MP=`1228.81` (Vol: 2,600,000.00 USD, Dist: `--7.05%`)
  * 7D Horizon: Short MP=`1404.10` (Vol: 3,000,000.00 USD, Dist: `+6.20%`) | Long MP=`1200.46` (Vol: 3,000,000.00 USD, Dist: `--9.20%`)
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
  * Current Rate: `67.87K` | Last 24h: `32.07K` | Last 3d: `282.84K` | Last 7d: `777.72K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0052%` | **USDT OKX** | `0.0100%` |
| **USDT Bybit** | `0.0100%` | **USDT KuCoin** | `0.0100%` |
| **USDT MEXC** | `0.0054%` | **USDT BingX** | `0.0045%` |
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
| `0:00 UTC` | `1335.45` | `1342.97` | `1335.45` | `1354.95` | `1333.05` | 31,234,081.19 USD | 13,144,149.56 USD | 18,089,931.62 USD | -4,945,782.06 USD | `-15.83%` | `2B / 7S` |
| `5:00 UTC` | `1333.95` | `1332.65` | `1333.95` | `1338.15` | `1327.05` | 42,051,592.22 USD | 20,998,597.47 USD | 21,052,994.75 USD | -54,397.28 USD | `-0.13%` | `1B / 3S` |
| `0:00 UTC` | `1324.05` | `1326.61` | `1324.05` | `1336.05` | `1320.15` | 35,175,848.19 USD | 15,805,961.43 USD | 19,369,886.76 USD | -3,563,925.33 USD | `-10.13%` | `1B / 10S` |
| `5:00 UTC` | `1321.35` | `1325.74` | `1321.35` | `1333.35` | `1318.35` | 26,289,288.34 USD | 11,537,630.34 USD | 14,751,657.99 USD | -3,214,027.65 USD | `-12.23%` | `3B / 5S` |
| `0:00 UTC` | `1315.95` | `1314.40` | `1315.95` | `1321.95` | `1307.85` | 50,919,152.62 USD | 22,517,005.07 USD | 28,402,147.55 USD | -5,885,142.49 USD | `-11.56%` | `2B / 5S` |
| `5:00 UTC` | `1315.95` | `1319.00` | `1315.95` | `1325.85` | `1312.05` | 22,246,351.59 USD | 13,151,982.06 USD | 9,094,369.53 USD | 4,057,612.52 USD | `+18.24%` | `9B / 1S` |
| `0:00 UTC` | `1320.75` | `1319.74` | `1320.75` | `1325.25` | `1315.95` | 11,564,611.33 USD | 5,754,638.99 USD | 5,809,972.34 USD | -55,333.35 USD | `-0.48%` | `1B / 2S` |
| `5:00 UTC` | `1322.85` | `1320.89` | `1322.85` | `1324.95` | `1316.85` | 7,868,027.33 USD | 4,223,932.72 USD | 3,644,094.61 USD | 579,838.11 USD | `+7.37%` | `3B / 0S` |
| `0:00 UTC` | `1324.95` | `1324.41` | `1324.95` | `1327.05` | `1319.85` | 12,000,472.36 USD | 6,714,467.49 USD | 5,286,004.87 USD | 1,428,462.62 USD | `+11.90%` | `2B / 1S` |
| `5:00 UTC` | `1325.25` | `1325.35` | `1325.25` | `1330.65` | `1320.75` | 10,789,291.39 USD | 5,373,785.30 USD | 5,415,506.09 USD | -41,720.79 USD | `-0.39%` | `3B / 1S` |

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
| `5m` | -16,580.00 USD | -1,330,000.00 USD | **`DISTRIBUTION`** |
| `15m` | -493,900.00 USD | 935,580.00 USD | **`ACCUMULATION`** |
| `30m` | 120,760.00 USD | 4,610,000.00 USD | **`ACCUMULATION`** |
| `1h` | 776,640.00 USD | 14,920,000.00 USD | **`ACCUMULATION`** |
| `2h` | 487,210.00 USD | -9,460,000.00 USD | **`DISTRIBUTION`** |
| `4h` | 12,760,000.00 USD | 35,690,000.00 USD | **`ACCUMULATION`** |
| `6h` | 29,070,000.00 USD | 90,640,000.00 USD | **`ACCUMULATION`** |
| `8h` | 31,250,000.00 USD | 105,890,000.00 USD | **`ACCUMULATION`** |
| `12h` | 27,820,000.00 USD | 119,390,000.00 USD | **`ACCUMULATION`** |
| `24h` | 10,730,000.00 USD | 78,660,000.00 USD | **`ACCUMULATION`** |
| `1w` | 48,720,000.00 USD | 256,100,000.00 USD | **`ACCUMULATION`** |
| `30d` | 69,010,000.00 USD | -503,270,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-16.58K` | 15m=`-493.90K` | 1h=`+776.64K` | 24h=`+10.73M`
* Futures Capital Netflows: 5m=`-1.33M` | 15m=`+935.58K` | 1h=`+14.92M` | 24h=`+78.66M`
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
  * `2026-10-30 00:58:24 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 00:48:24 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 01:28:24 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 01:28:24 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 01:27:24 IST`: [@DeItaone] - (Sentiment: `Neutral`)
  * `2026-10-30 01:27:24 IST`: [@mb_ghalibaf] - (Sentiment: `Neutral`)
  * `2026-10-30 01:27:24 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-30 01:27:24 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-30 01:27:24 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:29:24 IST`: [fxstreet.com] - (Sentiment: `Neutral`)
  * `2026-10-29 21:29:24 IST`: [ForexFactory] - (Sentiment: `Neutral`)
  * `2026-10-29 21:29:24 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-29 21:29:24 IST`: [youtube.com/bankofcanadaofficial] - (Sentiment: `Neutral`)
  * `2026-10-29 21:29:24 IST`: [notayesmanseconomics.wordpress.com] - (Sentiment: `Neutral`)
  * `2026-10-29 20:29:24 IST`: [think.ing.com] - (Sentiment: `Neutral`)


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
  * Spread-Padded Stop Loss: `1224.73` (Risk Distance: `5.82` pts)
  * +2.5R Take Profit: `1245.10`
  * Mathematical Lot Sizing: **`1.71 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `1309.36` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `1315.18` (Risk Distance: `5.82` pts)
  * +2.5R Take Profit: `1294.81`
  * Mathematical Lot Sizing: **`1.71 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`1335.64`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
