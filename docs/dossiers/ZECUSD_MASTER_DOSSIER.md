# 🏛️ SOVEREIGN CANDIDATE DOSSIER: ZECUSD
**Canonical Key**: `ZECUSD` | **Broker Instrument**: `ZECUSD.p` | **Asset Class**: `Crypto Altcoin`
**Timestamp**: `2026-10-30 15:33:14 IST` (`2026-10-30 10:03:14 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `1255.20` | **Live Ask Quote**: `1256.02` | **Mid Price**: `1255.61`
- **Spread Points**: `82.00` | **Spread BPS**: `6.53 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `1253.52` | VWAP Z-Score: `-0.31` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `11.94` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `42.41` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `1317.10` | Lower -3.00σ Band: `1189.95`
  * Upper +2.51σ Band: `1306.71` | Lower -2.51σ Band: `1200.34`
  * Upper +2.01σ Band: `1296.12` | Lower -2.01σ Band: `1210.93`
  * Upper +2.00σ Band: `1295.91` | Lower -2.00σ Band: `1211.14`
  * Upper +1.28σ Band: `1280.65` | Lower -1.28σ Band: `1226.40`
  * Upper +1.00σ Band: `1274.72` | Lower -1.00σ Band: `1232.33`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`1249.63` | EMA-20=`1255.34` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`1261.97` (Slope: `+0.0000`) | EMA-100=`1268.22`
  * Institutional Anchors: EMA-144=`1271.46` | EMA-200=`1275.82` (Slope: `-0.2396`) | EMA-233=`1276.27`
- **Range Boundaries**: 24H High=`1396.49` | 24H Low=`1180.03` | Weekly High=`1396.49` | Weekly Low=`1180.03`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `1279.38` (Distance: `-1.86%`)
  * Point of Control (POC) = `1247.68` (Distance: `+0.64%`)
  * Value Area Low (VAL) = `1237.63` (Distance: `+1.45%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`1309.91` | POC=`1246.71` | VAL=`1230.27`
  * Prior Day Extremes: PDH=`1396.49` | PDL=`1206.89` | PDC=`1244.38`
  * Monday Range Blueprint: High=`1267.53` | Mid=`1222.14` | Low=`1176.75`
  * Developing Weekly Value Area: Weekly VAH=`1293.21` | Weekly POC=`1240.47` | Weekly VAL=`1200.92`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`1296.00` | Low=`1180.03`
  * London Session (08:00-16:00 UTC): High=`1283.82` | Low=`1239.95`
  * New York Session (13:00-21:00 UTC): High=`1263.14` | Low=`1248.08`
  * Initial Balance (First Hour): IB High=`1283.82` | IB Low=`1264.92`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `1250.59` - `1260.63`
  * Optimal Trade Entry (OTE 0.705): `1258.12`
  * Structural Invalidation Anchor (0.786): `1265.65`

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
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 15:30:10 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `12` | `0xb83d...6e36` | `SHORT` | 65,675,663.74 USD | `52,385.47` | `1336.45` | `1252.00` | `3381.30` | 4,334,903.66 USD | `+6.60%` | `3X Cross` |
| `21` | `0x5b5d...c060` | `SHORT` | 50,420,538.25 USD | `40,121.38` | `1478.36` | `1252.00` | `4832.80` | 8,893,496.87 USD | `+17.64%` | `3X Cross` |
| `36` | `0x7fda...17d1` | `SHORT` | 33,393,422.59 USD | `26,618.91` | `1262.58` | `1252.00` | `2616.20` | 215,148.55 USD | `+0.64%` | `5X Cross` |
| `82` | `0x60b0...991e` | `LONG` | 21,053,999.54 USD | `16,779.74` | `1179.65` | `1252.00` | `913.97` | 1,259,752.53 USD | `+5.98%` | `10X Cross` |
| `140` | `0xc36a...105b` | `LONG` | 14,424,208.54 USD | `11,510.82` | `1215.14` | `1252.00` | `966.33` | 436,927.51 USD | `+3.03%` | `10X Cross` |
| `178` | `0x8742...8427` | `LONG` | 11,565,000.85 USD | `9,201.21` | `1286.37` | `1252.00` | `713.10` | -271,169.14 USD | `-2.34%` | `10X Cross` |
| `192` | `0x58b2...11f3` | `LONG` | 10,735,533.40 USD | `8,563.08` | `1246.56` | `1252.00` | `385.92` | 61,115.82 USD | `+0.57%` | `10X Cross` |
| `193` | `0x9071...5c0b` | `LONG` | 10,709,510.13 USD | `8,517.29` | `1353.83` | `1252.00` | `172.69` | -821,449.47 USD | `-7.67%` | `2X Cross` |
| `195` | `0x9ffd...ce40` | `LONG` | 10,647,153.79 USD | `8,493.94` | `1252.16` | `1252.00` | `603.40` | 11,348.91 USD | `+0.11%` | `5X Cross` |
| `199` | `0xad59...ba81` | `SHORT` | 10,571,506.34 USD | `8,425.00` | `330.91` | `1252.00` | `2147.64` | -7,783,548.56 USD | `-73.63%` | `10X Cross` |
| `204` | `0xdd53...2b13` | `SHORT` | 10,268,668.17 USD | `8,195.92` | `741.54` | `1252.00` | `8426.64` | -4,191,071.80 USD | `-40.81%` | `3X Cross` |
| `225` | `0x880a...311c` | `SHORT` | 9,658,550.25 USD | `7,707.11` | `1367.50` | `1252.00` | `2234.62` | 880,933.95 USD | `+9.12%` | `10X Cross` |
| `235` | `0xbf73...5d58` | `LONG` | 9,398,250.00 USD | `7,500.00` | `1248.78` | `1252.00` | `141.17` | 32,404.38 USD | `+0.34%` | `10X Cross` |
| `268` | `0x2b61...2f6c` | `LONG` | 8,541,423.60 USD | `6,807.00` | `1453.56` | `1252.00` | `558.95` | -1,352,927.62 USD | `-15.84%` | `10X Cross` |
| `289` | `0x2ae5...83e7` | `LONG` | 8,065,310.40 USD | `6,436.80` | `1391.82` | `1252.00` | `0.000000` | -893,581.59 USD | `-11.08%` | `1X Cross` |
| `322` | `0xecb6...2b00` | `SHORT` | 7,185,280.66 USD | `5,731.26` | `1277.80` | `1252.00` | `6447.55` | 138,116.85 USD | `+1.92%` | `5X Cross` |
| `334` | `0x26b6...9a13` | `LONG` | 6,832,288.97 USD | `5,433.73` | `1282.23` | `1252.00` | `229.31` | -135,014.27 USD | `-1.98%` | `10X Cross` |
| `351` | `0x45d2...4029` | `SHORT` | 6,549,431.00 USD | `5,227.00` | `833.44` | `1252.00` | `9121.99` | -2,193,053.03 USD | `-33.48%` | `5X Cross` |
| `366` | `0xea00...a918` | `LONG` | 6,271,000.00 USD | `5,000.00` | `739.16` | `1252.00` | `0.000000` | 2,575,184.89 USD | `+41.06%` | `5X Cross` |
| `377` | `0xdd7a...8830` | `LONG` | 6,098,566.41 USD | `4,860.19` | `897.48` | `1252.00` | `786.58` | 1,736,662.74 USD | `+28.48%` | `10X Cross` |
| `420` | `0x469e...58a5` | `SHORT` | 5,234,793.70 USD | `4,163.52` | `1242.31` | `1252.00` | `1954.20` | -62,409.04 USD | `-1.19%` | `10X Cross` |
| `433` | `0x4cae...7c34` | `LONG` | 5,031,253.62 USD | `4,002.27` | `1169.72` | `1252.00` | `963.77` | 349,704.27 USD | `+6.95%` | `10X Cross` |
| `442` | `0xd4c1...3d1d` | `SHORT` | 4,928,253.07 USD | `3,928.46` | `1291.68` | `1252.00` | `2354.86` | 146,058.32 USD | `+2.96%` | `10X Cross` |
| `443` | `0x382b...3e39` | `LONG` | 4,919,506.26 USD | `3,923.99` | `1220.61` | `1252.00` | `0.000000` | 129,862.21 USD | `+2.64%` | `10X Cross` |
| `449` | `0xa61c...66b9` | `LONG` | 4,878,662.40 USD | `3,888.00` | `1148.34` | `1252.00` | `0.000000` | 413,920.26 USD | `+8.48%` | `10X Cross` |
| `477` | `0x9aa5...58af` | `SHORT` | 4,661,920.46 USD | `3,720.31` | `1205.51` | `1252.00` | `3699.45` | -177,033.66 USD | `-3.80%` | `10X Cross` |
| `479` | `0x0153...8052` | `SHORT` | 4,647,872.62 USD | `3,698.18` | `1307.82` | `1252.00` | `2504.94` | 188,698.12 USD | `+4.06%` | `1X Isolated` |
| `508` | `0xb122...e4ba` | `LONG` | 4,386,031.84 USD | `3,498.47` | `1265.25` | `1252.00` | `1123.40` | -40,419.69 USD | `-0.92%` | `10X Cross` |
| `538` | `0xd21d...90f1` | `LONG` | 4,077,125.00 USD | `3,250.00` | `1253.64` | `1252.00` | `876.17` | 2,783.27 USD | `+0.07%` | `4X Isolated` |
| `545` | `0x456f...cdf1` | `LONG` | 4,059,193.71 USD | `3,235.12` | `1267.53` | `1252.00` | `518.53` | -41,418.85 USD | `-1.02%` | `10X Cross` |
| `560` | `0x1338...c48e` | `LONG` | 3,950,015.11 USD | `3,149.43` | `1018.52` | `1252.00` | `820.45` | 742,269.56 USD | `+18.79%` | `4X Isolated` |
| `580` | `0xdbe0...d6d5` | `LONG` | 3,866,277.15 USD | `3,085.37` | `422.97` | `1252.00` | `338.78` | 2,561,272.65 USD | `+66.25%` | `3X Isolated` |
| `594` | `0x325e...9564` | `LONG` | 3,765,541.87 USD | `3,000.91` | `1298.07` | `1252.00` | `136.81` | -129,863.29 USD | `-3.45%` | `10X Cross` |
| `597` | `0x2e30...4cb5` | `SHORT` | 3,754,151.97 USD | `2,996.37` | `1282.33` | `1252.00` | `2887.19` | 88,178.49 USD | `+2.35%` | `2X Cross` |
| `598` | `0x9c06...0560` | `SHORT` | 3,746,518.38 USD | `2,989.80` | `786.00` | `1252.00` | `2567.61` | -1,396,523.38 USD | `-37.28%` | `10X Cross` |
| `610` | `0x27c9...d65d` | `SHORT` | 3,684,889.77 USD | `2,938.04` | `1254.41` | `1252.00` | `1737.87` | 620.28 USD | `+0.02%` | `10X Cross` |
| `705` | `0xac48...3201` | `LONG` | 3,175,007.30 USD | `2,531.50` | `1378.58` | `1252.00` | `537.91` | -314,864.98 USD | `-9.92%` | `10X Cross` |
| `706` | `0xa183...0482` | `LONG` | 3,174,848.60 USD | `2,534.00` | `530.25` | `1252.00` | `444.70` | 1,831,185.88 USD | `+57.68%` | `5X Isolated` |
| `714` | `0x0871...e927` | `LONG` | 3,137,000.00 USD | `2,500.00` | `1276.50` | `1252.00` | `0.000000` | -54,250.00 USD | `-1.73%` | `10X Cross` |
| `737` | `0x9b86...6e6e` | `LONG` | 3,090,209.85 USD | `2,463.30` | `637.58` | `1252.00` | `882.63` | 1,519,660.57 USD | `+49.18%` | `3X Cross` |
| `812` | `0xf48f...10fe` | `LONG` | 2,783,712.89 USD | `2,218.49` | `1517.87` | `1252.00` | `980.31` | -583,673.94 USD | `-20.97%` | `3X Cross` |
| `835` | `0x71d0...8c26` | `SHORT` | 2,691,681.36 USD | `2,146.99` | `1265.96` | `1252.00` | `3808.93` | 26,321.47 USD | `+0.98%` | `10X Cross` |
| `841` | `0x5bc4...3b0c` | `SHORT` | 2,669,604.15 USD | `2,130.74` | `1089.65` | `1252.00` | `3677.05` | -347,846.57 USD | `-13.03%` | `5X Cross` |
| `856` | `0x8de4...b9aa` | `SHORT` | 2,621,850.27 USD | `2,091.29` | `1331.35` | `1252.00` | `1690.07` | 162,389.43 USD | `+6.19%` | `3X Cross` |
| `863` | `0x4fe2...ac59` | `SHORT` | 2,597,127.31 USD | `2,071.57` | `1478.56` | `1252.00` | `1849.81` | 465,818.91 USD | `+17.94%` | `10X Cross` |
| `868` | `0xdf57...93f5` | `LONG` | 2,573,895.12 USD | `2,054.35` | `1227.36` | `1252.00` | `897.41` | 52,473.07 USD | `+2.04%` | `4X Isolated` |
| `870` | `0xbcd4...0dd2` | `LONG` | 2,550,942.46 USD | `2,033.92` | `1228.20` | `1252.00` | `765.85` | 52,891.65 USD | `+2.07%` | `10X Cross` |
| `881` | `0x9a99...d21a` | `LONG` | 2,510,600.00 USD | `2,000.00` | `1278.44` | `1252.00` | `0.000000` | -46,273.67 USD | `-1.84%` | `10X Cross` |
| `885` | `0xf29c...9971` | `LONG` | 2,505,800.00 USD | `2,000.00` | `1254.95` | `1252.00` | `0.000000` | -4,097.07 USD | `-0.16%` | `10X Cross` |
| `906` | `0x77ee...2902` | `SHORT` | 2,446,354.31 USD | `1,946.03` | `759.84` | `1252.00` | `5762.44` | -967,676.81 USD | `-39.56%` | `10X Cross` |
| `916` | `0x3e2f...b269` | `SHORT` | 2,412,471.48 USD | `1,925.51` | `1134.87` | `1252.00` | `2977.34` | -227,272.62 USD | `-9.42%` | `10X Cross` |
| `930` | `0x4f12...618b` | `SHORT` | 2,380,400.28 USD | `1,896.28` | `1608.30` | `1252.00` | `2116.94` | 669,384.10 USD | `+28.12%` | `3X Cross` |
| `974` | `0x866d...d6e1` | `LONG` | 2,265,357.06 USD | `1,802.05` | `674.73` | `1252.00` | `130.12` | 1,049,455.74 USD | `+46.33%` | `10X Cross` |
| `998` | `0x2309...a2d9` | `LONG` | 2,200,740.20 USD | `1,750.37` | `1186.09` | `1252.00` | `806.55` | 124,646.09 USD | `+5.66%` | `8X Cross` |
| `1038` | `0x265e...7f70` | `LONG` | 2,074,255.09 USD | `1,651.74` | `1382.98` | `1252.00` | `0.000000` | -210,067.67 USD | `-10.13%` | `3X Cross` |
| `1048` | `0xfe7c...b7ae` | `SHORT` | 2,060,199.09 USD | `1,642.64` | `1346.92` | `1252.00` | `5693.07` | 152,309.53 USD | `+7.39%` | `10X Cross` |
| `1050` | `0x3e47...aaf6` | `LONG` | 2,052,713.26 USD | `1,636.28` | `1278.38` | `1252.00` | `1051.51` | -39,078.53 USD | `-1.90%` | `10X Cross` |
| `1051` | `0x2edd...8179` | `SHORT` | 2,052,336.91 USD | `1,635.98` | `1261.55` | `1252.00` | `2869.40` | 11,525.97 USD | `+0.56%` | `10X Cross` |
| `1071` | `0x7f75...9edf` | `LONG` | 2,026,014.04 USD | `1,612.17` | `1200.26` | `1252.00` | `986.35` | 90,992.96 USD | `+4.49%` | `10X Cross` |
| `1083` | `0x6646...6de5` | `SHORT` | 2,004,960.00 USD | `1,600.00` | `660.64` | `1252.00` | `4199.73` | -947,935.03 USD | `-47.28%` | `10X Cross` |
| `1086` | `0x023a...2355` | `SHORT` | 1,996,775.79 USD | `1,591.31` | `1310.00` | `1252.00` | `4415.95` | 87,833.46 USD | `+4.40%` | `10X Cross` |
| `1092` | `0xfc27...9d9d` | `SHORT` | 1,984,643.72 USD | `1,584.04` | `1295.64` | `1252.00` | `12990.04` | 67,708.81 USD | `+3.41%` | `10X Cross` |
| `1104` | `0xab59...59b5` | `LONG` | 1,965,102.73 USD | `1,565.32` | `1342.15` | `1252.00` | `836.05` | -135,792.49 USD | `-6.91%` | `10X Cross` |
| `1154` | `0x039c...0ebd` | `SHORT` | 1,908,127.34 USD | `1,521.39` | `1245.17` | `1252.00` | `3738.51` | -13,733.48 USD | `-0.72%` | `10X Cross` |
| `1167` | `0xcf67...eb24` | `LONG` | 1,882,950.00 USD | `1,500.00` | `887.05` | `1252.00` | `608.77` | 552,378.63 USD | `+29.34%` | `10X Cross` |
| `1182` | `0x7277...0b98` | `SHORT` | 1,849,827.55 USD | `1,475.73` | `1287.86` | `1252.00` | `2200.00` | 50,704.57 USD | `+2.74%` | `10X Cross` |
| `1238` | `0x3205...40bb` | `SHORT` | 1,776,136.10 USD | `1,417.62` | `1257.20` | `1252.00` | `2295.69` | 6,101.87 USD | `+0.34%` | `10X Cross` |
| `1251` | `0x2ab7...c2f8` | `LONG` | 1,754,698.98 USD | `1,400.51` | `813.26` | `1252.00` | `792.91` | 615,717.29 USD | `+35.09%` | `3X Cross` |
| `1266` | `0x11be...8b1d` | `LONG` | 1,725,565.99 USD | `1,375.83` | `1206.55` | `1252.00` | `1134.68` | 65,558.03 USD | `+3.80%` | `10X Isolated` |
| `1351` | `0xe065...0f85` | `SHORT` | 1,582,934.16 USD | `1,262.61` | `1087.02` | `1252.00` | `1543.10` | -210,458.03 USD | `-13.30%` | `10X Cross` |
| `1365` | `0x413c...886c` | `LONG` | 1,568,125.00 USD | `1,250.00` | `1237.51` | `1252.00` | `0.000000` | 21,235.54 USD | `+1.35%` | `10X Cross` |
| `1368` | `0xdf83...3cff` | `SHORT` | 1,565,963.19 USD | `1,248.00` | `1260.55` | `1252.00` | `1871.15` | 7,207.10 USD | `+0.46%` | `10X Cross` |
| `1430` | `0x2847...d47b` | `LONG` | 1,518,393.80 USD | `1,211.71` | `1232.45` | `1252.00` | `0.000000` | 25,026.20 USD | `+1.65%` | `5X Cross` |
| `1443` | `0x5975...9abd` | `LONG` | 1,505,040.00 USD | `1,200.00` | `1179.54` | `1252.00` | `548.75` | 89,597.21 USD | `+5.95%` | `5X Cross` |
| `1444` | `0x266b...efcb` | `LONG` | 1,503,720.00 USD | `1,200.00` | `893.76` | `1252.00` | `420.97` | 431,210.30 USD | `+28.68%` | `10X Cross` |
| `1465` | `0x5323...b23c` | `SHORT` | 1,467,025.20 USD | `1,169.69` | `1254.28` | `1252.00` | `6017.50` | 89.26 USD | `+0.01%` | `5X Cross` |
| `1475` | `0x69cc...14fd` | `SHORT` | 1,455,764.76 USD | `1,161.36` | `675.33` | `1252.00` | `8127.48` | -671,459.23 USD | `-46.12%` | `10X Cross` |
| `1489` | `0x3fc5...c0c1` | `SHORT` | 1,440,373.45 USD | `1,148.44` | `1264.34` | `1252.00` | `2788.07` | 11,640.33 USD | `+0.81%` | `10X Cross` |
| `1531` | `0x5f94...4b96` | `LONG` | 1,399,416.48 USD | `1,115.27` | `538.00` | `1252.00` | `0.000000` | 799,398.85 USD | `+57.12%` | `10X Cross` |
| `1539` | `0xe35c...a1d3` | `LONG` | 1,394,534.53 USD | `1,111.36` | `1311.66` | `1252.00` | `690.98` | -63,189.62 USD | `-4.53%` | `2X Isolated` |
| `1554` | `0x71df...a23d` | `SHORT` | 1,376,364.50 USD | `1,098.28` | `513.50` | `1252.00` | `2560.84` | -812,394.31 USD | `-59.02%` | `2X Cross` |
| `1584` | `0xbfc7...80b4` | `SHORT` | 1,349,340.00 USD | `1,075.00` | `558.03` | `1252.00` | `2663.13` | -749,461.27 USD | `-55.54%` | `10X Cross` |
| `1611` | `0x123d...3bff` | `SHORT` | 1,311,011.49 USD | `1,044.34` | `519.62` | `1252.00` | `4094.56` | -768,353.28 USD | `-58.61%` | `10X Cross` |
| `1673` | `0x926a...af36` | `LONG` | 1,256,908.06 USD | `1,001.68` | `1255.52` | `1252.00` | `1188.67` | -718.30 USD | `-0.06%` | `10X Isolated` |
| `1682` | `0xe282...df29` | `LONG` | 1,254,800.00 USD | `1,000.00` | `420.99` | `1252.00` | `806.01` | 833,813.14 USD | `+66.45%` | `10X Cross` |
| `1683` | `0x668c...ea2e` | `SHORT` | 1,253,100.00 USD | `1,000.00` | `1406.98` | `1252.00` | `4213.07` | 153,881.99 USD | `+12.28%` | `10X Cross` |
| `1705` | `0x17f0...094f` | `LONG` | 1,233,524.76 USD | `984.30` | `1287.23` | `1252.00` | `537.03` | -33,495.40 USD | `-2.72%` | `5X Cross` |
| `1722` | `0x51f6...2b39` | `SHORT` | 1,218,930.93 USD | `972.81` | `1299.77` | `1252.00` | `2507.84` | 45,496.78 USD | `+3.73%` | `10X Cross` |
| `1728` | `0x38f9...cb04` | `SHORT` | 1,212,483.53 USD | `967.51` | `1253.74` | `1252.00` | `2143.39` | 524.66 USD | `+0.04%` | `10X Cross` |
| `1783` | `0x757d...94ba` | `LONG` | 1,158,932.50 USD | `925.00` | `1558.31` | `1252.00` | `0.000000` | -282,508.09 USD | `-24.38%` | `10X Cross` |
| `1830` | `0xb911...5525` | `LONG` | 1,128,780.00 USD | `900.00` | `1294.82` | `1252.00` | `1035.46` | -36,557.82 USD | `-3.24%` | `10X Cross` |
| `1847` | `0xef96...9383` | `SHORT` | 1,112,997.25 USD | `887.77` | `1259.32` | `1252.00` | `5093.58` | 4,989.63 USD | `+0.45%` | `10X Cross` |
| `1873` | `0xcf0a...856f` | `LONG` | 1,091,638.06 USD | `871.15` | `1292.19` | `1252.00` | `1032.75` | -34,056.78 USD | `-3.12%` | `4X Cross` |
| `1894` | `0xdf95...7d72` | `SHORT` | 1,069,232.64 USD | `853.27` | `1074.39` | `1252.00` | `45258.52` | -152,485.20 USD | `-14.26%` | `10X Cross` |
| `1926` | `0xb2f7...af9f` | `SHORT` | 1,042,369.35 USD | `830.72` | `746.63` | `1252.00` | `8194.78` | -422,130.32 USD | `-40.50%` | `10X Cross` |
| `1933` | `0x601c...4f54` | `SHORT` | 1,036,378.38 USD | `824.42` | `615.11` | `1252.00` | `3133.09` | -529,265.63 USD | `-51.07%` | `5X Cross` |
| `1954` | `0xae55...2236` | `LONG` | 1,024,289.91 USD | `817.47` | `1467.80` | `1252.00` | `0.000000` | -175,591.31 USD | `-17.14%` | `10X Cross` |
| `1987` | `0x0f02...5384` | `LONG` | 1,004,498.43 USD | `800.78` | `1290.36` | `1252.00` | `307.97` | -28,795.64 USD | `-2.87%` | `3X Cross` |
| `1992` | `0x9b0f...db40` | `LONG` | 1,002,480.00 USD | `800.00` | `1268.86` | `1252.00` | `799.97` | -12,609.76 USD | `-1.26%` | `10X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
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
  * 24H Horizon: Short MP=`1404.55` (Vol: 3,000,000.00 USD, Dist: `+12.62%`) | Long MP=`1176.48` (Vol: 3,400,000.00 USD, Dist: `--5.67%`)
  * 48H Horizon: Short MP=`1404.55` (Vol: 3,000,000.00 USD, Dist: `+12.62%`) | Long MP=`1176.48` (Vol: 3,400,000.00 USD, Dist: `--5.67%`)
  * 3D Horizon: Short MP=`1404.55` (Vol: 3,000,000.00 USD, Dist: `+12.62%`) | Long MP=`1176.48` (Vol: 3,400,000.00 USD, Dist: `--5.67%`)
  * 7D Horizon: Short MP=`1404.10` (Vol: 3,000,000.00 USD, Dist: `+12.58%`) | Long MP=`1176.74` (Vol: 4,900,000.00 USD, Dist: `--5.65%`)
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
| `5m` | `BALANCED` | 0.00 USD | 1,750.00 USD | 1,750.00 USD | 1,750.00 USD | `1` | `2026-10-30 09:55:00 UTC - 2026-10-30 10:00:00 UTC` |
| `15m` | `BALANCED` | 0.00 USD | 1,750.00 USD | 1,750.00 USD | 1,750.00 USD | `1` | `2026-10-30 09:45:00 UTC - 2026-10-30 10:00:00 UTC` |
| `1h` | `BALANCED` | 0.00 USD | 1,750.00 USD | 1,750.00 USD | 1,750.00 USD | `1` | `2026-10-30 09:00:00 UTC - 2026-10-30 10:00:00 UTC` |
| `4h` | `BALANCED` | 0.00 USD | 1,750.00 USD | 1,750.00 USD | 1,750.00 USD | `1` | `2026-10-30 08:00:00 UTC - 2026-10-30 12:00:00 UTC` |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `0 USD` | Total OI Tokens: `-`
  * 1h OI Change: `0.00%` | 4h OI Change: `0.00%` | 24h OI Change: `0.00%`
  * Exchange Breakdown: Binance=`-` | Bybit=`-` | OKX=`-` | Hyperliquid=`-`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `84.54K` | Last 24h: `171.90K` | Last 3d: `285.15K` | Last 7d: `847.79K`
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
| `0:00 UTC` | `1255.05` | `1256.16` | `1255.05` | `1269.15` | `1247.25` | 26,236,011.28 USD | 8,922,234.21 USD | 17,313,777.08 USD | -8,391,542.87 USD | `-31.98%` | `2B / 24S` |
| `5:00 UTC` | `1248.15` | `1248.05` | `1248.15` | `1253.25` | `1244.25` | 21,008,122.73 USD | 11,395,427.09 USD | 9,612,695.64 USD | 1,782,731.45 USD | `+8.49%` | `1B / 0S` |
| `0:00 UTC` | `1245.75` | `1245.57` | `1245.75` | `1250.55` | `1240.05` | 17,224,192.69 USD | 9,235,789.14 USD | 7,988,403.55 USD | 1,247,385.58 USD | `+7.24%` | `1B / 6S` |
| `5:00 UTC` | `1251.45` | `1250.99` | `1251.45` | `1255.05` | `1246.35` | 13,619,576.55 USD | 6,741,413.50 USD | 6,878,163.05 USD | -136,749.55 USD | `-1.00%` | `2B / 0S` |
| `0:00 UTC` | `1249.95` | `1249.10` | `1249.95` | `1253.55` | `1244.55` | 10,263,783.49 USD | 5,117,369.60 USD | 5,146,413.89 USD | -29,044.29 USD | `-0.28%` | `1B / 4S` |
| `5:00 UTC` | `1246.65` | `1246.77` | `1246.65` | `1252.35` | `1243.95` | 13,017,000.97 USD | 7,727,648.32 USD | 5,289,352.64 USD | 2,438,295.68 USD | `+18.73%` | `8B / 5S` |
| `0:00 UTC` | `1244.55` | `1245.81` | `1244.55` | `1249.05` | `1243.65` | 9,717,386.64 USD | 3,914,194.68 USD | 5,803,191.96 USD | -1,888,997.28 USD | `-19.44%` | `0B / 1S` |
| `5:00 UTC` | `1242.15` | `1244.40` | `1242.15` | `1249.35` | `1241.25` | 8,638,502.97 USD | 4,533,952.89 USD | 4,104,550.08 USD | 429,402.82 USD | `+4.97%` | `4B / 2S` |
| `0:00 UTC` | `1251.15` | `1247.35` | `1251.15` | `1251.75` | `1240.05` | 9,977,652.60 USD | 4,992,881.35 USD | 4,984,771.25 USD | 8,110.10 USD | `+0.08%` | `3B / 5S` |
| `5:00 UTC` | `1243.95` | `1247.47` | `1243.95` | `1252.65` | `1243.35` | 11,017,036.23 USD | 6,254,046.22 USD | 4,762,990.01 USD | 1,491,056.21 USD | `+13.53%` | `6B / 2S` |

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
| `5m` | -136,760.00 USD | 2,090,000.00 USD | **`ACCUMULATION`** |
| `15m` | 517,620.00 USD | 4,240,000.00 USD | **`ACCUMULATION`** |
| `30m` | -264,770.00 USD | 4,710,000.00 USD | **`ACCUMULATION`** |
| `1h` | -2,040,000.00 USD | 4,820,000.00 USD | **`ACCUMULATION`** |
| `2h` | -1,830,000.00 USD | 8,680,000.00 USD | **`ACCUMULATION`** |
| `4h` | 2,050,000.00 USD | -12,280,000.00 USD | **`DISTRIBUTION`** |
| `6h` | -236,930.00 USD | -31,030,000.00 USD | **`DISTRIBUTION`** |
| `8h` | 13,340,000.00 USD | -4,450,000.00 USD | **`ACCUMULATION`** |
| `12h` | 625,350.00 USD | -16,540,000.00 USD | **`DISTRIBUTION`** |
| `24h` | 23,090,000.00 USD | 78,080,000.00 USD | **`ACCUMULATION`** |
| `1w` | 37,630,000.00 USD | 207,850,000.00 USD | **`ACCUMULATION`** |
| `30d` | 64,250,000.00 USD | -537,740,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-136.76K` | 15m=`+517.62K` | 1h=`-2.04M` | 24h=`+23.09M`
* Futures Capital Netflows: 5m=`+2.09M` | 15m=`+4.24M` | 1h=`+4.82M` | 24h=`+78.08M`
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
  * `2026-10-30 15:18:36 IST`: [dailyforex.com] - (Sentiment: `Neutral`)
  * `2026-10-30 15:12:36 IST`: [breakingthenews.net] - (Sentiment: `Neutral`)
  * `2026-10-30 14:41:36 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 14:37:36 IST`: [@FirstSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 14:33:36 IST`: [destatis.de] - (Sentiment: `Neutral`)
  * `2026-10-30 14:32:36 IST`: [istat.it] - (Sentiment: `Neutral`)
  * `2026-10-30 15:25:36 IST`: [channelnewsasia.com] - (Sentiment: `Neutral`)
  * `2026-10-30 15:25:36 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 15:25:36 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 15:25:36 IST`: [kof.ethz.ch] - (Sentiment: `Neutral`)
  * `2026-10-30 15:24:36 IST`: [gerlachmacro.substack.com] - (Sentiment: `Neutral`)
  * `2026-10-30 15:24:36 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-30 15:24:36 IST`: [insee.fr] - (Sentiment: `Neutral`)
  * `2026-10-30 15:24:36 IST`: [insee.fr] - (Sentiment: `Neutral`)
  * `2026-10-30 15:24:36 IST`: [@FirstSquawk] - (Sentiment: `Neutral`)


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
  * Execution Entry: `1237.63` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `1222.07` (Risk Distance: `15.56` pts)
  * +2.5R Take Profit: `1276.53`
  * Mathematical Lot Sizing: **`0.64 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `1279.38` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `1294.94` (Risk Distance: `15.56` pts)
  * +2.5R Take Profit: `1240.48`
  * Mathematical Lot Sizing: **`0.64 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`1265.65`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
