# 🏛️ SOVEREIGN CANDIDATE DOSSIER: ZECUSD
**Canonical Key**: `ZECUSD` | **Broker Instrument**: `ZECUSD.p` | **Asset Class**: `Crypto Altcoin`
**Timestamp**: `2026-10-30 03:37:25 IST` (`2026-10-29 22:07:25 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `1254.43` | **Live Ask Quote**: `1255.47` | **Mid Price**: `1254.95`
- **Spread Points**: `104.00` | **Spread BPS**: `8.29 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `1281.09` | VWAP Z-Score: `-0.55` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `22.38` (Volatility Regime: `HIGH_EXPANSION`)
  * 14-Period RSI: `37.75` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `1394.32` | Lower -3.00σ Band: `1167.85`
  * Upper +2.51σ Band: `1375.83` | Lower -2.51σ Band: `1186.34`
  * Upper +2.01σ Band: `1356.95` | Lower -2.01σ Band: `1205.22`
  * Upper +2.00σ Band: `1356.58` | Lower -2.00σ Band: `1205.59`
  * Upper +1.28σ Band: `1329.40` | Lower -1.28σ Band: `1232.77`
  * Upper +1.00σ Band: `1318.83` | Lower -1.00σ Band: `1243.34`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`1275.32` | EMA-20=`1291.96` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`1293.95` (Slope: `+0.0000`) | EMA-100=`1288.24`
  * Institutional Anchors: EMA-144=`1284.39` | EMA-200=`1280.59` (Slope: `+0.0510`) | EMA-233=`1279.78`
- **Range Boundaries**: 24H High=`1396.49` | 24H Low=`1206.89` | Weekly High=`1396.49` | Weekly Low=`1206.89`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `1285.20` (Distance: `-2.13%`)
  * Point of Control (POC) = `1268.59` (Distance: `-0.85%`)
  * Value Area Low (VAL) = `1259.96` (Distance: `-0.17%`)
  * Auction Positioning: `BELOW_VALUE (Imbalance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `RANGE_EXPANSION`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`1309.91` | POC=`1246.71` | VAL=`1230.27`
  * Prior Day Extremes: PDH=`1396.49` | PDL=`1206.89` | PDC=`1244.38`
  * Monday Range Blueprint: High=`1267.53` | Mid=`1222.14` | Low=`1176.75`
  * Developing Weekly Value Area: Weekly VAH=`1296.14` | Weekly POC=`1239.01` | Weekly VAL=`1196.53`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`1296.00` | Low=`1246.17`
  * London Session (08:00-16:00 UTC): High=`1259.97` | Low=`1249.93`
  * New York Session (13:00-21:00 UTC): High=`1262.48` | Low=`1247.42`
  * Initial Balance (First Hour): IB High=`1258.71` | IB Low=`1251.19`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `1249.93` - `1259.97`
  * Optimal Trade Entry (OTE 0.705): `1257.46`
  * Structural Invalidation Anchor (0.786): `1264.99`

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
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 03:35:39 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `16` | `0xb83d...6e36` | `SHORT` | 66,524,308.35 USD | `52,385.47` | `1336.45` | `1272.70` | `3982.82` | 3,486,259.05 USD | `+5.24%` | `3X Cross` |
| `23` | `0x5b5d...c060` | `SHORT` | 50,958,164.74 USD | `40,121.38` | `1478.36` | `1272.70` | `5456.88` | 8,355,870.37 USD | `+16.40%` | `3X Cross` |
| `43` | `0x7fda...17d1` | `SHORT` | 28,768,036.43 USD | `22,600.39` | `1262.40` | `1272.70` | `2970.36` | -237,232.71 USD | `-0.82%` | `5X Cross` |
| `81` | `0x60b0...991e` | `LONG` | 21,372,354.84 USD | `16,779.74` | `1179.65` | `1272.70` | `923.18` | 1,578,107.82 USD | `+7.38%` | `10X Cross` |
| `139` | `0xc36a...105b` | `LONG` | 14,581,906.78 USD | `11,510.82` | `1215.14` | `1272.70` | `958.59` | 594,625.75 USD | `+4.08%` | `10X Cross` |
| `156` | `0x9071...5c0b` | `LONG` | 13,386,406.71 USD | `10,517.29` | `1353.83` | `1272.70` | `0.000000` | -852,212.16 USD | `-6.37%` | `1X Cross` |
| `177` | `0x8742...8427` | `LONG` | 11,711,300.09 USD | `9,201.21` | `1286.37` | `1272.70` | `707.54` | -124,869.91 USD | `-1.07%` | `10X Cross` |
| `201` | `0x58b2...11f3` | `LONG` | 10,756,358.03 USD | `8,463.08` | `1257.17` | `1272.70` | `431.39` | 116,868.83 USD | `+1.09%` | `10X Cross` |
| `202` | `0xad59...ba81` | `SHORT` | 10,723,340.00 USD | `8,425.00` | `330.91` | `1272.70` | `2144.58` | -7,935,382.23 USD | `-74.00%` | `10X Cross` |
| `207` | `0x9ffd...ce40` | `LONG` | 10,657,688.52 USD | `8,391.22` | `1256.51` | `1272.70` | `600.64` | 114,077.83 USD | `+1.07%` | `5X Cross` |
| `213` | `0xdd53...2b13` | `SHORT` | 10,394,851.32 USD | `8,168.20` | `739.52` | `1272.70` | `8544.78` | -4,354,341.13 USD | `-41.89%` | `3X Cross` |
| `219` | `0xbf73...5d58` | `LONG` | 10,134,400.00 USD | `8,000.00` | `1291.41` | `1272.70` | `292.54` | -196,856.76 USD | `-1.94%` | `10X Cross` |
| `231` | `0x880a...311c` | `SHORT` | 9,769,532.64 USD | `7,707.11` | `1367.50` | `1272.70` | `2276.45` | 769,951.57 USD | `+7.88%` | `10X Cross` |
| `269` | `0xfc66...ca06` | `SHORT` | 8,763,089.12 USD | `6,884.35` | `1319.65` | `1272.70` | `4755.07` | 321,861.67 USD | `+3.67%` | `10X Cross` |
| `276` | `0x2b61...2f6c` | `LONG` | 8,628,553.20 USD | `6,807.00` | `1453.56` | `1272.70` | `556.37` | -1,265,798.02 USD | `-14.67%` | `10X Cross` |
| `292` | `0x2ae5...83e7` | `LONG` | 8,192,759.04 USD | `6,436.80` | `1391.82` | `1272.70` | `0.000000` | -766,132.95 USD | `-9.35%` | `1X Cross` |
| `336` | `0x26b6...9a13` | `LONG` | 6,916,594.92 USD | `5,433.73` | `1282.23` | `1272.70` | `218.08` | -50,708.32 USD | `-0.73%` | `10X Cross` |
| `350` | `0x45d2...4029` | `SHORT` | 6,652,925.60 USD | `5,227.00` | `833.44` | `1272.70` | `8764.43` | -2,296,547.63 USD | `-34.52%` | `5X Cross` |
| `373` | `0xea00...a918` | `LONG` | 6,357,500.00 USD | `5,000.00` | `739.16` | `1272.70` | `0.000000` | 2,661,684.89 USD | `+41.87%` | `5X Cross` |
| `377` | `0xecb6...2b00` | `SHORT` | 6,321,805.71 USD | `4,962.95` | `1305.76` | `1272.70` | `6764.04` | 158,624.75 USD | `+2.51%` | `5X Cross` |
| `386` | `0xdd7a...8830` | `LONG` | 6,186,535.85 USD | `4,860.19` | `897.48` | `1272.70` | `776.92` | 1,824,632.18 USD | `+29.49%` | `10X Cross` |
| `432` | `0x5323...b23c` | `SHORT` | 5,128,692.31 USD | `4,029.14` | `1287.77` | `1272.70` | `2630.13` | 59,912.98 USD | `+1.17%` | `5X Cross` |
| `435` | `0x4cae...7c34` | `LONG` | 5,079,530.66 USD | `4,004.36` | `999.34` | `1272.70` | `915.98` | 1,077,802.50 USD | `+21.22%` | `10X Cross` |
| `445` | `0xa61c...66b9` | `LONG` | 4,953,700.80 USD | `3,888.00` | `1148.34` | `1272.70` | `0.000000` | 488,958.66 USD | `+9.87%` | `10X Cross` |
| `468` | `0x9aa5...58af` | `SHORT` | 4,725,537.76 USD | `3,720.31` | `1205.51` | `1272.70` | `3632.91` | -240,650.96 USD | `-5.09%` | `10X Cross` |
| `473` | `0x0153...8052` | `SHORT` | 4,709,262.41 USD | `3,698.18` | `1307.82` | `1272.70` | `2504.72` | 127,308.34 USD | `+2.70%` | `1X Isolated` |
| `534` | `0xd21d...90f1` | `LONG` | 4,135,950.00 USD | `3,250.00` | `1253.64` | `1272.70` | `875.91` | 61,608.27 USD | `+1.49%` | `4X Isolated` |
| `552` | `0x382b...3e39` | `LONG` | 4,023,630.32 USD | `3,161.74` | `1210.73` | `1272.70` | `0.000000` | 195,628.33 USD | `+4.86%` | `10X Cross` |
| `559` | `0x1338...c48e` | `LONG` | 4,011,743.93 USD | `3,149.43` | `1018.52` | `1272.70` | `820.21` | 803,998.39 USD | `+20.04%` | `4X Isolated` |
| `567` | `0x456f...cdf1` | `LONG` | 3,984,707.45 USD | `3,134.11` | `1268.47` | `1272.70` | `493.65` | 9,197.99 USD | `+0.23%` | `10X Cross` |
| `580` | `0xdbe0...d6d5` | `LONG` | 3,928,910.16 USD | `3,085.37` | `422.97` | `1272.70` | `338.52` | 2,623,905.67 USD | `+66.78%` | `3X Isolated` |
| `589` | `0x27c9...d65d` | `SHORT` | 3,879,506.43 USD | `3,047.77` | `1254.41` | `1272.70` | `1753.64` | -56,349.86 USD | `-1.45%` | `10X Cross` |
| `596` | `0x325e...9564` | `LONG` | 3,824,733.53 USD | `3,001.91` | `1301.41` | `1272.70` | `145.81` | -81,975.68 USD | `-2.14%` | `10X Cross` |
| `602` | `0x9c06...0560` | `SHORT` | 3,797,344.98 USD | `2,989.80` | `786.00` | `1272.70` | `2541.83` | -1,447,349.98 USD | `-38.11%` | `10X Cross` |
| `612` | `0xd4c1...3d1d` | `SHORT` | 3,737,796.90 USD | `2,935.75` | `1301.98` | `1272.70` | `2931.89` | 84,494.02 USD | `+2.26%` | `10X Cross` |
| `636` | `0xac48...3201` | `LONG` | 3,616,282.53 USD | `2,846.57` | `1381.74` | `1272.70` | `627.11` | -316,950.57 USD | `-8.76%` | `10X Cross` |
| `640` | `0x2e30...4cb5` | `SHORT` | 3,584,247.78 USD | `2,819.80` | `1299.29` | `1272.70` | `2959.28` | 79,498.39 USD | `+2.22%` | `2X Cross` |
| `713` | `0xa183...0482` | `LONG` | 3,225,275.20 USD | `2,534.00` | `530.25` | `1272.70` | `444.45` | 1,881,612.48 USD | `+58.34%` | `5X Isolated` |
| `720` | `0x413c...886c` | `LONG` | 3,182,000.00 USD | `2,500.00` | `1268.64` | `1272.70` | `0.000000` | 10,388.36 USD | `+0.33%` | `10X Cross` |
| `724` | `0x0871...e927` | `LONG` | 3,169,000.00 USD | `2,500.00` | `1276.50` | `1272.70` | `0.000000` | -22,250.00 USD | `-0.70%` | `10X Cross` |
| `737` | `0x9b86...6e6e` | `LONG` | 3,136,925.22 USD | `2,467.30` | `637.58` | `1272.70` | `889.67` | 1,563,825.62 USD | `+49.85%` | `3X Cross` |
| `785` | `0xb2f7...af9f` | `SHORT` | 2,947,216.54 USD | `2,313.72` | `746.63` | `1272.70` | `4373.69` | -1,219,727.79 USD | `-41.39%` | `10X Cross` |
| `817` | `0xf48f...10fe` | `LONG` | 2,823,250.37 USD | `2,218.49` | `1517.87` | `1272.70` | `968.94` | -544,136.45 USD | `-19.27%` | `3X Cross` |
| `847` | `0x5bc4...3b0c` | `SHORT` | 2,712,005.87 USD | `2,130.74` | `1089.65` | `1272.70` | `3668.54` | -390,248.29 USD | `-14.39%` | `5X Cross` |
| `860` | `0x8de4...b9aa` | `SHORT` | 2,657,976.05 USD | `2,091.29` | `1331.35` | `1272.70` | `1689.84` | 126,263.65 USD | `+4.75%` | `3X Cross` |
| `867` | `0x4fe2...ac59` | `SHORT` | 2,634,001.25 USD | `2,071.57` | `1478.56` | `1272.70` | `1828.84` | 428,944.96 USD | `+16.28%` | `10X Cross` |
| `879` | `0x71d0...8c26` | `SHORT` | 2,587,080.15 USD | `2,032.43` | `1289.75` | `1272.70` | `4025.03` | 34,250.38 USD | `+1.32%` | `10X Cross` |
| `894` | `0x9a99...d21a` | `LONG` | 2,534,400.00 USD | `2,000.00` | `1278.44` | `1272.70` | `0.000000` | -22,473.67 USD | `-0.89%` | `10X Cross` |
| `926` | `0x77ee...2902` | `SHORT` | 2,466,787.63 USD | `1,946.03` | `759.84` | `1272.70` | `5333.67` | -988,110.12 USD | `-40.06%` | `10X Cross` |
| `931` | `0x3e2f...b269` | `SHORT` | 2,450,789.13 USD | `1,925.51` | `1134.87` | `1272.70` | `2931.77` | -265,590.27 USD | `-10.84%` | `10X Cross` |
| `940` | `0xe097...d0fe` | `LONG` | 2,436,344.59 USD | `1,913.56` | `1261.17` | `1272.70` | `0.000000` | 23,018.43 USD | `+0.94%` | `10X Cross` |
| `950` | `0x4f12...618b` | `SHORT` | 2,401,069.74 USD | `1,896.28` | `1608.30` | `1272.70` | `2116.73` | 648,714.65 USD | `+27.02%` | `3X Cross` |
| `991` | `0x866d...d6e1` | `LONG` | 2,285,900.42 USD | `1,802.05` | `674.73` | `1272.70` | `196.17` | 1,069,999.11 USD | `+46.81%` | `10X Cross` |
| `1016` | `0x2309...a2d9` | `LONG` | 2,217,368.72 USD | `1,750.37` | `1186.09` | `1272.70` | `813.67` | 141,274.61 USD | `+6.37%` | `8X Cross` |
| `1038` | `0x023a...2355` | `SHORT` | 2,160,000.65 USD | `1,696.38` | `1313.00` | `1272.70` | `5809.80` | 67,346.64 USD | `+3.12%` | `10X Cross` |
| `1039` | `0x2edd...8179` | `SHORT` | 2,158,286.17 USD | `1,701.85` | `1261.58` | `1272.70` | `3066.06` | -11,267.32 USD | `-0.52%` | `10X Cross` |
| `1072` | `0xfe7c...b7ae` | `SHORT` | 2,082,580.41 USD | `1,640.99` | `1347.05` | `1272.70` | `6996.39` | 127,908.78 USD | `+6.14%` | `10X Cross` |
| `1073` | `0x3e47...aaf6` | `LONG` | 2,080,366.39 USD | `1,636.28` | `1278.38` | `1272.70` | `1046.47` | -11,425.39 USD | `-0.55%` | `10X Cross` |
| `1077` | `0xa271...a3f7` | `LONG` | 2,072,079.24 USD | `1,631.43` | `1190.60` | `1272.70` | `910.31` | 129,697.44 USD | `+6.26%` | `4X Cross` |
| `1096` | `0x6646...6de5` | `SHORT` | 2,037,120.00 USD | `1,600.00` | `660.64` | `1272.70` | `4466.09` | -980,095.03 USD | `-48.11%` | `10X Cross` |
| `1097` | `0x265e...7f70` | `LONG` | 2,034,369.97 USD | `1,601.74` | `1388.09` | `1272.70` | `0.000000` | -188,995.03 USD | `-9.29%` | `3X Cross` |
| `1098` | `0x7f75...9edf` | `LONG` | 2,034,202.10 USD | `1,605.78` | `1199.97` | `1272.70` | `976.87` | 107,310.21 USD | `+5.28%` | `10X Cross` |
| `1112` | `0xdf57...93f5` | `LONG` | 2,010,086.62 USD | `1,579.76` | `1218.38` | `1272.70` | `780.15` | 85,330.64 USD | `+4.25%` | `3X Isolated` |
| `1127` | `0xab59...59b5` | `LONG` | 1,992,339.30 USD | `1,565.32` | `1342.15` | `1272.70` | `826.38` | -108,555.92 USD | `-5.45%` | `10X Cross` |
| `1197` | `0xcf67...eb24` | `LONG` | 1,900,800.00 USD | `1,500.00` | `887.05` | `1272.70` | `652.84` | 570,228.63 USD | `+30.00%` | `10X Cross` |
| `1205` | `0xb695...a92d` | `LONG` | 1,887,562.40 USD | `1,483.00` | `1249.80` | `1272.70` | `0.000000` | 34,103.54 USD | `+1.81%` | `10X Cross` |
| `1277` | `0x2ab7...c2f8` | `LONG` | 1,780,188.26 USD | `1,400.51` | `813.26` | `1272.70` | `800.74` | 641,206.58 USD | `+36.02%` | `3X Cross` |
| `1296` | `0x11be...8b1d` | `LONG` | 1,749,367.84 USD | `1,375.83` | `1206.55` | `1272.70` | `1134.43` | 89,359.89 USD | `+5.11%` | `10X Isolated` |
| `1321` | `0x3205...40bb` | `SHORT` | 1,700,689.37 USD | `1,335.55` | `1270.19` | `1272.70` | `2350.19` | -4,290.43 USD | `-0.25%` | `10X Cross` |
| `1395` | `0xe065...0f85` | `SHORT` | 1,603,640.96 USD | `1,262.61` | `1087.02` | `1272.70` | `1816.76` | -231,164.83 USD | `-14.41%` | `10X Cross` |
| `1400` | `0x039c...0ebd` | `SHORT` | 1,591,812.37 USD | `1,250.54` | `1239.86` | `1272.70` | `3629.47` | -41,313.80 USD | `-2.60%` | `10X Cross` |
| `1430` | `0x7277...0b98` | `SHORT` | 1,571,363.10 USD | `1,234.96` | `1298.48` | `1272.70` | `2418.02` | 32,206.31 USD | `+2.05%` | `10X Cross` |
| `1469` | `0x5975...9abd` | `LONG` | 1,527,360.00 USD | `1,200.00` | `1179.54` | `1272.70` | `477.95` | 111,917.21 USD | `+7.33%` | `5X Cross` |
| `1509` | `0x69cc...14fd` | `SHORT` | 1,477,714.46 USD | `1,161.36` | `675.33` | `1272.70` | `7998.65` | -693,408.94 USD | `-46.92%` | `10X Cross` |
| `1521` | `0x3fc5...c0c1` | `SHORT` | 1,460,126.62 USD | `1,148.44` | `1264.34` | `1272.70` | `3079.83` | -8,112.84 USD | `-0.56%` | `10X Cross` |
| `1551` | `0xe35c...a1d3` | `LONG` | 1,434,634.67 USD | `1,127.06` | `1318.20` | `1272.70` | `694.35` | -51,060.68 USD | `-3.56%` | `2X Isolated` |
| `1555` | `0x2847...d47b` | `LONG` | 1,432,610.76 USD | `1,125.47` | `1233.65` | `1272.70` | `0.000000` | 44,178.64 USD | `+3.08%` | `5X Cross` |
| `1559` | `0xdf83...3cff` | `SHORT` | 1,426,495.52 USD | `1,120.93` | `1254.83` | `1272.70` | `1783.59` | -19,919.87 USD | `-1.40%` | `10X Cross` |
| `1570` | `0x5f94...4b96` | `LONG` | 1,417,731.22 USD | `1,115.27` | `538.00` | `1272.70` | `0.000000` | 817,713.59 USD | `+57.68%` | `10X Cross` |
| `1573` | `0xfc27...9d9d` | `SHORT` | 1,415,760.90 USD | `1,112.32` | `1315.10` | `1272.70` | `16287.94` | 47,050.86 USD | `+3.32%` | `10X Cross` |
| `1584` | `0x266b...efcb` | `LONG` | 1,400,520.00 USD | `1,100.00` | `863.84` | `1272.70` | `300.98` | 450,295.24 USD | `+32.15%` | `10X Cross` |
| `1590` | `0x71df...a23d` | `SHORT` | 1,392,179.73 USD | `1,098.28` | `513.50` | `1272.70` | `2551.88` | -828,209.54 USD | `-59.49%` | `2X Cross` |
| `1614` | `0xbfc7...80b4` | `SHORT` | 1,361,810.00 USD | `1,075.00` | `558.03` | `1272.70` | `5299.97` | -761,931.27 USD | `-55.95%` | `10X Cross` |
| `1623` | `0xef96...9383` | `SHORT` | 1,346,576.24 USD | `1,058.13` | `1258.98` | `1272.70` | `5213.09` | -14,408.68 USD | `-1.07%` | `10X Cross` |
| `1634` | `0x51f6...2b39` | `SHORT` | 1,341,371.30 USD | `1,054.04` | `1302.05` | `1272.70` | `2792.19` | 31,036.76 USD | `+2.31%` | `10X Cross` |
| `1652` | `0x38f9...cb04` | `SHORT` | 1,318,448.16 USD | `1,036.19` | `1269.33` | `1272.70` | `2091.50` | -3,176.12 USD | `-0.24%` | `10X Cross` |
| `1679` | `0x123d...3bff` | `SHORT` | 1,284,662.50 USD | `1,009.32` | `490.16` | `1272.70` | `4405.95` | -789,936.63 USD | `-61.49%` | `10X Cross` |
| `1690` | `0xb5ff...d912` | `LONG` | 1,272,900.00 USD | `1,000.00` | `1280.79` | `1272.70` | `452.78` | -7,887.44 USD | `-0.62%` | `2X Cross` |
| `1700` | `0x668c...ea2e` | `SHORT` | 1,266,800.00 USD | `1,000.00` | `1406.98` | `1272.70` | `4180.89` | 140,181.99 USD | `+11.07%` | `10X Cross` |
| `1701` | `0xe282...df29` | `LONG` | 1,266,400.00 USD | `1,000.00` | `420.99` | `1272.70` | `184.60` | 845,413.14 USD | `+66.76%` | `10X Cross` |
| `1718` | `0x17f0...094f` | `LONG` | 1,248,584.55 USD | `984.30` | `1287.23` | `1272.70` | `536.78` | -18,435.61 USD | `-1.48%` | `5X Cross` |
| `1785` | `0x757d...94ba` | `LONG` | 1,177,340.00 USD | `925.00` | `1558.31` | `1272.70` | `0.000000` | -264,100.59 USD | `-22.43%` | `10X Cross` |
| `1823` | `0xb911...5525` | `LONG` | 1,143,180.00 USD | `900.00` | `1294.82` | `1272.70` | `1070.30` | -22,157.82 USD | `-1.94%` | `10X Cross` |
| `1875` | `0xcf0a...856f` | `LONG` | 1,103,572.82 USD | `871.15` | `1292.19` | `1272.70` | `992.27` | -22,122.03 USD | `-2.00%` | `4X Cross` |
| `1881` | `0xdf95...7d72` | `SHORT` | 1,090,955.76 USD | `857.40` | `1074.33` | `1272.70` | `45765.75` | -169,827.44 USD | `-15.57%` | `10X Cross` |
| `1936` | `0x601c...4f54` | `SHORT` | 1,048,167.59 USD | `824.42` | `615.11` | `1272.70` | `3013.26` | -541,054.84 USD | `-51.62%` | `5X Cross` |
| `1946` | `0xae55...2236` | `LONG` | 1,040,475.82 USD | `817.47` | `1467.80` | `1272.70` | `0.000000` | -159,405.40 USD | `-15.32%` | `10X Cross` |
| `1978` | `0x0f02...5384` | `LONG` | 1,019,072.63 USD | `800.78` | `1290.36` | `1272.70` | `297.61` | -14,221.44 USD | `-1.40%` | `3X Cross` |
| `1980` | `0x9b0f...db40` | `LONG` | 1,018,720.00 USD | `800.00` | `1268.86` | `1272.70` | `788.59` | 3,630.24 USD | `+0.36%` | `10X Cross` |
| `2005` | `0xf096...7553` | `SHORT` | 1,006,668.56 USD | `792.59` | `1251.77` | `1272.70` | `4012.65` | -14,526.52 USD | `-1.44%` | `10X Cross` |
| `2009` | `0xabdb...84ac` | `LONG` | 1,005,446.49 USD | `793.69` | `711.79` | `1272.70` | `664.35` | 440,506.13 USD | `+43.81%` | `3X Cross` |

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
  * 24H Horizon: Short MP=`1403.54` (Vol: 3,000,000.00 USD, Dist: `+10.01%`) | Long MP=`1200.05` (Vol: 597,500.00 USD, Dist: `--5.94%`)
  * 48H Horizon: Short MP=`1403.54` (Vol: 3,000,000.00 USD, Dist: `+10.01%`) | Long MP=`1246.00` (Vol: 2,300,000.00 USD, Dist: `--2.34%`)
  * 3D Horizon: Short MP=`1403.54` (Vol: 3,000,000.00 USD, Dist: `+10.01%`) | Long MP=`1247.64` (Vol: 2,400,000.00 USD, Dist: `--2.21%`)
  * 7D Horizon: Short MP=`1404.10` (Vol: 3,000,000.00 USD, Dist: `+10.05%`) | Long MP=`1200.46` (Vol: 3,000,000.00 USD, Dist: `--5.91%`)
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
| `5m` | `BALANCED` | 0.00 USD | 1,750.00 USD | 1,750.00 USD | 1,750.00 USD | `1` | `2026-10-29 22:05:00 UTC - 2026-10-29 22:10:00 UTC` |
| `15m` | `BALANCED` | 0.00 USD | 1,750.00 USD | 1,750.00 USD | 1,750.00 USD | `1` | `2026-10-29 22:00:00 UTC - 2026-10-29 22:15:00 UTC` |
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
  * Current Rate: `5.05K` | Last 24h: `33.19K` | Last 3d: `283.86K` | Last 7d: `777.60K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `-0.0019%` | **USDT OKX** | `0.0001%` |
| **USDT Bybit** | `0.0100%` | **USDT KuCoin** | `-0.0061%` |
| **USDT MEXC** | `-0.0018%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `-0.0077%` | **USDT Bitget** | `0.0100%` |
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
| `5:00 UTC` | `1325.25` | `1325.38` | `1325.25` | `1330.65` | `1320.75` | 11,021,893.68 USD | 5,577,839.59 USD | 5,444,054.10 USD | 133,785.49 USD | `+1.21%` | `3B / 1S` |
| `0:00 UTC` | `1294.05` | `1302.04` | `1294.05` | `1328.55` | `1286.25` | 68,949,402.59 USD | 35,232,633.05 USD | 33,716,769.55 USD | 1,515,863.50 USD | `+2.20%` | `6B / 24S` |
| `5:00 UTC` | `1306.05` | `1306.88` | `1306.05` | `1312.05` | `1300.05` | 17,712,248.68 USD | 9,074,345.66 USD | 8,637,903.02 USD | 436,442.64 USD | `+2.46%` | `3B / 5S` |
| `0:00 UTC` | `1249.20` | `1269.32` | `1249.20` | `1308.60` | `1241.40` | 130,590,816.99 USD | 58,796,845.15 USD | 71,793,971.84 USD | -12,997,126.69 USD | `-9.95%` | `4B / 19S` |
| `5:00 UTC` | `1229.25` | `1237.79` | `1229.25` | `1264.35` | `1206.75` | 149,162,484.89 USD | 77,012,548.38 USD | 72,149,936.51 USD | 4,862,611.87 USD | `+3.26%` | `9B / 11S` |
| `0:00 UTC` | `1249.95` | `1248.07` | `1249.95` | `1259.85` | `1233.15` | 61,152,789.32 USD | 32,267,997.87 USD | 28,884,791.45 USD | 3,383,206.41 USD | `+5.53%` | `6B / 4S` |
| `5:00 UTC` | `1273.95` | `1271.85` | `1273.95` | `1286.25` | `1253.25` | 67,607,862.35 USD | 37,234,359.13 USD | 30,373,503.22 USD | 6,860,855.91 USD | `+10.15%` | `6B / 2S` |
| `0:00 UTC` | `1294.65` | `1287.25` | `1294.65` | `1297.05` | `1269.15` | 47,983,765.84 USD | 24,978,907.15 USD | 23,004,858.69 USD | 1,974,048.46 USD | `+4.11%` | `4B / 9S` |
| `5:00 UTC` | `1264.05` | `1267.99` | `1264.05` | `1276.65` | `1260.75` | 31,349,361.20 USD | 15,100,777.24 USD | 16,248,583.96 USD | -1,147,806.72 USD | `-3.66%` | `0B / 1S` |
| `0:00 UTC` | `1261.95` | `1262.96` | `1261.95` | `1269.15` | `1258.95` | 6,881,925.29 USD | 3,378,791.27 USD | 3,503,134.02 USD | -124,342.74 USD | `-1.81%` | `3B / 5S` |

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
| `5m` | -734,770.00 USD | -1,570,000.00 USD | **`DISTRIBUTION`** |
| `15m` | -760,070.00 USD | -4,630,000.00 USD | **`DISTRIBUTION`** |
| `30m` | 619,510.00 USD | -11,580,000.00 USD | **`DISTRIBUTION`** |
| `1h` | 5,590,000.00 USD | 17,350,000.00 USD | **`ACCUMULATION`** |
| `2h` | -8,370,000.00 USD | 2,350,000.00 USD | **`DISTRIBUTION`** |
| `4h` | -10,420,000.00 USD | -16,670,000.00 USD | **`DISTRIBUTION`** |
| `6h` | 7,110,000.00 USD | -4,400,000.00 USD | **`ACCUMULATION`** |
| `8h` | 17,010,000.00 USD | 83,400,000.00 USD | **`ACCUMULATION`** |
| `12h` | 21,840,000.00 USD | 93,760,000.00 USD | **`ACCUMULATION`** |
| `24h` | 2,680,000.00 USD | 58,330,000.00 USD | **`ACCUMULATION`** |
| `1w` | 35,580,000.00 USD | 244,880,000.00 USD | **`ACCUMULATION`** |
| `30d` | 57,860,000.00 USD | -543,320,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-734.77K` | 15m=`-760.07K` | 1h=`+5.59M` | 24h=`+2.68M`
* Futures Capital Netflows: 5m=`-1.57M` | 15m=`-4.63M` | 1h=`+17.35M` | 24h=`+58.33M`
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
  * `2026-10-30 03:29:54 IST`: [investinglive.com] - (Sentiment: `Neutral`)
  * `2026-10-30 02:53:54 IST`: [msn.com] - (Sentiment: `Neutral`)
  * `2026-10-30 03:30:54 IST`: [morningstar.com] - (Sentiment: `Neutral`)
  * `2026-10-30 03:30:54 IST`: [sec.gov] - (Sentiment: `Neutral`)
  * `2026-10-30 03:29:54 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 03:29:54 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 00:31:54 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:31:54 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:31:54 IST`: [@DeItaone] - (Sentiment: `Neutral`)
  * `2026-10-29 23:31:54 IST`: [@mb_ghalibaf] - (Sentiment: `Neutral`)
  * `2026-10-29 23:31:54 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-29 23:31:54 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-29 23:31:54 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:31:54 IST`: [fxstreet.com] - (Sentiment: `Neutral`)
  * `2026-10-29 21:31:54 IST`: [ForexFactory] - (Sentiment: `Neutral`)


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
  * Execution Entry: `1259.96` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `1231.54` (Risk Distance: `28.42` pts)
  * +2.5R Take Profit: `1331.01`
  * Mathematical Lot Sizing: **`0.35 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `1285.20` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `1313.62` (Risk Distance: `28.42` pts)
  * +2.5R Take Profit: `1214.15`
  * Mathematical Lot Sizing: **`0.35 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`1264.99`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
