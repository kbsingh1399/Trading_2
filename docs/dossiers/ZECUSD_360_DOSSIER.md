# 🏛️ SOVEREIGN CANDIDATE DOSSIER: ZECUSD
**Canonical Key**: `ZECUSD` | **Broker Instrument**: `ZECUSD.p` | **Asset Class**: `Crypto Altcoin`
**Timestamp**: `2026-10-29 22:55:04 IST` (`2026-10-29 17:25:04 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `1346.65` | **Live Ask Quote**: `1347.58` | **Mid Price**: `1347.12`
- **Spread Points**: `93.00` | **Spread BPS**: `6.90 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `1347.12` | VWAP Z-Score: `+0.00` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `3.37` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `50.00` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `1356.54` | Lower -3.00σ Band: `1337.69`
  * Upper +2.51σ Band: `1354.52` | Lower -2.51σ Band: `1339.71`
  * Upper +2.01σ Band: `1352.77` | Lower -2.01σ Band: `1341.46`
  * Upper +2.00σ Band: `1352.50` | Lower -2.00σ Band: `1341.73`
  * Upper +1.28σ Band: `1350.89` | Lower -1.28σ Band: `1343.34`
  * Upper +1.00σ Band: `1349.81` | Lower -1.00σ Band: `1344.42`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`1347.12` | EMA-20=`1347.12` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`1347.12` (Slope: `+0.0000`) | EMA-100=`1347.12`
  * Institutional Anchors: EMA-144=`1347.12` | EMA-200=`1347.12` (Slope: `+0.0000`) | EMA-233=`1347.12`
- **Range Boundaries**: 24H High=`1360.59` | 24H Low=`1333.64` | Weekly High=`1374.06` | Weekly Low=`1320.17`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `1300.48` (Distance: `+3.56%`)
  * Point of Control (POC) = `1247.20` (Distance: `+7.98%`)
  * Value Area Low (VAL) = `1230.55` (Distance: `+9.45%`)
  * Auction Positioning: `ABOVE_VALUE (Imbalance)` | Session Bias: **`BULLISH (Above Pivot)`** | Market Regime: `TREND_UP_ACCEPTANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`1320.44` | POC=`1312.10` | VAL=`1285.78`
  * Prior Day Extremes: PDH=`1328.99` | PDL=`1263.19` | PDC=`1296.46`
  * Monday Range Blueprint: High=`1267.53` | Mid=`1222.14` | Low=`1176.75`
  * Developing Weekly Value Area: Weekly VAH=`1293.21` | Weekly POC=`1239.01` | Weekly VAL=`1195.06`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`1318.68` | Low=`1230.00`
  * London Session (08:00-16:00 UTC): High=`1276.13` | Low=`1233.52`
  * New York Session (13:00-21:00 UTC): High=`1396.49` | Low=`1250.65`
  * Initial Balance (First Hour): IB High=`1255.79` | IB Low=`1245.43`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `1341.73` - `1352.50`
  * Optimal Trade Entry (OTE 0.705): `1349.81`
  * Structural Invalidation Anchor (0.786): `1357.89`

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
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-29 22:54:46 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `16` | `0xb83d...6e36` | `SHORT` | 71,107,341.80 USD | `52,582.52` | `1336.45` | `1353.10` | `3640.77` | -833,426.90 USD | `-1.17%` | `3X Cross` |
| `22` | `0x5b5d...c060` | `SHORT` | 55,100,383.57 USD | `40,727.61` | `1478.36` | `1353.10` | `4884.74` | 5,109,880.62 USD | `+9.27%` | `3X Cross` |
| `42` | `0x7fda...17d1` | `SHORT` | 30,307,315.63 USD | `22,398.43` | `1261.01` | `1353.10` | `2942.04` | -2,062,643.50 USD | `-6.81%` | `5X Cross` |
| `81` | `0x60b0...991e` | `LONG` | 22,656,004.95 USD | `16,779.74` | `1179.65` | `1353.10` | `870.77` | 2,861,757.93 USD | `+12.63%` | `10X Cross` |
| `86` | `0xbf73...5d58` | `LONG` | 21,649,600.00 USD | `16,000.00` | `1214.30` | `1353.10` | `705.47` | 2,220,767.75 USD | `+10.26%` | `10X Cross` |
| `131` | `0xc36a...105b` | `LONG` | 15,545,362.41 USD | `11,510.82` | `1215.14` | `1353.10` | `921.30` | 1,558,081.38 USD | `+10.02%` | `10X Cross` |
| `172` | `0x8742...8427` | `LONG` | 12,428,074.35 USD | `9,201.21` | `1286.37` | `1353.10` | `698.32` | 591,904.35 USD | `+4.76%` | `10X Cross` |
| `193` | `0xad59...ba81` | `SHORT` | 11,373,750.00 USD | `8,425.00` | `330.91` | `1353.10` | `2137.83` | -8,585,792.23 USD | `-75.49%` | `10X Cross` |
| `202` | `0xdd53...2b13` | `SHORT` | 11,145,068.44 USD | `8,237.91` | `739.37` | `1353.10` | `7627.45` | -5,054,181.41 USD | `-45.35%` | `3X Cross` |
| `206` | `0x9ffd...ce40` | `LONG` | 10,918,065.35 USD | `8,070.12` | `1249.44` | `1353.10` | `553.99` | 834,918.85 USD | `+7.65%` | `5X Cross` |
| `209` | `0xfc66...ca06` | `SHORT` | 10,797,873.31 USD | `7,980.10` | `1319.26` | `1353.10` | `5429.58` | -270,047.49 USD | `-2.50%` | `10X Cross` |
| `220` | `0x880a...311c` | `SHORT` | 10,428,490.54 USD | `7,707.11` | `1367.50` | `1353.10` | `2298.82` | 110,993.66 USD | `+1.06%` | `10X Cross` |
| `269` | `0x2b61...2f6c` | `LONG` | 9,195,576.30 USD | `6,807.00` | `1453.56` | `1353.10` | `657.67` | -698,774.92 USD | `-7.60%` | `10X Cross` |
| `285` | `0x2ae5...83e7` | `LONG` | 8,699,335.20 USD | `6,436.80` | `1391.82` | `1353.10` | `0.000000` | -259,556.79 USD | `-2.98%` | `2X Cross` |
| `319` | `0xecb6...2b00` | `SHORT` | 7,942,588.75 USD | `5,869.92` | `1323.71` | `1353.10` | `6686.25` | -172,540.87 USD | `-2.17%` | `5X Cross` |
| `332` | `0x26b6...9a13` | `LONG` | 7,343,686.09 USD | `5,433.73` | `1282.23` | `1353.10` | `195.75` | 376,382.86 USD | `+5.13%` | `10X Cross` |
| `340` | `0x45d2...4029` | `SHORT` | 7,064,290.50 USD | `5,227.00` | `833.44` | `1353.10` | `7745.22` | -2,707,912.53 USD | `-38.33%` | `5X Cross` |
| `359` | `0xea00...a918` | `LONG` | 6,762,000.00 USD | `5,000.00` | `739.16` | `1353.10` | `0.000000` | 3,066,184.89 USD | `+45.34%` | `5X Cross` |
| `361` | `0x469e...58a5` | `SHORT` | 6,756,500.00 USD | `5,000.00` | `1190.36` | `1353.10` | `1803.13` | -804,715.10 USD | `-11.91%` | `10X Cross` |
| `378` | `0xdd7a...8830` | `LONG` | 6,572,434.94 USD | `4,860.19` | `897.48` | `1353.10` | `792.17` | 2,210,531.26 USD | `+33.63%` | `10X Cross` |
| `386` | `0xf081...e39e` | `LONG` | 6,375,025.50 USD | `4,717.00` | `1195.70` | `1353.10` | `1200.06` | 734,901.45 USD | `+11.53%` | `10X Cross` |
| `447` | `0x4cae...7c34` | `LONG` | 5,409,489.92 USD | `4,004.36` | `999.34` | `1353.10` | `676.54` | 1,407,761.77 USD | `+26.02%` | `10X Cross` |
| `449` | `0x382b...3e39` | `LONG` | 5,356,868.78 USD | `3,958.96` | `1166.42` | `1353.10` | `0.000000` | 739,076.41 USD | `+13.80%` | `10X Cross` |
| `456` | `0xa61c...66b9` | `LONG` | 5,257,742.40 USD | `3,888.00` | `1148.34` | `1353.10` | `0.000000` | 793,000.26 USD | `+15.08%` | `10X Cross` |
| `478` | `0x9aa5...58af` | `SHORT` | 5,019,070.22 USD | `3,720.31` | `1205.51` | `1353.10` | `3234.46` | -534,183.42 USD | `-10.64%` | `10X Cross` |
| `481` | `0x0153...8052` | `SHORT` | 5,004,007.36 USD | `3,698.18` | `1307.82` | `1353.10` | `2504.65` | -167,436.61 USD | `-3.35%` | `1X Isolated` |
| `512` | `0xd4c1...3d1d` | `SHORT` | 4,688,450.91 USD | `3,464.97` | `1302.89` | `1353.10` | `2595.51` | -173,992.85 USD | `-3.71%` | `10X Cross` |
| `538` | `0xd21d...90f1` | `LONG` | 4,394,975.00 USD | `3,250.00` | `1253.64` | `1353.10` | `875.85` | 320,633.27 USD | `+7.30%` | `4X Isolated` |
| `553` | `0x1338...c48e` | `LONG` | 4,261,493.73 USD | `3,149.43` | `1018.52` | `1353.10` | `820.14` | 1,053,748.19 USD | `+24.73%` | `4X Isolated` |
| `563` | `0x456f...cdf1` | `LONG` | 4,208,357.75 USD | `3,111.77` | `1267.78` | `1353.10` | `486.79` | 263,319.42 USD | `+6.26%` | `10X Cross` |
| `566` | `0xdbe0...d6d5` | `LONG` | 4,174,814.15 USD | `3,085.37` | `422.97` | `1353.10` | `338.46` | 2,869,809.65 USD | `+68.74%` | `3X Isolated` |
| `592` | `0x9c06...0560` | `SHORT` | 4,039,817.76 USD | `2,989.80` | `786.00` | `1353.10` | `2343.71` | -1,689,822.76 USD | `-41.83%` | `10X Cross` |
| `626` | `0x27c9...d65d` | `SHORT` | 3,825,635.92 USD | `2,827.73` | `1245.62` | `1353.10` | `1815.36` | -303,372.06 USD | `-7.93%` | `10X Cross` |
| `687` | `0xac48...3201` | `LONG` | 3,434,739.63 USD | `2,540.30` | `1393.86` | `1353.10` | `525.76` | -106,089.66 USD | `-3.09%` | `10X Cross` |
| `692` | `0xa183...0482` | `LONG` | 3,422,673.80 USD | `2,534.00` | `530.25` | `1353.10` | `444.38` | 2,079,011.08 USD | `+60.74%` | `5X Isolated` |
| `699` | `0x325e...9564` | `LONG` | 3,383,332.89 USD | `2,501.91` | `1306.24` | `1353.10` | `0.000000` | 115,238.99 USD | `+3.41%` | `10X Cross` |
| `700` | `0x0871...e927` | `LONG` | 3,376,750.00 USD | `2,500.00` | `1276.50` | `1353.10` | `0.000000` | 185,500.00 USD | `+5.49%` | `10X Cross` |
| `710` | `0x9b86...6e6e` | `LONG` | 3,336,529.79 USD | `2,467.30` | `637.58` | `1353.10` | `889.61` | 1,763,430.19 USD | `+52.85%` | `3X Cross` |
| `758` | `0xb2f7...af9f` | `SHORT` | 3,128,843.56 USD | `2,313.72` | `746.63` | `1353.10` | `4162.78` | -1,401,354.81 USD | `-44.79%` | `10X Cross` |
| `789` | `0x2e30...4cb5` | `SHORT` | 3,024,908.52 USD | `2,235.87` | `1295.46` | `1353.10` | `3342.14` | -128,425.91 USD | `-4.25%` | `2X Cross` |
| `792` | `0xf48f...10fe` | `LONG` | 3,000,064.03 USD | `2,218.49` | `1517.87` | `1353.10` | `870.46` | -367,322.80 USD | `-12.24%` | `3X Cross` |
| `825` | `0x5bc4...3b0c` | `SHORT` | 2,879,055.89 USD | `2,130.74` | `1089.65` | `1353.10` | `3531.52` | -557,298.31 USD | `-19.36%` | `5X Cross` |
| `848` | `0x71d0...8c26` | `SHORT` | 2,806,983.39 USD | `2,074.79` | `1362.27` | `1353.10` | `4994.76` | 19,440.94 USD | `+0.69%` | `10X Cross` |
| `850` | `0x4fe2...ac59` | `SHORT` | 2,799,105.38 USD | `2,071.57` | `1478.56` | `1353.10` | `1795.19` | 263,840.83 USD | `+9.43%` | `10X Cross` |
| `852` | `0x4e23...20c3` | `LONG` | 2,794,577.30 USD | `2,065.62` | `1302.47` | `1353.10` | `0.000000` | 104,166.55 USD | `+3.73%` | `4X Cross` |
| `867` | `0x668c...ea2e` | `SHORT` | 2,702,600.00 USD | `2,000.00` | `1409.16` | `1353.10` | `2701.61` | 115,722.04 USD | `+4.28%` | `10X Cross` |
| `868` | `0x362a...1d9f` | `SHORT` | 2,701,559.50 USD | `1,999.23` | `1382.50` | `1353.10` | `1675.46` | 62,377.90 USD | `+2.31%` | `5X Cross` |
| `887` | `0x77ee...2902` | `SHORT` | 2,628,891.93 USD | `1,946.03` | `759.84` | `1353.10` | `5303.84` | -1,150,214.42 USD | `-43.75%` | `10X Cross` |
| `896` | `0x3e2f...b269` | `SHORT` | 2,601,749.11 USD | `1,925.51` | `1134.87` | `1353.10` | `2931.71` | -416,550.26 USD | `-16.01%` | `10X Cross` |
| `902` | `0xe097...d0fe` | `LONG` | 2,589,238.04 USD | `1,913.56` | `1261.17` | `1353.10` | `0.000000` | 175,911.87 USD | `+6.79%` | `10X Cross` |
| `909` | `0x4f12...618b` | `SHORT` | 2,564,529.07 USD | `1,896.28` | `1608.30` | `1353.10` | `2116.67` | 485,255.32 USD | `+18.92%` | `3X Cross` |
| `948` | `0x866d...d6e1` | `LONG` | 2,436,371.60 USD | `1,802.05` | `674.73` | `1353.10` | `39.41` | 1,220,470.29 USD | `+50.09%` | `10X Cross` |
| `978` | `0x2309...a2d9` | `LONG` | 2,363,699.65 USD | `1,750.37` | `1186.09` | `1353.10` | `799.00` | 287,605.54 USD | `+12.17%` | `8X Cross` |
| `1007` | `0x2edd...8179` | `SHORT` | 2,294,775.45 USD | `1,696.19` | `1259.73` | `1353.10` | `2922.87` | -158,042.25 USD | `-6.89%` | `10X Cross` |
| `1031` | `0x023a...2355` | `SHORT` | 2,233,697.48 USD | `1,650.80` | `1310.64` | `1353.10` | `6516.42` | -70,092.99 USD | `-3.14%` | `10X Cross` |
| `1033` | `0x265e...7f70` | `LONG` | 2,231,831.09 USD | `1,651.74` | `1388.09` | `1353.10` | `0.000000` | -60,938.60 USD | `-2.73%` | `3X Cross` |
| `1041` | `0xa271...a3f7` | `LONG` | 2,204,388.22 USD | `1,631.43` | `1190.60` | `1353.10` | `910.24` | 262,006.41 USD | `+11.89%` | `4X Cross` |
| `1049` | `0x7f75...9edf` | `LONG` | 2,172,780.92 USD | `1,605.78` | `1199.97` | `1353.10` | `975.31` | 245,889.03 USD | `+11.32%` | `10X Cross` |
| `1051` | `0x6646...6de5` | `SHORT` | 2,164,960.00 USD | `1,600.00` | `660.64` | `1353.10` | `4926.15` | -1,107,935.03 USD | `-51.18%` | `10X Cross` |
| `1062` | `0xdf57...93f5` | `LONG` | 2,134,571.71 USD | `1,579.76` | `1218.38` | `1353.10` | `780.08` | 209,815.73 USD | `+9.83%` | `3X Isolated` |
| `1072` | `0xab59...59b5` | `LONG` | 2,116,782.24 USD | `1,565.32` | `1342.15` | `1353.10` | `779.40` | 15,887.02 USD | `+0.75%` | `10X Cross` |
| `1077` | `0xfe7c...b7ae` | `SHORT` | 2,109,998.80 USD | `1,560.65` | `1350.64` | `1353.10` | `6231.09` | -2,125.05 USD | `-0.10%` | `10X Cross` |
| `1089` | `0x634f...6951` | `LONG` | 2,094,375.80 USD | `1,553.00` | `1263.46` | `1353.10` | `1184.28` | 132,226.22 USD | `+6.31%` | `10X Cross` |
| `1098` | `0x3e47...aaf6` | `LONG` | 2,077,511.44 USD | `1,536.28` | `1277.06` | `1353.10` | `1010.01` | 115,589.36 USD | `+5.56%` | `10X Cross` |
| `1121` | `0xcf67...eb24` | `LONG` | 2,026,800.00 USD | `1,500.00` | `887.05` | `1353.10` | `472.61` | 696,228.63 USD | `+34.35%` | `10X Cross` |
| `1141` | `0x039c...0ebd` | `SHORT` | 2,003,251.02 USD | `1,480.49` | `1238.67` | `1353.10` | `3102.91` | -169,419.70 USD | `-8.46%` | `10X Cross` |
| `1205` | `0x7a76...b16d` | `LONG` | 1,914,255.45 USD | `1,415.66` | `1362.09` | `1353.10` | `1253.18` | -13,999.80 USD | `-0.73%` | `10X Cross` |
| `1226` | `0x9546...181c` | `LONG` | 1,893,533.85 USD | `1,400.75` | `1348.55` | `1353.10` | `0.000000` | 4,546.28 USD | `+0.24%` | `10X Cross` |
| `1229` | `0x2ab7...c2f8` | `LONG` | 1,892,789.26 USD | `1,400.51` | `813.26` | `1353.10` | `790.68` | 753,807.58 USD | `+39.83%` | `3X Cross` |
| `1250` | `0x11be...8b1d` | `LONG` | 1,860,122.16 USD | `1,375.83` | `1206.55` | `1353.10` | `1134.36` | 200,114.20 USD | `+10.76%` | `10X Isolated` |
| `1303` | `0xef96...9383` | `SHORT` | 1,770,048.17 USD | `1,308.82` | `1249.96` | `1353.10` | `4054.58` | -134,081.75 USD | `-7.58%` | `10X Cross` |
| `1319` | `0xfc27...9d9d` | `SHORT` | 1,739,477.65 USD | `1,285.74` | `1314.84` | `1353.10` | `11928.99` | -48,929.16 USD | `-2.81%` | `10X Cross` |
| `1321` | `0x5323...b23c` | `SHORT` | 1,735,729.62 USD | `1,282.78` | `1360.23` | `1353.10` | `5778.09` | 9,144.36 USD | `+0.53%` | `5X Cross` |
| `1340` | `0xdf83...3cff` | `SHORT` | 1,710,962.01 USD | `1,266.16` | `1240.89` | `1353.10` | `1883.18` | -139,794.42 USD | `-8.17%` | `10X Cross` |
| `1343` | `0xe065...0f85` | `SHORT` | 1,706,038.63 USD | `1,262.61` | `1087.02` | `1353.10` | `1603.57` | -333,562.50 USD | `-19.55%` | `10X Cross` |
| `1371` | `0x7277...0b98` | `SHORT` | 1,668,677.95 USD | `1,234.96` | `1298.48` | `1353.10` | `2337.88` | -65,108.53 USD | `-3.90%` | `10X Cross` |
| `1409` | `0x5975...9abd` | `LONG` | 1,622,400.00 USD | `1,200.00` | `1179.54` | `1353.10` | `268.95` | 206,957.21 USD | `+12.76%` | `5X Cross` |
| `1466` | `0x69cc...14fd` | `SHORT` | 1,569,229.63 USD | `1,161.36` | `675.33` | `1353.10` | `7744.70` | -784,924.10 USD | `-50.02%` | `10X Cross` |
| `1479` | `0x3fc5...c0c1` | `SHORT` | 1,552,690.88 USD | `1,148.44` | `1264.34` | `1353.10` | `2983.49` | -100,677.10 USD | `-6.48%` | `10X Cross` |
| `1514` | `0x5f94...4b96` | `LONG` | 1,507,064.35 USD | `1,115.27` | `538.00` | `1353.10` | `0.000000` | 907,046.71 USD | `+60.19%` | `10X Cross` |
| `1535` | `0x71df...a23d` | `SHORT` | 1,483,666.45 USD | `1,098.28` | `513.50` | `1353.10` | `2543.86` | -919,696.26 USD | `-61.99%` | `2X Cross` |
| `1565` | `0xbfc7...80b4` | `SHORT` | 1,451,787.50 USD | `1,075.00` | `558.03` | `1353.10` | `5175.86` | -851,908.77 USD | `-58.68%` | `10X Cross` |
| `1613` | `0x51f6...2b39` | `SHORT` | 1,407,061.63 USD | `1,039.88` | `1302.72` | `1353.10` | `2854.13` | -52,384.82 USD | `-3.72%` | `10X Cross` |
| `1644` | `0x123d...3bff` | `SHORT` | 1,363,518.87 USD | `1,007.70` | `488.87` | `1353.10` | `4137.95` | -870,883.75 USD | `-63.87%` | `10X Cross` |
| `1651` | `0x266b...efcb` | `LONG` | 1,353,100.00 USD | `1,000.00` | `826.11` | `1353.10` | `133.71` | 526,987.07 USD | `+38.95%` | `10X Cross` |
| `1652` | `0xe282...df29` | `LONG` | 1,352,300.00 USD | `1,000.00` | `420.99` | `1353.10` | `84.44` | 931,313.14 USD | `+68.87%` | `10X Cross` |
| `1654` | `0xb5ff...d912` | `LONG` | 1,351,500.00 USD | `1,000.00` | `1141.93` | `1353.10` | `400.40` | 209,569.70 USD | `+15.51%` | `2X Cross` |
| `1656` | `0x0748...d4b2` | `LONG` | 1,350,700.00 USD | `1,000.00` | `1334.09` | `1353.10` | `0.000000` | 16,611.70 USD | `+1.23%` | `7X Cross` |
| `1671` | `0x17f0...094f` | `LONG` | 1,330,281.45 USD | `984.30` | `1287.23` | `1353.10` | `536.71` | 63,261.29 USD | `+4.76%` | `5X Cross` |
| `1749` | `0x757d...94ba` | `LONG` | 1,249,860.00 USD | `925.00` | `1558.31` | `1353.10` | `0.000000` | -191,580.58 USD | `-15.33%` | `10X Cross` |
| `1757` | `0x5d90...eea3` | `LONG` | 1,244,544.80 USD | `920.93` | `1288.61` | `1353.10` | `904.51` | 57,827.55 USD | `+4.65%` | `3X Isolated` |
| `1765` | `0x3205...40bb` | `SHORT` | 1,235,285.58 USD | `912.93` | `1342.91` | `1353.10` | `2730.59` | -9,301.84 USD | `-0.75%` | `10X Cross` |
| `1817` | `0xf096...7553` | `SHORT` | 1,190,501.78 USD | `881.07` | `1240.34` | `1353.10` | `3447.17` | -97,671.70 USD | `-8.20%` | `10X Cross` |
| `1818` | `0xdf95...7d72` | `SHORT` | 1,190,430.24 USD | `879.91` | `1073.66` | `1353.10` | `40495.49` | -245,706.19 USD | `-20.64%` | `10X Cross` |
| `1831` | `0xcf0a...856f` | `LONG` | 1,177,620.57 USD | `871.15` | `1292.19` | `1353.10` | `938.42` | 51,925.72 USD | `+4.41%` | `4X Cross` |
| `1844` | `0x2847...d47b` | `LONG` | 1,165,212.63 USD | `860.38` | `1235.10` | `1353.10` | `0.000000` | 102,556.24 USD | `+8.80%` | `5X Cross` |
| `1866` | `0x7d0f...ea35` | `LONG` | 1,149,030.00 USD | `850.00` | `1317.57` | `1353.10` | `1275.59` | 29,094.42 USD | `+2.53%` | `10X Cross` |
| `1878` | `0xe35c...a1d3` | `LONG` | 1,141,014.07 USD | `844.57` | `1306.64` | `1353.10` | `688.39` | 37,465.31 USD | `+3.28%` | `2X Isolated` |
| `1903` | `0x601c...4f54` | `SHORT` | 1,114,038.75 USD | `824.42` | `615.11` | `1353.10` | `2897.19` | -606,925.99 USD | `-54.48%` | `5X Cross` |
| `1913` | `0xae55...2236` | `LONG` | 1,104,810.71 USD | `817.47` | `1467.80` | `1353.10` | `0.000000` | -95,070.51 USD | `-8.61%` | `10X Cross` |
| `1922` | `0x71b1...79c8` | `LONG` | 1,097,714.52 USD | `812.52` | `1231.55` | `1353.10` | `652.90` | 97,059.07 USD | `+8.84%` | `10X Cross` |
| `1937` | `0x9b0f...db40` | `LONG` | 1,082,480.00 USD | `800.00` | `1268.86` | `1353.10` | `772.82` | 67,390.24 USD | `+6.23%` | `10X Cross` |
| `1938` | `0x0f02...5384` | `LONG` | 1,082,414.33 USD | `800.78` | `1290.36` | `1353.10` | `282.41` | 49,120.26 USD | `+4.54%` | `3X Cross` |
| `1958` | `0xabdb...84ac` | `LONG` | 1,071,878.34 USD | `793.69` | `711.79` | `1353.10` | `664.28` | 506,937.98 USD | `+47.29%` | `3X Cross` |
| `1964` | `0xfdf8...e381` | `LONG` | 1,067,066.51 USD | `790.01` | `1337.72` | `1353.10` | `185.30` | 10,256.82 USD | `+0.96%` | `10X Cross` |
| `2009` | `0x0c1f...1d39` | `SHORT` | 1,030,952.09 USD | `762.99` | `1299.17` | `1353.10` | `4626.04` | -39,701.00 USD | `-3.85%` | `10X Cross` |
| `2010` | `0xf6f3...47f8` | `SHORT` | 1,030,328.05 USD | `761.57` | `1253.10` | `1353.10` | `2311.77` | -76,005.06 USD | `-7.38%` | `5X Cross` |
| `2012` | `0x389a...e76b` | `LONG` | 1,028,379.88 USD | `760.13` | `1266.20` | `1353.10` | `366.75` | 65,906.46 USD | `+6.41%` | `10X Cross` |
| `2025` | `0xadd1...5e0d` | `LONG` | 1,015,663.92 USD | `750.62` | `1195.15` | `1353.10` | `0.000000` | 118,562.82 USD | `+11.67%` | `10X Cross` |
| `2043` | `0xd6e1...f256` | `SHORT` | 1,008,121.96 USD | `746.37` | `1368.65` | `1353.10` | `2024.20` | 13,393.82 USD | `+1.33%` | `10X Cross` |
| `2053` | `0x87a7...9fa2` | `SHORT` | 1,005,183.00 USD | `744.58` | `1464.55` | `1353.10` | `1711.91` | 85,293.74 USD | `+8.49%` | `10X Cross` |
| `2060` | `0x8923...1bac` | `LONG` | 1,003,487.74 USD | `742.06` | `1239.64` | `1353.10` | `696.13` | 83,601.21 USD | `+8.33%` | `5X Cross` |
| `2064` | `0xb122...e4ba` | `LONG` | 1,001,387.83 USD | `741.11` | `1299.26` | `1353.10` | `908.08` | 38,495.67 USD | `+3.84%` | `10X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `1304.60` | 10,019.33 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Long: 10.02K USD at 1304.6000 USD [API] | `2026-10-27 16:27:21` |
| `ANNOUNCEMENT` | `INFO` | `1289.60` | 10,407.07 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Long: 10.41K USD at 1289.6000 USD [API] | `2026-10-27 15:20:59` |
| `ANNOUNCEMENT` | `INFO` | `1297.10` | 194.56 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Long: 0.19K USD at 1297.1000 USD [API] | `2026-10-27 15:46:39` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`1404.15` (Vol: 3,000,000.00 USD, Dist: `+4.12%`) | Long MP=`1287.60` (Vol: 2,300,000.00 USD, Dist: `--4.53%`)
  * 48H Horizon: Short MP=`1404.15` (Vol: 3,000,000.00 USD, Dist: `+4.12%`) | Long MP=`0.000000` (Vol: 0.00 USD, Dist: `-0.00%`)
  * 3D Horizon: Short MP=`1404.42` (Vol: 3,000,000.00 USD, Dist: `+4.14%`) | Long MP=`0.000000` (Vol: 0.00 USD, Dist: `-0.00%`)
  * 7D Horizon: Short MP=`1404.10` (Vol: 3,000,000.00 USD, Dist: `+4.11%`) | Long MP=`1200.46` (Vol: 3,000,000.00 USD, Dist: `--10.99%`)
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
  * Current Rate: `83.52K` | Last 24h: `32.07K` | Last 3d: `282.84K` | Last 7d: `777.72K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0081%` | **USDT OKX** | `0.0073%` |
| **USDT Bybit** | `0.0100%` | **USDT KuCoin** | `0.0091%` |
| **USDT MEXC** | `0.0080%` | **USDT BingX** | `0.0030%` |
| **USDT Gate** | `0.0100%` | **USDT Bitget** | `0.0041%` |
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
| `0:00 UTC` | `1320.15` | `1314.27` | `1320.15` | `1324.95` | `1296.75` | 56,796,886.08 USD | 33,062,545.27 USD | 23,734,340.81 USD | 9,328,204.46 USD | `+16.42%` | `18B / 3S` |
| `5:00 UTC` | `1317.75` | `1318.00` | `1317.75` | `1324.05` | `1313.25` | 29,849,949.75 USD | 16,298,218.14 USD | 13,551,731.61 USD | 2,746,486.54 USD | `+9.20%` | `4B / 2S` |
| `0:00 UTC` | `1345.05` | `1339.86` | `1345.05` | `1353.45` | `1318.65` | 81,702,422.73 USD | 46,151,799.06 USD | 35,550,623.66 USD | 10,601,175.40 USD | `+12.98%` | `23B / 1S` |
| `5:00 UTC` | `1360.05` | `1349.51` | `1360.05` | `1362.15` | `1334.25` | 65,905,391.58 USD | 39,286,823.07 USD | 26,618,568.52 USD | 12,668,254.55 USD | `+19.22%` | `19B / 3S` |
| `0:00 UTC` | `1369.95` | `1375.81` | `1369.95` | `1397.55` | `1350.75` | 159,915,504.01 USD | 87,974,917.65 USD | 71,940,586.35 USD | 16,034,331.30 USD | `+10.03%` | `21B / 3S` |
| `5:00 UTC` | `1359.75` | `1358.32` | `1359.75` | `1373.25` | `1346.25` | 77,512,400.13 USD | 36,921,415.88 USD | 40,590,984.25 USD | -3,669,568.36 USD | `-4.73%` | `4B / 13S` |
| `0:00 UTC` | `1353.15` | `1350.71` | `1353.15` | `1361.25` | `1341.75` | 52,010,841.39 USD | 26,247,439.78 USD | 25,763,401.61 USD | 484,038.17 USD | `+0.93%` | `5B / 3S` |
| `5:00 UTC` | `1343.25` | `1344.85` | `1343.25` | `1353.45` | `1340.25` | 26,552,172.39 USD | 11,915,117.49 USD | 14,637,054.90 USD | -2,721,937.40 USD | `-10.25%` | `0B / 9S` |
| `0:00 UTC` | `1342.95` | `1346.21` | `1342.95` | `1354.05` | `1340.25` | 27,005,669.33 USD | 14,153,013.83 USD | 12,852,655.50 USD | 1,300,358.33 USD | `+4.82%` | `5B / 3S` |
| `5:00 UTC` | `1349.85` | `1349.54` | `1349.85` | `1354.95` | `1344.45` | 12,634,407.63 USD | 7,335,095.76 USD | 5,299,311.86 USD | 2,035,783.90 USD | `+16.11%` | `5B / 2S` |

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
| `5m` | 4,330,000.00 USD | 4,950,000.00 USD | **`ACCUMULATION`** |
| `15m` | 6,170,000.00 USD | 3,250,000.00 USD | **`ACCUMULATION`** |
| `30m` | 5,040,000.00 USD | -441,350.00 USD | **`ACCUMULATION`** |
| `1h` | 3,100,000.00 USD | -1,150,000.00 USD | **`ACCUMULATION`** |
| `2h` | 18,010,000.00 USD | 69,730,000.00 USD | **`ACCUMULATION`** |
| `4h` | 28,930,000.00 USD | 103,570,000.00 USD | **`ACCUMULATION`** |
| `6h` | 31,130,000.00 USD | 113,110,000.00 USD | **`ACCUMULATION`** |
| `8h` | 28,740,000.00 USD | 130,070,000.00 USD | **`ACCUMULATION`** |
| `12h` | 27,610,000.00 USD | 115,540,000.00 USD | **`ACCUMULATION`** |
| `24h` | 18,010,000.00 USD | 127,640,000.00 USD | **`ACCUMULATION`** |
| `1w` | 55,560,000.00 USD | 282,250,000.00 USD | **`ACCUMULATION`** |
| `30d` | 70,940,000.00 USD | -490,340,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+4.33M` | 15m=`+6.17M` | 1h=`+3.10M` | 24h=`+18.01M`
* Futures Capital Netflows: 5m=`+4.95M` | 15m=`+3.25M` | 1h=`-1.15M` | 24h=`+127.64M`
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
  * `2026-10-29 22:45:14 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:06:14 IST`: [fxstreet.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:50:14 IST`: [ForexFactory] - (Sentiment: `Neutral`)
  * `2026-10-29 22:50:14 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-29 22:50:14 IST`: [youtube.com/bankofcanadaofficial] - (Sentiment: `Neutral`)
  * `2026-10-29 22:49:14 IST`: [notayesmanseconomics.wordpress.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:49:14 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:49:14 IST`: [breakingthenews.net] - (Sentiment: `Neutral`)
  * `2026-10-29 19:51:14 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-29 19:51:14 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-29 19:51:14 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-29 19:51:14 IST`: [youtube.com/ecbeuro] - (Sentiment: `Neutral`)
  * `2026-10-29 18:51:14 IST`: [ecb.europa.eu] - (Sentiment: `Neutral`)
  * `2026-10-29 18:51:14 IST`: [zerohedge.com] - (Sentiment: `Neutral`)
  * `2026-10-29 18:51:14 IST`: [dol.gov] - (Sentiment: `Neutral`)


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
  * Spread-Padded Stop Loss: `1225.11` (Risk Distance: `5.44` pts)
  * +2.5R Take Profit: `1244.14`
  * Mathematical Lot Sizing: **`1.83 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `1300.48` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `1305.92` (Risk Distance: `5.44` pts)
  * +2.5R Take Profit: `1286.89`
  * Mathematical Lot Sizing: **`1.83 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`1357.89`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
