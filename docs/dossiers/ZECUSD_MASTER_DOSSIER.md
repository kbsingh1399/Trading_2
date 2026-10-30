# 🏛️ SOVEREIGN CANDIDATE DOSSIER: ZECUSD
**Canonical Key**: `ZECUSD` | **Broker Instrument**: `ZECUSD.p` | **Asset Class**: `Crypto Altcoin`
**Timestamp**: `2026-10-30 08:00:30 IST` (`2026-10-30 02:30:30 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `1227.90` | **Live Ask Quote**: `1228.69` | **Mid Price**: `1228.30`
- **Spread Points**: `79.00` | **Spread BPS**: `6.43 bps` (Charter Threshold: `12.00 bps`)
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
  * Session VWAP: `1223.69` | VWAP Z-Score: `+0.96` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `22.97` (Volatility Regime: `HIGH_EXPANSION`)
  * 14-Period RSI: `44.26` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `1255.16` | Lower -3.00σ Band: `1192.21`
  * Upper +2.51σ Band: `1250.02` | Lower -2.51σ Band: `1197.35`
  * Upper +2.01σ Band: `1244.78` | Lower -2.01σ Band: `1202.60`
  * Upper +2.00σ Band: `1244.67` | Lower -2.00σ Band: `1202.70`
  * Upper +1.28σ Band: `1237.12` | Lower -1.28σ Band: `1210.26`
  * Upper +1.00σ Band: `1234.18` | Lower -1.00σ Band: `1213.20`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`1231.50` | EMA-20=`1243.46` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`1264.99` (Slope: `+0.0000`) | EMA-100=`1273.15`
  * Institutional Anchors: EMA-144=`1274.30` | EMA-200=`1274.29` (Slope: `-0.4550`) | EMA-233=`1276.78`
- **Range Boundaries**: 24H High=`1396.49` | 24H Low=`1180.03` | Weekly High=`1396.49` | Weekly Low=`1180.03`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `1256.18` (Distance: `-0.83%`)
  * Point of Control (POC) = `1229.90` (Distance: `+1.28%`)
  * Value Area Low (VAL) = `1216.75` (Distance: `+2.38%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`1309.91` | POC=`1246.71` | VAL=`1230.27`
  * Prior Day Extremes: PDH=`1396.49` | PDL=`1206.89` | PDC=`1244.38`
  * Monday Range Blueprint: High=`1267.53` | Mid=`1222.14` | Low=`1176.75`
  * Developing Weekly Value Area: Weekly VAH=`1294.68` | Weekly POC=`1239.01` | Weekly VAL=`1196.53`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`1296.00` | Low=`1180.03`
  * London Session (08:00-16:00 UTC): High=`1233.21` | Low=`1223.38`
  * New York Session (13:00-21:00 UTC): High=`1235.66` | Low=`1220.93`
  * Initial Balance (First Hour): IB High=`1231.98` | IB Low=`1224.61`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `1223.38` - `1233.21`
  * Optimal Trade Entry (OTE 0.705): `1230.75`
  * Structural Invalidation Anchor (0.786): `1238.12`

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
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 07:57:16 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `12` | `0xb83d...6e36` | `SHORT` | 65,424,213.48 USD | `52,385.47` | `1336.45` | `1257.30` | `3886.85` | 4,586,353.92 USD | `+7.01%` | `3X Cross` |
| `22` | `0x5b5d...c060` | `SHORT` | 49,216,896.85 USD | `40,121.38` | `1478.36` | `1257.30` | `5518.20` | 10,097,138.27 USD | `+20.52%` | `3X Cross` |
| `41` | `0x7fda...17d1` | `SHORT` | 28,666,384.60 USD | `22,878.20` | `1261.32` | `1257.30` | `2904.34` | 190,429.54 USD | `+0.66%` | `5X Cross` |
| `82` | `0x60b0...991e` | `LONG` | 20,895,726.32 USD | `16,779.74` | `1179.65` | `1257.30` | `948.81` | 1,101,479.31 USD | `+5.27%` | `10X Cross` |
| `139` | `0xc36a...105b` | `LONG` | 14,374,712.02 USD | `11,510.82` | `1215.14` | `1257.30` | `978.01` | 387,430.99 USD | `+2.70%` | `10X Cross` |
| `155` | `0x9071...5c0b` | `LONG` | 13,157,420.07 USD | `10,517.29` | `1353.83` | `1257.30` | `0.0812` | -1,081,198.80 USD | `-8.22%` | `1X Cross` |
| `178` | `0x8742...8427` | `LONG` | 11,523,595.40 USD | `9,201.21` | `1286.37` | `1257.30` | `718.00` | -312,574.59 USD | `-2.71%` | `10X Cross` |
| `194` | `0x58b2...11f3` | `LONG` | 10,663,560.71 USD | `8,563.08` | `1246.56` | `1257.30` | `383.25` | -10,856.86 USD | `-0.10%` | `10X Cross` |
| `195` | `0x9ffd...ce40` | `LONG` | 10,652,541.15 USD | `8,502.37` | `1250.73` | `1257.30` | `610.09` | 18,349.87 USD | `+0.17%` | `5X Cross` |
| `198` | `0xad59...ba81` | `SHORT` | 10,560,452.73 USD | `8,425.00` | `330.91` | `1257.30` | `2148.12` | -7,772,494.96 USD | `-73.60%` | `10X Cross` |
| `204` | `0xdd53...2b13` | `SHORT` | 10,275,224.90 USD | `8,195.92` | `741.54` | `1257.30` | `9000.69` | -4,197,628.54 USD | `-40.85%` | `3X Cross` |
| `220` | `0x880a...311c` | `SHORT` | 9,621,556.12 USD | `7,707.11` | `1367.50` | `1257.30` | `2233.84` | 917,928.08 USD | `+9.54%` | `10X Cross` |
| `232` | `0xbf73...5d58` | `LONG` | 9,397,500.00 USD | `7,500.00` | `1248.78` | `1257.30` | `138.87` | 31,654.38 USD | `+0.34%` | `10X Cross` |
| `275` | `0x2b61...2f6c` | `LONG` | 8,355,592.50 USD | `6,807.00` | `1453.56` | `1257.30` | `512.35` | -1,538,758.72 USD | `-18.42%` | `10X Cross` |
| `286` | `0x2ae5...83e7` | `LONG` | 8,052,614.46 USD | `6,436.80` | `1391.82` | `1257.30` | `0.000000` | -906,277.54 USD | `-11.25%` | `1X Cross` |
| `329` | `0x26b6...9a13` | `LONG` | 6,797,746.20 USD | `5,433.73` | `1282.23` | `1257.30` | `226.21` | -169,557.03 USD | `-2.49%` | `10X Cross` |
| `345` | `0x45d2...4029` | `SHORT` | 6,539,121.27 USD | `5,227.00` | `833.44` | `1257.30` | `9566.92` | -2,182,743.29 USD | `-33.38%` | `5X Cross` |
| `365` | `0xea00...a918` | `LONG` | 6,176,500.00 USD | `5,000.00` | `739.16` | `1257.30` | `0.000000` | 2,480,684.89 USD | `+40.16%` | `5X Cross` |
| `373` | `0xdd7a...8830` | `LONG` | 6,071,349.35 USD | `4,860.19` | `897.48` | `1257.30` | `789.12` | 1,709,445.68 USD | `+28.16%` | `10X Cross` |
| `393` | `0xecb6...2b00` | `SHORT` | 5,676,446.24 USD | `4,528.53` | `1280.62` | `1257.30` | `7504.77` | 122,858.21 USD | `+2.16%` | `5X Cross` |
| `443` | `0xa61c...66b9` | `LONG` | 4,856,500.80 USD | `3,888.00` | `1148.34` | `1257.30` | `0.000000` | 391,758.66 USD | `+8.07%` | `10X Cross` |
| `463` | `0x9aa5...58af` | `SHORT` | 4,663,354.27 USD | `3,720.31` | `1205.51` | `1257.30` | `3781.45` | -178,467.47 USD | `-3.83%` | `10X Cross` |
| `467` | `0x0153...8052` | `SHORT` | 4,635,668.63 USD | `3,698.18` | `1307.82` | `1257.30` | `2504.79` | 200,902.12 USD | `+4.33%` | `1X Isolated` |
| `520` | `0x469e...58a5` | `SHORT` | 4,216,945.32 USD | `3,363.60` | `1235.64` | `1257.30` | `2125.69` | -60,753.58 USD | `-1.44%` | `10X Cross` |
| `535` | `0xd21d...90f1` | `LONG` | 4,073,765.15 USD | `3,250.00` | `1253.64` | `1257.30` | `876.00` | -576.58 USD | `-0.01%` | `4X Isolated` |
| `555` | `0x1338...c48e` | `LONG` | 3,918,835.75 USD | `3,149.43` | `1018.52` | `1257.30` | `820.29` | 711,090.21 USD | `+18.15%` | `4X Isolated` |
| `556` | `0x456f...cdf1` | `LONG` | 3,916,407.47 USD | `3,170.41` | `1268.13` | `1257.30` | `503.52` | -104,083.43 USD | `-2.66%` | `10X Cross` |
| `565` | `0x325e...9564` | `LONG` | 3,874,595.78 USD | `3,101.91` | `1298.07` | `1257.30` | `239.94` | -151,914.92 USD | `-3.92%` | `10X Cross` |
| `568` | `0xdbe0...d6d5` | `LONG` | 3,867,511.29 USD | `3,085.37` | `422.97` | `1257.30` | `338.61` | 2,562,506.80 USD | `+66.26%` | `3X Isolated` |
| `569` | `0x382b...3e39` | `LONG` | 3,866,125.02 USD | `3,084.30` | `1211.32` | `1257.30` | `0.000000` | 130,041.68 USD | `+3.36%` | `10X Cross` |
| `598` | `0x27c9...d65d` | `SHORT` | 3,714,127.38 USD | `2,963.04` | `1254.41` | `1257.30` | `1736.40` | 2,742.94 USD | `+0.07%` | `10X Cross` |
| `602` | `0x9c06...0560` | `SHORT` | 3,693,897.90 USD | `2,989.80` | `786.00` | `1257.30` | `2659.55` | -1,343,902.90 USD | `-36.38%` | `10X Cross` |
| `607` | `0x2e30...4cb5` | `SHORT` | 3,655,350.40 USD | `2,915.65` | `1288.34` | `1257.30` | `2940.59` | 100,991.60 USD | `+2.76%` | `2X Cross` |
| `624` | `0xd4c1...3d1d` | `SHORT` | 3,551,303.38 USD | `2,833.11` | `1298.52` | `1257.30` | `2902.90` | 127,547.41 USD | `+3.59%` | `10X Cross` |
| `634` | `0x4cae...7c34` | `LONG` | 3,492,227.36 USD | `2,800.27` | `1114.07` | `1257.30` | `857.63` | 372,538.06 USD | `+10.67%` | `10X Cross` |
| `694` | `0xa183...0482` | `LONG` | 3,173,581.60 USD | `2,534.00` | `530.25` | `1257.30` | `444.53` | 1,829,918.88 USD | `+57.66%` | `5X Isolated` |
| `700` | `0xac48...3201` | `LONG` | 3,155,261.60 USD | `2,531.50` | `1378.58` | `1257.30` | `485.10` | -334,610.68 USD | `-10.60%` | `10X Cross` |
| `724` | `0x0871...e927` | `LONG` | 3,088,750.00 USD | `2,500.00` | `1276.50` | `1257.30` | `0.000000` | -102,500.00 USD | `-3.32%` | `10X Cross` |
| `735` | `0x9b86...6e6e` | `LONG` | 3,076,415.37 USD | `2,463.30` | `637.58` | `1257.30` | `882.46` | 1,505,866.09 USD | `+48.95%` | `3X Cross` |
| `778` | `0xb2f7...af9f` | `SHORT` | 2,889,604.91 USD | `2,313.72` | `746.63` | `1257.30` | `4599.40` | -1,162,116.16 USD | `-40.22%` | `10X Cross` |
| `807` | `0xf48f...10fe` | `LONG` | 2,780,802.23 USD | `2,218.49` | `1517.87` | `1257.30` | `1043.26` | -586,584.59 USD | `-21.09%` | `3X Cross` |
| `839` | `0x5bc4...3b0c` | `SHORT` | 2,671,308.74 USD | `2,130.74` | `1089.65` | `1257.30` | `3738.41` | -349,551.16 USD | `-13.09%` | `5X Cross` |
| `858` | `0x8de4...b9aa` | `SHORT` | 2,603,865.18 USD | `2,091.29` | `1331.35` | `1257.30` | `1689.91` | 180,374.53 USD | `+6.93%` | `3X Cross` |
| `867` | `0xdf57...93f5` | `LONG` | 2,575,538.60 USD | `2,054.35` | `1227.36` | `1257.30` | `897.24` | 54,116.55 USD | `+2.10%` | `4X Isolated` |
| `871` | `0x4fe2...ac59` | `SHORT` | 2,559,424.73 USD | `2,071.57` | `1478.56` | `1257.30` | `1875.61` | 503,521.48 USD | `+19.67%` | `10X Cross` |
| `879` | `0xbcd4...0dd2` | `LONG` | 2,540,162.69 USD | `2,033.92` | `1228.20` | `1257.30` | `653.46` | 42,111.87 USD | `+1.66%` | `10X Cross` |
| `895` | `0x9a99...d21a` | `LONG` | 2,477,800.00 USD | `2,000.00` | `1278.44` | `1257.30` | `0.000000` | -79,073.67 USD | `-3.19%` | `10X Cross` |
| `918` | `0x77ee...2902` | `SHORT` | 2,404,320.06 USD | `1,946.03` | `759.84` | `1257.30` | `5464.71` | -925,642.56 USD | `-38.50%` | `10X Cross` |
| `919` | `0x3e2f...b269` | `SHORT` | 2,403,614.13 USD | `1,925.51` | `1134.87` | `1257.30` | `2931.84` | -218,415.28 USD | `-9.09%` | `10X Cross` |
| `939` | `0x4f12...618b` | `SHORT` | 2,332,045.14 USD | `1,896.28` | `1608.30` | `1257.30` | `2116.80` | 717,739.24 USD | `+30.78%` | `3X Cross` |
| `956` | `0xb122...e4ba` | `LONG` | 2,299,047.12 USD | `1,844.55` | `1255.11` | `1257.30` | `981.85` | -16,071.00 USD | `-0.70%` | `10X Cross` |
| `971` | `0x413c...886c` | `LONG` | 2,242,800.00 USD | `1,800.00` | `1206.29` | `1257.30` | `0.000000` | 71,476.78 USD | `+3.19%` | `10X Cross` |
| `980` | `0x866d...d6e1` | `LONG` | 2,212,016.38 USD | `1,802.05` | `674.73` | `1257.30` | `336.75` | 996,115.06 USD | `+45.03%` | `10X Cross` |
| `1000` | `0x2309...a2d9` | `LONG` | 2,156,105.77 USD | `1,750.37` | `1186.09` | `1257.30` | `820.27` | 80,011.66 USD | `+3.71%` | `8X Cross` |
| `1034` | `0x2edd...8179` | `SHORT` | 2,066,923.24 USD | `1,654.73` | `1261.58` | `1257.30` | `2921.07` | 20,649.99 USD | `+1.00%` | `10X Cross` |
| `1043` | `0x265e...7f70` | `LONG` | 2,056,581.47 USD | `1,651.74` | `1382.98` | `1257.30` | `0.000000` | -227,741.29 USD | `-11.07%` | `3X Cross` |
| `1047` | `0xfe7c...b7ae` | `SHORT` | 2,051,493.10 USD | `1,642.64` | `1346.92` | `1257.30` | `6021.29` | 161,015.52 USD | `+7.85%` | `10X Cross` |
| `1052` | `0x3e47...aaf6` | `LONG` | 2,043,550.09 USD | `1,636.28` | `1278.38` | `1257.30` | `1055.66` | -48,241.69 USD | `-2.36%` | `10X Cross` |
| `1066` | `0x6646...6de5` | `SHORT` | 2,005,280.00 USD | `1,600.00` | `660.64` | `1257.30` | `4067.39` | -948,255.03 USD | `-47.29%` | `10X Cross` |
| `1068` | `0x7f75...9edf` | `LONG` | 2,001,444.19 USD | `1,605.78` | `1199.97` | `1257.30` | `980.52` | 74,552.30 USD | `+3.72%` | `10X Cross` |
| `1071` | `0x023a...2355` | `SHORT` | 1,999,153.24 USD | `1,594.90` | `1310.00` | `1257.30` | `4524.49` | 90,158.89 USD | `+4.51%` | `10X Cross` |
| `1095` | `0xab59...59b5` | `LONG` | 1,962,075.71 USD | `1,565.32` | `1342.15` | `1257.30` | `847.35` | -138,819.51 USD | `-7.08%` | `10X Cross` |
| `1164` | `0xb695...a92d` | `LONG` | 1,857,309.20 USD | `1,483.00` | `1249.80` | `1257.30` | `0.000000` | 3,850.34 USD | `+0.21%` | `10X Cross` |
| `1169` | `0x7277...0b98` | `SHORT` | 1,850,122.70 USD | `1,475.73` | `1287.86` | `1257.30` | `2226.82` | 50,409.42 USD | `+2.72%` | `10X Cross` |
| `1173` | `0xcf67...eb24` | `LONG` | 1,843,050.00 USD | `1,500.00` | `887.05` | `1257.30` | `744.86` | 512,478.63 USD | `+27.81%` | `10X Cross` |
| `1187` | `0x71d0...8c26` | `SHORT` | 1,811,572.03 USD | `1,445.25` | `1263.46` | `1257.30` | `4916.53` | 14,444.80 USD | `+0.80%` | `10X Cross` |
| `1207` | `0x3205...40bb` | `SHORT` | 1,794,773.83 USD | `1,431.81` | `1237.02` | `1257.30` | `2297.58` | -23,591.22 USD | `-1.31%` | `10X Cross` |
| `1242` | `0x2ab7...c2f8` | `LONG` | 1,752,076.66 USD | `1,400.51` | `813.26` | `1257.30` | `795.00` | 613,094.98 USD | `+34.99%` | `3X Cross` |
| `1255` | `0x11be...8b1d` | `LONG` | 1,714,284.18 USD | `1,375.83` | `1206.55` | `1257.30` | `1134.51` | 54,276.22 USD | `+3.17%` | `10X Isolated` |
| `1292` | `0xfc27...9d9d` | `SHORT` | 1,650,643.35 USD | `1,319.43` | `1298.53` | `1257.30` | `16140.18` | 62,673.43 USD | `+3.80%` | `10X Cross` |
| `1313` | `0x38f9...cb04` | `SHORT` | 1,618,907.78 USD | `1,291.51` | `1238.48` | `1257.30` | `1921.21` | -19,396.05 USD | `-1.20%` | `10X Cross` |
| `1339` | `0x039c...0ebd` | `SHORT` | 1,590,560.87 USD | `1,268.93` | `1239.61` | `1257.30` | `3719.79` | -17,582.11 USD | `-1.11%` | `10X Cross` |
| `1347` | `0xe065...0f85` | `SHORT` | 1,581,912.45 USD | `1,262.61` | `1087.02` | `1257.30` | `1628.61` | -209,436.33 USD | `-13.24%` | `10X Cross` |
| `1355` | `0xf29c...9971` | `LONG` | 1,565,500.00 USD | `1,250.00` | `1245.71` | `1257.30` | `0.000000` | 8,366.68 USD | `+0.53%` | `10X Cross` |
| `1422` | `0x266b...efcb` | `LONG` | 1,501,080.00 USD | `1,200.00` | `893.76` | `1257.30` | `441.13` | 428,570.30 USD | `+28.55%` | `10X Cross` |
| `1431` | `0x5975...9abd` | `LONG` | 1,495,920.00 USD | `1,200.00` | `1179.54` | `1257.30` | `626.08` | 80,477.21 USD | `+5.38%` | `5X Cross` |
| `1448` | `0x2847...d47b` | `LONG` | 1,478,448.30 USD | `1,186.27` | `1232.07` | `1257.30` | `0.000000` | 16,879.80 USD | `+1.14%` | `5X Cross` |
| `1468` | `0x69cc...14fd` | `SHORT` | 1,449,841.82 USD | `1,161.36` | `675.33` | `1257.30` | `8264.69` | -665,536.30 USD | `-45.90%` | `10X Cross` |
| `1487` | `0x3fc5...c0c1` | `SHORT` | 1,430,956.24 USD | `1,148.44` | `1264.34` | `1257.30` | `2993.33` | 21,057.54 USD | `+1.47%` | `10X Cross` |
| `1503` | `0xe35c...a1d3` | `LONG` | 1,412,731.62 USD | `1,127.06` | `1318.20` | `1257.30` | `694.43` | -72,963.73 USD | `-5.16%` | `2X Isolated` |
| `1525` | `0x5f94...4b96` | `LONG` | 1,392,860.70 USD | `1,115.27` | `538.00` | `1257.30` | `0.000000` | 792,843.07 USD | `+56.92%` | `10X Cross` |
| `1553` | `0x71df...a23d` | `SHORT` | 1,356,924.94 USD | `1,098.28` | `513.50` | `1257.30` | `2559.36` | -792,954.75 USD | `-58.44%` | `2X Cross` |
| `1560` | `0x51f6...2b39` | `SHORT` | 1,349,745.96 USD | `1,076.61` | `1299.77` | `1257.30` | `2478.14` | 49,597.71 USD | `+3.67%` | `10X Cross` |
| `1574` | `0xbfc7...80b4` | `SHORT` | 1,328,162.50 USD | `1,075.00` | `558.03` | `1257.30` | `3222.08` | -728,283.77 USD | `-54.83%` | `10X Cross` |
| `1633` | `0x123d...3bff` | `SHORT` | 1,258,415.30 USD | `1,009.64` | `491.08` | `1257.30` | `4424.74` | -762,597.39 USD | `-60.60%` | `10X Cross` |
| `1640` | `0x9321...d75a` | `SHORT` | 1,250,900.00 USD | `1,000.00` | `1242.18` | `1257.30` | `6346.75` | -8,716.27 USD | `-0.70%` | `10X Cross` |
| `1646` | `0xe282...df29` | `LONG` | 1,249,200.00 USD | `1,000.00` | `420.99` | `1257.30` | `853.55` | 828,213.14 USD | `+66.30%` | `10X Cross` |
| `1665` | `0x668c...ea2e` | `SHORT` | 1,235,500.00 USD | `1,000.00` | `1406.98` | `1257.30` | `4177.38` | 171,481.99 USD | `+13.88%` | `10X Cross` |
| `1689` | `0x17f0...094f` | `LONG` | 1,212,362.31 USD | `984.30` | `1287.23` | `1257.30` | `536.86` | -54,657.85 USD | `-4.51%` | `5X Cross` |
| `1740` | `0x757d...94ba` | `LONG` | 1,159,672.50 USD | `925.00` | `1558.31` | `1257.30` | `0.000000` | -281,768.09 USD | `-24.30%` | `10X Cross` |
| `1749` | `0xaa82...9556` | `LONG` | 1,153,683.89 USD | `924.13` | `1254.72` | `1257.30` | `185.85` | -5,842.79 USD | `-0.51%` | `10X Cross` |
| `1804` | `0xb911...5525` | `LONG` | 1,114,560.00 USD | `900.00` | `1294.82` | `1257.30` | `1070.38` | -50,777.82 USD | `-4.56%` | `10X Cross` |
| `1839` | `0xcf0a...856f` | `LONG` | 1,085,801.36 USD | `871.15` | `1292.19` | `1257.30` | `1010.65` | -39,893.49 USD | `-3.67%` | `4X Cross` |
| `1841` | `0xef96...9383` | `SHORT` | 1,084,135.53 USD | `868.42` | `1259.08` | `1257.30` | `5546.38` | 9,276.26 USD | `+0.86%` | `10X Cross` |
| `1859` | `0xdf95...7d72` | `SHORT` | 1,069,649.23 USD | `853.34` | `1074.39` | `1257.30` | `46727.66` | -152,826.58 USD | `-14.29%` | `10X Cross` |
| `1908` | `0x601c...4f54` | `SHORT` | 1,027,557.09 USD | `824.42` | `615.11` | `1257.30` | `3185.34` | -520,444.34 USD | `-50.65%` | `5X Cross` |
| `1917` | `0xae55...2236` | `LONG` | 1,022,677.53 USD | `817.47` | `1467.80` | `1257.30` | `0.000000` | -177,203.68 USD | `-17.33%` | `10X Cross` |
| `1954` | `0x0f02...5384` | `LONG` | 1,003,766.04 USD | `800.78` | `1290.36` | `1257.30` | `315.70` | -29,528.03 USD | `-2.94%` | `3X Cross` |
| `1958` | `0x9b0f...db40` | `LONG` | 1,002,400.00 USD | `800.00` | `1268.86` | `1257.30` | `804.27` | -12,689.76 USD | `-1.27%` | `10X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
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
  * 24H Horizon: Short MP=`1403.54` (Vol: 3,000,000.00 USD, Dist: `+12.58%`) | Long MP=`1200.05` (Vol: 597,500.00 USD, Dist: `--3.74%`)
  * 48H Horizon: Short MP=`1403.54` (Vol: 3,000,000.00 USD, Dist: `+12.58%`) | Long MP=`1200.05` (Vol: 597,500.00 USD, Dist: `--3.74%`)
  * 3D Horizon: Short MP=`1403.54` (Vol: 3,000,000.00 USD, Dist: `+12.58%`) | Long MP=`1195.13` (Vol: 1,600,000.00 USD, Dist: `--4.14%`)
  * 7D Horizon: Short MP=`1404.10` (Vol: 3,000,000.00 USD, Dist: `+12.62%`) | Long MP=`1200.46` (Vol: 3,000,000.00 USD, Dist: `--3.71%`)
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
| `5m` | `BALANCED` | 0.00 USD | 1,750.00 USD | 1,750.00 USD | 1,750.00 USD | `1` | `2026-10-30 02:25:00 UTC - 2026-10-30 02:30:00 UTC` |
| `15m` | `BALANCED` | 0.00 USD | 1,750.00 USD | 1,750.00 USD | 1,750.00 USD | `1` | `2026-10-30 02:15:00 UTC - 2026-10-30 02:30:00 UTC` |
| `1h` | `BALANCED` | 0.00 USD | 1,750.00 USD | 1,750.00 USD | 1,750.00 USD | `1` | `2026-10-30 02:00:00 UTC - 2026-10-30 03:00:00 UTC` |
| `4h` | `BALANCED` | 0.00 USD | 1,750.00 USD | 1,750.00 USD | 1,750.00 USD | `1` | `2026-10-30 00:00:00 UTC - 2026-10-30 04:00:00 UTC` |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `0 USD` | Total OI Tokens: `-`
  * 1h OI Change: `0.00%` | 4h OI Change: `0.00%` | 24h OI Change: `0.00%`
  * Exchange Breakdown: Binance=`-` | Bybit=`-` | OKX=`-` | Hyperliquid=`-`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `83.40K` | Last 24h: `133.88K` | Last 3d: `245.74K` | Last 7d: `771.70K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0095%` | **USDT OKX** | `0.0100%` |
| **USDT Bybit** | `0.0100%` | **USDT KuCoin** | `0.0100%` |
| **USDT MEXC** | `0.0095%` | **USDT BingX** | `0.0100%` |
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
| `0:00 UTC` | `1224.15` | `1225.28` | `1224.15` | `1233.15` | `1216.35` | 41,862,859.26 USD | 20,823,357.89 USD | 21,039,501.37 USD | -216,143.49 USD | `-0.52%` | `5B / 3S` |
| `5:00 UTC` | `1209.15` | `1203.96` | `1209.15` | `1231.05` | `1180.35` | 101,980,019.94 USD | 48,295,180.78 USD | 53,684,839.16 USD | -5,389,658.38 USD | `-5.29%` | `3B / 24S` |
| `0:00 UTC` | `1197.75` | `1211.98` | `1197.75` | `1236.15` | `1189.35` | 90,739,097.90 USD | 52,854,086.90 USD | 37,885,011.00 USD | 14,969,075.89 USD | `+16.50%` | `25B / 1S` |
| `5:00 UTC` | `1232.55` | `1227.83` | `1232.55` | `1237.35` | `1215.45` | 35,400,223.44 USD | 18,306,250.09 USD | 17,093,973.35 USD | 1,212,276.73 USD | `+3.42%` | `7B / 4S` |
| `0:00 UTC` | `1230.15` | `1232.52` | `1230.15` | `1240.05` | `1225.05` | 27,822,128.62 USD | 14,746,863.10 USD | 13,075,265.52 USD | 1,671,597.57 USD | `+6.01%` | `5B / 1S` |
| `5:00 UTC` | `1219.95` | `1220.53` | `1219.95` | `1230.45` | `1215.45` | 25,624,282.39 USD | 13,502,208.52 USD | 12,122,073.88 USD | 1,380,134.64 USD | `+5.39%` | `6B / 3S` |
| `0:00 UTC` | `1245.15` | `1232.68` | `1245.15` | `1249.05` | `1206.75` | 51,931,159.61 USD | 26,761,787.01 USD | 25,169,372.61 USD | 1,592,414.40 USD | `+3.07%` | `20B / 9S` |
| `5:00 UTC` | `1236.45` | `1237.15` | `1236.45` | `1245.15` | `1230.45` | 21,904,768.45 USD | 9,625,705.12 USD | 12,279,063.33 USD | -2,653,358.20 USD | `-12.11%` | `1B / 0S` |
| `0:00 UTC` | `1228.65` | `1236.25` | `1228.65` | `1253.25` | `1219.35` | 45,146,863.08 USD | 23,450,812.50 USD | 21,696,050.59 USD | 1,754,761.91 USD | `+3.89%` | `18B / 9S` |
| `5:00 UTC` | `1254.75` | `1256.08` | `1254.75` | `1263.45` | `1247.85` | 26,296,000.42 USD | 15,016,207.50 USD | 11,279,792.92 USD | 3,736,414.58 USD | `+14.21%` | `5B / 3S` |

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
| `5m` | 679,960.00 USD | 3,500,000.00 USD | **`ACCUMULATION`** |
| `15m` | 3,460,000.00 USD | -1,940,000.00 USD | **`ACCUMULATION`** |
| `30m` | 5,690,000.00 USD | -9,370,000.00 USD | **`DISTRIBUTION`** |
| `1h` | 6,740,000.00 USD | 7,490,000.00 USD | **`ACCUMULATION`** |
| `2h` | 7,430,000.00 USD | 16,550,000.00 USD | **`ACCUMULATION`** |
| `4h` | -302,240.00 USD | -543,630.00 USD | **`DISTRIBUTION`** |
| `6h` | -8,510,000.00 USD | -212,220.00 USD | **`DISTRIBUTION`** |
| `8h` | -10,590,000.00 USD | -18,750,000.00 USD | **`DISTRIBUTION`** |
| `12h` | 15,370,000.00 USD | 79,410,000.00 USD | **`ACCUMULATION`** |
| `24h` | 11,270,000.00 USD | 106,110,000.00 USD | **`ACCUMULATION`** |
| `1w` | 33,820,000.00 USD | 224,100,000.00 USD | **`ACCUMULATION`** |
| `30d` | 61,520,000.00 USD | -540,780,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+679.96K` | 15m=`+3.46M` | 1h=`+6.74M` | 24h=`+11.27M`
* Futures Capital Netflows: 5m=`+3.50M` | 15m=`-1.94M` | 1h=`+7.49M` | 24h=`+106.11M`
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
  * `2026-10-30 07:16:25 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-30 07:52:25 IST`: [kathleenhays.substack.com] - (Sentiment: `Neutral`)
  * `2026-10-30 07:52:25 IST`: [rba.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 07:52:25 IST`: [abs.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 07:51:25 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 07:51:25 IST`: [@NodeWire] - (Sentiment: `Neutral`)
  * `2026-10-30 07:51:25 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 07:51:25 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 07:51:25 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-30 07:51:25 IST`: [media.rabobank.com] - (Sentiment: `Neutral`)
  * `2026-10-30 04:53:25 IST`: [economics.td.com] - (Sentiment: `Neutral`)
  * `2026-10-30 03:53:25 IST`: [investinglive.com] - (Sentiment: `Neutral`)
  * `2026-10-30 03:53:25 IST`: [msn.com] - (Sentiment: `Neutral`)
  * `2026-10-30 02:53:25 IST`: [morningstar.com] - (Sentiment: `Neutral`)
  * `2026-10-30 01:53:25 IST`: [sec.gov] - (Sentiment: `Neutral`)


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
  * Execution Entry: `1216.75` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `1188.00` (Risk Distance: `28.75` pts)
  * +2.5R Take Profit: `1288.61`
  * Mathematical Lot Sizing: **`0.34 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `1256.18` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `1284.93` (Risk Distance: `28.75` pts)
  * +2.5R Take Profit: `1184.32`
  * Mathematical Lot Sizing: **`0.34 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`1238.12`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
