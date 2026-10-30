# 🏛️ SOVEREIGN CANDIDATE DOSSIER: ZECUSD
**Canonical Key**: `ZECUSD` | **Broker Instrument**: `ZECUSD.p` | **Asset Class**: `Crypto Altcoin`
**Timestamp**: `2026-10-30 11:47:32 IST` (`2026-10-30 06:17:32 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `1272.34` | **Live Ask Quote**: `1273.63` | **Mid Price**: `1272.99`
- **Spread Points**: `129.00` | **Spread BPS**: `10.13 bps` (Charter Threshold: `25.00 bps`)
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
  * Value Area High (VAH) = `1285.56` (Distance: `-0.86%`)
  * Point of Control (POC) = `1275.51` (Distance: `-0.08%`)
  * Value Area Low (VAL) = `1235.31` (Distance: `+3.17%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`1309.91` | POC=`1246.71` | VAL=`1230.27`
  * Prior Day Extremes: PDH=`1396.49` | PDL=`1206.89` | PDC=`1244.38`
  * Monday Range Blueprint: High=`1267.53` | Mid=`1222.14` | Low=`1176.75`
  * Developing Weekly Value Area: Weekly VAH=`1294.68` | Weekly POC=`1239.01` | Weekly VAL=`1200.92`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`1296.00` | Low=`1180.03`
  * London Session (08:00-16:00 UTC): High=`1283.82` | Low=`1263.39`
  * New York Session (13:00-21:00 UTC): High=`1280.62` | Low=`1265.35`
  * Initial Balance (First Hour): IB High=`1283.82` | IB Low=`1264.92`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `1267.89` - `1278.08`
  * Optimal Trade Entry (OTE 0.705): `1275.53`
  * Structural Invalidation Anchor (0.786): `1283.17`

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
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 11:43:56 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `13` | `0xb83d...6e36` | `SHORT` | 66,770,520.06 USD | `52,385.47` | `1336.45` | `1273.10` | `3662.34` | 3,240,047.34 USD | `+4.85%` | `3X Cross` |
| `22` | `0x5b5d...c060` | `SHORT` | 51,090,565.29 USD | `40,121.38` | `1478.36` | `1273.10` | `5078.31` | 8,223,469.82 USD | `+16.10%` | `3X Cross` |
| `38` | `0x7fda...17d1` | `SHORT` | 33,435,982.51 USD | `26,214.02` | `1262.66` | `1273.10` | `2601.42` | -336,502.46 USD | `-1.01%` | `5X Cross` |
| `81` | `0x60b0...991e` | `LONG` | 21,389,134.58 USD | `16,779.74` | `1179.65` | `1273.10` | `918.71` | 1,594,887.56 USD | `+7.46%` | `10X Cross` |
| `139` | `0xc36a...105b` | `LONG` | 14,679,748.75 USD | `11,510.82` | `1215.14` | `1273.10` | `960.59` | 692,467.72 USD | `+4.72%` | `10X Cross` |
| `156` | `0x9071...5c0b` | `LONG` | 13,412,699.94 USD | `10,517.29` | `1353.83` | `1273.10` | `0.1837` | -825,918.94 USD | `-6.16%` | `1X Cross` |
| `178` | `0x8742...8427` | `LONG` | 11,728,782.39 USD | `9,201.21` | `1286.37` | `1273.10` | `697.01` | -107,387.61 USD | `-0.92%` | `10X Cross` |
| `194` | `0x58b2...11f3` | `LONG` | 10,914,501.77 USD | `8,563.08` | `1246.56` | `1273.10` | `382.75` | 240,084.19 USD | `+2.20%` | `10X Cross` |
| `200` | `0xad59...ba81` | `SHORT` | 10,738,505.00 USD | `8,425.00` | `330.91` | `1273.10` | `2144.57` | -7,950,547.23 USD | `-74.04%` | `10X Cross` |
| `201` | `0x9ffd...ce40` | `LONG` | 10,722,998.11 USD | `8,400.97` | `1251.91` | `1273.10` | `596.04` | 205,734.57 USD | `+1.92%` | `5X Cross` |
| `205` | `0xdd53...2b13` | `SHORT` | 10,446,519.63 USD | `8,195.92` | `741.54` | `1273.10` | `8378.54` | -4,368,923.27 USD | `-41.82%` | `3X Cross` |
| `223` | `0x880a...311c` | `SHORT` | 9,815,004.59 USD | `7,707.11` | `1367.50` | `1273.10` | `2270.82` | 724,479.62 USD | `+7.38%` | `10X Cross` |
| `237` | `0xbf73...5d58` | `LONG` | 9,550,500.00 USD | `7,500.00` | `1248.78` | `1273.10` | `112.69` | 184,654.38 USD | `+1.93%` | `10X Cross` |
| `271` | `0x2b61...2f6c` | `LONG` | 8,681,647.80 USD | `6,807.00` | `1453.56` | `1273.10` | `579.74` | -1,212,703.42 USD | `-13.97%` | `10X Cross` |
| `286` | `0x2ae5...83e7` | `LONG` | 8,208,851.04 USD | `6,436.80` | `1391.82` | `1273.10` | `0.000000` | -750,040.95 USD | `-9.14%` | `1X Cross` |
| `332` | `0x26b6...9a13` | `LONG` | 6,920,941.90 USD | `5,433.73` | `1282.23` | `1273.10` | `231.06` | -46,361.33 USD | `-0.67%` | `10X Cross` |
| `333` | `0xecb6...2b00` | `SHORT` | 6,818,167.05 USD | `5,353.04` | `1279.05` | `1273.10` | `6366.02` | 28,622.17 USD | `+0.42%` | `5X Cross` |
| `344` | `0x45d2...4029` | `SHORT` | 6,665,993.10 USD | `5,227.00` | `833.44` | `1273.10` | `8804.69` | -2,309,615.13 USD | `-34.65%` | `5X Cross` |
| `362` | `0xea00...a918` | `LONG` | 6,373,500.00 USD | `5,000.00` | `739.16` | `1273.10` | `0.000000` | 2,677,684.89 USD | `+42.01%` | `5X Cross` |
| `376` | `0xdd7a...8830` | `LONG` | 6,194,798.17 USD | `4,860.19` | `897.48` | `1273.10` | `780.19` | 1,832,894.50 USD | `+29.59%` | `10X Cross` |
| `418` | `0x469e...58a5` | `SHORT` | 5,302,242.72 USD | `4,163.52` | `1242.31` | `1273.10` | `1975.37` | -129,858.07 USD | `-2.45%` | `10X Cross` |
| `432` | `0x4cae...7c34` | `LONG` | 5,096,890.84 USD | `4,002.27` | `1169.72` | `1273.10` | `963.87` | 415,341.50 USD | `+8.15%` | `10X Cross` |
| `442` | `0xa61c...66b9` | `LONG` | 4,955,256.00 USD | `3,888.00` | `1148.34` | `1273.10` | `0.000000` | 490,513.86 USD | `+9.90%` | `10X Cross` |
| `451` | `0xd4c1...3d1d` | `SHORT` | 4,880,706.74 USD | `3,831.01` | `1292.39` | `1273.10` | `2328.74` | 70,471.25 USD | `+1.44%` | `10X Cross` |
| `471` | `0x9aa5...58af` | `SHORT` | 4,738,558.85 USD | `3,720.31` | `1205.51` | `1273.10` | `3660.24` | -253,672.05 USD | `-5.35%` | `10X Cross` |
| `475` | `0x0153...8052` | `SHORT` | 4,711,481.32 USD | `3,698.18` | `1307.82` | `1273.10` | `2504.88` | 125,089.43 USD | `+2.65%` | `1X Isolated` |
| `504` | `0xb122...e4ba` | `LONG` | 4,459,149.86 USD | `3,498.47` | `1265.25` | `1273.10` | `1087.66` | 32,698.33 USD | `+0.73%` | `10X Cross` |
| `532` | `0x382b...3e39` | `LONG` | 4,163,631.84 USD | `3,269.44` | `1215.08` | `1273.10` | `0.000000` | 191,001.84 USD | `+4.59%` | `10X Cross` |
| `538` | `0xd21d...90f1` | `LONG` | 4,142,450.00 USD | `3,250.00` | `1253.64` | `1273.10` | `876.10` | 68,108.27 USD | `+1.64%` | `4X Isolated` |
| `551` | `0x456f...cdf1` | `LONG` | 4,052,577.95 USD | `3,179.49` | `1267.80` | `1273.10` | `504.18` | 21,623.03 USD | `+0.53%` | `10X Cross` |
| `560` | `0x1338...c48e` | `LONG` | 4,017,412.91 USD | `3,149.43` | `1018.52` | `1273.10` | `820.39` | 809,667.37 USD | `+20.15%` | `4X Isolated` |
| `568` | `0x325e...9564` | `LONG` | 3,953,384.29 USD | `3,101.91` | `1298.07` | `1273.10` | `140.86` | -73,126.40 USD | `-1.85%` | `10X Cross` |
| `574` | `0xdbe0...d6d5` | `LONG` | 3,930,761.38 USD | `3,085.37` | `422.97` | `1273.10` | `338.71` | 2,625,756.89 USD | `+66.80%` | `3X Isolated` |
| `599` | `0x9c06...0560` | `SHORT` | 3,807,211.32 USD | `2,989.80` | `786.00` | `1273.10` | `2545.79` | -1,457,216.32 USD | `-38.28%` | `10X Cross` |
| `602` | `0x27c9...d65d` | `SHORT` | 3,775,508.44 USD | `2,961.88` | `1254.41` | `1273.10` | `1739.73` | -60,093.23 USD | `-1.59%` | `10X Cross` |
| `605` | `0x2e30...4cb5` | `SHORT` | 3,751,517.77 USD | `2,945.37` | `1286.95` | `1273.10` | `2901.26` | 39,021.59 USD | `+1.04%` | `2X Cross` |
| `693` | `0x71d0...8c26` | `SHORT` | 3,245,361.57 USD | `2,548.78` | `1266.76` | `1273.10` | `3639.95` | -16,681.24 USD | `-0.51%` | `10X Cross` |
| `699` | `0xa183...0482` | `LONG` | 3,230,089.80 USD | `2,534.00` | `530.25` | `1273.10` | `444.63` | 1,886,427.08 USD | `+58.40%` | `5X Isolated` |
| `700` | `0xac48...3201` | `LONG` | 3,226,903.05 USD | `2,531.50` | `1378.58` | `1273.10` | `558.51` | -262,969.23 USD | `-8.15%` | `10X Cross` |
| `709` | `0x0871...e927` | `LONG` | 3,188,500.00 USD | `2,500.00` | `1276.50` | `1273.10` | `0.000000` | -2,750.00 USD | `-0.09%` | `10X Cross` |
| `728` | `0x9b86...6e6e` | `LONG` | 3,139,722.18 USD | `2,463.30` | `637.58` | `1273.10` | `882.57` | 1,569,172.90 USD | `+49.98%` | `3X Cross` |
| `779` | `0xb2f7...af9f` | `SHORT` | 2,949,067.51 USD | `2,313.72` | `746.63` | `1273.10` | `4417.54` | -1,221,578.77 USD | `-41.42%` | `10X Cross` |
| `806` | `0xf48f...10fe` | `LONG` | 2,827,687.35 USD | `2,218.49` | `1517.87` | `1273.10` | `957.13` | -539,699.47 USD | `-19.09%` | `3X Cross` |
| `813` | `0x5323...b23c` | `SHORT` | 2,802,628.72 USD | `2,198.83` | `1267.49` | `1273.10` | `3770.93` | -15,633.73 USD | `-0.56%` | `5X Cross` |
| `834` | `0x5bc4...3b0c` | `SHORT` | 2,716,693.50 USD | `2,130.74` | `1089.65` | `1273.10` | `3666.10` | -394,935.92 USD | `-14.54%` | `5X Cross` |
| `852` | `0x8de4...b9aa` | `SHORT` | 2,663,048.69 USD | `2,091.29` | `1331.35` | `1273.10` | `1690.01` | 121,191.02 USD | `+4.55%` | `3X Cross` |
| `857` | `0x4fe2...ac59` | `SHORT` | 2,641,251.75 USD | `2,071.57` | `1478.56` | `1273.10` | `1826.61` | 421,694.47 USD | `+15.97%` | `10X Cross` |
| `862` | `0xdf57...93f5` | `LONG` | 2,619,296.25 USD | `2,054.35` | `1227.36` | `1273.10` | `897.34` | 97,874.21 USD | `+3.74%` | `4X Isolated` |
| `870` | `0xbcd4...0dd2` | `LONG` | 2,591,620.86 USD | `2,033.92` | `1228.20` | `1273.10` | `791.10` | 93,570.05 USD | `+3.61%` | `10X Cross` |
| `880` | `0x9a99...d21a` | `LONG` | 2,550,000.00 USD | `2,000.00` | `1278.44` | `1273.10` | `0.000000` | -6,873.67 USD | `-0.27%` | `10X Cross` |
| `881` | `0xf29c...9971` | `LONG` | 2,549,400.00 USD | `2,000.00` | `1254.95` | `1273.10` | `0.000000` | 39,502.93 USD | `+1.55%` | `10X Cross` |
| `903` | `0x77ee...2902` | `SHORT` | 2,478,269.21 USD | `1,946.03` | `759.84` | `1273.10` | `5484.68` | -999,591.70 USD | `-40.33%` | `10X Cross` |
| `915` | `0x3e2f...b269` | `SHORT` | 2,455,025.25 USD | `1,925.51` | `1134.87` | `1273.10` | `2977.28` | -269,826.39 USD | `-10.99%` | `10X Cross` |
| `924` | `0x4f12...618b` | `SHORT` | 2,416,998.49 USD | `1,896.28` | `1608.30` | `1273.10` | `2116.90` | 632,785.90 USD | `+26.18%` | `3X Cross` |
| `967` | `0x866d...d6e1` | `LONG` | 2,294,910.67 USD | `1,802.05` | `674.73` | `1273.10` | `153.79` | 1,079,009.36 USD | `+47.02%` | `10X Cross` |
| `990` | `0x2309...a2d9` | `LONG` | 2,232,246.86 USD | `1,750.37` | `1186.09` | `1273.10` | `812.21` | 156,152.75 USD | `+7.00%` | `8X Cross` |
| `1028` | `0x265e...7f70` | `LONG` | 2,103,325.72 USD | `1,651.74` | `1382.98` | `1273.10` | `0.000000` | -180,997.04 USD | `-8.61%` | `3X Cross` |
| `1034` | `0xfe7c...b7ae` | `SHORT` | 2,093,708.94 USD | `1,642.64` | `1346.92` | `1273.10` | `5585.50` | 118,799.68 USD | `+5.67%` | `10X Cross` |
| `1037` | `0x3e47...aaf6` | `LONG` | 2,085,602.49 USD | `1,636.28` | `1278.38` | `1273.10` | `1045.99` | -6,189.30 USD | `-0.30%` | `10X Cross` |
| `1040` | `0x2edd...8179` | `SHORT` | 2,082,392.80 USD | `1,633.89` | `1261.58` | `1273.10` | `2899.16` | -21,110.89 USD | `-1.01%` | `10X Cross` |
| `1046` | `0x3205...40bb` | `SHORT` | 2,069,269.02 USD | `1,624.23` | `1256.96` | `1273.10` | `2126.89` | -27,673.09 USD | `-1.34%` | `10X Cross` |
| `1056` | `0x7f75...9edf` | `LONG` | 2,052,300.58 USD | `1,611.67` | `1200.24` | `1273.10` | `983.18` | 117,916.60 USD | `+5.75%` | `10X Cross` |
| `1068` | `0x6646...6de5` | `SHORT` | 2,038,400.00 USD | `1,600.00` | `660.64` | `1273.10` | `4318.57` | -981,375.03 USD | `-48.14%` | `10X Cross` |
| `1071` | `0x023a...2355` | `SHORT` | 2,032,859.54 USD | `1,594.90` | `1310.00` | `1273.10` | `4426.11` | 56,452.60 USD | `+2.78%` | `10X Cross` |
| `1088` | `0xfc27...9d9d` | `SHORT` | 1,998,602.13 USD | `1,567.90` | `1296.11` | `1273.10` | `12299.18` | 33,572.15 USD | `+1.68%` | `10X Cross` |
| `1093` | `0xab59...59b5` | `LONG` | 1,995,313.40 USD | `1,565.32` | `1342.15` | `1273.10` | `826.25` | -105,581.81 USD | `-5.29%` | `10X Cross` |
| `1141` | `0x039c...0ebd` | `SHORT` | 1,937,477.43 USD | `1,521.38` | `1245.17` | `1273.10` | `3213.41` | -43,096.06 USD | `-2.22%` | `10X Cross` |
| `1158` | `0xcf67...eb24` | `LONG` | 1,911,900.00 USD | `1,500.00` | `887.05` | `1273.10` | `622.21` | 581,328.63 USD | `+30.41%` | `10X Cross` |
| `1168` | `0xb695...a92d` | `LONG` | 1,890,380.10 USD | `1,483.00` | `1249.80` | `1273.10` | `0.000000` | 36,921.25 USD | `+1.95%` | `10X Cross` |
| `1172` | `0x7277...0b98` | `SHORT` | 1,881,555.75 USD | `1,475.73` | `1287.86` | `1273.10` | `2157.93` | 18,976.37 USD | `+1.01%` | `10X Cross` |
| `1240` | `0x2ab7...c2f8` | `LONG` | 1,783,829.59 USD | `1,400.51` | `813.26` | `1273.10` | `789.80` | 644,847.90 USD | `+36.15%` | `3X Cross` |
| `1255` | `0xe35c...a1d3` | `LONG` | 1,770,484.42 USD | `1,389.16` | `1311.66` | `1273.10` | `690.81` | -51,618.29 USD | `-2.92%` | `2X Isolated` |
| `1262` | `0x11be...8b1d` | `LONG` | 1,753,770.50 USD | `1,375.83` | `1206.55` | `1273.10` | `1134.61` | 93,762.54 USD | `+5.35%` | `10X Isolated` |
| `1336` | `0xe065...0f85` | `SHORT` | 1,609,322.71 USD | `1,262.61` | `1087.02` | `1273.10` | `1575.09` | -236,846.58 USD | `-14.72%` | `10X Cross` |
| `1347` | `0x413c...886c` | `LONG` | 1,593,375.00 USD | `1,250.00` | `1237.51` | `1273.10` | `0.000000` | 46,485.54 USD | `+2.92%` | `10X Cross` |
| `1419` | `0x5975...9abd` | `LONG` | 1,529,640.00 USD | `1,200.00` | `1179.54` | `1273.10` | `469.44` | 114,197.21 USD | `+7.47%` | `5X Cross` |
| `1421` | `0x266b...efcb` | `LONG` | 1,528,800.00 USD | `1,200.00` | `893.76` | `1273.10` | `382.04` | 456,290.30 USD | `+29.85%` | `10X Cross` |
| `1438` | `0x2847...d47b` | `LONG` | 1,510,714.84 USD | `1,186.27` | `1232.07` | `1273.10` | `0.000000` | 49,146.35 USD | `+3.25%` | `5X Cross` |
| `1456` | `0x69cc...14fd` | `SHORT` | 1,480,501.73 USD | `1,161.36` | `675.33` | `1273.10` | `7940.88` | -696,196.20 USD | `-47.02%` | `10X Cross` |
| `1470` | `0x3fc5...c0c1` | `SHORT` | 1,463,916.47 USD | `1,148.44` | `1264.34` | `1273.10` | `2637.53` | -11,902.69 USD | `-0.81%` | `10X Cross` |
| `1488` | `0x38f9...cb04` | `SHORT` | 1,447,974.37 USD | `1,135.31` | `1252.77` | `1273.10` | `1999.20` | -25,691.80 USD | `-1.77%` | `10X Cross` |
| `1511` | `0x5f94...4b96` | `LONG` | 1,421,523.14 USD | `1,115.27` | `538.00` | `1273.10` | `0.000000` | 821,505.51 USD | `+57.79%` | `10X Cross` |
| `1527` | `0x9e7e...0047` | `LONG` | 1,403,145.54 USD | `1,100.42` | `1283.06` | `1273.10` | `1193.14` | -8,760.19 USD | `-0.62%` | `10X Cross` |
| `1530` | `0x71df...a23d` | `SHORT` | 1,400,746.31 USD | `1,098.28` | `513.50` | `1273.10` | `2559.85` | -836,776.12 USD | `-59.74%` | `2X Cross` |
| `1564` | `0xbfc7...80b4` | `SHORT` | 1,369,012.50 USD | `1,075.00` | `558.03` | `1273.10` | `2624.48` | -769,133.77 USD | `-56.18%` | `10X Cross` |
| `1590` | `0xdf83...3cff` | `SHORT` | 1,335,844.53 USD | `1,048.05` | `1260.93` | `1273.10` | `1905.87` | -14,328.12 USD | `-1.07%` | `10X Cross` |
| `1638` | `0x123d...3bff` | `SHORT` | 1,287,879.28 USD | `1,011.45` | `494.46` | `1273.10` | `4322.15` | -787,759.18 USD | `-61.17%` | `10X Cross` |
| `1649` | `0x668c...ea2e` | `SHORT` | 1,275,200.00 USD | `1,000.00` | `1406.98` | `1273.10` | `4210.96` | 131,781.99 USD | `+10.33%` | `10X Cross` |
| `1652` | `0xe282...df29` | `LONG` | 1,274,500.00 USD | `1,000.00` | `420.99` | `1273.10` | `791.31` | 853,513.14 USD | `+66.97%` | `10X Cross` |
| `1672` | `0x17f0...094f` | `LONG` | 1,253,506.05 USD | `984.30` | `1287.23` | `1273.10` | `536.96` | -13,514.11 USD | `-1.08%` | `5X Cross` |
| `1687` | `0x51f6...2b39` | `SHORT` | 1,240,624.59 USD | `972.81` | `1299.77` | `1273.10` | `2533.97` | 23,803.11 USD | `+1.92%` | `10X Cross` |
| `1746` | `0x757d...94ba` | `LONG` | 1,179,375.00 USD | `925.00` | `1558.31` | `1273.10` | `0.000000` | -262,065.58 USD | `-22.22%` | `10X Cross` |
| `1750` | `0xaa82...9556` | `LONG` | 1,178,265.75 USD | `924.13` | `1254.72` | `1273.10` | `179.49` | 18,739.07 USD | `+1.59%` | `10X Cross` |
| `1787` | `0xb911...5525` | `LONG` | 1,147,230.00 USD | `900.00` | `1294.82` | `1273.10` | `1035.40` | -18,107.82 USD | `-1.58%` | `10X Cross` |
| `1810` | `0xef96...9383` | `SHORT` | 1,131,551.64 USD | `887.77` | `1259.32` | `1273.10` | `5186.69` | -13,564.77 USD | `-1.20%` | `10X Cross` |
| `1842` | `0xcf0a...856f` | `LONG` | 1,110,542.02 USD | `871.15` | `1292.19` | `1273.10` | `1011.50` | -15,152.83 USD | `-1.36%` | `4X Cross` |
| `1866` | `0xdf95...7d72` | `SHORT` | 1,086,639.34 USD | `853.27` | `1074.39` | `1273.10` | `44092.50` | -169,891.90 USD | `-15.63%` | `10X Cross` |
| `1898` | `0x601c...4f54` | `SHORT` | 1,051,630.15 USD | `824.42` | `615.11` | `1273.10` | `3073.81` | -544,517.40 USD | `-51.78%` | `5X Cross` |
| `1914` | `0xae55...2236` | `LONG` | 1,042,519.49 USD | `817.47` | `1467.80` | `1273.10` | `0.000000` | -157,361.73 USD | `-15.09%` | `10X Cross` |
| `1958` | `0x0f02...5384` | `LONG` | 1,020,834.34 USD | `800.78` | `1290.36` | `1273.10` | `296.63` | -12,459.73 USD | `-1.22%` | `3X Cross` |
| `1963` | `0x9b0f...db40` | `LONG` | 1,018,956.56 USD | `800.00` | `1268.86` | `1273.10` | `792.21` | 3,866.80 USD | `+0.38%` | `10X Cross` |
| `1964` | `0x11ee...1d1d` | `SHORT` | 1,018,720.00 USD | `800.00` | `1269.65` | `1273.10` | `1592.66` | -2,996.99 USD | `-0.29%` | `5X Cross` |
| `1982` | `0x6e8f...4364` | `LONG` | 1,011,506.93 USD | `793.65` | `1260.00` | `1273.10` | `939.05` | 11,507.92 USD | `+1.14%` | `10X Cross` |
| `1985` | `0xabdb...84ac` | `LONG` | 1,010,764.21 USD | `793.69` | `711.79` | `1273.10` | `664.53` | 445,823.85 USD | `+44.11%` | `3X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
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
| `5m` | `BALANCED` | 0.00 USD | 1,750.00 USD | 1,750.00 USD | 1,750.00 USD | `1` | `2026-10-30 06:10:00 UTC - 2026-10-30 06:15:00 UTC` |
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
  * Current Rate: `79.54K` | Last 24h: `134.73K` | Last 3d: `246.48K` | Last 7d: `772.71K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0089%` | **USDT OKX** | `0.0100%` |
| **USDT Bybit** | `0.0100%` | **USDT KuCoin** | `0.0100%` |
| **USDT MEXC** | `0.0089%` | **USDT BingX** | `0.0100%` |
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
| `0:00 UTC` | `1270.95` | `1269.16` | `1270.95` | `1274.25` | `1263.15` | 7,981,868.45 USD | 3,939,177.59 USD | 4,042,690.86 USD | -103,513.28 USD | `-1.30%` | `2B / 5S` |

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
| `5m` | 40,530.00 USD | 555,940.00 USD | **`ACCUMULATION`** |
| `15m` | -197,200.00 USD | -532,600.00 USD | **`DISTRIBUTION`** |
| `30m` | 212,140.00 USD | -5,740,000.00 USD | **`DISTRIBUTION`** |
| `1h` | -277,090.00 USD | -7,700,000.00 USD | **`DISTRIBUTION`** |
| `2h` | -798,710.00 USD | -16,560,000.00 USD | **`DISTRIBUTION`** |
| `4h` | 2,580,000.00 USD | -10,540,000.00 USD | **`DISTRIBUTION`** |
| `6h` | 1,760,000.00 USD | 9,670,000.00 USD | **`ACCUMULATION`** |
| `8h` | -939,410.00 USD | 9,770,000.00 USD | **`ACCUMULATION`** |
| `12h` | -12,290,000.00 USD | -16,030,000.00 USD | **`DISTRIBUTION`** |
| `24h` | 15,770,000.00 USD | 94,040,000.00 USD | **`ACCUMULATION`** |
| `1w` | 34,940,000.00 USD | 214,860,000.00 USD | **`ACCUMULATION`** |
| `30d` | 61,080,000.00 USD | -523,920,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+40.53K` | 15m=`-197.20K` | 1h=`-277.09K` | 24h=`+15.77M`
* Futures Capital Netflows: 5m=`+555.94K` | 15m=`-532.60K` | 1h=`-7.70M` | 24h=`+94.04M`
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
  * `2026-10-30 11:03:46 IST`: [kitco.com] - (Sentiment: `Neutral`)
  * `2026-10-30 11:38:46 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 11:37:46 IST`: [forex.com] - (Sentiment: `Neutral`)
  * `2026-10-30 08:39:46 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 08:39:46 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 08:39:46 IST`: [financemagnates.com] - (Sentiment: `Neutral`)
  * `2026-10-30 07:39:46 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-30 06:39:46 IST`: [kathleenhays.substack.com] - (Sentiment: `Neutral`)
  * `2026-10-30 06:39:46 IST`: [rba.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 06:39:46 IST`: [abs.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 06:39:46 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 05:39:46 IST`: [@NodeWire] - (Sentiment: `Neutral`)
  * `2026-10-30 05:39:46 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 05:39:46 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 05:39:46 IST`: [@financialjuice] - (Sentiment: `Neutral`)


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
  * Spread-Padded Stop Loss: `1214.94` (Risk Distance: `20.37` pts)
  * +2.5R Take Profit: `1286.23`
  * Mathematical Lot Sizing: **`0.49 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `1285.56` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `1305.93` (Risk Distance: `20.37` pts)
  * +2.5R Take Profit: `1234.64`
  * Mathematical Lot Sizing: **`0.49 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`1283.17`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
