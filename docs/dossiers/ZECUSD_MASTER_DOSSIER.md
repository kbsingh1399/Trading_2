# 🏛️ SOVEREIGN CANDIDATE DOSSIER: ZECUSD
**Canonical Key**: `ZECUSD` | **Broker Instrument**: `ZECUSD.p` | **Asset Class**: `Crypto Altcoin`
**Timestamp**: `2026-10-30 00:50:30 IST` (`2026-10-29 19:20:30 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `1320.75` | **Live Ask Quote**: `1321.86` | **Mid Price**: `1321.30`
- **Spread Points**: `111.00` | **Spread BPS**: `8.40 bps` (Charter Threshold: `25.00 bps`)
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
  * Value Area High (VAH) = `1307.14` (Distance: `+1.05%`)
  * Point of Control (POC) = `1247.20` (Distance: `+5.90%`)
  * Value Area Low (VAL) = `1230.55` (Distance: `+7.34%`)
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
  * Golden Pocket Zone (0.618 - 0.650): `1316.02` - `1326.59`
  * Optimal Trade Entry (OTE 0.705): `1323.95`
  * Structural Invalidation Anchor (0.786): `1331.88`

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
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 00:43:50 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `16` | `0xb83d...6e36` | `SHORT` | 69,433,981.97 USD | `52,582.52` | `1336.45` | `1319.40` | `3722.39` | 839,932.93 USD | `+1.21%` | `3X Cross` |
| `24` | `0x5b5d...c060` | `SHORT` | 53,780,809.01 USD | `40,727.61` | `1478.36` | `1319.40` | `5013.80` | 6,429,455.19 USD | `+11.95%` | `3X Cross` |
| `41` | `0x7fda...17d1` | `SHORT` | 29,605,187.44 USD | `22,419.68` | `1261.41` | `1319.40` | `2817.23` | -1,324,792.70 USD | `-4.47%` | `5X Cross` |
| `77` | `0x60b0...991e` | `LONG` | 22,144,227.91 USD | `16,779.74` | `1179.65` | `1319.40` | `891.58` | 2,349,980.90 USD | `+10.61%` | `10X Cross` |
| `82` | `0xbf73...5d58` | `LONG` | 21,113,600.00 USD | `16,000.00` | `1214.30` | `1319.40` | `722.74` | 1,684,767.75 USD | `+7.98%` | `10X Cross` |
| `132` | `0xc36a...105b` | `LONG` | 15,191,980.24 USD | `11,510.82` | `1215.14` | `1319.40` | `933.52` | 1,204,699.21 USD | `+7.93%` | `10X Cross` |
| `169` | `0x8742...8427` | `LONG` | 12,149,277.68 USD | `9,201.21` | `1286.37` | `1319.40` | `698.35` | 313,107.69 USD | `+2.58%` | `10X Cross` |
| `178` | `0x9071...5c0b` | `LONG` | 11,659,052.78 USD | `8,829.94` | `1370.53` | `1319.40` | `579.50` | -442,635.87 USD | `-3.80%` | `2X Cross` |
| `192` | `0xad59...ba81` | `SHORT` | 11,125,014.51 USD | `8,425.00` | `330.91` | `1319.40` | `2140.27` | -8,337,056.74 USD | `-74.94%` | `10X Cross` |
| `199` | `0xdd53...2b13` | `SHORT` | 10,869,220.37 USD | `8,231.14` | `739.37` | `1319.40` | `7888.48` | -4,783,338.89 USD | `-44.01%` | `3X Cross` |
| `200` | `0x9ffd...ce40` | `LONG` | 10,827,740.27 USD | `8,205.32` | `1253.82` | `1319.40` | `570.83` | 539,772.65 USD | `+4.99%` | `5X Cross` |
| `216` | `0xfc66...ca06` | `SHORT` | 10,255,874.12 USD | `7,763.72` | `1319.72` | `1319.40` | `5599.13` | -9,909.04 USD | `-0.10%` | `10X Cross` |
| `220` | `0x880a...311c` | `SHORT` | 10,176,468.04 USD | `7,707.11` | `1367.50` | `1319.40` | `2311.66` | 363,016.16 USD | `+3.57%` | `10X Cross` |
| `268` | `0x2b61...2f6c` | `LONG` | 8,987,962.80 USD | `6,807.00` | `1453.56` | `1319.40` | `638.36` | -906,388.42 USD | `-10.08%` | `10X Cross` |
| `285` | `0x2ae5...83e7` | `LONG` | 8,499,150.72 USD | `6,436.80` | `1391.82` | `1319.40` | `264.91` | -459,741.27 USD | `-5.41%` | `2X Cross` |
| `330` | `0xecb6...2b00` | `SHORT` | 7,189,264.17 USD | `5,444.35` | `1324.05` | `1319.40` | `6119.13` | 19,341.66 USD | `+0.27%` | `5X Cross` |
| `332` | `0x26b6...9a13` | `LONG` | 7,174,697.09 USD | `5,433.73` | `1282.23` | `1319.40` | `209.77` | 207,393.86 USD | `+2.89%` | `10X Cross` |
| `343` | `0x45d2...4029` | `SHORT` | 6,901,730.80 USD | `5,227.00` | `833.44` | `1319.40` | `8061.19` | -2,545,352.83 USD | `-36.88%` | `5X Cross` |
| `362` | `0xea00...a918` | `LONG` | 6,600,500.00 USD | `5,000.00` | `739.16` | `1319.40` | `0.000000` | 2,904,684.89 USD | `+44.01%` | `5X Cross` |
| `377` | `0xdd7a...8830` | `LONG` | 6,422,741.08 USD | `4,860.19` | `897.48` | `1319.40` | `783.56` | 2,060,837.41 USD | `+32.09%` | `10X Cross` |
| `385` | `0xf081...e39e` | `LONG` | 6,231,157.00 USD | `4,717.00` | `1195.70` | `1319.40` | `1200.09` | 591,032.95 USD | `+9.49%` | `10X Cross` |
| `436` | `0x4cae...7c34` | `LONG` | 5,290,160.00 USD | `4,004.36` | `999.34` | `1319.40` | `754.83` | 1,288,431.84 USD | `+24.36%` | `10X Cross` |
| `439` | `0x382b...3e39` | `LONG` | 5,237,604.79 USD | `3,966.38` | `1198.83` | `1319.40` | `0.000000` | 482,607.27 USD | `+9.21%` | `10X Cross` |
| `452` | `0xa61c...66b9` | `LONG` | 5,134,713.25 USD | `3,888.00` | `1148.34` | `1319.40` | `0.000000` | 669,971.11 USD | `+13.05%` | `10X Cross` |
| `472` | `0x9aa5...58af` | `SHORT` | 4,909,693.11 USD | `3,720.31` | `1205.51` | `1319.40` | `3341.88` | -424,806.31 USD | `-8.65%` | `10X Cross` |
| `479` | `0x0153...8052` | `SHORT` | 4,882,337.24 USD | `3,698.18` | `1307.82` | `1319.40` | `2504.69` | -45,766.49 USD | `-0.94%` | `1X Isolated` |
| `504` | `0xd4c1...3d1d` | `SHORT` | 4,564,149.94 USD | `3,455.97` | `1302.96` | `1319.40` | `2691.22` | -61,143.51 USD | `-1.34%` | `10X Cross` |
| `529` | `0xd21d...90f1` | `LONG` | 4,291,548.62 USD | `3,250.00` | `1253.64` | `1319.40` | `875.88` | 217,206.89 USD | `+5.06%` | `4X Isolated` |
| `549` | `0x1338...c48e` | `LONG` | 4,160,397.03 USD | `3,149.43` | `1018.52` | `1319.40` | `820.17` | 952,651.49 USD | `+22.90%` | `4X Isolated` |
| `553` | `0x456f...cdf1` | `LONG` | 4,137,338.61 USD | `3,134.11` | `1268.52` | `1319.40` | `493.35` | 161,648.97 USD | `+3.91%` | `10X Cross` |
| `561` | `0xdbe0...d6d5` | `LONG` | 4,073,305.47 USD | `3,085.37` | `422.97` | `1319.40` | `338.49` | 2,768,300.98 USD | `+67.96%` | `3X Isolated` |
| `572` | `0x27c9...d65d` | `SHORT` | 4,026,899.04 USD | `3,050.45` | `1251.57` | `1319.40` | `1817.11` | -209,036.47 USD | `-5.19%` | `10X Cross` |
| `587` | `0x9c06...0560` | `SHORT` | 3,945,340.08 USD | `2,989.80` | `786.00` | `1319.40` | `2378.11` | -1,595,345.08 USD | `-40.44%` | `10X Cross` |
| `690` | `0xac48...3201` | `LONG` | 3,353,450.03 USD | `2,540.30` | `1393.86` | `1319.40` | `532.11` | -187,379.26 USD | `-5.59%` | `10X Cross` |
| `692` | `0xa183...0482` | `LONG` | 3,345,893.60 USD | `2,534.00` | `530.25` | `1319.40` | `444.42` | 2,002,230.88 USD | `+59.84%` | `5X Isolated` |
| `698` | `0x2e30...4cb5` | `SHORT` | 3,310,941.19 USD | `2,506.39` | `1299.10` | `1319.40` | `3131.12` | -54,882.09 USD | `-1.66%` | `2X Cross` |
| `699` | `0x325e...9564` | `LONG` | 3,304,272.54 USD | `2,501.91` | `1306.24` | `1319.40` | `0.000000` | 36,178.63 USD | `+1.09%` | `10X Cross` |
| `700` | `0x0871...e927` | `LONG` | 3,301,000.00 USD | `2,500.00` | `1276.50` | `1319.40` | `0.000000` | 109,750.00 USD | `+3.32%` | `10X Cross` |
| `708` | `0x9b86...6e6e` | `LONG` | 3,258,011.67 USD | `2,467.30` | `637.58` | `1319.40` | `889.64` | 1,684,912.07 USD | `+51.72%` | `3X Cross` |
| `774` | `0xb2f7...af9f` | `SHORT` | 3,055,212.89 USD | `2,313.72` | `746.63` | `1319.40` | `4185.17` | -1,327,724.14 USD | `-43.46%` | `10X Cross` |
| `788` | `0x634f...6951` | `LONG` | 2,998,685.43 USD | `2,272.42` | `1281.94` | `1319.40` | `1250.03` | 85,584.97 USD | `+2.85%` | `10X Cross` |
| `806` | `0xf48f...10fe` | `LONG` | 2,929,463.91 USD | `2,218.49` | `1517.87` | `1319.40` | `897.75` | -437,922.91 USD | `-14.95%` | `3X Cross` |
| `832` | `0x5bc4...3b0c` | `SHORT` | 2,814,707.54 USD | `2,130.74` | `1089.65` | `1319.40` | `3568.43` | -492,949.96 USD | `-17.51%` | `5X Cross` |
| `844` | `0x8de4...b9aa` | `SHORT` | 2,759,666.28 USD | `2,091.29` | `1331.35` | `1319.40` | `1689.81` | 24,573.42 USD | `+0.89%` | `3X Cross` |
| `851` | `0x4fe2...ac59` | `SHORT` | 2,733,851.55 USD | `2,071.57` | `1478.56` | `1319.40` | `1812.94` | 329,094.66 USD | `+12.04%` | `10X Cross` |
| `868` | `0x668c...ea2e` | `SHORT` | 2,639,200.00 USD | `2,000.00` | `1406.98` | `1319.40` | `2702.05` | 174,763.99 USD | `+6.62%` | `10X Cross` |
| `890` | `0x77ee...2902` | `SHORT` | 2,569,538.01 USD | `1,946.03` | `759.84` | `1319.40` | `5189.35` | -1,090,860.51 USD | `-42.45%` | `10X Cross` |
| `903` | `0x3e2f...b269` | `SHORT` | 2,543,021.06 USD | `1,925.51` | `1134.87` | `1319.40` | `2931.74` | -357,822.20 USD | `-14.07%` | `10X Cross` |
| `909` | `0xe097...d0fe` | `LONG` | 2,526,281.91 USD | `1,913.56` | `1261.17` | `1319.40` | `0.000000` | 112,955.75 USD | `+4.47%` | `10X Cross` |
| `918` | `0x4f12...618b` | `SHORT` | 2,502,521.28 USD | `1,896.28` | `1608.30` | `1319.40` | `2116.70` | 547,263.10 USD | `+21.87%` | `3X Cross` |
| `960` | `0x866d...d6e1` | `LONG` | 2,380,688.25 USD | `1,802.05` | `674.73` | `1319.40` | `98.55` | 1,164,786.94 USD | `+48.93%` | `10X Cross` |
| `993` | `0x2309...a2d9` | `LONG` | 2,309,963.29 USD | `1,750.37` | `1186.09` | `1319.40` | `805.64` | 233,869.18 USD | `+10.12%` | `8X Cross` |
| `1010` | `0x023a...2355` | `SHORT` | 2,246,545.44 USD | `1,700.64` | `1313.33` | `1319.40` | `6072.59` | -13,035.52 USD | `-0.58%` | `10X Cross` |
| `1017` | `0x2edd...8179` | `SHORT` | 2,238,683.27 USD | `1,695.33` | `1261.35` | `1319.40` | `2983.45` | -100,282.30 USD | `-4.48%` | `10X Cross` |
| `1043` | `0x3e47...aaf6` | `LONG` | 2,162,344.02 USD | `1,636.28` | `1279.54` | `1319.40` | `1037.21` | 68,651.93 USD | `+3.17%` | `10X Cross` |
| `1048` | `0xa271...a3f7` | `LONG` | 2,152,998.66 USD | `1,631.43` | `1190.60` | `1319.40` | `910.27` | 210,616.86 USD | `+9.78%` | `4X Cross` |
| `1060` | `0x7f75...9edf` | `LONG` | 2,118,987.29 USD | `1,605.78` | `1199.97` | `1319.40` | `973.93` | 192,095.40 USD | `+9.07%` | `10X Cross` |
| `1061` | `0x265e...7f70` | `LONG` | 2,116,379.06 USD | `1,601.74` | `1388.09` | `1319.40` | `0.000000` | -106,985.95 USD | `-5.06%` | `3X Cross` |
| `1063` | `0x6646...6de5` | `SHORT` | 2,115,360.00 USD | `1,600.00` | `660.64` | `1319.40` | `4799.88` | -1,058,335.03 USD | `-50.03%` | `10X Cross` |
| `1079` | `0xdf57...93f5` | `LONG` | 2,086,389.03 USD | `1,579.76` | `1218.38` | `1319.40` | `780.12` | 161,633.05 USD | `+7.75%` | `3X Isolated` |
| `1096` | `0xab59...59b5` | `LONG` | 2,066,968.27 USD | `1,565.32` | `1342.15` | `1319.40` | `793.30` | -33,926.94 USD | `-1.64%` | `10X Cross` |
| `1100` | `0xfe7c...b7ae` | `SHORT` | 2,062,018.52 USD | `1,562.49` | `1350.62` | `1319.40` | `6541.70` | 48,310.53 USD | `+2.34%` | `10X Cross` |
| `1155` | `0xcf67...eb24` | `LONG` | 1,979,550.45 USD | `1,500.00` | `887.05` | `1319.40` | `549.85` | 648,979.08 USD | `+32.78%` | `10X Cross` |
| `1173` | `0x039c...0ebd` | `SHORT` | 1,955,219.04 USD | `1,480.49` | `1238.67` | `1319.40` | `3170.26` | -121,387.72 USD | `-6.21%` | `10X Cross` |
| `1199` | `0x71d0...8c26` | `SHORT` | 1,908,725.28 USD | `1,444.80` | `1361.12` | `1319.40` | `6492.50` | 57,821.17 USD | `+3.03%` | `10X Cross` |
| `1246` | `0xfc27...9d9d` | `SHORT` | 1,853,722.76 USD | `1,403.91` | `1317.50` | `1319.40` | `11394.51` | -4,076.60 USD | `-0.22%` | `10X Cross` |
| `1250` | `0x2ab7...c2f8` | `LONG` | 1,848,953.30 USD | `1,400.51` | `813.26` | `1319.40` | `796.18` | 709,971.62 USD | `+38.40%` | `3X Cross` |
| `1264` | `0x11be...8b1d` | `LONG` | 1,817,609.01 USD | `1,375.83` | `1206.55` | `1319.40` | `1134.40` | 157,601.06 USD | `+8.67%` | `10X Isolated` |
| `1315` | `0xdf83...3cff` | `SHORT` | 1,733,693.21 USD | `1,312.93` | `1246.70` | `1319.40` | `1852.46` | -96,862.90 USD | `-5.59%` | `10X Cross` |
| `1317` | `0xef96...9383` | `SHORT` | 1,728,296.81 USD | `1,308.82` | `1249.96` | `1319.40` | `4220.37` | -92,330.39 USD | `-5.34%` | `10X Cross` |
| `1363` | `0xe065...0f85` | `SHORT` | 1,668,034.07 USD | `1,262.61` | `1087.02` | `1319.40` | `1759.61` | -295,557.94 USD | `-17.72%` | `10X Cross` |
| `1388` | `0x7277...0b98` | `SHORT` | 1,631,011.67 USD | `1,234.96` | `1298.48` | `1319.40` | `2361.86` | -27,442.25 USD | `-1.68%` | `10X Cross` |
| `1436` | `0x5975...9abd` | `LONG` | 1,584,120.00 USD | `1,200.00` | `1179.54` | `1319.40` | `341.58` | 168,677.21 USD | `+10.65%` | `5X Cross` |
| `1479` | `0x69cc...14fd` | `SHORT` | 1,533,808.15 USD | `1,161.36` | `675.33` | `1319.40` | `7866.43` | -749,502.62 USD | `-48.87%` | `10X Cross` |
| `1481` | `0x7a76...b16d` | `LONG` | 1,530,788.79 USD | `1,159.27` | `1358.50` | `1319.40` | `1240.21` | -44,079.72 USD | `-2.88%` | `10X Cross` |
| `1493` | `0x3fc5...c0c1` | `SHORT` | 1,516,055.64 USD | `1,148.44` | `1264.34` | `1319.40` | `3103.38` | -64,041.87 USD | `-4.22%` | `10X Cross` |
| `1511` | `0xe35c...a1d3` | `LONG` | 1,488,459.34 USD | `1,127.06` | `1318.20` | `1319.40` | `694.32` | 2,763.99 USD | `+0.19%` | `2X Isolated` |
| `1516` | `0x5f94...4b96` | `LONG` | 1,472,687.83 USD | `1,115.27` | `538.00` | `1319.40` | `0.000000` | 872,670.19 USD | `+59.26%` | `10X Cross` |
| `1536` | `0x71df...a23d` | `SHORT` | 1,450,168.91 USD | `1,098.28` | `513.50` | `1319.40` | `2547.31` | -886,198.72 USD | `-61.11%` | `2X Cross` |
| `1565` | `0xbfc7...80b4` | `SHORT` | 1,418,677.50 USD | `1,075.00` | `558.03` | `1319.40` | `5469.84` | -818,798.77 USD | `-57.72%` | `10X Cross` |
| `1609` | `0x51f6...2b39` | `SHORT` | 1,373,785.47 USD | `1,039.88` | `1302.72` | `1319.40` | `2875.87` | -19,108.66 USD | `-1.39%` | `10X Cross` |
| `1643` | `0x123d...3bff` | `SHORT` | 1,331,161.26 USD | `1,008.15` | `489.25` | `1319.40` | `4212.83` | -837,927.19 USD | `-62.95%` | `10X Cross` |
| `1651` | `0xe282...df29` | `LONG` | 1,320,656.70 USD | `1,000.00` | `420.99` | `1319.40` | `110.08` | 899,669.84 USD | `+68.12%` | `10X Cross` |
| `1652` | `0xb5ff...d912` | `LONG` | 1,320,400.00 USD | `1,000.00` | `1141.93` | `1319.40` | `400.44` | 178,469.70 USD | `+13.52%` | `2X Cross` |
| `1653` | `0x0748...d4b2` | `LONG` | 1,320,400.00 USD | `1,000.00` | `1334.09` | `1319.40` | `0.000000` | -13,688.30 USD | `-1.04%` | `7X Cross` |
| `1654` | `0x266b...efcb` | `LONG` | 1,320,200.00 USD | `1,000.00` | `826.11` | `1319.40` | `153.60` | 494,087.07 USD | `+37.43%` | `10X Cross` |
| `1677` | `0x17f0...094f` | `LONG` | 1,300,358.73 USD | `984.30` | `1287.23` | `1319.40` | `536.75` | 33,338.57 USD | `+2.56%` | `5X Cross` |
| `1752` | `0x757d...94ba` | `LONG` | 1,221,647.50 USD | `925.00` | `1558.31` | `1319.40` | `0.000000` | -219,793.08 USD | `-17.99%` | `10X Cross` |
| `1807` | `0x2847...d47b` | `LONG` | 1,169,107.45 USD | `884.95` | `1237.75` | `1319.40` | `0.000000` | 73,763.04 USD | `+6.31%` | `5X Cross` |
| `1815` | `0xdf95...7d72` | `SHORT` | 1,162,889.51 USD | `880.31` | `1073.82` | `1319.40` | `41542.86` | -217,591.21 USD | `-18.71%` | `10X Cross` |
| `1816` | `0xf096...7553` | `SHORT` | 1,162,659.97 USD | `881.07` | `1240.34` | `1319.40` | `3536.22` | -69,829.89 USD | `-6.01%` | `10X Cross` |
| `1829` | `0xcf0a...856f` | `LONG` | 1,149,569.54 USD | `871.15` | `1292.19` | `1319.40` | `938.45` | 23,874.69 USD | `+2.08%` | `4X Cross` |
| `1859` | `0x7d0f...ea35` | `LONG` | 1,121,660.00 USD | `850.00` | `1317.57` | `1319.40` | `1275.62` | 1,724.42 USD | `+0.15%` | `10X Cross` |
| `1897` | `0x601c...4f54` | `SHORT` | 1,089,058.82 USD | `824.42` | `615.11` | `1319.40` | `2944.02` | -581,946.07 USD | `-53.44%` | `5X Cross` |
| `1904` | `0xae55...2236` | `LONG` | 1,080,736.70 USD | `817.47` | `1467.80` | `1319.40` | `0.000000` | -119,144.51 USD | `-11.02%` | `10X Cross` |
| `1911` | `0x71b1...79c8` | `LONG` | 1,073,095.16 USD | `812.52` | `1231.55` | `1319.40` | `708.46` | 72,439.71 USD | `+6.75%` | `10X Cross` |
| `1931` | `0x9b0f...db40` | `LONG` | 1,057,640.48 USD | `800.00` | `1268.86` | `1319.40` | `774.68` | 42,550.72 USD | `+4.02%` | `10X Cross` |
| `1932` | `0x0f02...5384` | `LONG` | 1,057,590.15 USD | `800.78` | `1290.36` | `1319.40` | `290.23` | 24,296.08 USD | `+2.30%` | `3X Cross` |
| `1943` | `0xabdb...84ac` | `LONG` | 1,047,512.06 USD | `793.69` | `711.79` | `1319.40` | `664.32` | 482,571.70 USD | `+46.07%` | `3X Cross` |
| `1947` | `0xfdf8...e381` | `LONG` | 1,044,417.71 USD | `790.01` | `1337.72` | `1319.40` | `390.67` | -12,391.98 USD | `-1.19%` | `10X Cross` |
| `2016` | `0x0c1f...1d39` | `SHORT` | 1,007,528.30 USD | `762.99` | `1299.17` | `1319.40` | `4917.78` | -16,277.21 USD | `-1.62%` | `10X Cross` |
| `2020` | `0xf6f3...47f8` | `SHORT` | 1,006,871.70 USD | `761.57` | `1253.10` | `1319.40` | `2399.86` | -52,548.70 USD | `-5.22%` | `5X Cross` |
| `2025` | `0x389a...e76b` | `LONG` | 1,003,733.80 USD | `760.13` | `1266.20` | `1319.40` | `358.81` | 41,260.38 USD | `+4.11%` | `10X Cross` |

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
  * Current Rate: `85.39K` | Last 24h: `32.07K` | Last 3d: `282.84K` | Last 7d: `777.72K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0079%` | **USDT OKX** | `0.0100%` |
| **USDT Bybit** | `0.0100%` | **USDT KuCoin** | `0.0100%` |
| **USDT MEXC** | `0.0080%` | **USDT BingX** | `0.0065%` |
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
| `5m` | 191,980.00 USD | 596,830.00 USD | **`ACCUMULATION`** |
| `15m` | 983,870.00 USD | 2,000,000.00 USD | **`ACCUMULATION`** |
| `30m` | 1,850,000.00 USD | 12,660,000.00 USD | **`ACCUMULATION`** |
| `1h` | 295,800.00 USD | -3,860,000.00 USD | **`DISTRIBUTION`** |
| `2h` | 1,520,000.00 USD | -15,100,000.00 USD | **`DISTRIBUTION`** |
| `4h` | 18,460,000.00 USD | 53,090,000.00 USD | **`ACCUMULATION`** |
| `6h` | 29,780,000.00 USD | 85,520,000.00 USD | **`ACCUMULATION`** |
| `8h` | 31,890,000.00 USD | 102,220,000.00 USD | **`ACCUMULATION`** |
| `12h` | 29,350,000.00 USD | 111,570,000.00 USD | **`ACCUMULATION`** |
| `24h` | 12,180,000.00 USD | 76,820,000.00 USD | **`ACCUMULATION`** |
| `1w` | 51,270,000.00 USD | 252,440,000.00 USD | **`ACCUMULATION`** |
| `30d` | 66,680,000.00 USD | -506,920,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+191.98K` | 15m=`+983.87K` | 1h=`+295.80K` | 24h=`+12.18M`
* Futures Capital Netflows: 5m=`+596.83K` | 15m=`+2.00M` | 1h=`-3.86M` | 24h=`+76.82M`
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
  * `2026-10-30 00:48:09 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 00:17:09 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 00:49:09 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 00:49:09 IST`: [@DeItaone] - (Sentiment: `Neutral`)
  * `2026-10-30 00:49:09 IST`: [@mb_ghalibaf] - (Sentiment: `Neutral`)
  * `2026-10-30 00:49:09 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-30 00:49:09 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-30 00:48:09 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-30 00:48:09 IST`: [fxstreet.com] - (Sentiment: `Neutral`)
  * `2026-10-29 21:50:09 IST`: [ForexFactory] - (Sentiment: `Neutral`)
  * `2026-10-29 21:50:09 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-29 21:50:09 IST`: [youtube.com/bankofcanadaofficial] - (Sentiment: `Neutral`)
  * `2026-10-29 20:50:09 IST`: [notayesmanseconomics.wordpress.com] - (Sentiment: `Neutral`)
  * `2026-10-29 20:50:09 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 20:50:09 IST`: [breakingthenews.net] - (Sentiment: `Neutral`)


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
  * Spread-Padded Stop Loss: `1209.11` (Risk Distance: `21.44` pts)
  * +2.5R Take Profit: `1284.15`
  * Mathematical Lot Sizing: **`0.46 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `1307.14` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `1328.58` (Risk Distance: `21.44` pts)
  * +2.5R Take Profit: `1253.54`
  * Mathematical Lot Sizing: **`0.46 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`1331.88`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
