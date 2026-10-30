# 🏛️ SOVEREIGN CANDIDATE DOSSIER: ZECUSD
**Canonical Key**: `ZECUSD` | **Broker Instrument**: `ZECUSD.p` | **Asset Class**: `Crypto Altcoin`
**Timestamp**: `2026-10-30 14:53:54 IST` (`2026-10-30 09:23:54 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `1243.07` | **Live Ask Quote**: `1244.08` | **Mid Price**: `1243.57`
- **Spread Points**: `101.00` | **Spread BPS**: `8.12 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `1253.88` | VWAP Z-Score: `-0.44` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `12.29` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `40.23` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `1318.67` | Lower -3.00σ Band: `1189.09`
  * Upper +2.51σ Band: `1308.09` | Lower -2.51σ Band: `1199.67`
  * Upper +2.01σ Band: `1297.29` | Lower -2.01σ Band: `1210.47`
  * Upper +2.00σ Band: `1297.08` | Lower -2.00σ Band: `1210.69`
  * Upper +1.28σ Band: `1281.53` | Lower -1.28σ Band: `1226.24`
  * Upper +1.00σ Band: `1275.48` | Lower -1.00σ Band: `1232.28`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`1251.34` | EMA-20=`1257.28` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`1263.26` (Slope: `+0.0000`) | EMA-100=`1269.08`
  * Institutional Anchors: EMA-144=`1272.04` | EMA-200=`1276.01` (Slope: `-0.1990`) | EMA-233=`1276.77`
- **Range Boundaries**: 24H High=`1396.49` | 24H Low=`1180.03` | Weekly High=`1396.49` | Weekly Low=`1180.03`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `1280.15` (Distance: `-2.87%`)
  * Point of Control (POC) = `1247.68` (Distance: `-0.34%`)
  * Value Area Low (VAL) = `1237.63` (Distance: `+0.47%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`1309.91` | POC=`1246.71` | VAL=`1230.27`
  * Prior Day Extremes: PDH=`1396.49` | PDL=`1206.89` | PDC=`1244.38`
  * Monday Range Blueprint: High=`1267.53` | Mid=`1222.14` | Low=`1176.75`
  * Developing Weekly Value Area: Weekly VAH=`1294.68` | Weekly POC=`1239.01` | Weekly VAL=`1200.92`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`1296.00` | Low=`1180.03`
  * London Session (08:00-16:00 UTC): High=`1283.82` | Low=`1239.96`
  * New York Session (13:00-21:00 UTC): High=`1251.04` | Low=`1236.11`
  * Initial Balance (First Hour): IB High=`1283.82` | IB Low=`1264.92`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `1238.60` - `1248.55`
  * Optimal Trade Entry (OTE 0.705): `1246.06`
  * Structural Invalidation Anchor (0.786): `1253.52`

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
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 14:52:21 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `12` | `0xb83d...6e36` | `SHORT` | 65,319,442.54 USD | `52,385.47` | `1336.45` | `1246.40` | `3357.88` | 4,691,124.86 USD | `+7.18%` | `3X Cross` |
| `21` | `0x5b5d...c060` | `SHORT` | 50,027,348.72 USD | `40,121.38` | `1478.36` | `1246.40` | `4822.81` | 9,286,686.39 USD | `+18.56%` | `3X Cross` |
| `35` | `0x7fda...17d1` | `SHORT` | 33,143,401.97 USD | `26,578.51` | `1262.61` | `1246.40` | `2611.68` | 414,852.89 USD | `+1.25%` | `5X Cross` |
| `82` | `0x60b0...991e` | `LONG` | 20,905,878.07 USD | `16,779.74` | `1179.65` | `1246.40` | `918.16` | 1,111,631.05 USD | `+5.32%` | `10X Cross` |
| `140` | `0xc36a...105b` | `LONG` | 14,375,863.10 USD | `11,510.82` | `1215.14` | `1246.40` | `965.92` | 388,582.07 USD | `+2.70%` | `10X Cross` |
| `179` | `0x8742...8427` | `LONG` | 11,473,908.87 USD | `9,201.21` | `1286.37` | `1246.40` | `710.86` | -362,261.12 USD | `-3.16%` | `10X Cross` |
| `195` | `0x58b2...11f3` | `LONG` | 10,691,861.69 USD | `8,563.08` | `1246.56` | `1246.40` | `383.20` | 17,444.11 USD | `+0.16%` | `10X Cross` |
| `197` | `0x9ffd...ce40` | `LONG` | 10,637,160.52 USD | `8,519.27` | `1252.21` | `1246.40` | `606.88` | -30,757.90 USD | `-0.29%` | `5X Cross` |
| `198` | `0x9071...5c0b` | `LONG` | 10,620,208.90 USD | `8,517.29` | `1353.83` | `1246.40` | `0.000000` | -910,750.70 USD | `-8.58%` | `2X Cross` |
| `202` | `0xad59...ba81` | `SHORT` | 10,504,295.05 USD | `8,425.00` | `330.91` | `1246.40` | `2146.87` | -7,716,337.28 USD | `-73.46%` | `10X Cross` |
| `207` | `0xdd53...2b13` | `SHORT` | 10,222,771.02 USD | `8,195.92` | `741.54` | `1246.40` | `8473.90` | -4,145,174.65 USD | `-40.55%` | `3X Cross` |
| `230` | `0x880a...311c` | `SHORT` | 9,622,326.84 USD | `7,707.11` | `1367.50` | `1246.40` | `2218.35` | 917,157.37 USD | `+9.53%` | `10X Cross` |
| `238` | `0xbf73...5d58` | `LONG` | 9,364,500.00 USD | `7,500.00` | `1248.78` | `1246.40` | `136.43` | -1,345.62 USD | `-0.01%` | `10X Cross` |
| `278` | `0x2b61...2f6c` | `LONG` | 8,498,539.50 USD | `6,807.00` | `1453.56` | `1246.40` | `558.39` | -1,395,811.72 USD | `-16.42%` | `10X Cross` |
| `294` | `0x2ae5...83e7` | `LONG` | 8,026,045.92 USD | `6,436.80` | `1391.82` | `1246.40` | `0.000000` | -932,846.07 USD | `-11.62%` | `1X Cross` |
| `327` | `0xecb6...2b00` | `SHORT` | 7,056,207.10 USD | `5,659.00` | `1278.13` | `1246.40` | `6800.60` | 176,750.87 USD | `+2.50%` | `5X Cross` |
| `335` | `0x26b6...9a13` | `LONG` | 6,775,317.94 USD | `5,433.73` | `1282.23` | `1246.40` | `222.79` | -191,985.30 USD | `-2.83%` | `10X Cross` |
| `355` | `0x45d2...4029` | `SHORT` | 6,517,546.30 USD | `5,227.00` | `833.44` | `1246.40` | `9108.33` | -2,161,168.33 USD | `-33.16%` | `5X Cross` |
| `371` | `0xea00...a918` | `LONG` | 6,229,500.00 USD | `5,000.00` | `739.16` | `1246.40` | `0.000000` | 2,533,684.89 USD | `+40.67%` | `5X Cross` |
| `381` | `0xdd7a...8830` | `LONG` | 6,068,919.25 USD | `4,860.19` | `897.48` | `1246.40` | `787.68` | 1,707,015.58 USD | `+28.13%` | `10X Cross` |
| `428` | `0x469e...58a5` | `SHORT` | 5,198,232.58 USD | `4,163.52` | `1242.31` | `1246.40` | `1962.27` | -25,847.92 USD | `-0.50%` | `10X Cross` |
| `439` | `0x4cae...7c34` | `LONG` | 4,998,034.78 USD | `4,002.27` | `1169.72` | `1246.40` | `971.79` | 316,485.43 USD | `+6.33%` | `10X Cross` |
| `448` | `0xd4c1...3d1d` | `SHORT` | 4,898,789.62 USD | `3,928.46` | `1291.68` | `1246.40` | `2359.49` | 175,521.77 USD | `+3.58%` | `10X Cross` |
| `455` | `0xa61c...66b9` | `LONG` | 4,847,231.42 USD | `3,888.00` | `1148.34` | `1246.40` | `0.000000` | 382,489.28 USD | `+7.89%` | `10X Cross` |
| `476` | `0x382b...3e39` | `LONG` | 4,668,693.18 USD | `3,743.94` | `1219.28` | `1246.40` | `0.000000` | 103,780.52 USD | `+2.22%` | `10X Cross` |
| `479` | `0x9aa5...58af` | `SHORT` | 4,644,876.60 USD | `3,720.31` | `1205.51` | `1246.40` | `3722.31` | -159,989.81 USD | `-3.44%` | `10X Cross` |
| `486` | `0x0153...8052` | `SHORT` | 4,610,890.82 USD | `3,698.18` | `1307.82` | `1246.40` | `2504.93` | 225,679.92 USD | `+4.89%` | `1X Isolated` |
| `514` | `0xb122...e4ba` | `LONG` | 4,364,341.33 USD | `3,498.47` | `1265.25` | `1246.40` | `1123.60` | -62,110.20 USD | `-1.42%` | `10X Cross` |
| `554` | `0xd21d...90f1` | `LONG` | 4,058,275.00 USD | `3,250.00` | `1253.64` | `1246.40` | `876.15` | -16,066.73 USD | `-0.40%` | `4X Isolated` |
| `559` | `0x456f...cdf1` | `LONG` | 4,035,632.07 USD | `3,239.13` | `1267.62` | `1246.40` | `519.80` | -70,350.68 USD | `-1.74%` | `10X Cross` |
| `576` | `0x1338...c48e` | `LONG` | 3,931,433.47 USD | `3,149.43` | `1018.52` | `1246.40` | `820.45` | 723,687.93 USD | `+18.41%` | `4X Isolated` |
| `596` | `0xdbe0...d6d5` | `LONG` | 3,846,839.32 USD | `3,085.37` | `422.97` | `1246.40` | `338.76` | 2,541,834.82 USD | `+66.08%` | `3X Isolated` |
| `611` | `0x325e...9564` | `LONG` | 3,741,282.21 USD | `3,000.91` | `1298.07` | `1246.40` | `155.11` | -154,122.95 USD | `-4.12%` | `10X Cross` |
| `614` | `0x9c06...0560` | `SHORT` | 3,733,064.28 USD | `2,989.80` | `786.00` | `1246.40` | `2581.40` | -1,383,069.28 USD | `-37.05%` | `10X Cross` |
| `620` | `0x2e30...4cb5` | `SHORT` | 3,678,791.42 USD | `2,950.35` | `1283.50` | `1246.40` | `2912.23` | 107,985.13 USD | `+2.94%` | `2X Cross` |
| `624` | `0x27c9...d65d` | `SHORT` | 3,661,500.76 USD | `2,938.84` | `1254.41` | `1246.40` | `1727.39` | 25,012.82 USD | `+0.68%` | `10X Cross` |
| `713` | `0xa183...0482` | `LONG` | 3,160,658.20 USD | `2,534.00` | `530.25` | `1246.40` | `444.69` | 1,816,995.48 USD | `+57.49%` | `5X Isolated` |
| `716` | `0xac48...3201` | `LONG` | 3,153,995.85 USD | `2,531.50` | `1378.58` | `1246.40` | `524.21` | -335,876.43 USD | `-10.65%` | `10X Cross` |
| `722` | `0x0871...e927` | `LONG` | 3,121,250.00 USD | `2,500.00` | `1276.50` | `1246.40` | `0.000000` | -70,000.00 USD | `-2.24%` | `10X Cross` |
| `747` | `0x9b86...6e6e` | `LONG` | 3,071,243.92 USD | `2,463.30` | `637.58` | `1246.40` | `882.62` | 1,500,694.63 USD | `+48.86%` | `3X Cross` |
| `821` | `0xf48f...10fe` | `LONG` | 2,766,235.18 USD | `2,218.49` | `1517.87` | `1246.40` | `970.25` | -601,151.64 USD | `-21.73%` | `3X Cross` |
| `856` | `0x5bc4...3b0c` | `SHORT` | 2,657,672.00 USD | `2,130.74` | `1089.65` | `1246.40` | `3680.30` | -335,914.42 USD | `-12.64%` | `5X Cross` |
| `868` | `0x8de4...b9aa` | `SHORT` | 2,611,184.69 USD | `2,091.29` | `1331.35` | `1246.40` | `1690.05` | 173,055.01 USD | `+6.63%` | `3X Cross` |
| `870` | `0x71d0...8c26` | `SHORT` | 2,594,825.18 USD | `2,082.19` | `1266.91` | `1246.40` | `3870.84` | 43,113.58 USD | `+1.66%` | `10X Cross` |
| `872` | `0x4fe2...ac59` | `SHORT` | 2,586,769.46 USD | `2,071.57` | `1478.56` | `1246.40` | `1846.39` | 476,176.76 USD | `+18.41%` | `10X Cross` |
| `879` | `0xdf57...93f5` | `LONG` | 2,562,390.75 USD | `2,054.35` | `1227.36` | `1246.40` | `897.39` | 40,968.71 USD | `+1.60%` | `4X Isolated` |
| `887` | `0xbcd4...0dd2` | `LONG` | 2,535,892.68 USD | `2,033.92` | `1228.20` | `1246.40` | `734.94` | 37,841.86 USD | `+1.49%` | `10X Cross` |
| `895` | `0x9a99...d21a` | `LONG` | 2,497,400.00 USD | `2,000.00` | `1278.44` | `1246.40` | `0.000000` | -59,473.67 USD | `-2.38%` | `10X Cross` |
| `898` | `0xf29c...9971` | `LONG` | 2,494,600.00 USD | `2,000.00` | `1254.95` | `1246.40` | `0.000000` | -15,297.07 USD | `-0.61%` | `10X Cross` |
| `922` | `0x77ee...2902` | `SHORT` | 2,429,618.46 USD | `1,946.03` | `759.84` | `1246.40` | `5682.38` | -950,940.95 USD | `-39.14%` | `10X Cross` |
| `927` | `0x3e2f...b269` | `SHORT` | 2,401,688.62 USD | `1,925.51` | `1134.87` | `1246.40` | `2977.33` | -216,489.77 USD | `-9.01%` | `10X Cross` |
| `943` | `0x4f12...618b` | `SHORT` | 2,367,695.21 USD | `1,896.28` | `1608.30` | `1246.40` | `2116.94` | 682,089.18 USD | `+28.81%` | `3X Cross` |
| `989` | `0x866d...d6e1` | `LONG` | 2,249,859.42 USD | `1,802.05` | `674.73` | `1246.40` | `148.62` | 1,033,958.11 USD | `+45.96%` | `10X Cross` |
| `1018` | `0x2309...a2d9` | `LONG` | 2,185,369.68 USD | `1,750.37` | `1186.09` | `1246.40` | `807.99` | 109,275.57 USD | `+5.00%` | `8X Cross` |
| `1059` | `0x265e...7f70` | `LONG` | 2,062,362.56 USD | `1,651.74` | `1382.98` | `1246.40` | `0.000000` | -221,960.20 USD | `-10.76%` | `3X Cross` |
| `1067` | `0xfe7c...b7ae` | `SHORT` | 2,046,565.18 USD | `1,642.64` | `1346.92` | `1246.40` | `5715.67` | 165,943.44 USD | `+8.11%` | `10X Cross` |
| `1071` | `0x3e47...aaf6` | `LONG` | 2,040,114.89 USD | `1,636.28` | `1278.38` | `1246.40` | `1051.21` | -51,676.90 USD | `-2.53%` | `10X Cross` |
| `1072` | `0x2edd...8179` | `SHORT` | 2,039,539.94 USD | `1,635.93` | `1261.55` | `1246.40` | `2876.97` | 24,260.53 USD | `+1.19%` | `10X Cross` |
| `1095` | `0x7f75...9edf` | `LONG` | 2,009,917.97 USD | `1,612.17` | `1200.26` | `1246.40` | `986.83` | 74,896.89 USD | `+3.73%` | `10X Cross` |
| `1102` | `0x6646...6de5` | `SHORT` | 1,994,880.00 USD | `1,600.00` | `660.64` | `1246.40` | `4187.60` | -937,855.03 USD | `-47.01%` | `10X Cross` |
| `1110` | `0x023a...2355` | `SHORT` | 1,983,911.48 USD | `1,591.31` | `1310.00` | `1246.40` | `4412.68` | 100,697.77 USD | `+5.08%` | `10X Cross` |
| `1119` | `0xfc27...9d9d` | `SHORT` | 1,968,156.84 USD | `1,578.44` | `1295.79` | `1246.40` | `12877.56` | 77,167.37 USD | `+3.92%` | `10X Cross` |
| `1130` | `0xab59...59b5` | `LONG` | 1,951,641.92 USD | `1,565.32` | `1342.15` | `1246.40` | `835.74` | -149,253.30 USD | `-7.65%` | `10X Cross` |
| `1174` | `0x039c...0ebd` | `SHORT` | 1,897,021.19 USD | `1,521.39` | `1245.17` | `1246.40` | `3736.47` | -2,627.33 USD | `-0.14%` | `10X Cross` |
| `1183` | `0xcf67...eb24` | `LONG` | 1,873,050.00 USD | `1,500.00` | `887.05` | `1246.40` | `620.53` | 542,478.63 USD | `+28.96%` | `10X Cross` |
| `1200` | `0x7277...0b98` | `SHORT` | 1,840,678.03 USD | `1,475.73` | `1287.86` | `1246.40` | `2193.68` | 59,854.09 USD | `+3.25%` | `10X Cross` |
| `1266` | `0x2ab7...c2f8` | `LONG` | 1,746,295.92 USD | `1,400.51` | `813.26` | `1246.40` | `792.64` | 607,314.23 USD | `+34.78%` | `3X Cross` |
| `1285` | `0x11be...8b1d` | `LONG` | 1,714,146.60 USD | `1,375.83` | `1206.55` | `1246.40` | `1134.67` | 54,138.64 USD | `+3.16%` | `10X Isolated` |
| `1299` | `0x3205...40bb` | `SHORT` | 1,681,337.09 USD | `1,346.47` | `1257.43` | `1246.40` | `2354.31` | 11,752.51 USD | `+0.70%` | `10X Cross` |
| `1369` | `0xe065...0f85` | `SHORT` | 1,576,621.11 USD | `1,262.61` | `1087.02` | `1246.40` | `1547.84` | -204,144.98 USD | `-12.95%` | `10X Cross` |
| `1385` | `0x413c...886c` | `LONG` | 1,560,875.00 USD | `1,250.00` | `1237.51` | `1246.40` | `0.000000` | 13,985.54 USD | `+0.90%` | `10X Cross` |
| `1411` | `0xdf83...3cff` | `SHORT` | 1,548,138.57 USD | `1,241.59` | `1260.63` | `1246.40` | `1841.47` | 17,043.58 USD | `+1.10%` | `10X Cross` |
| `1450` | `0x2847...d47b` | `LONG` | 1,510,658.12 USD | `1,211.71` | `1232.45` | `1246.40` | `0.000000` | 17,290.52 USD | `+1.14%` | `5X Cross` |
| `1461` | `0x266b...efcb` | `LONG` | 1,496,160.00 USD | `1,200.00` | `893.76` | `1246.40` | `411.96` | 423,650.30 USD | `+28.32%` | `10X Cross` |
| `1463` | `0x5975...9abd` | `LONG` | 1,495,080.00 USD | `1,200.00` | `1179.54` | `1246.40` | `543.29` | 79,637.21 USD | `+5.33%` | `5X Cross` |
| `1492` | `0x69cc...14fd` | `SHORT` | 1,448,215.92 USD | `1,161.36` | `675.33` | `1246.40` | `8100.77` | -663,910.39 USD | `-45.84%` | `10X Cross` |
| `1509` | `0x3fc5...c0c1` | `SHORT` | 1,431,875.68 USD | `1,148.44` | `1264.34` | `1246.40` | `2766.64` | 20,138.09 USD | `+1.41%` | `10X Cross` |
| `1550` | `0x5f94...4b96` | `LONG` | 1,390,519.31 USD | `1,115.27` | `538.00` | `1246.40` | `0.000000` | 790,501.67 USD | `+56.85%` | `10X Cross` |
| `1554` | `0xe35c...a1d3` | `LONG` | 1,385,550.18 USD | `1,111.36` | `1311.66` | `1246.40` | `690.96` | -72,173.96 USD | `-5.21%` | `2X Isolated` |
| `1580` | `0x71df...a23d` | `SHORT` | 1,371,202.58 USD | `1,098.28` | `513.50` | `1246.40` | `2558.80` | -807,232.39 USD | `-58.87%` | `2X Cross` |
| `1592` | `0xbfc7...80b4` | `SHORT` | 1,342,157.60 USD | `1,075.00` | `558.03` | `1246.40` | `2684.98` | -742,278.88 USD | `-55.30%` | `10X Cross` |
| `1637` | `0x123d...3bff` | `SHORT` | 1,301,143.21 USD | `1,044.34` | `519.62` | `1246.40` | `4150.26` | -758,485.00 USD | `-58.29%` | `10X Cross` |
| `1691` | `0x668c...ea2e` | `SHORT` | 1,248,518.70 USD | `1,000.00` | `1406.98` | `1246.40` | `4211.46` | 158,463.29 USD | `+12.69%` | `10X Cross` |
| `1695` | `0xe282...df29` | `LONG` | 1,246,715.90 USD | `1,000.00` | `420.99` | `1246.40` | `810.23` | 825,729.04 USD | `+66.23%` | `10X Cross` |
| `1714` | `0x17f0...094f` | `LONG` | 1,228,898.55 USD | `984.30` | `1287.23` | `1246.40` | `537.02` | -38,121.61 USD | `-3.10%` | `5X Cross` |
| `1729` | `0x51f6...2b39` | `SHORT` | 1,213,094.07 USD | `972.81` | `1299.77` | `1246.40` | `2500.34` | 51,333.64 USD | `+4.23%` | `10X Cross` |
| `1797` | `0x757d...94ba` | `LONG` | 1,153,752.50 USD | `925.00` | `1558.31` | `1246.40` | `0.000000` | -287,688.09 USD | `-24.93%` | `10X Cross` |
| `1840` | `0xb911...5525` | `LONG` | 1,122,120.54 USD | `900.00` | `1294.82` | `1246.40` | `1035.45` | -43,217.28 USD | `-3.85%` | `10X Cross` |
| `1860` | `0xef96...9383` | `SHORT` | 1,108,558.40 USD | `887.77` | `1259.32` | `1246.40` | `5133.78` | 9,428.48 USD | `+0.85%` | `10X Cross` |
| `1884` | `0xcf0a...856f` | `LONG` | 1,087,717.89 USD | `871.15` | `1292.19` | `1246.40` | `1029.84` | -37,976.96 USD | `-3.49%` | `4X Cross` |
| `1905` | `0xdf95...7d72` | `SHORT` | 1,064,027.69 USD | `853.27` | `1074.39` | `1246.40` | `45250.92` | -147,280.25 USD | `-13.84%` | `10X Cross` |
| `1942` | `0xb2f7...af9f` | `SHORT` | 1,035,742.19 USD | `830.72` | `746.63` | `1246.40` | `8144.56` | -415,503.16 USD | `-40.12%` | `10X Cross` |
| `1956` | `0x601c...4f54` | `SHORT` | 1,029,288.37 USD | `824.42` | `615.11` | `1246.40` | `3127.16` | -522,175.62 USD | `-50.73%` | `5X Cross` |
| `1963` | `0x5323...b23c` | `SHORT` | 1,024,759.66 USD | `821.78` | `1258.47` | `1246.40` | `8018.76` | 9,425.73 USD | `+0.92%` | `5X Cross` |
| `1975` | `0xae55...2236` | `LONG` | 1,019,303.34 USD | `817.47` | `1467.80` | `1246.40` | `0.000000` | -180,577.87 USD | `-17.72%` | `10X Cross` |
| `1988` | `0x38f9...cb04` | `SHORT` | 1,013,393.83 USD | `812.47` | `1253.34` | `1246.40` | `2335.32` | 4,905.07 USD | `+0.48%` | `10X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `1608.80` | 1,238.78 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 1.24K USD at 1608.8000 USD [API] | `2026-09-26 21:17:31` |
| `ANNOUNCEMENT` | `INFO` | `1608.80` | 128.70 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 0.13K USD at 1608.8000 USD [API] | `2026-09-26 21:17:31` |
| `ANNOUNCEMENT` | `INFO` | `1608.60` | 3,989.33 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 3.99K USD at 1608.6000 USD [API] | `2026-09-26 21:17:31` |
| `ANNOUNCEMENT` | `INFO` | `1608.60` | 997.33 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 1.00K USD at 1608.6000 USD [API] | `2026-09-26 21:17:31` |
| `ANNOUNCEMENT` | `INFO` | `1608.60` | 160.86 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 0.16K USD at 1608.6000 USD [API] | `2026-09-26 21:17:31` |
| `ANNOUNCEMENT` | `INFO` | `1608.60` | 96.52 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 0.10K USD at 1608.6000 USD [API] | `2026-09-26 21:17:31` |
| `ANNOUNCEMENT` | `INFO` | `1608.60` | 3,088.51 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 3.09K USD at 1608.6000 USD [API] | `2026-09-26 21:17:31` |
| `ANNOUNCEMENT` | `INFO` | `1608.50` | 3,989.08 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 3.99K USD at 1608.5000 USD [API] | `2026-09-26 21:17:31` |
| `ANNOUNCEMENT` | `INFO` | `1608.50` | 579.06 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 0.58K USD at 1608.5000 USD [API] | `2026-09-26 21:17:31` |
| `ANNOUNCEMENT` | `INFO` | `1608.50` | 1,849.77 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 1.85K USD at 1608.5000 USD [API] | `2026-09-26 21:17:31` |
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
  * 24H Horizon: Short MP=`1404.55` (Vol: 3,000,000.00 USD, Dist: `+12.58%`) | Long MP=`1176.48` (Vol: 3,400,000.00 USD, Dist: `--5.70%`)
  * 48H Horizon: Short MP=`1404.55` (Vol: 3,000,000.00 USD, Dist: `+12.58%`) | Long MP=`1176.48` (Vol: 3,400,000.00 USD, Dist: `--5.70%`)
  * 3D Horizon: Short MP=`1404.55` (Vol: 3,000,000.00 USD, Dist: `+12.58%`) | Long MP=`1176.48` (Vol: 3,400,000.00 USD, Dist: `--5.70%`)
  * 7D Horizon: Short MP=`1404.10` (Vol: 3,000,000.00 USD, Dist: `+12.55%`) | Long MP=`1176.74` (Vol: 4,900,000.00 USD, Dist: `--5.68%`)
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
| `5m` | `BALANCED` | 0.00 USD | 1,750.00 USD | 1,750.00 USD | 1,750.00 USD | `1` | `2026-10-30 09:20:00 UTC - 2026-10-30 09:25:00 UTC` |
| `15m` | `BALANCED` | 0.00 USD | 1,750.00 USD | 1,750.00 USD | 1,750.00 USD | `1` | `2026-10-30 09:15:00 UTC - 2026-10-30 09:30:00 UTC` |
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
  * Current Rate: `84.03K` | Last 24h: `171.90K` | Last 3d: `285.15K` | Last 7d: `847.79K`
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
| `0:00 UTC` | `1266.15` | `1267.62` | `1266.15` | `1278.45` | `1260.45` | 12,479,157.49 USD | 5,007,423.22 USD | 7,471,734.27 USD | -2,464,311.04 USD | `-19.75%` | `3B / 15S` |
| `5:00 UTC` | `1263.15` | `1263.66` | `1263.15` | `1267.05` | `1260.45` | 8,382,487.91 USD | 4,193,725.38 USD | 4,188,762.53 USD | 4,962.85 USD | `+0.06%` | `3B / 2S` |
| `0:00 UTC` | `1255.05` | `1256.16` | `1255.05` | `1269.15` | `1247.25` | 26,236,011.28 USD | 8,922,234.21 USD | 17,313,777.08 USD | -8,391,542.87 USD | `-31.98%` | `2B / 24S` |
| `5:00 UTC` | `1248.15` | `1248.05` | `1248.15` | `1253.25` | `1244.25` | 21,008,122.73 USD | 11,395,427.09 USD | 9,612,695.64 USD | 1,782,731.45 USD | `+8.49%` | `1B / 0S` |
| `0:00 UTC` | `1245.75` | `1245.57` | `1245.75` | `1250.55` | `1240.05` | 17,224,192.69 USD | 9,235,789.14 USD | 7,988,403.55 USD | 1,247,385.58 USD | `+7.24%` | `1B / 6S` |
| `5:00 UTC` | `1251.45` | `1250.99` | `1251.45` | `1255.05` | `1246.35` | 13,619,576.55 USD | 6,741,413.50 USD | 6,878,163.05 USD | -136,749.55 USD | `-1.00%` | `2B / 0S` |
| `0:00 UTC` | `1249.95` | `1249.10` | `1249.95` | `1253.55` | `1244.55` | 10,263,783.49 USD | 5,117,369.60 USD | 5,146,413.89 USD | -29,044.29 USD | `-0.28%` | `1B / 4S` |
| `5:00 UTC` | `1246.65` | `1246.77` | `1246.65` | `1252.35` | `1243.95` | 13,017,000.97 USD | 7,727,648.32 USD | 5,289,352.64 USD | 2,438,295.68 USD | `+18.73%` | `8B / 5S` |
| `0:00 UTC` | `1244.55` | `1245.81` | `1244.55` | `1249.05` | `1243.65` | 9,717,386.64 USD | 3,914,194.68 USD | 5,803,191.96 USD | -1,888,997.28 USD | `-19.44%` | `0B / 1S` |
| `5:00 UTC` | `1246.35` | `1246.80` | `1246.35` | `1249.35` | `1244.55` | 2,104,180.53 USD | 1,056,055.07 USD | 1,048,125.46 USD | 7,929.61 USD | `+0.38%` | `4B / 2S` |

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
| `5m` | -360,440.00 USD | -167,580.00 USD | **`DISTRIBUTION`** |
| `15m` | -1,030,000.00 USD | -2,120,000.00 USD | **`DISTRIBUTION`** |
| `30m` | -1,450,000.00 USD | 1,510,000.00 USD | **`ACCUMULATION`** |
| `1h` | -1,560,000.00 USD | 1,580,000.00 USD | **`ACCUMULATION`** |
| `2h` | 1,670,000.00 USD | -14,300,000.00 USD | **`DISTRIBUTION`** |
| `4h` | 1,880,000.00 USD | -24,350,000.00 USD | **`DISTRIBUTION`** |
| `6h` | 771,760.00 USD | -33,450,000.00 USD | **`DISTRIBUTION`** |
| `8h` | 8,550,000.00 USD | -9,250,000.00 USD | **`DISTRIBUTION`** |
| `12h` | 4,340,000.00 USD | -23,330,000.00 USD | **`DISTRIBUTION`** |
| `24h` | 19,220,000.00 USD | 69,850,000.00 USD | **`ACCUMULATION`** |
| `1w` | 33,430,000.00 USD | 202,170,000.00 USD | **`ACCUMULATION`** |
| `30d` | 62,950,000.00 USD | -543,420,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-360.44K` | 15m=`-1.03M` | 1h=`-1.56M` | 24h=`+19.22M`
* Futures Capital Netflows: 5m=`-167.58K` | 15m=`-2.12M` | 1h=`+1.58M` | 24h=`+69.85M`
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
  * `2026-10-30 14:41:03 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 14:38:03 IST`: [@FirstSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 14:34:03 IST`: [destatis.de] - (Sentiment: `Neutral`)
  * `2026-10-30 14:33:03 IST`: [istat.it] - (Sentiment: `Neutral`)
  * `2026-10-30 14:10:03 IST`: [channelnewsasia.com] - (Sentiment: `Neutral`)
  * `2026-10-30 13:52:03 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 13:51:03 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 14:48:03 IST`: [kof.ethz.ch] - (Sentiment: `Neutral`)
  * `2026-10-30 14:48:03 IST`: [gerlachmacro.substack.com] - (Sentiment: `Neutral`)
  * `2026-10-30 14:48:03 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-30 14:48:03 IST`: [insee.fr] - (Sentiment: `Neutral`)
  * `2026-10-30 14:48:03 IST`: [insee.fr] - (Sentiment: `Neutral`)
  * `2026-10-30 14:48:03 IST`: [@FirstSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 14:48:03 IST`: [nationwide.co.uk] - (Sentiment: `Neutral`)
  * `2026-10-30 14:47:03 IST`: [destatis.de] - (Sentiment: `Neutral`)


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
  * Spread-Padded Stop Loss: `1221.36` (Risk Distance: `16.27` pts)
  * +2.5R Take Profit: `1278.30`
  * Mathematical Lot Sizing: **`0.61 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `1280.15` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `1296.42` (Risk Distance: `16.27` pts)
  * +2.5R Take Profit: `1239.48`
  * Mathematical Lot Sizing: **`0.61 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`1253.52`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
