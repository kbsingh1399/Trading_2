# 🏛️ SOVEREIGN CANDIDATE DOSSIER: ZECUSD
**Canonical Key**: `ZECUSD` | **Broker Instrument**: `ZECUSD.p` | **Asset Class**: `Crypto Altcoin`
**Timestamp**: `2026-10-30 00:20:14 IST` (`2026-10-29 18:50:14 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `1315.99` | **Live Ask Quote**: `1316.52` | **Mid Price**: `1316.26`
- **Spread Points**: `53.00` | **Spread BPS**: `4.03 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `1316.26` | VWAP Z-Score: `+0.00` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `3.29` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `50.00` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `1325.47` | Lower -3.00σ Band: `1307.04`
  * Upper +2.51σ Band: `1323.49` | Lower -2.51σ Band: `1309.02`
  * Upper +2.01σ Band: `1321.78` | Lower -2.01σ Band: `1310.73`
  * Upper +2.00σ Band: `1321.52` | Lower -2.00σ Band: `1310.99`
  * Upper +1.28σ Band: `1319.94` | Lower -1.28σ Band: `1312.57`
  * Upper +1.00σ Band: `1318.89` | Lower -1.00σ Band: `1313.62`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`1316.26` | EMA-20=`1316.26` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`1316.26` (Slope: `+0.0000`) | EMA-100=`1316.26`
  * Institutional Anchors: EMA-144=`1316.26` | EMA-200=`1316.26` (Slope: `+0.0000`) | EMA-233=`1316.26`
- **Range Boundaries**: 24H High=`1329.42` | 24H Low=`1303.09` | Weekly High=`1342.58` | Weekly Low=`1289.93`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `1306.03` (Distance: `+0.79%`)
  * Point of Control (POC) = `1247.20` (Distance: `+5.54%`)
  * Value Area Low (VAL) = `1230.55` (Distance: `+6.97%`)
  * Auction Positioning: `ABOVE_VALUE (Imbalance)` | Session Bias: **`BULLISH (Above Pivot)`** | Market Regime: `RANGE_EXPANSION`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`1320.44` | POC=`1312.10` | VAL=`1285.78`
  * Prior Day Extremes: PDH=`1328.99` | PDL=`1263.19` | PDC=`1296.46`
  * Monday Range Blueprint: High=`1267.53` | Mid=`1222.14` | Low=`1176.75`
  * Developing Weekly Value Area: Weekly VAH=`1294.68` | Weekly POC=`1239.01` | Weekly VAL=`1195.06`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`1318.68` | Low=`1230.00`
  * London Session (08:00-16:00 UTC): High=`1276.13` | Low=`1233.52`
  * New York Session (13:00-21:00 UTC): High=`1396.49` | Low=`1250.65`
  * Initial Balance (First Hour): IB High=`1255.79` | IB Low=`1245.43`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `1310.99` - `1321.52`
  * Optimal Trade Entry (OTE 0.705): `1318.89`
  * Structural Invalidation Anchor (0.786): `1326.79`

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
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 00:15:45 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `16` | `0xb83d...6e36` | `SHORT` | 69,203,854.57 USD | `52,582.52` | `1336.45` | `1313.80` | `3711.22` | 1,070,060.32 USD | `+1.55%` | `3X Cross` |
| `24` | `0x5b5d...c060` | `SHORT` | 53,592,932.54 USD | `40,727.61` | `1478.36` | `1313.80` | `5017.73` | 6,617,331.65 USD | `+12.35%` | `3X Cross` |
| `42` | `0x7fda...17d1` | `SHORT` | 29,509,515.23 USD | `22,421.94` | `1261.40` | `1313.80` | `2801.88` | -1,226,386.09 USD | `-4.16%` | `5X Cross` |
| `79` | `0x60b0...991e` | `LONG` | 22,095,561.63 USD | `16,779.74` | `1179.65` | `1313.80` | `890.71` | 2,301,314.62 USD | `+10.42%` | `10X Cross` |
| `83` | `0xbf73...5d58` | `LONG` | 21,054,192.00 USD | `16,000.00` | `1214.30` | `1313.80` | `713.78` | 1,625,359.75 USD | `+7.72%` | `10X Cross` |
| `134` | `0xc36a...105b` | `LONG` | 15,147,088.04 USD | `11,510.82` | `1215.14` | `1313.80` | `933.93` | 1,159,807.01 USD | `+7.66%` | `10X Cross` |
| `157` | `0x9071...5c0b` | `LONG` | 13,318,853.03 USD | `10,119.94` | `1370.53` | `1313.80` | `682.76` | -550,818.00 USD | `-4.14%` | `2X Cross` |
| `171` | `0x8742...8427` | `LONG` | 12,116,227.86 USD | `9,201.21` | `1286.37` | `1313.80` | `698.34` | 280,057.86 USD | `+2.31%` | `10X Cross` |
| `193` | `0xad59...ba81` | `SHORT` | 11,089,827.50 USD | `8,425.00` | `330.91` | `1313.80` | `2139.06` | -8,301,869.73 USD | `-74.86%` | `10X Cross` |
| `200` | `0xdd53...2b13` | `SHORT` | 10,835,472.70 USD | `8,231.14` | `739.37` | `1313.80` | `7870.54` | -4,749,591.22 USD | `-43.83%` | `3X Cross` |
| `201` | `0x9ffd...ce40` | `LONG` | 10,821,263.74 USD | `8,222.22` | `1253.28` | `1313.80` | `572.05` | 516,493.69 USD | `+4.77%` | `5X Cross` |
| `220` | `0xfc66...ca06` | `SHORT` | 10,228,688.09 USD | `7,773.15` | `1319.72` | `1313.80` | `5590.82` | 29,721.84 USD | `+0.29%` | `10X Cross` |
| `222` | `0x880a...311c` | `SHORT` | 10,141,786.05 USD | `7,707.11` | `1367.50` | `1313.80` | `2303.45` | 397,698.15 USD | `+3.92%` | `10X Cross` |
| `269` | `0x2b61...2f6c` | `LONG` | 8,957,331.30 USD | `6,807.00` | `1453.56` | `1313.80` | `638.62` | -937,019.92 USD | `-10.46%` | `10X Cross` |
| `287` | `0x2ae5...83e7` | `LONG` | 8,475,978.24 USD | `6,436.80` | `1391.82` | `1313.80` | `0.000000` | -482,913.75 USD | `-5.70%` | `2X Cross` |
| `327` | `0xecb6...2b00` | `SHORT` | 7,319,240.09 USD | `5,561.31` | `1324.05` | `1313.80` | `5997.57` | 44,227.03 USD | `+0.60%` | `5X Cross` |
| `333` | `0x26b6...9a13` | `LONG` | 7,155,135.66 USD | `5,433.73` | `1282.23` | `1313.80` | `207.28` | 187,832.43 USD | `+2.63%` | `10X Cross` |
| `345` | `0x45d2...4029` | `SHORT` | 6,879,254.70 USD | `5,227.00` | `833.44` | `1313.80` | `8011.72` | -2,522,876.73 USD | `-36.67%` | `5X Cross` |
| `368` | `0xea00...a918` | `LONG` | 6,584,000.00 USD | `5,000.00` | `739.16` | `1313.80` | `0.000000` | 2,888,184.89 USD | `+43.87%` | `5X Cross` |
| `378` | `0xdd7a...8830` | `LONG` | 6,396,496.06 USD | `4,860.19` | `897.48` | `1313.80` | `780.14` | 2,034,592.39 USD | `+31.81%` | `10X Cross` |
| `388` | `0xf081...e39e` | `LONG` | 6,218,892.80 USD | `4,717.00` | `1195.70` | `1313.80` | `1200.07` | 578,768.76 USD | `+9.31%` | `10X Cross` |
| `438` | `0x4cae...7c34` | `LONG` | 5,269,337.32 USD | `4,004.36` | `999.34` | `1313.80` | `736.82` | 1,267,609.17 USD | `+24.06%` | `10X Cross` |
| `452` | `0xa61c...66b9` | `LONG` | 5,116,639.10 USD | `3,888.00` | `1148.34` | `1313.80` | `0.000000` | 651,896.96 USD | `+12.74%` | `10X Cross` |
| `474` | `0x9aa5...58af` | `SHORT` | 4,895,555.93 USD | `3,720.31` | `1205.51` | `1313.80` | `3334.50` | -410,669.13 USD | `-8.39%` | `10X Cross` |
| `481` | `0x0153...8052` | `SHORT` | 4,869,393.61 USD | `3,698.18` | `1307.82` | `1313.80` | `2504.67` | -32,822.86 USD | `-0.67%` | `1X Isolated` |
| `503` | `0xd4c1...3d1d` | `SHORT` | 4,548,676.37 USD | `3,456.42` | `1302.96` | `1313.80` | `2668.96` | -45,084.22 USD | `-0.99%` | `10X Cross` |
| `526` | `0x382b...3e39` | `LONG` | 4,338,487.30 USD | `3,294.72` | `1173.49` | `1313.80` | `0.000000` | 472,164.16 USD | `+10.88%` | `10X Cross` |
| `534` | `0xd21d...90f1` | `LONG` | 4,277,975.00 USD | `3,250.00` | `1253.64` | `1313.80` | `875.86` | 203,633.27 USD | `+4.76%` | `4X Isolated` |
| `551` | `0x456f...cdf1` | `LONG` | 4,151,988.91 USD | `3,153.09` | `1268.52` | `1313.80` | `498.76` | 152,222.71 USD | `+3.67%` | `10X Cross` |
| `553` | `0x1338...c48e` | `LONG` | 4,144,964.82 USD | `3,149.43` | `1018.52` | `1313.80` | `820.16` | 937,219.28 USD | `+22.61%` | `4X Isolated` |
| `568` | `0xdbe0...d6d5` | `LONG` | 4,062,815.22 USD | `3,085.37` | `422.97` | `1313.80` | `338.47` | 2,757,810.72 USD | `+67.88%` | `3X Isolated` |
| `592` | `0x9c06...0560` | `SHORT` | 3,934,238.95 USD | `2,989.80` | `786.00` | `1313.80` | `2375.83` | -1,584,243.95 USD | `-40.27%` | `10X Cross` |
| `608` | `0x27c9...d65d` | `SHORT` | 3,832,677.18 USD | `2,912.59` | `1248.26` | `1313.80` | `1839.80` | -197,015.84 USD | `-5.14%` | `10X Cross` |
| `690` | `0xac48...3201` | `LONG` | 3,345,067.04 USD | `2,540.30` | `1393.86` | `1313.80` | `525.75` | -195,762.25 USD | `-5.85%` | `10X Cross` |
| `692` | `0xa183...0482` | `LONG` | 3,334,593.23 USD | `2,534.00` | `530.25` | `1313.80` | `444.40` | 1,990,930.51 USD | `+59.71%` | `5X Isolated` |
| `702` | `0x2e30...4cb5` | `SHORT` | 3,297,700.06 USD | `2,505.28` | `1299.09` | `1313.80` | `3133.68` | -43,104.79 USD | `-1.31%` | `2X Cross` |
| `705` | `0x325e...9564` | `LONG` | 3,292,533.58 USD | `2,501.91` | `1306.24` | `1313.80` | `0.000000` | 24,439.67 USD | `+0.74%` | `10X Cross` |
| `707` | `0x0871...e927` | `LONG` | 3,289,750.00 USD | `2,500.00` | `1276.50` | `1313.80` | `0.000000` | 98,500.00 USD | `+2.99%` | `10X Cross` |
| `715` | `0x9b86...6e6e` | `LONG` | 3,247,706.99 USD | `2,467.30` | `637.58` | `1313.80` | `889.62` | 1,674,607.39 USD | `+51.56%` | `3X Cross` |
| `778` | `0xb2f7...af9f` | `SHORT` | 3,045,086.89 USD | `2,313.72` | `746.63` | `1313.80` | `4195.78` | -1,317,598.15 USD | `-43.27%` | `10X Cross` |
| `784` | `0x634f...6951` | `LONG` | 2,990,247.94 USD | `2,272.42` | `1281.94` | `1313.80` | `1250.01` | 77,147.47 USD | `+2.58%` | `10X Cross` |
| `804` | `0xf48f...10fe` | `LONG` | 2,919,754.69 USD | `2,218.49` | `1517.87` | `1313.80` | `896.91` | -447,632.14 USD | `-15.33%` | `3X Cross` |
| `832` | `0x5bc4...3b0c` | `SHORT` | 2,804,906.14 USD | `2,130.74` | `1089.65` | `1313.80` | `3571.78` | -483,148.56 USD | `-17.23%` | `5X Cross` |
| `845` | `0x8de4...b9aa` | `SHORT` | 2,752,346.77 USD | `2,091.29` | `1331.35` | `1313.80` | `1689.79` | 31,892.94 USD | `+1.16%` | `3X Cross` |
| `850` | `0x4fe2...ac59` | `SHORT` | 2,726,600.43 USD | `2,071.57` | `1478.56` | `1313.80` | `1801.59` | 336,345.78 USD | `+12.34%` | `10X Cross` |
| `870` | `0x668c...ea2e` | `SHORT` | 2,631,800.00 USD | `2,000.00` | `1409.16` | `1313.80` | `2702.09` | 186,522.04 USD | `+7.09%` | `10X Cross` |
| `894` | `0x77ee...2902` | `SHORT` | 2,560,780.88 USD | `1,946.03` | `759.84` | `1313.80` | `5215.92` | -1,082,103.37 USD | `-42.26%` | `10X Cross` |
| `903` | `0x3e2f...b269` | `SHORT` | 2,534,741.36 USD | `1,925.51` | `1134.87` | `1313.80` | `2931.72` | -349,542.51 USD | `-13.79%` | `10X Cross` |
| `910` | `0xe097...d0fe` | `LONG` | 2,518,819.03 USD | `1,913.56` | `1261.17` | `1313.80` | `0.000000` | 105,492.86 USD | `+4.19%` | `10X Cross` |
| `917` | `0x4f12...618b` | `SHORT` | 2,495,694.11 USD | `1,896.28` | `1608.30` | `1313.80` | `2116.68` | 554,090.28 USD | `+22.20%` | `3X Cross` |
| `960` | `0x866d...d6e1` | `LONG` | 2,375,642.52 USD | `1,802.05` | `674.73` | `1313.80` | `83.99` | 1,159,741.20 USD | `+48.82%` | `10X Cross` |
| `997` | `0x2309...a2d9` | `LONG` | 2,303,311.88 USD | `1,750.37` | `1186.09` | `1313.80` | `805.27` | 227,217.77 USD | `+9.86%` | `8X Cross` |
| `1000` | `0x023a...2355` | `SHORT` | 2,277,208.35 USD | `1,730.27` | `1313.33` | `1313.80` | `5954.20` | -4,798.88 USD | `-0.21%` | `10X Cross` |
| `1015` | `0x2edd...8179` | `SHORT` | 2,234,174.50 USD | `1,697.83` | `1261.26` | `1313.80` | `2962.65` | -92,763.24 USD | `-4.15%` | `10X Cross` |
| `1046` | `0xa271...a3f7` | `LONG` | 2,147,288.17 USD | `1,631.43` | `1190.60` | `1313.80` | `910.25` | 204,906.36 USD | `+9.54%` | `4X Cross` |
| `1058` | `0x7f75...9edf` | `LONG` | 2,113,025.03 USD | `1,605.78` | `1199.97` | `1313.80` | `973.68` | 186,133.13 USD | `+8.81%` | `10X Cross` |
| `1059` | `0x265e...7f70` | `LONG` | 2,108,050.01 USD | `1,601.74` | `1388.09` | `1313.80` | `0.000000` | -115,314.99 USD | `-5.47%` | `3X Cross` |
| `1062` | `0x6646...6de5` | `SHORT` | 2,107,040.00 USD | `1,600.00` | `660.64` | `1313.80` | `4798.45` | -1,050,015.03 USD | `-49.83%` | `10X Cross` |
| `1080` | `0x71d0...8c26` | `SHORT` | 2,080,794.19 USD | `1,580.19` | `1361.12` | `1313.80` | `6039.30` | 70,034.32 USD | `+3.37%` | `10X Cross` |
| `1084` | `0xdf57...93f5` | `LONG` | 2,079,596.06 USD | `1,579.76` | `1218.38` | `1313.80` | `780.10` | 154,840.08 USD | `+7.45%` | `3X Isolated` |
| `1094` | `0xab59...59b5` | `LONG` | 2,061,213.38 USD | `1,565.32` | `1342.15` | `1313.80` | `790.84` | -39,681.84 USD | `-1.93%` | `10X Cross` |
| `1096` | `0xfe7c...b7ae` | `SHORT` | 2,057,486.83 USD | `1,562.49` | `1350.62` | `1313.80` | `6498.96` | 52,842.22 USD | `+2.57%` | `10X Cross` |
| `1109` | `0x3e47...aaf6` | `LONG` | 2,022,205.36 USD | `1,536.28` | `1277.06` | `1313.80` | `1011.01` | 60,283.28 USD | `+2.98%` | `10X Cross` |
| `1157` | `0xcf67...eb24` | `LONG` | 1,974,300.00 USD | `1,500.00` | `887.05` | `1313.80` | `546.02` | 643,728.63 USD | `+32.61%` | `10X Cross` |
| `1173` | `0x039c...0ebd` | `SHORT` | 1,948,176.79 USD | `1,480.49` | `1238.67` | `1313.80` | `3134.31` | -114,345.47 USD | `-5.87%` | `10X Cross` |
| `1222` | `0xfc27...9d9d` | `SHORT` | 1,874,521.23 USD | `1,424.30` | `1317.50` | `1313.80` | `11362.89` | 1,988.68 USD | `+0.11%` | `10X Cross` |
| `1243` | `0x2ab7...c2f8` | `LONG` | 1,843,211.21 USD | `1,400.51` | `813.26` | `1313.80` | `793.23` | 704,229.53 USD | `+38.21%` | `3X Cross` |
| `1258` | `0x11be...8b1d` | `LONG` | 1,811,692.94 USD | `1,375.83` | `1206.55` | `1313.80` | `1134.38` | 151,684.99 USD | `+8.37%` | `10X Isolated` |
| `1306` | `0xdf83...3cff` | `SHORT` | 1,743,858.82 USD | `1,325.02` | `1246.70` | `1313.80` | `1841.47` | -91,955.90 USD | `-5.27%` | `10X Cross` |
| `1316` | `0xef96...9383` | `SHORT` | 1,722,276.24 USD | `1,308.82` | `1249.96` | `1313.80` | `4180.83` | -86,309.82 USD | `-5.01%` | `10X Cross` |
| `1366` | `0xe065...0f85` | `SHORT` | 1,661,847.28 USD | `1,262.61` | `1087.02` | `1313.80` | `1756.92` | -289,371.15 USD | `-17.41%` | `10X Cross` |
| `1390` | `0x7277...0b98` | `SHORT` | 1,625,948.34 USD | `1,234.96` | `1298.48` | `1313.80` | `2360.76` | -22,378.92 USD | `-1.38%` | `10X Cross` |
| `1435` | `0x5975...9abd` | `LONG` | 1,580,160.00 USD | `1,200.00` | `1179.54` | `1313.80` | `272.81` | 164,717.21 USD | `+10.42%` | `5X Cross` |
| `1480` | `0x69cc...14fd` | `SHORT` | 1,529,046.58 USD | `1,161.36` | `675.33` | `1313.80` | `7816.95` | -744,741.05 USD | `-48.71%` | `10X Cross` |
| `1485` | `0x7a76...b16d` | `LONG` | 1,525,715.25 USD | `1,159.27` | `1358.50` | `1313.80` | `1237.14` | -49,153.26 USD | `-3.22%` | `10X Cross` |
| `1493` | `0x3fc5...c0c1` | `SHORT` | 1,512,265.79 USD | `1,148.44` | `1264.34` | `1313.80` | `3086.57` | -60,252.02 USD | `-3.98%` | `10X Cross` |
| `1510` | `0xe35c...a1d3` | `LONG` | 1,483,219.98 USD | `1,127.06` | `1318.20` | `1313.80` | `694.30` | -2,475.37 USD | `-0.17%` | `2X Isolated` |
| `1517` | `0x5f94...4b96` | `LONG` | 1,468,029.90 USD | `1,115.27` | `538.00` | `1313.80` | `0.000000` | 868,012.26 USD | `+59.13%` | `10X Cross` |
| `1539` | `0x71df...a23d` | `SHORT` | 1,445,226.65 USD | `1,098.28` | `513.50` | `1313.80` | `2546.52` | -881,256.46 USD | `-60.98%` | `2X Cross` |
| `1576` | `0xbfc7...80b4` | `SHORT` | 1,414,592.50 USD | `1,075.00` | `558.03` | `1313.80` | `5464.94` | -814,713.77 USD | `-57.59%` | `10X Cross` |
| `1613` | `0x51f6...2b39` | `SHORT` | 1,369,313.98 USD | `1,039.88` | `1302.72` | `1313.80` | `2890.97` | -14,637.18 USD | `-1.07%` | `10X Cross` |
| `1645` | `0x123d...3bff` | `SHORT` | 1,327,531.92 USD | `1,008.15` | `489.25` | `1313.80` | `4202.61` | -834,297.85 USD | `-62.85%` | `10X Cross` |
| `1654` | `0x0748...d4b2` | `LONG` | 1,316,808.10 USD | `1,000.00` | `1334.09` | `1313.80` | `0.000000` | -17,280.20 USD | `-1.31%` | `7X Cross` |
| `1655` | `0xb5ff...d912` | `LONG` | 1,316,800.00 USD | `1,000.00` | `1141.93` | `1313.80` | `400.42` | 174,869.70 USD | `+13.28%` | `2X Cross` |
| `1656` | `0x266b...efcb` | `LONG` | 1,316,700.00 USD | `1,000.00` | `826.11` | `1313.80` | `137.69` | 490,587.07 USD | `+37.26%` | `10X Cross` |
| `1658` | `0xe282...df29` | `LONG` | 1,316,100.00 USD | `1,000.00` | `420.99` | `1313.80` | `105.50` | 895,113.14 USD | `+68.01%` | `10X Cross` |
| `1686` | `0x17f0...094f` | `LONG` | 1,295,240.37 USD | `984.30` | `1287.23` | `1313.80` | `536.73` | 28,220.21 USD | `+2.18%` | `5X Cross` |
| `1752` | `0x757d...94ba` | `LONG` | 1,217,670.00 USD | `925.00` | `1558.31` | `1313.80` | `0.000000` | -223,770.58 USD | `-18.38%` | `10X Cross` |
| `1818` | `0xf096...7553` | `SHORT` | 1,159,576.23 USD | `881.07` | `1240.34` | `1313.80` | `3504.87` | -66,746.14 USD | `-5.76%` | `10X Cross` |
| `1820` | `0xdf95...7d72` | `SHORT` | 1,158,388.49 USD | `880.31` | `1073.81` | `1313.80` | `41600.88` | -213,099.92 USD | `-18.40%` | `10X Cross` |
| `1822` | `0x2847...d47b` | `LONG` | 1,156,781.37 USD | `879.08` | `1237.19` | `1313.80` | `0.000000` | 69,188.72 USD | `+5.98%` | `5X Cross` |
| `1833` | `0xcf0a...856f` | `LONG` | 1,146,334.96 USD | `871.15` | `1292.19` | `1313.80` | `938.44` | 20,640.11 USD | `+1.80%` | `4X Cross` |
| `1862` | `0x7d0f...ea35` | `LONG` | 1,118,685.00 USD | `850.00` | `1317.57` | `1313.80` | `1275.61` | -1,250.58 USD | `-0.11%` | `10X Cross` |
| `1889` | `0x3205...40bb` | `SHORT` | 1,098,057.46 USD | `834.20` | `1334.55` | `1313.80` | `2923.99` | 15,228.09 USD | `+1.39%` | `10X Cross` |
| `1899` | `0x601c...4f54` | `SHORT` | 1,085,019.16 USD | `824.42` | `615.11` | `1313.80` | `2909.85` | -577,906.41 USD | `-53.26%` | `5X Cross` |
| `1908` | `0xae55...2236` | `LONG` | 1,076,444.50 USD | `817.47` | `1467.80` | `1313.80` | `0.000000` | -123,436.72 USD | `-11.47%` | `10X Cross` |
| `1915` | `0x71b1...79c8` | `LONG` | 1,069,372.77 USD | `812.52` | `1231.55` | `1313.80` | `700.75` | 68,717.31 USD | `+6.43%` | `10X Cross` |
| `1937` | `0x0f02...5384` | `LONG` | 1,054,306.95 USD | `800.78` | `1290.36` | `1313.80` | `286.76` | 21,012.88 USD | `+1.99%` | `3X Cross` |
| `1940` | `0x9b0f...db40` | `LONG` | 1,053,040.00 USD | `800.00` | `1268.86` | `1313.80` | `775.97` | 37,950.24 USD | `+3.60%` | `10X Cross` |
| `1955` | `0xabdb...84ac` | `LONG` | 1,044,416.67 USD | `793.69` | `711.79` | `1313.80` | `664.30` | 479,476.31 USD | `+45.91%` | `3X Cross` |
| `1961` | `0xfdf8...e381` | `LONG` | 1,040,291.57 USD | `790.01` | `1337.72` | `1313.80` | `407.06` | -16,518.12 USD | `-1.59%` | `10X Cross` |
| `1992` | `0x4e23...20c3` | `LONG` | 1,021,497.28 USD | `775.86` | `1306.32` | `1313.80` | `0.000000` | 7,978.05 USD | `+0.78%` | `4X Cross` |
| `2018` | `0x0c1f...1d39` | `SHORT` | 1,004,552.63 USD | `762.99` | `1299.17` | `1313.80` | `4835.77` | -13,301.55 USD | `-1.32%` | `10X Cross` |
| `2030` | `0xf6f3...47f8` | `SHORT` | 1,002,394.43 USD | `761.57` | `1253.10` | `1313.80` | `2403.12` | -48,071.43 USD | `-4.80%` | `5X Cross` |
| `2032` | `0x389a...e76b` | `LONG` | 1,000,559.12 USD | `760.13` | `1266.20` | `1313.80` | `360.61` | 38,085.70 USD | `+3.81%` | `10X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `1297.10` | 194.56 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Long: 0.19K USD at 1297.1000 USD [API] | `2026-10-27 15:46:39` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`1404.15` (Vol: 3,000,000.00 USD, Dist: `+6.30%`) | Long MP=`1287.60` (Vol: 2,300,000.00 USD, Dist: `--2.52%`)
  * 48H Horizon: Short MP=`1404.15` (Vol: 3,000,000.00 USD, Dist: `+6.30%`) | Long MP=`1287.60` (Vol: 2,300,000.00 USD, Dist: `--2.52%`)
  * 3D Horizon: Short MP=`1404.42` (Vol: 3,000,000.00 USD, Dist: `+6.32%`) | Long MP=`1228.81` (Vol: 2,600,000.00 USD, Dist: `--6.97%`)
  * 7D Horizon: Short MP=`1404.10` (Vol: 3,000,000.00 USD, Dist: `+6.30%`) | Long MP=`1200.46` (Vol: 3,000,000.00 USD, Dist: `--9.12%`)
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
  * Current Rate: `95.86K` | Last 24h: `32.07K` | Last 3d: `282.84K` | Last 7d: `777.72K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0095%` | **USDT OKX** | `0.0100%` |
| **USDT Bybit** | `0.0100%` | **USDT KuCoin** | `0.0100%` |
| **USDT MEXC** | `0.0095%` | **USDT BingX** | `0.0077%` |
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
| `5:00 UTC` | `1359.75` | `1358.32` | `1359.75` | `1373.25` | `1346.25` | 77,512,400.13 USD | 36,921,415.88 USD | 40,590,984.25 USD | -3,669,568.36 USD | `-4.73%` | `4B / 13S` |
| `0:00 UTC` | `1353.15` | `1350.71` | `1353.15` | `1361.25` | `1341.75` | 52,010,841.39 USD | 26,247,439.78 USD | 25,763,401.61 USD | 484,038.17 USD | `+0.93%` | `5B / 3S` |
| `5:00 UTC` | `1343.25` | `1344.85` | `1343.25` | `1353.45` | `1340.25` | 26,552,172.39 USD | 11,915,117.49 USD | 14,637,054.90 USD | -2,721,937.40 USD | `-10.25%` | `0B / 9S` |
| `0:00 UTC` | `1342.95` | `1346.21` | `1342.95` | `1354.05` | `1340.25` | 27,005,669.33 USD | 14,153,013.83 USD | 12,852,655.50 USD | 1,300,358.33 USD | `+4.82%` | `5B / 3S` |
| `5:00 UTC` | `1348.65` | `1350.13` | `1348.65` | `1356.15` | `1344.45` | 21,612,679.16 USD | 11,526,731.97 USD | 10,085,947.19 USD | 1,440,784.78 USD | `+6.67%` | `2B / 2S` |
| `0:00 UTC` | `1335.45` | `1342.97` | `1335.45` | `1354.95` | `1333.05` | 31,234,081.19 USD | 13,144,149.56 USD | 18,089,931.62 USD | -4,945,782.06 USD | `-15.83%` | `2B / 7S` |
| `5:00 UTC` | `1333.95` | `1332.65` | `1333.95` | `1338.15` | `1327.05` | 42,051,592.22 USD | 20,998,597.47 USD | 21,052,994.75 USD | -54,397.28 USD | `-0.13%` | `1B / 3S` |
| `0:00 UTC` | `1324.05` | `1326.61` | `1324.05` | `1336.05` | `1320.15` | 35,175,848.19 USD | 15,805,961.43 USD | 19,369,886.76 USD | -3,563,925.33 USD | `-10.13%` | `1B / 10S` |
| `5:00 UTC` | `1321.35` | `1325.74` | `1321.35` | `1333.35` | `1318.35` | 26,289,288.34 USD | 11,537,630.34 USD | 14,751,657.99 USD | -3,214,027.65 USD | `-12.23%` | `3B / 5S` |
| `0:00 UTC` | `1315.95` | `1314.37` | `1315.95` | `1321.95` | `1307.85` | 46,864,087.78 USD | 20,067,820.53 USD | 26,796,267.24 USD | -6,728,446.71 USD | `-14.36%` | `2B / 5S` |

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
| `5m` | 620,620.00 USD | -5,390,000.00 USD | **`DISTRIBUTION`** |
| `15m` | -563,120.00 USD | -11,210,000.00 USD | **`DISTRIBUTION`** |
| `30m` | -1,470,000.00 USD | -15,940,000.00 USD | **`DISTRIBUTION`** |
| `1h` | -1,300,000.00 USD | -26,770,000.00 USD | **`DISTRIBUTION`** |
| `2h` | 2,510,000.00 USD | -31,250,000.00 USD | **`DISTRIBUTION`** |
| `4h` | 15,740,000.00 USD | 53,900,000.00 USD | **`ACCUMULATION`** |
| `6h` | 28,210,000.00 USD | 79,410,000.00 USD | **`ACCUMULATION`** |
| `8h` | 32,180,000.00 USD | 87,800,000.00 USD | **`ACCUMULATION`** |
| `12h` | 26,300,000.00 USD | 94,820,000.00 USD | **`ACCUMULATION`** |
| `24h` | 12,150,000.00 USD | 68,360,000.00 USD | **`ACCUMULATION`** |
| `1w` | 51,030,000.00 USD | 232,700,000.00 USD | **`ACCUMULATION`** |
| `30d` | 65,390,000.00 USD | -556,560,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+620.62K` | 15m=`-563.12K` | 1h=`-1.30M` | 24h=`+12.15M`
* Futures Capital Netflows: 5m=`-5.39M` | 15m=`-11.21M` | 1h=`-26.77M` | 24h=`+68.36M`
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
  * `2026-10-29 23:31:18 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:26:18 IST`: [@DeItaone] - (Sentiment: `Neutral`)
  * `2026-10-30 00:11:18 IST`: [@mb_ghalibaf] - (Sentiment: `Neutral`)
  * `2026-10-30 00:11:18 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-30 00:11:18 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-30 00:11:18 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-30 00:10:18 IST`: [fxstreet.com] - (Sentiment: `Neutral`)
  * `2026-10-30 00:10:18 IST`: [ForexFactory] - (Sentiment: `Neutral`)
  * `2026-10-29 21:12:18 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-29 21:12:18 IST`: [youtube.com/bankofcanadaofficial] - (Sentiment: `Neutral`)
  * `2026-10-29 21:12:18 IST`: [notayesmanseconomics.wordpress.com] - (Sentiment: `Neutral`)
  * `2026-10-29 21:12:18 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 20:12:18 IST`: [breakingthenews.net] - (Sentiment: `Neutral`)
  * `2026-10-29 20:12:18 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-29 20:12:18 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)


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
  * Spread-Padded Stop Loss: `1225.81` (Risk Distance: `4.74` pts)
  * +2.5R Take Profit: `1242.41`
  * Mathematical Lot Sizing: **`2.10 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `1306.03` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `1310.77` (Risk Distance: `4.74` pts)
  * +2.5R Take Profit: `1294.17`
  * Mathematical Lot Sizing: **`2.10 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`1326.79`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
