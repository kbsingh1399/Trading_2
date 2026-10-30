# 🏛️ SOVEREIGN CANDIDATE DOSSIER: ZECUSD
**Canonical Key**: `ZECUSD` | **Broker Instrument**: `ZECUSD.p` | **Asset Class**: `Crypto Altcoin`
**Timestamp**: `2026-10-30 10:01:31 IST` (`2026-10-30 04:31:31 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

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
| `13` | `0xb83d...6e36` | `SHORT` | 67,451,531.17 USD | `52,385.47` | `1336.45` | `1286.70` | `3703.42` | 2,559,036.23 USD | `+3.79%` | `3X Cross` |
| `22` | `0x5b5d...c060` | `SHORT` | 51,640,228.20 USD | `40,121.38` | `1478.36` | `1286.70` | `5127.92` | 7,673,806.91 USD | `+14.86%` | `3X Cross` |
| `39` | `0x7fda...17d1` | `SHORT` | 32,685,099.44 USD | `25,376.63` | `1262.04` | `1286.70` | `2653.89` | -658,673.87 USD | `-2.02%` | `5X Cross` |
| `79` | `0x60b0...991e` | `LONG` | 21,610,627.15 USD | `16,779.74` | `1179.65` | `1286.70` | `926.11` | 1,816,380.13 USD | `+8.41%` | `10X Cross` |
| `137` | `0xc36a...105b` | `LONG` | 14,815,576.42 USD | `11,510.82` | `1215.14` | `1286.70` | `962.71` | 828,295.39 USD | `+5.59%` | `10X Cross` |
| `152` | `0x9071...5c0b` | `LONG` | 13,542,062.60 USD | `10,517.29` | `1353.83` | `1286.70` | `0.1437` | -696,556.27 USD | `-5.14%` | `1X Cross` |
| `172` | `0x8742...8427` | `LONG` | 11,848,398.12 USD | `9,201.21` | `1286.37` | `1286.70` | `701.38` | 12,228.12 USD | `+0.10%` | `10X Cross` |
| `187` | `0x58b2...11f3` | `LONG` | 11,026,678.12 USD | `8,563.08` | `1246.56` | `1286.70` | `381.54` | 352,260.54 USD | `+3.19%` | `10X Cross` |
| `194` | `0xad59...ba81` | `SHORT` | 10,847,090.61 USD | `8,425.00` | `330.91` | `1286.70` | `2144.55` | -8,059,132.84 USD | `-74.30%` | `10X Cross` |
| `197` | `0x9ffd...ce40` | `LONG` | 10,752,642.68 USD | `8,350.27` | `1251.19` | `1286.70` | `592.20` | 304,848.68 USD | `+2.84%` | `5X Cross` |
| `203` | `0xdd53...2b13` | `SHORT` | 10,556,344.96 USD | `8,195.92` | `741.54` | `1286.70` | `8514.88` | -4,478,748.60 USD | `-42.43%` | `3X Cross` |
| `218` | `0x880a...311c` | `SHORT` | 9,917,509.15 USD | `7,707.11` | `1367.50` | `1286.70` | `2240.16` | 621,975.05 USD | `+6.27%` | `10X Cross` |
| `234` | `0xbf73...5d58` | `LONG` | 9,608,250.00 USD | `7,500.00` | `1248.78` | `1286.70` | `125.38` | 242,404.38 USD | `+2.52%` | `10X Cross` |
| `267` | `0x2b61...2f6c` | `LONG` | 8,691,177.60 USD | `6,807.00` | `1453.56` | `1286.70` | `564.41` | -1,203,173.62 USD | `-13.84%` | `10X Cross` |
| `282` | `0x2ae5...83e7` | `LONG` | 8,288,023.68 USD | `6,436.80` | `1391.82` | `1286.70` | `0.000000` | -670,868.31 USD | `-8.09%` | `1X Cross` |
| `330` | `0x26b6...9a13` | `LONG` | 6,996,470.75 USD | `5,433.73` | `1282.23` | `1286.70` | `219.61` | 29,167.51 USD | `+0.42%` | `10X Cross` |
| `336` | `0x45d2...4029` | `SHORT` | 6,730,807.90 USD | `5,227.00` | `833.44` | `1286.70` | `8943.38` | -2,374,429.93 USD | `-35.28%` | `5X Cross` |
| `355` | `0xecb6...2b00` | `SHORT` | 6,541,095.12 USD | `5,078.49` | `1279.00` | `1286.70` | `6469.04` | -45,694.03 USD | `-0.70%` | `5X Cross` |
| `359` | `0xea00...a918` | `LONG` | 6,441,000.00 USD | `5,000.00` | `739.16` | `1286.70` | `0.000000` | 2,745,184.89 USD | `+42.62%` | `5X Cross` |
| `372` | `0xdd7a...8830` | `LONG` | 6,256,522.59 USD | `4,860.19` | `897.48` | `1286.70` | `785.66` | 1,894,618.91 USD | `+30.28%` | `10X Cross` |
| `417` | `0x469e...58a5` | `SHORT` | 5,316,398.69 USD | `4,163.52` | `1242.31` | `1286.70` | `1967.94` | -144,014.03 USD | `-2.71%` | `10X Cross` |
| `425` | `0x4cae...7c34` | `LONG` | 5,147,719.67 USD | `4,002.27` | `1169.72` | `1286.70` | `978.93` | 466,170.33 USD | `+9.06%` | `10X Cross` |
| `438` | `0xa61c...66b9` | `LONG` | 5,005,022.40 USD | `3,888.00` | `1148.34` | `1286.70` | `0.000000` | 540,280.26 USD | `+10.79%` | `10X Cross` |
| `457` | `0x9aa5...58af` | `SHORT` | 4,790,271.16 USD | `3,720.31` | `1205.51` | `1286.70` | `3681.29` | -305,384.36 USD | `-6.38%` | `10X Cross` |
| `462` | `0x0153...8052` | `SHORT` | 4,758,448.21 USD | `3,698.18` | `1307.82` | `1286.70` | `2504.85` | 78,122.54 USD | `+1.64%` | `1X Isolated` |
| `520` | `0xd4c1...3d1d` | `SHORT` | 4,275,400.08 USD | `3,319.41` | `1294.02` | `1286.70` | `2539.79` | 19,977.16 USD | `+0.47%` | `10X Cross` |
| `521` | `0x382b...3e39` | `LONG` | 4,254,238.88 USD | `3,303.75` | `1215.08` | `1286.70` | `0.000000` | 239,919.49 USD | `+5.64%` | `10X Cross` |
| `533` | `0xd21d...90f1` | `LONG` | 4,184,337.62 USD | `3,250.00` | `1253.64` | `1286.70` | `876.06` | 109,995.89 USD | `+2.63%` | `4X Isolated` |
| `537` | `0x456f...cdf1` | `LONG` | 4,156,480.36 USD | `3,226.58` | `1267.75` | `1286.70` | `516.66` | 65,993.73 USD | `+1.59%` | `10X Cross` |
| `554` | `0x1338...c48e` | `LONG` | 4,028,718.73 USD | `3,149.43` | `1018.52` | `1286.70` | `820.35` | 820,973.19 USD | `+20.38%` | `4X Isolated` |
| `559` | `0x325e...9564` | `LONG` | 3,994,949.89 USD | `3,101.91` | `1298.07` | `1286.70` | `153.82` | -31,560.81 USD | `-0.79%` | `10X Cross` |
| `565` | `0xdbe0...d6d5` | `LONG` | 3,969,945.58 USD | `3,085.37` | `422.97` | `1286.70` | `338.67` | 2,664,941.09 USD | `+67.13%` | `3X Isolated` |
| `581` | `0x2e30...4cb5` | `SHORT` | 3,907,518.35 USD | `3,034.73` | `1287.61` | `1286.70` | `2854.06` | 32.20 USD | `+0.00%` | `2X Cross` |
| `590` | `0x9c06...0560` | `SHORT` | 3,848,171.58 USD | `2,989.80` | `786.00` | `1286.70` | `2582.19` | -1,498,176.58 USD | `-38.93%` | `10X Cross` |
| `593` | `0x27c9...d65d` | `SHORT` | 3,815,493.82 USD | `2,961.88` | `1254.41` | `1286.70` | `1726.21` | -100,078.61 USD | `-2.62%` | `10X Cross` |
| `661` | `0x5323...b23c` | `SHORT` | 3,391,930.57 USD | `2,634.10` | `1264.16` | `1286.70` | `3313.72` | -62,017.68 USD | `-1.83%` | `5X Cross` |
| `685` | `0xa183...0482` | `LONG` | 3,263,031.80 USD | `2,534.00` | `530.25` | `1286.70` | `444.59` | 1,919,369.08 USD | `+58.82%` | `5X Isolated` |
| `691` | `0xac48...3201` | `LONG` | 3,243,104.65 USD | `2,531.50` | `1378.58` | `1286.70` | `528.73` | -246,767.63 USD | `-7.61%` | `10X Cross` |
| `702` | `0x0871...e927` | `LONG` | 3,207,000.00 USD | `2,500.00` | `1276.50` | `1286.70` | `0.000000` | 15,750.00 USD | `+0.49%` | `10X Cross` |
| `713` | `0x9b86...6e6e` | `LONG` | 3,156,226.29 USD | `2,463.30` | `637.58` | `1286.70` | `882.52` | 1,585,677.01 USD | `+50.24%` | `3X Cross` |
| `732` | `0xb122...e4ba` | `LONG` | 3,097,129.04 USD | `2,404.79` | `1259.16` | `1286.70` | `973.38` | 69,110.59 USD | `+2.23%` | `10X Cross` |
| `746` | `0x71d0...8c26` | `SHORT` | 3,071,041.88 USD | `2,385.09` | `1263.98` | `1286.70` | `3526.51` | -56,335.83 USD | `-1.83%` | `10X Cross` |
| `771` | `0xb2f7...af9f` | `SHORT` | 2,964,569.44 USD | `2,313.72` | `746.63` | `1286.70` | `4461.96` | -1,237,080.69 USD | `-41.73%` | `10X Cross` |
| `782` | `0x413c...886c` | `LONG` | 2,898,450.00 USD | `2,250.00` | `1237.51` | `1286.70` | `0.000000` | 114,048.97 USD | `+3.93%` | `10X Cross` |
| `797` | `0xf48f...10fe` | `LONG` | 2,856,527.72 USD | `2,218.49` | `1517.87` | `1286.70` | `969.99` | -510,859.10 USD | `-17.88%` | `3X Cross` |
| `824` | `0x5bc4...3b0c` | `SHORT` | 2,744,393.12 USD | `2,130.74` | `1089.65` | `1286.70` | `3692.20` | -422,635.54 USD | `-15.40%` | `5X Cross` |
| `845` | `0x8de4...b9aa` | `SHORT` | 2,692,954.13 USD | `2,091.29` | `1331.35` | `1286.70` | `1689.97` | 91,285.57 USD | `+3.39%` | `3X Cross` |
| `854` | `0x4fe2...ac59` | `SHORT` | 2,667,975.00 USD | `2,071.57` | `1478.56` | `1286.70` | `1835.83` | 394,971.21 USD | `+14.80%` | `10X Cross` |
| `863` | `0xdf57...93f5` | `LONG` | 2,646,002.80 USD | `2,054.35` | `1227.36` | `1286.70` | `897.30` | 124,580.76 USD | `+4.71%` | `4X Isolated` |
| `869` | `0xbcd4...0dd2` | `LONG` | 2,618,648.61 USD | `2,033.92` | `1228.20` | `1286.70` | `746.95` | 120,597.80 USD | `+4.61%` | `10X Cross` |
| `881` | `0x9a99...d21a` | `LONG` | 2,575,400.00 USD | `2,000.00` | `1278.44` | `1286.70` | `0.000000` | 18,526.33 USD | `+0.72%` | `10X Cross` |
| `882` | `0xf29c...9971` | `LONG` | 2,575,400.00 USD | `2,000.00` | `1254.95` | `1286.70` | `0.000000` | 65,502.93 USD | `+2.54%` | `10X Cross` |
| `908` | `0x77ee...2902` | `SHORT` | 2,484,691.10 USD | `1,946.03` | `759.84` | `1286.70` | `5440.11` | -1,006,013.60 USD | `-40.49%` | `10X Cross` |
| `911` | `0x3e2f...b269` | `SHORT` | 2,476,590.96 USD | `1,925.51` | `1134.87` | `1286.70` | `2931.90` | -291,392.11 USD | `-11.77%` | `10X Cross` |
| `924` | `0x4f12...618b` | `SHORT` | 2,441,839.76 USD | `1,896.28` | `1608.30` | `1286.70` | `2116.86` | 607,944.63 USD | `+24.90%` | `3X Cross` |
| `963` | `0x866d...d6e1` | `LONG` | 2,311,669.74 USD | `1,802.05` | `674.73` | `1286.70` | `202.22` | 1,095,768.43 USD | `+47.40%` | `10X Cross` |
| `980` | `0x2309...a2d9` | `LONG` | 2,252,901.23 USD | `1,750.37` | `1186.09` | `1286.70` | `813.29` | 176,807.12 USD | `+7.85%` | `8X Cross` |
| `1025` | `0x265e...7f70` | `LONG` | 2,126,945.60 USD | `1,651.74` | `1382.98` | `1286.70` | `0.000000` | -157,377.16 USD | `-7.40%` | `3X Cross` |
| `1028` | `0xfe7c...b7ae` | `SHORT` | 2,115,556.06 USD | `1,642.64` | `1346.92` | `1286.70` | `5693.06` | 96,952.56 USD | `+4.58%` | `10X Cross` |
| `1032` | `0x3e47...aaf6` | `LONG` | 2,106,691.68 USD | `1,636.28` | `1278.38` | `1286.70` | `1048.34` | 14,899.90 USD | `+0.71%` | `10X Cross` |
| `1035` | `0x2edd...8179` | `SHORT` | 2,102,979.82 USD | `1,633.89` | `1261.58` | `1286.70` | `2892.99` | -41,697.90 USD | `-1.98%` | `10X Cross` |
| `1046` | `0x3205...40bb` | `SHORT` | 2,079,680.02 USD | `1,615.16` | `1252.62` | `1286.70` | `2143.71` | -56,499.96 USD | `-2.72%` | `10X Cross` |
| `1047` | `0x7f75...9edf` | `LONG` | 2,074,380.46 USD | `1,611.67` | `1200.24` | `1286.70` | `983.02` | 139,996.48 USD | `+6.75%` | `10X Cross` |
| `1057` | `0x6646...6de5` | `SHORT` | 2,057,760.00 USD | `1,600.00` | `660.64` | `1286.70` | `4284.30` | -1,000,735.03 USD | `-48.63%` | `10X Cross` |
| `1060` | `0x023a...2355` | `SHORT` | 2,053,114.77 USD | `1,594.90` | `1310.00` | `1286.70` | `4434.41` | 36,197.37 USD | `+1.76%` | `10X Cross` |
| `1088` | `0xab59...59b5` | `LONG` | 2,016,445.22 USD | `1,565.32` | `1342.15` | `1286.70` | `834.50` | -84,449.99 USD | `-4.19%` | `10X Cross` |
| `1150` | `0xcf67...eb24` | `LONG` | 1,931,850.00 USD | `1,500.00` | `887.05` | `1286.70` | `648.29` | 601,278.63 USD | `+31.12%` | `10X Cross` |
| `1164` | `0xb695...a92d` | `LONG` | 1,909,659.10 USD | `1,483.00` | `1249.80` | `1286.70` | `0.000000` | 56,200.25 USD | `+2.94%` | `10X Cross` |
| `1172` | `0x7277...0b98` | `SHORT` | 1,900,740.24 USD | `1,475.73` | `1287.86` | `1286.70` | `2180.25` | -208.12 USD | `-0.01%` | `10X Cross` |
| `1230` | `0x2ab7...c2f8` | `LONG` | 1,803,296.68 USD | `1,400.51` | `813.26` | `1286.70` | `790.96` | 664,314.99 USD | `+36.84%` | `3X Cross` |
| `1247` | `0xe35c...a1d3` | `LONG` | 1,786,737.59 USD | `1,389.16` | `1311.66` | `1286.70` | `690.77` | -35,365.12 USD | `-1.98%` | `2X Isolated` |
| `1252` | `0x11be...8b1d` | `LONG` | 1,772,344.21 USD | `1,375.83` | `1206.55` | `1286.70` | `1134.57` | 112,336.25 USD | `+6.34%` | `10X Isolated` |
| `1273` | `0xfc27...9d9d` | `SHORT` | 1,735,335.28 USD | `1,347.31` | `1298.22` | `1286.70` | `14420.35` | 13,770.37 USD | `+0.79%` | `10X Cross` |
| `1323` | `0x039c...0ebd` | `SHORT` | 1,648,369.52 USD | `1,279.79` | `1239.81` | `1286.70` | `3649.13` | -61,667.69 USD | `-3.74%` | `10X Cross` |
| `1338` | `0xe065...0f85` | `SHORT` | 1,625,862.90 USD | `1,262.61` | `1087.02` | `1286.70` | `1589.15` | -253,386.77 USD | `-15.58%` | `10X Cross` |
| `1413` | `0x5975...9abd` | `LONG` | 1,545,840.00 USD | `1,200.00` | `1179.54` | `1286.70` | `483.88` | 130,397.21 USD | `+8.44%` | `5X Cross` |
| `1425` | `0x266b...efcb` | `LONG` | 1,538,160.00 USD | `1,200.00` | `893.76` | `1286.70` | `394.14` | 465,650.30 USD | `+30.27%` | `10X Cross` |
| `1438` | `0x2847...d47b` | `LONG` | 1,521,865.78 USD | `1,186.27` | `1232.07` | `1286.70` | `0.000000` | 60,297.28 USD | `+3.96%` | `5X Cross` |
| `1453` | `0x38f9...cb04` | `SHORT` | 1,502,835.22 USD | `1,167.16` | `1249.74` | `1286.70` | `1977.22` | -44,191.12 USD | `-2.94%` | `10X Cross` |
| `1460` | `0x69cc...14fd` | `SHORT` | 1,493,392.82 USD | `1,161.36` | `675.33` | `1286.70` | `8024.95` | -709,087.30 USD | `-47.48%` | `10X Cross` |
| `1470` | `0x3fc5...c0c1` | `SHORT` | 1,479,420.41 USD | `1,148.44` | `1264.34` | `1286.70` | `2721.33` | -27,406.63 USD | `-1.85%` | `10X Cross` |
| `1512` | `0x5f94...4b96` | `LONG` | 1,435,897.30 USD | `1,115.27` | `538.00` | `1286.70` | `0.000000` | 835,879.66 USD | `+58.21%` | `10X Cross` |
| `1526` | `0x71df...a23d` | `SHORT` | 1,413,266.70 USD | `1,098.28` | `513.50` | `1286.70` | `2556.12` | -849,296.51 USD | `-60.09%` | `2X Cross` |
| `1556` | `0xbfc7...80b4` | `SHORT` | 1,384,600.00 USD | `1,075.00` | `558.03` | `1286.70` | `2743.06` | -784,721.27 USD | `-56.67%` | `10X Cross` |
| `1628` | `0x123d...3bff` | `SHORT` | 1,300,315.36 USD | `1,009.64` | `491.08` | `1286.70` | `4360.78` | -804,497.45 USD | `-61.87%` | `10X Cross` |
| `1645` | `0xe282...df29` | `LONG` | 1,287,300.00 USD | `1,000.00` | `420.99` | `1286.70` | `808.99` | 866,313.14 USD | `+67.30%` | `10X Cross` |
| `1646` | `0x668c...ea2e` | `SHORT` | 1,287,100.00 USD | `1,000.00` | `1406.98` | `1286.70` | `4195.09` | 119,881.99 USD | `+9.31%` | `10X Cross` |
| `1671` | `0x17f0...094f` | `LONG` | 1,262,660.04 USD | `984.30` | `1287.23` | `1286.70` | `536.92` | -4,360.12 USD | `-0.35%` | `5X Cross` |
| `1680` | `0x51f6...2b39` | `SHORT` | 1,257,474.40 USD | `976.30` | `1299.77` | `1286.70` | `2514.51` | 11,489.50 USD | `+0.91%` | `10X Cross` |
| `1742` | `0x757d...94ba` | `LONG` | 1,191,400.00 USD | `925.00` | `1558.31` | `1286.70` | `0.000000` | -250,040.58 USD | `-20.99%` | `10X Cross` |
| `1743` | `0xaa82...9556` | `LONG` | 1,190,279.44 USD | `924.13` | `1254.72` | `1286.70` | `181.95` | 30,752.76 USD | `+2.58%` | `10X Cross` |
| `1793` | `0xb911...5525` | `LONG` | 1,159,380.00 USD | `900.00` | `1294.82` | `1286.70` | `1035.36` | -5,957.82 USD | `-0.51%` | `10X Cross` |
| `1836` | `0xcf0a...856f` | `LONG` | 1,121,257.17 USD | `871.15` | `1292.19` | `1286.70` | `1005.24` | -4,437.68 USD | `-0.40%` | `4X Cross` |
| `1848` | `0xef96...9383` | `SHORT` | 1,118,524.96 USD | `868.42` | `1259.08` | `1286.70` | `5384.61` | -25,113.17 USD | `-2.25%` | `10X Cross` |
| `1866` | `0xdf95...7d72` | `SHORT` | 1,098,755.78 USD | `853.27` | `1074.39` | `1286.70` | `44530.52` | -182,008.34 USD | `-16.56%` | `10X Cross` |
| `1874` | `0xdf83...3cff` | `SHORT` | 1,091,472.77 USD | `847.68` | `1256.66` | `1286.70` | `1921.06` | -26,223.03 USD | `-2.40%` | `10X Cross` |
| `1919` | `0xae55...2236` | `LONG` | 1,052,574.37 USD | `817.47` | `1467.80` | `1286.70` | `0.000000` | -147,306.85 USD | `-13.99%` | `10X Cross` |
| `1920` | `0x601c...4f54` | `SHORT` | 1,052,454.57 USD | `824.42` | `615.11` | `1286.70` | `3088.89` | -545,341.82 USD | `-51.82%` | `5X Cross` |
| `1964` | `0x9b0f...db40` | `LONG` | 1,029,680.00 USD | `800.00` | `1268.86` | `1286.70` | `794.15` | 14,590.24 USD | `+1.42%` | `10X Cross` |
| `1965` | `0x11ee...1d1d` | `SHORT` | 1,029,680.00 USD | `800.00` | `1269.65` | `1286.70` | `1600.61` | -13,956.99 USD | `-1.36%` | `5X Cross` |
| `1966` | `0x0f02...5384` | `LONG` | 1,029,642.92 USD | `800.78` | `1290.36` | `1286.70` | `301.92` | -3,651.14 USD | `-0.35%` | `3X Cross` |
| `1975` | `0x6e8f...4364` | `LONG` | 1,021,665.65 USD | `793.65` | `1260.00` | `1286.70` | `964.64` | 21,666.65 USD | `+2.12%` | `10X Cross` |
| `1976` | `0xabdb...84ac` | `LONG` | 1,021,558.40 USD | `793.69` | `711.79` | `1286.70` | `664.49` | 456,618.04 USD | `+44.70%` | `3X Cross` |

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
  * Current Rate: `85.52K` | Last 24h: `134.73K` | Last 3d: `246.48K` | Last 7d: `772.71K`
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
| `5m` | 334,580.00 USD | 135,830.00 USD | **`ACCUMULATION`** |
| `15m` | 1,080,000.00 USD | -642,440.00 USD | **`ACCUMULATION`** |
| `30m` | 796,730.00 USD | -4,200,000.00 USD | **`DISTRIBUTION`** |
| `1h` | -21,870.00 USD | -39,260.00 USD | **`DISTRIBUTION`** |
| `2h` | -944,600.00 USD | 262,850.00 USD | **`DISTRIBUTION`** |
| `4h` | 10,180,000.00 USD | 28,370,000.00 USD | **`ACCUMULATION`** |
| `6h` | 816,320.00 USD | 9,120,000.00 USD | **`ACCUMULATION`** |
| `8h` | -7,300,000.00 USD | 6,110,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -5,030,000.00 USD | -13,390,000.00 USD | **`DISTRIBUTION`** |
| `24h` | 18,710,000.00 USD | 120,240,000.00 USD | **`ACCUMULATION`** |
| `1w` | 40,100,000.00 USD | 239,150,000.00 USD | **`ACCUMULATION`** |
| `30d` | 62,740,000.00 USD | -520,130,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+334.58K` | 15m=`+1.08M` | 1h=`-21.87K` | 24h=`+18.71M`
* Futures Capital Netflows: 5m=`+135.83K` | 15m=`-642.44K` | 1h=`-39.26K` | 24h=`+120.24M`
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
