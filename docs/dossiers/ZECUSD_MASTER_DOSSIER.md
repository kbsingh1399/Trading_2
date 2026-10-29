# 🏛️ SOVEREIGN CANDIDATE DOSSIER: ZECUSD
**Canonical Key**: `ZECUSD` | **Broker Instrument**: `ZECUSD.p` | **Asset Class**: `Crypto Altcoin`
**Timestamp**: `2026-10-30 03:52:33 IST` (`2026-10-29 22:22:33 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `1251.19` | **Live Ask Quote**: `1252.53` | **Mid Price**: `1251.86`
- **Spread Points**: `134.00` | **Spread BPS**: `10.70 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `1280.70` | VWAP Z-Score: `-0.75` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `22.75` (Volatility Regime: `HIGH_EXPANSION`)
  * 14-Period RSI: `35.80` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `1393.56` | Lower -3.00σ Band: `1167.85`
  * Upper +2.51σ Band: `1375.12` | Lower -2.51σ Band: `1186.29`
  * Upper +2.01σ Band: `1356.31` | Lower -2.01σ Band: `1205.09`
  * Upper +2.00σ Band: `1355.94` | Lower -2.00σ Band: `1205.47`
  * Upper +1.28σ Band: `1328.85` | Lower -1.28σ Band: `1232.55`
  * Upper +1.00σ Band: `1318.32` | Lower -1.00σ Band: `1243.09`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`1270.79` | EMA-20=`1288.21` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`1292.33` (Slope: `+0.0000`) | EMA-100=`1287.53`
  * Institutional Anchors: EMA-144=`1283.94` | EMA-200=`1280.33` (Slope: `-0.0006`) | EMA-233=`1279.70`
- **Range Boundaries**: 24H High=`1396.49` | 24H Low=`1206.89` | Weekly High=`1396.49` | Weekly Low=`1206.89`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `1277.75` (Distance: `-2.15%`)
  * Point of Control (POC) = `1268.53` (Distance: `-1.44%`)
  * Value Area Low (VAL) = `1249.72` (Distance: `+0.05%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`1309.91` | POC=`1246.71` | VAL=`1230.27`
  * Prior Day Extremes: PDH=`1396.49` | PDL=`1206.89` | PDC=`1244.38`
  * Monday Range Blueprint: High=`1267.53` | Mid=`1222.14` | Low=`1176.75`
  * Developing Weekly Value Area: Weekly VAH=`1296.14` | Weekly POC=`1239.01` | Weekly VAL=`1196.53`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`1296.00` | Low=`1240.69`
  * London Session (08:00-16:00 UTC): High=`1256.87` | Low=`1246.85`
  * New York Session (13:00-21:00 UTC): High=`1259.37` | Low=`1244.35`
  * Initial Balance (First Hour): IB High=`1255.62` | IB Low=`1248.10`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `1246.85` - `1256.87`
  * Optimal Trade Entry (OTE 0.705): `1254.36`
  * Structural Invalidation Anchor (0.786): `1261.87`

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
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 03:45:41 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `16` | `0xb83d...6e36` | `SHORT` | 65,481,837.50 USD | `52,385.47` | `1336.45` | `1245.70` | `4028.22` | 4,528,729.90 USD | `+6.92%` | `3X Cross` |
| `22` | `0x5b5d...c060` | `SHORT` | 51,154,759.50 USD | `40,121.38` | `1478.36` | `1245.70` | `5430.66` | 8,159,275.61 USD | `+15.95%` | `3X Cross` |
| `45` | `0x7fda...17d1` | `SHORT` | 29,047,929.93 USD | `23,273.72` | `1262.40` | `1245.70` | `2960.79` | 332,726.28 USD | `+1.15%` | `5X Cross` |
| `84` | `0x60b0...991e` | `LONG` | 20,964,607.16 USD | `16,779.74` | `1179.65` | `1245.70` | `931.50` | 1,170,360.14 USD | `+5.58%` | `10X Cross` |
| `143` | `0xc36a...105b` | `LONG` | 14,385,071.75 USD | `11,510.82` | `1215.14` | `1245.70` | `965.10` | 397,790.73 USD | `+2.77%` | `10X Cross` |
| `162` | `0x9071...5c0b` | `LONG` | 13,134,341.98 USD | `10,517.29` | `1353.83` | `1245.70` | `0.0163` | -1,104,276.89 USD | `-8.41%` | `1X Cross` |
| `182` | `0x8742...8427` | `LONG` | 11,492,311.29 USD | `9,201.21` | `1286.37` | `1245.70` | `711.67` | -343,858.70 USD | `-2.99%` | `10X Cross` |
| `206` | `0x9ffd...ce40` | `LONG` | 10,616,655.51 USD | `8,475.72` | `1256.56` | `1245.70` | `610.41` | -33,554.27 USD | `-0.32%` | `5X Cross` |
| `207` | `0xad59...ba81` | `SHORT` | 10,531,250.00 USD | `8,425.00` | `330.91` | `1245.70` | `2145.05` | -7,743,292.23 USD | `-73.53%` | `10X Cross` |
| `215` | `0xdd53...2b13` | `SHORT` | 10,205,349.08 USD | `8,168.20` | `739.52` | `1245.70` | `8684.16` | -4,164,838.89 USD | `-40.81%` | `3X Cross` |
| `218` | `0xbf73...5d58` | `LONG` | 10,007,200.00 USD | `8,000.00` | `1291.41` | `1245.70` | `292.79` | -324,056.76 USD | `-3.24%` | `10X Cross` |
| `237` | `0x880a...311c` | `SHORT` | 9,629,263.23 USD | `7,707.11` | `1367.50` | `1245.70` | `2265.60` | 910,220.97 USD | `+9.45%` | `10X Cross` |
| `280` | `0x2b61...2f6c` | `LONG` | 8,484,925.50 USD | `6,807.00` | `1453.56` | `1245.70` | `526.10` | -1,409,425.72 USD | `-16.61%` | `10X Cross` |
| `294` | `0x58b2...11f3` | `LONG` | 8,076,911.08 USD | `6,463.08` | `1257.17` | `1245.70` | `147.61` | -48,247.83 USD | `-0.60%` | `10X Cross` |
| `297` | `0x2ae5...83e7` | `LONG` | 8,038,490.19 USD | `6,436.80` | `1391.82` | `1245.70` | `0.000000` | -920,401.81 USD | `-11.45%` | `1X Cross` |
| `344` | `0x26b6...9a13` | `LONG` | 6,782,381.79 USD | `5,433.73` | `1282.23` | `1245.70` | `215.76` | -184,921.45 USD | `-2.73%` | `10X Cross` |
| `359` | `0x45d2...4029` | `SHORT` | 6,528,523.00 USD | `5,227.00` | `833.44` | `1245.70` | `8966.74` | -2,172,145.03 USD | `-33.27%` | `5X Cross` |
| `377` | `0xecb6...2b00` | `SHORT` | 6,263,886.43 USD | `5,030.83` | `1305.05` | `1245.70` | `6765.72` | 301,594.28 USD | `+4.81%` | `5X Cross` |
| `380` | `0xea00...a918` | `LONG` | 6,246,500.00 USD | `5,000.00` | `739.16` | `1245.70` | `0.000000` | 2,550,684.89 USD | `+40.83%` | `5X Cross` |
| `389` | `0xdd7a...8830` | `LONG` | 6,074,751.48 USD | `4,860.19` | `897.48` | `1245.70` | `789.43` | 1,712,847.81 USD | `+28.20%` | `10X Cross` |
| `434` | `0x4cae...7c34` | `LONG` | 5,059,108.42 USD | `4,004.36` | `999.34` | `1245.70` | `929.40` | 1,057,380.27 USD | `+20.90%` | `10X Cross` |
| `455` | `0xa61c...66b9` | `LONG` | 4,860,000.00 USD | `3,888.00` | `1148.34` | `1245.70` | `0.000000` | 395,257.86 USD | `+8.13%` | `10X Cross` |
| `462` | `0x9aa5...58af` | `SHORT` | 4,725,537.76 USD | `3,720.31` | `1205.51` | `1245.70` | `3632.91` | -240,650.96 USD | `-5.09%` | `10X Cross` |
| `475` | `0x0153...8052` | `SHORT` | 4,618,657.00 USD | `3,698.18` | `1307.82` | `1245.70` | `2504.73` | 217,913.75 USD | `+4.72%` | `1X Isolated` |
| `545` | `0xd21d...90f1` | `LONG` | 4,062,500.00 USD | `3,250.00` | `1253.64` | `1245.70` | `875.93` | -11,841.73 USD | `-0.29%` | `4X Isolated` |
| `559` | `0x1338...c48e` | `LONG` | 3,977,730.09 USD | `3,149.43` | `1018.52` | `1245.70` | `820.23` | 769,984.55 USD | `+19.36%` | `4X Isolated` |
| `579` | `0x456f...cdf1` | `LONG` | 3,915,443.62 USD | `3,134.11` | `1268.47` | `1245.70` | `493.71` | -60,065.84 USD | `-1.53%` | `10X Cross` |
| `581` | `0xd4c1...3d1d` | `SHORT` | 3,901,314.06 USD | `3,123.05` | `1299.54` | `1245.70` | `2879.00` | 157,217.52 USD | `+4.03%` | `10X Cross` |
| `582` | `0x382b...3e39` | `LONG` | 3,890,161.14 USD | `3,114.87` | `1211.32` | `1245.70` | `0.000000` | 117,047.66 USD | `+3.01%` | `10X Cross` |
| `589` | `0xdbe0...d6d5` | `LONG` | 3,853,318.59 USD | `3,085.37` | `422.97` | `1245.70` | `338.54` | 2,548,314.10 USD | `+66.13%` | `3X Isolated` |
| `597` | `0x27c9...d65d` | `SHORT` | 3,806,479.68 USD | `3,046.89` | `1254.41` | `1245.70` | `1771.06` | 15,573.02 USD | `+0.41%` | `10X Cross` |
| `602` | `0x325e...9564` | `LONG` | 3,752,387.50 USD | `3,001.91` | `1301.41` | `1245.70` | `171.79` | -154,321.71 USD | `-4.11%` | `10X Cross` |
| `609` | `0x9c06...0560` | `SHORT` | 3,726,486.72 USD | `2,989.80` | `786.00` | `1245.70` | `2562.34` | -1,376,491.72 USD | `-36.94%` | `10X Cross` |
| `622` | `0x2e30...4cb5` | `SHORT` | 3,669,293.18 USD | `2,938.02` | `1297.89` | `1245.70` | `2894.77` | 143,921.32 USD | `+3.92%` | `2X Cross` |
| `626` | `0xac48...3201` | `LONG` | 3,659,849.34 USD | `2,929.52` | `1378.58` | `1245.70` | `646.97` | -378,724.89 USD | `-10.35%` | `10X Cross` |
| `716` | `0xa183...0482` | `LONG` | 3,164,966.00 USD | `2,534.00` | `530.25` | `1245.70` | `444.47` | 1,821,303.28 USD | `+57.55%` | `5X Isolated` |
| `717` | `0x0871...e927` | `LONG` | 3,160,750.00 USD | `2,500.00` | `1276.50` | `1245.70` | `0.000000` | -30,500.00 USD | `-0.96%` | `10X Cross` |
| `742` | `0x9b86...6e6e` | `LONG` | 3,084,125.00 USD | `2,467.30` | `637.58` | `1245.70` | `889.69` | 1,511,025.40 USD | `+48.99%` | `3X Cross` |
| `785` | `0xb2f7...af9f` | `SHORT` | 2,892,150.00 USD | `2,313.72` | `746.63` | `1245.70` | `4410.14` | -1,164,661.25 USD | `-40.27%` | `10X Cross` |
| `812` | `0xf48f...10fe` | `LONG` | 2,773,112.50 USD | `2,218.49` | `1517.87` | `1245.70` | `980.83` | -594,274.32 USD | `-21.43%` | `3X Cross` |
| `847` | `0x5bc4...3b0c` | `SHORT` | 2,662,359.63 USD | `2,130.74` | `1089.65` | `1245.70` | `3684.46` | -340,602.05 USD | `-12.79%` | `5X Cross` |
| `866` | `0x8de4...b9aa` | `SHORT` | 2,606,583.86 USD | `2,091.29` | `1331.35` | `1245.70` | `1689.86` | 177,655.85 USD | `+6.82%` | `3X Cross` |
| `872` | `0x4fe2...ac59` | `SHORT` | 2,587,183.77 USD | `2,071.57` | `1478.56` | `1245.70` | `1841.13` | 475,762.44 USD | `+18.39%` | `10X Cross` |
| `900` | `0x9a99...d21a` | `LONG` | 2,496,200.00 USD | `2,000.00` | `1278.44` | `1245.70` | `0.000000` | -60,673.67 USD | `-2.43%` | `10X Cross` |
| `910` | `0x71d0...8c26` | `SHORT` | 2,470,389.29 USD | `1,979.32` | `1289.75` | `1245.70` | `4112.68` | 82,442.51 USD | `+3.34%` | `10X Cross` |
| `927` | `0x77ee...2902` | `SHORT` | 2,434,288.93 USD | `1,946.03` | `759.84` | `1245.70` | `5313.86` | -955,611.42 USD | `-39.26%` | `10X Cross` |
| `937` | `0x3e2f...b269` | `SHORT` | 2,406,309.85 USD | `1,925.51` | `1134.87` | `1245.70` | `2931.78` | -221,110.99 USD | `-9.19%` | `10X Cross` |
| `943` | `0x5323...b23c` | `SHORT` | 2,392,432.97 USD | `1,916.86` | `1286.12` | `1245.70` | `4169.65` | 72,878.04 USD | `+3.05%` | `5X Cross` |
| `945` | `0xe097...d0fe` | `LONG` | 2,390,227.80 USD | `1,913.56` | `1261.17` | `1245.70` | `0.000000` | -23,098.37 USD | `-0.97%` | `10X Cross` |
| `951` | `0x4f12...618b` | `SHORT` | 2,366,747.07 USD | `1,896.28` | `1608.30` | `1245.70` | `2116.75` | 683,037.32 USD | `+28.86%` | `3X Cross` |
| `997` | `0x866d...d6e1` | `LONG` | 2,252,202.09 USD | `1,802.05` | `674.73` | `1245.70` | `221.29` | 1,036,300.78 USD | `+46.01%` | `10X Cross` |
| `1015` | `0x2309...a2d9` | `LONG` | 2,195,664.13 USD | `1,750.37` | `1186.09` | `1245.70` | `814.94` | 119,570.02 USD | `+5.45%` | `8X Cross` |
| `1036` | `0x2edd...8179` | `SHORT` | 2,127,312.50 USD | `1,701.85` | `1261.58` | `1245.70` | `3090.29` | 19,706.35 USD | `+0.93%` | `10X Cross` |
| `1040` | `0x023a...2355` | `SHORT` | 2,120,305.36 USD | `1,696.38` | `1313.00` | `1245.70` | `5199.96` | 107,041.93 USD | `+5.05%` | `10X Cross` |
| `1070` | `0xfe7c...b7ae` | `SHORT` | 2,049,432.41 USD | `1,640.99` | `1347.05` | `1245.70` | `7088.59` | 161,056.77 USD | `+7.86%` | `10X Cross` |
| `1073` | `0x3e47...aaf6` | `LONG` | 2,045,350.00 USD | `1,636.28` | `1278.38` | `1245.70` | `1049.20` | -46,441.79 USD | `-2.27%` | `10X Cross` |
| `1079` | `0xa271...a3f7` | `LONG` | 2,033,740.64 USD | `1,631.43` | `1190.60` | `1245.70` | `910.32` | 91,358.84 USD | `+4.49%` | `4X Cross` |
| `1088` | `0x7f75...9edf` | `LONG` | 2,019,268.35 USD | `1,605.78` | `1199.97` | `1245.70` | `977.80` | 92,376.46 USD | `+4.57%` | `10X Cross` |
| `1091` | `0x265e...7f70` | `LONG` | 2,014,988.92 USD | `1,601.74` | `1388.09` | `1245.70` | `0.000000` | -208,376.09 USD | `-10.34%` | `3X Cross` |
| `1105` | `0x6646...6de5` | `SHORT` | 1,998,560.00 USD | `1,600.00` | `660.64` | `1245.70` | `4403.66` | -941,535.03 USD | `-47.11%` | `10X Cross` |
| `1123` | `0xdf57...93f5` | `LONG` | 1,974,226.07 USD | `1,579.76` | `1218.38` | `1245.70` | `780.17` | 49,470.09 USD | `+2.51%` | `3X Isolated` |
| `1140` | `0xab59...59b5` | `LONG` | 1,956,401.74 USD | `1,565.32` | `1342.15` | `1245.70` | `833.50` | -144,493.48 USD | `-7.39%` | `10X Cross` |
| `1191` | `0xcf67...eb24` | `LONG` | 1,876,800.00 USD | `1,500.00` | `887.05` | `1245.70` | `686.05` | 546,228.63 USD | `+29.10%` | `10X Cross` |
| `1201` | `0xb695...a92d` | `LONG` | 1,852,267.00 USD | `1,483.00` | `1249.80` | `1245.70` | `0.000000` | -1,191.86 USD | `-0.06%` | `10X Cross` |
| `1283` | `0x2ab7...c2f8` | `LONG` | 1,748,116.58 USD | `1,400.51` | `813.26` | `1245.70` | `805.42` | 609,134.90 USD | `+34.85%` | `3X Cross` |
| `1298` | `0x11be...8b1d` | `LONG` | 1,718,824.42 USD | `1,375.83` | `1206.55` | `1245.70` | `1134.45` | 58,816.46 USD | `+3.42%` | `10X Isolated` |
| `1409` | `0xe065...0f85` | `SHORT` | 1,573,717.10 USD | `1,262.61` | `1087.02` | `1245.70` | `1829.05` | -201,240.98 USD | `-12.79%` | `10X Cross` |
| `1421` | `0x039c...0ebd` | `SHORT` | 1,563,187.50 USD | `1,250.55` | `1239.86` | `1245.70` | `3636.66` | -12,676.22 USD | `-0.81%` | `10X Cross` |
| `1440` | `0x7277...0b98` | `SHORT` | 1,543,329.51 USD | `1,234.96` | `1298.48` | `1245.70` | `2426.19` | 60,239.91 USD | `+3.90%` | `10X Cross` |
| `1472` | `0x5975...9abd` | `LONG` | 1,499,160.00 USD | `1,200.00` | `1179.54` | `1245.70` | `511.73` | 83,717.21 USD | `+5.58%` | `5X Cross` |
| `1475` | `0x3205...40bb` | `SHORT` | 1,491,381.46 USD | `1,194.73` | `1267.14` | `1245.70` | `2491.31` | 22,503.71 USD | `+1.51%` | `10X Cross` |
| `1476` | `0xdf83...3cff` | `SHORT` | 1,491,087.50 USD | `1,192.87` | `1255.46` | `1245.70` | `1764.11` | 6,516.89 USD | `+0.44%` | `10X Cross` |
| `1512` | `0x69cc...14fd` | `SHORT` | 1,451,583.86 USD | `1,161.36` | `675.33` | `1245.70` | `8080.62` | -667,278.34 USD | `-45.97%` | `10X Cross` |
| `1527` | `0x3fc5...c0c1` | `SHORT` | 1,435,367.86 USD | `1,148.44` | `1264.34` | `1245.70` | `3121.35` | 16,645.92 USD | `+1.16%` | `10X Cross` |
| `1555` | `0x2847...d47b` | `LONG` | 1,409,639.66 USD | `1,129.70` | `1233.74` | `1245.70` | `0.000000` | 15,882.39 USD | `+1.13%` | `5X Cross` |
| `1557` | `0xe35c...a1d3` | `LONG` | 1,408,825.00 USD | `1,127.06` | `1318.20` | `1245.70` | `694.37` | -76,870.35 USD | `-5.46%` | `2X Isolated` |
| `1563` | `0xfc27...9d9d` | `SHORT` | 1,394,738.05 USD | `1,112.32` | `1315.10` | `1245.70` | `16625.29` | 68,073.71 USD | `+4.88%` | `10X Cross` |
| `1564` | `0x5f94...4b96` | `LONG` | 1,394,087.50 USD | `1,115.27` | `538.00` | `1245.70` | `0.000000` | 794,069.86 USD | `+56.96%` | `10X Cross` |
| `1566` | `0x51f6...2b39` | `SHORT` | 1,392,530.13 USD | `1,115.72` | `1299.77` | `1245.70` | `2704.22` | 57,647.48 USD | `+4.14%` | `10X Cross` |
| `1582` | `0x266b...efcb` | `LONG` | 1,374,010.00 USD | `1,100.00` | `863.84` | `1245.70` | `321.62` | 423,785.24 USD | `+30.84%` | `10X Cross` |
| `1584` | `0x71df...a23d` | `SHORT` | 1,373,838.45 USD | `1,098.28` | `513.50` | `1245.70` | `2552.03` | -809,868.26 USD | `-58.95%` | `2X Cross` |
| `1594` | `0xbfc7...80b4` | `SHORT` | 1,357,832.50 USD | `1,075.00` | `558.03` | `1245.70` | `5332.06` | -757,953.77 USD | `-55.82%` | `10X Cross` |
| `1603` | `0xef96...9383` | `SHORT` | 1,346,500.20 USD | `1,078.84` | `1259.08` | `1245.70` | `5175.26` | 11,847.57 USD | `+0.88%` | `10X Cross` |
| `1678` | `0x123d...3bff` | `SHORT` | 1,260,943.48 USD | `1,009.32` | `490.16` | `1245.70` | `4490.59` | -766,217.61 USD | `-60.77%` | `10X Cross` |
| `1685` | `0x668c...ea2e` | `SHORT` | 1,254,400.00 USD | `1,000.00` | `1406.98` | `1245.70` | `4181.09` | 152,581.99 USD | `+12.16%` | `10X Cross` |
| `1688` | `0xb5ff...d912` | `LONG` | 1,253,900.00 USD | `1,000.00` | `1280.79` | `1245.70` | `452.80` | -26,887.44 USD | `-2.14%` | `2X Cross` |
| `1691` | `0xe282...df29` | `LONG` | 1,249,900.00 USD | `1,000.00` | `420.99` | `1245.70` | `199.39` | 828,913.14 USD | `+66.32%` | `10X Cross` |
| `1713` | `0x17f0...094f` | `LONG` | 1,230,276.57 USD | `984.30` | `1287.23` | `1245.70` | `536.80` | -36,743.59 USD | `-2.99%` | `5X Cross` |
| `1786` | `0x757d...94ba` | `LONG` | 1,155,787.50 USD | `925.00` | `1558.31` | `1245.70` | `0.000000` | -285,653.09 USD | `-24.72%` | `10X Cross` |
| `1826` | `0xb911...5525` | `LONG` | 1,124,857.26 USD | `900.00` | `1294.82` | `1245.70` | `1070.32` | -40,480.56 USD | `-3.60%` | `10X Cross` |
| `1866` | `0x7a76...b16d` | `LONG` | 1,095,950.00 USD | `876.76` | `1297.31` | `1245.70` | `1199.47` | -41,480.66 USD | `-3.78%` | `10X Cross` |
| `1868` | `0xcf0a...856f` | `LONG` | 1,095,471.12 USD | `871.15` | `1292.19` | `1245.70` | `992.86` | -30,223.72 USD | `-2.76%` | `4X Cross` |
| `1892` | `0xdf95...7d72` | `SHORT` | 1,070,345.60 USD | `857.58` | `1074.37` | `1245.70` | `46381.47` | -148,990.22 USD | `-13.92%` | `10X Cross` |
| `1902` | `0x38f9...cb04` | `SHORT` | 1,061,708.75 USD | `850.66` | `1266.75` | `1245.70` | `2315.11` | 15,867.81 USD | `+1.49%` | `10X Cross` |
| `1936` | `0x601c...4f54` | `SHORT` | 1,030,360.12 USD | `824.42` | `615.11` | `1245.70` | `3084.28` | -523,247.36 USD | `-50.78%` | `5X Cross` |
| `1958` | `0xae55...2236` | `LONG` | 1,020,883.76 USD | `817.47` | `1467.80` | `1245.70` | `0.000000` | -178,997.46 USD | `-17.53%` | `10X Cross` |
| `2003` | `0x0f02...5384` | `LONG` | 1,000,894.92 USD | `800.78` | `1290.36` | `1245.70` | `303.47` | -32,399.15 USD | `-3.24%` | `3X Cross` |

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
| `ANNOUNCEMENT` | `INFO` | `1284.20` | 179.79 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 0.18K USD at 1284.2000 USD [API] | `2026-10-11 16:30:00` |
| `ANNOUNCEMENT` | `INFO` | `1284.20` | 783.36 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 0.78K USD at 1284.2000 USD [API] | `2026-10-11 16:30:00` |
| `ANNOUNCEMENT` | `INFO` | `1284.10` | 975.92 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 0.98K USD at 1284.1000 USD [API] | `2026-10-11 16:30:00` |
| `ANNOUNCEMENT` | `INFO` | `1284.10` | 77.05 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 0.08K USD at 1284.1000 USD [API] | `2026-10-11 16:30:00` |
| `ANNOUNCEMENT` | `INFO` | `1284.10` | 1,284.10 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 1.28K USD at 1284.1000 USD [API] | `2026-10-11 16:30:00` |
| `ANNOUNCEMENT` | `INFO` | `1284.00` | 1,284.00 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 1.28K USD at 1284.0000 USD [API] | `2026-10-11 16:30:00` |
| `ANNOUNCEMENT` | `INFO` | `1284.00` | 975.84 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 0.98K USD at 1284.0000 USD [API] | `2026-10-11 16:30:00` |
| `ANNOUNCEMENT` | `INFO` | `1284.00` | 102.72 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 0.10K USD at 1284.0000 USD [API] | `2026-10-11 16:30:00` |
| `ANNOUNCEMENT` | `INFO` | `1284.00` | 12.84 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 0.01K USD at 1284.0000 USD [API] | `2026-10-11 16:30:00` |
| `ANNOUNCEMENT` | `INFO` | `1283.90` | 12.84 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 0.01K USD at 1283.9000 USD [API] | `2026-10-11 16:30:00` |
| `ANNOUNCEMENT` | `INFO` | `1283.80` | 12.84 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 0.01K USD at 1283.8000 USD [API] | `2026-10-11 16:30:00` |
| `ANNOUNCEMENT` | `INFO` | `1283.80` | 12.84 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 0.01K USD at 1283.8000 USD [API] | `2026-10-11 16:30:00` |
| `ANNOUNCEMENT` | `INFO` | `1283.80` | 12.84 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 0.01K USD at 1283.8000 USD [API] | `2026-10-11 16:30:00` |
| `ANNOUNCEMENT` | `INFO` | `1536.50` | 4,609.50 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 4.61K USD at 1536.5000 USD [API] | `2026-09-24 16:28:40` |
| `ANNOUNCEMENT` | `INFO` | `1522.40` | 4,567.20 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 4.57K USD at 1522.4000 USD [API] | `2026-09-22 05:43:11` |
| `ANNOUNCEMENT` | `INFO` | `1509.70` | 332.13 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 0.33K USD at 1509.7000 USD [API] | `2026-09-20 19:32:55` |
| `ANNOUNCEMENT` | `INFO` | `1509.70` | 1,992.80 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 1.99K USD at 1509.7000 USD [API] | `2026-09-20 19:32:55` |
| `ANNOUNCEMENT` | `INFO` | `1509.70` | 105.68 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 0.11K USD at 1509.7000 USD [API] | `2026-09-20 19:32:55` |
| `ANNOUNCEMENT` | `INFO` | `1509.70` | 105.68 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 0.11K USD at 1509.7000 USD [API] | `2026-09-20 19:32:55` |
| `ANNOUNCEMENT` | `INFO` | `1509.70` | 1,992.80 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 1.99K USD at 1509.7000 USD [API] | `2026-09-20 19:32:55` |
| `ANNOUNCEMENT` | `INFO` | `1509.70` | 3,019.40 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 3.02K USD at 1509.7000 USD [API] | `2026-09-20 19:32:55` |
| `ANNOUNCEMENT` | `INFO` | `1536.40` | 3,917.82 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 3.92K USD at 1536.4000 USD [API] | `2026-09-18 22:58:29` |
| `ANNOUNCEMENT` | `INFO` | `1536.40` | 1,628.58 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 1.63K USD at 1536.4000 USD [API] | `2026-09-18 22:58:29` |
| `ANNOUNCEMENT` | `INFO` | `1536.40` | 1,966.59 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 1.97K USD at 1536.4000 USD [API] | `2026-09-18 22:58:29` |
| `ANNOUNCEMENT` | `INFO` | `1536.40` | 169.00 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 0.17K USD at 1536.4000 USD [API] | `2026-09-18 22:58:29` |
| `ANNOUNCEMENT` | `INFO` | `1172.70` | 3,518.10 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 3.52K USD at 1172.7000 USD [API] | `2026-09-14 18:22:41` |
| `ANNOUNCEMENT` | `INFO` | `1124.90` | 3,374.70 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 3.37K USD at 1124.9000 USD [API] | `2026-09-14 04:10:24` |
| `ANNOUNCEMENT` | `INFO` | `1151.40` | 3,454.20 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 3.45K USD at 1151.4000 USD [API] | `2026-09-11 12:29:35` |
| `ANNOUNCEMENT` | `INFO` | `1176.90` | 3,530.70 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 3.53K USD at 1176.9000 USD [API] | `2026-09-08 14:39:00` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`1403.54` (Vol: 3,000,000.00 USD, Dist: `+11.94%`) | Long MP=`0.000000` (Vol: 0.00 USD, Dist: `-0.00%`)
  * 48H Horizon: Short MP=`1403.54` (Vol: 3,000,000.00 USD, Dist: `+11.94%`) | Long MP=`0.000000` (Vol: 0.00 USD, Dist: `-0.00%`)
  * 3D Horizon: Short MP=`1403.54` (Vol: 3,000,000.00 USD, Dist: `+11.94%`) | Long MP=`0.000000` (Vol: 0.00 USD, Dist: `-0.00%`)
  * 7D Horizon: Short MP=`1404.10` (Vol: 3,000,000.00 USD, Dist: `+11.98%`) | Long MP=`1200.46` (Vol: 3,000,000.00 USD, Dist: `--4.26%`)
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
| `5m` | `BALANCED` | 0.00 USD | 1,750.00 USD | 1,750.00 USD | 1,750.00 USD | `1` | `2026-10-29 22:15:00 UTC - 2026-10-29 22:20:00 UTC` |
| `15m` | `BALANCED` | 0.00 USD | 1,750.00 USD | 1,750.00 USD | 1,750.00 USD | `1` | `2026-10-29 22:15:00 UTC - 2026-10-29 22:30:00 UTC` |
| `1h` | `BALANCED` | 0.00 USD | 1,750.00 USD | 1,750.00 USD | 1,750.00 USD | `1` | `2026-10-29 22:00:00 UTC - 2026-10-29 23:00:00 UTC` |
| `4h` | `BALANCED` | 0.00 USD | 1,750.00 USD | 1,750.00 USD | 1,750.00 USD | `1` | `2026-10-29 20:00:00 UTC - 2026-10-30 00:00:00 UTC` |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `0 USD` | Total OI Tokens: `-`
  * 1h OI Change: `0.00%` | 4h OI Change: `0.00%` | 24h OI Change: `0.00%`
  * Exchange Breakdown: Binance=`-` | Bybit=`-` | OKX=`-` | Hyperliquid=`-`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `6.72K` | Last 24h: `33.19K` | Last 3d: `283.86K` | Last 7d: `777.60K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `-0.0017%` | **USDT OKX** | `0.0008%` |
| **USDT Bybit** | `0.0100%` | **USDT KuCoin** | `-0.0054%` |
| **USDT MEXC** | `-0.0017%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `-0.0020%` | **USDT Bitget** | `0.0100%` |
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
| `0:00 UTC` | `1294.05` | `1302.04` | `1294.05` | `1328.55` | `1286.25` | 68,949,402.59 USD | 35,232,633.05 USD | 33,716,769.55 USD | 1,515,863.50 USD | `+2.20%` | `6B / 24S` |
| `5:00 UTC` | `1306.05` | `1306.88` | `1306.05` | `1312.05` | `1300.05` | 17,712,248.68 USD | 9,074,345.66 USD | 8,637,903.02 USD | 436,442.64 USD | `+2.46%` | `3B / 5S` |
| `0:00 UTC` | `1249.20` | `1269.32` | `1249.20` | `1308.60` | `1241.40` | 130,590,816.99 USD | 58,796,845.15 USD | 71,793,971.84 USD | -12,997,126.69 USD | `-9.95%` | `4B / 19S` |
| `5:00 UTC` | `1229.25` | `1237.79` | `1229.25` | `1264.35` | `1206.75` | 149,162,484.89 USD | 77,012,548.38 USD | 72,149,936.51 USD | 4,862,611.87 USD | `+3.26%` | `9B / 11S` |
| `0:00 UTC` | `1249.95` | `1248.07` | `1249.95` | `1259.85` | `1233.15` | 61,152,789.32 USD | 32,267,997.87 USD | 28,884,791.45 USD | 3,383,206.41 USD | `+5.53%` | `6B / 4S` |
| `5:00 UTC` | `1273.95` | `1271.85` | `1273.95` | `1286.25` | `1253.25` | 67,607,862.35 USD | 37,234,359.13 USD | 30,373,503.22 USD | 6,860,855.91 USD | `+10.15%` | `6B / 2S` |
| `0:00 UTC` | `1294.65` | `1287.25` | `1294.65` | `1297.05` | `1269.15` | 47,983,765.84 USD | 24,978,907.15 USD | 23,004,858.69 USD | 1,974,048.46 USD | `+4.11%` | `4B / 9S` |
| `5:00 UTC` | `1264.05` | `1267.99` | `1264.05` | `1276.65` | `1260.75` | 31,349,361.20 USD | 15,100,777.24 USD | 16,248,583.96 USD | -1,147,806.72 USD | `-3.66%` | `0B / 1S` |
| `0:00 UTC` | `1261.05` | `1255.07` | `1261.05` | `1269.15` | `1241.25` | 60,510,539.13 USD | 31,467,084.85 USD | 29,043,454.28 USD | 2,423,630.57 USD | `+4.01%` | `3B / 5S` |
| `5:00 UTC` | `1247.55` | `1250.72` | `1247.55` | `1257.45` | `1242.15` | 11,977,950.07 USD | 6,539,390.12 USD | 5,438,559.95 USD | 1,100,830.17 USD | `+9.19%` | `3B / 3S` |

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
| `5m` | 541,010.00 USD | 5,920,000.00 USD | **`ACCUMULATION`** |
| `15m` | -437,470.00 USD | 1,140,000.00 USD | **`ACCUMULATION`** |
| `30m` | 469,190.00 USD | -871,000.00 USD | **`DISTRIBUTION`** |
| `1h` | 5,860,000.00 USD | 9,260,000.00 USD | **`ACCUMULATION`** |
| `2h` | -8,730,000.00 USD | -764,740.00 USD | **`DISTRIBUTION`** |
| `4h` | -11,830,000.00 USD | -10,090,000.00 USD | **`DISTRIBUTION`** |
| `6h` | -8,050,000.00 USD | -28,370,000.00 USD | **`DISTRIBUTION`** |
| `8h` | 15,100,000.00 USD | 85,320,000.00 USD | **`ACCUMULATION`** |
| `12h` | 22,270,000.00 USD | 96,430,000.00 USD | **`ACCUMULATION`** |
| `24h` | 2,030,000.00 USD | 59,190,000.00 USD | **`ACCUMULATION`** |
| `1w` | 35,400,000.00 USD | 248,400,000.00 USD | **`ACCUMULATION`** |
| `30d` | 57,540,000.00 USD | -539,810,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+541.01K` | 15m=`-437.47K` | 1h=`+5.86M` | 24h=`+2.03M`
* Futures Capital Netflows: 5m=`+5.92M` | 15m=`+1.14M` | 1h=`+9.26M` | 24h=`+59.19M`
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
  * `2026-10-30 03:30:02 IST`: [investinglive.com] - (Sentiment: `Neutral`)
  * `2026-10-30 02:54:02 IST`: [msn.com] - (Sentiment: `Neutral`)
  * `2026-10-30 03:51:02 IST`: [morningstar.com] - (Sentiment: `Neutral`)
  * `2026-10-30 03:50:02 IST`: [sec.gov] - (Sentiment: `Neutral`)
  * `2026-10-30 03:50:02 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 00:52:02 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 00:52:02 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:52:02 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:52:02 IST`: [@DeItaone] - (Sentiment: `Neutral`)
  * `2026-10-29 23:52:02 IST`: [@mb_ghalibaf] - (Sentiment: `Neutral`)
  * `2026-10-29 23:52:02 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-29 23:52:02 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-29 22:52:02 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:52:02 IST`: [fxstreet.com] - (Sentiment: `Neutral`)
  * `2026-10-29 21:52:02 IST`: [ForexFactory] - (Sentiment: `Neutral`)


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
  * Execution Entry: `1249.72` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `1220.41` (Risk Distance: `29.31` pts)
  * +2.5R Take Profit: `1322.98`
  * Mathematical Lot Sizing: **`0.34 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `1277.75` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `1307.06` (Risk Distance: `29.31` pts)
  * +2.5R Take Profit: `1204.49`
  * Mathematical Lot Sizing: **`0.34 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`1261.87`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
