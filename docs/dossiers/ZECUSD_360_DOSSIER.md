# 🏛️ SOVEREIGN CANDIDATE DOSSIER: ZECUSD
**Canonical Key**: `ZECUSD` | **Broker Instrument**: `ZECUSD.p` | **Asset Class**: `Crypto Altcoin`
**Timestamp**: `2026-10-30 14:17:33 IST` (`2026-10-30 08:47:33 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `1248.66` | **Live Ask Quote**: `1249.64` | **Mid Price**: `1249.15`
- **Spread Points**: `98.00` | **Spread BPS**: `7.85 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `1254.44` | VWAP Z-Score: `-0.36` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `13.51` (Volatility Regime: `HIGH_EXPANSION`)
  * 14-Period RSI: `41.16` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `1321.54` | Lower -3.00σ Band: `1187.35`
  * Upper +2.51σ Band: `1310.58` | Lower -2.51σ Band: `1198.31`
  * Upper +2.01σ Band: `1299.40` | Lower -2.01σ Band: `1209.49`
  * Upper +2.00σ Band: `1299.17` | Lower -2.00σ Band: `1209.71`
  * Upper +1.28σ Band: `1283.07` | Lower -1.28σ Band: `1225.82`
  * Upper +1.00σ Band: `1276.81` | Lower -1.00σ Band: `1232.08`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`1256.52` | EMA-20=`1261.23` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`1265.45` (Slope: `+0.0000`) | EMA-100=`1270.48`
  * Institutional Anchors: EMA-144=`1272.97` | EMA-200=`1276.33` (Slope: `-0.1430`) | EMA-233=`1277.69`
- **Range Boundaries**: 24H High=`1396.49` | 24H Low=`1180.03` | Weekly High=`1396.49` | Weekly Low=`1180.03`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `1284.79` (Distance: `-2.72%`)
  * Point of Control (POC) = `1275.51` (Distance: `-2.01%`)
  * Value Area Low (VAL) = `1240.72` (Distance: `+0.74%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`1309.91` | POC=`1246.71` | VAL=`1230.27`
  * Prior Day Extremes: PDH=`1396.49` | PDL=`1206.89` | PDC=`1244.38`
  * Monday Range Blueprint: High=`1267.53` | Mid=`1222.14` | Low=`1176.75`
  * Developing Weekly Value Area: Weekly VAH=`1294.68` | Weekly POC=`1239.01` | Weekly VAL=`1200.92`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`1296.00` | Low=`1180.03`
  * London Session (08:00-16:00 UTC): High=`1283.82` | Low=`1239.96`
  * New York Session (13:00-21:00 UTC): High=`1256.64` | Low=`1241.66`
  * Initial Balance (First Hour): IB High=`1283.82` | IB Low=`1264.92`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `1244.15` - `1254.15`
  * Optimal Trade Entry (OTE 0.705): `1251.65`
  * Structural Invalidation Anchor (0.786): `1259.14`

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
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 14:11:10 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `12` | `0xb83d...6e36` | `SHORT` | 65,528,984.42 USD | `52,385.47` | `1336.45` | `1251.50` | `3593.79` | 4,481,582.98 USD | `+6.84%` | `3X Cross` |
| `21` | `0x5b5d...c060` | `SHORT` | 50,187,834.24 USD | `40,121.38` | `1478.36` | `1251.50` | `5004.10` | 9,126,200.87 USD | `+18.18%` | `3X Cross` |
| `37` | `0x7fda...17d1` | `SHORT` | 33,230,221.05 USD | `26,565.05` | `1262.62` | `1251.50` | `2606.23` | 311,238.86 USD | `+0.94%` | `5X Cross` |
| `82` | `0x60b0...991e` | `LONG` | 20,964,607.16 USD | `16,779.74` | `1179.65` | `1251.50` | `917.80` | 1,170,360.14 USD | `+5.58%` | `10X Cross` |
| `140` | `0xc36a...105b` | `LONG` | 14,389,676.08 USD | `11,510.82` | `1215.14` | `1251.50` | `965.25` | 402,395.05 USD | `+2.80%` | `10X Cross` |
| `179` | `0x8742...8427` | `LONG` | 11,516,234.44 USD | `9,201.21` | `1286.37` | `1251.50` | `707.20` | -319,935.56 USD | `-2.78%` | `10X Cross` |
| `196` | `0x58b2...11f3` | `LONG` | 10,699,568.46 USD | `8,563.08` | `1246.56` | `1251.50` | `383.60` | 25,150.89 USD | `+0.24%` | `10X Cross` |
| `198` | `0x9071...5c0b` | `LONG` | 10,660,240.16 USD | `8,517.29` | `1353.83` | `1251.50` | `0.000000` | -870,719.44 USD | `-8.17%` | `2X Cross` |
| `199` | `0x9ffd...ce40` | `LONG` | 10,627,112.26 USD | `8,502.37` | `1252.23` | `1251.50` | `604.64` | -19,810.54 USD | `-0.19%` | `5X Cross` |
| `204` | `0xad59...ba81` | `SHORT` | 10,538,832.50 USD | `8,425.00` | `330.91` | `1251.50` | `2146.74` | -7,750,874.73 USD | `-73.55%` | `10X Cross` |
| `208` | `0xdd53...2b13` | `SHORT` | 10,252,276.33 USD | `8,195.92` | `741.54` | `1251.50` | `8457.96` | -4,174,679.96 USD | `-40.72%` | `3X Cross` |
| `228` | `0x880a...311c` | `SHORT` | 9,640,823.90 USD | `7,707.11` | `1367.50` | `1251.50` | `2229.42` | 898,660.30 USD | `+9.32%` | `10X Cross` |
| `237` | `0xbf73...5d58` | `LONG` | 9,374,250.00 USD | `7,500.00` | `1248.78` | `1251.50` | `139.19` | 8,404.38 USD | `+0.09%` | `10X Cross` |
| `276` | `0x2b61...2f6c` | `LONG` | 8,509,430.70 USD | `6,807.00` | `1453.56` | `1251.50` | `563.64` | -1,384,920.52 USD | `-16.28%` | `10X Cross` |
| `294` | `0x2ae5...83e7` | `LONG` | 8,056,298.88 USD | `6,436.80` | `1391.82` | `1251.50` | `0.000000` | -902,593.11 USD | `-11.20%` | `1X Cross` |
| `329` | `0xecb6...2b00` | `SHORT` | 7,053,049.54 USD | `5,638.38` | `1278.25` | `1251.50` | `6522.30` | 154,184.82 USD | `+2.19%` | `5X Cross` |
| `338` | `0x26b6...9a13` | `LONG` | 6,800,856.47 USD | `5,433.73` | `1282.23` | `1251.50` | `225.70` | -166,446.77 USD | `-2.45%` | `10X Cross` |
| `358` | `0x45d2...4029` | `SHORT` | 6,542,113.20 USD | `5,227.00` | `833.44` | `1251.50` | `9063.74` | -2,185,735.23 USD | `-33.41%` | `5X Cross` |
| `372` | `0xea00...a918` | `LONG` | 6,247,000.00 USD | `5,000.00` | `739.16` | `1251.50` | `0.000000` | 2,551,184.89 USD | `+40.84%` | `5X Cross` |
| `384` | `0xdd7a...8830` | `LONG` | 6,073,293.42 USD | `4,860.19` | `897.48` | `1251.50` | `786.61` | 1,711,389.75 USD | `+28.18%` | `10X Cross` |
| `426` | `0x469e...58a5` | `SHORT` | 5,204,816.35 USD | `4,163.52` | `1242.31` | `1251.50` | `1964.10` | -32,431.70 USD | `-0.62%` | `10X Cross` |
| `444` | `0x4cae...7c34` | `LONG` | 5,003,237.73 USD | `4,002.27` | `1169.72` | `1251.50` | `973.70` | 321,688.38 USD | `+6.43%` | `10X Cross` |
| `448` | `0xd4c1...3d1d` | `SHORT` | 4,913,109.89 USD | `3,927.66` | `1291.69` | `1251.50` | `2349.98` | 160,204.01 USD | `+3.26%` | `10X Cross` |
| `457` | `0xa61c...66b9` | `LONG` | 4,858,444.80 USD | `3,888.00` | `1148.34` | `1251.50` | `0.000000` | 393,702.66 USD | `+8.10%` | `10X Cross` |
| `475` | `0x382b...3e39` | `LONG` | 4,683,294.55 USD | `3,743.94` | `1219.28` | `1251.50` | `0.000000` | 118,381.89 USD | `+2.53%` | `10X Cross` |
| `482` | `0x9aa5...58af` | `SHORT` | 4,656,340.00 USD | `3,720.31` | `1205.51` | `1251.50` | `3704.91` | -171,453.20 USD | `-3.68%` | `10X Cross` |
| `486` | `0x0153...8052` | `SHORT` | 4,627,902.45 USD | `3,698.18` | `1307.82` | `1251.50` | `2504.91` | 208,668.30 USD | `+4.51%` | `1X Isolated` |
| `521` | `0xb122...e4ba` | `LONG` | 4,371,338.26 USD | `3,498.47` | `1265.25` | `1251.50` | `1109.68` | -55,113.26 USD | `-1.26%` | `10X Cross` |
| `557` | `0xd21d...90f1` | `LONG` | 4,060,875.00 USD | `3,250.00` | `1253.64` | `1251.50` | `876.13` | -13,466.73 USD | `-0.33%` | `4X Isolated` |
| `561` | `0x456f...cdf1` | `LONG` | 4,042,282.44 USD | `3,235.12` | `1267.65` | `1251.50` | `518.49` | -58,705.05 USD | `-1.45%` | `10X Cross` |
| `578` | `0x1338...c48e` | `LONG` | 3,937,102.44 USD | `3,149.43` | `1018.52` | `1251.50` | `820.43` | 729,356.90 USD | `+18.53%` | `4X Isolated` |
| `592` | `0x2e30...4cb5` | `SHORT` | 3,884,515.82 USD | `3,103.64` | `1283.50` | `1251.50` | `2824.89` | 99,008.56 USD | `+2.55%` | `2X Cross` |
| `597` | `0xdbe0...d6d5` | `LONG` | 3,861,032.02 USD | `3,085.37` | `422.97` | `1251.50` | `338.74` | 2,556,027.53 USD | `+66.20%` | `3X Isolated` |
| `613` | `0x325e...9564` | `LONG` | 3,751,137.50 USD | `3,000.91` | `1298.07` | `1251.50` | `144.28` | -144,267.66 USD | `-3.85%` | `10X Cross` |
| `617` | `0x9c06...0560` | `SHORT` | 3,736,951.02 USD | `2,989.80` | `786.00` | `1251.50` | `2572.72` | -1,386,956.02 USD | `-37.11%` | `10X Cross` |
| `622` | `0x27c9...d65d` | `SHORT` | 3,678,165.65 USD | `2,943.71` | `1254.41` | `1251.50` | `1730.76` | 14,456.91 USD | `+0.39%` | `10X Cross` |
| `720` | `0xa183...0482` | `LONG` | 3,170,287.40 USD | `2,534.00` | `530.25` | `1251.50` | `444.67` | 1,826,624.68 USD | `+57.62%` | `5X Isolated` |
| `721` | `0xac48...3201` | `LONG` | 3,163,109.25 USD | `2,531.50` | `1378.58` | `1251.50` | `524.04` | -326,763.03 USD | `-10.33%` | `10X Cross` |
| `731` | `0x0871...e927` | `LONG` | 3,125,250.00 USD | `2,500.00` | `1276.50` | `1251.50` | `0.000000` | -66,000.00 USD | `-2.11%` | `10X Cross` |
| `748` | `0x9b86...6e6e` | `LONG` | 3,077,893.35 USD | `2,463.30` | `637.58` | `1251.50` | `882.60` | 1,507,344.07 USD | `+48.97%` | `3X Cross` |
| `796` | `0xb2f7...af9f` | `SHORT` | 2,890,993.14 USD | `2,313.72` | `746.63` | `1251.50` | `4493.89` | -1,163,504.39 USD | `-40.25%` | `10X Cross` |
| `827` | `0xf48f...10fe` | `LONG` | 2,772,003.25 USD | `2,218.49` | `1517.87` | `1251.50` | `978.69` | -595,383.57 USD | `-21.48%` | `3X Cross` |
| `864` | `0x5bc4...3b0c` | `SHORT` | 2,665,768.81 USD | `2,130.74` | `1089.65` | `1251.50` | `3678.43` | -344,011.24 USD | `-12.90%` | `5X Cross` |
| `867` | `0x71d0...8c26` | `SHORT` | 2,657,224.33 USD | `2,124.25` | `1266.91` | `1251.50` | `3813.65` | 34,000.49 USD | `+1.28%` | `10X Cross` |
| `876` | `0x8de4...b9aa` | `SHORT` | 2,613,903.37 USD | `2,091.29` | `1331.35` | `1251.50` | `1690.04` | 170,336.33 USD | `+6.52%` | `3X Cross` |
| `882` | `0x4fe2...ac59` | `SHORT` | 2,588,426.71 USD | `2,071.57` | `1478.56` | `1251.50` | `1848.78` | 474,519.50 USD | `+18.33%` | `10X Cross` |
| `886` | `0xdf57...93f5` | `LONG` | 2,569,786.42 USD | `2,054.35` | `1227.36` | `1251.50` | `897.38` | 48,364.37 USD | `+1.88%` | `4X Isolated` |
| `894` | `0xbcd4...0dd2` | `LONG` | 2,544,230.53 USD | `2,033.92` | `1228.20` | `1251.50` | `739.29` | 46,179.71 USD | `+1.82%` | `10X Cross` |
| `904` | `0xf29c...9971` | `LONG` | 2,502,200.00 USD | `2,000.00` | `1254.95` | `1251.50` | `0.000000` | -7,697.07 USD | `-0.31%` | `10X Cross` |
| `907` | `0x9a99...d21a` | `LONG` | 2,499,000.00 USD | `2,000.00` | `1278.44` | `1251.50` | `0.000000` | -57,873.67 USD | `-2.32%` | `10X Cross` |
| `928` | `0x77ee...2902` | `SHORT` | 2,436,234.96 USD | `1,946.03` | `759.84` | `1251.50` | `5651.06` | -957,557.45 USD | `-39.30%` | `10X Cross` |
| `934` | `0x3e2f...b269` | `SHORT` | 2,409,005.56 USD | `1,925.51` | `1134.87` | `1251.50` | `2977.31` | -223,806.70 USD | `-9.29%` | `10X Cross` |
| `950` | `0x4f12...618b` | `SHORT` | 2,370,160.37 USD | `1,896.28` | `1608.30` | `1251.50` | `2116.93` | 679,624.02 USD | `+28.67%` | `3X Cross` |
| `993` | `0x866d...d6e1` | `LONG` | 2,252,742.71 USD | `1,802.05` | `674.73` | `1251.50` | `155.50` | 1,036,841.39 USD | `+46.03%` | `10X Cross` |
| `1022` | `0x2309...a2d9` | `LONG` | 2,189,712.87 USD | `1,750.37` | `1186.09` | `1251.50` | `808.25` | 113,618.76 USD | `+5.19%` | `8X Cross` |
| `1066` | `0x265e...7f70` | `LONG` | 2,064,509.83 USD | `1,651.74` | `1382.98` | `1251.50` | `0.000000` | -219,812.93 USD | `-10.65%` | `3X Cross` |
| `1070` | `0xfe7c...b7ae` | `SHORT` | 2,055,106.90 USD | `1,642.64` | `1346.92` | `1251.50` | `5698.74` | 157,401.72 USD | `+7.66%` | `10X Cross` |
| `1075` | `0x3e47...aaf6` | `LONG` | 2,044,531.86 USD | `1,636.28` | `1278.38` | `1251.50` | `1051.31` | -47,259.93 USD | `-2.31%` | `10X Cross` |
| `1076` | `0x2edd...8179` | `SHORT` | 2,044,510.09 USD | `1,634.17` | `1261.56` | `1251.50` | `2880.14` | 17,093.38 USD | `+0.84%` | `10X Cross` |
| `1096` | `0x7f75...9edf` | `LONG` | 2,016,663.45 USD | `1,612.17` | `1200.26` | `1251.50` | `985.83` | 81,642.37 USD | `+4.05%` | `10X Cross` |
| `1105` | `0x6646...6de5` | `SHORT` | 1,998,880.00 USD | `1,600.00` | `660.64` | `1251.50` | `4187.97` | -941,855.03 USD | `-47.12%` | `10X Cross` |
| `1109` | `0x023a...2355` | `SHORT` | 1,990,569.68 USD | `1,591.31` | `1310.00` | `1251.50` | `4433.58` | 94,039.57 USD | `+4.72%` | `10X Cross` |
| `1120` | `0xfc27...9d9d` | `SHORT` | 1,974,470.60 USD | `1,578.44` | `1295.79` | `1251.50` | `12723.42` | 70,853.61 USD | `+3.59%` | `10X Cross` |
| `1131` | `0xab59...59b5` | `LONG` | 1,955,867.34 USD | `1,565.32` | `1342.15` | `1251.50` | `835.77` | -145,027.88 USD | `-7.42%` | `10X Cross` |
| `1175` | `0x039c...0ebd` | `SHORT` | 1,901,128.94 USD | `1,521.39` | `1245.17` | `1251.50` | `3736.90` | -6,735.08 USD | `-0.35%` | `10X Cross` |
| `1184` | `0xcf67...eb24` | `LONG` | 1,874,250.00 USD | `1,500.00` | `887.05` | `1251.50` | `621.92` | 543,678.63 USD | `+29.01%` | `10X Cross` |
| `1197` | `0xb695...a92d` | `LONG` | 1,855,084.70 USD | `1,483.00` | `1249.80` | `1251.50` | `0.000000` | 1,625.85 USD | `+0.09%` | `10X Cross` |
| `1202` | `0x7277...0b98` | `SHORT` | 1,845,990.66 USD | `1,475.73` | `1287.86` | `1251.50` | `2189.28` | 54,541.47 USD | `+2.95%` | `10X Cross` |
| `1258` | `0x3205...40bb` | `SHORT` | 1,777,676.27 USD | `1,420.55` | `1257.45` | `1251.50` | `2291.84` | 8,595.26 USD | `+0.48%` | `10X Cross` |
| `1267` | `0x2ab7...c2f8` | `LONG` | 1,752,878.32 USD | `1,400.51` | `813.26` | `1251.50` | `792.58` | 613,896.63 USD | `+35.02%` | `3X Cross` |
| `1287` | `0x11be...8b1d` | `LONG` | 1,719,099.58 USD | `1,375.83` | `1206.55` | `1251.50` | `1134.65` | 59,091.63 USD | `+3.44%` | `10X Isolated` |
| `1367` | `0xe065...0f85` | `SHORT` | 1,577,631.20 USD | `1,262.61` | `1087.02` | `1251.50` | `1550.53` | -205,155.07 USD | `-13.00%` | `10X Cross` |
| `1380` | `0x413c...886c` | `LONG` | 1,563,500.00 USD | `1,250.00` | `1237.51` | `1251.50` | `0.000000` | 16,610.54 USD | `+1.06%` | `10X Cross` |
| `1415` | `0xdf83...3cff` | `SHORT` | 1,545,111.68 USD | `1,235.20` | `1260.67` | `1251.50` | `1846.62` | 12,072.11 USD | `+0.78%` | `10X Cross` |
| `1446` | `0x2847...d47b` | `LONG` | 1,515,728.04 USD | `1,211.71` | `1232.45` | `1251.50` | `0.000000` | 22,360.44 USD | `+1.48%` | `5X Cross` |
| `1459` | `0x266b...efcb` | `LONG` | 1,501,680.00 USD | `1,200.00` | `893.76` | `1251.50` | `413.24` | 429,170.30 USD | `+28.58%` | `10X Cross` |
| `1463` | `0x5975...9abd` | `LONG` | 1,499,400.00 USD | `1,200.00` | `1179.54` | `1251.50` | `535.28` | 83,957.21 USD | `+5.60%` | `5X Cross` |
| `1494` | `0x69cc...14fd` | `SHORT` | 1,452,745.22 USD | `1,161.36` | `675.33` | `1251.50` | `8088.13` | -668,439.70 USD | `-46.01%` | `10X Cross` |
| `1506` | `0x3fc5...c0c1` | `SHORT` | 1,434,975.78 USD | `1,148.44` | `1264.34` | `1251.50` | `2774.28` | 17,038.00 USD | `+1.19%` | `10X Cross` |
| `1553` | `0x5f94...4b96` | `LONG` | 1,395,091.24 USD | `1,115.27` | `538.00` | `1251.50` | `0.000000` | 795,073.61 USD | `+56.99%` | `10X Cross` |
| `1555` | `0xe35c...a1d3` | `LONG` | 1,390,200.22 USD | `1,111.36` | `1311.66` | `1251.50` | `690.94` | -67,523.92 USD | `-4.86%` | `2X Isolated` |
| `1580` | `0x71df...a23d` | `SHORT` | 1,372,959.83 USD | `1,098.28` | `513.50` | `1251.50` | `2560.59` | -808,989.64 USD | `-58.92%` | `2X Cross` |
| `1597` | `0x5323...b23c` | `SHORT` | 1,347,169.26 USD | `1,076.96` | `1262.16` | `1251.50` | `6450.38` | 12,128.95 USD | `+0.90%` | `5X Cross` |
| `1600` | `0xbfc7...80b4` | `SHORT` | 1,343,857.50 USD | `1,075.00` | `558.03` | `1251.50` | `2670.98` | -743,978.77 USD | `-55.36%` | `10X Cross` |
| `1641` | `0x123d...3bff` | `SHORT` | 1,304,902.83 USD | `1,044.34` | `519.62` | `1251.82` | `4119.85` | -762,244.62 USD | `-58.41%` | `10X Cross` |
| `1703` | `0xe282...df29` | `LONG` | 1,250,900.00 USD | `1,000.00` | `420.99` | `1251.82` | `805.91` | 829,913.14 USD | `+66.35%` | `10X Cross` |
| `1704` | `0x668c...ea2e` | `SHORT` | 1,250,100.00 USD | `1,000.00` | `1406.98` | `1251.82` | `4212.45` | 156,881.99 USD | `+12.55%` | `10X Cross` |
| `1728` | `0x17f0...094f` | `LONG` | 1,230,473.43 USD | `984.30` | `1287.23` | `1251.82` | `537.00` | -36,546.73 USD | `-2.97%` | `5X Cross` |
| `1744` | `0x51f6...2b39` | `SHORT` | 1,217,569.00 USD | `972.81` | `1299.77` | `1251.82` | `2502.25` | 46,858.71 USD | `+3.85%` | `10X Cross` |
| `1804` | `0x757d...94ba` | `LONG` | 1,157,267.50 USD | `925.00` | `1558.31` | `1251.82` | `0.000000` | -284,173.09 USD | `-24.56%` | `10X Cross` |
| `1842` | `0xb911...5525` | `LONG` | 1,124,550.00 USD | `900.00` | `1294.82` | `1251.82` | `1035.43` | -40,787.82 USD | `-3.63%` | `10X Cross` |
| `1864` | `0xef96...9383` | `SHORT` | 1,109,268.61 USD | `887.77` | `1259.32` | `1251.82` | `5124.59` | 8,718.26 USD | `+0.79%` | `10X Cross` |
| `1885` | `0xcf0a...856f` | `LONG` | 1,088,850.39 USD | `871.15` | `1292.19` | `1251.82` | `1035.68` | -36,844.46 USD | `-3.38%` | `4X Cross` |
| `1908` | `0xdf95...7d72` | `SHORT` | 1,067,355.44 USD | `853.27` | `1074.39` | `1251.82` | `44994.65` | -150,608.00 USD | `-14.11%` | `10X Cross` |
| `1958` | `0x601c...4f54` | `SHORT` | 1,030,607.44 USD | `824.42` | `615.11` | `1251.82` | `3123.94` | -523,494.69 USD | `-50.79%` | `5X Cross` |
| `1972` | `0xae55...2236` | `LONG` | 1,023,145.45 USD | `817.47` | `1467.80` | `1251.82` | `0.000000` | -176,735.77 USD | `-17.27%` | `10X Cross` |
| `1986` | `0x38f9...cb04` | `SHORT` | 1,016,343.80 USD | `813.01` | `1253.37` | `1251.82` | `2318.67` | 2,654.76 USD | `+0.26%` | `10X Cross` |
| `2012` | `0x0f02...5384` | `LONG` | 1,001,695.70 USD | `800.78` | `1290.36` | `1251.82` | `306.60` | -31,598.37 USD | `-3.15%` | `3X Cross` |
| `2015` | `0x9b0f...db40` | `LONG` | 1,001,280.00 USD | `800.00` | `1268.86` | `1251.82` | `796.97` | -13,809.76 USD | `-1.38%` | `10X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `1608.80` | 1,238.78 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 1.24K USD at 1608.8000 USD [API] | `2026-09-26 21:17:31` |
| `ANNOUNCEMENT` | `INFO` | `1608.80` | 128.70 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 0.13K USD at 1608.8000 USD [API] | `2026-09-26 21:17:31` |
| `ANNOUNCEMENT` | `INFO` | `1608.60` | 3,989.33 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 3.99K USD at 1608.6000 USD [API] | `2026-09-26 21:17:31` |
| `ANNOUNCEMENT` | `INFO` | `1608.60` | 997.33 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 1.00K USD at 1608.6000 USD [API] | `2026-09-26 21:17:31` |
| `ANNOUNCEMENT` | `INFO` | `1608.60` | 160.86 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 0.16K USD at 1608.6000 USD [API] | `2026-09-26 21:17:31` |
| `ANNOUNCEMENT` | `INFO` | `1608.60` | 96.52 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 0.10K USD at 1608.6000 USD [API] | `2026-09-26 21:17:31` |
| `ANNOUNCEMENT` | `INFO` | `1608.60` | 3,088.51 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 3.09K USD at 1608.6000 USD [API] | `2026-09-26 21:17:31` |
| `ANNOUNCEMENT` | `INFO` | `1608.50` | 3,989.08 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 3.99K USD at 1608.5000 USD [API] | `2026-09-26 21:17:31` |
| `ANNOUNCEMENT` | `INFO` | `1608.50` | 579.06 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 0.58K USD at 1608.5000 USD [API] | `2026-09-26 21:17:31` |
| `ANNOUNCEMENT` | `INFO` | `1608.50` | 1,849.77 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 1.85K USD at 1608.5000 USD [API] | `2026-09-26 21:17:31` |
| `ANNOUNCEMENT` | `INFO` | `1251.50` | 3,191.32 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 3.19K USD at 1251.5000 USD [API] | `2026-10-29 01:59:43` |
| `ANNOUNCEMENT` | `INFO` | `1251.50` | 1,151.38 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 1.15K USD at 1251.5000 USD [API] | `2026-10-29 01:59:43` |
| `ANNOUNCEMENT` | `INFO` | `1251.50` | 37.55 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 0.04K USD at 1251.5000 USD [API] | `2026-10-29 01:59:43` |
| `ANNOUNCEMENT` | `INFO` | `1251.50` | 25.03 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 0.03K USD at 1251.5000 USD [API] | `2026-10-29 01:59:43` |
| `ANNOUNCEMENT` | `INFO` | `1251.50` | 87.61 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 0.09K USD at 1251.5000 USD [API] | `2026-10-29 01:59:43` |
| `ANNOUNCEMENT` | `INFO` | `1251.50` | 200.24 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 0.20K USD at 1251.5000 USD [API] | `2026-10-29 01:59:43` |
| `ANNOUNCEMENT` | `INFO` | `1251.50` | 638.26 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 0.64K USD at 1251.5000 USD [API] | `2026-10-29 01:59:43` |
| `ANNOUNCEMENT` | `INFO` | `1251.50` | 47,419.33 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 47.42K USD at 1251.5000 USD [API] | `2026-10-29 01:59:43` |
| `ANNOUNCEMENT` | `INFO` | `1254.20` | 37.63 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 0.04K USD at 1254.2000 USD [API] | `2026-10-29 01:59:40` |
| `ANNOUNCEMENT` | `INFO` | `1254.20` | 12.54 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 0.01K USD at 1254.2000 USD [API] | `2026-10-29 01:59:40` |
| `ANNOUNCEMENT` | `INFO` | `1254.20` | 2,872.12 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 2.87K USD at 1254.2000 USD [API] | `2026-10-29 01:59:40` |
| `ANNOUNCEMENT` | `INFO` | `1254.20` | 50.17 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 0.05K USD at 1254.2000 USD [API] | `2026-10-29 01:59:40` |
| `ANNOUNCEMENT` | `INFO` | `1254.20` | 2,031.80 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 2.03K USD at 1254.2000 USD [API] | `2026-10-29 01:59:40` |
| `ANNOUNCEMENT` | `INFO` | `1254.20` | 1,944.01 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 1.94K USD at 1254.2000 USD [API] | `2026-10-29 01:59:40` |
| `ANNOUNCEMENT` | `INFO` | `1268.60` | 3,247.62 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Long: 3.25K USD at 1268.6000 USD [API] | `2026-10-29 10:47:00` |
| `ANNOUNCEMENT` | `INFO` | `1266.10` | 3,456.45 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Long: 3.46K USD at 1266.1000 USD [API] | `2026-10-29 10:49:57` |
| `ANNOUNCEMENT` | `INFO` | `1241.60` | 24.83 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Long: 0.02K USD at 1241.6000 USD [API] | `2026-10-26 09:56:17` |
| `ANNOUNCEMENT` | `INFO` | `1241.60` | 62.08 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Long: 0.06K USD at 1241.6000 USD [API] | `2026-10-26 09:56:17` |
| `ANNOUNCEMENT` | `INFO` | `1266.50` | 937.21 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Long: 0.94K USD at 1266.5000 USD [API] | `2026-10-29 10:49:57` |
| `ANNOUNCEMENT` | `INFO` | `1267.40` | 1,368.79 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Long: 1.37K USD at 1267.4000 USD [API] | `2026-10-29 10:44:46` |
| `ANNOUNCEMENT` | `INFO` | `1266.40` | 1,139.76 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Long: 1.14K USD at 1266.4000 USD [API] | `2026-10-29 10:49:57` |
| `ANNOUNCEMENT` | `INFO` | `1266.40` | 10,333.82 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Long: 10.33K USD at 1266.4000 USD [API] | `2026-10-29 10:49:57` |
| `ANNOUNCEMENT` | `INFO` | `1266.30` | 1,139.67 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Long: 1.14K USD at 1266.3000 USD [API] | `2026-10-29 10:49:57` |
| `ANNOUNCEMENT` | `INFO` | `1268.60` | 10,491.32 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Long: 10.49K USD at 1268.6000 USD [API] | `2026-10-29 10:47:00` |
| `ANNOUNCEMENT` | `INFO` | `1239.10` | 2,007.34 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 2.01K USD at 1239.1000 USD [API] | `2026-10-29 02:30:54` |
| `ANNOUNCEMENT` | `INFO` | `1266.30` | 7,990.35 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Long: 7.99K USD at 1266.3000 USD [API] | `2026-10-29 10:49:57` |
| `ANNOUNCEMENT` | `INFO` | `1238.40` | 3,987.65 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 3.99K USD at 1238.4000 USD [API] | `2026-10-29 02:30:57` |
| `ANNOUNCEMENT` | `INFO` | `1239.00` | 3,989.58 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 3.99K USD at 1239.0000 USD [API] | `2026-10-29 02:30:54` |
| `ANNOUNCEMENT` | `INFO` | `1248.40` | 37.45 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 0.04K USD at 1248.4000 USD [API] | `2026-10-29 02:05:52` |
| `ANNOUNCEMENT` | `INFO` | `1087.00` | 239.14 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Long: 0.24K USD at 1087.0000 USD [API] | `2026-10-15 02:24:27` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`1404.55` (Vol: 3,000,000.00 USD, Dist: `+12.58%`) | Long MP=`1176.48` (Vol: 3,400,000.00 USD, Dist: `--5.70%`)
  * 48H Horizon: Short MP=`1404.55` (Vol: 3,000,000.00 USD, Dist: `+12.58%`) | Long MP=`1176.48` (Vol: 3,400,000.00 USD, Dist: `--5.70%`)
  * 3D Horizon: Short MP=`1404.55` (Vol: 3,000,000.00 USD, Dist: `+12.58%`) | Long MP=`1176.48` (Vol: 3,400,000.00 USD, Dist: `--5.70%`)
  * 7D Horizon: Short MP=`1404.10` (Vol: 3,000,000.00 USD, Dist: `+12.55%`) | Long MP=`1176.74` (Vol: 4,900,000.00 USD, Dist: `--5.68%`)
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
| `5m` | `BALANCED` | 0.00 USD | 1,750.00 USD | 1,750.00 USD | 1,750.00 USD | `1` | `2026-10-30 08:40:00 UTC - 2026-10-30 08:45:00 UTC` |
| `15m` | `BALANCED` | 0.00 USD | 1,750.00 USD | 1,750.00 USD | 1,750.00 USD | `1` | `2026-10-30 08:30:00 UTC - 2026-10-30 08:45:00 UTC` |
| `1h` | `BALANCED` | 0.00 USD | 1,750.00 USD | 1,750.00 USD | 1,750.00 USD | `1` | `2026-10-30 08:00:00 UTC - 2026-10-30 09:00:00 UTC` |
| `4h` | `BALANCED` | 0.00 USD | 1,750.00 USD | 1,750.00 USD | 1,750.00 USD | `1` | `2026-10-30 08:00:00 UTC - 2026-10-30 12:00:00 UTC` |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `0 USD` | Total OI Tokens: `-`
  * 1h OI Change: `0.00%` | 4h OI Change: `0.00%` | 24h OI Change: `0.00%`
  * Exchange Breakdown: Binance=`-` | Bybit=`-` | OKX=`-` | Hyperliquid=`-`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `81.93K` | Last 24h: `171.90K` | Last 3d: `285.15K` | Last 7d: `847.79K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0096%` | **USDT OKX** | `0.0100%` |
| **USDT Bybit** | `0.0100%` | **USDT KuCoin** | `0.0100%` |
| **USDT MEXC** | `0.0095%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `0.0043%` | **USDT Bitget** | `0.0100%` |
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
| `5:00 UTC` | `1276.05` | `1275.11` | `1276.05` | `1278.15` | `1270.05` | 5,707,002.45 USD | 3,166,515.95 USD | 2,540,486.50 USD | 626,029.45 USD | `+10.97%` | `3B / 0S` |
| `0:00 UTC` | `1271.85` | `1274.42` | `1271.85` | `1282.95` | `1268.85` | 8,167,112.53 USD | 4,190,418.72 USD | 3,976,693.81 USD | 213,724.90 USD | `+2.62%` | `8B / 7S` |
| `5:00 UTC` | `1267.95` | `1271.35` | `1267.95` | `1277.85` | `1264.95` | 9,333,572.45 USD | 5,033,580.65 USD | 4,299,991.80 USD | 733,588.86 USD | `+7.86%` | `7B / 2S` |
| `0:00 UTC` | `1266.15` | `1267.62` | `1266.15` | `1278.45` | `1260.45` | 12,479,157.49 USD | 5,007,423.22 USD | 7,471,734.27 USD | -2,464,311.04 USD | `-19.75%` | `3B / 15S` |
| `5:00 UTC` | `1263.15` | `1263.66` | `1263.15` | `1267.05` | `1260.45` | 8,382,487.91 USD | 4,193,725.38 USD | 4,188,762.53 USD | 4,962.85 USD | `+0.06%` | `3B / 2S` |
| `0:00 UTC` | `1255.05` | `1256.16` | `1255.05` | `1269.15` | `1247.25` | 26,236,011.28 USD | 8,922,234.21 USD | 17,313,777.08 USD | -8,391,542.87 USD | `-31.98%` | `2B / 24S` |
| `5:00 UTC` | `1248.15` | `1248.05` | `1248.15` | `1253.25` | `1244.25` | 21,008,122.73 USD | 11,395,427.09 USD | 9,612,695.64 USD | 1,782,731.45 USD | `+8.49%` | `1B / 0S` |
| `0:00 UTC` | `1245.75` | `1245.57` | `1245.75` | `1250.55` | `1240.05` | 17,224,192.69 USD | 9,235,789.14 USD | 7,988,403.55 USD | 1,247,385.58 USD | `+7.24%` | `1B / 6S` |
| `5:00 UTC` | `1251.45` | `1250.99` | `1251.45` | `1255.05` | `1246.35` | 13,619,576.55 USD | 6,741,413.50 USD | 6,878,163.05 USD | -136,749.55 USD | `-1.00%` | `2B / 0S` |
| `0:00 UTC` | `1249.95` | `1248.51` | `1249.95` | `1252.35` | `1244.55` | 6,379,048.29 USD | 3,020,673.68 USD | 3,358,374.61 USD | -337,700.93 USD | `-5.29%` | `2B / 6S` |

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
| `5m` | 125,390.00 USD | 2,170,000.00 USD | **`ACCUMULATION`** |
| `15m` | -1,600.00 USD | -1,050,000.00 USD | **`DISTRIBUTION`** |
| `30m` | 554,000.00 USD | 3,160,000.00 USD | **`ACCUMULATION`** |
| `1h` | 3,070,000.00 USD | -8,700,000.00 USD | **`DISTRIBUTION`** |
| `2h` | 3,110,000.00 USD | -22,580,000.00 USD | **`DISTRIBUTION`** |
| `4h` | 1,860,000.00 USD | -36,510,000.00 USD | **`DISTRIBUTION`** |
| `6h` | 4,930,000.00 USD | -42,190,000.00 USD | **`DISTRIBUTION`** |
| `8h` | 9,440,000.00 USD | -22,340,000.00 USD | **`DISTRIBUTION`** |
| `12h` | 1,170,000.00 USD | -15,510,000.00 USD | **`DISTRIBUTION`** |
| `24h` | 20,260,000.00 USD | 75,830,000.00 USD | **`ACCUMULATION`** |
| `1w` | 36,250,000.00 USD | 194,800,000.00 USD | **`ACCUMULATION`** |
| `30d` | 65,360,000.00 USD | -543,570,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+125.39K` | 15m=`-1.60K` | 1h=`+3.07M` | 24h=`+20.26M`
* Futures Capital Netflows: 5m=`+2.17M` | 15m=`-1.05M` | 1h=`-8.70M` | 24h=`+75.83M`
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
  * `2026-10-30 13:52:16 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 13:51:16 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 13:32:16 IST`: [kof.ethz.ch] - (Sentiment: `Neutral`)
  * `2026-10-30 13:24:16 IST`: [gerlachmacro.substack.com] - (Sentiment: `Neutral`)
  * `2026-10-30 13:24:16 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-30 13:22:16 IST`: [insee.fr] - (Sentiment: `Neutral`)
  * `2026-10-30 13:21:16 IST`: [insee.fr] - (Sentiment: `Neutral`)
  * `2026-10-30 14:06:16 IST`: [@FirstSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 14:06:16 IST`: [nationwide.co.uk] - (Sentiment: `Neutral`)
  * `2026-10-30 14:06:16 IST`: [destatis.de] - (Sentiment: `Neutral`)
  * `2026-10-30 14:06:16 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-30 14:06:16 IST`: [@FirstSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 14:05:16 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-30 14:05:16 IST`: [insee.fr] - (Sentiment: `Neutral`)
  * `2026-10-30 14:05:16 IST`: [insee.fr] - (Sentiment: `Neutral`)


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
  * Execution Entry: `1240.72` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `1223.03` (Risk Distance: `17.69` pts)
  * +2.5R Take Profit: `1284.93`
  * Mathematical Lot Sizing: **`0.56 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `1284.79` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `1302.48` (Risk Distance: `17.69` pts)
  * +2.5R Take Profit: `1240.58`
  * Mathematical Lot Sizing: **`0.56 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`1259.14`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
