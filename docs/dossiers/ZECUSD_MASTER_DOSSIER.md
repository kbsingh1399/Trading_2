# 🏛️ SOVEREIGN CANDIDATE DOSSIER: ZECUSD
**Canonical Key**: `ZECUSD` | **Broker Instrument**: `ZECUSD.p` | **Asset Class**: `Crypto Altcoin`
**Timestamp**: `2026-10-30 16:24:41 IST` (`2026-10-30 10:54:41 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `1261.40` | **Live Ask Quote**: `1262.50` | **Mid Price**: `1261.95`
- **Spread Points**: `110.00` | **Spread BPS**: `8.72 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `1261.95` | VWAP Z-Score: `+0.00` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `3.15` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `50.00` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `1270.78` | Lower -3.00σ Band: `1253.12`
  * Upper +2.51σ Band: `1268.89` | Lower -2.51σ Band: `1255.01`
  * Upper +2.01σ Band: `1267.25` | Lower -2.01σ Band: `1256.65`
  * Upper +2.00σ Band: `1267.00` | Lower -2.00σ Band: `1256.90`
  * Upper +1.28σ Band: `1265.48` | Lower -1.28σ Band: `1258.42`
  * Upper +1.00σ Band: `1264.47` | Lower -1.00σ Band: `1259.43`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`1261.95` | EMA-20=`1261.95` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`1261.95` (Slope: `+0.0000`) | EMA-100=`1261.95`
  * Institutional Anchors: EMA-144=`1261.95` | EMA-200=`1261.95` (Slope: `+0.0000`) | EMA-233=`1261.95`
- **Range Boundaries**: 24H High=`1274.57` | 24H Low=`1249.33` | Weekly High=`1287.19` | Weekly Low=`1236.71`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `1279.38` (Distance: `-1.17%`)
  * Point of Control (POC) = `1247.68` (Distance: `+1.34%`)
  * Value Area Low (VAL) = `1239.95` (Distance: `+1.97%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`1309.91` | POC=`1246.71` | VAL=`1230.27`
  * Prior Day Extremes: PDH=`1396.49` | PDL=`1206.89` | PDC=`1244.38`
  * Monday Range Blueprint: High=`1267.53` | Mid=`1222.14` | Low=`1176.75`
  * Developing Weekly Value Area: Weekly VAH=`1300.54` | Weekly POC=`1240.47` | Weekly VAL=`1214.11`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`1296.00` | Low=`1180.03`
  * London Session (08:00-16:00 UTC): High=`1283.82` | Low=`1239.95`
  * New York Session (13:00-21:00 UTC): High=`1276.03` | Low=`1245.73`
  * Initial Balance (First Hour): IB High=`1283.82` | IB Low=`1264.92`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `1256.90` - `1267.00`
  * Optimal Trade Entry (OTE 0.705): `1264.47`
  * Structural Invalidation Anchor (0.786): `1272.05`

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
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 16:23:13 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `12` | `0xb83d...6e36` | `SHORT` | 66,576,693.82 USD | `52,385.47` | `1336.45` | `1269.00` | `3173.30` | 3,433,873.58 USD | `+5.16%` | `3X Cross` |
| `21` | `0x5b5d...c060` | `SHORT` | 50,990,261.84 USD | `40,121.38` | `1478.36` | `1269.00` | `4778.47` | 8,323,773.27 USD | `+16.32%` | `3X Cross` |
| `36` | `0x7fda...17d1` | `SHORT` | 33,811,624.15 USD | `26,635.91` | `1262.58` | `1269.00` | `2598.68` | -181,733.70 USD | `-0.54%` | `5X Cross` |
| `78` | `0x60b0...991e` | `LONG` | 21,315,303.72 USD | `16,779.74` | `1179.65` | `1269.00` | `914.87` | 1,521,056.71 USD | `+7.14%` | `10X Cross` |
| `137` | `0xc36a...105b` | `LONG` | 14,622,194.65 USD | `11,510.82` | `1215.14` | `1269.00` | `964.35` | 634,913.62 USD | `+4.34%` | `10X Cross` |
| `172` | `0x8742...8427` | `LONG` | 11,681,856.22 USD | `9,201.21` | `1286.37` | `1269.00` | `712.83` | -154,313.78 USD | `-1.32%` | `10X Cross` |
| `188` | `0x58b2...11f3` | `LONG` | 10,882,818.37 USD | `8,563.08` | `1246.56` | `1269.00` | `386.20` | 208,400.80 USD | `+1.91%` | `10X Cross` |
| `192` | `0x9071...5c0b` | `LONG` | 10,813,551.38 USD | `8,517.29` | `1353.83` | `1269.00` | `253.57` | -717,408.22 USD | `-6.63%` | `2X Cross` |
| `194` | `0xad59...ba81` | `SHORT` | 10,703,962.50 USD | `8,425.00` | `330.91` | `1269.00` | `2145.56` | -7,916,004.73 USD | `-73.95%` | `10X Cross` |
| `195` | `0x9ffd...ce40` | `LONG` | 10,698,270.98 USD | `8,417.87` | `1252.20` | `1269.00` | `597.52` | 157,416.70 USD | `+1.47%` | `5X Cross` |
| `202` | `0xdd53...2b13` | `SHORT` | 10,407,179.22 USD | `8,195.92` | `741.54` | `1269.00` | `8399.91` | -4,329,582.85 USD | `-41.60%` | `3X Cross` |
| `221` | `0x880a...311c` | `SHORT` | 9,789,571.12 USD | `7,707.11` | `1367.50` | `1269.00` | `2232.77` | 749,913.08 USD | `+7.66%` | `10X Cross` |
| `233` | `0xbf73...5d58` | `LONG` | 9,531,750.00 USD | `7,500.00` | `1248.78` | `1269.00` | `117.66` | 165,904.38 USD | `+1.74%` | `10X Cross` |
| `267` | `0x2b61...2f6c` | `LONG` | 8,644,890.00 USD | `6,807.00` | `1453.56` | `1269.00` | `575.15` | -1,249,461.22 USD | `-14.45%` | `10X Cross` |
| `283` | `0x2ae5...83e7` | `LONG` | 8,172,161.28 USD | `6,436.80` | `1391.82` | `1269.00` | `0.000000` | -786,730.71 USD | `-9.63%` | `1X Cross` |
| `311` | `0xecb6...2b00` | `SHORT` | 7,531,384.92 USD | `5,932.56` | `1277.46` | `1269.00` | `6430.35` | 47,214.53 USD | `+0.63%` | `5X Cross` |
| `329` | `0x26b6...9a13` | `LONG` | 6,898,663.61 USD | `5,433.73` | `1282.23` | `1269.00` | `229.61` | -68,639.63 USD | `-0.99%` | `10X Cross` |
| `341` | `0x45d2...4029` | `SHORT` | 6,636,199.20 USD | `5,227.00` | `833.44` | `1269.00` | `8919.87` | -2,279,821.23 USD | `-34.35%` | `5X Cross` |
| `361` | `0xea00...a918` | `LONG` | 6,351,500.00 USD | `5,000.00` | `739.16` | `1269.00` | `0.000000` | 2,655,684.89 USD | `+41.81%` | `5X Cross` |
| `372` | `0xdd7a...8830` | `LONG` | 6,176,815.47 USD | `4,860.19` | `897.48` | `1269.00` | `777.87` | 1,814,911.80 USD | `+29.38%` | `10X Cross` |
| `420` | `0x469e...58a5` | `SHORT` | 5,288,919.46 USD | `4,163.52` | `1242.31` | `1269.00` | `1950.72` | -116,534.80 USD | `-2.20%` | `10X Cross` |
| `421` | `0x4cae...7c34` | `LONG` | 5,273,798.13 USD | `4,152.27` | `1172.97` | `1269.00` | `982.23` | 403,304.58 USD | `+7.65%` | `10X Cross` |
| `441` | `0xd4c1...3d1d` | `SHORT` | 4,989,439.68 USD | `3,930.24` | `1291.66` | `1269.00` | `2325.47` | 87,096.42 USD | `+1.75%` | `10X Cross` |
| `444` | `0xa61c...66b9` | `LONG` | 4,935,816.00 USD | `3,888.00` | `1148.34` | `1269.00` | `0.000000` | 471,073.86 USD | `+9.54%` | `10X Cross` |
| `466` | `0x9aa5...58af` | `SHORT` | 4,722,561.51 USD | `3,720.31` | `1205.51` | `1269.00` | `3651.72` | -237,674.71 USD | `-5.03%` | `10X Cross` |
| `472` | `0x0153...8052` | `SHORT` | 4,694,839.51 USD | `3,698.18` | `1307.82` | `1269.00` | `2504.94` | 141,731.24 USD | `+3.02%` | `1X Isolated` |
| `484` | `0x382b...3e39` | `LONG` | 4,577,766.22 USD | `3,605.96` | `1220.72` | `1269.00` | `0.000000` | 175,904.39 USD | `+3.84%` | `10X Cross` |
| `500` | `0xb122...e4ba` | `LONG` | 4,453,552.31 USD | `3,498.47` | `1265.25` | `1269.00` | `1076.34` | 27,100.78 USD | `+0.61%` | `10X Cross` |
| `539` | `0xd21d...90f1` | `LONG` | 4,129,125.00 USD | `3,250.00` | `1253.64` | `1269.00` | `876.17` | 54,783.27 USD | `+1.33%` | `4X Isolated` |
| `545` | `0x456f...cdf1` | `LONG` | 4,059,446.90 USD | `3,195.66` | `1267.53` | `1269.00` | `508.34` | 8,851.09 USD | `+0.22%` | `10X Cross` |
| `554` | `0x1338...c48e` | `LONG` | 3,998,831.27 USD | `3,149.43` | `1018.52` | `1269.00` | `820.46` | 791,085.73 USD | `+19.78%` | `4X Isolated` |
| `571` | `0xdbe0...d6d5` | `LONG` | 3,916,877.21 USD | `3,085.37` | `422.97` | `1269.00` | `338.78` | 2,611,872.72 USD | `+66.68%` | `3X Isolated` |
| `590` | `0x325e...9564` | `LONG` | 3,809,655.25 USD | `3,000.91` | `1298.07` | `1269.00` | `131.92` | -85,749.92 USD | `-2.25%` | `10X Cross` |
| `593` | `0x9c06...0560` | `SHORT` | 3,797,046.00 USD | `2,989.80` | `786.00` | `1269.00` | `2543.01` | -1,447,051.00 USD | `-38.11%` | `10X Cross` |
| `595` | `0x2e30...4cb5` | `SHORT` | 3,794,890.96 USD | `2,989.28` | `1282.25` | `1269.00` | `2887.56` | 38,112.63 USD | `+1.00%` | `2X Cross` |
| `606` | `0x27c9...d65d` | `SHORT` | 3,729,841.78 USD | `2,938.04` | `1254.41` | `1269.00` | `1723.94` | -44,331.74 USD | `-1.19%` | `10X Cross` |
| `694` | `0xa183...0482` | `LONG` | 3,217,166.40 USD | `2,534.00` | `530.25` | `1269.00` | `444.70` | 1,873,503.68 USD | `+58.23%` | `5X Isolated` |
| `695` | `0xac48...3201` | `LONG` | 3,215,764.45 USD | `2,531.50` | `1378.58` | `1269.00` | `561.73` | -274,107.83 USD | `-8.52%` | `10X Cross` |
| `707` | `0x0871...e927` | `LONG` | 3,174,500.00 USD | `2,500.00` | `1276.50` | `1269.00` | `0.000000` | -16,750.00 USD | `-0.53%` | `10X Cross` |
| `717` | `0x9b86...6e6e` | `LONG` | 3,129,622.65 USD | `2,463.30` | `637.58` | `1269.00` | `882.63` | 1,559,073.37 USD | `+49.82%` | `3X Cross` |
| `792` | `0x71d0...8c26` | `SHORT` | 2,856,746.62 USD | `2,250.47` | `1266.69` | `1269.00` | `3684.27` | -6,097.81 USD | `-0.21%` | `10X Cross` |
| `804` | `0xf48f...10fe` | `LONG` | 2,819,478.94 USD | `2,218.49` | `1517.87` | `1269.00` | `966.09` | -547,907.88 USD | `-19.43%` | `3X Cross` |
| `833` | `0x5bc4...3b0c` | `SHORT` | 2,705,613.65 USD | `2,130.74` | `1089.65` | `1269.00` | `3667.16` | -383,856.07 USD | `-14.19%` | `5X Cross` |
| `845` | `0x8de4...b9aa` | `SHORT` | 2,657,820.46 USD | `2,091.29` | `1331.35` | `1269.00` | `1690.07` | 126,419.24 USD | `+4.76%` | `3X Cross` |
| `853` | `0x4fe2...ac59` | `SHORT` | 2,637,108.61 USD | `2,071.57` | `1478.56` | `1269.00` | `1830.56` | 425,837.60 USD | `+16.15%` | `10X Cross` |
| `861` | `0xdf57...93f5` | `LONG` | 2,608,613.63 USD | `2,054.35` | `1227.36` | `1269.00` | `897.41` | 87,191.59 USD | `+3.34%` | `4X Isolated` |
| `868` | `0xbcd4...0dd2` | `LONG` | 2,584,095.36 USD | `2,033.92` | `1228.20` | `1269.00` | `801.92` | 86,044.55 USD | `+3.33%` | `10X Cross` |
| `874` | `0x9a99...d21a` | `LONG` | 2,546,600.00 USD | `2,000.00` | `1278.44` | `1269.00` | `0.000000` | -10,273.67 USD | `-0.40%` | `10X Cross` |
| `875` | `0xf29c...9971` | `LONG` | 2,539,200.00 USD | `2,000.00` | `1254.95` | `1269.00` | `0.000000` | 29,302.93 USD | `+1.15%` | `10X Cross` |
| `895` | `0x77ee...2902` | `SHORT` | 2,477,880.00 USD | `1,946.03` | `759.84` | `1269.00` | `5677.26` | -999,202.49 USD | `-40.32%` | `10X Cross` |
| `910` | `0x3e2f...b269` | `SHORT` | 2,445,012.60 USD | `1,925.51` | `1134.87` | `1269.00` | `2977.34` | -259,813.74 USD | `-10.63%` | `10X Cross` |
| `922` | `0x4f12...618b` | `SHORT` | 2,409,982.25 USD | `1,896.28` | `1608.30` | `1269.00` | `2116.96` | 639,802.14 USD | `+26.55%` | `3X Cross` |
| `935` | `0x039c...0ebd` | `SHORT` | 2,364,029.01 USD | `1,862.32` | `1250.00` | `1269.00` | `3307.86` | -36,127.02 USD | `-1.53%` | `10X Cross` |
| `966` | `0x866d...d6e1` | `LONG` | 2,288,783.71 USD | `1,802.05` | `674.73` | `1269.00` | `117.43` | 1,072,882.39 USD | `+46.88%` | `10X Cross` |
| `987` | `0x2309...a2d9` | `LONG` | 2,228,396.05 USD | `1,750.37` | `1186.09` | `1269.00` | `808.32` | 152,301.94 USD | `+6.83%` | `8X Cross` |
| `1009` | `0x5323...b23c` | `SHORT` | 2,150,664.31 USD | `1,693.97` | `1263.89` | `1269.00` | `4495.64` | -9,677.72 USD | `-0.45%` | `5X Cross` |
| `1020` | `0x265e...7f70` | `LONG` | 2,102,169.50 USD | `1,651.74` | `1382.98` | `1269.00` | `0.000000` | -182,153.26 USD | `-8.67%` | `3X Cross` |
| `1024` | `0xfe7c...b7ae` | `SHORT` | 2,085,331.48 USD | `1,642.64` | `1346.92` | `1269.00` | `5602.91` | 127,177.14 USD | `+6.10%` | `10X Cross` |
| `1031` | `0x3e47...aaf6` | `LONG` | 2,078,893.74 USD | `1,636.28` | `1278.38` | `1269.00` | `1046.54` | -12,898.05 USD | `-0.62%` | `10X Cross` |
| `1035` | `0x2edd...8179` | `SHORT` | 2,076,876.61 USD | `1,635.98` | `1261.55` | `1269.00` | `2850.78` | -13,013.73 USD | `-0.63%` | `10X Cross` |
| `1049` | `0x7f75...9edf` | `LONG` | 2,049,402.50 USD | `1,612.56` | `1200.27` | `1269.00` | `987.88` | 113,888.58 USD | `+5.56%` | `10X Cross` |
| `1064` | `0xfc27...9d9d` | `SHORT` | 2,037,250.94 USD | `1,604.64` | `1295.09` | `1269.00` | `12766.53` | 40,894.86 USD | `+2.01%` | `10X Cross` |
| `1068` | `0x6646...6de5` | `SHORT` | 2,031,200.00 USD | `1,600.00` | `660.64` | `1269.00` | `4311.90` | -974,175.03 USD | `-47.96%` | `10X Cross` |
| `1074` | `0x023a...2355` | `SHORT` | 2,020,168.04 USD | `1,591.31` | `1310.00` | `1269.00` | `4410.00` | 64,441.21 USD | `+3.19%` | `10X Cross` |
| `1088` | `0xab59...59b5` | `LONG` | 1,989,264.69 USD | `1,565.32` | `1342.15` | `1269.00` | `833.73` | -111,630.52 USD | `-5.61%` | `10X Cross` |
| `1119` | `0x3205...40bb` | `SHORT` | 1,948,123.92 USD | `1,534.56` | `1259.67` | `1269.00` | `2206.85` | -15,080.42 USD | `-0.77%` | `10X Cross` |
| `1152` | `0xcf67...eb24` | `LONG` | 1,906,350.00 USD | `1,500.00` | `887.05` | `1269.00` | `608.91` | 575,778.63 USD | `+30.20%` | `10X Cross` |
| `1169` | `0x7277...0b98` | `SHORT` | 1,873,881.95 USD | `1,475.73` | `1287.86` | `1269.00` | `2175.79` | 26,650.17 USD | `+1.42%` | `10X Cross` |
| `1235` | `0x926a...af36` | `LONG` | 1,779,432.76 USD | `1,401.68` | `1254.50` | `1269.00` | `1187.92` | 21,030.86 USD | `+1.18%` | `10X Isolated` |
| `1236` | `0x2ab7...c2f8` | `LONG` | 1,778,087.50 USD | `1,400.51` | `813.26` | `1269.00` | `790.19` | 639,105.81 USD | `+35.94%` | `3X Cross` |
| `1256` | `0x11be...8b1d` | `LONG` | 1,747,716.85 USD | `1,375.83` | `1206.55` | `1269.00` | `1134.68` | 87,708.89 USD | `+5.02%` | `10X Isolated` |
| `1307` | `0xef96...9383` | `SHORT` | 1,647,036.60 USD | `1,297.39` | `1262.03` | `1269.00` | `3885.62` | -9,694.66 USD | `-0.59%` | `10X Cross` |
| `1331` | `0xdf83...3cff` | `SHORT` | 1,625,073.19 USD | `1,280.19` | `1260.37` | `1269.00` | `1884.94` | -11,556.86 USD | `-0.71%` | `10X Cross` |
| `1336` | `0xe065...0f85` | `SHORT` | 1,604,651.05 USD | `1,262.61` | `1087.02` | `1269.00` | `1547.23` | -232,174.92 USD | `-14.47%` | `10X Cross` |
| `1347` | `0x413c...886c` | `LONG` | 1,588,125.00 USD | `1,250.00` | `1237.51` | `1269.00` | `0.000000` | 41,235.54 USD | `+2.60%` | `10X Cross` |
| `1401` | `0x2847...d47b` | `LONG` | 1,538,871.70 USD | `1,211.71` | `1232.45` | `1269.00` | `0.000000` | 45,504.10 USD | `+2.96%` | `5X Cross` |
| `1415` | `0x5975...9abd` | `LONG` | 1,524,360.00 USD | `1,200.00` | `1179.54` | `1269.00` | `523.24` | 108,917.21 USD | `+7.15%` | `5X Cross` |
| `1417` | `0x266b...efcb` | `LONG` | 1,523,400.00 USD | `1,200.00` | `893.76` | `1269.00` | `394.29` | 450,890.30 USD | `+29.60%` | `10X Cross` |
| `1445` | `0xb897...ebc1` | `SHORT` | 1,489,951.78 USD | `1,173.56` | `1256.04` | `1269.00` | `1365.84` | -15,908.49 USD | `-1.07%` | `10X Cross` |
| `1455` | `0x69cc...14fd` | `SHORT` | 1,474,694.93 USD | `1,161.36` | `675.33` | `1269.00` | `7991.98` | -690,389.40 USD | `-46.82%` | `10X Cross` |
| `1464` | `0x3fc5...c0c1` | `SHORT` | 1,459,093.02 USD | `1,148.44` | `1264.34` | `1269.00` | `2724.81` | -7,079.24 USD | `-0.49%` | `10X Cross` |
| `1510` | `0x5f94...4b96` | `LONG` | 1,416,950.53 USD | `1,115.27` | `538.00` | `1269.00` | `0.000000` | 816,932.90 USD | `+57.65%` | `10X Cross` |
| `1516` | `0xe35c...a1d3` | `LONG` | 1,410,871.52 USD | `1,111.36` | `1311.66` | `1269.00` | `690.98` | -46,852.62 USD | `-3.32%` | `2X Isolated` |
| `1538` | `0x71df...a23d` | `SHORT` | 1,395,035.26 USD | `1,098.28` | `513.50` | `1269.00` | `2559.18` | -831,065.07 USD | `-59.57%` | `2X Cross` |
| `1566` | `0xbfc7...80b4` | `SHORT` | 1,365,572.50 USD | `1,075.00` | `558.03` | `1269.00` | `2660.94` | -765,693.77 USD | `-56.07%` | `10X Cross` |
| `1583` | `0x8b9d...7b28` | `SHORT` | 1,338,772.71 USD | `1,054.65` | `1272.24` | `1269.00` | `3369.59` | 2,999.10 USD | `+0.22%` | `10X Cross` |
| `1593` | `0x123d...3bff` | `SHORT` | 1,326,625.10 USD | `1,044.34` | `519.62` | `1269.00` | `4143.72` | -783,966.89 USD | `-59.09%` | `10X Cross` |
| `1646` | `0x668c...ea2e` | `SHORT` | 1,273,100.00 USD | `1,000.00` | `1406.98` | `1269.00` | `4212.47` | 133,881.99 USD | `+10.52%` | `10X Cross` |
| `1650` | `0xe282...df29` | `LONG` | 1,270,800.00 USD | `1,000.00` | `420.99` | `1269.00` | `799.12` | 849,813.14 USD | `+66.87%` | `10X Cross` |
| `1675` | `0x17f0...094f` | `LONG` | 1,250,159.43 USD | `984.30` | `1287.23` | `1269.00` | `537.03` | -16,860.73 USD | `-1.35%` | `5X Cross` |
| `1695` | `0x51f6...2b39` | `SHORT` | 1,235,079.58 USD | `972.81` | `1299.77` | `1269.00` | `2513.26` | 29,348.13 USD | `+2.38%` | `10X Cross` |
| `1731` | `0x38f9...cb04` | `SHORT` | 1,199,659.16 USD | `945.06` | `1253.73` | `1269.00` | `2171.95` | -14,810.36 USD | `-1.23%` | `10X Cross` |
| `1739` | `0xf096...7553` | `SHORT` | 1,189,813.49 USD | `937.23` | `1257.91` | `1269.00` | `3098.82` | -10,860.47 USD | `-0.91%` | `10X Cross` |
| `1758` | `0x757d...94ba` | `LONG` | 1,174,565.00 USD | `925.00` | `1558.31` | `1269.00` | `0.000000` | -266,875.59 USD | `-22.72%` | `10X Cross` |
| `1807` | `0xb911...5525` | `LONG` | 1,143,270.00 USD | `900.00` | `1294.82` | `1269.00` | `1035.46` | -22,067.82 USD | `-1.93%` | `10X Cross` |
| `1852` | `0xcf0a...856f` | `LONG` | 1,109,496.64 USD | `871.15` | `1292.19` | `1269.00` | `1024.61` | -16,198.21 USD | `-1.46%` | `4X Cross` |
| `1861` | `0x4e23...20c3` | `LONG` | 1,102,795.90 USD | `868.48` | `1264.99` | `1269.00` | `0.000000` | 4,180.34 USD | `+0.38%` | `4X Cross` |
| `1880` | `0xdf95...7d72` | `SHORT` | 1,083,115.55 USD | `853.25` | `1074.39` | `1269.00` | `44652.46` | -166,389.60 USD | `-15.36%` | `10X Cross` |
| `1906` | `0xb2f7...af9f` | `SHORT` | 1,055,429.76 USD | `830.72` | `746.63` | `1269.00` | `8165.27` | -435,190.73 USD | `-41.23%` | `10X Cross` |
| `1920` | `0x601c...4f54` | `SHORT` | 1,047,095.84 USD | `824.42` | `615.11` | `1269.00` | `3123.57` | -539,983.09 USD | `-51.57%` | `5X Cross` |
| `1928` | `0x8b61...c0c2` | `LONG` | 1,039,638.93 USD | `818.42` | `1274.67` | `1269.00` | `1005.18` | -3,575.11 USD | `-0.34%` | `4X Isolated` |
| `1935` | `0xae55...2236` | `LONG` | 1,037,859.91 USD | `817.47` | `1467.80` | `1269.00` | `0.000000` | -162,021.30 USD | `-15.61%` | `10X Cross` |
| `1969` | `0x0f02...5384` | `LONG` | 1,016,830.44 USD | `800.78` | `1290.36` | `1269.00` | `298.01` | -16,463.62 USD | `-1.62%` | `3X Cross` |
| `1971` | `0x9b0f...db40` | `LONG` | 1,015,600.00 USD | `800.00` | `1268.86` | `1269.00` | `799.48` | 510.24 USD | `+0.05%` | `10X Cross` |
| `1986` | `0x6e8f...4364` | `LONG` | 1,008,649.79 USD | `793.65` | `1260.00` | `1269.00` | `894.98` | 8,650.78 USD | `+0.86%` | `10X Cross` |
| `1988` | `0xabdb...84ac` | `LONG` | 1,008,224.41 USD | `793.69` | `711.79` | `1269.00` | `664.60` | 443,284.05 USD | `+43.97%` | `3X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `1239.10` | 2,007.34 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 2.01K USD at 1239.1000 USD [API] | `2026-10-29 02:30:54` |
| `ANNOUNCEMENT` | `INFO` | `1266.30` | 7,990.35 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Long: 7.99K USD at 1266.3000 USD [API] | `2026-10-29 10:49:57` |
| `ANNOUNCEMENT` | `INFO` | `1238.40` | 3,987.65 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 3.99K USD at 1238.4000 USD [API] | `2026-10-29 02:30:57` |
| `ANNOUNCEMENT` | `INFO` | `1239.00` | 3,989.58 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 3.99K USD at 1239.0000 USD [API] | `2026-10-29 02:30:54` |
| `ANNOUNCEMENT` | `INFO` | `1248.40` | 37.45 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 0.04K USD at 1248.4000 USD [API] | `2026-10-29 02:05:52` |
| `ANNOUNCEMENT` | `INFO` | `1087.00` | 239.14 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Long: 0.24K USD at 1087.0000 USD [API] | `2026-10-15 02:24:27` |
| `ANNOUNCEMENT` | `INFO` | `1017.00` | 10.17 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Long: 0.01K USD at 1017.0000 USD [API] | `2026-09-04 08:53:37` |
| `ANNOUNCEMENT` | `INFO` | `1327.50` | 13.28 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Long: 0.01K USD at 1327.5000 USD [API] | `2026-10-29 15:31:54` |
| `ANNOUNCEMENT` | `INFO` | `1327.50` | 61,343.78 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Long: 61.34K USD at 1327.5000 USD [API] | `2026-10-29 15:31:54` |
| `ANNOUNCEMENT` | `INFO` | `1319.10` | 10,420.89 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 10.42K USD at 1319.1000 USD [API] | `2026-10-29 18:31:05` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`1404.55` (Vol: 3,000,000.00 USD, Dist: `+11.24%`) | Long MP=`1176.48` (Vol: 3,400,000.00 USD, Dist: `--6.82%`)
  * 48H Horizon: Short MP=`1404.55` (Vol: 3,000,000.00 USD, Dist: `+11.24%`) | Long MP=`1176.48` (Vol: 3,400,000.00 USD, Dist: `--6.82%`)
  * 3D Horizon: Short MP=`1404.55` (Vol: 3,000,000.00 USD, Dist: `+11.24%`) | Long MP=`1176.48` (Vol: 3,400,000.00 USD, Dist: `--6.82%`)
  * 7D Horizon: Short MP=`1404.10` (Vol: 3,000,000.00 USD, Dist: `+11.21%`) | Long MP=`1176.74` (Vol: 4,900,000.00 USD, Dist: `--6.80%`)
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
| `5m` | `BALANCED` | 0.00 USD | 1,750.00 USD | 1,750.00 USD | 1,750.00 USD | `1` | `2026-10-30 10:50:00 UTC - 2026-10-30 10:55:00 UTC` |
| `15m` | `BALANCED` | 0.00 USD | 1,750.00 USD | 1,750.00 USD | 1,750.00 USD | `1` | `2026-10-30 10:45:00 UTC - 2026-10-30 11:00:00 UTC` |
| `1h` | `BALANCED` | 0.00 USD | 1,750.00 USD | 1,750.00 USD | 1,750.00 USD | `1` | `2026-10-30 10:00:00 UTC - 2026-10-30 11:00:00 UTC` |
| `4h` | `BALANCED` | 0.00 USD | 1,750.00 USD | 1,750.00 USD | 1,750.00 USD | `1` | `2026-10-30 08:00:00 UTC - 2026-10-30 12:00:00 UTC` |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `0 USD` | Total OI Tokens: `-`
  * 1h OI Change: `0.00%` | 4h OI Change: `0.00%` | 24h OI Change: `0.00%`
  * Exchange Breakdown: Binance=`-` | Bybit=`-` | OKX=`-` | Hyperliquid=`-`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `85.69K` | Last 24h: `171.90K` | Last 3d: `285.15K` | Last 7d: `847.79K`
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
| `0:00 UTC` | `1249.95` | `1249.10` | `1249.95` | `1253.55` | `1244.55` | 10,263,783.49 USD | 5,117,369.60 USD | 5,146,413.89 USD | -29,044.29 USD | `-0.28%` | `1B / 4S` |
| `5:00 UTC` | `1246.65` | `1246.77` | `1246.65` | `1252.35` | `1243.95` | 13,017,000.97 USD | 7,727,648.32 USD | 5,289,352.64 USD | 2,438,295.68 USD | `+18.73%` | `8B / 5S` |
| `0:00 UTC` | `1244.55` | `1245.81` | `1244.55` | `1249.05` | `1243.65` | 9,717,386.64 USD | 3,914,194.68 USD | 5,803,191.96 USD | -1,888,997.28 USD | `-19.44%` | `0B / 1S` |
| `5:00 UTC` | `1242.15` | `1244.40` | `1242.15` | `1249.35` | `1241.25` | 8,638,502.97 USD | 4,533,952.89 USD | 4,104,550.08 USD | 429,402.82 USD | `+4.97%` | `4B / 2S` |
| `0:00 UTC` | `1251.15` | `1247.35` | `1251.15` | `1251.75` | `1240.05` | 9,977,652.60 USD | 4,992,881.35 USD | 4,984,771.25 USD | 8,110.10 USD | `+0.08%` | `3B / 5S` |
| `5:00 UTC` | `1243.95` | `1249.40` | `1243.95` | `1256.55` | `1243.35` | 15,678,426.53 USD | 9,268,825.46 USD | 6,409,601.07 USD | 2,859,224.38 USD | `+18.24%` | `10B / 2S` |
| `0:00 UTC` | `1249.95` | `1250.19` | `1249.95` | `1256.25` | `1246.35` | 11,248,393.80 USD | 4,953,252.73 USD | 6,295,141.07 USD | -1,341,888.34 USD | `-11.93%` | `1B / 7S` |
| `5:00 UTC` | `1263.15` | `1259.85` | `1263.15` | `1266.15` | `1247.85` | 19,587,954.68 USD | 10,529,516.42 USD | 9,058,438.26 USD | 1,471,078.16 USD | `+7.51%` | `10B / 4S` |
| `0:00 UTC` | `1272.15` | `1270.75` | `1272.15` | `1276.65` | `1262.25` | 28,700,563.02 USD | 14,735,645.79 USD | 13,964,917.22 USD | 770,728.57 USD | `+2.69%` | `10B / 0S` |
| `5:00 UTC` | `1261.95` | `1263.12` | `1261.95` | `1268.85` | `1260.45` | 6,720,404.83 USD | 3,122,310.34 USD | 3,598,094.49 USD | -475,784.15 USD | `-7.08%` | `1B / 8S` |

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
| `5m` | -244,630.00 USD | -787,770.00 USD | **`DISTRIBUTION`** |
| `15m` | -753,410.00 USD | -2,980,000.00 USD | **`DISTRIBUTION`** |
| `30m` | -482,040.00 USD | 4,080,000.00 USD | **`ACCUMULATION`** |
| `1h` | -828,510.00 USD | 5,640,000.00 USD | **`ACCUMULATION`** |
| `2h` | -3,280,000.00 USD | 9,270,000.00 USD | **`ACCUMULATION`** |
| `4h` | -513,350.00 USD | -10,400,000.00 USD | **`DISTRIBUTION`** |
| `6h` | -1,300,000.00 USD | -23,360,000.00 USD | **`DISTRIBUTION`** |
| `8h` | -1,650,000.00 USD | -3,380,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -940,970.00 USD | -14,770,000.00 USD | **`DISTRIBUTION`** |
| `24h` | 20,650,000.00 USD | 73,530,000.00 USD | **`ACCUMULATION`** |
| `1w` | 35,510,000.00 USD | 226,770,000.00 USD | **`ACCUMULATION`** |
| `30d` | 62,110,000.00 USD | -568,170,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-244.63K` | 15m=`-753.41K` | 1h=`-828.51K` | 24h=`+20.65M`
* Futures Capital Netflows: 5m=`-787.77K` | 15m=`-2.98M` | 1h=`+5.64M` | 24h=`+73.53M`
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
  * `2026-10-30 15:50:15 IST`: [istat.it] - (Sentiment: `Neutral`)
  * `2026-10-30 15:33:15 IST`: [ec.europa.eu] - (Sentiment: `Neutral`)
  * `2026-10-30 15:32:15 IST`: [ec.europa.eu] - (Sentiment: `Neutral`)
  * `2026-10-30 16:18:15 IST`: [dailyforex.com] - (Sentiment: `Neutral`)
  * `2026-10-30 16:18:15 IST`: [breakingthenews.net] - (Sentiment: `Neutral`)
  * `2026-10-30 16:18:15 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 16:18:15 IST`: [@FirstSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 16:18:15 IST`: [destatis.de] - (Sentiment: `Neutral`)
  * `2026-10-30 16:18:15 IST`: [istat.it] - (Sentiment: `Neutral`)
  * `2026-10-30 16:17:15 IST`: [channelnewsasia.com] - (Sentiment: `Neutral`)
  * `2026-10-30 16:17:15 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 16:17:15 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 16:17:15 IST`: [kof.ethz.ch] - (Sentiment: `Neutral`)
  * `2026-10-30 16:17:15 IST`: [gerlachmacro.substack.com] - (Sentiment: `Neutral`)
  * `2026-10-30 16:17:15 IST`: [@financialjuice] - (Sentiment: `Neutral`)


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
  * Execution Entry: `1239.95` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `1234.51` (Risk Distance: `5.44` pts)
  * +2.5R Take Profit: `1253.54`
  * Mathematical Lot Sizing: **`1.83 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `1279.38` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `1284.82` (Risk Distance: `5.44` pts)
  * +2.5R Take Profit: `1265.79`
  * Mathematical Lot Sizing: **`1.83 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`1272.05`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
