# 🏛️ SOVEREIGN CANDIDATE DOSSIER: ZECUSD
**Canonical Key**: `ZECUSD` | **Broker Instrument**: `ZECUSD.p` | **Asset Class**: `Crypto Altcoin`
**Timestamp**: `2026-10-30 02:24:37 IST` (`2026-10-29 20:54:37 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `1247.85` | **Live Ask Quote**: `1249.74` | **Mid Price**: `1248.80`
- **Spread Points**: `189.00` | **Spread BPS**: `15.13 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `1248.80` | VWAP Z-Score: `+0.00` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `3.12` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `50.00` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `1257.54` | Lower -3.00σ Band: `1240.05`
  * Upper +2.51σ Band: `1255.66` | Lower -2.51σ Band: `1241.93`
  * Upper +2.01σ Band: `1254.04` | Lower -2.01σ Band: `1243.55`
  * Upper +2.00σ Band: `1253.79` | Lower -2.00σ Band: `1243.80`
  * Upper +1.28σ Band: `1252.29` | Lower -1.28σ Band: `1245.30`
  * Upper +1.00σ Band: `1251.29` | Lower -1.00σ Band: `1246.30`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`1248.80` | EMA-20=`1248.80` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`1248.80` (Slope: `+0.0000`) | EMA-100=`1248.80`
  * Institutional Anchors: EMA-144=`1248.80` | EMA-200=`1248.80` (Slope: `+0.0000`) | EMA-233=`1248.80`
- **Range Boundaries**: 24H High=`1261.28` | 24H Low=`1236.31` | Weekly High=`1273.77` | Weekly Low=`1223.82`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `1309.36` (Distance: `-4.76%`)
  * Point of Control (POC) = `1247.20` (Distance: `-0.01%`)
  * Value Area Low (VAL) = `1230.55` (Distance: `+1.34%`)
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
  * Golden Pocket Zone (0.618 - 0.650): `1243.80` - `1253.79`
  * Optimal Trade Entry (OTE 0.705): `1251.29`
  * Structural Invalidation Anchor (0.786): `1258.79`

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
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 02:14:34 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `16` | `0xb83d...6e36` | `SHORT` | 67,400,274.14 USD | `52,582.52` | `1336.45` | `1215.60` | `3869.60` | 2,873,640.76 USD | `+4.26%` | `3X Cross` |
| `26` | `0x5b5d...c060` | `SHORT` | 50,701,801.69 USD | `40,727.61` | `1478.36` | `1215.60` | `5452.21` | 9,508,462.50 USD | `+18.75%` | `3X Cross` |
| `43` | `0x7fda...17d1` | `SHORT` | 27,573,274.22 USD | `22,337.39` | `1261.69` | `1215.60` | `3044.14` | 609,690.22 USD | `+2.21%` | `5X Cross` |
| `76` | `0x60b0...991e` | `LONG` | 21,838,831.61 USD | `16,779.74` | `1179.65` | `1215.60` | `899.68` | 2,044,584.60 USD | `+9.36%` | `10X Cross` |
| `138` | `0xc36a...105b` | `LONG` | 14,989,389.80 USD | `11,510.82` | `1215.14` | `1215.60` | `939.41` | 1,002,108.78 USD | `+6.69%` | `10X Cross` |
| `179` | `0x8742...8427` | `LONG` | 11,454,586.33 USD | `9,201.21` | `1286.37` | `1215.60` | `698.37` | -381,583.66 USD | `-3.33%` | `10X Cross` |
| `200` | `0x9071...5c0b` | `LONG` | 10,894,556.57 USD | `8,829.94` | `1370.53` | `1215.60` | `579.52` | -1,207,132.08 USD | `-11.08%` | `2X Cross` |
| `201` | `0xad59...ba81` | `SHORT` | 10,804,220.00 USD | `8,425.00` | `330.91` | `1215.60` | `2144.15` | -8,016,262.23 USD | `-74.20%` | `10X Cross` |
| `205` | `0x9ffd...ce40` | `LONG` | 10,671,461.01 USD | `8,543.32` | `1256.92` | `1215.60` | `611.02` | -66,820.47 USD | `-0.63%` | `5X Cross` |
| `220` | `0xdd53...2b13` | `SHORT` | 10,139,694.89 USD | `8,214.27` | `739.37` | `1215.60` | `8607.28` | -4,066,286.63 USD | `-40.10%` | `3X Cross` |
| `235` | `0x880a...311c` | `SHORT` | 9,842,750.18 USD | `7,707.11` | `1367.50` | `1215.60` | `2282.91` | 696,734.02 USD | `+7.08%` | `10X Cross` |
| `264` | `0xfc66...ca06` | `SHORT` | 9,002,468.92 USD | `7,296.42` | `1319.65` | `1215.60` | `5955.83` | 626,271.13 USD | `+6.96%` | `10X Cross` |
| `269` | `0x2b61...2f6c` | `LONG` | 8,864,075.40 USD | `6,807.00` | `1453.56` | `1215.60` | `621.05` | -1,030,275.82 USD | `-11.62%` | `10X Cross` |
| `310` | `0x2ae5...83e7` | `LONG` | 7,944,298.56 USD | `6,436.80` | `1391.82` | `1215.60` | `482.34` | -1,014,593.43 USD | `-12.77%` | `2X Cross` |
| `323` | `0xbf73...5d58` | `LONG` | 7,480,800.00 USD | `6,000.00` | `1214.30` | `1215.60` | `0.000000` | 194,987.91 USD | `+2.61%` | `10X Cross` |
| `326` | `0x5323...b23c` | `LONG` | 7,441,760.65 USD | `6,031.48` | `1249.23` | `1215.60` | `279.12` | -92,934.23 USD | `-1.25%` | `5X Cross` |
| `348` | `0x26b6...9a13` | `LONG` | 6,707,396.31 USD | `5,433.73` | `1282.23` | `1215.60` | `211.02` | -259,906.92 USD | `-3.87%` | `10X Cross` |
| `365` | `0xea00...a918` | `LONG` | 6,508,000.00 USD | `5,000.00` | `739.16` | `1215.60` | `0.000000` | 2,812,184.89 USD | `+43.21%` | `5X Cross` |
| `372` | `0x45d2...4029` | `SHORT` | 6,449,177.14 USD | `5,227.00` | `833.44` | `1215.60` | `9059.51` | -2,092,799.17 USD | `-32.45%` | `5X Cross` |
| `388` | `0xdd7a...8830` | `LONG` | 6,232,707.66 USD | `4,860.19` | `897.48` | `1215.60` | `792.02` | 1,870,803.98 USD | `+30.02%` | `10X Cross` |
| `391` | `0xf081...e39e` | `LONG` | 6,137,288.70 USD | `4,717.00` | `1195.70` | `1215.60` | `1200.11` | 497,164.66 USD | `+8.10%` | `10X Cross` |
| `439` | `0x4cae...7c34` | `LONG` | 5,210,072.80 USD | `4,004.36` | `999.34` | `1215.60` | `807.77` | 1,208,344.64 USD | `+23.19%` | `10X Cross` |
| `457` | `0xa61c...66b9` | `LONG` | 4,978,584.00 USD | `3,888.00` | `1148.34` | `1215.60` | `0.000000` | 513,841.86 USD | `+10.32%` | `10X Cross` |
| `458` | `0xecb6...2b00` | `SHORT` | 4,964,240.28 USD | `4,020.82` | `1319.32` | `1215.60` | `7791.16` | 340,519.26 USD | `+6.86%` | `5X Cross` |
| `473` | `0x9aa5...58af` | `SHORT` | 4,844,587.68 USD | `3,720.31` | `1205.51` | `1215.60` | `3396.37` | -359,700.88 USD | `-7.42%` | `10X Cross` |
| `496` | `0x0153...8052` | `SHORT` | 4,578,346.84 USD | `3,698.18` | `1307.82` | `1215.60` | `2504.70` | 258,223.91 USD | `+5.64%` | `1X Isolated` |
| `536` | `0xd21d...90f1` | `LONG` | 4,167,800.00 USD | `3,250.00` | `1253.64` | `1215.60` | `875.90` | 93,458.27 USD | `+2.24%` | `4X Isolated` |
| `543` | `0xd4c1...3d1d` | `SHORT` | 4,120,403.58 USD | `3,339.55` | `1302.99` | `1215.60` | `3042.77` | 230,992.21 USD | `+5.61%` | `10X Cross` |
| `546` | `0x1338...c48e` | `LONG` | 4,098,353.26 USD | `3,149.43` | `1018.52` | `1215.60` | `820.19` | 890,607.72 USD | `+21.73%` | `4X Isolated` |
| `558` | `0x27c9...d65d` | `SHORT` | 4,036,075.47 USD | `3,186.04` | `1254.40` | `1215.60` | `1769.88` | -39,518.18 USD | `-0.98%` | `10X Cross` |
| `564` | `0x456f...cdf1` | `LONG` | 4,021,376.54 USD | `3,134.11` | `1268.52` | `1215.60` | `493.54` | 45,686.90 USD | `+1.14%` | `10X Cross` |
| `587` | `0x382b...3e39` | `LONG` | 3,932,798.40 USD | `3,186.00` | `1207.77` | `1215.60` | `0.000000` | 84,837.19 USD | `+2.16%` | `10X Cross` |
| `592` | `0x9c06...0560` | `SHORT` | 3,905,575.74 USD | `2,989.80` | `786.00` | `1215.60` | `2403.22` | -1,555,580.74 USD | `-39.83%` | `10X Cross` |
| `601` | `0xdbe0...d6d5` | `LONG` | 3,819,688.06 USD | `3,085.37` | `422.97` | `1215.60` | `338.51` | 2,514,683.57 USD | `+65.83%` | `3X Isolated` |
| `640` | `0x2e30...4cb5` | `SHORT` | 3,577,612.14 USD | `2,898.26` | `1299.68` | `1215.60` | `2916.93` | 189,196.47 USD | `+5.29%` | `2X Cross` |
| `689` | `0xac48...3201` | `LONG` | 3,319,664.04 USD | `2,540.30` | `1393.86` | `1215.60` | `530.24` | -221,165.25 USD | `-6.66%` | `10X Cross` |
| `697` | `0x58b2...11f3` | `LONG` | 3,284,909.18 USD | `2,663.08` | `1288.37` | `1215.60` | `0.000000` | -146,123.13 USD | `-4.45%` | `10X Cross` |
| `703` | `0x0871...e927` | `LONG` | 3,255,500.00 USD | `2,500.00` | `1276.50` | `1215.60` | `0.000000` | 64,250.00 USD | `+1.97%` | `10X Cross` |
| `722` | `0x325e...9564` | `LONG` | 3,188,434.10 USD | `2,501.91` | `1306.24` | `1215.60` | `0.000000` | -79,659.80 USD | `-2.50%` | `10X Cross` |
| `725` | `0x9b86...6e6e` | `LONG` | 3,164,065.52 USD | `2,467.30` | `637.58` | `1215.60` | `889.66` | 1,590,965.92 USD | `+50.28%` | `3X Cross` |
| `730` | `0xa183...0482` | `LONG` | 3,154,576.60 USD | `2,534.00` | `530.25` | `1215.60` | `444.43` | 1,810,913.88 USD | `+57.41%` | `5X Isolated` |
| `781` | `0x634f...6951` | `LONG` | 2,968,462.25 USD | `2,272.42` | `1281.94` | `1215.60` | `1250.04` | 55,361.78 USD | `+1.86%` | `10X Cross` |
| `782` | `0xb2f7...af9f` | `SHORT` | 2,967,114.53 USD | `2,313.72` | `746.63` | `1215.60` | `4281.59` | -1,239,625.78 USD | `-41.78%` | `10X Cross` |
| `811` | `0xf48f...10fe` | `LONG` | 2,843,882.33 USD | `2,218.49` | `1517.87` | `1215.60` | `947.27` | -523,504.49 USD | `-18.41%` | `3X Cross` |
| `845` | `0x8de4...b9aa` | `SHORT` | 2,733,943.42 USD | `2,091.29` | `1331.35` | `1215.60` | `1689.83` | 50,296.29 USD | `+1.84%` | `3X Cross` |
| `852` | `0x4fe2...ac59` | `SHORT` | 2,706,091.89 USD | `2,071.57` | `1478.56` | `1215.60` | `1831.35` | 356,854.32 USD | `+13.19%` | `10X Cross` |
| `856` | `0x5bc4...3b0c` | `SHORT` | 2,682,209.82 USD | `2,130.74` | `1089.65` | `1215.60` | `3654.35` | -360,452.24 USD | `-13.44%` | `5X Cross` |
| `868` | `0x4e23...20c3` | `LONG` | 2,624,819.26 USD | `2,070.21` | `1296.80` | `1215.60` | `0.000000` | -59,822.53 USD | `-2.28%` | `4X Cross` |
| `876` | `0x668c...ea2e` | `SHORT` | 2,604,400.00 USD | `2,000.00` | `1406.98` | `1215.60` | `2702.62` | 209,563.99 USD | `+8.05%` | `10X Cross` |
| `899` | `0x77ee...2902` | `SHORT` | 2,531,979.63 USD | `1,946.03` | `759.84` | `1215.60` | `5234.95` | -1,053,302.13 USD | `-41.60%` | `10X Cross` |
| `914` | `0x4f12...618b` | `SHORT` | 2,479,006.84 USD | `1,896.28` | `1608.30` | `1215.60` | `2116.72` | 570,777.55 USD | `+23.02%` | `3X Cross` |
| `932` | `0x3e2f...b269` | `SHORT` | 2,420,366.07 USD | `1,925.51` | `1134.87` | `1215.60` | `2931.75` | -235,167.21 USD | `-9.72%` | `10X Cross` |
| `946` | `0x3205...40bb` | `LONG` | 2,378,861.90 USD | `1,928.39` | `1240.20` | `1215.60` | `444.06` | -12,719.22 USD | `-0.53%` | `10X Cross` |
| `955` | `0xe097...d0fe` | `LONG` | 2,362,672.53 USD | `1,913.56` | `1261.17` | `1215.60` | `0.000000` | -50,653.63 USD | `-2.14%` | `10X Cross` |
| `960` | `0x866d...d6e1` | `LONG` | 2,344,647.25 USD | `1,802.05` | `674.73` | `1215.60` | `125.55` | 1,128,745.94 USD | `+48.14%` | `10X Cross` |
| `991` | `0x2309...a2d9` | `LONG` | 2,277,581.44 USD | `1,750.37` | `1186.09` | `1215.60` | `807.10` | 201,487.33 USD | `+8.85%` | `8X Cross` |
| `1016` | `0xf5a5...1286` | `LONG` | 2,198,642.56 USD | `1,781.98` | `1240.37` | `1215.60` | `0.000000` | -11,680.47 USD | `-0.53%` | `10X Cross` |
| `1050` | `0xa271...a3f7` | `LONG` | 2,123,469.29 USD | `1,631.43` | `1190.60` | `1215.60` | `910.29` | 181,087.48 USD | `+8.53%` | `4X Cross` |
| `1062` | `0x2edd...8179` | `SHORT` | 2,099,776.57 USD | `1,701.85` | `1261.58` | `1215.60` | `3078.72` | 47,242.29 USD | `+2.25%` | `10X Cross` |
| `1063` | `0x3e47...aaf6` | `LONG` | 2,098,692.73 USD | `1,636.28` | `1279.54` | `1215.60` | `1044.12` | 5,000.64 USD | `+0.24%` | `10X Cross` |
| `1066` | `0x7f75...9edf` | `LONG` | 2,097,630.41 USD | `1,605.78` | `1199.97` | `1215.60` | `974.03` | 170,738.52 USD | `+8.14%` | `10X Cross` |
| `1073` | `0x265e...7f70` | `LONG` | 2,084,824.78 USD | `1,601.74` | `1388.09` | `1215.60` | `0.000000` | -138,540.22 USD | `-6.65%` | `3X Cross` |
| `1080` | `0x023a...2355` | `SHORT` | 2,074,672.74 USD | `1,696.38` | `1313.00` | `1215.60` | `5965.53` | 152,674.56 USD | `+7.36%` | `10X Cross` |
| `1094` | `0xab59...59b5` | `LONG` | 2,037,263.98 USD | `1,565.32` | `1342.15` | `1215.60` | `804.58` | -63,631.24 USD | `-3.12%` | `10X Cross` |
| `1108` | `0xdf57...93f5` | `LONG` | 2,018,459.35 USD | `1,579.76` | `1218.38` | `1215.60` | `780.13` | 93,703.37 USD | `+4.64%` | `3X Isolated` |
| `1150` | `0x6646...6de5` | `SHORT` | 1,975,520.00 USD | `1,600.00` | `660.64` | `1215.60` | `4428.32` | -918,495.03 USD | `-46.49%` | `10X Cross` |
| `1170` | `0xfe7c...b7ae` | `SHORT` | 1,942,331.32 USD | `1,562.49` | `1350.62` | `1215.60` | `7366.03` | 167,997.73 USD | `+8.65%` | `10X Cross` |
| `1210` | `0xcf67...eb24` | `LONG` | 1,867,350.00 USD | `1,500.00` | `887.05` | `1215.60` | `656.30` | 536,778.63 USD | `+28.75%` | `10X Cross` |
| `1273` | `0x039c...0ebd` | `SHORT` | 1,803,289.62 USD | `1,461.10` | `1238.67` | `1215.60` | `3330.91` | 6,523.98 USD | `+0.36%` | `10X Cross` |
| `1280` | `0x11be...8b1d` | `LONG` | 1,790,780.33 USD | `1,375.83` | `1206.55` | `1215.60` | `1134.41` | 130,772.37 USD | `+7.30%` | `10X Isolated` |
| `1304` | `0x2ab7...c2f8` | `LONG` | 1,728,789.54 USD | `1,400.51` | `813.26` | `1215.60` | `812.02` | 589,807.86 USD | `+34.12%` | `3X Cross` |
| `1368` | `0xe065...0f85` | `SHORT` | 1,643,413.18 USD | `1,262.61` | `1087.02` | `1215.60` | `1772.03` | -270,937.05 USD | `-16.49%` | `10X Cross` |
| `1375` | `0xdf83...3cff` | `SHORT` | 1,630,333.80 USD | `1,320.75` | `1251.92` | `1215.60` | `1757.71` | 23,135.78 USD | `+1.42%` | `10X Cross` |
| `1425` | `0xef96...9383` | `SHORT` | 1,580,393.10 USD | `1,280.50` | `1249.96` | `1215.60` | `4587.78` | 20,174.59 USD | `+1.28%` | `10X Cross` |
| `1431` | `0x7277...0b98` | `SHORT` | 1,577,908.39 USD | `1,234.96` | `1298.48` | `1215.60` | `2398.97` | 25,661.03 USD | `+1.63%` | `10X Cross` |
| `1447` | `0x5975...9abd` | `LONG` | 1,561,920.00 USD | `1,200.00` | `1179.54` | `1215.60` | `425.43` | 146,477.21 USD | `+9.38%` | `5X Cross` |
| `1454` | `0xfc27...9d9d` | `SHORT` | 1,558,763.29 USD | `1,262.77` | `1317.11` | `1215.60` | `14765.78` | 104,440.43 USD | `+6.70%` | `10X Cross` |
| `1518` | `0x69cc...14fd` | `SHORT` | 1,482,476.04 USD | `1,161.36` | `675.33` | `1215.60` | `8066.80` | -698,170.51 USD | `-47.09%` | `10X Cross` |
| `1534` | `0x38f9...cb04` | `LONG` | 1,450,376.87 USD | `1,176.49` | `1244.90` | `1215.60` | `431.97` | -14,231.48 USD | `-0.98%` | `10X Cross` |
| `1550` | `0xe35c...a1d3` | `LONG` | 1,436,325.26 USD | `1,127.06` | `1318.20` | `1215.60` | `694.33` | -49,370.09 USD | `-3.44%` | `2X Isolated` |
| `1554` | `0x3fc5...c0c1` | `SHORT` | 1,434,860.94 USD | `1,148.44` | `1264.34` | `1215.60` | `3450.21` | 17,152.84 USD | `+1.20%` | `10X Cross` |
| `1557` | `0x5f94...4b96` | `LONG` | 1,430,222.25 USD | `1,115.27` | `538.00` | `1215.60` | `0.000000` | 830,204.61 USD | `+58.05%` | `10X Cross` |
| `1559` | `0x71df...a23d` | `SHORT` | 1,428,972.11 USD | `1,098.28` | `513.50` | `1215.60` | `2549.10` | -865,001.92 USD | `-60.53%` | `2X Cross` |
| `1583` | `0xbfc7...80b4` | `SHORT` | 1,398,897.50 USD | `1,075.00` | `558.03` | `1215.60` | `5655.03` | -799,018.77 USD | `-57.12%` | `10X Cross` |
| `1682` | `0x51f6...2b39` | `SHORT` | 1,288,837.04 USD | `1,044.10` | `1302.75` | `1215.60` | `2745.38` | 71,361.11 USD | `+5.54%` | `10X Cross` |
| `1684` | `0x123d...3bff` | `SHORT` | 1,287,537.89 USD | `1,008.41` | `489.46` | `1215.60` | `4334.52` | -793,963.87 USD | `-61.67%` | `10X Cross` |
| `1689` | `0xe282...df29` | `LONG` | 1,282,400.00 USD | `1,000.00` | `420.99` | `1215.60` | `146.57` | 861,413.14 USD | `+67.17%` | `10X Cross` |
| `1692` | `0x17f0...094f` | `LONG` | 1,280,672.73 USD | `984.30` | `1287.23` | `1215.60` | `536.76` | 13,652.57 USD | `+1.07%` | `5X Cross` |
| `1735` | `0x266b...efcb` | `LONG` | 1,238,000.00 USD | `1,000.00` | `826.11` | `1215.60` | `237.54` | 411,887.07 USD | `+33.27%` | `10X Cross` |
| `1814` | `0x757d...94ba` | `LONG` | 1,162,725.00 USD | `925.00` | `1558.31` | `1215.60` | `0.000000` | -278,715.59 USD | `-23.97%` | `10X Cross` |
| `1839` | `0xcf0a...856f` | `LONG` | 1,137,983.25 USD | `871.15` | `1292.19` | `1215.60` | `938.47` | 12,288.40 USD | `+1.08%` | `4X Cross` |
| `1849` | `0x2847...d47b` | `LONG` | 1,123,091.13 USD | `903.46` | `1239.25` | `1215.60` | `0.000000` | 3,473.84 USD | `+0.31%` | `5X Cross` |
| `1888` | `0x7a76...b16d` | `LONG` | 1,099,690.73 USD | `857.86` | `1358.50` | `1215.60` | `1221.22` | -65,712.24 USD | `-5.98%` | `10X Cross` |
| `1896` | `0xdf95...7d72` | `SHORT` | 1,088,721.42 USD | `881.77` | `1074.26` | `1215.60` | `45098.04` | -141,469.28 USD | `-12.99%` | `10X Cross` |
| `1920` | `0x601c...4f54` | `SHORT` | 1,072,817.75 USD | `824.42` | `615.11` | `1215.60` | `3003.21` | -565,704.99 USD | `-52.73%` | `5X Cross` |
| `1935` | `0xf096...7553` | `SHORT` | 1,058,913.68 USD | `858.24` | `1240.34` | `1215.60` | `3860.89` | 5,599.35 USD | `+0.53%` | `10X Cross` |
| `1957` | `0x71b1...79c8` | `LONG` | 1,035,963.00 USD | `812.52` | `1231.55` | `1215.60` | `751.45` | 35,307.55 USD | `+3.41%` | `10X Cross` |
| `1963` | `0xabdb...84ac` | `LONG` | 1,032,828.80 USD | `793.69` | `711.79` | `1215.60` | `664.33` | 467,888.44 USD | `+45.30%` | `3X Cross` |
| `1981` | `0x0f02...5384` | `LONG` | 1,022,195.67 USD | `800.78` | `1290.36` | `1215.60` | `303.48` | -11,098.40 USD | `-1.09%` | `3X Cross` |
| `2006` | `0xae55...2236` | `LONG` | 1,008,610.84 USD | `817.47` | `1467.80` | `1215.60` | `0.000000` | -191,270.38 USD | `-18.96%` | `10X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `1268.00` | 95,100.00 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Long: 95.10K USD at 1268.0000 USD [API] | `2026-10-22 08:34:05` |
| `ANNOUNCEMENT` | `INFO` | `1326.50` | 4,589.69 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Long: 4.59K USD at 1326.5000 USD [API] | `2026-10-27 23:06:49` |
| `ANNOUNCEMENT` | `INFO` | `1326.50` | 24,420.87 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Long: 24.42K USD at 1326.5000 USD [API] | `2026-10-27 23:06:49` |
| `ANNOUNCEMENT` | `INFO` | `1326.50` | 20,640.34 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Long: 20.64K USD at 1326.5000 USD [API] | `2026-10-27 23:06:49` |
| `ANNOUNCEMENT` | `INFO` | `1326.10` | 2,081.98 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Long: 2.08K USD at 1326.1000 USD [API] | `2026-10-27 23:06:49` |
| `ANNOUNCEMENT` | `INFO` | `1326.10` | 13.26 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Long: 0.01K USD at 1326.1000 USD [API] | `2026-10-27 23:06:49` |
| `ANNOUNCEMENT` | `INFO` | `1326.10` | 530.44 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Long: 0.53K USD at 1326.1000 USD [API] | `2026-10-27 23:06:49` |
| `ANNOUNCEMENT` | `INFO` | `1326.10` | 26.52 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Long: 0.03K USD at 1326.1000 USD [API] | `2026-10-27 23:06:49` |
| `ANNOUNCEMENT` | `INFO` | `1326.10` | 106.09 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Long: 0.11K USD at 1326.1000 USD [API] | `2026-10-27 23:06:49` |
| `ANNOUNCEMENT` | `INFO` | `1326.10` | 1,710.67 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Long: 1.71K USD at 1326.1000 USD [API] | `2026-10-27 23:06:49` |
| `ANNOUNCEMENT` | `INFO` | `1326.10` | 397.83 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Long: 0.40K USD at 1326.1000 USD [API] | `2026-10-27 23:06:49` |
| `ANNOUNCEMENT` | `INFO` | `1326.10` | 39.78 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Long: 0.04K USD at 1326.1000 USD [API] | `2026-10-27 23:06:49` |
| `ANNOUNCEMENT` | `INFO` | `1326.50` | 10,187.52 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Long: 10.19K USD at 1326.5000 USD [API] | `2026-10-27 23:06:49` |
| `ANNOUNCEMENT` | `INFO` | `1326.20` | 10,185.22 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Long: 10.19K USD at 1326.2000 USD [API] | `2026-10-27 23:06:49` |
| `ANNOUNCEMENT` | `INFO` | `1216.00` | 9,496.96 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 9.50K USD at 1216.0000 USD [API] | `2026-10-25 01:39:18` |
| `ANNOUNCEMENT` | `INFO` | `1216.00` | 1,094.40 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 1.09K USD at 1216.0000 USD [API] | `2026-10-25 01:39:18` |
| `ANNOUNCEMENT` | `INFO` | `1216.00` | 997.12 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 1.00K USD at 1216.0000 USD [API] | `2026-10-25 01:39:18` |
| `ANNOUNCEMENT` | `INFO` | `1216.00` | 3,502.08 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 3.50K USD at 1216.0000 USD [API] | `2026-10-25 01:39:18` |
| `ANNOUNCEMENT` | `INFO` | `1216.00` | 36.48 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 0.04K USD at 1216.0000 USD [API] | `2026-10-25 01:39:18` |
| `ANNOUNCEMENT` | `INFO` | `1216.00` | 24.32 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 0.02K USD at 1216.0000 USD [API] | `2026-10-25 01:39:18` |
| `ANNOUNCEMENT` | `INFO` | `1216.00` | 12.16 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 0.01K USD at 1216.0000 USD [API] | `2026-10-25 01:39:18` |
| `ANNOUNCEMENT` | `INFO` | `1216.00` | 17,096.96 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 17.10K USD at 1216.0000 USD [API] | `2026-10-25 01:39:18` |
| `ANNOUNCEMENT` | `INFO` | `1158.50` | 3,614.52 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Long: 3.61K USD at 1158.5000 USD [API] | `2026-10-14 14:36:47` |
| `ANNOUNCEMENT` | `INFO` | `1158.60` | 104.27 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Long: 0.10K USD at 1158.6000 USD [API] | `2026-10-14 14:36:47` |
| `ANNOUNCEMENT` | `INFO` | `1158.60` | 69.52 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Long: 0.07K USD at 1158.6000 USD [API] | `2026-10-14 14:36:47` |
| `ANNOUNCEMENT` | `INFO` | `1158.70` | 11.59 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Long: 0.01K USD at 1158.7000 USD [API] | `2026-10-14 14:36:47` |
| `ANNOUNCEMENT` | `INFO` | `1158.70` | 11.59 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Long: 0.01K USD at 1158.7000 USD [API] | `2026-10-14 14:36:47` |
| `ANNOUNCEMENT` | `INFO` | `1158.80` | 11.59 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Long: 0.01K USD at 1158.8000 USD [API] | `2026-10-14 14:36:47` |
| `ANNOUNCEMENT` | `INFO` | `1158.90` | 660.57 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Long: 0.66K USD at 1158.9000 USD [API] | `2026-10-14 14:36:47` |
| `ANNOUNCEMENT` | `INFO` | `1158.90` | 1,170.49 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Long: 1.17K USD at 1158.9000 USD [API] | `2026-10-14 14:36:47` |
| `ANNOUNCEMENT` | `INFO` | `1158.90` | 1,158.90 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Long: 1.16K USD at 1158.9000 USD [API] | `2026-10-14 14:36:47` |
| `ANNOUNCEMENT` | `INFO` | `1127.70` | 2,153.91 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Long: 2.15K USD at 1127.7000 USD [API] | `2026-09-15 08:08:11` |
| `ANNOUNCEMENT` | `INFO` | `1330.10` | 53.20 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Long: 0.05K USD at 1330.1000 USD [API] | `2026-10-28 04:31:27` |
| `ANNOUNCEMENT` | `INFO` | `1330.10` | 26.60 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Long: 0.03K USD at 1330.1000 USD [API] | `2026-10-28 04:31:27` |
| `ANNOUNCEMENT` | `INFO` | `1330.10` | 26.60 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Long: 0.03K USD at 1330.1000 USD [API] | `2026-10-28 04:31:27` |
| `ANNOUNCEMENT` | `INFO` | `1330.10` | 305.92 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Long: 0.31K USD at 1330.1000 USD [API] | `2026-10-28 04:31:27` |
| `ANNOUNCEMENT` | `INFO` | `1330.10` | 79.81 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Long: 0.08K USD at 1330.1000 USD [API] | `2026-10-28 04:31:27` |


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
  * Current Rate: `31.06K` | Last 24h: `33.19K` | Last 3d: `283.86K` | Last 7d: `777.60K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `-0.0004%` | **USDT OKX** | `0.0094%` |
| **USDT Bybit** | `0.0100%` | **USDT KuCoin** | `0.0059%` |
| **USDT MEXC** | `-0.0004%` | **USDT BingX** | `0.0005%` |
| **USDT Gate** | `0.0003%` | **USDT Bitget** | `0.0100%` |
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
| `0:00 UTC` | `1315.95` | `1314.40` | `1315.95` | `1321.95` | `1307.85` | 50,919,152.62 USD | 22,517,005.07 USD | 28,402,147.55 USD | -5,885,142.49 USD | `-11.56%` | `2B / 5S` |
| `5:00 UTC` | `1315.95` | `1319.00` | `1315.95` | `1325.85` | `1312.05` | 22,246,351.59 USD | 13,151,982.06 USD | 9,094,369.53 USD | 4,057,612.52 USD | `+18.24%` | `9B / 1S` |
| `0:00 UTC` | `1320.75` | `1319.74` | `1320.75` | `1325.25` | `1315.95` | 11,564,611.33 USD | 5,754,638.99 USD | 5,809,972.34 USD | -55,333.35 USD | `-0.48%` | `1B / 2S` |
| `5:00 UTC` | `1322.85` | `1320.89` | `1322.85` | `1324.95` | `1316.85` | 7,868,027.33 USD | 4,223,932.72 USD | 3,644,094.61 USD | 579,838.11 USD | `+7.37%` | `3B / 0S` |
| `0:00 UTC` | `1324.95` | `1324.41` | `1324.95` | `1327.05` | `1319.85` | 12,000,472.36 USD | 6,714,467.49 USD | 5,286,004.87 USD | 1,428,462.62 USD | `+11.90%` | `2B / 1S` |
| `5:00 UTC` | `1325.25` | `1325.38` | `1325.25` | `1330.65` | `1320.75` | 11,021,893.68 USD | 5,577,839.59 USD | 5,444,054.10 USD | 133,785.49 USD | `+1.21%` | `3B / 1S` |
| `0:00 UTC` | `1294.05` | `1302.04` | `1294.05` | `1328.55` | `1286.25` | 68,949,402.59 USD | 35,232,633.05 USD | 33,716,769.55 USD | 1,515,863.50 USD | `+2.20%` | `6B / 24S` |
| `5:00 UTC` | `1306.05` | `1306.88` | `1306.05` | `1312.05` | `1300.05` | 17,712,248.68 USD | 9,074,345.66 USD | 8,637,903.02 USD | 436,442.64 USD | `+2.46%` | `3B / 5S` |
| `0:00 UTC` | `1249.20` | `1269.32` | `1249.20` | `1308.60` | `1241.40` | 130,590,816.99 USD | 58,796,845.15 USD | 71,793,971.84 USD | -12,997,126.69 USD | `-9.95%` | `4B / 19S` |
| `5:00 UTC` | `1229.25` | `1231.87` | `1229.25` | `1254.45` | `1206.75` | 110,295,078.04 USD | 55,880,373.46 USD | 54,414,704.58 USD | 1,465,668.88 USD | `+1.33%` | `11B / 11S` |

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
| `5m` | -3,020,000.00 USD | -13,850,000.00 USD | **`DISTRIBUTION`** |
| `15m` | -9,420,000.00 USD | -22,750,000.00 USD | **`DISTRIBUTION`** |
| `30m` | -9,390,000.00 USD | -21,430,000.00 USD | **`DISTRIBUTION`** |
| `1h` | -12,550,000.00 USD | -31,760,000.00 USD | **`DISTRIBUTION`** |
| `2h` | -12,220,000.00 USD | -15,090,000.00 USD | **`DISTRIBUTION`** |
| `4h` | -8,240,000.00 USD | -47,550,000.00 USD | **`DISTRIBUTION`** |
| `6h` | 10,190,000.00 USD | 36,070,000.00 USD | **`ACCUMULATION`** |
| `8h` | 16,580,000.00 USD | 68,660,000.00 USD | **`ACCUMULATION`** |
| `12h` | 14,950,000.00 USD | 80,390,000.00 USD | **`ACCUMULATION`** |
| `24h` | 1,510,000.00 USD | 34,970,000.00 USD | **`ACCUMULATION`** |
| `1w` | 37,710,000.00 USD | 229,440,000.00 USD | **`ACCUMULATION`** |
| `30d` | 58,380,000.00 USD | -531,630,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-3.02M` | 15m=`-9.42M` | 1h=`-12.55M` | 24h=`+1.51M`
* Futures Capital Netflows: 5m=`-13.85M` | 15m=`-22.75M` | 1h=`-31.76M` | 24h=`+34.97M`
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
  * `2026-10-30 02:14:39 IST`: [morningstar.com] - (Sentiment: `Neutral`)
  * `2026-10-30 01:35:39 IST`: [sec.gov] - (Sentiment: `Neutral`)
  * `2026-10-30 02:21:39 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 02:21:39 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 02:20:39 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 02:20:39 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 02:20:39 IST`: [@DeItaone] - (Sentiment: `Neutral`)
  * `2026-10-29 23:22:39 IST`: [@mb_ghalibaf] - (Sentiment: `Neutral`)
  * `2026-10-29 23:22:39 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-29 23:22:39 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-29 23:22:39 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:22:39 IST`: [fxstreet.com] - (Sentiment: `Neutral`)
  * `2026-10-29 21:22:39 IST`: [ForexFactory] - (Sentiment: `Neutral`)
  * `2026-10-29 21:22:39 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-29 21:22:39 IST`: [youtube.com/bankofcanadaofficial] - (Sentiment: `Neutral`)


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
  * Spread-Padded Stop Loss: `1223.97` (Risk Distance: `6.58` pts)
  * +2.5R Take Profit: `1247.00`
  * Mathematical Lot Sizing: **`1.51 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `1309.36` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `1315.94` (Risk Distance: `6.58` pts)
  * +2.5R Take Profit: `1292.91`
  * Mathematical Lot Sizing: **`1.51 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`1258.79`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
