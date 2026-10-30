# 🏛️ SOVEREIGN CANDIDATE DOSSIER: ZECUSD
**Canonical Key**: `ZECUSD` | **Broker Instrument**: `ZECUSD.p` | **Asset Class**: `Crypto Altcoin`
**Timestamp**: `2026-10-30 10:22:41 IST` (`2026-10-30 04:52:41 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `1282.54` | **Live Ask Quote**: `1284.08` | **Mid Price**: `1283.31`
- **Spread Points**: `154.00` | **Spread BPS**: `12.00 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `1245.35` | VWAP Z-Score: `+1.59` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `18.53` (Volatility Regime: `HIGH_EXPANSION`)
  * 14-Period RSI: `59.10` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `1317.99` | Lower -3.00σ Band: `1172.71`
  * Upper +2.51σ Band: `1306.13` | Lower -2.51σ Band: `1184.58`
  * Upper +2.01σ Band: `1294.02` | Lower -2.01σ Band: `1196.68`
  * Upper +2.00σ Band: `1293.78` | Lower -2.00σ Band: `1196.93`
  * Upper +1.28σ Band: `1276.34` | Lower -1.28σ Band: `1214.36`
  * Upper +1.00σ Band: `1269.56` | Lower -1.00σ Band: `1221.14`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`1270.35` | EMA-20=`1261.51` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`1266.75` (Slope: `+0.0000`) | EMA-100=`1272.52`
  * Institutional Anchors: EMA-144=`1273.92` | EMA-200=`1275.12` (Slope: `-0.1049`) | EMA-233=`1277.61`
- **Range Boundaries**: 24H High=`1396.49` | 24H Low=`1180.03` | Weekly High=`1396.49` | Weekly Low=`1180.03`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `1270.10` (Distance: `+1.06%`)
  * Point of Control (POC) = `1229.90` (Distance: `+4.36%`)
  * Value Area Low (VAL) = `1221.39` (Distance: `+5.09%`)
  * Auction Positioning: `ABOVE_VALUE (Imbalance)` | Session Bias: **`BULLISH (Above Pivot)`** | Market Regime: `RANGE_EXPANSION`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`1309.91` | POC=`1246.71` | VAL=`1230.27`
  * Prior Day Extremes: PDH=`1396.49` | PDL=`1206.89` | PDC=`1244.38`
  * Monday Range Blueprint: High=`1267.53` | Mid=`1222.14` | Low=`1176.75`
  * Developing Weekly Value Area: Weekly VAH=`1296.14` | Weekly POC=`1239.01` | Weekly VAL=`1200.92`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`1296.00` | Low=`1180.03`
  * London Session (08:00-16:00 UTC): High=`1288.44` | Low=`1278.18`
  * New York Session (13:00-21:00 UTC): High=`1291.01` | Low=`1275.61`
  * Initial Balance (First Hour): IB High=`1287.16` | IB Low=`1279.46`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `1278.18` - `1288.44`
  * Optimal Trade Entry (OTE 0.705): `1285.88`
  * Structural Invalidation Anchor (0.786): `1293.58`

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
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 10:14:44 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `13` | `0xb83d...6e36` | `SHORT` | 67,336,283.14 USD | `52,385.47` | `1336.45` | `1285.90` | `3699.07` | 2,674,284.26 USD | `+3.97%` | `3X Cross` |
| `22` | `0x5b5d...c060` | `SHORT` | 51,527,888.33 USD | `40,121.38` | `1478.36` | `1285.90` | `5122.15` | 7,786,146.78 USD | `+15.11%` | `3X Cross` |
| `39` | `0x7fda...17d1` | `SHORT` | 33,166,855.04 USD | `25,814.80` | `1262.44` | `1285.90` | `2635.48` | -577,295.59 USD | `-1.74%` | `5X Cross` |
| `79` | `0x60b0...991e` | `LONG` | 21,570,355.77 USD | `16,779.74` | `1179.65` | `1285.90` | `924.68` | 1,776,108.76 USD | `+8.23%` | `10X Cross` |
| `138` | `0xc36a...105b` | `LONG` | 14,782,195.04 USD | `11,510.82` | `1215.14` | `1285.90` | `963.07` | 794,914.02 USD | `+5.38%` | `10X Cross` |
| `153` | `0x9071...5c0b` | `LONG` | 13,515,769.38 USD | `10,517.29` | `1353.83` | `1285.90` | `0.1437` | -722,849.49 USD | `-5.35%` | `1X Cross` |
| `172` | `0x8742...8427` | `LONG` | 11,827,235.33 USD | `9,201.21` | `1286.37` | `1285.90` | `702.44` | -8,934.66 USD | `-0.08%` | `10X Cross` |
| `189` | `0x58b2...11f3` | `LONG` | 11,007,839.34 USD | `8,563.08` | `1246.56` | `1285.90` | `381.29` | 333,421.77 USD | `+3.03%` | `10X Cross` |
| `194` | `0xad59...ba81` | `SHORT` | 10,829,495.00 USD | `8,425.00` | `330.91` | `1285.90` | `2145.20` | -8,041,537.23 USD | `-74.26%` | `10X Cross` |
| `197` | `0x9ffd...ce40` | `LONG` | 10,724,251.76 USD | `8,350.27` | `1251.39` | `1285.90` | `591.90` | 274,834.39 USD | `+2.56%` | `5X Cross` |
| `203` | `0xdd53...2b13` | `SHORT` | 10,523,561.28 USD | `8,195.92` | `741.54` | `1285.90` | `8505.89` | -4,445,964.92 USD | `-42.25%` | `3X Cross` |
| `220` | `0x880a...311c` | `SHORT` | 9,902,094.93 USD | `7,707.11` | `1367.50` | `1285.90` | `2253.14` | 637,389.27 USD | `+6.44%` | `10X Cross` |
| `234` | `0xbf73...5d58` | `LONG` | 9,630,000.00 USD | `7,500.00` | `1248.78` | `1285.90` | `128.72` | 264,154.38 USD | `+2.74%` | `10X Cross` |
| `265` | `0x2b61...2f6c` | `LONG` | 8,746,995.00 USD | `6,807.00` | `1453.56` | `1285.90` | `572.35` | -1,147,356.22 USD | `-13.12%` | `10X Cross` |
| `285` | `0x2ae5...83e7` | `LONG` | 8,271,931.68 USD | `6,436.80` | `1391.82` | `1285.90` | `0.000000` | -686,960.31 USD | `-8.30%` | `1X Cross` |
| `331` | `0x26b6...9a13` | `LONG` | 6,983,973.17 USD | `5,433.73` | `1282.23` | `1285.90` | `223.00` | 16,669.93 USD | `+0.24%` | `10X Cross` |
| `341` | `0x45d2...4029` | `SHORT` | 6,718,263.10 USD | `5,227.00` | `833.44` | `1285.90` | `8964.71` | -2,361,885.13 USD | `-35.16%` | `5X Cross` |
| `347` | `0xecb6...2b00` | `SHORT` | 6,657,396.77 USD | `5,181.66` | `1279.13` | `1285.90` | `6363.50` | -29,384.44 USD | `-0.44%` | `5X Cross` |
| `361` | `0xea00...a918` | `LONG` | 6,427,500.00 USD | `5,000.00` | `739.16` | `1285.90` | `0.000000` | 2,731,684.89 USD | `+42.50%` | `5X Cross` |
| `375` | `0xdd7a...8830` | `LONG` | 6,247,288.23 USD | `4,860.19` | `897.48` | `1285.90` | `786.56` | 1,885,384.55 USD | `+30.18%` | `10X Cross` |
| `417` | `0x469e...58a5` | `SHORT` | 5,345,959.68 USD | `4,163.52` | `1242.31` | `1285.90` | `1965.58` | -173,575.02 USD | `-3.25%` | `10X Cross` |
| `427` | `0x4cae...7c34` | `LONG` | 5,142,916.95 USD | `4,002.27` | `1169.72` | `1285.90` | `975.22` | 461,367.60 USD | `+8.97%` | `10X Cross` |
| `440` | `0xa61c...66b9` | `LONG` | 4,999,579.20 USD | `3,888.00` | `1148.34` | `1285.90` | `0.000000` | 534,837.06 USD | `+10.70%` | `10X Cross` |
| `461` | `0x9aa5...58af` | `SHORT` | 4,779,854.29 USD | `3,720.31` | `1205.51` | `1285.90` | `3676.94` | -294,967.49 USD | `-6.17%` | `10X Cross` |
| `466` | `0x0153...8052` | `SHORT` | 4,754,010.39 USD | `3,698.18` | `1307.82` | `1285.90` | `2504.85` | 82,560.36 USD | `+1.74%` | `1X Isolated` |
| `479` | `0xd4c1...3d1d` | `SHORT` | 4,663,226.45 USD | `3,628.97` | `1293.30` | `1285.90` | `2429.67` | 30,116.76 USD | `+0.65%` | `10X Cross` |
| `528` | `0x382b...3e39` | `LONG` | 4,213,899.89 USD | `3,279.81` | `1215.08` | `1285.90` | `0.000000` | 228,669.51 USD | `+5.43%` | `10X Cross` |
| `533` | `0xd21d...90f1` | `LONG` | 4,175,600.00 USD | `3,250.00` | `1253.64` | `1285.90` | `876.06` | 101,258.27 USD | `+2.42%` | `4X Isolated` |
| `550` | `0x456f...cdf1` | `LONG` | 4,067,129.17 USD | `3,163.85` | `1267.75` | `1285.90` | `499.97` | 56,168.31 USD | `+1.38%` | `10X Cross` |
| `553` | `0x1338...c48e` | `LONG` | 4,046,702.61 USD | `3,149.43` | `1018.52` | `1285.90` | `820.35` | 838,957.06 USD | `+20.73%` | `4X Isolated` |
| `561` | `0x325e...9564` | `LONG` | 3,988,746.07 USD | `3,101.91` | `1298.07` | `1285.90` | `157.42` | -37,764.63 USD | `-0.95%` | `10X Cross` |
| `566` | `0xdbe0...d6d5` | `LONG` | 3,965,133.94 USD | `3,085.37` | `422.97` | `1285.90` | `338.67` | 2,660,129.45 USD | `+67.09%` | `3X Isolated` |
| `589` | `0x2e30...4cb5` | `SHORT` | 3,859,190.40 USD | `3,005.60` | `1287.36` | `1285.90` | `2869.22` | 10,089.94 USD | `+0.26%` | `2X Cross` |
| `593` | `0x9c06...0560` | `SHORT` | 3,838,903.20 USD | `2,989.80` | `786.00` | `1285.90` | `2584.77` | -1,488,908.20 USD | `-38.78%` | `10X Cross` |
| `597` | `0x27c9...d65d` | `SHORT` | 3,807,496.74 USD | `2,961.88` | `1254.41` | `1285.90` | `1733.04` | -92,081.54 USD | `-2.42%` | `10X Cross` |
| `625` | `0x5323...b23c` | `SHORT` | 3,629,482.80 USD | `2,826.70` | `1265.89` | `1285.90` | `3183.38` | -51,179.47 USD | `-1.41%` | `5X Cross` |
| `681` | `0x71d0...8c26` | `SHORT` | 3,325,423.06 USD | `2,589.49` | `1265.67` | `1285.90` | `3597.84` | -47,990.43 USD | `-1.44%` | `10X Cross` |
| `692` | `0xa183...0482` | `LONG` | 3,256,443.40 USD | `2,534.00` | `530.25` | `1285.90` | `444.59` | 1,912,780.68 USD | `+58.74%` | `5X Isolated` |
| `694` | `0xac48...3201` | `LONG` | 3,254,243.25 USD | `2,531.50` | `1378.58` | `1285.90` | `539.20` | -235,629.03 USD | `-7.24%` | `10X Cross` |
| `706` | `0x0871...e927` | `LONG` | 3,212,500.00 USD | `2,500.00` | `1276.50` | `1285.90` | `0.000000` | 21,250.00 USD | `+0.66%` | `10X Cross` |
| `716` | `0x9b86...6e6e` | `LONG` | 3,164,847.84 USD | `2,463.30` | `637.58` | `1285.90` | `882.52` | 1,594,298.56 USD | `+50.38%` | `3X Cross` |
| `744` | `0xb122...e4ba` | `LONG` | 3,091,357.54 USD | `2,404.79` | `1259.16` | `1285.90` | `989.54` | 63,339.09 USD | `+2.05%` | `10X Cross` |
| `773` | `0xb2f7...af9f` | `SHORT` | 2,974,055.69 USD | `2,313.72` | `746.63` | `1285.90` | `4452.84` | -1,246,566.94 USD | `-41.91%` | `10X Cross` |
| `791` | `0x413c...886c` | `LONG` | 2,892,375.00 USD | `2,250.00` | `1237.51` | `1285.90` | `0.000000` | 107,973.97 USD | `+3.73%` | `10X Cross` |
| `805` | `0xf48f...10fe` | `LONG` | 2,851,647.05 USD | `2,218.49` | `1517.87` | `1285.90` | `969.60` | -515,739.78 USD | `-18.09%` | `3X Cross` |
| `834` | `0x5bc4...3b0c` | `SHORT` | 2,739,705.49 USD | `2,130.74` | `1089.65` | `1285.90` | `3693.64` | -417,947.91 USD | `-15.26%` | `5X Cross` |
| `852` | `0x8de4...b9aa` | `SHORT` | 2,685,843.75 USD | `2,091.29` | `1331.35` | `1285.90` | `1689.97` | 98,395.96 USD | `+3.66%` | `3X Cross` |
| `861` | `0x4fe2...ac59` | `SHORT` | 2,663,003.23 USD | `2,071.57` | `1478.56` | `1285.90` | `1839.28` | 399,942.98 USD | `+15.02%` | `10X Cross` |
| `866` | `0xdf57...93f5` | `LONG` | 2,641,894.10 USD | `2,054.35` | `1227.36` | `1285.90` | `897.30` | 120,472.06 USD | `+4.56%` | `4X Isolated` |
| `872` | `0xbcd4...0dd2` | `LONG` | 2,614,400.77 USD | `2,033.92` | `1228.20` | `1285.90` | `759.58` | 116,349.95 USD | `+4.45%` | `10X Cross` |
| `883` | `0x9a99...d21a` | `LONG` | 2,571,000.00 USD | `2,000.00` | `1278.44` | `1285.90` | `0.000000` | 14,126.33 USD | `+0.55%` | `10X Cross` |
| `884` | `0xf29c...9971` | `LONG` | 2,570,800.00 USD | `2,000.00` | `1254.95` | `1285.90` | `0.000000` | 60,902.93 USD | `+2.37%` | `10X Cross` |
| `908` | `0x77ee...2902` | `SHORT` | 2,500,648.55 USD | `1,946.03` | `759.84` | `1285.90` | `5455.70` | -1,021,971.04 USD | `-40.87%` | `10X Cross` |
| `913` | `0x3e2f...b269` | `SHORT` | 2,476,205.86 USD | `1,925.51` | `1134.87` | `1285.90` | `2977.24` | -291,007.00 USD | `-11.75%` | `10X Cross` |
| `927` | `0x4f12...618b` | `SHORT` | 2,437,667.94 USD | `1,896.28` | `1608.30` | `1285.90` | `2116.86` | 612,116.45 USD | `+25.11%` | `3X Cross` |
| `967` | `0x866d...d6e1` | `LONG` | 2,315,634.25 USD | `1,802.05` | `674.73` | `1285.90` | `169.78` | 1,099,732.94 USD | `+47.49%` | `10X Cross` |
| `988` | `0x2309...a2d9` | `LONG` | 2,247,475.08 USD | `1,750.37` | `1186.09` | `1285.90` | `812.72` | 171,380.97 USD | `+7.63%` | `8X Cross` |
| `997` | `0x3205...40bb` | `SHORT` | 2,238,084.50 USD | `1,741.70` | `1255.41` | `1285.90` | `2077.81` | -51,540.88 USD | `-2.30%` | `10X Cross` |
| `1028` | `0x265e...7f70` | `LONG` | 2,121,329.68 USD | `1,651.74` | `1382.98` | `1285.90` | `0.000000` | -162,993.08 USD | `-7.68%` | `3X Cross` |
| `1034` | `0xfe7c...b7ae` | `SHORT` | 2,111,613.72 USD | `1,642.64` | `1346.92` | `1285.90` | `5697.43` | 100,894.90 USD | `+4.78%` | `10X Cross` |
| `1036` | `0x3e47...aaf6` | `LONG` | 2,102,292.54 USD | `1,636.28` | `1278.38` | `1285.90` | `1049.07` | 10,500.76 USD | `+0.50%` | `10X Cross` |
| `1037` | `0x2edd...8179` | `SHORT` | 2,101,019.15 USD | `1,633.89` | `1261.58` | `1285.90` | `2898.61` | -39,737.23 USD | `-1.89%` | `10X Cross` |
| `1052` | `0x7f75...9edf` | `LONG` | 2,069,384.28 USD | `1,611.67` | `1200.24` | `1285.90` | `983.20` | 135,000.30 USD | `+6.52%` | `10X Cross` |
| `1060` | `0x6646...6de5` | `SHORT` | 2,056,800.00 USD | `1,600.00` | `660.64` | `1285.90` | `4305.16` | -999,775.03 USD | `-48.61%` | `10X Cross` |
| `1067` | `0x023a...2355` | `SHORT` | 2,047,851.60 USD | `1,594.90` | `1310.00` | `1285.90` | `4452.49` | 41,460.54 USD | `+2.02%` | `10X Cross` |
| `1093` | `0xab59...59b5` | `LONG` | 2,012,218.86 USD | `1,565.32` | `1342.15` | `1285.90` | `834.27` | -88,676.36 USD | `-4.41%` | `10X Cross` |
| `1153` | `0xcf67...eb24` | `LONG` | 1,928,250.00 USD | `1,500.00` | `887.05` | `1285.90` | `644.02` | 597,678.63 USD | `+31.00%` | `10X Cross` |
| `1166` | `0xfc27...9d9d` | `SHORT` | 1,908,146.42 USD | `1,485.17` | `1297.09` | `1285.90` | `13192.45` | 18,245.61 USD | `+0.96%` | `10X Cross` |
| `1172` | `0xb695...a92d` | `LONG` | 1,904,913.50 USD | `1,483.00` | `1249.80` | `1285.90` | `0.000000` | 51,454.64 USD | `+2.70%` | `10X Cross` |
| `1174` | `0x7277...0b98` | `SHORT` | 1,897,788.78 USD | `1,475.73` | `1287.86` | `1285.90` | `2180.88` | 2,743.34 USD | `+0.14%` | `10X Cross` |
| `1234` | `0x2ab7...c2f8` | `LONG` | 1,800,075.50 USD | `1,400.51` | `813.26` | `1285.90` | `791.52` | 661,093.82 USD | `+36.73%` | `3X Cross` |
| `1245` | `0xe35c...a1d3` | `LONG` | 1,786,320.84 USD | `1,389.16` | `1311.66` | `1285.90` | `690.77` | -35,781.87 USD | `-2.00%` | `2X Isolated` |
| `1257` | `0x11be...8b1d` | `LONG` | 1,768,629.47 USD | `1,375.83` | `1206.55` | `1285.90` | `1134.57` | 108,621.51 USD | `+6.14%` | `10X Isolated` |
| `1326` | `0x039c...0ebd` | `SHORT` | 1,645,042.07 USD | `1,279.79` | `1239.81` | `1285.90` | `3637.32` | -58,340.24 USD | `-3.55%` | `10X Cross` |
| `1341` | `0x38f9...cb04` | `SHORT` | 1,630,668.16 USD | `1,269.20` | `1252.68` | `1285.90` | `1915.15` | -40,772.45 USD | `-2.50%` | `10X Cross` |
| `1344` | `0xe065...0f85` | `SHORT` | 1,623,085.16 USD | `1,262.61` | `1087.02` | `1285.90` | `1585.83` | -250,609.03 USD | `-15.44%` | `10X Cross` |
| `1425` | `0x266b...efcb` | `LONG` | 1,542,600.00 USD | `1,200.00` | `893.76` | `1285.90` | `393.49` | 470,090.30 USD | `+30.47%` | `10X Cross` |
| `1426` | `0x5975...9abd` | `LONG` | 1,542,600.00 USD | `1,200.00` | `1179.54` | `1285.90` | `489.81` | 127,157.21 USD | `+8.24%` | `5X Cross` |
| `1440` | `0x2847...d47b` | `LONG` | 1,523,407.93 USD | `1,186.27` | `1232.07` | `1285.90` | `0.000000` | 61,839.44 USD | `+4.06%` | `5X Cross` |
| `1465` | `0x69cc...14fd` | `SHORT` | 1,493,392.82 USD | `1,161.36` | `675.33` | `1285.90` | `8038.65` | -709,087.30 USD | `-47.48%` | `10X Cross` |
| `1474` | `0x3fc5...c0c1` | `SHORT` | 1,476,319.62 USD | `1,148.44` | `1264.34` | `1285.90` | `2725.44` | -24,305.84 USD | `-1.65%` | `10X Cross` |
| `1519` | `0x5f94...4b96` | `LONG` | 1,433,568.06 USD | `1,115.27` | `538.00` | `1285.90` | `0.000000` | 833,550.42 USD | `+58.15%` | `10X Cross` |
| `1530` | `0x71df...a23d` | `SHORT` | 1,411,289.80 USD | `1,098.28` | `513.50` | `1285.90` | `2556.82` | -847,319.61 USD | `-60.04%` | `2X Cross` |
| `1569` | `0xbfc7...80b4` | `SHORT` | 1,381,160.00 USD | `1,075.00` | `558.03` | `1285.90` | `2733.04` | -781,281.27 USD | `-56.57%` | `10X Cross` |
| `1631` | `0x123d...3bff` | `SHORT` | 1,302,710.11 USD | `1,013.94` | `494.46` | `1285.90` | `4334.46` | -801,358.81 USD | `-61.51%` | `10X Cross` |
| `1647` | `0xe282...df29` | `LONG` | 1,285,400.00 USD | `1,000.00` | `420.99` | `1285.90` | `807.33` | 864,413.14 USD | `+67.25%` | `10X Cross` |
| `1648` | `0x668c...ea2e` | `SHORT` | 1,284,000.00 USD | `1,000.00` | `1406.98` | `1285.90` | `4195.54` | 122,981.99 USD | `+9.58%` | `10X Cross` |
| `1674` | `0x17f0...094f` | `LONG` | 1,264,825.50 USD | `984.30` | `1287.23` | `1285.90` | `536.92` | -2,194.66 USD | `-0.17%` | `5X Cross` |
| `1689` | `0x51f6...2b39` | `SHORT` | 1,251,033.66 USD | `972.81` | `1299.77` | `1285.90` | `2523.97` | 13,394.05 USD | `+1.07%` | `10X Cross` |
| `1745` | `0x757d...94ba` | `LONG` | 1,189,365.00 USD | `925.00` | `1558.31` | `1285.90` | `0.000000` | -252,075.58 USD | `-21.19%` | `10X Cross` |
| `1750` | `0xaa82...9556` | `LONG` | 1,188,338.77 USD | `924.13` | `1254.72` | `1285.90` | `181.95` | 28,812.09 USD | `+2.42%` | `10X Cross` |
| `1781` | `0xdf83...3cff` | `SHORT` | 1,171,367.52 USD | `912.28` | `1258.55` | `1285.90` | `1915.70` | -23,220.94 USD | `-1.98%` | `10X Cross` |
| `1800` | `0xb911...5525` | `LONG` | 1,156,950.00 USD | `900.00` | `1294.82` | `1285.90` | `1035.36` | -8,387.82 USD | `-0.72%` | `10X Cross` |
| `1852` | `0xcf0a...856f` | `LONG` | 1,118,556.60 USD | `871.15` | `1292.19` | `1285.90` | `1002.91` | -7,138.25 USD | `-0.64%` | `4X Cross` |
| `1853` | `0x9e7e...0047` | `LONG` | 1,118,500.70 USD | `870.09` | `1284.68` | `1285.90` | `1180.68` | 715.28 USD | `+0.06%` | `10X Cross` |
| `1859` | `0xef96...9383` | `SHORT` | 1,115,224.96 USD | `868.42` | `1259.08` | `1285.90` | `5382.18` | -21,813.17 USD | `-1.96%` | `10X Cross` |
| `1877` | `0xdf95...7d72` | `SHORT` | 1,095,598.68 USD | `853.27` | `1074.39` | `1285.90` | `44485.08` | -178,851.24 USD | `-16.32%` | `10X Cross` |
| `1880` | `0x2577...4897` | `SHORT` | 1,094,097.14 USD | `851.57` | `1270.81` | `1285.90` | `5035.53` | -11,913.27 USD | `-1.09%` | `10X Cross` |
| `1915` | `0x601c...4f54` | `SHORT` | 1,059,297.26 USD | `824.42` | `615.11` | `1285.90` | `3083.12` | -552,184.51 USD | `-52.13%` | `5X Cross` |
| `1930` | `0xae55...2236` | `LONG` | 1,050,694.19 USD | `817.47` | `1467.80` | `1285.90` | `0.000000` | -149,187.03 USD | `-14.20%` | `10X Cross` |
| `1970` | `0x0f02...5384` | `LONG` | 1,029,723.00 USD | `800.78` | `1290.36` | `1285.90` | `302.79` | -3,571.07 USD | `-0.35%` | `3X Cross` |
| `1973` | `0x9b0f...db40` | `LONG` | 1,028,112.40 USD | `800.00` | `1268.86` | `1285.90` | `794.64` | 13,022.64 USD | `+1.27%` | `10X Cross` |
| `1977` | `0x11ee...1d1d` | `SHORT` | 1,027,200.00 USD | `800.00` | `1269.65` | `1285.90` | `1603.55` | -11,476.99 USD | `-1.12%` | `5X Cross` |
| `1984` | `0x6e8f...4364` | `LONG` | 1,020,157.71 USD | `793.65` | `1260.00` | `1285.90` | `959.45` | 20,158.71 USD | `+1.98%` | `10X Cross` |
| `1986` | `0xabdb...84ac` | `LONG` | 1,019,256.70 USD | `793.69` | `711.79` | `1285.90` | `664.49` | 454,316.34 USD | `+44.57%` | `3X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `873.68` | 6,203.13 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 6.20K USD at 873.6800 USD [API] | `2026-08-23 14:08:41` |
| `ANNOUNCEMENT` | `INFO` | `873.59` | 8,727.16 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 8.73K USD at 873.5900 USD [API] | `2026-08-23 14:08:41` |
| `ANNOUNCEMENT` | `INFO` | `1257.50` | 12.58 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 0.01K USD at 1257.5000 USD [API] | `2026-10-29 01:59:34` |
| `ANNOUNCEMENT` | `INFO` | `1256.60` | 992.71 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 0.99K USD at 1256.6000 USD [API] | `2026-10-29 01:59:31` |
| `ANNOUNCEMENT` | `INFO` | `1290.00` | 309.60 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Long: 0.31K USD at 1290.0000 USD [API] | `2026-10-27 15:21:38` |


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
| `5m` | `BALANCED` | 0.00 USD | 1,750.00 USD | 1,750.00 USD | 1,750.00 USD | `1` | `2026-10-30 04:40:00 UTC - 2026-10-30 04:45:00 UTC` |
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
  * Current Rate: `86.35K` | Last 24h: `134.73K` | Last 3d: `246.48K` | Last 7d: `772.71K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0098%` | **USDT OKX** | `0.0100%` |
| **USDT Bybit** | `0.0100%` | **USDT KuCoin** | `0.0100%` |
| **USDT MEXC** | `0.0098%` | **USDT BingX** | `0.0100%` |
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
| `0:00 UTC` | `1263.45` | `1263.47` | `1263.45` | `1267.65` | `1258.35` | 21,490,941.27 USD | 11,626,504.00 USD | 9,864,437.27 USD | 1,762,066.74 USD | `+8.20%` | `2B / 3S` |
| `5:00 UTC` | `1257.45` | `1259.53` | `1257.45` | `1270.05` | `1249.95` | 34,915,865.69 USD | 14,880,758.20 USD | 20,035,107.50 USD | -5,154,349.30 USD | `-14.76%` | `1B / 7S` |
| `0:00 UTC` | `1260.15` | `1262.58` | `1260.15` | `1267.95` | `1257.15` | 13,992,732.07 USD | 6,287,729.60 USD | 7,705,002.47 USD | -1,417,272.88 USD | `-10.13%` | `0B / 2S` |
| `5:00 UTC` | `1265.55` | `1265.89` | `1265.55` | `1274.25` | `1259.25` | 13,172,642.30 USD | 7,854,309.17 USD | 5,318,333.13 USD | 2,535,976.04 USD | `+19.25%` | `13B / 1S` |
| `0:00 UTC` | `1282.05` | `1279.57` | `1282.05` | `1285.35` | `1269.15` | 31,465,166.07 USD | 16,761,441.58 USD | 14,703,724.48 USD | 2,057,717.10 USD | `+6.54%` | `8B / 5S` |
| `5:00 UTC` | `1279.95` | `1280.45` | `1279.95` | `1287.45` | `1275.15` | 19,925,691.14 USD | 8,662,599.23 USD | 11,263,091.92 USD | -2,600,492.69 USD | `-13.05%` | `1B / 6S` |
| `0:00 UTC` | `1275.15` | `1271.95` | `1275.15` | `1279.35` | `1264.95` | 23,738,198.29 USD | 11,363,344.84 USD | 12,374,853.45 USD | -1,011,508.62 USD | `-4.26%` | `3B / 3S` |
| `5:00 UTC` | `1279.05` | `1280.95` | `1279.05` | `1287.45` | `1274.25` | 14,930,858.33 USD | 7,292,403.22 USD | 7,638,455.11 USD | -346,051.88 USD | `-2.32%` | `2B / 4S` |
| `0:00 UTC` | `1285.05` | `1286.06` | `1285.05` | `1289.85` | `1282.05` | 15,953,463.93 USD | 6,542,642.51 USD | 9,410,821.42 USD | -2,868,178.91 USD | `-17.98%` | `1B / 3S` |
| `5:00 UTC` | `1279.95` | `1281.97` | `1279.95` | `1286.25` | `1278.15` | 6,689,304.17 USD | 2,644,898.70 USD | 4,044,405.47 USD | -1,399,506.76 USD | `-20.92%` | `0B / 8S` |

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
| `5m` | -190,520.00 USD | -1,100,000.00 USD | **`DISTRIBUTION`** |
| `15m` | 10,260.00 USD | -2,230,000.00 USD | **`DISTRIBUTION`** |
| `30m` | 841,230.00 USD | -534,910.00 USD | **`ACCUMULATION`** |
| `1h` | -2,140,000.00 USD | -6,940,000.00 USD | **`DISTRIBUTION`** |
| `2h` | 1,030,000.00 USD | -9,700,000.00 USD | **`DISTRIBUTION`** |
| `4h` | 5,760,000.00 USD | 22,340,000.00 USD | **`ACCUMULATION`** |
| `6h` | 764,090.00 USD | 10,080,000.00 USD | **`ACCUMULATION`** |
| `8h` | 415,690.00 USD | 3,510,000.00 USD | **`ACCUMULATION`** |
| `12h` | -5,400,000.00 USD | -15,280,000.00 USD | **`DISTRIBUTION`** |
| `24h` | 17,800,000.00 USD | 109,660,000.00 USD | **`ACCUMULATION`** |
| `1w` | 39,610,000.00 USD | 238,540,000.00 USD | **`ACCUMULATION`** |
| `30d` | 62,500,000.00 USD | -520,740,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-190.52K` | 15m=`+10.26K` | 1h=`-2.14M` | 24h=`+17.80M`
* Futures Capital Netflows: 5m=`-1.10M` | 15m=`-2.23M` | 1h=`-6.94M` | 24h=`+109.66M`
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
  * `2026-10-30 09:51:07 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 10:20:07 IST`: [forex.com] - (Sentiment: `Neutral`)
  * `2026-10-30 10:20:07 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 10:20:07 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 10:19:07 IST`: [financemagnates.com] - (Sentiment: `Neutral`)
  * `2026-10-30 07:21:07 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-30 07:21:07 IST`: [kathleenhays.substack.com] - (Sentiment: `Neutral`)
  * `2026-10-30 06:21:07 IST`: [rba.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 06:21:07 IST`: [abs.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 06:21:07 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 06:21:07 IST`: [@NodeWire] - (Sentiment: `Neutral`)
  * `2026-10-30 05:21:07 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 05:21:07 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 05:21:07 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-30 05:21:07 IST`: [media.rabobank.com] - (Sentiment: `Neutral`)


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
  * Execution Entry: `1221.39` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `1196.84` (Risk Distance: `24.55` pts)
  * +2.5R Take Profit: `1282.76`
  * Mathematical Lot Sizing: **`0.40 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `1270.10` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `1294.65` (Risk Distance: `24.55` pts)
  * +2.5R Take Profit: `1208.73`
  * Mathematical Lot Sizing: **`0.40 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`1293.58`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
