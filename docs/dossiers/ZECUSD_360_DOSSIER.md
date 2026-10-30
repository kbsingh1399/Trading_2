# 🏛️ SOVEREIGN CANDIDATE DOSSIER: ZECUSD
**Canonical Key**: `ZECUSD` | **Broker Instrument**: `ZECUSD.p` | **Asset Class**: `Crypto Altcoin`
**Timestamp**: `2026-10-30 17:10:08 IST` (`2026-10-30 11:40:08 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `1263.09` | **Live Ask Quote**: `1264.23` | **Mid Price**: `1263.66`
- **Spread Points**: `114.00` | **Spread BPS**: `9.02 bps` (Charter Threshold: `25.00 bps`)
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
  * Value Area High (VAH) = `1278.60` (Distance: `-1.20%`)
  * Point of Control (POC) = `1247.68` (Distance: `+1.25%`)
  * Value Area Low (VAL) = `1239.95` (Distance: `+1.88%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`1309.91` | POC=`1246.71` | VAL=`1230.27`
  * Prior Day Extremes: PDH=`1396.49` | PDL=`1206.89` | PDC=`1244.38`
  * Monday Range Blueprint: High=`1267.53` | Mid=`1222.14` | Low=`1176.75`
  * Developing Weekly Value Area: Weekly VAH=`1300.54` | Weekly POC=`1240.47` | Weekly VAL=`1214.11`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`1296.00` | Low=`1180.03`
  * London Session (08:00-16:00 UTC): High=`1283.82` | Low=`1239.95`
  * New York Session (13:00-21:00 UTC): High=`1276.27` | Low=`1245.73`
  * Initial Balance (First Hour): IB High=`1283.82` | IB Low=`1264.92`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `1258.61` - `1268.71`
  * Optimal Trade Entry (OTE 0.705): `1266.19`
  * Structural Invalidation Anchor (0.786): `1273.77`

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
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 16:52:59 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `12` | `0xb83d...6e36` | `SHORT` | 66,189,041.34 USD | `52,385.47` | `1336.45` | `1262.50` | `3184.23` | 3,821,526.06 USD | `+5.77%` | `3X Cross` |
| `21` | `0x5b5d...c060` | `SHORT` | 50,749,533.56 USD | `40,121.38` | `1478.36` | `1262.50` | `4787.02` | 8,564,501.55 USD | `+16.88%` | `3X Cross` |
| `36` | `0x7fda...17d1` | `SHORT` | 33,622,218.86 USD | `26,635.68` | `1262.58` | `1262.50` | `2391.20` | 7,400.17 USD | `+0.02%` | `5X Cross` |
| `80` | `0x60b0...991e` | `LONG` | 21,201,201.49 USD | `16,779.74` | `1179.65` | `1262.50` | `914.66` | 1,406,954.48 USD | `+6.64%` | `10X Cross` |
| `141` | `0xc36a...105b` | `LONG` | 14,528,957.00 USD | `11,510.82` | `1215.14` | `1262.50` | `962.23` | 541,675.98 USD | `+3.73%` | `10X Cross` |
| `175` | `0x8742...8427` | `LONG` | 11,617,447.75 USD | `9,201.21` | `1286.37` | `1262.50` | `712.69` | -218,722.25 USD | `-1.88%` | `10X Cross` |
| `192` | `0x58b2...11f3` | `LONG` | 10,831,439.89 USD | `8,563.08` | `1246.56` | `1262.50` | `386.72` | 157,022.32 USD | `+1.45%` | `10X Cross` |
| `196` | `0x9ffd...ce40` | `LONG` | 10,690,517.38 USD | `8,451.67` | `1252.41` | `1262.50` | `600.66` | 105,536.50 USD | `+0.99%` | `5X Cross` |
| `198` | `0xad59...ba81` | `SHORT` | 10,644,987.50 USD | `8,425.00` | `330.91` | `1262.50` | `2145.72` | -7,857,029.73 USD | `-73.81%` | `10X Cross` |
| `203` | `0xdd53...2b13` | `SHORT` | 10,345,709.82 USD | `8,195.92` | `741.54` | `1262.50` | `8385.01` | -4,268,113.45 USD | `-41.25%` | `3X Cross` |
| `228` | `0x880a...311c` | `SHORT` | 9,728,684.95 USD | `7,707.11` | `1367.50` | `1262.50` | `2236.32` | 810,799.25 USD | `+8.33%` | `10X Cross` |
| `237` | `0x9071...5c0b` | `LONG` | 9,491,330.35 USD | `7,517.29` | `1353.83` | `1262.50` | `108.98` | -685,799.62 USD | `-7.23%` | `2X Cross` |
| `238` | `0xbf73...5d58` | `LONG` | 9,474,000.00 USD | `7,500.00` | `1248.78` | `1262.50` | `114.06` | 108,154.38 USD | `+1.14%` | `10X Cross` |
| `273` | `0x2b61...2f6c` | `LONG` | 8,592,476.10 USD | `6,807.00` | `1453.56` | `1262.50` | `582.50` | -1,301,875.12 USD | `-15.15%` | `10X Cross` |
| `291` | `0x2ae5...83e7` | `LONG` | 8,127,103.68 USD | `6,436.80` | `1391.82` | `1262.50` | `0.000000` | -831,788.31 USD | `-10.23%` | `1X Cross` |
| `315` | `0xecb6...2b00` | `SHORT` | 7,676,538.60 USD | `6,081.39` | `1277.42` | `1262.50` | `6570.84` | 91,948.73 USD | `+1.20%` | `5X Cross` |
| `339` | `0x26b6...9a13` | `LONG` | 6,860,627.50 USD | `5,433.73` | `1282.23` | `1262.50` | `232.67` | -106,675.74 USD | `-1.55%` | `10X Cross` |
| `351` | `0x45d2...4029` | `SHORT` | 6,599,610.20 USD | `5,227.00` | `833.44` | `1262.50` | `8906.45` | -2,243,232.23 USD | `-33.99%` | `5X Cross` |
| `366` | `0xea00...a918` | `LONG` | 6,317,500.00 USD | `5,000.00` | `739.16` | `1262.50` | `0.000000` | 2,621,684.89 USD | `+41.50%` | `5X Cross` |
| `379` | `0xdd7a...8830` | `LONG` | 6,135,989.88 USD | `4,860.19` | `897.48` | `1262.50` | `779.21` | 1,774,086.20 USD | `+28.91%` | `10X Cross` |
| `423` | `0x469e...58a5` | `SHORT` | 5,255,194.94 USD | `4,163.52` | `1242.31` | `1262.50` | `1952.78` | -82,810.29 USD | `-1.58%` | `10X Cross` |
| `425` | `0x4cae...7c34` | `LONG` | 5,241,410.42 USD | `4,152.27` | `1172.97` | `1262.50` | `985.85` | 370,916.87 USD | `+7.08%` | `10X Cross` |
| `445` | `0xd4c1...3d1d` | `SHORT` | 4,963,011.98 USD | `3,931.41` | `1291.66` | `1262.50` | `2316.65` | 115,016.84 USD | `+2.32%` | `10X Cross` |
| `448` | `0xa61c...66b9` | `LONG` | 4,907,822.40 USD | `3,888.00` | `1148.34` | `1262.50` | `0.000000` | 443,080.26 USD | `+9.03%` | `10X Cross` |
| `476` | `0x9aa5...58af` | `SHORT` | 4,696,147.31 USD | `3,720.31` | `1205.51` | `1262.50` | `3635.54` | -211,260.51 USD | `-4.50%` | `10X Cross` |
| `477` | `0x0153...8052` | `SHORT` | 4,668,472.97 USD | `3,698.18` | `1307.82` | `1262.50` | `2504.97` | 168,097.78 USD | `+3.60%` | `1X Isolated` |
| `512` | `0xb122...e4ba` | `LONG` | 4,420,126.18 USD | `3,498.47` | `1265.25` | `1262.50` | `1058.88` | -6,325.35 USD | `-0.14%` | `10X Cross` |
| `543` | `0xd21d...90f1` | `LONG` | 4,106,375.00 USD | `3,250.00` | `1253.64` | `1262.50` | `876.19` | 32,033.27 USD | `+0.78%` | `4X Isolated` |
| `555` | `0x456f...cdf1` | `LONG` | 4,037,716.41 USD | `3,195.66` | `1267.53` | `1262.50` | `508.40` | -12,879.40 USD | `-0.32%` | `10X Cross` |
| `556` | `0x382b...3e39` | `LONG` | 4,025,272.73 USD | `3,188.84` | `1220.72` | `1262.50` | `0.000000` | 132,596.98 USD | `+3.29%` | `10X Cross` |
| `563` | `0x1338...c48e` | `LONG` | 3,975,840.43 USD | `3,149.43` | `1018.52` | `1262.50` | `820.49` | 768,094.89 USD | `+19.32%` | `4X Isolated` |
| `578` | `0xdbe0...d6d5` | `LONG` | 3,894,879.76 USD | `3,085.37` | `422.97` | `1262.50` | `338.80` | 2,589,875.27 USD | `+66.49%` | `3X Isolated` |
| `600` | `0x325e...9564` | `LONG` | 3,788,048.69 USD | `3,000.91` | `1298.07` | `1262.50` | `132.72` | -107,356.47 USD | `-2.83%` | `10X Cross` |
| `602` | `0x9c06...0560` | `SHORT` | 3,782,993.94 USD | `2,989.80` | `786.00` | `1262.50` | `2528.27` | -1,432,998.94 USD | `-37.88%` | `10X Cross` |
| `603` | `0x2e30...4cb5` | `SHORT` | 3,772,934.78 USD | `2,988.77` | `1282.25` | `1262.50` | `2887.84` | 59,414.87 USD | `+1.57%` | `2X Cross` |
| `613` | `0x27c9...d65d` | `SHORT` | 3,712,213.54 USD | `2,938.04` | `1254.41` | `1262.50` | `1727.15` | -26,703.50 USD | `-0.72%` | `10X Cross` |
| `704` | `0xa183...0482` | `LONG` | 3,198,668.20 USD | `2,534.00` | `530.25` | `1262.50` | `444.73` | 1,855,005.48 USD | `+57.99%` | `5X Isolated` |
| `705` | `0xac48...3201` | `LONG` | 3,198,550.25 USD | `2,531.50` | `1378.58` | `1262.50` | `562.68` | -291,322.03 USD | `-9.11%` | `10X Cross` |
| `715` | `0x9e2c...5508` | `LONG` | 3,157,000.00 USD | `2,500.00` | `1275.77` | `1262.50` | `456.52` | -32,425.91 USD | `-1.03%` | `10X Cross` |
| `716` | `0x0871...e927` | `LONG` | 3,155,750.00 USD | `2,500.00` | `1276.50` | `1262.50` | `0.000000` | -35,500.00 USD | `-1.12%` | `10X Cross` |
| `727` | `0x9b86...6e6e` | `LONG` | 3,115,581.84 USD | `2,463.30` | `637.58` | `1262.50` | `882.66` | 1,545,032.56 USD | `+49.59%` | `3X Cross` |
| `779` | `0x71d0...8c26` | `SHORT` | 2,945,375.08 USD | `2,333.34` | `1268.47` | `1262.50` | `3595.79` | 14,406.59 USD | `+0.49%` | `10X Cross` |
| `814` | `0xf48f...10fe` | `LONG` | 2,805,502.45 USD | `2,218.49` | `1517.87` | `1262.50` | `978.60` | -561,884.37 USD | `-20.03%` | `3X Cross` |
| `842` | `0x5bc4...3b0c` | `SHORT` | 2,689,633.10 USD | `2,130.74` | `1089.65` | `1262.50` | `3671.37` | -367,875.52 USD | `-13.68%` | `5X Cross` |
| `856` | `0x8de4...b9aa` | `SHORT` | 2,642,972.30 USD | `2,091.29` | `1331.35` | `1262.50` | `1690.09` | 141,267.40 USD | `+5.35%` | `3X Cross` |
| `862` | `0x4fe2...ac59` | `SHORT` | 2,622,607.62 USD | `2,071.57` | `1478.56` | `1262.50` | `1829.55` | 440,338.59 USD | `+16.79%` | `10X Cross` |
| `868` | `0xdf57...93f5` | `LONG` | 2,593,206.00 USD | `2,054.35` | `1227.36` | `1262.50` | `897.43` | 71,783.96 USD | `+2.77%` | `4X Isolated` |
| `874` | `0xbcd4...0dd2` | `LONG` | 2,568,027.39 USD | `2,033.92` | `1228.20` | `1262.50` | `786.98` | 69,976.58 USD | `+2.72%` | `10X Cross` |
| `880` | `0x9a99...d21a` | `LONG` | 2,526,891.00 USD | `2,000.00` | `1278.44` | `1262.50` | `0.000000` | -29,982.67 USD | `-1.19%` | `10X Cross` |
| `882` | `0xf29c...9971` | `LONG` | 2,524,600.00 USD | `2,000.00` | `1254.95` | `1262.50` | `0.000000` | 14,702.93 USD | `+0.58%` | `10X Cross` |
| `906` | `0x77ee...2902` | `SHORT` | 2,456,473.67 USD | `1,946.03` | `759.84` | `1262.50` | `5675.29` | -977,796.16 USD | `-39.80%` | `10X Cross` |
| `918` | `0x3e2f...b269` | `SHORT` | 2,430,571.27 USD | `1,925.51` | `1134.87` | `1262.50` | `2977.36` | -245,372.42 USD | `-10.10%` | `10X Cross` |
| `926` | `0x5323...b23c` | `SHORT` | 2,405,779.70 USD | `1,905.87` | `1270.60` | `1262.50` | `4111.90` | 15,821.07 USD | `+0.66%` | `5X Cross` |
| `929` | `0x4f12...618b` | `SHORT` | 2,398,604.57 USD | `1,896.28` | `1608.30` | `1262.50` | `2116.98` | 651,179.82 USD | `+27.15%` | `3X Cross` |
| `938` | `0x039c...0ebd` | `SHORT` | 2,364,452.00 USD | `1,873.13` | `1250.08` | `1262.50` | `3290.51` | -22,884.45 USD | `-0.97%` | `10X Cross` |
| `974` | `0x866d...d6e1` | `LONG` | 2,274,727.71 USD | `1,802.05` | `674.73` | `1262.50` | `102.81` | 1,058,826.40 USD | `+46.55%` | `10X Cross` |
| `997` | `0x2309...a2d9` | `LONG` | 2,209,317.01 USD | `1,750.37` | `1186.09` | `1262.50` | `808.60` | 133,222.90 USD | `+6.03%` | `8X Cross` |
| `1030` | `0x265e...7f70` | `LONG` | 2,087,469.01 USD | `1,651.74` | `1382.98` | `1262.50` | `0.000000` | -196,853.75 USD | `-9.43%` | `3X Cross` |
| `1037` | `0xfe7c...b7ae` | `SHORT` | 2,073,504.47 USD | `1,642.64` | `1346.92` | `1262.50` | `5607.47` | 139,004.15 USD | `+6.70%` | `10X Cross` |
| `1044` | `0x3e47...aaf6` | `LONG` | 2,067,439.78 USD | `1,636.28` | `1278.38` | `1262.50` | `1046.42` | -24,352.01 USD | `-1.18%` | `10X Cross` |
| `1045` | `0x2edd...8179` | `SHORT` | 2,065,097.55 USD | `1,635.98` | `1261.55` | `1262.50` | `2851.01` | -1,234.67 USD | `-0.06%` | `10X Cross` |
| `1066` | `0x7f75...9edf` | `LONG` | 2,040,482.70 USD | `1,616.48` | `1200.45` | `1262.50` | `989.89` | 99,978.23 USD | `+4.90%` | `10X Cross` |
| `1067` | `0x3205...40bb` | `SHORT` | 2,032,315.35 USD | `1,609.92` | `1262.15` | `1262.50` | `2153.99` | -360.44 USD | `-0.02%` | `10X Cross` |
| `1070` | `0xfc27...9d9d` | `SHORT` | 2,026,018.46 USD | `1,604.64` | `1295.09` | `1262.50` | `12761.04` | 52,127.34 USD | `+2.57%` | `10X Cross` |
| `1075` | `0x6646...6de5` | `SHORT` | 2,019,840.00 USD | `1,600.00` | `660.64` | `1262.50` | `4308.27` | -962,815.03 USD | `-47.67%` | `10X Cross` |
| `1083` | `0x023a...2355` | `SHORT` | 2,012,156.69 USD | `1,594.04` | `1309.94` | `1262.50` | `4427.11` | 75,937.56 USD | `+3.77%` | `10X Cross` |
| `1100` | `0xab59...59b5` | `LONG` | 1,977,781.82 USD | `1,565.32` | `1342.15` | `1262.50` | `836.46` | -123,113.40 USD | `-6.22%` | `10X Cross` |
| `1160` | `0xcf67...eb24` | `LONG` | 1,895,168.25 USD | `1,500.00` | `887.05` | `1262.50` | `607.50` | 564,596.88 USD | `+29.79%` | `10X Cross` |
| `1180` | `0x7277...0b98` | `SHORT` | 1,862,813.98 USD | `1,475.73` | `1287.86` | `1262.50` | `2179.28` | 37,718.14 USD | `+2.02%` | `10X Cross` |
| `1242` | `0x926a...af36` | `LONG` | 1,769,340.66 USD | `1,401.68` | `1254.50` | `1262.50` | `1187.95` | 10,938.76 USD | `+0.62%` | `10X Isolated` |
| `1244` | `0x2ab7...c2f8` | `LONG` | 1,768,283.93 USD | `1,400.51` | `813.26` | `1262.50` | `790.08` | 629,302.24 USD | `+35.59%` | `3X Cross` |
| `1265` | `0x11be...8b1d` | `LONG` | 1,738,361.21 USD | `1,375.83` | `1206.55` | `1262.50` | `1134.71` | 78,353.25 USD | `+4.51%` | `10X Isolated` |
| `1306` | `0xdf83...3cff` | `SHORT` | 1,657,225.63 USD | `1,312.55` | `1260.71` | `1262.50` | `1862.06` | -2,482.07 USD | `-0.15%` | `10X Cross` |
| `1318` | `0xef96...9383` | `SHORT` | 1,639,181.56 USD | `1,297.39` | `1262.03` | `1262.50` | `3895.83` | -1,839.61 USD | `-0.11%` | `10X Cross` |
| `1346` | `0xe065...0f85` | `SHORT` | 1,595,238.92 USD | `1,262.61` | `1087.02` | `1262.50` | `1551.31` | -222,762.80 USD | `-13.96%` | `10X Cross` |
| `1360` | `0x413c...886c` | `LONG` | 1,579,375.00 USD | `1,250.00` | `1237.51` | `1262.50` | `0.000000` | 32,485.54 USD | `+2.06%` | `10X Cross` |
| `1414` | `0x2847...d47b` | `LONG` | 1,529,541.53 USD | `1,211.71` | `1232.45` | `1262.50` | `0.000000` | 36,173.93 USD | `+2.37%` | `5X Cross` |
| `1427` | `0x5975...9abd` | `LONG` | 1,517,640.00 USD | `1,200.00` | `1179.54` | `1262.50` | `516.15` | 102,197.21 USD | `+6.73%` | `5X Cross` |
| `1431` | `0x266b...efcb` | `LONG` | 1,514,880.00 USD | `1,200.00` | `893.76` | `1262.50` | `393.42` | 442,370.30 USD | `+29.20%` | `10X Cross` |
| `1459` | `0xb897...ebc1` | `SHORT` | 1,481,736.86 USD | `1,173.56` | `1256.04` | `1262.50` | `1350.13` | -7,693.57 USD | `-0.52%` | `10X Cross` |
| `1469` | `0x69cc...14fd` | `SHORT` | 1,465,984.73 USD | `1,161.36` | `675.33` | `1262.50` | `7986.93` | -681,679.20 USD | `-46.50%` | `10X Cross` |
| `1483` | `0x3fc5...c0c1` | `SHORT` | 1,452,776.60 USD | `1,148.44` | `1264.34` | `1262.50` | `2743.01` | -762.82 USD | `-0.05%` | `10X Cross` |
| `1525` | `0x5f94...4b96` | `LONG` | 1,409,143.65 USD | `1,115.27` | `538.00` | `1262.50` | `0.000000` | 809,126.01 USD | `+57.42%` | `10X Cross` |
| `1538` | `0xe35c...a1d3` | `LONG` | 1,402,869.73 USD | `1,111.36` | `1311.66` | `1262.50` | `691.00` | -54,854.42 USD | `-3.91%` | `2X Isolated` |
| `1539` | `0xfc66...ca06` | `SHORT` | 1,401,935.63 USD | `1,110.62` | `1272.72` | `1262.50` | `24432.03` | 11,575.69 USD | `+0.83%` | `10X Cross` |
| `1558` | `0x71df...a23d` | `SHORT` | 1,386,358.84 USD | `1,098.28` | `513.50` | `1262.50` | `2559.66` | -822,388.65 USD | `-59.32%` | `2X Cross` |
| `1583` | `0xbfc7...80b4` | `SHORT` | 1,356,865.00 USD | `1,075.00` | `558.03` | `1262.50` | `2659.41` | -756,986.27 USD | `-55.79%` | `10X Cross` |
| `1586` | `0x8b9d...7b28` | `SHORT` | 1,351,519.36 USD | `1,070.68` | `1272.16` | `1262.50` | `3321.88` | 10,558.88 USD | `+0.78%` | `10X Cross` |
| `1609` | `0x123d...3bff` | `SHORT` | 1,320,776.80 USD | `1,044.34` | `519.62` | `1262.50` | `4154.32` | -778,118.59 USD | `-58.91%` | `10X Cross` |
| `1616` | `0x38f9...cb04` | `SHORT` | 1,309,909.62 USD | `1,037.47` | `1259.78` | `1262.50` | `2096.33` | -2,927.00 USD | `-0.22%` | `10X Cross` |
| `1668` | `0x8ab1...15ef` | `LONG` | 1,263,800.00 USD | `1,000.00` | `1275.75` | `1262.50` | `984.06` | -11,954.92 USD | `-0.95%` | `10X Cross` |
| `1669` | `0x98e0...d7e0` | `LONG` | 1,262,600.00 USD | `1,000.00` | `1276.62` | `1262.50` | `934.10` | -14,022.14 USD | `-1.11%` | `10X Cross` |
| `1670` | `0xe282...df29` | `LONG` | 1,262,500.00 USD | `1,000.00` | `420.99` | `1262.50` | `796.01` | 841,513.14 USD | `+66.65%` | `10X Cross` |
| `1671` | `0x668c...ea2e` | `SHORT` | 1,262,200.00 USD | `1,000.00` | `1406.98` | `1262.50` | `4212.14` | 144,781.99 USD | `+11.47%` | `10X Cross` |
| `1700` | `0x17f0...094f` | `LONG` | 1,242,481.89 USD | `984.30` | `1287.23` | `1262.50` | `537.06` | -24,538.27 USD | `-1.97%` | `5X Cross` |
| `1727` | `0x51f6...2b39` | `SHORT` | 1,217,487.30 USD | `964.27` | `1299.77` | `1262.50` | `2504.72` | 35,840.38 USD | `+2.94%` | `10X Cross` |
| `1736` | `0x4e23...20c3` | `LONG` | 1,207,427.82 USD | `956.53` | `1265.15` | `1262.50` | `0.000000` | -2,723.62 USD | `-0.23%` | `4X Cross` |
| `1751` | `0xf096...7553` | `SHORT` | 1,188,266.98 USD | `940.68` | `1257.96` | `1262.50` | `3090.41` | -4,933.26 USD | `-0.42%` | `10X Cross` |
| `1774` | `0x757d...94ba` | `LONG` | 1,167,627.50 USD | `925.00` | `1558.31` | `1262.50` | `0.000000` | -273,813.09 USD | `-23.45%` | `10X Cross` |
| `1819` | `0xb911...5525` | `LONG` | 1,137,150.00 USD | `900.00` | `1294.82` | `1262.50` | `1035.49` | -28,187.82 USD | `-2.48%` | `10X Cross` |
| `1869` | `0xcf0a...856f` | `LONG` | 1,100,175.33 USD | `871.15` | `1292.19` | `1262.50` | `1028.35` | -25,519.51 USD | `-2.32%` | `4X Cross` |
| `1890` | `0xdf95...7d72` | `SHORT` | 1,077,288.20 USD | `853.23` | `1074.39` | `1262.50` | `44659.55` | -160,583.73 USD | `-14.91%` | `10X Cross` |
| `1918` | `0xb2f7...af9f` | `SHORT` | 1,049,614.72 USD | `830.72` | `746.63` | `1262.50` | `8174.97` | -429,375.69 USD | `-40.91%` | `10X Cross` |
| `1932` | `0x601c...4f54` | `SHORT` | 1,040,747.81 USD | `824.42` | `615.11` | `1262.50` | `3126.97` | -533,635.06 USD | `-51.27%` | `5X Cross` |
| `1941` | `0x8b61...c0c2` | `LONG` | 1,035,055.77 USD | `818.42` | `1274.67` | `1262.50` | `1005.21` | -8,158.27 USD | `-0.79%` | `4X Isolated` |
| `1949` | `0xae55...2236` | `LONG` | 1,032,137.62 USD | `817.47` | `1467.80` | `1262.50` | `0.000000` | -167,743.60 USD | `-16.25%` | `10X Cross` |
| `1988` | `0x0f02...5384` | `LONG` | 1,010,824.59 USD | `800.78` | `1290.36` | `1262.50` | `297.87` | -22,469.47 USD | `-2.22%` | `3X Cross` |
| `1991` | `0x9b0f...db40` | `LONG` | 1,009,896.32 USD | `800.00` | `1268.86` | `1262.50` | `799.43` | -5,193.44 USD | `-0.51%` | `10X Cross` |
| `2007` | `0x6e8f...4364` | `LONG` | 1,001,824.40 USD | `793.65` | `1260.00` | `1262.50` | `905.78` | 1,825.39 USD | `+0.18%` | `10X Cross` |
| `2008` | `0xabdb...84ac` | `LONG` | 1,001,795.52 USD | `793.69` | `711.79` | `1262.50` | `664.63` | 436,855.16 USD | `+43.61%` | `3X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `1017.00` | 10.17 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Long: 0.01K USD at 1017.0000 USD [API] | `2026-09-04 08:53:37` |
| `ANNOUNCEMENT` | `INFO` | `1327.50` | 13.28 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Long: 0.01K USD at 1327.5000 USD [API] | `2026-10-29 15:31:54` |
| `ANNOUNCEMENT` | `INFO` | `1327.50` | 61,343.78 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Long: 61.34K USD at 1327.5000 USD [API] | `2026-10-29 15:31:54` |
| `ANNOUNCEMENT` | `INFO` | `1319.10` | 10,420.89 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 10.42K USD at 1319.1000 USD [API] | `2026-10-29 18:31:05` |
| `ANNOUNCEMENT` | `INFO` | `1304.20` | 2,373.64 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 2.37K USD at 1304.2000 USD [API] | `2026-10-29 20:03:49` |
| `ANNOUNCEMENT` | `INFO` | `1304.20` | 899.90 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 0.90K USD at 1304.2000 USD [API] | `2026-10-29 20:03:49` |
| `ANNOUNCEMENT` | `INFO` | `1362.30` | 449.56 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Long: 0.45K USD at 1362.3000 USD [API] | `2026-10-29 15:57:56` |
| `ANNOUNCEMENT` | `INFO` | `1362.30` | 54.49 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Long: 0.05K USD at 1362.3000 USD [API] | `2026-10-29 15:57:56` |
| `ANNOUNCEMENT` | `INFO` | `1362.30` | 762.89 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Long: 0.76K USD at 1362.3000 USD [API] | `2026-10-29 15:57:56` |
| `ANNOUNCEMENT` | `INFO` | `1303.60` | 13,505.30 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 13.51K USD at 1303.6000 USD [API] | `2026-10-29 20:03:47` |
| `ANNOUNCEMENT` | `INFO` | `1303.60` | 495.37 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 0.50K USD at 1303.6000 USD [API] | `2026-10-29 20:03:47` |
| `ANNOUNCEMENT` | `INFO` | `1304.00` | 495.52 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 0.50K USD at 1304.0000 USD [API] | `2026-10-29 20:03:47` |
| `ANNOUNCEMENT` | `INFO` | `1282.60` | 115.43 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 0.12K USD at 1282.6000 USD [API] | `2026-10-29 20:35:42` |
| `ANNOUNCEMENT` | `INFO` | `1282.70` | 64.14 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 0.06K USD at 1282.7000 USD [API] | `2026-10-29 20:35:42` |
| `ANNOUNCEMENT` | `INFO` | `1283.60` | 115.52 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 0.12K USD at 1283.6000 USD [API] | `2026-10-29 20:35:36` |


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
| `5m` | `BALANCED` | 0.00 USD | 1,750.00 USD | 1,750.00 USD | 1,750.00 USD | `1` | `2026-10-30 11:20:00 UTC - 2026-10-30 11:25:00 UTC` |
| `15m` | `BALANCED` | 0.00 USD | 1,750.00 USD | 1,750.00 USD | 1,750.00 USD | `1` | `2026-10-30 11:15:00 UTC - 2026-10-30 11:30:00 UTC` |
| `1h` | `BALANCED` | 0.00 USD | 1,750.00 USD | 1,750.00 USD | 1,750.00 USD | `1` | `2026-10-30 11:00:00 UTC - 2026-10-30 12:00:00 UTC` |
| `4h` | `BALANCED` | 0.00 USD | 1,750.00 USD | 1,750.00 USD | 1,750.00 USD | `1` | `2026-10-30 08:00:00 UTC - 2026-10-30 12:00:00 UTC` |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `0 USD` | Total OI Tokens: `-`
  * 1h OI Change: `0.00%` | 4h OI Change: `0.00%` | 24h OI Change: `0.00%`
  * Exchange Breakdown: Binance=`-` | Bybit=`-` | OKX=`-` | Hyperliquid=`-`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `85.01K` | Last 24h: `171.90K` | Last 3d: `285.15K` | Last 7d: `847.79K`
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
| `0:00 UTC` | `1244.55` | `1245.81` | `1244.55` | `1249.05` | `1243.65` | 9,717,386.64 USD | 3,914,194.68 USD | 5,803,191.96 USD | -1,888,997.28 USD | `-19.44%` | `0B / 1S` |
| `5:00 UTC` | `1242.15` | `1244.40` | `1242.15` | `1249.35` | `1241.25` | 8,638,502.97 USD | 4,533,952.89 USD | 4,104,550.08 USD | 429,402.82 USD | `+4.97%` | `4B / 2S` |
| `0:00 UTC` | `1251.15` | `1247.35` | `1251.15` | `1251.75` | `1240.05` | 9,977,652.60 USD | 4,992,881.35 USD | 4,984,771.25 USD | 8,110.10 USD | `+0.08%` | `3B / 5S` |
| `5:00 UTC` | `1243.95` | `1249.40` | `1243.95` | `1256.55` | `1243.35` | 15,678,426.53 USD | 9,268,825.46 USD | 6,409,601.07 USD | 2,859,224.38 USD | `+18.24%` | `10B / 2S` |
| `0:00 UTC` | `1249.95` | `1250.19` | `1249.95` | `1256.25` | `1246.35` | 11,248,393.80 USD | 4,953,252.73 USD | 6,295,141.07 USD | -1,341,888.34 USD | `-11.93%` | `1B / 7S` |
| `5:00 UTC` | `1263.15` | `1259.85` | `1263.15` | `1266.15` | `1247.85` | 19,587,954.68 USD | 10,529,516.42 USD | 9,058,438.26 USD | 1,471,078.16 USD | `+7.51%` | `10B / 4S` |
| `0:00 UTC` | `1272.15` | `1270.75` | `1272.15` | `1276.65` | `1262.25` | 28,700,563.02 USD | 14,735,645.79 USD | 13,964,917.22 USD | 770,728.57 USD | `+2.69%` | `10B / 0S` |
| `5:00 UTC` | `1267.95` | `1266.37` | `1267.95` | `1276.95` | `1257.75` | 25,317,311.22 USD | 15,013,433.04 USD | 10,303,878.19 USD | 4,709,554.85 USD | `+18.60%` | `12B / 5S` |
| `0:00 UTC` | `1270.05` | `1270.22` | `1270.05` | `1276.65` | `1264.05` | 13,074,018.65 USD | 5,810,348.90 USD | 7,263,669.75 USD | -1,453,320.86 USD | `-11.12%` | `2B / 4S` |
| `5:00 UTC` | `1263.15` | `1263.09` | `1263.15` | `1266.75` | `1259.55` | 7,424,461.24 USD | 3,284,480.41 USD | 4,139,980.83 USD | -855,500.43 USD | `-11.52%` | `1B / 9S` |

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
| `5m` | 82,740.00 USD | -1,370,000.00 USD | **`DISTRIBUTION`** |
| `15m` | -583,050.00 USD | -2,380,000.00 USD | **`DISTRIBUTION`** |
| `30m` | -480,030.00 USD | 3,540,000.00 USD | **`ACCUMULATION`** |
| `1h` | -1,130,000.00 USD | 7,280,000.00 USD | **`ACCUMULATION`** |
| `2h` | -2,390,000.00 USD | 10,750,000.00 USD | **`ACCUMULATION`** |
| `4h` | -882,470.00 USD | -4,010,000.00 USD | **`DISTRIBUTION`** |
| `6h` | -483,030.00 USD | -14,720,000.00 USD | **`DISTRIBUTION`** |
| `8h` | -1,720,000.00 USD | -15,870,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -520,410.00 USD | -8,730,000.00 USD | **`DISTRIBUTION`** |
| `24h` | 20,020,000.00 USD | 77,540,000.00 USD | **`ACCUMULATION`** |
| `1w` | 36,770,000.00 USD | 224,910,000.00 USD | **`ACCUMULATION`** |
| `30d` | 61,360,000.00 USD | -567,570,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+82.74K` | 15m=`-583.05K` | 1h=`-1.13M` | 24h=`+20.02M`
* Futures Capital Netflows: 5m=`-1.37M` | 15m=`-2.38M` | 1h=`+7.28M` | 24h=`+77.54M`
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
  * `2026-10-30 16:36:03 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 16:26:03 IST`: [marctomarket.com] - (Sentiment: `Neutral`)
  * `2026-10-30 15:50:03 IST`: [istat.it] - (Sentiment: `Neutral`)
  * `2026-10-30 16:48:03 IST`: [ec.europa.eu] - (Sentiment: `Neutral`)
  * `2026-10-30 16:48:03 IST`: [ec.europa.eu] - (Sentiment: `Neutral`)
  * `2026-10-30 16:48:03 IST`: [dailyforex.com] - (Sentiment: `Neutral`)
  * `2026-10-30 16:48:03 IST`: [breakingthenews.net] - (Sentiment: `Neutral`)
  * `2026-10-30 16:47:03 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 16:47:03 IST`: [@FirstSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 16:47:03 IST`: [destatis.de] - (Sentiment: `Neutral`)
  * `2026-10-30 16:47:03 IST`: [istat.it] - (Sentiment: `Neutral`)
  * `2026-10-30 16:47:03 IST`: [channelnewsasia.com] - (Sentiment: `Neutral`)
  * `2026-10-30 16:47:03 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 16:47:03 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 13:49:03 IST`: [kof.ethz.ch] - (Sentiment: `Neutral`)


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
  * Spread-Padded Stop Loss: `1212.84` (Risk Distance: `27.11` pts)
  * +2.5R Take Profit: `1307.74`
  * Mathematical Lot Sizing: **`0.36 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `1278.60` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `1305.71` (Risk Distance: `27.11` pts)
  * +2.5R Take Profit: `1210.81`
  * Mathematical Lot Sizing: **`0.36 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`1273.77`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
