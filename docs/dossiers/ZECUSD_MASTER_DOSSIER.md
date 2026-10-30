# 🏛️ SOVEREIGN CANDIDATE DOSSIER: ZECUSD
**Canonical Key**: `ZECUSD` | **Broker Instrument**: `ZECUSD.p` | **Asset Class**: `Crypto Altcoin`
**Timestamp**: `2026-10-30 14:29:41 IST` (`2026-10-30 08:59:41 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `1243.99` | **Live Ask Quote**: `1244.87` | **Mid Price**: `1244.43`
- **Spread Points**: `88.00` | **Spread BPS**: `7.07 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `1244.43` | VWAP Z-Score: `+0.00` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `3.11` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `50.00` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `1253.14` | Lower -3.00σ Band: `1235.72`
  * Upper +2.51σ Band: `1251.27` | Lower -2.51σ Band: `1237.59`
  * Upper +2.01σ Band: `1249.66` | Lower -2.01σ Band: `1239.20`
  * Upper +2.00σ Band: `1249.41` | Lower -2.00σ Band: `1239.45`
  * Upper +1.28σ Band: `1247.91` | Lower -1.28σ Band: `1240.95`
  * Upper +1.00σ Band: `1246.92` | Lower -1.00σ Band: `1241.94`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`1244.43` | EMA-20=`1244.43` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`1244.43` (Slope: `+0.0000`) | EMA-100=`1244.43`
  * Institutional Anchors: EMA-144=`1244.43` | EMA-200=`1244.43` (Slope: `+0.0000`) | EMA-233=`1244.43`
- **Range Boundaries**: 24H High=`1256.87` | 24H Low=`1231.99` | Weekly High=`1269.32` | Weekly Low=`1219.54`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `1284.79` (Distance: `-3.08%`)
  * Point of Control (POC) = `1275.51` (Distance: `-2.37%`)
  * Value Area Low (VAL) = `1241.49` (Distance: `+0.30%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`1309.91` | POC=`1246.71` | VAL=`1230.27`
  * Prior Day Extremes: PDH=`1396.49` | PDL=`1206.89` | PDC=`1244.38`
  * Monday Range Blueprint: High=`1267.53` | Mid=`1222.14` | Low=`1176.75`
  * Developing Weekly Value Area: Weekly VAH=`1294.68` | Weekly POC=`1239.01` | Weekly VAL=`1200.92`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`1296.00` | Low=`1180.03`
  * London Session (08:00-16:00 UTC): High=`1283.82` | Low=`1239.96`
  * New York Session (13:00-21:00 UTC): High=`1251.90` | Low=`1236.96`
  * Initial Balance (First Hour): IB High=`1283.82` | IB Low=`1264.92`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `1239.45` - `1249.41`
  * Optimal Trade Entry (OTE 0.705): `1246.92`
  * Structural Invalidation Anchor (0.786): `1254.39`

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
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 14:22:11 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `12` | `0xb83d...6e36` | `SHORT` | 65,392,782.20 USD | `52,385.47` | `1336.45` | `1250.50` | `3594.36` | 4,617,785.20 USD | `+7.06%` | `3X Cross` |
| `21` | `0x5b5d...c060` | `SHORT` | 50,083,518.65 USD | `40,121.38` | `1478.36` | `1250.50` | `5001.04` | 9,230,516.46 USD | `+18.43%` | `3X Cross` |
| `36` | `0x7fda...17d1` | `SHORT` | 33,164,047.97 USD | `26,567.37` | `1262.61` | `1250.50` | `2606.49` | 380,308.57 USD | `+1.15%` | `5X Cross` |
| `82` | `0x60b0...991e` | `LONG` | 20,942,793.49 USD | `16,779.74` | `1179.65` | `1250.50` | `917.87` | 1,148,546.48 USD | `+5.48%` | `10X Cross` |
| `141` | `0xc36a...105b` | `LONG` | 14,343,632.80 USD | `11,510.82` | `1215.14` | `1250.50` | `966.21` | 356,351.77 USD | `+2.48%` | `10X Cross` |
| `179` | `0x8742...8427` | `LONG` | 11,484,030.20 USD | `9,201.21` | `1286.37` | `1250.50` | `708.13` | -352,139.79 USD | `-3.07%` | `10X Cross` |
| `197` | `0x58b2...11f3` | `LONG` | 10,669,834.88 USD | `8,563.08` | `1246.56` | `1250.50` | `383.58` | -4,582.70 USD | `-0.04%` | `10X Cross` |
| `199` | `0x9ffd...ce40` | `LONG` | 10,632,498.24 USD | `8,519.63` | `1252.22` | `1250.50` | `606.30` | -35,984.42 USD | `-0.34%` | `5X Cross` |
| `200` | `0x9071...5c0b` | `LONG` | 10,630,429.65 USD | `8,517.29` | `1353.83` | `1250.50` | `0.000000` | -900,529.95 USD | `-8.47%` | `2X Cross` |
| `204` | `0xad59...ba81` | `SHORT` | 10,513,557.50 USD | `8,425.00` | `330.91` | `1250.50` | `2146.83` | -7,725,599.73 USD | `-73.48%` | `10X Cross` |
| `210` | `0xdd53...2b13` | `SHORT` | 10,227,257.46 USD | `8,195.92` | `741.54` | `1250.50` | `8461.98` | -4,149,661.10 USD | `-40.57%` | `3X Cross` |
| `232` | `0x880a...311c` | `SHORT` | 9,619,243.99 USD | `7,707.11` | `1367.50` | `1250.50` | `2230.13` | 920,240.21 USD | `+9.57%` | `10X Cross` |
| `240` | `0xbf73...5d58` | `LONG` | 9,361,500.00 USD | `7,500.00` | `1248.78` | `1250.50` | `136.03` | -4,345.62 USD | `-0.05%` | `10X Cross` |
| `278` | `0x2b61...2f6c` | `LONG` | 8,482,202.70 USD | `6,807.00` | `1453.56` | `1250.50` | `563.37` | -1,412,148.52 USD | `-16.65%` | `10X Cross` |
| `296` | `0x2ae5...83e7` | `LONG` | 8,022,183.84 USD | `6,436.80` | `1391.82` | `1250.50` | `0.000000` | -936,708.15 USD | `-11.68%` | `1X Cross` |
| `329` | `0xecb6...2b00` | `SHORT` | 7,045,704.79 USD | `5,644.24` | `1278.22` | `1250.50` | `6506.02` | 168,856.28 USD | `+2.40%` | `5X Cross` |
| `337` | `0x26b6...9a13` | `LONG` | 6,781,838.41 USD | `5,433.73` | `1282.23` | `1250.50` | `225.16` | -185,464.82 USD | `-2.73%` | `10X Cross` |
| `358` | `0x45d2...4029` | `SHORT` | 6,514,410.10 USD | `5,227.00` | `833.44` | `1250.50` | `9088.72` | -2,158,032.13 USD | `-33.13%` | `5X Cross` |
| `374` | `0xea00...a918` | `LONG` | 6,230,138.50 USD | `5,000.00` | `739.16` | `1250.50` | `0.000000` | 2,534,323.39 USD | `+40.68%` | `5X Cross` |
| `382` | `0xdd7a...8830` | `LONG` | 6,064,120.79 USD | `4,860.19` | `897.48` | `1250.50` | `787.32` | 1,702,217.11 USD | `+28.07%` | `10X Cross` |
| `426` | `0x469e...58a5` | `SHORT` | 5,186,080.51 USD | `4,163.52` | `1242.31` | `1250.50` | `1962.65` | -13,695.86 USD | `-0.26%` | `10X Cross` |
| `440` | `0x4cae...7c34` | `LONG` | 4,989,630.01 USD | `4,002.27` | `1169.72` | `1250.50` | `979.74` | 308,080.66 USD | `+6.17%` | `10X Cross` |
| `446` | `0xd4c1...3d1d` | `SHORT` | 4,903,896.62 USD | `3,928.46` | `1291.68` | `1250.50` | `2348.22` | 170,414.77 USD | `+3.48%` | `10X Cross` |
| `455` | `0xa61c...66b9` | `LONG` | 4,851,271.44 USD | `3,888.00` | `1148.34` | `1250.50` | `0.000000` | 386,529.30 USD | `+7.97%` | `10X Cross` |
| `477` | `0x382b...3e39` | `LONG` | 4,672,811.51 USD | `3,743.94` | `1219.28` | `1250.50` | `0.000000` | 107,898.86 USD | `+2.31%` | `10X Cross` |
| `481` | `0x9aa5...58af` | `SHORT` | 4,644,062.97 USD | `3,720.31` | `1205.51` | `1250.50` | `3715.67` | -159,176.17 USD | `-3.43%` | `10X Cross` |
| `485` | `0x0153...8052` | `SHORT` | 4,613,479.55 USD | `3,698.18` | `1307.82` | `1250.50` | `2504.91` | 223,091.20 USD | `+4.84%` | `1X Isolated` |
| `519` | `0xb122...e4ba` | `LONG` | 4,366,440.41 USD | `3,498.47` | `1265.25` | `1250.50` | `1107.19` | -60,011.12 USD | `-1.37%` | `10X Cross` |
| `554` | `0xd21d...90f1` | `LONG` | 4,055,675.00 USD | `3,250.00` | `1253.64` | `1250.50` | `876.13` | -18,666.73 USD | `-0.46%` | `4X Isolated` |
| `559` | `0x456f...cdf1` | `LONG` | 4,031,049.13 USD | `3,235.12` | `1267.65` | `1250.50` | `518.80` | -69,938.35 USD | `-1.73%` | `10X Cross` |
| `583` | `0x1338...c48e` | `LONG` | 3,922,930.01 USD | `3,149.43` | `1018.52` | `1250.50` | `820.43` | 715,184.47 USD | `+18.23%` | `4X Isolated` |
| `598` | `0xdbe0...d6d5` | `LONG` | 3,845,913.71 USD | `3,085.37` | `422.97` | `1250.50` | `338.74` | 2,540,909.21 USD | `+66.07%` | `3X Isolated` |
| `614` | `0x325e...9564` | `LONG` | 3,744,400.46 USD | `3,000.91` | `1298.07` | `1250.50` | `145.89` | -151,004.70 USD | `-4.03%` | `10X Cross` |
| `616` | `0x9c06...0560` | `SHORT` | 3,731,868.36 USD | `2,989.80` | `786.00` | `1250.50` | `2571.16` | -1,381,873.36 USD | `-37.03%` | `10X Cross` |
| `617` | `0x2e30...4cb5` | `SHORT` | 3,725,104.22 USD | `2,984.62` | `1283.50` | `1250.50` | `2890.18` | 105,657.90 USD | `+2.84%` | `2X Cross` |
| `626` | `0x27c9...d65d` | `SHORT` | 3,668,553.97 USD | `2,938.84` | `1254.41` | `1250.50` | `1728.21` | 17,959.60 USD | `+0.49%` | `10X Cross` |
| `718` | `0xa183...0482` | `LONG` | 3,162,685.40 USD | `2,534.00` | `530.25` | `1250.50` | `444.67` | 1,819,022.68 USD | `+57.52%` | `5X Isolated` |
| `720` | `0xac48...3201` | `LONG` | 3,159,565.15 USD | `2,531.50` | `1378.58` | `1250.50` | `529.53` | -330,307.13 USD | `-10.45%` | `10X Cross` |
| `730` | `0x0871...e927` | `LONG` | 3,120,750.00 USD | `2,500.00` | `1276.50` | `1250.50` | `0.000000` | -70,500.00 USD | `-2.26%` | `10X Cross` |
| `754` | `0x9b86...6e6e` | `LONG` | 3,073,952.07 USD | `2,463.30` | `637.58` | `1250.50` | `882.60` | 1,503,402.79 USD | `+48.91%` | `3X Cross` |
| `829` | `0xf48f...10fe` | `LONG` | 2,764,016.69 USD | `2,218.49` | `1517.87` | `1250.50` | `982.04` | -603,370.13 USD | `-21.83%` | `3X Cross` |
| `864` | `0x5bc4...3b0c` | `SHORT` | 2,658,950.45 USD | `2,130.74` | `1089.65` | `1250.50` | `3677.88` | -337,192.87 USD | `-12.68%` | `5X Cross` |
| `876` | `0x8de4...b9aa` | `SHORT` | 2,609,929.92 USD | `2,091.29` | `1331.35` | `1250.50` | `1690.04` | 174,309.79 USD | `+6.68%` | `3X Cross` |
| `877` | `0x71d0...8c26` | `SHORT` | 2,598,781.34 USD | `2,082.19` | `1266.91` | `1250.50` | `3870.10` | 39,157.42 USD | `+1.51%` | `10X Cross` |
| `880` | `0x4fe2...ac59` | `SHORT` | 2,585,526.52 USD | `2,071.57` | `1478.56` | `1250.50` | `1846.15` | 477,419.70 USD | `+18.47%` | `10X Cross` |
| `884` | `0xdf57...93f5` | `LONG` | 2,563,515.31 USD | `2,054.35` | `1227.36` | `1250.50` | `897.38` | 42,093.26 USD | `+1.64%` | `4X Isolated` |
| `892` | `0xbcd4...0dd2` | `LONG` | 2,538,942.34 USD | `2,033.92` | `1228.20` | `1250.50` | `743.28` | 40,891.52 USD | `+1.61%` | `10X Cross` |
| `905` | `0x9a99...d21a` | `LONG` | 2,496,200.00 USD | `2,000.00` | `1278.44` | `1250.50` | `0.000000` | -60,673.67 USD | `-2.43%` | `10X Cross` |
| `906` | `0xf29c...9971` | `LONG` | 2,496,200.00 USD | `2,000.00` | `1254.95` | `1250.50` | `0.000000` | -13,697.07 USD | `-0.55%` | `10X Cross` |
| `927` | `0x77ee...2902` | `SHORT` | 2,429,229.25 USD | `1,946.03` | `759.84` | `1250.50` | `5671.24` | -950,551.74 USD | `-39.13%` | `10X Cross` |
| `935` | `0x3e2f...b269` | `SHORT` | 2,402,843.93 USD | `1,925.51` | `1134.87` | `1250.50` | `2977.31` | -217,645.07 USD | `-9.06%` | `10X Cross` |
| `949` | `0x4f12...618b` | `SHORT` | 2,366,557.44 USD | `1,896.28` | `1608.30` | `1250.50` | `2116.93` | 683,226.95 USD | `+28.87%` | `3X Cross` |
| `992` | `0x866d...d6e1` | `LONG` | 2,249,499.02 USD | `1,802.05` | `674.73` | `1250.50` | `155.93` | 1,033,597.70 USD | `+45.95%` | `10X Cross` |
| `1023` | `0x2309...a2d9` | `LONG` | 2,180,260.87 USD | `1,750.37` | `1186.09` | `1250.50` | `808.75` | 104,166.76 USD | `+4.78%` | `8X Cross` |
| `1067` | `0x265e...7f70` | `LONG` | 2,061,371.52 USD | `1,651.74` | `1382.98` | `1250.50` | `0.000000` | -222,951.24 USD | `-10.82%` | `3X Cross` |
| `1072` | `0xfe7c...b7ae` | `SHORT` | 2,050,178.98 USD | `1,642.64` | `1346.92` | `1250.50` | `5703.44` | 162,329.64 USD | `+7.92%` | `10X Cross` |
| `1074` | `0x3e47...aaf6` | `LONG` | 2,041,913.81 USD | `1,636.28` | `1278.38` | `1250.50` | `1050.91` | -49,877.97 USD | `-2.44%` | `10X Cross` |
| `1075` | `0x2edd...8179` | `SHORT` | 2,041,804.23 USD | `1,635.93` | `1261.55` | `1250.50` | `2878.81` | 21,996.24 USD | `+1.08%` | `10X Cross` |
| `1099` | `0x7f75...9edf` | `LONG` | 2,012,310.59 USD | `1,612.17` | `1200.26` | `1250.50` | `986.23` | 77,289.51 USD | `+3.84%` | `10X Cross` |
| `1105` | `0x6646...6de5` | `SHORT` | 1,994,560.00 USD | `1,600.00` | `660.64` | `1250.50` | `4187.24` | -937,535.03 USD | `-47.00%` | `10X Cross` |
| `1113` | `0x023a...2355` | `SHORT` | 1,986,114.01 USD | `1,591.31` | `1310.00` | `1250.50` | `4425.96` | 98,495.24 USD | `+4.96%` | `10X Cross` |
| `1122` | `0xfc27...9d9d` | `SHORT` | 1,970,366.65 USD | `1,578.44` | `1295.79` | `1250.50` | `12742.65` | 74,957.56 USD | `+3.80%` | `10X Cross` |
| `1131` | `0xab59...59b5` | `LONG` | 1,953,362.83 USD | `1,565.32` | `1342.15` | `1250.50` | `834.07` | -147,532.39 USD | `-7.55%` | `10X Cross` |
| `1173` | `0x039c...0ebd` | `SHORT` | 1,898,257.62 USD | `1,521.39` | `1245.17` | `1250.50` | `3741.79` | -3,863.77 USD | `-0.20%` | `10X Cross` |
| `1187` | `0xcf67...eb24` | `LONG` | 1,872,150.00 USD | `1,500.00` | `887.05` | `1250.50` | `620.80` | 541,578.63 USD | `+28.93%` | `10X Cross` |
| `1206` | `0x7277...0b98` | `SHORT` | 1,841,485.84 USD | `1,475.73` | `1287.86` | `1250.50` | `2188.94` | 59,046.28 USD | `+3.21%` | `10X Cross` |
| `1276` | `0x2ab7...c2f8` | `LONG` | 1,745,455.61 USD | `1,400.51` | `813.26` | `1250.50` | `792.53` | 606,473.93 USD | `+34.75%` | `3X Cross` |
| `1291` | `0x11be...8b1d` | `LONG` | 1,717,173.42 USD | `1,375.83` | `1206.55` | `1250.50` | `1134.65` | 57,165.47 USD | `+3.33%` | `10X Isolated` |
| `1305` | `0x3205...40bb` | `SHORT` | 1,679,721.32 USD | `1,346.47` | `1257.43` | `1250.50` | `2353.11` | 13,368.27 USD | `+0.80%` | `10X Cross` |
| `1371` | `0xe065...0f85` | `SHORT` | 1,575,863.54 USD | `1,262.61` | `1087.02` | `1250.50` | `1549.37` | -203,387.41 USD | `-12.91%` | `10X Cross` |
| `1387` | `0x413c...886c` | `LONG` | 1,559,875.00 USD | `1,250.00` | `1237.51` | `1250.50` | `0.000000` | 12,985.54 USD | `+0.83%` | `10X Cross` |
| `1414` | `0xdf83...3cff` | `SHORT` | 1,549,876.80 USD | `1,241.59` | `1260.63` | `1250.50` | `1837.09` | 15,305.36 USD | `+0.99%` | `10X Cross` |
| `1452` | `0x2847...d47b` | `LONG` | 1,512,577.59 USD | `1,211.71` | `1232.45` | `1250.50` | `0.000000` | 19,209.99 USD | `+1.27%` | `5X Cross` |
| `1462` | `0x5975...9abd` | `LONG` | 1,497,720.00 USD | `1,200.00` | `1179.54` | `1250.50` | `535.91` | 82,277.21 USD | `+5.49%` | `5X Cross` |
| `1465` | `0x266b...efcb` | `LONG` | 1,495,200.00 USD | `1,200.00` | `893.76` | `1250.50` | `416.86` | 422,690.30 USD | `+28.27%` | `10X Cross` |
| `1493` | `0x69cc...14fd` | `SHORT` | 1,449,200.06 USD | `1,161.36` | `675.33` | `1250.50` | `8087.93` | -664,894.53 USD | `-45.88%` | `10X Cross` |
| `1505` | `0x3fc5...c0c1` | `SHORT` | 1,433,367.96 USD | `1,148.44` | `1264.34` | `1250.50` | `2765.56` | 18,645.81 USD | `+1.30%` | `10X Cross` |
| `1523` | `0xb2f7...af9f` | `SHORT` | 1,418,902.49 USD | `1,136.85` | `746.63` | `1250.50` | `7913.13` | -570,098.14 USD | `-40.18%` | `10X Cross` |
| `1551` | `0x5f94...4b96` | `LONG` | 1,391,745.43 USD | `1,115.27` | `538.00` | `1250.50` | `0.000000` | 791,727.80 USD | `+56.89%` | `10X Cross` |
| `1557` | `0xe35c...a1d3` | `LONG` | 1,385,199.10 USD | `1,111.36` | `1311.66` | `1250.50` | `690.94` | -72,525.04 USD | `-5.24%` | `2X Isolated` |
| `1584` | `0x71df...a23d` | `SHORT` | 1,368,566.71 USD | `1,098.28` | `513.50` | `1250.50` | `2560.67` | -804,596.52 USD | `-58.79%` | `2X Cross` |
| `1598` | `0xbfc7...80b4` | `SHORT` | 1,341,922.50 USD | `1,075.00` | `558.03` | `1250.50` | `2668.50` | -742,043.77 USD | `-55.30%` | `10X Cross` |
| `1637` | `0x123d...3bff` | `SHORT` | 1,303,440.75 USD | `1,044.34` | `519.62` | `1250.50` | `4123.29` | -760,782.55 USD | `-58.37%` | `10X Cross` |
| `1705` | `0xe282...df29` | `LONG` | 1,246,400.00 USD | `1,000.00` | `420.99` | `1250.50` | `807.45` | 825,413.14 USD | `+66.22%` | `10X Cross` |
| `1708` | `0x668c...ea2e` | `SHORT` | 1,245,600.00 USD | `1,000.00` | `1406.98` | `1250.50` | `4211.60` | 161,381.99 USD | `+12.96%` | `10X Cross` |
| `1725` | `0x17f0...094f` | `LONG` | 1,226,044.08 USD | `984.30` | `1287.23` | `1250.50` | `537.00` | -40,976.08 USD | `-3.34%` | `5X Cross` |
| `1741` | `0x51f6...2b39` | `SHORT` | 1,214,164.16 USD | `972.81` | `1299.77` | `1250.50` | `2506.18` | 50,263.54 USD | `+4.14%` | `10X Cross` |
| `1806` | `0x757d...94ba` | `LONG` | 1,154,307.50 USD | `925.00` | `1558.31` | `1250.50` | `0.000000` | -287,133.09 USD | `-24.87%` | `10X Cross` |
| `1841` | `0xb911...5525` | `LONG` | 1,123,290.00 USD | `900.00` | `1294.82` | `1250.50` | `1035.43` | -42,047.82 USD | `-3.74%` | `10X Cross` |
| `1864` | `0xef96...9383` | `SHORT` | 1,108,025.74 USD | `887.77` | `1259.32` | `1250.50` | `5130.50` | 9,961.14 USD | `+0.90%` | `10X Cross` |
| `1875` | `0x5323...b23c` | `SHORT` | 1,098,841.04 USD | `880.27` | `1258.88` | `1250.50` | `7601.67` | 9,313.96 USD | `+0.85%` | `5X Cross` |
| `1887` | `0xcf0a...856f` | `LONG` | 1,087,369.43 USD | `871.15` | `1292.19` | `1250.50` | `1040.02` | -38,325.42 USD | `-3.52%` | `4X Cross` |
| `1908` | `0xdf95...7d72` | `SHORT` | 1,065,136.94 USD | `853.27` | `1074.39` | `1250.50` | `44985.04` | -148,389.50 USD | `-13.93%` | `10X Cross` |
| `1965` | `0x601c...4f54` | `SHORT` | 1,026,897.55 USD | `824.42` | `615.11` | `1250.50` | `3126.66` | -519,784.80 USD | `-50.62%` | `5X Cross` |
| `1972` | `0x38f9...cb04` | `SHORT` | 1,020,285.52 USD | `817.34` | `1253.34` | `1250.50` | `2321.23` | 4,117.14 USD | `+0.40%` | `10X Cross` |
| `1977` | `0xae55...2236` | `LONG` | 1,018,812.86 USD | `817.47` | `1467.80` | `1250.50` | `0.000000` | -181,068.36 USD | `-17.77%` | `10X Cross` |

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
| `5m` | `BALANCED` | 0.00 USD | 1,750.00 USD | 1,750.00 USD | 1,750.00 USD | `1` | `2026-10-30 08:50:00 UTC - 2026-10-30 08:55:00 UTC` |
| `15m` | `BALANCED` | 0.00 USD | 1,750.00 USD | 1,750.00 USD | 1,750.00 USD | `1` | `2026-10-30 08:45:00 UTC - 2026-10-30 09:00:00 UTC` |
| `1h` | `BALANCED` | 0.00 USD | 1,750.00 USD | 1,750.00 USD | 1,750.00 USD | `1` | `2026-10-30 08:00:00 UTC - 2026-10-30 09:00:00 UTC` |
| `4h` | `BALANCED` | 0.00 USD | 1,750.00 USD | 1,750.00 USD | 1,750.00 USD | `1` | `2026-10-30 08:00:00 UTC - 2026-10-30 12:00:00 UTC` |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `0 USD` | Total OI Tokens: `-`
  * 1h OI Change: `0.00%` | 4h OI Change: `0.00%` | 24h OI Change: `0.00%`
  * Exchange Breakdown: Binance=`-` | Bybit=`-` | OKX=`-` | Hyperliquid=`-`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `84.50K` | Last 24h: `171.90K` | Last 3d: `285.15K` | Last 7d: `847.79K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0100%` | **USDT OKX** | `0.0100%` |
| **USDT Bybit** | `0.0100%` | **USDT KuCoin** | `0.0100%` |
| **USDT MEXC** | `0.0098%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `0.0073%` | **USDT Bitget** | `0.0100%` |
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
| `0:00 UTC` | `1271.85` | `1274.42` | `1271.85` | `1282.95` | `1268.85` | 8,167,112.53 USD | 4,190,418.72 USD | 3,976,693.81 USD | 213,724.90 USD | `+2.62%` | `8B / 7S` |
| `5:00 UTC` | `1267.95` | `1271.35` | `1267.95` | `1277.85` | `1264.95` | 9,333,572.45 USD | 5,033,580.65 USD | 4,299,991.80 USD | 733,588.86 USD | `+7.86%` | `7B / 2S` |
| `0:00 UTC` | `1266.15` | `1267.62` | `1266.15` | `1278.45` | `1260.45` | 12,479,157.49 USD | 5,007,423.22 USD | 7,471,734.27 USD | -2,464,311.04 USD | `-19.75%` | `3B / 15S` |
| `5:00 UTC` | `1263.15` | `1263.66` | `1263.15` | `1267.05` | `1260.45` | 8,382,487.91 USD | 4,193,725.38 USD | 4,188,762.53 USD | 4,962.85 USD | `+0.06%` | `3B / 2S` |
| `0:00 UTC` | `1255.05` | `1256.16` | `1255.05` | `1269.15` | `1247.25` | 26,236,011.28 USD | 8,922,234.21 USD | 17,313,777.08 USD | -8,391,542.87 USD | `-31.98%` | `2B / 24S` |
| `5:00 UTC` | `1248.15` | `1248.05` | `1248.15` | `1253.25` | `1244.25` | 21,008,122.73 USD | 11,395,427.09 USD | 9,612,695.64 USD | 1,782,731.45 USD | `+8.49%` | `1B / 0S` |
| `0:00 UTC` | `1245.75` | `1245.57` | `1245.75` | `1250.55` | `1240.05` | 17,224,192.69 USD | 9,235,789.14 USD | 7,988,403.55 USD | 1,247,385.58 USD | `+7.24%` | `1B / 6S` |
| `5:00 UTC` | `1251.45` | `1250.99` | `1251.45` | `1255.05` | `1246.35` | 13,619,576.55 USD | 6,741,413.50 USD | 6,878,163.05 USD | -136,749.55 USD | `-1.00%` | `2B / 0S` |
| `0:00 UTC` | `1249.95` | `1249.10` | `1249.95` | `1253.55` | `1244.55` | 10,263,783.49 USD | 5,117,369.60 USD | 5,146,413.89 USD | -29,044.29 USD | `-0.28%` | `1B / 4S` |
| `5:00 UTC` | `1246.65` | `1246.72` | `1246.65` | `1252.35` | `1243.95` | 12,378,849.44 USD | 7,324,216.90 USD | 5,054,632.54 USD | 2,269,584.36 USD | `+18.33%` | `8B / 5S` |

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
| `5m` | -309,600.00 USD | -637,960.00 USD | **`DISTRIBUTION`** |
| `15m` | -542,810.00 USD | 1,210,000.00 USD | **`ACCUMULATION`** |
| `30m` | -1,150,000.00 USD | -1,220,000.00 USD | **`DISTRIBUTION`** |
| `1h` | 559,150.00 USD | 1,620,000.00 USD | **`ACCUMULATION`** |
| `2h` | 2,730,000.00 USD | -21,040,000.00 USD | **`DISTRIBUTION`** |
| `4h` | 1,940,000.00 USD | -32,010,000.00 USD | **`DISTRIBUTION`** |
| `6h` | 1,570,000.00 USD | -43,750,000.00 USD | **`DISTRIBUTION`** |
| `8h` | 7,200,000.00 USD | -18,230,000.00 USD | **`DISTRIBUTION`** |
| `12h` | 7,500,000.00 USD | -6,800,000.00 USD | **`ACCUMULATION`** |
| `24h` | 19,770,000.00 USD | 77,790,000.00 USD | **`ACCUMULATION`** |
| `1w` | 35,110,000.00 USD | 195,450,000.00 USD | **`ACCUMULATION`** |
| `30d` | 64,300,000.00 USD | -542,930,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-309.60K` | 15m=`-542.81K` | 1h=`+559.15K` | 24h=`+19.77M`
* Futures Capital Netflows: 5m=`-637.96K` | 15m=`+1.21M` | 1h=`+1.62M` | 24h=`+77.79M`
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
  * `2026-10-30 14:09:50 IST`: [channelnewsasia.com] - (Sentiment: `Neutral`)
  * `2026-10-30 13:51:50 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 13:50:50 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 13:31:50 IST`: [kof.ethz.ch] - (Sentiment: `Neutral`)
  * `2026-10-30 14:27:50 IST`: [gerlachmacro.substack.com] - (Sentiment: `Neutral`)
  * `2026-10-30 14:27:50 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-30 14:27:50 IST`: [insee.fr] - (Sentiment: `Neutral`)
  * `2026-10-30 14:27:50 IST`: [insee.fr] - (Sentiment: `Neutral`)
  * `2026-10-30 14:27:50 IST`: [@FirstSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 14:27:50 IST`: [nationwide.co.uk] - (Sentiment: `Neutral`)
  * `2026-10-30 14:27:50 IST`: [destatis.de] - (Sentiment: `Neutral`)
  * `2026-10-30 14:26:50 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-30 14:26:50 IST`: [@FirstSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 14:26:50 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-30 14:26:50 IST`: [insee.fr] - (Sentiment: `Neutral`)


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
  * Execution Entry: `1241.49` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `1236.44` (Risk Distance: `5.05` pts)
  * +2.5R Take Profit: `1254.12`
  * Mathematical Lot Sizing: **`1.97 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `1284.79` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `1289.84` (Risk Distance: `5.05` pts)
  * +2.5R Take Profit: `1272.16`
  * Mathematical Lot Sizing: **`1.97 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`1254.39`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
