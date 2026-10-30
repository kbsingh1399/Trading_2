# 🏛️ SOVEREIGN CANDIDATE DOSSIER: ZECUSD
**Canonical Key**: `ZECUSD` | **Broker Instrument**: `ZECUSD.p` | **Asset Class**: `Crypto Altcoin`
**Timestamp**: `2026-10-30 11:35:25 IST` (`2026-10-30 06:05:25 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `1268.73` | **Live Ask Quote**: `1269.98` | **Mid Price**: `1269.36`
- **Spread Points**: `125.00` | **Spread BPS**: `9.85 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `1251.85` | VWAP Z-Score: `+0.56` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `15.36` (Volatility Regime: `HIGH_EXPANSION`)
  * 14-Period RSI: `49.99` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `1326.55` | Lower -3.00σ Band: `1177.16`
  * Upper +2.51σ Band: `1314.35` | Lower -2.51σ Band: `1189.36`
  * Upper +2.01σ Band: `1301.90` | Lower -2.01σ Band: `1201.81`
  * Upper +2.00σ Band: `1301.65` | Lower -2.00σ Band: `1202.05`
  * Upper +1.28σ Band: `1283.72` | Lower -1.28σ Band: `1219.98`
  * Upper +1.00σ Band: `1276.75` | Lower -1.00σ Band: `1226.95`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`1271.59` | EMA-20=`1266.71` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`1268.20` (Slope: `+0.0000`) | EMA-100=`1272.66`
  * Institutional Anchors: EMA-144=`1274.16` | EMA-200=`1276.06` (Slope: `-0.0105`) | EMA-233=`1278.20`
- **Range Boundaries**: 24H High=`1396.49` | 24H Low=`1180.03` | Weekly High=`1396.49` | Weekly Low=`1180.03`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `1285.56` (Distance: `-1.20%`)
  * Point of Control (POC) = `1275.51` (Distance: `-0.42%`)
  * Value Area Low (VAL) = `1235.31` (Distance: `+2.82%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`1309.91` | POC=`1246.71` | VAL=`1230.27`
  * Prior Day Extremes: PDH=`1396.49` | PDL=`1206.89` | PDC=`1244.38`
  * Monday Range Blueprint: High=`1267.53` | Mid=`1222.14` | Low=`1176.75`
  * Developing Weekly Value Area: Weekly VAH=`1294.68` | Weekly POC=`1239.01` | Weekly VAL=`1200.92`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`1296.00` | Low=`1180.03`
  * London Session (08:00-16:00 UTC): High=`1283.82` | Low=`1263.39`
  * New York Session (13:00-21:00 UTC): High=`1276.97` | Low=`1261.74`
  * Initial Balance (First Hour): IB High=`1283.82` | IB Low=`1264.92`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `1264.28` - `1274.43`
  * Optimal Trade Entry (OTE 0.705): `1271.89`
  * Structural Invalidation Anchor (0.786): `1279.51`

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
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 11:33:47 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `13` | `0xb83d...6e36` | `SHORT` | 66,508,592.71 USD | `52,385.47` | `1336.45` | `1269.80` | `3683.67` | 3,501,974.69 USD | `+5.27%` | `3X Cross` |
| `22` | `0x5b5d...c060` | `SHORT` | 51,126,674.53 USD | `40,121.38` | `1478.36` | `1269.80` | `5095.34` | 8,187,360.58 USD | `+16.01%` | `3X Cross` |
| `38` | `0x7fda...17d1` | `SHORT` | 33,263,024.86 USD | `26,199.61` | `1262.66` | `1269.80` | `2613.42` | -181,857.94 USD | `-0.55%` | `5X Cross` |
| `81` | `0x60b0...991e` | `LONG` | 21,333,761.44 USD | `16,779.74` | `1179.65` | `1269.80` | `921.24` | 1,539,514.42 USD | `+7.22%` | `10X Cross` |
| `139` | `0xc36a...105b` | `LONG` | 14,669,389.01 USD | `11,510.82` | `1215.14` | `1269.80` | `960.70` | 682,107.98 USD | `+4.65%` | `10X Cross` |
| `155` | `0x9071...5c0b` | `LONG` | 13,354,854.84 USD | `10,517.29` | `1353.83` | `1269.80` | `0.1605` | -883,764.03 USD | `-6.62%` | `1X Cross` |
| `179` | `0x8742...8427` | `LONG` | 11,683,696.46 USD | `9,201.21` | `1286.37` | `1269.80` | `697.88` | -152,473.54 USD | `-1.31%` | `10X Cross` |
| `192` | `0x58b2...11f3` | `LONG` | 10,911,932.84 USD | `8,563.08` | `1246.56` | `1269.80` | `382.70` | 237,515.27 USD | `+2.18%` | `10X Cross` |
| `198` | `0x9ffd...ce40` | `LONG` | 10,702,479.92 USD | `8,417.87` | `1251.88` | `1269.80` | `598.44` | 164,331.00 USD | `+1.54%` | `5X Cross` |
| `199` | `0xad59...ba81` | `SHORT` | 10,696,380.00 USD | `8,425.00` | `330.91` | `1269.80` | `2145.42` | -7,908,422.23 USD | `-73.94%` | `10X Cross` |
| `206` | `0xdd53...2b13` | `SHORT` | 10,405,540.03 USD | `8,195.92` | `741.54` | `1269.80` | `8440.55` | -4,327,943.67 USD | `-41.59%` | `3X Cross` |
| `225` | `0x880a...311c` | `SHORT` | 9,790,341.83 USD | `7,707.11` | `1367.50` | `1269.80` | `2273.10` | 749,142.37 USD | `+7.65%` | `10X Cross` |
| `236` | `0xbf73...5d58` | `LONG` | 9,557,250.00 USD | `7,500.00` | `1248.78` | `1269.80` | `122.60` | 191,404.38 USD | `+2.00%` | `10X Cross` |
| `268` | `0x2b61...2f6c` | `LONG` | 8,674,840.80 USD | `6,807.00` | `1453.56` | `1269.80` | `576.63` | -1,219,510.42 USD | `-14.06%` | `10X Cross` |
| `285` | `0x2ae5...83e7` | `LONG` | 8,173,448.64 USD | `6,436.80` | `1391.82` | `1269.80` | `0.000000` | -785,443.35 USD | `-9.61%` | `1X Cross` |
| `330` | `0x26b6...9a13` | `LONG` | 6,914,964.80 USD | `5,433.73` | `1282.23` | `1269.80` | `232.05` | -52,338.44 USD | `-0.76%` | `10X Cross` |
| `331` | `0xecb6...2b00` | `SHORT` | 6,788,659.10 USD | `5,344.98` | `1279.06` | `1269.80` | `6748.51` | 47,899.27 USD | `+0.71%` | `5X Cross` |
| `345` | `0x45d2...4029` | `SHORT` | 6,637,244.60 USD | `5,227.00` | `833.44` | `1269.80` | `8896.05` | -2,280,866.63 USD | `-34.36%` | `5X Cross` |
| `362` | `0xea00...a918` | `LONG` | 6,357,000.00 USD | `5,000.00` | `739.16` | `1269.80` | `0.000000` | 2,661,184.89 USD | `+41.86%` | `5X Cross` |
| `377` | `0xdd7a...8830` | `LONG` | 6,170,497.22 USD | `4,860.19` | `897.48` | `1269.80` | `783.56` | 1,808,593.55 USD | `+29.31%` | `10X Cross` |
| `418` | `0x469e...58a5` | `SHORT` | 5,293,499.33 USD | `4,163.52` | `1242.31` | `1269.80` | `1973.73` | -121,114.67 USD | `-2.29%` | `10X Cross` |
| `431` | `0x4cae...7c34` | `LONG` | 5,088,486.08 USD | `4,002.27` | `1169.72` | `1269.80` | `982.35` | 406,936.73 USD | `+8.00%` | `10X Cross` |
| `442` | `0xa61c...66b9` | `LONG` | 4,936,204.80 USD | `3,888.00` | `1148.34` | `1269.80` | `0.000000` | 471,462.66 USD | `+9.55%` | `10X Cross` |
| `454` | `0xd4c1...3d1d` | `SHORT` | 4,843,348.54 USD | `3,813.36` | `1292.50` | `1269.80` | `2353.37` | 85,422.72 USD | `+1.76%` | `10X Cross` |
| `467` | `0x9aa5...58af` | `SHORT` | 4,725,165.73 USD | `3,720.31` | `1205.51` | `1269.80` | `3669.41` | -240,278.93 USD | `-5.09%` | `10X Cross` |
| `473` | `0x0153...8052` | `SHORT` | 4,697,428.24 USD | `3,698.18` | `1307.82` | `1269.80` | `2504.86` | 139,142.51 USD | `+2.96%` | `1X Isolated` |
| `501` | `0xb122...e4ba` | `LONG` | 4,447,954.76 USD | `3,498.47` | `1265.25` | `1269.80` | `1098.21` | 21,503.23 USD | `+0.48%` | `10X Cross` |
| `533` | `0x382b...3e39` | `LONG` | 4,152,515.74 USD | `3,269.44` | `1215.08` | `1269.80` | `0.000000` | 179,885.74 USD | `+4.33%` | `10X Cross` |
| `537` | `0xd21d...90f1` | `LONG` | 4,126,200.00 USD | `3,250.00` | `1253.64` | `1269.80` | `876.08` | 51,858.27 USD | `+1.26%` | `4X Isolated` |
| `553` | `0x456f...cdf1` | `LONG` | 4,038,270.25 USD | `3,179.49` | `1267.80` | `1269.80` | `504.14` | 7,315.33 USD | `+0.18%` | `10X Cross` |
| `560` | `0x1338...c48e` | `LONG` | 4,000,405.99 USD | `3,149.43` | `1018.52` | `1269.80` | `820.37` | 792,660.44 USD | `+19.81%` | `4X Isolated` |
| `569` | `0x325e...9564` | `LONG` | 3,938,184.94 USD | `3,101.91` | `1298.07` | `1269.80` | `146.25` | -88,325.76 USD | `-2.24%` | `10X Cross` |
| `579` | `0xdbe0...d6d5` | `LONG` | 3,919,036.97 USD | `3,085.37` | `422.97` | `1269.80` | `338.69` | 2,614,032.48 USD | `+66.70%` | `3X Isolated` |
| `595` | `0x9c06...0560` | `SHORT` | 3,809,902.14 USD | `2,989.80` | `786.00` | `1269.80` | `2561.38` | -1,459,907.14 USD | `-38.32%` | `10X Cross` |
| `604` | `0x27c9...d65d` | `SHORT` | 3,761,883.79 USD | `2,961.88` | `1254.41` | `1269.80` | `1750.32` | -46,468.58 USD | `-1.24%` | `10X Cross` |
| `605` | `0x2e30...4cb5` | `SHORT` | 3,755,683.52 USD | `2,956.30` | `1287.06` | `1269.80` | `2895.88` | 49,263.28 USD | `+1.31%` | `2X Cross` |
| `626` | `0x5323...b23c` | `SHORT` | 3,606,422.47 USD | `2,840.15` | `1267.49` | `1269.80` | `3200.73` | -6,560.80 USD | `-0.18%` | `5X Cross` |
| `681` | `0x71d0...8c26` | `SHORT` | 3,293,951.81 USD | `2,594.48` | `1266.76` | `1269.80` | `3596.80` | -7,380.76 USD | `-0.22%` | `10X Cross` |
| `698` | `0xac48...3201` | `LONG` | 3,218,802.25 USD | `2,531.50` | `1378.58` | `1269.80` | `553.40` | -271,070.03 USD | `-8.42%` | `10X Cross` |
| `701` | `0xa183...0482` | `LONG` | 3,217,673.20 USD | `2,534.00` | `530.25` | `1269.80` | `444.61` | 1,874,010.48 USD | `+58.24%` | `5X Isolated` |
| `706` | `0x0871...e927` | `LONG` | 3,186,000.00 USD | `2,500.00` | `1276.50` | `1269.80` | `0.000000` | -5,250.00 USD | `-0.16%` | `10X Cross` |
| `731` | `0x9b86...6e6e` | `LONG` | 3,127,405.68 USD | `2,463.30` | `637.58` | `1269.80` | `882.54` | 1,556,856.40 USD | `+49.78%` | `3X Cross` |
| `780` | `0xb2f7...af9f` | `SHORT` | 2,937,498.91 USD | `2,313.72` | `746.63` | `1269.80` | `4427.49` | -1,210,010.17 USD | `-41.19%` | `10X Cross` |
| `807` | `0xf48f...10fe` | `LONG` | 2,816,594.90 USD | `2,218.49` | `1517.87` | `1269.80` | `962.44` | -550,791.92 USD | `-19.56%` | `3X Cross` |
| `833` | `0x5bc4...3b0c` | `SHORT` | 2,705,613.65 USD | `2,130.74` | `1089.65` | `1269.80` | `3672.33` | -383,856.07 USD | `-14.19%` | `5X Cross` |
| `850` | `0x8de4...b9aa` | `SHORT` | 2,658,866.11 USD | `2,091.29` | `1331.35` | `1269.80` | `1689.99` | 125,373.60 USD | `+4.72%` | `3X Cross` |
| `854` | `0x4fe2...ac59` | `SHORT` | 2,639,801.65 USD | `2,071.57` | `1478.56` | `1269.80` | `1834.84` | 423,144.56 USD | `+16.03%` | `10X Cross` |
| `867` | `0xdf57...93f5` | `LONG` | 2,608,202.76 USD | `2,054.35` | `1227.36` | `1269.80` | `897.32` | 86,780.72 USD | `+3.33%` | `4X Isolated` |
| `872` | `0xbcd4...0dd2` | `LONG` | 2,582,264.83 USD | `2,033.92` | `1228.20` | `1269.80` | `793.44` | 84,214.02 USD | `+3.26%` | `10X Cross` |
| `882` | `0x9a99...d21a` | `LONG` | 2,548,600.00 USD | `2,000.00` | `1278.44` | `1269.80` | `0.000000` | -8,273.67 USD | `-0.32%` | `10X Cross` |
| `886` | `0xf29c...9971` | `LONG` | 2,539,600.00 USD | `2,000.00` | `1254.95` | `1269.80` | `0.000000` | 29,702.93 USD | `+1.17%` | `10X Cross` |
| `887` | `0x413c...886c` | `LONG` | 2,539,200.00 USD | `2,000.00` | `1237.51` | `1269.80` | `0.000000` | 64,176.87 USD | `+2.53%` | `10X Cross` |
| `904` | `0x77ee...2902` | `SHORT` | 2,480,020.63 USD | `1,946.03` | `759.84` | `1269.80` | `5465.53` | -1,001,343.13 USD | `-40.38%` | `10X Cross` |
| `918` | `0x3e2f...b269` | `SHORT` | 2,444,627.50 USD | `1,925.51` | `1134.87` | `1269.80` | `2977.26` | -259,428.64 USD | `-10.61%` | `10X Cross` |
| `928` | `0x4f12...618b` | `SHORT` | 2,410,930.39 USD | `1,896.28` | `1608.30` | `1269.80` | `2116.88` | 638,854.00 USD | `+26.50%` | `3X Cross` |
| `974` | `0x866d...d6e1` | `LONG` | 2,296,892.93 USD | `1,802.05` | `674.73` | `1269.80` | `159.49` | 1,080,991.62 USD | `+47.06%` | `10X Cross` |
| `997` | `0x2309...a2d9` | `LONG` | 2,230,496.49 USD | `1,750.37` | `1186.09` | `1269.80` | `812.26` | 154,402.38 USD | `+6.92%` | `8X Cross` |
| `1014` | `0x3205...40bb` | `SHORT` | 2,163,656.35 USD | `1,703.13` | `1256.96` | `1269.80` | `2084.93` | -22,886.10 USD | `-1.06%` | `10X Cross` |
| `1030` | `0x265e...7f70` | `LONG` | 2,104,812.28 USD | `1,651.74` | `1382.98` | `1269.80` | `0.000000` | -179,510.48 USD | `-8.53%` | `3X Cross` |
| `1043` | `0xfe7c...b7ae` | `SHORT` | 2,085,824.27 USD | `1,642.64` | `1346.92` | `1269.80` | `5658.91` | 126,684.35 USD | `+6.07%` | `10X Cross` |
| `1045` | `0x3e47...aaf6` | `LONG` | 2,077,421.09 USD | `1,636.28` | `1278.38` | `1269.80` | `1048.08` | -14,370.70 USD | `-0.69%` | `10X Cross` |
| `1047` | `0x2edd...8179` | `SHORT` | 2,075,203.69 USD | `1,633.89` | `1261.58` | `1269.80` | `2921.74` | -13,921.77 USD | `-0.67%` | `10X Cross` |
| `1058` | `0x7f75...9edf` | `LONG` | 2,053,751.08 USD | `1,611.67` | `1200.24` | `1269.80` | `983.37` | 119,367.10 USD | `+5.81%` | `10X Cross` |
| `1074` | `0x6646...6de5` | `SHORT` | 2,032,640.00 USD | `1,600.00` | `660.64` | `1269.80` | `4290.09` | -975,615.03 USD | `-48.00%` | `10X Cross` |
| `1078` | `0x023a...2355` | `SHORT` | 2,025,682.49 USD | `1,594.90` | `1310.00` | `1269.80` | `4449.16` | 63,629.65 USD | `+3.14%` | `10X Cross` |
| `1099` | `0xfc27...9d9d` | `SHORT` | 1,990,725.00 USD | `1,567.50` | `1296.12` | `1269.80` | `12367.39` | 40,939.56 USD | `+2.06%` | `10X Cross` |
| `1105` | `0xab59...59b5` | `LONG` | 1,987,330.27 USD | `1,565.32` | `1342.15` | `1269.80` | `828.33` | -113,564.95 USD | `-5.71%` | `10X Cross` |
| `1162` | `0xcf67...eb24` | `LONG` | 1,907,100.00 USD | `1,500.00` | `887.05` | `1269.80` | `633.75` | 576,528.63 USD | `+30.23%` | `10X Cross` |
| `1172` | `0xb695...a92d` | `LONG` | 1,883,558.30 USD | `1,483.00` | `1249.80` | `1269.80` | `0.000000` | 30,099.44 USD | `+1.60%` | `10X Cross` |
| `1178` | `0x7277...0b98` | `SHORT` | 1,873,586.81 USD | `1,475.73` | `1287.86` | `1269.80` | `2163.28` | 26,945.31 USD | `+1.44%` | `10X Cross` |
| `1191` | `0x039c...0ebd` | `SHORT` | 1,853,215.61 USD | `1,459.11` | `1244.17` | `1269.80` | `3305.67` | -37,829.64 USD | `-2.04%` | `10X Cross` |
| `1244` | `0x2ab7...c2f8` | `LONG` | 1,779,207.90 USD | `1,400.51` | `813.26` | `1269.80` | `790.93` | 640,226.22 USD | `+35.98%` | `3X Cross` |
| `1255` | `0xe35c...a1d3` | `LONG` | 1,763,677.54 USD | `1,389.16` | `1311.66` | `1269.80` | `690.78` | -58,425.18 USD | `-3.31%` | `2X Isolated` |
| `1265` | `0x11be...8b1d` | `LONG` | 1,747,441.68 USD | `1,375.83` | `1206.55` | `1269.80` | `1134.59` | 87,433.73 USD | `+5.00%` | `10X Isolated` |
| `1339` | `0xe065...0f85` | `SHORT` | 1,608,943.92 USD | `1,262.61` | `1087.02` | `1269.80` | `1582.64` | -236,467.80 USD | `-14.70%` | `10X Cross` |
| `1418` | `0x266b...efcb` | `LONG` | 1,528,920.00 USD | `1,200.00` | `893.76` | `1269.80` | `393.57` | 456,410.30 USD | `+29.85%` | `10X Cross` |
| `1422` | `0x5975...9abd` | `LONG` | 1,524,120.00 USD | `1,200.00` | `1179.54` | `1269.80` | `489.39` | 108,677.21 USD | `+7.13%` | `5X Cross` |
| `1441` | `0x2847...d47b` | `LONG` | 1,506,681.53 USD | `1,186.27` | `1232.07` | `1269.80` | `0.000000` | 45,113.03 USD | `+2.99%` | `5X Cross` |
| `1461` | `0x69cc...14fd` | `SHORT` | 1,474,578.79 USD | `1,161.36` | `675.33` | `1269.80` | `7997.85` | -690,273.26 USD | `-46.81%` | `10X Cross` |
| `1479` | `0x3fc5...c0c1` | `SHORT` | 1,458,518.80 USD | `1,148.44` | `1264.34` | `1269.80` | `2662.56` | -6,505.02 USD | `-0.45%` | `10X Cross` |
| `1495` | `0x38f9...cb04` | `SHORT` | 1,444,535.53 USD | `1,137.34` | `1252.77` | `1269.80` | `2002.61` | -19,709.83 USD | `-1.36%` | `10X Cross` |
| `1518` | `0x5f94...4b96` | `LONG` | 1,415,946.79 USD | `1,115.27` | `538.00` | `1269.80` | `0.000000` | 815,929.16 USD | `+57.62%` | `10X Cross` |
| `1533` | `0x9e7e...0047` | `LONG` | 1,397,093.23 USD | `1,100.42` | `1283.06` | `1269.80` | `1195.33` | -14,812.50 USD | `-1.06%` | `10X Cross` |
| `1534` | `0x71df...a23d` | `SHORT` | 1,396,353.19 USD | `1,098.28` | `513.50` | `1269.80` | `2559.70` | -832,383.00 USD | `-59.61%` | `2X Cross` |
| `1565` | `0xbfc7...80b4` | `SHORT` | 1,369,980.00 USD | `1,075.00` | `558.03` | `1269.80` | `2660.76` | -770,101.27 USD | `-56.21%` | `10X Cross` |
| `1604` | `0xdf83...3cff` | `SHORT` | 1,316,270.50 USD | `1,036.76` | `1260.83` | `1269.80` | `1893.87` | -9,096.63 USD | `-0.69%` | `10X Cross` |
| `1643` | `0x123d...3bff` | `SHORT` | 1,284,136.92 USD | `1,011.45` | `494.46` | `1269.80` | `4364.55` | -784,016.82 USD | `-61.05%` | `10X Cross` |
| `1658` | `0x668c...ea2e` | `SHORT` | 1,270,100.00 USD | `1,000.00` | `1406.98` | `1269.80` | `4208.44` | 136,881.99 USD | `+10.78%` | `10X Cross` |
| `1660` | `0xe282...df29` | `LONG` | 1,269,600.00 USD | `1,000.00` | `420.99` | `1269.80` | `800.01` | 848,613.14 USD | `+66.84%` | `10X Cross` |
| `1681` | `0x17f0...094f` | `LONG` | 1,251,439.02 USD | `984.30` | `1287.23` | `1269.80` | `536.94` | -15,581.14 USD | `-1.25%` | `5X Cross` |
| `1699` | `0x51f6...2b39` | `SHORT` | 1,235,565.98 USD | `972.81` | `1299.77` | `1269.80` | `2553.33` | 28,861.72 USD | `+2.34%` | `10X Cross` |
| `1761` | `0x757d...94ba` | `LONG` | 1,174,380.00 USD | `925.00` | `1558.31` | `1269.80` | `0.000000` | -267,060.59 USD | `-22.74%` | `10X Cross` |
| `1765` | `0xaa82...9556` | `LONG` | 1,173,367.86 USD | `924.13` | `1254.72` | `1269.80` | `179.88` | 13,841.18 USD | `+1.18%` | `10X Cross` |
| `1789` | `0x2577...4897` | `SHORT` | 1,149,338.89 USD | `904.92` | `1272.29` | `1269.80` | `4822.57` | 1,979.47 USD | `+0.17%` | `10X Cross` |
| `1803` | `0xb911...5525` | `LONG` | 1,144,350.00 USD | `900.00` | `1294.82` | `1269.80` | `1035.37` | -20,987.82 USD | `-1.83%` | `10X Cross` |
| `1853` | `0xcf0a...856f` | `LONG` | 1,110,106.45 USD | `871.15` | `1292.19` | `1269.80` | `1011.46` | -15,588.40 USD | `-1.40%` | `4X Cross` |
| `1858` | `0xef96...9383` | `SHORT` | 1,102,980.24 USD | `868.42` | `1259.08` | `1269.80` | `5314.61` | -9,568.45 USD | `-0.87%` | `10X Cross` |
| `1880` | `0xdf95...7d72` | `SHORT` | 1,083,652.90 USD | `853.27` | `1074.39` | `1269.80` | `44374.61` | -166,905.46 USD | `-15.40%` | `10X Cross` |
| `1913` | `0x601c...4f54` | `SHORT` | 1,050,805.73 USD | `824.42` | `615.11` | `1269.80` | `3077.10` | -543,692.98 USD | `-51.74%` | `5X Cross` |
| `1936` | `0xae55...2236` | `LONG` | 1,038,023.41 USD | `817.47` | `1467.80` | `1269.80` | `0.000000` | -161,857.81 USD | `-15.59%` | `10X Cross` |
| `1968` | `0x11ee...1d1d` | `SHORT` | 1,019,440.00 USD | `800.00` | `1269.65` | `1269.80` | `1598.70` | -3,716.99 USD | `-0.36%` | `5X Cross` |
| `1977` | `0x0f02...5384` | `LONG` | 1,016,750.37 USD | `800.78` | `1290.36` | `1269.80` | `300.79` | -16,543.70 USD | `-1.63%` | `3X Cross` |
| `1981` | `0x9b0f...db40` | `LONG` | 1,016,320.00 USD | `800.00` | `1268.86` | `1269.80` | `792.49` | 1,230.24 USD | `+0.12%` | `10X Cross` |
| `1993` | `0xabdb...84ac` | `LONG` | 1,011,478.54 USD | `793.69` | `711.79` | `1269.80` | `664.51` | 446,538.17 USD | `+44.15%` | `3X Cross` |
| `2001` | `0x6e8f...4364` | `LONG` | 1,007,618.04 USD | `793.65` | `1260.00` | `1269.80` | `959.03` | 7,619.04 USD | `+0.76%` | `10X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `1234.70` | 3,481.85 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 3.48K USD at 1234.7000 USD [API] | `2026-10-29 02:35:52` |
| `ANNOUNCEMENT` | `INFO` | `1190.50` | 35.71 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 0.04K USD at 1190.5000 USD [API] | `2026-10-22 18:01:21` |
| `ANNOUNCEMENT` | `INFO` | `1615.00` | 500.65 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 0.50K USD at 1615.0000 USD [API] | `2026-09-26 21:18:11` |
| `ANNOUNCEMENT` | `INFO` | `1615.00` | 8,075.00 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 8.07K USD at 1615.0000 USD [API] | `2026-09-26 21:18:11` |
| `ANNOUNCEMENT` | `INFO` | `1615.00` | 403.75 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 0.40K USD at 1615.0000 USD [API] | `2026-09-26 21:18:11` |
| `ANNOUNCEMENT` | `INFO` | `1615.00` | 18,766.30 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 18.77K USD at 1615.0000 USD [API] | `2026-09-26 21:18:11` |
| `ANNOUNCEMENT` | `INFO` | `1615.00` | 40,375.00 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 40.38K USD at 1615.0000 USD [API] | `2026-09-26 21:18:11` |
| `ANNOUNCEMENT` | `INFO` | `1615.00` | 161.50 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 0.16K USD at 1615.0000 USD [API] | `2026-09-26 21:18:11` |
| `ANNOUNCEMENT` | `INFO` | `1614.90` | 3,100.61 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 3.10K USD at 1614.9000 USD [API] | `2026-09-26 21:18:11` |
| `ANNOUNCEMENT` | `INFO` | `1614.90` | 6,411.15 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 6.41K USD at 1614.9000 USD [API] | `2026-09-26 21:18:11` |
| `ANNOUNCEMENT` | `INFO` | `1614.90` | 209.94 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 0.21K USD at 1614.9000 USD [API] | `2026-09-26 21:18:11` |
| `ANNOUNCEMENT` | `INFO` | `1614.90` | 161.49 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 0.16K USD at 1614.9000 USD [API] | `2026-09-26 21:18:11` |
| `ANNOUNCEMENT` | `INFO` | `1614.80` | 500.59 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 0.50K USD at 1614.8000 USD [API] | `2026-09-26 21:18:11` |
| `ANNOUNCEMENT` | `INFO` | `1233.00` | 17,249.67 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 17.25K USD at 1233.0000 USD [API] | `2026-10-29 03:25:29` |
| `ANNOUNCEMENT` | `INFO` | `1233.10` | 2,638.83 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 2.64K USD at 1233.1000 USD [API] | `2026-10-29 03:25:29` |
| `ANNOUNCEMENT` | `INFO` | `1237.60` | 284.65 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 0.28K USD at 1237.6000 USD [API] | `2026-10-29 02:31:04` |
| `ANNOUNCEMENT` | `INFO` | `1237.60` | 185.64 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 0.19K USD at 1237.6000 USD [API] | `2026-10-29 02:31:04` |
| `ANNOUNCEMENT` | `INFO` | `1237.60` | 61.88 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 0.06K USD at 1237.6000 USD [API] | `2026-10-29 02:31:04` |
| `ANNOUNCEMENT` | `INFO` | `655.00` | 9,602.30 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 9.60K USD at 655.0000 USD [API] | `2025-11-07 14:41:41` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`1404.55` (Vol: 3,000,000.00 USD, Dist: `+10.33%`) | Long MP=`1176.48` (Vol: 3,400,000.00 USD, Dist: `--7.58%`)
  * 48H Horizon: Short MP=`1404.55` (Vol: 3,000,000.00 USD, Dist: `+10.33%`) | Long MP=`1176.48` (Vol: 3,400,000.00 USD, Dist: `--7.58%`)
  * 3D Horizon: Short MP=`1404.55` (Vol: 3,000,000.00 USD, Dist: `+10.33%`) | Long MP=`1176.48` (Vol: 3,400,000.00 USD, Dist: `--7.58%`)
  * 7D Horizon: Short MP=`1404.10` (Vol: 3,000,000.00 USD, Dist: `+10.30%`) | Long MP=`1176.74` (Vol: 4,900,000.00 USD, Dist: `--7.56%`)
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
| `5m` | `BALANCED` | 0.00 USD | 1,750.00 USD | 1,750.00 USD | 1,750.00 USD | `1` | `2026-10-30 06:00:00 UTC - 2026-10-30 06:05:00 UTC` |
| `15m` | `BALANCED` | 0.00 USD | 1,750.00 USD | 1,750.00 USD | 1,750.00 USD | `1` | `2026-10-30 06:00:00 UTC - 2026-10-30 06:15:00 UTC` |
| `1h` | `BALANCED` | 0.00 USD | 1,750.00 USD | 1,750.00 USD | 1,750.00 USD | `1` | `2026-10-30 06:00:00 UTC - 2026-10-30 07:00:00 UTC` |
| `4h` | `BALANCED` | 0.00 USD | 1,750.00 USD | 1,750.00 USD | 1,750.00 USD | `1` | `2026-10-30 04:00:00 UTC - 2026-10-30 08:00:00 UTC` |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `0 USD` | Total OI Tokens: `-`
  * 1h OI Change: `0.00%` | 4h OI Change: `0.00%` | 24h OI Change: `0.00%`
  * Exchange Breakdown: Binance=`-` | Bybit=`-` | OKX=`-` | Hyperliquid=`-`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `78.08K` | Last 24h: `134.73K` | Last 3d: `246.48K` | Last 7d: `772.71K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0084%` | **USDT OKX** | `0.0100%` |
| **USDT Bybit** | `0.0100%` | **USDT KuCoin** | `0.0100%` |
| **USDT MEXC** | `0.0085%` | **USDT BingX** | `0.0100%` |
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
| `5:00 UTC` | `1279.95` | `1280.45` | `1279.95` | `1287.45` | `1275.15` | 19,925,691.14 USD | 8,662,599.23 USD | 11,263,091.92 USD | -2,600,492.69 USD | `-13.05%` | `1B / 6S` |
| `0:00 UTC` | `1275.15` | `1271.95` | `1275.15` | `1279.35` | `1264.95` | 23,738,198.29 USD | 11,363,344.84 USD | 12,374,853.45 USD | -1,011,508.62 USD | `-4.26%` | `3B / 3S` |
| `5:00 UTC` | `1279.05` | `1280.95` | `1279.05` | `1287.45` | `1274.25` | 14,930,858.33 USD | 7,292,403.22 USD | 7,638,455.11 USD | -346,051.88 USD | `-2.32%` | `2B / 4S` |
| `0:00 UTC` | `1285.05` | `1286.06` | `1285.05` | `1289.85` | `1282.05` | 15,953,463.93 USD | 6,542,642.51 USD | 9,410,821.42 USD | -2,868,178.91 USD | `-17.98%` | `1B / 3S` |
| `5:00 UTC` | `1276.95` | `1279.23` | `1276.95` | `1286.25` | `1275.15` | 15,449,899.62 USD | 6,063,485.10 USD | 9,386,414.52 USD | -3,322,929.42 USD | `-21.51%` | `0B / 8S` |
| `0:00 UTC` | `1275.15` | `1278.02` | `1275.15` | `1285.05` | `1272.15` | 16,039,119.46 USD | 6,719,465.52 USD | 9,319,653.95 USD | -2,600,188.43 USD | `-16.21%` | `2B / 3S` |
| `5:00 UTC` | `1272.15` | `1274.44` | `1272.15` | `1278.75` | `1270.65` | 10,354,318.48 USD | 4,552,930.99 USD | 5,801,387.50 USD | -1,248,456.51 USD | `-12.06%` | `0B / 2S` |
| `0:00 UTC` | `1270.05` | `1270.86` | `1270.05` | `1275.75` | `1267.35` | 11,469,050.63 USD | 5,693,129.81 USD | 5,775,920.83 USD | -82,791.02 USD | `-0.72%` | `1B / 1S` |
| `5:00 UTC` | `1266.75` | `1270.68` | `1266.75` | `1276.95` | `1265.25` | 9,416,171.49 USD | 3,994,637.12 USD | 5,421,534.37 USD | -1,426,897.25 USD | `-15.15%` | `0B / 7S` |
| `0:00 UTC` | `1268.55` | `1267.87` | `1268.55` | `1268.55` | `1266.75` | 220,928.05 USD | 104,625.77 USD | 116,302.28 USD | -11,676.51 USD | `-5.29%` | `1B / 1S` |

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
| `5m` | 16,290.00 USD | -1,840,000.00 USD | **`DISTRIBUTION`** |
| `15m` | -257,330.00 USD | -7,010,000.00 USD | **`DISTRIBUTION`** |
| `30m` | -78,290.00 USD | -7,220,000.00 USD | **`DISTRIBUTION`** |
| `1h` | -441,520.00 USD | -8,770,000.00 USD | **`DISTRIBUTION`** |
| `2h` | -481,030.00 USD | -14,160,000.00 USD | **`DISTRIBUTION`** |
| `4h` | 3,400,000.00 USD | -3,690,000.00 USD | **`DISTRIBUTION`** |
| `6h` | 595,670.00 USD | 3,870,000.00 USD | **`ACCUMULATION`** |
| `8h` | -1,010,000.00 USD | 14,410,000.00 USD | **`ACCUMULATION`** |
| `12h` | -10,470,000.00 USD | -20,000,000.00 USD | **`DISTRIBUTION`** |
| `24h` | 15,460,000.00 USD | 90,610,000.00 USD | **`ACCUMULATION`** |
| `1w` | 35,510,000.00 USD | 214,480,000.00 USD | **`ACCUMULATION`** |
| `30d` | 60,270,000.00 USD | -524,300,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+16.29K` | 15m=`-257.33K` | 1h=`-441.52K` | 24h=`+15.46M`
* Futures Capital Netflows: 5m=`-1.84M` | 15m=`-7.01M` | 1h=`-8.77M` | 24h=`+90.61M`
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
  * `2026-10-30 11:03:56 IST`: [kitco.com] - (Sentiment: `Neutral`)
  * `2026-10-30 11:28:56 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 11:27:56 IST`: [forex.com] - (Sentiment: `Neutral`)
  * `2026-10-30 11:27:56 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 11:27:56 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 08:29:56 IST`: [financemagnates.com] - (Sentiment: `Neutral`)
  * `2026-10-30 07:29:56 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-30 07:29:56 IST`: [kathleenhays.substack.com] - (Sentiment: `Neutral`)
  * `2026-10-30 06:29:56 IST`: [rba.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 06:29:56 IST`: [abs.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 06:29:56 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 05:29:56 IST`: [@NodeWire] - (Sentiment: `Neutral`)
  * `2026-10-30 05:29:56 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 05:29:56 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 05:29:56 IST`: [@financialjuice] - (Sentiment: `Neutral`)


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
  * Execution Entry: `1235.31` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `1215.00` (Risk Distance: `20.31` pts)
  * +2.5R Take Profit: `1286.08`
  * Mathematical Lot Sizing: **`0.49 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `1285.56` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `1305.87` (Risk Distance: `20.31` pts)
  * +2.5R Take Profit: `1234.79`
  * Mathematical Lot Sizing: **`0.49 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`1279.51`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
