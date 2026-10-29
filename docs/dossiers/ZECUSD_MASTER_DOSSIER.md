# 🏛️ SOVEREIGN CANDIDATE DOSSIER: ZECUSD
**Canonical Key**: `ZECUSD` | **Broker Instrument**: `ZECUSD.p` | **Asset Class**: `Crypto Altcoin`
**Timestamp**: `2026-10-30 03:16:11 IST` (`2026-10-29 21:46:11 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `1274.33` | **Live Ask Quote**: `1275.43` | **Mid Price**: `1274.88`
- **Spread Points**: `110.00` | **Spread BPS**: `8.63 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `1281.33` | VWAP Z-Score: `-0.17` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `22.50` (Volatility Regime: `HIGH_EXPANSION`)
  * 14-Period RSI: `41.60` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `1395.91` | Lower -3.00σ Band: `1166.74`
  * Upper +2.51σ Band: `1377.20` | Lower -2.51σ Band: `1185.46`
  * Upper +2.01σ Band: `1358.10` | Lower -2.01σ Band: `1204.56`
  * Upper +2.00σ Band: `1357.72` | Lower -2.00σ Band: `1204.94`
  * Upper +1.28σ Band: `1330.22` | Lower -1.28σ Band: `1232.44`
  * Upper +1.00σ Band: `1319.52` | Lower -1.00σ Band: `1243.13`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`1281.56` | EMA-20=`1298.04` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`1296.39` (Slope: `+0.0000`) | EMA-100=`1289.21`
  * Institutional Anchors: EMA-144=`1284.95` | EMA-200=`1280.81` (Slope: `+0.1394`) | EMA-233=`1279.70`
- **Range Boundaries**: 24H High=`1396.49` | 24H Low=`1206.89` | Weekly High=`1396.49` | Weekly Low=`1206.89`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `1295.83` (Distance: `-1.65%`)
  * Point of Control (POC) = `1273.58` (Distance: `+0.07%`)
  * Value Area Low (VAL) = `1264.27` (Distance: `+0.81%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`1309.91` | POC=`1246.71` | VAL=`1230.27`
  * Prior Day Extremes: PDH=`1396.49` | PDL=`1206.89` | PDC=`1244.38`
  * Monday Range Blueprint: High=`1267.53` | Mid=`1222.14` | Low=`1176.75`
  * Developing Weekly Value Area: Weekly VAH=`1296.14` | Weekly POC=`1239.01` | Weekly VAL=`1196.53`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`1296.00` | Low=`1246.17`
  * London Session (08:00-16:00 UTC): High=`1279.98` | Low=`1269.78`
  * New York Session (13:00-21:00 UTC): High=`1282.53` | Low=`1267.23`
  * Initial Balance (First Hour): IB High=`1278.70` | IB Low=`1271.06`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `1269.78` - `1279.98`
  * Optimal Trade Entry (OTE 0.705): `1277.43`
  * Structural Invalidation Anchor (0.786): `1285.08`

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
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 03:15:37 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `16` | `0xb83d...6e36` | `SHORT` | 67,666,699.11 USD | `52,385.77` | `1336.45` | `1290.80` | `3886.06` | 2,344,269.23 USD | `+3.46%` | `3X Cross` |
| `24` | `0x5b5d...c060` | `SHORT` | 51,839,821.93 USD | `40,133.02` | `1478.36` | `1290.80` | `5323.04` | 7,491,421.34 USD | `+14.45%` | `3X Cross` |
| `42` | `0x7fda...17d1` | `SHORT` | 28,748,039.29 USD | `22,271.49` | `1262.05` | `1290.80` | `2909.95` | -640,396.41 USD | `-2.23%` | `5X Cross` |
| `79` | `0x60b0...991e` | `LONG` | 21,617,339.04 USD | `16,779.74` | `1179.65` | `1290.80` | `915.11` | 1,823,092.03 USD | `+8.43%` | `10X Cross` |
| `137` | `0xc36a...105b` | `LONG` | 14,812,123.18 USD | `11,510.82` | `1215.14` | `1290.80` | `948.75` | 824,842.15 USD | `+5.57%` | `10X Cross` |
| `155` | `0x9071...5c0b` | `LONG` | 13,586,235.22 USD | `10,517.29` | `1353.83` | `1290.80` | `0.000000` | -652,383.65 USD | `-4.80%` | `1X Cross` |
| `173` | `0x8742...8427` | `LONG` | 11,885,202.96 USD | `9,201.21` | `1286.37` | `1290.80` | `700.64` | 49,032.96 USD | `+0.41%` | `10X Cross` |
| `198` | `0x58b2...11f3` | `LONG` | 10,951,225.52 USD | `8,463.08` | `1257.17` | `1290.80` | `460.85` | 311,736.33 USD | `+2.85%` | `10X Cross` |
| `202` | `0xad59...ba81` | `SHORT` | 10,850,557.50 USD | `8,425.00` | `330.91` | `1290.80` | `2141.14` | -8,062,599.73 USD | `-74.31%` | `10X Cross` |
| `205` | `0x9ffd...ce40` | `LONG` | 10,734,774.26 USD | `8,306.72` | `1256.02` | `1290.80` | `588.85` | 301,373.48 USD | `+2.81%` | `5X Cross` |
| `207` | `0xdd53...2b13` | `SHORT` | 10,548,413.48 USD | `8,168.20` | `739.52` | `1290.80` | `8324.94` | -4,507,903.29 USD | `-42.74%` | `3X Cross` |
| `214` | `0xbf73...5d58` | `LONG` | 10,333,600.00 USD | `8,000.00` | `1291.41` | `1290.80` | `225.44` | 2,343.24 USD | `+0.02%` | `10X Cross` |
| `222` | `0x880a...311c` | `SHORT` | 9,960,668.96 USD | `7,707.11` | `1367.50` | `1290.80` | `2260.51` | 578,815.24 USD | `+5.81%` | `10X Cross` |
| `271` | `0xfc66...ca06` | `SHORT` | 8,793,864.32 USD | `6,935.14` | `1319.65` | `1290.80` | `6154.97` | 358,111.62 USD | `+4.07%` | `10X Cross` |
| `279` | `0x2b61...2f6c` | `LONG` | 8,651,016.30 USD | `6,807.00` | `1453.56` | `1290.80` | `585.58` | -1,243,334.92 USD | `-14.37%` | `10X Cross` |
| `287` | `0x2ae5...83e7` | `LONG` | 8,315,058.24 USD | `6,436.80` | `1391.82` | `1290.80` | `0.000000` | -643,833.75 USD | `-7.74%` | `1X Cross` |
| `331` | `0x26b6...9a13` | `LONG` | 7,017,662.29 USD | `5,433.73` | `1282.23` | `1290.80` | `205.80` | 50,359.06 USD | `+0.72%` | `10X Cross` |
| `344` | `0x45d2...4029` | `SHORT` | 6,752,238.60 USD | `5,227.00` | `833.44` | `1290.80` | `8415.05` | -2,395,860.63 USD | `-35.48%` | `5X Cross` |
| `372` | `0xea00...a918` | `LONG` | 6,441,500.00 USD | `5,000.00` | `739.16` | `1290.80` | `0.000000` | 2,745,684.89 USD | `+42.62%` | `5X Cross` |
| `385` | `0xdd7a...8830` | `LONG` | 6,258,466.66 USD | `4,860.19` | `897.48` | `1290.80` | `777.73` | 1,896,562.99 USD | `+30.30%` | `10X Cross` |
| `390` | `0xecb6...2b00` | `SHORT` | 6,136,140.43 USD | `4,750.07` | `1306.59` | `1290.80` | `6390.19` | 70,250.99 USD | `+1.14%` | `5X Cross` |
| `396` | `0x5323...b23c` | `SHORT` | 5,984,399.26 USD | `4,634.04` | `1287.73` | `1290.80` | `2401.94` | -17,001.88 USD | `-0.28%` | `5X Cross` |
| `444` | `0x4cae...7c34` | `LONG` | 5,088,340.25 USD | `4,004.36` | `999.34` | `1290.80` | `860.03` | 1,086,612.10 USD | `+21.35%` | `10X Cross` |
| `449` | `0xa61c...66b9` | `LONG` | 5,028,739.20 USD | `3,888.00` | `1148.34` | `1290.80` | `0.000000` | 563,997.06 USD | `+11.22%` | `10X Cross` |
| `471` | `0x9aa5...58af` | `SHORT` | 4,788,411.00 USD | `3,720.31` | `1205.51` | `1290.80` | `3545.59` | -303,524.20 USD | `-6.34%` | `10X Cross` |
| `476` | `0x0153...8052` | `SHORT` | 4,760,297.30 USD | `3,698.18` | `1307.82` | `1290.80` | `2504.72` | 76,273.45 USD | `+1.60%` | `1X Isolated` |
| `514` | `0x382b...3e39` | `LONG` | 4,387,349.05 USD | `3,394.73` | `1210.63` | `1290.80` | `0.000000` | 277,583.13 USD | `+6.33%` | `10X Cross` |
| `537` | `0xd21d...90f1` | `LONG` | 4,185,675.00 USD | `3,250.00` | `1253.64` | `1290.80` | `875.91` | 111,333.27 USD | `+2.66%` | `4X Isolated` |
| `558` | `0x456f...cdf1` | `LONG` | 4,037,673.91 USD | `3,134.11` | `1268.47` | `1290.80` | `493.61` | 62,164.45 USD | `+1.54%` | `10X Cross` |
| `560` | `0x1338...c48e` | `LONG` | 4,031,270.40 USD | `3,149.43` | `1018.52` | `1290.80` | `820.21` | 823,524.86 USD | `+20.43%` | `4X Isolated` |
| `579` | `0xdbe0...d6d5` | `LONG` | 3,971,488.26 USD | `3,085.37` | `422.97` | `1290.80` | `338.52` | 2,666,483.77 USD | `+67.14%` | `3X Isolated` |
| `585` | `0x27c9...d65d` | `SHORT` | 3,934,061.52 USD | `3,047.77` | `1254.41` | `1290.80` | `1712.66` | -110,904.94 USD | `-2.82%` | `10X Cross` |
| `594` | `0x325e...9564` | `LONG` | 3,882,670.39 USD | `3,001.91` | `1301.41` | `1290.80` | `102.94` | -24,038.81 USD | `-0.62%` | `10X Cross` |
| `599` | `0x9c06...0560` | `SHORT` | 3,846,676.68 USD | `2,989.80` | `786.00` | `1290.80` | `2499.36` | -1,496,681.68 USD | `-38.91%` | `10X Cross` |
| `637` | `0x2e30...4cb5` | `SHORT` | 3,645,155.46 USD | `2,819.80` | `1299.29` | `1290.80` | `2948.86` | 18,590.71 USD | `+0.51%` | `2X Cross` |
| `647` | `0xd4c1...3d1d` | `SHORT` | 3,564,342.81 USD | `2,759.42` | `1302.70` | `1290.80` | `2944.13` | 30,342.42 USD | `+0.85%` | `10X Cross` |
| `684` | `0xac48...3201` | `LONG` | 3,371,422.13 USD | `2,610.48` | `1391.07` | `1290.80` | `530.95` | -259,945.86 USD | `-7.71%` | `10X Cross` |
| `705` | `0xa183...0482` | `LONG` | 3,273,167.80 USD | `2,534.00` | `530.25` | `1290.80` | `444.45` | 1,929,505.08 USD | `+58.95%` | `5X Isolated` |
| `717` | `0x413c...886c` | `LONG` | 3,220,750.00 USD | `2,500.00` | `1268.64` | `1290.80` | `0.000000` | 49,138.36 USD | `+1.53%` | `10X Cross` |
| `727` | `0x9b86...6e6e` | `LONG` | 3,177,635.67 USD | `2,467.30` | `637.58` | `1290.80` | `889.67` | 1,604,536.07 USD | `+50.49%` | `3X Cross` |
| `734` | `0x0871...e927` | `LONG` | 3,147,000.00 USD | `2,500.00` | `1276.50` | `1290.80` | `0.000000` | -44,250.00 USD | `-1.41%` | `10X Cross` |
| `785` | `0xb2f7...af9f` | `SHORT` | 2,979,839.99 USD | `2,313.72` | `746.63` | `1290.80` | `4321.59` | -1,252,351.24 USD | `-42.03%` | `10X Cross` |
| `810` | `0xf48f...10fe` | `LONG` | 2,857,193.27 USD | `2,218.49` | `1517.87` | `1290.80` | `955.58` | -510,193.55 USD | `-17.86%` | `3X Cross` |
| `841` | `0x5bc4...3b0c` | `SHORT` | 2,751,637.64 USD | `2,130.74` | `1089.65` | `1290.80` | `3642.96` | -429,880.06 USD | `-15.62%` | `5X Cross` |
| `845` | `0x71d0...8c26` | `SHORT` | 2,727,379.65 USD | `2,108.69` | `1289.73` | `1290.80` | `4620.67` | -7,748.65 USD | `-0.28%` | `10X Cross` |
| `853` | `0x8de4...b9aa` | `SHORT` | 2,702,574.07 USD | `2,091.29` | `1331.35` | `1290.80` | `1689.84` | 81,665.64 USD | `+3.02%` | `3X Cross` |
| `867` | `0x4fe2...ac59` | `SHORT` | 2,666,317.75 USD | `2,071.57` | `1478.56` | `1290.80` | `1806.08` | 396,628.47 USD | `+14.88%` | `10X Cross` |
| `891` | `0x9a99...d21a` | `LONG` | 2,574,200.00 USD | `2,000.00` | `1278.44` | `1290.80` | `0.000000` | 17,326.33 USD | `+0.67%` | `10X Cross` |
| `925` | `0x3e2f...b269` | `SHORT` | 2,486,603.61 USD | `1,925.51` | `1134.87` | `1290.80` | `2931.77` | -301,404.76 USD | `-12.12%` | `10X Cross` |
| `929` | `0xe097...d0fe` | `LONG` | 2,474,424.44 USD | `1,913.56` | `1261.17` | `1290.80` | `0.000000` | 61,098.27 USD | `+2.47%` | `10X Cross` |
| `930` | `0x77ee...2902` | `SHORT` | 2,473,209.53 USD | `1,946.03` | `759.84` | `1290.80` | `5334.71` | -994,532.02 USD | `-40.21%` | `10X Cross` |
| `939` | `0x4f12...618b` | `SHORT` | 2,450,562.64 USD | `1,896.28` | `1608.30` | `1290.80` | `2116.73` | 599,221.74 USD | `+24.45%` | `3X Cross` |
| `1003` | `0x866d...d6e1` | `LONG` | 2,268,055.26 USD | `1,802.05` | `674.73` | `1290.80` | `206.96` | 1,052,153.95 USD | `+46.39%` | `10X Cross` |
| `1010` | `0x2309...a2d9` | `LONG` | 2,252,901.23 USD | `1,750.37` | `1186.09` | `1290.80` | `811.64` | 176,807.12 USD | `+7.85%` | `8X Cross` |
| `1029` | `0x2edd...8179` | `SHORT` | 2,201,172.79 USD | `1,701.85` | `1261.58` | `1290.80` | `2992.14` | -54,153.94 USD | `-2.46%` | `10X Cross` |
| `1032` | `0x023a...2355` | `SHORT` | 2,194,097.89 USD | `1,696.38` | `1313.00` | `1290.80` | `5728.69` | 33,249.40 USD | `+1.52%` | `10X Cross` |
| `1057` | `0xfe7c...b7ae` | `SHORT` | 2,119,174.49 USD | `1,640.99` | `1347.05` | `1290.80` | `6711.17` | 91,314.70 USD | `+4.31%` | `10X Cross` |
| `1059` | `0x3e47...aaf6` | `LONG` | 2,114,237.39 USD | `1,636.28` | `1278.38` | `1290.80` | `1040.73` | 22,445.60 USD | `+1.06%` | `10X Cross` |
| `1068` | `0xa271...a3f7` | `LONG` | 2,099,813.55 USD | `1,631.43` | `1190.60` | `1290.80` | `910.31` | 157,431.75 USD | `+7.50%` | `4X Cross` |
| `1084` | `0x7f75...9edf` | `LONG` | 2,065,996.55 USD | `1,605.78` | `1199.97` | `1290.80` | `976.17` | 139,104.66 USD | `+6.73%` | `10X Cross` |
| `1087` | `0x265e...7f70` | `LONG` | 2,061,599.55 USD | `1,601.74` | `1388.09` | `1290.80` | `0.000000` | -161,765.45 USD | `-7.85%` | `3X Cross` |
| `1089` | `0x6646...6de5` | `SHORT` | 2,060,000.00 USD | `1,600.00` | `660.64` | `1290.80` | `4551.99` | -1,002,975.03 USD | `-48.69%` | `10X Cross` |
| `1098` | `0xdf57...93f5` | `LONG` | 2,039,154.21 USD | `1,579.76` | `1218.38` | `1290.80` | `780.15` | 114,398.23 USD | `+5.61%` | `3X Isolated` |
| `1113` | `0xab59...59b5` | `LONG` | 2,022,549.97 USD | `1,565.32` | `1342.15` | `1290.80` | `813.20` | -78,345.25 USD | `-3.87%` | `10X Cross` |
| `1179` | `0xcf67...eb24` | `LONG` | 1,930,650.00 USD | `1,500.00` | `887.05` | `1290.80` | `613.95` | 600,078.63 USD | `+31.08%` | `10X Cross` |
| `1180` | `0x668c...ea2e` | `SHORT` | 1,930,650.00 USD | `1,500.00` | `1406.98` | `1290.80` | `3198.62` | 179,822.99 USD | `+9.31%` | `10X Cross` |
| `1189` | `0xb695...a92d` | `LONG` | 1,915,287.23 USD | `1,483.00` | `1249.80` | `1290.80` | `0.000000` | 61,828.38 USD | `+3.23%` | `10X Cross` |
| `1262` | `0x2ab7...c2f8` | `LONG` | 1,810,999.48 USD | `1,400.51` | `813.26` | `1290.80` | `793.08` | 672,017.80 USD | `+37.11%` | `3X Cross` |
| `1290` | `0x11be...8b1d` | `LONG` | 1,772,481.79 USD | `1,375.83` | `1206.55` | `1290.80` | `1134.43` | 112,473.83 USD | `+6.35%` | `10X Isolated` |
| `1389` | `0xe065...0f85` | `SHORT` | 1,625,105.33 USD | `1,262.61` | `1087.02` | `1290.80` | `1801.78` | -252,629.20 USD | `-15.55%` | `10X Cross` |
| `1393` | `0x3205...40bb` | `SHORT` | 1,616,753.63 USD | `1,250.97` | `1266.02` | `1290.80` | `2399.09` | -33,004.04 USD | `-2.04%` | `10X Cross` |
| `1415` | `0x7277...0b98` | `SHORT` | 1,594,086.37 USD | `1,234.96` | `1298.48` | `1290.80` | `2405.76` | 9,483.05 USD | `+0.59%` | `10X Cross` |
| `1434` | `0x039c...0ebd` | `SHORT` | 1,582,533.22 USD | `1,225.44` | `1238.80` | `1290.80` | `3635.74` | -64,453.02 USD | `-4.07%` | `10X Cross` |
| `1442` | `0x38f9...cb04` | `SHORT` | 1,571,510.28 USD | `1,217.47` | `1269.33` | `1290.80` | `1949.53` | -26,133.22 USD | `-1.66%` | `10X Cross` |
| `1460` | `0x5975...9abd` | `LONG` | 1,550,520.00 USD | `1,200.00` | `1179.54` | `1290.80` | `382.59` | 135,077.21 USD | `+8.71%` | `5X Cross` |
| `1498` | `0x69cc...14fd` | `SHORT` | 1,499,083.49 USD | `1,161.36` | `675.33` | `1290.80` | `7830.64` | -714,777.96 USD | `-47.68%` | `10X Cross` |
| `1510` | `0x3fc5...c0c1` | `SHORT` | 1,484,243.86 USD | `1,148.44` | `1264.34` | `1290.80` | `2946.18` | -32,230.08 USD | `-2.17%` | `10X Cross` |
| `1540` | `0xe35c...a1d3` | `LONG` | 1,457,739.40 USD | `1,127.06` | `1318.20` | `1290.80` | `694.35` | -27,955.95 USD | `-1.92%` | `2X Isolated` |
| `1545` | `0x2847...d47b` | `LONG` | 1,448,037.22 USD | `1,121.21` | `1233.48` | `1290.80` | `0.000000` | 65,047.82 USD | `+4.49%` | `5X Cross` |
| `1550` | `0x5f94...4b96` | `LONG` | 1,441,040.37 USD | `1,115.27` | `538.00` | `1290.80` | `0.000000` | 841,022.73 USD | `+58.36%` | `10X Cross` |
| `1555` | `0xfc27...9d9d` | `SHORT` | 1,436,005.12 USD | `1,112.32` | `1315.10` | `1290.80` | `15529.80` | 26,806.64 USD | `+1.87%` | `10X Cross` |
| `1556` | `0xdf83...3cff` | `SHORT` | 1,435,951.96 USD | `1,111.59` | `1254.37` | `1290.80` | `1828.65` | -41,609.54 USD | `-2.90%` | `10X Cross` |
| `1571` | `0x266b...efcb` | `LONG` | 1,422,410.00 USD | `1,100.00` | `863.84` | `1290.80` | `263.97` | 472,185.24 USD | `+33.20%` | `10X Cross` |
| `1593` | `0xbfc7...80b4` | `SHORT` | 1,391,050.00 USD | `1,075.00` | `558.03` | `1290.80` | `5095.86` | -791,171.27 USD | `-56.88%` | `10X Cross` |
| `1603` | `0x71df...a23d` | `SHORT` | 1,382,514.86 USD | `1,098.28` | `513.50` | `1290.80` | `2548.89` | -818,544.67 USD | `-59.21%` | `2X Cross` |
| `1627` | `0x51f6...2b39` | `SHORT` | 1,356,880.07 USD | `1,049.08` | `1302.21` | `1290.80` | `2763.11` | 9,245.30 USD | `+0.68%` | `10X Cross` |
| `1666` | `0x123d...3bff` | `SHORT` | 1,304,142.37 USD | `1,009.32` | `490.16` | `1290.80` | `4323.72` | -809,416.50 USD | `-62.07%` | `10X Cross` |
| `1678` | `0xe282...df29` | `LONG` | 1,293,400.00 USD | `1,000.00` | `420.99` | `1290.80` | `151.84` | 872,413.14 USD | `+67.45%` | `10X Cross` |
| `1681` | `0xb5ff...d912` | `LONG` | 1,291,000.00 USD | `1,000.00` | `1280.79` | `1290.80` | `452.78` | 10,212.56 USD | `+0.79%` | `2X Cross` |
| `1718` | `0x17f0...094f` | `LONG` | 1,250,750.01 USD | `984.30` | `1287.23` | `1290.80` | `536.78` | -16,270.15 USD | `-1.30%` | `5X Cross` |
| `1768` | `0x757d...94ba` | `LONG` | 1,194,545.00 USD | `925.00` | `1558.31` | `1290.80` | `0.000000` | -246,895.58 USD | `-20.67%` | `10X Cross` |
| `1808` | `0xb911...5525` | `LONG` | 1,159,470.00 USD | `900.00` | `1294.82` | `1290.80` | `1070.30` | -5,867.82 USD | `-0.51%` | `10X Cross` |
| `1853` | `0xcf0a...856f` | `LONG` | 1,125,525.80 USD | `871.15` | `1292.19` | `1290.80` | `982.36` | -169.05 USD | `-0.02%` | `4X Cross` |
| `1873` | `0xdf95...7d72` | `SHORT` | 1,107,615.16 USD | `857.42` | `1074.32` | `1290.80` | `44570.34` | -186,473.73 USD | `-16.84%` | `10X Cross` |
| `1930` | `0xae55...2236` | `LONG` | 1,056,007.75 USD | `817.47` | `1467.80` | `1290.80` | `0.000000` | -143,873.47 USD | `-13.62%` | `10X Cross` |
| `1945` | `0x601c...4f54` | `SHORT` | 1,048,167.59 USD | `824.42` | `615.11` | `1290.80` | `3013.26` | -541,054.84 USD | `-51.62%` | `5X Cross` |
| `1960` | `0x9b0f...db40` | `LONG` | 1,036,640.00 USD | `800.00` | `1268.86` | `1290.80` | `785.40` | 21,550.24 USD | `+2.08%` | `10X Cross` |
| `1962` | `0x0f02...5384` | `LONG` | 1,034,928.07 USD | `800.78` | `1290.36` | `1290.80` | `285.74` | 1,634.00 USD | `+0.16%` | `3X Cross` |
| `1974` | `0xef96...9383` | `SHORT` | 1,026,307.32 USD | `794.54` | `1252.23` | `1290.80` | `6445.69` | -31,363.46 USD | `-3.06%` | `10X Cross` |
| `1990` | `0xabdb...84ac` | `LONG` | 1,015,843.83 USD | `793.69` | `711.79` | `1290.80` | `664.35` | 450,903.47 USD | `+44.39%` | `3X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `1092.10` | 8,889.69 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Long: 8.89K USD at 1092.1000 USD [API] | `2026-10-18 14:31:53` |
| `ANNOUNCEMENT` | `INFO` | `1131.00` | 5,553.21 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 5.55K USD at 1131.0000 USD [API] | `2026-10-24 14:16:46` |
| `ANNOUNCEMENT` | `INFO` | `1351.00` | 13.51 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Long: 0.01K USD at 1351.0000 USD [API] | `2026-10-05 21:05:42` |
| `ANNOUNCEMENT` | `INFO` | `1183.40` | 3,928.89 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 3.93K USD at 1183.4000 USD [API] | `2026-10-20 13:59:40` |
| `ANNOUNCEMENT` | `INFO` | `1183.40` | 23.67 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 0.02K USD at 1183.4000 USD [API] | `2026-10-20 13:59:40` |
| `ANNOUNCEMENT` | `INFO` | `1183.40` | 11.83 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 0.01K USD at 1183.4000 USD [API] | `2026-10-20 13:59:40` |
| `ANNOUNCEMENT` | `INFO` | `1183.40` | 3,136.01 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 3.14K USD at 1183.4000 USD [API] | `2026-10-20 13:59:40` |
| `ANNOUNCEMENT` | `INFO` | `1248.70` | 3,671.18 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 3.67K USD at 1248.7000 USD [API] | `2026-10-14 00:30:06` |
| `ANNOUNCEMENT` | `INFO` | `1248.60` | 74.92 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 0.07K USD at 1248.6000 USD [API] | `2026-10-14 00:30:06` |
| `ANNOUNCEMENT` | `INFO` | `1314.50` | 302.34 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 0.30K USD at 1314.5000 USD [API] | `2026-10-12 04:36:03` |
| `ANNOUNCEMENT` | `INFO` | `1314.50` | 3,641.16 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 3.64K USD at 1314.5000 USD [API] | `2026-10-12 04:36:03` |
| `ANNOUNCEMENT` | `INFO` | `1284.20` | 1,887.77 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 1.89K USD at 1284.2000 USD [API] | `2026-10-11 16:30:00` |
| `ANNOUNCEMENT` | `INFO` | `1284.20` | 89.89 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 0.09K USD at 1284.2000 USD [API] | `2026-10-11 16:30:00` |


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
| `5m` | `BALANCED` | 0.00 USD | 1,750.00 USD | 1,750.00 USD | 1,750.00 USD | `1` | `2026-10-29 21:40:00 UTC - 2026-10-29 21:45:00 UTC` |
| `15m` | `BALANCED` | 0.00 USD | 1,750.00 USD | 1,750.00 USD | 1,750.00 USD | `1` | `2026-10-29 21:30:00 UTC - 2026-10-29 21:45:00 UTC` |
| `1h` | `BALANCED` | 0.00 USD | 1,750.00 USD | 1,750.00 USD | 1,750.00 USD | `1` | `2026-10-29 21:00:00 UTC - 2026-10-29 22:00:00 UTC` |
| `4h` | `BALANCED` | 0.00 USD | 1,750.00 USD | 1,750.00 USD | 1,750.00 USD | `1` | `2026-10-29 20:00:00 UTC - 2026-10-30 00:00:00 UTC` |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `0 USD` | Total OI Tokens: `-`
  * 1h OI Change: `0.00%` | 4h OI Change: `0.00%` | 24h OI Change: `0.00%`
  * Exchange Breakdown: Binance=`-` | Bybit=`-` | OKX=`-` | Hyperliquid=`-`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `5.25K` | Last 24h: `33.19K` | Last 3d: `283.86K` | Last 7d: `777.60K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `-0.0019%` | **USDT OKX** | `-0.0000%` |
| **USDT Bybit** | `0.0100%` | **USDT KuCoin** | `-0.0052%` |
| **USDT MEXC** | `-0.0020%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `-0.0076%` | **USDT Bitget** | `0.0100%` |
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
| `5:00 UTC` | `1322.85` | `1320.89` | `1322.85` | `1324.95` | `1316.85` | 7,868,027.33 USD | 4,223,932.72 USD | 3,644,094.61 USD | 579,838.11 USD | `+7.37%` | `3B / 0S` |
| `0:00 UTC` | `1324.95` | `1324.41` | `1324.95` | `1327.05` | `1319.85` | 12,000,472.36 USD | 6,714,467.49 USD | 5,286,004.87 USD | 1,428,462.62 USD | `+11.90%` | `2B / 1S` |
| `5:00 UTC` | `1325.25` | `1325.38` | `1325.25` | `1330.65` | `1320.75` | 11,021,893.68 USD | 5,577,839.59 USD | 5,444,054.10 USD | 133,785.49 USD | `+1.21%` | `3B / 1S` |
| `0:00 UTC` | `1294.05` | `1302.04` | `1294.05` | `1328.55` | `1286.25` | 68,949,402.59 USD | 35,232,633.05 USD | 33,716,769.55 USD | 1,515,863.50 USD | `+2.20%` | `6B / 24S` |
| `5:00 UTC` | `1306.05` | `1306.88` | `1306.05` | `1312.05` | `1300.05` | 17,712,248.68 USD | 9,074,345.66 USD | 8,637,903.02 USD | 436,442.64 USD | `+2.46%` | `3B / 5S` |
| `0:00 UTC` | `1249.20` | `1269.32` | `1249.20` | `1308.60` | `1241.40` | 130,590,816.99 USD | 58,796,845.15 USD | 71,793,971.84 USD | -12,997,126.69 USD | `-9.95%` | `4B / 19S` |
| `5:00 UTC` | `1229.25` | `1237.79` | `1229.25` | `1264.35` | `1206.75` | 149,162,484.89 USD | 77,012,548.38 USD | 72,149,936.51 USD | 4,862,611.87 USD | `+3.26%` | `9B / 11S` |
| `0:00 UTC` | `1249.95` | `1248.07` | `1249.95` | `1259.85` | `1233.15` | 61,152,789.32 USD | 32,267,997.87 USD | 28,884,791.45 USD | 3,383,206.41 USD | `+5.53%` | `6B / 4S` |
| `5:00 UTC` | `1273.95` | `1271.85` | `1273.95` | `1286.25` | `1253.25` | 67,607,862.35 USD | 37,234,359.13 USD | 30,373,503.22 USD | 6,860,855.91 USD | `+10.15%` | `6B / 2S` |
| `0:00 UTC` | `1294.65` | `1289.33` | `1294.65` | `1297.05` | `1275.45` | 39,424,944.92 USD | 22,644,577.69 USD | 16,780,367.23 USD | 5,864,210.46 USD | `+14.87%` | `12B / 0S` |

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
| `5m` | -1,010,000.00 USD | 3,360,000.00 USD | **`ACCUMULATION`** |
| `15m` | 1,780,000.00 USD | 6,920,000.00 USD | **`ACCUMULATION`** |
| `30m` | 4,220,000.00 USD | 19,390,000.00 USD | **`ACCUMULATION`** |
| `1h` | -862,680.00 USD | 4,050,000.00 USD | **`ACCUMULATION`** |
| `2h` | -13,950,000.00 USD | -2,960,000.00 USD | **`DISTRIBUTION`** |
| `4h` | -12,660,000.00 USD | -23,710,000.00 USD | **`DISTRIBUTION`** |
| `6h` | 1,870,000.00 USD | 40,870,000.00 USD | **`ACCUMULATION`** |
| `8h` | 16,690,000.00 USD | 90,040,000.00 USD | **`ACCUMULATION`** |
| `12h` | 17,570,000.00 USD | 99,820,000.00 USD | **`ACCUMULATION`** |
| `24h` | 920,950.00 USD | 67,670,000.00 USD | **`ACCUMULATION`** |
| `1w` | 34,460,000.00 USD | 245,490,000.00 USD | **`ACCUMULATION`** |
| `30d` | 58,280,000.00 USD | -515,510,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-1.01M` | 15m=`+1.78M` | 1h=`-862.68K` | 24h=`+920.95K`
* Futures Capital Netflows: 5m=`+3.36M` | 15m=`+6.92M` | 1h=`+4.05M` | 24h=`+67.67M`
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
  * `2026-10-30 02:54:26 IST`: [msn.com] - (Sentiment: `Neutral`)
  * `2026-10-30 02:15:26 IST`: [morningstar.com] - (Sentiment: `Neutral`)
  * `2026-10-30 03:10:26 IST`: [sec.gov] - (Sentiment: `Neutral`)
  * `2026-10-30 03:09:26 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 03:09:26 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 03:09:26 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 00:11:26 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 00:11:26 IST`: [@DeItaone] - (Sentiment: `Neutral`)
  * `2026-10-29 23:11:26 IST`: [@mb_ghalibaf] - (Sentiment: `Neutral`)
  * `2026-10-29 23:11:26 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-29 23:11:26 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-29 23:11:26 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:11:26 IST`: [fxstreet.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:11:26 IST`: [ForexFactory] - (Sentiment: `Neutral`)
  * `2026-10-29 21:11:26 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)


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
  * Execution Entry: `1264.27` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `1235.62` (Risk Distance: `28.65` pts)
  * +2.5R Take Profit: `1335.90`
  * Mathematical Lot Sizing: **`0.34 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `1295.83` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `1324.48` (Risk Distance: `28.65` pts)
  * +2.5R Take Profit: `1224.20`
  * Mathematical Lot Sizing: **`0.34 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`1285.08`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
