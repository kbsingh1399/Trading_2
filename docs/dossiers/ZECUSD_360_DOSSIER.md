# 🏛️ SOVEREIGN CANDIDATE DOSSIER: ZECUSD
**Canonical Key**: `ZECUSD` | **Broker Instrument**: `ZECUSD.p` | **Asset Class**: `Crypto Altcoin`
**Timestamp**: `2026-10-30 08:58:00 IST` (`2026-10-30 03:28:00 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `1264.56` | **Live Ask Quote**: `1265.95` | **Mid Price**: `1265.26`
- **Spread Points**: `139.00` | **Spread BPS**: `10.99 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `1234.64` | VWAP Z-Score: `+1.45` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `20.66` (Volatility Regime: `HIGH_EXPANSION`)
  * 14-Period RSI: `52.67` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `1289.14` | Lower -3.00σ Band: `1180.14`
  * Upper +2.51σ Band: `1280.24` | Lower -2.51σ Band: `1189.04`
  * Upper +2.01σ Band: `1271.16` | Lower -2.01σ Band: `1198.13`
  * Upper +2.00σ Band: `1270.98` | Lower -2.00σ Band: `1198.31`
  * Upper +1.28σ Band: `1257.90` | Lower -1.28σ Band: `1211.39`
  * Upper +1.00σ Band: `1252.81` | Lower -1.00σ Band: `1216.48`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`1250.56` | EMA-20=`1249.78` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`1263.96` (Slope: `+0.0000`) | EMA-100=`1271.82`
  * Institutional Anchors: EMA-144=`1273.38` | EMA-200=`1274.07` (Slope: `-0.3406`) | EMA-233=`1276.88`
- **Range Boundaries**: 24H High=`1396.49` | 24H Low=`1180.03` | Weekly High=`1396.49` | Weekly Low=`1180.03`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `1263.14` (Distance: `+0.18%`)
  * Point of Control (POC) = `1229.90` (Distance: `+2.89%`)
  * Value Area Low (VAL) = `1222.17` (Distance: `+3.54%`)
  * Auction Positioning: `ABOVE_VALUE (Imbalance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `RANGE_EXPANSION`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`1309.91` | POC=`1246.71` | VAL=`1230.27`
  * Prior Day Extremes: PDH=`1396.49` | PDL=`1206.89` | PDC=`1244.38`
  * Monday Range Blueprint: High=`1267.53` | Mid=`1222.14` | Low=`1176.75`
  * Developing Weekly Value Area: Weekly VAH=`1296.14` | Weekly POC=`1239.01` | Weekly VAL=`1200.92`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`1296.00` | Low=`1180.03`
  * London Session (08:00-16:00 UTC): High=`1270.32` | Low=`1260.19`
  * New York Session (13:00-21:00 UTC): High=`1272.85` | Low=`1257.66`
  * Initial Balance (First Hour): IB High=`1269.05` | IB Low=`1261.46`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `1260.19` - `1270.32`
  * Optimal Trade Entry (OTE 0.705): `1267.79`
  * Structural Invalidation Anchor (0.786): `1275.38`

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
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 08:53:31 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `13` | `0xb83d...6e36` | `SHORT` | 66,513,831.26 USD | `52,385.47` | `1336.45` | `1268.00` | `3811.87` | 3,496,736.14 USD | `+5.26%` | `3X Cross` |
| `22` | `0x5b5d...c060` | `SHORT` | 50,769,594.25 USD | `40,121.38` | `1478.36` | `1268.00` | `5322.97` | 8,544,440.86 USD | `+16.83%` | `3X Cross` |
| `40` | `0x7fda...17d1` | `SHORT` | 31,017,669.23 USD | `24,454.17` | `1261.42` | `1268.00` | `2764.69` | -170,665.46 USD | `-0.55%` | `5X Cross` |
| `80` | `0x60b0...991e` | `LONG` | 21,313,625.75 USD | `16,779.74` | `1179.65` | `1268.00` | `938.13` | 1,519,378.73 USD | `+7.13%` | `10X Cross` |
| `138` | `0xc36a...105b` | `LONG` | 14,583,057.86 USD | `11,510.82` | `1215.14` | `1268.00` | `973.82` | 595,776.83 USD | `+4.09%` | `10X Cross` |
| `152` | `0x9071...5c0b` | `LONG` | 13,326,458.16 USD | `10,517.29` | `1353.83` | `1268.00` | `0.1126` | -912,160.71 USD | `-6.84%` | `1X Cross` |
| `173` | `0x8742...8427` | `LONG` | 11,658,853.19 USD | `9,201.21` | `1286.37` | `1268.00` | `715.94` | -177,316.80 USD | `-1.52%` | `10X Cross` |
| `189` | `0x58b2...11f3` | `LONG` | 10,848,566.05 USD | `8,563.08` | `1246.56` | `1268.00` | `381.98` | 174,148.48 USD | `+1.61%` | `10X Cross` |
| `193` | `0x9ffd...ce40` | `LONG` | 10,715,531.81 USD | `8,434.77` | `1250.94` | `1268.00` | `602.67` | 164,113.92 USD | `+1.53%` | `5X Cross` |
| `194` | `0xad59...ba81` | `SHORT` | 10,697,222.50 USD | `8,425.00` | `330.91` | `1268.00` | `2147.30` | -7,909,264.73 USD | `-73.94%` | `10X Cross` |
| `205` | `0xdd53...2b13` | `SHORT` | 10,380,952.27 USD | `8,195.92` | `741.54` | `1268.00` | `8841.88` | -4,303,355.91 USD | `-41.45%` | `3X Cross` |
| `221` | `0x880a...311c` | `SHORT` | 9,764,137.66 USD | `7,707.11` | `1367.50` | `1268.00` | `2242.54` | 775,346.54 USD | `+7.94%` | `10X Cross` |
| `237` | `0xbf73...5d58` | `LONG` | 9,501,750.00 USD | `7,500.00` | `1248.78` | `1268.00` | `150.61` | 135,904.38 USD | `+1.43%` | `10X Cross` |
| `267` | `0x2b61...2f6c` | `LONG` | 8,616,981.30 USD | `6,807.00` | `1453.56` | `1268.00` | `544.22` | -1,277,369.92 USD | `-14.82%` | `10X Cross` |
| `286` | `0x2ae5...83e7` | `LONG` | 8,152,850.88 USD | `6,436.80` | `1391.82` | `1268.00` | `0.000000` | -806,041.11 USD | `-9.89%` | `1X Cross` |
| `328` | `0x26b6...9a13` | `LONG` | 6,884,535.91 USD | `5,433.73` | `1282.23` | `1268.00` | `228.16` | -82,767.32 USD | `-1.20%` | `10X Cross` |
| `342` | `0x45d2...4029` | `SHORT` | 6,623,131.70 USD | `5,227.00` | `833.44` | `1268.00` | `9356.19` | -2,266,753.73 USD | `-34.22%` | `5X Cross` |
| `357` | `0xea00...a918` | `LONG` | 6,351,000.00 USD | `5,000.00` | `739.16` | `1268.00` | `0.000000` | 2,655,184.89 USD | `+41.81%` | `5X Cross` |
| `371` | `0xdd7a...8830` | `LONG` | 6,170,011.21 USD | `4,860.19` | `897.48` | `1268.00` | `792.72` | 1,808,107.53 USD | `+29.30%` | `10X Cross` |
| `377` | `0xecb6...2b00` | `SHORT` | 6,051,130.51 USD | `4,770.68` | `1278.86` | `1268.00` | `7027.41` | 49,887.72 USD | `+0.82%` | `5X Cross` |
| `436` | `0xa61c...66b9` | `LONG` | 4,935,816.00 USD | `3,888.00` | `1148.34` | `1268.00` | `0.000000` | 471,073.86 USD | `+9.54%` | `10X Cross` |
| `448` | `0x469e...58a5` | `SHORT` | 4,814,118.65 USD | `3,799.92` | `1238.77` | `1268.00` | `2026.96` | -106,872.93 USD | `-2.22%` | `10X Cross` |
| `459` | `0x9aa5...58af` | `SHORT` | 4,711,028.55 USD | `3,720.31` | `1205.51` | `1268.00` | `3742.46` | -226,141.75 USD | `-4.80%` | `10X Cross` |
| `462` | `0x0153...8052` | `SHORT` | 4,688,552.60 USD | `3,698.18` | `1307.82` | `1268.00` | `2504.82` | 148,018.14 USD | `+3.16%` | `1X Isolated` |
| `493` | `0x4cae...7c34` | `LONG` | 4,439,392.44 USD | `3,500.27` | `1143.60` | `1268.00` | `951.60` | 436,470.10 USD | `+9.83%` | `10X Cross` |
| `519` | `0x456f...cdf1` | `LONG` | 4,204,603.34 USD | `3,310.19` | `1267.51` | `1268.00` | `537.87` | 8,898.15 USD | `+0.21%` | `10X Cross` |
| `523` | `0x382b...3e39` | `LONG` | 4,196,753.62 USD | `3,303.75` | `1215.08` | `1268.00` | `0.000000` | 182,434.24 USD | `+4.35%` | `10X Cross` |
| `531` | `0xd21d...90f1` | `LONG` | 4,118,075.00 USD | `3,250.00` | `1253.64` | `1268.00` | `876.03` | 43,733.27 USD | `+1.06%` | `4X Isolated` |
| `548` | `0x1338...c48e` | `LONG` | 3,986,863.44 USD | `3,149.43` | `1018.52` | `1268.00` | `820.32` | 779,117.89 USD | `+19.54%` | `4X Isolated` |
| `550` | `0xd4c1...3d1d` | `SHORT` | 3,977,101.28 USD | `3,137.01` | `1295.08` | `1268.00` | `2712.00` | 85,566.97 USD | `+2.15%` | `10X Cross` |
| `558` | `0x325e...9564` | `LONG` | 3,937,874.75 USD | `3,101.91` | `1298.07` | `1268.00` | `205.85` | -88,635.95 USD | `-2.25%` | `10X Cross` |
| `564` | `0xdbe0...d6d5` | `LONG` | 3,908,238.18 USD | `3,085.37` | `422.97` | `1268.00` | `338.64` | 2,603,233.69 USD | `+66.61%` | `3X Isolated` |
| `591` | `0x9c06...0560` | `SHORT` | 3,797,942.94 USD | `2,989.80` | `786.00` | `1268.00` | `2622.15` | -1,447,947.94 USD | `-38.12%` | `10X Cross` |
| `595` | `0x27c9...d65d` | `SHORT` | 3,762,476.16 USD | `2,961.88` | `1254.41` | `1268.00` | `1743.47` | -47,060.96 USD | `-1.25%` | `10X Cross` |
| `598` | `0x2e30...4cb5` | `SHORT` | 3,750,902.82 USD | `2,960.46` | `1287.96` | `1268.00` | `2907.26` | 62,056.23 USD | `+1.65%` | `2X Cross` |
| `628` | `0x5323...b23c` | `SHORT` | 3,574,649.18 USD | `2,822.24` | `1260.38` | `1268.00` | `3219.78` | -17,565.47 USD | `-0.49%` | `5X Cross` |
| `688` | `0xac48...3201` | `LONG` | 3,215,511.30 USD | `2,531.50` | `1378.58` | `1268.00` | `508.91` | -274,360.98 USD | `-8.53%` | `10X Cross` |
| `690` | `0xa183...0482` | `LONG` | 3,210,831.40 USD | `2,534.00` | `530.25` | `1268.00` | `444.56` | 1,867,168.68 USD | `+58.15%` | `5X Isolated` |
| `696` | `0x0871...e927` | `LONG` | 3,175,750.00 USD | `2,500.00` | `1276.50` | `1268.00` | `0.000000` | -15,500.00 USD | `-0.49%` | `10X Cross` |
| `711` | `0x9b86...6e6e` | `LONG` | 3,127,652.01 USD | `2,463.30` | `637.58` | `1268.00` | `882.49` | 1,557,102.73 USD | `+49.79%` | `3X Cross` |
| `742` | `0x71d0...8c26` | `SHORT` | 3,065,627.70 USD | `2,413.50` | `1262.25` | `1268.00` | `3485.51` | -19,178.75 USD | `-0.63%` | `10X Cross` |
| `771` | `0xb2f7...af9f` | `SHORT` | 2,937,730.28 USD | `2,313.72` | `746.63` | `1268.00` | `4538.50` | -1,210,241.54 USD | `-41.20%` | `10X Cross` |
| `792` | `0x413c...886c` | `LONG` | 2,848,725.00 USD | `2,250.00` | `1237.51` | `1268.00` | `0.000000` | 64,323.97 USD | `+2.26%` | `10X Cross` |
| `807` | `0xf48f...10fe` | `LONG` | 2,808,830.19 USD | `2,218.49` | `1517.87` | `1268.00` | `1013.86` | -558,556.64 USD | `-19.89%` | `3X Cross` |
| `831` | `0x5bc4...3b0c` | `SHORT` | 2,698,795.28 USD | `2,130.74` | `1089.65` | `1268.00` | `3720.49` | -377,037.71 USD | `-13.97%` | `5X Cross` |
| `851` | `0x8de4...b9aa` | `SHORT` | 2,656,774.82 USD | `2,091.29` | `1331.35` | `1268.00` | `1689.94` | 127,464.89 USD | `+4.80%` | `3X Cross` |
| `858` | `0x4fe2...ac59` | `SHORT` | 2,631,722.53 USD | `2,071.57` | `1478.56` | `1268.00` | `1856.73` | 431,223.69 USD | `+16.39%` | `10X Cross` |
| `871` | `0xdf57...93f5` | `LONG` | 2,604,299.50 USD | `2,054.35` | `1227.36` | `1268.00` | `897.27` | 82,877.45 USD | `+3.18%` | `4X Isolated` |
| `878` | `0xbcd4...0dd2` | `LONG` | 2,582,468.22 USD | `2,033.92` | `1228.20` | `1268.00` | `710.54` | 84,417.41 USD | `+3.27%` | `10X Cross` |
| `887` | `0x9a99...d21a` | `LONG` | 2,540,800.00 USD | `2,000.00` | `1278.44` | `1268.00` | `0.000000` | -16,073.67 USD | `-0.63%` | `10X Cross` |
| `889` | `0xf29c...9971` | `LONG` | 2,534,200.00 USD | `2,000.00` | `1254.95` | `1268.00` | `0.000000` | 24,302.93 USD | `+0.96%` | `10X Cross` |
| `910` | `0x77ee...2902` | `SHORT` | 2,463,479.38 USD | `1,946.03` | `759.84` | `1268.00` | `5461.24` | -984,801.87 USD | `-39.98%` | `10X Cross` |
| `917` | `0x3e2f...b269` | `SHORT` | 2,438,850.97 USD | `1,925.51` | `1134.87` | `1268.00` | `2931.87` | -253,652.11 USD | `-10.40%` | `10X Cross` |
| `918` | `0xb122...e4ba` | `LONG` | 2,437,488.21 USD | `1,924.89` | `1255.46` | `1268.00` | `968.29` | 20,861.14 USD | `+0.86%` | `10X Cross` |
| `930` | `0x4f12...618b` | `SHORT` | 2,399,363.08 USD | `1,896.28` | `1608.30` | `1268.00` | `2116.83` | 650,421.31 USD | `+27.11%` | `3X Cross` |
| `968` | `0x866d...d6e1` | `LONG` | 2,281,215.10 USD | `1,802.05` | `674.73` | `1268.00` | `292.92` | 1,065,313.78 USD | `+46.70%` | `10X Cross` |
| `990` | `0x2309...a2d9` | `LONG` | 2,214,918.20 USD | `1,750.37` | `1186.09` | `1268.00` | `817.09` | 138,824.09 USD | `+6.27%` | `8X Cross` |
| `1028` | `0x265e...7f70` | `LONG` | 2,088,460.06 USD | `1,651.74` | `1382.98` | `1268.00` | `0.000000` | -195,862.70 USD | `-9.38%` | `3X Cross` |
| `1030` | `0xfe7c...b7ae` | `SHORT` | 2,086,481.33 USD | `1,642.64` | `1346.92` | `1268.00` | `5919.93` | 126,027.29 USD | `+6.04%` | `10X Cross` |
| `1037` | `0x3e47...aaf6` | `LONG` | 2,077,584.72 USD | `1,636.28` | `1278.38` | `1268.00` | `1053.20` | -14,207.07 USD | `-0.68%` | `10X Cross` |
| `1040` | `0x2edd...8179` | `SHORT` | 2,070,138.63 USD | `1,633.89` | `1261.58` | `1268.00` | `2931.45` | -8,856.71 USD | `-0.43%` | `10X Cross` |
| `1052` | `0x7f75...9edf` | `LONG` | 2,039,676.21 USD | `1,609.72` | `1200.14` | `1268.00` | `982.39` | 107,791.16 USD | `+5.28%` | `10X Cross` |
| `1059` | `0x6646...6de5` | `SHORT` | 2,026,880.00 USD | `1,600.00` | `660.64` | `1268.00` | `4140.90` | -969,855.03 USD | `-47.85%` | `10X Cross` |
| `1061` | `0x023a...2355` | `SHORT` | 2,024,725.55 USD | `1,594.90` | `1310.00` | `1268.00` | `4493.95` | 64,586.59 USD | `+3.19%` | `10X Cross` |
| `1073` | `0x3205...40bb` | `SHORT` | 2,010,299.75 USD | `1,585.66` | `1245.09` | `1268.00` | `2185.01` | -36,006.47 USD | `-1.79%` | `10X Cross` |
| `1097` | `0xab59...59b5` | `LONG` | 1,983,416.97 USD | `1,565.32` | `1342.15` | `1268.00` | `843.99` | -117,478.25 USD | `-5.92%` | `10X Cross` |
| `1149` | `0xcf67...eb24` | `LONG` | 1,900,650.00 USD | `1,500.00` | `887.05` | `1268.00` | `700.00` | 570,078.63 USD | `+29.99%` | `10X Cross` |
| `1164` | `0xb695...a92d` | `LONG` | 1,878,071.20 USD | `1,483.00` | `1249.80` | `1268.00` | `0.000000` | 24,612.35 USD | `+1.31%` | `10X Cross` |
| `1167` | `0x7277...0b98` | `SHORT` | 1,870,782.92 USD | `1,475.73` | `1287.86` | `1268.00` | `2194.66` | 29,749.20 USD | `+1.59%` | `10X Cross` |
| `1236` | `0x2ab7...c2f8` | `LONG` | 1,773,885.97 USD | `1,400.51` | `813.26` | `1268.00` | `793.74` | 634,904.28 USD | `+35.79%` | `3X Cross` |
| `1251` | `0x11be...8b1d` | `LONG` | 1,741,938.36 USD | `1,375.83` | `1206.55` | `1268.00` | `1134.54` | 81,930.41 USD | `+4.70%` | `10X Isolated` |
| `1288` | `0xfc27...9d9d` | `SHORT` | 1,671,190.04 USD | `1,319.43` | `1298.53` | `1268.00` | `15580.55` | 42,126.74 USD | `+2.52%` | `10X Cross` |
| `1320` | `0x039c...0ebd` | `SHORT` | 1,621,621.91 USD | `1,279.79` | `1239.81` | `1268.00` | `3674.09` | -34,920.08 USD | `-2.15%` | `10X Cross` |
| `1337` | `0xe065...0f85` | `SHORT` | 1,599,600.61 USD | `1,262.61` | `1087.02` | `1268.00` | `1615.77` | -227,124.48 USD | `-14.20%` | `10X Cross` |
| `1414` | `0x5975...9abd` | `LONG` | 1,524,240.00 USD | `1,200.00` | `1179.54` | `1268.00` | `561.75` | 108,797.21 USD | `+7.14%` | `5X Cross` |
| `1416` | `0x266b...efcb` | `LONG` | 1,521,360.00 USD | `1,200.00` | `893.76` | `1268.00` | `425.57` | 448,850.30 USD | `+29.50%` | `10X Cross` |
| `1437` | `0x2847...d47b` | `LONG` | 1,501,106.06 USD | `1,186.27` | `1232.07` | `1268.00` | `0.000000` | 39,537.56 USD | `+2.63%` | `5X Cross` |
| `1460` | `0x69cc...14fd` | `SHORT` | 1,472,256.07 USD | `1,161.36` | `675.33` | `1268.00` | `8172.46` | -687,950.54 USD | `-46.73%` | `10X Cross` |
| `1478` | `0x3fc5...c0c1` | `SHORT` | 1,454,039.88 USD | `1,148.44` | `1264.34` | `1266.70` | `2892.01` | -2,026.11 USD | `-0.14%` | `10X Cross` |
| `1500` | `0xe35c...a1d3` | `LONG` | 1,430,802.67 USD | `1,127.06` | `1318.20` | `1266.70` | `694.46` | -54,892.68 USD | `-3.84%` | `2X Isolated` |
| `1518` | `0x5f94...4b96` | `LONG` | 1,416,058.32 USD | `1,115.27` | `538.00` | `1266.70` | `0.000000` | 816,040.68 USD | `+57.63%` | `10X Cross` |
| `1534` | `0x38f9...cb04` | `SHORT` | 1,396,102.51 USD | `1,100.68` | `1243.50` | `1266.70` | `2038.23` | -27,411.29 USD | `-1.96%` | `10X Cross` |
| `1542` | `0x71df...a23d` | `SHORT` | 1,391,410.93 USD | `1,098.28` | `513.50` | `1266.70` | `2558.73` | -827,440.74 USD | `-59.47%` | `2X Cross` |
| `1561` | `0xbfc7...80b4` | `SHORT` | 1,361,917.50 USD | `1,075.00` | `558.03` | `1266.70` | `2983.86` | -762,038.77 USD | `-55.95%` | `10X Cross` |
| `1599` | `0x51f6...2b39` | `SHORT` | 1,309,027.02 USD | `1,033.66` | `1299.77` | `1266.70` | `2485.79` | 34,491.59 USD | `+2.63%` | `10X Cross` |
| `1627` | `0x123d...3bff` | `SHORT` | 1,282,444.73 USD | `1,009.64` | `491.08` | `1266.70` | `4426.98` | -786,626.82 USD | `-61.34%` | `10X Cross` |
| `1646` | `0xe282...df29` | `LONG` | 1,267,100.00 USD | `1,000.00` | `420.99` | `1266.70` | `835.99` | 846,113.14 USD | `+66.78%` | `10X Cross` |
| `1648` | `0x668c...ea2e` | `SHORT` | 1,265,400.00 USD | `1,000.00` | `1406.98` | `1266.70` | `4184.43` | 141,581.99 USD | `+11.19%` | `10X Cross` |
| `1667` | `0x17f0...094f` | `LONG` | 1,250,356.29 USD | `984.30` | `1287.23` | `1266.70` | `536.89` | -16,663.87 USD | `-1.33%` | `5X Cross` |
| `1745` | `0x757d...94ba` | `LONG` | 1,172,067.50 USD | `925.00` | `1558.31` | `1266.70` | `0.000000` | -269,373.09 USD | `-22.98%` | `10X Cross` |
| `1748` | `0xaa82...9556` | `LONG` | 1,171,519.60 USD | `924.13` | `1254.72` | `1266.70` | `183.87` | 11,992.92 USD | `+1.02%` | `10X Cross` |
| `1791` | `0xb911...5525` | `LONG` | 1,138,410.00 USD | `900.00` | `1294.82` | `1266.70` | `1035.32` | -26,927.82 USD | `-2.37%` | `10X Cross` |
| `1838` | `0xcf0a...856f` | `LONG` | 1,103,137.25 USD | `871.15` | `1292.19` | `1266.70` | `1011.53` | -22,557.60 USD | `-2.04%` | `4X Cross` |
| `1842` | `0xef96...9383` | `SHORT` | 1,100,374.98 USD | `868.42` | `1259.08` | `1266.70` | `5472.73` | -6,963.19 USD | `-0.63%` | `10X Cross` |
| `1863` | `0xdf95...7d72` | `SHORT` | 1,083,908.88 USD | `853.27` | `1074.39` | `1266.70` | `45878.48` | -167,161.44 USD | `-15.42%` | `10X Cross` |
| `1865` | `0x2577...4897` | `SHORT` | 1,080,834.75 USD | `850.85` | `1262.87` | `1266.70` | `5045.77` | -6,320.41 USD | `-0.58%` | `10X Cross` |
| `1901` | `0x601c...4f54` | `SHORT` | 1,042,314.21 USD | `824.42` | `615.11` | `1266.70` | `3148.76` | -535,201.45 USD | `-51.35%` | `5X Cross` |
| `1912` | `0xae55...2236` | `LONG` | 1,035,407.50 USD | `817.47` | `1467.80` | `1266.70` | `0.000000` | -164,473.71 USD | `-15.88%` | `10X Cross` |
| `1950` | `0x0f02...5384` | `LONG` | 1,015,389.04 USD | `800.78` | `1290.36` | `1266.70` | `310.82` | -17,905.03 USD | `-1.76%` | `3X Cross` |
| `1952` | `0x9b0f...db40` | `LONG` | 1,013,319.60 USD | `800.00` | `1268.86` | `1266.70` | `800.93` | -1,770.16 USD | `-0.17%` | `10X Cross` |
| `1956` | `0x11ee...1d1d` | `SHORT` | 1,012,320.00 USD | `800.00` | `1269.65` | `1266.70` | `1616.99` | 3,403.01 USD | `+0.34%` | `5X Cross` |
| `1970` | `0x6e8f...4364` | `LONG` | 1,007,538.68 USD | `793.65` | `1260.00` | `1266.70` | `1009.97` | 7,539.68 USD | `+0.75%` | `10X Cross` |
| `1975` | `0xabdb...84ac` | `LONG` | 1,004,732.17 USD | `793.69` | `711.79` | `1266.70` | `664.46` | 439,791.81 USD | `+43.77%` | `3X Cross` |
| `1977` | `0xdf83...3cff` | `SHORT` | 1,003,745.94 USD | `792.16` | `1254.45` | `1266.70` | `1910.64` | -10,020.64 USD | `-1.00%` | `10X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| Intel | Baseline | - | - | - | Neutral | - | No anomalous telegram alerts in current window | - |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`1404.55` (Vol: 3,000,000.00 USD, Dist: `+11.26%`) | Long MP=`1176.48` (Vol: 3,400,000.00 USD, Dist: `--6.80%`)
  * 48H Horizon: Short MP=`1404.55` (Vol: 3,000,000.00 USD, Dist: `+11.26%`) | Long MP=`1176.48` (Vol: 3,400,000.00 USD, Dist: `--6.80%`)
  * 3D Horizon: Short MP=`1404.55` (Vol: 3,000,000.00 USD, Dist: `+11.26%`) | Long MP=`1176.48` (Vol: 3,100,000.00 USD, Dist: `--6.80%`)
  * 7D Horizon: Short MP=`1404.10` (Vol: 3,000,000.00 USD, Dist: `+11.23%`) | Long MP=`1176.74` (Vol: 4,900,000.00 USD, Dist: `--6.78%`)
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
| `5m` | `BALANCED` | 0.00 USD | 1,750.00 USD | 1,750.00 USD | 1,750.00 USD | `1` | `2026-10-30 03:20:00 UTC - 2026-10-30 03:25:00 UTC` |
| `15m` | `BALANCED` | 0.00 USD | 1,750.00 USD | 1,750.00 USD | 1,750.00 USD | `1` | `2026-10-30 03:15:00 UTC - 2026-10-30 03:30:00 UTC` |
| `1h` | `BALANCED` | 0.00 USD | 1,750.00 USD | 1,750.00 USD | 1,750.00 USD | `1` | `2026-10-30 03:00:00 UTC - 2026-10-30 04:00:00 UTC` |
| `4h` | `BALANCED` | 0.00 USD | 1,750.00 USD | 1,750.00 USD | 1,750.00 USD | `1` | `2026-10-30 00:00:00 UTC - 2026-10-30 04:00:00 UTC` |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `0 USD` | Total OI Tokens: `-`
  * 1h OI Change: `0.00%` | 4h OI Change: `0.00%` | 24h OI Change: `0.00%`
  * Exchange Breakdown: Binance=`-` | Bybit=`-` | OKX=`-` | Hyperliquid=`-`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `85.96K` | Last 24h: `133.88K` | Last 3d: `245.74K` | Last 7d: `771.70K`
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
| `0:00 UTC` | `1230.15` | `1232.52` | `1230.15` | `1240.05` | `1225.05` | 27,822,128.62 USD | 14,746,863.10 USD | 13,075,265.52 USD | 1,671,597.57 USD | `+6.01%` | `5B / 1S` |
| `5:00 UTC` | `1219.95` | `1220.53` | `1219.95` | `1230.45` | `1215.45` | 25,624,282.39 USD | 13,502,208.52 USD | 12,122,073.88 USD | 1,380,134.64 USD | `+5.39%` | `6B / 3S` |
| `0:00 UTC` | `1245.15` | `1232.68` | `1245.15` | `1249.05` | `1206.75` | 51,931,159.61 USD | 26,761,787.01 USD | 25,169,372.61 USD | 1,592,414.40 USD | `+3.07%` | `20B / 9S` |
| `5:00 UTC` | `1236.45` | `1237.15` | `1236.45` | `1245.15` | `1230.45` | 21,904,768.45 USD | 9,625,705.12 USD | 12,279,063.33 USD | -2,653,358.20 USD | `-12.11%` | `1B / 0S` |
| `0:00 UTC` | `1228.65` | `1236.25` | `1228.65` | `1253.25` | `1219.35` | 45,146,863.08 USD | 23,450,812.50 USD | 21,696,050.59 USD | 1,754,761.91 USD | `+3.89%` | `18B / 9S` |
| `5:00 UTC` | `1254.75` | `1256.85` | `1254.75` | `1263.45` | `1247.85` | 37,496,922.68 USD | 20,689,312.95 USD | 16,807,609.72 USD | 3,881,703.23 USD | `+10.35%` | `5B / 3S` |
| `0:00 UTC` | `1263.45` | `1263.47` | `1263.45` | `1267.65` | `1258.35` | 21,490,941.27 USD | 11,626,504.00 USD | 9,864,437.27 USD | 1,762,066.74 USD | `+8.20%` | `2B / 3S` |
| `5:00 UTC` | `1257.45` | `1259.53` | `1257.45` | `1270.05` | `1249.95` | 34,915,865.69 USD | 14,880,758.20 USD | 20,035,107.50 USD | -5,154,349.30 USD | `-14.76%` | `1B / 7S` |
| `0:00 UTC` | `1260.15` | `1262.58` | `1260.15` | `1267.95` | `1257.15` | 13,992,732.07 USD | 6,287,729.60 USD | 7,705,002.47 USD | -1,417,272.88 USD | `-10.13%` | `0B / 2S` |
| `5:00 UTC` | `1260.15` | `1261.89` | `1260.15` | `1265.55` | `1259.25` | 3,683,995.80 USD | 2,071,736.09 USD | 1,612,259.71 USD | 459,476.38 USD | `+12.47%` | `4B / 1S` |

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
| `5m` | 148,990.00 USD | 157,370.00 USD | **`ACCUMULATION`** |
| `15m` | 661,440.00 USD | -1,030,000.00 USD | **`DISTRIBUTION`** |
| `30m` | -475,390.00 USD | -7,540,000.00 USD | **`DISTRIBUTION`** |
| `1h` | 1,430,000.00 USD | 706,370.00 USD | **`ACCUMULATION`** |
| `2h` | 8,080,000.00 USD | 21,220,000.00 USD | **`ACCUMULATION`** |
| `4h` | 1,160,000.00 USD | 14,040,000.00 USD | **`ACCUMULATION`** |
| `6h` | 3,380,000.00 USD | 10,160,000.00 USD | **`ACCUMULATION`** |
| `8h` | -10,540,000.00 USD | -3,720,000.00 USD | **`DISTRIBUTION`** |
| `12h` | 6,500,000.00 USD | 54,550,000.00 USD | **`ACCUMULATION`** |
| `24h` | 15,500,000.00 USD | 111,880,000.00 USD | **`ACCUMULATION`** |
| `1w` | 37,190,000.00 USD | 232,940,000.00 USD | **`ACCUMULATION`** |
| `30d` | 62,100,000.00 USD | -517,890,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+148.99K` | 15m=`+661.44K` | 1h=`+1.43M` | 24h=`+15.50M`
* Futures Capital Netflows: 5m=`+157.37K` | 15m=`-1.03M` | 1h=`+706.37K` | 24h=`+111.88M`
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
  * `2026-10-30 08:33:58 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 08:32:58 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 08:00:58 IST`: [financemagnates.com] - (Sentiment: `Neutral`)
  * `2026-10-30 08:48:58 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-30 08:47:58 IST`: [kathleenhays.substack.com] - (Sentiment: `Neutral`)
  * `2026-10-30 08:47:58 IST`: [rba.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 08:47:58 IST`: [abs.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 05:49:58 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 05:49:58 IST`: [@NodeWire] - (Sentiment: `Neutral`)
  * `2026-10-30 05:49:58 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 05:49:58 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 05:49:58 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-30 05:49:58 IST`: [media.rabobank.com] - (Sentiment: `Neutral`)
  * `2026-10-30 04:49:58 IST`: [economics.td.com] - (Sentiment: `Neutral`)
  * `2026-10-30 03:49:58 IST`: [investinglive.com] - (Sentiment: `Neutral`)


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
  * Execution Entry: `1222.17` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `1195.29` (Risk Distance: `26.88` pts)
  * +2.5R Take Profit: `1289.37`
  * Mathematical Lot Sizing: **`0.37 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `1263.14` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `1290.02` (Risk Distance: `26.88` pts)
  * +2.5R Take Profit: `1195.94`
  * Mathematical Lot Sizing: **`0.37 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`1275.38`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
