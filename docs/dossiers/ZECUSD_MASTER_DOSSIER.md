# 🏛️ SOVEREIGN CANDIDATE DOSSIER: ZECUSD
**Canonical Key**: `ZECUSD` | **Broker Instrument**: `ZECUSD.p` | **Asset Class**: `Crypto Altcoin`
**Timestamp**: `2026-10-30 04:50:10 IST` (`2026-10-29 23:20:10 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `1238.53` | **Live Ask Quote**: `1240.19` | **Mid Price**: `1239.36`
- **Spread Points**: `166.00` | **Spread BPS**: `13.39 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `1278.94` | VWAP Z-Score: `-1.02` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `21.73` (Volatility Regime: `HIGH_EXPANSION`)
  * 14-Period RSI: `32.96` (State: `OVERSOLD`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `1391.26` | Lower -3.00σ Band: `1166.63`
  * Upper +2.51σ Band: `1372.91` | Lower -2.51σ Band: `1184.97`
  * Upper +2.01σ Band: `1354.19` | Lower -2.01σ Band: `1203.69`
  * Upper +2.00σ Band: `1353.82` | Lower -2.00σ Band: `1204.07`
  * Upper +1.28σ Band: `1326.86` | Lower -1.28σ Band: `1231.02`
  * Upper +1.00σ Band: `1316.38` | Lower -1.00σ Band: `1241.50`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`1256.09` | EMA-20=`1274.50` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`1285.63` (Slope: `+0.0000`) | EMA-100=`1284.40`
  * Institutional Anchors: EMA-144=`1281.95` | EMA-200=`1279.20` (Slope: `-0.2219`) | EMA-233=`1279.28`
- **Range Boundaries**: 24H High=`1396.49` | 24H Low=`1206.89` | Weekly High=`1396.49` | Weekly Low=`1206.89`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `1272.04` (Distance: `-2.38%`)
  * Point of Control (POC) = `1252.78` (Distance: `-0.88%`)
  * Value Area Low (VAL) = `1240.92` (Distance: `+0.06%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`1309.91` | POC=`1246.71` | VAL=`1230.27`
  * Prior Day Extremes: PDH=`1396.49` | PDL=`1206.89` | PDC=`1244.38`
  * Monday Range Blueprint: High=`1267.53` | Mid=`1222.14` | Low=`1176.75`
  * Developing Weekly Value Area: Weekly VAH=`1297.61` | Weekly POC=`1239.01` | Weekly VAL=`1199.46`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`1296.00` | Low=`1221.90`
  * London Session (08:00-16:00 UTC): High=`1244.32` | Low=`1234.40`
  * New York Session (13:00-21:00 UTC): High=`1246.80` | Low=`1231.92`
  * Initial Balance (First Hour): IB High=`1243.08` | IB Low=`1235.64`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `1234.40` - `1244.32`
  * Optimal Trade Entry (OTE 0.705): `1241.84`
  * Structural Invalidation Anchor (0.786): `1249.27`

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
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 04:46:31 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `16` | `0xb83d...6e36` | `SHORT` | 65,052,276.65 USD | `52,385.47` | `1336.45` | `1240.40` | `4027.67` | 4,958,290.75 USD | `+7.62%` | `3X Cross` |
| `23` | `0x5b5d...c060` | `SHORT` | 49,878,899.62 USD | `40,121.38` | `1478.36` | `1240.40` | `5504.39` | 9,435,135.50 USD | `+18.92%` | `3X Cross` |
| `42` | `0x7fda...17d1` | `SHORT` | 28,570,621.81 USD | `22,981.65` | `1262.36` | `1240.40` | `2803.55` | 440,526.93 USD | `+1.54%` | `5X Cross` |
| `88` | `0x60b0...991e` | `LONG` | 20,736,402.69 USD | `16,779.74` | `1179.65` | `1240.40` | `933.86` | 942,155.68 USD | `+4.54%` | `10X Cross` |
| `143` | `0xc36a...105b` | `LONG` | 14,219,315.95 USD | `11,510.82` | `1215.14` | `1240.40` | `964.23` | 232,034.92 USD | `+1.63%` | `10X Cross` |
| `160` | `0x9071...5c0b` | `LONG` | 13,058,267.26 USD | `10,517.29` | `1353.83` | `1240.40` | `0.0327` | -1,180,351.61 USD | `-9.04%` | `1X Cross` |
| `183` | `0x8742...8427` | `LONG` | 11,423,302.21 USD | `9,201.21` | `1286.37` | `1240.40` | `710.30` | -412,867.78 USD | `-3.61%` | `10X Cross` |
| `203` | `0x9ffd...ce40` | `LONG` | 10,621,055.42 USD | `8,543.32` | `1255.69` | `1240.40` | `616.98` | -106,674.49 USD | `-1.00%` | `5X Cross` |
| `205` | `0xad59...ba81` | `SHORT` | 10,445,315.00 USD | `8,425.00` | `330.91` | `1240.40` | `2146.67` | -7,657,357.23 USD | `-73.31%` | `10X Cross` |
| `213` | `0xdd53...2b13` | `SHORT` | 10,154,706.24 USD | `8,168.20` | `739.52` | `1240.40` | `8722.04` | -4,114,196.05 USD | `-40.52%` | `3X Cross` |
| `231` | `0x880a...311c` | `SHORT` | 9,552,192.13 USD | `7,707.11` | `1367.50` | `1240.40` | `2274.80` | 987,292.07 USD | `+10.34%` | `10X Cross` |
| `279` | `0x2b61...2f6c` | `LONG` | 8,438,637.90 USD | `6,807.00` | `1453.56` | `1240.40` | `531.82` | -1,455,713.32 USD | `-17.25%` | `10X Cross` |
| `295` | `0x2ae5...83e7` | `LONG` | 7,991,930.88 USD | `6,436.80` | `1391.82` | `1240.40` | `0.000000` | -966,961.11 USD | `-12.10%` | `1X Cross` |
| `342` | `0x26b6...9a13` | `LONG` | 6,746,519.17 USD | `5,433.73` | `1282.23` | `1240.40` | `218.65` | -220,784.07 USD | `-3.27%` | `10X Cross` |
| `357` | `0x45d2...4029` | `SHORT` | 6,489,320.50 USD | `5,227.00` | `833.44` | `1240.40` | `9082.04` | -2,132,942.53 USD | `-32.87%` | `5X Cross` |
| `379` | `0xea00...a918` | `LONG` | 6,196,000.00 USD | `5,000.00` | `739.16` | `1240.40` | `0.000000` | 2,500,184.89 USD | `+40.35%` | `5X Cross` |
| `381` | `0x58b2...11f3` | `LONG` | 6,164,641.67 USD | `4,963.08` | `1257.17` | `1240.40` | `0.000000` | -74,769.52 USD | `-1.21%` | `10X Cross` |
| `386` | `0xdd7a...8830` | `LONG` | 6,035,383.94 USD | `4,860.19` | `897.48` | `1240.40` | `787.51` | 1,673,480.27 USD | `+27.73%` | `10X Cross` |
| `425` | `0xecb6...2b00` | `SHORT` | 5,185,854.45 USD | `4,171.40` | `1303.80` | `1240.40` | `7914.91` | 252,805.93 USD | `+4.87%` | `5X Cross` |
| `452` | `0xa61c...66b9` | `LONG` | 4,826,952.00 USD | `3,888.00` | `1148.34` | `1240.40` | `0.000000` | 362,209.86 USD | `+7.50%` | `10X Cross` |
| `472` | `0x9aa5...58af` | `SHORT` | 4,620,997.05 USD | `3,720.31` | `1205.51` | `1240.40` | `3665.01` | -136,110.25 USD | `-2.95%` | `10X Cross` |
| `476` | `0x0153...8052` | `SHORT` | 4,595,358.47 USD | `3,698.18` | `1307.82` | `1240.40` | `2504.75` | 241,212.28 USD | `+5.25%` | `1X Isolated` |
| `550` | `0xd21d...90f1` | `LONG` | 4,027,400.00 USD | `3,250.00` | `1253.64` | `1240.40` | `875.95` | -46,941.73 USD | `-1.17%` | `4X Isolated` |
| `571` | `0x4cae...7c34` | `LONG` | 3,919,899.96 USD | `3,162.74` | `1011.50` | `1240.40` | `920.19` | 720,788.06 USD | `+18.39%` | `10X Cross` |
| `576` | `0x1338...c48e` | `LONG` | 3,903,088.60 USD | `3,149.43` | `1018.52` | `1240.40` | `820.24` | 695,343.06 USD | `+17.82%` | `4X Isolated` |
| `580` | `0x456f...cdf1` | `LONG` | 3,873,133.14 USD | `3,134.11` | `1268.47` | `1240.40` | `493.80` | -102,376.33 USD | `-2.64%` | `10X Cross` |
| `588` | `0x382b...3e39` | `LONG` | 3,834,401.76 USD | `3,084.30` | `1211.32` | `1240.40` | `0.000000` | 98,318.42 USD | `+2.56%` | `10X Cross` |
| `591` | `0xdbe0...d6d5` | `LONG` | 3,829,252.71 USD | `3,085.37` | `422.97` | `1240.40` | `338.56` | 2,524,248.21 USD | `+65.92%` | `3X Isolated` |
| `596` | `0x27c9...d65d` | `SHORT` | 3,765,161.02 USD | `3,036.91` | `1254.41` | `1240.40` | `1777.03` | 44,372.65 USD | `+1.18%` | `10X Cross` |
| `602` | `0x325e...9564` | `LONG` | 3,727,771.84 USD | `3,001.91` | `1301.41` | `1240.40` | `179.39` | -178,937.37 USD | `-4.80%` | `10X Cross` |
| `607` | `0x9c06...0560` | `SHORT` | 3,716,897.83 USD | `2,989.80` | `786.00` | `1240.40` | `2545.31` | -1,366,902.83 USD | `-36.78%` | `10X Cross` |
| `609` | `0xd4c1...3d1d` | `SHORT` | 3,708,518.71 USD | `2,983.06` | `1299.23` | `1240.40` | `2931.89` | 167,158.37 USD | `+4.51%` | `10X Cross` |
| `621` | `0x2e30...4cb5` | `SHORT` | 3,658,672.38 USD | `2,946.74` | `1297.52` | `1240.40` | `2885.44` | 164,781.81 USD | `+4.50%` | `2X Cross` |
| `718` | `0xac48...3201` | `LONG` | 3,147,160.80 USD | `2,531.50` | `1378.58` | `1240.40` | `555.30` | -342,711.48 USD | `-10.89%` | `10X Cross` |
| `720` | `0xa183...0482` | `LONG` | 3,145,454.20 USD | `2,534.00` | `530.25` | `1240.40` | `444.48` | 1,801,791.48 USD | `+57.28%` | `5X Isolated` |
| `739` | `0x0871...e927` | `LONG` | 3,099,250.00 USD | `2,500.00` | `1276.50` | `1240.40` | `0.000000` | -92,000.00 USD | `-2.97%` | `10X Cross` |
| `748` | `0x9b86...6e6e` | `LONG` | 3,053,999.34 USD | `2,463.30` | `637.58` | `1240.40` | `882.41` | 1,483,450.06 USD | `+48.57%` | `3X Cross` |
| `798` | `0xb2f7...af9f` | `SHORT` | 2,868,550.06 USD | `2,313.72` | `746.63` | `1240.40` | `4394.39` | -1,141,061.31 USD | `-39.78%` | `10X Cross` |
| `825` | `0xf48f...10fe` | `LONG` | 2,754,920.88 USD | `2,218.49` | `1517.87` | `1240.40` | `980.39` | -612,465.94 USD | `-22.23%` | `3X Cross` |
| `860` | `0x5bc4...3b0c` | `SHORT` | 2,645,526.78 USD | `2,130.74` | `1089.65` | `1240.40` | `3684.87` | -323,769.21 USD | `-12.24%` | `5X Cross` |
| `875` | `0x8de4...b9aa` | `SHORT` | 2,599,891.73 USD | `2,091.29` | `1331.35` | `1240.40` | `1689.87` | 184,347.98 USD | `+7.09%` | `3X Cross` |
| `885` | `0x4fe2...ac59` | `SHORT` | 2,568,125.33 USD | `2,071.57` | `1478.56` | `1240.40` | `1859.50` | 494,820.89 USD | `+19.27%` | `10X Cross` |
| `914` | `0x9a99...d21a` | `LONG` | 2,478,200.00 USD | `2,000.00` | `1278.44` | `1240.40` | `0.000000` | -78,673.67 USD | `-3.17%` | `10X Cross` |
| `940` | `0x77ee...2902` | `SHORT` | 2,412,493.39 USD | `1,946.03` | `759.84` | `1240.40` | `5292.69` | -933,815.88 USD | `-38.71%` | `10X Cross` |
| `948` | `0x3e2f...b269` | `SHORT` | 2,390,713.22 USD | `1,925.51` | `1134.87` | `1240.40` | `2931.80` | -205,514.36 USD | `-8.60%` | `10X Cross` |
| `954` | `0xe097...d0fe` | `LONG` | 2,374,919.32 USD | `1,913.56` | `1261.17` | `1240.40` | `0.000000` | -38,406.85 USD | `-1.62%` | `10X Cross` |
| `967` | `0x5323...b23c` | `LONG` | 2,358,922.27 USD | `1,897.46` | `1234.97` | `1240.40` | `0.000000` | 15,610.70 USD | `+0.66%` | `5X Cross` |
| `969` | `0x4f12...618b` | `SHORT` | 2,349,680.55 USD | `1,896.28` | `1608.30` | `1240.40` | `2116.76` | 700,103.84 USD | `+29.80%` | `3X Cross` |
| `1005` | `0x866d...d6e1` | `LONG` | 2,233,460.77 USD | `1,802.05` | `674.73` | `1240.40` | `249.36` | 1,017,559.46 USD | `+45.56%` | `10X Cross` |
| `1031` | `0x2309...a2d9` | `LONG` | 2,169,933.69 USD | `1,750.37` | `1186.09` | `1240.40` | `816.32` | 93,839.58 USD | `+4.32%` | `8X Cross` |
| `1052` | `0x2edd...8179` | `SHORT` | 2,113,016.96 USD | `1,701.85` | `1261.58` | `1240.40` | `3124.76` | 34,001.89 USD | `+1.61%` | `10X Cross` |
| `1054` | `0x023a...2355` | `SHORT` | 2,108,691.20 USD | `1,696.19` | `1313.00` | `1240.40` | `5209.29` | 118,406.63 USD | `+5.62%` | `10X Cross` |
| `1083` | `0xfe7c...b7ae` | `SHORT` | 2,038,273.68 USD | `1,640.99` | `1347.05` | `1240.40` | `7036.53` | 172,215.51 USD | `+8.45%` | `10X Cross` |
| `1087` | `0x3e47...aaf6` | `LONG` | 2,027,678.18 USD | `1,636.28` | `1278.38` | `1240.40` | `1053.18` | -64,113.61 USD | `-3.16%` | `10X Cross` |
| `1089` | `0xa271...a3f7` | `LONG` | 2,026,399.20 USD | `1,631.43` | `1190.60` | `1240.40` | `910.34` | 84,017.40 USD | `+4.15%` | `4X Cross` |
| `1112` | `0x7f75...9edf` | `LONG` | 1,996,294.13 USD | `1,605.78` | `1199.97` | `1240.40` | `978.28` | 69,402.24 USD | `+3.48%` | `10X Cross` |
| `1118` | `0x265e...7f70` | `LONG` | 1,991,283.17 USD | `1,601.74` | `1388.09` | `1240.40` | `0.000000` | -232,081.84 USD | `-11.65%` | `3X Cross` |
| `1124` | `0x6646...6de5` | `SHORT` | 1,985,760.00 USD | `1,600.00` | `660.64` | `1240.40` | `4454.20` | -928,735.03 USD | `-46.77%` | `10X Cross` |
| `1144` | `0xdf57...93f5` | `LONG` | 1,958,270.50 USD | `1,579.76` | `1218.38` | `1240.40` | `780.18` | 33,514.52 USD | `+1.71%` | `3X Isolated` |
| `1155` | `0xab59...59b5` | `LONG` | 1,940,683.74 USD | `1,565.32` | `1342.15` | `1240.40` | `836.82` | -160,211.48 USD | `-8.26%` | `10X Cross` |
| `1202` | `0xcf67...eb24` | `LONG` | 1,859,550.00 USD | `1,500.00` | `887.05` | `1240.40` | `689.14` | 528,978.63 USD | `+28.45%` | `10X Cross` |
| `1211` | `0xb695...a92d` | `LONG` | 1,841,144.50 USD | `1,483.00` | `1249.80` | `1240.40` | `0.000000` | -12,314.35 USD | `-0.67%` | `10X Cross` |
| `1280` | `0x2ab7...c2f8` | `LONG` | 1,738,873.22 USD | `1,400.51` | `813.26` | `1240.40` | `793.34` | 599,891.53 USD | `+34.50%` | `3X Cross` |
| `1297` | `0x11be...8b1d` | `LONG` | 1,705,754.03 USD | `1,375.83` | `1206.55` | `1240.40` | `1134.46` | 45,746.08 USD | `+2.68%` | `10X Isolated` |
| `1408` | `0xe065...0f85` | `SHORT` | 1,565,257.62 USD | `1,262.61` | `1087.02` | `1240.40` | `1833.40` | -192,781.49 USD | `-12.32%` | `10X Cross` |
| `1415` | `0x039c...0ebd` | `SHORT` | 1,550,807.05 USD | `1,250.55` | `1239.86` | `1240.40` | `3659.46` | -295.77 USD | `-0.02%` | `10X Cross` |
| `1445` | `0x7277...0b98` | `SHORT` | 1,532,214.87 USD | `1,234.96` | `1298.48` | `1240.40` | `2426.68` | 71,354.55 USD | `+4.66%` | `10X Cross` |
| `1472` | `0x266b...efcb` | `LONG` | 1,489,320.00 USD | `1,200.00` | `893.76` | `1240.40` | `422.43` | 416,810.30 USD | `+27.99%` | `10X Cross` |
| `1475` | `0x5975...9abd` | `LONG` | 1,487,760.00 USD | `1,200.00` | `1179.54` | `1240.40` | `594.73` | 72,317.21 USD | `+4.86%` | `5X Cross` |
| `1511` | `0x69cc...14fd` | `SHORT` | 1,442,409.12 USD | `1,161.36` | `675.33` | `1240.40` | `8174.80` | -658,103.59 USD | `-45.63%` | `10X Cross` |
| `1531` | `0x3fc5...c0c1` | `SHORT` | 1,419,242.15 USD | `1,148.44` | `1264.34` | `1240.40` | `3143.69` | 32,771.62 USD | `+2.31%` | `10X Cross` |
| `1535` | `0x2847...d47b` | `LONG` | 1,418,739.04 USD | `1,142.21` | `1233.90` | `1240.40` | `0.000000` | 9,366.71 USD | `+0.66%` | `5X Cross` |
| `1561` | `0xe35c...a1d3` | `LONG` | 1,399,244.99 USD | `1,127.06` | `1318.20` | `1240.40` | `694.38` | -86,450.36 USD | `-6.18%` | `2X Isolated` |
| `1574` | `0x51f6...2b39` | `SHORT` | 1,387,063.10 USD | `1,115.72` | `1299.77` | `1240.40` | `2649.82` | 63,114.50 USD | `+4.55%` | `10X Cross` |
| `1576` | `0x5f94...4b96` | `LONG` | 1,384,942.29 USD | `1,115.27` | `538.00` | `1240.40` | `0.000000` | 784,924.65 USD | `+56.68%` | `10X Cross` |
| `1586` | `0xfc27...9d9d` | `SHORT` | 1,365,742.22 USD | `1,098.57` | `1315.05` | `1240.40` | `16739.85` | 78,935.50 USD | `+5.78%` | `10X Cross` |
| `1594` | `0x71df...a23d` | `SHORT` | 1,361,208.23 USD | `1,098.28` | `513.50` | `1240.40` | `2552.83` | -797,238.04 USD | `-58.57%` | `2X Cross` |
| `1611` | `0xef96...9383` | `SHORT` | 1,340,027.16 USD | `1,078.84` | `1259.08` | `1240.40` | `5160.59` | 18,320.61 USD | `+1.37%` | `10X Cross` |
| `1614` | `0xbfc7...80b4` | `SHORT` | 1,332,677.50 USD | `1,075.00` | `558.03` | `1240.40` | `4685.83` | -732,798.77 USD | `-54.99%` | `10X Cross` |
| `1665` | `0x71d0...8c26` | `SHORT` | 1,272,589.25 USD | `1,023.64` | `1289.25` | `1240.40` | `6330.33` | 47,141.68 USD | `+3.70%` | `10X Cross` |
| `1689` | `0x123d...3bff` | `SHORT` | 1,250,177.13 USD | `1,008.37` | `490.16` | `1240.40` | `4582.82` | -755,916.91 USD | `-60.46%` | `10X Cross` |
| `1700` | `0xe282...df29` | `LONG` | 1,241,800.00 USD | `1,000.00` | `420.99` | `1240.40` | `212.59` | 820,813.14 USD | `+66.10%` | `10X Cross` |
| `1702` | `0x668c...ea2e` | `SHORT` | 1,241,546.10 USD | `1,000.00` | `1406.98` | `1240.40` | `4181.31` | 165,435.89 USD | `+13.32%` | `10X Cross` |
| `1723` | `0xdf83...3cff` | `SHORT` | 1,228,712.19 USD | `989.62` | `1255.39` | `1240.40` | `1776.73` | 13,642.39 USD | `+1.11%` | `10X Cross` |
| `1731` | `0x17f0...094f` | `LONG` | 1,219,941.42 USD | `984.30` | `1287.23` | `1240.40` | `536.81` | -47,078.74 USD | `-3.86%` | `5X Cross` |
| `1799` | `0x757d...94ba` | `LONG` | 1,148,572.50 USD | `925.00` | `1558.31` | `1240.40` | `0.000000` | -292,868.09 USD | `-25.50%` | `10X Cross` |
| `1837` | `0xb911...5525` | `LONG` | 1,117,980.00 USD | `900.00` | `1294.82` | `1240.40` | `1070.33` | -47,357.82 USD | `-4.24%` | `10X Cross` |
| `1886` | `0xcf0a...856f` | `LONG` | 1,079,790.43 USD | `871.15` | `1292.19` | `1240.40` | `1008.89` | -45,904.42 USD | `-4.25%` | `4X Cross` |
| `1898` | `0xdf95...7d72` | `SHORT` | 1,065,615.14 USD | `857.16` | `1074.39` | `1240.40` | `46035.62` | -144,688.31 USD | `-13.58%` | `10X Cross` |
| `1957` | `0x601c...4f54` | `SHORT` | 1,021,703.71 USD | `824.42` | `615.11` | `1240.40` | `3134.94` | -514,590.95 USD | `-50.37%` | `5X Cross` |
| `1972` | `0xae55...2236` | `LONG` | 1,014,889.01 USD | `817.47` | `1467.80` | `1240.40` | `0.000000` | -184,992.21 USD | `-18.23%` | `10X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `1121.60` | 594.45 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 0.59K USD at 1121.6000 USD [API] | `2026-10-24 14:16:53` |
| `ANNOUNCEMENT` | `INFO` | `1121.60` | 179.46 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 0.18K USD at 1121.6000 USD [API] | `2026-10-24 14:16:53` |
| `ANNOUNCEMENT` | `INFO` | `1122.30` | 2,020.14 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 2.02K USD at 1122.3000 USD [API] | `2026-10-24 14:16:53` |
| `ANNOUNCEMENT` | `INFO` | `1131.50` | 2,036.70 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 2.04K USD at 1131.5000 USD [API] | `2026-10-24 14:16:43` |
| `ANNOUNCEMENT` | `INFO` | `1132.20` | 2,037.96 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 2.04K USD at 1132.2000 USD [API] | `2026-10-24 14:16:43` |
| `ANNOUNCEMENT` | `INFO` | `1133.60` | 2,040.48 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 2.04K USD at 1133.6000 USD [API] | `2026-10-24 14:16:30` |
| `ANNOUNCEMENT` | `INFO` | `1135.80` | 545.18 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 0.55K USD at 1135.8000 USD [API] | `2026-10-24 14:16:14` |
| `ANNOUNCEMENT` | `INFO` | `1297.50` | 1,699.73 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Long: 1.70K USD at 1297.5000 USD [API] | `2026-10-28 19:57:32` |
| `ANNOUNCEMENT` | `INFO` | `1297.70` | 7,708.34 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Long: 7.71K USD at 1297.7000 USD [API] | `2026-10-28 19:57:32` |
| `ANNOUNCEMENT` | `INFO` | `1297.60` | 2,141.04 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Long: 2.14K USD at 1297.6000 USD [API] | `2026-10-28 19:57:32` |
| `ANNOUNCEMENT` | `INFO` | `1297.60` | 2,141.04 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Long: 2.14K USD at 1297.6000 USD [API] | `2026-10-28 19:57:32` |
| `ANNOUNCEMENT` | `INFO` | `1297.60` | 2,141.04 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Long: 2.14K USD at 1297.6000 USD [API] | `2026-10-28 19:57:32` |
| `ANNOUNCEMENT` | `INFO` | `1297.60` | 13,650.75 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Long: 13.65K USD at 1297.6000 USD [API] | `2026-10-28 19:57:32` |
| `ANNOUNCEMENT` | `INFO` | `1297.50` | 2,140.88 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Long: 2.14K USD at 1297.5000 USD [API] | `2026-10-28 19:57:32` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`1403.54` (Vol: 3,000,000.00 USD, Dist: `+12.15%`) | Long MP=`1223.03` (Vol: 1,200,000.00 USD, Dist: `--2.28%`)
  * 48H Horizon: Short MP=`1403.54` (Vol: 3,000,000.00 USD, Dist: `+12.15%`) | Long MP=`1223.03` (Vol: 1,200,000.00 USD, Dist: `--2.28%`)
  * 3D Horizon: Short MP=`1403.54` (Vol: 3,000,000.00 USD, Dist: `+12.15%`) | Long MP=`1200.05` (Vol: 1,600,000.00 USD, Dist: `--4.11%`)
  * 7D Horizon: Short MP=`1404.10` (Vol: 3,000,000.00 USD, Dist: `+12.19%`) | Long MP=`1200.46` (Vol: 3,000,000.00 USD, Dist: `--4.08%`)
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
| `5m` | `BALANCED` | 0.00 USD | 1,750.00 USD | 1,750.00 USD | 1,750.00 USD | `1` | `2026-10-29 23:15:00 UTC - 2026-10-29 23:20:00 UTC` |
| `15m` | `BALANCED` | 0.00 USD | 1,750.00 USD | 1,750.00 USD | 1,750.00 USD | `1` | `2026-10-29 23:15:00 UTC - 2026-10-29 23:30:00 UTC` |
| `1h` | `BALANCED` | 0.00 USD | 1,750.00 USD | 1,750.00 USD | 1,750.00 USD | `1` | `2026-10-29 23:00:00 UTC - 2026-10-30 00:00:00 UTC` |
| `4h` | `BALANCED` | 0.00 USD | 1,750.00 USD | 1,750.00 USD | 1,750.00 USD | `1` | `2026-10-29 20:00:00 UTC - 2026-10-30 00:00:00 UTC` |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `0 USD` | Total OI Tokens: `-`
  * 1h OI Change: `0.00%` | 4h OI Change: `0.00%` | 24h OI Change: `0.00%`
  * Exchange Breakdown: Binance=`-` | Bybit=`-` | OKX=`-` | Hyperliquid=`-`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `17.82K` | Last 24h: `33.19K` | Last 3d: `283.86K` | Last 7d: `777.60K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `-0.0004%` | **USDT OKX** | `0.0028%` |
| **USDT Bybit** | `0.0100%` | **USDT KuCoin** | `-0.0032%` |
| **USDT MEXC** | `-0.0003%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `0.0073%` | **USDT Bitget** | `0.0100%` |
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
| `5:00 UTC` | `1229.25` | `1237.79` | `1229.25` | `1264.35` | `1206.75` | 149,162,484.89 USD | 77,012,548.38 USD | 72,149,936.51 USD | 4,862,611.87 USD | `+3.26%` | `9B / 11S` |
| `0:00 UTC` | `1249.95` | `1248.07` | `1249.95` | `1259.85` | `1233.15` | 61,152,789.32 USD | 32,267,997.87 USD | 28,884,791.45 USD | 3,383,206.41 USD | `+5.53%` | `6B / 4S` |
| `5:00 UTC` | `1273.95` | `1271.85` | `1273.95` | `1286.25` | `1253.25` | 67,607,862.35 USD | 37,234,359.13 USD | 30,373,503.22 USD | 6,860,855.91 USD | `+10.15%` | `6B / 2S` |
| `0:00 UTC` | `1294.65` | `1287.25` | `1294.65` | `1297.05` | `1269.15` | 47,983,765.84 USD | 24,978,907.15 USD | 23,004,858.69 USD | 1,974,048.46 USD | `+4.11%` | `4B / 9S` |
| `5:00 UTC` | `1264.05` | `1267.99` | `1264.05` | `1276.65` | `1260.75` | 31,349,361.20 USD | 15,100,777.24 USD | 16,248,583.96 USD | -1,147,806.72 USD | `-3.66%` | `0B / 1S` |
| `0:00 UTC` | `1261.05` | `1255.07` | `1261.05` | `1269.15` | `1241.25` | 60,510,539.13 USD | 31,467,084.85 USD | 29,043,454.28 USD | 2,423,630.57 USD | `+4.01%` | `3B / 5S` |
| `5:00 UTC` | `1259.85` | `1254.56` | `1259.85` | `1263.15` | `1242.15` | 22,141,749.31 USD | 11,943,317.16 USD | 10,198,432.15 USD | 1,744,885.01 USD | `+7.88%` | `3B / 3S` |
| `0:00 UTC` | `1257.15` | `1255.20` | `1257.15` | `1264.35` | `1245.45` | 28,871,970.63 USD | 12,578,804.66 USD | 16,293,165.97 USD | -3,714,361.32 USD | `-12.86%` | `7B / 2S` |
| `5:00 UTC` | `1241.25` | `1245.94` | `1241.25` | `1254.45` | `1236.15` | 26,347,049.74 USD | 11,469,285.37 USD | 14,877,764.37 USD | -3,408,478.99 USD | `-12.94%` | `1B / 6S` |
| `0:00 UTC` | `1224.15` | `1230.51` | `1224.15` | `1243.65` | `1222.05` | 36,854,164.51 USD | 16,245,634.04 USD | 20,608,530.47 USD | -4,362,896.43 USD | `-11.84%` | `1B / 6S` |

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
| `5m` | 1,280,000.00 USD | 3,120,000.00 USD | **`ACCUMULATION`** |
| `15m` | -536,460.00 USD | 1,240,000.00 USD | **`ACCUMULATION`** |
| `30m` | -1,110,000.00 USD | -3,090,000.00 USD | **`DISTRIBUTION`** |
| `1h` | -1,440,000.00 USD | -5,690,000.00 USD | **`DISTRIBUTION`** |
| `2h` | 6,460,000.00 USD | -2,730,000.00 USD | **`ACCUMULATION`** |
| `4h` | -13,840,000.00 USD | -10,790,000.00 USD | **`DISTRIBUTION`** |
| `6h` | -13,440,000.00 USD | -31,830,000.00 USD | **`DISTRIBUTION`** |
| `8h` | 5,360,000.00 USD | 74,430,000.00 USD | **`ACCUMULATION`** |
| `12h` | 20,310,000.00 USD | 84,950,000.00 USD | **`ACCUMULATION`** |
| `24h` | 172,690.00 USD | 58,590,000.00 USD | **`ACCUMULATION`** |
| `1w` | 35,140,000.00 USD | 236,830,000.00 USD | **`ACCUMULATION`** |
| `30d` | 56,930,000.00 USD | -544,900,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+1.28M` | 15m=`-536.46K` | 1h=`-1.44M` | 24h=`+172.69K`
* Futures Capital Netflows: 5m=`+3.12M` | 15m=`+1.24M` | 1h=`-5.69M` | 24h=`+58.59M`
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
  * `2026-10-30 04:15:34 IST`: [economics.td.com] - (Sentiment: `Neutral`)
  * `2026-10-30 04:41:34 IST`: [investinglive.com] - (Sentiment: `Neutral`)
  * `2026-10-30 04:41:34 IST`: [msn.com] - (Sentiment: `Neutral`)
  * `2026-10-30 04:40:34 IST`: [morningstar.com] - (Sentiment: `Neutral`)
  * `2026-10-30 01:42:34 IST`: [sec.gov] - (Sentiment: `Neutral`)
  * `2026-10-30 01:42:34 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 01:42:34 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 00:42:34 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:42:34 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:42:34 IST`: [@DeItaone] - (Sentiment: `Neutral`)
  * `2026-10-29 23:42:34 IST`: [@mb_ghalibaf] - (Sentiment: `Neutral`)
  * `2026-10-29 23:42:34 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-29 23:42:34 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-29 23:42:34 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:42:34 IST`: [fxstreet.com] - (Sentiment: `Neutral`)


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
  * Execution Entry: `1240.92` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `1212.36` (Risk Distance: `28.56` pts)
  * +2.5R Take Profit: `1312.33`
  * Mathematical Lot Sizing: **`0.35 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `1272.04` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `1300.60` (Risk Distance: `28.56` pts)
  * +2.5R Take Profit: `1200.63`
  * Mathematical Lot Sizing: **`0.35 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`1249.27`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
