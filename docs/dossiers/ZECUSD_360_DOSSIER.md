# 🏛️ SOVEREIGN CANDIDATE DOSSIER: ZECUSD
**Canonical Key**: `ZECUSD` | **Broker Instrument**: `ZECUSD.p` | **Asset Class**: `Crypto Altcoin`
**Timestamp**: `2026-10-30 01:20:51 IST` (`2026-10-29 19:50:51 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `1323.59` | **Live Ask Quote**: `1324.62` | **Mid Price**: `1324.11`
- **Spread Points**: `103.00` | **Spread BPS**: `7.78 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `1280.82` | VWAP Z-Score: `+0.99` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `15.41` (Volatility Regime: `HIGH_EXPANSION`)
  * 14-Period RSI: `51.38` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `1397.32` | Lower -3.00σ Band: `1164.32`
  * Upper +2.51σ Band: `1378.29` | Lower -2.51σ Band: `1183.35`
  * Upper +2.01σ Band: `1358.87` | Lower -2.01σ Band: `1202.77`
  * Upper +2.00σ Band: `1358.48` | Lower -2.00σ Band: `1203.16`
  * Upper +1.28σ Band: `1330.52` | Lower -1.28σ Band: `1231.11`
  * Upper +1.00σ Band: `1319.65` | Lower -1.00σ Band: `1241.99`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`1325.40` | EMA-20=`1322.21` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`1301.96` (Slope: `+0.0000`) | EMA-100=`1290.40`
  * Institutional Anchors: EMA-144=`1285.34` | EMA-200=`1280.39` (Slope: `+0.5212`) | EMA-233=`1278.02`
- **Range Boundaries**: 24H High=`1396.49` | 24H Low=`1230.00` | Weekly High=`1396.49` | Weekly Low=`1210.62`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `1308.25` (Distance: `+1.23%`)
  * Point of Control (POC) = `1247.20` (Distance: `+6.19%`)
  * Value Area Low (VAL) = `1230.55` (Distance: `+7.63%`)
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
  * Golden Pocket Zone (0.618 - 0.650): `1318.81` - `1329.40`
  * Optimal Trade Entry (OTE 0.705): `1326.75`
  * Structural Invalidation Anchor (0.786): `1334.70`

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
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 01:14:07 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `16` | `0xb83d...6e36` | `SHORT` | 69,682,355.50 USD | `52,582.52` | `1336.45` | `1323.80` | `3705.80` | 591,559.39 USD | `+0.85%` | `3X Cross` |
| `24` | `0x5b5d...c060` | `SHORT` | 53,943,719.45 USD | `40,727.61` | `1478.36` | `1323.80` | `5001.76` | 6,266,544.75 USD | `+11.62%` | `3X Cross` |
| `41` | `0x7fda...17d1` | `SHORT` | 29,692,926.34 USD | `22,423.02` | `1261.42` | `1323.80` | `2819.01` | -1,408,113.90 USD | `-4.74%` | `5X Cross` |
| `77` | `0x60b0...991e` | `LONG` | 22,236,511.45 USD | `16,779.74` | `1179.65` | `1323.80` | `891.38` | 2,442,264.43 USD | `+10.98%` | `10X Cross` |
| `82` | `0xbf73...5d58` | `LONG` | 21,192,000.00 USD | `16,000.00` | `1214.30` | `1323.80` | `726.42` | 1,763,167.75 USD | `+8.32%` | `10X Cross` |
| `132` | `0xc36a...105b` | `LONG` | 15,252,987.58 USD | `11,510.82` | `1215.14` | `1323.80` | `933.04` | 1,265,706.55 USD | `+8.30%` | `10X Cross` |
| `169` | `0x8742...8427` | `LONG` | 12,198,964.22 USD | `9,201.21` | `1286.37` | `1323.80` | `698.35` | 362,794.22 USD | `+2.97%` | `10X Cross` |
| `176` | `0x9071...5c0b` | `LONG` | 11,706,734.45 USD | `8,829.94` | `1370.53` | `1323.80` | `579.50` | -394,954.20 USD | `-3.37%` | `2X Cross` |
| `191` | `0xad59...ba81` | `SHORT` | 11,164,810.00 USD | `8,425.00` | `330.91` | `1323.80` | `2140.16` | -8,376,852.23 USD | `-75.03%` | `10X Cross` |
| `199` | `0xdd53...2b13` | `SHORT` | 10,912,022.30 USD | `8,231.14` | `739.37` | `1323.80` | `7879.08` | -4,826,140.82 USD | `-44.23%` | `3X Cross` |
| `200` | `0x9ffd...ce40` | `LONG` | 10,845,562.29 USD | `8,188.42` | `1254.09` | `1323.80` | `568.52` | 576,544.45 USD | `+5.32%` | `5X Cross` |
| `215` | `0xfc66...ca06` | `SHORT` | 10,280,843.80 USD | `7,763.72` | `1319.72` | `1323.80` | `5602.27` | -34,878.71 USD | `-0.34%` | `10X Cross` |
| `221` | `0x880a...311c` | `SHORT` | 10,220,398.57 USD | `7,707.11` | `1367.50` | `1323.80` | `2306.93` | 319,085.63 USD | `+3.12%` | `10X Cross` |
| `267` | `0x2b61...2f6c` | `LONG` | 9,018,230.13 USD | `6,807.00` | `1453.56` | `1323.80` | `636.82` | -876,121.10 USD | `-9.72%` | `10X Cross` |
| `285` | `0x2ae5...83e7` | `LONG` | 8,533,909.44 USD | `6,436.80` | `1391.82` | `1323.80` | `344.63` | -424,982.55 USD | `-4.98%` | `2X Cross` |
| `330` | `0x26b6...9a13` | `LONG` | 7,204,039.23 USD | `5,433.73` | `1282.23` | `1323.80` | `208.00` | 236,736.00 USD | `+3.29%` | `10X Cross` |
| `332` | `0xecb6...2b00` | `SHORT` | 7,179,794.30 USD | `5,421.92` | `1324.05` | `1323.80` | `6143.12` | -886.97 USD | `-0.01%` | `5X Cross` |
| `342` | `0x45d2...4029` | `SHORT` | 6,929,956.60 USD | `5,227.00` | `833.44` | `1323.80` | `8021.19` | -2,573,578.63 USD | `-37.14%` | `5X Cross` |
| `360` | `0xea00...a918` | `LONG` | 6,626,000.00 USD | `5,000.00` | `739.16` | `1323.80` | `0.000000` | 2,930,184.89 USD | `+44.22%` | `5X Cross` |
| `375` | `0xdd7a...8830` | `LONG` | 6,441,695.83 USD | `4,860.19` | `897.48` | `1323.80` | `783.87` | 2,079,792.15 USD | `+32.29%` | `10X Cross` |
| `383` | `0xf081...e39e` | `LONG` | 6,247,666.50 USD | `4,717.00` | `1195.70` | `1323.80` | `1200.09` | 607,542.45 USD | `+9.72%` | `10X Cross` |
| `435` | `0x4cae...7c34` | `LONG` | 5,304,575.69 USD | `4,004.36` | `999.34` | `1323.80` | `768.40` | 1,302,847.54 USD | `+24.56%` | `10X Cross` |
| `446` | `0xa61c...66b9` | `LONG` | 5,153,155.20 USD | `3,888.00` | `1148.34` | `1323.80` | `0.000000` | 688,413.06 USD | `+13.36%` | `10X Cross` |
| `447` | `0x382b...3e39` | `LONG` | 5,150,525.67 USD | `3,889.49` | `1200.39` | `1323.80` | `0.000000` | 481,636.79 USD | `+9.35%` | `10X Cross` |
| `468` | `0x9aa5...58af` | `SHORT` | 4,927,021.94 USD | `3,720.31` | `1205.51` | `1323.80` | `3331.98` | -442,135.14 USD | `-8.97%` | `10X Cross` |
| `473` | `0x0153...8052` | `SHORT` | 4,903,047.04 USD | `3,698.18` | `1307.82` | `1323.80` | `2504.69` | -66,476.30 USD | `-1.36%` | `1X Isolated` |
| `502` | `0xd4c1...3d1d` | `SHORT` | 4,578,861.53 USD | `3,457.79` | `1302.97` | `1323.80` | `2693.32` | -73,448.71 USD | `-1.60%` | `10X Cross` |
| `527` | `0xd21d...90f1` | `LONG` | 4,306,900.00 USD | `3,250.00` | `1253.64` | `1323.80` | `875.88` | 232,558.27 USD | `+5.40%` | `4X Isolated` |
| `547` | `0x1338...c48e` | `LONG` | 4,171,105.09 USD | `3,149.43` | `1018.52` | `1323.80` | `820.17` | 963,359.55 USD | `+23.10%` | `4X Isolated` |
| `551` | `0x456f...cdf1` | `LONG` | 4,153,322.57 USD | `3,134.11` | `1268.52` | `1323.80` | `493.31` | 177,632.94 USD | `+4.28%` | `10X Cross` |
| `560` | `0x27c9...d65d` | `SHORT` | 4,093,018.47 USD | `3,090.47` | `1252.51` | `1323.80` | `1800.28` | -222,186.78 USD | `-5.43%` | `10X Cross` |
| `561` | `0xdbe0...d6d5` | `LONG` | 4,090,583.55 USD | `3,085.37` | `422.97` | `1323.80` | `338.49` | 2,785,579.05 USD | `+68.10%` | `3X Isolated` |
| `585` | `0x9c06...0560` | `SHORT` | 3,959,990.10 USD | `2,989.80` | `786.00` | `1323.80` | `2370.67` | -1,609,995.10 USD | `-40.66%` | `10X Cross` |
| `645` | `0x2e30...4cb5` | `SHORT` | 3,586,368.55 USD | `2,705.06` | `1301.01` | `1323.80` | `2991.22` | -67,071.69 USD | `-1.87%` | `2X Cross` |
| `688` | `0xac48...3201` | `LONG` | 3,367,929.74 USD | `2,540.30` | `1393.86` | `1323.80` | `534.42` | -172,899.55 USD | `-5.13%` | `10X Cross` |
| `691` | `0xa183...0482` | `LONG` | 3,359,577.20 USD | `2,534.00` | `530.25` | `1323.80` | `444.42` | 2,015,914.48 USD | `+60.01%` | `5X Isolated` |
| `698` | `0x325e...9564` | `LONG` | 3,316,727.80 USD | `2,501.91` | `1306.24` | `1323.80` | `0.000000` | 48,633.89 USD | `+1.47%` | `10X Cross` |
| `699` | `0x0871...e927` | `LONG` | 3,312,116.25 USD | `2,500.00` | `1276.50` | `1323.80` | `0.000000` | 120,866.25 USD | `+3.65%` | `10X Cross` |
| `710` | `0x9b86...6e6e` | `LONG` | 3,271,146.34 USD | `2,467.30` | `637.58` | `1323.80` | `889.64` | 1,698,046.74 USD | `+51.91%` | `3X Cross` |
| `770` | `0xb2f7...af9f` | `SHORT` | 3,066,141.74 USD | `2,313.72` | `746.63` | `1323.80` | `4176.55` | -1,338,653.00 USD | `-43.66%` | `10X Cross` |
| `784` | `0x634f...6951` | `LONG` | 3,009,497.38 USD | `2,272.42` | `1281.94` | `1323.80` | `1250.03` | 96,396.92 USD | `+3.20%` | `10X Cross` |
| `800` | `0xf48f...10fe` | `LONG` | 2,939,942.95 USD | `2,218.49` | `1517.87` | `1323.80` | `890.01` | -427,443.88 USD | `-14.54%` | `3X Cross` |
| `827` | `0x5bc4...3b0c` | `SHORT` | 2,824,722.02 USD | `2,130.74` | `1089.65` | `1323.80` | `3568.85` | -502,964.44 USD | `-17.81%` | `5X Cross` |
| `841` | `0x8de4...b9aa` | `SHORT` | 2,769,913.60 USD | `2,091.29` | `1331.35` | `1323.80` | `1689.81` | 14,326.10 USD | `+0.52%` | `3X Cross` |
| `844` | `0x4fe2...ac59` | `SHORT` | 2,745,300.70 USD | `2,071.57` | `1478.56` | `1323.80` | `1814.14` | 317,645.51 USD | `+11.57%` | `10X Cross` |
| `863` | `0x668c...ea2e` | `SHORT` | 2,648,715.80 USD | `2,000.00` | `1406.98` | `1323.80` | `2702.07` | 165,248.19 USD | `+6.24%` | `10X Cross` |
| `888` | `0x77ee...2902` | `SHORT` | 2,577,905.94 USD | `1,946.03` | `759.84` | `1323.80` | `5158.60` | -1,099,228.43 USD | `-42.64%` | `10X Cross` |
| `898` | `0x3e2f...b269` | `SHORT` | 2,552,648.61 USD | `1,925.51` | `1134.87` | `1323.80` | `2931.74` | -367,449.75 USD | `-14.39%` | `10X Cross` |
| `906` | `0xe097...d0fe` | `LONG` | 2,536,997.85 USD | `1,913.56` | `1261.17` | `1323.80` | `0.000000` | 123,671.68 USD | `+4.87%` | `10X Cross` |
| `914` | `0x4f12...618b` | `SHORT` | 2,511,622.86 USD | `1,896.28` | `1608.30` | `1323.80` | `2116.70` | 538,161.53 USD | `+21.43%` | `3X Cross` |
| `955` | `0x866d...d6e1` | `LONG` | 2,387,175.63 USD | `1,802.05` | `674.73` | `1323.80` | `93.72` | 1,171,274.32 USD | `+49.07%` | `10X Cross` |
| `990` | `0x2309...a2d9` | `LONG` | 2,318,116.34 USD | `1,750.37` | `1186.09` | `1323.80` | `805.92` | 242,022.23 USD | `+10.44%` | `8X Cross` |
| `1006` | `0x023a...2355` | `SHORT` | 2,255,444.76 USD | `1,703.23` | `1313.35` | `1323.80` | `6088.66` | -18,506.16 USD | `-0.82%` | `10X Cross` |
| `1012` | `0x2edd...8179` | `SHORT` | 2,245,464.58 USD | `1,695.33` | `1261.35` | `1323.80` | `2985.71` | -107,063.62 USD | `-4.77%` | `10X Cross` |
| `1039` | `0x3e47...aaf6` | `LONG` | 2,168,398.26 USD | `1,636.28` | `1279.54` | `1323.80` | `1037.26` | 74,706.17 USD | `+3.45%` | `10X Cross` |
| `1041` | `0xa271...a3f7` | `LONG` | 2,162,015.25 USD | `1,631.43` | `1190.60` | `1323.80` | `910.27` | 219,633.44 USD | `+10.16%` | `4X Cross` |
| `1055` | `0x7f75...9edf` | `LONG` | 2,126,855.61 USD | `1,605.78` | `1199.97` | `1323.80` | `973.74` | 199,963.72 USD | `+9.40%` | `10X Cross` |
| `1060` | `0x265e...7f70` | `LONG` | 2,121,504.63 USD | `1,601.74` | `1388.09` | `1323.80` | `0.000000` | -101,860.38 USD | `-4.80%` | `3X Cross` |
| `1061` | `0x6646...6de5` | `SHORT` | 2,121,280.00 USD | `1,600.00` | `660.64` | `1323.80` | `4838.55` | -1,064,255.03 USD | `-50.17%` | `10X Cross` |
| `1075` | `0xdf57...93f5` | `LONG` | 2,094,287.83 USD | `1,579.76` | `1218.38` | `1323.80` | `780.12` | 169,531.85 USD | `+8.09%` | `3X Isolated` |
| `1091` | `0xab59...59b5` | `LONG` | 2,074,362.06 USD | `1,565.32` | `1342.15` | `1323.80` | `792.02` | -26,533.15 USD | `-1.28%` | `10X Cross` |
| `1092` | `0xfe7c...b7ae` | `SHORT` | 2,070,611.75 USD | `1,562.49` | `1350.62` | `1323.80` | `6496.22` | 39,717.30 USD | `+1.92%` | `10X Cross` |
| `1147` | `0xcf67...eb24` | `LONG` | 1,987,840.65 USD | `1,500.00` | `887.05` | `1323.80` | `552.43` | 657,269.28 USD | `+33.06%` | `10X Cross` |
| `1169` | `0x039c...0ebd` | `SHORT` | 1,962,833.64 USD | `1,480.49` | `1238.67` | `1323.80` | `3176.11` | -129,002.32 USD | `-6.57%` | `10X Cross` |
| `1200` | `0x71d0...8c26` | `SHORT` | 1,913,227.57 USD | `1,444.80` | `1361.12` | `1323.80` | `6483.04` | 53,318.89 USD | `+2.79%` | `10X Cross` |
| `1240` | `0xfc27...9d9d` | `SHORT` | 1,860,404.58 USD | `1,404.91` | `1317.50` | `1323.80` | `11322.60` | -9,436.62 USD | `-0.51%` | `10X Cross` |
| `1246` | `0x2ab7...c2f8` | `LONG` | 1,856,796.16 USD | `1,400.51` | `813.26` | `1323.80` | `796.45` | 717,814.47 USD | `+38.66%` | `3X Cross` |
| `1264` | `0x11be...8b1d` | `LONG` | 1,823,249.92 USD | `1,375.83` | `1206.55` | `1323.80` | `1134.40` | 163,241.96 USD | `+8.95%` | `10X Isolated` |
| `1306` | `0xdf83...3cff` | `SHORT` | 1,747,885.79 USD | `1,318.96` | `1247.06` | `1323.80` | `1854.17` | -103,059.70 USD | `-5.90%` | `10X Cross` |
| `1317` | `0xef96...9383` | `SHORT` | 1,734,483.73 USD | `1,308.82` | `1249.96` | `1323.80` | `4245.81` | -98,517.31 USD | `-5.68%` | `10X Cross` |
| `1364` | `0xe065...0f85` | `SHORT` | 1,673,244.99 USD | `1,262.61` | `1087.02` | `1323.80` | `1760.88` | -300,768.86 USD | `-17.98%` | `10X Cross` |
| `1388` | `0x7277...0b98` | `SHORT` | 1,637,186.47 USD | `1,234.96` | `1298.48` | `1323.80` | `2362.06` | -33,617.05 USD | `-2.05%` | `10X Cross` |
| `1433` | `0x5975...9abd` | `LONG` | 1,590,240.00 USD | `1,200.00` | `1179.54` | `1323.80` | `372.95` | 174,797.21 USD | `+10.99%` | `5X Cross` |
| `1477` | `0x69cc...14fd` | `SHORT` | 1,539,614.95 USD | `1,161.36` | `675.33` | `1323.80` | `7877.52` | -755,309.42 USD | `-49.06%` | `10X Cross` |
| `1478` | `0x7a76...b16d` | `LONG` | 1,536,264.60 USD | `1,159.27` | `1358.50` | `1323.80` | `1238.54` | -38,603.91 USD | `-2.51%` | `10X Cross` |
| `1492` | `0x3fc5...c0c1` | `SHORT` | 1,522,601.75 USD | `1,148.44` | `1264.34` | `1323.80` | `3088.94` | -70,587.98 USD | `-4.64%` | `10X Cross` |
| `1512` | `0xe35c...a1d3` | `LONG` | 1,493,805.32 USD | `1,127.06` | `1318.20` | `1323.80` | `694.32` | 8,109.97 USD | `+0.54%` | `2X Isolated` |
| `1519` | `0x5f94...4b96` | `LONG` | 1,477,955.80 USD | `1,115.27` | `538.00` | `1323.80` | `0.000000` | 877,938.17 USD | `+59.40%` | `10X Cross` |
| `1537` | `0x71df...a23d` | `SHORT` | 1,454,891.52 USD | `1,098.28` | `513.50` | `1323.80` | `2546.62` | -890,921.33 USD | `-61.24%` | `2X Cross` |
| `1565` | `0xbfc7...80b4` | `SHORT` | 1,423,684.74 USD | `1,075.00` | `558.03` | `1323.80` | `5449.87` | -823,806.02 USD | `-57.86%` | `10X Cross` |
| `1613` | `0x51f6...2b39` | `SHORT` | 1,377,025.94 USD | `1,039.88` | `1302.72` | `1323.80` | `2854.03` | -22,349.13 USD | `-1.62%` | `10X Cross` |
| `1643` | `0x123d...3bff` | `SHORT` | 1,336,000.38 USD | `1,008.15` | `489.25` | `1323.80` | `4210.92` | -842,766.31 USD | `-63.08%` | `10X Cross` |
| `1651` | `0x266b...efcb` | `LONG` | 1,325,800.00 USD | `1,000.00` | `826.11` | `1323.80` | `154.90` | 499,687.07 USD | `+37.69%` | `10X Cross` |
| `1652` | `0xb5ff...d912` | `LONG` | 1,325,800.00 USD | `1,000.00` | `1141.93` | `1323.80` | `400.44` | 183,869.70 USD | `+13.87%` | `2X Cross` |
| `1653` | `0x0748...d4b2` | `LONG` | 1,325,800.00 USD | `1,000.00` | `1334.09` | `1323.80` | `0.000000` | -8,288.30 USD | `-0.63%` | `7X Cross` |
| `1654` | `0xe282...df29` | `LONG` | 1,325,400.00 USD | `1,000.00` | `420.99` | `1323.80` | `107.25` | 904,413.14 USD | `+68.24%` | `10X Cross` |
| `1676` | `0x17f0...094f` | `LONG` | 1,304,099.07 USD | `984.30` | `1287.23` | `1323.80` | `536.75` | 37,078.91 USD | `+2.84%` | `5X Cross` |
| `1749` | `0x757d...94ba` | `LONG` | 1,226,272.50 USD | `925.00` | `1558.31` | `1323.80` | `0.000000` | -215,168.08 USD | `-17.55%` | `10X Cross` |
| `1800` | `0x2847...d47b` | `LONG` | 1,180,328.18 USD | `891.15` | `1238.34` | `1323.80` | `0.000000` | 76,778.77 USD | `+6.50%` | `5X Cross` |
| `1816` | `0xf096...7553` | `SHORT` | 1,166,977.22 USD | `881.07` | `1240.34` | `1323.80` | `3557.46` | -74,147.13 USD | `-6.35%` | `10X Cross` |
| `1818` | `0xdf95...7d72` | `SHORT` | 1,165,882.56 USD | `880.31` | `1073.82` | `1323.80` | `41411.65` | -220,584.26 USD | `-18.92%` | `10X Cross` |
| `1833` | `0xcf0a...856f` | `LONG` | 1,154,970.67 USD | `871.15` | `1292.19` | `1323.80` | `938.45` | 29,275.82 USD | `+2.53%` | `4X Cross` |
| `1863` | `0x7d0f...ea35` | `LONG` | 1,125,825.00 USD | `850.00` | `1317.57` | `1323.80` | `1260.02` | 5,889.42 USD | `+0.52%` | `10X Cross` |
| `1899` | `0x601c...4f54` | `SHORT` | 1,091,861.85 USD | `824.42` | `615.11` | `1323.80` | `2974.45` | -584,749.10 USD | `-53.56%` | `5X Cross` |
| `1907` | `0xae55...2236` | `LONG` | 1,083,801.73 USD | `817.47` | `1467.80` | `1323.80` | `0.000000` | -116,079.49 USD | `-10.71%` | `10X Cross` |
| `1912` | `0x71b1...79c8` | `LONG` | 1,077,140.13 USD | `812.52` | `1231.55` | `1323.80` | `702.28` | 76,484.68 USD | `+7.10%` | `10X Cross` |
| `1932` | `0x0f02...5384` | `LONG` | 1,061,576.67 USD | `800.78` | `1290.36` | `1323.80` | `290.85` | 28,282.60 USD | `+2.66%` | `3X Cross` |
| `1934` | `0x9b0f...db40` | `LONG` | 1,060,640.00 USD | `800.00` | `1268.86` | `1323.80` | `774.20` | 45,550.24 USD | `+4.29%` | `10X Cross` |
| `1944` | `0xabdb...84ac` | `LONG` | 1,051,718.62 USD | `793.69` | `711.79` | `1323.80` | `664.32` | 486,778.26 USD | `+46.28%` | `3X Cross` |
| `1950` | `0xfdf8...e381` | `LONG` | 1,047,395.26 USD | `790.01` | `1337.72` | `1323.80` | `403.21` | -9,414.43 USD | `-0.90%` | `10X Cross` |
| `2012` | `0x0c1f...1d39` | `SHORT` | 1,011,266.95 USD | `762.99` | `1299.17` | `1323.80` | `4922.71` | -20,015.86 USD | `-1.98%` | `10X Cross` |
| `2015` | `0xf6f3...47f8` | `SHORT` | 1,009,537.19 USD | `761.57` | `1253.10` | `1323.80` | `2388.61` | -55,214.20 USD | `-5.47%` | `5X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `1297.10` | 194.56 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Long: 0.19K USD at 1297.1000 USD [API] | `2026-10-27 15:46:39` |
| `ANNOUNCEMENT` | `INFO` | `1326.30` | 13.26 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Long: 0.01K USD at 1326.3000 USD [API] | `2026-10-27 23:06:56` |
| `ANNOUNCEMENT` | `INFO` | `1326.50` | 11,341.58 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Long: 11.34K USD at 1326.5000 USD [API] | `2026-10-27 23:06:49` |


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
  * Current Rate: `74.04K` | Last 24h: `32.07K` | Last 3d: `282.84K` | Last 7d: `777.72K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0061%` | **USDT OKX** | `0.0100%` |
| **USDT Bybit** | `0.0100%` | **USDT KuCoin** | `0.0100%` |
| **USDT MEXC** | `0.0061%` | **USDT BingX** | `0.0050%` |
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
| `0:00 UTC` | `1335.45` | `1342.97` | `1335.45` | `1354.95` | `1333.05` | 31,234,081.19 USD | 13,144,149.56 USD | 18,089,931.62 USD | -4,945,782.06 USD | `-15.83%` | `2B / 7S` |
| `5:00 UTC` | `1333.95` | `1332.65` | `1333.95` | `1338.15` | `1327.05` | 42,051,592.22 USD | 20,998,597.47 USD | 21,052,994.75 USD | -54,397.28 USD | `-0.13%` | `1B / 3S` |
| `0:00 UTC` | `1324.05` | `1326.61` | `1324.05` | `1336.05` | `1320.15` | 35,175,848.19 USD | 15,805,961.43 USD | 19,369,886.76 USD | -3,563,925.33 USD | `-10.13%` | `1B / 10S` |
| `5:00 UTC` | `1321.35` | `1325.74` | `1321.35` | `1333.35` | `1318.35` | 26,289,288.34 USD | 11,537,630.34 USD | 14,751,657.99 USD | -3,214,027.65 USD | `-12.23%` | `3B / 5S` |
| `0:00 UTC` | `1315.95` | `1314.40` | `1315.95` | `1321.95` | `1307.85` | 50,919,152.62 USD | 22,517,005.07 USD | 28,402,147.55 USD | -5,885,142.49 USD | `-11.56%` | `2B / 5S` |
| `5:00 UTC` | `1315.95` | `1319.00` | `1315.95` | `1325.85` | `1312.05` | 22,246,351.59 USD | 13,151,982.06 USD | 9,094,369.53 USD | 4,057,612.52 USD | `+18.24%` | `9B / 1S` |
| `0:00 UTC` | `1320.75` | `1319.74` | `1320.75` | `1325.25` | `1315.95` | 11,564,611.33 USD | 5,754,638.99 USD | 5,809,972.34 USD | -55,333.35 USD | `-0.48%` | `1B / 2S` |
| `5:00 UTC` | `1322.85` | `1320.89` | `1322.85` | `1324.95` | `1316.85` | 7,868,027.33 USD | 4,223,932.72 USD | 3,644,094.61 USD | 579,838.11 USD | `+7.37%` | `3B / 0S` |
| `0:00 UTC` | `1324.95` | `1324.41` | `1324.95` | `1327.05` | `1319.85` | 12,000,472.36 USD | 6,714,467.49 USD | 5,286,004.87 USD | 1,428,462.62 USD | `+11.90%` | `2B / 1S` |
| `5:00 UTC` | `1323.15` | `1323.90` | `1323.15` | `1328.25` | `1320.75` | 4,264,968.16 USD | 2,109,372.39 USD | 2,155,595.77 USD | -46,223.38 USD | `-1.08%` | `5B / 2S` |

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
| `5m` | 648,690.00 USD | 1,610,000.00 USD | **`ACCUMULATION`** |
| `15m` | 947,510.00 USD | 4,310,000.00 USD | **`ACCUMULATION`** |
| `30m` | 48,910.00 USD | 5,410,000.00 USD | **`ACCUMULATION`** |
| `1h` | 2,070,000.00 USD | 17,580,000.00 USD | **`ACCUMULATION`** |
| `2h` | 49,230.00 USD | -8,670,000.00 USD | **`DISTRIBUTION`** |
| `4h` | 14,950,000.00 USD | 33,710,000.00 USD | **`ACCUMULATION`** |
| `6h` | 30,160,000.00 USD | 100,410,000.00 USD | **`ACCUMULATION`** |
| `8h` | 32,730,000.00 USD | 106,880,000.00 USD | **`ACCUMULATION`** |
| `12h` | 29,480,000.00 USD | 120,550,000.00 USD | **`ACCUMULATION`** |
| `24h` | 12,600,000.00 USD | 81,300,000.00 USD | **`ACCUMULATION`** |
| `1w` | 49,190,000.00 USD | 257,380,000.00 USD | **`ACCUMULATION`** |
| `30d` | 68,510,000.00 USD | -501,990,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+648.69K` | 15m=`+947.51K` | 1h=`+2.07M` | 24h=`+12.60M`
* Futures Capital Netflows: 5m=`+1.61M` | 15m=`+4.31M` | 1h=`+17.58M` | 24h=`+81.30M`
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
  * `2026-10-30 00:57:53 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 00:47:53 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 01:18:53 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 01:18:53 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 01:18:53 IST`: [@DeItaone] - (Sentiment: `Neutral`)
  * `2026-10-30 01:17:53 IST`: [@mb_ghalibaf] - (Sentiment: `Neutral`)
  * `2026-10-30 01:17:53 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-30 01:17:53 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-30 01:17:53 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:19:53 IST`: [fxstreet.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:19:53 IST`: [ForexFactory] - (Sentiment: `Neutral`)
  * `2026-10-29 21:19:53 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-29 21:19:53 IST`: [youtube.com/bankofcanadaofficial] - (Sentiment: `Neutral`)
  * `2026-10-29 21:19:53 IST`: [notayesmanseconomics.wordpress.com] - (Sentiment: `Neutral`)
  * `2026-10-29 20:19:53 IST`: [think.ing.com] - (Sentiment: `Neutral`)


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
  * Spread-Padded Stop Loss: `1210.52` (Risk Distance: `20.03` pts)
  * +2.5R Take Profit: `1280.63`
  * Mathematical Lot Sizing: **`0.49 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `1308.25` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `1328.28` (Risk Distance: `20.03` pts)
  * +2.5R Take Profit: `1258.17`
  * Mathematical Lot Sizing: **`0.49 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`1334.70`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
