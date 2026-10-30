# 🏛️ SOVEREIGN CANDIDATE DOSSIER: ZECUSD
**Canonical Key**: `ZECUSD` | **Broker Instrument**: `ZECUSD.p` | **Asset Class**: `Crypto Altcoin`
**Timestamp**: `2026-10-30 10:04:33 IST` (`2026-10-30 04:34:33 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `1285.19` | **Live Ask Quote**: `1286.14` | **Mid Price**: `1285.66`
- **Spread Points**: `95.00` | **Spread BPS**: `7.39 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `1285.66` | VWAP Z-Score: `+0.00` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `3.21` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `50.00` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `1294.66` | Lower -3.00σ Band: `1276.67`
  * Upper +2.51σ Band: `1292.74` | Lower -2.51σ Band: `1278.59`
  * Upper +2.01σ Band: `1291.06` | Lower -2.01σ Band: `1280.27`
  * Upper +2.00σ Band: `1290.81` | Lower -2.00σ Band: `1280.52`
  * Upper +1.28σ Band: `1289.26` | Lower -1.28σ Band: `1282.07`
  * Upper +1.00σ Band: `1288.24` | Lower -1.00σ Band: `1283.09`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`1285.66` | EMA-20=`1285.66` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`1285.66` (Slope: `+0.0000`) | EMA-100=`1285.66`
  * Institutional Anchors: EMA-144=`1285.66` | EMA-200=`1285.66` (Slope: `+0.0000`) | EMA-233=`1285.66`
- **Range Boundaries**: 24H High=`1298.52` | 24H Low=`1272.81` | Weekly High=`1311.38` | Weekly Low=`1259.95`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `1269.33` (Distance: `+1.30%`)
  * Point of Control (POC) = `1229.90` (Distance: `+4.55%`)
  * Value Area Low (VAL) = `1222.17` (Distance: `+5.21%`)
  * Auction Positioning: `ABOVE_VALUE (Imbalance)` | Session Bias: **`BULLISH (Above Pivot)`** | Market Regime: `RANGE_EXPANSION`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`1309.91` | POC=`1246.71` | VAL=`1230.27`
  * Prior Day Extremes: PDH=`1396.49` | PDL=`1206.89` | PDC=`1244.38`
  * Monday Range Blueprint: High=`1267.53` | Mid=`1222.14` | Low=`1176.75`
  * Developing Weekly Value Area: Weekly VAH=`1296.14` | Weekly POC=`1239.01` | Weekly VAL=`1200.92`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`1296.00` | Low=`1180.03`
  * London Session (08:00-16:00 UTC): High=`1290.81` | Low=`1280.52`
  * New York Session (13:00-21:00 UTC): High=`1293.38` | Low=`1277.95`
  * Initial Balance (First Hour): IB High=`1289.52` | IB Low=`1281.81`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `1280.52` - `1290.81`
  * Optimal Trade Entry (OTE 0.705): `1288.24`
  * Structural Invalidation Anchor (0.786): `1295.95`

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
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 10:01:04 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `13` | `0xb83d...6e36` | `SHORT` | 67,456,769.72 USD | `52,385.47` | `1336.45` | `1288.50` | `3698.57` | 2,553,797.68 USD | `+3.79%` | `3X Cross` |
| `22` | `0x5b5d...c060` | `SHORT` | 51,732,507.37 USD | `40,121.38` | `1478.36` | `1288.50` | `5115.80` | 7,581,527.74 USD | `+14.66%` | `3X Cross` |
| `39` | `0x7fda...17d1` | `SHORT` | 33,095,045.21 USD | `25,641.16` | `1262.27` | `1288.50` | `2640.65` | -728,958.84 USD | `-2.20%` | `5X Cross` |
| `79` | `0x60b0...991e` | `LONG` | 21,622,372.96 USD | `16,779.74` | `1179.65` | `1288.50` | `926.68` | 1,828,125.95 USD | `+8.45%` | `10X Cross` |
| `137` | `0xc36a...105b` | `LONG` | 14,842,051.31 USD | `11,510.82` | `1215.14` | `1288.50` | `964.32` | 854,770.28 USD | `+5.76%` | `10X Cross` |
| `152` | `0x9071...5c0b` | `LONG` | 13,576,769.66 USD | `10,517.29` | `1353.83` | `1288.50` | `0.1437` | -661,849.21 USD | `-4.87%` | `1X Cross` |
| `172` | `0x8742...8427` | `LONG` | 11,877,841.99 USD | `9,201.21` | `1286.37` | `1288.50` | `700.05` | 41,672.00 USD | `+0.35%` | `10X Cross` |
| `188` | `0x58b2...11f3` | `LONG` | 11,037,810.12 USD | `8,563.08` | `1246.56` | `1288.50` | `381.37` | 363,392.55 USD | `+3.29%` | `10X Cross` |
| `194` | `0xad59...ba81` | `SHORT` | 10,852,242.50 USD | `8,425.00` | `330.91` | `1288.50` | `2144.69` | -8,064,284.73 USD | `-74.31%` | `10X Cross` |
| `197` | `0x9ffd...ce40` | `LONG` | 10,755,880.66 USD | `8,333.37` | `1251.31` | `1288.50` | `591.28` | 328,216.97 USD | `+3.05%` | `5X Cross` |
| `202` | `0xdd53...2b13` | `SHORT` | 10,578,473.94 USD | `8,195.92` | `741.54` | `1288.50` | `8517.63` | -4,500,877.58 USD | `-42.55%` | `3X Cross` |
| `217` | `0x880a...311c` | `SHORT` | 9,937,547.63 USD | `7,707.11` | `1367.50` | `1288.50` | `2244.60` | 601,936.57 USD | `+6.06%` | `10X Cross` |
| `233` | `0xbf73...5d58` | `LONG` | 9,670,500.00 USD | `7,500.00` | `1248.78` | `1288.50` | `124.01` | 304,654.38 USD | `+3.15%` | `10X Cross` |
| `265` | `0x2b61...2f6c` | `LONG` | 8,776,945.80 USD | `6,807.00` | `1453.56` | `1288.50` | `567.19` | -1,117,405.42 USD | `-12.73%` | `10X Cross` |
| `284` | `0x2ae5...83e7` | `LONG` | 8,309,265.12 USD | `6,436.80` | `1391.82` | `1288.50` | `0.000000` | -649,626.87 USD | `-7.82%` | `1X Cross` |
| `330` | `0x26b6...9a13` | `LONG` | 7,014,402.06 USD | `5,433.73` | `1282.23` | `1288.50` | `219.57` | 47,098.82 USD | `+0.67%` | `10X Cross` |
| `336` | `0x45d2...4029` | `SHORT` | 6,747,534.30 USD | `5,227.00` | `833.44` | `1288.50` | `8918.79` | -2,391,156.33 USD | `-35.44%` | `5X Cross` |
| `349` | `0xecb6...2b00` | `SHORT` | 6,654,748.06 USD | `5,157.52` | `1279.09` | `1288.50` | `6376.32` | -57,831.95 USD | `-0.87%` | `5X Cross` |
| `360` | `0xea00...a918` | `LONG` | 6,443,000.00 USD | `5,000.00` | `739.16` | `1288.50` | `0.000000` | 2,747,184.89 USD | `+42.64%` | `5X Cross` |
| `374` | `0xdd7a...8830` | `LONG` | 6,259,438.70 USD | `4,860.19` | `897.48` | `1288.50` | `786.04` | 1,897,535.03 USD | `+30.31%` | `10X Cross` |
| `413` | `0x469e...58a5` | `SHORT` | 5,368,442.69 USD | `4,163.52` | `1242.31` | `1288.50` | `1969.96` | -196,058.03 USD | `-3.65%` | `10X Cross` |
| `425` | `0x4cae...7c34` | `LONG` | 5,148,520.13 USD | `4,002.27` | `1169.72` | `1288.50` | `979.59` | 466,970.78 USD | `+9.07%` | `10X Cross` |
| `436` | `0xa61c...66b9` | `LONG` | 5,007,355.20 USD | `3,888.00` | `1148.34` | `1288.50` | `0.000000` | 542,613.06 USD | `+10.84%` | `10X Cross` |
| `457` | `0x9aa5...58af` | `SHORT` | 4,801,804.12 USD | `3,720.31` | `1205.51` | `1288.50` | `3688.80` | -316,917.32 USD | `-6.60%` | `10X Cross` |
| `462` | `0x0153...8052` | `SHORT` | 4,773,980.56 USD | `3,698.18` | `1307.82` | `1288.50` | `2504.85` | 62,590.19 USD | `+1.31%` | `1X Isolated` |
| `489` | `0xd4c1...3d1d` | `SHORT` | 4,564,952.37 USD | `3,537.90` | `1293.44` | `1288.50` | `2460.85` | 11,126.36 USD | `+0.24%` | `10X Cross` |
| `522` | `0x382b...3e39` | `LONG` | 4,255,541.16 USD | `3,297.08` | `1215.08` | `1288.50` | `0.000000` | 249,326.35 USD | `+5.86%` | `10X Cross` |
| `531` | `0xd21d...90f1` | `LONG` | 4,186,325.00 USD | `3,250.00` | `1253.64` | `1288.50` | `876.06` | 111,983.27 USD | `+2.67%` | `4X Isolated` |
| `547` | `0x456f...cdf1` | `LONG` | 4,083,581.19 USD | `3,163.85` | `1267.75` | `1288.50` | `499.97` | 72,620.33 USD | `+1.78%` | `10X Cross` |
| `550` | `0x1338...c48e` | `LONG` | 4,060,875.04 USD | `3,149.43` | `1018.52` | `1288.50` | `820.35` | 853,129.50 USD | `+21.01%` | `4X Isolated` |
| `562` | `0x325e...9564` | `LONG` | 3,994,949.89 USD | `3,101.91` | `1298.07` | `1288.50` | `151.64` | -31,560.81 USD | `-0.79%` | `10X Cross` |
| `563` | `0xdbe0...d6d5` | `LONG` | 3,982,904.13 USD | `3,085.37` | `422.97` | `1288.50` | `338.67` | 2,677,899.64 USD | `+67.23%` | `3X Isolated` |
| `571` | `0x2e30...4cb5` | `SHORT` | 3,946,462.03 USD | `3,057.14` | `1287.36` | `1288.50` | `2840.23` | -10,831.39 USD | `-0.27%` | `2X Cross` |
| `590` | `0x9c06...0560` | `SHORT` | 3,844,583.82 USD | `2,989.80` | `786.00` | `1288.50` | `2586.99` | -1,494,588.82 USD | `-38.88%` | `10X Cross` |
| `596` | `0x27c9...d65d` | `SHORT` | 3,816,678.57 USD | `2,961.88` | `1254.41` | `1288.50` | `1727.90` | -101,263.36 USD | `-2.65%` | `10X Cross` |
| `615` | `0x5323...b23c` | `SHORT` | 3,666,116.49 USD | `2,841.29` | `1265.89` | `1288.50` | `3162.96` | -69,343.76 USD | `-1.89%` | `5X Cross` |
| `673` | `0x71d0...8c26` | `SHORT` | 3,342,513.69 USD | `2,589.49` | `1265.67` | `1288.50` | `3599.24` | -65,081.06 USD | `-1.95%` | `10X Cross` |
| `684` | `0xa183...0482` | `LONG` | 3,270,887.20 USD | `2,534.00` | `530.25` | `1288.50` | `444.59` | 1,927,224.48 USD | `+58.92%` | `5X Isolated` |
| `687` | `0xac48...3201` | `LONG` | 3,262,090.90 USD | `2,531.50` | `1378.58` | `1288.50` | `536.10` | -227,781.38 USD | `-6.98%` | `10X Cross` |
| `695` | `0x0871...e927` | `LONG` | 3,223,500.00 USD | `2,500.00` | `1276.50` | `1288.50` | `0.000000` | 32,250.00 USD | `+1.00%` | `10X Cross` |
| `709` | `0x9b86...6e6e` | `LONG` | 3,172,976.73 USD | `2,463.30` | `637.58` | `1288.50` | `882.52` | 1,602,427.45 USD | `+50.50%` | `3X Cross` |
| `731` | `0xb122...e4ba` | `LONG` | 3,099,774.31 USD | `2,404.79` | `1259.16` | `1288.50` | `1002.81` | 71,755.86 USD | `+2.31%` | `10X Cross` |
| `766` | `0xb2f7...af9f` | `SHORT` | 2,979,377.24 USD | `2,313.72` | `746.63` | `1288.50` | `4444.98` | -1,251,888.50 USD | `-42.02%` | `10X Cross` |
| `784` | `0x413c...886c` | `LONG` | 2,898,225.00 USD | `2,250.00` | `1237.51` | `1288.50` | `0.000000` | 113,823.97 USD | `+3.93%` | `10X Cross` |
| `800` | `0xf48f...10fe` | `LONG` | 2,856,749.57 USD | `2,218.49` | `1517.87` | `1288.50` | `967.22` | -510,637.25 USD | `-17.87%` | `3X Cross` |
| `822` | `0x5bc4...3b0c` | `SHORT` | 2,750,359.19 USD | `2,130.74` | `1089.65` | `1288.50` | `3691.18` | -428,601.61 USD | `-15.58%` | `5X Cross` |
| `842` | `0x8de4...b9aa` | `SHORT` | 2,695,672.81 USD | `2,091.29` | `1331.35` | `1288.50` | `1689.97` | 88,566.90 USD | `+3.29%` | `3X Cross` |
| `851` | `0x4fe2...ac59` | `SHORT` | 2,670,253.73 USD | `2,071.57` | `1478.56` | `1288.50` | `1836.14` | 392,692.48 USD | `+14.71%` | `10X Cross` |
| `858` | `0xdf57...93f5` | `LONG` | 2,651,549.54 USD | `2,054.35` | `1227.36` | `1288.50` | `897.30` | 130,127.50 USD | `+4.91%` | `4X Isolated` |
| `867` | `0xbcd4...0dd2` | `LONG` | 2,619,892.35 USD | `2,033.92` | `1228.20` | `1288.50` | `758.00` | 121,841.54 USD | `+4.65%` | `10X Cross` |
| `877` | `0xf29c...9971` | `LONG` | 2,581,800.00 USD | `2,000.00` | `1254.95` | `1288.50` | `0.000000` | 71,902.93 USD | `+2.78%` | `10X Cross` |
| `878` | `0x9a99...d21a` | `LONG` | 2,578,000.00 USD | `2,000.00` | `1278.44` | `1288.50` | `0.000000` | 21,126.33 USD | `+0.82%` | `10X Cross` |
| `899` | `0x77ee...2902` | `SHORT` | 2,509,211.08 USD | `1,946.03` | `759.84` | `1288.50` | `5440.78` | -1,030,533.58 USD | `-41.07%` | `10X Cross` |
| `908` | `0x3e2f...b269` | `SHORT` | 2,485,448.31 USD | `1,925.51` | `1134.87` | `1288.50` | `2977.24` | -300,249.45 USD | `-12.08%` | `10X Cross` |
| `923` | `0x4f12...618b` | `SHORT` | 2,444,304.92 USD | `1,896.28` | `1608.30` | `1288.50` | `2116.86` | 605,479.47 USD | `+24.77%` | `3X Cross` |
| `965` | `0x866d...d6e1` | `LONG` | 2,323,563.27 USD | `1,802.05` | `674.73` | `1288.50` | `177.93` | 1,107,661.96 USD | `+47.67%` | `10X Cross` |
| `983` | `0x2309...a2d9` | `LONG` | 2,256,927.08 USD | `1,750.37` | `1186.09` | `1288.50` | `812.79` | 180,832.97 USD | `+8.01%` | `8X Cross` |
| `987` | `0x3205...40bb` | `SHORT` | 2,248,360.53 USD | `1,741.70` | `1255.41` | `1288.50` | `2079.01` | -61,816.91 USD | `-2.75%` | `10X Cross` |
| `1026` | `0x265e...7f70` | `LONG` | 2,129,092.86 USD | `1,651.74` | `1382.98` | `1288.50` | `0.000000` | -155,229.90 USD | `-7.29%` | `3X Cross` |
| `1028` | `0xfe7c...b7ae` | `SHORT` | 2,117,527.22 USD | `1,642.64` | `1346.92` | `1288.50` | `5706.45` | 94,981.40 USD | `+4.49%` | `10X Cross` |
| `1037` | `0x2edd...8179` | `SHORT` | 2,104,286.93 USD | `1,633.89` | `1261.58` | `1288.50` | `2906.81` | -43,005.01 USD | `-2.04%` | `10X Cross` |
| `1038` | `0x3e47...aaf6` | `LONG` | 2,102,947.06 USD | `1,636.28` | `1278.38` | `1288.50` | `1048.68` | 11,155.27 USD | `+0.53%` | `10X Cross` |
| `1047` | `0x7f75...9edf` | `LONG` | 2,078,087.30 USD | `1,611.67` | `1200.24` | `1288.50` | `983.33` | 143,703.32 USD | `+6.92%` | `10X Cross` |
| `1055` | `0x6646...6de5` | `SHORT` | 2,064,320.00 USD | `1,600.00` | `660.64` | `1288.50` | `4304.37` | -1,007,295.03 USD | `-48.80%` | `10X Cross` |
| `1060` | `0x023a...2355` | `SHORT` | 2,058,537.43 USD | `1,594.90` | `1310.00` | `1288.50` | `4445.08` | 30,774.71 USD | `+1.49%` | `10X Cross` |
| `1087` | `0xab59...59b5` | `LONG` | 2,016,288.69 USD | `1,565.32` | `1342.15` | `1288.50` | `833.98` | -84,606.53 USD | `-4.20%` | `10X Cross` |
| `1149` | `0xcf67...eb24` | `LONG` | 1,928,700.00 USD | `1,500.00` | `887.05` | `1288.50` | `651.43` | 598,128.63 USD | `+31.01%` | `10X Cross` |
| `1158` | `0xb695...a92d` | `LONG` | 1,914,404.70 USD | `1,483.00` | `1249.80` | `1288.50` | `0.000000` | 60,945.85 USD | `+3.18%` | `10X Cross` |
| `1168` | `0x7277...0b98` | `SHORT` | 1,904,724.71 USD | `1,475.73` | `1287.86` | `1288.50` | `2179.62` | -4,192.59 USD | `-0.22%` | `10X Cross` |
| `1185` | `0xfc27...9d9d` | `SHORT` | 1,859,550.21 USD | `1,440.73` | `1297.35` | `1288.50` | `13512.00` | 9,577.69 USD | `+0.52%` | `10X Cross` |
| `1227` | `0x2ab7...c2f8` | `LONG` | 1,807,918.36 USD | `1,400.51` | `813.26` | `1288.50` | `790.78` | 668,936.67 USD | `+37.00%` | `3X Cross` |
| `1242` | `0xe35c...a1d3` | `LONG` | 1,789,099.16 USD | `1,389.16` | `1311.66` | `1288.50` | `690.77` | -33,003.55 USD | `-1.84%` | `2X Isolated` |
| `1252` | `0x11be...8b1d` | `LONG` | 1,772,894.54 USD | `1,375.83` | `1206.55` | `1288.50` | `1134.57` | 112,886.58 USD | `+6.37%` | `10X Isolated` |
| `1318` | `0x039c...0ebd` | `SHORT` | 1,651,824.95 USD | `1,279.79` | `1239.81` | `1288.50` | `3659.50` | -65,123.12 USD | `-3.94%` | `10X Cross` |
| `1333` | `0x38f9...cb04` | `SHORT` | 1,638,283.36 USD | `1,269.20` | `1252.68` | `1288.50` | `1918.75` | -48,387.65 USD | `-2.95%` | `10X Cross` |
| `1341` | `0xe065...0f85` | `SHORT` | 1,627,504.29 USD | `1,262.61` | `1087.02` | `1288.50` | `1587.28` | -255,028.16 USD | `-15.67%` | `10X Cross` |
| `1413` | `0x266b...efcb` | `LONG` | 1,548,480.00 USD | `1,200.00` | `893.76` | `1288.50` | `389.72` | 475,970.30 USD | `+30.74%` | `10X Cross` |
| `1419` | `0x5975...9abd` | `LONG` | 1,546,320.00 USD | `1,200.00` | `1179.54` | `1288.50` | `489.05` | 130,877.21 USD | `+8.46%` | `5X Cross` |
| `1434` | `0x2847...d47b` | `LONG` | 1,529,576.54 USD | `1,186.27` | `1232.07` | `1288.50` | `0.000000` | 68,008.04 USD | `+4.45%` | `5X Cross` |
| `1459` | `0x69cc...14fd` | `SHORT` | 1,496,993.04 USD | `1,161.36` | `675.33` | `1288.50` | `8020.11` | -712,687.51 USD | `-47.61%` | `10X Cross` |
| `1473` | `0x3fc5...c0c1` | `SHORT` | 1,479,879.78 USD | `1,148.44` | `1264.34` | `1288.50` | `2723.66` | -27,866.01 USD | `-1.88%` | `10X Cross` |
| `1512` | `0x5f94...4b96` | `LONG` | 1,436,133.18 USD | `1,115.27` | `538.00` | `1288.50` | `0.000000` | 836,115.54 USD | `+58.22%` | `10X Cross` |
| `1527` | `0x71df...a23d` | `SHORT` | 1,416,122.23 USD | `1,098.28` | `513.50` | `1288.50` | `2556.03` | -852,152.04 USD | `-60.18%` | `2X Cross` |
| `1553` | `0xbfc7...80b4` | `SHORT` | 1,387,502.50 USD | `1,075.00` | `558.03` | `1288.50` | `2740.37` | -787,623.77 USD | `-56.77%` | `10X Cross` |
| `1628` | `0x123d...3bff` | `SHORT` | 1,308,692.36 USD | `1,013.94` | `494.46` | `1288.50` | `4358.36` | -807,341.05 USD | `-61.69%` | `10X Cross` |
| `1649` | `0x668c...ea2e` | `SHORT` | 1,289,400.00 USD | `1,000.00` | `1406.98` | `1288.50` | `4193.26` | 117,581.99 USD | `+9.12%` | `10X Cross` |
| `1650` | `0xe282...df29` | `LONG` | 1,287,900.00 USD | `1,000.00` | `420.99` | `1288.50` | `809.13` | 866,913.14 USD | `+67.31%` | `10X Cross` |
| `1669` | `0x17f0...094f` | `LONG` | 1,269,156.42 USD | `984.30` | `1287.23` | `1288.50` | `536.92` | 2,136.26 USD | `+0.17%` | `5X Cross` |
| `1684` | `0x51f6...2b39` | `SHORT` | 1,255,605.87 USD | `972.81` | `1299.77` | `1288.50` | `2529.76` | 8,821.84 USD | `+0.70%` | `10X Cross` |
| `1742` | `0x757d...94ba` | `LONG` | 1,193,990.00 USD | `925.00` | `1558.31` | `1288.50` | `0.000000` | -247,450.58 USD | `-20.72%` | `10X Cross` |
| `1746` | `0xaa82...9556` | `LONG` | 1,192,774.59 USD | `924.13` | `1254.72` | `1288.50` | `181.48` | 33,247.91 USD | `+2.79%` | `10X Cross` |
| `1796` | `0xb911...5525` | `LONG` | 1,159,740.00 USD | `900.00` | `1294.82` | `1288.50` | `1035.36` | -5,597.82 USD | `-0.48%` | `10X Cross` |
| `1800` | `0xdf83...3cff` | `SHORT` | 1,157,695.87 USD | `897.23` | `1258.06` | `1288.50` | `1917.76` | -28,928.47 USD | `-2.50%` | `10X Cross` |
| `1841` | `0xcf0a...856f` | `LONG` | 1,123,260.81 USD | `871.15` | `1292.19` | `1288.50` | `1003.07` | -2,434.04 USD | `-0.22%` | `4X Cross` |
| `1852` | `0x9e7e...0047` | `LONG` | 1,120,762.93 USD | `870.09` | `1284.68` | `1288.50` | `1178.90` | 2,977.51 USD | `+0.27%` | `10X Cross` |
| `1855` | `0xef96...9383` | `SHORT` | 1,119,393.38 USD | `868.42` | `1259.08` | `1288.50` | `5395.79` | -25,981.59 USD | `-2.32%` | `10X Cross` |
| `1873` | `0xdf95...7d72` | `SHORT` | 1,100,974.28 USD | `853.27` | `1074.39` | `1288.50` | `44439.77` | -184,226.84 USD | `-16.73%` | `10X Cross` |
| `1904` | `0x2577...4897` | `SHORT` | 1,072,381.23 USD | `831.11` | `1270.31` | `1288.50` | `5119.63` | -16,613.95 USD | `-1.55%` | `10X Cross` |
| `1913` | `0x601c...4f54` | `SHORT` | 1,063,007.15 USD | `824.42` | `615.11` | `1288.50` | `3081.87` | -555,894.40 USD | `-52.29%` | `5X Cross` |
| `1924` | `0xae55...2236` | `LONG` | 1,055,272.02 USD | `817.47` | `1467.80` | `1288.50` | `0.000000` | -144,609.19 USD | `-13.70%` | `10X Cross` |
| `1962` | `0x0f02...5384` | `LONG` | 1,033,566.75 USD | `800.78` | `1290.36` | `1288.50` | `300.53` | 272.68 USD | `+0.03%` | `3X Cross` |
| `1965` | `0x9b0f...db40` | `LONG` | 1,032,720.00 USD | `800.00` | `1268.86` | `1288.50` | `793.48` | 17,630.24 USD | `+1.71%` | `10X Cross` |
| `1971` | `0x11ee...1d1d` | `SHORT` | 1,031,520.00 USD | `800.00` | `1269.65` | `1288.50` | `1601.59` | -15,796.99 USD | `-1.53%` | `5X Cross` |
| `1981` | `0xabdb...84ac` | `LONG` | 1,023,383.89 USD | `793.69` | `711.79` | `1288.50` | `664.49` | 458,443.52 USD | `+44.80%` | `3X Cross` |
| `1982` | `0x6e8f...4364` | `LONG` | 1,022,141.83 USD | `793.65` | `1260.00` | `1288.50` | `963.27` | 22,142.83 USD | `+2.17%` | `10X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `873.68` | 6,203.13 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 6.20K USD at 873.6800 USD [API] | `2026-08-23 14:08:41` |
| `ANNOUNCEMENT` | `INFO` | `873.59` | 8,727.16 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 8.73K USD at 873.5900 USD [API] | `2026-08-23 14:08:41` |
| `ANNOUNCEMENT` | `INFO` | `1257.50` | 12.58 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 0.01K USD at 1257.5000 USD [API] | `2026-10-29 01:59:34` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`1404.55` (Vol: 3,000,000.00 USD, Dist: `+9.99%`) | Long MP=`1176.48` (Vol: 3,400,000.00 USD, Dist: `--7.87%`)
  * 48H Horizon: Short MP=`1404.55` (Vol: 3,000,000.00 USD, Dist: `+9.99%`) | Long MP=`1176.48` (Vol: 3,400,000.00 USD, Dist: `--7.87%`)
  * 3D Horizon: Short MP=`1404.55` (Vol: 3,000,000.00 USD, Dist: `+9.99%`) | Long MP=`1176.48` (Vol: 3,000,000.00 USD, Dist: `--7.87%`)
  * 7D Horizon: Short MP=`1404.10` (Vol: 3,000,000.00 USD, Dist: `+9.95%`) | Long MP=`1176.74` (Vol: 4,900,000.00 USD, Dist: `--7.85%`)
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
| `5m` | `BALANCED` | 0.00 USD | 1,750.00 USD | 1,750.00 USD | 1,750.00 USD | `1` | `2026-10-30 04:30:00 UTC - 2026-10-30 04:35:00 UTC` |
| `15m` | `BALANCED` | 0.00 USD | 1,750.00 USD | 1,750.00 USD | 1,750.00 USD | `1` | `2026-10-30 04:30:00 UTC - 2026-10-30 04:45:00 UTC` |
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
  * Current Rate: `86.20K` | Last 24h: `134.73K` | Last 3d: `246.48K` | Last 7d: `772.71K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0098%` | **USDT OKX** | `0.0100%` |
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
| `0:00 UTC` | `1228.65` | `1236.25` | `1228.65` | `1253.25` | `1219.35` | 45,146,863.08 USD | 23,450,812.50 USD | 21,696,050.59 USD | 1,754,761.91 USD | `+3.89%` | `18B / 9S` |
| `5:00 UTC` | `1254.75` | `1256.85` | `1254.75` | `1263.45` | `1247.85` | 37,496,922.68 USD | 20,689,312.95 USD | 16,807,609.72 USD | 3,881,703.23 USD | `+10.35%` | `5B / 3S` |
| `0:00 UTC` | `1263.45` | `1263.47` | `1263.45` | `1267.65` | `1258.35` | 21,490,941.27 USD | 11,626,504.00 USD | 9,864,437.27 USD | 1,762,066.74 USD | `+8.20%` | `2B / 3S` |
| `5:00 UTC` | `1257.45` | `1259.53` | `1257.45` | `1270.05` | `1249.95` | 34,915,865.69 USD | 14,880,758.20 USD | 20,035,107.50 USD | -5,154,349.30 USD | `-14.76%` | `1B / 7S` |
| `0:00 UTC` | `1260.15` | `1262.58` | `1260.15` | `1267.95` | `1257.15` | 13,992,732.07 USD | 6,287,729.60 USD | 7,705,002.47 USD | -1,417,272.88 USD | `-10.13%` | `0B / 2S` |
| `5:00 UTC` | `1265.55` | `1265.89` | `1265.55` | `1274.25` | `1259.25` | 13,172,642.30 USD | 7,854,309.17 USD | 5,318,333.13 USD | 2,535,976.04 USD | `+19.25%` | `13B / 1S` |
| `0:00 UTC` | `1282.05` | `1279.57` | `1282.05` | `1285.35` | `1269.15` | 31,465,166.07 USD | 16,761,441.58 USD | 14,703,724.48 USD | 2,057,717.10 USD | `+6.54%` | `8B / 5S` |
| `5:00 UTC` | `1279.95` | `1280.45` | `1279.95` | `1287.45` | `1275.15` | 19,925,691.14 USD | 8,662,599.23 USD | 11,263,091.92 USD | -2,600,492.69 USD | `-13.05%` | `1B / 6S` |
| `0:00 UTC` | `1275.15` | `1271.95` | `1275.15` | `1279.35` | `1264.95` | 23,738,198.29 USD | 11,363,344.84 USD | 12,374,853.45 USD | -1,011,508.62 USD | `-4.26%` | `3B / 3S` |
| `5:00 UTC` | `1279.05` | `1280.73` | `1279.05` | `1287.45` | `1274.25` | 13,587,253.48 USD | 6,520,700.59 USD | 7,066,552.89 USD | -545,852.30 USD | `-4.02%` | `2B / 4S` |

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
| `5m` | 334,580.00 USD | 1,280,000.00 USD | **`ACCUMULATION`** |
| `15m` | 1,080,000.00 USD | 1,540,000.00 USD | **`ACCUMULATION`** |
| `30m` | 796,730.00 USD | -1,470,000.00 USD | **`DISTRIBUTION`** |
| `1h` | -21,870.00 USD | 1,280,000.00 USD | **`ACCUMULATION`** |
| `2h` | -944,600.00 USD | -604,740.00 USD | **`DISTRIBUTION`** |
| `4h` | 10,180,000.00 USD | 43,130,000.00 USD | **`ACCUMULATION`** |
| `6h` | 816,320.00 USD | 6,150,000.00 USD | **`ACCUMULATION`** |
| `8h` | -7,300,000.00 USD | 6,380,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -5,030,000.00 USD | -9,820,000.00 USD | **`DISTRIBUTION`** |
| `24h` | 18,710,000.00 USD | 119,630,000.00 USD | **`ACCUMULATION`** |
| `1w` | 40,100,000.00 USD | 240,720,000.00 USD | **`ACCUMULATION`** |
| `30d` | 62,740,000.00 USD | -518,560,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+334.58K` | 15m=`+1.08M` | 1h=`-21.87K` | 24h=`+18.71M`
* Futures Capital Netflows: 5m=`+1.28M` | 15m=`+1.54M` | 1h=`+1.28M` | 24h=`+119.63M`
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
  * `2026-10-30 09:50:37 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 09:09:37 IST`: [forex.com] - (Sentiment: `Neutral`)
  * `2026-10-30 09:56:37 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 09:56:37 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 09:56:37 IST`: [financemagnates.com] - (Sentiment: `Neutral`)
  * `2026-10-30 09:55:37 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-30 06:57:37 IST`: [kathleenhays.substack.com] - (Sentiment: `Neutral`)
  * `2026-10-30 06:57:37 IST`: [rba.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 06:57:37 IST`: [abs.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 05:57:37 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 05:57:37 IST`: [@NodeWire] - (Sentiment: `Neutral`)
  * `2026-10-30 05:57:37 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 05:57:37 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 05:57:37 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-30 05:57:37 IST`: [media.rabobank.com] - (Sentiment: `Neutral`)


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
  * Spread-Padded Stop Loss: `1216.89` (Risk Distance: `5.28` pts)
  * +2.5R Take Profit: `1235.37`
  * Mathematical Lot Sizing: **`1.89 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `1269.33` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `1274.61` (Risk Distance: `5.28` pts)
  * +2.5R Take Profit: `1256.13`
  * Mathematical Lot Sizing: **`1.89 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`1295.95`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
