# 🏛️ SOVEREIGN CANDIDATE DOSSIER: ZECUSD
**Canonical Key**: `ZECUSD` | **Broker Instrument**: `ZECUSD.p` | **Asset Class**: `Crypto Altcoin`
**Timestamp**: `2026-10-30 02:57:59 IST` (`2026-10-29 21:27:59 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `1273.51` | **Live Ask Quote**: `1274.68` | **Mid Price**: `1274.10`
- **Spread Points**: `117.00` | **Spread BPS**: `9.18 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `1281.48` | VWAP Z-Score: `-0.73` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `21.76` (Volatility Regime: `HIGH_EXPANSION`)
  * 14-Period RSI: `32.59` (State: `OVERSOLD`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `1396.85` | Lower -3.00σ Band: `1166.11`
  * Upper +2.51σ Band: `1378.01` | Lower -2.51σ Band: `1184.95`
  * Upper +2.01σ Band: `1358.78` | Lower -2.01σ Band: `1204.18`
  * Upper +2.00σ Band: `1358.40` | Lower -2.00σ Band: `1204.57`
  * Upper +1.28σ Band: `1330.71` | Lower -1.28σ Band: `1232.26`
  * Upper +1.00σ Band: `1319.94` | Lower -1.00σ Band: `1243.02`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`1283.21` | EMA-20=`1300.47` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`1297.27` (Slope: `+0.0000`) | EMA-100=`1289.51`
  * Institutional Anchors: EMA-144=`1285.10` | EMA-200=`1280.83` (Slope: `+0.1775`) | EMA-233=`1279.58`
- **Range Boundaries**: 24H High=`1396.49` | 24H Low=`1206.89` | Weekly High=`1396.49` | Weekly Low=`1206.89`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `1271.22` (Distance: `+0.31%`)
  * Point of Control (POC) = `1253.05` (Distance: `+1.77%`)
  * Value Area Low (VAL) = `1246.30` (Distance: `+2.32%`)
  * Auction Positioning: `ABOVE_VALUE (Imbalance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `RANGE_EXPANSION`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`1309.91` | POC=`1246.71` | VAL=`1230.27`
  * Prior Day Extremes: PDH=`1396.49` | PDL=`1206.89` | PDC=`1244.38`
  * Monday Range Blueprint: High=`1267.53` | Mid=`1222.14` | Low=`1176.75`
  * Developing Weekly Value Area: Weekly VAH=`1297.61` | Weekly POC=`1239.01` | Weekly VAL=`1196.53`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`1285.11` | Low=`1246.17`
  * London Session (08:00-16:00 UTC): High=`1279.19` | Low=`1269.00`
  * New York Session (13:00-21:00 UTC): High=`1281.74` | Low=`1266.45`
  * Initial Balance (First Hour): IB High=`1277.92` | IB Low=`1270.27`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `1269.00` - `1279.19`
  * Optimal Trade Entry (OTE 0.705): `1276.64`
  * Structural Invalidation Anchor (0.786): `1284.29`

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
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 02:55:39 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `16` | `0xb83d...6e36` | `SHORT` | 66,874,463.49 USD | `52,393.03` | `1336.45` | `1268.10` | `3923.37` | 3,146,207.47 USD | `+4.70%` | `3X Cross` |
| `24` | `0x5b5d...c060` | `SHORT` | 51,130,422.39 USD | `40,136.92` | `1478.36` | `1268.10` | `5393.66` | 8,206,586.51 USD | `+16.05%` | `3X Cross` |
| `41` | `0x7fda...17d1` | `SHORT` | 27,995,535.94 USD | `21,991.78` | `1261.72` | `1268.10` | `2961.93` | -247,974.56 USD | `-0.89%` | `5X Cross` |
| `81` | `0x60b0...991e` | `LONG` | 21,130,095.66 USD | `16,779.74` | `1179.65` | `1268.10` | `917.65` | 1,335,848.65 USD | `+6.32%` | `10X Cross` |
| `137` | `0xc36a...105b` | `LONG` | 14,508,237.53 USD | `11,510.82` | `1215.14` | `1268.10` | `950.94` | 520,956.50 USD | `+3.59%` | `10X Cross` |
| `153` | `0x9071...5c0b` | `LONG` | 13,422,165.50 USD | `10,517.29` | `1353.83` | `1268.10` | `0.000000` | -816,453.37 USD | `-6.08%` | `1X Cross` |
| `171` | `0x8742...8427` | `LONG` | 11,742,584.20 USD | `9,201.21` | `1286.37` | `1268.10` | `703.51` | -93,585.79 USD | `-0.80%` | `10X Cross` |
| `201` | `0xad59...ba81` | `SHORT` | 10,671,105.00 USD | `8,425.00` | `330.91` | `1268.10` | `2142.55` | -7,883,147.23 USD | `-73.87%` | `10X Cross` |
| `202` | `0x9ffd...ce40` | `LONG` | 10,645,855.27 USD | `8,425.02` | `1255.70` | `1268.10` | `599.98` | 66,560.70 USD | `+0.63%` | `5X Cross` |
| `203` | `0x58b2...11f3` | `LONG` | 10,636,398.94 USD | `8,463.08` | `1257.17` | `1268.10` | `370.22` | -3,090.25 USD | `-0.03%` | `10X Cross` |
| `208` | `0xdd53...2b13` | `SHORT` | 10,424,256.84 USD | `8,168.20` | `739.52` | `1268.10` | `8395.11` | -4,383,746.65 USD | `-42.05%` | `3X Cross` |
| `226` | `0x880a...311c` | `SHORT` | 9,825,023.83 USD | `7,707.11` | `1367.50` | `1268.10` | `2251.03` | 714,460.37 USD | `+7.27%` | `10X Cross` |
| `262` | `0xfc66...ca06` | `SHORT` | 8,850,625.67 USD | `6,935.14` | `1319.65` | `1268.10` | `6140.34` | 301,350.28 USD | `+3.40%` | `10X Cross` |
| `273` | `0x2b61...2f6c` | `LONG` | 8,651,016.30 USD | `6,807.00` | `1453.56` | `1268.10` | `585.58` | -1,243,334.92 USD | `-14.37%` | `10X Cross` |
| `288` | `0x2ae5...83e7` | `LONG` | 8,214,644.16 USD | `6,436.80` | `1391.82` | `1268.10` | `0.000000` | -744,247.83 USD | `-9.06%` | `1X Cross` |
| `330` | `0x26b6...9a13` | `LONG` | 6,934,028.50 USD | `5,433.73` | `1282.23` | `1268.10` | `204.07` | -33,274.74 USD | `-0.48%` | `10X Cross` |
| `346` | `0x45d2...4029` | `SHORT` | 6,670,697.40 USD | `5,227.00` | `833.44` | `1268.10` | `8544.18` | -2,314,319.43 USD | `-34.69%` | `5X Cross` |
| `373` | `0xea00...a918` | `LONG` | 6,296,312.00 USD | `5,000.00` | `739.16` | `1268.10` | `0.000000` | 2,600,496.89 USD | `+41.30%` | `5X Cross` |
| `382` | `0xdd7a...8830` | `LONG` | 6,142,794.14 USD | `4,860.19` | `897.48` | `1268.10` | `785.23` | 1,780,890.47 USD | `+28.99%` | `10X Cross` |
| `425` | `0xecb6...2b00` | `SHORT` | 5,256,151.38 USD | `4,117.95` | `1308.70` | `1268.10` | `7307.93` | 133,028.21 USD | `+2.53%` | `5X Cross` |
| `436` | `0x4cae...7c34` | `LONG` | 5,088,340.25 USD | `4,004.36` | `999.34` | `1268.10` | `860.03` | 1,086,612.10 USD | `+21.35%` | `10X Cross` |
| `445` | `0xa61c...66b9` | `LONG` | 4,953,312.00 USD | `3,888.00` | `1148.34` | `1268.10` | `0.000000` | 488,569.86 USD | `+9.86%` | `10X Cross` |
| `471` | `0x0153...8052` | `SHORT` | 4,715,549.32 USD | `3,698.18` | `1307.82` | `1268.10` | `2504.72` | 121,021.43 USD | `+2.57%` | `1X Isolated` |
| `483` | `0x9aa5...58af` | `SHORT` | 4,629,925.79 USD | `3,720.31` | `1205.51` | `1268.10` | `3656.44` | -145,039.00 USD | `-3.13%` | `10X Cross` |
| `516` | `0x382b...3e39` | `LONG` | 4,291,003.14 USD | `3,406.91` | `1210.61` | `1268.10` | `0.000000` | 166,552.09 USD | `+3.88%` | `10X Cross` |
| `540` | `0xd21d...90f1` | `LONG` | 4,130,750.00 USD | `3,250.00` | `1253.64` | `1268.10` | `875.91` | 56,408.27 USD | `+1.37%` | `4X Isolated` |
| `557` | `0x1338...c48e` | `LONG` | 4,004,185.30 USD | `3,149.43` | `1018.52` | `1268.10` | `820.21` | 796,439.76 USD | `+19.89%` | `4X Isolated` |
| `564` | `0x456f...cdf1` | `LONG` | 3,983,453.81 USD | `3,134.11` | `1268.47` | `1268.10` | `493.64` | 7,944.34 USD | `+0.20%` | `10X Cross` |
| `576` | `0xdbe0...d6d5` | `LONG` | 3,915,643.07 USD | `3,085.37` | `422.97` | `1268.10` | `338.52` | 2,610,638.57 USD | `+66.67%` | `3X Isolated` |
| `584` | `0x27c9...d65d` | `SHORT` | 3,889,868.85 USD | `3,047.77` | `1254.41` | `1268.10` | `1714.72` | -66,712.28 USD | `-1.72%` | `10X Cross` |
| `599` | `0x325e...9564` | `LONG` | 3,794,114.05 USD | `3,001.91` | `1301.41` | `1268.10` | `130.98` | -112,595.16 USD | `-2.97%` | `10X Cross` |
| `605` | `0x9c06...0560` | `SHORT` | 3,764,158.20 USD | `2,989.80` | `786.00` | `1268.10` | `2537.20` | -1,414,163.20 USD | `-37.57%` | `10X Cross` |
| `617` | `0x2e30...4cb5` | `SHORT` | 3,693,195.18 USD | `2,893.90` | `1299.63` | `1268.10` | `2909.83` | 67,809.64 USD | `+1.84%` | `2X Cross` |
| `652` | `0xd4c1...3d1d` | `SHORT` | 3,482,038.32 USD | `2,728.32` | `1302.83` | `1268.10` | `3015.13` | 72,500.01 USD | `+2.08%` | `10X Cross` |
| `699` | `0xa183...0482` | `LONG` | 3,234,397.60 USD | `2,534.00` | `530.25` | `1268.10` | `444.45` | 1,890,734.88 USD | `+58.46%` | `5X Isolated` |
| `708` | `0xac48...3201` | `LONG` | 3,198,904.27 USD | `2,540.30` | `1393.86` | `1268.10` | `494.82` | -341,925.02 USD | `-10.69%` | `10X Cross` |
| `721` | `0x0871...e927` | `LONG` | 3,147,000.00 USD | `2,500.00` | `1276.50` | `1268.10` | `0.000000` | -44,250.00 USD | `-1.41%` | `10X Cross` |
| `730` | `0x9b86...6e6e` | `LONG` | 3,125,082.18 USD | `2,467.30` | `637.58` | `1268.10` | `889.67` | 1,551,982.58 USD | `+49.66%` | `3X Cross` |
| `783` | `0xb2f7...af9f` | `SHORT` | 2,940,738.12 USD | `2,313.72` | `746.63` | `1268.10` | `4331.26` | -1,213,249.37 USD | `-41.26%` | `10X Cross` |
| `812` | `0xf48f...10fe` | `LONG` | 2,819,700.79 USD | `2,218.49` | `1517.87` | `1268.10` | `958.46` | -547,686.03 USD | `-19.42%` | `3X Cross` |
| `836` | `0x5bc4...3b0c` | `SHORT` | 2,719,676.54 USD | `2,130.74` | `1089.65` | `1268.10` | `3651.11` | -397,918.96 USD | `-14.63%` | `5X Cross` |
| `863` | `0x4fe2...ac59` | `SHORT` | 2,632,965.47 USD | `2,071.57` | `1478.56` | `1268.10` | `1822.33` | 429,980.74 USD | `+16.33%` | `10X Cross` |
| `865` | `0x8de4...b9aa` | `SHORT` | 2,631,470.21 USD | `2,091.29` | `1331.35` | `1268.10` | `1689.84` | 152,769.50 USD | `+5.81%` | `3X Cross` |
| `889` | `0x413c...886c` | `LONG` | 2,542,000.00 USD | `2,000.00` | `1266.31` | `1268.10` | `0.000000` | 9,372.73 USD | `+0.37%` | `10X Cross` |
| `892` | `0x9a99...d21a` | `LONG` | 2,538,400.00 USD | `2,000.00` | `1278.44` | `1268.10` | `0.000000` | -18,473.67 USD | `-0.73%` | `10X Cross` |
| `900` | `0x668c...ea2e` | `SHORT` | 2,515,200.00 USD | `2,000.00` | `1406.98` | `1268.10` | `2701.91` | 298,763.99 USD | `+11.88%` | `10X Cross` |
| `922` | `0x77ee...2902` | `SHORT` | 2,473,209.53 USD | `1,946.03` | `759.84` | `1268.10` | `5334.71` | -994,532.02 USD | `-40.21%` | `10X Cross` |
| `926` | `0x3e2f...b269` | `SHORT` | 2,457,528.41 USD | `1,925.51` | `1134.87` | `1268.10` | `2931.77` | -272,329.56 USD | `-11.08%` | `10X Cross` |
| `938` | `0xe097...d0fe` | `LONG` | 2,429,838.49 USD | `1,913.56` | `1261.17` | `1268.10` | `0.000000` | 16,512.32 USD | `+0.68%` | `10X Cross` |
| `944` | `0x4f12...618b` | `SHORT` | 2,410,281.67 USD | `1,896.28` | `1608.30` | `1268.10` | `2116.73` | 639,502.71 USD | `+26.53%` | `3X Cross` |
| `995` | `0x866d...d6e1` | `LONG` | 2,268,055.26 USD | `1,802.05` | `674.73` | `1268.10` | `206.96` | 1,052,153.95 USD | `+46.39%` | `10X Cross` |
| `1025` | `0x2309...a2d9` | `LONG` | 2,178,335.46 USD | `1,750.37` | `1186.09` | `1268.10` | `814.20` | 102,241.35 USD | `+4.69%` | `8X Cross` |
| `1031` | `0x2edd...8179` | `SHORT` | 2,172,071.15 USD | `1,701.85` | `1261.58` | `1268.10` | `2991.78` | -25,052.30 USD | `-1.15%` | `10X Cross` |
| `1036` | `0x023a...2355` | `SHORT` | 2,161,018.48 USD | `1,696.38` | `1313.00` | `1268.10` | `5727.46` | 66,328.81 USD | `+3.07%` | `10X Cross` |
| `1058` | `0xfe7c...b7ae` | `SHORT` | 2,090,621.26 USD | `1,640.99` | `1347.05` | `1268.10` | `6762.07` | 119,867.92 USD | `+5.73%` | `10X Cross` |
| `1068` | `0xa271...a3f7` | `LONG` | 2,073,641.99 USD | `1,631.43` | `1190.60` | `1268.10` | `910.31` | 131,260.19 USD | `+6.33%` | `4X Cross` |
| `1069` | `0x3e47...aaf6` | `LONG` | 2,072,512.25 USD | `1,636.28` | `1278.38` | `1268.10` | `1045.14` | -19,279.54 USD | `-0.93%` | `10X Cross` |
| `1084` | `0x265e...7f70` | `LONG` | 2,035,904.28 USD | `1,601.74` | `1388.09` | `1268.10` | `0.000000` | -187,460.73 USD | `-9.21%` | `3X Cross` |
| `1087` | `0x6646...6de5` | `SHORT` | 2,031,680.00 USD | `1,600.00` | `660.64` | `1268.10` | `4452.17` | -974,655.03 USD | `-47.97%` | `10X Cross` |
| `1097` | `0xdf57...93f5` | `LONG` | 2,015,931.74 USD | `1,579.76` | `1218.38` | `1268.10` | `780.15` | 91,175.76 USD | `+4.52%` | `3X Isolated` |
| `1110` | `0x7f75...9edf` | `LONG` | 1,999,196.10 USD | `1,605.78` | `1199.97` | `1268.10` | `976.98` | 72,304.21 USD | `+3.62%` | `10X Cross` |
| `1141` | `0xab59...59b5` | `LONG` | 1,971,797.60 USD | `1,565.32` | `1342.15` | `1268.10` | `824.01` | -129,097.62 USD | `-6.55%` | `10X Cross` |
| `1192` | `0xb695...a92d` | `LONG` | 1,892,604.60 USD | `1,483.00` | `1249.80` | `1268.10` | `0.000000` | 39,145.75 USD | `+2.07%` | `10X Cross` |
| `1196` | `0xcf67...eb24` | `LONG` | 1,885,200.00 USD | `1,500.00` | `887.05` | `1268.10` | `634.70` | 554,628.63 USD | `+29.42%` | `10X Cross` |
| `1265` | `0x2ab7...c2f8` | `LONG` | 1,787,202.58 USD | `1,400.51` | `813.26` | `1268.10` | `796.35` | 648,220.89 USD | `+36.27%` | `3X Cross` |
| `1304` | `0x11be...8b1d` | `LONG` | 1,733,958.55 USD | `1,375.83` | `1206.55` | `1268.10` | `1134.43` | 73,950.59 USD | `+4.26%` | `10X Isolated` |
| `1416` | `0xe065...0f85` | `SHORT` | 1,586,848.25 USD | `1,262.61` | `1087.02` | `1268.10` | `1808.44` | -214,372.12 USD | `-13.51%` | `10X Cross` |
| `1426` | `0x7277...0b98` | `SHORT` | 1,575,932.46 USD | `1,234.96` | `1298.48` | `1268.10` | `2409.64` | 27,636.96 USD | `+1.75%` | `10X Cross` |
| `1450` | `0x039c...0ebd` | `SHORT` | 1,544,864.97 USD | `1,222.30` | `1238.67` | `1268.10` | `3652.23` | -30,844.60 USD | `-2.00%` | `10X Cross` |
| `1478` | `0x5975...9abd` | `LONG` | 1,512,360.00 USD | `1,200.00` | `1179.54` | `1268.10` | `453.38` | 96,917.21 USD | `+6.41%` | `5X Cross` |
| `1497` | `0x69cc...14fd` | `SHORT` | 1,482,127.63 USD | `1,161.36` | `675.33` | `1268.10` | `7904.29` | -697,822.10 USD | `-47.08%` | `10X Cross` |
| `1516` | `0x3fc5...c0c1` | `SHORT` | 1,462,997.72 USD | `1,148.44` | `1264.34` | `1268.10` | `2997.17` | -10,983.94 USD | `-0.75%` | `10X Cross` |
| `1536` | `0xe35c...a1d3` | `LONG` | 1,435,874.44 USD | `1,127.06` | `1318.20` | `1268.10` | `694.35` | -49,820.91 USD | `-3.47%` | `2X Isolated` |
| `1548` | `0x2847...d47b` | `LONG` | 1,428,169.48 USD | `1,119.16` | `1233.39` | `1268.10` | `0.000000` | 47,808.45 USD | `+3.35%` | `5X Cross` |
| `1557` | `0xfc27...9d9d` | `SHORT` | 1,416,990.38 USD | `1,110.32` | `1315.18` | `1268.10` | `15864.12` | 43,279.57 USD | `+3.05%` | `10X Cross` |
| `1566` | `0x5f94...4b96` | `LONG` | 1,409,589.75 USD | `1,115.27` | `538.00` | `1268.10` | `0.000000` | 809,572.12 USD | `+57.43%` | `10X Cross` |
| `1580` | `0x266b...efcb` | `LONG` | 1,396,780.00 USD | `1,100.00` | `863.84` | `1268.10` | `275.84` | 446,555.24 USD | `+31.97%` | `10X Cross` |
| `1592` | `0x71df...a23d` | `SHORT` | 1,382,514.86 USD | `1,098.28` | `513.50` | `1268.10` | `2548.89` | -818,544.67 USD | `-59.21%` | `2X Cross` |
| `1602` | `0xbfc7...80b4` | `SHORT` | 1,366,540.00 USD | `1,075.00` | `558.03` | `1268.10` | `5122.49` | -766,661.27 USD | `-56.10%` | `10X Cross` |
| `1609` | `0x3205...40bb` | `SHORT` | 1,353,856.77 USD | `1,060.85` | `1262.69` | `1268.10` | `2612.86` | -14,326.70 USD | `-1.06%` | `10X Cross` |
| `1628` | `0x51f6...2b39` | `SHORT` | 1,338,835.90 USD | `1,049.08` | `1302.21` | `1268.10` | `2749.09` | 27,289.48 USD | `+2.04%` | `10X Cross` |
| `1645` | `0xdf83...3cff` | `SHORT` | 1,321,366.15 USD | `1,035.31` | `1252.52` | `1268.10` | `1836.59` | -24,617.95 USD | `-1.86%` | `10X Cross` |
| `1682` | `0x4e23...20c3` | `LONG` | 1,275,105.72 USD | `999.08` | `1278.54` | `1268.10` | `0.000000` | -2,257.31 USD | `-0.18%` | `4X Cross` |
| `1684` | `0x123d...3bff` | `SHORT` | 1,272,046.00 USD | `1,009.32` | `490.16` | `1268.10` | `4346.97` | -777,320.13 USD | `-61.11%` | `10X Cross` |
| `1696` | `0xe282...df29` | `LONG` | 1,263,900.00 USD | `1,000.00` | `420.99` | `1268.10` | `161.96` | 842,913.14 USD | `+66.69%` | `10X Cross` |
| `1710` | `0x17f0...094f` | `LONG` | 1,250,750.01 USD | `984.30` | `1287.23` | `1268.10` | `536.78` | -16,270.15 USD | `-1.30%` | `5X Cross` |
| `1774` | `0x757d...94ba` | `LONG` | 1,180,392.50 USD | `925.00` | `1558.31` | `1268.10` | `0.000000` | -261,048.08 USD | `-22.12%` | `10X Cross` |
| `1829` | `0xb911...5525` | `LONG` | 1,134,270.00 USD | `900.00` | `1294.82` | `1268.10` | `1070.30` | -31,067.82 USD | `-2.74%` | `10X Cross` |
| `1877` | `0xdf95...7d72` | `SHORT` | 1,094,288.53 USD | `857.42` | `1074.31` | `1268.10` | `45120.61` | -173,151.52 USD | `-15.82%` | `10X Cross` |
| `1885` | `0xcf0a...856f` | `LONG` | 1,084,668.86 USD | `871.15` | `1292.19` | `1268.10` | `938.49` | -41,025.98 USD | `-3.78%` | `4X Cross` |
| `1936` | `0x601c...4f54` | `SHORT` | 1,048,167.59 USD | `824.42` | `615.11` | `1268.10` | `3013.26` | -541,054.84 USD | `-51.62%` | `5X Cross` |
| `1945` | `0xae55...2236` | `LONG` | 1,043,255.21 USD | `817.47` | `1467.80` | `1268.10` | `0.000000` | -156,626.00 USD | `-15.01%` | `10X Cross` |
| `1947` | `0x38f9...cb04` | `SHORT` | 1,041,094.13 USD | `815.74` | `1262.59` | `1268.10` | `2310.33` | -11,150.90 USD | `-1.07%` | `10X Cross` |
| `1953` | `0xabdb...84ac` | `LONG` | 1,032,828.80 USD | `793.69` | `711.79` | `1268.10` | `664.33` | 467,888.44 USD | `+45.30%` | `3X Cross` |
| `1975` | `0x0f02...5384` | `LONG` | 1,022,107.18 USD | `800.78` | `1290.36` | `1268.10` | `290.53` | -11,186.89 USD | `-1.09%` | `3X Cross` |
| `1976` | `0x9b0f...db40` | `LONG` | 1,020,000.00 USD | `800.00` | `1268.86` | `1268.10` | `784.95` | 4,910.24 USD | `+0.48%` | `10X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `1092.10` | 8,889.69 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Long: 8.89K USD at 1092.1000 USD [API] | `2026-10-18 14:31:53` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`1404.15` (Vol: 3,000,000.00 USD, Dist: `+7.59%`) | Long MP=`1287.60` (Vol: 2,300,000.00 USD, Dist: `--1.34%`)
  * 48H Horizon: Short MP=`1404.15` (Vol: 3,000,000.00 USD, Dist: `+7.59%`) | Long MP=`1287.60` (Vol: 2,300,000.00 USD, Dist: `--1.34%`)
  * 3D Horizon: Short MP=`1404.42` (Vol: 3,000,000.00 USD, Dist: `+7.61%`) | Long MP=`1228.81` (Vol: 2,600,000.00 USD, Dist: `--5.85%`)
  * 7D Horizon: Short MP=`1404.10` (Vol: 3,000,000.00 USD, Dist: `+7.58%`) | Long MP=`1200.46` (Vol: 3,000,000.00 USD, Dist: `--8.02%`)
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
| `5m` | `BALANCED` | 0.00 USD | 1,750.00 USD | 1,750.00 USD | 1,750.00 USD | `1` | `2026-10-29 21:25:00 UTC - 2026-10-29 21:30:00 UTC` |
| `15m` | `BALANCED` | 0.00 USD | 1,750.00 USD | 1,750.00 USD | 1,750.00 USD | `1` | `2026-10-29 21:15:00 UTC - 2026-10-29 21:30:00 UTC` |
| `1h` | `BALANCED` | 0.00 USD | 1,750.00 USD | 1,750.00 USD | 1,750.00 USD | `1` | `2026-10-29 21:00:00 UTC - 2026-10-29 22:00:00 UTC` |
| `4h` | `BALANCED` | 0.00 USD | 1,750.00 USD | 1,750.00 USD | 1,750.00 USD | `1` | `2026-10-29 20:00:00 UTC - 2026-10-30 00:00:00 UTC` |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `0 USD` | Total OI Tokens: `-`
  * 1h OI Change: `0.00%` | 4h OI Change: `0.00%` | 24h OI Change: `0.00%`
  * Exchange Breakdown: Binance=`-` | Bybit=`-` | OKX=`-` | Hyperliquid=`-`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `-4.90K` | Last 24h: `33.19K` | Last 3d: `283.86K` | Last 7d: `777.60K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `-0.0031%` | **USDT OKX** | `0.0011%` |
| **USDT Bybit** | `0.0100%` | **USDT KuCoin** | `-0.0038%` |
| **USDT MEXC** | `-0.0034%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `-0.0103%` | **USDT Bitget** | `0.0100%` |
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
| `0:00 UTC` | `1320.75` | `1319.74` | `1320.75` | `1325.25` | `1315.95` | 11,564,611.33 USD | 5,754,638.99 USD | 5,809,972.34 USD | -55,333.35 USD | `-0.48%` | `1B / 2S` |
| `5:00 UTC` | `1322.85` | `1320.89` | `1322.85` | `1324.95` | `1316.85` | 7,868,027.33 USD | 4,223,932.72 USD | 3,644,094.61 USD | 579,838.11 USD | `+7.37%` | `3B / 0S` |
| `0:00 UTC` | `1324.95` | `1324.41` | `1324.95` | `1327.05` | `1319.85` | 12,000,472.36 USD | 6,714,467.49 USD | 5,286,004.87 USD | 1,428,462.62 USD | `+11.90%` | `2B / 1S` |
| `5:00 UTC` | `1325.25` | `1325.38` | `1325.25` | `1330.65` | `1320.75` | 11,021,893.68 USD | 5,577,839.59 USD | 5,444,054.10 USD | 133,785.49 USD | `+1.21%` | `3B / 1S` |
| `0:00 UTC` | `1294.05` | `1302.04` | `1294.05` | `1328.55` | `1286.25` | 68,949,402.59 USD | 35,232,633.05 USD | 33,716,769.55 USD | 1,515,863.50 USD | `+2.20%` | `6B / 24S` |
| `5:00 UTC` | `1306.05` | `1306.88` | `1306.05` | `1312.05` | `1300.05` | 17,712,248.68 USD | 9,074,345.66 USD | 8,637,903.02 USD | 436,442.64 USD | `+2.46%` | `3B / 5S` |
| `0:00 UTC` | `1249.20` | `1269.32` | `1249.20` | `1308.60` | `1241.40` | 130,590,816.99 USD | 58,796,845.15 USD | 71,793,971.84 USD | -12,997,126.69 USD | `-9.95%` | `4B / 19S` |
| `5:00 UTC` | `1229.25` | `1237.79` | `1229.25` | `1264.35` | `1206.75` | 149,162,484.89 USD | 77,012,548.38 USD | 72,149,936.51 USD | 4,862,611.87 USD | `+3.26%` | `9B / 11S` |
| `0:00 UTC` | `1249.95` | `1248.07` | `1249.95` | `1259.85` | `1233.15` | 61,152,789.32 USD | 32,267,997.87 USD | 28,884,791.45 USD | 3,383,206.41 USD | `+5.53%` | `6B / 4S` |
| `5:00 UTC` | `1282.65` | `1272.10` | `1282.65` | `1286.25` | `1253.25` | 43,789,612.68 USD | 24,704,113.59 USD | 19,085,499.09 USD | 5,618,614.51 USD | `+12.83%` | `6B / 1S` |

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
| `5m` | 894,150.00 USD | 8,050,000.00 USD | **`ACCUMULATION`** |
| `15m` | 3,410,000.00 USD | 18,040,000.00 USD | **`ACCUMULATION`** |
| `30m` | 4,450,000.00 USD | 16,790,000.00 USD | **`ACCUMULATION`** |
| `1h` | -10,900,000.00 USD | -3,790,000.00 USD | **`DISTRIBUTION`** |
| `2h` | -13,020,000.00 USD | -5,970,000.00 USD | **`DISTRIBUTION`** |
| `4h` | -12,250,000.00 USD | -27,030,000.00 USD | **`DISTRIBUTION`** |
| `6h` | 3,370,000.00 USD | 44,190,000.00 USD | **`ACCUMULATION`** |
| `8h` | 14,530,000.00 USD | 83,140,000.00 USD | **`ACCUMULATION`** |
| `12h` | 15,950,000.00 USD | 92,470,000.00 USD | **`ACCUMULATION`** |
| `24h` | -263,020.00 USD | 53,550,000.00 USD | **`ACCUMULATION`** |
| `1w` | 34,490,000.00 USD | 240,130,000.00 USD | **`ACCUMULATION`** |
| `30d` | 57,030,000.00 USD | -520,870,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+894.15K` | 15m=`+3.41M` | 1h=`-10.90M` | 24h=`-263.02K`
* Futures Capital Netflows: 5m=`+8.05M` | 15m=`+18.04M` | 1h=`-3.79M` | 24h=`+53.55M`
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
  * `2026-10-30 02:15:01 IST`: [morningstar.com] - (Sentiment: `Neutral`)
  * `2026-10-30 02:51:01 IST`: [sec.gov] - (Sentiment: `Neutral`)
  * `2026-10-30 02:51:01 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 02:50:01 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 02:50:01 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:52:01 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:52:01 IST`: [@DeItaone] - (Sentiment: `Neutral`)
  * `2026-10-29 23:52:01 IST`: [@mb_ghalibaf] - (Sentiment: `Neutral`)
  * `2026-10-29 23:52:01 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-29 23:52:01 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-29 22:52:01 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:52:01 IST`: [fxstreet.com] - (Sentiment: `Neutral`)
  * `2026-10-29 21:52:01 IST`: [ForexFactory] - (Sentiment: `Neutral`)
  * `2026-10-29 21:52:01 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-29 21:52:01 IST`: [youtube.com/bankofcanadaofficial] - (Sentiment: `Neutral`)


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
  * Execution Entry: `1246.30` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `1218.44` (Risk Distance: `27.86` pts)
  * +2.5R Take Profit: `1315.96`
  * Mathematical Lot Sizing: **`0.35 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `1271.22` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `1299.08` (Risk Distance: `27.86` pts)
  * +2.5R Take Profit: `1201.56`
  * Mathematical Lot Sizing: **`0.35 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`1284.29`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
