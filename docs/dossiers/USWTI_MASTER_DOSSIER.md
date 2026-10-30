# 🏛️ SOVEREIGN CANDIDATE DOSSIER: USWTI
**Canonical Key**: `USWTI` | **Broker Instrument**: `USWTI.p` | **Asset Class**: `Energy Commodity`
**Timestamp**: `2026-10-30 11:29:21 IST` (`2026-10-30 05:59:21 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `103.99` | **Live Ask Quote**: `104.04` | **Mid Price**: `104.01`
- **Spread Points**: `46.00` | **Spread BPS**: `4.42 bps` (Charter Threshold: `5.00 bps`)
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
  * Session VWAP: `104.14` | VWAP Z-Score: `-0.33` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `0.3058` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `55.72` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `106.02` | Lower -3.00σ Band: `102.26`
  * Upper +2.51σ Band: `105.71` | Lower -2.51σ Band: `102.57`
  * Upper +2.01σ Band: `105.40` | Lower -2.01σ Band: `102.88`
  * Upper +2.00σ Band: `105.39` | Lower -2.00σ Band: `102.89`
  * Upper +1.28σ Band: `104.94` | Lower -1.28σ Band: `103.34`
  * Upper +1.00σ Band: `104.76` | Lower -1.00σ Band: `103.51`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`103.78` | EMA-20=`103.77` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`103.38` (Slope: `+0.0000`) | EMA-100=`102.98`
  * Institutional Anchors: EMA-144=`102.77` | EMA-200=`102.55` (Slope: `+0.1556`) | EMA-233=`102.49`
- **Range Boundaries**: 24H High=`105.59` | 24H Low=`100.46` | Weekly High=`105.59` | Weekly Low=`100.17`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `104.36` (Distance: `-0.30%`)
  * Point of Control (POC) = `103.38` (Distance: `+0.65%`)
  * Value Area Low (VAL) = `103.07` (Distance: `+0.94%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BULLISH (Above Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`102.76` | POC=`102.02` | VAL=`101.40`
  * Prior Day Extremes: PDH=`103.64` | PDL=`100.46` | PDC=`103.54`
  * Monday Range Blueprint: High=`103.88` | Mid=`102.48` | Low=`101.08`
  * Developing Weekly Value Area: Weekly VAH=`103.22` | Weekly POC=`102.03` | Weekly VAL=`101.42`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`105.59` | Low=`103.05`
  * London Session (08:00-16:00 UTC): High=`104.12` | Low=`103.51`
  * New York Session (13:00-21:00 UTC): High=`104.64` | Low=`103.39`
  * Initial Balance (First Hour): IB High=`104.12` | IB Low=`103.51`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `103.60` - `104.43`
  * Optimal Trade Entry (OTE 0.705): `104.22`
  * Structural Invalidation Anchor (0.786): `104.85`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `104.27` | `104.37` | `104.07` | `104.19` | `659` | 68,658.57 USD | -16,423.31 USD | `-23.92%` | 344,559.60 USD | `-0.71` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `5m` | `104.19` | `104.19` | `104.01` | `104.08` | `506` | 52,663.47 USD | -22,714.74 USD | `-43.13%` | 321,844.86 USD | `-0.87` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `5m` | `104.09` | `104.19` | `104.06` | `104.13` | `339` | 35,299.73 USD | 6,275.51 USD | `+17.78%` | 328,120.37 USD | `+0.01` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `104.92` | `105.25` | `104.75` | `104.77` | `1,722` | 180,408.77 USD | -111,535.28 USD | `-61.82%` | 827,877.53 USD | `-1.77` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `104.76` | `104.86` | `104.28` | `104.28` | `734` | 76,540.79 USD | -68,886.71 USD | `-90.00%` | 758,990.82 USD | `-1.03` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `104.27` | `104.37` | `104.01` | `104.13` | `1,504` | 156,610.02 USD | -56,432.10 USD | `-36.03%` | 702,558.72 USD | `-0.82` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `1h` | `103.46` | `103.53` | `103.06` | `103.07` | `1,416` | 145,947.12 USD | -131,352.41 USD | `-90.00%` | 670,573.75 USD | `-0.60` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `1h` | `103.06` | `105.59` | `103.05` | `104.94` | `7,807` | 819,305.61 USD | 505,426.25 USD | `+61.69%` | 1,176,000.01 USD | `+1.48` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `1h` | `104.92` | `105.25` | `103.91` | `103.99` | `4,862` | 505,599.38 USD | -397,014.28 USD | `-78.52%` | 778,985.73 USD | `-1.39` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `101.97` | `103.64` | `101.90` | `103.54` | `17,042` | 1,764,579.81 USD | 1,581,740.16 USD | `+89.64%` | 2,776,620.79 USD | `+0.96` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `4h` | `103.47` | `103.54` | `103.06` | `103.07` | `2,890` | 297,872.30 USD | -268,085.07 USD | `-90.00%` | 2,508,535.72 USD | `-0.85` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `103.06` | `105.59` | `103.05` | `103.55` | `15,766` | 1,632,600.83 USD | -333,255.85 USD | `-20.41%` | 2,175,279.87 USD | `-0.79` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `101.72` | `102.75` | `101.25` | `101.97` | `20,456` | 2,085,877.86 USD | 137,301.80 USD | `+6.58%` | -392,114.57 USD | `+1.00` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `101.97` | `102.01` | `100.46` | `101.98` | `32,502` | 3,314,488.96 USD | 1,586,995.19 USD | `+47.88%` | 1,194,880.62 USD | `+1.35` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `4h` | `101.97` | `103.64` | `101.90` | `103.54` | `17,042` | 1,764,579.81 USD | 1,581,740.16 USD | `+89.64%` | 2,776,620.79 USD | `+0.96` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `4h` | `103.47` | `103.54` | `103.06` | `103.07` | `2,890` | 297,872.30 USD | -268,085.07 USD | `-90.00%` | 2,508,535.72 USD | `-0.85` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `103.06` | `105.59` | `103.05` | `103.55` | `15,766` | 1,632,600.83 USD | -333,255.85 USD | `-20.41%` | 2,175,279.87 USD | `-0.79` | **`BEARISH`** | `BEARISH ABSORPTION` |

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
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 11:24:14 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `40` | `0x0cc1...c7cb` | `LONG` | 31,098,487.93 USD | `300,817.26` | `98.89` | `103.38` | `31.36` | 1,348,986.89 USD | `+4.34%` | `3X Cross` |
| `114` | `0x30af...393e` | `LONG` | 18,370,134.61 USD | `177,712.44` | `100.98` | `103.38` | `93.19` | 424,732.72 USD | `+2.31%` | `10X Isolated` |
| `287` | `0x7fda...17d1` | `SHORT` | 8,130,586.72 USD | `78,647.58` | `100.15` | `103.38` | `211.12` | -253,964.87 USD | `-3.12%` | `20X Cross` |
| `327` | `0x10e1...f4bd` | `LONG` | 6,991,163.16 USD | `67,625.88` | `84.36` | `103.38` | `58.53` | 1,285,932.78 USD | `+18.39%` | `3X Isolated` |
| `395` | `0xea00...a918` | `SHORT` | 5,701,539.84 USD | `55,151.29` | `89.22` | `103.38` | `240.07` | -780,815.35 USD | `-13.69%` | `20X Cross` |
| `414` | `0x354b...6425` | `SHORT` | 5,386,769.66 USD | `52,106.50` | `102.88` | `103.38` | `308.63` | -26,217.39 USD | `-0.49%` | `8X Cross` |
| `481` | `0x4692...164f` | `SHORT` | 4,631,829.20 USD | `44,799.59` | `103.49` | `103.38` | `1506.95` | 4,395.36 USD | `+0.09%` | `5X Cross` |
| `489` | `0x5989...bc29` | `SHORT` | 4,516,849.91 USD | `43,691.72` | `99.48` | `103.38` | `113.23` | -170,543.01 USD | `-3.78%` | `10X Cross` |
| `536` | `0xd84a...c8a5` | `SHORT` | 4,134,800.00 USD | `40,000.00` | `101.97` | `103.38` | `119.11` | -56,170.00 USD | `-1.36%` | `20X Cross` |
| `544` | `0xd507...c948` | `LONG` | 4,115,402.42 USD | `39,808.50` | `93.57` | `103.38` | `82.63` | 390,327.01 USD | `+9.48%` | `7X Isolated` |
| `700` | `0xb5e7...eff1` | `SHORT` | 3,218,144.61 USD | `31,132.29` | `91.71` | `103.38` | `144.94` | -362,935.97 USD | `-11.28%` | `20X Cross` |
| `738` | `0xbd33...4200` | `SHORT` | 3,099,311.18 USD | `29,982.69` | `104.89` | `103.38` | `403.27` | 45,573.70 USD | `+1.47%` | `20X Cross` |
| `786` | `0xebe1...4070` | `LONG` | 2,894,637.21 USD | `27,999.97` | `101.87` | `103.38` | `0.000000` | 42,241.89 USD | `+1.46%` | `20X Cross` |
| `791` | `0x61d7...7dee` | `LONG` | 2,879,968.83 USD | `27,858.08` | `88.25` | `103.38` | `83.50` | 421,492.83 USD | `+14.64%` | `20X Cross` |
| `871` | `0xf0ae...2f74` | `SHORT` | 2,584,250.00 USD | `25,000.00` | `100.78` | `103.38` | `176.66` | -64,731.39 USD | `-2.50%` | `20X Cross` |
| `885` | `0x645b...87b8` | `SHORT` | 2,542,793.61 USD | `24,596.57` | `101.24` | `103.38` | `134.75` | -52,556.25 USD | `-2.07%` | `3X Isolated` |
| `983` | `0x40f2...6a9e` | `LONG` | 2,246,795.58 USD | `21,733.37` | `103.34` | `103.38` | `100.58` | 785.63 USD | `+0.03%` | `20X Cross` |
| `1073` | `0x9aa5...58af` | `SHORT` | 2,033,587.98 USD | `19,671.00` | `101.76` | `103.38` | `568.24` | -31,837.05 USD | `-1.57%` | `20X Cross` |
| `1247` | `0x4169...6f06` | `LONG` | 1,775,399.39 USD | `17,175.19` | `76.61` | `103.38` | `82.98` | 459,631.39 USD | `+25.89%` | `12X Isolated` |
| `1260` | `0x6788...98d4` | `SHORT` | 1,757,460.00 USD | `17,000.00` | `99.31` | `103.38` | `197.84` | -69,135.41 USD | `-3.93%` | `20X Cross` |
| `1305` | `0xa99c...40d5` | `SHORT` | 1,664,418.00 USD | `16,100.00` | `101.02` | `103.38` | `153.25` | -37,960.63 USD | `-2.28%` | `20X Cross` |
| `1312` | `0x1bf6...5bfa` | `SHORT` | 1,654,240.00 USD | `16,000.00` | `99.60` | `103.38` | `229.19` | -60,617.69 USD | `-3.66%` | `20X Cross` |
| `1386` | `0xe5dd...ecba` | `SHORT` | 1,568,962.47 USD | `15,178.12` | `102.71` | `103.38` | `146.05` | -10,024.68 USD | `-0.64%` | `20X Cross` |
| `1399` | `0x34ea...2f47` | `SHORT` | 1,550,700.00 USD | `15,000.00` | `99.80` | `103.38` | `197.98` | -53,698.69 USD | `-3.46%` | `20X Cross` |
| `1400` | `0x5d6f...6f8a` | `LONG` | 1,550,550.00 USD | `15,000.00` | `101.91` | `103.38` | `27.02` | 21,895.00 USD | `+1.41%` | `20X Cross` |
| `1444` | `0xfc27...9d9d` | `LONG` | 1,504,590.87 USD | `14,555.39` | `102.69` | `103.38` | `0.000000` | 9,931.90 USD | `+0.66%` | `20X Cross` |
| `1511` | `0xfb29...21dd` | `LONG` | 1,421,047.06 USD | `13,744.53` | `89.85` | `103.38` | `84.65` | 186,053.10 USD | `+13.09%` | `20X Cross` |
| `1535` | `0x6fa6...825e` | `SHORT` | 1,395,765.00 USD | `13,500.00` | `102.95` | `103.38` | `135.50` | -5,990.73 USD | `-0.43%` | `20X Isolated` |
| `1560` | `0xa9d9...b48e` | `SHORT` | 1,378,266.63 USD | `13,333.33` | `96.39` | `103.38` | `173.96` | -93,019.45 USD | `-6.75%` | `20X Cross` |
| `1610` | `0x936c...bb0f` | `SHORT` | 1,311,675.93 USD | `12,687.91` | `101.39` | `103.38` | `163.64` | -25,203.06 USD | `-1.92%` | `2X Isolated` |
| `1648` | `0x89c2...c94b` | `LONG` | 1,278,261.76 USD | `12,364.69` | `75.25` | `103.38` | `45.76` | 347,778.60 USD | `+27.21%` | `3X Isolated` |
| `1685` | `0xcd81...36e3` | `SHORT` | 1,246,810.68 USD | `12,063.96` | `97.96` | `103.38` | `109.06` | -64,971.76 USD | `-5.21%` | `20X Cross` |
| `1691` | `0x436c...b3d1` | `SHORT` | 1,240,560.00 USD | `12,000.00` | `101.05` | `103.38` | `207.78` | -27,900.17 USD | `-2.25%` | `20X Cross` |
| `1748` | `0x9dea...d617` | `LONG` | 1,178,728.51 USD | `11,400.80` | `90.37` | `103.38` | `8.16` | 148,454.78 USD | `+12.59%` | `20X Cross` |
| `1772` | `0x17c3...a868` | `LONG` | 1,168,876.00 USD | `11,306.60` | `95.13` | `103.38` | `64.99` | 93,229.13 USD | `+7.98%` | `3X Isolated` |
| `1816` | `0x8607...08d5` | `SHORT` | 1,136,983.78 USD | `10,998.10` | `92.18` | `103.38` | `135.02` | -123,194.08 USD | `-10.84%` | `4X Isolated` |
| `2000` | `0xce97...7e78` | `SHORT` | 1,008,430.89 USD | `9,755.55` | `103.23` | `103.38` | `120.87` | -1,317.08 USD | `-0.13%` | `5X Isolated` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `94.91` | 1,011.58 USD | `-` | `NEWS_INTEL` | `-` | #XYZ:CL Liquidated Long: 1.01K USD at 94.9130 USD [API] | `2026-09-17 12:09:11` |
| `ANNOUNCEMENT` | `INFO` | `94.91` | 1,931.10 USD | `-` | `NEWS_INTEL` | `-` | #XYZ:CL Liquidated Long: 1.93K USD at 94.9130 USD [API] | `2026-09-17 12:09:11` |
| `ANNOUNCEMENT` | `INFO` | `94.91` | 2,292.43 USD | `-` | `NEWS_INTEL` | `-` | #XYZ:CL Liquidated Long: 2.29K USD at 94.9130 USD [API] | `2026-09-17 12:09:11` |
| `ANNOUNCEMENT` | `INFO` | `94.91` | 3,821.71 USD | `-` | `NEWS_INTEL` | `-` | #XYZ:CL Liquidated Long: 3.82K USD at 94.9140 USD [API] | `2026-09-17 12:09:11` |
| `ANNOUNCEMENT` | `INFO` | `94.91` | 2,292.36 USD | `-` | `NEWS_INTEL` | `-` | #XYZ:CL Liquidated Long: 2.29K USD at 94.9140 USD [API] | `2026-09-17 12:09:11` |
| `ANNOUNCEMENT` | `INFO` | `94.91` | 1,931.88 USD | `-` | `NEWS_INTEL` | `-` | #XYZ:CL Liquidated Long: 1.93K USD at 94.9140 USD [API] | `2026-09-17 12:09:11` |
| `ANNOUNCEMENT` | `INFO` | `94.91` | 2,292.84 USD | `-` | `NEWS_INTEL` | `-` | #XYZ:CL Liquidated Long: 2.29K USD at 94.9140 USD [API] | `2026-09-17 12:09:11` |
| `ANNOUNCEMENT` | `INFO` | `94.91` | 1,108.41 USD | `-` | `NEWS_INTEL` | `-` | #XYZ:CL Liquidated Long: 1.11K USD at 94.9140 USD [API] | `2026-09-17 12:09:11` |
| `ANNOUNCEMENT` | `INFO` | `84.31` | 5,111.99 USD | `-` | `NEWS_INTEL` | `-` | #XYZ:CL Liquidated Long: 5.11K USD at 84.3090 USD [API] | `2026-03-11 13:24:34` |
| `ANNOUNCEMENT` | `INFO` | `83.80` | 5,851.98 USD | `-` | `NEWS_INTEL` | `-` | #XYZ:CL Liquidated Long: 5.85K USD at 83.7960 USD [API] | `2026-03-10 14:40:53` |
| `ANNOUNCEMENT` | `INFO` | `86.06` | 13,470.35 USD | `-` | `NEWS_INTEL` | `-` | #XYZ:CL Liquidated Long: 13.47K USD at 86.0610 USD [API] | `2026-03-10 07:23:35` |
| `ANNOUNCEMENT` | `INFO` | `91.74` | 26,993.03 USD | `-` | `NEWS_INTEL` | `-` | #XYZ:CL Liquidated Long: 26.99K USD at 91.7400 USD [API] | `2026-03-09 19:19:31` |
| `ANNOUNCEMENT` | `INFO` | `91.77` | 40,765.73 USD | `-` | `NEWS_INTEL` | `-` | #XYZ:CL Liquidated Long: 40.77K USD at 91.7680 USD [API] | `2026-03-09 19:19:31` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`105.84` (Vol: 3,800,000.00 USD, Dist: `+2.45%`) | Long MP=`99.16` (Vol: 6,700,000.00 USD, Dist: `--4.01%`)
  * 48H Horizon: Short MP=`105.84` (Vol: 2,400,000.00 USD, Dist: `+2.45%`) | Long MP=`99.16` (Vol: 4,000,000.00 USD, Dist: `--4.01%`)
  * 3D Horizon: Short MP=`105.86` (Vol: 2,700,000.00 USD, Dist: `+2.47%`) | Long MP=`99.12` (Vol: 9,700,000.00 USD, Dist: `--4.05%`)
  * 7D Horizon: Short MP=`105.58` (Vol: 4,200,000.00 USD, Dist: `+2.21%`) | Long MP=`99.12` (Vol: 8,700,000.00 USD, Dist: `--4.05%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Envelope` | `Long Liquidation` | `102.87` | 25,000,000.00 USD | 50,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 4 Macro Envelope` |
| `Envelope` | `Short Liquidation` | `104.33` | 25,000,000.00 USD | 50,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 4 Macro Envelope` |

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
  * Current Rate: `-183.63K` | Last 24h: `-501.60K` | Last 3d: `-815.84K` | Last 7d: `-1.22M`
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
| `05:05:00` | `104.96` | `104.96` | `104.96` | `105.18` | `104.86` | 60,772.42 USD | 17,985.61 USD | 42,786.81 USD | -24,801.21 USD | `-40.81%` | `0B / 1S` |
| `05:10:00` | `104.77` | `104.77` | `104.77` | `105.06` | `104.75` | 49,240.49 USD | 7,268.83 USD | 41,971.66 USD | -34,702.82 USD | `-70.48%` | `0B / 1S` |
| `05:15:00` | `104.28` | `104.28` | `104.28` | `104.86` | `104.28` | 76,540.79 USD | 3,827.04 USD | 72,713.75 USD | -68,886.71 USD | `-90.00%` | `0B / 1S` |
| `05:15:00` | `104.69` | `104.69` | `104.69` | `104.86` | `104.66` | 23,870.46 USD | 6,496.76 USD | 17,373.70 USD | -10,876.93 USD | `-45.57%` | `0B / 1S` |
| `05:20:00` | `104.54` | `104.54` | `104.54` | `104.71` | `104.53` | 16,935.48 USD | 940.86 USD | 15,994.62 USD | -15,053.76 USD | `-88.89%` | `0B / 1S` |
| `05:25:00` | `104.28` | `104.28` | `104.28` | `104.53` | `104.28` | 35,871.98 USD | 1,793.60 USD | 34,078.38 USD | -32,284.78 USD | `-90.00%` | `0B / 1S` |
| `05:30:00` | `104.19` | `104.19` | `104.19` | `104.37` | `104.07` | 68,658.57 USD | 26,117.63 USD | 42,540.94 USD | -16,423.31 USD | `-23.92%` | `0B / 1S` |
| `05:30:00` | `104.13` | `104.13` | `104.13` | `104.37` | `104.01` | 156,610.02 USD | 50,088.96 USD | 106,521.06 USD | -56,432.10 USD | `-36.03%` | `0B / 1S` |
| `05:35:00` | `104.08` | `104.08` | `104.08` | `104.19` | `104.01` | 52,663.47 USD | 14,974.37 USD | 37,689.10 USD | -22,714.74 USD | `-43.13%` | `0B / 1S` |
| `05:40:00` | `104.13` | `104.13` | `104.13` | `104.19` | `104.06` | 35,299.73 USD | 20,787.62 USD | 14,512.11 USD | 6,275.51 USD | `+17.78%` | `1B / 0S` |
| `0:00 UTC` | `103.50` | `103.53` | `103.50` | `103.66` | `103.41` | 4,898,115.03 USD | 2,100,565.02 USD | 2,797,550.01 USD | -696,984.99 USD | `-14.23%` | `4B / 8S` |
| `5:00 UTC` | `103.32` | `103.37` | `103.32` | `103.50` | `103.30` | 5,800,580.27 USD | 3,315,920.42 USD | 2,484,659.85 USD | 831,260.57 USD | `+14.33%` | `4B / 1S` |
| `0:00 UTC` | `103.38` | `103.38` | `103.38` | `103.44` | `103.31` | 5,199,824.51 USD | 3,341,152.42 USD | 1,858,672.10 USD | 1,482,480.32 USD | `+28.51%` | `3B / 2S` |
| `5:00 UTC` | `103.31` | `103.30` | `103.31` | `103.34` | `103.23` | 3,756,770.69 USD | 2,127,360.29 USD | 1,629,410.40 USD | 497,949.89 USD | `+13.25%` | `2B / 1S` |
| `0:00 UTC` | `103.25` | `103.28` | `103.25` | `103.37` | `103.23` | 2,263,324.74 USD | 1,120,957.51 USD | 1,142,367.23 USD | -21,409.73 USD | `-0.95%` | `3B / 0S` |
| `5:00 UTC` | `103.00` | `103.14` | `103.00` | `103.50` | `102.94` | 9,234,794.82 USD | 4,542,925.91 USD | 4,691,868.91 USD | -148,943.00 USD | `-1.61%` | `4B / 6S` |
| `0:00 UTC` | `103.09` | `103.10` | `103.09` | `103.19` | `103.05` | 2,687,690.44 USD | 1,506,949.94 USD | 1,180,740.51 USD | 326,209.43 USD | `+12.14%` | `2B / 0S` |
| `5:00 UTC` | `103.10` | `103.11` | `103.10` | `103.19` | `103.06` | 3,024,324.91 USD | 1,670,672.44 USD | 1,353,652.47 USD | 317,019.96 USD | `+10.48%` | `1B / 0S` |
| `0:00 UTC` | `103.31` | `103.29` | `103.31` | `103.48` | `103.03` | 6,474,098.12 USD | 3,535,065.19 USD | 2,939,032.93 USD | 596,032.26 USD | `+9.21%` | `13B / 4S` |
| `5:00 UTC` | `103.52` | `103.49` | `103.52` | `103.60` | `103.40` | 2,735,621.58 USD | 1,373,352.30 USD | 1,362,269.28 USD | 11,083.02 USD | `+0.41%` | `6B / 2S` |

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
  * `2026-10-30 11:03:23 IST`: [kitco.com] - (Sentiment: `Neutral`)
  * `2026-10-30 11:19:23 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 11:18:23 IST`: [forex.com] - (Sentiment: `Neutral`)
  * `2026-10-30 11:18:23 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 11:18:23 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 08:20:23 IST`: [financemagnates.com] - (Sentiment: `Neutral`)
  * `2026-10-30 07:20:23 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-30 07:20:23 IST`: [kathleenhays.substack.com] - (Sentiment: `Neutral`)
  * `2026-10-30 06:20:23 IST`: [rba.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 06:20:23 IST`: [abs.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 06:20:23 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 06:20:23 IST`: [@NodeWire] - (Sentiment: `Neutral`)
  * `2026-10-30 06:20:23 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 06:20:23 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 05:20:23 IST`: [@financialjuice] - (Sentiment: `Neutral`)


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
  * Execution Entry: `103.07` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `102.63` (Risk Distance: `0.4360` pts)
  * +2.5R Take Profit: `104.16`
  * Mathematical Lot Sizing: **`0.10 lots`** (Nominal Risk = `0.44 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `104.36` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `104.80` (Risk Distance: `0.4360` pts)
  * +2.5R Take Profit: `103.27`
  * Mathematical Lot Sizing: **`0.10 lots`** (Nominal Risk = `0.44 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`PASSIVE_MAKER_LIMIT_ARMED`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`104.85`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
