# 🏛️ SOVEREIGN CANDIDATE DOSSIER: ZECUSD
**Canonical Key**: `ZECUSD` | **Broker Instrument**: `ZECUSD.p` | **Asset Class**: `Crypto Altcoin`
**Timestamp**: `2026-10-30 01:45:09 IST` (`2026-10-29 20:15:09 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

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
| `16` | `0xb83d...6e36` | `SHORT` | 69,755,971.03 USD | `52,582.52` | `1336.45` | `1290.80` | `3712.88` | 517,943.86 USD | `+0.74%` | `3X Cross` |
| `24` | `0x5b5d...c060` | `SHORT` | 52,571,198.99 USD | `40,727.61` | `1478.36` | `1290.80` | `5183.14` | 7,639,065.21 USD | `+14.53%` | `3X Cross` |
| `41` | `0x7fda...17d1` | `SHORT` | 29,144,028.13 USD | `22,463.41` | `1261.54` | `1290.80` | `2889.63` | -805,492.84 USD | `-2.76%` | `5X Cross` |
| `76` | `0x60b0...991e` | `LONG` | 22,288,528.64 USD | `16,779.74` | `1179.65` | `1290.80` | `890.09` | 2,494,281.63 USD | `+11.19%` | `10X Cross` |
| `85` | `0xbf73...5d58` | `LONG` | 20,824,000.00 USD | `16,000.00` | `1214.30` | `1290.80` | `742.40` | 1,395,167.75 USD | `+6.70%` | `10X Cross` |
| `133` | `0xc36a...105b` | `LONG` | 15,271,404.89 USD | `11,510.82` | `1215.14` | `1290.80` | `933.46` | 1,284,123.87 USD | `+8.41%` | `10X Cross` |
| `170` | `0x8742...8427` | `LONG` | 11,930,288.89 USD | `9,201.21` | `1286.37` | `1290.80` | `698.37` | 94,118.89 USD | `+0.79%` | `10X Cross` |
| `180` | `0x9071...5c0b` | `LONG` | 11,448,017.21 USD | `8,829.94` | `1370.53` | `1290.80` | `579.52` | -653,671.44 USD | `-5.71%` | `2X Cross` |
| `188` | `0xad59...ba81` | `SHORT` | 11,187,557.50 USD | `8,425.00` | `330.91` | `1290.80` | `2140.51` | -8,399,599.73 USD | `-75.08%` | `10X Cross` |
| `200` | `0x9ffd...ce40` | `LONG` | 10,826,944.63 USD | `8,256.02` | `1255.00` | `1290.80` | `576.57` | 465,629.96 USD | `+4.30%` | `5X Cross` |
| `205` | `0xdd53...2b13` | `SHORT` | 10,720,590.95 USD | `8,230.78` | `739.37` | `1290.80` | `8042.30` | -4,634,975.65 USD | `-43.23%` | `3X Cross` |
| `220` | `0x880a...311c` | `SHORT` | 10,195,735.82 USD | `7,707.11` | `1367.50` | `1290.80` | `2307.89` | 343,748.38 USD | `+3.37%` | `10X Cross` |
| `227` | `0xfc66...ca06` | `SHORT` | 10,055,570.14 USD | `7,763.72` | `1319.73` | `1290.80` | `5623.32` | 190,446.70 USD | `+1.89%` | `10X Cross` |
| `267` | `0x2b61...2f6c` | `LONG` | 9,004,980.30 USD | `6,807.00` | `1453.56` | `1290.80` | `633.67` | -889,370.92 USD | `-9.88%` | `10X Cross` |
| `290` | `0x2ae5...83e7` | `LONG` | 8,358,184.80 USD | `6,436.80` | `1391.82` | `1290.80` | `482.34` | -600,707.19 USD | `-7.19%` | `2X Cross` |
| `337` | `0x26b6...9a13` | `LONG` | 7,055,698.41 USD | `5,433.73` | `1282.23` | `1290.80` | `216.67` | 88,395.17 USD | `+1.25%` | `10X Cross` |
| `342` | `0xecb6...2b00` | `SHORT` | 6,991,671.83 USD | `5,393.56` | `1324.05` | `1290.80` | `6348.87` | 149,693.46 USD | `+2.14%` | `5X Cross` |
| `350` | `0x45d2...4029` | `SHORT` | 6,776,805.50 USD | `5,227.00` | `833.44` | `1290.80` | `8344.11` | -2,420,427.53 USD | `-35.72%` | `5X Cross` |
| `363` | `0xea00...a918` | `LONG` | 6,641,000.00 USD | `5,000.00` | `739.16` | `1290.80` | `0.000000` | 2,945,184.89 USD | `+44.35%` | `5X Cross` |
| `380` | `0xdd7a...8830` | `LONG` | 6,452,388.24 USD | `4,860.19` | `897.48` | `1290.80` | `782.37` | 2,090,484.57 USD | `+32.40%` | `10X Cross` |
| `387` | `0xf081...e39e` | `LONG` | 6,237,289.10 USD | `4,717.00` | `1195.70` | `1290.80` | `1200.11` | 597,165.06 USD | `+9.57%` | `10X Cross` |
| `437` | `0x4cae...7c34` | `LONG` | 5,294,965.23 USD | `4,004.36` | `999.34` | `1290.80` | `771.45` | 1,293,237.07 USD | `+24.42%` | `10X Cross` |
| `442` | `0x382b...3e39` | `LONG` | 5,220,936.79 USD | `4,040.66` | `1205.00` | `1290.80` | `0.000000` | 351,956.58 USD | `+6.74%` | `10X Cross` |
| `455` | `0xa61c...66b9` | `LONG` | 5,040,792.00 USD | `3,888.00` | `1148.34` | `1290.80` | `0.000000` | 576,049.86 USD | `+11.43%` | `10X Cross` |
| `468` | `0x9aa5...58af` | `SHORT` | 4,928,666.69 USD | `3,720.31` | `1205.51` | `1290.80` | `3340.12` | -443,779.89 USD | `-9.00%` | `10X Cross` |
| `481` | `0x0153...8052` | `SHORT` | 4,801,347.09 USD | `3,698.18` | `1307.82` | `1290.80` | `2504.70` | 35,223.65 USD | `+0.73%` | `1X Isolated` |
| `500` | `0xd4c1...3d1d` | `SHORT` | 4,495,807.58 USD | `3,471.13` | `1303.00` | `1290.80` | `2777.88` | 27,077.25 USD | `+0.60%` | `10X Cross` |
| `524` | `0xd21d...90f1` | `LONG` | 4,315,675.00 USD | `3,250.00` | `1253.64` | `1290.80` | `875.90` | 241,333.27 USD | `+5.59%` | `4X Isolated` |
| `543` | `0x456f...cdf1` | `LONG` | 4,162,724.90 USD | `3,134.11` | `1268.52` | `1290.80` | `493.27` | 187,035.27 USD | `+4.49%` | `10X Cross` |
| `544` | `0x1338...c48e` | `LONG` | 4,161,849.86 USD | `3,149.43` | `1018.52` | `1290.80` | `820.19` | 954,104.32 USD | `+22.93%` | `4X Isolated` |
| `556` | `0x27c9...d65d` | `SHORT` | 4,090,688.78 USD | `3,147.41` | `1253.73` | `1290.80` | `1818.47` | -144,699.61 USD | `-3.54%` | `10X Cross` |
| `572` | `0xdbe0...d6d5` | `LONG` | 4,006,352.94 USD | `3,085.37` | `422.97` | `1290.80` | `338.51` | 2,701,348.45 USD | `+67.43%` | `3X Isolated` |
| `578` | `0x9c06...0560` | `SHORT` | 3,970,753.38 USD | `2,989.80` | `786.00` | `1290.80` | `2373.04` | -1,620,758.38 USD | `-40.82%` | `10X Cross` |
| `660` | `0x2e30...4cb5` | `SHORT` | 3,512,520.41 USD | `2,705.06` | `1301.01` | `1290.80` | `3006.66` | 6,776.44 USD | `+0.19%` | `2X Cross` |
| `684` | `0xac48...3201` | `LONG` | 3,374,026.46 USD | `2,540.30` | `1393.86` | `1290.80` | `535.95` | -166,802.83 USD | `-4.94%` | `10X Cross` |
| `703` | `0x0871...e927` | `LONG` | 3,307,250.00 USD | `2,500.00` | `1276.50` | `1290.80` | `0.000000` | 116,000.00 USD | `+3.51%` | `10X Cross` |
| `705` | `0xa183...0482` | `LONG` | 3,299,521.40 USD | `2,534.00` | `530.25` | `1290.80` | `444.43` | 1,955,858.68 USD | `+59.28%` | `5X Isolated` |
| `708` | `0x9b86...6e6e` | `LONG` | 3,276,327.67 USD | `2,467.30` | `637.58` | `1290.80` | `889.66` | 1,703,228.07 USD | `+51.99%` | `3X Cross` |
| `711` | `0x325e...9564` | `LONG` | 3,243,726.31 USD | `2,501.91` | `1306.24` | `1290.80` | `0.000000` | -24,367.59 USD | `-0.75%` | `10X Cross` |
| `767` | `0xb2f7...af9f` | `SHORT` | 3,072,388.79 USD | `2,313.72` | `746.63` | `1290.80` | `4182.31` | -1,344,900.04 USD | `-43.77%` | `10X Cross` |
| `783` | `0x634f...6951` | `LONG` | 3,017,319.28 USD | `2,272.42` | `1281.94` | `1290.80` | `1250.04` | 104,218.81 USD | `+3.45%` | `10X Cross` |
| `793` | `0xf48f...10fe` | `LONG` | 2,945,932.87 USD | `2,218.49` | `1517.87` | `1290.80` | `895.75` | -421,453.95 USD | `-14.31%` | `3X Cross` |
| `838` | `0x8de4...b9aa` | `SHORT` | 2,779,115.28 USD | `2,091.29` | `1331.35` | `1290.80` | `1689.83` | 5,124.43 USD | `+0.18%` | `3X Cross` |
| `841` | `0x5bc4...3b0c` | `SHORT` | 2,759,521.37 USD | `2,130.74` | `1089.65` | `1290.80` | `3600.48` | -437,763.80 USD | `-15.86%` | `5X Cross` |
| `844` | `0x4fe2...ac59` | `SHORT` | 2,751,666.43 USD | `2,071.57` | `1478.56` | `1290.80` | `1814.79` | 311,279.78 USD | `+11.31%` | `10X Cross` |
| `864` | `0x668c...ea2e` | `SHORT` | 2,654,200.00 USD | `2,000.00` | `1406.98` | `1290.80` | `2702.50` | 159,763.99 USD | `+6.02%` | `10X Cross` |
| `881` | `0x77ee...2902` | `SHORT` | 2,574,403.09 USD | `1,946.03` | `759.84` | `1290.80` | `5191.36` | -1,095,725.58 USD | `-42.56%` | `10X Cross` |
| `897` | `0x3e2f...b269` | `SHORT` | 2,525,113.81 USD | `1,925.51` | `1134.87` | `1290.80` | `2931.75` | -339,914.96 USD | `-13.46%` | `10X Cross` |
| `901` | `0x4f12...618b` | `SHORT` | 2,518,259.84 USD | `1,896.28` | `1608.30` | `1290.80` | `2116.70` | 531,524.55 USD | `+21.11%` | `3X Cross` |
| `917` | `0xe097...d0fe` | `LONG` | 2,488,202.07 USD | `1,913.56` | `1261.17` | `1290.80` | `0.000000` | 74,875.90 USD | `+3.01%` | `10X Cross` |
| `948` | `0x866d...d6e1` | `LONG` | 2,382,850.71 USD | `1,802.05` | `674.73` | `1290.80` | `87.24` | 1,166,949.40 USD | `+48.97%` | `10X Cross` |
| `981` | `0x2309...a2d9` | `LONG` | 2,318,890.18 USD | `1,750.37` | `1186.09` | `1290.80` | `805.50` | 242,796.07 USD | `+10.47%` | `8X Cross` |
| `997` | `0x4e23...20c3` | `LONG` | 2,271,175.51 USD | `1,759.51` | `1298.31` | `1290.80` | `0.000000` | -13,208.34 USD | `-0.58%` | `4X Cross` |
| `1014` | `0x023a...2355` | `SHORT` | 2,208,510.28 USD | `1,705.15` | `1313.37` | `1290.80` | `6016.18` | 30,985.49 USD | `+1.40%` | `10X Cross` |
| `1019` | `0x2edd...8179` | `SHORT` | 2,203,560.85 USD | `1,701.46` | `1261.58` | `1290.80` | `3027.26` | -57,038.85 USD | `-2.59%` | `10X Cross` |
| `1031` | `0x3e47...aaf6` | `LONG` | 2,170,852.68 USD | `1,636.28` | `1279.54` | `1290.80` | `1037.67` | 77,160.59 USD | `+3.55%` | `10X Cross` |
| `1033` | `0xa271...a3f7` | `LONG` | 2,167,028.47 USD | `1,631.43` | `1190.60` | `1290.80` | `910.29` | 224,646.67 USD | `+10.37%` | `4X Cross` |
| `1041` | `0x7f75...9edf` | `LONG` | 2,132,636.42 USD | `1,605.78` | `1199.97` | `1290.80` | `973.48` | 205,744.53 USD | `+9.65%` | `10X Cross` |
| `1044` | `0x265e...7f70` | `LONG` | 2,127,270.89 USD | `1,601.74` | `1388.09` | `1290.80` | `0.000000` | -96,094.11 USD | `-4.52%` | `3X Cross` |
| `1076` | `0xab59...59b5` | `LONG` | 2,078,588.43 USD | `1,565.32` | `1342.15` | `1290.80` | `791.71` | -22,306.79 USD | `-1.07%` | `10X Cross` |
| `1079` | `0x6646...6de5` | `SHORT` | 2,077,280.00 USD | `1,600.00` | `660.64` | `1290.80` | `4681.91` | -1,020,255.03 USD | `-49.11%` | `10X Cross` |
| `1097` | `0xdf57...93f5` | `LONG` | 2,045,315.27 USD | `1,579.76` | `1218.38` | `1290.80` | `780.13` | 120,559.29 USD | `+5.89%` | `3X Isolated` |
| `1103` | `0xfe7c...b7ae` | `SHORT` | 2,032,486.99 USD | `1,562.49` | `1350.62` | `1290.80` | `6753.06` | 77,842.06 USD | `+3.83%` | `10X Cross` |
| `1142` | `0xcf67...eb24` | `LONG` | 1,992,450.00 USD | `1,500.00` | `887.05` | `1290.80` | `548.99` | 661,878.63 USD | `+33.22%` | `10X Cross` |
| `1193` | `0x039c...0ebd` | `SHORT` | 1,917,530.65 USD | `1,480.49` | `1238.67` | `1290.80` | `3182.52` | -83,699.33 USD | `-4.36%` | `10X Cross` |
| `1241` | `0x71d0...8c26` | `SHORT` | 1,853,644.95 USD | `1,429.73` | `1358.60` | `1290.80` | `6509.29` | 88,783.95 USD | `+4.79%` | `10X Cross` |
| `1255` | `0x11be...8b1d` | `LONG` | 1,826,964.66 USD | `1,375.83` | `1206.55` | `1290.80` | `1134.40` | 166,956.70 USD | `+9.14%` | `10X Isolated` |
| `1260` | `0xfc27...9d9d` | `SHORT` | 1,819,717.90 USD | `1,401.40` | `1317.49` | `1290.80` | `11880.94` | 26,618.78 USD | `+1.46%` | `10X Cross` |
| `1261` | `0x2ab7...c2f8` | `LONG` | 1,818,562.24 USD | `1,400.51` | `813.26` | `1290.80` | `801.26` | 679,580.55 USD | `+37.37%` | `3X Cross` |
| `1310` | `0xdf83...3cff` | `SHORT` | 1,739,275.55 USD | `1,347.44` | `1248.29` | `1290.80` | `1809.51` | -57,276.20 USD | `-3.29%` | `10X Cross` |
| `1334` | `0xef96...9383` | `SHORT` | 1,696,885.13 USD | `1,308.82` | `1249.96` | `1290.80` | `4291.14` | -60,918.71 USD | `-3.59%` | `10X Cross` |
| `1351` | `0xe065...0f85` | `SHORT` | 1,676,746.08 USD | `1,262.61` | `1087.02` | `1290.80` | `1756.35` | -304,269.95 USD | `-18.15%` | `10X Cross` |
| `1416` | `0x7277...0b98` | `SHORT` | 1,608,041.42 USD | `1,234.96` | `1298.48` | `1290.80` | `2384.53` | -4,472.00 USD | `-0.28%` | `10X Cross` |
| `1430` | `0x5975...9abd` | `LONG` | 1,592,040.00 USD | `1,200.00` | `1179.54` | `1290.80` | `376.97` | 176,597.21 USD | `+11.09%` | `5X Cross` |
| `1471` | `0x7a76...b16d` | `LONG` | 1,539,394.63 USD | `1,159.27` | `1358.50` | `1290.80` | `1236.75` | -35,473.88 USD | `-2.30%` | `10X Cross` |
| `1484` | `0x3fc5...c0c1` | `SHORT` | 1,525,128.32 USD | `1,148.44` | `1264.34` | `1290.80` | `3100.54` | -73,114.54 USD | `-4.79%` | `10X Cross` |
| `1503` | `0x69cc...14fd` | `SHORT` | 1,505,935.51 USD | `1,161.36` | `675.33` | `1290.80` | `7994.79` | -721,629.98 USD | `-47.92%` | `10X Cross` |
| `1519` | `0x5f94...4b96` | `LONG` | 1,480,967.03 USD | `1,115.27` | `538.00` | `1290.80` | `0.000000` | 880,949.40 USD | `+59.48%` | `10X Cross` |
| `1530` | `0xe35c...a1d3` | `LONG` | 1,462,247.64 USD | `1,127.06` | `1318.20` | `1290.80` | `694.33` | -23,447.71 USD | `-1.60%` | `2X Isolated` |
| `1534` | `0x71df...a23d` | `SHORT` | 1,452,914.61 USD | `1,098.28` | `513.50` | `1290.80` | `2546.94` | -888,944.42 USD | `-61.18%` | `2X Cross` |
| `1564` | `0xbfc7...80b4` | `SHORT` | 1,424,160.00 USD | `1,075.00` | `558.03` | `1290.80` | `5465.83` | -824,281.27 USD | `-57.88%` | `10X Cross` |
| `1634` | `0x51f6...2b39` | `SHORT` | 1,350,284.18 USD | `1,039.88` | `1302.72` | `1289.50` | `2880.25` | 4,392.63 USD | `+0.33%` | `10X Cross` |
| `1646` | `0xe282...df29` | `LONG` | 1,327,600.00 USD | `1,000.00` | `420.99` | `1289.50` | `107.04` | 906,613.14 USD | `+68.29%` | `10X Cross` |
| `1665` | `0x123d...3bff` | `SHORT` | 1,307,973.81 USD | `1,008.15` | `489.25` | `1289.50` | `4227.51` | -814,739.74 USD | `-62.29%` | `10X Cross` |
| `1671` | `0x17f0...094f` | `LONG` | 1,301,539.89 USD | `984.30` | `1287.23` | `1289.50` | `536.76` | 34,519.73 USD | `+2.65%` | `5X Cross` |
| `1673` | `0x266b...efcb` | `LONG` | 1,300,300.00 USD | `1,000.00` | `826.11` | `1289.50` | `176.42` | 474,187.07 USD | `+36.47%` | `10X Cross` |
| `1677` | `0xb5ff...d912` | `LONG` | 1,298,500.00 USD | `1,000.00` | `1141.93` | `1289.50` | `400.45` | 156,569.70 USD | `+12.06%` | `2X Cross` |
| `1684` | `0x0748...d4b2` | `LONG` | 1,296,600.00 USD | `1,000.00` | `1334.09` | `1289.50` | `0.000000` | -37,488.30 USD | `-2.89%` | `7X Cross` |
| `1767` | `0x757d...94ba` | `LONG` | 1,203,887.50 USD | `925.00` | `1558.31` | `1289.50` | `0.000000` | -237,553.08 USD | `-19.73%` | `10X Cross` |
| `1809` | `0x2847...d47b` | `LONG` | 1,163,442.35 USD | `895.30` | `1238.73` | `1289.50` | `0.000000` | 54,404.74 USD | `+4.68%` | `5X Cross` |
| `1814` | `0xcf0a...856f` | `LONG` | 1,156,712.97 USD | `871.15` | `1292.19` | `1289.50` | `938.47` | 31,018.12 USD | `+2.68%` | `4X Cross` |
| `1833` | `0xdf95...7d72` | `SHORT` | 1,142,594.23 USD | `880.68` | `1073.96` | `1289.50` | `42611.07` | -196,776.90 USD | `-17.22%` | `10X Cross` |
| `1834` | `0xf096...7553` | `SHORT` | 1,141,778.61 USD | `881.07` | `1240.34` | `1289.50` | `3594.86` | -48,948.53 USD | `-4.29%` | `10X Cross` |
| `1854` | `0x7d0f...ea35` | `LONG` | 1,129,565.00 USD | `850.00` | `1317.57` | `1289.50` | `1255.65` | 9,629.42 USD | `+0.85%` | `10X Cross` |
| `1899` | `0x601c...4f54` | `SHORT` | 1,089,439.12 USD | `824.42` | `615.11` | `1289.50` | `2973.85` | -582,326.37 USD | `-53.45%` | `5X Cross` |
| `1929` | `0xae55...2236` | `LONG` | 1,059,849.85 USD | `817.47` | `1467.80` | `1289.50` | `0.000000` | -140,031.36 USD | `-13.21%` | `10X Cross` |
| `1942` | `0x71b1...79c8` | `LONG` | 1,052,457.16 USD | `812.52` | `1231.55` | `1289.50` | `732.12` | 51,801.70 USD | `+4.92%` | `10X Cross` |
| `1946` | `0xabdb...84ac` | `LONG` | 1,051,480.51 USD | `793.69` | `711.79` | `1289.50` | `664.33` | 486,540.15 USD | `+46.27%` | `3X Cross` |
| `1947` | `0x0f02...5384` | `LONG` | 1,050,142.89 USD | `800.78` | `1290.36` | `1289.50` | `294.39` | 16,848.82 USD | `+1.60%` | `3X Cross` |
| `1957` | `0x9b0f...db40` | `LONG` | 1,038,800.00 USD | `800.00` | `1268.86` | `1289.50` | `778.37` | 23,710.24 USD | `+2.28%` | `10X Cross` |
| `1978` | `0x3205...40bb` | `SHORT` | 1,030,175.70 USD | `794.95` | `1327.42` | `1289.50` | `3033.55` | 25,052.98 USD | `+2.43%` | `10X Cross` |
| `1991` | `0xfdf8...e381` | `LONG` | 1,023,141.95 USD | `790.01` | `1337.72` | `1289.50` | `557.87` | -33,667.73 USD | `-3.29%` | `10X Cross` |

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
  * Current Rate: `55.18K` | Last 24h: `33.19K` | Last 3d: `283.86K` | Last 7d: `777.60K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0036%` | **USDT OKX** | `0.0100%` |
| **USDT Bybit** | `0.0100%` | **USDT KuCoin** | `0.0100%` |
| **USDT MEXC** | `0.0036%` | **USDT BingX** | `0.0036%` |
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
| `5m` | -1,410,000.00 USD | -4,550,000.00 USD | **`DISTRIBUTION`** |
| `15m` | -1,220,000.00 USD | -4,640,000.00 USD | **`DISTRIBUTION`** |
| `30m` | -1,200,000.00 USD | -1,630,000.00 USD | **`DISTRIBUTION`** |
| `1h` | -925,060.00 USD | 2,660,000.00 USD | **`ACCUMULATION`** |
| `2h` | -872,130.00 USD | -6,820,000.00 USD | **`DISTRIBUTION`** |
| `4h` | 8,110,000.00 USD | 8,790,000.00 USD | **`ACCUMULATION`** |
| `6h` | 26,920,000.00 USD | 84,850,000.00 USD | **`ACCUMULATION`** |
| `8h` | 28,680,000.00 USD | 95,960,000.00 USD | **`ACCUMULATION`** |
| `12h` | 26,200,000.00 USD | 111,250,000.00 USD | **`ACCUMULATION`** |
| `24h` | 9,010,000.00 USD | 52,280,000.00 USD | **`ACCUMULATION`** |
| `1w` | 48,520,000.00 USD | 257,660,000.00 USD | **`ACCUMULATION`** |
| `30d` | 69,520,000.00 USD | -503,410,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-1.41M` | 15m=`-1.22M` | 1h=`-925.06K` | 24h=`+9.01M`
* Futures Capital Netflows: 5m=`-4.55M` | 15m=`-4.64M` | 1h=`+2.66M` | 24h=`+52.28M`
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
