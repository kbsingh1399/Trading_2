# 🏛️ SOVEREIGN CANDIDATE DOSSIER: NEAR
**Canonical Key**: `NEAR` | **Broker Instrument**: `NERUSD.p` | **Asset Class**: `Crypto Alt L1`
**Timestamp**: `2026-10-30 15:42:19 IST` (`2026-10-30 10:12:19 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `4.33` | **Live Ask Quote**: `4.36` | **Mid Price**: `4.35`
- **Spread Points**: `29.00` | **Spread BPS**: `66.74 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `4.14` | VWAP Z-Score: `+1.57` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `0.0552` (Volatility Regime: `HIGH_EXPANSION`)
  * 14-Period RSI: `63.10` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `4.56` | Lower -3.00σ Band: `3.71`
  * Upper +2.51σ Band: `4.49` | Lower -2.51σ Band: `3.78`
  * Upper +2.01σ Band: `4.42` | Lower -2.01σ Band: `3.85`
  * Upper +2.00σ Band: `4.42` | Lower -2.00σ Band: `3.85`
  * Upper +1.28σ Band: `4.32` | Lower -1.28σ Band: `3.95`
  * Upper +1.00σ Band: `4.28` | Lower -1.00σ Band: `3.99`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`4.32` | EMA-20=`4.28` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`4.24` (Slope: `+0.0000`) | EMA-100=`4.29`
  * Institutional Anchors: EMA-144=`4.33` | EMA-200=`4.38` (Slope: `-0.2353`) | EMA-233=`4.41`
- **Range Boundaries**: 24H High=`4.67` | 24H Low=`3.89` | Weekly High=`4.80` | Weekly Low=`3.89`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `4.23` (Distance: `+2.73%`)
  * Point of Control (POC) = `4.07` (Distance: `+6.88%`)
  * Value Area Low (VAL) = `3.94` (Distance: `+10.38%`)
  * Auction Positioning: `ABOVE_VALUE (Imbalance)` | Session Bias: **`BULLISH (Above Pivot)`** | Market Regime: `RANGE_EXPANSION`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`4.57` | POC=`4.41` | VAL=`4.29`
  * Prior Day Extremes: PDH=`4.75` | PDL=`4.08` | PDC=`4.15`
  * Monday Range Blueprint: High=`4.65` | Mid=`4.53` | Low=`4.41`
  * Developing Weekly Value Area: Weekly VAH=`4.71` | Weekly POC=`4.45` | Weekly VAL=`4.39`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`4.26` | Low=`3.89`
  * London Session (08:00-16:00 UTC): High=`4.37` | Low=`4.15`
  * New York Session (13:00-21:00 UTC): High=`4.36` | Low=`4.32`
  * Initial Balance (First Hour): IB High=`4.27` | IB Low=`4.17`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `4.33` - `4.36`
  * Optimal Trade Entry (OTE 0.705): `4.35`
  * Structural Invalidation Anchor (0.786): `4.38`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `4.36` | `4.36` | `4.34` | `4.36` | `442,208` | 1,922,562.92 USD | -252,146.30 USD | `-13.12%` | -6,904,552.65 USD | `-0.44` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `5m` | `4.36` | `4.37` | `4.36` | `4.37` | `431,921` | 1,884,723.70 USD | 406,193.44 USD | `+21.55%` | -6,498,359.22 USD | `+0.46` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `5m` | `4.37` | `4.38` | `4.36` | `4.38` | `467,436` | 2,044,256.75 USD | 258,144.92 USD | `+12.63%` | -6,240,214.29 USD | `+0.34` | **`BULLISH`** | `DELTA ALIGNED` |
| `15m` | `4.32` | `4.36` | `4.29` | `4.36` | `1,336,780` | 5,778,991.37 USD | -52,711.67 USD | `-0.91%` | -6,786,143.49 USD | `-0.12` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `15m` | `4.36` | `4.38` | `4.34` | `4.38` | `1,396,865` | 6,093,690.79 USD | 603,495.51 USD | `+9.90%` | -6,182,647.98 USD | `+0.13` | **`BULLISH`** | `DELTA ALIGNED` |
| `15m` | `4.38` | `4.38` | `4.33` | `4.35` | `1,246,417` | 5,420,832.95 USD | -696,485.48 USD | `-12.85%` | -6,879,133.46 USD | `-0.41` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `4.25` | `4.39` | `4.24` | `4.36` | `15,226,975` | 65,865,283.41 USD | 8,809,838.63 USD | `+13.38%` | -7,440,212.42 USD | `+2.04` | **`BULLISH`** | `DELTA ALIGNED` |
| `1h` | `4.36` | `4.38` | `4.29` | `4.38` | `6,481,728` | 28,107,012.78 USD | 1,024,636.46 USD | `+3.65%` | -6,415,575.95 USD | `+0.27` | **`BULLISH`** | `NEUTRAL CHOP` |
| `1h` | `4.38` | `4.38` | `4.33` | `4.35` | `1,246,113` | 5,419,510.55 USD | -697,807.88 USD | `-12.88%` | -7,113,383.83 USD | `-0.11` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `4.06` | `4.17` | `3.90` | `4.16` | `46,830,819` | 188,194,075.16 USD | -412,364.95 USD | `-0.22%` | -12,215,320.93 USD | `+0.44` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `4.16` | `4.36` | `4.12` | `4.25` | `33,821,215` | 143,651,581.49 USD | -2,835,728.00 USD | `-1.97%` | -15,051,048.93 USD | `+0.03` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `4.25` | `4.39` | `4.24` | `4.38` | `21,653,403` | 93,730,148.77 USD | 9,643,171.64 USD | `+10.29%` | -5,407,877.29 USD | `+1.55` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `4.65` | `4.69` | `4.38` | `4.40` | `28,351,581` | 128,263,626.10 USD | -4,168,943.82 USD | `-3.25%` | 240,083.28 USD | `-1.00` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `4.40` | `4.41` | `4.04` | `4.06` | `71,964,012` | 300,508,235.77 USD | -12,043,039.27 USD | `-4.01%` | -11,802,955.99 USD | `-1.21` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `4.06` | `4.17` | `3.90` | `4.16` | `46,830,819` | 188,194,075.16 USD | -412,364.95 USD | `-0.22%` | -12,215,320.93 USD | `+0.44` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `4.16` | `4.36` | `4.12` | `4.25` | `33,821,215` | 143,651,581.49 USD | -2,835,728.00 USD | `-1.97%` | -15,051,048.93 USD | `+0.03` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `4.25` | `4.39` | `4.24` | `4.35` | `22,954,816` | 99,391,806.74 USD | 9,136,667.22 USD | `+9.19%` | -5,914,381.71 USD | `+1.52` | **`BULLISH`** | `DELTA ALIGNED` |

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
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 15:40:55 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `51` | `0x7737...bf66` | `LONG` | 24,680,594.58 USD | `5,640,376.30` | `2.35` | `4.35` | `0.8339` | 11,408,691.75 USD | `+46.23%` | `10X Cross` |
| `91` | `0xefe4...194b` | `SHORT` | 19,616,057.13 USD | `4,507,262.50` | `4.21` | `4.35` | `6.46` | -640,960.41 USD | `-3.27%` | `5X Cross` |
| `124` | `0xb581...6f4f` | `LONG` | 15,669,720.00 USD | `3,600,000.00` | `5.19` | `4.35` | `0.000000` | -3,023,315.22 USD | `-19.29%` | `4X Cross` |
| `201` | `0xdd53...2b13` | `SHORT` | 10,470,641.20 USD | `2,400,202.00` | `2.31` | `4.35` | `28.85` | -4,924,792.65 USD | `-47.03%` | `3X Cross` |
| `249` | `0x77ee...2902` | `LONG` | 9,026,551.27 USD | `2,063,023.10` | `1.93` | `4.35` | `0.000000` | 5,035,355.34 USD | `+55.78%` | `10X Cross` |
| `346` | `0x9df2...c665` | `SHORT` | 6,609,622.76 USD | `1,514,579.00` | `2.36` | `4.35` | `24.25` | -3,029,633.09 USD | `-45.84%` | `10X Cross` |
| `364` | `0xb83d...6e36` | `SHORT` | 6,302,208.49 USD | `1,445,759.10` | `5.19` | `4.35` | `81.88` | 1,207,240.45 USD | `+19.16%` | `3X Cross` |
| `365` | `0x7fda...17d1` | `SHORT` | 6,297,202.53 USD | `1,443,915.10` | `4.28` | `4.35` | `29.90` | -115,124.01 USD | `-1.83%` | `10X Cross` |
| `387` | `0xb46b...538e` | `SHORT` | 5,831,907.20 USD | `1,336,000.00` | `4.33` | `4.35` | `7.43` | -47,043.14 USD | `-0.81%` | `10X Cross` |
| `445` | `0x60b0...991e` | `LONG` | 4,901,121.20 USD | `1,121,307.10` | `5.00` | `4.35` | `0.000000` | -700,303.23 USD | `-14.29%` | `10X Cross` |
| `488` | `0x781e...96b7` | `SHORT` | 4,538,289.92 USD | `1,039,604.60` | `2.45` | `4.35` | `7.53` | -1,993,952.73 USD | `-43.94%` | `10X Cross` |
| `557` | `0x45d2...4029` | `SHORT` | 3,969,803.82 USD | `909,400.00` | `3.26` | `4.35` | `49.72` | -1,003,653.92 USD | `-25.28%` | `10X Cross` |
| `565` | `0x4cae...7c34` | `LONG` | 3,940,430.11 USD | `900,587.40` | `3.97` | `4.35` | `3.07` | 362,237.32 USD | `+9.19%` | `10X Cross` |
| `794` | `0x005a...61fe` | `LONG` | 2,846,615.38 USD | `652,414.60` | `2.08` | `4.35` | `2.42` | 1,489,084.15 USD | `+52.31%` | `7X Cross` |
| `801` | `0xba5d...a352` | `SHORT` | 2,831,076.84 USD | `647,532.50` | `2.83` | `4.35` | `11.65` | -998,361.90 USD | `-35.26%` | `10X Cross` |
| `810` | `0xb695...a92d` | `SHORT` | 2,790,438.14 USD | `639,231.70` | `4.57` | `4.35` | `38.97` | 132,920.79 USD | `+4.76%` | `10X Cross` |
| `815` | `0xd1dd...9e85` | `SHORT` | 2,774,990.35 USD | `637,621.00` | `4.96` | `4.35` | `18.69` | 388,482.38 USD | `+14.00%` | `10X Cross` |
| `825` | `0x123d...3bff` | `SHORT` | 2,731,486.13 USD | `624,568.10` | `2.09` | `4.35` | `9.12` | -1,426,061.95 USD | `-52.21%` | `10X Cross` |
| `828` | `0xcf53...ee11` | `SHORT` | 2,718,809.24 USD | `621,598.40` | `5.07` | `4.35` | `25.24` | 433,361.01 USD | `+15.94%` | `10X Cross` |
| `949` | `0xbfc7...80b4` | `SHORT` | 2,322,275.40 USD | `531,000.00` | `2.01` | `4.35` | `7.22` | -1,257,076.01 USD | `-54.13%` | `10X Cross` |
| `1091` | `0xf382...578c` | `SHORT` | 1,985,396.56 USD | `454,948.80` | `4.32` | `4.35` | `6.37` | -21,892.05 USD | `-1.10%` | `10X Cross` |
| `1175` | `0x0eec...d4c5` | `LONG` | 1,859,074.20 USD | `426,481.20` | `4.02` | `4.35` | `2.02` | 145,543.00 USD | `+7.83%` | `10X Cross` |
| `1254` | `0xe097...d0fe` | `LONG` | 1,747,760.00 USD | `400,000.00` | `5.29` | `4.35` | `0.000000` | -369,027.30 USD | `-21.11%` | `10X Cross` |
| `1354` | `0x6e8f...4364` | `LONG` | 1,577,586.86 USD | `361,210.50` | `3.28` | `4.35` | `3.55` | 393,526.63 USD | `+24.94%` | `10X Cross` |
| `1361` | `0xef96...9383` | `SHORT` | 1,572,087.18 USD | `360,644.90` | `4.50` | `4.35` | `13.81` | 51,020.16 USD | `+3.25%` | `10X Cross` |
| `1415` | `0xcf67...eb24` | `LONG` | 1,530,830.00 USD | `350,000.00` | `1.98` | `4.35` | `1.60` | 839,212.12 USD | `+54.82%` | `10X Cross` |
| `1422` | `0xdf95...7d72` | `SHORT` | 1,524,508.80 USD | `350,244.40` | `4.23` | `4.35` | `111.50` | -42,164.54 USD | `-2.77%` | `10X Cross` |
| `1521` | `0xcac1...26b3` | `SHORT` | 1,411,426.28 USD | `323,743.90` | `2.48` | `4.35` | `31.03` | -609,428.27 USD | `-43.18%` | `10X Cross` |
| `1538` | `0xfc27...9d9d` | `SHORT` | 1,395,957.97 USD | `319,997.70` | `5.01` | `4.35` | `62.55` | 207,584.66 USD | `+14.87%` | `10X Cross` |
| `1542` | `0x089f...a4f8` | `LONG` | 1,392,049.73 USD | `319,043.30` | `4.06` | `4.35` | `0.000000` | 97,193.02 USD | `+6.98%` | `1X Cross` |
| `1589` | `0x17c3...a868` | `LONG` | 1,337,772.64 USD | `306,168.50` | `4.36` | `4.35` | `0.000000` | 2,048.14 USD | `+0.15%` | `3X Cross` |
| `1680` | `0xe065...0f85` | `SHORT` | 1,255,542.42 USD | `288,027.90` | `2.81` | `4.35` | `5.63` | -444,989.30 USD | `-35.44%` | `10X Cross` |
| `1874` | `0xff43...d924` | `LONG` | 1,091,575.67 USD | `249,474.50` | `4.64` | `4.35` | `3.28` | -66,468.00 USD | `-6.09%` | `10X Isolated` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
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
  * 24H Horizon: Short MP=`4.42` (Vol: 795,900.00 USD, Dist: `+1.52%`) | Long MP=`4.18` (Vol: 505,600.00 USD, Dist: `--3.95%`)
  * 48H Horizon: Short MP=`4.41` (Vol: 795,900.00 USD, Dist: `+1.44%`) | Long MP=`4.18` (Vol: 505,600.00 USD, Dist: `--3.95%`)
  * 3D Horizon: Short MP=`4.41` (Vol: 795,900.00 USD, Dist: `+1.44%`) | Long MP=`4.18` (Vol: 505,600.00 USD, Dist: `--3.95%`)
  * 7D Horizon: Short MP=`4.42` (Vol: 795,900.00 USD, Dist: `+1.58%`) | Long MP=`4.18` (Vol: 505,600.00 USD, Dist: `--3.86%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long Liquidation` | `0.8750` | 1,660.00 USD | 22,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8950` | 39,060.00 USD | 22,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9050` | 292.22 USD | 22,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9150` | 11,370.00 USD | 22,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9250` | 1,850.00 USD | 22,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9350` | 29,760.00 USD | 22,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9550` | 2,890.00 USD | 22,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9650` | 965.00 USD | 22,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9850` | 707.53 USD | 22,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9950` | 154,200.00 USD | 22,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.00` | 2,560.00 USD | 21,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.02` | 11,240.00 USD | 21,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.03` | 36,980.00 USD | 21,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.04` | 2,740.00 USD | 21,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.05` | 6,860.00 USD | 21,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.06` | 892.90 USD | 21,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.07` | 5,310.00 USD | 21,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.08` | 470,570.00 USD | 21,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.09` | 6,690.00 USD | 21,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.10` | 1,430.00 USD | 21,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.11` | 2,160.00 USD | 21,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.12` | 856.24 USD | 21,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.14` | 4,960.00 USD | 21,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.15` | 26,780.00 USD | 21,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.17` | 1,810.00 USD | 21,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.18` | 647.54 USD | 21,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.19` | 12,420.00 USD | 21,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.20` | 148.42 USD | 21,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.24` | 18,650.00 USD | 21,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.25` | 250.87 USD | 21,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.25` | 15,020.00 USD | 21,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.26` | 2,060.00 USD | 21,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.27` | 2,390.00 USD | 21,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.28` | 1,160.00 USD | 21,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.29` | 258.35 USD | 21,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.30` | 116.80 USD | 21,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.32` | 9,260.00 USD | 21,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.33` | 148.32 USD | 21,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.34` | 603.91 USD | 21,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.35` | 66,360.00 USD | 21,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.36` | 725.63 USD | 21,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.38` | 10,080.00 USD | 21,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.39` | 12,760.00 USD | 21,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.40` | 1,060.00 USD | 21,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.41` | 27,720.00 USD | 21,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.42` | 76,020.00 USD | 21,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.43` | 1,130.00 USD | 21,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.45` | 1,530.00 USD | 21,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.46` | 5,440.00 USD | 21,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.47` | 14,940.00 USD | 21,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.48` | 2,290.00 USD | 21,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.49` | 3,110.00 USD | 21,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.50` | 2,740.00 USD | 21,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.51` | 454.50 USD | 21,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.53` | 2,340.00 USD | 21,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.54` | 169.95 USD | 21,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.55` | 1,450.00 USD | 21,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.56` | 20,570.00 USD | 21,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.57` | 1,020.00 USD | 20,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.58` | 2,180.00 USD | 20,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.59` | 3,700.00 USD | 20,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.60` | 191.64 USD | 20,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.64` | 6,790.00 USD | 20,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.65` | 582,010.00 USD | 20,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.66` | 83,540.00 USD | 20,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.67` | 6,160.00 USD | 20,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.68` | 1,520.00 USD | 20,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.69` | 17,300.00 USD | 20,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.70` | 102.72 USD | 20,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.73` | 5,460.00 USD | 20,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.75` | 23,850.00 USD | 20,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.76` | 2,510.00 USD | 20,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.77` | 4,330.00 USD | 20,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.79` | 456.47 USD | 20,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.80` | 529.05 USD | 20,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.81` | 1,580.00 USD | 20,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.82` | 853.74 USD | 20,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.83` | 36,780.00 USD | 20,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.85` | 984.26 USD | 20,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.86` | 16,100.00 USD | 20,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.88` | 656.25 USD | 20,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.90` | 37,060.00 USD | 20,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.91` | 288.61 USD | 20,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.93` | 1,120.00 USD | 20,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.94` | 1,270.00 USD | 20,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.95` | 2,740.00 USD | 20,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.96` | 2,860.00 USD | 20,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.97` | 1,730.00 USD | 20,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.98` | 35,130.00 USD | 20,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.00` | 46,610.00 USD | 20,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.02` | 3,100.00 USD | 20,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.02` | 3,660.00 USD | 20,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.04` | 323.36 USD | 20,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.04` | 3,460.00 USD | 20,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.06` | 1,100.00 USD | 20,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.06` | 2,520.00 USD | 20,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.08` | 11,100.00 USD | 20,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.08` | 18,600.00 USD | 20,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.10` | 17,340.00 USD | 20,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.10` | 6,090.00 USD | 19,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.12` | 14,240.00 USD | 19,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.12` | 8,770.00 USD | 19,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.13` | 2,140.00 USD | 19,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.15` | 2,110.00 USD | 19,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.15` | 4,550.00 USD | 19,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.17` | 279,760.00 USD | 19,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.17` | 14,140.00 USD | 19,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.19` | 1,110.00 USD | 19,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.19` | 12,830.00 USD | 19,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.21` | 39,620.00 USD | 19,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.21` | 91,610.00 USD | 19,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.23` | 457.24 USD | 19,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.23` | 2,450.00 USD | 19,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.25` | 38,480.00 USD | 19,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.25` | 329,770.00 USD | 19,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.27` | 1,580.00 USD | 19,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.27` | 812.18 USD | 19,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.29` | 463.86 USD | 19,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.29` | 11,990.00 USD | 19,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.31` | 7,500.00 USD | 19,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.31` | 2,330.00 USD | 19,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.33` | 13,770.00 USD | 19,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.33` | 30,690.00 USD | 19,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.35` | 5,790.00 USD | 19,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.35` | 25,910.00 USD | 19,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.37` | 3,840.00 USD | 19,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.38` | 35,180.00 USD | 19,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.38` | 6,250.00 USD | 19,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.40` | 119,870.00 USD | 19,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.40` | 11,030.00 USD | 18,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.42` | 1,760,000.00 USD | 18,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.42` | 273,060.00 USD | 17,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.44` | 4,770.00 USD | 16,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.44` | 253,220.00 USD | 16,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.46` | 49,540.00 USD | 16,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.46` | 6,090.00 USD | 16,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.48` | 336.35 USD | 16,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.48` | 3,110.00 USD | 16,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.50` | 15,100.00 USD | 16,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.50` | 6,000.00 USD | 16,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.52` | 39,960.00 USD | 16,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.54` | 866.97 USD | 16,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.54` | 105.36 USD | 16,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.56` | 621.12 USD | 16,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.56` | 7,890.00 USD | 16,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.58` | 431,260.00 USD | 16,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.58` | 11,810.00 USD | 16,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.60` | 82,820.00 USD | 16,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.60` | 779.94 USD | 15,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.62` | 1,190.00 USD | 15,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.62` | 2,470.00 USD | 15,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.63` | 24,310.00 USD | 15,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.65` | 6,020.00 USD | 15,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.65` | 16,760.00 USD | 15,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.67` | 1,920.00 USD | 15,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.67` | 172,860.00 USD | 15,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.69` | 8,920.00 USD | 15,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.69` | 733.85 USD | 15,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.71` | 170,360.00 USD | 15,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.71` | 11,750.00 USD | 15,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.73` | 28,380.00 USD | 15,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.73` | 1,850.00 USD | 15,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.75` | 39,550.00 USD | 15,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.75` | 365,820.00 USD | 15,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.77` | 8,890.00 USD | 15,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.77` | 719.84 USD | 15,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.79` | 49,490.00 USD | 15,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.79` | 12,340.00 USD | 15,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.81` | 90,180.00 USD | 14,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.81` | 4,780.00 USD | 14,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.83` | 13,990.00 USD | 14,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.83` | 2,400.00 USD | 14,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.85` | 180.94 USD | 14,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.85` | 1,970.00 USD | 14,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.87` | 21,320.00 USD | 14,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.88` | 878,580.00 USD | 14,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.88` | 7,430.00 USD | 13,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.90` | 114,000.00 USD | 13,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.90` | 199,300.00 USD | 13,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.92` | 4,900.00 USD | 13,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.92` | 48,730.00 USD | 13,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.94` | 50,520.00 USD | 13,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.94` | 16,860.00 USD | 13,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.96` | 13,510.00 USD | 13,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.96` | 104,820.00 USD | 13,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.98` | 148,230.00 USD | 13,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.98` | 5,840.00 USD | 13,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.00` | 13,250.00 USD | 13,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.00` | 11,020.00 USD | 13,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.02` | 32,670.00 USD | 13,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.02` | 20,580.00 USD | 13,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.04` | 2,570.00 USD | 13,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.04` | 109,800.00 USD | 13,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.06` | 137,520.00 USD | 13,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.06` | 163,450.00 USD | 12,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.08` | 157,420.00 USD | 12,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.08` | 50,590.00 USD | 12,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.10` | 5,110.00 USD | 12,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.10` | 22,590.00 USD | 12,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.12` | 56,190.00 USD | 12,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.12` | 2,990,000.00 USD | 12,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.13` | 10,160.00 USD | 9,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.15` | 99,300.00 USD | 9,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.15` | 4,250.00 USD | 9,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.17` | 68,020.00 USD | 9,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.17` | 1,200.00 USD | 9,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.19` | 245,320.00 USD | 9,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.19` | 258.16 USD | 9,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.21` | 5,090.00 USD | 9,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.21` | 41,620.00 USD | 9,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.23` | 23,110.00 USD | 9,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.23` | 43,760.00 USD | 8,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.25` | 20,060.00 USD | 8,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.25` | 4,050.00 USD | 8,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.27` | 33,650.00 USD | 8,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.27` | 868,070.00 USD | 8,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.29` | 4,080.00 USD | 8,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.29` | 134,250.00 USD | 8,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.31` | 132,030.00 USD | 7,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.31` | 24,690.00 USD | 7,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.33` | 13,340.00 USD | 7,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.33` | 73,460.00 USD | 7,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.35` | 18,900.00 USD | 7,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.35` | 1,210.00 USD | 7,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.37` | 41,020.00 USD | 7,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.38` | 55,170.00 USD | 7,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.38` | 46,170.00 USD | 7,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.40` | 51,750.00 USD | 7,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.40` | 104,080.00 USD | 7,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.42` | 390,810.00 USD | 7,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.42` | 13,630.00 USD | 6,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.44` | 29,830.00 USD | 6,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.44` | 26,540.00 USD | 6,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.46` | 150,240.00 USD | 6,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.46` | 16,470.00 USD | 6,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.48` | 108,220.00 USD | 6,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.48` | 18,510,000.00 USD | 18,510,000.00 USD | 45,650.00 USD | 26,250.00 USD | 1,510.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.48` | 30,100.00 USD | 6,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.50` | 48,550.00 USD | 6,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.50` | 18,440,000.00 USD | 18,440,000.00 USD | 16,960.00 USD | 6,940.00 USD | 38,050.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.50` | 68,770.00 USD | 6,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.51` | 18,380,000.00 USD | 18,380,000.00 USD | 3,690.00 USD | 0.00 USD | 231.64 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.52` | 42,280.00 USD | 6,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.52` | 18,370,000.00 USD | 18,370,000.00 USD | 15,180.00 USD | 0.00 USD | 41,090.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.52` | 21,620.00 USD | 6,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.53` | 18,320,000.00 USD | 18,320,000.00 USD | 93,360.00 USD | 40,470.00 USD | 96,140.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.54` | 84,160.00 USD | 6,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.54` | 18,090,000.00 USD | 18,090,000.00 USD | 3,040.00 USD | 58,300.00 USD | 30,480.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.54` | 152,250.00 USD | 6,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.55` | 17,990,000.00 USD | 17,990,000.00 USD | 128,490.00 USD | 54,880.00 USD | 45,330.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.56` | 570,020.00 USD | 6,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.56` | 17,770,000.00 USD | 17,770,000.00 USD | 61,170.00 USD | 0.00 USD | 32.49 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.56` | 25,750.00 USD | 5,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.57` | 17,700,000.00 USD | 17,700,000.00 USD | 86,360.00 USD | 27,910.00 USD | 84,270.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.58` | 1,340,000.00 USD | 5,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.58` | 17,510,000.00 USD | 17,510,000.00 USD | 173,980.00 USD | 48,640.00 USD | 59,950.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.58` | 120,640.00 USD | 4,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.59` | 17,220,000.00 USD | 17,220,000.00 USD | 535.75 USD | 18,170.00 USD | 78.80 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.60` | 24,010.00 USD | 4,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.60` | 17,200,000.00 USD | 17,200,000.00 USD | 64,170.00 USD | 21,460.00 USD | 22,050.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.60` | 72,910.00 USD | 4,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.61` | 17,100,000.00 USD | 17,100,000.00 USD | 56,580.00 USD | 37,060.00 USD | 44,890.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.62` | 229,270.00 USD | 3,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.62` | 16,960,000.00 USD | 16,960,000.00 USD | 92,130.00 USD | 26,640.00 USD | 97,570.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.62` | 125,580.00 USD | 3,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.63` | 16,740,000.00 USD | 16,740,000.00 USD | 50,840.00 USD | 8,120.00 USD | 159.02 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.63` | 3,550.00 USD | 3,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.64` | 16,680,000.00 USD | 16,680,000.00 USD | 2,410.00 USD | 41,960.00 USD | 119,140.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.65` | 15,050.00 USD | 3,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.65` | 16,520,000.00 USD | 16,520,000.00 USD | 53,900.00 USD | 7,050.00 USD | 31,190.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.65` | 20,860.00 USD | 3,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.66` | 16,430,000.00 USD | 16,430,000.00 USD | 32,350.00 USD | 15,090.00 USD | 125,270.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.67` | 39,720.00 USD | 3,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.67` | 16,250,000.00 USD | 16,250,000.00 USD | 52,020.00 USD | 14,480.00 USD | 53,670.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.67` | 94,680.00 USD | 3,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.68` | 16,130,000.00 USD | 16,130,000.00 USD | 1,010.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.69` | 217,880.00 USD | 3,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.69` | 16,130,000.00 USD | 16,130,000.00 USD | 27,750.00 USD | 0.00 USD | 59,840.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.69` | 102,030.00 USD | 3,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.70` | 16,050,000.00 USD | 16,050,000.00 USD | 20,470.00 USD | 7,370.00 USD | 112,470.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.71` | 90,780.00 USD | 3,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.71` | 15,900,000.00 USD | 15,900,000.00 USD | 51,960.00 USD | 0.00 USD | 74,330.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.71` | 12,740.00 USD | 3,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.72` | 15,780,000.00 USD | 15,780,000.00 USD | 425.03 USD | 0.00 USD | 183.06 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.73` | 355,230.00 USD | 3,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.73` | 15,780,000.00 USD | 15,780,000.00 USD | 41,940.00 USD | 10,880.00 USD | 56,790.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.73` | 123,790.00 USD | 2,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.74` | 15,670,000.00 USD | 15,670,000.00 USD | 130,620.00 USD | 40,020.00 USD | 122,480.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.75` | 24,210.00 USD | 2,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.75` | 15,380,000.00 USD | 15,380,000.00 USD | 3,890.00 USD | 51,780.00 USD | 129,350.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.75` | 150,270.00 USD | 2,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.76` | 15,190,000.00 USD | 15,190,000.00 USD | 32,650.00 USD | 10,110.00 USD | 22,610.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.77` | 65,190.00 USD | 2,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.77` | 15,120,000.00 USD | 15,120,000.00 USD | 15,340.00 USD | 8,090.00 USD | 23,020.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.77` | 123,660.00 USD | 2,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.78` | 15,080,000.00 USD | 15,080,000.00 USD | 24,180.00 USD | 93,830.00 USD | 41,570.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.79` | 48,560.00 USD | 2,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.79` | 14,920,000.00 USD | 14,920,000.00 USD | 51,640.00 USD | 0.00 USD | 137,710.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.79` | 34,520.00 USD | 2,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.80` | 14,730,000.00 USD | 14,730,000.00 USD | 8,210.00 USD | 34,570.00 USD | 17,840.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.81` | 585,450.00 USD | 2,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.81` | 14,670,000.00 USD | 14,670,000.00 USD | 5,310.00 USD | 0.00 USD | 1,430.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.81` | 10,980.00 USD | 1,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.82` | 14,660,000.00 USD | 14,660,000.00 USD | 5,630.00 USD | 18,370.00 USD | 25,600.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.83` | 181,850.00 USD | 1,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.83` | 14,610,000.00 USD | 14,610,000.00 USD | 50,540.00 USD | 50,500.00 USD | 153.98 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.83` | 171,380.00 USD | 1,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.84` | 17,600,000.00 USD | 17,600,000.00 USD | 275,920.00 USD | 171,520.00 USD | 179,530.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.84` | 14,510,000.00 USD | 14,510,000.00 USD | 7,940.00 USD | 33,350.00 USD | 146.37 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.85` | 119,620.00 USD | 1,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.85` | 16,970,000.00 USD | 16,970,000.00 USD | 186,230.00 USD | 175,470.00 USD | 37,740.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.85` | 14,470,000.00 USD | 14,470,000.00 USD | 3,390.00 USD | 49,170.00 USD | 84,260.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.85` | 22,330.00 USD | 1,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.86` | 16,570,000.00 USD | 16,570,000.00 USD | 39,130.00 USD | 39,050.00 USD | 52,990.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.86` | 14,330,000.00 USD | 14,330,000.00 USD | 5,190.00 USD | 173,980.00 USD | 39,790.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.87` | 71,550.00 USD | 1,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.87` | 16,440,000.00 USD | 16,440,000.00 USD | 53,480.00 USD | 58,230.00 USD | 188,360.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.87` | 14,110,000.00 USD | 14,110,000.00 USD | 62,650.00 USD | 0.00 USD | 197,600.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.88` | 8,130.00 USD | 950,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.88` | 16,140,000.00 USD | 16,140,000.00 USD | 35,520.00 USD | 26,560.00 USD | 224,940.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.88` | 13,850,000.00 USD | 13,850,000.00 USD | 110,160.00 USD | 86,900.00 USD | 156,790.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.88` | 173,140.00 USD | 942,610.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.89` | 15,860,000.00 USD | 15,860,000.00 USD | 396,980.00 USD | 100,370.00 USD | 258,260.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.89` | 13,500,000.00 USD | 13,500,000.00 USD | 4,240.00 USD | 50,710.00 USD | 83,380.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.90` | 93,930.00 USD | 769,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.90` | 15,100,000.00 USD | 15,100,000.00 USD | 33,360.00 USD | 49,080.00 USD | 223,320.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.90` | 13,360,000.00 USD | 13,360,000.00 USD | 274,050.00 USD | 28,250.00 USD | 51,510.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.90` | 7,990.00 USD | 675,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.91` | 14,790,000.00 USD | 14,790,000.00 USD | 351,900.00 USD | 120,100.00 USD | 276,080.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.91` | 13,010,000.00 USD | 13,010,000.00 USD | 122,540.00 USD | 67,260.00 USD | 46,930.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.92` | 37,030.00 USD | 667,540.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.92` | 14,050,000.00 USD | 14,050,000.00 USD | 318,260.00 USD | 13,670.00 USD | 124,180.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.92` | 12,770,000.00 USD | 12,770,000.00 USD | 85,790.00 USD | 66,710.00 USD | 105,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.92` | 2,050.00 USD | 630,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.93` | 13,590,000.00 USD | 13,590,000.00 USD | 116,350.00 USD | 99,220.00 USD | 97,360.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.93` | 12,510,000.00 USD | 12,510,000.00 USD | 0.00 USD | 28,720.00 USD | 67.04 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.94` | 17,100.00 USD | 628,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.94` | 13,280,000.00 USD | 13,280,000.00 USD | 144,900.00 USD | 53,060.00 USD | 137,210.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.94` | 12,480,000.00 USD | 12,480,000.00 USD | 55,330.00 USD | 0.00 USD | 2,250.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.94` | 149,880.00 USD | 611,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.95` | 12,940,000.00 USD | 12,940,000.00 USD | 116,010.00 USD | 0.00 USD | 33,080.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.95` | 12,430,000.00 USD | 12,430,000.00 USD | 8,490.00 USD | 0.00 USD | 2,800.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.96` | 56,160.00 USD | 461,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.96` | 12,790,000.00 USD | 12,790,000.00 USD | 67,260.00 USD | 22,830.00 USD | 17,320.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.96` | 12,420,000.00 USD | 12,420,000.00 USD | 165,060.00 USD | 0.00 USD | 325.84 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.96` | 1,240.00 USD | 405,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.97` | 12,680,000.00 USD | 12,680,000.00 USD | 2,650.00 USD | 36,470.00 USD | 137,700.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.97` | 12,250,000.00 USD | 12,250,000.00 USD | 235,890.00 USD | 0.00 USD | 2,980.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.98` | 82,400.00 USD | 404,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.98` | 12,510,000.00 USD | 12,510,000.00 USD | 20,780.00 USD | 76,990.00 USD | 94,490.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.98` | 12,010,000.00 USD | 12,010,000.00 USD | 506,280.00 USD | 0.00 USD | 279,750.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.98` | 5,650.00 USD | 321,680.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.99` | 12,320,000.00 USD | 12,320,000.00 USD | 34,010.00 USD | 64,350.00 USD | 106,350.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.99` | 11,230,000.00 USD | 11,230,000.00 USD | 298,270.00 USD | 26,340.00 USD | 78,590.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.00` | 160,840.00 USD | 316,030.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.00` | 12,110,000.00 USD | 12,110,000.00 USD | 40,030.00 USD | 17,140.00 USD | 137,750.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.00` | 10,820,000.00 USD | 10,820,000.00 USD | 307,590.00 USD | 68,590.00 USD | 574,560.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.00` | 11,990.00 USD | 155,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.01` | 11,920,000.00 USD | 11,920,000.00 USD | 2,740.00 USD | 158,450.00 USD | 222,850.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.01` | 9,870,000.00 USD | 9,870,000.00 USD | 371,710.00 USD | 57,440.00 USD | 439,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.01` | 275.83 USD | 143,200.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.02` | 11,530,000.00 USD | 11,530,000.00 USD | 135,580.00 USD | 52,150.00 USD | 125,360.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.02` | 9,000,000.00 USD | 9,000,000.00 USD | 271,690.00 USD | 156,620.00 USD | 251,320.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.03` | 1,910.00 USD | 142,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.03` | 11,220,000.00 USD | 11,220,000.00 USD | 65,620.00 USD | 59,350.00 USD | 324.38 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.03` | 8,320,000.00 USD | 8,320,000.00 USD | 247,960.00 USD | 0.00 USD | 344,930.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.04` | 25,700.00 USD | 141,020.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.04` | 11,090,000.00 USD | 11,090,000.00 USD | 69,810.00 USD | 21,940.00 USD | 183,420.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.04` | 7,730,000.00 USD | 7,730,000.00 USD | 321,230.00 USD | 0.00 USD | 492,290.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.04` | 32,100.00 USD | 115,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.05` | 10,820,000.00 USD | 10,820,000.00 USD | 348,930.00 USD | 23,720.00 USD | 232.83 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.05` | 6,920,000.00 USD | 6,920,000.00 USD | 2,180.00 USD | 41,020.00 USD | 68,490.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.05` | 4,380.00 USD | 83,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.06` | 10,450,000.00 USD | 10,450,000.00 USD | 35,870.00 USD | 83,800.00 USD | 450,950.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.06` | 6,810,000.00 USD | 6,810,000.00 USD | 0.00 USD | 72,410.00 USD | 523.71 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.07` | 1,200.00 USD | 78,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.07` | 9,880,000.00 USD | 9,880,000.00 USD | 358,380.00 USD | 205,460.00 USD | 334,510.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.07` | 6,730,000.00 USD | 6,730,000.00 USD | 0.00 USD | 287,180.00 USD | 166,640.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.08` | 10,210.00 USD | 77,640.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.08` | 8,980,000.00 USD | 8,980,000.00 USD | 69,080.00 USD | 277,630.00 USD | 133,890.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.08` | 6,280,000.00 USD | 6,280,000.00 USD | 0.00 USD | 237,170.00 USD | 135.50 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.08` | 5,330.00 USD | 67,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.09` | 8,500,000.00 USD | 8,500,000.00 USD | 246,920.00 USD | 60,230.00 USD | 168,490.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.09` | 6,040,000.00 USD | 6,040,000.00 USD | 253,510.00 USD | 179,350.00 USD | 433,540.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.09` | 17,640.00 USD | 62,110.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.10` | 8,020,000.00 USD | 8,020,000.00 USD | 4,000.00 USD | 89,650.00 USD | 141,410.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.10` | 5,180,000.00 USD | 5,180,000.00 USD | 27,630.00 USD | 0.00 USD | 240.24 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.11` | 15,640.00 USD | 44,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.11` | 7,790,000.00 USD | 7,790,000.00 USD | 120,600.00 USD | 138,540.00 USD | 345,580.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.11` | 5,150,000.00 USD | 5,150,000.00 USD | 0.00 USD | 25,170.00 USD | 295,730.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.12` | 17,630.00 USD | 28,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.12` | 7,180,000.00 USD | 7,180,000.00 USD | 48,010.00 USD | 34,010.00 USD | 274,300.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.12` | 4,830,000.00 USD | 4,830,000.00 USD | 2,900.00 USD | 181,330.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.12` | 11,200.00 USD | 11,200.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.13` | 6,820,000.00 USD | 6,820,000.00 USD | 159,720.00 USD | 0.00 USD | 398,490.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.13` | 4,640,000.00 USD | 4,640,000.00 USD | 154,140.00 USD | 0.00 USD | 237,800.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `4.14` | 6,270,000.00 USD | 6,270,000.00 USD | 139,890.00 USD | 29,960.00 USD | 125,370.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.14` | 4,250,000.00 USD | 4,250,000.00 USD | 238,150.00 USD | 244,270.00 USD | 345,750.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `4.15` | 5,970,000.00 USD | 5,970,000.00 USD | 526,070.00 USD | 102,010.00 USD | 367,560.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.15` | 3,420,000.00 USD | 3,420,000.00 USD | 326,430.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `4.16` | 4,980,000.00 USD | 4,980,000.00 USD | 297,170.00 USD | 59,420.00 USD | 316,310.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.17` | 8,230.00 USD | 8,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.17` | 4,300,000.00 USD | 4,300,000.00 USD | 250,510.00 USD | 283,430.00 USD | 238,930.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.17` | 3,100,000.00 USD | 3,100,000.00 USD | 252,690.00 USD | 84,340.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `4.18` | 3,530,000.00 USD | 3,530,000.00 USD | 329,080.00 USD | 62,340.00 USD | 201,720.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.18` | 2,760,000.00 USD | 2,760,000.00 USD | 0.00 USD | 0.00 USD | 86,570.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `4.19` | 2,940,000.00 USD | 2,940,000.00 USD | 148,260.00 USD | 138,280.00 USD | 244,930.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.19` | 2,670,000.00 USD | 2,670,000.00 USD | 2,760.00 USD | 50,340.00 USD | 393,520.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `4.20` | 2,400,000.00 USD | 2,400,000.00 USD | 31,500.00 USD | 40,570.00 USD | 131,830.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.20` | 2,230,000.00 USD | 2,230,000.00 USD | 227,690.00 USD | 86,790.00 USD | 371,630.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `4.21` | 2,200,000.00 USD | 2,200,000.00 USD | 487,450.00 USD | 98,820.00 USD | 217,230.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.21` | 1,540,000.00 USD | 1,540,000.00 USD | 308,290.00 USD | 0.00 USD | 146,990.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.21` | 1,770.00 USD | 10,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.22` | 1,400,000.00 USD | 1,400,000.00 USD | 83,280.00 USD | 59,930.00 USD | 56,420.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.22` | 1,080,000.00 USD | 1,080,000.00 USD | 119,070.00 USD | 142,820.00 USD | 417,550.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `4.23` | 1,200,000.00 USD | 1,200,000.00 USD | 113,770.00 USD | 114,760.00 USD | 274,130.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.23` | 404,910.00 USD | 404,910.00 USD | 182,720.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `4.24` | 695,280.00 USD | 695,280.00 USD | 40,490.00 USD | 15,710.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `4.25` | 639,070.00 USD | 639,070.00 USD | 70,910.00 USD | 0.00 USD | 186,310.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.25` | 222,190.00 USD | 222,190.00 USD | 3,390.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `4.26` | 381,860.00 USD | 381,860.00 USD | 0.00 USD | 0.00 USD | 85,610.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.26` | 218,800.00 USD | 218,800.00 USD | 2,960.00 USD | 0.00 USD | 173,150.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `4.27` | 296,250.00 USD | 296,250.00 USD | 0.00 USD | 44,870.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.27` | 42,690.00 USD | 42,690.00 USD | 24,810.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `4.28` | 251,390.00 USD | 251,390.00 USD | 4,310.00 USD | 28,780.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.28` | 17,880.00 USD | 17,880.00 USD | 5,380.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `4.29` | 218,290.00 USD | 218,290.00 USD | 217,970.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.29` | 12,490.00 USD | 12,490.00 USD | 5,150.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.29` | 1,080.00 USD | 11,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.32` | 326.33 USD | 326.33 USD | 0.00 USD | 0.00 USD | 326.33 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.34` | 7,340.00 USD | 7,340.00 USD | 0.00 USD | 0.00 USD | 7,340.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.35` | 157,030.00 USD | 157,030.00 USD | 157,030.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.35` | 314,060.00 USD | 314,060.00 USD | 157,030.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.35` | 252,690.00 USD | 252,690.00 USD | 252,690.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.35` | 505,380.00 USD | 505,380.00 USD | 252,690.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.36` | 3,050.00 USD | 14,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.36` | 694,220.00 USD | 694,220.00 USD | 100,970.00 USD | 0.00 USD | 279,180.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.37` | 1,370,000.00 USD | 1,370,000.00 USD | 280,420.00 USD | 0.00 USD | 400,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.37` | 949,240.00 USD | 949,240.00 USD | 0.00 USD | 50,340.00 USD | 393,520.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.38` | 83,560.00 USD | 97,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.38` | 2,020,000.00 USD | 2,020,000.00 USD | 3,030.00 USD | 0.00 USD | 640,700.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.38` | 1,440,000.00 USD | 1,440,000.00 USD | 0.00 USD | 228,720.00 USD | 261,380.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.39` | 2,920,000.00 USD | 2,920,000.00 USD | 356,920.00 USD | 41,380.00 USD | 505,620.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.39` | 2,520,000.00 USD | 2,520,000.00 USD | 560,900.00 USD | 149,280.00 USD | 369,470.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.39` | 180,760.00 USD | 278,450.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.40` | 3,990,000.00 USD | 3,990,000.00 USD | 541,780.00 USD | 118,310.00 USD | 408,330.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.40` | 3,680,000.00 USD | 3,680,000.00 USD | 111,810.00 USD | 169,770.00 USD | 881,540.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.41` | 5,450,000.00 USD | 5,450,000.00 USD | 450,080.00 USD | 317,280.00 USD | 689,400.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.41` | 4,210,000.00 USD | 4,210,000.00 USD | 184,170.00 USD | 65,600.00 USD | 278,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.42` | 507.73 USD | 278,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.42` | 5,770,000.00 USD | 5,770,000.00 USD | 41,570.00 USD | 157,960.00 USD | 127,800.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.42` | 4,860,000.00 USD | 4,860,000.00 USD | 404,280.00 USD | 71,590.00 USD | 175,990.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.42` | 1,930.00 USD | 280,890.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.43` | 6,340,000.00 USD | 6,340,000.00 USD | 155,560.00 USD | 109,630.00 USD | 300,550.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.43` | 5,320,000.00 USD | 5,320,000.00 USD | 293,250.00 USD | 88,400.00 USD | 71,780.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.43` | 4,430.00 USD | 285,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.44` | 7,320,000.00 USD | 7,320,000.00 USD | 156,430.00 USD | 370,280.00 USD | 457,750.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.44` | 5,710,000.00 USD | 5,710,000.00 USD | 0.00 USD | 143,990.00 USD | 246,120.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.45` | 358.27 USD | 285,680.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.45` | 7,680,000.00 USD | 7,680,000.00 USD | 76,860.00 USD | 153,510.00 USD | 124,130.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.45` | 5,930,000.00 USD | 5,930,000.00 USD | 0.00 USD | 25,170.00 USD | 196,900.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.46` | 38,840.00 USD | 324,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.46` | 7,780,000.00 USD | 7,780,000.00 USD | 4,580.00 USD | 65,940.00 USD | 33,060.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.46` | 6,040,000.00 USD | 6,040,000.00 USD | 3,070.00 USD | 105,500.00 USD | 2,350.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.46` | 1,370.00 USD | 325,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.47` | 8,150,000.00 USD | 8,150,000.00 USD | 222,670.00 USD | 25,190.00 USD | 120,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.47` | 6,610,000.00 USD | 6,610,000.00 USD | 358,290.00 USD | 135,940.00 USD | 75,550.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.47` | 17,400.00 USD | 343,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.48` | 8,670,000.00 USD | 8,670,000.00 USD | 246,890.00 USD | 116,490.00 USD | 150,910.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.48` | 6,890,000.00 USD | 6,890,000.00 USD | 1,870.00 USD | 71,410.00 USD | 210,580.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.49` | 2,030.00 USD | 345,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.49` | 9,610,000.00 USD | 9,610,000.00 USD | 310,660.00 USD | 235,310.00 USD | 403,450.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.49` | 7,320,000.00 USD | 7,320,000.00 USD | 335,730.00 USD | 93,790.00 USD | 162.91 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.50` | 22,680.00 USD | 368,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.50` | 10,250,000.00 USD | 10,250,000.00 USD | 383,900.00 USD | 77,440.00 USD | 175,170.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.50` | 7,900,000.00 USD | 7,900,000.00 USD | 376,770.00 USD | 200,700.00 USD | 2,050.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.50` | 1,530.00 USD | 369,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.51` | 11,040,000.00 USD | 11,040,000.00 USD | 224,110.00 USD | 149,810.00 USD | 418,530.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.51` | 7,980,000.00 USD | 7,980,000.00 USD | 77,780.00 USD | 0.00 USD | 2,140.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.51` | 13,270.00 USD | 382,800.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.52` | 11,710,000.00 USD | 11,710,000.00 USD | 291,580.00 USD | 92,260.00 USD | 286,020.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.52` | 8,210,000.00 USD | 8,210,000.00 USD | 2,080.00 USD | 0.00 USD | 225,430.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.53` | 819.48 USD | 383,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.53` | 12,520,000.00 USD | 12,520,000.00 USD | 505,320.00 USD | 22,430.00 USD | 280,200.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.53` | 9,190,000.00 USD | 9,190,000.00 USD | 439,420.00 USD | 232,800.00 USD | 310,070.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.54` | 965.96 USD | 384,590.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.54` | 12,870,000.00 USD | 12,870,000.00 USD | 16,950.00 USD | 164,990.00 USD | 167,990.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.54` | 10,430,000.00 USD | 10,430,000.00 USD | 2,730.00 USD | 0.00 USD | 1,240,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.54` | 24,260.00 USD | 408,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.55` | 13,020,000.00 USD | 13,020,000.00 USD | 1,620.00 USD | 34,450.00 USD | 108,590.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.55` | 10,430,000.00 USD | 10,430,000.00 USD | 0.00 USD | 0.00 USD | 237.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.55` | 120,920.00 USD | 529,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.56` | 13,450,000.00 USD | 13,450,000.00 USD | 112,410.00 USD | 32,800.00 USD | 288,580.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.56` | 10,920,000.00 USD | 10,920,000.00 USD | 364,250.00 USD | 124,220.00 USD | 219.44 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.57` | 182,600.00 USD | 712,370.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.57` | 13,800,000.00 USD | 13,800,000.00 USD | 176,460.00 USD | 70,180.00 USD | 99,620.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.57` | 11,460,000.00 USD | 11,460,000.00 USD | 305,830.00 USD | 27,650.00 USD | 209,740.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.58` | 14,950,000.00 USD | 14,950,000.00 USD | 423,030.00 USD | 99,430.00 USD | 634,060.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.58` | 11,590,000.00 USD | 11,590,000.00 USD | 44,380.00 USD | 0.00 USD | 86,090.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.58` | 2,140.00 USD | 714,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.59` | 15,560,000.00 USD | 15,560,000.00 USD | 420,560.00 USD | 75,460.00 USD | 109,360.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.59` | 13,300,000.00 USD | 13,300,000.00 USD | 760,880.00 USD | 68,070.00 USD | 881,740.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.60` | 15,720,000.00 USD | 15,720,000.00 USD | 48,970.00 USD | 50,860.00 USD | 66,480.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.60` | 13,420,000.00 USD | 13,420,000.00 USD | 3,460.00 USD | 112,080.00 USD | 2,580.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.61` | 15,870,000.00 USD | 15,870,000.00 USD | 65,250.00 USD | 7,560.00 USD | 76,320.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.61` | 13,430,000.00 USD | 13,430,000.00 USD | 5,400.00 USD | 0.00 USD | 1,140.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.62` | 16,020,000.00 USD | 16,020,000.00 USD | 94,450.00 USD | 31,380.00 USD | 19,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.62` | 13,570,000.00 USD | 13,570,000.00 USD | 134,680.00 USD | 0.00 USD | 2,890.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.62` | 51,690.00 USD | 766,200.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.63` | 16,020,000.00 USD | 16,020,000.00 USD | 2,310.00 USD | 0.00 USD | 422.42 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.63` | 13,780,000.00 USD | 13,780,000.00 USD | 215,660.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.63` | 990.04 USD | 767,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.64` | 16,180,000.00 USD | 16,180,000.00 USD | 106,430.00 USD | 11,270.00 USD | 41,640.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.64` | 14,320,000.00 USD | 14,320,000.00 USD | 503,610.00 USD | 34,570.00 USD | 1,960.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.64` | 8,450.00 USD | 775,640.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.65` | 16,920,000.00 USD | 16,920,000.00 USD | 203,560.00 USD | 52,020.00 USD | 486,530.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.65` | 14,750,000.00 USD | 14,750,000.00 USD | 420,940.00 USD | 0.00 USD | 2,070.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.66` | 150,680.00 USD | 926,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.66` | 17,710,000.00 USD | 17,710,000.00 USD | 202,480.00 USD | 309,340.00 USD | 277,010.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.66` | 15,060,000.00 USD | 15,060,000.00 USD | 144,860.00 USD | 18,370.00 USD | 150,940.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.67` | 101.70 USD | 926,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.67` | 18,060,000.00 USD | 18,060,000.00 USD | 88,400.00 USD | 0.00 USD | 259,350.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.67` | 15,100,000.00 USD | 15,100,000.00 USD | 0.00 USD | 0.00 USD | 43,230.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.67` | 54,290.00 USD | 980,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.68` | 18,260,000.00 USD | 18,260,000.00 USD | 60,330.00 USD | 106,120.00 USD | 37,010.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.68` | 16,020,000.00 USD | 16,020,000.00 USD | 381,910.00 USD | 83,630.00 USD | 450,770.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.68` | 1,030.00 USD | 981,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.69` | 18,650,000.00 USD | 18,650,000.00 USD | 168,690.00 USD | 49,160.00 USD | 168,810.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.69` | 16,180,000.00 USD | 16,180,000.00 USD | 52,990.00 USD | 16,870.00 USD | 88,340.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.70` | 230.06 USD | 981,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.70` | 18,990,000.00 USD | 18,990,000.00 USD | 69,690.00 USD | 97,490.00 USD | 175,270.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.70` | 16,490,000.00 USD | 16,490,000.00 USD | 74,240.00 USD | 60,360.00 USD | 181,350.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.71` | 7,480.00 USD | 989,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.71` | 20,040,000.00 USD | 20,040,000.00 USD | 390,710.00 USD | 298,900.00 USD | 353,490.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.71` | 16,980,000.00 USD | 16,980,000.00 USD | 178,360.00 USD | 232,800.00 USD | 78,760.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.72` | 20,270,000.00 USD | 20,270,000.00 USD | 2,370.00 USD | 181,280.00 USD | 49,950.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.72` | 17,190,000.00 USD | 17,190,000.00 USD | 7,140.00 USD | 17,360.00 USD | 180,490.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.72` | 2,590.00 USD | 992,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.73` | 20,440,000.00 USD | 20,440,000.00 USD | 110,530.00 USD | 25,210.00 USD | 35,540.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.73` | 17,260,000.00 USD | 17,260,000.00 USD | 59,970.00 USD | 15,660.00 USD | 1,040.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.74` | 3,380.00 USD | 995,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.74` | 20,830,000.00 USD | 20,830,000.00 USD | 68,200.00 USD | 141,320.00 USD | 176,260.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.74` | 17,650,000.00 USD | 17,650,000.00 USD | 14,750.00 USD | 191,030.00 USD | 182,880.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.75` | 111,130.00 USD | 1,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.75` | 21,240,000.00 USD | 21,240,000.00 USD | 100,050.00 USD | 141,340.00 USD | 171,270.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.75` | 18,200,000.00 USD | 18,200,000.00 USD | 17,340.00 USD | 185,060.00 USD | 343,810.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.76` | 21,350,000.00 USD | 21,350,000.00 USD | 32,430.00 USD | 51,460.00 USD | 31,810.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.76` | 19,550,000.00 USD | 19,550,000.00 USD | 1,030,000.00 USD | 46,890.00 USD | 272,680.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.76` | 5,980.00 USD | 1,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.77` | 21,510,000.00 USD | 21,510,000.00 USD | 19,050.00 USD | 85,030.00 USD | 47,800.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.77` | 20,450,000.00 USD | 20,450,000.00 USD | 732,640.00 USD | 73,410.00 USD | 101,640.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.78` | 1,730.00 USD | 1,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.78` | 21,650,000.00 USD | 21,650,000.00 USD | 37,290.00 USD | 20,000.00 USD | 87,070.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.78` | 21,580,000.00 USD | 21,580,000.00 USD | 499,950.00 USD | 477,230.00 USD | 154,510.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.79` | 143.55 USD | 1,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.79` | 21,830,000.00 USD | 21,830,000.00 USD | 74,330.00 USD | 44,330.00 USD | 59,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.79` | 22,620,000.00 USD | 22,620,000.00 USD | 713,060.00 USD | 249,310.00 USD | 72,220.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.79` | 1,330.00 USD | 1,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.80` | 22,300,000.00 USD | 22,300,000.00 USD | 209,090.00 USD | 128,280.00 USD | 138,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.80` | 24,210,000.00 USD | 24,210,000.00 USD | 1,160,000.00 USD | 432,340.00 USD | 2,480.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.81` | 22,320,000.00 USD | 22,320,000.00 USD | 0.00 USD | 13,110.00 USD | 210.83 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.81` | 24,840,000.00 USD | 24,840,000.00 USD | 400,800.00 USD | 125,900.00 USD | 101,780.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.82` | 22,460,000.00 USD | 22,460,000.00 USD | 20,630.00 USD | 81,720.00 USD | 35,520.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.82` | 27,610,000.00 USD | 27,610,000.00 USD | 1,010,000.00 USD | 369,430.00 USD | 1,390,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.83` | 2,360.00 USD | 1,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.83` | 22,480,000.00 USD | 22,480,000.00 USD | 15,330.00 USD | 5,610.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.83` | 29,250,000.00 USD | 29,250,000.00 USD | 822,860.00 USD | 85,680.00 USD | 739,630.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.83` | 1,540.00 USD | 1,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.84` | 22,620,000.00 USD | 22,620,000.00 USD | 34,640.00 USD | 76,320.00 USD | 34,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.84` | 29,750,000.00 USD | 29,750,000.00 USD | 97,300.00 USD | 71,790.00 USD | 322,840.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.84` | 11,220.00 USD | 1,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `4.85` | 31,780,000.00 USD | 31,780,000.00 USD | 487,940.00 USD | 380,760.00 USD | 1,160,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.86` | 33,190,000.00 USD | 33,190,000.00 USD | 444,810.00 USD | 162,380.00 USD | 802,380.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.87` | 259.79 USD | 1,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `4.87` | 34,250,000.00 USD | 34,250,000.00 USD | 264,730.00 USD | 136,820.00 USD | 663,430.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.88` | 35,740,000.00 USD | 35,740,000.00 USD | 428,040.00 USD | 266,980.00 USD | 789,710.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.88` | 827.03 USD | 1,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4.91` | 674.44 USD | 1,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4.92` | 20,720.00 USD | 1,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4.92` | 2,100.00 USD | 1,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4.93` | 157.43 USD | 1,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4.95` | 2,060.00 USD | 1,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4.96` | 488.56 USD | 1,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `4.97` | 99,370.00 USD | 1,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.01` | 36,420.00 USD | 1,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.04` | 118.83 USD | 1,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.05` | 35,380.00 USD | 1,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.07` | 3,420.00 USD | 1,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.11` | 177.14 USD | 1,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.12` | 5,710.00 USD | 1,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.12` | 51,250.00 USD | 1,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.17` | 3,330.00 USD | 1,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.20` | 11,250.00 USD | 1,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.22` | 73,780.00 USD | 1,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.25` | 143.71 USD | 1,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.25` | 17,380.00 USD | 1,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.26` | 21,280.00 USD | 1,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.28` | 608.21 USD | 1,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.29` | 1,060,000.00 USD | 2,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.29` | 41,410.00 USD | 2,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.30` | 524.66 USD | 2,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.32` | 147.23 USD | 2,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.33` | 286.49 USD | 2,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.34` | 338,680.00 USD | 2,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.36` | 5,940.00 USD | 2,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.38` | 182.21 USD | 2,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.42` | 1,030.00 USD | 2,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.42` | 914.65 USD | 2,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.43` | 419.04 USD | 2,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.47` | 7,840.00 USD | 2,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.49` | 12,740.00 USD | 2,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.50` | 66,470.00 USD | 3,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.50` | 62,990.00 USD | 3,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.51` | 38,800.00 USD | 3,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.53` | 1,270.00 USD | 3,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.54` | 209.22 USD | 3,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.57` | 9,360.00 USD | 3,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.58` | 62,420.00 USD | 3,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.62` | 3,980,000.00 USD | 7,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.66` | 1,630,000.00 USD | 8,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.67` | 211.30 USD | 8,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.67` | 228.70 USD | 8,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.68` | 26,090.00 USD | 8,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.70` | 1,520.00 USD | 8,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.71` | 2,130.00 USD | 8,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.75` | 4,580.00 USD | 8,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.75` | 3,020.00 USD | 8,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.76` | 475,940.00 USD | 9,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.83` | 198.97 USD | 9,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.84` | 270,530.00 USD | 9,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.86` | 848.39 USD | 9,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.88` | 7,150.00 USD | 9,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.89` | 88,420.00 USD | 9,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.91` | 162.98 USD | 9,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.92` | 189.28 USD | 9,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.92` | 130.35 USD | 9,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.95` | 103,650.00 USD | 9,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.03` | 23,060.00 USD | 9,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.05` | 23,520.00 USD | 9,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.07` | 740.54 USD | 9,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.08` | 5,920.00 USD | 9,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.09` | 37,510.00 USD | 9,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.12` | 1,870.00 USD | 9,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.13` | 2,430.00 USD | 9,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.18` | 35,350.00 USD | 9,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.21` | 332,230.00 USD | 10,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.24` | 526,230.00 USD | 10,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.25` | 7,300.00 USD | 10,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.25` | 439.10 USD | 10,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.26` | 256,050.00 USD | 11,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.30` | 2,020.00 USD | 11,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.32` | 8,430.00 USD | 11,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.33` | 382.00 USD | 11,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.34` | 214.46 USD | 11,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.37` | 113.93 USD | 11,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.38` | 288.15 USD | 11,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.39` | 2,000.00 USD | 11,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.41` | 15,590.00 USD | 11,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.42` | 943.65 USD | 11,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.42` | 5,650.00 USD | 11,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.45` | 5,270.00 USD | 11,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.46` | 7,150.00 USD | 11,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.46` | 1,940.00 USD | 11,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.51` | 380.48 USD | 11,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.54` | 1,240,000.00 USD | 12,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.57` | 29,590,000.00 USD | 41,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.59` | 418.78 USD | 41,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.61` | 382,680.00 USD | 42,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.64` | 41,250.00 USD | 42,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.66` | 7,230.00 USD | 42,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.67` | 233.94 USD | 42,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.67` | 200.25 USD | 42,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.71` | 37,260.00 USD | 42,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.72` | 713.52 USD | 42,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.75` | 1,250,000.00 USD | 43,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.80` | 5,260.00 USD | 43,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.82` | 344.16 USD | 43,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.83` | 91,230.00 USD | 43,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.84` | 753.63 USD | 43,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.87` | 2,650.00 USD | 43,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.92` | 6,920.00 USD | 43,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.96` | 24,540.00 USD | 43,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.99` | 664.27 USD | 43,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.03` | 665.27 USD | 43,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.08` | 996.15 USD | 43,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.09` | 699.57 USD | 43,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.14` | 15,990.00 USD | 43,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.21` | 13,560.00 USD | 43,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.24` | 3,840,000.00 USD | 47,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.25` | 3,770.00 USD | 47,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.25` | 575.32 USD | 47,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.30` | 3,520.00 USD | 47,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.32` | 54,860.00 USD | 47,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.33` | 1,320.00 USD | 47,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.34` | 59,770.00 USD | 47,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.38` | 12,910.00 USD | 47,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.41` | 776.04 USD | 47,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.43` | 106,150.00 USD | 47,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.46` | 1,420.00 USD | 47,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.46` | 9,970,000.00 USD | 57,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.53` | 7,820,000.00 USD | 65,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.54` | 3,100.00 USD | 65,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.62` | 35,860.00 USD | 65,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.63` | 19,210.00 USD | 65,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.64` | 23,890.00 USD | 65,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.66` | 20,000.00 USD | 65,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.67` | 27,160.00 USD | 65,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.72` | 259.56 USD | 65,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.74` | 4,970.00 USD | 65,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.75` | 629.67 USD | 65,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.76` | 11,760.00 USD | 65,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.82` | 1,690.00 USD | 65,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.86` | 120.18 USD | 65,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.87` | 2,980.00 USD | 65,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.95` | 6,120.00 USD | 65,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.96` | 166.26 USD | 65,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.96` | 95,580.00 USD | 65,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.99` | 399.25 USD | 65,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.03` | 435,420.00 USD | 66,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.04` | 259.05 USD | 66,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.07` | 6,460.00 USD | 66,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.20` | 951.44 USD | 66,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.24` | 62,980.00 USD | 66,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.31` | 8,640.00 USD | 66,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.35` | 25,310.00 USD | 66,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.37` | 1,100,000.00 USD | 67,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.38` | 191.79 USD | 67,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.41` | 1,220.00 USD | 67,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.46` | 53,330.00 USD | 67,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.47` | 816.99 USD | 67,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.48` | 6,640.00 USD | 67,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.49` | 25,490.00 USD | 67,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.53` | 34,680.00 USD | 67,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.54` | 127.17 USD | 67,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.54` | 124.76 USD | 67,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.55` | 430,710.00 USD | 68,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.59` | 240.38 USD | 68,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.60` | 17,660.00 USD | 68,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `0.8850` | 22,540,000.00 USD | 0.00 USD | 411.70 USD | `-79.62%` | `465.20` |
| `Live` | `Long` | `0.8950` | 22,540,000.00 USD | 0.00 USD | 38,570.00 USD | `-79.39%` | `43,089.80` |
| `Live` | `Long` | `0.9050` | 22,500,000.00 USD | 0.00 USD | 292.22 USD | `-79.15%` | `322.90` |
| `Live` | `Long` | `0.9150` | 22,500,000.00 USD | 0.00 USD | 11,370.00 USD | `-78.92%` | `12,425.00` |
| `Live` | `Long` | `0.9350` | 22,490,000.00 USD | 0.00 USD | 2,810.00 USD | `-78.46%` | `3,001.60` |
| `Live` | `Long` | `0.9450` | 22,490,000.00 USD | 0.00 USD | 6,620.00 USD | `-78.23%` | `7,000.00` |
| `Live` | `Long` | `0.9550` | 22,480,000.00 USD | 0.00 USD | 1,450.00 USD | `-78.00%` | `1,521.50` |
| `Live` | `Long` | `0.9650` | 22,480,000.00 USD | 0.00 USD | 965.00 USD | `-77.77%` | `1,000.00` |
| `Live` | `Long` | `0.9850` | 22,480,000.00 USD | 0.00 USD | 3,690.00 USD | `-77.31%` | `3,749.70` |
| `Live` | `Long` | `0.9950` | 22,470,000.00 USD | 0.00 USD | 154,200.00 USD | `-77.08%` | `154,969.90` |
| `Live` | `Long` | `1.00` | 22,320,000.00 USD | 0.00 USD | 2,560.00 USD | `-76.85%` | `2,543.70` |
| `Live` | `Long` | `1.02` | 22,320,000.00 USD | 0.00 USD | 10,250.00 USD | `-76.39%` | `10,000.00` |
| `Live` | `Long` | `1.03` | 22,310,000.00 USD | 0.00 USD | 5,070.00 USD | `-76.16%` | `4,897.40` |
| `Live` | `Long` | `1.04` | 22,300,000.00 USD | 0.00 USD | 34,960.00 USD | `-75.93%` | `33,454.20` |
| `Live` | `Long` | `1.05` | 22,270,000.00 USD | 0.00 USD | 4,330.00 USD | `-75.70%` | `4,108.90` |
| `Live` | `Long` | `1.06` | 22,260,000.00 USD | 0.00 USD | 892.90 USD | `-75.47%` | `838.40` |
| `Live` | `Long` | `1.07` | 22,260,000.00 USD | 0.00 USD | 5,740.00 USD | `-75.24%` | `5,342.20` |
| `Live` | `Long` | `1.08` | 22,260,000.00 USD | 0.00 USD | 216.89 USD | `-75.01%` | `199.90` |
| `Live` | `Long` | `1.10` | 22,260,000.00 USD | 0.00 USD | 18,980.00 USD | `-74.55%` | `17,179.40` |
| `Live` | `Long` | `1.11` | 22,240,000.00 USD | 0.00 USD | 1,690.00 USD | `-74.32%` | `1,513.70` |
| `Live` | `Long` | `1.12` | 22,240,000.00 USD | 0.00 USD | 6,930.00 USD | `-74.09%` | `6,158.40` |
| `Live` | `Long` | `1.14` | 22,230,000.00 USD | 0.00 USD | 4,960.00 USD | `-73.86%` | `4,368.60` |
| `Live` | `Long` | `1.15` | 22,220,000.00 USD | 0.00 USD | 26,620.00 USD | `-73.63%` | `23,252.70` |
| `Live` | `Long` | `1.16` | 22,200,000.00 USD | 0.00 USD | 1,730.00 USD | `-73.40%` | `1,500.00` |
| `Live` | `Long` | `1.17` | 22,200,000.00 USD | 0.00 USD | 2,390.00 USD | `-73.17%` | `2,054.80` |
| `Live` | `Long` | `1.18` | 22,190,000.00 USD | 0.00 USD | 9,630.00 USD | `-72.94%` | `8,196.50` |
| `Live` | `Long` | `1.21` | 22,180,000.00 USD | 0.00 USD | 4,940.00 USD | `-72.24%` | `4,103.20` |
| `Live` | `Long` | `1.22` | 22,180,000.00 USD | 0.00 USD | 150.90 USD | `-72.01%` | `124.20` |
| `Live` | `Long` | `1.23` | 22,180,000.00 USD | 0.00 USD | 1,040.00 USD | `-71.78%` | `847.00` |
| `Live` | `Long` | `1.25` | 22,180,000.00 USD | 0.00 USD | 20,460.00 USD | `-71.32%` | `16,436.80` |
| `Live` | `Long` | `1.25` | 22,160,000.00 USD | 0.00 USD | 15,020.00 USD | `-71.09%` | `11,969.60` |
| `Live` | `Long` | `1.26` | 22,140,000.00 USD | 0.00 USD | 2,060.00 USD | `-70.86%` | `1,630.60` |
| `Live` | `Long` | `1.27` | 22,140,000.00 USD | 0.00 USD | 3,370.00 USD | `-70.63%` | `2,646.90` |
| `Live` | `Long` | `1.28` | 22,140,000.00 USD | 0.00 USD | 425.59 USD | `-70.40%` | `331.20` |
| `Live` | `Long` | `1.30` | 22,140,000.00 USD | 0.00 USD | 379.76 USD | `-69.94%` | `291.00` |
| `Live` | `Long` | `1.32` | 22,140,000.00 USD | 0.00 USD | 28,340.00 USD | `-69.48%` | `21,389.30` |
| `Live` | `Long` | `1.33` | 22,110,000.00 USD | 0.00 USD | 179.96 USD | `-69.25%` | `134.80` |
| `Live` | `Long` | `1.34` | 22,110,000.00 USD | 0.00 USD | 603.91 USD | `-69.02%` | `449.00` |
| `Live` | `Long` | `1.35` | 22,110,000.00 USD | 0.00 USD | 2,130.00 USD | `-68.79%` | `1,572.30` |
| `Live` | `Long` | `1.36` | 22,100,000.00 USD | 0.00 USD | 2,200.00 USD | `-68.56%` | `1,615.10` |
| `Live` | `Long` | `1.39` | 22,100,000.00 USD | 0.00 USD | 12,760.00 USD | `-68.10%` | `9,213.40` |
| `Live` | `Long` | `1.40` | 22,090,000.00 USD | 0.00 USD | 931.86 USD | `-67.87%` | `668.00` |
| `Live` | `Long` | `1.41` | 22,090,000.00 USD | 0.00 USD | 77,850.00 USD | `-67.64%` | `55,412.50` |
| `Live` | `Long` | `1.42` | 22,010,000.00 USD | 0.00 USD | 4,710.00 USD | `-67.41%` | `3,325.90` |
| `Live` | `Long` | `1.43` | 22,010,000.00 USD | 0.00 USD | 1,130.00 USD | `-67.18%` | `793.40` |
| `Live` | `Long` | `1.45` | 22,010,000.00 USD | 0.00 USD | 2,690.00 USD | `-66.72%` | `1,861.70` |
| `Live` | `Long` | `1.46` | 22,000,000.00 USD | 0.00 USD | 5,440.00 USD | `-66.49%` | `3,738.20` |
| `Live` | `Long` | `1.47` | 22,000,000.00 USD | 0.00 USD | 13,180.00 USD | `-66.26%` | `9,000.00` |
| `Live` | `Long` | `1.48` | 21,980,000.00 USD | 0.00 USD | 1,480.00 USD | `-66.03%` | `1,000.00` |
| `Live` | `Long` | `1.49` | 21,980,000.00 USD | 0.00 USD | 74,750.00 USD | `-65.80%` | `50,337.90` |
| `Live` | `Long` | `1.50` | 21,910,000.00 USD | 0.00 USD | 4,920.00 USD | `-65.56%` | `3,291.10` |
| `Live` | `Long` | `1.50` | 21,900,000.00 USD | 0.00 USD | 2,640.00 USD | `-65.33%` | `1,756.00` |
| `Live` | `Long` | `1.51` | 21,900,000.00 USD | 0.00 USD | 454.50 USD | `-65.10%` | `300.00` |
| `Live` | `Long` | `1.53` | 21,900,000.00 USD | 0.00 USD | 6,190.00 USD | `-64.64%` | `4,030.50` |
| `Live` | `Long` | `1.56` | 21,890,000.00 USD | 0.00 USD | 20,570.00 USD | `-63.95%` | `13,146.30` |
| `Live` | `Long` | `1.57` | 21,870,000.00 USD | 0.00 USD | 2,630.00 USD | `-63.72%` | `1,669.90` |
| `Live` | `Long` | `1.58` | 21,870,000.00 USD | 0.00 USD | 1,980.00 USD | `-63.49%` | `1,246.60` |
| `Live` | `Long` | `1.59` | 21,870,000.00 USD | 0.00 USD | 3,380.00 USD | `-63.26%` | `2,119.70` |
| `Live` | `Long` | `1.60` | 21,860,000.00 USD | 0.00 USD | 753.39 USD | `-63.03%` | `469.40` |
| `Live` | `Long` | `1.64` | 21,860,000.00 USD | 0.00 USD | 3,760.00 USD | `-62.34%` | `2,300.50` |
| `Live` | `Long` | `1.65` | 21,860,000.00 USD | 0.00 USD | 981.08 USD | `-62.11%` | `596.40` |
| `Live` | `Long` | `1.66` | 21,860,000.00 USD | 0.00 USD | 3,420.00 USD | `-61.88%` | `2,068.70` |
| `Live` | `Long` | `1.67` | 21,860,000.00 USD | 0.00 USD | 617.72 USD | `-61.65%` | `371.00` |
| `Live` | `Long` | `1.68` | 21,860,000.00 USD | 0.00 USD | 9,620.00 USD | `-61.42%` | `5,742.30` |
| `Live` | `Long` | `1.69` | 21,850,000.00 USD | 0.00 USD | 603,680.00 USD | `-61.19%` | `358,268.30` |
| `Live` | `Long` | `1.71` | 21,240,000.00 USD | 0.00 USD | 929.23 USD | `-60.73%` | `545.00` |
| `Live` | `Long` | `1.72` | 21,240,000.00 USD | 0.00 USD | 5,000.00 USD | `-60.50%` | `2,912.70` |
| `Live` | `Long` | `1.73` | 21,240,000.00 USD | 0.00 USD | 8,910.00 USD | `-60.27%` | `5,164.50` |
| `Live` | `Long` | `1.74` | 21,230,000.00 USD | 0.00 USD | 105.14 USD | `-60.04%` | `60.60` |
| `Live` | `Long` | `1.75` | 21,230,000.00 USD | 0.00 USD | 10,250.00 USD | `-59.58%` | `5,841.90` |
| `Live` | `Long` | `1.77` | 21,220,000.00 USD | 0.00 USD | 17,220.00 USD | `-59.12%` | `9,703.40` |
| `Live` | `Long` | `1.78` | 21,200,000.00 USD | 0.00 USD | 2,230.00 USD | `-58.89%` | `1,250.00` |
| `Live` | `Long` | `1.79` | 21,200,000.00 USD | 0.00 USD | 91,410.00 USD | `-58.65%` | `50,924.10` |
| `Live` | `Long` | `1.80` | 21,110,000.00 USD | 0.00 USD | 529.05 USD | `-58.42%` | `293.10` |
| `Live` | `Long` | `1.81` | 21,110,000.00 USD | 0.00 USD | 1,580.00 USD | `-58.19%` | `873.20` |
| `Live` | `Long` | `1.83` | 21,100,000.00 USD | 0.00 USD | 27,520.00 USD | `-57.73%` | `15,000.00` |
| `Live` | `Long` | `1.84` | 21,080,000.00 USD | 0.00 USD | 1,840.00 USD | `-57.50%` | `995.20` |
| `Live` | `Long` | `1.85` | 21,070,000.00 USD | 0.00 USD | 1,400.00 USD | `-57.27%` | `755.00` |
| `Live` | `Long` | `1.88` | 21,070,000.00 USD | 0.00 USD | 14,720.00 USD | `-56.81%` | `7,852.10` |
| `Live` | `Long` | `1.90` | 21,060,000.00 USD | 0.00 USD | 2,750.00 USD | `-56.35%` | `1,450.00` |
| `Live` | `Long` | `1.91` | 21,060,000.00 USD | 0.00 USD | 39,130.00 USD | `-56.12%` | `20,538.40` |
| `Live` | `Long` | `1.93` | 21,020,000.00 USD | 0.00 USD | 1,120.00 USD | `-55.66%` | `579.70` |
| `Live` | `Long` | `1.95` | 21,020,000.00 USD | 0.00 USD | 2,740.00 USD | `-55.20%` | `1,410.10` |
| `Live` | `Long` | `1.96` | 21,010,000.00 USD | 0.00 USD | 775.55 USD | `-54.97%` | `396.70` |
| `Live` | `Long` | `1.97` | 21,010,000.00 USD | 0.00 USD | 2,280.00 USD | `-54.74%` | `1,160.90` |
| `Live` | `Long` | `1.98` | 21,010,000.00 USD | 0.00 USD | 37,250.00 USD | `-54.51%` | `18,860.60` |
| `Live` | `Long` | `2.00` | 20,970,000.00 USD | 0.00 USD | 856,120.00 USD | `-53.82%` | `426,991.00` |
| `Live` | `Long` | `2.02` | 20,120,000.00 USD | 0.00 USD | 12,900.00 USD | `-53.59%` | `6,399.80` |
| `Live` | `Long` | `2.02` | 20,100,000.00 USD | 0.00 USD | 398.72 USD | `-53.36%` | `196.90` |
| `Live` | `Long` | `2.04` | 20,100,000.00 USD | 0.00 USD | 323.36 USD | `-53.13%` | `158.90` |
| `Live` | `Long` | `2.04` | 20,100,000.00 USD | 0.00 USD | 3,640.00 USD | `-52.90%` | `1,778.40` |
| `Live` | `Long` | `2.06` | 20,100,000.00 USD | 0.00 USD | 39,180.00 USD | `-52.67%` | `19,063.40` |
| `Live` | `Long` | `2.06` | 20,060,000.00 USD | 0.00 USD | 8,860.00 USD | `-52.44%` | `4,292.80` |
| `Live` | `Long` | `2.08` | 20,050,000.00 USD | 0.00 USD | 13,270.00 USD | `-52.21%` | `6,393.50` |
| `Live` | `Long` | `2.08` | 20,040,000.00 USD | 0.00 USD | 18,600.00 USD | `-51.98%` | `8,920.10` |
| `Live` | `Long` | `2.10` | 20,020,000.00 USD | 0.00 USD | 1,100.00 USD | `-51.74%` | `527.40` |
| `Live` | `Long` | `2.10` | 20,020,000.00 USD | 0.00 USD | 10,540.00 USD | `-51.51%` | `5,006.20` |
| `Live` | `Long` | `2.12` | 20,010,000.00 USD | 0.00 USD | 11,510.00 USD | `-51.28%` | `5,442.30` |
| `Live` | `Long` | `2.12` | 20,000,000.00 USD | 0.00 USD | 18,310.00 USD | `-51.05%` | `8,615.20` |
| `Live` | `Long` | `2.13` | 19,980,000.00 USD | 0.00 USD | 2,140.00 USD | `-50.82%` | `1,000.80` |
| `Live` | `Long` | `2.15` | 19,980,000.00 USD | 0.00 USD | 2,110.00 USD | `-50.59%` | `983.60` |
| `Live` | `Long` | `2.15` | 19,970,000.00 USD | 0.00 USD | 2,530.00 USD | `-50.36%` | `1,175.20` |
| `Live` | `Long` | `2.17` | 19,970,000.00 USD | 0.00 USD | 188,810.00 USD | `-50.13%` | `87,210.30` |
| `Live` | `Long` | `2.17` | 19,780,000.00 USD | 0.00 USD | 93,620.00 USD | `-49.90%` | `43,045.60` |
| `Live` | `Long` | `2.19` | 19,690,000.00 USD | 0.00 USD | 3,530.00 USD | `-49.67%` | `1,614.40` |
| `Live` | `Long` | `2.19` | 19,680,000.00 USD | 0.00 USD | 12,830.00 USD | `-49.44%` | `5,843.40` |
| `Live` | `Long` | `2.21` | 19,670,000.00 USD | 0.00 USD | 19,420.00 USD | `-49.21%` | `8,807.10` |
| `Live` | `Long` | `2.21` | 19,650,000.00 USD | 0.00 USD | 25,570.00 USD | `-48.98%` | `11,546.10` |
| `Live` | `Long` | `2.23` | 19,630,000.00 USD | 0.00 USD | 8,450.00 USD | `-48.75%` | `3,795.90` |
| `Live` | `Long` | `2.23` | 19,620,000.00 USD | 0.00 USD | 21,160.00 USD | `-48.52%` | `9,467.70` |
| `Live` | `Long` | `2.25` | 19,600,000.00 USD | 0.00 USD | 3,020.00 USD | `-48.29%` | `1,344.30` |
| `Live` | `Long` | `2.25` | 19,590,000.00 USD | 0.00 USD | 117,220.00 USD | `-48.06%` | `51,980.50` |
| `Live` | `Long` | `2.27` | 19,480,000.00 USD | 0.00 USD | 2,040.00 USD | `-47.83%` | `900.00` |
| `Live` | `Long` | `2.27` | 19,480,000.00 USD | 0.00 USD | 72,840.00 USD | `-47.60%` | `32,019.10` |
| `Live` | `Long` | `2.29` | 19,400,000.00 USD | 0.00 USD | 5,120.00 USD | `-47.37%` | `2,241.40` |
| `Live` | `Long` | `2.29` | 19,400,000.00 USD | 0.00 USD | 221,220.00 USD | `-47.14%` | `96,393.30` |
| `Live` | `Long` | `2.31` | 19,180,000.00 USD | 0.00 USD | 12,250.00 USD | `-46.91%` | `5,316.10` |
| `Live` | `Long` | `2.31` | 19,160,000.00 USD | 0.00 USD | 2,330.00 USD | `-46.68%` | `1,005.00` |
| `Live` | `Long` | `2.33` | 19,160,000.00 USD | 0.00 USD | 13,770.00 USD | `-46.45%` | `5,923.50` |
| `Live` | `Long` | `2.33` | 19,150,000.00 USD | 0.00 USD | 2,670.00 USD | `-46.22%` | `1,145.40` |
| `Live` | `Long` | `2.35` | 19,140,000.00 USD | 0.00 USD | 5,100.00 USD | `-45.99%` | `2,175.10` |
| `Live` | `Long` | `2.35` | 19,140,000.00 USD | 0.00 USD | 26,590.00 USD | `-45.76%` | `11,292.40` |
| `Live` | `Long` | `2.37` | 19,110,000.00 USD | 0.00 USD | 1,580.00 USD | `-45.53%` | `667.80` |
| `Live` | `Long` | `2.38` | 19,110,000.00 USD | 0.00 USD | 35,720.00 USD | `-45.30%` | `15,041.30` |
| `Live` | `Long` | `2.38` | 19,080,000.00 USD | 0.00 USD | 7,680.00 USD | `-45.07%` | `3,218.80` |
| `Live` | `Long` | `2.40` | 19,070,000.00 USD | 0.00 USD | 115.20 USD | `-44.83%` | `48.10` |
| `Live` | `Long` | `2.42` | 19,070,000.00 USD | 0.00 USD | 183,000.00 USD | `-44.37%` | `75,774.50` |
| `Live` | `Long` | `2.42` | 18,890,000.00 USD | 0.00 USD | 1,870,000.00 USD | `-44.14%` | `769,602.00` |
| `Live` | `Long` | `2.44` | 17,020,000.00 USD | 0.00 USD | 2,320.00 USD | `-43.91%` | `953.50` |
| `Live` | `Long` | `2.44` | 17,020,000.00 USD | 0.00 USD | 160,000.00 USD | `-43.68%` | `65,440.70` |
| `Live` | `Long` | `2.46` | 16,860,000.00 USD | 0.00 USD | 281,230.00 USD | `-43.45%` | `114,554.40` |
| `Live` | `Long` | `2.46` | 16,580,000.00 USD | 0.00 USD | 4,590.00 USD | `-43.22%` | `1,862.10` |
| `Live` | `Long` | `2.48` | 16,570,000.00 USD | 0.00 USD | 12,520.00 USD | `-42.99%` | `5,058.20` |
| `Live` | `Long` | `2.48` | 16,560,000.00 USD | 0.00 USD | 9,240.00 USD | `-42.76%` | `3,719.70` |
| `Live` | `Long` | `2.50` | 16,550,000.00 USD | 0.00 USD | 15,850.00 USD | `-42.53%` | `6,351.10` |
| `Live` | `Long` | `2.50` | 16,530,000.00 USD | 0.00 USD | 425,370.00 USD | `-42.30%` | `169,806.80` |
| `Live` | `Long` | `2.52` | 16,110,000.00 USD | 0.00 USD | 346.32 USD | `-42.07%` | `137.70` |
| `Live` | `Long` | `2.52` | 16,110,000.00 USD | 0.00 USD | 33,330.00 USD | `-41.84%` | `13,198.20` |
| `Live` | `Long` | `2.54` | 16,070,000.00 USD | 0.00 USD | 395.71 USD | `-41.61%` | `156.10` |
| `Live` | `Long` | `2.54` | 16,070,000.00 USD | 0.00 USD | 2,440.00 USD | `-41.38%` | `959.90` |
| `Live` | `Long` | `2.56` | 16,070,000.00 USD | 0.00 USD | 670.94 USD | `-41.15%` | `262.60` |
| `Live` | `Long` | `2.56` | 16,070,000.00 USD | 0.00 USD | 7,890.00 USD | `-40.92%` | `3,077.60` |
| `Live` | `Long` | `2.58` | 16,060,000.00 USD | 0.00 USD | 2,050.00 USD | `-40.69%` | `796.50` |
| `Live` | `Long` | `2.58` | 16,060,000.00 USD | 0.00 USD | 1,910.00 USD | `-40.46%` | `739.30` |
| `Live` | `Long` | `2.60` | 16,060,000.00 USD | 0.00 USD | 80,250.00 USD | `-40.23%` | `30,925.80` |
| `Live` | `Long` | `2.60` | 15,980,000.00 USD | 0.00 USD | 2,450.00 USD | `-40.00%` | `940.80` |
| `Live` | `Long` | `2.62` | 15,980,000.00 USD | 0.00 USD | 1,190.00 USD | `-39.77%` | `454.70` |
| `Live` | `Long` | `2.63` | 15,970,000.00 USD | 0.00 USD | 24,310.00 USD | `-39.31%` | `9,225.00` |
| `Live` | `Long` | `2.65` | 15,950,000.00 USD | 0.00 USD | 2,950.00 USD | `-39.08%` | `1,115.50` |
| `Live` | `Long` | `2.65` | 15,950,000.00 USD | 0.00 USD | 27,700.00 USD | `-38.85%` | `10,434.90` |
| `Live` | `Long` | `2.67` | 15,920,000.00 USD | 0.00 USD | 169,690.00 USD | `-38.62%` | `63,673.50` |
| `Live` | `Long` | `2.67` | 15,750,000.00 USD | 0.00 USD | 4,600.00 USD | `-38.39%` | `1,719.40` |
| `Live` | `Long` | `2.69` | 15,750,000.00 USD | 0.00 USD | 7,260.00 USD | `-38.16%` | `2,702.60` |
| `Live` | `Long` | `2.69` | 15,740,000.00 USD | 0.00 USD | 13,910.00 USD | `-37.92%` | `5,161.50` |
| `Live` | `Long` | `2.71` | 15,720,000.00 USD | 0.00 USD | 164,840.00 USD | `-37.69%` | `60,938.90` |
| `Live` | `Long` | `2.71` | 15,560,000.00 USD | 0.00 USD | 11,880.00 USD | `-37.46%` | `4,377.20` |
| `Live` | `Long` | `2.73` | 15,550,000.00 USD | 0.00 USD | 28,380.00 USD | `-37.23%` | `10,414.30` |
| `Live` | `Long` | `2.73` | 15,520,000.00 USD | 0.00 USD | 1,960.00 USD | `-37.00%` | `715.80` |
| `Live` | `Long` | `2.75` | 15,520,000.00 USD | 0.00 USD | 458.96 USD | `-36.77%` | `167.20` |
| `Live` | `Long` | `2.75` | 15,520,000.00 USD | 0.00 USD | 64,490.00 USD | `-36.54%` | `23,408.80` |
| `Live` | `Long` | `2.77` | 15,450,000.00 USD | 0.00 USD | 350,290.00 USD | `-36.31%` | `126,687.80` |
| `Live` | `Long` | `2.77` | 15,100,000.00 USD | 0.00 USD | 398.77 USD | `-36.08%` | `143.70` |
| `Live` | `Long` | `2.79` | 15,100,000.00 USD | 0.00 USD | 47,860.00 USD | `-35.85%` | `17,186.00` |
| `Live` | `Long` | `2.79` | 15,050,000.00 USD | 0.00 USD | 12,340.00 USD | `-35.62%` | `4,416.00` |
| `Live` | `Long` | `2.81` | 15,040,000.00 USD | 0.00 USD | 90,180.00 USD | `-35.39%` | `32,148.50` |
| `Live` | `Long` | `2.81` | 14,950,000.00 USD | 0.00 USD | 4,780.00 USD | `-35.16%` | `1,698.90` |
| `Live` | `Long` | `2.83` | 14,950,000.00 USD | 0.00 USD | 2,350.00 USD | `-34.93%` | `832.70` |
| `Live` | `Long` | `2.83` | 14,940,000.00 USD | 0.00 USD | 10,910.00 USD | `-34.70%` | `3,847.80` |
| `Live` | `Long` | `2.85` | 14,930,000.00 USD | 0.00 USD | 3,790.00 USD | `-34.47%` | `1,333.60` |
| `Live` | `Long` | `2.85` | 14,930,000.00 USD | 0.00 USD | 3,540.00 USD | `-34.24%` | `1,240.70` |
| `Live` | `Long` | `2.87` | 14,930,000.00 USD | 0.00 USD | 18,770.00 USD | `-34.01%` | `6,552.50` |
| `Live` | `Long` | `2.88` | 14,910,000.00 USD | 0.00 USD | 868,330.00 USD | `-33.78%` | `302,028.00` |
| `Live` | `Long` | `2.88` | 14,040,000.00 USD | 0.00 USD | 8,470.00 USD | `-33.55%` | `2,934.40` |
| `Live` | `Long` | `2.90` | 14,030,000.00 USD | 0.00 USD | 112,920.00 USD | `-33.32%` | `39,005.40` |
| `Live` | `Long` | `2.90` | 13,920,000.00 USD | 0.00 USD | 4,500.00 USD | `-33.09%` | `1,547.90` |
| `Live` | `Long` | `2.92` | 13,910,000.00 USD | 0.00 USD | 11,820.00 USD | `-32.86%` | `4,055.30` |
| `Live` | `Long` | `2.92` | 13,900,000.00 USD | 0.00 USD | 245,610.00 USD | `-32.63%` | `83,969.90` |
| `Live` | `Long` | `2.94` | 13,660,000.00 USD | 0.00 USD | 50,370.00 USD | `-32.40%` | `17,161.30` |
| `Live` | `Long` | `2.94` | 13,610,000.00 USD | 0.00 USD | 18,090.00 USD | `-32.17%` | `6,142.40` |
| `Live` | `Long` | `2.96` | 13,590,000.00 USD | 0.00 USD | 13,510.00 USD | `-31.94%` | `4,571.50` |
| `Live` | `Long` | `2.96` | 13,570,000.00 USD | 0.00 USD | 1,380.00 USD | `-31.71%` | `465.60` |
| `Live` | `Long` | `2.98` | 13,570,000.00 USD | 0.00 USD | 148,680.00 USD | `-31.48%` | `49,976.10` |
| `Live` | `Long` | `2.98` | 13,420,000.00 USD | 0.00 USD | 5,270.00 USD | `-31.24%` | `1,764.40` |
| `Live` | `Long` | `3.00` | 13,420,000.00 USD | 0.00 USD | 11,160.00 USD | `-31.01%` | `3,725.50` |
| `Live` | `Long` | `3.00` | 13,410,000.00 USD | 0.00 USD | 116,780.00 USD | `-30.78%` | `38,863.00` |
| `Live` | `Long` | `3.02` | 13,290,000.00 USD | 0.00 USD | 26,540.00 USD | `-30.55%` | `8,801.10` |
| `Live` | `Long` | `3.02` | 13,260,000.00 USD | 0.00 USD | 26,810.00 USD | `-30.32%` | `8,863.50` |
| `Live` | `Long` | `3.04` | 13,240,000.00 USD | 0.00 USD | 1,220.00 USD | `-30.09%` | `402.10` |
| `Live` | `Long` | `3.04` | 13,240,000.00 USD | 0.00 USD | 141,830.00 USD | `-29.86%` | `46,576.50` |
| `Live` | `Long` | `3.06` | 13,090,000.00 USD | 0.00 USD | 86,530.00 USD | `-29.63%` | `28,323.50` |
| `Live` | `Long` | `3.06` | 13,010,000.00 USD | 0.00 USD | 130,870.00 USD | `-29.40%` | `42,697.30` |
| `Live` | `Long` | `3.08` | 12,880,000.00 USD | 0.00 USD | 48,380.00 USD | `-28.94%` | `15,683.80` |
| `Live` | `Long` | `3.10` | 12,830,000.00 USD | 0.00 USD | 163,550.00 USD | `-28.71%` | `52,843.20` |
| `Live` | `Long` | `3.10` | 12,660,000.00 USD | 0.00 USD | 25,870.00 USD | `-28.48%` | `8,331.80` |
| `Live` | `Long` | `3.12` | 12,640,000.00 USD | 0.00 USD | 31,050.00 USD | `-28.25%` | `9,969.20` |
| `Live` | `Long` | `3.12` | 12,610,000.00 USD | 0.00 USD | 11,560.00 USD | `-28.02%` | `3,700.50` |
| `Live` | `Long` | `3.13` | 12,600,000.00 USD | 0.00 USD | 35,950.00 USD | `-27.79%` | `11,467.10` |
| `Live` | `Long` | `3.15` | 12,560,000.00 USD | 0.00 USD | 22,930.00 USD | `-27.56%` | `7,291.60` |
| `Live` | `Long` | `3.15` | 12,540,000.00 USD | 0.00 USD | 81,350.00 USD | `-27.33%` | `25,783.10` |
| `Live` | `Long` | `3.17` | 12,460,000.00 USD | 0.00 USD | 181,270.00 USD | `-27.10%` | `57,273.30` |
| `Live` | `Long` | `3.17` | 12,270,000.00 USD | 0.00 USD | 2,860,000.00 USD | `-26.87%` | `901,455.60` |
| `Live` | `Long` | `3.19` | 9,410,000.00 USD | 0.00 USD | 306,920.00 USD | `-26.64%` | `96,363.90` |
| `Live` | `Long` | `3.21` | 9,110,000.00 USD | 0.00 USD | 112.17 USD | `-26.18%` | `35.00` |
| `Live` | `Long` | `3.21` | 9,110,000.00 USD | 0.00 USD | 8,790.00 USD | `-25.95%` | `2,733.30` |
| `Live` | `Long` | `3.23` | 9,100,000.00 USD | 0.00 USD | 23,110.00 USD | `-25.72%` | `7,167.00` |
| `Live` | `Long` | `3.23` | 9,070,000.00 USD | 0.00 USD | 64,820.00 USD | `-25.49%` | `20,036.00` |
| `Live` | `Long` | `3.25` | 9,010,000.00 USD | 0.00 USD | 20,190.00 USD | `-25.26%` | `6,220.90` |
| `Live` | `Long` | `3.25` | 8,990,000.00 USD | 0.00 USD | 4,050.00 USD | `-25.03%` | `1,245.10` |
| `Live` | `Long` | `3.27` | 8,980,000.00 USD | 0.00 USD | 39,060.00 USD | `-24.80%` | `11,963.70` |
| `Live` | `Long` | `3.27` | 8,950,000.00 USD | 0.00 USD | 869,330.00 USD | `-24.57%` | `265,445.20` |
| `Live` | `Long` | `3.29` | 8,080,000.00 USD | 0.00 USD | 4,080.00 USD | `-24.33%` | `1,240.60` |
| `Live` | `Long` | `3.29` | 8,070,000.00 USD | 0.00 USD | 133,000.00 USD | `-24.10%` | `40,362.70` |
| `Live` | `Long` | `3.31` | 7,940,000.00 USD | 0.00 USD | 132,030.00 USD | `-23.87%` | `39,948.60` |
| `Live` | `Long` | `3.31` | 7,810,000.00 USD | 0.00 USD | 24,690.00 USD | `-23.64%` | `7,448.70` |
| `Live` | `Long` | `3.33` | 7,780,000.00 USD | 0.00 USD | 10,380.00 USD | `-23.41%` | `3,121.60` |
| `Live` | `Long` | `3.33` | 7,770,000.00 USD | 0.00 USD | 77,700.00 USD | `-23.18%` | `23,297.70` |
| `Live` | `Long` | `3.35` | 7,690,000.00 USD | 0.00 USD | 22,160.00 USD | `-22.95%` | `6,625.40` |
| `Live` | `Long` | `3.35` | 7,670,000.00 USD | 0.00 USD | 1,210.00 USD | `-22.72%` | `360.80` |
| `Live` | `Long` | `3.37` | 7,670,000.00 USD | 0.00 USD | 24,110.00 USD | `-22.49%` | `7,163.70` |
| `Live` | `Long` | `3.38` | 7,650,000.00 USD | 0.00 USD | 54,650.00 USD | `-22.26%` | `16,193.90` |
| `Live` | `Long` | `3.38` | 7,590,000.00 USD | 0.00 USD | 40,370.00 USD | `-22.03%` | `11,926.20` |
| `Live` | `Long` | `3.40` | 7,550,000.00 USD | 0.00 USD | 41,460.00 USD | `-21.80%` | `12,212.30` |
| `Live` | `Long` | `3.40` | 7,510,000.00 USD | 0.00 USD | 103,060.00 USD | `-21.57%` | `30,267.20` |
| `Live` | `Long` | `3.42` | 7,410,000.00 USD | 0.00 USD | 390,990.00 USD | `-21.34%` | `114,490.80` |
| `Live` | `Long` | `3.42` | 7,020,000.00 USD | 0.00 USD | 6,570.00 USD | `-21.11%` | `1,918.80` |
| `Live` | `Long` | `3.44` | 7,010,000.00 USD | 0.00 USD | 29,310.00 USD | `-20.88%` | `8,533.80` |
| `Live` | `Long` | `3.44` | 6,980,000.00 USD | 0.00 USD | 26,840.00 USD | `-20.65%` | `7,792.20` |
| `Live` | `Long` | `3.46` | 6,950,000.00 USD | 0.00 USD | 151,120.00 USD | `-20.42%` | `43,739.10` |
| `Live` | `Long` | `3.46` | 6,800,000.00 USD | 0.00 USD | 16,150.00 USD | `-20.19%` | `4,661.90` |
| `Live` | `Long` | `3.48` | 6,790,000.00 USD | 0.00 USD | 116,220.00 USD | `-19.96%` | `33,445.40` |
| `Live` | `Long` | `3.48` | 6,670,000.00 USD | 0.00 USD | 267,390.00 USD | `-19.73%` | `76,724.80` |
| `Live` | `Long` | `3.50` | 6,400,000.00 USD | 0.00 USD | 48,130.00 USD | `-19.50%` | `13,771.70` |
| `Live` | `Long` | `3.50` | 6,350,000.00 USD | 0.00 USD | 33,810.00 USD | `-19.27%` | `9,647.00` |
| `Live` | `Long` | `3.52` | 6,320,000.00 USD | 0.00 USD | 42,800.00 USD | `-19.04%` | `12,176.80` |
| `Live` | `Long` | `3.52` | 6,280,000.00 USD | 0.00 USD | 21,970.00 USD | `-18.81%` | `6,232.60` |
| `Live` | `Long` | `3.54` | 6,260,000.00 USD | 0.00 USD | 77,190.00 USD | `-18.58%` | `21,836.90` |
| `Live` | `Long` | `3.54` | 6,180,000.00 USD | 0.00 USD | 159,350.00 USD | `-18.35%` | `44,951.40` |
| `Live` | `Long` | `3.56` | 6,020,000.00 USD | 0.00 USD | 570,020.00 USD | `-18.12%` | `160,343.30` |
| `Live` | `Long` | `3.56` | 5,450,000.00 USD | 0.00 USD | 7,550.00 USD | `-17.89%` | `2,117.70` |
| `Live` | `Long` | `3.58` | 5,440,000.00 USD | 0.00 USD | 1,340,000.00 USD | `-17.66%` | `373,566.50` |
| `Live` | `Long` | `3.58` | 4,110,000.00 USD | 0.00 USD | 52,750.00 USD | `-17.42%` | `14,714.40` |
| `Live` | `Long` | `3.60` | 4,050,000.00 USD | 0.00 USD | 23,850.00 USD | `-17.19%` | `6,633.20` |
| `Live` | `Long` | `3.60` | 4,030,000.00 USD | 0.00 USD | 63,970.00 USD | `-16.96%` | `17,746.00` |
| `Live` | `Long` | `3.62` | 3,970,000.00 USD | 0.00 USD | 102,890.00 USD | `-16.73%` | `28,462.50` |
| `Live` | `Long` | `3.62` | 3,860,000.00 USD | 0.00 USD | 114,340.00 USD | `-16.50%` | `31,542.70` |
| `Live` | `Long` | `3.63` | 3,750,000.00 USD | 0.00 USD | 1,670.00 USD | `-16.27%` | `458.20` |
| `Live` | `Long` | `3.65` | 3,750,000.00 USD | 0.00 USD | 333,140.00 USD | `-16.04%` | `91,395.10` |
| `Live` | `Long` | `3.65` | 3,410,000.00 USD | 0.00 USD | 20,750.00 USD | `-15.81%` | `5,676.60` |
| `Live` | `Long` | `3.67` | 3,390,000.00 USD | 0.00 USD | 171,100.00 USD | `-15.58%` | `46,685.60` |
| `Live` | `Long` | `3.67` | 3,220,000.00 USD | 0.00 USD | 95,680.00 USD | `-15.35%` | `26,036.10` |
| `Live` | `Long` | `3.69` | 3,130,000.00 USD | 0.00 USD | 224,510.00 USD | `-15.12%` | `60,924.30` |
| `Live` | `Long` | `3.69` | 2,900,000.00 USD | 0.00 USD | 93,310.00 USD | `-14.89%` | `25,252.00` |
| `Live` | `Long` | `3.71` | 2,810,000.00 USD | 0.00 USD | 79,950.00 USD | `-14.66%` | `21,579.30` |
| `Live` | `Long` | `3.71` | 2,730,000.00 USD | 0.00 USD | 11,810.00 USD | `-14.43%` | `3,180.20` |
| `Live` | `Long` | `3.73` | 2,720,000.00 USD | 0.00 USD | 224,430.00 USD | `-14.20%` | `60,250.20` |
| `Live` | `Long` | `3.73` | 2,490,000.00 USD | 0.00 USD | 119,590.00 USD | `-13.97%` | `32,019.80` |
| `Live` | `Long` | `3.75` | 2,370,000.00 USD | 0.00 USD | 25,820.00 USD | `-13.74%` | `6,895.80` |
| `Live` | `Long` | `3.75` | 2,350,000.00 USD | 0.00 USD | 150,270.00 USD | `-13.51%` | `40,017.50` |
| `Live` | `Long` | `3.77` | 2,200,000.00 USD | 0.00 USD | 65,080.00 USD | `-13.28%` | `17,286.40` |
| `Live` | `Long` | `3.77` | 2,130,000.00 USD | 0.00 USD | 29,390.00 USD | `-13.05%` | `7,786.10` |
| `Live` | `Long` | `3.79` | 2,100,000.00 USD | 0.00 USD | 59,430.00 USD | `-12.82%` | `15,701.60` |
| `Live` | `Long` | `3.79` | 2,040,000.00 USD | 0.00 USD | 37,390.00 USD | `-12.59%` | `9,851.70` |
| `Live` | `Long` | `3.81` | 2,010,000.00 USD | 0.00 USD | 570,030.00 USD | `-12.36%` | `149,810.30` |
| `Live` | `Long` | `3.81` | 1,440,000.00 USD | 0.00 USD | 14,090.00 USD | `-12.13%` | `3,694.00` |
| `Live` | `Long` | `3.83` | 1,420,000.00 USD | 0.00 USD | 134,350.00 USD | `-11.90%` | `35,123.90` |
| `Live` | `Long` | `3.83` | 1,290,000.00 USD | 0.00 USD | 171,380.00 USD | `-11.67%` | `44,688.70` |
| `Live` | `Long` | `3.85` | 1,120,000.00 USD | 0.00 USD | 116,490.00 USD | `-11.44%` | `30,296.00` |
| `Live` | `Long` | `3.85` | 998,740.00 USD | 0.00 USD | 22,330.00 USD | `-11.21%` | `5,792.70` |
| `Live` | `Long` | `3.87` | 976,410.00 USD | 0.00 USD | 71,550.00 USD | `-10.98%` | `18,512.20` |
| `Live` | `Long` | `3.88` | 904,860.00 USD | 0.00 USD | 7,870.00 USD | `-10.75%` | `2,030.50` |
| `Live` | `Long` | `3.88` | 896,990.00 USD | 0.00 USD | 175,650.00 USD | `-10.51%` | `45,213.00` |
| `Live` | `Long` | `3.90` | 721,340.00 USD | 0.00 USD | 93,930.00 USD | `-10.28%` | `24,116.30` |
| `Live` | `Long` | `3.90` | 627,410.00 USD | 0.00 USD | 8,860.00 USD | `-10.05%` | `2,268.20` |
| `Live` | `Long` | `3.92` | 618,550.00 USD | 0.00 USD | 132,720.00 USD | `-9.82%` | `33,899.30` |
| `Live` | `Long` | `3.92` | 485,830.00 USD | 0.00 USD | 2,050.00 USD | `-9.59%` | `522.20` |
| `Live` | `Long` | `3.94` | 483,780.00 USD | 0.00 USD | 3,320.00 USD | `-9.36%` | `844.50` |
| `Live` | `Long` | `3.94` | 480,460.00 USD | 0.00 USD | 22,630.00 USD | `-9.13%` | `5,736.60` |
| `Live` | `Long` | `3.96` | 457,830.00 USD | 0.00 USD | 55,290.00 USD | `-8.90%` | `13,979.20` |
| `Live` | `Long` | `3.96` | 402,540.00 USD | 0.00 USD | 2,110.00 USD | `-8.67%` | `533.00` |
| `Live` | `Long` | `3.98` | 400,430.00 USD | 0.00 USD | 26,000.00 USD | `-8.44%` | `6,541.70` |
| `Live` | `Long` | `3.98` | 374,420.00 USD | 0.00 USD | 1,070.00 USD | `-8.21%` | `268.00` |
| `Live` | `Long` | `4.00` | 373,360.00 USD | 0.00 USD | 160,840.00 USD | `-7.98%` | `40,260.30` |
| `Live` | `Long` | `4.00` | 212,520.00 USD | 0.00 USD | 13,260.00 USD | `-7.75%` | `3,311.20` |
| `Live` | `Long` | `4.01` | 199,250.00 USD | 0.00 USD | 275.83 USD | `-7.52%` | `68.70` |
| `Live` | `Long` | `4.03` | 198,980.00 USD | 0.00 USD | 2,110.00 USD | `-7.29%` | `524.90` |
| `Live` | `Long` | `4.04` | 196,870.00 USD | 0.00 USD | 24,650.00 USD | `-7.06%` | `6,108.60` |
| `Live` | `Long` | `4.04` | 172,220.00 USD | 0.00 USD | 21,310.00 USD | `-6.83%` | `5,268.70` |
| `Live` | `Long` | `4.05` | 150,910.00 USD | 0.00 USD | 54,890.00 USD | `-6.60%` | `13,535.60` |
| `Live` | `Long` | `4.07` | 96,020.00 USD | 0.00 USD | 1,200.00 USD | `-6.37%` | `295.00` |
| `Live` | `Long` | `4.08` | 94,820.00 USD | 0.00 USD | 2,640.00 USD | `-6.14%` | `647.70` |
| `Live` | `Long` | `4.08` | 92,180.00 USD | 0.00 USD | 8,310.00 USD | `-5.91%` | `2,034.10` |
| `Live` | `Long` | `4.09` | 83,870.00 USD | 0.00 USD | 19,450.00 USD | `-5.68%` | `4,748.50` |
| `Live` | `Long` | `4.11` | 64,430.00 USD | 0.00 USD | 25,410.00 USD | `-5.45%` | `6,191.00` |
| `Live` | `Long` | `4.12` | 39,010.00 USD | 0.00 USD | 16,830.00 USD | `-5.22%` | `4,089.40` |
| `Live` | `Long` | `4.12` | 22,180.00 USD | 0.00 USD | 10,570.00 USD | `-4.99%` | `2,562.30` |
| `Live` | `Long` | `4.13` | 11,610.00 USD | 0.00 USD | 2,230.00 USD | `-4.76%` | `539.70` |
| `Live` | `Long` | `4.14` | 9,380.00 USD | 0.00 USD | 652.84 USD | `-4.53%` | `157.50` |
| `Live` | `Long` | `4.16` | 8,730.00 USD | 0.00 USD | 8,730.00 USD | `-4.30%` | `2,101.20` |
| `Live` | `Short` | `4.24` | 15,550.00 USD | 15,550.00 USD | 0.00 USD | `-2.45%` | `3,670.90` |
| `Live` | `Short` | `4.39` | 196,310.00 USD | 180,760.00 USD | 0.00 USD | `+1.23%` | `41,128.80` |
| `Live` | `Short` | `4.42` | 198,240.00 USD | 1,930.00 USD | 0.00 USD | `+1.92%` | `436.00` |
| `Live` | `Short` | `4.43` | 201,770.00 USD | 3,540.00 USD | 0.00 USD | `+2.15%` | `797.70` |
| `Live` | `Short` | `4.45` | 202,130.00 USD | 358.27 USD | 0.00 USD | `+2.38%` | `80.60` |
| `Live` | `Short` | `4.46` | 238,820.00 USD | 36,680.00 USD | 0.00 USD | `+2.61%` | `8,234.00` |
| `Live` | `Short` | `4.46` | 240,190.00 USD | 1,370.00 USD | 0.00 USD | `+2.84%` | `306.90` |
| `Live` | `Short` | `4.47` | 257,580.00 USD | 17,400.00 USD | 0.00 USD | `+3.07%` | `3,887.90` |
| `Live` | `Short` | `4.49` | 260,560.00 USD | 2,970.00 USD | 0.00 USD | `+3.31%` | `663.30` |
| `Live` | `Short` | `4.50` | 283,230.00 USD | 22,680.00 USD | 0.00 USD | `+3.54%` | `5,044.50` |
| `Live` | `Short` | `4.50` | 291,180.00 USD | 7,940.00 USD | 0.00 USD | `+3.77%` | `1,763.30` |
| `Live` | `Short` | `4.51` | 300,730.00 USD | 9,560.00 USD | 0.00 USD | `+4.00%` | `2,116.70` |
| `Live` | `Short` | `4.53` | 307,850.00 USD | 7,110.00 USD | 0.00 USD | `+4.23%` | `1,572.30` |
| `Live` | `Short` | `4.54` | 315,170.00 USD | 7,320.00 USD | 0.00 USD | `+4.46%` | `1,614.30` |
| `Live` | `Short` | `4.54` | 325,240.00 USD | 10,070.00 USD | 0.00 USD | `+4.69%` | `2,215.40` |
| `Live` | `Short` | `4.55` | 339,350.00 USD | 14,110.00 USD | 0.00 USD | `+4.92%` | `3,098.50` |
| `Live` | `Short` | `4.57` | 348,140.00 USD | 8,790.00 USD | 0.00 USD | `+5.15%` | `1,925.70` |
| `Live` | `Short` | `4.58` | 349,940.00 USD | 1,800.00 USD | 0.00 USD | `+5.61%` | `391.60` |
| `Live` | `Short` | `4.62` | 401,630.00 USD | 51,690.00 USD | 0.00 USD | `+6.53%` | `11,176.20` |
| `Live` | `Short` | `4.63` | 551,900.00 USD | 150,270.00 USD | 0.00 USD | `+6.76%` | `32,421.00` |
| `Live` | `Short` | `4.64` | 552,750.00 USD | 852.82 USD | 0.00 USD | `+6.99%` | `183.60` |
| `Live` | `Short` | `4.66` | 553,510.00 USD | 756.44 USD | 0.00 USD | `+7.22%` | `162.50` |
| `Live` | `Short` | `4.67` | 561,390.00 USD | 7,880.00 USD | 0.00 USD | `+7.45%` | `1,688.80` |
| `Live` | `Short` | `4.67` | 616,030.00 USD | 54,640.00 USD | 0.00 USD | `+7.68%` | `11,687.70` |
| `Live` | `Short` | `4.68` | 617,060.00 USD | 1,030.00 USD | 0.00 USD | `+7.91%` | `220.50` |
| `Live` | `Short` | `4.70` | 617,290.00 USD | 230.06 USD | 0.00 USD | `+8.14%` | `49.00` |
| `Live` | `Short` | `4.71` | 624,250.00 USD | 6,960.00 USD | 0.00 USD | `+8.37%` | `1,479.20` |
| `Live` | `Short` | `4.72` | 637,050.00 USD | 12,800.00 USD | 0.00 USD | `+8.83%` | `2,709.30` |
| `Live` | `Short` | `4.74` | 640,900.00 USD | 3,850.00 USD | 0.00 USD | `+9.06%` | `812.50` |
| `Live` | `Short` | `4.75` | 752,030.00 USD | 111,130.00 USD | 0.00 USD | `+9.29%` | `23,421.00` |
| `Live` | `Short` | `4.76` | 847,330.00 USD | 95,300.00 USD | 0.00 USD | `+9.75%` | `20,000.00` |
| `Live` | `Short` | `4.78` | 849,060.00 USD | 1,730.00 USD | 0.00 USD | `+9.99%` | `362.40` |
| `Live` | `Short` | `4.79` | 849,210.00 USD | 143.55 USD | 0.00 USD | `+10.22%` | `30.00` |
| `Live` | `Short` | `4.79` | 850,540.00 USD | 1,330.00 USD | 0.00 USD | `+10.45%` | `277.70` |
| `Live` | `Short` | `4.82` | 856,320.00 USD | 5,780.00 USD | 0.00 USD | `+10.91%` | `1,200.00` |
| `Live` | `Short` | `4.83` | 858,670.00 USD | 2,360.00 USD | 0.00 USD | `+11.14%` | `489.00` |
| `Live` | `Short` | `4.83` | 860,210.00 USD | 1,540.00 USD | 0.00 USD | `+11.37%` | `317.90` |
| `Live` | `Short` | `4.84` | 871,430.00 USD | 11,220.00 USD | 0.00 USD | `+11.60%` | `2,316.40` |
| `Live` | `Short` | `4.87` | 871,690.00 USD | 259.79 USD | 0.00 USD | `+12.06%` | `53.40` |
| `Live` | `Short` | `4.88` | 872,520.00 USD | 827.03 USD | 0.00 USD | `+12.52%` | `169.30` |
| `Live` | `Short` | `4.91` | 873,200.00 USD | 674.44 USD | 0.00 USD | `+12.98%` | `137.50` |
| `Live` | `Short` | `4.92` | 893,910.00 USD | 20,720.00 USD | 0.00 USD | `+13.21%` | `4,214.80` |
| `Live` | `Short` | `4.92` | 896,500.00 USD | 2,590.00 USD | 0.00 USD | `+13.44%` | `526.30` |
| `Live` | `Short` | `4.93` | 908,810.00 USD | 12,300.00 USD | 0.00 USD | `+13.67%` | `2,493.30` |
| `Live` | `Short` | `4.96` | 909,300.00 USD | 488.56 USD | 0.00 USD | `+14.13%` | `98.60` |
| `Live` | `Short` | `4.97` | 1,010,000.00 USD | 99,370.00 USD | 0.00 USD | `+14.59%` | `19,974.00` |
| `Live` | `Short` | `5.04` | 1,010,000.00 USD | 118.83 USD | 0.00 USD | `+15.97%` | `23.60` |
| `Live` | `Short` | `5.05` | 1,040,000.00 USD | 35,380.00 USD | 0.00 USD | `+16.43%` | `6,998.80` |
| `Live` | `Short` | `5.07` | 1,050,000.00 USD | 3,420.00 USD | 0.00 USD | `+16.66%` | `675.80` |
| `Live` | `Short` | `5.08` | 1,050,000.00 USD | 6,860.00 USD | 0.00 USD | `+17.13%` | `1,349.30` |
| `Live` | `Short` | `5.09` | 1,060,000.00 USD | 6,650.00 USD | 0.00 USD | `+17.36%` | `1,306.10` |
| `Live` | `Short` | `5.12` | 1,110,000.00 USD | 51,430.00 USD | 0.00 USD | `+18.05%` | `10,034.70` |
| `Live` | `Short` | `5.16` | 1,120,000.00 USD | 2,580.00 USD | 0.00 USD | `+18.74%` | `500.00` |
| `Live` | `Short` | `5.17` | 1,120,000.00 USD | 751.51 USD | 0.00 USD | `+18.97%` | `145.50` |
| `Live` | `Short` | `5.22` | 1,190,000.00 USD | 72,940.00 USD | 0.00 USD | `+20.35%` | `13,959.60` |
| `Live` | `Short` | `5.24` | 1,210,000.00 USD | 17,260.00 USD | 0.00 USD | `+20.58%` | `3,297.00` |
| `Live` | `Short` | `5.25` | 1,210,000.00 USD | 143.71 USD | 0.00 USD | `+20.81%` | `27.40` |
| `Live` | `Short` | `5.25` | 1,220,000.00 USD | 17,380.00 USD | 0.00 USD | `+21.04%` | `3,307.90` |
| `Live` | `Short` | `5.26` | 1,230,000.00 USD | 6,220.00 USD | 0.00 USD | `+21.27%` | `1,181.40` |
| `Live` | `Short` | `5.29` | 1,230,000.00 USD | 134.77 USD | 0.00 USD | `+21.73%` | `25.50` |
| `Live` | `Short` | `5.30` | 1,230,000.00 USD | 524.66 USD | 0.00 USD | `+22.19%` | `98.90` |
| `Live` | `Short` | `5.33` | 2,300,000.00 USD | 1,070,000.00 USD | 0.00 USD | `+22.88%` | `200,053.70` |
| `Live` | `Short` | `5.34` | 2,600,000.00 USD | 298,680.00 USD | 0.00 USD | `+23.11%` | `55,879.90` |
| `Live` | `Short` | `5.36` | 2,600,000.00 USD | 142.44 USD | 0.00 USD | `+23.34%` | `26.60` |
| `Live` | `Short` | `5.38` | 2,630,000.00 USD | 37,990.00 USD | 0.00 USD | `+23.81%` | `7,068.80` |
| `Live` | `Short` | `5.42` | 2,950,000.00 USD | 313,840.00 USD | 0.00 USD | `+24.73%` | `57,958.30` |
| `Live` | `Short` | `5.42` | 2,950,000.00 USD | 914.65 USD | 0.00 USD | `+24.96%` | `168.60` |
| `Live` | `Short` | `5.43` | 2,950,000.00 USD | 419.04 USD | 0.00 USD | `+25.19%` | `77.10` |
| `Live` | `Short` | `5.47` | 2,960,000.00 USD | 12,190.00 USD | 0.00 USD | `+26.11%` | `2,226.70` |
| `Live` | `Short` | `5.50` | 3,090,000.00 USD | 128,840.00 USD | 0.00 USD | `+26.57%` | `23,447.00` |
| `Live` | `Short` | `5.50` | 3,100,000.00 USD | 12,780.00 USD | 0.00 USD | `+26.80%` | `2,322.30` |
| `Live` | `Short` | `5.53` | 3,100,000.00 USD | 1,270.00 USD | 0.00 USD | `+27.26%` | `229.80` |
| `Live` | `Short` | `5.54` | 3,110,000.00 USD | 209.22 USD | 0.00 USD | `+27.49%` | `37.80` |
| `Live` | `Short` | `5.57` | 3,110,000.00 USD | 8,670.00 USD | 0.00 USD | `+28.18%` | `1,557.40` |
| `Live` | `Short` | `5.58` | 3,180,000.00 USD | 62,420.00 USD | 0.00 USD | `+28.64%` | `11,175.80` |
| `Live` | `Short` | `5.62` | 3,180,000.00 USD | 532.69 USD | 0.00 USD | `+29.56%` | `94.70` |
| `Live` | `Short` | `5.67` | 8,600,000.00 USD | 5,420,000.00 USD | 0.00 USD | `+30.48%` | `957,107.60` |
| `Live` | `Short` | `5.67` | 8,600,000.00 USD | 228.70 USD | 0.00 USD | `+30.72%` | `40.30` |
| `Live` | `Short` | `5.68` | 8,620,000.00 USD | 26,090.00 USD | 0.00 USD | `+30.95%` | `4,589.50` |
| `Live` | `Short` | `5.70` | 8,630,000.00 USD | 1,520.00 USD | 0.00 USD | `+31.18%` | `267.40` |
| `Live` | `Short` | `5.71` | 8,630,000.00 USD | 2,130.00 USD | 0.00 USD | `+31.64%` | `372.40` |
| `Live` | `Short` | `5.75` | 9,110,000.00 USD | 481,600.00 USD | 0.00 USD | `+32.33%` | `83,830.20` |
| `Live` | `Short` | `5.75` | 9,110,000.00 USD | 286.02 USD | 0.00 USD | `+32.56%` | `49.70` |
| `Live` | `Short` | `5.79` | 9,130,000.00 USD | 16,050.00 USD | 0.00 USD | `+33.48%` | `2,769.00` |
| `Live` | `Short` | `5.83` | 9,130,000.00 USD | 198.97 USD | 0.00 USD | `+34.40%` | `34.10` |
| `Live` | `Short` | `5.84` | 9,130,000.00 USD | 310.95 USD | 0.00 USD | `+34.63%` | `53.20` |
| `Live` | `Short` | `5.86` | 9,130,000.00 USD | 848.39 USD | 0.00 USD | `+34.86%` | `144.90` |
| `Live` | `Short` | `5.88` | 9,130,000.00 USD | 190.67 USD | 0.00 USD | `+35.55%` | `32.40` |
| `Live` | `Short` | `5.89` | 9,240,000.00 USD | 112,780.00 USD | 0.00 USD | `+35.78%` | `19,131.80` |
| `Live` | `Short` | `5.91` | 9,240,000.00 USD | 162.98 USD | 0.00 USD | `+36.01%` | `27.60` |
| `Live` | `Short` | `5.92` | 9,240,000.00 USD | 189.28 USD | 0.00 USD | `+36.24%` | `32.00` |
| `Live` | `Short` | `5.95` | 9,340,000.00 USD | 103,650.00 USD | 0.00 USD | `+36.93%` | `17,434.80` |
| `Live` | `Short` | `5.96` | 9,370,000.00 USD | 29,860.00 USD | 0.00 USD | `+37.16%` | `5,014.50` |
| `Live` | `Short` | `6.00` | 9,400,000.00 USD | 23,320.00 USD | 0.00 USD | `+38.32%` | `3,883.80` |
| `Live` | `Short` | `6.07` | 9,400,000.00 USD | 740.54 USD | 0.00 USD | `+39.70%` | `122.10` |
| `Live` | `Short` | `6.08` | 9,410,000.00 USD | 7,290.00 USD | 0.00 USD | `+40.16%` | `1,198.10` |
| `Live` | `Short` | `6.09` | 9,440,000.00 USD | 37,510.00 USD | 0.00 USD | `+40.39%` | `6,154.10` |
| `Live` | `Short` | `6.12` | 9,470,000.00 USD | 28,250.00 USD | 0.00 USD | `+41.08%` | `4,611.60` |
| `Live` | `Short` | `6.13` | 9,470,000.00 USD | 2,430.00 USD | 0.00 USD | `+41.31%` | `396.10` |
| `Live` | `Short` | `6.14` | 9,480,000.00 USD | 1,870.00 USD | 0.00 USD | `+41.54%` | `305.00` |
| `Live` | `Short` | `6.16` | 9,490,000.00 USD | 12,760.00 USD | 0.00 USD | `+41.77%` | `2,073.30` |
| `Live` | `Short` | `6.18` | 9,520,000.00 USD | 35,350.00 USD | 0.00 USD | `+42.46%` | `5,715.90` |
| `Live` | `Short` | `6.22` | 9,530,000.00 USD | 2,010.00 USD | 0.00 USD | `+43.38%` | `323.00` |
| `Live` | `Short` | `6.24` | 10,050,000.00 USD | 526,230.00 USD | 0.00 USD | `+43.61%` | `84,400.00` |
| `Live` | `Short` | `6.25` | 10,320,000.00 USD | 262,530.00 USD | 0.00 USD | `+43.84%` | `42,038.20` |
| `Live` | `Short` | `6.25` | 10,320,000.00 USD | 439.10 USD | 0.00 USD | `+44.07%` | `70.20` |
| `Live` | `Short` | `6.29` | 10,320,000.00 USD | 5,360.00 USD | 0.00 USD | `+44.77%` | `852.80` |
| `Live` | `Short` | `6.29` | 10,660,000.00 USD | 336,800.00 USD | 0.00 USD | `+45.00%` | `53,503.40` |
| `Live` | `Short` | `6.32` | 10,660,000.00 USD | 310.70 USD | 0.00 USD | `+45.46%` | `49.20` |
| `Live` | `Short` | `6.33` | 10,660,000.00 USD | 382.00 USD | 0.00 USD | `+45.92%` | `60.30` |
| `Live` | `Short` | `6.34` | 10,660,000.00 USD | 214.46 USD | 0.00 USD | `+46.15%` | `33.80` |
| `Live` | `Short` | `6.37` | 10,660,000.00 USD | 113.93 USD | 0.00 USD | `+46.61%` | `17.90` |
| `Live` | `Short` | `6.38` | 10,660,000.00 USD | 288.15 USD | 0.00 USD | `+46.84%` | `45.20` |
| `Live` | `Short` | `6.39` | 10,660,000.00 USD | 2,000.00 USD | 0.00 USD | `+47.30%` | `312.80` |
| `Live` | `Short` | `6.41` | 10,660,000.00 USD | 3,780.00 USD | 0.00 USD | `+47.53%` | `590.10` |
| `Live` | `Short` | `6.42` | 10,670,000.00 USD | 943.65 USD | 0.00 USD | `+47.76%` | `147.10` |
| `Live` | `Short` | `6.42` | 10,670,000.00 USD | 173.47 USD | 0.00 USD | `+47.99%` | `27.00` |
| `Live` | `Short` | `6.45` | 10,670,000.00 USD | 5,270.00 USD | 0.00 USD | `+48.45%` | `818.40` |
| `Live` | `Short` | `6.46` | 39,770,000.00 USD | 29,100,000.00 USD | 0.00 USD | `+48.68%` | `4,508,369.60` |
| `Live` | `Short` | `6.46` | 39,770,000.00 USD | 1,940.00 USD | 0.00 USD | `+48.91%` | `300.00` |
| `Live` | `Short` | `6.51` | 39,800,000.00 USD | 24,040.00 USD | 0.00 USD | `+50.06%` | `3,689.70` |
| `Live` | `Short` | `6.54` | 39,800,000.00 USD | 265.07 USD | 0.00 USD | `+50.75%` | `40.50` |
| `Live` | `Short` | `6.57` | 39,810,000.00 USD | 7,670.00 USD | 0.00 USD | `+51.22%` | `1,168.60` |
| `Live` | `Short` | `6.59` | 39,810,000.00 USD | 418.78 USD | 0.00 USD | `+51.91%` | `63.50` |
| `Live` | `Short` | `6.62` | 41,050,000.00 USD | 1,240,000.00 USD | 0.00 USD | `+52.37%` | `188,000.00` |
| `Live` | `Short` | `6.62` | 41,090,000.00 USD | 42,100.00 USD | 0.00 USD | `+52.60%` | `6,354.10` |
| `Live` | `Short` | `6.63` | 41,090,000.00 USD | 2,090.00 USD | 0.00 USD | `+52.83%` | `315.60` |
| `Live` | `Short` | `6.66` | 41,100,000.00 USD | 7,940.00 USD | 0.00 USD | `+53.29%` | `1,193.00` |
| `Live` | `Short` | `6.67` | 41,100,000.00 USD | 233.94 USD | 0.00 USD | `+53.52%` | `35.10` |
| `Live` | `Short` | `6.67` | 41,140,000.00 USD | 41,520.00 USD | 0.00 USD | `+53.75%` | `6,220.00` |
| `Live` | `Short` | `6.68` | 41,180,000.00 USD | 37,150.00 USD | 0.00 USD | `+53.98%` | `5,556.90` |
| `Live` | `Short` | `6.71` | 41,570,000.00 USD | 388,480.00 USD | 0.00 USD | `+54.44%` | `57,938.40` |
| `Live` | `Short` | `6.75` | 42,820,000.00 USD | 1,250,000.00 USD | 0.00 USD | `+55.59%` | `184,501.00` |
| `Live` | `Short` | `6.83` | 42,820,000.00 USD | 187.69 USD | 0.00 USD | `+57.20%` | `27.50` |
| `Live` | `Short` | `6.84` | 42,820,000.00 USD | 753.63 USD | 0.00 USD | `+57.66%` | `110.10` |
| `Live` | `Short` | `6.86` | 42,820,000.00 USD | 623.81 USD | 0.00 USD | `+57.89%` | `91.00` |
| `Live` | `Short` | `6.87` | 42,820,000.00 USD | 2,650.00 USD | 0.00 USD | `+58.13%` | `386.60` |
| `Live` | `Short` | `6.92` | 42,830,000.00 USD | 7,900.00 USD | 0.00 USD | `+59.51%` | `1,140.60` |
| `Live` | `Short` | `6.99` | 42,920,000.00 USD | 94,030.00 USD | 0.00 USD | `+60.89%` | `13,462.20` |
| `Live` | `Short` | `7.00` | 42,950,000.00 USD | 24,680.00 USD | 0.00 USD | `+61.35%` | `3,523.00` |
| `Live` | `Short` | `7.09` | 42,950,000.00 USD | 699.57 USD | 0.00 USD | `+63.42%` | `98.60` |
| `Live` | `Short` | `7.16` | 42,960,000.00 USD | 16,010.00 USD | 0.00 USD | `+64.80%` | `2,237.40` |
| `Live` | `Short` | `7.21` | 42,980,000.00 USD | 17,040.00 USD | 0.00 USD | `+66.19%` | `2,361.10` |
| `Live` | `Short` | `7.24` | 42,980,000.00 USD | 1,150.00 USD | 0.00 USD | `+66.65%` | `159.30` |
| `Live` | `Short` | `7.25` | 42,990,000.00 USD | 3,770.00 USD | 0.00 USD | `+66.88%` | `520.00` |
| `Live` | `Short` | `7.28` | 42,990,000.00 USD | 2,260.00 USD | 0.00 USD | `+67.57%` | `310.00` |
| `Live` | `Short` | `7.30` | 43,040,000.00 USD | 54,790.00 USD | 0.00 USD | `+68.26%` | `7,500.00` |
| `Live` | `Short` | `7.32` | 46,930,000.00 USD | 3,880,000.00 USD | 0.00 USD | `+68.49%` | `531,079.30` |
| `Live` | `Short` | `7.33` | 46,940,000.00 USD | 14,160.00 USD | 0.00 USD | `+68.95%` | `1,930.00` |
| `Live` | `Short` | `7.42` | 46,940,000.00 USD | 777.09 USD | 0.00 USD | `+70.79%` | `104.80` |
| `Live` | `Short` | `7.42` | 47,050,000.00 USD | 106,000.00 USD | 0.00 USD | `+71.02%` | `14,276.50` |
| `Live` | `Short` | `7.46` | 57,010,000.00 USD | 9,960,000.00 USD | 0.00 USD | `+71.71%` | `1,336,191.10` |
| `Live` | `Short` | `7.50` | 57,010,000.00 USD | 481.82 USD | 0.00 USD | `+72.87%` | `64.20` |
| `Live` | `Short` | `7.53` | 57,010,000.00 USD | 1,570.00 USD | 0.00 USD | `+73.33%` | `208.40` |
| `Live` | `Short` | `7.54` | 64,850,000.00 USD | 7,840,000.00 USD | 0.00 USD | `+73.56%` | `1,040,428.20` |
| `Live` | `Short` | `7.55` | 64,850,000.00 USD | 115.59 USD | 0.00 USD | `+74.02%` | `15.30` |
| `Live` | `Short` | `7.62` | 64,860,000.00 USD | 9,100.00 USD | 0.00 USD | `+75.40%` | `1,194.40` |
| `Live` | `Short` | `7.63` | 64,910,000.00 USD | 45,910.00 USD | 0.00 USD | `+75.86%` | `6,012.60` |
| `Live` | `Short` | `7.64` | 64,920,000.00 USD | 17,820.00 USD | 0.00 USD | `+76.09%` | `2,330.50` |
| `Live` | `Short` | `7.66` | 64,970,000.00 USD | 46,030.00 USD | 0.00 USD | `+76.32%` | `6,012.80` |
| `Live` | `Short` | `7.67` | 64,970,000.00 USD | 360.25 USD | 0.00 USD | `+76.55%` | `47.00` |
| `Live` | `Short` | `7.71` | 64,980,000.00 USD | 4,450.00 USD | 0.00 USD | `+77.47%` | `577.20` |
| `Live` | `Short` | `7.72` | 66,170,000.00 USD | 1,200,000.00 USD | 0.00 USD | `+77.93%` | `154,780.70` |
| `Live` | `Short` | `7.74` | 66,210,000.00 USD | 33,830.00 USD | 0.00 USD | `+78.16%` | `4,373.90` |
| `Live` | `Short` | `7.75` | 66,210,000.00 USD | 629.67 USD | 0.00 USD | `+78.39%` | `81.30` |
| `Live` | `Short` | `7.76` | 66,210,000.00 USD | 1,680.00 USD | 0.00 USD | `+78.86%` | `216.50` |
| `Live` | `Short` | `7.87` | 66,210,000.00 USD | 2,980.00 USD | 0.00 USD | `+81.16%` | `378.70` |
| `Live` | `Short` | `7.92` | 66,220,000.00 USD | 12,000.00 USD | 0.00 USD | `+82.54%` | `1,514.20` |
| `Live` | `Short` | `7.95` | 66,230,000.00 USD | 6,120.00 USD | 0.00 USD | `+83.00%` | `769.80` |
| `Live` | `Short` | `7.99` | 66,230,000.00 USD | 399.25 USD | 0.00 USD | `+83.92%` | `50.00` |
| `Live` | `Short` | `8.03` | 66,660,000.00 USD | 435,580.00 USD | 0.00 USD | `+84.84%` | `54,278.30` |
| `Live` | `Short` | `8.07` | 66,670,000.00 USD | 6,460.00 USD | 0.00 USD | `+86.00%` | `800.00` |
| `Live` | `Short` | `8.09` | 66,770,000.00 USD | 97,280.00 USD | 0.00 USD | `+86.23%` | `12,032.20` |
| `Live` | `Short` | `8.20` | 66,770,000.00 USD | 951.44 USD | 0.00 USD | `+88.76%` | `116.10` |
| `Live` | `Short` | `8.29` | 66,770,000.00 USD | 165.07 USD | 0.00 USD | `+91.06%` | `19.90` |
| `Live` | `Short` | `8.34` | 66,870,000.00 USD | 96,080.00 USD | 0.00 USD | `+91.98%` | `11,527.10` |
| `Live` | `Short` | `8.35` | 66,890,000.00 USD | 25,310.00 USD | 0.00 USD | `+92.21%` | `3,032.60` |
| `Live` | `Short` | `8.38` | 66,890,000.00 USD | 191.79 USD | 0.00 USD | `+92.91%` | `22.90` |
| `Live` | `Short` | `8.43` | 66,890,000.00 USD | 1,220.00 USD | 0.00 USD | `+94.06%` | `145.00` |
| `Live` | `Short` | `8.44` | 66,900,000.00 USD | 8,770.00 USD | 0.00 USD | `+94.29%` | `1,039.60` |
| `Live` | `Short` | `8.47` | 66,900,000.00 USD | 816.99 USD | 0.00 USD | `+95.21%` | `96.40` |
| `Live` | `Short` | `8.48` | 66,910,000.00 USD | 6,640.00 USD | 0.00 USD | `+95.44%` | `782.50` |
| `Live` | `Short` | `8.49` | 66,930,000.00 USD | 25,490.00 USD | 0.00 USD | `+95.67%` | `3,000.00` |
| `Live` | `Short` | `8.52` | 66,950,000.00 USD | 17,500.00 USD | 0.00 USD | `+96.13%` | `2,054.80` |
| `Live` | `Short` | `8.53` | 66,990,000.00 USD | 34,680.00 USD | 0.00 USD | `+96.36%` | `4,068.00` |
| `Live` | `Short` | `8.54` | 66,990,000.00 USD | 127.17 USD | 0.00 USD | `+96.59%` | `14.90` |
| `Live` | `Short` | `8.54` | 66,990,000.00 USD | 124.76 USD | 0.00 USD | `+96.82%` | `14.60` |
| `Live` | `Short` | `8.59` | 67,420,000.00 USD | 432,220.00 USD | 0.00 USD | `+97.74%` | `50,346.40` |
| `Live` | `Short` | `8.60` | 67,420,000.00 USD | 240.66 USD | 0.00 USD | `+97.97%` | `28.00` |
| `Live` | `Short` | `8.61` | 67,470,000.00 USD | 54,210.00 USD | 0.00 USD | `+98.20%` | `6,300.00` |
| `Live` | `Short` | `8.62` | 67,480,000.00 USD | 4,950.00 USD | 0.00 USD | `+98.43%` | `574.10` |
| `Live` | `Short` | `8.68` | 67,480,000.00 USD | 2,320.00 USD | 0.00 USD | `+99.82%` | `267.10` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `1.00` | 3,170,000.00 USD | 0.00 USD | 585.51 USD | `-76.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.01` | 3,170,000.00 USD | 0.00 USD | 339.82 USD | `-76.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.20` | 3,170,000.00 USD | 0.00 USD | 196.58 USD | `-72.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.34` | 3,170,000.00 USD | 0.00 USD | 331.54 USD | `-69.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.35` | 3,170,000.00 USD | 0.00 USD | 345.25 USD | `-68.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.38` | 3,170,000.00 USD | 0.00 USD | 5,640.00 USD | `-68.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.40` | 3,160,000.00 USD | 0.00 USD | 997.29 USD | `-67.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.49` | 3,160,000.00 USD | 0.00 USD | 582.71 USD | `-65.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.51` | 3,160,000.00 USD | 0.00 USD | 139.83 USD | `-65.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.53` | 3,160,000.00 USD | 0.00 USD | 113.28 USD | `-64.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.54` | 3,160,000.00 USD | 0.00 USD | 4,000.00 USD | `-64.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.55` | 3,160,000.00 USD | 0.00 USD | 950.26 USD | `-64.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.59` | 3,150,000.00 USD | 0.00 USD | 4,590.00 USD | `-63.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.61` | 3,150,000.00 USD | 0.00 USD | 739.67 USD | `-62.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.62` | 3,150,000.00 USD | 0.00 USD | 1,740.00 USD | `-62.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.64` | 3,150,000.00 USD | 0.00 USD | 6,260.00 USD | `-62.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.66` | 3,140,000.00 USD | 0.00 USD | 345.40 USD | `-61.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.68` | 3,140,000.00 USD | 0.00 USD | 167.50 USD | `-61.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.70` | 3,140,000.00 USD | 0.00 USD | 669.02 USD | `-60.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.71` | 3,140,000.00 USD | 0.00 USD | 105.88 USD | `-60.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.73` | 3,140,000.00 USD | 0.00 USD | 172.50 USD | `-60.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.77` | 3,140,000.00 USD | 0.00 USD | 10,650.00 USD | `-59.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.80` | 3,130,000.00 USD | 0.00 USD | 722.00 USD | `-58.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.81` | 3,130,000.00 USD | 0.00 USD | 259.00 USD | `-58.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.82` | 3,130,000.00 USD | 0.00 USD | 103.84 USD | `-57.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.83` | 3,130,000.00 USD | 0.00 USD | 109.00 USD | `-57.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.88` | 3,130,000.00 USD | 0.00 USD | 222.19 USD | `-56.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.89` | 3,130,000.00 USD | 0.00 USD | 10,280.00 USD | `-56.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.91` | 3,120,000.00 USD | 0.00 USD | 558.36 USD | `-56.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.93` | 3,120,000.00 USD | 0.00 USD | 1,520.00 USD | `-55.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.94` | 3,120,000.00 USD | 0.00 USD | 222.14 USD | `-55.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.95` | 3,120,000.00 USD | 0.00 USD | 279.50 USD | `-55.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.98` | 3,120,000.00 USD | 0.00 USD | 197.50 USD | `-54.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.00` | 3,110,000.00 USD | 0.00 USD | 935.66 USD | `-54.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.00` | 3,110,000.00 USD | 0.00 USD | 18,860.00 USD | `-53.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.02` | 3,100,000.00 USD | 0.00 USD | 3,020.00 USD | `-53.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.04` | 3,090,000.00 USD | 0.00 USD | 214.52 USD | `-52.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.06` | 3,090,000.00 USD | 0.00 USD | 1,200.00 USD | `-52.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.06` | 3,090,000.00 USD | 0.00 USD | 578.41 USD | `-52.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.10` | 3,090,000.00 USD | 0.00 USD | 18,070.00 USD | `-51.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.10` | 3,070,000.00 USD | 0.00 USD | 108.62 USD | `-51.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.12` | 3,070,000.00 USD | 0.00 USD | 107.23 USD | `-51.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.12` | 3,070,000.00 USD | 0.00 USD | 1,590.00 USD | `-51.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.15` | 3,070,000.00 USD | 0.00 USD | 5,830.00 USD | `-50.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.15` | 3,060,000.00 USD | 0.00 USD | 310.32 USD | `-50.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.17` | 3,060,000.00 USD | 0.00 USD | 1,170.00 USD | `-50.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.19` | 3,060,000.00 USD | 0.00 USD | 576.18 USD | `-49.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.19` | 3,060,000.00 USD | 0.00 USD | 295.67 USD | `-49.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.21` | 3,060,000.00 USD | 0.00 USD | 1,430.00 USD | `-49.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.21` | 3,060,000.00 USD | 0.00 USD | 812.68 USD | `-48.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.23` | 3,060,000.00 USD | 0.00 USD | 1,440.00 USD | `-48.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.23` | 3,060,000.00 USD | 0.00 USD | 106.16 USD | `-48.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.25` | 3,060,000.00 USD | 0.00 USD | 6,270.00 USD | `-48.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.25` | 3,050,000.00 USD | 0.00 USD | 478.06 USD | `-48.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.27` | 3,050,000.00 USD | 0.00 USD | 540.88 USD | `-47.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.27` | 3,050,000.00 USD | 0.00 USD | 867.46 USD | `-47.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.29` | 3,050,000.00 USD | 0.00 USD | 759.76 USD | `-47.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.29` | 3,050,000.00 USD | 0.00 USD | 11,060.00 USD | `-47.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.31` | 3,040,000.00 USD | 0.00 USD | 3,690.00 USD | `-46.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.33` | 3,030,000.00 USD | 0.00 USD | 10,280.00 USD | `-46.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.33` | 3,020,000.00 USD | 0.00 USD | 467.00 USD | `-46.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.35` | 3,020,000.00 USD | 0.00 USD | 506.75 USD | `-45.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.37` | 3,020,000.00 USD | 0.00 USD | 214.27 USD | `-45.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.38` | 3,020,000.00 USD | 0.00 USD | 428.69 USD | `-45.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.38` | 3,020,000.00 USD | 0.00 USD | 322.45 USD | `-45.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.40` | 3,020,000.00 USD | 0.00 USD | 108.25 USD | `-44.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.40` | 3,020,000.00 USD | 0.00 USD | 3,900.00 USD | `-44.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.42` | 3,020,000.00 USD | 0.00 USD | 799.04 USD | `-44.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.44` | 3,020,000.00 USD | 0.00 USD | 6,830.00 USD | `-43.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.44` | 3,010,000.00 USD | 0.00 USD | 137.16 USD | `-43.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.48` | 3,010,000.00 USD | 0.00 USD | 504.41 USD | `-42.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.48` | 3,010,000.00 USD | 0.00 USD | 963.93 USD | `-42.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.50` | 3,010,000.00 USD | 0.00 USD | 6,690.00 USD | `-42.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.52` | 3,000,000.00 USD | 0.00 USD | 541.98 USD | `-42.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.54` | 3,000,000.00 USD | 0.00 USD | 108.75 USD | `-41.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.54` | 3,000,000.00 USD | 0.00 USD | 766.55 USD | `-41.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.56` | 3,000,000.00 USD | 0.00 USD | 7,110.00 USD | `-41.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.58` | 2,990,000.00 USD | 0.00 USD | 1,100.00 USD | `-40.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.58` | 2,990,000.00 USD | 0.00 USD | 100.04 USD | `-40.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.60` | 2,990,000.00 USD | 0.00 USD | 743.47 USD | `-40.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.62` | 2,990,000.00 USD | 0.00 USD | 5,090.00 USD | `-39.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.67` | 2,990,000.00 USD | 0.00 USD | 226.57 USD | `-38.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.69` | 2,990,000.00 USD | 0.00 USD | 104.98 USD | `-38.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.69` | 2,990,000.00 USD | 0.00 USD | 889.89 USD | `-37.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.71` | 2,990,000.00 USD | 0.00 USD | 7,270.00 USD | `-37.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.73` | 2,980,000.00 USD | 0.00 USD | 107.21 USD | `-37.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.75` | 2,980,000.00 USD | 0.00 USD | 197.37 USD | `-36.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.75` | 2,980,000.00 USD | 0.00 USD | 8,110.00 USD | `-36.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.77` | 2,970,000.00 USD | 0.00 USD | 108.39 USD | `-36.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.77` | 2,970,000.00 USD | 0.00 USD | 435.95 USD | `-36.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.79` | 2,970,000.00 USD | 0.00 USD | 217.23 USD | `-35.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.79` | 2,970,000.00 USD | 0.00 USD | 437.98 USD | `-35.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.81` | 2,970,000.00 USD | 0.00 USD | 1,230.00 USD | `-35.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.83` | 2,970,000.00 USD | 0.00 USD | 8,380.00 USD | `-34.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.83` | 2,960,000.00 USD | 0.00 USD | 283.50 USD | `-34.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.85` | 2,960,000.00 USD | 0.00 USD | 109.53 USD | `-34.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.85` | 2,960,000.00 USD | 0.00 USD | 1,230.00 USD | `-34.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.88` | 2,960,000.00 USD | 0.00 USD | 1,960.00 USD | `-33.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.88` | 2,960,000.00 USD | 0.00 USD | 157.81 USD | `-33.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.90` | 2,960,000.00 USD | 0.00 USD | 2,900.00 USD | `-33.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.90` | 2,950,000.00 USD | 0.00 USD | 4,870.00 USD | `-33.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.92` | 2,950,000.00 USD | 0.00 USD | 1,320.00 USD | `-32.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.92` | 2,950,000.00 USD | 0.00 USD | 493.15 USD | `-32.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.94` | 2,950,000.00 USD | 0.00 USD | 1,560.00 USD | `-32.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.94` | 2,940,000.00 USD | 0.00 USD | 24,200.00 USD | `-32.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.96` | 2,920,000.00 USD | 0.00 USD | 738.75 USD | `-31.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.96` | 2,920,000.00 USD | 0.00 USD | 523.32 USD | `-31.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.98` | 2,920,000.00 USD | 0.00 USD | 4,470.00 USD | `-31.48%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.00` | 2,910,000.00 USD | 0.00 USD | 12,170.00 USD | `-30.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.02` | 2,900,000.00 USD | 0.00 USD | 1,020.00 USD | `-30.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.04` | 2,900,000.00 USD | 0.00 USD | 214.57 USD | `-30.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.04` | 2,900,000.00 USD | 0.00 USD | 249.08 USD | `-29.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.06` | 2,900,000.00 USD | 0.00 USD | 305.50 USD | `-29.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.06` | 2,900,000.00 USD | 0.00 USD | 109.42 USD | `-29.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.10` | 2,900,000.00 USD | 0.00 USD | 9,300.00 USD | `-28.48%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.12` | 2,890,000.00 USD | 0.00 USD | 8,570.00 USD | `-28.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.12` | 2,880,000.00 USD | 0.00 USD | 104.69 USD | `-28.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.13` | 2,880,000.00 USD | 0.00 USD | 315.69 USD | `-27.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.15` | 2,880,000.00 USD | 0.00 USD | 214.17 USD | `-27.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.15` | 2,880,000.00 USD | 0.00 USD | 329.07 USD | `-27.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.17` | 2,880,000.00 USD | 0.00 USD | 4,210.00 USD | `-27.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.17` | 2,880,000.00 USD | 0.00 USD | 1,030.00 USD | `-26.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.19` | 2,880,000.00 USD | 0.00 USD | 218.81 USD | `-26.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.21` | 2,880,000.00 USD | 0.00 USD | 24,840.00 USD | `-26.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.21` | 2,850,000.00 USD | 0.00 USD | 144.67 USD | `-25.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.23` | 2,850,000.00 USD | 0.00 USD | 273,030.00 USD | `-25.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.25` | 2,580,000.00 USD | 0.00 USD | 27,380.00 USD | `-25.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.25` | 2,550,000.00 USD | 0.00 USD | 1,530.00 USD | `-25.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.27` | 2,550,000.00 USD | 0.00 USD | 104.81 USD | `-24.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.27` | 2,550,000.00 USD | 0.00 USD | 200.10 USD | `-24.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.29` | 2,550,000.00 USD | 0.00 USD | 1,480.00 USD | `-24.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.29` | 2,550,000.00 USD | 0.00 USD | 1,870.00 USD | `-24.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.31` | 2,550,000.00 USD | 0.00 USD | 11,460.00 USD | `-23.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.31` | 2,530,000.00 USD | 0.00 USD | 240.67 USD | `-23.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.33` | 2,530,000.00 USD | 0.00 USD | 306.56 USD | `-23.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.33` | 2,530,000.00 USD | 0.00 USD | 1,670.00 USD | `-23.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.37` | 2,530,000.00 USD | 0.00 USD | 73,220.00 USD | `-22.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.38` | 2,460,000.00 USD | 0.00 USD | 19,600.00 USD | `-22.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.40` | 2,440,000.00 USD | 0.00 USD | 8,490.00 USD | `-21.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.40` | 2,430,000.00 USD | 0.00 USD | 102,530.00 USD | `-21.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.42` | 2,330,000.00 USD | 0.00 USD | 421.41 USD | `-21.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.42` | 2,330,000.00 USD | 0.00 USD | 4,350.00 USD | `-21.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.44` | 2,320,000.00 USD | 0.00 USD | 444.49 USD | `-20.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.44` | 2,320,000.00 USD | 0.00 USD | 2,550.00 USD | `-20.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.46` | 2,320,000.00 USD | 0.00 USD | 1,380.00 USD | `-20.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.46` | 2,320,000.00 USD | 0.00 USD | 344.07 USD | `-20.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.48` | 2,320,000.00 USD | 0.00 USD | 24,320.00 USD | `-19.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.48` | 2,290,000.00 USD | 0.00 USD | 19,170.00 USD | `-19.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.50` | 2,270,000.00 USD | 0.00 USD | 894.72 USD | `-19.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.50` | 2,270,000.00 USD | 0.00 USD | 70,870.00 USD | `-19.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.52` | 2,200,000.00 USD | 0.00 USD | 24,110.00 USD | `-19.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.52` | 2,180,000.00 USD | 0.00 USD | 3,700.00 USD | `-18.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.54` | 2,180,000.00 USD | 0.00 USD | 16,250.00 USD | `-18.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.54` | 2,160,000.00 USD | 0.00 USD | 5,130.00 USD | `-18.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.56` | 2,150,000.00 USD | 0.00 USD | 1,800.00 USD | `-18.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.56` | 2,150,000.00 USD | 0.00 USD | 18,440.00 USD | `-17.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.58` | 2,130,000.00 USD | 0.00 USD | 77,480.00 USD | `-17.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.58` | 2,060,000.00 USD | 0.00 USD | 1,610.00 USD | `-17.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.60` | 2,050,000.00 USD | 0.00 USD | 331.46 USD | `-17.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.60` | 2,050,000.00 USD | 0.00 USD | 58,330.00 USD | `-16.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.62` | 2,000,000.00 USD | 0.00 USD | 632.99 USD | `-16.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.62` | 2,000,000.00 USD | 0.00 USD | 1,000.00 USD | `-16.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.63` | 1,990,000.00 USD | 0.00 USD | 1,210.00 USD | `-16.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.65` | 1,990,000.00 USD | 0.00 USD | 54,670.00 USD | `-16.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.65` | 1,940,000.00 USD | 0.00 USD | 4,080.00 USD | `-15.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.67` | 1,930,000.00 USD | 0.00 USD | 4,070.00 USD | `-15.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.67` | 1,930,000.00 USD | 0.00 USD | 367.50 USD | `-15.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.69` | 1,930,000.00 USD | 0.00 USD | 19,240.00 USD | `-15.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.69` | 1,910,000.00 USD | 0.00 USD | 4,370.00 USD | `-14.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.71` | 1,910,000.00 USD | 0.00 USD | 389,710.00 USD | `-14.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.71` | 1,520,000.00 USD | 0.00 USD | 6,300.00 USD | `-14.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.73` | 1,510,000.00 USD | 0.00 USD | 8,050.00 USD | `-14.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.73` | 1,500,000.00 USD | 0.00 USD | 32,040.00 USD | `-13.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.75` | 1,470,000.00 USD | 0.00 USD | 28,820.00 USD | `-13.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.75` | 1,440,000.00 USD | 0.00 USD | 14,490.00 USD | `-13.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.77` | 1,430,000.00 USD | 0.00 USD | 8,780.00 USD | `-13.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.77` | 1,420,000.00 USD | 0.00 USD | 1,190.00 USD | `-13.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.79` | 1,420,000.00 USD | 0.00 USD | 1,780.00 USD | `-12.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.79` | 1,420,000.00 USD | 0.00 USD | 166,450.00 USD | `-12.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.81` | 1,250,000.00 USD | 0.00 USD | 4,530.00 USD | `-12.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.81` | 1,240,000.00 USD | 0.00 USD | 21,180.00 USD | `-12.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.83` | 1,220,000.00 USD | 0.00 USD | 7,350.00 USD | `-11.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.83` | 1,220,000.00 USD | 0.00 USD | 41,340.00 USD | `-11.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.85` | 1,170,000.00 USD | 0.00 USD | 43,060.00 USD | `-11.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.85` | 1,130,000.00 USD | 0.00 USD | 5,890.00 USD | `-11.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.87` | 1,130,000.00 USD | 0.00 USD | 6,580.00 USD | `-10.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.88` | 1,120,000.00 USD | 0.00 USD | 161,230.00 USD | `-10.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.88` | 957,570.00 USD | 0.00 USD | 26,910.00 USD | `-10.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.90` | 930,660.00 USD | 0.00 USD | 8,970.00 USD | `-10.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.90` | 921,700.00 USD | 0.00 USD | 47,220.00 USD | `-10.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.92` | 874,480.00 USD | 0.00 USD | 1,310.00 USD | `-9.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.92` | 873,160.00 USD | 0.00 USD | 6,910.00 USD | `-9.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.94` | 866,260.00 USD | 0.00 USD | 934.17 USD | `-9.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.94` | 865,320.00 USD | 0.00 USD | 5,090.00 USD | `-9.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.96` | 860,230.00 USD | 0.00 USD | 396.29 USD | `-8.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.96` | 859,840.00 USD | 0.00 USD | 25,410.00 USD | `-8.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.98` | 834,420.00 USD | 0.00 USD | 317.60 USD | `-8.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.98` | 834,100.00 USD | 0.00 USD | 42,280.00 USD | `-8.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.00` | 791,820.00 USD | 0.00 USD | 667.16 USD | `-7.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.00` | 791,150.00 USD | 0.00 USD | 189,510.00 USD | `-7.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.01` | 601,650.00 USD | 0.00 USD | 350.51 USD | `-7.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.03` | 601,300.00 USD | 0.00 USD | 58,180.00 USD | `-7.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.04` | 543,120.00 USD | 0.00 USD | 428.11 USD | `-7.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.04` | 542,690.00 USD | 0.00 USD | 919.83 USD | `-6.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.05` | 541,770.00 USD | 0.00 USD | 34,070.00 USD | `-6.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.07` | 507,700.00 USD | 0.00 USD | 15,710.00 USD | `-6.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.08` | 491,990.00 USD | 0.00 USD | 5,760.00 USD | `-6.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.08` | 486,240.00 USD | 0.00 USD | 3,400.00 USD | `-5.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.09` | 482,830.00 USD | 0.00 USD | 13,580.00 USD | `-5.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.11` | 469,250.00 USD | 0.00 USD | 49,120.00 USD | `-5.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.12` | 420,120.00 USD | 0.00 USD | 65,790.00 USD | `-5.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.12` | 354,330.00 USD | 0.00 USD | 3,880.00 USD | `-4.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.13` | 350,450.00 USD | 0.00 USD | 31,590.00 USD | `-4.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.14` | 318,860.00 USD | 0.00 USD | 2,390.00 USD | `-4.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.16` | 316,470.00 USD | 0.00 USD | 69,250.00 USD | `-4.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.17` | 247,220.00 USD | 0.00 USD | 19,470.00 USD | `-4.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.17` | 227,750.00 USD | 0.00 USD | 8,530.00 USD | `-3.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.18` | 219,220.00 USD | 0.00 USD | 3,680.00 USD | `-3.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.20` | 215,540.00 USD | 0.00 USD | 1,680.00 USD | `-3.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.21` | 213,860.00 USD | 0.00 USD | 23,600.00 USD | `-3.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.21` | 190,270.00 USD | 0.00 USD | 14,410.00 USD | `-2.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.22` | 175,860.00 USD | 0.00 USD | 15,350.00 USD | `-2.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.24` | 160,500.00 USD | 0.00 USD | 63,060.00 USD | `-2.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.25` | 97,440.00 USD | 0.00 USD | 13,050.00 USD | `-2.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.25` | 84,390.00 USD | 0.00 USD | 20,990.00 USD | `-1.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.26` | 63,400.00 USD | 0.00 USD | 494.74 USD | `-1.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.28` | 62,910.00 USD | 0.00 USD | 2,220.00 USD | `-1.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.29` | 60,690.00 USD | 0.00 USD | 17,360.00 USD | `-1.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.29` | 43,330.00 USD | 0.00 USD | 282.18 USD | `-1.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.30` | 43,050.00 USD | 0.00 USD | 1,910.00 USD | `-0.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.32` | 41,140.00 USD | 0.00 USD | 39,760.00 USD | `-0.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.33` | 1,380.00 USD | 0.00 USD | 182.52 USD | `-0.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.33` | 1,190.00 USD | 0.00 USD | 1,190.00 USD | `-0.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.34` | 17,380.00 USD | 17,380.00 USD | 0.00 USD | `+0.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.36` | 32,790.00 USD | 15,410.00 USD | 0.00 USD | `+0.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.37` | 193,810.00 USD | 161,010.00 USD | 0.00 USD | `+0.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.38` | 283,440.00 USD | 89,630.00 USD | 0.00 USD | `+0.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.38` | 285,170.00 USD | 1,730.00 USD | 0.00 USD | `+1.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.39` | 477,520.00 USD | 192,350.00 USD | 0.00 USD | `+1.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.41` | 521,670.00 USD | 44,150.00 USD | 0.00 USD | `+1.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.42` | 525,340.00 USD | 3,670.00 USD | 0.00 USD | `+1.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.42` | 541,720.00 USD | 16,370.00 USD | 0.00 USD | `+1.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.43` | 592,020.00 USD | 50,300.00 USD | 0.00 USD | `+2.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.45` | 601,300.00 USD | 9,280.00 USD | 0.00 USD | `+2.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.46` | 642,620.00 USD | 41,330.00 USD | 0.00 USD | `+2.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.46` | 646,030.00 USD | 3,410.00 USD | 0.00 USD | `+2.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.47` | 646,530.00 USD | 498.51 USD | 0.00 USD | `+3.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.49` | 647,840.00 USD | 1,310.00 USD | 0.00 USD | `+3.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.50` | 663,800.00 USD | 15,960.00 USD | 0.00 USD | `+3.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.50` | 708,030.00 USD | 44,220.00 USD | 0.00 USD | `+3.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.51` | 726,960.00 USD | 18,940.00 USD | 0.00 USD | `+4.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.53` | 833,980.00 USD | 107,010.00 USD | 0.00 USD | `+4.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.54` | 854,450.00 USD | 20,470.00 USD | 0.00 USD | `+4.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.54` | 854,760.00 USD | 312.24 USD | 0.00 USD | `+4.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.55` | 855,150.00 USD | 392.64 USD | 0.00 USD | `+4.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.57` | 855,540.00 USD | 388.48 USD | 0.00 USD | `+5.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.58` | 859,820.00 USD | 4,280.00 USD | 0.00 USD | `+5.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.58` | 860,580.00 USD | 759.73 USD | 0.00 USD | `+5.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.59` | 860,950.00 USD | 364.84 USD | 0.00 USD | `+5.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.61` | 979,650.00 USD | 118,700.00 USD | 0.00 USD | `+6.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.62` | 980,390.00 USD | 742.55 USD | 0.00 USD | `+6.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.62` | 1,000,000.00 USD | 21,860.00 USD | 0.00 USD | `+6.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.63` | 2,010,000.00 USD | 1,010,000.00 USD | 0.00 USD | `+6.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.64` | 2,010,000.00 USD | 4,070.00 USD | 0.00 USD | `+6.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.66` | 2,020,000.00 USD | 1,240.00 USD | 0.00 USD | `+7.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.67` | 2,090,000.00 USD | 77,690.00 USD | 0.00 USD | `+7.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.67` | 2,100,000.00 USD | 3,030.00 USD | 0.00 USD | `+7.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.68` | 2,100,000.00 USD | 914.98 USD | 0.00 USD | `+7.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.70` | 2,100,000.00 USD | 152.12 USD | 0.00 USD | `+8.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.71` | 2,500,000.00 USD | 397,590.00 USD | 0.00 USD | `+8.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.71` | 2,730,000.00 USD | 235,990.00 USD | 0.00 USD | `+8.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.72` | 2,730,000.00 USD | 2,650.00 USD | 0.00 USD | `+8.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.74` | 2,820,000.00 USD | 84,970.00 USD | 0.00 USD | `+9.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.75` | 2,870,000.00 USD | 49,950.00 USD | 0.00 USD | `+9.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.75` | 2,900,000.00 USD | 29,420.00 USD | 0.00 USD | `+9.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.76` | 2,910,000.00 USD | 13,030.00 USD | 0.00 USD | `+9.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.78` | 2,910,000.00 USD | 2,640.00 USD | 0.00 USD | `+9.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.79` | 2,910,000.00 USD | 314.37 USD | 0.00 USD | `+10.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.79` | 2,940,000.00 USD | 22,590.00 USD | 0.00 USD | `+10.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.80` | 3,110,000.00 USD | 176,250.00 USD | 0.00 USD | `+10.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.82` | 3,140,000.00 USD | 30,560.00 USD | 0.00 USD | `+10.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.83` | 3,150,000.00 USD | 8,540.00 USD | 0.00 USD | `+11.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.83` | 3,250,000.00 USD | 93,590.00 USD | 0.00 USD | `+11.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.84` | 3,290,000.00 USD | 40,760.00 USD | 0.00 USD | `+11.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.86` | 3,310,000.00 USD | 27,630.00 USD | 0.00 USD | `+11.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.87` | 3,340,000.00 USD | 23,180.00 USD | 0.00 USD | `+12.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.88` | 3,350,000.00 USD | 10,400.00 USD | 0.00 USD | `+12.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.88` | 3,370,000.00 USD | 19,890.00 USD | 0.00 USD | `+12.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.89` | 3,370,000.00 USD | 4,060.00 USD | 0.00 USD | `+12.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.91` | 3,480,000.00 USD | 111,630.00 USD | 0.00 USD | `+12.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.92` | 3,480,000.00 USD | 156.30 USD | 0.00 USD | `+13.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.92` | 3,500,000.00 USD | 13,180.00 USD | 0.00 USD | `+13.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.93` | 3,500,000.00 USD | 4,420.00 USD | 0.00 USD | `+13.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.95` | 3,500,000.00 USD | 313.51 USD | 0.00 USD | `+13.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.96` | 3,510,000.00 USD | 7,900.00 USD | 0.00 USD | `+14.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.96` | 3,560,000.00 USD | 47,350.00 USD | 0.00 USD | `+14.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.97` | 3,560,000.00 USD | 187.06 USD | 0.00 USD | `+14.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.99` | 3,650,000.00 USD | 92,570.00 USD | 0.00 USD | `+14.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.00` | 3,650,000.00 USD | 2,540.00 USD | 0.00 USD | `+15.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.00` | 3,710,000.00 USD | 63,070.00 USD | 0.00 USD | `+15.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.01` | 3,740,000.00 USD | 25,080.00 USD | 0.00 USD | `+15.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.03` | 3,740,000.00 USD | 5,030.00 USD | 0.00 USD | `+15.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.04` | 3,760,000.00 USD | 19,640.00 USD | 0.00 USD | `+15.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.04` | 3,760,000.00 USD | 120.58 USD | 0.00 USD | `+16.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.05` | 3,780,000.00 USD | 14,090.00 USD | 0.00 USD | `+16.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.07` | 3,780,000.00 USD | 5,860.00 USD | 0.00 USD | `+16.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.08` | 3,870,000.00 USD | 87,450.00 USD | 0.00 USD | `+16.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.08` | 3,880,000.00 USD | 5,460.00 USD | 0.00 USD | `+17.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.09` | 3,880,000.00 USD | 178.33 USD | 0.00 USD | `+17.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.11` | 3,950,000.00 USD | 70,250.00 USD | 0.00 USD | `+17.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.12` | 3,960,000.00 USD | 15,350.00 USD | 0.00 USD | `+17.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.12` | 3,960,000.00 USD | 179.38 USD | 0.00 USD | `+18.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.13` | 3,960,000.00 USD | 179.72 USD | 0.00 USD | `+18.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.14` | 3,960,000.00 USD | 217.63 USD | 0.00 USD | `+18.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.16` | 3,960,000.00 USD | 493.85 USD | 0.00 USD | `+18.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.17` | 3,960,000.00 USD | 575.38 USD | 0.00 USD | `+18.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.17` | 3,970,000.00 USD | 327.58 USD | 0.00 USD | `+19.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.18` | 3,970,000.00 USD | 163.85 USD | 0.00 USD | `+19.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.20` | 4,090,000.00 USD | 120,930.00 USD | 0.00 USD | `+19.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.21` | 4,120,000.00 USD | 38,230.00 USD | 0.00 USD | `+19.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.21` | 4,130,000.00 USD | 1,710.00 USD | 0.00 USD | `+20.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.22` | 4,130,000.00 USD | 432.63 USD | 0.00 USD | `+20.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.24` | 4,130,000.00 USD | 2,620.00 USD | 0.00 USD | `+20.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.25` | 4,130,000.00 USD | 537.61 USD | 0.00 USD | `+20.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.25` | 4,550,000.00 USD | 420,400.00 USD | 0.00 USD | `+21.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.26` | 4,550,000.00 USD | 278.52 USD | 0.00 USD | `+21.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.28` | 4,550,000.00 USD | 589.22 USD | 0.00 USD | `+21.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.29` | 4,550,000.00 USD | 733.03 USD | 0.00 USD | `+21.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.29` | 4,550,000.00 USD | 423.60 USD | 0.00 USD | `+21.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.30` | 4,560,000.00 USD | 12,620.00 USD | 0.00 USD | `+22.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.32` | 4,570,000.00 USD | 381.09 USD | 0.00 USD | `+22.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.33` | 4,570,000.00 USD | 961.16 USD | 0.00 USD | `+22.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.33` | 4,570,000.00 USD | 1,570.00 USD | 0.00 USD | `+22.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.34` | 4,570,000.00 USD | 5,650.00 USD | 0.00 USD | `+23.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.36` | 4,570,000.00 USD | 160.11 USD | 0.00 USD | `+23.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.37` | 4,570,000.00 USD | 225.33 USD | 0.00 USD | `+23.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.38` | 4,570,000.00 USD | 438.60 USD | 0.00 USD | `+23.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.38` | 4,580,000.00 USD | 6,610.00 USD | 0.00 USD | `+24.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.39` | 4,620,000.00 USD | 40,880.00 USD | 0.00 USD | `+24.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.41` | 4,640,000.00 USD | 21,220.00 USD | 0.00 USD | `+24.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.42` | 4,650,000.00 USD | 4,330.00 USD | 0.00 USD | `+24.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.42` | 4,650,000.00 USD | 639.61 USD | 0.00 USD | `+24.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.43` | 4,650,000.00 USD | 1,710.00 USD | 0.00 USD | `+25.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.45` | 4,660,000.00 USD | 13,690.00 USD | 0.00 USD | `+25.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.46` | 4,660,000.00 USD | 1,020.00 USD | 0.00 USD | `+25.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.46` | 4,750,000.00 USD | 87,720.00 USD | 0.00 USD | `+25.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.47` | 4,780,000.00 USD | 30,110.00 USD | 0.00 USD | `+26.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.49` | 4,780,000.00 USD | 863.89 USD | 0.00 USD | `+26.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.50` | 4,780,000.00 USD | 1,040.00 USD | 0.00 USD | `+26.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.50` | 5,760,000.00 USD | 972,790.00 USD | 0.00 USD | `+26.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.51` | 5,760,000.00 USD | 5,600.00 USD | 0.00 USD | `+27.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.53` | 5,780,000.00 USD | 19,110.00 USD | 0.00 USD | `+27.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.54` | 5,800,000.00 USD | 18,790.00 USD | 0.00 USD | `+27.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.54` | 5,860,000.00 USD | 58,030.00 USD | 0.00 USD | `+27.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.55` | 5,900,000.00 USD | 46,110.00 USD | 0.00 USD | `+27.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.57` | 5,920,000.00 USD | 14,320.00 USD | 0.00 USD | `+28.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.58` | 5,930,000.00 USD | 11,740.00 USD | 0.00 USD | `+28.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.58` | 5,950,000.00 USD | 23,650.00 USD | 0.00 USD | `+28.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.59` | 5,950,000.00 USD | 384.94 USD | 0.00 USD | `+28.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.61` | 5,960,000.00 USD | 1,300.00 USD | 0.00 USD | `+29.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.62` | 5,960,000.00 USD | 347.06 USD | 0.00 USD | `+29.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.63` | 5,960,000.00 USD | 347.68 USD | 0.00 USD | `+29.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.64` | 5,960,000.00 USD | 491.11 USD | 0.00 USD | `+30.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.66` | 5,960,000.00 USD | 3,290.00 USD | 0.00 USD | `+30.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.67` | 5,960,000.00 USD | 281.55 USD | 0.00 USD | `+30.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.67` | 5,970,000.00 USD | 6,590.00 USD | 0.00 USD | `+30.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.68` | 5,970,000.00 USD | 235.93 USD | 0.00 USD | `+30.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.70` | 5,970,000.00 USD | 5,860.00 USD | 0.00 USD | `+31.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.71` | 6,080,000.00 USD | 103,820.00 USD | 0.00 USD | `+31.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.71` | 6,080,000.00 USD | 705.23 USD | 0.00 USD | `+31.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.72` | 6,080,000.00 USD | 5,720.00 USD | 0.00 USD | `+31.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.75` | 6,080,000.00 USD | 139.03 USD | 0.00 USD | `+32.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.75` | 6,090,000.00 USD | 2,480.00 USD | 0.00 USD | `+32.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.78` | 6,090,000.00 USD | 1,850.00 USD | 0.00 USD | `+33.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.79` | 6,090,000.00 USD | 286.94 USD | 0.00 USD | `+33.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.80` | 6,100,000.00 USD | 7,120.00 USD | 0.00 USD | `+33.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.82` | 6,100,000.00 USD | 329.13 USD | 0.00 USD | `+33.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.83` | 6,100,000.00 USD | 1,970.00 USD | 0.00 USD | `+34.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.83` | 6,100,000.00 USD | 1,020.00 USD | 0.00 USD | `+34.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.84` | 6,100,000.00 USD | 2,720.00 USD | 0.00 USD | `+34.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.86` | 6,100,000.00 USD | 1,190.00 USD | 0.00 USD | `+34.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.87` | 6,100,000.00 USD | 1,770.00 USD | 0.00 USD | `+35.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.88` | 6,110,000.00 USD | 3,450.00 USD | 0.00 USD | `+35.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.88` | 6,110,000.00 USD | 345.45 USD | 0.00 USD | `+35.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.91` | 6,130,000.00 USD | 23,750.00 USD | 0.00 USD | `+36.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.92` | 6,130,000.00 USD | 1,670.00 USD | 0.00 USD | `+36.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.92` | 6,130,000.00 USD | 1,020.00 USD | 0.00 USD | `+36.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.93` | 6,290,000.00 USD | 153,150.00 USD | 0.00 USD | `+36.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.96` | 6,310,000.00 USD | 26,180.00 USD | 0.00 USD | `+37.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.96` | 6,320,000.00 USD | 5,440.00 USD | 0.00 USD | `+37.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.97` | 6,330,000.00 USD | 8,940.00 USD | 0.00 USD | `+37.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.99` | 6,450,000.00 USD | 119,340.00 USD | 0.00 USD | `+37.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.00` | 6,450,000.00 USD | 3,000.00 USD | 0.00 USD | `+38.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.00` | 6,650,000.00 USD | 197,080.00 USD | 0.00 USD | `+38.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.01` | 6,660,000.00 USD | 13,710.00 USD | 0.00 USD | `+38.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.03` | 6,750,000.00 USD | 90,380.00 USD | 0.00 USD | `+38.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.04` | 6,750,000.00 USD | 2,050.00 USD | 0.00 USD | `+39.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.04` | 6,760,000.00 USD | 3,300.00 USD | 0.00 USD | `+39.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.05` | 6,760,000.00 USD | 1,040.00 USD | 0.00 USD | `+39.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.07` | 6,760,000.00 USD | 425.76 USD | 0.00 USD | `+39.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.08` | 6,760,000.00 USD | 4,120.00 USD | 0.00 USD | `+40.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.11` | 6,820,000.00 USD | 61,050.00 USD | 0.00 USD | `+40.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.12` | 6,830,000.00 USD | 1,610.00 USD | 0.00 USD | `+40.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.13` | 6,830,000.00 USD | 1,200.00 USD | 0.00 USD | `+41.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.14` | 6,830,000.00 USD | 420.32 USD | 0.00 USD | `+41.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.16` | 6,830,000.00 USD | 1,940.00 USD | 0.00 USD | `+41.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.17` | 6,830,000.00 USD | 4,010.00 USD | 0.00 USD | `+42.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.21` | 6,900,000.00 USD | 66,060.00 USD | 0.00 USD | `+42.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.21` | 6,900,000.00 USD | 1,890.00 USD | 0.00 USD | `+43.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.22` | 6,900,000.00 USD | 195.46 USD | 0.00 USD | `+43.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.24` | 6,900,000.00 USD | 289.93 USD | 0.00 USD | `+43.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.25` | 6,900,000.00 USD | 116.16 USD | 0.00 USD | `+43.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.30` | 6,910,000.00 USD | 7,310.00 USD | 0.00 USD | `+45.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.32` | 6,910,000.00 USD | 310.70 USD | 0.00 USD | `+45.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.33` | 6,910,000.00 USD | 325.62 USD | 0.00 USD | `+45.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.36` | 6,910,000.00 USD | 1,760.00 USD | 0.00 USD | `+46.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.39` | 6,910,000.00 USD | 3,230.00 USD | 0.00 USD | `+47.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.41` | 6,920,000.00 USD | 5,120.00 USD | 0.00 USD | `+47.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.50` | 6,920,000.00 USD | 1,310.00 USD | 0.00 USD | `+49.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.50` | 6,950,000.00 USD | 30,990.00 USD | 0.00 USD | `+49.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.51` | 6,950,000.00 USD | 611.11 USD | 0.00 USD | `+50.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.54` | 6,970,000.00 USD | 13,580.00 USD | 0.00 USD | `+50.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.58` | 6,970,000.00 USD | 1,630.00 USD | 0.00 USD | `+51.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.59` | 6,970,000.00 USD | 1,370.00 USD | 0.00 USD | `+51.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.61` | 6,970,000.00 USD | 5,400.00 USD | 0.00 USD | `+52.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.62` | 6,980,000.00 USD | 1,620.00 USD | 0.00 USD | `+52.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.67` | 6,980,000.00 USD | 450.55 USD | 0.00 USD | `+53.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.67` | 6,980,000.00 USD | 3,060.00 USD | 0.00 USD | `+53.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.71` | 6,980,000.00 USD | 3,070.00 USD | 0.00 USD | `+54.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.75` | 6,980,000.00 USD | 1,550.00 USD | 0.00 USD | `+55.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.79` | 6,990,000.00 USD | 647.56 USD | 0.00 USD | `+56.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.80` | 6,990,000.00 USD | 1,420.00 USD | 0.00 USD | `+56.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.82` | 6,990,000.00 USD | 2,130.00 USD | 0.00 USD | `+56.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.83` | 7,000,000.00 USD | 6,870.00 USD | 0.00 USD | `+57.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.84` | 7,000,000.00 USD | 342.25 USD | 0.00 USD | `+57.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.87` | 7,000,000.00 USD | 2,990.00 USD | 0.00 USD | `+58.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.89` | 7,000,000.00 USD | 2,970.00 USD | 0.00 USD | `+58.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.91` | 7,000,000.00 USD | 324.54 USD | 0.00 USD | `+59.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.95` | 7,000,000.00 USD | 504.21 USD | 0.00 USD | `+59.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.97` | 7,000,000.00 USD | 166.00 USD | 0.00 USD | `+60.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.99` | 7,010,000.00 USD | 4,190.00 USD | 0.00 USD | `+60.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.00` | 7,020,000.00 USD | 13,480.00 USD | 0.00 USD | `+61.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.04` | 7,020,000.00 USD | 2,860.00 USD | 0.00 USD | `+62.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.11` | 7,020,000.00 USD | 264.31 USD | 0.00 USD | `+63.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.13` | 7,020,000.00 USD | 599.34 USD | 0.00 USD | `+64.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.16` | 7,020,000.00 USD | 193.19 USD | 0.00 USD | `+64.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.18` | 7,030,000.00 USD | 3,950.00 USD | 0.00 USD | `+65.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.21` | 7,030,000.00 USD | 1,940.00 USD | 0.00 USD | `+66.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.25` | 7,190,000.00 USD | 160,550.00 USD | 0.00 USD | `+66.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.28` | 7,190,000.00 USD | 1,290.00 USD | 0.00 USD | `+67.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.32` | 7,190,000.00 USD | 1,180.00 USD | 0.00 USD | `+68.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.39` | 7,190,000.00 USD | 630.05 USD | 0.00 USD | `+70.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.41` | 7,200,000.00 USD | 1,410.00 USD | 0.00 USD | `+70.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.42` | 7,200,000.00 USD | 2,610.00 USD | 0.00 USD | `+70.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.50` | 7,210,000.00 USD | 7,630.00 USD | 0.00 USD | `+72.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.58` | 7,210,000.00 USD | 4,640.00 USD | 0.00 USD | `+74.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.61` | 7,210,000.00 USD | 371.88 USD | 0.00 USD | `+75.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.62` | 7,210,000.00 USD | 2,510.00 USD | 0.00 USD | `+75.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.67` | 7,210,000.00 USD | 380.68 USD | 0.00 USD | `+76.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.79` | 7,220,000.00 USD | 11,170.00 USD | 0.00 USD | `+79.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.80` | 7,260,000.00 USD | 34,360.00 USD | 0.00 USD | `+79.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.82` | 7,260,000.00 USD | 253.21 USD | 0.00 USD | `+80.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.83` | 7,260,000.00 USD | 100.29 USD | 0.00 USD | `+80.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.96` | 7,270,000.00 USD | 10,610.00 USD | 0.00 USD | `+83.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.97` | 7,270,000.00 USD | 309.43 USD | 0.00 USD | `+83.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.99` | 7,270,000.00 USD | 4,640.00 USD | 0.00 USD | `+83.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.01` | 7,310,000.00 USD | 36,740.00 USD | 0.00 USD | `+84.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.03` | 7,390,000.00 USD | 81,310.00 USD | 0.00 USD | `+84.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.15` | 7,400,000.00 USD | 2,150.00 USD | 0.00 USD | `+87.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.19` | 7,400,000.00 USD | 216.90 USD | 0.00 USD | `+88.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.20` | 7,400,000.00 USD | 1,990.00 USD | 0.00 USD | `+88.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.21` | 7,400,000.00 USD | 7,200.00 USD | 0.00 USD | `+88.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.38` | 7,410,000.00 USD | 998.65 USD | 0.00 USD | `+93.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.39` | 7,410,000.00 USD | 1,260.00 USD | 0.00 USD | `+93.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.40` | 7,510,000.00 USD | 103,010.00 USD | 0.00 USD | `+93.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.46` | 7,510,000.00 USD | 721.22 USD | 0.00 USD | `+94.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.51` | 7,520,000.00 USD | 5,130.00 USD | 0.00 USD | `+95.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.61` | 7,520,000.00 USD | 2,010.00 USD | 0.00 USD | `+98.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.65` | 7,520,000.00 USD | 198.20 USD | 0.00 USD | `+99.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.66` | 7,520,000.00 USD | 3,670.00 USD | 0.00 USD | `+99.59%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `3.48` | 18,510,000.00 USD | 0.00 USD | 18,510,000.00 USD | 45,650.00 USD | 26,250.00 USD | 1,510.00 USD |
| `7D` | `3.50` | 18,440,000.00 USD | 0.00 USD | 18,440,000.00 USD | 16,960.00 USD | 6,940.00 USD | 38,050.00 USD |
| `7D` | `3.51` | 18,380,000.00 USD | 0.00 USD | 18,380,000.00 USD | 3,690.00 USD | 0.00 USD | 231.64 USD |
| `7D` | `3.52` | 18,370,000.00 USD | 0.00 USD | 18,370,000.00 USD | 15,180.00 USD | 0.00 USD | 41,090.00 USD |
| `7D` | `3.53` | 18,320,000.00 USD | 0.00 USD | 18,320,000.00 USD | 93,360.00 USD | 40,470.00 USD | 96,140.00 USD |
| `7D` | `3.54` | 18,090,000.00 USD | 0.00 USD | 18,090,000.00 USD | 3,040.00 USD | 58,300.00 USD | 30,480.00 USD |
| `7D` | `3.55` | 17,990,000.00 USD | 0.00 USD | 17,990,000.00 USD | 128,490.00 USD | 54,880.00 USD | 45,330.00 USD |
| `7D` | `3.56` | 17,770,000.00 USD | 0.00 USD | 17,770,000.00 USD | 61,170.00 USD | 0.00 USD | 32.49 USD |
| `7D` | `3.57` | 17,700,000.00 USD | 0.00 USD | 17,700,000.00 USD | 86,360.00 USD | 27,910.00 USD | 84,270.00 USD |
| `7D` | `3.58` | 17,510,000.00 USD | 0.00 USD | 17,510,000.00 USD | 173,980.00 USD | 48,640.00 USD | 59,950.00 USD |
| `7D` | `3.59` | 17,220,000.00 USD | 0.00 USD | 17,220,000.00 USD | 535.75 USD | 18,170.00 USD | 78.80 USD |
| `7D` | `3.60` | 17,200,000.00 USD | 0.00 USD | 17,200,000.00 USD | 64,170.00 USD | 21,460.00 USD | 22,050.00 USD |
| `7D` | `3.61` | 17,100,000.00 USD | 0.00 USD | 17,100,000.00 USD | 56,580.00 USD | 37,060.00 USD | 44,890.00 USD |
| `7D` | `3.62` | 16,960,000.00 USD | 0.00 USD | 16,960,000.00 USD | 92,130.00 USD | 26,640.00 USD | 97,570.00 USD |
| `7D` | `3.63` | 16,740,000.00 USD | 0.00 USD | 16,740,000.00 USD | 50,840.00 USD | 8,120.00 USD | 159.02 USD |
| `7D` | `3.64` | 16,680,000.00 USD | 0.00 USD | 16,680,000.00 USD | 2,410.00 USD | 41,960.00 USD | 119,140.00 USD |
| `7D` | `3.65` | 16,520,000.00 USD | 0.00 USD | 16,520,000.00 USD | 53,900.00 USD | 7,050.00 USD | 31,190.00 USD |
| `7D` | `3.66` | 16,430,000.00 USD | 0.00 USD | 16,430,000.00 USD | 32,350.00 USD | 15,090.00 USD | 125,270.00 USD |
| `7D` | `3.67` | 16,250,000.00 USD | 0.00 USD | 16,250,000.00 USD | 52,020.00 USD | 14,480.00 USD | 53,670.00 USD |
| `7D` | `3.68` | 16,130,000.00 USD | 0.00 USD | 16,130,000.00 USD | 1,010.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `3.69` | 16,130,000.00 USD | 0.00 USD | 16,130,000.00 USD | 27,750.00 USD | 0.00 USD | 59,840.00 USD |
| `7D` | `3.70` | 16,050,000.00 USD | 0.00 USD | 16,050,000.00 USD | 20,470.00 USD | 7,370.00 USD | 112,470.00 USD |
| `7D` | `3.71` | 15,900,000.00 USD | 0.00 USD | 15,900,000.00 USD | 51,960.00 USD | 0.00 USD | 74,330.00 USD |
| `7D` | `3.72` | 15,780,000.00 USD | 0.00 USD | 15,780,000.00 USD | 425.03 USD | 0.00 USD | 183.06 USD |
| `7D` | `3.73` | 15,780,000.00 USD | 0.00 USD | 15,780,000.00 USD | 41,940.00 USD | 10,880.00 USD | 56,790.00 USD |
| `7D` | `3.74` | 15,670,000.00 USD | 0.00 USD | 15,670,000.00 USD | 130,620.00 USD | 40,020.00 USD | 122,480.00 USD |
| `7D` | `3.75` | 15,380,000.00 USD | 0.00 USD | 15,380,000.00 USD | 3,890.00 USD | 51,780.00 USD | 129,350.00 USD |
| `7D` | `3.76` | 15,190,000.00 USD | 0.00 USD | 15,190,000.00 USD | 32,650.00 USD | 10,110.00 USD | 22,610.00 USD |
| `7D` | `3.77` | 15,120,000.00 USD | 0.00 USD | 15,120,000.00 USD | 15,340.00 USD | 8,090.00 USD | 23,020.00 USD |
| `7D` | `3.78` | 15,080,000.00 USD | 0.00 USD | 15,080,000.00 USD | 24,180.00 USD | 93,830.00 USD | 41,570.00 USD |
| `7D` | `3.79` | 14,920,000.00 USD | 0.00 USD | 14,920,000.00 USD | 51,640.00 USD | 0.00 USD | 137,710.00 USD |
| `7D` | `3.80` | 14,730,000.00 USD | 0.00 USD | 14,730,000.00 USD | 8,210.00 USD | 34,570.00 USD | 17,840.00 USD |
| `7D` | `3.81` | 14,670,000.00 USD | 0.00 USD | 14,670,000.00 USD | 5,310.00 USD | 0.00 USD | 1,430.00 USD |
| `7D` | `3.82` | 14,660,000.00 USD | 0.00 USD | 14,660,000.00 USD | 5,630.00 USD | 18,370.00 USD | 25,600.00 USD |
| `7D` | `3.83` | 14,610,000.00 USD | 0.00 USD | 14,610,000.00 USD | 50,540.00 USD | 50,500.00 USD | 153.98 USD |
| `1D` | `3.84` | 17,600,000.00 USD | 0.00 USD | 17,600,000.00 USD | 275,920.00 USD | 171,520.00 USD | 179,530.00 USD |
| `7D` | `3.84` | 14,510,000.00 USD | 0.00 USD | 14,510,000.00 USD | 7,940.00 USD | 33,350.00 USD | 146.37 USD |
| `1D` | `3.85` | 16,970,000.00 USD | 0.00 USD | 16,970,000.00 USD | 186,230.00 USD | 175,470.00 USD | 37,740.00 USD |
| `7D` | `3.85` | 14,470,000.00 USD | 0.00 USD | 14,470,000.00 USD | 3,390.00 USD | 49,170.00 USD | 84,260.00 USD |
| `1D` | `3.86` | 16,570,000.00 USD | 0.00 USD | 16,570,000.00 USD | 39,130.00 USD | 39,050.00 USD | 52,990.00 USD |
| `7D` | `3.86` | 14,330,000.00 USD | 0.00 USD | 14,330,000.00 USD | 5,190.00 USD | 173,980.00 USD | 39,790.00 USD |
| `1D` | `3.87` | 16,440,000.00 USD | 0.00 USD | 16,440,000.00 USD | 53,480.00 USD | 58,230.00 USD | 188,360.00 USD |
| `7D` | `3.87` | 14,110,000.00 USD | 0.00 USD | 14,110,000.00 USD | 62,650.00 USD | 0.00 USD | 197,600.00 USD |
| `1D` | `3.88` | 16,140,000.00 USD | 0.00 USD | 16,140,000.00 USD | 35,520.00 USD | 26,560.00 USD | 224,940.00 USD |
| `7D` | `3.88` | 13,850,000.00 USD | 0.00 USD | 13,850,000.00 USD | 110,160.00 USD | 86,900.00 USD | 156,790.00 USD |
| `1D` | `3.89` | 15,860,000.00 USD | 0.00 USD | 15,860,000.00 USD | 396,980.00 USD | 100,370.00 USD | 258,260.00 USD |
| `7D` | `3.89` | 13,500,000.00 USD | 0.00 USD | 13,500,000.00 USD | 4,240.00 USD | 50,710.00 USD | 83,380.00 USD |
| `1D` | `3.90` | 15,100,000.00 USD | 0.00 USD | 15,100,000.00 USD | 33,360.00 USD | 49,080.00 USD | 223,320.00 USD |
| `7D` | `3.90` | 13,360,000.00 USD | 0.00 USD | 13,360,000.00 USD | 274,050.00 USD | 28,250.00 USD | 51,510.00 USD |
| `1D` | `3.91` | 14,790,000.00 USD | 0.00 USD | 14,790,000.00 USD | 351,900.00 USD | 120,100.00 USD | 276,080.00 USD |
| `7D` | `3.91` | 13,010,000.00 USD | 0.00 USD | 13,010,000.00 USD | 122,540.00 USD | 67,260.00 USD | 46,930.00 USD |
| `1D` | `3.92` | 14,050,000.00 USD | 0.00 USD | 14,050,000.00 USD | 318,260.00 USD | 13,670.00 USD | 124,180.00 USD |
| `7D` | `3.92` | 12,770,000.00 USD | 0.00 USD | 12,770,000.00 USD | 85,790.00 USD | 66,710.00 USD | 105,000.00 USD |
| `1D` | `3.93` | 13,590,000.00 USD | 0.00 USD | 13,590,000.00 USD | 116,350.00 USD | 99,220.00 USD | 97,360.00 USD |
| `7D` | `3.93` | 12,510,000.00 USD | 0.00 USD | 12,510,000.00 USD | 0.00 USD | 28,720.00 USD | 67.04 USD |
| `1D` | `3.94` | 13,280,000.00 USD | 0.00 USD | 13,280,000.00 USD | 144,900.00 USD | 53,060.00 USD | 137,210.00 USD |
| `7D` | `3.94` | 12,480,000.00 USD | 0.00 USD | 12,480,000.00 USD | 55,330.00 USD | 0.00 USD | 2,250.00 USD |
| `1D` | `3.95` | 12,940,000.00 USD | 0.00 USD | 12,940,000.00 USD | 116,010.00 USD | 0.00 USD | 33,080.00 USD |
| `7D` | `3.95` | 12,430,000.00 USD | 0.00 USD | 12,430,000.00 USD | 8,490.00 USD | 0.00 USD | 2,800.00 USD |
| `1D` | `3.96` | 12,790,000.00 USD | 0.00 USD | 12,790,000.00 USD | 67,260.00 USD | 22,830.00 USD | 17,320.00 USD |
| `7D` | `3.96` | 12,420,000.00 USD | 0.00 USD | 12,420,000.00 USD | 165,060.00 USD | 0.00 USD | 325.84 USD |
| `1D` | `3.97` | 12,680,000.00 USD | 0.00 USD | 12,680,000.00 USD | 2,650.00 USD | 36,470.00 USD | 137,700.00 USD |
| `7D` | `3.97` | 12,250,000.00 USD | 0.00 USD | 12,250,000.00 USD | 235,890.00 USD | 0.00 USD | 2,980.00 USD |
| `1D` | `3.98` | 12,510,000.00 USD | 0.00 USD | 12,510,000.00 USD | 20,780.00 USD | 76,990.00 USD | 94,490.00 USD |
| `7D` | `3.98` | 12,010,000.00 USD | 0.00 USD | 12,010,000.00 USD | 506,280.00 USD | 0.00 USD | 279,750.00 USD |
| `1D` | `3.99` | 12,320,000.00 USD | 0.00 USD | 12,320,000.00 USD | 34,010.00 USD | 64,350.00 USD | 106,350.00 USD |
| `7D` | `3.99` | 11,230,000.00 USD | 0.00 USD | 11,230,000.00 USD | 298,270.00 USD | 26,340.00 USD | 78,590.00 USD |
| `1D` | `4.00` | 12,110,000.00 USD | 0.00 USD | 12,110,000.00 USD | 40,030.00 USD | 17,140.00 USD | 137,750.00 USD |
| `7D` | `4.00` | 10,820,000.00 USD | 0.00 USD | 10,820,000.00 USD | 307,590.00 USD | 68,590.00 USD | 574,560.00 USD |
| `1D` | `4.01` | 11,920,000.00 USD | 0.00 USD | 11,920,000.00 USD | 2,740.00 USD | 158,450.00 USD | 222,850.00 USD |
| `7D` | `4.01` | 9,870,000.00 USD | 0.00 USD | 9,870,000.00 USD | 371,710.00 USD | 57,440.00 USD | 439,000.00 USD |
| `1D` | `4.02` | 11,530,000.00 USD | 0.00 USD | 11,530,000.00 USD | 135,580.00 USD | 52,150.00 USD | 125,360.00 USD |
| `7D` | `4.02` | 9,000,000.00 USD | 0.00 USD | 9,000,000.00 USD | 271,690.00 USD | 156,620.00 USD | 251,320.00 USD |
| `1D` | `4.03` | 11,220,000.00 USD | 0.00 USD | 11,220,000.00 USD | 65,620.00 USD | 59,350.00 USD | 324.38 USD |
| `7D` | `4.03` | 8,320,000.00 USD | 0.00 USD | 8,320,000.00 USD | 247,960.00 USD | 0.00 USD | 344,930.00 USD |
| `1D` | `4.04` | 11,090,000.00 USD | 0.00 USD | 11,090,000.00 USD | 69,810.00 USD | 21,940.00 USD | 183,420.00 USD |
| `7D` | `4.04` | 7,730,000.00 USD | 0.00 USD | 7,730,000.00 USD | 321,230.00 USD | 0.00 USD | 492,290.00 USD |
| `1D` | `4.05` | 10,820,000.00 USD | 0.00 USD | 10,820,000.00 USD | 348,930.00 USD | 23,720.00 USD | 232.83 USD |
| `7D` | `4.05` | 6,920,000.00 USD | 0.00 USD | 6,920,000.00 USD | 2,180.00 USD | 41,020.00 USD | 68,490.00 USD |
| `1D` | `4.06` | 10,450,000.00 USD | 0.00 USD | 10,450,000.00 USD | 35,870.00 USD | 83,800.00 USD | 450,950.00 USD |
| `7D` | `4.06` | 6,810,000.00 USD | 0.00 USD | 6,810,000.00 USD | 0.00 USD | 72,410.00 USD | 523.71 USD |
| `1D` | `4.07` | 9,880,000.00 USD | 0.00 USD | 9,880,000.00 USD | 358,380.00 USD | 205,460.00 USD | 334,510.00 USD |
| `7D` | `4.07` | 6,730,000.00 USD | 0.00 USD | 6,730,000.00 USD | 0.00 USD | 287,180.00 USD | 166,640.00 USD |
| `1D` | `4.08` | 8,980,000.00 USD | 0.00 USD | 8,980,000.00 USD | 69,080.00 USD | 277,630.00 USD | 133,890.00 USD |
| `7D` | `4.08` | 6,280,000.00 USD | 0.00 USD | 6,280,000.00 USD | 0.00 USD | 237,170.00 USD | 135.50 USD |
| `1D` | `4.09` | 8,500,000.00 USD | 0.00 USD | 8,500,000.00 USD | 246,920.00 USD | 60,230.00 USD | 168,490.00 USD |
| `7D` | `4.09` | 6,040,000.00 USD | 0.00 USD | 6,040,000.00 USD | 253,510.00 USD | 179,350.00 USD | 433,540.00 USD |
| `1D` | `4.10` | 8,020,000.00 USD | 0.00 USD | 8,020,000.00 USD | 4,000.00 USD | 89,650.00 USD | 141,410.00 USD |
| `7D` | `4.10` | 5,180,000.00 USD | 0.00 USD | 5,180,000.00 USD | 27,630.00 USD | 0.00 USD | 240.24 USD |
| `1D` | `4.11` | 7,790,000.00 USD | 0.00 USD | 7,790,000.00 USD | 120,600.00 USD | 138,540.00 USD | 345,580.00 USD |
| `7D` | `4.11` | 5,150,000.00 USD | 0.00 USD | 5,150,000.00 USD | 0.00 USD | 25,170.00 USD | 295,730.00 USD |
| `1D` | `4.12` | 7,180,000.00 USD | 0.00 USD | 7,180,000.00 USD | 48,010.00 USD | 34,010.00 USD | 274,300.00 USD |
| `7D` | `4.12` | 4,830,000.00 USD | 0.00 USD | 4,830,000.00 USD | 2,900.00 USD | 181,330.00 USD | 0.00 USD |
| `1D` | `4.13` | 6,820,000.00 USD | 0.00 USD | 6,820,000.00 USD | 159,720.00 USD | 0.00 USD | 398,490.00 USD |
| `7D` | `4.13` | 4,640,000.00 USD | 0.00 USD | 4,640,000.00 USD | 154,140.00 USD | 0.00 USD | 237,800.00 USD |
| `1D` | `4.14` | 6,270,000.00 USD | 0.00 USD | 6,270,000.00 USD | 139,890.00 USD | 29,960.00 USD | 125,370.00 USD |
| `7D` | `4.14` | 4,250,000.00 USD | 0.00 USD | 4,250,000.00 USD | 238,150.00 USD | 244,270.00 USD | 345,750.00 USD |
| `1D` | `4.15` | 5,970,000.00 USD | 0.00 USD | 5,970,000.00 USD | 526,070.00 USD | 102,010.00 USD | 367,560.00 USD |
| `7D` | `4.15` | 3,420,000.00 USD | 0.00 USD | 3,420,000.00 USD | 326,430.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `4.16` | 4,980,000.00 USD | 0.00 USD | 4,980,000.00 USD | 297,170.00 USD | 59,420.00 USD | 316,310.00 USD |
| `1D` | `4.17` | 4,300,000.00 USD | 0.00 USD | 4,300,000.00 USD | 250,510.00 USD | 283,430.00 USD | 238,930.00 USD |
| `7D` | `4.17` | 3,100,000.00 USD | 0.00 USD | 3,100,000.00 USD | 252,690.00 USD | 84,340.00 USD | 0.00 USD |
| `1D` | `4.18` | 3,530,000.00 USD | 0.00 USD | 3,530,000.00 USD | 329,080.00 USD | 62,340.00 USD | 201,720.00 USD |
| `7D` | `4.18` | 2,760,000.00 USD | 0.00 USD | 2,760,000.00 USD | 0.00 USD | 0.00 USD | 86,570.00 USD |
| `1D` | `4.19` | 2,940,000.00 USD | 0.00 USD | 2,940,000.00 USD | 148,260.00 USD | 138,280.00 USD | 244,930.00 USD |
| `7D` | `4.19` | 2,670,000.00 USD | 0.00 USD | 2,670,000.00 USD | 2,760.00 USD | 50,340.00 USD | 393,520.00 USD |
| `1D` | `4.20` | 2,400,000.00 USD | 0.00 USD | 2,400,000.00 USD | 31,500.00 USD | 40,570.00 USD | 131,830.00 USD |
| `7D` | `4.20` | 2,230,000.00 USD | 0.00 USD | 2,230,000.00 USD | 227,690.00 USD | 86,790.00 USD | 371,630.00 USD |
| `1D` | `4.21` | 2,200,000.00 USD | 0.00 USD | 2,200,000.00 USD | 487,450.00 USD | 98,820.00 USD | 217,230.00 USD |
| `7D` | `4.21` | 1,540,000.00 USD | 0.00 USD | 1,540,000.00 USD | 308,290.00 USD | 0.00 USD | 146,990.00 USD |
| `1D` | `4.22` | 1,400,000.00 USD | 0.00 USD | 1,400,000.00 USD | 83,280.00 USD | 59,930.00 USD | 56,420.00 USD |
| `7D` | `4.22` | 1,080,000.00 USD | 0.00 USD | 1,080,000.00 USD | 119,070.00 USD | 142,820.00 USD | 417,550.00 USD |
| `1D` | `4.23` | 1,200,000.00 USD | 0.00 USD | 1,200,000.00 USD | 113,770.00 USD | 114,760.00 USD | 274,130.00 USD |
| `7D` | `4.23` | 404,910.00 USD | 0.00 USD | 404,910.00 USD | 182,720.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `4.24` | 695,280.00 USD | 0.00 USD | 695,280.00 USD | 40,490.00 USD | 15,710.00 USD | 0.00 USD |
| `1D` | `4.25` | 639,070.00 USD | 0.00 USD | 639,070.00 USD | 70,910.00 USD | 0.00 USD | 186,310.00 USD |
| `7D` | `4.25` | 222,190.00 USD | 0.00 USD | 222,190.00 USD | 3,390.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `4.26` | 381,860.00 USD | 0.00 USD | 381,860.00 USD | 0.00 USD | 0.00 USD | 85,610.00 USD |
| `7D` | `4.26` | 218,800.00 USD | 0.00 USD | 218,800.00 USD | 2,960.00 USD | 0.00 USD | 173,150.00 USD |
| `1D` | `4.27` | 296,250.00 USD | 0.00 USD | 296,250.00 USD | 0.00 USD | 44,870.00 USD | 0.00 USD |
| `7D` | `4.27` | 42,690.00 USD | 0.00 USD | 42,690.00 USD | 24,810.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `4.28` | 251,390.00 USD | 0.00 USD | 251,390.00 USD | 4,310.00 USD | 28,780.00 USD | 0.00 USD |
| `7D` | `4.28` | 17,880.00 USD | 0.00 USD | 17,880.00 USD | 5,380.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `4.29` | 218,290.00 USD | 0.00 USD | 218,290.00 USD | 217,970.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4.29` | 12,490.00 USD | 0.00 USD | 12,490.00 USD | 5,150.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `4.32` | 326.33 USD | 0.00 USD | 326.33 USD | 0.00 USD | 0.00 USD | 326.33 USD |
| `7D` | `4.34` | 7,340.00 USD | 0.00 USD | 7,340.00 USD | 0.00 USD | 0.00 USD | 7,340.00 USD |
| `1D` | `4.35` | 157,030.00 USD | 157,030.00 USD | 0.00 USD | 157,030.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `4.35` | 314,060.00 USD | 314,060.00 USD | 0.00 USD | 157,030.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4.35` | 252,690.00 USD | 252,690.00 USD | 0.00 USD | 252,690.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `4.35` | 505,380.00 USD | 505,380.00 USD | 0.00 USD | 252,690.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `4.36` | 694,220.00 USD | 694,220.00 USD | 0.00 USD | 100,970.00 USD | 0.00 USD | 279,180.00 USD |
| `1D` | `4.37` | 1,370,000.00 USD | 1,370,000.00 USD | 0.00 USD | 280,420.00 USD | 0.00 USD | 400,000.00 USD |
| `7D` | `4.37` | 949,240.00 USD | 949,240.00 USD | 0.00 USD | 0.00 USD | 50,340.00 USD | 393,520.00 USD |
| `1D` | `4.38` | 2,020,000.00 USD | 2,020,000.00 USD | 0.00 USD | 3,030.00 USD | 0.00 USD | 640,700.00 USD |
| `7D` | `4.38` | 1,440,000.00 USD | 1,440,000.00 USD | 0.00 USD | 0.00 USD | 228,720.00 USD | 261,380.00 USD |
| `1D` | `4.39` | 2,920,000.00 USD | 2,920,000.00 USD | 0.00 USD | 356,920.00 USD | 41,380.00 USD | 505,620.00 USD |
| `7D` | `4.39` | 2,520,000.00 USD | 2,520,000.00 USD | 0.00 USD | 560,900.00 USD | 149,280.00 USD | 369,470.00 USD |
| `1D` | `4.40` | 3,990,000.00 USD | 3,990,000.00 USD | 0.00 USD | 541,780.00 USD | 118,310.00 USD | 408,330.00 USD |
| `7D` | `4.40` | 3,680,000.00 USD | 3,680,000.00 USD | 0.00 USD | 111,810.00 USD | 169,770.00 USD | 881,540.00 USD |
| `1D` | `4.41` | 5,450,000.00 USD | 5,450,000.00 USD | 0.00 USD | 450,080.00 USD | 317,280.00 USD | 689,400.00 USD |
| `7D` | `4.41` | 4,210,000.00 USD | 4,210,000.00 USD | 0.00 USD | 184,170.00 USD | 65,600.00 USD | 278,000.00 USD |
| `1D` | `4.42` | 5,770,000.00 USD | 5,770,000.00 USD | 0.00 USD | 41,570.00 USD | 157,960.00 USD | 127,800.00 USD |
| `7D` | `4.42` | 4,860,000.00 USD | 4,860,000.00 USD | 0.00 USD | 404,280.00 USD | 71,590.00 USD | 175,990.00 USD |
| `1D` | `4.43` | 6,340,000.00 USD | 6,340,000.00 USD | 0.00 USD | 155,560.00 USD | 109,630.00 USD | 300,550.00 USD |
| `7D` | `4.43` | 5,320,000.00 USD | 5,320,000.00 USD | 0.00 USD | 293,250.00 USD | 88,400.00 USD | 71,780.00 USD |
| `1D` | `4.44` | 7,320,000.00 USD | 7,320,000.00 USD | 0.00 USD | 156,430.00 USD | 370,280.00 USD | 457,750.00 USD |
| `7D` | `4.44` | 5,710,000.00 USD | 5,710,000.00 USD | 0.00 USD | 0.00 USD | 143,990.00 USD | 246,120.00 USD |
| `1D` | `4.45` | 7,680,000.00 USD | 7,680,000.00 USD | 0.00 USD | 76,860.00 USD | 153,510.00 USD | 124,130.00 USD |
| `7D` | `4.45` | 5,930,000.00 USD | 5,930,000.00 USD | 0.00 USD | 0.00 USD | 25,170.00 USD | 196,900.00 USD |
| `1D` | `4.46` | 7,780,000.00 USD | 7,780,000.00 USD | 0.00 USD | 4,580.00 USD | 65,940.00 USD | 33,060.00 USD |
| `7D` | `4.46` | 6,040,000.00 USD | 6,040,000.00 USD | 0.00 USD | 3,070.00 USD | 105,500.00 USD | 2,350.00 USD |
| `1D` | `4.47` | 8,150,000.00 USD | 8,150,000.00 USD | 0.00 USD | 222,670.00 USD | 25,190.00 USD | 120,030.00 USD |
| `7D` | `4.47` | 6,610,000.00 USD | 6,610,000.00 USD | 0.00 USD | 358,290.00 USD | 135,940.00 USD | 75,550.00 USD |
| `1D` | `4.48` | 8,670,000.00 USD | 8,670,000.00 USD | 0.00 USD | 246,890.00 USD | 116,490.00 USD | 150,910.00 USD |
| `7D` | `4.48` | 6,890,000.00 USD | 6,890,000.00 USD | 0.00 USD | 1,870.00 USD | 71,410.00 USD | 210,580.00 USD |
| `1D` | `4.49` | 9,610,000.00 USD | 9,610,000.00 USD | 0.00 USD | 310,660.00 USD | 235,310.00 USD | 403,450.00 USD |
| `7D` | `4.49` | 7,320,000.00 USD | 7,320,000.00 USD | 0.00 USD | 335,730.00 USD | 93,790.00 USD | 162.91 USD |
| `1D` | `4.50` | 10,250,000.00 USD | 10,250,000.00 USD | 0.00 USD | 383,900.00 USD | 77,440.00 USD | 175,170.00 USD |
| `7D` | `4.50` | 7,900,000.00 USD | 7,900,000.00 USD | 0.00 USD | 376,770.00 USD | 200,700.00 USD | 2,050.00 USD |
| `1D` | `4.51` | 11,040,000.00 USD | 11,040,000.00 USD | 0.00 USD | 224,110.00 USD | 149,810.00 USD | 418,530.00 USD |
| `7D` | `4.51` | 7,980,000.00 USD | 7,980,000.00 USD | 0.00 USD | 77,780.00 USD | 0.00 USD | 2,140.00 USD |
| `1D` | `4.52` | 11,710,000.00 USD | 11,710,000.00 USD | 0.00 USD | 291,580.00 USD | 92,260.00 USD | 286,020.00 USD |
| `7D` | `4.52` | 8,210,000.00 USD | 8,210,000.00 USD | 0.00 USD | 2,080.00 USD | 0.00 USD | 225,430.00 USD |
| `1D` | `4.53` | 12,520,000.00 USD | 12,520,000.00 USD | 0.00 USD | 505,320.00 USD | 22,430.00 USD | 280,200.00 USD |
| `7D` | `4.53` | 9,190,000.00 USD | 9,190,000.00 USD | 0.00 USD | 439,420.00 USD | 232,800.00 USD | 310,070.00 USD |
| `1D` | `4.54` | 12,870,000.00 USD | 12,870,000.00 USD | 0.00 USD | 16,950.00 USD | 164,990.00 USD | 167,990.00 USD |
| `7D` | `4.54` | 10,430,000.00 USD | 10,430,000.00 USD | 0.00 USD | 2,730.00 USD | 0.00 USD | 1,240,000.00 USD |
| `1D` | `4.55` | 13,020,000.00 USD | 13,020,000.00 USD | 0.00 USD | 1,620.00 USD | 34,450.00 USD | 108,590.00 USD |
| `7D` | `4.55` | 10,430,000.00 USD | 10,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 237.00 USD |
| `1D` | `4.56` | 13,450,000.00 USD | 13,450,000.00 USD | 0.00 USD | 112,410.00 USD | 32,800.00 USD | 288,580.00 USD |
| `7D` | `4.56` | 10,920,000.00 USD | 10,920,000.00 USD | 0.00 USD | 364,250.00 USD | 124,220.00 USD | 219.44 USD |
| `1D` | `4.57` | 13,800,000.00 USD | 13,800,000.00 USD | 0.00 USD | 176,460.00 USD | 70,180.00 USD | 99,620.00 USD |
| `7D` | `4.57` | 11,460,000.00 USD | 11,460,000.00 USD | 0.00 USD | 305,830.00 USD | 27,650.00 USD | 209,740.00 USD |
| `1D` | `4.58` | 14,950,000.00 USD | 14,950,000.00 USD | 0.00 USD | 423,030.00 USD | 99,430.00 USD | 634,060.00 USD |
| `7D` | `4.58` | 11,590,000.00 USD | 11,590,000.00 USD | 0.00 USD | 44,380.00 USD | 0.00 USD | 86,090.00 USD |
| `1D` | `4.59` | 15,560,000.00 USD | 15,560,000.00 USD | 0.00 USD | 420,560.00 USD | 75,460.00 USD | 109,360.00 USD |
| `7D` | `4.59` | 13,300,000.00 USD | 13,300,000.00 USD | 0.00 USD | 760,880.00 USD | 68,070.00 USD | 881,740.00 USD |
| `1D` | `4.60` | 15,720,000.00 USD | 15,720,000.00 USD | 0.00 USD | 48,970.00 USD | 50,860.00 USD | 66,480.00 USD |
| `7D` | `4.60` | 13,420,000.00 USD | 13,420,000.00 USD | 0.00 USD | 3,460.00 USD | 112,080.00 USD | 2,580.00 USD |
| `1D` | `4.61` | 15,870,000.00 USD | 15,870,000.00 USD | 0.00 USD | 65,250.00 USD | 7,560.00 USD | 76,320.00 USD |
| `7D` | `4.61` | 13,430,000.00 USD | 13,430,000.00 USD | 0.00 USD | 5,400.00 USD | 0.00 USD | 1,140.00 USD |
| `1D` | `4.62` | 16,020,000.00 USD | 16,020,000.00 USD | 0.00 USD | 94,450.00 USD | 31,380.00 USD | 19,780.00 USD |
| `7D` | `4.62` | 13,570,000.00 USD | 13,570,000.00 USD | 0.00 USD | 134,680.00 USD | 0.00 USD | 2,890.00 USD |
| `1D` | `4.63` | 16,020,000.00 USD | 16,020,000.00 USD | 0.00 USD | 2,310.00 USD | 0.00 USD | 422.42 USD |
| `7D` | `4.63` | 13,780,000.00 USD | 13,780,000.00 USD | 0.00 USD | 215,660.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `4.64` | 16,180,000.00 USD | 16,180,000.00 USD | 0.00 USD | 106,430.00 USD | 11,270.00 USD | 41,640.00 USD |
| `7D` | `4.64` | 14,320,000.00 USD | 14,320,000.00 USD | 0.00 USD | 503,610.00 USD | 34,570.00 USD | 1,960.00 USD |
| `1D` | `4.65` | 16,920,000.00 USD | 16,920,000.00 USD | 0.00 USD | 203,560.00 USD | 52,020.00 USD | 486,530.00 USD |
| `7D` | `4.65` | 14,750,000.00 USD | 14,750,000.00 USD | 0.00 USD | 420,940.00 USD | 0.00 USD | 2,070.00 USD |
| `1D` | `4.66` | 17,710,000.00 USD | 17,710,000.00 USD | 0.00 USD | 202,480.00 USD | 309,340.00 USD | 277,010.00 USD |
| `7D` | `4.66` | 15,060,000.00 USD | 15,060,000.00 USD | 0.00 USD | 144,860.00 USD | 18,370.00 USD | 150,940.00 USD |
| `1D` | `4.67` | 18,060,000.00 USD | 18,060,000.00 USD | 0.00 USD | 88,400.00 USD | 0.00 USD | 259,350.00 USD |
| `7D` | `4.67` | 15,100,000.00 USD | 15,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 43,230.00 USD |
| `1D` | `4.68` | 18,260,000.00 USD | 18,260,000.00 USD | 0.00 USD | 60,330.00 USD | 106,120.00 USD | 37,010.00 USD |
| `7D` | `4.68` | 16,020,000.00 USD | 16,020,000.00 USD | 0.00 USD | 381,910.00 USD | 83,630.00 USD | 450,770.00 USD |
| `1D` | `4.69` | 18,650,000.00 USD | 18,650,000.00 USD | 0.00 USD | 168,690.00 USD | 49,160.00 USD | 168,810.00 USD |
| `7D` | `4.69` | 16,180,000.00 USD | 16,180,000.00 USD | 0.00 USD | 52,990.00 USD | 16,870.00 USD | 88,340.00 USD |
| `1D` | `4.70` | 18,990,000.00 USD | 18,990,000.00 USD | 0.00 USD | 69,690.00 USD | 97,490.00 USD | 175,270.00 USD |
| `7D` | `4.70` | 16,490,000.00 USD | 16,490,000.00 USD | 0.00 USD | 74,240.00 USD | 60,360.00 USD | 181,350.00 USD |
| `1D` | `4.71` | 20,040,000.00 USD | 20,040,000.00 USD | 0.00 USD | 390,710.00 USD | 298,900.00 USD | 353,490.00 USD |
| `7D` | `4.71` | 16,980,000.00 USD | 16,980,000.00 USD | 0.00 USD | 178,360.00 USD | 232,800.00 USD | 78,760.00 USD |
| `1D` | `4.72` | 20,270,000.00 USD | 20,270,000.00 USD | 0.00 USD | 2,370.00 USD | 181,280.00 USD | 49,950.00 USD |
| `7D` | `4.72` | 17,190,000.00 USD | 17,190,000.00 USD | 0.00 USD | 7,140.00 USD | 17,360.00 USD | 180,490.00 USD |
| `1D` | `4.73` | 20,440,000.00 USD | 20,440,000.00 USD | 0.00 USD | 110,530.00 USD | 25,210.00 USD | 35,540.00 USD |
| `7D` | `4.73` | 17,260,000.00 USD | 17,260,000.00 USD | 0.00 USD | 59,970.00 USD | 15,660.00 USD | 1,040.00 USD |
| `1D` | `4.74` | 20,830,000.00 USD | 20,830,000.00 USD | 0.00 USD | 68,200.00 USD | 141,320.00 USD | 176,260.00 USD |
| `7D` | `4.74` | 17,650,000.00 USD | 17,650,000.00 USD | 0.00 USD | 14,750.00 USD | 191,030.00 USD | 182,880.00 USD |
| `1D` | `4.75` | 21,240,000.00 USD | 21,240,000.00 USD | 0.00 USD | 100,050.00 USD | 141,340.00 USD | 171,270.00 USD |
| `7D` | `4.75` | 18,200,000.00 USD | 18,200,000.00 USD | 0.00 USD | 17,340.00 USD | 185,060.00 USD | 343,810.00 USD |
| `1D` | `4.76` | 21,350,000.00 USD | 21,350,000.00 USD | 0.00 USD | 32,430.00 USD | 51,460.00 USD | 31,810.00 USD |
| `7D` | `4.76` | 19,550,000.00 USD | 19,550,000.00 USD | 0.00 USD | 1,030,000.00 USD | 46,890.00 USD | 272,680.00 USD |
| `1D` | `4.77` | 21,510,000.00 USD | 21,510,000.00 USD | 0.00 USD | 19,050.00 USD | 85,030.00 USD | 47,800.00 USD |
| `7D` | `4.77` | 20,450,000.00 USD | 20,450,000.00 USD | 0.00 USD | 732,640.00 USD | 73,410.00 USD | 101,640.00 USD |
| `1D` | `4.78` | 21,650,000.00 USD | 21,650,000.00 USD | 0.00 USD | 37,290.00 USD | 20,000.00 USD | 87,070.00 USD |
| `7D` | `4.78` | 21,580,000.00 USD | 21,580,000.00 USD | 0.00 USD | 499,950.00 USD | 477,230.00 USD | 154,510.00 USD |
| `1D` | `4.79` | 21,830,000.00 USD | 21,830,000.00 USD | 0.00 USD | 74,330.00 USD | 44,330.00 USD | 59,380.00 USD |
| `7D` | `4.79` | 22,620,000.00 USD | 22,620,000.00 USD | 0.00 USD | 713,060.00 USD | 249,310.00 USD | 72,220.00 USD |
| `1D` | `4.80` | 22,300,000.00 USD | 22,300,000.00 USD | 0.00 USD | 209,090.00 USD | 128,280.00 USD | 138,780.00 USD |
| `7D` | `4.80` | 24,210,000.00 USD | 24,210,000.00 USD | 0.00 USD | 1,160,000.00 USD | 432,340.00 USD | 2,480.00 USD |
| `1D` | `4.81` | 22,320,000.00 USD | 22,320,000.00 USD | 0.00 USD | 0.00 USD | 13,110.00 USD | 210.83 USD |
| `7D` | `4.81` | 24,840,000.00 USD | 24,840,000.00 USD | 0.00 USD | 400,800.00 USD | 125,900.00 USD | 101,780.00 USD |
| `1D` | `4.82` | 22,460,000.00 USD | 22,460,000.00 USD | 0.00 USD | 20,630.00 USD | 81,720.00 USD | 35,520.00 USD |
| `7D` | `4.82` | 27,610,000.00 USD | 27,610,000.00 USD | 0.00 USD | 1,010,000.00 USD | 369,430.00 USD | 1,390,000.00 USD |
| `1D` | `4.83` | 22,480,000.00 USD | 22,480,000.00 USD | 0.00 USD | 15,330.00 USD | 5,610.00 USD | 0.00 USD |
| `7D` | `4.83` | 29,250,000.00 USD | 29,250,000.00 USD | 0.00 USD | 822,860.00 USD | 85,680.00 USD | 739,630.00 USD |
| `1D` | `4.84` | 22,620,000.00 USD | 22,620,000.00 USD | 0.00 USD | 34,640.00 USD | 76,320.00 USD | 34,780.00 USD |
| `7D` | `4.84` | 29,750,000.00 USD | 29,750,000.00 USD | 0.00 USD | 97,300.00 USD | 71,790.00 USD | 322,840.00 USD |
| `7D` | `4.85` | 31,780,000.00 USD | 31,780,000.00 USD | 0.00 USD | 487,940.00 USD | 380,760.00 USD | 1,160,000.00 USD |
| `7D` | `4.86` | 33,190,000.00 USD | 33,190,000.00 USD | 0.00 USD | 444,810.00 USD | 162,380.00 USD | 802,380.00 USD |
| `7D` | `4.87` | 34,250,000.00 USD | 34,250,000.00 USD | 0.00 USD | 264,730.00 USD | 136,820.00 USD | 663,430.00 USD |
| `7D` | `4.88` | 35,740,000.00 USD | 35,740,000.00 USD | 0.00 USD | 428,040.00 USD | 266,980.00 USD | 789,710.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `1.12B` | Total OI Tokens: `256,538,718.0 NEAR`
  * 1h OI Change: `-0.64%` | 4h OI Change: `+2.14%` | 24h OI Change: `-12.42%`
  * Exchange Breakdown: Binance=`199.57M` | Bybit=`148.42M` | OKX=`52.37M` | Hyperliquid=`243.92M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `-136.70K` | Last 24h: `-22.13K` | Last 3d: `231.31K` | Last 7d: `198.53K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `-0.0003%` | **USDT OKX** | `-0.0291%` |
| **USDT Bybit** | `-0.0809%` | **USDT KuCoin** | `0.0100%` |
| **USDT MEXC** | `-0.0003%` | **USDT BingX** | `-0.0002%` |
| **USDT Gate** | `-0.0104%` | **USDT Bitget** | `-0.0504%` |
| **CoinM Binance** | `0.0100%` | **CoinM OKX** | `-` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `NEAR` | `43.69%` | `56.31%` | `0.78` | 4,050,000.00 USD |
| `15M` | `Binance` | `47.34%` | `52.66%` | `0.90` | 1,610,000.00 USD |
| `15M` | `OKX` | `46.35%` | `53.65%` | `0.86` | 609,890.00 USD |
| `15M` | `Bybit` | `41.21%` | `58.79%` | `0.70` | 356,850.00 USD |
| `15M` | `KuCoin` | `60.33%` | `39.67%` | `1.52` | 60,850.00 USD |
| `15M` | `Gate` | `51.64%` | `48.36%` | `1.07` | 56,630.00 USD |
| `15M` | `Bitget` | `32.31%` | `67.69%` | `0.48` | 134,690.00 USD |
| `15M` | `BingX` | `37.32%` | `62.68%` | `0.60` | 437,350.00 USD |
| `15M` | `MEXC` | `49.97%` | `50.03%` | `1.00` | 333,050.00 USD |
| `15M` | `Bitunix` | `34.5%` | `65.5%` | `0.53` | 78,110.00 USD |
| `15M` | `Hyperliquid` | `46.42%` | `53.58%` | `0.87` | 28,940.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `40.23%` | `59.77%` | `0.67` | 40,500.00 USD |
| `15M` | `Crypto.com` | `28.26%` | `71.74%` | `0.39` | 0.00 USD |
| `15M` | `WhiteBIT` | `22.48%` | `77.52%` | `0.29` | 278,660.00 USD |
| `15M` | `HTX` | `55.96%` | `44.04%` | `1.27` | 3,780.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `40.38%` | `59.62%` | `0.68` | 16,830.00 USD |
| `15M` | `Aster` | `11%` | `89%` | `0.12` | 4,170.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `72.23%` | `27.77%` | `2.60` | 4,920.00 USD |
| `15M` | `Whale Positions` | `47.34%` | `52.66%` | `0.90` | 1,610,000.00 USD |
| `15M` | `Global Accounts` | `43.69%` | `56.31%` | `0.78` | 4,050,000.00 USD |
| `1H` | `NEAR` | `51.52%` | `48.48%` | `1.06` | 13,910,000.00 USD |
| `1H` | `Binance` | `48.09%` | `51.91%` | `0.93` | 3,790,000.00 USD |
| `1H` | `OKX` | `50.33%` | `49.67%` | `1.01` | 551,870.00 USD |
| `1H` | `Bybit` | `52.42%` | `47.58%` | `1.10` | 517,430.00 USD |
| `1H` | `KuCoin` | `52.15%` | `47.85%` | `1.09` | 74,480.00 USD |
| `1H` | `Gate` | `54.73%` | `45.27%` | `1.21` | 170,200.00 USD |
| `1H` | `Bitget` | `47.09%` | `52.91%` | `0.89` | 163,600.00 USD |
| `1H` | `BingX` | `27.69%` | `72.31%` | `0.38` | 4,130,000.00 USD |
| `1H` | `MEXC` | `60.02%` | `39.98%` | `1.50` | 1,090,000.00 USD |
| `1H` | `Bitunix` | `49.17%` | `50.83%` | `0.97` | 202,820.00 USD |
| `1H` | `Hyperliquid` | `49.01%` | `50.99%` | `0.96` | 130,130.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `41.58%` | `58.42%` | `0.71` | 1,670,000.00 USD |
| `1H` | `Crypto.com` | `0%` | `0%` | `1.00` | 710.02 USD |
| `1H` | `WhiteBIT` | `85.48%` | `14.52%` | `5.89` | 1,210,000.00 USD |
| `1H` | `HTX` | `35.71%` | `64.29%` | `0.56` | 5,450.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `44.47%` | `55.53%` | `0.80` | 163,250.00 USD |
| `1H` | `Aster` | `78.33%` | `21.67%` | `3.61` | 2,790.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `9.14%` | `90.86%` | `0.10` | 43,180.00 USD |
| `1H` | `Whale Positions` | `48.09%` | `51.91%` | `0.93` | 3,790,000.00 USD |
| `1H` | `Global Accounts` | `51.52%` | `48.48%` | `1.06` | 13,910,000.00 USD |
| `4H` | `NEAR` | `46.68%` | `53.32%` | `0.88` | 73,280,000.00 USD |
| `4H` | `Binance` | `50.74%` | `49.26%` | `1.03` | 23,060,000.00 USD |
| `4H` | `OKX` | `52.67%` | `47.33%` | `1.11` | 5,770,000.00 USD |
| `4H` | `Bybit` | `52.77%` | `47.23%` | `1.12` | 5,270,000.00 USD |
| `4H` | `KuCoin` | `46.55%` | `53.45%` | `0.87` | 998,740.00 USD |
| `4H` | `Gate` | `53.12%` | `46.88%` | `1.13` | 2,170,000.00 USD |
| `4H` | `Bitget` | `44.28%` | `55.72%` | `0.79` | 2,100,000.00 USD |
| `4H` | `BingX` | `36.43%` | `63.57%` | `0.57` | 10,150,000.00 USD |
| `4H` | `MEXC` | `47.06%` | `52.94%` | `0.89` | 6,460,000.00 USD |
| `4H` | `Bitunix` | `48.94%` | `51.06%` | `0.96` | 1,740,000.00 USD |
| `4H` | `Hyperliquid` | `35.33%` | `64.67%` | `0.55` | 848,300.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `50.92%` | `49.08%` | `1.04` | 11,050,000.00 USD |
| `4H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `WhiteBIT` | `4.72%` | `95.28%` | `0.05` | 2,820,000.00 USD |
| `4H` | `HTX` | `56.35%` | `43.65%` | `1.29` | 316,160.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `57.84%` | `42.16%` | `1.37` | 421,610.00 USD |
| `4H` | `Aster` | `30.42%` | `69.58%` | `0.44` | 28,660.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `83.77%` | `16.23%` | `5.16` | 70,960.00 USD |
| `4H` | `Whale Positions` | `50.74%` | `49.26%` | `1.03` | 23,060,000.00 USD |
| `4H` | `Global Accounts` | `46.68%` | `53.32%` | `0.88` | 73,280,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5:00 UTC` | `4.25` | `4.25` | `4.25` | `4.26` | `4.23` | 9,185,944.44 USD | 4,818,806.27 USD | 4,367,138.17 USD | 451,668.11 USD | `+4.92%` | `4B / 5S` |
| `0:00 UTC` | `4.30` | `4.30` | `4.30` | `4.36` | `4.24` | 30,489,684.47 USD | 19,297,257.05 USD | 11,192,427.43 USD | 8,104,829.62 USD | `+26.58%` | `32B / 2S` |
| `5:00 UTC` | `4.35` | `4.35` | `4.35` | `4.36` | `4.33` | 15,245,662.84 USD | 8,049,667.44 USD | 7,195,995.40 USD | 853,672.05 USD | `+5.60%` | `0B / 3S` |
| `0:00 UTC` | `4.33` | `4.33` | `4.33` | `4.35` | `4.31` | 8,553,382.74 USD | 3,656,231.21 USD | 4,897,151.53 USD | -1,240,920.31 USD | `-14.51%` | `1B / 5S` |
| `5:00 UTC` | `4.31` | `4.35` | `4.31` | `4.39` | `4.31` | 11,576,553.35 USD | 6,334,405.32 USD | 5,242,148.03 USD | 1,092,257.28 USD | `+9.44%` | `19B / 4S` |
| `0:00 UTC` | `4.34` | `4.34` | `4.34` | `4.37` | `4.32` | 8,173,916.95 USD | 4,141,201.50 USD | 4,032,715.45 USD | 108,486.05 USD | `+1.33%` | `4B / 2S` |
| `5:00 UTC` | `4.32` | `4.32` | `4.32` | `4.34` | `4.31` | 8,060,413.67 USD | 4,212,890.12 USD | 3,847,523.55 USD | 365,366.56 USD | `+4.53%` | `0B / 2S` |
| `0:00 UTC` | `4.31` | `4.32` | `4.31` | `4.36` | `4.29` | 5,778,991.37 USD | 2,863,139.85 USD | 2,915,851.52 USD | -52,711.67 USD | `-0.91%` | `7B / 7S` |
| `5:00 UTC` | `4.36` | `4.36` | `4.36` | `4.38` | `4.34` | 6,093,690.79 USD | 3,348,593.15 USD | 2,745,097.64 USD | 603,495.51 USD | `+9.90%` | `4B / 5S` |
| `0:00 UTC` | `4.35` | `4.35` | `4.35` | `4.38` | `4.33` | 4,415,817.33 USD | 1,729,583.72 USD | 2,686,233.62 USD | -956,649.90 USD | `-21.66%` | `3B / 16S` |

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
| `5m` | 55,780.00 USD | -381,970.00 USD | **`DISTRIBUTION`** |
| `15m` | -118,590.00 USD | -697,890.00 USD | **`DISTRIBUTION`** |
| `30m` | -196,870.00 USD | -998,400.00 USD | **`DISTRIBUTION`** |
| `1h` | -486,430.00 USD | -3,910,000.00 USD | **`DISTRIBUTION`** |
| `2h` | 7,030,000.00 USD | 634,020.00 USD | **`ACCUMULATION`** |
| `4h` | 17,370,000.00 USD | 6,220,000.00 USD | **`ACCUMULATION`** |
| `6h` | 16,860,000.00 USD | -453,780.00 USD | **`ACCUMULATION`** |
| `8h` | 22,410,000.00 USD | 16,230,000.00 USD | **`ACCUMULATION`** |
| `12h` | 18,220,000.00 USD | -2,910,000.00 USD | **`ACCUMULATION`** |
| `24h` | 1,210,000.00 USD | -28,370,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -60,310,000.00 USD | -132,390,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -225,770,000.00 USD | -682,760,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+55.78K` | 15m=`-118.59K` | 1h=`-486.43K` | 24h=`+1.21M`
* Futures Capital Netflows: 5m=`-381.97K` | 15m=`-697.89K` | 1h=`-3.91M` | 24h=`-28.37M`
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
  * `2026-10-30 15:33:00 IST`: [ec.europa.eu] - (Sentiment: `Neutral`)
  * `2026-10-30 15:32:00 IST`: [ec.europa.eu] - (Sentiment: `Neutral`)
  * `2026-10-30 15:19:00 IST`: [dailyforex.com] - (Sentiment: `Neutral`)
  * `2026-10-30 15:12:00 IST`: [breakingthenews.net] - (Sentiment: `Neutral`)
  * `2026-10-30 14:41:00 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 14:38:00 IST`: [@FirstSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 15:36:00 IST`: [destatis.de] - (Sentiment: `Neutral`)
  * `2026-10-30 15:36:00 IST`: [istat.it] - (Sentiment: `Neutral`)
  * `2026-10-30 15:36:00 IST`: [channelnewsasia.com] - (Sentiment: `Neutral`)
  * `2026-10-30 15:36:00 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 15:36:00 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 15:35:00 IST`: [kof.ethz.ch] - (Sentiment: `Neutral`)
  * `2026-10-30 15:35:00 IST`: [gerlachmacro.substack.com] - (Sentiment: `Neutral`)
  * `2026-10-30 15:35:00 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-30 15:35:00 IST`: [insee.fr] - (Sentiment: `Neutral`)


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
  * Spread-Padded Stop Loss: `3.83` (Risk Distance: `0.1097` pts)
  * +2.5R Take Profit: `4.21`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `4.23` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `4.34` (Risk Distance: `0.1097` pts)
  * +2.5R Take Profit: `3.96`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`4.38`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
