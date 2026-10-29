# 🏛️ SOVEREIGN CANDIDATE DOSSIER: ZECUSD
**Canonical Key**: `ZECUSD` | **Broker Instrument**: `ZECUSD.p` | **Asset Class**: `Crypto Altcoin`
**Timestamp**: `2026-10-29 23:01:08 IST` (`2026-10-29 17:31:08 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `1346.65` | **Live Ask Quote**: `1347.58` | **Mid Price**: `1347.12`
- **Spread Points**: `93.00` | **Spread BPS**: `6.90 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `1347.12` | VWAP Z-Score: `+0.00` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `3.37` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `50.00` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `1356.54` | Lower -3.00σ Band: `1337.69`
  * Upper +2.51σ Band: `1354.52` | Lower -2.51σ Band: `1339.71`
  * Upper +2.01σ Band: `1352.77` | Lower -2.01σ Band: `1341.46`
  * Upper +2.00σ Band: `1352.50` | Lower -2.00σ Band: `1341.73`
  * Upper +1.28σ Band: `1350.89` | Lower -1.28σ Band: `1343.34`
  * Upper +1.00σ Band: `1349.81` | Lower -1.00σ Band: `1344.42`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`1347.12` | EMA-20=`1347.12` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`1347.12` (Slope: `+0.0000`) | EMA-100=`1347.12`
  * Institutional Anchors: EMA-144=`1347.12` | EMA-200=`1347.12` (Slope: `+0.0000`) | EMA-233=`1347.12`
- **Range Boundaries**: 24H High=`1360.59` | 24H Low=`1333.64` | Weekly High=`1374.06` | Weekly Low=`1320.17`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `1300.48` (Distance: `+3.56%`)
  * Point of Control (POC) = `1247.20` (Distance: `+7.98%`)
  * Value Area Low (VAL) = `1230.55` (Distance: `+9.45%`)
  * Auction Positioning: `ABOVE_VALUE (Imbalance)` | Session Bias: **`BULLISH (Above Pivot)`** | Market Regime: `TREND_UP_ACCEPTANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`1320.44` | POC=`1312.10` | VAL=`1285.78`
  * Prior Day Extremes: PDH=`1328.99` | PDL=`1263.19` | PDC=`1296.46`
  * Monday Range Blueprint: High=`1267.53` | Mid=`1222.14` | Low=`1176.75`
  * Developing Weekly Value Area: Weekly VAH=`1293.21` | Weekly POC=`1239.01` | Weekly VAL=`1195.06`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`1318.68` | Low=`1230.00`
  * London Session (08:00-16:00 UTC): High=`1276.13` | Low=`1233.52`
  * New York Session (13:00-21:00 UTC): High=`1396.49` | Low=`1250.65`
  * Initial Balance (First Hour): IB High=`1255.79` | IB Low=`1245.43`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `1341.73` - `1352.50`
  * Optimal Trade Entry (OTE 0.705): `1349.81`
  * Structural Invalidation Anchor (0.786): `1357.89`

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
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-29 22:54:46 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `16` | `0xb83d...6e36` | `SHORT` | 70,954,852.49 USD | `52,582.52` | `1336.45` | `1349.50` | `3637.68` | -680,937.59 USD | `-0.96%` | `3X Cross` |
| `23` | `0x5b5d...c060` | `SHORT` | 54,957,836.93 USD | `40,727.61` | `1478.36` | `1349.50` | `4886.21` | 5,252,427.26 USD | `+9.56%` | `3X Cross` |
| `42` | `0x7fda...17d1` | `SHORT` | 30,251,213.54 USD | `22,418.27` | `1261.11` | `1349.50` | `2954.78` | -1,979,416.89 USD | `-6.54%` | `5X Cross` |
| `80` | `0x60b0...991e` | `LONG` | 22,628,318.38 USD | `16,779.74` | `1179.65` | `1349.50` | `874.77` | 2,834,071.36 USD | `+12.52%` | `10X Cross` |
| `85` | `0xbf73...5d58` | `LONG` | 21,587,200.00 USD | `16,000.00` | `1214.30` | `1349.50` | `708.85` | 2,158,367.75 USD | `+10.00%` | `10X Cross` |
| `131` | `0xc36a...105b` | `LONG` | 15,530,398.34 USD | `11,510.82` | `1215.14` | `1349.50` | `924.47` | 1,543,117.32 USD | `+9.94%` | `10X Cross` |
| `170` | `0x8742...8427` | `LONG` | 12,412,432.29 USD | `9,201.21` | `1286.37` | `1349.50` | `698.32` | 576,262.30 USD | `+4.64%` | `10X Cross` |
| `193` | `0xad59...ba81` | `SHORT` | 11,368,695.00 USD | `8,425.00` | `330.91` | `1349.50` | `2138.63` | -8,580,737.23 USD | `-75.48%` | `10X Cross` |
| `201` | `0xdd53...2b13` | `SHORT` | 11,117,883.34 USD | `8,237.91` | `739.37` | `1349.50` | `7659.68` | -5,026,996.30 USD | `-45.22%` | `3X Cross` |
| `206` | `0x9ffd...ce40` | `LONG` | 10,908,581.28 USD | `8,087.02` | `1250.06` | `1349.50` | `555.43` | 799,283.87 USD | `+7.33%` | `5X Cross` |
| `208` | `0xfc66...ca06` | `SHORT` | 10,795,334.94 USD | `8,000.10` | `1319.34` | `1349.50` | `5426.00` | -240,486.12 USD | `-2.23%` | `10X Cross` |
| `219` | `0x880a...311c` | `SHORT` | 10,401,515.66 USD | `7,707.11` | `1367.50` | `1349.50` | `2300.72` | 137,968.55 USD | `+1.33%` | `10X Cross` |
| `267` | `0x2b61...2f6c` | `LONG` | 9,184,004.40 USD | `6,807.00` | `1453.56` | `1349.50` | `654.32` | -710,346.82 USD | `-7.73%` | `10X Cross` |
| `284` | `0x2ae5...83e7` | `LONG` | 8,683,886.88 USD | `6,436.80` | `1391.82` | `1349.50` | `0.000000` | -275,005.11 USD | `-3.17%` | `2X Cross` |
| `318` | `0xecb6...2b00` | `SHORT` | 7,915,189.07 USD | `5,865.71` | `1323.84` | `1349.50` | `6425.02` | -149,943.48 USD | `-1.89%` | `5X Cross` |
| `329` | `0x26b6...9a13` | `LONG` | 7,331,731.89 USD | `5,433.73` | `1282.23` | `1349.50` | `197.51` | 364,428.65 USD | `+4.97%` | `10X Cross` |
| `339` | `0x45d2...4029` | `SHORT` | 7,051,745.70 USD | `5,227.00` | `833.44` | `1349.50` | `7796.07` | -2,695,367.73 USD | `-38.22%` | `5X Cross` |
| `358` | `0x469e...58a5` | `SHORT` | 6,747,000.00 USD | `5,000.00` | `1190.36` | `1349.50` | `1817.86` | -795,215.10 USD | `-11.79%` | `10X Cross` |
| `359` | `0xea00...a918` | `LONG` | 6,742,750.00 USD | `5,000.00` | `739.16` | `1349.50` | `0.000000` | 3,046,934.89 USD | `+45.19%` | `5X Cross` |
| `376` | `0xdd7a...8830` | `LONG` | 6,558,195.55 USD | `4,860.19` | `897.48` | `1349.50` | `791.29` | 2,196,291.88 USD | `+33.49%` | `10X Cross` |
| `384` | `0xf081...e39e` | `LONG` | 6,364,648.10 USD | `4,717.00` | `1195.70` | `1349.50` | `1200.06` | 724,524.06 USD | `+11.38%` | `10X Cross` |
| `443` | `0x4cae...7c34` | `LONG` | 5,403,082.95 USD | `4,004.36` | `999.34` | `1349.50` | `686.15` | 1,401,354.79 USD | `+25.94%` | `10X Cross` |
| `449` | `0x382b...3e39` | `LONG` | 5,309,393.88 USD | `3,934.05` | `1166.42` | `1349.50` | `0.000000` | 720,651.23 USD | `+13.57%` | `10X Cross` |
| `452` | `0xa61c...66b9` | `LONG` | 5,246,351.34 USD | `3,888.00` | `1148.34` | `1349.50` | `0.000000` | 781,609.20 USD | `+14.90%` | `10X Cross` |
| `477` | `0x9aa5...58af` | `SHORT` | 5,020,186.31 USD | `3,720.31` | `1205.51` | `1349.50` | `3246.99` | -535,299.51 USD | `-10.66%` | `10X Cross` |
| `479` | `0x0153...8052` | `SHORT` | 4,990,693.91 USD | `3,698.18` | `1307.82` | `1349.50` | `2504.65` | -154,123.16 USD | `-3.09%` | `1X Isolated` |
| `511` | `0xd4c1...3d1d` | `SHORT` | 4,676,323.51 USD | `3,464.97` | `1302.89` | `1349.50` | `2607.10` | -161,865.46 USD | `-3.46%` | `10X Cross` |
| `535` | `0xd21d...90f1` | `LONG` | 4,385,550.00 USD | `3,250.00` | `1253.64` | `1349.50` | `875.85` | 311,208.27 USD | `+7.10%` | `4X Isolated` |
| `552` | `0x1338...c48e` | `LONG` | 4,249,525.90 USD | `3,149.43` | `1018.52` | `1349.50` | `820.14` | 1,041,780.36 USD | `+24.52%` | `4X Isolated` |
| `562` | `0x456f...cdf1` | `LONG` | 4,199,333.62 USD | `3,111.77` | `1267.78` | `1349.50` | `486.74` | 254,295.29 USD | `+6.06%` | `10X Cross` |
| `567` | `0xdbe0...d6d5` | `LONG` | 4,163,706.81 USD | `3,085.37` | `422.97` | `1349.50` | `338.46` | 2,858,702.32 USD | `+68.66%` | `3X Isolated` |
| `591` | `0x9c06...0560` | `SHORT` | 4,033,838.16 USD | `2,989.80` | `786.00` | `1349.50` | `2343.96` | -1,683,843.16 USD | `-41.74%` | `10X Cross` |
| `628` | `0x27c9...d65d` | `SHORT` | 3,816,223.69 USD | `2,827.71` | `1245.67` | `1349.50` | `1827.29` | -293,823.81 USD | `-7.70%` | `10X Cross` |
| `689` | `0xac48...3201` | `LONG` | 3,428,340.61 USD | `2,540.30` | `1393.86` | `1349.50` | `531.06` | -112,488.68 USD | `-3.28%` | `10X Cross` |
| `694` | `0xa183...0482` | `LONG` | 3,418,366.00 USD | `2,534.00` | `530.25` | `1349.50` | `444.38` | 2,074,703.28 USD | `+60.69%` | `5X Isolated` |
| `699` | `0x325e...9564` | `LONG` | 3,376,077.35 USD | `2,501.91` | `1306.24` | `1349.50` | `0.000000` | 107,983.45 USD | `+3.20%` | `10X Cross` |
| `701` | `0x0871...e927` | `LONG` | 3,373,000.00 USD | `2,500.00` | `1276.50` | `1349.50` | `0.000000` | 181,750.00 USD | `+5.39%` | `10X Cross` |
| `710` | `0x9b86...6e6e` | `LONG` | 3,329,374.62 USD | `2,467.30` | `637.58` | `1349.50` | `889.61` | 1,756,275.02 USD | `+52.75%` | `3X Cross` |
| `762` | `0xb2f7...af9f` | `SHORT` | 3,122,133.77 USD | `2,313.72` | `746.63` | `1349.50` | `4151.65` | -1,394,645.02 USD | `-44.67%` | `10X Cross` |
| `790` | `0x2e30...4cb5` | `SHORT` | 3,017,034.80 USD | `2,236.00` | `1295.46` | `1349.50` | `3341.20` | -120,376.54 USD | `-3.99%` | `2X Cross` |
| `796` | `0xf48f...10fe` | `LONG` | 2,993,630.41 USD | `2,218.49` | `1517.87` | `1349.50` | `866.92` | -373,756.42 USD | `-12.49%` | `3X Cross` |
| `825` | `0x5bc4...3b0c` | `SHORT` | 2,874,368.26 USD | `2,130.74` | `1089.65` | `1349.50` | `3535.41` | -552,610.68 USD | `-19.23%` | `5X Cross` |
| `851` | `0x4fe2...ac59` | `SHORT` | 2,794,340.77 USD | `2,071.57` | `1478.56` | `1349.50` | `1803.36` | 268,605.44 USD | `+9.61%` | `10X Cross` |
| `853` | `0x4e23...20c3` | `LONG` | 2,787,347.63 USD | `2,065.62` | `1302.47` | `1349.50` | `0.000000` | 96,936.88 USD | `+3.48%` | `4X Cross` |
| `861` | `0x71d0...8c26` | `SHORT` | 2,728,256.89 USD | `2,021.53` | `1362.26` | `1349.50` | `5074.14` | 25,587.63 USD | `+0.94%` | `10X Cross` |
| `866` | `0x668c...ea2e` | `SHORT` | 2,698,800.00 USD | `2,000.00` | `1409.16` | `1349.50` | `2701.36` | 119,522.04 USD | `+4.43%` | `10X Cross` |
| `867` | `0x362a...1d9f` | `SHORT` | 2,697,561.04 USD | `1,999.23` | `1382.50` | `1349.50` | `1677.36` | 66,376.36 USD | `+2.46%` | `5X Cross` |
| `888` | `0x77ee...2902` | `SHORT` | 2,625,583.68 USD | `1,946.03` | `759.84` | `1349.50` | `5287.70` | -1,146,906.17 USD | `-43.68%` | `10X Cross` |
| `897` | `0x3e2f...b269` | `SHORT` | 2,598,668.30 USD | `1,925.51` | `1134.87` | `1349.50` | `2931.71` | -413,469.44 USD | `-15.91%` | `10X Cross` |
| `904` | `0xe097...d0fe` | `LONG` | 2,582,540.58 USD | `1,913.56` | `1261.17` | `1349.50` | `0.000000` | 169,214.41 USD | `+6.55%` | `10X Cross` |
| `912` | `0x4f12...618b` | `SHORT` | 2,557,892.09 USD | `1,896.28` | `1608.30` | `1349.50` | `2116.67` | 491,892.30 USD | `+19.23%` | `3X Cross` |
| `953` | `0x866d...d6e1` | `LONG` | 2,431,506.06 USD | `1,802.05` | `674.73` | `1349.50` | `54.66` | 1,215,604.75 USD | `+49.99%` | `10X Cross` |
| `978` | `0x2309...a2d9` | `LONG` | 2,361,949.28 USD | `1,750.37` | `1186.09` | `1349.50` | `799.66` | 285,855.17 USD | `+12.10%` | `8X Cross` |
| `1000` | `0x023a...2355` | `SHORT` | 2,314,966.02 USD | `1,715.59` | `1313.12` | `1349.50` | `6289.27` | -62,187.15 USD | `-2.69%` | `10X Cross` |
| `1006` | `0x2edd...8179` | `SHORT` | 2,302,508.21 USD | `1,706.32` | `1261.18` | `1349.50` | `2922.15` | -150,531.20 USD | `-6.54%` | `10X Cross` |
| `1031` | `0x265e...7f70` | `LONG` | 2,228,032.09 USD | `1,651.74` | `1388.09` | `1349.50` | `0.000000` | -64,737.60 USD | `-2.91%` | `3X Cross` |
| `1042` | `0xa271...a3f7` | `LONG` | 2,200,635.93 USD | `1,631.43` | `1190.60` | `1349.50` | `910.24` | 258,254.12 USD | `+11.74%` | `4X Cross` |
| `1049` | `0x7f75...9edf` | `LONG` | 2,166,518.38 USD | `1,605.78` | `1199.97` | `1349.50` | `975.07` | 239,626.48 USD | `+11.06%` | `10X Cross` |
| `1052` | `0x6646...6de5` | `SHORT` | 2,159,360.00 USD | `1,600.00` | `660.64` | `1349.50` | `4929.77` | -1,102,335.03 USD | `-51.05%` | `10X Cross` |
| `1063` | `0xdf57...93f5` | `LONG` | 2,132,044.10 USD | `1,579.76` | `1218.38` | `1349.50` | `780.08` | 207,288.12 USD | `+9.72%` | `3X Isolated` |
| `1072` | `0xab59...59b5` | `LONG` | 2,112,399.34 USD | `1,565.32` | `1342.15` | `1349.50` | `781.02` | 11,504.12 USD | `+0.54%` | `10X Cross` |
| `1076` | `0xfe7c...b7ae` | `SHORT` | 2,106,253.24 USD | `1,560.65` | `1350.64` | `1349.50` | `6275.49` | 1,620.51 USD | `+0.08%` | `10X Cross` |
| `1086` | `0x634f...6951` | `LONG` | 2,095,618.20 USD | `1,553.00` | `1263.46` | `1349.50` | `1184.28` | 133,468.62 USD | `+6.37%` | `10X Cross` |
| `1099` | `0x3e47...aaf6` | `LONG` | 2,073,209.86 USD | `1,536.28` | `1277.06` | `1349.50` | `1011.63` | 111,287.77 USD | `+5.37%` | `10X Cross` |
| `1127` | `0xcf67...eb24` | `LONG` | 2,023,350.00 USD | `1,500.00` | `887.05` | `1349.50` | `482.05` | 692,778.63 USD | `+34.24%` | `10X Cross` |
| `1147` | `0x039c...0ebd` | `SHORT` | 1,997,773.21 USD | `1,480.49` | `1238.67` | `1349.50` | `3111.66` | -163,941.89 USD | `-8.21%` | `10X Cross` |
| `1207` | `0x7a76...b16d` | `LONG` | 1,910,291.60 USD | `1,415.66` | `1362.09` | `1349.50` | `1256.25` | -17,963.65 USD | `-0.94%` | `10X Cross` |
| `1228` | `0x2ab7...c2f8` | `LONG` | 1,889,708.14 USD | `1,400.51` | `813.26` | `1349.50` | `793.18` | 750,726.46 USD | `+39.73%` | `3X Cross` |
| `1253` | `0x11be...8b1d` | `LONG` | 1,856,682.58 USD | `1,375.83` | `1206.55` | `1349.50` | `1134.36` | 196,674.63 USD | `+10.59%` | `10X Isolated` |
| `1303` | `0xef96...9383` | `SHORT` | 1,765,467.30 USD | `1,308.82` | `1249.96` | `1349.50` | `4068.33` | -129,500.88 USD | `-7.34%` | `10X Cross` |
| `1310` | `0xfc27...9d9d` | `SHORT` | 1,757,256.71 USD | `1,302.54` | `1315.39` | `1349.50` | `11743.46` | -43,914.69 USD | `-2.50%` | `10X Cross` |
| `1330` | `0xdf83...3cff` | `SHORT` | 1,720,066.69 USD | `1,274.69` | `1243.56` | `1349.50` | `1881.47` | -134,907.16 USD | `-7.84%` | `10X Cross` |
| `1350` | `0xe065...0f85` | `SHORT` | 1,703,134.63 USD | `1,262.61` | `1087.02` | `1349.50` | `1606.10` | -330,658.50 USD | `-19.41%` | `10X Cross` |
| `1362` | `0x5323...b23c` | `SHORT` | 1,685,228.26 USD | `1,249.15` | `1359.55` | `1349.50` | `5892.23` | 13,057.07 USD | `+0.77%` | `5X Cross` |
| `1372` | `0x7277...0b98` | `SHORT` | 1,666,702.02 USD | `1,234.96` | `1298.48` | `1349.50` | `2336.96` | -63,132.60 USD | `-3.79%` | `10X Cross` |
| `1423` | `0x5975...9abd` | `LONG` | 1,619,400.00 USD | `1,200.00` | `1179.54` | `1349.50` | `279.77` | 203,957.21 USD | `+12.59%` | `5X Cross` |
| `1469` | `0x69cc...14fd` | `SHORT` | 1,567,371.46 USD | `1,161.36` | `675.33` | `1349.50` | `7783.91` | -783,065.93 USD | `-49.96%` | `10X Cross` |
| `1484` | `0x3fc5...c0c1` | `SHORT` | 1,549,819.78 USD | `1,148.44` | `1264.34` | `1349.50` | `2991.85` | -97,806.00 USD | `-6.31%` | `10X Cross` |
| `1519` | `0x5f94...4b96` | `LONG` | 1,504,945.34 USD | `1,115.27` | `538.00` | `1349.50` | `0.000000` | 904,927.70 USD | `+60.13%` | `10X Cross` |
| `1531` | `0x9546...181c` | `LONG` | 1,485,131.90 USD | `1,100.75` | `1348.55` | `1349.50` | `0.000000` | 710.65 USD | `+0.05%` | `10X Cross` |
| `1534` | `0x71df...a23d` | `SHORT` | 1,481,799.38 USD | `1,098.28` | `513.50` | `1349.50` | `2544.32` | -917,829.19 USD | `-61.94%` | `2X Cross` |
| `1565` | `0xbfc7...80b4` | `SHORT` | 1,450,605.00 USD | `1,075.00` | `558.03` | `1349.50` | `5178.49` | -850,726.27 USD | `-58.65%` | `10X Cross` |
| `1613` | `0x51f6...2b39` | `SHORT` | 1,402,798.12 USD | `1,039.88` | `1302.72` | `1349.50` | `2843.85` | -48,121.31 USD | `-3.43%` | `10X Cross` |
| `1646` | `0x123d...3bff` | `SHORT` | 1,359,972.77 USD | `1,007.70` | `488.87` | `1349.50` | `4122.99` | -867,337.65 USD | `-63.78%` | `10X Cross` |
| `1654` | `0x266b...efcb` | `LONG` | 1,349,600.00 USD | `1,000.00` | `826.11` | `1349.50` | `144.68` | 523,487.07 USD | `+38.79%` | `10X Cross` |
| `1655` | `0xe282...df29` | `LONG` | 1,349,370.20 USD | `1,000.00` | `420.99` | `1349.50` | `85.61` | 928,383.34 USD | `+68.80%` | `10X Cross` |
| `1657` | `0xb5ff...d912` | `LONG` | 1,349,100.00 USD | `1,000.00` | `1141.93` | `1349.50` | `400.40` | 207,169.70 USD | `+15.36%` | `2X Cross` |
| `1659` | `0x0748...d4b2` | `LONG` | 1,349,000.00 USD | `1,000.00` | `1334.09` | `1349.50` | `0.000000` | 14,911.70 USD | `+1.11%` | `7X Cross` |
| `1665` | `0xe35c...a1d3` | `LONG` | 1,335,282.78 USD | `989.56` | `1313.36` | `1349.50` | `691.81` | 35,638.24 USD | `+2.67%` | `2X Isolated` |
| `1676` | `0x17f0...094f` | `LONG` | 1,328,115.99 USD | `984.30` | `1287.23` | `1349.50` | `536.71` | 61,095.83 USD | `+4.60%` | `5X Cross` |
| `1754` | `0x757d...94ba` | `LONG` | 1,247,825.00 USD | `925.00` | `1558.31` | `1349.50` | `0.000000` | -193,615.58 USD | `-15.52%` | `10X Cross` |
| `1761` | `0x5d90...eea3` | `LONG` | 1,242,334.57 USD | `920.93` | `1288.61` | `1349.50` | `904.51` | 55,617.32 USD | `+4.48%` | `3X Isolated` |
| `1765` | `0x3205...40bb` | `SHORT` | 1,236,088.02 USD | `915.96` | `1344.67` | `1349.50` | `2742.16` | -4,423.66 USD | `-0.36%` | `10X Cross` |
| `1820` | `0xf096...7553` | `SHORT` | 1,188,915.86 USD | `881.07` | `1240.34` | `1349.50` | `3456.26` | -96,085.77 USD | `-8.08%` | `10X Cross` |
| `1822` | `0xdf95...7d72` | `SHORT` | 1,187,526.54 USD | `879.91` | `1073.66` | `1349.50` | `40496.46` | -242,802.49 USD | `-20.45%` | `10X Cross` |
| `1835` | `0xcf0a...856f` | `LONG` | 1,175,529.81 USD | `871.15` | `1292.19` | `1349.50` | `938.42` | 49,834.96 USD | `+4.24%` | `4X Cross` |
| `1850` | `0x2847...d47b` | `LONG` | 1,163,431.56 USD | `862.44` | `1235.38` | `1349.50` | `0.000000` | 97,993.75 USD | `+8.42%` | `5X Cross` |
| `1871` | `0x7d0f...ea35` | `LONG` | 1,146,820.00 USD | `850.00` | `1317.57` | `1349.50` | `1275.59` | 26,884.42 USD | `+2.34%` | `10X Cross` |
| `1906` | `0x601c...4f54` | `SHORT` | 1,112,389.91 USD | `824.42` | `615.11` | `1349.50` | `2901.45` | -605,277.15 USD | `-54.41%` | `5X Cross` |
| `1914` | `0xae55...2236` | `LONG` | 1,102,848.78 USD | `817.47` | `1467.80` | `1349.50` | `0.000000` | -97,032.44 USD | `-8.80%` | `10X Cross` |
| `1923` | `0x71b1...79c8` | `LONG` | 1,096,414.49 USD | `812.52` | `1231.55` | `1349.50` | `661.70` | 95,759.03 USD | `+8.73%` | `10X Cross` |
| `1937` | `0x0f02...5384` | `LONG` | 1,080,572.53 USD | `800.78` | `1290.36` | `1349.50` | `285.89` | 47,278.46 USD | `+4.38%` | `3X Cross` |
| `1941` | `0x9b0f...db40` | `LONG` | 1,079,600.00 USD | `800.00` | `1268.86` | `1349.50` | `772.49` | 64,510.24 USD | `+5.98%` | `10X Cross` |
| `1942` | `0xea0f...4e73` | `LONG` | 1,079,496.16 USD | `800.00` | `1364.27` | `1349.50` | `572.76` | -11,922.52 USD | `-1.10%` | `10X Cross` |
| `1959` | `0xabdb...84ac` | `LONG` | 1,070,846.55 USD | `793.69` | `711.79` | `1349.50` | `664.28` | 505,906.19 USD | `+47.24%` | `3X Cross` |
| `1969` | `0xfdf8...e381` | `LONG` | 1,065,723.49 USD | `790.01` | `1337.72` | `1349.50` | `220.54` | 8,913.80 USD | `+0.84%` | `10X Cross` |
| `2013` | `0x0c1f...1d39` | `SHORT` | 1,029,578.71 USD | `762.99` | `1299.17` | `1349.50` | `4641.18` | -38,327.62 USD | `-3.72%` | `10X Cross` |
| `2016` | `0xf6f3...47f8` | `SHORT` | 1,027,814.87 USD | `761.57` | `1253.10` | `1349.50` | `2311.32` | -73,491.88 USD | `-7.15%` | `5X Cross` |
| `2020` | `0x389a...e76b` | `LONG` | 1,025,795.44 USD | `760.13` | `1266.20` | `1349.50` | `366.54` | 63,322.01 USD | `+6.17%` | `10X Cross` |
| `2036` | `0xadd1...5e0d` | `LONG` | 1,012,736.50 USD | `750.62` | `1195.15` | `1349.50` | `0.000000` | 115,635.41 USD | `+11.42%` | `10X Cross` |
| `2038` | `0xe83b...3ca8` | `LONG` | 1,012,050.00 USD | `750.00` | `1346.44` | `1349.50` | `0.000000` | 2,222.36 USD | `+0.22%` | `10X Cross` |
| `2050` | `0xd6e1...f256` | `SHORT` | 1,006,927.77 USD | `746.37` | `1368.65` | `1349.50` | `2024.32` | 14,588.02 USD | `+1.45%` | `10X Cross` |
| `2058` | `0x87a7...9fa2` | `SHORT` | 1,004,810.71 USD | `744.58` | `1464.55` | `1349.50` | `1714.72` | 85,666.03 USD | `+8.53%` | `10X Cross` |
| `2065` | `0x8923...1bac` | `LONG` | 1,001,335.76 USD | `742.06` | `1239.64` | `1349.50` | `701.54` | 81,449.23 USD | `+8.13%` | `5X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `1304.60` | 10,019.33 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Long: 10.02K USD at 1304.6000 USD [API] | `2026-10-27 16:27:21` |
| `ANNOUNCEMENT` | `INFO` | `1289.60` | 10,407.07 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Long: 10.41K USD at 1289.6000 USD [API] | `2026-10-27 15:20:59` |
| `ANNOUNCEMENT` | `INFO` | `1297.10` | 194.56 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Long: 0.19K USD at 1297.1000 USD [API] | `2026-10-27 15:46:39` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`1404.15` (Vol: 3,000,000.00 USD, Dist: `+3.89%`) | Long MP=`1287.60` (Vol: 2,300,000.00 USD, Dist: `--4.73%`)
  * 48H Horizon: Short MP=`1404.15` (Vol: 3,000,000.00 USD, Dist: `+3.89%`) | Long MP=`1287.60` (Vol: 2,300,000.00 USD, Dist: `--4.73%`)
  * 3D Horizon: Short MP=`1404.42` (Vol: 3,000,000.00 USD, Dist: `+3.91%`) | Long MP=`0.000000` (Vol: 0.00 USD, Dist: `-0.00%`)
  * 7D Horizon: Short MP=`1404.10` (Vol: 3,000,000.00 USD, Dist: `+3.89%`) | Long MP=`1200.46` (Vol: 3,000,000.00 USD, Dist: `--11.18%`)
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
  * Current Rate: `86.41K` | Last 24h: `32.07K` | Last 3d: `282.84K` | Last 7d: `777.72K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0081%` | **USDT OKX** | `0.0083%` |
| **USDT Bybit** | `0.0100%` | **USDT KuCoin** | `0.0100%` |
| **USDT MEXC** | `0.0080%` | **USDT BingX** | `0.0041%` |
| **USDT Gate** | `0.0100%` | **USDT Bitget** | `0.0056%` |
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
| `0:00 UTC` | `1320.15` | `1314.27` | `1320.15` | `1324.95` | `1296.75` | 56,796,886.08 USD | 33,062,545.27 USD | 23,734,340.81 USD | 9,328,204.46 USD | `+16.42%` | `18B / 3S` |
| `5:00 UTC` | `1317.75` | `1318.00` | `1317.75` | `1324.05` | `1313.25` | 29,849,949.75 USD | 16,298,218.14 USD | 13,551,731.61 USD | 2,746,486.54 USD | `+9.20%` | `4B / 2S` |
| `0:00 UTC` | `1345.05` | `1339.86` | `1345.05` | `1353.45` | `1318.65` | 81,702,422.73 USD | 46,151,799.06 USD | 35,550,623.66 USD | 10,601,175.40 USD | `+12.98%` | `23B / 1S` |
| `5:00 UTC` | `1360.05` | `1349.51` | `1360.05` | `1362.15` | `1334.25` | 65,905,391.58 USD | 39,286,823.07 USD | 26,618,568.52 USD | 12,668,254.55 USD | `+19.22%` | `19B / 3S` |
| `0:00 UTC` | `1369.95` | `1375.81` | `1369.95` | `1397.55` | `1350.75` | 159,915,504.01 USD | 87,974,917.65 USD | 71,940,586.35 USD | 16,034,331.30 USD | `+10.03%` | `21B / 3S` |
| `5:00 UTC` | `1359.75` | `1358.32` | `1359.75` | `1373.25` | `1346.25` | 77,512,400.13 USD | 36,921,415.88 USD | 40,590,984.25 USD | -3,669,568.36 USD | `-4.73%` | `4B / 13S` |
| `0:00 UTC` | `1353.15` | `1350.71` | `1353.15` | `1361.25` | `1341.75` | 52,010,841.39 USD | 26,247,439.78 USD | 25,763,401.61 USD | 484,038.17 USD | `+0.93%` | `5B / 3S` |
| `5:00 UTC` | `1343.25` | `1344.85` | `1343.25` | `1353.45` | `1340.25` | 26,552,172.39 USD | 11,915,117.49 USD | 14,637,054.90 USD | -2,721,937.40 USD | `-10.25%` | `0B / 9S` |
| `0:00 UTC` | `1342.95` | `1346.21` | `1342.95` | `1354.05` | `1340.25` | 27,005,669.33 USD | 14,153,013.83 USD | 12,852,655.50 USD | 1,300,358.33 USD | `+4.82%` | `5B / 3S` |
| `5:00 UTC` | `1349.85` | `1349.54` | `1349.85` | `1354.95` | `1344.45` | 12,634,407.63 USD | 7,335,095.76 USD | 5,299,311.86 USD | 2,035,783.90 USD | `+16.11%` | `5B / 2S` |

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
| `5m` | 183,230.00 USD | 2,230,000.00 USD | **`ACCUMULATION`** |
| `15m` | 4,760,000.00 USD | 10,200,000.00 USD | **`ACCUMULATION`** |
| `30m` | 6,100,000.00 USD | 8,760,000.00 USD | **`ACCUMULATION`** |
| `1h` | 5,290,000.00 USD | 5,530,000.00 USD | **`ACCUMULATION`** |
| `2h` | 17,170,000.00 USD | 71,090,000.00 USD | **`ACCUMULATION`** |
| `4h` | 28,180,000.00 USD | 107,300,000.00 USD | **`ACCUMULATION`** |
| `6h` | 32,570,000.00 USD | 118,470,000.00 USD | **`ACCUMULATION`** |
| `8h` | 29,580,000.00 USD | 132,420,000.00 USD | **`ACCUMULATION`** |
| `12h` | 27,680,000.00 USD | 127,030,000.00 USD | **`ACCUMULATION`** |
| `24h` | 17,850,000.00 USD | 128,760,000.00 USD | **`ACCUMULATION`** |
| `1w` | 54,750,000.00 USD | 286,820,000.00 USD | **`ACCUMULATION`** |
| `30d` | 71,070,000.00 USD | -485,780,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+183.23K` | 15m=`+4.76M` | 1h=`+5.29M` | 24h=`+17.85M`
* Futures Capital Netflows: 5m=`+2.23M` | 15m=`+10.20M` | 1h=`+5.53M` | 24h=`+128.76M`
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
  * `2026-10-29 22:45:14 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:06:14 IST`: [fxstreet.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:50:14 IST`: [ForexFactory] - (Sentiment: `Neutral`)
  * `2026-10-29 22:50:14 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-29 22:50:14 IST`: [youtube.com/bankofcanadaofficial] - (Sentiment: `Neutral`)
  * `2026-10-29 22:49:14 IST`: [notayesmanseconomics.wordpress.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:49:14 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:49:14 IST`: [breakingthenews.net] - (Sentiment: `Neutral`)
  * `2026-10-29 19:51:14 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-29 19:51:14 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-29 19:51:14 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-29 19:51:14 IST`: [youtube.com/ecbeuro] - (Sentiment: `Neutral`)
  * `2026-10-29 18:51:14 IST`: [ecb.europa.eu] - (Sentiment: `Neutral`)
  * `2026-10-29 18:51:14 IST`: [zerohedge.com] - (Sentiment: `Neutral`)
  * `2026-10-29 18:51:14 IST`: [dol.gov] - (Sentiment: `Neutral`)


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
  * Spread-Padded Stop Loss: `1225.11` (Risk Distance: `5.44` pts)
  * +2.5R Take Profit: `1244.14`
  * Mathematical Lot Sizing: **`1.83 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `1300.48` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `1305.92` (Risk Distance: `5.44` pts)
  * +2.5R Take Profit: `1286.89`
  * Mathematical Lot Sizing: **`1.83 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`1357.89`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
