# 🏛️ SOVEREIGN CANDIDATE DOSSIER: ZECUSD
**Canonical Key**: `ZECUSD` | **Broker Instrument**: `ZECUSD.p` | **Asset Class**: `Crypto Altcoin`
**Timestamp**: `2026-10-30 07:36:16 IST` (`2026-10-30 02:06:16 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `1230.37` | **Live Ask Quote**: `1231.87` | **Mid Price**: `1231.12`
- **Spread Points**: `150.00` | **Spread BPS**: `12.18 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `1278.56` | VWAP Z-Score: `-0.85` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `21.17` (Volatility Regime: `HIGH_EXPANSION`)
  * 14-Period RSI: `36.27` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `1390.74` | Lower -3.00σ Band: `1166.38`
  * Upper +2.51σ Band: `1372.42` | Lower -2.51σ Band: `1184.70`
  * Upper +2.01σ Band: `1353.72` | Lower -2.01σ Band: `1203.40`
  * Upper +2.00σ Band: `1353.35` | Lower -2.00σ Band: `1203.77`
  * Upper +1.28σ Band: `1326.43` | Lower -1.28σ Band: `1230.69`
  * Upper +1.00σ Band: `1315.95` | Lower -1.00σ Band: `1241.17`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`1254.23` | EMA-20=`1271.86` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`1284.11` (Slope: `+0.0000`) | EMA-100=`1283.66`
  * Institutional Anchors: EMA-144=`1281.46` | EMA-200=`1278.91` (Slope: `-0.2620`) | EMA-233=`1279.20`
- **Range Boundaries**: 24H High=`1396.49` | 24H Low=`1206.89` | Weekly High=`1396.49` | Weekly Low=`1206.89`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `1257.73` (Distance: `-2.10%`)
  * Point of Control (POC) = `1229.90` (Distance: `+0.12%`)
  * Value Area Low (VAL) = `1216.75` (Distance: `+1.20%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`1309.91` | POC=`1246.71` | VAL=`1230.27`
  * Prior Day Extremes: PDH=`1396.49` | PDL=`1206.89` | PDC=`1244.38`
  * Monday Range Blueprint: High=`1267.53` | Mid=`1222.14` | Low=`1176.75`
  * Developing Weekly Value Area: Weekly VAH=`1294.68` | Weekly POC=`1239.01` | Weekly VAL=`1196.53`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`1296.00` | Low=`1180.03`
  * London Session (08:00-16:00 UTC): High=`1236.04` | Low=`1226.20`
  * New York Session (13:00-21:00 UTC): High=`1238.51` | Low=`1223.73`
  * Initial Balance (First Hour): IB High=`1234.81` | IB Low=`1227.43`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `1226.20` - `1236.04`
  * Optimal Trade Entry (OTE 0.705): `1233.58`
  * Structural Invalidation Anchor (0.786): `1240.97`

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
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 07:28:02 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `13` | `0xb83d...6e36` | `SHORT` | 64,622,715.79 USD | `52,385.47` | `1336.45` | `1235.70` | `3926.80` | 5,387,851.61 USD | `+8.34%` | `3X Cross` |
| `22` | `0x5b5d...c060` | `SHORT` | 49,493,734.37 USD | `40,121.38` | `1478.36` | `1235.70` | `5484.43` | 9,820,300.74 USD | `+19.84%` | `3X Cross` |
| `42` | `0x7fda...17d1` | `SHORT` | 28,120,328.19 USD | `22,806.43` | `1261.40` | `1235.70` | `2926.96` | 647,815.94 USD | `+2.30%` | `5X Cross` |
| `84` | `0x60b0...991e` | `LONG` | 20,684,385.50 USD | `16,779.74` | `1179.65` | `1235.70` | `951.81` | 890,138.48 USD | `+4.30%` | `10X Cross` |
| `143` | `0xc36a...105b` | `LONG` | 14,192,841.06 USD | `11,510.82` | `1215.14` | `1235.70` | `980.25` | 205,560.03 USD | `+1.45%` | `10X Cross` |
| `157` | `0x9071...5c0b` | `LONG` | 12,972,025.49 USD | `10,517.29` | `1353.83` | `1235.70` | `0.0650` | -1,266,593.39 USD | `-9.76%` | `1X Cross` |
| `180` | `0x8742...8427` | `LONG` | 11,336,810.84 USD | `9,201.21` | `1286.37` | `1235.70` | `721.93` | -499,359.15 USD | `-4.40%` | `10X Cross` |
| `195` | `0x9ffd...ce40` | `LONG` | 10,592,762.83 USD | `8,586.87` | `1250.83` | `1235.70` | `619.06` | -147,978.50 USD | `-1.40%` | `5X Cross` |
| `196` | `0x58b2...11f3` | `LONG` | 10,561,702.87 USD | `8,563.08` | `1246.56` | `1235.70` | `383.30` | -112,714.70 USD | `-1.07%` | `10X Cross` |
| `202` | `0xad59...ba81` | `SHORT` | 10,393,080.00 USD | `8,425.00` | `330.91` | `1235.70` | `2149.14` | -7,605,122.23 USD | `-73.17%` | `10X Cross` |
| `206` | `0xdd53...2b13` | `SHORT` | 10,108,847.73 USD | `8,195.92` | `741.54` | `1235.70` | `9102.13` | -4,031,251.36 USD | `-39.88%` | `3X Cross` |
| `221` | `0x880a...311c` | `SHORT` | 9,502,866.63 USD | `7,707.11` | `1367.50` | `1235.70` | `2224.70` | 1,036,617.57 USD | `+10.91%` | `10X Cross` |
| `270` | `0x2b61...2f6c` | `LONG` | 8,393,031.00 USD | `6,807.00` | `1453.56` | `1235.70` | `519.17` | -1,501,320.22 USD | `-17.89%` | `10X Cross` |
| `291` | `0x2ae5...83e7` | `LONG` | 7,933,356.00 USD | `6,436.80` | `1391.82` | `1235.70` | `0.000000` | -1,025,535.99 USD | `-12.93%` | `1X Cross` |
| `328` | `0x26b6...9a13` | `LONG` | 6,694,898.73 USD | `5,433.73` | `1282.23` | `1235.70` | `227.03` | -272,404.50 USD | `-4.07%` | `10X Cross` |
| `347` | `0x45d2...4029` | `SHORT` | 6,442,277.50 USD | `5,227.00` | `833.44` | `1235.70` | `9732.33` | -2,085,899.53 USD | `-32.38%` | `5X Cross` |
| `365` | `0xea00...a918` | `LONG` | 6,163,500.00 USD | `5,000.00` | `739.16` | `1235.70` | `0.000000` | 2,467,684.89 USD | `+40.04%` | `5X Cross` |
| `375` | `0xdd7a...8830` | `LONG` | 5,995,044.37 USD | `4,860.19` | `897.48` | `1235.70` | `790.79` | 1,633,140.69 USD | `+27.24%` | `10X Cross` |
| `442` | `0xa61c...66b9` | `LONG` | 4,794,292.80 USD | `3,888.00` | `1148.34` | `1235.70` | `0.000000` | 329,550.66 USD | `+6.87%` | `10X Cross` |
| `447` | `0xecb6...2b00` | `SHORT` | 4,777,172.19 USD | `3,874.43` | `1286.92` | `1235.70` | `8685.59` | 208,891.73 USD | `+4.37%` | `5X Cross` |
| `465` | `0x9aa5...58af` | `SHORT` | 4,586,398.17 USD | `3,720.31` | `1205.51` | `1235.70` | `3798.97` | -101,511.37 USD | `-2.21%` | `10X Cross` |
| `471` | `0x0153...8052` | `SHORT` | 4,555,787.94 USD | `3,698.18` | `1307.82` | `1235.70` | `2504.77` | 280,782.81 USD | `+6.16%` | `1X Isolated` |
| `538` | `0xd21d...90f1` | `LONG` | 4,009,200.00 USD | `3,250.00` | `1253.64` | `1235.70` | `875.98` | -65,141.73 USD | `-1.62%` | `4X Isolated` |
| `549` | `0x456f...cdf1` | `LONG` | 3,900,368.49 USD | `3,162.29` | `1268.22` | `1235.70` | `501.39` | -110,120.66 USD | `-2.82%` | `10X Cross` |
| `553` | `0x1338...c48e` | `LONG` | 3,889,546.05 USD | `3,149.43` | `1018.52` | `1235.70` | `820.27` | 681,800.51 USD | `+17.53%` | `4X Isolated` |
| `571` | `0x325e...9564` | `LONG` | 3,826,516.18 USD | `3,101.91` | `1298.07` | `1235.70` | `262.29` | -199,994.52 USD | `-5.23%` | `10X Cross` |
| `576` | `0x382b...3e39` | `LONG` | 3,804,175.62 USD | `3,084.30` | `1211.32` | `1235.70` | `0.000000` | 68,092.28 USD | `+1.79%` | `10X Cross` |
| `578` | `0xdbe0...d6d5` | `LONG` | 3,800,867.30 USD | `3,085.37` | `422.97` | `1235.70` | `338.59` | 2,495,862.81 USD | `+65.67%` | `3X Isolated` |
| `593` | `0x2e30...4cb5` | `SHORT` | 3,701,334.73 USD | `3,000.92` | `1288.94` | `1235.70` | `2895.82` | 166,681.76 USD | `+4.50%` | `2X Cross` |
| `594` | `0x469e...58a5` | `SHORT` | 3,700,200.00 USD | `3,000.00` | `1234.30` | `1235.70` | `2236.85` | 2,702.53 USD | `+0.07%` | `10X Cross` |
| `598` | `0x9c06...0560` | `SHORT` | 3,688,217.28 USD | `2,989.80` | `786.00` | `1235.70` | `2660.13` | -1,338,222.28 USD | `-36.28%` | `10X Cross` |
| `602` | `0x27c9...d65d` | `SHORT` | 3,657,105.00 USD | `2,965.06` | `1254.41` | `1235.70` | `1741.47` | 62,299.23 USD | `+1.70%` | `10X Cross` |
| `630` | `0xd4c1...3d1d` | `SHORT` | 3,488,251.65 USD | `2,827.93` | `1298.65` | `1235.70` | `2951.89` | 184,228.40 USD | `+5.28%` | `10X Cross` |
| `633` | `0x4cae...7c34` | `LONG` | 3,452,732.91 USD | `2,800.27` | `1114.07` | `1235.70` | `868.52` | 333,043.62 USD | `+9.65%` | `10X Cross` |
| `704` | `0xa183...0482` | `LONG` | 3,124,422.00 USD | `2,534.00` | `530.25` | `1235.70` | `444.52` | 1,780,759.28 USD | `+56.99%` | `5X Isolated` |
| `707` | `0xac48...3201` | `LONG` | 3,120,580.05 USD | `2,531.50` | `1378.58` | `1235.70` | `472.24` | -369,292.23 USD | `-11.83%` | `10X Cross` |
| `717` | `0x0871...e927` | `LONG` | 3,082,500.00 USD | `2,500.00` | `1276.50` | `1235.70` | `0.000000` | -108,750.00 USD | `-3.53%` | `10X Cross` |
| `738` | `0x9b86...6e6e` | `LONG` | 3,038,726.88 USD | `2,463.30` | `637.58` | `1235.70` | `882.45` | 1,468,177.60 USD | `+48.32%` | `3X Cross` |
| `782` | `0xb2f7...af9f` | `SHORT` | 2,854,204.99 USD | `2,313.72` | `746.63` | `1235.70` | `4623.32` | -1,126,716.25 USD | `-39.48%` | `10X Cross` |
| `814` | `0xf48f...10fe` | `LONG` | 2,736,729.26 USD | `2,218.49` | `1517.87` | `1235.70` | `1055.12` | -630,657.56 USD | `-23.04%` | `3X Cross` |
| `846` | `0x5bc4...3b0c` | `SHORT` | 2,625,923.98 USD | `2,130.74` | `1089.65` | `1235.70` | `3748.97` | -304,166.40 USD | `-11.58%` | `5X Cross` |
| `861` | `0x8de4...b9aa` | `SHORT` | 2,579,815.34 USD | `2,091.29` | `1331.35` | `1235.70` | `1689.90` | 204,424.36 USD | `+7.92%` | `3X Cross` |
| `866` | `0x4fe2...ac59` | `SHORT` | 2,555,074.44 USD | `2,071.57` | `1478.56` | `1235.70` | `1876.51` | 507,871.78 USD | `+19.88%` | `10X Cross` |
| `876` | `0xdf57...93f5` | `LONG` | 2,531,780.94 USD | `2,054.35` | `1227.36` | `1235.70` | `897.22` | 10,358.90 USD | `+0.41%` | `4X Isolated` |
| `881` | `0xbcd4...0dd2` | `LONG` | 2,509,043.71 USD | `2,033.92` | `1228.20` | `1235.70` | `632.35` | 10,992.90 USD | `+0.44%` | `10X Cross` |
| `893` | `0x9a99...d21a` | `LONG` | 2,466,800.00 USD | `2,000.00` | `1278.44` | `1235.70` | `0.000000` | -90,073.67 USD | `-3.65%` | `10X Cross` |
| `915` | `0x77ee...2902` | `SHORT` | 2,399,454.99 USD | `1,946.03` | `759.84` | `1235.70` | `5469.78` | -920,777.48 USD | `-38.37%` | `10X Cross` |
| `926` | `0x3e2f...b269` | `SHORT` | 2,374,924.03 USD | `1,925.51` | `1134.87` | `1235.70` | `2931.83` | -189,725.18 USD | `-7.99%` | `10X Cross` |
| `940` | `0x4f12...618b` | `SHORT` | 2,338,871.75 USD | `1,896.28` | `1608.30` | `1235.70` | `2116.79` | 710,912.64 USD | `+30.40%` | `3X Cross` |
| `976` | `0x866d...d6e1` | `LONG` | 2,221,747.44 USD | `1,802.05` | `674.73` | `1235.70` | `337.77` | 1,005,846.13 USD | `+45.27%` | `10X Cross` |
| `977` | `0x413c...886c` | `LONG` | 2,220,120.00 USD | `1,800.00` | `1206.29` | `1235.70` | `0.000000` | 48,796.78 USD | `+2.20%` | `10X Cross` |
| `999` | `0x2309...a2d9` | `LONG` | 2,158,906.36 USD | `1,750.37` | `1186.09` | `1235.70` | `820.07` | 82,812.25 USD | `+3.84%` | `8X Cross` |
| `1043` | `0x2edd...8179` | `SHORT` | 2,046,404.59 USD | `1,654.73` | `1261.58` | `1235.70` | `2931.46` | 41,168.64 USD | `+2.01%` | `10X Cross` |
| `1049` | `0x265e...7f70` | `LONG` | 2,037,586.46 USD | `1,651.74` | `1382.98` | `1235.70` | `0.000000` | -246,736.30 USD | `-12.11%` | `3X Cross` |
| `1051` | `0xb122...e4ba` | `LONG` | 2,035,258.01 USD | `1,650.12` | `1256.26` | `1235.70` | `936.41` | -37,729.86 USD | `-1.85%` | `10X Cross` |
| `1056` | `0xfe7c...b7ae` | `SHORT` | 2,026,032.18 USD | `1,642.64` | `1346.92` | `1235.70` | `6371.01` | 186,476.44 USD | `+9.20%` | `10X Cross` |
| `1060` | `0x3e47...aaf6` | `LONG` | 2,018,515.01 USD | `1,636.28` | `1278.38` | `1235.70` | `1057.48` | -73,276.78 USD | `-3.63%` | `10X Cross` |
| `1079` | `0x7f75...9edf` | `LONG` | 1,980,890.21 USD | `1,605.78` | `1199.97` | `1235.70` | `981.35` | 53,998.32 USD | `+2.73%` | `10X Cross` |
| `1082` | `0x6646...6de5` | `SHORT` | 1,973,600.00 USD | `1,600.00` | `660.64` | `1235.70` | `3994.71` | -916,575.03 USD | `-46.44%` | `10X Cross` |
| `1085` | `0x023a...2355` | `SHORT` | 1,968,225.57 USD | `1,596.29` | `1310.00` | `1235.70` | `4559.24` | 122,907.46 USD | `+6.24%` | `10X Cross` |
| `1110` | `0xab59...59b5` | `LONG` | 1,930,978.75 USD | `1,565.32` | `1342.15` | `1235.70` | `852.07` | -169,916.47 USD | `-8.80%` | `10X Cross` |
| `1164` | `0xcf67...eb24` | `LONG` | 1,850,100.00 USD | `1,500.00` | `887.05` | `1235.70` | `740.45` | 519,528.63 USD | `+28.08%` | `10X Cross` |
| `1177` | `0xb695...a92d` | `LONG` | 1,828,539.00 USD | `1,483.00` | `1249.80` | `1235.70` | `0.000000` | -24,919.85 USD | `-1.36%` | `10X Cross` |
| `1180` | `0x7277...0b98` | `SHORT` | 1,819,575.09 USD | `1,475.73` | `1287.86` | `1235.70` | `2245.76` | 80,957.03 USD | `+4.45%` | `10X Cross` |
| `1251` | `0x2ab7...c2f8` | `LONG` | 1,725,568.37 USD | `1,400.51` | `813.26` | `1235.70` | `796.24` | 586,586.69 USD | `+33.99%` | `3X Cross` |
| `1265` | `0x11be...8b1d` | `LONG` | 1,696,948.72 USD | `1,375.83` | `1206.55` | `1235.70` | `1134.50` | 36,940.76 USD | `+2.18%` | `10X Isolated` |
| `1307` | `0xfc27...9d9d` | `SHORT` | 1,625,669.70 USD | `1,319.43` | `1298.53` | `1235.70` | `16452.83` | 87,647.07 USD | `+5.39%` | `10X Cross` |
| `1350` | `0x039c...0ebd` | `SHORT` | 1,564,590.69 USD | `1,268.93` | `1239.61` | `1235.70` | `3722.20` | 8,388.06 USD | `+0.54%` | `10X Cross` |
| `1357` | `0xe065...0f85` | `SHORT` | 1,557,303.17 USD | `1,262.61` | `1087.02` | `1235.70` | `1637.23` | -184,827.05 USD | `-11.87%` | `10X Cross` |
| `1372` | `0xf29c...9971` | `LONG` | 1,540,125.00 USD | `1,250.00` | `1245.71` | `1235.70` | `0.000000` | -17,008.32 USD | `-1.10%` | `10X Cross` |
| `1441` | `0x5975...9abd` | `LONG` | 1,480,080.00 USD | `1,200.00` | `1179.54` | `1235.70` | `648.67` | 64,637.21 USD | `+4.37%` | `5X Cross` |
| `1443` | `0x266b...efcb` | `LONG` | 1,477,440.00 USD | `1,200.00` | `893.76` | `1235.70` | `456.08` | 404,930.30 USD | `+27.41%` | `10X Cross` |
| `1454` | `0x2847...d47b` | `LONG` | 1,463,145.42 USD | `1,186.27` | `1232.07` | `1235.70` | `0.000000` | 1,576.92 USD | `+0.11%` | `5X Cross` |
| `1472` | `0x69cc...14fd` | `SHORT` | 1,431,956.88 USD | `1,161.36` | `675.33` | `1235.70` | `8327.80` | -647,651.35 USD | `-45.23%` | `10X Cross` |
| `1488` | `0x3fc5...c0c1` | `SHORT` | 1,416,485.90 USD | `1,148.44` | `1264.34` | `1235.70` | `3037.05` | 35,527.88 USD | `+2.51%` | `10X Cross` |
| `1524` | `0xe35c...a1d3` | `LONG` | 1,389,777.69 USD | `1,127.06` | `1318.20` | `1235.70` | `694.41` | -95,917.66 USD | `-6.90%` | `2X Isolated` |
| `1539` | `0x5f94...4b96` | `LONG` | 1,375,797.07 USD | `1,115.27` | `538.00` | `1235.70` | `0.000000` | 775,779.44 USD | `+56.39%` | `10X Cross` |
| `1552` | `0x71df...a23d` | `SHORT` | 1,354,179.24 USD | `1,098.28` | `513.50` | `1235.70` | `2559.62` | -790,209.05 USD | `-58.35%` | `2X Cross` |
| `1572` | `0x51f6...2b39` | `SHORT` | 1,327,460.13 USD | `1,076.61` | `1299.77` | `1235.70` | `2470.41` | 71,883.54 USD | `+5.42%` | `10X Cross` |
| `1573` | `0xbfc7...80b4` | `SHORT` | 1,325,905.00 USD | `1,075.00` | `558.03` | `1235.70` | `3246.43` | -726,026.27 USD | `-54.76%` | `10X Cross` |
| `1636` | `0x123d...3bff` | `SHORT` | 1,245,289.98 USD | `1,009.64` | `491.08` | `1235.70` | `4454.40` | -749,472.07 USD | `-60.18%` | `10X Cross` |
| `1659` | `0xe282...df29` | `LONG` | 1,233,500.00 USD | `1,000.00` | `420.99` | `1235.70` | `862.98` | 812,513.14 USD | `+65.87%` | `10X Cross` |
| `1660` | `0x9321...d75a` | `SHORT` | 1,233,500.00 USD | `1,000.00` | `1242.18` | `1235.70` | `6346.72` | 8,683.73 USD | `+0.70%` | `10X Cross` |
| `1661` | `0x668c...ea2e` | `SHORT` | 1,233,400.00 USD | `1,000.00` | `1406.98` | `1235.70` | `4178.40` | 173,581.99 USD | `+14.07%` | `10X Cross` |
| `1682` | `0x17f0...094f` | `LONG` | 1,213,543.47 USD | `984.30` | `1287.23` | `1235.70` | `536.85` | -53,476.69 USD | `-4.41%` | `5X Cross` |
| `1758` | `0x757d...94ba` | `LONG` | 1,139,970.00 USD | `925.00` | `1558.31` | `1235.70` | `0.000000` | -301,470.59 USD | `-26.45%` | `10X Cross` |
| `1761` | `0xaa82...9556` | `LONG` | 1,139,452.29 USD | `924.13` | `1254.72` | `1235.70` | `186.99` | -20,074.39 USD | `-1.76%` | `10X Cross` |
| `1763` | `0x71d0...8c26` | `SHORT` | 1,137,874.05 USD | `922.85` | `1273.23` | `1235.70` | `6996.06` | 37,122.72 USD | `+3.26%` | `10X Cross` |
| `1801` | `0xb911...5525` | `LONG` | 1,110,060.00 USD | `900.00` | `1294.82` | `1235.70` | `1070.37` | -55,277.82 USD | `-4.98%` | `10X Cross` |
| `1838` | `0xcf0a...856f` | `LONG` | 1,074,650.64 USD | `871.15` | `1292.19` | `1235.70` | `1014.28` | -51,044.21 USD | `-4.75%` | `4X Cross` |
| `1845` | `0xef96...9383` | `SHORT` | 1,070,588.18 USD | `868.42` | `1259.08` | `1235.70` | `5575.74` | 22,823.62 USD | `+2.13%` | `10X Cross` |
| `1864` | `0xdf95...7d72` | `SHORT` | 1,052,791.25 USD | `853.43` | `1074.39` | `1235.70` | `47300.04` | -135,871.90 USD | `-12.91%` | `10X Cross` |
| `1914` | `0x601c...4f54` | `SHORT` | 1,016,427.42 USD | `824.42` | `615.11` | `1235.70` | `3202.32` | -509,314.67 USD | `-50.11%` | `5X Cross` |
| `1939` | `0xae55...2236` | `LONG` | 1,007,531.78 USD | `817.47` | `1467.80` | `1235.70` | `0.000000` | -192,349.44 USD | `-19.09%` | `10X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
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
  * 24H Horizon: Short MP=`1403.54` (Vol: 3,000,000.00 USD, Dist: `+12.58%`) | Long MP=`1200.05` (Vol: 597,500.00 USD, Dist: `--3.74%`)
  * 48H Horizon: Short MP=`1403.54` (Vol: 3,000,000.00 USD, Dist: `+12.58%`) | Long MP=`1200.05` (Vol: 597,500.00 USD, Dist: `--3.74%`)
  * 3D Horizon: Short MP=`1403.54` (Vol: 3,000,000.00 USD, Dist: `+12.58%`) | Long MP=`1195.13` (Vol: 1,600,000.00 USD, Dist: `--4.14%`)
  * 7D Horizon: Short MP=`1404.10` (Vol: 3,000,000.00 USD, Dist: `+12.62%`) | Long MP=`1200.46` (Vol: 3,000,000.00 USD, Dist: `--3.71%`)
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
| `5m` | `BALANCED` | 0.00 USD | 1,750.00 USD | 1,750.00 USD | 1,750.00 USD | `1` | `2026-10-30 01:55:00 UTC - 2026-10-30 02:00:00 UTC` |
| `15m` | `BALANCED` | 0.00 USD | 1,750.00 USD | 1,750.00 USD | 1,750.00 USD | `1` | `2026-10-30 01:45:00 UTC - 2026-10-30 02:00:00 UTC` |
| `1h` | `BALANCED` | 0.00 USD | 1,750.00 USD | 1,750.00 USD | 1,750.00 USD | `1` | `2026-10-30 01:00:00 UTC - 2026-10-30 02:00:00 UTC` |
| `4h` | `BALANCED` | 0.00 USD | 1,750.00 USD | 1,750.00 USD | 1,750.00 USD | `1` | `2026-10-30 00:00:00 UTC - 2026-10-30 04:00:00 UTC` |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `0 USD` | Total OI Tokens: `-`
  * 1h OI Change: `0.00%` | 4h OI Change: `0.00%` | 24h OI Change: `0.00%`
  * Exchange Breakdown: Binance=`-` | Bybit=`-` | OKX=`-` | Hyperliquid=`-`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `71.26K` | Last 24h: `133.88K` | Last 3d: `245.74K` | Last 7d: `771.70K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0079%` | **USDT OKX** | `0.0100%` |
| **USDT Bybit** | `0.0100%` | **USDT KuCoin** | `0.0100%` |
| **USDT MEXC** | `0.0076%` | **USDT BingX** | `0.0100%` |
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
| `0:00 UTC` | `1232.25` | `1238.43` | `1232.25` | `1250.55` | `1228.35` | 25,461,092.94 USD | 11,564,862.97 USD | 13,896,229.97 USD | -2,331,367.00 USD | `-9.16%` | `5B / 7S` |
| `5:00 UTC` | `1226.85` | `1227.98` | `1226.85` | `1239.75` | `1221.15` | 38,101,048.89 USD | 19,322,035.41 USD | 18,779,013.49 USD | 543,021.92 USD | `+1.43%` | `4B / 1S` |
| `0:00 UTC` | `1224.15` | `1225.28` | `1224.15` | `1233.15` | `1216.35` | 41,862,859.26 USD | 20,823,357.89 USD | 21,039,501.37 USD | -216,143.49 USD | `-0.52%` | `5B / 3S` |
| `5:00 UTC` | `1209.15` | `1203.96` | `1209.15` | `1231.05` | `1180.35` | 101,980,019.94 USD | 48,295,180.78 USD | 53,684,839.16 USD | -5,389,658.38 USD | `-5.29%` | `3B / 24S` |
| `0:00 UTC` | `1197.75` | `1211.98` | `1197.75` | `1236.15` | `1189.35` | 90,739,097.90 USD | 52,854,086.90 USD | 37,885,011.00 USD | 14,969,075.89 USD | `+16.50%` | `25B / 1S` |
| `5:00 UTC` | `1232.55` | `1227.83` | `1232.55` | `1237.35` | `1215.45` | 35,400,223.44 USD | 18,306,250.09 USD | 17,093,973.35 USD | 1,212,276.73 USD | `+3.42%` | `7B / 4S` |
| `0:00 UTC` | `1230.15` | `1232.52` | `1230.15` | `1240.05` | `1225.05` | 27,822,128.62 USD | 14,746,863.10 USD | 13,075,265.52 USD | 1,671,597.57 USD | `+6.01%` | `5B / 1S` |
| `5:00 UTC` | `1219.95` | `1220.53` | `1219.95` | `1230.45` | `1215.45` | 25,624,282.39 USD | 13,502,208.52 USD | 12,122,073.88 USD | 1,380,134.64 USD | `+5.39%` | `6B / 3S` |
| `0:00 UTC` | `1245.15` | `1232.68` | `1245.15` | `1249.05` | `1206.75` | 51,931,159.61 USD | 26,761,787.01 USD | 25,169,372.61 USD | 1,592,414.40 USD | `+3.07%` | `20B / 9S` |
| `5:00 UTC` | `1239.15` | `1238.23` | `1239.15` | `1245.15` | `1231.05` | 16,842,223.93 USD | 7,201,018.50 USD | 9,641,205.43 USD | -2,440,186.93 USD | `-14.49%` | `1B / 5S` |

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
| `5m` | 389,580.00 USD | -409,810.00 USD | **`DISTRIBUTION`** |
| `15m` | 226,220.00 USD | -5,260,000.00 USD | **`DISTRIBUTION`** |
| `30m` | 1,470,000.00 USD | 11,750,000.00 USD | **`ACCUMULATION`** |
| `1h` | -725,450.00 USD | 13,300,000.00 USD | **`ACCUMULATION`** |
| `2h` | -4,660,000.00 USD | 17,430,000.00 USD | **`ACCUMULATION`** |
| `4h` | -6,050,000.00 USD | 787,050.00 USD | **`DISTRIBUTION`** |
| `6h` | -16,890,000.00 USD | -9,220,000.00 USD | **`DISTRIBUTION`** |
| `8h` | -15,630,000.00 USD | -16,540,000.00 USD | **`DISTRIBUTION`** |
| `12h` | 11,980,000.00 USD | 81,860,000.00 USD | **`ACCUMULATION`** |
| `24h` | 146,170.00 USD | 85,830,000.00 USD | **`ACCUMULATION`** |
| `1w` | 27,110,000.00 USD | 234,360,000.00 USD | **`ACCUMULATION`** |
| `30d` | 57,710,000.00 USD | -545,270,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+389.58K` | 15m=`+226.22K` | 1h=`-725.45K` | 24h=`+146.17K`
* Futures Capital Netflows: 5m=`-409.81K` | 15m=`-5.26M` | 1h=`+13.30M` | 24h=`+85.83M`
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
  * `2026-10-30 05:01:10 IST`: [media.rabobank.com] - (Sentiment: `Neutral`)
  * `2026-10-30 04:15:10 IST`: [economics.td.com] - (Sentiment: `Neutral`)
  * `2026-10-30 05:01:10 IST`: [investinglive.com] - (Sentiment: `Neutral`)
  * `2026-10-30 05:00:10 IST`: [msn.com] - (Sentiment: `Neutral`)
  * `2026-10-30 05:00:10 IST`: [morningstar.com] - (Sentiment: `Neutral`)
  * `2026-10-30 02:02:10 IST`: [sec.gov] - (Sentiment: `Neutral`)
  * `2026-10-30 01:02:10 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 01:02:10 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 01:02:10 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 00:02:10 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 00:02:10 IST`: [@DeItaone] - (Sentiment: `Neutral`)
  * `2026-10-30 00:02:10 IST`: [@mb_ghalibaf] - (Sentiment: `Neutral`)
  * `2026-10-29 23:02:10 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-29 23:02:10 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-29 23:02:10 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)


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
  * Execution Entry: `1216.75` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `1189.10` (Risk Distance: `27.65` pts)
  * +2.5R Take Profit: `1285.89`
  * Mathematical Lot Sizing: **`0.36 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `1257.73` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `1285.38` (Risk Distance: `27.65` pts)
  * +2.5R Take Profit: `1188.59`
  * Mathematical Lot Sizing: **`0.36 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`1240.97`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
