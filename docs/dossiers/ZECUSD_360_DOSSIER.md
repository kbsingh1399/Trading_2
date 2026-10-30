# 🏛️ SOVEREIGN CANDIDATE DOSSIER: ZECUSD
**Canonical Key**: `ZECUSD` | **Broker Instrument**: `ZECUSD.p` | **Asset Class**: `Crypto Altcoin`
**Timestamp**: `2026-10-30 16:48:54 IST` (`2026-10-30 11:18:54 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `1265.62` | **Live Ask Quote**: `1266.74` | **Mid Price**: `1266.18`
- **Spread Points**: `112.00` | **Spread BPS**: `8.85 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `1254.22` | VWAP Z-Score: `+1.04` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `12.91` (Volatility Regime: `HIGH_EXPANSION`)
  * 14-Period RSI: `60.19` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `1314.91` | Lower -3.00σ Band: `1193.53`
  * Upper +2.51σ Band: `1304.99` | Lower -2.51σ Band: `1203.44`
  * Upper +2.01σ Band: `1294.88` | Lower -2.01σ Band: `1213.55`
  * Upper +2.00σ Band: `1294.68` | Lower -2.00σ Band: `1213.76`
  * Upper +1.28σ Band: `1280.11` | Lower -1.28σ Band: `1228.32`
  * Upper +1.00σ Band: `1274.45` | Lower -1.00σ Band: `1233.99`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`1259.57` | EMA-20=`1258.34` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`1262.03` (Slope: `+0.0000`) | EMA-100=`1267.66`
  * Institutional Anchors: EMA-144=`1271.06` | EMA-200=`1275.97` (Slope: `-0.2270`) | EMA-233=`1275.72`
- **Range Boundaries**: 24H High=`1396.49` | 24H Low=`1180.03` | Weekly High=`1396.49` | Weekly Low=`1180.03`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `1278.60` (Distance: `-0.99%`)
  * Point of Control (POC) = `1247.68` (Distance: `+1.46%`)
  * Value Area Low (VAL) = `1239.95` (Distance: `+2.09%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`1309.91` | POC=`1246.71` | VAL=`1230.27`
  * Prior Day Extremes: PDH=`1396.49` | PDL=`1206.89` | PDC=`1244.38`
  * Monday Range Blueprint: High=`1267.53` | Mid=`1222.14` | Low=`1176.75`
  * Developing Weekly Value Area: Weekly VAH=`1300.54` | Weekly POC=`1240.47` | Weekly VAL=`1214.11`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`1296.00` | Low=`1180.03`
  * London Session (08:00-16:00 UTC): High=`1283.82` | Low=`1239.95`
  * New York Session (13:00-21:00 UTC): High=`1276.27` | Low=`1245.73`
  * Initial Balance (First Hour): IB High=`1283.82` | IB Low=`1264.92`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `1261.12` - `1271.24`
  * Optimal Trade Entry (OTE 0.705): `1268.71`
  * Structural Invalidation Anchor (0.786): `1276.31`

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
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 16:42:20 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `12` | `0xb83d...6e36` | `SHORT` | 66,335,720.66 USD | `52,385.47` | `1336.45` | `1265.80` | `3185.43` | 3,674,846.74 USD | `+5.54%` | `3X Cross` |
| `21` | `0x5b5d...c060` | `SHORT` | 50,849,837.01 USD | `40,121.38` | `1478.36` | `1265.80` | `4781.69` | 8,464,198.10 USD | `+16.65%` | `3X Cross` |
| `36` | `0x7fda...17d1` | `SHORT` | 33,755,397.26 USD | `26,635.68` | `1262.58` | `1265.80` | `2392.07` | -125,778.23 USD | `-0.37%` | `5X Cross` |
| `80` | `0x60b0...991e` | `LONG` | 21,281,744.24 USD | `16,779.74` | `1179.65` | `1265.80` | `913.57` | 1,487,497.23 USD | `+6.99%` | `10X Cross` |
| `140` | `0xc36a...105b` | `LONG` | 14,589,964.35 USD | `11,510.82` | `1215.14` | `1265.80` | `962.92` | 602,683.32 USD | `+4.13%` | `10X Cross` |
| `174` | `0x8742...8427` | `LONG` | 11,655,172.71 USD | `9,201.21` | `1286.37` | `1265.80` | `712.45` | -180,997.29 USD | `-1.55%` | `10X Cross` |
| `191` | `0x58b2...11f3` | `LONG` | 10,859,698.06 USD | `8,563.08` | `1246.56` | `1265.80` | `386.69` | 185,280.48 USD | `+1.71%` | `10X Cross` |
| `195` | `0x9ffd...ce40` | `LONG` | 10,690,227.50 USD | `8,434.77` | `1252.39` | `1265.80` | `598.24` | 126,611.60 USD | `+1.18%` | `5X Cross` |
| `196` | `0xad59...ba81` | `SHORT` | 10,677,845.00 USD | `8,425.00` | `330.91` | `1265.80` | `2146.02` | -7,889,887.23 USD | `-73.89%` | `10X Cross` |
| `203` | `0xdd53...2b13` | `SHORT` | 10,380,952.27 USD | `8,195.92` | `741.54` | `1265.80` | `8378.72` | -4,303,355.91 USD | `-41.45%` | `3X Cross` |
| `222` | `0x880a...311c` | `SHORT` | 9,766,449.79 USD | `7,707.11` | `1367.50` | `1265.80` | `2235.99` | 773,034.41 USD | `+7.92%` | `10X Cross` |
| `235` | `0x9071...5c0b` | `LONG` | 9,522,151.24 USD | `7,517.29` | `1353.83` | `1265.80` | `108.98` | -654,978.73 USD | `-6.88%` | `2X Cross` |
| `236` | `0xbf73...5d58` | `LONG` | 9,507,000.00 USD | `7,500.00` | `1248.78` | `1265.80` | `119.00` | 141,154.38 USD | `+1.48%` | `10X Cross` |
| `270` | `0x2b61...2f6c` | `LONG` | 8,625,830.40 USD | `6,807.00` | `1453.56` | `1265.80` | `583.95` | -1,268,520.82 USD | `-14.71%` | `10X Cross` |
| `288` | `0x2ae5...83e7` | `LONG` | 8,153,494.56 USD | `6,436.80` | `1391.82` | `1265.80` | `0.000000` | -805,397.43 USD | `-9.88%` | `1X Cross` |
| `311` | `0xecb6...2b00` | `SHORT` | 7,736,321.56 USD | `6,104.57` | `1277.42` | `1265.80` | `6544.14` | 61,776.35 USD | `+0.80%` | `5X Cross` |
| `336` | `0x26b6...9a13` | `LONG` | 6,882,905.79 USD | `5,433.73` | `1282.23` | `1265.80` | `231.65` | -84,397.44 USD | `-1.23%` | `10X Cross` |
| `347` | `0x45d2...4029` | `SHORT` | 6,621,040.90 USD | `5,227.00` | `833.44` | `1265.80` | `8926.66` | -2,264,662.93 USD | `-34.20%` | `5X Cross` |
| `364` | `0xea00...a918` | `LONG` | 6,341,500.00 USD | `5,000.00` | `739.16` | `1265.80` | `0.000000` | 2,645,684.89 USD | `+41.72%` | `5X Cross` |
| `375` | `0xdd7a...8830` | `LONG` | 6,154,944.62 USD | `4,860.19` | `897.48` | `1265.80` | `780.45` | 1,793,040.94 USD | `+29.13%` | `10X Cross` |
| `420` | `0x469e...58a5` | `SHORT` | 5,277,261.60 USD | `4,163.52` | `1242.31` | `1265.80` | `1950.91` | -104,876.95 USD | `-1.99%` | `10X Cross` |
| `422` | `0x4cae...7c34` | `LONG` | 5,261,756.54 USD | `4,152.27` | `1172.97` | `1265.80` | `981.53` | 391,262.99 USD | `+7.44%` | `10X Cross` |
| `441` | `0xd4c1...3d1d` | `SHORT` | 4,980,703.33 USD | `3,931.41` | `1291.66` | `1265.80` | `2321.90` | 97,325.50 USD | `+1.95%` | `10X Cross` |
| `445` | `0xa61c...66b9` | `LONG` | 4,924,929.60 USD | `3,888.00` | `1148.34` | `1265.80` | `0.000000` | 460,187.46 USD | `+9.34%` | `10X Cross` |
| `469` | `0x9aa5...58af` | `SHORT` | 4,715,492.92 USD | `3,720.31` | `1205.51` | `1265.80` | `3638.97` | -230,606.13 USD | `-4.89%` | `10X Cross` |
| `474` | `0x0153...8052` | `SHORT` | 4,685,224.24 USD | `3,698.18` | `1307.82` | `1265.80` | `2504.97` | 151,346.51 USD | `+3.23%` | `1X Isolated` |
| `505` | `0xb122...e4ba` | `LONG` | 4,437,459.35 USD | `3,498.47` | `1265.25` | `1265.80` | `1058.07` | 11,007.82 USD | `+0.25%` | `10X Cross` |
| `538` | `0x382b...3e39` | `LONG` | 4,128,685.98 USD | `3,257.86` | `1220.72` | `1265.80` | `0.000000` | 151,756.24 USD | `+3.68%` | `10X Cross` |
| `540` | `0xd21d...90f1` | `LONG` | 4,119,050.00 USD | `3,250.00` | `1253.64` | `1265.80` | `876.19` | 44,708.27 USD | `+1.09%` | `4X Isolated` |
| `547` | `0x456f...cdf1` | `LONG` | 4,050,499.05 USD | `3,195.66` | `1267.53` | `1265.80` | `508.40` | -96.76 USD | `-0.00%` | `10X Cross` |
| `556` | `0x1338...c48e` | `LONG` | 3,991,272.64 USD | `3,149.43` | `1018.52` | `1265.80` | `820.49` | 783,527.10 USD | `+19.63%` | `4X Isolated` |
| `574` | `0xdbe0...d6d5` | `LONG` | 3,908,855.25 USD | `3,085.37` | `422.97` | `1265.80` | `338.80` | 2,603,850.76 USD | `+66.61%` | `3X Isolated` |
| `595` | `0x325e...9564` | `LONG` | 3,801,252.70 USD | `3,000.91` | `1298.07` | `1265.80` | `133.12` | -94,152.46 USD | `-2.48%` | `10X Cross` |
| `599` | `0x9c06...0560` | `SHORT` | 3,789,870.48 USD | `2,989.80` | `786.00` | `1265.80` | `2530.60` | -1,439,875.48 USD | `-37.99%` | `10X Cross` |
| `601` | `0x2e30...4cb5` | `SHORT` | 3,785,874.96 USD | `2,988.77` | `1282.25` | `1265.80` | `2888.28` | 46,474.69 USD | `+1.23%` | `2X Cross` |
| `606` | `0x27c9...d65d` | `SHORT` | 3,726,316.13 USD | `2,938.04` | `1254.41` | `1265.80` | `1728.56` | -40,806.09 USD | `-1.10%` | `10X Cross` |
| `685` | `0x5323...b23c` | `SHORT` | 3,283,096.40 USD | `2,591.85` | `1270.67` | `1265.80` | `3367.76` | 10,287.31 USD | `+0.31%` | `5X Cross` |
| `699` | `0xac48...3201` | `LONG` | 3,210,701.45 USD | `2,531.50` | `1378.58` | `1265.80` | `562.08` | -279,170.83 USD | `-8.70%` | `10X Cross` |
| `700` | `0xa183...0482` | `LONG` | 3,209,564.40 USD | `2,534.00` | `530.25` | `1265.80` | `444.73` | 1,865,901.68 USD | `+58.14%` | `5X Isolated` |
| `711` | `0x9e2c...5508` | `LONG` | 3,169,000.00 USD | `2,500.00` | `1275.77` | `1265.80` | `453.20` | -20,425.91 USD | `-0.64%` | `10X Cross` |
| `712` | `0x0871...e927` | `LONG` | 3,168,000.00 USD | `2,500.00` | `1276.50` | `1265.80` | `0.000000` | -23,250.00 USD | `-0.73%` | `10X Cross` |
| `715` | `0x71d0...8c26` | `SHORT` | 3,157,199.14 USD | `2,491.28` | `1268.47` | `1265.80` | `3447.07` | 2,925.35 USD | `+0.09%` | `10X Cross` |
| `727` | `0x9b86...6e6e` | `LONG` | 3,121,986.42 USD | `2,463.30` | `637.58` | `1265.80` | `882.66` | 1,551,437.14 USD | `+49.69%` | `3X Cross` |
| `813` | `0xf48f...10fe` | `LONG` | 2,811,714.23 USD | `2,218.49` | `1517.87` | `1265.80` | `972.60` | -555,672.60 USD | `-19.76%` | `3X Cross` |
| `840` | `0x5bc4...3b0c` | `SHORT` | 2,698,795.28 USD | `2,130.74` | `1089.65` | `1265.80` | `3668.36` | -377,037.71 USD | `-13.97%` | `5X Cross` |
| `852` | `0x8de4...b9aa` | `SHORT` | 2,650,500.95 USD | `2,091.29` | `1331.35` | `1265.80` | `1690.09` | 133,738.76 USD | `+5.05%` | `3X Cross` |
| `860` | `0x4fe2...ac59` | `SHORT` | 2,627,579.39 USD | `2,071.57` | `1478.56` | `1265.80` | `1830.96` | 435,366.83 USD | `+16.57%` | `10X Cross` |
| `865` | `0xdf57...93f5` | `LONG` | 2,602,039.71 USD | `2,054.35` | `1227.36` | `1265.80` | `897.43` | 80,617.67 USD | `+3.10%` | `4X Isolated` |
| `871` | `0xbcd4...0dd2` | `LONG` | 2,577,790.21 USD | `2,033.92` | `1228.20` | `1265.80` | `798.51` | 79,739.39 USD | `+3.09%` | `10X Cross` |
| `878` | `0x9a99...d21a` | `LONG` | 2,536,600.00 USD | `2,000.00` | `1278.44` | `1265.80` | `0.000000` | -20,273.67 USD | `-0.80%` | `10X Cross` |
| `880` | `0xf29c...9971` | `LONG` | 2,533,200.00 USD | `2,000.00` | `1254.95` | `1265.80` | `0.000000` | 23,302.93 USD | `+0.92%` | `10X Cross` |
| `900` | `0x77ee...2902` | `SHORT` | 2,466,009.22 USD | `1,946.03` | `759.84` | `1265.80` | `5690.41` | -987,331.71 USD | `-40.04%` | `10X Cross` |
| `912` | `0x3e2f...b269` | `SHORT` | 2,438,850.97 USD | `1,925.51` | `1134.87` | `1265.80` | `2977.36` | -253,652.11 USD | `-10.40%` | `10X Cross` |
| `924` | `0x4f12...618b` | `SHORT` | 2,404,862.30 USD | `1,896.28` | `1608.30` | `1265.80` | `2116.98` | 644,922.09 USD | `+26.82%` | `3X Cross` |
| `934` | `0x039c...0ebd` | `SHORT` | 2,371,944.52 USD | `1,873.13` | `1250.08` | `1265.80` | `3290.36` | -30,376.97 USD | `-1.28%` | `10X Cross` |
| `971` | `0x866d...d6e1` | `LONG` | 2,283,557.76 USD | `1,802.05` | `674.73` | `1265.80` | `108.89` | 1,067,656.45 USD | `+46.75%` | `10X Cross` |
| `994` | `0x2309...a2d9` | `LONG` | 2,218,593.98 USD | `1,750.37` | `1186.09` | `1265.80` | `807.74` | 142,499.86 USD | `+6.42%` | `8X Cross` |
| `1027` | `0x265e...7f70` | `LONG` | 2,093,415.28 USD | `1,651.74` | `1382.98` | `1265.80` | `0.000000` | -190,907.48 USD | `-9.12%` | `3X Cross` |
| `1034` | `0xfe7c...b7ae` | `SHORT` | 2,083,360.31 USD | `1,642.64` | `1346.92` | `1265.80` | `5608.62` | 129,148.31 USD | `+6.20%` | `10X Cross` |
| `1038` | `0x3e47...aaf6` | `LONG` | 2,073,821.27 USD | `1,636.28` | `1278.38` | `1265.80` | `1047.19` | -17,970.51 USD | `-0.87%` | `10X Cross` |
| `1040` | `0x2edd...8179` | `SHORT` | 2,072,295.87 USD | `1,635.98` | `1261.55` | `1265.80` | `2847.00` | -8,432.98 USD | `-0.41%` | `10X Cross` |
| `1048` | `0x3205...40bb` | `SHORT` | 2,063,805.44 USD | `1,629.02` | `1262.15` | `1265.80` | `2144.36` | -7,743.53 USD | `-0.38%` | `10X Cross` |
| `1057` | `0x7f75...9edf` | `LONG` | 2,049,050.05 USD | `1,616.48` | `1200.45` | `1265.80` | `989.39` | 108,545.57 USD | `+5.30%` | `10X Cross` |
| `1067` | `0xfc27...9d9d` | `SHORT` | 2,032,597.49 USD | `1,604.64` | `1295.09` | `1265.80` | `12734.58` | 45,548.32 USD | `+2.24%` | `10X Cross` |
| `1072` | `0x6646...6de5` | `SHORT` | 2,027,040.00 USD | `1,600.00` | `660.64` | `1265.80` | `4308.55` | -970,015.03 USD | `-47.85%` | `10X Cross` |
| `1077` | `0x023a...2355` | `SHORT` | 2,019,170.47 USD | `1,594.04` | `1309.94` | `1265.80` | `4413.10` | 68,923.79 USD | `+3.41%` | `10X Cross` |
| `1097` | `0xab59...59b5` | `LONG` | 1,983,886.57 USD | `1,565.32` | `1342.15` | `1265.80` | `835.33` | -117,008.65 USD | `-5.90%` | `10X Cross` |
| `1156` | `0xcf67...eb24` | `LONG` | 1,902,450.00 USD | `1,500.00` | `887.05` | `1265.80` | `604.04` | 571,878.63 USD | `+30.06%` | `10X Cross` |
| `1172` | `0x7277...0b98` | `SHORT` | 1,869,159.62 USD | `1,475.73` | `1287.86` | `1265.80` | `2178.87` | 31,372.50 USD | `+1.68%` | `10X Cross` |
| `1239` | `0x926a...af36` | `LONG` | 1,775,508.06 USD | `1,401.68` | `1254.50` | `1265.80` | `1187.95` | 17,106.16 USD | `+0.96%` | `10X Isolated` |
| `1241` | `0x2ab7...c2f8` | `LONG` | 1,774,026.02 USD | `1,400.51` | `813.26` | `1265.80` | `790.70` | 635,044.33 USD | `+35.80%` | `3X Cross` |
| `1261` | `0x11be...8b1d` | `LONG` | 1,743,864.52 USD | `1,375.83` | `1206.55` | `1265.80` | `1134.71` | 83,856.57 USD | `+4.81%` | `10X Isolated` |
| `1305` | `0xdf83...3cff` | `SHORT` | 1,655,528.58 USD | `1,306.24` | `1260.68` | `1265.80` | `1869.67` | -8,783.58 USD | `-0.53%` | `10X Cross` |
| `1312` | `0xef96...9383` | `SHORT` | 1,645,609.48 USD | `1,297.39` | `1262.03` | `1265.80` | `3872.86` | -8,267.53 USD | `-0.50%` | `10X Cross` |
| `1342` | `0xe065...0f85` | `SHORT` | 1,601,368.26 USD | `1,262.61` | `1087.02` | `1265.80` | `1545.22` | -228,892.14 USD | `-14.29%` | `10X Cross` |
| `1354` | `0x413c...886c` | `LONG` | 1,584,250.00 USD | `1,250.00` | `1237.51` | `1265.80` | `0.000000` | 37,360.54 USD | `+2.36%` | `10X Cross` |
| `1404` | `0x2847...d47b` | `LONG` | 1,535,842.43 USD | `1,211.71` | `1232.45` | `1265.80` | `0.000000` | 42,474.83 USD | `+2.77%` | `5X Cross` |
| `1423` | `0x5975...9abd` | `LONG` | 1,521,000.00 USD | `1,200.00` | `1179.54` | `1265.80` | `518.62` | 105,557.21 USD | `+6.94%` | `5X Cross` |
| `1425` | `0x266b...efcb` | `LONG` | 1,520,280.00 USD | `1,200.00` | `893.76` | `1265.80` | `399.58` | 447,770.30 USD | `+29.45%` | `10X Cross` |
| `1456` | `0xb897...ebc1` | `SHORT` | 1,486,548.45 USD | `1,173.56` | `1256.04` | `1265.80` | `1349.58` | -12,505.17 USD | `-0.84%` | `10X Cross` |
| `1465` | `0x69cc...14fd` | `SHORT` | 1,470,978.58 USD | `1,161.36` | `675.33` | `1265.80` | `8016.53` | -686,673.05 USD | `-46.68%` | `10X Cross` |
| `1477` | `0x3fc5...c0c1` | `SHORT` | 1,455,647.70 USD | `1,148.44` | `1264.34` | `1265.80` | `2738.07` | -3,633.92 USD | `-0.25%` | `10X Cross` |
| `1518` | `0x5f94...4b96` | `LONG` | 1,413,493.20 USD | `1,115.27` | `538.00` | `1265.80` | `0.000000` | 813,475.56 USD | `+57.55%` | `10X Cross` |
| `1523` | `0xe35c...a1d3` | `LONG` | 1,407,759.71 USD | `1,111.36` | `1311.66` | `1265.80` | `691.00` | -49,964.43 USD | `-3.55%` | `2X Isolated` |
| `1551` | `0x71df...a23d` | `SHORT` | 1,391,740.42 USD | `1,098.28` | `513.50` | `1265.80` | `2559.42` | -827,770.23 USD | `-59.48%` | `2X Cross` |
| `1575` | `0x38f9...cb04` | `SHORT` | 1,366,763.90 USD | `1,078.57` | `1259.78` | `1265.80` | `2061.72` | -8,004.38 USD | `-0.59%` | `10X Cross` |
| `1577` | `0xbfc7...80b4` | `SHORT` | 1,362,562.50 USD | `1,075.00` | `558.03` | `1265.80` | `2629.24` | -762,683.77 USD | `-55.97%` | `10X Cross` |
| `1580` | `0x8b9d...7b28` | `SHORT` | 1,356,872.76 USD | `1,070.68` | `1272.16` | `1265.80` | `3324.32` | 5,205.48 USD | `+0.38%` | `10X Cross` |
| `1603` | `0x123d...3bff` | `SHORT` | 1,323,700.95 USD | `1,044.34` | `519.62` | `1265.80` | `4141.86` | -781,042.74 USD | `-59.00%` | `10X Cross` |
| `1661` | `0x668c...ea2e` | `SHORT` | 1,267,500.00 USD | `1,000.00` | `1406.98` | `1265.80` | `4212.37` | 139,481.99 USD | `+11.00%` | `10X Cross` |
| `1662` | `0x8ab1...15ef` | `LONG` | 1,267,400.00 USD | `1,000.00` | `1275.75` | `1265.80` | `981.00` | -8,354.92 USD | `-0.66%` | `10X Cross` |
| `1663` | `0x98e0...d7e0` | `LONG` | 1,266,700.00 USD | `1,000.00` | `1276.62` | `1265.80` | `937.08` | -9,922.14 USD | `-0.78%` | `10X Cross` |
| `1665` | `0xe282...df29` | `LONG` | 1,266,400.00 USD | `1,000.00` | `420.99` | `1265.80` | `792.65` | 845,413.14 USD | `+66.76%` | `10X Cross` |
| `1667` | `0xfc66...ca06` | `SHORT` | 1,264,702.03 USD | `997.95` | `1273.61` | `1265.80` | `27170.04` | 6,298.84 USD | `+0.50%` | `10X Cross` |
| `1693` | `0x17f0...094f` | `LONG` | 1,247,304.96 USD | `984.30` | `1287.23` | `1265.80` | `537.06` | -19,715.20 USD | `-1.58%` | `5X Cross` |
| `1722` | `0x51f6...2b39` | `SHORT` | 1,221,440.81 USD | `964.27` | `1299.77` | `1265.80` | `2499.52` | 31,886.87 USD | `+2.61%` | `10X Cross` |
| `1732` | `0x4e23...20c3` | `LONG` | 1,211,540.90 USD | `956.53` | `1265.15` | `1265.80` | `0.000000` | 1,389.46 USD | `+0.11%` | `4X Cross` |
| `1746` | `0xf096...7553` | `SHORT` | 1,192,217.83 USD | `940.68` | `1257.96` | `1265.80` | `3075.41` | -8,884.11 USD | `-0.75%` | `10X Cross` |
| `1769` | `0x757d...94ba` | `LONG` | 1,171,605.00 USD | `925.00` | `1558.31` | `1265.80` | `0.000000` | -269,835.59 USD | `-23.03%` | `10X Cross` |
| `1815` | `0xb911...5525` | `LONG` | 1,140,750.00 USD | `900.00` | `1294.82` | `1265.80` | `1035.49` | -24,587.82 USD | `-2.16%` | `10X Cross` |
| `1866` | `0xcf0a...856f` | `LONG` | 1,104,269.74 USD | `871.15` | `1292.19` | `1265.80` | `1029.27` | -21,425.11 USD | `-1.94%` | `4X Cross` |
| `1885` | `0xdf95...7d72` | `SHORT` | 1,081,298.38 USD | `853.23` | `1074.39` | `1265.80` | `44606.62` | -164,593.91 USD | `-15.22%` | `10X Cross` |
| `1916` | `0xb2f7...af9f` | `SHORT` | 1,052,854.53 USD | `830.72` | `746.63` | `1265.80` | `8168.30` | -432,615.50 USD | `-41.09%` | `10X Cross` |
| `1925` | `0x601c...4f54` | `SHORT` | 1,044,787.47 USD | `824.42` | `615.11` | `1265.80` | `3126.22` | -537,674.71 USD | `-51.46%` | `5X Cross` |
| `1937` | `0x8b61...c0c2` | `LONG` | 1,037,347.35 USD | `818.42` | `1274.67` | `1265.80` | `1005.21` | -5,866.69 USD | `-0.57%` | `4X Isolated` |
| `1940` | `0xae55...2236` | `LONG` | 1,035,489.25 USD | `817.47` | `1467.80` | `1265.80` | `0.000000` | -164,391.97 USD | `-15.88%` | `10X Cross` |
| `1986` | `0x0f02...5384` | `LONG` | 1,014,267.95 USD | `800.78` | `1290.36` | `1265.80` | `299.94` | -19,026.12 USD | `-1.88%` | `3X Cross` |
| `1988` | `0x9b0f...db40` | `LONG` | 1,013,360.00 USD | `800.00` | `1268.86` | `1265.80` | `799.32` | -1,729.76 USD | `-0.17%` | `10X Cross` |
| `1996` | `0xabdb...84ac` | `LONG` | 1,006,002.07 USD | `793.69` | `711.79` | `1265.80` | `664.63` | 441,061.71 USD | `+43.84%` | `3X Cross` |
| `1999` | `0x6e8f...4364` | `LONG` | 1,005,078.36 USD | `793.65` | `1260.00` | `1265.80` | `896.22` | 5,079.36 USD | `+0.51%` | `10X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `1017.00` | 10.17 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Long: 0.01K USD at 1017.0000 USD [API] | `2026-09-04 08:53:37` |
| `ANNOUNCEMENT` | `INFO` | `1327.50` | 13.28 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Long: 0.01K USD at 1327.5000 USD [API] | `2026-10-29 15:31:54` |
| `ANNOUNCEMENT` | `INFO` | `1327.50` | 61,343.78 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Long: 61.34K USD at 1327.5000 USD [API] | `2026-10-29 15:31:54` |
| `ANNOUNCEMENT` | `INFO` | `1319.10` | 10,420.89 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 10.42K USD at 1319.1000 USD [API] | `2026-10-29 18:31:05` |
| `ANNOUNCEMENT` | `INFO` | `1304.20` | 2,373.64 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 2.37K USD at 1304.2000 USD [API] | `2026-10-29 20:03:49` |
| `ANNOUNCEMENT` | `INFO` | `1304.20` | 899.90 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 0.90K USD at 1304.2000 USD [API] | `2026-10-29 20:03:49` |
| `ANNOUNCEMENT` | `INFO` | `1362.30` | 449.56 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Long: 0.45K USD at 1362.3000 USD [API] | `2026-10-29 15:57:56` |
| `ANNOUNCEMENT` | `INFO` | `1362.30` | 54.49 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Long: 0.05K USD at 1362.3000 USD [API] | `2026-10-29 15:57:56` |
| `ANNOUNCEMENT` | `INFO` | `1362.30` | 762.89 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Long: 0.76K USD at 1362.3000 USD [API] | `2026-10-29 15:57:56` |
| `ANNOUNCEMENT` | `INFO` | `1303.60` | 13,505.30 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 13.51K USD at 1303.6000 USD [API] | `2026-10-29 20:03:47` |
| `ANNOUNCEMENT` | `INFO` | `1303.60` | 495.37 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 0.50K USD at 1303.6000 USD [API] | `2026-10-29 20:03:47` |
| `ANNOUNCEMENT` | `INFO` | `1304.00` | 495.52 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 0.50K USD at 1304.0000 USD [API] | `2026-10-29 20:03:47` |
| `ANNOUNCEMENT` | `INFO` | `1282.60` | 115.43 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 0.12K USD at 1282.6000 USD [API] | `2026-10-29 20:35:42` |
| `ANNOUNCEMENT` | `INFO` | `1282.70` | 64.14 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 0.06K USD at 1282.7000 USD [API] | `2026-10-29 20:35:42` |
| `ANNOUNCEMENT` | `INFO` | `1283.60` | 115.52 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 0.12K USD at 1283.6000 USD [API] | `2026-10-29 20:35:36` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`1404.55` (Vol: 3,000,000.00 USD, Dist: `+11.24%`) | Long MP=`1176.48` (Vol: 3,400,000.00 USD, Dist: `--6.82%`)
  * 48H Horizon: Short MP=`1404.55` (Vol: 3,000,000.00 USD, Dist: `+11.24%`) | Long MP=`1176.48` (Vol: 3,400,000.00 USD, Dist: `--6.82%`)
  * 3D Horizon: Short MP=`1404.55` (Vol: 3,000,000.00 USD, Dist: `+11.24%`) | Long MP=`1176.48` (Vol: 3,400,000.00 USD, Dist: `--6.82%`)
  * 7D Horizon: Short MP=`1404.10` (Vol: 3,000,000.00 USD, Dist: `+11.21%`) | Long MP=`1176.74` (Vol: 4,900,000.00 USD, Dist: `--6.80%`)
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
| `5m` | `BALANCED` | 0.00 USD | 1,750.00 USD | 1,750.00 USD | 1,750.00 USD | `1` | `2026-10-30 11:10:00 UTC - 2026-10-30 11:15:00 UTC` |
| `15m` | `BALANCED` | 0.00 USD | 1,750.00 USD | 1,750.00 USD | 1,750.00 USD | `1` | `2026-10-30 11:00:00 UTC - 2026-10-30 11:15:00 UTC` |
| `1h` | `BALANCED` | 0.00 USD | 1,750.00 USD | 1,750.00 USD | 1,750.00 USD | `1` | `2026-10-30 11:00:00 UTC - 2026-10-30 12:00:00 UTC` |
| `4h` | `BALANCED` | 0.00 USD | 1,750.00 USD | 1,750.00 USD | 1,750.00 USD | `1` | `2026-10-30 08:00:00 UTC - 2026-10-30 12:00:00 UTC` |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `0 USD` | Total OI Tokens: `-`
  * 1h OI Change: `0.00%` | 4h OI Change: `0.00%` | 24h OI Change: `0.00%`
  * Exchange Breakdown: Binance=`-` | Bybit=`-` | OKX=`-` | Hyperliquid=`-`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `85.59K` | Last 24h: `171.90K` | Last 3d: `285.15K` | Last 7d: `847.79K`
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
| `5:00 UTC` | `1246.65` | `1246.77` | `1246.65` | `1252.35` | `1243.95` | 13,017,000.97 USD | 7,727,648.32 USD | 5,289,352.64 USD | 2,438,295.68 USD | `+18.73%` | `8B / 5S` |
| `0:00 UTC` | `1244.55` | `1245.81` | `1244.55` | `1249.05` | `1243.65` | 9,717,386.64 USD | 3,914,194.68 USD | 5,803,191.96 USD | -1,888,997.28 USD | `-19.44%` | `0B / 1S` |
| `5:00 UTC` | `1242.15` | `1244.40` | `1242.15` | `1249.35` | `1241.25` | 8,638,502.97 USD | 4,533,952.89 USD | 4,104,550.08 USD | 429,402.82 USD | `+4.97%` | `4B / 2S` |
| `0:00 UTC` | `1251.15` | `1247.35` | `1251.15` | `1251.75` | `1240.05` | 9,977,652.60 USD | 4,992,881.35 USD | 4,984,771.25 USD | 8,110.10 USD | `+0.08%` | `3B / 5S` |
| `5:00 UTC` | `1243.95` | `1249.40` | `1243.95` | `1256.55` | `1243.35` | 15,678,426.53 USD | 9,268,825.46 USD | 6,409,601.07 USD | 2,859,224.38 USD | `+18.24%` | `10B / 2S` |
| `0:00 UTC` | `1249.95` | `1250.19` | `1249.95` | `1256.25` | `1246.35` | 11,248,393.80 USD | 4,953,252.73 USD | 6,295,141.07 USD | -1,341,888.34 USD | `-11.93%` | `1B / 7S` |
| `5:00 UTC` | `1263.15` | `1259.85` | `1263.15` | `1266.15` | `1247.85` | 19,587,954.68 USD | 10,529,516.42 USD | 9,058,438.26 USD | 1,471,078.16 USD | `+7.51%` | `10B / 4S` |
| `0:00 UTC` | `1272.15` | `1270.75` | `1272.15` | `1276.65` | `1262.25` | 28,700,563.02 USD | 14,735,645.79 USD | 13,964,917.22 USD | 770,728.57 USD | `+2.69%` | `10B / 0S` |
| `5:00 UTC` | `1267.95` | `1266.37` | `1267.95` | `1276.95` | `1257.75` | 25,317,311.22 USD | 15,013,433.04 USD | 10,303,878.19 USD | 4,709,554.85 USD | `+18.60%` | `12B / 5S` |
| `0:00 UTC` | `1270.05` | `1271.66` | `1270.05` | `1276.65` | `1268.55` | 8,962,178.06 USD | 3,956,107.67 USD | 5,006,070.38 USD | -1,049,962.71 USD | `-11.72%` | `1B / 2S` |

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
| `5m` | -407,970.00 USD | -263,450.00 USD | **`DISTRIBUTION`** |
| `15m` | -228,630.00 USD | 2,000,000.00 USD | **`ACCUMULATION`** |
| `30m` | -821,850.00 USD | 879,450.00 USD | **`ACCUMULATION`** |
| `1h` | -1,140,000.00 USD | 8,710,000.00 USD | **`ACCUMULATION`** |
| `2h` | -3,060,000.00 USD | 11,500,000.00 USD | **`ACCUMULATION`** |
| `4h` | -26,070.00 USD | -5,040,000.00 USD | **`DISTRIBUTION`** |
| `6h` | -838,990.00 USD | -12,730,000.00 USD | **`DISTRIBUTION`** |
| `8h` | -900,830.00 USD | -17,620,000.00 USD | **`DISTRIBUTION`** |
| `12h` | 1,190,000.00 USD | -97,150.00 USD | **`ACCUMULATION`** |
| `24h` | 19,050,000.00 USD | 75,010,000.00 USD | **`ACCUMULATION`** |
| `1w` | 37,490,000.00 USD | 227,140,000.00 USD | **`ACCUMULATION`** |
| `30d` | 61,260,000.00 USD | -565,330,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-407.97K` | 15m=`-228.63K` | 1h=`-1.14M` | 24h=`+19.05M`
* Futures Capital Netflows: 5m=`-263.45K` | 15m=`+2.00M` | 1h=`+8.71M` | 24h=`+75.01M`
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
  * `2026-10-30 16:35:32 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 16:26:32 IST`: [marctomarket.com] - (Sentiment: `Neutral`)
  * `2026-10-30 15:50:32 IST`: [istat.it] - (Sentiment: `Neutral`)
  * `2026-10-30 16:37:32 IST`: [ec.europa.eu] - (Sentiment: `Neutral`)
  * `2026-10-30 16:37:32 IST`: [ec.europa.eu] - (Sentiment: `Neutral`)
  * `2026-10-30 16:37:32 IST`: [dailyforex.com] - (Sentiment: `Neutral`)
  * `2026-10-30 16:37:32 IST`: [breakingthenews.net] - (Sentiment: `Neutral`)
  * `2026-10-30 16:37:32 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 16:36:32 IST`: [@FirstSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 16:36:32 IST`: [destatis.de] - (Sentiment: `Neutral`)
  * `2026-10-30 16:36:32 IST`: [istat.it] - (Sentiment: `Neutral`)
  * `2026-10-30 16:36:32 IST`: [channelnewsasia.com] - (Sentiment: `Neutral`)
  * `2026-10-30 16:36:32 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 16:36:32 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 13:38:32 IST`: [kof.ethz.ch] - (Sentiment: `Neutral`)


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
  * Spread-Padded Stop Loss: `1222.78` (Risk Distance: `17.17` pts)
  * +2.5R Take Profit: `1282.87`
  * Mathematical Lot Sizing: **`0.58 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `1278.60` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `1295.77` (Risk Distance: `17.17` pts)
  * +2.5R Take Profit: `1235.68`
  * Mathematical Lot Sizing: **`0.58 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`1276.31`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
