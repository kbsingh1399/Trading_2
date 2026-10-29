# 🏛️ SOVEREIGN CANDIDATE DOSSIER: ZECUSD
**Canonical Key**: `ZECUSD` | **Broker Instrument**: `ZECUSD.p` | **Asset Class**: `Crypto Altcoin`
**Timestamp**: `2026-10-30 00:41:24 IST` (`2026-10-29 19:11:24 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `1320.72` | **Live Ask Quote**: `1321.78` | **Mid Price**: `1321.25`
- **Spread Points**: `106.00` | **Spread BPS**: `8.02 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `1279.89` | VWAP Z-Score: `+1.12` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `16.48` (Volatility Regime: `HIGH_EXPANSION`)
  * 14-Period RSI: `53.31` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `1396.35` | Lower -3.00σ Band: `1163.43`
  * Upper +2.51σ Band: `1377.32` | Lower -2.51σ Band: `1182.45`
  * Upper +2.01σ Band: `1357.92` | Lower -2.01σ Band: `1201.86`
  * Upper +2.00σ Band: `1357.53` | Lower -2.00σ Band: `1202.25`
  * Upper +1.28σ Band: `1329.58` | Lower -1.28σ Band: `1230.20`
  * Upper +1.00σ Band: `1318.71` | Lower -1.00σ Band: `1241.07`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`1329.09` | EMA-20=`1322.96` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`1300.56` (Slope: `+0.0000`) | EMA-100=`1289.27`
  * Institutional Anchors: EMA-144=`1284.45` | EMA-200=`1279.53` (Slope: `+0.6009`) | EMA-233=`1276.98`
- **Range Boundaries**: 24H High=`1396.49` | 24H Low=`1230.00` | Weekly High=`1396.49` | Weekly Low=`1210.62`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `1307.14` (Distance: `+1.09%`)
  * Point of Control (POC) = `1247.20` (Distance: `+5.95%`)
  * Value Area Low (VAL) = `1230.55` (Distance: `+7.38%`)
  * Auction Positioning: `ABOVE_VALUE (Imbalance)` | Session Bias: **`BULLISH (Above Pivot)`** | Market Regime: `RANGE_EXPANSION`
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
  * Golden Pocket Zone (0.618 - 0.650): `1315.96` - `1326.54`
  * Optimal Trade Entry (OTE 0.705): `1323.89`
  * Structural Invalidation Anchor (0.786): `1331.82`

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
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 00:34:35 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `16` | `0xb83d...6e36` | `SHORT` | 69,535,124.45 USD | `52,582.52` | `1336.45` | `1321.00` | `3712.32` | 738,790.45 USD | `+1.06%` | `3X Cross` |
| `24` | `0x5b5d...c060` | `SHORT` | 53,870,409.75 USD | `40,727.61` | `1478.36` | `1321.00` | `5002.08` | 6,339,854.45 USD | `+11.77%` | `3X Cross` |
| `41` | `0x7fda...17d1` | `SHORT` | 29,656,342.64 USD | `22,419.37` | `1261.41` | `1321.00` | `2810.45` | -1,376,357.06 USD | `-4.64%` | `5X Cross` |
| `77` | `0x60b0...991e` | `LONG` | 22,194,562.10 USD | `16,779.74` | `1179.65` | `1321.00` | `890.05` | 2,400,315.08 USD | `+10.81%` | `10X Cross` |
| `82` | `0xbf73...5d58` | `LONG` | 21,163,200.00 USD | `16,000.00` | `1214.30` | `1321.00` | `719.67` | 1,734,367.75 USD | `+8.20%` | `10X Cross` |
| `132` | `0xc36a...105b` | `LONG` | 15,225,361.61 USD | `11,510.82` | `1215.14` | `1321.00` | `932.77` | 1,238,080.59 USD | `+8.13%` | `10X Cross` |
| `169` | `0x8742...8427` | `LONG` | 12,152,575.40 USD | `9,201.21` | `1286.37` | `1321.00` | `698.35` | 316,405.40 USD | `+2.60%` | `10X Cross` |
| `178` | `0x9071...5c0b` | `LONG` | 11,662,217.43 USD | `8,829.94` | `1370.53` | `1321.00` | `579.50` | -439,471.22 USD | `-3.77%` | `2X Cross` |
| `192` | `0xad59...ba81` | `SHORT` | 11,141,220.00 USD | `8,425.00` | `330.91` | `1321.00` | `2140.12` | -8,353,262.23 USD | `-74.98%` | `10X Cross` |
| `199` | `0xdd53...2b13` | `SHORT` | 10,872,512.83 USD | `8,231.14` | `739.37` | `1321.00` | `7874.68` | -4,786,631.35 USD | `-44.03%` | `3X Cross` |
| `200` | `0x9ffd...ce40` | `LONG` | 10,853,997.30 USD | `8,205.32` | `1253.68` | `1321.00` | `570.40` | 567,121.13 USD | `+5.22%` | `5X Cross` |
| `215` | `0xfc66...ca06` | `SHORT` | 10,267,542.19 USD | `7,763.15` | `1319.72` | `1321.00` | `5598.05` | -22,329.51 USD | `-0.22%` | `10X Cross` |
| `219` | `0x880a...311c` | `SHORT` | 10,194,194.40 USD | `7,707.11` | `1367.50` | `1321.00` | `2308.56` | 345,289.81 USD | `+3.39%` | `10X Cross` |
| `268` | `0x2b61...2f6c` | `LONG` | 9,003,618.90 USD | `6,807.00` | `1453.56` | `1321.00` | `637.05` | -890,732.32 USD | `-9.89%` | `10X Cross` |
| `285` | `0x2ae5...83e7` | `LONG` | 8,501,457.67 USD | `6,436.80` | `1391.82` | `1321.00` | `233.36` | -457,434.32 USD | `-5.38%` | `2X Cross` |
| `330` | `0xecb6...2b00` | `SHORT` | 7,216,376.66 USD | `5,455.38` | `1324.05` | `1321.00` | `6099.60` | 6,833.47 USD | `+0.09%` | `5X Cross` |
| `331` | `0x26b6...9a13` | `LONG` | 7,176,870.58 USD | `5,433.73` | `1282.23` | `1321.00` | `208.41` | 209,567.35 USD | `+2.92%` | `10X Cross` |
| `343` | `0x45d2...4029` | `SHORT` | 6,903,604.16 USD | `5,227.00` | `833.44` | `1321.00` | `8046.25` | -2,547,226.18 USD | `-36.90%` | `5X Cross` |
| `361` | `0xea00...a918` | `LONG` | 6,613,500.00 USD | `5,000.00` | `739.16` | `1321.00` | `0.000000` | 2,917,684.89 USD | `+44.12%` | `5X Cross` |
| `377` | `0xdd7a...8830` | `LONG` | 6,426,143.22 USD | `4,860.19` | `897.48` | `1321.00` | `783.88` | 2,064,239.54 USD | `+32.12%` | `10X Cross` |
| `385` | `0xf081...e39e` | `LONG` | 6,239,175.90 USD | `4,717.00` | `1195.70` | `1321.00` | `1200.09` | 599,051.85 USD | `+9.60%` | `10X Cross` |
| `437` | `0x4cae...7c34` | `LONG` | 5,296,566.97 USD | `4,004.36` | `999.34` | `1321.00` | `750.54` | 1,294,838.82 USD | `+24.45%` | `10X Cross` |
| `449` | `0xa61c...66b9` | `LONG` | 5,140,713.60 USD | `3,888.00` | `1148.34` | `1321.00` | `0.000000` | 675,971.46 USD | `+13.15%` | `10X Cross` |
| `452` | `0x382b...3e39` | `LONG` | 5,104,497.71 USD | `3,859.15` | `1195.35` | `1321.00` | `0.000000` | 491,476.73 USD | `+9.63%` | `10X Cross` |
| `471` | `0x9aa5...58af` | `SHORT` | 4,921,226.07 USD | `3,720.31` | `1205.51` | `1321.00` | `3334.29` | -436,339.27 USD | `-8.87%` | `10X Cross` |
| `477` | `0x0153...8052` | `SHORT` | 4,888,809.05 USD | `3,698.18` | `1307.82` | `1321.00` | `2504.69` | -52,238.30 USD | `-1.07%` | `1X Isolated` |
| `503` | `0xd4c1...3d1d` | `SHORT` | 4,570,865.92 USD | `3,455.97` | `1302.96` | `1321.00` | `2680.70` | -67,859.50 USD | `-1.48%` | `10X Cross` |
| `528` | `0xd21d...90f1` | `LONG` | 4,298,450.00 USD | `3,250.00` | `1253.64` | `1321.00` | `875.88` | 224,108.27 USD | `+5.21%` | `4X Isolated` |
| `549` | `0x1338...c48e` | `LONG` | 4,159,514.24 USD | `3,149.43` | `1018.52` | `1321.00` | `820.17` | 951,768.70 USD | `+22.88%` | `4X Isolated` |
| `552` | `0x456f...cdf1` | `LONG` | 4,145,173.89 USD | `3,134.11` | `1268.52` | `1321.00` | `493.32` | 169,484.25 USD | `+4.09%` | `10X Cross` |
| `562` | `0xdbe0...d6d5` | `LONG` | 4,078,704.87 USD | `3,085.37` | `422.97` | `1321.00` | `338.49` | 2,773,700.38 USD | `+68.00%` | `3X Isolated` |
| `586` | `0x9c06...0560` | `SHORT` | 3,954,309.48 USD | `2,989.80` | `786.00` | `1321.00` | `2374.07` | -1,604,314.48 USD | `-40.57%` | `10X Cross` |
| `587` | `0x27c9...d65d` | `SHORT` | 3,952,478.91 USD | `2,988.19` | `1250.13` | `1321.00` | `1829.01` | -216,866.81 USD | `-5.49%` | `10X Cross` |
| `687` | `0xac48...3201` | `LONG` | 3,360,054.81 USD | `2,540.30` | `1393.86` | `1321.00` | `529.48` | -180,774.48 USD | `-5.38%` | `10X Cross` |
| `692` | `0xa183...0482` | `LONG` | 3,346,801.79 USD | `2,534.00` | `530.25` | `1321.00` | `444.42` | 2,003,139.06 USD | `+59.85%` | `5X Isolated` |
| `698` | `0x2e30...4cb5` | `SHORT` | 3,311,942.02 USD | `2,505.94` | `1299.10` | `1321.00` | `3130.56` | -56,476.28 USD | `-1.71%` | `2X Cross` |
| `699` | `0x325e...9564` | `LONG` | 3,308,025.40 USD | `2,501.91` | `1306.24` | `1321.00` | `0.000000` | 39,931.50 USD | `+1.21%` | `10X Cross` |
| `700` | `0x0871...e927` | `LONG` | 3,306,750.00 USD | `2,500.00` | `1276.50` | `1321.00` | `0.000000` | 115,500.00 USD | `+3.49%` | `10X Cross` |
| `708` | `0x9b86...6e6e` | `LONG` | 3,263,250.98 USD | `2,467.30` | `637.58` | `1321.00` | `889.64` | 1,690,151.38 USD | `+51.79%` | `3X Cross` |
| `773` | `0xb2f7...af9f` | `SHORT` | 3,059,663.33 USD | `2,313.72` | `746.63` | `1321.00` | `4180.21` | -1,332,174.58 USD | `-43.54%` | `10X Cross` |
| `788` | `0x634f...6951` | `LONG` | 3,005,502.69 USD | `2,272.42` | `1281.94` | `1321.00` | `1250.03` | 92,402.23 USD | `+3.07%` | `10X Cross` |
| `804` | `0xf48f...10fe` | `LONG` | 2,933,731.18 USD | `2,218.49` | `1517.87` | `1321.00` | `894.46` | -433,655.65 USD | `-14.78%` | `3X Cross` |
| `833` | `0x5bc4...3b0c` | `SHORT` | 2,814,494.47 USD | `2,130.74` | `1089.65` | `1321.00` | `3566.88` | -492,736.89 USD | `-17.51%` | `5X Cross` |
| `846` | `0x8de4...b9aa` | `SHORT` | 2,766,358.41 USD | `2,091.29` | `1331.35` | `1321.00` | `1689.81` | 17,881.29 USD | `+0.65%` | `3X Cross` |
| `850` | `0x4fe2...ac59` | `SHORT` | 2,740,065.64 USD | `2,071.57` | `1478.56` | `1321.00` | `1811.17` | 322,880.58 USD | `+11.78%` | `10X Cross` |
| `868` | `0x668c...ea2e` | `SHORT` | 2,645,200.00 USD | `2,000.00` | `1406.98` | `1321.00` | `2701.92` | 168,763.99 USD | `+6.38%` | `10X Cross` |
| `889` | `0x77ee...2902` | `SHORT` | 2,574,013.88 USD | `1,946.03` | `759.84` | `1321.00` | `5196.25` | -1,095,336.37 USD | `-42.55%` | `10X Cross` |
| `904` | `0x3e2f...b269` | `SHORT` | 2,543,406.16 USD | `1,925.51` | `1134.87` | `1321.00` | `2931.74` | -358,207.30 USD | `-14.08%` | `10X Cross` |
| `908` | `0xe097...d0fe` | `LONG` | 2,529,534.96 USD | `1,913.56` | `1261.17` | `1321.00` | `0.000000` | 116,208.80 USD | `+4.59%` | `10X Cross` |
| `914` | `0x4f12...618b` | `SHORT` | 2,508,209.56 USD | `1,896.28` | `1608.30` | `1321.00` | `2116.70` | 541,574.83 USD | `+21.59%` | `3X Cross` |
| `959` | `0x866d...d6e1` | `LONG` | 2,380,002.94 USD | `1,802.05` | `674.73` | `1321.00` | `90.99` | 1,164,101.62 USD | `+48.91%` | `10X Cross` |
| `993` | `0x2309...a2d9` | `LONG` | 2,315,039.36 USD | `1,750.37` | `1186.09` | `1321.00` | `805.25` | 238,945.25 USD | `+10.32%` | `8X Cross` |
| `1011` | `0x023a...2355` | `SHORT` | 2,248,926.34 USD | `1,700.64` | `1313.33` | `1321.00` | `6064.72` | -15,416.42 USD | `-0.69%` | `10X Cross` |
| `1013` | `0x2edd...8179` | `SHORT` | 2,242,243.46 USD | `1,695.33` | `1261.35` | `1321.00` | `2980.25` | -103,842.49 USD | `-4.63%` | `10X Cross` |
| `1042` | `0x3e47...aaf6` | `LONG` | 2,164,143.93 USD | `1,636.28` | `1279.54` | `1321.00` | `1036.70` | 70,451.84 USD | `+3.26%` | `10X Cross` |
| `1046` | `0xa271...a3f7` | `LONG` | 2,157,892.46 USD | `1,631.43` | `1190.60` | `1321.00` | `910.27` | 215,510.66 USD | `+9.99%` | `4X Cross` |
| `1058` | `0x7f75...9edf` | `LONG` | 2,123,804.63 USD | `1,605.78` | `1199.97` | `1321.00` | `973.77` | 196,912.74 USD | `+9.27%` | `10X Cross` |
| `1062` | `0x265e...7f70` | `LONG` | 2,118,781.67 USD | `1,601.74` | `1388.09` | `1321.00` | `0.000000` | -104,583.34 USD | `-4.94%` | `3X Cross` |
| `1064` | `0x6646...6de5` | `SHORT` | 2,115,040.00 USD | `1,600.00` | `660.64` | `1321.00` | `4804.03` | -1,058,015.03 USD | `-50.02%` | `10X Cross` |
| `1079` | `0xdf57...93f5` | `LONG` | 2,086,704.98 USD | `1,579.76` | `1218.38` | `1321.00` | `780.12` | 161,949.00 USD | `+7.76%` | `3X Isolated` |
| `1093` | `0xab59...59b5` | `LONG` | 2,070,292.23 USD | `1,565.32` | `1342.15` | `1321.00` | `792.17` | -30,602.99 USD | `-1.48%` | `10X Cross` |
| `1097` | `0xfe7c...b7ae` | `SHORT` | 2,066,705.52 USD | `1,562.49` | `1350.62` | `1321.00` | `6507.43` | 43,623.53 USD | `+2.11%` | `10X Cross` |
| `1150` | `0xcf67...eb24` | `LONG` | 1,984,050.00 USD | `1,500.00` | `887.05` | `1321.00` | `545.32` | 653,478.63 USD | `+32.94%` | `10X Cross` |
| `1174` | `0x039c...0ebd` | `SHORT` | 1,957,799.98 USD | `1,480.49` | `1238.67` | `1321.00` | `3153.33` | -123,968.66 USD | `-6.33%` | `10X Cross` |
| `1199` | `0x71d0...8c26` | `SHORT` | 1,911,036.96 USD | `1,444.80` | `1361.12` | `1321.00` | `6493.18` | 55,509.49 USD | `+2.90%` | `10X Cross` |
| `1247` | `0xfc27...9d9d` | `SHORT` | 1,854,225.93 USD | `1,403.91` | `1317.50` | `1321.00` | `11341.53` | -4,579.77 USD | `-0.25%` | `10X Cross` |
| `1251` | `0x2ab7...c2f8` | `LONG` | 1,851,614.27 USD | `1,400.51` | `813.26` | `1321.00` | `796.79` | 712,632.59 USD | `+38.49%` | `3X Cross` |
| `1263` | `0x11be...8b1d` | `LONG` | 1,819,672.76 USD | `1,375.83` | `1206.55` | `1321.00` | `1134.40` | 159,664.80 USD | `+8.77%` | `10X Isolated` |
| `1314` | `0xdf83...3cff` | `SHORT` | 1,736,218.63 USD | `1,312.93` | `1246.70` | `1321.00` | `1850.22` | -99,388.32 USD | `-5.72%` | `10X Cross` |
| `1319` | `0xef96...9383` | `SHORT` | 1,731,176.21 USD | `1,308.82` | `1249.96` | `1321.00` | `4207.76` | -95,209.79 USD | `-5.50%` | `10X Cross` |
| `1363` | `0xe065...0f85` | `SHORT` | 1,670,054.25 USD | `1,262.61` | `1087.02` | `1321.00` | `1756.45` | -297,578.12 USD | `-17.82%` | `10X Cross` |
| `1388` | `0x7277...0b98` | `SHORT` | 1,631,258.66 USD | `1,234.96` | `1298.48` | `1321.00` | `2359.16` | -27,689.25 USD | `-1.70%` | `10X Cross` |
| `1436` | `0x5975...9abd` | `LONG` | 1,587,120.00 USD | `1,200.00` | `1179.54` | `1321.00` | `317.01` | 171,677.21 USD | `+10.82%` | `5X Cross` |
| `1477` | `0x69cc...14fd` | `SHORT` | 1,534,156.56 USD | `1,161.36` | `675.33` | `1321.00` | `7867.32` | -749,851.03 USD | `-48.88%` | `10X Cross` |
| `1479` | `0x7a76...b16d` | `LONG` | 1,533,018.65 USD | `1,159.27` | `1358.50` | `1321.00` | `1236.56` | -41,849.86 USD | `-2.73%` | `10X Cross` |
| `1491` | `0x3fc5...c0c1` | `SHORT` | 1,518,926.74 USD | `1,148.44` | `1264.34` | `1321.00` | `3090.31` | -66,912.97 USD | `-4.41%` | `10X Cross` |
| `1511` | `0xe35c...a1d3` | `LONG` | 1,490,198.73 USD | `1,127.06` | `1318.20` | `1321.00` | `694.32` | 4,503.38 USD | `+0.30%` | `2X Isolated` |
| `1517` | `0x5f94...4b96` | `LONG` | 1,474,833.05 USD | `1,115.27` | `538.00` | `1321.00` | `0.000000` | 874,815.41 USD | `+59.32%` | `10X Cross` |
| `1538` | `0x71df...a23d` | `SHORT` | 1,452,694.96 USD | `1,098.28` | `513.50` | `1321.00` | `2546.86` | -888,724.77 USD | `-61.18%` | `2X Cross` |
| `1566` | `0xbfc7...80b4` | `SHORT` | 1,422,010.00 USD | `1,075.00` | `558.03` | `1321.00` | `5438.62` | -822,131.27 USD | `-57.81%` | `10X Cross` |
| `1611` | `0x51f6...2b39` | `SHORT` | 1,374,553.73 USD | `1,039.88` | `1302.72` | `1321.00` | `2865.92` | -19,876.92 USD | `-1.45%` | `10X Cross` |
| `1641` | `0x123d...3bff` | `SHORT` | 1,333,480.00 USD | `1,008.15` | `489.25` | `1321.00` | `4209.24` | -840,245.93 USD | `-63.01%` | `10X Cross` |
| `1650` | `0xe282...df29` | `LONG` | 1,322,200.00 USD | `1,000.00` | `420.99` | `1321.00` | `108.13` | 901,213.14 USD | `+68.16%` | `10X Cross` |
| `1651` | `0x266b...efcb` | `LONG` | 1,321,900.00 USD | `1,000.00` | `826.11` | `1321.00` | `156.30` | 495,787.07 USD | `+37.51%` | `10X Cross` |
| `1652` | `0xb5ff...d912` | `LONG` | 1,320,758.40 USD | `1,000.00` | `1141.93` | `1321.00` | `400.44` | 178,828.10 USD | `+13.54%` | `2X Cross` |
| `1653` | `0x0748...d4b2` | `LONG` | 1,320,758.40 USD | `1,000.00` | `1334.09` | `1321.00` | `0.000000` | -13,329.90 USD | `-1.01%` | `7X Cross` |
| `1676` | `0x17f0...094f` | `LONG` | 1,301,933.61 USD | `984.30` | `1287.23` | `1321.00` | `536.75` | 34,913.45 USD | `+2.68%` | `5X Cross` |
| `1750` | `0x757d...94ba` | `LONG` | 1,221,832.50 USD | `925.00` | `1558.31` | `1321.00` | `0.000000` | -219,608.08 USD | `-17.97%` | `10X Cross` |
| `1807` | `0x2847...d47b` | `LONG` | 1,168,032.40 USD | `883.00` | `1237.56` | `1321.00` | `0.000000` | 75,263.80 USD | `+6.44%` | `5X Cross` |
| `1811` | `0xf096...7553` | `SHORT` | 1,165,391.29 USD | `881.07` | `1240.34` | `1321.00` | `3521.14` | -72,561.20 USD | `-6.23%` | `10X Cross` |
| `1812` | `0xdf95...7d72` | `SHORT` | 1,164,298.01 USD | `880.31` | `1073.82` | `1321.00` | `41472.54` | -218,999.70 USD | `-18.81%` | `10X Cross` |
| `1827` | `0xcf0a...856f` | `LONG` | 1,152,182.99 USD | `871.15` | `1292.19` | `1321.00` | `938.45` | 26,488.14 USD | `+2.30%` | `4X Cross` |
| `1860` | `0x7d0f...ea35` | `LONG` | 1,124,295.00 USD | `850.00` | `1317.57` | `1321.00` | `1275.62` | 4,359.42 USD | `+0.39%` | `10X Cross` |
| `1895` | `0x601c...4f54` | `SHORT` | 1,090,377.89 USD | `824.42` | `615.11` | `1321.00` | `2930.59` | -583,265.14 USD | `-53.49%` | `5X Cross` |
| `1904` | `0xae55...2236` | `LONG` | 1,079,680.37 USD | `817.47` | `1467.80` | `1321.00` | `0.000000` | -120,200.85 USD | `-11.13%` | `10X Cross` |
| `1911` | `0x71b1...79c8` | `LONG` | 1,073,528.32 USD | `812.52` | `1231.55` | `1321.00` | `697.50` | 72,872.86 USD | `+6.79%` | `10X Cross` |
| `1934` | `0x0f02...5384` | `LONG` | 1,058,017.04 USD | `800.78` | `1290.36` | `1321.00` | `289.98` | 24,722.97 USD | `+2.34%` | `3X Cross` |
| `1935` | `0x9b0f...db40` | `LONG` | 1,057,560.00 USD | `800.00` | `1268.86` | `1321.00` | `774.65` | 42,470.24 USD | `+4.02%` | `10X Cross` |
| `1944` | `0xabdb...84ac` | `LONG` | 1,049,893.13 USD | `793.69` | `711.79` | `1321.00` | `664.32` | 484,952.77 USD | `+46.19%` | `3X Cross` |
| `1952` | `0xfdf8...e381` | `LONG` | 1,043,412.34 USD | `790.01` | `1337.72` | `1321.00` | `387.23` | -13,397.34 USD | `-1.28%` | `10X Cross` |
| `2012` | `0x0c1f...1d39` | `SHORT` | 1,008,087.64 USD | `762.99` | `1299.17` | `1321.00` | `4876.15` | -16,836.56 USD | `-1.67%` | `10X Cross` |
| `2019` | `0xf6f3...47f8` | `SHORT` | 1,006,719.38 USD | `761.57` | `1253.10` | `1321.00` | `2397.50` | -52,396.39 USD | `-5.20%` | `5X Cross` |
| `2024` | `0x389a...e76b` | `LONG` | 1,005,347.94 USD | `760.13` | `1266.20` | `1321.00` | `358.51` | 42,874.52 USD | `+4.26%` | `10X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `1297.10` | 194.56 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Long: 0.19K USD at 1297.1000 USD [API] | `2026-10-27 15:46:39` |
| `ANNOUNCEMENT` | `INFO` | `1326.30` | 13.26 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Long: 0.01K USD at 1326.3000 USD [API] | `2026-10-27 23:06:56` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`1404.15` (Vol: 3,000,000.00 USD, Dist: `+5.98%`) | Long MP=`1287.60` (Vol: 2,300,000.00 USD, Dist: `--2.81%`)
  * 48H Horizon: Short MP=`1404.15` (Vol: 3,000,000.00 USD, Dist: `+5.98%`) | Long MP=`1287.60` (Vol: 2,300,000.00 USD, Dist: `--2.81%`)
  * 3D Horizon: Short MP=`1404.42` (Vol: 3,000,000.00 USD, Dist: `+6.01%`) | Long MP=`1228.81` (Vol: 2,600,000.00 USD, Dist: `--7.25%`)
  * 7D Horizon: Short MP=`1404.10` (Vol: 3,000,000.00 USD, Dist: `+5.98%`) | Long MP=`1200.46` (Vol: 3,000,000.00 USD, Dist: `--9.39%`)
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
  * Current Rate: `89.74K` | Last 24h: `32.07K` | Last 3d: `282.84K` | Last 7d: `777.72K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0086%` | **USDT OKX** | `0.0100%` |
| **USDT Bybit** | `0.0100%` | **USDT KuCoin** | `0.0100%` |
| **USDT MEXC** | `0.0087%` | **USDT BingX** | `0.0071%` |
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
| `5:00 UTC` | `1343.25` | `1344.85` | `1343.25` | `1353.45` | `1340.25` | 26,552,172.39 USD | 11,915,117.49 USD | 14,637,054.90 USD | -2,721,937.40 USD | `-10.25%` | `0B / 9S` |
| `0:00 UTC` | `1342.95` | `1346.21` | `1342.95` | `1354.05` | `1340.25` | 27,005,669.33 USD | 14,153,013.83 USD | 12,852,655.50 USD | 1,300,358.33 USD | `+4.82%` | `5B / 3S` |
| `5:00 UTC` | `1348.65` | `1350.13` | `1348.65` | `1356.15` | `1344.45` | 21,612,679.16 USD | 11,526,731.97 USD | 10,085,947.19 USD | 1,440,784.78 USD | `+6.67%` | `2B / 2S` |
| `0:00 UTC` | `1335.45` | `1342.97` | `1335.45` | `1354.95` | `1333.05` | 31,234,081.19 USD | 13,144,149.56 USD | 18,089,931.62 USD | -4,945,782.06 USD | `-15.83%` | `2B / 7S` |
| `5:00 UTC` | `1333.95` | `1332.65` | `1333.95` | `1338.15` | `1327.05` | 42,051,592.22 USD | 20,998,597.47 USD | 21,052,994.75 USD | -54,397.28 USD | `-0.13%` | `1B / 3S` |
| `0:00 UTC` | `1324.05` | `1326.61` | `1324.05` | `1336.05` | `1320.15` | 35,175,848.19 USD | 15,805,961.43 USD | 19,369,886.76 USD | -3,563,925.33 USD | `-10.13%` | `1B / 10S` |
| `5:00 UTC` | `1321.35` | `1325.74` | `1321.35` | `1333.35` | `1318.35` | 26,289,288.34 USD | 11,537,630.34 USD | 14,751,657.99 USD | -3,214,027.65 USD | `-12.23%` | `3B / 5S` |
| `0:00 UTC` | `1315.95` | `1314.40` | `1315.95` | `1321.95` | `1307.85` | 50,919,152.62 USD | 22,517,005.07 USD | 28,402,147.55 USD | -5,885,142.49 USD | `-11.56%` | `2B / 5S` |
| `5:00 UTC` | `1315.95` | `1319.00` | `1315.95` | `1325.85` | `1312.05` | 22,246,351.59 USD | 13,151,982.06 USD | 9,094,369.53 USD | 4,057,612.52 USD | `+18.24%` | `9B / 1S` |
| `0:00 UTC` | `1318.35` | `1319.59` | `1318.35` | `1325.25` | `1315.95` | 9,682,926.91 USD | 4,714,231.14 USD | 4,968,695.78 USD | -254,464.64 USD | `-2.63%` | `1B / 2S` |

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
| `5m` | -132,960.00 USD | 349,490.00 USD | **`ACCUMULATION`** |
| `15m` | 1,330,000.00 USD | 10,260,000.00 USD | **`ACCUMULATION`** |
| `30m` | 1,740,000.00 USD | 7,550,000.00 USD | **`ACCUMULATION`** |
| `1h` | 829,590.00 USD | -8,370,000.00 USD | **`DISTRIBUTION`** |
| `2h` | 6,200,000.00 USD | -15,090,000.00 USD | **`DISTRIBUTION`** |
| `4h` | 21,470,000.00 USD | 63,990,000.00 USD | **`ACCUMULATION`** |
| `6h` | 29,790,000.00 USD | 84,580,000.00 USD | **`ACCUMULATION`** |
| `8h` | 31,900,000.00 USD | 100,120,000.00 USD | **`ACCUMULATION`** |
| `12h` | 28,660,000.00 USD | 106,330,000.00 USD | **`ACCUMULATION`** |
| `24h` | 12,450,000.00 USD | 76,790,000.00 USD | **`ACCUMULATION`** |
| `1w` | 50,930,000.00 USD | 250,980,000.00 USD | **`ACCUMULATION`** |
| `30d` | 66,870,000.00 USD | -508,390,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-132.96K` | 15m=`+1.33M` | 1h=`+829.59K` | 24h=`+12.45M`
* Futures Capital Netflows: 5m=`+349.49K` | 15m=`+10.26M` | 1h=`-8.37M` | 24h=`+76.79M`
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
  * `2026-10-30 00:17:29 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 00:39:29 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 00:39:29 IST`: [@DeItaone] - (Sentiment: `Neutral`)
  * `2026-10-30 00:39:29 IST`: [@mb_ghalibaf] - (Sentiment: `Neutral`)
  * `2026-10-30 00:39:29 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-30 00:39:29 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-30 00:39:29 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-30 00:38:29 IST`: [fxstreet.com] - (Sentiment: `Neutral`)
  * `2026-10-29 21:40:29 IST`: [ForexFactory] - (Sentiment: `Neutral`)
  * `2026-10-29 21:40:29 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-29 21:40:29 IST`: [youtube.com/bankofcanadaofficial] - (Sentiment: `Neutral`)
  * `2026-10-29 21:40:29 IST`: [notayesmanseconomics.wordpress.com] - (Sentiment: `Neutral`)
  * `2026-10-29 20:40:29 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 20:40:29 IST`: [breakingthenews.net] - (Sentiment: `Neutral`)
  * `2026-10-29 20:40:29 IST`: [@financialjuice] - (Sentiment: `Neutral`)


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
  * Spread-Padded Stop Loss: `1209.18` (Risk Distance: `21.37` pts)
  * +2.5R Take Profit: `1283.96`
  * Mathematical Lot Sizing: **`0.46 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `1307.14` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `1328.51` (Risk Distance: `21.37` pts)
  * +2.5R Take Profit: `1253.73`
  * Mathematical Lot Sizing: **`0.46 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`1331.82`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
