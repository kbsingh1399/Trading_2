# 🏛️ SOVEREIGN CANDIDATE DOSSIER: ZECUSD
**Canonical Key**: `ZECUSD` | **Broker Instrument**: `ZECUSD.p` | **Asset Class**: `Crypto Altcoin`
**Timestamp**: `2026-10-30 00:56:34 IST` (`2026-10-29 19:26:34 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `1321.49` | **Live Ask Quote**: `1322.65` | **Mid Price**: `1322.07`
- **Spread Points**: `116.00` | **Spread BPS**: `8.77 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `1280.37` | VWAP Z-Score: `+0.98` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `15.96` (Volatility Regime: `HIGH_EXPANSION`)
  * 14-Period RSI: `50.90` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `1396.84` | Lower -3.00σ Band: `1163.89`
  * Upper +2.51σ Band: `1377.82` | Lower -2.51σ Band: `1182.91`
  * Upper +2.01σ Band: `1358.41` | Lower -2.01σ Band: `1202.33`
  * Upper +2.00σ Band: `1358.02` | Lower -2.00σ Band: `1202.72`
  * Upper +1.28σ Band: `1330.06` | Lower -1.28σ Band: `1230.67`
  * Upper +1.00σ Band: `1319.19` | Lower -1.00σ Band: `1241.54`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`1326.93` | EMA-20=`1322.51` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`1301.25` (Slope: `+0.0000`) | EMA-100=`1289.83`
  * Institutional Anchors: EMA-144=`1284.89` | EMA-200=`1279.95` (Slope: `+0.5524`) | EMA-233=`1277.49`
- **Range Boundaries**: 24H High=`1396.49` | 24H Low=`1230.00` | Weekly High=`1396.49` | Weekly Low=`1210.62`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `1307.14` (Distance: `+1.12%`)
  * Point of Control (POC) = `1247.20` (Distance: `+5.98%`)
  * Value Area Low (VAL) = `1230.55` (Distance: `+7.41%`)
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
  * Golden Pocket Zone (0.618 - 0.650): `1316.78` - `1327.36`
  * Optimal Trade Entry (OTE 0.705): `1324.71`
  * Structural Invalidation Anchor (0.786): `1332.65`

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
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 00:53:52 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `16` | `0xb83d...6e36` | `SHORT` | 69,698,130.26 USD | `52,582.52` | `1336.45` | `1324.80` | `3706.25` | 575,784.64 USD | `+0.83%` | `3X Cross` |
| `23` | `0x5b5d...c060` | `SHORT` | 53,992,592.58 USD | `40,727.61` | `1478.36` | `1324.80` | `4994.32` | 6,217,671.62 USD | `+11.52%` | `3X Cross` |
| `41` | `0x7fda...17d1` | `SHORT` | 29,710,795.91 USD | `22,421.55` | `1261.41` | `1324.80` | `2810.69` | -1,427,932.87 USD | `-4.81%` | `5X Cross` |
| `77` | `0x60b0...991e` | `LONG` | 22,241,545.37 USD | `16,779.74` | `1179.65` | `1324.80` | `887.37` | 2,447,298.36 USD | `+11.00%` | `10X Cross` |
| `82` | `0xbf73...5d58` | `LONG` | 21,211,200.00 USD | `16,000.00` | `1214.30` | `1324.80` | `723.61` | 1,782,367.75 USD | `+8.40%` | `10X Cross` |
| `132` | `0xc36a...105b` | `LONG` | 15,247,232.17 USD | `11,510.82` | `1215.14` | `1324.80` | `931.71` | 1,259,951.14 USD | `+8.26%` | `10X Cross` |
| `169` | `0x8742...8427` | `LONG` | 12,191,603.25 USD | `9,201.21` | `1286.37` | `1324.80` | `698.35` | 355,433.26 USD | `+2.92%` | `10X Cross` |
| `176` | `0x9071...5c0b` | `LONG` | 11,697,021.52 USD | `8,829.94` | `1370.53` | `1324.80` | `579.50` | -404,667.13 USD | `-3.46%` | `2X Cross` |
| `191` | `0xad59...ba81` | `SHORT` | 11,167,337.50 USD | `8,425.00` | `330.91` | `1324.80` | `2140.08` | -8,379,379.73 USD | `-75.03%` | `10X Cross` |
| `199` | `0xdd53...2b13` | `SHORT` | 10,904,614.27 USD | `8,231.14` | `739.37` | `1324.80` | `7860.31` | -4,818,732.79 USD | `-44.19%` | `3X Cross` |
| `201` | `0x9ffd...ce40` | `LONG` | 10,874,510.60 USD | `8,205.32` | `1253.95` | `1324.80` | `570.34` | 585,453.76 USD | `+5.38%` | `5X Cross` |
| `215` | `0xfc66...ca06` | `SHORT` | 10,285,376.26 USD | `7,763.72` | `1319.72` | `1324.80` | `5596.10` | -39,411.17 USD | `-0.38%` | `10X Cross` |
| `220` | `0x880a...311c` | `SHORT` | 10,212,407.84 USD | `7,707.11` | `1367.50` | `1324.80` | `2307.75` | 327,076.36 USD | `+3.20%` | `10X Cross` |
| `268` | `0x2b61...2f6c` | `LONG` | 9,019,705.20 USD | `6,807.00` | `1453.56` | `1324.80` | `638.60` | -874,646.02 USD | `-9.70%` | `10X Cross` |
| `285` | `0x2ae5...83e7` | `LONG` | 8,526,828.96 USD | `6,436.80` | `1391.82` | `1324.80` | `264.91` | -432,063.03 USD | `-5.07%` | `2X Cross` |
| `330` | `0xecb6...2b00` | `SHORT` | 7,206,103.87 USD | `5,439.39` | `1324.05` | `1324.80` | `6109.32` | -4,065.34 USD | `-0.06%` | `5X Cross` |
| `331` | `0x26b6...9a13` | `LONG` | 7,198,062.13 USD | `5,433.73` | `1282.23` | `1324.80` | `207.10` | 230,758.90 USD | `+3.21%` | `10X Cross` |
| `342` | `0x45d2...4029` | `SHORT` | 6,924,206.90 USD | `5,227.00` | `833.44` | `1324.80` | `8022.32` | -2,567,828.93 USD | `-37.08%` | `5X Cross` |
| `360` | `0xea00...a918` | `LONG` | 6,618,000.00 USD | `5,000.00` | `739.16` | `1324.80` | `0.000000` | 2,922,184.89 USD | `+44.16%` | `5X Cross` |
| `378` | `0xdd7a...8830` | `LONG` | 6,441,695.83 USD | `4,860.19` | `897.48` | `1324.80` | `783.46` | 2,079,792.15 USD | `+32.29%` | `10X Cross` |
| `385` | `0xf081...e39e` | `LONG` | 6,250,496.70 USD | `4,717.00` | `1195.70` | `1324.80` | `1200.09` | 610,372.66 USD | `+9.77%` | `10X Cross` |
| `436` | `0x4cae...7c34` | `LONG` | 5,306,177.44 USD | `4,004.36` | `999.34` | `1324.80` | `749.31` | 1,304,449.28 USD | `+24.58%` | `10X Cross` |
| `449` | `0x382b...3e39` | `LONG` | 5,154,372.86 USD | `3,890.68` | `1198.83` | `1324.80` | `0.000000` | 490,122.86 USD | `+9.51%` | `10X Cross` |
| `450` | `0xa61c...66b9` | `LONG` | 5,153,155.20 USD | `3,888.00` | `1148.34` | `1324.80` | `0.000000` | 688,413.06 USD | `+13.36%` | `10X Cross` |
| `468` | `0x9aa5...58af` | `SHORT` | 4,929,410.75 USD | `3,720.31` | `1205.51` | `1324.80` | `3323.41` | -444,523.95 USD | `-9.02%` | `10X Cross` |
| `475` | `0x0153...8052` | `SHORT` | 4,898,979.05 USD | `3,698.18` | `1307.82` | `1324.80` | `2504.69` | -62,408.30 USD | `-1.27%` | `1X Isolated` |
| `502` | `0xd4c1...3d1d` | `SHORT` | 4,579,899.84 USD | `3,457.05` | `1302.97` | `1324.80` | `2679.19` | -75,467.19 USD | `-1.65%` | `10X Cross` |
| `527` | `0xd21d...90f1` | `LONG` | 4,307,875.00 USD | `3,250.00` | `1253.64` | `1324.80` | `875.88` | 233,533.27 USD | `+5.42%` | `4X Isolated` |
| `548` | `0x1338...c48e` | `LONG` | 4,172,364.86 USD | `3,149.43` | `1018.52` | `1324.80` | `820.17` | 964,619.32 USD | `+23.12%` | `4X Isolated` |
| `551` | `0x456f...cdf1` | `LONG` | 4,148,308.00 USD | `3,134.11` | `1268.52` | `1324.80` | `493.31` | 172,618.36 USD | `+4.16%` | `10X Cross` |
| `561` | `0xdbe0...d6d5` | `LONG` | 4,087,189.64 USD | `3,085.37` | `422.97` | `1324.80` | `338.49` | 2,782,185.15 USD | `+68.07%` | `3X Isolated` |
| `567` | `0x27c9...d65d` | `SHORT` | 4,051,741.82 USD | `3,058.38` | `1251.75` | `1324.80` | `1808.56` | -223,423.98 USD | `-5.51%` | `10X Cross` |
| `586` | `0x9c06...0560` | `SHORT` | 3,963,577.86 USD | `2,989.80` | `786.00` | `1324.80` | `2371.48` | -1,613,582.86 USD | `-40.71%` | `10X Cross` |
| `687` | `0xac48...3201` | `LONG` | 3,367,167.65 USD | `2,540.30` | `1393.86` | `1324.80` | `532.74` | -173,661.64 USD | `-5.16%` | `10X Cross` |
| `691` | `0xa183...0482` | `LONG` | 3,357,550.00 USD | `2,534.00` | `530.25` | `1324.80` | `444.42` | 2,013,887.28 USD | `+59.98%` | `5X Isolated` |
| `698` | `0x2e30...4cb5` | `SHORT` | 3,320,214.83 USD | `2,506.39` | `1299.10` | `1324.80` | `3129.21` | -64,155.74 USD | `-1.93%` | `2X Cross` |
| `699` | `0x325e...9564` | `LONG` | 3,316,031.51 USD | `2,501.91` | `1306.24` | `1324.80` | `0.000000` | 47,937.61 USD | `+1.45%` | `10X Cross` |
| `700` | `0x0871...e927` | `LONG` | 3,312,658.00 USD | `2,500.00` | `1276.50` | `1324.80` | `0.000000` | 121,408.00 USD | `+3.66%` | `10X Cross` |
| `710` | `0x9b86...6e6e` | `LONG` | 3,267,692.12 USD | `2,467.30` | `637.58` | `1324.80` | `889.64` | 1,694,592.52 USD | `+51.86%` | `3X Cross` |
| `770` | `0xb2f7...af9f` | `SHORT` | 3,066,835.86 USD | `2,313.72` | `746.63` | `1324.80` | `4174.77` | -1,339,347.11 USD | `-43.67%` | `10X Cross` |
| `784` | `0x634f...6951` | `LONG` | 3,012,547.19 USD | `2,272.42` | `1281.94` | `1324.80` | `1250.03` | 99,446.73 USD | `+3.30%` | `10X Cross` |
| `801` | `0xf48f...10fe` | `LONG` | 2,940,608.50 USD | `2,218.49` | `1517.87` | `1324.80` | `892.18` | -426,778.33 USD | `-14.51%` | `3X Cross` |
| `830` | `0x5bc4...3b0c` | `SHORT` | 2,822,804.35 USD | `2,130.74` | `1089.65` | `1324.80` | `3562.24` | -501,046.77 USD | `-17.75%` | `5X Cross` |
| `842` | `0x8de4...b9aa` | `SHORT` | 2,771,586.64 USD | `2,091.29` | `1331.35` | `1324.80` | `1689.81` | 12,653.07 USD | `+0.46%` | `3X Cross` |
| `848` | `0x4fe2...ac59` | `SHORT` | 2,741,722.90 USD | `2,071.57` | `1478.56` | `1324.80` | `1812.30` | 321,223.32 USD | `+11.72%` | `10X Cross` |
| `865` | `0x668c...ea2e` | `SHORT` | 2,650,000.00 USD | `2,000.00` | `1406.98` | `1324.80` | `2702.08` | 163,963.99 USD | `+6.19%` | `10X Cross` |
| `887` | `0x77ee...2902` | `SHORT` | 2,578,612.74 USD | `1,946.03` | `759.84` | `1324.80` | `5209.06` | -1,099,935.23 USD | `-42.66%` | `10X Cross` |
| `899` | `0x3e2f...b269` | `SHORT` | 2,551,300.75 USD | `1,925.51` | `1134.87` | `1324.80` | `2931.74` | -366,101.89 USD | `-14.35%` | `10X Cross` |
| `906` | `0xe097...d0fe` | `LONG` | 2,535,084.29 USD | `1,913.56` | `1261.17` | `1324.80` | `0.000000` | 121,758.12 USD | `+4.80%` | `10X Cross` |
| `914` | `0x4f12...618b` | `SHORT` | 2,513,139.88 USD | `1,896.28` | `1608.30` | `1324.80` | `2116.70` | 536,644.51 USD | `+21.35%` | `3X Cross` |
| `957` | `0x866d...d6e1` | `LONG` | 2,387,896.46 USD | `1,802.05` | `674.73` | `1324.80` | `96.46` | 1,171,995.14 USD | `+49.08%` | `10X Cross` |
| `991` | `0x2309...a2d9` | `LONG` | 2,319,240.25 USD | `1,750.37` | `1186.09` | `1324.80` | `804.33` | 243,146.14 USD | `+10.48%` | `8X Cross` |
| `1007` | `0x023a...2355` | `SHORT` | 2,254,379.38 USD | `1,701.29` | `1313.34` | `1324.80` | `6061.82` | -20,010.49 USD | `-0.89%` | `10X Cross` |
| `1014` | `0x2edd...8179` | `SHORT` | 2,245,973.18 USD | `1,695.33` | `1261.35` | `1324.80` | `2977.96` | -107,572.21 USD | `-4.79%` | `10X Cross` |
| `1041` | `0x3e47...aaf6` | `LONG` | 2,166,598.35 USD | `1,636.28` | `1279.54` | `1324.80` | `1036.79` | 72,906.26 USD | `+3.37%` | `10X Cross` |
| `1046` | `0xa271...a3f7` | `LONG` | 2,159,197.60 USD | `1,631.43` | `1190.60` | `1324.80` | `910.27` | 216,815.80 USD | `+10.04%` | `4X Cross` |
| `1057` | `0x7f75...9edf` | `LONG` | 2,124,928.67 USD | `1,605.78` | `1199.97` | `1324.80` | `973.84` | 198,036.78 USD | `+9.32%` | `10X Cross` |
| `1060` | `0x265e...7f70` | `LONG` | 2,119,902.89 USD | `1,601.74` | `1388.09` | `1324.80` | `0.000000` | -103,462.12 USD | `-4.88%` | `3X Cross` |
| `1062` | `0x6646...6de5` | `SHORT` | 2,119,680.00 USD | `1,600.00` | `660.64` | `1324.80` | `4815.20` | -1,062,655.03 USD | `-50.13%` | `10X Cross` |
| `1075` | `0xdf57...93f5` | `LONG` | 2,093,655.93 USD | `1,579.76` | `1218.38` | `1324.80` | `780.12` | 168,899.95 USD | `+8.07%` | `3X Isolated` |
| `1092` | `0xab59...59b5` | `LONG` | 2,072,640.21 USD | `1,565.32` | `1342.15` | `1324.80` | `791.47` | -28,255.01 USD | `-1.36%` | `10X Cross` |
| `1094` | `0xfe7c...b7ae` | `SHORT` | 2,068,111.76 USD | `1,562.49` | `1350.62` | `1324.80` | `6496.86` | 42,217.28 USD | `+2.04%` | `10X Cross` |
| `1149` | `0xcf67...eb24` | `LONG` | 1,987,950.00 USD | `1,500.00` | `887.05` | `1324.80` | `534.69` | 657,378.63 USD | `+33.07%` | `10X Cross` |
| `1170` | `0x039c...0ebd` | `SHORT` | 1,962,389.50 USD | `1,480.49` | `1238.67` | `1324.80` | `3172.02` | -128,558.17 USD | `-6.55%` | `10X Cross` |
| `1195` | `0x71d0...8c26` | `SHORT` | 1,914,504.48 USD | `1,444.80` | `1361.12` | `1324.80` | `6494.38` | 52,041.97 USD | `+2.72%` | `10X Cross` |
| `1244` | `0xfc27...9d9d` | `SHORT` | 1,860,601.92 USD | `1,403.91` | `1317.50` | `1324.80` | `11277.97` | -10,955.76 USD | `-0.59%` | `10X Cross` |
| `1247` | `0x2ab7...c2f8` | `LONG` | 1,855,255.60 USD | `1,400.51` | `813.26` | `1324.80` | `796.29` | 716,273.91 USD | `+38.61%` | `3X Cross` |
| `1261` | `0x11be...8b1d` | `LONG` | 1,823,662.67 USD | `1,375.83` | `1206.55` | `1324.80` | `1134.40` | 163,654.71 USD | `+8.97%` | `10X Isolated` |
| `1312` | `0xdf83...3cff` | `SHORT` | 1,740,288.72 USD | `1,312.93` | `1246.70` | `1324.80` | `1848.50` | -103,458.40 USD | `-5.94%` | `10X Cross` |
| `1316` | `0xef96...9383` | `SHORT` | 1,734,579.15 USD | `1,308.82` | `1249.96` | `1324.80` | `4221.28` | -98,612.73 USD | `-5.69%` | `10X Cross` |
| `1361` | `0xe065...0f85` | `SHORT` | 1,673,337.03 USD | `1,262.61` | `1087.02` | `1324.80` | `1750.58` | -300,860.91 USD | `-17.98%` | `10X Cross` |
| `1384` | `0x7277...0b98` | `SHORT` | 1,636,692.49 USD | `1,234.96` | `1298.48` | `1324.80` | `2359.06` | -33,123.07 USD | `-2.02%` | `10X Cross` |
| `1436` | `0x5975...9abd` | `LONG` | 1,590,600.00 USD | `1,200.00` | `1179.54` | `1324.80` | `348.01` | 175,157.21 USD | `+11.01%` | `5X Cross` |
| `1475` | `0x69cc...14fd` | `SHORT` | 1,539,150.41 USD | `1,161.36` | `675.33` | `1324.80` | `7870.15` | -754,844.88 USD | `-49.04%` | `10X Cross` |
| `1478` | `0x7a76...b16d` | `LONG` | 1,536,612.39 USD | `1,159.27` | `1358.50` | `1324.80` | `1235.43` | -38,256.13 USD | `-2.49%` | `10X Cross` |
| `1492` | `0x3fc5...c0c1` | `SHORT` | 1,522,257.22 USD | `1,148.44` | `1264.34` | `1324.80` | `3085.19` | -70,243.44 USD | `-4.61%` | `10X Cross` |
| `1509` | `0xe35c...a1d3` | `LONG` | 1,493,805.32 USD | `1,127.06` | `1318.20` | `1324.80` | `694.32` | 8,109.97 USD | `+0.54%` | `2X Isolated` |
| `1517` | `0x5f94...4b96` | `LONG` | 1,478,290.39 USD | `1,115.27` | `538.00` | `1324.80` | `0.000000` | 878,272.75 USD | `+59.41%` | `10X Cross` |
| `1536` | `0x71df...a23d` | `SHORT` | 1,455,290.41 USD | `1,098.28` | `513.50` | `1324.80` | `2546.57` | -891,320.22 USD | `-61.25%` | `2X Cross` |
| `1564` | `0xbfc7...80b4` | `SHORT` | 1,424,052.50 USD | `1,075.00` | `558.03` | `1324.80` | `5414.84` | -824,173.77 USD | `-57.88%` | `10X Cross` |
| `1612` | `0x51f6...2b39` | `SHORT` | 1,377,906.72 USD | `1,039.88` | `1302.72` | `1324.80` | `2862.92` | -23,229.91 USD | `-1.69%` | `10X Cross` |
| `1643` | `0x123d...3bff` | `SHORT` | 1,335,862.47 USD | `1,008.15` | `489.25` | `1324.80` | `4191.93` | -842,628.39 USD | `-63.08%` | `10X Cross` |
| `1651` | `0xe282...df29` | `LONG` | 1,325,400.00 USD | `1,000.00` | `420.99` | `1324.80` | `105.54` | 904,413.14 USD | `+68.24%` | `10X Cross` |
| `1652` | `0x0748...d4b2` | `LONG` | 1,325,000.00 USD | `1,000.00` | `1334.09` | `1324.80` | `0.000000` | -9,088.30 USD | `-0.69%` | `7X Cross` |
| `1653` | `0x266b...efcb` | `LONG` | 1,324,800.00 USD | `1,000.00` | `826.11` | `1324.80` | `154.24` | 498,687.07 USD | `+37.64%` | `10X Cross` |
| `1654` | `0xb5ff...d912` | `LONG` | 1,324,700.00 USD | `1,000.00` | `1141.93` | `1324.80` | `400.44` | 182,769.70 USD | `+13.80%` | `2X Cross` |
| `1677` | `0x17f0...094f` | `LONG` | 1,304,295.93 USD | `984.30` | `1287.23` | `1324.80` | `536.75` | 37,275.77 USD | `+2.86%` | `5X Cross` |
| `1750` | `0x757d...94ba` | `LONG` | 1,225,625.00 USD | `925.00` | `1558.31` | `1324.80` | `0.000000` | -215,815.58 USD | `-17.61%` | `10X Cross` |
| `1806` | `0x2847...d47b` | `LONG` | 1,175,429.96 USD | `887.05` | `1237.95` | `1324.80` | `0.000000` | 77,309.73 USD | `+6.58%` | `5X Cross` |
| `1812` | `0xf096...7553` | `SHORT` | 1,168,034.50 USD | `881.07` | `1240.34` | `1324.80` | `3535.81` | -75,204.41 USD | `-6.44%` | `10X Cross` |
| `1814` | `0xdf95...7d72` | `SHORT` | 1,166,234.69 USD | `880.31` | `1073.82` | `1324.80` | `41370.50` | -220,936.39 USD | `-18.94%` | `10X Cross` |
| `1828` | `0xcf0a...856f` | `LONG` | 1,154,883.55 USD | `871.15` | `1292.19` | `1324.80` | `938.45` | 29,188.71 USD | `+2.53%` | `4X Cross` |
| `1858` | `0x7d0f...ea35` | `LONG` | 1,126,845.00 USD | `850.00` | `1317.57` | `1324.80` | `1275.62` | 6,909.42 USD | `+0.61%` | `10X Cross` |
| `1895` | `0x601c...4f54` | `SHORT` | 1,092,438.94 USD | `824.42` | `615.11` | `1324.80` | `2951.01` | -585,326.19 USD | `-53.58%` | `5X Cross` |
| `1903` | `0xae55...2236` | `LONG` | 1,082,902.51 USD | `817.47` | `1467.80` | `1324.80` | `0.000000` | -116,978.71 USD | `-10.80%` | `10X Cross` |
| `1908` | `0x71b1...79c8` | `LONG` | 1,076,832.76 USD | `812.52` | `1231.55` | `1324.80` | `699.55` | 76,177.30 USD | `+7.07%` | `10X Cross` |
| `1929` | `0x0f02...5384` | `LONG` | 1,061,273.73 USD | `800.78` | `1290.36` | `1324.80` | `290.34` | 27,979.67 USD | `+2.64%` | `3X Cross` |
| `1932` | `0x9b0f...db40` | `LONG` | 1,059,760.00 USD | `800.00` | `1268.86` | `1324.80` | `774.24` | 44,670.24 USD | `+4.22%` | `10X Cross` |
| `1943` | `0xabdb...84ac` | `LONG` | 1,051,321.77 USD | `793.69` | `711.79` | `1324.80` | `664.32` | 486,381.41 USD | `+46.26%` | `3X Cross` |
| `1950` | `0xfdf8...e381` | `LONG` | 1,046,763.25 USD | `790.01` | `1337.72` | `1324.80` | `364.37` | -10,046.44 USD | `-0.96%` | `10X Cross` |
| `2013` | `0x0c1f...1d39` | `SHORT` | 1,011,038.05 USD | `762.99` | `1299.17` | `1324.80` | `4899.74` | -19,786.96 USD | `-1.96%` | `10X Cross` |
| `2018` | `0xf6f3...47f8` | `SHORT` | 1,008,927.94 USD | `761.57` | `1253.10` | `1324.80` | `2387.00` | -54,604.94 USD | `-5.41%` | `5X Cross` |
| `2021` | `0x389a...e76b` | `LONG` | 1,007,552.31 USD | `760.13` | `1266.20` | `1324.80` | `358.57` | 45,078.89 USD | `+4.47%` | `10X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `1297.10` | 194.56 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Long: 0.19K USD at 1297.1000 USD [API] | `2026-10-27 15:46:39` |
| `ANNOUNCEMENT` | `INFO` | `1326.30` | 13.26 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Long: 0.01K USD at 1326.3000 USD [API] | `2026-10-27 23:06:56` |
| `ANNOUNCEMENT` | `INFO` | `1326.50` | 11,341.58 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Long: 11.34K USD at 1326.5000 USD [API] | `2026-10-27 23:06:49` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`1404.15` (Vol: 3,000,000.00 USD, Dist: `+5.98%`) | Long MP=`1287.60` (Vol: 2,300,000.00 USD, Dist: `--2.81%`)
  * 48H Horizon: Short MP=`1404.15` (Vol: 3,000,000.00 USD, Dist: `+5.98%`) | Long MP=`1287.60` (Vol: 2,300,000.00 USD, Dist: `--2.81%`)
  * 3D Horizon: Short MP=`1404.42` (Vol: 3,000,000.00 USD, Dist: `+6.01%`) | Long MP=`1228.81` (Vol: 2,600,000.00 USD, Dist: `--7.25%`)
  * 7D Horizon: Short MP=`1404.10` (Vol: 3,000,000.00 USD, Dist: `+5.98%`) | Long MP=`1200.46` (Vol: 3,000,000.00 USD, Dist: `--9.39%`)
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
  * Current Rate: `85.39K` | Last 24h: `32.07K` | Last 3d: `282.84K` | Last 7d: `777.72K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0079%` | **USDT OKX** | `0.0100%` |
| **USDT Bybit** | `0.0100%` | **USDT KuCoin** | `0.0100%` |
| **USDT MEXC** | `0.0080%` | **USDT BingX** | `0.0065%` |
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
| `0:00 UTC` | `1342.95` | `1346.21` | `1342.95` | `1354.05` | `1340.25` | 27,005,669.33 USD | 14,153,013.83 USD | 12,852,655.50 USD | 1,300,358.33 USD | `+4.82%` | `5B / 3S` |
| `5:00 UTC` | `1348.65` | `1350.13` | `1348.65` | `1356.15` | `1344.45` | 21,612,679.16 USD | 11,526,731.97 USD | 10,085,947.19 USD | 1,440,784.78 USD | `+6.67%` | `2B / 2S` |
| `0:00 UTC` | `1335.45` | `1342.97` | `1335.45` | `1354.95` | `1333.05` | 31,234,081.19 USD | 13,144,149.56 USD | 18,089,931.62 USD | -4,945,782.06 USD | `-15.83%` | `2B / 7S` |
| `5:00 UTC` | `1333.95` | `1332.65` | `1333.95` | `1338.15` | `1327.05` | 42,051,592.22 USD | 20,998,597.47 USD | 21,052,994.75 USD | -54,397.28 USD | `-0.13%` | `1B / 3S` |
| `0:00 UTC` | `1324.05` | `1326.61` | `1324.05` | `1336.05` | `1320.15` | 35,175,848.19 USD | 15,805,961.43 USD | 19,369,886.76 USD | -3,563,925.33 USD | `-10.13%` | `1B / 10S` |
| `5:00 UTC` | `1321.35` | `1325.74` | `1321.35` | `1333.35` | `1318.35` | 26,289,288.34 USD | 11,537,630.34 USD | 14,751,657.99 USD | -3,214,027.65 USD | `-12.23%` | `3B / 5S` |
| `0:00 UTC` | `1315.95` | `1314.40` | `1315.95` | `1321.95` | `1307.85` | 50,919,152.62 USD | 22,517,005.07 USD | 28,402,147.55 USD | -5,885,142.49 USD | `-11.56%` | `2B / 5S` |
| `5:00 UTC` | `1315.95` | `1319.00` | `1315.95` | `1325.85` | `1312.05` | 22,246,351.59 USD | 13,151,982.06 USD | 9,094,369.53 USD | 4,057,612.52 USD | `+18.24%` | `9B / 1S` |
| `0:00 UTC` | `1320.75` | `1319.74` | `1320.75` | `1325.25` | `1315.95` | 11,564,611.33 USD | 5,754,638.99 USD | 5,809,972.34 USD | -55,333.35 USD | `-0.48%` | `1B / 2S` |
| `5:00 UTC` | `1317.45` | `1318.89` | `1317.45` | `1321.05` | `1316.85` | 2,666,053.20 USD | 1,223,824.92 USD | 1,442,228.28 USD | -218,403.36 USD | `-8.19%` | `1B / 0S` |

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
| `5m` | -289,600.00 USD | -735,850.00 USD | **`DISTRIBUTION`** |
| `15m` | -937,870.00 USD | -164,460.00 USD | **`DISTRIBUTION`** |
| `30m` | 885,400.00 USD | 8,380,000.00 USD | **`ACCUMULATION`** |
| `1h` | 451,390.00 USD | -1,800,000.00 USD | **`DISTRIBUTION`** |
| `2h` | -208,210.00 USD | -23,480,000.00 USD | **`DISTRIBUTION`** |
| `4h` | 17,040,000.00 USD | 49,590,000.00 USD | **`ACCUMULATION`** |
| `6h` | 27,930,000.00 USD | 84,160,000.00 USD | **`ACCUMULATION`** |
| `8h` | 32,260,000.00 USD | 101,620,000.00 USD | **`ACCUMULATION`** |
| `12h` | 27,800,000.00 USD | 111,090,000.00 USD | **`ACCUMULATION`** |
| `24h` | 12,520,000.00 USD | 75,960,000.00 USD | **`ACCUMULATION`** |
| `1w` | 49,660,000.00 USD | 251,000,000.00 USD | **`ACCUMULATION`** |
| `30d` | 65,790,000.00 USD | -508,370,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-289.60K` | 15m=`-937.87K` | 1h=`+451.39K` | 24h=`+12.52M`
* Futures Capital Netflows: 5m=`-735.85K` | 15m=`-164.46K` | 1h=`-1.80M` | 24h=`+75.96M`
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
  * `2026-10-30 00:48:09 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 00:17:09 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 00:49:09 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 00:49:09 IST`: [@DeItaone] - (Sentiment: `Neutral`)
  * `2026-10-30 00:49:09 IST`: [@mb_ghalibaf] - (Sentiment: `Neutral`)
  * `2026-10-30 00:49:09 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-30 00:49:09 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-30 00:48:09 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-30 00:48:09 IST`: [fxstreet.com] - (Sentiment: `Neutral`)
  * `2026-10-29 21:50:09 IST`: [ForexFactory] - (Sentiment: `Neutral`)
  * `2026-10-29 21:50:09 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-29 21:50:09 IST`: [youtube.com/bankofcanadaofficial] - (Sentiment: `Neutral`)
  * `2026-10-29 20:50:09 IST`: [notayesmanseconomics.wordpress.com] - (Sentiment: `Neutral`)
  * `2026-10-29 20:50:09 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 20:50:09 IST`: [breakingthenews.net] - (Sentiment: `Neutral`)


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
  * Spread-Padded Stop Loss: `1209.66` (Risk Distance: `20.89` pts)
  * +2.5R Take Profit: `1282.78`
  * Mathematical Lot Sizing: **`0.47 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `1307.14` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `1328.03` (Risk Distance: `20.89` pts)
  * +2.5R Take Profit: `1254.91`
  * Mathematical Lot Sizing: **`0.47 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`1332.65`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
