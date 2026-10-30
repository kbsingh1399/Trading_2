# 🏛️ SOVEREIGN CANDIDATE DOSSIER: ZECUSD
**Canonical Key**: `ZECUSD` | **Broker Instrument**: `ZECUSD.p` | **Asset Class**: `Crypto Altcoin`
**Timestamp**: `2026-10-30 15:51:23 IST` (`2026-10-30 10:21:23 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `1252.05` | **Live Ask Quote**: `1253.10` | **Mid Price**: `1252.57`
- **Spread Points**: `105.00` | **Spread BPS**: `8.38 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `1252.57` | VWAP Z-Score: `+0.00` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `3.13` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `50.00` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `1261.34` | Lower -3.00σ Band: `1243.81`
  * Upper +2.51σ Band: `1259.46` | Lower -2.51σ Band: `1245.69`
  * Upper +2.01σ Band: `1257.84` | Lower -2.01σ Band: `1247.31`
  * Upper +2.00σ Band: `1257.59` | Lower -2.00σ Band: `1247.56`
  * Upper +1.28σ Band: `1256.08` | Lower -1.28σ Band: `1249.07`
  * Upper +1.00σ Band: `1255.08` | Lower -1.00σ Band: `1250.07`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`1252.57` | EMA-20=`1252.57` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`1252.57` (Slope: `+0.0000`) | EMA-100=`1252.57`
  * Institutional Anchors: EMA-144=`1252.57` | EMA-200=`1252.57` (Slope: `+0.0000`) | EMA-233=`1252.57`
- **Range Boundaries**: 24H High=`1265.10` | 24H Low=`1240.05` | Weekly High=`1277.63` | Weekly Low=`1227.52`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `1280.92` (Distance: `-2.26%`)
  * Point of Control (POC) = `1247.68` (Distance: `+0.34%`)
  * Value Area Low (VAL) = `1239.95` (Distance: `+0.97%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`1309.91` | POC=`1246.71` | VAL=`1230.27`
  * Prior Day Extremes: PDH=`1396.49` | PDL=`1206.89` | PDC=`1244.38`
  * Monday Range Blueprint: High=`1267.53` | Mid=`1222.14` | Low=`1176.75`
  * Developing Weekly Value Area: Weekly VAH=`1293.21` | Weekly POC=`1240.47` | Weekly VAL=`1200.92`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`1296.00` | Low=`1180.03`
  * London Session (08:00-16:00 UTC): High=`1283.82` | Low=`1239.95`
  * New York Session (13:00-21:00 UTC): High=`1255.62` | Low=`1245.73`
  * Initial Balance (First Hour): IB High=`1283.82` | IB Low=`1264.92`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `1247.56` - `1257.59`
  * Optimal Trade Entry (OTE 0.705): `1255.08`
  * Structural Invalidation Anchor (0.786): `1262.60`

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
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 15:50:34 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `12` | `0xb83d...6e36` | `SHORT` | 65,528,984.42 USD | `52,385.47` | `1336.45` | `1251.10` | `3224.23` | 4,481,582.98 USD | `+6.84%` | `3X Cross` |
| `21` | `0x5b5d...c060` | `SHORT` | 50,195,681.98 USD | `40,121.38` | `1478.36` | `1251.10` | `4874.52` | 9,118,353.13 USD | `+18.17%` | `3X Cross` |
| `36` | `0x7fda...17d1` | `SHORT` | 33,318,859.82 USD | `26,635.91` | `1262.58` | `1251.10` | `2620.45` | 310,975.29 USD | `+0.93%` | `5X Cross` |
| `82` | `0x60b0...991e` | `LONG` | 20,993,132.71 USD | `16,779.74` | `1179.65` | `1251.10` | `917.14` | 1,198,885.70 USD | `+5.71%` | `10X Cross` |
| `140` | `0xc36a...105b` | `LONG` | 14,401,186.90 USD | `11,510.82` | `1215.14` | `1251.10` | `967.21` | 413,905.87 USD | `+2.87%` | `10X Cross` |
| `178` | `0x8742...8427` | `LONG` | 11,509,793.59 USD | `9,201.21` | `1286.37` | `1251.10` | `717.61` | -326,376.40 USD | `-2.84%` | `10X Cross` |
| `192` | `0x58b2...11f3` | `LONG` | 10,718,407.24 USD | `8,563.08` | `1246.56` | `1251.10` | `385.73` | 43,989.66 USD | `+0.41%` | `10X Cross` |
| `194` | `0x9071...5c0b` | `LONG` | 10,654,278.06 USD | `8,517.29` | `1353.83` | `1251.10` | `214.62` | -876,681.54 USD | `-8.23%` | `2X Cross` |
| `195` | `0x9ffd...ce40` | `LONG` | 10,642,416.53 USD | `8,502.37` | `1252.16` | `1251.10` | `604.35` | -3,900.30 USD | `-0.04%` | `5X Cross` |
| `199` | `0xad59...ba81` | `SHORT` | 10,540,517.50 USD | `8,425.00` | `330.91` | `1251.10` | `2147.69` | -7,752,559.73 USD | `-73.55%` | `10X Cross` |
| `204` | `0xdd53...2b13` | `SHORT` | 10,252,276.33 USD | `8,195.92` | `741.54` | `1251.10` | `8465.08` | -4,174,679.96 USD | `-40.72%` | `3X Cross` |
| `223` | `0x880a...311c` | `SHORT` | 9,640,823.90 USD | `7,707.11` | `1367.50` | `1251.10` | `2232.11` | 898,660.30 USD | `+9.32%` | `10X Cross` |
| `235` | `0xbf73...5d58` | `LONG` | 9,387,750.00 USD | `7,500.00` | `1248.78` | `1251.10` | `137.84` | 21,904.38 USD | `+0.23%` | `10X Cross` |
| `269` | `0x2b61...2f6c` | `LONG` | 8,515,505.27 USD | `6,807.00` | `1453.56` | `1251.10` | `555.67` | -1,378,845.96 USD | `-16.19%` | `10X Cross` |
| `290` | `0x2ae5...83e7` | `LONG` | 8,051,793.12 USD | `6,436.80` | `1391.82` | `1251.10` | `0.000000` | -907,098.87 USD | `-11.27%` | `1X Cross` |
| `321` | `0xecb6...2b00` | `SHORT` | 7,196,101.72 USD | `5,751.84` | `1277.70` | `1251.10` | `6159.39` | 153,033.71 USD | `+2.13%` | `5X Cross` |
| `335` | `0x26b6...9a13` | `LONG` | 6,797,052.86 USD | `5,433.73` | `1282.23` | `1251.10` | `232.96` | -170,250.38 USD | `-2.50%` | `10X Cross` |
| `352` | `0x45d2...4029` | `SHORT` | 6,538,454.30 USD | `5,227.00` | `833.44` | `1251.10` | `9144.28` | -2,182,076.33 USD | `-33.37%` | `5X Cross` |
| `367` | `0xea00...a918` | `LONG` | 6,259,500.00 USD | `5,000.00` | `739.16` | `1251.10` | `0.000000` | 2,563,684.89 USD | `+40.96%` | `5X Cross` |
| `377` | `0xdd7a...8830` | `LONG` | 6,080,097.69 USD | `4,860.19` | `897.48` | `1251.10` | `786.60` | 1,718,194.02 USD | `+28.26%` | `10X Cross` |
| `421` | `0x469e...58a5` | `SHORT` | 5,208,979.87 USD | `4,163.52` | `1242.31` | `1251.10` | `1952.42` | -36,595.22 USD | `-0.70%` | `10X Cross` |
| `433` | `0x4cae...7c34` | `LONG` | 5,005,035.15 USD | `4,002.27` | `1169.72` | `1251.10` | `978.11` | 323,485.80 USD | `+6.46%` | `10X Cross` |
| `439` | `0x382b...3e39` | `LONG` | 4,926,281.87 USD | `3,938.19` | `1220.71` | `1251.10` | `0.000000` | 118,888.55 USD | `+2.41%` | `10X Cross` |
| `442` | `0xd4c1...3d1d` | `SHORT` | 4,916,337.22 USD | `3,930.24` | `1291.66` | `1251.10` | `2362.95` | 160,198.89 USD | `+3.26%` | `10X Cross` |
| `449` | `0xa61c...66b9` | `LONG` | 4,863,499.20 USD | `3,888.00` | `1148.34` | `1251.10` | `0.000000` | 398,757.06 USD | `+8.20%` | `10X Cross` |
| `474` | `0x9aa5...58af` | `SHORT` | 4,653,735.78 USD | `3,720.31` | `1205.51` | `1251.10` | `3692.81` | -168,848.98 USD | `-3.63%` | `10X Cross` |
| `477` | `0x0153...8052` | `SHORT` | 4,627,532.63 USD | `3,698.18` | `1307.82` | `1251.10` | `2504.94` | 209,038.11 USD | `+4.52%` | `1X Isolated` |
| `506` | `0xb122...e4ba` | `LONG` | 4,376,236.12 USD | `3,498.47` | `1265.25` | `1251.10` | `1127.16` | -50,215.41 USD | `-1.15%` | `10X Cross` |
| `540` | `0xd21d...90f1` | `LONG` | 4,066,075.00 USD | `3,250.00` | `1253.64` | `1251.10` | `876.17` | -8,266.73 USD | `-0.20%` | `4X Isolated` |
| `545` | `0x456f...cdf1` | `LONG` | 4,047,458.63 USD | `3,235.12` | `1267.53` | `1251.10` | `518.58` | -53,153.92 USD | `-1.31%` | `10X Cross` |
| `563` | `0x1338...c48e` | `LONG` | 3,941,196.70 USD | `3,149.43` | `1018.52` | `1251.10` | `820.46` | 733,451.16 USD | `+18.61%` | `4X Isolated` |
| `579` | `0xdbe0...d6d5` | `LONG` | 3,860,723.48 USD | `3,085.37` | `422.97` | `1251.10` | `338.78` | 2,555,718.99 USD | `+66.20%` | `3X Isolated` |
| `594` | `0x2e30...4cb5` | `SHORT` | 3,754,401.22 USD | `3,001.36` | `1282.27` | `1251.10` | `2884.88` | 94,166.25 USD | `+2.51%` | `2X Cross` |
| `595` | `0x325e...9564` | `LONG` | 3,753,838.32 USD | `3,000.91` | `1298.07` | `1251.10` | `148.56` | -141,566.84 USD | `-3.77%` | `10X Cross` |
| `597` | `0x9c06...0560` | `SHORT` | 3,741,734.70 USD | `2,989.80` | `786.00` | `1251.10` | `2573.12` | -1,391,739.70 USD | `-37.20%` | `10X Cross` |
| `611` | `0x27c9...d65d` | `SHORT` | 3,675,781.84 USD | `2,938.04` | `1254.41` | `1251.10` | `1737.92` | 9,728.20 USD | `+0.26%` | `10X Cross` |
| `702` | `0xa183...0482` | `LONG` | 3,169,780.60 USD | `2,534.00` | `530.25` | `1251.10` | `444.70` | 1,826,117.88 USD | `+57.61%` | `5X Isolated` |
| `704` | `0xac48...3201` | `LONG` | 3,167,159.65 USD | `2,531.50` | `1378.58` | `1251.10` | `538.02` | -322,712.63 USD | `-10.19%` | `10X Cross` |
| `712` | `0x0871...e927` | `LONG` | 3,127,481.00 USD | `2,500.00` | `1276.50` | `1251.10` | `0.000000` | -63,769.00 USD | `-2.04%` | `10X Cross` |
| `734` | `0x9b86...6e6e` | `LONG` | 3,081,834.63 USD | `2,463.30` | `637.58` | `1251.10` | `882.63` | 1,511,285.35 USD | `+49.04%` | `3X Cross` |
| `811` | `0xf48f...10fe` | `LONG` | 2,775,552.84 USD | `2,218.49` | `1517.87` | `1251.10` | `983.76` | -591,833.98 USD | `-21.32%` | `3X Cross` |
| `834` | `0x71d0...8c26` | `SHORT` | 2,685,669.79 USD | `2,146.99` | `1265.96` | `1251.10` | `3810.67` | 32,333.04 USD | `+1.20%` | `10X Cross` |
| `840` | `0x5bc4...3b0c` | `SHORT` | 2,665,342.67 USD | `2,130.74` | `1089.65` | `1251.10` | `3682.18` | -343,585.09 USD | `-12.89%` | `5X Cross` |
| `855` | `0x8de4...b9aa` | `SHORT` | 2,616,403.72 USD | `2,091.29` | `1331.35` | `1251.10` | `1690.07` | 167,835.99 USD | `+6.41%` | `3X Cross` |
| `862` | `0x4fe2...ac59` | `SHORT` | 2,591,326.91 USD | `2,071.57` | `1478.56` | `1251.10` | `1848.48` | 471,619.30 USD | `+18.20%` | `10X Cross` |
| `867` | `0xdf57...93f5` | `LONG` | 2,569,991.85 USD | `2,054.35` | `1227.36` | `1251.10` | `897.41` | 48,569.81 USD | `+1.89%` | `4X Isolated` |
| `871` | `0xbcd4...0dd2` | `LONG` | 2,544,230.53 USD | `2,033.92` | `1228.20` | `1251.10` | `767.25` | 46,179.71 USD | `+1.82%` | `10X Cross` |
| `881` | `0x9a99...d21a` | `LONG` | 2,501,800.00 USD | `2,000.00` | `1278.44` | `1251.10` | `0.000000` | -55,073.67 USD | `-2.20%` | `10X Cross` |
| `882` | `0xf29c...9971` | `LONG` | 2,501,800.00 USD | `2,000.00` | `1254.95` | `1251.10` | `0.000000` | -8,097.07 USD | `-0.32%` | `10X Cross` |
| `907` | `0x77ee...2902` | `SHORT` | 2,434,468.74 USD | `1,946.03` | `759.84` | `1251.10` | `5738.62` | -955,791.23 USD | `-39.26%` | `10X Cross` |
| `915` | `0x3e2f...b269` | `SHORT` | 2,408,813.01 USD | `1,925.51` | `1134.87` | `1251.10` | `2977.34` | -223,614.15 USD | `-9.28%` | `10X Cross` |
| `929` | `0x4f12...618b` | `SHORT` | 2,373,573.68 USD | `1,896.28` | `1608.30` | `1251.10` | `2116.96` | 676,210.71 USD | `+28.49%` | `3X Cross` |
| `973` | `0x866d...d6e1` | `LONG` | 2,254,350.85 USD | `1,802.05` | `674.73` | `1251.10` | `134.27` | 1,038,449.54 USD | `+46.06%` | `10X Cross` |
| `997` | `0x2309...a2d9` | `LONG` | 2,189,887.91 USD | `1,750.37` | `1186.09` | `1251.10` | `807.72` | 113,793.80 USD | `+5.20%` | `8X Cross` |
| `1035` | `0x265e...7f70` | `LONG` | 2,066,484.65 USD | `1,651.74` | `1382.98` | `1251.10` | `0.000000` | -217,838.11 USD | `-10.54%` | `3X Cross` |
| `1046` | `0xfe7c...b7ae` | `SHORT` | 2,055,106.90 USD | `1,642.64` | `1346.92` | `1251.10` | `5730.68` | 157,401.72 USD | `+7.66%` | `10X Cross` |
| `1049` | `0x3e47...aaf6` | `LONG` | 2,047,149.91 USD | `1,636.28` | `1278.38` | `1251.10` | `1051.25` | -44,641.88 USD | `-2.18%` | `10X Cross` |
| `1050` | `0x2edd...8179` | `SHORT` | 2,046,447.38 USD | `1,635.98` | `1261.55` | `1251.10` | `2869.78` | 17,415.50 USD | `+0.85%` | `10X Cross` |
| `1071` | `0x7f75...9edf` | `LONG` | 2,017,630.75 USD | `1,612.17` | `1200.26` | `1251.10` | `986.82` | 82,609.68 USD | `+4.09%` | `10X Cross` |
| `1080` | `0xfc27...9d9d` | `SHORT` | 2,007,244.18 USD | `1,604.64` | `1295.09` | `1251.10` | `12995.82` | 70,901.63 USD | `+3.53%` | `10X Cross` |
| `1082` | `0x6646...6de5` | `SHORT` | 2,001,120.00 USD | `1,600.00` | `660.64` | `1251.10` | `4189.82` | -944,095.03 USD | `-47.18%` | `10X Cross` |
| `1086` | `0x023a...2355` | `SHORT` | 1,990,569.68 USD | `1,591.31` | `1310.00` | `1251.10` | `4414.05` | 94,039.57 USD | `+4.72%` | `10X Cross` |
| `1106` | `0xab59...59b5` | `LONG` | 1,958,371.85 USD | `1,565.32` | `1342.15` | `1251.10` | `839.03` | -142,523.37 USD | `-7.28%` | `10X Cross` |
| `1155` | `0x039c...0ebd` | `SHORT` | 1,903,106.75 USD | `1,521.39` | `1245.17` | `1251.10` | `3751.26` | -8,712.89 USD | `-0.46%` | `10X Cross` |
| `1164` | `0xcf67...eb24` | `LONG` | 1,876,350.00 USD | `1,500.00` | `887.05` | `1251.10` | `619.52` | 545,778.63 USD | `+29.09%` | `10X Cross` |
| `1181` | `0x7277...0b98` | `SHORT` | 1,846,138.23 USD | `1,475.73` | `1287.86` | `1251.10` | `2205.46` | 54,393.89 USD | `+2.95%` | `10X Cross` |
| `1208` | `0x3205...40bb` | `SHORT` | 1,823,957.45 USD | `1,457.65` | `1257.03` | `1251.10` | `2264.70` | 8,346.04 USD | `+0.46%` | `10X Cross` |
| `1249` | `0x926a...af36` | `LONG` | 1,753,361.51 USD | `1,401.68` | `1254.50` | `1251.10` | `1187.92` | -5,040.39 USD | `-0.29%` | `10X Isolated` |
| `1251` | `0x2ab7...c2f8` | `LONG` | 1,751,897.96 USD | `1,400.51` | `813.26` | `1251.10` | `792.69` | 612,916.27 USD | `+34.99%` | `3X Cross` |
| `1268` | `0x11be...8b1d` | `LONG` | 1,721,300.91 USD | `1,375.83` | `1206.55` | `1251.10` | `1134.68` | 61,292.96 USD | `+3.56%` | `10X Isolated` |
| `1323` | `0x5323...b23c` | `SHORT` | 1,630,598.19 USD | `1,303.54` | `1254.00` | `1251.10` | `5523.42` | 4,036.02 USD | `+0.25%` | `5X Cross` |
| `1354` | `0xe065...0f85` | `SHORT` | 1,580,408.94 USD | `1,262.61` | `1087.02` | `1251.10` | `1547.02` | -207,932.81 USD | `-13.16%` | `10X Cross` |
| `1368` | `0x413c...886c` | `LONG` | 1,564,875.00 USD | `1,250.00` | `1237.51` | `1251.10` | `0.000000` | 17,985.54 USD | `+1.15%` | `10X Cross` |
| `1375` | `0xdf83...3cff` | `SHORT` | 1,561,372.80 USD | `1,248.00` | `1260.55` | `1251.10` | `1865.26` | 11,797.50 USD | `+0.76%` | `10X Cross` |
| `1428` | `0x2847...d47b` | `LONG` | 1,515,728.04 USD | `1,211.71` | `1232.45` | `1251.10` | `0.000000` | 22,360.44 USD | `+1.48%` | `5X Cross` |
| `1442` | `0x5975...9abd` | `LONG` | 1,501,320.00 USD | `1,200.00` | `1179.54` | `1251.10` | `554.48` | 85,877.21 USD | `+5.72%` | `5X Cross` |
| `1445` | `0x266b...efcb` | `LONG` | 1,501,200.00 USD | `1,200.00` | `893.76` | `1251.10` | `418.82` | 428,690.30 USD | `+28.56%` | `10X Cross` |
| `1472` | `0x69cc...14fd` | `SHORT` | 1,452,972.39 USD | `1,161.36` | `675.33` | `1251.10` | `8122.85` | -668,666.86 USD | `-46.02%` | `10X Cross` |
| `1487` | `0x3fc5...c0c1` | `SHORT` | 1,436,813.28 USD | `1,148.44` | `1264.34` | `1251.10` | `2806.08` | 15,200.49 USD | `+1.06%` | `10X Cross` |
| `1527` | `0x5f94...4b96` | `LONG` | 1,395,314.30 USD | `1,115.27` | `538.00` | `1251.10` | `0.000000` | 795,296.66 USD | `+57.00%` | `10X Cross` |
| `1536` | `0xe35c...a1d3` | `LONG` | 1,390,200.22 USD | `1,111.36` | `1311.66` | `1251.10` | `690.98` | -67,523.92 USD | `-4.86%` | `2X Isolated` |
| `1550` | `0x71df...a23d` | `SHORT` | 1,373,939.93 USD | `1,098.28` | `513.50` | `1251.10` | `2561.31` | -809,969.74 USD | `-58.95%` | `2X Cross` |
| `1578` | `0xbfc7...80b4` | `SHORT` | 1,344,932.50 USD | `1,075.00` | `558.03` | `1251.10` | `2704.98` | -745,053.77 USD | `-55.40%` | `10X Cross` |
| `1607` | `0x123d...3bff` | `SHORT` | 1,306,573.77 USD | `1,044.34` | `519.62` | `1251.10` | `4110.75` | -763,915.57 USD | `-58.47%` | `10X Cross` |
| `1673` | `0x668c...ea2e` | `SHORT` | 1,251,100.00 USD | `1,000.00` | `1406.98` | `1251.10` | `4212.80` | 155,881.99 USD | `+12.46%` | `10X Cross` |
| `1675` | `0xe282...df29` | `LONG` | 1,250,900.00 USD | `1,000.00` | `420.99` | `1251.10` | `809.51` | 829,913.14 USD | `+66.35%` | `10X Cross` |
| `1696` | `0x17f0...094f` | `LONG` | 1,231,351.82 USD | `984.30` | `1287.23` | `1251.10` | `537.03` | -35,668.35 USD | `-2.90%` | `5X Cross` |
| `1714` | `0x38f9...cb04` | `SHORT` | 1,218,817.04 USD | `974.43` | `1253.73` | `1251.10` | `2136.89` | 2,853.77 USD | `+0.23%` | `10X Cross` |
| `1717` | `0x51f6...2b39` | `SHORT` | 1,216,888.03 USD | `972.81` | `1299.77` | `1251.10` | `2520.72` | 47,539.68 USD | `+3.91%` | `10X Cross` |
| `1776` | `0x757d...94ba` | `LONG` | 1,157,175.00 USD | `925.00` | `1558.31` | `1251.10` | `0.000000` | -284,265.59 USD | `-24.57%` | `10X Cross` |
| `1820` | `0xb911...5525` | `LONG` | 1,125,990.00 USD | `900.00` | `1294.82` | `1251.10` | `1035.46` | -39,347.82 USD | `-3.49%` | `10X Cross` |
| `1830` | `0xef96...9383` | `SHORT` | 1,115,977.93 USD | `892.14` | `1259.28` | `1251.10` | `5092.54` | 7,477.08 USD | `+0.67%` | `10X Cross` |
| `1865` | `0xcf0a...856f` | `LONG` | 1,090,244.23 USD | `871.15` | `1292.19` | `1251.10` | `1026.63` | -35,450.62 USD | `-3.25%` | `4X Cross` |
| `1891` | `0xdf95...7d72` | `SHORT` | 1,067,355.44 USD | `853.27` | `1074.39` | `1251.10` | `45445.42` | -150,608.00 USD | `-14.11%` | `10X Cross` |
| `1920` | `0xb2f7...af9f` | `SHORT` | 1,039,313.79 USD | `830.72` | `746.63` | `1251.10` | `8264.95` | -419,074.76 USD | `-40.32%` | `10X Cross` |
| `1932` | `0x601c...4f54` | `SHORT` | 1,030,977.69 USD | `824.42` | `615.11` | `1251.10` | `3145.76` | -523,864.94 USD | `-50.81%` | `5X Cross` |
| `1950` | `0xae55...2236` | `LONG` | 1,022,573.22 USD | `817.47` | `1467.80` | `1251.10` | `0.000000` | -177,307.99 USD | `-17.34%` | `10X Cross` |
| `1986` | `0x0f02...5384` | `LONG` | 1,002,256.25 USD | `800.78` | `1290.36` | `1251.10` | `307.08` | -31,037.82 USD | `-3.10%` | `3X Cross` |
| `1988` | `0x9b0f...db40` | `LONG` | 1,001,040.00 USD | `800.00` | `1268.86` | `1251.10` | `801.62` | -14,049.76 USD | `-1.40%` | `10X Cross` |

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
| `ANNOUNCEMENT` | `INFO` | `1017.00` | 10.17 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Long: 0.01K USD at 1017.0000 USD [API] | `2026-09-04 08:53:37` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`1404.55` (Vol: 3,000,000.00 USD, Dist: `+12.45%`) | Long MP=`1176.48` (Vol: 3,400,000.00 USD, Dist: `--5.81%`)
  * 48H Horizon: Short MP=`1404.55` (Vol: 3,000,000.00 USD, Dist: `+12.45%`) | Long MP=`1176.48` (Vol: 3,400,000.00 USD, Dist: `--5.81%`)
  * 3D Horizon: Short MP=`1404.55` (Vol: 3,000,000.00 USD, Dist: `+12.45%`) | Long MP=`1176.48` (Vol: 3,400,000.00 USD, Dist: `--5.81%`)
  * 7D Horizon: Short MP=`1404.10` (Vol: 3,000,000.00 USD, Dist: `+12.41%`) | Long MP=`1176.74` (Vol: 4,900,000.00 USD, Dist: `--5.79%`)
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
| `5m` | `BALANCED` | 0.00 USD | 1,750.00 USD | 1,750.00 USD | 1,750.00 USD | `1` | `2026-10-30 10:20:00 UTC - 2026-10-30 10:25:00 UTC` |
| `15m` | `BALANCED` | 0.00 USD | 1,750.00 USD | 1,750.00 USD | 1,750.00 USD | `1` | `2026-10-30 10:15:00 UTC - 2026-10-30 10:30:00 UTC` |
| `1h` | `BALANCED` | 0.00 USD | 1,750.00 USD | 1,750.00 USD | 1,750.00 USD | `1` | `2026-10-30 10:00:00 UTC - 2026-10-30 11:00:00 UTC` |
| `4h` | `BALANCED` | 0.00 USD | 1,750.00 USD | 1,750.00 USD | 1,750.00 USD | `1` | `2026-10-30 08:00:00 UTC - 2026-10-30 12:00:00 UTC` |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `0 USD` | Total OI Tokens: `-`
  * 1h OI Change: `0.00%` | 4h OI Change: `0.00%` | 24h OI Change: `0.00%`
  * Exchange Breakdown: Binance=`-` | Bybit=`-` | OKX=`-` | Hyperliquid=`-`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `84.54K` | Last 24h: `171.90K` | Last 3d: `285.15K` | Last 7d: `847.79K`
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
| `0:00 UTC` | `1245.75` | `1245.57` | `1245.75` | `1250.55` | `1240.05` | 17,224,192.69 USD | 9,235,789.14 USD | 7,988,403.55 USD | 1,247,385.58 USD | `+7.24%` | `1B / 6S` |
| `5:00 UTC` | `1251.45` | `1250.99` | `1251.45` | `1255.05` | `1246.35` | 13,619,576.55 USD | 6,741,413.50 USD | 6,878,163.05 USD | -136,749.55 USD | `-1.00%` | `2B / 0S` |
| `0:00 UTC` | `1249.95` | `1249.10` | `1249.95` | `1253.55` | `1244.55` | 10,263,783.49 USD | 5,117,369.60 USD | 5,146,413.89 USD | -29,044.29 USD | `-0.28%` | `1B / 4S` |
| `5:00 UTC` | `1246.65` | `1246.77` | `1246.65` | `1252.35` | `1243.95` | 13,017,000.97 USD | 7,727,648.32 USD | 5,289,352.64 USD | 2,438,295.68 USD | `+18.73%` | `8B / 5S` |
| `0:00 UTC` | `1244.55` | `1245.81` | `1244.55` | `1249.05` | `1243.65` | 9,717,386.64 USD | 3,914,194.68 USD | 5,803,191.96 USD | -1,888,997.28 USD | `-19.44%` | `0B / 1S` |
| `5:00 UTC` | `1242.15` | `1244.40` | `1242.15` | `1249.35` | `1241.25` | 8,638,502.97 USD | 4,533,952.89 USD | 4,104,550.08 USD | 429,402.82 USD | `+4.97%` | `4B / 2S` |
| `0:00 UTC` | `1251.15` | `1247.35` | `1251.15` | `1251.75` | `1240.05` | 9,977,652.60 USD | 4,992,881.35 USD | 4,984,771.25 USD | 8,110.10 USD | `+0.08%` | `3B / 5S` |
| `5:00 UTC` | `1243.95` | `1249.40` | `1243.95` | `1256.55` | `1243.35` | 15,678,426.53 USD | 9,268,825.46 USD | 6,409,601.07 USD | 2,859,224.38 USD | `+18.24%` | `10B / 2S` |
| `0:00 UTC` | `1249.95` | `1250.19` | `1249.95` | `1256.25` | `1246.35` | 11,248,393.80 USD | 4,953,252.73 USD | 6,295,141.07 USD | -1,341,888.34 USD | `-11.93%` | `1B / 7S` |
| `5:00 UTC` | `1249.35` | `1248.88` | `1249.35` | `1249.95` | `1247.85` | 785,272.97 USD | 420,674.78 USD | 364,598.19 USD | 56,076.60 USD | `+7.14%` | `1B / 1S` |

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
| `5m` | 92,950.00 USD | -465,520.00 USD | **`DISTRIBUTION`** |
| `15m` | -545,480.00 USD | 193,590.00 USD | **`DISTRIBUTION`** |
| `30m` | -127,580.00 USD | 1,530,000.00 USD | **`ACCUMULATION`** |
| `1h` | -1,820,000.00 USD | 2,720,000.00 USD | **`ACCUMULATION`** |
| `2h` | -2,480,000.00 USD | 9,420,000.00 USD | **`ACCUMULATION`** |
| `4h` | 1,400,000.00 USD | -13,090,000.00 USD | **`DISTRIBUTION`** |
| `6h` | 1,130,000.00 USD | -27,230,000.00 USD | **`DISTRIBUTION`** |
| `8h` | 4,150,000.00 USD | -5,650,000.00 USD | **`DISTRIBUTION`** |
| `12h` | 979,260.00 USD | -13,660,000.00 USD | **`DISTRIBUTION`** |
| `24h` | 22,310,000.00 USD | 77,430,000.00 USD | **`ACCUMULATION`** |
| `1w` | 34,950,000.00 USD | 223,470,000.00 USD | **`ACCUMULATION`** |
| `30d` | 61,890,000.00 USD | -571,470,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+92.95K` | 15m=`-545.48K` | 1h=`-1.82M` | 24h=`+22.31M`
* Futures Capital Netflows: 5m=`-465.52K` | 15m=`+193.59K` | 1h=`+2.72M` | 24h=`+77.43M`
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
  * `2026-10-30 15:33:17 IST`: [ec.europa.eu] - (Sentiment: `Neutral`)
  * `2026-10-30 15:32:17 IST`: [ec.europa.eu] - (Sentiment: `Neutral`)
  * `2026-10-30 15:18:17 IST`: [dailyforex.com] - (Sentiment: `Neutral`)
  * `2026-10-30 15:12:17 IST`: [breakingthenews.net] - (Sentiment: `Neutral`)
  * `2026-10-30 15:46:17 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 15:46:17 IST`: [@FirstSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 15:46:17 IST`: [destatis.de] - (Sentiment: `Neutral`)
  * `2026-10-30 15:46:17 IST`: [istat.it] - (Sentiment: `Neutral`)
  * `2026-10-30 15:46:17 IST`: [channelnewsasia.com] - (Sentiment: `Neutral`)
  * `2026-10-30 15:46:17 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 15:46:17 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 15:45:17 IST`: [kof.ethz.ch] - (Sentiment: `Neutral`)
  * `2026-10-30 15:45:17 IST`: [gerlachmacro.substack.com] - (Sentiment: `Neutral`)
  * `2026-10-30 15:45:17 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-30 15:45:17 IST`: [insee.fr] - (Sentiment: `Neutral`)


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
  * Execution Entry: `1239.95` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `1234.62` (Risk Distance: `5.33` pts)
  * +2.5R Take Profit: `1253.28`
  * Mathematical Lot Sizing: **`1.87 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `1280.92` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `1286.25` (Risk Distance: `5.33` pts)
  * +2.5R Take Profit: `1267.59`
  * Mathematical Lot Sizing: **`1.87 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`1262.60`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
