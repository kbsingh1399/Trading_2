# 🏛️ SOVEREIGN CANDIDATE DOSSIER: ZECUSD
**Canonical Key**: `ZECUSD` | **Broker Instrument**: `ZECUSD.p` | **Asset Class**: `Crypto Altcoin`
**Timestamp**: `2026-10-29 22:45:59 IST` (`2026-10-29 17:15:59 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `1350.69` | **Live Ask Quote**: `1351.36` | **Mid Price**: `1351.03`
- **Spread Points**: `67.00` | **Spread BPS**: `4.96 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `1273.16` | VWAP Z-Score: `+2.01` (Regime: `STRETCH_EXTREME`)
  * 14-Period ATR: `18.12` (Volatility Regime: `HIGH_EXPANSION`)
  * 14-Period RSI: `65.92` (State: `OVERBOUGHT`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `1380.24` | Lower -3.00σ Band: `1166.07`
  * Upper +2.51σ Band: `1362.75` | Lower -2.51σ Band: `1183.56`
  * Upper +2.01σ Band: `1344.90` | Lower -2.01σ Band: `1201.41`
  * Upper +2.00σ Band: `1344.55` | Lower -2.00σ Band: `1201.76`
  * Upper +1.28σ Band: `1318.85` | Lower -1.28σ Band: `1227.47`
  * Upper +1.00σ Band: `1308.85` | Lower -1.00σ Band: `1237.46`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`1337.87` | EMA-20=`1314.35` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`1288.91` (Slope: `+0.0000`) | EMA-100=`1281.96`
  * Institutional Anchors: EMA-144=`1279.14` | EMA-200=`1274.80` (Slope: `+0.5302`) | EMA-233=`1272.69`
- **Range Boundaries**: 24H High=`1396.49` | 24H Low=`1230.00` | Weekly High=`1396.49` | Weekly Low=`1210.62`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `1299.37` (Distance: `+4.20%`)
  * Point of Control (POC) = `1247.20` (Distance: `+8.56%`)
  * Value Area Low (VAL) = `1230.55` (Distance: `+10.03%`)
  * Auction Positioning: `ABOVE_VALUE (Imbalance)` | Session Bias: **`BULLISH (Above Pivot)`** | Market Regime: `TREND_UP_ACCEPTANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`1320.44` | POC=`1312.10` | VAL=`1285.78`
  * Prior Day Extremes: PDH=`1328.99` | PDL=`1263.19` | PDC=`1296.46`
  * Monday Range Blueprint: High=`1267.53` | Mid=`1222.14` | Low=`1176.75`
  * Developing Weekly Value Area: Weekly VAH=`1293.21` | Weekly POC=`1239.01` | Weekly VAL=`1195.06`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`1318.68` | Low=`1230.00`
  * London Session (08:00-16:00 UTC): High=`1276.13` | Low=`1233.52`
  * New York Session (13:00-21:00 UTC): High=`1396.49` | Low=`1250.65`
  * Initial Balance (First Hour): IB High=`1255.79` | IB Low=`1245.43`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `1345.62` - `1356.43`
  * Optimal Trade Entry (OTE 0.705): `1353.73`
  * Structural Invalidation Anchor (0.786): `1361.83`

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
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-29 22:44:58 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `16` | `0xb83d...6e36` | `SHORT` | 70,660,390.38 USD | `52,582.52` | `1336.45` | `1344.30` | `3622.84` | -386,475.48 USD | `-0.55%` | `3X Cross` |
| `22` | `0x5b5d...c060` | `SHORT` | 54,728,972.20 USD | `40,727.61` | `1478.36` | `1344.30` | `4869.66` | 5,481,291.99 USD | `+10.02%` | `3X Cross` |
| `42` | `0x7fda...17d1` | `SHORT` | 30,070,100.99 USD | `22,377.24` | `1260.93` | `1344.30` | `2925.04` | -1,854,048.65 USD | `-6.17%` | `5X Cross` |
| `81` | `0x60b0...991e` | `LONG` | 22,578,818.14 USD | `16,779.74` | `1179.65` | `1344.30` | `868.08` | 2,784,571.13 USD | `+12.33%` | `10X Cross` |
| `86` | `0xbf73...5d58` | `LONG` | 21,488,000.00 USD | `16,000.00` | `1214.30` | `1344.30` | `700.64` | 2,059,167.75 USD | `+9.58%` | `10X Cross` |
| `132` | `0xc36a...105b` | `LONG` | 15,465,937.75 USD | `11,510.82` | `1215.14` | `1344.30` | `918.12` | 1,478,656.72 USD | `+9.56%` | `10X Cross` |
| `172` | `0x8742...8427` | `LONG` | 12,373,787.21 USD | `9,201.21` | `1286.37` | `1344.30` | `698.32` | 537,617.21 USD | `+4.34%` | `10X Cross` |
| `198` | `0xad59...ba81` | `SHORT` | 11,315,617.50 USD | `8,425.00` | `330.91` | `1344.30` | `2136.96` | -8,527,659.73 USD | `-75.36%` | `10X Cross` |
| `202` | `0xdd53...2b13` | `SHORT` | 11,063,513.13 USD | `8,237.91` | `739.37` | `1344.30` | `7584.05` | -4,972,626.10 USD | `-44.95%` | `3X Cross` |
| `208` | `0x9ffd...ce40` | `LONG` | 10,902,200.85 USD | `8,120.82` | `1249.23` | `1344.30` | `559.09` | 757,424.55 USD | `+6.95%` | `5X Cross` |
| `211` | `0xfc66...ca06` | `SHORT` | 10,787,260.43 USD | `8,027.43` | `1319.26` | `1344.30` | `5377.45` | -196,994.04 USD | `-1.83%` | `10X Cross` |
| `223` | `0x880a...311c` | `SHORT` | 10,355,273.00 USD | `7,707.11` | `1367.50` | `1344.30` | `2290.41` | 184,211.21 USD | `+1.78%` | `10X Cross` |
| `271` | `0x2b61...2f6c` | `LONG` | 9,145,885.20 USD | `6,807.00` | `1453.56` | `1344.30` | `656.62` | -748,466.02 USD | `-8.18%` | `10X Cross` |
| `288` | `0x2ae5...83e7` | `LONG` | 8,658,783.36 USD | `6,436.80` | `1391.82` | `1344.30` | `0.000000` | -300,108.63 USD | `-3.47%` | `2X Cross` |
| `319` | `0xecb6...2b00` | `SHORT` | 7,975,915.69 USD | `5,935.43` | `1323.70` | `1344.30` | `6596.69` | -119,207.93 USD | `-1.49%` | `5X Cross` |
| `337` | `0x26b6...9a13` | `LONG` | 7,316,517.45 USD | `5,433.73` | `1282.23` | `1344.30` | `190.54` | 349,214.21 USD | `+4.77%` | `10X Cross` |
| `346` | `0x45d2...4029` | `SHORT` | 7,031,360.40 USD | `5,227.00` | `833.44` | `1344.30` | `7645.15` | -2,674,982.43 USD | `-38.04%` | `5X Cross` |
| `368` | `0x469e...58a5` | `SHORT` | 6,723,000.00 USD | `5,000.00` | `1190.36` | `1344.30` | `1803.78` | -771,215.10 USD | `-11.47%` | `10X Cross` |
| `370` | `0xea00...a918` | `LONG` | 6,715,000.00 USD | `5,000.00` | `739.16` | `1344.30` | `0.000000` | 3,019,184.89 USD | `+44.96%` | `5X Cross` |
| `381` | `0xdd7a...8830` | `LONG` | 6,531,123.32 USD | `4,860.19` | `897.48` | `1344.30` | `787.40` | 2,169,219.65 USD | `+33.21%` | `10X Cross` |
| `391` | `0xf081...e39e` | `LONG` | 6,337,761.20 USD | `4,717.00` | `1195.70` | `1344.30` | `1200.06` | 697,637.16 USD | `+11.01%` | `10X Cross` |
| `447` | `0x382b...3e39` | `LONG` | 5,417,478.36 USD | `4,031.52` | `1166.42` | `1344.30` | `4.76` | 715,050.89 USD | `+13.20%` | `10X Cross` |
| `449` | `0x4cae...7c34` | `LONG` | 5,383,461.58 USD | `4,004.36` | `999.34` | `1344.30` | `657.88` | 1,381,733.43 USD | `+25.67%` | `10X Cross` |
| `462` | `0xa61c...66b9` | `LONG` | 5,224,618.97 USD | `3,888.00` | `1148.34` | `1344.30` | `0.000000` | 759,876.83 USD | `+14.54%` | `10X Cross` |
| `483` | `0x9aa5...58af` | `SHORT` | 4,998,608.52 USD | `3,720.31` | `1205.51` | `1344.30` | `3224.62` | -513,721.72 USD | `-10.28%` | `10X Cross` |
| `484` | `0x0153...8052` | `SHORT` | 4,974,052.10 USD | `3,698.18` | `1307.82` | `1344.30` | `2504.65` | -137,481.35 USD | `-2.76%` | `1X Isolated` |
| `517` | `0xd4c1...3d1d` | `SHORT` | 4,655,781.08 USD | `3,465.67` | `1302.88` | `1344.30` | `2577.04` | -140,430.26 USD | `-3.02%` | `10X Cross` |
| `544` | `0xd21d...90f1` | `LONG` | 4,365,075.00 USD | `3,250.00` | `1253.64` | `1344.30` | `875.85` | 290,733.27 USD | `+6.66%` | `4X Isolated` |
| `559` | `0x1338...c48e` | `LONG` | 4,231,574.15 USD | `3,149.43` | `1018.52` | `1344.30` | `820.14` | 1,023,828.61 USD | `+24.19%` | `4X Isolated` |
| `567` | `0x456f...cdf1` | `LONG` | 4,182,530.06 USD | `3,111.77` | `1267.78` | `1344.30` | `486.74` | 237,491.73 USD | `+5.68%` | `10X Cross` |
| `575` | `0xdbe0...d6d5` | `LONG` | 4,149,822.65 USD | `3,085.37` | `422.97` | `1344.30` | `338.46` | 2,844,818.16 USD | `+68.55%` | `3X Isolated` |
| `593` | `0x9c06...0560` | `SHORT` | 4,018,590.18 USD | `2,989.80` | `786.00` | `1344.30` | `2325.40` | -1,668,595.18 USD | `-41.52%` | `10X Cross` |
| `631` | `0x27c9...d65d` | `SHORT` | 3,799,055.25 USD | `2,827.73` | `1245.62` | `1344.30` | `1794.26` | -276,791.40 USD | `-7.29%` | `10X Cross` |
| `693` | `0xac48...3201` | `LONG` | 3,415,179.32 USD | `2,540.30` | `1393.86` | `1344.30` | `525.97` | -125,649.97 USD | `-3.68%` | `10X Cross` |
| `697` | `0xa183...0482` | `LONG` | 3,402,908.60 USD | `2,534.00` | `530.25` | `1344.30` | `444.38` | 2,059,245.88 USD | `+60.51%` | `5X Isolated` |
| `705` | `0x325e...9564` | `LONG` | 3,362,018.12 USD | `2,501.91` | `1306.24` | `1344.30` | `0.000000` | 93,924.22 USD | `+2.79%` | `10X Cross` |
| `706` | `0x0871...e927` | `LONG` | 3,361,500.00 USD | `2,500.00` | `1276.50` | `1344.30` | `0.000000` | 170,250.00 USD | `+5.06%` | `10X Cross` |
| `718` | `0x9b86...6e6e` | `LONG` | 3,313,830.63 USD | `2,467.30` | `637.58` | `1344.30` | `889.61` | 1,740,731.03 USD | `+52.53%` | `3X Cross` |
| `767` | `0xb2f7...af9f` | `SHORT` | 3,107,557.33 USD | `2,313.72` | `746.63` | `1344.30` | `4155.18` | -1,380,068.59 USD | `-44.41%` | `10X Cross` |
| `800` | `0xf48f...10fe` | `LONG` | 2,981,206.86 USD | `2,218.49` | `1517.87` | `1344.30` | `867.13` | -386,179.96 USD | `-12.95%` | `3X Cross` |
| `817` | `0x2e30...4cb5` | `SHORT` | 2,913,408.58 USD | `2,163.69` | `1293.44` | `1344.30` | `3407.39` | -114,798.20 USD | `-3.94%` | `2X Cross` |
| `834` | `0x5bc4...3b0c` | `SHORT` | 2,861,583.82 USD | `2,130.74` | `1089.65` | `1344.30` | `3525.71` | -539,826.24 USD | `-18.86%` | `5X Cross` |
| `848` | `0x71d0...8c26` | `SHORT` | 2,802,441.00 USD | `2,085.49` | `1362.27` | `1344.30` | `5006.25` | 38,559.61 USD | `+1.38%` | `10X Cross` |
| `852` | `0x4fe2...ac59` | `SHORT` | 2,785,225.87 USD | `2,071.57` | `1478.56` | `1344.30` | `1788.62` | 277,720.35 USD | `+9.97%` | `10X Cross` |
| `854` | `0x4e23...20c3` | `LONG` | 2,774,953.91 USD | `2,065.62` | `1302.47` | `1344.30` | `0.000000` | 84,543.16 USD | `+3.05%` | `4X Cross` |
| `875` | `0x668c...ea2e` | `SHORT` | 2,688,800.00 USD | `2,000.00` | `1409.16` | `1344.30` | `2701.40` | 129,522.04 USD | `+4.82%` | `10X Cross` |
| `876` | `0x362a...1d9f` | `SHORT` | 2,686,165.43 USD | `1,999.23` | `1382.50` | `1344.30` | `1677.92` | 77,771.97 USD | `+2.90%` | `5X Cross` |
| `895` | `0x77ee...2902` | `SHORT` | 2,614,685.91 USD | `1,946.03` | `759.84` | `1344.30` | `5283.80` | -1,136,008.40 USD | `-43.45%` | `10X Cross` |
| `905` | `0x3e2f...b269` | `SHORT` | 2,585,959.93 USD | `1,925.51` | `1134.87` | `1344.30` | `2931.71` | -400,761.07 USD | `-15.50%` | `10X Cross` |
| `909` | `0xe097...d0fe` | `LONG` | 2,572,207.35 USD | `1,913.56` | `1261.17` | `1344.30` | `0.000000` | 158,881.19 USD | `+6.18%` | `10X Cross` |
| `919` | `0x4f12...618b` | `SHORT` | 2,549,358.83 USD | `1,896.28` | `1608.30` | `1344.30` | `2116.67` | 500,425.56 USD | `+19.63%` | `3X Cross` |
| `961` | `0x866d...d6e1` | `LONG` | 2,421,234.38 USD | `1,802.05` | `674.73` | `1344.30` | `32.19` | 1,205,333.07 USD | `+49.78%` | `10X Cross` |
| `991` | `0x2309...a2d9` | `LONG` | 2,351,797.13 USD | `1,750.37` | `1186.09` | `1344.30` | `799.36` | 275,703.02 USD | `+11.72%` | `8X Cross` |
| `1019` | `0x2edd...8179` | `SHORT` | 2,279,307.22 USD | `1,696.19` | `1259.73` | `1344.30` | `2902.97` | -142,574.02 USD | `-6.26%` | `10X Cross` |
| `1038` | `0x265e...7f70` | `LONG` | 2,218,286.82 USD | `1,651.74` | `1388.09` | `1344.30` | `0.000000` | -74,482.87 USD | `-3.36%` | `3X Cross` |
| `1039` | `0x023a...2355` | `SHORT` | 2,217,130.49 USD | `1,649.92` | `1310.62` | `1344.30` | `6449.08` | -54,719.01 USD | `-2.47%` | `10X Cross` |
| `1047` | `0xa271...a3f7` | `LONG` | 2,193,457.63 USD | `1,631.43` | `1190.60` | `1344.30` | `910.24` | 251,075.83 USD | `+11.45%` | `4X Cross` |
| `1057` | `0x7f75...9edf` | `LONG` | 2,158,328.90 USD | `1,605.78` | `1199.97` | `1344.30` | `974.81` | 231,437.01 USD | `+10.72%` | `10X Cross` |
| `1059` | `0x6646...6de5` | `SHORT` | 2,150,720.00 USD | `1,600.00` | `660.64` | `1344.30` | `4936.10` | -1,093,695.03 USD | `-50.85%` | `10X Cross` |
| `1074` | `0xdf57...93f5` | `LONG` | 2,121,617.68 USD | `1,579.76` | `1218.38` | `1344.30` | `780.08` | 196,861.70 USD | `+9.28%` | `3X Isolated` |
| `1087` | `0xab59...59b5` | `LONG` | 2,102,381.29 USD | `1,565.32` | `1342.15` | `1344.30` | `777.66` | 1,486.07 USD | `+0.07%` | `10X Cross` |
| `1093` | `0xfe7c...b7ae` | `SHORT` | 2,095,952.95 USD | `1,560.65` | `1350.64` | `1344.30` | `6149.86` | 11,920.80 USD | `+0.57%` | `10X Cross` |
| `1097` | `0x634f...6951` | `LONG` | 2,086,766.10 USD | `1,553.00` | `1263.46` | `1344.30` | `1184.28` | 124,616.52 USD | `+5.97%` | `10X Cross` |
| `1104` | `0x3e47...aaf6` | `LONG` | 2,063,377.67 USD | `1,536.28` | `1277.06` | `1344.30` | `1007.77` | 101,455.58 USD | `+4.92%` | `10X Cross` |
| `1136` | `0xcf67...eb24` | `LONG` | 2,016,600.00 USD | `1,500.00` | `887.05` | `1344.30` | `463.55` | 686,028.63 USD | `+34.02%` | `10X Cross` |
| `1157` | `0x039c...0ebd` | `SHORT` | 1,989,482.46 USD | `1,480.49` | `1238.67` | `1344.30` | `3095.61` | -155,651.14 USD | `-7.82%` | `10X Cross` |
| `1219` | `0x5323...b23c` | `SHORT` | 1,917,145.71 USD | `1,426.66` | `1360.26` | `1344.30` | `5255.66` | 23,483.93 USD | `+1.22%` | `5X Cross` |
| `1226` | `0x7a76...b16d` | `LONG` | 1,902,363.91 USD | `1,415.66` | `1362.09` | `1344.30` | `1253.60` | -25,891.35 USD | `-1.36%` | `10X Cross` |
| `1241` | `0x2ab7...c2f8` | `LONG` | 1,883,545.90 USD | `1,400.51` | `813.26` | `1344.30` | `787.33` | 744,564.21 USD | `+39.53%` | `3X Cross` |
| `1242` | `0x9546...181c` | `LONG` | 1,883,168.30 USD | `1,400.75` | `1348.55` | `1344.30` | `0.000000` | -5,819.27 USD | `-0.31%` | `10X Cross` |
| `1262` | `0x11be...8b1d` | `LONG` | 1,849,253.10 USD | `1,375.83` | `1206.55` | `1344.30` | `1134.36` | 189,245.15 USD | `+10.23%` | `10X Isolated` |
| `1320` | `0xef96...9383` | `SHORT` | 1,757,745.26 USD | `1,308.82` | `1249.96` | `1344.30` | `4043.14` | -121,778.84 USD | `-6.93%` | `10X Cross` |
| `1339` | `0xfc27...9d9d` | `SHORT` | 1,726,610.26 USD | `1,284.89` | `1314.81` | `1344.30` | `11915.75` | -37,220.15 USD | `-2.16%` | `10X Cross` |
| `1361` | `0xe065...0f85` | `SHORT` | 1,695,685.23 USD | `1,262.61` | `1087.02` | `1344.30` | `1600.42` | -323,209.10 USD | `-19.06%` | `10X Cross` |
| `1374` | `0xdf83...3cff` | `SHORT` | 1,680,663.78 USD | `1,250.68` | `1239.56` | `1344.30` | `1885.35` | -130,376.10 USD | `-7.76%` | `10X Cross` |
| `1384` | `0x7277...0b98` | `SHORT` | 1,658,551.28 USD | `1,234.96` | `1298.48` | `1344.30` | `2336.32` | -54,981.86 USD | `-3.32%` | `10X Cross` |
| `1441` | `0x5975...9abd` | `LONG` | 1,612,920.00 USD | `1,200.00` | `1179.54` | `1344.30` | `258.72` | 197,477.21 USD | `+12.24%` | `5X Cross` |
| `1479` | `0x69cc...14fd` | `SHORT` | 1,560,287.16 USD | `1,161.36` | `675.33` | `1344.30` | `7677.73` | -775,981.63 USD | `-49.73%` | `10X Cross` |
| `1494` | `0x3fc5...c0c1` | `SHORT` | 1,542,929.14 USD | `1,148.44` | `1264.34` | `1344.30` | `2970.87` | -90,915.36 USD | `-5.89%` | `10X Cross` |
| `1522` | `0x5f94...4b96` | `LONG` | 1,497,919.14 USD | `1,115.27` | `538.00` | `1344.30` | `0.000000` | 897,901.50 USD | `+59.94%` | `10X Cross` |
| `1540` | `0x71df...a23d` | `SHORT` | 1,476,527.63 USD | `1,098.28` | `513.50` | `1344.30` | `2543.17` | -912,557.44 USD | `-61.80%` | `2X Cross` |
| `1574` | `0xbfc7...80b4` | `SHORT` | 1,444,370.00 USD | `1,075.00` | `558.03` | `1344.30` | `5142.11` | -844,491.27 USD | `-58.47%` | `10X Cross` |
| `1618` | `0x51f6...2b39` | `SHORT` | 1,397,078.78 USD | `1,039.88` | `1302.72` | `1344.30` | `2850.15` | -42,401.97 USD | `-3.04%` | `10X Cross` |
| `1650` | `0x123d...3bff` | `SHORT` | 1,354,852.65 USD | `1,007.70` | `488.87` | `1344.30` | `4121.45` | -862,217.53 USD | `-63.64%` | `10X Cross` |
| `1656` | `0xb5ff...d912` | `LONG` | 1,345,200.00 USD | `1,000.00` | `1141.93` | `1344.30` | `400.40` | 203,269.70 USD | `+15.11%` | `2X Cross` |
| `1657` | `0x0748...d4b2` | `LONG` | 1,344,800.00 USD | `1,000.00` | `1334.09` | `1344.30` | `0.000000` | 10,711.70 USD | `+0.80%` | `7X Cross` |
| `1658` | `0x266b...efcb` | `LONG` | 1,344,200.00 USD | `1,000.00` | `826.11` | `1344.30` | `119.89` | 518,087.07 USD | `+38.54%` | `10X Cross` |
| `1660` | `0xe282...df29` | `LONG` | 1,343,780.60 USD | `1,000.00` | `420.99` | `1344.30` | `79.22` | 922,793.74 USD | `+68.67%` | `10X Cross` |
| `1684` | `0x17f0...094f` | `LONG` | 1,322,505.48 USD | `984.30` | `1287.23` | `1344.30` | `536.71` | 55,485.32 USD | `+4.20%` | `5X Cross` |
| `1756` | `0x757d...94ba` | `LONG` | 1,242,275.00 USD | `925.00` | `1558.31` | `1344.30` | `0.000000` | -199,165.58 USD | `-16.03%` | `10X Cross` |
| `1760` | `0x5d90...eea3` | `LONG` | 1,237,269.46 USD | `920.93` | `1288.61` | `1344.30` | `904.51` | 50,552.21 USD | `+4.09%` | `3X Isolated` |
| `1771` | `0x3205...40bb` | `SHORT` | 1,227,019.50 USD | `913.11` | `1342.82` | `1344.30` | `2721.51` | -874.26 USD | `-0.07%` | `10X Cross` |
| `1825` | `0xf096...7553` | `SHORT` | 1,184,510.51 USD | `881.07` | `1240.34` | `1344.30` | `3452.10` | -91,680.42 USD | `-7.74%` | `10X Cross` |
| `1828` | `0xdf95...7d72` | `SHORT` | 1,182,459.74 USD | `879.95` | `1073.66` | `1344.30` | `40388.48` | -237,692.74 USD | `-20.10%` | `10X Cross` |
| `1842` | `0xcf0a...856f` | `LONG` | 1,171,174.06 USD | `871.15` | `1292.19` | `1344.30` | `938.42` | 45,479.21 USD | `+3.88%` | `4X Cross` |
| `1862` | `0x2847...d47b` | `LONG` | 1,153,139.49 USD | `858.31` | `1234.83` | `1344.30` | `0.000000` | 93,273.73 USD | `+8.09%` | `5X Cross` |
| `1882` | `0x7d0f...ea35` | `LONG` | 1,141,550.00 USD | `850.00` | `1317.57` | `1344.30` | `1275.59` | 21,614.42 USD | `+1.89%` | `10X Cross` |
| `1888` | `0xe35c...a1d3` | `LONG` | 1,134,916.78 USD | `844.57` | `1306.64` | `1344.30` | `688.39` | 31,368.02 USD | `+2.76%` | `2X Isolated` |
| `1911` | `0x601c...4f54` | `SHORT` | 1,108,432.69 USD | `824.42` | `615.11` | `1344.30` | `2885.23` | -601,319.94 USD | `-54.25%` | `5X Cross` |
| `1921` | `0xae55...2236` | `LONG` | 1,099,660.64 USD | `817.47` | `1467.80` | `1344.30` | `0.000000` | -100,220.57 USD | `-9.11%` | `10X Cross` |
| `1931` | `0x71b1...79c8` | `LONG` | 1,091,539.37 USD | `812.52` | `1231.55` | `1344.30` | `651.23` | 90,883.91 USD | `+8.33%` | `10X Cross` |
| `1954` | `0x9b0f...db40` | `LONG` | 1,076,000.00 USD | `800.00` | `1268.86` | `1344.30` | `772.33` | 60,910.24 USD | `+5.66%` | `10X Cross` |
| `1955` | `0x0f02...5384` | `LONG` | 1,075,847.93 USD | `800.78` | `1290.36` | `1344.30` | `277.94` | 42,553.86 USD | `+3.96%` | `3X Cross` |
| `1972` | `0xabdb...84ac` | `LONG` | 1,066,401.88 USD | `793.69` | `711.79` | `1344.30` | `664.28` | 501,461.52 USD | `+47.02%` | `3X Cross` |
| `1978` | `0xfdf8...e381` | `LONG` | 1,060,904.43 USD | `790.01` | `1337.72` | `1344.30` | `153.74` | 4,094.74 USD | `+0.39%` | `10X Cross` |
| `2018` | `0x0c1f...1d39` | `SHORT` | 1,025,077.06 USD | `762.99` | `1299.17` | `1344.30` | `4588.81` | -33,825.98 USD | `-3.30%` | `10X Cross` |
| `2020` | `0xf6f3...47f8` | `SHORT` | 1,024,159.34 USD | `761.57` | `1253.10` | `1344.30` | `2296.68` | -69,836.34 USD | `-6.82%` | `5X Cross` |
| `2030` | `0x38f9...cb04` | `SHORT` | 1,015,548.75 USD | `755.74` | `1344.43` | `1344.30` | `2360.26` | 493.04 USD | `+0.05%` | `10X Cross` |
| `2047` | `0xadd1...5e0d` | `LONG` | 1,009,133.53 USD | `750.62` | `1195.15` | `1344.30` | `0.000000` | 112,032.43 USD | `+11.10%` | `10X Cross` |
| `2061` | `0xd6e1...f256` | `SHORT` | 1,003,718.38 USD | `746.37` | `1368.65` | `1344.30` | `2025.11` | 17,797.41 USD | `+1.77%` | `10X Cross` |
| `2068` | `0x87a7...9fa2` | `SHORT` | 1,000,045.40 USD | `744.58` | `1464.55` | `1344.30` | `1706.30` | 90,431.35 USD | `+9.04%` | `10X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `1304.60` | 10,019.33 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Long: 10.02K USD at 1304.6000 USD [API] | `2026-10-27 16:27:21` |
| `ANNOUNCEMENT` | `INFO` | `1289.60` | 10,407.07 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Long: 10.41K USD at 1289.6000 USD [API] | `2026-10-27 15:20:59` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`1288.96` (Vol: 1,400,000.00 USD, Dist: `+0.78%`) | Long MP=`1243.06` (Vol: 1,400,000.00 USD, Dist: `--2.81%`)
  * 48H Horizon: Short MP=`1332.96` (Vol: 2,800,000.00 USD, Dist: `+4.22%`) | Long MP=`1243.86` (Vol: 1,400,000.00 USD, Dist: `--2.74%`)
  * 3D Horizon: Short MP=`1332.46` (Vol: 2,200,000.00 USD, Dist: `+4.18%`) | Long MP=`1199.86` (Vol: 1,800,000.00 USD, Dist: `--6.18%`)
  * 7D Horizon: Short MP=`1333.81` (Vol: 3,100,000.00 USD, Dist: `+4.29%`) | Long MP=`1228.42` (Vol: 2,600,000.00 USD, Dist: `--3.95%`)
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
  * Current Rate: `70.34K` | Last 24h: `32.07K` | Last 3d: `282.84K` | Last 7d: `777.72K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0072%` | **USDT OKX** | `0.0061%` |
| **USDT Bybit** | `0.0100%` | **USDT KuCoin** | `0.0089%` |
| **USDT MEXC** | `0.0070%` | **USDT BingX** | `0.0021%` |
| **USDT Gate** | `0.0100%` | **USDT Bitget** | `0.0032%` |
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
| `5:00 UTC` | `1309.95` | `1301.15` | `1309.95` | `1310.55` | `1290.15` | 39,138,254.95 USD | 17,154,217.83 USD | 21,984,037.12 USD | -4,829,819.29 USD | `-12.34%` | `2B / 6S` |
| `0:00 UTC` | `1320.15` | `1314.27` | `1320.15` | `1324.95` | `1296.75` | 56,796,886.08 USD | 33,062,545.27 USD | 23,734,340.81 USD | 9,328,204.46 USD | `+16.42%` | `18B / 3S` |
| `5:00 UTC` | `1317.75` | `1318.00` | `1317.75` | `1324.05` | `1313.25` | 29,849,949.75 USD | 16,298,218.14 USD | 13,551,731.61 USD | 2,746,486.54 USD | `+9.20%` | `4B / 2S` |
| `0:00 UTC` | `1345.05` | `1339.86` | `1345.05` | `1353.45` | `1318.65` | 81,702,422.73 USD | 46,151,799.06 USD | 35,550,623.66 USD | 10,601,175.40 USD | `+12.98%` | `23B / 1S` |
| `5:00 UTC` | `1360.05` | `1349.51` | `1360.05` | `1362.15` | `1334.25` | 65,905,391.58 USD | 39,286,823.07 USD | 26,618,568.52 USD | 12,668,254.55 USD | `+19.22%` | `19B / 3S` |
| `0:00 UTC` | `1369.95` | `1375.81` | `1369.95` | `1397.55` | `1350.75` | 159,915,504.01 USD | 87,974,917.65 USD | 71,940,586.35 USD | 16,034,331.30 USD | `+10.03%` | `21B / 3S` |
| `5:00 UTC` | `1359.75` | `1358.32` | `1359.75` | `1373.25` | `1346.25` | 77,512,400.13 USD | 36,921,415.88 USD | 40,590,984.25 USD | -3,669,568.36 USD | `-4.73%` | `4B / 13S` |
| `0:00 UTC` | `1353.15` | `1350.71` | `1353.15` | `1361.25` | `1341.75` | 52,010,841.39 USD | 26,247,439.78 USD | 25,763,401.61 USD | 484,038.17 USD | `+0.93%` | `5B / 3S` |
| `5:00 UTC` | `1343.25` | `1344.85` | `1343.25` | `1353.45` | `1340.25` | 26,552,172.39 USD | 11,915,117.49 USD | 14,637,054.90 USD | -2,721,937.40 USD | `-10.25%` | `0B / 9S` |
| `0:00 UTC` | `1342.95` | `1344.23` | `1342.95` | `1347.45` | `1340.25` | 18,250,378.54 USD | 8,764,785.30 USD | 9,485,593.24 USD | -720,807.94 USD | `-3.95%` | `2B / 3S` |

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
| `5m` | 4,330,000.00 USD | 4,950,000.00 USD | **`ACCUMULATION`** |
| `15m` | 6,170,000.00 USD | 3,250,000.00 USD | **`ACCUMULATION`** |
| `30m` | 5,040,000.00 USD | -441,350.00 USD | **`ACCUMULATION`** |
| `1h` | 3,100,000.00 USD | -1,150,000.00 USD | **`ACCUMULATION`** |
| `2h` | 18,010,000.00 USD | 69,730,000.00 USD | **`ACCUMULATION`** |
| `4h` | 28,930,000.00 USD | 103,570,000.00 USD | **`ACCUMULATION`** |
| `6h` | 31,130,000.00 USD | 113,110,000.00 USD | **`ACCUMULATION`** |
| `8h` | 28,740,000.00 USD | 130,070,000.00 USD | **`ACCUMULATION`** |
| `12h` | 27,610,000.00 USD | 115,540,000.00 USD | **`ACCUMULATION`** |
| `24h` | 18,010,000.00 USD | 127,640,000.00 USD | **`ACCUMULATION`** |
| `1w` | 55,560,000.00 USD | 282,250,000.00 USD | **`ACCUMULATION`** |
| `30d` | 70,940,000.00 USD | -490,340,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+4.33M` | 15m=`+6.17M` | 1h=`+3.10M` | 24h=`+18.01M`
* Futures Capital Netflows: 5m=`+4.95M` | 15m=`+3.25M` | 1h=`-1.15M` | 24h=`+127.64M`
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
  * `2026-10-29 22:05:54 IST`: [fxstreet.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:39:54 IST`: [ForexFactory] - (Sentiment: `Neutral`)
  * `2026-10-29 22:39:54 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-29 22:39:54 IST`: [youtube.com/bankofcanadaofficial] - (Sentiment: `Neutral`)
  * `2026-10-29 22:39:54 IST`: [notayesmanseconomics.wordpress.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:38:54 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:38:54 IST`: [breakingthenews.net] - (Sentiment: `Neutral`)
  * `2026-10-29 22:38:54 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-29 19:40:54 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-29 19:40:54 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-29 19:40:54 IST`: [youtube.com/ecbeuro] - (Sentiment: `Neutral`)
  * `2026-10-29 19:40:54 IST`: [ecb.europa.eu] - (Sentiment: `Neutral`)
  * `2026-10-29 18:40:54 IST`: [zerohedge.com] - (Sentiment: `Neutral`)
  * `2026-10-29 18:40:54 IST`: [dol.gov] - (Sentiment: `Neutral`)
  * `2026-10-29 18:40:54 IST`: [bea.gov] - (Sentiment: `Neutral`)


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
  * Spread-Padded Stop Loss: `1207.81` (Risk Distance: `22.74` pts)
  * +2.5R Take Profit: `1287.41`
  * Mathematical Lot Sizing: **`0.43 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `1299.37` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `1322.11` (Risk Distance: `22.74` pts)
  * +2.5R Take Profit: `1242.51`
  * Mathematical Lot Sizing: **`0.43 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`1361.83`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
