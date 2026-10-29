# 🏛️ SOVEREIGN CANDIDATE DOSSIER: ZECUSD
**Canonical Key**: `ZECUSD` | **Broker Instrument**: `ZECUSD.p` | **Asset Class**: `Crypto Altcoin`
**Timestamp**: `2026-10-30 01:48:13 IST` (`2026-10-29 20:18:13 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `1304.98` | **Live Ask Quote**: `1306.38` | **Mid Price**: `1305.68`
- **Spread Points**: `140.00` | **Spread BPS**: `10.72 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `1281.87` | VWAP Z-Score: `+1.14` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `14.45` (Volatility Regime: `HIGH_EXPANSION`)
  * 14-Period RSI: `54.75` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `1398.67` | Lower -3.00σ Band: `1165.06`
  * Upper +2.51σ Band: `1379.60` | Lower -2.51σ Band: `1184.14`
  * Upper +2.01σ Band: `1360.13` | Lower -2.01σ Band: `1203.61`
  * Upper +2.00σ Band: `1359.74` | Lower -2.00σ Band: `1203.99`
  * Upper +1.28σ Band: `1331.70` | Lower -1.28σ Band: `1232.03`
  * Upper +1.00σ Band: `1320.80` | Lower -1.00σ Band: `1242.93`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`1325.29` | EMA-20=`1322.72` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`1303.73` (Slope: `+0.0000`) | EMA-100=`1291.74`
  * Institutional Anchors: EMA-144=`1286.38` | EMA-200=`1281.35` (Slope: `+0.4726`) | EMA-233=`1279.18`
- **Range Boundaries**: 24H High=`1396.49` | 24H Low=`1230.00` | Weekly High=`1396.49` | Weekly Low=`1210.62`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `1309.36` (Distance: `-0.25%`)
  * Point of Control (POC) = `1247.20` (Distance: `+4.72%`)
  * Value Area Low (VAL) = `1230.55` (Distance: `+6.14%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BULLISH (Above Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
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
  * Golden Pocket Zone (0.618 - 0.650): `1300.46` - `1310.90`
  * Optimal Trade Entry (OTE 0.705): `1308.29`
  * Structural Invalidation Anchor (0.786): `1316.13`

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
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 01:44:44 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `16` | `0xb83d...6e36` | `SHORT` | 68,720,095.39 USD | `52,582.52` | `1336.45` | `1310.00` | `3781.21` | 1,553,819.51 USD | `+2.26%` | `3X Cross` |
| `24` | `0x5b5d...c060` | `SHORT` | 53,349,096.34 USD | `40,727.61` | `1478.36` | `1310.00` | `5099.28` | 6,861,167.85 USD | `+12.86%` | `3X Cross` |
| `41` | `0x7fda...17d1` | `SHORT` | 29,434,472.04 USD | `22,484.51` | `1261.60` | `1310.00` | `2860.43` | -1,067,926.02 USD | `-3.63%` | `5X Cross` |
| `78` | `0x60b0...991e` | `LONG` | 21,929,442.21 USD | `16,779.74` | `1179.65` | `1310.00` | `899.52` | 2,135,195.19 USD | `+9.74%` | `10X Cross` |
| `84` | `0xbf73...5d58` | `LONG` | 20,878,400.00 USD | `16,000.00` | `1214.30` | `1310.00` | `736.94` | 1,449,567.75 USD | `+6.94%` | `10X Cross` |
| `135` | `0xc36a...105b` | `LONG` | 15,012,411.44 USD | `11,510.82` | `1215.14` | `1310.00` | `942.42` | 1,025,130.42 USD | `+6.83%` | `10X Cross` |
| `168` | `0x8742...8427` | `LONG` | 12,052,664.98 USD | `9,201.21` | `1286.37` | `1310.00` | `698.37` | 216,494.99 USD | `+1.80%` | `10X Cross` |
| `177` | `0x9071...5c0b` | `LONG` | 11,559,274.45 USD | `8,829.94` | `1370.53` | `1310.00` | `579.52` | -542,414.19 USD | `-4.69%` | `2X Cross` |
| `192` | `0xad59...ba81` | `SHORT` | 11,010,632.50 USD | `8,425.00` | `330.91` | `1310.00` | `2141.26` | -8,222,674.73 USD | `-74.68%` | `10X Cross` |
| `200` | `0x9ffd...ce40` | `LONG` | 10,797,815.18 USD | `8,272.92` | `1255.71` | `1310.00` | `579.14` | 409,464.07 USD | `+3.79%` | `5X Cross` |
| `203` | `0xdd53...2b13` | `SHORT` | 10,779,826.37 USD | `8,230.76` | `739.37` | `1310.00` | `8017.04` | -4,694,225.86 USD | `-43.55%` | `3X Cross` |
| `220` | `0xfc66...ca06` | `SHORT` | 10,134,747.03 USD | `7,763.71` | `1319.70` | `1310.00` | `5616.07` | 111,017.14 USD | `+1.10%` | `10X Cross` |
| `221` | `0x880a...311c` | `SHORT` | 10,095,543.39 USD | `7,707.11` | `1367.50` | `1310.00` | `2308.01` | 443,940.81 USD | `+4.40%` | `10X Cross` |
| `269` | `0x2b61...2f6c` | `LONG` | 8,892,664.80 USD | `6,807.00` | `1453.56` | `1310.00` | `621.79` | -1,001,686.42 USD | `-11.26%` | `10X Cross` |
| `286` | `0x2ae5...83e7` | `LONG` | 8,426,414.88 USD | `6,436.80` | `1391.82` | `1310.00` | `482.34` | -532,477.11 USD | `-6.32%` | `2X Cross` |
| `334` | `0x26b6...9a13` | `LONG` | 7,113,295.94 USD | `5,433.73` | `1282.23` | `1310.00` | `218.57` | 145,992.71 USD | `+2.05%` | `10X Cross` |
| `337` | `0xecb6...2b00` | `SHORT` | 7,053,352.25 USD | `5,387.94` | `1324.02` | `1310.00` | `6292.31` | 80,361.88 USD | `+1.14%` | `5X Cross` |
| `346` | `0x45d2...4029` | `SHORT` | 6,842,665.70 USD | `5,227.00` | `833.44` | `1310.00` | `8218.91` | -2,486,287.73 USD | `-36.34%` | `5X Cross` |
| `373` | `0xea00...a918` | `LONG` | 6,531,000.00 USD | `5,000.00` | `739.16` | `1310.00` | `0.000000` | 2,835,184.89 USD | `+43.41%` | `5X Cross` |
| `381` | `0xdd7a...8830` | `LONG` | 6,357,128.52 USD | `4,860.19` | `897.48` | `1310.00` | `783.92` | 1,995,224.85 USD | `+31.39%` | `10X Cross` |
| `386` | `0xf081...e39e` | `LONG` | 6,237,289.10 USD | `4,717.00` | `1195.70` | `1310.00` | `1200.11` | 597,165.06 USD | `+9.57%` | `10X Cross` |
| `437` | `0x4cae...7c34` | `LONG` | 5,228,893.29 USD | `4,004.36` | `999.34` | `1310.00` | `804.06` | 1,227,165.13 USD | `+23.47%` | `10X Cross` |
| `448` | `0xa61c...66b9` | `LONG` | 5,080,060.80 USD | `3,888.00` | `1148.34` | `1310.00` | `0.000000` | 615,318.66 USD | `+12.11%` | `10X Cross` |
| `472` | `0x9aa5...58af` | `SHORT` | 4,857,980.80 USD | `3,720.31` | `1205.51` | `1310.00` | `3393.91` | -373,094.00 USD | `-7.68%` | `10X Cross` |
| `473` | `0x382b...3e39` | `LONG` | 4,848,539.85 USD | `3,703.72` | `1205.04` | `1310.00` | `0.000000` | 385,426.64 USD | `+7.95%` | `10X Cross` |
| `475` | `0x0153...8052` | `SHORT` | 4,839,808.17 USD | `3,698.18` | `1307.82` | `1310.00` | `2504.70` | -3,237.42 USD | `-0.07%` | `1X Isolated` |
| `497` | `0xd4c1...3d1d` | `SHORT` | 4,542,353.33 USD | `3,467.71` | `1302.99` | `1310.00` | `2731.28` | -23,949.74 USD | `-0.53%` | `10X Cross` |
| `531` | `0xd21d...90f1` | `LONG` | 4,247,750.00 USD | `3,250.00` | `1253.64` | `1310.00` | `875.90` | 173,408.27 USD | `+4.08%` | `4X Isolated` |
| `554` | `0x1338...c48e` | `LONG` | 4,112,210.75 USD | `3,149.43` | `1018.52` | `1310.00` | `820.19` | 904,465.21 USD | `+21.99%` | `4X Isolated` |
| `555` | `0x27c9...d65d` | `SHORT` | 4,112,204.96 USD | `3,148.22` | `1253.74` | `1310.00` | `1807.21` | -165,159.55 USD | `-4.02%` | `10X Cross` |
| `557` | `0x456f...cdf1` | `LONG` | 4,093,774.48 USD | `3,134.11` | `1268.52` | `1310.00` | `493.51` | 118,084.85 USD | `+2.88%` | `10X Cross` |
| `567` | `0xdbe0...d6d5` | `LONG` | 4,039,983.48 USD | `3,085.37` | `422.97` | `1310.00` | `338.51` | 2,734,978.99 USD | `+67.70%` | `3X Isolated` |
| `594` | `0x9c06...0560` | `SHORT` | 3,901,390.02 USD | `2,989.80` | `786.00` | `1310.00` | `2395.58` | -1,551,395.02 USD | `-39.77%` | `10X Cross` |
| `650` | `0x2e30...4cb5` | `SHORT` | 3,542,851.82 USD | `2,704.88` | `1301.01` | `1310.00` | `3003.16` | -23,787.08 USD | `-0.67%` | `2X Cross` |
| `685` | `0xa183...0482` | `LONG` | 3,319,286.60 USD | `2,534.00` | `530.25` | `1310.00` | `444.43` | 1,975,623.88 USD | `+59.52%` | `5X Isolated` |
| `686` | `0xac48...3201` | `LONG` | 3,318,139.86 USD | `2,540.30` | `1393.86` | `1310.00` | `536.08` | -222,689.43 USD | `-6.71%` | `10X Cross` |
| `699` | `0x325e...9564` | `LONG` | 3,270,997.13 USD | `2,501.91` | `1306.24` | `1310.00` | `0.000000` | 2,903.23 USD | `+0.09%` | `10X Cross` |
| `704` | `0x0871...e927` | `LONG` | 3,260,500.00 USD | `2,500.00` | `1276.50` | `1310.00` | `0.000000` | 69,250.00 USD | `+2.12%` | `10X Cross` |
| `707` | `0x9b86...6e6e` | `LONG` | 3,224,514.37 USD | `2,467.30` | `637.58` | `1310.00` | `889.66` | 1,651,414.77 USD | `+51.21%` | `3X Cross` |
| `771` | `0xb2f7...af9f` | `SHORT` | 3,023,800.67 USD | `2,313.72` | `746.63` | `1310.00` | `4230.90` | -1,296,311.92 USD | `-42.87%` | `10X Cross` |
| `782` | `0x634f...6951` | `LONG` | 2,966,417.07 USD | `2,272.42` | `1281.94` | `1310.00` | `1250.04` | 53,316.61 USD | `+1.80%` | `10X Cross` |
| `797` | `0xf48f...10fe` | `LONG` | 2,899,788.28 USD | `2,218.49` | `1517.87` | `1310.00` | `922.48` | -467,598.54 USD | `-16.13%` | `3X Cross` |
| `828` | `0x5bc4...3b0c` | `SHORT` | 2,790,630.18 USD | `2,130.74` | `1089.65` | `1310.00` | `3594.06` | -468,872.60 USD | `-16.80%` | `5X Cross` |
| `843` | `0x8de4...b9aa` | `SHORT` | 2,729,551.71 USD | `2,091.29` | `1331.35` | `1310.00` | `1689.83` | 54,688.00 USD | `+2.00%` | `3X Cross` |
| `847` | `0x4fe2...ac59` | `SHORT` | 2,707,956.30 USD | `2,071.57` | `1478.56` | `1310.00` | `1819.57` | 354,989.91 USD | `+13.11%` | `10X Cross` |
| `868` | `0x668c...ea2e` | `SHORT` | 2,610,800.00 USD | `2,000.00` | `1406.98` | `1310.00` | `2702.58` | 203,163.99 USD | `+7.78%` | `10X Cross` |
| `883` | `0x4e23...20c3` | `LONG` | 2,555,080.44 USD | `1,954.92` | `1297.39` | `1310.00` | `0.000000` | 18,793.82 USD | `+0.74%` | `4X Cross` |
| `888` | `0x77ee...2902` | `SHORT` | 2,541,125.97 USD | `1,946.03` | `759.84` | `1310.00` | `5236.01` | -1,062,448.47 USD | `-41.81%` | `10X Cross` |
| `898` | `0x3e2f...b269` | `SHORT` | 2,521,840.45 USD | `1,925.51` | `1134.87` | `1310.00` | `2931.75` | -336,641.59 USD | `-13.35%` | `10X Cross` |
| `903` | `0xe097...d0fe` | `LONG` | 2,501,022.92 USD | `1,913.56` | `1261.17` | `1310.00` | `0.000000` | 87,696.76 USD | `+3.51%` | `10X Cross` |
| `916` | `0x4f12...618b` | `SHORT` | 2,477,110.56 USD | `1,896.28` | `1608.30` | `1310.00` | `2116.72` | 572,673.82 USD | `+23.12%` | `3X Cross` |
| `955` | `0x866d...d6e1` | `LONG` | 2,352,215.87 USD | `1,802.05` | `674.73` | `1310.00` | `118.95` | 1,136,314.55 USD | `+48.31%` | `10X Cross` |
| `989` | `0x2309...a2d9` | `LONG` | 2,285,633.15 USD | `1,750.37` | `1186.09` | `1310.00` | `807.32` | 209,539.04 USD | `+9.17%` | `8X Cross` |
| `1003` | `0x2edd...8179` | `SHORT` | 2,228,572.31 USD | `1,701.46` | `1261.58` | `1310.00` | `2995.43` | -82,050.31 USD | `-3.68%` | `10X Cross` |
| `1005` | `0x023a...2355` | `SHORT` | 2,226,584.87 USD | `1,705.15` | `1313.37` | `1310.00` | `5990.00` | 12,910.90 USD | `+0.58%` | `10X Cross` |
| `1038` | `0x3e47...aaf6` | `LONG` | 2,137,851.36 USD | `1,636.28` | `1279.54` | `1310.00` | `1039.12` | 44,159.28 USD | `+2.07%` | `10X Cross` |
| `1040` | `0xa271...a3f7` | `LONG` | 2,131,137.01 USD | `1,631.43` | `1190.60` | `1310.00` | `910.29` | 188,755.21 USD | `+8.86%` | `4X Cross` |
| `1057` | `0x7f75...9edf` | `LONG` | 2,095,382.32 USD | `1,605.78` | `1199.97` | `1310.00` | `974.55` | 168,490.43 USD | `+8.04%` | `10X Cross` |
| `1058` | `0x6646...6de5` | `SHORT` | 2,093,440.00 USD | `1,600.00` | `660.64` | `1310.00` | `4718.23` | -1,036,415.03 USD | `-49.51%` | `10X Cross` |
| `1060` | `0x265e...7f70` | `LONG` | 2,090,591.05 USD | `1,601.74` | `1388.09` | `1310.00` | `0.000000` | -132,773.96 USD | `-6.35%` | `3X Cross` |
| `1080` | `0xdf57...93f5` | `LONG` | 2,069,011.67 USD | `1,579.76` | `1218.38` | `1310.00` | `780.13` | 144,255.69 USD | `+6.97%` | `3X Isolated` |
| `1091` | `0xab59...59b5` | `LONG` | 2,044,307.92 USD | `1,565.32` | `1342.15` | `1310.00` | `800.52` | -56,587.30 USD | `-2.77%` | `10X Cross` |
| `1095` | `0xfe7c...b7ae` | `SHORT` | 2,042,018.18 USD | `1,562.49` | `1350.62` | `1310.00` | `6711.79` | 68,310.87 USD | `+3.35%` | `10X Cross` |
| `1156` | `0xcf67...eb24` | `LONG` | 1,959,450.00 USD | `1,500.00` | `887.05` | `1310.00` | `566.88` | 628,878.63 USD | `+32.09%` | `10X Cross` |
| `1177` | `0x039c...0ebd` | `SHORT` | 1,931,891.40 USD | `1,480.49` | `1238.67` | `1310.00` | `3179.03` | -98,060.08 USD | `-5.08%` | `10X Cross` |
| `1242` | `0x71d0...8c26` | `SHORT` | 1,836,147.01 USD | `1,401.96` | `1358.60` | `1310.00` | `6622.38` | 68,553.60 USD | `+3.73%` | `10X Cross` |
| `1245` | `0x2ab7...c2f8` | `LONG` | 1,834,388.00 USD | `1,400.51` | `813.26` | `1310.00` | `797.96` | 695,406.31 USD | `+37.91%` | `3X Cross` |
| `1246` | `0xdf83...3cff` | `SHORT` | 1,833,237.46 USD | `1,400.38` | `1250.38` | `1310.00` | `1813.00` | -82,231.01 USD | `-4.49%` | `10X Cross` |
| `1247` | `0xfc27...9d9d` | `SHORT` | 1,831,928.36 USD | `1,399.38` | `1317.47` | `1310.00` | `11821.67` | 11,714.87 USD | `+0.64%` | `10X Cross` |
| `1267` | `0x11be...8b1d` | `LONG` | 1,797,109.15 USD | `1,375.83` | `1206.55` | `1310.00` | `1134.41` | 137,101.19 USD | `+7.63%` | `10X Isolated` |
| `1314` | `0xef96...9383` | `SHORT` | 1,710,889.50 USD | `1,308.82` | `1249.96` | `1310.00` | `4286.17` | -74,923.08 USD | `-4.38%` | `10X Cross` |
| `1370` | `0xe065...0f85` | `SHORT` | 1,649,347.44 USD | `1,262.61` | `1087.02` | `1310.00` | `1772.47` | -276,871.32 USD | `-16.79%` | `10X Cross` |
| `1391` | `0x7277...0b98` | `SHORT` | 1,617,427.11 USD | `1,234.96` | `1298.48` | `1310.00` | `2383.39` | -13,857.69 USD | `-0.86%` | `10X Cross` |
| `1447` | `0x5975...9abd` | `LONG` | 1,567,440.00 USD | `1,200.00` | `1179.54` | `1310.00` | `417.35` | 151,997.21 USD | `+9.70%` | `5X Cross` |
| `1488` | `0x69cc...14fd` | `SHORT` | 1,521,033.19 USD | `1,161.36` | `675.33` | `1310.00` | `7915.70` | -736,727.66 USD | `-48.44%` | `10X Cross` |
| `1504` | `0x3fc5...c0c1` | `SHORT` | 1,499,862.64 USD | `1,148.44` | `1264.34` | `1310.00` | `3177.01` | -47,848.86 USD | `-3.19%` | `10X Cross` |
| `1523` | `0xe35c...a1d3` | `LONG` | 1,472,616.60 USD | `1,127.06` | `1318.20` | `1310.00` | `694.33` | -13,078.75 USD | `-0.89%` | `2X Isolated` |
| `1530` | `0x5f94...4b96` | `LONG` | 1,457,769.42 USD | `1,115.27` | `538.00` | `1310.00` | `0.000000` | 857,751.78 USD | `+58.84%` | `10X Cross` |
| `1531` | `0x71df...a23d` | `SHORT` | 1,452,914.61 USD | `1,098.28` | `513.50` | `1310.00` | `2546.94` | -888,944.42 USD | `-61.18%` | `2X Cross` |
| `1579` | `0xbfc7...80b4` | `SHORT` | 1,403,735.00 USD | `1,075.00` | `558.03` | `1310.00` | `5636.43` | -803,856.27 USD | `-57.27%` | `10X Cross` |
| `1616` | `0x51f6...2b39` | `SHORT` | 1,366,831.31 USD | `1,044.10` | `1302.75` | `1310.00` | `2694.90` | -6,633.16 USD | `-0.49%` | `10X Cross` |
| `1648` | `0x123d...3bff` | `SHORT` | 1,316,845.53 USD | `1,008.15` | `489.25` | `1310.00` | `4221.33` | -823,611.46 USD | `-62.54%` | `10X Cross` |
| `1654` | `0x0748...d4b2` | `LONG` | 1,309,900.00 USD | `1,000.00` | `1334.09` | `1310.00` | `0.000000` | -24,188.30 USD | `-1.85%` | `7X Cross` |
| `1655` | `0xb5ff...d912` | `LONG` | 1,309,100.00 USD | `1,000.00` | `1141.93` | `1310.00` | `400.45` | 167,169.70 USD | `+12.77%` | `2X Cross` |
| `1658` | `0x266b...efcb` | `LONG` | 1,308,400.00 USD | `1,000.00` | `826.11` | `1310.00` | `162.96` | 482,287.07 USD | `+36.86%` | `10X Cross` |
| `1662` | `0xe282...df29` | `LONG` | 1,306,600.00 USD | `1,000.00` | `420.99` | `1310.00` | `124.02` | 885,613.14 USD | `+67.78%` | `10X Cross` |
| `1688` | `0x17f0...094f` | `LONG` | 1,284,806.79 USD | `984.30` | `1287.23` | `1310.00` | `536.76` | 17,786.63 USD | `+1.38%` | `5X Cross` |
| `1720` | `0x58b2...11f3` | `LONG` | 1,258,071.40 USD | `963.08` | `1300.23` | `1310.00` | `0.000000` | 5,843.41 USD | `+0.46%` | `10X Cross` |
| `1739` | `0x3205...40bb` | `SHORT` | 1,228,976.65 USD | `938.58` | `1320.33` | `1310.00` | `2754.80` | 10,260.24 USD | `+0.83%` | `10X Cross` |
| `1751` | `0x757d...94ba` | `LONG` | 1,211,472.50 USD | `925.00` | `1558.31` | `1310.00` | `0.000000` | -229,968.08 USD | `-18.98%` | `10X Cross` |
| `1793` | `0x2847...d47b` | `LONG` | 1,175,008.89 USD | `897.57` | `1238.89` | `1310.00` | `0.000000` | 63,014.62 USD | `+5.36%` | `5X Cross` |
| `1813` | `0xdf95...7d72` | `SHORT` | 1,153,540.86 USD | `880.70` | `1073.97` | `1310.00` | `42181.18` | -207,697.63 USD | `-18.01%` | `10X Cross` |
| `1822` | `0xf096...7553` | `SHORT` | 1,149,708.24 USD | `881.07` | `1240.34` | `1310.00` | `3589.86` | -56,878.16 USD | `-4.95%` | `10X Cross` |
| `1834` | `0xcf0a...856f` | `LONG` | 1,136,763.64 USD | `871.15` | `1292.19` | `1310.00` | `938.47` | 11,068.79 USD | `+0.97%` | `4X Cross` |
| `1858` | `0x7a76...b16d` | `LONG` | 1,121,308.81 USD | `857.86` | `1358.50` | `1310.00` | `1208.47` | -44,094.16 USD | `-3.93%` | `10X Cross` |
| `1870` | `0x7d0f...ea35` | `LONG` | 1,109,165.00 USD | `850.00` | `1317.57` | `1310.00` | `1255.65` | -10,770.58 USD | `-0.97%` | `10X Cross` |
| `1904` | `0x601c...4f54` | `SHORT` | 1,077,022.29 USD | `824.42` | `615.11` | `1310.00` | `3004.59` | -569,909.54 USD | `-52.92%` | `5X Cross` |
| `1911` | `0xae55...2236` | `LONG` | 1,070,149.98 USD | `817.47` | `1467.80` | `1310.00` | `0.000000` | -129,731.24 USD | `-12.12%` | `10X Cross` |
| `1927` | `0x71b1...79c8` | `LONG` | 1,061,963.64 USD | `812.52` | `1231.55` | `1310.00` | `720.69` | 61,308.19 USD | `+5.77%` | `10X Cross` |
| `1940` | `0x9b0f...db40` | `LONG` | 1,047,840.00 USD | `800.00` | `1268.86` | `1310.00` | `777.79` | 32,750.24 USD | `+3.13%` | `10X Cross` |
| `1941` | `0x0f02...5384` | `LONG` | 1,046,379.23 USD | `800.78` | `1290.36` | `1310.00` | `294.53` | 13,085.16 USD | `+1.25%` | `3X Cross` |
| `1958` | `0xabdb...84ac` | `LONG` | 1,036,876.62 USD | `793.69` | `711.79` | `1310.00` | `664.33` | 471,936.25 USD | `+45.52%` | `3X Cross` |
| `1959` | `0xfdf8...e381` | `LONG` | 1,034,834.10 USD | `790.01` | `1337.72` | `1310.00` | `566.86` | -21,975.59 USD | `-2.12%` | `10X Cross` |

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
  * 24H Horizon: Short MP=`1404.15` (Vol: 3,000,000.00 USD, Dist: `+6.21%`) | Long MP=`1287.60` (Vol: 2,300,000.00 USD, Dist: `--2.61%`)
  * 48H Horizon: Short MP=`1404.15` (Vol: 3,000,000.00 USD, Dist: `+6.21%`) | Long MP=`1287.60` (Vol: 2,300,000.00 USD, Dist: `--2.61%`)
  * 3D Horizon: Short MP=`1404.42` (Vol: 3,000,000.00 USD, Dist: `+6.23%`) | Long MP=`1228.81` (Vol: 2,600,000.00 USD, Dist: `--7.05%`)
  * 7D Horizon: Short MP=`1404.10` (Vol: 3,000,000.00 USD, Dist: `+6.20%`) | Long MP=`1200.46` (Vol: 3,000,000.00 USD, Dist: `--9.20%`)
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
  * Current Rate: `52.23K` | Last 24h: `33.19K` | Last 3d: `283.86K` | Last 7d: `777.60K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0032%` | **USDT OKX** | `0.0100%` |
| **USDT Bybit** | `0.0100%` | **USDT KuCoin** | `0.0098%` |
| **USDT MEXC** | `0.0032%` | **USDT BingX** | `0.0026%` |
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
| `5:00 UTC` | `1333.95` | `1332.65` | `1333.95` | `1338.15` | `1327.05` | 42,051,592.22 USD | 20,998,597.47 USD | 21,052,994.75 USD | -54,397.28 USD | `-0.13%` | `1B / 3S` |
| `0:00 UTC` | `1324.05` | `1326.61` | `1324.05` | `1336.05` | `1320.15` | 35,175,848.19 USD | 15,805,961.43 USD | 19,369,886.76 USD | -3,563,925.33 USD | `-10.13%` | `1B / 10S` |
| `5:00 UTC` | `1321.35` | `1325.74` | `1321.35` | `1333.35` | `1318.35` | 26,289,288.34 USD | 11,537,630.34 USD | 14,751,657.99 USD | -3,214,027.65 USD | `-12.23%` | `3B / 5S` |
| `0:00 UTC` | `1315.95` | `1314.40` | `1315.95` | `1321.95` | `1307.85` | 50,919,152.62 USD | 22,517,005.07 USD | 28,402,147.55 USD | -5,885,142.49 USD | `-11.56%` | `2B / 5S` |
| `5:00 UTC` | `1315.95` | `1319.00` | `1315.95` | `1325.85` | `1312.05` | 22,246,351.59 USD | 13,151,982.06 USD | 9,094,369.53 USD | 4,057,612.52 USD | `+18.24%` | `9B / 1S` |
| `0:00 UTC` | `1320.75` | `1319.74` | `1320.75` | `1325.25` | `1315.95` | 11,564,611.33 USD | 5,754,638.99 USD | 5,809,972.34 USD | -55,333.35 USD | `-0.48%` | `1B / 2S` |
| `5:00 UTC` | `1322.85` | `1320.89` | `1322.85` | `1324.95` | `1316.85` | 7,868,027.33 USD | 4,223,932.72 USD | 3,644,094.61 USD | 579,838.11 USD | `+7.37%` | `3B / 0S` |
| `0:00 UTC` | `1324.95` | `1324.41` | `1324.95` | `1327.05` | `1319.85` | 12,000,472.36 USD | 6,714,467.49 USD | 5,286,004.87 USD | 1,428,462.62 USD | `+11.90%` | `2B / 1S` |
| `5:00 UTC` | `1325.25` | `1325.38` | `1325.25` | `1330.65` | `1320.75` | 11,021,893.68 USD | 5,577,839.59 USD | 5,444,054.10 USD | 133,785.49 USD | `+1.21%` | `3B / 1S` |
| `0:00 UTC` | `1294.05` | `1301.54` | `1294.05` | `1328.55` | `1286.25` | 62,696,804.96 USD | 31,429,712.61 USD | 31,267,092.35 USD | 162,620.27 USD | `+0.26%` | `6B / 26S` |

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
| `5m` | 420,940.00 USD | 6,220,000.00 USD | **`ACCUMULATION`** |
| `15m` | -2,790,000.00 USD | -11,680,000.00 USD | **`DISTRIBUTION`** |
| `30m` | -3,620,000.00 USD | -10,510,000.00 USD | **`DISTRIBUTION`** |
| `1h` | -3,310,000.00 USD | -6,510,000.00 USD | **`DISTRIBUTION`** |
| `2h` | -3,150,000.00 USD | -10,370,000.00 USD | **`DISTRIBUTION`** |
| `4h` | 636,700.00 USD | -32,120,000.00 USD | **`DISTRIBUTION`** |
| `6h` | 23,770,000.00 USD | 78,600,000.00 USD | **`ACCUMULATION`** |
| `8h` | 26,830,000.00 USD | 85,150,000.00 USD | **`ACCUMULATION`** |
| `12h` | 24,730,000.00 USD | 99,970,000.00 USD | **`ACCUMULATION`** |
| `24h` | 8,510,000.00 USD | 53,300,000.00 USD | **`ACCUMULATION`** |
| `1w` | 46,830,000.00 USD | 250,580,000.00 USD | **`ACCUMULATION`** |
| `30d` | 69,680,000.00 USD | -510,490,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+420.94K` | 15m=`-2.79M` | 1h=`-3.31M` | 24h=`+8.51M`
* Futures Capital Netflows: 5m=`+6.22M` | 15m=`-11.68M` | 1h=`-6.51M` | 24h=`+53.30M`
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
  * `2026-10-30 01:36:17 IST`: [sec.gov] - (Sentiment: `Neutral`)
  * `2026-10-30 00:58:17 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 00:48:17 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 01:40:17 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 01:39:17 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 01:39:17 IST`: [@DeItaone] - (Sentiment: `Neutral`)
  * `2026-10-30 01:39:17 IST`: [@mb_ghalibaf] - (Sentiment: `Neutral`)
  * `2026-10-30 01:39:17 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-30 01:39:17 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-30 01:39:17 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:41:17 IST`: [fxstreet.com] - (Sentiment: `Neutral`)
  * `2026-10-29 21:41:17 IST`: [ForexFactory] - (Sentiment: `Neutral`)
  * `2026-10-29 21:41:17 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-29 21:41:17 IST`: [youtube.com/bankofcanadaofficial] - (Sentiment: `Neutral`)
  * `2026-10-29 21:41:17 IST`: [notayesmanseconomics.wordpress.com] - (Sentiment: `Neutral`)


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
  * Spread-Padded Stop Loss: `1211.11` (Risk Distance: `19.44` pts)
  * +2.5R Take Profit: `1279.16`
  * Mathematical Lot Sizing: **`0.51 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `1309.36` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `1328.80` (Risk Distance: `19.44` pts)
  * +2.5R Take Profit: `1260.75`
  * Mathematical Lot Sizing: **`0.51 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`1316.13`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
