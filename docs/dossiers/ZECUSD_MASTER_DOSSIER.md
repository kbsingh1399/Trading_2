# 🏛️ SOVEREIGN CANDIDATE DOSSIER: ZECUSD
**Canonical Key**: `ZECUSD` | **Broker Instrument**: `ZECUSD.p` | **Asset Class**: `Crypto Altcoin`
**Timestamp**: `2026-10-30 15:18:05 IST` (`2026-10-30 09:48:05 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `1248.71` | **Live Ask Quote**: `1249.79` | **Mid Price**: `1249.25`
- **Spread Points**: `108.00` | **Spread BPS**: `8.65 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `1253.69` | VWAP Z-Score: `-0.36` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `11.99` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `41.57` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `1317.89` | Lower -3.00σ Band: `1189.49`
  * Upper +2.51σ Band: `1307.41` | Lower -2.51σ Band: `1199.98`
  * Upper +2.01σ Band: `1296.71` | Lower -2.01σ Band: `1210.68`
  * Upper +2.00σ Band: `1296.49` | Lower -2.00σ Band: `1210.89`
  * Upper +1.28σ Band: `1281.09` | Lower -1.28σ Band: `1226.30`
  * Upper +1.00σ Band: `1275.09` | Lower -1.00σ Band: `1232.29`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`1250.28` | EMA-20=`1256.21` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`1262.58` (Slope: `+0.0000`) | EMA-100=`1268.63`
  * Institutional Anchors: EMA-144=`1271.75` | EMA-200=`1275.91` (Slope: `-0.2231`) | EMA-233=`1276.51`
- **Range Boundaries**: 24H High=`1396.49` | 24H Low=`1180.03` | Weekly High=`1396.49` | Weekly Low=`1180.03`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `1280.15` (Distance: `-2.45%`)
  * Point of Control (POC) = `1247.68` (Distance: `+0.09%`)
  * Value Area Low (VAL) = `1237.63` (Distance: `+0.90%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`1309.91` | POC=`1246.71` | VAL=`1230.27`
  * Prior Day Extremes: PDH=`1396.49` | PDL=`1206.89` | PDC=`1244.38`
  * Monday Range Blueprint: High=`1267.53` | Mid=`1222.14` | Low=`1176.75`
  * Developing Weekly Value Area: Weekly VAH=`1294.68` | Weekly POC=`1240.47` | Weekly VAL=`1200.92`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`1296.00` | Low=`1180.03`
  * London Session (08:00-16:00 UTC): High=`1283.82` | Low=`1239.95`
  * New York Session (13:00-21:00 UTC): High=`1256.75` | Low=`1241.75`
  * Initial Balance (First Hour): IB High=`1283.82` | IB Low=`1264.92`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `1244.25` - `1254.25`
  * Optimal Trade Entry (OTE 0.705): `1251.75`
  * Structural Invalidation Anchor (0.786): `1259.24`

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
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 15:10:55 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `12` | `0xb83d...6e36` | `SHORT` | 65,361,350.92 USD | `52,385.47` | `1336.45` | `1248.50` | `3375.83` | 4,649,216.48 USD | `+7.11%` | `3X Cross` |
| `21` | `0x5b5d...c060` | `SHORT` | 50,035,373.00 USD | `40,121.38` | `1478.36` | `1248.50` | `4838.05` | 9,278,662.11 USD | `+18.54%` | `3X Cross` |
| `36` | `0x7fda...17d1` | `SHORT` | 33,185,763.14 USD | `26,597.55` | `1262.59` | `1248.50` | `2621.18` | 396,119.54 USD | `+1.19%` | `5X Cross` |
| `83` | `0x60b0...991e` | `LONG` | 20,941,115.52 USD | `16,779.74` | `1179.65` | `1248.50` | `918.44` | 1,146,868.51 USD | `+5.48%` | `10X Cross` |
| `140` | `0xc36a...105b` | `LONG` | 14,358,596.87 USD | `11,510.82` | `1215.14` | `1248.50` | `967.81` | 371,315.84 USD | `+2.59%` | `10X Cross` |
| `178` | `0x8742...8427` | `LONG` | 11,492,311.29 USD | `9,201.21` | `1286.37` | `1248.50` | `712.56` | -343,858.70 USD | `-2.99%` | `10X Cross` |
| `192` | `0x58b2...11f3` | `LONG` | 10,685,729.67 USD | `8,563.08` | `1246.56` | `1248.50` | `383.89` | 11,312.09 USD | `+0.11%` | `10X Cross` |
| `193` | `0x9071...5c0b` | `LONG` | 10,650,871.14 USD | `8,517.29` | `1353.83` | `1248.50` | `0.000000` | -880,088.46 USD | `-8.26%` | `2X Cross` |
| `196` | `0x9ffd...ce40` | `LONG` | 10,630,345.11 USD | `8,519.27` | `1252.18` | `1248.50` | `606.67` | -37,283.44 USD | `-0.35%` | `5X Cross` |
| `200` | `0xad59...ba81` | `SHORT` | 10,516,085.00 USD | `8,425.00` | `330.91` | `1248.50` | `2147.50` | -7,728,127.23 USD | `-73.49%` | `10X Cross` |
| `204` | `0xdd53...2b13` | `SHORT` | 10,235,884.49 USD | `8,195.92` | `741.54` | `1248.50` | `8478.82` | -4,158,288.12 USD | `-40.62%` | `3X Cross` |
| `227` | `0x880a...311c` | `SHORT` | 9,613,849.01 USD | `7,707.11` | `1367.50` | `1248.50` | `2232.53` | 925,635.19 USD | `+9.63%` | `10X Cross` |
| `237` | `0xbf73...5d58` | `LONG` | 9,358,500.00 USD | `7,500.00` | `1248.78` | `1248.50` | `142.29` | -7,345.62 USD | `-0.08%` | `10X Cross` |
| `272` | `0x2b61...2f6c` | `LONG` | 8,491,051.80 USD | `6,807.00` | `1453.56` | `1248.50` | `557.30` | -1,403,299.42 USD | `-16.53%` | `10X Cross` |
| `289` | `0x2ae5...83e7` | `LONG` | 8,029,264.32 USD | `6,436.80` | `1391.82` | `1248.50` | `0.000000` | -929,627.67 USD | `-11.58%` | `1X Cross` |
| `325` | `0xecb6...2b00` | `SHORT` | 7,059,212.11 USD | `5,657.78` | `1278.09` | `1248.50` | `6528.11` | 171,964.12 USD | `+2.44%` | `5X Cross` |
| `335` | `0x26b6...9a13` | `LONG` | 6,798,139.60 USD | `5,433.73` | `1282.23` | `1248.50` | `227.66` | -169,163.63 USD | `-2.49%` | `10X Cross` |
| `353` | `0x45d2...4029` | `SHORT` | 6,536,363.50 USD | `5,227.00` | `833.44` | `1248.50` | `9104.53` | -2,179,985.53 USD | `-33.35%` | `5X Cross` |
| `369` | `0xea00...a918` | `LONG` | 6,241,500.00 USD | `5,000.00` | `739.16` | `1248.50` | `0.000000` | 2,545,684.89 USD | `+40.79%` | `5X Cross` |
| `379` | `0xdd7a...8830` | `LONG` | 6,066,019.66 USD | `4,860.19` | `897.48` | `1248.50` | `788.70` | 1,704,115.99 USD | `+28.09%` | `10X Cross` |
| `423` | `0x469e...58a5` | `SHORT` | 5,194,720.65 USD | `4,163.52` | `1242.31` | `1248.50` | `1952.57` | -22,335.99 USD | `-0.43%` | `10X Cross` |
| `436` | `0x4cae...7c34` | `LONG` | 4,992,431.60 USD | `4,002.27` | `1169.72` | `1248.50` | `985.22` | 310,882.25 USD | `+6.23%` | `10X Cross` |
| `443` | `0xd4c1...3d1d` | `SHORT` | 4,901,539.54 USD | `3,928.46` | `1291.68` | `1248.50` | `2365.69` | 172,771.85 USD | `+3.52%` | `10X Cross` |
| `449` | `0xa61c...66b9` | `LONG` | 4,853,390.40 USD | `3,888.00` | `1148.34` | `1248.50` | `0.000000` | 388,648.26 USD | `+8.01%` | `10X Cross` |
| `471` | `0x382b...3e39` | `LONG` | 4,672,437.12 USD | `3,743.94` | `1219.28` | `1248.50` | `0.000000` | 107,524.46 USD | `+2.30%` | `10X Cross` |
| `478` | `0x9aa5...58af` | `SHORT` | 4,641,785.40 USD | `3,720.31` | `1205.51` | `1248.50` | `3718.38` | -156,898.60 USD | `-3.38%` | `10X Cross` |
| `480` | `0x0153...8052` | `SHORT` | 4,626,793.00 USD | `3,698.18` | `1307.82` | `1248.50` | `2504.93` | 209,777.75 USD | `+4.53%` | `1X Isolated` |
| `510` | `0xb122...e4ba` | `LONG` | 4,366,090.56 USD | `3,498.47` | `1265.25` | `1248.50` | `1126.15` | -60,360.97 USD | `-1.38%` | `10X Cross` |
| `546` | `0xd21d...90f1` | `LONG` | 4,056,650.00 USD | `3,250.00` | `1253.64` | `1248.50` | `876.15` | -17,691.73 USD | `-0.44%` | `4X Isolated` |
| `549` | `0x456f...cdf1` | `LONG` | 4,038,400.30 USD | `3,235.12` | `1267.53` | `1248.50` | `518.47` | -62,212.26 USD | `-1.54%` | `10X Cross` |
| `569` | `0x1338...c48e` | `LONG` | 3,928,284.04 USD | `3,149.43` | `1018.52` | `1248.50` | `820.45` | 720,538.50 USD | `+18.34%` | `4X Isolated` |
| `585` | `0xdbe0...d6d5` | `LONG` | 3,860,106.41 USD | `3,085.37` | `422.97` | `1248.50` | `338.76` | 2,555,101.91 USD | `+66.19%` | `3X Isolated` |
| `603` | `0x325e...9564` | `LONG` | 3,746,035.95 USD | `3,000.91` | `1298.07` | `1248.50` | `137.96` | -149,369.21 USD | `-3.99%` | `10X Cross` |
| `609` | `0x2e30...4cb5` | `SHORT` | 3,734,489.18 USD | `2,991.66` | `1282.39` | `1248.50` | `2888.52` | 102,000.92 USD | `+2.73%` | `2X Cross` |
| `612` | `0x9c06...0560` | `SHORT` | 3,730,672.44 USD | `2,989.80` | `786.00` | `1248.50` | `2586.23` | -1,380,677.44 USD | `-37.01%` | `10X Cross` |
| `620` | `0x27c9...d65d` | `SHORT` | 3,667,555.33 USD | `2,938.04` | `1254.41` | `1248.50` | `1739.41` | 17,954.71 USD | `+0.49%` | `10X Cross` |
| `711` | `0xa183...0482` | `LONG` | 3,168,006.80 USD | `2,534.00` | `530.25` | `1248.50` | `444.69` | 1,824,344.08 USD | `+57.59%` | `5X Isolated` |
| `714` | `0xac48...3201` | `LONG` | 3,160,071.45 USD | `2,531.50` | `1378.58` | `1248.50` | `538.29` | -329,800.83 USD | `-10.44%` | `10X Cross` |
| `721` | `0x0871...e927` | `LONG` | 3,118,500.00 USD | `2,500.00` | `1276.50` | `1248.50` | `0.000000` | -72,750.00 USD | `-2.33%` | `10X Cross` |
| `747` | `0x9b86...6e6e` | `LONG` | 3,074,691.06 USD | `2,463.30` | `637.58` | `1248.50` | `882.62` | 1,504,141.78 USD | `+48.92%` | `3X Cross` |
| `821` | `0xf48f...10fe` | `LONG` | 2,769,119.22 USD | `2,218.49` | `1517.87` | `1248.50` | `976.22` | -598,267.61 USD | `-21.60%` | `3X Cross` |
| `849` | `0x5bc4...3b0c` | `SHORT` | 2,662,572.70 USD | `2,130.74` | `1089.65` | `1248.50` | `3681.43` | -340,815.13 USD | `-12.80%` | `5X Cross` |
| `864` | `0x8de4...b9aa` | `SHORT` | 2,609,687.12 USD | `2,091.29` | `1331.35` | `1248.50` | `1690.05` | 174,552.58 USD | `+6.69%` | `3X Cross` |
| `866` | `0x4fe2...ac59` | `SHORT` | 2,587,183.77 USD | `2,071.57` | `1478.56` | `1248.50` | `1849.48` | 475,762.44 USD | `+18.39%` | `10X Cross` |
| `871` | `0xdf57...93f5` | `LONG` | 2,562,596.19 USD | `2,054.35` | `1227.36` | `1248.50` | `897.39` | 41,174.15 USD | `+1.61%` | `4X Isolated` |
| `879` | `0xbcd4...0dd2` | `LONG` | 2,537,697.17 USD | `2,033.92` | `1228.20` | `1248.50` | `755.88` | 39,646.36 USD | `+1.56%` | `10X Cross` |
| `887` | `0x71d0...8c26` | `SHORT` | 2,505,684.48 USD | `2,007.76` | `1266.91` | `1248.50` | `3977.06` | 37,958.47 USD | `+1.51%` | `10X Cross` |
| `889` | `0xf29c...9971` | `LONG` | 2,500,400.00 USD | `2,000.00` | `1254.95` | `1248.50` | `0.000000` | -9,497.07 USD | `-0.38%` | `10X Cross` |
| `891` | `0x9a99...d21a` | `LONG` | 2,495,767.80 USD | `2,000.00` | `1278.44` | `1248.50` | `0.000000` | -61,105.87 USD | `-2.45%` | `10X Cross` |
| `916` | `0x77ee...2902` | `SHORT` | 2,427,477.82 USD | `1,946.03` | `759.84` | `1248.50` | `5691.55` | -948,800.32 USD | `-39.09%` | `10X Cross` |
| `920` | `0x3e2f...b269` | `SHORT` | 2,406,694.95 USD | `1,925.51` | `1134.87` | `1248.50` | `2977.33` | -221,496.09 USD | `-9.20%` | `10X Cross` |
| `936` | `0x4f12...618b` | `SHORT` | 2,366,337.28 USD | `1,896.28` | `1608.30` | `1248.50` | `2116.94` | 683,447.11 USD | `+28.88%` | `3X Cross` |
| `978` | `0x866d...d6e1` | `LONG` | 2,247,877.17 USD | `1,802.05` | `674.73` | `1248.50` | `152.12` | 1,031,975.86 USD | `+45.91%` | `10X Cross` |
| `1006` | `0x2309...a2d9` | `LONG` | 2,183,893.24 USD | `1,750.37` | `1186.09` | `1248.50` | `808.46` | 107,799.13 USD | `+4.94%` | `8X Cross` |
| `1051` | `0x265e...7f70` | `LONG` | 2,061,179.75 USD | `1,651.74` | `1382.98` | `1248.50` | `0.000000` | -223,143.01 USD | `-10.83%` | `3X Cross` |
| `1055` | `0xfe7c...b7ae` | `SHORT` | 2,050,014.72 USD | `1,642.64` | `1346.92` | `1248.50` | `5738.11` | 162,493.90 USD | `+7.93%` | `10X Cross` |
| `1060` | `0x3e47...aaf6` | `LONG` | 2,042,404.70 USD | `1,636.28` | `1278.38` | `1248.50` | `1051.68` | -49,387.09 USD | `-2.42%` | `10X Cross` |
| `1061` | `0x2edd...8179` | `SHORT` | 2,042,193.83 USD | `1,635.98` | `1261.55` | `1248.50` | `2884.08` | 21,669.05 USD | `+1.06%` | `10X Cross` |
| `1083` | `0x7f75...9edf` | `LONG` | 2,011,665.73 USD | `1,612.17` | `1200.26` | `1248.50` | `987.05` | 76,644.65 USD | `+3.81%` | `10X Cross` |
| `1091` | `0x6646...6de5` | `SHORT` | 1,999,680.00 USD | `1,600.00` | `660.64` | `1248.50` | `4221.62` | -942,655.03 USD | `-47.14%` | `10X Cross` |
| `1094` | `0x023a...2355` | `SHORT` | 1,986,432.27 USD | `1,591.31` | `1310.00` | `1248.50` | `4430.46` | 98,176.98 USD | `+4.94%` | `10X Cross` |
| `1107` | `0xfc27...9d9d` | `SHORT` | 1,969,400.33 USD | `1,578.44` | `1295.79` | `1248.50` | `12979.50` | 75,923.88 USD | `+3.86%` | `10X Cross` |
| `1117` | `0xab59...59b5` | `LONG` | 1,954,458.55 USD | `1,565.32` | `1342.15` | `1248.50` | `836.80` | -146,436.67 USD | `-7.49%` | `10X Cross` |
| `1164` | `0x039c...0ebd` | `SHORT` | 1,898,238.30 USD | `1,521.39` | `1245.17` | `1248.50` | `3735.01` | -3,844.44 USD | `-0.20%` | `10X Cross` |
| `1174` | `0xcf67...eb24` | `LONG` | 1,871,825.85 USD | `1,500.00` | `887.05` | `1248.50` | `625.02` | 541,254.48 USD | `+28.92%` | `10X Cross` |
| `1191` | `0x7277...0b98` | `SHORT` | 1,840,382.88 USD | `1,475.73` | `1287.86` | `1248.50` | `2193.83` | 60,149.24 USD | `+3.27%` | `10X Cross` |
| `1255` | `0x2ab7...c2f8` | `LONG` | 1,749,236.99 USD | `1,400.51` | `813.26` | `1248.50` | `792.86` | 610,255.30 USD | `+34.89%` | `3X Cross` |
| `1271` | `0x11be...8b1d` | `LONG` | 1,717,448.59 USD | `1,375.83` | `1206.55` | `1248.50` | `1134.67` | 57,440.63 USD | `+3.34%` | `10X Isolated` |
| `1345` | `0x3205...40bb` | `SHORT` | 1,592,382.68 USD | `1,274.11` | `1257.43` | `1248.50` | `2419.91` | 9,719.40 USD | `+0.61%` | `10X Cross` |
| `1356` | `0xe065...0f85` | `SHORT` | 1,575,590.69 USD | `1,262.61` | `1087.02` | `1248.50` | `1551.20` | -203,114.56 USD | `-12.89%` | `10X Cross` |
| `1369` | `0x413c...886c` | `LONG` | 1,560,750.00 USD | `1,250.00` | `1237.51` | `1248.50` | `0.000000` | 13,860.54 USD | `+0.89%` | `10X Cross` |
| `1376` | `0xdf83...3cff` | `SHORT` | 1,557,504.00 USD | `1,248.00` | `1260.55` | `1248.50` | `1848.22` | 15,666.30 USD | `+1.01%` | `10X Cross` |
| `1436` | `0x2847...d47b` | `LONG` | 1,511,835.78 USD | `1,211.71` | `1232.45` | `1248.50` | `0.000000` | 18,468.19 USD | `+1.22%` | `5X Cross` |
| `1445` | `0x266b...efcb` | `LONG` | 1,501,320.00 USD | `1,200.00` | `893.76` | `1248.50` | `414.09` | 428,810.30 USD | `+28.56%` | `10X Cross` |
| `1449` | `0x5975...9abd` | `LONG` | 1,497,960.00 USD | `1,200.00` | `1179.54` | `1248.50` | `553.39` | 82,517.21 USD | `+5.51%` | `5X Cross` |
| `1478` | `0x69cc...14fd` | `SHORT` | 1,449,201.80 USD | `1,161.36` | `675.33` | `1248.50` | `8115.92` | -664,896.27 USD | `-45.88%` | `10X Cross` |
| `1491` | `0x3fc5...c0c1` | `SHORT` | 1,433,942.18 USD | `1,148.44` | `1264.34` | `1248.50` | `2778.95` | 18,071.59 USD | `+1.26%` | `10X Cross` |
| `1536` | `0x5f94...4b96` | `LONG` | 1,392,080.01 USD | `1,115.27` | `538.00` | `1248.50` | `0.000000` | 792,062.38 USD | `+56.90%` | `10X Cross` |
| `1542` | `0xe35c...a1d3` | `LONG` | 1,387,310.69 USD | `1,111.36` | `1311.66` | `1248.50` | `690.96` | -70,413.46 USD | `-5.08%` | `2X Isolated` |
| `1572` | `0x71df...a23d` | `SHORT` | 1,369,994.47 USD | `1,098.28` | `513.50` | `1248.50` | `2560.43` | -806,024.28 USD | `-58.83%` | `2X Cross` |
| `1585` | `0xbfc7...80b4` | `SHORT` | 1,341,250.84 USD | `1,075.00` | `558.03` | `1248.50` | `2711.64` | -741,372.11 USD | `-55.27%` | `10X Cross` |
| `1625` | `0x123d...3bff` | `SHORT` | 1,303,649.62 USD | `1,044.34` | `519.62` | `1248.50` | `4148.54` | -760,991.41 USD | `-58.37%` | `10X Cross` |
| `1685` | `0x668c...ea2e` | `SHORT` | 1,249,200.00 USD | `1,000.00` | `1406.98` | `1248.50` | `4211.47` | 157,781.99 USD | `+12.63%` | `10X Cross` |
| `1687` | `0xe282...df29` | `LONG` | 1,248,300.00 USD | `1,000.00` | `420.99` | `1248.50` | `810.14` | 827,313.14 USD | `+66.28%` | `10X Cross` |
| `1708` | `0x5323...b23c` | `SHORT` | 1,232,365.77 USD | `987.71` | `1254.57` | `1248.50` | `6873.32` | 6,783.17 USD | `+0.55%` | `5X Cross` |
| `1712` | `0x17f0...094f` | `LONG` | 1,227,815.82 USD | `984.30` | `1287.23` | `1248.50` | `537.02` | -39,204.34 USD | `-3.19%` | `5X Cross` |
| `1725` | `0x51f6...2b39` | `SHORT` | 1,215,039.69 USD | `972.81` | `1299.77` | `1248.50` | `2519.76` | 49,388.02 USD | `+4.06%` | `10X Cross` |
| `1789` | `0x757d...94ba` | `LONG` | 1,155,880.00 USD | `925.00` | `1558.31` | `1248.50` | `0.000000` | -285,560.59 USD | `-24.71%` | `10X Cross` |
| `1833` | `0xb911...5525` | `LONG` | 1,123,740.00 USD | `900.00` | `1294.82` | `1248.50` | `1035.45` | -41,597.82 USD | `-3.70%` | `10X Cross` |
| `1853` | `0xef96...9383` | `SHORT` | 1,107,659.80 USD | `887.77` | `1259.32` | `1248.50` | `5154.34` | 10,327.08 USD | `+0.93%` | `10X Cross` |
| `1879` | `0xcf0a...856f` | `LONG` | 1,086,411.17 USD | `871.15` | `1292.19` | `1248.50` | `1027.91` | -39,283.68 USD | `-3.62%` | `4X Cross` |
| `1896` | `0xdf95...7d72` | `SHORT` | 1,064,624.98 USD | `853.27` | `1074.39` | `1248.50` | `45204.25` | -147,877.54 USD | `-13.89%` | `10X Cross` |
| `1929` | `0xb2f7...af9f` | `SHORT` | 1,036,904.70 USD | `830.72` | `746.63` | `1248.50` | `8174.69` | -416,665.67 USD | `-40.18%` | `10X Cross` |
| `1946` | `0x601c...4f54` | `SHORT` | 1,028,299.07 USD | `824.42` | `615.11` | `1248.50` | `3140.20` | -521,186.31 USD | `-50.68%` | `5X Cross` |
| `1959` | `0xae55...2236` | `LONG` | 1,022,246.23 USD | `817.47` | `1467.80` | `1248.50` | `0.000000` | -177,634.98 USD | `-17.38%` | `10X Cross` |
| `1998` | `0x9b0f...db40` | `LONG` | 1,000,880.00 USD | `800.00` | `1268.86` | `1248.50` | `799.19` | -14,209.76 USD | `-1.42%` | `10X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
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
  * 24H Horizon: Short MP=`1404.55` (Vol: 3,000,000.00 USD, Dist: `+12.62%`) | Long MP=`1176.48` (Vol: 3,400,000.00 USD, Dist: `--5.67%`)
  * 48H Horizon: Short MP=`1404.55` (Vol: 3,000,000.00 USD, Dist: `+12.62%`) | Long MP=`1176.48` (Vol: 3,400,000.00 USD, Dist: `--5.67%`)
  * 3D Horizon: Short MP=`1404.55` (Vol: 3,000,000.00 USD, Dist: `+12.62%`) | Long MP=`1176.48` (Vol: 3,400,000.00 USD, Dist: `--5.67%`)
  * 7D Horizon: Short MP=`1404.10` (Vol: 3,000,000.00 USD, Dist: `+12.58%`) | Long MP=`1176.74` (Vol: 4,900,000.00 USD, Dist: `--5.65%`)
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
| `5m` | `BALANCED` | 0.00 USD | 1,750.00 USD | 1,750.00 USD | 1,750.00 USD | `1` | `2026-10-30 09:40:00 UTC - 2026-10-30 09:45:00 UTC` |
| `15m` | `BALANCED` | 0.00 USD | 1,750.00 USD | 1,750.00 USD | 1,750.00 USD | `1` | `2026-10-30 09:30:00 UTC - 2026-10-30 09:45:00 UTC` |
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
  * Current Rate: `84.13K` | Last 24h: `171.90K` | Last 3d: `285.15K` | Last 7d: `847.79K`
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
| `0:00 UTC` | `1255.05` | `1256.16` | `1255.05` | `1269.15` | `1247.25` | 26,236,011.28 USD | 8,922,234.21 USD | 17,313,777.08 USD | -8,391,542.87 USD | `-31.98%` | `2B / 24S` |
| `5:00 UTC` | `1248.15` | `1248.05` | `1248.15` | `1253.25` | `1244.25` | 21,008,122.73 USD | 11,395,427.09 USD | 9,612,695.64 USD | 1,782,731.45 USD | `+8.49%` | `1B / 0S` |
| `0:00 UTC` | `1245.75` | `1245.57` | `1245.75` | `1250.55` | `1240.05` | 17,224,192.69 USD | 9,235,789.14 USD | 7,988,403.55 USD | 1,247,385.58 USD | `+7.24%` | `1B / 6S` |
| `5:00 UTC` | `1251.45` | `1250.99` | `1251.45` | `1255.05` | `1246.35` | 13,619,576.55 USD | 6,741,413.50 USD | 6,878,163.05 USD | -136,749.55 USD | `-1.00%` | `2B / 0S` |
| `0:00 UTC` | `1249.95` | `1249.10` | `1249.95` | `1253.55` | `1244.55` | 10,263,783.49 USD | 5,117,369.60 USD | 5,146,413.89 USD | -29,044.29 USD | `-0.28%` | `1B / 4S` |
| `5:00 UTC` | `1246.65` | `1246.77` | `1246.65` | `1252.35` | `1243.95` | 13,017,000.97 USD | 7,727,648.32 USD | 5,289,352.64 USD | 2,438,295.68 USD | `+18.73%` | `8B / 5S` |
| `0:00 UTC` | `1244.55` | `1245.81` | `1244.55` | `1249.05` | `1243.65` | 9,717,386.64 USD | 3,914,194.68 USD | 5,803,191.96 USD | -1,888,997.28 USD | `-19.44%` | `0B / 1S` |
| `5:00 UTC` | `1242.15` | `1244.40` | `1242.15` | `1249.35` | `1241.25` | 8,638,502.97 USD | 4,533,952.89 USD | 4,104,550.08 USD | 429,402.82 USD | `+4.97%` | `4B / 2S` |
| `0:00 UTC` | `1251.15` | `1247.35` | `1251.15` | `1251.75` | `1240.05` | 9,977,652.60 USD | 4,992,881.35 USD | 4,984,771.25 USD | 8,110.10 USD | `+0.08%` | `3B / 5S` |
| `5:00 UTC` | `1243.95` | `1245.06` | `1243.95` | `1248.15` | `1243.35` | 3,263,672.05 USD | 880,315.48 USD | 2,383,356.57 USD | -1,503,041.09 USD | `-46.05%` | `2B / 5S` |

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
| `5m` | -147,980.00 USD | 574,330.00 USD | **`ACCUMULATION`** |
| `15m` | -708,230.00 USD | 1,700,000.00 USD | **`ACCUMULATION`** |
| `30m` | -1,750,000.00 USD | 473,720.00 USD | **`DISTRIBUTION`** |
| `1h` | -2,730,000.00 USD | 4,210,000.00 USD | **`ACCUMULATION`** |
| `2h` | 202,640.00 USD | -4,690,000.00 USD | **`DISTRIBUTION`** |
| `4h` | 1,430,000.00 USD | -22,190,000.00 USD | **`DISTRIBUTION`** |
| `6h` | -1,910,000.00 USD | -41,350,000.00 USD | **`DISTRIBUTION`** |
| `8h` | 7,560,000.00 USD | 4,290,000.00 USD | **`ACCUMULATION`** |
| `12h` | 626,250.00 USD | -31,420,000.00 USD | **`DISTRIBUTION`** |
| `24h` | 19,380,000.00 USD | 73,890,000.00 USD | **`ACCUMULATION`** |
| `1w` | 34,900,000.00 USD | 203,700,000.00 USD | **`ACCUMULATION`** |
| `30d` | 62,180,000.00 USD | -541,890,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-147.98K` | 15m=`-708.23K` | 1h=`-2.73M` | 24h=`+19.38M`
* Futures Capital Netflows: 5m=`+574.33K` | 15m=`+1.70M` | 1h=`+4.21M` | 24h=`+73.89M`
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
  * `2026-10-30 15:12:05 IST`: [breakingthenews.net] - (Sentiment: `Neutral`)
  * `2026-10-30 14:41:05 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 14:38:05 IST`: [@FirstSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 14:34:05 IST`: [destatis.de] - (Sentiment: `Neutral`)
  * `2026-10-30 14:33:05 IST`: [istat.it] - (Sentiment: `Neutral`)
  * `2026-10-30 15:16:05 IST`: [channelnewsasia.com] - (Sentiment: `Neutral`)
  * `2026-10-30 15:16:05 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 15:16:05 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 15:16:05 IST`: [kof.ethz.ch] - (Sentiment: `Neutral`)
  * `2026-10-30 15:16:05 IST`: [gerlachmacro.substack.com] - (Sentiment: `Neutral`)
  * `2026-10-30 15:16:05 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-30 15:16:05 IST`: [insee.fr] - (Sentiment: `Neutral`)
  * `2026-10-30 15:16:05 IST`: [insee.fr] - (Sentiment: `Neutral`)
  * `2026-10-30 15:15:05 IST`: [@FirstSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 15:15:05 IST`: [nationwide.co.uk] - (Sentiment: `Neutral`)


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
  * Spread-Padded Stop Loss: `1221.62` (Risk Distance: `16.01` pts)
  * +2.5R Take Profit: `1277.66`
  * Mathematical Lot Sizing: **`0.62 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `1280.15` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `1296.16` (Risk Distance: `16.01` pts)
  * +2.5R Take Profit: `1240.12`
  * Mathematical Lot Sizing: **`0.62 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`1259.24`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
