# 🏛️ SOVEREIGN CANDIDATE DOSSIER: ZECUSD
**Canonical Key**: `ZECUSD` | **Broker Instrument**: `ZECUSD.p` | **Asset Class**: `Crypto Altcoin`
**Timestamp**: `2026-10-30 09:37:21 IST` (`2026-10-30 04:07:21 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `1269.92` | **Live Ask Quote**: `1270.85` | **Mid Price**: `1270.38`
- **Spread Points**: `93.00` | **Spread BPS**: `7.32 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `1241.72` | VWAP Z-Score: `+1.61` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `19.33` (Volatility Regime: `HIGH_EXPANSION`)
  * 14-Period RSI: `57.43` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `1310.20` | Lower -3.00σ Band: `1173.23`
  * Upper +2.51σ Band: `1299.02` | Lower -2.51σ Band: `1184.42`
  * Upper +2.01σ Band: `1287.60` | Lower -2.01σ Band: `1195.83`
  * Upper +2.00σ Band: `1287.38` | Lower -2.00σ Band: `1196.06`
  * Upper +1.28σ Band: `1270.94` | Lower -1.28σ Band: `1212.50`
  * Upper +1.00σ Band: `1264.55` | Lower -1.00σ Band: `1218.89`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`1264.27` | EMA-20=`1257.20` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`1265.58` (Slope: `+0.0000`) | EMA-100=`1272.19`
  * Institutional Anchors: EMA-144=`1273.66` | EMA-200=`1274.65` (Slope: `-0.1942`) | EMA-233=`1277.28`
- **Range Boundaries**: 24H High=`1396.49` | 24H Low=`1180.03` | Weekly High=`1396.49` | Weekly Low=`1180.03`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `1267.01` (Distance: `+0.20%`)
  * Point of Control (POC) = `1229.90` (Distance: `+3.22%`)
  * Value Area Low (VAL) = `1222.17` (Distance: `+3.87%`)
  * Auction Positioning: `ABOVE_VALUE (Imbalance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `RANGE_EXPANSION`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`1309.91` | POC=`1246.71` | VAL=`1230.27`
  * Prior Day Extremes: PDH=`1396.49` | PDL=`1206.89` | PDC=`1244.38`
  * Monday Range Blueprint: High=`1267.53` | Mid=`1222.14` | Low=`1176.75`
  * Developing Weekly Value Area: Weekly VAH=`1296.14` | Weekly POC=`1239.01` | Weekly VAL=`1200.92`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`1296.00` | Low=`1180.03`
  * London Session (08:00-16:00 UTC): High=`1275.47` | Low=`1265.30`
  * New York Session (13:00-21:00 UTC): High=`1278.01` | Low=`1262.76`
  * Initial Balance (First Hour): IB High=`1274.20` | IB Low=`1266.57`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `1265.30` - `1275.47`
  * Optimal Trade Entry (OTE 0.705): `1272.93`
  * Structural Invalidation Anchor (0.786): `1280.55`

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
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 09:33:32 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `13` | `0xb83d...6e36` | `SHORT` | 66,466,684.34 USD | `52,385.47` | `1336.45` | `1267.21` | `3753.06` | 3,543,883.06 USD | `+5.33%` | `3X Cross` |
| `22` | `0x5b5d...c060` | `SHORT` | 50,877,921.98 USD | `40,121.38` | `1478.36` | `1267.21` | `5213.58` | 8,436,113.13 USD | `+16.58%` | `3X Cross` |
| `39` | `0x7fda...17d1` | `SHORT` | 31,916,238.25 USD | `25,168.55` | `1261.92` | `1267.21` | `2693.01` | -155,547.24 USD | `-0.49%` | `5X Cross` |
| `81` | `0x60b0...991e` | `LONG` | 21,288,456.14 USD | `16,779.74` | `1179.65` | `1267.21` | `933.09` | 1,494,209.12 USD | `+7.02%` | `10X Cross` |
| `136` | `0xc36a...105b` | `LONG` | 14,622,194.65 USD | `11,510.82` | `1215.14` | `1267.21` | `968.00` | 634,913.62 USD | `+4.34%` | `10X Cross` |
| `152` | `0x9071...5c0b` | `LONG` | 13,324,791.17 USD | `10,517.29` | `1353.83` | `1267.21` | `0.1437` | -913,827.70 USD | `-6.86%` | `1X Cross` |
| `177` | `0x8742...8427` | `LONG` | 11,657,394.80 USD | `9,201.21` | `1286.37` | `1267.21` | `707.84` | -178,775.19 USD | `-1.53%` | `10X Cross` |
| `190` | `0x58b2...11f3` | `LONG` | 10,862,266.98 USD | `8,563.08` | `1246.56` | `1267.21` | `382.59` | 187,849.41 USD | `+1.73%` | `10X Cross` |
| `195` | `0xad59...ba81` | `SHORT` | 10,706,490.00 USD | `8,425.00` | `330.91` | `1267.21` | `2145.52` | -7,918,532.23 USD | `-73.96%` | `10X Cross` |
| `196` | `0x9ffd...ce40` | `LONG` | 10,687,393.42 USD | `8,434.77` | `1251.19` | `1267.21` | `602.48` | 133,886.96 USD | `+1.25%` | `5X Cross` |
| `204` | `0xdd53...2b13` | `SHORT` | 10,385,050.23 USD | `8,195.92` | `741.54` | `1267.21` | `8697.69` | -4,307,453.87 USD | `-41.48%` | `3X Cross` |
| `222` | `0x880a...311c` | `SHORT` | 9,765,679.08 USD | `7,707.11` | `1367.50` | `1267.21` | `2249.58` | 773,805.12 USD | `+7.92%` | `10X Cross` |
| `235` | `0xbf73...5d58` | `LONG` | 9,528,750.00 USD | `7,500.00` | `1248.78` | `1267.21` | `130.25` | 162,904.38 USD | `+1.71%` | `10X Cross` |
| `266` | `0x2b61...2f6c` | `LONG` | 8,631,956.70 USD | `6,807.00` | `1453.56` | `1267.21` | `556.43` | -1,262,394.52 USD | `-14.62%` | `10X Cross` |
| `285` | `0x2ae5...83e7` | `LONG` | 8,155,049.05 USD | `6,436.80` | `1391.82` | `1267.21` | `0.000000` | -803,842.94 USD | `-9.86%` | `1X Cross` |
| `331` | `0x26b6...9a13` | `LONG` | 6,884,883.67 USD | `5,433.73` | `1282.23` | `1267.21` | `227.04` | -82,419.57 USD | `-1.20%` | `10X Cross` |
| `344` | `0x45d2...4029` | `SHORT` | 6,622,303.22 USD | `5,227.00` | `833.44` | `1267.21` | `9129.89` | -2,265,925.25 USD | `-34.22%` | `5X Cross` |
| `358` | `0xea00...a918` | `LONG` | 6,343,500.00 USD | `5,000.00` | `739.16` | `1267.21` | `0.000000` | 2,647,684.89 USD | `+41.74%` | `5X Cross` |
| `359` | `0xecb6...2b00` | `SHORT` | 6,309,063.80 USD | `4,975.21` | `1278.98` | `1267.21` | `6361.88` | 54,153.96 USD | `+0.86%` | `5X Cross` |
| `373` | `0xdd7a...8830` | `LONG` | 6,166,609.07 USD | `4,860.19` | `897.48` | `1267.21` | `787.88` | 1,804,705.40 USD | `+29.27%` | `10X Cross` |
| `416` | `0x469e...58a5` | `SHORT` | 5,312,651.52 USD | `4,163.52` | `1242.31` | `1267.21` | `1969.17` | -140,266.86 USD | `-2.64%` | `10X Cross` |
| `429` | `0x4cae...7c34` | `LONG` | 5,075,278.59 USD | `4,002.27` | `1169.72` | `1267.21` | `1002.85` | 393,729.24 USD | `+7.76%` | `10X Cross` |
| `438` | `0xa61c...66b9` | `LONG` | 4,936,204.80 USD | `3,888.00` | `1148.34` | `1267.21` | `0.000000` | 471,462.66 USD | `+9.55%` | `10X Cross` |
| `464` | `0x9aa5...58af` | `SHORT` | 4,714,004.80 USD | `3,720.31` | `1205.51` | `1267.21` | `3710.31` | -229,118.00 USD | `-4.86%` | `10X Cross` |
| `468` | `0x0153...8052` | `SHORT` | 4,686,333.70 USD | `3,698.18` | `1307.82` | `1267.21` | `2504.85` | 150,237.05 USD | `+3.21%` | `1X Isolated` |
| `528` | `0x382b...3e39` | `LONG` | 4,189,485.38 USD | `3,303.75` | `1215.08` | `1267.21` | `0.000000` | 175,165.99 USD | `+4.18%` | `10X Cross` |
| `530` | `0xd4c1...3d1d` | `SHORT` | 4,174,220.20 USD | `3,294.31` | `1294.12` | `1267.21` | `2589.27` | 89,006.45 USD | `+2.13%` | `10X Cross` |
| `537` | `0xd21d...90f1` | `LONG` | 4,123,600.00 USD | `3,250.00` | `1253.64` | `1267.21` | `876.06` | 49,258.27 USD | `+1.19%` | `4X Isolated` |
| `541` | `0x456f...cdf1` | `LONG` | 4,100,015.21 USD | `3,226.58` | `1267.75` | `1267.21` | `516.75` | 9,528.58 USD | `+0.23%` | `10X Cross` |
| `556` | `0x1338...c48e` | `LONG` | 4,000,405.99 USD | `3,149.43` | `1018.52` | `1267.21` | `820.35` | 792,660.44 USD | `+19.81%` | `4X Isolated` |
| `563` | `0x325e...9564` | `LONG` | 3,949,351.81 USD | `3,101.91` | `1298.07` | `1267.21` | `171.11` | -77,158.89 USD | `-1.95%` | `10X Cross` |
| `572` | `0xdbe0...d6d5` | `LONG` | 3,909,780.86 USD | `3,085.37` | `422.97` | `1267.21` | `338.67` | 2,604,776.37 USD | `+66.62%` | `3X Isolated` |
| `592` | `0x2e30...4cb5` | `SHORT` | 3,809,928.95 USD | `3,006.81` | `1287.70` | `1267.21` | `2874.90` | 61,948.21 USD | `+1.63%` | `2X Cross` |
| `594` | `0x9c06...0560` | `SHORT` | 3,791,365.38 USD | `2,989.80` | `786.00` | `1267.21` | `2592.72` | -1,441,370.38 USD | `-38.02%` | `10X Cross` |
| `599` | `0x27c9...d65d` | `SHORT` | 3,755,960.03 USD | `2,961.88` | `1254.41` | `1267.21` | `1738.22` | -40,544.82 USD | `-1.08%` | `10X Cross` |
| `690` | `0xac48...3201` | `LONG` | 3,216,777.05 USD | `2,531.50` | `1378.58` | `1267.21` | `523.64` | -273,095.23 USD | `-8.49%` | `10X Cross` |
| `694` | `0xa183...0482` | `LONG` | 3,210,429.76 USD | `2,534.00` | `530.25` | `1267.21` | `444.59` | 1,866,767.04 USD | `+58.15%` | `5X Isolated` |
| `703` | `0x0871...e927` | `LONG` | 3,170,250.00 USD | `2,500.00` | `1276.50` | `1267.21` | `0.000000` | -21,000.00 USD | `-0.66%` | `10X Cross` |
| `711` | `0x5323...b23c` | `SHORT` | 3,140,849.47 USD | `2,478.77` | `1262.62` | `1267.21` | `3455.14` | -11,113.38 USD | `-0.35%` | `5X Cross` |
| `717` | `0x9b86...6e6e` | `LONG` | 3,125,435.04 USD | `2,463.30` | `637.58` | `1267.21` | `882.52` | 1,554,885.76 USD | `+49.75%` | `3X Cross` |
| `764` | `0x71d0...8c26` | `SHORT` | 2,969,651.59 USD | `2,343.66` | `1263.62` | `1267.21` | `3557.68` | -8,154.08 USD | `-0.27%` | `10X Cross` |
| `775` | `0xb2f7...af9f` | `SHORT` | 2,935,647.94 USD | `2,313.72` | `746.63` | `1267.21` | `4487.66` | -1,208,159.19 USD | `-41.15%` | `10X Cross` |
| `793` | `0x413c...886c` | `LONG` | 2,854,575.00 USD | `2,250.00` | `1237.51` | `1267.21` | `0.000000` | 70,173.97 USD | `+2.46%` | `10X Cross` |
| `798` | `0xb122...e4ba` | `LONG` | 2,846,226.95 USD | `2,243.42` | `1258.05` | `1267.21` | `984.64` | 23,893.03 USD | `+0.84%` | `10X Cross` |
| `805` | `0xf48f...10fe` | `LONG` | 2,814,820.11 USD | `2,218.49` | `1517.87` | `1267.21` | `987.56` | -552,566.71 USD | `-19.63%` | `3X Cross` |
| `836` | `0x5bc4...3b0c` | `SHORT` | 2,699,860.65 USD | `2,130.74` | `1089.65` | `1267.21` | `3705.95` | -378,103.08 USD | `-14.00%` | `5X Cross` |
| `849` | `0x8de4...b9aa` | `SHORT` | 2,655,101.78 USD | `2,091.29` | `1331.35` | `1267.21` | `1689.97` | 129,137.92 USD | `+4.86%` | `3X Cross` |
| `863` | `0x4fe2...ac59` | `SHORT` | 2,628,200.86 USD | `2,071.57` | `1478.56` | `1267.21` | `1841.97` | 434,745.36 USD | `+16.54%` | `10X Cross` |
| `870` | `0xdf57...93f5` | `LONG` | 2,603,066.88 USD | `2,054.35` | `1227.36` | `1267.21` | `897.30` | 81,644.84 USD | `+3.14%` | `4X Isolated` |
| `874` | `0xbcd4...0dd2` | `LONG` | 2,580,637.70 USD | `2,033.92` | `1228.20` | `1267.21` | `735.92` | 82,586.88 USD | `+3.20%` | `10X Cross` |
| `883` | `0x9a99...d21a` | `LONG` | 2,539,200.00 USD | `2,000.00` | `1278.44` | `1267.21` | `0.000000` | -17,673.67 USD | `-0.70%` | `10X Cross` |
| `888` | `0xf29c...9971` | `LONG` | 2,533,883.00 USD | `2,000.00` | `1254.95` | `1267.21` | `0.000000` | 23,985.93 USD | `+0.95%` | `10X Cross` |
| `908` | `0x77ee...2902` | `SHORT` | 2,471,847.31 USD | `1,946.03` | `759.84` | `1267.21` | `5445.24` | -993,169.80 USD | `-40.18%` | `10X Cross` |
| `919` | `0x3e2f...b269` | `SHORT` | 2,439,813.72 USD | `1,925.51` | `1134.87` | `1267.21` | `2931.90` | -254,614.86 USD | `-10.44%` | `10X Cross` |
| `929` | `0x4f12...618b` | `SHORT` | 2,407,517.09 USD | `1,896.28` | `1608.30` | `1267.21` | `2116.86` | 642,267.30 USD | `+26.68%` | `3X Cross` |
| `961` | `0x866d...d6e1` | `LONG` | 2,306,804.21 USD | `1,802.05` | `674.73` | `1267.21` | `239.63` | 1,090,902.89 USD | `+47.29%` | `10X Cross` |
| `994` | `0x2309...a2d9` | `LONG` | 2,219,644.20 USD | `1,750.37` | `1186.09` | `1267.21` | `815.11` | 143,550.09 USD | `+6.47%` | `8X Cross` |
| `1030` | `0x265e...7f70` | `LONG` | 2,095,232.19 USD | `1,651.74` | `1382.98` | `1267.21` | `0.000000` | -189,090.57 USD | `-9.02%` | `3X Cross` |
| `1037` | `0xfe7c...b7ae` | `SHORT` | 2,084,017.37 USD | `1,642.64` | `1346.92` | `1267.21` | `5779.19` | 128,491.25 USD | `+6.17%` | `10X Cross` |
| `1043` | `0x3e47...aaf6` | `LONG` | 2,076,112.06 USD | `1,636.28` | `1278.38` | `1267.21` | `1049.64` | -15,679.72 USD | `-0.76%` | `10X Cross` |
| `1045` | `0x2edd...8179` | `SHORT` | 2,073,569.80 USD | `1,633.89` | `1261.58` | `1267.21` | `2922.18` | -12,287.88 USD | `-0.59%` | `10X Cross` |
| `1058` | `0x7f75...9edf` | `LONG` | 2,043,758.73 USD | `1,611.67` | `1200.24` | `1267.21` | `984.91` | 109,374.75 USD | `+5.35%` | `10X Cross` |
| `1067` | `0x6646...6de5` | `SHORT` | 2,027,520.00 USD | `1,600.00` | `660.64` | `1267.21` | `4208.64` | -970,495.03 USD | `-47.87%` | `10X Cross` |
| `1075` | `0x023a...2355` | `SHORT` | 2,020,897.79 USD | `1,594.90` | `1310.00` | `1267.21` | `4475.48` | 68,414.35 USD | `+3.39%` | `10X Cross` |
| `1100` | `0xab59...59b5` | `LONG` | 1,985,921.48 USD | `1,565.32` | `1342.15` | `1267.21` | `839.10` | -114,973.73 USD | `-5.79%` | `10X Cross` |
| `1160` | `0xcf67...eb24` | `LONG` | 1,904,400.00 USD | `1,500.00` | `887.05` | `1267.21` | `670.18` | 573,828.63 USD | `+30.13%` | `10X Cross` |
| `1166` | `0x3205...40bb` | `SHORT` | 1,899,816.70 USD | `1,498.16` | `1250.12` | `1267.21` | `2228.70` | -26,942.49 USD | `-1.42%` | `10X Cross` |
| `1175` | `0xb695...a92d` | `LONG` | 1,880,592.30 USD | `1,483.00` | `1249.80` | `1267.21` | `0.000000` | 27,133.44 USD | `+1.44%` | `10X Cross` |
| `1179` | `0x7277...0b98` | `SHORT` | 1,871,373.21 USD | `1,475.73` | `1287.86` | `1267.21` | `2200.05` | 29,158.91 USD | `+1.56%` | `10X Cross` |
| `1242` | `0x2ab7...c2f8` | `LONG` | 1,774,535.80 USD | `1,400.51` | `813.26` | `1267.21` | `791.89` | 635,554.12 USD | `+35.82%` | `3X Cross` |
| `1260` | `0x11be...8b1d` | `LONG` | 1,745,515.52 USD | `1,375.83` | `1206.55` | `1267.21` | `1134.57` | 85,507.56 USD | `+4.90%` | `10X Isolated` |
| `1292` | `0xfc27...9d9d` | `SHORT` | 1,678,089.41 USD | `1,323.31` | `1298.46` | `1267.21` | `15069.28` | 40,177.28 USD | `+2.39%` | `10X Cross` |
| `1335` | `0x039c...0ebd` | `SHORT` | 1,621,621.91 USD | `1,279.79` | `1239.81` | `1267.21` | `3665.58` | -34,920.08 USD | `-2.15%` | `10X Cross` |
| `1351` | `0xe065...0f85` | `SHORT` | 1,601,873.31 USD | `1,262.61` | `1087.02` | `1267.21` | `1602.28` | -229,397.18 USD | `-14.32%` | `10X Cross` |
| `1423` | `0x5975...9abd` | `LONG` | 1,524,840.00 USD | `1,200.00` | `1179.54` | `1267.21` | `510.14` | 109,397.21 USD | `+7.17%` | `5X Cross` |
| `1425` | `0x266b...efcb` | `LONG` | 1,520,640.00 USD | `1,200.00` | `893.76` | `1267.21` | `406.03` | 448,130.30 USD | `+29.47%` | `10X Cross` |
| `1442` | `0x2847...d47b` | `LONG` | 1,506,918.78 USD | `1,186.27` | `1232.07` | `1267.21` | `0.000000` | 45,350.28 USD | `+3.01%` | `5X Cross` |
| `1463` | `0x69cc...14fd` | `SHORT` | 1,472,720.62 USD | `1,161.36` | `675.33` | `1267.21` | `8069.69` | -688,415.09 USD | `-46.74%` | `10X Cross` |
| `1476` | `0x3fc5...c0c1` | `SHORT` | 1,455,146.98 USD | `1,148.44` | `1264.34` | `1267.21` | `2790.42` | -3,133.20 USD | `-0.22%` | `10X Cross` |
| `1506` | `0xe35c...a1d3` | `LONG` | 1,430,351.85 USD | `1,127.06` | `1318.20` | `1267.21` | `694.49` | -55,343.50 USD | `-3.87%` | `2X Isolated` |
| `1518` | `0x5f94...4b96` | `LONG` | 1,415,054.58 USD | `1,115.27` | `538.00` | `1267.21` | `0.000000` | 815,036.94 USD | `+57.60%` | `10X Cross` |
| `1541` | `0x71df...a23d` | `SHORT` | 1,392,728.87 USD | `1,098.28` | `513.50` | `1267.21` | `2558.18` | -828,758.68 USD | `-59.51%` | `2X Cross` |
| `1570` | `0xbfc7...80b4` | `SHORT` | 1,362,132.50 USD | `1,075.00` | `558.03` | `1267.21` | `2876.49` | -762,253.77 USD | `-55.96%` | `10X Cross` |
| `1588` | `0x38f9...cb04` | `SHORT` | 1,335,715.09 USD | `1,053.32` | `1245.93` | `1267.21` | `2075.73` | -23,350.88 USD | `-1.75%` | `10X Cross` |
| `1642` | `0x123d...3bff` | `SHORT` | 1,279,314.84 USD | `1,009.64` | `491.08` | `1267.21` | `4421.07` | -783,496.94 USD | `-61.24%` | `10X Cross` |
| `1652` | `0x668c...ea2e` | `SHORT` | 1,270,300.00 USD | `1,000.00` | `1406.98` | `1267.21` | `4187.56` | 136,681.99 USD | `+10.76%` | `10X Cross` |
| `1657` | `0xe282...df29` | `LONG` | 1,268,800.00 USD | `1,000.00` | `420.99` | `1267.21` | `823.19` | 847,813.14 USD | `+66.82%` | `10X Cross` |
| `1682` | `0x17f0...094f` | `LONG` | 1,248,190.83 USD | `984.30` | `1287.23` | `1267.21` | `536.92` | -18,829.33 USD | `-1.51%` | `5X Cross` |
| `1694` | `0x51f6...2b39` | `SHORT` | 1,238,046.03 USD | `976.30` | `1299.77` | `1267.21` | `2542.88` | 30,917.87 USD | `+2.50%` | `10X Cross` |
| `1753` | `0x757d...94ba` | `LONG` | 1,177,617.50 USD | `925.00` | `1558.31` | `1267.21` | `0.000000` | -263,823.09 USD | `-22.40%` | `10X Cross` |
| `1756` | `0xaa82...9556` | `LONG` | 1,172,628.56 USD | `924.13` | `1254.72` | `1267.21` | `183.01` | 13,101.88 USD | `+1.12%` | `10X Cross` |
| `1801` | `0xb911...5525` | `LONG` | 1,143,630.00 USD | `900.00` | `1294.82` | `1267.21` | `1035.36` | -21,707.82 USD | `-1.90%` | `10X Cross` |
| `1852` | `0xcf0a...856f` | `LONG` | 1,104,705.31 USD | `871.15` | `1292.19` | `1267.21` | `1009.01` | -20,989.53 USD | `-1.90%` | `4X Cross` |
| `1859` | `0xef96...9383` | `SHORT` | 1,100,237.34 USD | `868.42` | `1259.08` | `1267.21` | `5413.06` | -6,825.55 USD | `-0.62%` | `10X Cross` |
| `1878` | `0xdf95...7d72` | `SHORT` | 1,081,043.17 USD | `853.27` | `1074.39` | `1267.21` | `45237.53` | -164,295.73 USD | `-15.20%` | `10X Cross` |
| `1915` | `0x601c...4f54` | `SHORT` | 1,045,447.00 USD | `824.42` | `615.11` | `1267.21` | `3106.18` | -538,334.25 USD | `-51.49%` | `5X Cross` |
| `1924` | `0xdf83...3cff` | `SHORT` | 1,039,832.94 USD | `820.64` | `1255.99` | `1267.21` | `1918.01` | -9,118.17 USD | `-0.88%` | `10X Cross` |
| `1928` | `0xae55...2236` | `LONG` | 1,035,686.67 USD | `817.47` | `1467.80` | `1267.21` | `0.000000` | -164,194.55 USD | `-15.85%` | `10X Cross` |
| `1964` | `0x0f02...5384` | `LONG` | 1,015,469.12 USD | `800.78` | `1290.36` | `1267.21` | `304.22` | -17,824.95 USD | `-1.76%` | `3X Cross` |
| `1968` | `0x11ee...1d1d` | `SHORT` | 1,014,480.00 USD | `800.00` | `1269.65` | `1267.21` | `1603.44` | 1,243.01 USD | `+0.12%` | `5X Cross` |
| `1972` | `0x9b0f...db40` | `LONG` | 1,013,758.96 USD | `800.00` | `1268.86` | `1267.21` | `797.19` | -1,330.80 USD | `-0.13%` | `10X Cross` |
| `1992` | `0x6e8f...4364` | `LONG` | 1,006,983.12 USD | `793.65` | `1260.00` | `1267.21` | `990.76` | 6,984.12 USD | `+0.69%` | `10X Cross` |
| `1993` | `0xabdb...84ac` | `LONG` | 1,006,478.29 USD | `793.69` | `711.79` | `1267.21` | `664.49` | 441,537.93 USD | `+43.87%` | `3X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `873.68` | 6,203.13 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 6.20K USD at 873.6800 USD [API] | `2026-08-23 14:08:41` |
| `ANNOUNCEMENT` | `INFO` | `873.59` | 8,727.16 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 8.73K USD at 873.5900 USD [API] | `2026-08-23 14:08:41` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`1404.55` (Vol: 3,000,000.00 USD, Dist: `+9.15%`) | Long MP=`1176.48` (Vol: 3,400,000.00 USD, Dist: `--8.57%`)
  * 48H Horizon: Short MP=`1404.55` (Vol: 3,000,000.00 USD, Dist: `+9.15%`) | Long MP=`1176.48` (Vol: 3,400,000.00 USD, Dist: `--8.57%`)
  * 3D Horizon: Short MP=`1404.55` (Vol: 3,000,000.00 USD, Dist: `+9.15%`) | Long MP=`1176.48` (Vol: 3,100,000.00 USD, Dist: `--8.57%`)
  * 7D Horizon: Short MP=`1404.10` (Vol: 3,000,000.00 USD, Dist: `+9.12%`) | Long MP=`1176.74` (Vol: 4,900,000.00 USD, Dist: `--8.55%`)
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
| `5m` | `BALANCED` | 0.00 USD | 1,750.00 USD | 1,750.00 USD | 1,750.00 USD | `1` | `2026-10-30 04:00:00 UTC - 2026-10-30 04:05:00 UTC` |
| `15m` | `BALANCED` | 0.00 USD | 1,750.00 USD | 1,750.00 USD | 1,750.00 USD | `1` | `2026-10-30 04:00:00 UTC - 2026-10-30 04:15:00 UTC` |
| `1h` | `BALANCED` | 0.00 USD | 1,750.00 USD | 1,750.00 USD | 1,750.00 USD | `1` | `2026-10-30 04:00:00 UTC - 2026-10-30 05:00:00 UTC` |
| `4h` | `BALANCED` | 0.00 USD | 1,750.00 USD | 1,750.00 USD | 1,750.00 USD | `1` | `2026-10-30 04:00:00 UTC - 2026-10-30 08:00:00 UTC` |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `0 USD` | Total OI Tokens: `-`
  * 1h OI Change: `0.00%` | 4h OI Change: `0.00%` | 24h OI Change: `0.00%`
  * Exchange Breakdown: Binance=`-` | Bybit=`-` | OKX=`-` | Hyperliquid=`-`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `83.78K` | Last 24h: `134.73K` | Last 3d: `246.48K` | Last 7d: `772.71K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0097%` | **USDT OKX** | `0.0100%` |
| **USDT Bybit** | `0.0100%` | **USDT KuCoin** | `0.0100%` |
| **USDT MEXC** | `0.0096%` | **USDT BingX** | `0.0100%` |
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
| `5:00 UTC` | `1236.45` | `1237.15` | `1236.45` | `1245.15` | `1230.45` | 21,904,768.45 USD | 9,625,705.12 USD | 12,279,063.33 USD | -2,653,358.20 USD | `-12.11%` | `1B / 0S` |
| `0:00 UTC` | `1228.65` | `1236.25` | `1228.65` | `1253.25` | `1219.35` | 45,146,863.08 USD | 23,450,812.50 USD | 21,696,050.59 USD | 1,754,761.91 USD | `+3.89%` | `18B / 9S` |
| `5:00 UTC` | `1254.75` | `1256.85` | `1254.75` | `1263.45` | `1247.85` | 37,496,922.68 USD | 20,689,312.95 USD | 16,807,609.72 USD | 3,881,703.23 USD | `+10.35%` | `5B / 3S` |
| `0:00 UTC` | `1263.45` | `1263.47` | `1263.45` | `1267.65` | `1258.35` | 21,490,941.27 USD | 11,626,504.00 USD | 9,864,437.27 USD | 1,762,066.74 USD | `+8.20%` | `2B / 3S` |
| `5:00 UTC` | `1257.45` | `1259.53` | `1257.45` | `1270.05` | `1249.95` | 34,915,865.69 USD | 14,880,758.20 USD | 20,035,107.50 USD | -5,154,349.30 USD | `-14.76%` | `1B / 7S` |
| `0:00 UTC` | `1260.15` | `1262.58` | `1260.15` | `1267.95` | `1257.15` | 13,992,732.07 USD | 6,287,729.60 USD | 7,705,002.47 USD | -1,417,272.88 USD | `-10.13%` | `0B / 2S` |
| `5:00 UTC` | `1265.55` | `1265.89` | `1265.55` | `1274.25` | `1259.25` | 13,172,642.30 USD | 7,854,309.17 USD | 5,318,333.13 USD | 2,535,976.04 USD | `+19.25%` | `13B / 1S` |
| `0:00 UTC` | `1282.05` | `1279.57` | `1282.05` | `1285.35` | `1269.15` | 31,465,166.07 USD | 16,761,441.58 USD | 14,703,724.48 USD | 2,057,717.10 USD | `+6.54%` | `8B / 5S` |
| `5:00 UTC` | `1279.95` | `1280.45` | `1279.95` | `1287.45` | `1275.15` | 19,925,691.14 USD | 8,662,599.23 USD | 11,263,091.92 USD | -2,600,492.69 USD | `-13.05%` | `1B / 6S` |
| `0:00 UTC` | `1278.15` | `1278.03` | `1278.15` | `1279.35` | `1276.65` | 278,954.33 USD | 135,508.53 USD | 143,445.80 USD | -7,937.27 USD | `-2.85%` | `3B / 2S` |

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
| `5m` | -530,170.00 USD | 148,100.00 USD | **`DISTRIBUTION`** |
| `15m` | -885,710.00 USD | -2,660,000.00 USD | **`DISTRIBUTION`** |
| `30m` | -1,230,000.00 USD | 1,180,000.00 USD | **`DISTRIBUTION`** |
| `1h` | 298,540.00 USD | 3,230,000.00 USD | **`ACCUMULATION`** |
| `2h` | 3,910,000.00 USD | 9,630,000.00 USD | **`ACCUMULATION`** |
| `4h` | 1,100,000.00 USD | 27,230,000.00 USD | **`ACCUMULATION`** |
| `6h` | -511,650.00 USD | 14,700,000.00 USD | **`ACCUMULATION`** |
| `8h` | -10,230,000.00 USD | 17,900,000.00 USD | **`ACCUMULATION`** |
| `12h` | -2,370,000.00 USD | 14,380,000.00 USD | **`ACCUMULATION`** |
| `24h` | 17,590,000.00 USD | 122,820,000.00 USD | **`ACCUMULATION`** |
| `1w` | 37,690,000.00 USD | 242,840,000.00 USD | **`ACCUMULATION`** |
| `30d` | 62,050,000.00 USD | -516,440,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-530.17K` | 15m=`-885.71K` | 1h=`+298.54K` | 24h=`+17.59M`
* Futures Capital Netflows: 5m=`+148.10K` | 15m=`-2.66M` | 1h=`+3.23M` | 24h=`+122.82M`
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
  * `2026-10-30 09:09:56 IST`: [forex.com] - (Sentiment: `Neutral`)
  * `2026-10-30 08:33:56 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 08:32:56 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 09:28:56 IST`: [financemagnates.com] - (Sentiment: `Neutral`)
  * `2026-10-30 09:27:56 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-30 09:27:56 IST`: [kathleenhays.substack.com] - (Sentiment: `Neutral`)
  * `2026-10-30 06:29:56 IST`: [rba.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 06:29:56 IST`: [abs.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 06:29:56 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 05:29:56 IST`: [@NodeWire] - (Sentiment: `Neutral`)
  * `2026-10-30 05:29:56 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 05:29:56 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 05:29:56 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-30 05:29:56 IST`: [media.rabobank.com] - (Sentiment: `Neutral`)
  * `2026-10-30 04:29:56 IST`: [economics.td.com] - (Sentiment: `Neutral`)


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
  * Spread-Padded Stop Loss: `1197.58` (Risk Distance: `24.59` pts)
  * +2.5R Take Profit: `1283.64`
  * Mathematical Lot Sizing: **`0.40 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `1267.01` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `1291.60` (Risk Distance: `24.59` pts)
  * +2.5R Take Profit: `1205.54`
  * Mathematical Lot Sizing: **`0.40 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`1280.55`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
