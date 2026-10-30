# 🏛️ SOVEREIGN CANDIDATE DOSSIER: ZECUSD
**Canonical Key**: `ZECUSD` | **Broker Instrument**: `ZECUSD.p` | **Asset Class**: `Crypto Altcoin`
**Timestamp**: `2026-10-30 16:27:43 IST` (`2026-10-30 10:57:43 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `1261.40` | **Live Ask Quote**: `1262.50` | **Mid Price**: `1261.95`
- **Spread Points**: `110.00` | **Spread BPS**: `8.72 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `1261.95` | VWAP Z-Score: `+0.00` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `3.15` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `50.00` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `1270.78` | Lower -3.00σ Band: `1253.12`
  * Upper +2.51σ Band: `1268.89` | Lower -2.51σ Band: `1255.01`
  * Upper +2.01σ Band: `1267.25` | Lower -2.01σ Band: `1256.65`
  * Upper +2.00σ Band: `1267.00` | Lower -2.00σ Band: `1256.90`
  * Upper +1.28σ Band: `1265.48` | Lower -1.28σ Band: `1258.42`
  * Upper +1.00σ Band: `1264.47` | Lower -1.00σ Band: `1259.43`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`1261.95` | EMA-20=`1261.95` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`1261.95` (Slope: `+0.0000`) | EMA-100=`1261.95`
  * Institutional Anchors: EMA-144=`1261.95` | EMA-200=`1261.95` (Slope: `+0.0000`) | EMA-233=`1261.95`
- **Range Boundaries**: 24H High=`1274.57` | 24H Low=`1249.33` | Weekly High=`1287.19` | Weekly Low=`1236.71`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `1279.38` (Distance: `-1.17%`)
  * Point of Control (POC) = `1247.68` (Distance: `+1.34%`)
  * Value Area Low (VAL) = `1239.95` (Distance: `+1.97%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`1309.91` | POC=`1246.71` | VAL=`1230.27`
  * Prior Day Extremes: PDH=`1396.49` | PDL=`1206.89` | PDC=`1244.38`
  * Monday Range Blueprint: High=`1267.53` | Mid=`1222.14` | Low=`1176.75`
  * Developing Weekly Value Area: Weekly VAH=`1300.54` | Weekly POC=`1240.47` | Weekly VAL=`1214.11`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`1296.00` | Low=`1180.03`
  * London Session (08:00-16:00 UTC): High=`1283.82` | Low=`1239.95`
  * New York Session (13:00-21:00 UTC): High=`1276.03` | Low=`1245.73`
  * Initial Balance (First Hour): IB High=`1283.82` | IB Low=`1264.92`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `1256.90` - `1267.00`
  * Optimal Trade Entry (OTE 0.705): `1264.47`
  * Structural Invalidation Anchor (0.786): `1272.05`

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
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 16:23:13 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `12` | `0xb83d...6e36` | `SHORT` | 66,456,207.24 USD | `52,385.47` | `1336.45` | `1268.70` | `3176.44` | 3,554,360.16 USD | `+5.35%` | `3X Cross` |
| `21` | `0x5b5d...c060` | `SHORT` | 50,901,994.81 USD | `40,121.38` | `1478.36` | `1268.70` | `4777.65` | 8,412,040.31 USD | `+16.53%` | `3X Cross` |
| `36` | `0x7fda...17d1` | `SHORT` | 33,789,972.20 USD | `26,633.54` | `1262.58` | `1268.70` | `2596.02` | -163,074.05 USD | `-0.48%` | `5X Cross` |
| `78` | `0x60b0...991e` | `LONG` | 21,288,456.14 USD | `16,779.74` | `1179.65` | `1268.70` | `911.76` | 1,494,209.12 USD | `+7.02%` | `10X Cross` |
| `137` | `0xc36a...105b` | `LONG` | 14,602,626.25 USD | `11,510.82` | `1215.14` | `1268.70` | `961.73` | 615,345.22 USD | `+4.21%` | `10X Cross` |
| `172` | `0x8742...8427` | `LONG` | 11,666,584.97 USD | `9,201.21` | `1286.37` | `1268.70` | `712.56` | -169,585.03 USD | `-1.45%` | `10X Cross` |
| `189` | `0x58b2...11f3` | `LONG` | 10,857,129.13 USD | `8,563.08` | `1246.56` | `1268.70` | `386.27` | 182,711.56 USD | `+1.68%` | `10X Cross` |
| `192` | `0x9071...5c0b` | `LONG` | 10,799,071.99 USD | `8,517.29` | `1353.83` | `1268.70` | `253.57` | -731,887.61 USD | `-6.78%` | `2X Cross` |
| `194` | `0x9ffd...ce40` | `LONG` | 10,695,288.36 USD | `8,434.77` | `1252.27` | `1268.70` | `598.41` | 132,664.23 USD | `+1.24%` | `5X Cross` |
| `196` | `0xad59...ba81` | `SHORT` | 10,677,682.40 USD | `8,425.00` | `330.91` | `1268.70` | `2145.85` | -7,889,724.63 USD | `-73.89%` | `10X Cross` |
| `202` | `0xdd53...2b13` | `SHORT` | 10,392,426.56 USD | `8,195.92` | `741.54` | `1268.70` | `8363.56` | -4,314,830.20 USD | `-41.52%` | `3X Cross` |
| `221` | `0x880a...311c` | `SHORT` | 9,777,239.75 USD | `7,707.11` | `1367.50` | `1268.70` | `2231.08` | 762,244.46 USD | `+7.80%` | `10X Cross` |
| `234` | `0xbf73...5d58` | `LONG` | 9,515,250.00 USD | `7,500.00` | `1248.78` | `1268.70` | `119.74` | 149,404.38 USD | `+1.57%` | `10X Cross` |
| `267` | `0x2b61...2f6c` | `LONG` | 8,632,637.40 USD | `6,807.00` | `1453.56` | `1268.70` | `578.75` | -1,261,713.82 USD | `-14.62%` | `10X Cross` |
| `284` | `0x2ae5...83e7` | `LONG` | 8,161,218.72 USD | `6,436.80` | `1391.82` | `1268.70` | `0.000000` | -797,673.27 USD | `-9.77%` | `1X Cross` |
| `313` | `0xecb6...2b00` | `SHORT` | 7,528,839.25 USD | `5,935.23` | `1277.44` | `1268.70` | `6417.50` | 53,038.52 USD | `+0.70%` | `5X Cross` |
| `330` | `0x26b6...9a13` | `LONG` | 6,889,426.27 USD | `5,433.73` | `1282.23` | `1268.70` | `227.88` | -77,876.97 USD | `-1.13%` | `10X Cross` |
| `344` | `0x45d2...4029` | `SHORT` | 6,627,313.30 USD | `5,227.00` | `833.44` | `1268.70` | `8914.21` | -2,270,935.33 USD | `-34.27%` | `5X Cross` |
| `362` | `0xea00...a918` | `LONG` | 6,338,500.00 USD | `5,000.00` | `739.16` | `1268.70` | `0.000000` | 2,642,684.89 USD | `+41.69%` | `5X Cross` |
| `372` | `0xdd7a...8830` | `LONG` | 6,162,234.90 USD | `4,860.19` | `897.48` | `1268.70` | `779.20` | 1,800,331.23 USD | `+29.22%` | `10X Cross` |
| `417` | `0x469e...58a5` | `SHORT` | 5,282,257.82 USD | `4,163.52` | `1242.31` | `1268.70` | `1949.55` | -109,873.17 USD | `-2.08%` | `10X Cross` |
| `419` | `0x4cae...7c34` | `LONG` | 5,265,908.81 USD | `4,152.27` | `1172.97` | `1268.70` | `977.44` | 395,415.26 USD | `+7.51%` | `10X Cross` |
| `438` | `0xd4c1...3d1d` | `SHORT` | 4,982,365.25 USD | `3,930.24` | `1291.66` | `1268.70` | `2320.75` | 94,170.85 USD | `+1.89%` | `10X Cross` |
| `443` | `0xa61c...66b9` | `LONG` | 4,929,595.20 USD | `3,888.00` | `1148.34` | `1268.70` | `0.000000` | 464,853.06 USD | `+9.43%` | `10X Cross` |
| `466` | `0x9aa5...58af` | `SHORT` | 4,719,585.27 USD | `3,720.31` | `1205.51` | `1268.70` | `3640.72` | -234,698.47 USD | `-4.97%` | `10X Cross` |
| `470` | `0x0153...8052` | `SHORT` | 4,688,922.42 USD | `3,698.18` | `1307.82` | `1268.70` | `2504.94` | 147,648.33 USD | `+3.15%` | `1X Isolated` |
| `503` | `0xb122...e4ba` | `LONG` | 4,435,710.11 USD | `3,498.47` | `1265.25` | `1268.70` | `1076.03` | 9,258.58 USD | `+0.21%` | `10X Cross` |
| `511` | `0x382b...3e39` | `LONG` | 4,378,505.89 USD | `3,454.17` | `1220.72` | `1268.70` | `0.000000` | 161,936.92 USD | `+3.70%` | `10X Cross` |
| `537` | `0xd21d...90f1` | `LONG` | 4,123,275.00 USD | `3,250.00` | `1253.64` | `1268.70` | `876.17` | 48,933.27 USD | `+1.19%` | `4X Isolated` |
| `543` | `0x456f...cdf1` | `LONG` | 4,051,138.18 USD | `3,195.66` | `1267.53` | `1268.70` | `508.37` | 542.37 USD | `+0.01%` | `10X Cross` |
| `553` | `0x1338...c48e` | `LONG` | 3,994,017.68 USD | `3,149.43` | `1018.52` | `1268.70` | `820.46` | 786,272.14 USD | `+19.69%` | `4X Isolated` |
| `569` | `0xdbe0...d6d5` | `LONG` | 3,911,940.62 USD | `3,085.37` | `422.97` | `1268.70` | `338.78` | 2,606,936.13 USD | `+66.64%` | `3X Isolated` |
| `591` | `0x325e...9564` | `LONG` | 3,803,353.33 USD | `3,000.91` | `1298.07` | `1268.70` | `134.37` | -92,051.83 USD | `-2.42%` | `10X Cross` |
| `595` | `0x9c06...0560` | `SHORT` | 3,792,561.30 USD | `2,989.80` | `786.00` | `1268.70` | `2541.92` | -1,442,566.30 USD | `-38.04%` | `10X Cross` |
| `596` | `0x2e30...4cb5` | `SHORT` | 3,790,407.04 USD | `2,989.28` | `1282.25` | `1268.70` | `2887.62` | 42,596.55 USD | `+1.12%` | `2X Cross` |
| `605` | `0x27c9...d65d` | `SHORT` | 3,724,259.50 USD | `2,938.04` | `1254.41` | `1268.70` | `1723.21` | -38,749.46 USD | `-1.04%` | `10X Cross` |
| `693` | `0xa183...0482` | `LONG` | 3,212,960.72 USD | `2,534.00` | `530.25` | `1268.70` | `444.70` | 1,869,298.00 USD | `+58.18%` | `5X Isolated` |
| `694` | `0xac48...3201` | `LONG` | 3,211,714.05 USD | `2,531.50` | `1378.58` | `1268.70` | `560.97` | -278,158.23 USD | `-8.66%` | `10X Cross` |
| `708` | `0x0871...e927` | `LONG` | 3,171,500.00 USD | `2,500.00` | `1276.50` | `1268.70` | `0.000000` | -19,750.00 USD | `-0.62%` | `10X Cross` |
| `719` | `0x9b86...6e6e` | `LONG` | 3,125,188.71 USD | `2,463.30` | `637.58` | `1268.70` | `882.63` | 1,554,639.43 USD | `+49.75%` | `3X Cross` |
| `804` | `0xf48f...10fe` | `LONG` | 2,814,376.41 USD | `2,218.49` | `1517.87` | `1268.70` | `964.81` | -553,010.41 USD | `-19.65%` | `3X Cross` |
| `819` | `0x71d0...8c26` | `SHORT` | 2,751,978.44 USD | `2,170.33` | `1266.69` | `1268.70` | `3779.34` | -2,842.21 USD | `-0.10%` | `10X Cross` |
| `835` | `0x5bc4...3b0c` | `SHORT` | 2,701,778.32 USD | `2,130.74` | `1089.65` | `1268.70` | `3661.97` | -380,020.74 USD | `-14.07%` | `5X Cross` |
| `847` | `0x8de4...b9aa` | `SHORT` | 2,653,219.62 USD | `2,091.29` | `1331.35` | `1268.70` | `1690.07` | 131,020.08 USD | `+4.94%` | `3X Cross` |
| `856` | `0x4fe2...ac59` | `SHORT` | 2,628,200.86 USD | `2,071.57` | `1478.56` | `1268.70` | `1831.16` | 434,745.36 USD | `+16.54%` | `10X Cross` |
| `861` | `0xdf57...93f5` | `LONG` | 2,604,915.80 USD | `2,054.35` | `1227.36` | `1268.70` | `897.41` | 83,493.76 USD | `+3.21%` | `4X Isolated` |
| `867` | `0xbcd4...0dd2` | `LONG` | 2,580,230.91 USD | `2,033.92` | `1228.20` | `1268.70` | `806.14` | 82,180.10 USD | `+3.18%` | `10X Cross` |
| `877` | `0x9a99...d21a` | `LONG` | 2,537,400.00 USD | `2,000.00` | `1278.44` | `1268.70` | `0.000000` | -19,473.67 USD | `-0.77%` | `10X Cross` |
| `878` | `0xf29c...9971` | `LONG` | 2,535,880.60 USD | `2,000.00` | `1254.95` | `1268.70` | `0.000000` | 25,983.53 USD | `+1.02%` | `10X Cross` |
| `897` | `0x77ee...2902` | `SHORT` | 2,468,733.66 USD | `1,946.03` | `759.84` | `1268.70` | `5707.60` | -990,056.15 USD | `-40.10%` | `10X Cross` |
| `909` | `0x3e2f...b269` | `SHORT` | 2,441,546.68 USD | `1,925.51` | `1134.87` | `1268.70` | `2977.34` | -256,347.82 USD | `-10.50%` | `10X Cross` |
| `924` | `0x4f12...618b` | `SHORT` | 2,404,293.41 USD | `1,896.28` | `1608.30` | `1268.70` | `2116.96` | 645,490.98 USD | `+26.85%` | `3X Cross` |
| `932` | `0x039c...0ebd` | `SHORT` | 2,376,252.72 USD | `1,873.13` | `1250.08` | `1268.70` | `3289.90` | -34,685.17 USD | `-1.46%` | `10X Cross` |
| `968` | `0x866d...d6e1` | `LONG` | 2,285,359.81 USD | `1,802.05` | `674.73` | `1268.70` | `109.54` | 1,069,458.50 USD | `+46.80%` | `10X Cross` |
| `991` | `0x2309...a2d9` | `LONG` | 2,220,519.38 USD | `1,750.37` | `1186.09` | `1268.70` | `806.85` | 144,425.27 USD | `+6.50%` | `8X Cross` |
| `1021` | `0x265e...7f70` | `LONG` | 2,094,241.15 USD | `1,651.74` | `1382.98` | `1268.70` | `0.000000` | -190,081.61 USD | `-9.08%` | `3X Cross` |
| `1025` | `0xfe7c...b7ae` | `SHORT` | 2,082,374.73 USD | `1,642.64` | `1346.92` | `1268.70` | `5596.89` | 130,133.89 USD | `+6.25%` | `10X Cross` |
| `1032` | `0x3e47...aaf6` | `LONG` | 2,075,948.44 USD | `1,636.28` | `1278.38` | `1268.70` | `1047.23` | -15,843.35 USD | `-0.76%` | `10X Cross` |
| `1035` | `0x2edd...8179` | `SHORT` | 2,074,259.04 USD | `1,635.98` | `1261.55` | `1268.70` | `2843.17` | -10,396.16 USD | `-0.50%` | `10X Cross` |
| `1050` | `0x7f75...9edf` | `LONG` | 2,045,854.87 USD | `1,612.56` | `1200.27` | `1268.70` | `988.16` | 110,340.95 USD | `+5.39%` | `10X Cross` |
| `1062` | `0xfc27...9d9d` | `SHORT` | 2,034,523.06 USD | `1,604.64` | `1295.09` | `1268.70` | `12732.13` | 43,622.75 USD | `+2.14%` | `10X Cross` |
| `1067` | `0x6646...6de5` | `SHORT` | 2,029,481.60 USD | `1,600.00` | `660.64` | `1268.70` | `4317.82` | -972,456.63 USD | `-47.92%` | `10X Cross` |
| `1075` | `0x023a...2355` | `SHORT` | 2,017,621.95 USD | `1,591.31` | `1310.00` | `1268.70` | `4404.15` | 66,987.30 USD | `+3.32%` | `10X Cross` |
| `1091` | `0xab59...59b5` | `LONG` | 1,984,512.70 USD | `1,565.32` | `1342.15` | `1268.70` | `833.27` | -116,382.52 USD | `-5.86%` | `10X Cross` |
| `1151` | `0xcf67...eb24` | `LONG` | 1,903,050.00 USD | `1,500.00` | `887.05` | `1268.70` | `598.32` | 572,478.63 USD | `+30.08%` | `10X Cross` |
| `1168` | `0x7277...0b98` | `SHORT` | 1,870,635.35 USD | `1,475.73` | `1287.86` | `1268.70` | `2175.55` | 29,896.77 USD | `+1.60%` | `10X Cross` |
| `1175` | `0x3205...40bb` | `SHORT` | 1,859,623.44 USD | `1,466.58` | `1259.67` | `1268.70` | `2250.85` | -12,212.50 USD | `-0.66%` | `10X Cross` |
| `1235` | `0x926a...af36` | `LONG` | 1,776,909.74 USD | `1,401.68` | `1254.50` | `1268.70` | `1187.92` | 18,507.84 USD | `+1.04%` | `10X Isolated` |
| `1236` | `0x2ab7...c2f8` | `LONG` | 1,775,846.68 USD | `1,400.51` | `813.26` | `1268.70` | `790.60` | 636,864.99 USD | `+35.86%` | `3X Cross` |
| `1257` | `0x11be...8b1d` | `LONG` | 1,744,139.69 USD | `1,375.83` | `1206.55` | `1268.70` | `1134.68` | 84,131.73 USD | `+4.82%` | `10X Isolated` |
| `1308` | `0x5323...b23c` | `SHORT` | 1,646,526.79 USD | `1,298.83` | `1263.89` | `1268.70` | `5527.70` | -4,952.49 USD | `-0.30%` | `5X Cross` |
| `1310` | `0xef96...9383` | `SHORT` | 1,644,701.30 USD | `1,297.39` | `1262.03` | `1268.70` | `3878.86` | -7,359.35 USD | `-0.45%` | `10X Cross` |
| `1333` | `0xdf83...3cff` | `SHORT` | 1,619,286.72 USD | `1,277.04` | `1260.37` | `1268.70` | `1870.98` | -9,740.57 USD | `-0.60%` | `10X Cross` |
| `1341` | `0xe065...0f85` | `SHORT` | 1,600,863.22 USD | `1,262.61` | `1087.02` | `1268.70` | `1541.58` | -228,387.09 USD | `-14.27%` | `10X Cross` |
| `1351` | `0x413c...886c` | `LONG` | 1,585,875.00 USD | `1,250.00` | `1237.51` | `1268.70` | `0.000000` | 38,985.54 USD | `+2.46%` | `10X Cross` |
| `1407` | `0x2847...d47b` | `LONG` | 1,537,296.48 USD | `1,211.71` | `1232.45` | `1268.70` | `0.000000` | 43,928.88 USD | `+2.86%` | `5X Cross` |
| `1421` | `0x5975...9abd` | `LONG` | 1,522,440.00 USD | `1,200.00` | `1179.54` | `1268.70` | `530.72` | 106,997.21 USD | `+7.03%` | `5X Cross` |
| `1423` | `0x266b...efcb` | `LONG` | 1,521,720.00 USD | `1,200.00` | `893.76` | `1268.70` | `398.81` | 449,210.30 USD | `+29.52%` | `10X Cross` |
| `1446` | `0xb897...ebc1` | `SHORT` | 1,488,004.02 USD | `1,173.56` | `1256.04` | `1268.70` | `1348.37` | -13,960.73 USD | `-0.94%` | `10X Cross` |
| `1458` | `0x69cc...14fd` | `SHORT` | 1,472,139.94 USD | `1,161.36` | `675.33` | `1268.70` | `8006.00` | -687,834.41 USD | `-46.72%` | `10X Cross` |
| `1467` | `0x3fc5...c0c1` | `SHORT` | 1,457,025.83 USD | `1,148.44` | `1264.34` | `1268.70` | `2725.11` | -5,012.05 USD | `-0.34%` | `10X Cross` |
| `1514` | `0x5f94...4b96` | `LONG` | 1,414,831.52 USD | `1,115.27` | `538.00` | `1268.70` | `0.000000` | 814,813.89 USD | `+57.59%` | `10X Cross` |
| `1518` | `0xe35c...a1d3` | `LONG` | 1,409,093.34 USD | `1,111.36` | `1311.66` | `1268.70` | `690.98` | -48,630.80 USD | `-3.45%` | `2X Isolated` |
| `1538` | `0x71df...a23d` | `SHORT` | 1,392,838.70 USD | `1,098.28` | `513.50` | `1268.70` | `2559.06` | -828,868.51 USD | `-59.51%` | `2X Cross` |
| `1567` | `0xbfc7...80b4` | `SHORT` | 1,363,852.50 USD | `1,075.00` | `558.03` | `1268.70` | `2623.71` | -763,973.77 USD | `-56.02%` | `10X Cross` |
| `1569` | `0x8b9d...7b28` | `SHORT` | 1,358,078.35 USD | `1,070.68` | `1272.16` | `1268.70` | `3327.95` | 3,999.90 USD | `+0.29%` | `10X Cross` |
| `1594` | `0x123d...3bff` | `SHORT` | 1,323,909.82 USD | `1,044.34` | `519.62` | `1268.70` | `4124.83` | -781,251.61 USD | `-59.01%` | `10X Cross` |
| `1652` | `0x668c...ea2e` | `SHORT` | 1,268,600.00 USD | `1,000.00` | `1406.98` | `1268.70` | `4212.88` | 138,381.99 USD | `+10.91%` | `10X Cross` |
| `1653` | `0xe282...df29` | `LONG` | 1,267,700.00 USD | `1,000.00` | `420.99` | `1268.70` | `796.46` | 846,713.14 USD | `+66.79%` | `10X Cross` |
| `1681` | `0x17f0...094f` | `LONG` | 1,248,289.26 USD | `984.30` | `1287.23` | `1268.70` | `537.03` | -18,730.90 USD | `-1.50%` | `5X Cross` |
| `1697` | `0x51f6...2b39` | `SHORT` | 1,233,425.80 USD | `972.81` | `1299.77` | `1268.70` | `2499.86` | 31,001.91 USD | `+2.51%` | `10X Cross` |
| `1722` | `0x4e23...20c3` | `LONG` | 1,212,593.08 USD | `956.53` | `1265.15` | `1268.70` | `0.000000` | 2,441.64 USD | `+0.20%` | `4X Cross` |
| `1733` | `0x38f9...cb04` | `SHORT` | 1,197,958.06 USD | `945.06` | `1253.73` | `1268.70` | `2173.92` | -13,109.25 USD | `-1.09%` | `10X Cross` |
| `1742` | `0xf096...7553` | `SHORT` | 1,188,876.25 USD | `937.23` | `1257.91` | `1268.70` | `3086.18` | -9,923.24 USD | `-0.83%` | `10X Cross` |
| `1760` | `0x757d...94ba` | `LONG` | 1,172,900.00 USD | `925.00` | `1558.31` | `1268.70` | `0.000000` | -268,540.59 USD | `-22.90%` | `10X Cross` |
| `1808` | `0xb911...5525` | `LONG` | 1,141,830.00 USD | `900.00` | `1294.82` | `1268.70` | `1035.46` | -23,507.82 USD | `-2.06%` | `10X Cross` |
| `1856` | `0xcf0a...856f` | `LONG` | 1,105,053.77 USD | `871.15` | `1292.19` | `1268.70` | `1030.52` | -20,641.07 USD | `-1.87%` | `4X Cross` |
| `1879` | `0xdf95...7d72` | `SHORT` | 1,081,554.35 USD | `853.23` | `1074.39` | `1268.70` | `44601.34` | -164,849.88 USD | `-15.24%` | `10X Cross` |
| `1907` | `0xb2f7...af9f` | `SHORT` | 1,053,851.39 USD | `830.72` | `746.63` | `1268.70` | `8170.66` | -433,612.36 USD | `-41.15%` | `10X Cross` |
| `1914` | `0x601c...4f54` | `SHORT` | 1,045,506.03 USD | `824.42` | `615.11` | `1268.70` | `3126.62` | -538,393.28 USD | `-51.50%` | `5X Cross` |
| `1929` | `0x8b61...c0c2` | `LONG` | 1,038,329.45 USD | `818.42` | `1274.67` | `1268.70` | `1005.18` | -4,884.59 USD | `-0.47%` | `4X Isolated` |
| `1933` | `0xae55...2236` | `LONG` | 1,036,470.21 USD | `817.47` | `1467.80` | `1268.70` | `0.000000` | -163,411.00 USD | `-15.77%` | `10X Cross` |
| `1969` | `0x0f02...5384` | `LONG` | 1,015,068.73 USD | `800.78` | `1290.36` | `1268.70` | `299.19` | -18,225.34 USD | `-1.80%` | `3X Cross` |
| `1972` | `0x9b0f...db40` | `LONG` | 1,014,400.00 USD | `800.00` | `1268.86` | `1268.70` | `799.21` | -689.76 USD | `-0.07%` | `10X Cross` |
| `1987` | `0xabdb...84ac` | `LONG` | 1,006,954.50 USD | `793.69` | `711.79` | `1268.70` | `664.60` | 442,014.14 USD | `+43.90%` | `3X Cross` |
| `1989` | `0x6e8f...4364` | `LONG` | 1,006,268.83 USD | `793.65` | `1260.00` | `1268.70` | `885.84` | 6,269.84 USD | `+0.62%` | `10X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `1239.10` | 2,007.34 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 2.01K USD at 1239.1000 USD [API] | `2026-10-29 02:30:54` |
| `ANNOUNCEMENT` | `INFO` | `1266.30` | 7,990.35 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Long: 7.99K USD at 1266.3000 USD [API] | `2026-10-29 10:49:57` |
| `ANNOUNCEMENT` | `INFO` | `1238.40` | 3,987.65 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 3.99K USD at 1238.4000 USD [API] | `2026-10-29 02:30:57` |
| `ANNOUNCEMENT` | `INFO` | `1239.00` | 3,989.58 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 3.99K USD at 1239.0000 USD [API] | `2026-10-29 02:30:54` |
| `ANNOUNCEMENT` | `INFO` | `1248.40` | 37.45 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 0.04K USD at 1248.4000 USD [API] | `2026-10-29 02:05:52` |
| `ANNOUNCEMENT` | `INFO` | `1087.00` | 239.14 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Long: 0.24K USD at 1087.0000 USD [API] | `2026-10-15 02:24:27` |
| `ANNOUNCEMENT` | `INFO` | `1017.00` | 10.17 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Long: 0.01K USD at 1017.0000 USD [API] | `2026-09-04 08:53:37` |
| `ANNOUNCEMENT` | `INFO` | `1327.50` | 13.28 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Long: 0.01K USD at 1327.5000 USD [API] | `2026-10-29 15:31:54` |
| `ANNOUNCEMENT` | `INFO` | `1327.50` | 61,343.78 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Long: 61.34K USD at 1327.5000 USD [API] | `2026-10-29 15:31:54` |
| `ANNOUNCEMENT` | `INFO` | `1319.10` | 10,420.89 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 10.42K USD at 1319.1000 USD [API] | `2026-10-29 18:31:05` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`1404.55` (Vol: 3,000,000.00 USD, Dist: `+11.24%`) | Long MP=`1176.48` (Vol: 3,400,000.00 USD, Dist: `--6.82%`)
  * 48H Horizon: Short MP=`1404.55` (Vol: 3,000,000.00 USD, Dist: `+11.24%`) | Long MP=`1176.48` (Vol: 3,400,000.00 USD, Dist: `--6.82%`)
  * 3D Horizon: Short MP=`1404.55` (Vol: 3,000,000.00 USD, Dist: `+11.24%`) | Long MP=`1176.48` (Vol: 3,400,000.00 USD, Dist: `--6.82%`)
  * 7D Horizon: Short MP=`1404.10` (Vol: 3,000,000.00 USD, Dist: `+11.21%`) | Long MP=`1176.74` (Vol: 4,900,000.00 USD, Dist: `--6.80%`)
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
| `5m` | `BALANCED` | 0.00 USD | 1,750.00 USD | 1,750.00 USD | 1,750.00 USD | `1` | `2026-10-30 10:50:00 UTC - 2026-10-30 10:55:00 UTC` |
| `15m` | `BALANCED` | 0.00 USD | 1,750.00 USD | 1,750.00 USD | 1,750.00 USD | `1` | `2026-10-30 10:45:00 UTC - 2026-10-30 11:00:00 UTC` |
| `1h` | `BALANCED` | 0.00 USD | 1,750.00 USD | 1,750.00 USD | 1,750.00 USD | `1` | `2026-10-30 10:00:00 UTC - 2026-10-30 11:00:00 UTC` |
| `4h` | `BALANCED` | 0.00 USD | 1,750.00 USD | 1,750.00 USD | 1,750.00 USD | `1` | `2026-10-30 08:00:00 UTC - 2026-10-30 12:00:00 UTC` |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `0 USD` | Total OI Tokens: `-`
  * 1h OI Change: `0.00%` | 4h OI Change: `0.00%` | 24h OI Change: `0.00%`
  * Exchange Breakdown: Binance=`-` | Bybit=`-` | OKX=`-` | Hyperliquid=`-`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `85.30K` | Last 24h: `171.90K` | Last 3d: `285.15K` | Last 7d: `847.79K`
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
| `0:00 UTC` | `1249.95` | `1249.10` | `1249.95` | `1253.55` | `1244.55` | 10,263,783.49 USD | 5,117,369.60 USD | 5,146,413.89 USD | -29,044.29 USD | `-0.28%` | `1B / 4S` |
| `5:00 UTC` | `1246.65` | `1246.77` | `1246.65` | `1252.35` | `1243.95` | 13,017,000.97 USD | 7,727,648.32 USD | 5,289,352.64 USD | 2,438,295.68 USD | `+18.73%` | `8B / 5S` |
| `0:00 UTC` | `1244.55` | `1245.81` | `1244.55` | `1249.05` | `1243.65` | 9,717,386.64 USD | 3,914,194.68 USD | 5,803,191.96 USD | -1,888,997.28 USD | `-19.44%` | `0B / 1S` |
| `5:00 UTC` | `1242.15` | `1244.40` | `1242.15` | `1249.35` | `1241.25` | 8,638,502.97 USD | 4,533,952.89 USD | 4,104,550.08 USD | 429,402.82 USD | `+4.97%` | `4B / 2S` |
| `0:00 UTC` | `1251.15` | `1247.35` | `1251.15` | `1251.75` | `1240.05` | 9,977,652.60 USD | 4,992,881.35 USD | 4,984,771.25 USD | 8,110.10 USD | `+0.08%` | `3B / 5S` |
| `5:00 UTC` | `1243.95` | `1249.40` | `1243.95` | `1256.55` | `1243.35` | 15,678,426.53 USD | 9,268,825.46 USD | 6,409,601.07 USD | 2,859,224.38 USD | `+18.24%` | `10B / 2S` |
| `0:00 UTC` | `1249.95` | `1250.19` | `1249.95` | `1256.25` | `1246.35` | 11,248,393.80 USD | 4,953,252.73 USD | 6,295,141.07 USD | -1,341,888.34 USD | `-11.93%` | `1B / 7S` |
| `5:00 UTC` | `1263.15` | `1259.85` | `1263.15` | `1266.15` | `1247.85` | 19,587,954.68 USD | 10,529,516.42 USD | 9,058,438.26 USD | 1,471,078.16 USD | `+7.51%` | `10B / 4S` |
| `0:00 UTC` | `1272.15` | `1270.75` | `1272.15` | `1276.65` | `1262.25` | 28,700,563.02 USD | 14,735,645.79 USD | 13,964,917.22 USD | 770,728.57 USD | `+2.69%` | `10B / 0S` |
| `5:00 UTC` | `1261.95` | `1263.12` | `1261.95` | `1268.85` | `1260.45` | 6,720,404.83 USD | 3,122,310.34 USD | 3,598,094.49 USD | -475,784.15 USD | `-7.08%` | `1B / 8S` |

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
| `5m` | -244,630.00 USD | -787,770.00 USD | **`DISTRIBUTION`** |
| `15m` | -753,410.00 USD | -2,980,000.00 USD | **`DISTRIBUTION`** |
| `30m` | -482,040.00 USD | 4,080,000.00 USD | **`ACCUMULATION`** |
| `1h` | -828,510.00 USD | 5,640,000.00 USD | **`ACCUMULATION`** |
| `2h` | -3,280,000.00 USD | 9,270,000.00 USD | **`ACCUMULATION`** |
| `4h` | -513,350.00 USD | -10,400,000.00 USD | **`DISTRIBUTION`** |
| `6h` | -1,300,000.00 USD | -23,360,000.00 USD | **`DISTRIBUTION`** |
| `8h` | -1,650,000.00 USD | -3,380,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -940,970.00 USD | -14,770,000.00 USD | **`DISTRIBUTION`** |
| `24h` | 20,650,000.00 USD | 73,530,000.00 USD | **`ACCUMULATION`** |
| `1w` | 35,510,000.00 USD | 226,770,000.00 USD | **`ACCUMULATION`** |
| `30d` | 62,110,000.00 USD | -568,170,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-244.63K` | 15m=`-753.41K` | 1h=`-828.51K` | 24h=`+20.65M`
* Futures Capital Netflows: 5m=`-787.77K` | 15m=`-2.98M` | 1h=`+5.64M` | 24h=`+73.53M`
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
  * `2026-10-30 15:50:15 IST`: [istat.it] - (Sentiment: `Neutral`)
  * `2026-10-30 15:33:15 IST`: [ec.europa.eu] - (Sentiment: `Neutral`)
  * `2026-10-30 15:32:15 IST`: [ec.europa.eu] - (Sentiment: `Neutral`)
  * `2026-10-30 16:18:15 IST`: [dailyforex.com] - (Sentiment: `Neutral`)
  * `2026-10-30 16:18:15 IST`: [breakingthenews.net] - (Sentiment: `Neutral`)
  * `2026-10-30 16:18:15 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 16:18:15 IST`: [@FirstSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 16:18:15 IST`: [destatis.de] - (Sentiment: `Neutral`)
  * `2026-10-30 16:18:15 IST`: [istat.it] - (Sentiment: `Neutral`)
  * `2026-10-30 16:17:15 IST`: [channelnewsasia.com] - (Sentiment: `Neutral`)
  * `2026-10-30 16:17:15 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 16:17:15 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 16:17:15 IST`: [kof.ethz.ch] - (Sentiment: `Neutral`)
  * `2026-10-30 16:17:15 IST`: [gerlachmacro.substack.com] - (Sentiment: `Neutral`)
  * `2026-10-30 16:17:15 IST`: [@financialjuice] - (Sentiment: `Neutral`)


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
  * Execution Entry: `1239.95` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `1234.51` (Risk Distance: `5.44` pts)
  * +2.5R Take Profit: `1253.54`
  * Mathematical Lot Sizing: **`1.83 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `1279.38` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `1284.82` (Risk Distance: `5.44` pts)
  * +2.5R Take Profit: `1265.79`
  * Mathematical Lot Sizing: **`1.83 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`1272.05`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
