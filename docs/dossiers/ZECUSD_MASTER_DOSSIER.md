# 🏛️ SOVEREIGN CANDIDATE DOSSIER: ZECUSD
**Canonical Key**: `ZECUSD` | **Broker Instrument**: `ZECUSD.p` | **Asset Class**: `Crypto Altcoin`
**Timestamp**: `2026-10-30 04:38:03 IST` (`2026-10-29 23:08:03 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `1222.01` | **Live Ask Quote**: `1223.81` | **Mid Price**: `1222.91`
- **Spread Points**: `180.00` | **Spread BPS**: `14.72 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `1279.50` | VWAP Z-Score: `-1.00` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `21.77` (Volatility Regime: `HIGH_EXPANSION`)
  * 14-Period RSI: `33.37` (State: `OVERSOLD`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `1391.54` | Lower -3.00σ Band: `1167.46`
  * Upper +2.51σ Band: `1373.24` | Lower -2.51σ Band: `1185.76`
  * Upper +2.01σ Band: `1354.57` | Lower -2.01σ Band: `1204.44`
  * Upper +2.00σ Band: `1354.20` | Lower -2.00σ Band: `1204.81`
  * Upper +1.28σ Band: `1327.31` | Lower -1.28σ Band: `1231.70`
  * Upper +1.00σ Band: `1316.85` | Lower -1.00σ Band: `1242.16`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`1259.92` | EMA-20=`1278.05` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`1287.46` (Slope: `+0.0000`) | EMA-100=`1285.29`
  * Institutional Anchors: EMA-144=`1282.53` | EMA-200=`1279.53` (Slope: `-0.1717`) | EMA-233=`1279.42`
- **Range Boundaries**: 24H High=`1396.49` | 24H Low=`1206.89` | Weekly High=`1396.49` | Weekly Low=`1206.89`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `1269.57` (Distance: `-3.50%`)
  * Point of Control (POC) = `1252.78` (Distance: `-2.21%`)
  * Value Area Low (VAL) = `1241.41` (Distance: `-1.31%`)
  * Auction Positioning: `BELOW_VALUE (Imbalance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `RANGE_EXPANSION`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`1309.91` | POC=`1246.71` | VAL=`1230.27`
  * Prior Day Extremes: PDH=`1396.49` | PDL=`1206.89` | PDC=`1244.38`
  * Monday Range Blueprint: High=`1267.53` | Mid=`1222.14` | Low=`1176.75`
  * Developing Weekly Value Area: Weekly VAH=`1297.61` | Weekly POC=`1239.01` | Weekly VAL=`1199.46`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`1296.00` | Low=`1221.90`
  * London Session (08:00-16:00 UTC): High=`1227.80` | Low=`1218.02`
  * New York Session (13:00-21:00 UTC): High=`1230.25` | Low=`1215.57`
  * Initial Balance (First Hour): IB High=`1226.58` | IB Low=`1219.24`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `1218.02` - `1227.80`
  * Optimal Trade Entry (OTE 0.705): `1225.36`
  * Structural Invalidation Anchor (0.786): `1232.69`

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
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 04:36:18 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `16` | `0xb83d...6e36` | `SHORT` | 65,073,230.83 USD | `52,385.47` | `1336.45` | `1242.05` | `4009.72` | 4,937,336.57 USD | `+7.59%` | `3X Cross` |
| `23` | `0x5b5d...c060` | `SHORT` | 49,806,444.42 USD | `40,121.38` | `1478.36` | `1242.05` | `5492.01` | 9,507,590.70 USD | `+19.09%` | `3X Cross` |
| `43` | `0x7fda...17d1` | `SHORT` | 28,919,521.02 USD | `23,292.14` | `1262.37` | `1242.05` | `2771.40` | 483,781.07 USD | `+1.67%` | `5X Cross` |
| `84` | `0x60b0...991e` | `LONG` | 20,837,081.13 USD | `16,779.74` | `1179.65` | `1242.05` | `930.71` | 1,042,834.12 USD | `+5.00%` | `10X Cross` |
| `143` | `0xc36a...105b` | `LONG` | 14,291,834.11 USD | `11,510.82` | `1215.14` | `1242.05` | `960.50` | 304,553.08 USD | `+2.13%` | `10X Cross` |
| `159` | `0x9071...5c0b` | `LONG` | 13,086,663.95 USD | `10,517.29` | `1353.83` | `1242.05` | `0.0163` | -1,151,954.93 USD | `-8.80%` | `1X Cross` |
| `180` | `0x8742...8427` | `LONG` | 11,448,145.48 USD | `9,201.21` | `1286.37` | `1242.05` | `707.99` | -388,024.51 USD | `-3.39%` | `10X Cross` |
| `201` | `0x9ffd...ce40` | `LONG` | 10,584,647.48 USD | `8,526.42` | `1256.26` | `1242.05` | `615.75` | -126,730.36 USD | `-1.20%` | `5X Cross` |
| `204` | `0xad59...ba81` | `SHORT` | 10,463,850.00 USD | `8,425.00` | `330.91` | `1242.05` | `2145.66` | -7,675,892.23 USD | `-73.36%` | `10X Cross` |
| `211` | `0xdd53...2b13` | `SHORT` | 10,157,973.52 USD | `8,168.20` | `739.52` | `1242.05` | `8685.83` | -4,117,463.33 USD | `-40.53%` | `3X Cross` |
| `233` | `0x880a...311c` | `SHORT` | 9,569,147.78 USD | `7,707.11` | `1367.50` | `1242.05` | `2269.83` | 970,336.43 USD | `+10.14%` | `10X Cross` |
| `275` | `0x2b61...2f6c` | `LONG` | 8,451,571.20 USD | `6,807.00` | `1453.56` | `1242.05` | `533.97` | -1,442,780.02 USD | `-17.07%` | `10X Cross` |
| `290` | `0x2ae5...83e7` | `LONG` | 8,044,712.64 USD | `6,436.80` | `1391.82` | `1242.05` | `0.000000` | -914,179.35 USD | `-11.36%` | `1X Cross` |
| `337` | `0x26b6...9a13` | `LONG` | 6,780,208.29 USD | `5,433.73` | `1282.23` | `1242.05` | `221.79` | -187,094.94 USD | `-2.76%` | `10X Cross` |
| `354` | `0x45d2...4029` | `SHORT` | 6,522,250.60 USD | `5,227.00` | `833.44` | `1242.05` | `9008.65` | -2,165,872.63 USD | `-33.21%` | `5X Cross` |
| `376` | `0xea00...a918` | `LONG` | 6,209,000.00 USD | `5,000.00` | `739.16` | `1242.05` | `0.000000` | 2,513,184.89 USD | `+40.48%` | `5X Cross` |
| `377` | `0x58b2...11f3` | `LONG` | 6,162,656.44 USD | `4,963.08` | `1257.17` | `1242.05` | `0.000000` | -76,754.75 USD | `-1.25%` | `10X Cross` |
| `383` | `0xdd7a...8830` | `LONG` | 6,037,328.02 USD | `4,860.19` | `897.48` | `1242.05` | `786.31` | 1,675,424.34 USD | `+27.75%` | `10X Cross` |
| `421` | `0xecb6...2b00` | `SHORT` | 5,194,838.21 USD | `4,183.65` | `1304.24` | `1242.05` | `7908.40` | 261,660.01 USD | `+5.04%` | `5X Cross` |
| `434` | `0x4cae...7c34` | `LONG` | 4,973,014.68 USD | `4,004.36` | `999.34` | `1242.05` | `987.52` | 971,286.53 USD | `+19.53%` | `10X Cross` |
| `447` | `0xa61c...66b9` | `LONG` | 4,830,840.00 USD | `3,888.00` | `1148.34` | `1242.05` | `0.000000` | 366,097.86 USD | `+7.58%` | `10X Cross` |
| `466` | `0x9aa5...58af` | `SHORT` | 4,618,936.37 USD | `3,720.31` | `1205.51` | `1242.05` | `3673.83` | -134,049.57 USD | `-2.90%` | `10X Cross` |
| `471` | `0x0153...8052` | `SHORT` | 4,600,166.10 USD | `3,698.18` | `1307.82` | `1242.05` | `2504.73` | 236,404.65 USD | `+5.14%` | `1X Isolated` |
| `543` | `0xd21d...90f1` | `LONG` | 4,036,500.00 USD | `3,250.00` | `1253.64` | `1242.05` | `875.93` | -37,841.73 USD | `-0.94%` | `4X Isolated` |
| `569` | `0x1338...c48e` | `LONG` | 3,912,851.83 USD | `3,149.43` | `1018.52` | `1242.05` | `820.23` | 705,106.29 USD | `+18.02%` | `4X Isolated` |
| `573` | `0xd4c1...3d1d` | `SHORT` | 3,899,009.34 USD | `3,135.26` | `1299.23` | `1242.05` | `2836.81` | 174,410.35 USD | `+4.47%` | `10X Cross` |
| `574` | `0x456f...cdf1` | `LONG` | 3,892,564.62 USD | `3,134.11` | `1268.47` | `1242.05` | `493.77` | -82,944.85 USD | `-2.13%` | `10X Cross` |
| `580` | `0x382b...3e39` | `LONG` | 3,864,679.50 USD | `3,112.41` | `1211.32` | `1242.05` | `0.000000` | 94,545.87 USD | `+2.45%` | `10X Cross` |
| `584` | `0xdbe0...d6d5` | `LONG` | 3,837,891.74 USD | `3,085.37` | `422.97` | `1242.05` | `338.54` | 2,532,887.25 USD | `+66.00%` | `3X Isolated` |
| `589` | `0x27c9...d65d` | `SHORT` | 3,778,114.41 USD | `3,042.45` | `1254.41` | `1242.05` | `1775.56` | 38,368.70 USD | `+1.02%` | `10X Cross` |
| `597` | `0x325e...9564` | `LONG` | 3,729,873.17 USD | `3,001.91` | `1301.41` | `1242.05` | `170.80` | -176,836.03 USD | `-4.74%` | `10X Cross` |
| `603` | `0x9c06...0560` | `SHORT` | 3,711,520.08 USD | `2,989.80` | `786.00` | `1242.05` | `2549.44` | -1,361,525.08 USD | `-36.68%` | `10X Cross` |
| `611` | `0x2e30...4cb5` | `SHORT` | 3,686,114.32 USD | `2,962.40` | `1297.53` | `1242.05` | `2873.86` | 157,679.41 USD | `+4.28%` | `2X Cross` |
| `702` | `0xac48...3201` | `LONG` | 3,192,233.17 USD | `2,570.65` | `1378.58` | `1242.05` | `554.74` | -351,610.47 USD | `-11.01%` | `10X Cross` |
| `713` | `0xa183...0482` | `LONG` | 3,152,549.40 USD | `2,534.00` | `530.25` | `1242.05` | `444.47` | 1,808,886.68 USD | `+57.38%` | `5X Isolated` |
| `728` | `0x0871...e927` | `LONG` | 3,104,000.00 USD | `2,500.00` | `1276.50` | `1242.05` | `0.000000` | -87,250.00 USD | `-2.81%` | `10X Cross` |
| `740` | `0x9b86...6e6e` | `LONG` | 3,059,418.60 USD | `2,463.30` | `637.58` | `1242.05` | `882.40` | 1,488,869.32 USD | `+48.67%` | `3X Cross` |
| `788` | `0xb2f7...af9f` | `SHORT` | 2,874,102.98 USD | `2,313.72` | `746.63` | `1242.05` | `4380.68` | -1,146,614.24 USD | `-39.89%` | `10X Cross` |
| `816` | `0xf48f...10fe` | `LONG` | 2,755,808.28 USD | `2,218.49` | `1517.87` | `1242.05` | `983.75` | -611,578.55 USD | `-22.19%` | `3X Cross` |
| `846` | `0x5bc4...3b0c` | `SHORT` | 2,650,853.63 USD | `2,130.74` | `1089.65` | `1242.05` | `3681.99` | -329,096.06 USD | `-12.41%` | `5X Cross` |
| `863` | `0x8de4...b9aa` | `SHORT` | 2,596,754.79 USD | `2,091.29` | `1331.35` | `1242.05` | `1689.86` | 187,484.91 USD | `+7.22%` | `3X Cross` |
| `870` | `0x4fe2...ac59` | `SHORT` | 2,572,268.47 USD | `2,071.57` | `1478.56` | `1242.05` | `1850.50` | 490,677.75 USD | `+19.08%` | `10X Cross` |
| `900` | `0x9321...d75a` | `SHORT` | 2,487,800.00 USD | `2,000.00` | `1252.00` | `1242.05` | `3741.62` | 16,195.67 USD | `+0.65%` | `10X Cross` |
| `904` | `0x9a99...d21a` | `LONG` | 2,483,400.00 USD | `2,000.00` | `1278.44` | `1242.05` | `0.000000` | -73,473.67 USD | `-2.96%` | `10X Cross` |
| `930` | `0x77ee...2902` | `SHORT` | 2,416,190.85 USD | `1,946.03` | `759.84` | `1242.05` | `5269.09` | -937,513.34 USD | `-38.80%` | `10X Cross` |
| `937` | `0x3e2f...b269` | `SHORT` | 2,394,564.24 USD | `1,925.51` | `1134.87` | `1242.05` | `2931.78` | -209,365.38 USD | `-8.74%` | `10X Cross` |
| `941` | `0xe097...d0fe` | `LONG` | 2,377,789.66 USD | `1,913.56` | `1261.17` | `1242.05` | `0.000000` | -35,536.51 USD | `-1.49%` | `10X Cross` |
| `956` | `0x4f12...618b` | `SHORT` | 2,354,610.88 USD | `1,896.28` | `1608.30` | `1242.05` | `2116.75` | 695,173.51 USD | `+29.52%` | `3X Cross` |
| `994` | `0x866d...d6e1` | `LONG` | 2,237,965.90 USD | `1,802.05` | `674.73` | `1242.05` | `236.68` | 1,022,064.58 USD | `+45.67%` | `10X Cross` |
| `1017` | `0x2309...a2d9` | `LONG` | 2,173,165.05 USD | `1,750.37` | `1186.09` | `1242.05` | `816.28` | 97,070.94 USD | `+4.47%` | `8X Cross` |
| `1037` | `0x2edd...8179` | `SHORT` | 2,114,548.62 USD | `1,701.85` | `1261.58` | `1242.05` | `3118.52` | 32,470.23 USD | `+1.54%` | `10X Cross` |
| `1041` | `0x023a...2355` | `SHORT` | 2,107,752.15 USD | `1,696.38` | `1313.00` | `1242.05` | `5256.61` | 119,595.15 USD | `+5.67%` | `10X Cross` |
| `1074` | `0xfe7c...b7ae` | `SHORT` | 2,037,781.38 USD | `1,640.99` | `1347.05` | `1242.05` | `6994.49` | 172,707.80 USD | `+8.48%` | `10X Cross` |
| `1076` | `0x3e47...aaf6` | `LONG` | 2,032,259.76 USD | `1,636.28` | `1278.38` | `1242.05` | `1050.96` | -59,532.03 USD | `-2.93%` | `10X Cross` |
| `1078` | `0xa271...a3f7` | `LONG` | 2,025,746.63 USD | `1,631.43` | `1190.60` | `1242.05` | `910.32` | 83,364.83 USD | `+4.12%` | `4X Cross` |
| `1103` | `0x6646...6de5` | `SHORT` | 1,997,760.00 USD | `1,600.00` | `660.64` | `1242.05` | `4471.89` | -940,735.03 USD | `-47.09%` | `10X Cross` |
| `1109` | `0x7f75...9edf` | `LONG` | 1,993,405.82 USD | `1,605.78` | `1199.97` | `1242.05` | `978.27` | 66,513.93 USD | `+3.34%` | `10X Cross` |
| `1112` | `0x265e...7f70` | `LONG` | 1,988,880.56 USD | `1,601.74` | `1388.09` | `1242.05` | `0.000000` | -234,484.45 USD | `-11.79%` | `3X Cross` |
| `1132` | `0xdf57...93f5` | `LONG` | 1,964,589.54 USD | `1,579.76` | `1218.38` | `1242.05` | `780.17` | 39,833.56 USD | `+2.03%` | `3X Isolated` |
| `1146` | `0xab59...59b5` | `LONG` | 1,944,127.44 USD | `1,565.32` | `1342.15` | `1242.05` | `833.43` | -156,767.78 USD | `-8.06%` | `10X Cross` |
| `1192` | `0xcf67...eb24` | `LONG` | 1,862,550.00 USD | `1,500.00` | `887.05` | `1242.05` | `678.84` | 531,978.63 USD | `+28.56%` | `10X Cross` |
| `1205` | `0xb695...a92d` | `LONG` | 1,841,737.70 USD | `1,483.00` | `1249.80` | `1242.05` | `0.000000` | -11,721.16 USD | `-0.64%` | `10X Cross` |
| `1269` | `0x2ab7...c2f8` | `LONG` | 1,747,556.38 USD | `1,400.51` | `813.26` | `1242.05` | `792.64` | 608,574.69 USD | `+34.82%` | `3X Cross` |
| `1293` | `0x11be...8b1d` | `LONG` | 1,708,780.86 USD | `1,375.83` | `1206.55` | `1242.05` | `1134.45` | 48,772.90 USD | `+2.85%` | `10X Isolated` |
| `1404` | `0xe065...0f85` | `SHORT` | 1,567,782.84 USD | `1,262.61` | `1087.02` | `1242.05` | `1832.42` | -195,306.71 USD | `-12.46%` | `10X Cross` |
| `1414` | `0x039c...0ebd` | `SHORT` | 1,553,433.21 USD | `1,250.55` | `1239.86` | `1242.05` | `3643.51` | -2,921.93 USD | `-0.19%` | `10X Cross` |
| `1440` | `0x7277...0b98` | `SHORT` | 1,535,796.26 USD | `1,234.96` | `1298.48` | `1242.05` | `2419.74` | 67,773.16 USD | `+4.41%` | `10X Cross` |
| `1469` | `0x5975...9abd` | `LONG` | 1,490,400.00 USD | `1,200.00` | `1179.54` | `1242.05` | `570.27` | 74,957.21 USD | `+5.03%` | `5X Cross` |
| `1476` | `0xdf83...3cff` | `SHORT` | 1,481,435.30 USD | `1,192.59` | `1255.41` | `1242.05` | `1762.58` | 15,760.05 USD | `+1.06%` | `10X Cross` |
| `1496` | `0x5323...b23c` | `LONG` | 1,454,813.02 USD | `1,169.84` | `1239.58` | `1242.05` | `0.000000` | 4,700.15 USD | `+0.32%` | `5X Cross` |
| `1503` | `0x69cc...14fd` | `SHORT` | 1,444,267.30 USD | `1,161.36` | `675.33` | `1242.05` | `8114.93` | -659,961.77 USD | `-45.70%` | `10X Cross` |
| `1507` | `0x71d0...8c26` | `SHORT` | 1,441,899.29 USD | `1,161.23` | `1289.25` | `1242.05` | `5749.19` | 55,219.95 USD | `+3.83%` | `10X Cross` |
| `1526` | `0x3fc5...c0c1` | `SHORT` | 1,426,362.48 USD | `1,148.44` | `1264.34` | `1242.05` | `3106.26` | 25,651.30 USD | `+1.80%` | `10X Cross` |
| `1545` | `0x2847...d47b` | `LONG` | 1,412,966.37 USD | `1,138.07` | `1233.89` | `1242.05` | `0.000000` | 8,708.45 USD | `+0.62%` | `5X Cross` |
| `1561` | `0xe35c...a1d3` | `LONG` | 1,400,372.05 USD | `1,127.06` | `1318.20` | `1242.05` | `694.37` | -85,323.30 USD | `-6.09%` | `2X Isolated` |
| `1569` | `0x51f6...2b39` | `SHORT` | 1,388,848.26 USD | `1,115.72` | `1299.77` | `1242.05` | `2665.26` | 61,329.35 USD | `+4.42%` | `10X Cross` |
| `1570` | `0xfc27...9d9d` | `SHORT` | 1,387,952.90 USD | `1,112.32` | `1315.10` | `1242.05` | `16533.59` | 74,858.86 USD | `+5.39%` | `10X Cross` |
| `1572` | `0x5f94...4b96` | `LONG` | 1,385,165.34 USD | `1,115.27` | `538.00` | `1242.05` | `0.000000` | 785,147.70 USD | `+56.68%` | `10X Cross` |
| `1589` | `0x266b...efcb` | `LONG` | 1,368,180.00 USD | `1,100.00` | `863.84` | `1242.05` | `332.73` | 417,955.24 USD | `+30.55%` | `10X Cross` |
| `1596` | `0x71df...a23d` | `SHORT` | 1,363,624.45 USD | `1,098.28` | `513.50` | `1242.05` | `2551.84` | -799,654.26 USD | `-58.64%` | `2X Cross` |
| `1610` | `0xef96...9383` | `SHORT` | 1,339,595.63 USD | `1,078.84` | `1259.08` | `1242.05` | `5172.85` | 18,752.15 USD | `+1.40%` | `10X Cross` |
| `1611` | `0xbfc7...80b4` | `SHORT` | 1,335,042.50 USD | `1,075.00` | `558.03` | `1242.05` | `4647.76` | -735,163.77 USD | `-55.07%` | `10X Cross` |
| `1686` | `0x123d...3bff` | `SHORT` | 1,252,193.87 USD | `1,008.37` | `490.16` | `1242.05` | `4561.43` | -757,933.65 USD | `-60.53%` | `10X Cross` |
| `1693` | `0xb5ff...d912` | `LONG` | 1,244,300.00 USD | `1,000.00` | `1280.79` | `1242.05` | `452.80` | -36,487.44 USD | `-2.93%` | `2X Cross` |
| `1694` | `0xe282...df29` | `LONG` | 1,242,200.00 USD | `1,000.00` | `420.99` | `1242.05` | `209.49` | 821,213.14 USD | `+66.11%` | `10X Cross` |
| `1697` | `0x668c...ea2e` | `SHORT` | 1,241,546.10 USD | `1,000.00` | `1406.98` | `1242.05` | `4181.31` | 165,435.89 USD | `+13.32%` | `10X Cross` |
| `1723` | `0x17f0...094f` | `LONG` | 1,222,402.17 USD | `984.30` | `1287.23` | `1242.05` | `536.80` | -44,617.99 USD | `-3.65%` | `5X Cross` |
| `1796` | `0x757d...94ba` | `LONG` | 1,150,792.50 USD | `925.00` | `1558.31` | `1242.05` | `0.000000` | -290,648.09 USD | `-25.26%` | `10X Cross` |
| `1835` | `0xb911...5525` | `LONG` | 1,117,800.00 USD | `900.00` | `1294.82` | `1242.05` | `1070.32` | -47,537.82 USD | `-4.25%` | `10X Cross` |
| `1881` | `0xcf0a...856f` | `LONG` | 1,081,440.47 USD | `871.15` | `1292.19` | `1242.05` | `1003.71` | -44,254.38 USD | `-4.09%` | `4X Cross` |
| `1899` | `0xdf95...7d72` | `SHORT` | 1,064,296.82 USD | `857.34` | `1074.39` | `1242.05` | `45991.23` | -143,176.60 USD | `-13.45%` | `10X Cross` |
| `1952` | `0x601c...4f54` | `SHORT` | 1,023,847.20 USD | `824.42` | `615.11` | `1242.05` | `3126.66` | -516,734.45 USD | `-50.47%` | `5X Cross` |
| `1960` | `0xae55...2236` | `LONG` | 1,017,177.92 USD | `817.47` | `1467.80` | `1242.05` | `0.000000` | -182,703.30 USD | `-17.96%` | `10X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
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
| `ANNOUNCEMENT` | `INFO` | `1121.60` | 594.45 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 0.59K USD at 1121.6000 USD [API] | `2026-10-24 14:16:53` |
| `ANNOUNCEMENT` | `INFO` | `1121.60` | 179.46 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 0.18K USD at 1121.6000 USD [API] | `2026-10-24 14:16:53` |
| `ANNOUNCEMENT` | `INFO` | `1122.30` | 2,020.14 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 2.02K USD at 1122.3000 USD [API] | `2026-10-24 14:16:53` |
| `ANNOUNCEMENT` | `INFO` | `1131.50` | 2,036.70 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 2.04K USD at 1131.5000 USD [API] | `2026-10-24 14:16:43` |
| `ANNOUNCEMENT` | `INFO` | `1132.20` | 2,037.96 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 2.04K USD at 1132.2000 USD [API] | `2026-10-24 14:16:43` |
| `ANNOUNCEMENT` | `INFO` | `1133.60` | 2,040.48 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 2.04K USD at 1133.6000 USD [API] | `2026-10-24 14:16:30` |
| `ANNOUNCEMENT` | `INFO` | `1135.80` | 545.18 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 0.55K USD at 1135.8000 USD [API] | `2026-10-24 14:16:14` |
| `ANNOUNCEMENT` | `INFO` | `1297.50` | 1,699.73 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Long: 1.70K USD at 1297.5000 USD [API] | `2026-10-28 19:57:32` |
| `ANNOUNCEMENT` | `INFO` | `1297.70` | 7,708.34 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Long: 7.71K USD at 1297.7000 USD [API] | `2026-10-28 19:57:32` |
| `ANNOUNCEMENT` | `INFO` | `1297.60` | 2,141.04 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Long: 2.14K USD at 1297.6000 USD [API] | `2026-10-28 19:57:32` |
| `ANNOUNCEMENT` | `INFO` | `1297.60` | 2,141.04 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Long: 2.14K USD at 1297.6000 USD [API] | `2026-10-28 19:57:32` |
| `ANNOUNCEMENT` | `INFO` | `1297.60` | 2,141.04 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Long: 2.14K USD at 1297.6000 USD [API] | `2026-10-28 19:57:32` |
| `ANNOUNCEMENT` | `INFO` | `1297.60` | 13,650.75 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Long: 13.65K USD at 1297.6000 USD [API] | `2026-10-28 19:57:32` |
| `ANNOUNCEMENT` | `INFO` | `1297.50` | 2,140.88 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Long: 2.14K USD at 1297.5000 USD [API] | `2026-10-28 19:57:32` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`1403.54` (Vol: 3,000,000.00 USD, Dist: `+12.15%`) | Long MP=`1223.03` (Vol: 1,200,000.00 USD, Dist: `--2.28%`)
  * 48H Horizon: Short MP=`1403.54` (Vol: 3,000,000.00 USD, Dist: `+12.15%`) | Long MP=`1223.03` (Vol: 1,200,000.00 USD, Dist: `--2.28%`)
  * 3D Horizon: Short MP=`1403.54` (Vol: 3,000,000.00 USD, Dist: `+12.15%`) | Long MP=`1200.05` (Vol: 1,600,000.00 USD, Dist: `--4.11%`)
  * 7D Horizon: Short MP=`1404.10` (Vol: 3,000,000.00 USD, Dist: `+12.19%`) | Long MP=`1200.46` (Vol: 3,000,000.00 USD, Dist: `--4.08%`)
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
| `5m` | `BALANCED` | 0.00 USD | 1,750.00 USD | 1,750.00 USD | 1,750.00 USD | `1` | `2026-10-29 23:05:00 UTC - 2026-10-29 23:10:00 UTC` |
| `15m` | `BALANCED` | 0.00 USD | 1,750.00 USD | 1,750.00 USD | 1,750.00 USD | `1` | `2026-10-29 23:00:00 UTC - 2026-10-29 23:15:00 UTC` |
| `1h` | `BALANCED` | 0.00 USD | 1,750.00 USD | 1,750.00 USD | 1,750.00 USD | `1` | `2026-10-29 23:00:00 UTC - 2026-10-30 00:00:00 UTC` |
| `4h` | `BALANCED` | 0.00 USD | 1,750.00 USD | 1,750.00 USD | 1,750.00 USD | `1` | `2026-10-29 20:00:00 UTC - 2026-10-30 00:00:00 UTC` |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `0 USD` | Total OI Tokens: `-`
  * 1h OI Change: `0.00%` | 4h OI Change: `0.00%` | 24h OI Change: `0.00%`
  * Exchange Breakdown: Binance=`-` | Bybit=`-` | OKX=`-` | Hyperliquid=`-`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `12.75K` | Last 24h: `33.19K` | Last 3d: `283.86K` | Last 7d: `777.60K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `-0.0008%` | **USDT OKX** | `0.0019%` |
| **USDT Bybit** | `0.0100%` | **USDT KuCoin** | `-0.0041%` |
| **USDT MEXC** | `-0.0009%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `0.0049%` | **USDT Bitget** | `0.0100%` |
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
| `5:00 UTC` | `1229.25` | `1237.79` | `1229.25` | `1264.35` | `1206.75` | 149,162,484.89 USD | 77,012,548.38 USD | 72,149,936.51 USD | 4,862,611.87 USD | `+3.26%` | `9B / 11S` |
| `0:00 UTC` | `1249.95` | `1248.07` | `1249.95` | `1259.85` | `1233.15` | 61,152,789.32 USD | 32,267,997.87 USD | 28,884,791.45 USD | 3,383,206.41 USD | `+5.53%` | `6B / 4S` |
| `5:00 UTC` | `1273.95` | `1271.85` | `1273.95` | `1286.25` | `1253.25` | 67,607,862.35 USD | 37,234,359.13 USD | 30,373,503.22 USD | 6,860,855.91 USD | `+10.15%` | `6B / 2S` |
| `0:00 UTC` | `1294.65` | `1287.25` | `1294.65` | `1297.05` | `1269.15` | 47,983,765.84 USD | 24,978,907.15 USD | 23,004,858.69 USD | 1,974,048.46 USD | `+4.11%` | `4B / 9S` |
| `5:00 UTC` | `1264.05` | `1267.99` | `1264.05` | `1276.65` | `1260.75` | 31,349,361.20 USD | 15,100,777.24 USD | 16,248,583.96 USD | -1,147,806.72 USD | `-3.66%` | `0B / 1S` |
| `0:00 UTC` | `1261.05` | `1255.07` | `1261.05` | `1269.15` | `1241.25` | 60,510,539.13 USD | 31,467,084.85 USD | 29,043,454.28 USD | 2,423,630.57 USD | `+4.01%` | `3B / 5S` |
| `5:00 UTC` | `1259.85` | `1254.56` | `1259.85` | `1263.15` | `1242.15` | 22,141,749.31 USD | 11,943,317.16 USD | 10,198,432.15 USD | 1,744,885.01 USD | `+7.88%` | `3B / 3S` |
| `0:00 UTC` | `1257.15` | `1255.20` | `1257.15` | `1264.35` | `1245.45` | 28,871,970.63 USD | 12,578,804.66 USD | 16,293,165.97 USD | -3,714,361.32 USD | `-12.86%` | `7B / 2S` |
| `5:00 UTC` | `1241.25` | `1245.94` | `1241.25` | `1254.45` | `1236.15` | 26,347,049.74 USD | 11,469,285.37 USD | 14,877,764.37 USD | -3,408,478.99 USD | `-12.94%` | `1B / 6S` |
| `0:00 UTC` | `1240.05` | `1237.72` | `1240.05` | `1243.65` | `1232.25` | 8,272,932.35 USD | 3,060,794.54 USD | 5,212,137.81 USD | -2,151,343.27 USD | `-26.00%` | `1B / 6S` |

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
| `5m` | -1,110,000.00 USD | -8,040,000.00 USD | **`DISTRIBUTION`** |
| `15m` | -2,250,000.00 USD | -11,780,000.00 USD | **`DISTRIBUTION`** |
| `30m` | -2,270,000.00 USD | -14,800,000.00 USD | **`DISTRIBUTION`** |
| `1h` | -1,860,000.00 USD | -9,730,000.00 USD | **`DISTRIBUTION`** |
| `2h` | 2,700,000.00 USD | 5,990,000.00 USD | **`ACCUMULATION`** |
| `4h` | -13,980,000.00 USD | -17,780,000.00 USD | **`DISTRIBUTION`** |
| `6h` | -8,570,000.00 USD | -32,070,000.00 USD | **`DISTRIBUTION`** |
| `8h` | 7,220,000.00 USD | 77,780,000.00 USD | **`ACCUMULATION`** |
| `12h` | 18,220,000.00 USD | 74,020,000.00 USD | **`ACCUMULATION`** |
| `24h` | 146,100.00 USD | 53,390,000.00 USD | **`ACCUMULATION`** |
| `1w` | 34,420,000.00 USD | 230,440,000.00 USD | **`ACCUMULATION`** |
| `30d` | 55,800,000.00 USD | -551,300,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-1.11M` | 15m=`-2.25M` | 1h=`-1.86M` | 24h=`+146.10K`
* Futures Capital Netflows: 5m=`-8.04M` | 15m=`-11.78M` | 1h=`-9.73M` | 24h=`+53.39M`
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
  * `2026-10-30 04:14:42 IST`: [economics.td.com] - (Sentiment: `Neutral`)
  * `2026-10-30 04:31:42 IST`: [investinglive.com] - (Sentiment: `Neutral`)
  * `2026-10-30 04:31:42 IST`: [msn.com] - (Sentiment: `Neutral`)
  * `2026-10-30 04:30:42 IST`: [morningstar.com] - (Sentiment: `Neutral`)
  * `2026-10-30 04:30:42 IST`: [sec.gov] - (Sentiment: `Neutral`)
  * `2026-10-30 01:32:42 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 01:32:42 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 00:32:42 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:32:42 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:32:42 IST`: [@DeItaone] - (Sentiment: `Neutral`)
  * `2026-10-29 23:32:42 IST`: [@mb_ghalibaf] - (Sentiment: `Neutral`)
  * `2026-10-29 23:32:42 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-29 23:32:42 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-29 23:32:42 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:32:42 IST`: [fxstreet.com] - (Sentiment: `Neutral`)


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
  * Execution Entry: `1241.41` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `1212.59` (Risk Distance: `28.82` pts)
  * +2.5R Take Profit: `1313.47`
  * Mathematical Lot Sizing: **`0.34 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `1269.57` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `1298.39` (Risk Distance: `28.82` pts)
  * +2.5R Take Profit: `1197.51`
  * Mathematical Lot Sizing: **`0.34 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`1232.69`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
