# 🏛️ SOVEREIGN CANDIDATE DOSSIER: ZECUSD
**Canonical Key**: `ZECUSD` | **Broker Instrument**: `ZECUSD.p` | **Asset Class**: `Crypto Altcoin`
**Timestamp**: `2026-10-30 02:45:50 IST` (`2026-10-29 21:15:50 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `1253.76` | **Live Ask Quote**: `1255.01` | **Mid Price**: `1254.38`
- **Spread Points**: `125.00` | **Spread BPS**: `9.97 bps` (Charter Threshold: `25.00 bps`)
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
  * Value Area High (VAH) = `1258.81` (Distance: `-0.30%`)
  * Point of Control (POC) = `1252.89` (Distance: `+0.17%`)
  * Value Area Low (VAL) = `1250.19` (Distance: `+0.39%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`1309.91` | POC=`1246.71` | VAL=`1230.27`
  * Prior Day Extremes: PDH=`1396.49` | PDL=`1206.89` | PDC=`1244.38`
  * Monday Range Blueprint: High=`1267.53` | Mid=`1222.14` | Low=`1176.75`
  * Developing Weekly Value Area: Weekly VAH=`1296.14` | Weekly POC=`1239.01` | Weekly VAL=`1195.06`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`1258.85` | Low=`1246.17`
  * London Session (08:00-16:00 UTC): High=`1259.40` | Low=`1249.37`
  * New York Session (13:00-21:00 UTC): High=`1261.91` | Low=`1246.86`
  * Initial Balance (First Hour): IB High=`1258.15` | IB Low=`1250.62`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `1249.37` - `1259.40`
  * Optimal Trade Entry (OTE 0.705): `1256.89`
  * Structural Invalidation Anchor (0.786): `1264.42`

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
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 02:45:18 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `16` | `0xb83d...6e36` | `SHORT` | 65,396,880.12 USD | `52,582.52` | `1336.45` | `1245.40` | `4002.63` | 4,877,034.77 USD | `+7.46%` | `3X Cross` |
| `25` | `0x5b5d...c060` | `SHORT` | 50,562,124.25 USD | `40,651.33` | `1478.36` | `1245.40` | `5472.26` | 9,535,370.27 USD | `+18.86%` | `3X Cross` |
| `43` | `0x7fda...17d1` | `SHORT` | 27,298,137.04 USD | `21,972.10` | `1261.67` | `1245.40` | `3049.00` | 423,379.57 USD | `+1.55%` | `5X Cross` |
| `82` | `0x60b0...991e` | `LONG` | 20,894,132.25 USD | `16,779.74` | `1179.65` | `1245.40` | `927.53` | 1,099,885.23 USD | `+5.26%` | `10X Cross` |
| `135` | `0xc36a...105b` | `LONG` | 14,989,389.80 USD | `11,510.82` | `1215.14` | `1245.40` | `939.41` | 1,002,108.78 USD | `+6.69%` | `10X Cross` |
| `172` | `0x8742...8427` | `LONG` | 11,370,855.32 USD | `9,201.21` | `1286.37` | `1245.40` | `709.97` | -465,314.68 USD | `-4.09%` | `10X Cross` |
| `189` | `0x9071...5c0b` | `LONG` | 10,919,103.80 USD | `8,829.94` | `1370.53` | `1245.40` | `0.000000` | -1,182,584.84 USD | `-10.83%` | `1X Cross` |
| `198` | `0x9ffd...ce40` | `LONG` | 10,587,023.11 USD | `8,543.32` | `1255.56` | `1245.40` | `612.63` | -139,657.90 USD | `-1.32%` | `5X Cross` |
| `200` | `0xad59...ba81` | `SHORT` | 10,549,785.00 USD | `8,425.00` | `330.91` | `1245.40` | `2144.45` | -7,761,827.23 USD | `-73.57%` | `10X Cross` |
| `207` | `0x58b2...11f3` | `LONG` | 10,267,703.21 USD | `8,263.08` | `1257.44` | `1245.40` | `334.51` | -122,659.58 USD | `-1.19%` | `10X Cross` |
| `212` | `0xdd53...2b13` | `SHORT` | 10,091,331.16 USD | `8,177.74` | `739.52` | `1245.40` | `8664.56` | -4,043,765.99 USD | `-40.07%` | `3X Cross` |
| `233` | `0x880a...311c` | `SHORT` | 9,628,492.52 USD | `7,707.11` | `1367.50` | `1245.40` | `2268.63` | 910,991.68 USD | `+9.46%` | `10X Cross` |
| `262` | `0x2b61...2f6c` | `LONG` | 8,864,075.40 USD | `6,807.00` | `1453.56` | `1245.40` | `621.05` | -1,030,275.82 USD | `-11.62%` | `10X Cross` |
| `273` | `0xfc66...ca06` | `SHORT` | 8,625,233.62 USD | `6,935.14` | `1319.65` | `1245.40` | `6199.22` | 526,742.33 USD | `+6.11%` | `10X Cross` |
| `297` | `0x2ae5...83e7` | `LONG` | 7,964,896.32 USD | `6,436.80` | `1391.82` | `1245.40` | `0.000000` | -993,995.67 USD | `-12.48%` | `1X Cross` |
| `339` | `0x26b6...9a13` | `LONG` | 6,735,322.42 USD | `5,433.73` | `1282.23` | `1245.40` | `216.06` | -231,980.81 USD | `-3.44%` | `10X Cross` |
| `361` | `0x45d2...4029` | `SHORT` | 6,463,708.20 USD | `5,227.00` | `833.44` | `1245.40` | `8950.22` | -2,107,330.23 USD | `-32.60%` | `5X Cross` |
| `377` | `0xea00...a918` | `LONG` | 6,226,000.00 USD | `5,000.00` | `739.16` | `1245.40` | `0.000000` | 2,530,184.89 USD | `+40.64%` | `5X Cross` |
| `383` | `0xdd7a...8830` | `LONG` | 6,075,237.50 USD | `4,860.19` | `897.48` | `1245.40` | `794.97` | 1,713,333.83 USD | `+28.20%` | `10X Cross` |
| `399` | `0x5323...b23c` | `LONG` | 5,745,284.59 USD | `4,619.51` | `1245.70` | `1245.40` | `0.000000` | -9,254.12 USD | `-0.16%` | `5X Cross` |
| `425` | `0x4cae...7c34` | `LONG` | 5,210,072.80 USD | `4,004.36` | `999.34` | `1245.40` | `807.77` | 1,208,344.64 USD | `+23.19%` | `10X Cross` |
| `451` | `0xa61c...66b9` | `LONG` | 4,863,110.40 USD | `3,888.00` | `1148.34` | `1245.40` | `0.000000` | 398,368.26 USD | `+8.19%` | `10X Cross` |
| `457` | `0xecb6...2b00` | `SHORT` | 4,821,538.85 USD | `3,876.77` | `1311.47` | `1245.40` | `7942.88` | 262,716.23 USD | `+5.45%` | `5X Cross` |
| `472` | `0x0153...8052` | `SHORT` | 4,635,937.49 USD | `3,698.18` | `1307.82` | `1245.40` | `2504.72` | 200,633.26 USD | `+4.33%` | `1X Isolated` |
| `475` | `0x9aa5...58af` | `SHORT` | 4,629,925.79 USD | `3,720.31` | `1205.51` | `1245.40` | `3656.44` | -145,039.00 USD | `-3.13%` | `10X Cross` |
| `515` | `0x382b...3e39` | `LONG` | 4,243,647.10 USD | `3,406.91` | `1210.61` | `1245.40` | `0.000000` | 119,196.04 USD | `+2.81%` | `10X Cross` |
| `524` | `0xd21d...90f1` | `LONG` | 4,167,800.00 USD | `3,250.00` | `1253.64` | `1245.40` | `875.90` | 93,458.27 USD | `+2.24%` | `4X Isolated` |
| `535` | `0x1338...c48e` | `LONG` | 4,098,353.26 USD | `3,149.43` | `1018.52` | `1245.40` | `820.19` | 890,607.72 USD | `+21.73%` | `4X Isolated` |
| `577` | `0x456f...cdf1` | `LONG` | 3,908,548.58 USD | `3,134.11` | `1268.47` | `1245.40` | `493.67` | -66,960.88 USD | `-1.71%` | `10X Cross` |
| `591` | `0xdbe0...d6d5` | `LONG` | 3,837,274.67 USD | `3,085.37` | `422.97` | `1245.40` | `338.52` | 2,532,270.18 USD | `+65.99%` | `3X Isolated` |
| `596` | `0x27c9...d65d` | `SHORT` | 3,807,632.98 USD | `3,064.74` | `1254.41` | `1245.40` | `1758.38` | 36,810.96 USD | `+0.97%` | `10X Cross` |
| `602` | `0x4e23...20c3` | `LONG` | 3,774,178.58 USD | `3,041.73` | `1279.86` | `1245.40` | `0.000000` | -118,818.47 USD | `-3.15%` | `4X Cross` |
| `612` | `0x9c06...0560` | `SHORT` | 3,722,301.00 USD | `2,989.80` | `786.00` | `1245.40` | `2572.68` | -1,372,306.00 USD | `-36.87%` | `10X Cross` |
| `633` | `0x2e30...4cb5` | `SHORT` | 3,597,473.84 USD | `2,891.86` | `1299.68` | `1245.40` | `2922.43` | 161,016.83 USD | `+4.48%` | `2X Cross` |
| `656` | `0xd4c1...3d1d` | `SHORT` | 3,452,337.08 USD | `2,775.86` | `1302.90` | `1245.40` | `3060.71` | 164,339.33 USD | `+4.76%` | `10X Cross` |
| `691` | `0x0871...e927` | `LONG` | 3,255,500.00 USD | `2,500.00` | `1276.50` | `1245.40` | `0.000000` | 64,250.00 USD | `+1.97%` | `10X Cross` |
| `710` | `0xac48...3201` | `LONG` | 3,163,181.56 USD | `2,540.30` | `1393.86` | `1245.40` | `503.12` | -377,647.73 USD | `-11.94%` | `10X Cross` |
| `723` | `0xa183...0482` | `LONG` | 3,131,517.20 USD | `2,534.00` | `530.25` | `1245.40` | `444.45` | 1,787,854.48 USD | `+57.09%` | `5X Isolated` |
| `724` | `0x325e...9564` | `LONG` | 3,129,389.03 USD | `2,501.91` | `1306.24` | `1245.40` | `0.000000` | -138,704.88 USD | `-4.43%` | `10X Cross` |
| `736` | `0x9b86...6e6e` | `LONG` | 3,091,280.17 USD | `2,467.30` | `637.58` | `1245.40` | `889.67` | 1,518,180.57 USD | `+49.11%` | `3X Cross` |
| `786` | `0xb2f7...af9f` | `SHORT` | 2,897,240.18 USD | `2,313.72` | `746.63` | `1245.40` | `4378.89` | -1,169,751.44 USD | `-40.37%` | `10X Cross` |
| `820` | `0xf48f...10fe` | `LONG` | 2,779,102.42 USD | `2,218.49` | `1517.87` | `1245.40` | `993.57` | -588,284.40 USD | `-21.17%` | `3X Cross` |
| `854` | `0x5bc4...3b0c` | `SHORT` | 2,630,398.53 USD | `2,130.74` | `1089.65` | `1245.40` | `3681.57` | -308,640.95 USD | `-11.73%` | `5X Cross` |
| `862` | `0x8de4...b9aa` | `SHORT` | 2,604,910.82 USD | `2,091.29` | `1331.35` | `1245.40` | `1689.84` | 179,328.88 USD | `+6.88%` | `3X Cross` |
| `870` | `0x4fe2...ac59` | `SHORT` | 2,580,347.59 USD | `2,071.57` | `1478.56` | `1245.40` | `1834.45` | 482,598.62 USD | `+18.70%` | `10X Cross` |
| `883` | `0x77ee...2902` | `SHORT` | 2,531,979.63 USD | `1,946.03` | `759.84` | `1245.40` | `5234.95` | -1,053,302.13 USD | `-41.60%` | `10X Cross` |
| `900` | `0x668c...ea2e` | `SHORT` | 2,489,000.00 USD | `2,000.00` | `1406.98` | `1245.40` | `2702.62` | 324,963.99 USD | `+13.06%` | `10X Cross` |
| `933` | `0xe097...d0fe` | `LONG` | 2,377,789.66 USD | `1,913.56` | `1261.17` | `1245.40` | `0.000000` | -35,536.51 USD | `-1.49%` | `10X Cross` |
| `934` | `0x3e2f...b269` | `SHORT` | 2,374,924.03 USD | `1,925.51` | `1134.87` | `1245.40` | `2931.77` | -189,725.18 USD | `-7.99%` | `10X Cross` |
| `945` | `0x4f12...618b` | `SHORT` | 2,362,006.37 USD | `1,896.28` | `1608.30` | `1245.40` | `2116.73` | 687,778.02 USD | `+29.12%` | `3X Cross` |
| `949` | `0x866d...d6e1` | `LONG` | 2,344,647.25 USD | `1,802.05` | `674.73` | `1245.40` | `125.55` | 1,128,745.94 USD | `+48.14%` | `10X Cross` |
| `1015` | `0x2309...a2d9` | `LONG` | 2,178,335.46 USD | `1,750.37` | `1186.09` | `1245.40` | `814.20` | 102,241.35 USD | `+4.69%` | `8X Cross` |
| `1035` | `0x2edd...8179` | `SHORT` | 2,116,590.85 USD | `1,701.85` | `1261.58` | `1245.40` | `3043.91` | 30,428.01 USD | `+1.44%` | `10X Cross` |
| `1039` | `0x023a...2355` | `SHORT` | 2,109,957.44 USD | `1,696.38` | `1313.00` | `1245.40` | `5834.49` | 117,389.85 USD | `+5.56%` | `10X Cross` |
| `1070` | `0x3e47...aaf6` | `LONG` | 2,041,422.93 USD | `1,636.28` | `1278.38` | `1245.40` | `1041.82` | -50,368.86 USD | `-2.47%` | `10X Cross` |
| `1077` | `0xa271...a3f7` | `LONG` | 2,032,109.21 USD | `1,631.43` | `1190.60` | `1245.40` | `910.31` | 89,727.40 USD | `+4.42%` | `4X Cross` |
| `1095` | `0x7f75...9edf` | `LONG` | 1,999,196.10 USD | `1,605.78` | `1199.97` | `1245.40` | `976.98` | 72,304.21 USD | `+3.62%` | `10X Cross` |
| `1098` | `0x265e...7f70` | `LONG` | 1,995,127.34 USD | `1,601.74` | `1388.09` | `1245.40` | `0.000000` | -228,237.66 USD | `-11.44%` | `3X Cross` |
| `1106` | `0x6646...6de5` | `SHORT` | 1,988,160.00 USD | `1,600.00` | `660.64` | `1245.40` | `4378.40` | -931,135.03 USD | `-46.83%` | `10X Cross` |
| `1135` | `0xab59...59b5` | `LONG` | 1,952,893.23 USD | `1,565.32` | `1342.15` | `1245.40` | `826.19` | -148,001.99 USD | `-7.58%` | `10X Cross` |
| `1139` | `0xdf57...93f5` | `LONG` | 1,949,423.84 USD | `1,579.76` | `1218.38` | `1245.40` | `780.15` | 24,667.86 USD | `+1.27%` | `3X Isolated` |
| `1147` | `0xfe7c...b7ae` | `SHORT` | 1,932,348.26 USD | `1,562.63` | `1350.61` | `1245.40` | `7361.24` | 178,153.57 USD | `+9.22%` | `10X Cross` |
| `1185` | `0xcf67...eb24` | `LONG` | 1,868,400.00 USD | `1,500.00` | `887.05` | `1245.40` | `660.63` | 537,828.63 USD | `+28.79%` | `10X Cross` |
| `1276` | `0x2ab7...c2f8` | `LONG` | 1,744,055.10 USD | `1,400.51` | `813.26` | `1245.40` | `804.46` | 605,073.42 USD | `+34.69%` | `3X Cross` |
| `1288` | `0x11be...8b1d` | `LONG` | 1,715,797.59 USD | `1,375.83` | `1206.55` | `1245.40` | `1134.43` | 55,789.64 USD | `+3.25%` | `10X Isolated` |
| `1407` | `0xe065...0f85` | `SHORT` | 1,572,707.02 USD | `1,262.61` | `1087.02` | `1245.40` | `1821.41` | -200,230.89 USD | `-12.73%` | `10X Cross` |
| `1409` | `0x039c...0ebd` | `SHORT` | 1,570,419.99 USD | `1,262.70` | `1238.67` | `1245.40` | `3649.99` | -6,357.55 USD | `-0.40%` | `10X Cross` |
| `1435` | `0x7277...0b98` | `SHORT` | 1,537,895.69 USD | `1,234.96` | `1298.48` | `1245.40` | `2435.37` | 65,673.73 USD | `+4.27%` | `10X Cross` |
| `1465` | `0x5975...9abd` | `LONG` | 1,496,520.00 USD | `1,200.00` | `1179.54` | `1245.40` | `472.23` | 81,077.21 USD | `+5.42%` | `5X Cross` |
| `1513` | `0x69cc...14fd` | `SHORT` | 1,435,440.96 USD | `1,161.36` | `675.33` | `1245.40` | `8126.22` | -651,135.43 USD | `-45.36%` | `10X Cross` |
| `1516` | `0x3fc5...c0c1` | `SHORT` | 1,432,219.52 USD | `1,148.44` | `1264.34` | `1245.40` | `3092.59` | 19,794.25 USD | `+1.38%` | `10X Cross` |
| `1520` | `0x71df...a23d` | `SHORT` | 1,428,972.11 USD | `1,098.28` | `513.50` | `1245.40` | `2549.10` | -865,001.92 USD | `-60.53%` | `2X Cross` |
| `1536` | `0xe35c...a1d3` | `LONG` | 1,409,726.65 USD | `1,127.06` | `1318.20` | `1245.40` | `694.35` | -75,968.70 USD | `-5.39%` | `2X Isolated` |
| `1545` | `0x5f94...4b96` | `LONG` | 1,396,541.09 USD | `1,115.27` | `538.00` | `1245.40` | `0.000000` | 796,523.46 USD | `+57.04%` | `10X Cross` |
| `1555` | `0x2847...d47b` | `LONG` | 1,385,858.36 USD | `1,115.02` | `1233.28` | `1245.40` | `0.000000` | 10,722.75 USD | `+0.77%` | `5X Cross` |
| `1573` | `0x266b...efcb` | `LONG` | 1,366,860.00 USD | `1,100.00` | `863.84` | `1245.40` | `300.93` | 416,635.24 USD | `+30.48%` | `10X Cross` |
| `1576` | `0x15e9...d016` | `LONG` | 1,362,162.43 USD | `1,095.25` | `1240.50` | `1245.40` | `966.89` | 3,504.80 USD | `+0.26%` | `10X Cross` |
| `1587` | `0xfc27...9d9d` | `SHORT` | 1,344,083.14 USD | `1,081.67` | `1316.44` | `1245.40` | `16879.29` | 79,871.69 USD | `+5.94%` | `10X Cross` |
| `1591` | `0xbfc7...80b4` | `SHORT` | 1,338,052.50 USD | `1,075.00` | `558.03` | `1245.40` | `6245.76` | -738,173.77 USD | `-55.17%` | `10X Cross` |
| `1627` | `0xdf83...3cff` | `SHORT` | 1,300,101.33 USD | `1,053.14` | `1252.15` | `1245.40` | `1823.61` | 18,590.65 USD | `+1.43%` | `10X Cross` |
| `1631` | `0x51f6...2b39` | `SHORT` | 1,297,243.99 USD | `1,045.49` | `1302.39` | `1245.40` | `2767.01` | 64,392.80 USD | `+4.96%` | `10X Cross` |
| `1646` | `0x17f0...094f` | `LONG` | 1,280,672.73 USD | `984.30` | `1287.23` | `1245.40` | `536.76` | 13,652.57 USD | `+1.07%` | `5X Cross` |
| `1678` | `0xe282...df29` | `LONG` | 1,251,900.00 USD | `1,000.00` | `420.99` | `1245.40` | `175.81` | 830,913.14 USD | `+66.37%` | `10X Cross` |
| `1680` | `0x123d...3bff` | `SHORT` | 1,250,042.82 USD | `1,009.32` | `490.16` | `1245.40` | `4362.42` | -755,316.95 USD | `-60.42%` | `10X Cross` |
| `1784` | `0x757d...94ba` | `LONG` | 1,141,912.50 USD | `925.00` | `1558.31` | `1245.40` | `0.000000` | -299,528.09 USD | `-26.23%` | `10X Cross` |
| `1807` | `0xb911...5525` | `LONG` | 1,122,390.00 USD | `900.00` | `1294.82` | `1245.40` | `1070.30` | -42,947.82 USD | `-3.83%` | `10X Cross` |
| `1851` | `0xcf0a...856f` | `LONG` | 1,084,668.86 USD | `871.15` | `1292.19` | `1245.40` | `938.49` | -41,025.98 USD | `-3.78%` | `4X Cross` |
| `1864` | `0x601c...4f54` | `SHORT` | 1,072,817.75 USD | `824.42` | `615.11` | `1245.40` | `3003.21` | -565,704.99 USD | `-52.73%` | `5X Cross` |
| `1869` | `0xdf95...7d72` | `SHORT` | 1,068,698.13 USD | `860.05` | `1074.31` | `1245.40` | `46181.81` | -144,737.73 USD | `-13.54%` | `10X Cross` |
| `1883` | `0xb695...a92d` | `LONG` | 1,055,159.68 USD | `853.62` | `1249.35` | `1245.40` | `0.000000` | -11,314.59 USD | `-1.07%` | `10X Cross` |
| `1915` | `0xabdb...84ac` | `LONG` | 1,032,828.80 USD | `793.69` | `711.79` | `1245.40` | `664.33` | 467,888.44 USD | `+45.30%` | `3X Cross` |
| `1948` | `0xae55...2236` | `LONG` | 1,010,883.40 USD | `817.47` | `1467.80` | `1245.40` | `0.000000` | -188,997.82 USD | `-18.70%` | `10X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `1330.10` | 53.20 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Long: 0.05K USD at 1330.1000 USD [API] | `2026-10-28 04:31:27` |
| `ANNOUNCEMENT` | `INFO` | `1330.10` | 26.60 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Long: 0.03K USD at 1330.1000 USD [API] | `2026-10-28 04:31:27` |
| `ANNOUNCEMENT` | `INFO` | `1330.10` | 26.60 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Long: 0.03K USD at 1330.1000 USD [API] | `2026-10-28 04:31:27` |
| `ANNOUNCEMENT` | `INFO` | `1330.10` | 305.92 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Long: 0.31K USD at 1330.1000 USD [API] | `2026-10-28 04:31:27` |
| `ANNOUNCEMENT` | `INFO` | `1330.10` | 79.81 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Long: 0.08K USD at 1330.1000 USD [API] | `2026-10-28 04:31:27` |
| `ANNOUNCEMENT` | `INFO` | `1279.40` | 1,266.61 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 1.27K USD at 1279.4000 USD [API] | `2026-10-11 16:28:56` |
| `ANNOUNCEMENT` | `INFO` | `1279.40` | 12.79 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 0.01K USD at 1279.4000 USD [API] | `2026-10-11 16:28:56` |
| `ANNOUNCEMENT` | `INFO` | `1279.40` | 89.56 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 0.09K USD at 1279.4000 USD [API] | `2026-10-11 16:28:56` |
| `ANNOUNCEMENT` | `INFO` | `1279.40` | 729.26 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 0.73K USD at 1279.4000 USD [API] | `2026-10-11 16:28:56` |
| `ANNOUNCEMENT` | `INFO` | `1279.20` | 14,736.38 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 14.74K USD at 1279.2000 USD [API] | `2026-10-11 16:28:56` |
| `ANNOUNCEMENT` | `INFO` | `1279.20` | 268.63 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 0.27K USD at 1279.2000 USD [API] | `2026-10-11 16:28:56` |
| `ANNOUNCEMENT` | `INFO` | `1279.20` | 11,039.50 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 11.04K USD at 1279.2000 USD [API] | `2026-10-11 16:28:56` |
| `ANNOUNCEMENT` | `INFO` | `446.31` | 473.09 USD | `-` | `NEWS_INTEL` | `-` | #ZEC Liquidated Short: 0.47K USD at 446.3100 USD [API] | `2026-01-09 06:33:42` |


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
| `5m` | `BALANCED` | 0.00 USD | 1,750.00 USD | 1,750.00 USD | 1,750.00 USD | `1` | `2026-10-29 21:15:00 UTC - 2026-10-29 21:20:00 UTC` |
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
  * Current Rate: `-2.99K` | Last 24h: `33.19K` | Last 3d: `283.86K` | Last 7d: `777.60K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `-0.0042%` | **USDT OKX** | `0.0013%` |
| **USDT Bybit** | `0.0100%` | **USDT KuCoin** | `-0.0024%` |
| **USDT MEXC** | `-0.0041%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `-0.0113%` | **USDT Bitget** | `0.0100%` |
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
| `5:00 UTC` | `1315.95` | `1319.00` | `1315.95` | `1325.85` | `1312.05` | 22,246,351.59 USD | 13,151,982.06 USD | 9,094,369.53 USD | 4,057,612.52 USD | `+18.24%` | `9B / 1S` |
| `0:00 UTC` | `1320.75` | `1319.74` | `1320.75` | `1325.25` | `1315.95` | 11,564,611.33 USD | 5,754,638.99 USD | 5,809,972.34 USD | -55,333.35 USD | `-0.48%` | `1B / 2S` |
| `5:00 UTC` | `1322.85` | `1320.89` | `1322.85` | `1324.95` | `1316.85` | 7,868,027.33 USD | 4,223,932.72 USD | 3,644,094.61 USD | 579,838.11 USD | `+7.37%` | `3B / 0S` |
| `0:00 UTC` | `1324.95` | `1324.41` | `1324.95` | `1327.05` | `1319.85` | 12,000,472.36 USD | 6,714,467.49 USD | 5,286,004.87 USD | 1,428,462.62 USD | `+11.90%` | `2B / 1S` |
| `5:00 UTC` | `1325.25` | `1325.38` | `1325.25` | `1330.65` | `1320.75` | 11,021,893.68 USD | 5,577,839.59 USD | 5,444,054.10 USD | 133,785.49 USD | `+1.21%` | `3B / 1S` |
| `0:00 UTC` | `1294.05` | `1302.04` | `1294.05` | `1328.55` | `1286.25` | 68,949,402.59 USD | 35,232,633.05 USD | 33,716,769.55 USD | 1,515,863.50 USD | `+2.20%` | `6B / 24S` |
| `5:00 UTC` | `1306.05` | `1306.88` | `1306.05` | `1312.05` | `1300.05` | 17,712,248.68 USD | 9,074,345.66 USD | 8,637,903.02 USD | 436,442.64 USD | `+2.46%` | `3B / 5S` |
| `0:00 UTC` | `1249.20` | `1269.32` | `1249.20` | `1308.60` | `1241.40` | 130,590,816.99 USD | 58,796,845.15 USD | 71,793,971.84 USD | -12,997,126.69 USD | `-9.95%` | `4B / 19S` |
| `5:00 UTC` | `1229.25` | `1237.79` | `1229.25` | `1264.35` | `1206.75` | 149,162,484.89 USD | 77,012,548.38 USD | 72,149,936.51 USD | 4,862,611.87 USD | `+3.26%` | `9B / 11S` |
| `0:00 UTC` | `1249.95` | `1246.74` | `1249.95` | `1255.05` | `1233.15` | 51,473,456.56 USD | 27,027,709.99 USD | 24,445,746.57 USD | 2,581,963.41 USD | `+5.02%` | `3B / 2S` |

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
| `5m` | 912,360.00 USD | 4,490,000.00 USD | **`ACCUMULATION`** |
| `15m` | 915,560.00 USD | 19,540,000.00 USD | **`ACCUMULATION`** |
| `30m` | -12,530,000.00 USD | -13,890,000.00 USD | **`DISTRIBUTION`** |
| `1h` | -13,810,000.00 USD | -21,700,000.00 USD | **`DISTRIBUTION`** |
| `2h` | -16,960,000.00 USD | -17,330,000.00 USD | **`DISTRIBUTION`** |
| `4h` | -10,760,000.00 USD | -33,120,000.00 USD | **`DISTRIBUTION`** |
| `6h` | 7,740,000.00 USD | 48,040,000.00 USD | **`ACCUMULATION`** |
| `8h` | 12,840,000.00 USD | 73,860,000.00 USD | **`ACCUMULATION`** |
| `12h` | 12,420,000.00 USD | 83,650,000.00 USD | **`ACCUMULATION`** |
| `24h` | -2,820,000.00 USD | 40,730,000.00 USD | **`ACCUMULATION`** |
| `1w` | 32,940,000.00 USD | 227,540,000.00 USD | **`ACCUMULATION`** |
| `30d` | 54,250,000.00 USD | -533,450,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+912.36K` | 15m=`+915.56K` | 1h=`-13.81M` | 24h=`-2.82M`
* Futures Capital Netflows: 5m=`+4.49M` | 15m=`+19.54M` | 1h=`-21.70M` | 24h=`+40.73M`
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
  * `2026-10-30 02:15:06 IST`: [morningstar.com] - (Sentiment: `Neutral`)
  * `2026-10-30 02:41:06 IST`: [sec.gov] - (Sentiment: `Neutral`)
  * `2026-10-30 02:41:06 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 02:41:06 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 02:40:06 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:42:06 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:42:06 IST`: [@DeItaone] - (Sentiment: `Neutral`)
  * `2026-10-29 23:42:06 IST`: [@mb_ghalibaf] - (Sentiment: `Neutral`)
  * `2026-10-29 23:42:06 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-29 23:42:06 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-29 23:42:06 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:42:06 IST`: [fxstreet.com] - (Sentiment: `Neutral`)
  * `2026-10-29 21:42:06 IST`: [ForexFactory] - (Sentiment: `Neutral`)
  * `2026-10-29 21:42:06 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-29 21:42:06 IST`: [youtube.com/bankofcanadaofficial] - (Sentiment: `Neutral`)


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
  * Execution Entry: `1250.19` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `1222.21` (Risk Distance: `27.98` pts)
  * +2.5R Take Profit: `1320.15`
  * Mathematical Lot Sizing: **`0.35 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `1258.81` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `1286.79` (Risk Distance: `27.98` pts)
  * +2.5R Take Profit: `1188.85`
  * Mathematical Lot Sizing: **`0.35 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`1264.42`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
