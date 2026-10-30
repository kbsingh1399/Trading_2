# 🏛️ SOVEREIGN CANDIDATE DOSSIER: ZECUSD
**Canonical Key**: `ZECUSD` | **Broker Instrument**: `ZECUSD.p` | **Asset Class**: `Crypto Altcoin`
**Timestamp**: `2026-10-30 09:28:14 IST` (`2026-10-30 03:58:14 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `1282.88` | **Live Ask Quote**: `1284.35` | **Mid Price**: `1283.62`
- **Spread Points**: `147.00` | **Spread BPS**: `11.45 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `1283.62` | VWAP Z-Score: `+0.00` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `3.21` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `50.00` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `1292.60` | Lower -3.00σ Band: `1274.63`
  * Upper +2.51σ Band: `1290.67` | Lower -2.51σ Band: `1276.56`
  * Upper +2.01σ Band: `1289.01` | Lower -2.01σ Band: `1278.22`
  * Upper +2.00σ Band: `1288.75` | Lower -2.00σ Band: `1278.48`
  * Upper +1.28σ Band: `1287.21` | Lower -1.28σ Band: `1280.02`
  * Upper +1.00σ Band: `1286.18` | Lower -1.00σ Band: `1281.05`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`1283.62` | EMA-20=`1283.62` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`1283.62` (Slope: `+0.0000`) | EMA-100=`1283.62`
  * Institutional Anchors: EMA-144=`1283.62` | EMA-200=`1283.62` (Slope: `+0.0000`) | EMA-233=`1283.62`
- **Range Boundaries**: 24H High=`1296.45` | 24H Low=`1270.78` | Weekly High=`1309.29` | Weekly Low=`1257.94`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `1265.46` (Distance: `+1.48%`)
  * Point of Control (POC) = `1229.90` (Distance: `+4.42%`)
  * Value Area Low (VAL) = `1222.17` (Distance: `+5.08%`)
  * Auction Positioning: `ABOVE_VALUE (Imbalance)` | Session Bias: **`BULLISH (Above Pivot)`** | Market Regime: `RANGE_EXPANSION`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`1309.91` | POC=`1246.71` | VAL=`1230.27`
  * Prior Day Extremes: PDH=`1396.49` | PDL=`1206.89` | PDC=`1244.38`
  * Monday Range Blueprint: High=`1267.53` | Mid=`1222.14` | Low=`1176.75`
  * Developing Weekly Value Area: Weekly VAH=`1296.14` | Weekly POC=`1239.01` | Weekly VAL=`1200.92`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`1296.00` | Low=`1180.03`
  * London Session (08:00-16:00 UTC): High=`1288.75` | Low=`1278.48`
  * New York Session (13:00-21:00 UTC): High=`1291.32` | Low=`1275.91`
  * Initial Balance (First Hour): IB High=`1287.47` | IB Low=`1279.76`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `1278.48` - `1288.75`
  * Optimal Trade Entry (OTE 0.705): `1286.18`
  * Structural Invalidation Anchor (0.786): `1293.88`

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
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 09:20:12 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `13` | `0xb83d...6e36` | `SHORT` | 67,090,071.43 USD | `52,385.47` | `1336.45` | `1280.30` | `3723.29` | 2,920,495.97 USD | `+4.35%` | `3X Cross` |
| `22` | `0x5b5d...c060` | `SHORT` | 51,487,766.95 USD | `40,121.38` | `1478.36` | `1280.30` | `5169.02` | 7,826,268.16 USD | `+15.20%` | `3X Cross` |
| `39` | `0x7fda...17d1` | `SHORT` | 32,095,800.87 USD | `25,055.27` | `1261.85` | `1280.30` | `2681.87` | -479,688.70 USD | `-1.49%` | `5X Cross` |
| `80` | `0x60b0...991e` | `LONG` | 21,514,982.63 USD | `16,779.74` | `1179.65` | `1280.30` | `930.57` | 1,720,735.61 USD | `+8.00%` | `10X Cross` |
| `135` | `0xc36a...105b` | `LONG` | 14,790,252.62 USD | `11,510.82` | `1215.14` | `1280.30` | `966.71` | 802,971.59 USD | `+5.43%` | `10X Cross` |
| `151` | `0x9071...5c0b` | `LONG` | 13,474,751.95 USD | `10,517.29` | `1353.83` | `1280.30` | `0.1126` | -763,866.92 USD | `-5.67%` | `1X Cross` |
| `169` | `0x8742...8427` | `LONG` | 11,788,590.25 USD | `9,201.21` | `1286.37` | `1280.30` | `705.96` | -47,579.74 USD | `-0.40%` | `10X Cross` |
| `188` | `0x58b2...11f3` | `LONG` | 10,968,449.17 USD | `8,563.08` | `1246.56` | `1280.30` | `382.48` | 294,031.60 USD | `+2.68%` | `10X Cross` |
| `194` | `0xad59...ba81` | `SHORT` | 10,789,897.50 USD | `8,425.00` | `330.91` | `1280.30` | `2144.42` | -8,001,939.73 USD | `-74.16%` | `10X Cross` |
| `195` | `0x9ffd...ce40` | `LONG` | 10,717,508.05 USD | `8,367.17` | `1251.01` | `1280.30` | `594.62` | 250,107.09 USD | `+2.33%` | `5X Cross` |
| `200` | `0xdd53...2b13` | `SHORT` | 10,501,432.30 USD | `8,195.92` | `741.54` | `1280.30` | `8633.08` | -4,423,835.93 USD | `-42.13%` | `3X Cross` |
| `217` | `0x880a...311c` | `SHORT` | 9,885,139.29 USD | `7,707.11` | `1367.50` | `1280.30` | `2239.93` | 654,344.92 USD | `+6.62%` | `10X Cross` |
| `230` | `0xbf73...5d58` | `LONG` | 9,624,750.00 USD | `7,500.00` | `1248.78` | `1280.30` | `120.55` | 258,904.38 USD | `+2.69%` | `10X Cross` |
| `264` | `0x2b61...2f6c` | `LONG` | 8,746,314.30 USD | `6,807.00` | `1453.56` | `1280.30` | `559.56` | -1,148,036.92 USD | `-13.13%` | `10X Cross` |
| `281` | `0x2ae5...83e7` | `LONG` | 8,246,828.16 USD | `6,436.80` | `1391.82` | `1280.30` | `0.000000` | -712,063.83 USD | `-8.63%` | `1X Cross` |
| `330` | `0x26b6...9a13` | `LONG` | 6,958,978.01 USD | `5,433.73` | `1282.23` | `1280.30` | `223.71` | -8,325.22 USD | `-0.12%` | `10X Cross` |
| `338` | `0x45d2...4029` | `SHORT` | 6,696,832.40 USD | `5,227.00` | `833.44` | `1280.30` | `9010.42` | -2,340,454.43 USD | `-34.95%` | `5X Cross` |
| `358` | `0xea00...a918` | `LONG` | 6,411,000.00 USD | `5,000.00` | `739.16` | `1280.30` | `0.000000` | 2,715,184.89 USD | `+42.35%` | `5X Cross` |
| `359` | `0xecb6...2b00` | `SHORT` | 6,370,069.41 USD | `4,973.12` | `1278.99` | `1280.30` | `6605.31` | -9,510.05 USD | `-0.15%` | `5X Cross` |
| `372` | `0xdd7a...8830` | `LONG` | 6,224,445.33 USD | `4,860.19` | `897.48` | `1280.30` | `784.01` | 1,862,541.66 USD | `+29.92%` | `10X Cross` |
| `399` | `0x4cae...7c34` | `LONG` | 5,527,986.72 USD | `4,302.27` | `1169.72` | `1280.30` | `1008.96` | 495,520.32 USD | `+8.96%` | `10X Cross` |
| `415` | `0x469e...58a5` | `SHORT` | 5,338,048.99 USD | `4,163.52` | `1242.31` | `1280.30` | `1971.89` | -165,664.34 USD | `-3.10%` | `10X Cross` |
| `439` | `0xa61c...66b9` | `LONG` | 4,979,750.40 USD | `3,888.00` | `1148.34` | `1280.30` | `0.000000` | 515,008.26 USD | `+10.34%` | `10X Cross` |
| `461` | `0x9aa5...58af` | `SHORT` | 4,765,717.11 USD | `3,720.31` | `1205.51` | `1280.30` | `3691.37` | -280,830.31 USD | `-5.89%` | `10X Cross` |
| `466` | `0x0153...8052` | `SHORT` | 4,735,889.31 USD | `3,698.18` | `1307.82` | `1280.30` | `2504.82` | 100,681.44 USD | `+2.13%` | `1X Isolated` |
| `523` | `0x382b...3e39` | `LONG` | 4,232,103.75 USD | `3,303.75` | `1215.08` | `1280.30` | `0.000000` | 217,784.36 USD | `+5.15%` | `10X Cross` |
| `532` | `0xd4c1...3d1d` | `SHORT` | 4,191,649.77 USD | `3,272.17` | `1294.25` | `1280.30` | `2567.63` | 43,348.35 USD | `+1.03%` | `10X Cross` |
| `535` | `0xd21d...90f1` | `LONG` | 4,162,275.00 USD | `3,250.00` | `1253.64` | `1280.30` | `876.03` | 87,933.27 USD | `+2.11%` | `4X Isolated` |
| `540` | `0x456f...cdf1` | `LONG` | 4,133,248.98 USD | `3,226.58` | `1267.75` | `1280.30` | `516.68` | 42,762.36 USD | `+1.03%` | `10X Cross` |
| `550` | `0x1338...c48e` | `LONG` | 4,032,215.23 USD | `3,149.43` | `1018.52` | `1280.30` | `820.32` | 824,469.69 USD | `+20.45%` | `4X Isolated` |
| `563` | `0x325e...9564` | `LONG` | 3,972,926.33 USD | `3,101.91` | `1298.07` | `1280.30` | `165.77` | -53,584.37 USD | `-1.35%` | `10X Cross` |
| `565` | `0xdbe0...d6d5` | `LONG` | 3,965,934.60 USD | `3,085.37` | `422.97` | `1280.30` | `338.64` | 2,660,930.11 USD | `+67.09%` | `3X Isolated` |
| `589` | `0x9c06...0560` | `SHORT` | 3,840,697.08 USD | `2,989.80` | `786.00` | `1280.30` | `2586.87` | -1,490,702.08 USD | `-38.81%` | `10X Cross` |
| `593` | `0x27c9...d65d` | `SHORT` | 3,794,168.28 USD | `2,961.88` | `1254.41` | `1280.30` | `1723.70` | -78,753.08 USD | `-2.08%` | `10X Cross` |
| `594` | `0x2e30...4cb5` | `SHORT` | 3,792,011.82 USD | `2,960.89` | `1287.96` | `1280.30` | `2898.01` | 21,496.00 USD | `+0.57%` | `2X Cross` |
| `659` | `0x5323...b23c` | `SHORT` | 3,386,964.00 USD | `2,644.00` | `1262.62` | `1280.30` | `3301.93` | -48,605.77 USD | `-1.44%` | `5X Cross` |
| `685` | `0xa183...0482` | `LONG` | 3,247,321.00 USD | `2,534.00` | `530.25` | `1280.30` | `444.56` | 1,903,658.28 USD | `+58.62%` | `5X Isolated` |
| `688` | `0xac48...3201` | `LONG` | 3,242,851.50 USD | `2,531.50` | `1378.58` | `1280.30` | `527.47` | -247,020.78 USD | `-7.62%` | `10X Cross` |
| `698` | `0x0871...e927` | `LONG` | 3,201,750.00 USD | `2,500.00` | `1276.50` | `1280.30` | `0.000000` | 10,500.00 USD | `+0.33%` | `10X Cross` |
| `709` | `0x9b86...6e6e` | `LONG` | 3,154,748.31 USD | `2,463.30` | `637.58` | `1280.30` | `882.49` | 1,584,199.03 USD | `+50.22%` | `3X Cross` |
| `715` | `0x71d0...8c26` | `SHORT` | 3,147,263.28 USD | `2,456.88` | `1263.62` | `1280.30` | `3733.00` | -42,698.62 USD | `-1.36%` | `10X Cross` |
| `770` | `0xb2f7...af9f` | `SHORT` | 2,963,181.20 USD | `2,313.72` | `746.63` | `1280.30` | `4472.48` | -1,235,692.46 USD | `-41.70%` | `10X Cross` |
| `785` | `0x413c...886c` | `LONG` | 2,881,575.00 USD | `2,250.00` | `1237.51` | `1280.30` | `0.000000` | 97,173.97 USD | `+3.37%` | `10X Cross` |
| `790` | `0xb122...e4ba` | `LONG` | 2,873,596.68 USD | `2,243.42` | `1258.05` | `1280.30` | `983.00` | 51,262.75 USD | `+1.78%` | `10X Cross` |
| `802` | `0xf48f...10fe` | `LONG` | 2,841,220.14 USD | `2,218.49` | `1517.87` | `1280.30` | `981.49` | -526,166.68 USD | `-18.52%` | `3X Cross` |
| `829` | `0x5bc4...3b0c` | `SHORT` | 2,730,543.31 USD | `2,130.74` | `1089.65` | `1280.30` | `3695.26` | -408,785.73 USD | `-14.97%` | `5X Cross` |
| `850` | `0x8de4...b9aa` | `SHORT` | 2,678,733.36 USD | `2,091.29` | `1331.35` | `1280.30` | `1689.94` | 105,506.35 USD | `+3.94%` | `3X Cross` |
| `859` | `0x4fe2...ac59` | `SHORT` | 2,653,681.17 USD | `2,071.57` | `1478.56` | `1280.30` | `1832.59` | 409,265.04 USD | `+15.42%` | `10X Cross` |
| `868` | `0xdf57...93f5` | `LONG` | 2,632,649.52 USD | `2,054.35` | `1227.36` | `1280.30` | `897.27` | 111,227.48 USD | `+4.22%` | `4X Isolated` |
| `874` | `0xbcd4...0dd2` | `LONG` | 2,604,841.34 USD | `2,033.92` | `1228.20` | `1280.30` | `734.13` | 106,790.53 USD | `+4.10%` | `10X Cross` |
| `885` | `0xf29c...9971` | `LONG` | 2,563,000.00 USD | `2,000.00` | `1254.95` | `1280.30` | `0.000000` | 53,102.93 USD | `+2.07%` | `10X Cross` |
| `886` | `0x9a99...d21a` | `LONG` | 2,561,800.00 USD | `2,000.00` | `1278.44` | `1280.30` | `0.000000` | 4,926.33 USD | `+0.19%` | `10X Cross` |
| `907` | `0x77ee...2902` | `SHORT` | 2,492,280.62 USD | `1,946.03` | `759.84` | `1280.30` | `5433.15` | -1,013,603.11 USD | `-40.67%` | `10X Cross` |
| `915` | `0x3e2f...b269` | `SHORT` | 2,467,541.06 USD | `1,925.51` | `1134.87` | `1280.30` | `2931.87` | -282,342.21 USD | `-11.44%` | `10X Cross` |
| `931` | `0x4f12...618b` | `SHORT` | 2,431,979.10 USD | `1,896.28` | `1608.30` | `1280.30` | `2116.83` | 617,805.29 USD | `+25.40%` | `3X Cross` |
| `973` | `0x866d...d6e1` | `LONG` | 2,307,885.44 USD | `1,802.05` | `674.73` | `1280.30` | `253.75` | 1,091,984.12 USD | `+47.32%` | `10X Cross` |
| `988` | `0x2309...a2d9` | `LONG` | 2,241,348.79 USD | `1,750.37` | `1186.09` | `1280.30` | `814.41` | 165,254.67 USD | `+7.37%` | `8X Cross` |
| `1032` | `0x265e...7f70` | `LONG` | 2,115,713.77 USD | `1,651.74` | `1382.98` | `1280.30` | `0.000000` | -168,608.99 USD | `-7.97%` | `3X Cross` |
| `1037` | `0xfe7c...b7ae` | `SHORT` | 2,104,221.84 USD | `1,642.64` | `1346.92` | `1280.30` | `5714.15` | 108,286.78 USD | `+5.15%` | `10X Cross` |
| `1041` | `0x3e47...aaf6` | `LONG` | 2,095,583.80 USD | `1,636.28` | `1278.38` | `1280.30` | `1047.26` | 3,792.01 USD | `+0.18%` | `10X Cross` |
| `1043` | `0x2edd...8179` | `SHORT` | 2,092,686.31 USD | `1,633.89` | `1261.58` | `1280.30` | `2898.62` | -31,404.39 USD | `-1.50%` | `10X Cross` |
| `1053` | `0x7f75...9edf` | `LONG` | 2,068,094.94 USD | `1,611.67` | `1200.24` | `1280.30` | `982.85` | 133,710.96 USD | `+6.47%` | `10X Cross` |
| `1065` | `0x6646...6de5` | `SHORT` | 2,049,440.00 USD | `1,600.00` | `660.64` | `1280.30` | `4250.78` | -992,415.03 USD | `-48.42%` | `10X Cross` |
| `1070` | `0x023a...2355` | `SHORT` | 2,042,747.92 USD | `1,594.90` | `1310.00` | `1280.30` | `4437.44` | 46,564.22 USD | `+2.28%` | `10X Cross` |
| `1082` | `0x3205...40bb` | `SHORT` | 2,025,026.30 USD | `1,580.20` | `1250.12` | `1280.30` | `2172.18` | -49,592.56 USD | `-2.45%` | `10X Cross` |
| `1096` | `0xab59...59b5` | `LONG` | 2,004,705.32 USD | `1,565.32` | `1342.15` | `1280.30` | `834.16` | -96,189.89 USD | `-4.80%` | `10X Cross` |
| `1153` | `0xcf67...eb24` | `LONG` | 1,921,350.00 USD | `1,500.00` | `887.05` | `1280.30` | `659.91` | 590,778.63 USD | `+30.75%` | `10X Cross` |
| `1170` | `0xb695...a92d` | `LONG` | 1,899,278.10 USD | `1,483.00` | `1249.80` | `1280.30` | `0.000000` | 45,819.25 USD | `+2.41%` | `10X Cross` |
| `1173` | `0x7277...0b98` | `SHORT` | 1,891,148.00 USD | `1,475.73` | `1287.86` | `1280.30` | `2165.56` | 9,384.13 USD | `+0.50%` | `10X Cross` |
| `1233` | `0x2ab7...c2f8` | `LONG` | 1,793,633.16 USD | `1,400.51` | `813.26` | `1280.30` | `790.52` | 654,651.47 USD | `+36.50%` | `3X Cross` |
| `1255` | `0x11be...8b1d` | `LONG` | 1,762,438.23 USD | `1,375.83` | `1206.55` | `1280.30` | `1134.54` | 102,430.27 USD | `+5.81%` | `10X Isolated` |
| `1283` | `0xfc27...9d9d` | `SHORT` | 1,695,160.11 USD | `1,323.31` | `1298.46` | `1280.30` | `14887.10` | 23,106.58 USD | `+1.36%` | `10X Cross` |
| `1324` | `0x039c...0ebd` | `SHORT` | 1,639,027.05 USD | `1,279.79` | `1239.81` | `1280.30` | `3664.40` | -52,325.22 USD | `-3.19%` | `10X Cross` |
| `1339` | `0xe065...0f85` | `SHORT` | 1,617,277.15 USD | `1,262.61` | `1087.02` | `1280.30` | `1597.60` | -244,801.02 USD | `-15.14%` | `10X Cross` |
| `1414` | `0x266b...efcb` | `LONG` | 1,542,480.00 USD | `1,200.00` | `893.76` | `1280.30` | `387.61` | 469,970.30 USD | `+30.47%` | `10X Cross` |
| `1419` | `0x5975...9abd` | `LONG` | 1,538,011.68 USD | `1,200.00` | `1179.54` | `1280.30` | `491.22` | 122,568.89 USD | `+7.97%` | `5X Cross` |
| `1425` | `0x2847...d47b` | `LONG` | 1,525,661.85 USD | `1,186.27` | `1232.07` | `1280.30` | `0.000000` | 64,093.35 USD | `+4.20%` | `5X Cross` |
| `1453` | `0x69cc...14fd` | `SHORT` | 1,488,050.57 USD | `1,161.36` | `675.33` | `1280.30` | `7998.47` | -703,745.04 USD | `-47.29%` | `10X Cross` |
| `1468` | `0x3fc5...c0c1` | `SHORT` | 1,471,151.64 USD | `1,148.44` | `1264.34` | `1280.30` | `2749.49` | -19,137.86 USD | `-1.30%` | `10X Cross` |
| `1500` | `0xe35c...a1d3` | `LONG` | 1,443,538.45 USD | `1,127.06` | `1318.20` | `1280.30` | `694.46` | -42,156.90 USD | `-2.92%` | `2X Isolated` |
| `1512` | `0x5f94...4b96` | `LONG` | 1,428,326.29 USD | `1,115.27` | `538.00` | `1280.30` | `0.000000` | 828,308.65 USD | `+57.99%` | `10X Cross` |
| `1529` | `0x71df...a23d` | `SHORT` | 1,408,104.79 USD | `1,098.28` | `513.50` | `1280.30` | `2556.89` | -844,134.60 USD | `-59.95%` | `2X Cross` |
| `1563` | `0xbfc7...80b4` | `SHORT` | 1,376,537.50 USD | `1,075.00` | `558.03` | `1280.30` | `2802.22` | -776,658.77 USD | `-56.42%` | `10X Cross` |
| `1582` | `0x38f9...cb04` | `SHORT` | 1,348,999.73 USD | `1,053.33` | `1245.93` | `1280.30` | `2064.19` | -36,623.06 USD | `-2.71%` | `10X Cross` |
| `1638` | `0x123d...3bff` | `SHORT` | 1,293,348.84 USD | `1,009.64` | `491.08` | `1280.30` | `4389.28` | -797,530.93 USD | `-61.66%` | `10X Cross` |
| `1649` | `0xe282...df29` | `LONG` | 1,280,700.00 USD | `1,000.00` | `420.99` | `1280.30` | `812.22` | 859,713.14 USD | `+67.13%` | `10X Cross` |
| `1650` | `0x668c...ea2e` | `SHORT` | 1,280,500.00 USD | `1,000.00` | `1406.98` | `1280.30` | `4192.50` | 126,481.99 USD | `+9.88%` | `10X Cross` |
| `1668` | `0x17f0...094f` | `LONG` | 1,264,727.07 USD | `984.30` | `1287.23` | `1280.30` | `536.89` | -2,293.09 USD | `-0.18%` | `5X Cross` |
| `1684` | `0x51f6...2b39` | `SHORT` | 1,250,835.56 USD | `976.30` | `1299.77` | `1280.30` | `2528.97` | 18,128.34 USD | `+1.45%` | `10X Cross` |
| `1747` | `0x757d...94ba` | `LONG` | 1,185,387.50 USD | `925.00` | `1558.31` | `1280.30` | `0.000000` | -256,053.08 USD | `-21.60%` | `10X Cross` |
| `1750` | `0xaa82...9556` | `LONG` | 1,184,087.77 USD | `924.13` | `1254.72` | `1280.30` | `181.78` | 24,561.09 USD | `+2.07%` | `10X Cross` |
| `1793` | `0xb911...5525` | `LONG` | 1,152,900.00 USD | `900.00` | `1294.82` | `1280.30` | `1035.32` | -12,437.82 USD | `-1.08%` | `10X Cross` |
| `1846` | `0xcf0a...856f` | `LONG` | 1,115,507.57 USD | `871.15` | `1292.19` | `1280.30` | `1008.98` | -10,187.27 USD | `-0.91%` | `4X Cross` |
| `1849` | `0xef96...9383` | `SHORT` | 1,114,356.54 USD | `868.42` | `1259.08` | `1280.30` | `5400.92` | -20,944.75 USD | `-1.88%` | `10X Cross` |
| `1855` | `0x2577...4897` | `SHORT` | 1,111,865.32 USD | `868.17` | `1266.36` | `1280.30` | `4985.01` | -12,453.45 USD | `-1.12%` | `10X Cross` |
| `1873` | `0xdf95...7d72` | `SHORT` | 1,092,612.24 USD | `853.27` | `1074.39` | `1280.30` | `44891.77` | -175,864.79 USD | `-16.10%` | `10X Cross` |
| `1898` | `0xdf83...3cff` | `SHORT` | 1,063,345.29 USD | `830.09` | `1255.81` | `1280.30` | `1915.13` | -20,907.12 USD | `-1.97%` | `10X Cross` |
| `1909` | `0x601c...4f54` | `SHORT` | 1,055,504.93 USD | `824.42` | `615.11` | `1280.30` | `3089.09` | -548,392.17 USD | `-51.96%` | `5X Cross` |
| `1922` | `0xae55...2236` | `LONG` | 1,047,342.56 USD | `817.47` | `1467.80` | `1280.30` | `0.000000` | -152,538.65 USD | `-14.56%` | `10X Cross` |
| `1959` | `0x9b0f...db40` | `LONG` | 1,028,440.00 USD | `800.00` | `1268.86` | `1280.30` | `795.71` | 13,350.24 USD | `+1.30%` | `10X Cross` |
| `1961` | `0x0f02...5384` | `LONG` | 1,026,039.41 USD | `800.78` | `1290.36` | `1280.30` | `299.11` | -7,254.65 USD | `-0.71%` | `3X Cross` |
| `1962` | `0x11ee...1d1d` | `SHORT` | 1,024,400.00 USD | `800.00` | `1269.65` | `1280.30` | `1595.39` | -8,676.99 USD | `-0.85%` | `5X Cross` |
| `1975` | `0xabdb...84ac` | `LONG` | 1,017,589.95 USD | `793.69` | `711.79` | `1280.30` | `664.46` | 452,649.59 USD | `+44.48%` | `3X Cross` |
| `1979` | `0x6e8f...4364` | `LONG` | 1,016,427.56 USD | `793.65` | `1260.00` | `1280.30` | `981.84` | 16,428.56 USD | `+1.62%` | `10X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| Intel | Baseline | - | - | - | Neutral | - | No anomalous telegram alerts in current window | - |


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
| `5m` | `BALANCED` | 0.00 USD | 1,750.00 USD | 1,750.00 USD | 1,750.00 USD | `1` | `2026-10-30 03:50:00 UTC - 2026-10-30 03:55:00 UTC` |
| `15m` | `BALANCED` | 0.00 USD | 1,750.00 USD | 1,750.00 USD | 1,750.00 USD | `1` | `2026-10-30 03:45:00 UTC - 2026-10-30 04:00:00 UTC` |
| `1h` | `BALANCED` | 0.00 USD | 1,750.00 USD | 1,750.00 USD | 1,750.00 USD | `1` | `2026-10-30 03:00:00 UTC - 2026-10-30 04:00:00 UTC` |
| `4h` | `BALANCED` | 0.00 USD | 1,750.00 USD | 1,750.00 USD | 1,750.00 USD | `1` | `2026-10-30 00:00:00 UTC - 2026-10-30 04:00:00 UTC` |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `0 USD` | Total OI Tokens: `-`
  * 1h OI Change: `0.00%` | 4h OI Change: `0.00%` | 24h OI Change: `0.00%`
  * Exchange Breakdown: Binance=`-` | Bybit=`-` | OKX=`-` | Hyperliquid=`-`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `85.31K` | Last 24h: `133.88K` | Last 3d: `245.74K` | Last 7d: `771.70K`
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
| `0:00 UTC` | `1245.15` | `1232.68` | `1245.15` | `1249.05` | `1206.75` | 51,931,159.61 USD | 26,761,787.01 USD | 25,169,372.61 USD | 1,592,414.40 USD | `+3.07%` | `20B / 9S` |
| `5:00 UTC` | `1236.45` | `1237.15` | `1236.45` | `1245.15` | `1230.45` | 21,904,768.45 USD | 9,625,705.12 USD | 12,279,063.33 USD | -2,653,358.20 USD | `-12.11%` | `1B / 0S` |
| `0:00 UTC` | `1228.65` | `1236.25` | `1228.65` | `1253.25` | `1219.35` | 45,146,863.08 USD | 23,450,812.50 USD | 21,696,050.59 USD | 1,754,761.91 USD | `+3.89%` | `18B / 9S` |
| `5:00 UTC` | `1254.75` | `1256.85` | `1254.75` | `1263.45` | `1247.85` | 37,496,922.68 USD | 20,689,312.95 USD | 16,807,609.72 USD | 3,881,703.23 USD | `+10.35%` | `5B / 3S` |
| `0:00 UTC` | `1263.45` | `1263.47` | `1263.45` | `1267.65` | `1258.35` | 21,490,941.27 USD | 11,626,504.00 USD | 9,864,437.27 USD | 1,762,066.74 USD | `+8.20%` | `2B / 3S` |
| `5:00 UTC` | `1257.45` | `1259.53` | `1257.45` | `1270.05` | `1249.95` | 34,915,865.69 USD | 14,880,758.20 USD | 20,035,107.50 USD | -5,154,349.30 USD | `-14.76%` | `1B / 7S` |
| `0:00 UTC` | `1260.15` | `1262.58` | `1260.15` | `1267.95` | `1257.15` | 13,992,732.07 USD | 6,287,729.60 USD | 7,705,002.47 USD | -1,417,272.88 USD | `-10.13%` | `0B / 2S` |
| `5:00 UTC` | `1265.55` | `1265.89` | `1265.55` | `1274.25` | `1259.25` | 13,172,642.30 USD | 7,854,309.17 USD | 5,318,333.13 USD | 2,535,976.04 USD | `+19.25%` | `13B / 1S` |
| `0:00 UTC` | `1282.05` | `1279.57` | `1282.05` | `1285.35` | `1269.15` | 31,465,166.07 USD | 16,761,441.58 USD | 14,703,724.48 USD | 2,057,717.10 USD | `+6.54%` | `8B / 5S` |
| `5:00 UTC` | `1279.95` | `1283.06` | `1279.95` | `1287.45` | `1279.65` | 7,064,986.96 USD | 2,493,374.27 USD | 4,571,612.69 USD | -2,078,238.41 USD | `-29.42%` | `1B / 9S` |

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
| `5m` | -34,560.00 USD | -1,440,000.00 USD | **`DISTRIBUTION`** |
| `15m` | -633,680.00 USD | 2,740,000.00 USD | **`ACCUMULATION`** |
| `30m` | 134,620.00 USD | 6,340,000.00 USD | **`ACCUMULATION`** |
| `1h` | -699,510.00 USD | -697,480.00 USD | **`DISTRIBUTION`** |
| `2h` | 7,730,000.00 USD | 7,680,000.00 USD | **`ACCUMULATION`** |
| `4h` | -1,310,000.00 USD | 31,640,000.00 USD | **`ACCUMULATION`** |
| `6h` | 1,500,000.00 USD | 15,730,000.00 USD | **`ACCUMULATION`** |
| `8h` | -10,610,000.00 USD | 9,830,000.00 USD | **`DISTRIBUTION`** |
| `12h` | 2,240,000.00 USD | 36,880,000.00 USD | **`ACCUMULATION`** |
| `24h` | 18,450,000.00 USD | 130,290,000.00 USD | **`ACCUMULATION`** |
| `1w` | 37,250,000.00 USD | 238,970,000.00 USD | **`ACCUMULATION`** |
| `30d` | 62,920,000.00 USD | -511,860,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-34.56K` | 15m=`-633.68K` | 1h=`-699.51K` | 24h=`+18.45M`
* Futures Capital Netflows: 5m=`-1.44M` | 15m=`+2.74M` | 1h=`-697.48K` | 24h=`+130.29M`
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
  * `2026-10-30 09:09:58 IST`: [forex.com] - (Sentiment: `Neutral`)
  * `2026-10-30 08:33:58 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 08:32:58 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 09:15:58 IST`: [financemagnates.com] - (Sentiment: `Neutral`)
  * `2026-10-30 09:14:58 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-30 09:14:58 IST`: [kathleenhays.substack.com] - (Sentiment: `Neutral`)
  * `2026-10-30 06:16:58 IST`: [rba.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 06:16:58 IST`: [abs.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 06:16:58 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 06:16:58 IST`: [@NodeWire] - (Sentiment: `Neutral`)
  * `2026-10-30 06:16:58 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 06:16:58 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 05:16:58 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-30 05:16:58 IST`: [media.rabobank.com] - (Sentiment: `Neutral`)
  * `2026-10-30 04:16:58 IST`: [economics.td.com] - (Sentiment: `Neutral`)


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
  * Spread-Padded Stop Loss: `1216.11` (Risk Distance: `6.06` pts)
  * +2.5R Take Profit: `1237.31`
  * Mathematical Lot Sizing: **`1.65 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `1265.46` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `1271.52` (Risk Distance: `6.06` pts)
  * +2.5R Take Profit: `1250.32`
  * Mathematical Lot Sizing: **`1.65 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`1293.88`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
