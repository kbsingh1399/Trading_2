# 🏛️ SOVEREIGN CANDIDATE DOSSIER: ZECUSD
**Canonical Key**: `ZECUSD` | **Broker Instrument**: `ZECUSD.p` | **Asset Class**: `Crypto Altcoin`
**Timestamp**: `2026-10-30 04:25:55 IST` (`2026-10-29 22:55:55 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `1239.00` | **Live Ask Quote**: `1240.96` | **Mid Price**: `1239.98`
- **Spread Points**: `196.00` | **Spread BPS**: `15.81 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `1279.94` | VWAP Z-Score: `-0.76` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `22.27` (Volatility Regime: `HIGH_EXPANSION`)
  * 14-Period RSI: `35.81` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `1392.08` | Lower -3.00σ Band: `1167.80`
  * Upper +2.51σ Band: `1373.76` | Lower -2.51σ Band: `1186.12`
  * Upper +2.01σ Band: `1355.07` | Lower -2.01σ Band: `1204.81`
  * Upper +2.00σ Band: `1354.70` | Lower -2.00σ Band: `1205.18`
  * Upper +1.28σ Band: `1327.78` | Lower -1.28σ Band: `1232.09`
  * Upper +1.00σ Band: `1317.32` | Lower -1.00σ Band: `1242.56`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`1264.32` | EMA-20=`1281.81` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`1289.30` (Slope: `+0.0000`) | EMA-100=`1286.16`
  * Institutional Anchors: EMA-144=`1283.09` | EMA-200=`1279.87` (Slope: `-0.1072`) | EMA-233=`1279.56`
- **Range Boundaries**: 24H High=`1396.49` | 24H Low=`1206.89` | Weekly High=`1396.49` | Weekly Low=`1206.89`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `1268.33` (Distance: `-2.06%`)
  * Point of Control (POC) = `1253.07` (Distance: `-0.87%`)
  * Value Area Low (VAL) = `1241.62` (Distance: `+0.05%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`1309.91` | POC=`1246.71` | VAL=`1230.27`
  * Prior Day Extremes: PDH=`1396.49` | PDL=`1206.89` | PDC=`1244.38`
  * Monday Range Blueprint: High=`1267.53` | Mid=`1222.14` | Low=`1176.75`
  * Developing Weekly Value Area: Weekly VAH=`1297.61` | Weekly POC=`1239.01` | Weekly VAL=`1199.46`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`1296.00` | Low=`1238.76`
  * London Session (08:00-16:00 UTC): High=`1244.94` | Low=`1235.02`
  * New York Session (13:00-21:00 UTC): High=`1247.42` | Low=`1232.54`
  * Initial Balance (First Hour): IB High=`1243.70` | IB Low=`1236.26`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `1235.02` - `1244.94`
  * Optimal Trade Entry (OTE 0.705): `1242.46`
  * Structural Invalidation Anchor (0.786): `1249.90`

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
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 04:16:04 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `16` | `0xb83d...6e36` | `SHORT` | 65,466,121.86 USD | `52,385.47` | `1336.45` | `1251.40` | `4015.27` | 4,544,445.54 USD | `+6.94%` | `3X Cross` |
| `23` | `0x5b5d...c060` | `SHORT` | 50,448,623.21 USD | `40,121.38` | `1478.36` | `1251.40` | `5449.22` | 8,865,411.90 USD | `+17.57%` | `3X Cross` |
| `43` | `0x7fda...17d1` | `SHORT` | 29,213,833.40 USD | `23,341.19` | `1262.37` | `1251.40` | `2764.23` | 251,441.69 USD | `+0.86%` | `5X Cross` |
| `84` | `0x60b0...991e` | `LONG` | 20,964,607.16 USD | `16,779.74` | `1179.65` | `1251.40` | `931.03` | 1,170,360.14 USD | `+5.58%` | `10X Cross` |
| `142` | `0xc36a...105b` | `LONG` | 14,373,560.93 USD | `11,510.82` | `1215.14` | `1251.40` | `960.89` | 386,279.91 USD | `+2.69%` | `10X Cross` |
| `159` | `0x9071...5c0b` | `LONG` | 13,148,190.09 USD | `10,517.29` | `1353.83` | `1251.40` | `0.0163` | -1,090,428.78 USD | `-8.29%` | `1X Cross` |
| `179` | `0x8742...8427` | `LONG` | 11,541,077.70 USD | `9,201.21` | `1286.37` | `1251.40` | `708.63` | -295,092.29 USD | `-2.56%` | `10X Cross` |
| `201` | `0x9ffd...ce40` | `LONG` | 10,635,333.46 USD | `8,475.72` | `1256.44` | `1251.40` | `609.94` | -13,880.08 USD | `-0.13%` | `5X Cross` |
| `202` | `0xad59...ba81` | `SHORT` | 10,550,627.50 USD | `8,425.00` | `330.91` | `1251.40` | `2145.69` | -7,762,669.73 USD | `-73.58%` | `10X Cross` |
| `210` | `0xdd53...2b13` | `SHORT` | 10,223,319.12 USD | `8,168.20` | `739.52` | `1251.40` | `8668.49` | -4,182,808.93 USD | `-40.91%` | `3X Cross` |
| `217` | `0xbf73...5d58` | `LONG` | 9,989,600.00 USD | `8,000.00` | `1291.41` | `1251.40` | `316.25` | -341,656.76 USD | `-3.42%` | `10X Cross` |
| `230` | `0x880a...311c` | `SHORT` | 9,680,900.87 USD | `7,707.11` | `1367.50` | `1251.40` | `2269.70` | 858,583.33 USD | `+8.87%` | `10X Cross` |
| `273` | `0x2b61...2f6c` | `LONG` | 8,559,121.80 USD | `6,807.00` | `1453.56` | `1251.40` | `544.38` | -1,335,229.42 USD | `-15.60%` | `10X Cross` |
| `291` | `0x2ae5...83e7` | `LONG` | 8,046,965.52 USD | `6,436.80` | `1391.82` | `1251.40` | `0.000000` | -911,926.47 USD | `-11.33%` | `1X Cross` |
| `338` | `0x26b6...9a13` | `LONG` | 6,794,335.99 USD | `5,433.73` | `1282.23` | `1251.40` | `220.30` | -172,967.24 USD | `-2.55%` | `10X Cross` |
| `354` | `0x45d2...4029` | `SHORT` | 6,534,534.05 USD | `5,227.00` | `833.44` | `1251.40` | `8963.42` | -2,178,156.08 USD | `-33.33%` | `5X Cross` |
| `373` | `0xea00...a918` | `LONG` | 6,247,000.00 USD | `5,000.00` | `739.16` | `1251.40` | `0.000000` | 2,551,184.89 USD | `+40.84%` | `5X Cross` |
| `376` | `0x58b2...11f3` | `LONG` | 6,201,306.92 USD | `4,963.08` | `1257.17` | `1251.40` | `0.000000` | -38,104.27 USD | `-0.61%` | `10X Cross` |
| `380` | `0xecb6...2b00` | `SHORT` | 6,125,292.08 USD | `4,901.41` | `1304.52` | `1251.40` | `6908.33` | 268,712.97 USD | `+4.39%` | `5X Cross` |
| `381` | `0xdd7a...8830` | `LONG` | 6,095,650.30 USD | `4,860.19` | `897.48` | `1251.40` | `785.49` | 1,733,746.62 USD | `+28.44%` | `10X Cross` |
| `434` | `0x4cae...7c34` | `LONG` | 5,035,082.26 USD | `4,004.36` | `999.34` | `1251.40` | `959.60` | 1,033,354.11 USD | `+20.52%` | `10X Cross` |
| `436` | `0x9321...d75a` | `SHORT` | 5,019,200.00 USD | `4,000.00` | `1252.00` | `1251.40` | `2464.81` | -11,208.65 USD | `-0.22%` | `10X Cross` |
| `448` | `0xa61c...66b9` | `LONG` | 4,876,329.60 USD | `3,888.00` | `1148.34` | `1251.40` | `0.000000` | 411,587.46 USD | `+8.44%` | `10X Cross` |
| `469` | `0x9aa5...58af` | `SHORT` | 4,645,551.10 USD | `3,720.31` | `1205.51` | `1251.40` | `3655.78` | -160,664.30 USD | `-3.46%` | `10X Cross` |
| `472` | `0x0153...8052` | `SHORT` | 4,626,053.36 USD | `3,698.18` | `1307.82` | `1251.40` | `2504.73` | 210,517.39 USD | `+4.55%` | `1X Isolated` |
| `542` | `0xd21d...90f1` | `LONG` | 4,069,975.00 USD | `3,250.00` | `1253.64` | `1251.40` | `875.93` | -4,366.73 USD | `-0.11%` | `4X Isolated` |
| `567` | `0xd4c1...3d1d` | `SHORT` | 3,937,934.11 USD | `3,146.32` | `1299.23` | `1251.40` | `2834.61` | 149,855.04 USD | `+3.81%` | `10X Cross` |
| `568` | `0x1338...c48e` | `LONG` | 3,936,157.61 USD | `3,149.43` | `1018.52` | `1251.40` | `820.23` | 728,412.07 USD | `+18.51%` | `4X Isolated` |
| `571` | `0x456f...cdf1` | `LONG` | 3,923,592.31 USD | `3,134.11` | `1268.47` | `1251.40` | `493.75` | -51,917.16 USD | `-1.32%` | `10X Cross` |
| `576` | `0x382b...3e39` | `LONG` | 3,898,604.77 USD | `3,112.41` | `1211.32` | `1251.40` | `0.000000` | 128,471.13 USD | `+3.30%` | `10X Cross` |
| `581` | `0xdbe0...d6d5` | `LONG` | 3,859,489.33 USD | `3,085.37` | `422.97` | `1251.40` | `338.54` | 2,554,484.84 USD | `+66.19%` | `3X Isolated` |
| `590` | `0x27c9...d65d` | `SHORT` | 3,805,822.33 USD | `3,046.12` | `1254.41` | `1251.40` | `1771.10` | 15,264.47 USD | `+0.40%` | `10X Cross` |
| `595` | `0x9c06...0560` | `SHORT` | 3,759,374.52 USD | `2,989.80` | `786.00` | `1251.40` | `2541.11` | -1,409,379.52 USD | `-37.49%` | `10X Cross` |
| `597` | `0x325e...9564` | `LONG` | 3,751,486.93 USD | `3,001.91` | `1301.41` | `1251.40` | `173.50` | -155,222.28 USD | `-4.14%` | `10X Cross` |
| `611` | `0x2e30...4cb5` | `SHORT` | 3,704,084.93 USD | `2,962.32` | `1297.53` | `1251.40` | `2876.03` | 139,608.91 USD | `+3.77%` | `2X Cross` |
| `666` | `0xac48...3201` | `LONG` | 3,411,789.75 USD | `2,727.25` | `1378.58` | `1251.40` | `597.93` | -347,939.34 USD | `-10.20%` | `10X Cross` |
| `708` | `0xa183...0482` | `LONG` | 3,167,880.10 USD | `2,534.00` | `530.25` | `1251.40` | `444.47` | 1,824,217.38 USD | `+57.58%` | `5X Isolated` |
| `722` | `0x0871...e927` | `LONG` | 3,143,500.00 USD | `2,500.00` | `1276.50` | `1251.40` | `0.000000` | -47,750.00 USD | `-1.52%` | `10X Cross` |
| `739` | `0x9b86...6e6e` | `LONG` | 3,077,647.02 USD | `2,463.30` | `637.58` | `1251.40` | `882.40` | 1,507,097.74 USD | `+48.97%` | `3X Cross` |
| `778` | `0xb2f7...af9f` | `SHORT` | 2,896,777.44 USD | `2,313.72` | `746.63` | `1251.40` | `4382.68` | -1,169,288.69 USD | `-40.37%` | `10X Cross` |
| `808` | `0xf48f...10fe` | `LONG` | 2,777,549.48 USD | `2,218.49` | `1517.87` | `1251.40` | `976.93` | -589,837.34 USD | `-21.24%` | `3X Cross` |
| `843` | `0x5bc4...3b0c` | `SHORT` | 2,662,998.85 USD | `2,130.74` | `1089.65` | `1251.40` | `3678.65` | -341,241.27 USD | `-12.81%` | `5X Cross` |
| `852` | `0x8de4...b9aa` | `SHORT` | 2,629,797.17 USD | `2,091.29` | `1331.35` | `1251.40` | `1689.86` | 154,442.53 USD | `+5.87%` | `3X Cross` |
| `865` | `0x4fe2...ac59` | `SHORT` | 2,588,219.56 USD | `2,071.57` | `1478.56` | `1251.40` | `1847.19` | 474,726.66 USD | `+18.34%` | `10X Cross` |
| `892` | `0x9a99...d21a` | `LONG` | 2,498,800.00 USD | `2,000.00` | `1278.44` | `1251.40` | `0.000000` | -58,073.67 USD | `-2.32%` | `10X Cross` |
| `915` | `0x77ee...2902` | `SHORT` | 2,446,938.12 USD | `1,946.03` | `759.84` | `1251.40` | `5296.61` | -968,260.62 USD | `-39.57%` | `10X Cross` |
| `929` | `0x3e2f...b269` | `SHORT` | 2,416,322.50 USD | `1,925.51` | `1134.87` | `1251.40` | `2931.78` | -231,123.64 USD | `-9.57%` | `10X Cross` |
| `936` | `0xe097...d0fe` | `LONG` | 2,394,419.07 USD | `1,913.56` | `1261.17` | `1251.40` | `0.000000` | -18,907.10 USD | `-0.79%` | `10X Cross` |
| `940` | `0x4f12...618b` | `SHORT` | 2,384,572.10 USD | `1,896.28` | `1608.30` | `1251.40` | `2116.75` | 665,212.29 USD | `+27.90%` | `3X Cross` |
| `984` | `0x866d...d6e1` | `LONG` | 2,265,897.67 USD | `1,802.05` | `674.73` | `1251.40` | `215.62` | 1,049,996.36 USD | `+46.34%` | `10X Cross` |
| `1009` | `0x2309...a2d9` | `LONG` | 2,198,114.65 USD | `1,750.37` | `1186.09` | `1251.40` | `815.36` | 122,020.54 USD | `+5.55%` | `8X Cross` |
| `1030` | `0x2edd...8179` | `SHORT` | 2,135,141.01 USD | `1,701.85` | `1261.58` | `1251.40` | `3101.89` | 11,877.84 USD | `+0.56%` | `10X Cross` |
| `1035` | `0x023a...2355` | `SHORT` | 2,119,966.09 USD | `1,696.38` | `1313.00` | `1251.40` | `5230.50` | 107,381.21 USD | `+5.07%` | `10X Cross` |
| `1051` | `0x71d0...8c26` | `SHORT` | 2,086,710.40 USD | `1,670.17` | `1289.75` | `1251.40` | `4663.30` | 67,394.59 USD | `+3.23%` | `10X Cross` |
| `1065` | `0xa271...a3f7` | `LONG` | 2,051,523.23 USD | `1,631.43` | `1190.60` | `1251.40` | `910.32` | 109,141.42 USD | `+5.32%` | `4X Cross` |
| `1066` | `0xfe7c...b7ae` | `SHORT` | 2,050,745.20 USD | `1,640.99` | `1347.05` | `1251.40` | `6975.97` | 159,743.98 USD | `+7.79%` | `10X Cross` |
| `1067` | `0x3e47...aaf6` | `LONG` | 2,049,113.44 USD | `1,636.28` | `1278.38` | `1251.40` | `1050.69` | -42,678.34 USD | `-2.08%` | `10X Cross` |
| `1080` | `0x7f75...9edf` | `LONG` | 2,019,107.77 USD | `1,605.78` | `1199.97` | `1251.40` | `977.67` | 92,215.88 USD | `+4.57%` | `10X Cross` |
| `1099` | `0x6646...6de5` | `SHORT` | 2,002,064.48 USD | `1,600.00` | `660.64` | `1251.40` | `4469.57` | -945,039.51 USD | `-47.20%` | `10X Cross` |
| `1101` | `0x265e...7f70` | `LONG` | 2,001,354.27 USD | `1,601.74` | `1388.09` | `1251.40` | `0.000000` | -222,010.74 USD | `-11.09%` | `3X Cross` |
| `1116` | `0xdf57...93f5` | `LONG` | 1,982,440.82 USD | `1,579.76` | `1218.38` | `1251.40` | `780.17` | 57,684.84 USD | `+2.91%` | `3X Isolated` |
| `1135` | `0xab59...59b5` | `LONG` | 1,960,093.70 USD | `1,565.32` | `1342.15` | `1251.40` | `832.76` | -140,801.51 USD | `-7.18%` | `10X Cross` |
| `1189` | `0xcf67...eb24` | `LONG` | 1,874,231.40 USD | `1,500.00` | `887.05` | `1251.40` | `676.78` | 543,660.03 USD | `+29.01%` | `10X Cross` |
| `1196` | `0xb695...a92d` | `LONG` | 1,853,972.45 USD | `1,483.00` | `1249.80` | `1251.40` | `0.000000` | 513.60 USD | `+0.03%` | `10X Cross` |
| `1273` | `0x2ab7...c2f8` | `LONG` | 1,751,197.70 USD | `1,400.51` | `813.26` | `1251.40` | `792.28` | 612,216.02 USD | `+34.96%` | `3X Cross` |
| `1292` | `0x11be...8b1d` | `LONG` | 1,718,962.00 USD | `1,375.83` | `1206.55` | `1251.40` | `1134.45` | 58,954.04 USD | `+3.43%` | `10X Isolated` |
| `1401` | `0xe065...0f85` | `SHORT` | 1,577,615.54 USD | `1,262.61` | `1087.02` | `1251.40` | `1832.09` | -205,139.41 USD | `-13.00%` | `10X Cross` |
| `1411` | `0x039c...0ebd` | `SHORT` | 1,562,812.33 USD | `1,250.55` | `1239.86` | `1251.40` | `3647.90` | -12,301.05 USD | `-0.79%` | `10X Cross` |
| `1434` | `0x7277...0b98` | `SHORT` | 1,543,453.01 USD | `1,234.96` | `1298.48` | `1251.40` | `2419.69` | 60,116.41 USD | `+3.89%` | `10X Cross` |
| `1463` | `0xdf83...3cff` | `SHORT` | 1,506,118.61 USD | `1,200.86` | `1255.46` | `1251.40` | `1785.98` | 1,517.66 USD | `+0.10%` | `10X Cross` |
| `1467` | `0x5975...9abd` | `LONG` | 1,501,200.00 USD | `1,200.00` | `1179.54` | `1251.40` | `567.19` | 85,757.21 USD | `+5.71%` | `5X Cross` |
| `1504` | `0x69cc...14fd` | `SHORT` | 1,455,997.03 USD | `1,161.36` | `675.33` | `1251.40` | `8099.12` | -671,691.50 USD | `-46.13%` | `10X Cross` |
| `1518` | `0x3fc5...c0c1` | `SHORT` | 1,437,732.04 USD | `1,148.44` | `1264.34` | `1251.40` | `3104.36` | 14,281.74 USD | `+0.99%` | `10X Cross` |
| `1538` | `0x2847...d47b` | `LONG` | 1,421,908.02 USD | `1,135.80` | `1233.86` | `1251.40` | `0.000000` | 20,485.60 USD | `+1.44%` | `5X Cross` |
| `1553` | `0xe35c...a1d3` | `LONG` | 1,408,486.88 USD | `1,127.06` | `1318.20` | `1251.40` | `694.37` | -77,208.47 USD | `-5.48%` | `2X Isolated` |
| `1570` | `0x51f6...2b39` | `SHORT` | 1,394,315.28 USD | `1,115.72` | `1299.77` | `1251.40` | `2669.75` | 55,862.32 USD | `+4.01%` | `10X Cross` |
| `1571` | `0x5f94...4b96` | `LONG` | 1,393,418.34 USD | `1,115.27` | `538.00` | `1251.40` | `0.000000` | 793,400.70 USD | `+56.94%` | `10X Cross` |
| `1573` | `0xfc27...9d9d` | `SHORT` | 1,390,844.93 USD | `1,112.32` | `1315.10` | `1251.40` | `16513.34` | 71,966.83 USD | `+5.17%` | `10X Cross` |
| `1579` | `0x71df...a23d` | `SHORT` | 1,380,977.27 USD | `1,098.28` | `513.50` | `1251.40` | `2551.34` | -817,007.08 USD | `-59.16%` | `2X Cross` |
| `1584` | `0x266b...efcb` | `LONG` | 1,376,870.00 USD | `1,100.00` | `863.84` | `1251.40` | `330.86` | 426,645.24 USD | `+30.99%` | `10X Cross` |
| `1606` | `0xbfc7...80b4` | `SHORT` | 1,351,812.50 USD | `1,075.00` | `558.03` | `1251.40` | `4489.71` | -751,933.77 USD | `-55.62%` | `10X Cross` |
| `1610` | `0xef96...9383` | `SHORT` | 1,350,276.14 USD | `1,078.84` | `1259.08` | `1251.40` | `5175.94` | 8,071.63 USD | `+0.60%` | `10X Cross` |
| `1681` | `0x123d...3bff` | `SHORT` | 1,260,260.83 USD | `1,008.37` | `490.16` | `1251.40` | `4548.49` | -766,000.61 USD | `-60.78%` | `10X Cross` |
| `1690` | `0x668c...ea2e` | `SHORT` | 1,255,800.00 USD | `1,000.00` | `1406.98` | `1251.40` | `4181.42` | 151,181.99 USD | `+12.04%` | `10X Cross` |
| `1691` | `0xe282...df29` | `LONG` | 1,254,200.00 USD | `1,000.00` | `420.99` | `1251.40` | `197.85` | 833,213.14 USD | `+66.43%` | `10X Cross` |
| `1697` | `0xb5ff...d912` | `LONG` | 1,250,400.00 USD | `1,000.00` | `1280.79` | `1251.40` | `452.80` | -30,387.44 USD | `-2.43%` | `2X Cross` |
| `1711` | `0x17f0...094f` | `LONG` | 1,237,658.82 USD | `984.30` | `1287.23` | `1251.40` | `536.80` | -29,361.34 USD | `-2.37%` | `5X Cross` |
| `1793` | `0x757d...94ba` | `LONG` | 1,156,065.00 USD | `925.00` | `1558.31` | `1251.40` | `0.000000` | -285,375.59 USD | `-24.69%` | `10X Cross` |
| `1827` | `0xb911...5525` | `LONG` | 1,130,040.00 USD | `900.00` | `1294.82` | `1251.40` | `1070.32` | -35,297.82 USD | `-3.12%` | `10X Cross` |
| `1868` | `0xcf0a...856f` | `LONG` | 1,095,384.01 USD | `871.15` | `1292.19` | `1251.40` | `998.47` | -30,310.84 USD | `-2.77%` | `4X Cross` |
| `1895` | `0xdf95...7d72` | `SHORT` | 1,071,841.11 USD | `857.37` | `1074.38` | `1251.40` | `45968.21` | -150,697.17 USD | `-14.06%` | `10X Cross` |
| `1935` | `0x601c...4f54` | `SHORT` | 1,036,790.59 USD | `824.42` | `615.11` | `1251.40` | `3111.43` | -529,677.84 USD | `-51.09%` | `5X Cross` |
| `1958` | `0xae55...2236` | `LONG` | 1,021,960.12 USD | `817.47` | `1467.80` | `1251.40` | `0.000000` | -177,921.10 USD | `-17.41%` | `10X Cross` |
| `1998` | `0x0f02...5384` | `LONG` | 1,003,970.24 USD | `800.78` | `1290.36` | `1251.40` | `305.47` | -29,323.83 USD | `-2.92%` | `3X Cross` |
| `2006` | `0x9b0f...db40` | `LONG` | 1,000,320.00 USD | `800.00` | `1268.86` | `1251.40` | `789.60` | -14,769.76 USD | `-1.48%` | `10X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
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
| `5m` | `BALANCED` | 0.00 USD | 1,750.00 USD | 1,750.00 USD | 1,750.00 USD | `1` | `2026-10-29 22:55:00 UTC - 2026-10-29 23:00:00 UTC` |
| `15m` | `BALANCED` | 0.00 USD | 1,750.00 USD | 1,750.00 USD | 1,750.00 USD | `1` | `2026-10-29 22:45:00 UTC - 2026-10-29 23:00:00 UTC` |
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
  * Current Rate: `11.73K` | Last 24h: `33.19K` | Last 3d: `283.86K` | Last 7d: `777.60K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `-0.0011%` | **USDT OKX** | `0.0015%` |
| **USDT Bybit** | `0.0100%` | **USDT KuCoin** | `-0.0051%` |
| **USDT MEXC** | `-0.0011%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `0.0036%` | **USDT Bitget** | `0.0100%` |
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
| `0:00 UTC` | `1249.20` | `1269.32` | `1249.20` | `1308.60` | `1241.40` | 130,590,816.99 USD | 58,796,845.15 USD | 71,793,971.84 USD | -12,997,126.69 USD | `-9.95%` | `4B / 19S` |
| `5:00 UTC` | `1229.25` | `1237.79` | `1229.25` | `1264.35` | `1206.75` | 149,162,484.89 USD | 77,012,548.38 USD | 72,149,936.51 USD | 4,862,611.87 USD | `+3.26%` | `9B / 11S` |
| `0:00 UTC` | `1249.95` | `1248.07` | `1249.95` | `1259.85` | `1233.15` | 61,152,789.32 USD | 32,267,997.87 USD | 28,884,791.45 USD | 3,383,206.41 USD | `+5.53%` | `6B / 4S` |
| `5:00 UTC` | `1273.95` | `1271.85` | `1273.95` | `1286.25` | `1253.25` | 67,607,862.35 USD | 37,234,359.13 USD | 30,373,503.22 USD | 6,860,855.91 USD | `+10.15%` | `6B / 2S` |
| `0:00 UTC` | `1294.65` | `1287.25` | `1294.65` | `1297.05` | `1269.15` | 47,983,765.84 USD | 24,978,907.15 USD | 23,004,858.69 USD | 1,974,048.46 USD | `+4.11%` | `4B / 9S` |
| `5:00 UTC` | `1264.05` | `1267.99` | `1264.05` | `1276.65` | `1260.75` | 31,349,361.20 USD | 15,100,777.24 USD | 16,248,583.96 USD | -1,147,806.72 USD | `-3.66%` | `0B / 1S` |
| `0:00 UTC` | `1261.05` | `1255.07` | `1261.05` | `1269.15` | `1241.25` | 60,510,539.13 USD | 31,467,084.85 USD | 29,043,454.28 USD | 2,423,630.57 USD | `+4.01%` | `3B / 5S` |
| `5:00 UTC` | `1259.85` | `1254.56` | `1259.85` | `1263.15` | `1242.15` | 22,141,749.31 USD | 11,943,317.16 USD | 10,198,432.15 USD | 1,744,885.01 USD | `+7.88%` | `3B / 3S` |
| `0:00 UTC` | `1257.15` | `1255.20` | `1257.15` | `1264.35` | `1245.45` | 28,871,970.63 USD | 12,578,804.66 USD | 16,293,165.97 USD | -3,714,361.32 USD | `-12.86%` | `7B / 2S` |
| `5:00 UTC` | `1249.05` | `1250.84` | `1249.05` | `1254.45` | `1246.95` | 9,490,497.10 USD | 4,312,825.50 USD | 5,177,671.60 USD | -864,846.10 USD | `-9.11%` | `1B / 1S` |

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
| `5m` | 54,980.00 USD | -1,110,000.00 USD | **`DISTRIBUTION`** |
| `15m` | -84,720.00 USD | -6,060,000.00 USD | **`DISTRIBUTION`** |
| `30m` | 177,350.00 USD | -1,870,000.00 USD | **`DISTRIBUTION`** |
| `1h` | 1,540,000.00 USD | -3,680,000.00 USD | **`DISTRIBUTION`** |
| `2h` | -4,470,000.00 USD | 20,140,000.00 USD | **`ACCUMULATION`** |
| `4h` | -9,970,000.00 USD | 5,310,000.00 USD | **`DISTRIBUTION`** |
| `6h` | -7,080,000.00 USD | -25,420,000.00 USD | **`DISTRIBUTION`** |
| `8h` | 8,550,000.00 USD | 78,460,000.00 USD | **`ACCUMULATION`** |
| `12h` | 22,050,000.00 USD | 89,110,000.00 USD | **`ACCUMULATION`** |
| `24h` | 3,290,000.00 USD | 62,650,000.00 USD | **`ACCUMULATION`** |
| `1w` | 36,370,000.00 USD | 247,630,000.00 USD | **`ACCUMULATION`** |
| `30d` | 58,640,000.00 USD | -540,570,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+54.98K` | 15m=`-84.72K` | 1h=`+1.54M` | 24h=`+3.29M`
* Futures Capital Netflows: 5m=`-1.11M` | 15m=`-6.06M` | 1h=`-3.68M` | 24h=`+62.65M`
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
  * `2026-10-30 04:15:19 IST`: [economics.td.com] - (Sentiment: `Neutral`)
  * `2026-10-30 03:30:19 IST`: [investinglive.com] - (Sentiment: `Neutral`)
  * `2026-10-30 04:21:19 IST`: [msn.com] - (Sentiment: `Neutral`)
  * `2026-10-30 04:20:19 IST`: [morningstar.com] - (Sentiment: `Neutral`)
  * `2026-10-30 04:20:19 IST`: [sec.gov] - (Sentiment: `Neutral`)
  * `2026-10-30 01:22:19 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 01:22:19 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 00:22:19 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 00:22:19 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 00:22:19 IST`: [@DeItaone] - (Sentiment: `Neutral`)
  * `2026-10-29 23:22:19 IST`: [@mb_ghalibaf] - (Sentiment: `Neutral`)
  * `2026-10-29 23:22:19 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-29 23:22:19 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-29 23:22:19 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:22:19 IST`: [fxstreet.com] - (Sentiment: `Neutral`)


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
  * Execution Entry: `1241.62` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `1211.96` (Risk Distance: `29.66` pts)
  * +2.5R Take Profit: `1315.77`
  * Mathematical Lot Sizing: **`0.33 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `1268.33` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `1297.99` (Risk Distance: `29.66` pts)
  * +2.5R Take Profit: `1194.18`
  * Mathematical Lot Sizing: **`0.33 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`1249.90`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
