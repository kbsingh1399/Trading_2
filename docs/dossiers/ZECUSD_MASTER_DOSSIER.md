# 🏛️ SOVEREIGN CANDIDATE DOSSIER: ZECUSD
**Canonical Key**: `ZECUSD` | **Broker Instrument**: `ZECUSD.p` | **Asset Class**: `Crypto Altcoin`
**Timestamp**: `2026-10-30 01:14:46 IST` (`2026-10-29 19:44:46 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `1323.59` | **Live Ask Quote**: `1324.62` | **Mid Price**: `1324.11`
- **Spread Points**: `103.00` | **Spread BPS**: `7.78 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `1280.82` | VWAP Z-Score: `+0.99` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `15.41` (Volatility Regime: `HIGH_EXPANSION`)
  * 14-Period RSI: `51.38` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `1397.32` | Lower -3.00σ Band: `1164.32`
  * Upper +2.51σ Band: `1378.29` | Lower -2.51σ Band: `1183.35`
  * Upper +2.01σ Band: `1358.87` | Lower -2.01σ Band: `1202.77`
  * Upper +2.00σ Band: `1358.48` | Lower -2.00σ Band: `1203.16`
  * Upper +1.28σ Band: `1330.52` | Lower -1.28σ Band: `1231.11`
  * Upper +1.00σ Band: `1319.65` | Lower -1.00σ Band: `1241.99`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`1325.40` | EMA-20=`1322.21` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`1301.96` (Slope: `+0.0000`) | EMA-100=`1290.40`
  * Institutional Anchors: EMA-144=`1285.34` | EMA-200=`1280.39` (Slope: `+0.5212`) | EMA-233=`1278.02`
- **Range Boundaries**: 24H High=`1396.49` | 24H Low=`1230.00` | Weekly High=`1396.49` | Weekly Low=`1210.62`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `1308.25` (Distance: `+1.23%`)
  * Point of Control (POC) = `1247.20` (Distance: `+6.19%`)
  * Value Area Low (VAL) = `1230.55` (Distance: `+7.63%`)
  * Auction Positioning: `ABOVE_VALUE (Imbalance)` | Session Bias: **`BULLISH (Above Pivot)`** | Market Regime: `RANGE_EXPANSION`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`1320.44` | POC=`1312.10` | VAL=`1285.78`
  * Prior Day Extremes: PDH=`1328.99` | PDL=`1263.19` | PDC=`1296.46`
  * Monday Range Blueprint: High=`1267.53` | Mid=`1222.14` | Low=`1176.75`
  * Developing Weekly Value Area: Weekly VAH=`1296.14` | Weekly POC=`1239.01` | Weekly VAL=`1195.06`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`1318.68` | Low=`1230.00`
  * London Session (08:00-16:00 UTC): High=`1276.13` | Low=`1233.52`
  * New York Session (13:00-21:00 UTC): High=`1396.49` | Low=`1250.65`
  * Initial Balance (First Hour): IB High=`1255.79` | IB Low=`1245.43`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `1318.81` - `1329.40`
  * Optimal Trade Entry (OTE 0.705): `1326.75`
  * Structural Invalidation Anchor (0.786): `1334.70`

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
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 01:14:07 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `16` | `0xb83d...6e36` | `SHORT` | 69,687,613.76 USD | `52,582.52` | `1336.45` | `1324.90` | `3704.85` | 586,301.14 USD | `+0.84%` | `3X Cross` |
| `23` | `0x5b5d...c060` | `SHORT` | 53,988,519.82 USD | `40,727.61` | `1478.36` | `1324.90` | `4990.19` | 6,221,744.38 USD | `+11.52%` | `3X Cross` |
| `41` | `0x7fda...17d1` | `SHORT` | 29,690,616.51 USD | `22,421.55` | `1261.41` | `1324.90` | `2814.98` | -1,407,753.47 USD | `-4.74%` | `5X Cross` |
| `77` | `0x60b0...991e` | `LONG` | 22,237,301.77 USD | `16,779.74` | `1179.65` | `1324.90` | `889.28` | 2,443,054.76 USD | `+10.99%` | `10X Cross` |
| `82` | `0xbf73...5d58` | `LONG` | 21,200,745.60 USD | `16,000.00` | `1214.30` | `1324.90` | `725.45` | 1,771,913.35 USD | `+8.36%` | `10X Cross` |
| `132` | `0xc36a...105b` | `LONG` | 15,251,020.38 USD | `11,510.82` | `1215.14` | `1324.90` | `932.03` | 1,263,739.36 USD | `+8.29%` | `10X Cross` |
| `169` | `0x8742...8427` | `LONG` | 12,191,603.25 USD | `9,201.21` | `1286.37` | `1324.90` | `698.35` | 355,433.26 USD | `+2.92%` | `10X Cross` |
| `175` | `0x9071...5c0b` | `LONG` | 11,700,553.49 USD | `8,829.94` | `1370.53` | `1324.90` | `579.50` | -401,135.15 USD | `-3.43%` | `2X Cross` |
| `190` | `0xad59...ba81` | `SHORT` | 11,165,652.50 USD | `8,425.00` | `330.91` | `1324.90` | `2140.35` | -8,377,694.73 USD | `-75.03%` | `10X Cross` |
| `199` | `0xdd53...2b13` | `SHORT` | 10,899,675.59 USD | `8,231.14` | `739.37` | `1324.90` | `7871.30` | -4,813,794.11 USD | `-44.16%` | `3X Cross` |
| `201` | `0x9ffd...ce40` | `LONG` | 10,850,034.80 USD | `8,188.42` | `1253.95` | `1324.90` | `568.42` | 582,169.71 USD | `+5.37%` | `5X Cross` |
| `215` | `0xfc66...ca06` | `SHORT` | 10,280,718.02 USD | `7,763.72` | `1319.72` | `1324.90` | `5599.38` | -34,752.94 USD | `-0.34%` | `10X Cross` |
| `221` | `0x880a...311c` | `SHORT` | 10,214,232.88 USD | `7,707.11` | `1367.50` | `1324.90` | `2309.16` | 325,251.32 USD | `+3.18%` | `10X Cross` |
| `268` | `0x2b61...2f6c` | `LONG` | 9,021,317.10 USD | `6,807.00` | `1453.56` | `1324.90` | `640.19` | -873,034.12 USD | `-9.68%` | `10X Cross` |
| `285` | `0x2ae5...83e7` | `LONG` | 8,529,403.68 USD | `6,436.80` | `1391.82` | `1324.90` | `264.91` | -429,488.31 USD | `-5.04%` | `2X Cross` |
| `329` | `0x26b6...9a13` | `LONG` | 7,200,235.62 USD | `5,433.73` | `1282.23` | `1324.90` | `208.05` | 232,932.39 USD | `+3.24%` | `10X Cross` |
| `330` | `0xecb6...2b00` | `SHORT` | 7,197,622.89 USD | `5,435.45` | `1324.05` | `1324.90` | `6122.79` | -801.13 USD | `-0.01%` | `5X Cross` |
| `342` | `0x45d2...4029` | `SHORT` | 6,926,297.70 USD | `5,227.00` | `833.44` | `1324.90` | `8028.45` | -2,569,919.73 USD | `-37.10%` | `5X Cross` |
| `360` | `0xea00...a918` | `LONG` | 6,626,235.50 USD | `5,000.00` | `739.16` | `1324.90` | `0.000000` | 2,930,420.39 USD | `+44.22%` | `5X Cross` |
| `376` | `0xdd7a...8830` | `LONG` | 6,441,209.81 USD | `4,860.19` | `897.48` | `1324.90` | `784.29` | 2,079,306.13 USD | `+32.28%` | `10X Cross` |
| `385` | `0xf081...e39e` | `LONG` | 6,251,440.10 USD | `4,717.00` | `1195.70` | `1324.90` | `1200.09` | 611,316.06 USD | `+9.78%` | `10X Cross` |
| `436` | `0x4cae...7c34` | `LONG` | 5,306,978.31 USD | `4,004.36` | `999.34` | `1324.90` | `757.48` | 1,305,250.15 USD | `+24.59%` | `10X Cross` |
| `448` | `0xa61c...66b9` | `LONG` | 5,153,932.80 USD | `3,888.00` | `1148.34` | `1324.90` | `0.000000` | 689,190.66 USD | `+13.37%` | `10X Cross` |
| `455` | `0x382b...3e39` | `LONG` | 5,097,454.93 USD | `3,849.46` | `1198.83` | `1324.90` | `0.000000` | 482,620.55 USD | `+9.47%` | `10X Cross` |
| `470` | `0x9aa5...58af` | `SHORT` | 4,929,146.98 USD | `3,720.31` | `1205.51` | `1324.90` | `3324.36` | -444,260.18 USD | `-9.01%` | `10X Cross` |
| `475` | `0x0153...8052` | `SHORT` | 4,900,828.14 USD | `3,698.18` | `1307.82` | `1324.90` | `2504.69` | -64,257.39 USD | `-1.31%` | `1X Isolated` |
| `501` | `0xd4c1...3d1d` | `SHORT` | 4,582,954.87 USD | `3,457.79` | `1302.97` | `1324.90` | `2682.26` | -77,542.04 USD | `-1.69%` | `10X Cross` |
| `527` | `0xd21d...90f1` | `LONG` | 4,307,225.00 USD | `3,250.00` | `1253.64` | `1324.90` | `875.88` | 232,883.27 USD | `+5.41%` | `4X Isolated` |
| `547` | `0x1338...c48e` | `LONG` | 4,174,884.41 USD | `3,149.43` | `1018.52` | `1324.90` | `820.17` | 967,138.87 USD | `+23.17%` | `4X Isolated` |
| `550` | `0x456f...cdf1` | `LONG` | 4,153,470.19 USD | `3,134.11` | `1268.52` | `1324.90` | `493.29` | 177,780.55 USD | `+4.28%` | `10X Cross` |
| `560` | `0xdbe0...d6d5` | `LONG` | 4,088,732.32 USD | `3,085.37` | `422.97` | `1324.90` | `338.49` | 2,783,727.83 USD | `+68.08%` | `3X Isolated` |
| `565` | `0x27c9...d65d` | `SHORT` | 4,072,100.39 USD | `3,075.14` | `1252.14` | `1324.90` | `1809.92` | -221,583.88 USD | `-5.44%` | `10X Cross` |
| `586` | `0x9c06...0560` | `SHORT` | 3,961,624.32 USD | `2,989.80` | `786.00` | `1324.90` | `2372.43` | -1,611,629.32 USD | `-40.68%` | `10X Cross` |
| `647` | `0x2e30...4cb5` | `SHORT` | 3,585,286.52 USD | `2,705.06` | `1301.01` | `1324.90` | `2991.25` | -65,989.67 USD | `-1.84%` | `2X Cross` |
| `686` | `0xac48...3201` | `LONG` | 3,366,525.21 USD | `2,540.30` | `1393.86` | `1324.90` | `533.87` | -174,304.08 USD | `-5.18%` | `10X Cross` |
| `689` | `0xa183...0482` | `LONG` | 3,357,550.00 USD | `2,534.00` | `530.25` | `1324.90` | `444.42` | 2,013,887.28 USD | `+59.98%` | `5X Isolated` |
| `696` | `0x325e...9564` | `LONG` | 3,316,531.90 USD | `2,501.91` | `1306.24` | `1324.90` | `0.000000` | 48,437.99 USD | `+1.46%` | `10X Cross` |
| `697` | `0x0871...e927` | `LONG` | 3,313,250.00 USD | `2,500.00` | `1276.50` | `1324.90` | `0.000000` | 122,000.00 USD | `+3.68%` | `10X Cross` |
| `706` | `0x9b86...6e6e` | `LONG` | 3,269,912.69 USD | `2,467.30` | `637.58` | `1324.90` | `889.64` | 1,696,813.09 USD | `+51.89%` | `3X Cross` |
| `768` | `0xb2f7...af9f` | `SHORT` | 3,066,373.12 USD | `2,313.72` | `746.63` | `1324.90` | `4173.78` | -1,338,884.37 USD | `-43.66%` | `10X Cross` |
| `784` | `0x634f...6951` | `LONG` | 3,011,062.39 USD | `2,272.42` | `1281.94` | `1324.90` | `1250.03` | 97,961.93 USD | `+3.25%` | `10X Cross` |
| `800` | `0xf48f...10fe` | `LONG` | 2,940,164.80 USD | `2,218.49` | `1517.87` | `1324.90` | `889.50` | -427,222.03 USD | `-14.53%` | `3X Cross` |
| `825` | `0x5bc4...3b0c` | `SHORT` | 2,823,230.50 USD | `2,130.74` | `1089.65` | `1324.90` | `3563.34` | -501,472.92 USD | `-17.76%` | `5X Cross` |
| `842` | `0x8de4...b9aa` | `SHORT` | 2,771,055.87 USD | `2,091.29` | `1331.35` | `1324.90` | `1689.81` | 13,183.84 USD | `+0.48%` | `3X Cross` |
| `845` | `0x4fe2...ac59` | `SHORT` | 2,745,037.41 USD | `2,071.57` | `1478.56` | `1324.90` | `1815.53` | 317,908.81 USD | `+11.58%` | `10X Cross` |
| `864` | `0x668c...ea2e` | `SHORT` | 2,649,858.20 USD | `2,000.00` | `1406.98` | `1324.90` | `2702.01` | 164,105.79 USD | `+6.19%` | `10X Cross` |
| `890` | `0x77ee...2902` | `SHORT` | 2,579,073.56 USD | `1,946.03` | `759.84` | `1324.90` | `5173.01` | -1,100,396.05 USD | `-42.67%` | `10X Cross` |
| `901` | `0x3e2f...b269` | `SHORT` | 2,551,300.75 USD | `1,925.51` | `1134.87` | `1324.90` | `2931.74` | -366,101.89 USD | `-14.35%` | `10X Cross` |
| `907` | `0xe097...d0fe` | `LONG` | 2,535,658.36 USD | `1,913.56` | `1261.17` | `1324.90` | `0.000000` | 122,332.19 USD | `+4.82%` | `10X Cross` |
| `916` | `0x4f12...618b` | `SHORT` | 2,512,760.63 USD | `1,896.28` | `1608.30` | `1324.90` | `2116.70` | 537,023.76 USD | `+21.37%` | `3X Cross` |
| `957` | `0x866d...d6e1` | `LONG` | 2,388,256.87 USD | `1,802.05` | `674.73` | `1324.90` | `95.33` | 1,172,355.55 USD | `+49.09%` | `10X Cross` |
| `994` | `0x2309...a2d9` | `LONG` | 2,319,116.15 USD | `1,750.37` | `1186.09` | `1324.90` | `805.22` | 243,022.04 USD | `+10.48%` | `8X Cross` |
| `1014` | `0x023a...2355` | `SHORT` | 2,255,417.17 USD | `1,703.23` | `1313.35` | `1324.90` | `6077.00` | -18,478.57 USD | `-0.82%` | `10X Cross` |
| `1017` | `0x2edd...8179` | `SHORT` | 2,244,955.99 USD | `1,695.33` | `1261.35` | `1324.90` | `2984.76` | -106,555.02 USD | `-4.75%` | `10X Cross` |
| `1041` | `0x3e47...aaf6` | `LONG` | 2,168,561.88 USD | `1,636.28` | `1279.54` | `1324.90` | `1037.55` | 74,869.80 USD | `+3.45%` | `10X Cross` |
| `1044` | `0xa271...a3f7` | `LONG` | 2,161,807.89 USD | `1,631.43` | `1190.60` | `1324.90` | `910.27` | 219,426.09 USD | `+10.15%` | `4X Cross` |
| `1054` | `0x7f75...9edf` | `LONG` | 2,127,733.33 USD | `1,605.78` | `1199.97` | `1324.90` | `973.74` | 200,841.44 USD | `+9.44%` | `10X Cross` |
| `1058` | `0x265e...7f70` | `LONG` | 2,122,379.50 USD | `1,601.74` | `1388.09` | `1324.90` | `0.000000` | -100,985.51 USD | `-4.76%` | `3X Cross` |
| `1061` | `0x6646...6de5` | `SHORT` | 2,120,160.00 USD | `1,600.00` | `660.64` | `1324.90` | `4832.20` | -1,063,135.03 USD | `-50.14%` | `10X Cross` |
| `1077` | `0xdf57...93f5` | `LONG` | 2,091,918.19 USD | `1,579.76` | `1218.38` | `1324.90` | `780.12` | 167,162.21 USD | `+7.99%` | `3X Isolated` |
| `1091` | `0xab59...59b5` | `LONG` | 2,074,518.60 USD | `1,565.32` | `1342.15` | `1324.90` | `791.50` | -26,376.62 USD | `-1.27%` | `10X Cross` |
| `1092` | `0xfe7c...b7ae` | `SHORT` | 2,070,685.34 USD | `1,562.49` | `1350.62` | `1324.90` | `6485.09` | 39,643.71 USD | `+1.91%` | `10X Cross` |
| `1150` | `0xcf67...eb24` | `LONG` | 1,987,650.00 USD | `1,500.00` | `887.05` | `1324.90` | `545.65` | 657,078.63 USD | `+33.06%` | `10X Cross` |
| `1173` | `0x039c...0ebd` | `SHORT` | 1,962,093.40 USD | `1,480.49` | `1238.67` | `1324.90` | `3176.95` | -128,262.08 USD | `-6.54%` | `10X Cross` |
| `1201` | `0x71d0...8c26` | `SHORT` | 1,914,504.48 USD | `1,444.80` | `1361.12` | `1324.90` | `6486.15` | 52,041.97 USD | `+2.72%` | `10X Cross` |
| `1245` | `0xfc27...9d9d` | `SHORT` | 1,861,646.24 USD | `1,404.91` | `1317.50` | `1324.90` | `11255.80` | -10,678.28 USD | `-0.57%` | `10X Cross` |
| `1250` | `0x2ab7...c2f8` | `LONG` | 1,856,235.95 USD | `1,400.51` | `813.26` | `1324.90` | `797.05` | 717,254.27 USD | `+38.64%` | `3X Cross` |
| `1263` | `0x11be...8b1d` | `LONG` | 1,823,314.72 USD | `1,375.83` | `1206.55` | `1324.90` | `1134.40` | 163,306.76 USD | `+8.96%` | `10X Isolated` |
| `1311` | `0xdf83...3cff` | `SHORT` | 1,740,026.13 USD | `1,312.93` | `1246.70` | `1324.90` | `1851.27` | -103,195.82 USD | `-5.93%` | `10X Cross` |
| `1319` | `0xef96...9383` | `SHORT` | 1,734,317.38 USD | `1,308.82` | `1249.96` | `1324.90` | `4234.76` | -98,350.96 USD | `-5.67%` | `10X Cross` |
| `1365` | `0xe065...0f85` | `SHORT` | 1,673,084.51 USD | `1,262.61` | `1087.02` | `1324.90` | `1756.52` | -300,608.38 USD | `-17.97%` | `10X Cross` |
| `1391` | `0x7277...0b98` | `SHORT` | 1,635,334.03 USD | `1,234.96` | `1298.48` | `1324.90` | `2361.22` | -31,764.61 USD | `-1.94%` | `10X Cross` |
| `1436` | `0x5975...9abd` | `LONG` | 1,590,296.52 USD | `1,200.00` | `1179.54` | `1324.90` | `360.37` | 174,853.73 USD | `+11.00%` | `5X Cross` |
| `1479` | `0x69cc...14fd` | `SHORT` | 1,537,872.91 USD | `1,161.36` | `675.33` | `1324.90` | `7894.48` | -753,567.38 USD | `-49.00%` | `10X Cross` |
| `1481` | `0x7a76...b16d` | `LONG` | 1,536,380.53 USD | `1,159.27` | `1358.50` | `1324.90` | `1236.42` | -38,487.98 USD | `-2.51%` | `10X Cross` |
| `1494` | `0x3fc5...c0c1` | `SHORT` | 1,522,027.53 USD | `1,148.44` | `1264.34` | `1324.90` | `3086.81` | -70,013.76 USD | `-4.60%` | `10X Cross` |
| `1513` | `0xe35c...a1d3` | `LONG` | 1,494,030.74 USD | `1,127.06` | `1318.20` | `1324.90` | `694.32` | 8,335.39 USD | `+0.56%` | `2X Isolated` |
| `1520` | `0x5f94...4b96` | `LONG` | 1,478,067.33 USD | `1,115.27` | `538.00` | `1324.90` | `0.000000` | 878,049.69 USD | `+59.41%` | `10X Cross` |
| `1539` | `0x71df...a23d` | `SHORT` | 1,455,550.48 USD | `1,098.28` | `513.50` | `1324.90` | `2546.64` | -891,580.29 USD | `-61.25%` | `2X Cross` |
| `1567` | `0xbfc7...80b4` | `SHORT` | 1,424,298.78 USD | `1,075.00` | `558.03` | `1324.90` | `5417.69` | -824,420.06 USD | `-57.88%` | `10X Cross` |
| `1614` | `0x51f6...2b39` | `SHORT` | 1,377,841.00 USD | `1,039.88` | `1302.72` | `1324.90` | `2853.72` | -23,164.19 USD | `-1.68%` | `10X Cross` |
| `1645` | `0x123d...3bff` | `SHORT` | 1,336,047.86 USD | `1,008.15` | `489.25` | `1324.90` | `4203.69` | -842,813.79 USD | `-63.08%` | `10X Cross` |
| `1653` | `0xe282...df29` | `LONG` | 1,325,300.00 USD | `1,000.00` | `420.99` | `1324.90` | `105.38` | 904,313.14 USD | `+68.23%` | `10X Cross` |
| `1654` | `0x266b...efcb` | `LONG` | 1,325,100.00 USD | `1,000.00` | `826.11` | `1324.90` | `157.76` | 498,987.07 USD | `+37.66%` | `10X Cross` |
| `1655` | `0xb5ff...d912` | `LONG` | 1,325,100.00 USD | `1,000.00` | `1141.93` | `1324.90` | `400.44` | 183,169.70 USD | `+13.82%` | `2X Cross` |
| `1656` | `0x0748...d4b2` | `LONG` | 1,325,000.00 USD | `1,000.00` | `1334.09` | `1324.90` | `0.000000` | -9,088.30 USD | `-0.69%` | `7X Cross` |
| `1678` | `0x17f0...094f` | `LONG` | 1,304,492.79 USD | `984.30` | `1287.23` | `1324.90` | `536.75` | 37,472.63 USD | `+2.87%` | `5X Cross` |
| `1751` | `0x757d...94ba` | `LONG` | 1,225,625.00 USD | `925.00` | `1558.31` | `1324.90` | `0.000000` | -215,815.58 USD | `-17.61%` | `10X Cross` |
| `1805` | `0x2847...d47b` | `LONG` | 1,178,084.00 USD | `889.12` | `1238.14` | `1324.90` | `0.000000` | 77,224.84 USD | `+6.56%` | `5X Cross` |
| `1819` | `0xf096...7553` | `SHORT` | 1,167,458.46 USD | `881.07` | `1240.34` | `1324.90` | `3545.45` | -74,628.37 USD | `-6.39%` | `10X Cross` |
| `1821` | `0xdf95...7d72` | `SHORT` | 1,165,706.50 USD | `880.31` | `1073.82` | `1324.90` | `41343.24` | -220,408.20 USD | `-18.91%` | `10X Cross` |
| `1832` | `0xcf0a...856f` | `LONG` | 1,154,314.35 USD | `871.15` | `1292.19` | `1324.90` | `938.45` | 28,619.50 USD | `+2.48%` | `4X Cross` |
| `1863` | `0x7d0f...ea35` | `LONG` | 1,126,289.27 USD | `850.00` | `1317.57` | `1324.90` | `1273.30` | 6,353.69 USD | `+0.56%` | `10X Cross` |
| `1900` | `0x601c...4f54` | `SHORT` | 1,092,851.15 USD | `824.42` | `615.11` | `1324.90` | `2956.12` | -585,738.40 USD | `-53.60%` | `5X Cross` |
| `1908` | `0xae55...2236` | `LONG` | 1,083,229.50 USD | `817.47` | `1467.80` | `1324.90` | `0.000000` | -116,651.72 USD | `-10.77%` | `10X Cross` |
| `1914` | `0x71b1...79c8` | `LONG` | 1,077,076.51 USD | `812.52` | `1231.55` | `1324.90` | `700.25` | 76,421.06 USD | `+7.10%` | `10X Cross` |
| `1935` | `0x0f02...5384` | `LONG` | 1,061,674.12 USD | `800.78` | `1290.36` | `1324.90` | `291.14` | 28,380.06 USD | `+2.67%` | `3X Cross` |
| `1936` | `0x9b0f...db40` | `LONG` | 1,060,320.00 USD | `800.00` | `1268.86` | `1324.90` | `774.02` | 45,230.24 USD | `+4.27%` | `10X Cross` |
| `1948` | `0xabdb...84ac` | `LONG` | 1,051,582.98 USD | `793.69` | `711.79` | `1324.90` | `664.32` | 486,642.62 USD | `+46.28%` | `3X Cross` |
| `1955` | `0xfdf8...e381` | `LONG` | 1,046,763.25 USD | `790.01` | `1337.72` | `1324.90` | `351.01` | -10,046.44 USD | `-0.96%` | `10X Cross` |
| `2015` | `0x0c1f...1d39` | `SHORT` | 1,011,572.14 USD | `762.99` | `1299.17` | `1324.90` | `4898.86` | -20,321.06 USD | `-2.01%` | `10X Cross` |
| `2020` | `0xf6f3...47f8` | `SHORT` | 1,009,461.04 USD | `761.57` | `1253.10` | `1324.90` | `2381.98` | -55,138.04 USD | `-5.46%` | `5X Cross` |
| `2023` | `0x389a...e76b` | `LONG` | 1,007,400.29 USD | `760.13` | `1266.20` | `1324.90` | `358.69` | 44,926.87 USD | `+4.46%` | `10X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `1297.10` | 194.56 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Long: 0.19K USD at 1297.1000 USD [API] | `2026-10-27 15:46:39` |
| `ANNOUNCEMENT` | `INFO` | `1326.30` | 13.26 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Long: 0.01K USD at 1326.3000 USD [API] | `2026-10-27 23:06:56` |
| `ANNOUNCEMENT` | `INFO` | `1326.50` | 11,341.58 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Long: 11.34K USD at 1326.5000 USD [API] | `2026-10-27 23:06:49` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`1404.15` (Vol: 3,000,000.00 USD, Dist: `+6.21%`) | Long MP=`1287.60` (Vol: 2,300,000.00 USD, Dist: `--2.61%`)
  * 48H Horizon: Short MP=`1404.15` (Vol: 3,000,000.00 USD, Dist: `+6.21%`) | Long MP=`1287.60` (Vol: 2,300,000.00 USD, Dist: `--2.61%`)
  * 3D Horizon: Short MP=`1404.42` (Vol: 3,000,000.00 USD, Dist: `+6.23%`) | Long MP=`1228.81` (Vol: 2,600,000.00 USD, Dist: `--7.05%`)
  * 7D Horizon: Short MP=`1404.10` (Vol: 3,000,000.00 USD, Dist: `+6.20%`) | Long MP=`1200.46` (Vol: 3,000,000.00 USD, Dist: `--9.20%`)
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
  * Current Rate: `76.43K` | Last 24h: `32.07K` | Last 3d: `282.84K` | Last 7d: `777.72K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0066%` | **USDT OKX** | `0.0100%` |
| **USDT Bybit** | `0.0100%` | **USDT KuCoin** | `0.0100%` |
| **USDT MEXC** | `0.0067%` | **USDT BingX** | `0.0054%` |
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
| `5:00 UTC` | `1348.65` | `1350.13` | `1348.65` | `1356.15` | `1344.45` | 21,612,679.16 USD | 11,526,731.97 USD | 10,085,947.19 USD | 1,440,784.78 USD | `+6.67%` | `2B / 2S` |
| `0:00 UTC` | `1335.45` | `1342.97` | `1335.45` | `1354.95` | `1333.05` | 31,234,081.19 USD | 13,144,149.56 USD | 18,089,931.62 USD | -4,945,782.06 USD | `-15.83%` | `2B / 7S` |
| `5:00 UTC` | `1333.95` | `1332.65` | `1333.95` | `1338.15` | `1327.05` | 42,051,592.22 USD | 20,998,597.47 USD | 21,052,994.75 USD | -54,397.28 USD | `-0.13%` | `1B / 3S` |
| `0:00 UTC` | `1324.05` | `1326.61` | `1324.05` | `1336.05` | `1320.15` | 35,175,848.19 USD | 15,805,961.43 USD | 19,369,886.76 USD | -3,563,925.33 USD | `-10.13%` | `1B / 10S` |
| `5:00 UTC` | `1321.35` | `1325.74` | `1321.35` | `1333.35` | `1318.35` | 26,289,288.34 USD | 11,537,630.34 USD | 14,751,657.99 USD | -3,214,027.65 USD | `-12.23%` | `3B / 5S` |
| `0:00 UTC` | `1315.95` | `1314.40` | `1315.95` | `1321.95` | `1307.85` | 50,919,152.62 USD | 22,517,005.07 USD | 28,402,147.55 USD | -5,885,142.49 USD | `-11.56%` | `2B / 5S` |
| `5:00 UTC` | `1315.95` | `1319.00` | `1315.95` | `1325.85` | `1312.05` | 22,246,351.59 USD | 13,151,982.06 USD | 9,094,369.53 USD | 4,057,612.52 USD | `+18.24%` | `9B / 1S` |
| `0:00 UTC` | `1320.75` | `1319.74` | `1320.75` | `1325.25` | `1315.95` | 11,564,611.33 USD | 5,754,638.99 USD | 5,809,972.34 USD | -55,333.35 USD | `-0.48%` | `1B / 2S` |
| `5:00 UTC` | `1322.85` | `1320.89` | `1322.85` | `1324.95` | `1316.85` | 7,868,027.33 USD | 4,223,932.72 USD | 3,644,094.61 USD | 579,838.11 USD | `+7.37%` | `3B / 0S` |
| `0:00 UTC` | `1324.05` | `1324.07` | `1324.05` | `1326.45` | `1319.85` | 8,116,012.51 USD | 4,361,577.48 USD | 3,754,435.03 USD | 607,142.45 USD | `+7.48%` | `2B / 1S` |

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
| `5m` | 648,690.00 USD | 927,540.00 USD | **`ACCUMULATION`** |
| `15m` | 947,510.00 USD | 2,970,000.00 USD | **`ACCUMULATION`** |
| `30m` | 48,910.00 USD | 4,130,000.00 USD | **`ACCUMULATION`** |
| `1h` | 2,070,000.00 USD | 11,160,000.00 USD | **`ACCUMULATION`** |
| `2h` | 49,230.00 USD | -20,530,000.00 USD | **`DISTRIBUTION`** |
| `4h` | 14,950,000.00 USD | 28,770,000.00 USD | **`ACCUMULATION`** |
| `6h` | 30,160,000.00 USD | 94,250,000.00 USD | **`ACCUMULATION`** |
| `8h` | 32,730,000.00 USD | 104,210,000.00 USD | **`ACCUMULATION`** |
| `12h` | 29,480,000.00 USD | 117,890,000.00 USD | **`ACCUMULATION`** |
| `24h` | 12,600,000.00 USD | 79,580,000.00 USD | **`ACCUMULATION`** |
| `1w` | 49,190,000.00 USD | 254,060,000.00 USD | **`ACCUMULATION`** |
| `30d` | 68,510,000.00 USD | -505,300,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+648.69K` | 15m=`+947.51K` | 1h=`+2.07M` | 24h=`+12.60M`
* Futures Capital Netflows: 5m=`+927.54K` | 15m=`+2.97M` | 1h=`+11.16M` | 24h=`+79.58M`
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
  * `2026-10-30 00:58:08 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 00:48:08 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 00:17:08 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 01:09:08 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 01:09:08 IST`: [@DeItaone] - (Sentiment: `Neutral`)
  * `2026-10-30 01:08:08 IST`: [@mb_ghalibaf] - (Sentiment: `Neutral`)
  * `2026-10-30 01:08:08 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-30 01:08:08 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-30 01:08:08 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:10:08 IST`: [fxstreet.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:10:08 IST`: [ForexFactory] - (Sentiment: `Neutral`)
  * `2026-10-29 21:10:08 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-29 21:10:08 IST`: [youtube.com/bankofcanadaofficial] - (Sentiment: `Neutral`)
  * `2026-10-29 21:10:08 IST`: [notayesmanseconomics.wordpress.com] - (Sentiment: `Neutral`)
  * `2026-10-29 21:10:08 IST`: [think.ing.com] - (Sentiment: `Neutral`)


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
  * Spread-Padded Stop Loss: `1210.52` (Risk Distance: `20.03` pts)
  * +2.5R Take Profit: `1280.63`
  * Mathematical Lot Sizing: **`0.49 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `1308.25` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `1328.28` (Risk Distance: `20.03` pts)
  * +2.5R Take Profit: `1258.17`
  * Mathematical Lot Sizing: **`0.49 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`1334.70`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
