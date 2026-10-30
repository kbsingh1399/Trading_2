# 🏛️ SOVEREIGN CANDIDATE DOSSIER: NEAR
**Canonical Key**: `NEAR` | **Broker Instrument**: `NERUSD.p` | **Asset Class**: `Crypto Alt L1`
**Timestamp**: `2026-10-30 07:51:26 IST` (`2026-10-30 02:21:26 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `4.00` | **Live Ask Quote**: `4.03` | **Mid Price**: `4.01`
- **Spread Points**: `30.00` | **Spread BPS**: `74.76 bps` (Charter Threshold: `25.00 bps`)
- **Gate 1 Clearance**: **`SPREAD_DISQUALIFIED`** | **Execution Posture**: `DISQUALIFIED` | **Order Type Allowed**: `NONE`
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
  * Session VWAP: `3.98` | VWAP Z-Score: `+0.13` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `0.0633` (Volatility Regime: `HIGH_EXPANSION`)
  * 14-Period RSI: `30.24` (State: `OVERSOLD`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `4.07` | Lower -3.00σ Band: `3.89`
  * Upper +2.51σ Band: `4.06` | Lower -2.51σ Band: `3.90`
  * Upper +2.01σ Band: `4.04` | Lower -2.01σ Band: `3.92`
  * Upper +2.00σ Band: `4.04` | Lower -2.00σ Band: `3.92`
  * Upper +1.28σ Band: `4.02` | Lower -1.28σ Band: `3.94`
  * Upper +1.00σ Band: `4.01` | Lower -1.00σ Band: `3.95`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`4.01` | EMA-20=`4.08` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`4.22` (Slope: `+0.0000`) | EMA-100=`4.33`
  * Institutional Anchors: EMA-144=`4.38` | EMA-200=`4.42` (Slope: `-1.1612`) | EMA-233=`4.45`
- **Range Boundaries**: 24H High=`4.67` | 24H Low=`3.89` | Weekly High=`4.80` | Weekly Low=`3.89`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `4.12` (Distance: `-2.60%`)
  * Point of Control (POC) = `4.09` (Distance: `-1.95%`)
  * Value Area Low (VAL) = `3.94` (Distance: `+1.91%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`4.57` | POC=`4.41` | VAL=`4.29`
  * Prior Day Extremes: PDH=`4.75` | PDL=`4.08` | PDC=`4.15`
  * Monday Range Blueprint: High=`4.65` | Mid=`4.53` | Low=`4.41`
  * Developing Weekly Value Area: Weekly VAH=`4.67` | Weekly POC=`4.45` | Weekly VAL=`4.39`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`4.26` | Low=`3.89`
  * London Session (08:00-16:00 UTC): High=`4.03` | Low=`4.00`
  * New York Session (13:00-21:00 UTC): High=`4.04` | Low=`3.99`
  * Initial Balance (First Hour): IB High=`4.03` | IB Low=`4.00`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `4.00` - `4.03`
  * Optimal Trade Entry (OTE 0.705): `4.02`
  * Structural Invalidation Anchor (0.786): `4.05`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `4.00` | `4.01` | `3.97` | `3.97` | `461,343` | 1,840,662.40 USD | -286,797.19 USD | `-15.58%` | -36,040,127.27 USD | `-0.04` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `5m` | `3.97` | `4.01` | `3.97` | `4.00` | `442,947` | 1,767,945.92 USD | 425,455.00 USD | `+24.06%` | -35,614,672.27 USD | `+0.92` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `5m` | `4.00` | `4.02` | `4.00` | `4.02` | `423,122` | 1,698,142.33 USD | 190,466.17 USD | `+11.22%` | -35,424,206.10 USD | `+0.40` | **`BULLISH`** | `DELTA ALIGNED` |
| `15m` | `3.99` | `4.03` | `3.95` | `4.01` | `2,752,687` | 11,016,623.88 USD | -5,606.55 USD | `-0.05%` | -34,699,252.99 USD | `+0.35` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `15m` | `4.01` | `4.01` | `3.97` | `4.00` | `1,599,337` | 6,380,993.73 USD | -1,054,077.10 USD | `-16.52%` | -35,753,330.09 USD | `-0.42` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `4.00` | `4.02` | `3.97` | `4.01` | `1,324,246` | 5,294,042.85 USD | 316,416.19 USD | `+5.98%` | -35,436,913.90 USD | `+0.48` | **`BULLISH`** | `DELTA ALIGNED` |
| `1h` | `4.06` | `4.08` | `3.90` | `3.99` | `24,939,110` | 99,515,350.06 USD | -6,770,272.40 USD | `-6.80%` | -36,224,836.10 USD | `-1.19` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `3.99` | `4.04` | `3.95` | `4.00` | `8,344,084` | 33,377,841.60 USD | -1,208,714.23 USD | `-3.62%` | -37,433,550.33 USD | `+0.14` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `1h` | `4.00` | `4.02` | `3.97` | `4.02` | `1,327,412` | 5,306,750.64 USD | 329,123.99 USD | `+6.20%` | -37,104,426.34 USD | `+0.43` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `4.65` | `4.69` | `4.38` | `4.40` | `28,351,581` | 128,263,626.10 USD | -4,168,943.82 USD | `-3.25%` | -16,525,751.06 USD | `-0.01` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `4.40` | `4.41` | `4.04` | `4.06` | `71,964,012` | 300,508,235.77 USD | -12,043,039.27 USD | `-4.01%` | -28,568,790.33 USD | `-0.87` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `4.06` | `4.08` | `3.90` | `4.01` | `34,610,106` | 138,197,934.42 USD | -7,651,870.51 USD | `-5.54%` | -36,220,660.84 USD | `-0.24` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `4.32` | `4.44` | `4.31` | `4.42` | `17,257,912` | 75,510,006.79 USD | -1,093,709.03 USD | `-1.45%` | -16,765,834.34 USD | `+1.00` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `4.42` | `4.66` | `4.38` | `4.65` | `38,831,237` | 175,324,190.65 USD | 4,409,027.10 USD | `+2.51%` | -12,356,807.24 USD | `+1.01` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `4.65` | `4.69` | `4.38` | `4.40` | `28,351,581` | 128,263,626.10 USD | -4,168,943.82 USD | `-3.25%` | -16,525,751.06 USD | `-0.01` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `4.40` | `4.41` | `4.04` | `4.06` | `71,964,012` | 300,508,235.77 USD | -12,043,039.27 USD | `-4.01%` | -28,568,790.33 USD | `-0.87` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `4.06` | `4.08` | `3.90` | `4.01` | `34,610,106` | 138,197,934.42 USD | -7,651,870.51 USD | `-5.54%` | -36,220,660.84 USD | `-0.24` | **`BEARISH`** | `DELTA ALIGNED` |

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
| --- | **`4.01`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `MID` | Regular L2 Book | - | - | - | Interbank L2 | 0.00% | Interbank |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 07:43:27 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `68` | `0x7737...bf66` | `LONG` | 22,484,796.08 USD | `5,640,376.30` | `2.35` | `4.03` | `0.7750` | 9,212,893.25 USD | `+40.97%` | `10X Cross` |
| `107` | `0xefe4...194b` | `SHORT` | 18,164,267.88 USD | `4,507,262.50` | `4.21` | `4.03` | `6.67` | 810,828.84 USD | `+4.46%` | `5X Cross` |
| `140` | `0xb581...6f4f` | `LONG` | 14,352,480.00 USD | `3,600,000.00` | `5.19` | `4.03` | `0.2780` | -4,340,555.22 USD | `-30.24%` | `4X Cross` |
| `217` | `0xdd53...2b13` | `SHORT` | 9,668,733.72 USD | `2,400,202.00` | `2.31` | `4.03` | `30.49` | -4,122,885.16 USD | `-42.64%` | `3X Cross` |
| `278` | `0x77ee...2902` | `LONG` | 8,260,757.10 USD | `2,063,023.10` | `1.93` | `4.03` | `0.000000` | 4,269,561.16 USD | `+51.68%` | `10X Cross` |
| `387` | `0xb83d...6e36` | `SHORT` | 5,817,011.74 USD | `1,445,759.10` | `5.19` | `4.03` | `100.05` | 1,692,437.20 USD | `+29.09%` | `3X Cross` |
| `405` | `0xb46b...538e` | `SHORT` | 5,381,007.20 USD | `1,336,000.00` | `4.33` | `4.03` | `7.55` | 403,856.86 USD | `+7.51%` | `10X Cross` |
| `409` | `0x7fda...17d1` | `SHORT` | 5,326,883.76 USD | `1,321,676.20` | `4.30` | `4.03` | `33.12` | 357,056.50 USD | `+6.70%` | `10X Cross` |
| `414` | `0x9df2...c665` | `SHORT` | 5,254,787.02 USD | `1,304,143.90` | `2.09` | `4.03` | `28.30` | -2,531,473.45 USD | `-48.17%` | `10X Cross` |
| `485` | `0x60b0...991e` | `LONG` | 4,500,814.57 USD | `1,121,307.10` | `5.00` | `4.03` | `0.000000` | -1,100,609.86 USD | `-24.45%` | `10X Cross` |
| `504` | `0xcac1...26b3` | `SHORT` | 4,322,570.82 USD | `1,073,743.90` | `2.48` | `4.03` | `12.33` | -1,662,627.35 USD | `-38.46%` | `10X Cross` |
| `524` | `0x781e...96b7` | `SHORT` | 4,190,022.38 USD | `1,039,604.60` | `2.45` | `4.03` | `7.59` | -1,645,685.19 USD | `-39.28%` | `10X Cross` |
| `605` | `0x45d2...4029` | `SHORT` | 3,661,699.10 USD | `909,400.00` | `3.26` | `4.03` | `51.97` | -695,549.20 USD | `-19.00%` | `10X Cross` |
| `851` | `0x005a...61fe` | `LONG` | 2,628,382.70 USD | `652,414.60` | `2.08` | `4.03` | `2.43` | 1,270,851.46 USD | `+48.35%` | `7X Cross` |
| `861` | `0xba5d...a352` | `SHORT` | 2,597,900.39 USD | `647,532.50` | `2.83` | `4.03` | `14.35` | -765,185.45 USD | `-29.45%` | `10X Cross` |
| `868` | `0xb695...a92d` | `SHORT` | 2,574,633.52 USD | `639,231.70` | `4.57` | `4.03` | `47.15` | 348,725.41 USD | `+13.54%` | `10X Cross` |
| `870` | `0xd1dd...9e85` | `SHORT` | 2,560,430.89 USD | `637,621.00` | `4.96` | `4.03` | `18.99` | 603,041.85 USD | `+23.55%` | `10X Cross` |
| `875` | `0x123d...3bff` | `SHORT` | 2,549,257.45 USD | `635,392.30` | `2.09` | `4.03` | `9.06` | -1,223,308.98 USD | `-47.99%` | `10X Cross` |
| `887` | `0xcf53...ee11` | `SHORT` | 2,505,352.35 USD | `621,598.40` | `5.07` | `4.03` | `25.72` | 646,817.90 USD | `+25.82%` | `10X Cross` |
| `1007` | `0xbfc7...80b4` | `SHORT` | 2,126,230.20 USD | `531,000.00` | `2.01` | `4.03` | `8.03` | -1,061,030.81 USD | `-49.90%` | `10X Cross` |
| `1250` | `0x0eec...d4c5` | `LONG` | 1,733,308.32 USD | `429,909.30` | `4.01` | `4.03` | `1.18` | 10,913.20 USD | `+0.63%` | `10X Cross` |
| `1314` | `0x2577...4897` | `LONG` | 1,617,847.24 USD | `401,271.70` | `4.13` | `4.03` | `0.000000` | -41,127.40 USD | `-2.54%` | `10X Cross` |
| `1318` | `0xe097...d0fe` | `LONG` | 1,611,280.00 USD | `400,000.00` | `5.29` | `4.03` | `0.000000` | -505,507.30 USD | `-31.37%` | `10X Cross` |
| `1330` | `0x4cae...7c34` | `LONG` | 1,602,879.37 USD | `398,587.40` | `3.81` | `4.03` | `1.29` | 85,983.98 USD | `+5.36%` | `10X Cross` |
| `1464` | `0x6e8f...4364` | `LONG` | 1,454,125.11 USD | `361,210.50` | `3.28` | `4.03` | `3.57` | 270,064.88 USD | `+18.57%` | `10X Cross` |
| `1482` | `0xef96...9383` | `SHORT` | 1,437,199.86 USD | `357,165.90` | `4.50` | `4.03` | `14.47` | 171,041.93 USD | `+11.90%` | `10X Cross` |
| `1506` | `0xdf95...7d72` | `SHORT` | 1,411,974.75 USD | `350,479.00` | `4.23` | `4.03` | `114.70` | 71,364.41 USD | `+5.05%` | `10X Cross` |
| `1518` | `0x9aa5...58af` | `SHORT` | 1,399,677.14 USD | `347,426.50` | `4.78` | `4.03` | `31.10` | 260,552.51 USD | `+18.62%` | `10X Cross` |
| `1521` | `0xcf67...eb24` | `LONG` | 1,395,870.00 USD | `350,000.00` | `1.98` | `4.03` | `1.91` | 704,252.12 USD | `+50.45%` | `10X Cross` |
| `1613` | `0xfc27...9d9d` | `SHORT` | 1,288,470.74 USD | `319,997.70` | `5.01` | `4.03` | `65.47` | 315,071.88 USD | `+24.45%` | `10X Cross` |
| `1618` | `0x089f...a4f8` | `LONG` | 1,285,017.08 USD | `319,043.30` | `4.06` | `4.03` | `0.000000` | -9,839.63 USD | `-0.77%` | `1X Cross` |
| `1684` | `0x17c3...a868` | `LONG` | 1,216,643.19 USD | `301,874.10` | `4.37` | `4.03` | `0.000000` | -101,518.04 USD | `-8.34%` | `3X Cross` |
| `1692` | `0x9836...457e` | `LONG` | 1,209,092.42 USD | `300,000.60` | `4.57` | `4.03` | `1.90` | -162,980.75 USD | `-13.48%` | `10X Cross` |
| `1739` | `0xe065...0f85` | `SHORT` | 1,160,579.62 USD | `288,027.90` | `2.81` | `4.03` | `5.68` | -350,026.50 USD | `-30.16%` | `10X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `4.79` | 7,562.68 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Whale SELL: 7.56K USD at 4.7859 USD [API] | `2026-10-28 20:03:05` |
| `ANNOUNCEMENT` | `INFO` | `4.78` | 257.09 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Liquidated Long: 0.26K USD at 4.7786 USD [API] | `2026-10-28 20:01:20` |
| `ANNOUNCEMENT` | `INFO` | `4.78` | 477.06 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Liquidated Long: 0.48K USD at 4.7754 USD [API] | `2026-10-28 20:01:11` |
| `ANNOUNCEMENT` | `INFO` | `4.77` | 387.71 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Liquidated Long: 0.39K USD at 4.7748 USD [API] | `2026-10-28 20:01:11` |
| `ANNOUNCEMENT` | `INFO` | `4.77` | 23,853.50 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Whale SELL: 23.85K USD at 4.7707 USD [API] | `2026-10-28 20:05:14` |
| `ANNOUNCEMENT` | `INFO` | `4.77` | 8,946.97 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Whale SELL: 8.95K USD at 4.7707 USD [API] | `2026-10-28 20:05:12` |
| `ANNOUNCEMENT` | `INFO` | `4.78` | 149.02 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Liquidated Long: 0.15K USD at 4.7764 USD [API] | `2026-10-28 20:05:44` |
| `ANNOUNCEMENT` | `INFO` | `4.77` | 6,889.87 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Whale SELL: 6.89K USD at 4.7661 USD [API] | `2026-10-28 20:06:45` |
| `ANNOUNCEMENT` | `INFO` | `4.78` | 8,585.21 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Liquidated Long: 8.59K USD at 4.7754 USD [API] | `2026-10-28 20:01:11` |
| `ANNOUNCEMENT` | `INFO` | `6.00` | 954.79 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Liquidated Short: 0.95K USD at 5.9974 USD [API] | `2026-10-12 04:57:10` |
| `ANNOUNCEMENT` | `INFO` | `6.00` | 1,383.58 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Liquidated Short: 1.38K USD at 5.9973 USD [API] | `2026-10-12 04:57:10` |
| `ANNOUNCEMENT` | `INFO` | `6.00` | 1,383.46 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Liquidated Short: 1.38K USD at 5.9968 USD [API] | `2026-10-12 04:57:10` |
| `ANNOUNCEMENT` | `INFO` | `6.00` | 30.58 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Liquidated Short: 0.03K USD at 5.9968 USD [API] | `2026-10-12 04:57:10` |
| `ANNOUNCEMENT` | `INFO` | `6.00` | 917.43 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Liquidated Short: 0.92K USD at 5.9963 USD [API] | `2026-10-12 04:57:10` |
| `ANNOUNCEMENT` | `INFO` | `4.78` | 11,342.27 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Liquidated Long: 11.34K USD at 4.7771 USD [API] | `2026-10-28 20:01:11` |
| `ANNOUNCEMENT` | `INFO` | `4.78` | 9,007.26 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Liquidated Long: 9.01K USD at 4.7756 USD [API] | `2026-10-28 20:01:11` |
| `ANNOUNCEMENT` | `INFO` | `4.69` | 5,798.10 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Whale SELL: 5.80K USD at 4.6895 USD [API] | `2026-10-28 20:24:43` |
| `ANNOUNCEMENT` | `INFO` | `4.67` | 5,826.81 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Whale SELL: 5.83K USD at 4.6663 USD [API] | `2026-10-28 20:29:19` |
| `ANNOUNCEMENT` | `INFO` | `1.82` | 317.41 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Liquidated Short: 0.32K USD at 1.8200 USD [API] | `2026-06-28 17:35:22` |
| `ANNOUNCEMENT` | `INFO` | `4.68` | 8,432.64 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Whale BUY: 8.43K USD at 4.6796 USD [API] | `2026-10-28 20:37:07` |
| `ANNOUNCEMENT` | `INFO` | `4.68` | 9,000.08 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Whale BUY: 9.00K USD at 4.6795 USD [API] | `2026-10-28 20:37:07` |
| `ANNOUNCEMENT` | `INFO` | `4.68` | 11,342.64 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Whale BUY: 11.34K USD at 4.6795 USD [API] | `2026-10-28 20:37:07` |
| `ANNOUNCEMENT` | `INFO` | `4.70` | 5,721.97 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Whale BUY: 5.72K USD at 4.7017 USD [API] | `2026-10-28 20:52:09` |
| `ANNOUNCEMENT` | `INFO` | `4.71` | 9,007.68 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Whale SELL: 9.01K USD at 4.7099 USD [API] | `2026-10-28 20:54:26` |
| `ANNOUNCEMENT` | `INFO` | `4.71` | 9,002.97 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Whale SELL: 9.00K USD at 4.7099 USD [API] | `2026-10-28 20:54:26` |
| `ANNOUNCEMENT` | `INFO` | `4.73` | 10,254.32 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Whale SELL: 10.25K USD at 4.7268 USD [API] | `2026-10-28 20:58:08` |
| `ANNOUNCEMENT` | `INFO` | `4.78` | 10,361.27 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Liquidated Long: 10.36K USD at 4.7761 USD [API] | `2026-10-28 20:01:11` |
| `ANNOUNCEMENT` | `INFO` | `4.78` | 10,359.10 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Liquidated Long: 10.36K USD at 4.7751 USD [API] | `2026-10-28 20:01:11` |
| `ANNOUNCEMENT` | `INFO` | `4.74` | 7,117.98 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Whale SELL: 7.12K USD at 4.7390 USD [API] | `2026-10-28 20:59:25` |
| `ANNOUNCEMENT` | `INFO` | `4.78` | 3,062.76 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Liquidated Long: 3.06K USD at 4.7766 USD [API] | `2026-10-28 20:01:11` |
| `ANNOUNCEMENT` | `INFO` | `4.74` | 5,692.43 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Whale BUY: 5.69K USD at 4.7358 USD [API] | `2026-10-28 22:09:58` |
| `ANNOUNCEMENT` | `INFO` | `4.74` | 6,421.82 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Whale BUY: 6.42K USD at 4.7404 USD [API] | `2026-10-28 22:36:20` |
| `ANNOUNCEMENT` | `INFO` | `4.74` | 10,286.86 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Whale BUY: 10.29K USD at 4.7418 USD [API] | `2026-10-28 22:47:46` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`4.42` (Vol: 795,900.00 USD, Dist: `+7.72%`) | Long MP=`3.99` (Vol: 531,700.00 USD, Dist: `--2.74%`)
  * 48H Horizon: Short MP=`4.41` (Vol: 795,900.00 USD, Dist: `+7.60%`) | Long MP=`3.99` (Vol: 531,700.00 USD, Dist: `--2.81%`)
  * 3D Horizon: Short MP=`4.41` (Vol: 795,900.00 USD, Dist: `+7.60%`) | Long MP=`3.99` (Vol: 531,700.00 USD, Dist: `--2.81%`)
  * 7D Horizon: Short MP=`5.01` (Vol: 953,300.00 USD, Dist: `+22.13%`) | Long MP=`3.99` (Vol: 531,700.00 USD, Dist: `--2.76%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long Liquidation` | `0.8050` | 73,060.00 USD | 19,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8450` | 2,030.00 USD | 19,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8550` | 3,680.00 USD | 19,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8650` | 433.80 USD | 19,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8750` | 8,310.00 USD | 19,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8950` | 39,460.00 USD | 19,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9050` | 292.22 USD | 19,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9150` | 11,790.00 USD | 19,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9450` | 9,450.00 USD | 19,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9550` | 528.88 USD | 19,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9650` | 965.00 USD | 19,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9750` | 123.53 USD | 19,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9850` | 707.53 USD | 19,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9950` | 154,200.00 USD | 19,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.01` | 1,340.00 USD | 18,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.02` | 10,250.00 USD | 18,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.03` | 36,980.00 USD | 18,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.04` | 2,740.00 USD | 18,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.05` | 4,480.00 USD | 18,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.06` | 892.90 USD | 18,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.07` | 7,840.00 USD | 18,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.08` | 205,550.00 USD | 18,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.09` | 4,030.00 USD | 18,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.11` | 557.50 USD | 18,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.12` | 1,580.00 USD | 18,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.14` | 4,960.00 USD | 18,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.15` | 26,620.00 USD | 18,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.17` | 1,110.00 USD | 18,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.18` | 19,930.00 USD | 18,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.19` | 2,140.00 USD | 18,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.22` | 396.09 USD | 18,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.25` | 1,220.00 USD | 18,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.26` | 5,250.00 USD | 18,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.27` | 2,390.00 USD | 18,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.28` | 169.23 USD | 18,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.30` | 328.21 USD | 18,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.31` | 146.10 USD | 18,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.32` | 4,150.00 USD | 18,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.34` | 73,410.00 USD | 18,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.35` | 3,230.00 USD | 18,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.36` | 6,220.00 USD | 18,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.38` | 12,380.00 USD | 18,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.39` | 13,340.00 USD | 18,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.40` | 42,490.00 USD | 18,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.41` | 28,140.00 USD | 18,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.42` | 9,190.00 USD | 18,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.43` | 855.00 USD | 18,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.45` | 1,040.00 USD | 18,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.48` | 14,750.00 USD | 18,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.50` | 441.57 USD | 18,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.51` | 454.50 USD | 18,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.52` | 1,820.00 USD | 18,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.53` | 3,500.00 USD | 18,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.54` | 77,250.00 USD | 18,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.55` | 311.00 USD | 18,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.56` | 20,570.00 USD | 18,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.57` | 825.46 USD | 18,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.59` | 3,700.00 USD | 18,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.60` | 2,260.00 USD | 18,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.62` | 6,010.00 USD | 18,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.64` | 2,030.00 USD | 18,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.65` | 2,350.00 USD | 18,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.66` | 384.13 USD | 18,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.67` | 2,660.00 USD | 18,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.68` | 108.71 USD | 18,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.69` | 12,850.00 USD | 18,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.71` | 156,200.00 USD | 18,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.73` | 5,460.00 USD | 18,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.75` | 920.49 USD | 18,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.75` | 10,860.00 USD | 18,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.77` | 4,100.00 USD | 18,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.78` | 5,270.00 USD | 18,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.79` | 2,900.00 USD | 18,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.80` | 2,370.00 USD | 18,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.81` | 28,810.00 USD | 18,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.82` | 7,370.00 USD | 18,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.83` | 41,990.00 USD | 18,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.84` | 645,750.00 USD | 17,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.85` | 557,490.00 USD | 17,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.86` | 184.82 USD | 16,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.88` | 393.56 USD | 16,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.89` | 1,540.00 USD | 16,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.90` | 2,080.00 USD | 16,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.91` | 3,950.00 USD | 16,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.92` | 49,920.00 USD | 16,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.93` | 154.77 USD | 16,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.94` | 7,300.00 USD | 16,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.95` | 2,740.00 USD | 16,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.96` | 15,710.00 USD | 16,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.97` | 6,350.00 USD | 16,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.98` | 356,140.00 USD | 16,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.99` | 53,060.00 USD | 16,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.00` | 20,240.00 USD | 16,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.02` | 141,710.00 USD | 16,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.02` | 260.62 USD | 16,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.04` | 102,580.00 USD | 16,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.04` | 4,480.00 USD | 15,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.06` | 11,890.00 USD | 15,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.06` | 7,180.00 USD | 15,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.08` | 6,690.00 USD | 15,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.08` | 18,600.00 USD | 15,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.10` | 1,310.00 USD | 15,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.10` | 7,880.00 USD | 15,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.12` | 12,630.00 USD | 15,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.12` | 32,770.00 USD | 15,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.13` | 1,180.00 USD | 15,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.15` | 110.04 USD | 15,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.15` | 2,150.00 USD | 15,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.17` | 1,100.00 USD | 15,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.17` | 2,560.00 USD | 15,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.19` | 104,270.00 USD | 15,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.19` | 10,250.00 USD | 15,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.21` | 33,940.00 USD | 15,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.21` | 2,010.00 USD | 15,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.23` | 3,110.00 USD | 15,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.25` | 57,210.00 USD | 15,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.25` | 115,820.00 USD | 15,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.27` | 379,750.00 USD | 15,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.29` | 1,330.00 USD | 15,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.29` | 3,570.00 USD | 15,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.31` | 1,980.00 USD | 15,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.31` | 2,140.00 USD | 15,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.33` | 6,180.00 USD | 15,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.35` | 43,490.00 USD | 15,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.35` | 8,310.00 USD | 15,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.37` | 70,820.00 USD | 15,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.38` | 431,710.00 USD | 15,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.38` | 38,280.00 USD | 14,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.40` | 465,510.00 USD | 14,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.40` | 36,690.00 USD | 14,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.42` | 286,450.00 USD | 14,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.42` | 273,060.00 USD | 13,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.44` | 1,600,000.00 USD | 13,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.44` | 3,700.00 USD | 11,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.46` | 1,360.00 USD | 11,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.46` | 6,130.00 USD | 11,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.48` | 336.35 USD | 11,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.48` | 10,220.00 USD | 11,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.50` | 2,130.00 USD | 11,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.50` | 33,560.00 USD | 11,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.52` | 17,890.00 USD | 11,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.54` | 7,250.00 USD | 11,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.54` | 11,140.00 USD | 11,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.56` | 5,420.00 USD | 11,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.56` | 11,370.00 USD | 11,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.58` | 2,810.00 USD | 11,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.58` | 905.27 USD | 11,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.60` | 116,830.00 USD | 11,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.60` | 666.10 USD | 11,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.62` | 17,220.00 USD | 11,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.62` | 3,780.00 USD | 11,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.63` | 25,270.00 USD | 11,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.65` | 2,650.00 USD | 11,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.65` | 18,510.00 USD | 11,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.67` | 81,240.00 USD | 11,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.67` | 17,840.00 USD | 11,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.69` | 4,860.00 USD | 11,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.69` | 733.85 USD | 11,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.71` | 127,130.00 USD | 11,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.71` | 11,940.00 USD | 11,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.73` | 27,780.00 USD | 11,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.73` | 14,100.00 USD | 11,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.75` | 41,680.00 USD | 11,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.75` | 25,260.00 USD | 11,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.77` | 358,140.00 USD | 11,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.77` | 13,310.00 USD | 10,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.79` | 70,320.00 USD | 10,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.79` | 25,660.00 USD | 10,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.81` | 22,400.00 USD | 10,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.81` | 42,850.00 USD | 10,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.83` | 3,910.00 USD | 10,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.83` | 1,140.00 USD | 10,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.85` | 4,490.00 USD | 10,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.85` | 1,980.00 USD | 10,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.87` | 11,220.00 USD | 10,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.88` | 389,820.00 USD | 10,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.88` | 6,800.00 USD | 10,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.90` | 23,820.00 USD | 10,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.90` | 88,370.00 USD | 10,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.92` | 94,100.00 USD | 10,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.92` | 48,610.00 USD | 10,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.94` | 49,570.00 USD | 10,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.94` | 19,090.00 USD | 9,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.96` | 1,470.00 USD | 9,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.96` | 3,170.00 USD | 9,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.98` | 41,370.00 USD | 9,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.98` | 4,870.00 USD | 9,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.00` | 2,000.00 USD | 9,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.00` | 10,410.00 USD | 9,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.02` | 21,830.00 USD | 9,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.02` | 7,060.00 USD | 9,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.04` | 7,200.00 USD | 9,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.04` | 170,120.00 USD | 9,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.06` | 25,520.00 USD | 9,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.06` | 116,000.00 USD | 9,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.08` | 3,090.00 USD | 9,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.08` | 32,250.00 USD | 9,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.10` | 239,320.00 USD | 9,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.10` | 17,980.00 USD | 9,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.12` | 36,650.00 USD | 9,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.12` | 15,600.00 USD | 9,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.13` | 228,890.00 USD | 9,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.15` | 23,000.00 USD | 8,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.15` | 46,550.00 USD | 8,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.17` | 7,040.00 USD | 8,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.17` | 6,970.00 USD | 8,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.19` | 245,480.00 USD | 8,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.21` | 1,090.00 USD | 8,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.21` | 19,660.00 USD | 8,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.23` | 338,820.00 USD | 8,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.23` | 42,020.00 USD | 8,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.25` | 20,160.00 USD | 8,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.25` | 5,640.00 USD | 8,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.27` | 51,020.00 USD | 8,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.27` | 841,550.00 USD | 8,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.29` | 61,360.00 USD | 7,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.29` | 135,090.00 USD | 7,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.31` | 308,100.00 USD | 7,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.31` | 134,620.00 USD | 6,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.33` | 14,710.00 USD | 6,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.33` | 115,790.00 USD | 6,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.35` | 56,630.00 USD | 6,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.35` | 1,480.00 USD | 6,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.37` | 2,060.00 USD | 6,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.38` | 159,680.00 USD | 6,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.38` | 43,640.00 USD | 6,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.40` | 83,190.00 USD | 6,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.42` | 383,360.00 USD | 6,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.42` | 28,690.00 USD | 5,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.44` | 26,030.00 USD | 5,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.44` | 46,740.00 USD | 5,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.46` | 8,840.00 USD | 5,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.46` | 14,340.00 USD | 5,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.48` | 180,040.00 USD | 5,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.48` | 24,990.00 USD | 5,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.50` | 69,220.00 USD | 5,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.50` | 31,490.00 USD | 5,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.52` | 7,350.00 USD | 5,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.52` | 189,090.00 USD | 5,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.54` | 79,310.00 USD | 5,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.54` | 177,080.00 USD | 5,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.56` | 375,580.00 USD | 4,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.56` | 9,280.00 USD | 4,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.58` | 62,290.00 USD | 4,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.58` | 94,480.00 USD | 4,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.59` | 12,300,000.00 USD | 12,300,000.00 USD | 176,290.00 USD | 66,810.00 USD | 144,570.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.60` | 1,330,000.00 USD | 4,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.60` | 11,920,000.00 USD | 11,920,000.00 USD | 64,170.00 USD | 21,460.00 USD | 22,050.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.60` | 60,200.00 USD | 3,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.61` | 11,810,000.00 USD | 11,810,000.00 USD | 55,130.00 USD | 17,400.00 USD | 44,890.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.62` | 3,620.00 USD | 3,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.62` | 11,690,000.00 USD | 11,690,000.00 USD | 92,130.00 USD | 26,640.00 USD | 97,570.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.62` | 43,700.00 USD | 3,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.63` | 5,930,000.00 USD | 5,930,000.00 USD | 1,910.00 USD | 9,650.00 USD | 22,610.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.63` | 11,480,000.00 USD | 11,480,000.00 USD | 50,840.00 USD | 8,120.00 USD | 159.02 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.63` | 2,680.00 USD | 2,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.64` | 5,900,000.00 USD | 5,900,000.00 USD | 152.80 USD | 5,040.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.64` | 11,420,000.00 USD | 11,420,000.00 USD | 2,410.00 USD | 14,370.00 USD | 119,140.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.65` | 43,430.00 USD | 2,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.65` | 5,890,000.00 USD | 5,890,000.00 USD | 386.30 USD | 0.00 USD | 13.37 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.65` | 11,280,000.00 USD | 11,280,000.00 USD | 52,910.00 USD | 7,050.00 USD | 31,190.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.65` | 20,650.00 USD | 2,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.66` | 5,890,000.00 USD | 5,890,000.00 USD | 291.38 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.66` | 11,190,000.00 USD | 11,190,000.00 USD | 30,480.00 USD | 15,090.00 USD | 125,270.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.67` | 141,430.00 USD | 2,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.67` | 5,890,000.00 USD | 5,890,000.00 USD | 16,750.00 USD | 3,070.00 USD | 11,520.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.67` | 11,020,000.00 USD | 11,020,000.00 USD | 47,650.00 USD | 14,480.00 USD | 53,670.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.67` | 220,440.00 USD | 2,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.68` | 5,860,000.00 USD | 5,860,000.00 USD | 216.77 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.69` | 144,940.00 USD | 2,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.69` | 5,860,000.00 USD | 5,860,000.00 USD | 23,960.00 USD | 0.00 USD | 281.19 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.69` | 10,900,000.00 USD | 10,900,000.00 USD | 27,750.00 USD | 0.00 USD | 59,840.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.69` | 111,990.00 USD | 2,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.70` | 5,840,000.00 USD | 5,840,000.00 USD | 39,190.00 USD | 4,110.00 USD | 55,010.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.70` | 10,820,000.00 USD | 10,820,000.00 USD | 20,470.00 USD | 7,370.00 USD | 112,470.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.71` | 229,560.00 USD | 2,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.71` | 5,740,000.00 USD | 5,740,000.00 USD | 430.40 USD | 0.00 USD | 522.93 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.71` | 10,680,000.00 USD | 10,680,000.00 USD | 50,620.00 USD | 0.00 USD | 74,330.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.71` | 50,160.00 USD | 2,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.72` | 5,740,000.00 USD | 5,740,000.00 USD | 403.05 USD | 0.00 USD | 18.60 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.72` | 10,550,000.00 USD | 10,550,000.00 USD | 425.03 USD | 0.00 USD | 183.06 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.73` | 179,640.00 USD | 2,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.73` | 5,740,000.00 USD | 5,740,000.00 USD | 8,890.00 USD | 6,020.00 USD | 8,370.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.73` | 10,550,000.00 USD | 10,550,000.00 USD | 38,260.00 USD | 10,880.00 USD | 56,790.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.73` | 141,610.00 USD | 1,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.74` | 5,710,000.00 USD | 5,710,000.00 USD | 94,200.00 USD | 33,110.00 USD | 42,360.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.74` | 10,440,000.00 USD | 10,440,000.00 USD | 128,440.00 USD | 40,020.00 USD | 122,480.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.75` | 96,600.00 USD | 1,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.75` | 5,540,000.00 USD | 5,540,000.00 USD | 0.00 USD | 0.00 USD | 20,450.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.75` | 10,150,000.00 USD | 10,150,000.00 USD | 1,770.00 USD | 24,350.00 USD | 42,760.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.75` | 165,310.00 USD | 1,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.76` | 5,520,000.00 USD | 5,520,000.00 USD | 0.00 USD | 2,230.00 USD | 10,030.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.76` | 10,080,000.00 USD | 10,080,000.00 USD | 32,650.00 USD | 10,110.00 USD | 22,610.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.77` | 279,910.00 USD | 1,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.77` | 5,510,000.00 USD | 5,510,000.00 USD | 187.12 USD | 5,330.00 USD | 2,020.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.77` | 10,020,000.00 USD | 10,020,000.00 USD | 13,170.00 USD | 8,090.00 USD | 23,020.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.77` | 139,340.00 USD | 1,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.78` | 5,500,000.00 USD | 5,500,000.00 USD | 106.91 USD | 4,490.00 USD | 29,810.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.78` | 9,970,000.00 USD | 9,970,000.00 USD | 21,640.00 USD | 15,520.00 USD | 41,570.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.79` | 26,860.00 USD | 1,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.79` | 5,470,000.00 USD | 5,470,000.00 USD | 472.79 USD | 0.00 USD | 176.51 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.79` | 9,900,000.00 USD | 9,900,000.00 USD | 49,420.00 USD | 0.00 USD | 38,980.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.79` | 150,080.00 USD | 980,140.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.80` | 5,470,000.00 USD | 5,470,000.00 USD | 1,270.00 USD | 0.00 USD | 1,720.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.80` | 9,810,000.00 USD | 9,810,000.00 USD | 1,530.00 USD | 18,170.00 USD | 17,780.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.81` | 106,830.00 USD | 830,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.81` | 5,470,000.00 USD | 5,470,000.00 USD | 54,290.00 USD | 0.00 USD | 13,100.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.81` | 9,770,000.00 USD | 9,770,000.00 USD | 0.00 USD | 0.00 USD | 1,350.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.81` | 126,250.00 USD | 723,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.82` | 5,400,000.00 USD | 5,400,000.00 USD | 487.48 USD | 11,960.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.82` | 9,770,000.00 USD | 9,770,000.00 USD | 527.85 USD | 18,370.00 USD | 25,600.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.83` | 32,950.00 USD | 596,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.83` | 5,390,000.00 USD | 5,390,000.00 USD | 1,150.00 USD | 18,900.00 USD | 17,280.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.83` | 9,720,000.00 USD | 9,720,000.00 USD | 0.00 USD | 0.00 USD | 89.29 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.83` | 207,520.00 USD | 564,030.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.84` | 5,350,000.00 USD | 5,350,000.00 USD | 0.00 USD | 0.00 USD | 784.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.84` | 9,720,000.00 USD | 9,720,000.00 USD | 2,020.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.85` | 125,510.00 USD | 356,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.85` | 5,350,000.00 USD | 5,350,000.00 USD | 929.01 USD | 6,330.00 USD | 141.64 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.85` | 9,720,000.00 USD | 9,720,000.00 USD | 0.00 USD | 0.00 USD | 5,500.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.85` | 19,690.00 USD | 231,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.86` | 5,340,000.00 USD | 5,340,000.00 USD | 2,080.00 USD | 12,320.00 USD | 54,290.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.86` | 9,720,000.00 USD | 9,720,000.00 USD | 2,220.00 USD | 0.00 USD | 72,520.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.87` | 76,590.00 USD | 211,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.87` | 5,270,000.00 USD | 5,270,000.00 USD | 1,690.00 USD | 11,800.00 USD | 845.92 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.87` | 9,640,000.00 USD | 9,640,000.00 USD | 57,040.00 USD | 0.00 USD | 29,890.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.88` | 11,710.00 USD | 134,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.88` | 5,260,000.00 USD | 5,260,000.00 USD | 106,680.00 USD | 6,860.00 USD | 39,950.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.88` | 9,550,000.00 USD | 9,550,000.00 USD | 106,950.00 USD | 8,890.00 USD | 101,810.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.88` | 44,870.00 USD | 123,010.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.89` | 5,100,000.00 USD | 5,100,000.00 USD | 113,490.00 USD | 37,150.00 USD | 23,350.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.89` | 9,340,000.00 USD | 9,340,000.00 USD | 1,210.00 USD | 50,710.00 USD | 1,390.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.90` | 73,800.00 USD | 78,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.90` | 4,930,000.00 USD | 4,930,000.00 USD | 31,410.00 USD | 10,910.00 USD | 21,360.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.90` | 9,280,000.00 USD | 9,280,000.00 USD | 171,750.00 USD | 28,250.00 USD | 51,570.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.90` | 4,350.00 USD | 4,350.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.91` | 4,870,000.00 USD | 4,870,000.00 USD | 32,140.00 USD | 35,760.00 USD | 39,260.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.91` | 9,030,000.00 USD | 9,030,000.00 USD | 3,970.00 USD | 25,680.00 USD | 46,930.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3.92` | 4,760,000.00 USD | 4,760,000.00 USD | 148,140.00 USD | 26,030.00 USD | 33,330.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.92` | 8,960,000.00 USD | 8,960,000.00 USD | 90,780.00 USD | 41,330.00 USD | 89,160.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3.93` | 4,550,000.00 USD | 4,550,000.00 USD | 0.00 USD | 29,900.00 USD | 38,510.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.93` | 8,730,000.00 USD | 8,730,000.00 USD | 51,660.00 USD | 20,780.00 USD | 19,870.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3.94` | 4,480,000.00 USD | 4,480,000.00 USD | 96,340.00 USD | 14,940.00 USD | 20,530.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.94` | 8,640,000.00 USD | 8,640,000.00 USD | 82,440.00 USD | 31,050.00 USD | 96,310.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3.95` | 4,350,000.00 USD | 4,350,000.00 USD | 95,940.00 USD | 15,880.00 USD | 95,070.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.95` | 8,430,000.00 USD | 8,430,000.00 USD | 8,490.00 USD | 19,870.00 USD | 2,700.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3.96` | 4,150,000.00 USD | 4,150,000.00 USD | 65,960.00 USD | 39,680.00 USD | 36,690.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.96` | 8,400,000.00 USD | 8,400,000.00 USD | 166,560.00 USD | 15,590.00 USD | 312,280.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3.97` | 4,000,000.00 USD | 4,000,000.00 USD | 190,720.00 USD | 66,010.00 USD | 102,960.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.97` | 7,910,000.00 USD | 7,910,000.00 USD | 231,790.00 USD | 102,960.00 USD | 271,360.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3.98` | 3,640,000.00 USD | 3,640,000.00 USD | 192,590.00 USD | 43,880.00 USD | 14,880.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.98` | 7,300,000.00 USD | 7,300,000.00 USD | 295,470.00 USD | 147,090.00 USD | 230,240.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `3.99` | 3,390,000.00 USD | 3,390,000.00 USD | 413,960.00 USD | 106,190.00 USD | 138,330.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.99` | 6,630,000.00 USD | 6,630,000.00 USD | 63,200.00 USD | 103,210.00 USD | 78,470.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `4.00` | 2,730,000.00 USD | 2,730,000.00 USD | 35,730.00 USD | 53,390.00 USD | 134,490.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.00` | 6,380,000.00 USD | 6,380,000.00 USD | 317,210.00 USD | 126,990.00 USD | 166,390.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `4.01` | 2,510,000.00 USD | 2,510,000.00 USD | 112,570.00 USD | 72,850.00 USD | 129,520.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.01` | 5,770,000.00 USD | 5,770,000.00 USD | 392,150.00 USD | 94,720.00 USD | 438,650.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `4.02` | 2,190,000.00 USD | 2,190,000.00 USD | 243,600.00 USD | 50,310.00 USD | 107,340.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.02` | 4,850,000.00 USD | 4,850,000.00 USD | 279,800.00 USD | 88,330.00 USD | 250,940.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `4.03` | 1,790,000.00 USD | 1,790,000.00 USD | 189,730.00 USD | 76,190.00 USD | 266,680.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.03` | 4,230,000.00 USD | 4,230,000.00 USD | 250,870.00 USD | 45,290.00 USD | 147,160.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `4.04` | 1,260,000.00 USD | 1,260,000.00 USD | 105,670.00 USD | 48,960.00 USD | 207,560.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.04` | 3,780,000.00 USD | 3,780,000.00 USD | 326,350.00 USD | 65,670.00 USD | 491,840.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.04` | 2,180.00 USD | 2,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.05` | 898,580.00 USD | 898,580.00 USD | 2,370.00 USD | 46,690.00 USD | 95,690.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.05` | 2,900,000.00 USD | 2,900,000.00 USD | 291,930.00 USD | 117,530.00 USD | 85,640.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `4.06` | 753,820.00 USD | 753,820.00 USD | 0.00 USD | 27,150.00 USD | 125,920.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.06` | 2,410,000.00 USD | 2,410,000.00 USD | 305,310.00 USD | 72,410.00 USD | 187,820.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `4.07` | 600,750.00 USD | 600,750.00 USD | 0.00 USD | 72,110.00 USD | 22,350.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.07` | 1,840,000.00 USD | 1,840,000.00 USD | 715,320.00 USD | 219,920.00 USD | 329,160.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `4.08` | 506,300.00 USD | 506,300.00 USD | 506,300.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.08` | 575,150.00 USD | 575,150.00 USD | 9,180.00 USD | 117,780.00 USD | 229,680.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.09` | 218,520.00 USD | 218,520.00 USD | 134,630.00 USD | 83,890.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.10` | 143,210.00 USD | 143,210.00 USD | 24,900.00 USD | 118,310.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.10` | 286,420.00 USD | 286,420.00 USD | 24,900.00 USD | 118,310.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.11` | 2,960.00 USD | 5,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4.12` | 1,700.00 USD | 6,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.12` | 309,660.00 USD | 309,660.00 USD | 0.00 USD | 80,980.00 USD | 228,680.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.12` | 35,040.00 USD | 41,880.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.13` | 471,110.00 USD | 471,110.00 USD | 0.00 USD | 0.00 USD | 161,450.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.14` | 531,130.00 USD | 531,130.00 USD | 60,020.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.14` | 377,250.00 USD | 377,250.00 USD | 0.00 USD | 90,830.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.14` | 5,620.00 USD | 47,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.15` | 595,400.00 USD | 595,400.00 USD | 64,270.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.15` | 431,140.00 USD | 431,140.00 USD | 0.00 USD | 53,890.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.16` | 638.21 USD | 48,140.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4.17` | 41,650.00 USD | 89,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.17` | 664,710.00 USD | 664,710.00 USD | 0.00 USD | 16,800.00 USD | 52,510.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.17` | 2,340.00 USD | 92,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.18` | 874,490.00 USD | 874,490.00 USD | 192,730.00 USD | 17,040.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.18` | 1,280.00 USD | 93,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.19` | 1,250,000.00 USD | 1,250,000.00 USD | 174,270.00 USD | 20,540.00 USD | 185,170.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.20` | 6,530.00 USD | 99,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `4.20` | 1,030,000.00 USD | 1,030,000.00 USD | 227,690.00 USD | 0.00 USD | 371,630.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.21` | 194.69 USD | 100,140.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.21` | 1,330,000.00 USD | 1,330,000.00 USD | 58,200.00 USD | 20,820.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.21` | 2,120.00 USD | 102,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.22` | 1,530,000.00 USD | 1,530,000.00 USD | 97,990.00 USD | 27,150.00 USD | 74,260.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.22` | 11,950.00 USD | 114,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.23` | 2,200,000.00 USD | 2,200,000.00 USD | 203,550.00 USD | 468,020.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.24` | 1,190.00 USD | 115,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.24` | 2,880,000.00 USD | 2,880,000.00 USD | 506,300.00 USD | 0.00 USD | 173,430.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.25` | 649.06 USD | 116,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.25` | 3,210,000.00 USD | 3,210,000.00 USD | 0.00 USD | 72,920.00 USD | 255,640.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.25` | 1,090,000.00 USD | 1,090,000.00 USD | 0.00 USD | 57,340.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.25` | 1,780.00 USD | 117,820.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.26` | 3,480,000.00 USD | 3,480,000.00 USD | 92,160.00 USD | 173,320.00 USD | 248.22 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.26` | 1,820,000.00 USD | 1,820,000.00 USD | 0.00 USD | 378,440.00 USD | 355,620.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.26` | 328.41 USD | 118,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.27` | 4,340,000.00 USD | 4,340,000.00 USD | 677,660.00 USD | 34,890.00 USD | 152,200.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.27` | 3,610,000.00 USD | 3,610,000.00 USD | 18,140.00 USD | 194,220.00 USD | 1,580,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.28` | 4,970,000.00 USD | 4,970,000.00 USD | 305,690.00 USD | 30,410.00 USD | 288,910.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.28` | 5,520,000.00 USD | 5,520,000.00 USD | 113,840.00 USD | 497,680.00 USD | 1,300,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.29` | 163.69 USD | 118,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.29` | 5,320,000.00 USD | 5,320,000.00 USD | 153,130.00 USD | 32,690.00 USD | 161,450.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.29` | 5,570,000.00 USD | 5,570,000.00 USD | 0.00 USD | 46,530.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.29` | 210,730.00 USD | 329,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.30` | 5,560,000.00 USD | 5,560,000.00 USD | 32,410.00 USD | 45,120.00 USD | 163,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.30` | 6,040,000.00 USD | 6,040,000.00 USD | 214,920.00 USD | 180,920.00 USD | 75,610.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.30` | 573.00 USD | 329,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.31` | 5,970,000.00 USD | 5,970,000.00 USD | 304,920.00 USD | 13,580.00 USD | 95,430.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.31` | 6,470,000.00 USD | 6,470,000.00 USD | 213,530.00 USD | 53,890.00 USD | 170,400.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.32` | 28,390.00 USD | 358,010.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.32` | 6,130,000.00 USD | 6,130,000.00 USD | 86,850.00 USD | 73,400.00 USD | 18.65 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.32` | 7,120,000.00 USD | 7,120,000.00 USD | 265,720.00 USD | 160,980.00 USD | 222,930.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.33` | 6,570,000.00 USD | 6,570,000.00 USD | 255,620.00 USD | 93,880.00 USD | 87,760.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.33` | 7,240,000.00 USD | 7,240,000.00 USD | 2,690.00 USD | 27,170.00 USD | 88,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.34` | 7,090,000.00 USD | 7,090,000.00 USD | 270,720.00 USD | 140,540.00 USD | 114,690.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.34` | 7,420,000.00 USD | 7,420,000.00 USD | 4,550.00 USD | 28,670.00 USD | 141,900.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.34` | 69,420.00 USD | 427,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.35` | 7,180,000.00 USD | 7,180,000.00 USD | 855.62 USD | 0.00 USD | 84,830.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.35` | 7,500,000.00 USD | 7,500,000.00 USD | 0.00 USD | 0.00 USD | 85,370.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.36` | 4,970.00 USD | 432,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.36` | 7,310,000.00 USD | 7,310,000.00 USD | 84,880.00 USD | 12,310.00 USD | 31,110.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.36` | 7,650,000.00 USD | 7,650,000.00 USD | 8,190.00 USD | 0.00 USD | 140,550.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.37` | 21,970.00 USD | 454,380.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.37` | 7,540,000.00 USD | 7,540,000.00 USD | 52,520.00 USD | 46,860.00 USD | 130,010.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.38` | 1,110.00 USD | 455,490.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.38` | 8,380,000.00 USD | 8,380,000.00 USD | 248,590.00 USD | 34,500.00 USD | 559,230.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.38` | 8,050,000.00 USD | 8,050,000.00 USD | 0.00 USD | 141,930.00 USD | 261,380.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.39` | 8,710,000.00 USD | 8,710,000.00 USD | 399.48 USD | 17,360.00 USD | 310,880.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.39` | 8,570,000.00 USD | 8,570,000.00 USD | 248,520.00 USD | 108,260.00 USD | 154,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.39` | 192,710.00 USD | 648,200.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.40` | 9,110,000.00 USD | 9,110,000.00 USD | 288,790.00 USD | 34,040.00 USD | 81,970.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.40` | 9,170,000.00 USD | 9,170,000.00 USD | 108,780.00 USD | 26,950.00 USD | 463,990.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.41` | 1,410.00 USD | 649,600.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.41` | 9,490,000.00 USD | 9,490,000.00 USD | 196,820.00 USD | 112,990.00 USD | 65,530.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.41` | 9,490,000.00 USD | 9,490,000.00 USD | 0.00 USD | 45,930.00 USD | 278,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.42` | 52,950.00 USD | 702,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.42` | 9,540,000.00 USD | 9,540,000.00 USD | 0.00 USD | 47,240.00 USD | 774.54 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.42` | 10,140,000.00 USD | 10,140,000.00 USD | 404,280.00 USD | 71,590.00 USD | 175,990.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.42` | 104.87 USD | 702,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.43` | 9,690,000.00 USD | 9,690,000.00 USD | 5,100.00 USD | 49,400.00 USD | 98,670.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.43` | 10,420,000.00 USD | 10,420,000.00 USD | 163,540.00 USD | 46,230.00 USD | 71,660.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.44` | 10,470,000.00 USD | 10,470,000.00 USD | 154,480.00 USD | 339,100.00 USD | 290,890.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.44` | 10,610,000.00 USD | 10,610,000.00 USD | 0.00 USD | 116,400.00 USD | 72,830.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.45` | 10,530,000.00 USD | 10,530,000.00 USD | 649.63 USD | 50,720.00 USD | 1,400.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.46` | 10,540,000.00 USD | 10,540,000.00 USD | 704.30 USD | 9,070.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.46` | 10,680,000.00 USD | 10,680,000.00 USD | 0.00 USD | 62,110.00 USD | 2,080.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.46` | 468.38 USD | 703,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.47` | 10,570,000.00 USD | 10,570,000.00 USD | 210.23 USD | 16,700.00 USD | 18,310.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.47` | 11,020,000.00 USD | 11,020,000.00 USD | 203,160.00 USD | 135,940.00 USD | 2,060.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.47` | 1,200.00 USD | 704,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.48` | 10,790,000.00 USD | 10,790,000.00 USD | 117,480.00 USD | 73,240.00 USD | 26,920.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.48` | 11,020,000.00 USD | 11,020,000.00 USD | 0.00 USD | 0.00 USD | 1,510.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.49` | 16,750.00 USD | 721,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.49` | 11,350,000.00 USD | 11,350,000.00 USD | 252,600.00 USD | 155,000.00 USD | 150,280.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.49` | 11,360,000.00 USD | 11,360,000.00 USD | 242,770.00 USD | 93,790.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.50` | 90,180.00 USD | 811,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.50` | 11,890,000.00 USD | 11,890,000.00 USD | 361,770.00 USD | 65,710.00 USD | 120,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.50` | 11,930,000.00 USD | 11,930,000.00 USD | 373,240.00 USD | 200,700.00 USD | 1,820.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.50` | 65,700.00 USD | 876,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.51` | 12,700,000.00 USD | 12,700,000.00 USD | 186,860.00 USD | 307,580.00 USD | 312,530.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.51` | 12,010,000.00 USD | 12,010,000.00 USD | 77,780.00 USD | 0.00 USD | 2,030.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.51` | 389.19 USD | 877,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.52` | 13,320,000.00 USD | 13,320,000.00 USD | 287,830.00 USD | 92,260.00 USD | 242,880.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.52` | 12,150,000.00 USD | 12,150,000.00 USD | 2,080.00 USD | 0.00 USD | 138,450.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.53` | 18,820.00 USD | 896,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.53` | 14,090,000.00 USD | 14,090,000.00 USD | 487,540.00 USD | 0.00 USD | 279,080.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.53` | 13,130,000.00 USD | 13,130,000.00 USD | 438,070.00 USD | 232,800.00 USD | 309,560.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.54` | 198.18 USD | 896,380.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.54` | 14,810,000.00 USD | 14,810,000.00 USD | 216.65 USD | 150,600.00 USD | 564,340.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.54` | 14,370,000.00 USD | 14,370,000.00 USD | 0.00 USD | 0.00 USD | 1,240,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.54` | 252.70 USD | 896,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.55` | 15,020,000.00 USD | 15,020,000.00 USD | 0.00 USD | 22,540.00 USD | 195,790.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.55` | 8,980.00 USD | 905,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.56` | 15,430,000.00 USD | 15,430,000.00 USD | 79,110.00 USD | 32,800.00 USD | 288,660.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.56` | 14,850,000.00 USD | 14,850,000.00 USD | 361,350.00 USD | 124,220.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.57` | 243.77 USD | 905,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.57` | 15,740,000.00 USD | 15,740,000.00 USD | 177,440.00 USD | 70,180.00 USD | 67,980.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.57` | 15,400,000.00 USD | 15,400,000.00 USD | 305,830.00 USD | 27,650.00 USD | 209,310.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.58` | 14,690.00 USD | 920,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.58` | 17,200,000.00 USD | 17,200,000.00 USD | 506,750.00 USD | 73,690.00 USD | 875,260.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.58` | 15,530,000.00 USD | 15,530,000.00 USD | 44,380.00 USD | 0.00 USD | 85,990.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.59` | 18,180,000.00 USD | 18,180,000.00 USD | 826,150.00 USD | 75,460.00 USD | 79,420.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.59` | 17,120,000.00 USD | 17,120,000.00 USD | 760,880.00 USD | 40,640.00 USD | 794,930.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.60` | 18,380,000.00 USD | 18,380,000.00 USD | 54,450.00 USD | 84,420.00 USD | 66,160.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.60` | 17,240,000.00 USD | 17,240,000.00 USD | 3,460.00 USD | 112,080.00 USD | 2,360.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.61` | 156,780.00 USD | 1,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.61` | 18,520,000.00 USD | 18,520,000.00 USD | 66,620.00 USD | 7,560.00 USD | 60,990.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.61` | 17,250,000.00 USD | 17,250,000.00 USD | 3,350.00 USD | 0.00 USD | 960.97 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.62` | 18,670,000.00 USD | 18,670,000.00 USD | 95,090.00 USD | 31,380.00 USD | 21,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.62` | 17,380,000.00 USD | 17,380,000.00 USD | 134,680.00 USD | 0.00 USD | 2,720.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.62` | 203.50 USD | 1,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.63` | 18,670,000.00 USD | 18,670,000.00 USD | 1,040.00 USD | 0.00 USD | 614.32 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.63` | 17,600,000.00 USD | 17,600,000.00 USD | 213,490.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.63` | 990.04 USD | 1,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.64` | 19,080,000.00 USD | 19,080,000.00 USD | 334,190.00 USD | 11,270.00 USD | 63,790.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.64` | 18,120,000.00 USD | 18,120,000.00 USD | 501,930.00 USD | 18,170.00 USD | 1,670.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.64` | 3,950.00 USD | 1,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.65` | 20,150,000.00 USD | 20,150,000.00 USD | 423,550.00 USD | 52,020.00 USD | 600,100.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.65` | 18,540,000.00 USD | 18,540,000.00 USD | 420,940.00 USD | 0.00 USD | 2,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.66` | 8.84 USD | 1,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.66` | 21,130,000.00 USD | 21,130,000.00 USD | 281,290.00 USD | 316,500.00 USD | 379,880.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.66` | 18,860,000.00 USD | 18,860,000.00 USD | 144,860.00 USD | 18,370.00 USD | 150,940.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.67` | 101.70 USD | 1,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.67` | 21,690,000.00 USD | 21,690,000.00 USD | 184,440.00 USD | 0.00 USD | 378,090.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.67` | 18,900,000.00 USD | 18,900,000.00 USD | 0.00 USD | 0.00 USD | 43,230.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.68` | 22,300,000.00 USD | 22,300,000.00 USD | 345,840.00 USD | 81,340.00 USD | 175,700.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.68` | 19,820,000.00 USD | 19,820,000.00 USD | 381,910.00 USD | 83,630.00 USD | 450,700.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.69` | 22,800,000.00 USD | 22,800,000.00 USD | 213,780.00 USD | 40,000.00 USD | 254,150.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.69` | 19,910,000.00 USD | 19,910,000.00 USD | 2,450.00 USD | 0.00 USD | 88,340.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.70` | 230.06 USD | 1,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.70` | 23,140,000.00 USD | 23,140,000.00 USD | 74,090.00 USD | 123,520.00 USD | 143,310.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.70` | 20,220,000.00 USD | 20,220,000.00 USD | 74,240.00 USD | 60,360.00 USD | 181,210.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.71` | 7,480.00 USD | 1,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.71` | 24,100,000.00 USD | 24,100,000.00 USD | 359,510.00 USD | 284,360.00 USD | 316,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.71` | 20,630,000.00 USD | 20,630,000.00 USD | 178,360.00 USD | 232,800.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.71` | 460.18 USD | 1,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `4.72` | 20,820,000.00 USD | 20,820,000.00 USD | 7,140.00 USD | 0.00 USD | 180,490.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.73` | 20,880,000.00 USD | 20,880,000.00 USD | 59,970.00 USD | 0.00 USD | 894.74 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.74` | 21,200,000.00 USD | 21,200,000.00 USD | 14,750.00 USD | 173,100.00 USD | 127,910.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.75` | 21,230.00 USD | 1,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `4.75` | 21,740,000.00 USD | 21,740,000.00 USD | 17,340.00 USD | 185,060.00 USD | 343,810.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.76` | 23,090,000.00 USD | 23,090,000.00 USD | 1,030,000.00 USD | 46,890.00 USD | 272,560.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.76` | 64,260.00 USD | 1,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `4.77` | 24,000,000.00 USD | 24,000,000.00 USD | 731,680.00 USD | 73,410.00 USD | 101,640.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.78` | 8,780.00 USD | 1,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `4.78` | 25,350,000.00 USD | 25,350,000.00 USD | 683,730.00 USD | 513,870.00 USD | 154,510.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.79` | 4,420.00 USD | 1,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `4.79` | 26,380,000.00 USD | 26,380,000.00 USD | 713,060.00 USD | 249,310.00 USD | 72,120.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.79` | 1,330.00 USD | 1,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `4.80` | 27,970,000.00 USD | 27,970,000.00 USD | 1,160,000.00 USD | 432,340.00 USD | 2,480.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.81` | 28,600,000.00 USD | 28,600,000.00 USD | 400,070.00 USD | 125,900.00 USD | 101,780.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.82` | 45,670.00 USD | 1,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `4.82` | 31,370,000.00 USD | 31,370,000.00 USD | 1,010,000.00 USD | 369,430.00 USD | 1,390,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.83` | 3,020.00 USD | 1,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `4.83` | 33,020,000.00 USD | 33,020,000.00 USD | 822,860.00 USD | 85,680.00 USD | 739,630.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.83` | 1,950.00 USD | 1,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `4.84` | 33,510,000.00 USD | 33,510,000.00 USD | 97,300.00 USD | 71,790.00 USD | 322,840.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.84` | 11,220.00 USD | 1,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `4.85` | 35,530,000.00 USD | 35,530,000.00 USD | 487,940.00 USD | 366,970.00 USD | 1,160,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.86` | 36,940,000.00 USD | 36,940,000.00 USD | 444,810.00 USD | 162,380.00 USD | 802,380.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.87` | 1,350.00 USD | 1,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `4.87` | 38,000,000.00 USD | 38,000,000.00 USD | 264,730.00 USD | 136,820.00 USD | 663,430.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.88` | 39,590,000.00 USD | 39,590,000.00 USD | 449,970.00 USD | 340,260.00 USD | 792,630.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.88` | 827.03 USD | 1,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `4.89` | 40,170,000.00 USD | 40,170,000.00 USD | 213,960.00 USD | 100,850.00 USD | 272,060.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.90` | 41,310,000.00 USD | 41,310,000.00 USD | 450,550.00 USD | 145,910.00 USD | 541,330.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.91` | 42,750,000.00 USD | 42,750,000.00 USD | 637,320.00 USD | 208,910.00 USD | 590,510.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.92` | 20,720.00 USD | 1,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `4.92` | 44,480,000.00 USD | 44,480,000.00 USD | 576,460.00 USD | 277,640.00 USD | 877,920.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.92` | 2,100.00 USD | 1,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `4.93` | 46,040,000.00 USD | 46,040,000.00 USD | 730,010.00 USD | 78,190.00 USD | 749,940.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.93` | 157.43 USD | 1,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `4.94` | 47,380,000.00 USD | 47,380,000.00 USD | 351,940.00 USD | 290,290.00 USD | 696,960.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.95` | 48,680,000.00 USD | 48,680,000.00 USD | 468,360.00 USD | 161,040.00 USD | 670,270.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.96` | 342.89 USD | 1,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `4.96` | 49,910,000.00 USD | 49,910,000.00 USD | 607,770.00 USD | 214,910.00 USD | 410,880.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.97` | 50,290,000.00 USD | 50,290,000.00 USD | 198,220.00 USD | 72,330.00 USD | 113,320.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.97` | 99,810.00 USD | 1,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `4.98` | 50,950,000.00 USD | 50,950,000.00 USD | 251,840.00 USD | 102,410.00 USD | 299,870.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.99` | 611.16 USD | 1,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `4.99` | 51,300,000.00 USD | 51,300,000.00 USD | 133,330.00 USD | 103,060.00 USD | 117,980.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `5.00` | 339.66 USD | 1,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `5.00` | 52,000,000.00 USD | 52,000,000.00 USD | 210,680.00 USD | 36,180.00 USD | 454,070.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `5.01` | 53,830,000.00 USD | 53,830,000.00 USD | 781,840.00 USD | 255,770.00 USD | 786,470.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `5.02` | 55,280,000.00 USD | 55,280,000.00 USD | 821,860.00 USD | 309,020.00 USD | 321,920.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `5.03` | 56,410,000.00 USD | 56,410,000.00 USD | 385,330.00 USD | 172,880.00 USD | 567,890.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `5.04` | 57,490,000.00 USD | 57,490,000.00 USD | 305,260.00 USD | 163,190.00 USD | 619,980.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `5.05` | 58,940,000.00 USD | 58,940,000.00 USD | 694,310.00 USD | 267,140.00 USD | 486,680.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `5.06` | 59,620,000.00 USD | 59,620,000.00 USD | 92,480.00 USD | 165,230.00 USD | 420,210.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `5.07` | 3,420.00 USD | 1,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `5.07` | 60,660,000.00 USD | 60,660,000.00 USD | 358,750.00 USD | 137,080.00 USD | 542,550.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `5.08` | 61,180,000.00 USD | 61,180,000.00 USD | 204,140.00 USD | 167,810.00 USD | 150,010.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `5.08` | 2,720.00 USD | 1,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `5.09` | 61,720,000.00 USD | 61,720,000.00 USD | 105,390.00 USD | 52,790.00 USD | 385,540.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `5.10` | 62,110,000.00 USD | 62,110,000.00 USD | 182,200.00 USD | 0.00 USD | 201,110.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `5.11` | 62,700,000.00 USD | 62,700,000.00 USD | 369,260.00 USD | 78,100.00 USD | 140,600.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `5.12` | 63,270,000.00 USD | 63,270,000.00 USD | 303,840.00 USD | 152,530.00 USD | 115,650.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `5.12` | 2,560.00 USD | 1,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `5.13` | 63,840,000.00 USD | 63,840,000.00 USD | 173,190.00 USD | 71,310.00 USD | 325,090.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `5.14` | 64,280,000.00 USD | 64,280,000.00 USD | 140,950.00 USD | 59,640.00 USD | 239,260.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `5.14` | 20,690.00 USD | 1,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `5.15` | 64,830,000.00 USD | 64,830,000.00 USD | 205,680.00 USD | 82,350.00 USD | 267,910.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `5.16` | 65,350,000.00 USD | 65,350,000.00 USD | 51,850.00 USD | 112,830.00 USD | 347,470.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `5.17` | 751.51 USD | 1,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `5.17` | 65,960,000.00 USD | 65,960,000.00 USD | 280,710.00 USD | 85,040.00 USD | 244,330.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `5.18` | 66,210,000.00 USD | 66,210,000.00 USD | 67,600.00 USD | 63,250.00 USD | 124,260.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `5.19` | 66,430,000.00 USD | 66,430,000.00 USD | 69,310.00 USD | 13,680.00 USD | 138,850.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `5.20` | 7,280.00 USD | 1,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `5.20` | 66,680,000.00 USD | 66,680,000.00 USD | 137,830.00 USD | 45,820.00 USD | 65,990.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `5.21` | 66,920,000.00 USD | 66,920,000.00 USD | 105,330.00 USD | 20,850.00 USD | 110,400.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `5.22` | 66,980,000.00 USD | 66,980,000.00 USD | 48,760.00 USD | 13,410.00 USD | 398.26 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `5.22` | 72,110.00 USD | 1,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `5.23` | 67,040,000.00 USD | 67,040,000.00 USD | 5,060.00 USD | 15,520.00 USD | 34,400.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `5.25` | 2,770.00 USD | 1,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.25` | 1,050,000.00 USD | 2,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.26` | 5,610.00 USD | 2,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.29` | 134.77 USD | 2,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.30` | 524.66 USD | 2,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.32` | 718.59 USD | 2,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.36` | 43,340.00 USD | 2,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.38` | 620.89 USD | 2,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.41` | 5,410.00 USD | 2,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.43` | 20,870.00 USD | 2,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.46` | 104,530.00 USD | 2,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.46` | 1,370.00 USD | 2,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.47` | 627.98 USD | 2,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.50` | 66,470.00 USD | 2,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.51` | 38,800.00 USD | 2,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.53` | 712.73 USD | 2,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.54` | 26,740.00 USD | 2,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.55` | 3,720.00 USD | 2,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.57` | 8,670.00 USD | 2,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.58` | 62,420.00 USD | 2,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.59` | 56,640.00 USD | 2,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.61` | 89,690.00 USD | 3,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.63` | 63,090.00 USD | 3,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.67` | 303,310.00 USD | 3,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.67` | 228.70 USD | 3,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.68` | 26,090.00 USD | 3,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.70` | 1,520.00 USD | 3,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.71` | 2,130.00 USD | 3,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.72` | 169.46 USD | 3,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.75` | 1,670,000.00 USD | 5,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.75` | 286.02 USD | 5,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.79` | 132,520.00 USD | 5,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.80` | 2,670.00 USD | 5,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.82` | 127.93 USD | 5,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.83` | 337,490.00 USD | 5,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.84` | 310.95 USD | 5,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.86` | 848.39 USD | 5,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.88` | 200.34 USD | 5,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.88` | 7,150.00 USD | 5,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.89` | 88,590.00 USD | 5,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.92` | 189.28 USD | 5,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.95` | 103,650.00 USD | 5,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.00` | 154.07 USD | 5,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.03` | 23,060.00 USD | 5,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.07` | 740.54 USD | 5,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.08` | 5,920.00 USD | 5,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.09` | 37,510.00 USD | 5,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.12` | 1,870.00 USD | 5,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.12` | 5,220.00 USD | 5,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.13` | 2,430.00 USD | 5,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.21` | 46,080.00 USD | 5,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.25` | 31,550.00 USD | 5,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.25` | 439.10 USD | 5,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.28` | 397.84 USD | 5,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.29` | 291,020.00 USD | 6,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.32` | 1,200.00 USD | 6,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.33` | 382.00 USD | 6,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.34` | 214.46 USD | 6,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.37` | 113.93 USD | 6,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.38` | 1,460.00 USD | 6,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.39` | 2,000.00 USD | 6,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.41` | 55,840.00 USD | 6,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.42` | 8,700.00 USD | 6,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.42` | 346.95 USD | 6,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.45` | 5,270.00 USD | 6,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.46` | 9,270.00 USD | 6,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.46` | 1,940.00 USD | 6,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.51` | 380.48 USD | 6,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.54` | 14,180.00 USD | 6,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.54` | 265.07 USD | 6,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.58` | 87,890.00 USD | 6,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.58` | 698.67 USD | 6,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.59` | 418.78 USD | 6,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.61` | 2,050.00 USD | 6,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.66` | 7,230.00 USD | 6,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.67` | 233.94 USD | 6,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.67` | 200.25 USD | 6,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.75` | 1,250,000.00 USD | 7,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.78` | 41,940.00 USD | 7,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.79` | 37,480.00 USD | 7,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.84` | 872.05 USD | 7,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.87` | 2,650.00 USD | 7,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.88` | 187.69 USD | 7,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.92` | 6,920.00 USD | 7,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.95` | 190.99 USD | 7,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.96` | 171.09 USD | 7,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.97` | 69,750.00 USD | 7,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.99` | 664.27 USD | 7,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.08` | 28,590,000.00 USD | 36,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.09` | 699.57 USD | 36,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.12` | 9,860.00 USD | 36,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.18` | 1,350,000.00 USD | 37,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.21` | 13,560.00 USD | 37,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.24` | 4,910.00 USD | 37,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.25` | 10,990.00 USD | 37,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.32` | 5,810.00 USD | 37,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.33` | 1,320.00 USD | 37,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.37` | 181.18 USD | 37,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.38` | 26,920.00 USD | 37,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.42` | 106,000.00 USD | 38,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.45` | 271,800.00 USD | 38,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.46` | 7,050.00 USD | 38,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.47` | 221.26 USD | 38,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.50` | 2,610.00 USD | 38,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.53` | 1,570.00 USD | 38,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.54` | 789.67 USD | 38,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.57` | 7,860,000.00 USD | 46,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.58` | 10,120,000.00 USD | 56,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.63` | 19,210.00 USD | 56,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.66` | 13,400.00 USD | 56,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.67` | 27,160.00 USD | 56,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.72` | 259.56 USD | 56,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.74` | 505.87 USD | 56,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.75` | 629.67 USD | 56,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.75` | 33,410.00 USD | 56,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.79` | 997,350.00 USD | 57,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.80` | 231.03 USD | 57,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.87` | 334,500.00 USD | 57,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.92` | 2,310.00 USD | 57,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.95` | 6,120.00 USD | 57,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.96` | 140,310.00 USD | 57,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.99` | 4,240,000.00 USD | 62,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `0.8050` | 20,520,000.00 USD | 0.00 USD | 3,890.00 USD | `-79.87%` | `4,835.70` |
| `Live` | `Long` | `0.8150` | 20,510,000.00 USD | 0.00 USD | 475.39 USD | `-79.62%` | `583.30` |
| `Live` | `Long` | `0.8250` | 20,510,000.00 USD | 0.00 USD | 241.06 USD | `-79.37%` | `292.20` |
| `Live` | `Long` | `0.8450` | 20,510,000.00 USD | 0.00 USD | 3,630.00 USD | `-78.87%` | `4,298.30` |
| `Live` | `Long` | `0.8550` | 20,510,000.00 USD | 0.00 USD | 24,980.00 USD | `-78.62%` | `29,219.30` |
| `Live` | `Long` | `0.8650` | 20,480,000.00 USD | 0.00 USD | 9,770.00 USD | `-78.37%` | `11,295.30` |
| `Live` | `Long` | `0.8750` | 20,470,000.00 USD | 0.00 USD | 5,190.00 USD | `-78.12%` | `5,926.50` |
| `Live` | `Long` | `0.8950` | 20,470,000.00 USD | 0.00 USD | 39,460.00 USD | `-77.62%` | `44,089.80` |
| `Live` | `Long` | `0.9050` | 20,430,000.00 USD | 0.00 USD | 292.22 USD | `-77.37%` | `322.90` |
| `Live` | `Long` | `0.9150` | 20,430,000.00 USD | 0.00 USD | 19,030.00 USD | `-77.12%` | `20,793.60` |
| `Live` | `Long` | `0.9250` | 20,410,000.00 USD | 0.00 USD | 207.75 USD | `-76.87%` | `224.60` |
| `Live` | `Long` | `0.9450` | 20,410,000.00 USD | 0.00 USD | 4,290.00 USD | `-76.37%` | `4,536.70` |
| `Live` | `Long` | `0.9650` | 20,400,000.00 USD | 0.00 USD | 6,260.00 USD | `-75.87%` | `6,483.50` |
| `Live` | `Long` | `0.9750` | 20,400,000.00 USD | 0.00 USD | 169.55 USD | `-75.62%` | `173.90` |
| `Live` | `Long` | `0.9850` | 20,400,000.00 USD | 0.00 USD | 404,290.00 USD | `-75.37%` | `410,445.10` |
| `Live` | `Long` | `0.9950` | 19,990,000.00 USD | 0.00 USD | 501,040.00 USD | `-75.12%` | `503,557.30` |
| `Live` | `Long` | `1.01` | 19,490,000.00 USD | 0.00 USD | 2,850.00 USD | `-74.62%` | `2,804.20` |
| `Live` | `Long` | `1.02` | 19,490,000.00 USD | 0.00 USD | 10,250.00 USD | `-74.37%` | `10,000.00` |
| `Live` | `Long` | `1.03` | 19,480,000.00 USD | 0.00 USD | 5,070.00 USD | `-74.12%` | `4,897.40` |
| `Live` | `Long` | `1.04` | 19,470,000.00 USD | 0.00 USD | 2,740.00 USD | `-73.87%` | `2,617.40` |
| `Live` | `Long` | `1.05` | 19,470,000.00 USD | 0.00 USD | 4,330.00 USD | `-73.62%` | `4,108.90` |
| `Live` | `Long` | `1.06` | 19,470,000.00 USD | 0.00 USD | 892.90 USD | `-73.37%` | `838.40` |
| `Live` | `Long` | `1.07` | 19,470,000.00 USD | 0.00 USD | 51,410.00 USD | `-73.12%` | `47,826.50` |
| `Live` | `Long` | `1.08` | 19,420,000.00 USD | 0.00 USD | 216.89 USD | `-72.87%` | `199.90` |
| `Live` | `Long` | `1.11` | 19,410,000.00 USD | 0.00 USD | 4,180.00 USD | `-72.12%` | `3,751.60` |
| `Live` | `Long` | `1.12` | 19,410,000.00 USD | 0.00 USD | 1,670.00 USD | `-71.87%` | `1,480.20` |
| `Live` | `Long` | `1.14` | 19,410,000.00 USD | 0.00 USD | 4,960.00 USD | `-71.62%` | `4,368.60` |
| `Live` | `Long` | `1.15` | 19,400,000.00 USD | 0.00 USD | 26,620.00 USD | `-71.37%` | `23,252.70` |
| `Live` | `Long` | `1.16` | 19,380,000.00 USD | 0.00 USD | 17,080.00 USD | `-71.12%` | `14,783.90` |
| `Live` | `Long` | `1.17` | 19,360,000.00 USD | 0.00 USD | 3,530.00 USD | `-70.87%` | `3,031.40` |
| `Live` | `Long` | `1.18` | 19,360,000.00 USD | 0.00 USD | 2,620.00 USD | `-70.62%` | `2,225.90` |
| `Live` | `Long` | `1.22` | 19,350,000.00 USD | 0.00 USD | 17,150.00 USD | `-69.62%` | `14,117.50` |
| `Live` | `Long` | `1.25` | 19,340,000.00 USD | 0.00 USD | 23,260.00 USD | `-68.62%` | `18,535.00` |
| `Live` | `Long` | `1.26` | 19,310,000.00 USD | 0.00 USD | 2,630.00 USD | `-68.37%` | `2,079.10` |
| `Live` | `Long` | `1.27` | 19,310,000.00 USD | 0.00 USD | 2,710.00 USD | `-68.12%` | `2,127.70` |
| `Live` | `Long` | `1.28` | 19,310,000.00 USD | 0.00 USD | 169.23 USD | `-67.87%` | `131.70` |
| `Live` | `Long` | `1.30` | 19,310,000.00 USD | 0.00 USD | 116.80 USD | `-67.37%` | `89.50` |
| `Live` | `Long` | `1.32` | 19,310,000.00 USD | 0.00 USD | 3,270.00 USD | `-66.87%` | `2,467.20` |
| `Live` | `Long` | `1.33` | 19,300,000.00 USD | 0.00 USD | 3,200.00 USD | `-66.62%` | `2,395.50` |
| `Live` | `Long` | `1.34` | 19,300,000.00 USD | 0.00 USD | 1,740.00 USD | `-66.37%` | `1,296.00` |
| `Live` | `Long` | `1.35` | 19,300,000.00 USD | 0.00 USD | 2,000.00 USD | `-66.12%` | `1,474.80` |
| `Live` | `Long` | `1.38` | 19,300,000.00 USD | 0.00 USD | 12,380.00 USD | `-65.62%` | `9,000.00` |
| `Live` | `Long` | `1.39` | 19,290,000.00 USD | 0.00 USD | 491.54 USD | `-65.37%` | `354.90` |
| `Live` | `Long` | `1.40` | 19,290,000.00 USD | 0.00 USD | 931.86 USD | `-65.12%` | `668.00` |
| `Live` | `Long` | `1.42` | 19,280,000.00 USD | 0.00 USD | 17,680.00 USD | `-64.62%` | `12,495.30` |
| `Live` | `Long` | `1.43` | 19,270,000.00 USD | 0.00 USD | 997.50 USD | `-64.37%` | `700.00` |
| `Live` | `Long` | `1.44` | 19,270,000.00 USD | 0.00 USD | 1,260.00 USD | `-64.12%` | `877.60` |
| `Live` | `Long` | `1.45` | 19,260,000.00 USD | 0.00 USD | 1,530.00 USD | `-63.87%` | `1,061.70` |
| `Live` | `Long` | `1.47` | 19,260,000.00 USD | 0.00 USD | 28,560.00 USD | `-63.37%` | `19,497.20` |
| `Live` | `Long` | `1.48` | 19,230,000.00 USD | 0.00 USD | 14,750.00 USD | `-63.12%` | `10,000.00` |
| `Live` | `Long` | `1.50` | 19,220,000.00 USD | 0.00 USD | 3,190.00 USD | `-62.62%` | `2,134.40` |
| `Live` | `Long` | `1.50` | 19,220,000.00 USD | 0.00 USD | 376.40 USD | `-62.37%` | `250.10` |
| `Live` | `Long` | `1.51` | 19,220,000.00 USD | 0.00 USD | 899.00 USD | `-62.12%` | `593.40` |
| `Live` | `Long` | `1.52` | 19,210,000.00 USD | 0.00 USD | 3,200.00 USD | `-61.87%` | `2,096.20` |
| `Live` | `Long` | `1.53` | 19,210,000.00 USD | 0.00 USD | 279.37 USD | `-61.62%` | `182.00` |
| `Live` | `Long` | `1.55` | 19,210,000.00 USD | 0.00 USD | 75,170.00 USD | `-61.12%` | `48,340.90` |
| `Live` | `Long` | `1.56` | 19,140,000.00 USD | 0.00 USD | 20,570.00 USD | `-60.87%` | `13,146.30` |
| `Live` | `Long` | `1.57` | 19,120,000.00 USD | 0.00 USD | 589.52 USD | `-60.62%` | `374.30` |
| `Live` | `Long` | `1.58` | 19,120,000.00 USD | 0.00 USD | 3,870.00 USD | `-60.37%` | `2,441.50` |
| `Live` | `Long` | `1.59` | 19,110,000.00 USD | 0.00 USD | 3,700.00 USD | `-60.12%` | `2,319.70` |
| `Live` | `Long` | `1.60` | 19,110,000.00 USD | 0.00 USD | 2,440.00 USD | `-59.87%` | `1,520.90` |
| `Live` | `Long` | `1.62` | 19,110,000.00 USD | 0.00 USD | 1,480.00 USD | `-59.37%` | `912.40` |
| `Live` | `Long` | `1.64` | 19,100,000.00 USD | 0.00 USD | 2,530.00 USD | `-59.12%` | `1,550.30` |
| `Live` | `Long` | `1.65` | 19,100,000.00 USD | 0.00 USD | 981.08 USD | `-58.87%` | `596.40` |
| `Live` | `Long` | `1.66` | 19,100,000.00 USD | 0.00 USD | 959.57 USD | `-58.62%` | `579.80` |
| `Live` | `Long` | `1.67` | 19,100,000.00 USD | 0.00 USD | 1,300.00 USD | `-58.37%` | `783.20` |
| `Live` | `Long` | `1.68` | 19,100,000.00 USD | 0.00 USD | 84,620.00 USD | `-58.12%` | `50,519.70` |
| `Live` | `Long` | `1.69` | 19,010,000.00 USD | 0.00 USD | 167,100.00 USD | `-57.87%` | `99,167.90` |
| `Live` | `Long` | `1.71` | 18,850,000.00 USD | 0.00 USD | 6,020.00 USD | `-57.37%` | `3,529.90` |
| `Live` | `Long` | `1.73` | 18,840,000.00 USD | 0.00 USD | 6,060.00 USD | `-56.87%` | `3,514.50` |
| `Live` | `Long` | `1.74` | 18,830,000.00 USD | 0.00 USD | 1,710.00 USD | `-56.62%` | `983.40` |
| `Live` | `Long` | `1.75` | 18,830,000.00 USD | 0.00 USD | 6,580.00 USD | `-56.37%` | `3,773.50` |
| `Live` | `Long` | `1.75` | 18,830,000.00 USD | 0.00 USD | 10,930.00 USD | `-56.12%` | `6,230.20` |
| `Live` | `Long` | `1.77` | 18,810,000.00 USD | 0.00 USD | 3,470.00 USD | `-55.62%` | `1,953.10` |
| `Live` | `Long` | `1.78` | 18,810,000.00 USD | 0.00 USD | 53,180.00 USD | `-55.37%` | `29,790.70` |
| `Live` | `Long` | `1.80` | 18,760,000.00 USD | 0.00 USD | 529.05 USD | `-54.87%` | `293.10` |
| `Live` | `Long` | `1.81` | 18,760,000.00 USD | 0.00 USD | 2,960.00 USD | `-54.62%` | `1,631.80` |
| `Live` | `Long` | `1.82` | 18,750,000.00 USD | 0.00 USD | 2,330.00 USD | `-54.37%` | `1,276.50` |
| `Live` | `Long` | `1.83` | 18,750,000.00 USD | 0.00 USD | 27,520.00 USD | `-54.12%` | `15,000.00` |
| `Live` | `Long` | `1.84` | 18,720,000.00 USD | 0.00 USD | 15,410.00 USD | `-53.87%` | `8,350.30` |
| `Live` | `Long` | `1.85` | 18,710,000.00 USD | 0.00 USD | 650,230.00 USD | `-53.62%` | `350,530.60` |
| `Live` | `Long` | `1.88` | 18,060,000.00 USD | 0.00 USD | 5,540.00 USD | `-53.12%` | `2,953.60` |
| `Live` | `Long` | `1.89` | 18,050,000.00 USD | 0.00 USD | 2,770.00 USD | `-52.87%` | `1,470.30` |
| `Live` | `Long` | `1.90` | 18,050,000.00 USD | 0.00 USD | 2,080.00 USD | `-52.62%` | `1,100.00` |
| `Live` | `Long` | `1.91` | 18,050,000.00 USD | 0.00 USD | 379.10 USD | `-52.37%` | `199.00` |
| `Live` | `Long` | `1.92` | 18,050,000.00 USD | 0.00 USD | 638,570.00 USD | `-52.12%` | `333,456.50` |
| `Live` | `Long` | `1.93` | 17,410,000.00 USD | 0.00 USD | 1,870.00 USD | `-51.87%` | `971.20` |
| `Live` | `Long` | `1.94` | 17,410,000.00 USD | 0.00 USD | 191.76 USD | `-51.62%` | `99.10` |
| `Live` | `Long` | `1.95` | 17,410,000.00 USD | 0.00 USD | 17,600.00 USD | `-51.37%` | `9,047.30` |
| `Live` | `Long` | `1.96` | 17,390,000.00 USD | 0.00 USD | 775.55 USD | `-51.12%` | `396.70` |
| `Live` | `Long` | `1.97` | 17,390,000.00 USD | 0.00 USD | 1,590.00 USD | `-50.87%` | `810.90` |
| `Live` | `Long` | `1.98` | 17,390,000.00 USD | 0.00 USD | 34,950.00 USD | `-50.62%` | `17,697.20` |
| `Live` | `Long` | `2.00` | 17,350,000.00 USD | 0.00 USD | 149.62 USD | `-50.12%` | `75.00` |
| `Live` | `Long` | `2.00` | 17,350,000.00 USD | 0.00 USD | 2,000.00 USD | `-49.87%` | `995.20` |
| `Live` | `Long` | `2.02` | 17,350,000.00 USD | 0.00 USD | 260.62 USD | `-49.37%` | `128.70` |
| `Live` | `Long` | `2.04` | 17,350,000.00 USD | 0.00 USD | 4,480.00 USD | `-48.87%` | `2,192.50` |
| `Live` | `Long` | `2.06` | 17,350,000.00 USD | 0.00 USD | 15,900.00 USD | `-48.62%` | `7,737.90` |
| `Live` | `Long` | `2.06` | 17,330,000.00 USD | 0.00 USD | 13,280.00 USD | `-48.37%` | `6,429.20` |
| `Live` | `Long` | `2.08` | 17,320,000.00 USD | 0.00 USD | 17,140.00 USD | `-48.12%` | `8,260.40` |
| `Live` | `Long` | `2.08` | 17,300,000.00 USD | 0.00 USD | 22,770.00 USD | `-47.87%` | `10,920.10` |
| `Live` | `Long` | `2.10` | 17,280,000.00 USD | 0.00 USD | 1,100.00 USD | `-47.62%` | `527.40` |
| `Live` | `Long` | `2.10` | 17,280,000.00 USD | 0.00 USD | 32,000.00 USD | `-47.37%` | `15,200.00` |
| `Live` | `Long` | `2.12` | 17,240,000.00 USD | 0.00 USD | 31,860.00 USD | `-47.12%` | `15,064.10` |
| `Live` | `Long` | `2.12` | 17,210,000.00 USD | 0.00 USD | 33,610.00 USD | `-46.87%` | `15,817.30` |
| `Live` | `Long` | `2.15` | 17,180,000.00 USD | 0.00 USD | 594.13 USD | `-46.12%` | `275.70` |
| `Live` | `Long` | `2.17` | 17,180,000.00 USD | 0.00 USD | 188,590.00 USD | `-45.87%` | `87,108.00` |
| `Live` | `Long` | `2.17` | 16,990,000.00 USD | 0.00 USD | 292.32 USD | `-45.62%` | `134.40` |
| `Live` | `Long` | `2.19` | 16,990,000.00 USD | 0.00 USD | 15,490.00 USD | `-45.37%` | `7,090.30` |
| `Live` | `Long` | `2.19` | 16,970,000.00 USD | 0.00 USD | 10,380.00 USD | `-45.12%` | `4,730.10` |
| `Live` | `Long` | `2.21` | 16,960,000.00 USD | 0.00 USD | 125,520.00 USD | `-44.87%` | `56,923.70` |
| `Live` | `Long` | `2.21` | 16,840,000.00 USD | 0.00 USD | 1,200.00 USD | `-44.62%` | `542.90` |
| `Live` | `Long` | `2.23` | 16,840,000.00 USD | 0.00 USD | 243.19 USD | `-44.37%` | `109.30` |
| `Live` | `Long` | `2.23` | 16,840,000.00 USD | 0.00 USD | 4,190.00 USD | `-44.12%` | `1,875.00` |
| `Live` | `Long` | `2.25` | 16,830,000.00 USD | 0.00 USD | 38,060.00 USD | `-43.87%` | `16,955.00` |
| `Live` | `Long` | `2.25` | 16,790,000.00 USD | 0.00 USD | 117,220.00 USD | `-43.62%` | `51,980.50` |
| `Live` | `Long` | `2.27` | 16,680,000.00 USD | 0.00 USD | 379,560.00 USD | `-43.12%` | `166,841.40` |
| `Live` | `Long` | `2.29` | 16,300,000.00 USD | 0.00 USD | 463.86 USD | `-42.87%` | `203.00` |
| `Live` | `Long` | `2.29` | 16,300,000.00 USD | 0.00 USD | 2,670.00 USD | `-42.62%` | `1,161.30` |
| `Live` | `Long` | `2.31` | 16,290,000.00 USD | 0.00 USD | 16,340.00 USD | `-42.37%` | `7,089.10` |
| `Live` | `Long` | `2.31` | 16,280,000.00 USD | 0.00 USD | 3,700.00 USD | `-42.12%` | `1,599.40` |
| `Live` | `Long` | `2.33` | 16,270,000.00 USD | 0.00 USD | 4,780.00 USD | `-41.62%` | `2,045.40` |
| `Live` | `Long` | `2.35` | 16,270,000.00 USD | 0.00 USD | 32,860.00 USD | `-41.37%` | `14,014.40` |
| `Live` | `Long` | `2.35` | 16,240,000.00 USD | 0.00 USD | 223.72 USD | `-41.12%` | `95.00` |
| `Live` | `Long` | `2.37` | 16,240,000.00 USD | 0.00 USD | 3,080.00 USD | `-40.87%` | `1,302.60` |
| `Live` | `Long` | `2.38` | 16,230,000.00 USD | 0.00 USD | 549,210.00 USD | `-40.62%` | `231,244.40` |
| `Live` | `Long` | `2.38` | 15,680,000.00 USD | 0.00 USD | 5,860.00 USD | `-40.37%` | `2,457.90` |
| `Live` | `Long` | `2.40` | 15,680,000.00 USD | 0.00 USD | 973.57 USD | `-40.12%` | `406.50` |
| `Live` | `Long` | `2.40` | 15,680,000.00 USD | 0.00 USD | 2,900.00 USD | `-39.87%` | `1,207.50` |
| `Live` | `Long` | `2.42` | 15,670,000.00 USD | 0.00 USD | 222,950.00 USD | `-39.62%` | `92,318.80` |
| `Live` | `Long` | `2.42` | 15,450,000.00 USD | 0.00 USD | 273,210.00 USD | `-39.37%` | `112,662.00` |
| `Live` | `Long` | `2.44` | 15,180,000.00 USD | 0.00 USD | 1,590,000.00 USD | `-39.12%` | `653,660.50` |
| `Live` | `Long` | `2.44` | 13,590,000.00 USD | 0.00 USD | 502,760.00 USD | `-38.87%` | `205,629.50` |
| `Live` | `Long` | `2.46` | 13,080,000.00 USD | 0.00 USD | 1,240.00 USD | `-38.62%` | `504.90` |
| `Live` | `Long` | `2.46` | 13,080,000.00 USD | 0.00 USD | 5,860.00 USD | `-38.37%` | `2,378.60` |
| `Live` | `Long` | `2.48` | 13,080,000.00 USD | 0.00 USD | 11,920.00 USD | `-38.12%` | `4,815.90` |
| `Live` | `Long` | `2.48` | 13,060,000.00 USD | 0.00 USD | 5,990.00 USD | `-37.87%` | `2,409.50` |
| `Live` | `Long` | `2.50` | 13,060,000.00 USD | 0.00 USD | 3,430.00 USD | `-37.62%` | `1,375.10` |
| `Live` | `Long` | `2.50` | 13,050,000.00 USD | 0.00 USD | 6,000.00 USD | `-37.37%` | `2,395.50` |
| `Live` | `Long` | `2.52` | 13,050,000.00 USD | 0.00 USD | 30,430.00 USD | `-36.87%` | `12,050.90` |
| `Live` | `Long` | `2.54` | 13,020,000.00 USD | 0.00 USD | 32,040.00 USD | `-36.62%` | `12,639.80` |
| `Live` | `Long` | `2.54` | 12,990,000.00 USD | 0.00 USD | 315,780.00 USD | `-36.37%` | `124,076.70` |
| `Live` | `Long` | `2.56` | 12,670,000.00 USD | 0.00 USD | 16,660.00 USD | `-36.12%` | `6,519.80` |
| `Live` | `Long` | `2.56` | 12,650,000.00 USD | 0.00 USD | 22,340.00 USD | `-35.87%` | `8,710.90` |
| `Live` | `Long` | `2.58` | 12,630,000.00 USD | 0.00 USD | 1,260.00 USD | `-35.62%` | `490.00` |
| `Live` | `Long` | `2.58` | 12,630,000.00 USD | 0.00 USD | 18,280.00 USD | `-35.37%` | `7,071.20` |
| `Live` | `Long` | `2.60` | 12,610,000.00 USD | 0.00 USD | 84,460.00 USD | `-35.12%` | `32,548.40` |
| `Live` | `Long` | `2.62` | 12,530,000.00 USD | 0.00 USD | 30,860.00 USD | `-34.62%` | `11,801.70` |
| `Live` | `Long` | `2.62` | 12,500,000.00 USD | 0.00 USD | 342,060.00 USD | `-34.37%` | `130,308.00` |
| `Live` | `Long` | `2.63` | 12,150,000.00 USD | 0.00 USD | 24,670.00 USD | `-34.12%` | `9,362.70` |
| `Live` | `Long` | `2.65` | 12,130,000.00 USD | 0.00 USD | 5,790.00 USD | `-33.87%` | `2,190.00` |
| `Live` | `Long` | `2.65` | 12,120,000.00 USD | 0.00 USD | 18,200.00 USD | `-33.62%` | `6,856.80` |
| `Live` | `Long` | `2.67` | 12,110,000.00 USD | 0.00 USD | 5,770.00 USD | `-33.12%` | `2,157.10` |
| `Live` | `Long` | `2.69` | 12,100,000.00 USD | 0.00 USD | 11,520.00 USD | `-32.87%` | `4,291.10` |
| `Live` | `Long` | `2.69` | 12,090,000.00 USD | 0.00 USD | 13,090.00 USD | `-32.62%` | `4,858.30` |
| `Live` | `Long` | `2.71` | 12,080,000.00 USD | 0.00 USD | 133,390.00 USD | `-32.37%` | `49,310.70` |
| `Live` | `Long` | `2.71` | 11,940,000.00 USD | 0.00 USD | 12,630.00 USD | `-32.12%` | `4,653.70` |
| `Live` | `Long` | `2.73` | 11,930,000.00 USD | 0.00 USD | 27,780.00 USD | `-31.87%` | `10,194.90` |
| `Live` | `Long` | `2.73` | 11,900,000.00 USD | 0.00 USD | 9,400.00 USD | `-31.62%` | `3,435.70` |
| `Live` | `Long` | `2.75` | 11,890,000.00 USD | 0.00 USD | 39,550.00 USD | `-31.37%` | `14,408.60` |
| `Live` | `Long` | `2.75` | 11,850,000.00 USD | 0.00 USD | 25,260.00 USD | `-31.12%` | `9,167.40` |
| `Live` | `Long` | `2.77` | 11,830,000.00 USD | 0.00 USD | 349,840.00 USD | `-30.87%` | `126,526.20` |
| `Live` | `Long` | `2.77` | 11,480,000.00 USD | 0.00 USD | 2,550.00 USD | `-30.62%` | `917.60` |
| `Live` | `Long` | `2.79` | 11,480,000.00 USD | 0.00 USD | 53,120.00 USD | `-30.37%` | `19,075.40` |
| `Live` | `Long` | `2.79` | 11,420,000.00 USD | 0.00 USD | 25,870.00 USD | `-30.12%` | `9,257.20` |
| `Live` | `Long` | `2.81` | 11,400,000.00 USD | 0.00 USD | 94,190.00 USD | `-29.87%` | `33,580.40` |
| `Live` | `Long` | `2.81` | 11,300,000.00 USD | 0.00 USD | 4,390.00 USD | `-29.61%` | `1,559.90` |
| `Live` | `Long` | `2.83` | 11,300,000.00 USD | 0.00 USD | 2,550.00 USD | `-29.36%` | `901.60` |
| `Live` | `Long` | `2.83` | 11,300,000.00 USD | 0.00 USD | 6,710.00 USD | `-29.11%` | `2,366.40` |
| `Live` | `Long` | `2.85` | 11,290,000.00 USD | 0.00 USD | 43,920.00 USD | `-28.86%` | `15,436.90` |
| `Live` | `Long` | `2.85` | 11,240,000.00 USD | 0.00 USD | 1,860.00 USD | `-28.61%` | `652.60` |
| `Live` | `Long` | `2.87` | 11,240,000.00 USD | 0.00 USD | 8,690.00 USD | `-28.36%` | `3,034.00` |
| `Live` | `Long` | `2.88` | 11,230,000.00 USD | 0.00 USD | 393,880.00 USD | `-28.11%` | `137,003.40` |
| `Live` | `Long` | `2.88` | 10,840,000.00 USD | 0.00 USD | 6,700.00 USD | `-27.86%` | `2,321.10` |
| `Live` | `Long` | `2.90` | 10,830,000.00 USD | 0.00 USD | 27,100.00 USD | `-27.61%` | `9,360.40` |
| `Live` | `Long` | `2.90` | 10,810,000.00 USD | 0.00 USD | 98,690.00 USD | `-27.36%` | `33,972.30` |
| `Live` | `Long` | `2.92` | 10,710,000.00 USD | 0.00 USD | 82,550.00 USD | `-27.11%` | `28,320.00` |
| `Live` | `Long` | `2.92` | 10,620,000.00 USD | 0.00 USD | 50,340.00 USD | `-26.86%` | `17,211.40` |
| `Live` | `Long` | `2.94` | 10,570,000.00 USD | 0.00 USD | 67,450.00 USD | `-26.61%` | `22,981.80` |
| `Live` | `Long` | `2.94` | 10,510,000.00 USD | 0.00 USD | 20,210.00 USD | `-26.36%` | `6,862.70` |
| `Live` | `Long` | `2.96` | 10,490,000.00 USD | 0.00 USD | 1,470.00 USD | `-26.11%` | `497.80` |
| `Live` | `Long` | `2.96` | 10,490,000.00 USD | 0.00 USD | 1,480.00 USD | `-25.86%` | `499.90` |
| `Live` | `Long` | `2.98` | 10,480,000.00 USD | 0.00 USD | 40,970.00 USD | `-25.61%` | `13,772.00` |
| `Live` | `Long` | `2.98` | 10,440,000.00 USD | 0.00 USD | 8,710.00 USD | `-25.36%` | `2,917.90` |
| `Live` | `Long` | `3.00` | 10,430,000.00 USD | 0.00 USD | 2,330.00 USD | `-25.11%` | `777.40` |
| `Live` | `Long` | `3.00` | 10,430,000.00 USD | 0.00 USD | 10,410.00 USD | `-24.86%` | `3,463.30` |
| `Live` | `Long` | `3.02` | 10,420,000.00 USD | 0.00 USD | 22,260.00 USD | `-24.61%` | `7,383.80` |
| `Live` | `Long` | `3.02` | 10,400,000.00 USD | 0.00 USD | 20,250.00 USD | `-24.36%` | `6,694.10` |
| `Live` | `Long` | `3.04` | 10,380,000.00 USD | 0.00 USD | 1,020.00 USD | `-24.11%` | `335.50` |
| `Live` | `Long` | `3.04` | 10,380,000.00 USD | 0.00 USD | 173,780.00 USD | `-23.86%` | `57,069.50` |
| `Live` | `Long` | `3.06` | 10,200,000.00 USD | 0.00 USD | 26,410.00 USD | `-23.61%` | `8,643.90` |
| `Live` | `Long` | `3.06` | 10,180,000.00 USD | 0.00 USD | 129,700.00 USD | `-23.36%` | `42,315.00` |
| `Live` | `Long` | `3.08` | 10,050,000.00 USD | 0.00 USD | 9,900.00 USD | `-23.11%` | `3,219.60` |
| `Live` | `Long` | `3.08` | 10,040,000.00 USD | 0.00 USD | 6,950.00 USD | `-22.86%` | `2,253.80` |
| `Live` | `Long` | `3.10` | 10,030,000.00 USD | 0.00 USD | 13,570.00 USD | `-22.61%` | `4,384.80` |
| `Live` | `Long` | `3.10` | 10,020,000.00 USD | 0.00 USD | 17,000.00 USD | `-22.36%` | `5,476.00` |
| `Live` | `Long` | `3.12` | 10,000,000.00 USD | 0.00 USD | 32,910.00 USD | `-22.11%` | `10,565.20` |
| `Live` | `Long` | `3.12` | 9,970,000.00 USD | 0.00 USD | 9,600.00 USD | `-21.86%` | `3,072.50` |
| `Live` | `Long` | `3.13` | 9,960,000.00 USD | 0.00 USD | 11,780.00 USD | `-21.61%` | `3,757.80` |
| `Live` | `Long` | `3.15` | 9,950,000.00 USD | 0.00 USD | 236,000.00 USD | `-21.36%` | `75,040.20` |
| `Live` | `Long` | `3.15` | 9,710,000.00 USD | 0.00 USD | 41,210.00 USD | `-21.11%` | `13,063.00` |
| `Live` | `Long` | `3.17` | 9,670,000.00 USD | 0.00 USD | 10,620.00 USD | `-20.86%` | `3,354.40` |
| `Live` | `Long` | `3.17` | 9,660,000.00 USD | 0.00 USD | 10,890.00 USD | `-20.61%` | `3,430.50` |
| `Live` | `Long` | `3.19` | 9,650,000.00 USD | 0.00 USD | 243,240.00 USD | `-20.36%` | `76,370.90` |
| `Live` | `Long` | `3.21` | 9,400,000.00 USD | 0.00 USD | 104,190.00 USD | `-19.86%` | `32,507.80` |
| `Live` | `Long` | `3.21` | 9,300,000.00 USD | 0.00 USD | 243,410.00 USD | `-19.61%` | `75,709.80` |
| `Live` | `Long` | `3.23` | 9,060,000.00 USD | 0.00 USD | 23,570.00 USD | `-19.36%` | `7,307.10` |
| `Live` | `Long` | `3.23` | 9,030,000.00 USD | 0.00 USD | 46,270.00 USD | `-19.11%` | `14,302.70` |
| `Live` | `Long` | `3.25` | 8,990,000.00 USD | 0.00 USD | 224,710.00 USD | `-18.86%` | `69,248.20` |
| `Live` | `Long` | `3.25` | 8,760,000.00 USD | 0.00 USD | 5,640.00 USD | `-18.61%` | `1,733.30` |
| `Live` | `Long` | `3.27` | 8,760,000.00 USD | 0.00 USD | 50,750.00 USD | `-18.36%` | `15,544.60` |
| `Live` | `Long` | `3.27` | 8,710,000.00 USD | 0.00 USD | 909,040.00 USD | `-18.11%` | `277,569.60` |
| `Live` | `Long` | `3.29` | 7,800,000.00 USD | 0.00 USD | 5,470.00 USD | `-17.86%` | `1,666.40` |
| `Live` | `Long` | `3.29` | 7,790,000.00 USD | 0.00 USD | 159,640.00 USD | `-17.61%` | `48,449.50` |
| `Live` | `Long` | `3.31` | 7,630,000.00 USD | 0.00 USD | 309,320.00 USD | `-17.36%` | `93,591.10` |
| `Live` | `Long` | `3.31` | 7,320,000.00 USD | 0.00 USD | 17,260.00 USD | `-17.11%` | `5,207.20` |
| `Live` | `Long` | `3.33` | 7,310,000.00 USD | 0.00 USD | 10,150.00 USD | `-16.86%` | `3,052.10` |
| `Live` | `Long` | `3.33` | 7,300,000.00 USD | 0.00 USD | 74,210.00 USD | `-16.61%` | `22,251.00` |
| `Live` | `Long` | `3.35` | 7,220,000.00 USD | 0.00 USD | 35,820.00 USD | `-16.36%` | `10,709.20` |
| `Live` | `Long` | `3.35` | 7,190,000.00 USD | 0.00 USD | 12,140.00 USD | `-16.11%` | `3,619.30` |
| `Live` | `Long` | `3.37` | 7,170,000.00 USD | 0.00 USD | 20,550.00 USD | `-15.86%` | `6,106.30` |
| `Live` | `Long` | `3.38` | 7,150,000.00 USD | 0.00 USD | 58,160.00 USD | `-15.61%` | `17,233.10` |
| `Live` | `Long` | `3.38` | 7,090,000.00 USD | 0.00 USD | 43,640.00 USD | `-15.36%` | `12,892.50` |
| `Live` | `Long` | `3.40` | 7,050,000.00 USD | 0.00 USD | 4,570.00 USD | `-15.11%` | `1,345.80` |
| `Live` | `Long` | `3.40` | 7,050,000.00 USD | 0.00 USD | 76,860.00 USD | `-14.86%` | `22,573.70` |
| `Live` | `Long` | `3.42` | 6,970,000.00 USD | 0.00 USD | 383,470.00 USD | `-14.61%` | `112,288.70` |
| `Live` | `Long` | `3.42` | 6,590,000.00 USD | 0.00 USD | 39,770.00 USD | `-14.36%` | `11,610.70` |
| `Live` | `Long` | `3.44` | 6,550,000.00 USD | 0.00 USD | 27,410.00 USD | `-14.11%` | `7,979.60` |
| `Live` | `Long` | `3.44` | 6,520,000.00 USD | 0.00 USD | 47,430.00 USD | `-13.86%` | `13,767.30` |
| `Live` | `Long` | `3.46` | 6,470,000.00 USD | 0.00 USD | 10,640.00 USD | `-13.61%` | `3,078.50` |
| `Live` | `Long` | `3.46` | 6,460,000.00 USD | 0.00 USD | 16,650.00 USD | `-13.36%` | `4,805.90` |
| `Live` | `Long` | `3.48` | 6,440,000.00 USD | 0.00 USD | 191,200.00 USD | `-13.11%` | `55,022.40` |
| `Live` | `Long` | `3.48` | 6,250,000.00 USD | 0.00 USD | 24,410.00 USD | `-12.86%` | `7,005.20` |
| `Live` | `Long` | `3.50` | 6,230,000.00 USD | 0.00 USD | 58,820.00 USD | `-12.61%` | `16,831.00` |
| `Live` | `Long` | `3.50` | 6,170,000.00 USD | 0.00 USD | 50,010.00 USD | `-12.36%` | `14,267.20` |
| `Live` | `Long` | `3.52` | 6,120,000.00 USD | 0.00 USD | 8,180.00 USD | `-12.11%` | `2,327.20` |
| `Live` | `Long` | `3.52` | 6,110,000.00 USD | 0.00 USD | 188,060.00 USD | `-11.86%` | `53,350.20` |
| `Live` | `Long` | `3.54` | 5,920,000.00 USD | 0.00 USD | 208,650.00 USD | `-11.61%` | `59,022.80` |
| `Live` | `Long` | `3.54` | 5,710,000.00 USD | 0.00 USD | 167,840.00 USD | `-11.36%` | `47,344.30` |
| `Live` | `Long` | `3.56` | 5,550,000.00 USD | 0.00 USD | 376,480.00 USD | `-11.11%` | `105,901.00` |
| `Live` | `Long` | `3.56` | 5,170,000.00 USD | 0.00 USD | 16,340.00 USD | `-10.86%` | `4,584.20` |
| `Live` | `Long` | `3.58` | 5,150,000.00 USD | 0.00 USD | 61,750.00 USD | `-10.61%` | `17,273.20` |
| `Live` | `Long` | `3.58` | 5,090,000.00 USD | 0.00 USD | 35,220.00 USD | `-10.36%` | `9,824.80` |
| `Live` | `Long` | `3.60` | 5,060,000.00 USD | 0.00 USD | 1,320,000.00 USD | `-10.11%` | `367,083.00` |
| `Live` | `Long` | `3.60` | 3,740,000.00 USD | 0.00 USD | 70,390.00 USD | `-9.86%` | `19,525.60` |
| `Live` | `Long` | `3.62` | 3,670,000.00 USD | 0.00 USD | 16,180.00 USD | `-9.61%` | `4,476.60` |
| `Live` | `Long` | `3.62` | 3,650,000.00 USD | 0.00 USD | 32,950.00 USD | `-9.36%` | `9,089.10` |
| `Live` | `Long` | `3.63` | 3,620,000.00 USD | 0.00 USD | 5,070.00 USD | `-9.11%` | `1,393.40` |
| `Live` | `Long` | `3.65` | 3,610,000.00 USD | 0.00 USD | 46,460.00 USD | `-8.86%` | `12,744.90` |
| `Live` | `Long` | `3.65` | 3,570,000.00 USD | 0.00 USD | 19,240.00 USD | `-8.61%` | `5,262.90` |
| `Live` | `Long` | `3.67` | 3,550,000.00 USD | 0.00 USD | 144,310.00 USD | `-8.36%` | `39,374.40` |
| `Live` | `Long` | `3.67` | 3,400,000.00 USD | 0.00 USD | 220,200.00 USD | `-8.11%` | `59,917.40` |
| `Live` | `Long` | `3.69` | 3,180,000.00 USD | 0.00 USD | 256,890.00 USD | `-7.86%` | `69,713.70` |
| `Live` | `Long` | `3.69` | 2,930,000.00 USD | 0.00 USD | 111,190.00 USD | `-7.61%` | `30,092.00` |
| `Live` | `Long` | `3.71` | 2,810,000.00 USD | 0.00 USD | 229,780.00 USD | `-7.36%` | `62,019.80` |
| `Live` | `Long` | `3.71` | 2,580,000.00 USD | 0.00 USD | 15,140.00 USD | `-7.11%` | `4,076.40` |
| `Live` | `Long` | `3.73` | 2,570,000.00 USD | 0.00 USD | 182,160.00 USD | `-6.86%` | `48,901.60` |
| `Live` | `Long` | `3.73` | 2,390,000.00 USD | 0.00 USD | 117,660.00 USD | `-6.61%` | `31,503.30` |
| `Live` | `Long` | `3.75` | 2,270,000.00 USD | 0.00 USD | 98,890.00 USD | `-6.36%` | `26,405.30` |
| `Live` | `Long` | `3.75` | 2,170,000.00 USD | 0.00 USD | 210,440.00 USD | `-6.11%` | `56,042.60` |
| `Live` | `Long` | `3.77` | 1,960,000.00 USD | 0.00 USD | 61,220.00 USD | `-5.86%` | `16,261.50` |
| `Live` | `Long` | `3.77` | 1,900,000.00 USD | 0.00 USD | 67,960.00 USD | `-5.61%` | `18,002.80` |
| `Live` | `Long` | `3.79` | 1,830,000.00 USD | 0.00 USD | 275,510.00 USD | `-5.36%` | `72,791.20` |
| `Live` | `Long` | `3.79` | 1,560,000.00 USD | 0.00 USD | 232,200.00 USD | `-5.11%` | `61,186.80` |
| `Live` | `Long` | `3.81` | 1,320,000.00 USD | 0.00 USD | 20,160.00 USD | `-4.86%` | `5,299.10` |
| `Live` | `Long` | `3.81` | 1,300,000.00 USD | 0.00 USD | 187,420.00 USD | `-4.61%` | `49,127.10` |
| `Live` | `Long` | `3.83` | 1,120,000.00 USD | 0.00 USD | 152,850.00 USD | `-4.36%` | `39,960.40` |
| `Live` | `Long` | `3.83` | 962,850.00 USD | 0.00 USD | 198,510.00 USD | `-4.11%` | `51,763.40` |
| `Live` | `Long` | `3.85` | 764,340.00 USD | 0.00 USD | 115,050.00 USD | `-3.86%` | `29,921.30` |
| `Live` | `Long` | `3.85` | 649,290.00 USD | 0.00 USD | 71,510.00 USD | `-3.61%` | `18,549.70` |
| `Live` | `Long` | `3.87` | 577,790.00 USD | 0.00 USD | 22,480.00 USD | `-3.36%` | `5,816.20` |
| `Live` | `Long` | `3.88` | 555,310.00 USD | 0.00 USD | 8,340.00 USD | `-3.11%` | `2,152.90` |
| `Live` | `Long` | `3.88` | 546,960.00 USD | 0.00 USD | 41,870.00 USD | `-2.86%` | `10,777.00` |
| `Live` | `Long` | `3.90` | 505,090.00 USD | 0.00 USD | 70,490.00 USD | `-2.61%` | `18,098.50` |
| `Live` | `Long` | `3.90` | 434,600.00 USD | 0.00 USD | 4,350.00 USD | `-2.36%` | `1,114.10` |
| `Live` | `Long` | `3.94` | 430,250.00 USD | 0.00 USD | 7,140.00 USD | `-1.36%` | `1,810.90` |
| `Live` | `Long` | `3.96` | 423,110.00 USD | 0.00 USD | 418,460.00 USD | `-1.11%` | `105,805.30` |
| `Live` | `Long` | `3.98` | 4,650.00 USD | 0.00 USD | 4,650.00 USD | `-0.61%` | `1,169.00` |
| `Live` | `Short` | `4.03` | 2,530.00 USD | 2,530.00 USD | 0.00 USD | `+0.64%` | `629.70` |
| `Live` | `Short` | `4.12` | 11,510.00 USD | 8,970.00 USD | 0.00 USD | `+2.89%` | `2,180.50` |
| `Live` | `Short` | `4.12` | 42,020.00 USD | 30,520.00 USD | 0.00 USD | `+3.14%` | `7,397.70` |
| `Live` | `Short` | `4.14` | 46,750.00 USD | 4,730.00 USD | 0.00 USD | `+3.64%` | `1,140.40` |
| `Live` | `Short` | `4.16` | 125,020.00 USD | 78,270.00 USD | 0.00 USD | `+3.89%` | `18,837.30` |
| `Live` | `Short` | `4.17` | 125,540.00 USD | 524.37 USD | 0.00 USD | `+4.14%` | `125.90` |
| `Live` | `Short` | `4.17` | 153,770.00 USD | 28,220.00 USD | 0.00 USD | `+4.39%` | `6,760.20` |
| `Live` | `Short` | `4.18` | 223,740.00 USD | 69,970.00 USD | 0.00 USD | `+4.64%` | `16,720.20` |
| `Live` | `Short` | `4.20` | 224,790.00 USD | 1,050.00 USD | 0.00 USD | `+4.89%` | `249.50` |
| `Live` | `Short` | `4.21` | 259,810.00 USD | 35,020.00 USD | 0.00 USD | `+5.14%` | `8,327.80` |
| `Live` | `Short` | `4.21` | 259,920.00 USD | 112.54 USD | 0.00 USD | `+5.39%` | `26.70` |
| `Live` | `Short` | `4.22` | 260,810.00 USD | 893.59 USD | 0.00 USD | `+5.64%` | `211.50` |
| `Live` | `Short` | `4.24` | 262,870.00 USD | 2,060.00 USD | 0.00 USD | `+5.89%` | `486.60` |
| `Live` | `Short` | `4.25` | 263,520.00 USD | 649.06 USD | 0.00 USD | `+6.14%` | `152.90` |
| `Live` | `Short` | `4.25` | 264,570.00 USD | 1,050.00 USD | 0.00 USD | `+6.39%` | `246.20` |
| `Live` | `Short` | `4.26` | 264,780.00 USD | 208.99 USD | 0.00 USD | `+6.64%` | `49.00` |
| `Live` | `Short` | `4.28` | 265,520.00 USD | 736.58 USD | 0.00 USD | `+6.89%` | `172.30` |
| `Live` | `Short` | `4.29` | 265,680.00 USD | 163.69 USD | 0.00 USD | `+7.14%` | `38.20` |
| `Live` | `Short` | `4.29` | 476,410.00 USD | 210,730.00 USD | 0.00 USD | `+7.39%` | `49,064.30` |
| `Live` | `Short` | `4.30` | 476,980.00 USD | 573.00 USD | 0.00 USD | `+7.64%` | `133.10` |
| `Live` | `Short` | `4.32` | 505,380.00 USD | 28,390.00 USD | 0.00 USD | `+7.89%` | `6,580.40` |
| `Live` | `Short` | `4.34` | 514,170.00 USD | 8,790.00 USD | 0.00 USD | `+8.64%` | `2,023.20` |
| `Live` | `Short` | `4.36` | 519,140.00 USD | 4,970.00 USD | 0.00 USD | `+8.89%` | `1,141.00` |
| `Live` | `Short` | `4.38` | 520,250.00 USD | 1,110.00 USD | 0.00 USD | `+9.39%` | `254.40` |
| `Live` | `Short` | `4.39` | 712,960.00 USD | 192,710.00 USD | 0.00 USD | `+9.89%` | `43,846.50` |
| `Live` | `Short` | `4.41` | 736,390.00 USD | 23,430.00 USD | 0.00 USD | `+10.14%` | `5,319.80` |
| `Live` | `Short` | `4.42` | 736,490.00 USD | 104.87 USD | 0.00 USD | `+10.64%` | `23.70` |
| `Live` | `Short` | `4.46` | 736,960.00 USD | 468.38 USD | 0.00 USD | `+11.64%` | `104.90` |
| `Live` | `Short` | `4.47` | 737,590.00 USD | 629.18 USD | 0.00 USD | `+11.89%` | `140.60` |
| `Live` | `Short` | `4.50` | 827,770.00 USD | 90,180.00 USD | 0.00 USD | `+12.39%` | `20,062.40` |
| `Live` | `Short` | `4.50` | 897,900.00 USD | 70,130.00 USD | 0.00 USD | `+12.64%` | `15,566.70` |
| `Live` | `Short` | `4.51` | 898,290.00 USD | 389.19 USD | 0.00 USD | `+12.89%` | `86.20` |
| `Live` | `Short` | `4.53` | 917,350.00 USD | 19,060.00 USD | 0.00 USD | `+13.14%` | `4,211.20` |
| `Live` | `Short` | `4.54` | 921,460.00 USD | 4,110.00 USD | 0.00 USD | `+13.64%` | `905.20` |
| `Live` | `Short` | `4.55` | 922,040.00 USD | 583.50 USD | 0.00 USD | `+13.89%` | `128.10` |
| `Live` | `Short` | `4.57` | 1,610,000.00 USD | 685,090.00 USD | 0.00 USD | `+14.14%` | `150,075.00` |
| `Live` | `Short` | `4.58` | 1,620,000.00 USD | 14,690.00 USD | 0.00 USD | `+14.39%` | `3,211.90` |
| `Live` | `Short` | `4.59` | 1,630,000.00 USD | 8,230.00 USD | 0.00 USD | `+14.89%` | `1,790.50` |
| `Live` | `Short` | `4.61` | 1,630,000.00 USD | 1,050.00 USD | 0.00 USD | `+15.14%` | `227.10` |
| `Live` | `Short` | `4.63` | 1,630,000.00 USD | 990.04 USD | 0.00 USD | `+15.89%` | `213.60` |
| `Live` | `Short` | `4.66` | 1,630,000.00 USD | 124.75 USD | 0.00 USD | `+16.39%` | `26.80` |
| `Live` | `Short` | `4.67` | 1,630,000.00 USD | 101.70 USD | 0.00 USD | `+16.64%` | `21.80` |
| `Live` | `Short` | `4.70` | 1,630,000.00 USD | 230.06 USD | 0.00 USD | `+17.39%` | `49.00` |
| `Live` | `Short` | `4.71` | 1,640,000.00 USD | 7,480.00 USD | 0.00 USD | `+17.64%` | `1,590.30` |
| `Live` | `Short` | `4.71` | 1,640,000.00 USD | 460.18 USD | 0.00 USD | `+17.89%` | `97.60` |
| `Live` | `Short` | `4.72` | 1,640,000.00 USD | 851.44 USD | 0.00 USD | `+18.14%` | `180.20` |
| `Live` | `Short` | `4.76` | 1,710,000.00 USD | 64,260.00 USD | 0.00 USD | `+19.14%` | `13,485.80` |
| `Live` | `Short` | `4.78` | 1,710,000.00 USD | 8,780.00 USD | 0.00 USD | `+19.39%` | `1,839.40` |
| `Live` | `Short` | `4.79` | 1,740,000.00 USD | 25,830.00 USD | 0.00 USD | `+19.64%` | `5,398.50` |
| `Live` | `Short` | `4.79` | 1,740,000.00 USD | 1,330.00 USD | 0.00 USD | `+19.89%` | `277.70` |
| `Live` | `Short` | `4.82` | 1,790,000.00 USD | 45,670.00 USD | 0.00 USD | `+20.39%` | `9,484.50` |
| `Live` | `Short` | `4.83` | 1,790,000.00 USD | 3,020.00 USD | 0.00 USD | `+20.64%` | `625.50` |
| `Live` | `Short` | `4.83` | 1,790,000.00 USD | 1,950.00 USD | 0.00 USD | `+20.89%` | `403.60` |
| `Live` | `Short` | `4.84` | 1,800,000.00 USD | 11,220.00 USD | 0.00 USD | `+21.14%` | `2,316.40` |
| `Live` | `Short` | `4.87` | 1,800,000.00 USD | 137.68 USD | 0.00 USD | `+21.64%` | `28.30` |
| `Live` | `Short` | `4.88` | 1,800,000.00 USD | 827.03 USD | 0.00 USD | `+22.14%` | `169.30` |
| `Live` | `Short` | `4.92` | 1,830,000.00 USD | 20,720.00 USD | 0.00 USD | `+22.89%` | `4,214.80` |
| `Live` | `Short` | `4.92` | 1,830,000.00 USD | 2,100.00 USD | 0.00 USD | `+23.14%` | `425.70` |
| `Live` | `Short` | `4.93` | 1,830,000.00 USD | 157.43 USD | 0.00 USD | `+23.39%` | `31.90` |
| `Live` | `Short` | `4.96` | 1,830,000.00 USD | 342.89 USD | 0.00 USD | `+23.89%` | `69.20` |
| `Live` | `Short` | `4.97` | 1,930,000.00 USD | 99,810.00 USD | 0.00 USD | `+24.39%` | `20,062.00` |
| `Live` | `Short` | `4.99` | 1,930,000.00 USD | 139.08 USD | 0.00 USD | `+24.64%` | `27.90` |
| `Live` | `Short` | `5.00` | 1,930,000.00 USD | 339.66 USD | 0.00 USD | `+24.89%` | `68.00` |
| `Live` | `Short` | `5.05` | 1,960,000.00 USD | 35,380.00 USD | 0.00 USD | `+26.39%` | `6,998.80` |
| `Live` | `Short` | `5.07` | 1,970,000.00 USD | 3,420.00 USD | 0.00 USD | `+26.64%` | `675.80` |
| `Live` | `Short` | `5.08` | 1,990,000.00 USD | 21,540.00 USD | 0.00 USD | `+27.14%` | `4,236.30` |
| `Live` | `Short` | `5.12` | 1,990,000.00 USD | 2,560.00 USD | 0.00 USD | `+28.14%` | `500.00` |
| `Live` | `Short` | `5.13` | 1,990,000.00 USD | 1,650.00 USD | 0.00 USD | `+28.39%` | `320.50` |
| `Live` | `Short` | `5.17` | 1,990,000.00 USD | 751.51 USD | 0.00 USD | `+29.14%` | `145.50` |
| `Live` | `Short` | `5.20` | 2,000,000.00 USD | 7,280.00 USD | 0.00 USD | `+29.89%` | `1,401.50` |
| `Live` | `Short` | `5.22` | 2,070,000.00 USD | 72,110.00 USD | 0.00 USD | `+30.64%` | `13,800.00` |
| `Live` | `Short` | `5.24` | 2,080,000.00 USD | 2,620.00 USD | 0.00 USD | `+30.89%` | `500.00` |
| `Live` | `Short` | `5.25` | 2,080,000.00 USD | 143.71 USD | 0.00 USD | `+31.14%` | `27.40` |
| `Live` | `Short` | `5.25` | 2,080,000.00 USD | 288.50 USD | 0.00 USD | `+31.39%` | `54.90` |
| `Live` | `Short` | `5.26` | 2,080,000.00 USD | 5,610.00 USD | 0.00 USD | `+31.64%` | `1,066.10` |
| `Live` | `Short` | `5.29` | 2,080,000.00 USD | 134.77 USD | 0.00 USD | `+32.14%` | `25.50` |
| `Live` | `Short` | `5.30` | 2,080,000.00 USD | 524.66 USD | 0.00 USD | `+32.64%` | `98.90` |
| `Live` | `Short` | `5.32` | 2,080,000.00 USD | 718.59 USD | 0.00 USD | `+32.89%` | `135.20` |
| `Live` | `Short` | `5.34` | 2,100,000.00 USD | 19,710.00 USD | 0.00 USD | `+33.64%` | `3,686.80` |
| `Live` | `Short` | `5.36` | 2,100,000.00 USD | 142.44 USD | 0.00 USD | `+33.89%` | `26.60` |
| `Live` | `Short` | `5.38` | 3,180,000.00 USD | 1,080,000.00 USD | 0.00 USD | `+34.39%` | `200,129.00` |
| `Live` | `Short` | `5.38` | 3,180,000.00 USD | 620.89 USD | 0.00 USD | `+34.64%` | `115.30` |
| `Live` | `Short` | `5.41` | 3,180,000.00 USD | 5,410.00 USD | 0.00 USD | `+35.14%` | `1,000.00` |
| `Live` | `Short` | `5.43` | 3,180,000.00 USD | 419.04 USD | 0.00 USD | `+35.89%` | `77.10` |
| `Live` | `Short` | `5.45` | 3,250,000.00 USD | 63,020.00 USD | 0.00 USD | `+36.14%` | `11,574.80` |
| `Live` | `Short` | `5.46` | 3,250,000.00 USD | 1,360.00 USD | 0.00 USD | `+36.39%` | `250.00` |
| `Live` | `Short` | `5.46` | 3,310,000.00 USD | 62,030.00 USD | 0.00 USD | `+36.64%` | `11,349.70` |
| `Live` | `Short` | `5.47` | 3,310,000.00 USD | 627.98 USD | 0.00 USD | `+36.89%` | `114.70` |
| `Live` | `Short` | `5.50` | 3,380,000.00 USD | 66,470.00 USD | 0.00 USD | `+37.39%` | `12,097.30` |
| `Live` | `Short` | `5.51` | 3,420,000.00 USD | 38,800.00 USD | 0.00 USD | `+37.89%` | `7,034.90` |
| `Live` | `Short` | `5.54` | 3,440,000.00 USD | 26,740.00 USD | 0.00 USD | `+38.39%` | `4,831.90` |
| `Live` | `Short` | `5.55` | 3,530,000.00 USD | 88,750.00 USD | 0.00 USD | `+38.89%` | `15,976.20` |
| `Live` | `Short` | `5.57` | 3,540,000.00 USD | 8,670.00 USD | 0.00 USD | `+39.14%` | `1,557.40` |
| `Live` | `Short` | `5.58` | 3,600,000.00 USD | 62,420.00 USD | 0.00 USD | `+39.64%` | `11,175.80` |
| `Live` | `Short` | `5.59` | 3,600,000.00 USD | 686.51 USD | 0.00 USD | `+39.89%` | `122.70` |
| `Live` | `Short` | `5.62` | 3,720,000.00 USD | 119,230.00 USD | 0.00 USD | `+40.65%` | `21,196.20` |
| `Live` | `Short` | `5.67` | 3,720,000.00 USD | 211.30 USD | 0.00 USD | `+41.65%` | `37.30` |
| `Live` | `Short` | `5.67` | 3,720,000.00 USD | 228.70 USD | 0.00 USD | `+41.90%` | `40.30` |
| `Live` | `Short` | `5.68` | 3,750,000.00 USD | 26,090.00 USD | 0.00 USD | `+42.15%` | `4,589.50` |
| `Live` | `Short` | `5.70` | 3,750,000.00 USD | 1,520.00 USD | 0.00 USD | `+42.40%` | `267.40` |
| `Live` | `Short` | `5.71` | 3,750,000.00 USD | 2,130.00 USD | 0.00 USD | `+42.90%` | `372.40` |
| `Live` | `Short` | `5.75` | 3,760,000.00 USD | 4,580.00 USD | 0.00 USD | `+43.65%` | `796.90` |
| `Live` | `Short` | `5.75` | 5,420,000.00 USD | 1,660,000.00 USD | 0.00 USD | `+43.90%` | `288,077.60` |
| `Live` | `Short` | `5.78` | 5,420,000.00 USD | 127.05 USD | 0.00 USD | `+44.40%` | `22.00` |
| `Live` | `Short` | `5.80` | 5,420,000.00 USD | 2,670.00 USD | 0.00 USD | `+45.15%` | `460.20` |
| `Live` | `Short` | `5.83` | 5,550,000.00 USD | 133,430.00 USD | 0.00 USD | `+45.90%` | `22,867.70` |
| `Live` | `Short` | `5.84` | 5,550,000.00 USD | 310.95 USD | 0.00 USD | `+46.15%` | `53.20` |
| `Live` | `Short` | `5.86` | 5,550,000.00 USD | 848.39 USD | 0.00 USD | `+46.40%` | `144.90` |
| `Live` | `Short` | `5.87` | 5,580,000.00 USD | 22,780.00 USD | 0.00 USD | `+46.65%` | `3,883.80` |
| `Live` | `Short` | `5.88` | 5,580,000.00 USD | 200.34 USD | 0.00 USD | `+46.90%` | `34.10` |
| `Live` | `Short` | `5.88` | 5,580,000.00 USD | 7,150.00 USD | 0.00 USD | `+47.15%` | `1,215.40` |
| `Live` | `Short` | `5.89` | 5,670,000.00 USD | 88,590.00 USD | 0.00 USD | `+47.40%` | `15,027.60` |
| `Live` | `Short` | `5.92` | 5,670,000.00 USD | 189.28 USD | 0.00 USD | `+47.90%` | `32.00` |
| `Live` | `Short` | `5.95` | 5,780,000.00 USD | 103,650.00 USD | 0.00 USD | `+48.65%` | `17,434.80` |
| `Live` | `Short` | `5.97` | 5,780,000.00 USD | 5,100.00 USD | 0.00 USD | `+49.40%` | `852.80` |
| `Live` | `Short` | `6.00` | 6,100,000.00 USD | 320,750.00 USD | 0.00 USD | `+49.90%` | `53,503.40` |
| `Live` | `Short` | `6.01` | 6,100,000.00 USD | 154.59 USD | 0.00 USD | `+50.40%` | `25.70` |
| `Live` | `Short` | `6.03` | 6,130,000.00 USD | 23,060.00 USD | 0.00 USD | `+50.65%` | `3,827.40` |
| `Live` | `Short` | `6.07` | 6,130,000.00 USD | 740.54 USD | 0.00 USD | `+51.65%` | `122.10` |
| `Live` | `Short` | `6.08` | 6,480,000.00 USD | 352,550.00 USD | 0.00 USD | `+51.90%` | `58,033.10` |
| `Live` | `Short` | `6.08` | 6,480,000.00 USD | 5,920.00 USD | 0.00 USD | `+52.15%` | `973.10` |
| `Live` | `Short` | `6.09` | 6,520,000.00 USD | 37,510.00 USD | 0.00 USD | `+52.40%` | `6,154.10` |
| `Live` | `Short` | `6.13` | 6,520,000.00 USD | 2,430.00 USD | 0.00 USD | `+53.40%` | `396.10` |
| `Live` | `Short` | `6.16` | 6,530,000.00 USD | 865.39 USD | 0.00 USD | `+53.90%` | `140.60` |
| `Live` | `Short` | `6.17` | 6,570,000.00 USD | 47,670.00 USD | 0.00 USD | `+54.40%` | `7,720.00` |
| `Live` | `Short` | `6.25` | 6,580,000.00 USD | 7,300.00 USD | 0.00 USD | `+56.15%` | `1,168.90` |
| `Live` | `Short` | `6.25` | 6,580,000.00 USD | 439.10 USD | 0.00 USD | `+56.40%` | `70.20` |
| `Live` | `Short` | `6.28` | 6,580,000.00 USD | 397.84 USD | 0.00 USD | `+56.90%` | `63.40` |
| `Live` | `Short` | `6.32` | 6,580,000.00 USD | 310.70 USD | 0.00 USD | `+57.90%` | `49.20` |
| `Live` | `Short` | `6.33` | 6,580,000.00 USD | 382.00 USD | 0.00 USD | `+58.40%` | `60.30` |
| `Live` | `Short` | `6.34` | 6,580,000.00 USD | 214.46 USD | 0.00 USD | `+58.65%` | `33.80` |
| `Live` | `Short` | `6.36` | 6,630,000.00 USD | 49,740.00 USD | 0.00 USD | `+58.90%` | `7,827.40` |
| `Live` | `Short` | `6.37` | 6,930,000.00 USD | 294,370.00 USD | 0.00 USD | `+59.15%` | `46,248.60` |
| `Live` | `Short` | `6.38` | 6,930,000.00 USD | 3,390.00 USD | 0.00 USD | `+59.40%` | `532.10` |
| `Live` | `Short` | `6.38` | 6,930,000.00 USD | 2,000.00 USD | 0.00 USD | `+59.65%` | `312.80` |
| `Live` | `Short` | `6.41` | 6,940,000.00 USD | 3,780.00 USD | 0.00 USD | `+60.15%` | `590.10` |
| `Live` | `Short` | `6.42` | 6,940,000.00 USD | 8,700.00 USD | 0.00 USD | `+60.40%` | `1,356.50` |
| `Live` | `Short` | `6.42` | 6,940,000.00 USD | 173.47 USD | 0.00 USD | `+60.65%` | `27.00` |
| `Live` | `Short` | `6.45` | 6,950,000.00 USD | 5,270.00 USD | 0.00 USD | `+61.15%` | `818.40` |
| `Live` | `Short` | `6.46` | 6,960,000.00 USD | 7,150.00 USD | 0.00 USD | `+61.40%` | `1,107.10` |
| `Live` | `Short` | `6.46` | 6,960,000.00 USD | 1,940.00 USD | 0.00 USD | `+61.65%` | `300.00` |
| `Live` | `Short` | `6.51` | 6,960,000.00 USD | 1,070.00 USD | 0.00 USD | `+62.90%` | `164.50` |
| `Live` | `Short` | `6.54` | 6,960,000.00 USD | 265.07 USD | 0.00 USD | `+63.65%` | `40.50` |
| `Live` | `Short` | `6.57` | 6,960,000.00 USD | 122.11 USD | 0.00 USD | `+64.15%` | `18.60` |
| `Live` | `Short` | `6.59` | 6,960,000.00 USD | 418.78 USD | 0.00 USD | `+64.90%` | `63.50` |
| `Live` | `Short` | `6.66` | 36,960,000.00 USD | 30,000,000.00 USD | 0.00 USD | `+66.40%` | `4,508,349.40` |
| `Live` | `Short` | `6.67` | 36,960,000.00 USD | 233.94 USD | 0.00 USD | `+66.65%` | `35.10` |
| `Live` | `Short` | `6.67` | 37,000,000.00 USD | 37,290.00 USD | 0.00 USD | `+66.90%` | `5,586.90` |
| `Live` | `Short` | `6.71` | 37,000,000.00 USD | 2,190.00 USD | 0.00 USD | `+67.90%` | `326.60` |
| `Live` | `Short` | `6.75` | 38,380,000.00 USD | 1,380,000.00 USD | 0.00 USD | `+68.90%` | `204,058.10` |
| `Live` | `Short` | `6.79` | 38,390,000.00 USD | 9,390.00 USD | 0.00 USD | `+69.65%` | `1,384.00` |
| `Live` | `Short` | `6.79` | 38,660,000.00 USD | 266,450.00 USD | 0.00 USD | `+69.90%` | `39,212.60` |
| `Live` | `Short` | `6.84` | 38,660,000.00 USD | 753.63 USD | 0.00 USD | `+71.15%` | `110.10` |
| `Live` | `Short` | `6.87` | 38,660,000.00 USD | 2,650.00 USD | 0.00 USD | `+71.65%` | `386.60` |
| `Live` | `Short` | `6.89` | 38,660,000.00 USD | 189.61 USD | 0.00 USD | `+72.40%` | `27.50` |
| `Live` | `Short` | `6.92` | 38,670,000.00 USD | 6,920.00 USD | 0.00 USD | `+73.15%` | `1,000.00` |
| `Live` | `Short` | `6.99` | 38,670,000.00 USD | 664.27 USD | 0.00 USD | `+74.65%` | `95.10` |
| `Live` | `Short` | `7.00` | 38,670,000.00 USD | 190.96 USD | 0.00 USD | `+74.90%` | `27.30` |
| `Live` | `Short` | `7.03` | 38,740,000.00 USD | 70,250.00 USD | 0.00 USD | `+75.65%` | `10,000.00` |
| `Live` | `Short` | `7.09` | 38,740,000.00 USD | 699.57 USD | 0.00 USD | `+77.40%` | `98.60` |
| `Live` | `Short` | `7.14` | 38,760,000.00 USD | 15,990.00 USD | 0.00 USD | `+78.65%` | `2,237.40` |
| `Live` | `Short` | `7.20` | 38,770,000.00 USD | 11,070.00 USD | 0.00 USD | `+79.90%` | `1,538.10` |
| `Live` | `Short` | `7.21` | 38,780,000.00 USD | 13,560.00 USD | 0.00 USD | `+80.40%` | `1,879.60` |
| `Live` | `Short` | `7.24` | 38,790,000.00 USD | 4,910.00 USD | 0.00 USD | `+80.90%` | `679.30` |
| `Live` | `Short` | `7.29` | 39,130,000.00 USD | 342,210.00 USD | 0.00 USD | `+82.15%` | `46,974.00` |
| `Live` | `Short` | `7.33` | 40,510,000.00 USD | 1,380,000.00 USD | 0.00 USD | `+83.40%` | `188,180.00` |
| `Live` | `Short` | `7.42` | 40,610,000.00 USD | 105,860.00 USD | 0.00 USD | `+85.40%` | `14,276.50` |
| `Live` | `Short` | `7.46` | 40,610,000.00 USD | 1,420.00 USD | 0.00 USD | `+86.40%` | `191.10` |
| `Live` | `Short` | `7.50` | 40,640,000.00 USD | 26,210.00 USD | 0.00 USD | `+87.40%` | `3,496.50` |
| `Live` | `Short` | `7.51` | 40,640,000.00 USD | 2,610.00 USD | 0.00 USD | `+87.90%` | `347.20` |
| `Live` | `Short` | `7.53` | 40,650,000.00 USD | 1,570.00 USD | 0.00 USD | `+88.15%` | `208.40` |
| `Live` | `Short` | `7.54` | 40,650,000.00 USD | 5,990.00 USD | 0.00 USD | `+88.65%` | `794.40` |
| `Live` | `Short` | `7.57` | 40,650,000.00 USD | 599.90 USD | 0.00 USD | `+89.15%` | `79.30` |
| `Live` | `Short` | `7.59` | 50,810,000.00 USD | 10,160,000.00 USD | 0.00 USD | `+89.90%` | `1,337,750.00` |
| `Live` | `Short` | `7.61` | 50,810,000.00 USD | 911.08 USD | 0.00 USD | `+90.15%` | `119.80` |
| `Live` | `Short` | `7.62` | 58,730,000.00 USD | 7,920,000.00 USD | 0.00 USD | `+90.40%` | `1,039,618.50` |
| `Live` | `Short` | `7.63` | 58,750,000.00 USD | 19,210.00 USD | 0.00 USD | `+90.90%` | `2,516.10` |
| `Live` | `Short` | `7.67` | 58,750,000.00 USD | 360.25 USD | 0.00 USD | `+91.65%` | `47.00` |
| `Live` | `Short` | `7.71` | 58,750,000.00 USD | 318.63 USD | 0.00 USD | `+92.90%` | `41.30` |
| `Live` | `Short` | `7.72` | 58,750,000.00 USD | 259.56 USD | 0.00 USD | `+93.15%` | `33.60` |
| `Live` | `Short` | `7.74` | 58,750,000.00 USD | 505.87 USD | 0.00 USD | `+93.40%` | `65.40` |
| `Live` | `Short` | `7.75` | 58,750,000.00 USD | 629.67 USD | 0.00 USD | `+93.65%` | `81.30` |
| `Live` | `Short` | `7.79` | 58,780,000.00 USD | 33,540.00 USD | 0.00 USD | `+94.65%` | `4,308.50` |
| `Live` | `Short` | `7.79` | 59,780,000.00 USD | 999,130.00 USD | 0.00 USD | `+94.90%` | `128,176.10` |
| `Live` | `Short` | `7.87` | 59,790,000.00 USD | 2,980.00 USD | 0.00 USD | `+96.65%` | `378.70` |
| `Live` | `Short` | `7.92` | 59,790,000.00 USD | 1,800.00 USD | 0.00 USD | `+98.15%` | `226.70` |
| `Live` | `Short` | `7.93` | 60,120,000.00 USD | 334,980.00 USD | 0.00 USD | `+98.40%` | `42,215.40` |
| `Live` | `Short` | `7.95` | 60,130,000.00 USD | 6,120.00 USD | 0.00 USD | `+98.65%` | `769.80` |
| `Live` | `Short` | `7.96` | 60,260,000.00 USD | 134,380.00 USD | 0.00 USD | `+99.15%` | `16,871.00` |
| `Live` | `Short` | `7.99` | 60,260,000.00 USD | 399.25 USD | 0.00 USD | `+99.65%` | `50.00` |
| `Live` | `Short` | `8.00` | 60,270,000.00 USD | 6,090.00 USD | 0.00 USD | `+99.90%` | `761.90` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `0.8050` | 2,330,000.00 USD | 0.00 USD | 107.71 USD | `-79.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8250` | 2,330,000.00 USD | 0.00 USD | 209.80 USD | `-79.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.00` | 2,330,000.00 USD | 0.00 USD | 585.51 USD | `-74.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.01` | 2,330,000.00 USD | 0.00 USD | 339.82 USD | `-74.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.20` | 2,330,000.00 USD | 0.00 USD | 196.58 USD | `-70.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.34` | 2,330,000.00 USD | 0.00 USD | 331.54 USD | `-66.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.35` | 2,330,000.00 USD | 0.00 USD | 345.25 USD | `-66.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.38` | 2,330,000.00 USD | 0.00 USD | 5,640.00 USD | `-65.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.40` | 2,330,000.00 USD | 0.00 USD | 997.29 USD | `-65.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.51` | 2,330,000.00 USD | 0.00 USD | 139.83 USD | `-62.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.53` | 2,330,000.00 USD | 0.00 USD | 113.28 USD | `-61.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.54` | 2,330,000.00 USD | 0.00 USD | 4,000.00 USD | `-61.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.55` | 2,320,000.00 USD | 0.00 USD | 324.22 USD | `-61.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.59` | 2,320,000.00 USD | 0.00 USD | 4,590.00 USD | `-60.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.61` | 2,320,000.00 USD | 0.00 USD | 739.67 USD | `-59.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.62` | 2,320,000.00 USD | 0.00 USD | 1,740.00 USD | `-59.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.64` | 2,310,000.00 USD | 0.00 USD | 6,260.00 USD | `-59.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.66` | 2,310,000.00 USD | 0.00 USD | 345.40 USD | `-58.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.68` | 2,310,000.00 USD | 0.00 USD | 167.50 USD | `-58.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.70` | 2,310,000.00 USD | 0.00 USD | 669.02 USD | `-57.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.71` | 2,310,000.00 USD | 0.00 USD | 105.88 USD | `-57.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.73` | 2,310,000.00 USD | 0.00 USD | 172.50 USD | `-56.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.77` | 2,310,000.00 USD | 0.00 USD | 10,650.00 USD | `-55.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.80` | 2,300,000.00 USD | 0.00 USD | 722.00 USD | `-54.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.81` | 2,290,000.00 USD | 0.00 USD | 259.00 USD | `-54.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.82` | 2,290,000.00 USD | 0.00 USD | 103.84 USD | `-54.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.83` | 2,290,000.00 USD | 0.00 USD | 109.00 USD | `-54.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.88` | 2,290,000.00 USD | 0.00 USD | 222.19 USD | `-53.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.89` | 2,290,000.00 USD | 0.00 USD | 10,280.00 USD | `-52.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.91` | 2,280,000.00 USD | 0.00 USD | 558.36 USD | `-52.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.93` | 2,280,000.00 USD | 0.00 USD | 1,520.00 USD | `-51.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.94` | 2,280,000.00 USD | 0.00 USD | 222.14 USD | `-51.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.95` | 2,280,000.00 USD | 0.00 USD | 279.50 USD | `-51.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.98` | 2,280,000.00 USD | 0.00 USD | 197.50 USD | `-50.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.00` | 2,280,000.00 USD | 0.00 USD | 935.66 USD | `-50.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.00` | 2,280,000.00 USD | 0.00 USD | 18,860.00 USD | `-49.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.02` | 2,260,000.00 USD | 0.00 USD | 3,020.00 USD | `-49.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.04` | 2,260,000.00 USD | 0.00 USD | 214.52 USD | `-48.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.06` | 2,260,000.00 USD | 0.00 USD | 1,200.00 USD | `-48.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.06` | 2,260,000.00 USD | 0.00 USD | 578.41 USD | `-48.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.10` | 2,260,000.00 USD | 0.00 USD | 18,070.00 USD | `-47.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.10` | 2,240,000.00 USD | 0.00 USD | 108.62 USD | `-47.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.12` | 2,240,000.00 USD | 0.00 USD | 107.23 USD | `-47.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.12` | 2,240,000.00 USD | 0.00 USD | 1,590.00 USD | `-46.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.15` | 2,240,000.00 USD | 0.00 USD | 5,830.00 USD | `-46.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.15` | 2,230,000.00 USD | 0.00 USD | 310.32 USD | `-46.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.17` | 2,230,000.00 USD | 0.00 USD | 1,170.00 USD | `-45.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.19` | 2,230,000.00 USD | 0.00 USD | 576.18 USD | `-45.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.19` | 2,230,000.00 USD | 0.00 USD | 295.67 USD | `-45.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.21` | 2,230,000.00 USD | 0.00 USD | 1,430.00 USD | `-44.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.21` | 2,230,000.00 USD | 0.00 USD | 812.68 USD | `-44.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.23` | 2,230,000.00 USD | 0.00 USD | 1,590.00 USD | `-44.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.23` | 2,220,000.00 USD | 0.00 USD | 106.16 USD | `-44.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.25` | 2,220,000.00 USD | 0.00 USD | 6,270.00 USD | `-43.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.25` | 2,220,000.00 USD | 0.00 USD | 478.06 USD | `-43.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.27` | 2,220,000.00 USD | 0.00 USD | 540.88 USD | `-43.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.27` | 2,220,000.00 USD | 0.00 USD | 1,210.00 USD | `-43.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.29` | 2,220,000.00 USD | 0.00 USD | 759.76 USD | `-42.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.29` | 2,210,000.00 USD | 0.00 USD | 11,060.00 USD | `-42.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.31` | 2,200,000.00 USD | 0.00 USD | 3,690.00 USD | `-42.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.33` | 2,200,000.00 USD | 0.00 USD | 722.15 USD | `-41.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.33` | 2,200,000.00 USD | 0.00 USD | 467.00 USD | `-41.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.35` | 2,200,000.00 USD | 0.00 USD | 506.75 USD | `-41.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.37` | 2,200,000.00 USD | 0.00 USD | 214.27 USD | `-40.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.38` | 2,200,000.00 USD | 0.00 USD | 428.69 USD | `-40.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.38` | 2,200,000.00 USD | 0.00 USD | 322.45 USD | `-40.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.40` | 2,200,000.00 USD | 0.00 USD | 108.25 USD | `-40.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.40` | 2,200,000.00 USD | 0.00 USD | 3,900.00 USD | `-39.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.42` | 2,190,000.00 USD | 0.00 USD | 799.04 USD | `-39.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.44` | 2,190,000.00 USD | 0.00 USD | 6,830.00 USD | `-39.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.44` | 2,190,000.00 USD | 0.00 USD | 137.16 USD | `-38.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.48` | 2,190,000.00 USD | 0.00 USD | 504.41 USD | `-38.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.48` | 2,190,000.00 USD | 0.00 USD | 963.93 USD | `-37.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.50` | 2,180,000.00 USD | 0.00 USD | 6,690.00 USD | `-37.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.52` | 2,180,000.00 USD | 0.00 USD | 541.98 USD | `-37.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.54` | 2,180,000.00 USD | 0.00 USD | 108.75 USD | `-36.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.54` | 2,180,000.00 USD | 0.00 USD | 766.55 USD | `-36.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.56` | 2,180,000.00 USD | 0.00 USD | 1,010.00 USD | `-36.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.58` | 2,180,000.00 USD | 0.00 USD | 1,100.00 USD | `-35.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.58` | 2,170,000.00 USD | 0.00 USD | 100.04 USD | `-35.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.60` | 2,170,000.00 USD | 0.00 USD | 833.08 USD | `-34.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.62` | 2,170,000.00 USD | 0.00 USD | 5,090.00 USD | `-34.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.67` | 2,170,000.00 USD | 0.00 USD | 226.57 USD | `-33.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.69` | 2,170,000.00 USD | 0.00 USD | 104.98 USD | `-32.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.69` | 2,170,000.00 USD | 0.00 USD | 889.89 USD | `-32.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.71` | 2,170,000.00 USD | 0.00 USD | 7,410.00 USD | `-32.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.73` | 2,160,000.00 USD | 0.00 USD | 107.21 USD | `-31.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.75` | 2,160,000.00 USD | 0.00 USD | 197.37 USD | `-31.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.75` | 2,160,000.00 USD | 0.00 USD | 8,390.00 USD | `-31.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.77` | 2,150,000.00 USD | 0.00 USD | 108.39 USD | `-30.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.77` | 2,150,000.00 USD | 0.00 USD | 435.95 USD | `-30.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.79` | 2,150,000.00 USD | 0.00 USD | 217.23 USD | `-30.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.79` | 2,150,000.00 USD | 0.00 USD | 437.98 USD | `-30.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.81` | 2,150,000.00 USD | 0.00 USD | 2,720.00 USD | `-29.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.83` | 2,150,000.00 USD | 0.00 USD | 8,380.00 USD | `-29.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.85` | 2,140,000.00 USD | 0.00 USD | 109.53 USD | `-28.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.85` | 2,140,000.00 USD | 0.00 USD | 1,230.00 USD | `-28.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.88` | 2,140,000.00 USD | 0.00 USD | 3,220.00 USD | `-28.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.88` | 2,130,000.00 USD | 0.00 USD | 746.06 USD | `-27.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.90` | 2,130,000.00 USD | 0.00 USD | 2,900.00 USD | `-27.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.90` | 2,130,000.00 USD | 0.00 USD | 4,870.00 USD | `-27.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.92` | 2,130,000.00 USD | 0.00 USD | 358.90 USD | `-26.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.94` | 2,120,000.00 USD | 0.00 USD | 15,370.00 USD | `-26.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.96` | 2,110,000.00 USD | 0.00 USD | 738.75 USD | `-26.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.96` | 2,110,000.00 USD | 0.00 USD | 523.32 USD | `-25.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.98` | 2,110,000.00 USD | 0.00 USD | 4,470.00 USD | `-25.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.00` | 2,100,000.00 USD | 0.00 USD | 22,910.00 USD | `-24.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.02` | 2,080,000.00 USD | 0.00 USD | 1,020.00 USD | `-24.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.02` | 2,080,000.00 USD | 0.00 USD | 345.76 USD | `-24.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.04` | 2,080,000.00 USD | 0.00 USD | 214.57 USD | `-24.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.04` | 2,080,000.00 USD | 0.00 USD | 249.08 USD | `-23.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.06` | 2,080,000.00 USD | 0.00 USD | 109.42 USD | `-23.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.08` | 2,080,000.00 USD | 0.00 USD | 721.58 USD | `-22.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.10` | 2,080,000.00 USD | 0.00 USD | 9,300.00 USD | `-22.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.12` | 2,070,000.00 USD | 0.00 USD | 8,570.00 USD | `-22.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.12` | 2,060,000.00 USD | 0.00 USD | 104.69 USD | `-21.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.13` | 2,060,000.00 USD | 0.00 USD | 315.69 USD | `-21.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.15` | 2,060,000.00 USD | 0.00 USD | 17,510.00 USD | `-21.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.15` | 2,040,000.00 USD | 0.00 USD | 231,740.00 USD | `-21.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.17` | 1,810,000.00 USD | 0.00 USD | 4,210.00 USD | `-20.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.17` | 1,810,000.00 USD | 0.00 USD | 1,030.00 USD | `-20.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.19` | 1,810,000.00 USD | 0.00 USD | 218.81 USD | `-20.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.21` | 1,810,000.00 USD | 0.00 USD | 25,410.00 USD | `-19.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.21` | 1,780,000.00 USD | 0.00 USD | 144.67 USD | `-19.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.25` | 1,780,000.00 USD | 0.00 USD | 27,380.00 USD | `-18.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.25` | 1,750,000.00 USD | 0.00 USD | 1,870.00 USD | `-18.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.27` | 1,750,000.00 USD | 0.00 USD | 104.81 USD | `-18.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.27` | 1,750,000.00 USD | 0.00 USD | 200.10 USD | `-18.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.29` | 1,750,000.00 USD | 0.00 USD | 1,480.00 USD | `-17.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.29` | 1,750,000.00 USD | 0.00 USD | 1,870.00 USD | `-17.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.31` | 1,750,000.00 USD | 0.00 USD | 18,500.00 USD | `-17.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.31` | 1,730,000.00 USD | 0.00 USD | 405.09 USD | `-17.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.33` | 1,730,000.00 USD | 0.00 USD | 629.75 USD | `-16.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.33` | 1,730,000.00 USD | 0.00 USD | 6,750.00 USD | `-16.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.35` | 1,720,000.00 USD | 0.00 USD | 505.76 USD | `-16.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.37` | 1,720,000.00 USD | 0.00 USD | 73,220.00 USD | `-15.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.38` | 1,650,000.00 USD | 0.00 USD | 20,860.00 USD | `-15.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.40` | 1,630,000.00 USD | 0.00 USD | 8,490.00 USD | `-15.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.40` | 1,620,000.00 USD | 0.00 USD | 17,050.00 USD | `-14.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.42` | 1,600,000.00 USD | 0.00 USD | 271.15 USD | `-14.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.42` | 1,600,000.00 USD | 0.00 USD | 506.22 USD | `-14.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.44` | 1,600,000.00 USD | 0.00 USD | 171.75 USD | `-14.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.44` | 1,600,000.00 USD | 0.00 USD | 2,550.00 USD | `-13.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.46` | 1,600,000.00 USD | 0.00 USD | 2,270.00 USD | `-13.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.46` | 1,590,000.00 USD | 0.00 USD | 344.07 USD | `-13.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.48` | 1,590,000.00 USD | 0.00 USD | 156.83 USD | `-12.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.50` | 1,590,000.00 USD | 0.00 USD | 894.72 USD | `-12.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.50` | 1,590,000.00 USD | 0.00 USD | 139,820.00 USD | `-12.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.52` | 1,450,000.00 USD | 0.00 USD | 21,320.00 USD | `-12.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.52` | 1,430,000.00 USD | 0.00 USD | 3,700.00 USD | `-11.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.54` | 1,430,000.00 USD | 0.00 USD | 16,250.00 USD | `-11.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.54` | 1,410,000.00 USD | 0.00 USD | 5,130.00 USD | `-11.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.56` | 1,410,000.00 USD | 0.00 USD | 17,420.00 USD | `-11.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.56` | 1,390,000.00 USD | 0.00 USD | 18,440.00 USD | `-10.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.58` | 1,370,000.00 USD | 0.00 USD | 78,170.00 USD | `-10.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.58` | 1,290,000.00 USD | 0.00 USD | 1,250.00 USD | `-10.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.60` | 1,290,000.00 USD | 0.00 USD | 331.46 USD | `-10.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.60` | 1,290,000.00 USD | 0.00 USD | 15,710.00 USD | `-9.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.62` | 1,280,000.00 USD | 0.00 USD | 632.99 USD | `-9.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.62` | 1,280,000.00 USD | 0.00 USD | 172.19 USD | `-9.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.63` | 1,270,000.00 USD | 0.00 USD | 14,810.00 USD | `-9.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.65` | 1,260,000.00 USD | 0.00 USD | 179.33 USD | `-8.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.65` | 1,260,000.00 USD | 0.00 USD | 4,080.00 USD | `-8.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.67` | 1,260,000.00 USD | 0.00 USD | 3,180.00 USD | `-8.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.67` | 1,250,000.00 USD | 0.00 USD | 367.50 USD | `-8.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.69` | 1,250,000.00 USD | 0.00 USD | 39,580.00 USD | `-7.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.69` | 1,210,000.00 USD | 0.00 USD | 4,370.00 USD | `-7.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.71` | 1,210,000.00 USD | 0.00 USD | 234,410.00 USD | `-7.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.71` | 973,900.00 USD | 0.00 USD | 6,300.00 USD | `-7.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.73` | 967,600.00 USD | 0.00 USD | 2,490.00 USD | `-6.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.73` | 965,100.00 USD | 0.00 USD | 32,040.00 USD | `-6.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.75` | 933,060.00 USD | 0.00 USD | 28,820.00 USD | `-6.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.75` | 904,240.00 USD | 0.00 USD | 33,010.00 USD | `-6.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.77` | 871,240.00 USD | 0.00 USD | 183,980.00 USD | `-5.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.77` | 687,250.00 USD | 0.00 USD | 1,510.00 USD | `-5.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.79` | 685,740.00 USD | 0.00 USD | 183.19 USD | `-5.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.79` | 685,560.00 USD | 0.00 USD | 181,010.00 USD | `-5.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.81` | 504,550.00 USD | 0.00 USD | 8,230.00 USD | `-4.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.81` | 496,310.00 USD | 0.00 USD | 22,340.00 USD | `-4.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.83` | 473,970.00 USD | 0.00 USD | 63,260.00 USD | `-4.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.83` | 410,710.00 USD | 0.00 USD | 4,900.00 USD | `-4.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.85` | 405,810.00 USD | 0.00 USD | 43,780.00 USD | `-3.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.85` | 362,030.00 USD | 0.00 USD | 23,560.00 USD | `-3.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.87` | 338,470.00 USD | 0.00 USD | 8,900.00 USD | `-3.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.88` | 329,570.00 USD | 0.00 USD | 161,220.00 USD | `-3.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.88` | 168,350.00 USD | 0.00 USD | 31,620.00 USD | `-2.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.90` | 136,740.00 USD | 0.00 USD | 7,770.00 USD | `-2.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.90` | 128,970.00 USD | 0.00 USD | 65,680.00 USD | `-2.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.92` | 63,290.00 USD | 0.00 USD | 841.73 USD | `-2.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.92` | 62,450.00 USD | 0.00 USD | 5,190.00 USD | `-1.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.94` | 57,260.00 USD | 0.00 USD | 2,230.00 USD | `-1.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.94` | 55,030.00 USD | 0.00 USD | 6,990.00 USD | `-1.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.96` | 48,040.00 USD | 0.00 USD | 338.15 USD | `-1.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.96` | 47,700.00 USD | 0.00 USD | 170.89 USD | `-0.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.98` | 47,530.00 USD | 0.00 USD | 4,930.00 USD | `-0.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.98` | 42,610.00 USD | 0.00 USD | 100.42 USD | `-0.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.00` | 42,510.00 USD | 0.00 USD | 42,510.00 USD | `-0.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.00` | 298.37 USD | 298.37 USD | 0.00 USD | `+0.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.01` | 14,440.00 USD | 14,140.00 USD | 0.00 USD | `+0.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.03` | 24,030.00 USD | 9,590.00 USD | 0.00 USD | `+0.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.04` | 128,420.00 USD | 104,400.00 USD | 0.00 USD | `+0.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.04` | 130,200.00 USD | 1,780.00 USD | 0.00 USD | `+1.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.05` | 610,010.00 USD | 479,800.00 USD | 0.00 USD | `+1.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.07` | 610,120.00 USD | 113.41 USD | 0.00 USD | `+1.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.08` | 611,410.00 USD | 1,290.00 USD | 0.00 USD | `+1.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.08` | 650,010.00 USD | 38,600.00 USD | 0.00 USD | `+2.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.09` | 652,180.00 USD | 2,170.00 USD | 0.00 USD | `+2.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.11` | 849,550.00 USD | 197,370.00 USD | 0.00 USD | `+2.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.12` | 865,380.00 USD | 15,840.00 USD | 0.00 USD | `+2.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.12` | 865,650.00 USD | 265.65 USD | 0.00 USD | `+3.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.13` | 887,050.00 USD | 21,400.00 USD | 0.00 USD | `+3.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.14` | 888,020.00 USD | 968.27 USD | 0.00 USD | `+3.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.16` | 910,390.00 USD | 22,370.00 USD | 0.00 USD | `+3.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.17` | 1,160,000.00 USD | 254,600.00 USD | 0.00 USD | `+4.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.17` | 1,170,000.00 USD | 2,060.00 USD | 0.00 USD | `+4.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.18` | 1,170,000.00 USD | 557.02 USD | 0.00 USD | `+4.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.20` | 1,540,000.00 USD | 371,990.00 USD | 0.00 USD | `+4.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.21` | 1,600,000.00 USD | 58,520.00 USD | 0.00 USD | `+5.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.21` | 1,600,000.00 USD | 687.04 USD | 0.00 USD | `+5.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.22` | 1,600,000.00 USD | 3,890.00 USD | 0.00 USD | `+5.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.24` | 1,630,000.00 USD | 31,790.00 USD | 0.00 USD | `+5.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.25` | 1,640,000.00 USD | 2,200.00 USD | 0.00 USD | `+6.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.25` | 1,670,000.00 USD | 33,240.00 USD | 0.00 USD | `+6.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.26` | 1,670,000.00 USD | 2,180.00 USD | 0.00 USD | `+6.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.28` | 1,670,000.00 USD | 1,020.00 USD | 0.00 USD | `+6.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.29` | 1,680,000.00 USD | 4,290.00 USD | 0.00 USD | `+7.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.29` | 1,710,000.00 USD | 31,410.00 USD | 0.00 USD | `+7.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.30` | 1,760,000.00 USD | 47,870.00 USD | 0.00 USD | `+7.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.32` | 1,760,000.00 USD | 269.26 USD | 0.00 USD | `+7.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.33` | 1,760,000.00 USD | 2,420.00 USD | 0.00 USD | `+8.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.33` | 1,760,000.00 USD | 621.21 USD | 0.00 USD | `+8.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.34` | 1,780,000.00 USD | 17,380.00 USD | 0.00 USD | `+8.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.36` | 1,790,000.00 USD | 14,710.00 USD | 0.00 USD | `+8.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.37` | 1,790,000.00 USD | 464.00 USD | 0.00 USD | `+9.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.38` | 1,820,000.00 USD | 25,510.00 USD | 0.00 USD | `+9.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.38` | 1,890,000.00 USD | 71,900.00 USD | 0.00 USD | `+9.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.39` | 1,890,000.00 USD | 538.39 USD | 0.00 USD | `+9.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.41` | 2,290,000.00 USD | 404,370.00 USD | 0.00 USD | `+10.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.42` | 2,310,000.00 USD | 13,130.00 USD | 0.00 USD | `+10.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.42` | 2,310,000.00 USD | 4,090.00 USD | 0.00 USD | `+10.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.43` | 2,310,000.00 USD | 301.58 USD | 0.00 USD | `+10.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.45` | 2,310,000.00 USD | 889.00 USD | 0.00 USD | `+11.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.46` | 2,380,000.00 USD | 62,240.00 USD | 0.00 USD | `+11.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.46` | 2,380,000.00 USD | 2,360.00 USD | 0.00 USD | `+11.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.47` | 2,380,000.00 USD | 375.90 USD | 0.00 USD | `+11.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.49` | 2,380,000.00 USD | 133.20 USD | 0.00 USD | `+12.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.50` | 2,410,000.00 USD | 29,550.00 USD | 0.00 USD | `+12.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.50` | 3,170,000.00 USD | 762,970.00 USD | 0.00 USD | `+12.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.51` | 3,180,000.00 USD | 13,100.00 USD | 0.00 USD | `+12.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.53` | 3,240,000.00 USD | 52,300.00 USD | 0.00 USD | `+13.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.54` | 3,240,000.00 USD | 3,390.00 USD | 0.00 USD | `+13.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.54` | 3,240,000.00 USD | 2,270.00 USD | 0.00 USD | `+13.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.55` | 3,240,000.00 USD | 1,190.00 USD | 0.00 USD | `+13.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.57` | 3,240,000.00 USD | 227.79 USD | 0.00 USD | `+14.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.58` | 3,290,000.00 USD | 45,750.00 USD | 0.00 USD | `+14.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.58` | 3,290,000.00 USD | 1,150.00 USD | 0.00 USD | `+14.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.59` | 3,310,000.00 USD | 17,590.00 USD | 0.00 USD | `+14.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.61` | 3,310,000.00 USD | 2,950.00 USD | 0.00 USD | `+15.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.62` | 3,310,000.00 USD | 289.82 USD | 0.00 USD | `+15.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.62` | 3,310,000.00 USD | 3,670.00 USD | 0.00 USD | `+15.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.63` | 3,320,000.00 USD | 1,100.00 USD | 0.00 USD | `+15.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.64` | 3,320,000.00 USD | 739.02 USD | 0.00 USD | `+16.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.66` | 3,360,000.00 USD | 44,520.00 USD | 0.00 USD | `+16.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.67` | 3,380,000.00 USD | 16,750.00 USD | 0.00 USD | `+16.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.67` | 3,380,000.00 USD | 617.10 USD | 0.00 USD | `+16.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.68` | 3,390,000.00 USD | 15,710.00 USD | 0.00 USD | `+17.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.70` | 3,390,000.00 USD | 152.12 USD | 0.00 USD | `+17.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.71` | 3,750,000.00 USD | 357,810.00 USD | 0.00 USD | `+17.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.71` | 3,970,000.00 USD | 217,980.00 USD | 0.00 USD | `+17.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.72` | 3,970,000.00 USD | 2,650.00 USD | 0.00 USD | `+18.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.74` | 4,060,000.00 USD | 84,180.00 USD | 0.00 USD | `+18.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.75` | 4,060,000.00 USD | 6,160.00 USD | 0.00 USD | `+18.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.75` | 4,110,000.00 USD | 51,120.00 USD | 0.00 USD | `+18.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.76` | 4,130,000.00 USD | 13,030.00 USD | 0.00 USD | `+19.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.78` | 4,130,000.00 USD | 2,640.00 USD | 0.00 USD | `+19.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.79` | 4,960,000.00 USD | 832,330.00 USD | 0.00 USD | `+19.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.79` | 4,960,000.00 USD | 559.58 USD | 0.00 USD | `+19.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.80` | 5,140,000.00 USD | 177,030.00 USD | 0.00 USD | `+20.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.82` | 5,160,000.00 USD | 20,720.00 USD | 0.00 USD | `+20.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.83` | 5,170,000.00 USD | 8,540.00 USD | 0.00 USD | `+20.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.83` | 5,170,000.00 USD | 283.33 USD | 0.00 USD | `+20.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.84` | 5,180,000.00 USD | 11,760.00 USD | 0.00 USD | `+21.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.86` | 5,210,000.00 USD | 24,370.00 USD | 0.00 USD | `+21.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.87` | 5,230,000.00 USD | 22,170.00 USD | 0.00 USD | `+21.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.88` | 5,240,000.00 USD | 10,400.00 USD | 0.00 USD | `+21.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.88` | 5,260,000.00 USD | 19,890.00 USD | 0.00 USD | `+22.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.89` | 5,260,000.00 USD | 4,060.00 USD | 0.00 USD | `+22.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.91` | 5,390,000.00 USD | 125,180.00 USD | 0.00 USD | `+22.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.92` | 5,390,000.00 USD | 156.30 USD | 0.00 USD | `+22.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.92` | 5,400,000.00 USD | 13,180.00 USD | 0.00 USD | `+23.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.93` | 5,400,000.00 USD | 4,420.00 USD | 0.00 USD | `+23.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.95` | 5,410,000.00 USD | 313.51 USD | 0.00 USD | `+23.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.96` | 5,410,000.00 USD | 5,070.00 USD | 0.00 USD | `+23.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.96` | 5,460,000.00 USD | 47,350.00 USD | 0.00 USD | `+24.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.97` | 5,460,000.00 USD | 187.06 USD | 0.00 USD | `+24.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.99` | 5,550,000.00 USD | 92,570.00 USD | 0.00 USD | `+24.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.00` | 5,550,000.00 USD | 2,540.00 USD | 0.00 USD | `+24.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.00` | 5,590,000.00 USD | 41,580.00 USD | 0.00 USD | `+25.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.01` | 5,620,000.00 USD | 25,080.00 USD | 0.00 USD | `+25.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.03` | 5,620,000.00 USD | 5,030.00 USD | 0.00 USD | `+25.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.04` | 5,640,000.00 USD | 19,640.00 USD | 0.00 USD | `+25.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.04` | 5,640,000.00 USD | 120.58 USD | 0.00 USD | `+26.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.05` | 5,660,000.00 USD | 14,440.00 USD | 0.00 USD | `+26.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.07` | 5,660,000.00 USD | 6,090.00 USD | 0.00 USD | `+26.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.08` | 5,750,000.00 USD | 87,290.00 USD | 0.00 USD | `+26.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.08` | 5,760,000.00 USD | 5,460.00 USD | 0.00 USD | `+27.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.09` | 5,760,000.00 USD | 178.33 USD | 0.00 USD | `+27.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.11` | 5,830,000.00 USD | 68,210.00 USD | 0.00 USD | `+27.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.12` | 5,840,000.00 USD | 17,900.00 USD | 0.00 USD | `+27.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.12` | 5,840,000.00 USD | 179.38 USD | 0.00 USD | `+28.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.13` | 5,840,000.00 USD | 179.72 USD | 0.00 USD | `+28.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.14` | 5,840,000.00 USD | 217.63 USD | 0.00 USD | `+28.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.16` | 5,850,000.00 USD | 493.85 USD | 0.00 USD | `+28.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.17` | 5,850,000.00 USD | 575.38 USD | 0.00 USD | `+29.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.17` | 5,850,000.00 USD | 327.58 USD | 0.00 USD | `+29.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.18` | 5,850,000.00 USD | 163.85 USD | 0.00 USD | `+29.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.20` | 5,970,000.00 USD | 120,930.00 USD | 0.00 USD | `+29.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.21` | 6,010,000.00 USD | 38,230.00 USD | 0.00 USD | `+30.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.21` | 6,010,000.00 USD | 1,710.00 USD | 0.00 USD | `+30.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.22` | 6,010,000.00 USD | 432.63 USD | 0.00 USD | `+30.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.24` | 6,010,000.00 USD | 2,620.00 USD | 0.00 USD | `+30.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.25` | 6,010,000.00 USD | 537.61 USD | 0.00 USD | `+31.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.25` | 6,430,000.00 USD | 420,400.00 USD | 0.00 USD | `+31.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.26` | 6,430,000.00 USD | 278.52 USD | 0.00 USD | `+31.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.28` | 6,430,000.00 USD | 589.22 USD | 0.00 USD | `+31.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.29` | 6,430,000.00 USD | 733.03 USD | 0.00 USD | `+32.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.29` | 6,430,000.00 USD | 423.60 USD | 0.00 USD | `+32.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.30` | 6,440,000.00 USD | 10,930.00 USD | 0.00 USD | `+32.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.32` | 6,440,000.00 USD | 381.09 USD | 0.00 USD | `+32.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.33` | 6,450,000.00 USD | 961.16 USD | 0.00 USD | `+33.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.33` | 6,450,000.00 USD | 1,570.00 USD | 0.00 USD | `+33.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.34` | 6,450,000.00 USD | 5,650.00 USD | 0.00 USD | `+33.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.36` | 6,450,000.00 USD | 160.11 USD | 0.00 USD | `+33.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.37` | 6,450,000.00 USD | 225.33 USD | 0.00 USD | `+34.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.38` | 6,450,000.00 USD | 438.60 USD | 0.00 USD | `+34.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.38` | 6,460,000.00 USD | 4,840.00 USD | 0.00 USD | `+34.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.39` | 6,500,000.00 USD | 40,880.00 USD | 0.00 USD | `+34.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.41` | 6,520,000.00 USD | 17,160.00 USD | 0.00 USD | `+35.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.42` | 6,520,000.00 USD | 270.75 USD | 0.00 USD | `+35.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.42` | 6,520,000.00 USD | 639.61 USD | 0.00 USD | `+35.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.43` | 6,520,000.00 USD | 1,710.00 USD | 0.00 USD | `+35.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.45` | 6,530,000.00 USD | 12,600.00 USD | 0.00 USD | `+36.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.46` | 6,540,000.00 USD | 3,650.00 USD | 0.00 USD | `+36.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.46` | 6,730,000.00 USD | 192,640.00 USD | 0.00 USD | `+36.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.47` | 6,760,000.00 USD | 30,110.00 USD | 0.00 USD | `+36.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.49` | 6,800,000.00 USD | 38,920.00 USD | 0.00 USD | `+37.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.50` | 6,800,000.00 USD | 1,180.00 USD | 0.00 USD | `+37.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.50` | 6,860,000.00 USD | 62,490.00 USD | 0.00 USD | `+37.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.51` | 6,870,000.00 USD | 5,600.00 USD | 0.00 USD | `+37.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.53` | 6,890,000.00 USD | 19,110.00 USD | 0.00 USD | `+38.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.54` | 6,900,000.00 USD | 18,790.00 USD | 0.00 USD | `+38.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.54` | 6,960,000.00 USD | 58,030.00 USD | 0.00 USD | `+38.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.55` | 7,010,000.00 USD | 46,450.00 USD | 0.00 USD | `+38.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.57` | 7,020,000.00 USD | 14,320.00 USD | 0.00 USD | `+39.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.58` | 7,030,000.00 USD | 10,390.00 USD | 0.00 USD | `+39.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.58` | 7,050,000.00 USD | 20,540.00 USD | 0.00 USD | `+39.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.59` | 7,050,000.00 USD | 384.94 USD | 0.00 USD | `+39.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.61` | 7,050,000.00 USD | 573.39 USD | 0.00 USD | `+40.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.62` | 7,060,000.00 USD | 2,190.00 USD | 0.00 USD | `+40.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.63` | 7,060,000.00 USD | 581.53 USD | 0.00 USD | `+40.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.64` | 7,060,000.00 USD | 491.11 USD | 0.00 USD | `+41.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.66` | 7,060,000.00 USD | 3,290.00 USD | 0.00 USD | `+41.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.67` | 7,060,000.00 USD | 281.55 USD | 0.00 USD | `+41.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.67` | 7,070,000.00 USD | 6,590.00 USD | 0.00 USD | `+41.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.68` | 7,070,000.00 USD | 235.93 USD | 0.00 USD | `+42.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.70` | 7,070,000.00 USD | 5,860.00 USD | 0.00 USD | `+42.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.71` | 7,180,000.00 USD | 103,470.00 USD | 0.00 USD | `+42.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.71` | 7,180,000.00 USD | 705.23 USD | 0.00 USD | `+42.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.72` | 7,180,000.00 USD | 5,720.00 USD | 0.00 USD | `+43.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.75` | 7,180,000.00 USD | 139.03 USD | 0.00 USD | `+43.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.75` | 7,190,000.00 USD | 2,450.00 USD | 0.00 USD | `+43.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.76` | 7,190,000.00 USD | 2,430.00 USD | 0.00 USD | `+44.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.78` | 7,190,000.00 USD | 1,850.00 USD | 0.00 USD | `+44.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.79` | 7,190,000.00 USD | 286.94 USD | 0.00 USD | `+44.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.80` | 7,200,000.00 USD | 7,120.00 USD | 0.00 USD | `+45.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.82` | 7,200,000.00 USD | 329.13 USD | 0.00 USD | `+45.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.83` | 7,200,000.00 USD | 1,970.00 USD | 0.00 USD | `+45.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.83` | 7,200,000.00 USD | 1,020.00 USD | 0.00 USD | `+45.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.84` | 7,200,000.00 USD | 1,150.00 USD | 0.00 USD | `+46.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.86` | 7,200,000.00 USD | 1,190.00 USD | 0.00 USD | `+46.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.87` | 7,210,000.00 USD | 1,770.00 USD | 0.00 USD | `+46.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.88` | 7,210,000.00 USD | 3,450.00 USD | 0.00 USD | `+46.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.88` | 7,210,000.00 USD | 345.45 USD | 0.00 USD | `+47.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.91` | 7,270,000.00 USD | 65,350.00 USD | 0.00 USD | `+47.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.92` | 7,280,000.00 USD | 2,510.00 USD | 0.00 USD | `+47.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.92` | 7,280,000.00 USD | 1,020.00 USD | 0.00 USD | `+48.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.93` | 7,430,000.00 USD | 153,150.00 USD | 0.00 USD | `+48.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.96` | 7,460,000.00 USD | 26,180.00 USD | 0.00 USD | `+48.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.96` | 7,460,000.00 USD | 5,440.00 USD | 0.00 USD | `+49.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.97` | 7,470,000.00 USD | 8,940.00 USD | 0.00 USD | `+49.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.99` | 7,590,000.00 USD | 119,340.00 USD | 0.00 USD | `+49.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.00` | 7,590,000.00 USD | 3,000.00 USD | 0.00 USD | `+49.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.00` | 7,800,000.00 USD | 208,340.00 USD | 0.00 USD | `+50.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.01` | 7,820,000.00 USD | 13,710.00 USD | 0.00 USD | `+50.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.03` | 7,910,000.00 USD | 90,380.00 USD | 0.00 USD | `+50.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.04` | 7,910,000.00 USD | 2,170.00 USD | 0.00 USD | `+50.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.04` | 7,910,000.00 USD | 3,300.00 USD | 0.00 USD | `+51.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.05` | 7,910,000.00 USD | 1,040.00 USD | 0.00 USD | `+51.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.07` | 7,910,000.00 USD | 425.76 USD | 0.00 USD | `+51.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.08` | 7,920,000.00 USD | 2,030.00 USD | 0.00 USD | `+51.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.08` | 7,920,000.00 USD | 4,120.00 USD | 0.00 USD | `+52.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.09` | 7,920,000.00 USD | 2,000.00 USD | 0.00 USD | `+52.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.11` | 7,980,000.00 USD | 61,050.00 USD | 0.00 USD | `+52.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.12` | 7,980,000.00 USD | 1,610.00 USD | 0.00 USD | `+52.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.13` | 7,990,000.00 USD | 1,200.00 USD | 0.00 USD | `+53.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.14` | 7,990,000.00 USD | 420.32 USD | 0.00 USD | `+53.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.16` | 7,990,000.00 USD | 1,940.00 USD | 0.00 USD | `+53.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.17` | 7,990,000.00 USD | 4,010.00 USD | 0.00 USD | `+54.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.18` | 8,000,000.00 USD | 3,960.00 USD | 0.00 USD | `+54.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.21` | 8,060,000.00 USD | 66,060.00 USD | 0.00 USD | `+55.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.21` | 8,060,000.00 USD | 1,890.00 USD | 0.00 USD | `+55.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.22` | 8,060,000.00 USD | 195.46 USD | 0.00 USD | `+55.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.24` | 8,070,000.00 USD | 1,540.00 USD | 0.00 USD | `+55.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.25` | 8,070,000.00 USD | 116.16 USD | 0.00 USD | `+56.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.30` | 8,070,000.00 USD | 7,310.00 USD | 0.00 USD | `+57.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.32` | 8,070,000.00 USD | 310.70 USD | 0.00 USD | `+57.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.33` | 8,070,000.00 USD | 325.62 USD | 0.00 USD | `+58.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.36` | 8,080,000.00 USD | 1,760.00 USD | 0.00 USD | `+58.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.38` | 8,080,000.00 USD | 3,560.00 USD | 0.00 USD | `+59.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.39` | 8,080,000.00 USD | 3,230.00 USD | 0.00 USD | `+59.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.41` | 8,090,000.00 USD | 5,120.00 USD | 0.00 USD | `+60.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.43` | 8,090,000.00 USD | 613.26 USD | 0.00 USD | `+60.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.50` | 8,090,000.00 USD | 1,310.00 USD | 0.00 USD | `+62.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.50` | 8,120,000.00 USD | 30,990.00 USD | 0.00 USD | `+62.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.51` | 8,120,000.00 USD | 104.24 USD | 0.00 USD | `+62.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.54` | 8,130,000.00 USD | 13,580.00 USD | 0.00 USD | `+63.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.58` | 8,140,000.00 USD | 1,630.00 USD | 0.00 USD | `+64.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.59` | 8,140,000.00 USD | 1,370.00 USD | 0.00 USD | `+64.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.61` | 8,140,000.00 USD | 3,540.00 USD | 0.00 USD | `+65.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.62` | 8,140,000.00 USD | 1,620.00 USD | 0.00 USD | `+65.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.64` | 8,150,000.00 USD | 3,220.00 USD | 0.00 USD | `+66.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.67` | 8,150,000.00 USD | 450.55 USD | 0.00 USD | `+66.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.67` | 8,150,000.00 USD | 3,060.00 USD | 0.00 USD | `+66.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.71` | 8,150,000.00 USD | 3,070.00 USD | 0.00 USD | `+67.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.74` | 8,160,000.00 USD | 3,120.00 USD | 0.00 USD | `+68.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.75` | 8,160,000.00 USD | 1,550.00 USD | 0.00 USD | `+68.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.78` | 8,160,000.00 USD | 3,080.00 USD | 0.00 USD | `+69.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.79` | 8,160,000.00 USD | 647.56 USD | 0.00 USD | `+69.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.80` | 8,160,000.00 USD | 1,420.00 USD | 0.00 USD | `+70.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.82` | 8,160,000.00 USD | 2,130.00 USD | 0.00 USD | `+70.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.83` | 8,170,000.00 USD | 6,870.00 USD | 0.00 USD | `+70.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.84` | 8,170,000.00 USD | 342.25 USD | 0.00 USD | `+71.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.87` | 8,170,000.00 USD | 2,990.00 USD | 0.00 USD | `+71.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.89` | 8,180,000.00 USD | 2,970.00 USD | 0.00 USD | `+72.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.91` | 8,180,000.00 USD | 324.54 USD | 0.00 USD | `+72.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.95` | 8,180,000.00 USD | 504.21 USD | 0.00 USD | `+73.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.97` | 8,180,000.00 USD | 166.00 USD | 0.00 USD | `+74.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.99` | 8,180,000.00 USD | 4,190.00 USD | 0.00 USD | `+74.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.00` | 8,200,000.00 USD | 12,970.00 USD | 0.00 USD | `+75.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.01` | 8,200,000.00 USD | 1,750.00 USD | 0.00 USD | `+75.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.04` | 8,200,000.00 USD | 2,860.00 USD | 0.00 USD | `+76.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.11` | 8,200,000.00 USD | 264.31 USD | 0.00 USD | `+77.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.13` | 8,200,000.00 USD | 599.34 USD | 0.00 USD | `+78.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.16` | 8,200,000.00 USD | 193.19 USD | 0.00 USD | `+78.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.18` | 8,210,000.00 USD | 3,950.00 USD | 0.00 USD | `+79.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.21` | 8,210,000.00 USD | 1,940.00 USD | 0.00 USD | `+80.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.25` | 8,370,000.00 USD | 160,550.00 USD | 0.00 USD | `+81.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.28` | 8,370,000.00 USD | 1,290.00 USD | 0.00 USD | `+81.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.32` | 8,370,000.00 USD | 1,180.00 USD | 0.00 USD | `+82.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.39` | 8,370,000.00 USD | 630.05 USD | 0.00 USD | `+84.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.41` | 8,370,000.00 USD | 1,410.00 USD | 0.00 USD | `+85.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.42` | 8,370,000.00 USD | 2,610.00 USD | 0.00 USD | `+85.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.50` | 8,380,000.00 USD | 6,000.00 USD | 0.00 USD | `+87.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.58` | 8,390,000.00 USD | 4,640.00 USD | 0.00 USD | `+89.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.61` | 8,390,000.00 USD | 371.88 USD | 0.00 USD | `+90.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.62` | 8,390,000.00 USD | 2,510.00 USD | 0.00 USD | `+90.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.67` | 8,390,000.00 USD | 380.68 USD | 0.00 USD | `+91.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.76` | 8,390,000.00 USD | 1,490.00 USD | 0.00 USD | `+94.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.78` | 8,390,000.00 USD | 1,470.00 USD | 0.00 USD | `+94.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.79` | 8,400,000.00 USD | 11,170.00 USD | 0.00 USD | `+94.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.80` | 8,440,000.00 USD | 34,360.00 USD | 0.00 USD | `+95.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.82` | 8,440,000.00 USD | 253.21 USD | 0.00 USD | `+95.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.83` | 8,440,000.00 USD | 100.29 USD | 0.00 USD | `+95.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.88` | 8,440,000.00 USD | 1,550.00 USD | 0.00 USD | `+96.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.96` | 8,450,000.00 USD | 10,610.00 USD | 0.00 USD | `+99.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.97` | 8,450,000.00 USD | 309.43 USD | 0.00 USD | `+99.40%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `3.59` | 12,300,000.00 USD | 0.00 USD | 12,300,000.00 USD | 176,290.00 USD | 66,810.00 USD | 144,570.00 USD |
| `7D` | `3.60` | 11,920,000.00 USD | 0.00 USD | 11,920,000.00 USD | 64,170.00 USD | 21,460.00 USD | 22,050.00 USD |
| `7D` | `3.61` | 11,810,000.00 USD | 0.00 USD | 11,810,000.00 USD | 55,130.00 USD | 17,400.00 USD | 44,890.00 USD |
| `7D` | `3.62` | 11,690,000.00 USD | 0.00 USD | 11,690,000.00 USD | 92,130.00 USD | 26,640.00 USD | 97,570.00 USD |
| `1D` | `3.63` | 5,930,000.00 USD | 0.00 USD | 5,930,000.00 USD | 1,910.00 USD | 9,650.00 USD | 22,610.00 USD |
| `7D` | `3.63` | 11,480,000.00 USD | 0.00 USD | 11,480,000.00 USD | 50,840.00 USD | 8,120.00 USD | 159.02 USD |
| `1D` | `3.64` | 5,900,000.00 USD | 0.00 USD | 5,900,000.00 USD | 152.80 USD | 5,040.00 USD | 0.00 USD |
| `7D` | `3.64` | 11,420,000.00 USD | 0.00 USD | 11,420,000.00 USD | 2,410.00 USD | 14,370.00 USD | 119,140.00 USD |
| `1D` | `3.65` | 5,890,000.00 USD | 0.00 USD | 5,890,000.00 USD | 386.30 USD | 0.00 USD | 13.37 USD |
| `7D` | `3.65` | 11,280,000.00 USD | 0.00 USD | 11,280,000.00 USD | 52,910.00 USD | 7,050.00 USD | 31,190.00 USD |
| `1D` | `3.66` | 5,890,000.00 USD | 0.00 USD | 5,890,000.00 USD | 291.38 USD | 0.00 USD | 0.00 USD |
| `7D` | `3.66` | 11,190,000.00 USD | 0.00 USD | 11,190,000.00 USD | 30,480.00 USD | 15,090.00 USD | 125,270.00 USD |
| `1D` | `3.67` | 5,890,000.00 USD | 0.00 USD | 5,890,000.00 USD | 16,750.00 USD | 3,070.00 USD | 11,520.00 USD |
| `7D` | `3.67` | 11,020,000.00 USD | 0.00 USD | 11,020,000.00 USD | 47,650.00 USD | 14,480.00 USD | 53,670.00 USD |
| `1D` | `3.68` | 5,860,000.00 USD | 0.00 USD | 5,860,000.00 USD | 216.77 USD | 0.00 USD | 0.00 USD |
| `1D` | `3.69` | 5,860,000.00 USD | 0.00 USD | 5,860,000.00 USD | 23,960.00 USD | 0.00 USD | 281.19 USD |
| `7D` | `3.69` | 10,900,000.00 USD | 0.00 USD | 10,900,000.00 USD | 27,750.00 USD | 0.00 USD | 59,840.00 USD |
| `1D` | `3.70` | 5,840,000.00 USD | 0.00 USD | 5,840,000.00 USD | 39,190.00 USD | 4,110.00 USD | 55,010.00 USD |
| `7D` | `3.70` | 10,820,000.00 USD | 0.00 USD | 10,820,000.00 USD | 20,470.00 USD | 7,370.00 USD | 112,470.00 USD |
| `1D` | `3.71` | 5,740,000.00 USD | 0.00 USD | 5,740,000.00 USD | 430.40 USD | 0.00 USD | 522.93 USD |
| `7D` | `3.71` | 10,680,000.00 USD | 0.00 USD | 10,680,000.00 USD | 50,620.00 USD | 0.00 USD | 74,330.00 USD |
| `1D` | `3.72` | 5,740,000.00 USD | 0.00 USD | 5,740,000.00 USD | 403.05 USD | 0.00 USD | 18.60 USD |
| `7D` | `3.72` | 10,550,000.00 USD | 0.00 USD | 10,550,000.00 USD | 425.03 USD | 0.00 USD | 183.06 USD |
| `1D` | `3.73` | 5,740,000.00 USD | 0.00 USD | 5,740,000.00 USD | 8,890.00 USD | 6,020.00 USD | 8,370.00 USD |
| `7D` | `3.73` | 10,550,000.00 USD | 0.00 USD | 10,550,000.00 USD | 38,260.00 USD | 10,880.00 USD | 56,790.00 USD |
| `1D` | `3.74` | 5,710,000.00 USD | 0.00 USD | 5,710,000.00 USD | 94,200.00 USD | 33,110.00 USD | 42,360.00 USD |
| `7D` | `3.74` | 10,440,000.00 USD | 0.00 USD | 10,440,000.00 USD | 128,440.00 USD | 40,020.00 USD | 122,480.00 USD |
| `1D` | `3.75` | 5,540,000.00 USD | 0.00 USD | 5,540,000.00 USD | 0.00 USD | 0.00 USD | 20,450.00 USD |
| `7D` | `3.75` | 10,150,000.00 USD | 0.00 USD | 10,150,000.00 USD | 1,770.00 USD | 24,350.00 USD | 42,760.00 USD |
| `1D` | `3.76` | 5,520,000.00 USD | 0.00 USD | 5,520,000.00 USD | 0.00 USD | 2,230.00 USD | 10,030.00 USD |
| `7D` | `3.76` | 10,080,000.00 USD | 0.00 USD | 10,080,000.00 USD | 32,650.00 USD | 10,110.00 USD | 22,610.00 USD |
| `1D` | `3.77` | 5,510,000.00 USD | 0.00 USD | 5,510,000.00 USD | 187.12 USD | 5,330.00 USD | 2,020.00 USD |
| `7D` | `3.77` | 10,020,000.00 USD | 0.00 USD | 10,020,000.00 USD | 13,170.00 USD | 8,090.00 USD | 23,020.00 USD |
| `1D` | `3.78` | 5,500,000.00 USD | 0.00 USD | 5,500,000.00 USD | 106.91 USD | 4,490.00 USD | 29,810.00 USD |
| `7D` | `3.78` | 9,970,000.00 USD | 0.00 USD | 9,970,000.00 USD | 21,640.00 USD | 15,520.00 USD | 41,570.00 USD |
| `1D` | `3.79` | 5,470,000.00 USD | 0.00 USD | 5,470,000.00 USD | 472.79 USD | 0.00 USD | 176.51 USD |
| `7D` | `3.79` | 9,900,000.00 USD | 0.00 USD | 9,900,000.00 USD | 49,420.00 USD | 0.00 USD | 38,980.00 USD |
| `1D` | `3.80` | 5,470,000.00 USD | 0.00 USD | 5,470,000.00 USD | 1,270.00 USD | 0.00 USD | 1,720.00 USD |
| `7D` | `3.80` | 9,810,000.00 USD | 0.00 USD | 9,810,000.00 USD | 1,530.00 USD | 18,170.00 USD | 17,780.00 USD |
| `1D` | `3.81` | 5,470,000.00 USD | 0.00 USD | 5,470,000.00 USD | 54,290.00 USD | 0.00 USD | 13,100.00 USD |
| `7D` | `3.81` | 9,770,000.00 USD | 0.00 USD | 9,770,000.00 USD | 0.00 USD | 0.00 USD | 1,350.00 USD |
| `1D` | `3.82` | 5,400,000.00 USD | 0.00 USD | 5,400,000.00 USD | 487.48 USD | 11,960.00 USD | 0.00 USD |
| `7D` | `3.82` | 9,770,000.00 USD | 0.00 USD | 9,770,000.00 USD | 527.85 USD | 18,370.00 USD | 25,600.00 USD |
| `1D` | `3.83` | 5,390,000.00 USD | 0.00 USD | 5,390,000.00 USD | 1,150.00 USD | 18,900.00 USD | 17,280.00 USD |
| `7D` | `3.83` | 9,720,000.00 USD | 0.00 USD | 9,720,000.00 USD | 0.00 USD | 0.00 USD | 89.29 USD |
| `1D` | `3.84` | 5,350,000.00 USD | 0.00 USD | 5,350,000.00 USD | 0.00 USD | 0.00 USD | 784.00 USD |
| `7D` | `3.84` | 9,720,000.00 USD | 0.00 USD | 9,720,000.00 USD | 2,020.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `3.85` | 5,350,000.00 USD | 0.00 USD | 5,350,000.00 USD | 929.01 USD | 6,330.00 USD | 141.64 USD |
| `7D` | `3.85` | 9,720,000.00 USD | 0.00 USD | 9,720,000.00 USD | 0.00 USD | 0.00 USD | 5,500.00 USD |
| `1D` | `3.86` | 5,340,000.00 USD | 0.00 USD | 5,340,000.00 USD | 2,080.00 USD | 12,320.00 USD | 54,290.00 USD |
| `7D` | `3.86` | 9,720,000.00 USD | 0.00 USD | 9,720,000.00 USD | 2,220.00 USD | 0.00 USD | 72,520.00 USD |
| `1D` | `3.87` | 5,270,000.00 USD | 0.00 USD | 5,270,000.00 USD | 1,690.00 USD | 11,800.00 USD | 845.92 USD |
| `7D` | `3.87` | 9,640,000.00 USD | 0.00 USD | 9,640,000.00 USD | 57,040.00 USD | 0.00 USD | 29,890.00 USD |
| `1D` | `3.88` | 5,260,000.00 USD | 0.00 USD | 5,260,000.00 USD | 106,680.00 USD | 6,860.00 USD | 39,950.00 USD |
| `7D` | `3.88` | 9,550,000.00 USD | 0.00 USD | 9,550,000.00 USD | 106,950.00 USD | 8,890.00 USD | 101,810.00 USD |
| `1D` | `3.89` | 5,100,000.00 USD | 0.00 USD | 5,100,000.00 USD | 113,490.00 USD | 37,150.00 USD | 23,350.00 USD |
| `7D` | `3.89` | 9,340,000.00 USD | 0.00 USD | 9,340,000.00 USD | 1,210.00 USD | 50,710.00 USD | 1,390.00 USD |
| `1D` | `3.90` | 4,930,000.00 USD | 0.00 USD | 4,930,000.00 USD | 31,410.00 USD | 10,910.00 USD | 21,360.00 USD |
| `7D` | `3.90` | 9,280,000.00 USD | 0.00 USD | 9,280,000.00 USD | 171,750.00 USD | 28,250.00 USD | 51,570.00 USD |
| `1D` | `3.91` | 4,870,000.00 USD | 0.00 USD | 4,870,000.00 USD | 32,140.00 USD | 35,760.00 USD | 39,260.00 USD |
| `7D` | `3.91` | 9,030,000.00 USD | 0.00 USD | 9,030,000.00 USD | 3,970.00 USD | 25,680.00 USD | 46,930.00 USD |
| `1D` | `3.92` | 4,760,000.00 USD | 0.00 USD | 4,760,000.00 USD | 148,140.00 USD | 26,030.00 USD | 33,330.00 USD |
| `7D` | `3.92` | 8,960,000.00 USD | 0.00 USD | 8,960,000.00 USD | 90,780.00 USD | 41,330.00 USD | 89,160.00 USD |
| `1D` | `3.93` | 4,550,000.00 USD | 0.00 USD | 4,550,000.00 USD | 0.00 USD | 29,900.00 USD | 38,510.00 USD |
| `7D` | `3.93` | 8,730,000.00 USD | 0.00 USD | 8,730,000.00 USD | 51,660.00 USD | 20,780.00 USD | 19,870.00 USD |
| `1D` | `3.94` | 4,480,000.00 USD | 0.00 USD | 4,480,000.00 USD | 96,340.00 USD | 14,940.00 USD | 20,530.00 USD |
| `7D` | `3.94` | 8,640,000.00 USD | 0.00 USD | 8,640,000.00 USD | 82,440.00 USD | 31,050.00 USD | 96,310.00 USD |
| `1D` | `3.95` | 4,350,000.00 USD | 0.00 USD | 4,350,000.00 USD | 95,940.00 USD | 15,880.00 USD | 95,070.00 USD |
| `7D` | `3.95` | 8,430,000.00 USD | 0.00 USD | 8,430,000.00 USD | 8,490.00 USD | 19,870.00 USD | 2,700.00 USD |
| `1D` | `3.96` | 4,150,000.00 USD | 0.00 USD | 4,150,000.00 USD | 65,960.00 USD | 39,680.00 USD | 36,690.00 USD |
| `7D` | `3.96` | 8,400,000.00 USD | 0.00 USD | 8,400,000.00 USD | 166,560.00 USD | 15,590.00 USD | 312,280.00 USD |
| `1D` | `3.97` | 4,000,000.00 USD | 0.00 USD | 4,000,000.00 USD | 190,720.00 USD | 66,010.00 USD | 102,960.00 USD |
| `7D` | `3.97` | 7,910,000.00 USD | 0.00 USD | 7,910,000.00 USD | 231,790.00 USD | 102,960.00 USD | 271,360.00 USD |
| `1D` | `3.98` | 3,640,000.00 USD | 0.00 USD | 3,640,000.00 USD | 192,590.00 USD | 43,880.00 USD | 14,880.00 USD |
| `7D` | `3.98` | 7,300,000.00 USD | 0.00 USD | 7,300,000.00 USD | 295,470.00 USD | 147,090.00 USD | 230,240.00 USD |
| `1D` | `3.99` | 3,390,000.00 USD | 0.00 USD | 3,390,000.00 USD | 413,960.00 USD | 106,190.00 USD | 138,330.00 USD |
| `7D` | `3.99` | 6,630,000.00 USD | 0.00 USD | 6,630,000.00 USD | 63,200.00 USD | 103,210.00 USD | 78,470.00 USD |
| `1D` | `4.00` | 2,730,000.00 USD | 0.00 USD | 2,730,000.00 USD | 35,730.00 USD | 53,390.00 USD | 134,490.00 USD |
| `7D` | `4.00` | 6,380,000.00 USD | 0.00 USD | 6,380,000.00 USD | 317,210.00 USD | 126,990.00 USD | 166,390.00 USD |
| `1D` | `4.01` | 2,510,000.00 USD | 0.00 USD | 2,510,000.00 USD | 112,570.00 USD | 72,850.00 USD | 129,520.00 USD |
| `7D` | `4.01` | 5,770,000.00 USD | 0.00 USD | 5,770,000.00 USD | 392,150.00 USD | 94,720.00 USD | 438,650.00 USD |
| `1D` | `4.02` | 2,190,000.00 USD | 0.00 USD | 2,190,000.00 USD | 243,600.00 USD | 50,310.00 USD | 107,340.00 USD |
| `7D` | `4.02` | 4,850,000.00 USD | 0.00 USD | 4,850,000.00 USD | 279,800.00 USD | 88,330.00 USD | 250,940.00 USD |
| `1D` | `4.03` | 1,790,000.00 USD | 0.00 USD | 1,790,000.00 USD | 189,730.00 USD | 76,190.00 USD | 266,680.00 USD |
| `7D` | `4.03` | 4,230,000.00 USD | 0.00 USD | 4,230,000.00 USD | 250,870.00 USD | 45,290.00 USD | 147,160.00 USD |
| `1D` | `4.04` | 1,260,000.00 USD | 0.00 USD | 1,260,000.00 USD | 105,670.00 USD | 48,960.00 USD | 207,560.00 USD |
| `7D` | `4.04` | 3,780,000.00 USD | 0.00 USD | 3,780,000.00 USD | 326,350.00 USD | 65,670.00 USD | 491,840.00 USD |
| `1D` | `4.05` | 898,580.00 USD | 0.00 USD | 898,580.00 USD | 2,370.00 USD | 46,690.00 USD | 95,690.00 USD |
| `7D` | `4.05` | 2,900,000.00 USD | 0.00 USD | 2,900,000.00 USD | 291,930.00 USD | 117,530.00 USD | 85,640.00 USD |
| `1D` | `4.06` | 753,820.00 USD | 0.00 USD | 753,820.00 USD | 0.00 USD | 27,150.00 USD | 125,920.00 USD |
| `7D` | `4.06` | 2,410,000.00 USD | 0.00 USD | 2,410,000.00 USD | 305,310.00 USD | 72,410.00 USD | 187,820.00 USD |
| `1D` | `4.07` | 600,750.00 USD | 0.00 USD | 600,750.00 USD | 0.00 USD | 72,110.00 USD | 22,350.00 USD |
| `7D` | `4.07` | 1,840,000.00 USD | 0.00 USD | 1,840,000.00 USD | 715,320.00 USD | 219,920.00 USD | 329,160.00 USD |
| `1D` | `4.08` | 506,300.00 USD | 0.00 USD | 506,300.00 USD | 506,300.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4.08` | 575,150.00 USD | 0.00 USD | 575,150.00 USD | 9,180.00 USD | 117,780.00 USD | 229,680.00 USD |
| `7D` | `4.09` | 218,520.00 USD | 0.00 USD | 218,520.00 USD | 134,630.00 USD | 83,890.00 USD | 0.00 USD |
| `7D` | `4.10` | 143,210.00 USD | 143,210.00 USD | 0.00 USD | 24,900.00 USD | 118,310.00 USD | 0.00 USD |
| `7D` | `4.10` | 286,420.00 USD | 286,420.00 USD | 0.00 USD | 24,900.00 USD | 118,310.00 USD | 0.00 USD |
| `1D` | `4.11` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `4.12` | 309,660.00 USD | 309,660.00 USD | 0.00 USD | 0.00 USD | 80,980.00 USD | 228,680.00 USD |
| `1D` | `4.13` | 471,110.00 USD | 471,110.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 161,450.00 USD |
| `1D` | `4.14` | 531,130.00 USD | 531,130.00 USD | 0.00 USD | 60,020.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4.14` | 377,250.00 USD | 377,250.00 USD | 0.00 USD | 0.00 USD | 90,830.00 USD | 0.00 USD |
| `1D` | `4.15` | 595,400.00 USD | 595,400.00 USD | 0.00 USD | 64,270.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4.15` | 431,140.00 USD | 431,140.00 USD | 0.00 USD | 0.00 USD | 53,890.00 USD | 0.00 USD |
| `1D` | `4.17` | 664,710.00 USD | 664,710.00 USD | 0.00 USD | 0.00 USD | 16,800.00 USD | 52,510.00 USD |
| `1D` | `4.18` | 874,490.00 USD | 874,490.00 USD | 0.00 USD | 192,730.00 USD | 17,040.00 USD | 0.00 USD |
| `1D` | `4.19` | 1,250,000.00 USD | 1,250,000.00 USD | 0.00 USD | 174,270.00 USD | 20,540.00 USD | 185,170.00 USD |
| `7D` | `4.20` | 1,030,000.00 USD | 1,030,000.00 USD | 0.00 USD | 227,690.00 USD | 0.00 USD | 371,630.00 USD |
| `1D` | `4.21` | 1,330,000.00 USD | 1,330,000.00 USD | 0.00 USD | 58,200.00 USD | 20,820.00 USD | 0.00 USD |
| `1D` | `4.22` | 1,530,000.00 USD | 1,530,000.00 USD | 0.00 USD | 97,990.00 USD | 27,150.00 USD | 74,260.00 USD |
| `1D` | `4.23` | 2,200,000.00 USD | 2,200,000.00 USD | 0.00 USD | 203,550.00 USD | 468,020.00 USD | 0.00 USD |
| `1D` | `4.24` | 2,880,000.00 USD | 2,880,000.00 USD | 0.00 USD | 506,300.00 USD | 0.00 USD | 173,430.00 USD |
| `1D` | `4.25` | 3,210,000.00 USD | 3,210,000.00 USD | 0.00 USD | 0.00 USD | 72,920.00 USD | 255,640.00 USD |
| `7D` | `4.25` | 1,090,000.00 USD | 1,090,000.00 USD | 0.00 USD | 0.00 USD | 57,340.00 USD | 0.00 USD |
| `1D` | `4.26` | 3,480,000.00 USD | 3,480,000.00 USD | 0.00 USD | 92,160.00 USD | 173,320.00 USD | 248.22 USD |
| `7D` | `4.26` | 1,820,000.00 USD | 1,820,000.00 USD | 0.00 USD | 0.00 USD | 378,440.00 USD | 355,620.00 USD |
| `1D` | `4.27` | 4,340,000.00 USD | 4,340,000.00 USD | 0.00 USD | 677,660.00 USD | 34,890.00 USD | 152,200.00 USD |
| `7D` | `4.27` | 3,610,000.00 USD | 3,610,000.00 USD | 0.00 USD | 18,140.00 USD | 194,220.00 USD | 1,580,000.00 USD |
| `1D` | `4.28` | 4,970,000.00 USD | 4,970,000.00 USD | 0.00 USD | 305,690.00 USD | 30,410.00 USD | 288,910.00 USD |
| `7D` | `4.28` | 5,520,000.00 USD | 5,520,000.00 USD | 0.00 USD | 113,840.00 USD | 497,680.00 USD | 1,300,000.00 USD |
| `1D` | `4.29` | 5,320,000.00 USD | 5,320,000.00 USD | 0.00 USD | 153,130.00 USD | 32,690.00 USD | 161,450.00 USD |
| `7D` | `4.29` | 5,570,000.00 USD | 5,570,000.00 USD | 0.00 USD | 0.00 USD | 46,530.00 USD | 0.00 USD |
| `1D` | `4.30` | 5,560,000.00 USD | 5,560,000.00 USD | 0.00 USD | 32,410.00 USD | 45,120.00 USD | 163,210.00 USD |
| `7D` | `4.30` | 6,040,000.00 USD | 6,040,000.00 USD | 0.00 USD | 214,920.00 USD | 180,920.00 USD | 75,610.00 USD |
| `1D` | `4.31` | 5,970,000.00 USD | 5,970,000.00 USD | 0.00 USD | 304,920.00 USD | 13,580.00 USD | 95,430.00 USD |
| `7D` | `4.31` | 6,470,000.00 USD | 6,470,000.00 USD | 0.00 USD | 213,530.00 USD | 53,890.00 USD | 170,400.00 USD |
| `1D` | `4.32` | 6,130,000.00 USD | 6,130,000.00 USD | 0.00 USD | 86,850.00 USD | 73,400.00 USD | 18.65 USD |
| `7D` | `4.32` | 7,120,000.00 USD | 7,120,000.00 USD | 0.00 USD | 265,720.00 USD | 160,980.00 USD | 222,930.00 USD |
| `1D` | `4.33` | 6,570,000.00 USD | 6,570,000.00 USD | 0.00 USD | 255,620.00 USD | 93,880.00 USD | 87,760.00 USD |
| `7D` | `4.33` | 7,240,000.00 USD | 7,240,000.00 USD | 0.00 USD | 2,690.00 USD | 27,170.00 USD | 88,000.00 USD |
| `1D` | `4.34` | 7,090,000.00 USD | 7,090,000.00 USD | 0.00 USD | 270,720.00 USD | 140,540.00 USD | 114,690.00 USD |
| `7D` | `4.34` | 7,420,000.00 USD | 7,420,000.00 USD | 0.00 USD | 4,550.00 USD | 28,670.00 USD | 141,900.00 USD |
| `1D` | `4.35` | 7,180,000.00 USD | 7,180,000.00 USD | 0.00 USD | 855.62 USD | 0.00 USD | 84,830.00 USD |
| `7D` | `4.35` | 7,500,000.00 USD | 7,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 85,370.00 USD |
| `1D` | `4.36` | 7,310,000.00 USD | 7,310,000.00 USD | 0.00 USD | 84,880.00 USD | 12,310.00 USD | 31,110.00 USD |
| `7D` | `4.36` | 7,650,000.00 USD | 7,650,000.00 USD | 0.00 USD | 8,190.00 USD | 0.00 USD | 140,550.00 USD |
| `1D` | `4.37` | 7,540,000.00 USD | 7,540,000.00 USD | 0.00 USD | 52,520.00 USD | 46,860.00 USD | 130,010.00 USD |
| `1D` | `4.38` | 8,380,000.00 USD | 8,380,000.00 USD | 0.00 USD | 248,590.00 USD | 34,500.00 USD | 559,230.00 USD |
| `7D` | `4.38` | 8,050,000.00 USD | 8,050,000.00 USD | 0.00 USD | 0.00 USD | 141,930.00 USD | 261,380.00 USD |
| `1D` | `4.39` | 8,710,000.00 USD | 8,710,000.00 USD | 0.00 USD | 399.48 USD | 17,360.00 USD | 310,880.00 USD |
| `7D` | `4.39` | 8,570,000.00 USD | 8,570,000.00 USD | 0.00 USD | 248,520.00 USD | 108,260.00 USD | 154,000.00 USD |
| `1D` | `4.40` | 9,110,000.00 USD | 9,110,000.00 USD | 0.00 USD | 288,790.00 USD | 34,040.00 USD | 81,970.00 USD |
| `7D` | `4.40` | 9,170,000.00 USD | 9,170,000.00 USD | 0.00 USD | 108,780.00 USD | 26,950.00 USD | 463,990.00 USD |
| `1D` | `4.41` | 9,490,000.00 USD | 9,490,000.00 USD | 0.00 USD | 196,820.00 USD | 112,990.00 USD | 65,530.00 USD |
| `7D` | `4.41` | 9,490,000.00 USD | 9,490,000.00 USD | 0.00 USD | 0.00 USD | 45,930.00 USD | 278,000.00 USD |
| `1D` | `4.42` | 9,540,000.00 USD | 9,540,000.00 USD | 0.00 USD | 0.00 USD | 47,240.00 USD | 774.54 USD |
| `7D` | `4.42` | 10,140,000.00 USD | 10,140,000.00 USD | 0.00 USD | 404,280.00 USD | 71,590.00 USD | 175,990.00 USD |
| `1D` | `4.43` | 9,690,000.00 USD | 9,690,000.00 USD | 0.00 USD | 5,100.00 USD | 49,400.00 USD | 98,670.00 USD |
| `7D` | `4.43` | 10,420,000.00 USD | 10,420,000.00 USD | 0.00 USD | 163,540.00 USD | 46,230.00 USD | 71,660.00 USD |
| `1D` | `4.44` | 10,470,000.00 USD | 10,470,000.00 USD | 0.00 USD | 154,480.00 USD | 339,100.00 USD | 290,890.00 USD |
| `7D` | `4.44` | 10,610,000.00 USD | 10,610,000.00 USD | 0.00 USD | 0.00 USD | 116,400.00 USD | 72,830.00 USD |
| `1D` | `4.45` | 10,530,000.00 USD | 10,530,000.00 USD | 0.00 USD | 649.63 USD | 50,720.00 USD | 1,400.00 USD |
| `1D` | `4.46` | 10,540,000.00 USD | 10,540,000.00 USD | 0.00 USD | 704.30 USD | 9,070.00 USD | 0.00 USD |
| `7D` | `4.46` | 10,680,000.00 USD | 10,680,000.00 USD | 0.00 USD | 0.00 USD | 62,110.00 USD | 2,080.00 USD |
| `1D` | `4.47` | 10,570,000.00 USD | 10,570,000.00 USD | 0.00 USD | 210.23 USD | 16,700.00 USD | 18,310.00 USD |
| `7D` | `4.47` | 11,020,000.00 USD | 11,020,000.00 USD | 0.00 USD | 203,160.00 USD | 135,940.00 USD | 2,060.00 USD |
| `1D` | `4.48` | 10,790,000.00 USD | 10,790,000.00 USD | 0.00 USD | 117,480.00 USD | 73,240.00 USD | 26,920.00 USD |
| `7D` | `4.48` | 11,020,000.00 USD | 11,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,510.00 USD |
| `1D` | `4.49` | 11,350,000.00 USD | 11,350,000.00 USD | 0.00 USD | 252,600.00 USD | 155,000.00 USD | 150,280.00 USD |
| `7D` | `4.49` | 11,360,000.00 USD | 11,360,000.00 USD | 0.00 USD | 242,770.00 USD | 93,790.00 USD | 0.00 USD |
| `1D` | `4.50` | 11,890,000.00 USD | 11,890,000.00 USD | 0.00 USD | 361,770.00 USD | 65,710.00 USD | 120,210.00 USD |
| `7D` | `4.50` | 11,930,000.00 USD | 11,930,000.00 USD | 0.00 USD | 373,240.00 USD | 200,700.00 USD | 1,820.00 USD |
| `1D` | `4.51` | 12,700,000.00 USD | 12,700,000.00 USD | 0.00 USD | 186,860.00 USD | 307,580.00 USD | 312,530.00 USD |
| `7D` | `4.51` | 12,010,000.00 USD | 12,010,000.00 USD | 0.00 USD | 77,780.00 USD | 0.00 USD | 2,030.00 USD |
| `1D` | `4.52` | 13,320,000.00 USD | 13,320,000.00 USD | 0.00 USD | 287,830.00 USD | 92,260.00 USD | 242,880.00 USD |
| `7D` | `4.52` | 12,150,000.00 USD | 12,150,000.00 USD | 0.00 USD | 2,080.00 USD | 0.00 USD | 138,450.00 USD |
| `1D` | `4.53` | 14,090,000.00 USD | 14,090,000.00 USD | 0.00 USD | 487,540.00 USD | 0.00 USD | 279,080.00 USD |
| `7D` | `4.53` | 13,130,000.00 USD | 13,130,000.00 USD | 0.00 USD | 438,070.00 USD | 232,800.00 USD | 309,560.00 USD |
| `1D` | `4.54` | 14,810,000.00 USD | 14,810,000.00 USD | 0.00 USD | 216.65 USD | 150,600.00 USD | 564,340.00 USD |
| `7D` | `4.54` | 14,370,000.00 USD | 14,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,240,000.00 USD |
| `1D` | `4.55` | 15,020,000.00 USD | 15,020,000.00 USD | 0.00 USD | 0.00 USD | 22,540.00 USD | 195,790.00 USD |
| `1D` | `4.56` | 15,430,000.00 USD | 15,430,000.00 USD | 0.00 USD | 79,110.00 USD | 32,800.00 USD | 288,660.00 USD |
| `7D` | `4.56` | 14,850,000.00 USD | 14,850,000.00 USD | 0.00 USD | 361,350.00 USD | 124,220.00 USD | 0.00 USD |
| `1D` | `4.57` | 15,740,000.00 USD | 15,740,000.00 USD | 0.00 USD | 177,440.00 USD | 70,180.00 USD | 67,980.00 USD |
| `7D` | `4.57` | 15,400,000.00 USD | 15,400,000.00 USD | 0.00 USD | 305,830.00 USD | 27,650.00 USD | 209,310.00 USD |
| `1D` | `4.58` | 17,200,000.00 USD | 17,200,000.00 USD | 0.00 USD | 506,750.00 USD | 73,690.00 USD | 875,260.00 USD |
| `7D` | `4.58` | 15,530,000.00 USD | 15,530,000.00 USD | 0.00 USD | 44,380.00 USD | 0.00 USD | 85,990.00 USD |
| `1D` | `4.59` | 18,180,000.00 USD | 18,180,000.00 USD | 0.00 USD | 826,150.00 USD | 75,460.00 USD | 79,420.00 USD |
| `7D` | `4.59` | 17,120,000.00 USD | 17,120,000.00 USD | 0.00 USD | 760,880.00 USD | 40,640.00 USD | 794,930.00 USD |
| `1D` | `4.60` | 18,380,000.00 USD | 18,380,000.00 USD | 0.00 USD | 54,450.00 USD | 84,420.00 USD | 66,160.00 USD |
| `7D` | `4.60` | 17,240,000.00 USD | 17,240,000.00 USD | 0.00 USD | 3,460.00 USD | 112,080.00 USD | 2,360.00 USD |
| `1D` | `4.61` | 18,520,000.00 USD | 18,520,000.00 USD | 0.00 USD | 66,620.00 USD | 7,560.00 USD | 60,990.00 USD |
| `7D` | `4.61` | 17,250,000.00 USD | 17,250,000.00 USD | 0.00 USD | 3,350.00 USD | 0.00 USD | 960.97 USD |
| `1D` | `4.62` | 18,670,000.00 USD | 18,670,000.00 USD | 0.00 USD | 95,090.00 USD | 31,380.00 USD | 21,030.00 USD |
| `7D` | `4.62` | 17,380,000.00 USD | 17,380,000.00 USD | 0.00 USD | 134,680.00 USD | 0.00 USD | 2,720.00 USD |
| `1D` | `4.63` | 18,670,000.00 USD | 18,670,000.00 USD | 0.00 USD | 1,040.00 USD | 0.00 USD | 614.32 USD |
| `7D` | `4.63` | 17,600,000.00 USD | 17,600,000.00 USD | 0.00 USD | 213,490.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `4.64` | 19,080,000.00 USD | 19,080,000.00 USD | 0.00 USD | 334,190.00 USD | 11,270.00 USD | 63,790.00 USD |
| `7D` | `4.64` | 18,120,000.00 USD | 18,120,000.00 USD | 0.00 USD | 501,930.00 USD | 18,170.00 USD | 1,670.00 USD |
| `1D` | `4.65` | 20,150,000.00 USD | 20,150,000.00 USD | 0.00 USD | 423,550.00 USD | 52,020.00 USD | 600,100.00 USD |
| `7D` | `4.65` | 18,540,000.00 USD | 18,540,000.00 USD | 0.00 USD | 420,940.00 USD | 0.00 USD | 2,000.00 USD |
| `1D` | `4.66` | 21,130,000.00 USD | 21,130,000.00 USD | 0.00 USD | 281,290.00 USD | 316,500.00 USD | 379,880.00 USD |
| `7D` | `4.66` | 18,860,000.00 USD | 18,860,000.00 USD | 0.00 USD | 144,860.00 USD | 18,370.00 USD | 150,940.00 USD |
| `1D` | `4.67` | 21,690,000.00 USD | 21,690,000.00 USD | 0.00 USD | 184,440.00 USD | 0.00 USD | 378,090.00 USD |
| `7D` | `4.67` | 18,900,000.00 USD | 18,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 43,230.00 USD |
| `1D` | `4.68` | 22,300,000.00 USD | 22,300,000.00 USD | 0.00 USD | 345,840.00 USD | 81,340.00 USD | 175,700.00 USD |
| `7D` | `4.68` | 19,820,000.00 USD | 19,820,000.00 USD | 0.00 USD | 381,910.00 USD | 83,630.00 USD | 450,700.00 USD |
| `1D` | `4.69` | 22,800,000.00 USD | 22,800,000.00 USD | 0.00 USD | 213,780.00 USD | 40,000.00 USD | 254,150.00 USD |
| `7D` | `4.69` | 19,910,000.00 USD | 19,910,000.00 USD | 0.00 USD | 2,450.00 USD | 0.00 USD | 88,340.00 USD |
| `1D` | `4.70` | 23,140,000.00 USD | 23,140,000.00 USD | 0.00 USD | 74,090.00 USD | 123,520.00 USD | 143,310.00 USD |
| `7D` | `4.70` | 20,220,000.00 USD | 20,220,000.00 USD | 0.00 USD | 74,240.00 USD | 60,360.00 USD | 181,210.00 USD |
| `1D` | `4.71` | 24,100,000.00 USD | 24,100,000.00 USD | 0.00 USD | 359,510.00 USD | 284,360.00 USD | 316,030.00 USD |
| `7D` | `4.71` | 20,630,000.00 USD | 20,630,000.00 USD | 0.00 USD | 178,360.00 USD | 232,800.00 USD | 0.00 USD |
| `7D` | `4.72` | 20,820,000.00 USD | 20,820,000.00 USD | 0.00 USD | 7,140.00 USD | 0.00 USD | 180,490.00 USD |
| `7D` | `4.73` | 20,880,000.00 USD | 20,880,000.00 USD | 0.00 USD | 59,970.00 USD | 0.00 USD | 894.74 USD |
| `7D` | `4.74` | 21,200,000.00 USD | 21,200,000.00 USD | 0.00 USD | 14,750.00 USD | 173,100.00 USD | 127,910.00 USD |
| `7D` | `4.75` | 21,740,000.00 USD | 21,740,000.00 USD | 0.00 USD | 17,340.00 USD | 185,060.00 USD | 343,810.00 USD |
| `7D` | `4.76` | 23,090,000.00 USD | 23,090,000.00 USD | 0.00 USD | 1,030,000.00 USD | 46,890.00 USD | 272,560.00 USD |
| `7D` | `4.77` | 24,000,000.00 USD | 24,000,000.00 USD | 0.00 USD | 731,680.00 USD | 73,410.00 USD | 101,640.00 USD |
| `7D` | `4.78` | 25,350,000.00 USD | 25,350,000.00 USD | 0.00 USD | 683,730.00 USD | 513,870.00 USD | 154,510.00 USD |
| `7D` | `4.79` | 26,380,000.00 USD | 26,380,000.00 USD | 0.00 USD | 713,060.00 USD | 249,310.00 USD | 72,120.00 USD |
| `7D` | `4.80` | 27,970,000.00 USD | 27,970,000.00 USD | 0.00 USD | 1,160,000.00 USD | 432,340.00 USD | 2,480.00 USD |
| `7D` | `4.81` | 28,600,000.00 USD | 28,600,000.00 USD | 0.00 USD | 400,070.00 USD | 125,900.00 USD | 101,780.00 USD |
| `7D` | `4.82` | 31,370,000.00 USD | 31,370,000.00 USD | 0.00 USD | 1,010,000.00 USD | 369,430.00 USD | 1,390,000.00 USD |
| `7D` | `4.83` | 33,020,000.00 USD | 33,020,000.00 USD | 0.00 USD | 822,860.00 USD | 85,680.00 USD | 739,630.00 USD |
| `7D` | `4.84` | 33,510,000.00 USD | 33,510,000.00 USD | 0.00 USD | 97,300.00 USD | 71,790.00 USD | 322,840.00 USD |
| `7D` | `4.85` | 35,530,000.00 USD | 35,530,000.00 USD | 0.00 USD | 487,940.00 USD | 366,970.00 USD | 1,160,000.00 USD |
| `7D` | `4.86` | 36,940,000.00 USD | 36,940,000.00 USD | 0.00 USD | 444,810.00 USD | 162,380.00 USD | 802,380.00 USD |
| `7D` | `4.87` | 38,000,000.00 USD | 38,000,000.00 USD | 0.00 USD | 264,730.00 USD | 136,820.00 USD | 663,430.00 USD |
| `7D` | `4.88` | 39,590,000.00 USD | 39,590,000.00 USD | 0.00 USD | 449,970.00 USD | 340,260.00 USD | 792,630.00 USD |
| `7D` | `4.89` | 40,170,000.00 USD | 40,170,000.00 USD | 0.00 USD | 213,960.00 USD | 100,850.00 USD | 272,060.00 USD |
| `7D` | `4.90` | 41,310,000.00 USD | 41,310,000.00 USD | 0.00 USD | 450,550.00 USD | 145,910.00 USD | 541,330.00 USD |
| `7D` | `4.91` | 42,750,000.00 USD | 42,750,000.00 USD | 0.00 USD | 637,320.00 USD | 208,910.00 USD | 590,510.00 USD |
| `7D` | `4.92` | 44,480,000.00 USD | 44,480,000.00 USD | 0.00 USD | 576,460.00 USD | 277,640.00 USD | 877,920.00 USD |
| `7D` | `4.93` | 46,040,000.00 USD | 46,040,000.00 USD | 0.00 USD | 730,010.00 USD | 78,190.00 USD | 749,940.00 USD |
| `7D` | `4.94` | 47,380,000.00 USD | 47,380,000.00 USD | 0.00 USD | 351,940.00 USD | 290,290.00 USD | 696,960.00 USD |
| `7D` | `4.95` | 48,680,000.00 USD | 48,680,000.00 USD | 0.00 USD | 468,360.00 USD | 161,040.00 USD | 670,270.00 USD |
| `7D` | `4.96` | 49,910,000.00 USD | 49,910,000.00 USD | 0.00 USD | 607,770.00 USD | 214,910.00 USD | 410,880.00 USD |
| `7D` | `4.97` | 50,290,000.00 USD | 50,290,000.00 USD | 0.00 USD | 198,220.00 USD | 72,330.00 USD | 113,320.00 USD |
| `7D` | `4.98` | 50,950,000.00 USD | 50,950,000.00 USD | 0.00 USD | 251,840.00 USD | 102,410.00 USD | 299,870.00 USD |
| `7D` | `4.99` | 51,300,000.00 USD | 51,300,000.00 USD | 0.00 USD | 133,330.00 USD | 103,060.00 USD | 117,980.00 USD |
| `7D` | `5.00` | 52,000,000.00 USD | 52,000,000.00 USD | 0.00 USD | 210,680.00 USD | 36,180.00 USD | 454,070.00 USD |
| `7D` | `5.01` | 53,830,000.00 USD | 53,830,000.00 USD | 0.00 USD | 781,840.00 USD | 255,770.00 USD | 786,470.00 USD |
| `7D` | `5.02` | 55,280,000.00 USD | 55,280,000.00 USD | 0.00 USD | 821,860.00 USD | 309,020.00 USD | 321,920.00 USD |
| `7D` | `5.03` | 56,410,000.00 USD | 56,410,000.00 USD | 0.00 USD | 385,330.00 USD | 172,880.00 USD | 567,890.00 USD |
| `7D` | `5.04` | 57,490,000.00 USD | 57,490,000.00 USD | 0.00 USD | 305,260.00 USD | 163,190.00 USD | 619,980.00 USD |
| `7D` | `5.05` | 58,940,000.00 USD | 58,940,000.00 USD | 0.00 USD | 694,310.00 USD | 267,140.00 USD | 486,680.00 USD |
| `7D` | `5.06` | 59,620,000.00 USD | 59,620,000.00 USD | 0.00 USD | 92,480.00 USD | 165,230.00 USD | 420,210.00 USD |
| `7D` | `5.07` | 60,660,000.00 USD | 60,660,000.00 USD | 0.00 USD | 358,750.00 USD | 137,080.00 USD | 542,550.00 USD |
| `7D` | `5.08` | 61,180,000.00 USD | 61,180,000.00 USD | 0.00 USD | 204,140.00 USD | 167,810.00 USD | 150,010.00 USD |
| `7D` | `5.09` | 61,720,000.00 USD | 61,720,000.00 USD | 0.00 USD | 105,390.00 USD | 52,790.00 USD | 385,540.00 USD |
| `7D` | `5.10` | 62,110,000.00 USD | 62,110,000.00 USD | 0.00 USD | 182,200.00 USD | 0.00 USD | 201,110.00 USD |
| `7D` | `5.11` | 62,700,000.00 USD | 62,700,000.00 USD | 0.00 USD | 369,260.00 USD | 78,100.00 USD | 140,600.00 USD |
| `7D` | `5.12` | 63,270,000.00 USD | 63,270,000.00 USD | 0.00 USD | 303,840.00 USD | 152,530.00 USD | 115,650.00 USD |
| `7D` | `5.13` | 63,840,000.00 USD | 63,840,000.00 USD | 0.00 USD | 173,190.00 USD | 71,310.00 USD | 325,090.00 USD |
| `7D` | `5.14` | 64,280,000.00 USD | 64,280,000.00 USD | 0.00 USD | 140,950.00 USD | 59,640.00 USD | 239,260.00 USD |
| `7D` | `5.15` | 64,830,000.00 USD | 64,830,000.00 USD | 0.00 USD | 205,680.00 USD | 82,350.00 USD | 267,910.00 USD |
| `7D` | `5.16` | 65,350,000.00 USD | 65,350,000.00 USD | 0.00 USD | 51,850.00 USD | 112,830.00 USD | 347,470.00 USD |
| `7D` | `5.17` | 65,960,000.00 USD | 65,960,000.00 USD | 0.00 USD | 280,710.00 USD | 85,040.00 USD | 244,330.00 USD |
| `7D` | `5.18` | 66,210,000.00 USD | 66,210,000.00 USD | 0.00 USD | 67,600.00 USD | 63,250.00 USD | 124,260.00 USD |
| `7D` | `5.19` | 66,430,000.00 USD | 66,430,000.00 USD | 0.00 USD | 69,310.00 USD | 13,680.00 USD | 138,850.00 USD |
| `7D` | `5.20` | 66,680,000.00 USD | 66,680,000.00 USD | 0.00 USD | 137,830.00 USD | 45,820.00 USD | 65,990.00 USD |
| `7D` | `5.21` | 66,920,000.00 USD | 66,920,000.00 USD | 0.00 USD | 105,330.00 USD | 20,850.00 USD | 110,400.00 USD |
| `7D` | `5.22` | 66,980,000.00 USD | 66,980,000.00 USD | 0.00 USD | 48,760.00 USD | 13,410.00 USD | 398.26 USD |
| `7D` | `5.23` | 67,040,000.00 USD | 67,040,000.00 USD | 0.00 USD | 5,060.00 USD | 15,520.00 USD | 34,400.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `1.06B` | Total OI Tokens: `262,081,817.7 NEAR`
  * 1h OI Change: `-1.47%` | 4h OI Change: `-8.21%` | 24h OI Change: `-16.19%`
  * Exchange Breakdown: Binance=`203.92M` | Bybit=`143.53M` | OKX=`49.07M` | Hyperliquid=`228.12M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `-4.28K` | Last 24h: `59.84K` | Last 3d: `308.79K` | Last 7d: `236.18K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0043%` | **USDT OKX** | `-0.0024%` |
| **USDT Bybit** | `-0.0090%` | **USDT KuCoin** | `0.0100%` |
| **USDT MEXC** | `0.0043%` | **USDT BingX** | `0.0039%` |
| **USDT Gate** | `-0.0560%` | **USDT Bitget** | `0.0010%` |
| **CoinM Binance** | `0.0100%` | **CoinM OKX** | `-` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `NEAR` | `54.57%` | `45.43%` | `1.20` | 7,590,000.00 USD |
| `15M` | `Binance` | `53.91%` | `46.09%` | `1.17` | 3,250,000.00 USD |
| `15M` | `OKX` | `46.77%` | `53.23%` | `0.88` | 1,020,000.00 USD |
| `15M` | `Bybit` | `55.71%` | `44.29%` | `1.26` | 774,690.00 USD |
| `15M` | `KuCoin` | `59.07%` | `40.93%` | `1.44` | 108,180.00 USD |
| `15M` | `Gate` | `53.59%` | `46.41%` | `1.15` | 206,000.00 USD |
| `15M` | `Bitget` | `49.68%` | `50.32%` | `0.99` | 368,280.00 USD |
| `15M` | `BingX` | `31.34%` | `68.66%` | `0.46` | 306,710.00 USD |
| `15M` | `MEXC` | `73.12%` | `26.88%` | `2.72` | 819,810.00 USD |
| `15M` | `Bitunix` | `62.4%` | `37.6%` | `1.66` | 175,600.00 USD |
| `15M` | `Hyperliquid` | `42.09%` | `57.91%` | `0.73` | 173,540.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `35.14%` | `64.86%` | `0.54` | 128,670.00 USD |
| `15M` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `WhiteBIT` | `99.44%` | `0.56%` | `177.57` | 177,700.00 USD |
| `15M` | `HTX` | `40.15%` | `59.85%` | `0.67` | 12,350.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `23.35%` | `76.65%` | `0.30` | 43,590.00 USD |
| `15M` | `Aster` | `36.1%` | `63.9%` | `0.56` | 29,000.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `59.1%` | `40.9%` | `1.44` | 3,700.00 USD |
| `15M` | `Whale Positions` | `53.91%` | `46.09%` | `1.17` | 3,250,000.00 USD |
| `15M` | `Global Accounts` | `54.57%` | `45.43%` | `1.20` | 7,590,000.00 USD |
| `1H` | `NEAR` | `45.59%` | `54.41%` | `0.84` | 41,630,000.00 USD |
| `1H` | `Binance` | `48.8%` | `51.2%` | `0.95` | 15,660,000.00 USD |
| `1H` | `OKX` | `45.86%` | `54.14%` | `0.85` | 4,840,000.00 USD |
| `1H` | `Bybit` | `49.45%` | `50.55%` | `0.98` | 5,300,000.00 USD |
| `1H` | `KuCoin` | `45.55%` | `54.45%` | `0.84` | 464,420.00 USD |
| `1H` | `Gate` | `44.21%` | `55.79%` | `0.79` | 1,370,000.00 USD |
| `1H` | `Bitget` | `48.16%` | `51.84%` | `0.93` | 2,490,000.00 USD |
| `1H` | `BingX` | `12.33%` | `87.67%` | `0.14` | 3,630,000.00 USD |
| `1H` | `MEXC` | `46.57%` | `53.43%` | `0.87` | 3,760,000.00 USD |
| `1H` | `Bitunix` | `44%` | `56%` | `0.79` | 1,190,000.00 USD |
| `1H` | `Hyperliquid` | `54.63%` | `45.37%` | `1.20` | 1,510,000.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `40.17%` | `59.83%` | `0.67` | 274,050.00 USD |
| `1H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `WhiteBIT` | `95.84%` | `4.16%` | `23.04` | 657,840.00 USD |
| `1H` | `HTX` | `43.13%` | `56.87%` | `0.76` | 119,420.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `40.91%` | `59.09%` | `0.69` | 233,520.00 USD |
| `1H` | `Aster` | `31.65%` | `68.35%` | `0.46` | 107,340.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `44.57%` | `55.43%` | `0.80` | 16,380.00 USD |
| `1H` | `Whale Positions` | `48.8%` | `51.2%` | `0.95` | 15,660,000.00 USD |
| `1H` | `Global Accounts` | `45.59%` | `54.41%` | `0.84` | 41,630,000.00 USD |
| `4H` | `NEAR` | `44.68%` | `55.32%` | `0.81` | 284,910,000.00 USD |
| `4H` | `Binance` | `45.55%` | `54.45%` | `0.84` | 105,890,000.00 USD |
| `4H` | `OKX` | `47.77%` | `52.23%` | `0.91` | 37,470,000.00 USD |
| `4H` | `Bybit` | `45.68%` | `54.32%` | `0.84` | 41,350,000.00 USD |
| `4H` | `KuCoin` | `43.62%` | `56.38%` | `0.77` | 4,200,000.00 USD |
| `4H` | `Gate` | `40.05%` | `59.95%` | `0.67` | 9,790,000.00 USD |
| `4H` | `Bitget` | `44.82%` | `55.18%` | `0.81` | 21,560,000.00 USD |
| `4H` | `BingX` | `26.13%` | `73.87%` | `0.35` | 9,440,000.00 USD |
| `4H` | `MEXC` | `43.21%` | `56.79%` | `0.76` | 23,560,000.00 USD |
| `4H` | `Bitunix` | `42.41%` | `57.59%` | `0.74` | 8,820,000.00 USD |
| `4H` | `Hyperliquid` | `50.6%` | `49.4%` | `1.02` | 11,240,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `31.18%` | `68.82%` | `0.45` | 2,850,000.00 USD |
| `4H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `WhiteBIT` | `42.49%` | `57.51%` | `0.74` | 4,390,000.00 USD |
| `4H` | `HTX` | `46.41%` | `53.59%` | `0.87` | 536,740.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `52.16%` | `47.84%` | `1.09` | 2,000,000.00 USD |
| `4H` | `Aster` | `41.13%` | `58.87%` | `0.70` | 1,350,000.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `39.07%` | `60.93%` | `0.64` | 451,210.00 USD |
| `4H` | `Whale Positions` | `45.55%` | `54.45%` | `0.84` | 105,890,000.00 USD |
| `4H` | `Global Accounts` | `44.68%` | `55.32%` | `0.81` | 284,910,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5:00 UTC` | `4.06` | `4.06` | `4.06` | `4.08` | `4.04` | 13,393,607.00 USD | 6,718,844.40 USD | 6,674,762.60 USD | 44,081.81 USD | `+0.33%` | `2B / 2S` |
| `0:00 UTC` | `4.06` | `4.05` | `4.06` | `4.08` | `4.02` | 16,647,053.78 USD | 8,059,551.61 USD | 8,587,502.18 USD | -527,950.57 USD | `-3.17%` | `5B / 5S` |
| `5:00 UTC` | `3.98` | `3.99` | `3.98` | `4.05` | `3.92` | 44,923,279.18 USD | 19,438,062.87 USD | 25,485,216.31 USD | -6,047,153.45 USD | `-13.46%` | `4B / 18S` |
| `0:00 UTC` | `3.96` | `3.94` | `3.96` | `3.98` | `3.91` | 23,036,432.35 USD | 10,793,071.74 USD | 12,243,360.61 USD | -1,450,288.88 USD | `-6.30%` | `4B / 6S` |
| `5:00 UTC` | `4.00` | `3.99` | `4.00` | `4.02` | `3.95` | 14,908,541.20 USD | 8,081,809.07 USD | 6,826,732.13 USD | 1,255,076.95 USD | `+8.42%` | `5B / 3S` |
| `0:00 UTC` | `3.99` | `4.00` | `3.99` | `4.04` | `3.98` | 10,043,819.37 USD | 5,055,045.74 USD | 4,988,773.63 USD | 66,272.12 USD | `+0.66%` | `10B / 0S` |
| `5:00 UTC` | `4.00` | `4.00` | `4.00` | `4.04` | `3.99` | 5,936,404.63 USD | 2,860,550.97 USD | 3,075,853.66 USD | -215,302.69 USD | `-3.63%` | `6B / 8S` |
| `0:00 UTC` | `4.02` | `4.00` | `4.02` | `4.03` | `3.95` | 11,016,623.88 USD | 5,505,508.67 USD | 5,511,115.21 USD | -5,606.55 USD | `-0.05%` | `3B / 8S` |
| `5:00 UTC` | `3.99` | `3.99` | `3.99` | `4.01` | `3.97` | 6,380,993.73 USD | 2,663,458.31 USD | 3,717,535.41 USD | -1,054,077.10 USD | `-16.52%` | `2B / 11S` |
| `0:00 UTC` | `4.00` | `3.99` | `4.00` | `4.01` | `3.97` | 3,599,195.33 USD | 1,872,972.45 USD | 1,726,222.88 USD | 146,749.57 USD | `+4.08%` | `4B / 4S` |

- **CoinGlass Algorithmic Footprint Signals Table (25_CoinGlass_Footprint_Signals.parquet)**:
| Time | Timeframe | Signal Type | Bias | Headline | Price Level | Absorbed Vol (USD) | Bar Delta (USD) |
|:---:|:---:|:---:|:---:|:---|:---:|:---:|:---:|
| `10-28 21:10` | `Range 0.02` | `Absorption` | **`BEARISH`** | Buying absorbed at the high | `4.65` | 100,000.00 USD | 0.00 USD |
| `10-28 20:51` | `Range 0.02` | `Exhaustion` | **`BEARISH`** | Buyer exhaustion | `4.64` | 0.00 USD | 0.00 USD |
| `10-28 20:33` | `Range 0.02` | `Divergence` | **`BEARISH`** | Rally without taker buying | `4.63` | 0.00 USD | 0.00 USD |
| `10-28 19:52` | `Range 0.02` | `Divergence` | **`BEARISH`** | Rally without taker buying | `4.57` | 0.00 USD | 0.00 USD |
| `10-28 19:52` | `Range 0.02` | `Exhaustion` | **`BULLISH`** | Seller exhaustion | `4.54` | 0.00 USD | 0.00 USD |
| `10-28 19:51` | `Volume 2.0M NEAR` | `Exhaustion` | **`BULLISH`** | Seller exhaustion | `4.54` | 0.00 USD | 0.00 USD |
| `10-28 19:32` | `Range 0.02` | `Absorption` | **`BEARISH`** | Buying absorbed at the high | `4.61` | 185,000.00 USD | 0.00 USD |
| `10-28 19:03` | `Volume 2.0M NEAR` | `Absorption` | **`BEARISH`** | Buying absorbed at the high | `4.65` | 419,000.00 USD | 0.00 USD |
| `10-28 19:03` | `Volume 2.0M NEAR` | `Trapped longs` | **`BEARISH`** | Failed breakout | `4.65` | 419,000.00 USD | 0.00 USD |
| `10-28 18:51` | `Volume 2.0M NEAR` | `Absorption` | **`BULLISH`** | Selling absorbed at the low | `4.59` | 469,000.00 USD | 0.00 USD |
| `10-28 18:17` | `Range 0.02` | `Divergence` | **`BEARISH`** | Rally without taker buying | `4.61` | 0.00 USD | 0.00 USD |
| `10-28 17:55` | `Range 0.02` | `Divergence` | **`BULLISH`** | Drop without taker selling | `4.62` | 0.00 USD | 0.00 USD |
| `10-28 17:34` | `Range 0.02` | `Divergence` | **`BEARISH`** | Rally without taker buying | `4.66` | 0.00 USD | 0.00 USD |
| `10-28 17:34` | `Range 0.02` | `Absorption` | **`BULLISH`** | Selling absorbed at the low | `4.64` | 209,000.00 USD | 0.00 USD |
| `10-28 16:42` | `Volume 2.0M NEAR` | `Exhaustion` | **`BULLISH`** | Seller exhaustion | `4.65` | 0.00 USD | 0.00 USD |
| `10-28 14:29` | `Range 0.02` | `Exhaustion` | **`BULLISH`** | Seller exhaustion | `4.72` | 0.00 USD | 0.00 USD |
| `10-28 13:31` | `Volume 2.0M NEAR` | `Divergence` | **`BEARISH`** | Rally without taker buying | `4.76` | 0.00 USD | 0.00 USD |
| `10-28 07:47` | `Range 0.02` | `Absorption` | **`BEARISH`** | Buying absorbed at the high | `4.75` | 145,000.00 USD | 0.00 USD |
| `10-28 07:47` | `Range 0.02` | `Trapped longs` | **`BEARISH`** | Failed breakout | `4.75` | 145,000.00 USD | 0.00 USD |
| `10-28 07:26` | `Range 0.02` | `Absorption` | **`BULLISH`** | Selling absorbed at the low | `4.71` | 84,000.00 USD | 0.00 USD |
| `10-28 06:42` | `Range 0.02` | `Divergence` | **`BEARISH`** | Rally without taker buying | `4.65` | 0.00 USD | 0.00 USD |
| `10-28 06:42` | `Range 0.02` | `Absorption` | **`BULLISH`** | Selling absorbed at the low | `4.63` | 166,000.00 USD | 0.00 USD |
| `10-28 06:40` | `Volume 2.0M NEAR` | `Absorption` | **`BULLISH`** | Selling absorbed at the low | `4.63` | 374,000.00 USD | 0.00 USD |
| `10-28 05:31` | `Range 0.02` | `Exhaustion` | **`BULLISH`** | Seller exhaustion | `4.65` | 0.00 USD | 0.00 USD |

- **12-Horizon Macro Capital Netflows Table (2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet)**:
| Horizon | Spot Netflow (USD) | Futures Netflow (USD) | Institutional Bias |
|:---:|:---:|:---:|:---:|
| `5m` | -305,920.00 USD | 1,680,000.00 USD | **`ACCUMULATION`** |
| `15m` | -376,850.00 USD | 1,390,000.00 USD | **`ACCUMULATION`** |
| `30m` | -1,530,000.00 USD | -144,080.00 USD | **`DISTRIBUTION`** |
| `1h` | -1,850,000.00 USD | 643,580.00 USD | **`DISTRIBUTION`** |
| `2h` | -1,980,000.00 USD | -11,790,000.00 USD | **`DISTRIBUTION`** |
| `4h` | -5,200,000.00 USD | -16,470,000.00 USD | **`DISTRIBUTION`** |
| `6h` | -12,340,000.00 USD | -33,700,000.00 USD | **`DISTRIBUTION`** |
| `8h` | -16,560,000.00 USD | -37,200,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -18,700,000.00 USD | -40,940,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -23,040,000.00 USD | -66,840,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -83,620,000.00 USD | -144,640,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -252,420,000.00 USD | -695,910,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-305.92K` | 15m=`-376.85K` | 1h=`-1.85M` | 24h=`-23.04M`
* Futures Capital Netflows: 5m=`+1.68M` | 15m=`+1.39M` | 1h=`+643.58K` | 24h=`-66.84M`
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
  * `2026-10-30 07:16:34 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-30 07:38:34 IST`: [kathleenhays.substack.com] - (Sentiment: `Neutral`)
  * `2026-10-30 07:38:34 IST`: [rba.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 07:38:34 IST`: [abs.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 07:38:34 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 07:37:34 IST`: [@NodeWire] - (Sentiment: `Neutral`)
  * `2026-10-30 07:37:34 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 07:37:34 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 07:37:34 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-30 07:37:34 IST`: [media.rabobank.com] - (Sentiment: `Neutral`)
  * `2026-10-30 04:39:34 IST`: [economics.td.com] - (Sentiment: `Neutral`)
  * `2026-10-30 03:39:34 IST`: [investinglive.com] - (Sentiment: `Neutral`)
  * `2026-10-30 03:39:34 IST`: [msn.com] - (Sentiment: `Neutral`)
  * `2026-10-30 02:39:34 IST`: [morningstar.com] - (Sentiment: `Neutral`)
  * `2026-10-30 01:39:34 IST`: [sec.gov] - (Sentiment: `Neutral`)


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
  * Execution Entry: `3.94` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `3.82` (Risk Distance: `0.1210` pts)
  * +2.5R Take Profit: `4.24`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `4.12` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `4.24` (Risk Distance: `0.1210` pts)
  * +2.5R Take Profit: `3.82`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`4.05`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
