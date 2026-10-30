# 🏛️ SOVEREIGN CANDIDATE DOSSIER: NEAR
**Canonical Key**: `NEAR` | **Broker Instrument**: `NERUSD.p` | **Asset Class**: `Crypto Alt L1`
**Timestamp**: `2026-10-30 14:38:47 IST` (`2026-10-30 09:08:47 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `4.34` | **Live Ask Quote**: `4.37` | **Mid Price**: `4.35`
- **Spread Points**: `30.00` | **Spread BPS**: `68.92 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `4.12` | VWAP Z-Score: `+1.66` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `0.0571` (Volatility Regime: `HIGH_EXPANSION`)
  * 14-Period RSI: `62.53` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `4.52` | Lower -3.00σ Band: `3.71`
  * Upper +2.51σ Band: `4.45` | Lower -2.51σ Band: `3.78`
  * Upper +2.01σ Band: `4.39` | Lower -2.01σ Band: `3.85`
  * Upper +2.00σ Band: `4.38` | Lower -2.00σ Band: `3.85`
  * Upper +1.28σ Band: `4.29` | Lower -1.28σ Band: `3.94`
  * Upper +1.00σ Band: `4.25` | Lower -1.00σ Band: `3.98`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`4.29` | EMA-20=`4.25` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`4.23` (Slope: `+0.0000`) | EMA-100=`4.28`
  * Institutional Anchors: EMA-144=`4.33` | EMA-200=`4.38` (Slope: `-0.2815`) | EMA-233=`4.41`
- **Range Boundaries**: 24H High=`4.67` | 24H Low=`3.89` | Weekly High=`4.80` | Weekly Low=`3.89`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `4.21` (Distance: `+3.69%`)
  * Point of Control (POC) = `4.07` (Distance: `+7.23%`)
  * Value Area Low (VAL) = `3.94` (Distance: `+10.74%`)
  * Auction Positioning: `ABOVE_VALUE (Imbalance)` | Session Bias: **`BULLISH (Above Pivot)`** | Market Regime: `RANGE_EXPANSION`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`4.57` | POC=`4.41` | VAL=`4.29`
  * Prior Day Extremes: PDH=`4.75` | PDL=`4.08` | PDC=`4.15`
  * Monday Range Blueprint: High=`4.65` | Mid=`4.53` | Low=`4.41`
  * Developing Weekly Value Area: Weekly VAH=`4.70` | Weekly POC=`4.45` | Weekly VAL=`4.39`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`4.26` | Low=`3.89`
  * London Session (08:00-16:00 UTC): High=`4.37` | Low=`4.15`
  * New York Session (13:00-21:00 UTC): High=`4.38` | Low=`4.33`
  * Initial Balance (First Hour): IB High=`4.27` | IB Low=`4.17`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `4.34` - `4.37`
  * Optimal Trade Entry (OTE 0.705): `4.36`
  * Structural Invalidation Anchor (0.786): `4.39`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `4.32` | `4.39` | `4.31` | `4.39` | `1,296,383` | 5,655,850.18 USD | 2,272,317.44 USD | `+40.18%` | -5,835,459.72 USD | `+1.16` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `5m` | `4.39` | `4.39` | `4.35` | `4.36` | `880,853` | 3,844,054.35 USD | -937,677.71 USD | `-24.39%` | -6,773,137.44 USD | `-0.83` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `5m` | `4.36` | `4.36` | `4.34` | `4.35` | `143,864` | 626,132.14 USD | 49,328.11 USD | `+7.88%` | -6,723,809.32 USD | `-0.23` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `15m` | `4.34` | `4.35` | `4.31` | `4.31` | `1,976,133` | 8,553,382.74 USD | -1,240,920.31 USD | `-14.51%` | -8,610,200.49 USD | `-0.62` | **`BEARISH`** | `DELTA ALIGNED` |
| `15m` | `4.31` | `4.39` | `4.31` | `4.36` | `2,658,657` | 11,576,553.35 USD | 1,092,257.28 USD | `+9.44%` | -7,517,943.21 USD | `+0.32` | **`BULLISH`** | `DELTA ALIGNED` |
| `15m` | `4.36` | `4.36` | `4.34` | `4.36` | `149,116` | 649,002.06 USD | 72,180.62 USD | `+11.12%` | -7,445,762.60 USD | `-0.10` | **`BULLISH`** | `DELTA ALIGNED` |
| `1h` | `4.34` | `4.34` | `4.21` | `4.25` | `9,473,664` | 40,439,071.22 USD | -3,673,419.57 USD | `-9.08%` | -15,883,385.93 USD | `-0.74` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `4.25` | `4.39` | `4.24` | `4.36` | `15,226,975` | 65,865,283.41 USD | 8,809,838.63 USD | `+13.38%` | -7,073,547.30 USD | `+2.04` | **`BULLISH`** | `DELTA ALIGNED` |
| `1h` | `4.36` | `4.36` | `4.34` | `4.35` | `143,864` | 626,132.14 USD | 49,328.11 USD | `+7.88%` | -7,024,219.19 USD | `+0.06` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `4.06` | `4.17` | `3.90` | `4.16` | `46,830,819` | 188,194,075.16 USD | -412,364.95 USD | `-0.22%` | -12,215,320.93 USD | `+0.44` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `4.16` | `4.36` | `4.12` | `4.25` | `33,821,215` | 143,651,581.49 USD | -2,835,728.00 USD | `-1.97%` | -15,051,048.93 USD | `+0.03` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `4.25` | `4.39` | `4.24` | `4.36` | `15,373,922` | 66,504,839.47 USD | 8,872,590.67 USD | `+13.34%` | -6,178,458.26 USD | `+1.50` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `4.65` | `4.69` | `4.38` | `4.40` | `28,351,581` | 128,263,626.10 USD | -4,168,943.82 USD | `-3.25%` | 240,083.28 USD | `-1.00` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `4.40` | `4.41` | `4.04` | `4.06` | `71,964,012` | 300,508,235.77 USD | -12,043,039.27 USD | `-4.01%` | -11,802,955.99 USD | `-1.21` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `4.06` | `4.17` | `3.90` | `4.16` | `46,830,819` | 188,194,075.16 USD | -412,364.95 USD | `-0.22%` | -12,215,320.93 USD | `+0.44` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `4.16` | `4.36` | `4.12` | `4.25` | `33,821,215` | 143,651,581.49 USD | -2,835,728.00 USD | `-1.97%` | -15,051,048.93 USD | `+0.03` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `4.25` | `4.39` | `4.24` | `4.36` | `15,373,922` | 66,504,839.47 USD | 8,872,590.67 USD | `+13.34%` | -6,178,458.26 USD | `+1.50` | **`BULLISH`** | `DELTA ALIGNED` |

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
| --- | **`4.35`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `MID` | Regular L2 Book | - | - | - | Interbank L2 | 0.00% | Interbank |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 14:32:27 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `52` | `0x7737...bf66` | `LONG` | 24,554,814.18 USD | `5,640,376.30` | `2.35` | `4.36` | `0.8392` | 11,282,911.36 USD | `+45.95%` | `10X Cross` |
| `92` | `0xefe4...194b` | `SHORT` | 19,659,326.85 USD | `4,507,262.50` | `4.21` | `4.36` | `6.57` | -684,230.13 USD | `-3.48%` | `5X Cross` |
| `124` | `0xb581...6f4f` | `LONG` | 15,705,072.00 USD | `3,600,000.00` | `5.19` | `4.36` | `0.000000` | -2,987,963.22 USD | `-19.03%` | `4X Cross` |
| `205` | `0xdd53...2b13` | `SHORT` | 10,476,833.73 USD | `2,400,202.00` | `2.31` | `4.36` | `28.85` | -4,930,985.17 USD | `-47.07%` | `3X Cross` |
| `253` | `0x77ee...2902` | `LONG` | 8,985,290.81 USD | `2,063,023.10` | `1.93` | `4.36` | `0.000000` | 4,994,094.88 USD | `+55.58%` | `10X Cross` |
| `352` | `0x9df2...c665` | `SHORT` | 6,607,456.91 USD | `1,514,579.00` | `2.36` | `4.36` | `24.15` | -3,027,467.24 USD | `-45.82%` | `10X Cross` |
| `368` | `0xb83d...6e36` | `SHORT` | 6,305,967.47 USD | `1,445,759.10` | `5.19` | `4.36` | `89.79` | 1,203,481.48 USD | `+19.08%` | `3X Cross` |
| `369` | `0x7fda...17d1` | `SHORT` | 6,297,058.14 USD | `1,443,915.10` | `4.28` | `4.36` | `29.70` | -114,979.62 USD | `-1.83%` | `10X Cross` |
| `392` | `0xb46b...538e` | `SHORT` | 5,831,613.28 USD | `1,336,000.00` | `4.33` | `4.36` | `7.45` | -46,749.22 USD | `-0.80%` | `10X Cross` |
| `452` | `0x60b0...991e` | `LONG` | 4,878,919.32 USD | `1,121,307.10` | `5.00` | `4.36` | `0.000000` | -722,505.11 USD | `-14.81%` | `10X Cross` |
| `475` | `0xcac1...26b3` | `SHORT` | 4,682,704.52 USD | `1,073,743.90` | `2.48` | `4.36` | `12.20` | -2,022,761.06 USD | `-43.20%` | `10X Cross` |
| `493` | `0x781e...96b7` | `SHORT` | 4,537,458.24 USD | `1,039,604.60` | `2.45` | `4.36` | `7.51` | -1,993,121.05 USD | `-43.93%` | `10X Cross` |
| `570` | `0x45d2...4029` | `SHORT` | 3,969,167.24 USD | `909,400.00` | `3.26` | `4.36` | `49.10` | -1,003,017.34 USD | `-25.27%` | `10X Cross` |
| `582` | `0x4cae...7c34` | `LONG` | 3,925,750.54 USD | `900,587.40` | `3.97` | `4.36` | `3.10` | 347,557.75 USD | `+8.85%` | `10X Cross` |
| `807` | `0x005a...61fe` | `LONG` | 2,848,246.42 USD | `652,414.60` | `2.08` | `4.36` | `2.42` | 1,490,715.18 USD | `+52.34%` | `7X Cross` |
| `814` | `0xba5d...a352` | `SHORT` | 2,824,873.48 USD | `647,532.50` | `2.83` | `4.36` | `11.63` | -992,158.54 USD | `-35.12%` | `10X Cross` |
| `821` | `0xb695...a92d` | `SHORT` | 2,788,136.91 USD | `639,231.70` | `4.57` | `4.36` | `38.44` | 135,222.02 USD | `+4.85%` | `10X Cross` |
| `826` | `0xd1dd...9e85` | `SHORT` | 2,777,094.50 USD | `637,621.00` | `4.96` | `4.36` | `18.33` | 386,378.23 USD | `+13.91%` | `10X Cross` |
| `840` | `0x123d...3bff` | `SHORT` | 2,723,803.94 USD | `624,568.10` | `2.09` | `4.36` | `9.18` | -1,418,379.76 USD | `-52.07%` | `10X Cross` |
| `845` | `0xcf53...ee11` | `SHORT` | 2,712,406.78 USD | `621,598.40` | `5.07` | `4.36` | `25.23` | 439,763.47 USD | `+16.21%` | `10X Cross` |
| `971` | `0xbfc7...80b4` | `SHORT` | 2,311,974.00 USD | `531,000.00` | `2.01` | `4.36` | `7.18` | -1,246,774.61 USD | `-53.93%` | `10X Cross` |
| `1221` | `0x0eec...d4c5` | `LONG` | 1,821,462.06 USD | `417,603.70` | `4.01` | `4.36` | `1.99` | 146,944.43 USD | `+8.07%` | `10X Cross` |
| `1274` | `0xe097...d0fe` | `LONG` | 1,745,440.00 USD | `400,000.00` | `5.29` | `4.36` | `0.000000` | -371,347.30 USD | `-21.28%` | `10X Cross` |
| `1369` | `0x6e8f...4364` | `LONG` | 1,577,659.10 USD | `361,210.50` | `3.28` | `4.36` | `3.57` | 393,598.87 USD | `+24.95%` | `10X Cross` |
| `1377` | `0xef96...9383` | `SHORT` | 1,573,024.86 USD | `360,644.90` | `4.50` | `4.36` | `13.90` | 50,082.49 USD | `+3.18%` | `10X Cross` |
| `1435` | `0xdf95...7d72` | `SHORT` | 1,527,765.68 USD | `350,268.40` | `4.23` | `4.36` | `110.62` | -45,319.84 USD | `-2.97%` | `10X Cross` |
| `1437` | `0xcf67...eb24` | `LONG` | 1,526,595.00 USD | `350,000.00` | `1.98` | `4.36` | `1.63` | 834,977.12 USD | `+54.70%` | `10X Cross` |
| `1550` | `0xfc27...9d9d` | `SHORT` | 1,396,661.96 USD | `319,997.70` | `5.01` | `4.36` | `60.88` | 206,880.66 USD | `+14.81%` | `10X Cross` |
| `1552` | `0x089f...a4f8` | `LONG` | 1,392,847.33 USD | `319,043.30` | `4.06` | `4.36` | `0.000000` | 97,990.62 USD | `+7.04%` | `1X Cross` |
| `1607` | `0x17c3...a868` | `LONG` | 1,336,533.59 USD | `306,291.50` | `4.36` | `4.36` | `0.000000` | 272.48 USD | `+0.02%` | `3X Cross` |
| `1693` | `0xe065...0f85` | `SHORT` | 1,253,897.78 USD | `288,027.90` | `2.81` | `4.36` | `5.66` | -443,344.66 USD | `-35.36%` | `10X Cross` |
| `1879` | `0x2577...4897` | `LONG` | 1,094,568.61 USD | `250,950.00` | `4.26` | `4.36` | `0.000000` | 25,469.83 USD | `+2.33%` | `10X Cross` |
| `1885` | `0xff43...d924` | `LONG` | 1,088,337.50 USD | `249,474.50` | `4.64` | `4.36` | `3.28` | -69,706.18 USD | `-6.40%` | `10X Isolated` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `4.30` | 9,828.61 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Liquidated Short: 9.83K USD at 4.3040 USD [API] | `2026-10-29 06:47:16` |
| `ANNOUNCEMENT` | `INFO` | `4.39` | 17,972.86 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Whale SELL: 17.97K USD at 4.3908 USD [API] | `2026-10-29 10:37:17` |
| `ANNOUNCEMENT` | `INFO` | `4.28` | 29,976.98 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Liquidated Short: 29.98K USD at 4.2842 USD [API] | `2026-10-29 07:17:49` |
| `ANNOUNCEMENT` | `INFO` | `4.29` | 27,237.35 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Liquidated Short: 27.24K USD at 4.2855 USD [API] | `2026-10-29 07:17:49` |
| `ANNOUNCEMENT` | `INFO` | `4.29` | 8,702.99 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Liquidated Short: 8.70K USD at 4.2855 USD [API] | `2026-10-29 07:17:49` |
| `ANNOUNCEMENT` | `INFO` | `4.30` | 8,954.84 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Liquidated Short: 8.95K USD at 4.3048 USD [API] | `2026-10-29 06:47:22` |
| `ANNOUNCEMENT` | `INFO` | `4.30` | 13,001.43 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Liquidated Short: 13.00K USD at 4.3034 USD [API] | `2026-10-29 06:47:19` |
| `ANNOUNCEMENT` | `INFO` | `4.40` | 8,303.74 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Whale BUY: 8.30K USD at 4.4026 USD [API] | `2026-10-29 10:38:18` |
| `ANNOUNCEMENT` | `INFO` | `4.42` | 5,300.98 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Whale BUY: 5.30K USD at 4.4208 USD [API] | `2026-10-29 11:21:54` |
| `ANNOUNCEMENT` | `INFO` | `4.42` | 44,540.74 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Whale BUY: 44.54K USD at 4.4232 USD [API] | `2026-10-29 11:46:57` |
| `ANNOUNCEMENT` | `INFO` | `4.40` | 10,050.12 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Whale BUY: 10.05K USD at 4.4010 USD [API] | `2026-10-29 12:09:30` |
| `ANNOUNCEMENT` | `INFO` | `4.44` | 9,012.52 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Whale BUY: 9.01K USD at 4.4447 USD [API] | `2026-10-29 12:42:38` |
| `ANNOUNCEMENT` | `INFO` | `4.52` | 10.84 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Liquidated Long: 0.01K USD at 4.5165 USD [API] | `2026-10-29 13:17:08` |
| `ANNOUNCEMENT` | `INFO` | `4.47` | 5,384.77 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Whale SELL: 5.38K USD at 4.4724 USD [API] | `2026-10-29 13:23:50` |
| `ANNOUNCEMENT` | `INFO` | `4.44` | 5,669.53 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Whale SELL: 5.67K USD at 4.4366 USD [API] | `2026-10-29 13:34:47` |
| `ANNOUNCEMENT` | `INFO` | `4.56` | 237.36 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Liquidated Long: 0.24K USD at 4.5647 USD [API] | `2026-10-15 10:22:09` |
| `ANNOUNCEMENT` | `INFO` | `4.69` | 665.94 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Liquidated Long: 0.67K USD at 4.6864 USD [API] | `2026-10-02 18:08:41` |
| `ANNOUNCEMENT` | `INFO` | `4.44` | 7,080.12 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Whale BUY: 7.08K USD at 4.4448 USD [API] | `2026-10-29 13:56:45` |
| `ANNOUNCEMENT` | `INFO` | `4.44` | 10,056.32 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Whale BUY: 10.06K USD at 4.4438 USD [API] | `2026-10-29 14:09:11` |
| `ANNOUNCEMENT` | `INFO` | `4.44` | 5,685.75 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Whale SELL: 5.69K USD at 4.4413 USD [API] | `2026-10-29 14:14:37` |
| `ANNOUNCEMENT` | `INFO` | `4.59` | 7,741.31 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Whale BUY: 7.74K USD at 4.5888 USD [API] | `2026-10-29 17:02:52` |
| `ANNOUNCEMENT` | `INFO` | `4.58` | 5,821.25 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Whale BUY: 5.82K USD at 4.5815 USD [API] | `2026-10-29 17:14:21` |
| `ANNOUNCEMENT` | `INFO` | `4.69` | 3,685.86 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Liquidated Long: 3.69K USD at 4.6876 USD [API] | `2026-10-18 14:31:48` |
| `ANNOUNCEMENT` | `INFO` | `5.06` | 661.89 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Liquidated Long: 0.66K USD at 5.0603 USD [API] | `2026-10-13 11:02:34` |
| `ANNOUNCEMENT` | `INFO` | `5.06` | 499.96 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Liquidated Long: 0.50K USD at 5.0603 USD [API] | `2026-10-13 11:02:34` |
| `ANNOUNCEMENT` | `INFO` | `5.06` | 10.63 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Liquidated Long: 0.01K USD at 5.0604 USD [API] | `2026-10-13 11:02:34` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`4.42` (Vol: 795,900.00 USD, Dist: `+2.37%`) | Long MP=`4.18` (Vol: 505,600.00 USD, Dist: `--3.15%`)
  * 48H Horizon: Short MP=`4.41` (Vol: 795,900.00 USD, Dist: `+2.28%`) | Long MP=`4.18` (Vol: 505,600.00 USD, Dist: `--3.15%`)
  * 3D Horizon: Short MP=`4.41` (Vol: 795,900.00 USD, Dist: `+2.28%`) | Long MP=`4.18` (Vol: 505,600.00 USD, Dist: `--3.15%`)
  * 7D Horizon: Short MP=`5.03` (Vol: 833,800.00 USD, Dist: `+16.46%`) | Long MP=`4.18` (Vol: 505,600.00 USD, Dist: `--3.08%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long Liquidation` | `0.8950` | 38,570.00 USD | 22,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9050` | 2,100.00 USD | 22,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9150` | 11,370.00 USD | 22,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9250` | 2,440.00 USD | 22,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9350` | 935.00 USD | 22,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9650` | 3,890.00 USD | 22,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9850` | 3,450.00 USD | 22,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9950` | 155,480.00 USD | 22,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.00` | 108.04 USD | 22,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.02` | 41,860.00 USD | 22,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.03` | 5,070.00 USD | 22,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.04` | 9,010.00 USD | 22,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.05` | 19,930.00 USD | 22,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.06` | 2,550.00 USD | 22,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.07` | 5,310.00 USD | 22,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.08` | 216.89 USD | 22,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.11` | 557.50 USD | 22,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.12` | 479,050.00 USD | 22,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.14` | 4,960.00 USD | 22,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.15` | 27,770.00 USD | 22,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.16` | 3,070.00 USD | 22,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.17` | 144.69 USD | 22,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.18` | 647.54 USD | 22,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.19` | 37,440.00 USD | 22,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.22` | 363.28 USD | 22,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.23` | 274,360.00 USD | 22,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.25` | 138.32 USD | 21,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.25` | 16,280.00 USD | 21,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.26` | 7,400.00 USD | 21,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.27` | 2,390.00 USD | 21,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.28` | 1,340.00 USD | 21,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.29` | 997.28 USD | 21,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.30` | 60,910.00 USD | 21,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.31` | 65,900.00 USD | 21,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.32` | 11,520.00 USD | 21,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.33` | 794.59 USD | 21,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.34` | 3,470.00 USD | 21,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.35` | 2,120.00 USD | 21,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.39` | 39,430.00 USD | 21,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.40` | 931.86 USD | 21,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.41` | 665.13 USD | 21,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.42` | 5,120.00 USD | 21,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.43` | 2,420.00 USD | 21,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.44` | 810.20 USD | 21,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.45` | 1,640.00 USD | 21,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.46` | 81,340.00 USD | 21,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.47` | 13,180.00 USD | 21,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.48` | 4,570.00 USD | 21,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.50` | 788.61 USD | 21,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.50` | 1,810.00 USD | 21,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.51` | 454.50 USD | 21,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.52` | 3,050.00 USD | 21,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.53` | 4,750.00 USD | 21,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.56` | 20,570.00 USD | 21,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.57` | 589.52 USD | 21,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.58` | 5,150.00 USD | 21,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.59` | 3,700.00 USD | 21,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.60` | 562,450.00 USD | 21,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.61` | 242.25 USD | 20,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.64` | 2,030.00 USD | 20,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.65` | 2,390.00 USD | 20,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.66` | 2,860.00 USD | 20,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.67` | 6,840.00 USD | 20,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.68` | 2,440.00 USD | 20,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.69` | 12,850.00 USD | 20,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.71` | 7,410.00 USD | 20,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.73` | 5,850.00 USD | 20,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.74` | 347.00 USD | 20,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.75` | 13,520.00 USD | 20,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.75` | 10,250.00 USD | 20,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.77` | 3,920.00 USD | 20,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.79` | 1,970.00 USD | 20,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.80` | 529.05 USD | 20,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.81` | 1,580.00 USD | 20,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.83` | 42,180.00 USD | 20,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.85` | 984.26 USD | 20,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.89` | 567,380.00 USD | 20,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.90` | 37,060.00 USD | 20,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.91` | 288.61 USD | 20,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.92` | 3,000.00 USD | 20,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.93` | 34,510.00 USD | 20,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.95` | 2,740.00 USD | 20,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.96` | 775.55 USD | 20,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.97` | 15,710.00 USD | 20,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.98` | 35,130.00 USD | 20,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.99` | 177.46 USD | 20,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.00` | 102.34 USD | 20,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.02` | 2,680.00 USD | 20,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.02` | 2,700.00 USD | 20,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.04` | 2,400.00 USD | 20,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.04` | 5,960.00 USD | 20,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.06` | 8,290.00 USD | 20,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.08` | 21,830.00 USD | 20,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.08` | 33,800.00 USD | 20,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.10` | 1,100.00 USD | 20,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.10` | 7,620.00 USD | 20,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.12` | 11,690.00 USD | 20,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.12` | 5,370.00 USD | 20,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.13` | 7,480.00 USD | 20,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.15` | 92,530.00 USD | 20,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.15` | 857.04 USD | 19,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.17` | 271,220.00 USD | 19,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.17` | 439.57 USD | 19,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.19` | 3,570.00 USD | 19,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.19` | 12,830.00 USD | 19,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.21` | 251,430.00 USD | 19,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.21` | 2,790.00 USD | 19,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.23` | 2,710.00 USD | 19,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.23` | 2,450.00 USD | 19,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.25` | 65,420.00 USD | 19,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.25` | 116,480.00 USD | 19,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.27` | 1,390.00 USD | 19,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.27` | 379,690.00 USD | 19,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.29` | 3,110.00 USD | 18,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.29` | 2,150.00 USD | 18,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.31` | 11,600.00 USD | 18,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.31` | 2,640.00 USD | 18,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.33` | 2,260.00 USD | 18,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.33` | 4,910.00 USD | 18,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.35` | 5,100.00 USD | 18,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.35` | 25,910.00 USD | 18,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.37` | 1,580.00 USD | 18,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.38` | 153,930.00 USD | 18,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.38` | 16,980.00 USD | 18,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.40` | 570.49 USD | 18,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.40` | 1,570,000.00 USD | 18,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.42` | 429,790.00 USD | 17,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.42` | 279,710.00 USD | 16,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.44` | 42,870.00 USD | 16,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.44` | 3,830.00 USD | 16,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.46` | 1,700.00 USD | 16,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.46` | 5,740.00 USD | 16,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.48` | 3,760.00 USD | 16,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.48` | 2,760.00 USD | 16,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.50` | 13,290.00 USD | 16,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.50` | 6,000.00 USD | 16,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.52` | 752.99 USD | 16,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.52` | 39,960.00 USD | 16,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.54` | 395.71 USD | 16,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.54` | 105.36 USD | 16,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.56` | 1,080.00 USD | 16,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.56` | 7,890.00 USD | 16,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.58` | 1,570.00 USD | 16,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.58` | 4,330.00 USD | 16,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.60` | 82,690.00 USD | 16,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.60` | 2,330.00 USD | 16,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.62` | 5,150.00 USD | 16,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.63` | 24,310.00 USD | 16,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.65` | 2,650.00 USD | 16,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.65` | 183,640.00 USD | 16,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.67` | 1,920.00 USD | 15,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.67` | 4,470.00 USD | 15,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.69` | 4,860.00 USD | 15,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.69` | 733.85 USD | 15,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.71` | 164,840.00 USD | 15,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.71` | 11,750.00 USD | 15,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.73` | 28,380.00 USD | 15,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.73` | 3,760.00 USD | 15,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.75` | 45,290.00 USD | 15,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.75` | 33,840.00 USD | 15,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.77` | 353,860.00 USD | 15,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.77` | 398.77 USD | 15,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.79` | 57,290.00 USD | 15,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.79` | 12,340.00 USD | 15,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.81` | 95,500.00 USD | 15,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.81` | 14,950.00 USD | 15,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.83` | 5,660.00 USD | 15,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.83` | 11,620.00 USD | 15,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.85` | 8,780.00 USD | 15,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.85` | 1,970.00 USD | 14,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.87` | 10,780.00 USD | 14,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.88` | 871,990.00 USD | 14,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.88` | 6,540.00 USD | 14,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.90` | 126,700.00 USD | 14,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.90` | 230,110.00 USD | 13,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.92` | 4,900.00 USD | 13,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.92` | 51,300.00 USD | 13,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.94` | 152,910.00 USD | 13,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.94` | 18,680.00 USD | 13,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.96` | 14,060.00 USD | 13,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.96` | 1,380.00 USD | 13,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.98` | 173,220.00 USD | 13,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.98` | 7,400.00 USD | 13,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.00` | 9,500.00 USD | 13,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.00` | 11,020.00 USD | 13,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.02` | 26,540.00 USD | 13,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.02` | 33,130.00 USD | 13,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.04` | 99,420.00 USD | 13,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.04` | 167,580.00 USD | 13,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.06` | 132,270.00 USD | 12,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.06` | 2,890,000.00 USD | 12,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.08` | 40,840.00 USD | 9,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.08` | 11,370.00 USD | 9,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.10` | 6,300.00 USD | 9,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.10` | 186,200.00 USD | 9,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.12` | 111,930.00 USD | 9,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.12` | 7,810.00 USD | 9,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.13` | 7,780.00 USD | 9,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.15` | 22,850.00 USD | 9,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.15` | 2,060.00 USD | 9,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.17` | 11,930.00 USD | 9,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.17` | 1,200.00 USD | 9,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.19` | 300,690.00 USD | 9,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.19` | 8,280.00 USD | 9,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.21` | 27,760.00 USD | 9,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.21` | 13,040.00 USD | 9,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.23` | 23,110.00 USD | 9,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.23` | 39,310.00 USD | 9,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.25` | 19,810.00 USD | 9,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.25` | 5,290.00 USD | 9,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.27` | 51,360.00 USD | 9,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.27` | 868,730.00 USD | 9,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.29` | 4,080.00 USD | 8,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.29` | 133,000.00 USD | 8,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.31` | 136,230.00 USD | 8,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.31` | 24,860.00 USD | 7,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.33` | 9,110.00 USD | 7,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.33` | 73,460.00 USD | 7,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.35` | 18,900.00 USD | 7,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.35` | 1,210.00 USD | 7,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.37` | 41,170.00 USD | 7,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.38` | 64,430.00 USD | 7,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.38` | 46,170.00 USD | 7,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.40` | 36,770.00 USD | 7,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.40` | 103,060.00 USD | 7,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.42` | 391,020.00 USD | 7,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.42` | 5,400.00 USD | 7,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.44` | 29,660.00 USD | 7,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.44` | 164,130.00 USD | 7,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.46` | 12,040.00 USD | 6,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.46` | 16,780.00 USD | 6,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.48` | 164,470.00 USD | 6,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.48` | 18,740,000.00 USD | 18,740,000.00 USD | 45,650.00 USD | 26,250.00 USD | 1,510.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.48` | 30,100.00 USD | 6,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.50` | 49,910.00 USD | 6,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.50` | 18,660,000.00 USD | 18,660,000.00 USD | 16,960.00 USD | 6,940.00 USD | 38,050.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.50` | 47,110.00 USD | 6,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.51` | 18,600,000.00 USD | 18,600,000.00 USD | 3,690.00 USD | 0.00 USD | 231.64 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.52` | 69,940.00 USD | 6,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.52` | 18,600,000.00 USD | 18,600,000.00 USD | 15,180.00 USD | 0.00 USD | 41,090.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.52` | 114,740.00 USD | 6,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.53` | 18,540,000.00 USD | 18,540,000.00 USD | 93,360.00 USD | 40,470.00 USD | 96,140.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.54` | 94,440.00 USD | 6,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.54` | 18,310,000.00 USD | 18,310,000.00 USD | 3,040.00 USD | 58,300.00 USD | 30,480.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.54` | 167,840.00 USD | 6,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.55` | 18,220,000.00 USD | 18,220,000.00 USD | 128,490.00 USD | 54,880.00 USD | 45,330.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.56` | 556,540.00 USD | 6,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.56` | 17,990,000.00 USD | 17,990,000.00 USD | 61,170.00 USD | 0.00 USD | 32.49 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.56` | 1,380,000.00 USD | 5,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.57` | 17,930,000.00 USD | 17,930,000.00 USD | 86,360.00 USD | 27,910.00 USD | 84,270.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.58` | 67,180.00 USD | 4,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.58` | 17,730,000.00 USD | 17,730,000.00 USD | 173,980.00 USD | 48,640.00 USD | 59,950.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.58` | 42,530.00 USD | 4,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.59` | 17,450,000.00 USD | 17,450,000.00 USD | 535.75 USD | 18,170.00 USD | 78.80 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.60` | 22,620.00 USD | 4,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.60` | 17,430,000.00 USD | 17,430,000.00 USD | 64,170.00 USD | 21,460.00 USD | 22,050.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.60` | 276,290.00 USD | 4,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.61` | 17,320,000.00 USD | 17,320,000.00 USD | 56,580.00 USD | 37,060.00 USD | 44,890.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.62` | 16,360.00 USD | 3,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.62` | 17,180,000.00 USD | 17,180,000.00 USD | 92,130.00 USD | 26,640.00 USD | 97,570.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.62` | 132,530.00 USD | 3,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.63` | 16,970,000.00 USD | 16,970,000.00 USD | 50,840.00 USD | 8,120.00 USD | 159.02 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.63` | 95,160.00 USD | 3,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.64` | 16,910,000.00 USD | 16,910,000.00 USD | 2,410.00 USD | 41,960.00 USD | 119,140.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.65` | 15,050.00 USD | 3,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.65` | 16,750,000.00 USD | 16,750,000.00 USD | 53,900.00 USD | 7,050.00 USD | 31,190.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.65` | 20,880.00 USD | 3,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.66` | 16,650,000.00 USD | 16,650,000.00 USD | 32,350.00 USD | 15,090.00 USD | 125,270.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.67` | 40,010.00 USD | 3,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.67` | 16,480,000.00 USD | 16,480,000.00 USD | 52,020.00 USD | 14,480.00 USD | 53,670.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.67` | 106,380.00 USD | 3,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.68` | 16,360,000.00 USD | 16,360,000.00 USD | 1,010.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.69` | 217,880.00 USD | 3,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.69` | 16,360,000.00 USD | 16,360,000.00 USD | 27,750.00 USD | 0.00 USD | 59,840.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.69` | 93,270.00 USD | 3,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.70` | 16,270,000.00 USD | 16,270,000.00 USD | 20,470.00 USD | 7,370.00 USD | 112,470.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.71` | 79,410.00 USD | 3,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.71` | 16,130,000.00 USD | 16,130,000.00 USD | 51,960.00 USD | 0.00 USD | 74,330.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.71` | 68,990.00 USD | 2,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.72` | 16,010,000.00 USD | 16,010,000.00 USD | 425.03 USD | 0.00 USD | 183.06 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.73` | 163,920.00 USD | 2,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.73` | 16,000,000.00 USD | 16,000,000.00 USD | 41,940.00 USD | 10,880.00 USD | 56,790.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.73` | 123,490.00 USD | 2,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.74` | 15,890,000.00 USD | 15,890,000.00 USD | 130,620.00 USD | 40,020.00 USD | 122,480.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.75` | 24,210.00 USD | 2,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.75` | 15,600,000.00 USD | 15,600,000.00 USD | 3,890.00 USD | 51,780.00 USD | 129,350.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.75` | 150,270.00 USD | 2,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.76` | 15,420,000.00 USD | 15,420,000.00 USD | 32,650.00 USD | 10,110.00 USD | 22,610.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.77` | 201,540.00 USD | 2,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.77` | 15,350,000.00 USD | 15,350,000.00 USD | 15,340.00 USD | 8,090.00 USD | 23,020.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.77` | 29,280.00 USD | 2,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.78` | 15,300,000.00 USD | 15,300,000.00 USD | 24,180.00 USD | 93,830.00 USD | 41,570.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.79` | 34,900.00 USD | 2,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.79` | 19,690,000.00 USD | 19,690,000.00 USD | 9,260.00 USD | 79,360.00 USD | 106,250.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.79` | 15,150,000.00 USD | 15,150,000.00 USD | 51,640.00 USD | 0.00 USD | 137,710.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.79` | 36,690.00 USD | 2,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.80` | 19,500,000.00 USD | 19,500,000.00 USD | 3,400.00 USD | 0.00 USD | 74,400.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.80` | 14,960,000.00 USD | 14,960,000.00 USD | 8,210.00 USD | 34,570.00 USD | 17,840.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.81` | 585,850.00 USD | 2,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.81` | 19,420,000.00 USD | 19,420,000.00 USD | 213,700.00 USD | 0.00 USD | 103,870.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.81` | 14,900,000.00 USD | 14,900,000.00 USD | 5,310.00 USD | 0.00 USD | 1,430.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.81` | 10,380.00 USD | 1,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.82` | 19,100,000.00 USD | 19,100,000.00 USD | 49,390.00 USD | 31,910.00 USD | 141,610.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.82` | 14,890,000.00 USD | 14,890,000.00 USD | 5,630.00 USD | 18,370.00 USD | 25,600.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.83` | 181,850.00 USD | 1,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.83` | 18,880,000.00 USD | 18,880,000.00 USD | 125,840.00 USD | 125,330.00 USD | 114,620.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.83` | 14,840,000.00 USD | 14,840,000.00 USD | 50,540.00 USD | 50,500.00 USD | 153.98 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.83` | 177,970.00 USD | 1,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.84` | 18,520,000.00 USD | 18,520,000.00 USD | 150,080.00 USD | 46,190.00 USD | 64,230.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.84` | 14,740,000.00 USD | 14,740,000.00 USD | 7,940.00 USD | 33,350.00 USD | 146.37 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.85` | 119,980.00 USD | 1,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.85` | 18,260,000.00 USD | 18,260,000.00 USD | 186,230.00 USD | 175,470.00 USD | 37,740.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.85` | 14,700,000.00 USD | 14,700,000.00 USD | 3,390.00 USD | 49,170.00 USD | 84,260.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.85` | 37,650.00 USD | 1,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.86` | 17,860,000.00 USD | 17,860,000.00 USD | 39,130.00 USD | 39,050.00 USD | 52,990.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.86` | 14,560,000.00 USD | 14,560,000.00 USD | 5,190.00 USD | 173,980.00 USD | 72,520.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.87` | 75,620.00 USD | 1,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.87` | 17,720,000.00 USD | 17,720,000.00 USD | 52,700.00 USD | 58,230.00 USD | 188,300.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.87` | 14,310,000.00 USD | 14,310,000.00 USD | 63,710.00 USD | 0.00 USD | 227,340.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.88` | 8,180.00 USD | 938,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.88` | 17,430,000.00 USD | 17,430,000.00 USD | 35,520.00 USD | 17,520.00 USD | 224,870.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.88` | 14,020,000.00 USD | 14,020,000.00 USD | 110,160.00 USD | 86,900.00 USD | 156,790.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.88` | 177,470.00 USD | 929,910.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.89` | 17,150,000.00 USD | 17,150,000.00 USD | 373,610.00 USD | 100,370.00 USD | 238,830.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.89` | 13,660,000.00 USD | 13,660,000.00 USD | 4,240.00 USD | 50,710.00 USD | 83,380.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.90` | 97,100.00 USD | 752,440.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.90` | 16,430,000.00 USD | 16,430,000.00 USD | 33,360.00 USD | 49,080.00 USD | 223,320.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.90` | 13,520,000.00 USD | 13,520,000.00 USD | 274,050.00 USD | 28,250.00 USD | 51,510.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.90` | 6,520.00 USD | 655,340.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.91` | 16,130,000.00 USD | 16,130,000.00 USD | 337,710.00 USD | 120,100.00 USD | 276,080.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.91` | 13,170,000.00 USD | 13,170,000.00 USD | 122,540.00 USD | 67,260.00 USD | 46,930.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.92` | 37,310.00 USD | 648,820.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.92` | 15,400,000.00 USD | 15,400,000.00 USD | 318,260.00 USD | 8,570.00 USD | 127,670.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.92` | 12,930,000.00 USD | 12,930,000.00 USD | 85,790.00 USD | 66,710.00 USD | 104,900.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.92` | 2,480.00 USD | 611,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.93` | 14,940,000.00 USD | 14,940,000.00 USD | 116,350.00 USD | 99,220.00 USD | 97,360.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.93` | 12,680,000.00 USD | 12,680,000.00 USD | 0.00 USD | 28,720.00 USD | 67.04 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.94` | 3,320.00 USD | 609,030.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.94` | 14,630,000.00 USD | 14,630,000.00 USD | 132,520.00 USD | 53,060.00 USD | 137,210.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.94` | 12,650,000.00 USD | 12,650,000.00 USD | 55,330.00 USD | 0.00 USD | 2,250.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.94` | 149,880.00 USD | 605,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.95` | 14,310,000.00 USD | 14,310,000.00 USD | 116,010.00 USD | 0.00 USD | 33,080.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.95` | 12,590,000.00 USD | 12,590,000.00 USD | 8,490.00 USD | 0.00 USD | 2,800.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.96` | 56,160.00 USD | 455,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.96` | 14,160,000.00 USD | 14,160,000.00 USD | 67,260.00 USD | 22,830.00 USD | 17,320.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.96` | 12,580,000.00 USD | 12,580,000.00 USD | 165,060.00 USD | 0.00 USD | 325.84 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.96` | 10,220.00 USD | 399,670.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.97` | 14,050,000.00 USD | 14,050,000.00 USD | 2,650.00 USD | 36,470.00 USD | 137,700.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.97` | 12,410,000.00 USD | 12,410,000.00 USD | 235,890.00 USD | 0.00 USD | 2,980.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.98` | 71,610.00 USD | 389,450.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.98` | 13,870,000.00 USD | 13,870,000.00 USD | 20,780.00 USD | 76,990.00 USD | 94,490.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.98` | 12,170,000.00 USD | 12,170,000.00 USD | 506,280.00 USD | 0.00 USD | 279,750.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.98` | 5,650.00 USD | 317,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.99` | 13,680,000.00 USD | 13,680,000.00 USD | 34,010.00 USD | 64,350.00 USD | 106,350.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.99` | 11,390,000.00 USD | 11,390,000.00 USD | 298,270.00 USD | 26,340.00 USD | 78,590.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.00` | 160,840.00 USD | 312,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.00` | 13,470,000.00 USD | 13,470,000.00 USD | 40,030.00 USD | 17,140.00 USD | 137,750.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.00` | 10,990,000.00 USD | 10,990,000.00 USD | 307,590.00 USD | 68,590.00 USD | 574,560.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.00` | 11,990.00 USD | 151,350.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.01` | 13,280,000.00 USD | 13,280,000.00 USD | 1,580.00 USD | 158,450.00 USD | 222,750.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.01` | 10,030,000.00 USD | 10,030,000.00 USD | 371,710.00 USD | 57,440.00 USD | 438,780.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.01` | 4,070.00 USD | 4,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.02` | 12,900,000.00 USD | 12,900,000.00 USD | 135,580.00 USD | 52,150.00 USD | 125,260.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.02` | 9,170,000.00 USD | 9,170,000.00 USD | 271,690.00 USD | 156,620.00 USD | 251,090.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.03` | 856.12 USD | 139,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.03` | 12,580,000.00 USD | 12,580,000.00 USD | 64,700.00 USD | 59,350.00 USD | 324.38 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.03` | 8,490,000.00 USD | 8,490,000.00 USD | 247,960.00 USD | 0.00 USD | 344,930.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.04` | 21,260.00 USD | 138,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.04` | 12,460,000.00 USD | 12,460,000.00 USD | 69,810.00 USD | 21,940.00 USD | 183,420.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.04` | 7,890,000.00 USD | 7,890,000.00 USD | 321,230.00 USD | 0.00 USD | 492,290.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.04` | 19,300.00 USD | 117,250.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.05` | 12,180,000.00 USD | 12,180,000.00 USD | 348,930.00 USD | 23,720.00 USD | 145.87 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.05` | 7,080,000.00 USD | 7,080,000.00 USD | 2,180.00 USD | 41,020.00 USD | 68,490.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.05` | 1,080.00 USD | 97,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.06` | 11,810,000.00 USD | 11,810,000.00 USD | 35,870.00 USD | 83,800.00 USD | 450,780.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.06` | 6,970,000.00 USD | 6,970,000.00 USD | 0.00 USD | 72,410.00 USD | 292.74 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.07` | 6,800.00 USD | 96,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.07` | 11,240,000.00 USD | 11,240,000.00 USD | 358,380.00 USD | 205,460.00 USD | 334,550.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.07` | 6,900,000.00 USD | 6,900,000.00 USD | 0.00 USD | 287,180.00 USD | 166,640.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.08` | 553.79 USD | 90,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.08` | 10,340,000.00 USD | 10,340,000.00 USD | 69,080.00 USD | 277,630.00 USD | 133,910.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.08` | 6,440,000.00 USD | 6,440,000.00 USD | 0.00 USD | 237,170.00 USD | 135.50 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.08` | 21,030.00 USD | 89,520.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.09` | 9,860,000.00 USD | 9,860,000.00 USD | 245,370.00 USD | 60,230.00 USD | 168,220.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.09` | 6,210,000.00 USD | 6,210,000.00 USD | 253,510.00 USD | 179,350.00 USD | 432,940.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.09` | 17,640.00 USD | 68,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.10` | 9,390,000.00 USD | 9,390,000.00 USD | 2,770.00 USD | 89,650.00 USD | 141,410.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.10` | 5,340,000.00 USD | 5,340,000.00 USD | 27,630.00 USD | 0.00 USD | 240.24 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.11` | 16,940.00 USD | 50,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.11` | 9,150,000.00 USD | 9,150,000.00 USD | 120,600.00 USD | 138,540.00 USD | 345,580.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.11` | 5,310,000.00 USD | 5,310,000.00 USD | 0.00 USD | 25,170.00 USD | 295,730.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.12` | 24,080.00 USD | 33,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.12` | 8,550,000.00 USD | 8,550,000.00 USD | 48,010.00 USD | 34,010.00 USD | 274,180.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.12` | 4,990,000.00 USD | 4,990,000.00 USD | 2,900.00 USD | 181,330.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `4.13` | 8,190,000.00 USD | 8,190,000.00 USD | 159,720.00 USD | 0.00 USD | 398,260.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.13` | 4,810,000.00 USD | 4,810,000.00 USD | 154,140.00 USD | 0.00 USD | 237,490.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `4.14` | 7,640,000.00 USD | 7,640,000.00 USD | 98,250.00 USD | 0.00 USD | 125,370.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.14` | 4,420,000.00 USD | 4,420,000.00 USD | 238,150.00 USD | 217,700.00 USD | 345,750.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.14` | 9,830.00 USD | 9,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.15` | 7,410,000.00 USD | 7,410,000.00 USD | 469,190.00 USD | 102,010.00 USD | 318,980.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.15` | 3,610,000.00 USD | 3,610,000.00 USD | 235,070.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `4.16` | 6,520,000.00 USD | 6,520,000.00 USD | 276,920.00 USD | 51,570.00 USD | 316,310.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.17` | 9,290.00 USD | 13,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.17` | 5,880,000.00 USD | 5,880,000.00 USD | 215,050.00 USD | 283,430.00 USD | 238,930.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.17` | 3,380,000.00 USD | 3,380,000.00 USD | 252,690.00 USD | 84,340.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `4.18` | 5,140,000.00 USD | 5,140,000.00 USD | 329,080.00 USD | 62,340.00 USD | 158,920.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.18` | 3,040,000.00 USD | 3,040,000.00 USD | 0.00 USD | 0.00 USD | 86,570.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `4.19` | 4,590,000.00 USD | 4,590,000.00 USD | 148,260.00 USD | 115,850.00 USD | 244,930.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.19` | 2,950,000.00 USD | 2,950,000.00 USD | 2,760.00 USD | 50,340.00 USD | 393,520.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `4.20` | 4,080,000.00 USD | 4,080,000.00 USD | 540.30 USD | 26,180.00 USD | 131,830.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.20` | 2,510,000.00 USD | 2,510,000.00 USD | 227,690.00 USD | 86,790.00 USD | 371,630.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `4.21` | 3,920,000.00 USD | 3,920,000.00 USD | 487,450.00 USD | 98,820.00 USD | 217,230.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.21` | 1,820,000.00 USD | 1,820,000.00 USD | 308,290.00 USD | 0.00 USD | 146,990.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `4.22` | 3,120,000.00 USD | 3,120,000.00 USD | 0.00 USD | 0.00 USD | 56,420.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.22` | 1,370,000.00 USD | 1,370,000.00 USD | 119,070.00 USD | 89,680.00 USD | 417,550.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `4.23` | 3,060,000.00 USD | 3,060,000.00 USD | 0.00 USD | 114,760.00 USD | 176,960.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `4.25` | 2,770,000.00 USD | 2,770,000.00 USD | 0.00 USD | 0.00 USD | 186,310.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.25` | 740,600.00 USD | 740,600.00 USD | 3,390.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.26` | 737,210.00 USD | 737,210.00 USD | 2,960.00 USD | 0.00 USD | 173,150.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.27` | 561,100.00 USD | 561,100.00 USD | 24,810.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.28` | 395.44 USD | 13,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.28` | 2,580,000.00 USD | 2,580,000.00 USD | 4,310.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.28` | 536,280.00 USD | 536,280.00 USD | 5,380.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `4.29` | 2,580,000.00 USD | 2,580,000.00 USD | 156,040.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.29` | 530,900.00 USD | 530,900.00 USD | 5,150.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `4.31` | 2,420,000.00 USD | 2,420,000.00 USD | 0.00 USD | 0.00 USD | 353.18 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `4.32` | 2,420,000.00 USD | 2,420,000.00 USD | 381,790.00 USD | 0.00 USD | 326.33 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.32` | 525,750.00 USD | 525,750.00 USD | 265,720.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `4.33` | 2,040,000.00 USD | 2,040,000.00 USD | 287,160.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `4.34` | 1,750,000.00 USD | 1,750,000.00 USD | 269,670.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.34` | 260,030.00 USD | 260,030.00 USD | 0.00 USD | 0.00 USD | 7,340.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.34` | 4,130.00 USD | 17,880.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.35` | 1,480,000.00 USD | 1,480,000.00 USD | 157,030.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.35` | 252,690.00 USD | 252,690.00 USD | 252,690.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.36` | 3,050.00 USD | 20,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.36` | 1,330,000.00 USD | 1,330,000.00 USD | 100,970.00 USD | 93,400.00 USD | 279,180.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `4.37` | 853,590.00 USD | 853,590.00 USD | 280,420.00 USD | 173,170.00 USD | 400,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.37` | 443,860.00 USD | 443,860.00 USD | 0.00 USD | 50,340.00 USD | 393,520.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.38` | 76,420.00 USD | 97,350.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.38` | 952,140.00 USD | 952,140.00 USD | 250,760.00 USD | 60,680.00 USD | 640,700.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.38` | 1,900,000.00 USD | 1,900,000.00 USD | 250,760.00 USD | 60,680.00 USD | 640,700.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.38` | 933,960.00 USD | 933,960.00 USD | 0.00 USD | 228,720.00 USD | 261,380.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.39` | 2,810,000.00 USD | 2,810,000.00 USD | 356,920.00 USD | 41,380.00 USD | 505,620.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.39` | 2,010,000.00 USD | 2,010,000.00 USD | 560,900.00 USD | 149,280.00 USD | 369,470.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.39` | 180,760.00 USD | 278,110.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.40` | 3,730,000.00 USD | 3,730,000.00 USD | 458,500.00 USD | 58,380.00 USD | 408,330.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.40` | 3,120,000.00 USD | 3,120,000.00 USD | 111,810.00 USD | 116,620.00 USD | 881,540.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.41` | 4,980,000.00 USD | 4,980,000.00 USD | 336,310.00 USD | 317,280.00 USD | 592,230.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.41` | 3,470,000.00 USD | 3,470,000.00 USD | 1,450.00 USD | 65,600.00 USD | 278,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.42` | 3,410.00 USD | 281,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.42` | 5,250,000.00 USD | 5,250,000.00 USD | 1,080.00 USD | 142,250.00 USD | 127,800.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.42` | 4,120,000.00 USD | 4,120,000.00 USD | 404,280.00 USD | 71,590.00 USD | 175,990.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.42` | 1,930.00 USD | 283,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.43` | 5,750,000.00 USD | 5,750,000.00 USD | 84,650.00 USD | 109,630.00 USD | 300,550.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.43` | 4,570,000.00 USD | 4,570,000.00 USD | 293,250.00 USD | 88,400.00 USD | 71,780.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.43` | 5,610.00 USD | 289,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.44` | 6,640,000.00 USD | 6,640,000.00 USD | 156,430.00 USD | 370,280.00 USD | 372,140.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.44` | 4,960,000.00 USD | 4,960,000.00 USD | 0.00 USD | 143,990.00 USD | 246,120.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.45` | 33,190.00 USD | 322,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.45` | 6,950,000.00 USD | 6,950,000.00 USD | 76,860.00 USD | 108,640.00 USD | 124,130.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.45` | 5,190,000.00 USD | 5,190,000.00 USD | 0.00 USD | 25,170.00 USD | 196,900.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.46` | 2,160.00 USD | 324,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.46` | 7,030,000.00 USD | 7,030,000.00 USD | 4,580.00 USD | 37,160.00 USD | 33,060.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.46` | 5,300,000.00 USD | 5,300,000.00 USD | 3,070.00 USD | 105,500.00 USD | 2,350.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.46` | 1,370.00 USD | 325,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.47` | 7,330,000.00 USD | 7,330,000.00 USD | 160,740.00 USD | 25,190.00 USD | 120,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.47` | 5,870,000.00 USD | 5,870,000.00 USD | 358,290.00 USD | 135,940.00 USD | 75,550.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.47` | 19,880.00 USD | 345,670.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.48` | 7,780,000.00 USD | 7,780,000.00 USD | 205,250.00 USD | 86,520.00 USD | 150,910.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.48` | 6,120,000.00 USD | 6,120,000.00 USD | 1,870.00 USD | 44,840.00 USD | 210,580.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.49` | 5,000.00 USD | 350,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.49` | 8,620,000.00 USD | 8,620,000.00 USD | 253,770.00 USD | 235,310.00 USD | 354,870.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.49` | 6,460,000.00 USD | 6,460,000.00 USD | 244,370.00 USD | 93,790.00 USD | 162.91 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.50` | 20,580.00 USD | 371,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.50` | 9,230,000.00 USD | 9,230,000.00 USD | 363,660.00 USD | 69,580.00 USD | 175,170.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.50` | 7,040,000.00 USD | 7,040,000.00 USD | 376,770.00 USD | 200,700.00 USD | 2,050.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.50` | 1,330.00 USD | 372,580.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.51` | 9,990,000.00 USD | 9,990,000.00 USD | 188,660.00 USD | 149,810.00 USD | 418,530.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.51` | 7,120,000.00 USD | 7,120,000.00 USD | 77,780.00 USD | 0.00 USD | 2,140.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.51` | 5,220.00 USD | 377,800.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.52` | 10,610,000.00 USD | 10,610,000.00 USD | 290,030.00 USD | 92,260.00 USD | 243,090.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.52` | 7,350,000.00 USD | 7,350,000.00 USD | 2,080.00 USD | 0.00 USD | 225,130.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.53` | 819.48 USD | 378,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.53` | 11,400,000.00 USD | 11,400,000.00 USD | 505,320.00 USD | 0.00 USD | 280,060.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.53` | 8,330,000.00 USD | 8,330,000.00 USD | 439,420.00 USD | 232,800.00 USD | 309,760.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.54` | 3,060.00 USD | 381,680.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.54` | 11,800,000.00 USD | 11,800,000.00 USD | 15,720.00 USD | 150,600.00 USD | 234,180.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.54` | 9,570,000.00 USD | 9,570,000.00 USD | 2,730.00 USD | 0.00 USD | 1,240,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.54` | 252.70 USD | 381,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.55` | 11,940,000.00 USD | 11,940,000.00 USD | 1,620.00 USD | 34,450.00 USD | 108,590.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.55` | 9,570,000.00 USD | 9,570,000.00 USD | 0.00 USD | 0.00 USD | 237.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.56` | 12,350,000.00 USD | 12,350,000.00 USD | 81,450.00 USD | 32,800.00 USD | 288,460.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.56` | 10,060,000.00 USD | 10,060,000.00 USD | 364,250.00 USD | 124,220.00 USD | 219.44 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.57` | 12,690,000.00 USD | 12,690,000.00 USD | 176,460.00 USD | 70,180.00 USD | 99,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.57` | 10,600,000.00 USD | 10,600,000.00 USD | 305,830.00 USD | 27,650.00 USD | 209,430.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.58` | 13,850,000.00 USD | 13,850,000.00 USD | 423,030.00 USD | 99,430.00 USD | 634,100.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.58` | 10,730,000.00 USD | 10,730,000.00 USD | 44,380.00 USD | 0.00 USD | 86,090.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.58` | 2,140.00 USD | 384,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.59` | 14,450,000.00 USD | 14,450,000.00 USD | 419,400.00 USD | 75,460.00 USD | 109,280.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.59` | 12,440,000.00 USD | 12,440,000.00 USD | 760,880.00 USD | 68,070.00 USD | 881,510.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.60` | 14,620,000.00 USD | 14,620,000.00 USD | 49,460.00 USD | 50,860.00 USD | 66,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.60` | 12,560,000.00 USD | 12,560,000.00 USD | 3,460.00 USD | 112,080.00 USD | 2,360.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.61` | 14,770,000.00 USD | 14,770,000.00 USD | 64,340.00 USD | 7,560.00 USD | 76,320.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.61` | 12,570,000.00 USD | 12,570,000.00 USD | 5,400.00 USD | 0.00 USD | 1,140.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.62` | 14,910,000.00 USD | 14,910,000.00 USD | 94,450.00 USD | 31,380.00 USD | 19,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.62` | 12,710,000.00 USD | 12,710,000.00 USD | 134,680.00 USD | 0.00 USD | 2,890.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.62` | 51,690.00 USD | 435,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.63` | 14,920,000.00 USD | 14,920,000.00 USD | 2,310.00 USD | 0.00 USD | 335.46 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.63` | 12,920,000.00 USD | 12,920,000.00 USD | 215,660.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.63` | 1,500.00 USD | 437,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.64` | 15,070,000.00 USD | 15,070,000.00 USD | 106,430.00 USD | 11,270.00 USD | 41,460.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.64` | 13,460,000.00 USD | 13,460,000.00 USD | 503,610.00 USD | 34,570.00 USD | 1,730.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.64` | 713.47 USD | 437,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.65` | 15,820,000.00 USD | 15,820,000.00 USD | 203,560.00 USD | 52,020.00 USD | 486,560.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.65` | 13,880,000.00 USD | 13,880,000.00 USD | 420,940.00 USD | 0.00 USD | 2,070.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.66` | 756.44 USD | 438,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.66` | 16,610,000.00 USD | 16,610,000.00 USD | 202,480.00 USD | 309,340.00 USD | 277,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.66` | 14,200,000.00 USD | 14,200,000.00 USD | 144,860.00 USD | 18,370.00 USD | 150,940.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.67` | 150,350.00 USD | 589,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.67` | 16,950,000.00 USD | 16,950,000.00 USD | 88,770.00 USD | 0.00 USD | 259,350.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.67` | 14,240,000.00 USD | 14,240,000.00 USD | 0.00 USD | 0.00 USD | 43,230.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.67` | 54,290.00 USD | 643,380.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.68` | 17,160,000.00 USD | 17,160,000.00 USD | 60,330.00 USD | 106,120.00 USD | 37,010.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.68` | 15,160,000.00 USD | 15,160,000.00 USD | 381,910.00 USD | 83,630.00 USD | 450,770.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.68` | 1,030.00 USD | 644,410.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.69` | 17,540,000.00 USD | 17,540,000.00 USD | 168,690.00 USD | 49,160.00 USD | 168,810.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.69` | 15,320,000.00 USD | 15,320,000.00 USD | 52,990.00 USD | 16,870.00 USD | 88,340.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.70` | 230.06 USD | 644,640.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.70` | 17,890,000.00 USD | 17,890,000.00 USD | 69,690.00 USD | 97,490.00 USD | 175,270.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.70` | 15,630,000.00 USD | 15,630,000.00 USD | 74,240.00 USD | 60,360.00 USD | 181,350.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.71` | 7,480.00 USD | 652,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.71` | 18,930,000.00 USD | 18,930,000.00 USD | 390,710.00 USD | 298,900.00 USD | 353,490.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.71` | 16,120,000.00 USD | 16,120,000.00 USD | 178,360.00 USD | 232,800.00 USD | 78,760.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.72` | 19,160,000.00 USD | 19,160,000.00 USD | 2,370.00 USD | 181,280.00 USD | 49,950.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.72` | 16,330,000.00 USD | 16,330,000.00 USD | 7,140.00 USD | 17,360.00 USD | 180,490.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.73` | 19,330,000.00 USD | 19,330,000.00 USD | 109,760.00 USD | 25,210.00 USD | 35,480.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.73` | 16,400,000.00 USD | 16,400,000.00 USD | 59,970.00 USD | 15,660.00 USD | 894.74 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.74` | 8,880.00 USD | 661,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.74` | 19,710,000.00 USD | 19,710,000.00 USD | 68,200.00 USD | 132,280.00 USD | 176,190.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.74` | 16,790,000.00 USD | 16,790,000.00 USD | 14,750.00 USD | 191,030.00 USD | 182,880.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.75` | 20,080,000.00 USD | 20,080,000.00 USD | 76,690.00 USD | 141,340.00 USD | 151,830.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.75` | 17,340,000.00 USD | 17,340,000.00 USD | 17,340.00 USD | 185,060.00 USD | 343,810.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.76` | 20,200,000.00 USD | 20,200,000.00 USD | 32,430.00 USD | 51,460.00 USD | 31,810.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.76` | 18,680,000.00 USD | 18,680,000.00 USD | 1,030,000.00 USD | 46,890.00 USD | 272,680.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.76` | 205.37 USD | 661,200.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.77` | 20,330,000.00 USD | 20,330,000.00 USD | 4,870.00 USD | 85,030.00 USD | 47,800.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.77` | 19,590,000.00 USD | 19,590,000.00 USD | 732,640.00 USD | 73,410.00 USD | 101,640.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.78` | 15,680.00 USD | 676,880.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.78` | 20,480,000.00 USD | 20,480,000.00 USD | 37,290.00 USD | 20,000.00 USD | 87,070.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.78` | 20,720,000.00 USD | 20,720,000.00 USD | 499,950.00 USD | 477,230.00 USD | 154,510.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.79` | 143.55 USD | 677,020.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.79` | 20,680,000.00 USD | 20,680,000.00 USD | 112,300.00 USD | 44,330.00 USD | 42,140.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.79` | 21,760,000.00 USD | 21,760,000.00 USD | 713,060.00 USD | 249,310.00 USD | 72,120.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.79` | 1,950.00 USD | 678,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.80` | 21,200,000.00 USD | 21,200,000.00 USD | 226,540.00 USD | 136,530.00 USD | 159,500.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.80` | 23,350,000.00 USD | 23,350,000.00 USD | 1,160,000.00 USD | 432,340.00 USD | 2,480.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.81` | 21,240,000.00 USD | 21,240,000.00 USD | 0.00 USD | 30,450.00 USD | 11,630.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.81` | 23,980,000.00 USD | 23,980,000.00 USD | 400,800.00 USD | 125,900.00 USD | 101,780.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.82` | 4,090.00 USD | 683,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.82` | 21,370,000.00 USD | 21,370,000.00 USD | 8,250.00 USD | 81,720.00 USD | 35,520.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.82` | 26,740,000.00 USD | 26,740,000.00 USD | 1,010,000.00 USD | 369,430.00 USD | 1,390,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.83` | 1,740.00 USD | 684,800.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.83` | 21,390,000.00 USD | 21,390,000.00 USD | 15,330.00 USD | 5,610.00 USD | 129.50 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.83` | 28,390,000.00 USD | 28,390,000.00 USD | 822,860.00 USD | 85,680.00 USD | 739,630.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.83` | 1,540.00 USD | 686,340.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.84` | 21,540,000.00 USD | 21,540,000.00 USD | 38,320.00 USD | 76,320.00 USD | 34,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.84` | 28,880,000.00 USD | 28,880,000.00 USD | 97,300.00 USD | 71,790.00 USD | 322,840.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.84` | 11,220.00 USD | 697,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.85` | 21,670,000.00 USD | 21,670,000.00 USD | 104,560.00 USD | 0.00 USD | 28,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.85` | 30,920,000.00 USD | 30,920,000.00 USD | 487,940.00 USD | 380,760.00 USD | 1,160,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.86` | 32,330,000.00 USD | 32,330,000.00 USD | 444,810.00 USD | 162,380.00 USD | 802,380.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.87` | 137.68 USD | 697,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `4.87` | 33,390,000.00 USD | 33,390,000.00 USD | 264,730.00 USD | 136,820.00 USD | 663,430.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.88` | 34,880,000.00 USD | 34,880,000.00 USD | 428,040.00 USD | 266,980.00 USD | 789,710.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.88` | 3,200.00 USD | 700,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4.91` | 674.44 USD | 701,570.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4.92` | 20,720.00 USD | 722,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4.92` | 81,000.00 USD | 803,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4.93` | 157.43 USD | 803,450.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4.96` | 488.56 USD | 803,940.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4.97` | 99,370.00 USD | 903,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.05` | 35,380.00 USD | 938,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.07` | 3,420.00 USD | 942,110.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.08` | 1,200.00 USD | 943,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.12` | 53,810.00 USD | 997,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.14` | 2,570.00 USD | 999,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.17` | 751.51 USD | 1,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.20` | 11,250.00 USD | 1,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.22` | 72,290.00 USD | 1,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.25` | 143.71 USD | 1,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.25` | 17,990.00 USD | 1,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.26` | 5,610.00 USD | 1,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.28` | 1,690.00 USD | 1,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.29` | 134.77 USD | 1,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.29` | 1,100,000.00 USD | 2,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.30` | 41,660.00 USD | 2,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.32` | 15,970.00 USD | 2,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.34` | 298,680.00 USD | 2,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.36` | 142.44 USD | 2,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.38` | 182.21 USD | 2,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.42` | 1,030.00 USD | 2,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.42` | 60,740.00 USD | 2,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.43` | 13,040.00 USD | 2,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.47` | 7,840.00 USD | 2,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.50` | 66,470.00 USD | 2,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.51` | 38,800.00 USD | 2,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.53` | 62,710.00 USD | 2,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.54` | 209.22 USD | 2,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.57` | 8,670.00 USD | 2,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.58` | 62,420.00 USD | 2,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.59` | 686.51 USD | 2,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.61` | 701.75 USD | 2,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.63` | 1,620,000.00 USD | 4,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.67` | 1,630.00 USD | 4,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.67` | 228.70 USD | 4,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.68` | 3,900,000.00 USD | 8,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.70` | 471,680.00 USD | 8,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.71` | 3,900.00 USD | 8,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.75` | 4,580.00 USD | 8,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.75` | 286.02 USD | 8,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.78` | 2,710.00 USD | 8,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.83` | 269,960.00 USD | 9,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.84` | 310.95 USD | 9,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.86` | 848.39 USD | 9,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.88` | 7,150.00 USD | 9,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.89` | 88,420.00 USD | 9,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.91` | 162.98 USD | 9,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.92` | 189.28 USD | 9,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.95` | 103,780.00 USD | 9,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.03` | 23,060.00 USD | 9,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.05` | 323,960.00 USD | 9,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.07` | 740.54 USD | 9,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.08` | 17,160.00 USD | 9,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.09` | 37,510.00 USD | 9,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.13` | 2,430.00 USD | 9,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.14` | 23,870.00 USD | 9,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.16` | 1,880.00 USD | 9,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.18` | 35,350.00 USD | 9,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.24` | 527,010.00 USD | 10,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.25` | 7,300.00 USD | 10,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.25` | 439.10 USD | 10,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.26` | 256,050.00 USD | 10,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.32` | 310.70 USD | 10,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.33` | 2,010.00 USD | 10,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.33` | 382.00 USD | 10,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.34` | 214.46 USD | 10,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.37` | 113.93 USD | 10,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.38` | 288.15 USD | 10,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.39` | 2,750.00 USD | 10,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.41` | 3,780.00 USD | 10,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.42` | 943.65 USD | 10,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.42` | 173.47 USD | 10,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.45` | 1,220,000.00 USD | 11,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.46` | 7,150.00 USD | 11,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.46` | 1,940.00 USD | 11,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.51` | 380.48 USD | 11,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.54` | 376.34 USD | 11,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.55` | 5,590.00 USD | 11,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.57` | 380,370.00 USD | 12,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.58` | 29,680,000.00 USD | 41,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.59` | 418.78 USD | 41,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.61` | 40,880.00 USD | 41,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.66` | 7,230.00 USD | 41,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.67` | 233.94 USD | 41,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.67` | 200.25 USD | 41,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.72` | 37,370.00 USD | 42,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.75` | 1,270,000.00 USD | 43,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.78` | 186.31 USD | 43,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.79` | 719.89 USD | 43,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.82` | 156.75 USD | 43,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.84` | 753.63 USD | 43,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.87` | 2,650.00 USD | 43,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.92` | 6,920.00 USD | 43,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.96` | 93,100.00 USD | 43,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.99` | 664.27 USD | 43,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.03` | 665.27 USD | 43,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.04` | 15,740.00 USD | 43,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.09` | 699.57 USD | 43,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.14` | 3,790,000.00 USD | 47,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.17` | 1,010.00 USD | 47,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.20` | 570.56 USD | 47,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.21` | 13,560.00 USD | 47,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.24` | 4,910.00 USD | 47,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.33` | 54,940.00 USD | 47,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.33` | 4,850.00 USD | 47,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.39` | 59,980.00 USD | 47,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.41` | 776.04 USD | 47,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.45` | 106,290.00 USD | 47,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.46` | 1,420.00 USD | 47,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.46` | 9,970,000.00 USD | 57,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.50` | 7,800,000.00 USD | 65,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.53` | 1,570.00 USD | 65,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.54` | 13,670.00 USD | 65,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.54` | 2,620.00 USD | 65,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.55` | 11,440.00 USD | 65,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.59` | 17,700.00 USD | 65,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.62` | 3,050.00 USD | 65,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.63` | 19,210.00 USD | 65,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.66` | 20,000.00 USD | 65,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.67` | 360.25 USD | 65,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.67` | 33,070.00 USD | 65,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.70` | 317.80 USD | 65,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.71` | 26,980.00 USD | 65,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.72` | 6,400.00 USD | 65,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.74` | 505.87 USD | 65,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.75` | 629.67 USD | 65,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.80` | 1,690.00 USD | 65,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.83` | 109.69 USD | 65,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.86` | 94,260.00 USD | 65,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.87` | 2,980.00 USD | 65,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.93` | 165.84 USD | 65,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.95` | 6,120.00 USD | 65,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.99` | 399.25 USD | 65,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.00` | 257.44 USD | 65,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.03` | 435,420.00 USD | 65,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.06` | 6,450.00 USD | 65,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.19` | 63,470.00 USD | 66,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.20` | 951.44 USD | 66,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.21` | 51,690.00 USD | 66,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.35` | 25,310.00 USD | 66,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.37` | 1,100,000.00 USD | 67,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.38` | 8,900.00 USD | 67,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.46` | 1,230.00 USD | 67,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.47` | 816.99 USD | 67,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.48` | 6,640.00 USD | 67,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.51` | 428,200.00 USD | 67,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `0.8750` | 22,120,000.00 USD | 0.00 USD | 1,660.00 USD | `-79.88%` | `1,894.00` |
| `Live` | `Long` | `0.8950` | 22,120,000.00 USD | 0.00 USD | 39,060.00 USD | `-79.42%` | `43,643.60` |
| `Live` | `Long` | `0.9050` | 22,080,000.00 USD | 0.00 USD | 292.22 USD | `-79.19%` | `322.90` |
| `Live` | `Long` | `0.9150` | 22,080,000.00 USD | 0.00 USD | 11,370.00 USD | `-78.96%` | `12,425.00` |
| `Live` | `Long` | `0.9250` | 22,070,000.00 USD | 0.00 USD | 1,850.00 USD | `-78.73%` | `2,001.60` |
| `Live` | `Long` | `0.9350` | 22,070,000.00 USD | 0.00 USD | 29,760.00 USD | `-78.50%` | `31,823.80` |
| `Live` | `Long` | `0.9550` | 22,040,000.00 USD | 0.00 USD | 2,890.00 USD | `-78.04%` | `3,031.40` |
| `Live` | `Long` | `0.9650` | 22,030,000.00 USD | 0.00 USD | 965.00 USD | `-77.81%` | `1,000.00` |
| `Live` | `Long` | `0.9850` | 22,030,000.00 USD | 0.00 USD | 707.53 USD | `-77.35%` | `718.30` |
| `Live` | `Long` | `0.9950` | 22,030,000.00 USD | 0.00 USD | 154,200.00 USD | `-77.12%` | `154,969.90` |
| `Live` | `Long` | `1.00` | 21,880,000.00 USD | 0.00 USD | 2,560.00 USD | `-76.89%` | `2,543.70` |
| `Live` | `Long` | `1.02` | 21,880,000.00 USD | 0.00 USD | 11,240.00 USD | `-76.43%` | `10,967.70` |
| `Live` | `Long` | `1.03` | 21,860,000.00 USD | 0.00 USD | 36,980.00 USD | `-76.20%` | `35,734.20` |
| `Live` | `Long` | `1.04` | 21,830,000.00 USD | 0.00 USD | 2,740.00 USD | `-75.97%` | `2,617.40` |
| `Live` | `Long` | `1.05` | 21,820,000.00 USD | 0.00 USD | 6,860.00 USD | `-75.74%` | `6,504.40` |
| `Live` | `Long` | `1.06` | 21,820,000.00 USD | 0.00 USD | 892.90 USD | `-75.51%` | `838.40` |
| `Live` | `Long` | `1.07` | 21,820,000.00 USD | 0.00 USD | 5,310.00 USD | `-75.28%` | `4,939.60` |
| `Live` | `Long` | `1.08` | 21,810,000.00 USD | 0.00 USD | 470,570.00 USD | `-75.05%` | `433,703.70` |
| `Live` | `Long` | `1.09` | 21,340,000.00 USD | 0.00 USD | 6,690.00 USD | `-74.82%` | `6,107.50` |
| `Live` | `Long` | `1.10` | 21,330,000.00 USD | 0.00 USD | 1,430.00 USD | `-74.59%` | `1,295.60` |
| `Live` | `Long` | `1.11` | 21,330,000.00 USD | 0.00 USD | 2,160.00 USD | `-74.36%` | `1,936.80` |
| `Live` | `Long` | `1.12` | 21,330,000.00 USD | 0.00 USD | 856.24 USD | `-74.13%` | `761.10` |
| `Live` | `Long` | `1.14` | 21,330,000.00 USD | 0.00 USD | 4,960.00 USD | `-73.90%` | `4,368.60` |
| `Live` | `Long` | `1.15` | 21,320,000.00 USD | 0.00 USD | 26,780.00 USD | `-73.67%` | `23,387.50` |
| `Live` | `Long` | `1.17` | 21,300,000.00 USD | 0.00 USD | 1,810.00 USD | `-73.21%` | `1,553.20` |
| `Live` | `Long` | `1.18` | 21,300,000.00 USD | 0.00 USD | 647.54 USD | `-72.98%` | `551.10` |
| `Live` | `Long` | `1.19` | 21,300,000.00 USD | 0.00 USD | 12,420.00 USD | `-72.75%` | `10,484.90` |
| `Live` | `Long` | `1.20` | 21,280,000.00 USD | 0.00 USD | 148.42 USD | `-72.52%` | `124.20` |
| `Live` | `Long` | `1.24` | 21,280,000.00 USD | 0.00 USD | 18,650.00 USD | `-71.60%` | `15,097.50` |
| `Live` | `Long` | `1.25` | 21,260,000.00 USD | 0.00 USD | 250.87 USD | `-71.37%` | `201.50` |
| `Live` | `Long` | `1.25` | 21,260,000.00 USD | 0.00 USD | 15,020.00 USD | `-71.14%` | `11,969.60` |
| `Live` | `Long` | `1.26` | 21,250,000.00 USD | 0.00 USD | 2,060.00 USD | `-70.91%` | `1,630.60` |
| `Live` | `Long` | `1.27` | 21,250,000.00 USD | 0.00 USD | 2,390.00 USD | `-70.68%` | `1,876.80` |
| `Live` | `Long` | `1.28` | 21,240,000.00 USD | 0.00 USD | 1,160.00 USD | `-70.45%` | `901.80` |
| `Live` | `Long` | `1.29` | 21,240,000.00 USD | 0.00 USD | 258.35 USD | `-70.22%` | `199.50` |
| `Live` | `Long` | `1.30` | 21,240,000.00 USD | 0.00 USD | 116.80 USD | `-69.99%` | `89.50` |
| `Live` | `Long` | `1.32` | 21,240,000.00 USD | 0.00 USD | 9,260.00 USD | `-69.53%` | `6,989.40` |
| `Live` | `Long` | `1.33` | 21,230,000.00 USD | 0.00 USD | 148.32 USD | `-69.30%` | `111.10` |
| `Live` | `Long` | `1.34` | 21,230,000.00 USD | 0.00 USD | 603.91 USD | `-69.07%` | `449.00` |
| `Live` | `Long` | `1.35` | 21,230,000.00 USD | 0.00 USD | 66,360.00 USD | `-68.84%` | `48,972.10` |
| `Live` | `Long` | `1.36` | 21,170,000.00 USD | 0.00 USD | 725.63 USD | `-68.61%` | `531.60` |
| `Live` | `Long` | `1.38` | 21,170,000.00 USD | 0.00 USD | 10,080.00 USD | `-68.38%` | `7,330.70` |
| `Live` | `Long` | `1.39` | 21,160,000.00 USD | 0.00 USD | 12,760.00 USD | `-68.15%` | `9,213.40` |
| `Live` | `Long` | `1.40` | 21,140,000.00 USD | 0.00 USD | 1,060.00 USD | `-67.92%` | `758.20` |
| `Live` | `Long` | `1.41` | 21,140,000.00 USD | 0.00 USD | 27,720.00 USD | `-67.69%` | `19,730.30` |
| `Live` | `Long` | `1.42` | 21,110,000.00 USD | 0.00 USD | 76,020.00 USD | `-67.46%` | `53,725.90` |
| `Live` | `Long` | `1.43` | 21,040,000.00 USD | 0.00 USD | 1,130.00 USD | `-67.23%` | `793.40` |
| `Live` | `Long` | `1.45` | 21,040,000.00 USD | 0.00 USD | 1,530.00 USD | `-66.77%` | `1,061.70` |
| `Live` | `Long` | `1.46` | 21,040,000.00 USD | 0.00 USD | 5,440.00 USD | `-66.54%` | `3,738.20` |
| `Live` | `Long` | `1.47` | 21,030,000.00 USD | 0.00 USD | 14,940.00 USD | `-66.31%` | `10,194.90` |
| `Live` | `Long` | `1.48` | 21,020,000.00 USD | 0.00 USD | 2,290.00 USD | `-66.08%` | `1,550.00` |
| `Live` | `Long` | `1.49` | 21,010,000.00 USD | 0.00 USD | 3,110.00 USD | `-65.85%` | `2,096.20` |
| `Live` | `Long` | `1.50` | 21,010,000.00 USD | 0.00 USD | 2,740.00 USD | `-65.62%` | `1,831.00` |
| `Live` | `Long` | `1.51` | 21,010,000.00 USD | 0.00 USD | 454.50 USD | `-65.16%` | `300.00` |
| `Live` | `Long` | `1.53` | 21,010,000.00 USD | 0.00 USD | 2,340.00 USD | `-64.70%` | `1,527.10` |
| `Live` | `Long` | `1.54` | 21,000,000.00 USD | 0.00 USD | 169.95 USD | `-64.47%` | `110.00` |
| `Live` | `Long` | `1.55` | 21,000,000.00 USD | 0.00 USD | 1,450.00 USD | `-64.24%` | `932.00` |
| `Live` | `Long` | `1.56` | 21,000,000.00 USD | 0.00 USD | 20,570.00 USD | `-64.01%` | `13,146.30` |
| `Live` | `Long` | `1.57` | 20,980,000.00 USD | 0.00 USD | 1,020.00 USD | `-63.78%` | `646.20` |
| `Live` | `Long` | `1.58` | 20,980,000.00 USD | 0.00 USD | 2,180.00 USD | `-63.55%` | `1,374.10` |
| `Live` | `Long` | `1.59` | 20,980,000.00 USD | 0.00 USD | 3,700.00 USD | `-63.32%` | `2,319.70` |
| `Live` | `Long` | `1.60` | 20,980,000.00 USD | 0.00 USD | 191.64 USD | `-63.09%` | `119.40` |
| `Live` | `Long` | `1.64` | 20,980,000.00 USD | 0.00 USD | 6,790.00 USD | `-62.40%` | `4,153.70` |
| `Live` | `Long` | `1.65` | 20,970,000.00 USD | 0.00 USD | 582,010.00 USD | `-62.17%` | `353,805.20` |
| `Live` | `Long` | `1.66` | 20,390,000.00 USD | 0.00 USD | 83,540.00 USD | `-61.94%` | `50,475.70` |
| `Live` | `Long` | `1.67` | 20,300,000.00 USD | 0.00 USD | 6,160.00 USD | `-61.71%` | `3,699.10` |
| `Live` | `Long` | `1.68` | 20,300,000.00 USD | 0.00 USD | 1,520.00 USD | `-61.48%` | `908.70` |
| `Live` | `Long` | `1.69` | 20,300,000.00 USD | 0.00 USD | 17,300.00 USD | `-61.25%` | `10,268.30` |
| `Live` | `Long` | `1.70` | 20,280,000.00 USD | 0.00 USD | 102.72 USD | `-61.02%` | `60.60` |
| `Live` | `Long` | `1.73` | 20,280,000.00 USD | 0.00 USD | 5,460.00 USD | `-60.33%` | `3,164.50` |
| `Live` | `Long` | `1.75` | 20,270,000.00 USD | 0.00 USD | 23,850.00 USD | `-59.64%` | `13,592.20` |
| `Live` | `Long` | `1.76` | 20,250,000.00 USD | 0.00 USD | 2,510.00 USD | `-59.41%` | `1,419.70` |
| `Live` | `Long` | `1.77` | 20,250,000.00 USD | 0.00 USD | 4,330.00 USD | `-59.18%` | `2,440.30` |
| `Live` | `Long` | `1.79` | 20,240,000.00 USD | 0.00 USD | 456.47 USD | `-58.72%` | `254.30` |
| `Live` | `Long` | `1.80` | 20,240,000.00 USD | 0.00 USD | 529.05 USD | `-58.49%` | `293.10` |
| `Live` | `Long` | `1.81` | 20,240,000.00 USD | 0.00 USD | 1,580.00 USD | `-58.26%` | `873.20` |
| `Live` | `Long` | `1.82` | 20,240,000.00 USD | 0.00 USD | 853.74 USD | `-58.03%` | `467.80` |
| `Live` | `Long` | `1.83` | 20,240,000.00 USD | 0.00 USD | 36,780.00 USD | `-57.80%` | `20,041.70` |
| `Live` | `Long` | `1.85` | 20,200,000.00 USD | 0.00 USD | 984.26 USD | `-57.34%` | `530.60` |
| `Live` | `Long` | `1.86` | 20,200,000.00 USD | 0.00 USD | 16,100.00 USD | `-57.11%` | `8,632.40` |
| `Live` | `Long` | `1.88` | 20,180,000.00 USD | 0.00 USD | 656.25 USD | `-56.88%` | `350.00` |
| `Live` | `Long` | `1.90` | 20,180,000.00 USD | 0.00 USD | 37,060.00 USD | `-56.42%` | `19,555.90` |
| `Live` | `Long` | `1.91` | 20,150,000.00 USD | 0.00 USD | 288.61 USD | `-56.19%` | `151.50` |
| `Live` | `Long` | `1.93` | 20,150,000.00 USD | 0.00 USD | 1,120.00 USD | `-55.73%` | `579.70` |
| `Live` | `Long` | `1.94` | 20,150,000.00 USD | 0.00 USD | 1,270.00 USD | `-55.50%` | `654.30` |
| `Live` | `Long` | `1.95` | 20,140,000.00 USD | 0.00 USD | 2,740.00 USD | `-55.27%` | `1,410.10` |
| `Live` | `Long` | `1.96` | 20,140,000.00 USD | 0.00 USD | 2,860.00 USD | `-55.04%` | `1,465.00` |
| `Live` | `Long` | `1.97` | 20,140,000.00 USD | 0.00 USD | 1,730.00 USD | `-54.81%` | `879.10` |
| `Live` | `Long` | `1.98` | 20,140,000.00 USD | 0.00 USD | 35,130.00 USD | `-54.58%` | `17,789.50` |
| `Live` | `Long` | `2.00` | 20,100,000.00 USD | 0.00 USD | 46,610.00 USD | `-54.12%` | `23,361.10` |
| `Live` | `Long` | `2.02` | 20,050,000.00 USD | 0.00 USD | 3,100.00 USD | `-53.66%` | `1,539.50` |
| `Live` | `Long` | `2.02` | 20,050,000.00 USD | 0.00 USD | 3,660.00 USD | `-53.43%` | `1,808.10` |
| `Live` | `Long` | `2.04` | 20,050,000.00 USD | 0.00 USD | 323.36 USD | `-53.20%` | `158.90` |
| `Live` | `Long` | `2.04` | 20,050,000.00 USD | 0.00 USD | 3,460.00 USD | `-52.97%` | `1,693.20` |
| `Live` | `Long` | `2.06` | 20,040,000.00 USD | 0.00 USD | 1,100.00 USD | `-52.74%` | `537.20` |
| `Live` | `Long` | `2.06` | 20,040,000.00 USD | 0.00 USD | 2,520.00 USD | `-52.51%` | `1,220.50` |
| `Live` | `Long` | `2.08` | 20,040,000.00 USD | 0.00 USD | 11,100.00 USD | `-52.28%` | `5,347.70` |
| `Live` | `Long` | `2.08` | 20,030,000.00 USD | 0.00 USD | 18,600.00 USD | `-52.05%` | `8,920.10` |
| `Live` | `Long` | `2.10` | 20,010,000.00 USD | 0.00 USD | 17,340.00 USD | `-51.82%` | `8,274.80` |
| `Live` | `Long` | `2.10` | 19,990,000.00 USD | 0.00 USD | 6,090.00 USD | `-51.59%` | `2,894.60` |
| `Live` | `Long` | `2.12` | 19,990,000.00 USD | 0.00 USD | 14,240.00 USD | `-51.36%` | `6,731.40` |
| `Live` | `Long` | `2.12` | 19,970,000.00 USD | 0.00 USD | 8,770.00 USD | `-51.13%` | `4,127.30` |
| `Live` | `Long` | `2.13` | 19,960,000.00 USD | 0.00 USD | 2,140.00 USD | `-50.90%` | `1,000.80` |
| `Live` | `Long` | `2.15` | 19,960,000.00 USD | 0.00 USD | 2,110.00 USD | `-50.67%` | `983.60` |
| `Live` | `Long` | `2.15` | 19,960,000.00 USD | 0.00 USD | 4,550.00 USD | `-50.44%` | `2,113.50` |
| `Live` | `Long` | `2.17` | 19,960,000.00 USD | 0.00 USD | 279,760.00 USD | `-50.21%` | `129,219.70` |
| `Live` | `Long` | `2.17` | 19,680,000.00 USD | 0.00 USD | 14,140.00 USD | `-49.98%` | `6,500.40` |
| `Live` | `Long` | `2.19` | 19,660,000.00 USD | 0.00 USD | 1,110.00 USD | `-49.75%` | `505.90` |
| `Live` | `Long` | `2.19` | 19,660,000.00 USD | 0.00 USD | 12,830.00 USD | `-49.52%` | `5,843.40` |
| `Live` | `Long` | `2.21` | 19,650,000.00 USD | 0.00 USD | 39,620.00 USD | `-49.29%` | `17,967.40` |
| `Live` | `Long` | `2.21` | 19,610,000.00 USD | 0.00 USD | 91,610.00 USD | `-49.06%` | `41,357.70` |
| `Live` | `Long` | `2.23` | 19,520,000.00 USD | 0.00 USD | 457.24 USD | `-48.83%` | `205.50` |
| `Live` | `Long` | `2.23` | 19,520,000.00 USD | 0.00 USD | 2,450.00 USD | `-48.60%` | `1,097.50` |
| `Live` | `Long` | `2.25` | 19,510,000.00 USD | 0.00 USD | 38,480.00 USD | `-48.37%` | `17,142.40` |
| `Live` | `Long` | `2.25` | 19,480,000.00 USD | 0.00 USD | 329,770.00 USD | `-48.14%` | `146,238.50` |
| `Live` | `Long` | `2.27` | 19,150,000.00 USD | 0.00 USD | 1,580.00 USD | `-47.91%` | `695.70` |
| `Live` | `Long` | `2.27` | 19,140,000.00 USD | 0.00 USD | 812.18 USD | `-47.68%` | `357.00` |
| `Live` | `Long` | `2.29` | 19,140,000.00 USD | 0.00 USD | 463.86 USD | `-47.45%` | `203.00` |
| `Live` | `Long` | `2.29` | 19,140,000.00 USD | 0.00 USD | 11,990.00 USD | `-47.22%` | `5,224.90` |
| `Live` | `Long` | `2.31` | 19,130,000.00 USD | 0.00 USD | 7,500.00 USD | `-46.99%` | `3,254.60` |
| `Live` | `Long` | `2.31` | 19,120,000.00 USD | 0.00 USD | 2,330.00 USD | `-46.76%` | `1,005.00` |
| `Live` | `Long` | `2.33` | 19,120,000.00 USD | 0.00 USD | 13,770.00 USD | `-46.53%` | `5,923.50` |
| `Live` | `Long` | `2.33` | 19,110,000.00 USD | 0.00 USD | 30,690.00 USD | `-46.30%` | `13,145.40` |
| `Live` | `Long` | `2.35` | 19,080,000.00 USD | 0.00 USD | 5,790.00 USD | `-46.07%` | `2,467.50` |
| `Live` | `Long` | `2.35` | 19,070,000.00 USD | 0.00 USD | 25,910.00 USD | `-45.84%` | `11,000.00` |
| `Live` | `Long` | `2.37` | 19,040,000.00 USD | 0.00 USD | 3,840.00 USD | `-45.61%` | `1,624.70` |
| `Live` | `Long` | `2.38` | 19,040,000.00 USD | 0.00 USD | 35,180.00 USD | `-45.38%` | `14,811.30` |
| `Live` | `Long` | `2.38` | 19,010,000.00 USD | 0.00 USD | 6,250.00 USD | `-45.15%` | `2,620.90` |
| `Live` | `Long` | `2.40` | 19,000,000.00 USD | 0.00 USD | 119,870.00 USD | `-44.92%` | `50,048.30` |
| `Live` | `Long` | `2.40` | 18,880,000.00 USD | 0.00 USD | 11,030.00 USD | `-44.69%` | `4,586.00` |
| `Live` | `Long` | `2.42` | 18,870,000.00 USD | 0.00 USD | 1,760,000.00 USD | `-44.46%` | `730,349.00` |
| `Live` | `Long` | `2.42` | 17,100,000.00 USD | 0.00 USD | 273,060.00 USD | `-44.23%` | `112,601.40` |
| `Live` | `Long` | `2.44` | 16,830,000.00 USD | 0.00 USD | 4,770.00 USD | `-44.00%` | `1,957.90` |
| `Live` | `Long` | `2.44` | 16,830,000.00 USD | 0.00 USD | 253,220.00 USD | `-43.77%` | `103,564.60` |
| `Live` | `Long` | `2.46` | 16,570,000.00 USD | 0.00 USD | 49,540.00 USD | `-43.54%` | `20,179.00` |
| `Live` | `Long` | `2.46` | 16,520,000.00 USD | 0.00 USD | 6,090.00 USD | `-43.31%` | `2,469.20` |
| `Live` | `Long` | `2.48` | 16,520,000.00 USD | 0.00 USD | 336.35 USD | `-43.08%` | `135.90` |
| `Live` | `Long` | `2.48` | 16,520,000.00 USD | 0.00 USD | 3,110.00 USD | `-42.85%` | `1,250.20` |
| `Live` | `Long` | `2.50` | 16,510,000.00 USD | 0.00 USD | 15,100.00 USD | `-42.62%` | `6,050.70` |
| `Live` | `Long` | `2.50` | 16,500,000.00 USD | 0.00 USD | 6,000.00 USD | `-42.39%` | `2,395.50` |
| `Live` | `Long` | `2.52` | 16,490,000.00 USD | 0.00 USD | 39,960.00 USD | `-41.93%` | `15,824.10` |
| `Live` | `Long` | `2.54` | 16,450,000.00 USD | 0.00 USD | 866.97 USD | `-41.70%` | `342.00` |
| `Live` | `Long` | `2.54` | 16,450,000.00 USD | 0.00 USD | 105.36 USD | `-41.47%` | `41.40` |
| `Live` | `Long` | `2.56` | 16,450,000.00 USD | 0.00 USD | 621.12 USD | `-41.24%` | `243.10` |
| `Live` | `Long` | `2.56` | 16,450,000.00 USD | 0.00 USD | 7,890.00 USD | `-41.01%` | `3,077.60` |
| `Live` | `Long` | `2.58` | 16,440,000.00 USD | 0.00 USD | 431,260.00 USD | `-40.78%` | `167,479.10` |
| `Live` | `Long` | `2.58` | 16,010,000.00 USD | 0.00 USD | 11,810.00 USD | `-40.55%` | `4,568.30` |
| `Live` | `Long` | `2.60` | 16,000,000.00 USD | 0.00 USD | 82,820.00 USD | `-40.32%` | `31,916.30` |
| `Live` | `Long` | `2.60` | 15,920,000.00 USD | 0.00 USD | 779.94 USD | `-40.09%` | `299.40` |
| `Live` | `Long` | `2.62` | 15,920,000.00 USD | 0.00 USD | 1,190.00 USD | `-39.86%` | `454.70` |
| `Live` | `Long` | `2.62` | 15,920,000.00 USD | 0.00 USD | 2,470.00 USD | `-39.63%` | `941.80` |
| `Live` | `Long` | `2.63` | 15,910,000.00 USD | 0.00 USD | 24,310.00 USD | `-39.40%` | `9,225.00` |
| `Live` | `Long` | `2.65` | 15,890,000.00 USD | 0.00 USD | 6,020.00 USD | `-39.17%` | `2,274.90` |
| `Live` | `Long` | `2.65` | 15,880,000.00 USD | 0.00 USD | 16,760.00 USD | `-38.94%` | `6,312.10` |
| `Live` | `Long` | `2.67` | 15,870,000.00 USD | 0.00 USD | 1,920.00 USD | `-38.71%` | `721.80` |
| `Live` | `Long` | `2.67` | 15,860,000.00 USD | 0.00 USD | 172,860.00 USD | `-38.48%` | `64,622.30` |
| `Live` | `Long` | `2.69` | 15,690,000.00 USD | 0.00 USD | 8,920.00 USD | `-38.25%` | `3,323.40` |
| `Live` | `Long` | `2.69` | 15,680,000.00 USD | 0.00 USD | 733.85 USD | `-38.02%` | `272.30` |
| `Live` | `Long` | `2.71` | 15,680,000.00 USD | 0.00 USD | 170,360.00 USD | `-37.79%` | `62,978.90` |
| `Live` | `Long` | `2.71` | 15,510,000.00 USD | 0.00 USD | 11,750.00 USD | `-37.56%` | `4,327.50` |
| `Live` | `Long` | `2.73` | 15,500,000.00 USD | 0.00 USD | 28,380.00 USD | `-37.33%` | `10,414.30` |
| `Live` | `Long` | `2.73` | 15,470,000.00 USD | 0.00 USD | 1,850.00 USD | `-37.10%` | `675.80` |
| `Live` | `Long` | `2.75` | 15,470,000.00 USD | 0.00 USD | 39,550.00 USD | `-36.87%` | `14,408.60` |
| `Live` | `Long` | `2.75` | 15,430,000.00 USD | 0.00 USD | 365,820.00 USD | `-36.64%` | `132,783.60` |
| `Live` | `Long` | `2.77` | 15,060,000.00 USD | 0.00 USD | 8,890.00 USD | `-36.41%` | `3,214.40` |
| `Live` | `Long` | `2.77` | 15,060,000.00 USD | 0.00 USD | 719.84 USD | `-36.18%` | `259.40` |
| `Live` | `Long` | `2.79` | 15,050,000.00 USD | 0.00 USD | 49,490.00 USD | `-35.95%` | `17,770.30` |
| `Live` | `Long` | `2.79` | 15,010,000.00 USD | 0.00 USD | 12,340.00 USD | `-35.72%` | `4,416.00` |
| `Live` | `Long` | `2.81` | 14,990,000.00 USD | 0.00 USD | 90,180.00 USD | `-35.49%` | `32,148.50` |
| `Live` | `Long` | `2.81` | 14,900,000.00 USD | 0.00 USD | 4,780.00 USD | `-35.26%` | `1,698.90` |
| `Live` | `Long` | `2.83` | 14,900,000.00 USD | 0.00 USD | 13,990.00 USD | `-35.03%` | `4,952.70` |
| `Live` | `Long` | `2.83` | 14,880,000.00 USD | 0.00 USD | 2,400.00 USD | `-34.80%` | `847.80` |
| `Live` | `Long` | `2.85` | 14,880,000.00 USD | 0.00 USD | 180.94 USD | `-34.57%` | `63.60` |
| `Live` | `Long` | `2.85` | 14,880,000.00 USD | 0.00 USD | 1,970.00 USD | `-34.34%` | `690.70` |
| `Live` | `Long` | `2.87` | 14,880,000.00 USD | 0.00 USD | 21,320.00 USD | `-34.11%` | `7,441.30` |
| `Live` | `Long` | `2.88` | 14,860,000.00 USD | 0.00 USD | 878,580.00 USD | `-33.88%` | `305,591.60` |
| `Live` | `Long` | `2.88` | 13,980,000.00 USD | 0.00 USD | 7,430.00 USD | `-33.65%` | `2,576.40` |
| `Live` | `Long` | `2.90` | 13,970,000.00 USD | 0.00 USD | 114,000.00 USD | `-33.42%` | `39,379.30` |
| `Live` | `Long` | `2.90` | 13,860,000.00 USD | 0.00 USD | 199,300.00 USD | `-33.19%` | `68,605.60` |
| `Live` | `Long` | `2.92` | 13,660,000.00 USD | 0.00 USD | 4,900.00 USD | `-32.96%` | `1,681.40` |
| `Live` | `Long` | `2.92` | 13,650,000.00 USD | 0.00 USD | 48,730.00 USD | `-32.73%` | `16,661.40` |
| `Live` | `Long` | `2.94` | 13,610,000.00 USD | 0.00 USD | 50,520.00 USD | `-32.50%` | `17,211.30` |
| `Live` | `Long` | `2.94` | 13,550,000.00 USD | 0.00 USD | 16,860.00 USD | `-32.27%` | `5,725.40` |
| `Live` | `Long` | `2.96` | 13,540,000.00 USD | 0.00 USD | 13,510.00 USD | `-32.04%` | `4,571.50` |
| `Live` | `Long` | `2.96` | 13,520,000.00 USD | 0.00 USD | 104,820.00 USD | `-31.81%` | `35,353.40` |
| `Live` | `Long` | `2.98` | 13,420,000.00 USD | 0.00 USD | 148,230.00 USD | `-31.58%` | `49,824.70` |
| `Live` | `Long` | `2.98` | 13,270,000.00 USD | 0.00 USD | 5,840.00 USD | `-31.35%` | `1,957.00` |
| `Live` | `Long` | `3.00` | 13,270,000.00 USD | 0.00 USD | 13,250.00 USD | `-31.12%` | `4,424.50` |
| `Live` | `Long` | `3.00` | 13,250,000.00 USD | 0.00 USD | 11,020.00 USD | `-30.89%` | `3,667.70` |
| `Live` | `Long` | `3.02` | 13,240,000.00 USD | 0.00 USD | 32,670.00 USD | `-30.66%` | `10,836.40` |
| `Live` | `Long` | `3.02` | 13,210,000.00 USD | 0.00 USD | 20,580.00 USD | `-30.43%` | `6,804.70` |
| `Live` | `Long` | `3.04` | 13,190,000.00 USD | 0.00 USD | 2,570.00 USD | `-30.20%` | `847.40` |
| `Live` | `Long` | `3.04` | 13,190,000.00 USD | 0.00 USD | 109,800.00 USD | `-29.97%` | `36,057.70` |
| `Live` | `Long` | `3.06` | 13,080,000.00 USD | 0.00 USD | 137,520.00 USD | `-29.74%` | `45,013.70` |
| `Live` | `Long` | `3.06` | 12,940,000.00 USD | 0.00 USD | 163,450.00 USD | `-29.51%` | `53,327.10` |
| `Live` | `Long` | `3.08` | 12,770,000.00 USD | 0.00 USD | 157,420.00 USD | `-29.28%` | `51,192.30` |
| `Live` | `Long` | `3.08` | 12,620,000.00 USD | 0.00 USD | 50,590.00 USD | `-29.05%` | `16,398.80` |
| `Live` | `Long` | `3.10` | 12,570,000.00 USD | 0.00 USD | 5,110.00 USD | `-28.82%` | `1,650.90` |
| `Live` | `Long` | `3.10` | 12,560,000.00 USD | 0.00 USD | 22,590.00 USD | `-28.59%` | `7,275.30` |
| `Live` | `Long` | `3.12` | 12,540,000.00 USD | 0.00 USD | 56,190.00 USD | `-28.36%` | `18,037.60` |
| `Live` | `Long` | `3.12` | 12,480,000.00 USD | 0.00 USD | 2,990,000.00 USD | `-28.13%` | `956,842.50` |
| `Live` | `Long` | `3.13` | 9,490,000.00 USD | 0.00 USD | 10,160.00 USD | `-27.90%` | `3,241.30` |
| `Live` | `Long` | `3.15` | 9,480,000.00 USD | 0.00 USD | 99,300.00 USD | `-27.67%` | `31,574.10` |
| `Live` | `Long` | `3.15` | 9,380,000.00 USD | 0.00 USD | 4,250.00 USD | `-27.44%` | `1,347.20` |
| `Live` | `Long` | `3.17` | 9,380,000.00 USD | 0.00 USD | 68,020.00 USD | `-27.21%` | `21,491.90` |
| `Live` | `Long` | `3.17` | 9,310,000.00 USD | 0.00 USD | 1,200.00 USD | `-26.98%` | `376.60` |
| `Live` | `Long` | `3.19` | 9,310,000.00 USD | 0.00 USD | 245,320.00 USD | `-26.75%` | `77,025.00` |
| `Live` | `Long` | `3.19` | 9,060,000.00 USD | 0.00 USD | 258.16 USD | `-26.52%` | `80.80` |
| `Live` | `Long` | `3.21` | 9,060,000.00 USD | 0.00 USD | 5,090.00 USD | `-26.29%` | `1,589.20` |
| `Live` | `Long` | `3.21` | 9,060,000.00 USD | 0.00 USD | 41,620.00 USD | `-26.06%` | `12,945.80` |
| `Live` | `Long` | `3.23` | 9,020,000.00 USD | 0.00 USD | 23,110.00 USD | `-25.83%` | `7,167.00` |
| `Live` | `Long` | `3.23` | 8,990,000.00 USD | 0.00 USD | 43,760.00 USD | `-25.60%` | `13,526.90` |
| `Live` | `Long` | `3.25` | 8,950,000.00 USD | 0.00 USD | 20,060.00 USD | `-25.37%` | `6,181.90` |
| `Live` | `Long` | `3.25` | 8,930,000.00 USD | 0.00 USD | 4,050.00 USD | `-25.14%` | `1,245.10` |
| `Live` | `Long` | `3.27` | 8,930,000.00 USD | 0.00 USD | 33,650.00 USD | `-24.91%` | `10,307.00` |
| `Live` | `Long` | `3.27` | 8,890,000.00 USD | 0.00 USD | 868,070.00 USD | `-24.68%` | `265,060.40` |
| `Live` | `Long` | `3.29` | 8,020,000.00 USD | 0.00 USD | 4,080.00 USD | `-24.45%` | `1,240.60` |
| `Live` | `Long` | `3.29` | 8,020,000.00 USD | 0.00 USD | 134,250.00 USD | `-24.22%` | `40,743.80` |
| `Live` | `Long` | `3.31` | 7,890,000.00 USD | 0.00 USD | 132,030.00 USD | `-23.99%` | `39,948.60` |
| `Live` | `Long` | `3.31` | 7,750,000.00 USD | 0.00 USD | 24,690.00 USD | `-23.76%` | `7,448.70` |
| `Live` | `Long` | `3.33` | 7,730,000.00 USD | 0.00 USD | 13,340.00 USD | `-23.53%` | `4,011.80` |
| `Live` | `Long` | `3.33` | 7,720,000.00 USD | 0.00 USD | 73,460.00 USD | `-23.30%` | `22,026.40` |
| `Live` | `Long` | `3.35` | 7,640,000.00 USD | 0.00 USD | 18,900.00 USD | `-23.07%` | `5,650.40` |
| `Live` | `Long` | `3.35` | 7,620,000.00 USD | 0.00 USD | 1,210.00 USD | `-22.84%` | `360.80` |
| `Live` | `Long` | `3.37` | 7,620,000.00 USD | 0.00 USD | 41,020.00 USD | `-22.61%` | `12,189.30` |
| `Live` | `Long` | `3.38` | 7,580,000.00 USD | 0.00 USD | 55,170.00 USD | `-22.38%` | `16,345.80` |
| `Live` | `Long` | `3.38` | 7,530,000.00 USD | 0.00 USD | 46,170.00 USD | `-22.15%` | `13,638.50` |
| `Live` | `Long` | `3.40` | 7,480,000.00 USD | 0.00 USD | 51,750.00 USD | `-21.92%` | `15,241.70` |
| `Live` | `Long` | `3.40` | 7,430,000.00 USD | 0.00 USD | 104,080.00 USD | `-21.69%` | `30,566.60` |
| `Live` | `Long` | `3.42` | 7,320,000.00 USD | 0.00 USD | 390,810.00 USD | `-21.46%` | `114,438.90` |
| `Live` | `Long` | `3.42` | 6,930,000.00 USD | 0.00 USD | 13,630.00 USD | `-21.23%` | `3,979.80` |
| `Live` | `Long` | `3.44` | 6,920,000.00 USD | 0.00 USD | 29,830.00 USD | `-21.00%` | `8,683.80` |
| `Live` | `Long` | `3.44` | 6,890,000.00 USD | 0.00 USD | 26,540.00 USD | `-20.77%` | `7,703.10` |
| `Live` | `Long` | `3.46` | 6,860,000.00 USD | 0.00 USD | 150,240.00 USD | `-20.54%` | `43,486.10` |
| `Live` | `Long` | `3.46` | 6,710,000.00 USD | 0.00 USD | 16,470.00 USD | `-20.31%` | `4,754.00` |
| `Live` | `Long` | `3.48` | 6,700,000.00 USD | 0.00 USD | 108,220.00 USD | `-20.08%` | `31,141.30` |
| `Live` | `Long` | `3.48` | 6,590,000.00 USD | 0.00 USD | 30,100.00 USD | `-19.85%` | `8,635.80` |
| `Live` | `Long` | `3.50` | 6,560,000.00 USD | 0.00 USD | 48,550.00 USD | `-19.62%` | `13,891.50` |
| `Live` | `Long` | `3.50` | 6,510,000.00 USD | 0.00 USD | 68,770.00 USD | `-19.39%` | `19,621.10` |
| `Live` | `Long` | `3.52` | 6,440,000.00 USD | 0.00 USD | 42,280.00 USD | `-19.16%` | `12,028.70` |
| `Live` | `Long` | `3.52` | 6,400,000.00 USD | 0.00 USD | 21,620.00 USD | `-18.93%` | `6,133.60` |
| `Live` | `Long` | `3.54` | 6,380,000.00 USD | 0.00 USD | 84,160.00 USD | `-18.70%` | `23,807.00` |
| `Live` | `Long` | `3.54` | 6,290,000.00 USD | 0.00 USD | 152,250.00 USD | `-18.47%` | `42,948.30` |
| `Live` | `Long` | `3.56` | 6,140,000.00 USD | 0.00 USD | 570,020.00 USD | `-18.24%` | `160,343.30` |
| `Live` | `Long` | `3.56` | 5,570,000.00 USD | 0.00 USD | 25,750.00 USD | `-18.01%` | `7,223.40` |
| `Live` | `Long` | `3.58` | 5,550,000.00 USD | 0.00 USD | 1,340,000.00 USD | `-17.78%` | `373,803.30` |
| `Live` | `Long` | `3.58` | 4,210,000.00 USD | 0.00 USD | 120,640.00 USD | `-17.55%` | `33,652.60` |
| `Live` | `Long` | `3.60` | 4,090,000.00 USD | 0.00 USD | 24,010.00 USD | `-17.32%` | `6,680.00` |
| `Live` | `Long` | `3.60` | 4,060,000.00 USD | 0.00 USD | 72,910.00 USD | `-17.09%` | `20,224.70` |
| `Live` | `Long` | `3.62` | 3,990,000.00 USD | 0.00 USD | 229,270.00 USD | `-16.86%` | `63,422.10` |
| `Live` | `Long` | `3.62` | 3,760,000.00 USD | 0.00 USD | 125,580.00 USD | `-16.63%` | `34,643.60` |
| `Live` | `Long` | `3.63` | 3,640,000.00 USD | 0.00 USD | 3,550.00 USD | `-16.40%` | `975.40` |
| `Live` | `Long` | `3.65` | 3,630,000.00 USD | 0.00 USD | 15,050.00 USD | `-16.17%` | `4,128.20` |
| `Live` | `Long` | `3.65` | 3,620,000.00 USD | 0.00 USD | 20,860.00 USD | `-15.94%` | `5,706.00` |
| `Live` | `Long` | `3.67` | 3,600,000.00 USD | 0.00 USD | 39,720.00 USD | `-15.71%` | `10,837.40` |
| `Live` | `Long` | `3.67` | 3,560,000.00 USD | 0.00 USD | 94,680.00 USD | `-15.48%` | `25,762.00` |
| `Live` | `Long` | `3.69` | 3,460,000.00 USD | 0.00 USD | 217,880.00 USD | `-15.25%` | `59,126.00` |
| `Live` | `Long` | `3.69` | 3,240,000.00 USD | 0.00 USD | 102,030.00 USD | `-15.02%` | `27,612.70` |
| `Live` | `Long` | `3.71` | 3,140,000.00 USD | 0.00 USD | 90,780.00 USD | `-14.79%` | `24,501.50` |
| `Live` | `Long` | `3.71` | 3,050,000.00 USD | 0.00 USD | 12,740.00 USD | `-14.56%` | `3,428.30` |
| `Live` | `Long` | `3.73` | 3,040,000.00 USD | 0.00 USD | 355,230.00 USD | `-14.33%` | `95,364.50` |
| `Live` | `Long` | `3.73` | 2,680,000.00 USD | 0.00 USD | 123,790.00 USD | `-14.10%` | `33,143.60` |
| `Live` | `Long` | `3.75` | 2,560,000.00 USD | 0.00 USD | 24,210.00 USD | `-13.87%` | `6,464.40` |
| `Live` | `Long` | `3.75` | 2,540,000.00 USD | 0.00 USD | 150,270.00 USD | `-13.64%` | `40,017.50` |
| `Live` | `Long` | `3.77` | 2,390,000.00 USD | 0.00 USD | 65,190.00 USD | `-13.41%` | `17,315.20` |
| `Live` | `Long` | `3.77` | 2,320,000.00 USD | 0.00 USD | 123,660.00 USD | `-13.18%` | `32,757.30` |
| `Live` | `Long` | `3.79` | 2,200,000.00 USD | 0.00 USD | 48,560.00 USD | `-12.95%` | `12,829.90` |
| `Live` | `Long` | `3.79` | 2,150,000.00 USD | 0.00 USD | 34,520.00 USD | `-12.72%` | `9,097.00` |
| `Live` | `Long` | `3.81` | 2,110,000.00 USD | 0.00 USD | 585,450.00 USD | `-12.49%` | `153,864.10` |
| `Live` | `Long` | `3.81` | 1,530,000.00 USD | 0.00 USD | 10,980.00 USD | `-12.26%` | `2,878.90` |
| `Live` | `Long` | `3.83` | 1,520,000.00 USD | 0.00 USD | 181,850.00 USD | `-12.03%` | `47,542.20` |
| `Live` | `Long` | `3.83` | 1,340,000.00 USD | 0.00 USD | 171,380.00 USD | `-11.80%` | `44,688.70` |
| `Live` | `Long` | `3.85` | 1,160,000.00 USD | 0.00 USD | 119,620.00 USD | `-11.57%` | `31,111.10` |
| `Live` | `Long` | `3.85` | 1,040,000.00 USD | 0.00 USD | 22,330.00 USD | `-11.34%` | `5,792.70` |
| `Live` | `Long` | `3.87` | 1,020,000.00 USD | 0.00 USD | 71,550.00 USD | `-11.11%` | `18,512.20` |
| `Live` | `Long` | `3.88` | 950,740.00 USD | 0.00 USD | 8,130.00 USD | `-10.88%` | `2,097.40` |
| `Live` | `Long` | `3.88` | 942,610.00 USD | 0.00 USD | 173,140.00 USD | `-10.65%` | `44,567.00` |
| `Live` | `Long` | `3.90` | 769,470.00 USD | 0.00 USD | 93,930.00 USD | `-10.42%` | `24,116.30` |
| `Live` | `Long` | `3.90` | 675,530.00 USD | 0.00 USD | 7,990.00 USD | `-10.19%` | `2,047.30` |
| `Live` | `Long` | `3.92` | 667,540.00 USD | 0.00 USD | 37,030.00 USD | `-9.96%` | `9,458.00` |
| `Live` | `Long` | `3.92` | 630,510.00 USD | 0.00 USD | 2,050.00 USD | `-9.73%` | `522.20` |
| `Live` | `Long` | `3.94` | 628,460.00 USD | 0.00 USD | 17,100.00 USD | `-9.50%` | `4,346.00` |
| `Live` | `Long` | `3.94` | 611,360.00 USD | 0.00 USD | 149,880.00 USD | `-9.27%` | `37,992.30` |
| `Live` | `Long` | `3.96` | 461,480.00 USD | 0.00 USD | 56,160.00 USD | `-9.04%` | `14,200.30` |
| `Live` | `Long` | `3.96` | 405,320.00 USD | 0.00 USD | 1,240.00 USD | `-8.81%` | `311.90` |
| `Live` | `Long` | `3.98` | 404,080.00 USD | 0.00 USD | 82,400.00 USD | `-8.58%` | `20,729.90` |
| `Live` | `Long` | `3.98` | 321,680.00 USD | 0.00 USD | 5,650.00 USD | `-8.35%` | `1,417.40` |
| `Live` | `Long` | `4.00` | 316,030.00 USD | 0.00 USD | 160,840.00 USD | `-8.12%` | `40,260.30` |
| `Live` | `Long` | `4.00` | 155,190.00 USD | 0.00 USD | 11,990.00 USD | `-7.89%` | `2,993.80` |
| `Live` | `Long` | `4.01` | 143,200.00 USD | 0.00 USD | 275.83 USD | `-7.66%` | `68.70` |
| `Live` | `Long` | `4.03` | 142,930.00 USD | 0.00 USD | 1,910.00 USD | `-7.43%` | `473.70` |
| `Live` | `Long` | `4.04` | 141,020.00 USD | 0.00 USD | 25,700.00 USD | `-7.20%` | `6,368.40` |
| `Live` | `Long` | `4.04` | 115,320.00 USD | 0.00 USD | 32,100.00 USD | `-6.97%` | `7,936.70` |
| `Live` | `Long` | `4.05` | 83,220.00 USD | 0.00 USD | 4,380.00 USD | `-6.74%` | `1,079.20` |
| `Live` | `Long` | `4.07` | 78,840.00 USD | 0.00 USD | 1,200.00 USD | `-6.51%` | `295.00` |
| `Live` | `Long` | `4.08` | 77,640.00 USD | 0.00 USD | 10,210.00 USD | `-6.28%` | `2,505.20` |
| `Live` | `Long` | `4.08` | 67,430.00 USD | 0.00 USD | 5,330.00 USD | `-6.05%` | `1,304.00` |
| `Live` | `Long` | `4.09` | 62,110.00 USD | 0.00 USD | 17,640.00 USD | `-5.82%` | `4,307.40` |
| `Live` | `Long` | `4.11` | 44,470.00 USD | 0.00 USD | 15,640.00 USD | `-5.59%` | `3,809.30` |
| `Live` | `Long` | `4.12` | 28,830.00 USD | 0.00 USD | 17,630.00 USD | `-5.36%` | `4,284.60` |
| `Live` | `Long` | `4.12` | 11,200.00 USD | 0.00 USD | 11,200.00 USD | `-5.13%` | `2,715.40` |
| `Live` | `Short` | `4.17` | 8,230.00 USD | 8,230.00 USD | 0.00 USD | `-4.21%` | `1,975.90` |
| `Live` | `Short` | `4.21` | 10,000.00 USD | 1,770.00 USD | 0.00 USD | `-3.06%` | `420.00` |
| `Live` | `Short` | `4.29` | 11,080.00 USD | 1,080.00 USD | 0.00 USD | `-1.22%` | `251.30` |
| `Live` | `Short` | `4.36` | 14,130.00 USD | 3,050.00 USD | 0.00 USD | `+0.16%` | `701.00` |
| `Live` | `Short` | `4.38` | 97,690.00 USD | 83,560.00 USD | 0.00 USD | `+0.62%` | `19,099.00` |
| `Live` | `Short` | `4.39` | 278,450.00 USD | 180,760.00 USD | 0.00 USD | `+1.08%` | `41,128.80` |
| `Live` | `Short` | `4.42` | 278,960.00 USD | 507.73 USD | 0.00 USD | `+1.54%` | `115.00` |
| `Live` | `Short` | `4.42` | 280,890.00 USD | 1,930.00 USD | 0.00 USD | `+1.77%` | `436.00` |
| `Live` | `Short` | `4.43` | 285,320.00 USD | 4,430.00 USD | 0.00 USD | `+2.00%` | `999.90` |
| `Live` | `Short` | `4.45` | 285,680.00 USD | 358.27 USD | 0.00 USD | `+2.23%` | `80.60` |
| `Live` | `Short` | `4.46` | 324,530.00 USD | 38,840.00 USD | 0.00 USD | `+2.46%` | `8,719.30` |
| `Live` | `Short` | `4.46` | 325,900.00 USD | 1,370.00 USD | 0.00 USD | `+2.69%` | `306.90` |
| `Live` | `Short` | `4.47` | 343,290.00 USD | 17,400.00 USD | 0.00 USD | `+2.92%` | `3,887.90` |
| `Live` | `Short` | `4.49` | 345,320.00 USD | 2,030.00 USD | 0.00 USD | `+3.15%` | `452.20` |
| `Live` | `Short` | `4.50` | 368,000.00 USD | 22,680.00 USD | 0.00 USD | `+3.38%` | `5,044.50` |
| `Live` | `Short` | `4.50` | 369,530.00 USD | 1,530.00 USD | 0.00 USD | `+3.61%` | `340.10` |
| `Live` | `Short` | `4.51` | 382,800.00 USD | 13,270.00 USD | 0.00 USD | `+3.84%` | `2,939.10` |
| `Live` | `Short` | `4.53` | 383,620.00 USD | 819.48 USD | 0.00 USD | `+4.07%` | `181.10` |
| `Live` | `Short` | `4.54` | 384,590.00 USD | 965.96 USD | 0.00 USD | `+4.30%` | `213.00` |
| `Live` | `Short` | `4.54` | 408,850.00 USD | 24,260.00 USD | 0.00 USD | `+4.53%` | `5,338.60` |
| `Live` | `Short` | `4.55` | 529,770.00 USD | 120,920.00 USD | 0.00 USD | `+4.76%` | `26,547.00` |
| `Live` | `Short` | `4.57` | 712,370.00 USD | 182,600.00 USD | 0.00 USD | `+4.99%` | `40,000.00` |
| `Live` | `Short` | `4.58` | 714,510.00 USD | 2,140.00 USD | 0.00 USD | `+5.45%` | `467.20` |
| `Live` | `Short` | `4.62` | 766,200.00 USD | 51,690.00 USD | 0.00 USD | `+6.37%` | `11,176.20` |
| `Live` | `Short` | `4.63` | 767,190.00 USD | 990.04 USD | 0.00 USD | `+6.60%` | `213.60` |
| `Live` | `Short` | `4.64` | 775,640.00 USD | 8,450.00 USD | 0.00 USD | `+6.83%` | `1,819.00` |
| `Live` | `Short` | `4.66` | 926,320.00 USD | 150,680.00 USD | 0.00 USD | `+7.06%` | `32,369.90` |
| `Live` | `Short` | `4.67` | 926,430.00 USD | 101.70 USD | 0.00 USD | `+7.29%` | `21.80` |
| `Live` | `Short` | `4.67` | 980,710.00 USD | 54,290.00 USD | 0.00 USD | `+7.52%` | `11,612.70` |
| `Live` | `Short` | `4.68` | 981,750.00 USD | 1,030.00 USD | 0.00 USD | `+7.75%` | `220.50` |
| `Live` | `Short` | `4.70` | 981,980.00 USD | 230.06 USD | 0.00 USD | `+7.98%` | `49.00` |
| `Live` | `Short` | `4.71` | 989,460.00 USD | 7,480.00 USD | 0.00 USD | `+8.21%` | `1,590.30` |
| `Live` | `Short` | `4.72` | 992,050.00 USD | 2,590.00 USD | 0.00 USD | `+8.67%` | `547.30` |
| `Live` | `Short` | `4.74` | 995,430.00 USD | 3,380.00 USD | 0.00 USD | `+8.90%` | `714.50` |
| `Live` | `Short` | `4.75` | 1,110,000.00 USD | 111,130.00 USD | 0.00 USD | `+9.13%` | `23,421.00` |
| `Live` | `Short` | `4.76` | 1,110,000.00 USD | 5,980.00 USD | 0.00 USD | `+9.59%` | `1,254.10` |
| `Live` | `Short` | `4.78` | 1,110,000.00 USD | 1,730.00 USD | 0.00 USD | `+9.82%` | `362.40` |
| `Live` | `Short` | `4.79` | 1,110,000.00 USD | 143.55 USD | 0.00 USD | `+10.05%` | `30.00` |
| `Live` | `Short` | `4.79` | 1,120,000.00 USD | 1,330.00 USD | 0.00 USD | `+10.28%` | `277.70` |
| `Live` | `Short` | `4.83` | 1,120,000.00 USD | 2,360.00 USD | 0.00 USD | `+10.97%` | `489.00` |
| `Live` | `Short` | `4.83` | 1,120,000.00 USD | 1,540.00 USD | 0.00 USD | `+11.20%` | `317.90` |
| `Live` | `Short` | `4.84` | 1,130,000.00 USD | 11,220.00 USD | 0.00 USD | `+11.43%` | `2,316.40` |
| `Live` | `Short` | `4.87` | 1,130,000.00 USD | 259.79 USD | 0.00 USD | `+11.89%` | `53.40` |
| `Live` | `Short` | `4.88` | 1,130,000.00 USD | 827.03 USD | 0.00 USD | `+12.35%` | `169.30` |
| `Live` | `Short` | `4.91` | 1,130,000.00 USD | 674.44 USD | 0.00 USD | `+12.81%` | `137.50` |
| `Live` | `Short` | `4.92` | 1,150,000.00 USD | 20,720.00 USD | 0.00 USD | `+13.04%` | `4,214.80` |
| `Live` | `Short` | `4.92` | 1,160,000.00 USD | 2,100.00 USD | 0.00 USD | `+13.27%` | `425.70` |
| `Live` | `Short` | `4.93` | 1,160,000.00 USD | 157.43 USD | 0.00 USD | `+13.50%` | `31.90` |
| `Live` | `Short` | `4.95` | 1,160,000.00 USD | 2,060.00 USD | 0.00 USD | `+13.73%` | `417.10` |
| `Live` | `Short` | `4.96` | 1,160,000.00 USD | 488.56 USD | 0.00 USD | `+13.96%` | `98.60` |
| `Live` | `Short` | `4.97` | 1,260,000.00 USD | 99,370.00 USD | 0.00 USD | `+14.42%` | `19,974.00` |
| `Live` | `Short` | `5.01` | 1,290,000.00 USD | 36,420.00 USD | 0.00 USD | `+15.34%` | `7,262.50` |
| `Live` | `Short` | `5.04` | 1,290,000.00 USD | 118.83 USD | 0.00 USD | `+15.80%` | `23.60` |
| `Live` | `Short` | `5.05` | 1,330,000.00 USD | 35,380.00 USD | 0.00 USD | `+16.26%` | `6,998.80` |
| `Live` | `Short` | `5.07` | 1,330,000.00 USD | 3,420.00 USD | 0.00 USD | `+16.49%` | `675.80` |
| `Live` | `Short` | `5.11` | 1,330,000.00 USD | 177.14 USD | 0.00 USD | `+17.41%` | `34.70` |
| `Live` | `Short` | `5.12` | 1,340,000.00 USD | 5,710.00 USD | 0.00 USD | `+17.64%` | `1,115.40` |
| `Live` | `Short` | `5.12` | 1,390,000.00 USD | 51,250.00 USD | 0.00 USD | `+17.87%` | `10,000.00` |
| `Live` | `Short` | `5.17` | 1,390,000.00 USD | 3,330.00 USD | 0.00 USD | `+18.79%` | `645.50` |
| `Live` | `Short` | `5.20` | 1,400,000.00 USD | 11,250.00 USD | 0.00 USD | `+19.48%` | `2,166.50` |
| `Live` | `Short` | `5.22` | 1,480,000.00 USD | 73,780.00 USD | 0.00 USD | `+20.17%` | `14,120.50` |
| `Live` | `Short` | `5.25` | 1,480,000.00 USD | 143.71 USD | 0.00 USD | `+20.63%` | `27.40` |
| `Live` | `Short` | `5.25` | 1,500,000.00 USD | 17,380.00 USD | 0.00 USD | `+20.86%` | `3,307.90` |
| `Live` | `Short` | `5.26` | 1,520,000.00 USD | 21,280.00 USD | 0.00 USD | `+21.09%` | `4,042.60` |
| `Live` | `Short` | `5.28` | 1,520,000.00 USD | 608.21 USD | 0.00 USD | `+21.32%` | `115.30` |
| `Live` | `Short` | `5.29` | 2,570,000.00 USD | 1,060,000.00 USD | 0.00 USD | `+21.55%` | `200,025.50` |
| `Live` | `Short` | `5.29` | 2,620,000.00 USD | 41,410.00 USD | 0.00 USD | `+21.78%` | `7,820.30` |
| `Live` | `Short` | `5.30` | 2,620,000.00 USD | 524.66 USD | 0.00 USD | `+22.01%` | `98.90` |
| `Live` | `Short` | `5.32` | 2,620,000.00 USD | 147.23 USD | 0.00 USD | `+22.24%` | `27.70` |
| `Live` | `Short` | `5.33` | 2,620,000.00 USD | 286.49 USD | 0.00 USD | `+22.70%` | `53.70` |
| `Live` | `Short` | `5.34` | 2,960,000.00 USD | 338,680.00 USD | 0.00 USD | `+22.93%` | `63,364.20` |
| `Live` | `Short` | `5.36` | 2,960,000.00 USD | 5,940.00 USD | 0.00 USD | `+23.16%` | `1,108.50` |
| `Live` | `Short` | `5.38` | 2,960,000.00 USD | 182.21 USD | 0.00 USD | `+23.62%` | `33.90` |
| `Live` | `Short` | `5.42` | 2,960,000.00 USD | 1,030.00 USD | 0.00 USD | `+24.54%` | `189.60` |
| `Live` | `Short` | `5.42` | 2,960,000.00 USD | 914.65 USD | 0.00 USD | `+24.77%` | `168.60` |
| `Live` | `Short` | `5.43` | 2,960,000.00 USD | 419.04 USD | 0.00 USD | `+25.00%` | `77.10` |
| `Live` | `Short` | `5.47` | 2,970,000.00 USD | 7,840.00 USD | 0.00 USD | `+25.92%` | `1,432.70` |
| `Live` | `Short` | `5.49` | 2,990,000.00 USD | 12,740.00 USD | 0.00 USD | `+26.15%` | `2,322.30` |
| `Live` | `Short` | `5.50` | 3,050,000.00 USD | 66,470.00 USD | 0.00 USD | `+26.38%` | `12,097.30` |
| `Live` | `Short` | `5.50` | 3,110,000.00 USD | 62,990.00 USD | 0.00 USD | `+26.61%` | `11,443.00` |
| `Live` | `Short` | `5.51` | 3,150,000.00 USD | 38,800.00 USD | 0.00 USD | `+26.84%` | `7,034.90` |
| `Live` | `Short` | `5.53` | 3,150,000.00 USD | 1,270.00 USD | 0.00 USD | `+27.07%` | `229.80` |
| `Live` | `Short` | `5.54` | 3,150,000.00 USD | 209.22 USD | 0.00 USD | `+27.30%` | `37.80` |
| `Live` | `Short` | `5.57` | 3,160,000.00 USD | 9,360.00 USD | 0.00 USD | `+27.99%` | `1,682.60` |
| `Live` | `Short` | `5.58` | 3,230,000.00 USD | 62,420.00 USD | 0.00 USD | `+28.45%` | `11,175.80` |
| `Live` | `Short` | `5.62` | 7,200,000.00 USD | 3,980,000.00 USD | 0.00 USD | `+29.37%` | `706,994.70` |
| `Live` | `Short` | `5.66` | 8,830,000.00 USD | 1,630,000.00 USD | 0.00 USD | `+30.06%` | `288,027.90` |
| `Live` | `Short` | `5.67` | 8,830,000.00 USD | 211.30 USD | 0.00 USD | `+30.29%` | `37.30` |
| `Live` | `Short` | `5.67` | 8,830,000.00 USD | 228.70 USD | 0.00 USD | `+30.52%` | `40.30` |
| `Live` | `Short` | `5.68` | 8,860,000.00 USD | 26,090.00 USD | 0.00 USD | `+30.75%` | `4,589.50` |
| `Live` | `Short` | `5.70` | 8,860,000.00 USD | 1,520.00 USD | 0.00 USD | `+30.98%` | `267.40` |
| `Live` | `Short` | `5.71` | 8,860,000.00 USD | 2,130.00 USD | 0.00 USD | `+31.44%` | `372.40` |
| `Live` | `Short` | `5.75` | 8,870,000.00 USD | 4,580.00 USD | 0.00 USD | `+32.13%` | `796.90` |
| `Live` | `Short` | `5.75` | 8,870,000.00 USD | 3,020.00 USD | 0.00 USD | `+32.36%` | `524.10` |
| `Live` | `Short` | `5.76` | 9,350,000.00 USD | 475,940.00 USD | 0.00 USD | `+32.59%` | `82,556.10` |
| `Live` | `Short` | `5.83` | 9,350,000.00 USD | 198.97 USD | 0.00 USD | `+34.20%` | `34.10` |
| `Live` | `Short` | `5.84` | 9,620,000.00 USD | 270,530.00 USD | 0.00 USD | `+34.43%` | `46,283.90` |
| `Live` | `Short` | `5.86` | 9,620,000.00 USD | 848.39 USD | 0.00 USD | `+34.66%` | `144.90` |
| `Live` | `Short` | `5.88` | 9,620,000.00 USD | 7,150.00 USD | 0.00 USD | `+35.35%` | `1,215.40` |
| `Live` | `Short` | `5.89` | 9,710,000.00 USD | 88,420.00 USD | 0.00 USD | `+35.58%` | `15,000.00` |
| `Live` | `Short` | `5.91` | 9,710,000.00 USD | 162.98 USD | 0.00 USD | `+35.81%` | `27.60` |
| `Live` | `Short` | `5.92` | 9,710,000.00 USD | 189.28 USD | 0.00 USD | `+36.04%` | `32.00` |
| `Live` | `Short` | `5.92` | 9,710,000.00 USD | 130.35 USD | 0.00 USD | `+36.27%` | `22.00` |
| `Live` | `Short` | `5.95` | 9,820,000.00 USD | 103,650.00 USD | 0.00 USD | `+36.73%` | `17,434.80` |
| `Live` | `Short` | `6.03` | 9,840,000.00 USD | 23,060.00 USD | 0.00 USD | `+38.57%` | `3,827.40` |
| `Live` | `Short` | `6.05` | 9,860,000.00 USD | 23,520.00 USD | 0.00 USD | `+39.26%` | `3,883.80` |
| `Live` | `Short` | `6.07` | 9,860,000.00 USD | 740.54 USD | 0.00 USD | `+39.49%` | `122.10` |
| `Live` | `Short` | `6.08` | 9,870,000.00 USD | 5,920.00 USD | 0.00 USD | `+39.95%` | `973.10` |
| `Live` | `Short` | `6.09` | 9,910,000.00 USD | 37,510.00 USD | 0.00 USD | `+40.18%` | `6,154.10` |
| `Live` | `Short` | `6.12` | 9,910,000.00 USD | 1,870.00 USD | 0.00 USD | `+40.87%` | `305.00` |
| `Live` | `Short` | `6.13` | 9,910,000.00 USD | 2,430.00 USD | 0.00 USD | `+41.10%` | `396.10` |
| `Live` | `Short` | `6.18` | 9,950,000.00 USD | 35,350.00 USD | 0.00 USD | `+42.25%` | `5,715.90` |
| `Live` | `Short` | `6.21` | 10,280,000.00 USD | 332,230.00 USD | 0.00 USD | `+42.71%` | `53,541.50` |
| `Live` | `Short` | `6.24` | 10,810,000.00 USD | 526,230.00 USD | 0.00 USD | `+43.40%` | `84,400.00` |
| `Live` | `Short` | `6.25` | 10,810,000.00 USD | 7,300.00 USD | 0.00 USD | `+43.63%` | `1,168.90` |
| `Live` | `Short` | `6.25` | 10,810,000.00 USD | 439.10 USD | 0.00 USD | `+43.86%` | `70.20` |
| `Live` | `Short` | `6.26` | 11,070,000.00 USD | 256,050.00 USD | 0.00 USD | `+44.09%` | `40,869.30` |
| `Live` | `Short` | `6.30` | 11,070,000.00 USD | 2,020.00 USD | 0.00 USD | `+45.01%` | `320.30` |
| `Live` | `Short` | `6.32` | 11,080,000.00 USD | 8,430.00 USD | 0.00 USD | `+45.24%` | `1,335.70` |
| `Live` | `Short` | `6.33` | 11,080,000.00 USD | 382.00 USD | 0.00 USD | `+45.70%` | `60.30` |
| `Live` | `Short` | `6.34` | 11,080,000.00 USD | 214.46 USD | 0.00 USD | `+45.93%` | `33.80` |
| `Live` | `Short` | `6.37` | 11,080,000.00 USD | 113.93 USD | 0.00 USD | `+46.39%` | `17.90` |
| `Live` | `Short` | `6.38` | 11,080,000.00 USD | 288.15 USD | 0.00 USD | `+46.62%` | `45.20` |
| `Live` | `Short` | `6.39` | 11,080,000.00 USD | 2,000.00 USD | 0.00 USD | `+47.08%` | `312.80` |
| `Live` | `Short` | `6.41` | 11,100,000.00 USD | 15,590.00 USD | 0.00 USD | `+47.31%` | `2,434.70` |
| `Live` | `Short` | `6.42` | 11,100,000.00 USD | 943.65 USD | 0.00 USD | `+47.54%` | `147.10` |
| `Live` | `Short` | `6.42` | 11,110,000.00 USD | 5,650.00 USD | 0.00 USD | `+47.77%` | `879.80` |
| `Live` | `Short` | `6.45` | 11,110,000.00 USD | 5,270.00 USD | 0.00 USD | `+48.23%` | `818.40` |
| `Live` | `Short` | `6.46` | 11,120,000.00 USD | 7,150.00 USD | 0.00 USD | `+48.46%` | `1,107.10` |
| `Live` | `Short` | `6.46` | 11,120,000.00 USD | 1,940.00 USD | 0.00 USD | `+48.69%` | `300.00` |
| `Live` | `Short` | `6.51` | 11,120,000.00 USD | 380.48 USD | 0.00 USD | `+49.84%` | `58.40` |
| `Live` | `Short` | `6.54` | 12,360,000.00 USD | 1,240,000.00 USD | 0.00 USD | `+50.53%` | `189,207.50` |
| `Live` | `Short` | `6.57` | 41,950,000.00 USD | 29,590,000.00 USD | 0.00 USD | `+50.99%` | `4,507,262.50` |
| `Live` | `Short` | `6.59` | 41,950,000.00 USD | 418.78 USD | 0.00 USD | `+51.68%` | `63.50` |
| `Live` | `Short` | `6.61` | 42,330,000.00 USD | 382,680.00 USD | 0.00 USD | `+51.91%` | `57,938.40` |
| `Live` | `Short` | `6.64` | 42,370,000.00 USD | 41,250.00 USD | 0.00 USD | `+52.83%` | `6,207.00` |
| `Live` | `Short` | `6.66` | 42,380,000.00 USD | 7,230.00 USD | 0.00 USD | `+53.06%` | `1,086.90` |
| `Live` | `Short` | `6.67` | 42,380,000.00 USD | 233.94 USD | 0.00 USD | `+53.29%` | `35.10` |
| `Live` | `Short` | `6.67` | 42,380,000.00 USD | 200.25 USD | 0.00 USD | `+53.52%` | `30.00` |
| `Live` | `Short` | `6.71` | 42,420,000.00 USD | 37,260.00 USD | 0.00 USD | `+54.21%` | `5,556.90` |
| `Live` | `Short` | `6.72` | 42,420,000.00 USD | 713.52 USD | 0.00 USD | `+54.67%` | `106.10` |
| `Live` | `Short` | `6.75` | 43,670,000.00 USD | 1,250,000.00 USD | 0.00 USD | `+55.36%` | `184,501.00` |
| `Live` | `Short` | `6.80` | 43,670,000.00 USD | 5,260.00 USD | 0.00 USD | `+56.51%` | `772.70` |
| `Live` | `Short` | `6.82` | 43,670,000.00 USD | 344.16 USD | 0.00 USD | `+56.74%` | `50.50` |
| `Live` | `Short` | `6.83` | 43,760,000.00 USD | 91,230.00 USD | 0.00 USD | `+56.97%` | `13,367.10` |
| `Live` | `Short` | `6.84` | 43,760,000.00 USD | 753.63 USD | 0.00 USD | `+57.43%` | `110.10` |
| `Live` | `Short` | `6.87` | 43,770,000.00 USD | 2,650.00 USD | 0.00 USD | `+57.89%` | `386.60` |
| `Live` | `Short` | `6.92` | 43,770,000.00 USD | 6,920.00 USD | 0.00 USD | `+59.27%` | `1,000.00` |
| `Live` | `Short` | `6.96` | 43,800,000.00 USD | 24,540.00 USD | 0.00 USD | `+60.19%` | `3,523.00` |
| `Live` | `Short` | `6.99` | 43,800,000.00 USD | 664.27 USD | 0.00 USD | `+60.65%` | `95.10` |
| `Live` | `Short` | `7.03` | 43,800,000.00 USD | 665.27 USD | 0.00 USD | `+61.57%` | `94.70` |
| `Live` | `Short` | `7.08` | 43,800,000.00 USD | 996.15 USD | 0.00 USD | `+62.95%` | `140.60` |
| `Live` | `Short` | `7.09` | 43,800,000.00 USD | 699.57 USD | 0.00 USD | `+63.18%` | `98.60` |
| `Live` | `Short` | `7.14` | 43,820,000.00 USD | 15,990.00 USD | 0.00 USD | `+64.33%` | `2,237.40` |
| `Live` | `Short` | `7.21` | 43,830,000.00 USD | 13,560.00 USD | 0.00 USD | `+65.94%` | `1,879.60` |
| `Live` | `Short` | `7.24` | 47,670,000.00 USD | 3,840,000.00 USD | 0.00 USD | `+66.40%` | `531,159.30` |
| `Live` | `Short` | `7.25` | 47,680,000.00 USD | 3,770.00 USD | 0.00 USD | `+66.63%` | `520.00` |
| `Live` | `Short` | `7.25` | 47,680,000.00 USD | 575.32 USD | 0.00 USD | `+66.86%` | `79.30` |
| `Live` | `Short` | `7.30` | 47,680,000.00 USD | 3,520.00 USD | 0.00 USD | `+68.01%` | `481.50` |
| `Live` | `Short` | `7.32` | 47,730,000.00 USD | 54,860.00 USD | 0.00 USD | `+68.24%` | `7,500.00` |
| `Live` | `Short` | `7.33` | 47,740,000.00 USD | 1,320.00 USD | 0.00 USD | `+68.70%` | `180.00` |
| `Live` | `Short` | `7.34` | 47,800,000.00 USD | 59,770.00 USD | 0.00 USD | `+68.93%` | `8,137.40` |
| `Live` | `Short` | `7.38` | 47,810,000.00 USD | 12,910.00 USD | 0.00 USD | `+69.62%` | `1,750.00` |
| `Live` | `Short` | `7.41` | 47,810,000.00 USD | 776.04 USD | 0.00 USD | `+70.31%` | `104.80` |
| `Live` | `Short` | `7.43` | 47,920,000.00 USD | 106,150.00 USD | 0.00 USD | `+71.00%` | `14,276.50` |
| `Live` | `Short` | `7.46` | 47,920,000.00 USD | 1,420.00 USD | 0.00 USD | `+71.46%` | `191.10` |
| `Live` | `Short` | `7.46` | 57,890,000.00 USD | 9,970,000.00 USD | 0.00 USD | `+71.69%` | `1,336,000.00` |
| `Live` | `Short` | `7.53` | 65,720,000.00 USD | 7,820,000.00 USD | 0.00 USD | `+73.07%` | `1,039,813.00` |
| `Live` | `Short` | `7.54` | 65,720,000.00 USD | 3,100.00 USD | 0.00 USD | `+73.30%` | `411.40` |
| `Live` | `Short` | `7.62` | 65,750,000.00 USD | 35,860.00 USD | 0.00 USD | `+75.14%` | `4,708.50` |
| `Live` | `Short` | `7.63` | 65,770,000.00 USD | 19,210.00 USD | 0.00 USD | `+75.60%` | `2,516.10` |
| `Live` | `Short` | `7.64` | 65,800,000.00 USD | 23,890.00 USD | 0.00 USD | `+75.83%` | `3,124.90` |
| `Live` | `Short` | `7.66` | 65,820,000.00 USD | 20,000.00 USD | 0.00 USD | `+76.06%` | `2,612.80` |
| `Live` | `Short` | `7.67` | 65,840,000.00 USD | 27,160.00 USD | 0.00 USD | `+76.29%` | `3,543.50` |
| `Live` | `Short` | `7.72` | 65,840,000.00 USD | 259.56 USD | 0.00 USD | `+77.67%` | `33.60` |
| `Live` | `Short` | `7.74` | 65,850,000.00 USD | 4,970.00 USD | 0.00 USD | `+77.90%` | `642.60` |
| `Live` | `Short` | `7.75` | 65,850,000.00 USD | 629.67 USD | 0.00 USD | `+78.13%` | `81.30` |
| `Live` | `Short` | `7.76` | 65,860,000.00 USD | 11,760.00 USD | 0.00 USD | `+78.59%` | `1,514.20` |
| `Live` | `Short` | `7.82` | 65,860,000.00 USD | 1,690.00 USD | 0.00 USD | `+79.74%` | `216.50` |
| `Live` | `Short` | `7.86` | 65,860,000.00 USD | 120.18 USD | 0.00 USD | `+80.66%` | `15.30` |
| `Live` | `Short` | `7.87` | 65,870,000.00 USD | 2,980.00 USD | 0.00 USD | `+80.89%` | `378.70` |
| `Live` | `Short` | `7.95` | 65,870,000.00 USD | 6,120.00 USD | 0.00 USD | `+82.73%` | `769.80` |
| `Live` | `Short` | `7.96` | 65,870,000.00 USD | 166.26 USD | 0.00 USD | `+82.96%` | `20.90` |
| `Live` | `Short` | `7.96` | 65,970,000.00 USD | 95,580.00 USD | 0.00 USD | `+83.19%` | `12,000.00` |
| `Live` | `Short` | `7.99` | 65,970,000.00 USD | 399.25 USD | 0.00 USD | `+83.65%` | `50.00` |
| `Live` | `Short` | `8.03` | 66,400,000.00 USD | 435,420.00 USD | 0.00 USD | `+84.57%` | `54,257.40` |
| `Live` | `Short` | `8.04` | 66,400,000.00 USD | 259.05 USD | 0.00 USD | `+85.03%` | `32.20` |
| `Live` | `Short` | `8.07` | 66,410,000.00 USD | 6,460.00 USD | 0.00 USD | `+85.72%` | `800.00` |
| `Live` | `Short` | `8.20` | 66,410,000.00 USD | 951.44 USD | 0.00 USD | `+88.48%` | `116.10` |
| `Live` | `Short` | `8.24` | 66,480,000.00 USD | 62,980.00 USD | 0.00 USD | `+89.63%` | `7,638.50` |
| `Live` | `Short` | `8.31` | 66,480,000.00 USD | 8,640.00 USD | 0.00 USD | `+91.24%` | `1,039.60` |
| `Live` | `Short` | `8.35` | 66,510,000.00 USD | 25,310.00 USD | 0.00 USD | `+91.93%` | `3,032.60` |
| `Live` | `Short` | `8.37` | 67,610,000.00 USD | 1,100,000.00 USD | 0.00 USD | `+92.39%` | `131,528.10` |
| `Live` | `Short` | `8.38` | 67,610,000.00 USD | 191.79 USD | 0.00 USD | `+92.62%` | `22.90` |
| `Live` | `Short` | `8.41` | 67,610,000.00 USD | 1,220.00 USD | 0.00 USD | `+93.54%` | `145.00` |
| `Live` | `Short` | `8.46` | 67,660,000.00 USD | 53,330.00 USD | 0.00 USD | `+94.69%` | `6,300.00` |
| `Live` | `Short` | `8.47` | 67,660,000.00 USD | 816.99 USD | 0.00 USD | `+94.92%` | `96.40` |
| `Live` | `Short` | `8.48` | 67,670,000.00 USD | 6,640.00 USD | 0.00 USD | `+95.15%` | `782.50` |
| `Live` | `Short` | `8.49` | 67,700,000.00 USD | 25,490.00 USD | 0.00 USD | `+95.38%` | `3,000.00` |
| `Live` | `Short` | `8.53` | 67,730,000.00 USD | 34,680.00 USD | 0.00 USD | `+96.07%` | `4,068.00` |
| `Live` | `Short` | `8.54` | 67,730,000.00 USD | 127.17 USD | 0.00 USD | `+96.30%` | `14.90` |
| `Live` | `Short` | `8.54` | 67,730,000.00 USD | 124.76 USD | 0.00 USD | `+96.53%` | `14.60` |
| `Live` | `Short` | `8.55` | 68,160,000.00 USD | 430,710.00 USD | 0.00 USD | `+96.76%` | `50,346.40` |
| `Live` | `Short` | `8.59` | 68,160,000.00 USD | 240.38 USD | 0.00 USD | `+97.45%` | `28.00` |
| `Live` | `Short` | `8.60` | 68,180,000.00 USD | 17,660.00 USD | 0.00 USD | `+97.68%` | `2,054.80` |
| `Live` | `Short` | `8.68` | 68,180,000.00 USD | 2,320.00 USD | 0.00 USD | `+99.52%` | `267.10` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `1.00` | 3,270,000.00 USD | 0.00 USD | 585.51 USD | `-76.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.01` | 3,270,000.00 USD | 0.00 USD | 339.82 USD | `-76.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.20` | 3,270,000.00 USD | 0.00 USD | 196.58 USD | `-72.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.34` | 3,270,000.00 USD | 0.00 USD | 331.54 USD | `-69.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.35` | 3,270,000.00 USD | 0.00 USD | 345.25 USD | `-68.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.38` | 3,270,000.00 USD | 0.00 USD | 5,640.00 USD | `-68.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.40` | 3,260,000.00 USD | 0.00 USD | 997.29 USD | `-67.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.49` | 3,260,000.00 USD | 0.00 USD | 582.71 USD | `-65.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.51` | 3,260,000.00 USD | 0.00 USD | 139.83 USD | `-65.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.53` | 3,260,000.00 USD | 0.00 USD | 113.28 USD | `-64.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.54` | 3,260,000.00 USD | 0.00 USD | 4,000.00 USD | `-64.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.55` | 3,260,000.00 USD | 0.00 USD | 324.22 USD | `-64.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.59` | 3,260,000.00 USD | 0.00 USD | 4,590.00 USD | `-63.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.61` | 3,250,000.00 USD | 0.00 USD | 739.67 USD | `-62.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.62` | 3,250,000.00 USD | 0.00 USD | 1,740.00 USD | `-62.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.64` | 3,250,000.00 USD | 0.00 USD | 6,260.00 USD | `-62.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.66` | 3,240,000.00 USD | 0.00 USD | 345.40 USD | `-61.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.68` | 3,240,000.00 USD | 0.00 USD | 167.50 USD | `-61.48%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.70` | 3,240,000.00 USD | 0.00 USD | 669.02 USD | `-61.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.71` | 3,240,000.00 USD | 0.00 USD | 105.88 USD | `-60.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.73` | 3,240,000.00 USD | 0.00 USD | 172.50 USD | `-60.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.77` | 3,240,000.00 USD | 0.00 USD | 10,650.00 USD | `-59.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.80` | 3,230,000.00 USD | 0.00 USD | 722.00 USD | `-58.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.81` | 3,230,000.00 USD | 0.00 USD | 259.00 USD | `-58.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.82` | 3,230,000.00 USD | 0.00 USD | 103.84 USD | `-58.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.83` | 3,230,000.00 USD | 0.00 USD | 109.00 USD | `-57.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.88` | 3,230,000.00 USD | 0.00 USD | 222.19 USD | `-56.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.89` | 3,230,000.00 USD | 0.00 USD | 10,280.00 USD | `-56.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.91` | 3,220,000.00 USD | 0.00 USD | 558.36 USD | `-56.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.93` | 3,220,000.00 USD | 0.00 USD | 1,520.00 USD | `-55.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.94` | 3,220,000.00 USD | 0.00 USD | 222.14 USD | `-55.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.95` | 3,220,000.00 USD | 0.00 USD | 279.50 USD | `-55.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.98` | 3,220,000.00 USD | 0.00 USD | 197.50 USD | `-54.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.00` | 3,220,000.00 USD | 0.00 USD | 935.66 USD | `-54.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.00` | 3,220,000.00 USD | 0.00 USD | 18,860.00 USD | `-53.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.02` | 3,200,000.00 USD | 0.00 USD | 3,020.00 USD | `-53.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.04` | 3,190,000.00 USD | 0.00 USD | 214.52 USD | `-52.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.06` | 3,190,000.00 USD | 0.00 USD | 1,200.00 USD | `-52.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.06` | 3,190,000.00 USD | 0.00 USD | 578.41 USD | `-52.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.10` | 3,190,000.00 USD | 0.00 USD | 18,070.00 USD | `-51.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.10` | 3,170,000.00 USD | 0.00 USD | 108.62 USD | `-51.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.12` | 3,170,000.00 USD | 0.00 USD | 107.23 USD | `-51.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.12` | 3,170,000.00 USD | 0.00 USD | 1,590.00 USD | `-51.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.15` | 3,170,000.00 USD | 0.00 USD | 5,830.00 USD | `-50.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.15` | 3,170,000.00 USD | 0.00 USD | 310.32 USD | `-50.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.17` | 3,170,000.00 USD | 0.00 USD | 1,170.00 USD | `-50.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.19` | 3,170,000.00 USD | 0.00 USD | 576.18 USD | `-49.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.19` | 3,160,000.00 USD | 0.00 USD | 295.67 USD | `-49.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.21` | 3,160,000.00 USD | 0.00 USD | 1,430.00 USD | `-49.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.21` | 3,160,000.00 USD | 0.00 USD | 812.68 USD | `-49.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.23` | 3,160,000.00 USD | 0.00 USD | 1,440.00 USD | `-48.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.23` | 3,160,000.00 USD | 0.00 USD | 106.16 USD | `-48.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.25` | 3,160,000.00 USD | 0.00 USD | 6,270.00 USD | `-48.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.25` | 3,150,000.00 USD | 0.00 USD | 478.06 USD | `-48.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.27` | 3,150,000.00 USD | 0.00 USD | 540.88 USD | `-47.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.27` | 3,150,000.00 USD | 0.00 USD | 867.46 USD | `-47.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.29` | 3,150,000.00 USD | 0.00 USD | 759.76 USD | `-47.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.29` | 3,150,000.00 USD | 0.00 USD | 11,060.00 USD | `-47.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.31` | 3,140,000.00 USD | 0.00 USD | 3,690.00 USD | `-46.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.33` | 3,140,000.00 USD | 0.00 USD | 722.15 USD | `-46.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.33` | 3,140,000.00 USD | 0.00 USD | 467.00 USD | `-46.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.35` | 3,140,000.00 USD | 0.00 USD | 506.75 USD | `-46.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.37` | 3,140,000.00 USD | 0.00 USD | 214.27 USD | `-45.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.38` | 3,140,000.00 USD | 0.00 USD | 428.69 USD | `-45.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.38` | 3,130,000.00 USD | 0.00 USD | 322.45 USD | `-45.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.40` | 3,130,000.00 USD | 0.00 USD | 108.25 USD | `-44.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.40` | 3,130,000.00 USD | 0.00 USD | 3,900.00 USD | `-44.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.42` | 3,130,000.00 USD | 0.00 USD | 799.04 USD | `-44.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.44` | 3,130,000.00 USD | 0.00 USD | 6,830.00 USD | `-44.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.44` | 3,120,000.00 USD | 0.00 USD | 137.16 USD | `-43.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.48` | 3,120,000.00 USD | 0.00 USD | 504.41 USD | `-43.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.48` | 3,120,000.00 USD | 0.00 USD | 963.93 USD | `-42.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.50` | 3,120,000.00 USD | 0.00 USD | 6,690.00 USD | `-42.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.52` | 3,110,000.00 USD | 0.00 USD | 541.98 USD | `-42.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.54` | 3,110,000.00 USD | 0.00 USD | 108.75 USD | `-41.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.54` | 3,110,000.00 USD | 0.00 USD | 766.55 USD | `-41.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.56` | 3,110,000.00 USD | 0.00 USD | 7,110.00 USD | `-41.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.58` | 3,110,000.00 USD | 0.00 USD | 1,100.00 USD | `-40.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.58` | 3,100,000.00 USD | 0.00 USD | 100.04 USD | `-40.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.60` | 3,100,000.00 USD | 0.00 USD | 390.75 USD | `-40.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.62` | 3,100,000.00 USD | 0.00 USD | 5,090.00 USD | `-39.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.67` | 3,100,000.00 USD | 0.00 USD | 226.57 USD | `-38.48%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.69` | 3,100,000.00 USD | 0.00 USD | 104.98 USD | `-38.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.69` | 3,100,000.00 USD | 0.00 USD | 889.89 USD | `-38.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.71` | 3,100,000.00 USD | 0.00 USD | 7,270.00 USD | `-37.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.73` | 3,090,000.00 USD | 0.00 USD | 107.21 USD | `-37.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.75` | 3,090,000.00 USD | 0.00 USD | 197.37 USD | `-36.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.75` | 3,090,000.00 USD | 0.00 USD | 8,110.00 USD | `-36.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.77` | 3,080,000.00 USD | 0.00 USD | 108.39 USD | `-36.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.77` | 3,080,000.00 USD | 0.00 USD | 435.95 USD | `-36.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.79` | 3,080,000.00 USD | 0.00 USD | 217.23 USD | `-35.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.79` | 3,080,000.00 USD | 0.00 USD | 437.98 USD | `-35.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.81` | 3,080,000.00 USD | 0.00 USD | 1,230.00 USD | `-35.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.83` | 3,080,000.00 USD | 0.00 USD | 8,380.00 USD | `-35.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.83` | 3,070,000.00 USD | 0.00 USD | 283.50 USD | `-34.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.85` | 3,070,000.00 USD | 0.00 USD | 109.53 USD | `-34.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.85` | 3,070,000.00 USD | 0.00 USD | 1,230.00 USD | `-34.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.88` | 3,070,000.00 USD | 0.00 USD | 1,960.00 USD | `-33.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.88` | 3,070,000.00 USD | 0.00 USD | 157.81 USD | `-33.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.90` | 3,070,000.00 USD | 0.00 USD | 4,190.00 USD | `-33.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.90` | 3,060,000.00 USD | 0.00 USD | 4,870.00 USD | `-33.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.92` | 3,060,000.00 USD | 0.00 USD | 1,320.00 USD | `-32.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.92` | 3,060,000.00 USD | 0.00 USD | 1,090.00 USD | `-32.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.94` | 3,060,000.00 USD | 0.00 USD | 1,560.00 USD | `-32.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.94` | 3,050,000.00 USD | 0.00 USD | 24,200.00 USD | `-32.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.96` | 3,030,000.00 USD | 0.00 USD | 738.75 USD | `-32.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.96` | 3,030,000.00 USD | 0.00 USD | 523.32 USD | `-31.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.98` | 3,030,000.00 USD | 0.00 USD | 4,470.00 USD | `-31.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.00` | 3,020,000.00 USD | 0.00 USD | 24,210.00 USD | `-30.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.02` | 3,000,000.00 USD | 0.00 USD | 1,020.00 USD | `-30.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.04` | 3,000,000.00 USD | 0.00 USD | 214.57 USD | `-30.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.04` | 3,000,000.00 USD | 0.00 USD | 249.08 USD | `-29.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.06` | 3,000,000.00 USD | 0.00 USD | 305.50 USD | `-29.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.06` | 3,000,000.00 USD | 0.00 USD | 109.42 USD | `-29.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.10` | 3,000,000.00 USD | 0.00 USD | 9,300.00 USD | `-28.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.12` | 2,990,000.00 USD | 0.00 USD | 8,570.00 USD | `-28.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.12` | 2,980,000.00 USD | 0.00 USD | 104.69 USD | `-28.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.13` | 2,980,000.00 USD | 0.00 USD | 315.69 USD | `-27.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.15` | 2,980,000.00 USD | 0.00 USD | 214.17 USD | `-27.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.15` | 2,980,000.00 USD | 0.00 USD | 329.07 USD | `-27.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.17` | 2,980,000.00 USD | 0.00 USD | 4,210.00 USD | `-27.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.17` | 2,980,000.00 USD | 0.00 USD | 1,030.00 USD | `-26.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.19` | 2,970,000.00 USD | 0.00 USD | 218.81 USD | `-26.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.21` | 2,970,000.00 USD | 0.00 USD | 24,840.00 USD | `-26.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.21` | 2,950,000.00 USD | 0.00 USD | 144.67 USD | `-26.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.23` | 2,950,000.00 USD | 0.00 USD | 273,030.00 USD | `-25.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.25` | 2,680,000.00 USD | 0.00 USD | 27,380.00 USD | `-25.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.25` | 2,650,000.00 USD | 0.00 USD | 1,560.00 USD | `-25.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.27` | 2,650,000.00 USD | 0.00 USD | 104.81 USD | `-24.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.27` | 2,650,000.00 USD | 0.00 USD | 200.10 USD | `-24.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.29` | 2,650,000.00 USD | 0.00 USD | 1,480.00 USD | `-24.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.29` | 2,650,000.00 USD | 0.00 USD | 1,870.00 USD | `-24.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.31` | 2,640,000.00 USD | 0.00 USD | 18,240.00 USD | `-23.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.31` | 2,630,000.00 USD | 0.00 USD | 240.67 USD | `-23.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.33` | 2,630,000.00 USD | 0.00 USD | 306.56 USD | `-23.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.33` | 2,630,000.00 USD | 0.00 USD | 1,670.00 USD | `-23.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.37` | 2,620,000.00 USD | 0.00 USD | 73,220.00 USD | `-22.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.38` | 2,550,000.00 USD | 0.00 USD | 19,600.00 USD | `-22.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.40` | 2,530,000.00 USD | 0.00 USD | 8,490.00 USD | `-21.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.40` | 2,520,000.00 USD | 0.00 USD | 102,530.00 USD | `-21.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.42` | 2,420,000.00 USD | 0.00 USD | 421.41 USD | `-21.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.42` | 2,420,000.00 USD | 0.00 USD | 4,350.00 USD | `-21.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.44` | 2,410,000.00 USD | 0.00 USD | 444.49 USD | `-21.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.44` | 2,410,000.00 USD | 0.00 USD | 2,550.00 USD | `-20.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.46` | 2,410,000.00 USD | 0.00 USD | 1,380.00 USD | `-20.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.46` | 2,410,000.00 USD | 0.00 USD | 344.07 USD | `-20.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.48` | 2,410,000.00 USD | 0.00 USD | 24,320.00 USD | `-20.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.48` | 2,390,000.00 USD | 0.00 USD | 17,430.00 USD | `-19.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.50` | 2,370,000.00 USD | 0.00 USD | 894.72 USD | `-19.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.50` | 2,370,000.00 USD | 0.00 USD | 70,280.00 USD | `-19.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.52` | 2,300,000.00 USD | 0.00 USD | 21,320.00 USD | `-19.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.52` | 2,280,000.00 USD | 0.00 USD | 3,700.00 USD | `-18.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.54` | 2,270,000.00 USD | 0.00 USD | 16,250.00 USD | `-18.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.54` | 2,260,000.00 USD | 0.00 USD | 5,130.00 USD | `-18.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.56` | 2,250,000.00 USD | 0.00 USD | 1,800.00 USD | `-18.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.56` | 2,250,000.00 USD | 0.00 USD | 18,440.00 USD | `-18.01%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.58` | 2,230,000.00 USD | 0.00 USD | 78,170.00 USD | `-17.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.58` | 2,150,000.00 USD | 0.00 USD | 1,610.00 USD | `-17.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.60` | 2,150,000.00 USD | 0.00 USD | 331.46 USD | `-17.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.60` | 2,150,000.00 USD | 0.00 USD | 56,250.00 USD | `-17.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.62` | 2,090,000.00 USD | 0.00 USD | 632.99 USD | `-16.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.62` | 2,090,000.00 USD | 0.00 USD | 1,000.00 USD | `-16.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.63` | 2,090,000.00 USD | 0.00 USD | 1,210.00 USD | `-16.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.65` | 2,090,000.00 USD | 0.00 USD | 54,670.00 USD | `-16.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.65` | 2,040,000.00 USD | 0.00 USD | 8,030.00 USD | `-15.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.67` | 2,030,000.00 USD | 0.00 USD | 4,070.00 USD | `-15.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.67` | 2,020,000.00 USD | 0.00 USD | 367.50 USD | `-15.48%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.69` | 2,020,000.00 USD | 0.00 USD | 32,620.00 USD | `-15.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.69` | 1,990,000.00 USD | 0.00 USD | 4,370.00 USD | `-15.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.71` | 1,990,000.00 USD | 0.00 USD | 391,610.00 USD | `-14.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.71` | 1,600,000.00 USD | 0.00 USD | 6,300.00 USD | `-14.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.73` | 1,590,000.00 USD | 0.00 USD | 821.36 USD | `-14.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.73` | 1,590,000.00 USD | 0.00 USD | 32,040.00 USD | `-14.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.75` | 1,560,000.00 USD | 0.00 USD | 28,820.00 USD | `-13.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.75` | 1,530,000.00 USD | 0.00 USD | 14,490.00 USD | `-13.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.77` | 1,510,000.00 USD | 0.00 USD | 6,850.00 USD | `-13.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.77` | 1,510,000.00 USD | 0.00 USD | 1,190.00 USD | `-13.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.79` | 1,510,000.00 USD | 0.00 USD | 1,660.00 USD | `-12.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.79` | 1,500,000.00 USD | 0.00 USD | 166,450.00 USD | `-12.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.81` | 1,340,000.00 USD | 0.00 USD | 4,530.00 USD | `-12.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.81` | 1,330,000.00 USD | 0.00 USD | 22,340.00 USD | `-12.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.83` | 1,310,000.00 USD | 0.00 USD | 7,350.00 USD | `-12.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.83` | 1,300,000.00 USD | 0.00 USD | 41,340.00 USD | `-11.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.85` | 1,260,000.00 USD | 0.00 USD | 43,060.00 USD | `-11.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.85` | 1,220,000.00 USD | 0.00 USD | 16,170.00 USD | `-11.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.87` | 1,200,000.00 USD | 0.00 USD | 8,380.00 USD | `-11.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.88` | 1,190,000.00 USD | 0.00 USD | 161,230.00 USD | `-10.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.88` | 1,030,000.00 USD | 0.00 USD | 27,360.00 USD | `-10.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.90` | 1,010,000.00 USD | 0.00 USD | 10,330.00 USD | `-10.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.90` | 994,820.00 USD | 0.00 USD | 46,610.00 USD | `-10.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.92` | 948,220.00 USD | 0.00 USD | 2,340.00 USD | `-9.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.92` | 945,880.00 USD | 0.00 USD | 6,910.00 USD | `-9.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.94` | 938,970.00 USD | 0.00 USD | 934.17 USD | `-9.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.94` | 938,040.00 USD | 0.00 USD | 3,940.00 USD | `-9.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.96` | 934,100.00 USD | 0.00 USD | 2,780.00 USD | `-9.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.96` | 931,320.00 USD | 0.00 USD | 22,700.00 USD | `-8.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.98` | 908,620.00 USD | 0.00 USD | 791.02 USD | `-8.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.98` | 907,830.00 USD | 0.00 USD | 42,280.00 USD | `-8.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.00` | 865,550.00 USD | 0.00 USD | 667.16 USD | `-8.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.00` | 864,880.00 USD | 0.00 USD | 179,460.00 USD | `-7.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.01` | 685,420.00 USD | 0.00 USD | 9,720.00 USD | `-7.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.03` | 675,700.00 USD | 0.00 USD | 58,180.00 USD | `-7.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.04` | 617,520.00 USD | 0.00 USD | 428.11 USD | `-7.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.04` | 617,090.00 USD | 0.00 USD | 919.83 USD | `-6.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.05` | 616,170.00 USD | 0.00 USD | 71,120.00 USD | `-6.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.07` | 545,060.00 USD | 0.00 USD | 113.41 USD | `-6.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.08` | 544,940.00 USD | 0.00 USD | 3,880.00 USD | `-6.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.08` | 541,070.00 USD | 0.00 USD | 6,340.00 USD | `-6.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.09` | 534,730.00 USD | 0.00 USD | 11,540.00 USD | `-5.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.11` | 523,190.00 USD | 0.00 USD | 30,490.00 USD | `-5.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.12` | 492,700.00 USD | 0.00 USD | 89,870.00 USD | `-5.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.12` | 402,830.00 USD | 0.00 USD | 11,940.00 USD | `-5.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.13` | 390,900.00 USD | 0.00 USD | 54,000.00 USD | `-4.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.14` | 336,900.00 USD | 0.00 USD | 16,900.00 USD | `-4.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.16` | 320,000.00 USD | 0.00 USD | 56,810.00 USD | `-4.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.17` | 263,190.00 USD | 0.00 USD | 20,560.00 USD | `-4.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.17` | 242,630.00 USD | 0.00 USD | 1,220.00 USD | `-3.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.18` | 241,410.00 USD | 0.00 USD | 13,390.00 USD | `-3.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.20` | 228,020.00 USD | 0.00 USD | 126.69 USD | `-3.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.21` | 227,900.00 USD | 0.00 USD | 62,370.00 USD | `-3.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.21` | 165,530.00 USD | 0.00 USD | 982.52 USD | `-3.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.22` | 164,550.00 USD | 0.00 USD | 1,130.00 USD | `-2.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.24` | 163,410.00 USD | 0.00 USD | 18,180.00 USD | `-2.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.25` | 145,230.00 USD | 0.00 USD | 5,190.00 USD | `-2.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.25` | 140,040.00 USD | 0.00 USD | 23,900.00 USD | `-2.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.26` | 116,140.00 USD | 0.00 USD | 2,390.00 USD | `-1.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.28` | 113,750.00 USD | 0.00 USD | 1,200.00 USD | `-1.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.29` | 112,550.00 USD | 0.00 USD | 143.98 USD | `-1.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.29` | 112,400.00 USD | 0.00 USD | 34,570.00 USD | `-1.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.30` | 77,840.00 USD | 0.00 USD | 19,320.00 USD | `-0.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.32` | 58,520.00 USD | 0.00 USD | 39,760.00 USD | `-0.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.33` | 18,760.00 USD | 0.00 USD | 182.52 USD | `-0.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.33` | 18,570.00 USD | 0.00 USD | 1,190.00 USD | `-0.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.34` | 17,380.00 USD | 0.00 USD | 17,380.00 USD | `-0.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.36` | 15,410.00 USD | 15,410.00 USD | 0.00 USD | `+0.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.37` | 176,430.00 USD | 161,010.00 USD | 0.00 USD | `+0.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.38` | 266,060.00 USD | 89,630.00 USD | 0.00 USD | `+0.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.38` | 334,170.00 USD | 68,110.00 USD | 0.00 USD | `+0.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.39` | 515,130.00 USD | 180,960.00 USD | 0.00 USD | `+1.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.41` | 537,170.00 USD | 22,050.00 USD | 0.00 USD | `+1.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.42` | 540,880.00 USD | 3,710.00 USD | 0.00 USD | `+1.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.42` | 543,860.00 USD | 2,970.00 USD | 0.00 USD | `+1.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.43` | 551,490.00 USD | 7,640.00 USD | 0.00 USD | `+2.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.45` | 552,600.00 USD | 1,110.00 USD | 0.00 USD | `+2.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.46` | 621,280.00 USD | 68,670.00 USD | 0.00 USD | `+2.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.46` | 628,110.00 USD | 6,830.00 USD | 0.00 USD | `+2.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.47` | 628,490.00 USD | 375.90 USD | 0.00 USD | `+2.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.49` | 629,800.00 USD | 1,310.00 USD | 0.00 USD | `+3.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.50` | 637,260.00 USD | 7,460.00 USD | 0.00 USD | `+3.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.50` | 648,610.00 USD | 11,350.00 USD | 0.00 USD | `+3.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.51` | 667,550.00 USD | 18,940.00 USD | 0.00 USD | `+3.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.53` | 774,330.00 USD | 106,780.00 USD | 0.00 USD | `+4.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.54` | 775,030.00 USD | 699.75 USD | 0.00 USD | `+4.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.54` | 775,940.00 USD | 909.00 USD | 0.00 USD | `+4.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.55` | 777,130.00 USD | 1,190.00 USD | 0.00 USD | `+4.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.57` | 777,520.00 USD | 388.48 USD | 0.00 USD | `+4.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.58` | 778,580.00 USD | 1,060.00 USD | 0.00 USD | `+5.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.58` | 779,340.00 USD | 759.73 USD | 0.00 USD | `+5.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.59` | 807,700.00 USD | 28,360.00 USD | 0.00 USD | `+5.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.61` | 928,310.00 USD | 120,610.00 USD | 0.00 USD | `+5.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.62` | 929,060.00 USD | 742.55 USD | 0.00 USD | `+6.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.62` | 950,510.00 USD | 21,450.00 USD | 0.00 USD | `+6.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.63` | 951,610.00 USD | 1,100.00 USD | 0.00 USD | `+6.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.64` | 955,680.00 USD | 4,070.00 USD | 0.00 USD | `+6.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.66` | 956,920.00 USD | 1,240.00 USD | 0.00 USD | `+7.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.67` | 1,030,000.00 USD | 77,690.00 USD | 0.00 USD | `+7.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.67` | 1,040,000.00 USD | 617.10 USD | 0.00 USD | `+7.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.68` | 1,050,000.00 USD | 15,710.00 USD | 0.00 USD | `+7.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.70` | 1,050,000.00 USD | 152.12 USD | 0.00 USD | `+7.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.71` | 1,480,000.00 USD | 429,960.00 USD | 0.00 USD | `+8.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.71` | 1,720,000.00 USD | 234,370.00 USD | 0.00 USD | `+8.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.72` | 1,720,000.00 USD | 2,650.00 USD | 0.00 USD | `+8.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.74` | 1,800,000.00 USD | 84,180.00 USD | 0.00 USD | `+8.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.75` | 1,810,000.00 USD | 6,160.00 USD | 0.00 USD | `+9.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.75` | 1,840,000.00 USD | 29,420.00 USD | 0.00 USD | `+9.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.76` | 1,850,000.00 USD | 13,030.00 USD | 0.00 USD | `+9.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.78` | 1,850,000.00 USD | 2,640.00 USD | 0.00 USD | `+9.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.79` | 2,670,000.00 USD | 818,540.00 USD | 0.00 USD | `+10.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.79` | 2,670,000.00 USD | 559.58 USD | 0.00 USD | `+10.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.80` | 2,850,000.00 USD | 175,870.00 USD | 0.00 USD | `+10.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.82` | 2,880,000.00 USD | 33,510.00 USD | 0.00 USD | `+10.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.83` | 2,890,000.00 USD | 8,540.00 USD | 0.00 USD | `+10.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.83` | 2,980,000.00 USD | 93,100.00 USD | 0.00 USD | `+11.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.84` | 3,040,000.00 USD | 59,460.00 USD | 0.00 USD | `+11.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.86` | 3,070,000.00 USD | 24,370.00 USD | 0.00 USD | `+11.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.87` | 3,090,000.00 USD | 23,180.00 USD | 0.00 USD | `+11.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.88` | 3,100,000.00 USD | 10,400.00 USD | 0.00 USD | `+12.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.88` | 3,120,000.00 USD | 19,890.00 USD | 0.00 USD | `+12.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.89` | 3,120,000.00 USD | 4,060.00 USD | 0.00 USD | `+12.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.91` | 3,250,000.00 USD | 120,030.00 USD | 0.00 USD | `+12.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.92` | 3,250,000.00 USD | 156.30 USD | 0.00 USD | `+13.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.92` | 3,260,000.00 USD | 13,180.00 USD | 0.00 USD | `+13.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.93` | 3,260,000.00 USD | 4,420.00 USD | 0.00 USD | `+13.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.95` | 3,260,000.00 USD | 313.51 USD | 0.00 USD | `+13.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.96` | 3,270,000.00 USD | 7,900.00 USD | 0.00 USD | `+13.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.96` | 3,320,000.00 USD | 47,350.00 USD | 0.00 USD | `+14.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.97` | 3,320,000.00 USD | 187.06 USD | 0.00 USD | `+14.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.99` | 3,410,000.00 USD | 92,570.00 USD | 0.00 USD | `+14.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.00` | 3,410,000.00 USD | 2,540.00 USD | 0.00 USD | `+14.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.00` | 3,470,000.00 USD | 60,150.00 USD | 0.00 USD | `+15.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.01` | 3,500,000.00 USD | 25,080.00 USD | 0.00 USD | `+15.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.03` | 3,500,000.00 USD | 5,030.00 USD | 0.00 USD | `+15.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.04` | 3,520,000.00 USD | 19,640.00 USD | 0.00 USD | `+15.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.04` | 3,520,000.00 USD | 120.58 USD | 0.00 USD | `+16.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.05` | 3,540,000.00 USD | 14,690.00 USD | 0.00 USD | `+16.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.07` | 3,540,000.00 USD | 5,860.00 USD | 0.00 USD | `+16.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.08` | 3,630,000.00 USD | 87,450.00 USD | 0.00 USD | `+16.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.08` | 3,640,000.00 USD | 5,460.00 USD | 0.00 USD | `+16.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.09` | 3,640,000.00 USD | 178.33 USD | 0.00 USD | `+17.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.11` | 3,710,000.00 USD | 70,250.00 USD | 0.00 USD | `+17.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.12` | 3,720,000.00 USD | 15,350.00 USD | 0.00 USD | `+17.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.12` | 3,720,000.00 USD | 179.38 USD | 0.00 USD | `+17.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.13` | 3,720,000.00 USD | 179.72 USD | 0.00 USD | `+18.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.14` | 3,720,000.00 USD | 217.63 USD | 0.00 USD | `+18.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.16` | 3,720,000.00 USD | 493.85 USD | 0.00 USD | `+18.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.17` | 3,720,000.00 USD | 575.38 USD | 0.00 USD | `+18.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.17` | 3,720,000.00 USD | 327.58 USD | 0.00 USD | `+19.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.18` | 3,730,000.00 USD | 163.85 USD | 0.00 USD | `+19.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.20` | 3,850,000.00 USD | 120,930.00 USD | 0.00 USD | `+19.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.21` | 3,880,000.00 USD | 38,230.00 USD | 0.00 USD | `+19.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.21` | 3,890,000.00 USD | 1,710.00 USD | 0.00 USD | `+19.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.22` | 3,890,000.00 USD | 432.63 USD | 0.00 USD | `+20.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.24` | 3,890,000.00 USD | 2,620.00 USD | 0.00 USD | `+20.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.25` | 3,890,000.00 USD | 537.61 USD | 0.00 USD | `+20.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.25` | 4,310,000.00 USD | 420,400.00 USD | 0.00 USD | `+20.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.26` | 4,310,000.00 USD | 278.52 USD | 0.00 USD | `+21.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.28` | 4,310,000.00 USD | 589.22 USD | 0.00 USD | `+21.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.29` | 4,310,000.00 USD | 733.03 USD | 0.00 USD | `+21.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.29` | 4,310,000.00 USD | 423.60 USD | 0.00 USD | `+21.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.30` | 4,320,000.00 USD | 12,620.00 USD | 0.00 USD | `+22.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.32` | 4,320,000.00 USD | 381.09 USD | 0.00 USD | `+22.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.33` | 4,330,000.00 USD | 961.16 USD | 0.00 USD | `+22.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.33` | 4,330,000.00 USD | 1,570.00 USD | 0.00 USD | `+22.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.34` | 4,330,000.00 USD | 5,650.00 USD | 0.00 USD | `+22.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.36` | 4,330,000.00 USD | 160.11 USD | 0.00 USD | `+23.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.37` | 4,330,000.00 USD | 225.33 USD | 0.00 USD | `+23.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.38` | 4,330,000.00 USD | 438.60 USD | 0.00 USD | `+23.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.38` | 4,340,000.00 USD | 6,610.00 USD | 0.00 USD | `+23.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.39` | 4,380,000.00 USD | 40,880.00 USD | 0.00 USD | `+24.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.41` | 4,400,000.00 USD | 19,950.00 USD | 0.00 USD | `+24.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.42` | 4,410,000.00 USD | 4,330.00 USD | 0.00 USD | `+24.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.42` | 4,410,000.00 USD | 639.61 USD | 0.00 USD | `+24.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.43` | 4,410,000.00 USD | 1,710.00 USD | 0.00 USD | `+25.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.45` | 4,420,000.00 USD | 12,600.00 USD | 0.00 USD | `+25.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.46` | 4,420,000.00 USD | 1,020.00 USD | 0.00 USD | `+25.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.46` | 4,510,000.00 USD | 87,720.00 USD | 0.00 USD | `+25.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.47` | 4,540,000.00 USD | 30,110.00 USD | 0.00 USD | `+25.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.49` | 4,540,000.00 USD | 863.89 USD | 0.00 USD | `+26.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.50` | 4,540,000.00 USD | 1,040.00 USD | 0.00 USD | `+26.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.50` | 5,510,000.00 USD | 972,470.00 USD | 0.00 USD | `+26.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.51` | 5,520,000.00 USD | 5,600.00 USD | 0.00 USD | `+26.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.53` | 5,540,000.00 USD | 19,110.00 USD | 0.00 USD | `+27.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.54` | 5,560,000.00 USD | 18,790.00 USD | 0.00 USD | `+27.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.54` | 5,620,000.00 USD | 58,030.00 USD | 0.00 USD | `+27.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.55` | 5,660,000.00 USD | 46,110.00 USD | 0.00 USD | `+27.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.57` | 5,680,000.00 USD | 14,320.00 USD | 0.00 USD | `+27.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.58` | 5,690,000.00 USD | 11,740.00 USD | 0.00 USD | `+28.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.58` | 5,710,000.00 USD | 20,540.00 USD | 0.00 USD | `+28.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.59` | 5,710,000.00 USD | 384.94 USD | 0.00 USD | `+28.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.61` | 5,710,000.00 USD | 1,300.00 USD | 0.00 USD | `+28.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.62` | 5,710,000.00 USD | 347.06 USD | 0.00 USD | `+29.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.63` | 5,710,000.00 USD | 347.68 USD | 0.00 USD | `+29.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.64` | 5,710,000.00 USD | 839.41 USD | 0.00 USD | `+29.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.66` | 5,710,000.00 USD | 3,290.00 USD | 0.00 USD | `+30.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.67` | 5,710,000.00 USD | 281.55 USD | 0.00 USD | `+30.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.67` | 5,720,000.00 USD | 6,590.00 USD | 0.00 USD | `+30.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.68` | 5,720,000.00 USD | 235.93 USD | 0.00 USD | `+30.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.70` | 5,730,000.00 USD | 5,860.00 USD | 0.00 USD | `+30.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.71` | 5,830,000.00 USD | 103,470.00 USD | 0.00 USD | `+31.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.71` | 5,830,000.00 USD | 705.23 USD | 0.00 USD | `+31.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.72` | 5,840,000.00 USD | 5,720.00 USD | 0.00 USD | `+31.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.75` | 5,840,000.00 USD | 139.03 USD | 0.00 USD | `+32.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.75` | 5,840,000.00 USD | 2,480.00 USD | 0.00 USD | `+32.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.78` | 5,840,000.00 USD | 1,850.00 USD | 0.00 USD | `+32.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.79` | 5,840,000.00 USD | 286.94 USD | 0.00 USD | `+33.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.80` | 5,850,000.00 USD | 7,120.00 USD | 0.00 USD | `+33.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.82` | 5,850,000.00 USD | 329.13 USD | 0.00 USD | `+33.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.83` | 5,850,000.00 USD | 1,970.00 USD | 0.00 USD | `+33.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.83` | 5,850,000.00 USD | 1,020.00 USD | 0.00 USD | `+34.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.84` | 5,850,000.00 USD | 1,150.00 USD | 0.00 USD | `+34.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.86` | 5,860,000.00 USD | 1,190.00 USD | 0.00 USD | `+34.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.87` | 5,860,000.00 USD | 1,770.00 USD | 0.00 USD | `+34.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.88` | 5,860,000.00 USD | 3,450.00 USD | 0.00 USD | `+35.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.88` | 5,860,000.00 USD | 345.45 USD | 0.00 USD | `+35.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.91` | 5,940,000.00 USD | 81,590.00 USD | 0.00 USD | `+35.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.92` | 5,940,000.00 USD | 1,670.00 USD | 0.00 USD | `+36.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.92` | 5,940,000.00 USD | 1,020.00 USD | 0.00 USD | `+36.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.93` | 6,100,000.00 USD | 153,150.00 USD | 0.00 USD | `+36.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.96` | 6,120,000.00 USD | 26,180.00 USD | 0.00 USD | `+36.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.96` | 6,130,000.00 USD | 5,440.00 USD | 0.00 USD | `+37.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.97` | 6,140,000.00 USD | 8,940.00 USD | 0.00 USD | `+37.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.99` | 6,260,000.00 USD | 119,340.00 USD | 0.00 USD | `+37.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.00` | 6,270,000.00 USD | 7,340.00 USD | 0.00 USD | `+37.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.00` | 6,470,000.00 USD | 205,320.00 USD | 0.00 USD | `+38.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.01` | 6,480,000.00 USD | 13,710.00 USD | 0.00 USD | `+38.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.03` | 6,570,000.00 USD | 90,380.00 USD | 0.00 USD | `+38.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.04` | 6,580,000.00 USD | 2,080.00 USD | 0.00 USD | `+38.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.04` | 6,580,000.00 USD | 3,300.00 USD | 0.00 USD | `+39.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.05` | 6,580,000.00 USD | 1,040.00 USD | 0.00 USD | `+39.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.07` | 6,580,000.00 USD | 425.76 USD | 0.00 USD | `+39.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.08` | 6,590,000.00 USD | 4,120.00 USD | 0.00 USD | `+39.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.09` | 6,590,000.00 USD | 2,000.00 USD | 0.00 USD | `+40.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.11` | 6,650,000.00 USD | 61,050.00 USD | 0.00 USD | `+40.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.12` | 6,650,000.00 USD | 1,610.00 USD | 0.00 USD | `+40.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.13` | 6,650,000.00 USD | 1,200.00 USD | 0.00 USD | `+41.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.14` | 6,650,000.00 USD | 420.32 USD | 0.00 USD | `+41.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.16` | 6,650,000.00 USD | 1,940.00 USD | 0.00 USD | `+41.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.17` | 6,660,000.00 USD | 4,010.00 USD | 0.00 USD | `+42.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.21` | 6,720,000.00 USD | 66,060.00 USD | 0.00 USD | `+42.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.21` | 6,730,000.00 USD | 1,890.00 USD | 0.00 USD | `+42.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.22` | 6,730,000.00 USD | 195.46 USD | 0.00 USD | `+43.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.24` | 6,730,000.00 USD | 289.93 USD | 0.00 USD | `+43.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.25` | 6,730,000.00 USD | 116.16 USD | 0.00 USD | `+43.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.30` | 6,730,000.00 USD | 7,310.00 USD | 0.00 USD | `+45.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.32` | 6,730,000.00 USD | 310.70 USD | 0.00 USD | `+45.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.33` | 6,730,000.00 USD | 325.62 USD | 0.00 USD | `+45.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.36` | 6,740,000.00 USD | 1,760.00 USD | 0.00 USD | `+46.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.39` | 6,740,000.00 USD | 3,230.00 USD | 0.00 USD | `+47.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.41` | 6,740,000.00 USD | 5,120.00 USD | 0.00 USD | `+47.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.50` | 6,750,000.00 USD | 1,310.00 USD | 0.00 USD | `+49.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.50` | 6,780,000.00 USD | 30,990.00 USD | 0.00 USD | `+49.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.51` | 6,780,000.00 USD | 104.24 USD | 0.00 USD | `+49.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.54` | 6,790,000.00 USD | 13,580.00 USD | 0.00 USD | `+50.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.58` | 6,790,000.00 USD | 1,630.00 USD | 0.00 USD | `+51.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.59` | 6,790,000.00 USD | 1,370.00 USD | 0.00 USD | `+51.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.61` | 6,800,000.00 USD | 5,400.00 USD | 0.00 USD | `+51.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.62` | 6,800,000.00 USD | 1,620.00 USD | 0.00 USD | `+52.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.67` | 6,800,000.00 USD | 450.55 USD | 0.00 USD | `+53.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.67` | 6,800,000.00 USD | 3,060.00 USD | 0.00 USD | `+53.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.71` | 6,810,000.00 USD | 3,070.00 USD | 0.00 USD | `+54.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.75` | 6,810,000.00 USD | 1,550.00 USD | 0.00 USD | `+55.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.79` | 6,810,000.00 USD | 647.56 USD | 0.00 USD | `+56.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.80` | 6,810,000.00 USD | 1,420.00 USD | 0.00 USD | `+56.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.82` | 6,810,000.00 USD | 2,130.00 USD | 0.00 USD | `+56.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.83` | 6,820,000.00 USD | 6,870.00 USD | 0.00 USD | `+56.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.84` | 6,820,000.00 USD | 342.25 USD | 0.00 USD | `+57.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.87` | 6,820,000.00 USD | 2,990.00 USD | 0.00 USD | `+57.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.89` | 6,830,000.00 USD | 2,970.00 USD | 0.00 USD | `+58.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.91` | 6,830,000.00 USD | 324.54 USD | 0.00 USD | `+58.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.95` | 6,830,000.00 USD | 504.21 USD | 0.00 USD | `+59.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.97` | 6,830,000.00 USD | 166.00 USD | 0.00 USD | `+60.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.99` | 6,830,000.00 USD | 4,190.00 USD | 0.00 USD | `+60.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.00` | 6,840,000.00 USD | 13,480.00 USD | 0.00 USD | `+61.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.04` | 6,850,000.00 USD | 2,860.00 USD | 0.00 USD | `+62.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.11` | 6,850,000.00 USD | 264.31 USD | 0.00 USD | `+63.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.13` | 6,850,000.00 USD | 599.34 USD | 0.00 USD | `+64.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.16` | 6,850,000.00 USD | 193.19 USD | 0.00 USD | `+64.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.18` | 6,850,000.00 USD | 3,950.00 USD | 0.00 USD | `+65.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.21` | 6,850,000.00 USD | 1,940.00 USD | 0.00 USD | `+65.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.25` | 7,010,000.00 USD | 160,550.00 USD | 0.00 USD | `+66.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.28` | 7,020,000.00 USD | 1,290.00 USD | 0.00 USD | `+67.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.32` | 7,020,000.00 USD | 1,180.00 USD | 0.00 USD | `+68.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.39` | 7,020,000.00 USD | 630.05 USD | 0.00 USD | `+70.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.41` | 7,020,000.00 USD | 1,410.00 USD | 0.00 USD | `+70.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.42` | 7,020,000.00 USD | 2,610.00 USD | 0.00 USD | `+70.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.50` | 7,030,000.00 USD | 7,630.00 USD | 0.00 USD | `+72.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.58` | 7,030,000.00 USD | 4,640.00 USD | 0.00 USD | `+74.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.61` | 7,030,000.00 USD | 371.88 USD | 0.00 USD | `+74.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.62` | 7,040,000.00 USD | 2,510.00 USD | 0.00 USD | `+75.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.67` | 7,040,000.00 USD | 380.68 USD | 0.00 USD | `+76.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.79` | 7,050,000.00 USD | 11,170.00 USD | 0.00 USD | `+79.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.80` | 7,080,000.00 USD | 34,360.00 USD | 0.00 USD | `+79.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.82` | 7,080,000.00 USD | 253.21 USD | 0.00 USD | `+79.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.83` | 7,080,000.00 USD | 100.29 USD | 0.00 USD | `+80.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.96` | 7,090,000.00 USD | 10,610.00 USD | 0.00 USD | `+83.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.97` | 7,090,000.00 USD | 309.43 USD | 0.00 USD | `+83.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.99` | 7,100,000.00 USD | 4,640.00 USD | 0.00 USD | `+83.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.01` | 7,140,000.00 USD | 36,740.00 USD | 0.00 USD | `+84.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.03` | 7,220,000.00 USD | 81,310.00 USD | 0.00 USD | `+84.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.19` | 7,220,000.00 USD | 216.90 USD | 0.00 USD | `+88.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.20` | 7,220,000.00 USD | 1,990.00 USD | 0.00 USD | `+88.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.21` | 7,230,000.00 USD | 7,200.00 USD | 0.00 USD | `+88.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.38` | 7,230,000.00 USD | 998.65 USD | 0.00 USD | `+92.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.39` | 7,230,000.00 USD | 1,260.00 USD | 0.00 USD | `+93.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.40` | 7,330,000.00 USD | 103,010.00 USD | 0.00 USD | `+93.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.44` | 7,330,000.00 USD | 1,330.00 USD | 0.00 USD | `+94.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.46` | 7,330,000.00 USD | 721.22 USD | 0.00 USD | `+94.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.51` | 7,340,000.00 USD | 5,130.00 USD | 0.00 USD | `+95.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.61` | 7,340,000.00 USD | 2,010.00 USD | 0.00 USD | `+97.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.65` | 7,340,000.00 USD | 198.20 USD | 0.00 USD | `+99.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.66` | 7,340,000.00 USD | 3,670.00 USD | 0.00 USD | `+99.29%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `3.48` | 18,210,000.00 USD | 0.00 USD | 18,210,000.00 USD | 45,650.00 USD | 26,250.00 USD | 1,510.00 USD |
| `7D` | `3.50` | 18,140,000.00 USD | 0.00 USD | 18,140,000.00 USD | 16,960.00 USD | 6,940.00 USD | 38,050.00 USD |
| `7D` | `3.51` | 18,080,000.00 USD | 0.00 USD | 18,080,000.00 USD | 3,690.00 USD | 0.00 USD | 231.64 USD |
| `7D` | `3.52` | 18,070,000.00 USD | 0.00 USD | 18,070,000.00 USD | 15,180.00 USD | 0.00 USD | 41,090.00 USD |
| `7D` | `3.53` | 18,020,000.00 USD | 0.00 USD | 18,020,000.00 USD | 93,360.00 USD | 40,470.00 USD | 96,140.00 USD |
| `7D` | `3.54` | 17,790,000.00 USD | 0.00 USD | 17,790,000.00 USD | 3,040.00 USD | 58,300.00 USD | 30,480.00 USD |
| `7D` | `3.55` | 17,690,000.00 USD | 0.00 USD | 17,690,000.00 USD | 128,490.00 USD | 54,880.00 USD | 45,330.00 USD |
| `7D` | `3.56` | 17,470,000.00 USD | 0.00 USD | 17,470,000.00 USD | 61,170.00 USD | 0.00 USD | 32.49 USD |
| `7D` | `3.57` | 17,400,000.00 USD | 0.00 USD | 17,400,000.00 USD | 86,360.00 USD | 27,910.00 USD | 84,270.00 USD |
| `7D` | `3.58` | 17,210,000.00 USD | 0.00 USD | 17,210,000.00 USD | 173,980.00 USD | 48,640.00 USD | 59,950.00 USD |
| `7D` | `3.59` | 16,920,000.00 USD | 0.00 USD | 16,920,000.00 USD | 535.75 USD | 18,170.00 USD | 78.80 USD |
| `7D` | `3.60` | 16,900,000.00 USD | 0.00 USD | 16,900,000.00 USD | 64,170.00 USD | 21,460.00 USD | 22,050.00 USD |
| `7D` | `3.61` | 16,800,000.00 USD | 0.00 USD | 16,800,000.00 USD | 56,580.00 USD | 37,060.00 USD | 44,890.00 USD |
| `7D` | `3.62` | 16,660,000.00 USD | 0.00 USD | 16,660,000.00 USD | 92,130.00 USD | 26,640.00 USD | 97,570.00 USD |
| `7D` | `3.63` | 16,440,000.00 USD | 0.00 USD | 16,440,000.00 USD | 50,840.00 USD | 8,120.00 USD | 159.02 USD |
| `7D` | `3.64` | 16,380,000.00 USD | 0.00 USD | 16,380,000.00 USD | 2,410.00 USD | 41,960.00 USD | 119,140.00 USD |
| `7D` | `3.65` | 16,220,000.00 USD | 0.00 USD | 16,220,000.00 USD | 53,900.00 USD | 7,050.00 USD | 31,190.00 USD |
| `7D` | `3.66` | 16,130,000.00 USD | 0.00 USD | 16,130,000.00 USD | 32,350.00 USD | 15,090.00 USD | 125,270.00 USD |
| `7D` | `3.67` | 15,950,000.00 USD | 0.00 USD | 15,950,000.00 USD | 52,020.00 USD | 14,480.00 USD | 53,670.00 USD |
| `7D` | `3.68` | 15,830,000.00 USD | 0.00 USD | 15,830,000.00 USD | 1,010.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `3.69` | 15,830,000.00 USD | 0.00 USD | 15,830,000.00 USD | 27,750.00 USD | 0.00 USD | 59,840.00 USD |
| `7D` | `3.70` | 15,750,000.00 USD | 0.00 USD | 15,750,000.00 USD | 20,470.00 USD | 7,370.00 USD | 112,470.00 USD |
| `7D` | `3.71` | 15,610,000.00 USD | 0.00 USD | 15,610,000.00 USD | 51,960.00 USD | 0.00 USD | 74,330.00 USD |
| `7D` | `3.72` | 15,480,000.00 USD | 0.00 USD | 15,480,000.00 USD | 425.03 USD | 0.00 USD | 183.06 USD |
| `7D` | `3.73` | 15,480,000.00 USD | 0.00 USD | 15,480,000.00 USD | 41,940.00 USD | 10,880.00 USD | 56,790.00 USD |
| `7D` | `3.74` | 15,370,000.00 USD | 0.00 USD | 15,370,000.00 USD | 130,620.00 USD | 40,020.00 USD | 122,480.00 USD |
| `7D` | `3.75` | 15,080,000.00 USD | 0.00 USD | 15,080,000.00 USD | 3,890.00 USD | 51,780.00 USD | 129,350.00 USD |
| `7D` | `3.76` | 14,890,000.00 USD | 0.00 USD | 14,890,000.00 USD | 32,650.00 USD | 10,110.00 USD | 22,610.00 USD |
| `7D` | `3.77` | 14,830,000.00 USD | 0.00 USD | 14,830,000.00 USD | 15,340.00 USD | 8,090.00 USD | 23,020.00 USD |
| `7D` | `3.78` | 14,780,000.00 USD | 0.00 USD | 14,780,000.00 USD | 24,180.00 USD | 93,830.00 USD | 41,570.00 USD |
| `1D` | `3.79` | 18,120,000.00 USD | 0.00 USD | 18,120,000.00 USD | 9,260.00 USD | 79,360.00 USD | 106,250.00 USD |
| `7D` | `3.79` | 14,620,000.00 USD | 0.00 USD | 14,620,000.00 USD | 51,640.00 USD | 0.00 USD | 137,710.00 USD |
| `1D` | `3.80` | 17,920,000.00 USD | 0.00 USD | 17,920,000.00 USD | 3,400.00 USD | 0.00 USD | 74,400.00 USD |
| `7D` | `3.80` | 14,430,000.00 USD | 0.00 USD | 14,430,000.00 USD | 8,210.00 USD | 34,570.00 USD | 17,840.00 USD |
| `1D` | `3.81` | 17,840,000.00 USD | 0.00 USD | 17,840,000.00 USD | 213,700.00 USD | 0.00 USD | 103,870.00 USD |
| `7D` | `3.81` | 14,370,000.00 USD | 0.00 USD | 14,370,000.00 USD | 5,310.00 USD | 0.00 USD | 1,430.00 USD |
| `1D` | `3.82` | 17,530,000.00 USD | 0.00 USD | 17,530,000.00 USD | 49,390.00 USD | 31,910.00 USD | 141,610.00 USD |
| `7D` | `3.82` | 14,360,000.00 USD | 0.00 USD | 14,360,000.00 USD | 5,630.00 USD | 18,370.00 USD | 25,600.00 USD |
| `1D` | `3.83` | 17,300,000.00 USD | 0.00 USD | 17,300,000.00 USD | 125,840.00 USD | 125,330.00 USD | 114,620.00 USD |
| `7D` | `3.83` | 14,310,000.00 USD | 0.00 USD | 14,310,000.00 USD | 50,540.00 USD | 50,500.00 USD | 153.98 USD |
| `1D` | `3.84` | 16,940,000.00 USD | 0.00 USD | 16,940,000.00 USD | 150,080.00 USD | 46,190.00 USD | 64,230.00 USD |
| `7D` | `3.84` | 14,210,000.00 USD | 0.00 USD | 14,210,000.00 USD | 7,940.00 USD | 33,350.00 USD | 146.37 USD |
| `1D` | `3.85` | 16,680,000.00 USD | 0.00 USD | 16,680,000.00 USD | 186,230.00 USD | 175,470.00 USD | 37,740.00 USD |
| `7D` | `3.85` | 14,170,000.00 USD | 0.00 USD | 14,170,000.00 USD | 3,390.00 USD | 49,170.00 USD | 84,260.00 USD |
| `1D` | `3.86` | 16,280,000.00 USD | 0.00 USD | 16,280,000.00 USD | 39,130.00 USD | 39,050.00 USD | 52,990.00 USD |
| `7D` | `3.86` | 14,030,000.00 USD | 0.00 USD | 14,030,000.00 USD | 5,190.00 USD | 173,980.00 USD | 72,520.00 USD |
| `1D` | `3.87` | 16,150,000.00 USD | 0.00 USD | 16,150,000.00 USD | 52,700.00 USD | 58,230.00 USD | 188,300.00 USD |
| `7D` | `3.87` | 13,780,000.00 USD | 0.00 USD | 13,780,000.00 USD | 63,710.00 USD | 0.00 USD | 227,340.00 USD |
| `1D` | `3.88` | 15,850,000.00 USD | 0.00 USD | 15,850,000.00 USD | 35,520.00 USD | 17,520.00 USD | 224,870.00 USD |
| `7D` | `3.88` | 13,490,000.00 USD | 0.00 USD | 13,490,000.00 USD | 110,160.00 USD | 86,900.00 USD | 156,790.00 USD |
| `1D` | `3.89` | 15,570,000.00 USD | 0.00 USD | 15,570,000.00 USD | 373,610.00 USD | 100,370.00 USD | 238,830.00 USD |
| `7D` | `3.89` | 13,140,000.00 USD | 0.00 USD | 13,140,000.00 USD | 4,240.00 USD | 50,710.00 USD | 83,380.00 USD |
| `1D` | `3.90` | 14,860,000.00 USD | 0.00 USD | 14,860,000.00 USD | 33,360.00 USD | 49,080.00 USD | 223,320.00 USD |
| `7D` | `3.90` | 13,000,000.00 USD | 0.00 USD | 13,000,000.00 USD | 274,050.00 USD | 28,250.00 USD | 51,510.00 USD |
| `1D` | `3.91` | 14,550,000.00 USD | 0.00 USD | 14,550,000.00 USD | 337,710.00 USD | 120,100.00 USD | 276,080.00 USD |
| `7D` | `3.91` | 12,650,000.00 USD | 0.00 USD | 12,650,000.00 USD | 122,540.00 USD | 67,260.00 USD | 46,930.00 USD |
| `1D` | `3.92` | 13,820,000.00 USD | 0.00 USD | 13,820,000.00 USD | 318,260.00 USD | 8,570.00 USD | 144,790.00 USD |
| `7D` | `3.92` | 12,410,000.00 USD | 0.00 USD | 12,410,000.00 USD | 85,790.00 USD | 66,710.00 USD | 104,900.00 USD |
| `1D` | `3.93` | 13,340,000.00 USD | 0.00 USD | 13,340,000.00 USD | 116,350.00 USD | 99,220.00 USD | 97,360.00 USD |
| `7D` | `3.93` | 12,150,000.00 USD | 0.00 USD | 12,150,000.00 USD | 0.00 USD | 28,720.00 USD | 67.04 USD |
| `1D` | `3.94` | 13,030,000.00 USD | 0.00 USD | 13,030,000.00 USD | 132,520.00 USD | 53,060.00 USD | 137,210.00 USD |
| `7D` | `3.94` | 12,120,000.00 USD | 0.00 USD | 12,120,000.00 USD | 55,330.00 USD | 0.00 USD | 2,250.00 USD |
| `1D` | `3.95` | 12,710,000.00 USD | 0.00 USD | 12,710,000.00 USD | 116,010.00 USD | 0.00 USD | 33,080.00 USD |
| `7D` | `3.95` | 12,060,000.00 USD | 0.00 USD | 12,060,000.00 USD | 8,490.00 USD | 0.00 USD | 2,800.00 USD |
| `1D` | `3.96` | 12,560,000.00 USD | 0.00 USD | 12,560,000.00 USD | 67,260.00 USD | 22,830.00 USD | 17,320.00 USD |
| `7D` | `3.96` | 12,050,000.00 USD | 0.00 USD | 12,050,000.00 USD | 165,060.00 USD | 0.00 USD | 325.84 USD |
| `1D` | `3.97` | 12,450,000.00 USD | 0.00 USD | 12,450,000.00 USD | 2,650.00 USD | 36,470.00 USD | 137,700.00 USD |
| `7D` | `3.97` | 11,890,000.00 USD | 0.00 USD | 11,890,000.00 USD | 235,890.00 USD | 0.00 USD | 2,980.00 USD |
| `1D` | `3.98` | 12,280,000.00 USD | 0.00 USD | 12,280,000.00 USD | 20,780.00 USD | 76,990.00 USD | 94,490.00 USD |
| `7D` | `3.98` | 11,650,000.00 USD | 0.00 USD | 11,650,000.00 USD | 506,280.00 USD | 0.00 USD | 279,750.00 USD |
| `1D` | `3.99` | 12,080,000.00 USD | 0.00 USD | 12,080,000.00 USD | 34,010.00 USD | 64,350.00 USD | 106,350.00 USD |
| `7D` | `3.99` | 10,860,000.00 USD | 0.00 USD | 10,860,000.00 USD | 298,270.00 USD | 26,340.00 USD | 78,590.00 USD |
| `1D` | `4.00` | 11,880,000.00 USD | 0.00 USD | 11,880,000.00 USD | 40,030.00 USD | 17,140.00 USD | 137,750.00 USD |
| `7D` | `4.00` | 10,460,000.00 USD | 0.00 USD | 10,460,000.00 USD | 307,590.00 USD | 68,590.00 USD | 574,560.00 USD |
| `1D` | `4.01` | 11,680,000.00 USD | 0.00 USD | 11,680,000.00 USD | 1,580.00 USD | 158,450.00 USD | 222,750.00 USD |
| `7D` | `4.01` | 9,510,000.00 USD | 0.00 USD | 9,510,000.00 USD | 371,710.00 USD | 57,440.00 USD | 438,780.00 USD |
| `1D` | `4.02` | 11,300,000.00 USD | 0.00 USD | 11,300,000.00 USD | 135,580.00 USD | 52,150.00 USD | 125,260.00 USD |
| `7D` | `4.02` | 8,640,000.00 USD | 0.00 USD | 8,640,000.00 USD | 271,690.00 USD | 156,620.00 USD | 251,090.00 USD |
| `1D` | `4.03` | 10,990,000.00 USD | 0.00 USD | 10,990,000.00 USD | 64,700.00 USD | 59,350.00 USD | 324.38 USD |
| `7D` | `4.03` | 7,960,000.00 USD | 0.00 USD | 7,960,000.00 USD | 247,960.00 USD | 0.00 USD | 344,930.00 USD |
| `1D` | `4.04` | 10,860,000.00 USD | 0.00 USD | 10,860,000.00 USD | 69,810.00 USD | 21,940.00 USD | 183,420.00 USD |
| `7D` | `4.04` | 7,370,000.00 USD | 0.00 USD | 7,370,000.00 USD | 321,230.00 USD | 0.00 USD | 492,290.00 USD |
| `1D` | `4.05` | 10,590,000.00 USD | 0.00 USD | 10,590,000.00 USD | 348,930.00 USD | 23,720.00 USD | 145.87 USD |
| `7D` | `4.05` | 6,560,000.00 USD | 0.00 USD | 6,560,000.00 USD | 2,180.00 USD | 41,020.00 USD | 68,490.00 USD |
| `1D` | `4.06` | 10,220,000.00 USD | 0.00 USD | 10,220,000.00 USD | 35,870.00 USD | 83,800.00 USD | 450,780.00 USD |
| `7D` | `4.06` | 6,440,000.00 USD | 0.00 USD | 6,440,000.00 USD | 0.00 USD | 72,410.00 USD | 292.74 USD |
| `1D` | `4.07` | 9,640,000.00 USD | 0.00 USD | 9,640,000.00 USD | 358,380.00 USD | 205,460.00 USD | 334,550.00 USD |
| `7D` | `4.07` | 6,370,000.00 USD | 0.00 USD | 6,370,000.00 USD | 0.00 USD | 287,180.00 USD | 166,640.00 USD |
| `1D` | `4.08` | 8,750,000.00 USD | 0.00 USD | 8,750,000.00 USD | 69,080.00 USD | 277,630.00 USD | 133,910.00 USD |
| `7D` | `4.08` | 5,920,000.00 USD | 0.00 USD | 5,920,000.00 USD | 0.00 USD | 237,170.00 USD | 135.50 USD |
| `1D` | `4.09` | 8,270,000.00 USD | 0.00 USD | 8,270,000.00 USD | 245,370.00 USD | 60,230.00 USD | 168,220.00 USD |
| `7D` | `4.09` | 5,680,000.00 USD | 0.00 USD | 5,680,000.00 USD | 253,510.00 USD | 179,350.00 USD | 432,940.00 USD |
| `1D` | `4.10` | 7,790,000.00 USD | 0.00 USD | 7,790,000.00 USD | 2,770.00 USD | 89,650.00 USD | 141,410.00 USD |
| `7D` | `4.10` | 4,810,000.00 USD | 0.00 USD | 4,810,000.00 USD | 27,630.00 USD | 0.00 USD | 240.24 USD |
| `1D` | `4.11` | 7,560,000.00 USD | 0.00 USD | 7,560,000.00 USD | 120,600.00 USD | 138,540.00 USD | 345,580.00 USD |
| `7D` | `4.11` | 4,790,000.00 USD | 0.00 USD | 4,790,000.00 USD | 0.00 USD | 25,170.00 USD | 295,730.00 USD |
| `1D` | `4.12` | 6,950,000.00 USD | 0.00 USD | 6,950,000.00 USD | 48,010.00 USD | 34,010.00 USD | 274,180.00 USD |
| `7D` | `4.12` | 4,470,000.00 USD | 0.00 USD | 4,470,000.00 USD | 2,900.00 USD | 181,330.00 USD | 0.00 USD |
| `1D` | `4.13` | 6,600,000.00 USD | 0.00 USD | 6,600,000.00 USD | 159,720.00 USD | 0.00 USD | 398,260.00 USD |
| `7D` | `4.13` | 4,280,000.00 USD | 0.00 USD | 4,280,000.00 USD | 154,140.00 USD | 0.00 USD | 237,490.00 USD |
| `1D` | `4.14` | 6,040,000.00 USD | 0.00 USD | 6,040,000.00 USD | 98,250.00 USD | 0.00 USD | 125,370.00 USD |
| `7D` | `4.14` | 3,890,000.00 USD | 0.00 USD | 3,890,000.00 USD | 238,150.00 USD | 217,700.00 USD | 345,750.00 USD |
| `1D` | `4.15` | 5,820,000.00 USD | 0.00 USD | 5,820,000.00 USD | 469,190.00 USD | 102,010.00 USD | 318,980.00 USD |
| `7D` | `4.15` | 3,090,000.00 USD | 0.00 USD | 3,090,000.00 USD | 235,070.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `4.16` | 4,930,000.00 USD | 0.00 USD | 4,930,000.00 USD | 276,920.00 USD | 51,570.00 USD | 316,310.00 USD |
| `1D` | `4.17` | 4,280,000.00 USD | 0.00 USD | 4,280,000.00 USD | 215,050.00 USD | 283,430.00 USD | 238,930.00 USD |
| `7D` | `4.17` | 2,850,000.00 USD | 0.00 USD | 2,850,000.00 USD | 252,690.00 USD | 84,340.00 USD | 0.00 USD |
| `1D` | `4.18` | 3,540,000.00 USD | 0.00 USD | 3,540,000.00 USD | 329,080.00 USD | 62,340.00 USD | 201,720.00 USD |
| `7D` | `4.18` | 2,520,000.00 USD | 0.00 USD | 2,520,000.00 USD | 0.00 USD | 0.00 USD | 86,570.00 USD |
| `1D` | `4.19` | 2,950,000.00 USD | 0.00 USD | 2,950,000.00 USD | 148,260.00 USD | 125,540.00 USD | 244,930.00 USD |
| `7D` | `4.19` | 2,430,000.00 USD | 0.00 USD | 2,430,000.00 USD | 2,760.00 USD | 50,340.00 USD | 393,520.00 USD |
| `1D` | `4.20` | 2,430,000.00 USD | 0.00 USD | 2,430,000.00 USD | 540.30 USD | 26,180.00 USD | 131,830.00 USD |
| `7D` | `4.20` | 1,980,000.00 USD | 0.00 USD | 1,980,000.00 USD | 227,690.00 USD | 86,790.00 USD | 371,630.00 USD |
| `1D` | `4.21` | 2,270,000.00 USD | 0.00 USD | 2,270,000.00 USD | 487,450.00 USD | 98,820.00 USD | 217,230.00 USD |
| `7D` | `4.21` | 1,300,000.00 USD | 0.00 USD | 1,300,000.00 USD | 308,290.00 USD | 0.00 USD | 146,990.00 USD |
| `1D` | `4.22` | 1,470,000.00 USD | 0.00 USD | 1,470,000.00 USD | 0.00 USD | 0.00 USD | 56,420.00 USD |
| `7D` | `4.22` | 841,160.00 USD | 0.00 USD | 841,160.00 USD | 119,070.00 USD | 89,680.00 USD | 417,550.00 USD |
| `1D` | `4.23` | 1,410,000.00 USD | 0.00 USD | 1,410,000.00 USD | 0.00 USD | 114,760.00 USD | 176,960.00 USD |
| `1D` | `4.25` | 1,120,000.00 USD | 0.00 USD | 1,120,000.00 USD | 0.00 USD | 0.00 USD | 186,310.00 USD |
| `7D` | `4.25` | 214,850.00 USD | 0.00 USD | 214,850.00 USD | 3,390.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `4.26` | 934,970.00 USD | 0.00 USD | 934,970.00 USD | 0.00 USD | 0.00 USD | 85,610.00 USD |
| `7D` | `4.26` | 211,460.00 USD | 0.00 USD | 211,460.00 USD | 2,960.00 USD | 0.00 USD | 173,150.00 USD |
| `1D` | `4.27` | 849,360.00 USD | 0.00 USD | 849,360.00 USD | 0.00 USD | 19,380.00 USD | 0.00 USD |
| `7D` | `4.27` | 35,350.00 USD | 0.00 USD | 35,350.00 USD | 24,810.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `4.28` | 829,980.00 USD | 0.00 USD | 829,980.00 USD | 4,310.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4.28` | 10,540.00 USD | 0.00 USD | 10,540.00 USD | 5,380.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `4.29` | 825,670.00 USD | 0.00 USD | 825,670.00 USD | 156,040.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4.29` | 5,150.00 USD | 0.00 USD | 5,150.00 USD | 5,150.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `4.31` | 669,620.00 USD | 0.00 USD | 669,620.00 USD | 0.00 USD | 0.00 USD | 353.18 USD |
| `1D` | `4.32` | 669,270.00 USD | 0.00 USD | 669,270.00 USD | 381,790.00 USD | 0.00 USD | 326.33 USD |
| `7D` | `4.32` | 265,720.00 USD | 265,720.00 USD | 0.00 USD | 265,720.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4.32` | 531,440.00 USD | 531,440.00 USD | 0.00 USD | 265,720.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `4.33` | 287,160.00 USD | 0.00 USD | 287,160.00 USD | 287,160.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `4.34` | 269,670.00 USD | 269,670.00 USD | 0.00 USD | 269,670.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `4.34` | 539,330.00 USD | 539,330.00 USD | 0.00 USD | 269,670.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4.34` | 538,780.00 USD | 538,780.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 7,340.00 USD |
| `1D` | `4.35` | 696,360.00 USD | 696,360.00 USD | 0.00 USD | 157,030.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4.35` | 791,460.00 USD | 791,460.00 USD | 0.00 USD | 252,690.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `4.36` | 1,080,000.00 USD | 1,080,000.00 USD | 0.00 USD | 100,970.00 USD | 0.00 USD | 279,180.00 USD |
| `1D` | `4.37` | 1,930,000.00 USD | 1,930,000.00 USD | 0.00 USD | 280,420.00 USD | 173,170.00 USD | 400,000.00 USD |
| `7D` | `4.37` | 1,240,000.00 USD | 1,240,000.00 USD | 0.00 USD | 0.00 USD | 50,340.00 USD | 393,520.00 USD |
| `1D` | `4.38` | 2,880,000.00 USD | 2,880,000.00 USD | 0.00 USD | 250,760.00 USD | 60,680.00 USD | 640,700.00 USD |
| `7D` | `4.38` | 1,730,000.00 USD | 1,730,000.00 USD | 0.00 USD | 0.00 USD | 228,720.00 USD | 261,380.00 USD |
| `1D` | `4.39` | 3,790,000.00 USD | 3,790,000.00 USD | 0.00 USD | 356,920.00 USD | 41,380.00 USD | 505,620.00 USD |
| `7D` | `4.39` | 2,810,000.00 USD | 2,810,000.00 USD | 0.00 USD | 560,900.00 USD | 149,280.00 USD | 369,470.00 USD |
| `1D` | `4.40` | 4,710,000.00 USD | 4,710,000.00 USD | 0.00 USD | 458,500.00 USD | 58,380.00 USD | 408,330.00 USD |
| `7D` | `4.40` | 3,920,000.00 USD | 3,920,000.00 USD | 0.00 USD | 111,810.00 USD | 116,620.00 USD | 881,540.00 USD |
| `1D` | `4.41` | 5,960,000.00 USD | 5,960,000.00 USD | 0.00 USD | 336,310.00 USD | 317,280.00 USD | 592,230.00 USD |
| `7D` | `4.41` | 4,260,000.00 USD | 4,260,000.00 USD | 0.00 USD | 1,450.00 USD | 65,600.00 USD | 278,000.00 USD |
| `1D` | `4.42` | 6,230,000.00 USD | 6,230,000.00 USD | 0.00 USD | 1,080.00 USD | 142,250.00 USD | 127,800.00 USD |
| `7D` | `4.42` | 4,910,000.00 USD | 4,910,000.00 USD | 0.00 USD | 404,280.00 USD | 71,590.00 USD | 175,990.00 USD |
| `1D` | `4.43` | 6,720,000.00 USD | 6,720,000.00 USD | 0.00 USD | 84,650.00 USD | 109,630.00 USD | 300,550.00 USD |
| `7D` | `4.43` | 5,370,000.00 USD | 5,370,000.00 USD | 0.00 USD | 293,250.00 USD | 88,400.00 USD | 71,780.00 USD |
| `1D` | `4.44` | 7,710,000.00 USD | 7,710,000.00 USD | 0.00 USD | 156,430.00 USD | 370,280.00 USD | 457,750.00 USD |
| `7D` | `4.44` | 5,760,000.00 USD | 5,760,000.00 USD | 0.00 USD | 0.00 USD | 143,990.00 USD | 246,120.00 USD |
| `1D` | `4.45` | 8,040,000.00 USD | 8,040,000.00 USD | 0.00 USD | 76,860.00 USD | 128,020.00 USD | 124,130.00 USD |
| `7D` | `4.45` | 5,980,000.00 USD | 5,980,000.00 USD | 0.00 USD | 0.00 USD | 25,170.00 USD | 196,900.00 USD |
| `1D` | `4.46` | 8,110,000.00 USD | 8,110,000.00 USD | 0.00 USD | 4,580.00 USD | 37,160.00 USD | 33,060.00 USD |
| `7D` | `4.46` | 6,090,000.00 USD | 6,090,000.00 USD | 0.00 USD | 3,070.00 USD | 105,500.00 USD | 2,350.00 USD |
| `1D` | `4.47` | 8,420,000.00 USD | 8,420,000.00 USD | 0.00 USD | 160,740.00 USD | 25,190.00 USD | 120,030.00 USD |
| `7D` | `4.47` | 6,660,000.00 USD | 6,660,000.00 USD | 0.00 USD | 358,290.00 USD | 135,940.00 USD | 75,550.00 USD |
| `1D` | `4.48` | 8,860,000.00 USD | 8,860,000.00 USD | 0.00 USD | 205,250.00 USD | 86,520.00 USD | 150,910.00 USD |
| `7D` | `4.48` | 6,920,000.00 USD | 6,920,000.00 USD | 0.00 USD | 1,870.00 USD | 44,840.00 USD | 210,580.00 USD |
| `1D` | `4.49` | 9,700,000.00 USD | 9,700,000.00 USD | 0.00 USD | 253,770.00 USD | 235,310.00 USD | 354,870.00 USD |
| `7D` | `4.49` | 7,250,000.00 USD | 7,250,000.00 USD | 0.00 USD | 244,370.00 USD | 93,790.00 USD | 162.91 USD |
| `1D` | `4.50` | 10,310,000.00 USD | 10,310,000.00 USD | 0.00 USD | 363,660.00 USD | 69,580.00 USD | 175,170.00 USD |
| `7D` | `4.50` | 7,830,000.00 USD | 7,830,000.00 USD | 0.00 USD | 376,770.00 USD | 200,700.00 USD | 2,050.00 USD |
| `1D` | `4.51` | 11,070,000.00 USD | 11,070,000.00 USD | 0.00 USD | 188,660.00 USD | 149,810.00 USD | 418,530.00 USD |
| `7D` | `4.51` | 7,910,000.00 USD | 7,910,000.00 USD | 0.00 USD | 77,780.00 USD | 0.00 USD | 2,140.00 USD |
| `1D` | `4.52` | 11,740,000.00 USD | 11,740,000.00 USD | 0.00 USD | 290,030.00 USD | 92,260.00 USD | 285,900.00 USD |
| `7D` | `4.52` | 8,140,000.00 USD | 8,140,000.00 USD | 0.00 USD | 2,080.00 USD | 0.00 USD | 225,130.00 USD |
| `1D` | `4.53` | 12,530,000.00 USD | 12,530,000.00 USD | 0.00 USD | 505,320.00 USD | 9,690.00 USD | 280,060.00 USD |
| `7D` | `4.53` | 9,120,000.00 USD | 9,120,000.00 USD | 0.00 USD | 439,420.00 USD | 232,800.00 USD | 309,760.00 USD |
| `1D` | `4.54` | 12,930,000.00 USD | 12,930,000.00 USD | 0.00 USD | 15,720.00 USD | 150,600.00 USD | 234,180.00 USD |
| `7D` | `4.54` | 10,360,000.00 USD | 10,360,000.00 USD | 0.00 USD | 2,730.00 USD | 0.00 USD | 1,240,000.00 USD |
| `1D` | `4.55` | 13,080,000.00 USD | 13,080,000.00 USD | 0.00 USD | 1,620.00 USD | 34,450.00 USD | 108,590.00 USD |
| `7D` | `4.55` | 10,360,000.00 USD | 10,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 237.00 USD |
| `1D` | `4.56` | 13,480,000.00 USD | 13,480,000.00 USD | 0.00 USD | 81,450.00 USD | 32,800.00 USD | 288,460.00 USD |
| `7D` | `4.56` | 10,850,000.00 USD | 10,850,000.00 USD | 0.00 USD | 364,250.00 USD | 124,220.00 USD | 219.44 USD |
| `1D` | `4.57` | 13,830,000.00 USD | 13,830,000.00 USD | 0.00 USD | 176,460.00 USD | 70,180.00 USD | 99,380.00 USD |
| `7D` | `4.57` | 11,390,000.00 USD | 11,390,000.00 USD | 0.00 USD | 305,830.00 USD | 27,650.00 USD | 209,430.00 USD |
| `1D` | `4.58` | 14,980,000.00 USD | 14,980,000.00 USD | 0.00 USD | 423,030.00 USD | 99,430.00 USD | 634,100.00 USD |
| `7D` | `4.58` | 11,530,000.00 USD | 11,530,000.00 USD | 0.00 USD | 44,380.00 USD | 0.00 USD | 86,090.00 USD |
| `1D` | `4.59` | 15,590,000.00 USD | 15,590,000.00 USD | 0.00 USD | 419,400.00 USD | 75,460.00 USD | 109,280.00 USD |
| `7D` | `4.59` | 13,240,000.00 USD | 13,240,000.00 USD | 0.00 USD | 760,880.00 USD | 68,070.00 USD | 881,510.00 USD |
| `1D` | `4.60` | 15,750,000.00 USD | 15,750,000.00 USD | 0.00 USD | 49,460.00 USD | 50,860.00 USD | 66,380.00 USD |
| `7D` | `4.60` | 13,350,000.00 USD | 13,350,000.00 USD | 0.00 USD | 3,460.00 USD | 112,080.00 USD | 2,360.00 USD |
| `1D` | `4.61` | 15,900,000.00 USD | 15,900,000.00 USD | 0.00 USD | 64,340.00 USD | 7,560.00 USD | 76,320.00 USD |
| `7D` | `4.61` | 13,360,000.00 USD | 13,360,000.00 USD | 0.00 USD | 5,400.00 USD | 0.00 USD | 1,140.00 USD |
| `1D` | `4.62` | 16,050,000.00 USD | 16,050,000.00 USD | 0.00 USD | 94,450.00 USD | 31,380.00 USD | 19,780.00 USD |
| `7D` | `4.62` | 13,500,000.00 USD | 13,500,000.00 USD | 0.00 USD | 134,680.00 USD | 0.00 USD | 2,890.00 USD |
| `1D` | `4.63` | 16,050,000.00 USD | 16,050,000.00 USD | 0.00 USD | 2,310.00 USD | 0.00 USD | 335.46 USD |
| `7D` | `4.63` | 13,710,000.00 USD | 13,710,000.00 USD | 0.00 USD | 215,660.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `4.64` | 16,210,000.00 USD | 16,210,000.00 USD | 0.00 USD | 106,430.00 USD | 11,270.00 USD | 41,460.00 USD |
| `7D` | `4.64` | 14,250,000.00 USD | 14,250,000.00 USD | 0.00 USD | 503,610.00 USD | 34,570.00 USD | 1,730.00 USD |
| `1D` | `4.65` | 16,950,000.00 USD | 16,950,000.00 USD | 0.00 USD | 203,560.00 USD | 52,020.00 USD | 486,560.00 USD |
| `7D` | `4.65` | 14,680,000.00 USD | 14,680,000.00 USD | 0.00 USD | 420,940.00 USD | 0.00 USD | 2,070.00 USD |
| `1D` | `4.66` | 17,740,000.00 USD | 17,740,000.00 USD | 0.00 USD | 202,480.00 USD | 309,340.00 USD | 277,030.00 USD |
| `7D` | `4.66` | 14,990,000.00 USD | 14,990,000.00 USD | 0.00 USD | 144,860.00 USD | 18,370.00 USD | 150,940.00 USD |
| `1D` | `4.67` | 18,090,000.00 USD | 18,090,000.00 USD | 0.00 USD | 88,770.00 USD | 0.00 USD | 259,350.00 USD |
| `7D` | `4.67` | 15,030,000.00 USD | 15,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 43,230.00 USD |
| `1D` | `4.68` | 18,290,000.00 USD | 18,290,000.00 USD | 0.00 USD | 60,330.00 USD | 106,120.00 USD | 37,010.00 USD |
| `7D` | `4.68` | 15,950,000.00 USD | 15,950,000.00 USD | 0.00 USD | 381,910.00 USD | 83,630.00 USD | 450,770.00 USD |
| `1D` | `4.69` | 18,680,000.00 USD | 18,680,000.00 USD | 0.00 USD | 168,690.00 USD | 49,160.00 USD | 168,810.00 USD |
| `7D` | `4.69` | 16,110,000.00 USD | 16,110,000.00 USD | 0.00 USD | 52,990.00 USD | 16,870.00 USD | 88,340.00 USD |
| `1D` | `4.70` | 19,020,000.00 USD | 19,020,000.00 USD | 0.00 USD | 69,690.00 USD | 97,490.00 USD | 175,270.00 USD |
| `7D` | `4.70` | 16,420,000.00 USD | 16,420,000.00 USD | 0.00 USD | 74,240.00 USD | 60,360.00 USD | 181,350.00 USD |
| `1D` | `4.71` | 20,060,000.00 USD | 20,060,000.00 USD | 0.00 USD | 390,710.00 USD | 298,900.00 USD | 353,490.00 USD |
| `7D` | `4.71` | 16,910,000.00 USD | 16,910,000.00 USD | 0.00 USD | 178,360.00 USD | 232,800.00 USD | 78,760.00 USD |
| `1D` | `4.72` | 20,300,000.00 USD | 20,300,000.00 USD | 0.00 USD | 2,370.00 USD | 181,280.00 USD | 49,950.00 USD |
| `7D` | `4.72` | 17,120,000.00 USD | 17,120,000.00 USD | 0.00 USD | 7,140.00 USD | 17,360.00 USD | 180,490.00 USD |
| `1D` | `4.73` | 20,470,000.00 USD | 20,470,000.00 USD | 0.00 USD | 109,760.00 USD | 25,210.00 USD | 35,480.00 USD |
| `7D` | `4.73` | 17,200,000.00 USD | 17,200,000.00 USD | 0.00 USD | 59,970.00 USD | 15,660.00 USD | 894.74 USD |
| `1D` | `4.74` | 20,850,000.00 USD | 20,850,000.00 USD | 0.00 USD | 68,200.00 USD | 132,280.00 USD | 176,190.00 USD |
| `7D` | `4.74` | 17,580,000.00 USD | 17,580,000.00 USD | 0.00 USD | 14,750.00 USD | 191,030.00 USD | 182,880.00 USD |
| `1D` | `4.75` | 21,220,000.00 USD | 21,220,000.00 USD | 0.00 USD | 76,690.00 USD | 141,340.00 USD | 151,830.00 USD |
| `7D` | `4.75` | 18,130,000.00 USD | 18,130,000.00 USD | 0.00 USD | 17,340.00 USD | 185,060.00 USD | 343,810.00 USD |
| `1D` | `4.76` | 21,330,000.00 USD | 21,330,000.00 USD | 0.00 USD | 32,430.00 USD | 51,460.00 USD | 31,810.00 USD |
| `7D` | `4.76` | 19,480,000.00 USD | 19,480,000.00 USD | 0.00 USD | 1,030,000.00 USD | 46,890.00 USD | 272,680.00 USD |
| `1D` | `4.77` | 21,470,000.00 USD | 21,470,000.00 USD | 0.00 USD | 4,870.00 USD | 85,030.00 USD | 47,800.00 USD |
| `7D` | `4.77` | 20,380,000.00 USD | 20,380,000.00 USD | 0.00 USD | 732,640.00 USD | 73,410.00 USD | 101,640.00 USD |
| `1D` | `4.78` | 21,610,000.00 USD | 21,610,000.00 USD | 0.00 USD | 37,290.00 USD | 20,000.00 USD | 87,070.00 USD |
| `7D` | `4.78` | 21,520,000.00 USD | 21,520,000.00 USD | 0.00 USD | 499,950.00 USD | 477,230.00 USD | 154,510.00 USD |
| `1D` | `4.79` | 21,820,000.00 USD | 21,820,000.00 USD | 0.00 USD | 101,950.00 USD | 44,330.00 USD | 59,260.00 USD |
| `7D` | `4.79` | 22,550,000.00 USD | 22,550,000.00 USD | 0.00 USD | 713,060.00 USD | 249,310.00 USD | 72,120.00 USD |
| `1D` | `4.80` | 22,330,000.00 USD | 22,330,000.00 USD | 0.00 USD | 226,540.00 USD | 128,360.00 USD | 159,500.00 USD |
| `7D` | `4.80` | 24,140,000.00 USD | 24,140,000.00 USD | 0.00 USD | 1,160,000.00 USD | 432,340.00 USD | 2,480.00 USD |
| `1D` | `4.81` | 22,370,000.00 USD | 22,370,000.00 USD | 0.00 USD | 0.00 USD | 30,450.00 USD | 11,630.00 USD |
| `7D` | `4.81` | 24,770,000.00 USD | 24,770,000.00 USD | 0.00 USD | 400,800.00 USD | 125,900.00 USD | 101,780.00 USD |
| `1D` | `4.82` | 22,500,000.00 USD | 22,500,000.00 USD | 0.00 USD | 8,250.00 USD | 81,720.00 USD | 35,520.00 USD |
| `7D` | `4.82` | 27,540,000.00 USD | 27,540,000.00 USD | 0.00 USD | 1,010,000.00 USD | 369,430.00 USD | 1,390,000.00 USD |
| `1D` | `4.83` | 22,520,000.00 USD | 22,520,000.00 USD | 0.00 USD | 15,330.00 USD | 5,610.00 USD | 129.50 USD |
| `7D` | `4.83` | 29,180,000.00 USD | 29,180,000.00 USD | 0.00 USD | 822,860.00 USD | 85,680.00 USD | 739,630.00 USD |
| `1D` | `4.84` | 22,670,000.00 USD | 22,670,000.00 USD | 0.00 USD | 38,320.00 USD | 76,320.00 USD | 34,780.00 USD |
| `7D` | `4.84` | 29,680,000.00 USD | 29,680,000.00 USD | 0.00 USD | 97,300.00 USD | 71,790.00 USD | 322,840.00 USD |
| `1D` | `4.85` | 22,800,000.00 USD | 22,800,000.00 USD | 0.00 USD | 104,560.00 USD | 0.00 USD | 28,210.00 USD |
| `7D` | `4.85` | 31,710,000.00 USD | 31,710,000.00 USD | 0.00 USD | 487,940.00 USD | 380,760.00 USD | 1,160,000.00 USD |
| `7D` | `4.86` | 33,120,000.00 USD | 33,120,000.00 USD | 0.00 USD | 444,810.00 USD | 162,380.00 USD | 802,380.00 USD |
| `7D` | `4.87` | 34,180,000.00 USD | 34,180,000.00 USD | 0.00 USD | 264,730.00 USD | 136,820.00 USD | 663,430.00 USD |
| `7D` | `4.88` | 35,670,000.00 USD | 35,670,000.00 USD | 0.00 USD | 428,040.00 USD | 266,980.00 USD | 789,710.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `1.12B` | Total OI Tokens: `257,714,457.9 NEAR`
  * 1h OI Change: `+0.24%` | 4h OI Change: `+0.12%` | 24h OI Change: `-11.30%`
  * Exchange Breakdown: Binance=`201.24M` | Bybit=`151.69M` | OKX=`52.47M` | Hyperliquid=`246.04M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `-148.06K` | Last 24h: `-22.13K` | Last 3d: `231.31K` | Last 7d: `198.53K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `-0.0008%` | **USDT OKX** | `-0.0312%` |
| **USDT Bybit** | `-0.0823%` | **USDT KuCoin** | `0.0100%` |
| **USDT MEXC** | `-0.0006%` | **USDT BingX** | `-0.0002%` |
| **USDT Gate** | `-0.0162%` | **USDT Bitget** | `-0.0505%` |
| **CoinM Binance** | `0.0100%` | **CoinM OKX** | `-` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `NEAR` | `57.06%` | `42.94%` | `1.33` | 2,920,000.00 USD |
| `15M` | `Binance` | `62.21%` | `37.79%` | `1.65` | 612,340.00 USD |
| `15M` | `OKX` | `67%` | `33%` | `2.03` | 194,320.00 USD |
| `15M` | `Bybit` | `48.99%` | `51.01%` | `0.96` | 160,330.00 USD |
| `15M` | `KuCoin` | `38.19%` | `61.81%` | `0.62` | 25,120.00 USD |
| `15M` | `Gate` | `64.94%` | `35.06%` | `1.85` | 50,900.00 USD |
| `15M` | `Bitget` | `66.99%` | `33.01%` | `2.03` | 56,080.00 USD |
| `15M` | `BingX` | `53.45%` | `46.55%` | `1.15` | 1,000,000.00 USD |
| `15M` | `MEXC` | `88.18%` | `11.82%` | `7.46` | 236,080.00 USD |
| `15M` | `Bitunix` | `66.38%` | `33.62%` | `1.97` | 41,860.00 USD |
| `15M` | `Hyperliquid` | `70.79%` | `29.21%` | `2.42` | 29,470.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `55.22%` | `44.78%` | `1.23` | 323,120.00 USD |
| `15M` | `Crypto.com` | `0.89%` | `99.11%` | `0.01` | 662.67 USD |
| `15M` | `WhiteBIT` | `10.08%` | `89.92%` | `0.11` | 173,320.00 USD |
| `15M` | `HTX` | `74%` | `26%` | `2.85` | 1,270.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `51.55%` | `48.45%` | `1.06` | 4,620.00 USD |
| `15M` | `Aster` | `56.22%` | `43.78%` | `1.28` | 135.67 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `52.76%` | `47.24%` | `1.12` | 5,990.00 USD |
| `15M` | `Whale Positions` | `62.21%` | `37.79%` | `1.65` | 612,340.00 USD |
| `15M` | `Global Accounts` | `57.06%` | `42.94%` | `1.33` | 2,920,000.00 USD |
| `1H` | `NEAR` | `45.45%` | `54.55%` | `0.83` | 19,670,000.00 USD |
| `1H` | `Binance` | `47.76%` | `52.24%` | `0.91` | 6,670,000.00 USD |
| `1H` | `OKX` | `50.3%` | `49.7%` | `1.01` | 1,280,000.00 USD |
| `1H` | `Bybit` | `47.87%` | `52.13%` | `0.92` | 1,220,000.00 USD |
| `1H` | `KuCoin` | `59.15%` | `40.85%` | `1.45` | 123,740.00 USD |
| `1H` | `Gate` | `37.77%` | `62.23%` | `0.61` | 266,580.00 USD |
| `1H` | `Bitget` | `49.72%` | `50.28%` | `0.99` | 475,140.00 USD |
| `1H` | `BingX` | `35.35%` | `64.65%` | `0.55` | 1,260,000.00 USD |
| `1H` | `MEXC` | `50.09%` | `49.91%` | `1.00` | 4,890,000.00 USD |
| `1H` | `Bitunix` | `30.64%` | `69.36%` | `0.44` | 792,560.00 USD |
| `1H` | `Hyperliquid` | `46.58%` | `53.42%` | `0.87` | 384,790.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `49.97%` | `50.03%` | `1.00` | 1,170,000.00 USD |
| `1H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `WhiteBIT` | `0.32%` | `99.68%` | `0.00` | 875,550.00 USD |
| `1H` | `HTX` | `74.37%` | `25.63%` | `2.90` | 28,640.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `86.99%` | `13.01%` | `6.69` | 121,530.00 USD |
| `1H` | `Aster` | `92.86%` | `7.14%` | `13.01` | 65,340.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `53.31%` | `46.69%` | `1.14` | 47,160.00 USD |
| `1H` | `Whale Positions` | `47.76%` | `52.24%` | `0.91` | 6,670,000.00 USD |
| `1H` | `Global Accounts` | `45.45%` | `54.55%` | `0.83` | 19,670,000.00 USD |
| `4H` | `NEAR` | `44.27%` | `55.73%` | `0.79` | 70,000,000.00 USD |
| `4H` | `Binance` | `49.52%` | `50.48%` | `0.98` | 22,300,000.00 USD |
| `4H` | `OKX` | `44.3%` | `55.7%` | `0.80` | 4,060,000.00 USD |
| `4H` | `Bybit` | `41.82%` | `58.18%` | `0.72` | 4,620,000.00 USD |
| `4H` | `KuCoin` | `52.92%` | `47.08%` | `1.12` | 462,010.00 USD |
| `4H` | `Gate` | `56.46%` | `43.54%` | `1.30` | 1,640,000.00 USD |
| `4H` | `Bitget` | `40.84%` | `59.16%` | `0.69` | 1,240,000.00 USD |
| `4H` | `BingX` | `36.87%` | `63.13%` | `0.58` | 17,390,000.00 USD |
| `4H` | `MEXC` | `42.06%` | `57.94%` | `0.73` | 3,630,000.00 USD |
| `4H` | `Bitunix` | `44.14%` | `55.86%` | `0.79` | 1,220,000.00 USD |
| `4H` | `Hyperliquid` | `32.75%` | `67.25%` | `0.49` | 542,110.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `49.06%` | `50.94%` | `0.96` | 11,170,000.00 USD |
| `4H` | `Crypto.com` | `35.63%` | `64.37%` | `0.55` | 5,900.00 USD |
| `4H` | `WhiteBIT` | `21.01%` | `78.99%` | `0.27` | 1,460,000.00 USD |
| `4H` | `HTX` | `46.55%` | `53.45%` | `0.87` | 59,330.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `20.93%` | `79.07%` | `0.26` | 22,300.00 USD |
| `4H` | `Aster` | `9.32%` | `90.68%` | `0.10` | 55,680.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `44.8%` | `55.2%` | `0.81` | 121,650.00 USD |
| `4H` | `Whale Positions` | `49.52%` | `50.48%` | `0.98` | 22,300,000.00 USD |
| `4H` | `Global Accounts` | `44.27%` | `55.73%` | `0.79` | 70,000,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `0:00 UTC` | `4.31` | `4.31` | `4.31` | `4.33` | `4.29` | 8,450,528.91 USD | 3,282,248.80 USD | 5,168,280.11 USD | -1,886,031.31 USD | `-22.32%` | `1B / 7S` |
| `5:00 UTC` | `4.34` | `4.31` | `4.34` | `4.36` | `4.27` | 7,427,881.94 USD | 3,957,867.39 USD | 3,470,014.55 USD | 487,852.84 USD | `+6.57%` | `16B / 5S` |
| `0:00 UTC` | `4.31` | `4.31` | `4.31` | `4.34` | `4.28` | 9,663,695.00 USD | 3,248,414.35 USD | 6,415,280.65 USD | -3,166,866.30 USD | `-32.77%` | `1B / 19S` |
| `5:00 UTC` | `4.28` | `4.29` | `4.28` | `4.30` | `4.28` | 4,754,194.91 USD | 2,441,201.28 USD | 2,312,993.62 USD | 128,207.66 USD | `+2.70%` | `1B / 2S` |
| `0:00 UTC` | `4.25` | `4.26` | `4.25` | `4.30` | `4.21` | 16,835,236.87 USD | 7,874,403.92 USD | 8,960,832.95 USD | -1,086,429.03 USD | `-6.45%` | `8B / 9S` |
| `5:00 UTC` | `4.25` | `4.25` | `4.25` | `4.26` | `4.23` | 9,185,944.44 USD | 4,818,806.27 USD | 4,367,138.17 USD | 451,668.11 USD | `+4.92%` | `4B / 5S` |
| `0:00 UTC` | `4.30` | `4.30` | `4.30` | `4.36` | `4.24` | 30,489,684.47 USD | 19,297,257.05 USD | 11,192,427.43 USD | 8,104,829.62 USD | `+26.58%` | `32B / 2S` |
| `5:00 UTC` | `4.35` | `4.35` | `4.35` | `4.36` | `4.33` | 15,245,662.84 USD | 8,049,667.44 USD | 7,195,995.40 USD | 853,672.05 USD | `+5.60%` | `0B / 3S` |
| `0:00 UTC` | `4.33` | `4.33` | `4.33` | `4.35` | `4.31` | 8,553,382.74 USD | 3,656,231.21 USD | 4,897,151.53 USD | -1,240,920.31 USD | `-14.51%` | `1B / 5S` |
| `5:00 UTC` | `4.31` | `4.35` | `4.31` | `4.39` | `4.31` | 11,451,410.96 USD | 6,275,300.17 USD | 5,176,110.79 USD | 1,099,189.39 USD | `+9.60%` | `19B / 4S` |

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
| `5m` | 243,270.00 USD | -1,630,000.00 USD | **`DISTRIBUTION`** |
| `15m` | 809,780.00 USD | 1,550,000.00 USD | **`ACCUMULATION`** |
| `30m` | 929,730.00 USD | -790,200.00 USD | **`ACCUMULATION`** |
| `1h` | 5,500,000.00 USD | 11,340,000.00 USD | **`ACCUMULATION`** |
| `2h` | 9,430,000.00 USD | 3,770,000.00 USD | **`ACCUMULATION`** |
| `4h` | 15,520,000.00 USD | 1,530,000.00 USD | **`ACCUMULATION`** |
| `6h` | 20,290,000.00 USD | 10,300,000.00 USD | **`ACCUMULATION`** |
| `8h` | 22,460,000.00 USD | 3,540,000.00 USD | **`ACCUMULATION`** |
| `12h` | 16,100,000.00 USD | 4,100,000.00 USD | **`ACCUMULATION`** |
| `24h` | 1,370,000.00 USD | -22,560,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -60,790,000.00 USD | -130,770,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -226,600,000.00 USD | -665,940,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+243.27K` | 15m=`+809.78K` | 1h=`+5.50M` | 24h=`+1.37M`
* Futures Capital Netflows: 5m=`-1.63M` | 15m=`+1.55M` | 1h=`+11.34M` | 24h=`-22.56M`
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
  * `2026-10-30 14:09:50 IST`: [channelnewsasia.com] - (Sentiment: `Neutral`)
  * `2026-10-30 13:51:50 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 13:50:50 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 13:31:50 IST`: [kof.ethz.ch] - (Sentiment: `Neutral`)
  * `2026-10-30 14:27:50 IST`: [gerlachmacro.substack.com] - (Sentiment: `Neutral`)
  * `2026-10-30 14:27:50 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-30 14:27:50 IST`: [insee.fr] - (Sentiment: `Neutral`)
  * `2026-10-30 14:27:50 IST`: [insee.fr] - (Sentiment: `Neutral`)
  * `2026-10-30 14:27:50 IST`: [@FirstSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 14:27:50 IST`: [nationwide.co.uk] - (Sentiment: `Neutral`)
  * `2026-10-30 14:27:50 IST`: [destatis.de] - (Sentiment: `Neutral`)
  * `2026-10-30 14:26:50 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-30 14:26:50 IST`: [@FirstSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 14:26:50 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-30 14:26:50 IST`: [insee.fr] - (Sentiment: `Neutral`)


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
  * Spread-Padded Stop Loss: `3.83` (Risk Distance: `0.1135` pts)
  * +2.5R Take Profit: `4.22`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `4.21` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `4.32` (Risk Distance: `0.1135` pts)
  * +2.5R Take Profit: `3.92`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`4.39`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
