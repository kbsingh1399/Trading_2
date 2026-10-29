# 🏛️ SOVEREIGN CANDIDATE DOSSIER: ZECUSD
**Canonical Key**: `ZECUSD` | **Broker Instrument**: `ZECUSD.p` | **Asset Class**: `Crypto Altcoin`
**Timestamp**: `2026-10-30 00:05:06 IST` (`2026-10-29 18:35:06 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `1323.08` | **Live Ask Quote**: `1323.93` | **Mid Price**: `1323.51`
- **Spread Points**: `85.00` | **Spread BPS**: `6.42 bps` (Charter Threshold: `25.00 bps`)
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
  * Value Area High (VAH) = `1304.92` (Distance: `+1.38%`)
  * Point of Control (POC) = `1247.20` (Distance: `+6.07%`)
  * Value Area Low (VAL) = `1230.55` (Distance: `+7.51%`)
  * Auction Positioning: `ABOVE_VALUE (Imbalance)` | Session Bias: **`BULLISH (Above Pivot)`** | Market Regime: `RANGE_EXPANSION`
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
  * Golden Pocket Zone (0.618 - 0.650): `1318.21` - `1328.80`
  * Optimal Trade Entry (OTE 0.705): `1326.15`
  * Structural Invalidation Anchor (0.786): `1334.09`

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
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-29 23:55:43 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `16` | `0xb83d...6e36` | `SHORT` | 69,571,932.21 USD | `52,582.52` | `1336.45` | `1323.30` | `3695.07` | 701,982.68 USD | `+1.01%` | `3X Cross` |
| `23` | `0x5b5d...c060` | `SHORT` | 53,931,501.16 USD | `40,727.61` | `1478.36` | `1323.30` | `4976.74` | 6,278,763.03 USD | `+11.64%` | `3X Cross` |
| `42` | `0x7fda...17d1` | `SHORT` | 29,723,652.70 USD | `22,458.37` | `1261.40` | `1323.30` | `2826.29` | -1,394,729.55 USD | `-4.69%` | `5X Cross` |
| `77` | `0x60b0...991e` | `LONG` | 22,207,985.89 USD | `16,779.74` | `1179.65` | `1323.30` | `884.47` | 2,413,738.88 USD | `+10.87%` | `10X Cross` |
| `82` | `0xbf73...5d58` | `LONG` | 21,185,600.00 USD | `16,000.00` | `1214.30` | `1323.30` | `710.89` | 1,756,767.75 USD | `+8.29%` | `10X Cross` |
| `133` | `0xc36a...105b` | `LONG` | 15,234,570.27 USD | `11,510.82` | `1215.14` | `1323.30` | `929.78` | 1,247,289.24 USD | `+8.19%` | `10X Cross` |
| `157` | `0x9071...5c0b` | `LONG` | 13,400,824.55 USD | `10,119.94` | `1370.53` | `1323.30` | `505.81` | -468,846.48 USD | `-3.50%` | `2X Cross` |
| `171` | `0x8742...8427` | `LONG` | 12,160,319.14 USD | `9,201.21` | `1286.37` | `1323.30` | `698.34` | 324,149.14 USD | `+2.67%` | `10X Cross` |
| `192` | `0xad59...ba81` | `SHORT` | 11,147,117.50 USD | `8,425.00` | `330.91` | `1323.30` | `2139.31` | -8,359,159.73 USD | `-74.99%` | `10X Cross` |
| `199` | `0xdd53...2b13` | `SHORT` | 10,896,931.37 USD | `8,233.42` | `739.37` | `1323.30` | `7811.71` | -4,809,364.12 USD | `-44.14%` | `3X Cross` |
| `202` | `0x9ffd...ce40` | `LONG` | 10,865,484.74 USD | `8,205.32` | `1252.74` | `1323.30` | `569.61` | 586,376.62 USD | `+5.40%` | `5X Cross` |
| `208` | `0xfc66...ca06` | `SHORT` | 10,528,240.86 USD | `7,967.02` | `1319.72` | `1323.30` | `5475.62` | -13,976.11 USD | `-0.13%` | `10X Cross` |
| `221` | `0x880a...311c` | `SHORT` | 10,187,258.00 USD | `7,707.11` | `1367.50` | `1323.30` | `2299.20` | 352,226.20 USD | `+3.46%` | `10X Cross` |
| `268` | `0x2b61...2f6c` | `LONG` | 8,997,492.60 USD | `6,807.00` | `1453.56` | `1323.30` | `639.09` | -896,858.62 USD | `-9.97%` | `10X Cross` |
| `285` | `0x2ae5...83e7` | `LONG` | 8,506,874.88 USD | `6,436.80` | `1391.82` | `1323.30` | `0.000000` | -452,017.11 USD | `-5.31%` | `2X Cross` |
| `322` | `0xecb6...2b00` | `SHORT` | 7,617,222.14 USD | `5,752.32` | `1324.06` | `1323.30` | `5798.08` | -831.68 USD | `-0.01%` | `5X Cross` |
| `332` | `0x26b6...9a13` | `LONG` | 7,181,217.57 USD | `5,433.73` | `1282.23` | `1323.30` | `204.70` | 213,914.33 USD | `+2.98%` | `10X Cross` |
| `344` | `0x45d2...4029` | `SHORT` | 6,908,003.20 USD | `5,227.00` | `833.44` | `1323.30` | `7959.51` | -2,551,625.23 USD | `-36.94%` | `5X Cross` |
| `366` | `0xea00...a918` | `LONG` | 6,623,500.00 USD | `5,000.00` | `739.16` | `1323.30` | `0.000000` | 2,927,684.89 USD | `+44.20%` | `5X Cross` |
| `379` | `0xdd7a...8830` | `LONG` | 6,430,031.37 USD | `4,860.19` | `897.48` | `1323.30` | `801.89` | 2,068,127.70 USD | `+32.16%` | `10X Cross` |
| `387` | `0xf081...e39e` | `LONG` | 6,233,987.20 USD | `4,717.00` | `1195.70` | `1323.30` | `1200.07` | 593,863.16 USD | `+9.53%` | `10X Cross` |
| `438` | `0x4cae...7c34` | `LONG` | 5,292,162.18 USD | `4,004.36` | `999.34` | `1323.30` | `722.12` | 1,290,434.02 USD | `+24.38%` | `10X Cross` |
| `452` | `0xa61c...66b9` | `LONG` | 5,143,824.00 USD | `3,888.00` | `1148.34` | `1323.30` | `0.000000` | 679,081.86 USD | `+13.20%` | `10X Cross` |
| `472` | `0x9aa5...58af` | `SHORT` | 4,924,946.38 USD | `3,720.31` | `1205.51` | `1323.30` | `3301.00` | -440,059.58 USD | `-8.94%` | `10X Cross` |
| `476` | `0x0153...8052` | `SHORT` | 4,887,514.69 USD | `3,698.18` | `1307.82` | `1323.30` | `2504.67` | -50,943.94 USD | `-1.04%` | `1X Isolated` |
| `503` | `0xd4c1...3d1d` | `SHORT` | 4,583,518.73 USD | `3,463.18` | `1302.96` | `1323.30` | `2652.87` | -71,118.54 USD | `-1.55%` | `10X Cross` |
| `528` | `0x382b...3e39` | `LONG` | 4,319,881.81 USD | `3,264.97` | `1166.49` | `1323.30` | `0.000000` | 511,324.52 USD | `+11.84%` | `10X Cross` |
| `532` | `0xd21d...90f1` | `LONG` | 4,300,075.00 USD | `3,250.00` | `1253.64` | `1323.30` | `875.86` | 225,733.27 USD | `+5.25%` | `4X Isolated` |
| `548` | `0x1338...c48e` | `LONG` | 4,161,902.14 USD | `3,149.43` | `1018.52` | `1323.30` | `820.16` | 954,156.60 USD | `+22.93%` | `4X Isolated` |
| `552` | `0x456f...cdf1` | `LONG` | 4,147,919.39 USD | `3,134.29` | `1268.23` | `1323.30` | `493.42` | 172,912.79 USD | `+4.17%` | `10X Cross` |
| `564` | `0xdbe0...d6d5` | `LONG` | 4,077,624.99 USD | `3,085.37` | `422.97` | `1323.30` | `338.47` | 2,772,620.50 USD | `+68.00%` | `3X Isolated` |
| `585` | `0x9c06...0560` | `SHORT` | 3,958,794.18 USD | `2,989.80` | `786.00` | `1323.30` | `2362.53` | -1,608,799.18 USD | `-40.64%` | `10X Cross` |
| `601` | `0x27c9...d65d` | `SHORT` | 3,854,812.87 USD | `2,912.59` | `1248.26` | `1323.30` | `1835.38` | -219,151.52 USD | `-5.69%` | `10X Cross` |
| `684` | `0xac48...3201` | `LONG` | 3,362,087.05 USD | `2,540.30` | `1393.86` | `1323.30` | `525.55` | -178,742.24 USD | `-5.32%` | `10X Cross` |
| `689` | `0xa183...0482` | `LONG` | 3,348,934.40 USD | `2,534.00` | `530.25` | `1323.30` | `444.40` | 2,005,271.68 USD | `+59.88%` | `5X Isolated` |
| `696` | `0x325e...9564` | `LONG` | 3,310,026.93 USD | `2,501.91` | `1306.24` | `1323.30` | `0.000000` | 41,933.03 USD | `+1.27%` | `10X Cross` |
| `699` | `0x0871...e927` | `LONG` | 3,304,500.00 USD | `2,500.00` | `1276.50` | `1323.30` | `0.000000` | 113,250.00 USD | `+3.43%` | `10X Cross` |
| `706` | `0x9b86...6e6e` | `LONG` | 3,264,484.63 USD | `2,467.30` | `637.58` | `1323.30` | `889.62` | 1,691,385.03 USD | `+51.81%` | `3X Cross` |
| `730` | `0x2e30...4cb5` | `SHORT` | 3,197,650.85 USD | `2,419.53` | `1298.38` | `1323.30` | `3194.99` | -56,186.74 USD | `-1.76%` | `2X Cross` |
| `770` | `0xb2f7...af9f` | `SHORT` | 3,061,282.93 USD | `2,313.72` | `746.63` | `1323.30` | `4185.64` | -1,333,794.19 USD | `-43.57%` | `10X Cross` |
| `801` | `0xf48f...10fe` | `LONG` | 2,935,284.12 USD | `2,218.49` | `1517.87` | `1323.30` | `887.55` | -432,102.71 USD | `-14.72%` | `3X Cross` |
| `827` | `0x5bc4...3b0c` | `SHORT` | 2,816,199.06 USD | `2,130.74` | `1089.65` | `1323.30` | `3560.10` | -494,441.48 USD | `-17.56%` | `5X Cross` |
| `844` | `0x8de4...b9aa` | `SHORT` | 2,769,286.22 USD | `2,091.29` | `1331.35` | `1323.30` | `1689.79` | 14,953.49 USD | `+0.54%` | `3X Cross` |
| `849` | `0x4fe2...ac59` | `SHORT` | 2,742,758.68 USD | `2,071.57` | `1478.56` | `1323.30` | `1805.64` | 320,187.53 USD | `+11.67%` | `10X Cross` |
| `866` | `0x668c...ea2e` | `SHORT` | 2,647,600.00 USD | `2,000.00` | `1409.16` | `1323.30` | `2701.78` | 170,722.04 USD | `+6.45%` | `10X Cross` |
| `890` | `0x77ee...2902` | `SHORT` | 2,572,262.45 USD | `1,946.03` | `759.84` | `1323.30` | `5234.71` | -1,093,584.95 USD | `-42.51%` | `10X Cross` |
| `900` | `0x3e2f...b269` | `SHORT` | 2,544,946.57 USD | `1,925.51` | `1134.87` | `1323.30` | `2931.72` | -359,747.71 USD | `-14.14%` | `10X Cross` |
| `908` | `0xe097...d0fe` | `LONG` | 2,528,960.90 USD | `1,913.56` | `1261.17` | `1323.30` | `0.000000` | 115,634.73 USD | `+4.57%` | `10X Cross` |
| `913` | `0x4f12...618b` | `SHORT` | 2,511,053.98 USD | `1,896.28` | `1608.30` | `1323.30` | `2116.68` | 538,730.41 USD | `+21.45%` | `3X Cross` |
| `953` | `0x866d...d6e1` | `LONG` | 2,381,589.28 USD | `1,802.05` | `674.73` | `1323.30` | `79.72` | 1,165,687.97 USD | `+48.95%` | `10X Cross` |
| `988` | `0x2309...a2d9` | `LONG` | 2,317,139.81 USD | `1,750.37` | `1186.09` | `1323.30` | `802.96` | 241,045.70 USD | `+10.40%` | `8X Cross` |
| `1001` | `0x023a...2355` | `SHORT` | 2,265,848.44 USD | `1,712.53` | `1313.29` | `1323.30` | `6048.71` | -16,804.02 USD | `-0.74%` | `10X Cross` |
| `1009` | `0x2edd...8179` | `SHORT` | 2,246,945.65 USD | `1,697.73` | `1261.18` | `1323.30` | `2954.03` | -105,802.19 USD | `-4.71%` | `10X Cross` |
| `1031` | `0x265e...7f70` | `LONG` | 2,187,234.11 USD | `1,651.74` | `1388.09` | `1323.30` | `0.000000` | -105,535.58 USD | `-4.83%` | `3X Cross` |
| `1042` | `0xa271...a3f7` | `LONG` | 2,160,013.32 USD | `1,631.43` | `1190.60` | `1323.30` | `910.25` | 217,631.52 USD | `+10.08%` | `4X Cross` |
| `1044` | `0x71d0...8c26` | `SHORT` | 2,151,897.20 USD | `1,625.30` | `1361.12` | `1323.30` | `5913.09` | 60,331.45 USD | `+2.80%` | `10X Cross` |
| `1055` | `0x7f75...9edf` | `LONG` | 2,125,249.83 USD | `1,605.78` | `1199.97` | `1323.30` | `973.45` | 198,357.94 USD | `+9.33%` | `10X Cross` |
| `1060` | `0x6646...6de5` | `SHORT` | 2,114,560.00 USD | `1,600.00` | `660.64` | `1323.30` | `4836.00` | -1,057,535.03 USD | `-50.01%` | `10X Cross` |
| `1074` | `0xdf57...93f5` | `LONG` | 2,088,284.74 USD | `1,579.76` | `1218.38` | `1323.30` | `780.10` | 163,528.76 USD | `+7.83%` | `3X Isolated` |
| `1087` | `0xab59...59b5` | `LONG` | 2,071,701.02 USD | `1,565.32` | `1342.15` | `1323.30` | `789.75` | -29,194.20 USD | `-1.41%` | `10X Cross` |
| `1090` | `0xfe7c...b7ae` | `SHORT` | 2,067,955.51 USD | `1,562.49` | `1350.62` | `1323.30` | `6443.11` | 42,373.53 USD | `+2.05%` | `10X Cross` |
| `1095` | `0x634f...6951` | `LONG` | 2,055,084.90 USD | `1,553.00` | `1263.46` | `1323.30` | `1184.29` | 92,935.32 USD | `+4.52%` | `10X Cross` |
| `1103` | `0x3e47...aaf6` | `LONG` | 2,033,266.58 USD | `1,536.28` | `1277.06` | `1323.30` | `1012.39` | 71,344.49 USD | `+3.51%` | `10X Cross` |
| `1145` | `0xcf67...eb24` | `LONG` | 1,986,000.00 USD | `1,500.00` | `887.05` | `1323.30` | `524.46` | 655,428.63 USD | `+33.00%` | `10X Cross` |
| `1166` | `0x4e23...20c3` | `LONG` | 1,960,278.36 USD | `1,482.14` | `1302.47` | `1323.30` | `0.000000` | 29,833.57 USD | `+1.52%` | `4X Cross` |
| `1169` | `0x039c...0ebd` | `SHORT` | 1,958,836.32 USD | `1,480.49` | `1238.67` | `1323.30` | `3127.95` | -125,005.00 USD | `-6.38%` | `10X Cross` |
| `1200` | `0xfc27...9d9d` | `SHORT` | 1,903,982.65 USD | `1,440.12` | `1317.50` | `1323.30` | `11071.33` | -6,629.95 USD | `-0.35%` | `10X Cross` |
| `1245` | `0x2ab7...c2f8` | `LONG` | 1,850,914.02 USD | `1,400.51` | `813.26` | `1323.30` | `794.09` | 711,932.33 USD | `+38.46%` | `3X Cross` |
| `1257` | `0x11be...8b1d` | `LONG` | 1,820,911.00 USD | `1,375.83` | `1206.55` | `1323.30` | `1134.38` | 160,903.05 USD | `+8.84%` | `10X Isolated` |
| `1314` | `0xef96...9383` | `SHORT` | 1,729,867.39 USD | `1,308.82` | `1249.96` | `1323.30` | `4146.72` | -93,900.97 USD | `-5.43%` | `10X Cross` |
| `1320` | `0xdf83...3cff` | `SHORT` | 1,714,142.21 USD | `1,295.55` | `1245.14` | `1323.30` | `1851.71` | -101,000.00 USD | `-5.89%` | `10X Cross` |
| `1358` | `0xe065...0f85` | `SHORT` | 1,671,064.33 USD | `1,262.61` | `1087.02` | `1323.30` | `1740.67` | -298,588.21 USD | `-17.87%` | `10X Cross` |
| `1382` | `0x7277...0b98` | `SHORT` | 1,632,493.62 USD | `1,234.96` | `1298.48` | `1323.30` | `2352.69` | -28,924.21 USD | `-1.77%` | `10X Cross` |
| `1433` | `0x5975...9abd` | `LONG` | 1,588,200.00 USD | `1,200.00` | `1179.54` | `1323.30` | `288.26` | 172,757.21 USD | `+10.88%` | `5X Cross` |
| `1476` | `0x69cc...14fd` | `SHORT` | 1,535,201.78 USD | `1,161.36` | `675.33` | `1323.30` | `7818.16` | -750,896.26 USD | `-48.91%` | `10X Cross` |
| `1479` | `0x7a76...b16d` | `LONG` | 1,533,830.14 USD | `1,159.27` | `1358.50` | `1323.30` | `1234.68` | -41,038.37 USD | `-2.68%` | `10X Cross` |
| `1490` | `0x3fc5...c0c1` | `SHORT` | 1,519,960.34 USD | `1,148.44` | `1264.34` | `1323.30` | `3065.51` | -67,946.56 USD | `-4.47%` | `10X Cross` |
| `1508` | `0xe35c...a1d3` | `LONG` | 1,491,100.38 USD | `1,127.06` | `1318.20` | `1323.30` | `694.30` | 5,405.03 USD | `+0.36%` | `2X Isolated` |
| `1518` | `0x5f94...4b96` | `LONG` | 1,475,613.74 USD | `1,115.27` | `538.00` | `1323.30` | `0.000000` | 875,596.10 USD | `+59.34%` | `10X Cross` |
| `1537` | `0x71df...a23d` | `SHORT` | 1,451,706.50 USD | `1,098.28` | `513.50` | `1323.30` | `2545.83` | -887,736.31 USD | `-61.15%` | `2X Cross` |
| `1564` | `0xbfc7...80b4` | `SHORT` | 1,423,085.00 USD | `1,075.00` | `558.03` | `1323.30` | `5369.74` | -823,206.27 USD | `-57.85%` | `10X Cross` |
| `1609` | `0x51f6...2b39` | `SHORT` | 1,374,305.41 USD | `1,039.88` | `1302.72` | `1323.30` | `2865.81` | -19,628.60 USD | `-1.43%` | `10X Cross` |
| `1636` | `0x123d...3bff` | `SHORT` | 1,334,286.52 USD | `1,008.15` | `489.25` | `1323.30` | `4171.60` | -841,052.45 USD | `-63.03%` | `10X Cross` |
| `1648` | `0x266b...efcb` | `LONG` | 1,324,400.00 USD | `1,000.00` | `826.11` | `1323.30` | `143.72` | 498,287.07 USD | `+37.62%` | `10X Cross` |
| `1649` | `0xe282...df29` | `LONG` | 1,323,000.00 USD | `1,000.00` | `420.99` | `1323.30` | `100.70` | 902,013.14 USD | `+68.18%` | `10X Cross` |
| `1650` | `0xb5ff...d912` | `LONG` | 1,321,600.00 USD | `1,000.00` | `1141.93` | `1323.30` | `400.42` | 179,669.70 USD | `+13.59%` | `2X Cross` |
| `1651` | `0x0748...d4b2` | `LONG` | 1,321,600.00 USD | `1,000.00` | `1334.09` | `1323.30` | `0.000000` | -12,488.30 USD | `-0.94%` | `7X Cross` |
| `1677` | `0x17f0...094f` | `LONG` | 1,300,850.88 USD | `984.30` | `1287.23` | `1323.30` | `536.73` | 33,830.72 USD | `+2.60%` | `5X Cross` |
| `1747` | `0x757d...94ba` | `LONG` | 1,222,572.50 USD | `925.00` | `1558.31` | `1323.30` | `0.000000` | -218,868.08 USD | `-17.90%` | `10X Cross` |
| `1810` | `0xf096...7553` | `SHORT` | 1,166,712.89 USD | `881.07` | `1240.34` | `1323.30` | `3472.46` | -73,882.81 USD | `-6.33%` | `10X Cross` |
| `1813` | `0xdf95...7d72` | `SHORT` | 1,164,940.69 USD | `880.33` | `1073.80` | `1323.30` | `41266.34` | -219,644.92 USD | `-18.85%` | `10X Cross` |
| `1819` | `0x2847...d47b` | `LONG` | 1,158,391.19 USD | `875.05` | `1236.83` | `1323.30` | `0.000000` | 76,106.36 USD | `+6.57%` | `5X Cross` |
| `1823` | `0xcf0a...856f` | `LONG` | 1,153,489.72 USD | `871.15` | `1292.19` | `1323.30` | `938.44` | 27,794.87 USD | `+2.41%` | `4X Cross` |
| `1852` | `0x7d0f...ea35` | `LONG` | 1,124,975.00 USD | `850.00` | `1317.57` | `1323.30` | `1275.61` | 5,039.42 USD | `+0.45%` | `10X Cross` |
| `1890` | `0x601c...4f54` | `SHORT` | 1,089,452.81 USD | `824.42` | `615.11` | `1323.30` | `2911.14` | -582,340.06 USD | `-53.45%` | `5X Cross` |
| `1900` | `0xae55...2236` | `LONG` | 1,080,368.35 USD | `817.47` | `1467.80` | `1323.30` | `0.000000` | -119,512.87 USD | `-11.06%` | `10X Cross` |
| `1904` | `0x71b1...79c8` | `LONG` | 1,074,638.95 USD | `812.52` | `1231.55` | `1323.30` | `701.44` | 73,983.50 USD | `+6.88%` | `10X Cross` |
| `1928` | `0x0f02...5384` | `LONG` | 1,058,551.08 USD | `800.78` | `1290.36` | `1323.30` | `287.33` | 25,257.01 USD | `+2.39%` | `3X Cross` |
| `1929` | `0xea0f...4e73` | `LONG` | 1,058,400.00 USD | `800.00` | `1364.27` | `1323.30` | `572.78` | -33,018.68 USD | `-3.12%` | `10X Cross` |
| `1931` | `0x9b0f...db40` | `LONG` | 1,057,280.00 USD | `800.00` | `1268.86` | `1323.30` | `774.98` | 42,190.24 USD | `+3.99%` | `10X Cross` |
| `1945` | `0xabdb...84ac` | `LONG` | 1,050,448.72 USD | `793.69` | `711.79` | `1323.30` | `664.30` | 485,508.35 USD | `+46.22%` | `3X Cross` |
| `1951` | `0xfdf8...e381` | `LONG` | 1,044,077.22 USD | `790.01` | `1337.72` | `1323.30` | `351.32` | -12,732.47 USD | `-1.22%` | `10X Cross` |
| `2006` | `0x0c1f...1d39` | `SHORT` | 1,008,596.48 USD | `762.99` | `1299.17` | `1323.30` | `4782.88` | -17,345.39 USD | `-1.72%` | `10X Cross` |
| `2009` | `0xf6f3...47f8` | `SHORT` | 1,006,490.91 USD | `761.57` | `1253.10` | `1323.30` | `2373.31` | -52,167.92 USD | `-5.18%` | `5X Cross` |
| `2011` | `0x389a...e76b` | `LONG` | 1,006,032.06 USD | `760.13` | `1266.20` | `1323.30` | `360.95` | 43,558.63 USD | `+4.33%` | `10X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `1297.10` | 194.56 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Long: 0.19K USD at 1297.1000 USD [API] | `2026-10-27 15:46:39` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`1404.15` (Vol: 3,000,000.00 USD, Dist: `+6.30%`) | Long MP=`1287.60` (Vol: 2,300,000.00 USD, Dist: `--2.52%`)
  * 48H Horizon: Short MP=`1404.15` (Vol: 3,000,000.00 USD, Dist: `+6.30%`) | Long MP=`1287.60` (Vol: 2,300,000.00 USD, Dist: `--2.52%`)
  * 3D Horizon: Short MP=`1404.42` (Vol: 3,000,000.00 USD, Dist: `+6.32%`) | Long MP=`1228.81` (Vol: 2,600,000.00 USD, Dist: `--6.97%`)
  * 7D Horizon: Short MP=`1404.10` (Vol: 3,000,000.00 USD, Dist: `+6.30%`) | Long MP=`1200.46` (Vol: 3,000,000.00 USD, Dist: `--9.12%`)
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
  * Current Rate: `96.87K` | Last 24h: `32.07K` | Last 3d: `282.84K` | Last 7d: `777.72K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0096%` | **USDT OKX** | `0.0100%` |
| **USDT Bybit** | `0.0100%` | **USDT KuCoin** | `0.0100%` |
| **USDT MEXC** | `0.0096%` | **USDT BingX** | `0.0078%` |
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
| `5:00 UTC` | `1359.75` | `1358.32` | `1359.75` | `1373.25` | `1346.25` | 77,512,400.13 USD | 36,921,415.88 USD | 40,590,984.25 USD | -3,669,568.36 USD | `-4.73%` | `4B / 13S` |
| `0:00 UTC` | `1353.15` | `1350.71` | `1353.15` | `1361.25` | `1341.75` | 52,010,841.39 USD | 26,247,439.78 USD | 25,763,401.61 USD | 484,038.17 USD | `+0.93%` | `5B / 3S` |
| `5:00 UTC` | `1343.25` | `1344.85` | `1343.25` | `1353.45` | `1340.25` | 26,552,172.39 USD | 11,915,117.49 USD | 14,637,054.90 USD | -2,721,937.40 USD | `-10.25%` | `0B / 9S` |
| `0:00 UTC` | `1342.95` | `1346.21` | `1342.95` | `1354.05` | `1340.25` | 27,005,669.33 USD | 14,153,013.83 USD | 12,852,655.50 USD | 1,300,358.33 USD | `+4.82%` | `5B / 3S` |
| `5:00 UTC` | `1348.65` | `1350.13` | `1348.65` | `1356.15` | `1344.45` | 21,612,679.16 USD | 11,526,731.97 USD | 10,085,947.19 USD | 1,440,784.78 USD | `+6.67%` | `2B / 2S` |
| `0:00 UTC` | `1335.45` | `1342.97` | `1335.45` | `1354.95` | `1333.05` | 31,234,081.19 USD | 13,144,149.56 USD | 18,089,931.62 USD | -4,945,782.06 USD | `-15.83%` | `2B / 7S` |
| `5:00 UTC` | `1333.95` | `1332.65` | `1333.95` | `1338.15` | `1327.05` | 42,051,592.22 USD | 20,998,597.47 USD | 21,052,994.75 USD | -54,397.28 USD | `-0.13%` | `1B / 3S` |
| `0:00 UTC` | `1324.05` | `1326.61` | `1324.05` | `1336.05` | `1320.15` | 35,175,848.19 USD | 15,805,961.43 USD | 19,369,886.76 USD | -3,563,925.33 USD | `-10.13%` | `1B / 10S` |
| `5:00 UTC` | `1321.35` | `1325.74` | `1321.35` | `1333.35` | `1318.35` | 26,289,288.34 USD | 11,537,630.34 USD | 14,751,657.99 USD | -3,214,027.65 USD | `-12.23%` | `3B / 5S` |
| `0:00 UTC` | `1315.95` | `1315.66` | `1315.95` | `1321.95` | `1311.75` | 16,218,798.47 USD | 6,090,298.21 USD | 10,128,500.27 USD | -4,038,202.06 USD | `-24.90%` | `4B / 6S` |

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
| `5m` | -29,640.00 USD | -2,080,000.00 USD | **`DISTRIBUTION`** |
| `15m` | 659,270.00 USD | -464,600.00 USD | **`ACCUMULATION`** |
| `30m` | 621,290.00 USD | -8,680,000.00 USD | **`DISTRIBUTION`** |
| `1h` | -421,950.00 USD | -20,270,000.00 USD | **`DISTRIBUTION`** |
| `2h` | 6,040,000.00 USD | -15,170,000.00 USD | **`DISTRIBUTION`** |
| `4h` | 26,560,000.00 USD | 83,770,000.00 USD | **`ACCUMULATION`** |
| `6h` | 30,130,000.00 USD | 90,750,000.00 USD | **`ACCUMULATION`** |
| `8h` | 33,220,000.00 USD | 103,500,000.00 USD | **`ACCUMULATION`** |
| `12h` | 27,590,000.00 USD | 108,940,000.00 USD | **`ACCUMULATION`** |
| `24h` | 14,530,000.00 USD | 86,920,000.00 USD | **`ACCUMULATION`** |
| `1w` | 54,110,000.00 USD | 246,640,000.00 USD | **`ACCUMULATION`** |
| `30d` | 66,780,000.00 USD | -542,610,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-29.64K` | 15m=`+659.27K` | 1h=`-421.95K` | 24h=`+14.53M`
* Futures Capital Netflows: 5m=`-2.08M` | 15m=`-464.60K` | 1h=`-20.27M` | 24h=`+86.92M`
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
  * `2026-10-29 23:31:27 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:26:27 IST`: [@DeItaone] - (Sentiment: `Neutral`)
  * `2026-10-29 23:03:27 IST`: [@mb_ghalibaf] - (Sentiment: `Neutral`)
  * `2026-10-30 00:01:27 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-30 00:01:27 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-30 00:01:27 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-30 00:01:27 IST`: [fxstreet.com] - (Sentiment: `Neutral`)
  * `2026-10-30 00:00:27 IST`: [ForexFactory] - (Sentiment: `Neutral`)
  * `2026-10-30 00:00:27 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 00:00:27 IST`: [youtube.com/bankofcanadaofficial] - (Sentiment: `Neutral`)
  * `2026-10-29 21:02:27 IST`: [notayesmanseconomics.wordpress.com] - (Sentiment: `Neutral`)
  * `2026-10-29 21:02:27 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 21:02:27 IST`: [breakingthenews.net] - (Sentiment: `Neutral`)
  * `2026-10-29 20:02:27 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-29 20:02:27 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)


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
  * Spread-Padded Stop Loss: `1208.78` (Risk Distance: `21.77` pts)
  * +2.5R Take Profit: `1284.96`
  * Mathematical Lot Sizing: **`0.45 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `1304.92` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `1326.69` (Risk Distance: `21.77` pts)
  * +2.5R Take Profit: `1250.51`
  * Mathematical Lot Sizing: **`0.45 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`1334.09`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
