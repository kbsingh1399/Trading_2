# 🏛️ SOVEREIGN CANDIDATE DOSSIER: ZECUSD
**Canonical Key**: `ZECUSD` | **Broker Instrument**: `ZECUSD.p` | **Asset Class**: `Crypto Altcoin`
**Timestamp**: `2026-10-30 16:39:49 IST` (`2026-10-30 11:09:49 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `1272.59` | **Live Ask Quote**: `1273.73` | **Mid Price**: `1273.16`
- **Spread Points**: `114.00` | **Spread BPS**: `8.95 bps` (Charter Threshold: `25.00 bps`)
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
  * Value Area High (VAH) = `1278.60` (Distance: `-0.48%`)
  * Point of Control (POC) = `1247.68` (Distance: `+1.98%`)
  * Value Area Low (VAL) = `1239.95` (Distance: `+2.62%`)
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
  * Golden Pocket Zone (0.618 - 0.650): `1268.07` - `1278.25`
  * Optimal Trade Entry (OTE 0.705): `1275.71`
  * Structural Invalidation Anchor (0.786): `1283.35`

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
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 16:32:44 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `12` | `0xb83d...6e36` | `SHORT` | 66,570,973.33 USD | `52,385.47` | `1336.45` | `1271.69` | `3171.32` | 3,439,594.07 USD | `+5.17%` | `3X Cross` |
| `21` | `0x5b5d...c060` | `SHORT` | 51,099,367.92 USD | `40,121.38` | `1478.36` | `1271.69` | `4753.12` | 8,214,667.19 USD | `+16.08%` | `3X Cross` |
| `36` | `0x7fda...17d1` | `SHORT` | 33,864,603.55 USD | `26,635.68` | `1262.58` | `1271.69` | `2587.86` | -234,984.52 USD | `-0.69%` | `5X Cross` |
| `79` | `0x60b0...991e` | `LONG` | 21,320,337.64 USD | `16,779.74` | `1179.65` | `1271.69` | `912.33` | 1,526,090.63 USD | `+7.16%` | `10X Cross` |
| `137` | `0xc36a...105b` | `LONG` | 14,616,439.24 USD | `11,510.82` | `1215.14` | `1271.69` | `961.14` | 629,158.21 USD | `+4.30%` | `10X Cross` |
| `173` | `0x8742...8427` | `LONG` | 11,698,418.39 USD | `9,201.21` | `1286.37` | `1271.69` | `712.39` | -137,751.60 USD | `-1.18%` | `10X Cross` |
| `190` | `0x58b2...11f3` | `LONG` | 10,906,795.00 USD | `8,563.08` | `1246.56` | `1271.69` | `387.01` | 232,377.42 USD | `+2.13%` | `10X Cross` |
| `195` | `0xad59...ba81` | `SHORT` | 10,706,412.49 USD | `8,425.00` | `330.91` | `1271.69` | `2145.51` | -7,918,454.72 USD | `-73.96%` | `10X Cross` |
| `196` | `0x9ffd...ce40` | `LONG` | 10,702,479.92 USD | `8,417.87` | `1252.36` | `1271.69` | `595.79` | 160,293.22 USD | `+1.50%` | `5X Cross` |
| `201` | `0xdd53...2b13` | `SHORT` | 10,422,751.46 USD | `8,195.92` | `741.54` | `1271.69` | `8352.30` | -4,345,155.10 USD | `-41.69%` | `3X Cross` |
| `221` | `0x880a...311c` | `SHORT` | 9,801,902.50 USD | `7,707.11` | `1367.50` | `1271.69` | `2232.57` | 737,581.70 USD | `+7.52%` | `10X Cross` |
| `233` | `0x9071...5c0b` | `LONG` | 9,558,234.23 USD | `7,517.29` | `1353.83` | `1271.69` | `108.98` | -618,895.73 USD | `-6.48%` | `2X Cross` |
| `234` | `0xbf73...5d58` | `LONG` | 9,552,145.50 USD | `7,500.00` | `1248.78` | `1271.69` | `110.33` | 186,299.88 USD | `+1.95%` | `10X Cross` |
| `266` | `0x2b61...2f6c` | `LONG` | 8,667,353.10 USD | `6,807.00` | `1453.56` | `1271.69` | `593.37` | -1,226,998.12 USD | `-14.16%` | `10X Cross` |
| `285` | `0x2ae5...83e7` | `LONG` | 8,184,391.20 USD | `6,436.80` | `1391.82` | `1271.69` | `0.000000` | -774,500.79 USD | `-9.46%` | `1X Cross` |
| `308` | `0xecb6...2b00` | `SHORT` | 7,775,335.70 USD | `6,115.57` | `1277.42` | `1271.69` | `6506.69` | 36,813.83 USD | `+0.47%` | `5X Cross` |
| `333` | `0x26b6...9a13` | `LONG` | 6,908,987.70 USD | `5,433.73` | `1282.23` | `1271.69` | `229.42` | -58,315.54 USD | `-0.84%` | `10X Cross` |
| `346` | `0x45d2...4029` | `SHORT` | 6,646,130.50 USD | `5,227.00` | `833.44` | `1271.69` | `8865.51` | -2,289,752.53 USD | `-34.45%` | `5X Cross` |
| `364` | `0xea00...a918` | `LONG` | 6,353,000.00 USD | `5,000.00` | `739.16` | `1271.69` | `0.000000` | 2,657,184.89 USD | `+41.83%` | `5X Cross` |
| `374` | `0xdd7a...8830` | `LONG` | 6,175,843.43 USD | `4,860.19` | `897.48` | `1271.69` | `777.81` | 1,813,939.76 USD | `+29.37%` | `10X Cross` |
| `420` | `0x469e...58a5` | `SHORT` | 5,299,744.61 USD | `4,163.52` | `1242.31` | `1271.69` | `1952.82` | -127,359.95 USD | `-2.40%` | `10X Cross` |
| `421` | `0x4cae...7c34` | `LONG` | 5,284,556.24 USD | `4,152.27` | `1172.97` | `1271.69` | `969.32` | 414,062.69 USD | `+7.84%` | `10X Cross` |
| `439` | `0xd4c1...3d1d` | `SHORT` | 4,998,394.67 USD | `3,931.41` | `1291.66` | `1271.69` | `2304.12` | 79,634.15 USD | `+1.59%` | `10X Cross` |
| `444` | `0xa61c...66b9` | `LONG` | 4,940,481.60 USD | `3,888.00` | `1148.34` | `1271.69` | `0.000000` | 475,739.46 USD | `+9.63%` | `10X Cross` |
| `466` | `0x9aa5...58af` | `SHORT` | 4,740,727.42 USD | `3,720.31` | `1205.51` | `1271.69` | `3621.48` | -255,840.62 USD | `-5.40%` | `10X Cross` |
| `471` | `0x0153...8052` | `SHORT` | 4,701,126.42 USD | `3,698.18` | `1307.82` | `1271.69` | `2504.97` | 135,444.33 USD | `+2.88%` | `1X Isolated` |
| `500` | `0xb122...e4ba` | `LONG` | 4,460,549.25 USD | `3,498.47` | `1265.25` | `1271.69` | `1024.53` | 34,097.72 USD | `+0.76%` | `10X Cross` |
| `524` | `0x382b...3e39` | `LONG` | 4,244,123.91 USD | `3,338.15` | `1220.72` | `1271.69` | `0.000000` | 169,182.69 USD | `+3.99%` | `10X Cross` |
| `537` | `0xd21d...90f1` | `LONG` | 4,146,350.00 USD | `3,250.00` | `1253.64` | `1271.69` | `876.19` | 72,008.27 USD | `+1.74%` | `4X Isolated` |
| `546` | `0x456f...cdf1` | `LONG` | 4,060,405.60 USD | `3,195.66` | `1267.53` | `1271.69` | `508.40` | 9,809.79 USD | `+0.24%` | `10X Cross` |
| `556` | `0x1338...c48e` | `LONG` | 4,008,909.45 USD | `3,149.43` | `1018.52` | `1271.69` | `820.49` | 801,163.90 USD | `+19.98%` | `4X Isolated` |
| `568` | `0xdbe0...d6d5` | `LONG` | 3,926,750.40 USD | `3,085.37` | `422.97` | `1271.69` | `338.80` | 2,621,745.91 USD | `+66.77%` | `3X Isolated` |
| `593` | `0x325e...9564` | `LONG` | 3,813,256.34 USD | `3,000.91` | `1298.07` | `1271.69` | `131.46` | -82,148.82 USD | `-2.15%` | `10X Cross` |
| `594` | `0x9c06...0560` | `SHORT` | 3,807,867.28 USD | `2,989.80` | `786.00` | `1271.69` | `2523.10` | -1,457,872.28 USD | `-38.29%` | `10X Cross` |
| `598` | `0x2e30...4cb5` | `SHORT` | 3,799,623.30 USD | `2,988.77` | `1282.25` | `1271.69` | `2888.01` | 32,726.35 USD | `+0.86%` | `2X Cross` |
| `605` | `0x27c9...d65d` | `SHORT` | 3,733,073.62 USD | `2,938.04` | `1254.41` | `1271.69` | `1719.72` | -47,563.58 USD | `-1.27%` | `10X Cross` |
| `662` | `0x5323...b23c` | `SHORT` | 3,390,721.40 USD | `2,666.50` | `1270.67` | `1271.69` | `3301.93` | -2,482.25 USD | `-0.07%` | `5X Cross` |
| `696` | `0xac48...3201` | `LONG` | 3,224,877.85 USD | `2,531.50` | `1378.58` | `1271.69` | `565.00` | -264,994.43 USD | `-8.22%` | `10X Cross` |
| `697` | `0xa183...0482` | `LONG` | 3,222,234.40 USD | `2,534.00` | `530.25` | `1271.69` | `444.73` | 1,878,571.68 USD | `+58.30%` | `5X Isolated` |
| `705` | `0x0871...e927` | `LONG` | 3,193,061.00 USD | `2,500.00` | `1276.50` | `1271.69` | `0.000000` | 1,811.00 USD | `+0.06%` | `10X Cross` |
| `707` | `0x9e2c...5508` | `LONG` | 3,183,750.00 USD | `2,500.00` | `1275.77` | `1271.69` | `442.70` | -5,675.91 USD | `-0.18%` | `10X Cross` |
| `713` | `0x71d0...8c26` | `SHORT` | 3,175,105.36 USD | `2,497.33` | `1268.47` | `1271.69` | `3442.15` | -7,306.60 USD | `-0.23%` | `10X Cross` |
| `723` | `0x9b86...6e6e` | `LONG` | 3,130,338.98 USD | `2,463.30` | `637.58` | `1271.69` | `882.66` | 1,559,789.69 USD | `+49.83%` | `3X Cross` |
| `805` | `0xf48f...10fe` | `LONG` | 2,830,349.54 USD | `2,218.49` | `1517.87` | `1271.69` | `961.45` | -537,037.28 USD | `-18.97%` | `3X Cross` |
| `836` | `0x5bc4...3b0c` | `SHORT` | 2,709,448.98 USD | `2,130.74` | `1089.65` | `1271.69` | `3664.20` | -387,691.41 USD | `-14.31%` | `5X Cross` |
| `845` | `0x8de4...b9aa` | `SHORT` | 2,663,507.52 USD | `2,091.29` | `1331.35` | `1271.69` | `1690.09` | 120,732.19 USD | `+4.53%` | `3X Cross` |
| `852` | `0x4fe2...ac59` | `SHORT` | 2,642,287.54 USD | `2,071.57` | `1478.56` | `1271.69` | `1826.11` | 420,658.68 USD | `+15.92%` | `10X Cross` |
| `860` | `0xdf57...93f5` | `LONG` | 2,612,516.90 USD | `2,054.35` | `1227.36` | `1271.69` | `897.43` | 91,094.85 USD | `+3.49%` | `4X Isolated` |
| `868` | `0xbcd4...0dd2` | `LONG` | 2,584,686.82 USD | `2,033.92` | `1228.20` | `1271.69` | `793.90` | 86,636.01 USD | `+3.35%` | `10X Cross` |
| `874` | `0x9a99...d21a` | `LONG` | 2,547,400.00 USD | `2,000.00` | `1278.44` | `1271.69` | `0.000000` | -9,473.67 USD | `-0.37%` | `10X Cross` |
| `876` | `0xf29c...9971` | `LONG` | 2,543,200.00 USD | `2,000.00` | `1254.95` | `1271.69` | `0.000000` | 33,302.93 USD | `+1.31%` | `10X Cross` |
| `896` | `0x77ee...2902` | `SHORT` | 2,477,880.00 USD | `1,946.03` | `759.84` | `1271.69` | `5680.35` | -999,202.49 USD | `-40.32%` | `10X Cross` |
| `909` | `0x3e2f...b269` | `SHORT` | 2,448,478.52 USD | `1,925.51` | `1134.87` | `1271.69` | `2977.36` | -263,279.66 USD | `-10.75%` | `10X Cross` |
| `921` | `0x4f12...618b` | `SHORT` | 2,415,291.84 USD | `1,896.28` | `1608.30` | `1271.69` | `2116.98` | 634,492.55 USD | `+26.27%` | `3X Cross` |
| `931` | `0x039c...0ebd` | `SHORT` | 2,380,186.29 USD | `1,873.13` | `1250.08` | `1271.69` | `3287.58` | -38,618.75 USD | `-1.62%` | `10X Cross` |
| `965` | `0x866d...d6e1` | `LONG` | 2,294,550.27 USD | `1,802.05` | `674.73` | `1271.69` | `109.14` | 1,078,648.95 USD | `+47.01%` | `10X Cross` |
| `990` | `0x2309...a2d9` | `LONG` | 2,228,045.97 USD | `1,750.37` | `1186.09` | `1271.69` | `807.29` | 151,951.86 USD | `+6.82%` | `8X Cross` |
| `1022` | `0x265e...7f70` | `LONG` | 2,103,821.24 USD | `1,651.74` | `1382.98` | `1271.69` | `0.000000` | -180,501.52 USD | `-8.58%` | `3X Cross` |
| `1027` | `0x3e47...aaf6` | `LONG` | 2,087,729.65 USD | `1,636.28` | `1278.38` | `1271.69` | `1046.38` | -4,062.13 USD | `-0.19%` | `10X Cross` |
| `1028` | `0xfe7c...b7ae` | `SHORT` | 2,087,138.38 USD | `1,642.64` | `1346.92` | `1271.69` | `5572.87` | 125,370.24 USD | `+6.01%` | `10X Cross` |
| `1035` | `0x2edd...8179` | `SHORT` | 2,079,984.97 USD | `1,635.98` | `1261.55` | `1271.69` | `2831.41` | -16,122.09 USD | `-0.78%` | `10X Cross` |
| `1042` | `0x3205...40bb` | `SHORT` | 2,070,810.22 USD | `1,629.02` | `1262.15` | `1271.69` | `2144.50` | -14,748.32 USD | `-0.71%` | `10X Cross` |
| `1051` | `0x7f75...9edf` | `LONG` | 2,053,595.16 USD | `1,612.56` | `1200.27` | `1271.69` | `987.01` | 118,081.24 USD | `+5.75%` | `10X Cross` |
| `1065` | `0xfc27...9d9d` | `SHORT` | 2,040,299.76 USD | `1,604.64` | `1295.09` | `1271.69` | `12726.28` | 37,846.05 USD | `+1.85%` | `10X Cross` |
| `1069` | `0x6646...6de5` | `SHORT` | 2,033,440.00 USD | `1,600.00` | `660.64` | `1271.69` | `4314.11` | -976,415.03 USD | `-48.02%` | `10X Cross` |
| `1071` | `0x023a...2355` | `SHORT` | 2,026,662.46 USD | `1,594.04` | `1309.94` | `1271.69` | `4388.51` | 61,431.80 USD | `+3.03%` | `10X Cross` |
| `1090` | `0xab59...59b5` | `LONG` | 1,988,895.59 USD | `1,565.32` | `1342.15` | `1271.69` | `832.94` | -111,999.63 USD | `-5.63%` | `10X Cross` |
| `1151` | `0xcf67...eb24` | `LONG` | 1,912,500.00 USD | `1,500.00` | `887.05` | `1271.69` | `594.02` | 581,928.63 USD | `+30.43%` | `10X Cross` |
| `1169` | `0x7277...0b98` | `SHORT` | 1,876,243.12 USD | `1,475.73` | `1287.86` | `1271.69` | `2174.47` | 24,289.00 USD | `+1.29%` | `10X Cross` |
| `1232` | `0x2ab7...c2f8` | `LONG` | 1,781,168.62 USD | `1,400.51` | `813.26` | `1271.69` | `790.02` | 642,186.93 USD | `+36.05%` | `3X Cross` |
| `1234` | `0x926a...af36` | `LONG` | 1,781,114.78 USD | `1,401.68` | `1254.50` | `1271.69` | `1187.95` | 22,712.88 USD | `+1.28%` | `10X Isolated` |
| `1256` | `0x11be...8b1d` | `LONG` | 1,748,129.60 USD | `1,375.83` | `1206.55` | `1271.69` | `1134.71` | 88,121.64 USD | `+5.04%` | `10X Isolated` |
| `1309` | `0xef96...9383` | `SHORT` | 1,648,593.47 USD | `1,297.39` | `1262.03` | `1271.69` | `3856.52` | -11,251.52 USD | `-0.68%` | `10X Cross` |
| `1321` | `0xdf83...3cff` | `SHORT` | 1,636,016.08 USD | `1,287.40` | `1260.50` | `1271.69` | `1889.60` | -13,242.46 USD | `-0.81%` | `10X Cross` |
| `1340` | `0xe065...0f85` | `SHORT` | 1,604,398.53 USD | `1,262.61` | `1087.02` | `1271.69` | `1544.00` | -231,922.40 USD | `-14.46%` | `10X Cross` |
| `1352` | `0x413c...886c` | `LONG` | 1,588,250.00 USD | `1,250.00` | `1237.51` | `1271.69` | `0.000000` | 41,360.54 USD | `+2.60%` | `10X Cross` |
| `1404` | `0x2847...d47b` | `LONG` | 1,540,568.09 USD | `1,211.71` | `1232.45` | `1271.69` | `0.000000` | 47,200.49 USD | `+3.06%` | `5X Cross` |
| `1421` | `0x266b...efcb` | `LONG` | 1,525,080.00 USD | `1,200.00` | `893.76` | `1271.69` | `392.03` | 452,570.30 USD | `+29.68%` | `10X Cross` |
| `1422` | `0x5975...9abd` | `LONG` | 1,524,720.00 USD | `1,200.00` | `1179.54` | `1271.69` | `510.60` | 109,277.21 USD | `+7.17%` | `5X Cross` |
| `1453` | `0xb897...ebc1` | `SHORT` | 1,492,298.90 USD | `1,173.56` | `1256.04` | `1271.69` | `1348.94` | -18,255.61 USD | `-1.22%` | `10X Cross` |
| `1463` | `0x69cc...14fd` | `SHORT` | 1,476,553.10 USD | `1,161.36` | `675.33` | `1271.69` | `7977.95` | -692,247.58 USD | `-46.88%` | `10X Cross` |
| `1470` | `0x3fc5...c0c1` | `SHORT` | 1,459,207.86 USD | `1,148.44` | `1264.34` | `1271.69` | `2718.83` | -7,194.09 USD | `-0.49%` | `10X Cross` |
| `1519` | `0x5f94...4b96` | `LONG` | 1,417,274.86 USD | `1,115.27` | `538.00` | `1271.69` | `0.000000` | 817,257.22 USD | `+57.66%` | `10X Cross` |
| `1524` | `0xe35c...a1d3` | `LONG` | 1,412,205.15 USD | `1,111.36` | `1311.66` | `1271.69` | `691.00` | -45,518.99 USD | `-3.22%` | `2X Isolated` |
| `1540` | `0x71df...a23d` | `SHORT` | 1,401,185.62 USD | `1,098.28` | `513.50` | `1271.69` | `2558.92` | -837,215.43 USD | `-59.75%` | `2X Cross` |
| `1558` | `0x38f9...cb04` | `SHORT` | 1,385,927.71 USD | `1,090.08` | `1259.78` | `1271.69` | `2043.13` | -12,668.13 USD | `-0.91%` | `10X Cross` |
| `1577` | `0xbfc7...80b4` | `SHORT` | 1,368,367.50 USD | `1,075.00` | `558.03` | `1271.69` | `2599.38` | -768,488.77 USD | `-56.16%` | `10X Cross` |
| `1579` | `0x8b9d...7b28` | `SHORT` | 1,361,690.82 USD | `1,070.68` | `1272.16` | `1271.69` | `3317.39` | 387.42 USD | `+0.03%` | `10X Cross` |
| `1606` | `0x123d...3bff` | `SHORT` | 1,326,938.40 USD | `1,044.34` | `519.62` | `1271.69` | `4122.29` | -784,280.20 USD | `-59.10%` | `10X Cross` |
| `1656` | `0x8ab1...15ef` | `LONG` | 1,273,619.40 USD | `1,000.00` | `1275.75` | `1271.69` | `960.61` | -2,135.53 USD | `-0.17%` | `10X Cross` |
| `1658` | `0x668c...ea2e` | `SHORT` | 1,272,900.00 USD | `1,000.00` | `1406.98` | `1271.69` | `4212.85` | 134,081.99 USD | `+10.53%` | `10X Cross` |
| `1660` | `0x98e0...d7e0` | `LONG` | 1,271,400.00 USD | `1,000.00` | `1276.62` | `1271.69` | `931.79` | -5,222.14 USD | `-0.41%` | `10X Cross` |
| `1662` | `0xe282...df29` | `LONG` | 1,270,700.00 USD | `1,000.00` | `420.99` | `1271.69` | `791.88` | 849,713.14 USD | `+66.87%` | `10X Cross` |
| `1685` | `0x17f0...094f` | `LONG` | 1,252,709.65 USD | `984.30` | `1287.23` | `1271.69` | `537.06` | -14,310.51 USD | `-1.14%` | `5X Cross` |
| `1715` | `0x51f6...2b39` | `SHORT` | 1,225,972.88 USD | `964.27` | `1299.77` | `1271.69` | `2492.38` | 27,354.80 USD | `+2.23%` | `10X Cross` |
| `1725` | `0x4e23...20c3` | `LONG` | 1,218,852.33 USD | `956.53` | `1265.15` | `1271.69` | `0.000000` | 8,700.89 USD | `+0.71%` | `4X Cross` |
| `1743` | `0xf096...7553` | `SHORT` | 1,198,068.30 USD | `940.68` | `1257.96` | `1271.69` | `3059.44` | -14,734.58 USD | `-1.23%` | `10X Cross` |
| `1764` | `0x757d...94ba` | `LONG` | 1,176,230.00 USD | `925.00` | `1558.31` | `1271.69` | `0.000000` | -265,210.59 USD | `-22.55%` | `10X Cross` |
| `1811` | `0xb911...5525` | `LONG` | 1,143,540.00 USD | `900.00` | `1294.82` | `1271.69` | `1035.49` | -21,797.82 USD | `-1.91%` | `10X Cross` |
| `1856` | `0xcf0a...856f` | `LONG` | 1,109,513.54 USD | `871.15` | `1292.19` | `1271.69` | `1029.54` | -16,181.31 USD | `-1.46%` | `4X Cross` |
| `1879` | `0xdf95...7d72` | `SHORT` | 1,086,588.41 USD | `853.23` | `1074.39` | `1271.69` | `44369.98` | -169,883.94 USD | `-15.63%` | `10X Cross` |
| `1910` | `0xb2f7...af9f` | `SHORT` | 1,055,671.33 USD | `830.72` | `746.63` | `1271.69` | `8163.11` | -435,432.30 USD | `-41.25%` | `10X Cross` |
| `1921` | `0x601c...4f54` | `SHORT` | 1,049,231.83 USD | `824.42` | `615.11` | `1271.69` | `3122.02` | -542,119.08 USD | `-51.67%` | `5X Cross` |
| `1929` | `0x8b61...c0c2` | `LONG` | 1,039,884.45 USD | `818.42` | `1274.67` | `1271.69` | `1005.21` | -3,329.59 USD | `-0.32%` | `4X Isolated` |
| `1931` | `0xae55...2236` | `LONG` | 1,039,413.10 USD | `817.47` | `1467.80` | `1271.69` | `0.000000` | -160,468.11 USD | `-15.44%` | `10X Cross` |
| `1975` | `0x0f02...5384` | `LONG` | 1,018,111.69 USD | `800.78` | `1290.36` | `1271.69` | `297.27` | -15,182.38 USD | `-1.49%` | `3X Cross` |
| `1976` | `0x9b0f...db40` | `LONG` | 1,017,760.00 USD | `800.00` | `1268.86` | `1271.69` | `798.89` | 2,670.24 USD | `+0.26%` | `10X Cross` |
| `1990` | `0xabdb...84ac` | `LONG` | 1,010,843.58 USD | `793.69` | `711.79` | `1271.69` | `664.63` | 445,903.22 USD | `+44.11%` | `3X Cross` |
| `1997` | `0x6e8f...4364` | `LONG` | 1,008,491.06 USD | `793.65` | `1260.00` | `1271.69` | `893.17` | 8,492.06 USD | `+0.84%` | `10X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `1087.00` | 239.14 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Long: 0.24K USD at 1087.0000 USD [API] | `2026-10-15 02:24:27` |
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
| `5m` | `BALANCED` | 0.00 USD | 1,750.00 USD | 1,750.00 USD | 1,750.00 USD | `1` | `2026-10-30 11:00:00 UTC - 2026-10-30 11:05:00 UTC` |
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
  * Current Rate: `85.57K` | Last 24h: `171.90K` | Last 3d: `285.15K` | Last 7d: `847.79K`
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
| `5m` | 45,900.00 USD | 4,400,000.00 USD | **`ACCUMULATION`** |
| `15m` | -416,160.00 USD | 5,390,000.00 USD | **`ACCUMULATION`** |
| `30m` | -1,130,000.00 USD | 8,590,000.00 USD | **`ACCUMULATION`** |
| `1h` | -1,420,000.00 USD | 8,910,000.00 USD | **`ACCUMULATION`** |
| `2h` | -3,010,000.00 USD | 14,100,000.00 USD | **`ACCUMULATION`** |
| `4h` | -458,590.00 USD | -5,430,000.00 USD | **`DISTRIBUTION`** |
| `6h` | -329,120.00 USD | -11,580,000.00 USD | **`DISTRIBUTION`** |
| `8h` | -333,300.00 USD | -5,390,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -154,950.00 USD | -4,920,000.00 USD | **`DISTRIBUTION`** |
| `24h` | 20,040,000.00 USD | 77,790,000.00 USD | **`ACCUMULATION`** |
| `1w` | 36,590,000.00 USD | 234,680,000.00 USD | **`ACCUMULATION`** |
| `30d` | 61,510,000.00 USD | -560,260,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+45.90K` | 15m=`-416.16K` | 1h=`-1.42M` | 24h=`+20.04M`
* Futures Capital Netflows: 5m=`+4.40M` | 15m=`+5.39M` | 1h=`+8.91M` | 24h=`+77.79M`
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
  * Spread-Padded Stop Loss: `1222.75` (Risk Distance: `17.20` pts)
  * +2.5R Take Profit: `1282.95`
  * Mathematical Lot Sizing: **`0.58 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `1278.60` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `1295.80` (Risk Distance: `17.20` pts)
  * +2.5R Take Profit: `1235.60`
  * Mathematical Lot Sizing: **`0.58 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`1283.35`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
