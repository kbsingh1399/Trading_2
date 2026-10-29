# 🏛️ SOVEREIGN CANDIDATE DOSSIER: ZECUSD
**Canonical Key**: `ZECUSD` | **Broker Instrument**: `ZECUSD.p` | **Asset Class**: `Crypto Altcoin`
**Timestamp**: `2026-10-29 21:43:08 IST` (`2026-10-29 16:13:08 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `1278.53` | **Live Ask Quote**: `1279.33` | **Mid Price**: `1278.93`
- **Spread Points**: `80.00` | **Spread BPS**: `6.26 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `1258.65` | VWAP Z-Score: `+0.85` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `9.81` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `58.56` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `1318.31` | Lower -3.00σ Band: `1198.98`
  * Upper +2.51σ Band: `1308.57` | Lower -2.51σ Band: `1208.72`
  * Upper +2.01σ Band: `1298.62` | Lower -2.01σ Band: `1218.67`
  * Upper +2.00σ Band: `1298.42` | Lower -2.00σ Band: `1218.87`
  * Upper +1.28σ Band: `1284.10` | Lower -1.28σ Band: `1233.19`
  * Upper +1.00σ Band: `1278.53` | Lower -1.00σ Band: `1238.76`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`1272.69` | EMA-20=`1266.08` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`1263.46` (Slope: `+0.0000`) | EMA-100=`1269.43`
  * Institutional Anchors: EMA-144=`1270.59` | EMA-200=`1267.40` (Slope: `+0.0350`) | EMA-233=`1266.56`
- **Range Boundaries**: 24H High=`1318.68` | 24H Low=`1230.00` | Weekly High=`1328.99` | Weekly Low=`1210.62`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `1278.18` (Distance: `+0.07%`)
  * Point of Control (POC) = `1245.67` (Distance: `+2.68%`)
  * Value Area Low (VAL) = `1230.30` (Distance: `+3.97%`)
  * Auction Positioning: `ABOVE_VALUE (Imbalance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `RANGE_EXPANSION`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`1320.44` | POC=`1312.10` | VAL=`1285.78`
  * Prior Day Extremes: PDH=`1328.99` | PDL=`1263.19` | PDC=`1296.46`
  * Monday Range Blueprint: High=`1267.53` | Mid=`1222.14` | Low=`1176.75`
  * Developing Weekly Value Area: Weekly VAH=`1289.92` | Weekly POC=`1238.15` | Weekly VAL=`1195.53`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`1318.68` | Low=`1230.00`
  * London Session (08:00-16:00 UTC): High=`1276.13` | Low=`1233.52`
  * New York Session (13:00-21:00 UTC): High=`1287.09` | Low=`1250.65`
  * Initial Balance (First Hour): IB High=`1255.79` | IB Low=`1245.43`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `1273.81` - `1284.05`
  * Optimal Trade Entry (OTE 0.705): `1281.49`
  * Structural Invalidation Anchor (0.786): `1289.16`

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
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-29 19:44:05 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `16` | `0xb83d...6e36` | `SHORT` | 67,331,916.86 USD | `52,582.52` | `1336.45` | `1277.70` | `3382.40` | 2,941,998.04 USD | `+4.37%` | `3X Cross` |
| `25` | `0x5b5d...c060` | `SHORT` | 52,151,704.60 USD | `40,727.61` | `1478.36` | `1277.70` | `4608.84` | 8,058,559.59 USD | `+15.45%` | `3X Cross` |
| `54` | `0x7fda...17d1` | `SHORT` | 25,619,680.58 USD | `20,007.56` | `1251.76` | `1277.70` | `2862.62` | -574,973.57 USD | `-2.24%` | `5X Cross` |
| `83` | `0x60b0...991e` | `LONG` | 21,447,863.67 USD | `16,779.74` | `1179.65` | `1277.70` | `888.72` | 1,653,616.65 USD | `+7.71%` | `10X Cross` |
| `90` | `0xbf73...5d58` | `LONG` | 20,443,200.00 USD | `16,000.00` | `1214.30` | `1277.70` | `704.22` | 1,014,367.75 USD | `+4.96%` | `10X Cross` |
| `133` | `0x469e...58a5` | `SHORT` | 15,787,753.80 USD | `12,358.32` | `1190.36` | `1277.70` | `1501.14` | -1,076,941.32 USD | `-6.82%` | `10X Cross` |
| `144` | `0xc36a...105b` | `LONG` | 14,726,943.11 USD | `11,510.82` | `1215.14` | `1277.70` | `934.70` | 739,662.08 USD | `+5.02%` | `10X Cross` |
| `171` | `0x8742...8427` | `LONG` | 12,789,000.00 USD | `10,000.00` | `1286.37` | `1277.70` | `807.69` | -74,710.31 USD | `-0.58%` | `10X Cross` |
| `205` | `0x58b2...11f3` | `LONG` | 10,863,000.00 USD | `8,500.00` | `1267.88` | `1277.70` | `442.30` | 85,995.60 USD | `+0.79%` | `10X Cross` |
| `208` | `0xad59...ba81` | `SHORT` | 10,777,260.00 USD | `8,425.00` | `330.91` | `1277.70` | `2143.80` | -7,989,302.23 USD | `-74.13%` | `10X Cross` |
| `209` | `0x9ffd...ce40` | `LONG` | 10,747,474.58 USD | `8,391.22` | `1240.16` | `1277.70` | `589.69` | 341,052.33 USD | `+3.17%` | `5X Cross` |
| `215` | `0xdd53...2b13` | `SHORT` | 10,560,260.04 USD | `8,245.05` | `739.37` | `1277.70` | `7893.46` | -4,464,093.89 USD | `-42.27%` | `3X Cross` |
| `241` | `0x880a...311c` | `SHORT` | 9,860,172.10 USD | `7,707.11` | `1367.50` | `1277.70` | `2309.95` | 679,312.10 USD | `+6.89%` | `10X Cross` |
| `287` | `0x2b61...2f6c` | `LONG` | 8,708,606.92 USD | `6,807.00` | `1453.56` | `1277.70` | `603.15` | -1,185,744.30 USD | `-13.62%` | `10X Cross` |
| `350` | `0x26b6...9a13` | `LONG` | 6,947,967.64 USD | `5,433.73` | `1282.23` | `1277.70` | `211.30` | -19,335.59 USD | `-0.28%` | `10X Cross` |
| `363` | `0x45d2...4029` | `SHORT` | 6,683,627.43 USD | `5,227.00` | `833.44` | `1277.70` | `7614.00` | -2,327,249.46 USD | `-34.82%` | `5X Cross` |
| `382` | `0xea00...a918` | `LONG` | 6,391,000.00 USD | `5,000.00` | `739.16` | `1277.70` | `0.000000` | 2,695,184.89 USD | `+42.17%` | `5X Cross` |
| `391` | `0xdd7a...8830` | `LONG` | 6,224,931.35 USD | `4,860.19` | `897.48` | `1277.70` | `814.08` | 1,863,027.68 USD | `+29.93%` | `10X Cross` |
| `399` | `0xf081...e39e` | `LONG` | 6,034,743.48 USD | `4,717.00` | `1195.70` | `1277.70` | `1200.00` | 394,619.43 USD | `+6.54%` | `10X Cross` |
| `439` | `0xfc66...ca06` | `SHORT` | 5,442,016.74 USD | `4,248.92` | `1276.99` | `1277.70` | `8062.86` | -16,179.12 USD | `-0.30%` | `10X Cross` |
| `471` | `0xa61c...66b9` | `LONG` | 4,978,584.00 USD | `3,888.00` | `1148.34` | `1277.70` | `0.000000` | 513,841.86 USD | `+10.32%` | `10X Cross` |
| `475` | `0x4cae...7c34` | `LONG` | 4,931,115.94 USD | `3,854.36` | `986.41` | `1277.70` | `759.46` | 1,129,128.58 USD | `+22.90%` | `10X Cross` |
| `479` | `0x382b...3e39` | `LONG` | 4,892,188.67 USD | `3,820.53` | `1154.54` | `1277.70` | `0.000000` | 481,216.59 USD | `+9.84%` | `10X Cross` |
| `491` | `0x9aa5...58af` | `SHORT` | 4,752,696.03 USD | `3,720.31` | `1205.51` | `1277.70` | `3332.44` | -267,809.23 USD | `-5.63%` | `10X Cross` |
| `554` | `0x456f...cdf1` | `LONG` | 4,164,750.64 USD | `3,256.51` | `1256.72` | `1277.70` | `527.79` | 72,220.64 USD | `+1.73%` | `10X Cross` |
| `555` | `0xd21d...90f1` | `LONG` | 4,157,400.00 USD | `3,250.00` | `1253.64` | `1277.70` | `875.79` | 83,058.27 USD | `+2.00%` | `4X Isolated` |
| `574` | `0x1338...c48e` | `LONG` | 4,023,711.77 USD | `3,149.43` | `1018.52` | `1277.70` | `820.09` | 815,966.23 USD | `+20.28%` | `4X Isolated` |
| `592` | `0xdbe0...d6d5` | `LONG` | 3,945,262.62 USD | `3,085.37` | `422.97` | `1277.70` | `338.40` | 2,640,258.13 USD | `+66.92%` | `3X Isolated` |
| `612` | `0x9c06...0560` | `SHORT` | 3,825,150.12 USD | `2,989.80` | `786.00` | `1277.70` | `2444.09` | -1,475,155.12 USD | `-38.56%` | `10X Cross` |
| `622` | `0x0153...8052` | `SHORT` | 3,785,182.17 USD | `2,960.18` | `1296.93` | `1277.70` | `2487.28` | 53,969.85 USD | `+1.43%` | `1X Isolated` |
| `677` | `0xecb6...2b00` | `SHORT` | 3,434,838.81 USD | `2,682.42` | `1266.51` | `1277.70` | `10593.90` | -37,520.14 USD | `-1.09%` | `5X Cross` |
| `678` | `0x27c9...d65d` | `SHORT` | 3,427,078.98 USD | `2,676.36` | `1238.78` | `1277.70` | `1704.93` | -111,669.23 USD | `-3.26%` | `10X Cross` |
| `711` | `0xa183...0482` | `LONG` | 3,240,732.60 USD | `2,534.00` | `530.25` | `1277.70` | `444.33` | 1,897,069.88 USD | `+58.54%` | `5X Isolated` |
| `731` | `0x0871...e927` | `LONG` | 3,191,489.75 USD | `2,500.00` | `1276.50` | `1277.70` | `0.000000` | 239.75 USD | `+0.01%` | `10X Cross` |
| `739` | `0x9b86...6e6e` | `LONG` | 3,156,170.16 USD | `2,467.30` | `637.58` | `1277.70` | `889.55` | 1,583,070.56 USD | `+50.16%` | `3X Cross` |
| `788` | `0xb2f7...af9f` | `SHORT` | 2,959,710.62 USD | `2,313.72` | `746.63` | `1277.70` | `4225.55` | -1,232,221.88 USD | `-41.63%` | `10X Cross` |
| `794` | `0x2e30...4cb5` | `SHORT` | 2,941,914.15 USD | `2,298.55` | `1283.11` | `1277.70` | `3301.60` | 7,368.98 USD | `+0.25%` | `2X Cross` |
| `826` | `0xf48f...10fe` | `LONG` | 2,840,776.44 USD | `2,218.49` | `1517.87` | `1277.70` | `881.17` | -526,610.38 USD | `-18.54%` | `3X Cross` |
| `854` | `0x5bc4...3b0c` | `SHORT` | 2,725,642.61 USD | `2,130.74` | `1089.65` | `1277.70` | `3555.36` | -403,885.03 USD | `-14.82%` | `5X Cross` |
| `895` | `0x325e...9564` | `LONG` | 2,563,445.75 USD | `2,001.91` | `1286.02` | `1277.70` | `0.000000` | -11,048.15 USD | `-0.43%` | `10X Cross` |
| `897` | `0x668c...ea2e` | `SHORT` | 2,555,000.00 USD | `2,000.00` | `1409.16` | `1277.70` | `2652.38` | 263,322.04 USD | `+10.31%` | `10X Cross` |
| `898` | `0x9a99...d21a` | `LONG` | 2,551,800.00 USD | `2,000.00` | `1293.51` | `1277.70` | `0.000000` | -35,227.91 USD | `-1.38%` | `10X Cross` |
| `920` | `0x77ee...2902` | `SHORT` | 2,489,673.91 USD | `1,946.03` | `759.84` | `1277.70` | `5293.56` | -1,010,996.41 USD | `-40.61%` | `10X Cross` |
| `927` | `0x3e2f...b269` | `SHORT` | 2,463,112.39 USD | `1,925.51` | `1134.87` | `1277.70` | `2931.66` | -277,913.54 USD | `-11.28%` | `10X Cross` |
| `932` | `0xe097...d0fe` | `LONG` | 2,446,869.17 USD | `1,913.56` | `1261.17` | `1277.70` | `0.000000` | 33,543.01 USD | `+1.37%` | `10X Cross` |
| `939` | `0x4f12...618b` | `SHORT` | 2,423,445.84 USD | `1,896.28` | `1608.30` | `1277.70` | `2116.62` | 626,338.55 USD | `+25.84%` | `3X Cross` |
| `998` | `0xac48...3201` | `LONG` | 2,303,559.26 USD | `1,802.19` | `1411.21` | `1277.70` | `15.05` | -239,701.11 USD | `-10.41%` | `10X Cross` |
| `999` | `0x866d...d6e1` | `LONG` | 2,302,118.88 USD | `1,802.05` | `674.73` | `1277.70` | `76.44` | 1,086,217.56 USD | `+47.18%` | `10X Cross` |
| `1021` | `0x2309...a2d9` | `LONG` | 2,236,097.67 USD | `1,750.37` | `1186.09` | `1277.70` | `803.90` | 160,003.57 USD | `+7.16%` | `8X Cross` |
| `1027` | `0x3e47...aaf6` | `LONG` | 2,221,049.38 USD | `1,736.28` | `1277.06` | `1277.70` | `1067.21` | 3,715.24 USD | `+0.17%` | `10X Cross` |
| `1031` | `0x4fe2...ac59` | `SHORT` | 2,211,182.82 USD | `1,730.19` | `1496.85` | `1277.70` | `1960.87` | 378,659.65 USD | `+17.12%` | `10X Cross` |
| `1048` | `0x362a...1d9f` | `LONG` | 2,160,911.77 USD | `1,693.77` | `1280.14` | `1277.70` | `971.18` | -7,352.32 USD | `-0.34%` | `7X Cross` |
| `1074` | `0x265e...7f70` | `LONG` | 2,110,923.72 USD | `1,651.74` | `1388.09` | `1277.70` | `0.000000` | -181,845.97 USD | `-8.61%` | `3X Cross` |
| `1093` | `0xa271...a3f7` | `LONG` | 2,084,967.54 USD | `1,631.43` | `1190.60` | `1277.70` | `910.18` | 142,585.74 USD | `+6.84%` | `4X Cross` |
| `1103` | `0xd4c1...3d1d` | `SHORT` | 2,054,723.40 USD | `1,604.25` | `1243.57` | `1277.70` | `3365.53` | -59,719.21 USD | `-2.91%` | `10X Cross` |
| `1109` | `0x6646...6de5` | `SHORT` | 2,045,920.00 USD | `1,600.00` | `660.64` | `1277.70` | `4805.46` | -988,895.03 USD | `-48.33%` | `10X Cross` |
| `1124` | `0xdf57...93f5` | `LONG` | 2,020,828.99 USD | `1,579.76` | `1218.38` | `1277.70` | `780.03` | 96,073.01 USD | `+4.75%` | `3X Isolated` |
| `1136` | `0x7f75...9edf` | `LONG` | 2,008,659.39 USD | `1,572.09` | `1197.43` | `1277.70` | `965.67` | 126,196.64 USD | `+6.28%` | `10X Cross` |
| `1139` | `0xab59...59b5` | `LONG` | 2,002,357.34 USD | `1,565.32` | `1342.15` | `1277.70` | `806.72` | -98,537.87 USD | `-4.92%` | `10X Cross` |
| `1148` | `0xdf83...3cff` | `SHORT` | 1,992,522.02 USD | `1,556.05` | `1233.77` | `1277.70` | `1782.11` | -72,716.28 USD | `-3.65%` | `10X Cross` |
| `1160` | `0x634f...6951` | `LONG` | 1,986,908.20 USD | `1,553.00` | `1263.46` | `1277.70` | `1184.22` | 24,758.62 USD | `+1.25%` | `10X Cross` |
| `1173` | `0xfe7c...b7ae` | `SHORT` | 1,967,280.34 USD | `1,538.38` | `1350.17` | `1277.70` | `5445.22` | 109,791.58 USD | `+5.58%` | `10X Cross` |
| `1201` | `0xcf67...eb24` | `LONG` | 1,918,950.00 USD | `1,500.00` | `887.05` | `1277.70` | `537.87` | 588,378.63 USD | `+30.66%` | `10X Cross` |
| `1202` | `0x413c...886c` | `LONG` | 1,918,800.00 USD | `1,500.00` | `1265.89` | `1277.70` | `0.000000` | 19,958.91 USD | `+1.04%` | `10X Cross` |
| `1223` | `0x2edd...8179` | `SHORT` | 1,888,391.76 USD | `1,474.73` | `1241.44` | `1277.70` | `2760.49` | -57,605.58 USD | `-3.05%` | `10X Cross` |
| `1224` | `0x039c...0ebd` | `SHORT` | 1,884,678.31 USD | `1,471.83` | `1238.35` | `1277.70` | `2696.34` | -62,044.17 USD | `-3.29%` | `10X Cross` |
| `1289` | `0x2ab7...c2f8` | `LONG` | 1,790,795.30 USD | `1,400.51` | `813.26` | `1277.70` | `809.59` | 651,813.62 USD | `+36.40%` | `3X Cross` |
| `1305` | `0x11be...8b1d` | `LONG` | 1,759,548.99 USD | `1,375.83` | `1206.55` | `1277.70` | `1134.31` | 99,541.03 USD | `+5.66%` | `10X Isolated` |
| `1406` | `0xe065...0f85` | `SHORT` | 1,613,615.58 USD | `1,262.61` | `1087.02` | `1277.70` | `1634.93` | -241,139.45 USD | `-14.94%` | `10X Cross` |
| `1483` | `0x5975...9abd` | `LONG` | 1,534,680.00 USD | `1,200.00` | `1179.54` | `1277.70` | `413.61` | 119,237.21 USD | `+7.77%` | `5X Cross` |
| `1506` | `0x3fc5...c0c1` | `SHORT` | 1,503,359.74 USD | `1,175.51` | `1264.34` | `1277.70` | `2834.61` | -17,120.39 USD | `-1.14%` | `10X Cross` |
| `1514` | `0x023a...2355` | `SHORT` | 1,493,502.46 USD | `1,166.07` | `1282.96` | `1277.70` | `7790.81` | 2,518.30 USD | `+0.17%` | `10X Cross` |
| `1523` | `0x69cc...14fd` | `SHORT` | 1,485,655.73 USD | `1,161.36` | `675.33` | `1277.70` | `8119.44` | -701,350.20 USD | `-47.21%` | `10X Cross` |
| `1568` | `0xef96...9383` | `SHORT` | 1,428,777.97 USD | `1,116.32` | `1240.25` | `1277.70` | `4717.98` | -44,256.59 USD | `-3.10%` | `10X Cross` |
| `1570` | `0x5f94...4b96` | `LONG` | 1,426,653.38 USD | `1,115.27` | `538.00` | `1277.70` | `0.000000` | 826,635.75 USD | `+57.94%` | `10X Cross` |
| `1588` | `0x71df...a23d` | `SHORT` | 1,405,096.05 USD | `1,098.28` | `513.50` | `1277.70` | `2546.20` | -841,125.86 USD | `-59.86%` | `2X Cross` |
| `1617` | `0xbfc7...80b4` | `SHORT` | 1,375,355.00 USD | `1,075.00` | `558.03` | `1277.70` | `5395.00` | -775,476.27 USD | `-56.38%` | `10X Cross` |
| `1702` | `0xe282...df29` | `LONG` | 1,280,800.00 USD | `1,000.00` | `420.99` | `1277.70` | `119.50` | 859,813.14 USD | `+67.13%` | `10X Cross` |
| `1705` | `0x0748...d4b2` | `LONG` | 1,278,900.00 USD | `1,000.00` | `1334.09` | `1277.70` | `0.000000` | -55,188.30 USD | `-4.32%` | `7X Cross` |
| `1706` | `0x266b...efcb` | `LONG` | 1,278,700.00 USD | `1,000.00` | `826.11` | `1277.70` | `13.86` | 452,587.07 USD | `+35.39%` | `10X Cross` |
| `1707` | `0xb5ff...d912` | `LONG` | 1,278,673.70 USD | `1,000.00` | `1141.93` | `1277.70` | `400.35` | 136,743.40 USD | `+10.69%` | `2X Cross` |
| `1728` | `0x123d...3bff` | `SHORT` | 1,261,608.96 USD | `987.02` | `470.28` | `1277.70` | `4320.92` | -797,435.24 USD | `-63.21%` | `10X Cross` |
| `1730` | `0x17f0...094f` | `LONG` | 1,257,443.25 USD | `984.30` | `1287.23` | `1277.70` | `536.66` | -9,576.91 USD | `-0.76%` | `5X Cross` |
| `1809` | `0x757d...94ba` | `LONG` | 1,183,260.00 USD | `925.00` | `1558.31` | `1277.70` | `0.000000` | -258,180.58 USD | `-21.82%` | `10X Cross` |
| `1817` | `0xfc27...9d9d` | `SHORT` | 1,175,190.64 USD | `919.07` | `1297.54` | `1277.70` | `17087.26` | 17,338.00 USD | `+1.48%` | `10X Cross` |
| `1855` | `0x51f6...2b39` | `SHORT` | 1,137,952.43 USD | `889.79` | `1300.08` | `1277.70` | `3217.77` | 18,841.63 USD | `+1.66%` | `10X Cross` |
| `1873` | `0x5323...b23c` | `LONG` | 1,125,559.50 USD | `879.00` | `1256.06` | `1277.70` | `0.000000` | 21,482.78 USD | `+1.91%` | `5X Cross` |
| `1886` | `0xcf0a...856f` | `LONG` | 1,112,981.24 USD | `871.15` | `1292.19` | `1277.70` | `938.37` | -12,713.61 USD | `-1.14%` | `4X Cross` |
| `1931` | `0xe35c...a1d3` | `LONG` | 1,081,471.89 USD | `844.57` | `1306.64` | `1277.70` | `688.34` | -22,076.88 USD | `-2.04%` | `2X Isolated` |
| `1947` | `0xdf95...7d72` | `SHORT` | 1,067,521.18 USD | `833.48` | `1055.92` | `1277.70` | `42626.63` | -187,436.67 USD | `-17.56%` | `10X Cross` |
| `1962` | `0x2847...d47b` | `LONG` | 1,054,200.86 USD | `823.08` | `1230.74` | `1277.70` | `0.000000` | 41,202.04 USD | `+3.91%` | `5X Cross` |
| `1969` | `0x601c...4f54` | `SHORT` | 1,049,460.32 USD | `822.59` | `613.56` | `1277.70` | `2984.44` | -544,753.47 USD | `-51.91%` | `5X Cross` |
| `1973` | `0xae55...2236` | `LONG` | 1,045,277.39 USD | `817.47` | `1467.80` | `1277.70` | `0.000000` | -154,603.83 USD | `-14.79%` | `10X Cross` |
| `1979` | `0x71b1...79c8` | `LONG` | 1,040,431.86 USD | `812.52` | `1231.55` | `1277.70` | `770.79` | 39,776.41 USD | `+3.82%` | `10X Cross` |
| `2003` | `0x7a76...b16d` | `LONG` | 1,024,400.00 USD | `800.00` | `1289.46` | `1277.70` | `1129.10` | -7,165.10 USD | `-0.70%` | `10X Cross` |
| `2004` | `0x0f02...5384` | `LONG` | 1,024,388.13 USD | `800.78` | `1290.36` | `1277.70` | `309.86` | -8,905.94 USD | `-0.87%` | `3X Cross` |
| `2008` | `0x9b0f...db40` | `LONG` | 1,022,960.00 USD | `800.00` | `1268.86` | `1277.70` | `777.34` | 7,870.24 USD | `+0.77%` | `10X Cross` |
| `2019` | `0xabdb...84ac` | `LONG` | 1,015,446.99 USD | `793.69` | `711.79` | `1277.70` | `664.23` | 450,506.62 USD | `+44.37%` | `3X Cross` |
| `2031` | `0xfdf8...e381` | `LONG` | 1,010,343.79 USD | `790.01` | `1337.72` | `1277.70` | `263.14` | -46,465.90 USD | `-4.60%` | `10X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `1458.30` | 1,939.54 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 1.94K USD at 1458.3000 USD [API] | `2026-09-24 09:32:27` |
| `ANNOUNCEMENT` | `INFO` | `1076.30` | 1,657.50 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Long: 1.66K USD at 1076.3000 USD [API] | `2026-10-18 15:41:57` |
| `ANNOUNCEMENT` | `INFO` | `1076.30` | 990.20 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Long: 0.99K USD at 1076.3000 USD [API] | `2026-10-18 15:41:57` |
| `ANNOUNCEMENT` | `INFO` | `1076.30` | 5,499.89 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Long: 5.50K USD at 1076.3000 USD [API] | `2026-10-18 15:41:57` |
| `ANNOUNCEMENT` | `INFO` | `1076.30` | 32.29 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Long: 0.03K USD at 1076.3000 USD [API] | `2026-10-18 15:41:57` |
| `ANNOUNCEMENT` | `INFO` | `1076.40` | 990.29 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Long: 0.99K USD at 1076.4000 USD [API] | `2026-10-18 15:41:57` |
| `ANNOUNCEMENT` | `INFO` | `1076.40` | 21.53 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Long: 0.02K USD at 1076.4000 USD [API] | `2026-10-18 15:41:57` |
| `ANNOUNCEMENT` | `INFO` | `1076.40` | 2,594.12 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Long: 2.59K USD at 1076.4000 USD [API] | `2026-10-18 15:41:57` |
| `ANNOUNCEMENT` | `INFO` | `1139.90` | 1,766.85 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Long: 1.77K USD at 1139.9000 USD [API] | `2026-10-08 15:23:23` |
| `ANNOUNCEMENT` | `INFO` | `1139.90` | 10,749.26 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Long: 10.75K USD at 1139.9000 USD [API] | `2026-10-08 15:23:23` |
| `ANNOUNCEMENT` | `INFO` | `1304.60` | 10,019.33 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Long: 10.02K USD at 1304.6000 USD [API] | `2026-10-27 16:27:21` |
| `ANNOUNCEMENT` | `INFO` | `1289.60` | 10,407.07 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Long: 10.41K USD at 1289.6000 USD [API] | `2026-10-27 15:20:59` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`1288.96` (Vol: 1,400,000.00 USD, Dist: `+0.78%`) | Long MP=`1243.06` (Vol: 1,400,000.00 USD, Dist: `--2.81%`)
  * 48H Horizon: Short MP=`1332.96` (Vol: 2,800,000.00 USD, Dist: `+4.22%`) | Long MP=`1243.86` (Vol: 1,400,000.00 USD, Dist: `--2.74%`)
  * 3D Horizon: Short MP=`1332.46` (Vol: 2,200,000.00 USD, Dist: `+4.18%`) | Long MP=`1199.86` (Vol: 1,800,000.00 USD, Dist: `--6.18%`)
  * 7D Horizon: Short MP=`1333.81` (Vol: 3,100,000.00 USD, Dist: `+4.29%`) | Long MP=`1228.42` (Vol: 2,600,000.00 USD, Dist: `--3.95%`)
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
  * Current Rate: `31.81K` | Last 24h: `55.65K` | Last 3d: `287.36K` | Last 7d: `770.46K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0034%` | **USDT OKX** | `-0.0029%` |
| **USDT Bybit** | `0.0093%` | **USDT KuCoin** | `0.0007%` |
| **USDT MEXC** | `0.0034%` | **USDT BingX** | `0.0091%` |
| **USDT Gate** | `-0.0038%` | **USDT Bitget** | `-0.0027%` |
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
| `5:00 UTC` | `1273.05` | `1271.71` | `1273.05` | `1275.75` | `1266.75` | 14,607,808.21 USD | 8,236,157.48 USD | 6,371,650.73 USD | 1,864,506.74 USD | `+12.76%` | `3B / 2S` |
| `0:00 UTC` | `1267.65` | `1268.93` | `1267.65` | `1275.15` | `1264.95` | 13,160,284.62 USD | 6,005,318.77 USD | 7,154,965.86 USD | -1,149,647.09 USD | `-8.74%` | `2B / 7S` |
| `5:00 UTC` | `1270.05` | `1266.18` | `1270.05` | `1272.45` | `1261.65` | 14,821,973.17 USD | 7,844,579.16 USD | 6,977,394.01 USD | 867,185.15 USD | `+5.85%` | `5B / 4S` |
| `0:00 UTC` | `1267.05` | `1266.32` | `1267.05` | `1272.15` | `1261.05` | 20,347,628.60 USD | 8,993,467.95 USD | 11,354,160.65 USD | -2,360,692.70 USD | `-11.60%` | `2B / 1S` |
| `5:00 UTC` | `1275.15` | `1272.99` | `1275.15` | `1276.95` | `1268.85` | 14,236,279.84 USD | 7,044,569.63 USD | 7,191,710.21 USD | -147,140.58 USD | `-1.03%` | `2B / 1S` |
| `0:00 UTC` | `1283.25` | `1280.79` | `1283.25` | `1285.35` | `1272.15` | 30,590,976.02 USD | 15,924,236.95 USD | 14,666,739.07 USD | 1,257,497.88 USD | `+4.11%` | `6B / 6S` |
| `5:00 UTC` | `1282.65` | `1283.77` | `1282.65` | `1287.45` | `1279.95` | 18,382,768.24 USD | 9,473,428.52 USD | 8,909,339.72 USD | 564,088.80 USD | `+3.07%` | `2B / 0S` |
| `0:00 UTC` | `1272.15` | `1274.65` | `1272.15` | `1287.15` | `1267.35` | 29,597,275.23 USD | 13,089,023.10 USD | 16,508,252.13 USD | -3,419,229.03 USD | `-11.55%` | `0B / 17S` |
| `5:00 UTC` | `1271.55` | `1274.24` | `1271.55` | `1282.05` | `1269.75` | 23,016,974.01 USD | 12,504,704.65 USD | 10,512,269.35 USD | 1,992,435.30 USD | `+8.66%` | `4B / 3S` |
| `0:00 UTC` | `1276.95` | `1276.39` | `1276.95` | `1278.75` | `1272.15` | 9,550,391.77 USD | 4,466,289.90 USD | 5,084,101.87 USD | -617,811.98 USD | `-6.47%` | `1B / 2S` |

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
| `5m` | 1,380,000.00 USD | -1,290,000.00 USD | **`ACCUMULATION`** |
| `15m` | 2,390,000.00 USD | 797,290.00 USD | **`ACCUMULATION`** |
| `30m` | 2,990,000.00 USD | 9,360,000.00 USD | **`ACCUMULATION`** |
| `1h` | 2,330,000.00 USD | -1,200,000.00 USD | **`ACCUMULATION`** |
| `2h` | 3,260,000.00 USD | 5,600,000.00 USD | **`ACCUMULATION`** |
| `4h` | 7,370,000.00 USD | 18,070,000.00 USD | **`ACCUMULATION`** |
| `6h` | 1,160,000.00 USD | 20,800,000.00 USD | **`ACCUMULATION`** |
| `8h` | 1,480,000.00 USD | 18,190,000.00 USD | **`ACCUMULATION`** |
| `12h` | -4,440,000.00 USD | 28,880,000.00 USD | **`ACCUMULATION`** |
| `24h` | -13,630,000.00 USD | 780,140.00 USD | **`DISTRIBUTION`** |
| `1w` | 28,130,000.00 USD | 156,180,000.00 USD | **`ACCUMULATION`** |
| `30d` | 21,310,000.00 USD | -663,730,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+1.38M` | 15m=`+2.39M` | 1h=`+2.33M` | 24h=`-13.63M`
* Futures Capital Netflows: 5m=`-1.29M` | 15m=`+797.29K` | 1h=`-1.20M` | 24h=`+780.14K`
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
  * `2026-10-29 19:41:49 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-29 19:40:49 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-29 19:20:49 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-29 19:09:49 IST`: [youtube.com/ecbeuro] - (Sentiment: `Neutral`)
  * `2026-10-29 19:49:49 IST`: [ecb.europa.eu] - (Sentiment: `Neutral`)
  * `2026-10-29 19:49:49 IST`: [zerohedge.com] - (Sentiment: `Neutral`)
  * `2026-10-29 19:49:49 IST`: [dol.gov] - (Sentiment: `Neutral`)
  * `2026-10-29 19:49:49 IST`: [bea.gov] - (Sentiment: `Neutral`)
  * `2026-10-29 19:49:49 IST`: [bea.gov] - (Sentiment: `Neutral`)
  * `2026-10-29 19:48:49 IST`: [financemagnates.com] - (Sentiment: `Neutral`)
  * `2026-10-29 19:48:49 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-29 16:50:49 IST`: [marctomarket.com] - (Sentiment: `Neutral`)
  * `2026-10-29 15:50:49 IST`: [ecb.europa.eu] - (Sentiment: `Neutral`)
  * `2026-10-29 15:50:49 IST`: [dailyforex.com] - (Sentiment: `Neutral`)
  * `2026-10-29 15:50:49 IST`: [bankofengland.co.uk] - (Sentiment: `Neutral`)


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
  * Execution Entry: `1230.30` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `1217.33` (Risk Distance: `12.97` pts)
  * +2.5R Take Profit: `1262.72`
  * Mathematical Lot Sizing: **`0.77 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `1278.18` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `1291.15` (Risk Distance: `12.97` pts)
  * +2.5R Take Profit: `1245.76`
  * Mathematical Lot Sizing: **`0.77 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`1289.16`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
