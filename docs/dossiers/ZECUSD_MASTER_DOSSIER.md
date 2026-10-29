# 🏛️ SOVEREIGN CANDIDATE DOSSIER: ZECUSD
**Canonical Key**: `ZECUSD` | **Broker Instrument**: `ZECUSD.p` | **Asset Class**: `Crypto Altcoin`
**Timestamp**: `2026-10-29 23:52:58 IST` (`2026-10-29 18:22:58 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

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
| `16` | `0xb83d...6e36` | `SHORT` | 69,934,751.60 USD | `52,582.52` | `1336.45` | `1330.80` | `3687.24` | 339,163.30 USD | `+0.48%` | `3X Cross` |
| `23` | `0x5b5d...c060` | `SHORT` | 54,184,012.34 USD | `40,727.61` | `1478.36` | `1330.80` | `4955.28` | 6,026,251.85 USD | `+11.12%` | `3X Cross` |
| `42` | `0x7fda...17d1` | `SHORT` | 29,892,463.25 USD | `22,467.09` | `1261.40` | `1330.80` | `2919.75` | -1,552,540.72 USD | `-5.19%` | `5X Cross` |
| `77` | `0x60b0...991e` | `LONG` | 22,317,054.20 USD | `16,779.74` | `1179.65` | `1330.80` | `881.98` | 2,522,807.19 USD | `+11.30%` | `10X Cross` |
| `82` | `0xbf73...5d58` | `LONG` | 21,292,800.00 USD | `16,000.00` | `1214.30` | `1330.80` | `709.26` | 1,863,967.75 USD | `+8.75%` | `10X Cross` |
| `131` | `0xc36a...105b` | `LONG` | 15,318,599.26 USD | `11,510.82` | `1215.14` | `1330.80` | `927.20` | 1,331,318.23 USD | `+8.69%` | `10X Cross` |
| `139` | `0x9071...5c0b` | `LONG` | 14,795,080.17 USD | `11,119.94` | `1370.53` | `1330.80` | `582.80` | -445,119.84 USD | `-3.01%` | `2X Cross` |
| `170` | `0x8742...8427` | `LONG` | 12,237,356.27 USD | `9,201.21` | `1286.37` | `1330.80` | `698.34` | 401,186.27 USD | `+3.28%` | `10X Cross` |
| `192` | `0xad59...ba81` | `SHORT` | 11,205,250.00 USD | `8,425.00` | `330.91` | `1330.80` | `2139.67` | -8,417,292.23 USD | `-75.12%` | `10X Cross` |
| `199` | `0xdd53...2b13` | `SHORT` | 10,969,912.44 USD | `8,235.67` | `739.37` | `1330.80` | `7783.77` | -4,880,681.60 USD | `-44.49%` | `3X Cross` |
| `202` | `0x9ffd...ce40` | `LONG` | 10,874,658.82 USD | `8,171.52` | `1252.29` | `1330.80` | `565.73` | 641,560.25 USD | `+5.90%` | `5X Cross` |
| `207` | `0xfc66...ca06` | `SHORT` | 10,612,627.41 USD | `7,977.02` | `1319.72` | `1330.80` | `5466.22` | -85,165.43 USD | `-0.80%` | `10X Cross` |
| `220` | `0x880a...311c` | `SHORT` | 10,255,080.57 USD | `7,707.11` | `1367.50` | `1330.80` | `2299.35` | 284,403.64 USD | `+2.77%` | `10X Cross` |
| `267` | `0x2b61...2f6c` | `LONG` | 9,056,713.50 USD | `6,807.00` | `1453.56` | `1330.80` | `645.50` | -837,637.72 USD | `-9.25%` | `10X Cross` |
| `283` | `0x2ae5...83e7` | `LONG` | 8,568,024.48 USD | `6,436.80` | `1391.82` | `1330.80` | `0.000000` | -390,867.51 USD | `-4.56%` | `2X Cross` |
| `320` | `0xecb6...2b00` | `SHORT` | 7,729,300.26 USD | `5,809.32` | `1324.06` | `1330.80` | `6007.23` | -37,438.64 USD | `-0.48%` | `5X Cross` |
| `331` | `0x26b6...9a13` | `LONG` | 7,229,577.76 USD | `5,433.73` | `1282.23` | `1330.80` | `202.80` | 262,274.53 USD | `+3.63%` | `10X Cross` |
| `342` | `0x45d2...4029` | `SHORT` | 6,957,659.70 USD | `5,227.00` | `833.44` | `1330.80` | `7955.79` | -2,601,281.73 USD | `-37.39%` | `5X Cross` |
| `361` | `0xea00...a918` | `LONG` | 6,650,000.00 USD | `5,000.00` | `739.16` | `1330.80` | `0.000000` | 2,954,184.89 USD | `+44.42%` | `5X Cross` |
| `376` | `0xdd7a...8830` | `LONG` | 6,463,080.66 USD | `4,860.19` | `897.48` | `1330.80` | `801.61` | 2,101,176.99 USD | `+32.51%` | `10X Cross` |
| `381` | `0xf081...e39e` | `LONG` | 6,288,232.70 USD | `4,717.00` | `1195.70` | `1330.80` | `1200.07` | 648,108.66 USD | `+10.31%` | `10X Cross` |
| `438` | `0x4cae...7c34` | `LONG` | 5,327,800.98 USD | `4,004.36` | `999.34` | `1330.80` | `711.33` | 1,326,072.82 USD | `+24.89%` | `10X Cross` |
| `452` | `0xa61c...66b9` | `LONG` | 5,170,262.40 USD | `3,888.00` | `1148.34` | `1330.80` | `0.000000` | 705,520.26 USD | `+13.65%` | `10X Cross` |
| `469` | `0x9aa5...58af` | `SHORT` | 4,950,616.52 USD | `3,720.31` | `1205.51` | `1330.80` | `3285.87` | -465,729.72 USD | `-9.41%` | `10X Cross` |
| `473` | `0x0153...8052` | `SHORT` | 4,920,798.31 USD | `3,698.18` | `1307.82` | `1330.80` | `2504.67` | -84,227.56 USD | `-1.71%` | `1X Isolated` |
| `505` | `0xd4c1...3d1d` | `SHORT` | 4,610,329.41 USD | `3,464.85` | `1302.96` | `1330.80` | `2639.57` | -95,753.27 USD | `-2.08%` | `10X Cross` |
| `528` | `0x382b...3e39` | `LONG` | 4,343,181.50 USD | `3,265.55` | `1166.49` | `1330.80` | `0.000000` | 533,947.65 USD | `+12.29%` | `10X Cross` |
| `530` | `0xd21d...90f1` | `LONG` | 4,322,500.00 USD | `3,250.00` | `1253.64` | `1330.80` | `875.86` | 248,158.27 USD | `+5.74%` | `4X Isolated` |
| `546` | `0x1338...c48e` | `LONG` | 4,198,505.13 USD | `3,149.43` | `1018.52` | `1330.80` | `820.16` | 990,759.59 USD | `+23.60%` | `4X Isolated` |
| `553` | `0x456f...cdf1` | `LONG` | 4,153,251.10 USD | `3,122.98` | `1268.03` | `1330.80` | `490.15` | 193,226.86 USD | `+4.65%` | `10X Cross` |
| `561` | `0xdbe0...d6d5` | `LONG` | 4,105,393.32 USD | `3,085.37` | `422.97` | `1330.80` | `338.47` | 2,800,388.83 USD | `+68.21%` | `3X Isolated` |
| `581` | `0x9c06...0560` | `SHORT` | 3,978,825.84 USD | `2,989.80` | `786.00` | `1330.80` | `2359.76` | -1,628,830.84 USD | `-40.94%` | `10X Cross` |
| `600` | `0x27c9...d65d` | `SHORT` | 3,876,198.87 USD | `2,913.34` | `1248.26` | `1330.80` | `1833.60` | -239,601.33 USD | `-6.18%` | `10X Cross` |
| `680` | `0xac48...3201` | `LONG` | 3,378,344.97 USD | `2,540.30` | `1393.86` | `1330.80` | `524.44` | -162,484.32 USD | `-4.81%` | `10X Cross` |
| `682` | `0xa183...0482` | `LONG` | 3,373,007.40 USD | `2,534.00` | `530.25` | `1330.80` | `444.40` | 2,029,344.68 USD | `+60.16%` | `5X Isolated` |
| `694` | `0x0871...e927` | `LONG` | 3,326,250.00 USD | `2,500.00` | `1276.50` | `1330.80` | `0.000000` | 135,000.00 USD | `+4.06%` | `10X Cross` |
| `695` | `0x325e...9564` | `LONG` | 3,326,039.15 USD | `2,501.91` | `1306.24` | `1330.80` | `0.000000` | 57,945.25 USD | `+1.74%` | `10X Cross` |
| `706` | `0x9b86...6e6e` | `LONG` | 3,281,509.00 USD | `2,467.30` | `637.58` | `1330.80` | `889.62` | 1,708,409.40 USD | `+52.06%` | `3X Cross` |
| `725` | `0x2e30...4cb5` | `SHORT` | 3,219,426.62 USD | `2,419.53` | `1298.38` | `1330.80` | `3192.06` | -77,962.51 USD | `-2.42%` | `2X Cross` |
| `762` | `0xb2f7...af9f` | `SHORT` | 3,077,247.60 USD | `2,313.72` | `746.63` | `1330.80` | `4180.11` | -1,349,758.85 USD | `-43.86%` | `10X Cross` |
| `790` | `0xf48f...10fe` | `LONG` | 2,950,591.70 USD | `2,218.49` | `1517.87` | `1330.80` | `880.63` | -416,795.12 USD | `-14.13%` | `3X Cross` |
| `818` | `0x5bc4...3b0c` | `SHORT` | 2,833,825.60 USD | `2,130.74` | `1089.65` | `1330.80` | `3553.86` | -512,068.03 USD | `-18.07%` | `5X Cross` |
| `838` | `0x8de4...b9aa` | `SHORT` | 2,783,088.73 USD | `2,091.29` | `1331.35` | `1330.80` | `1689.79` | 1,150.97 USD | `+0.04%` | `3X Cross` |
| `844` | `0x4fe2...ac59` | `SHORT` | 2,755,188.10 USD | `2,071.57` | `1478.56` | `1330.80` | `1808.32` | 307,758.11 USD | `+11.17%` | `10X Cross` |
| `860` | `0x668c...ea2e` | `SHORT` | 2,661,400.00 USD | `2,000.00` | `1409.16` | `1330.80` | `2701.69` | 156,922.04 USD | `+5.90%` | `10X Cross` |
| `880` | `0x77ee...2902` | `SHORT` | 2,589,192.92 USD | `1,946.03` | `759.84` | `1330.80` | `5244.67` | -1,110,515.41 USD | `-42.89%` | `10X Cross` |
| `890` | `0x3e2f...b269` | `SHORT` | 2,565,356.97 USD | `1,925.51` | `1134.87` | `1330.80` | `2931.72` | -380,158.12 USD | `-14.82%` | `10X Cross` |
| `897` | `0xe097...d0fe` | `LONG` | 2,546,565.65 USD | `1,913.56` | `1261.17` | `1330.80` | `0.000000` | 133,239.48 USD | `+5.23%` | `10X Cross` |
| `907` | `0x4f12...618b` | `SHORT` | 2,522,052.40 USD | `1,896.28` | `1608.30` | `1330.80` | `2116.68` | 527,731.99 USD | `+20.92%` | `3X Cross` |
| `928` | `0x71d0...8c26` | `SHORT` | 2,437,599.74 USD | `1,831.68` | `1361.12` | `1330.80` | `5397.08` | 55,536.89 USD | `+2.28%` | `10X Cross` |
| `952` | `0x866d...d6e1` | `LONG` | 2,397,627.52 USD | `1,802.05` | `674.73` | `1330.80` | `75.77` | 1,181,726.21 USD | `+49.29%` | `10X Cross` |
| `985` | `0x2309...a2d9` | `LONG` | 2,329,217.36 USD | `1,750.37` | `1186.09` | `1330.80` | `802.40` | 253,123.25 USD | `+10.87%` | `8X Cross` |
| `998` | `0x023a...2355` | `SHORT` | 2,288,274.70 USD | `1,719.99` | `1313.29` | `1330.80` | `6039.09` | -29,433.15 USD | `-1.29%` | `10X Cross` |
| `1002` | `0x2edd...8179` | `SHORT` | 2,266,972.42 USD | `1,703.85` | `1261.18` | `1330.80` | `2940.45` | -118,110.53 USD | `-5.21%` | `10X Cross` |
| `1029` | `0x265e...7f70` | `LONG` | 2,198,135.59 USD | `1,651.74` | `1388.09` | `1330.80` | `0.000000` | -94,634.10 USD | `-4.31%` | `3X Cross` |
| `1038` | `0xa271...a3f7` | `LONG` | 2,169,801.90 USD | `1,631.43` | `1190.60` | `1330.80` | `910.25` | 227,420.10 USD | `+10.48%` | `4X Cross` |
| `1046` | `0x7f75...9edf` | `LONG` | 2,136,972.02 USD | `1,605.78` | `1199.97` | `1330.80` | `973.37` | 210,080.13 USD | `+9.83%` | `10X Cross` |
| `1050` | `0x6646...6de5` | `SHORT` | 2,129,280.00 USD | `1,600.00` | `660.64` | `1330.80` | `4864.15` | -1,072,255.03 USD | `-50.36%` | `10X Cross` |
| `1065` | `0xdf57...93f5` | `LONG` | 2,099,974.97 USD | `1,579.76` | `1218.38` | `1330.80` | `780.10` | 175,218.99 USD | `+8.34%` | `3X Isolated` |
| `1080` | `0xab59...59b5` | `LONG` | 2,081,875.60 USD | `1,565.32` | `1342.15` | `1330.80` | `790.04` | -19,019.62 USD | `-0.91%` | `10X Cross` |
| `1083` | `0xfe7c...b7ae` | `SHORT` | 2,078,111.70 USD | `1,562.49` | `1350.62` | `1330.80` | `6420.76` | 32,217.35 USD | `+1.55%` | `10X Cross` |
| `1087` | `0x634f...6951` | `LONG` | 2,066,732.40 USD | `1,553.00` | `1263.46` | `1330.80` | `1184.29` | 104,582.82 USD | `+5.06%` | `10X Cross` |
| `1097` | `0x3e47...aaf6` | `LONG` | 2,043,252.40 USD | `1,536.28` | `1277.06` | `1330.80` | `1013.68` | 81,330.31 USD | `+3.98%` | `10X Cross` |
| `1136` | `0xcf67...eb24` | `LONG` | 1,995,000.00 USD | `1,500.00` | `887.05` | `1330.80` | `514.67` | 664,428.63 USD | `+33.30%` | `10X Cross` |
| `1159` | `0x039c...0ebd` | `SHORT` | 1,969,791.95 USD | `1,480.49` | `1238.67` | `1330.80` | `3120.33` | -135,960.62 USD | `-6.90%` | `10X Cross` |
| `1161` | `0x4e23...20c3` | `LONG` | 1,969,467.63 USD | `1,482.14` | `1302.47` | `1330.80` | `0.000000` | 39,022.84 USD | `+1.98%` | `4X Cross` |
| `1185` | `0xfc27...9d9d` | `SHORT` | 1,928,852.46 USD | `1,449.72` | `1317.50` | `1330.80` | `10954.45` | -18,851.80 USD | `-0.98%` | `10X Cross` |
| `1239` | `0x2ab7...c2f8` | `LONG` | 1,863,378.55 USD | `1,400.51` | `813.26` | `1330.80` | `794.27` | 724,396.87 USD | `+38.88%` | `3X Cross` |
| `1251` | `0x11be...8b1d` | `LONG` | 1,829,716.32 USD | `1,375.83` | `1206.55` | `1330.80` | `1134.38` | 169,708.36 USD | `+9.28%` | `10X Isolated` |
| `1307` | `0xef96...9383` | `SHORT` | 1,741,515.89 USD | `1,308.82` | `1249.96` | `1330.80` | `4124.60` | -105,549.47 USD | `-6.06%` | `10X Cross` |
| `1316` | `0xdf83...3cff` | `SHORT` | 1,723,729.27 USD | `1,295.55` | `1245.14` | `1330.80` | `1862.08` | -110,587.07 USD | `-6.42%` | `10X Cross` |
| `1350` | `0xe065...0f85` | `SHORT` | 1,679,271.30 USD | `1,262.61` | `1087.02` | `1330.80` | `1737.58` | -306,795.17 USD | `-18.27%` | `10X Cross` |
| `1374` | `0x7277...0b98` | `SHORT` | 1,641,632.33 USD | `1,234.96` | `1298.48` | `1330.80` | `2347.77` | -38,062.91 USD | `-2.32%` | `10X Cross` |
| `1427` | `0x5975...9abd` | `LONG` | 1,595,880.00 USD | `1,200.00` | `1179.54` | `1330.80` | `292.56` | 180,437.21 USD | `+11.31%` | `5X Cross` |
| `1469` | `0x69cc...14fd` | `SHORT` | 1,543,215.17 USD | `1,161.36` | `675.33` | `1330.80` | `7853.23` | -758,909.64 USD | `-49.18%` | `10X Cross` |
| `1470` | `0x7a76...b16d` | `LONG` | 1,543,132.50 USD | `1,160.25` | `1358.50` | `1330.80` | `1228.47` | -33,067.34 USD | `-2.14%` | `10X Cross` |
| `1487` | `0x3fc5...c0c1` | `SHORT` | 1,527,310.36 USD | `1,148.44` | `1264.34` | `1330.80` | `3053.81` | -75,296.58 USD | `-4.93%` | `10X Cross` |
| `1505` | `0xe35c...a1d3` | `LONG` | 1,498,764.39 USD | `1,127.06` | `1318.20` | `1330.80` | `694.30` | 13,069.04 USD | `+0.87%` | `2X Isolated` |
| `1511` | `0x5f94...4b96` | `LONG` | 1,483,309.10 USD | `1,115.27` | `538.00` | `1330.80` | `0.000000` | 883,291.46 USD | `+59.55%` | `10X Cross` |
| `1526` | `0x71df...a23d` | `SHORT` | 1,461,261.54 USD | `1,098.28` | `513.50` | `1330.80` | `2545.60` | -897,291.35 USD | `-61.41%` | `2X Cross` |
| `1559` | `0xbfc7...80b4` | `SHORT` | 1,430,502.50 USD | `1,075.00` | `558.03` | `1330.80` | `5321.93` | -830,623.77 USD | `-58.07%` | `10X Cross` |
| `1600` | `0x51f6...2b39` | `SHORT` | 1,384,184.27 USD | `1,039.88` | `1302.72` | `1330.80` | `2848.10` | -29,507.46 USD | `-2.13%` | `10X Cross` |
| `1635` | `0x123d...3bff` | `SHORT` | 1,340,738.69 USD | `1,008.15` | `489.25` | `1330.80` | `4171.37` | -847,504.61 USD | `-63.21%` | `10X Cross` |
| `1642` | `0x266b...efcb` | `LONG` | 1,330,800.00 USD | `1,000.00` | `826.11` | `1330.80` | `148.69` | 504,687.07 USD | `+37.92%` | `10X Cross` |
| `1643` | `0xb5ff...d912` | `LONG` | 1,330,800.00 USD | `1,000.00` | `1141.93` | `1330.80` | `400.42` | 188,869.70 USD | `+14.19%` | `2X Cross` |
| `1646` | `0x0748...d4b2` | `LONG` | 1,329,972.50 USD | `1,000.00` | `1334.09` | `1330.80` | `0.000000` | -4,115.80 USD | `-0.31%` | `7X Cross` |
| `1647` | `0xe282...df29` | `LONG` | 1,329,800.00 USD | `1,000.00` | `420.99` | `1330.80` | `99.38` | 908,813.14 USD | `+68.34%` | `10X Cross` |
| `1670` | `0x17f0...094f` | `LONG` | 1,309,611.15 USD | `984.30` | `1287.23` | `1330.80` | `536.73` | 42,590.99 USD | `+3.25%` | `5X Cross` |
| `1744` | `0x757d...94ba` | `LONG` | 1,230,224.56 USD | `925.00` | `1558.31` | `1330.80` | `0.000000` | -211,216.02 USD | `-17.17%` | `10X Cross` |
| `1805` | `0xf096...7553` | `SHORT` | 1,172,527.96 USD | `881.07` | `1240.34` | `1330.80` | `3465.91` | -79,697.87 USD | `-6.80%` | `10X Cross` |
| `1809` | `0xdf95...7d72` | `SHORT` | 1,170,959.75 USD | `880.09` | `1073.73` | `1330.80` | `41054.47` | -225,982.24 USD | `-19.30%` | `10X Cross` |
| `1820` | `0x2847...d47b` | `LONG` | 1,161,600.49 USD | `872.99` | `1236.61` | `1330.80` | `0.000000` | 82,048.60 USD | `+7.06%` | `5X Cross` |
| `1821` | `0xcf0a...856f` | `LONG` | 1,159,326.42 USD | `871.15` | `1292.19` | `1330.80` | `938.44` | 33,631.57 USD | `+2.90%` | `4X Cross` |
| `1824` | `0x3205...40bb` | `SHORT` | 1,156,690.58 USD | `869.30` | `1339.90` | `1330.80` | `2836.02` | 8,086.98 USD | `+0.70%` | `10X Cross` |
| `1854` | `0x7d0f...ea35` | `LONG` | 1,131,180.00 USD | `850.00` | `1317.57` | `1330.80` | `1275.61` | 11,244.42 USD | `+0.99%` | `10X Cross` |
| `1885` | `0x601c...4f54` | `SHORT` | 1,096,890.81 USD | `824.42` | `615.11` | `1330.80` | `2903.60` | -589,778.06 USD | `-53.77%` | `5X Cross` |
| `1892` | `0xae55...2236` | `LONG` | 1,088,543.05 USD | `817.47` | `1467.80` | `1330.80` | `0.000000` | -111,338.16 USD | `-10.23%` | `10X Cross` |
| `1903` | `0x71b1...79c8` | `LONG` | 1,080,164.09 USD | `812.52` | `1231.55` | `1330.80` | `688.71` | 79,508.63 USD | `+7.36%` | `10X Cross` |
| `1924` | `0x9b0f...db40` | `LONG` | 1,065,280.00 USD | `800.00` | `1268.86` | `1330.80` | `774.45` | 50,190.24 USD | `+4.71%` | `10X Cross` |
| `1926` | `0x0f02...5384` | `LONG` | 1,064,076.46 USD | `800.78` | `1290.36` | `1330.80` | `290.24` | 30,782.40 USD | `+2.89%` | `3X Cross` |
| `1927` | `0xea0f...4e73` | `LONG` | 1,063,840.00 USD | `800.00` | `1364.27` | `1330.80` | `572.78` | -27,578.68 USD | `-2.59%` | `10X Cross` |
| `1936` | `0xabdb...84ac` | `LONG` | 1,056,163.28 USD | `793.69` | `711.79` | `1330.80` | `664.30` | 491,222.92 USD | `+46.51%` | `3X Cross` |
| `1945` | `0xfdf8...e381` | `LONG` | 1,051,582.31 USD | `790.01` | `1337.72` | `1330.80` | `322.28` | -5,227.37 USD | `-0.50%` | `10X Cross` |
| `1999` | `0x0c1f...1d39` | `SHORT` | 1,014,624.10 USD | `762.99` | `1299.17` | `1330.80` | `4746.93` | -23,373.02 USD | `-2.30%` | `10X Cross` |
| `2000` | `0xf6f3...47f8` | `SHORT` | 1,013,268.89 USD | `761.57` | `1253.10` | `1330.80` | `2354.80` | -58,945.89 USD | `-5.82%` | `5X Cross` |
| `2006` | `0x389a...e76b` | `LONG` | 1,010,972.90 USD | `760.13` | `1266.20` | `1330.80` | `370.51` | 48,499.48 USD | `+4.80%` | `10X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `1297.10` | 194.56 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Long: 0.19K USD at 1297.1000 USD [API] | `2026-10-27 15:46:39` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`1404.15` (Vol: 3,000,000.00 USD, Dist: `+6.02%`) | Long MP=`1287.60` (Vol: 2,300,000.00 USD, Dist: `--2.78%`)
  * 48H Horizon: Short MP=`1404.15` (Vol: 3,000,000.00 USD, Dist: `+6.02%`) | Long MP=`1287.60` (Vol: 2,300,000.00 USD, Dist: `--2.78%`)
  * 3D Horizon: Short MP=`1404.42` (Vol: 3,000,000.00 USD, Dist: `+6.04%`) | Long MP=`1228.81` (Vol: 2,600,000.00 USD, Dist: `--7.22%`)
  * 7D Horizon: Short MP=`1404.10` (Vol: 3,000,000.00 USD, Dist: `+6.02%`) | Long MP=`1200.46` (Vol: 3,000,000.00 USD, Dist: `--9.36%`)
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
  * Current Rate: `98.95K` | Last 24h: `32.07K` | Last 3d: `282.84K` | Last 7d: `777.72K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0100%` | **USDT OKX** | `0.0100%` |
| **USDT Bybit** | `0.0100%` | **USDT KuCoin** | `0.0100%` |
| **USDT MEXC** | `0.0100%` | **USDT BingX** | `0.0080%` |
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
| `0:00 UTC` | `1369.95` | `1375.81` | `1369.95` | `1397.55` | `1350.75` | 159,915,504.01 USD | 87,974,917.65 USD | 71,940,586.35 USD | 16,034,331.30 USD | `+10.03%` | `21B / 3S` |
| `5:00 UTC` | `1359.75` | `1358.32` | `1359.75` | `1373.25` | `1346.25` | 77,512,400.13 USD | 36,921,415.88 USD | 40,590,984.25 USD | -3,669,568.36 USD | `-4.73%` | `4B / 13S` |
| `0:00 UTC` | `1353.15` | `1350.71` | `1353.15` | `1361.25` | `1341.75` | 52,010,841.39 USD | 26,247,439.78 USD | 25,763,401.61 USD | 484,038.17 USD | `+0.93%` | `5B / 3S` |
| `5:00 UTC` | `1343.25` | `1344.85` | `1343.25` | `1353.45` | `1340.25` | 26,552,172.39 USD | 11,915,117.49 USD | 14,637,054.90 USD | -2,721,937.40 USD | `-10.25%` | `0B / 9S` |
| `0:00 UTC` | `1342.95` | `1346.21` | `1342.95` | `1354.05` | `1340.25` | 27,005,669.33 USD | 14,153,013.83 USD | 12,852,655.50 USD | 1,300,358.33 USD | `+4.82%` | `5B / 3S` |
| `5:00 UTC` | `1348.65` | `1350.13` | `1348.65` | `1356.15` | `1344.45` | 21,612,679.16 USD | 11,526,731.97 USD | 10,085,947.19 USD | 1,440,784.78 USD | `+6.67%` | `2B / 2S` |
| `0:00 UTC` | `1335.45` | `1342.97` | `1335.45` | `1354.95` | `1333.05` | 31,234,081.19 USD | 13,144,149.56 USD | 18,089,931.62 USD | -4,945,782.06 USD | `-15.83%` | `2B / 7S` |
| `5:00 UTC` | `1333.95` | `1332.65` | `1333.95` | `1338.15` | `1327.05` | 42,051,592.22 USD | 20,998,597.47 USD | 21,052,994.75 USD | -54,397.28 USD | `-0.13%` | `1B / 3S` |
| `0:00 UTC` | `1324.05` | `1326.61` | `1324.05` | `1336.05` | `1320.15` | 35,175,848.19 USD | 15,805,961.43 USD | 19,369,886.76 USD | -3,563,925.33 USD | `-10.13%` | `1B / 10S` |
| `5:00 UTC` | `1329.15` | `1327.73` | `1329.15` | `1333.35` | `1322.25` | 17,465,396.57 USD | 7,290,777.54 USD | 10,174,619.04 USD | -2,883,841.50 USD | `-16.51%` | `3B / 6S` |

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
  * `2026-10-29 23:31:26 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:26:26 IST`: [@DeItaone] - (Sentiment: `Neutral`)
  * `2026-10-29 23:03:26 IST`: [@mb_ghalibaf] - (Sentiment: `Neutral`)
  * `2026-10-29 23:01:26 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-29 22:55:26 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-29 23:51:26 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:51:26 IST`: [fxstreet.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:50:26 IST`: [ForexFactory] - (Sentiment: `Neutral`)
  * `2026-10-29 23:50:26 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-29 23:50:26 IST`: [youtube.com/bankofcanadaofficial] - (Sentiment: `Neutral`)
  * `2026-10-29 20:52:26 IST`: [notayesmanseconomics.wordpress.com] - (Sentiment: `Neutral`)
  * `2026-10-29 20:52:26 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 20:52:26 IST`: [breakingthenews.net] - (Sentiment: `Neutral`)
  * `2026-10-29 19:52:26 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-29 19:52:26 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)


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
