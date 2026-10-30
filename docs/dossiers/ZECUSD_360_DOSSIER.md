# 🏛️ SOVEREIGN CANDIDATE DOSSIER: ZECUSD
**Canonical Key**: `ZECUSD` | **Broker Instrument**: `ZECUSD.p` | **Asset Class**: `Crypto Altcoin`
**Timestamp**: `2026-10-30 09:19:10 IST` (`2026-10-30 03:49:10 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `1282.88` | **Live Ask Quote**: `1284.74` | **Mid Price**: `1283.81`
- **Spread Points**: `186.00` | **Spread BPS**: `14.49 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `1236.66` | VWAP Z-Score: `+1.80` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `20.24` (Volatility Regime: `HIGH_EXPANSION`)
  * 14-Period RSI: `56.05` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `1294.56` | Lower -3.00σ Band: `1178.76`
  * Upper +2.51σ Band: `1285.11` | Lower -2.51σ Band: `1188.22`
  * Upper +2.01σ Band: `1275.46` | Lower -2.01σ Band: `1197.87`
  * Upper +2.00σ Band: `1275.26` | Lower -2.00σ Band: `1198.06`
  * Upper +1.28σ Band: `1261.37` | Lower -1.28σ Band: `1211.96`
  * Upper +1.00σ Band: `1255.96` | Lower -1.00σ Band: `1217.36`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`1254.72` | EMA-20=`1251.83` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`1264.25` (Slope: `+0.0000`) | EMA-100=`1271.81`
  * Institutional Anchors: EMA-144=`1273.37` | EMA-200=`1274.19` (Slope: `-0.2825`) | EMA-233=`1276.95`
- **Range Boundaries**: 24H High=`1396.49` | 24H Low=`1180.03` | Weekly High=`1396.49` | Weekly Low=`1180.03`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `1263.91` (Distance: `+1.35%`)
  * Point of Control (POC) = `1229.90` (Distance: `+4.16%`)
  * Value Area Low (VAL) = `1222.17` (Distance: `+4.81%`)
  * Auction Positioning: `ABOVE_VALUE (Imbalance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `RANGE_EXPANSION`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`1309.91` | POC=`1246.71` | VAL=`1230.27`
  * Prior Day Extremes: PDH=`1396.49` | PDL=`1206.89` | PDC=`1244.38`
  * Monday Range Blueprint: High=`1267.53` | Mid=`1222.14` | Low=`1176.75`
  * Developing Weekly Value Area: Weekly VAH=`1296.14` | Weekly POC=`1239.01` | Weekly VAL=`1200.92`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`1296.00` | Low=`1180.03`
  * London Session (08:00-16:00 UTC): High=`1288.95` | Low=`1278.67`
  * New York Session (13:00-21:00 UTC): High=`1291.51` | Low=`1276.11`
  * Initial Balance (First Hour): IB High=`1287.66` | IB Low=`1279.96`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `1278.67` - `1288.95`
  * Optimal Trade Entry (OTE 0.705): `1286.38`
  * Structural Invalidation Anchor (0.786): `1294.08`

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
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 09:07:15 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `13` | `0xb83d...6e36` | `SHORT` | 67,095,309.98 USD | `52,385.47` | `1336.45` | `1282.20` | `3753.47` | 2,915,257.42 USD | `+4.34%` | `3X Cross` |
| `22` | `0x5b5d...c060` | `SHORT` | 51,363,390.68 USD | `40,121.38` | `1478.36` | `1282.20` | `5217.23` | 7,950,644.44 USD | `+15.48%` | `3X Cross` |
| `39` | `0x7fda...17d1` | `SHORT` | 31,849,473.12 USD | `24,820.35` | `1261.64` | `1282.20` | `2705.50` | -535,138.01 USD | `-1.68%` | `5X Cross` |
| `78` | `0x60b0...991e` | `LONG` | 21,535,118.32 USD | `16,779.74` | `1179.65` | `1282.20` | `933.48` | 1,740,871.30 USD | `+8.08%` | `10X Cross` |
| `135` | `0xc36a...105b` | `LONG` | 14,754,569.08 USD | `11,510.82` | `1215.14` | `1282.20` | `969.03` | 767,288.05 USD | `+5.20%` | `10X Cross` |
| `150` | `0x9071...5c0b` | `LONG` | 13,486,183.19 USD | `10,517.29` | `1353.83` | `1282.20` | `0.1126` | -752,435.68 USD | `-5.58%` | `1X Cross` |
| `169` | `0x8742...8427` | `LONG` | 11,809,753.04 USD | `9,201.21` | `1286.37` | `1282.20` | `707.24` | -26,416.96 USD | `-0.22%` | `10X Cross` |
| `185` | `0x58b2...11f3` | `LONG` | 10,962,507.25 USD | `8,563.08` | `1246.56` | `1282.20` | `381.75` | 288,089.68 USD | `+2.63%` | `10X Cross` |
| `189` | `0xad59...ba81` | `SHORT` | 10,810,960.00 USD | `8,425.00` | `330.91` | `1282.20` | `2144.93` | -8,023,002.23 USD | `-74.21%` | `10X Cross` |
| `193` | `0x9ffd...ce40` | `LONG` | 10,711,651.03 USD | `8,367.17` | `1250.94` | `1282.20` | `595.79` | 244,796.90 USD | `+2.29%` | `5X Cross` |
| `200` | `0xdd53...2b13` | `SHORT` | 10,514,545.77 USD | `8,195.92` | `741.54` | `1282.20` | `8707.75` | -4,436,949.40 USD | `-42.20%` | `3X Cross` |
| `216` | `0x880a...311c` | `SHORT` | 9,893,617.11 USD | `7,707.11` | `1367.50` | `1282.20` | `2245.10` | 645,867.10 USD | `+6.53%` | `10X Cross` |
| `230` | `0xbf73...5d58` | `LONG` | 9,601,500.00 USD | `7,500.00` | `1248.78` | `1282.20` | `126.10` | 235,654.38 USD | `+2.45%` | `10X Cross` |
| `262` | `0x2b61...2f6c` | `LONG` | 8,735,423.10 USD | `6,807.00` | `1453.56` | `1282.20` | `552.60` | -1,158,928.12 USD | `-13.27%` | `10X Cross` |
| `279` | `0x2ae5...83e7` | `LONG` | 8,253,824.32 USD | `6,436.80` | `1391.82` | `1282.20` | `0.000000` | -705,067.67 USD | `-8.54%` | `1X Cross` |
| `326` | `0x26b6...9a13` | `LONG` | 6,969,845.47 USD | `5,433.73` | `1282.23` | `1282.20` | `224.61` | 2,542.24 USD | `+0.04%` | `10X Cross` |
| `332` | `0x45d2...4029` | `SHORT` | 6,702,513.63 USD | `5,227.00` | `833.44` | `1282.20` | `9098.22` | -2,346,135.65 USD | `-35.00%` | `5X Cross` |
| `356` | `0xea00...a918` | `LONG` | 6,401,030.50 USD | `5,000.00` | `739.16` | `1282.20` | `0.000000` | 2,705,215.39 USD | `+42.26%` | `5X Cross` |
| `364` | `0xdd7a...8830` | `LONG` | 6,239,025.90 USD | `4,860.19` | `897.48` | `1282.20` | `784.66` | 1,877,122.23 USD | `+30.09%` | `10X Cross` |
| `367` | `0xecb6...2b00` | `SHORT` | 6,222,399.22 USD | `4,852.53` | `1278.81` | `1282.20` | `6801.71` | -16,954.54 USD | `-0.27%` | `5X Cross` |
| `412` | `0x469e...58a5` | `SHORT` | 5,330,138.30 USD | `4,163.52` | `1242.31` | `1282.20` | `1971.62` | -157,753.65 USD | `-2.96%` | `10X Cross` |
| `435` | `0xa61c...66b9` | `LONG` | 4,989,859.20 USD | `3,888.00` | `1148.34` | `1282.20` | `0.000000` | 525,117.06 USD | `+10.52%` | `10X Cross` |
| `451` | `0x4cae...7c34` | `LONG` | 4,864,630.62 USD | `3,800.27` | `1154.34` | `1282.20` | `965.68` | 477,827.75 USD | `+9.82%` | `10X Cross` |
| `460` | `0x9aa5...58af` | `SHORT` | 4,773,901.79 USD | `3,720.31` | `1205.51` | `1282.20` | `3701.67` | -289,014.99 USD | `-6.05%` | `10X Cross` |
| `462` | `0x0153...8052` | `SHORT` | 4,745,134.76 USD | `3,698.18` | `1307.82` | `1282.20` | `2504.82` | 91,435.99 USD | `+1.93%` | `1X Isolated` |
| `523` | `0x382b...3e39` | `LONG` | 4,236,398.62 USD | `3,303.75` | `1215.08` | `1282.20` | `0.000000` | 222,079.24 USD | `+5.24%` | `10X Cross` |
| `531` | `0xd21d...90f1` | `LONG` | 4,170,400.00 USD | `3,250.00` | `1253.64` | `1282.20` | `876.03` | 96,058.27 USD | `+2.30%` | `4X Isolated` |
| `535` | `0xd4c1...3d1d` | `SHORT` | 4,147,432.65 USD | `3,234.37` | `1294.38` | `1282.20` | `2606.42` | 39,057.22 USD | `+0.94%` | `10X Cross` |
| `539` | `0x456f...cdf1` | `LONG` | 4,122,079.49 USD | `3,219.62` | `1267.51` | `1282.20` | `515.00` | 41,172.85 USD | `+1.00%` | `10X Cross` |
| `547` | `0x1338...c48e` | `LONG` | 4,039,143.98 USD | `3,149.43` | `1018.52` | `1282.20` | `820.32` | 831,398.43 USD | `+20.58%` | `4X Isolated` |
| `557` | `0x325e...9564` | `LONG` | 3,980,991.29 USD | `3,101.91` | `1298.07` | `1282.20` | `175.58` | -45,519.40 USD | `-1.14%` | `10X Cross` |
| `560` | `0xdbe0...d6d5` | `LONG` | 3,956,678.49 USD | `3,085.37` | `422.97` | `1282.20` | `338.64` | 2,651,674.00 USD | `+67.02%` | `3X Isolated` |
| `586` | `0x9c06...0560` | `SHORT` | 3,827,541.96 USD | `2,989.80` | `786.00` | `1282.20` | `2589.95` | -1,477,546.96 USD | `-38.60%` | `10X Cross` |
| `589` | `0x27c9...d65d` | `SHORT` | 3,801,276.79 USD | `2,961.88` | `1254.41` | `1282.20` | `1725.44` | -85,861.59 USD | `-2.26%` | `10X Cross` |
| `591` | `0x2e30...4cb5` | `SHORT` | 3,794,495.12 USD | `2,960.89` | `1287.96` | `1282.20` | `2901.49` | 19,012.71 USD | `+0.50%` | `2X Cross` |
| `637` | `0x5323...b23c` | `SHORT` | 3,472,788.32 USD | `2,706.35` | `1261.08` | `1282.20` | `3275.17` | -59,851.22 USD | `-1.72%` | `5X Cross` |
| `681` | `0xa183...0482` | `LONG` | 3,252,389.00 USD | `2,534.00` | `530.25` | `1282.20` | `444.56` | 1,908,726.28 USD | `+58.69%` | `5X Isolated` |
| `683` | `0xac48...3201` | `LONG` | 3,240,841.74 USD | `2,531.50` | `1378.58` | `1282.20` | `518.62` | -249,030.54 USD | `-7.68%` | `10X Cross` |
| `694` | `0x0871...e927` | `LONG` | 3,208,000.00 USD | `2,500.00` | `1276.50` | `1282.20` | `0.000000` | 16,750.00 USD | `+0.52%` | `10X Cross` |
| `708` | `0x9b86...6e6e` | `LONG` | 3,153,762.99 USD | `2,463.30` | `637.58` | `1282.20` | `882.49` | 1,583,213.71 USD | `+50.20%` | `3X Cross` |
| `728` | `0x71d0...8c26` | `SHORT` | 3,097,485.90 USD | `2,413.50` | `1262.25` | `1282.20` | `3767.47` | -51,036.95 USD | `-1.65%` | `10X Cross` |
| `765` | `0xb2f7...af9f` | `SHORT` | 2,962,487.09 USD | `2,313.72` | `746.63` | `1282.20` | `4490.29` | -1,234,998.34 USD | `-41.69%` | `10X Cross` |
| `782` | `0x413c...886c` | `LONG` | 2,880,675.00 USD | `2,250.00` | `1237.51` | `1282.20` | `0.000000` | 96,273.97 USD | `+3.34%` | `10X Cross` |
| `784` | `0xb122...e4ba` | `LONG` | 2,879,205.23 USD | `2,243.42` | `1258.05` | `1282.20` | `1002.66` | 56,871.30 USD | `+1.98%` | `10X Cross` |
| `798` | `0xf48f...10fe` | `LONG` | 2,846,766.37 USD | `2,218.49` | `1517.87` | `1282.20` | `992.73` | -520,620.46 USD | `-18.29%` | `3X Cross` |
| `833` | `0x5bc4...3b0c` | `SHORT` | 2,734,804.79 USD | `2,130.74` | `1089.65` | `1282.20` | `3707.02` | -413,047.21 USD | `-15.10%` | `5X Cross` |
| `851` | `0x8de4...b9aa` | `SHORT` | 2,677,282.21 USD | `2,091.29` | `1331.35` | `1282.20` | `1689.94` | 106,957.49 USD | `+4.00%` | `3X Cross` |
| `860` | `0x4fe2...ac59` | `SHORT` | 2,652,036.55 USD | `2,071.57` | `1478.56` | `1282.20` | `1837.94` | 410,909.66 USD | `+15.49%` | `10X Cross` |
| `866` | `0xdf57...93f5` | `LONG` | 2,635,525.62 USD | `2,054.35` | `1227.36` | `1282.20` | `897.27` | 114,103.57 USD | `+4.33%` | `4X Isolated` |
| `877` | `0xbcd4...0dd2` | `LONG` | 2,609,926.14 USD | `2,033.92` | `1228.20` | `1282.20` | `717.01` | 111,875.33 USD | `+4.29%` | `10X Cross` |
| `885` | `0xf29c...9971` | `LONG` | 2,567,000.00 USD | `2,000.00` | `1254.95` | `1282.20` | `0.000000` | 57,102.93 USD | `+2.22%` | `10X Cross` |
| `886` | `0x9a99...d21a` | `LONG` | 2,566,800.00 USD | `2,000.00` | `1278.44` | `1282.20` | `0.000000` | 9,926.33 USD | `+0.39%` | `10X Cross` |
| `910` | `0x77ee...2902` | `SHORT` | 2,497,145.70 USD | `1,946.03` | `759.84` | `1282.20` | `5456.13` | -1,018,468.19 USD | `-40.79%` | `10X Cross` |
| `920` | `0x3e2f...b269` | `SHORT` | 2,470,236.78 USD | `1,925.51` | `1134.87` | `1282.20` | `2931.87` | -285,037.92 USD | `-11.54%` | `10X Cross` |
| `931` | `0x4f12...618b` | `SHORT` | 2,431,599.84 USD | `1,896.28` | `1608.30` | `1282.20` | `2116.83` | 618,184.55 USD | `+25.42%` | `3X Cross` |
| `972` | `0x866d...d6e1` | `LONG` | 2,306,759.15 USD | `1,802.05` | `674.73` | `1282.20` | `273.88` | 1,090,857.84 USD | `+47.29%` | `10X Cross` |
| `986` | `0x2309...a2d9` | `LONG` | 2,246,074.78 USD | `1,750.37` | `1186.09` | `1282.20` | `814.91` | 169,980.67 USD | `+7.57%` | `8X Cross` |
| `1024` | `0x265e...7f70` | `LONG` | 2,114,567.62 USD | `1,651.74` | `1382.98` | `1282.20` | `0.000000` | -169,755.14 USD | `-8.03%` | `3X Cross` |
| `1031` | `0xfe7c...b7ae` | `SHORT` | 2,102,917.75 USD | `1,642.64` | `1346.92` | `1282.20` | `5783.14` | 109,590.87 USD | `+5.21%` | `10X Cross` |
| `1033` | `0x3e47...aaf6` | `LONG` | 2,099,674.50 USD | `1,636.28` | `1278.38` | `1282.20` | `1048.23` | 7,882.71 USD | `+0.38%` | `10X Cross` |
| `1035` | `0x2edd...8179` | `SHORT` | 2,096,934.43 USD | `1,633.89` | `1261.58` | `1282.20` | `2907.97` | -35,652.51 USD | `-1.70%` | `10X Cross` |
| `1051` | `0x7f75...9edf` | `LONG` | 2,063,259.93 USD | `1,611.67` | `1200.24` | `1282.20` | `981.84` | 128,875.95 USD | `+6.25%` | `10X Cross` |
| `1057` | `0x6646...6de5` | `SHORT` | 2,050,240.00 USD | `1,600.00` | `660.64` | `1282.20` | `4196.39` | -993,215.03 USD | `-48.44%` | `10X Cross` |
| `1058` | `0x023a...2355` | `SHORT` | 2,045,140.27 USD | `1,594.90` | `1310.00` | `1282.20` | `4451.84` | 44,171.87 USD | `+2.16%` | `10X Cross` |
| `1087` | `0xab59...59b5` | `LONG` | 2,008,618.62 USD | `1,565.32` | `1342.15` | `1282.20` | `837.07` | -92,276.59 USD | `-4.59%` | `10X Cross` |
| `1129` | `0x3205...40bb` | `SHORT` | 1,948,462.27 USD | `1,518.84` | `1247.18` | `1282.20` | `2218.14` | -54,192.55 USD | `-2.78%` | `10X Cross` |
| `1151` | `0xcf67...eb24` | `LONG` | 1,920,309.15 USD | `1,500.00` | `887.05` | `1282.20` | `673.49` | 589,737.78 USD | `+30.71%` | `10X Cross` |
| `1163` | `0xb695...a92d` | `LONG` | 1,902,837.30 USD | `1,483.00` | `1249.80` | `1282.20` | `0.000000` | 49,378.44 USD | `+2.59%` | `10X Cross` |
| `1170` | `0x7277...0b98` | `SHORT` | 1,893,214.02 USD | `1,475.73` | `1287.86` | `1282.20` | `2177.64` | 7,318.11 USD | `+0.39%` | `10X Cross` |
| `1228` | `0x2ab7...c2f8` | `LONG` | 1,796,434.18 USD | `1,400.51` | `813.26` | `1282.20` | `791.18` | 657,452.49 USD | `+36.60%` | `3X Cross` |
| `1248` | `0x11be...8b1d` | `LONG` | 1,765,465.06 USD | `1,375.83` | `1206.55` | `1282.20` | `1134.54` | 105,457.10 USD | `+5.97%` | `10X Isolated` |
| `1282` | `0xfc27...9d9d` | `SHORT` | 1,692,037.03 USD | `1,319.43` | `1298.53` | `1282.20` | `15120.55` | 21,279.74 USD | `+1.26%` | `10X Cross` |
| `1311` | `0x039c...0ebd` | `SHORT` | 1,642,866.42 USD | `1,279.79` | `1239.81` | `1282.20` | `3663.11` | -56,164.59 USD | `-3.42%` | `10X Cross` |
| `1336` | `0xe065...0f85` | `SHORT` | 1,616,401.02 USD | `1,262.61` | `1087.02` | `1282.20` | `1603.07` | -243,924.90 USD | `-15.09%` | `10X Cross` |
| `1410` | `0x266b...efcb` | `LONG` | 1,537,680.00 USD | `1,200.00` | `893.76` | `1282.20` | `400.72` | 465,170.30 USD | `+30.25%` | `10X Cross` |
| `1412` | `0x5975...9abd` | `LONG` | 1,536,360.00 USD | `1,200.00` | `1179.54` | `1282.20` | `503.69` | 120,917.21 USD | `+7.87%` | `5X Cross` |
| `1427` | `0x2847...d47b` | `LONG` | 1,518,662.85 USD | `1,186.27` | `1232.07` | `1282.20` | `0.000000` | 57,094.36 USD | `+3.76%` | `5X Cross` |
| `1449` | `0x69cc...14fd` | `SHORT` | 1,489,908.74 USD | `1,161.36` | `675.33` | `1282.20` | `8028.57` | -705,603.22 USD | `-47.36%` | `10X Cross` |
| `1463` | `0x3fc5...c0c1` | `SHORT` | 1,473,333.68 USD | `1,148.44` | `1264.34` | `1282.20` | `2781.55` | -21,319.90 USD | `-1.45%` | `10X Cross` |
| `1488` | `0xe35c...a1d3` | `LONG` | 1,446,468.80 USD | `1,127.06` | `1318.20` | `1282.20` | `694.46` | -39,226.55 USD | `-2.71%` | `2X Isolated` |
| `1509` | `0x5f94...4b96` | `LONG` | 1,431,114.46 USD | `1,115.27` | `538.00` | `1282.20` | `0.000000` | 831,096.83 USD | `+58.07%` | `10X Cross` |
| `1525` | `0x71df...a23d` | `SHORT` | 1,410,960.32 USD | `1,098.28` | `513.50` | `1282.20` | `2557.42` | -846,990.13 USD | `-60.03%` | `2X Cross` |
| `1558` | `0xbfc7...80b4` | `SHORT` | 1,376,215.00 USD | `1,075.00` | `558.03` | `1282.20` | `2859.47` | -776,336.27 USD | `-56.41%` | `10X Cross` |
| `1630` | `0x123d...3bff` | `SHORT` | 1,295,570.05 USD | `1,009.64` | `491.08` | `1282.20` | `4401.68` | -799,752.14 USD | `-61.73%` | `10X Cross` |
| `1640` | `0x38f9...cb04` | `SHORT` | 1,287,993.55 USD | `1,004.00` | `1243.59` | `1282.20` | `2110.00` | -39,431.57 USD | `-3.06%` | `10X Cross` |
| `1646` | `0xe282...df29` | `LONG` | 1,283,700.00 USD | `1,000.00` | `420.99` | `1282.20` | `818.45` | 862,713.14 USD | `+67.21%` | `10X Cross` |
| `1647` | `0x668c...ea2e` | `SHORT` | 1,283,300.00 USD | `1,000.00` | `1406.98` | `1282.20` | `4189.61` | 123,681.99 USD | `+9.64%` | `10X Cross` |
| `1650` | `0x39b4...5c34` | `LONG` | 1,279,954.32 USD | `999.73` | `1268.85` | `1282.20` | `588.58` | 11,444.97 USD | `+0.89%` | `10X Cross` |
| `1663` | `0x51f6...2b39` | `SHORT` | 1,265,645.00 USD | `986.55` | `1299.77` | `1282.20` | `2513.83` | 16,641.53 USD | `+1.31%` | `10X Cross` |
| `1683` | `0x17f0...094f` | `LONG` | 1,247,501.82 USD | `984.30` | `1287.23` | `1282.20` | `536.89` | -19,518.34 USD | `-1.56%` | `5X Cross` |
| `1690` | `0x2577...4897` | `SHORT` | 1,240,945.82 USD | `967.75` | `1264.88` | `1282.20` | `4583.64` | -16,857.87 USD | `-1.36%` | `10X Cross` |
| `1749` | `0x757d...94ba` | `LONG` | 1,186,682.50 USD | `925.00` | `1558.31` | `1282.20` | `0.000000` | -254,758.08 USD | `-21.47%` | `10X Cross` |
| `1751` | `0xaa82...9556` | `LONG` | 1,185,566.38 USD | `924.13` | `1254.72` | `1282.20` | `182.61` | 26,039.70 USD | `+2.20%` | `10X Cross` |
| `1794` | `0xb911...5525` | `LONG` | 1,154,880.00 USD | `900.00` | `1294.82` | `1282.20` | `1035.32` | -10,457.82 USD | `-0.91%` | `10X Cross` |
| `1839` | `0xcf0a...856f` | `LONG` | 1,118,033.91 USD | `871.15` | `1292.19` | `1282.20` | `1010.20` | -7,660.94 USD | `-0.69%` | `4X Cross` |
| `1845` | `0xef96...9383` | `SHORT` | 1,113,563.59 USD | `868.42` | `1259.08` | `1282.20` | `5421.20` | -20,151.80 USD | `-1.81%` | `10X Cross` |
| `1870` | `0xdf95...7d72` | `SHORT` | 1,094,660.08 USD | `853.27` | `1074.39` | `1282.20` | `45235.38` | -177,912.64 USD | `-16.25%` | `10X Cross` |
| `1918` | `0xae55...2236` | `LONG` | 1,048,231.07 USD | `817.47` | `1467.80` | `1282.20` | `0.000000` | -151,650.14 USD | `-14.47%` | `10X Cross` |
| `1923` | `0x601c...4f54` | `SHORT` | 1,044,696.04 USD | `824.42` | `615.11` | `1282.20` | `3135.61` | -537,583.29 USD | `-51.46%` | `5X Cross` |
| `1927` | `0xdf83...3cff` | `SHORT` | 1,040,790.69 USD | `811.09` | `1254.92` | `1282.20` | `1892.26` | -22,934.92 USD | `-2.20%` | `10X Cross` |
| `1952` | `0x0f02...5384` | `LONG` | 1,027,320.66 USD | `800.78` | `1290.36` | `1282.20` | `301.09` | -5,973.41 USD | `-0.58%` | `3X Cross` |
| `1953` | `0x11ee...1d1d` | `SHORT` | 1,026,720.00 USD | `800.00` | `1269.65` | `1282.20` | `1598.96` | -10,996.99 USD | `-1.07%` | `5X Cross` |
| `1956` | `0x9b0f...db40` | `LONG` | 1,025,230.96 USD | `800.00` | `1268.86` | `1282.20` | `797.40` | 10,141.20 USD | `+0.99%` | `10X Cross` |
| `1969` | `0x6e8f...4364` | `LONG` | 1,018,808.51 USD | `793.65` | `1260.00` | `1282.20` | `989.58` | 18,809.51 USD | `+1.85%` | `10X Cross` |
| `1974` | `0xabdb...84ac` | `LONG` | 1,016,081.94 USD | `793.69` | `711.79` | `1282.20` | `664.46` | 451,141.58 USD | `+44.40%` | `3X Cross` |

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
| `5m` | `BALANCED` | 0.00 USD | 1,750.00 USD | 1,750.00 USD | 1,750.00 USD | `1` | `2026-10-30 03:35:00 UTC - 2026-10-30 03:40:00 UTC` |
| `15m` | `BALANCED` | 0.00 USD | 1,750.00 USD | 1,750.00 USD | 1,750.00 USD | `1` | `2026-10-30 03:30:00 UTC - 2026-10-30 03:45:00 UTC` |
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
  * Current Rate: `86.73K` | Last 24h: `133.88K` | Last 3d: `245.74K` | Last 7d: `771.70K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0099%` | **USDT OKX** | `0.0100%` |
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
| `5m` | 1,440,000.00 USD | 3,410,000.00 USD | **`ACCUMULATION`** |
| `15m` | 1,770,000.00 USD | 6,180,000.00 USD | **`ACCUMULATION`** |
| `30m` | 2,470,000.00 USD | 5,140,000.00 USD | **`ACCUMULATION`** |
| `1h` | 2,990,000.00 USD | 3,230,000.00 USD | **`ACCUMULATION`** |
| `2h` | 9,780,000.00 USD | 22,030,000.00 USD | **`ACCUMULATION`** |
| `4h` | 2,180,000.00 USD | 25,040,000.00 USD | **`ACCUMULATION`** |
| `6h` | 2,380,000.00 USD | 7,390,000.00 USD | **`ACCUMULATION`** |
| `8h` | -9,360,000.00 USD | 6,160,000.00 USD | **`DISTRIBUTION`** |
| `12h` | 3,760,000.00 USD | 35,180,000.00 USD | **`ACCUMULATION`** |
| `24h` | 18,990,000.00 USD | 128,640,000.00 USD | **`ACCUMULATION`** |
| `1w` | 38,850,000.00 USD | 239,090,000.00 USD | **`ACCUMULATION`** |
| `30d` | 63,570,000.00 USD | -511,730,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+1.44M` | 15m=`+1.77M` | 1h=`+2.99M` | 24h=`+18.99M`
* Futures Capital Netflows: 5m=`+3.41M` | 15m=`+6.18M` | 1h=`+3.23M` | 24h=`+128.64M`
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
  * Spread-Padded Stop Loss: `1195.09` (Risk Distance: `27.08` pts)
  * +2.5R Take Profit: `1289.86`
  * Mathematical Lot Sizing: **`0.36 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `1263.91` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `1290.99` (Risk Distance: `27.08` pts)
  * +2.5R Take Profit: `1196.22`
  * Mathematical Lot Sizing: **`0.36 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`1294.08`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
