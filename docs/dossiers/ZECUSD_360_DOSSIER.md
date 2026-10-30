# 🏛️ SOVEREIGN CANDIDATE DOSSIER: ZECUSD
**Canonical Key**: `ZECUSD` | **Broker Instrument**: `ZECUSD.p` | **Asset Class**: `Crypto Altcoin`
**Timestamp**: `2026-10-30 11:11:09 IST` (`2026-10-30 05:41:09 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `1272.21` | **Live Ask Quote**: `1273.83` | **Mid Price**: `1273.02`
- **Spread Points**: `162.00` | **Spread BPS**: `12.73 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `1250.41` | VWAP Z-Score: `+0.84` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `16.24` (Volatility Regime: `HIGH_EXPANSION`)
  * 14-Period RSI: `53.05` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `1326.33` | Lower -3.00σ Band: `1174.48`
  * Upper +2.51σ Band: `1313.93` | Lower -2.51σ Band: `1186.88`
  * Upper +2.01σ Band: `1301.28` | Lower -2.01σ Band: `1199.54`
  * Upper +2.00σ Band: `1301.02` | Lower -2.00σ Band: `1199.79`
  * Upper +1.28σ Band: `1282.80` | Lower -1.28σ Band: `1218.01`
  * Upper +1.00σ Band: `1275.71` | Lower -1.00σ Band: `1225.10`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`1273.54` | EMA-20=`1266.36` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`1268.19` (Slope: `+0.0000`) | EMA-100=`1272.83`
  * Institutional Anchors: EMA-144=`1274.22` | EMA-200=`1275.86` (Slope: `-0.0168`) | EMA-233=`1278.10`
- **Range Boundaries**: 24H High=`1396.49` | 24H Low=`1180.03` | Weekly High=`1396.49` | Weekly Low=`1180.03`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `1285.56` (Distance: `-0.99%`)
  * Point of Control (POC) = `1275.51` (Distance: `-0.21%`)
  * Value Area Low (VAL) = `1233.76` (Distance: `+3.17%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`1309.91` | POC=`1246.71` | VAL=`1230.27`
  * Prior Day Extremes: PDH=`1396.49` | PDL=`1206.89` | PDC=`1244.38`
  * Monday Range Blueprint: High=`1267.53` | Mid=`1222.14` | Low=`1176.75`
  * Developing Weekly Value Area: Weekly VAH=`1296.14` | Weekly POC=`1239.01` | Weekly VAL=`1200.92`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`1296.00` | Low=`1180.03`
  * London Session (08:00-16:00 UTC): High=`1283.82` | Low=`1268.20`
  * New York Session (13:00-21:00 UTC): High=`1280.66` | Low=`1265.38`
  * Initial Balance (First Hour): IB High=`1283.82` | IB Low=`1268.20`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `1267.93` - `1278.11`
  * Optimal Trade Entry (OTE 0.705): `1275.57`
  * Structural Invalidation Anchor (0.786): `1283.20`

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
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 11:04:06 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `13` | `0xb83d...6e36` | `SHORT` | 66,676,226.22 USD | `52,385.47` | `1336.45` | `1273.70` | `3649.29` | 3,334,341.18 USD | `+5.00%` | `3X Cross` |
| `22` | `0x5b5d...c060` | `SHORT` | 51,072,370.25 USD | `40,121.38` | `1478.36` | `1273.70` | `5053.01` | 8,241,664.87 USD | `+16.14%` | `3X Cross` |
| `38` | `0x7fda...17d1` | `SHORT` | 33,251,793.07 USD | `26,098.26` | `1262.62` | `1273.70` | `2600.20` | -299,726.05 USD | `-0.90%` | `5X Cross` |
| `81` | `0x60b0...991e` | `LONG` | 21,360,609.02 USD | `16,779.74` | `1179.65` | `1273.70` | `915.01` | 1,566,362.01 USD | `+7.33%` | `10X Cross` |
| `139` | `0xc36a...105b` | `LONG` | 14,638,309.79 USD | `11,510.82` | `1215.14` | `1273.70` | `956.97` | 651,028.77 USD | `+4.45%` | `10X Cross` |
| `156` | `0x9071...5c0b` | `LONG` | 13,389,561.90 USD | `10,517.29` | `1353.83` | `1273.70` | `0.1605` | -849,056.97 USD | `-6.34%` | `1X Cross` |
| `179` | `0x8742...8427` | `LONG` | 11,714,060.45 USD | `9,201.21` | `1286.37` | `1273.70` | `695.60` | -122,109.54 USD | `-1.04%` | `10X Cross` |
| `194` | `0x58b2...11f3` | `LONG` | 10,900,800.84 USD | `8,563.08` | `1246.56` | `1273.70` | `382.37` | 226,383.27 USD | `+2.08%` | `10X Cross` |
| `197` | `0xad59...ba81` | `SHORT` | 10,723,340.00 USD | `8,425.00` | `330.91` | `1273.70` | `2144.13` | -7,935,382.23 USD | `-74.00%` | `10X Cross` |
| `199` | `0x9ffd...ce40` | `LONG` | 10,693,985.36 USD | `8,400.97` | `1251.80` | `1273.70` | `595.52` | 177,667.21 USD | `+1.66%` | `5X Cross` |
| `205` | `0xdd53...2b13` | `SHORT` | 10,430,127.79 USD | `8,195.92` | `741.54` | `1273.70` | `8392.41` | -4,352,531.43 USD | `-41.73%` | `3X Cross` |
| `225` | `0x880a...311c` | `SHORT` | 9,809,609.61 USD | `7,707.11` | `1367.50` | `1273.70` | `2277.03` | 729,874.59 USD | `+7.44%` | `10X Cross` |
| `235` | `0xbf73...5d58` | `LONG` | 9,547,098.75 USD | `7,500.00` | `1248.78` | `1273.70` | `107.46` | 181,253.13 USD | `+1.90%` | `10X Cross` |
| `271` | `0x2b61...2f6c` | `LONG` | 8,669,395.20 USD | `6,807.00` | `1453.56` | `1273.70` | `583.13` | -1,224,956.02 USD | `-14.13%` | `10X Cross` |
| `285` | `0x2ae5...83e7` | `LONG` | 8,194,690.08 USD | `6,436.80` | `1391.82` | `1273.70` | `0.000000` | -764,201.91 USD | `-9.33%` | `1X Cross` |
| `330` | `0x26b6...9a13` | `LONG` | 6,917,681.66 USD | `5,433.73` | `1282.23` | `1273.70` | `229.28` | -49,621.57 USD | `-0.72%` | `10X Cross` |
| `340` | `0xecb6...2b00` | `SHORT` | 6,707,600.64 USD | `5,269.35` | `1279.14` | `1273.70` | `6737.17` | 32,611.09 USD | `+0.49%` | `5X Cross` |
| `346` | `0x45d2...4029` | `SHORT` | 6,654,493.70 USD | `5,227.00` | `833.44` | `1273.70` | `8749.51` | -2,298,115.73 USD | `-34.53%` | `5X Cross` |
| `362` | `0xea00...a918` | `LONG` | 6,365,000.00 USD | `5,000.00` | `739.16` | `1273.70` | `0.000000` | 2,669,184.89 USD | `+41.94%` | `5X Cross` |
| `374` | `0xdd7a...8830` | `LONG` | 6,185,563.81 USD | `4,860.19` | `897.48` | `1273.70` | `779.93` | 1,823,660.14 USD | `+29.48%` | `10X Cross` |
| `419` | `0x469e...58a5` | `SHORT` | 5,302,659.07 USD | `4,163.52` | `1242.31` | `1273.70` | `1979.82` | -130,274.42 USD | `-2.46%` | `10X Cross` |
| `433` | `0x4cae...7c34` | `LONG` | 5,100,893.12 USD | `4,002.27` | `1169.72` | `1273.70` | `952.14` | 419,343.77 USD | `+8.22%` | `10X Cross` |
| `444` | `0xa61c...66b9` | `LONG` | 4,947,868.80 USD | `3,888.00` | `1148.34` | `1273.70` | `0.000000` | 483,126.66 USD | `+9.76%` | `10X Cross` |
| `471` | `0x9aa5...58af` | `SHORT` | 4,737,070.72 USD | `3,720.31` | `1205.51` | `1273.70` | `3658.75` | -252,183.92 USD | `-5.32%` | `10X Cross` |
| `476` | `0x0153...8052` | `SHORT` | 4,710,002.05 USD | `3,698.18` | `1307.82` | `1273.70` | `2504.86` | 126,568.70 USD | `+2.69%` | `1X Isolated` |
| `478` | `0xd4c1...3d1d` | `SHORT` | 4,687,520.29 USD | `3,683.42` | `1293.10` | `1273.70` | `2361.90` | 75,523.73 USD | `+1.61%` | `10X Cross` |
| `541` | `0x382b...3e39` | `LONG` | 4,161,997.12 USD | `3,269.44` | `1215.08` | `1273.70` | `0.000000` | 189,367.12 USD | `+4.55%` | `10X Cross` |
| `544` | `0xd21d...90f1` | `LONG` | 4,136,600.00 USD | `3,250.00` | `1253.64` | `1273.70` | `876.08` | 62,258.27 USD | `+1.51%` | `4X Isolated` |
| `550` | `0xb122...e4ba` | `LONG` | 4,100,791.28 USD | `3,221.36` | `1264.20` | `1273.70` | `1063.87` | 28,334.00 USD | `+0.69%` | `10X Cross` |
| `559` | `0x456f...cdf1` | `LONG` | 4,047,172.82 USD | `3,179.49` | `1267.80` | `1273.70` | `504.08` | 16,217.90 USD | `+0.40%` | `10X Cross` |
| `566` | `0x1338...c48e` | `LONG` | 4,013,948.54 USD | `3,149.43` | `1018.52` | `1273.70` | `820.37` | 806,202.99 USD | `+20.09%` | `4X Isolated` |
| `572` | `0x325e...9564` | `LONG` | 3,947,490.67 USD | `3,101.91` | `1298.07` | `1273.70` | `137.65` | -79,020.03 USD | `-2.00%` | `10X Cross` |
| `583` | `0xdbe0...d6d5` | `LONG` | 3,927,984.55 USD | `3,085.37` | `422.97` | `1273.70` | `338.69` | 2,622,980.05 USD | `+66.78%` | `3X Isolated` |
| `600` | `0x9c06...0560` | `SHORT` | 3,805,855.45 USD | `2,989.80` | `786.00` | `1273.70` | `2550.77` | -1,455,860.44 USD | `-38.25%` | `10X Cross` |
| `602` | `0x2e30...4cb5` | `SHORT` | 3,797,071.67 USD | `2,982.54` | `1287.21` | `1273.70` | `2878.82` | 42,072.88 USD | `+1.11%` | `2X Cross` |
| `605` | `0x27c9...d65d` | `SHORT` | 3,770,177.05 USD | `2,961.88` | `1254.41` | `1273.70` | `1732.99` | -54,761.85 USD | `-1.45%` | `10X Cross` |
| `641` | `0x5323...b23c` | `SHORT` | 3,532,737.92 USD | `2,774.91` | `1267.04` | `1273.70` | `3221.04` | -16,807.82 USD | `-0.48%` | `5X Cross` |
| `685` | `0x71d0...8c26` | `SHORT` | 3,295,746.08 USD | `2,588.96` | `1266.50` | `1273.70` | `3596.19` | -16,823.84 USD | `-0.51%` | `10X Cross` |
| `702` | `0xa183...0482` | `LONG` | 3,225,782.00 USD | `2,534.00` | `530.25` | `1273.70` | `444.61` | 1,882,119.28 USD | `+58.35%` | `5X Isolated` |
| `703` | `0xac48...3201` | `LONG` | 3,222,346.35 USD | `2,531.50` | `1378.58` | `1273.70` | `561.06` | -267,525.93 USD | `-8.30%` | `10X Cross` |
| `713` | `0x0871...e927` | `LONG` | 3,179,250.00 USD | `2,500.00` | `1276.50` | `1273.70` | `0.000000` | -12,000.00 USD | `-0.38%` | `10X Cross` |
| `732` | `0x9b86...6e6e` | `LONG` | 3,135,288.24 USD | `2,463.30` | `637.58` | `1273.70` | `882.54` | 1,564,738.96 USD | `+49.91%` | `3X Cross` |
| `782` | `0xb2f7...af9f` | `SHORT` | 2,944,902.82 USD | `2,313.72` | `746.63` | `1273.70` | `4411.37` | -1,217,414.07 USD | `-41.34%` | `10X Cross` |
| `801` | `0x413c...886c` | `LONG` | 2,864,025.00 USD | `2,250.00` | `1237.51` | `1273.70` | `0.000000` | 79,623.97 USD | `+2.78%` | `10X Cross` |
| `808` | `0xf48f...10fe` | `LONG` | 2,823,694.07 USD | `2,218.49` | `1517.87` | `1273.70` | `956.95` | -543,692.75 USD | `-19.25%` | `3X Cross` |
| `841` | `0x5bc4...3b0c` | `SHORT` | 2,712,432.02 USD | `2,130.74` | `1089.65` | `1273.70` | `3672.51` | -390,674.44 USD | `-14.40%` | `5X Cross` |
| `855` | `0x8de4...b9aa` | `SHORT` | 2,662,100.29 USD | `2,091.29` | `1331.35` | `1273.70` | `1689.99` | 122,139.42 USD | `+4.59%` | `3X Cross` |
| `861` | `0x4fe2...ac59` | `SHORT` | 2,637,108.61 USD | `2,071.57` | `1478.56` | `1273.70` | `1822.35` | 425,837.60 USD | `+16.15%` | `10X Cross` |
| `867` | `0xdf57...93f5` | `LONG` | 2,615,187.55 USD | `2,054.35` | `1227.36` | `1273.70` | `897.32` | 93,765.51 USD | `+3.59%` | `4X Isolated` |
| `872` | `0xbcd4...0dd2` | `LONG` | 2,588,773.38 USD | `2,033.92` | `1228.20` | `1273.70` | `794.15` | 90,722.56 USD | `+3.50%` | `10X Cross` |
| `888` | `0x9a99...d21a` | `LONG` | 2,546,000.00 USD | `2,000.00` | `1278.44` | `1273.70` | `0.000000` | -10,873.67 USD | `-0.43%` | `10X Cross` |
| `889` | `0xf29c...9971` | `LONG` | 2,546,000.00 USD | `2,000.00` | `1254.95` | `1273.70` | `0.000000` | 36,102.93 USD | `+1.42%` | `10X Cross` |
| `908` | `0x77ee...2902` | `SHORT` | 2,483,328.88 USD | `1,946.03` | `759.84` | `1273.70` | `5484.28` | -1,004,651.38 USD | `-40.46%` | `10X Cross` |
| `923` | `0x3e2f...b269` | `SHORT` | 2,451,174.23 USD | `1,925.51` | `1134.87` | `1273.70` | `2977.26` | -265,975.37 USD | `-10.85%` | `10X Cross` |
| `934` | `0x4f12...618b` | `SHORT` | 2,413,964.44 USD | `1,896.28` | `1608.30` | `1273.70` | `2116.88` | 635,819.95 USD | `+26.34%` | `3X Cross` |
| `977` | `0x866d...d6e1` | `LONG` | 2,296,712.73 USD | `1,802.05` | `674.73` | `1273.70` | `170.84` | 1,080,811.41 USD | `+47.06%` | `10X Cross` |
| `1001` | `0x2309...a2d9` | `LONG` | 2,229,271.23 USD | `1,750.37` | `1186.09` | `1273.70` | `810.57` | 153,177.12 USD | `+6.87%` | `8X Cross` |
| `1031` | `0x3205...40bb` | `SHORT` | 2,120,910.34 USD | `1,665.68` | `1256.10` | `1273.70` | `2098.40` | -28,649.82 USD | `-1.35%` | `10X Cross` |
| `1037` | `0x265e...7f70` | `LONG` | 2,102,576.65 USD | `1,651.74` | `1382.98` | `1273.70` | `0.000000` | -181,746.11 USD | `-8.64%` | `3X Cross` |
| `1043` | `0xfe7c...b7ae` | `SHORT` | 2,091,080.72 USD | `1,642.64` | `1346.92` | `1273.70` | `5556.45` | 121,427.90 USD | `+5.81%` | `10X Cross` |
| `1051` | `0x3e47...aaf6` | `LONG` | 2,082,657.18 USD | `1,636.28` | `1278.38` | `1273.70` | `1044.95` | -9,134.60 USD | `-0.44%` | `10X Cross` |
| `1055` | `0x2edd...8179` | `SHORT` | 2,079,288.41 USD | `1,633.89` | `1261.58` | `1273.70` | `2897.57` | -18,006.49 USD | `-0.87%` | `10X Cross` |
| `1069` | `0x7f75...9edf` | `LONG` | 2,051,569.69 USD | `1,611.67` | `1200.24` | `1273.70` | `982.40` | 117,185.71 USD | `+5.71%` | `10X Cross` |
| `1077` | `0x6646...6de5` | `SHORT` | 2,037,280.00 USD | `1,600.00` | `660.64` | `1273.70` | `4327.78` | -980,255.03 USD | `-48.12%` | `10X Cross` |
| `1080` | `0x023a...2355` | `SHORT` | 2,029,829.23 USD | `1,594.90` | `1310.00` | `1273.70` | `4409.23` | 59,482.91 USD | `+2.93%` | `10X Cross` |
| `1107` | `0xab59...59b5` | `LONG` | 1,992,495.83 USD | `1,565.32` | `1342.15` | `1273.70` | `825.33` | -108,399.39 USD | `-5.44%` | `10X Cross` |
| `1138` | `0xfc27...9d9d` | `SHORT` | 1,960,542.11 USD | `1,540.58` | `1296.49` | `1273.70` | `12442.45` | 36,811.32 USD | `+1.88%` | `10X Cross` |
| `1165` | `0xcf67...eb24` | `LONG` | 1,909,500.00 USD | `1,500.00` | `887.05` | `1273.70` | `610.42` | 578,928.63 USD | `+30.32%` | `10X Cross` |
| `1175` | `0xb695...a92d` | `LONG` | 1,887,414.10 USD | `1,483.00` | `1249.80` | `1273.70` | `0.000000` | 33,955.25 USD | `+1.80%` | `10X Cross` |
| `1181` | `0x7277...0b98` | `SHORT` | 1,878,014.00 USD | `1,475.73` | `1287.86` | `1273.70` | `2151.85` | 22,518.12 USD | `+1.20%` | `10X Cross` |
| `1238` | `0x2ab7...c2f8` | `LONG` | 1,782,989.28 USD | `1,400.51` | `813.26` | `1273.70` | `789.26` | 644,007.60 USD | `+36.12%` | `3X Cross` |
| `1254` | `0xe35c...a1d3` | `LONG` | 1,767,845.02 USD | `1,389.16` | `1311.66` | `1273.70` | `690.78` | -54,257.70 USD | `-3.07%` | `2X Isolated` |
| `1261` | `0x11be...8b1d` | `LONG` | 1,751,294.01 USD | `1,375.83` | `1206.55` | `1273.70` | `1134.59` | 91,286.05 USD | `+5.21%` | `10X Isolated` |
| `1282` | `0x039c...0ebd` | `SHORT` | 1,701,275.39 USD | `1,336.64` | `1241.40` | `1273.70` | `3498.02` | -41,964.07 USD | `-2.47%` | `10X Cross` |
| `1345` | `0xe065...0f85` | `SHORT` | 1,607,302.53 USD | `1,262.61` | `1087.02` | `1273.70` | `1571.91` | -234,826.40 USD | `-14.61%` | `10X Cross` |
| `1430` | `0x266b...efcb` | `LONG` | 1,527,960.00 USD | `1,200.00` | `893.76` | `1273.70` | `376.80` | 455,450.30 USD | `+29.81%` | `10X Cross` |
| `1431` | `0x5975...9abd` | `LONG` | 1,527,480.00 USD | `1,200.00` | `1179.54` | `1273.70` | `448.47` | 112,037.21 USD | `+7.33%` | `5X Cross` |
| `1447` | `0x2847...d47b` | `LONG` | 1,510,833.47 USD | `1,186.27` | `1232.07` | `1273.70` | `0.000000` | 49,264.97 USD | `+3.26%` | `5X Cross` |
| `1469` | `0x69cc...14fd` | `SHORT` | 1,477,946.74 USD | `1,161.36` | `675.33` | `1273.70` | `7916.34` | -693,641.21 USD | `-46.93%` | `10X Cross` |
| `1487` | `0x3fc5...c0c1` | `SHORT` | 1,461,849.28 USD | `1,148.44` | `1264.34` | `1273.70` | `2656.12` | -9,835.50 USD | `-0.67%` | `10X Cross` |
| `1501` | `0x38f9...cb04` | `SHORT` | 1,447,052.58 USD | `1,136.28` | `1252.73` | `1273.70` | `1992.89` | -23,605.41 USD | `-1.63%` | `10X Cross` |
| `1522` | `0x5f94...4b96` | `LONG` | 1,419,515.66 USD | `1,115.27` | `538.00` | `1273.70` | `0.000000` | 819,498.02 USD | `+57.73%` | `10X Cross` |
| `1543` | `0x71df...a23d` | `SHORT` | 1,398,659.58 USD | `1,098.28` | `513.50` | `1273.70` | `2558.93` | -834,689.39 USD | `-59.68%` | `2X Cross` |
| `1571` | `0xbfc7...80b4` | `SHORT` | 1,368,045.00 USD | `1,075.00` | `558.03` | `1273.70` | `2609.54` | -768,166.27 USD | `-56.15%` | `10X Cross` |
| `1645` | `0x123d...3bff` | `SHORT` | 1,287,474.71 USD | `1,011.45` | `494.46` | `1273.70` | `4309.13` | -787,354.60 USD | `-61.15%` | `10X Cross` |
| `1658` | `0x668c...ea2e` | `SHORT` | 1,273,600.00 USD | `1,000.00` | `1406.98` | `1273.70` | `4197.16` | 133,381.99 USD | `+10.47%` | `10X Cross` |
| `1661` | `0xe282...df29` | `LONG` | 1,272,700.00 USD | `1,000.00` | `420.99` | `1273.70` | `790.96` | 851,713.14 USD | `+66.92%` | `10X Cross` |
| `1676` | `0x17f0...094f` | `LONG` | 1,254,490.35 USD | `984.30` | `1287.23` | `1273.70` | `536.94` | -12,529.81 USD | `-1.00%` | `5X Cross` |
| `1701` | `0x51f6...2b39` | `SHORT` | 1,238,484.41 USD | `972.81` | `1299.77` | `1273.70` | `2531.16` | 25,943.29 USD | `+2.09%` | `10X Cross` |
| `1720` | `0xdf83...3cff` | `SHORT` | 1,215,905.84 USD | `955.30` | `1259.52` | `1273.70` | `1923.21` | -12,682.25 USD | `-1.04%` | `10X Cross` |
| `1762` | `0x757d...94ba` | `LONG` | 1,177,525.00 USD | `925.00` | `1558.31` | `1273.70` | `0.000000` | -263,915.59 USD | `-22.41%` | `10X Cross` |
| `1767` | `0xaa82...9556` | `LONG` | 1,176,047.84 USD | `924.13` | `1254.72` | `1273.70` | `180.03` | 16,521.16 USD | `+1.40%` | `10X Cross` |
| `1810` | `0xb911...5525` | `LONG` | 1,145,610.00 USD | `900.00` | `1294.82` | `1273.70` | `1035.37` | -19,727.82 USD | `-1.72%` | `10X Cross` |
| `1856` | `0xcf0a...856f` | `LONG` | 1,108,927.34 USD | `871.15` | `1292.19` | `1273.70` | `1007.72` | -16,767.50 USD | `-1.51%` | `4X Cross` |
| `1860` | `0x9e7e...0047` | `LONG` | 1,107,450.55 USD | `870.09` | `1284.68` | `1273.70` | `1171.80` | -10,334.86 USD | `-0.93%` | `10X Cross` |
| `1861` | `0x2577...4897` | `SHORT` | 1,107,195.99 USD | `869.89` | `1271.99` | `1273.70` | `4965.20` | -704.60 USD | `-0.06%` | `10X Cross` |
| `1863` | `0xef96...9383` | `SHORT` | 1,105,498.66 USD | `868.42` | `1259.08` | `1273.70` | `5298.65` | -12,086.87 USD | `-1.09%` | `10X Cross` |
| `1883` | `0xdf95...7d72` | `SHORT` | 1,086,383.36 USD | `853.27` | `1074.39` | `1273.70` | `43994.93` | -169,635.92 USD | `-15.61%` | `10X Cross` |
| `1925` | `0x601c...4f54` | `SHORT` | 1,049,898.87 USD | `824.42` | `615.11` | `1273.70` | `3060.63` | -542,786.12 USD | `-51.70%` | `5X Cross` |
| `1943` | `0xae55...2236` | `LONG` | 1,040,721.06 USD | `817.47` | `1467.80` | `1273.70` | `0.000000` | -159,160.16 USD | `-15.29%` | `10X Cross` |
| `1981` | `0x0f02...5384` | `LONG` | 1,019,072.63 USD | `800.78` | `1290.36` | `1273.70` | `294.97` | -14,221.44 USD | `-1.40%` | `3X Cross` |
| `1983` | `0x9b0f...db40` | `LONG` | 1,018,480.00 USD | `800.00` | `1268.86` | `1273.70` | `791.45` | 3,390.24 USD | `+0.33%` | `10X Cross` |
| `1984` | `0x11ee...1d1d` | `SHORT` | 1,018,357.20 USD | `800.00` | `1269.65` | `1273.70` | `1589.61` | -2,634.19 USD | `-0.26%` | `5X Cross` |
| `2000` | `0xabdb...84ac` | `LONG` | 1,011,478.54 USD | `793.69` | `711.79` | `1273.70` | `664.51` | 446,538.17 USD | `+44.15%` | `3X Cross` |
| `2003` | `0x6e8f...4364` | `LONG` | 1,010,078.35 USD | `793.65` | `1260.00` | `1273.70` | `933.22` | 10,079.35 USD | `+1.00%` | `10X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `1290.00` | 309.60 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Long: 0.31K USD at 1290.0000 USD [API] | `2026-10-27 15:21:38` |
| `ANNOUNCEMENT` | `INFO` | `1290.00` | 516.00 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Long: 0.52K USD at 1290.0000 USD [API] | `2026-10-27 15:21:38` |
| `ANNOUNCEMENT` | `INFO` | `1238.70` | 1,350.18 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 1.35K USD at 1238.7000 USD [API] | `2026-10-29 02:30:54` |
| `ANNOUNCEMENT` | `INFO` | `1234.10` | 1,814.13 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 1.81K USD at 1234.1000 USD [API] | `2026-10-29 02:35:53` |
| `ANNOUNCEMENT` | `INFO` | `1234.10` | 222.14 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 0.22K USD at 1234.1000 USD [API] | `2026-10-29 02:35:53` |
| `ANNOUNCEMENT` | `INFO` | `1234.10` | 12.34 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 0.01K USD at 1234.1000 USD [API] | `2026-10-29 02:35:53` |
| `ANNOUNCEMENT` | `INFO` | `1234.10` | 12.34 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 0.01K USD at 1234.1000 USD [API] | `2026-10-29 02:35:53` |
| `ANNOUNCEMENT` | `INFO` | `1234.80` | 3,346.31 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 3.35K USD at 1234.8000 USD [API] | `2026-10-29 02:35:52` |
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
| `5m` | `BALANCED` | 0.00 USD | 1,750.00 USD | 1,750.00 USD | 1,750.00 USD | `1` | `2026-10-30 05:30:00 UTC - 2026-10-30 05:35:00 UTC` |
| `15m` | `BALANCED` | 0.00 USD | 1,750.00 USD | 1,750.00 USD | 1,750.00 USD | `1` | `2026-10-30 05:30:00 UTC - 2026-10-30 05:45:00 UTC` |
| `1h` | `BALANCED` | 0.00 USD | 1,750.00 USD | 1,750.00 USD | 1,750.00 USD | `1` | `2026-10-30 05:00:00 UTC - 2026-10-30 06:00:00 UTC` |
| `4h` | `BALANCED` | 0.00 USD | 1,750.00 USD | 1,750.00 USD | 1,750.00 USD | `1` | `2026-10-30 04:00:00 UTC - 2026-10-30 08:00:00 UTC` |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `0 USD` | Total OI Tokens: `-`
  * 1h OI Change: `0.00%` | 4h OI Change: `0.00%` | 24h OI Change: `0.00%`
  * Exchange Breakdown: Binance=`-` | Bybit=`-` | OKX=`-` | Hyperliquid=`-`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `79.30K` | Last 24h: `134.73K` | Last 3d: `246.48K` | Last 7d: `772.71K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0088%` | **USDT OKX** | `0.0100%` |
| **USDT Bybit** | `0.0100%` | **USDT KuCoin** | `0.0100%` |
| **USDT MEXC** | `0.0088%` | **USDT BingX** | `0.0100%` |
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
| `5:00 UTC` | `1265.55` | `1265.89` | `1265.55` | `1274.25` | `1259.25` | 13,172,642.30 USD | 7,854,309.17 USD | 5,318,333.13 USD | 2,535,976.04 USD | `+19.25%` | `13B / 1S` |
| `0:00 UTC` | `1282.05` | `1279.57` | `1282.05` | `1285.35` | `1269.15` | 31,465,166.07 USD | 16,761,441.58 USD | 14,703,724.48 USD | 2,057,717.10 USD | `+6.54%` | `8B / 5S` |
| `5:00 UTC` | `1279.95` | `1280.45` | `1279.95` | `1287.45` | `1275.15` | 19,925,691.14 USD | 8,662,599.23 USD | 11,263,091.92 USD | -2,600,492.69 USD | `-13.05%` | `1B / 6S` |
| `0:00 UTC` | `1275.15` | `1271.95` | `1275.15` | `1279.35` | `1264.95` | 23,738,198.29 USD | 11,363,344.84 USD | 12,374,853.45 USD | -1,011,508.62 USD | `-4.26%` | `3B / 3S` |
| `5:00 UTC` | `1279.05` | `1280.95` | `1279.05` | `1287.45` | `1274.25` | 14,930,858.33 USD | 7,292,403.22 USD | 7,638,455.11 USD | -346,051.88 USD | `-2.32%` | `2B / 4S` |
| `0:00 UTC` | `1285.05` | `1286.06` | `1285.05` | `1289.85` | `1282.05` | 15,953,463.93 USD | 6,542,642.51 USD | 9,410,821.42 USD | -2,868,178.91 USD | `-17.98%` | `1B / 3S` |
| `5:00 UTC` | `1276.95` | `1279.23` | `1276.95` | `1286.25` | `1275.15` | 15,449,899.62 USD | 6,063,485.10 USD | 9,386,414.52 USD | -3,322,929.42 USD | `-21.51%` | `0B / 8S` |
| `0:00 UTC` | `1275.15` | `1278.02` | `1275.15` | `1285.05` | `1272.15` | 16,039,119.46 USD | 6,719,465.52 USD | 9,319,653.95 USD | -2,600,188.43 USD | `-16.21%` | `2B / 3S` |
| `5:00 UTC` | `1272.15` | `1274.44` | `1272.15` | `1278.75` | `1270.65` | 10,354,318.48 USD | 4,552,930.99 USD | 5,801,387.50 USD | -1,248,456.51 USD | `-12.06%` | `0B / 2S` |
| `0:00 UTC` | `1270.05` | `1271.53` | `1270.05` | `1275.75` | `1268.25` | 8,176,427.83 USD | 4,035,540.38 USD | 4,140,887.45 USD | -105,347.06 USD | `-1.29%` | `1B / 0S` |

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
| `5m` | 129,850.00 USD | 98,250.00 USD | **`ACCUMULATION`** |
| `15m` | -89,210.00 USD | -614,320.00 USD | **`DISTRIBUTION`** |
| `30m` | -364,560.00 USD | -1,560,000.00 USD | **`DISTRIBUTION`** |
| `1h` | -2,380,000.00 USD | -12,030,000.00 USD | **`DISTRIBUTION`** |
| `2h` | -1,640,000.00 USD | -13,970,000.00 USD | **`DISTRIBUTION`** |
| `4h` | 7,060,000.00 USD | 13,140,000.00 USD | **`ACCUMULATION`** |
| `6h` | -1,160,000.00 USD | 8,770,000.00 USD | **`ACCUMULATION`** |
| `8h` | 195,000.00 USD | -58,400.00 USD | **`ACCUMULATION`** |
| `12h` | -13,280,000.00 USD | -28,130,000.00 USD | **`DISTRIBUTION`** |
| `24h` | 15,470,000.00 USD | 101,590,000.00 USD | **`ACCUMULATION`** |
| `1w` | 34,910,000.00 USD | 229,980,000.00 USD | **`ACCUMULATION`** |
| `30d` | 60,650,000.00 USD | -529,430,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+129.85K` | 15m=`-89.21K` | 1h=`-2.38M` | 24h=`+15.47M`
* Futures Capital Netflows: 5m=`+98.25K` | 15m=`-614.32K` | 1h=`-12.03M` | 24h=`+101.59M`
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
  * `2026-10-30 11:03:23 IST`: [kitco.com] - (Sentiment: `Neutral`)
  * `2026-10-30 11:09:23 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 09:10:23 IST`: [forex.com] - (Sentiment: `Neutral`)
  * `2026-10-30 11:08:23 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 11:08:23 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 08:10:23 IST`: [financemagnates.com] - (Sentiment: `Neutral`)
  * `2026-10-30 08:10:23 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-30 07:10:23 IST`: [kathleenhays.substack.com] - (Sentiment: `Neutral`)
  * `2026-10-30 06:10:23 IST`: [rba.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 06:10:23 IST`: [abs.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 06:10:23 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 06:10:23 IST`: [@NodeWire] - (Sentiment: `Neutral`)
  * `2026-10-30 06:10:23 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 06:10:23 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 06:10:23 IST`: [@financialjuice] - (Sentiment: `Neutral`)


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
  * Execution Entry: `1233.76` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `1211.84` (Risk Distance: `21.92` pts)
  * +2.5R Take Profit: `1288.57`
  * Mathematical Lot Sizing: **`0.45 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `1285.56` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `1307.48` (Risk Distance: `21.92` pts)
  * +2.5R Take Profit: `1230.75`
  * Mathematical Lot Sizing: **`0.45 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`1283.20`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
