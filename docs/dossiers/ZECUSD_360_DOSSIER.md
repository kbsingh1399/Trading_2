# 🏛️ SOVEREIGN CANDIDATE DOSSIER: ZECUSD
**Canonical Key**: `ZECUSD` | **Broker Instrument**: `ZECUSD.p` | **Asset Class**: `Crypto Altcoin`
**Timestamp**: `2026-10-30 10:40:52 IST` (`2026-10-30 05:10:52 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `1273.93` | **Live Ask Quote**: `1275.44` | **Mid Price**: `1274.68`
- **Spread Points**: `151.00` | **Spread BPS**: `11.85 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `1248.14` | VWAP Z-Score: `+1.06` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `17.25` (Volatility Regime: `HIGH_EXPANSION`)
  * 14-Period RSI: `54.81` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `1323.81` | Lower -3.00σ Band: `1172.46`
  * Upper +2.51σ Band: `1311.45` | Lower -2.51σ Band: `1184.82`
  * Upper +2.01σ Band: `1298.84` | Lower -2.01σ Band: `1197.43`
  * Upper +2.00σ Band: `1298.59` | Lower -2.00σ Band: `1197.69`
  * Upper +1.28σ Band: `1280.43` | Lower -1.28σ Band: `1215.85`
  * Upper +1.00σ Band: `1273.36` | Lower -1.00σ Band: `1222.91`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`1273.31` | EMA-20=`1264.65` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`1267.69` (Slope: `+0.0000`) | EMA-100=`1272.77`
  * Institutional Anchors: EMA-144=`1274.12` | EMA-200=`1275.53` (Slope: `-0.0438`) | EMA-233=`1277.86`
- **Range Boundaries**: 24H High=`1396.49` | 24H Low=`1180.03` | Weekly High=`1396.49` | Weekly Low=`1180.03`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `1271.65` (Distance: `+0.21%`)
  * Point of Control (POC) = `1229.90` (Distance: `+3.61%`)
  * Value Area Low (VAL) = `1220.62` (Distance: `+4.40%`)
  * Auction Positioning: `ABOVE_VALUE (Imbalance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `RANGE_EXPANSION`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`1309.91` | POC=`1246.71` | VAL=`1230.27`
  * Prior Day Extremes: PDH=`1396.49` | PDL=`1206.89` | PDC=`1244.38`
  * Monday Range Blueprint: High=`1267.53` | Mid=`1222.14` | Low=`1176.75`
  * Developing Weekly Value Area: Weekly VAH=`1296.14` | Weekly POC=`1239.01` | Weekly VAL=`1200.92`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`1296.00` | Low=`1180.03`
  * London Session (08:00-16:00 UTC): High=`1280.52` | Low=`1272.71`
  * New York Session (13:00-21:00 UTC): High=`1282.33` | Low=`1267.04`
  * Initial Balance (First Hour): IB High=`1280.52` | IB Low=`1272.71`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `1269.59` - `1279.78`
  * Optimal Trade Entry (OTE 0.705): `1277.23`
  * Structural Invalidation Anchor (0.786): `1284.88`

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
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 10:34:32 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `13` | `0xb83d...6e36` | `SHORT` | 66,817,127.41 USD | `52,385.47` | `1336.45` | `1276.40` | `3678.75` | 3,193,439.99 USD | `+4.78%` | `3X Cross` |
| `22` | `0x5b5d...c060` | `SHORT` | 51,130,686.67 USD | `40,121.38` | `1478.36` | `1276.40` | `5101.19` | 8,183,348.44 USD | `+16.00%` | `3X Cross` |
| `38` | `0x7fda...17d1` | `SHORT` | 33,140,556.82 USD | `25,962.05` | `1262.54` | `1276.40` | `2616.70` | -362,523.16 USD | `-1.09%` | `5X Cross` |
| `81` | `0x60b0...991e` | `LONG` | 21,387,456.60 USD | `16,779.74` | `1179.65` | `1276.40` | `919.87` | 1,593,209.59 USD | `+7.45%` | `10X Cross` |
| `141` | `0xc36a...105b` | `LONG` | 14,675,144.42 USD | `11,510.82` | `1215.14` | `1276.40` | `960.32` | 687,863.39 USD | `+4.69%` | `10X Cross` |
| `156` | `0x9071...5c0b` | `LONG` | 13,415,130.48 USD | `10,517.29` | `1353.83` | `1276.40` | `0.1605` | -823,488.39 USD | `-6.14%` | `1X Cross` |
| `177` | `0x8742...8427` | `LONG` | 11,744,475.05 USD | `9,201.21` | `1286.37` | `1276.40` | `700.13` | -91,694.94 USD | `-0.78%` | `10X Cross` |
| `192` | `0x58b2...11f3` | `LONG` | 10,915,358.08 USD | `8,563.08` | `1246.56` | `1276.40` | `381.76` | 240,940.50 USD | `+2.21%` | `10X Cross` |
| `196` | `0xad59...ba81` | `SHORT` | 10,745,876.88 USD | `8,425.00` | `330.91` | `1276.40` | `2144.41` | -7,957,919.10 USD | `-74.06%` | `10X Cross` |
| `197` | `0x9ffd...ce40` | `LONG` | 10,708,716.46 USD | `8,400.97` | `1251.60` | `1276.40` | `595.70` | 194,020.42 USD | `+1.81%` | `5X Cross` |
| `203` | `0xdd53...2b13` | `SHORT` | 10,459,947.83 USD | `8,195.92` | `741.54` | `1276.40` | `8494.35` | -4,382,351.46 USD | `-41.90%` | `3X Cross` |
| `223` | `0x880a...311c` | `SHORT` | 9,838,125.91 USD | `7,707.11` | `1367.50` | `1276.40` | `2262.50` | 701,358.29 USD | `+7.13%` | `10X Cross` |
| `236` | `0xbf73...5d58` | `LONG` | 9,558,000.00 USD | `7,500.00` | `1248.78` | `1276.40` | `115.46` | 192,154.38 USD | `+2.01%` | `10X Cross` |
| `270` | `0x2b61...2f6c` | `LONG` | 8,678,244.30 USD | `6,807.00` | `1453.56` | `1276.40` | `577.27` | -1,216,106.92 USD | `-14.01%` | `10X Cross` |
| `287` | `0x2ae5...83e7` | `LONG` | 8,216,575.20 USD | `6,436.80` | `1391.82` | `1276.40` | `0.000000` | -742,316.79 USD | `-9.03%` | `1X Cross` |
| `330` | `0x26b6...9a13` | `LONG` | 6,930,891.60 USD | `5,433.73` | `1282.23` | `1276.40` | `224.80` | -36,411.63 USD | `-0.53%` | `10X Cross` |
| `342` | `0x45d2...4029` | `SHORT` | 6,672,265.50 USD | `5,227.00` | `833.44` | `1276.40` | `8856.29` | -2,315,887.53 USD | `-34.71%` | `5X Cross` |
| `348` | `0xecb6...2b00` | `SHORT` | 6,646,046.19 USD | `5,206.46` | `1279.14` | `1276.40` | `6562.40` | 13,737.90 USD | `+0.21%` | `5X Cross` |
| `362` | `0xea00...a918` | `LONG` | 6,373,000.00 USD | `5,000.00` | `739.16` | `1276.40` | `0.000000` | 2,677,184.89 USD | `+42.01%` | `5X Cross` |
| `374` | `0xdd7a...8830` | `LONG` | 6,199,122.29 USD | `4,860.19` | `897.48` | `1276.40` | `783.47` | 1,837,218.61 USD | `+29.64%` | `10X Cross` |
| `419` | `0x469e...58a5` | `SHORT` | 5,308,071.65 USD | `4,163.52` | `1242.31` | `1276.40` | `1973.81` | -135,686.99 USD | `-2.56%` | `10X Cross` |
| `430` | `0x4cae...7c34` | `LONG` | 5,103,445.36 USD | `4,002.27` | `1169.72` | `1276.40` | `960.45` | 421,896.02 USD | `+8.27%` | `10X Cross` |
| `443` | `0xa61c...66b9` | `LONG` | 4,959,144.00 USD | `3,888.00` | `1148.34` | `1276.40` | `0.000000` | 494,401.86 USD | `+9.97%` | `10X Cross` |
| `468` | `0x9aa5...58af` | `SHORT` | 4,748,603.68 USD | `3,720.31` | `1205.51` | `1276.40` | `3674.28` | -263,716.88 USD | `-5.55%` | `10X Cross` |
| `474` | `0x0153...8052` | `SHORT` | 4,722,575.86 USD | `3,698.18` | `1307.82` | `1276.40` | `2504.86` | 113,994.89 USD | `+2.41%` | `1X Isolated` |
| `484` | `0xd4c1...3d1d` | `SHORT` | 4,643,938.88 USD | `3,638.31` | `1293.27` | `1276.40` | `2402.20` | 61,366.89 USD | `+1.32%` | `10X Cross` |
| `538` | `0x382b...3e39` | `LONG` | 4,173,508.90 USD | `3,269.75` | `1215.08` | `1276.40` | `0.000000` | 200,502.22 USD | `+4.80%` | `10X Cross` |
| `542` | `0xd21d...90f1` | `LONG` | 4,145,293.75 USD | `3,250.00` | `1253.64` | `1276.40` | `876.08` | 70,952.02 USD | `+1.71%` | `4X Isolated` |
| `554` | `0x456f...cdf1` | `LONG` | 4,054,485.65 USD | `3,179.49` | `1267.80` | `1276.40` | `504.13` | 23,530.73 USD | `+0.58%` | `10X Cross` |
| `561` | `0x1338...c48e` | `LONG` | 4,017,413.54 USD | `3,149.43` | `1018.52` | `1276.40` | `820.37` | 809,668.00 USD | `+20.15%` | `4X Isolated` |
| `568` | `0x325e...9564` | `LONG` | 3,956,486.21 USD | `3,101.91` | `1298.07` | `1276.40` | `147.41` | -70,024.49 USD | `-1.77%` | `10X Cross` |
| `572` | `0xdbe0...d6d5` | `LONG` | 3,944,645.54 USD | `3,085.37` | `422.97` | `1276.40` | `338.69` | 2,639,641.05 USD | `+66.92%` | `3X Isolated` |
| `597` | `0x2e30...4cb5` | `SHORT` | 3,820,223.98 USD | `2,994.61` | `1287.28` | `1276.40` | `2874.88` | 34,676.21 USD | `+0.91%` | `2X Cross` |
| `599` | `0x9c06...0560` | `SHORT` | 3,810,201.12 USD | `2,989.80` | `786.00` | `1276.40` | `2569.61` | -1,460,206.12 USD | `-38.32%` | `10X Cross` |
| `600` | `0xb122...e4ba` | `LONG` | 3,807,894.88 USD | `2,986.35` | `1263.08` | `1276.40` | `1044.25` | 35,886.99 USD | `+0.94%` | `10X Cross` |
| `604` | `0x27c9...d65d` | `SHORT` | 3,775,212.25 USD | `2,961.88` | `1254.41` | `1276.40` | `1732.79` | -59,797.04 USD | `-1.58%` | `10X Cross` |
| `674` | `0x5323...b23c` | `SHORT` | 3,354,241.75 USD | `2,629.54` | `1266.15` | `1276.40` | `3327.50` | -24,844.39 USD | `-0.74%` | `5X Cross` |
| `697` | `0xa183...0482` | `LONG` | 3,234,411.54 USD | `2,534.00` | `530.25` | `1276.40` | `444.61` | 1,890,748.82 USD | `+58.46%` | `5X Isolated` |
| `700` | `0xac48...3201` | `LONG` | 3,226,649.90 USD | `2,531.50` | `1378.58` | `1276.40` | `549.39` | -263,222.38 USD | `-8.16%` | `10X Cross` |
| `711` | `0x0871...e927` | `LONG` | 3,187,250.00 USD | `2,500.00` | `1276.50` | `1276.40` | `0.000000` | -4,000.00 USD | `-0.13%` | `10X Cross` |
| `716` | `0x71d0...8c26` | `SHORT` | 3,158,044.28 USD | `2,476.63` | `1265.67` | `1276.40` | `3705.90` | -23,454.86 USD | `-0.74%` | `10X Cross` |
| `720` | `0x9b86...6e6e` | `LONG` | 3,141,877.57 USD | `2,463.30` | `637.58` | `1276.40` | `882.54` | 1,571,328.28 USD | `+50.01%` | `3X Cross` |
| `779` | `0xb2f7...af9f` | `SHORT` | 2,951,092.02 USD | `2,313.72` | `746.63` | `1276.40` | `4436.24` | -1,223,603.27 USD | `-41.46%` | `10X Cross` |
| `798` | `0x413c...886c` | `LONG` | 2,869,200.00 USD | `2,250.00` | `1237.51` | `1276.40` | `0.000000` | 84,798.97 USD | `+2.96%` | `10X Cross` |
| `809` | `0xf48f...10fe` | `LONG` | 2,829,628.53 USD | `2,218.49` | `1517.87` | `1276.40` | `963.73` | -537,758.29 USD | `-19.00%` | `3X Cross` |
| `842` | `0x5bc4...3b0c` | `SHORT` | 2,719,332.21 USD | `2,130.74` | `1089.65` | `1276.40` | `3693.28` | -397,574.63 USD | `-14.62%` | `5X Cross` |
| `857` | `0x8de4...b9aa` | `SHORT` | 2,665,767.36 USD | `2,091.29` | `1331.35` | `1276.40` | `1689.99` | 118,472.34 USD | `+4.44%` | `3X Cross` |
| `863` | `0x4fe2...ac59` | `SHORT` | 2,640,630.28 USD | `2,071.57` | `1478.56` | `1276.40` | `1828.94` | 422,315.94 USD | `+15.99%` | `10X Cross` |
| `866` | `0xdf57...93f5` | `LONG` | 2,620,323.42 USD | `2,054.35` | `1227.36` | `1276.40` | `897.32` | 98,901.38 USD | `+3.77%` | `4X Isolated` |
| `876` | `0xbcd4...0dd2` | `LONG` | 2,594,214.11 USD | `2,033.92` | `1228.20` | `1276.40` | `776.35` | 96,163.30 USD | `+3.71%` | `10X Cross` |
| `883` | `0xf29c...9971` | `LONG` | 2,552,811.00 USD | `2,000.00` | `1254.95` | `1276.40` | `0.000000` | 42,913.93 USD | `+1.68%` | `10X Cross` |
| `885` | `0x9a99...d21a` | `LONG` | 2,549,400.00 USD | `2,000.00` | `1278.44` | `1276.40` | `0.000000` | -7,473.67 USD | `-0.29%` | `10X Cross` |
| `912` | `0x77ee...2902` | `SHORT` | 2,481,456.22 USD | `1,946.03` | `759.84` | `1276.40` | `5470.83` | -1,002,778.71 USD | `-40.41%` | `10X Cross` |
| `922` | `0x3e2f...b269` | `SHORT` | 2,455,988.00 USD | `1,925.51` | `1134.87` | `1276.40` | `2977.26` | -270,789.15 USD | `-11.03%` | `10X Cross` |
| `936` | `0x4f12...618b` | `SHORT` | 2,417,188.12 USD | `1,896.28` | `1608.30` | `1276.40` | `2116.88` | 632,596.27 USD | `+26.17%` | `3X Cross` |
| `973` | `0x866d...d6e1` | `LONG` | 2,297,861.89 USD | `1,802.05` | `674.73` | `1276.40` | `182.73` | 1,081,960.58 USD | `+47.09%` | `10X Cross` |
| `997` | `0x2309...a2d9` | `LONG` | 2,231,546.71 USD | `1,750.37` | `1186.09` | `1276.40` | `811.42` | 155,452.60 USD | `+6.97%` | `8X Cross` |
| `1033` | `0x265e...7f70` | `LONG` | 2,105,472.98 USD | `1,651.74` | `1382.98` | `1276.40` | `0.000000` | -178,849.78 USD | `-8.49%` | `3X Cross` |
| `1039` | `0xfe7c...b7ae` | `SHORT` | 2,093,708.94 USD | `1,642.64` | `1346.92` | `1276.40` | `5665.33` | 118,799.68 USD | `+5.67%` | `10X Cross` |
| `1044` | `0x3e47...aaf6` | `LONG` | 2,087,034.23 USD | `1,636.28` | `1278.38` | `1276.40` | `1046.53` | -4,757.55 USD | `-0.23%` | `10X Cross` |
| `1046` | `0x2edd...8179` | `SHORT` | 2,084,026.70 USD | `1,633.89` | `1261.58` | `1276.40` | `2894.14` | -22,744.78 USD | `-1.09%` | `10X Cross` |
| `1049` | `0x3205...40bb` | `SHORT` | 2,074,661.79 USD | `1,627.01` | `1255.41` | `1276.40` | `2125.95` | -32,100.88 USD | `-1.55%` | `10X Cross` |
| `1062` | `0x7f75...9edf` | `LONG` | 2,053,912.25 USD | `1,611.67` | `1200.24` | `1276.40` | `982.80` | 119,528.27 USD | `+5.82%` | `10X Cross` |
| `1070` | `0x6646...6de5` | `SHORT` | 2,040,640.00 USD | `1,600.00` | `660.64` | `1276.40` | `4310.81` | -983,615.03 USD | `-48.20%` | `10X Cross` |
| `1076` | `0x023a...2355` | `SHORT` | 2,033,717.12 USD | `1,594.90` | `1310.00` | `1276.40` | `4430.70` | 55,595.02 USD | `+2.73%` | `10X Cross` |
| `1098` | `0xab59...59b5` | `LONG` | 1,996,526.53 USD | `1,565.32` | `1342.15` | `1276.40` | `833.45` | -104,368.69 USD | `-5.23%` | `10X Cross` |
| `1148` | `0xfc27...9d9d` | `SHORT` | 1,937,663.18 USD | `1,517.95` | `1296.72` | `1276.40` | `12837.02` | 30,700.52 USD | `+1.58%` | `10X Cross` |
| `1162` | `0xcf67...eb24` | `LONG` | 1,912,050.00 USD | `1,500.00` | `887.05` | `1276.40` | `626.48` | 581,478.63 USD | `+30.41%` | `10X Cross` |
| `1175` | `0xb695...a92d` | `LONG` | 1,892,901.20 USD | `1,483.00` | `1249.80` | `1276.40` | `0.000000` | 39,442.35 USD | `+2.08%` | `10X Cross` |
| `1178` | `0x7277...0b98` | `SHORT` | 1,883,375.62 USD | `1,475.73` | `1287.86` | `1276.40` | `2177.32` | 17,156.50 USD | `+0.91%` | `10X Cross` |
| `1244` | `0x2ab7...c2f8` | `LONG` | 1,787,751.01 USD | `1,400.51` | `813.26` | `1276.40` | `790.20` | 648,769.33 USD | `+36.29%` | `3X Cross` |
| `1252` | `0xe35c...a1d3` | `LONG` | 1,771,873.58 USD | `1,389.16` | `1311.66` | `1276.40` | `690.78` | -50,229.13 USD | `-2.83%` | `2X Isolated` |
| `1263` | `0x11be...8b1d` | `LONG` | 1,754,458.42 USD | `1,375.83` | `1206.55` | `1276.40` | `1134.59` | 94,450.46 USD | `+5.38%` | `10X Isolated` |
| `1333` | `0x039c...0ebd` | `SHORT` | 1,633,651.94 USD | `1,279.79` | `1239.81` | `1276.40` | `3619.98` | -46,950.11 USD | `-2.87%` | `10X Cross` |
| `1350` | `0xe065...0f85` | `SHORT` | 1,609,448.97 USD | `1,262.61` | `1087.02` | `1276.40` | `1577.88` | -236,972.84 USD | `-14.72%` | `10X Cross` |
| `1425` | `0x266b...efcb` | `LONG` | 1,530,480.00 USD | `1,200.00` | `893.76` | `1276.40` | `382.33` | 457,970.30 USD | `+29.92%` | `10X Cross` |
| `1427` | `0x5975...9abd` | `LONG` | 1,530,240.00 USD | `1,200.00` | `1179.54` | `1276.40` | `471.39` | 114,797.21 USD | `+7.50%` | `5X Cross` |
| `1447` | `0x2847...d47b` | `LONG` | 1,512,375.62 USD | `1,186.27` | `1232.07` | `1276.40` | `0.000000` | 50,807.12 USD | `+3.36%` | `5X Cross` |
| `1468` | `0x69cc...14fd` | `SHORT` | 1,482,166.19 USD | `1,161.36` | `675.33` | `1276.40` | `7978.72` | -697,860.66 USD | `-47.08%` | `10X Cross` |
| `1482` | `0x3fc5...c0c1` | `SHORT` | 1,464,490.69 USD | `1,148.44` | `1264.34` | `1276.40` | `2700.34` | -12,476.91 USD | `-0.85%` | `10X Cross` |
| `1502` | `0x38f9...cb04` | `SHORT` | 1,448,277.00 USD | `1,136.26` | `1252.68` | `1276.40` | `1993.52` | -24,911.96 USD | `-1.72%` | `10X Cross` |
| `1519` | `0x5f94...4b96` | `LONG` | 1,422,499.00 USD | `1,115.27` | `538.00` | `1276.40` | `0.000000` | 822,481.37 USD | `+57.82%` | `10X Cross` |
| `1536` | `0x71df...a23d` | `SHORT` | 1,400,458.23 USD | `1,098.28` | `513.50` | `1276.40` | `2558.31` | -836,488.04 USD | `-59.73%` | `2X Cross` |
| `1570` | `0xbfc7...80b4` | `SHORT` | 1,370,517.50 USD | `1,075.00` | `558.03` | `1276.40` | `2700.78` | -770,638.77 USD | `-56.23%` | `10X Cross` |
| `1642` | `0x123d...3bff` | `SHORT` | 1,293,631.40 USD | `1,013.50` | `494.46` | `1276.40` | `4314.74` | -792,497.66 USD | `-61.26%` | `10X Cross` |
| `1658` | `0xe282...df29` | `LONG` | 1,275,489.70 USD | `1,000.00` | `420.99` | `1276.40` | `803.37` | 854,502.84 USD | `+66.99%` | `10X Cross` |
| `1659` | `0x668c...ea2e` | `SHORT` | 1,274,900.00 USD | `1,000.00` | `1406.98` | `1276.40` | `4196.78` | 132,081.99 USD | `+10.36%` | `10X Cross` |
| `1685` | `0x17f0...094f` | `LONG` | 1,255,118.04 USD | `984.30` | `1287.23` | `1276.40` | `536.94` | -11,902.13 USD | `-0.95%` | `5X Cross` |
| `1699` | `0x51f6...2b39` | `SHORT` | 1,240,916.63 USD | `972.81` | `1299.77` | `1276.40` | `2543.43` | 23,511.07 USD | `+1.89%` | `10X Cross` |
| `1756` | `0xdf83...3cff` | `SHORT` | 1,184,559.14 USD | `928.72` | `1258.91` | `1276.40` | `1910.93` | -15,384.00 USD | `-1.30%` | `10X Cross` |
| `1761` | `0x757d...94ba` | `LONG` | 1,179,837.50 USD | `925.00` | `1558.31` | `1276.40` | `0.000000` | -261,603.08 USD | `-22.17%` | `10X Cross` |
| `1762` | `0xaa82...9556` | `LONG` | 1,179,405.39 USD | `924.13` | `1254.72` | `1276.40` | `182.47` | 19,878.71 USD | `+1.69%` | `10X Cross` |
| `1809` | `0xb911...5525` | `LONG` | 1,147,680.00 USD | `900.00` | `1294.82` | `1276.40` | `1035.37` | -17,657.82 USD | `-1.54%` | `10X Cross` |
| `1860` | `0xcf0a...856f` | `LONG` | 1,110,193.56 USD | `871.15` | `1292.19` | `1276.40` | `1003.65` | -15,501.29 USD | `-1.40%` | `4X Cross` |
| `1861` | `0x9e7e...0047` | `LONG` | 1,109,778.04 USD | `870.09` | `1284.68` | `1276.40` | `1173.81` | -8,007.37 USD | `-0.72%` | `10X Cross` |
| `1864` | `0xef96...9383` | `SHORT` | 1,107,322.34 USD | `868.42` | `1259.08` | `1276.40` | `5343.49` | -13,910.55 USD | `-1.26%` | `10X Cross` |
| `1880` | `0xdf95...7d72` | `SHORT` | 1,088,431.38 USD | `853.27` | `1074.39` | `1276.40` | `44309.34` | -171,683.94 USD | `-15.77%` | `10X Cross` |
| `1924` | `0x601c...4f54` | `SHORT` | 1,051,630.32 USD | `824.42` | `615.11` | `1276.40` | `3074.47` | -544,517.56 USD | `-51.78%` | `5X Cross` |
| `1940` | `0xae55...2236` | `LONG` | 1,043,500.45 USD | `817.47` | `1467.80` | `1276.40` | `0.000000` | -156,380.76 USD | `-14.99%` | `10X Cross` |
| `1957` | `0x2577...4897` | `SHORT` | 1,035,173.16 USD | `811.01` | `1271.22` | `1276.40` | `5237.93` | -4,202.13 USD | `-0.41%` | `10X Cross` |
| `1984` | `0x9b0f...db40` | `LONG` | 1,021,600.00 USD | `800.00` | `1268.86` | `1276.40` | `793.39` | 6,510.24 USD | `+0.64%` | `10X Cross` |
| `1985` | `0x0f02...5384` | `LONG` | 1,021,394.89 USD | `800.78` | `1290.36` | `1276.40` | `298.10` | -11,899.18 USD | `-1.16%` | `3X Cross` |
| `1991` | `0x11ee...1d1d` | `SHORT` | 1,019,520.00 USD | `800.00` | `1269.65` | `1276.40` | `1594.60` | -3,796.99 USD | `-0.37%` | `5X Cross` |
| `1998` | `0x6e8f...4364` | `LONG` | 1,012,292.40 USD | `793.65` | `1260.00` | `1276.40` | `944.10` | 12,293.40 USD | `+1.21%` | `10X Cross` |
| `1999` | `0xabdb...84ac` | `LONG` | 1,011,875.38 USD | `793.69` | `711.79` | `1276.40` | `664.51` | 446,935.02 USD | `+44.17%` | `3X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `873.68` | 6,203.13 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 6.20K USD at 873.6800 USD [API] | `2026-08-23 14:08:41` |
| `ANNOUNCEMENT` | `INFO` | `873.59` | 8,727.16 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 8.73K USD at 873.5900 USD [API] | `2026-08-23 14:08:41` |
| `ANNOUNCEMENT` | `INFO` | `1257.50` | 12.58 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 0.01K USD at 1257.5000 USD [API] | `2026-10-29 01:59:34` |
| `ANNOUNCEMENT` | `INFO` | `1256.60` | 992.71 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 0.99K USD at 1256.6000 USD [API] | `2026-10-29 01:59:31` |
| `ANNOUNCEMENT` | `INFO` | `1290.00` | 309.60 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Long: 0.31K USD at 1290.0000 USD [API] | `2026-10-27 15:21:38` |
| `ANNOUNCEMENT` | `INFO` | `1290.00` | 516.00 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Long: 0.52K USD at 1290.0000 USD [API] | `2026-10-27 15:21:38` |
| `ANNOUNCEMENT` | `INFO` | `1238.70` | 1,350.18 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 1.35K USD at 1238.7000 USD [API] | `2026-10-29 02:30:54` |
| `ANNOUNCEMENT` | `INFO` | `1234.10` | 1,814.13 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 1.81K USD at 1234.1000 USD [API] | `2026-10-29 02:35:53` |
| `ANNOUNCEMENT` | `INFO` | `1234.10` | 222.14 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 0.22K USD at 1234.1000 USD [API] | `2026-10-29 02:35:53` |
| `ANNOUNCEMENT` | `INFO` | `1234.10` | 12.34 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 0.01K USD at 1234.1000 USD [API] | `2026-10-29 02:35:53` |
| `ANNOUNCEMENT` | `INFO` | `1234.10` | 12.34 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 0.01K USD at 1234.1000 USD [API] | `2026-10-29 02:35:53` |
| `ANNOUNCEMENT` | `INFO` | `1234.80` | 3,346.31 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 3.35K USD at 1234.8000 USD [API] | `2026-10-29 02:35:52` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`1404.55` (Vol: 3,000,000.00 USD, Dist: `+9.91%`) | Long MP=`1176.48` (Vol: 3,400,000.00 USD, Dist: `--7.94%`)
  * 48H Horizon: Short MP=`1404.55` (Vol: 3,000,000.00 USD, Dist: `+9.91%`) | Long MP=`1176.48` (Vol: 3,400,000.00 USD, Dist: `--7.94%`)
  * 3D Horizon: Short MP=`1404.55` (Vol: 3,000,000.00 USD, Dist: `+9.91%`) | Long MP=`1176.48` (Vol: 3,000,000.00 USD, Dist: `--7.94%`)
  * 7D Horizon: Short MP=`1404.10` (Vol: 3,000,000.00 USD, Dist: `+9.87%`) | Long MP=`1176.74` (Vol: 4,900,000.00 USD, Dist: `--7.92%`)
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
| `5m` | `BALANCED` | 0.00 USD | 1,750.00 USD | 1,750.00 USD | 1,750.00 USD | `1` | `2026-10-30 05:00:00 UTC - 2026-10-30 05:05:00 UTC` |
| `15m` | `BALANCED` | 0.00 USD | 1,750.00 USD | 1,750.00 USD | 1,750.00 USD | `1` | `2026-10-30 05:00:00 UTC - 2026-10-30 05:15:00 UTC` |
| `1h` | `BALANCED` | 0.00 USD | 1,750.00 USD | 1,750.00 USD | 1,750.00 USD | `1` | `2026-10-30 05:00:00 UTC - 2026-10-30 06:00:00 UTC` |
| `4h` | `BALANCED` | 0.00 USD | 1,750.00 USD | 1,750.00 USD | 1,750.00 USD | `1` | `2026-10-30 04:00:00 UTC - 2026-10-30 08:00:00 UTC` |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `0 USD` | Total OI Tokens: `-`
  * 1h OI Change: `0.00%` | 4h OI Change: `0.00%` | 24h OI Change: `0.00%`
  * Exchange Breakdown: Binance=`-` | Bybit=`-` | OKX=`-` | Hyperliquid=`-`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `84.83K` | Last 24h: `134.73K` | Last 3d: `246.48K` | Last 7d: `772.71K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0097%` | **USDT OKX** | `0.0100%` |
| **USDT Bybit** | `0.0100%` | **USDT KuCoin** | `0.0100%` |
| **USDT MEXC** | `0.0097%` | **USDT BingX** | `0.0100%` |
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
| `5:00 UTC` | `1257.45` | `1259.53` | `1257.45` | `1270.05` | `1249.95` | 34,915,865.69 USD | 14,880,758.20 USD | 20,035,107.50 USD | -5,154,349.30 USD | `-14.76%` | `1B / 7S` |
| `0:00 UTC` | `1260.15` | `1262.58` | `1260.15` | `1267.95` | `1257.15` | 13,992,732.07 USD | 6,287,729.60 USD | 7,705,002.47 USD | -1,417,272.88 USD | `-10.13%` | `0B / 2S` |
| `5:00 UTC` | `1265.55` | `1265.89` | `1265.55` | `1274.25` | `1259.25` | 13,172,642.30 USD | 7,854,309.17 USD | 5,318,333.13 USD | 2,535,976.04 USD | `+19.25%` | `13B / 1S` |
| `0:00 UTC` | `1282.05` | `1279.57` | `1282.05` | `1285.35` | `1269.15` | 31,465,166.07 USD | 16,761,441.58 USD | 14,703,724.48 USD | 2,057,717.10 USD | `+6.54%` | `8B / 5S` |
| `5:00 UTC` | `1279.95` | `1280.45` | `1279.95` | `1287.45` | `1275.15` | 19,925,691.14 USD | 8,662,599.23 USD | 11,263,091.92 USD | -2,600,492.69 USD | `-13.05%` | `1B / 6S` |
| `0:00 UTC` | `1275.15` | `1271.95` | `1275.15` | `1279.35` | `1264.95` | 23,738,198.29 USD | 11,363,344.84 USD | 12,374,853.45 USD | -1,011,508.62 USD | `-4.26%` | `3B / 3S` |
| `5:00 UTC` | `1279.05` | `1280.95` | `1279.05` | `1287.45` | `1274.25` | 14,930,858.33 USD | 7,292,403.22 USD | 7,638,455.11 USD | -346,051.88 USD | `-2.32%` | `2B / 4S` |
| `0:00 UTC` | `1285.05` | `1286.06` | `1285.05` | `1289.85` | `1282.05` | 15,953,463.93 USD | 6,542,642.51 USD | 9,410,821.42 USD | -2,868,178.91 USD | `-17.98%` | `1B / 3S` |
| `5:00 UTC` | `1276.95` | `1279.23` | `1276.95` | `1286.25` | `1275.15` | 15,449,899.62 USD | 6,063,485.10 USD | 9,386,414.52 USD | -3,322,929.42 USD | `-21.51%` | `0B / 8S` |
| `0:00 UTC` | `1275.15` | `1276.59` | `1275.15` | `1281.15` | `1272.15` | 11,295,725.97 USD | 4,774,375.35 USD | 6,521,350.62 USD | -1,746,975.27 USD | `-15.47%` | `0B / 4S` |

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
| `5m` | -214,890.00 USD | -1,320,000.00 USD | **`DISTRIBUTION`** |
| `15m` | -1,310,000.00 USD | -6,330,000.00 USD | **`DISTRIBUTION`** |
| `30m` | -2,100,000.00 USD | -10,370,000.00 USD | **`DISTRIBUTION`** |
| `1h` | -119,290.00 USD | -4,540,000.00 USD | **`DISTRIBUTION`** |
| `2h` | -383,880.00 USD | -9,260,000.00 USD | **`DISTRIBUTION`** |
| `4h` | 5,640,000.00 USD | 9,170,000.00 USD | **`ACCUMULATION`** |
| `6h` | 1,150,000.00 USD | 13,900,000.00 USD | **`ACCUMULATION`** |
| `8h` | 6,400,000.00 USD | -9,710,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -5,830,000.00 USD | -18,260,000.00 USD | **`DISTRIBUTION`** |
| `24h` | 16,620,000.00 USD | 98,410,000.00 USD | **`ACCUMULATION`** |
| `1w` | 36,150,000.00 USD | 230,980,000.00 USD | **`ACCUMULATION`** |
| `30d` | 60,820,000.00 USD | -528,430,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-214.89K` | 15m=`-1.31M` | 1h=`-119.29K` | 24h=`+16.62M`
* Futures Capital Netflows: 5m=`-1.32M` | 15m=`-6.33M` | 1h=`-4.54M` | 24h=`+98.41M`
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
  * `2026-10-30 09:51:14 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 10:39:14 IST`: [forex.com] - (Sentiment: `Neutral`)
  * `2026-10-30 10:38:14 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 10:38:14 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 10:38:14 IST`: [financemagnates.com] - (Sentiment: `Neutral`)
  * `2026-10-30 07:40:14 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-30 06:40:14 IST`: [kathleenhays.substack.com] - (Sentiment: `Neutral`)
  * `2026-10-30 06:40:14 IST`: [rba.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 06:40:14 IST`: [abs.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 06:40:14 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 05:40:14 IST`: [@NodeWire] - (Sentiment: `Neutral`)
  * `2026-10-30 05:40:14 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 05:40:14 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 05:40:14 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-30 05:40:14 IST`: [media.rabobank.com] - (Sentiment: `Neutral`)


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
  * Execution Entry: `1220.62` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `1197.66` (Risk Distance: `22.96` pts)
  * +2.5R Take Profit: `1278.03`
  * Mathematical Lot Sizing: **`0.43 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `1271.65` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `1294.61` (Risk Distance: `22.96` pts)
  * +2.5R Take Profit: `1214.24`
  * Mathematical Lot Sizing: **`0.43 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`1284.88`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
