# 🏛️ SOVEREIGN CANDIDATE DOSSIER: ZECUSD
**Canonical Key**: `ZECUSD` | **Broker Instrument**: `ZECUSD.p` | **Asset Class**: `Crypto Altcoin`
**Timestamp**: `2026-10-30 08:42:53 IST` (`2026-10-30 03:12:53 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `1266.59` | **Live Ask Quote**: `1267.90` | **Mid Price**: `1267.24`
- **Spread Points**: `131.00` | **Spread BPS**: `10.34 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `1232.93` | VWAP Z-Score: `+1.50` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `21.42` (Volatility Regime: `HIGH_EXPANSION`)
  * 14-Period RSI: `52.07` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `1285.07` | Lower -3.00σ Band: `1180.79`
  * Upper +2.51σ Band: `1276.56` | Lower -2.51σ Band: `1189.31`
  * Upper +2.01σ Band: `1267.87` | Lower -2.01σ Band: `1198.00`
  * Upper +2.00σ Band: `1267.69` | Lower -2.00σ Band: `1198.17`
  * Upper +1.28σ Band: `1255.18` | Lower -1.28σ Band: `1210.69`
  * Upper +1.00σ Band: `1250.31` | Lower -1.00σ Band: `1215.55`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`1247.97` | EMA-20=`1248.60` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`1264.08` (Slope: `+0.0000`) | EMA-100=`1272.04`
  * Institutional Anchors: EMA-144=`1273.54` | EMA-200=`1274.06` (Slope: `-0.3676`) | EMA-233=`1276.86`
- **Range Boundaries**: 24H High=`1396.49` | 24H Low=`1180.03` | Weekly High=`1396.49` | Weekly Low=`1180.03`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `1262.37` (Distance: `+0.39%`)
  * Point of Control (POC) = `1229.90` (Distance: `+3.04%`)
  * Value Area Low (VAL) = `1222.17` (Distance: `+3.70%`)
  * Auction Positioning: `ABOVE_VALUE (Imbalance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `RANGE_EXPANSION`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`1309.91` | POC=`1246.71` | VAL=`1230.27`
  * Prior Day Extremes: PDH=`1396.49` | PDL=`1206.89` | PDC=`1244.38`
  * Monday Range Blueprint: High=`1267.53` | Mid=`1222.14` | Low=`1176.75`
  * Developing Weekly Value Area: Weekly VAH=`1296.14` | Weekly POC=`1239.01` | Weekly VAL=`1200.92`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`1296.00` | Low=`1180.03`
  * London Session (08:00-16:00 UTC): High=`1272.31` | Low=`1262.18`
  * New York Session (13:00-21:00 UTC): High=`1274.85` | Low=`1259.64`
  * Initial Balance (First Hour): IB High=`1271.05` | IB Low=`1263.44`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `1262.18` - `1272.31`
  * Optimal Trade Entry (OTE 0.705): `1269.78`
  * Structural Invalidation Anchor (0.786): `1277.38`

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
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 08:40:08 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `13` | `0xb83d...6e36` | `SHORT` | 66,283,335.19 USD | `52,385.47` | `1336.45` | `1265.30` | `3818.90` | 3,727,232.21 USD | `+5.62%` | `3X Cross` |
| `22` | `0x5b5d...c060` | `SHORT` | 50,749,533.56 USD | `40,121.38` | `1478.36` | `1265.30` | `5317.90` | 8,564,501.55 USD | `+16.88%` | `3X Cross` |
| `41` | `0x7fda...17d1` | `SHORT` | 30,723,667.07 USD | `24,262.55` | `1261.40` | `1265.30` | `2778.14` | -119,002.29 USD | `-0.39%` | `5X Cross` |
| `80` | `0x60b0...991e` | `LONG` | 21,224,693.13 USD | `16,779.74` | `1179.65` | `1265.30` | `941.78` | 1,430,446.11 USD | `+6.74%` | `10X Cross` |
| `138` | `0xc36a...105b` | `LONG` | 14,575,000.28 USD | `11,510.82` | `1215.14` | `1265.30` | `974.43` | 587,719.26 USD | `+4.03%` | `10X Cross` |
| `152` | `0x9071...5c0b` | `LONG` | 13,333,820.26 USD | `10,517.29` | `1353.83` | `1265.30` | `0.1126` | -904,798.61 USD | `-6.79%` | `1X Cross` |
| `174` | `0x8742...8427` | `LONG` | 11,663,452.88 USD | `9,201.21` | `1286.37` | `1265.30` | `715.30` | -172,717.12 USD | `-1.48%` | `10X Cross` |
| `190` | `0x58b2...11f3` | `LONG` | 10,828,870.97 USD | `8,563.08` | `1246.56` | `1265.30` | `382.38` | 154,453.39 USD | `+1.43%` | `10X Cross` |
| `194` | `0x9ffd...ce40` | `LONG` | 10,666,610.14 USD | `8,434.77` | `1250.92` | `1265.30` | `603.55` | 115,416.30 USD | `+1.08%` | `5X Cross` |
| `195` | `0xad59...ba81` | `SHORT` | 10,660,152.50 USD | `8,425.00` | `330.91` | `1265.30` | `2146.94` | -7,872,194.73 USD | `-73.85%` | `10X Cross` |
| `205` | `0xdd53...2b13` | `SHORT` | 10,375,215.13 USD | `8,195.92` | `741.54` | `1265.30` | `8872.87` | -4,297,618.76 USD | `-41.42%` | `3X Cross` |
| `221` | `0x880a...311c` | `SHORT` | 9,757,201.26 USD | `7,707.11` | `1367.50` | `1265.30` | `2241.84` | 782,282.94 USD | `+8.02%` | `10X Cross` |
| `235` | `0xbf73...5d58` | `LONG` | 9,486,750.00 USD | `7,500.00` | `1248.78` | `1265.30` | `148.93` | 120,904.38 USD | `+1.27%` | `10X Cross` |
| `267` | `0x2b61...2f6c` | `LONG` | 8,617,662.00 USD | `6,807.00` | `1453.56` | `1265.30` | `546.45` | -1,276,689.22 USD | `-14.81%` | `10X Cross` |
| `287` | `0x2ae5...83e7` | `LONG` | 8,139,333.60 USD | `6,436.80` | `1391.82` | `1265.30` | `0.000000` | -819,558.39 USD | `-10.07%` | `1X Cross` |
| `331` | `0x26b6...9a13` | `LONG` | 6,888,882.89 USD | `5,433.73` | `1282.23` | `1265.30` | `226.67` | -78,420.34 USD | `-1.14%` | `10X Cross` |
| `342` | `0x45d2...4029` | `SHORT` | 6,626,790.60 USD | `5,227.00` | `833.44` | `1265.30` | `9339.79` | -2,270,412.63 USD | `-34.26%` | `5X Cross` |
| `359` | `0xea00...a918` | `LONG` | 6,324,500.00 USD | `5,000.00` | `739.16` | `1265.30` | `0.000000` | 2,628,684.89 USD | `+41.56%` | `5X Cross` |
| `370` | `0xdd7a...8830` | `LONG` | 6,151,056.46 USD | `4,860.19` | `897.48` | `1265.30` | `791.70` | 1,789,152.79 USD | `+29.09%` | `10X Cross` |
| `378` | `0xecb6...2b00` | `SHORT` | 6,021,826.33 USD | `4,755.45` | `1278.90` | `1265.30` | `7049.97` | 59,926.44 USD | `+1.00%` | `5X Cross` |
| `435` | `0xa61c...66b9` | `LONG` | 4,921,819.20 USD | `3,888.00` | `1148.34` | `1265.30` | `0.000000` | 457,077.06 USD | `+9.29%` | `10X Cross` |
| `446` | `0x469e...58a5` | `SHORT` | 4,811,458.70 USD | `3,799.92` | `1238.77` | `1265.30` | `2027.98` | -104,212.99 USD | `-2.17%` | `10X Cross` |
| `458` | `0x9aa5...58af` | `SHORT` | 4,709,540.43 USD | `3,720.31` | `1205.51` | `1265.30` | `3739.10` | -224,653.63 USD | `-4.77%` | `10X Cross` |
| `460` | `0x0153...8052` | `SHORT` | 4,688,151.35 USD | `3,698.18` | `1307.82` | `1265.30` | `2504.82` | 148,419.40 USD | `+3.17%` | `1X Isolated` |
| `493` | `0x4cae...7c34` | `LONG` | 4,429,241.66 USD | `3,500.27` | `1143.60` | `1265.30` | `954.28` | 426,319.31 USD | `+9.63%` | `10X Cross` |
| `521` | `0x456f...cdf1` | `LONG` | 4,188,383.41 USD | `3,310.19` | `1267.51` | `1265.30` | `537.89` | -7,321.78 USD | `-0.17%` | `10X Cross` |
| `522` | `0x382b...3e39` | `LONG` | 4,182,217.12 USD | `3,303.75` | `1215.08` | `1265.30` | `0.000000` | 167,897.74 USD | `+4.01%` | `10X Cross` |
| `532` | `0xd21d...90f1` | `LONG` | 4,112,225.00 USD | `3,250.00` | `1253.64` | `1265.30` | `876.03` | 37,883.27 USD | `+0.92%` | `4X Isolated` |
| `549` | `0x1338...c48e` | `LONG` | 3,986,863.44 USD | `3,149.43` | `1018.52` | `1265.30` | `820.32` | 779,117.89 USD | `+19.54%` | `4X Isolated` |
| `561` | `0x325e...9564` | `LONG` | 3,925,777.30 USD | `3,101.91` | `1298.07` | `1265.30` | `205.07` | -100,733.40 USD | `-2.57%` | `10X Cross` |
| `565` | `0xdbe0...d6d5` | `LONG` | 3,910,397.94 USD | `3,085.37` | `422.97` | `1265.30` | `338.64` | 2,605,393.45 USD | `+66.63%` | `3X Isolated` |
| `582` | `0xd4c1...3d1d` | `SHORT` | 3,834,748.95 USD | `3,028.31` | `1296.24` | `1265.30` | `2767.02` | 90,660.61 USD | `+2.36%` | `10X Cross` |
| `591` | `0x9c06...0560` | `SHORT` | 3,781,798.02 USD | `2,989.80` | `786.00` | `1265.30` | `2621.49` | -1,431,803.02 USD | `-37.86%` | `10X Cross` |
| `595` | `0x5323...b23c` | `SHORT` | 3,757,491.99 USD | `2,967.30` | `1260.37` | `1265.30` | `3109.27` | -17,600.72 USD | `-0.47%` | `5X Cross` |
| `597` | `0x27c9...d65d` | `SHORT` | 3,749,740.08 USD | `2,961.88` | `1254.41` | `1265.30` | `1737.82` | -34,324.88 USD | `-0.92%` | `10X Cross` |
| `599` | `0x2e30...4cb5` | `SHORT` | 3,743,267.06 USD | `2,956.30` | `1288.00` | `1265.30` | `2909.17` | 64,435.83 USD | `+1.72%` | `2X Cross` |
| `688` | `0xa183...0482` | `LONG` | 3,212,098.15 USD | `2,534.00` | `530.25` | `1265.30` | `444.56` | 1,868,435.43 USD | `+58.17%` | `5X Isolated` |
| `690` | `0xac48...3201` | `LONG` | 3,202,094.35 USD | `2,531.50` | `1378.58` | `1265.30` | `506.77` | -287,777.93 USD | `-8.99%` | `10X Cross` |
| `698` | `0x0871...e927` | `LONG` | 3,170,500.00 USD | `2,500.00` | `1276.50` | `1265.30` | `0.000000` | -20,750.00 USD | `-0.65%` | `10X Cross` |
| `714` | `0x9b86...6e6e` | `LONG` | 3,116,813.49 USD | `2,463.30` | `637.58` | `1265.30` | `882.49` | 1,546,264.21 USD | `+49.61%` | `3X Cross` |
| `741` | `0x71d0...8c26` | `SHORT` | 3,056,215.05 USD | `2,413.50` | `1262.25` | `1265.30` | `3677.10` | -9,766.10 USD | `-0.32%` | `10X Cross` |
| `772` | `0xb2f7...af9f` | `SHORT` | 2,927,549.92 USD | `2,313.72` | `746.63` | `1265.30` | `4540.94` | -1,200,061.17 USD | `-40.99%` | `10X Cross` |
| `796` | `0x413c...886c` | `LONG` | 2,846,925.00 USD | `2,250.00` | `1237.51` | `1265.30` | `0.000000` | 62,523.97 USD | `+2.20%` | `10X Cross` |
| `811` | `0xf48f...10fe` | `LONG` | 2,807,055.40 USD | `2,218.49` | `1517.87` | `1265.30` | `1016.14` | -560,331.43 USD | `-19.96%` | `3X Cross` |
| `833` | `0x5bc4...3b0c` | `SHORT` | 2,698,795.28 USD | `2,130.74` | `1089.65` | `1265.30` | `3723.82` | -377,037.71 USD | `-13.97%` | `5X Cross` |
| `852` | `0x8de4...b9aa` | `SHORT` | 2,644,645.33 USD | `2,091.29` | `1331.35` | `1265.30` | `1689.94` | 139,594.37 USD | `+5.28%` | `3X Cross` |
| `861` | `0x4fe2...ac59` | `SHORT` | 2,620,328.89 USD | `2,071.57` | `1478.56` | `1265.30` | `1856.37` | 442,617.32 USD | `+16.89%` | `10X Cross` |
| `870` | `0xdf57...93f5` | `LONG` | 2,600,807.10 USD | `2,054.35` | `1227.36` | `1265.30` | `897.27` | 79,385.06 USD | `+3.05%` | `4X Isolated` |
| `876` | `0xbcd4...0dd2` | `LONG` | 2,573,518.98 USD | `2,033.92` | `1228.20` | `1265.30` | `704.50` | 75,468.16 USD | `+2.93%` | `10X Cross` |
| `885` | `0xf29c...9971` | `LONG` | 2,535,199.80 USD | `2,000.00` | `1254.95` | `1265.30` | `0.000000` | 25,302.73 USD | `+1.00%` | `10X Cross` |
| `890` | `0x9a99...d21a` | `LONG` | 2,529,200.00 USD | `2,000.00` | `1278.44` | `1265.30` | `0.000000` | -27,673.67 USD | `-1.09%` | `10X Cross` |
| `908` | `0x77ee...2902` | `SHORT` | 2,463,673.98 USD | `1,946.03` | `759.84` | `1265.30` | `5470.92` | -984,996.47 USD | `-39.98%` | `10X Cross` |
| `917` | `0x3e2f...b269` | `SHORT` | 2,438,850.97 USD | `1,925.51` | `1134.87` | `1265.30` | `2931.87` | -253,652.11 USD | `-10.40%` | `10X Cross` |
| `920` | `0xb122...e4ba` | `LONG` | 2,434,793.36 USD | `1,924.89` | `1255.46` | `1265.30` | `949.59` | 18,166.30 USD | `+0.75%` | `10X Cross` |
| `934` | `0x4f12...618b` | `SHORT` | 2,398,035.69 USD | `1,896.28` | `1608.30` | `1265.30` | `2116.83` | 651,748.70 USD | `+27.18%` | `3X Cross` |
| `971` | `0x866d...d6e1` | `LONG` | 2,281,215.10 USD | `1,802.05` | `674.73` | `1265.30` | `302.90` | 1,065,313.78 USD | `+46.70%` | `10X Cross` |
| `989` | `0x2309...a2d9` | `LONG` | 2,216,318.49 USD | `1,750.37` | `1186.09` | `1265.30` | `816.99` | 140,224.38 USD | `+6.33%` | `8X Cross` |
| `1024` | `0x3205...40bb` | `SHORT` | 2,108,045.73 USD | `1,664.86` | `1245.09` | `1265.30` | `2137.87` | -35,141.13 USD | `-1.67%` | `10X Cross` |
| `1028` | `0x265e...7f70` | `LONG` | 2,088,790.40 USD | `1,651.74` | `1382.98` | `1265.30` | `0.000000` | -195,532.36 USD | `-9.36%` | `3X Cross` |
| `1039` | `0xfe7c...b7ae` | `SHORT` | 2,078,760.92 USD | `1,642.64` | `1346.92` | `1265.30` | `5958.23` | 133,747.70 USD | `+6.43%` | `10X Cross` |
| `1041` | `0x3e47...aaf6` | `LONG` | 2,070,385.08 USD | `1,636.28` | `1278.38` | `1265.30` | `1052.83` | -21,406.70 USD | `-1.03%` | `10X Cross` |
| `1044` | `0x2edd...8179` | `SHORT` | 2,067,851.18 USD | `1,633.89` | `1261.58` | `1265.30` | `2932.36` | -6,569.26 USD | `-0.32%` | `10X Cross` |
| `1061` | `0x7f75...9edf` | `LONG` | 2,031,151.12 USD | `1,605.78` | `1199.97` | `1265.30` | `981.72` | 104,259.23 USD | `+5.13%` | `10X Cross` |
| `1062` | `0x6646...6de5` | `SHORT` | 2,028,306.40 USD | `1,600.00` | `660.64` | `1265.30` | `4145.67` | -971,281.43 USD | `-47.89%` | `10X Cross` |
| `1070` | `0x023a...2355` | `SHORT` | 2,019,143.40 USD | `1,594.90` | `1310.00` | `1265.30` | `4508.44` | 70,168.74 USD | `+3.48%` | `10X Cross` |
| `1098` | `0xab59...59b5` | `LONG` | 1,980,599.40 USD | `1,565.32` | `1342.15` | `1265.30` | `845.50` | -120,295.82 USD | `-6.07%` | `10X Cross` |
| `1151` | `0xcf67...eb24` | `LONG` | 1,897,350.00 USD | `1,500.00` | `887.05` | `1265.30` | `703.26` | 566,778.63 USD | `+29.87%` | `10X Cross` |
| `1164` | `0xb695...a92d` | `LONG` | 1,879,850.80 USD | `1,483.00` | `1249.80` | `1265.30` | `0.000000` | 26,391.94 USD | `+1.40%` | `10X Cross` |
| `1168` | `0x7277...0b98` | `SHORT` | 1,868,274.18 USD | `1,475.73` | `1287.86` | `1265.30` | `2196.95` | 32,257.94 USD | `+1.73%` | `10X Cross` |
| `1237` | `0x2ab7...c2f8` | `LONG` | 1,770,944.90 USD | `1,400.51` | `813.26` | `1265.30` | `793.48` | 631,963.21 USD | `+35.69%` | `3X Cross` |
| `1253` | `0x11be...8b1d` | `LONG` | 1,740,837.70 USD | `1,375.83` | `1206.55` | `1265.30` | `1134.54` | 80,829.74 USD | `+4.64%` | `10X Isolated` |
| `1289` | `0xfc27...9d9d` | `SHORT` | 1,672,773.35 USD | `1,319.43` | `1298.53` | `1265.30` | `15588.15` | 40,543.42 USD | `+2.42%` | `10X Cross` |
| `1323` | `0x039c...0ebd` | `SHORT` | 1,619,318.29 USD | `1,279.79` | `1239.81` | `1265.30` | `3681.68` | -32,616.46 USD | `-2.01%` | `10X Cross` |
| `1345` | `0xe065...0f85` | `SHORT` | 1,596,696.61 USD | `1,262.61` | `1087.02` | `1265.30` | `1617.19` | -224,220.48 USD | `-14.04%` | `10X Cross` |
| `1418` | `0x5975...9abd` | `LONG` | 1,518,360.00 USD | `1,200.00` | `1179.54` | `1265.30` | `580.99` | 102,917.21 USD | `+6.78%` | `5X Cross` |
| `1421` | `0x266b...efcb` | `LONG` | 1,517,400.00 USD | `1,200.00` | `893.76` | `1265.30` | `425.34` | 444,890.30 USD | `+29.32%` | `10X Cross` |
| `1436` | `0x2847...d47b` | `LONG` | 1,502,055.07 USD | `1,186.27` | `1232.07` | `1265.30` | `0.000000` | 40,486.58 USD | `+2.70%` | `5X Cross` |
| `1462` | `0x69cc...14fd` | `SHORT` | 1,470,281.76 USD | `1,161.36` | `675.33` | `1265.30` | `8159.83` | -685,976.23 USD | `-46.66%` | `10X Cross` |
| `1478` | `0x3fc5...c0c1` | `SHORT` | 1,453,121.13 USD | `1,148.44` | `1264.34` | `1265.30` | `2889.12` | -1,107.36 USD | `-0.08%` | `10X Cross` |
| `1482` | `0x38f9...cb04` | `SHORT` | 1,444,417.22 USD | `1,141.02` | `1243.50` | `1265.30` | `2010.83` | -25,563.37 USD | `-1.77%` | `10X Cross` |
| `1503` | `0xe35c...a1d3` | `LONG` | 1,426,407.14 USD | `1,127.06` | `1318.20` | `1265.30` | `694.46` | -59,288.21 USD | `-4.16%` | `2X Isolated` |
| `1519` | `0x5f94...4b96` | `LONG` | 1,411,151.13 USD | `1,115.27` | `538.00` | `1265.30` | `0.000000` | 811,133.49 USD | `+57.48%` | `10X Cross` |
| `1540` | `0x71df...a23d` | `SHORT` | 1,390,422.48 USD | `1,098.28` | `513.50` | `1265.30` | `2558.39` | -826,452.29 USD | `-59.44%` | `2X Cross` |
| `1563` | `0xbfc7...80b4` | `SHORT` | 1,361,272.50 USD | `1,075.00` | `558.03` | `1265.30` | `2993.69` | -761,393.77 USD | `-55.93%` | `10X Cross` |
| `1598` | `0x51f6...2b39` | `SHORT` | 1,312,826.91 USD | `1,037.07` | `1299.77` | `1265.30` | `2484.57` | 35,123.91 USD | `+2.68%` | `10X Cross` |
| `1631` | `0x123d...3bff` | `SHORT` | 1,278,103.28 USD | `1,009.64` | `491.08` | `1265.30` | `4426.54` | -782,285.37 USD | `-61.21%` | `10X Cross` |
| `1644` | `0x668c...ea2e` | `SHORT` | 1,266,200.00 USD | `1,000.00` | `1406.98` | `1265.30` | `4185.64` | 140,781.99 USD | `+11.12%` | `10X Cross` |
| `1648` | `0xe282...df29` | `LONG` | 1,265,600.00 USD | `1,000.00` | `420.99` | `1265.30` | `837.49` | 844,613.14 USD | `+66.74%` | `10X Cross` |
| `1671` | `0x17f0...094f` | `LONG` | 1,246,025.37 USD | `984.30` | `1287.23` | `1265.30` | `536.89` | -20,994.79 USD | `-1.68%` | `5X Cross` |
| `1745` | `0x757d...94ba` | `LONG` | 1,171,605.00 USD | `925.00` | `1558.31` | `1265.30` | `0.000000` | -269,835.59 USD | `-23.03%` | `10X Cross` |
| `1749` | `0xaa82...9556` | `LONG` | 1,169,948.58 USD | `924.13` | `1254.72` | `1265.30` | `184.62` | 10,421.90 USD | `+0.89%` | `10X Cross` |
| `1790` | `0xb911...5525` | `LONG` | 1,138,770.00 USD | `900.00` | `1294.82` | `1265.30` | `1035.32` | -26,567.82 USD | `-2.33%` | `10X Cross` |
| `1838` | `0xcf0a...856f` | `LONG` | 1,102,440.32 USD | `871.15` | `1292.19` | `1265.30` | `1008.26` | -23,254.52 USD | `-2.11%` | `4X Cross` |
| `1842` | `0xef96...9383` | `SHORT` | 1,099,680.25 USD | `868.42` | `1259.08` | `1265.30` | `5473.18` | -6,268.45 USD | `-0.57%` | `10X Cross` |
| `1846` | `0x2577...4897` | `SHORT` | 1,095,982.65 USD | `865.50` | `1262.85` | `1265.30` | `4966.90` | -2,981.88 USD | `-0.27%` | `10X Cross` |
| `1866` | `0xdf95...7d72` | `SHORT` | 1,080,495.80 USD | `853.27` | `1074.39` | `1265.30` | `45969.51` | -163,748.36 USD | `-15.15%` | `10X Cross` |
| `1905` | `0x601c...4f54` | `SHORT` | 1,043,633.28 USD | `824.42` | `615.11` | `1265.30` | `3148.83` | -536,520.53 USD | `-51.41%` | `5X Cross` |
| `1916` | `0xae55...2236` | `LONG` | 1,033,690.81 USD | `817.47` | `1467.80` | `1265.30` | `0.000000` | -166,190.40 USD | `-16.08%` | `10X Cross` |
| `1950` | `0x0f02...5384` | `LONG` | 1,013,547.25 USD | `800.78` | `1290.36` | `1265.30` | `309.83` | -19,746.82 USD | `-1.95%` | `3X Cross` |
| `1955` | `0x11ee...1d1d` | `SHORT` | 1,011,920.00 USD | `800.00` | `1269.65` | `1265.30` | `1614.81` | 3,803.01 USD | `+0.38%` | `5X Cross` |
| `1958` | `0x9b0f...db40` | `LONG` | 1,011,600.00 USD | `800.00` | `1268.86` | `1265.30` | `800.68` | -3,489.76 USD | `-0.34%` | `10X Cross` |
| `1969` | `0xabdb...84ac` | `LONG` | 1,006,478.29 USD | `793.69` | `711.79` | `1265.30` | `664.46` | 441,537.93 USD | `+43.87%` | `3X Cross` |
| `1971` | `0x6e8f...4364` | `LONG` | 1,004,443.44 USD | `793.65` | `1260.00` | `1265.30` | `1016.84` | 4,444.44 USD | `+0.44%` | `10X Cross` |
| `1978` | `0xdf83...3cff` | `SHORT` | 1,001,801.28 USD | `791.75` | `1254.45` | `1265.30` | `1892.14` | -8,593.72 USD | `-0.86%` | `10X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| Intel | Baseline | - | - | - | Neutral | - | No anomalous telegram alerts in current window | - |


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
| `5m` | `BALANCED` | 0.00 USD | 1,750.00 USD | 1,750.00 USD | 1,750.00 USD | `1` | `2026-10-30 03:05:00 UTC - 2026-10-30 03:10:00 UTC` |
| `15m` | `BALANCED` | 0.00 USD | 1,750.00 USD | 1,750.00 USD | 1,750.00 USD | `1` | `2026-10-30 03:00:00 UTC - 2026-10-30 03:15:00 UTC` |
| `1h` | `BALANCED` | 0.00 USD | 1,750.00 USD | 1,750.00 USD | 1,750.00 USD | `1` | `2026-10-30 03:00:00 UTC - 2026-10-30 04:00:00 UTC` |
| `4h` | `BALANCED` | 0.00 USD | 1,750.00 USD | 1,750.00 USD | 1,750.00 USD | `1` | `2026-10-30 00:00:00 UTC - 2026-10-30 04:00:00 UTC` |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `0 USD` | Total OI Tokens: `-`
  * 1h OI Change: `0.00%` | 4h OI Change: `0.00%` | 24h OI Change: `0.00%`
  * Exchange Breakdown: Binance=`-` | Bybit=`-` | OKX=`-` | Hyperliquid=`-`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `85.55K` | Last 24h: `133.88K` | Last 3d: `245.74K` | Last 7d: `771.70K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0100%` | **USDT OKX** | `0.0100%` |
| **USDT Bybit** | `0.0100%` | **USDT KuCoin** | `0.0100%` |
| **USDT MEXC** | `0.0100%` | **USDT BingX** | `0.0100%` |
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
| `5:00 UTC` | `1232.55` | `1227.83` | `1232.55` | `1237.35` | `1215.45` | 35,400,223.44 USD | 18,306,250.09 USD | 17,093,973.35 USD | 1,212,276.73 USD | `+3.42%` | `7B / 4S` |
| `0:00 UTC` | `1230.15` | `1232.52` | `1230.15` | `1240.05` | `1225.05` | 27,822,128.62 USD | 14,746,863.10 USD | 13,075,265.52 USD | 1,671,597.57 USD | `+6.01%` | `5B / 1S` |
| `5:00 UTC` | `1219.95` | `1220.53` | `1219.95` | `1230.45` | `1215.45` | 25,624,282.39 USD | 13,502,208.52 USD | 12,122,073.88 USD | 1,380,134.64 USD | `+5.39%` | `6B / 3S` |
| `0:00 UTC` | `1245.15` | `1232.68` | `1245.15` | `1249.05` | `1206.75` | 51,931,159.61 USD | 26,761,787.01 USD | 25,169,372.61 USD | 1,592,414.40 USD | `+3.07%` | `20B / 9S` |
| `5:00 UTC` | `1236.45` | `1237.15` | `1236.45` | `1245.15` | `1230.45` | 21,904,768.45 USD | 9,625,705.12 USD | 12,279,063.33 USD | -2,653,358.20 USD | `-12.11%` | `1B / 0S` |
| `0:00 UTC` | `1228.65` | `1236.25` | `1228.65` | `1253.25` | `1219.35` | 45,146,863.08 USD | 23,450,812.50 USD | 21,696,050.59 USD | 1,754,761.91 USD | `+3.89%` | `18B / 9S` |
| `5:00 UTC` | `1254.75` | `1256.85` | `1254.75` | `1263.45` | `1247.85` | 37,496,922.68 USD | 20,689,312.95 USD | 16,807,609.72 USD | 3,881,703.23 USD | `+10.35%` | `5B / 3S` |
| `0:00 UTC` | `1263.45` | `1263.47` | `1263.45` | `1267.65` | `1258.35` | 21,490,941.27 USD | 11,626,504.00 USD | 9,864,437.27 USD | 1,762,066.74 USD | `+8.20%` | `2B / 3S` |
| `5:00 UTC` | `1257.45` | `1259.53` | `1257.45` | `1270.05` | `1249.95` | 34,915,865.69 USD | 14,880,758.20 USD | 20,035,107.50 USD | -5,154,349.30 USD | `-14.76%` | `1B / 7S` |
| `0:00 UTC` | `1264.05` | `1261.99` | `1264.05` | `1264.65` | `1257.15` | 6,331,740.50 USD | 3,201,914.40 USD | 3,129,826.10 USD | 72,088.30 USD | `+1.14%` | `1B / 0S` |

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
| `5m` | 229,930.00 USD | -498,310.00 USD | **`DISTRIBUTION`** |
| `15m` | -984,520.00 USD | -7,480,000.00 USD | **`DISTRIBUTION`** |
| `30m` | 831,820.00 USD | -6,840,000.00 USD | **`DISTRIBUTION`** |
| `1h` | 3,900,000.00 USD | 14,050,000.00 USD | **`ACCUMULATION`** |
| `2h` | 7,040,000.00 USD | 17,720,000.00 USD | **`ACCUMULATION`** |
| `4h` | 2,370,000.00 USD | 21,750,000.00 USD | **`ACCUMULATION`** |
| `6h` | 5,690,000.00 USD | 23,630,000.00 USD | **`ACCUMULATION`** |
| `8h` | -11,530,000.00 USD | -8,070,000.00 USD | **`DISTRIBUTION`** |
| `12h` | 8,590,000.00 USD | 66,370,000.00 USD | **`ACCUMULATION`** |
| `24h` | 13,390,000.00 USD | 110,010,000.00 USD | **`ACCUMULATION`** |
| `1w` | 33,720,000.00 USD | 233,160,000.00 USD | **`ACCUMULATION`** |
| `30d` | 60,460,000.00 USD | -517,670,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+229.93K` | 15m=`-984.52K` | 1h=`+3.90M` | 24h=`+13.39M`
* Futures Capital Netflows: 5m=`-498.31K` | 15m=`-7.48M` | 1h=`+14.05M` | 24h=`+110.01M`
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
  * `2026-10-30 08:34:38 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 08:33:38 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 08:00:38 IST`: [financemagnates.com] - (Sentiment: `Neutral`)
  * `2026-10-30 08:35:38 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-30 08:34:38 IST`: [kathleenhays.substack.com] - (Sentiment: `Neutral`)
  * `2026-10-30 08:34:38 IST`: [rba.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 08:34:38 IST`: [abs.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 08:34:38 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 05:36:38 IST`: [@NodeWire] - (Sentiment: `Neutral`)
  * `2026-10-30 05:36:38 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 05:36:38 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 05:36:38 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-30 05:36:38 IST`: [media.rabobank.com] - (Sentiment: `Neutral`)
  * `2026-10-30 04:36:38 IST`: [economics.td.com] - (Sentiment: `Neutral`)
  * `2026-10-30 03:36:38 IST`: [investinglive.com] - (Sentiment: `Neutral`)


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
  * Execution Entry: `1222.17` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `1194.50` (Risk Distance: `27.67` pts)
  * +2.5R Take Profit: `1291.34`
  * Mathematical Lot Sizing: **`0.36 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `1262.37` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `1290.04` (Risk Distance: `27.67` pts)
  * +2.5R Take Profit: `1193.20`
  * Mathematical Lot Sizing: **`0.36 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`1277.38`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
