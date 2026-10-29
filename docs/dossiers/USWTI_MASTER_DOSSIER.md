# 🏛️ SOVEREIGN CANDIDATE DOSSIER: USWTI
**Canonical Key**: `USWTI` | **Broker Instrument**: `USWTI.p` | **Asset Class**: `Energy Commodity`
**Timestamp**: `2026-10-30 03:34:24 IST` (`2026-10-29 22:04:24 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `103.54` | **Live Ask Quote**: `103.57` | **Mid Price**: `103.56`
- **Spread Points**: `30.00` | **Spread BPS**: `2.90 bps` (Charter Threshold: `5.00 bps`)
- **Gate 1 Clearance**: **`PASS`** | **Execution Posture**: `PASSIVE LIMIT ONLY` | **Order Type Allowed**: `BUY_LIMIT / SELL_LIMIT`
- **True Broker Contract Specifications**:
  * Contract Size: `1,000.0` | Digits: `2` | Point: `0.01`
  * Point Value (1.0 Lot): `10.00 USD` | Point Value (0.01 Lot): `0.1000 USD`
  * Allowed Lot Sizing: Min Lot=`0.10` | Step Lot=`0.10` | Max Lot=`50.00`
- **Solvency Defense Ladder**:
  * Hard Floor Stop: `4,775.00 USD` (Zero Open Risk) | Operating Defense Buffer: `4,795.00 USD` (Capital Preservation Mode)
  * Kernel Admission Floor: `4,795.00 USD` (`min(balance, equity) - StressedLoss - 2.00 >= 4,795.00 USD`)
- **Pipeline Health (23_Master_Pipeline_Telemetry.parquet)**: Status=`HEALTHY` | Latency=`4.2 ms` | RAM Usage=`385.0 MB`

---

## 2. Technical Profile, VWAP Dispersion Grid & BTC Ribbon
*(Sources: 11_Technical.parquet, 11_Technical_BTC_Ribbon.parquet)*
- **Session Anchor & Volatility**:
  * Session VWAP: `101.99` | VWAP Z-Score: `+2.32` (Regime: `STRETCH_EXTREME`)
  * 14-Period ATR: `0.3567` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `69.16` (State: `OVERBOUGHT`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `103.91` | Lower -3.00σ Band: `100.08`
  * Upper +2.51σ Band: `103.60` | Lower -2.51σ Band: `100.39`
  * Upper +2.01σ Band: `103.28` | Lower -2.01σ Band: `100.71`
  * Upper +2.00σ Band: `103.27` | Lower -2.00σ Band: `100.72`
  * Upper +1.28σ Band: `102.81` | Lower -1.28σ Band: `101.18`
  * Upper +1.00σ Band: `102.63` | Lower -1.00σ Band: `101.35`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`103.17` | EMA-20=`102.74` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`102.35` (Slope: `+0.0000`) | EMA-100=`102.28`
  * Institutional Anchors: EMA-144=`102.27` | EMA-200=`102.18` (Slope: `+0.1057`) | EMA-233=`102.14`
- **Range Boundaries**: 24H High=`103.64` | 24H Low=`100.46` | Weekly High=`104.23` | Weekly Low=`100.17`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `102.76` (Distance: `+0.78%`)
  * Point of Control (POC) = `102.02` (Distance: `+1.51%`)
  * Value Area Low (VAL) = `101.40` (Distance: `+2.13%`)
  * Auction Positioning: `ABOVE_VALUE (Imbalance)` | Session Bias: **`BULLISH (Above Pivot)`** | Market Regime: `RANGE_EXPANSION`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`103.28` | POC=`102.40` | VAL=`101.64`
  * Prior Day Extremes: PDH=`104.23` | PDL=`100.44` | PDC=`102.65`
  * Monday Range Blueprint: High=`103.88` | Mid=`102.48` | Low=`101.08`
  * Developing Weekly Value Area: Weekly VAH=`103.08` | Weekly POC=`102.03` | Weekly VAL=`101.46`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`102.95` | Low=`101.92`
  * London Session (08:00-16:00 UTC): High=`102.75` | Low=`101.25`
  * New York Session (13:00-21:00 UTC): High=`102.75` | Low=`100.46`
  * Initial Balance (First Hour): IB High=`102.04` | IB Low=`101.67`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `103.14` - `103.97`
  * Optimal Trade Entry (OTE 0.705): `103.77`
  * Structural Invalidation Anchor (0.786): `104.39`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `102.91` | `103.03` | `102.87` | `102.88` | `250` | 25,719.50 USD | -14,519.07 USD | `-56.45%` | 131,474.18 USD | `-0.76` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `5m` | `102.87` | `102.92` | `102.79` | `102.80` | `251` | 25,802.30 USD | -18,157.17 USD | `-70.37%` | 113,317.00 USD | `-0.82` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `5m` | `102.80` | `102.85` | `102.70` | `102.79` | `206` | 21,175.36 USD | 2,117.54 USD | `+10.00%` | 115,434.54 USD | `-0.11` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `15m` | `102.41` | `102.78` | `102.38` | `102.66` | `1,691` | 173,592.99 USD | 88,338.56 USD | `+50.89%` | 303,266.90 USD | `+0.61` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `102.62` | `102.99` | `102.57` | `102.91` | `1,097` | 112,895.56 USD | 74,468.67 USD | `+65.96%` | 377,735.57 USD | `+0.40` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `102.91` | `103.03` | `102.70` | `102.79` | `707` | 72,674.65 USD | -28,078.84 USD | `-38.64%` | 349,656.72 USD | `-0.61` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `1h` | `101.36` | `102.01` | `101.32` | `101.98` | `5,786` | 590,044.71 USD | 528,493.28 USD | `+89.57%` | -802,271.63 USD | `+1.93` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `1h` | `101.97` | `102.88` | `101.90` | `102.56` | `5,791` | 593,913.38 USD | 283,583.00 USD | `+47.75%` | -518,688.63 USD | `+1.05` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `1h` | `102.57` | `103.03` | `102.37` | `102.79` | `4,695` | 482,613.14 USD | 151,046.86 USD | `+31.30%` | -367,641.77 USD | `+0.55` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `4h` | `101.72` | `102.75` | `101.25` | `101.97` | `20,456` | 2,085,877.86 USD | 137,301.80 USD | `+6.58%` | -1,419,122.47 USD | `+1.16` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `101.97` | `102.01` | `100.46` | `101.98` | `32,502` | 3,314,488.96 USD | 1,586,995.19 USD | `+47.88%` | 167,872.72 USD | `+1.80` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `4h` | `101.97` | `103.64` | `101.90` | `103.54` | `17,042` | 1,764,579.81 USD | 1,581,740.16 USD | `+89.64%` | 1,749,612.88 USD | `+1.32` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `4h` | `102.59` | `102.87` | `101.92` | `101.96` | `11,805` | 1,203,637.80 USD | -961,636.55 USD | `-79.89%` | -1,027,007.90 USD | `-1.00` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `101.95` | `102.70` | `101.37` | `101.72` | `16,018` | 1,629,350.96 USD | -529,416.37 USD | `-32.49%` | -1,556,424.27 USD | `-0.03` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `101.72` | `102.75` | `101.25` | `101.97` | `20,456` | 2,085,877.86 USD | 137,301.80 USD | `+6.58%` | -1,419,122.47 USD | `+1.16` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `101.97` | `102.01` | `100.46` | `101.98` | `32,502` | 3,314,488.96 USD | 1,586,995.19 USD | `+47.88%` | 167,872.72 USD | `+1.80` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `4h` | `101.97` | `103.64` | `101.90` | `103.54` | `17,042` | 1,764,579.81 USD | 1,581,740.16 USD | `+89.64%` | 1,749,612.88 USD | `+1.32` | **`BULLISH`** | `AGGRESSIVE BUYING` |

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
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 03:25:41 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `41` | `0x0cc1...c7cb` | `LONG` | 30,863,850.47 USD | `300,817.26` | `98.89` | `102.61` | `31.91` | 1,114,349.43 USD | `+3.61%` | `3X Cross` |
| `113` | `0x30af...393e` | `LONG` | 18,226,187.54 USD | `177,712.44` | `100.98` | `102.61` | `93.20` | 280,785.65 USD | `+1.54%` | `10X Isolated` |
| `215` | `0x9e2c...5508` | `LONG` | 10,261,000.00 USD | `100,000.00` | `100.89` | `102.61` | `79.80` | 171,761.86 USD | `+1.67%` | `20X Cross` |
| `277` | `0xebe1...4070` | `LONG` | 8,618,396.10 USD | `83,999.96` | `101.87` | `102.61` | `0.000000` | 61,205.78 USD | `+0.71%` | `20X Cross` |
| `297` | `0x7fda...17d1` | `SHORT` | 8,070,028.08 USD | `78,647.58` | `100.15` | `102.61` | `203.73` | -193,406.23 USD | `-2.40%` | `20X Cross` |
| `334` | `0x10e1...f4bd` | `LONG` | 6,937,062.46 USD | `67,625.88` | `84.36` | `102.61` | `58.54` | 1,231,832.08 USD | `+17.76%` | `3X Isolated` |
| `346` | `0x4692...164f` | `SHORT` | 6,704,396.93 USD | `65,338.63` | `102.14` | `102.61` | `1039.95` | -30,740.38 USD | `-0.46%` | `5X Cross` |
| `403` | `0xea00...a918` | `SHORT` | 5,658,521.84 USD | `55,151.29` | `89.22` | `102.61` | `244.60` | -737,797.35 USD | `-13.04%` | `20X Cross` |
| `530` | `0x5989...bc29` | `SHORT` | 4,165,116.29 USD | `40,591.72` | `99.23` | `102.61` | `111.59` | -137,181.61 USD | `-3.29%` | `10X Cross` |
| `546` | `0xd507...c948` | `LONG` | 4,083,555.62 USD | `39,808.50` | `93.57` | `102.61` | `81.35` | 358,480.21 USD | `+8.78%` | `7X Isolated` |
| `607` | `0xd84a...c8a5` | `SHORT` | 3,762,386.09 USD | `36,666.86` | `101.90` | `102.61` | `121.27` | -25,963.33 USD | `-0.69%` | `20X Cross` |
| `693` | `0x354b...6425` | `SHORT` | 3,289,030.16 USD | `32,053.70` | `101.83` | `102.61` | `446.29` | -25,082.41 USD | `-0.76%` | `8X Cross` |
| `719` | `0xb5e7...eff1` | `SHORT` | 3,193,550.10 USD | `31,132.29` | `91.71` | `102.61` | `144.85` | -338,341.46 USD | `-10.59%` | `20X Cross` |
| `807` | `0x61d7...7dee` | `LONG` | 2,858,518.10 USD | `27,858.08` | `88.25` | `102.61` | `83.51` | 400,042.10 USD | `+13.99%` | `20X Cross` |
| `889` | `0xf0ae...2f74` | `SHORT` | 2,564,000.00 USD | `25,000.00` | `100.78` | `102.61` | `175.95` | -44,481.39 USD | `-1.73%` | `20X Cross` |
| `900` | `0xb8f3...04ea` | `SHORT` | 2,520,134.02 USD | `24,560.32` | `102.91` | `102.61` | `114.78` | 7,372.97 USD | `+0.29%` | `7X Isolated` |
| `914` | `0x645b...87b8` | `SHORT` | 2,493,714.82 USD | `24,302.84` | `101.22` | `102.61` | `134.77` | -33,753.26 USD | `-1.35%` | `3X Isolated` |
| `982` | `0x58f0...0d20` | `SHORT` | 2,309,909.74 USD | `22,511.55` | `96.77` | `102.61` | `114.43` | -131,491.95 USD | `-5.69%` | `20X Cross` |
| `1058` | `0xfc66...ca06` | `SHORT` | 2,109,756.09 USD | `20,566.93` | `101.34` | `102.61` | `1174.50` | -25,572.62 USD | `-1.21%` | `3X Cross` |
| `1070` | `0xce97...7e78` | `SHORT` | 2,085,221.23 USD | `20,321.81` | `102.72` | `102.61` | `120.33` | 2,216.76 USD | `+0.11%` | `5X Isolated` |
| `1106` | `0x9aa5...58af` | `SHORT` | 2,017,851.18 USD | `19,671.00` | `101.76` | `102.61` | `561.10` | -16,100.25 USD | `-0.80%` | `20X Cross` |
| `1212` | `0xe5dd...ecba` | `SHORT` | 1,865,311.33 USD | `18,183.97` | `102.71` | `102.61` | `138.75` | 2,355.38 USD | `+0.13%` | `20X Cross` |
| `1292` | `0x4169...6f06` | `LONG` | 1,761,487.49 USD | `17,175.19` | `76.61` | `102.61` | `82.99` | 445,719.49 USD | `+25.30%` | `12X Isolated` |
| `1302` | `0x6788...98d4` | `SHORT` | 1,744,200.00 USD | `17,000.00` | `99.31` | `102.61` | `197.66` | -55,875.41 USD | `-3.20%` | `20X Cross` |
| `1358` | `0xa99c...40d5` | `SHORT` | 1,651,860.00 USD | `16,100.00` | `101.02` | `102.61` | `154.95` | -25,402.63 USD | `-1.54%` | `20X Cross` |
| `1369` | `0x1bf6...5bfa` | `SHORT` | 1,641,760.00 USD | `16,000.00` | `99.60` | `102.61` | `225.97` | -48,137.69 USD | `-2.93%` | `20X Cross` |
| `1441` | `0x49e9...e1d0` | `SHORT` | 1,562,208.52 USD | `15,224.72` | `102.90` | `102.61` | `125.49` | 4,448.70 USD | `+0.28%` | `4X Isolated` |
| `1460` | `0x34ea...2f47` | `SHORT` | 1,539,000.00 USD | `15,000.00` | `99.80` | `102.61` | `199.87` | -41,998.69 USD | `-2.73%` | `20X Cross` |
| `1461` | `0x5d6f...6f8a` | `LONG` | 1,538,700.00 USD | `15,000.00` | `101.91` | `102.61` | `28.86` | 10,045.00 USD | `+0.65%` | `20X Cross` |
| `1578` | `0xfb29...21dd` | `LONG` | 1,410,188.88 USD | `13,744.53` | `89.85` | `102.61` | `84.64` | 175,194.92 USD | `+12.42%` | `20X Cross` |
| `1597` | `0x6fa6...825e` | `SHORT` | 1,385,235.00 USD | `13,500.00` | `102.95` | `102.61` | `135.51` | 4,539.27 USD | `+0.33%` | `20X Isolated` |
| `1609` | `0xa9d9...b48e` | `SHORT` | 1,368,133.30 USD | `13,333.33` | `96.39` | `102.61` | `174.37` | -82,886.11 USD | `-6.06%` | `20X Cross` |
| `1638` | `0xb078...de15` | `SHORT` | 1,333,930.00 USD | `13,000.00` | `102.96` | `102.61` | `531.87` | 4,579.53 USD | `+0.34%` | `5X Cross` |
| `1665` | `0x936c...bb0f` | `SHORT` | 1,301,906.24 USD | `12,687.91` | `101.39` | `102.61` | `163.65` | -15,433.37 USD | `-1.19%` | `2X Isolated` |
| `1698` | `0x89c2...c94b` | `LONG` | 1,268,617.30 USD | `12,364.69` | `75.25` | `102.61` | `45.77` | 338,134.14 USD | `+26.65%` | `3X Isolated` |
| `1727` | `0xcd81...36e3` | `SHORT` | 1,237,762.71 USD | `12,063.96` | `97.96` | `102.61` | `110.22` | -55,923.79 USD | `-4.52%` | `20X Cross` |
| `1731` | `0x436c...b3d1` | `SHORT` | 1,231,320.00 USD | `12,000.00` | `101.05` | `102.61` | `209.48` | -18,660.17 USD | `-1.52%` | `20X Cross` |
| `1794` | `0x9dea...d617` | `LONG` | 1,169,835.88 USD | `11,400.80` | `90.37` | `102.61` | `5.80` | 139,562.16 USD | `+11.93%` | `20X Cross` |
| `1797` | `0x91fd...9841` | `LONG` | 1,162,515.34 USD | `11,334.98` | `101.16` | `102.61` | `95.59` | 15,853.15 USD | `+1.36%` | `13X Isolated` |
| `1800` | `0x17c3...a868` | `LONG` | 1,160,169.92 USD | `11,306.60` | `95.13` | `102.61` | `65.00` | 84,523.05 USD | `+7.29%` | `3X Isolated` |
| `1825` | `0x7717...bd7e` | `SHORT` | 1,142,266.53 USD | `11,132.12` | `102.33` | `102.61` | `136.62` | -3,104.13 USD | `-0.27%` | `20X Cross` |
| `1839` | `0x8607...08d5` | `SHORT` | 1,128,515.25 USD | `10,998.10` | `92.18` | `102.61` | `135.03` | -114,725.54 USD | `-10.17%` | `4X Isolated` |
| `1921` | `0x7cee...fc93` | `SHORT` | 1,057,157.57 USD | `10,303.68` | `101.96` | `102.61` | `370.82` | -6,595.65 USD | `-0.62%` | `5X Cross` |
| `1949` | `0xf124...d738` | `LONG` | 1,039,135.40 USD | `10,130.00` | `102.56` | `102.61` | `95.39` | 243.12 USD | `+0.02%` | `20X Cross` |
| `1965` | `0xf29c...9971` | `SHORT` | 1,026,000.00 USD | `10,000.00` | `101.10` | `102.61` | `118.37` | -15,003.97 USD | `-1.46%` | `5X Isolated` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `102.32` | 625.79 USD | `-` | `NEWS_INTEL` | `-` | #XYZ:CL Liquidated Long: 0.63K USD at 102.3200 USD [API] | `2026-10-28 14:18:07` |
| `ANNOUNCEMENT` | `INFO` | `102.32` | 2,071.37 USD | `-` | `NEWS_INTEL` | `-` | #XYZ:CL Liquidated Long: 2.07K USD at 102.3200 USD [API] | `2026-10-28 14:18:07` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`103.89` (Vol: 2,900,000.00 USD, Dist: `+1.34%`) | Long MP=`99.17` (Vol: 6,700,000.00 USD, Dist: `--3.27%`)
  * 48H Horizon: Short MP=`104.00` (Vol: 7,100,000.00 USD, Dist: `+1.44%`) | Long MP=`99.18` (Vol: 4,000,000.00 USD, Dist: `--3.26%`)
  * 3D Horizon: Short MP=`104.04` (Vol: 7,000,000.00 USD, Dist: `+1.48%`) | Long MP=`99.25` (Vol: 9,800,000.00 USD, Dist: `--3.19%`)
  * 7D Horizon: Short MP=`103.98` (Vol: 11,000,000.00 USD, Dist: `+1.43%`) | Long MP=`99.25` (Vol: 12,300,000.00 USD, Dist: `--3.19%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Envelope` | `Long Liquidation` | `102.58` | 25,000,000.00 USD | 50,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 4 Macro Envelope` |
| `Envelope` | `Short Liquidation` | `104.37` | 25,000,000.00 USD | 50,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 4 Macro Envelope` |

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
  * Current Rate: `-295.82K` | Last 24h: `-77.94K` | Last 3d: `-389.33K` | Last 7d: `-828.50K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `-` | **USDT OKX** | `-` |
| **USDT Bybit** | `-` | **USDT KuCoin** | `-` |
| **USDT MEXC** | `-` | **USDT BingX** | `-` |
| **USDT Gate** | `-` | **USDT Bitget** | `-` |
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
| `21:20:00` | `102.59` | `102.59` | `102.59` | `102.70` | `102.52` | 50,886.13 USD | 16,608.67 USD | 34,277.46 USD | -17,668.79 USD | `-34.72%` | `0B / 1S` |
| `21:25:00` | `102.66` | `102.66` | `102.66` | `102.75` | `102.55` | 67,035.02 USD | 39,705.36 USD | 27,329.66 USD | 12,375.70 USD | `+18.46%` | `1B / 0S` |
| `21:30:00` | `102.91` | `102.91` | `102.91` | `102.99` | `102.57` | 112,895.56 USD | 93,682.11 USD | 19,213.45 USD | 74,468.67 USD | `+65.96%` | `1B / 0S` |
| `21:30:00` | `102.84` | `102.84` | `102.84` | `102.90` | `102.57` | 49,775.53 USD | 41,756.98 USD | 8,018.55 USD | 33,738.43 USD | `+67.78%` | `1B / 0S` |
| `21:35:00` | `102.77` | `102.77` | `102.77` | `102.90` | `102.71` | 31,447.01 USD | 9,179.13 USD | 22,267.88 USD | -13,088.75 USD | `-41.62%` | `0B / 1S` |
| `21:40:00` | `102.91` | `102.91` | `102.91` | `102.99` | `102.77` | 31,594.29 USD | 22,993.62 USD | 8,600.67 USD | 14,392.95 USD | `+45.56%` | `1B / 0S` |
| `21:45:00` | `102.88` | `102.88` | `102.88` | `103.03` | `102.87` | 25,719.50 USD | 5,600.21 USD | 20,119.29 USD | -14,519.07 USD | `-56.45%` | `0B / 1S` |
| `21:45:00` | `102.79` | `102.79` | `102.79` | `103.03` | `102.70` | 72,674.65 USD | 22,297.90 USD | 50,376.75 USD | -28,078.84 USD | `-38.64%` | `0B / 1S` |
| `21:50:00` | `102.80` | `102.80` | `102.80` | `102.92` | `102.79` | 25,802.30 USD | 3,822.56 USD | 21,979.74 USD | -18,157.17 USD | `-70.37%` | `0B / 1S` |
| `21:55:00` | `102.79` | `102.79` | `102.79` | `102.85` | `102.70` | 21,175.36 USD | 11,646.45 USD | 9,528.91 USD | 2,117.54 USD | `+10.00%` | `1B / 0S` |
| `5:00 UTC` | `102.81` | `102.73` | `102.81` | `102.97` | `102.35` | 32,224,554.20 USD | 17,495,336.21 USD | 14,729,217.99 USD | 2,766,118.21 USD | `+8.58%` | `13B / 7S` |
| `0:00 UTC` | `103.00` | `102.95` | `103.00` | `103.06` | `102.81` | 19,638,941.63 USD | 9,830,854.95 USD | 9,808,086.67 USD | 22,768.28 USD | `+0.12%` | `2B / 4S` |
| `5:00 UTC` | `103.02` | `102.95` | `103.02` | `103.06` | `102.82` | 8,073,511.20 USD | 2,057,722.32 USD | 6,015,788.89 USD | -3,958,066.57 USD | `-49.03%` | `1B / 13S` |
| `0:00 UTC` | `102.87` | `102.93` | `102.87` | `103.02` | `102.84` | 8,092,099.96 USD | 4,143,913.94 USD | 3,948,186.02 USD | 195,727.93 USD | `+2.42%` | `2B / 2S` |
| `5:00 UTC` | `102.81` | `102.87` | `102.81` | `103.02` | `102.78` | 25,235,874.42 USD | 17,074,162.87 USD | 8,161,711.55 USD | 8,912,451.33 USD | `+35.32%` | `6B / 1S` |
| `0:00 UTC` | `102.00` | `102.25` | `102.00` | `102.98` | `101.69` | 44,005,448.45 USD | 22,985,881.99 USD | 21,019,566.46 USD | 1,966,315.53 USD | `+4.47%` | `19B / 33S` |
| `5:00 UTC` | `101.85` | `102.09` | `101.85` | `102.65` | `101.69` | 23,974,978.54 USD | 13,713,172.54 USD | 10,261,806.01 USD | 3,451,366.53 USD | `+14.40%` | `18B / 9S` |
| `0:00 UTC` | `102.47` | `102.50` | `102.47` | `102.60` | `102.41` | 5,469,868.87 USD | 2,184,741.26 USD | 3,285,127.61 USD | -1,100,386.35 USD | `-20.12%` | `0B / 3S` |
| `5:00 UTC` | `102.62` | `102.58` | `102.62` | `102.66` | `102.50` | 2,045,755.51 USD | 1,077,529.04 USD | 968,226.47 USD | 109,302.57 USD | `+5.34%` | `4B / 1S` |
| `0:00 UTC` | `102.88` | `102.81` | `102.88` | `102.90` | `102.62` | 8,845,234.18 USD | 6,144,781.76 USD | 2,700,452.42 USD | 3,444,329.34 USD | `+38.94%` | `10B / 0S` |

- **CoinGlass Algorithmic Footprint Signals Table (25_CoinGlass_Footprint_Signals.parquet)**:
| Time | Timeframe | Signal Type | Bias | Headline | Price Level | Absorbed Vol (USD) | Bar Delta (USD) |
|:---:|:---:|:---:|:---:|:---|:---:|:---:|:---:|
| `2026-10-28 17:30:00 IST` | `4h` | `AGGRESSIVE BUYING` | **`BULLISH`** | WTI_OIL Macro Delta Flow: AGGRESSIVE BUY | `102.68` | 803,986.89 USD | 803,986.89 USD |
| `10-28 18:20` | `Volume 200K CL` | `Absorption` | **`BEARISH`** | Buying absorbed at the high | `102.21` | 51,000.00 USD | 0.00 USD |
| `10-28 11:54` | `Volume 200K CL` | `Divergence` | **`BEARISH`** | Rally without taker buying | `101.96` | 0.00 USD | 0.00 USD |
| `10-28 07:12` | `Volume 200K CL` | `Divergence` | **`BEARISH`** | Rally without taker buying | `101.50` | 0.00 USD | 0.00 USD |

- **12-Horizon Macro Capital Netflows Table (2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet)**:
| Horizon | Spot Netflow (USD) | Futures Netflow (USD) | Institutional Bias |
|:---:|:---:|:---:|:---:|
| `5m` | 0.00 USD | 0.00 USD | **`NEUTRAL`** |
| `15m` | 0.00 USD | 0.00 USD | **`NEUTRAL`** |
| `30m` | 0.00 USD | 0.00 USD | **`NEUTRAL`** |
| `1h` | 0.00 USD | 0.00 USD | **`NEUTRAL`** |
| `2h` | 0.00 USD | 0.00 USD | **`NEUTRAL`** |
| `4h` | 0.00 USD | 0.00 USD | **`NEUTRAL`** |
| `6h` | 0.00 USD | 0.00 USD | **`NEUTRAL`** |
| `8h` | 0.00 USD | 0.00 USD | **`NEUTRAL`** |
| `12h` | 0.00 USD | 0.00 USD | **`NEUTRAL`** |
| `24h` | 0.00 USD | 0.00 USD | **`NEUTRAL`** |
| `1w` | 0.00 USD | 0.00 USD | **`NEUTRAL`** |
| `30d` | 0.00 USD | 0.00 USD | **`NEUTRAL`** |

* Spot Capital Netflows: 5m=`-` | 15m=`-` | 1h=`-` | 24h=`-`
* Futures Capital Netflows: 5m=`-` | 15m=`-` | 1h=`-` | 24h=`-`
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
  * Execution Entry: `101.40` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `100.93` (Risk Distance: `0.4731` pts)
  * +2.5R Take Profit: `102.58`
  * Mathematical Lot Sizing: **`0.10 lots`** (Nominal Risk = `0.47 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `102.76` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `103.23` (Risk Distance: `0.4731` pts)
  * +2.5R Take Profit: `101.58`
  * Mathematical Lot Sizing: **`0.10 lots`** (Nominal Risk = `0.47 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`PASSIVE_MAKER_LIMIT_ARMED`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`104.39`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
