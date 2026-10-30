# 🏛️ SOVEREIGN CANDIDATE DOSSIER: ZECUSD
**Canonical Key**: `ZECUSD` | **Broker Instrument**: `ZECUSD.p` | **Asset Class**: `Crypto Altcoin`
**Timestamp**: `2026-10-30 08:36:49 IST` (`2026-10-30 03:06:49 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `1255.87` | **Live Ask Quote**: `1256.92` | **Mid Price**: `1256.39`
- **Spread Points**: `105.00` | **Spread BPS**: `8.36 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `1256.39` | VWAP Z-Score: `+0.00` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `3.14` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `50.00` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `1265.19` | Lower -3.00σ Band: `1247.60`
  * Upper +2.51σ Band: `1263.31` | Lower -2.51σ Band: `1249.48`
  * Upper +2.01σ Band: `1261.67` | Lower -2.01σ Band: `1251.12`
  * Upper +2.00σ Band: `1261.42` | Lower -2.00σ Band: `1251.37`
  * Upper +1.28σ Band: `1259.91` | Lower -1.28σ Band: `1252.88`
  * Upper +1.00σ Band: `1258.91` | Lower -1.00σ Band: `1253.88`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`1256.39` | EMA-20=`1256.39` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`1256.39` (Slope: `+0.0000`) | EMA-100=`1256.39`
  * Institutional Anchors: EMA-144=`1256.39` | EMA-200=`1256.39` (Slope: `+0.0000`) | EMA-233=`1256.39`
- **Range Boundaries**: 24H High=`1268.96` | 24H Low=`1243.83` | Weekly High=`1281.52` | Weekly Low=`1231.27`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `1262.37` (Distance: `-0.44%`)
  * Point of Control (POC) = `1229.90` (Distance: `+2.19%`)
  * Value Area Low (VAL) = `1222.17` (Distance: `+2.84%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`1309.91` | POC=`1246.71` | VAL=`1230.27`
  * Prior Day Extremes: PDH=`1396.49` | PDL=`1206.89` | PDC=`1244.38`
  * Monday Range Blueprint: High=`1267.53` | Mid=`1222.14` | Low=`1176.75`
  * Developing Weekly Value Area: Weekly VAH=`1296.14` | Weekly POC=`1239.01` | Weekly VAL=`1200.92`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`1296.00` | Low=`1180.03`
  * London Session (08:00-16:00 UTC): High=`1261.42` | Low=`1251.37`
  * New York Session (13:00-21:00 UTC): High=`1263.93` | Low=`1248.86`
  * Initial Balance (First Hour): IB High=`1260.16` | IB Low=`1252.63`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `1251.37` - `1261.42`
  * Optimal Trade Entry (OTE 0.705): `1258.91`
  * Structural Invalidation Anchor (0.786): `1266.45`

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
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 08:26:34 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `13` | `0xb83d...6e36` | `SHORT` | 65,969,022.37 USD | `52,385.47` | `1336.45` | `1257.20` | `3841.37` | 4,041,545.03 USD | `+6.13%` | `3X Cross` |
| `22` | `0x5b5d...c060` | `SHORT` | 50,506,983.77 USD | `40,121.38` | `1478.36` | `1257.20` | `5349.92` | 8,807,051.34 USD | `+17.44%` | `3X Cross` |
| `40` | `0x7fda...17d1` | `SHORT` | 30,222,864.24 USD | `24,037.91` | `1261.37` | `1257.20` | `2802.82` | 97,922.44 USD | `+0.32%` | `5X Cross` |
| `79` | `0x60b0...991e` | `LONG` | 21,112,268.87 USD | `16,779.74` | `1179.65` | `1257.20` | `943.86` | 1,318,021.85 USD | `+6.24%` | `10X Cross` |
| `139` | `0xc36a...105b` | `LONG` | 14,478,309.40 USD | `11,510.82` | `1215.14` | `1257.20` | `976.04` | 491,028.37 USD | `+3.39%` | `10X Cross` |
| `155` | `0x9071...5c0b` | `LONG` | 13,237,061.19 USD | `10,517.29` | `1353.83` | `1257.20` | `0.0812` | -1,001,557.68 USD | `-7.57%` | `1X Cross` |
| `179` | `0x8742...8427` | `LONG` | 11,580,642.91 USD | `9,201.21` | `1286.37` | `1257.20` | `718.20` | -255,527.09 USD | `-2.21%` | `10X Cross` |
| `191` | `0x58b2...11f3` | `LONG` | 10,782,176.49 USD | `8,563.08` | `1246.56` | `1257.20` | `382.39` | 107,758.92 USD | `+1.00%` | `10X Cross` |
| `195` | `0x9ffd...ce40` | `LONG` | 10,652,614.20 USD | `8,468.57` | `1250.90` | `1257.20` | `606.82` | 59,237.11 USD | `+0.56%` | `5X Cross` |
| `199` | `0xad59...ba81` | `SHORT` | 10,599,492.50 USD | `8,425.00` | `330.91` | `1257.20` | `2147.28` | -7,811,534.73 USD | `-73.70%` | `10X Cross` |
| `206` | `0xdd53...2b13` | `SHORT` | 10,304,730.22 USD | `8,195.92` | `741.54` | `1257.20` | `8906.78` | -4,227,133.85 USD | `-41.02%` | `3X Cross` |
| `223` | `0x880a...311c` | `SHORT` | 9,690,920.11 USD | `7,707.11` | `1367.50` | `1257.20` | `2243.38` | 848,564.09 USD | `+8.76%` | `10X Cross` |
| `237` | `0xbf73...5d58` | `LONG` | 9,443,602.50 USD | `7,500.00` | `1248.78` | `1257.20` | `148.16` | 77,756.88 USD | `+0.82%` | `10X Cross` |
| `268` | `0x2b61...2f6c` | `LONG` | 8,561,844.60 USD | `6,807.00` | `1453.56` | `1257.20` | `536.31` | -1,332,506.62 USD | `-15.56%` | `10X Cross` |
| `289` | `0x2ae5...83e7` | `LONG` | 8,091,701.28 USD | `6,436.80` | `1391.82` | `1257.20` | `0.000000` | -867,190.71 USD | `-10.72%` | `1X Cross` |
| `331` | `0x26b6...9a13` | `LONG` | 6,872,038.33 USD | `5,433.73` | `1282.23` | `1257.20` | `228.42` | -95,264.90 USD | `-1.39%` | `10X Cross` |
| `346` | `0x45d2...4029` | `SHORT` | 6,578,702.20 USD | `5,227.00` | `833.44` | `1257.20` | `9417.59` | -2,222,324.23 USD | `-33.78%` | `5X Cross` |
| `361` | `0xea00...a918` | `LONG` | 6,295,500.00 USD | `5,000.00` | `739.16` | `1257.20` | `0.000000` | 2,599,684.89 USD | `+41.29%` | `5X Cross` |
| `373` | `0xdd7a...8830` | `LONG` | 6,114,119.02 USD | `4,860.19` | `897.48` | `1257.20` | `792.50` | 1,752,215.35 USD | `+28.66%` | `10X Cross` |
| `379` | `0xecb6...2b00` | `SHORT` | 5,942,766.75 USD | `4,726.61` | `1279.01` | `1257.20` | `7144.09` | 102,594.49 USD | `+1.73%` | `5X Cross` |
| `436` | `0xa61c...66b9` | `LONG` | 4,891,104.00 USD | `3,888.00` | `1148.34` | `1257.20` | `0.000000` | 426,361.86 USD | `+8.72%` | `10X Cross` |
| `448` | `0x469e...58a5` | `SHORT` | 4,784,859.26 USD | `3,799.92` | `1238.77` | `1257.20` | `2031.63` | -77,613.54 USD | `-1.62%` | `10X Cross` |
| `459` | `0x9aa5...58af` | `SHORT` | 4,677,917.79 USD | `3,720.31` | `1205.51` | `1257.20` | `3759.94` | -193,030.99 USD | `-4.13%` | `10X Cross` |
| `463` | `0x0153...8052` | `SHORT` | 4,648,982.08 USD | `3,698.18` | `1307.82` | `1257.20` | `2504.79` | 187,588.67 USD | `+4.04%` | `1X Isolated` |
| `513` | `0x4cae...7c34` | `LONG` | 4,276,859.61 USD | `3,400.27` | `1139.92` | `1257.20` | `938.64` | 400,832.01 USD | `+9.37%` | `10X Cross` |
| `528` | `0x382b...3e39` | `LONG` | 4,153,804.88 USD | `3,303.75` | `1215.08` | `1257.20` | `0.000000` | 139,485.49 USD | `+3.36%` | `10X Cross` |
| `529` | `0x456f...cdf1` | `LONG` | 4,139,842.88 USD | `3,290.29` | `1267.66` | `1257.20` | `533.20` | -31,118.20 USD | `-0.75%` | `10X Cross` |
| `538` | `0xd21d...90f1` | `LONG` | 4,088,825.00 USD | `3,250.00` | `1253.64` | `1257.20` | `876.00` | 14,483.27 USD | `+0.35%` | `4X Isolated` |
| `554` | `0x1338...c48e` | `LONG` | 3,960,611.68 USD | `3,149.43` | `1018.52` | `1257.20` | `820.29` | 752,866.14 USD | `+19.01%` | `4X Isolated` |
| `565` | `0x325e...9564` | `LONG` | 3,902,202.78 USD | `3,101.91` | `1298.07` | `1257.20` | `216.25` | -124,307.92 USD | `-3.19%` | `10X Cross` |
| `572` | `0xdbe0...d6d5` | `LONG` | 3,878,618.63 USD | `3,085.37` | `422.97` | `1257.20` | `338.61` | 2,573,614.13 USD | `+66.35%` | `3X Isolated` |
| `594` | `0xd4c1...3d1d` | `SHORT` | 3,761,514.70 USD | `2,991.74` | `1296.64` | `1257.20` | `2800.95` | 117,685.06 USD | `+3.13%` | `10X Cross` |
| `595` | `0x9c06...0560` | `SHORT` | 3,760,869.42 USD | `2,989.80` | `786.00` | `1257.20` | `2625.19` | -1,410,874.42 USD | `-37.51%` | `10X Cross` |
| `599` | `0x27c9...d65d` | `SHORT` | 3,724,755.44 USD | `2,961.88` | `1254.41` | `1257.20` | `1741.84` | -9,340.23 USD | `-0.25%` | `10X Cross` |
| `601` | `0x2e30...4cb5` | `SHORT` | 3,715,346.48 USD | `2,955.49` | `1288.00` | `1257.20` | `2913.84` | 91,334.52 USD | `+2.46%` | `2X Cross` |
| `605` | `0x5323...b23c` | `SHORT` | 3,697,430.12 USD | `2,940.77` | `1260.37` | `1257.20` | `3108.53` | 9,028.08 USD | `+0.24%` | `5X Cross` |
| `692` | `0xa183...0482` | `LONG` | 3,186,251.60 USD | `2,534.00` | `530.25` | `1257.20` | `444.53` | 1,842,588.88 USD | `+57.83%` | `5X Isolated` |
| `694` | `0xac48...3201` | `LONG` | 3,185,133.30 USD | `2,531.50` | `1378.58` | `1257.20` | `500.92` | -304,738.98 USD | `-9.57%` | `10X Cross` |
| `704` | `0x0871...e927` | `LONG` | 3,144,500.00 USD | `2,500.00` | `1276.50` | `1257.20` | `0.000000` | -46,750.00 USD | `-1.49%` | `10X Cross` |
| `718` | `0x9b86...6e6e` | `LONG` | 3,102,071.13 USD | `2,463.30` | `637.58` | `1257.20` | `882.46` | 1,531,521.85 USD | `+49.37%` | `3X Cross` |
| `760` | `0x71d0...8c26` | `SHORT` | 2,982,753.98 USD | `2,372.16` | `1262.12` | `1257.20` | `3765.25` | 11,201.43 USD | `+0.38%` | `10X Cross` |
| `777` | `0xb2f7...af9f` | `SHORT` | 2,913,702.76 USD | `2,313.72` | `746.63` | `1257.20` | `4555.83` | -1,186,214.02 USD | `-40.71%` | `10X Cross` |
| `799` | `0x413c...886c` | `LONG` | 2,833,459.20 USD | `2,250.00` | `1237.51` | `1257.20` | `0.000000` | 49,058.17 USD | `+1.73%` | `10X Cross` |
| `809` | `0xf48f...10fe` | `LONG` | 2,791,082.27 USD | `2,218.49` | `1517.87` | `1257.20` | `1029.90` | -576,304.56 USD | `-20.65%` | `3X Cross` |
| `837` | `0x5bc4...3b0c` | `SHORT` | 2,678,979.40 USD | `2,130.74` | `1089.65` | `1257.20` | `3729.58` | -357,221.82 USD | `-13.33%` | `5X Cross` |
| `852` | `0x8de4...b9aa` | `SHORT` | 2,633,241.53 USD | `2,091.29` | `1331.35` | `1257.20` | `1689.91` | 150,998.18 USD | `+5.73%` | `3X Cross` |
| `861` | `0x4fe2...ac59` | `SHORT` | 2,606,449.37 USD | `2,071.57` | `1478.56` | `1257.20` | `1856.36` | 456,496.84 USD | `+17.51%` | `10X Cross` |
| `869` | `0xdf57...93f5` | `LONG` | 2,582,934.25 USD | `2,054.35` | `1227.36` | `1257.20` | `897.24` | 61,512.21 USD | `+2.38%` | `4X Isolated` |
| `878` | `0xbcd4...0dd2` | `LONG` | 2,561,346.37 USD | `2,033.92` | `1228.20` | `1257.20` | `681.41` | 63,295.56 USD | `+2.47%` | `10X Cross` |
| `891` | `0x9a99...d21a` | `LONG` | 2,517,709.20 USD | `2,000.00` | `1278.44` | `1257.20` | `0.000000` | -39,164.47 USD | `-1.56%` | `10X Cross` |
| `892` | `0xf29c...9971` | `LONG` | 2,514,800.00 USD | `2,000.00` | `1254.95` | `1257.20` | `0.000000` | 4,902.93 USD | `+0.19%` | `10X Cross` |
| `913` | `0x77ee...2902` | `SHORT` | 2,447,668.47 USD | `1,946.03` | `759.84` | `1257.20` | `5458.26` | -968,990.96 USD | `-39.59%` | `10X Cross` |
| `922` | `0x3e2f...b269` | `SHORT` | 2,420,943.72 USD | `1,925.51` | `1134.87` | `1257.20` | `2931.84` | -235,744.87 USD | `-9.74%` | `10X Cross` |
| `928` | `0xb122...e4ba` | `LONG` | 2,397,965.63 USD | `1,905.87` | `1255.41` | `1257.20` | `965.60` | 5,313.57 USD | `+0.22%` | `10X Cross` |
| `936` | `0x4f12...618b` | `SHORT` | 2,385,330.61 USD | `1,896.28` | `1608.30` | `1257.20` | `2116.80` | 664,453.78 USD | `+27.86%` | `3X Cross` |
| `975` | `0x866d...d6e1` | `LONG` | 2,266,618.49 USD | `1,802.05` | `674.73` | `1257.20` | `305.92` | 1,050,717.18 USD | `+46.36%` | `10X Cross` |
| `993` | `0x2309...a2d9` | `LONG` | 2,201,615.39 USD | `1,750.37` | `1186.09` | `1257.20` | `817.88` | 125,521.28 USD | `+5.70%` | `8X Cross` |
| `1034` | `0x265e...7f70` | `LONG` | 2,077,723.75 USD | `1,651.74` | `1382.98` | `1257.20` | `0.000000` | -206,599.01 USD | `-9.94%` | `3X Cross` |
| `1040` | `0xfe7c...b7ae` | `SHORT` | 2,065,291.27 USD | `1,642.64` | `1346.92` | `1257.20` | `5960.04` | 147,217.35 USD | `+7.13%` | `10X Cross` |
| `1046` | `0x3e47...aaf6` | `LONG` | 2,060,592.28 USD | `1,636.28` | `1278.38` | `1257.20` | `1053.03` | -31,199.51 USD | `-1.51%` | `10X Cross` |
| `1048` | `0x2edd...8179` | `SHORT` | 2,055,433.62 USD | `1,633.89` | `1261.58` | `1257.20` | `2940.08` | 5,848.30 USD | `+0.28%` | `10X Cross` |
| `1055` | `0x3205...40bb` | `SHORT` | 2,034,537.71 USD | `1,618.18` | `1244.68` | `1257.20` | `2171.94` | -20,426.56 USD | `-1.00%` | `10X Cross` |
| `1066` | `0x7f75...9edf` | `LONG` | 2,019,910.66 USD | `1,605.78` | `1199.97` | `1257.20` | `981.01` | 93,018.77 USD | `+4.61%` | `10X Cross` |
| `1069` | `0x6646...6de5` | `SHORT` | 2,011,360.00 USD | `1,600.00` | `660.64` | `1257.20` | `4087.48` | -954,335.03 USD | `-47.45%` | `10X Cross` |
| `1075` | `0x023a...2355` | `SHORT` | 2,005,427.26 USD | `1,594.90` | `1310.00` | `1257.20` | `4519.73` | 83,884.88 USD | `+4.18%` | `10X Cross` |
| `1103` | `0xab59...59b5` | `LONG` | 1,969,329.09 USD | `1,565.32` | `1342.15` | `1257.20` | `846.29` | -131,566.13 USD | `-6.68%` | `10X Cross` |
| `1155` | `0xcf67...eb24` | `LONG` | 1,886,850.00 USD | `1,500.00` | `887.05` | `1257.20` | `710.04` | 556,278.63 USD | `+29.48%` | `10X Cross` |
| `1165` | `0xb695...a92d` | `LONG` | 1,864,724.20 USD | `1,483.00` | `1249.80` | `1257.20` | `0.000000` | 11,265.34 USD | `+0.60%` | `10X Cross` |
| `1172` | `0x7277...0b98` | `SHORT` | 1,856,528.84 USD | `1,475.73` | `1287.86` | `1257.20` | `2212.86` | 44,003.28 USD | `+2.37%` | `10X Cross` |
| `1238` | `0x2ab7...c2f8` | `LONG` | 1,760,581.12 USD | `1,400.51` | `813.26` | `1257.20` | `793.71` | 621,599.44 USD | `+35.31%` | `3X Cross` |
| `1253` | `0x11be...8b1d` | `LONG` | 1,731,069.31 USD | `1,375.83` | `1206.55` | `1257.20` | `1134.51` | 71,061.35 USD | `+4.11%` | `10X Isolated` |
| `1293` | `0xfc27...9d9d` | `SHORT` | 1,658,655.45 USD | `1,319.43` | `1298.53` | `1257.20` | `15790.87` | 54,661.32 USD | `+3.30%` | `10X Cross` |
| `1323` | `0x039c...0ebd` | `SHORT` | 1,611,639.55 USD | `1,279.79` | `1239.81` | `1257.20` | `3678.07` | -24,937.72 USD | `-1.55%` | `10X Cross` |
| `1348` | `0xe065...0f85` | `SHORT` | 1,588,237.12 USD | `1,262.61` | `1087.02` | `1257.20` | `1622.25` | -215,760.99 USD | `-13.58%` | `10X Cross` |
| `1414` | `0x266b...efcb` | `LONG` | 1,517,760.00 USD | `1,200.00` | `893.76` | `1257.20` | `422.81` | 445,250.30 USD | `+29.34%` | `10X Cross` |
| `1423` | `0x5975...9abd` | `LONG` | 1,509,840.00 USD | `1,200.00` | `1179.54` | `1257.20` | `583.01` | 94,397.21 USD | `+6.25%` | `5X Cross` |
| `1441` | `0x2847...d47b` | `LONG` | 1,492,090.41 USD | `1,186.27` | `1232.07` | `1257.20` | `0.000000` | 30,521.91 USD | `+2.05%` | `5X Cross` |
| `1462` | `0x69cc...14fd` | `SHORT` | 1,461,038.50 USD | `1,161.36` | `675.33` | `1257.20` | `8173.56` | -676,732.97 USD | `-46.32%` | `10X Cross` |
| `1477` | `0x3fc5...c0c1` | `SHORT` | 1,444,048.46 USD | `1,148.44` | `1264.34` | `1257.20` | `2921.01` | 7,965.32 USD | `+0.55%` | `10X Cross` |
| `1486` | `0x38f9...cb04` | `SHORT` | 1,434,718.55 USD | `1,141.02` | `1243.50` | `1257.20` | `2015.99` | -15,864.70 USD | `-1.11%` | `10X Cross` |
| `1507` | `0xe35c...a1d3` | `LONG` | 1,417,841.48 USD | `1,127.06` | `1318.20` | `1257.20` | `694.43` | -67,853.87 USD | `-4.79%` | `2X Isolated` |
| `1516` | `0x5f94...4b96` | `LONG` | 1,404,476.46 USD | `1,115.27` | `538.00` | `1257.20` | `0.000000` | 804,458.83 USD | `+57.28%` | `10X Cross` |
| `1537` | `0x71df...a23d` | `SHORT` | 1,381,416.58 USD | `1,098.28` | `513.50` | `1257.20` | `2559.36` | -817,446.39 USD | `-59.17%` | `2X Cross` |
| `1561` | `0xbfc7...80b4` | `SHORT` | 1,351,705.00 USD | `1,075.00` | `558.03` | `1257.20` | `3071.24` | -751,826.27 USD | `-55.62%` | `10X Cross` |
| `1600` | `0x51f6...2b39` | `SHORT` | 1,304,182.52 USD | `1,037.07` | `1299.77` | `1257.20` | `2489.27` | 43,768.30 USD | `+3.36%` | `10X Cross` |
| `1636` | `0x123d...3bff` | `SHORT` | 1,270,329.05 USD | `1,009.64` | `491.08` | `1257.20` | `4423.11` | -774,511.14 USD | `-60.97%` | `10X Cross` |
| `1645` | `0xe282...df29` | `LONG` | 1,258,000.00 USD | `1,000.00` | `420.99` | `1257.20` | `842.82` | 837,013.14 USD | `+66.54%` | `10X Cross` |
| `1646` | `0x668c...ea2e` | `SHORT` | 1,257,900.00 USD | `1,000.00` | `1406.98` | `1257.20` | `4184.09` | 149,081.99 USD | `+11.85%` | `10X Cross` |
| `1674` | `0x17f0...094f` | `LONG` | 1,238,052.54 USD | `984.30` | `1287.23` | `1257.20` | `536.86` | -28,967.62 USD | `-2.34%` | `5X Cross` |
| `1749` | `0x757d...94ba` | `LONG` | 1,163,002.50 USD | `925.00` | `1558.31` | `1257.20` | `0.000000` | -278,438.09 USD | `-23.94%` | `10X Cross` |
| `1750` | `0xaa82...9556` | `LONG` | 1,162,593.43 USD | `924.13` | `1254.72` | `1257.20` | `185.25` | 3,066.75 USD | `+0.26%` | `10X Cross` |
| `1793` | `0xb911...5525` | `LONG` | 1,132,380.00 USD | `900.00` | `1294.82` | `1257.20` | `1070.38` | -32,957.82 USD | `-2.91%` | `10X Cross` |
| `1841` | `0xcf0a...856f` | `LONG` | 1,095,819.58 USD | `871.15` | `1292.19` | `1257.20` | `1009.00` | -29,875.26 USD | `-2.73%` | `4X Cross` |
| `1848` | `0xef96...9383` | `SHORT` | 1,092,646.04 USD | `868.42` | `1259.08` | `1257.20` | `5504.61` | 765.75 USD | `+0.07%` | `10X Cross` |
| `1871` | `0xdf95...7d72` | `SHORT` | 1,072,901.70 USD | `853.27` | `1074.39` | `1257.20` | `46366.58` | -156,154.26 USD | `-14.55%` | `10X Cross` |
| `1905` | `0x601c...4f54` | `SHORT` | 1,036,761.41 USD | `824.42` | `615.11` | `1257.20` | `3156.39` | -529,648.66 USD | `-51.09%` | `5X Cross` |
| `1908` | `0x2577...4897` | `SHORT` | 1,034,129.25 USD | `822.50` | `1262.84` | `1257.20` | `5101.87` | 4,559.45 USD | `+0.44%` | `10X Cross` |
| `1919` | `0xae55...2236` | `LONG` | 1,027,641.54 USD | `817.47` | `1467.80` | `1257.20` | `0.000000` | -172,239.68 USD | `-16.76%` | `10X Cross` |
| `1947` | `0x9b0f...db40` | `LONG` | 1,011,840.00 USD | `800.00` | `1268.86` | `1257.20` | `801.88` | -3,249.76 USD | `-0.32%` | `10X Cross` |
| `1958` | `0x11ee...1d1d` | `SHORT` | 1,007,360.00 USD | `800.00` | `1269.65` | `1257.20` | `1615.80` | 8,363.01 USD | `+0.83%` | `5X Cross` |
| `1960` | `0x0f02...5384` | `LONG` | 1,007,301.16 USD | `800.78` | `1290.36` | `1257.20` | `310.27` | -25,992.91 USD | `-2.58%` | `3X Cross` |

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
| `5m` | `BALANCED` | 0.00 USD | 1,750.00 USD | 1,750.00 USD | 1,750.00 USD | `1` | `2026-10-30 02:55:00 UTC - 2026-10-30 03:00:00 UTC` |
| `15m` | `BALANCED` | 0.00 USD | 1,750.00 USD | 1,750.00 USD | 1,750.00 USD | `1` | `2026-10-30 02:45:00 UTC - 2026-10-30 03:00:00 UTC` |
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
| `0:00 UTC` | `1197.75` | `1211.98` | `1197.75` | `1236.15` | `1189.35` | 90,739,097.90 USD | 52,854,086.90 USD | 37,885,011.00 USD | 14,969,075.89 USD | `+16.50%` | `25B / 1S` |
| `5:00 UTC` | `1232.55` | `1227.83` | `1232.55` | `1237.35` | `1215.45` | 35,400,223.44 USD | 18,306,250.09 USD | 17,093,973.35 USD | 1,212,276.73 USD | `+3.42%` | `7B / 4S` |
| `0:00 UTC` | `1230.15` | `1232.52` | `1230.15` | `1240.05` | `1225.05` | 27,822,128.62 USD | 14,746,863.10 USD | 13,075,265.52 USD | 1,671,597.57 USD | `+6.01%` | `5B / 1S` |
| `5:00 UTC` | `1219.95` | `1220.53` | `1219.95` | `1230.45` | `1215.45` | 25,624,282.39 USD | 13,502,208.52 USD | 12,122,073.88 USD | 1,380,134.64 USD | `+5.39%` | `6B / 3S` |
| `0:00 UTC` | `1245.15` | `1232.68` | `1245.15` | `1249.05` | `1206.75` | 51,931,159.61 USD | 26,761,787.01 USD | 25,169,372.61 USD | 1,592,414.40 USD | `+3.07%` | `20B / 9S` |
| `5:00 UTC` | `1236.45` | `1237.15` | `1236.45` | `1245.15` | `1230.45` | 21,904,768.45 USD | 9,625,705.12 USD | 12,279,063.33 USD | -2,653,358.20 USD | `-12.11%` | `1B / 0S` |
| `0:00 UTC` | `1228.65` | `1236.25` | `1228.65` | `1253.25` | `1219.35` | 45,146,863.08 USD | 23,450,812.50 USD | 21,696,050.59 USD | 1,754,761.91 USD | `+3.89%` | `18B / 9S` |
| `5:00 UTC` | `1254.75` | `1256.85` | `1254.75` | `1263.45` | `1247.85` | 37,496,922.68 USD | 20,689,312.95 USD | 16,807,609.72 USD | 3,881,703.23 USD | `+10.35%` | `5B / 3S` |
| `0:00 UTC` | `1263.45` | `1263.47` | `1263.45` | `1267.65` | `1258.35` | 21,490,941.27 USD | 11,626,504.00 USD | 9,864,437.27 USD | 1,762,066.74 USD | `+8.20%` | `2B / 3S` |
| `5:00 UTC` | `1263.45` | `1264.27` | `1263.45` | `1270.05` | `1260.15` | 11,854,596.42 USD | 6,285,096.02 USD | 5,569,500.40 USD | 715,595.62 USD | `+6.04%` | `1B / 3S` |

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
| `5m` | -1,540,000.00 USD | -1,470,000.00 USD | **`DISTRIBUTION`** |
| `15m` | 87,750.00 USD | 1,580,000.00 USD | **`ACCUMULATION`** |
| `30m` | -56,940.00 USD | 5,820,000.00 USD | **`ACCUMULATION`** |
| `1h` | 5,200,000.00 USD | 14,910,000.00 USD | **`ACCUMULATION`** |
| `2h` | 4,620,000.00 USD | 26,910,000.00 USD | **`ACCUMULATION`** |
| `4h` | -102,370.00 USD | 19,510,000.00 USD | **`ACCUMULATION`** |
| `6h` | 3,290,000.00 USD | 33,640,000.00 USD | **`ACCUMULATION`** |
| `8h` | -10,820,000.00 USD | -11,010,000.00 USD | **`DISTRIBUTION`** |
| `12h` | 10,120,000.00 USD | 84,450,000.00 USD | **`ACCUMULATION`** |
| `24h` | 10,810,000.00 USD | 118,250,000.00 USD | **`ACCUMULATION`** |
| `1w` | 32,820,000.00 USD | 241,330,000.00 USD | **`ACCUMULATION`** |
| `30d` | 59,730,000.00 USD | -523,550,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-1.54M` | 15m=`+87.75K` | 1h=`+5.20M` | 24h=`+10.81M`
* Futures Capital Netflows: 5m=`-1.47M` | 15m=`+1.58M` | 1h=`+14.91M` | 24h=`+118.25M`
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
  * Spread-Padded Stop Loss: `1216.83` (Risk Distance: `5.34` pts)
  * +2.5R Take Profit: `1235.53`
  * Mathematical Lot Sizing: **`1.87 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `1262.37` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `1267.71` (Risk Distance: `5.34` pts)
  * +2.5R Take Profit: `1249.01`
  * Mathematical Lot Sizing: **`1.87 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`1266.45`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
