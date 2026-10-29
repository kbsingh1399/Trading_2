# 🏛️ SOVEREIGN CANDIDATE DOSSIER: ZECUSD
**Canonical Key**: `ZECUSD` | **Broker Instrument**: `ZECUSD.p` | **Asset Class**: `Crypto Altcoin`
**Timestamp**: `2026-10-29 23:46:55 IST` (`2026-10-29 18:16:55 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `1329.75` | **Live Ask Quote**: `1330.61` | **Mid Price**: `1330.18`
- **Spread Points**: `86.00` | **Spread BPS**: `6.47 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `1278.32` | VWAP Z-Score: `+1.33` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `17.08` (Volatility Regime: `HIGH_EXPANSION`)
  * 14-Period RSI: `56.69` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `1394.55` | Lower -3.00σ Band: `1162.08`
  * Upper +2.51σ Band: `1375.57` | Lower -2.51σ Band: `1181.07`
  * Upper +2.01σ Band: `1356.19` | Lower -2.01σ Band: `1200.44`
  * Upper +2.00σ Band: `1355.81` | Lower -2.00σ Band: `1200.83`
  * Upper +1.28σ Band: `1327.91` | Lower -1.28σ Band: `1228.73`
  * Upper +1.00σ Band: `1317.06` | Lower -1.00σ Band: `1239.57`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`1337.67` | EMA-20=`1324.01` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`1298.09` (Slope: `+0.0000`) | EMA-100=`1287.42`
  * Institutional Anchors: EMA-144=`1283.07` | EMA-200=`1278.23` (Slope: `+0.6659`) | EMA-233=`1275.60`
- **Range Boundaries**: 24H High=`1396.49` | 24H Low=`1230.00` | Weekly High=`1396.49` | Weekly Low=`1210.62`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `1303.81` (Distance: `+2.15%`)
  * Point of Control (POC) = `1247.20` (Distance: `+6.78%`)
  * Value Area Low (VAL) = `1230.55` (Distance: `+8.23%`)
  * Auction Positioning: `ABOVE_VALUE (Imbalance)` | Session Bias: **`BULLISH (Above Pivot)`** | Market Regime: `TREND_UP_ACCEPTANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`1320.44` | POC=`1312.10` | VAL=`1285.78`
  * Prior Day Extremes: PDH=`1328.99` | PDL=`1263.19` | PDC=`1296.46`
  * Monday Range Blueprint: High=`1267.53` | Mid=`1222.14` | Low=`1176.75`
  * Developing Weekly Value Area: Weekly VAH=`1294.68` | Weekly POC=`1239.01` | Weekly VAL=`1195.06`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`1318.68` | Low=`1230.00`
  * London Session (08:00-16:00 UTC): High=`1276.13` | Low=`1233.52`
  * New York Session (13:00-21:00 UTC): High=`1396.49` | Low=`1250.65`
  * Initial Balance (First Hour): IB High=`1255.79` | IB Low=`1245.43`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `1324.86` - `1335.50`
  * Optimal Trade Entry (OTE 0.705): `1332.84`
  * Structural Invalidation Anchor (0.786): `1340.82`

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
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-29 23:45:33 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `16` | `0xb83d...6e36` | `SHORT` | 69,887,427.33 USD | `52,582.52` | `1336.45` | `1329.10` | `3685.27` | 386,487.56 USD | `+0.55%` | `3X Cross` |
| `23` | `0x5b5d...c060` | `SHORT` | 54,163,648.54 USD | `40,727.61` | `1478.36` | `1329.10` | `4956.85` | 6,046,615.65 USD | `+11.16%` | `3X Cross` |
| `43` | `0x7fda...17d1` | `SHORT` | 29,869,557.07 USD | `22,465.07` | `1261.38` | `1329.10` | `2920.20` | -1,532,534.64 USD | `-5.13%` | `5X Cross` |
| `77` | `0x60b0...991e` | `LONG` | 22,290,206.62 USD | `16,779.74` | `1179.65` | `1329.10` | `881.31` | 2,495,959.60 USD | `+11.20%` | `10X Cross` |
| `83` | `0xbf73...5d58` | `LONG` | 21,291,200.00 USD | `16,000.00` | `1214.30` | `1329.10` | `711.39` | 1,862,367.75 USD | `+8.75%` | `10X Cross` |
| `131` | `0xc36a...105b` | `LONG` | 15,308,239.52 USD | `11,510.82` | `1215.14` | `1329.10` | `927.59` | 1,320,958.49 USD | `+8.63%` | `10X Cross` |
| `169` | `0x8742...8427` | `LONG` | 12,233,928.82 USD | `9,201.21` | `1286.37` | `1329.10` | `698.34` | 397,758.82 USD | `+3.25%` | `10X Cross` |
| `192` | `0xad59...ba81` | `SHORT` | 11,197,667.50 USD | `8,425.00` | `330.91` | `1329.10` | `2139.66` | -8,409,709.73 USD | `-75.10%` | `10X Cross` |
| `199` | `0xdd53...2b13` | `SHORT` | 10,950,146.83 USD | `8,235.67` | `739.37` | `1329.10` | `7775.81` | -4,860,915.99 USD | `-44.39%` | `3X Cross` |
| `202` | `0x9ffd...ce40` | `LONG` | 10,873,024.51 USD | `8,171.52` | `1251.85` | `1329.10` | `565.51` | 643,473.44 USD | `+5.92%` | `5X Cross` |
| `207` | `0xfc66...ca06` | `SHORT` | 10,683,362.59 USD | `8,035.02` | `1319.72` | `1329.10` | `5433.33` | -79,356.64 USD | `-0.74%` | `10X Cross` |
| `220` | `0x880a...311c` | `SHORT` | 10,248,144.17 USD | `7,707.11` | `1367.50` | `1329.10` | `2301.07` | 291,340.04 USD | `+2.84%` | `10X Cross` |
| `267` | `0x2b61...2f6c` | `LONG` | 9,051,267.90 USD | `6,807.00` | `1453.56` | `1329.10` | `649.87` | -843,083.32 USD | `-9.31%` | `10X Cross` |
| `283` | `0x2ae5...83e7` | `LONG` | 8,558,369.28 USD | `6,436.80` | `1391.82` | `1329.10` | `0.000000` | -400,522.71 USD | `-4.68%` | `2X Cross` |
| `319` | `0xecb6...2b00` | `SHORT` | 7,758,972.00 USD | `5,844.80` | `1324.05` | `1329.10` | `5978.81` | -20,159.06 USD | `-0.26%` | `5X Cross` |
| `330` | `0x26b6...9a13` | `LONG` | 7,224,687.41 USD | `5,433.73` | `1282.23` | `1329.10` | `202.84` | 257,384.17 USD | `+3.56%` | `10X Cross` |
| `341` | `0x45d2...4029` | `SHORT` | 6,949,819.20 USD | `5,227.00` | `833.44` | `1329.10` | `7935.91` | -2,593,441.23 USD | `-37.32%` | `5X Cross` |
| `359` | `0xea00...a918` | `LONG` | 6,645,500.00 USD | `5,000.00` | `739.16` | `1329.10` | `0.000000` | 2,949,684.89 USD | `+44.39%` | `5X Cross` |
| `375` | `0xdd7a...8830` | `LONG` | 6,459,678.53 USD | `4,860.19` | `897.48` | `1329.10` | `801.76` | 2,097,774.86 USD | `+32.47%` | `10X Cross` |
| `380` | `0xf081...e39e` | `LONG` | 6,273,610.00 USD | `4,717.00` | `1195.70` | `1329.10` | `1200.07` | 633,485.95 USD | `+10.10%` | `10X Cross` |
| `438` | `0x4cae...7c34` | `LONG` | 5,324,597.49 USD | `4,004.36` | `999.34` | `1329.10` | `714.23` | 1,322,869.34 USD | `+24.84%` | `10X Cross` |
| `451` | `0xa61c...66b9` | `LONG` | 5,168,318.40 USD | `3,888.00` | `1148.34` | `1329.10` | `0.000000` | 703,576.26 USD | `+13.61%` | `10X Cross` |
| `471` | `0x9aa5...58af` | `SHORT` | 4,947,640.27 USD | `3,720.31` | `1205.51` | `1329.10` | `3275.81` | -462,753.47 USD | `-9.35%` | `10X Cross` |
| `474` | `0x0153...8052` | `SHORT` | 4,917,469.95 USD | `3,698.18` | `1307.82` | `1329.10` | `2504.67` | -80,899.20 USD | `-1.65%` | `1X Isolated` |
| `503` | `0xd4c1...3d1d` | `SHORT` | 4,614,270.43 USD | `3,470.42` | `1302.96` | `1329.10` | `2639.24` | -92,436.78 USD | `-2.00%` | `10X Cross` |
| `523` | `0x382b...3e39` | `LONG` | 4,368,895.42 USD | `3,291.07` | `1166.49` | `1329.10` | `0.000000` | 529,892.73 USD | `+12.13%` | `10X Cross` |
| `529` | `0xd21d...90f1` | `LONG` | 4,319,575.00 USD | `3,250.00` | `1253.64` | `1329.10` | `875.86` | 245,233.27 USD | `+5.68%` | `4X Isolated` |
| `547` | `0x1338...c48e` | `LONG` | 4,188,741.90 USD | `3,149.43` | `1018.52` | `1329.10` | `820.16` | 980,996.36 USD | `+23.42%` | `4X Isolated` |
| `551` | `0x456f...cdf1` | `LONG` | 4,150,752.72 USD | `3,122.98` | `1268.03` | `1329.10` | `490.15` | 190,728.48 USD | `+4.60%` | `10X Cross` |
| `559` | `0xdbe0...d6d5` | `LONG` | 4,102,616.49 USD | `3,085.37` | `422.97` | `1329.10` | `338.47` | 2,797,612.00 USD | `+68.19%` | `3X Isolated` |
| `581` | `0x9c06...0560` | `SHORT` | 3,978,526.86 USD | `2,989.80` | `786.00` | `1329.10` | `2362.94` | -1,628,531.86 USD | `-40.93%` | `10X Cross` |
| `600` | `0x27c9...d65d` | `SHORT` | 3,872,120.19 USD | `2,913.34` | `1248.26` | `1329.10` | `1838.25` | -235,522.66 USD | `-6.08%` | `10X Cross` |
| `682` | `0xac48...3201` | `LONG` | 3,376,312.73 USD | `2,540.30` | `1393.86` | `1329.10` | `526.61` | -164,516.56 USD | `-4.87%` | `10X Cross` |
| `687` | `0xa183...0482` | `LONG` | 3,369,206.40 USD | `2,534.00` | `530.25` | `1329.10` | `444.40` | 2,025,543.68 USD | `+60.12%` | `5X Isolated` |
| `696` | `0x325e...9564` | `LONG` | 3,325,788.96 USD | `2,501.91` | `1306.24` | `1329.10` | `0.000000` | 57,695.06 USD | `+1.73%` | `10X Cross` |
| `697` | `0x0871...e927` | `LONG` | 3,324,250.00 USD | `2,500.00` | `1276.50` | `1329.10` | `0.000000` | 133,000.00 USD | `+4.00%` | `10X Cross` |
| `709` | `0x9b86...6e6e` | `LONG` | 3,279,288.43 USD | `2,467.30` | `637.58` | `1329.10` | `889.62` | 1,706,188.83 USD | `+52.03%` | `3X Cross` |
| `726` | `0x2e30...4cb5` | `SHORT` | 3,217,249.04 USD | `2,419.53` | `1298.38` | `1329.10` | `3191.75` | -75,784.93 USD | `-2.36%` | `2X Cross` |
| `763` | `0xb2f7...af9f` | `SHORT` | 3,075,165.25 USD | `2,313.72` | `746.63` | `1329.10` | `4180.72` | -1,347,676.51 USD | `-43.82%` | `10X Cross` |
| `793` | `0xf48f...10fe` | `LONG` | 2,948,595.06 USD | `2,218.49` | `1517.87` | `1329.10` | `876.78` | -418,791.77 USD | `-14.20%` | `3X Cross` |
| `820` | `0x5bc4...3b0c` | `SHORT` | 2,833,031.90 USD | `2,130.74` | `1089.65` | `1329.10` | `3552.85` | -511,274.33 USD | `-18.05%` | `5X Cross` |
| `840` | `0x8de4...b9aa` | `SHORT` | 2,782,670.47 USD | `2,091.29` | `1331.35` | `1329.10` | `1689.79` | 1,569.23 USD | `+0.06%` | `3X Cross` |
| `847` | `0x4fe2...ac59` | `SHORT` | 2,751,873.59 USD | `2,071.57` | `1478.56` | `1329.10` | `1811.03` | 311,072.63 USD | `+11.30%` | `10X Cross` |
| `864` | `0x668c...ea2e` | `SHORT` | 2,659,800.00 USD | `2,000.00` | `1409.16` | `1329.10` | `2701.67` | 158,522.04 USD | `+5.96%` | `10X Cross` |
| `884` | `0x77ee...2902` | `SHORT` | 2,587,636.09 USD | `1,946.03` | `759.84` | `1329.10` | `5261.98` | -1,108,958.58 USD | `-42.86%` | `10X Cross` |
| `894` | `0x3e2f...b269` | `SHORT` | 2,560,158.10 USD | `1,925.51` | `1134.87` | `1329.10` | `2931.72` | -374,959.24 USD | `-14.65%` | `10X Cross` |
| `902` | `0xe097...d0fe` | `LONG` | 2,545,417.51 USD | `1,913.56` | `1261.17` | `1329.10` | `0.000000` | 132,091.35 USD | `+5.19%` | `10X Cross` |
| `912` | `0x4f12...618b` | `SHORT` | 2,517,311.70 USD | `1,896.28` | `1608.30` | `1329.10` | `2116.68` | 532,472.69 USD | `+21.15%` | `3X Cross` |
| `913` | `0x71d0...8c26` | `SHORT` | 2,509,201.48 USD | `1,888.89` | `1361.12` | `1329.10` | `5242.85` | 61,804.84 USD | `+2.46%` | `10X Cross` |
| `952` | `0x866d...d6e1` | `LONG` | 2,399,970.19 USD | `1,802.05` | `674.73` | `1329.10` | `74.59` | 1,184,068.88 USD | `+49.34%` | `10X Cross` |
| `987` | `0x2309...a2d9` | `LONG` | 2,327,817.06 USD | `1,750.37` | `1186.09` | `1329.10` | `801.83` | 251,722.95 USD | `+10.81%` | `8X Cross` |
| `1000` | `0x023a...2355` | `SHORT` | 2,282,089.07 USD | `1,716.76` | `1313.17` | `1329.10` | `6028.70` | -27,699.43 USD | `-1.21%` | `10X Cross` |
| `1004` | `0x2edd...8179` | `SHORT` | 2,268,211.18 USD | `1,706.32` | `1261.18` | `1329.10` | `2937.81` | -116,234.17 USD | `-5.12%` | `10X Cross` |
| `1030` | `0x265e...7f70` | `LONG` | 2,197,805.24 USD | `1,651.74` | `1388.09` | `1329.10` | `0.000000` | -94,964.44 USD | `-4.32%` | `3X Cross` |
| `1042` | `0xa271...a3f7` | `LONG` | 2,167,191.61 USD | `1,631.43` | `1190.60` | `1329.10` | `910.25` | 224,809.81 USD | `+10.37%` | `4X Cross` |
| `1050` | `0x7f75...9edf` | `LONG` | 2,136,811.45 USD | `1,605.78` | `1199.97` | `1329.10` | `973.41` | 209,919.55 USD | `+9.82%` | `10X Cross` |
| `1056` | `0x6646...6de5` | `SHORT` | 2,127,520.00 USD | `1,600.00` | `660.64` | `1329.10` | `4867.06` | -1,070,495.03 USD | `-50.32%` | `10X Cross` |
| `1067` | `0xdf57...93f5` | `LONG` | 2,100,448.90 USD | `1,579.76` | `1218.38` | `1329.10` | `780.10` | 175,692.92 USD | `+8.36%` | `3X Isolated` |
| `1080` | `0xab59...59b5` | `LONG` | 2,080,466.81 USD | `1,565.32` | `1342.15` | `1329.10` | `789.66` | -20,428.41 USD | `-0.98%` | `10X Cross` |
| `1084` | `0xfe7c...b7ae` | `SHORT` | 2,075,611.72 USD | `1,562.49` | `1350.62` | `1329.10` | `6410.93` | 34,717.33 USD | `+1.67%` | `10X Cross` |
| `1088` | `0x634f...6951` | `LONG` | 2,066,577.10 USD | `1,553.00` | `1263.46` | `1329.10` | `1184.29` | 104,427.52 USD | `+5.05%` | `10X Cross` |
| `1100` | `0x3e47...aaf6` | `LONG` | 2,041,869.75 USD | `1,536.28` | `1277.06` | `1329.10` | `1013.66` | 79,947.66 USD | `+3.92%` | `10X Cross` |
| `1139` | `0xcf67...eb24` | `LONG` | 1,992,600.00 USD | `1,500.00` | `887.05` | `1329.10` | `513.19` | 662,028.63 USD | `+33.22%` | `10X Cross` |
| `1148` | `0x4e23...20c3` | `LONG` | 1,982,387.99 USD | `1,491.19` | `1302.47` | `1329.10` | `0.000000` | 40,155.82 USD | `+2.03%` | `4X Cross` |
| `1161` | `0x039c...0ebd` | `SHORT` | 1,967,719.26 USD | `1,480.49` | `1238.67` | `1329.10` | `3122.80` | -133,887.94 USD | `-6.80%` | `10X Cross` |
| `1185` | `0xfc27...9d9d` | `SHORT` | 1,928,770.94 USD | `1,450.64` | `1317.46` | `1329.10` | `10940.91` | -17,605.24 USD | `-0.91%` | `10X Cross` |
| `1238` | `0x2ab7...c2f8` | `LONG` | 1,862,258.15 USD | `1,400.51` | `813.26` | `1329.10` | `795.33` | 723,276.46 USD | `+38.84%` | `3X Cross` |
| `1253` | `0x11be...8b1d` | `LONG` | 1,828,615.65 USD | `1,375.83` | `1206.55` | `1329.10` | `1134.38` | 168,607.70 USD | `+9.22%` | `10X Isolated` |
| `1310` | `0xef96...9383` | `SHORT` | 1,738,636.49 USD | `1,308.82` | `1249.96` | `1329.10` | `4092.18` | -102,670.07 USD | `-5.91%` | `10X Cross` |
| `1321` | `0xdf83...3cff` | `SHORT` | 1,713,236.48 USD | `1,289.02` | `1244.72` | `1329.10` | `1861.26` | -108,766.22 USD | `-6.35%` | `10X Cross` |
| `1350` | `0x5323...b23c` | `SHORT` | 1,684,456.94 USD | `1,266.89` | `1343.99` | `1329.10` | `5784.31` | 18,226.35 USD | `+1.08%` | `5X Cross` |
| `1353` | `0xe065...0f85` | `SHORT` | 1,677,251.12 USD | `1,262.61` | `1087.02` | `1329.10` | `1734.63` | -304,775.00 USD | `-18.17%` | `10X Cross` |
| `1374` | `0x7277...0b98` | `SHORT` | 1,642,002.82 USD | `1,234.96` | `1298.48` | `1329.10` | `2346.57` | -38,433.40 USD | `-2.34%` | `10X Cross` |
| `1429` | `0x5975...9abd` | `LONG` | 1,594,920.00 USD | `1,200.00` | `1179.54` | `1329.10` | `289.83` | 179,477.21 USD | `+11.25%` | `5X Cross` |
| `1470` | `0x69cc...14fd` | `SHORT` | 1,543,911.98 USD | `1,161.36` | `675.33` | `1329.10` | `7838.49` | -759,606.46 USD | `-49.20%` | `10X Cross` |
| `1474` | `0x7a76...b16d` | `LONG` | 1,542,088.27 USD | `1,160.25` | `1358.50` | `1329.10` | `1227.47` | -34,111.57 USD | `-2.21%` | `10X Cross` |
| `1487` | `0x3fc5...c0c1` | `SHORT` | 1,526,391.60 USD | `1,148.44` | `1264.34` | `1329.10` | `3049.08` | -74,377.83 USD | `-4.87%` | `10X Cross` |
| `1507` | `0xe35c...a1d3` | `LONG` | 1,498,200.86 USD | `1,127.06` | `1318.20` | `1329.10` | `694.30` | 12,505.51 USD | `+0.83%` | `2X Isolated` |
| `1512` | `0x5f94...4b96` | `LONG` | 1,482,305.36 USD | `1,115.27` | `538.00` | `1329.10` | `0.000000` | 882,287.72 USD | `+59.52%` | `10X Cross` |
| `1528` | `0x71df...a23d` | `SHORT` | 1,460,382.92 USD | `1,098.28` | `513.50` | `1329.10` | `2545.33` | -896,412.73 USD | `-61.38%` | `2X Cross` |
| `1560` | `0xbfc7...80b4` | `SHORT` | 1,429,642.50 USD | `1,075.00` | `558.03` | `1329.10` | `5298.68` | -829,763.77 USD | `-58.04%` | `10X Cross` |
| `1602` | `0x51f6...2b39` | `SHORT` | 1,382,624.45 USD | `1,039.88` | `1302.72` | `1329.10` | `2849.38` | -27,947.64 USD | `-2.02%` | `10X Cross` |
| `1632` | `0x123d...3bff` | `SHORT` | 1,339,932.17 USD | `1,008.15` | `489.25` | `1329.10` | `4173.52` | -846,698.09 USD | `-63.19%` | `10X Cross` |
| `1641` | `0x266b...efcb` | `LONG` | 1,329,700.00 USD | `1,000.00` | `826.11` | `1329.10` | `156.02` | 503,587.07 USD | `+37.87%` | `10X Cross` |
| `1642` | `0xb5ff...d912` | `LONG` | 1,329,600.00 USD | `1,000.00` | `1141.93` | `1329.10` | `400.42` | 187,669.70 USD | `+14.11%` | `2X Cross` |
| `1643` | `0x0748...d4b2` | `LONG` | 1,329,600.00 USD | `1,000.00` | `1334.09` | `1329.10` | `0.000000` | -4,488.30 USD | `-0.34%` | `7X Cross` |
| `1644` | `0xe282...df29` | `LONG` | 1,329,100.00 USD | `1,000.00` | `420.99` | `1329.10` | `98.42` | 908,113.14 USD | `+68.33%` | `10X Cross` |
| `1669` | `0x17f0...094f` | `LONG` | 1,308,823.71 USD | `984.30` | `1287.23` | `1329.10` | `536.73` | 41,803.55 USD | `+3.19%` | `5X Cross` |
| `1739` | `0x757d...94ba` | `LONG` | 1,229,880.00 USD | `925.00` | `1558.31` | `1329.10` | `0.000000` | -211,560.58 USD | `-17.20%` | `10X Cross` |
| `1755` | `0x3205...40bb` | `SHORT` | 1,214,042.69 USD | `913.02` | `1340.26` | `1329.10` | `2758.84` | 9,639.17 USD | `+0.79%` | `10X Cross` |
| `1806` | `0xf096...7553` | `SHORT` | 1,172,351.74 USD | `881.07` | `1240.34` | `1329.10` | `3460.92` | -79,521.66 USD | `-6.78%` | `10X Cross` |
| `1811` | `0xdf95...7d72` | `SHORT` | 1,170,308.86 USD | `880.13` | `1073.73` | `1329.10` | `41040.16` | -225,290.97 USD | `-19.25%` | `10X Cross` |
| `1823` | `0xcf0a...856f` | `LONG` | 1,159,239.30 USD | `871.15` | `1292.19` | `1329.10` | `938.44` | 33,544.46 USD | `+2.89%` | `4X Cross` |
| `1825` | `0x2847...d47b` | `LONG` | 1,157,961.94 USD | `870.91` | `1236.40` | `1329.10` | `0.000000` | 81,170.72 USD | `+7.01%` | `5X Cross` |
| `1853` | `0x7d0f...ea35` | `LONG` | 1,131,010.00 USD | `850.00` | `1317.57` | `1329.10` | `1275.61` | 11,074.42 USD | `+0.98%` | `10X Cross` |
| `1884` | `0x601c...4f54` | `SHORT` | 1,098,292.32 USD | `824.42` | `615.11` | `1329.10` | `2906.43` | -591,179.57 USD | `-53.83%` | `5X Cross` |
| `1894` | `0xae55...2236` | `LONG` | 1,086,908.11 USD | `817.47` | `1467.80` | `1329.10` | `0.000000` | -112,973.10 USD | `-10.39%` | `10X Cross` |
| `1902` | `0x71b1...79c8` | `LONG` | 1,080,082.84 USD | `812.52` | `1231.55` | `1329.10` | `687.72` | 79,427.38 USD | `+7.35%` | `10X Cross` |
| `1926` | `0x0f02...5384` | `LONG` | 1,064,556.93 USD | `800.78` | `1290.36` | `1329.10` | `289.29` | 31,262.86 USD | `+2.94%` | `3X Cross` |
| `1929` | `0x9b0f...db40` | `LONG` | 1,063,760.00 USD | `800.00` | `1268.86` | `1329.10` | `774.58` | 48,670.24 USD | `+4.58%` | `10X Cross` |
| `1930` | `0xea0f...4e73` | `LONG` | 1,063,280.00 USD | `800.00` | `1364.27` | `1329.10` | `572.78` | -28,138.68 USD | `-2.65%` | `10X Cross` |
| `1938` | `0xabdb...84ac` | `LONG` | 1,055,528.33 USD | `793.69` | `711.79` | `1329.10` | `664.30` | 490,587.97 USD | `+46.48%` | `3X Cross` |
| `1951` | `0xfdf8...e381` | `LONG` | 1,050,397.30 USD | `790.01` | `1337.72` | `1329.10` | `320.53` | -6,412.39 USD | `-0.61%` | `10X Cross` |
| `1997` | `0x0c1f...1d39` | `SHORT` | 1,014,318.91 USD | `762.99` | `1299.17` | `1329.10` | `4718.33` | -23,067.82 USD | `-2.27%` | `10X Cross` |
| `1998` | `0xf6f3...47f8` | `SHORT` | 1,013,192.73 USD | `761.57` | `1253.10` | `1329.10` | `2347.00` | -58,869.73 USD | `-5.81%` | `5X Cross` |
| `2007` | `0x389a...e76b` | `LONG` | 1,010,288.78 USD | `760.13` | `1266.20` | `1329.10` | `370.13` | 47,815.36 USD | `+4.73%` | `10X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `1297.10` | 194.56 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Long: 0.19K USD at 1297.1000 USD [API] | `2026-10-27 15:46:39` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`1404.15` (Vol: 3,000,000.00 USD, Dist: `+6.21%`) | Long MP=`1287.60` (Vol: 2,300,000.00 USD, Dist: `--2.61%`)
  * 48H Horizon: Short MP=`1404.15` (Vol: 3,000,000.00 USD, Dist: `+6.21%`) | Long MP=`1287.60` (Vol: 2,300,000.00 USD, Dist: `--2.61%`)
  * 3D Horizon: Short MP=`1404.42` (Vol: 3,000,000.00 USD, Dist: `+6.23%`) | Long MP=`1228.81` (Vol: 2,600,000.00 USD, Dist: `--7.06%`)
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
  * Current Rate: `98.65K` | Last 24h: `32.07K` | Last 3d: `282.84K` | Last 7d: `777.72K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0100%` | **USDT OKX** | `0.0100%` |
| **USDT Bybit** | `0.0100%` | **USDT KuCoin** | `0.0100%` |
| **USDT MEXC** | `0.0099%` | **USDT BingX** | `0.0078%` |
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
| `5:00 UTC` | `1360.05` | `1349.51` | `1360.05` | `1362.15` | `1334.25` | 65,905,391.58 USD | 39,286,823.07 USD | 26,618,568.52 USD | 12,668,254.55 USD | `+19.22%` | `19B / 3S` |
| `0:00 UTC` | `1369.95` | `1375.81` | `1369.95` | `1397.55` | `1350.75` | 159,915,504.01 USD | 87,974,917.65 USD | 71,940,586.35 USD | 16,034,331.30 USD | `+10.03%` | `21B / 3S` |
| `5:00 UTC` | `1359.75` | `1358.32` | `1359.75` | `1373.25` | `1346.25` | 77,512,400.13 USD | 36,921,415.88 USD | 40,590,984.25 USD | -3,669,568.36 USD | `-4.73%` | `4B / 13S` |
| `0:00 UTC` | `1353.15` | `1350.71` | `1353.15` | `1361.25` | `1341.75` | 52,010,841.39 USD | 26,247,439.78 USD | 25,763,401.61 USD | 484,038.17 USD | `+0.93%` | `5B / 3S` |
| `5:00 UTC` | `1343.25` | `1344.85` | `1343.25` | `1353.45` | `1340.25` | 26,552,172.39 USD | 11,915,117.49 USD | 14,637,054.90 USD | -2,721,937.40 USD | `-10.25%` | `0B / 9S` |
| `0:00 UTC` | `1342.95` | `1346.21` | `1342.95` | `1354.05` | `1340.25` | 27,005,669.33 USD | 14,153,013.83 USD | 12,852,655.50 USD | 1,300,358.33 USD | `+4.82%` | `5B / 3S` |
| `5:00 UTC` | `1348.65` | `1350.13` | `1348.65` | `1356.15` | `1344.45` | 21,612,679.16 USD | 11,526,731.97 USD | 10,085,947.19 USD | 1,440,784.78 USD | `+6.67%` | `2B / 2S` |
| `0:00 UTC` | `1335.45` | `1342.97` | `1335.45` | `1354.95` | `1333.05` | 31,234,081.19 USD | 13,144,149.56 USD | 18,089,931.62 USD | -4,945,782.06 USD | `-15.83%` | `2B / 7S` |
| `5:00 UTC` | `1333.95` | `1332.65` | `1333.95` | `1338.15` | `1327.05` | 42,051,592.22 USD | 20,998,597.47 USD | 21,052,994.75 USD | -54,397.28 USD | `-0.13%` | `1B / 3S` |
| `0:00 UTC` | `1324.05` | `1326.49` | `1324.05` | `1336.05` | `1320.15` | 29,653,806.82 USD | 12,474,049.45 USD | 17,179,757.37 USD | -4,705,707.93 USD | `-15.87%` | `1B / 15S` |

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
| `5m` | 959,330.00 USD | 1,530,000.00 USD | **`ACCUMULATION`** |
| `15m` | 1,700,000.00 USD | -7,390,000.00 USD | **`DISTRIBUTION`** |
| `30m` | 305,390.00 USD | -10,810,000.00 USD | **`DISTRIBUTION`** |
| `1h` | -1,140,000.00 USD | -14,360,000.00 USD | **`DISTRIBUTION`** |
| `2h` | 3,950,000.00 USD | -21,710,000.00 USD | **`DISTRIBUTION`** |
| `4h` | 27,110,000.00 USD | 88,210,000.00 USD | **`ACCUMULATION`** |
| `6h` | 30,170,000.00 USD | 94,780,000.00 USD | **`ACCUMULATION`** |
| `8h` | 34,250,000.00 USD | 113,860,000.00 USD | **`ACCUMULATION`** |
| `12h` | 28,360,000.00 USD | 109,100,000.00 USD | **`ACCUMULATION`** |
| `24h` | 15,090,000.00 USD | 88,250,000.00 USD | **`ACCUMULATION`** |
| `1w` | 56,570,000.00 USD | 248,680,000.00 USD | **`ACCUMULATION`** |
| `30d` | 67,190,000.00 USD | -540,570,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+959.33K` | 15m=`+1.70M` | 1h=`-1.14M` | 24h=`+15.09M`
* Futures Capital Netflows: 5m=`+1.53M` | 15m=`-7.39M` | 1h=`-14.36M` | 24h=`+88.25M`
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
  * `2026-10-29 23:30:59 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:25:59 IST`: [@DeItaone] - (Sentiment: `Neutral`)
  * `2026-10-29 23:03:59 IST`: [@mb_ghalibaf] - (Sentiment: `Neutral`)
  * `2026-10-29 23:01:59 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-29 22:54:59 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-29 22:44:59 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:40:59 IST`: [fxstreet.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:39:59 IST`: [ForexFactory] - (Sentiment: `Neutral`)
  * `2026-10-29 23:39:59 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-29 23:39:59 IST`: [youtube.com/bankofcanadaofficial] - (Sentiment: `Neutral`)
  * `2026-10-29 23:39:59 IST`: [notayesmanseconomics.wordpress.com] - (Sentiment: `Neutral`)
  * `2026-10-29 20:41:59 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 20:41:59 IST`: [breakingthenews.net] - (Sentiment: `Neutral`)
  * `2026-10-29 19:41:59 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-29 19:41:59 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)


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
  * Spread-Padded Stop Loss: `1208.77` (Risk Distance: `21.78` pts)
  * +2.5R Take Profit: `1285.00`
  * Mathematical Lot Sizing: **`0.45 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `1303.81` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `1325.59` (Risk Distance: `21.78` pts)
  * +2.5R Take Profit: `1249.36`
  * Mathematical Lot Sizing: **`0.45 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`1340.82`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
