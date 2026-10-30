# 🏛️ SOVEREIGN CANDIDATE DOSSIER: ZECUSD
**Canonical Key**: `ZECUSD` | **Broker Instrument**: `ZECUSD.p` | **Asset Class**: `Crypto Altcoin`
**Timestamp**: `2026-10-30 11:41:29 IST` (`2026-10-30 06:11:29 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `1268.73` | **Live Ask Quote**: `1269.98` | **Mid Price**: `1269.36`
- **Spread Points**: `125.00` | **Spread BPS**: `9.85 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `1251.85` | VWAP Z-Score: `+0.56` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `15.36` (Volatility Regime: `HIGH_EXPANSION`)
  * 14-Period RSI: `49.99` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `1326.55` | Lower -3.00σ Band: `1177.16`
  * Upper +2.51σ Band: `1314.35` | Lower -2.51σ Band: `1189.36`
  * Upper +2.01σ Band: `1301.90` | Lower -2.01σ Band: `1201.81`
  * Upper +2.00σ Band: `1301.65` | Lower -2.00σ Band: `1202.05`
  * Upper +1.28σ Band: `1283.72` | Lower -1.28σ Band: `1219.98`
  * Upper +1.00σ Band: `1276.75` | Lower -1.00σ Band: `1226.95`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`1271.59` | EMA-20=`1266.71` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`1268.20` (Slope: `+0.0000`) | EMA-100=`1272.66`
  * Institutional Anchors: EMA-144=`1274.16` | EMA-200=`1276.06` (Slope: `-0.0105`) | EMA-233=`1278.20`
- **Range Boundaries**: 24H High=`1396.49` | 24H Low=`1180.03` | Weekly High=`1396.49` | Weekly Low=`1180.03`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `1285.56` (Distance: `-1.20%`)
  * Point of Control (POC) = `1275.51` (Distance: `-0.42%`)
  * Value Area Low (VAL) = `1235.31` (Distance: `+2.82%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`1309.91` | POC=`1246.71` | VAL=`1230.27`
  * Prior Day Extremes: PDH=`1396.49` | PDL=`1206.89` | PDC=`1244.38`
  * Monday Range Blueprint: High=`1267.53` | Mid=`1222.14` | Low=`1176.75`
  * Developing Weekly Value Area: Weekly VAH=`1294.68` | Weekly POC=`1239.01` | Weekly VAL=`1200.92`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`1296.00` | Low=`1180.03`
  * London Session (08:00-16:00 UTC): High=`1283.82` | Low=`1263.39`
  * New York Session (13:00-21:00 UTC): High=`1276.97` | Low=`1261.74`
  * Initial Balance (First Hour): IB High=`1283.82` | IB Low=`1264.92`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `1264.28` - `1274.43`
  * Optimal Trade Entry (OTE 0.705): `1271.89`
  * Structural Invalidation Anchor (0.786): `1279.51`

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
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 11:33:47 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `13` | `0xb83d...6e36` | `SHORT` | 66,529,546.90 USD | `52,385.47` | `1336.45` | `1270.07` | `3686.49` | 3,481,020.50 USD | `+5.23%` | `3X Cross` |
| `22` | `0x5b5d...c060` | `SHORT` | 50,998,286.12 USD | `40,121.38` | `1478.36` | `1270.07` | `5104.93` | 8,315,748.99 USD | `+16.31%` | `3X Cross` |
| `38` | `0x7fda...17d1` | `SHORT` | 33,309,284.99 USD | `26,209.21` | `1262.66` | `1270.07` | `2610.71` | -215,928.54 USD | `-0.65%` | `5X Cross` |
| `81` | `0x60b0...991e` | `LONG` | 21,310,269.80 USD | `16,779.74` | `1179.65` | `1270.07` | `923.91` | 1,516,022.79 USD | `+7.11%` | `10X Cross` |
| `139` | `0xc36a...105b` | `LONG` | 14,629,101.14 USD | `11,510.82` | `1215.14` | `1270.07` | `962.10` | 641,820.11 USD | `+4.39%` | `10X Cross` |
| `155` | `0x9071...5c0b` | `LONG` | 13,354,854.84 USD | `10,517.29` | `1353.83` | `1270.07` | `0.1837` | -883,764.03 USD | `-6.62%` | `1X Cross` |
| `179` | `0x8742...8427` | `LONG` | 11,683,696.46 USD | `9,201.21` | `1286.37` | `1270.07` | `697.93` | -152,473.54 USD | `-1.31%` | `10X Cross` |
| `194` | `0x58b2...11f3` | `LONG` | 10,870,830.06 USD | `8,563.08` | `1246.56` | `1270.07` | `382.96` | 196,412.49 USD | `+1.81%` | `10X Cross` |
| `198` | `0x9ffd...ce40` | `LONG` | 10,700,796.34 USD | `8,417.87` | `1251.91` | `1270.07` | `598.56` | 162,375.51 USD | `+1.52%` | `5X Cross` |
| `199` | `0xad59...ba81` | `SHORT` | 10,699,750.00 USD | `8,425.00` | `330.91` | `1270.07` | `2145.12` | -7,911,792.23 USD | `-73.94%` | `10X Cross` |
| `206` | `0xdd53...2b13` | `SHORT` | 10,407,179.22 USD | `8,195.92` | `741.54` | `1270.07` | `8449.70` | -4,329,582.85 USD | `-41.60%` | `3X Cross` |
| `223` | `0x880a...311c` | `SHORT` | 9,792,653.97 USD | `7,707.11` | `1367.50` | `1270.07` | `2268.70` | 746,830.24 USD | `+7.63%` | `10X Cross` |
| `236` | `0xbf73...5d58` | `LONG` | 9,523,500.00 USD | `7,500.00` | `1248.78` | `1270.07` | `119.55` | 157,654.38 USD | `+1.66%` | `10X Cross` |
| `268` | `0x2b61...2f6c` | `LONG` | 8,648,974.20 USD | `6,807.00` | `1453.56` | `1270.07` | `575.71` | -1,245,377.02 USD | `-14.40%` | `10X Cross` |
| `285` | `0x2ae5...83e7` | `LONG` | 8,173,448.64 USD | `6,436.80` | `1391.82` | `1270.07` | `0.000000` | -785,443.35 USD | `-9.61%` | `1X Cross` |
| `331` | `0x26b6...9a13` | `LONG` | 6,899,750.35 USD | `5,433.73` | `1282.23` | `1270.07` | `232.49` | -67,552.88 USD | `-0.98%` | `10X Cross` |
| `332` | `0xecb6...2b00` | `SHORT` | 6,794,350.61 USD | `5,349.04` | `1279.05` | `1270.07` | `6428.19` | 47,363.94 USD | `+0.70%` | `5X Cross` |
| `343` | `0x45d2...4029` | `SHORT` | 6,637,244.60 USD | `5,227.00` | `833.44` | `1270.07` | `8902.41` | -2,280,866.63 USD | `-34.36%` | `5X Cross` |
| `361` | `0xea00...a918` | `LONG` | 6,350,000.00 USD | `5,000.00` | `739.16` | `1270.07` | `0.000000` | 2,654,184.89 USD | `+41.80%` | `5X Cross` |
| `375` | `0xdd7a...8830` | `LONG` | 6,170,983.24 USD | `4,860.19` | `897.48` | `1270.07` | `782.72` | 1,809,079.57 USD | `+29.32%` | `10X Cross` |
| `418` | `0x469e...58a5` | `SHORT` | 5,291,417.57 USD | `4,163.52` | `1242.31` | `1270.07` | `1977.63` | -119,032.91 USD | `-2.25%` | `10X Cross` |
| `433` | `0x4cae...7c34` | `LONG` | 5,085,284.26 USD | `4,002.27` | `1169.72` | `1270.07` | `984.95` | 403,734.92 USD | `+7.94%` | `10X Cross` |
| `443` | `0xa61c...66b9` | `LONG` | 4,936,593.60 USD | `3,888.00` | `1148.34` | `1270.07` | `0.000000` | 471,851.46 USD | `+9.56%` | `10X Cross` |
| `453` | `0xd4c1...3d1d` | `SHORT` | 4,859,354.01 USD | `3,827.77` | `1292.41` | `1270.07` | `2348.79` | 87,697.22 USD | `+1.80%` | `10X Cross` |
| `468` | `0x9aa5...58af` | `SHORT` | 4,725,165.73 USD | `3,720.31` | `1205.51` | `1270.07` | `3676.07` | -240,278.93 USD | `-5.09%` | `10X Cross` |
| `473` | `0x0153...8052` | `SHORT` | 4,696,688.60 USD | `3,698.18` | `1307.82` | `1270.07` | `2504.88` | 139,882.15 USD | `+2.98%` | `1X Isolated` |
| `502` | `0xb122...e4ba` | `LONG` | 4,441,307.67 USD | `3,498.47` | `1265.25` | `1270.07` | `1095.33` | 14,856.14 USD | `+0.33%` | `10X Cross` |
| `533` | `0x382b...3e39` | `LONG` | 4,150,554.08 USD | `3,269.44` | `1215.08` | `1270.07` | `0.000000` | 177,924.08 USD | `+4.29%` | `10X Cross` |
| `539` | `0xd21d...90f1` | `LONG` | 4,127,500.00 USD | `3,250.00` | `1253.64` | `1270.07` | `876.10` | 53,158.27 USD | `+1.29%` | `4X Isolated` |
| `551` | `0x456f...cdf1` | `LONG` | 4,037,952.30 USD | `3,179.49` | `1267.80` | `1270.07` | `504.18` | 6,997.38 USD | `+0.17%` | `10X Cross` |
| `561` | `0x1338...c48e` | `LONG` | 4,000,091.04 USD | `3,149.43` | `1018.52` | `1270.07` | `820.39` | 792,345.50 USD | `+19.81%` | `4X Isolated` |
| `569` | `0x325e...9564` | `LONG` | 3,937,564.55 USD | `3,101.91` | `1298.07` | `1270.07` | `147.22` | -88,946.15 USD | `-2.26%` | `10X Cross` |
| `578` | `0xdbe0...d6d5` | `LONG` | 3,918,419.90 USD | `3,085.37` | `422.97` | `1270.07` | `338.71` | 2,613,415.41 USD | `+66.70%` | `3X Isolated` |
| `598` | `0x9c06...0560` | `SHORT` | 3,796,448.04 USD | `2,989.80` | `786.00` | `1270.07` | `2553.81` | -1,446,453.04 USD | `-38.10%` | `10X Cross` |
| `605` | `0x27c9...d65d` | `SHORT` | 3,761,587.60 USD | `2,961.88` | `1254.41` | `1270.07` | `1745.05` | -46,172.40 USD | `-1.23%` | `10X Cross` |
| `607` | `0x2e30...4cb5` | `SHORT` | 3,745,050.39 USD | `2,950.02` | `1287.00` | `1270.07` | `2900.63` | 51,625.99 USD | `+1.38%` | `2X Cross` |
| `642` | `0x5323...b23c` | `SHORT` | 3,488,153.30 USD | `2,747.01` | `1267.49` | `1270.07` | `3268.90` | -6,345.65 USD | `-0.18%` | `5X Cross` |
| `684` | `0x71d0...8c26` | `SHORT` | 3,294,989.60 USD | `2,594.48` | `1266.76` | `1270.07` | `3593.20` | -8,418.55 USD | `-0.26%` | `10X Cross` |
| `700` | `0xa183...0482` | `LONG` | 3,217,673.20 USD | `2,534.00` | `530.25` | `1270.07` | `444.63` | 1,874,010.48 USD | `+58.24%` | `5X Isolated` |
| `701` | `0xac48...3201` | `LONG` | 3,215,005.00 USD | `2,531.50` | `1378.58` | `1270.07` | `550.28` | -274,867.28 USD | `-8.55%` | `10X Cross` |
| `711` | `0x0871...e927` | `LONG` | 3,176,500.00 USD | `2,500.00` | `1276.50` | `1270.07` | `0.000000` | -14,750.00 USD | `-0.46%` | `10X Cross` |
| `732` | `0x9b86...6e6e` | `LONG` | 3,128,391.00 USD | `2,463.30` | `637.58` | `1270.07` | `882.57` | 1,557,841.72 USD | `+49.80%` | `3X Cross` |
| `782` | `0xb2f7...af9f` | `SHORT` | 2,938,424.40 USD | `2,313.72` | `746.63` | `1270.07` | `4427.78` | -1,210,935.65 USD | `-41.21%` | `10X Cross` |
| `808` | `0xf48f...10fe` | `LONG` | 2,817,482.30 USD | `2,218.49` | `1517.87` | `1270.07` | `967.81` | -549,904.52 USD | `-19.52%` | `3X Cross` |
| `834` | `0x5bc4...3b0c` | `SHORT` | 2,705,613.65 USD | `2,130.74` | `1089.65` | `1270.07` | `3676.75` | -383,856.07 USD | `-14.19%` | `5X Cross` |
| `849` | `0x8de4...b9aa` | `SHORT` | 2,656,356.56 USD | `2,091.29` | `1331.35` | `1270.07` | `1690.01` | 127,883.15 USD | `+4.81%` | `3X Cross` |
| `857` | `0x4fe2...ac59` | `SHORT` | 2,629,858.12 USD | `2,071.57` | `1478.56` | `1270.07` | `1831.82` | 433,088.10 USD | `+16.47%` | `10X Cross` |
| `865` | `0xdf57...93f5` | `LONG` | 2,607,381.02 USD | `2,054.35` | `1227.36` | `1270.07` | `897.34` | 85,958.98 USD | `+3.30%` | `4X Isolated` |
| `870` | `0xbcd4...0dd2` | `LONG` | 2,583,078.40 USD | `2,033.92` | `1228.20` | `1270.07` | `781.96` | 85,027.59 USD | `+3.29%` | `10X Cross` |
| `882` | `0x413c...886c` | `LONG` | 2,540,000.00 USD | `2,000.00` | `1237.51` | `1270.07` | `0.000000` | 64,976.87 USD | `+2.56%` | `10X Cross` |
| `884` | `0xf29c...9971` | `LONG` | 2,539,600.00 USD | `2,000.00` | `1254.95` | `1270.07` | `0.000000` | 29,702.93 USD | `+1.17%` | `10X Cross` |
| `886` | `0x9a99...d21a` | `LONG` | 2,539,000.00 USD | `2,000.00` | `1278.44` | `1270.07` | `0.000000` | -17,873.67 USD | `-0.70%` | `10X Cross` |
| `907` | `0x77ee...2902` | `SHORT` | 2,472,625.72 USD | `1,946.03` | `759.84` | `1270.07` | `5458.35` | -993,948.21 USD | `-40.20%` | `10X Cross` |
| `917` | `0x3e2f...b269` | `SHORT` | 2,445,012.60 USD | `1,925.51` | `1134.87` | `1270.07` | `2977.28` | -259,813.74 USD | `-10.63%` | `10X Cross` |
| `928` | `0x4f12...618b` | `SHORT` | 2,407,327.46 USD | `1,896.28` | `1608.30` | `1270.07` | `2116.90` | 642,456.93 USD | `+26.69%` | `3X Cross` |
| `970` | `0x866d...d6e1` | `LONG` | 2,289,684.73 USD | `1,802.05` | `674.73` | `1270.07` | `156.90` | 1,073,783.42 USD | `+46.90%` | `10X Cross` |
| `992` | `0x2309...a2d9` | `LONG` | 2,224,545.23 USD | `1,750.37` | `1186.09` | `1270.07` | `813.16` | 148,451.12 USD | `+6.67%` | `8X Cross` |
| `1022` | `0x3205...40bb` | `SHORT` | 2,112,810.10 USD | `1,663.63` | `1256.96` | `1270.07` | `2109.76` | -21,689.86 USD | `-1.03%` | `10X Cross` |
| `1027` | `0x265e...7f70` | `LONG` | 2,097,874.97 USD | `1,651.74` | `1382.98` | `1270.07` | `0.000000` | -186,447.79 USD | `-8.89%` | `3X Cross` |
| `1039` | `0xfe7c...b7ae` | `SHORT` | 2,086,481.33 USD | `1,642.64` | `1346.92` | `1270.07` | `5653.31` | 126,027.29 USD | `+6.04%` | `10X Cross` |
| `1043` | `0x3e47...aaf6` | `LONG` | 2,078,075.60 USD | `1,636.28` | `1278.38` | `1270.07` | `1047.22` | -13,716.19 USD | `-0.66%` | `10X Cross` |
| `1047` | `0x2edd...8179` | `SHORT` | 2,074,059.97 USD | `1,633.89` | `1261.58` | `1270.07` | `2914.21` | -12,778.05 USD | `-0.62%` | `10X Cross` |
| `1060` | `0x7f75...9edf` | `LONG` | 2,048,593.74 USD | `1,611.67` | `1200.24` | `1270.07` | `983.81` | 114,209.76 USD | `+5.58%` | `10X Cross` |
| `1073` | `0x6646...6de5` | `SHORT` | 2,032,000.00 USD | `1,600.00` | `660.64` | `1270.07` | `4275.81` | -974,975.03 USD | `-47.98%` | `10X Cross` |
| `1078` | `0x023a...2355` | `SHORT` | 2,025,044.53 USD | `1,594.90` | `1310.00` | `1270.07` | `4456.54` | 64,267.61 USD | `+3.17%` | `10X Cross` |
| `1097` | `0xfc27...9d9d` | `SHORT` | 1,990,411.50 USD | `1,567.50` | `1296.12` | `1270.07` | `12376.87` | 41,253.06 USD | `+2.07%` | `10X Cross` |
| `1101` | `0xab59...59b5` | `LONG` | 1,987,956.40 USD | `1,565.32` | `1342.15` | `1270.07` | `828.75` | -112,938.82 USD | `-5.68%` | `10X Cross` |
| `1148` | `0x039c...0ebd` | `SHORT` | 1,929,119.50 USD | `1,519.59` | `1245.14` | `1270.07` | `3219.98` | -37,010.87 USD | `-1.92%` | `10X Cross` |
| `1166` | `0xcf67...eb24` | `LONG` | 1,904,250.00 USD | `1,500.00` | `887.05` | `1270.07` | `641.15` | 573,678.63 USD | `+30.13%` | `10X Cross` |
| `1174` | `0xb695...a92d` | `LONG` | 1,883,113.40 USD | `1,483.00` | `1249.80` | `1270.07` | `0.000000` | 29,654.54 USD | `+1.57%` | `10X Cross` |
| `1180` | `0x7277...0b98` | `SHORT` | 1,872,996.52 USD | `1,475.73` | `1287.86` | `1270.07` | `2168.50` | 27,535.61 USD | `+1.47%` | `10X Cross` |
| `1242` | `0x2ab7...c2f8` | `LONG` | 1,778,367.60 USD | `1,400.51` | `813.26` | `1270.07` | `790.53` | 639,385.91 USD | `+35.95%` | `3X Cross` |
| `1252` | `0xe35c...a1d3` | `LONG` | 1,763,816.45 USD | `1,389.16` | `1311.66` | `1270.07` | `690.81` | -58,286.26 USD | `-3.30%` | `2X Isolated` |
| `1263` | `0x11be...8b1d` | `LONG` | 1,747,304.10 USD | `1,375.83` | `1206.55` | `1270.07` | `1134.61` | 87,296.14 USD | `+5.00%` | `10X Isolated` |
| `1346` | `0xe065...0f85` | `SHORT` | 1,602,883.40 USD | `1,262.61` | `1087.02` | `1270.07` | `1588.61` | -230,407.27 USD | `-14.37%` | `10X Cross` |
| `1419` | `0x266b...efcb` | `LONG` | 1,524,000.00 USD | `1,200.00` | `893.76` | `1270.07` | `391.64` | 451,490.30 USD | `+29.63%` | `10X Cross` |
| `1420` | `0x5975...9abd` | `LONG` | 1,524,000.00 USD | `1,200.00` | `1179.54` | `1270.07` | `486.47` | 108,557.21 USD | `+7.12%` | `5X Cross` |
| `1438` | `0x2847...d47b` | `LONG` | 1,507,630.54 USD | `1,186.27` | `1232.07` | `1270.07` | `0.000000` | 46,062.04 USD | `+3.06%` | `5X Cross` |
| `1459` | `0x69cc...14fd` | `SHORT` | 1,473,998.11 USD | `1,161.36` | `675.33` | `1270.07` | `7983.00` | -689,692.58 USD | `-46.79%` | `10X Cross` |
| `1474` | `0x3fc5...c0c1` | `SHORT` | 1,458,518.80 USD | `1,148.44` | `1264.34` | `1270.07` | `2671.06` | -6,505.02 USD | `-0.45%` | `10X Cross` |
| `1496` | `0x38f9...cb04` | `SHORT` | 1,443,853.13 USD | `1,137.34` | `1252.77` | `1270.07` | `2002.25` | -19,027.43 USD | `-1.32%` | `10X Cross` |
| `1515` | `0x5f94...4b96` | `LONG` | 1,416,392.90 USD | `1,115.27` | `538.00` | `1270.07` | `0.000000` | 816,375.26 USD | `+57.64%` | `10X Cross` |
| `1531` | `0x9e7e...0047` | `LONG` | 1,397,533.40 USD | `1,100.42` | `1283.06` | `1270.07` | `1194.42` | -14,372.33 USD | `-1.03%` | `10X Cross` |
| `1534` | `0x71df...a23d` | `SHORT` | 1,395,474.57 USD | `1,098.28` | `513.50` | `1270.07` | `2560.13` | -831,504.38 USD | `-59.59%` | `2X Cross` |
| `1568` | `0xbfc7...80b4` | `SHORT` | 1,366,217.50 USD | `1,075.00` | `558.03` | `1270.07` | `2688.77` | -766,338.77 USD | `-56.09%` | `10X Cross` |
| `1594` | `0xdf83...3cff` | `SHORT` | 1,331,023.50 USD | `1,048.05` | `1260.93` | `1270.07` | `1893.13` | -9,507.09 USD | `-0.71%` | `10X Cross` |
| `1638` | `0x123d...3bff` | `SHORT` | 1,284,642.65 USD | `1,011.45` | `494.46` | `1270.07` | `4355.24` | -784,522.54 USD | `-61.07%` | `10X Cross` |
| `1649` | `0x668c...ea2e` | `SHORT` | 1,270,900.00 USD | `1,000.00` | `1406.98` | `1270.07` | `4210.51` | 136,081.99 USD | `+10.71%` | `10X Cross` |
| `1654` | `0xe282...df29` | `LONG` | 1,269,700.00 USD | `1,000.00` | `420.99` | `1270.07` | `800.02` | 848,713.14 USD | `+66.84%` | `10X Cross` |
| `1675` | `0x17f0...094f` | `LONG` | 1,250,651.58 USD | `984.30` | `1287.23` | `1270.07` | `536.96` | -16,368.58 USD | `-1.31%` | `5X Cross` |
| `1694` | `0x51f6...2b39` | `SHORT` | 1,235,663.26 USD | `972.81` | `1299.77` | `1270.07` | `2545.56` | 28,764.44 USD | `+2.33%` | `10X Cross` |
| `1754` | `0x757d...94ba` | `LONG` | 1,174,565.00 USD | `925.00` | `1558.31` | `1270.07` | `0.000000` | -266,875.59 USD | `-22.72%` | `10X Cross` |
| `1759` | `0xaa82...9556` | `LONG` | 1,172,905.80 USD | `924.13` | `1254.72` | `1270.07` | `180.00` | 13,379.12 USD | `+1.14%` | `10X Cross` |
| `1798` | `0xb911...5525` | `LONG` | 1,143,000.00 USD | `900.00` | `1294.82` | `1270.07` | `1035.40` | -22,337.82 USD | `-1.95%` | `10X Cross` |
| `1813` | `0xef96...9383` | `SHORT` | 1,127,645.45 USD | `887.77` | `1259.32` | `1270.07` | `5209.63` | -9,658.58 USD | `-0.86%` | `10X Cross` |
| `1849` | `0xcf0a...856f` | `LONG` | 1,107,318.76 USD | `871.15` | `1292.19` | `1270.07` | `1011.13` | -18,376.08 USD | `-1.66%` | `4X Cross` |
| `1873` | `0xdf95...7d72` | `SHORT` | 1,083,482.25 USD | `853.27` | `1074.39` | `1270.07` | `44429.92` | -166,734.80 USD | `-15.39%` | `10X Cross` |
| `1906` | `0x601c...4f54` | `SHORT` | 1,047,095.84 USD | `824.42` | `615.11` | `1270.07` | `3085.22` | -539,983.09 USD | `-51.57%` | `5X Cross` |
| `1928` | `0xae55...2236` | `LONG` | 1,038,023.41 USD | `817.47` | `1467.80` | `1270.07` | `0.000000` | -161,857.81 USD | `-15.59%` | `10X Cross` |
| `1971` | `0x0f02...5384` | `LONG` | 1,016,349.98 USD | `800.78` | `1290.36` | `1270.07` | `299.47` | -16,944.09 USD | `-1.67%` | `3X Cross` |
| `1972` | `0x9b0f...db40` | `LONG` | 1,016,000.00 USD | `800.00` | `1268.86` | `1270.07` | `792.53` | 910.24 USD | `+0.09%` | `10X Cross` |
| `1973` | `0x11ee...1d1d` | `SHORT` | 1,015,840.00 USD | `800.00` | `1269.65` | `1270.07` | `1597.35` | -116.99 USD | `-0.01%` | `5X Cross` |
| `1991` | `0xabdb...84ac` | `LONG` | 1,008,700.62 USD | `793.69` | `711.79` | `1270.07` | `664.53` | 443,760.26 USD | `+43.99%` | `3X Cross` |
| `1993` | `0x6e8f...4364` | `LONG` | 1,007,697.41 USD | `793.65` | `1260.00` | `1270.07` | `966.58` | 7,698.40 USD | `+0.76%` | `10X Cross` |
| `2002` | `0x2577...4897` | `SHORT` | 1,001,336.77 USD | `788.33` | `1272.28` | `1270.07` | `5365.36` | 1,642.27 USD | `+0.16%` | `10X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `1234.70` | 3,481.85 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 3.48K USD at 1234.7000 USD [API] | `2026-10-29 02:35:52` |
| `ANNOUNCEMENT` | `INFO` | `1190.50` | 35.71 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 0.04K USD at 1190.5000 USD [API] | `2026-10-22 18:01:21` |
| `ANNOUNCEMENT` | `INFO` | `1615.00` | 500.65 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 0.50K USD at 1615.0000 USD [API] | `2026-09-26 21:18:11` |
| `ANNOUNCEMENT` | `INFO` | `1615.00` | 8,075.00 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 8.07K USD at 1615.0000 USD [API] | `2026-09-26 21:18:11` |
| `ANNOUNCEMENT` | `INFO` | `1615.00` | 403.75 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 0.40K USD at 1615.0000 USD [API] | `2026-09-26 21:18:11` |
| `ANNOUNCEMENT` | `INFO` | `1615.00` | 18,766.30 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 18.77K USD at 1615.0000 USD [API] | `2026-09-26 21:18:11` |
| `ANNOUNCEMENT` | `INFO` | `1615.00` | 40,375.00 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 40.38K USD at 1615.0000 USD [API] | `2026-09-26 21:18:11` |
| `ANNOUNCEMENT` | `INFO` | `1615.00` | 161.50 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 0.16K USD at 1615.0000 USD [API] | `2026-09-26 21:18:11` |
| `ANNOUNCEMENT` | `INFO` | `1614.90` | 3,100.61 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 3.10K USD at 1614.9000 USD [API] | `2026-09-26 21:18:11` |
| `ANNOUNCEMENT` | `INFO` | `1614.90` | 6,411.15 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 6.41K USD at 1614.9000 USD [API] | `2026-09-26 21:18:11` |
| `ANNOUNCEMENT` | `INFO` | `1614.90` | 209.94 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 0.21K USD at 1614.9000 USD [API] | `2026-09-26 21:18:11` |
| `ANNOUNCEMENT` | `INFO` | `1614.90` | 161.49 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 0.16K USD at 1614.9000 USD [API] | `2026-09-26 21:18:11` |
| `ANNOUNCEMENT` | `INFO` | `1614.80` | 500.59 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 0.50K USD at 1614.8000 USD [API] | `2026-09-26 21:18:11` |
| `ANNOUNCEMENT` | `INFO` | `1233.00` | 17,249.67 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 17.25K USD at 1233.0000 USD [API] | `2026-10-29 03:25:29` |
| `ANNOUNCEMENT` | `INFO` | `1233.10` | 2,638.83 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 2.64K USD at 1233.1000 USD [API] | `2026-10-29 03:25:29` |
| `ANNOUNCEMENT` | `INFO` | `1237.60` | 284.65 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 0.28K USD at 1237.6000 USD [API] | `2026-10-29 02:31:04` |
| `ANNOUNCEMENT` | `INFO` | `1237.60` | 185.64 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 0.19K USD at 1237.6000 USD [API] | `2026-10-29 02:31:04` |
| `ANNOUNCEMENT` | `INFO` | `1237.60` | 61.88 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 0.06K USD at 1237.6000 USD [API] | `2026-10-29 02:31:04` |
| `ANNOUNCEMENT` | `INFO` | `655.00` | 9,602.30 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 9.60K USD at 655.0000 USD [API] | `2025-11-07 14:41:41` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`1404.55` (Vol: 3,000,000.00 USD, Dist: `+10.33%`) | Long MP=`1176.48` (Vol: 3,400,000.00 USD, Dist: `--7.58%`)
  * 48H Horizon: Short MP=`1404.55` (Vol: 3,000,000.00 USD, Dist: `+10.33%`) | Long MP=`1176.48` (Vol: 3,400,000.00 USD, Dist: `--7.58%`)
  * 3D Horizon: Short MP=`1404.55` (Vol: 3,000,000.00 USD, Dist: `+10.33%`) | Long MP=`1176.48` (Vol: 3,400,000.00 USD, Dist: `--7.58%`)
  * 7D Horizon: Short MP=`1404.10` (Vol: 3,000,000.00 USD, Dist: `+10.30%`) | Long MP=`1176.74` (Vol: 4,900,000.00 USD, Dist: `--7.56%`)
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
| `5m` | `BALANCED` | 0.00 USD | 1,750.00 USD | 1,750.00 USD | 1,750.00 USD | `1` | `2026-10-30 06:00:00 UTC - 2026-10-30 06:05:00 UTC` |
| `15m` | `BALANCED` | 0.00 USD | 1,750.00 USD | 1,750.00 USD | 1,750.00 USD | `1` | `2026-10-30 06:00:00 UTC - 2026-10-30 06:15:00 UTC` |
| `1h` | `BALANCED` | 0.00 USD | 1,750.00 USD | 1,750.00 USD | 1,750.00 USD | `1` | `2026-10-30 06:00:00 UTC - 2026-10-30 07:00:00 UTC` |
| `4h` | `BALANCED` | 0.00 USD | 1,750.00 USD | 1,750.00 USD | 1,750.00 USD | `1` | `2026-10-30 04:00:00 UTC - 2026-10-30 08:00:00 UTC` |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `0 USD` | Total OI Tokens: `-`
  * 1h OI Change: `0.00%` | 4h OI Change: `0.00%` | 24h OI Change: `0.00%`
  * Exchange Breakdown: Binance=`-` | Bybit=`-` | OKX=`-` | Hyperliquid=`-`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `77.96K` | Last 24h: `134.73K` | Last 3d: `246.48K` | Last 7d: `772.71K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0086%` | **USDT OKX** | `0.0100%` |
| **USDT Bybit** | `0.0100%` | **USDT KuCoin** | `0.0100%` |
| **USDT MEXC** | `0.0085%` | **USDT BingX** | `0.0100%` |
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
| `5:00 UTC` | `1279.95` | `1280.45` | `1279.95` | `1287.45` | `1275.15` | 19,925,691.14 USD | 8,662,599.23 USD | 11,263,091.92 USD | -2,600,492.69 USD | `-13.05%` | `1B / 6S` |
| `0:00 UTC` | `1275.15` | `1271.95` | `1275.15` | `1279.35` | `1264.95` | 23,738,198.29 USD | 11,363,344.84 USD | 12,374,853.45 USD | -1,011,508.62 USD | `-4.26%` | `3B / 3S` |
| `5:00 UTC` | `1279.05` | `1280.95` | `1279.05` | `1287.45` | `1274.25` | 14,930,858.33 USD | 7,292,403.22 USD | 7,638,455.11 USD | -346,051.88 USD | `-2.32%` | `2B / 4S` |
| `0:00 UTC` | `1285.05` | `1286.06` | `1285.05` | `1289.85` | `1282.05` | 15,953,463.93 USD | 6,542,642.51 USD | 9,410,821.42 USD | -2,868,178.91 USD | `-17.98%` | `1B / 3S` |
| `5:00 UTC` | `1276.95` | `1279.23` | `1276.95` | `1286.25` | `1275.15` | 15,449,899.62 USD | 6,063,485.10 USD | 9,386,414.52 USD | -3,322,929.42 USD | `-21.51%` | `0B / 8S` |
| `0:00 UTC` | `1275.15` | `1278.02` | `1275.15` | `1285.05` | `1272.15` | 16,039,119.46 USD | 6,719,465.52 USD | 9,319,653.95 USD | -2,600,188.43 USD | `-16.21%` | `2B / 3S` |
| `5:00 UTC` | `1272.15` | `1274.44` | `1272.15` | `1278.75` | `1270.65` | 10,354,318.48 USD | 4,552,930.99 USD | 5,801,387.50 USD | -1,248,456.51 USD | `-12.06%` | `0B / 2S` |
| `0:00 UTC` | `1270.05` | `1270.86` | `1270.05` | `1275.75` | `1267.35` | 11,469,050.63 USD | 5,693,129.81 USD | 5,775,920.83 USD | -82,791.02 USD | `-0.72%` | `1B / 1S` |
| `5:00 UTC` | `1266.75` | `1270.68` | `1266.75` | `1276.95` | `1265.25` | 9,416,171.49 USD | 3,994,637.12 USD | 5,421,534.37 USD | -1,426,897.25 USD | `-15.15%` | `0B / 7S` |
| `0:00 UTC` | `1270.95` | `1269.16` | `1270.95` | `1274.25` | `1263.15` | 7,981,868.45 USD | 3,939,177.59 USD | 4,042,690.86 USD | -103,513.28 USD | `-1.30%` | `2B / 5S` |

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
| `5m` | 16,290.00 USD | -1,840,000.00 USD | **`DISTRIBUTION`** |
| `15m` | -257,330.00 USD | -7,010,000.00 USD | **`DISTRIBUTION`** |
| `30m` | -78,290.00 USD | -7,220,000.00 USD | **`DISTRIBUTION`** |
| `1h` | -441,520.00 USD | -8,770,000.00 USD | **`DISTRIBUTION`** |
| `2h` | -481,030.00 USD | -14,160,000.00 USD | **`DISTRIBUTION`** |
| `4h` | 3,400,000.00 USD | -3,690,000.00 USD | **`DISTRIBUTION`** |
| `6h` | 595,670.00 USD | 3,870,000.00 USD | **`ACCUMULATION`** |
| `8h` | -1,010,000.00 USD | 14,410,000.00 USD | **`ACCUMULATION`** |
| `12h` | -10,470,000.00 USD | -20,000,000.00 USD | **`DISTRIBUTION`** |
| `24h` | 15,460,000.00 USD | 90,610,000.00 USD | **`ACCUMULATION`** |
| `1w` | 35,510,000.00 USD | 214,480,000.00 USD | **`ACCUMULATION`** |
| `30d` | 60,270,000.00 USD | -524,300,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+16.29K` | 15m=`-257.33K` | 1h=`-441.52K` | 24h=`+15.46M`
* Futures Capital Netflows: 5m=`-1.84M` | 15m=`-7.01M` | 1h=`-8.77M` | 24h=`+90.61M`
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
  * `2026-10-30 11:03:46 IST`: [kitco.com] - (Sentiment: `Neutral`)
  * `2026-10-30 11:38:46 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 11:37:46 IST`: [forex.com] - (Sentiment: `Neutral`)
  * `2026-10-30 08:39:46 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 08:39:46 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 08:39:46 IST`: [financemagnates.com] - (Sentiment: `Neutral`)
  * `2026-10-30 07:39:46 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-30 06:39:46 IST`: [kathleenhays.substack.com] - (Sentiment: `Neutral`)
  * `2026-10-30 06:39:46 IST`: [rba.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 06:39:46 IST`: [abs.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 06:39:46 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 05:39:46 IST`: [@NodeWire] - (Sentiment: `Neutral`)
  * `2026-10-30 05:39:46 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 05:39:46 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 05:39:46 IST`: [@financialjuice] - (Sentiment: `Neutral`)


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
  * Execution Entry: `1235.31` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `1215.00` (Risk Distance: `20.31` pts)
  * +2.5R Take Profit: `1286.08`
  * Mathematical Lot Sizing: **`0.49 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `1285.56` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `1305.87` (Risk Distance: `20.31` pts)
  * +2.5R Take Profit: `1234.79`
  * Mathematical Lot Sizing: **`0.49 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`1279.51`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
