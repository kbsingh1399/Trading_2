# 🏛️ SOVEREIGN CANDIDATE DOSSIER: ZECUSD
**Canonical Key**: `ZECUSD` | **Broker Instrument**: `ZECUSD.p` | **Asset Class**: `Crypto Altcoin`
**Timestamp**: `2026-10-30 14:56:55 IST` (`2026-10-30 09:26:55 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

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
| `12` | `0xb83d...6e36` | `SHORT` | 65,261,818.53 USD | `52,385.47` | `1336.45` | `1244.20` | `3374.99` | 4,748,748.87 USD | `+7.28%` | `3X Cross` |
| `21` | `0x5b5d...c060` | `SHORT` | 49,983,215.20 USD | `40,121.38` | `1478.36` | `1244.20` | `4842.25` | 9,330,819.91 USD | `+18.67%` | `3X Cross` |
| `35` | `0x7fda...17d1` | `SHORT` | 33,110,494.23 USD | `26,579.83` | `1262.60` | `1244.20` | `2618.61` | 449,330.56 USD | `+1.36%` | `5X Cross` |
| `83` | `0x60b0...991e` | `LONG` | 20,905,878.07 USD | `16,779.74` | `1179.65` | `1244.20` | `918.18` | 1,111,631.05 USD | `+5.32%` | `10X Cross` |
| `140` | `0xc36a...105b` | `LONG` | 14,331,349.61 USD | `11,510.82` | `1215.14` | `1244.20` | `965.97` | 344,068.58 USD | `+2.40%` | `10X Cross` |
| `177` | `0x8742...8427` | `LONG` | 11,461,027.18 USD | `9,201.21` | `1286.37` | `1244.20` | `713.00` | -375,142.82 USD | `-3.27%` | `10X Cross` |
| `191` | `0x58b2...11f3` | `LONG` | 10,667,885.06 USD | `8,563.08` | `1246.56` | `1244.20` | `384.10` | -6,532.51 USD | `-0.06%` | `10X Cross` |
| `194` | `0x9ffd...ce40` | `LONG` | 10,634,360.59 USD | `8,536.17` | `1252.20` | `1244.20` | `607.62` | -54,606.79 USD | `-0.51%` | `5X Cross` |
| `195` | `0x9071...5c0b` | `LONG` | 10,610,839.88 USD | `8,517.29` | `1353.83` | `1244.20` | `0.000000` | -920,119.72 USD | `-8.67%` | `2X Cross` |
| `199` | `0xad59...ba81` | `SHORT` | 10,493,360.25 USD | `8,425.00` | `330.91` | `1244.20` | `2147.04` | -7,705,402.48 USD | `-73.43%` | `10X Cross` |
| `205` | `0xdd53...2b13` | `SHORT` | 10,202,281.22 USD | `8,195.92` | `741.54` | `1244.20` | `8508.02` | -4,124,684.85 USD | `-40.43%` | `3X Cross` |
| `228` | `0x880a...311c` | `SHORT` | 9,600,746.93 USD | `7,707.11` | `1367.50` | `1244.20` | `2219.22` | 938,737.28 USD | `+9.78%` | `10X Cross` |
| `239` | `0xbf73...5d58` | `LONG` | 9,340,152.75 USD | `7,500.00` | `1248.78` | `1244.20` | `141.23` | -25,692.87 USD | `-0.28%` | `10X Cross` |
| `276` | `0x2b61...2f6c` | `LONG` | 8,484,244.80 USD | `6,807.00` | `1453.56` | `1244.20` | `556.56` | -1,410,106.42 USD | `-16.62%` | `10X Cross` |
| `294` | `0x2ae5...83e7` | `LONG` | 8,018,965.44 USD | `6,436.80` | `1391.82` | `1244.20` | `0.000000` | -939,926.55 USD | `-11.72%` | `1X Cross` |
| `326` | `0xecb6...2b00` | `SHORT` | 7,053,669.77 USD | `5,661.96` | `1278.10` | `1244.20` | `6526.57` | 182,900.90 USD | `+2.59%` | `5X Cross` |
| `334` | `0x26b6...9a13` | `LONG` | 6,769,340.83 USD | `5,433.73` | `1282.23` | `1244.20` | `224.75` | -197,962.40 USD | `-2.92%` | `10X Cross` |
| `355` | `0x45d2...4029` | `SHORT` | 6,511,796.60 USD | `5,227.00` | `833.44` | `1244.20` | `9151.27` | -2,155,418.63 USD | `-33.10%` | `5X Cross` |
| `370` | `0xea00...a918` | `LONG` | 6,229,500.00 USD | `5,000.00` | `739.16` | `1244.20` | `0.000000` | 2,533,684.89 USD | `+40.67%` | `5X Cross` |
| `381` | `0xdd7a...8830` | `LONG` | 6,053,379.77 USD | `4,860.19` | `897.48` | `1244.20` | `788.68` | 1,691,476.09 USD | `+27.94%` | `10X Cross` |
| `425` | `0x469e...58a5` | `SHORT` | 5,183,719.38 USD | `4,163.52` | `1242.31` | `1244.20` | `1956.44` | -11,334.72 USD | `-0.22%` | `10X Cross` |
| `440` | `0x4cae...7c34` | `LONG` | 4,988,029.10 USD | `4,002.27` | `1169.72` | `1244.20` | `978.75` | 306,479.75 USD | `+6.14%` | `10X Cross` |
| `447` | `0xd4c1...3d1d` | `SHORT` | 4,894,075.47 USD | `3,928.46` | `1291.68` | `1244.20` | `2367.79` | 180,235.92 USD | `+3.68%` | `10X Cross` |
| `453` | `0xa61c...66b9` | `LONG` | 4,832,395.20 USD | `3,888.00` | `1148.34` | `1244.20` | `0.000000` | 367,653.06 USD | `+7.61%` | `10X Cross` |
| `473` | `0x382b...3e39` | `LONG` | 4,664,200.45 USD | `3,743.94` | `1219.28` | `1244.20` | `0.000000` | 99,287.79 USD | `+2.13%` | `10X Cross` |
| `479` | `0x9aa5...58af` | `SHORT` | 4,634,390.17 USD | `3,720.31` | `1205.51` | `1244.20` | `3719.89` | -149,503.37 USD | `-3.23%` | `10X Cross` |
| `484` | `0x0153...8052` | `SHORT` | 4,607,192.64 USD | `3,698.18` | `1307.82` | `1244.20` | `2504.93` | 229,378.10 USD | `+4.98%` | `1X Isolated` |
| `513` | `0xb122...e4ba` | `LONG` | 4,358,743.77 USD | `3,498.47` | `1265.25` | `1244.20` | `1130.06` | -67,707.76 USD | `-1.55%` | `10X Cross` |
| `553` | `0xd21d...90f1` | `LONG` | 4,047,883.77 USD | `3,250.00` | `1253.64` | `1244.20` | `876.15` | -26,457.96 USD | `-0.65%` | `4X Isolated` |
| `555` | `0x456f...cdf1` | `LONG` | 4,035,632.07 USD | `3,239.13` | `1267.62` | `1244.20` | `519.85` | -70,350.68 USD | `-1.74%` | `10X Cross` |
| `575` | `0x1338...c48e` | `LONG` | 3,923,874.84 USD | `3,149.43` | `1018.52` | `1244.20` | `820.45` | 716,129.29 USD | `+18.25%` | `4X Isolated` |
| `594` | `0xdbe0...d6d5` | `LONG` | 3,843,753.95 USD | `3,085.37` | `422.97` | `1244.20` | `338.76` | 2,538,749.45 USD | `+66.05%` | `3X Isolated` |
| `602` | `0x2e30...4cb5` | `SHORT` | 3,784,316.83 USD | `3,037.66` | `1282.41` | `1244.20` | `2862.92` | 111,194.69 USD | `+2.94%` | `2X Cross` |
| `614` | `0x325e...9564` | `LONG` | 3,729,831.04 USD | `3,000.91` | `1298.07` | `1244.20` | `163.25` | -165,574.12 USD | `-4.44%` | `10X Cross` |
| `616` | `0x9c06...0560` | `SHORT` | 3,723,358.49 USD | `2,989.80` | `786.00` | `1244.20` | `2584.40` | -1,373,363.49 USD | `-36.89%` | `10X Cross` |
| `624` | `0x27c9...d65d` | `SHORT` | 3,658,328.57 USD | `2,938.84` | `1254.41` | `1244.20` | `1731.63` | 28,185.00 USD | `+0.77%` | `10X Cross` |
| `713` | `0xa183...0482` | `LONG` | 3,156,350.40 USD | `2,534.00` | `530.25` | `1244.20` | `444.69` | 1,812,687.68 USD | `+57.43%` | `5X Isolated` |
| `716` | `0xac48...3201` | `LONG` | 3,153,995.85 USD | `2,531.50` | `1378.58` | `1244.20` | `523.64` | -335,876.43 USD | `-10.65%` | `10X Cross` |
| `724` | `0x0871...e927` | `LONG` | 3,112,164.75 USD | `2,500.00` | `1276.50` | `1244.20` | `0.000000` | -79,085.25 USD | `-2.54%` | `10X Cross` |
| `747` | `0x9b86...6e6e` | `LONG` | 3,068,046.80 USD | `2,463.30` | `637.58` | `1244.20` | `882.62` | 1,497,497.52 USD | `+48.81%` | `3X Cross` |
| `821` | `0xf48f...10fe` | `LONG` | 2,769,784.77 USD | `2,218.49` | `1517.87` | `1244.20` | `967.62` | -597,602.06 USD | `-21.58%` | `3X Cross` |
| `854` | `0x5bc4...3b0c` | `SHORT` | 2,648,296.75 USD | `2,130.74` | `1089.65` | `1244.20` | `3683.56` | -326,539.17 USD | `-12.33%` | `5X Cross` |
| `865` | `0x8de4...b9aa` | `SHORT` | 2,605,329.08 USD | `2,091.29` | `1331.35` | `1244.20` | `1690.05` | 178,910.62 USD | `+6.87%` | `3X Cross` |
| `866` | `0x71d0...8c26` | `SHORT` | 2,594,200.52 USD | `2,082.19` | `1266.91` | `1244.20` | `3871.84` | 43,738.24 USD | `+1.69%` | `10X Cross` |
| `870` | `0x4fe2...ac59` | `SHORT` | 2,580,969.06 USD | `2,071.57` | `1478.56` | `1244.20` | `1849.65` | 481,977.15 USD | `+18.67%` | `10X Cross` |
| `876` | `0xdf57...93f5` | `LONG` | 2,553,557.05 USD | `2,054.35` | `1227.36` | `1244.20` | `897.39` | 32,135.01 USD | `+1.26%` | `4X Isolated` |
| `882` | `0xbcd4...0dd2` | `LONG` | 2,532,027.01 USD | `2,033.92` | `1228.20` | `1244.20` | `735.88` | 33,976.19 USD | `+1.34%` | `10X Cross` |
| `893` | `0x9a99...d21a` | `LONG` | 2,491,800.00 USD | `2,000.00` | `1278.44` | `1244.20` | `0.000000` | -65,073.67 USD | `-2.61%` | `10X Cross` |
| `894` | `0xf29c...9971` | `LONG` | 2,491,200.00 USD | `2,000.00` | `1254.95` | `1244.20` | `0.000000` | -18,697.07 USD | `-0.75%` | `10X Cross` |
| `918` | `0x77ee...2902` | `SHORT` | 2,422,546.39 USD | `1,946.03` | `759.84` | `1244.20` | `5693.28` | -943,868.88 USD | `-38.96%` | `10X Cross` |
| `928` | `0x3e2f...b269` | `SHORT` | 2,393,216.38 USD | `1,925.51` | `1134.87` | `1244.20` | `2977.33` | -208,017.52 USD | `-8.69%` | `10X Cross` |
| `940` | `0x4f12...618b` | `SHORT` | 2,362,385.62 USD | `1,896.28` | `1608.30` | `1244.20` | `2116.94` | 687,398.77 USD | `+29.10%` | `3X Cross` |
| `984` | `0x866d...d6e1` | `LONG` | 2,245,894.92 USD | `1,802.05` | `674.73` | `1244.20` | `147.09` | 1,029,993.60 USD | `+45.86%` | `10X Cross` |
| `1014` | `0x2309...a2d9` | `LONG` | 2,179,268.24 USD | `1,750.37` | `1186.09` | `1244.20` | `808.60` | 103,174.13 USD | `+4.73%` | `8X Cross` |
| `1057` | `0x265e...7f70` | `LONG` | 2,057,737.69 USD | `1,651.74` | `1382.98` | `1244.20` | `0.000000` | -226,585.07 USD | `-11.01%` | `3X Cross` |
| `1060` | `0xfe7c...b7ae` | `SHORT` | 2,046,565.18 USD | `1,642.64` | `1346.92` | `1244.20` | `5713.22` | 165,943.44 USD | `+8.11%` | `10X Cross` |
| `1064` | `0x3e47...aaf6` | `LONG` | 2,038,641.25 USD | `1,636.28` | `1278.38` | `1244.20` | `1051.56` | -53,150.53 USD | `-2.61%` | `10X Cross` |
| `1071` | `0x2edd...8179` | `SHORT` | 2,033,359.54 USD | `1,635.98` | `1261.55` | `1244.20` | `2879.99` | 30,503.34 USD | `+1.50%` | `10X Cross` |
| `1091` | `0x7f75...9edf` | `LONG` | 2,007,721.87 USD | `1,612.17` | `1200.26` | `1244.20` | `986.72` | 72,700.80 USD | `+3.62%` | `10X Cross` |
| `1100` | `0x6646...6de5` | `SHORT` | 1,993,120.00 USD | `1,600.00` | `660.64` | `1244.20` | `4184.67` | -936,095.03 USD | `-46.97%` | `10X Cross` |
| `1109` | `0x023a...2355` | `SHORT` | 1,978,316.59 USD | `1,591.31` | `1310.00` | `1244.20` | `4423.64` | 106,292.66 USD | `+5.37%` | `10X Cross` |
| `1115` | `0xfc27...9d9d` | `SHORT` | 1,966,420.55 USD | `1,578.44` | `1295.79` | `1244.20` | `12980.45` | 78,903.66 USD | `+4.01%` | `10X Cross` |
| `1129` | `0xab59...59b5` | `LONG` | 1,950,232.19 USD | `1,565.32` | `1342.15` | `1244.20` | `835.72` | -150,663.03 USD | `-7.73%` | `10X Cross` |
| `1173` | `0x039c...0ebd` | `SHORT` | 1,891,544.19 USD | `1,521.39` | `1245.17` | `1244.20` | `3726.21` | 2,849.67 USD | `+0.15%` | `10X Cross` |
| `1181` | `0xcf67...eb24` | `LONG` | 1,868,850.00 USD | `1,500.00` | `887.05` | `1244.20` | `623.69` | 538,278.63 USD | `+28.80%` | `10X Cross` |
| `1199` | `0x7277...0b98` | `SHORT` | 1,834,332.39 USD | `1,475.73` | `1287.86` | `1244.20` | `2200.90` | 66,199.73 USD | `+3.61%` | `10X Cross` |
| `1262` | `0x2ab7...c2f8` | `LONG` | 1,744,755.36 USD | `1,400.51` | `813.26` | `1244.20` | `793.15` | 605,773.67 USD | `+34.72%` | `3X Cross` |
| `1279` | `0x11be...8b1d` | `LONG` | 1,714,146.60 USD | `1,375.83` | `1206.55` | `1244.20` | `1134.67` | 54,138.64 USD | `+3.16%` | `10X Isolated` |
| `1295` | `0x3205...40bb` | `SHORT` | 1,677,297.68 USD | `1,346.47` | `1257.43` | `1244.20` | `2354.85` | 15,791.92 USD | `+0.94%` | `10X Cross` |
| `1364` | `0xe065...0f85` | `SHORT` | 1,573,085.80 USD | `1,262.61` | `1087.02` | `1244.20` | `1551.07` | -200,609.67 USD | `-12.75%` | `10X Cross` |
| `1381` | `0x413c...886c` | `LONG` | 1,557,375.00 USD | `1,250.00` | `1237.51` | `1244.20` | `0.000000` | 10,485.54 USD | `+0.67%` | `10X Cross` |
| `1405` | `0xdf83...3cff` | `SHORT` | 1,546,648.66 USD | `1,241.59` | `1260.63` | `1244.20` | `1847.05` | 18,533.49 USD | `+1.20%` | `10X Cross` |
| `1444` | `0x2847...d47b` | `LONG` | 1,509,427.15 USD | `1,211.71` | `1232.45` | `1244.20` | `0.000000` | 16,059.55 USD | `+1.06%` | `5X Cross` |
| `1455` | `0x5975...9abd` | `LONG` | 1,497,840.00 USD | `1,200.00` | `1179.54` | `1244.20` | `549.24` | 82,397.21 USD | `+5.50%` | `5X Cross` |
| `1457` | `0x266b...efcb` | `LONG` | 1,494,960.00 USD | `1,200.00` | `893.76` | `1244.20` | `419.74` | 422,450.30 USD | `+28.26%` | `10X Cross` |
| `1492` | `0x69cc...14fd` | `SHORT` | 1,443,570.48 USD | `1,161.36` | `675.33` | `1244.20` | `8137.88` | -659,264.95 USD | `-45.67%` | `10X Cross` |
| `1502` | `0x3fc5...c0c1` | `SHORT` | 1,430,841.40 USD | `1,148.44` | `1264.34` | `1244.20` | `2772.69` | 21,172.38 USD | `+1.48%` | `10X Cross` |
| `1546` | `0x5f94...4b96` | `LONG` | 1,392,414.59 USD | `1,115.27` | `538.00` | `1244.20` | `0.000000` | 792,396.96 USD | `+56.91%` | `10X Cross` |
| `1553` | `0xe35c...a1d3` | `LONG` | 1,381,642.75 USD | `1,111.36` | `1311.66` | `1244.20` | `690.96` | -76,081.39 USD | `-5.51%` | `2X Isolated` |
| `1578` | `0x71df...a23d` | `SHORT` | 1,367,211.32 USD | `1,098.28` | `513.50` | `1244.20` | `2559.03` | -803,241.13 USD | `-58.75%` | `2X Cross` |
| `1595` | `0xbfc7...80b4` | `SHORT` | 1,338,410.37 USD | `1,075.00` | `558.03` | `1244.20` | `2702.63` | -738,531.64 USD | `-55.18%` | `10X Cross` |
| `1615` | `0x5323...b23c` | `SHORT` | 1,321,133.53 USD | `1,060.47` | `1254.62` | `1244.20` | `6487.94` | 9,349.82 USD | `+0.71%` | `5X Cross` |
| `1637` | `0x123d...3bff` | `SHORT` | 1,301,143.21 USD | `1,044.34` | `519.62` | `1244.20` | `4133.23` | -758,485.00 USD | `-58.29%` | `10X Cross` |
| `1694` | `0xe282...df29` | `LONG` | 1,247,000.00 USD | `1,000.00` | `420.99` | `1244.20` | `810.37` | 826,013.14 USD | `+66.24%` | `10X Cross` |
| `1699` | `0x668c...ea2e` | `SHORT` | 1,245,032.90 USD | `1,000.00` | `1406.98` | `1244.20` | `4211.70` | 161,949.09 USD | `+13.01%` | `10X Cross` |
| `1719` | `0x17f0...094f` | `LONG` | 1,225,276.92 USD | `984.30` | `1287.23` | `1244.20` | `537.02` | -41,743.25 USD | `-3.41%` | `5X Cross` |
| `1735` | `0x51f6...2b39` | `SHORT` | 1,211,829.42 USD | `972.81` | `1299.77` | `1244.20` | `2506.10` | 52,598.29 USD | `+4.34%` | `10X Cross` |
| `1805` | `0x757d...94ba` | `LONG` | 1,149,682.50 USD | `925.00` | `1558.31` | `1244.20` | `0.000000` | -291,758.09 USD | `-25.38%` | `10X Cross` |
| `1841` | `0xb911...5525` | `LONG` | 1,121,310.00 USD | `900.00` | `1294.82` | `1244.20` | `1035.45` | -44,027.82 USD | `-3.93%` | `10X Cross` |
| `1862` | `0xef96...9383` | `SHORT` | 1,105,895.09 USD | `887.77` | `1259.32` | `1244.20` | `5128.51` | 12,091.79 USD | `+1.09%` | `10X Cross` |
| `1887` | `0xcf0a...856f` | `LONG` | 1,084,889.88 USD | `871.15` | `1292.19` | `1244.20` | `1031.75` | -40,804.97 USD | `-3.76%` | `4X Cross` |
| `1906` | `0xdf95...7d72` | `SHORT` | 1,062,918.44 USD | `853.27` | `1074.39` | `1244.20` | `45352.53` | -146,171.00 USD | `-13.75%` | `10X Cross` |
| `1937` | `0xb2f7...af9f` | `SHORT` | 1,034,664.00 USD | `830.72` | `746.63` | `1244.20` | `8177.43` | -414,424.97 USD | `-40.05%` | `10X Cross` |
| `1962` | `0x601c...4f54` | `SHORT` | 1,027,144.88 USD | `824.42` | `615.11` | `1244.20` | `3133.32` | -520,032.13 USD | `-50.63%` | `5X Cross` |
| `1973` | `0xae55...2236` | `LONG` | 1,018,404.13 USD | `817.47` | `1467.80` | `1244.20` | `0.000000` | -181,477.09 USD | `-17.82%` | `10X Cross` |
| `1990` | `0x38f9...cb04` | `SHORT` | 1,010,387.69 USD | `812.47` | `1253.34` | `1244.20` | `2332.29` | 7,911.21 USD | `+0.78%` | `10X Cross` |

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
  * Current Rate: `83.98K` | Last 24h: `171.90K` | Last 3d: `285.15K` | Last 7d: `847.79K`
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
