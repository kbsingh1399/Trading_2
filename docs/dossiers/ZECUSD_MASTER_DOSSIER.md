# 🏛️ SOVEREIGN CANDIDATE DOSSIER: ZECUSD
**Canonical Key**: `ZECUSD` | **Broker Instrument**: `ZECUSD.p` | **Asset Class**: `Crypto Altcoin`
**Timestamp**: `2026-10-30 08:12:35 IST` (`2026-10-30 02:42:35 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `1227.90` | **Live Ask Quote**: `1228.69` | **Mid Price**: `1228.30`
- **Spread Points**: `79.00` | **Spread BPS**: `6.43 bps` (Charter Threshold: `12.00 bps`)
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
  * Session VWAP: `1223.69` | VWAP Z-Score: `+0.96` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `22.97` (Volatility Regime: `HIGH_EXPANSION`)
  * 14-Period RSI: `44.26` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `1255.16` | Lower -3.00σ Band: `1192.21`
  * Upper +2.51σ Band: `1250.02` | Lower -2.51σ Band: `1197.35`
  * Upper +2.01σ Band: `1244.78` | Lower -2.01σ Band: `1202.60`
  * Upper +2.00σ Band: `1244.67` | Lower -2.00σ Band: `1202.70`
  * Upper +1.28σ Band: `1237.12` | Lower -1.28σ Band: `1210.26`
  * Upper +1.00σ Band: `1234.18` | Lower -1.00σ Band: `1213.20`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`1231.50` | EMA-20=`1243.46` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`1264.99` (Slope: `+0.0000`) | EMA-100=`1273.15`
  * Institutional Anchors: EMA-144=`1274.30` | EMA-200=`1274.29` (Slope: `-0.4550`) | EMA-233=`1276.78`
- **Range Boundaries**: 24H High=`1396.49` | 24H Low=`1180.03` | Weekly High=`1396.49` | Weekly Low=`1180.03`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `1256.18` (Distance: `-0.83%`)
  * Point of Control (POC) = `1229.90` (Distance: `+1.28%`)
  * Value Area Low (VAL) = `1216.75` (Distance: `+2.38%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`1309.91` | POC=`1246.71` | VAL=`1230.27`
  * Prior Day Extremes: PDH=`1396.49` | PDL=`1206.89` | PDC=`1244.38`
  * Monday Range Blueprint: High=`1267.53` | Mid=`1222.14` | Low=`1176.75`
  * Developing Weekly Value Area: Weekly VAH=`1294.68` | Weekly POC=`1239.01` | Weekly VAL=`1196.53`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`1296.00` | Low=`1180.03`
  * London Session (08:00-16:00 UTC): High=`1233.21` | Low=`1223.38`
  * New York Session (13:00-21:00 UTC): High=`1235.66` | Low=`1220.93`
  * Initial Balance (First Hour): IB High=`1231.98` | IB Low=`1224.61`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `1223.38` - `1233.21`
  * Optimal Trade Entry (OTE 0.705): `1230.75`
  * Structural Invalidation Anchor (0.786): `1238.12`

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
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 07:57:16 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `13` | `0xb83d...6e36` | `SHORT` | 65,927,113.99 USD | `52,385.47` | `1336.45` | `1264.20` | `3844.91` | 4,083,453.41 USD | `+6.19%` | `3X Cross` |
| `22` | `0x5b5d...c060` | `SHORT` | 50,713,424.32 USD | `40,121.38` | `1478.36` | `1264.20` | `5328.82` | 8,600,610.79 USD | `+16.96%` | `3X Cross` |
| `41` | `0x7fda...17d1` | `SHORT` | 29,471,026.18 USD | `23,298.44` | `1261.28` | `1264.20` | `2848.15` | -85,070.76 USD | `-0.29%` | `5X Cross` |
| `79` | `0x60b0...991e` | `LONG` | 21,153,151.03 USD | `16,779.74` | `1179.65` | `1264.20` | `941.37` | 1,358,904.01 USD | `+6.42%` | `10X Cross` |
| `140` | `0xc36a...105b` | `LONG` | 14,524,352.68 USD | `11,510.82` | `1215.14` | `1264.20` | `973.11` | 537,071.65 USD | `+3.70%` | `10X Cross` |
| `153` | `0x9071...5c0b` | `LONG` | 13,305,047.06 USD | `10,517.29` | `1353.83` | `1264.20` | `0.0812` | -933,571.81 USD | `-7.02%` | `1X Cross` |
| `176` | `0x8742...8427` | `LONG` | 11,610,086.78 USD | `9,201.21` | `1286.37` | `1264.20` | `719.97` | -226,083.22 USD | `-1.95%` | `10X Cross` |
| `192` | `0x58b2...11f3` | `LONG` | 10,794,618.65 USD | `8,563.08` | `1246.56` | `1264.20` | `382.70` | 120,201.07 USD | `+1.11%` | `10X Cross` |
| `196` | `0x9ffd...ce40` | `LONG` | 10,675,479.34 USD | `8,468.57` | `1250.77` | `1264.20` | `605.99` | 83,251.88 USD | `+0.78%` | `5X Cross` |
| `198` | `0xad59...ba81` | `SHORT` | 10,621,397.50 USD | `8,425.00` | `330.91` | `1264.20` | `2146.82` | -7,833,439.73 USD | `-73.75%` | `10X Cross` |
| `205` | `0xdd53...2b13` | `SHORT` | 10,360,462.47 USD | `8,195.92` | `741.54` | `1264.20` | `8851.12` | -4,282,866.11 USD | `-41.34%` | `3X Cross` |
| `221` | `0x880a...311c` | `SHORT` | 9,735,188.21 USD | `7,707.11` | `1367.50` | `1264.20` | `2236.36` | 804,295.99 USD | `+8.26%` | `10X Cross` |
| `238` | `0xbf73...5d58` | `LONG` | 9,463,500.00 USD | `7,500.00` | `1248.78` | `1264.20` | `145.52` | 97,654.38 USD | `+1.03%` | `10X Cross` |
| `267` | `0x2b61...2f6c` | `LONG` | 8,589,072.60 USD | `6,807.00` | `1453.56` | `1264.20` | `541.64` | -1,305,278.62 USD | `-15.20%` | `10X Cross` |
| `289` | `0x2ae5...83e7` | `LONG` | 8,136,758.88 USD | `6,436.80` | `1391.82` | `1264.20` | `0.000000` | -822,133.11 USD | `-10.10%` | `1X Cross` |
| `331` | `0x26b6...9a13` | `LONG` | 6,852,360.62 USD | `5,433.73` | `1282.23` | `1264.20` | `224.66` | -114,942.61 USD | `-1.68%` | `10X Cross` |
| `344` | `0x45d2...4029` | `SHORT` | 6,594,383.20 USD | `5,227.00` | `833.44` | `1264.20` | `9375.88` | -2,238,005.23 USD | `-33.94%` | `5X Cross` |
| `360` | `0xea00...a918` | `LONG` | 6,303,182.00 USD | `5,000.00` | `739.16` | `1264.20` | `0.000000` | 2,607,366.89 USD | `+41.37%` | `5X Cross` |
| `375` | `0xdd7a...8830` | `LONG` | 6,128,205.31 USD | `4,860.19` | `897.48` | `1264.20` | `786.10` | 1,766,301.64 USD | `+28.82%` | `10X Cross` |
| `376` | `0xecb6...2b00` | `SHORT` | 6,043,659.91 USD | `4,777.84` | `1279.39` | `1264.20` | `7043.94` | 69,081.63 USD | `+1.14%` | `5X Cross` |
| `438` | `0xa61c...66b9` | `LONG` | 4,914,820.80 USD | `3,888.00` | `1148.34` | `1264.20` | `0.000000` | 450,078.66 USD | `+9.16%` | `10X Cross` |
| `462` | `0x9aa5...58af` | `SHORT` | 4,699,286.51 USD | `3,720.31` | `1205.51` | `1264.20` | `3745.56` | -214,399.71 USD | `-4.56%` | `10X Cross` |
| `464` | `0x0153...8052` | `SHORT` | 4,678,567.52 USD | `3,698.18` | `1307.82` | `1264.20` | `2504.79` | 158,003.23 USD | `+3.38%` | `1X Isolated` |
| `478` | `0x469e...58a5` | `SHORT` | 4,562,081.36 USD | `3,618.12` | `1237.30` | `1264.20` | `2069.25` | -85,383.49 USD | `-1.87%` | `10X Cross` |
| `514` | `0x4cae...7c34` | `LONG` | 4,293,180.90 USD | `3,400.27` | `1139.92` | `1264.20` | `925.70` | 417,153.30 USD | `+9.72%` | `10X Cross` |
| `535` | `0x456f...cdf1` | `LONG` | 4,110,212.36 USD | `3,266.02` | `1267.73` | `1264.20` | `527.27` | -30,235.25 USD | `-0.74%` | `10X Cross` |
| `537` | `0xd21d...90f1` | `LONG` | 4,097,919.48 USD | `3,250.00` | `1253.64` | `1264.20` | `876.00` | 23,577.74 USD | `+0.58%` | `4X Isolated` |
| `550` | `0x1338...c48e` | `LONG` | 3,976,470.32 USD | `3,149.43` | `1018.52` | `1264.20` | `820.29` | 768,724.78 USD | `+19.33%` | `4X Isolated` |
| `566` | `0x325e...9564` | `LONG` | 3,910,888.13 USD | `3,101.91` | `1298.07` | `1264.20` | `215.02` | -115,622.57 USD | `-2.96%` | `10X Cross` |
| `568` | `0x382b...3e39` | `LONG` | 3,901,177.16 USD | `3,084.30` | `1211.32` | `1264.20` | `0.000000` | 165,093.82 USD | `+4.23%` | `10X Cross` |
| `570` | `0xdbe0...d6d5` | `LONG` | 3,891,577.18 USD | `3,085.37` | `422.97` | `1264.20` | `338.61` | 2,586,572.69 USD | `+66.47%` | `3X Isolated` |
| `592` | `0x9c06...0560` | `SHORT` | 3,772,529.64 USD | `2,989.80` | `786.00` | `1264.20` | `2624.48` | -1,422,534.64 USD | `-37.71%` | `10X Cross` |
| `595` | `0x27c9...d65d` | `SHORT` | 3,744,814.88 USD | `2,962.67` | `1254.41` | `1264.20` | `1726.36` | -28,408.69 USD | `-0.76%` | `10X Cross` |
| `605` | `0x2e30...4cb5` | `SHORT` | 3,677,078.20 USD | `2,915.82` | `1288.34` | `1264.20` | `2935.18` | 79,478.16 USD | `+2.16%` | `2X Cross` |
| `621` | `0xd4c1...3d1d` | `SHORT` | 3,587,787.44 USD | `2,836.34` | `1298.47` | `1264.20` | `2878.71` | 95,120.47 USD | `+2.65%` | `10X Cross` |
| `630` | `0x71d0...8c26` | `SHORT` | 3,522,744.45 USD | `2,784.92` | `1261.48` | `1264.20` | `3388.51` | -9,618.80 USD | `-0.27%` | `10X Cross` |
| `686` | `0xa183...0482` | `LONG` | 3,197,908.00 USD | `2,534.00` | `530.25` | `1264.20` | `444.53` | 1,854,245.28 USD | `+57.98%` | `5X Isolated` |
| `689` | `0xac48...3201` | `LONG` | 3,191,301.05 USD | `2,531.50` | `1378.58` | `1264.20` | `500.33` | -298,571.24 USD | `-9.36%` | `10X Cross` |
| `703` | `0x0871...e927` | `LONG` | 3,154,500.00 USD | `2,500.00` | `1276.50` | `1264.20` | `0.000000` | -36,750.00 USD | `-1.17%` | `10X Cross` |
| `717` | `0x9b86...6e6e` | `LONG` | 3,105,482.31 USD | `2,463.30` | `637.58` | `1264.20` | `882.46` | 1,534,933.03 USD | `+49.43%` | `3X Cross` |
| `776` | `0xb2f7...af9f` | `SHORT` | 2,916,906.80 USD | `2,313.72` | `746.63` | `1264.20` | `4571.18` | -1,189,418.06 USD | `-40.78%` | `10X Cross` |
| `808` | `0xf48f...10fe` | `LONG` | 2,797,290.27 USD | `2,218.49` | `1517.87` | `1264.20` | `1023.04` | -570,096.55 USD | `-20.38%` | `3X Cross` |
| `825` | `0x5323...b23c` | `SHORT` | 2,704,280.52 USD | `2,137.88` | `1256.41` | `1264.20` | `3777.58` | -18,229.60 USD | `-0.67%` | `5X Cross` |
| `836` | `0x5bc4...3b0c` | `SHORT` | 2,688,993.88 USD | `2,130.74` | `1089.65` | `1264.20` | `3725.48` | -367,236.30 USD | `-13.66%` | `5X Cross` |
| `854` | `0x8de4...b9aa` | `SHORT` | 2,636,904.01 USD | `2,091.29` | `1331.35` | `1264.20` | `1689.91` | 147,335.70 USD | `+5.59%` | `3X Cross` |
| `860` | `0x4fe2...ac59` | `SHORT` | 2,611,496.55 USD | `2,071.57` | `1478.56` | `1264.20` | `1855.23` | 451,449.67 USD | `+17.29%` | `10X Cross` |
| `871` | `0xdf57...93f5` | `LONG` | 2,590,696.82 USD | `2,054.35` | `1227.36` | `1264.20` | `897.24` | 69,274.78 USD | `+2.67%` | `4X Isolated` |
| `876` | `0xbcd4...0dd2` | `LONG` | 2,564,162.94 USD | `2,033.92` | `1228.20` | `1264.20` | `678.25` | 66,112.13 USD | `+2.58%` | `10X Cross` |
| `890` | `0x413c...886c` | `LONG` | 2,521,400.00 USD | `2,000.00` | `1234.10` | `1264.20` | `0.000000` | 53,201.34 USD | `+2.11%` | `10X Cross` |
| `891` | `0x9a99...d21a` | `LONG` | 2,521,200.00 USD | `2,000.00` | `1278.44` | `1264.20` | `0.000000` | -35,673.67 USD | `-1.41%` | `10X Cross` |
| `909` | `0x77ee...2902` | `SHORT` | 2,455,500.65 USD | `1,946.03` | `759.84` | `1264.20` | `5473.47` | -976,823.15 USD | `-39.78%` | `10X Cross` |
| `921` | `0x3e2f...b269` | `SHORT` | 2,428,219.46 USD | `1,925.51` | `1134.87` | `1264.20` | `2931.84` | -243,020.60 USD | `-10.01%` | `10X Cross` |
| `934` | `0x4f12...618b` | `SHORT` | 2,390,450.57 USD | `1,896.28` | `1608.30` | `1264.20` | `2116.80` | 659,333.82 USD | `+27.58%` | `3X Cross` |
| `948` | `0xb122...e4ba` | `LONG` | 2,325,239.73 USD | `1,844.55` | `1255.11` | `1264.20` | `966.65` | 10,121.61 USD | `+0.44%` | `10X Cross` |
| `973` | `0x866d...d6e1` | `LONG` | 2,275,268.33 USD | `1,802.05` | `674.73` | `1264.20` | `288.91` | 1,059,367.02 USD | `+46.56%` | `10X Cross` |
| `993` | `0x2309...a2d9` | `LONG` | 2,208,616.87 USD | `1,750.37` | `1186.09` | `1264.20` | `817.04` | 132,522.76 USD | `+6.00%` | `8X Cross` |
| `1025` | `0x2edd...8179` | `SHORT` | 2,093,126.89 USD | `1,654.73` | `1261.58` | `1264.20` | `2903.24` | -5,553.65 USD | `-0.27%` | `10X Cross` |
| `1028` | `0x265e...7f70` | `LONG` | 2,087,799.36 USD | `1,651.74` | `1382.98` | `1264.20` | `0.000000` | -196,523.40 USD | `-9.41%` | `3X Cross` |
| `1043` | `0xfe7c...b7ae` | `SHORT` | 2,070,771.78 USD | `1,642.64` | `1346.92` | `1264.20` | `5926.06` | 141,736.84 USD | `+6.84%` | `10X Cross` |
| `1044` | `0x3e47...aaf6` | `LONG` | 2,068,257.92 USD | `1,636.28` | `1278.38` | `1264.20` | `1052.51` | -23,533.87 USD | `-1.14%` | `10X Cross` |
| `1057` | `0x3205...40bb` | `SHORT` | 2,042,886.73 USD | `1,616.08` | `1241.01` | `1264.20` | `2169.89` | -37,307.41 USD | `-1.83%` | `10X Cross` |
| `1066` | `0x7f75...9edf` | `LONG` | 2,026,012.63 USD | `1,605.78` | `1199.97` | `1264.20` | `980.40` | 99,120.73 USD | `+4.89%` | `10X Cross` |
| `1069` | `0x6646...6de5` | `SHORT` | 2,021,600.00 USD | `1,600.00` | `660.64` | `1264.20` | `4132.40` | -964,575.03 USD | `-47.71%` | `10X Cross` |
| `1071` | `0x023a...2355` | `SHORT` | 2,017,445.79 USD | `1,594.90` | `1310.00` | `1264.20` | `4471.52` | 71,866.35 USD | `+3.56%` | `10X Cross` |
| `1100` | `0xab59...59b5` | `LONG` | 1,973,398.92 USD | `1,565.32` | `1342.15` | `1264.20` | `844.03` | -127,496.29 USD | `-6.46%` | `10X Cross` |
| `1157` | `0xcf67...eb24` | `LONG` | 1,890,900.00 USD | `1,500.00` | `887.05` | `1264.20` | `701.45` | 560,328.63 USD | `+29.63%` | `10X Cross` |
| `1166` | `0xb695...a92d` | `LONG` | 1,870,063.00 USD | `1,483.00` | `1249.80` | `1264.20` | `0.000000` | 16,604.15 USD | `+0.89%` | `10X Cross` |
| `1169` | `0x7277...0b98` | `SHORT` | 1,861,043.10 USD | `1,475.73` | `1287.86` | `1264.20` | `2209.86` | 39,489.02 USD | `+2.12%` | `10X Cross` |
| `1239` | `0x2ab7...c2f8` | `LONG` | 1,767,163.52 USD | `1,400.51` | `813.26` | `1264.20` | `793.24` | 628,181.83 USD | `+35.55%` | `3X Cross` |
| `1253` | `0x11be...8b1d` | `LONG` | 1,734,508.88 USD | `1,375.83` | `1206.55` | `1264.20` | `1134.51` | 74,500.92 USD | `+4.30%` | `10X Isolated` |
| `1288` | `0xfc27...9d9d` | `SHORT` | 1,663,669.29 USD | `1,319.43` | `1298.53` | `1264.20` | `15893.50` | 49,647.49 USD | `+2.98%` | `10X Cross` |
| `1336` | `0x039c...0ebd` | `SHORT` | 1,605,323.34 USD | `1,268.93` | `1239.61` | `1264.20` | `3699.64` | -32,344.59 USD | `-2.01%` | `10X Cross` |
| `1346` | `0xe065...0f85` | `SHORT` | 1,592,022.80 USD | `1,262.61` | `1087.02` | `1264.20` | `1617.34` | -219,546.67 USD | `-13.79%` | `10X Cross` |
| `1356` | `0xf29c...9971` | `LONG` | 1,576,224.00 USD | `1,250.00` | `1245.71` | `1264.20` | `0.000000` | 19,090.68 USD | `+1.21%` | `10X Cross` |
| `1414` | `0x266b...efcb` | `LONG` | 1,518,240.00 USD | `1,200.00` | `893.76` | `1264.20` | `422.42` | 445,730.30 USD | `+29.36%` | `10X Cross` |
| `1420` | `0x5975...9abd` | `LONG` | 1,512,840.00 USD | `1,200.00` | `1179.54` | `1264.20` | `590.59` | 97,397.21 USD | `+6.44%` | `5X Cross` |
| `1434` | `0x2847...d47b` | `LONG` | 1,499,208.03 USD | `1,186.27` | `1232.07` | `1264.20` | `0.000000` | 37,639.53 USD | `+2.51%` | `5X Cross` |
| `1465` | `0x69cc...14fd` | `SHORT` | 1,464,566.24 USD | `1,161.36` | `675.33` | `1264.20` | `8156.85` | -680,260.72 USD | `-46.45%` | `10X Cross` |
| `1466` | `0x38f9...cb04` | `SHORT` | 1,461,949.56 USD | `1,155.60` | `1243.46` | `1264.20` | `2000.61` | -25,009.34 USD | `-1.71%` | `10X Cross` |
| `1477` | `0x3fc5...c0c1` | `SHORT` | 1,447,838.31 USD | `1,148.44` | `1264.34` | `1264.20` | `2915.24` | 4,175.47 USD | `+0.29%` | `10X Cross` |
| `1507` | `0xe35c...a1d3` | `LONG` | 1,421,673.48 USD | `1,127.06` | `1318.20` | `1264.20` | `694.43` | -64,021.87 USD | `-4.50%` | `2X Isolated` |
| `1519` | `0x5f94...4b96` | `LONG` | 1,409,701.28 USD | `1,115.27` | `538.00` | `1264.20` | `0.000000` | 809,683.64 USD | `+57.44%` | `10X Cross` |
| `1544` | `0x71df...a23d` | `SHORT` | 1,385,809.70 USD | `1,098.28` | `513.50` | `1264.20` | `2558.06` | -821,839.51 USD | `-59.30%` | `2X Cross` |
| `1570` | `0xbfc7...80b4` | `SHORT` | 1,355,465.67 USD | `1,075.00` | `558.03` | `1264.20` | `3029.04` | -755,586.95 USD | `-55.74%` | `10X Cross` |
| `1584` | `0x51f6...2b39` | `SHORT` | 1,329,888.69 USD | `1,051.42` | `1299.77` | `1264.20` | `2474.17` | 36,713.81 USD | `+2.76%` | `10X Cross` |
| `1634` | `0x123d...3bff` | `SHORT` | 1,277,295.56 USD | `1,009.64` | `491.08` | `1264.20` | `4403.55` | -781,477.66 USD | `-61.18%` | `10X Cross` |
| `1640` | `0x9321...d75a` | `SHORT` | 1,265,200.00 USD | `1,000.00` | `1242.18` | `1264.20` | `6318.00` | -23,016.27 USD | `-1.82%` | `10X Cross` |
| `1645` | `0x668c...ea2e` | `SHORT` | 1,261,800.00 USD | `1,000.00` | `1406.98` | `1264.20` | `4187.31` | 145,181.99 USD | `+11.51%` | `10X Cross` |
| `1648` | `0xe282...df29` | `LONG` | 1,261,000.00 USD | `1,000.00` | `420.99` | `1264.20` | `838.97` | 840,013.14 USD | `+66.61%` | `10X Cross` |
| `1671` | `0x17f0...094f` | `LONG` | 1,242,777.18 USD | `984.30` | `1287.23` | `1264.20` | `536.86` | -24,242.98 USD | `-1.95%` | `5X Cross` |
| `1746` | `0x757d...94ba` | `LONG` | 1,166,497.71 USD | `925.00` | `1558.31` | `1264.20` | `0.000000` | -274,942.88 USD | `-23.57%` | `10X Cross` |
| `1747` | `0xaa82...9556` | `LONG` | 1,165,420.34 USD | `924.13` | `1254.72` | `1264.20` | `184.67` | 5,893.67 USD | `+0.51%` | `10X Cross` |
| `1793` | `0xb911...5525` | `LONG` | 1,137,600.00 USD | `900.00` | `1294.82` | `1264.20` | `1070.38` | -27,737.82 USD | `-2.44%` | `10X Cross` |
| `1840` | `0xcf0a...856f` | `LONG` | 1,099,217.07 USD | `871.15` | `1292.19` | `1264.20` | `1007.71` | -26,477.78 USD | `-2.41%` | `4X Cross` |
| `1843` | `0xef96...9383` | `SHORT` | 1,094,903.94 USD | `868.42` | `1259.08` | `1264.20` | `5503.31` | -1,492.14 USD | `-0.14%` | `10X Cross` |
| `1868` | `0xdf95...7d72` | `SHORT` | 1,079,283.94 USD | `853.29` | `1074.39` | `1264.20` | `46075.08` | -162,515.01 USD | `-15.06%` | `10X Cross` |
| `1902` | `0x601c...4f54` | `SHORT` | 1,040,912.69 USD | `824.42` | `615.11` | `1264.20` | `3158.77` | -533,799.94 USD | `-51.28%` | `5X Cross` |
| `1914` | `0xae55...2236` | `LONG` | 1,030,893.92 USD | `817.47` | `1467.80` | `1264.20` | `0.000000` | -168,987.29 USD | `-16.39%` | `10X Cross` |
| `1949` | `0x9b0f...db40` | `LONG` | 1,012,080.00 USD | `800.00` | `1268.86` | `1264.20` | `801.80` | -3,009.76 USD | `-0.30%` | `10X Cross` |
| `1952` | `0x0f02...5384` | `LONG` | 1,009,846.52 USD | `800.78` | `1290.36` | `1264.20` | `308.98` | -23,447.55 USD | `-2.32%` | `3X Cross` |
| `1974` | `0xabdb...84ac` | `LONG` | 1,001,478.04 USD | `793.69` | `711.79` | `1264.20` | `664.43` | 436,537.68 USD | `+43.59%` | `3X Cross` |
| `1976` | `0x6e8f...4364` | `LONG` | 1,000,792.65 USD | `793.65` | `1260.00` | `1264.20` | `1019.12` | 793.65 USD | `+0.08%` | `10X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
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
| `5m` | `BALANCED` | 0.00 USD | 1,750.00 USD | 1,750.00 USD | 1,750.00 USD | `1` | `2026-10-30 02:25:00 UTC - 2026-10-30 02:30:00 UTC` |
| `15m` | `BALANCED` | 0.00 USD | 1,750.00 USD | 1,750.00 USD | 1,750.00 USD | `1` | `2026-10-30 02:15:00 UTC - 2026-10-30 02:30:00 UTC` |
| `1h` | `BALANCED` | 0.00 USD | 1,750.00 USD | 1,750.00 USD | 1,750.00 USD | `1` | `2026-10-30 02:00:00 UTC - 2026-10-30 03:00:00 UTC` |
| `4h` | `BALANCED` | 0.00 USD | 1,750.00 USD | 1,750.00 USD | 1,750.00 USD | `1` | `2026-10-30 00:00:00 UTC - 2026-10-30 04:00:00 UTC` |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `0 USD` | Total OI Tokens: `-`
  * 1h OI Change: `0.00%` | 4h OI Change: `0.00%` | 24h OI Change: `0.00%`
  * Exchange Breakdown: Binance=`-` | Bybit=`-` | OKX=`-` | Hyperliquid=`-`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `86.15K` | Last 24h: `133.88K` | Last 3d: `245.74K` | Last 7d: `771.70K`
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
| `5:00 UTC` | `1209.15` | `1203.96` | `1209.15` | `1231.05` | `1180.35` | 101,980,019.94 USD | 48,295,180.78 USD | 53,684,839.16 USD | -5,389,658.38 USD | `-5.29%` | `3B / 24S` |
| `0:00 UTC` | `1197.75` | `1211.98` | `1197.75` | `1236.15` | `1189.35` | 90,739,097.90 USD | 52,854,086.90 USD | 37,885,011.00 USD | 14,969,075.89 USD | `+16.50%` | `25B / 1S` |
| `5:00 UTC` | `1232.55` | `1227.83` | `1232.55` | `1237.35` | `1215.45` | 35,400,223.44 USD | 18,306,250.09 USD | 17,093,973.35 USD | 1,212,276.73 USD | `+3.42%` | `7B / 4S` |
| `0:00 UTC` | `1230.15` | `1232.52` | `1230.15` | `1240.05` | `1225.05` | 27,822,128.62 USD | 14,746,863.10 USD | 13,075,265.52 USD | 1,671,597.57 USD | `+6.01%` | `5B / 1S` |
| `5:00 UTC` | `1219.95` | `1220.53` | `1219.95` | `1230.45` | `1215.45` | 25,624,282.39 USD | 13,502,208.52 USD | 12,122,073.88 USD | 1,380,134.64 USD | `+5.39%` | `6B / 3S` |
| `0:00 UTC` | `1245.15` | `1232.68` | `1245.15` | `1249.05` | `1206.75` | 51,931,159.61 USD | 26,761,787.01 USD | 25,169,372.61 USD | 1,592,414.40 USD | `+3.07%` | `20B / 9S` |
| `5:00 UTC` | `1236.45` | `1237.15` | `1236.45` | `1245.15` | `1230.45` | 21,904,768.45 USD | 9,625,705.12 USD | 12,279,063.33 USD | -2,653,358.20 USD | `-12.11%` | `1B / 0S` |
| `0:00 UTC` | `1228.65` | `1236.25` | `1228.65` | `1253.25` | `1219.35` | 45,146,863.08 USD | 23,450,812.50 USD | 21,696,050.59 USD | 1,754,761.91 USD | `+3.89%` | `18B / 9S` |
| `5:00 UTC` | `1254.75` | `1256.85` | `1254.75` | `1263.45` | `1247.85` | 37,496,922.68 USD | 20,689,312.95 USD | 16,807,609.72 USD | 3,881,703.23 USD | `+10.35%` | `5B / 3S` |
| `0:00 UTC` | `1261.35` | `1262.93` | `1261.35` | `1267.65` | `1258.35` | 16,881,908.87 USD | 9,370,261.82 USD | 7,511,647.05 USD | 1,858,614.76 USD | `+11.01%` | `5B / 3S` |

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
| `5m` | 679,960.00 USD | 1,220,000.00 USD | **`ACCUMULATION`** |
| `15m` | 3,460,000.00 USD | 11,760,000.00 USD | **`ACCUMULATION`** |
| `30m` | 5,690,000.00 USD | 8,390,000.00 USD | **`ACCUMULATION`** |
| `1h` | 6,740,000.00 USD | 20,920,000.00 USD | **`ACCUMULATION`** |
| `2h` | 7,430,000.00 USD | 44,210,000.00 USD | **`ACCUMULATION`** |
| `4h` | -302,240.00 USD | 5,240,000.00 USD | **`ACCUMULATION`** |
| `6h` | -8,510,000.00 USD | 10,110,000.00 USD | **`ACCUMULATION`** |
| `8h` | -10,590,000.00 USD | -7,200,000.00 USD | **`DISTRIBUTION`** |
| `12h` | 15,370,000.00 USD | 88,240,000.00 USD | **`ACCUMULATION`** |
| `24h` | 11,270,000.00 USD | 112,790,000.00 USD | **`ACCUMULATION`** |
| `1w` | 33,820,000.00 USD | 234,780,000.00 USD | **`ACCUMULATION`** |
| `30d` | 61,520,000.00 USD | -530,100,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+679.96K` | 15m=`+3.46M` | 1h=`+6.74M` | 24h=`+11.27M`
* Futures Capital Netflows: 5m=`+1.22M` | 15m=`+11.76M` | 1h=`+20.92M` | 24h=`+112.79M`
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
  * `2026-10-30 08:00:46 IST`: [financemagnates.com] - (Sentiment: `Neutral`)
  * `2026-10-30 07:15:46 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-30 08:08:46 IST`: [kathleenhays.substack.com] - (Sentiment: `Neutral`)
  * `2026-10-30 08:07:46 IST`: [rba.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 08:07:46 IST`: [abs.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 08:07:46 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 08:07:46 IST`: [@NodeWire] - (Sentiment: `Neutral`)
  * `2026-10-30 08:07:46 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 08:07:46 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 08:07:46 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-30 05:09:46 IST`: [media.rabobank.com] - (Sentiment: `Neutral`)
  * `2026-10-30 05:09:46 IST`: [economics.td.com] - (Sentiment: `Neutral`)
  * `2026-10-30 04:09:46 IST`: [investinglive.com] - (Sentiment: `Neutral`)
  * `2026-10-30 03:09:46 IST`: [msn.com] - (Sentiment: `Neutral`)
  * `2026-10-30 03:09:46 IST`: [morningstar.com] - (Sentiment: `Neutral`)


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
  * Spread-Padded Stop Loss: `1188.00` (Risk Distance: `28.75` pts)
  * +2.5R Take Profit: `1288.61`
  * Mathematical Lot Sizing: **`0.34 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `1256.18` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `1284.93` (Risk Distance: `28.75` pts)
  * +2.5R Take Profit: `1184.32`
  * Mathematical Lot Sizing: **`0.34 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`1238.12`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
