# 🏛️ SOVEREIGN CANDIDATE DOSSIER: ZECUSD
**Canonical Key**: `ZECUSD` | **Broker Instrument**: `ZECUSD.p` | **Asset Class**: `Crypto Altcoin`
**Timestamp**: `2026-10-30 02:06:25 IST` (`2026-10-29 20:36:25 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `1289.36` | **Live Ask Quote**: `1290.58` | **Mid Price**: `1289.97`
- **Spread Points**: `122.00` | **Spread BPS**: `9.46 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `1282.47` | VWAP Z-Score: `+0.48` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `16.04` (Volatility Regime: `HIGH_EXPANSION`)
  * 14-Period RSI: `42.57` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `1398.33` | Lower -3.00σ Band: `1166.61`
  * Upper +2.51σ Band: `1379.41` | Lower -2.51σ Band: `1185.53`
  * Upper +2.01σ Band: `1360.10` | Lower -2.01σ Band: `1204.84`
  * Upper +2.00σ Band: `1359.71` | Lower -2.00σ Band: `1205.23`
  * Upper +1.28σ Band: `1331.90` | Lower -1.28σ Band: `1233.03`
  * Upper +1.00σ Band: `1321.09` | Lower -1.00σ Band: `1243.85`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`1317.51` | EMA-20=`1319.30` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`1303.75` (Slope: `+0.0000`) | EMA-100=`1292.20`
  * Institutional Anchors: EMA-144=`1286.81` | EMA-200=`1281.83` (Slope: `+0.3905`) | EMA-233=`1279.93`
- **Range Boundaries**: 24H High=`1396.49` | 24H Low=`1230.00` | Weekly High=`1396.49` | Weekly Low=`1210.62`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `1309.36` (Distance: `-1.88%`)
  * Point of Control (POC) = `1247.20` (Distance: `+3.01%`)
  * Value Area Low (VAL) = `1230.55` (Distance: `+4.40%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`1320.44` | POC=`1312.10` | VAL=`1285.78`
  * Prior Day Extremes: PDH=`1328.99` | PDL=`1263.19` | PDC=`1296.46`
  * Monday Range Blueprint: High=`1267.53` | Mid=`1222.14` | Low=`1176.75`
  * Developing Weekly Value Area: Weekly VAH=`1296.14` | Weekly POC=`1239.01` | Weekly VAL=`1195.06`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`1318.68` | Low=`1230.00`
  * London Session (08:00-16:00 UTC): High=`1276.13` | Low=`1233.52`
  * New York Session (13:00-21:00 UTC): High=`1396.49` | Low=`1250.65`
  * Initial Balance (First Hour): IB High=`1255.79` | IB Low=`1245.43`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `1284.81` - `1295.13`
  * Optimal Trade Entry (OTE 0.705): `1292.55`
  * Structural Invalidation Anchor (0.786): `1300.29`

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
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 02:04:34 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `16` | `0xb83d...6e36` | `SHORT` | 68,451,924.54 USD | `52,582.52` | `1336.45` | `1285.60` | `3794.89` | 1,821,990.36 USD | `+2.66%` | `3X Cross` |
| `24` | `0x5b5d...c060` | `SHORT` | 52,279,756.28 USD | `40,727.61` | `1478.36` | `1285.60` | `5258.26` | 7,930,507.91 USD | `+15.17%` | `3X Cross` |
| `41` | `0x7fda...17d1` | `SHORT` | 28,943,125.01 USD | `22,522.08` | `1261.68` | `1285.60` | `2929.01` | -527,506.95 USD | `-1.82%` | `5X Cross` |
| `81` | `0x60b0...991e` | `LONG` | 21,838,831.61 USD | `16,779.74` | `1179.65` | `1285.60` | `899.68` | 2,044,584.60 USD | `+9.36%` | `10X Cross` |
| `89` | `0xbf73...5d58` | `LONG` | 20,542,400.00 USD | `16,000.00` | `1214.30` | `1285.60` | `747.24` | 1,113,567.75 USD | `+5.42%` | `10X Cross` |
| `137` | `0xc36a...105b` | `LONG` | 14,989,389.80 USD | `11,510.82` | `1215.14` | `1285.60` | `939.41` | 1,002,108.78 USD | `+6.69%` | `10X Cross` |
| `173` | `0x8742...8427` | `LONG` | 11,813,433.52 USD | `9,201.21` | `1286.37` | `1285.60` | `698.37` | -22,736.47 USD | `-0.19%` | `10X Cross` |
| `180` | `0x9071...5c0b` | `LONG` | 11,387,090.62 USD | `8,829.94` | `1370.53` | `1285.60` | `579.52` | -714,598.02 USD | `-6.28%` | `2X Cross` |
| `198` | `0xad59...ba81` | `SHORT` | 10,967,272.39 USD | `8,425.00` | `330.91` | `1285.60` | `2142.90` | -8,179,314.62 USD | `-74.58%` | `10X Cross` |
| `204` | `0x9ffd...ce40` | `LONG` | 10,746,806.38 USD | `8,357.42` | `1256.67` | `1285.60` | `591.80` | 244,301.82 USD | `+2.27%` | `5X Cross` |
| `208` | `0xdd53...2b13` | `SHORT` | 10,603,779.47 USD | `8,230.76` | `739.37` | `1285.60` | `8200.37` | -4,518,178.95 USD | `-42.61%` | `3X Cross` |
| `228` | `0xfc66...ca06` | `SHORT` | 9,967,293.80 USD | `7,751.22` | `1319.67` | `1285.60` | `5635.50` | 261,752.64 USD | `+2.63%` | `10X Cross` |
| `229` | `0x880a...311c` | `SHORT` | 9,964,522.52 USD | `7,707.11` | `1367.50` | `1285.60` | `2299.17` | 574,961.68 USD | `+5.77%` | `10X Cross` |
| `274` | `0x2b61...2f6c` | `LONG` | 8,864,075.40 USD | `6,807.00` | `1453.56` | `1285.60` | `621.05` | -1,030,275.82 USD | `-11.62%` | `10X Cross` |
| `292` | `0x2ae5...83e7` | `LONG` | 8,264,207.52 USD | `6,436.80` | `1391.82` | `1285.60` | `482.34` | -694,684.47 USD | `-8.41%` | `2X Cross` |
| `335` | `0x26b6...9a13` | `LONG` | 6,982,886.42 USD | `5,433.73` | `1282.23` | `1285.60` | `213.52` | 15,583.19 USD | `+0.22%` | `10X Cross` |
| `344` | `0xecb6...2b00` | `SHORT` | 6,787,385.21 USD | `5,293.34` | `1323.94` | `1285.60` | `6579.43` | 220,678.50 USD | `+3.25%` | `5X Cross` |
| `347` | `0x45d2...4029` | `SHORT` | 6,710,945.30 USD | `5,227.00` | `833.44` | `1285.60` | `8594.22` | -2,354,567.33 USD | `-35.09%` | `5X Cross` |
| `369` | `0xea00...a918` | `LONG` | 6,508,000.00 USD | `5,000.00` | `739.16` | `1285.60` | `0.000000` | 2,812,184.89 USD | `+43.21%` | `5X Cross` |
| `383` | `0xdd7a...8830` | `LONG` | 6,292,974.01 USD | `4,860.19` | `897.48` | `1285.60` | `789.29` | 1,931,070.34 USD | `+30.69%` | `10X Cross` |
| `389` | `0xf081...e39e` | `LONG` | 6,137,288.70 USD | `4,717.00` | `1195.70` | `1285.60` | `1200.11` | 497,164.66 USD | `+8.10%` | `10X Cross` |
| `440` | `0x4cae...7c34` | `LONG` | 5,210,072.80 USD | `4,004.36` | `999.34` | `1285.60` | `807.77` | 1,208,344.64 USD | `+23.19%` | `10X Cross` |
| `450` | `0xa61c...66b9` | `LONG` | 5,069,174.40 USD | `3,888.00` | `1148.34` | `1285.60` | `0.000000` | 604,432.26 USD | `+11.92%` | `10X Cross` |
| `475` | `0x9aa5...58af` | `SHORT` | 4,844,587.68 USD | `3,720.31` | `1205.51` | `1285.60` | `3396.37` | -359,700.88 USD | `-7.42%` | `10X Cross` |
| `482` | `0x0153...8052` | `SHORT` | 4,752,531.12 USD | `3,698.18` | `1307.82` | `1285.60` | `2504.70` | 84,039.63 USD | `+1.77%` | `1X Isolated` |
| `503` | `0xd4c1...3d1d` | `SHORT` | 4,452,833.02 USD | `3,468.90` | `1302.99` | `1285.60` | `2823.73` | 67,104.36 USD | `+1.51%` | `10X Cross` |
| `504` | `0x382b...3e39` | `LONG` | 4,443,695.54 USD | `3,465.14` | `1205.05` | `1285.60` | `0.000000` | 268,040.87 USD | `+6.03%` | `10X Cross` |
| `533` | `0xd21d...90f1` | `LONG` | 4,230,698.55 USD | `3,250.00` | `1253.64` | `1285.60` | `875.90` | 156,356.82 USD | `+3.70%` | `4X Isolated` |
| `553` | `0x1338...c48e` | `LONG` | 4,098,353.26 USD | `3,149.43` | `1018.52` | `1285.60` | `820.19` | 890,607.72 USD | `+21.73%` | `4X Isolated` |
| `554` | `0x27c9...d65d` | `SHORT` | 4,097,361.44 USD | `3,188.36` | `1254.40` | `1285.60` | `1759.23` | -97,893.95 USD | `-2.39%` | `10X Cross` |
| `558` | `0x456f...cdf1` | `LONG` | 4,079,357.58 USD | `3,134.11` | `1268.52` | `1285.60` | `493.51` | 103,667.94 USD | `+2.54%` | `10X Cross` |
| `583` | `0xdbe0...d6d5` | `LONG` | 3,965,008.99 USD | `3,085.37` | `422.97` | `1285.60` | `338.51` | 2,660,004.49 USD | `+67.09%` | `3X Isolated` |
| `593` | `0x9c06...0560` | `SHORT` | 3,905,575.74 USD | `2,989.80` | `786.00` | `1285.60` | `2403.22` | -1,555,580.74 USD | `-39.83%` | `10X Cross` |
| `656` | `0x2e30...4cb5` | `SHORT` | 3,499,108.83 USD | `2,722.83` | `1301.06` | `1285.60` | `3005.58` | 43,459.08 USD | `+1.24%` | `2X Cross` |
| `681` | `0xac48...3201` | `LONG` | 3,319,664.04 USD | `2,540.30` | `1393.86` | `1285.60` | `530.24` | -221,165.25 USD | `-6.66%` | `10X Cross` |
| `696` | `0xa183...0482` | `LONG` | 3,264,552.20 USD | `2,534.00` | `530.25` | `1285.60` | `444.43` | 1,920,889.48 USD | `+58.84%` | `5X Isolated` |
| `698` | `0x325e...9564` | `LONG` | 3,261,990.26 USD | `2,501.91` | `1306.24` | `1285.60` | `0.000000` | -6,103.65 USD | `-0.19%` | `10X Cross` |
| `700` | `0x0871...e927` | `LONG` | 3,255,500.00 USD | `2,500.00` | `1276.50` | `1285.60` | `0.000000` | 64,250.00 USD | `+1.97%` | `10X Cross` |
| `712` | `0x9b86...6e6e` | `LONG` | 3,211,816.16 USD | `2,467.30` | `637.58` | `1285.60` | `889.66` | 1,638,716.56 USD | `+51.02%` | `3X Cross` |
| `769` | `0xb2f7...af9f` | `SHORT` | 3,012,000.70 USD | `2,313.72` | `746.63` | `1285.60` | `4232.99` | -1,284,511.95 USD | `-42.65%` | `10X Cross` |
| `773` | `0x5b5f...c052` | `LONG` | 3,007,763.77 USD | `2,326.37` | `1307.86` | `1285.60` | `1236.08` | -34,791.66 USD | `-1.16%` | `10X Cross` |
| `783` | `0x634f...6951` | `LONG` | 2,968,462.25 USD | `2,272.42` | `1281.94` | `1285.60` | `1250.04` | 55,361.78 USD | `+1.86%` | `10X Cross` |
| `798` | `0xf48f...10fe` | `LONG` | 2,888,030.28 USD | `2,218.49` | `1517.87` | `1285.60` | `924.81` | -479,356.54 USD | `-16.60%` | `3X Cross` |
| `839` | `0x5bc4...3b0c` | `SHORT` | 2,744,393.12 USD | `2,130.74` | `1089.65` | `1285.60` | `3618.61` | -422,635.54 USD | `-15.40%` | `5X Cross` |
| `843` | `0x8de4...b9aa` | `SHORT` | 2,733,943.42 USD | `2,091.29` | `1331.35` | `1285.60` | `1689.83` | 50,296.29 USD | `+1.84%` | `3X Cross` |
| `846` | `0x4fe2...ac59` | `SHORT` | 2,706,091.89 USD | `2,071.57` | `1478.56` | `1285.60` | `1831.35` | 356,854.32 USD | `+13.19%` | `10X Cross` |
| `855` | `0x4e23...20c3` | `LONG` | 2,666,430.48 USD | `2,070.21` | `1296.80` | `1285.60` | `0.000000` | -18,211.31 USD | `-0.68%` | `4X Cross` |
| `870` | `0x668c...ea2e` | `SHORT` | 2,604,400.00 USD | `2,000.00` | `1406.98` | `1285.60` | `2702.62` | 209,563.99 USD | `+8.05%` | `10X Cross` |
| `889` | `0x58b2...11f3` | `LONG` | 2,548,863.07 USD | `1,963.08` | `1303.85` | `1285.60` | `0.000000` | -10,696.14 USD | `-0.42%` | `10X Cross` |
| `895` | `0x77ee...2902` | `SHORT` | 2,531,979.63 USD | `1,946.03` | `759.84` | `1285.60` | `5234.95` | -1,053,302.13 USD | `-41.60%` | `10X Cross` |
| `913` | `0x3e2f...b269` | `SHORT` | 2,480,056.88 USD | `1,925.51` | `1134.87` | `1285.60` | `2931.75` | -294,858.02 USD | `-11.89%` | `10X Cross` |
| `915` | `0x4f12...618b` | `SHORT` | 2,479,006.84 USD | `1,896.28` | `1608.30` | `1285.60` | `2116.72` | 570,777.55 USD | `+23.02%` | `3X Cross` |
| `920` | `0xe097...d0fe` | `LONG` | 2,460,646.80 USD | `1,913.56` | `1261.17` | `1285.60` | `0.000000` | 47,320.64 USD | `+1.92%` | `10X Cross` |
| `962` | `0x866d...d6e1` | `LONG` | 2,344,647.25 USD | `1,802.05` | `674.73` | `1285.60` | `125.55` | 1,128,745.94 USD | `+48.14%` | `10X Cross` |
| `992` | `0x2309...a2d9` | `LONG` | 2,277,581.44 USD | `1,750.37` | `1186.09` | `1285.60` | `807.10` | 201,487.33 USD | `+8.85%` | `8X Cross` |
| `1003` | `0x023a...2355` | `SHORT` | 2,237,365.99 USD | `1,742.98` | `1313.27` | `1285.60` | `5911.10` | 51,644.55 USD | `+2.31%` | `10X Cross` |
| `1021` | `0x2edd...8179` | `SHORT` | 2,184,504.49 USD | `1,701.46` | `1261.58` | `1285.60` | `3050.61` | -37,982.50 USD | `-1.74%` | `10X Cross` |
| `1046` | `0x3e47...aaf6` | `LONG` | 2,129,618.42 USD | `1,636.28` | `1279.54` | `1285.60` | `1041.94` | 35,926.33 USD | `+1.69%` | `10X Cross` |
| `1047` | `0xa271...a3f7` | `LONG` | 2,123,469.29 USD | `1,631.43` | `1190.60` | `1285.60` | `910.29` | 181,087.48 USD | `+8.53%` | `4X Cross` |
| `1061` | `0x7f75...9edf` | `LONG` | 2,097,630.41 USD | `1,605.78` | `1199.97` | `1285.60` | `974.03` | 170,738.52 USD | `+8.14%` | `10X Cross` |
| `1066` | `0x71d0...8c26` | `SHORT` | 2,092,733.95 USD | `1,628.46` | `1349.68` | `1285.60` | `5807.58` | 105,158.98 USD | `+5.02%` | `10X Cross` |
| `1071` | `0x265e...7f70` | `LONG` | 2,084,824.78 USD | `1,601.74` | `1388.09` | `1285.60` | `0.000000` | -138,540.22 USD | `-6.65%` | `3X Cross` |
| `1082` | `0x6646...6de5` | `SHORT` | 2,057,440.00 USD | `1,600.00` | `660.64` | `1285.60` | `4584.88` | -1,000,415.03 USD | `-48.62%` | `10X Cross` |
| `1089` | `0xdf57...93f5` | `LONG` | 2,046,807.20 USD | `1,579.76` | `1218.38` | `1285.60` | `780.13` | 122,051.22 USD | `+5.96%` | `3X Isolated` |
| `1097` | `0xab59...59b5` | `LONG` | 2,037,263.98 USD | `1,565.32` | `1342.15` | `1285.60` | `804.58` | -63,631.24 USD | `-3.12%` | `10X Cross` |
| `1100` | `0xfe7c...b7ae` | `SHORT` | 2,036,393.22 USD | `1,562.49` | `1350.62` | `1285.60` | `6739.09` | 73,935.83 USD | `+3.63%` | `10X Cross` |
| `1159` | `0xcf67...eb24` | `LONG` | 1,959,450.00 USD | `1,500.00` | `887.05` | `1285.60` | `561.11` | 628,878.63 USD | `+32.09%` | `10X Cross` |
| `1196` | `0x039c...0ebd` | `SHORT` | 1,904,576.36 USD | `1,480.49` | `1238.67` | `1285.60` | `3203.82` | -70,745.04 USD | `-3.71%` | `10X Cross` |
| `1247` | `0xdf83...3cff` | `SHORT` | 1,840,174.34 USD | `1,431.04` | `1251.71` | `1285.60` | `1779.24` | -48,927.14 USD | `-2.66%` | `10X Cross` |
| `1270` | `0x2ab7...c2f8` | `LONG` | 1,799,795.40 USD | `1,400.51` | `813.26` | `1285.60` | `805.57` | 660,813.72 USD | `+36.72%` | `3X Cross` |
| `1276` | `0x11be...8b1d` | `LONG` | 1,790,780.33 USD | `1,375.83` | `1206.55` | `1285.60` | `1134.41` | 130,772.37 USD | `+7.30%` | `10X Isolated` |
| `1277` | `0xfc27...9d9d` | `SHORT` | 1,790,758.04 USD | `1,394.78` | `1317.41` | `1285.60` | `12429.38` | 46,744.29 USD | `+2.61%` | `10X Cross` |
| `1338` | `0xef96...9383` | `SHORT` | 1,683,011.64 USD | `1,308.82` | `1249.96` | `1285.60` | `4356.26` | -47,045.22 USD | `-2.80%` | `10X Cross` |
| `1373` | `0xe065...0f85` | `SHORT` | 1,643,413.18 USD | `1,262.61` | `1087.02` | `1285.60` | `1772.03` | -270,937.05 USD | `-16.49%` | `10X Cross` |
| `1419` | `0x7277...0b98` | `SHORT` | 1,600,069.01 USD | `1,234.96` | `1298.48` | `1285.60` | `2389.70` | 3,500.41 USD | `+0.22%` | `10X Cross` |
| `1453` | `0x5975...9abd` | `LONG` | 1,561,920.00 USD | `1,200.00` | `1179.54` | `1285.60` | `425.43` | 146,477.21 USD | `+9.38%` | `5X Cross` |
| `1502` | `0x69cc...14fd` | `SHORT` | 1,504,709.58 USD | `1,161.36` | `675.33` | `1285.60` | `8014.90` | -720,404.05 USD | `-47.88%` | `10X Cross` |
| `1519` | `0x3fc5...c0c1` | `SHORT` | 1,479,535.25 USD | `1,148.44` | `1264.34` | `1285.60` | `3267.15` | -27,521.48 USD | `-1.86%` | `10X Cross` |
| `1528` | `0xe35c...a1d3` | `LONG` | 1,469,460.83 USD | `1,127.06` | `1318.20` | `1285.60` | `694.33` | -16,234.52 USD | `-1.10%` | `2X Isolated` |
| `1538` | `0x5f94...4b96` | `LONG` | 1,451,806.51 USD | `1,115.27` | `538.00` | `1285.60` | `0.000000` | 851,788.88 USD | `+58.67%` | `10X Cross` |
| `1557` | `0x71df...a23d` | `SHORT` | 1,428,972.11 USD | `1,098.28` | `513.50` | `1285.60` | `2549.10` | -865,001.92 USD | `-60.53%` | `2X Cross` |
| `1559` | `0x3205...40bb` | `SHORT` | 1,426,425.74 USD | `1,111.01` | `1314.30` | `1285.60` | `2535.17` | 33,778.20 USD | `+2.37%` | `10X Cross` |
| `1579` | `0xbfc7...80b4` | `SHORT` | 1,398,897.50 USD | `1,075.00` | `558.03` | `1285.60` | `5655.03` | -799,018.77 USD | `-57.12%` | `10X Cross` |
| `1632` | `0x51f6...2b39` | `SHORT` | 1,340,519.99 USD | `1,044.10` | `1302.75` | `1285.60` | `2710.64` | 19,678.16 USD | `+1.47%` | `10X Cross` |
| `1650` | `0x123d...3bff` | `SHORT` | 1,312,546.46 USD | `1,008.41` | `489.46` | `1285.60` | `4248.56` | -818,972.43 USD | `-62.40%` | `10X Cross` |
| `1657` | `0xe282...df29` | `LONG` | 1,303,800.00 USD | `1,000.00` | `420.99` | `1285.60` | `127.60` | 882,813.14 USD | `+67.71%` | `10X Cross` |
| `1679` | `0x266b...efcb` | `LONG` | 1,288,800.00 USD | `1,000.00` | `826.11` | `1285.60` | `200.94` | 462,687.07 USD | `+35.90%` | `10X Cross` |
| `1680` | `0x0748...d4b2` | `LONG` | 1,288,800.00 USD | `1,000.00` | `1334.09` | `1285.60` | `0.000000` | -45,288.30 USD | `-3.51%` | `7X Cross` |
| `1684` | `0xb5ff...d912` | `LONG` | 1,283,900.00 USD | `1,000.00` | `1141.93` | `1285.60` | `400.45` | 141,969.70 USD | `+11.06%` | `2X Cross` |
| `1690` | `0x17f0...094f` | `LONG` | 1,280,672.73 USD | `984.30` | `1287.23` | `1285.60` | `536.76` | 13,652.57 USD | `+1.07%` | `5X Cross` |
| `1776` | `0x757d...94ba` | `LONG` | 1,191,400.00 USD | `925.00` | `1558.31` | `1285.60` | `0.000000` | -250,040.58 USD | `-20.99%` | `10X Cross` |
| `1811` | `0x2847...d47b` | `LONG` | 1,159,354.58 USD | `901.59` | `1239.19` | `1285.60` | `0.000000` | 42,115.09 USD | `+3.63%` | `5X Cross` |
| `1835` | `0xcf0a...856f` | `LONG` | 1,137,983.25 USD | `871.15` | `1292.19` | `1285.60` | `938.47` | 12,288.40 USD | `+1.08%` | `4X Cross` |
| `1846` | `0xdf95...7d72` | `SHORT` | 1,130,987.51 USD | `880.90` | `1074.02` | `1285.60` | `43564.57` | -184,884.11 USD | `-16.35%` | `10X Cross` |
| `1863` | `0xf096...7553` | `SHORT` | 1,118,898.02 USD | `870.67` | `1240.34` | `1285.60` | `3674.00` | -38,967.51 USD | `-3.48%` | `10X Cross` |
| `1870` | `0x7a76...b16d` | `LONG` | 1,116,762.15 USD | `857.86` | `1358.50` | `1285.60` | `1208.72` | -48,640.82 USD | `-4.36%` | `10X Cross` |
| `1915` | `0x601c...4f54` | `SHORT` | 1,072,817.75 USD | `824.42` | `615.11` | `1285.60` | `3003.21` | -565,704.99 USD | `-52.73%` | `5X Cross` |
| `1931` | `0x71b1...79c8` | `LONG` | 1,059,769.84 USD | `812.52` | `1231.55` | `1285.60` | `721.94` | 59,114.38 USD | `+5.58%` | `10X Cross` |
| `1940` | `0xae55...2236` | `LONG` | 1,049,549.73 USD | `817.47` | `1467.80` | `1285.60` | `0.000000` | -150,331.48 USD | `-14.32%` | `10X Cross` |
| `1948` | `0x0f02...5384` | `LONG` | 1,044,697.59 USD | `800.78` | `1290.36` | `1285.60` | `299.14` | 11,403.52 USD | `+1.09%` | `3X Cross` |
| `1961` | `0xabdb...84ac` | `LONG` | 1,032,828.80 USD | `793.69` | `711.79` | `1285.60` | `664.33` | 467,888.44 USD | `+45.30%` | `3X Cross` |
| `1977` | `0x9b0f...db40` | `LONG` | 1,028,080.00 USD | `800.00` | `1268.86` | `1285.60` | `781.96` | 12,990.24 USD | `+1.26%` | `10X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `1297.10` | 194.56 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Long: 0.19K USD at 1297.1000 USD [API] | `2026-10-27 15:46:39` |
| `ANNOUNCEMENT` | `INFO` | `1326.30` | 13.26 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Long: 0.01K USD at 1326.3000 USD [API] | `2026-10-27 23:06:56` |
| `ANNOUNCEMENT` | `INFO` | `1326.50` | 11,341.58 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Long: 11.34K USD at 1326.5000 USD [API] | `2026-10-27 23:06:49` |
| `ANNOUNCEMENT` | `INFO` | `1268.00` | 95,100.00 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Long: 95.10K USD at 1268.0000 USD [API] | `2026-10-22 08:34:05` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`1404.15` (Vol: 3,000,000.00 USD, Dist: `+7.59%`) | Long MP=`1287.60` (Vol: 2,300,000.00 USD, Dist: `--1.34%`)
  * 48H Horizon: Short MP=`1404.15` (Vol: 3,000,000.00 USD, Dist: `+7.59%`) | Long MP=`1287.60` (Vol: 2,300,000.00 USD, Dist: `--1.34%`)
  * 3D Horizon: Short MP=`1404.42` (Vol: 3,000,000.00 USD, Dist: `+7.61%`) | Long MP=`1228.81` (Vol: 2,600,000.00 USD, Dist: `--5.85%`)
  * 7D Horizon: Short MP=`1404.10` (Vol: 3,000,000.00 USD, Dist: `+7.58%`) | Long MP=`1200.46` (Vol: 3,000,000.00 USD, Dist: `--8.02%`)
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
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `0 USD` | Total OI Tokens: `-`
  * 1h OI Change: `0.00%` | 4h OI Change: `0.00%` | 24h OI Change: `0.00%`
  * Exchange Breakdown: Binance=`-` | Bybit=`-` | OKX=`-` | Hyperliquid=`-`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `47.28K` | Last 24h: `33.19K` | Last 3d: `283.86K` | Last 7d: `777.60K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0022%` | **USDT OKX** | `0.0100%` |
| **USDT Bybit** | `0.0100%` | **USDT KuCoin** | `0.0087%` |
| **USDT MEXC** | `0.0023%` | **USDT BingX** | `0.0021%` |
| **USDT Gate** | `0.0074%` | **USDT Bitget** | `0.0100%` |
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
| `5:00 UTC` | `1321.35` | `1325.74` | `1321.35` | `1333.35` | `1318.35` | 26,289,288.34 USD | 11,537,630.34 USD | 14,751,657.99 USD | -3,214,027.65 USD | `-12.23%` | `3B / 5S` |
| `0:00 UTC` | `1315.95` | `1314.40` | `1315.95` | `1321.95` | `1307.85` | 50,919,152.62 USD | 22,517,005.07 USD | 28,402,147.55 USD | -5,885,142.49 USD | `-11.56%` | `2B / 5S` |
| `5:00 UTC` | `1315.95` | `1319.00` | `1315.95` | `1325.85` | `1312.05` | 22,246,351.59 USD | 13,151,982.06 USD | 9,094,369.53 USD | 4,057,612.52 USD | `+18.24%` | `9B / 1S` |
| `0:00 UTC` | `1320.75` | `1319.74` | `1320.75` | `1325.25` | `1315.95` | 11,564,611.33 USD | 5,754,638.99 USD | 5,809,972.34 USD | -55,333.35 USD | `-0.48%` | `1B / 2S` |
| `5:00 UTC` | `1322.85` | `1320.89` | `1322.85` | `1324.95` | `1316.85` | 7,868,027.33 USD | 4,223,932.72 USD | 3,644,094.61 USD | 579,838.11 USD | `+7.37%` | `3B / 0S` |
| `0:00 UTC` | `1324.95` | `1324.41` | `1324.95` | `1327.05` | `1319.85` | 12,000,472.36 USD | 6,714,467.49 USD | 5,286,004.87 USD | 1,428,462.62 USD | `+11.90%` | `2B / 1S` |
| `5:00 UTC` | `1325.25` | `1325.38` | `1325.25` | `1330.65` | `1320.75` | 11,021,893.68 USD | 5,577,839.59 USD | 5,444,054.10 USD | 133,785.49 USD | `+1.21%` | `3B / 1S` |
| `0:00 UTC` | `1294.05` | `1302.04` | `1294.05` | `1328.55` | `1286.25` | 68,949,402.59 USD | 35,232,633.05 USD | 33,716,769.55 USD | 1,515,863.50 USD | `+2.20%` | `6B / 24S` |
| `5:00 UTC` | `1306.05` | `1306.88` | `1306.05` | `1312.05` | `1300.05` | 17,712,248.68 USD | 9,074,345.66 USD | 8,637,903.02 USD | 436,442.64 USD | `+2.46%` | `3B / 5S` |
| `0:00 UTC` | `1303.95` | `1302.46` | `1303.95` | `1304.55` | `1300.95` | 740,527.25 USD | 423,144.95 USD | 317,382.30 USD | 105,762.65 USD | `+14.28%` | `5B / 1S` |

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
| `5m` | -1,060,000.00 USD | -1,070,000.00 USD | **`DISTRIBUTION`** |
| `15m` | -1,370,000.00 USD | -1,240,000.00 USD | **`DISTRIBUTION`** |
| `30m` | -2,730,000.00 USD | -7,990,000.00 USD | **`DISTRIBUTION`** |
| `1h` | -3,440,000.00 USD | -7,190,000.00 USD | **`DISTRIBUTION`** |
| `2h` | -2,570,000.00 USD | 4,130,000.00 USD | **`ACCUMULATION`** |
| `4h` | 1,810,000.00 USD | -21,410,000.00 USD | **`DISTRIBUTION`** |
| `6h` | 20,110,000.00 USD | 73,900,000.00 USD | **`ACCUMULATION`** |
| `8h` | 25,960,000.00 USD | 86,050,000.00 USD | **`ACCUMULATION`** |
| `12h` | 24,130,000.00 USD | 102,200,000.00 USD | **`ACCUMULATION`** |
| `24h` | 10,010,000.00 USD | 55,890,000.00 USD | **`ACCUMULATION`** |
| `1w` | 45,360,000.00 USD | 251,470,000.00 USD | **`ACCUMULATION`** |
| `30d` | 65,960,000.00 USD | -509,600,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-1.06M` | 15m=`-1.37M` | 1h=`-3.44M` | 24h=`+10.01M`
* Futures Capital Netflows: 5m=`-1.07M` | 15m=`-1.24M` | 1h=`-7.19M` | 24h=`+55.89M`
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
  * `2026-10-30 01:35:49 IST`: [sec.gov] - (Sentiment: `Neutral`)
  * `2026-10-30 01:59:49 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 01:59:49 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 01:59:49 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 01:58:49 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 01:58:49 IST`: [@DeItaone] - (Sentiment: `Neutral`)
  * `2026-10-30 01:58:49 IST`: [@mb_ghalibaf] - (Sentiment: `Neutral`)
  * `2026-10-30 01:58:49 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-29 23:00:49 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-29 23:00:49 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:00:49 IST`: [fxstreet.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:00:49 IST`: [ForexFactory] - (Sentiment: `Neutral`)
  * `2026-10-29 22:00:49 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-29 22:00:49 IST`: [youtube.com/bankofcanadaofficial] - (Sentiment: `Neutral`)
  * `2026-10-29 21:00:49 IST`: [notayesmanseconomics.wordpress.com] - (Sentiment: `Neutral`)


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
  * Execution Entry: `1230.55` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `1209.47` (Risk Distance: `21.08` pts)
  * +2.5R Take Profit: `1283.24`
  * Mathematical Lot Sizing: **`0.47 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `1309.36` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `1330.44` (Risk Distance: `21.08` pts)
  * +2.5R Take Profit: `1256.67`
  * Mathematical Lot Sizing: **`0.47 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`1300.29`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
