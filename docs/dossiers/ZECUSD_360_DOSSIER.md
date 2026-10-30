# 🏛️ SOVEREIGN CANDIDATE DOSSIER: ZECUSD
**Canonical Key**: `ZECUSD` | **Broker Instrument**: `ZECUSD.p` | **Asset Class**: `Crypto Altcoin`
**Timestamp**: `2026-10-30 17:28:17 IST` (`2026-10-30 11:58:17 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `1245.36` | **Live Ask Quote**: `1246.29` | **Mid Price**: `1245.82`
- **Spread Points**: `93.00` | **Spread BPS**: `7.46 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `1254.69` | VWAP Z-Score: `-0.24` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `12.68` (Volatility Regime: `HIGH_EXPANSION`)
  * 14-Period RSI: `44.77` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `1313.97` | Lower -3.00σ Band: `1195.40`
  * Upper +2.51σ Band: `1304.29` | Lower -2.51σ Band: `1205.08`
  * Upper +2.01σ Band: `1294.41` | Lower -2.01σ Band: `1214.96`
  * Upper +2.00σ Band: `1294.21` | Lower -2.00σ Band: `1215.16`
  * Upper +1.28σ Band: `1279.98` | Lower -1.28σ Band: `1229.39`
  * Upper +1.00σ Band: `1274.45` | Lower -1.00σ Band: `1234.92`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`1259.09` | EMA-20=`1258.58` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`1261.75` (Slope: `+0.0000`) | EMA-100=`1267.21`
  * Institutional Anchors: EMA-144=`1270.72` | EMA-200=`1275.89` (Slope: `-0.1954`) | EMA-233=`1275.43`
- **Range Boundaries**: 24H High=`1396.49` | 24H Low=`1180.03` | Weekly High=`1396.49` | Weekly Low=`1180.03`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `1278.60` (Distance: `-2.52%`)
  * Point of Control (POC) = `1247.68` (Distance: `-0.10%`)
  * Value Area Low (VAL) = `1240.72` (Distance: `+0.46%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`1309.91` | POC=`1246.71` | VAL=`1230.27`
  * Prior Day Extremes: PDH=`1396.49` | PDL=`1206.89` | PDC=`1244.38`
  * Monday Range Blueprint: High=`1267.53` | Mid=`1222.14` | Low=`1176.75`
  * Developing Weekly Value Area: Weekly VAH=`1300.54` | Weekly POC=`1240.47` | Weekly VAL=`1214.11`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`1296.00` | Low=`1180.03`
  * London Session (08:00-16:00 UTC): High=`1283.82` | Low=`1239.95`
  * New York Session (13:00-21:00 UTC): High=`1276.27` | Low=`1245.29`
  * Initial Balance (First Hour): IB High=`1283.82` | IB Low=`1264.92`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `1240.84` - `1250.81`
  * Optimal Trade Entry (OTE 0.705): `1248.32`
  * Structural Invalidation Anchor (0.786): `1255.79`

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
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 17:23:48 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `12` | `0xb83d...6e36` | `SHORT` | 65,235,625.79 USD | `52,385.47` | `1336.45` | `1245.20` | `3219.12` | 4,774,941.61 USD | `+7.32%` | `3X Cross` |
| `21` | `0x5b5d...c060` | `SHORT` | 49,955,130.24 USD | `40,121.38` | `1478.36` | `1245.20` | `4851.91` | 9,358,904.87 USD | `+18.73%` | `3X Cross` |
| `36` | `0x7fda...17d1` | `SHORT` | 33,153,279.30 USD | `26,629.14` | `1262.58` | `1245.20` | `2404.17` | 468,056.36 USD | `+1.41%` | `5X Cross` |
| `81` | `0x60b0...991e` | `LONG` | 20,897,488.20 USD | `16,779.74` | `1179.65` | `1245.20` | `917.61` | 1,103,241.18 USD | `+5.28%` | `10X Cross` |
| `139` | `0xc36a...105b` | `LONG` | 14,330,970.90 USD | `11,510.82` | `1215.14` | `1245.20` | `965.24` | 343,689.87 USD | `+2.40%` | `10X Cross` |
| `176` | `0x8742...8427` | `LONG` | 11,457,489.31 USD | `9,201.21` | `1286.37` | `1245.20` | `718.14` | -378,680.68 USD | `-3.31%` | `10X Cross` |
| `193` | `0x58b2...11f3` | `LONG` | 10,661,034.60 USD | `8,563.08` | `1246.56` | `1245.20` | `386.94` | -13,382.97 USD | `-0.13%` | `10X Cross` |
| `195` | `0x9ffd...ce40` | `LONG` | 10,627,531.65 USD | `8,536.17` | `1252.42` | `1245.20` | `607.73` | -63,324.35 USD | `-0.60%` | `5X Cross` |
| `198` | `0xad59...ba81` | `SHORT` | 10,493,337.50 USD | `8,425.00` | `330.91` | `1245.20` | `2147.17` | -7,705,379.73 USD | `-73.43%` | `10X Cross` |
| `203` | `0xdd53...2b13` | `SHORT` | 10,207,198.77 USD | `8,195.92` | `741.54` | `1245.20` | `8444.09` | -4,129,602.40 USD | `-40.46%` | `3X Cross` |
| `231` | `0x880a...311c` | `SHORT` | 9,593,810.53 USD | `7,707.11` | `1367.50` | `1245.20` | `2230.78` | 945,673.67 USD | `+9.86%` | `10X Cross` |
| `238` | `0x9071...5c0b` | `LONG` | 9,365,039.88 USD | `7,517.29` | `1353.83` | `1245.20` | `170.75` | -812,090.09 USD | `-8.67%` | `2X Cross` |
| `240` | `0xbf73...5d58` | `LONG` | 9,338,250.00 USD | `7,500.00` | `1248.78` | `1245.20` | `132.54` | -27,595.62 USD | `-0.30%` | `10X Cross` |
| `278` | `0x2b61...2f6c` | `LONG` | 8,490,303.03 USD | `6,807.00` | `1453.56` | `1245.20` | `585.43` | -1,404,048.19 USD | `-16.54%` | `10X Cross` |
| `296` | `0x2ae5...83e7` | `LONG` | 8,018,965.44 USD | `6,436.80` | `1391.82` | `1245.20` | `0.000000` | -939,926.55 USD | `-11.72%` | `1X Cross` |
| `318` | `0xecb6...2b00` | `SHORT` | 7,480,971.68 USD | `6,008.33` | `1277.41` | `1245.20` | `6446.21` | 194,107.01 USD | `+2.59%` | `5X Cross` |
| `339` | `0x26b6...9a13` | `LONG` | 6,771,514.33 USD | `5,433.73` | `1282.23` | `1245.20` | `233.54` | -195,788.91 USD | `-2.89%` | `10X Cross` |
| `357` | `0x45d2...4029` | `SHORT` | 6,511,796.60 USD | `5,227.00` | `833.44` | `1245.20` | `9050.93` | -2,155,418.63 USD | `-33.10%` | `5X Cross` |
| `366` | `0xea00...a918` | `LONG` | 6,240,000.00 USD | `5,000.00` | `739.16` | `1245.20` | `0.000000` | 2,544,184.89 USD | `+40.77%` | `5X Cross` |
| `379` | `0xdd7a...8830` | `LONG` | 6,052,394.61 USD | `4,860.19` | `897.48` | `1245.20` | `797.15` | 1,690,490.93 USD | `+27.93%` | `10X Cross` |
| `426` | `0x4cae...7c34` | `LONG` | 5,186,185.23 USD | `4,152.27` | `1172.97` | `1245.20` | `992.70` | 315,691.68 USD | `+6.09%` | `10X Cross` |
| `427` | `0x469e...58a5` | `SHORT` | 5,183,582.40 USD | `4,163.52` | `1242.31` | `1245.20` | `1945.64` | -11,197.75 USD | `-0.22%` | `10X Cross` |
| `448` | `0xd4c1...3d1d` | `SHORT` | 4,894,998.59 USD | `3,931.41` | `1291.66` | `1245.20` | `2359.71` | 183,030.24 USD | `+3.74%` | `10X Cross` |
| `454` | `0xa61c...66b9` | `LONG` | 4,842,196.46 USD | `3,888.00` | `1148.34` | `1245.20` | `0.000000` | 377,454.32 USD | `+7.80%` | `10X Cross` |
| `476` | `0x9aa5...58af` | `SHORT` | 4,632,587.68 USD | `3,720.31` | `1205.51` | `1245.20` | `3646.51` | -147,700.88 USD | `-3.19%` | `10X Cross` |
| `478` | `0x0153...8052` | `SHORT` | 4,610,890.82 USD | `3,698.18` | `1307.82` | `1245.20` | `2504.97` | 225,679.92 USD | `+4.89%` | `1X Isolated` |
| `513` | `0xb122...e4ba` | `LONG` | 4,356,994.54 USD | `3,498.47` | `1265.25` | `1245.20` | `1036.56` | -69,456.99 USD | `-1.59%` | `10X Cross` |
| `546` | `0xd21d...90f1` | `LONG` | 4,047,875.00 USD | `3,250.00` | `1253.64` | `1245.20` | `876.19` | -26,466.73 USD | `-0.65%` | `4X Isolated` |
| `557` | `0x456f...cdf1` | `LONG` | 3,979,555.40 USD | `3,195.66` | `1267.53` | `1245.20` | `508.48` | -71,040.41 USD | `-1.79%` | `10X Cross` |
| `567` | `0x1338...c48e` | `LONG` | 3,934,582.90 USD | `3,149.43` | `1018.52` | `1245.20` | `820.49` | 726,837.36 USD | `+18.47%` | `4X Isolated` |
| `577` | `0x382b...3e39` | `LONG` | 3,868,162.58 USD | `3,105.96` | `1220.72` | `1245.20` | `0.000000` | 76,659.97 USD | `+1.98%` | `10X Cross` |
| `585` | `0xdbe0...d6d5` | `LONG` | 3,846,839.32 USD | `3,085.37` | `422.97` | `1245.20` | `338.80` | 2,541,834.82 USD | `+66.08%` | `3X Isolated` |
| `597` | `0x2e30...4cb5` | `SHORT` | 3,767,144.58 USD | `3,025.09` | `1281.62` | `1245.20` | `2869.84` | 109,879.02 USD | `+2.92%` | `2X Cross` |
| `602` | `0x325e...9564` | `LONG` | 3,737,396.03 USD | `3,000.91` | `1298.07` | `1245.20` | `152.36` | -158,009.13 USD | `-4.23%` | `10X Cross` |
| `603` | `0x9c06...0560` | `SHORT` | 3,733,662.24 USD | `2,989.80` | `786.00` | `1245.20` | `2542.64` | -1,383,667.24 USD | `-37.06%` | `10X Cross` |
| `620` | `0x27c9...d65d` | `SHORT` | 3,658,051.15 USD | `2,937.25` | `1254.41` | `1245.20` | `1744.78` | 26,467.91 USD | `+0.72%` | `10X Cross` |
| `715` | `0xa183...0482` | `LONG` | 3,155,376.08 USD | `2,534.00` | `530.25` | `1245.20` | `444.73` | 1,811,713.36 USD | `+57.42%` | `5X Isolated` |
| `716` | `0xac48...3201` | `LONG` | 3,152,730.10 USD | `2,531.50` | `1378.58` | `1245.20` | `549.20` | -337,142.18 USD | `-10.69%` | `10X Cross` |
| `724` | `0x0871...e927` | `LONG` | 3,112,000.00 USD | `2,500.00` | `1276.50` | `1245.20` | `0.000000` | -79,250.00 USD | `-2.55%` | `10X Cross` |
| `741` | `0x9b86...6e6e` | `LONG` | 3,073,952.07 USD | `2,463.30` | `637.58` | `1245.20` | `882.66` | 1,503,402.79 USD | `+48.91%` | `3X Cross` |
| `820` | `0xf48f...10fe` | `LONG` | 2,763,129.29 USD | `2,218.49` | `1517.87` | `1245.20` | `980.64` | -604,257.53 USD | `-21.87%` | `3X Cross` |
| `847` | `0x5bc4...3b0c` | `SHORT` | 2,653,230.47 USD | `2,130.74` | `1089.65` | `1245.20` | `3676.60` | -331,472.90 USD | `-12.49%` | `5X Cross` |
| `861` | `0x8de4...b9aa` | `SHORT` | 2,603,656.05 USD | `2,091.29` | `1331.35` | `1245.20` | `1690.09` | 180,583.66 USD | `+6.94%` | `3X Cross` |
| `865` | `0x4fe2...ac59` | `SHORT` | 2,579,933.28 USD | `2,071.57` | `1478.56` | `1245.20` | `1842.53` | 483,012.94 USD | `+18.72%` | `10X Cross` |
| `873` | `0xdf57...93f5` | `LONG` | 2,558,487.49 USD | `2,054.35` | `1227.36` | `1245.20` | `897.43` | 37,065.45 USD | `+1.45%` | `4X Isolated` |
| `878` | `0xbcd4...0dd2` | `LONG` | 2,532,433.79 USD | `2,033.92` | `1228.20` | `1245.20` | `781.60` | 34,382.98 USD | `+1.36%` | `10X Cross` |
| `888` | `0xf29c...9971` | `LONG` | 2,490,431.00 USD | `2,000.00` | `1254.95` | `1245.20` | `0.000000` | -19,466.07 USD | `-0.78%` | `10X Cross` |
| `889` | `0x9a99...d21a` | `LONG` | 2,490,000.00 USD | `2,000.00` | `1278.44` | `1245.20` | `0.000000` | -66,873.67 USD | `-2.69%` | `10X Cross` |
| `915` | `0x77ee...2902` | `SHORT` | 2,422,418.14 USD | `1,946.03` | `759.84` | `1245.20` | `5714.92` | -943,740.64 USD | `-38.96%` | `10X Cross` |
| `920` | `0x3e2f...b269` | `SHORT` | 2,398,030.15 USD | `1,925.51` | `1134.87` | `1245.20` | `2977.36` | -212,831.30 USD | `-8.88%` | `10X Cross` |
| `933` | `0x4f12...618b` | `SHORT` | 2,360,868.60 USD | `1,896.28` | `1608.30` | `1245.20` | `2116.98` | 688,915.79 USD | `+29.18%` | `3X Cross` |
| `938` | `0x71d0...8c26` | `SHORT` | 2,338,350.59 USD | `1,877.59` | `1268.47` | `1245.20` | `4187.94` | 43,323.95 USD | `+1.85%` | `10X Cross` |
| `939` | `0x039c...0ebd` | `SHORT` | 2,332,608.79 USD | `1,873.13` | `1250.08` | `1245.20` | `3293.28` | 8,958.76 USD | `+0.38%` | `10X Cross` |
| `985` | `0x866d...d6e1` | `LONG` | 2,243,191.84 USD | `1,802.05` | `674.73` | `1245.20` | `116.72` | 1,027,290.53 USD | `+45.80%` | `10X Cross` |
| `1004` | `0x2309...a2d9` | `LONG` | 2,179,210.65 USD | `1,750.37` | `1186.09` | `1245.20` | `808.96` | 103,116.54 USD | `+4.73%` | `8X Cross` |
| `1045` | `0x265e...7f70` | `LONG` | 2,056,416.30 USD | `1,651.74` | `1382.98` | `1245.20` | `0.000000` | -227,906.46 USD | `-11.08%` | `3X Cross` |
| `1052` | `0xfe7c...b7ae` | `SHORT` | 2,045,251.06 USD | `1,642.64` | `1346.92` | `1245.20` | `5673.35` | 167,257.56 USD | `+8.18%` | `10X Cross` |
| `1059` | `0x3e47...aaf6` | `LONG` | 2,037,659.48 USD | `1,636.28` | `1278.38` | `1245.20` | `1049.79` | -54,132.30 USD | `-2.66%` | `10X Cross` |
| `1061` | `0x2edd...8179` | `SHORT` | 2,037,483.68 USD | `1,635.98` | `1261.55` | `1245.20` | `2854.27` | 26,379.20 USD | `+1.29%` | `10X Cross` |
| `1073` | `0x7f75...9edf` | `LONG` | 2,012,679.25 USD | `1,616.48` | `1200.45` | `1245.20` | `990.36` | 72,174.77 USD | `+3.59%` | `10X Cross` |
| `1084` | `0x6646...6de5` | `SHORT` | 1,994,880.00 USD | `1,600.00` | `660.64` | `1245.20` | `4252.04` | -937,855.03 USD | `-47.01%` | `10X Cross` |
| `1087` | `0xfc27...9d9d` | `SHORT` | 1,989,094.11 USD | `1,596.64` | `1295.09` | `1245.20` | `13064.41` | 78,691.01 USD | `+3.96%` | `10X Cross` |
| `1092` | `0x023a...2355` | `SHORT` | 1,981,489.49 USD | `1,591.43` | `1309.94` | `1245.20` | `4423.48` | 103,185.82 USD | `+5.21%` | `10X Cross` |
| `1117` | `0xab59...59b5` | `LONG` | 1,949,293.00 USD | `1,565.32` | `1342.15` | `1245.20` | `840.07` | -151,602.22 USD | `-7.78%` | `10X Cross` |
| `1172` | `0xcf67...eb24` | `LONG` | 1,868,100.00 USD | `1,500.00` | `887.05` | `1245.20` | `620.68` | 537,528.63 USD | `+28.77%` | `10X Cross` |
| `1199` | `0x7277...0b98` | `SHORT` | 1,837,874.14 USD | `1,475.73` | `1287.86` | `1245.20` | `2194.64` | 62,657.98 USD | `+3.41%` | `10X Cross` |
| `1245` | `0xfc66...ca06` | `SHORT` | 1,756,558.05 USD | `1,410.89` | `1269.67` | `1245.20` | `15679.60` | 34,811.70 USD | `+1.98%` | `10X Cross` |
| `1255` | `0x926a...af36` | `LONG` | 1,745,681.57 USD | `1,401.68` | `1254.50` | `1245.20` | `1187.95` | -12,720.33 USD | `-0.73%` | `10X Isolated` |
| `1256` | `0x2ab7...c2f8` | `LONG` | 1,745,595.66 USD | `1,400.51` | `813.26` | `1245.20` | `791.73` | 606,613.98 USD | `+34.75%` | `3X Cross` |
| `1272` | `0x11be...8b1d` | `LONG` | 1,713,321.10 USD | `1,375.83` | `1206.55` | `1245.20` | `1134.71` | 53,313.14 USD | `+3.11%` | `10X Isolated` |
| `1296` | `0xdf83...3cff` | `SHORT` | 1,668,001.62 USD | `1,338.90` | `1260.77` | `1245.20` | `1839.18` | 20,039.74 USD | `+1.20%` | `10X Cross` |
| `1340` | `0xef96...9383` | `SHORT` | 1,615,769.51 USD | `1,297.39` | `1262.03` | `1245.20` | `3889.67` | 21,572.44 USD | `+1.34%` | `10X Cross` |
| `1358` | `0xe065...0f85` | `SHORT` | 1,571,949.45 USD | `1,262.61` | `1087.02` | `1245.20` | `1553.71` | -199,473.32 USD | `-12.69%` | `10X Cross` |
| `1380` | `0x413c...886c` | `LONG` | 1,556,625.00 USD | `1,250.00` | `1237.51` | `1245.20` | `0.000000` | 9,735.54 USD | `+0.63%` | `10X Cross` |
| `1434` | `0x2847...d47b` | `LONG` | 1,508,578.95 USD | `1,211.71` | `1232.45` | `1245.20` | `0.000000` | 15,211.35 USD | `+1.01%` | `5X Cross` |
| `1450` | `0x266b...efcb` | `LONG` | 1,496,160.00 USD | `1,200.00` | `893.76` | `1245.20` | `412.09` | 423,650.30 USD | `+28.32%` | `10X Cross` |
| `1451` | `0x5975...9abd` | `LONG` | 1,494,360.00 USD | `1,200.00` | `1179.54` | `1245.20` | `539.18` | 78,917.21 USD | `+5.28%` | `5X Cross` |
| `1481` | `0x69cc...14fd` | `SHORT` | 1,446,357.74 USD | `1,161.36` | `675.33` | `1245.20` | `8070.25` | -662,052.22 USD | `-45.77%` | `10X Cross` |
| `1502` | `0x3fc5...c0c1` | `SHORT` | 1,430,152.33 USD | `1,148.44` | `1264.34` | `1245.20` | `2790.86` | 21,861.44 USD | `+1.53%` | `10X Cross` |
| `1543` | `0x5f94...4b96` | `LONG` | 1,391,745.43 USD | `1,115.27` | `538.00` | `1245.20` | `0.000000` | 791,727.80 USD | `+56.89%` | `10X Cross` |
| `1551` | `0xe35c...a1d3` | `LONG` | 1,383,976.61 USD | `1,111.36` | `1311.66` | `1245.20` | `691.00` | -73,747.54 USD | `-5.33%` | `2X Isolated` |
| `1570` | `0x71df...a23d` | `SHORT` | 1,369,873.66 USD | `1,098.28` | `513.50` | `1245.20` | `2560.59` | -805,903.47 USD | `-58.83%` | `2X Cross` |
| `1590` | `0xbfc7...80b4` | `SHORT` | 1,338,375.00 USD | `1,075.00` | `558.03` | `1245.20` | `2694.44` | -738,496.27 USD | `-55.18%` | `10X Cross` |
| `1592` | `0x8b9d...7b28` | `SHORT` | 1,335,780.37 USD | `1,070.68` | `1272.16` | `1245.20` | `3302.34` | 26,297.88 USD | `+1.97%` | `10X Cross` |
| `1621` | `0x123d...3bff` | `SHORT` | 1,300,516.60 USD | `1,044.34` | `519.62` | `1245.20` | `4164.73` | -757,858.39 USD | `-58.27%` | `10X Cross` |
| `1639` | `0x3205...40bb` | `SHORT` | 1,291,722.20 USD | `1,036.03` | `1262.06` | `1245.20` | `2686.09` | 15,807.66 USD | `+1.22%` | `10X Cross` |
| `1687` | `0xe282...df29` | `LONG` | 1,245,300.00 USD | `1,000.00` | `420.99` | `1245.20` | `801.38` | 824,313.14 USD | `+66.19%` | `10X Cross` |
| `1689` | `0x668c...ea2e` | `SHORT` | 1,245,000.00 USD | `1,000.00` | `1406.98` | `1245.20` | `4211.90` | 161,981.99 USD | `+13.01%` | `10X Cross` |
| `1690` | `0x8ab1...15ef` | `LONG` | 1,245,000.00 USD | `1,000.00` | `1275.75` | `1245.20` | `1008.58` | -30,754.92 USD | `-2.47%` | `10X Cross` |
| `1702` | `0x17f0...094f` | `LONG` | 1,229,753.41 USD | `984.30` | `1287.23` | `1245.20` | `537.06` | -37,266.75 USD | `-3.03%` | `5X Cross` |
| `1736` | `0x51f6...2b39` | `SHORT` | 1,200,901.86 USD | `964.27` | `1299.77` | `1245.20` | `2508.20` | 52,425.82 USD | `+4.37%` | `10X Cross` |
| `1739` | `0x5323...b23c` | `SHORT` | 1,196,702.96 USD | `961.13` | `1269.11` | `1245.20` | `7066.45` | 23,078.40 USD | `+1.93%` | `5X Cross` |
| `1744` | `0x4e23...20c3` | `LONG` | 1,191,358.11 USD | `956.53` | `1265.15` | `1245.20` | `0.000000` | -18,793.33 USD | `-1.58%` | `4X Cross` |
| `1765` | `0xf096...7553` | `SHORT` | 1,171,146.60 USD | `940.68` | `1257.96` | `1245.20` | `3092.40` | 12,187.12 USD | `+1.04%` | `10X Cross` |
| `1795` | `0x757d...94ba` | `LONG` | 1,151,824.34 USD | `925.00` | `1558.31` | `1245.20` | `0.000000` | -289,616.25 USD | `-25.14%` | `10X Cross` |
| `1834` | `0xb911...5525` | `LONG` | 1,120,770.00 USD | `900.00` | `1294.82` | `1245.20` | `1035.49` | -44,567.82 USD | `-3.98%` | `10X Cross` |
| `1875` | `0xcf0a...856f` | `LONG` | 1,087,892.12 USD | `871.15` | `1292.19` | `1245.20` | `1025.84` | -37,802.73 USD | `-3.47%` | `4X Cross` |
| `1895` | `0xdf95...7d72` | `SHORT` | 1,062,455.22 USD | `853.23` | `1074.39` | `1245.20` | `45154.81` | -145,750.76 USD | `-13.72%` | `10X Cross` |
| `1934` | `0xb2f7...af9f` | `SHORT` | 1,034,661.76 USD | `830.72` | `746.63` | `1245.20` | `8272.58` | -414,422.73 USD | `-40.05%` | `10X Cross` |
| `1948` | `0x601c...4f54` | `SHORT` | 1,028,216.62 USD | `824.42` | `615.11` | `1245.20` | `3139.27` | -521,103.87 USD | `-50.68%` | `5X Cross` |
| `1961` | `0x8b61...c0c2` | `LONG` | 1,019,178.43 USD | `818.42` | `1274.67` | `1245.20` | `1005.21` | -24,035.61 USD | `-2.36%` | `4X Isolated` |
| `1963` | `0xae55...2236` | `LONG` | 1,018,404.13 USD | `817.47` | `1467.80` | `1245.20` | `0.000000` | -181,477.09 USD | `-17.82%` | `10X Cross` |

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
| `ANNOUNCEMENT` | `INFO` | `1273.30` | 904.04 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 0.90K USD at 1273.3000 USD [API] | `2026-10-29 20:39:28` |
| `ANNOUNCEMENT` | `INFO` | `1254.80` | 1,279.90 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 1.28K USD at 1254.8000 USD [API] | `2026-10-29 20:42:27` |


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
| `5m` | `BALANCED` | 0.00 USD | 1,750.00 USD | 1,750.00 USD | 1,750.00 USD | `1` | `2026-10-30 11:50:00 UTC - 2026-10-30 11:55:00 UTC` |
| `15m` | `BALANCED` | 0.00 USD | 1,750.00 USD | 1,750.00 USD | 1,750.00 USD | `1` | `2026-10-30 11:45:00 UTC - 2026-10-30 12:00:00 UTC` |
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
  * Current Rate: `84.11K` | Last 24h: `171.90K` | Last 3d: `285.15K` | Last 7d: `847.79K`
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
| `0:00 UTC` | `1244.55` | `1245.81` | `1244.55` | `1249.05` | `1243.65` | 9,717,386.64 USD | 3,914,194.68 USD | 5,803,191.96 USD | -1,888,997.28 USD | `-19.44%` | `0B / 1S` |
| `5:00 UTC` | `1242.15` | `1244.40` | `1242.15` | `1249.35` | `1241.25` | 8,638,502.97 USD | 4,533,952.89 USD | 4,104,550.08 USD | 429,402.82 USD | `+4.97%` | `4B / 2S` |
| `0:00 UTC` | `1251.15` | `1247.35` | `1251.15` | `1251.75` | `1240.05` | 9,977,652.60 USD | 4,992,881.35 USD | 4,984,771.25 USD | 8,110.10 USD | `+0.08%` | `3B / 5S` |
| `5:00 UTC` | `1243.95` | `1249.40` | `1243.95` | `1256.55` | `1243.35` | 15,678,426.53 USD | 9,268,825.46 USD | 6,409,601.07 USD | 2,859,224.38 USD | `+18.24%` | `10B / 2S` |
| `0:00 UTC` | `1249.95` | `1250.19` | `1249.95` | `1256.25` | `1246.35` | 11,248,393.80 USD | 4,953,252.73 USD | 6,295,141.07 USD | -1,341,888.34 USD | `-11.93%` | `1B / 7S` |
| `5:00 UTC` | `1263.15` | `1259.85` | `1263.15` | `1266.15` | `1247.85` | 19,587,954.68 USD | 10,529,516.42 USD | 9,058,438.26 USD | 1,471,078.16 USD | `+7.51%` | `10B / 4S` |
| `0:00 UTC` | `1272.15` | `1270.75` | `1272.15` | `1276.65` | `1262.25` | 28,700,563.02 USD | 14,735,645.79 USD | 13,964,917.22 USD | 770,728.57 USD | `+2.69%` | `10B / 0S` |
| `5:00 UTC` | `1267.95` | `1266.37` | `1267.95` | `1276.95` | `1257.75` | 25,317,311.22 USD | 15,013,433.04 USD | 10,303,878.19 USD | 4,709,554.85 USD | `+18.60%` | `12B / 5S` |
| `0:00 UTC` | `1270.05` | `1270.22` | `1270.05` | `1276.65` | `1264.05` | 13,074,018.65 USD | 5,810,348.90 USD | 7,263,669.75 USD | -1,453,320.86 USD | `-11.12%` | `2B / 4S` |
| `5:00 UTC` | `1263.15` | `1263.09` | `1263.15` | `1266.75` | `1259.55` | 7,424,461.24 USD | 3,284,480.41 USD | 4,139,980.83 USD | -855,500.43 USD | `-11.52%` | `1B / 9S` |

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
| `5m` | -221,370.00 USD | 2,270,000.00 USD | **`ACCUMULATION`** |
| `15m` | -816,960.00 USD | -4,350,000.00 USD | **`DISTRIBUTION`** |
| `30m` | -906,390.00 USD | -3,940,000.00 USD | **`DISTRIBUTION`** |
| `1h` | -1,040,000.00 USD | -62,580.00 USD | **`DISTRIBUTION`** |
| `2h` | -2,370,000.00 USD | 5,080,000.00 USD | **`ACCUMULATION`** |
| `4h` | -4,160,000.00 USD | 11,910,000.00 USD | **`ACCUMULATION`** |
| `6h` | -1,640,000.00 USD | -16,220,000.00 USD | **`DISTRIBUTION`** |
| `8h` | -2,480,000.00 USD | -30,260,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -1,880,000.00 USD | -6,340,000.00 USD | **`DISTRIBUTION`** |
| `24h` | 18,030,000.00 USD | 71,810,000.00 USD | **`ACCUMULATION`** |
| `1w` | 33,040,000.00 USD | 221,660,000.00 USD | **`ACCUMULATION`** |
| `30d` | 62,770,000.00 USD | -570,810,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-221.37K` | 15m=`-816.96K` | 1h=`-1.04M` | 24h=`+18.03M`
* Futures Capital Netflows: 5m=`+2.27M` | 15m=`-4.35M` | 1h=`-62.58K` | 24h=`+71.81M`
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
  * `2026-10-30 16:36:03 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 16:26:03 IST`: [marctomarket.com] - (Sentiment: `Neutral`)
  * `2026-10-30 15:50:03 IST`: [istat.it] - (Sentiment: `Neutral`)
  * `2026-10-30 16:48:03 IST`: [ec.europa.eu] - (Sentiment: `Neutral`)
  * `2026-10-30 16:48:03 IST`: [ec.europa.eu] - (Sentiment: `Neutral`)
  * `2026-10-30 16:48:03 IST`: [dailyforex.com] - (Sentiment: `Neutral`)
  * `2026-10-30 16:48:03 IST`: [breakingthenews.net] - (Sentiment: `Neutral`)
  * `2026-10-30 16:47:03 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 16:47:03 IST`: [@FirstSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 16:47:03 IST`: [destatis.de] - (Sentiment: `Neutral`)
  * `2026-10-30 16:47:03 IST`: [istat.it] - (Sentiment: `Neutral`)
  * `2026-10-30 16:47:03 IST`: [channelnewsasia.com] - (Sentiment: `Neutral`)
  * `2026-10-30 16:47:03 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 16:47:03 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 13:49:03 IST`: [kof.ethz.ch] - (Sentiment: `Neutral`)


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
  * Execution Entry: `1240.72` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `1224.11` (Risk Distance: `16.61` pts)
  * +2.5R Take Profit: `1282.24`
  * Mathematical Lot Sizing: **`0.60 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `1278.60` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `1295.21` (Risk Distance: `16.61` pts)
  * +2.5R Take Profit: `1237.08`
  * Mathematical Lot Sizing: **`0.60 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`1255.79`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
