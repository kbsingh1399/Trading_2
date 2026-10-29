# 🏛️ SOVEREIGN CANDIDATE DOSSIER: ZECUSD
**Canonical Key**: `ZECUSD` | **Broker Instrument**: `ZECUSD.p` | **Asset Class**: `Crypto Altcoin`
**Timestamp**: `2026-10-29 23:13:20 IST` (`2026-10-29 17:43:20 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `1347.54` | **Live Ask Quote**: `1348.39` | **Mid Price**: `1347.97`
- **Spread Points**: `85.00` | **Spread BPS**: `6.31 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `1347.97` | VWAP Z-Score: `+0.00` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `3.37` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `50.00` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `1357.40` | Lower -3.00σ Band: `1338.53`
  * Upper +2.51σ Band: `1355.38` | Lower -2.51σ Band: `1340.55`
  * Upper +2.01σ Band: `1353.63` | Lower -2.01σ Band: `1342.30`
  * Upper +2.00σ Band: `1353.36` | Lower -2.00σ Band: `1342.57`
  * Upper +1.28σ Band: `1351.74` | Lower -1.28σ Band: `1344.19`
  * Upper +1.00σ Band: `1350.66` | Lower -1.00σ Band: `1345.27`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`1347.97` | EMA-20=`1347.97` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`1347.97` (Slope: `+0.0000`) | EMA-100=`1347.97`
  * Institutional Anchors: EMA-144=`1347.97` | EMA-200=`1347.97` (Slope: `+0.0000`) | EMA-233=`1347.97`
- **Range Boundaries**: 24H High=`1361.44` | 24H Low=`1334.49` | Weekly High=`1374.92` | Weekly Low=`1321.01`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `1300.48` (Distance: `+3.66%`)
  * Point of Control (POC) = `1247.20` (Distance: `+8.09%`)
  * Value Area Low (VAL) = `1230.55` (Distance: `+9.55%`)
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
  * Golden Pocket Zone (0.618 - 0.650): `1342.57` - `1353.36`
  * Optimal Trade Entry (OTE 0.705): `1350.66`
  * Structural Invalidation Anchor (0.786): `1358.75`

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
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-29 23:06:38 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `16` | `0xb83d...6e36` | `SHORT` | 71,102,083.54 USD | `52,582.52` | `1336.45` | `1352.90` | `3636.93` | -828,168.65 USD | `-1.16%` | `3X Cross` |
| `23` | `0x5b5d...c060` | `SHORT` | 55,096,310.81 USD | `40,727.61` | `1478.36` | `1352.90` | `4885.67` | 5,113,953.39 USD | `+9.28%` | `3X Cross` |
| `42` | `0x7fda...17d1` | `SHORT` | 30,334,538.13 USD | `22,433.47` | `1261.17` | `1352.90` | `2879.06` | -2,042,157.15 USD | `-6.73%` | `5X Cross` |
| `79` | `0x60b0...991e` | `LONG` | 22,696,684.07 USD | `16,779.74` | `1179.65` | `1352.90` | `874.67` | 2,902,437.06 USD | `+12.79%` | `10X Cross` |
| `84` | `0xbf73...5d58` | `LONG` | 21,625,600.00 USD | `16,000.00` | `1214.30` | `1352.90` | `707.89` | 2,196,767.75 USD | `+10.16%` | `10X Cross` |
| `131` | `0xc36a...105b` | `LONG` | 15,563,779.72 USD | `11,510.82` | `1215.14` | `1352.90` | `924.34` | 1,576,498.69 USD | `+10.13%` | `10X Cross` |
| `170` | `0x8742...8427` | `LONG` | 12,450,157.25 USD | `9,201.21` | `1286.37` | `1352.90` | `698.32` | 613,987.26 USD | `+4.93%` | `10X Cross` |
| `191` | `0xad59...ba81` | `SHORT` | 11,392,285.00 USD | `8,425.00` | `330.91` | `1352.90` | `2138.34` | -8,604,327.23 USD | `-75.53%` | `10X Cross` |
| `199` | `0xdd53...2b13` | `SHORT` | 11,139,301.90 USD | `8,237.91` | `739.37` | `1352.90` | `7662.16` | -5,048,414.87 USD | `-45.32%` | `3X Cross` |
| `204` | `0x9ffd...ce40` | `LONG` | 10,927,181.42 USD | `8,087.02` | `1250.27` | `1352.90` | `555.26` | 816,188.35 USD | `+7.47%` | `5X Cross` |
| `207` | `0xfc66...ca06` | `SHORT` | 10,821,447.27 USD | `8,000.10` | `1319.34` | `1352.90` | `5426.77` | -266,598.44 USD | `-2.46%` | `10X Cross` |
| `218` | `0x880a...311c` | `SHORT` | 10,420,012.72 USD | `7,707.11` | `1367.50` | `1352.90` | `2305.60` | 119,471.48 USD | `+1.15%` | `10X Cross` |
| `265` | `0x2b61...2f6c` | `LONG` | 9,207,148.20 USD | `6,807.00` | `1453.56` | `1352.90` | `659.52` | -687,203.02 USD | `-7.46%` | `10X Cross` |
| `283` | `0x2ae5...83e7` | `LONG` | 8,707,703.04 USD | `6,436.80` | `1391.82` | `1352.90` | `0.000000` | -251,188.95 USD | `-2.88%` | `2X Cross` |
| `319` | `0xecb6...2b00` | `SHORT` | 7,916,792.95 USD | `5,854.75` | `1323.84` | `1352.90` | `6159.29` | -166,053.82 USD | `-2.10%` | `5X Cross` |
| `329` | `0x26b6...9a13` | `LONG` | 7,350,749.94 USD | `5,433.73` | `1282.23` | `1352.90` | `201.48` | 383,446.71 USD | `+5.22%` | `10X Cross` |
| `337` | `0x45d2...4029` | `SHORT` | 7,071,085.60 USD | `5,227.00` | `833.44` | `1352.90` | `7750.39` | -2,714,707.63 USD | `-38.39%` | `5X Cross` |
| `357` | `0xea00...a918` | `LONG` | 6,763,121.50 USD | `5,000.00` | `739.16` | `1352.90` | `0.000000` | 3,067,306.39 USD | `+45.35%` | `5X Cross` |
| `359` | `0x469e...58a5` | `SHORT` | 6,760,500.00 USD | `5,000.00` | `1190.36` | `1352.90` | `1814.38` | -808,715.10 USD | `-11.96%` | `10X Cross` |
| `375` | `0xdd7a...8830` | `LONG` | 6,571,948.92 USD | `4,860.19` | `897.48` | `1352.90` | `788.66` | 2,210,045.25 USD | `+33.63%` | `10X Cross` |
| `383` | `0xf081...e39e` | `LONG` | 6,379,270.80 USD | `4,717.00` | `1195.70` | `1352.90` | `1200.06` | 739,146.76 USD | `+11.59%` | `10X Cross` |
| `443` | `0x4cae...7c34` | `LONG` | 5,416,297.34 USD | `4,004.36` | `999.34` | `1352.90` | `685.15` | 1,414,569.18 USD | `+26.12%` | `10X Cross` |
| `448` | `0x382b...3e39` | `LONG` | 5,282,220.56 USD | `3,906.39` | `1166.42` | `1352.90` | `0.000000` | 725,741.00 USD | `+13.74%` | `10X Cross` |
| `451` | `0xa61c...66b9` | `LONG` | 5,257,353.60 USD | `3,888.00` | `1148.34` | `1352.90` | `0.000000` | 792,611.46 USD | `+15.08%` | `10X Cross` |
| `473` | `0x9aa5...58af` | `SHORT` | 5,030,231.15 USD | `3,720.31` | `1205.51` | `1352.90` | `3242.12` | -545,344.35 USD | `-10.84%` | `10X Cross` |
| `476` | `0x0153...8052` | `SHORT` | 5,002,897.90 USD | `3,698.18` | `1307.82` | `1352.90` | `2504.65` | -166,327.16 USD | `-3.32%` | `1X Isolated` |
| `509` | `0xd4c1...3d1d` | `SHORT` | 4,685,332.43 USD | `3,464.97` | `1302.89` | `1352.90` | `2590.52` | -170,874.38 USD | `-3.65%` | `10X Cross` |
| `536` | `0xd21d...90f1` | `LONG` | 4,394,650.00 USD | `3,250.00` | `1253.64` | `1352.90` | `875.85` | 320,308.27 USD | `+7.29%` | `4X Isolated` |
| `551` | `0x1338...c48e` | `LONG` | 4,259,289.13 USD | `3,149.43` | `1018.52` | `1352.90` | `820.14` | 1,051,543.59 USD | `+24.69%` | `4X Isolated` |
| `560` | `0x456f...cdf1` | `LONG` | 4,209,055.72 USD | `3,111.77` | `1267.78` | `1352.90` | `486.75` | 264,017.39 USD | `+6.27%` | `10X Cross` |
| `567` | `0xdbe0...d6d5` | `LONG` | 4,162,164.13 USD | `3,085.37` | `422.97` | `1352.90` | `338.46` | 2,857,159.64 USD | `+68.65%` | `3X Isolated` |
| `589` | `0x9c06...0560` | `SHORT` | 4,041,013.68 USD | `2,989.80` | `786.00` | `1352.90` | `2340.66` | -1,691,018.68 USD | `-41.85%` | `10X Cross` |
| `625` | `0x27c9...d65d` | `SHORT` | 3,824,829.26 USD | `2,827.71` | `1245.67` | `1352.90` | `1826.21` | -302,429.38 USD | `-7.91%` | `10X Cross` |
| `687` | `0xac48...3201` | `LONG` | 3,436,071.51 USD | `2,540.30` | `1393.86` | `1352.90` | `535.45` | -104,757.78 USD | `-3.05%` | `10X Cross` |
| `690` | `0xa183...0482` | `LONG` | 3,428,755.40 USD | `2,534.00` | `530.25` | `1352.90` | `444.38` | 2,085,092.68 USD | `+60.81%` | `5X Isolated` |
| `698` | `0x325e...9564` | `LONG` | 3,383,082.70 USD | `2,501.91` | `1306.24` | `1352.90` | `0.000000` | 114,988.80 USD | `+3.40%` | `10X Cross` |
| `699` | `0x0871...e927` | `LONG` | 3,381,500.00 USD | `2,500.00` | `1276.50` | `1352.90` | `0.000000` | 190,250.00 USD | `+5.63%` | `10X Cross` |
| `709` | `0x9b86...6e6e` | `LONG` | 3,336,283.06 USD | `2,467.30` | `637.58` | `1352.90` | `889.61` | 1,763,183.46 USD | `+52.85%` | `3X Cross` |
| `759` | `0xb2f7...af9f` | `SHORT` | 3,128,612.18 USD | `2,313.72` | `746.63` | `1352.90` | `4148.26` | -1,401,123.44 USD | `-44.78%` | `10X Cross` |
| `788` | `0x2e30...4cb5` | `SHORT` | 3,024,400.85 USD | `2,235.66` | `1295.47` | `1352.90` | `3341.80` | -128,181.33 USD | `-4.24%` | `2X Cross` |
| `793` | `0xf48f...10fe` | `LONG` | 2,999,842.18 USD | `2,218.49` | `1517.87` | `1352.90` | `868.05` | -367,544.65 USD | `-12.25%` | `3X Cross` |
| `822` | `0x5bc4...3b0c` | `SHORT` | 2,883,289.67 USD | `2,130.74` | `1089.65` | `1352.90` | `3537.46` | -561,532.09 USD | `-19.48%` | `5X Cross` |
| `847` | `0x4fe2...ac59` | `SHORT` | 2,798,691.07 USD | `2,071.57` | `1478.56` | `1352.90` | `1802.27` | 264,255.15 USD | `+9.44%` | `10X Cross` |
| `849` | `0x4e23...20c3` | `LONG` | 2,794,370.74 USD | `2,065.62` | `1302.47` | `1352.90` | `0.000000` | 103,959.99 USD | `+3.72%` | `4X Cross` |
| `858` | `0x71d0...8c26` | `SHORT` | 2,727,501.83 USD | `2,016.19` | `1362.26` | `1352.90` | `5068.57` | 19,068.23 USD | `+0.70%` | `10X Cross` |
| `861` | `0x668c...ea2e` | `SHORT` | 2,704,200.00 USD | `2,000.00` | `1409.16` | `1352.90` | `2701.79` | 114,122.04 USD | `+4.22%` | `10X Cross` |
| `862` | `0x362a...1d9f` | `SHORT` | 2,703,758.65 USD | `1,999.23` | `1382.50` | `1352.90` | `1677.95` | 60,178.75 USD | `+2.23%` | `5X Cross` |
| `884` | `0x77ee...2902` | `SHORT` | 2,632,200.18 USD | `1,946.03` | `759.84` | `1352.90` | `5272.15` | -1,153,522.67 USD | `-43.82%` | `10X Cross` |
| `891` | `0x3e2f...b269` | `SHORT` | 2,605,575.10 USD | `1,925.51` | `1134.87` | `1352.90` | `2931.71` | -420,376.24 USD | `-16.13%` | `10X Cross` |
| `900` | `0xe097...d0fe` | `LONG` | 2,589,046.68 USD | `1,913.56` | `1261.17` | `1352.90` | `0.000000` | 175,720.52 USD | `+6.79%` | `10X Cross` |
| `906` | `0x4f12...618b` | `SHORT` | 2,561,874.28 USD | `1,896.28` | `1608.30` | `1352.90` | `2116.67` | 487,910.11 USD | `+19.05%` | `3X Cross` |
| `943` | `0x866d...d6e1` | `LONG` | 2,437,452.83 USD | `1,802.05` | `674.73` | `1352.90` | `52.57` | 1,221,551.52 USD | `+50.12%` | `10X Cross` |
| `975` | `0x2309...a2d9` | `LONG` | 2,366,675.28 USD | `1,750.37` | `1186.09` | `1352.90` | `799.95` | 290,581.17 USD | `+12.28%` | `8X Cross` |
| `997` | `0x023a...2355` | `SHORT` | 2,320,834.95 USD | `1,716.34` | `1313.14` | `1352.90` | `6200.66` | -67,039.15 USD | `-2.89%` | `10X Cross` |
| `1001` | `0x2edd...8179` | `SHORT` | 2,307,285.90 USD | `1,706.32` | `1261.18` | `1352.90` | `2913.86` | -155,308.90 USD | `-6.73%` | `10X Cross` |
| `1032` | `0x265e...7f70` | `LONG` | 2,231,831.09 USD | `1,651.74` | `1388.09` | `1352.90` | `0.000000` | -60,938.60 USD | `-2.73%` | `3X Cross` |
| `1040` | `0xa271...a3f7` | `LONG` | 2,204,061.93 USD | `1,631.43` | `1190.60` | `1352.90` | `910.24` | 261,680.13 USD | `+11.87%` | `4X Cross` |
| `1050` | `0x7f75...9edf` | `LONG` | 2,170,372.25 USD | `1,605.78` | `1199.97` | `1352.90` | `975.08` | 243,480.36 USD | `+11.22%` | `10X Cross` |
| `1052` | `0x6646...6de5` | `SHORT` | 2,164,800.00 USD | `1,600.00` | `660.64` | `1352.90` | `4925.79` | -1,107,775.03 USD | `-51.17%` | `10X Cross` |
| `1061` | `0xdf57...93f5` | `LONG` | 2,137,710.70 USD | `1,579.76` | `1218.38` | `1352.90` | `780.08` | 212,954.71 USD | `+9.96%` | `3X Isolated` |
| `1074` | `0xab59...59b5` | `LONG` | 2,117,289.87 USD | `1,565.32` | `1342.15` | `1352.90` | `784.03` | 16,394.65 USD | `+0.77%` | `10X Cross` |
| `1076` | `0xfe7c...b7ae` | `SHORT` | 2,110,973.11 USD | `1,560.65` | `1350.64` | `1352.90` | `6262.92` | -3,099.36 USD | `-0.15%` | `10X Cross` |
| `1084` | `0x634f...6951` | `LONG` | 2,099,034.80 USD | `1,553.00` | `1263.46` | `1352.90` | `1184.28` | 136,885.22 USD | `+6.52%` | `10X Cross` |
| `1099` | `0x3e47...aaf6` | `LONG` | 2,077,357.82 USD | `1,536.28` | `1277.06` | `1352.90` | `1010.46` | 115,435.73 USD | `+5.56%` | `10X Cross` |
| `1127` | `0xcf67...eb24` | `LONG` | 2,026,500.00 USD | `1,500.00` | `887.05` | `1352.90` | `484.55` | 695,928.63 USD | `+34.34%` | `10X Cross` |
| `1144` | `0x039c...0ebd` | `SHORT` | 2,001,918.58 USD | `1,480.49` | `1238.67` | `1352.90` | `3114.02` | -168,087.26 USD | `-8.40%` | `10X Cross` |
| `1203` | `0x7a76...b16d` | `LONG` | 1,914,255.45 USD | `1,415.66` | `1362.09` | `1352.90` | `1259.05` | -13,999.80 USD | `-0.73%` | `10X Cross` |
| `1226` | `0x2ab7...c2f8` | `LONG` | 1,894,609.93 USD | `1,400.51` | `813.26` | `1352.90` | `791.25` | 755,628.24 USD | `+39.88%` | `3X Cross` |
| `1249` | `0x11be...8b1d` | `LONG` | 1,860,981.09 USD | `1,375.83` | `1206.55` | `1352.90` | `1134.36` | 200,973.13 USD | `+10.80%` | `10X Isolated` |
| `1305` | `0xef96...9383` | `SHORT` | 1,768,215.82 USD | `1,308.82` | `1249.96` | `1352.90` | `4060.90` | -132,249.40 USD | `-7.48%` | `10X Cross` |
| `1310` | `0xfc27...9d9d` | `SHORT` | 1,762,076.11 USD | `1,302.54` | `1315.39` | `1352.90` | `11713.32` | -48,734.09 USD | `-2.77%` | `10X Cross` |
| `1324` | `0xdf83...3cff` | `SHORT` | 1,735,697.44 USD | `1,283.61` | `1244.31` | `1352.90` | `1883.48` | -138,489.37 USD | `-7.98%` | `10X Cross` |
| `1347` | `0xe065...0f85` | `SHORT` | 1,705,786.11 USD | `1,262.61` | `1087.02` | `1352.90` | `1608.25` | -333,309.98 USD | `-19.54%` | `10X Cross` |
| `1351` | `0x5323...b23c` | `SHORT` | 1,701,903.57 USD | `1,258.06` | `1359.39` | `1352.90` | `5862.78` | 8,294.86 USD | `+0.49%` | `5X Cross` |
| `1369` | `0x7277...0b98` | `SHORT` | 1,671,131.82 USD | `1,234.96` | `1298.48` | `1352.90` | `2338.22` | -67,562.40 USD | `-4.04%` | `10X Cross` |
| `1411` | `0x5975...9abd` | `LONG` | 1,623,149.16 USD | `1,200.00` | `1179.54` | `1352.90` | `276.52` | 207,706.37 USD | `+12.80%` | `5X Cross` |
| `1462` | `0x69cc...14fd` | `SHORT` | 1,571,087.81 USD | `1,161.36` | `675.33` | `1352.90` | `7746.62` | -786,782.28 USD | `-50.08%` | `10X Cross` |
| `1479` | `0x3fc5...c0c1` | `SHORT` | 1,553,407.85 USD | `1,148.44` | `1264.34` | `1352.90` | `2990.48` | -101,394.08 USD | `-6.53%` | `10X Cross` |
| `1506` | `0xe35c...a1d3` | `LONG` | 1,524,010.53 USD | `1,127.06` | `1318.20` | `1352.90` | `694.28` | 38,315.18 USD | `+2.51%` | `2X Isolated` |
| `1514` | `0x5f94...4b96` | `LONG` | 1,508,068.09 USD | `1,115.27` | `538.00` | `1352.90` | `0.000000` | 908,050.46 USD | `+60.21%` | `10X Cross` |
| `1532` | `0x9546...181c` | `LONG` | 1,487,333.40 USD | `1,100.75` | `1348.55` | `1352.90` | `0.000000` | 2,912.15 USD | `+0.20%` | `10X Cross` |
| `1535` | `0x71df...a23d` | `SHORT` | 1,485,533.53 USD | `1,098.28` | `513.50` | `1352.90` | `2544.41` | -921,563.34 USD | `-62.04%` | `2X Cross` |
| `1563` | `0xbfc7...80b4` | `SHORT` | 1,453,507.50 USD | `1,075.00` | `558.03` | `1352.90` | `5185.29` | -853,628.77 USD | `-58.73%` | `10X Cross` |
| `1613` | `0x51f6...2b39` | `SHORT` | 1,406,125.74 USD | `1,039.88` | `1302.72` | `1352.90` | `2849.13` | -51,448.93 USD | `-3.66%` | `10X Cross` |
| `1641` | `0x123d...3bff` | `SHORT` | 1,363,039.51 USD | `1,007.70` | `488.87` | `1352.90` | `4128.69` | -870,404.38 USD | `-63.86%` | `10X Cross` |
| `1649` | `0x0748...d4b2` | `LONG` | 1,353,100.00 USD | `1,000.00` | `1334.09` | `1352.90` | `0.000000` | 19,011.70 USD | `+1.41%` | `7X Cross` |
| `1650` | `0x266b...efcb` | `LONG` | 1,353,000.00 USD | `1,000.00` | `826.11` | `1352.90` | `138.06` | 526,887.07 USD | `+38.94%` | `10X Cross` |
| `1651` | `0xb5ff...d912` | `LONG` | 1,352,800.00 USD | `1,000.00` | `1141.93` | `1352.90` | `400.40` | 210,869.70 USD | `+15.59%` | `2X Cross` |
| `1652` | `0xe282...df29` | `LONG` | 1,352,200.00 USD | `1,000.00` | `420.99` | `1352.90` | `86.35` | 931,213.14 USD | `+68.87%` | `10X Cross` |
| `1670` | `0x17f0...094f` | `LONG` | 1,331,364.18 USD | `984.30` | `1287.23` | `1352.90` | `536.71` | 64,344.02 USD | `+4.83%` | `5X Cross` |
| `1748` | `0x757d...94ba` | `LONG` | 1,251,697.98 USD | `925.00` | `1558.31` | `1352.90` | `0.000000` | -189,742.61 USD | `-15.16%` | `10X Cross` |
| `1757` | `0x5d90...eea3` | `LONG` | 1,245,281.55 USD | `920.93` | `1288.61` | `1352.90` | `904.51` | 58,564.30 USD | `+4.70%` | `3X Isolated` |
| `1760` | `0x3205...40bb` | `SHORT` | 1,239,110.69 USD | `915.96` | `1344.67` | `1352.90` | `2746.17` | -7,446.33 USD | `-0.60%` | `10X Cross` |
| `1813` | `0xf096...7553` | `SHORT` | 1,190,501.78 USD | `881.07` | `1240.34` | `1352.90` | `3449.19` | -97,671.70 USD | `-8.20%` | `10X Cross` |
| `1815` | `0xdf95...7d72` | `SHORT` | 1,189,814.30 USD | `879.91` | `1073.66` | `1352.90` | `40491.76` | -245,090.25 USD | `-20.60%` | `10X Cross` |
| `1827` | `0xcf0a...856f` | `LONG` | 1,177,446.34 USD | `871.15` | `1292.19` | `1352.90` | `938.42` | 51,751.49 USD | `+4.40%` | `4X Cross` |
| `1838` | `0x2847...d47b` | `LONG` | 1,169,946.15 USD | `864.92` | `1235.71` | `1352.90` | `0.000000` | 101,156.01 USD | `+8.65%` | `5X Cross` |
| `1862` | `0x7d0f...ea35` | `LONG` | 1,148,520.00 USD | `850.00` | `1317.57` | `1352.90` | `1275.59` | 28,584.42 USD | `+2.49%` | `10X Cross` |
| `1896` | `0x601c...4f54` | `SHORT` | 1,114,945.61 USD | `824.42` | `615.11` | `1352.90` | `2898.96` | -607,832.86 USD | `-54.52%` | `5X Cross` |
| `1906` | `0xae55...2236` | `LONG` | 1,105,873.42 USD | `817.47` | `1467.80` | `1352.90` | `0.000000` | -94,007.80 USD | `-8.50%` | `10X Cross` |
| `1914` | `0x71b1...79c8` | `LONG` | 1,099,177.06 USD | `812.52` | `1231.55` | `1352.90` | `663.23` | 98,521.60 USD | `+8.96%` | `10X Cross` |
| `1929` | `0x0f02...5384` | `LONG` | 1,083,295.18 USD | `800.78` | `1290.36` | `1352.90` | `282.89` | 50,001.11 USD | `+4.62%` | `3X Cross` |
| `1932` | `0x9b0f...db40` | `LONG` | 1,082,131.20 USD | `800.00` | `1268.86` | `1352.90` | `772.18` | 67,041.44 USD | `+6.20%` | `10X Cross` |
| `1933` | `0xea0f...4e73` | `LONG` | 1,081,760.00 USD | `800.00` | `1364.27` | `1352.90` | `572.76` | -9,658.68 USD | `-0.89%` | `10X Cross` |
| `1946` | `0xabdb...84ac` | `LONG` | 1,073,148.25 USD | `793.69` | `711.79` | `1352.90` | `664.28` | 508,207.89 USD | `+47.36%` | `3X Cross` |
| `1958` | `0xfdf8...e381` | `LONG` | 1,068,962.53 USD | `790.01` | `1337.72` | `1352.90` | `225.49` | 12,152.85 USD | `+1.14%` | `10X Cross` |
| `2004` | `0x0c1f...1d39` | `SHORT` | 1,032,172.87 USD | `762.99` | `1299.17` | `1352.90` | `4632.30` | -40,921.79 USD | `-3.96%` | `10X Cross` |
| `2007` | `0xf6f3...47f8` | `SHORT` | 1,030,175.74 USD | `761.57` | `1253.10` | `1352.90` | `2313.34` | -75,852.74 USD | `-7.36%` | `5X Cross` |
| `2012` | `0x389a...e76b` | `LONG` | 1,027,847.79 USD | `760.13` | `1266.20` | `1352.90` | `366.32` | 65,374.37 USD | `+6.36%` | `10X Cross` |
| `2028` | `0xadd1...5e0d` | `LONG` | 1,014,237.74 USD | `750.62` | `1195.15` | `1352.90` | `0.000000` | 117,136.65 USD | `+11.55%` | `10X Cross` |
| `2029` | `0xe83b...3ca8` | `LONG` | 1,014,150.00 USD | `750.00` | `1346.44` | `1352.90` | `0.000000` | 4,322.36 USD | `+0.43%` | `10X Cross` |
| `2038` | `0xd6e1...f256` | `SHORT` | 1,009,913.25 USD | `746.37` | `1368.65` | `1352.90` | `2024.53` | 11,602.54 USD | `+1.15%` | `10X Cross` |
| `2045` | `0x87a7...9fa2` | `SHORT` | 1,006,821.08 USD | `744.58` | `1464.55` | `1352.90` | `1712.17` | 83,655.67 USD | `+8.31%` | `10X Cross` |
| `2056` | `0x8923...1bac` | `LONG` | 1,003,858.77 USD | `742.06` | `1239.64` | `1352.90` | `700.03` | 83,972.24 USD | `+8.36%` | `5X Cross` |
| `2063` | `0xb122...e4ba` | `LONG` | 1,001,239.61 USD | `741.11` | `1299.26` | `1352.90` | `922.99` | 38,347.45 USD | `+3.83%` | `10X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `1297.10` | 194.56 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Long: 0.19K USD at 1297.1000 USD [API] | `2026-10-27 15:46:39` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`1404.15` (Vol: 3,000,000.00 USD, Dist: `+3.89%`) | Long MP=`1287.60` (Vol: 2,300,000.00 USD, Dist: `--4.73%`)
  * 48H Horizon: Short MP=`1404.15` (Vol: 3,000,000.00 USD, Dist: `+3.89%`) | Long MP=`1287.60` (Vol: 2,300,000.00 USD, Dist: `--4.73%`)
  * 3D Horizon: Short MP=`1404.42` (Vol: 3,000,000.00 USD, Dist: `+3.91%`) | Long MP=`0.000000` (Vol: 0.00 USD, Dist: `-0.00%`)
  * 7D Horizon: Short MP=`1404.10` (Vol: 3,000,000.00 USD, Dist: `+3.89%`) | Long MP=`1200.46` (Vol: 3,000,000.00 USD, Dist: `--11.18%`)
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
  * Current Rate: `89.26K` | Last 24h: `32.07K` | Last 3d: `282.84K` | Last 7d: `777.72K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0084%` | **USDT OKX** | `0.0092%` |
| **USDT Bybit** | `0.0100%` | **USDT KuCoin** | `0.0100%` |
| **USDT MEXC** | `0.0083%` | **USDT BingX** | `0.0054%` |
| **USDT Gate** | `0.0100%` | **USDT Bitget** | `0.0073%` |
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
| `5:00 UTC` | `1317.75` | `1318.00` | `1317.75` | `1324.05` | `1313.25` | 29,849,949.75 USD | 16,298,218.14 USD | 13,551,731.61 USD | 2,746,486.54 USD | `+9.20%` | `4B / 2S` |
| `0:00 UTC` | `1345.05` | `1339.86` | `1345.05` | `1353.45` | `1318.65` | 81,702,422.73 USD | 46,151,799.06 USD | 35,550,623.66 USD | 10,601,175.40 USD | `+12.98%` | `23B / 1S` |
| `5:00 UTC` | `1360.05` | `1349.51` | `1360.05` | `1362.15` | `1334.25` | 65,905,391.58 USD | 39,286,823.07 USD | 26,618,568.52 USD | 12,668,254.55 USD | `+19.22%` | `19B / 3S` |
| `0:00 UTC` | `1369.95` | `1375.81` | `1369.95` | `1397.55` | `1350.75` | 159,915,504.01 USD | 87,974,917.65 USD | 71,940,586.35 USD | 16,034,331.30 USD | `+10.03%` | `21B / 3S` |
| `5:00 UTC` | `1359.75` | `1358.32` | `1359.75` | `1373.25` | `1346.25` | 77,512,400.13 USD | 36,921,415.88 USD | 40,590,984.25 USD | -3,669,568.36 USD | `-4.73%` | `4B / 13S` |
| `0:00 UTC` | `1353.15` | `1350.71` | `1353.15` | `1361.25` | `1341.75` | 52,010,841.39 USD | 26,247,439.78 USD | 25,763,401.61 USD | 484,038.17 USD | `+0.93%` | `5B / 3S` |
| `5:00 UTC` | `1343.25` | `1344.85` | `1343.25` | `1353.45` | `1340.25` | 26,552,172.39 USD | 11,915,117.49 USD | 14,637,054.90 USD | -2,721,937.40 USD | `-10.25%` | `0B / 9S` |
| `0:00 UTC` | `1342.95` | `1346.21` | `1342.95` | `1354.05` | `1340.25` | 27,005,669.33 USD | 14,153,013.83 USD | 12,852,655.50 USD | 1,300,358.33 USD | `+4.82%` | `5B / 3S` |
| `5:00 UTC` | `1348.65` | `1350.13` | `1348.65` | `1356.15` | `1344.45` | 21,612,679.16 USD | 11,526,731.97 USD | 10,085,947.19 USD | 1,440,784.78 USD | `+6.67%` | `2B / 2S` |
| `0:00 UTC` | `1354.05` | `1353.19` | `1354.05` | `1354.95` | `1348.65` | 3,931,914.96 USD | 2,188,172.01 USD | 1,743,742.94 USD | 444,429.07 USD | `+11.30%` | `2B / 3S` |

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
| `5m` | -189,100.00 USD | 1,290,000.00 USD | **`ACCUMULATION`** |
| `15m` | 1,100,000.00 USD | 2,640,000.00 USD | **`ACCUMULATION`** |
| `30m` | 5,690,000.00 USD | 9,640,000.00 USD | **`ACCUMULATION`** |
| `1h` | 6,680,000.00 USD | 9,980,000.00 USD | **`ACCUMULATION`** |
| `2h` | 14,050,000.00 USD | 47,560,000.00 USD | **`ACCUMULATION`** |
| `4h` | 30,290,000.00 USD | 114,200,000.00 USD | **`ACCUMULATION`** |
| `6h` | 33,150,000.00 USD | 119,840,000.00 USD | **`ACCUMULATION`** |
| `8h` | 31,140,000.00 USD | 130,980,000.00 USD | **`ACCUMULATION`** |
| `12h` | 28,470,000.00 USD | 130,050,000.00 USD | **`ACCUMULATION`** |
| `24h` | 17,790,000.00 USD | 126,060,000.00 USD | **`ACCUMULATION`** |
| `1w` | 55,140,000.00 USD | 289,990,000.00 USD | **`ACCUMULATION`** |
| `30d` | 71,600,000.00 USD | -482,610,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-189.10K` | 15m=`+1.10M` | 1h=`+6.68M` | 24h=`+17.79M`
* Futures Capital Netflows: 5m=`+1.29M` | 15m=`+2.64M` | 1h=`+9.98M` | 24h=`+126.06M`
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
  * `2026-10-29 23:01:06 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-29 22:55:06 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-29 22:45:06 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:06:06 IST`: [fxstreet.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:01:06 IST`: [ForexFactory] - (Sentiment: `Neutral`)
  * `2026-10-29 23:01:06 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-29 23:01:06 IST`: [youtube.com/bankofcanadaofficial] - (Sentiment: `Neutral`)
  * `2026-10-29 23:00:06 IST`: [notayesmanseconomics.wordpress.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:00:06 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:00:06 IST`: [breakingthenews.net] - (Sentiment: `Neutral`)
  * `2026-10-29 20:02:06 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-29 20:02:06 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-29 20:02:06 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-29 20:02:06 IST`: [youtube.com/ecbeuro] - (Sentiment: `Neutral`)
  * `2026-10-29 19:02:06 IST`: [ecb.europa.eu] - (Sentiment: `Neutral`)


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
  * Spread-Padded Stop Loss: `1225.23` (Risk Distance: `5.32` pts)
  * +2.5R Take Profit: `1243.85`
  * Mathematical Lot Sizing: **`1.88 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `1300.48` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `1305.80` (Risk Distance: `5.32` pts)
  * +2.5R Take Profit: `1287.18`
  * Mathematical Lot Sizing: **`1.88 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`1358.75`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
