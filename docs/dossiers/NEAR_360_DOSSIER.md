# 🏛️ SOVEREIGN CANDIDATE DOSSIER: NEAR
**Canonical Key**: `NEAR` | **Broker Instrument**: `NERUSD.p` | **Asset Class**: `Crypto Alt L1`
**Timestamp**: `2026-10-30 07:39:18 IST` (`2026-10-30 02:09:18 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `3.97` | **Live Ask Quote**: `4.00` | **Mid Price**: `3.98`
- **Spread Points**: `31.00` | **Spread BPS**: `77.84 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `3.98` | VWAP Z-Score: `-1.59` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `0.0650` (Volatility Regime: `HIGH_EXPANSION`)
  * 14-Period RSI: `31.09` (State: `OVERSOLD`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `4.90` | Lower -3.00σ Band: `3.72`
  * Upper +2.51σ Band: `4.80` | Lower -2.51σ Band: `3.81`
  * Upper +2.01σ Band: `4.70` | Lower -2.01σ Band: `3.91`
  * Upper +2.00σ Band: `4.70` | Lower -2.00σ Band: `3.91`
  * Upper +1.28σ Band: `4.56` | Lower -1.28σ Band: `4.05`
  * Upper +1.00σ Band: `4.50` | Lower -1.00σ Band: `4.11`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`4.01` | EMA-20=`4.08` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`4.23` (Slope: `+0.0000`) | EMA-100=`4.34`
  * Institutional Anchors: EMA-144=`4.39` | EMA-200=`4.42` (Slope: `-1.1470`) | EMA-233=`4.45`
- **Range Boundaries**: 24H High=`4.67` | 24H Low=`3.89` | Weekly High=`4.80` | Weekly Low=`3.89`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `4.15` (Distance: `-3.98%`)
  * Point of Control (POC) = `4.09` (Distance: `-2.71%`)
  * Value Area Low (VAL) = `3.97` (Distance: `+0.44%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`4.57` | POC=`4.41` | VAL=`4.29`
  * Prior Day Extremes: PDH=`4.75` | PDL=`4.08` | PDC=`4.15`
  * Monday Range Blueprint: High=`4.65` | Mid=`4.53` | Low=`4.41`
  * Developing Weekly Value Area: Weekly VAH=`4.67` | Weekly POC=`4.45` | Weekly VAL=`4.39`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`4.26` | Low=`3.89`
  * London Session (08:00-16:00 UTC): High=`4.00` | Low=`3.97`
  * New York Session (13:00-21:00 UTC): High=`4.01` | Low=`3.96`
  * Initial Balance (First Hour): IB High=`3.99` | IB Low=`3.97`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `3.97` - `4.00`
  * Optimal Trade Entry (OTE 0.705): `3.99`
  * Structural Invalidation Anchor (0.786): `4.01`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `4.01` | `4.01` | `3.98` | `4.00` | `592,465` | 2,366,387.68 USD | -707,200.75 USD | `-29.89%` | -35,932,471.77 USD | `-0.31` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `5m` | `4.00` | `4.00` | `3.97` | `3.99` | `685,918` | 2,733,492.48 USD | -453,127.82 USD | `-16.58%` | -36,385,599.59 USD | `-0.08` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `5m` | `3.98` | `4.00` | `3.98` | `3.98` | `149,134` | 594,923.33 USD | -5,736.57 USD | `-0.96%` | -36,391,336.16 USD | `+0.29` | **`BEARISH`** | `NEUTRAL CHOP` |
| `15m` | `4.03` | `4.04` | `3.98` | `3.99` | `1,482,938` | 5,936,404.63 USD | -215,302.69 USD | `-3.63%` | -35,219,664.47 USD | `+0.35` | **`BEARISH`** | `NEUTRAL CHOP` |
| `15m` | `3.99` | `4.03` | `3.95` | `4.01` | `2,752,687` | 11,016,623.88 USD | -5,606.55 USD | `-0.05%` | -35,225,271.02 USD | `+0.35` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `15m` | `4.01` | `4.01` | `3.97` | `3.98` | `1,427,517` | 5,694,803.49 USD | -1,166,065.14 USD | `-20.48%` | -36,391,336.16 USD | `-0.49` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `1h` | `4.11` | `4.12` | `4.04` | `4.06` | `10,668,517` | 43,520,640.79 USD | -835,968.86 USD | `-1.92%` | -28,300,361.50 USD | `+0.15` | **`BEARISH`** | `NEUTRAL CHOP` |
| `1h` | `4.06` | `4.08` | `3.90` | `3.99` | `24,939,110` | 99,515,350.06 USD | -6,770,272.40 USD | `-6.80%` | -35,070,633.89 USD | `-1.19` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `3.99` | `4.04` | `3.95` | `3.98` | `8,172,264` | 32,691,651.36 USD | -1,320,702.27 USD | `-4.04%` | -36,391,336.16 USD | `+0.11` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `4.65` | `4.69` | `4.38` | `4.40` | `28,351,581` | 128,263,626.10 USD | -4,168,943.82 USD | `-3.25%` | -16,525,751.06 USD | `-0.01` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `4.40` | `4.41` | `4.04` | `4.06` | `71,964,012` | 300,508,235.77 USD | -12,043,039.27 USD | `-4.01%` | -28,568,790.33 USD | `-0.87` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `4.06` | `4.08` | `3.90` | `3.98` | `33,112,729` | 132,212,399.46 USD | -8,085,712.05 USD | `-6.12%` | -36,654,502.38 USD | `-0.29` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `4.32` | `4.44` | `4.31` | `4.42` | `17,257,912` | 75,510,006.79 USD | -1,093,709.03 USD | `-1.45%` | -16,765,834.34 USD | `+1.00` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `4.42` | `4.66` | `4.38` | `4.65` | `38,831,237` | 175,324,190.65 USD | 4,409,027.10 USD | `+2.51%` | -12,356,807.24 USD | `+1.01` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `4.65` | `4.69` | `4.38` | `4.40` | `28,351,581` | 128,263,626.10 USD | -4,168,943.82 USD | `-3.25%` | -16,525,751.06 USD | `-0.01` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `4.40` | `4.41` | `4.04` | `4.06` | `71,964,012` | 300,508,235.77 USD | -12,043,039.27 USD | `-4.01%` | -28,568,790.33 USD | `-0.87` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `4.06` | `4.08` | `3.90` | `3.98` | `33,112,729` | 132,212,399.46 USD | -8,085,712.05 USD | `-6.12%` | -36,654,502.38 USD | `-0.29` | **`BEARISH`** | `DELTA ALIGNED` |

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
| --- | **`3.98`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `MID` | Regular L2 Book | - | - | - | Interbank L2 | 0.00% | Interbank |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 07:28:02 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `67` | `0x7737...bf66` | `LONG` | 22,527,662.94 USD | `5,640,376.30` | `2.35` | `4.00` | `0.7785` | 9,255,760.11 USD | `+41.09%` | `10X Cross` |
| `108` | `0xefe4...194b` | `SHORT` | 17,987,583.18 USD | `4,507,262.50` | `4.21` | `4.00` | `6.68` | 987,513.53 USD | `+5.49%` | `5X Cross` |
| `139` | `0xb581...6f4f` | `LONG` | 14,371,200.00 USD | `3,600,000.00` | `5.19` | `4.00` | `0.2703` | -4,321,835.22 USD | `-30.07%` | `4X Cross` |
| `219` | `0xdd53...2b13` | `SHORT` | 9,585,446.71 USD | `2,400,202.00` | `2.31` | `4.00` | `30.87` | -4,039,598.15 USD | `-42.14%` | `3X Cross` |
| `276` | `0x77ee...2902` | `LONG` | 8,234,556.70 USD | `2,063,023.10` | `1.93` | `4.00` | `0.000000` | 4,243,360.77 USD | `+51.53%` | `10X Cross` |
| `386` | `0xb83d...6e36` | `SHORT` | 5,773,494.39 USD | `1,445,759.10` | `5.19` | `4.00` | `102.03` | 1,735,954.55 USD | `+30.07%` | `3X Cross` |
| `406` | `0xb46b...538e` | `SHORT` | 5,327,300.00 USD | `1,336,000.00` | `4.33` | `4.00` | `7.58` | 457,564.06 USD | `+8.59%` | `10X Cross` |
| `414` | `0x7fda...17d1` | `SHORT` | 5,205,939.84 USD | `1,303,733.90` | `4.30` | `4.00` | `34.14` | 406,306.92 USD | `+7.80%` | `10X Cross` |
| `417` | `0x9df2...c665` | `SHORT` | 5,077,223.06 USD | `1,271,499.10` | `2.04` | `4.00` | `29.19` | -2,484,617.32 USD | `-48.94%` | `10X Cross` |
| `480` | `0x60b0...991e` | `LONG` | 4,477,267.12 USD | `1,121,307.10` | `5.00` | `4.00` | `0.000000` | -1,124,157.31 USD | `-25.11%` | `10X Cross` |
| `504` | `0xcac1...26b3` | `SHORT` | 4,282,734.92 USD | `1,073,743.90` | `2.48` | `4.00` | `12.39` | -1,622,791.46 USD | `-37.89%` | `10X Cross` |
| `525` | `0x781e...96b7` | `SHORT` | 4,139,705.52 USD | `1,039,604.60` | `2.45` | `4.00` | `7.63` | -1,595,368.33 USD | `-38.54%` | `10X Cross` |
| `605` | `0x45d2...4029` | `SHORT` | 3,623,049.60 USD | `909,400.00` | `3.26` | `4.00` | `52.98` | -656,899.70 USD | `-18.13%` | `10X Cross` |
| `855` | `0x005a...61fe` | `LONG` | 2,601,503.22 USD | `652,414.60` | `2.08` | `4.00` | `2.44` | 1,243,971.98 USD | `+47.82%` | `7X Cross` |
| `859` | `0xba5d...a352` | `SHORT` | 2,584,625.97 USD | `647,532.50` | `2.83` | `4.00` | `14.55` | -751,911.03 USD | `-29.09%` | `10X Cross` |
| `869` | `0xb695...a92d` | `SHORT` | 2,548,936.40 USD | `639,231.70` | `4.57` | `4.00` | `47.77` | 374,422.52 USD | `+14.69%` | `10X Cross` |
| `870` | `0xd1dd...9e85` | `SHORT` | 2,545,064.22 USD | `637,621.00` | `4.96` | `4.00` | `19.00` | 618,408.52 USD | `+24.30%` | `10X Cross` |
| `873` | `0x123d...3bff` | `SHORT` | 2,537,502.69 USD | `635,392.30` | `2.09` | `4.00` | `9.11` | -1,211,554.22 USD | `-47.75%` | `10X Cross` |
| `890` | `0xcf53...ee11` | `SHORT` | 2,484,031.53 USD | `621,598.40` | `5.07` | `4.00` | `25.78` | 668,138.73 USD | `+26.90%` | `10X Cross` |
| `1008` | `0xbfc7...80b4` | `SHORT` | 2,119,752.00 USD | `531,000.00` | `2.01` | `4.00` | `8.07` | -1,054,552.61 USD | `-49.75%` | `10X Cross` |
| `1287` | `0x2577...4897` | `LONG` | 1,653,931.31 USD | `414,456.80` | `4.13` | `4.00` | `0.000000` | -59,554.39 USD | `-3.60%` | `10X Cross` |
| `1291` | `0x0eec...d4c5` | `LONG` | 1,647,015.59 USD | `412,465.40` | `4.01` | `4.00` | `0.9916` | -5,720.09 USD | `-0.35%` | `10X Cross` |
| `1316` | `0x9aa5...58af` | `SHORT` | 1,610,060.72 USD | `403,443.10` | `4.78` | `4.00` | `27.65` | 317,852.66 USD | `+19.74%` | `10X Cross` |
| `1329` | `0xe097...d0fe` | `LONG` | 1,598,160.00 USD | `400,000.00` | `5.29` | `4.00` | `0.000000` | -518,627.30 USD | `-32.45%` | `10X Cross` |
| `1465` | `0x6e8f...4364` | `LONG` | 1,441,988.44 USD | `361,210.50` | `3.28` | `4.00` | `3.60` | 257,928.21 USD | `+17.89%` | `10X Cross` |
| `1481` | `0xef96...9383` | `SHORT` | 1,425,377.67 USD | `357,165.90` | `4.50` | `4.00` | `14.55` | 182,864.12 USD | `+12.83%` | `10X Cross` |
| `1507` | `0xdf95...7d72` | `SHORT` | 1,400,012.33 USD | `350,485.00` | `4.23` | `4.00` | `116.12` | 83,352.22 USD | `+5.95%` | `10X Cross` |
| `1510` | `0xcf67...eb24` | `LONG` | 1,397,760.00 USD | `350,000.00` | `1.98` | `4.00` | `1.88` | 706,142.12 USD | `+50.52%` | `10X Cross` |
| `1521` | `0x4cae...7c34` | `LONG` | 1,391,386.61 USD | `348,587.40` | `3.77` | `4.00` | `1.06` | 75,649.21 USD | `+5.44%` | `10X Cross` |
| `1617` | `0xfc27...9d9d` | `SHORT` | 1,274,563.64 USD | `319,997.70` | `5.01` | `4.00` | `66.79` | 328,978.98 USD | `+25.81%` | `10X Cross` |
| `1620` | `0x089f...a4f8` | `LONG` | 1,272,185.16 USD | `319,043.30` | `4.06` | `4.00` | `0.000000` | -22,671.55 USD | `-1.78%` | `1X Cross` |
| `1690` | `0x17c3...a868` | `LONG` | 1,206,198.34 USD | `301,874.10` | `4.37` | `4.00` | `0.000000` | -111,962.88 USD | `-9.28%` | `3X Cross` |
| `1700` | `0x9836...457e` | `LONG` | 1,193,852.39 USD | `300,000.60` | `4.57` | `4.00` | `1.92` | -178,220.78 USD | `-14.93%` | `10X Cross` |
| `1743` | `0xe065...0f85` | `SHORT` | 1,150,268.22 USD | `288,027.90` | `2.81` | `4.00` | `5.76` | -339,715.10 USD | `-29.53%` | `10X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `4.70` | 6,417.54 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Whale BUY: 6.42K USD at 4.7046 USD [API] | `2026-10-28 19:24:31` |
| `ANNOUNCEMENT` | `INFO` | `4.70` | 7,518.41 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Whale BUY: 7.52K USD at 4.7043 USD [API] | `2026-10-28 19:27:03` |
| `ANNOUNCEMENT` | `INFO` | `4.71` | 10,227.64 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Whale SELL: 10.23K USD at 4.7145 USD [API] | `2026-10-28 19:38:03` |
| `ANNOUNCEMENT` | `INFO` | `4.73` | 5,849.93 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Whale SELL: 5.85K USD at 4.7276 USD [API] | `2026-10-28 19:44:06` |
| `ANNOUNCEMENT` | `INFO` | `4.73` | 6,258.00 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Whale SELL: 6.26K USD at 4.7298 USD [API] | `2026-10-28 19:45:23` |
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
| `Live` | `Long Liquidation` | `0.8050` | 4,050.00 USD | 29,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8150` | 1,600.00 USD | 29,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8350` | 4,740,000.00 USD | 29,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8450` | 2,030.00 USD | 24,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8550` | 10,600.00 USD | 24,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8650` | 433.80 USD | 24,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8750` | 12,940.00 USD | 24,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8850` | 5,690.00 USD | 24,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8950` | 38,570.00 USD | 24,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9050` | 292.22 USD | 24,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9150` | 13,040.00 USD | 24,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9250` | 778.57 USD | 24,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9550` | 1,910.00 USD | 24,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9650` | 965.00 USD | 24,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9850` | 707.53 USD | 24,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9950` | 154,200.00 USD | 24,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.00` | 488.33 USD | 24,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.02` | 10,250.00 USD | 24,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.03` | 36,980.00 USD | 24,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.05` | 12,660.00 USD | 24,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.06` | 892.90 USD | 24,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.07` | 7,510.00 USD | 24,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.08` | 216.89 USD | 24,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.10` | 4,270.00 USD | 24,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.11` | 1,150.00 USD | 24,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.12` | 301.95 USD | 24,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.14` | 4,960.00 USD | 24,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.15` | 34,680.00 USD | 24,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.18` | 184.59 USD | 24,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.19` | 1,000.00 USD | 24,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.20` | 173.51 USD | 24,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.21` | 149.66 USD | 24,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.22` | 2,580.00 USD | 24,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.23` | 255.41 USD | 24,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.24` | 243.05 USD | 24,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.25` | 43,220.00 USD | 24,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.25` | 115,200.00 USD | 24,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.26` | 2,060.00 USD | 24,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.27` | 2,390.00 USD | 24,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.28` | 2,040.00 USD | 24,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.29` | 2,180.00 USD | 24,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.30` | 4,240.00 USD | 24,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.31` | 11,180.00 USD | 24,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.32` | 10,050.00 USD | 24,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.33` | 417.32 USD | 24,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.34` | 603.91 USD | 24,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.35` | 65,120.00 USD | 24,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.36` | 911.41 USD | 24,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.38` | 14,580.00 USD | 24,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.39` | 295.56 USD | 24,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.40` | 42,490.00 USD | 24,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.42` | 2,020.00 USD | 24,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.43` | 712.50 USD | 24,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.45` | 362,290.00 USD | 24,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.47` | 429.83 USD | 23,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.48` | 1,990.00 USD | 23,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.50` | 743.46 USD | 23,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.50` | 3,150.00 USD | 23,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.51` | 7,190.00 USD | 23,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.52` | 610.00 USD | 23,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.53` | 279.37 USD | 23,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.56` | 14,130.00 USD | 23,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.57` | 589.52 USD | 23,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.58` | 16,170.00 USD | 23,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.59` | 83,130.00 USD | 23,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.60` | 47,140.00 USD | 23,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.61` | 4,770.00 USD | 23,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.62` | 12,250.00 USD | 23,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.64` | 2,150.00 USD | 23,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.65` | 981.08 USD | 23,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.66` | 384.13 USD | 23,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.67` | 212.29 USD | 23,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.68` | 108.71 USD | 23,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.69` | 602,850.00 USD | 23,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.70` | 4,980.00 USD | 22,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.71` | 168.97 USD | 22,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.73` | 5,630.00 USD | 22,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.74` | 1,320.00 USD | 22,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.75` | 10,710.00 USD | 22,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.76` | 1,090.00 USD | 22,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.77` | 17,220.00 USD | 22,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.78` | 1,210.00 USD | 22,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.80` | 5,280.00 USD | 22,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.81` | 1,580.00 USD | 22,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.82` | 1,280.00 USD | 22,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.83` | 27,520.00 USD | 22,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.85` | 2,040.00 USD | 22,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.86` | 652.75 USD | 22,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.88` | 937.50 USD | 22,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.90` | 2,080.00 USD | 22,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.91` | 62,210.00 USD | 22,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.92` | 3,110.00 USD | 22,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.93` | 35,380.00 USD | 22,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.94` | 10,800.00 USD | 22,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.95` | 2,740.00 USD | 22,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.96` | 775.55 USD | 22,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.97` | 5,930.00 USD | 22,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.98` | 47,310.00 USD | 22,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.99` | 2,450.00 USD | 22,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.00` | 124,920.00 USD | 22,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.02` | 260.62 USD | 22,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.04` | 3,460.00 USD | 22,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.06` | 7,750.00 USD | 22,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.08` | 2,780.00 USD | 22,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.08` | 10,480.00 USD | 22,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.10` | 1,100.00 USD | 22,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.10` | 7,520.00 USD | 22,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.12` | 11,960.00 USD | 22,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.12` | 96,590.00 USD | 22,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.13` | 202.82 USD | 22,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.15` | 2,110.00 USD | 22,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.15` | 773.00 USD | 22,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.17` | 1,520.00 USD | 22,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.17` | 13,580.00 USD | 22,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.19` | 15,070.00 USD | 22,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.19` | 815.44 USD | 22,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.21` | 76,110.00 USD | 22,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.21` | 4,190.00 USD | 22,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.23` | 20,940.00 USD | 22,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.23` | 3,400.00 USD | 22,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.25` | 44,890.00 USD | 22,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.25` | 149,130.00 USD | 22,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.27` | 7,930.00 USD | 21,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.27` | 529.85 USD | 21,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.29` | 10,720.00 USD | 21,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.29` | 306,010.00 USD | 21,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.31` | 1,980.00 USD | 21,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.31` | 105,380.00 USD | 21,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.33` | 237,770.00 USD | 21,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.33` | 4,240.00 USD | 21,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.35` | 58,430.00 USD | 21,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.35` | 143.66 USD | 21,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.37` | 30,230.00 USD | 21,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.38` | 419,870.00 USD | 21,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.38` | 1,640.00 USD | 20,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.40` | 27,900.00 USD | 20,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.40` | 1,570.00 USD | 20,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.42` | 1,770,000.00 USD | 20,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.42` | 273,060.00 USD | 19,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.44` | 2,680.00 USD | 18,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.44` | 4,260.00 USD | 18,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.46` | 137,190.00 USD | 18,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.46` | 11,160.00 USD | 18,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.48` | 340.81 USD | 18,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.48` | 19,450.00 USD | 18,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.50` | 1,110.00 USD | 18,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.50` | 8,240.00 USD | 18,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.52` | 121.98 USD | 18,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.52` | 19,460.00 USD | 18,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.54` | 698.39 USD | 18,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.54` | 10,920.00 USD | 18,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.56` | 5,800.00 USD | 18,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.56` | 53,870.00 USD | 18,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.58` | 11,910.00 USD | 18,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.58` | 1,570.00 USD | 18,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.60` | 75,100.00 USD | 18,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.60` | 21,590.00 USD | 18,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.62` | 17,370.00 USD | 18,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.62` | 224.44 USD | 18,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.63` | 25,170.00 USD | 18,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.65` | 9,050.00 USD | 18,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.65` | 18,970.00 USD | 18,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.67` | 4,580.00 USD | 18,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.67` | 1,760.00 USD | 18,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.69` | 7,280.00 USD | 18,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.69` | 6,230.00 USD | 18,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.71` | 120,220.00 USD | 18,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.71` | 15,010.00 USD | 18,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.73` | 27,130.00 USD | 18,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.73` | 42,810.00 USD | 18,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.75` | 47,240.00 USD | 18,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.75` | 1,670.00 USD | 18,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.77` | 6,730.00 USD | 18,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.77` | 719.84 USD | 18,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.79` | 26,980.00 USD | 18,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.79` | 24,560.00 USD | 17,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.81` | 6,310.00 USD | 17,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.81` | 11,780.00 USD | 17,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.83` | 260,210.00 USD | 17,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.83` | 10,470.00 USD | 17,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.85` | 4,240.00 USD | 17,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.85` | 1,860.00 USD | 17,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.87` | 8,570.00 USD | 17,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.88` | 378,680.00 USD | 17,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.88` | 52,190.00 USD | 17,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.90` | 101,800.00 USD | 17,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.90` | 1,330.00 USD | 17,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.92` | 93,010.00 USD | 17,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.92` | 191,130.00 USD | 17,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.94` | 61,920.00 USD | 16,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.94` | 1,010.00 USD | 16,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.96` | 2,710,000.00 USD | 16,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.96` | 1,050.00 USD | 14,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.98` | 11,090.00 USD | 14,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.98` | 22,840.00 USD | 14,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.00` | 366,890.00 USD | 14,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.00` | 10,410.00 USD | 13,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.02` | 11,290.00 USD | 13,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.02` | 27,700.00 USD | 13,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.04` | 149.63 USD | 13,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.04` | 103,780.00 USD | 13,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.06` | 245,370.00 USD | 13,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.06` | 115,550.00 USD | 13,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.08` | 13,960.00 USD | 13,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.08` | 146,750.00 USD | 13,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.10` | 5,540.00 USD | 12,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.10` | 45,400.00 USD | 12,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.12` | 20,110.00 USD | 12,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.12` | 9,680.00 USD | 12,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.13` | 37,690.00 USD | 12,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.15` | 11,350.00 USD | 12,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.15` | 7,580.00 USD | 12,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.17` | 10,030.00 USD | 12,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.17` | 5,350.00 USD | 12,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.19` | 630,260.00 USD | 12,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.19` | 6,250.00 USD | 12,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.21` | 104,290.00 USD | 12,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.21` | 13,860.00 USD | 12,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.23` | 25,260.00 USD | 12,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.23` | 53,140.00 USD | 12,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.25` | 17,670.00 USD | 11,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.25` | 18,010.00 USD | 11,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.27` | 33,820.00 USD | 11,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.27` | 842,170.00 USD | 11,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.29` | 2,680.00 USD | 11,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.29` | 209,990.00 USD | 11,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.31` | 141,170.00 USD | 10,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.31` | 29,280.00 USD | 10,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.33` | 24,800.00 USD | 10,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.33` | 64,220.00 USD | 10,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.35` | 40,110.00 USD | 10,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.37` | 137,860.00 USD | 10,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.38` | 569,260.00 USD | 10,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.38` | 44,450.00 USD | 9,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.40` | 844.34 USD | 9,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.40` | 76,570.00 USD | 9,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.42` | 181,600.00 USD | 9,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.42` | 5,290.00 USD | 9,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.44` | 23,970.00 USD | 9,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.44` | 9,830.00 USD | 9,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.46` | 9,260.00 USD | 9,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.46` | 14,440.00 USD | 9,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.48` | 105,220.00 USD | 9,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.48` | 74,160.00 USD | 9,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.50` | 24,030.00 USD | 9,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.50` | 45,750.00 USD | 9,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.52` | 11,870.00 USD | 9,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.52` | 129,140.00 USD | 9,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.54` | 163,400.00 USD | 9,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.54` | 254,870.00 USD | 8,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.56` | 377,070.00 USD | 8,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.56` | 15,510.00 USD | 8,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.58` | 34,970.00 USD | 8,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.58` | 1,330,000.00 USD | 8,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.59` | 12,300,000.00 USD | 12,300,000.00 USD | 176,290.00 USD | 66,810.00 USD | 144,570.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.60` | 45,700.00 USD | 6,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.60` | 11,920,000.00 USD | 11,920,000.00 USD | 64,170.00 USD | 21,460.00 USD | 22,050.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.60` | 150,210.00 USD | 6,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.61` | 11,810,000.00 USD | 11,810,000.00 USD | 55,130.00 USD | 17,400.00 USD | 44,890.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.62` | 29,400.00 USD | 6,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.62` | 11,690,000.00 USD | 11,690,000.00 USD | 92,130.00 USD | 26,640.00 USD | 97,570.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.62` | 45,760.00 USD | 6,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.63` | 5,930,000.00 USD | 5,930,000.00 USD | 1,910.00 USD | 9,650.00 USD | 22,610.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.63` | 11,480,000.00 USD | 11,480,000.00 USD | 50,840.00 USD | 8,120.00 USD | 159.02 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.63` | 50,630.00 USD | 6,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.64` | 5,900,000.00 USD | 5,900,000.00 USD | 152.80 USD | 5,040.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.64` | 11,420,000.00 USD | 11,420,000.00 USD | 2,410.00 USD | 14,370.00 USD | 119,140.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.65` | 55,690.00 USD | 6,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.65` | 5,890,000.00 USD | 5,890,000.00 USD | 386.30 USD | 0.00 USD | 13.37 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.65` | 11,280,000.00 USD | 11,280,000.00 USD | 52,910.00 USD | 7,050.00 USD | 31,190.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.65` | 26,080.00 USD | 6,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.66` | 5,890,000.00 USD | 5,890,000.00 USD | 291.38 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.66` | 11,190,000.00 USD | 11,190,000.00 USD | 30,480.00 USD | 15,090.00 USD | 125,270.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.67` | 912,270.00 USD | 6,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.67` | 5,890,000.00 USD | 5,890,000.00 USD | 16,750.00 USD | 3,070.00 USD | 11,520.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.67` | 11,020,000.00 USD | 11,020,000.00 USD | 47,650.00 USD | 14,480.00 USD | 53,670.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.67` | 257,380.00 USD | 5,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.68` | 5,860,000.00 USD | 5,860,000.00 USD | 216.77 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.69` | 111,250.00 USD | 5,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.69` | 5,860,000.00 USD | 5,860,000.00 USD | 23,960.00 USD | 0.00 USD | 281.19 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.69` | 10,900,000.00 USD | 10,900,000.00 USD | 27,750.00 USD | 0.00 USD | 59,840.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.69` | 112,450.00 USD | 5,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.70` | 5,840,000.00 USD | 5,840,000.00 USD | 39,190.00 USD | 4,110.00 USD | 55,010.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.70` | 10,820,000.00 USD | 10,820,000.00 USD | 20,470.00 USD | 7,370.00 USD | 112,470.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.71` | 64,270.00 USD | 5,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.71` | 5,740,000.00 USD | 5,740,000.00 USD | 430.40 USD | 0.00 USD | 522.93 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.71` | 10,680,000.00 USD | 10,680,000.00 USD | 50,620.00 USD | 0.00 USD | 74,330.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.71` | 194,120.00 USD | 5,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.72` | 5,740,000.00 USD | 5,740,000.00 USD | 403.05 USD | 0.00 USD | 18.60 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.72` | 10,550,000.00 USD | 10,550,000.00 USD | 425.03 USD | 0.00 USD | 183.06 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.73` | 28,060.00 USD | 4,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.73` | 5,740,000.00 USD | 5,740,000.00 USD | 8,890.00 USD | 6,020.00 USD | 8,370.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.73` | 10,550,000.00 USD | 10,550,000.00 USD | 38,260.00 USD | 10,880.00 USD | 56,790.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.73` | 5,760.00 USD | 4,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.74` | 5,710,000.00 USD | 5,710,000.00 USD | 94,200.00 USD | 33,110.00 USD | 42,360.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.74` | 10,440,000.00 USD | 10,440,000.00 USD | 128,440.00 USD | 40,020.00 USD | 122,480.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.75` | 58,120.00 USD | 4,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.75` | 5,540,000.00 USD | 5,540,000.00 USD | 0.00 USD | 0.00 USD | 20,450.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.75` | 10,150,000.00 USD | 10,150,000.00 USD | 1,770.00 USD | 24,350.00 USD | 42,760.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.75` | 80,510.00 USD | 4,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.76` | 5,520,000.00 USD | 5,520,000.00 USD | 0.00 USD | 2,230.00 USD | 10,030.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.76` | 10,080,000.00 USD | 10,080,000.00 USD | 32,650.00 USD | 10,110.00 USD | 22,610.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.77` | 65,500.00 USD | 4,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.77` | 5,510,000.00 USD | 5,510,000.00 USD | 187.12 USD | 5,330.00 USD | 2,020.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.77` | 10,020,000.00 USD | 10,020,000.00 USD | 13,170.00 USD | 8,090.00 USD | 23,020.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.77` | 127,760.00 USD | 4,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.78` | 5,500,000.00 USD | 5,500,000.00 USD | 106.91 USD | 4,490.00 USD | 29,810.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.78` | 9,970,000.00 USD | 9,970,000.00 USD | 21,640.00 USD | 15,520.00 USD | 41,570.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.79` | 49,180.00 USD | 4,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.79` | 5,470,000.00 USD | 5,470,000.00 USD | 472.79 USD | 0.00 USD | 176.51 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.79` | 9,900,000.00 USD | 9,900,000.00 USD | 49,420.00 USD | 0.00 USD | 38,980.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.79` | 139,870.00 USD | 4,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.80` | 5,470,000.00 USD | 5,470,000.00 USD | 1,270.00 USD | 0.00 USD | 1,720.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.80` | 9,810,000.00 USD | 9,810,000.00 USD | 1,530.00 USD | 18,170.00 USD | 17,780.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.81` | 7,720.00 USD | 4,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.81` | 5,470,000.00 USD | 5,470,000.00 USD | 54,290.00 USD | 0.00 USD | 13,100.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.81` | 9,770,000.00 USD | 9,770,000.00 USD | 0.00 USD | 0.00 USD | 1,350.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.81` | 25,230.00 USD | 4,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.82` | 5,400,000.00 USD | 5,400,000.00 USD | 487.48 USD | 11,960.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.82` | 9,770,000.00 USD | 9,770,000.00 USD | 527.85 USD | 18,370.00 USD | 25,600.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.83` | 53,580.00 USD | 4,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.83` | 5,390,000.00 USD | 5,390,000.00 USD | 1,150.00 USD | 18,900.00 USD | 17,280.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.83` | 9,720,000.00 USD | 9,720,000.00 USD | 0.00 USD | 0.00 USD | 89.29 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.83` | 158,690.00 USD | 4,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.84` | 5,350,000.00 USD | 5,350,000.00 USD | 0.00 USD | 0.00 USD | 784.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.84` | 9,720,000.00 USD | 9,720,000.00 USD | 2,020.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.85` | 96,570.00 USD | 4,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.85` | 5,350,000.00 USD | 5,350,000.00 USD | 929.01 USD | 6,330.00 USD | 141.64 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.85` | 9,720,000.00 USD | 9,720,000.00 USD | 0.00 USD | 0.00 USD | 5,500.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.85` | 21,270.00 USD | 3,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.86` | 5,340,000.00 USD | 5,340,000.00 USD | 2,080.00 USD | 12,320.00 USD | 54,290.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.86` | 9,720,000.00 USD | 9,720,000.00 USD | 2,220.00 USD | 0.00 USD | 72,520.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.87` | 26,000.00 USD | 3,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.87` | 5,270,000.00 USD | 5,270,000.00 USD | 1,690.00 USD | 11,800.00 USD | 845.92 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.87` | 9,640,000.00 USD | 9,640,000.00 USD | 57,040.00 USD | 0.00 USD | 29,890.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.88` | 22,850.00 USD | 3,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.88` | 5,260,000.00 USD | 5,260,000.00 USD | 106,680.00 USD | 6,860.00 USD | 39,950.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.88` | 9,550,000.00 USD | 9,550,000.00 USD | 106,950.00 USD | 8,890.00 USD | 101,810.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.88` | 108,570.00 USD | 3,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.89` | 5,100,000.00 USD | 5,100,000.00 USD | 113,490.00 USD | 37,150.00 USD | 23,350.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.89` | 9,340,000.00 USD | 9,340,000.00 USD | 1,210.00 USD | 50,710.00 USD | 1,390.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.90` | 5,490.00 USD | 3,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.90` | 4,930,000.00 USD | 4,930,000.00 USD | 31,410.00 USD | 10,910.00 USD | 21,360.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.90` | 9,280,000.00 USD | 9,280,000.00 USD | 171,750.00 USD | 28,250.00 USD | 51,570.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.90` | 10,170.00 USD | 3,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.91` | 4,870,000.00 USD | 4,870,000.00 USD | 32,140.00 USD | 35,760.00 USD | 39,260.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.91` | 9,030,000.00 USD | 9,030,000.00 USD | 3,970.00 USD | 25,680.00 USD | 46,930.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.92` | 37,980.00 USD | 3,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.92` | 4,760,000.00 USD | 4,760,000.00 USD | 148,140.00 USD | 26,030.00 USD | 33,330.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.92` | 8,960,000.00 USD | 8,960,000.00 USD | 90,780.00 USD | 41,330.00 USD | 89,160.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.92` | 723,590.00 USD | 3,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.93` | 4,550,000.00 USD | 4,550,000.00 USD | 0.00 USD | 29,900.00 USD | 38,510.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.93` | 8,730,000.00 USD | 8,730,000.00 USD | 51,660.00 USD | 20,780.00 USD | 19,870.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.94` | 202,910.00 USD | 3,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.94` | 4,480,000.00 USD | 4,480,000.00 USD | 96,340.00 USD | 14,940.00 USD | 20,530.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.94` | 8,640,000.00 USD | 8,640,000.00 USD | 82,440.00 USD | 31,050.00 USD | 96,310.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.94` | 33,430.00 USD | 2,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.95` | 4,350,000.00 USD | 4,350,000.00 USD | 95,940.00 USD | 15,880.00 USD | 95,070.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.95` | 8,430,000.00 USD | 8,430,000.00 USD | 8,490.00 USD | 19,870.00 USD | 2,700.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.96` | 599,170.00 USD | 2,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.96` | 4,150,000.00 USD | 4,150,000.00 USD | 65,960.00 USD | 39,680.00 USD | 36,690.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.96` | 8,400,000.00 USD | 8,400,000.00 USD | 166,560.00 USD | 15,590.00 USD | 312,280.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.96` | 218,010.00 USD | 2,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.97` | 4,000,000.00 USD | 4,000,000.00 USD | 190,720.00 USD | 66,010.00 USD | 102,960.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.97` | 7,910,000.00 USD | 7,910,000.00 USD | 231,790.00 USD | 102,960.00 USD | 271,360.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.98` | 477,730.00 USD | 1,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.98` | 3,640,000.00 USD | 3,640,000.00 USD | 192,590.00 USD | 43,880.00 USD | 14,880.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.98` | 7,300,000.00 USD | 7,300,000.00 USD | 295,470.00 USD | 147,090.00 USD | 230,240.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.98` | 151,930.00 USD | 1,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.99` | 3,390,000.00 USD | 3,390,000.00 USD | 413,960.00 USD | 106,190.00 USD | 138,330.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.99` | 6,630,000.00 USD | 6,630,000.00 USD | 63,200.00 USD | 103,210.00 USD | 78,470.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.00` | 223,790.00 USD | 1,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.00` | 2,730,000.00 USD | 2,730,000.00 USD | 35,730.00 USD | 53,390.00 USD | 134,490.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.00` | 6,380,000.00 USD | 6,380,000.00 USD | 317,210.00 USD | 126,990.00 USD | 166,390.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.00` | 57,890.00 USD | 1,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.01` | 2,510,000.00 USD | 2,510,000.00 USD | 112,570.00 USD | 72,850.00 USD | 129,520.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.01` | 5,770,000.00 USD | 5,770,000.00 USD | 392,150.00 USD | 94,720.00 USD | 438,650.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.01` | 73,860.00 USD | 1,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.02` | 2,190,000.00 USD | 2,190,000.00 USD | 243,600.00 USD | 50,310.00 USD | 107,340.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.02` | 4,850,000.00 USD | 4,850,000.00 USD | 279,800.00 USD | 88,330.00 USD | 250,940.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.03` | 128,600.00 USD | 979,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.03` | 1,790,000.00 USD | 1,790,000.00 USD | 189,730.00 USD | 76,190.00 USD | 266,680.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.03` | 4,230,000.00 USD | 4,230,000.00 USD | 250,870.00 USD | 45,290.00 USD | 147,160.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.04` | 20,250.00 USD | 850,910.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.04` | 1,260,000.00 USD | 1,260,000.00 USD | 105,670.00 USD | 48,960.00 USD | 207,560.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.04` | 3,780,000.00 USD | 3,780,000.00 USD | 326,350.00 USD | 65,670.00 USD | 491,840.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.04` | 120,800.00 USD | 830,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.05` | 898,580.00 USD | 898,580.00 USD | 2,370.00 USD | 46,690.00 USD | 95,690.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.05` | 2,900,000.00 USD | 2,900,000.00 USD | 291,930.00 USD | 117,530.00 USD | 85,640.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.05` | 24,810.00 USD | 709,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.06` | 753,820.00 USD | 753,820.00 USD | 0.00 USD | 27,150.00 USD | 125,920.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.06` | 2,410,000.00 USD | 2,410,000.00 USD | 305,310.00 USD | 72,410.00 USD | 187,820.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.07` | 324,890.00 USD | 685,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.07` | 600,750.00 USD | 600,750.00 USD | 0.00 USD | 72,110.00 USD | 22,350.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.07` | 1,840,000.00 USD | 1,840,000.00 USD | 715,320.00 USD | 219,920.00 USD | 329,160.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.08` | 90,340.00 USD | 360,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.08` | 506,300.00 USD | 506,300.00 USD | 506,300.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.08` | 575,150.00 USD | 575,150.00 USD | 9,180.00 USD | 117,780.00 USD | 229,680.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.09` | 218,520.00 USD | 218,520.00 USD | 134,630.00 USD | 83,890.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.10` | 143,210.00 USD | 143,210.00 USD | 24,900.00 USD | 118,310.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.10` | 286,420.00 USD | 286,420.00 USD | 24,900.00 USD | 118,310.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.11` | 269,820.00 USD | 269,820.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.12` | 309,660.00 USD | 309,660.00 USD | 0.00 USD | 80,980.00 USD | 228,680.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.13` | 471,110.00 USD | 471,110.00 USD | 0.00 USD | 0.00 USD | 161,450.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.14` | 531,130.00 USD | 531,130.00 USD | 60,020.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.14` | 377,250.00 USD | 377,250.00 USD | 0.00 USD | 90,830.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.15` | 595,400.00 USD | 595,400.00 USD | 64,270.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.15` | 431,140.00 USD | 431,140.00 USD | 0.00 USD | 53,890.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.17` | 664,710.00 USD | 664,710.00 USD | 0.00 USD | 16,800.00 USD | 52,510.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.18` | 874,490.00 USD | 874,490.00 USD | 192,730.00 USD | 17,040.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.19` | 1,250,000.00 USD | 1,250,000.00 USD | 174,270.00 USD | 20,540.00 USD | 185,170.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.20` | 6,930.00 USD | 6,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `4.20` | 1,030,000.00 USD | 1,030,000.00 USD | 227,690.00 USD | 0.00 USD | 371,630.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.21` | 1,330,000.00 USD | 1,330,000.00 USD | 58,200.00 USD | 20,820.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.22` | 1,530,000.00 USD | 1,530,000.00 USD | 97,990.00 USD | 27,150.00 USD | 74,260.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.23` | 2,200,000.00 USD | 2,200,000.00 USD | 203,550.00 USD | 468,020.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.24` | 2,880,000.00 USD | 2,880,000.00 USD | 506,300.00 USD | 0.00 USD | 173,430.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.25` | 3,210,000.00 USD | 3,210,000.00 USD | 0.00 USD | 72,920.00 USD | 255,640.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.25` | 1,090,000.00 USD | 1,090,000.00 USD | 0.00 USD | 57,340.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.26` | 3,480,000.00 USD | 3,480,000.00 USD | 92,160.00 USD | 173,320.00 USD | 248.22 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.26` | 1,820,000.00 USD | 1,820,000.00 USD | 0.00 USD | 378,440.00 USD | 355,620.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.27` | 4,340,000.00 USD | 4,340,000.00 USD | 677,660.00 USD | 34,890.00 USD | 152,200.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.27` | 3,610,000.00 USD | 3,610,000.00 USD | 18,140.00 USD | 194,220.00 USD | 1,580,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.28` | 9,850.00 USD | 16,780.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.28` | 4,970,000.00 USD | 4,970,000.00 USD | 305,690.00 USD | 30,410.00 USD | 288,910.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.28` | 5,520,000.00 USD | 5,520,000.00 USD | 113,840.00 USD | 497,680.00 USD | 1,300,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.29` | 207.39 USD | 16,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.29` | 5,320,000.00 USD | 5,320,000.00 USD | 153,130.00 USD | 32,690.00 USD | 161,450.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.29` | 5,570,000.00 USD | 5,570,000.00 USD | 0.00 USD | 46,530.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.30` | 5,560,000.00 USD | 5,560,000.00 USD | 32,410.00 USD | 45,120.00 USD | 163,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.30` | 6,040,000.00 USD | 6,040,000.00 USD | 214,920.00 USD | 180,920.00 USD | 75,610.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.30` | 2,770.00 USD | 19,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.31` | 5,970,000.00 USD | 5,970,000.00 USD | 304,920.00 USD | 13,580.00 USD | 95,430.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.31` | 6,470,000.00 USD | 6,470,000.00 USD | 213,530.00 USD | 53,890.00 USD | 170,400.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.32` | 2,280.00 USD | 22,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.32` | 6,130,000.00 USD | 6,130,000.00 USD | 86,850.00 USD | 73,400.00 USD | 18.65 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.32` | 7,120,000.00 USD | 7,120,000.00 USD | 265,720.00 USD | 160,980.00 USD | 222,930.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.33` | 10,090.00 USD | 32,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.33` | 6,570,000.00 USD | 6,570,000.00 USD | 255,620.00 USD | 93,880.00 USD | 87,760.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.33` | 7,240,000.00 USD | 7,240,000.00 USD | 2,690.00 USD | 27,170.00 USD | 88,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.33` | 1,450.00 USD | 33,580.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.34` | 7,090,000.00 USD | 7,090,000.00 USD | 270,720.00 USD | 140,540.00 USD | 114,690.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.34` | 7,420,000.00 USD | 7,420,000.00 USD | 4,550.00 USD | 28,670.00 USD | 141,900.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.34` | 8,680.00 USD | 42,250.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.35` | 7,180,000.00 USD | 7,180,000.00 USD | 855.62 USD | 0.00 USD | 84,830.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.35` | 7,500,000.00 USD | 7,500,000.00 USD | 0.00 USD | 0.00 USD | 85,370.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.36` | 5,540.00 USD | 47,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.36` | 7,310,000.00 USD | 7,310,000.00 USD | 84,880.00 USD | 12,310.00 USD | 31,110.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.36` | 7,650,000.00 USD | 7,650,000.00 USD | 8,190.00 USD | 0.00 USD | 140,550.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.37` | 7,540,000.00 USD | 7,540,000.00 USD | 52,520.00 USD | 46,860.00 USD | 130,010.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.38` | 6,680.00 USD | 54,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.38` | 8,380,000.00 USD | 8,380,000.00 USD | 248,590.00 USD | 34,500.00 USD | 559,230.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.38` | 8,050,000.00 USD | 8,050,000.00 USD | 0.00 USD | 141,930.00 USD | 261,380.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.38` | 25,830.00 USD | 80,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.39` | 8,710,000.00 USD | 8,710,000.00 USD | 399.48 USD | 17,360.00 USD | 310,880.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.39` | 8,570,000.00 USD | 8,570,000.00 USD | 248,520.00 USD | 108,260.00 USD | 154,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.39` | 14,050.00 USD | 94,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.40` | 9,110,000.00 USD | 9,110,000.00 USD | 288,790.00 USD | 34,040.00 USD | 81,970.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.40` | 9,170,000.00 USD | 9,170,000.00 USD | 108,780.00 USD | 26,950.00 USD | 463,990.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.41` | 1,410.00 USD | 95,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.41` | 9,490,000.00 USD | 9,490,000.00 USD | 196,820.00 USD | 112,990.00 USD | 65,530.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.41` | 9,490,000.00 USD | 9,490,000.00 USD | 0.00 USD | 45,930.00 USD | 278,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.42` | 53,320.00 USD | 149,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.42` | 9,540,000.00 USD | 9,540,000.00 USD | 0.00 USD | 47,240.00 USD | 774.54 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.42` | 10,140,000.00 USD | 10,140,000.00 USD | 404,280.00 USD | 71,590.00 USD | 175,990.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.42` | 104.87 USD | 149,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.43` | 9,690,000.00 USD | 9,690,000.00 USD | 5,100.00 USD | 49,400.00 USD | 98,670.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.43` | 10,420,000.00 USD | 10,420,000.00 USD | 163,540.00 USD | 46,230.00 USD | 71,660.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.43` | 25,500.00 USD | 174,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.44` | 10,470,000.00 USD | 10,470,000.00 USD | 154,480.00 USD | 339,100.00 USD | 290,890.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.44` | 10,610,000.00 USD | 10,610,000.00 USD | 0.00 USD | 116,400.00 USD | 72,830.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.45` | 10,530,000.00 USD | 10,530,000.00 USD | 649.63 USD | 50,720.00 USD | 1,400.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.46` | 10,540,000.00 USD | 10,540,000.00 USD | 704.30 USD | 9,070.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.46` | 10,680,000.00 USD | 10,680,000.00 USD | 0.00 USD | 62,110.00 USD | 2,080.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.46` | 468.38 USD | 175,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.47` | 10,570,000.00 USD | 10,570,000.00 USD | 210.23 USD | 16,700.00 USD | 18,310.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.47` | 11,020,000.00 USD | 11,020,000.00 USD | 203,160.00 USD | 135,940.00 USD | 2,060.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.47` | 1,260.00 USD | 176,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.48` | 10,790,000.00 USD | 10,790,000.00 USD | 117,480.00 USD | 73,240.00 USD | 26,920.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.48` | 11,020,000.00 USD | 11,020,000.00 USD | 0.00 USD | 0.00 USD | 1,510.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.49` | 15,150.00 USD | 191,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.49` | 11,350,000.00 USD | 11,350,000.00 USD | 252,600.00 USD | 155,000.00 USD | 150,280.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.49` | 11,360,000.00 USD | 11,360,000.00 USD | 242,770.00 USD | 93,790.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.50` | 90,180.00 USD | 281,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.50` | 11,890,000.00 USD | 11,890,000.00 USD | 361,770.00 USD | 65,710.00 USD | 120,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.50` | 11,930,000.00 USD | 11,930,000.00 USD | 373,240.00 USD | 200,700.00 USD | 1,820.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.50` | 268.05 USD | 282,010.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.51` | 12,700,000.00 USD | 12,700,000.00 USD | 186,860.00 USD | 307,580.00 USD | 312,530.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.51` | 12,010,000.00 USD | 12,010,000.00 USD | 77,780.00 USD | 0.00 USD | 2,030.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.52` | 13,320,000.00 USD | 13,320,000.00 USD | 287,830.00 USD | 92,260.00 USD | 242,880.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.52` | 12,150,000.00 USD | 12,150,000.00 USD | 2,080.00 USD | 0.00 USD | 138,450.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.53` | 18,100.00 USD | 300,110.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.53` | 14,090,000.00 USD | 14,090,000.00 USD | 487,540.00 USD | 0.00 USD | 279,080.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.53` | 13,130,000.00 USD | 13,130,000.00 USD | 438,070.00 USD | 232,800.00 USD | 309,560.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.54` | 14,810,000.00 USD | 14,810,000.00 USD | 216.65 USD | 150,600.00 USD | 564,340.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.54` | 14,370,000.00 USD | 14,370,000.00 USD | 0.00 USD | 0.00 USD | 1,240,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.54` | 252.70 USD | 300,370.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.55` | 15,020,000.00 USD | 15,020,000.00 USD | 0.00 USD | 22,540.00 USD | 195,790.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.56` | 15,430,000.00 USD | 15,430,000.00 USD | 79,110.00 USD | 32,800.00 USD | 288,660.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.56` | 14,850,000.00 USD | 14,850,000.00 USD | 361,350.00 USD | 124,220.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.57` | 15,740,000.00 USD | 15,740,000.00 USD | 177,440.00 USD | 70,180.00 USD | 67,980.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.57` | 15,400,000.00 USD | 15,400,000.00 USD | 305,830.00 USD | 27,650.00 USD | 209,310.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.58` | 17,200,000.00 USD | 17,200,000.00 USD | 506,750.00 USD | 73,690.00 USD | 875,260.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.58` | 15,530,000.00 USD | 15,530,000.00 USD | 44,380.00 USD | 0.00 USD | 85,990.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.59` | 18,180,000.00 USD | 18,180,000.00 USD | 826,150.00 USD | 75,460.00 USD | 79,420.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.59` | 17,120,000.00 USD | 17,120,000.00 USD | 760,880.00 USD | 40,640.00 USD | 794,930.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.59` | 9,190.00 USD | 309,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.60` | 18,380,000.00 USD | 18,380,000.00 USD | 54,450.00 USD | 84,420.00 USD | 66,160.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.60` | 17,240,000.00 USD | 17,240,000.00 USD | 3,460.00 USD | 112,080.00 USD | 2,360.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.61` | 1,050.00 USD | 310,600.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.61` | 18,520,000.00 USD | 18,520,000.00 USD | 66,620.00 USD | 7,560.00 USD | 60,990.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.61` | 17,250,000.00 USD | 17,250,000.00 USD | 3,350.00 USD | 0.00 USD | 960.97 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.62` | 18,670,000.00 USD | 18,670,000.00 USD | 95,090.00 USD | 31,380.00 USD | 21,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.62` | 17,380,000.00 USD | 17,380,000.00 USD | 134,680.00 USD | 0.00 USD | 2,720.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.62` | 203.50 USD | 310,810.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.63` | 18,670,000.00 USD | 18,670,000.00 USD | 1,040.00 USD | 0.00 USD | 614.32 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.63` | 17,600,000.00 USD | 17,600,000.00 USD | 213,490.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.63` | 493.16 USD | 311,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.64` | 19,080,000.00 USD | 19,080,000.00 USD | 334,190.00 USD | 11,270.00 USD | 63,790.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.64` | 18,120,000.00 USD | 18,120,000.00 USD | 501,930.00 USD | 18,170.00 USD | 1,670.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.65` | 20,150,000.00 USD | 20,150,000.00 USD | 423,550.00 USD | 52,020.00 USD | 600,100.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.65` | 18,540,000.00 USD | 18,540,000.00 USD | 420,940.00 USD | 0.00 USD | 2,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.66` | 21,130,000.00 USD | 21,130,000.00 USD | 281,290.00 USD | 316,500.00 USD | 379,880.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.66` | 18,860,000.00 USD | 18,860,000.00 USD | 144,860.00 USD | 18,370.00 USD | 150,940.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.67` | 124,390.00 USD | 435,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.67` | 21,690,000.00 USD | 21,690,000.00 USD | 184,440.00 USD | 0.00 USD | 378,090.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.67` | 18,900,000.00 USD | 18,900,000.00 USD | 0.00 USD | 0.00 USD | 43,230.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.68` | 22,300,000.00 USD | 22,300,000.00 USD | 345,840.00 USD | 81,340.00 USD | 175,700.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.68` | 19,820,000.00 USD | 19,820,000.00 USD | 381,910.00 USD | 83,630.00 USD | 450,700.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.69` | 22,800,000.00 USD | 22,800,000.00 USD | 213,780.00 USD | 40,000.00 USD | 254,150.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.69` | 19,910,000.00 USD | 19,910,000.00 USD | 2,450.00 USD | 0.00 USD | 88,340.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.70` | 23,140,000.00 USD | 23,140,000.00 USD | 74,090.00 USD | 123,520.00 USD | 143,310.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.70` | 20,220,000.00 USD | 20,220,000.00 USD | 74,240.00 USD | 60,360.00 USD | 181,210.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.71` | 13,050.00 USD | 448,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.71` | 24,100,000.00 USD | 24,100,000.00 USD | 359,510.00 USD | 284,360.00 USD | 316,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.71` | 20,630,000.00 USD | 20,630,000.00 USD | 178,360.00 USD | 232,800.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.71` | 460.18 USD | 449,200.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `4.72` | 20,820,000.00 USD | 20,820,000.00 USD | 7,140.00 USD | 0.00 USD | 180,490.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.73` | 20,880,000.00 USD | 20,880,000.00 USD | 59,970.00 USD | 0.00 USD | 894.74 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.74` | 21,200,000.00 USD | 21,200,000.00 USD | 14,750.00 USD | 173,100.00 USD | 127,910.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.75` | 21,740,000.00 USD | 21,740,000.00 USD | 17,340.00 USD | 185,060.00 USD | 343,810.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.75` | 154,870.00 USD | 604,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `4.76` | 23,090,000.00 USD | 23,090,000.00 USD | 1,030,000.00 USD | 46,890.00 USD | 272,560.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.76` | 64,260.00 USD | 668,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `4.77` | 24,000,000.00 USD | 24,000,000.00 USD | 731,680.00 USD | 73,410.00 USD | 101,640.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.78` | 7,050.00 USD | 675,380.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `4.78` | 25,350,000.00 USD | 25,350,000.00 USD | 683,730.00 USD | 513,870.00 USD | 154,510.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.79` | 4,530.00 USD | 679,910.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `4.79` | 26,380,000.00 USD | 26,380,000.00 USD | 713,060.00 USD | 249,310.00 USD | 72,120.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.79` | 1,330.00 USD | 681,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `4.80` | 27,970,000.00 USD | 27,970,000.00 USD | 1,160,000.00 USD | 432,340.00 USD | 2,480.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.81` | 28,600,000.00 USD | 28,600,000.00 USD | 400,070.00 USD | 125,900.00 USD | 101,780.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.82` | 473,730.00 USD | 1,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `4.82` | 31,370,000.00 USD | 31,370,000.00 USD | 1,010,000.00 USD | 369,430.00 USD | 1,390,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.83` | 1,740.00 USD | 1,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `4.83` | 33,020,000.00 USD | 33,020,000.00 USD | 822,860.00 USD | 85,680.00 USD | 739,630.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.83` | 23,580.00 USD | 1,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `4.84` | 33,510,000.00 USD | 33,510,000.00 USD | 97,300.00 USD | 71,790.00 USD | 322,840.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.84` | 41,300.00 USD | 1,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `4.85` | 35,530,000.00 USD | 35,530,000.00 USD | 487,940.00 USD | 366,970.00 USD | 1,160,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.86` | 36,940,000.00 USD | 36,940,000.00 USD | 444,810.00 USD | 162,380.00 USD | 802,380.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.87` | 5,460.00 USD | 1,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `4.87` | 38,000,000.00 USD | 38,000,000.00 USD | 264,730.00 USD | 136,820.00 USD | 663,430.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.88` | 12,510.00 USD | 1,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `4.88` | 39,590,000.00 USD | 39,590,000.00 USD | 449,970.00 USD | 340,260.00 USD | 792,630.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.88` | 827.03 USD | 1,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `4.89` | 40,170,000.00 USD | 40,170,000.00 USD | 213,960.00 USD | 100,850.00 USD | 272,060.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.90` | 41,310,000.00 USD | 41,310,000.00 USD | 450,550.00 USD | 145,910.00 USD | 541,330.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.91` | 42,750,000.00 USD | 42,750,000.00 USD | 637,320.00 USD | 208,910.00 USD | 590,510.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.92` | 346,720.00 USD | 1,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `4.92` | 44,480,000.00 USD | 44,480,000.00 USD | 576,460.00 USD | 277,640.00 USD | 877,920.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.92` | 2,100.00 USD | 1,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `4.93` | 46,040,000.00 USD | 46,040,000.00 USD | 730,010.00 USD | 78,190.00 USD | 749,940.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.93` | 556.67 USD | 1,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `4.94` | 47,380,000.00 USD | 47,380,000.00 USD | 351,940.00 USD | 290,290.00 USD | 696,960.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.95` | 48,680,000.00 USD | 48,680,000.00 USD | 468,360.00 USD | 161,040.00 USD | 670,270.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.96` | 342.89 USD | 1,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `4.96` | 49,910,000.00 USD | 49,910,000.00 USD | 607,770.00 USD | 214,910.00 USD | 410,880.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.97` | 50,290,000.00 USD | 50,290,000.00 USD | 198,220.00 USD | 72,330.00 USD | 113,320.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.97` | 99,810.00 USD | 1,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `4.98` | 50,950,000.00 USD | 50,950,000.00 USD | 251,840.00 USD | 102,410.00 USD | 299,870.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.99` | 5,090.00 USD | 1,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `4.99` | 51,300,000.00 USD | 51,300,000.00 USD | 133,330.00 USD | 103,060.00 USD | 117,980.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `5.00` | 20,430.00 USD | 1,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `5.00` | 52,000,000.00 USD | 52,000,000.00 USD | 210,680.00 USD | 36,180.00 USD | 454,070.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `5.01` | 53,830,000.00 USD | 53,830,000.00 USD | 781,840.00 USD | 255,770.00 USD | 786,470.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `5.02` | 55,280,000.00 USD | 55,280,000.00 USD | 821,860.00 USD | 309,020.00 USD | 321,920.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `5.03` | 56,410,000.00 USD | 56,410,000.00 USD | 385,330.00 USD | 172,880.00 USD | 567,890.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `5.04` | 926.94 USD | 1,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `5.04` | 57,490,000.00 USD | 57,490,000.00 USD | 305,260.00 USD | 163,190.00 USD | 619,980.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `5.05` | 58,940,000.00 USD | 58,940,000.00 USD | 694,310.00 USD | 267,140.00 USD | 486,680.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `5.05` | 5,020.00 USD | 1,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `5.06` | 59,620,000.00 USD | 59,620,000.00 USD | 92,480.00 USD | 165,230.00 USD | 420,210.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `5.07` | 3,420.00 USD | 1,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `5.07` | 60,660,000.00 USD | 60,660,000.00 USD | 358,750.00 USD | 137,080.00 USD | 542,550.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `5.08` | 61,180,000.00 USD | 61,180,000.00 USD | 204,140.00 USD | 167,810.00 USD | 150,010.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `5.08` | 1,090.00 USD | 1,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `5.09` | 61,720,000.00 USD | 61,720,000.00 USD | 105,390.00 USD | 52,790.00 USD | 385,540.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `5.10` | 62,110,000.00 USD | 62,110,000.00 USD | 182,200.00 USD | 0.00 USD | 201,110.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `5.11` | 62,700,000.00 USD | 62,700,000.00 USD | 369,260.00 USD | 78,100.00 USD | 140,600.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `5.12` | 1,640.00 USD | 1,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `5.12` | 63,270,000.00 USD | 63,270,000.00 USD | 303,840.00 USD | 152,530.00 USD | 115,650.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `5.12` | 2,560.00 USD | 1,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `5.13` | 63,840,000.00 USD | 63,840,000.00 USD | 173,190.00 USD | 71,310.00 USD | 325,090.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `5.13` | 1,080.00 USD | 1,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `5.14` | 64,280,000.00 USD | 64,280,000.00 USD | 140,950.00 USD | 59,640.00 USD | 239,260.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `5.15` | 64,830,000.00 USD | 64,830,000.00 USD | 205,680.00 USD | 82,350.00 USD | 267,910.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `5.16` | 65,350,000.00 USD | 65,350,000.00 USD | 51,850.00 USD | 112,830.00 USD | 347,470.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `5.17` | 2,900.00 USD | 1,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `5.17` | 65,960,000.00 USD | 65,960,000.00 USD | 280,710.00 USD | 85,040.00 USD | 244,330.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `5.18` | 66,210,000.00 USD | 66,210,000.00 USD | 67,600.00 USD | 63,250.00 USD | 124,260.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `5.19` | 66,430,000.00 USD | 66,430,000.00 USD | 69,310.00 USD | 13,680.00 USD | 138,850.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `5.20` | 1,040.00 USD | 1,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `5.20` | 66,680,000.00 USD | 66,680,000.00 USD | 137,830.00 USD | 45,820.00 USD | 65,990.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `5.21` | 898,120.00 USD | 2,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `5.21` | 66,920,000.00 USD | 66,920,000.00 USD | 105,330.00 USD | 20,850.00 USD | 110,400.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `5.21` | 1,040,000.00 USD | 3,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `5.22` | 66,980,000.00 USD | 66,980,000.00 USD | 48,760.00 USD | 13,410.00 USD | 398.26 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `5.22` | 72,110.00 USD | 3,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `5.23` | 67,040,000.00 USD | 67,040,000.00 USD | 5,060.00 USD | 15,520.00 USD | 34,400.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `5.25` | 1,110.00 USD | 3,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.25` | 288.50 USD | 3,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.26` | 5,610.00 USD | 3,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.28` | 853.50 USD | 3,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.29` | 257.38 USD | 3,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.29` | 114.37 USD | 3,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.30` | 524.66 USD | 3,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.32` | 718.59 USD | 3,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.33` | 1,600.00 USD | 3,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.34` | 90,820.00 USD | 3,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.36` | 23,600.00 USD | 3,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.39` | 20,300.00 USD | 3,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.41` | 35,680.00 USD | 3,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.43` | 962.54 USD | 3,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.45` | 1,050.00 USD | 3,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.46` | 291,860.00 USD | 4,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.47` | 88,100.00 USD | 4,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.49` | 62,250.00 USD | 4,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.50` | 77,760.00 USD | 4,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.51` | 40,180.00 USD | 4,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.54` | 209.22 USD | 4,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.54` | 715.30 USD | 4,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.57` | 8,670.00 USD | 4,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.58` | 62,420.00 USD | 4,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.58` | 62,420.00 USD | 4,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.59` | 686.51 USD | 4,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.62` | 56,250.00 USD | 4,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.67` | 211.30 USD | 4,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.67` | 334.26 USD | 4,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.68` | 26,090.00 USD | 4,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.70` | 1,520.00 USD | 4,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.71` | 2,130.00 USD | 4,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.75` | 4,580.00 USD | 4,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.75` | 40,990.00 USD | 4,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.79` | 127.49 USD | 4,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.80` | 2,670.00 USD | 4,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.84` | 56,160.00 USD | 4,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.86` | 848.39 USD | 4,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.88` | 190.67 USD | 4,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.89` | 88,590.00 USD | 4,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.92` | 7,330.00 USD | 4,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.95` | 1,400.00 USD | 4,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.03` | 23,060.00 USD | 4,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.07` | 281,130.00 USD | 5,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.08` | 5,920.00 USD | 5,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.09` | 37,510.00 USD | 5,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.11` | 2,720.00 USD | 5,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.12` | 1,260.00 USD | 5,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.13` | 24,160.00 USD | 5,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.24` | 693.33 USD | 5,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.25` | 7,300.00 USD | 5,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.25` | 2,380.00 USD | 5,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.28` | 397.84 USD | 5,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.32` | 310.70 USD | 5,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.33` | 382.00 USD | 5,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.34` | 214.46 USD | 5,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.37` | 45,180.00 USD | 5,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.38` | 288.15 USD | 5,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.38` | 2,000.00 USD | 5,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.41` | 3,780.00 USD | 5,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.42` | 8,700.00 USD | 5,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.42` | 346.95 USD | 5,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.43` | 42,740.00 USD | 5,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.45` | 378,690.00 USD | 5,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.46` | 7,150.00 USD | 5,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.46` | 1,940.00 USD | 5,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.51` | 380.48 USD | 5,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.54` | 18,080.00 USD | 5,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.54` | 265.07 USD | 5,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.55` | 51,310.00 USD | 5,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.57` | 454.95 USD | 5,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.58` | 103,110.00 USD | 5,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.59` | 418.78 USD | 5,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.64` | 6,080.00 USD | 5,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.66` | 7,230.00 USD | 5,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.67` | 1,980,000.00 USD | 7,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.67` | 200.25 USD | 7,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.72` | 115,670.00 USD | 8,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.75` | 3,380.00 USD | 8,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.76` | 1,240,000.00 USD | 9,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.79` | 36,120.00 USD | 9,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.84` | 753.63 USD | 9,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.86` | 649.17 USD | 9,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.87` | 46,020.00 USD | 9,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.88` | 164.55 USD | 9,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.92` | 7,660.00 USD | 9,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.96` | 191.26 USD | 9,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.99` | 664.27 USD | 9,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.07` | 192.87 USD | 9,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.09` | 699.57 USD | 9,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.12` | 9,850.00 USD | 9,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.16` | 1,790.00 USD | 9,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.20` | 5,720.00 USD | 9,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.21` | 13,560.00 USD | 9,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.24` | 68,550.00 USD | 9,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.28` | 576.91 USD | 9,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.33` | 1,320.00 USD | 9,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.38` | 1,630.00 USD | 9,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.41` | 88,860.00 USD | 9,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.46` | 107,860.00 USD | 9,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.49` | 1,160.00 USD | 9,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.50` | 7,790,000.00 USD | 17,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.50` | 16,790.00 USD | 17,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.53` | 4,220.00 USD | 17,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.55` | 10,090,000.00 USD | 27,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.58` | 794.91 USD | 27,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.63` | 19,210.00 USD | 27,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.66` | 26,770.00 USD | 27,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.67` | 576,600.00 USD | 28,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.67` | 1,440,000.00 USD | 29,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.68` | 160.62 USD | 29,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.72` | 495.94 USD | 29,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.75` | 629.67 USD | 29,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.76` | 38,700.00 USD | 29,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.80` | 2,840.00 USD | 29,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.87` | 334,500.00 USD | 30,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.88` | 28,790.00 USD | 30,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.92` | 13,850.00 USD | 30,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.92` | 1,800.00 USD | 30,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.95` | 6,120.00 USD | 30,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.96` | 134,240.00 USD | 30,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.99` | 399.25 USD | 30,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.03` | 435,420.00 USD | 30,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.06` | 797.63 USD | 30,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.12` | 2,690.00 USD | 30,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.15` | 190.01 USD | 30,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.21` | 248,640.00 USD | 30,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `0.8050` | 19,210,000.00 USD | 0.00 USD | 73,060.00 USD | `-79.83%` | `90,751.80` |
| `Live` | `Long` | `0.8450` | 19,140,000.00 USD | 0.00 USD | 2,030.00 USD | `-78.83%` | `2,406.30` |
| `Live` | `Long` | `0.8550` | 19,140,000.00 USD | 0.00 USD | 3,680.00 USD | `-78.58%` | `4,298.30` |
| `Live` | `Long` | `0.8650` | 19,130,000.00 USD | 0.00 USD | 433.80 USD | `-78.33%` | `501.50` |
| `Live` | `Long` | `0.8750` | 19,130,000.00 USD | 0.00 USD | 8,310.00 USD | `-78.08%` | `9,498.00` |
| `Live` | `Long` | `0.8950` | 19,120,000.00 USD | 0.00 USD | 39,460.00 USD | `-77.58%` | `44,089.80` |
| `Live` | `Long` | `0.9050` | 19,090,000.00 USD | 0.00 USD | 292.22 USD | `-77.33%` | `322.90` |
| `Live` | `Long` | `0.9150` | 19,090,000.00 USD | 0.00 USD | 11,790.00 USD | `-77.08%` | `12,890.20` |
| `Live` | `Long` | `0.9450` | 19,070,000.00 USD | 0.00 USD | 9,450.00 USD | `-76.33%` | `10,000.00` |
| `Live` | `Long` | `0.9550` | 19,060,000.00 USD | 0.00 USD | 528.88 USD | `-76.08%` | `553.80` |
| `Live` | `Long` | `0.9650` | 19,060,000.00 USD | 0.00 USD | 965.00 USD | `-75.83%` | `1,000.00` |
| `Live` | `Long` | `0.9750` | 19,060,000.00 USD | 0.00 USD | 123.53 USD | `-75.57%` | `126.70` |
| `Live` | `Long` | `0.9850` | 19,060,000.00 USD | 0.00 USD | 707.53 USD | `-75.32%` | `718.30` |
| `Live` | `Long` | `0.9950` | 19,060,000.00 USD | 0.00 USD | 154,200.00 USD | `-75.07%` | `154,969.90` |
| `Live` | `Long` | `1.01` | 18,910,000.00 USD | 0.00 USD | 1,340.00 USD | `-74.57%` | `1,321.80` |
| `Live` | `Long` | `1.02` | 18,910,000.00 USD | 0.00 USD | 10,250.00 USD | `-74.32%` | `10,000.00` |
| `Live` | `Long` | `1.03` | 18,900,000.00 USD | 0.00 USD | 36,980.00 USD | `-74.07%` | `35,734.20` |
| `Live` | `Long` | `1.04` | 18,860,000.00 USD | 0.00 USD | 2,740.00 USD | `-73.82%` | `2,617.40` |
| `Live` | `Long` | `1.05` | 18,860,000.00 USD | 0.00 USD | 4,480.00 USD | `-73.57%` | `4,250.40` |
| `Live` | `Long` | `1.06` | 18,850,000.00 USD | 0.00 USD | 892.90 USD | `-73.32%` | `838.40` |
| `Live` | `Long` | `1.07` | 18,850,000.00 USD | 0.00 USD | 7,840.00 USD | `-73.07%` | `7,289.70` |
| `Live` | `Long` | `1.08` | 18,840,000.00 USD | 0.00 USD | 205,550.00 USD | `-72.82%` | `189,446.00` |
| `Live` | `Long` | `1.09` | 18,640,000.00 USD | 0.00 USD | 4,030.00 USD | `-72.57%` | `3,676.40` |
| `Live` | `Long` | `1.11` | 18,630,000.00 USD | 0.00 USD | 557.50 USD | `-72.07%` | `500.00` |
| `Live` | `Long` | `1.12` | 18,630,000.00 USD | 0.00 USD | 1,580.00 USD | `-71.82%` | `1,408.40` |
| `Live` | `Long` | `1.14` | 18,630,000.00 USD | 0.00 USD | 4,960.00 USD | `-71.57%` | `4,368.60` |
| `Live` | `Long` | `1.15` | 18,630,000.00 USD | 0.00 USD | 26,620.00 USD | `-71.32%` | `23,252.70` |
| `Live` | `Long` | `1.17` | 18,600,000.00 USD | 0.00 USD | 1,110.00 USD | `-70.82%` | `954.80` |
| `Live` | `Long` | `1.18` | 18,600,000.00 USD | 0.00 USD | 19,930.00 USD | `-70.56%` | `16,965.20` |
| `Live` | `Long` | `1.19` | 18,580,000.00 USD | 0.00 USD | 2,140.00 USD | `-70.31%` | `1,804.70` |
| `Live` | `Long` | `1.22` | 18,580,000.00 USD | 0.00 USD | 396.09 USD | `-69.56%` | `326.00` |
| `Live` | `Long` | `1.25` | 18,580,000.00 USD | 0.00 USD | 1,220.00 USD | `-68.56%` | `969.60` |
| `Live` | `Long` | `1.26` | 18,570,000.00 USD | 0.00 USD | 5,250.00 USD | `-68.31%` | `4,150.30` |
| `Live` | `Long` | `1.27` | 18,570,000.00 USD | 0.00 USD | 2,390.00 USD | `-68.06%` | `1,876.80` |
| `Live` | `Long` | `1.28` | 18,570,000.00 USD | 0.00 USD | 169.23 USD | `-67.81%` | `131.70` |
| `Live` | `Long` | `1.30` | 18,570,000.00 USD | 0.00 USD | 328.21 USD | `-67.31%` | `251.50` |
| `Live` | `Long` | `1.31` | 18,570,000.00 USD | 0.00 USD | 146.10 USD | `-67.06%` | `111.10` |
| `Live` | `Long` | `1.32` | 18,570,000.00 USD | 0.00 USD | 4,150.00 USD | `-66.81%` | `3,132.40` |
| `Live` | `Long` | `1.34` | 18,560,000.00 USD | 0.00 USD | 73,410.00 USD | `-66.31%` | `54,579.20` |
| `Live` | `Long` | `1.35` | 18,490,000.00 USD | 0.00 USD | 3,230.00 USD | `-66.06%` | `2,387.20` |
| `Live` | `Long` | `1.36` | 18,490,000.00 USD | 0.00 USD | 6,220.00 USD | `-65.80%` | `4,558.80` |
| `Live` | `Long` | `1.38` | 18,480,000.00 USD | 0.00 USD | 12,380.00 USD | `-65.55%` | `9,000.00` |
| `Live` | `Long` | `1.39` | 18,470,000.00 USD | 0.00 USD | 13,340.00 USD | `-65.30%` | `9,632.80` |
| `Live` | `Long` | `1.40` | 18,450,000.00 USD | 0.00 USD | 42,490.00 USD | `-65.05%` | `30,458.70` |
| `Live` | `Long` | `1.41` | 18,410,000.00 USD | 0.00 USD | 28,140.00 USD | `-64.80%` | `20,027.00` |
| `Live` | `Long` | `1.42` | 18,380,000.00 USD | 0.00 USD | 9,190.00 USD | `-64.55%` | `6,495.30` |
| `Live` | `Long` | `1.43` | 18,370,000.00 USD | 0.00 USD | 855.00 USD | `-64.30%` | `600.00` |
| `Live` | `Long` | `1.45` | 18,370,000.00 USD | 0.00 USD | 1,040.00 USD | `-63.80%` | `717.50` |
| `Live` | `Long` | `1.48` | 18,370,000.00 USD | 0.00 USD | 14,750.00 USD | `-63.05%` | `10,000.00` |
| `Live` | `Long` | `1.50` | 18,360,000.00 USD | 0.00 USD | 441.57 USD | `-62.30%` | `293.40` |
| `Live` | `Long` | `1.51` | 18,360,000.00 USD | 0.00 USD | 454.50 USD | `-62.05%` | `300.00` |
| `Live` | `Long` | `1.52` | 18,360,000.00 USD | 0.00 USD | 1,820.00 USD | `-61.80%` | `1,194.90` |
| `Live` | `Long` | `1.53` | 18,350,000.00 USD | 0.00 USD | 3,500.00 USD | `-61.55%` | `2,278.20` |
| `Live` | `Long` | `1.54` | 18,350,000.00 USD | 0.00 USD | 77,250.00 USD | `-61.30%` | `50,000.00` |
| `Live` | `Long` | `1.55` | 18,270,000.00 USD | 0.00 USD | 311.00 USD | `-61.05%` | `200.00` |
| `Live` | `Long` | `1.56` | 18,270,000.00 USD | 0.00 USD | 20,570.00 USD | `-60.79%` | `13,146.30` |
| `Live` | `Long` | `1.57` | 18,250,000.00 USD | 0.00 USD | 825.46 USD | `-60.54%` | `524.10` |
| `Live` | `Long` | `1.59` | 18,250,000.00 USD | 0.00 USD | 3,700.00 USD | `-60.04%` | `2,321.20` |
| `Live` | `Long` | `1.60` | 18,250,000.00 USD | 0.00 USD | 2,260.00 USD | `-59.79%` | `1,405.50` |
| `Live` | `Long` | `1.62` | 18,250,000.00 USD | 0.00 USD | 6,010.00 USD | `-59.29%` | `3,696.80` |
| `Live` | `Long` | `1.64` | 18,240,000.00 USD | 0.00 USD | 2,030.00 USD | `-59.04%` | `1,241.00` |
| `Live` | `Long` | `1.65` | 18,240,000.00 USD | 0.00 USD | 2,350.00 USD | `-58.79%` | `1,429.80` |
| `Live` | `Long` | `1.66` | 18,240,000.00 USD | 0.00 USD | 384.13 USD | `-58.54%` | `232.10` |
| `Live` | `Long` | `1.67` | 18,240,000.00 USD | 0.00 USD | 2,660.00 USD | `-58.29%` | `1,600.00` |
| `Live` | `Long` | `1.68` | 18,230,000.00 USD | 0.00 USD | 108.71 USD | `-58.04%` | `64.90` |
| `Live` | `Long` | `1.69` | 18,230,000.00 USD | 0.00 USD | 12,850.00 USD | `-57.79%` | `7,624.50` |
| `Live` | `Long` | `1.71` | 18,220,000.00 USD | 0.00 USD | 156,200.00 USD | `-57.29%` | `91,613.70` |
| `Live` | `Long` | `1.73` | 18,060,000.00 USD | 0.00 USD | 5,460.00 USD | `-56.79%` | `3,164.50` |
| `Live` | `Long` | `1.75` | 18,060,000.00 USD | 0.00 USD | 920.49 USD | `-56.29%` | `527.50` |
| `Live` | `Long` | `1.75` | 18,060,000.00 USD | 0.00 USD | 10,860.00 USD | `-56.03%` | `6,186.10` |
| `Live` | `Long` | `1.77` | 18,050,000.00 USD | 0.00 USD | 4,100.00 USD | `-55.53%` | `2,312.60` |
| `Live` | `Long` | `1.78` | 18,040,000.00 USD | 0.00 USD | 5,270.00 USD | `-55.28%` | `2,953.60` |
| `Live` | `Long` | `1.79` | 18,040,000.00 USD | 0.00 USD | 2,900.00 USD | `-55.03%` | `1,614.30` |
| `Live` | `Long` | `1.80` | 18,030,000.00 USD | 0.00 USD | 2,370.00 USD | `-54.78%` | `1,314.50` |
| `Live` | `Long` | `1.81` | 18,030,000.00 USD | 0.00 USD | 28,810.00 USD | `-54.53%` | `15,873.20` |
| `Live` | `Long` | `1.82` | 18,000,000.00 USD | 0.00 USD | 7,370.00 USD | `-54.28%` | `4,038.00` |
| `Live` | `Long` | `1.83` | 18,000,000.00 USD | 0.00 USD | 41,990.00 USD | `-54.03%` | `22,885.10` |
| `Live` | `Long` | `1.84` | 17,950,000.00 USD | 0.00 USD | 645,750.00 USD | `-53.78%` | `350,000.00` |
| `Live` | `Long` | `1.85` | 17,310,000.00 USD | 0.00 USD | 557,490.00 USD | `-53.53%` | `300,531.20` |
| `Live` | `Long` | `1.86` | 16,750,000.00 USD | 0.00 USD | 184.82 USD | `-53.28%` | `99.10` |
| `Live` | `Long` | `1.88` | 16,750,000.00 USD | 0.00 USD | 393.56 USD | `-53.03%` | `209.90` |
| `Live` | `Long` | `1.89` | 16,750,000.00 USD | 0.00 USD | 1,540.00 USD | `-52.78%` | `816.00` |
| `Live` | `Long` | `1.90` | 16,750,000.00 USD | 0.00 USD | 2,080.00 USD | `-52.53%` | `1,100.00` |
| `Live` | `Long` | `1.91` | 16,750,000.00 USD | 0.00 USD | 3,950.00 USD | `-52.28%` | `2,071.50` |
| `Live` | `Long` | `1.92` | 16,740,000.00 USD | 0.00 USD | 49,920.00 USD | `-52.03%` | `26,068.80` |
| `Live` | `Long` | `1.93` | 16,690,000.00 USD | 0.00 USD | 154.77 USD | `-51.78%` | `80.40` |
| `Live` | `Long` | `1.94` | 16,690,000.00 USD | 0.00 USD | 7,300.00 USD | `-51.53%` | `3,773.50` |
| `Live` | `Long` | `1.95` | 16,680,000.00 USD | 0.00 USD | 2,740.00 USD | `-51.28%` | `1,410.10` |
| `Live` | `Long` | `1.96` | 16,680,000.00 USD | 0.00 USD | 15,710.00 USD | `-51.02%` | `8,033.90` |
| `Live` | `Long` | `1.97` | 16,670,000.00 USD | 0.00 USD | 6,350.00 USD | `-50.77%` | `3,233.10` |
| `Live` | `Long` | `1.98` | 16,660,000.00 USD | 0.00 USD | 356,140.00 USD | `-50.52%` | `180,322.80` |
| `Live` | `Long` | `1.99` | 16,300,000.00 USD | 0.00 USD | 53,060.00 USD | `-50.27%` | `26,729.20` |
| `Live` | `Long` | `2.00` | 16,250,000.00 USD | 0.00 USD | 20,240.00 USD | `-49.77%` | `10,096.20` |
| `Live` | `Long` | `2.02` | 16,230,000.00 USD | 0.00 USD | 141,710.00 USD | `-49.52%` | `70,325.90` |
| `Live` | `Long` | `2.02` | 16,090,000.00 USD | 0.00 USD | 260.62 USD | `-49.27%` | `128.70` |
| `Live` | `Long` | `2.04` | 16,090,000.00 USD | 0.00 USD | 102,580.00 USD | `-49.02%` | `50,407.00` |
| `Live` | `Long` | `2.04` | 15,990,000.00 USD | 0.00 USD | 4,480.00 USD | `-48.77%` | `2,192.50` |
| `Live` | `Long` | `2.06` | 15,980,000.00 USD | 0.00 USD | 11,890.00 USD | `-48.52%` | `5,783.80` |
| `Live` | `Long` | `2.06` | 15,970,000.00 USD | 0.00 USD | 7,180.00 USD | `-48.27%` | `3,475.90` |
| `Live` | `Long` | `2.08` | 15,960,000.00 USD | 0.00 USD | 6,690.00 USD | `-48.02%` | `3,225.70` |
| `Live` | `Long` | `2.08` | 15,960,000.00 USD | 0.00 USD | 18,600.00 USD | `-47.77%` | `8,920.10` |
| `Live` | `Long` | `2.10` | 15,940,000.00 USD | 0.00 USD | 1,310.00 USD | `-47.52%` | `627.40` |
| `Live` | `Long` | `2.10` | 15,940,000.00 USD | 0.00 USD | 7,880.00 USD | `-47.27%` | `3,742.10` |
| `Live` | `Long` | `2.12` | 15,930,000.00 USD | 0.00 USD | 12,630.00 USD | `-47.02%` | `5,972.40` |
| `Live` | `Long` | `2.12` | 15,920,000.00 USD | 0.00 USD | 32,770.00 USD | `-46.77%` | `15,421.70` |
| `Live` | `Long` | `2.13` | 15,880,000.00 USD | 0.00 USD | 1,180.00 USD | `-46.52%` | `552.20` |
| `Live` | `Long` | `2.15` | 15,880,000.00 USD | 0.00 USD | 110.04 USD | `-46.26%` | `51.30` |
| `Live` | `Long` | `2.15` | 15,880,000.00 USD | 0.00 USD | 2,150.00 USD | `-46.01%` | `995.70` |
| `Live` | `Long` | `2.17` | 15,880,000.00 USD | 0.00 USD | 1,100.00 USD | `-45.76%` | `510.10` |
| `Live` | `Long` | `2.17` | 15,880,000.00 USD | 0.00 USD | 2,560.00 USD | `-45.51%` | `1,176.90` |
| `Live` | `Long` | `2.19` | 15,880,000.00 USD | 0.00 USD | 104,270.00 USD | `-45.26%` | `47,719.40` |
| `Live` | `Long` | `2.19` | 15,770,000.00 USD | 0.00 USD | 10,250.00 USD | `-45.01%` | `4,669.40` |
| `Live` | `Long` | `2.21` | 15,760,000.00 USD | 0.00 USD | 33,940.00 USD | `-44.76%` | `15,393.50` |
| `Live` | `Long` | `2.21` | 15,730,000.00 USD | 0.00 USD | 2,010.00 USD | `-44.51%` | `909.30` |
| `Live` | `Long` | `2.23` | 15,720,000.00 USD | 0.00 USD | 3,110.00 USD | `-44.01%` | `1,392.70` |
| `Live` | `Long` | `2.25` | 15,720,000.00 USD | 0.00 USD | 57,210.00 USD | `-43.76%` | `25,484.10` |
| `Live` | `Long` | `2.25` | 15,660,000.00 USD | 0.00 USD | 115,820.00 USD | `-43.51%` | `51,360.80` |
| `Live` | `Long` | `2.27` | 15,550,000.00 USD | 0.00 USD | 379,750.00 USD | `-43.01%` | `166,923.00` |
| `Live` | `Long` | `2.29` | 15,170,000.00 USD | 0.00 USD | 1,330.00 USD | `-42.76%` | `582.40` |
| `Live` | `Long` | `2.29` | 15,170,000.00 USD | 0.00 USD | 3,570.00 USD | `-42.51%` | `1,556.60` |
| `Live` | `Long` | `2.31` | 15,160,000.00 USD | 0.00 USD | 1,980.00 USD | `-42.26%` | `859.80` |
| `Live` | `Long` | `2.31` | 15,160,000.00 USD | 0.00 USD | 2,140.00 USD | `-42.01%` | `926.40` |
| `Live` | `Long` | `2.33` | 15,160,000.00 USD | 0.00 USD | 6,180.00 USD | `-41.51%` | `2,647.20` |
| `Live` | `Long` | `2.35` | 15,150,000.00 USD | 0.00 USD | 43,490.00 USD | `-41.25%` | `18,544.20` |
| `Live` | `Long` | `2.35` | 15,110,000.00 USD | 0.00 USD | 8,310.00 USD | `-41.00%` | `3,527.30` |
| `Live` | `Long` | `2.37` | 15,100,000.00 USD | 0.00 USD | 70,820.00 USD | `-40.75%` | `29,945.10` |
| `Live` | `Long` | `2.38` | 15,030,000.00 USD | 0.00 USD | 431,710.00 USD | `-40.50%` | `181,774.20` |
| `Live` | `Long` | `2.38` | 14,600,000.00 USD | 0.00 USD | 38,280.00 USD | `-40.25%` | `16,050.50` |
| `Live` | `Long` | `2.40` | 14,560,000.00 USD | 0.00 USD | 465,510.00 USD | `-40.00%` | `194,366.70` |
| `Live` | `Long` | `2.40` | 14,100,000.00 USD | 0.00 USD | 36,690.00 USD | `-39.75%` | `15,257.40` |
| `Live` | `Long` | `2.42` | 14,060,000.00 USD | 0.00 USD | 286,450.00 USD | `-39.50%` | `118,614.70` |
| `Live` | `Long` | `2.42` | 13,770,000.00 USD | 0.00 USD | 273,060.00 USD | `-39.25%` | `112,601.40` |
| `Live` | `Long` | `2.44` | 13,500,000.00 USD | 0.00 USD | 1,600,000.00 USD | `-39.00%` | `658,368.10` |
| `Live` | `Long` | `2.44` | 11,900,000.00 USD | 0.00 USD | 3,700.00 USD | `-38.75%` | `1,515.10` |
| `Live` | `Long` | `2.46` | 11,890,000.00 USD | 0.00 USD | 1,360.00 USD | `-38.50%` | `554.40` |
| `Live` | `Long` | `2.46` | 11,890,000.00 USD | 0.00 USD | 6,130.00 USD | `-38.25%` | `2,486.70` |
| `Live` | `Long` | `2.48` | 11,890,000.00 USD | 0.00 USD | 336.35 USD | `-38.00%` | `135.90` |
| `Live` | `Long` | `2.48` | 11,880,000.00 USD | 0.00 USD | 10,220.00 USD | `-37.75%` | `4,112.50` |
| `Live` | `Long` | `2.50` | 11,870,000.00 USD | 0.00 USD | 2,130.00 USD | `-37.50%` | `852.70` |
| `Live` | `Long` | `2.50` | 11,870,000.00 USD | 0.00 USD | 33,560.00 USD | `-37.25%` | `13,395.50` |
| `Live` | `Long` | `2.52` | 11,840,000.00 USD | 0.00 USD | 17,890.00 USD | `-36.75%` | `7,085.70` |
| `Live` | `Long` | `2.54` | 11,820,000.00 USD | 0.00 USD | 7,250.00 USD | `-36.49%` | `2,859.50` |
| `Live` | `Long` | `2.54` | 11,810,000.00 USD | 0.00 USD | 11,140.00 USD | `-36.24%` | `4,376.90` |
| `Live` | `Long` | `2.56` | 11,800,000.00 USD | 0.00 USD | 5,420.00 USD | `-35.99%` | `2,122.50` |
| `Live` | `Long` | `2.56` | 11,800,000.00 USD | 0.00 USD | 11,370.00 USD | `-35.74%` | `4,433.10` |
| `Live` | `Long` | `2.58` | 11,790,000.00 USD | 0.00 USD | 2,810.00 USD | `-35.49%` | `1,090.00` |
| `Live` | `Long` | `2.58` | 11,780,000.00 USD | 0.00 USD | 905.27 USD | `-35.24%` | `350.20` |
| `Live` | `Long` | `2.60` | 11,780,000.00 USD | 0.00 USD | 116,830.00 USD | `-34.99%` | `45,022.50` |
| `Live` | `Long` | `2.60` | 11,670,000.00 USD | 0.00 USD | 666.10 USD | `-34.74%` | `255.70` |
| `Live` | `Long` | `2.62` | 11,660,000.00 USD | 0.00 USD | 17,220.00 USD | `-34.49%` | `6,586.50` |
| `Live` | `Long` | `2.62` | 11,650,000.00 USD | 0.00 USD | 3,780.00 USD | `-34.24%` | `1,438.50` |
| `Live` | `Long` | `2.63` | 11,640,000.00 USD | 0.00 USD | 25,270.00 USD | `-33.99%` | `9,591.20` |
| `Live` | `Long` | `2.65` | 11,620,000.00 USD | 0.00 USD | 2,650.00 USD | `-33.74%` | `1,000.00` |
| `Live` | `Long` | `2.65` | 11,620,000.00 USD | 0.00 USD | 18,510.00 USD | `-33.49%` | `6,972.60` |
| `Live` | `Long` | `2.67` | 11,600,000.00 USD | 0.00 USD | 81,240.00 USD | `-33.24%` | `30,484.30` |
| `Live` | `Long` | `2.67` | 11,520,000.00 USD | 0.00 USD | 17,840.00 USD | `-32.99%` | `6,670.60` |
| `Live` | `Long` | `2.69` | 11,500,000.00 USD | 0.00 USD | 4,860.00 USD | `-32.74%` | `1,809.60` |
| `Live` | `Long` | `2.69` | 11,490,000.00 USD | 0.00 USD | 733.85 USD | `-32.49%` | `272.30` |
| `Live` | `Long` | `2.71` | 11,490,000.00 USD | 0.00 USD | 127,130.00 USD | `-32.24%` | `46,996.40` |
| `Live` | `Long` | `2.71` | 11,370,000.00 USD | 0.00 USD | 11,940.00 USD | `-31.99%` | `4,397.50` |
| `Live` | `Long` | `2.73` | 11,350,000.00 USD | 0.00 USD | 27,780.00 USD | `-31.74%` | `10,194.90` |
| `Live` | `Long` | `2.73` | 11,330,000.00 USD | 0.00 USD | 14,100.00 USD | `-31.48%` | `5,156.70` |
| `Live` | `Long` | `2.75` | 11,310,000.00 USD | 0.00 USD | 41,680.00 USD | `-31.23%` | `15,182.50` |
| `Live` | `Long` | `2.75` | 11,270,000.00 USD | 0.00 USD | 25,260.00 USD | `-30.98%` | `9,167.40` |
| `Live` | `Long` | `2.77` | 11,240,000.00 USD | 0.00 USD | 358,140.00 USD | `-30.73%` | `129,526.20` |
| `Live` | `Long` | `2.77` | 10,890,000.00 USD | 0.00 USD | 13,310.00 USD | `-30.48%` | `4,794.80` |
| `Live` | `Long` | `2.79` | 10,870,000.00 USD | 0.00 USD | 70,320.00 USD | `-30.23%` | `25,248.00` |
| `Live` | `Long` | `2.79` | 10,800,000.00 USD | 0.00 USD | 25,660.00 USD | `-29.98%` | `9,180.60` |
| `Live` | `Long` | `2.81` | 10,780,000.00 USD | 0.00 USD | 22,400.00 USD | `-29.73%` | `7,984.80` |
| `Live` | `Long` | `2.81` | 10,750,000.00 USD | 0.00 USD | 42,850.00 USD | `-29.48%` | `15,221.50` |
| `Live` | `Long` | `2.83` | 10,710,000.00 USD | 0.00 USD | 3,910.00 USD | `-29.23%` | `1,382.70` |
| `Live` | `Long` | `2.83` | 10,710,000.00 USD | 0.00 USD | 1,140.00 USD | `-28.98%` | `402.50` |
| `Live` | `Long` | `2.85` | 10,710,000.00 USD | 0.00 USD | 4,490.00 USD | `-28.73%` | `1,577.40` |
| `Live` | `Long` | `2.85` | 10,700,000.00 USD | 0.00 USD | 1,980.00 USD | `-28.48%` | `694.20` |
| `Live` | `Long` | `2.87` | 10,700,000.00 USD | 0.00 USD | 11,220.00 USD | `-28.23%` | `3,915.10` |
| `Live` | `Long` | `2.88` | 10,690,000.00 USD | 0.00 USD | 389,820.00 USD | `-27.98%` | `135,590.50` |
| `Live` | `Long` | `2.88` | 10,300,000.00 USD | 0.00 USD | 6,800.00 USD | `-27.73%` | `2,357.40` |
| `Live` | `Long` | `2.90` | 10,290,000.00 USD | 0.00 USD | 23,820.00 USD | `-27.48%` | `8,226.50` |
| `Live` | `Long` | `2.90` | 10,270,000.00 USD | 0.00 USD | 88,370.00 USD | `-27.23%` | `30,420.40` |
| `Live` | `Long` | `2.92` | 10,180,000.00 USD | 0.00 USD | 94,100.00 USD | `-26.98%` | `32,282.50` |
| `Live` | `Long` | `2.92` | 10,090,000.00 USD | 0.00 USD | 48,610.00 USD | `-26.72%` | `16,618.30` |
| `Live` | `Long` | `2.94` | 10,040,000.00 USD | 0.00 USD | 49,570.00 USD | `-26.47%` | `16,889.80` |
| `Live` | `Long` | `2.94` | 9,990,000.00 USD | 0.00 USD | 19,090.00 USD | `-26.22%` | `6,482.90` |
| `Live` | `Long` | `2.96` | 9,970,000.00 USD | 0.00 USD | 1,470.00 USD | `-25.97%` | `497.80` |
| `Live` | `Long` | `2.96` | 9,970,000.00 USD | 0.00 USD | 3,170.00 USD | `-25.72%` | `1,069.90` |
| `Live` | `Long` | `2.98` | 9,960,000.00 USD | 0.00 USD | 41,370.00 USD | `-25.47%` | `13,905.20` |
| `Live` | `Long` | `2.98` | 9,920,000.00 USD | 0.00 USD | 4,870.00 USD | `-25.22%` | `1,632.90` |
| `Live` | `Long` | `3.00` | 9,920,000.00 USD | 0.00 USD | 2,000.00 USD | `-24.97%` | `666.40` |
| `Live` | `Long` | `3.00` | 9,920,000.00 USD | 0.00 USD | 10,410.00 USD | `-24.72%` | `3,463.30` |
| `Live` | `Long` | `3.02` | 9,910,000.00 USD | 0.00 USD | 21,830.00 USD | `-24.47%` | `7,239.10` |
| `Live` | `Long` | `3.02` | 9,880,000.00 USD | 0.00 USD | 7,060.00 USD | `-24.22%` | `2,334.00` |
| `Live` | `Long` | `3.04` | 9,880,000.00 USD | 0.00 USD | 7,200.00 USD | `-23.97%` | `2,370.80` |
| `Live` | `Long` | `3.04` | 9,870,000.00 USD | 0.00 USD | 170,120.00 USD | `-23.72%` | `55,868.00` |
| `Live` | `Long` | `3.06` | 9,700,000.00 USD | 0.00 USD | 25,520.00 USD | `-23.47%` | `8,354.70` |
| `Live` | `Long` | `3.06` | 9,670,000.00 USD | 0.00 USD | 116,000.00 USD | `-23.22%` | `37,845.20` |
| `Live` | `Long` | `3.08` | 9,560,000.00 USD | 0.00 USD | 3,090.00 USD | `-22.97%` | `1,004.90` |
| `Live` | `Long` | `3.08` | 9,560,000.00 USD | 0.00 USD | 32,250.00 USD | `-22.72%` | `10,453.80` |
| `Live` | `Long` | `3.10` | 9,520,000.00 USD | 0.00 USD | 239,320.00 USD | `-22.47%` | `77,325.90` |
| `Live` | `Long` | `3.10` | 9,280,000.00 USD | 0.00 USD | 17,980.00 USD | `-22.22%` | `5,789.50` |
| `Live` | `Long` | `3.12` | 9,270,000.00 USD | 0.00 USD | 36,650.00 USD | `-21.97%` | `11,765.20` |
| `Live` | `Long` | `3.12` | 9,230,000.00 USD | 0.00 USD | 15,600.00 USD | `-21.71%` | `4,992.10` |
| `Live` | `Long` | `3.13` | 9,210,000.00 USD | 0.00 USD | 228,890.00 USD | `-21.46%` | `73,009.80` |
| `Live` | `Long` | `3.15` | 8,980,000.00 USD | 0.00 USD | 23,000.00 USD | `-21.21%` | `7,314.70` |
| `Live` | `Long` | `3.15` | 8,960,000.00 USD | 0.00 USD | 46,550.00 USD | `-20.96%` | `14,753.20` |
| `Live` | `Long` | `3.17` | 8,910,000.00 USD | 0.00 USD | 7,040.00 USD | `-20.71%` | `2,225.90` |
| `Live` | `Long` | `3.17` | 8,910,000.00 USD | 0.00 USD | 6,970.00 USD | `-20.46%` | `2,195.30` |
| `Live` | `Long` | `3.19` | 8,900,000.00 USD | 0.00 USD | 245,480.00 USD | `-20.21%` | `77,072.50` |
| `Live` | `Long` | `3.21` | 8,660,000.00 USD | 0.00 USD | 1,090.00 USD | `-19.71%` | `340.40` |
| `Live` | `Long` | `3.21` | 8,650,000.00 USD | 0.00 USD | 19,660.00 USD | `-19.46%` | `6,116.10` |
| `Live` | `Long` | `3.23` | 8,630,000.00 USD | 0.00 USD | 338,820.00 USD | `-19.21%` | `105,060.80` |
| `Live` | `Long` | `3.23` | 8,300,000.00 USD | 0.00 USD | 42,020.00 USD | `-18.96%` | `12,989.40` |
| `Live` | `Long` | `3.25` | 8,250,000.00 USD | 0.00 USD | 20,160.00 USD | `-18.71%` | `6,211.80` |
| `Live` | `Long` | `3.25` | 8,230,000.00 USD | 0.00 USD | 5,640.00 USD | `-18.46%` | `1,733.30` |
| `Live` | `Long` | `3.27` | 8,230,000.00 USD | 0.00 USD | 51,020.00 USD | `-18.21%` | `15,625.40` |
| `Live` | `Long` | `3.27` | 8,180,000.00 USD | 0.00 USD | 841,550.00 USD | `-17.96%` | `256,960.50` |
| `Live` | `Long` | `3.29` | 7,340,000.00 USD | 0.00 USD | 61,360.00 USD | `-17.71%` | `18,679.50` |
| `Live` | `Long` | `3.29` | 7,270,000.00 USD | 0.00 USD | 135,090.00 USD | `-17.46%` | `40,997.30` |
| `Live` | `Long` | `3.31` | 7,140,000.00 USD | 0.00 USD | 308,100.00 USD | `-17.21%` | `93,222.80` |
| `Live` | `Long` | `3.31` | 6,830,000.00 USD | 0.00 USD | 134,620.00 USD | `-16.95%` | `40,610.10` |
| `Live` | `Long` | `3.33` | 6,700,000.00 USD | 0.00 USD | 14,710.00 USD | `-16.70%` | `4,423.40` |
| `Live` | `Long` | `3.33` | 6,680,000.00 USD | 0.00 USD | 115,790.00 USD | `-16.45%` | `34,719.90` |
| `Live` | `Long` | `3.35` | 6,570,000.00 USD | 0.00 USD | 56,630.00 USD | `-16.20%` | `16,930.70` |
| `Live` | `Long` | `3.35` | 6,510,000.00 USD | 0.00 USD | 1,480.00 USD | `-15.95%` | `439.70` |
| `Live` | `Long` | `3.37` | 6,510,000.00 USD | 0.00 USD | 2,060.00 USD | `-15.70%` | `613.20` |
| `Live` | `Long` | `3.38` | 6,510,000.00 USD | 0.00 USD | 159,680.00 USD | `-15.45%` | `47,313.80` |
| `Live` | `Long` | `3.38` | 6,350,000.00 USD | 0.00 USD | 43,640.00 USD | `-15.20%` | `12,892.50` |
| `Live` | `Long` | `3.40` | 6,300,000.00 USD | 0.00 USD | 83,190.00 USD | `-14.70%` | `24,430.60` |
| `Live` | `Long` | `3.42` | 6,220,000.00 USD | 0.00 USD | 383,360.00 USD | `-14.45%` | `112,258.80` |
| `Live` | `Long` | `3.42` | 5,840,000.00 USD | 0.00 USD | 28,690.00 USD | `-14.20%` | `8,375.70` |
| `Live` | `Long` | `3.44` | 5,810,000.00 USD | 0.00 USD | 26,030.00 USD | `-13.95%` | `7,579.20` |
| `Live` | `Long` | `3.44` | 5,780,000.00 USD | 0.00 USD | 46,740.00 USD | `-13.70%` | `13,566.50` |
| `Live` | `Long` | `3.46` | 5,730,000.00 USD | 0.00 USD | 8,840.00 USD | `-13.45%` | `2,557.60` |
| `Live` | `Long` | `3.46` | 5,730,000.00 USD | 0.00 USD | 14,340.00 USD | `-13.20%` | `4,139.70` |
| `Live` | `Long` | `3.48` | 5,710,000.00 USD | 0.00 USD | 180,040.00 USD | `-12.95%` | `51,808.90` |
| `Live` | `Long` | `3.48` | 5,530,000.00 USD | 0.00 USD | 24,990.00 USD | `-12.70%` | `7,171.90` |
| `Live` | `Long` | `3.50` | 5,510,000.00 USD | 0.00 USD | 69,220.00 USD | `-12.45%` | `19,806.10` |
| `Live` | `Long` | `3.50` | 5,440,000.00 USD | 0.00 USD | 31,490.00 USD | `-12.19%` | `8,985.10` |
| `Live` | `Long` | `3.52` | 5,410,000.00 USD | 0.00 USD | 7,350.00 USD | `-11.94%` | `2,090.30` |
| `Live` | `Long` | `3.52` | 5,400,000.00 USD | 0.00 USD | 189,090.00 USD | `-11.69%` | `53,642.00` |
| `Live` | `Long` | `3.54` | 5,210,000.00 USD | 0.00 USD | 79,310.00 USD | `-11.44%` | `22,435.30` |
| `Live` | `Long` | `3.54` | 5,130,000.00 USD | 0.00 USD | 177,080.00 USD | `-11.19%` | `49,951.00` |
| `Live` | `Long` | `3.56` | 4,950,000.00 USD | 0.00 USD | 375,580.00 USD | `-10.94%` | `105,649.30` |
| `Live` | `Long` | `3.56` | 4,580,000.00 USD | 0.00 USD | 9,280.00 USD | `-10.69%` | `2,602.40` |
| `Live` | `Long` | `3.58` | 4,570,000.00 USD | 0.00 USD | 62,290.00 USD | `-10.44%` | `17,422.80` |
| `Live` | `Long` | `3.58` | 4,510,000.00 USD | 0.00 USD | 94,480.00 USD | `-10.19%` | `26,354.10` |
| `Live` | `Long` | `3.60` | 4,410,000.00 USD | 0.00 USD | 1,330,000.00 USD | `-9.94%` | `369,558.40` |
| `Live` | `Long` | `3.60` | 3,080,000.00 USD | 0.00 USD | 60,200.00 USD | `-9.69%` | `16,699.70` |
| `Live` | `Long` | `3.62` | 3,020,000.00 USD | 0.00 USD | 3,620.00 USD | `-9.44%` | `1,002.30` |
| `Live` | `Long` | `3.62` | 3,020,000.00 USD | 0.00 USD | 43,700.00 USD | `-9.19%` | `12,055.00` |
| `Live` | `Long` | `3.63` | 2,970,000.00 USD | 0.00 USD | 2,680.00 USD | `-8.94%` | `737.90` |
| `Live` | `Long` | `3.65` | 2,970,000.00 USD | 0.00 USD | 43,430.00 USD | `-8.69%` | `11,915.60` |
| `Live` | `Long` | `3.65` | 2,930,000.00 USD | 0.00 USD | 20,650.00 USD | `-8.44%` | `5,648.90` |
| `Live` | `Long` | `3.67` | 2,910,000.00 USD | 0.00 USD | 141,430.00 USD | `-8.19%` | `38,590.50` |
| `Live` | `Long` | `3.67` | 2,770,000.00 USD | 0.00 USD | 220,440.00 USD | `-7.94%` | `59,984.00` |
| `Live` | `Long` | `3.69` | 2,550,000.00 USD | 0.00 USD | 144,940.00 USD | `-7.69%` | `39,333.10` |
| `Live` | `Long` | `3.69` | 2,400,000.00 USD | 0.00 USD | 111,990.00 USD | `-7.44%` | `30,308.40` |
| `Live` | `Long` | `3.71` | 2,290,000.00 USD | 0.00 USD | 229,560.00 USD | `-7.18%` | `61,960.10` |
| `Live` | `Long` | `3.71` | 2,060,000.00 USD | 0.00 USD | 50,160.00 USD | `-6.93%` | `13,503.10` |
| `Live` | `Long` | `3.73` | 2,010,000.00 USD | 0.00 USD | 179,640.00 USD | `-6.68%` | `48,224.70` |
| `Live` | `Long` | `3.73` | 1,830,000.00 USD | 0.00 USD | 141,610.00 USD | `-6.43%` | `37,915.10` |
| `Live` | `Long` | `3.75` | 1,690,000.00 USD | 0.00 USD | 96,600.00 USD | `-6.18%` | `25,794.60` |
| `Live` | `Long` | `3.75` | 1,590,000.00 USD | 0.00 USD | 165,310.00 USD | `-5.93%` | `44,024.00` |
| `Live` | `Long` | `3.77` | 1,430,000.00 USD | 0.00 USD | 279,910.00 USD | `-5.68%` | `74,344.20` |
| `Live` | `Long` | `3.77` | 1,150,000.00 USD | 0.00 USD | 139,340.00 USD | `-5.43%` | `36,910.00` |
| `Live` | `Long` | `3.79` | 1,010,000.00 USD | 0.00 USD | 26,860.00 USD | `-5.18%` | `7,096.60` |
| `Live` | `Long` | `3.79` | 980,140.00 USD | 0.00 USD | 150,080.00 USD | `-4.93%` | `39,546.90` |
| `Live` | `Long` | `3.81` | 830,060.00 USD | 0.00 USD | 106,830.00 USD | `-4.68%` | `28,076.20` |
| `Live` | `Long` | `3.81` | 723,230.00 USD | 0.00 USD | 126,250.00 USD | `-4.43%` | `33,094.00` |
| `Live` | `Long` | `3.83` | 596,980.00 USD | 0.00 USD | 32,950.00 USD | `-4.18%` | `8,614.40` |
| `Live` | `Long` | `3.83` | 564,030.00 USD | 0.00 USD | 207,520.00 USD | `-3.93%` | `54,111.30` |
| `Live` | `Long` | `3.85` | 356,510.00 USD | 0.00 USD | 125,510.00 USD | `-3.68%` | `32,642.50` |
| `Live` | `Long` | `3.85` | 231,000.00 USD | 0.00 USD | 19,690.00 USD | `-3.43%` | `5,107.30` |
| `Live` | `Long` | `3.87` | 211,310.00 USD | 0.00 USD | 76,590.00 USD | `-3.18%` | `19,816.20` |
| `Live` | `Long` | `3.88` | 134,720.00 USD | 0.00 USD | 11,710.00 USD | `-2.93%` | `3,021.80` |
| `Live` | `Long` | `3.88` | 123,010.00 USD | 0.00 USD | 44,870.00 USD | `-2.68%` | `11,548.80` |
| `Live` | `Long` | `3.90` | 78,150.00 USD | 0.00 USD | 73,800.00 USD | `-2.42%` | `18,946.50` |
| `Live` | `Long` | `3.90` | 4,350.00 USD | 0.00 USD | 4,350.00 USD | `-2.17%` | `1,114.10` |
| `Live` | `Short` | `4.04` | 2,180.00 USD | 2,180.00 USD | 0.00 USD | `+1.33%` | `539.20` |
| `Live` | `Short` | `4.11` | 5,150.00 USD | 2,960.00 USD | 0.00 USD | `+2.84%` | `722.20` |
| `Live` | `Short` | `4.12` | 6,850.00 USD | 1,700.00 USD | 0.00 USD | `+3.09%` | `413.40` |
| `Live` | `Short` | `4.12` | 41,880.00 USD | 35,040.00 USD | 0.00 USD | `+3.34%` | `8,493.50` |
| `Live` | `Short` | `4.14` | 47,500.00 USD | 5,620.00 USD | 0.00 USD | `+3.84%` | `1,355.60` |
| `Live` | `Short` | `4.16` | 48,140.00 USD | 638.21 USD | 0.00 USD | `+4.09%` | `153.60` |
| `Live` | `Short` | `4.17` | 89,790.00 USD | 41,650.00 USD | 0.00 USD | `+4.34%` | `10,001.10` |
| `Live` | `Short` | `4.17` | 92,130.00 USD | 2,340.00 USD | 0.00 USD | `+4.59%` | `560.50` |
| `Live` | `Short` | `4.18` | 93,420.00 USD | 1,280.00 USD | 0.00 USD | `+4.84%` | `306.60` |
| `Live` | `Short` | `4.20` | 99,950.00 USD | 6,530.00 USD | 0.00 USD | `+5.09%` | `1,556.40` |
| `Live` | `Short` | `4.21` | 100,140.00 USD | 194.69 USD | 0.00 USD | `+5.34%` | `46.30` |
| `Live` | `Short` | `4.21` | 102,260.00 USD | 2,120.00 USD | 0.00 USD | `+5.59%` | `501.80` |
| `Live` | `Short` | `4.22` | 114,210.00 USD | 11,950.00 USD | 0.00 USD | `+5.84%` | `2,829.10` |
| `Live` | `Short` | `4.24` | 115,400.00 USD | 1,190.00 USD | 0.00 USD | `+6.09%` | `280.00` |
| `Live` | `Short` | `4.25` | 116,040.00 USD | 649.06 USD | 0.00 USD | `+6.34%` | `152.90` |
| `Live` | `Short` | `4.25` | 117,820.00 USD | 1,780.00 USD | 0.00 USD | `+6.59%` | `417.20` |
| `Live` | `Short` | `4.26` | 118,150.00 USD | 328.41 USD | 0.00 USD | `+6.84%` | `77.00` |
| `Live` | `Short` | `4.29` | 118,310.00 USD | 163.69 USD | 0.00 USD | `+7.35%` | `38.20` |
| `Live` | `Short` | `4.29` | 329,040.00 USD | 210,730.00 USD | 0.00 USD | `+7.60%` | `49,064.30` |
| `Live` | `Short` | `4.30` | 329,620.00 USD | 573.00 USD | 0.00 USD | `+7.85%` | `133.10` |
| `Live` | `Short` | `4.32` | 358,010.00 USD | 28,390.00 USD | 0.00 USD | `+8.10%` | `6,580.40` |
| `Live` | `Short` | `4.34` | 427,430.00 USD | 69,420.00 USD | 0.00 USD | `+8.85%` | `15,977.80` |
| `Live` | `Short` | `4.36` | 432,400.00 USD | 4,970.00 USD | 0.00 USD | `+9.10%` | `1,141.00` |
| `Live` | `Short` | `4.37` | 454,380.00 USD | 21,970.00 USD | 0.00 USD | `+9.35%` | `5,034.30` |
| `Live` | `Short` | `4.38` | 455,490.00 USD | 1,110.00 USD | 0.00 USD | `+9.60%` | `254.40` |
| `Live` | `Short` | `4.39` | 648,200.00 USD | 192,710.00 USD | 0.00 USD | `+10.10%` | `43,846.50` |
| `Live` | `Short` | `4.41` | 649,600.00 USD | 1,410.00 USD | 0.00 USD | `+10.35%` | `319.80` |
| `Live` | `Short` | `4.42` | 702,550.00 USD | 52,950.00 USD | 0.00 USD | `+10.60%` | `11,993.20` |
| `Live` | `Short` | `4.42` | 702,660.00 USD | 104.87 USD | 0.00 USD | `+10.85%` | `23.70` |
| `Live` | `Short` | `4.46` | 703,130.00 USD | 468.38 USD | 0.00 USD | `+11.85%` | `104.90` |
| `Live` | `Short` | `4.47` | 704,330.00 USD | 1,200.00 USD | 0.00 USD | `+12.10%` | `268.70` |
| `Live` | `Short` | `4.49` | 721,080.00 USD | 16,750.00 USD | 0.00 USD | `+12.36%` | `3,735.50` |
| `Live` | `Short` | `4.50` | 811,260.00 USD | 90,180.00 USD | 0.00 USD | `+12.61%` | `20,062.40` |
| `Live` | `Short` | `4.50` | 876,970.00 USD | 65,700.00 USD | 0.00 USD | `+12.86%` | `14,584.50` |
| `Live` | `Short` | `4.51` | 877,360.00 USD | 389.19 USD | 0.00 USD | `+13.11%` | `86.20` |
| `Live` | `Short` | `4.53` | 896,180.00 USD | 18,820.00 USD | 0.00 USD | `+13.36%` | `4,160.10` |
| `Live` | `Short` | `4.54` | 896,380.00 USD | 198.18 USD | 0.00 USD | `+13.61%` | `43.70` |
| `Live` | `Short` | `4.54` | 896,630.00 USD | 252.70 USD | 0.00 USD | `+13.86%` | `55.60` |
| `Live` | `Short` | `4.55` | 905,620.00 USD | 8,980.00 USD | 0.00 USD | `+14.11%` | `1,972.40` |
| `Live` | `Short` | `4.57` | 905,860.00 USD | 243.77 USD | 0.00 USD | `+14.36%` | `53.40` |
| `Live` | `Short` | `4.58` | 920,550.00 USD | 14,690.00 USD | 0.00 USD | `+14.61%` | `3,211.90` |
| `Live` | `Short` | `4.61` | 1,080,000.00 USD | 156,780.00 USD | 0.00 USD | `+15.36%` | `34,045.00` |
| `Live` | `Short` | `4.62` | 1,080,000.00 USD | 203.50 USD | 0.00 USD | `+15.86%` | `44.00` |
| `Live` | `Short` | `4.63` | 1,080,000.00 USD | 990.04 USD | 0.00 USD | `+16.11%` | `213.60` |
| `Live` | `Short` | `4.64` | 1,080,000.00 USD | 3,950.00 USD | 0.00 USD | `+16.36%` | `849.60` |
| `Live` | `Short` | `4.66` | 1,080,000.00 USD | 8.84 USD | 0.00 USD | `+16.61%` | `1.90` |
| `Live` | `Short` | `4.67` | 1,080,000.00 USD | 101.70 USD | 0.00 USD | `+16.86%` | `21.80` |
| `Live` | `Short` | `4.70` | 1,080,000.00 USD | 230.06 USD | 0.00 USD | `+17.62%` | `49.00` |
| `Live` | `Short` | `4.71` | 1,090,000.00 USD | 7,480.00 USD | 0.00 USD | `+17.87%` | `1,590.30` |
| `Live` | `Short` | `4.71` | 1,090,000.00 USD | 460.18 USD | 0.00 USD | `+18.12%` | `97.60` |
| `Live` | `Short` | `4.75` | 1,110,000.00 USD | 21,230.00 USD | 0.00 USD | `+18.87%` | `4,474.30` |
| `Live` | `Short` | `4.76` | 1,180,000.00 USD | 64,260.00 USD | 0.00 USD | `+19.37%` | `13,485.80` |
| `Live` | `Short` | `4.78` | 1,190,000.00 USD | 8,780.00 USD | 0.00 USD | `+19.62%` | `1,839.40` |
| `Live` | `Short` | `4.79` | 1,190,000.00 USD | 4,420.00 USD | 0.00 USD | `+19.87%` | `924.20` |
| `Live` | `Short` | `4.79` | 1,190,000.00 USD | 1,330.00 USD | 0.00 USD | `+20.12%` | `277.70` |
| `Live` | `Short` | `4.82` | 1,240,000.00 USD | 45,670.00 USD | 0.00 USD | `+20.62%` | `9,484.50` |
| `Live` | `Short` | `4.83` | 1,240,000.00 USD | 3,020.00 USD | 0.00 USD | `+20.87%` | `625.50` |
| `Live` | `Short` | `4.83` | 1,240,000.00 USD | 1,950.00 USD | 0.00 USD | `+21.12%` | `403.60` |
| `Live` | `Short` | `4.84` | 1,250,000.00 USD | 11,220.00 USD | 0.00 USD | `+21.37%` | `2,316.40` |
| `Live` | `Short` | `4.87` | 1,250,000.00 USD | 1,350.00 USD | 0.00 USD | `+21.87%` | `276.90` |
| `Live` | `Short` | `4.88` | 1,250,000.00 USD | 827.03 USD | 0.00 USD | `+22.38%` | `169.30` |
| `Live` | `Short` | `4.92` | 1,280,000.00 USD | 20,720.00 USD | 0.00 USD | `+23.13%` | `4,214.80` |
| `Live` | `Short` | `4.92` | 1,280,000.00 USD | 2,100.00 USD | 0.00 USD | `+23.38%` | `425.70` |
| `Live` | `Short` | `4.93` | 1,280,000.00 USD | 157.43 USD | 0.00 USD | `+23.63%` | `31.90` |
| `Live` | `Short` | `4.96` | 1,280,000.00 USD | 342.89 USD | 0.00 USD | `+24.13%` | `69.20` |
| `Live` | `Short` | `4.97` | 1,380,000.00 USD | 99,810.00 USD | 0.00 USD | `+24.63%` | `20,062.00` |
| `Live` | `Short` | `4.99` | 1,380,000.00 USD | 611.16 USD | 0.00 USD | `+24.88%` | `122.60` |
| `Live` | `Short` | `5.00` | 1,380,000.00 USD | 339.66 USD | 0.00 USD | `+25.13%` | `68.00` |
| `Live` | `Short` | `5.07` | 1,380,000.00 USD | 3,420.00 USD | 0.00 USD | `+26.89%` | `675.80` |
| `Live` | `Short` | `5.08` | 1,390,000.00 USD | 2,720.00 USD | 0.00 USD | `+27.39%` | `534.60` |
| `Live` | `Short` | `5.12` | 1,390,000.00 USD | 2,560.00 USD | 0.00 USD | `+28.39%` | `500.00` |
| `Live` | `Short` | `5.14` | 1,410,000.00 USD | 20,690.00 USD | 0.00 USD | `+28.89%` | `4,022.20` |
| `Live` | `Short` | `5.17` | 1,410,000.00 USD | 751.51 USD | 0.00 USD | `+29.39%` | `145.50` |
| `Live` | `Short` | `5.20` | 1,420,000.00 USD | 7,280.00 USD | 0.00 USD | `+30.14%` | `1,401.50` |
| `Live` | `Short` | `5.22` | 1,490,000.00 USD | 72,110.00 USD | 0.00 USD | `+30.89%` | `13,800.00` |
| `Live` | `Short` | `5.25` | 1,490,000.00 USD | 2,770.00 USD | 0.00 USD | `+31.39%` | `527.40` |
| `Live` | `Short` | `5.25` | 2,540,000.00 USD | 1,050,000.00 USD | 0.00 USD | `+31.64%` | `200,054.90` |
| `Live` | `Short` | `5.26` | 2,550,000.00 USD | 5,610.00 USD | 0.00 USD | `+31.90%` | `1,066.10` |
| `Live` | `Short` | `5.29` | 2,550,000.00 USD | 134.77 USD | 0.00 USD | `+32.40%` | `25.50` |
| `Live` | `Short` | `5.30` | 2,550,000.00 USD | 524.66 USD | 0.00 USD | `+32.90%` | `98.90` |
| `Live` | `Short` | `5.32` | 2,550,000.00 USD | 718.59 USD | 0.00 USD | `+33.15%` | `135.20` |
| `Live` | `Short` | `5.36` | 2,590,000.00 USD | 43,340.00 USD | 0.00 USD | `+34.15%` | `8,093.00` |
| `Live` | `Short` | `5.38` | 2,590,000.00 USD | 620.89 USD | 0.00 USD | `+34.90%` | `115.30` |
| `Live` | `Short` | `5.41` | 2,600,000.00 USD | 5,410.00 USD | 0.00 USD | `+35.40%` | `1,000.00` |
| `Live` | `Short` | `5.43` | 2,620,000.00 USD | 20,870.00 USD | 0.00 USD | `+36.15%` | `3,840.00` |
| `Live` | `Short` | `5.46` | 2,720,000.00 USD | 104,530.00 USD | 0.00 USD | `+36.66%` | `19,161.60` |
| `Live` | `Short` | `5.46` | 2,730,000.00 USD | 1,370.00 USD | 0.00 USD | `+36.91%` | `250.00` |
| `Live` | `Short` | `5.47` | 2,730,000.00 USD | 627.98 USD | 0.00 USD | `+37.16%` | `114.70` |
| `Live` | `Short` | `5.50` | 2,790,000.00 USD | 66,470.00 USD | 0.00 USD | `+37.66%` | `12,097.30` |
| `Live` | `Short` | `5.51` | 2,830,000.00 USD | 38,800.00 USD | 0.00 USD | `+38.16%` | `7,034.90` |
| `Live` | `Short` | `5.53` | 2,830,000.00 USD | 712.73 USD | 0.00 USD | `+38.41%` | `129.00` |
| `Live` | `Short` | `5.54` | 2,860,000.00 USD | 26,740.00 USD | 0.00 USD | `+38.66%` | `4,831.90` |
| `Live` | `Short` | `5.55` | 2,860,000.00 USD | 3,720.00 USD | 0.00 USD | `+39.16%` | `669.20` |
| `Live` | `Short` | `5.57` | 2,870,000.00 USD | 8,670.00 USD | 0.00 USD | `+39.41%` | `1,557.40` |
| `Live` | `Short` | `5.58` | 2,930,000.00 USD | 62,420.00 USD | 0.00 USD | `+39.91%` | `11,175.80` |
| `Live` | `Short` | `5.59` | 2,990,000.00 USD | 56,640.00 USD | 0.00 USD | `+40.16%` | `10,122.70` |
| `Live` | `Short` | `5.61` | 3,080,000.00 USD | 89,690.00 USD | 0.00 USD | `+40.41%` | `16,001.10` |
| `Live` | `Short` | `5.63` | 3,140,000.00 USD | 63,090.00 USD | 0.00 USD | `+41.16%` | `11,196.20` |
| `Live` | `Short` | `5.67` | 3,450,000.00 USD | 303,310.00 USD | 0.00 USD | `+41.92%` | `53,540.70` |
| `Live` | `Short` | `5.67` | 3,450,000.00 USD | 228.70 USD | 0.00 USD | `+42.17%` | `40.30` |
| `Live` | `Short` | `5.68` | 3,470,000.00 USD | 26,090.00 USD | 0.00 USD | `+42.42%` | `4,589.50` |
| `Live` | `Short` | `5.70` | 3,470,000.00 USD | 1,520.00 USD | 0.00 USD | `+42.67%` | `267.40` |
| `Live` | `Short` | `5.71` | 3,480,000.00 USD | 2,130.00 USD | 0.00 USD | `+43.17%` | `372.40` |
| `Live` | `Short` | `5.72` | 3,480,000.00 USD | 169.46 USD | 0.00 USD | `+43.42%` | `29.60` |
| `Live` | `Short` | `5.75` | 5,150,000.00 USD | 1,670,000.00 USD | 0.00 USD | `+43.92%` | `291,024.80` |
| `Live` | `Short` | `5.75` | 5,150,000.00 USD | 286.02 USD | 0.00 USD | `+44.17%` | `49.70` |
| `Live` | `Short` | `5.79` | 5,280,000.00 USD | 132,520.00 USD | 0.00 USD | `+45.17%` | `22,867.70` |
| `Live` | `Short` | `5.80` | 5,280,000.00 USD | 2,670.00 USD | 0.00 USD | `+45.42%` | `460.20` |
| `Live` | `Short` | `5.82` | 5,280,000.00 USD | 127.93 USD | 0.00 USD | `+45.67%` | `22.00` |
| `Live` | `Short` | `5.83` | 5,620,000.00 USD | 337,490.00 USD | 0.00 USD | `+45.92%` | `57,938.40` |
| `Live` | `Short` | `5.84` | 5,620,000.00 USD | 310.95 USD | 0.00 USD | `+46.43%` | `53.20` |
| `Live` | `Short` | `5.86` | 5,620,000.00 USD | 848.39 USD | 0.00 USD | `+46.68%` | `144.90` |
| `Live` | `Short` | `5.88` | 5,620,000.00 USD | 200.34 USD | 0.00 USD | `+47.18%` | `34.10` |
| `Live` | `Short` | `5.88` | 5,630,000.00 USD | 7,150.00 USD | 0.00 USD | `+47.43%` | `1,215.40` |
| `Live` | `Short` | `5.89` | 5,720,000.00 USD | 88,590.00 USD | 0.00 USD | `+47.68%` | `15,027.60` |
| `Live` | `Short` | `5.92` | 5,720,000.00 USD | 189.28 USD | 0.00 USD | `+48.18%` | `32.00` |
| `Live` | `Short` | `5.95` | 5,820,000.00 USD | 103,650.00 USD | 0.00 USD | `+48.93%` | `17,434.80` |
| `Live` | `Short` | `6.00` | 5,820,000.00 USD | 154.07 USD | 0.00 USD | `+50.18%` | `25.70` |
| `Live` | `Short` | `6.03` | 5,850,000.00 USD | 23,060.00 USD | 0.00 USD | `+50.93%` | `3,827.40` |
| `Live` | `Short` | `6.07` | 5,850,000.00 USD | 740.54 USD | 0.00 USD | `+51.94%` | `122.10` |
| `Live` | `Short` | `6.08` | 5,850,000.00 USD | 5,920.00 USD | 0.00 USD | `+52.44%` | `973.10` |
| `Live` | `Short` | `6.09` | 5,890,000.00 USD | 37,510.00 USD | 0.00 USD | `+52.69%` | `6,154.10` |
| `Live` | `Short` | `6.12` | 5,890,000.00 USD | 1,870.00 USD | 0.00 USD | `+53.19%` | `305.00` |
| `Live` | `Short` | `6.12` | 5,900,000.00 USD | 5,220.00 USD | 0.00 USD | `+53.44%` | `852.80` |
| `Live` | `Short` | `6.13` | 5,900,000.00 USD | 2,430.00 USD | 0.00 USD | `+53.69%` | `396.10` |
| `Live` | `Short` | `6.21` | 5,950,000.00 USD | 46,080.00 USD | 0.00 USD | `+55.69%` | `7,415.00` |
| `Live` | `Short` | `6.25` | 5,980,000.00 USD | 31,550.00 USD | 0.00 USD | `+56.45%` | `5,052.70` |
| `Live` | `Short` | `6.25` | 5,980,000.00 USD | 439.10 USD | 0.00 USD | `+56.70%` | `70.20` |
| `Live` | `Short` | `6.28` | 5,980,000.00 USD | 397.84 USD | 0.00 USD | `+57.20%` | `63.40` |
| `Live` | `Short` | `6.29` | 6,270,000.00 USD | 291,020.00 USD | 0.00 USD | `+57.70%` | `46,230.70` |
| `Live` | `Short` | `6.32` | 6,270,000.00 USD | 1,200.00 USD | 0.00 USD | `+58.20%` | `189.80` |
| `Live` | `Short` | `6.33` | 6,270,000.00 USD | 382.00 USD | 0.00 USD | `+58.70%` | `60.30` |
| `Live` | `Short` | `6.34` | 6,270,000.00 USD | 214.46 USD | 0.00 USD | `+58.95%` | `33.80` |
| `Live` | `Short` | `6.37` | 6,270,000.00 USD | 113.93 USD | 0.00 USD | `+59.45%` | `17.90` |
| `Live` | `Short` | `6.38` | 6,270,000.00 USD | 1,460.00 USD | 0.00 USD | `+59.70%` | `228.80` |
| `Live` | `Short` | `6.39` | 6,270,000.00 USD | 2,000.00 USD | 0.00 USD | `+60.20%` | `312.80` |
| `Live` | `Short` | `6.41` | 6,330,000.00 USD | 55,840.00 USD | 0.00 USD | `+60.45%` | `8,717.50` |
| `Live` | `Short` | `6.42` | 6,340,000.00 USD | 8,700.00 USD | 0.00 USD | `+60.70%` | `1,356.50` |
| `Live` | `Short` | `6.42` | 6,340,000.00 USD | 346.95 USD | 0.00 USD | `+60.95%` | `54.00` |
| `Live` | `Short` | `6.45` | 6,340,000.00 USD | 5,270.00 USD | 0.00 USD | `+61.46%` | `818.40` |
| `Live` | `Short` | `6.46` | 6,350,000.00 USD | 9,270.00 USD | 0.00 USD | `+61.71%` | `1,436.20` |
| `Live` | `Short` | `6.46` | 6,360,000.00 USD | 1,940.00 USD | 0.00 USD | `+61.96%` | `300.00` |
| `Live` | `Short` | `6.51` | 6,360,000.00 USD | 380.48 USD | 0.00 USD | `+63.21%` | `58.40` |
| `Live` | `Short` | `6.54` | 6,370,000.00 USD | 14,180.00 USD | 0.00 USD | `+63.71%` | `2,169.70` |
| `Live` | `Short` | `6.54` | 6,370,000.00 USD | 265.07 USD | 0.00 USD | `+63.96%` | `40.50` |
| `Live` | `Short` | `6.58` | 6,460,000.00 USD | 87,890.00 USD | 0.00 USD | `+64.71%` | `13,367.10` |
| `Live` | `Short` | `6.58` | 6,460,000.00 USD | 698.67 USD | 0.00 USD | `+64.96%` | `106.10` |
| `Live` | `Short` | `6.59` | 6,460,000.00 USD | 418.78 USD | 0.00 USD | `+65.21%` | `63.50` |
| `Live` | `Short` | `6.61` | 6,460,000.00 USD | 2,050.00 USD | 0.00 USD | `+65.46%` | `310.00` |
| `Live` | `Short` | `6.66` | 6,470,000.00 USD | 7,230.00 USD | 0.00 USD | `+66.72%` | `1,086.90` |
| `Live` | `Short` | `6.67` | 6,470,000.00 USD | 233.94 USD | 0.00 USD | `+66.97%` | `35.10` |
| `Live` | `Short` | `6.67` | 6,470,000.00 USD | 200.25 USD | 0.00 USD | `+67.22%` | `30.00` |
| `Live` | `Short` | `6.75` | 7,720,000.00 USD | 1,250,000.00 USD | 0.00 USD | `+69.22%` | `184,501.00` |
| `Live` | `Short` | `6.78` | 7,760,000.00 USD | 41,940.00 USD | 0.00 USD | `+69.72%` | `6,190.00` |
| `Live` | `Short` | `6.79` | 7,790,000.00 USD | 37,480.00 USD | 0.00 USD | `+70.22%` | `5,515.90` |
| `Live` | `Short` | `6.84` | 7,800,000.00 USD | 872.05 USD | 0.00 USD | `+71.48%` | `127.40` |
| `Live` | `Short` | `6.87` | 7,800,000.00 USD | 2,650.00 USD | 0.00 USD | `+71.98%` | `386.60` |
| `Live` | `Short` | `6.88` | 7,800,000.00 USD | 187.69 USD | 0.00 USD | `+72.23%` | `27.30` |
| `Live` | `Short` | `6.92` | 7,810,000.00 USD | 6,920.00 USD | 0.00 USD | `+73.48%` | `1,000.00` |
| `Live` | `Short` | `6.95` | 7,810,000.00 USD | 190.99 USD | 0.00 USD | `+73.98%` | `27.50` |
| `Live` | `Short` | `6.96` | 7,810,000.00 USD | 171.09 USD | 0.00 USD | `+74.23%` | `24.60` |
| `Live` | `Short` | `6.97` | 7,880,000.00 USD | 69,750.00 USD | 0.00 USD | `+74.73%` | `10,000.00` |
| `Live` | `Short` | `6.99` | 7,880,000.00 USD | 664.27 USD | 0.00 USD | `+74.98%` | `95.10` |
| `Live` | `Short` | `7.08` | 36,470,000.00 USD | 28,590,000.00 USD | 0.00 USD | `+77.24%` | `4,041,616.80` |
| `Live` | `Short` | `7.09` | 36,470,000.00 USD | 699.57 USD | 0.00 USD | `+77.74%` | `98.60` |
| `Live` | `Short` | `7.12` | 36,480,000.00 USD | 9,860.00 USD | 0.00 USD | `+78.49%` | `1,384.00` |
| `Live` | `Short` | `7.18` | 37,830,000.00 USD | 1,350,000.00 USD | 0.00 USD | `+79.99%` | `188,000.00` |
| `Live` | `Short` | `7.21` | 37,850,000.00 USD | 13,560.00 USD | 0.00 USD | `+80.75%` | `1,879.60` |
| `Live` | `Short` | `7.24` | 37,850,000.00 USD | 4,910.00 USD | 0.00 USD | `+81.25%` | `679.30` |
| `Live` | `Short` | `7.25` | 37,860,000.00 USD | 10,990.00 USD | 0.00 USD | `+81.75%` | `1,514.20` |
| `Live` | `Short` | `7.32` | 37,870,000.00 USD | 5,810.00 USD | 0.00 USD | `+83.25%` | `794.40` |
| `Live` | `Short` | `7.33` | 37,870,000.00 USD | 1,320.00 USD | 0.00 USD | `+83.75%` | `180.00` |
| `Live` | `Short` | `7.37` | 37,870,000.00 USD | 181.18 USD | 0.00 USD | `+84.50%` | `24.60` |
| `Live` | `Short` | `7.38` | 37,900,000.00 USD | 26,920.00 USD | 0.00 USD | `+84.75%` | `3,650.70` |
| `Live` | `Short` | `7.42` | 38,000,000.00 USD | 106,000.00 USD | 0.00 USD | `+86.01%` | `14,276.50` |
| `Live` | `Short` | `7.45` | 38,270,000.00 USD | 271,800.00 USD | 0.00 USD | `+86.51%` | `36,507.80` |
| `Live` | `Short` | `7.46` | 38,280,000.00 USD | 7,050.00 USD | 0.00 USD | `+86.76%` | `945.40` |
| `Live` | `Short` | `7.47` | 38,280,000.00 USD | 221.26 USD | 0.00 USD | `+87.26%` | `29.60` |
| `Live` | `Short` | `7.50` | 38,280,000.00 USD | 2,610.00 USD | 0.00 USD | `+88.01%` | `347.20` |
| `Live` | `Short` | `7.53` | 38,290,000.00 USD | 1,570.00 USD | 0.00 USD | `+88.51%` | `208.40` |
| `Live` | `Short` | `7.54` | 38,290,000.00 USD | 789.67 USD | 0.00 USD | `+88.76%` | `104.80` |
| `Live` | `Short` | `7.57` | 46,150,000.00 USD | 7,860,000.00 USD | 0.00 USD | `+89.51%` | `1,039,604.60` |
| `Live` | `Short` | `7.58` | 56,270,000.00 USD | 10,120,000.00 USD | 0.00 USD | `+89.76%` | `1,336,250.00` |
| `Live` | `Short` | `7.63` | 56,290,000.00 USD | 19,210.00 USD | 0.00 USD | `+91.27%` | `2,516.10` |
| `Live` | `Short` | `7.66` | 56,310,000.00 USD | 13,400.00 USD | 0.00 USD | `+91.77%` | `1,750.00` |
| `Live` | `Short` | `7.67` | 56,330,000.00 USD | 27,160.00 USD | 0.00 USD | `+92.02%` | `3,543.50` |
| `Live` | `Short` | `7.72` | 56,330,000.00 USD | 259.56 USD | 0.00 USD | `+93.52%` | `33.60` |
| `Live` | `Short` | `7.74` | 56,330,000.00 USD | 505.87 USD | 0.00 USD | `+93.77%` | `65.40` |
| `Live` | `Short` | `7.75` | 56,330,000.00 USD | 629.67 USD | 0.00 USD | `+94.02%` | `81.30` |
| `Live` | `Short` | `7.75` | 56,370,000.00 USD | 33,410.00 USD | 0.00 USD | `+94.27%` | `4,308.50` |
| `Live` | `Short` | `7.79` | 57,360,000.00 USD | 997,350.00 USD | 0.00 USD | `+95.28%` | `127,947.00` |
| `Live` | `Short` | `7.80` | 57,360,000.00 USD | 231.03 USD | 0.00 USD | `+95.53%` | `29.60` |
| `Live` | `Short` | `7.87` | 57,700,000.00 USD | 334,500.00 USD | 0.00 USD | `+97.03%` | `42,529.90` |
| `Live` | `Short` | `7.92` | 57,700,000.00 USD | 2,310.00 USD | 0.00 USD | `+98.53%` | `290.90` |
| `Live` | `Short` | `7.95` | 57,710,000.00 USD | 6,120.00 USD | 0.00 USD | `+99.03%` | `769.80` |
| `Live` | `Short` | `7.96` | 57,850,000.00 USD | 140,310.00 USD | 0.00 USD | `+99.53%` | `17,616.20` |
| `Live` | `Short` | `7.99` | 62,090,000.00 USD | 4,240,000.00 USD | 0.00 USD | `+100.04%` | `531,050.00` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `0.8050` | 2,100,000.00 USD | 0.00 USD | 107.71 USD | `-79.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.8250` | 2,100,000.00 USD | 0.00 USD | 209.80 USD | `-79.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.00` | 2,100,000.00 USD | 0.00 USD | 585.51 USD | `-74.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.01` | 2,090,000.00 USD | 0.00 USD | 339.82 USD | `-74.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.20` | 2,090,000.00 USD | 0.00 USD | 196.58 USD | `-70.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.34` | 2,090,000.00 USD | 0.00 USD | 331.54 USD | `-66.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.35` | 2,090,000.00 USD | 0.00 USD | 345.25 USD | `-66.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.38` | 2,090,000.00 USD | 0.00 USD | 5,640.00 USD | `-65.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.40` | 2,090,000.00 USD | 0.00 USD | 997.29 USD | `-65.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.51` | 2,090,000.00 USD | 0.00 USD | 139.83 USD | `-62.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.53` | 2,090,000.00 USD | 0.00 USD | 113.28 USD | `-61.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.54` | 2,090,000.00 USD | 0.00 USD | 4,000.00 USD | `-61.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.55` | 2,080,000.00 USD | 0.00 USD | 324.22 USD | `-61.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.59` | 2,080,000.00 USD | 0.00 USD | 4,590.00 USD | `-60.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.61` | 2,080,000.00 USD | 0.00 USD | 739.67 USD | `-59.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.62` | 2,080,000.00 USD | 0.00 USD | 1,740.00 USD | `-59.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.64` | 2,080,000.00 USD | 0.00 USD | 6,260.00 USD | `-59.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.66` | 2,070,000.00 USD | 0.00 USD | 345.40 USD | `-58.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.68` | 2,070,000.00 USD | 0.00 USD | 167.50 USD | `-58.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.70` | 2,070,000.00 USD | 0.00 USD | 669.02 USD | `-57.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.71` | 2,070,000.00 USD | 0.00 USD | 105.88 USD | `-57.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.73` | 2,070,000.00 USD | 0.00 USD | 172.50 USD | `-56.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.77` | 2,070,000.00 USD | 0.00 USD | 10,650.00 USD | `-55.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.80` | 2,060,000.00 USD | 0.00 USD | 722.00 USD | `-54.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.81` | 2,060,000.00 USD | 0.00 USD | 259.00 USD | `-54.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.82` | 2,060,000.00 USD | 0.00 USD | 103.84 USD | `-54.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.83` | 2,060,000.00 USD | 0.00 USD | 109.00 USD | `-54.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.88` | 2,060,000.00 USD | 0.00 USD | 222.19 USD | `-53.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.89` | 2,060,000.00 USD | 0.00 USD | 10,280.00 USD | `-52.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.91` | 2,050,000.00 USD | 0.00 USD | 558.36 USD | `-52.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.93` | 2,040,000.00 USD | 0.00 USD | 1,520.00 USD | `-51.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.94` | 2,040,000.00 USD | 0.00 USD | 222.14 USD | `-51.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.95` | 2,040,000.00 USD | 0.00 USD | 279.50 USD | `-51.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.98` | 2,040,000.00 USD | 0.00 USD | 197.50 USD | `-50.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.00` | 2,040,000.00 USD | 0.00 USD | 935.66 USD | `-50.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.00` | 2,040,000.00 USD | 0.00 USD | 18,860.00 USD | `-49.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.02` | 2,020,000.00 USD | 0.00 USD | 3,020.00 USD | `-49.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.04` | 2,020,000.00 USD | 0.00 USD | 214.52 USD | `-48.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.06` | 2,020,000.00 USD | 0.00 USD | 1,200.00 USD | `-48.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.06` | 2,020,000.00 USD | 0.00 USD | 578.41 USD | `-48.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.10` | 2,020,000.00 USD | 0.00 USD | 18,070.00 USD | `-47.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.10` | 2,000,000.00 USD | 0.00 USD | 108.62 USD | `-47.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.12` | 2,000,000.00 USD | 0.00 USD | 107.23 USD | `-47.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.12` | 2,000,000.00 USD | 0.00 USD | 1,590.00 USD | `-46.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.15` | 2,000,000.00 USD | 0.00 USD | 5,830.00 USD | `-46.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.15` | 1,990,000.00 USD | 0.00 USD | 310.32 USD | `-46.01%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.17` | 1,990,000.00 USD | 0.00 USD | 1,170.00 USD | `-45.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.19` | 1,990,000.00 USD | 0.00 USD | 576.18 USD | `-45.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.19` | 1,990,000.00 USD | 0.00 USD | 295.67 USD | `-45.01%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.21` | 1,990,000.00 USD | 0.00 USD | 1,430.00 USD | `-44.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.21` | 1,990,000.00 USD | 0.00 USD | 812.68 USD | `-44.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.23` | 1,990,000.00 USD | 0.00 USD | 1,590.00 USD | `-44.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.23` | 1,990,000.00 USD | 0.00 USD | 106.16 USD | `-44.01%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.25` | 1,990,000.00 USD | 0.00 USD | 6,270.00 USD | `-43.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.25` | 1,980,000.00 USD | 0.00 USD | 478.06 USD | `-43.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.27` | 1,980,000.00 USD | 0.00 USD | 540.88 USD | `-43.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.27` | 1,980,000.00 USD | 0.00 USD | 1,210.00 USD | `-43.01%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.29` | 1,980,000.00 USD | 0.00 USD | 759.76 USD | `-42.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.29` | 1,980,000.00 USD | 0.00 USD | 11,060.00 USD | `-42.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.31` | 1,970,000.00 USD | 0.00 USD | 3,690.00 USD | `-42.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.33` | 1,960,000.00 USD | 0.00 USD | 3,050.00 USD | `-41.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.33` | 1,960,000.00 USD | 0.00 USD | 467.00 USD | `-41.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.35` | 1,960,000.00 USD | 0.00 USD | 506.75 USD | `-41.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.37` | 1,960,000.00 USD | 0.00 USD | 214.27 USD | `-40.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.38` | 1,960,000.00 USD | 0.00 USD | 428.69 USD | `-40.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.38` | 1,960,000.00 USD | 0.00 USD | 322.45 USD | `-40.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.40` | 1,960,000.00 USD | 0.00 USD | 108.25 USD | `-40.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.40` | 1,960,000.00 USD | 0.00 USD | 3,900.00 USD | `-39.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.42` | 1,950,000.00 USD | 0.00 USD | 799.04 USD | `-39.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.44` | 1,950,000.00 USD | 0.00 USD | 6,830.00 USD | `-39.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.44` | 1,950,000.00 USD | 0.00 USD | 137.16 USD | `-38.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.48` | 1,950,000.00 USD | 0.00 USD | 504.41 USD | `-38.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.48` | 1,940,000.00 USD | 0.00 USD | 963.93 USD | `-37.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.50` | 1,940,000.00 USD | 0.00 USD | 6,690.00 USD | `-37.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.52` | 1,940,000.00 USD | 0.00 USD | 541.98 USD | `-37.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.54` | 1,940,000.00 USD | 0.00 USD | 108.75 USD | `-36.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.54` | 1,940,000.00 USD | 0.00 USD | 766.55 USD | `-36.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.56` | 1,940,000.00 USD | 0.00 USD | 1,010.00 USD | `-35.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.58` | 1,930,000.00 USD | 0.00 USD | 1,100.00 USD | `-35.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.58` | 1,930,000.00 USD | 0.00 USD | 100.04 USD | `-35.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.60` | 1,930,000.00 USD | 0.00 USD | 32,080.00 USD | `-34.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.62` | 1,900,000.00 USD | 0.00 USD | 5,090.00 USD | `-34.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.67` | 1,900,000.00 USD | 0.00 USD | 226.57 USD | `-32.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.69` | 1,900,000.00 USD | 0.00 USD | 104.98 USD | `-32.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.69` | 1,900,000.00 USD | 0.00 USD | 889.89 USD | `-32.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.71` | 1,890,000.00 USD | 0.00 USD | 7,410.00 USD | `-32.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.73` | 1,890,000.00 USD | 0.00 USD | 107.21 USD | `-31.48%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.75` | 1,890,000.00 USD | 0.00 USD | 197.37 USD | `-31.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.75` | 1,890,000.00 USD | 0.00 USD | 8,390.00 USD | `-30.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.77` | 1,880,000.00 USD | 0.00 USD | 108.39 USD | `-30.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.77` | 1,880,000.00 USD | 0.00 USD | 435.95 USD | `-30.48%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.79` | 1,880,000.00 USD | 0.00 USD | 217.23 USD | `-30.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.79` | 1,880,000.00 USD | 0.00 USD | 437.98 USD | `-29.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.81` | 1,880,000.00 USD | 0.00 USD | 2,720.00 USD | `-29.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.83` | 1,870,000.00 USD | 0.00 USD | 8,380.00 USD | `-29.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.85` | 1,870,000.00 USD | 0.00 USD | 109.53 USD | `-28.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.85` | 1,870,000.00 USD | 0.00 USD | 1,230.00 USD | `-28.48%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.88` | 1,870,000.00 USD | 0.00 USD | 1,960.00 USD | `-27.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.88` | 1,860,000.00 USD | 0.00 USD | 746.06 USD | `-27.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.90` | 1,860,000.00 USD | 0.00 USD | 2,900.00 USD | `-27.48%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.90` | 1,860,000.00 USD | 0.00 USD | 4,870.00 USD | `-27.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.92` | 1,850,000.00 USD | 0.00 USD | 696.98 USD | `-26.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.92` | 1,850,000.00 USD | 0.00 USD | 358.90 USD | `-26.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.94` | 1,850,000.00 USD | 0.00 USD | 15,370.00 USD | `-26.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.96` | 1,840,000.00 USD | 0.00 USD | 738.75 USD | `-25.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.96` | 1,840,000.00 USD | 0.00 USD | 523.32 USD | `-25.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.98` | 1,840,000.00 USD | 0.00 USD | 4,470.00 USD | `-25.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.00` | 1,830,000.00 USD | 0.00 USD | 16,630.00 USD | `-24.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.02` | 1,820,000.00 USD | 0.00 USD | 1,020.00 USD | `-24.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.02` | 1,810,000.00 USD | 0.00 USD | 345.76 USD | `-24.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.04` | 1,810,000.00 USD | 0.00 USD | 214.57 USD | `-23.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.04` | 1,810,000.00 USD | 0.00 USD | 249.08 USD | `-23.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.06` | 1,810,000.00 USD | 0.00 USD | 109.42 USD | `-23.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.08` | 1,810,000.00 USD | 0.00 USD | 721.58 USD | `-22.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.10` | 1,810,000.00 USD | 0.00 USD | 9,300.00 USD | `-22.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.12` | 1,800,000.00 USD | 0.00 USD | 8,570.00 USD | `-21.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.12` | 1,800,000.00 USD | 0.00 USD | 104.69 USD | `-21.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.13` | 1,800,000.00 USD | 0.00 USD | 315.69 USD | `-21.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.15` | 1,790,000.00 USD | 0.00 USD | 17,510.00 USD | `-21.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.15` | 1,780,000.00 USD | 0.00 USD | 191,650.00 USD | `-20.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.17` | 1,590,000.00 USD | 0.00 USD | 212.06 USD | `-20.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.17` | 1,590,000.00 USD | 0.00 USD | 1,030.00 USD | `-20.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.19` | 1,580,000.00 USD | 0.00 USD | 218.81 USD | `-20.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.21` | 1,580,000.00 USD | 0.00 USD | 25,410.00 USD | `-19.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.21` | 1,560,000.00 USD | 0.00 USD | 144.67 USD | `-19.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.25` | 1,560,000.00 USD | 0.00 USD | 27,380.00 USD | `-18.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.25` | 1,530,000.00 USD | 0.00 USD | 2,410.00 USD | `-18.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.27` | 1,530,000.00 USD | 0.00 USD | 104.81 USD | `-18.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.27` | 1,530,000.00 USD | 0.00 USD | 200.10 USD | `-17.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.29` | 1,530,000.00 USD | 0.00 USD | 1,310.00 USD | `-17.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.29` | 1,530,000.00 USD | 0.00 USD | 1,870.00 USD | `-17.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.31` | 1,530,000.00 USD | 0.00 USD | 22,800.00 USD | `-17.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.31` | 1,500,000.00 USD | 0.00 USD | 240.67 USD | `-16.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.33` | 1,500,000.00 USD | 0.00 USD | 465.50 USD | `-16.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.33` | 1,500,000.00 USD | 0.00 USD | 6,750.00 USD | `-16.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.35` | 1,500,000.00 USD | 0.00 USD | 505.76 USD | `-16.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.37` | 1,490,000.00 USD | 0.00 USD | 73,220.00 USD | `-15.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.38` | 1,420,000.00 USD | 0.00 USD | 20,860.00 USD | `-15.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.40` | 1,400,000.00 USD | 0.00 USD | 8,490.00 USD | `-14.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.40` | 1,390,000.00 USD | 0.00 USD | 15,700.00 USD | `-14.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.42` | 1,380,000.00 USD | 0.00 USD | 432.68 USD | `-14.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.42` | 1,380,000.00 USD | 0.00 USD | 506.22 USD | `-14.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.44` | 1,380,000.00 USD | 0.00 USD | 171.75 USD | `-13.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.44` | 1,380,000.00 USD | 0.00 USD | 2,550.00 USD | `-13.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.46` | 1,370,000.00 USD | 0.00 USD | 2,430.00 USD | `-13.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.46` | 1,370,000.00 USD | 0.00 USD | 503.81 USD | `-13.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.48` | 1,370,000.00 USD | 0.00 USD | 156.83 USD | `-12.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.50` | 1,370,000.00 USD | 0.00 USD | 894.72 USD | `-12.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.50` | 1,370,000.00 USD | 0.00 USD | 140,120.00 USD | `-12.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.52` | 1,230,000.00 USD | 0.00 USD | 21,320.00 USD | `-11.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.52` | 1,210,000.00 USD | 0.00 USD | 172.02 USD | `-11.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.54` | 1,210,000.00 USD | 0.00 USD | 16,250.00 USD | `-11.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.54` | 1,190,000.00 USD | 0.00 USD | 5,130.00 USD | `-11.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.56` | 1,190,000.00 USD | 0.00 USD | 17,420.00 USD | `-10.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.56` | 1,170,000.00 USD | 0.00 USD | 17,990.00 USD | `-10.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.58` | 1,150,000.00 USD | 0.00 USD | 78,170.00 USD | `-10.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.58` | 1,070,000.00 USD | 0.00 USD | 1,250.00 USD | `-10.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.60` | 1,070,000.00 USD | 0.00 USD | 643.50 USD | `-9.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.60` | 1,070,000.00 USD | 0.00 USD | 14,510.00 USD | `-9.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.62` | 1,060,000.00 USD | 0.00 USD | 632.99 USD | `-9.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.62` | 1,060,000.00 USD | 0.00 USD | 172.19 USD | `-9.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.63` | 1,060,000.00 USD | 0.00 USD | 14,810.00 USD | `-8.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.65` | 1,040,000.00 USD | 0.00 USD | 179.33 USD | `-8.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.65` | 1,040,000.00 USD | 0.00 USD | 4,080.00 USD | `-8.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.67` | 1,040,000.00 USD | 0.00 USD | 3,180.00 USD | `-8.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.67` | 1,030,000.00 USD | 0.00 USD | 367.50 USD | `-7.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.69` | 1,030,000.00 USD | 0.00 USD | 32,120.00 USD | `-7.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.69` | 1,000,000.00 USD | 0.00 USD | 4,370.00 USD | `-7.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.71` | 995,930.00 USD | 0.00 USD | 53,560.00 USD | `-7.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.71` | 942,370.00 USD | 0.00 USD | 6,300.00 USD | `-6.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.73` | 936,070.00 USD | 0.00 USD | 2,490.00 USD | `-6.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.73` | 933,580.00 USD | 0.00 USD | 32,040.00 USD | `-6.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.75` | 901,540.00 USD | 0.00 USD | 28,820.00 USD | `-6.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.75` | 872,720.00 USD | 0.00 USD | 14,230.00 USD | `-5.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.77` | 858,490.00 USD | 0.00 USD | 91,970.00 USD | `-5.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.77` | 766,520.00 USD | 0.00 USD | 536.81 USD | `-5.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.79` | 765,980.00 USD | 0.00 USD | 183.19 USD | `-5.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.79` | 765,800.00 USD | 0.00 USD | 219,990.00 USD | `-4.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.81` | 545,810.00 USD | 0.00 USD | 8,120.00 USD | `-4.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.81` | 537,690.00 USD | 0.00 USD | 21,820.00 USD | `-4.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.83` | 515,860.00 USD | 0.00 USD | 58,010.00 USD | `-4.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.83` | 457,850.00 USD | 0.00 USD | 2,990.00 USD | `-3.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.85` | 454,870.00 USD | 0.00 USD | 42,500.00 USD | `-3.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.85` | 412,370.00 USD | 0.00 USD | 3,550.00 USD | `-3.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.87` | 408,820.00 USD | 0.00 USD | 8,620.00 USD | `-3.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.88` | 400,200.00 USD | 0.00 USD | 160,970.00 USD | `-2.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.88` | 239,230.00 USD | 0.00 USD | 31,190.00 USD | `-2.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.90` | 208,040.00 USD | 0.00 USD | 2,980.00 USD | `-2.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.90` | 205,060.00 USD | 0.00 USD | 94,760.00 USD | `-2.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.92` | 110,290.00 USD | 0.00 USD | 732.89 USD | `-1.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.92` | 109,560.00 USD | 0.00 USD | 73,850.00 USD | `-1.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.94` | 35,710.00 USD | 0.00 USD | 1,050.00 USD | `-1.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.94` | 34,660.00 USD | 0.00 USD | 2,940.00 USD | `-1.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.96` | 31,720.00 USD | 0.00 USD | 26,520.00 USD | `-0.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.96` | 5,200.00 USD | 0.00 USD | 170.89 USD | `-0.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.98` | 5,030.00 USD | 0.00 USD | 4,930.00 USD | `-0.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.98` | 100.42 USD | 0.00 USD | 100.42 USD | `-0.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.00` | 42,510.00 USD | 42,510.00 USD | 0.00 USD | `+0.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.00` | 1,000,000.00 USD | 960,130.00 USD | 0.00 USD | `+0.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.01` | 1,040,000.00 USD | 41,630.00 USD | 0.00 USD | `+0.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.03` | 1,050,000.00 USD | 9,590.00 USD | 0.00 USD | `+0.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.04` | 1,120,000.00 USD | 66,330.00 USD | 0.00 USD | `+1.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.04` | 1,120,000.00 USD | 1,010.00 USD | 0.00 USD | `+1.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.05` | 1,120,000.00 USD | 1,250.00 USD | 0.00 USD | `+1.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.07` | 1,120,000.00 USD | 113.41 USD | 0.00 USD | `+1.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.08` | 1,180,000.00 USD | 53,850.00 USD | 0.00 USD | `+2.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.08` | 1,210,000.00 USD | 30,270.00 USD | 0.00 USD | `+2.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.09` | 1,210,000.00 USD | 3,970.00 USD | 0.00 USD | `+2.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.11` | 1,360,000.00 USD | 144,830.00 USD | 0.00 USD | `+2.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.12` | 1,370,000.00 USD | 11,360.00 USD | 0.00 USD | `+3.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.12` | 1,370,000.00 USD | 265.65 USD | 0.00 USD | `+3.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.13` | 1,390,000.00 USD | 21,400.00 USD | 0.00 USD | `+3.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.14` | 1,390,000.00 USD | 761.02 USD | 0.00 USD | `+3.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.16` | 1,410,000.00 USD | 21,970.00 USD | 0.00 USD | `+4.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.17` | 1,670,000.00 USD | 255,320.00 USD | 0.00 USD | `+4.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.17` | 1,670,000.00 USD | 1,410.00 USD | 0.00 USD | `+4.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.18` | 1,670,000.00 USD | 557.02 USD | 0.00 USD | `+4.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.20` | 2,040,000.00 USD | 371,990.00 USD | 0.00 USD | `+5.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.21` | 2,080,000.00 USD | 37,170.00 USD | 0.00 USD | `+5.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.21` | 2,080,000.00 USD | 687.04 USD | 0.00 USD | `+5.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.22` | 2,080,000.00 USD | 3,890.00 USD | 0.00 USD | `+5.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.24` | 2,110,000.00 USD | 31,590.00 USD | 0.00 USD | `+6.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.25` | 2,120,000.00 USD | 1,770.00 USD | 0.00 USD | `+6.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.25` | 2,150,000.00 USD | 33,240.00 USD | 0.00 USD | `+6.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.26` | 2,150,000.00 USD | 2,180.00 USD | 0.00 USD | `+6.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.28` | 2,150,000.00 USD | 1,870.00 USD | 0.00 USD | `+7.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.29` | 2,160,000.00 USD | 4,400.00 USD | 0.00 USD | `+7.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.29` | 2,190,000.00 USD | 31,730.00 USD | 0.00 USD | `+7.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.30` | 2,220,000.00 USD | 27,110.00 USD | 0.00 USD | `+7.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.32` | 2,220,000.00 USD | 790.51 USD | 0.00 USD | `+8.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.33` | 2,220,000.00 USD | 2,420.00 USD | 0.00 USD | `+8.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.33` | 2,220,000.00 USD | 621.21 USD | 0.00 USD | `+8.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.34` | 2,240,000.00 USD | 17,380.00 USD | 0.00 USD | `+8.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.36` | 2,250,000.00 USD | 14,710.00 USD | 0.00 USD | `+9.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.37` | 2,250,000.00 USD | 464.00 USD | 0.00 USD | `+9.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.38` | 2,280,000.00 USD | 25,510.00 USD | 0.00 USD | `+9.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.38` | 2,280,000.00 USD | 1,540.00 USD | 0.00 USD | `+9.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.39` | 2,280,000.00 USD | 261.50 USD | 0.00 USD | `+10.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.41` | 2,620,000.00 USD | 339,620.00 USD | 0.00 USD | `+10.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.42` | 2,630,000.00 USD | 9,860.00 USD | 0.00 USD | `+10.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.42` | 2,630,000.00 USD | 4,090.00 USD | 0.00 USD | `+10.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.43` | 2,630,000.00 USD | 301.58 USD | 0.00 USD | `+11.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.45` | 2,630,000.00 USD | 889.00 USD | 0.00 USD | `+11.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.46` | 2,700,000.00 USD | 62,240.00 USD | 0.00 USD | `+11.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.46` | 2,700,000.00 USD | 2,360.00 USD | 0.00 USD | `+11.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.47` | 2,700,000.00 USD | 375.90 USD | 0.00 USD | `+12.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.49` | 2,700,000.00 USD | 133.20 USD | 0.00 USD | `+12.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.50` | 2,730,000.00 USD | 29,550.00 USD | 0.00 USD | `+12.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.50` | 3,520,000.00 USD | 787,580.00 USD | 0.00 USD | `+12.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.51` | 3,530,000.00 USD | 13,100.00 USD | 0.00 USD | `+13.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.53` | 3,580,000.00 USD | 52,300.00 USD | 0.00 USD | `+13.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.54` | 3,590,000.00 USD | 3,390.00 USD | 0.00 USD | `+13.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.54` | 3,590,000.00 USD | 1,190.00 USD | 0.00 USD | `+13.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.55` | 3,590,000.00 USD | 1,190.00 USD | 0.00 USD | `+14.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.57` | 3,590,000.00 USD | 227.79 USD | 0.00 USD | `+14.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.58` | 3,630,000.00 USD | 45,750.00 USD | 0.00 USD | `+14.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.58` | 3,640,000.00 USD | 1,150.00 USD | 0.00 USD | `+14.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.59` | 3,650,000.00 USD | 17,590.00 USD | 0.00 USD | `+15.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.61` | 3,660,000.00 USD | 2,950.00 USD | 0.00 USD | `+15.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.62` | 3,660,000.00 USD | 289.82 USD | 0.00 USD | `+15.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.62` | 3,660,000.00 USD | 3,670.00 USD | 0.00 USD | `+15.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.63` | 3,660,000.00 USD | 1,100.00 USD | 0.00 USD | `+16.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.64` | 3,660,000.00 USD | 150.50 USD | 0.00 USD | `+16.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.66` | 3,680,000.00 USD | 21,240.00 USD | 0.00 USD | `+16.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.67` | 3,700,000.00 USD | 16,750.00 USD | 0.00 USD | `+16.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.67` | 3,700,000.00 USD | 617.10 USD | 0.00 USD | `+17.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.68` | 3,720,000.00 USD | 15,710.00 USD | 0.00 USD | `+17.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.70` | 3,720,000.00 USD | 152.12 USD | 0.00 USD | `+17.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.71` | 4,080,000.00 USD | 362,970.00 USD | 0.00 USD | `+17.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.71` | 4,300,000.00 USD | 217,980.00 USD | 0.00 USD | `+18.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.72` | 4,300,000.00 USD | 2,650.00 USD | 0.00 USD | `+18.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.74` | 4,380,000.00 USD | 84,180.00 USD | 0.00 USD | `+18.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.75` | 4,390,000.00 USD | 6,160.00 USD | 0.00 USD | `+18.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.75` | 4,440,000.00 USD | 51,120.00 USD | 0.00 USD | `+19.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.76` | 4,450,000.00 USD | 13,030.00 USD | 0.00 USD | `+19.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.78` | 4,460,000.00 USD | 2,640.00 USD | 0.00 USD | `+19.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.79` | 5,290,000.00 USD | 832,330.00 USD | 0.00 USD | `+19.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.79` | 5,290,000.00 USD | 559.58 USD | 0.00 USD | `+20.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.80` | 5,460,000.00 USD | 175,600.00 USD | 0.00 USD | `+20.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.82` | 5,490,000.00 USD | 20,920.00 USD | 0.00 USD | `+20.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.83` | 5,490,000.00 USD | 8,540.00 USD | 0.00 USD | `+20.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.83` | 5,490,000.00 USD | 283.33 USD | 0.00 USD | `+21.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.84` | 5,510,000.00 USD | 11,760.00 USD | 0.00 USD | `+21.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.86` | 5,530,000.00 USD | 24,370.00 USD | 0.00 USD | `+21.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.87` | 5,550,000.00 USD | 22,170.00 USD | 0.00 USD | `+21.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.88` | 5,560,000.00 USD | 10,400.00 USD | 0.00 USD | `+22.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.88` | 5,580,000.00 USD | 19,890.00 USD | 0.00 USD | `+22.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.89` | 5,590,000.00 USD | 4,060.00 USD | 0.00 USD | `+22.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.91` | 5,710,000.00 USD | 125,180.00 USD | 0.00 USD | `+22.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.92` | 5,710,000.00 USD | 156.30 USD | 0.00 USD | `+23.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.92` | 5,730,000.00 USD | 13,180.00 USD | 0.00 USD | `+23.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.93` | 5,740,000.00 USD | 17,000.00 USD | 0.00 USD | `+23.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.95` | 5,740,000.00 USD | 313.51 USD | 0.00 USD | `+23.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.96` | 5,750,000.00 USD | 5,070.00 USD | 0.00 USD | `+24.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.96` | 5,800,000.00 USD | 47,350.00 USD | 0.00 USD | `+24.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.97` | 5,800,000.00 USD | 187.06 USD | 0.00 USD | `+24.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.99` | 5,890,000.00 USD | 92,570.00 USD | 0.00 USD | `+24.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.00` | 5,890,000.00 USD | 2,540.00 USD | 0.00 USD | `+25.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.00` | 5,930,000.00 USD | 40,910.00 USD | 0.00 USD | `+25.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.01` | 5,960,000.00 USD | 25,080.00 USD | 0.00 USD | `+25.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.03` | 5,960,000.00 USD | 5,030.00 USD | 0.00 USD | `+25.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.04` | 5,980,000.00 USD | 19,640.00 USD | 0.00 USD | `+26.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.04` | 5,980,000.00 USD | 120.58 USD | 0.00 USD | `+26.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.05` | 6,000,000.00 USD | 14,440.00 USD | 0.00 USD | `+26.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.07` | 6,000,000.00 USD | 6,090.00 USD | 0.00 USD | `+26.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.08` | 6,090,000.00 USD | 87,290.00 USD | 0.00 USD | `+27.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.08` | 6,090,000.00 USD | 5,460.00 USD | 0.00 USD | `+27.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.09` | 6,100,000.00 USD | 547.20 USD | 0.00 USD | `+27.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.11` | 6,150,000.00 USD | 52,730.00 USD | 0.00 USD | `+27.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.12` | 6,170,000.00 USD | 18,080.00 USD | 0.00 USD | `+28.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.12` | 6,170,000.00 USD | 179.38 USD | 0.00 USD | `+28.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.13` | 6,170,000.00 USD | 179.72 USD | 0.00 USD | `+28.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.14` | 6,170,000.00 USD | 217.63 USD | 0.00 USD | `+28.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.16` | 6,170,000.00 USD | 493.85 USD | 0.00 USD | `+29.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.17` | 6,170,000.00 USD | 575.38 USD | 0.00 USD | `+29.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.17` | 6,170,000.00 USD | 327.58 USD | 0.00 USD | `+29.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.18` | 6,170,000.00 USD | 163.85 USD | 0.00 USD | `+29.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.20` | 6,290,000.00 USD | 120,930.00 USD | 0.00 USD | `+30.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.21` | 6,330,000.00 USD | 37,960.00 USD | 0.00 USD | `+30.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.21` | 6,330,000.00 USD | 1,710.00 USD | 0.00 USD | `+30.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.22` | 6,330,000.00 USD | 432.63 USD | 0.00 USD | `+30.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.24` | 6,330,000.00 USD | 2,620.00 USD | 0.00 USD | `+31.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.25` | 6,330,000.00 USD | 537.61 USD | 0.00 USD | `+31.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.25` | 6,750,000.00 USD | 420,400.00 USD | 0.00 USD | `+31.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.26` | 6,750,000.00 USD | 278.52 USD | 0.00 USD | `+31.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.28` | 6,750,000.00 USD | 589.22 USD | 0.00 USD | `+32.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.29` | 6,750,000.00 USD | 733.03 USD | 0.00 USD | `+32.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.29` | 6,750,000.00 USD | 423.60 USD | 0.00 USD | `+32.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.30` | 6,770,000.00 USD | 10,930.00 USD | 0.00 USD | `+32.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.32` | 6,770,000.00 USD | 381.09 USD | 0.00 USD | `+33.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.33` | 6,770,000.00 USD | 961.16 USD | 0.00 USD | `+33.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.33` | 6,770,000.00 USD | 1,570.00 USD | 0.00 USD | `+33.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.34` | 6,770,000.00 USD | 5,650.00 USD | 0.00 USD | `+33.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.36` | 6,770,000.00 USD | 160.11 USD | 0.00 USD | `+34.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.37` | 6,770,000.00 USD | 225.33 USD | 0.00 USD | `+34.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.38` | 6,780,000.00 USD | 438.60 USD | 0.00 USD | `+34.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.38` | 6,780,000.00 USD | 4,840.00 USD | 0.00 USD | `+34.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.39` | 6,820,000.00 USD | 40,880.00 USD | 0.00 USD | `+35.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.41` | 6,840,000.00 USD | 17,160.00 USD | 0.00 USD | `+35.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.42` | 6,840,000.00 USD | 270.75 USD | 0.00 USD | `+35.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.42` | 6,840,000.00 USD | 639.61 USD | 0.00 USD | `+35.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.45` | 6,850,000.00 USD | 12,600.00 USD | 0.00 USD | `+36.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.46` | 6,860,000.00 USD | 3,650.00 USD | 0.00 USD | `+36.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.46` | 7,050,000.00 USD | 192,640.00 USD | 0.00 USD | `+36.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.47` | 7,080,000.00 USD | 30,110.00 USD | 0.00 USD | `+37.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.49` | 7,120,000.00 USD | 38,920.00 USD | 0.00 USD | `+37.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.50` | 7,120,000.00 USD | 1,180.00 USD | 0.00 USD | `+37.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.50` | 7,180,000.00 USD | 62,490.00 USD | 0.00 USD | `+37.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.51` | 7,190,000.00 USD | 5,600.00 USD | 0.00 USD | `+38.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.53` | 7,210,000.00 USD | 19,110.00 USD | 0.00 USD | `+38.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.54` | 7,220,000.00 USD | 18,790.00 USD | 0.00 USD | `+38.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.54` | 7,280,000.00 USD | 58,030.00 USD | 0.00 USD | `+38.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.55` | 7,330,000.00 USD | 46,450.00 USD | 0.00 USD | `+39.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.57` | 7,340,000.00 USD | 14,320.00 USD | 0.00 USD | `+39.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.58` | 7,350,000.00 USD | 10,390.00 USD | 0.00 USD | `+39.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.58` | 7,370,000.00 USD | 20,540.00 USD | 0.00 USD | `+39.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.59` | 7,370,000.00 USD | 384.94 USD | 0.00 USD | `+40.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.61` | 7,370,000.00 USD | 573.39 USD | 0.00 USD | `+40.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.62` | 7,380,000.00 USD | 2,190.00 USD | 0.00 USD | `+40.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.63` | 7,380,000.00 USD | 581.53 USD | 0.00 USD | `+41.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.64` | 7,380,000.00 USD | 491.11 USD | 0.00 USD | `+41.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.66` | 7,380,000.00 USD | 3,290.00 USD | 0.00 USD | `+41.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.67` | 7,380,000.00 USD | 281.55 USD | 0.00 USD | `+41.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.67` | 7,390,000.00 USD | 6,590.00 USD | 0.00 USD | `+42.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.68` | 7,390,000.00 USD | 235.93 USD | 0.00 USD | `+42.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.70` | 7,390,000.00 USD | 5,860.00 USD | 0.00 USD | `+42.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.71` | 7,500,000.00 USD | 103,470.00 USD | 0.00 USD | `+42.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.71` | 7,500,000.00 USD | 705.23 USD | 0.00 USD | `+43.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.72` | 7,500,000.00 USD | 5,720.00 USD | 0.00 USD | `+43.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.75` | 7,500,000.00 USD | 139.03 USD | 0.00 USD | `+43.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.75` | 7,510,000.00 USD | 2,610.00 USD | 0.00 USD | `+44.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.76` | 7,510,000.00 USD | 2,430.00 USD | 0.00 USD | `+44.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.78` | 7,510,000.00 USD | 1,850.00 USD | 0.00 USD | `+44.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.79` | 7,510,000.00 USD | 286.94 USD | 0.00 USD | `+44.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.80` | 7,520,000.00 USD | 7,120.00 USD | 0.00 USD | `+45.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.82` | 7,520,000.00 USD | 329.13 USD | 0.00 USD | `+45.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.83` | 7,520,000.00 USD | 1,970.00 USD | 0.00 USD | `+45.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.83` | 7,520,000.00 USD | 1,020.00 USD | 0.00 USD | `+46.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.84` | 7,520,000.00 USD | 1,150.00 USD | 0.00 USD | `+46.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.86` | 7,520,000.00 USD | 1,190.00 USD | 0.00 USD | `+46.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.87` | 7,530,000.00 USD | 1,770.00 USD | 0.00 USD | `+46.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.88` | 7,530,000.00 USD | 3,450.00 USD | 0.00 USD | `+47.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.88` | 7,530,000.00 USD | 345.45 USD | 0.00 USD | `+47.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.91` | 7,600,000.00 USD | 65,350.00 USD | 0.00 USD | `+47.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.92` | 7,600,000.00 USD | 2,510.00 USD | 0.00 USD | `+48.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.92` | 7,600,000.00 USD | 1,020.00 USD | 0.00 USD | `+48.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.93` | 7,750,000.00 USD | 153,150.00 USD | 0.00 USD | `+48.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.96` | 7,780,000.00 USD | 26,180.00 USD | 0.00 USD | `+49.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.96` | 7,780,000.00 USD | 5,440.00 USD | 0.00 USD | `+49.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.97` | 7,790,000.00 USD | 8,940.00 USD | 0.00 USD | `+49.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.99` | 7,910,000.00 USD | 119,340.00 USD | 0.00 USD | `+49.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.00` | 7,910,000.00 USD | 3,000.00 USD | 0.00 USD | `+50.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.00` | 8,120,000.00 USD | 205,980.00 USD | 0.00 USD | `+50.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.01` | 8,130,000.00 USD | 13,710.00 USD | 0.00 USD | `+50.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.03` | 8,220,000.00 USD | 90,380.00 USD | 0.00 USD | `+50.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.04` | 8,230,000.00 USD | 2,170.00 USD | 0.00 USD | `+51.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.04` | 8,230,000.00 USD | 3,300.00 USD | 0.00 USD | `+51.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.05` | 8,230,000.00 USD | 1,040.00 USD | 0.00 USD | `+51.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.07` | 8,230,000.00 USD | 425.76 USD | 0.00 USD | `+51.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.08` | 8,230,000.00 USD | 2,030.00 USD | 0.00 USD | `+52.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.08` | 8,240,000.00 USD | 4,120.00 USD | 0.00 USD | `+52.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.09` | 8,240,000.00 USD | 2,000.00 USD | 0.00 USD | `+52.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.11` | 8,300,000.00 USD | 61,050.00 USD | 0.00 USD | `+52.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.12` | 8,300,000.00 USD | 1,610.00 USD | 0.00 USD | `+53.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.13` | 8,300,000.00 USD | 1,200.00 USD | 0.00 USD | `+53.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.14` | 8,300,000.00 USD | 420.32 USD | 0.00 USD | `+53.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.16` | 8,310,000.00 USD | 1,940.00 USD | 0.00 USD | `+54.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.17` | 8,310,000.00 USD | 1,410.00 USD | 0.00 USD | `+54.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.17` | 8,310,000.00 USD | 4,010.00 USD | 0.00 USD | `+54.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.18` | 8,320,000.00 USD | 3,960.00 USD | 0.00 USD | `+54.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.21` | 8,380,000.00 USD | 66,060.00 USD | 0.00 USD | `+55.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.21` | 8,380,000.00 USD | 1,890.00 USD | 0.00 USD | `+55.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.22` | 8,380,000.00 USD | 195.46 USD | 0.00 USD | `+55.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.24` | 8,390,000.00 USD | 1,540.00 USD | 0.00 USD | `+56.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.25` | 8,390,000.00 USD | 116.16 USD | 0.00 USD | `+56.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.28` | 8,390,000.00 USD | 3,670.00 USD | 0.00 USD | `+57.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.29` | 8,390,000.00 USD | 3,680.00 USD | 0.00 USD | `+57.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.30` | 8,400,000.00 USD | 7,310.00 USD | 0.00 USD | `+57.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.32` | 8,400,000.00 USD | 310.70 USD | 0.00 USD | `+58.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.33` | 8,400,000.00 USD | 325.62 USD | 0.00 USD | `+58.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.36` | 8,400,000.00 USD | 1,760.00 USD | 0.00 USD | `+59.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.38` | 8,410,000.00 USD | 3,560.00 USD | 0.00 USD | `+59.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.39` | 8,410,000.00 USD | 3,230.00 USD | 0.00 USD | `+60.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.41` | 8,410,000.00 USD | 5,120.00 USD | 0.00 USD | `+60.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.43` | 8,410,000.00 USD | 613.26 USD | 0.00 USD | `+61.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.50` | 8,420,000.00 USD | 1,310.00 USD | 0.00 USD | `+62.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.50` | 8,440,000.00 USD | 27,360.00 USD | 0.00 USD | `+62.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.51` | 8,440,000.00 USD | 104.24 USD | 0.00 USD | `+63.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.54` | 8,460,000.00 USD | 13,580.00 USD | 0.00 USD | `+63.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.58` | 8,460,000.00 USD | 1,630.00 USD | 0.00 USD | `+64.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.59` | 8,460,000.00 USD | 1,370.00 USD | 0.00 USD | `+65.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.61` | 8,460,000.00 USD | 562.09 USD | 0.00 USD | `+65.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.62` | 8,460,000.00 USD | 1,620.00 USD | 0.00 USD | `+65.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.64` | 8,470,000.00 USD | 3,220.00 USD | 0.00 USD | `+66.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.67` | 8,470,000.00 USD | 450.55 USD | 0.00 USD | `+66.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.67` | 8,470,000.00 USD | 3,060.00 USD | 0.00 USD | `+67.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.71` | 8,470,000.00 USD | 3,070.00 USD | 0.00 USD | `+67.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.74` | 8,480,000.00 USD | 3,120.00 USD | 0.00 USD | `+68.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.75` | 8,480,000.00 USD | 1,550.00 USD | 0.00 USD | `+68.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.78` | 8,480,000.00 USD | 3,080.00 USD | 0.00 USD | `+69.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.79` | 8,480,000.00 USD | 647.56 USD | 0.00 USD | `+70.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.80` | 8,480,000.00 USD | 1,420.00 USD | 0.00 USD | `+70.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.82` | 8,480,000.00 USD | 2,130.00 USD | 0.00 USD | `+70.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.83` | 8,490,000.00 USD | 6,870.00 USD | 0.00 USD | `+70.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.84` | 8,490,000.00 USD | 342.25 USD | 0.00 USD | `+71.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.86` | 8,490,000.00 USD | 1,830.00 USD | 0.00 USD | `+71.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.87` | 8,500,000.00 USD | 2,990.00 USD | 0.00 USD | `+71.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.89` | 8,500,000.00 USD | 2,970.00 USD | 0.00 USD | `+72.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.91` | 8,500,000.00 USD | 324.54 USD | 0.00 USD | `+72.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.95` | 8,500,000.00 USD | 504.21 USD | 0.00 USD | `+73.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.97` | 8,500,000.00 USD | 166.00 USD | 0.00 USD | `+74.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.99` | 8,500,000.00 USD | 4,190.00 USD | 0.00 USD | `+74.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.00` | 8,520,000.00 USD | 12,970.00 USD | 0.00 USD | `+75.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.01` | 8,520,000.00 USD | 1,750.00 USD | 0.00 USD | `+75.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.04` | 8,520,000.00 USD | 2,860.00 USD | 0.00 USD | `+76.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.11` | 8,520,000.00 USD | 264.31 USD | 0.00 USD | `+77.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.13` | 8,520,000.00 USD | 599.34 USD | 0.00 USD | `+78.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.16` | 8,520,000.00 USD | 193.19 USD | 0.00 USD | `+79.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.18` | 8,530,000.00 USD | 3,950.00 USD | 0.00 USD | `+79.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.21` | 8,530,000.00 USD | 1,940.00 USD | 0.00 USD | `+80.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.25` | 8,690,000.00 USD | 160,550.00 USD | 0.00 USD | `+81.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.28` | 8,690,000.00 USD | 1,290.00 USD | 0.00 USD | `+82.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.32` | 8,690,000.00 USD | 905.60 USD | 0.00 USD | `+83.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.38` | 8,700,000.00 USD | 7,870.00 USD | 0.00 USD | `+85.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.39` | 8,700,000.00 USD | 630.05 USD | 0.00 USD | `+85.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.41` | 8,700,000.00 USD | 1,410.00 USD | 0.00 USD | `+85.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.42` | 8,700,000.00 USD | 2,610.00 USD | 0.00 USD | `+85.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.50` | 8,710,000.00 USD | 6,000.00 USD | 0.00 USD | `+88.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.54` | 8,710,000.00 USD | 1,620.00 USD | 0.00 USD | `+89.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.58` | 8,720,000.00 USD | 4,640.00 USD | 0.00 USD | `+89.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.61` | 8,720,000.00 USD | 371.88 USD | 0.00 USD | `+90.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.62` | 8,720,000.00 USD | 2,510.00 USD | 0.00 USD | `+90.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.67` | 8,720,000.00 USD | 380.68 USD | 0.00 USD | `+92.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.76` | 8,720,000.00 USD | 1,490.00 USD | 0.00 USD | `+94.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.78` | 8,720,000.00 USD | 1,470.00 USD | 0.00 USD | `+94.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.79` | 8,730,000.00 USD | 11,170.00 USD | 0.00 USD | `+95.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.80` | 8,770,000.00 USD | 34,360.00 USD | 0.00 USD | `+95.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.82` | 8,770,000.00 USD | 253.21 USD | 0.00 USD | `+95.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.83` | 8,770,000.00 USD | 100.29 USD | 0.00 USD | `+96.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.88` | 8,770,000.00 USD | 1,550.00 USD | 0.00 USD | `+97.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.96` | 8,780,000.00 USD | 10,610.00 USD | 0.00 USD | `+99.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.97` | 8,780,000.00 USD | 309.43 USD | 0.00 USD | `+99.78%` | `TACTICAL (Retail Cluster)` |

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
  * Total Open Interest: `1.05B` | Total OI Tokens: `262,848,670.4 NEAR`
  * 1h OI Change: `-2.46%` | 4h OI Change: `-9.46%` | 24h OI Change: `-16.87%`
  * Exchange Breakdown: Binance=`202.14M` | Bybit=`142.42M` | OKX=`48.90M` | Hyperliquid=`225.85M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `-11.02K` | Last 24h: `59.84K` | Last 3d: `308.79K` | Last 7d: `236.18K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0033%` | **USDT OKX** | `-0.0023%` |
| **USDT Bybit** | `-0.0106%` | **USDT KuCoin** | `0.0100%` |
| **USDT MEXC** | `0.0030%` | **USDT BingX** | `0.0027%` |
| **USDT Gate** | `-0.0564%` | **USDT Bitget** | `0.0014%` |
| **CoinM Binance** | `0.0100%` | **CoinM OKX** | `-` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `NEAR` | `51.45%` | `48.55%` | `1.06` | 8,610,000.00 USD |
| `15M` | `Binance` | `52.7%` | `47.3%` | `1.11` | 2,720,000.00 USD |
| `15M` | `OKX` | `54.98%` | `45.02%` | `1.22` | 964,010.00 USD |
| `15M` | `Bybit` | `49.1%` | `50.9%` | `0.96` | 934,720.00 USD |
| `15M` | `KuCoin` | `46.73%` | `53.27%` | `0.88` | 41,850.00 USD |
| `15M` | `Gate` | `52.84%` | `47.16%` | `1.12` | 214,130.00 USD |
| `15M` | `Bitget` | `24.15%` | `75.85%` | `0.32` | 223,360.00 USD |
| `15M` | `BingX` | `50.13%` | `49.87%` | `1.01` | 1,190,000.00 USD |
| `15M` | `MEXC` | `54.64%` | `45.36%` | `1.20` | 621,480.00 USD |
| `15M` | `Bitunix` | `69.22%` | `30.78%` | `2.25` | 214,250.00 USD |
| `15M` | `Hyperliquid` | `27.15%` | `72.85%` | `0.37` | 27,850.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `55.89%` | `44.11%` | `1.27` | 1,220,000.00 USD |
| `15M` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `WhiteBIT` | `28.02%` | `71.98%` | `0.39` | 76,950.00 USD |
| `15M` | `HTX` | `12.68%` | `87.32%` | `0.15` | 103,380.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `24.13%` | `75.87%` | `0.32` | 36,850.00 USD |
| `15M` | `Aster` | `92.33%` | `7.67%` | `12.04` | 998.81 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `8.82%` | `91.18%` | `0.10` | 18,210.00 USD |
| `15M` | `Whale Positions` | `52.7%` | `47.3%` | `1.11` | 2,720,000.00 USD |
| `15M` | `Global Accounts` | `51.45%` | `48.55%` | `1.06` | 8,610,000.00 USD |
| `1H` | `NEAR` | `50.42%` | `49.58%` | `1.02` | 57,050,000.00 USD |
| `1H` | `Binance` | `52.59%` | `47.41%` | `1.11` | 22,440,000.00 USD |
| `1H` | `OKX` | `51.2%` | `48.8%` | `1.05` | 7,460,000.00 USD |
| `1H` | `Bybit` | `52.38%` | `47.62%` | `1.10` | 11,550,000.00 USD |
| `1H` | `KuCoin` | `56%` | `44%` | `1.27` | 1,040,000.00 USD |
| `1H` | `Gate` | `50.49%` | `49.51%` | `1.02` | 3,680,000.00 USD |
| `1H` | `Bitget` | `58.61%` | `41.39%` | `1.42` | 1,860,000.00 USD |
| `1H` | `BingX` | `23.73%` | `76.27%` | `0.31` | 662,260.00 USD |
| `1H` | `MEXC` | `51.18%` | `48.82%` | `1.05` | 958,680.00 USD |
| `1H` | `Bitunix` | `46.16%` | `53.84%` | `0.86` | 722,540.00 USD |
| `1H` | `Hyperliquid` | `60.93%` | `39.07%` | `1.56` | 2,180,000.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `51.35%` | `48.65%` | `1.06` | 810,760.00 USD |
| `1H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `WhiteBIT` | `12.47%` | `87.53%` | `0.14` | 2,400,000.00 USD |
| `1H` | `HTX` | `58.81%` | `41.19%` | `1.43` | 139,990.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `32.62%` | `67.38%` | `0.48` | 901,410.00 USD |
| `1H` | `Aster` | `46.12%` | `53.88%` | `0.86` | 93,340.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `75.76%` | `24.24%` | `3.13` | 155,950.00 USD |
| `1H` | `Whale Positions` | `52.59%` | `47.41%` | `1.11` | 22,440,000.00 USD |
| `1H` | `Global Accounts` | `50.42%` | `49.58%` | `1.02` | 57,050,000.00 USD |
| `4H` | `NEAR` | `49.97%` | `50.03%` | `1.00` | 264,750,000.00 USD |
| `4H` | `Binance` | `49.95%` | `50.05%` | `1.00` | 93,740,000.00 USD |
| `4H` | `OKX` | `49.33%` | `50.67%` | `0.97` | 24,150,000.00 USD |
| `4H` | `Bybit` | `47.72%` | `52.28%` | `0.91` | 32,750,000.00 USD |
| `4H` | `KuCoin` | `46.39%` | `53.61%` | `0.87` | 2,160,000.00 USD |
| `4H` | `Gate` | `56.55%` | `43.45%` | `1.30` | 11,850,000.00 USD |
| `4H` | `Bitget` | `46.64%` | `53.36%` | `0.87` | 12,240,000.00 USD |
| `4H` | `BingX` | `47.99%` | `52.01%` | `0.92` | 9,100,000.00 USD |
| `4H` | `MEXC` | `50.18%` | `49.82%` | `1.01` | 17,560,000.00 USD |
| `4H` | `Bitunix` | `46.72%` | `53.28%` | `0.88` | 6,440,000.00 USD |
| `4H` | `Hyperliquid` | `47.45%` | `52.55%` | `0.90` | 4,370,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `51.2%` | `48.8%` | `1.05` | 45,310,000.00 USD |
| `4H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `WhiteBIT` | `73.23%` | `26.77%` | `2.74` | 2,020,000.00 USD |
| `4H` | `HTX` | `52.5%` | `47.5%` | `1.11` | 842,500.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `54.15%` | `45.85%` | `1.18` | 1,740,000.00 USD |
| `4H` | `Aster` | `45.79%` | `54.21%` | `0.84` | 348,500.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `23.74%` | `76.26%` | `0.31` | 143,730.00 USD |
| `4H` | `Whale Positions` | `49.95%` | `50.05%` | `1.00` | 93,740,000.00 USD |
| `4H` | `Global Accounts` | `49.97%` | `50.03%` | `1.00` | 264,750,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `0:00 UTC` | `4.10` | `4.09` | `4.10` | `4.11` | `4.06` | 8,071,698.41 USD | 3,807,805.84 USD | 4,263,892.57 USD | -456,086.73 USD | `-5.65%` | `1B / 6S` |
| `5:00 UTC` | `4.06` | `4.06` | `4.06` | `4.08` | `4.04` | 13,393,607.00 USD | 6,718,844.40 USD | 6,674,762.60 USD | 44,081.81 USD | `+0.33%` | `2B / 2S` |
| `0:00 UTC` | `4.06` | `4.05` | `4.06` | `4.08` | `4.02` | 16,647,053.78 USD | 8,059,551.61 USD | 8,587,502.18 USD | -527,950.57 USD | `-3.17%` | `5B / 5S` |
| `5:00 UTC` | `3.98` | `3.99` | `3.98` | `4.05` | `3.92` | 44,923,279.18 USD | 19,438,062.87 USD | 25,485,216.31 USD | -6,047,153.45 USD | `-13.46%` | `4B / 18S` |
| `0:00 UTC` | `3.96` | `3.94` | `3.96` | `3.98` | `3.91` | 23,036,432.35 USD | 10,793,071.74 USD | 12,243,360.61 USD | -1,450,288.88 USD | `-6.30%` | `4B / 6S` |
| `5:00 UTC` | `4.00` | `3.99` | `4.00` | `4.02` | `3.95` | 14,908,541.20 USD | 8,081,809.07 USD | 6,826,732.13 USD | 1,255,076.95 USD | `+8.42%` | `5B / 3S` |
| `0:00 UTC` | `3.99` | `4.00` | `3.99` | `4.04` | `3.98` | 10,043,819.37 USD | 5,055,045.74 USD | 4,988,773.63 USD | 66,272.12 USD | `+0.66%` | `10B / 0S` |
| `5:00 UTC` | `4.00` | `4.00` | `4.00` | `4.04` | `3.99` | 5,936,404.63 USD | 2,860,550.97 USD | 3,075,853.66 USD | -215,302.69 USD | `-3.63%` | `6B / 8S` |
| `0:00 UTC` | `4.02` | `4.00` | `4.02` | `4.03` | `3.95` | 11,016,623.88 USD | 5,505,508.67 USD | 5,511,115.21 USD | -5,606.55 USD | `-0.05%` | `3B / 8S` |
| `5:00 UTC` | `3.99` | `3.99` | `3.99` | `4.01` | `3.97` | 5,000,226.83 USD | 1,928,953.18 USD | 3,071,273.65 USD | -1,142,320.48 USD | `-22.85%` | `3B / 12S` |

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
| `5m` | -61,370.00 USD | -1,150,000.00 USD | **`DISTRIBUTION`** |
| `15m` | -1,170,000.00 USD | -1,810,000.00 USD | **`DISTRIBUTION`** |
| `30m` | -1,430,000.00 USD | -1,090,000.00 USD | **`DISTRIBUTION`** |
| `1h` | -365,750.00 USD | -1,020,000.00 USD | **`DISTRIBUTION`** |
| `2h` | -2,070,000.00 USD | -13,840,000.00 USD | **`DISTRIBUTION`** |
| `4h` | -7,060,000.00 USD | -21,330,000.00 USD | **`DISTRIBUTION`** |
| `6h` | -13,480,000.00 USD | -35,760,000.00 USD | **`DISTRIBUTION`** |
| `8h` | -15,890,000.00 USD | -39,820,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -18,180,000.00 USD | -42,610,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -25,040,000.00 USD | -71,670,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -83,360,000.00 USD | -143,360,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -252,660,000.00 USD | -697,980,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-61.37K` | 15m=`-1.17M` | 1h=`-365.75K` | 24h=`-25.04M`
* Futures Capital Netflows: 5m=`-1.15M` | 15m=`-1.81M` | 1h=`-1.02M` | 24h=`-71.67M`
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
  * `2026-10-30 05:01:10 IST`: [media.rabobank.com] - (Sentiment: `Neutral`)
  * `2026-10-30 04:15:10 IST`: [economics.td.com] - (Sentiment: `Neutral`)
  * `2026-10-30 05:01:10 IST`: [investinglive.com] - (Sentiment: `Neutral`)
  * `2026-10-30 05:00:10 IST`: [msn.com] - (Sentiment: `Neutral`)
  * `2026-10-30 05:00:10 IST`: [morningstar.com] - (Sentiment: `Neutral`)
  * `2026-10-30 02:02:10 IST`: [sec.gov] - (Sentiment: `Neutral`)
  * `2026-10-30 01:02:10 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 01:02:10 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 01:02:10 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 00:02:10 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 00:02:10 IST`: [@DeItaone] - (Sentiment: `Neutral`)
  * `2026-10-30 00:02:10 IST`: [@mb_ghalibaf] - (Sentiment: `Neutral`)
  * `2026-10-29 23:02:10 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-29 23:02:10 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-29 23:02:10 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)


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
  * Execution Entry: `3.97` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `3.84` (Risk Distance: `0.1246` pts)
  * +2.5R Take Profit: `4.28`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `4.15` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `4.27` (Risk Distance: `0.1246` pts)
  * +2.5R Take Profit: `3.84`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`4.01`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
