# 🏛️ SOVEREIGN CANDIDATE DOSSIER: ZECUSD
**Canonical Key**: `ZECUSD` | **Broker Instrument**: `ZECUSD.p` | **Asset Class**: `Crypto Altcoin`
**Timestamp**: `2026-10-30 16:12:33 IST` (`2026-10-30 10:42:33 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `1269.00` | **Live Ask Quote**: `1270.01` | **Mid Price**: `1269.51`
- **Spread Points**: `101.00` | **Spread BPS**: `7.96 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `1253.52` | VWAP Z-Score: `+0.45` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `12.31` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `53.57` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `1314.84` | Lower -3.00σ Band: `1192.19`
  * Upper +2.51σ Band: `1304.83` | Lower -2.51σ Band: `1202.21`
  * Upper +2.01σ Band: `1294.61` | Lower -2.01σ Band: `1212.43`
  * Upper +2.00σ Band: `1294.40` | Lower -2.00σ Band: `1212.63`
  * Upper +1.28σ Band: `1279.68` | Lower -1.28σ Band: `1227.35`
  * Upper +1.00σ Band: `1273.96` | Lower -1.00σ Band: `1233.07`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`1252.82` | EMA-20=`1255.47` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`1261.26` (Slope: `+0.0000`) | EMA-100=`1267.50`
  * Institutional Anchors: EMA-144=`1270.98` | EMA-200=`1275.76` (Slope: `-0.2646`) | EMA-233=`1275.77`
- **Range Boundaries**: 24H High=`1396.49` | 24H Low=`1180.03` | Weekly High=`1396.49` | Weekly Low=`1180.03`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `1279.38` (Distance: `-0.78%`)
  * Point of Control (POC) = `1247.68` (Distance: `+1.74%`)
  * Value Area Low (VAL) = `1239.95` (Distance: `+2.37%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`1309.91` | POC=`1246.71` | VAL=`1230.27`
  * Prior Day Extremes: PDH=`1396.49` | PDL=`1206.89` | PDC=`1244.38`
  * Monday Range Blueprint: High=`1267.53` | Mid=`1222.14` | Low=`1176.75`
  * Developing Weekly Value Area: Weekly VAH=`1293.21` | Weekly POC=`1240.47` | Weekly VAL=`1200.92`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`1296.00` | Low=`1180.03`
  * London Session (08:00-16:00 UTC): High=`1283.82` | Low=`1239.95`
  * New York Session (13:00-21:00 UTC): High=`1276.03` | Low=`1245.73`
  * Initial Balance (First Hour): IB High=`1283.82` | IB Low=`1264.92`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `1264.43` - `1274.58`
  * Optimal Trade Entry (OTE 0.705): `1272.04`
  * Structural Invalidation Anchor (0.786): `1279.66`

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
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 16:12:11 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `12` | `0xb83d...6e36` | `SHORT` | 66,655,272.03 USD | `52,385.47` | `1336.45` | `1275.70` | `3189.72` | 3,355,295.37 USD | `+5.03%` | `3X Cross` |
| `21` | `0x5b5d...c060` | `SHORT` | 51,069,589.83 USD | `40,121.38` | `1478.36` | `1275.70` | `4820.60` | 8,244,445.28 USD | `+16.14%` | `3X Cross` |
| `34` | `0x7fda...17d1` | `SHORT` | 33,967,779.22 USD | `26,633.04` | `1262.58` | `1275.70` | `2597.80` | -341,545.38 USD | `-1.01%` | `5X Cross` |
| `77` | `0x60b0...991e` | `LONG` | 21,355,575.10 USD | `16,779.74` | `1179.65` | `1275.70` | `915.01` | 1,561,328.08 USD | `+7.31%` | `10X Cross` |
| `137` | `0xc36a...105b` | `LONG` | 14,649,820.61 USD | `11,510.82` | `1215.14` | `1275.70` | `965.39` | 662,539.59 USD | `+4.52%` | `10X Cross` |
| `170` | `0x8742...8427` | `LONG` | 11,734,303.11 USD | `9,201.21` | `1286.37` | `1275.70` | `713.99` | -101,866.88 USD | `-0.87%` | `10X Cross` |
| `187` | `0x58b2...11f3` | `LONG` | 10,899,944.53 USD | `8,563.08` | `1246.56` | `1275.70` | `385.70` | 225,526.96 USD | `+2.07%` | `10X Cross` |
| `190` | `0x9071...5c0b` | `LONG` | 10,862,099.94 USD | `8,517.29` | `1353.83` | `1275.70` | `253.57` | -668,859.67 USD | `-6.16%` | `2X Cross` |
| `194` | `0xad59...ba81` | `SHORT` | 10,710,702.50 USD | `8,425.00` | `330.91` | `1275.70` | `2146.62` | -7,922,744.73 USD | `-73.97%` | `10X Cross` |
| `195` | `0x9ffd...ce40` | `LONG` | 10,691,914.52 USD | `8,400.97` | `1252.16` | `1275.70` | `594.62` | 172,562.89 USD | `+1.61%` | `5X Cross` |
| `199` | `0xdd53...2b13` | `SHORT` | 10,444,880.45 USD | `8,195.92` | `741.54` | `1275.70` | `8381.75` | -4,367,284.08 USD | `-41.81%` | `3X Cross` |
| `220` | `0x880a...311c` | `SHORT` | 9,808,838.90 USD | `7,707.11` | `1367.50` | `1275.70` | `2231.39` | 730,645.31 USD | `+7.45%` | `10X Cross` |
| `232` | `0xbf73...5d58` | `LONG` | 9,546,579.00 USD | `7,500.00` | `1248.78` | `1275.70` | `122.70` | 180,733.38 USD | `+1.89%` | `10X Cross` |
| `266` | `0x2b61...2f6c` | `LONG` | 8,662,488.82 USD | `6,807.00` | `1453.56` | `1275.70` | `568.51` | -1,231,862.40 USD | `-14.22%` | `10X Cross` |
| `282` | `0x2ae5...83e7` | `LONG` | 8,208,851.04 USD | `6,436.80` | `1391.82` | `1275.70` | `0.000000` | -750,040.95 USD | `-9.14%` | `1X Cross` |
| `313` | `0xecb6...2b00` | `SHORT` | 7,415,430.68 USD | `5,814.20` | `1277.51` | `1275.70` | `6252.70` | 12,293.54 USD | `+0.17%` | `5X Cross` |
| `328` | `0x26b6...9a13` | `LONG` | 6,932,352.73 USD | `5,433.73` | `1282.23` | `1275.70` | `230.32` | -34,950.50 USD | `-0.50%` | `10X Cross` |
| `341` | `0x45d2...4029` | `SHORT` | 6,665,993.10 USD | `5,227.00` | `833.44` | `1275.70` | `8948.16` | -2,309,615.13 USD | `-34.65%` | `5X Cross` |
| `362` | `0xea00...a918` | `LONG` | 6,360,500.00 USD | `5,000.00` | `739.16` | `1275.70` | `0.000000` | 2,664,684.89 USD | `+41.89%` | `5X Cross` |
| `373` | `0xdd7a...8830` | `LONG` | 6,184,105.76 USD | `4,860.19` | `897.48` | `1275.70` | `780.32` | 1,822,202.08 USD | `+29.47%` | `10X Cross` |
| `420` | `0x469e...58a5` | `SHORT` | 5,299,328.26 USD | `4,163.52` | `1242.31` | `1275.70` | `1951.49` | -126,943.60 USD | `-2.40%` | `10X Cross` |
| `421` | `0x4cae...7c34` | `LONG` | 5,284,118.18 USD | `4,152.27` | `1172.97` | `1275.70` | `983.79` | 413,624.63 USD | `+7.83%` | `10X Cross` |
| `438` | `0xd4c1...3d1d` | `SHORT` | 5,008,280.07 USD | `3,930.24` | `1291.66` | `1275.70` | `2327.12` | 68,256.03 USD | `+1.36%` | `10X Cross` |
| `442` | `0xa61c...66b9` | `LONG` | 4,954,453.91 USD | `3,888.00` | `1148.34` | `1275.70` | `0.000000` | 489,711.77 USD | `+9.88%` | `10X Cross` |
| `456` | `0x382b...3e39` | `LONG` | 4,825,080.76 USD | `3,792.11` | `1220.71` | `1275.70` | `0.000000` | 196,008.96 USD | `+4.06%` | `10X Cross` |
| `463` | `0x9aa5...58af` | `SHORT` | 4,741,163.06 USD | `3,720.31` | `1205.51` | `1275.70` | `3663.55` | -256,276.26 USD | `-5.41%` | `10X Cross` |
| `469` | `0x0153...8052` | `SHORT` | 4,718,507.86 USD | `3,698.18` | `1307.82` | `1275.70` | `2504.94` | 118,062.89 USD | `+2.50%` | `1X Isolated` |
| `501` | `0xb122...e4ba` | `LONG` | 4,450,753.53 USD | `3,498.47` | `1265.25` | `1275.70` | `1090.56` | 24,302.01 USD | `+0.55%` | `10X Cross` |
| `538` | `0xd21d...90f1` | `LONG` | 4,131,725.00 USD | `3,250.00` | `1253.64` | `1275.70` | `876.17` | 57,383.27 USD | `+1.39%` | `4X Isolated` |
| `540` | `0x456f...cdf1` | `LONG` | 4,113,455.08 USD | `3,235.12` | `1267.53` | `1275.70` | `518.56` | 12,842.53 USD | `+0.31%` | `10X Cross` |
| `552` | `0x1338...c48e` | `LONG` | 4,010,169.22 USD | `3,149.43` | `1018.52` | `1275.70` | `820.46` | 802,423.68 USD | `+20.01%` | `4X Isolated` |
| `567` | `0xdbe0...d6d5` | `LONG` | 3,936,623.58 USD | `3,085.37` | `422.97` | `1275.70` | `338.78` | 2,631,619.09 USD | `+66.85%` | `3X Isolated` |
| `589` | `0x325e...9564` | `LONG` | 3,817,757.70 USD | `3,000.91` | `1298.07` | `1275.70` | `143.12` | -77,647.46 USD | `-2.03%` | `10X Cross` |
| `592` | `0x9c06...0560` | `SHORT` | 3,805,648.25 USD | `2,989.80` | `786.00` | `1275.70` | `2560.49` | -1,455,653.25 USD | `-38.25%` | `10X Cross` |
| `593` | `0x2e30...4cb5` | `SHORT` | 3,805,125.36 USD | `2,983.71` | `1282.27` | `1275.70` | `2891.57` | 20,809.96 USD | `+0.55%` | `2X Cross` |
| `600` | `0x27c9...d65d` | `SHORT` | 3,735,717.86 USD | `2,938.04` | `1254.41` | `1275.70` | `1735.29` | -50,207.82 USD | `-1.34%` | `10X Cross` |
| `692` | `0xa183...0482` | `LONG` | 3,231,610.20 USD | `2,534.00` | `530.25` | `1275.70` | `444.70` | 1,887,947.48 USD | `+58.42%` | `5X Isolated` |
| `697` | `0xac48...3201` | `LONG` | 3,221,840.05 USD | `2,531.50` | `1378.58` | `1275.70` | `552.17` | -268,032.23 USD | `-8.32%` | `10X Cross` |
| `706` | `0x0871...e927` | `LONG` | 3,181,463.50 USD | `2,500.00` | `1276.50` | `1275.70` | `0.000000` | -9,786.50 USD | `-0.31%` | `10X Cross` |
| `718` | `0x9b86...6e6e` | `LONG` | 3,131,593.29 USD | `2,463.30` | `637.58` | `1275.70` | `882.63` | 1,561,044.01 USD | `+49.85%` | `3X Cross` |
| `805` | `0xf48f...10fe` | `LONG` | 2,822,362.98 USD | `2,218.49` | `1517.87` | `1275.70` | `976.31` | -545,023.85 USD | `-19.31%` | `3X Cross` |
| `829` | `0x5bc4...3b0c` | `SHORT` | 2,715,415.06 USD | `2,130.74` | `1089.65` | `1275.70` | `3661.32` | -393,657.48 USD | `-14.50%` | `5X Cross` |
| `844` | `0x8de4...b9aa` | `SHORT` | 2,662,003.04 USD | `2,091.29` | `1331.35` | `1275.70` | `1690.07` | 122,236.66 USD | `+4.59%` | `3X Cross` |
| `851` | `0x71d0...8c26` | `SHORT` | 2,638,588.60 USD | `2,073.71` | `1265.96` | `1275.70` | `3897.14` | -13,355.30 USD | `-0.51%` | `10X Cross` |
| `853` | `0x4fe2...ac59` | `SHORT` | 2,635,451.35 USD | `2,071.57` | `1478.56` | `1275.70` | `1835.01` | 427,494.86 USD | `+16.22%` | `10X Cross` |
| `858` | `0xdf57...93f5` | `LONG` | 2,618,063.64 USD | `2,054.35` | `1227.36` | `1275.70` | `897.41` | 96,641.60 USD | `+3.69%` | `4X Isolated` |
| `866` | `0xbcd4...0dd2` | `LONG` | 2,587,959.81 USD | `2,033.92` | `1228.20` | `1275.70` | `787.55` | 89,908.99 USD | `+3.47%` | `10X Cross` |
| `872` | `0xf29c...9971` | `LONG` | 2,550,600.00 USD | `2,000.00` | `1254.95` | `1275.70` | `0.000000` | 40,702.93 USD | `+1.60%` | `10X Cross` |
| `874` | `0x9a99...d21a` | `LONG` | 2,544,400.00 USD | `2,000.00` | `1278.44` | `1275.70` | `0.000000` | -12,473.67 USD | `-0.49%` | `10X Cross` |
| `895` | `0x77ee...2902` | `SHORT` | 2,476,489.37 USD | `1,946.03` | `759.84` | `1275.70` | `5703.43` | -997,811.86 USD | `-40.29%` | `10X Cross` |
| `904` | `0x3e2f...b269` | `SHORT` | 2,453,869.94 USD | `1,925.51` | `1134.87` | `1275.70` | `2977.34` | -268,671.09 USD | `-10.95%` | `10X Cross` |
| `917` | `0x4f12...618b` | `SHORT` | 2,413,774.81 USD | `1,896.28` | `1608.30` | `1275.70` | `2116.96` | 636,009.58 USD | `+26.35%` | `3X Cross` |
| `965` | `0x866d...d6e1` | `LONG` | 2,293,262.52 USD | `1,802.05` | `674.73` | `1275.70` | `118.84` | 1,077,361.21 USD | `+46.98%` | `10X Cross` |
| `989` | `0x2309...a2d9` | `LONG` | 2,227,695.90 USD | `1,750.37` | `1186.09` | `1275.70` | `808.49` | 151,601.79 USD | `+6.81%` | `8X Cross` |
| `1014` | `0x039c...0ebd` | `SHORT` | 2,126,512.68 USD | `1,667.33` | `1247.23` | `1275.70` | `3550.05` | -46,961.05 USD | `-2.21%` | `10X Cross` |
| `1021` | `0x265e...7f70` | `LONG` | 2,102,499.85 USD | `1,651.74` | `1382.98` | `1275.70` | `0.000000` | -181,822.91 USD | `-8.65%` | `3X Cross` |
| `1025` | `0xfe7c...b7ae` | `SHORT` | 2,090,095.14 USD | `1,642.64` | `1346.92` | `1275.70` | `5625.49` | 122,413.48 USD | `+5.86%` | `10X Cross` |
| `1032` | `0x2edd...8179` | `SHORT` | 2,084,719.01 USD | `1,635.98` | `1261.55` | `1275.70` | `2844.01` | -20,856.12 USD | `-1.00%` | `10X Cross` |
| `1034` | `0x3e47...aaf6` | `LONG` | 2,080,202.76 USD | `1,636.28` | `1278.38` | `1275.70` | `1048.47` | -11,589.02 USD | `-0.56%` | `10X Cross` |
| `1048` | `0x7f75...9edf` | `LONG` | 2,052,305.11 USD | `1,612.56` | `1200.27` | `1275.70` | `986.04` | 116,791.19 USD | `+5.69%` | `10X Cross` |
| `1053` | `0xfc27...9d9d` | `SHORT` | 2,044,953.22 USD | `1,604.64` | `1295.09` | `1275.70` | `12817.37` | 33,192.59 USD | `+1.62%` | `10X Cross` |
| `1056` | `0x6646...6de5` | `SHORT` | 2,041,440.00 USD | `1,600.00` | `660.64` | `1275.70` | `4280.80` | -984,415.03 USD | `-48.22%` | `10X Cross` |
| `1072` | `0x023a...2355` | `SHORT` | 2,024,464.58 USD | `1,591.31` | `1310.00` | `1275.70` | `4405.66` | 60,144.67 USD | `+2.97%` | `10X Cross` |
| `1085` | `0xab59...59b5` | `LONG` | 1,991,713.17 USD | `1,565.32` | `1342.15` | `1275.70` | `834.17` | -109,182.05 USD | `-5.48%` | `10X Cross` |
| `1149` | `0xcf67...eb24` | `LONG` | 1,908,300.00 USD | `1,500.00` | `887.05` | `1275.70` | `613.52` | 577,728.63 USD | `+30.27%` | `10X Cross` |
| `1165` | `0x7277...0b98` | `SHORT` | 1,873,439.24 USD | `1,475.73` | `1287.86` | `1275.70` | `2191.72` | 27,092.89 USD | `+1.45%` | `10X Cross` |
| `1227` | `0x2ab7...c2f8` | `LONG` | 1,786,770.66 USD | `1,400.51` | `813.26` | `1275.70` | `790.56` | 647,788.97 USD | `+36.25%` | `3X Cross` |
| `1228` | `0x926a...af36` | `LONG` | 1,786,151.99 USD | `1,401.68` | `1254.50` | `1275.70` | `1187.92` | 27,750.09 USD | `+1.55%` | `10X Isolated` |
| `1244` | `0x5323...b23c` | `SHORT` | 1,762,223.10 USD | `1,384.96` | `1259.67` | `1275.70` | `5241.70` | -17,636.23 USD | `-1.00%` | `5X Cross` |
| `1251` | `0x11be...8b1d` | `LONG` | 1,749,092.68 USD | `1,375.83` | `1206.55` | `1275.70` | `1134.68` | 89,084.72 USD | `+5.09%` | `10X Isolated` |
| `1284` | `0x3205...40bb` | `SHORT` | 1,682,074.63 USD | `1,321.97` | `1257.09` | `1275.70` | `2366.65` | -20,243.78 USD | `-1.20%` | `10X Cross` |
| `1286` | `0xb897...ebc1` | `SHORT` | 1,681,291.75 USD | `1,318.35` | `1254.84` | `1275.70` | `1349.95` | -26,971.60 USD | `-1.60%` | `10X Cross` |
| `1324` | `0xdf83...3cff` | `SHORT` | 1,632,309.55 USD | `1,279.44` | `1260.36` | `1275.70` | `1879.22` | -19,749.33 USD | `-1.21%` | `10X Cross` |
| `1338` | `0xe065...0f85` | `SHORT` | 1,606,923.75 USD | `1,262.61` | `1087.02` | `1275.70` | `1547.97` | -234,447.62 USD | `-14.59%` | `10X Cross` |
| `1348` | `0x413c...886c` | `LONG` | 1,589,125.00 USD | `1,250.00` | `1237.51` | `1275.70` | `0.000000` | 42,235.54 USD | `+2.66%` | `10X Cross` |
| `1404` | `0x2847...d47b` | `LONG` | 1,544,203.22 USD | `1,211.71` | `1232.45` | `1275.70` | `0.000000` | 50,835.62 USD | `+3.29%` | `5X Cross` |
| `1413` | `0x266b...efcb` | `LONG` | 1,531,080.00 USD | `1,200.00` | `893.76` | `1275.70` | `396.69` | 458,570.30 USD | `+29.95%` | `10X Cross` |
| `1418` | `0x5975...9abd` | `LONG` | 1,525,560.00 USD | `1,200.00` | `1179.54` | `1275.70` | `522.03` | 110,117.21 USD | `+7.22%` | `5X Cross` |
| `1457` | `0x69cc...14fd` | `SHORT` | 1,480,037.18 USD | `1,161.36` | `675.33` | `1275.70` | `8018.02` | -695,731.66 USD | `-47.01%` | `10X Cross` |
| `1468` | `0x3fc5...c0c1` | `SHORT` | 1,460,011.77 USD | `1,148.44` | `1264.34` | `1275.70` | `2766.36` | -7,998.00 USD | `-0.55%` | `10X Cross` |
| `1515` | `0x5f94...4b96` | `LONG` | 1,417,842.75 USD | `1,115.27` | `538.00` | `1275.70` | `0.000000` | 817,825.11 USD | `+57.68%` | `10X Cross` |
| `1520` | `0xe35c...a1d3` | `LONG` | 1,412,316.29 USD | `1,111.36` | `1311.66` | `1275.70` | `690.98` | -45,407.86 USD | `-3.22%` | `2X Isolated` |
| `1531` | `0x71df...a23d` | `SHORT` | 1,397,780.96 USD | `1,098.28` | `513.50` | `1275.70` | `2559.89` | -833,810.77 USD | `-59.65%` | `2X Cross` |
| `1545` | `0xef96...9383` | `SHORT` | 1,389,937.10 USD | `1,090.66` | `1259.84` | `1275.70` | `4390.81` | -15,885.15 USD | `-1.14%` | `10X Cross` |
| `1568` | `0xbfc7...80b4` | `SHORT` | 1,368,152.50 USD | `1,075.00` | `558.03` | `1275.70` | `2654.65` | -768,273.77 USD | `-56.15%` | `10X Cross` |
| `1595` | `0x123d...3bff` | `SHORT` | 1,329,131.52 USD | `1,044.34` | `519.62` | `1275.70` | `4113.25` | -786,473.31 USD | `-59.17%` | `10X Cross` |
| `1649` | `0x668c...ea2e` | `SHORT` | 1,272,800.00 USD | `1,000.00` | `1406.98` | `1275.70` | `4212.84` | 134,181.99 USD | `+10.54%` | `10X Cross` |
| `1652` | `0xe282...df29` | `LONG` | 1,270,800.00 USD | `1,000.00` | `420.99` | `1275.70` | `802.95` | 849,813.14 USD | `+66.87%` | `10X Cross` |
| `1671` | `0x17f0...094f` | `LONG` | 1,252,605.81 USD | `984.30` | `1287.23` | `1275.70` | `537.03` | -14,414.36 USD | `-1.15%` | `5X Cross` |
| `1685` | `0x51f6...2b39` | `SHORT` | 1,240,624.59 USD | `972.81` | `1299.77` | `1275.70` | `2499.78` | 23,803.11 USD | `+1.92%` | `10X Cross` |
| `1720` | `0x38f9...cb04` | `SHORT` | 1,207,876.32 USD | `947.80` | `1253.73` | `1275.70` | `2158.69` | -19,592.30 USD | `-1.62%` | `10X Cross` |
| `1741` | `0x757d...94ba` | `LONG` | 1,178,820.00 USD | `925.00` | `1558.31` | `1275.70` | `0.000000` | -262,620.59 USD | `-22.28%` | `10X Cross` |
| `1791` | `0x8b9d...7b28` | `SHORT` | 1,147,870.21 USD | `902.13` | `1272.01` | `1275.70` | `3732.74` | -351.22 USD | `-0.03%` | `10X Cross` |
| `1798` | `0xb911...5525` | `LONG` | 1,144,170.00 USD | `900.00` | `1294.82` | `1275.70` | `1035.46` | -21,167.82 USD | `-1.85%` | `10X Cross` |
| `1844` | `0xcf0a...856f` | `LONG` | 1,108,866.97 USD | `871.15` | `1292.19` | `1275.70` | `1026.33` | -16,827.87 USD | `-1.52%` | `4X Cross` |
| `1867` | `0xdf95...7d72` | `SHORT` | 1,088,260.56 USD | `853.27` | `1074.39` | `1275.70` | `44750.95` | -171,513.12 USD | `-15.76%` | `10X Cross` |
| `1891` | `0xf096...7553` | `SHORT` | 1,062,500.87 USD | `834.84` | `1255.99` | `1275.70` | `3335.91` | -13,953.34 USD | `-1.31%` | `10X Cross` |
| `1898` | `0xb2f7...af9f` | `SHORT` | 1,057,008.13 USD | `830.72` | `746.63` | `1275.70` | `8207.68` | -436,769.10 USD | `-41.32%` | `10X Cross` |
| `1907` | `0x601c...4f54` | `SHORT` | 1,049,733.99 USD | `824.42` | `615.11` | `1275.70` | `3120.23` | -542,621.23 USD | `-51.69%` | `5X Cross` |
| `1919` | `0xae55...2236` | `LONG` | 1,042,519.49 USD | `817.47` | `1467.80` | `1275.70` | `0.000000` | -157,361.73 USD | `-15.09%` | `10X Cross` |
| `1954` | `0x9b0f...db40` | `LONG` | 1,020,640.00 USD | `800.00` | `1268.86` | `1275.70` | `800.02` | 5,550.24 USD | `+0.54%` | `10X Cross` |
| `1955` | `0x0f02...5384` | `LONG` | 1,020,514.03 USD | `800.78` | `1290.36` | `1275.70` | `299.89` | -12,780.04 USD | `-1.25%` | `3X Cross` |
| `1973` | `0x6e8f...4364` | `LONG` | 1,011,343.19 USD | `793.65` | `1260.00` | `1275.70` | `897.53` | 11,344.19 USD | `+1.12%` | `10X Cross` |
| `1975` | `0xabdb...84ac` | `LONG` | 1,010,129.26 USD | `793.69` | `711.79` | `1275.70` | `664.60` | 445,188.90 USD | `+44.07%` | `3X Cross` |

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
  * 24H Horizon: Short MP=`1404.55` (Vol: 3,000,000.00 USD, Dist: `+10.46%`) | Long MP=`1176.48` (Vol: 3,400,000.00 USD, Dist: `--7.48%`)
  * 48H Horizon: Short MP=`1404.55` (Vol: 3,000,000.00 USD, Dist: `+10.46%`) | Long MP=`1176.48` (Vol: 3,400,000.00 USD, Dist: `--7.48%`)
  * 3D Horizon: Short MP=`1404.55` (Vol: 3,000,000.00 USD, Dist: `+10.46%`) | Long MP=`1176.48` (Vol: 3,400,000.00 USD, Dist: `--7.48%`)
  * 7D Horizon: Short MP=`1404.10` (Vol: 3,000,000.00 USD, Dist: `+10.42%`) | Long MP=`1176.74` (Vol: 4,900,000.00 USD, Dist: `--7.46%`)
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
| `5m` | `BALANCED` | 0.00 USD | 1,750.00 USD | 1,750.00 USD | 1,750.00 USD | `1` | `2026-10-30 10:40:00 UTC - 2026-10-30 10:45:00 UTC` |
| `15m` | `BALANCED` | 0.00 USD | 1,750.00 USD | 1,750.00 USD | 1,750.00 USD | `1` | `2026-10-30 10:30:00 UTC - 2026-10-30 10:45:00 UTC` |
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
  * Current Rate: `86.02K` | Last 24h: `171.90K` | Last 3d: `285.15K` | Last 7d: `847.79K`
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
| `5:00 UTC` | `1251.45` | `1250.99` | `1251.45` | `1255.05` | `1246.35` | 13,619,576.55 USD | 6,741,413.50 USD | 6,878,163.05 USD | -136,749.55 USD | `-1.00%` | `2B / 0S` |
| `0:00 UTC` | `1249.95` | `1249.10` | `1249.95` | `1253.55` | `1244.55` | 10,263,783.49 USD | 5,117,369.60 USD | 5,146,413.89 USD | -29,044.29 USD | `-0.28%` | `1B / 4S` |
| `5:00 UTC` | `1246.65` | `1246.77` | `1246.65` | `1252.35` | `1243.95` | 13,017,000.97 USD | 7,727,648.32 USD | 5,289,352.64 USD | 2,438,295.68 USD | `+18.73%` | `8B / 5S` |
| `0:00 UTC` | `1244.55` | `1245.81` | `1244.55` | `1249.05` | `1243.65` | 9,717,386.64 USD | 3,914,194.68 USD | 5,803,191.96 USD | -1,888,997.28 USD | `-19.44%` | `0B / 1S` |
| `5:00 UTC` | `1242.15` | `1244.40` | `1242.15` | `1249.35` | `1241.25` | 8,638,502.97 USD | 4,533,952.89 USD | 4,104,550.08 USD | 429,402.82 USD | `+4.97%` | `4B / 2S` |
| `0:00 UTC` | `1251.15` | `1247.35` | `1251.15` | `1251.75` | `1240.05` | 9,977,652.60 USD | 4,992,881.35 USD | 4,984,771.25 USD | 8,110.10 USD | `+0.08%` | `3B / 5S` |
| `5:00 UTC` | `1243.95` | `1249.40` | `1243.95` | `1256.55` | `1243.35` | 15,678,426.53 USD | 9,268,825.46 USD | 6,409,601.07 USD | 2,859,224.38 USD | `+18.24%` | `10B / 2S` |
| `0:00 UTC` | `1249.95` | `1250.19` | `1249.95` | `1256.25` | `1246.35` | 11,248,393.80 USD | 4,953,252.73 USD | 6,295,141.07 USD | -1,341,888.34 USD | `-11.93%` | `1B / 7S` |
| `5:00 UTC` | `1263.15` | `1259.85` | `1263.15` | `1266.15` | `1247.85` | 19,587,954.68 USD | 10,529,516.42 USD | 9,058,438.26 USD | 1,471,078.16 USD | `+7.51%` | `10B / 4S` |
| `0:00 UTC` | `1272.15` | `1270.94` | `1272.15` | `1276.65` | `1262.25` | 22,696,810.66 USD | 12,228,675.95 USD | 10,468,134.71 USD | 1,760,541.25 USD | `+7.76%` | `12B / 0S` |

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
| `5m` | 462,240.00 USD | 2,420,000.00 USD | **`ACCUMULATION`** |
| `15m` | 642,450.00 USD | 3,880,000.00 USD | **`ACCUMULATION`** |
| `30m` | 91,860.00 USD | 3,490,000.00 USD | **`ACCUMULATION`** |
| `1h` | -437,220.00 USD | 7,290,000.00 USD | **`ACCUMULATION`** |
| `2h` | -2,590,000.00 USD | 9,960,000.00 USD | **`ACCUMULATION`** |
| `4h` | 728,700.00 USD | -11,170,000.00 USD | **`DISTRIBUTION`** |
| `6h` | -456,770.00 USD | -27,770,000.00 USD | **`DISTRIBUTION`** |
| `8h` | 877,270.00 USD | -8,730,000.00 USD | **`DISTRIBUTION`** |
| `12h` | 360,890.00 USD | -21,470,000.00 USD | **`DISTRIBUTION`** |
| `24h` | 22,930,000.00 USD | 79,410,000.00 USD | **`ACCUMULATION`** |
| `1w` | 35,710,000.00 USD | 226,880,000.00 USD | **`ACCUMULATION`** |
| `30d` | 61,300,000.00 USD | -568,060,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+462.24K` | 15m=`+642.45K` | 1h=`-437.22K` | 24h=`+22.93M`
* Futures Capital Netflows: 5m=`+2.42M` | 15m=`+3.88M` | 1h=`+7.29M` | 24h=`+79.41M`
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
  * `2026-10-30 15:49:45 IST`: [istat.it] - (Sentiment: `Neutral`)
  * `2026-10-30 15:32:45 IST`: [ec.europa.eu] - (Sentiment: `Neutral`)
  * `2026-10-30 15:32:45 IST`: [ec.europa.eu] - (Sentiment: `Neutral`)
  * `2026-10-30 15:18:45 IST`: [dailyforex.com] - (Sentiment: `Neutral`)
  * `2026-10-30 15:12:45 IST`: [breakingthenews.net] - (Sentiment: `Neutral`)
  * `2026-10-30 16:07:45 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 16:07:45 IST`: [@FirstSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 16:07:45 IST`: [destatis.de] - (Sentiment: `Neutral`)
  * `2026-10-30 16:07:45 IST`: [istat.it] - (Sentiment: `Neutral`)
  * `2026-10-30 16:07:45 IST`: [channelnewsasia.com] - (Sentiment: `Neutral`)
  * `2026-10-30 16:06:45 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 16:06:45 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 16:06:45 IST`: [kof.ethz.ch] - (Sentiment: `Neutral`)
  * `2026-10-30 16:06:45 IST`: [gerlachmacro.substack.com] - (Sentiment: `Neutral`)
  * `2026-10-30 16:06:45 IST`: [@financialjuice] - (Sentiment: `Neutral`)


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
  * Spread-Padded Stop Loss: `1223.66` (Risk Distance: `16.29` pts)
  * +2.5R Take Profit: `1280.66`
  * Mathematical Lot Sizing: **`0.61 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `1279.38` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `1295.67` (Risk Distance: `16.29` pts)
  * +2.5R Take Profit: `1238.67`
  * Mathematical Lot Sizing: **`0.61 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`1279.66`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
