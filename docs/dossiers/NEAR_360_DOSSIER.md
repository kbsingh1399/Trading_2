# 🏛️ SOVEREIGN CANDIDATE DOSSIER: NEAR
**Canonical Key**: `NEAR` | **Broker Instrument**: `NERUSD.p` | **Asset Class**: `Crypto Alt L1`
**Timestamp**: `2026-10-30 15:36:15 IST` (`2026-10-30 10:06:15 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `4.36` | **Live Ask Quote**: `4.39` | **Mid Price**: `4.38`
- **Spread Points**: `31.00` | **Spread BPS**: `70.83 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `4.13` | VWAP Z-Score: `+1.52` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `0.0560` (Volatility Regime: `HIGH_EXPANSION`)
  * 14-Period RSI: `61.45` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `4.55` | Lower -3.00σ Band: `3.71`
  * Upper +2.51σ Band: `4.48` | Lower -2.51σ Band: `3.78`
  * Upper +2.01σ Band: `4.41` | Lower -2.01σ Band: `3.85`
  * Upper +2.00σ Band: `4.41` | Lower -2.00σ Band: `3.85`
  * Upper +1.28σ Band: `4.31` | Lower -1.28σ Band: `3.95`
  * Upper +1.00σ Band: `4.27` | Lower -1.00σ Band: `3.99`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`4.31` | EMA-20=`4.27` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`4.24` (Slope: `+0.0000`) | EMA-100=`4.29`
  * Institutional Anchors: EMA-144=`4.33` | EMA-200=`4.38` (Slope: `-0.2440`) | EMA-233=`4.41`
- **Range Boundaries**: 24H High=`4.67` | 24H Low=`3.89` | Weekly High=`4.80` | Weekly Low=`3.89`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `4.23` (Distance: `+3.47%`)
  * Point of Control (POC) = `4.07` (Distance: `+7.57%`)
  * Value Area Low (VAL) = `3.94` (Distance: `+11.09%`)
  * Auction Positioning: `ABOVE_VALUE (Imbalance)` | Session Bias: **`BULLISH (Above Pivot)`** | Market Regime: `RANGE_EXPANSION`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`4.57` | POC=`4.41` | VAL=`4.29`
  * Prior Day Extremes: PDH=`4.75` | PDL=`4.08` | PDC=`4.15`
  * Monday Range Blueprint: High=`4.65` | Mid=`4.53` | Low=`4.41`
  * Developing Weekly Value Area: Weekly VAH=`4.70` | Weekly POC=`4.45` | Weekly VAL=`4.39`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`4.26` | Low=`3.89`
  * London Session (08:00-16:00 UTC): High=`4.37` | Low=`4.15`
  * New York Session (13:00-21:00 UTC): High=`4.40` | Low=`4.35`
  * Initial Balance (First Hour): IB High=`4.27` | IB Low=`4.17`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `4.36` - `4.39`
  * Optimal Trade Entry (OTE 0.705): `4.39`
  * Structural Invalidation Anchor (0.786): `4.41`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `4.36` | `4.36` | `4.34` | `4.36` | `442,208` | 1,922,562.92 USD | -252,146.30 USD | `-13.12%` | -6,904,552.65 USD | `-0.44` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `5m` | `4.36` | `4.37` | `4.36` | `4.37` | `431,921` | 1,884,723.70 USD | 406,193.44 USD | `+21.55%` | -6,498,359.22 USD | `+0.46` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `5m` | `4.37` | `4.38` | `4.36` | `4.38` | `467,436` | 2,044,256.75 USD | 258,144.92 USD | `+12.63%` | -6,240,214.29 USD | `+0.34` | **`BULLISH`** | `DELTA ALIGNED` |
| `15m` | `4.33` | `4.34` | `4.31` | `4.32` | `1,865,332` | 8,060,413.67 USD | 365,366.56 USD | `+4.53%` | -6,599,694.68 USD | `+0.07` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `15m` | `4.32` | `4.36` | `4.29` | `4.36` | `1,336,780` | 5,778,991.37 USD | -52,711.67 USD | `-0.91%` | -6,652,406.35 USD | `-0.12` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `15m` | `4.36` | `4.38` | `4.34` | `4.38` | `1,343,080` | 5,858,173.01 USD | 418,786.69 USD | `+7.15%` | -6,233,619.66 USD | `+0.05` | **`BULLISH`** | `DELTA ALIGNED` |
| `1h` | `4.34` | `4.34` | `4.21` | `4.25` | `9,473,664` | 40,439,071.22 USD | -3,673,419.57 USD | `-9.08%` | -15,883,385.93 USD | `-0.74` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `4.25` | `4.39` | `4.24` | `4.36` | `15,226,975` | 65,865,283.41 USD | 8,809,838.63 USD | `+13.38%` | -7,073,547.30 USD | `+2.04` | **`BULLISH`** | `DELTA ALIGNED` |
| `1h` | `4.36` | `4.38` | `4.29` | `4.38` | `6,426,428` | 27,864,865.36 USD | 833,333.00 USD | `+2.99%` | -6,240,214.29 USD | `+0.23` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `4.06` | `4.17` | `3.90` | `4.16` | `46,830,819` | 188,194,075.16 USD | -412,364.95 USD | `-0.22%` | -12,215,320.93 USD | `+0.44` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `4.16` | `4.36` | `4.12` | `4.25` | `33,821,215` | 143,651,581.49 USD | -2,835,728.00 USD | `-1.97%` | -15,051,048.93 USD | `+0.03` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `4.25` | `4.39` | `4.24` | `4.38` | `21,653,403` | 93,730,148.77 USD | 9,643,171.64 USD | `+10.29%` | -5,407,877.29 USD | `+1.55` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `4.65` | `4.69` | `4.38` | `4.40` | `28,351,581` | 128,263,626.10 USD | -4,168,943.82 USD | `-3.25%` | 240,083.28 USD | `-1.00` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `4.40` | `4.41` | `4.04` | `4.06` | `71,964,012` | 300,508,235.77 USD | -12,043,039.27 USD | `-4.01%` | -11,802,955.99 USD | `-1.21` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `4.06` | `4.17` | `3.90` | `4.16` | `46,830,819` | 188,194,075.16 USD | -412,364.95 USD | `-0.22%` | -12,215,320.93 USD | `+0.44` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `4.16` | `4.36` | `4.12` | `4.25` | `33,821,215` | 143,651,581.49 USD | -2,835,728.00 USD | `-1.97%` | -15,051,048.93 USD | `+0.03` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `4.25` | `4.39` | `4.24` | `4.38` | `21,653,403` | 93,730,148.77 USD | 9,643,171.64 USD | `+10.29%` | -5,407,877.29 USD | `+1.55` | **`BULLISH`** | `DELTA ALIGNED` |

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
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 15:30:10 IST` |

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
  * 24H Horizon: Short MP=`4.42` (Vol: 795,900.00 USD, Dist: `+1.52%`) | Long MP=`4.18` (Vol: 505,600.00 USD, Dist: `--3.95%`)
  * 48H Horizon: Short MP=`4.41` (Vol: 795,900.00 USD, Dist: `+1.44%`) | Long MP=`4.18` (Vol: 505,600.00 USD, Dist: `--3.95%`)
  * 3D Horizon: Short MP=`4.41` (Vol: 795,900.00 USD, Dist: `+1.44%`) | Long MP=`4.18` (Vol: 505,600.00 USD, Dist: `--3.95%`)
  * 7D Horizon: Short MP=`4.42` (Vol: 795,900.00 USD, Dist: `+1.58%`) | Long MP=`4.18` (Vol: 505,600.00 USD, Dist: `--3.86%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
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
| `7D` | `Long Liquidation` | `3.48` | 18,760,000.00 USD | 18,760,000.00 USD | 45,650.00 USD | 26,250.00 USD | 1,510.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.48` | 30,100.00 USD | 6,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.50` | 48,550.00 USD | 6,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.50` | 18,690,000.00 USD | 18,690,000.00 USD | 16,960.00 USD | 6,940.00 USD | 38,050.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.50` | 68,770.00 USD | 6,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.51` | 18,630,000.00 USD | 18,630,000.00 USD | 3,690.00 USD | 0.00 USD | 231.64 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.52` | 42,280.00 USD | 6,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.52` | 18,620,000.00 USD | 18,620,000.00 USD | 15,180.00 USD | 0.00 USD | 41,090.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.52` | 21,620.00 USD | 6,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.53` | 18,570,000.00 USD | 18,570,000.00 USD | 93,360.00 USD | 40,470.00 USD | 96,140.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.54` | 84,160.00 USD | 6,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.54` | 18,340,000.00 USD | 18,340,000.00 USD | 3,040.00 USD | 58,300.00 USD | 30,480.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.54` | 152,250.00 USD | 6,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.55` | 18,250,000.00 USD | 18,250,000.00 USD | 128,490.00 USD | 54,880.00 USD | 45,330.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.56` | 570,020.00 USD | 6,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.56` | 18,020,000.00 USD | 18,020,000.00 USD | 61,170.00 USD | 0.00 USD | 32.49 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.56` | 25,750.00 USD | 5,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.57` | 17,960,000.00 USD | 17,960,000.00 USD | 86,360.00 USD | 27,910.00 USD | 84,270.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.58` | 1,340,000.00 USD | 5,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.58` | 17,760,000.00 USD | 17,760,000.00 USD | 173,980.00 USD | 48,640.00 USD | 59,950.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.58` | 120,640.00 USD | 4,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.59` | 17,480,000.00 USD | 17,480,000.00 USD | 535.75 USD | 18,170.00 USD | 78.80 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.60` | 24,010.00 USD | 4,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.60` | 17,460,000.00 USD | 17,460,000.00 USD | 64,170.00 USD | 21,460.00 USD | 22,050.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.60` | 72,910.00 USD | 4,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.61` | 17,350,000.00 USD | 17,350,000.00 USD | 56,580.00 USD | 37,060.00 USD | 44,890.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.62` | 229,270.00 USD | 3,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.62` | 17,210,000.00 USD | 17,210,000.00 USD | 92,130.00 USD | 26,640.00 USD | 97,570.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.62` | 125,580.00 USD | 3,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.63` | 16,990,000.00 USD | 16,990,000.00 USD | 50,840.00 USD | 8,120.00 USD | 159.02 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.63` | 3,550.00 USD | 3,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.64` | 16,940,000.00 USD | 16,940,000.00 USD | 2,410.00 USD | 41,960.00 USD | 119,140.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.65` | 15,050.00 USD | 3,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.65` | 16,770,000.00 USD | 16,770,000.00 USD | 53,900.00 USD | 7,050.00 USD | 31,190.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.65` | 20,860.00 USD | 3,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.66` | 16,680,000.00 USD | 16,680,000.00 USD | 32,350.00 USD | 15,090.00 USD | 125,270.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.67` | 39,720.00 USD | 3,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.67` | 16,510,000.00 USD | 16,510,000.00 USD | 52,020.00 USD | 14,480.00 USD | 53,670.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.67` | 94,680.00 USD | 3,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.68` | 16,390,000.00 USD | 16,390,000.00 USD | 1,010.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.69` | 217,880.00 USD | 3,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.69` | 16,390,000.00 USD | 16,390,000.00 USD | 27,750.00 USD | 0.00 USD | 59,840.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.69` | 102,030.00 USD | 3,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.70` | 16,300,000.00 USD | 16,300,000.00 USD | 20,470.00 USD | 7,370.00 USD | 112,470.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.71` | 90,780.00 USD | 3,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.71` | 16,160,000.00 USD | 16,160,000.00 USD | 51,960.00 USD | 0.00 USD | 74,330.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.71` | 12,740.00 USD | 3,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.72` | 16,030,000.00 USD | 16,030,000.00 USD | 425.03 USD | 0.00 USD | 183.06 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.73` | 355,230.00 USD | 3,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.73` | 16,030,000.00 USD | 16,030,000.00 USD | 41,940.00 USD | 10,880.00 USD | 56,790.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.73` | 123,790.00 USD | 2,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.74` | 15,920,000.00 USD | 15,920,000.00 USD | 130,620.00 USD | 40,020.00 USD | 122,480.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.75` | 24,210.00 USD | 2,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.75` | 15,630,000.00 USD | 15,630,000.00 USD | 3,890.00 USD | 51,780.00 USD | 129,350.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.75` | 150,270.00 USD | 2,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.76` | 15,440,000.00 USD | 15,440,000.00 USD | 32,650.00 USD | 10,110.00 USD | 22,610.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.77` | 65,190.00 USD | 2,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.77` | 15,380,000.00 USD | 15,380,000.00 USD | 15,340.00 USD | 8,090.00 USD | 23,020.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.77` | 123,660.00 USD | 2,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.78` | 15,330,000.00 USD | 15,330,000.00 USD | 24,180.00 USD | 93,830.00 USD | 41,570.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.79` | 48,560.00 USD | 2,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.79` | 15,170,000.00 USD | 15,170,000.00 USD | 51,640.00 USD | 0.00 USD | 137,710.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.79` | 34,520.00 USD | 2,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.80` | 18,670,000.00 USD | 18,670,000.00 USD | 11,920.00 USD | 24,440.00 USD | 144,410.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.80` | 14,980,000.00 USD | 14,980,000.00 USD | 8,210.00 USD | 34,570.00 USD | 17,840.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.81` | 585,450.00 USD | 2,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.81` | 18,480,000.00 USD | 18,480,000.00 USD | 213,700.00 USD | 0.00 USD | 103,870.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.81` | 14,920,000.00 USD | 14,920,000.00 USD | 5,310.00 USD | 0.00 USD | 1,430.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.81` | 10,980.00 USD | 1,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.82` | 18,170,000.00 USD | 18,170,000.00 USD | 49,390.00 USD | 31,910.00 USD | 141,610.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.82` | 14,910,000.00 USD | 14,910,000.00 USD | 5,630.00 USD | 18,370.00 USD | 25,600.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.83` | 181,850.00 USD | 1,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.83` | 17,940,000.00 USD | 17,940,000.00 USD | 125,840.00 USD | 125,330.00 USD | 114,620.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.83` | 14,870,000.00 USD | 14,870,000.00 USD | 50,540.00 USD | 50,500.00 USD | 153.98 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.83` | 171,380.00 USD | 1,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.84` | 17,580,000.00 USD | 17,580,000.00 USD | 150,080.00 USD | 46,190.00 USD | 64,230.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.84` | 14,760,000.00 USD | 14,760,000.00 USD | 7,940.00 USD | 33,350.00 USD | 146.37 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.85` | 119,620.00 USD | 1,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.85` | 17,320,000.00 USD | 17,320,000.00 USD | 186,230.00 USD | 175,470.00 USD | 37,740.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.85` | 14,720,000.00 USD | 14,720,000.00 USD | 3,390.00 USD | 49,170.00 USD | 84,260.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.85` | 22,330.00 USD | 1,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.86` | 16,920,000.00 USD | 16,920,000.00 USD | 39,130.00 USD | 39,050.00 USD | 52,990.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.86` | 14,590,000.00 USD | 14,590,000.00 USD | 5,190.00 USD | 173,980.00 USD | 39,790.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.87` | 71,550.00 USD | 1,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.87` | 16,790,000.00 USD | 16,790,000.00 USD | 53,480.00 USD | 58,230.00 USD | 188,360.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.87` | 14,370,000.00 USD | 14,370,000.00 USD | 62,650.00 USD | 0.00 USD | 197,600.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.88` | 8,130.00 USD | 950,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.88` | 16,490,000.00 USD | 16,490,000.00 USD | 35,520.00 USD | 26,560.00 USD | 224,940.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.88` | 14,110,000.00 USD | 14,110,000.00 USD | 110,160.00 USD | 86,900.00 USD | 156,790.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.88` | 173,140.00 USD | 942,610.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.89` | 16,200,000.00 USD | 16,200,000.00 USD | 396,980.00 USD | 100,370.00 USD | 258,260.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.89` | 13,750,000.00 USD | 13,750,000.00 USD | 4,240.00 USD | 50,710.00 USD | 83,380.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.90` | 93,930.00 USD | 769,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.90` | 15,440,000.00 USD | 15,440,000.00 USD | 33,360.00 USD | 49,080.00 USD | 223,320.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.90` | 13,610,000.00 USD | 13,610,000.00 USD | 274,050.00 USD | 28,250.00 USD | 51,510.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.90` | 7,990.00 USD | 675,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.91` | 15,140,000.00 USD | 15,140,000.00 USD | 351,900.00 USD | 120,100.00 USD | 276,080.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.91` | 13,260,000.00 USD | 13,260,000.00 USD | 122,540.00 USD | 67,260.00 USD | 46,930.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.92` | 37,030.00 USD | 667,540.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.92` | 14,390,000.00 USD | 14,390,000.00 USD | 318,260.00 USD | 8,570.00 USD | 124,080.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.92` | 13,020,000.00 USD | 13,020,000.00 USD | 85,790.00 USD | 66,710.00 USD | 105,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.92` | 2,050.00 USD | 630,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.93` | 13,940,000.00 USD | 13,940,000.00 USD | 116,350.00 USD | 99,220.00 USD | 97,360.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.93` | 12,770,000.00 USD | 12,770,000.00 USD | 0.00 USD | 28,720.00 USD | 67.04 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.94` | 17,100.00 USD | 628,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.94` | 13,630,000.00 USD | 13,630,000.00 USD | 132,520.00 USD | 53,060.00 USD | 137,210.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.94` | 12,740,000.00 USD | 12,740,000.00 USD | 55,330.00 USD | 0.00 USD | 2,250.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.94` | 149,880.00 USD | 611,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.95` | 13,300,000.00 USD | 13,300,000.00 USD | 116,010.00 USD | 0.00 USD | 33,080.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.95` | 12,680,000.00 USD | 12,680,000.00 USD | 8,490.00 USD | 0.00 USD | 2,800.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.96` | 56,160.00 USD | 461,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.96` | 13,150,000.00 USD | 13,150,000.00 USD | 67,260.00 USD | 22,830.00 USD | 17,320.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.96` | 12,670,000.00 USD | 12,670,000.00 USD | 165,060.00 USD | 0.00 USD | 325.84 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.96` | 1,240.00 USD | 405,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.97` | 13,050,000.00 USD | 13,050,000.00 USD | 2,650.00 USD | 36,470.00 USD | 137,700.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.97` | 12,500,000.00 USD | 12,500,000.00 USD | 235,890.00 USD | 0.00 USD | 2,980.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.98` | 82,400.00 USD | 404,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.98` | 12,870,000.00 USD | 12,870,000.00 USD | 20,780.00 USD | 76,990.00 USD | 94,490.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.98` | 12,260,000.00 USD | 12,260,000.00 USD | 506,280.00 USD | 0.00 USD | 279,750.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.98` | 5,650.00 USD | 321,680.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.99` | 12,680,000.00 USD | 12,680,000.00 USD | 34,010.00 USD | 64,350.00 USD | 106,350.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.99` | 11,480,000.00 USD | 11,480,000.00 USD | 298,270.00 USD | 26,340.00 USD | 78,590.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.00` | 160,840.00 USD | 316,030.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.00` | 12,470,000.00 USD | 12,470,000.00 USD | 40,030.00 USD | 17,140.00 USD | 137,750.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.00` | 11,080,000.00 USD | 11,080,000.00 USD | 307,590.00 USD | 68,590.00 USD | 574,560.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.00` | 11,990.00 USD | 155,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.01` | 12,280,000.00 USD | 12,280,000.00 USD | 2,740.00 USD | 158,450.00 USD | 222,850.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.01` | 10,120,000.00 USD | 10,120,000.00 USD | 371,710.00 USD | 57,440.00 USD | 439,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.01` | 275.83 USD | 143,200.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.02` | 11,890,000.00 USD | 11,890,000.00 USD | 135,580.00 USD | 52,150.00 USD | 125,360.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.02` | 9,260,000.00 USD | 9,260,000.00 USD | 271,690.00 USD | 156,620.00 USD | 251,320.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.03` | 1,910.00 USD | 142,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.03` | 11,580,000.00 USD | 11,580,000.00 USD | 65,620.00 USD | 59,350.00 USD | 324.38 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.03` | 8,580,000.00 USD | 8,580,000.00 USD | 247,960.00 USD | 0.00 USD | 344,930.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.04` | 25,700.00 USD | 141,020.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.04` | 11,460,000.00 USD | 11,460,000.00 USD | 69,810.00 USD | 21,940.00 USD | 183,420.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.04` | 7,980,000.00 USD | 7,980,000.00 USD | 321,230.00 USD | 0.00 USD | 492,290.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.04` | 32,100.00 USD | 115,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.05` | 11,180,000.00 USD | 11,180,000.00 USD | 348,930.00 USD | 23,720.00 USD | 232.83 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.05` | 7,170,000.00 USD | 7,170,000.00 USD | 2,180.00 USD | 41,020.00 USD | 68,490.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.05` | 4,380.00 USD | 83,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.06` | 10,810,000.00 USD | 10,810,000.00 USD | 35,870.00 USD | 83,800.00 USD | 450,780.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.06` | 7,060,000.00 USD | 7,060,000.00 USD | 0.00 USD | 72,410.00 USD | 523.71 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.07` | 1,200.00 USD | 78,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.07` | 10,240,000.00 USD | 10,240,000.00 USD | 358,380.00 USD | 205,460.00 USD | 334,530.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.07` | 6,990,000.00 USD | 6,990,000.00 USD | 0.00 USD | 287,180.00 USD | 166,640.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.08` | 10,210.00 USD | 77,640.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.08` | 9,340,000.00 USD | 9,340,000.00 USD | 69,080.00 USD | 277,630.00 USD | 133,910.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.08` | 6,530,000.00 USD | 6,530,000.00 USD | 0.00 USD | 237,170.00 USD | 135.50 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.08` | 5,330.00 USD | 67,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.09` | 8,860,000.00 USD | 8,860,000.00 USD | 246,920.00 USD | 60,230.00 USD | 168,490.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.09` | 6,290,000.00 USD | 6,290,000.00 USD | 253,510.00 USD | 179,350.00 USD | 433,540.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.09` | 17,640.00 USD | 62,110.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.10` | 8,380,000.00 USD | 8,380,000.00 USD | 4,000.00 USD | 89,650.00 USD | 141,410.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.10` | 5,430,000.00 USD | 5,430,000.00 USD | 27,630.00 USD | 0.00 USD | 240.24 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.11` | 15,640.00 USD | 44,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.11` | 8,150,000.00 USD | 8,150,000.00 USD | 120,600.00 USD | 138,540.00 USD | 345,580.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.11` | 5,400,000.00 USD | 5,400,000.00 USD | 0.00 USD | 25,170.00 USD | 295,730.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.12` | 17,630.00 USD | 28,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.12` | 7,540,000.00 USD | 7,540,000.00 USD | 48,010.00 USD | 34,010.00 USD | 274,300.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.12` | 5,080,000.00 USD | 5,080,000.00 USD | 2,900.00 USD | 181,330.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `4.12` | 11,200.00 USD | 11,200.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.13` | 7,190,000.00 USD | 7,190,000.00 USD | 159,720.00 USD | 0.00 USD | 398,260.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.13` | 4,900,000.00 USD | 4,900,000.00 USD | 154,140.00 USD | 0.00 USD | 237,800.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `4.14` | 6,630,000.00 USD | 6,630,000.00 USD | 139,890.00 USD | 29,960.00 USD | 125,370.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.14` | 4,500,000.00 USD | 4,500,000.00 USD | 238,150.00 USD | 244,270.00 USD | 345,750.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `4.15` | 6,330,000.00 USD | 6,330,000.00 USD | 526,070.00 USD | 102,010.00 USD | 367,560.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.15` | 3,680,000.00 USD | 3,680,000.00 USD | 326,430.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `4.16` | 5,340,000.00 USD | 5,340,000.00 USD | 297,170.00 USD | 59,420.00 USD | 316,310.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.17` | 8,230.00 USD | 8,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.17` | 4,670,000.00 USD | 4,670,000.00 USD | 250,510.00 USD | 283,430.00 USD | 238,930.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.17` | 3,350,000.00 USD | 3,350,000.00 USD | 252,690.00 USD | 84,340.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `4.18` | 3,890,000.00 USD | 3,890,000.00 USD | 329,080.00 USD | 62,340.00 USD | 201,720.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.18` | 3,010,000.00 USD | 3,010,000.00 USD | 0.00 USD | 0.00 USD | 86,570.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `4.19` | 3,300,000.00 USD | 3,300,000.00 USD | 148,260.00 USD | 125,540.00 USD | 244,930.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.19` | 2,930,000.00 USD | 2,930,000.00 USD | 2,760.00 USD | 50,340.00 USD | 393,520.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `4.20` | 2,780,000.00 USD | 2,780,000.00 USD | 540.30 USD | 26,180.00 USD | 131,830.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.20` | 2,480,000.00 USD | 2,480,000.00 USD | 227,690.00 USD | 86,790.00 USD | 371,630.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `4.21` | 2,620,000.00 USD | 2,620,000.00 USD | 487,450.00 USD | 98,820.00 USD | 217,230.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.21` | 1,790,000.00 USD | 1,790,000.00 USD | 308,290.00 USD | 0.00 USD | 146,990.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.21` | 1,770.00 USD | 10,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.22` | 1,820,000.00 USD | 1,820,000.00 USD | 83,280.00 USD | 59,930.00 USD | 56,420.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.22` | 1,340,000.00 USD | 1,340,000.00 USD | 119,070.00 USD | 142,820.00 USD | 417,550.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `4.23` | 1,620,000.00 USD | 1,620,000.00 USD | 113,770.00 USD | 114,760.00 USD | 274,130.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.23` | 657,600.00 USD | 657,600.00 USD | 182,720.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `4.24` | 1,120,000.00 USD | 1,120,000.00 USD | 40,490.00 USD | 15,710.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `4.25` | 1,060,000.00 USD | 1,060,000.00 USD | 70,910.00 USD | 0.00 USD | 186,310.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.25` | 474,880.00 USD | 474,880.00 USD | 3,390.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `4.26` | 802,850.00 USD | 802,850.00 USD | 0.00 USD | 0.00 USD | 85,610.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.26` | 471,490.00 USD | 471,490.00 USD | 2,960.00 USD | 0.00 USD | 173,150.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `4.27` | 717,250.00 USD | 717,250.00 USD | 0.00 USD | 19,380.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.27` | 295,380.00 USD | 295,380.00 USD | 24,810.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `4.28` | 697,860.00 USD | 697,860.00 USD | 4,310.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.28` | 270,560.00 USD | 270,560.00 USD | 5,380.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `4.29` | 693,550.00 USD | 693,550.00 USD | 156,040.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.29` | 265,180.00 USD | 265,180.00 USD | 5,150.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.29` | 1,080.00 USD | 11,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.32` | 537,510.00 USD | 537,510.00 USD | 0.00 USD | 0.00 USD | 326.33 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.34` | 260,030.00 USD | 260,030.00 USD | 0.00 USD | 0.00 USD | 7,340.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `4.35` | 537,180.00 USD | 537,180.00 USD | 157,030.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `4.35` | 252,690.00 USD | 252,690.00 USD | 252,690.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.36` | 3,050.00 USD | 14,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `4.36` | 380,150.00 USD | 380,150.00 USD | 100,970.00 USD | 0.00 USD | 279,180.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.37` | 853,590.00 USD | 853,590.00 USD | 280,420.00 USD | 173,170.00 USD | 400,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.37` | 1,710,000.00 USD | 1,710,000.00 USD | 280,420.00 USD | 173,170.00 USD | 400,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.37` | 443,860.00 USD | 443,860.00 USD | 0.00 USD | 50,340.00 USD | 393,520.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.37` | 887,720.00 USD | 887,720.00 USD | 0.00 USD | 50,340.00 USD | 393,520.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.38` | 83,560.00 USD | 97,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.38` | 2,660,000.00 USD | 2,660,000.00 USD | 250,760.00 USD | 60,680.00 USD | 640,700.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.38` | 1,380,000.00 USD | 1,380,000.00 USD | 0.00 USD | 228,720.00 USD | 261,380.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.39` | 3,560,000.00 USD | 3,560,000.00 USD | 356,920.00 USD | 41,380.00 USD | 505,620.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.39` | 2,460,000.00 USD | 2,460,000.00 USD | 560,900.00 USD | 149,280.00 USD | 369,470.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.39` | 180,760.00 USD | 278,450.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.40` | 4,630,000.00 USD | 4,630,000.00 USD | 541,780.00 USD | 118,310.00 USD | 408,330.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.40` | 3,620,000.00 USD | 3,620,000.00 USD | 111,810.00 USD | 169,770.00 USD | 881,540.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.41` | 6,090,000.00 USD | 6,090,000.00 USD | 450,080.00 USD | 317,280.00 USD | 689,400.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.41` | 4,150,000.00 USD | 4,150,000.00 USD | 184,170.00 USD | 65,600.00 USD | 278,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.42` | 507.73 USD | 278,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.42` | 6,420,000.00 USD | 6,420,000.00 USD | 41,570.00 USD | 157,960.00 USD | 127,800.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.42` | 4,800,000.00 USD | 4,800,000.00 USD | 404,280.00 USD | 71,590.00 USD | 175,990.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.42` | 1,930.00 USD | 280,890.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.43` | 6,980,000.00 USD | 6,980,000.00 USD | 155,560.00 USD | 109,630.00 USD | 300,550.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.43` | 5,250,000.00 USD | 5,250,000.00 USD | 293,250.00 USD | 88,400.00 USD | 71,780.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.43` | 4,430.00 USD | 285,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.44` | 7,970,000.00 USD | 7,970,000.00 USD | 156,430.00 USD | 370,280.00 USD | 457,750.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.44` | 5,640,000.00 USD | 5,640,000.00 USD | 0.00 USD | 143,990.00 USD | 246,120.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.45` | 358.27 USD | 285,680.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.45` | 8,290,000.00 USD | 8,290,000.00 USD | 76,860.00 USD | 128,020.00 USD | 124,130.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.45` | 5,870,000.00 USD | 5,870,000.00 USD | 0.00 USD | 25,170.00 USD | 196,900.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.46` | 38,840.00 USD | 324,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.46` | 8,370,000.00 USD | 8,370,000.00 USD | 4,580.00 USD | 37,160.00 USD | 33,060.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.46` | 5,980,000.00 USD | 5,980,000.00 USD | 3,070.00 USD | 105,500.00 USD | 2,350.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.46` | 1,370.00 USD | 325,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.47` | 8,680,000.00 USD | 8,680,000.00 USD | 160,740.00 USD | 25,190.00 USD | 120,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.47` | 6,550,000.00 USD | 6,550,000.00 USD | 358,290.00 USD | 135,940.00 USD | 75,550.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.47` | 17,400.00 USD | 343,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.48` | 9,190,000.00 USD | 9,190,000.00 USD | 246,890.00 USD | 116,490.00 USD | 150,910.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.48` | 6,830,000.00 USD | 6,830,000.00 USD | 1,870.00 USD | 71,410.00 USD | 210,580.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.49` | 2,030.00 USD | 345,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.49` | 10,140,000.00 USD | 10,140,000.00 USD | 310,660.00 USD | 235,310.00 USD | 403,450.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.49` | 7,260,000.00 USD | 7,260,000.00 USD | 335,730.00 USD | 93,790.00 USD | 162.91 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.50` | 22,680.00 USD | 368,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.50` | 10,780,000.00 USD | 10,780,000.00 USD | 383,900.00 USD | 77,440.00 USD | 175,170.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.50` | 7,840,000.00 USD | 7,840,000.00 USD | 376,770.00 USD | 200,700.00 USD | 2,050.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.50` | 1,530.00 USD | 369,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.51` | 11,570,000.00 USD | 11,570,000.00 USD | 224,110.00 USD | 149,810.00 USD | 418,530.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.51` | 7,920,000.00 USD | 7,920,000.00 USD | 77,780.00 USD | 0.00 USD | 2,140.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.51` | 13,270.00 USD | 382,800.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.52` | 12,240,000.00 USD | 12,240,000.00 USD | 291,580.00 USD | 92,260.00 USD | 286,020.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.52` | 8,150,000.00 USD | 8,150,000.00 USD | 2,080.00 USD | 0.00 USD | 225,430.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.53` | 819.48 USD | 383,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.53` | 13,030,000.00 USD | 13,030,000.00 USD | 505,320.00 USD | 9,690.00 USD | 280,200.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.53` | 9,130,000.00 USD | 9,130,000.00 USD | 439,420.00 USD | 232,800.00 USD | 310,070.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.54` | 965.96 USD | 384,590.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.54` | 13,410,000.00 USD | 13,410,000.00 USD | 16,950.00 USD | 150,600.00 USD | 206,400.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.54` | 10,370,000.00 USD | 10,370,000.00 USD | 2,730.00 USD | 0.00 USD | 1,240,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.54` | 24,260.00 USD | 408,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.55` | 13,550,000.00 USD | 13,550,000.00 USD | 1,620.00 USD | 34,450.00 USD | 108,590.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.55` | 10,370,000.00 USD | 10,370,000.00 USD | 0.00 USD | 0.00 USD | 237.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.55` | 120,920.00 USD | 529,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.56` | 13,950,000.00 USD | 13,950,000.00 USD | 81,450.00 USD | 32,800.00 USD | 288,580.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.56` | 10,860,000.00 USD | 10,860,000.00 USD | 364,250.00 USD | 124,220.00 USD | 219.44 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.57` | 182,600.00 USD | 712,370.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.57` | 14,300,000.00 USD | 14,300,000.00 USD | 176,460.00 USD | 70,180.00 USD | 99,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.57` | 11,400,000.00 USD | 11,400,000.00 USD | 305,830.00 USD | 27,650.00 USD | 209,740.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.58` | 15,460,000.00 USD | 15,460,000.00 USD | 423,030.00 USD | 99,430.00 USD | 634,080.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.58` | 11,530,000.00 USD | 11,530,000.00 USD | 44,380.00 USD | 0.00 USD | 86,090.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.58` | 2,140.00 USD | 714,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.59` | 16,060,000.00 USD | 16,060,000.00 USD | 420,560.00 USD | 75,460.00 USD | 109,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.59` | 13,240,000.00 USD | 13,240,000.00 USD | 760,880.00 USD | 68,070.00 USD | 881,740.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.60` | 16,230,000.00 USD | 16,230,000.00 USD | 48,970.00 USD | 50,860.00 USD | 66,480.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.60` | 13,360,000.00 USD | 13,360,000.00 USD | 3,460.00 USD | 112,080.00 USD | 2,580.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.61` | 16,380,000.00 USD | 16,380,000.00 USD | 65,250.00 USD | 7,560.00 USD | 76,320.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.61` | 13,370,000.00 USD | 13,370,000.00 USD | 5,400.00 USD | 0.00 USD | 1,140.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.62` | 16,520,000.00 USD | 16,520,000.00 USD | 94,450.00 USD | 31,380.00 USD | 19,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.62` | 13,510,000.00 USD | 13,510,000.00 USD | 134,680.00 USD | 0.00 USD | 2,890.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.62` | 51,690.00 USD | 766,200.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.63` | 16,530,000.00 USD | 16,530,000.00 USD | 2,310.00 USD | 0.00 USD | 422.42 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.63` | 13,720,000.00 USD | 13,720,000.00 USD | 215,660.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.63` | 990.04 USD | 767,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.64` | 16,690,000.00 USD | 16,690,000.00 USD | 106,430.00 USD | 11,270.00 USD | 41,460.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.64` | 14,260,000.00 USD | 14,260,000.00 USD | 503,610.00 USD | 34,570.00 USD | 1,960.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.64` | 8,450.00 USD | 775,640.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.65` | 17,430,000.00 USD | 17,430,000.00 USD | 203,560.00 USD | 52,020.00 USD | 486,540.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.65` | 14,680,000.00 USD | 14,680,000.00 USD | 420,940.00 USD | 0.00 USD | 2,070.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.66` | 150,680.00 USD | 926,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.66` | 18,220,000.00 USD | 18,220,000.00 USD | 202,480.00 USD | 309,340.00 USD | 277,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.66` | 15,000,000.00 USD | 15,000,000.00 USD | 144,860.00 USD | 18,370.00 USD | 150,940.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.67` | 101.70 USD | 926,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.67` | 18,560,000.00 USD | 18,560,000.00 USD | 88,400.00 USD | 0.00 USD | 259,350.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.67` | 15,040,000.00 USD | 15,040,000.00 USD | 0.00 USD | 0.00 USD | 43,230.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.67` | 54,290.00 USD | 980,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.68` | 18,770,000.00 USD | 18,770,000.00 USD | 60,330.00 USD | 106,120.00 USD | 37,010.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.68` | 15,960,000.00 USD | 15,960,000.00 USD | 381,910.00 USD | 83,630.00 USD | 450,770.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.68` | 1,030.00 USD | 981,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.69` | 19,150,000.00 USD | 19,150,000.00 USD | 168,690.00 USD | 49,160.00 USD | 168,810.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.69` | 16,120,000.00 USD | 16,120,000.00 USD | 52,990.00 USD | 16,870.00 USD | 88,340.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.70` | 230.06 USD | 981,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.70` | 19,500,000.00 USD | 19,500,000.00 USD | 69,690.00 USD | 97,490.00 USD | 175,270.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.70` | 16,430,000.00 USD | 16,430,000.00 USD | 74,240.00 USD | 60,360.00 USD | 181,350.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.71` | 7,480.00 USD | 989,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.71` | 20,540,000.00 USD | 20,540,000.00 USD | 390,710.00 USD | 298,900.00 USD | 353,490.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.71` | 16,920,000.00 USD | 16,920,000.00 USD | 178,360.00 USD | 232,800.00 USD | 78,760.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.72` | 20,770,000.00 USD | 20,770,000.00 USD | 2,370.00 USD | 181,280.00 USD | 49,950.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.72` | 17,130,000.00 USD | 17,130,000.00 USD | 7,140.00 USD | 17,360.00 USD | 180,490.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.72` | 2,590.00 USD | 992,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.73` | 20,950,000.00 USD | 20,950,000.00 USD | 110,530.00 USD | 25,210.00 USD | 35,540.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.73` | 17,200,000.00 USD | 17,200,000.00 USD | 59,970.00 USD | 15,660.00 USD | 1,040.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.74` | 3,380.00 USD | 995,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.74` | 21,330,000.00 USD | 21,330,000.00 USD | 68,200.00 USD | 141,320.00 USD | 176,260.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.74` | 17,590,000.00 USD | 17,590,000.00 USD | 14,750.00 USD | 191,030.00 USD | 182,880.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.75` | 111,130.00 USD | 1,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.75` | 21,740,000.00 USD | 21,740,000.00 USD | 100,050.00 USD | 141,340.00 USD | 171,270.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.75` | 18,140,000.00 USD | 18,140,000.00 USD | 17,340.00 USD | 185,060.00 USD | 343,810.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.76` | 21,860,000.00 USD | 21,860,000.00 USD | 32,430.00 USD | 51,460.00 USD | 31,810.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.76` | 19,480,000.00 USD | 19,480,000.00 USD | 1,030,000.00 USD | 46,890.00 USD | 272,680.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.76` | 5,980.00 USD | 1,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.77` | 22,010,000.00 USD | 22,010,000.00 USD | 19,050.00 USD | 85,030.00 USD | 47,800.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.77` | 20,390,000.00 USD | 20,390,000.00 USD | 732,640.00 USD | 73,410.00 USD | 101,640.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.78` | 1,730.00 USD | 1,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.78` | 22,160,000.00 USD | 22,160,000.00 USD | 37,290.00 USD | 20,000.00 USD | 87,070.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.78` | 21,520,000.00 USD | 21,520,000.00 USD | 499,950.00 USD | 477,230.00 USD | 154,510.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.79` | 143.55 USD | 1,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.79` | 22,330,000.00 USD | 22,330,000.00 USD | 74,330.00 USD | 44,330.00 USD | 59,260.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.79` | 22,560,000.00 USD | 22,560,000.00 USD | 713,060.00 USD | 249,310.00 USD | 72,220.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.79` | 1,330.00 USD | 1,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.80` | 22,800,000.00 USD | 22,800,000.00 USD | 209,090.00 USD | 123,180.00 USD | 138,790.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.80` | 24,150,000.00 USD | 24,150,000.00 USD | 1,160,000.00 USD | 432,340.00 USD | 2,480.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.81` | 22,840,000.00 USD | 22,840,000.00 USD | 0.00 USD | 19,050.00 USD | 11,630.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.81` | 24,780,000.00 USD | 24,780,000.00 USD | 400,800.00 USD | 125,900.00 USD | 101,780.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.82` | 22,960,000.00 USD | 22,960,000.00 USD | 8,250.00 USD | 81,720.00 USD | 35,520.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.82` | 27,540,000.00 USD | 27,540,000.00 USD | 1,010,000.00 USD | 369,430.00 USD | 1,390,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.83` | 2,360.00 USD | 1,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.83` | 22,980,000.00 USD | 22,980,000.00 USD | 15,330.00 USD | 5,610.00 USD | 129.50 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.83` | 29,190,000.00 USD | 29,190,000.00 USD | 822,860.00 USD | 85,680.00 USD | 739,630.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.83` | 1,540.00 USD | 1,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.84` | 23,130,000.00 USD | 23,130,000.00 USD | 34,640.00 USD | 76,320.00 USD | 34,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.84` | 29,680,000.00 USD | 29,680,000.00 USD | 97,300.00 USD | 71,790.00 USD | 322,840.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.84` | 11,220.00 USD | 1,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `4.85` | 31,720,000.00 USD | 31,720,000.00 USD | 487,940.00 USD | 380,760.00 USD | 1,160,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.86` | 33,130,000.00 USD | 33,130,000.00 USD | 444,810.00 USD | 162,380.00 USD | 802,380.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.87` | 259.79 USD | 1,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `4.87` | 34,190,000.00 USD | 34,190,000.00 USD | 264,730.00 USD | 136,820.00 USD | 663,430.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.88` | 35,680,000.00 USD | 35,680,000.00 USD | 428,040.00 USD | 266,980.00 USD | 789,710.00 USD | `Tier 1 CEX` |
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
| `Live` | `Long` | `0.8950` | 22,120,000.00 USD | 0.00 USD | 39,060.00 USD | `-79.30%` | `43,643.60` |
| `Live` | `Long` | `0.9050` | 22,080,000.00 USD | 0.00 USD | 292.22 USD | `-79.07%` | `322.90` |
| `Live` | `Long` | `0.9150` | 22,080,000.00 USD | 0.00 USD | 11,370.00 USD | `-78.84%` | `12,425.00` |
| `Live` | `Long` | `0.9250` | 22,070,000.00 USD | 0.00 USD | 1,850.00 USD | `-78.61%` | `2,001.60` |
| `Live` | `Long` | `0.9350` | 22,070,000.00 USD | 0.00 USD | 29,760.00 USD | `-78.38%` | `31,823.80` |
| `Live` | `Long` | `0.9550` | 22,040,000.00 USD | 0.00 USD | 2,890.00 USD | `-77.92%` | `3,031.40` |
| `Live` | `Long` | `0.9650` | 22,030,000.00 USD | 0.00 USD | 965.00 USD | `-77.68%` | `1,000.00` |
| `Live` | `Long` | `0.9850` | 22,030,000.00 USD | 0.00 USD | 707.53 USD | `-77.22%` | `718.30` |
| `Live` | `Long` | `0.9950` | 22,030,000.00 USD | 0.00 USD | 154,200.00 USD | `-76.99%` | `154,969.90` |
| `Live` | `Long` | `1.00` | 21,880,000.00 USD | 0.00 USD | 2,560.00 USD | `-76.76%` | `2,543.70` |
| `Live` | `Long` | `1.02` | 21,880,000.00 USD | 0.00 USD | 11,240.00 USD | `-76.30%` | `10,967.70` |
| `Live` | `Long` | `1.03` | 21,860,000.00 USD | 0.00 USD | 36,980.00 USD | `-76.07%` | `35,734.20` |
| `Live` | `Long` | `1.04` | 21,830,000.00 USD | 0.00 USD | 2,740.00 USD | `-75.83%` | `2,617.40` |
| `Live` | `Long` | `1.05` | 21,820,000.00 USD | 0.00 USD | 6,860.00 USD | `-75.60%` | `6,504.40` |
| `Live` | `Long` | `1.06` | 21,820,000.00 USD | 0.00 USD | 892.90 USD | `-75.37%` | `838.40` |
| `Live` | `Long` | `1.07` | 21,820,000.00 USD | 0.00 USD | 5,310.00 USD | `-75.14%` | `4,939.60` |
| `Live` | `Long` | `1.08` | 21,810,000.00 USD | 0.00 USD | 470,570.00 USD | `-74.91%` | `433,703.70` |
| `Live` | `Long` | `1.09` | 21,340,000.00 USD | 0.00 USD | 6,690.00 USD | `-74.68%` | `6,107.50` |
| `Live` | `Long` | `1.10` | 21,330,000.00 USD | 0.00 USD | 1,430.00 USD | `-74.45%` | `1,295.60` |
| `Live` | `Long` | `1.11` | 21,330,000.00 USD | 0.00 USD | 2,160.00 USD | `-74.22%` | `1,936.80` |
| `Live` | `Long` | `1.12` | 21,330,000.00 USD | 0.00 USD | 856.24 USD | `-73.98%` | `761.10` |
| `Live` | `Long` | `1.14` | 21,330,000.00 USD | 0.00 USD | 4,960.00 USD | `-73.75%` | `4,368.60` |
| `Live` | `Long` | `1.15` | 21,320,000.00 USD | 0.00 USD | 26,780.00 USD | `-73.52%` | `23,387.50` |
| `Live` | `Long` | `1.17` | 21,300,000.00 USD | 0.00 USD | 1,810.00 USD | `-73.06%` | `1,553.20` |
| `Live` | `Long` | `1.18` | 21,300,000.00 USD | 0.00 USD | 647.54 USD | `-72.83%` | `551.10` |
| `Live` | `Long` | `1.19` | 21,300,000.00 USD | 0.00 USD | 12,420.00 USD | `-72.60%` | `10,484.90` |
| `Live` | `Long` | `1.20` | 21,280,000.00 USD | 0.00 USD | 148.42 USD | `-72.37%` | `124.20` |
| `Live` | `Long` | `1.24` | 21,280,000.00 USD | 0.00 USD | 18,650.00 USD | `-71.44%` | `15,097.50` |
| `Live` | `Long` | `1.25` | 21,260,000.00 USD | 0.00 USD | 250.87 USD | `-71.21%` | `201.50` |
| `Live` | `Long` | `1.25` | 21,260,000.00 USD | 0.00 USD | 15,020.00 USD | `-70.98%` | `11,969.60` |
| `Live` | `Long` | `1.26` | 21,250,000.00 USD | 0.00 USD | 2,060.00 USD | `-70.75%` | `1,630.60` |
| `Live` | `Long` | `1.27` | 21,250,000.00 USD | 0.00 USD | 2,390.00 USD | `-70.52%` | `1,876.80` |
| `Live` | `Long` | `1.28` | 21,240,000.00 USD | 0.00 USD | 1,160.00 USD | `-70.28%` | `901.80` |
| `Live` | `Long` | `1.29` | 21,240,000.00 USD | 0.00 USD | 258.35 USD | `-70.05%` | `199.50` |
| `Live` | `Long` | `1.30` | 21,240,000.00 USD | 0.00 USD | 116.80 USD | `-69.82%` | `89.50` |
| `Live` | `Long` | `1.32` | 21,240,000.00 USD | 0.00 USD | 9,260.00 USD | `-69.36%` | `6,989.40` |
| `Live` | `Long` | `1.33` | 21,230,000.00 USD | 0.00 USD | 148.32 USD | `-69.13%` | `111.10` |
| `Live` | `Long` | `1.34` | 21,230,000.00 USD | 0.00 USD | 603.91 USD | `-68.90%` | `449.00` |
| `Live` | `Long` | `1.35` | 21,230,000.00 USD | 0.00 USD | 66,360.00 USD | `-68.67%` | `48,972.10` |
| `Live` | `Long` | `1.36` | 21,170,000.00 USD | 0.00 USD | 725.63 USD | `-68.43%` | `531.60` |
| `Live` | `Long` | `1.38` | 21,170,000.00 USD | 0.00 USD | 10,080.00 USD | `-68.20%` | `7,330.70` |
| `Live` | `Long` | `1.39` | 21,160,000.00 USD | 0.00 USD | 12,760.00 USD | `-67.97%` | `9,213.40` |
| `Live` | `Long` | `1.40` | 21,140,000.00 USD | 0.00 USD | 1,060.00 USD | `-67.74%` | `758.20` |
| `Live` | `Long` | `1.41` | 21,140,000.00 USD | 0.00 USD | 27,720.00 USD | `-67.51%` | `19,730.30` |
| `Live` | `Long` | `1.42` | 21,110,000.00 USD | 0.00 USD | 76,020.00 USD | `-67.28%` | `53,725.90` |
| `Live` | `Long` | `1.43` | 21,040,000.00 USD | 0.00 USD | 1,130.00 USD | `-67.05%` | `793.40` |
| `Live` | `Long` | `1.45` | 21,040,000.00 USD | 0.00 USD | 1,530.00 USD | `-66.58%` | `1,061.70` |
| `Live` | `Long` | `1.46` | 21,040,000.00 USD | 0.00 USD | 5,440.00 USD | `-66.35%` | `3,738.20` |
| `Live` | `Long` | `1.47` | 21,030,000.00 USD | 0.00 USD | 14,940.00 USD | `-66.12%` | `10,194.90` |
| `Live` | `Long` | `1.48` | 21,020,000.00 USD | 0.00 USD | 2,290.00 USD | `-65.89%` | `1,550.00` |
| `Live` | `Long` | `1.49` | 21,010,000.00 USD | 0.00 USD | 3,110.00 USD | `-65.66%` | `2,096.20` |
| `Live` | `Long` | `1.50` | 21,010,000.00 USD | 0.00 USD | 2,740.00 USD | `-65.43%` | `1,831.00` |
| `Live` | `Long` | `1.51` | 21,010,000.00 USD | 0.00 USD | 454.50 USD | `-64.97%` | `300.00` |
| `Live` | `Long` | `1.53` | 21,010,000.00 USD | 0.00 USD | 2,340.00 USD | `-64.50%` | `1,527.10` |
| `Live` | `Long` | `1.54` | 21,000,000.00 USD | 0.00 USD | 169.95 USD | `-64.27%` | `110.00` |
| `Live` | `Long` | `1.55` | 21,000,000.00 USD | 0.00 USD | 1,450.00 USD | `-64.04%` | `932.00` |
| `Live` | `Long` | `1.56` | 21,000,000.00 USD | 0.00 USD | 20,570.00 USD | `-63.81%` | `13,146.30` |
| `Live` | `Long` | `1.57` | 20,980,000.00 USD | 0.00 USD | 1,020.00 USD | `-63.58%` | `646.20` |
| `Live` | `Long` | `1.58` | 20,980,000.00 USD | 0.00 USD | 2,180.00 USD | `-63.35%` | `1,374.10` |
| `Live` | `Long` | `1.59` | 20,980,000.00 USD | 0.00 USD | 3,700.00 USD | `-63.12%` | `2,319.70` |
| `Live` | `Long` | `1.60` | 20,980,000.00 USD | 0.00 USD | 191.64 USD | `-62.89%` | `119.40` |
| `Live` | `Long` | `1.64` | 20,980,000.00 USD | 0.00 USD | 6,790.00 USD | `-62.19%` | `4,153.70` |
| `Live` | `Long` | `1.65` | 20,970,000.00 USD | 0.00 USD | 582,010.00 USD | `-61.96%` | `353,805.20` |
| `Live` | `Long` | `1.66` | 20,390,000.00 USD | 0.00 USD | 83,540.00 USD | `-61.73%` | `50,475.70` |
| `Live` | `Long` | `1.67` | 20,300,000.00 USD | 0.00 USD | 6,160.00 USD | `-61.50%` | `3,699.10` |
| `Live` | `Long` | `1.68` | 20,300,000.00 USD | 0.00 USD | 1,520.00 USD | `-61.27%` | `908.70` |
| `Live` | `Long` | `1.69` | 20,300,000.00 USD | 0.00 USD | 17,300.00 USD | `-61.04%` | `10,268.30` |
| `Live` | `Long` | `1.70` | 20,280,000.00 USD | 0.00 USD | 102.72 USD | `-60.80%` | `60.60` |
| `Live` | `Long` | `1.73` | 20,280,000.00 USD | 0.00 USD | 5,460.00 USD | `-60.11%` | `3,164.50` |
| `Live` | `Long` | `1.75` | 20,270,000.00 USD | 0.00 USD | 23,850.00 USD | `-59.42%` | `13,592.20` |
| `Live` | `Long` | `1.76` | 20,250,000.00 USD | 0.00 USD | 2,510.00 USD | `-59.19%` | `1,419.70` |
| `Live` | `Long` | `1.77` | 20,250,000.00 USD | 0.00 USD | 4,330.00 USD | `-58.95%` | `2,440.30` |
| `Live` | `Long` | `1.79` | 20,240,000.00 USD | 0.00 USD | 456.47 USD | `-58.49%` | `254.30` |
| `Live` | `Long` | `1.80` | 20,240,000.00 USD | 0.00 USD | 529.05 USD | `-58.26%` | `293.10` |
| `Live` | `Long` | `1.81` | 20,240,000.00 USD | 0.00 USD | 1,580.00 USD | `-58.03%` | `873.20` |
| `Live` | `Long` | `1.82` | 20,240,000.00 USD | 0.00 USD | 853.74 USD | `-57.80%` | `467.80` |
| `Live` | `Long` | `1.83` | 20,240,000.00 USD | 0.00 USD | 36,780.00 USD | `-57.57%` | `20,041.70` |
| `Live` | `Long` | `1.85` | 20,200,000.00 USD | 0.00 USD | 984.26 USD | `-57.10%` | `530.60` |
| `Live` | `Long` | `1.86` | 20,200,000.00 USD | 0.00 USD | 16,100.00 USD | `-56.87%` | `8,632.40` |
| `Live` | `Long` | `1.88` | 20,180,000.00 USD | 0.00 USD | 656.25 USD | `-56.64%` | `350.00` |
| `Live` | `Long` | `1.90` | 20,180,000.00 USD | 0.00 USD | 37,060.00 USD | `-56.18%` | `19,555.90` |
| `Live` | `Long` | `1.91` | 20,150,000.00 USD | 0.00 USD | 288.61 USD | `-55.95%` | `151.50` |
| `Live` | `Long` | `1.93` | 20,150,000.00 USD | 0.00 USD | 1,120.00 USD | `-55.49%` | `579.70` |
| `Live` | `Long` | `1.94` | 20,150,000.00 USD | 0.00 USD | 1,270.00 USD | `-55.25%` | `654.30` |
| `Live` | `Long` | `1.95` | 20,140,000.00 USD | 0.00 USD | 2,740.00 USD | `-55.02%` | `1,410.10` |
| `Live` | `Long` | `1.96` | 20,140,000.00 USD | 0.00 USD | 2,860.00 USD | `-54.79%` | `1,465.00` |
| `Live` | `Long` | `1.97` | 20,140,000.00 USD | 0.00 USD | 1,730.00 USD | `-54.56%` | `879.10` |
| `Live` | `Long` | `1.98` | 20,140,000.00 USD | 0.00 USD | 35,130.00 USD | `-54.33%` | `17,789.50` |
| `Live` | `Long` | `2.00` | 20,100,000.00 USD | 0.00 USD | 46,610.00 USD | `-53.87%` | `23,361.10` |
| `Live` | `Long` | `2.02` | 20,050,000.00 USD | 0.00 USD | 3,100.00 USD | `-53.40%` | `1,539.50` |
| `Live` | `Long` | `2.02` | 20,050,000.00 USD | 0.00 USD | 3,660.00 USD | `-53.17%` | `1,808.10` |
| `Live` | `Long` | `2.04` | 20,050,000.00 USD | 0.00 USD | 323.36 USD | `-52.94%` | `158.90` |
| `Live` | `Long` | `2.04` | 20,050,000.00 USD | 0.00 USD | 3,460.00 USD | `-52.71%` | `1,693.20` |
| `Live` | `Long` | `2.06` | 20,040,000.00 USD | 0.00 USD | 1,100.00 USD | `-52.48%` | `537.20` |
| `Live` | `Long` | `2.06` | 20,040,000.00 USD | 0.00 USD | 2,520.00 USD | `-52.25%` | `1,220.50` |
| `Live` | `Long` | `2.08` | 20,040,000.00 USD | 0.00 USD | 11,100.00 USD | `-52.02%` | `5,347.70` |
| `Live` | `Long` | `2.08` | 20,030,000.00 USD | 0.00 USD | 18,600.00 USD | `-51.79%` | `8,920.10` |
| `Live` | `Long` | `2.10` | 20,010,000.00 USD | 0.00 USD | 17,340.00 USD | `-51.55%` | `8,274.80` |
| `Live` | `Long` | `2.10` | 19,990,000.00 USD | 0.00 USD | 6,090.00 USD | `-51.32%` | `2,894.60` |
| `Live` | `Long` | `2.12` | 19,990,000.00 USD | 0.00 USD | 14,240.00 USD | `-51.09%` | `6,731.40` |
| `Live` | `Long` | `2.12` | 19,970,000.00 USD | 0.00 USD | 8,770.00 USD | `-50.86%` | `4,127.30` |
| `Live` | `Long` | `2.13` | 19,960,000.00 USD | 0.00 USD | 2,140.00 USD | `-50.63%` | `1,000.80` |
| `Live` | `Long` | `2.15` | 19,960,000.00 USD | 0.00 USD | 2,110.00 USD | `-50.40%` | `983.60` |
| `Live` | `Long` | `2.15` | 19,960,000.00 USD | 0.00 USD | 4,550.00 USD | `-50.17%` | `2,113.50` |
| `Live` | `Long` | `2.17` | 19,960,000.00 USD | 0.00 USD | 279,760.00 USD | `-49.94%` | `129,219.70` |
| `Live` | `Long` | `2.17` | 19,680,000.00 USD | 0.00 USD | 14,140.00 USD | `-49.70%` | `6,500.40` |
| `Live` | `Long` | `2.19` | 19,660,000.00 USD | 0.00 USD | 1,110.00 USD | `-49.47%` | `505.90` |
| `Live` | `Long` | `2.19` | 19,660,000.00 USD | 0.00 USD | 12,830.00 USD | `-49.24%` | `5,843.40` |
| `Live` | `Long` | `2.21` | 19,650,000.00 USD | 0.00 USD | 39,620.00 USD | `-49.01%` | `17,967.40` |
| `Live` | `Long` | `2.21` | 19,610,000.00 USD | 0.00 USD | 91,610.00 USD | `-48.78%` | `41,357.70` |
| `Live` | `Long` | `2.23` | 19,520,000.00 USD | 0.00 USD | 457.24 USD | `-48.55%` | `205.50` |
| `Live` | `Long` | `2.23` | 19,520,000.00 USD | 0.00 USD | 2,450.00 USD | `-48.32%` | `1,097.50` |
| `Live` | `Long` | `2.25` | 19,510,000.00 USD | 0.00 USD | 38,480.00 USD | `-48.09%` | `17,142.40` |
| `Live` | `Long` | `2.25` | 19,480,000.00 USD | 0.00 USD | 329,770.00 USD | `-47.85%` | `146,238.50` |
| `Live` | `Long` | `2.27` | 19,150,000.00 USD | 0.00 USD | 1,580.00 USD | `-47.62%` | `695.70` |
| `Live` | `Long` | `2.27` | 19,140,000.00 USD | 0.00 USD | 812.18 USD | `-47.39%` | `357.00` |
| `Live` | `Long` | `2.29` | 19,140,000.00 USD | 0.00 USD | 463.86 USD | `-47.16%` | `203.00` |
| `Live` | `Long` | `2.29` | 19,140,000.00 USD | 0.00 USD | 11,990.00 USD | `-46.93%` | `5,224.90` |
| `Live` | `Long` | `2.31` | 19,130,000.00 USD | 0.00 USD | 7,500.00 USD | `-46.70%` | `3,254.60` |
| `Live` | `Long` | `2.31` | 19,120,000.00 USD | 0.00 USD | 2,330.00 USD | `-46.47%` | `1,005.00` |
| `Live` | `Long` | `2.33` | 19,120,000.00 USD | 0.00 USD | 13,770.00 USD | `-46.24%` | `5,923.50` |
| `Live` | `Long` | `2.33` | 19,110,000.00 USD | 0.00 USD | 30,690.00 USD | `-46.00%` | `13,145.40` |
| `Live` | `Long` | `2.35` | 19,080,000.00 USD | 0.00 USD | 5,790.00 USD | `-45.77%` | `2,467.50` |
| `Live` | `Long` | `2.35` | 19,070,000.00 USD | 0.00 USD | 25,910.00 USD | `-45.54%` | `11,000.00` |
| `Live` | `Long` | `2.37` | 19,040,000.00 USD | 0.00 USD | 3,840.00 USD | `-45.31%` | `1,624.70` |
| `Live` | `Long` | `2.38` | 19,040,000.00 USD | 0.00 USD | 35,180.00 USD | `-45.08%` | `14,811.30` |
| `Live` | `Long` | `2.38` | 19,010,000.00 USD | 0.00 USD | 6,250.00 USD | `-44.85%` | `2,620.90` |
| `Live` | `Long` | `2.40` | 19,000,000.00 USD | 0.00 USD | 119,870.00 USD | `-44.62%` | `50,048.30` |
| `Live` | `Long` | `2.40` | 18,880,000.00 USD | 0.00 USD | 11,030.00 USD | `-44.39%` | `4,586.00` |
| `Live` | `Long` | `2.42` | 18,870,000.00 USD | 0.00 USD | 1,760,000.00 USD | `-44.15%` | `730,349.00` |
| `Live` | `Long` | `2.42` | 17,100,000.00 USD | 0.00 USD | 273,060.00 USD | `-43.92%` | `112,601.40` |
| `Live` | `Long` | `2.44` | 16,830,000.00 USD | 0.00 USD | 4,770.00 USD | `-43.69%` | `1,957.90` |
| `Live` | `Long` | `2.44` | 16,830,000.00 USD | 0.00 USD | 253,220.00 USD | `-43.46%` | `103,564.60` |
| `Live` | `Long` | `2.46` | 16,570,000.00 USD | 0.00 USD | 49,540.00 USD | `-43.23%` | `20,179.00` |
| `Live` | `Long` | `2.46` | 16,520,000.00 USD | 0.00 USD | 6,090.00 USD | `-43.00%` | `2,469.20` |
| `Live` | `Long` | `2.48` | 16,520,000.00 USD | 0.00 USD | 336.35 USD | `-42.77%` | `135.90` |
| `Live` | `Long` | `2.48` | 16,520,000.00 USD | 0.00 USD | 3,110.00 USD | `-42.54%` | `1,250.20` |
| `Live` | `Long` | `2.50` | 16,510,000.00 USD | 0.00 USD | 15,100.00 USD | `-42.30%` | `6,050.70` |
| `Live` | `Long` | `2.50` | 16,500,000.00 USD | 0.00 USD | 6,000.00 USD | `-42.07%` | `2,395.50` |
| `Live` | `Long` | `2.52` | 16,490,000.00 USD | 0.00 USD | 39,960.00 USD | `-41.61%` | `15,824.10` |
| `Live` | `Long` | `2.54` | 16,450,000.00 USD | 0.00 USD | 866.97 USD | `-41.38%` | `342.00` |
| `Live` | `Long` | `2.54` | 16,450,000.00 USD | 0.00 USD | 105.36 USD | `-41.15%` | `41.40` |
| `Live` | `Long` | `2.56` | 16,450,000.00 USD | 0.00 USD | 621.12 USD | `-40.92%` | `243.10` |
| `Live` | `Long` | `2.56` | 16,450,000.00 USD | 0.00 USD | 7,890.00 USD | `-40.69%` | `3,077.60` |
| `Live` | `Long` | `2.58` | 16,440,000.00 USD | 0.00 USD | 431,260.00 USD | `-40.45%` | `167,479.10` |
| `Live` | `Long` | `2.58` | 16,010,000.00 USD | 0.00 USD | 11,810.00 USD | `-40.22%` | `4,568.30` |
| `Live` | `Long` | `2.60` | 16,000,000.00 USD | 0.00 USD | 82,820.00 USD | `-39.99%` | `31,916.30` |
| `Live` | `Long` | `2.60` | 15,920,000.00 USD | 0.00 USD | 779.94 USD | `-39.76%` | `299.40` |
| `Live` | `Long` | `2.62` | 15,920,000.00 USD | 0.00 USD | 1,190.00 USD | `-39.53%` | `454.70` |
| `Live` | `Long` | `2.62` | 15,920,000.00 USD | 0.00 USD | 2,470.00 USD | `-39.30%` | `941.80` |
| `Live` | `Long` | `2.63` | 15,910,000.00 USD | 0.00 USD | 24,310.00 USD | `-39.07%` | `9,225.00` |
| `Live` | `Long` | `2.65` | 15,890,000.00 USD | 0.00 USD | 6,020.00 USD | `-38.84%` | `2,274.90` |
| `Live` | `Long` | `2.65` | 15,880,000.00 USD | 0.00 USD | 16,760.00 USD | `-38.60%` | `6,312.10` |
| `Live` | `Long` | `2.67` | 15,870,000.00 USD | 0.00 USD | 1,920.00 USD | `-38.37%` | `721.80` |
| `Live` | `Long` | `2.67` | 15,860,000.00 USD | 0.00 USD | 172,860.00 USD | `-38.14%` | `64,622.30` |
| `Live` | `Long` | `2.69` | 15,690,000.00 USD | 0.00 USD | 8,920.00 USD | `-37.91%` | `3,323.40` |
| `Live` | `Long` | `2.69` | 15,680,000.00 USD | 0.00 USD | 733.85 USD | `-37.68%` | `272.30` |
| `Live` | `Long` | `2.71` | 15,680,000.00 USD | 0.00 USD | 170,360.00 USD | `-37.45%` | `62,978.90` |
| `Live` | `Long` | `2.71` | 15,510,000.00 USD | 0.00 USD | 11,750.00 USD | `-37.22%` | `4,327.50` |
| `Live` | `Long` | `2.73` | 15,500,000.00 USD | 0.00 USD | 28,380.00 USD | `-36.99%` | `10,414.30` |
| `Live` | `Long` | `2.73` | 15,470,000.00 USD | 0.00 USD | 1,850.00 USD | `-36.75%` | `675.80` |
| `Live` | `Long` | `2.75` | 15,470,000.00 USD | 0.00 USD | 39,550.00 USD | `-36.52%` | `14,408.60` |
| `Live` | `Long` | `2.75` | 15,430,000.00 USD | 0.00 USD | 365,820.00 USD | `-36.29%` | `132,783.60` |
| `Live` | `Long` | `2.77` | 15,060,000.00 USD | 0.00 USD | 8,890.00 USD | `-36.06%` | `3,214.40` |
| `Live` | `Long` | `2.77` | 15,060,000.00 USD | 0.00 USD | 719.84 USD | `-35.83%` | `259.40` |
| `Live` | `Long` | `2.79` | 15,050,000.00 USD | 0.00 USD | 49,490.00 USD | `-35.60%` | `17,770.30` |
| `Live` | `Long` | `2.79` | 15,010,000.00 USD | 0.00 USD | 12,340.00 USD | `-35.37%` | `4,416.00` |
| `Live` | `Long` | `2.81` | 14,990,000.00 USD | 0.00 USD | 90,180.00 USD | `-35.14%` | `32,148.50` |
| `Live` | `Long` | `2.81` | 14,900,000.00 USD | 0.00 USD | 4,780.00 USD | `-34.90%` | `1,698.90` |
| `Live` | `Long` | `2.83` | 14,900,000.00 USD | 0.00 USD | 13,990.00 USD | `-34.67%` | `4,952.70` |
| `Live` | `Long` | `2.83` | 14,880,000.00 USD | 0.00 USD | 2,400.00 USD | `-34.44%` | `847.80` |
| `Live` | `Long` | `2.85` | 14,880,000.00 USD | 0.00 USD | 180.94 USD | `-34.21%` | `63.60` |
| `Live` | `Long` | `2.85` | 14,880,000.00 USD | 0.00 USD | 1,970.00 USD | `-33.98%` | `690.70` |
| `Live` | `Long` | `2.87` | 14,880,000.00 USD | 0.00 USD | 21,320.00 USD | `-33.75%` | `7,441.30` |
| `Live` | `Long` | `2.88` | 14,860,000.00 USD | 0.00 USD | 878,580.00 USD | `-33.52%` | `305,591.60` |
| `Live` | `Long` | `2.88` | 13,980,000.00 USD | 0.00 USD | 7,430.00 USD | `-33.29%` | `2,576.40` |
| `Live` | `Long` | `2.90` | 13,970,000.00 USD | 0.00 USD | 114,000.00 USD | `-33.05%` | `39,379.30` |
| `Live` | `Long` | `2.90` | 13,860,000.00 USD | 0.00 USD | 199,300.00 USD | `-32.82%` | `68,605.60` |
| `Live` | `Long` | `2.92` | 13,660,000.00 USD | 0.00 USD | 4,900.00 USD | `-32.59%` | `1,681.40` |
| `Live` | `Long` | `2.92` | 13,650,000.00 USD | 0.00 USD | 48,730.00 USD | `-32.36%` | `16,661.40` |
| `Live` | `Long` | `2.94` | 13,610,000.00 USD | 0.00 USD | 50,520.00 USD | `-32.13%` | `17,211.30` |
| `Live` | `Long` | `2.94` | 13,550,000.00 USD | 0.00 USD | 16,860.00 USD | `-31.90%` | `5,725.40` |
| `Live` | `Long` | `2.96` | 13,540,000.00 USD | 0.00 USD | 13,510.00 USD | `-31.67%` | `4,571.50` |
| `Live` | `Long` | `2.96` | 13,520,000.00 USD | 0.00 USD | 104,820.00 USD | `-31.44%` | `35,353.40` |
| `Live` | `Long` | `2.98` | 13,420,000.00 USD | 0.00 USD | 148,230.00 USD | `-31.20%` | `49,824.70` |
| `Live` | `Long` | `2.98` | 13,270,000.00 USD | 0.00 USD | 5,840.00 USD | `-30.97%` | `1,957.00` |
| `Live` | `Long` | `3.00` | 13,270,000.00 USD | 0.00 USD | 13,250.00 USD | `-30.74%` | `4,424.50` |
| `Live` | `Long` | `3.00` | 13,250,000.00 USD | 0.00 USD | 11,020.00 USD | `-30.51%` | `3,667.70` |
| `Live` | `Long` | `3.02` | 13,240,000.00 USD | 0.00 USD | 32,670.00 USD | `-30.28%` | `10,836.40` |
| `Live` | `Long` | `3.02` | 13,210,000.00 USD | 0.00 USD | 20,580.00 USD | `-30.05%` | `6,804.70` |
| `Live` | `Long` | `3.04` | 13,190,000.00 USD | 0.00 USD | 2,570.00 USD | `-29.82%` | `847.40` |
| `Live` | `Long` | `3.04` | 13,190,000.00 USD | 0.00 USD | 109,800.00 USD | `-29.59%` | `36,057.70` |
| `Live` | `Long` | `3.06` | 13,080,000.00 USD | 0.00 USD | 137,520.00 USD | `-29.35%` | `45,013.70` |
| `Live` | `Long` | `3.06` | 12,940,000.00 USD | 0.00 USD | 163,450.00 USD | `-29.12%` | `53,327.10` |
| `Live` | `Long` | `3.08` | 12,770,000.00 USD | 0.00 USD | 157,420.00 USD | `-28.89%` | `51,192.30` |
| `Live` | `Long` | `3.08` | 12,620,000.00 USD | 0.00 USD | 50,590.00 USD | `-28.66%` | `16,398.80` |
| `Live` | `Long` | `3.10` | 12,570,000.00 USD | 0.00 USD | 5,110.00 USD | `-28.43%` | `1,650.90` |
| `Live` | `Long` | `3.10` | 12,560,000.00 USD | 0.00 USD | 22,590.00 USD | `-28.20%` | `7,275.30` |
| `Live` | `Long` | `3.12` | 12,540,000.00 USD | 0.00 USD | 56,190.00 USD | `-27.97%` | `18,037.60` |
| `Live` | `Long` | `3.12` | 12,480,000.00 USD | 0.00 USD | 2,990,000.00 USD | `-27.74%` | `956,842.50` |
| `Live` | `Long` | `3.13` | 9,490,000.00 USD | 0.00 USD | 10,160.00 USD | `-27.50%` | `3,241.30` |
| `Live` | `Long` | `3.15` | 9,480,000.00 USD | 0.00 USD | 99,300.00 USD | `-27.27%` | `31,574.10` |
| `Live` | `Long` | `3.15` | 9,380,000.00 USD | 0.00 USD | 4,250.00 USD | `-27.04%` | `1,347.20` |
| `Live` | `Long` | `3.17` | 9,380,000.00 USD | 0.00 USD | 68,020.00 USD | `-26.81%` | `21,491.90` |
| `Live` | `Long` | `3.17` | 9,310,000.00 USD | 0.00 USD | 1,200.00 USD | `-26.58%` | `376.60` |
| `Live` | `Long` | `3.19` | 9,310,000.00 USD | 0.00 USD | 245,320.00 USD | `-26.35%` | `77,025.00` |
| `Live` | `Long` | `3.19` | 9,060,000.00 USD | 0.00 USD | 258.16 USD | `-26.12%` | `80.80` |
| `Live` | `Long` | `3.21` | 9,060,000.00 USD | 0.00 USD | 5,090.00 USD | `-25.89%` | `1,589.20` |
| `Live` | `Long` | `3.21` | 9,060,000.00 USD | 0.00 USD | 41,620.00 USD | `-25.65%` | `12,945.80` |
| `Live` | `Long` | `3.23` | 9,020,000.00 USD | 0.00 USD | 23,110.00 USD | `-25.42%` | `7,167.00` |
| `Live` | `Long` | `3.23` | 8,990,000.00 USD | 0.00 USD | 43,760.00 USD | `-25.19%` | `13,526.90` |
| `Live` | `Long` | `3.25` | 8,950,000.00 USD | 0.00 USD | 20,060.00 USD | `-24.96%` | `6,181.90` |
| `Live` | `Long` | `3.25` | 8,930,000.00 USD | 0.00 USD | 4,050.00 USD | `-24.73%` | `1,245.10` |
| `Live` | `Long` | `3.27` | 8,930,000.00 USD | 0.00 USD | 33,650.00 USD | `-24.50%` | `10,307.00` |
| `Live` | `Long` | `3.27` | 8,890,000.00 USD | 0.00 USD | 868,070.00 USD | `-24.27%` | `265,060.40` |
| `Live` | `Long` | `3.29` | 8,020,000.00 USD | 0.00 USD | 4,080.00 USD | `-24.04%` | `1,240.60` |
| `Live` | `Long` | `3.29` | 8,020,000.00 USD | 0.00 USD | 134,250.00 USD | `-23.80%` | `40,743.80` |
| `Live` | `Long` | `3.31` | 7,890,000.00 USD | 0.00 USD | 132,030.00 USD | `-23.57%` | `39,948.60` |
| `Live` | `Long` | `3.31` | 7,750,000.00 USD | 0.00 USD | 24,690.00 USD | `-23.34%` | `7,448.70` |
| `Live` | `Long` | `3.33` | 7,730,000.00 USD | 0.00 USD | 13,340.00 USD | `-23.11%` | `4,011.80` |
| `Live` | `Long` | `3.33` | 7,720,000.00 USD | 0.00 USD | 73,460.00 USD | `-22.88%` | `22,026.40` |
| `Live` | `Long` | `3.35` | 7,640,000.00 USD | 0.00 USD | 18,900.00 USD | `-22.65%` | `5,650.40` |
| `Live` | `Long` | `3.35` | 7,620,000.00 USD | 0.00 USD | 1,210.00 USD | `-22.42%` | `360.80` |
| `Live` | `Long` | `3.37` | 7,620,000.00 USD | 0.00 USD | 41,020.00 USD | `-22.19%` | `12,189.30` |
| `Live` | `Long` | `3.38` | 7,580,000.00 USD | 0.00 USD | 55,170.00 USD | `-21.95%` | `16,345.80` |
| `Live` | `Long` | `3.38` | 7,530,000.00 USD | 0.00 USD | 46,170.00 USD | `-21.72%` | `13,638.50` |
| `Live` | `Long` | `3.40` | 7,480,000.00 USD | 0.00 USD | 51,750.00 USD | `-21.49%` | `15,241.70` |
| `Live` | `Long` | `3.40` | 7,430,000.00 USD | 0.00 USD | 104,080.00 USD | `-21.26%` | `30,566.60` |
| `Live` | `Long` | `3.42` | 7,320,000.00 USD | 0.00 USD | 390,810.00 USD | `-21.03%` | `114,438.90` |
| `Live` | `Long` | `3.42` | 6,930,000.00 USD | 0.00 USD | 13,630.00 USD | `-20.80%` | `3,979.80` |
| `Live` | `Long` | `3.44` | 6,920,000.00 USD | 0.00 USD | 29,830.00 USD | `-20.57%` | `8,683.80` |
| `Live` | `Long` | `3.44` | 6,890,000.00 USD | 0.00 USD | 26,540.00 USD | `-20.34%` | `7,703.10` |
| `Live` | `Long` | `3.46` | 6,860,000.00 USD | 0.00 USD | 150,240.00 USD | `-20.10%` | `43,486.10` |
| `Live` | `Long` | `3.46` | 6,710,000.00 USD | 0.00 USD | 16,470.00 USD | `-19.87%` | `4,754.00` |
| `Live` | `Long` | `3.48` | 6,700,000.00 USD | 0.00 USD | 108,220.00 USD | `-19.64%` | `31,141.30` |
| `Live` | `Long` | `3.48` | 6,590,000.00 USD | 0.00 USD | 30,100.00 USD | `-19.41%` | `8,635.80` |
| `Live` | `Long` | `3.50` | 6,560,000.00 USD | 0.00 USD | 48,550.00 USD | `-19.18%` | `13,891.50` |
| `Live` | `Long` | `3.50` | 6,510,000.00 USD | 0.00 USD | 68,770.00 USD | `-18.95%` | `19,621.10` |
| `Live` | `Long` | `3.52` | 6,440,000.00 USD | 0.00 USD | 42,280.00 USD | `-18.72%` | `12,028.70` |
| `Live` | `Long` | `3.52` | 6,400,000.00 USD | 0.00 USD | 21,620.00 USD | `-18.49%` | `6,133.60` |
| `Live` | `Long` | `3.54` | 6,380,000.00 USD | 0.00 USD | 84,160.00 USD | `-18.25%` | `23,807.00` |
| `Live` | `Long` | `3.54` | 6,290,000.00 USD | 0.00 USD | 152,250.00 USD | `-18.02%` | `42,948.30` |
| `Live` | `Long` | `3.56` | 6,140,000.00 USD | 0.00 USD | 570,020.00 USD | `-17.79%` | `160,343.30` |
| `Live` | `Long` | `3.56` | 5,570,000.00 USD | 0.00 USD | 25,750.00 USD | `-17.56%` | `7,223.40` |
| `Live` | `Long` | `3.58` | 5,550,000.00 USD | 0.00 USD | 1,340,000.00 USD | `-17.33%` | `373,803.30` |
| `Live` | `Long` | `3.58` | 4,210,000.00 USD | 0.00 USD | 120,640.00 USD | `-17.10%` | `33,652.60` |
| `Live` | `Long` | `3.60` | 4,090,000.00 USD | 0.00 USD | 24,010.00 USD | `-16.87%` | `6,680.00` |
| `Live` | `Long` | `3.60` | 4,060,000.00 USD | 0.00 USD | 72,910.00 USD | `-16.64%` | `20,224.70` |
| `Live` | `Long` | `3.62` | 3,990,000.00 USD | 0.00 USD | 229,270.00 USD | `-16.40%` | `63,422.10` |
| `Live` | `Long` | `3.62` | 3,760,000.00 USD | 0.00 USD | 125,580.00 USD | `-16.17%` | `34,643.60` |
| `Live` | `Long` | `3.63` | 3,640,000.00 USD | 0.00 USD | 3,550.00 USD | `-15.94%` | `975.40` |
| `Live` | `Long` | `3.65` | 3,630,000.00 USD | 0.00 USD | 15,050.00 USD | `-15.71%` | `4,128.20` |
| `Live` | `Long` | `3.65` | 3,620,000.00 USD | 0.00 USD | 20,860.00 USD | `-15.48%` | `5,706.00` |
| `Live` | `Long` | `3.67` | 3,600,000.00 USD | 0.00 USD | 39,720.00 USD | `-15.25%` | `10,837.40` |
| `Live` | `Long` | `3.67` | 3,560,000.00 USD | 0.00 USD | 94,680.00 USD | `-15.02%` | `25,762.00` |
| `Live` | `Long` | `3.69` | 3,460,000.00 USD | 0.00 USD | 217,880.00 USD | `-14.79%` | `59,126.00` |
| `Live` | `Long` | `3.69` | 3,240,000.00 USD | 0.00 USD | 102,030.00 USD | `-14.55%` | `27,612.70` |
| `Live` | `Long` | `3.71` | 3,140,000.00 USD | 0.00 USD | 90,780.00 USD | `-14.32%` | `24,501.50` |
| `Live` | `Long` | `3.71` | 3,050,000.00 USD | 0.00 USD | 12,740.00 USD | `-14.09%` | `3,428.30` |
| `Live` | `Long` | `3.73` | 3,040,000.00 USD | 0.00 USD | 355,230.00 USD | `-13.86%` | `95,364.50` |
| `Live` | `Long` | `3.73` | 2,680,000.00 USD | 0.00 USD | 123,790.00 USD | `-13.63%` | `33,143.60` |
| `Live` | `Long` | `3.75` | 2,560,000.00 USD | 0.00 USD | 24,210.00 USD | `-13.40%` | `6,464.40` |
| `Live` | `Long` | `3.75` | 2,540,000.00 USD | 0.00 USD | 150,270.00 USD | `-13.17%` | `40,017.50` |
| `Live` | `Long` | `3.77` | 2,390,000.00 USD | 0.00 USD | 65,190.00 USD | `-12.94%` | `17,315.20` |
| `Live` | `Long` | `3.77` | 2,320,000.00 USD | 0.00 USD | 123,660.00 USD | `-12.70%` | `32,757.30` |
| `Live` | `Long` | `3.79` | 2,200,000.00 USD | 0.00 USD | 48,560.00 USD | `-12.47%` | `12,829.90` |
| `Live` | `Long` | `3.79` | 2,150,000.00 USD | 0.00 USD | 34,520.00 USD | `-12.24%` | `9,097.00` |
| `Live` | `Long` | `3.81` | 2,110,000.00 USD | 0.00 USD | 585,450.00 USD | `-12.01%` | `153,864.10` |
| `Live` | `Long` | `3.81` | 1,530,000.00 USD | 0.00 USD | 10,980.00 USD | `-11.78%` | `2,878.90` |
| `Live` | `Long` | `3.83` | 1,520,000.00 USD | 0.00 USD | 181,850.00 USD | `-11.55%` | `47,542.20` |
| `Live` | `Long` | `3.83` | 1,340,000.00 USD | 0.00 USD | 171,380.00 USD | `-11.32%` | `44,688.70` |
| `Live` | `Long` | `3.85` | 1,160,000.00 USD | 0.00 USD | 119,620.00 USD | `-11.09%` | `31,111.10` |
| `Live` | `Long` | `3.85` | 1,040,000.00 USD | 0.00 USD | 22,330.00 USD | `-10.85%` | `5,792.70` |
| `Live` | `Long` | `3.87` | 1,020,000.00 USD | 0.00 USD | 71,550.00 USD | `-10.62%` | `18,512.20` |
| `Live` | `Long` | `3.88` | 950,740.00 USD | 0.00 USD | 8,130.00 USD | `-10.39%` | `2,097.40` |
| `Live` | `Long` | `3.88` | 942,610.00 USD | 0.00 USD | 173,140.00 USD | `-10.16%` | `44,567.00` |
| `Live` | `Long` | `3.90` | 769,470.00 USD | 0.00 USD | 93,930.00 USD | `-9.93%` | `24,116.30` |
| `Live` | `Long` | `3.90` | 675,530.00 USD | 0.00 USD | 7,990.00 USD | `-9.70%` | `2,047.30` |
| `Live` | `Long` | `3.92` | 667,540.00 USD | 0.00 USD | 37,030.00 USD | `-9.47%` | `9,458.00` |
| `Live` | `Long` | `3.92` | 630,510.00 USD | 0.00 USD | 2,050.00 USD | `-9.24%` | `522.20` |
| `Live` | `Long` | `3.94` | 628,460.00 USD | 0.00 USD | 17,100.00 USD | `-9.00%` | `4,346.00` |
| `Live` | `Long` | `3.94` | 611,360.00 USD | 0.00 USD | 149,880.00 USD | `-8.77%` | `37,992.30` |
| `Live` | `Long` | `3.96` | 461,480.00 USD | 0.00 USD | 56,160.00 USD | `-8.54%` | `14,200.30` |
| `Live` | `Long` | `3.96` | 405,320.00 USD | 0.00 USD | 1,240.00 USD | `-8.31%` | `311.90` |
| `Live` | `Long` | `3.98` | 404,080.00 USD | 0.00 USD | 82,400.00 USD | `-8.08%` | `20,729.90` |
| `Live` | `Long` | `3.98` | 321,680.00 USD | 0.00 USD | 5,650.00 USD | `-7.85%` | `1,417.40` |
| `Live` | `Long` | `4.00` | 316,030.00 USD | 0.00 USD | 160,840.00 USD | `-7.62%` | `40,260.30` |
| `Live` | `Long` | `4.00` | 155,190.00 USD | 0.00 USD | 11,990.00 USD | `-7.39%` | `2,993.80` |
| `Live` | `Long` | `4.01` | 143,200.00 USD | 0.00 USD | 275.83 USD | `-7.15%` | `68.70` |
| `Live` | `Long` | `4.03` | 142,930.00 USD | 0.00 USD | 1,910.00 USD | `-6.92%` | `473.70` |
| `Live` | `Long` | `4.04` | 141,020.00 USD | 0.00 USD | 25,700.00 USD | `-6.69%` | `6,368.40` |
| `Live` | `Long` | `4.04` | 115,320.00 USD | 0.00 USD | 32,100.00 USD | `-6.46%` | `7,936.70` |
| `Live` | `Long` | `4.05` | 83,220.00 USD | 0.00 USD | 4,380.00 USD | `-6.23%` | `1,079.20` |
| `Live` | `Long` | `4.07` | 78,840.00 USD | 0.00 USD | 1,200.00 USD | `-6.00%` | `295.00` |
| `Live` | `Long` | `4.08` | 77,640.00 USD | 0.00 USD | 10,210.00 USD | `-5.77%` | `2,505.20` |
| `Live` | `Long` | `4.08` | 67,430.00 USD | 0.00 USD | 5,330.00 USD | `-5.54%` | `1,304.00` |
| `Live` | `Long` | `4.09` | 62,110.00 USD | 0.00 USD | 17,640.00 USD | `-5.30%` | `4,307.40` |
| `Live` | `Long` | `4.11` | 44,470.00 USD | 0.00 USD | 15,640.00 USD | `-5.07%` | `3,809.30` |
| `Live` | `Long` | `4.12` | 28,830.00 USD | 0.00 USD | 17,630.00 USD | `-4.84%` | `4,284.60` |
| `Live` | `Long` | `4.12` | 11,200.00 USD | 0.00 USD | 11,200.00 USD | `-4.61%` | `2,715.40` |
| `Live` | `Short` | `4.17` | 8,230.00 USD | 8,230.00 USD | 0.00 USD | `-3.69%` | `1,975.90` |
| `Live` | `Short` | `4.21` | 10,000.00 USD | 1,770.00 USD | 0.00 USD | `-2.53%` | `420.00` |
| `Live` | `Short` | `4.29` | 11,080.00 USD | 1,080.00 USD | 0.00 USD | `-0.68%` | `251.30` |
| `Live` | `Short` | `4.36` | 14,130.00 USD | 3,050.00 USD | 0.00 USD | `+0.71%` | `701.00` |
| `Live` | `Short` | `4.38` | 97,690.00 USD | 83,560.00 USD | 0.00 USD | `+1.17%` | `19,099.00` |
| `Live` | `Short` | `4.39` | 278,450.00 USD | 180,760.00 USD | 0.00 USD | `+1.63%` | `41,128.80` |
| `Live` | `Short` | `4.42` | 278,960.00 USD | 507.73 USD | 0.00 USD | `+2.10%` | `115.00` |
| `Live` | `Short` | `4.42` | 280,890.00 USD | 1,930.00 USD | 0.00 USD | `+2.33%` | `436.00` |
| `Live` | `Short` | `4.43` | 285,320.00 USD | 4,430.00 USD | 0.00 USD | `+2.56%` | `999.90` |
| `Live` | `Short` | `4.45` | 285,680.00 USD | 358.27 USD | 0.00 USD | `+2.79%` | `80.60` |
| `Live` | `Short` | `4.46` | 324,530.00 USD | 38,840.00 USD | 0.00 USD | `+3.02%` | `8,719.30` |
| `Live` | `Short` | `4.46` | 325,900.00 USD | 1,370.00 USD | 0.00 USD | `+3.25%` | `306.90` |
| `Live` | `Short` | `4.47` | 343,290.00 USD | 17,400.00 USD | 0.00 USD | `+3.48%` | `3,887.90` |
| `Live` | `Short` | `4.49` | 345,320.00 USD | 2,030.00 USD | 0.00 USD | `+3.71%` | `452.20` |
| `Live` | `Short` | `4.50` | 368,000.00 USD | 22,680.00 USD | 0.00 USD | `+3.95%` | `5,044.50` |
| `Live` | `Short` | `4.50` | 369,530.00 USD | 1,530.00 USD | 0.00 USD | `+4.18%` | `340.10` |
| `Live` | `Short` | `4.51` | 382,800.00 USD | 13,270.00 USD | 0.00 USD | `+4.41%` | `2,939.10` |
| `Live` | `Short` | `4.53` | 383,620.00 USD | 819.48 USD | 0.00 USD | `+4.64%` | `181.10` |
| `Live` | `Short` | `4.54` | 384,590.00 USD | 965.96 USD | 0.00 USD | `+4.87%` | `213.00` |
| `Live` | `Short` | `4.54` | 408,850.00 USD | 24,260.00 USD | 0.00 USD | `+5.10%` | `5,338.60` |
| `Live` | `Short` | `4.55` | 529,770.00 USD | 120,920.00 USD | 0.00 USD | `+5.33%` | `26,547.00` |
| `Live` | `Short` | `4.57` | 712,370.00 USD | 182,600.00 USD | 0.00 USD | `+5.56%` | `40,000.00` |
| `Live` | `Short` | `4.58` | 714,510.00 USD | 2,140.00 USD | 0.00 USD | `+6.03%` | `467.20` |
| `Live` | `Short` | `4.62` | 766,200.00 USD | 51,690.00 USD | 0.00 USD | `+6.95%` | `11,176.20` |
| `Live` | `Short` | `4.63` | 767,190.00 USD | 990.04 USD | 0.00 USD | `+7.18%` | `213.60` |
| `Live` | `Short` | `4.64` | 775,640.00 USD | 8,450.00 USD | 0.00 USD | `+7.41%` | `1,819.00` |
| `Live` | `Short` | `4.66` | 926,320.00 USD | 150,680.00 USD | 0.00 USD | `+7.64%` | `32,369.90` |
| `Live` | `Short` | `4.67` | 926,430.00 USD | 101.70 USD | 0.00 USD | `+7.88%` | `21.80` |
| `Live` | `Short` | `4.67` | 980,710.00 USD | 54,290.00 USD | 0.00 USD | `+8.11%` | `11,612.70` |
| `Live` | `Short` | `4.68` | 981,750.00 USD | 1,030.00 USD | 0.00 USD | `+8.34%` | `220.50` |
| `Live` | `Short` | `4.70` | 981,980.00 USD | 230.06 USD | 0.00 USD | `+8.57%` | `49.00` |
| `Live` | `Short` | `4.71` | 989,460.00 USD | 7,480.00 USD | 0.00 USD | `+8.80%` | `1,590.30` |
| `Live` | `Short` | `4.72` | 992,050.00 USD | 2,590.00 USD | 0.00 USD | `+9.26%` | `547.30` |
| `Live` | `Short` | `4.74` | 995,430.00 USD | 3,380.00 USD | 0.00 USD | `+9.49%` | `714.50` |
| `Live` | `Short` | `4.75` | 1,110,000.00 USD | 111,130.00 USD | 0.00 USD | `+9.73%` | `23,421.00` |
| `Live` | `Short` | `4.76` | 1,110,000.00 USD | 5,980.00 USD | 0.00 USD | `+10.19%` | `1,254.10` |
| `Live` | `Short` | `4.78` | 1,110,000.00 USD | 1,730.00 USD | 0.00 USD | `+10.42%` | `362.40` |
| `Live` | `Short` | `4.79` | 1,110,000.00 USD | 143.55 USD | 0.00 USD | `+10.65%` | `30.00` |
| `Live` | `Short` | `4.79` | 1,120,000.00 USD | 1,330.00 USD | 0.00 USD | `+10.88%` | `277.70` |
| `Live` | `Short` | `4.83` | 1,120,000.00 USD | 2,360.00 USD | 0.00 USD | `+11.58%` | `489.00` |
| `Live` | `Short` | `4.83` | 1,120,000.00 USD | 1,540.00 USD | 0.00 USD | `+11.81%` | `317.90` |
| `Live` | `Short` | `4.84` | 1,130,000.00 USD | 11,220.00 USD | 0.00 USD | `+12.04%` | `2,316.40` |
| `Live` | `Short` | `4.87` | 1,130,000.00 USD | 259.79 USD | 0.00 USD | `+12.50%` | `53.40` |
| `Live` | `Short` | `4.88` | 1,130,000.00 USD | 827.03 USD | 0.00 USD | `+12.96%` | `169.30` |
| `Live` | `Short` | `4.91` | 1,130,000.00 USD | 674.44 USD | 0.00 USD | `+13.43%` | `137.50` |
| `Live` | `Short` | `4.92` | 1,150,000.00 USD | 20,720.00 USD | 0.00 USD | `+13.66%` | `4,214.80` |
| `Live` | `Short` | `4.92` | 1,160,000.00 USD | 2,100.00 USD | 0.00 USD | `+13.89%` | `425.70` |
| `Live` | `Short` | `4.93` | 1,160,000.00 USD | 157.43 USD | 0.00 USD | `+14.12%` | `31.90` |
| `Live` | `Short` | `4.95` | 1,160,000.00 USD | 2,060.00 USD | 0.00 USD | `+14.35%` | `417.10` |
| `Live` | `Short` | `4.96` | 1,160,000.00 USD | 488.56 USD | 0.00 USD | `+14.58%` | `98.60` |
| `Live` | `Short` | `4.97` | 1,260,000.00 USD | 99,370.00 USD | 0.00 USD | `+15.04%` | `19,974.00` |
| `Live` | `Short` | `5.01` | 1,290,000.00 USD | 36,420.00 USD | 0.00 USD | `+15.97%` | `7,262.50` |
| `Live` | `Short` | `5.04` | 1,290,000.00 USD | 118.83 USD | 0.00 USD | `+16.43%` | `23.60` |
| `Live` | `Short` | `5.05` | 1,330,000.00 USD | 35,380.00 USD | 0.00 USD | `+16.89%` | `6,998.80` |
| `Live` | `Short` | `5.07` | 1,330,000.00 USD | 3,420.00 USD | 0.00 USD | `+17.13%` | `675.80` |
| `Live` | `Short` | `5.11` | 1,330,000.00 USD | 177.14 USD | 0.00 USD | `+18.05%` | `34.70` |
| `Live` | `Short` | `5.12` | 1,340,000.00 USD | 5,710.00 USD | 0.00 USD | `+18.28%` | `1,115.40` |
| `Live` | `Short` | `5.12` | 1,390,000.00 USD | 51,250.00 USD | 0.00 USD | `+18.51%` | `10,000.00` |
| `Live` | `Short` | `5.17` | 1,390,000.00 USD | 3,330.00 USD | 0.00 USD | `+19.44%` | `645.50` |
| `Live` | `Short` | `5.20` | 1,400,000.00 USD | 11,250.00 USD | 0.00 USD | `+20.13%` | `2,166.50` |
| `Live` | `Short` | `5.22` | 1,480,000.00 USD | 73,780.00 USD | 0.00 USD | `+20.83%` | `14,120.50` |
| `Live` | `Short` | `5.25` | 1,480,000.00 USD | 143.71 USD | 0.00 USD | `+21.29%` | `27.40` |
| `Live` | `Short` | `5.25` | 1,500,000.00 USD | 17,380.00 USD | 0.00 USD | `+21.52%` | `3,307.90` |
| `Live` | `Short` | `5.26` | 1,520,000.00 USD | 21,280.00 USD | 0.00 USD | `+21.75%` | `4,042.60` |
| `Live` | `Short` | `5.28` | 1,520,000.00 USD | 608.21 USD | 0.00 USD | `+21.98%` | `115.30` |
| `Live` | `Short` | `5.29` | 2,570,000.00 USD | 1,060,000.00 USD | 0.00 USD | `+22.21%` | `200,025.50` |
| `Live` | `Short` | `5.29` | 2,620,000.00 USD | 41,410.00 USD | 0.00 USD | `+22.44%` | `7,820.30` |
| `Live` | `Short` | `5.30` | 2,620,000.00 USD | 524.66 USD | 0.00 USD | `+22.68%` | `98.90` |
| `Live` | `Short` | `5.32` | 2,620,000.00 USD | 147.23 USD | 0.00 USD | `+22.91%` | `27.70` |
| `Live` | `Short` | `5.33` | 2,620,000.00 USD | 286.49 USD | 0.00 USD | `+23.37%` | `53.70` |
| `Live` | `Short` | `5.34` | 2,960,000.00 USD | 338,680.00 USD | 0.00 USD | `+23.60%` | `63,364.20` |
| `Live` | `Short` | `5.36` | 2,960,000.00 USD | 5,940.00 USD | 0.00 USD | `+23.83%` | `1,108.50` |
| `Live` | `Short` | `5.38` | 2,960,000.00 USD | 182.21 USD | 0.00 USD | `+24.29%` | `33.90` |
| `Live` | `Short` | `5.42` | 2,960,000.00 USD | 1,030.00 USD | 0.00 USD | `+25.22%` | `189.60` |
| `Live` | `Short` | `5.42` | 2,960,000.00 USD | 914.65 USD | 0.00 USD | `+25.45%` | `168.60` |
| `Live` | `Short` | `5.43` | 2,960,000.00 USD | 419.04 USD | 0.00 USD | `+25.68%` | `77.10` |
| `Live` | `Short` | `5.47` | 2,970,000.00 USD | 7,840.00 USD | 0.00 USD | `+26.61%` | `1,432.70` |
| `Live` | `Short` | `5.49` | 2,990,000.00 USD | 12,740.00 USD | 0.00 USD | `+26.84%` | `2,322.30` |
| `Live` | `Short` | `5.50` | 3,050,000.00 USD | 66,470.00 USD | 0.00 USD | `+27.07%` | `12,097.30` |
| `Live` | `Short` | `5.50` | 3,110,000.00 USD | 62,990.00 USD | 0.00 USD | `+27.30%` | `11,443.00` |
| `Live` | `Short` | `5.51` | 3,150,000.00 USD | 38,800.00 USD | 0.00 USD | `+27.53%` | `7,034.90` |
| `Live` | `Short` | `5.53` | 3,150,000.00 USD | 1,270.00 USD | 0.00 USD | `+27.76%` | `229.80` |
| `Live` | `Short` | `5.54` | 3,150,000.00 USD | 209.22 USD | 0.00 USD | `+27.99%` | `37.80` |
| `Live` | `Short` | `5.57` | 3,160,000.00 USD | 9,360.00 USD | 0.00 USD | `+28.69%` | `1,682.60` |
| `Live` | `Short` | `5.58` | 3,230,000.00 USD | 62,420.00 USD | 0.00 USD | `+29.15%` | `11,175.80` |
| `Live` | `Short` | `5.62` | 7,200,000.00 USD | 3,980,000.00 USD | 0.00 USD | `+30.08%` | `706,994.70` |
| `Live` | `Short` | `5.66` | 8,830,000.00 USD | 1,630,000.00 USD | 0.00 USD | `+30.77%` | `288,027.90` |
| `Live` | `Short` | `5.67` | 8,830,000.00 USD | 211.30 USD | 0.00 USD | `+31.00%` | `37.30` |
| `Live` | `Short` | `5.67` | 8,830,000.00 USD | 228.70 USD | 0.00 USD | `+31.23%` | `40.30` |
| `Live` | `Short` | `5.68` | 8,860,000.00 USD | 26,090.00 USD | 0.00 USD | `+31.46%` | `4,589.50` |
| `Live` | `Short` | `5.70` | 8,860,000.00 USD | 1,520.00 USD | 0.00 USD | `+31.69%` | `267.40` |
| `Live` | `Short` | `5.71` | 8,860,000.00 USD | 2,130.00 USD | 0.00 USD | `+32.16%` | `372.40` |
| `Live` | `Short` | `5.75` | 8,870,000.00 USD | 4,580.00 USD | 0.00 USD | `+32.85%` | `796.90` |
| `Live` | `Short` | `5.75` | 8,870,000.00 USD | 3,020.00 USD | 0.00 USD | `+33.08%` | `524.10` |
| `Live` | `Short` | `5.76` | 9,350,000.00 USD | 475,940.00 USD | 0.00 USD | `+33.31%` | `82,556.10` |
| `Live` | `Short` | `5.83` | 9,350,000.00 USD | 198.97 USD | 0.00 USD | `+34.93%` | `34.10` |
| `Live` | `Short` | `5.84` | 9,620,000.00 USD | 270,530.00 USD | 0.00 USD | `+35.16%` | `46,283.90` |
| `Live` | `Short` | `5.86` | 9,620,000.00 USD | 848.39 USD | 0.00 USD | `+35.39%` | `144.90` |
| `Live` | `Short` | `5.88` | 9,620,000.00 USD | 7,150.00 USD | 0.00 USD | `+36.09%` | `1,215.40` |
| `Live` | `Short` | `5.89` | 9,710,000.00 USD | 88,420.00 USD | 0.00 USD | `+36.32%` | `15,000.00` |
| `Live` | `Short` | `5.91` | 9,710,000.00 USD | 162.98 USD | 0.00 USD | `+36.55%` | `27.60` |
| `Live` | `Short` | `5.92` | 9,710,000.00 USD | 189.28 USD | 0.00 USD | `+36.78%` | `32.00` |
| `Live` | `Short` | `5.92` | 9,710,000.00 USD | 130.35 USD | 0.00 USD | `+37.01%` | `22.00` |
| `Live` | `Short` | `5.95` | 9,820,000.00 USD | 103,650.00 USD | 0.00 USD | `+37.48%` | `17,434.80` |
| `Live` | `Short` | `6.03` | 9,840,000.00 USD | 23,060.00 USD | 0.00 USD | `+39.33%` | `3,827.40` |
| `Live` | `Short` | `6.05` | 9,860,000.00 USD | 23,520.00 USD | 0.00 USD | `+40.02%` | `3,883.80` |
| `Live` | `Short` | `6.07` | 9,860,000.00 USD | 740.54 USD | 0.00 USD | `+40.25%` | `122.10` |
| `Live` | `Short` | `6.08` | 9,870,000.00 USD | 5,920.00 USD | 0.00 USD | `+40.71%` | `973.10` |
| `Live` | `Short` | `6.09` | 9,910,000.00 USD | 37,510.00 USD | 0.00 USD | `+40.94%` | `6,154.10` |
| `Live` | `Short` | `6.12` | 9,910,000.00 USD | 1,870.00 USD | 0.00 USD | `+41.64%` | `305.00` |
| `Live` | `Short` | `6.13` | 9,910,000.00 USD | 2,430.00 USD | 0.00 USD | `+41.87%` | `396.10` |
| `Live` | `Short` | `6.18` | 9,950,000.00 USD | 35,350.00 USD | 0.00 USD | `+43.03%` | `5,715.90` |
| `Live` | `Short` | `6.21` | 10,280,000.00 USD | 332,230.00 USD | 0.00 USD | `+43.49%` | `53,541.50` |
| `Live` | `Short` | `6.24` | 10,810,000.00 USD | 526,230.00 USD | 0.00 USD | `+44.18%` | `84,400.00` |
| `Live` | `Short` | `6.25` | 10,810,000.00 USD | 7,300.00 USD | 0.00 USD | `+44.41%` | `1,168.90` |
| `Live` | `Short` | `6.25` | 10,810,000.00 USD | 439.10 USD | 0.00 USD | `+44.64%` | `70.20` |
| `Live` | `Short` | `6.26` | 11,070,000.00 USD | 256,050.00 USD | 0.00 USD | `+44.88%` | `40,869.30` |
| `Live` | `Short` | `6.30` | 11,070,000.00 USD | 2,020.00 USD | 0.00 USD | `+45.80%` | `320.30` |
| `Live` | `Short` | `6.32` | 11,080,000.00 USD | 8,430.00 USD | 0.00 USD | `+46.03%` | `1,335.70` |
| `Live` | `Short` | `6.33` | 11,080,000.00 USD | 382.00 USD | 0.00 USD | `+46.49%` | `60.30` |
| `Live` | `Short` | `6.34` | 11,080,000.00 USD | 214.46 USD | 0.00 USD | `+46.73%` | `33.80` |
| `Live` | `Short` | `6.37` | 11,080,000.00 USD | 113.93 USD | 0.00 USD | `+47.19%` | `17.90` |
| `Live` | `Short` | `6.38` | 11,080,000.00 USD | 288.15 USD | 0.00 USD | `+47.42%` | `45.20` |
| `Live` | `Short` | `6.39` | 11,080,000.00 USD | 2,000.00 USD | 0.00 USD | `+47.88%` | `312.80` |
| `Live` | `Short` | `6.41` | 11,100,000.00 USD | 15,590.00 USD | 0.00 USD | `+48.11%` | `2,434.70` |
| `Live` | `Short` | `6.42` | 11,100,000.00 USD | 943.65 USD | 0.00 USD | `+48.34%` | `147.10` |
| `Live` | `Short` | `6.42` | 11,110,000.00 USD | 5,650.00 USD | 0.00 USD | `+48.58%` | `879.80` |
| `Live` | `Short` | `6.45` | 11,110,000.00 USD | 5,270.00 USD | 0.00 USD | `+49.04%` | `818.40` |
| `Live` | `Short` | `6.46` | 11,120,000.00 USD | 7,150.00 USD | 0.00 USD | `+49.27%` | `1,107.10` |
| `Live` | `Short` | `6.46` | 11,120,000.00 USD | 1,940.00 USD | 0.00 USD | `+49.50%` | `300.00` |
| `Live` | `Short` | `6.51` | 11,120,000.00 USD | 380.48 USD | 0.00 USD | `+50.66%` | `58.40` |
| `Live` | `Short` | `6.54` | 12,360,000.00 USD | 1,240,000.00 USD | 0.00 USD | `+51.35%` | `189,207.50` |
| `Live` | `Short` | `6.57` | 41,950,000.00 USD | 29,590,000.00 USD | 0.00 USD | `+51.81%` | `4,507,262.50` |
| `Live` | `Short` | `6.59` | 41,950,000.00 USD | 418.78 USD | 0.00 USD | `+52.51%` | `63.50` |
| `Live` | `Short` | `6.61` | 42,330,000.00 USD | 382,680.00 USD | 0.00 USD | `+52.74%` | `57,938.40` |
| `Live` | `Short` | `6.64` | 42,370,000.00 USD | 41,250.00 USD | 0.00 USD | `+53.66%` | `6,207.00` |
| `Live` | `Short` | `6.66` | 42,380,000.00 USD | 7,230.00 USD | 0.00 USD | `+53.89%` | `1,086.90` |
| `Live` | `Short` | `6.67` | 42,380,000.00 USD | 233.94 USD | 0.00 USD | `+54.13%` | `35.10` |
| `Live` | `Short` | `6.67` | 42,380,000.00 USD | 200.25 USD | 0.00 USD | `+54.36%` | `30.00` |
| `Live` | `Short` | `6.71` | 42,420,000.00 USD | 37,260.00 USD | 0.00 USD | `+55.05%` | `5,556.90` |
| `Live` | `Short` | `6.72` | 42,420,000.00 USD | 713.52 USD | 0.00 USD | `+55.51%` | `106.10` |
| `Live` | `Short` | `6.75` | 43,670,000.00 USD | 1,250,000.00 USD | 0.00 USD | `+56.21%` | `184,501.00` |
| `Live` | `Short` | `6.80` | 43,670,000.00 USD | 5,260.00 USD | 0.00 USD | `+57.36%` | `772.70` |
| `Live` | `Short` | `6.82` | 43,670,000.00 USD | 344.16 USD | 0.00 USD | `+57.59%` | `50.50` |
| `Live` | `Short` | `6.83` | 43,760,000.00 USD | 91,230.00 USD | 0.00 USD | `+57.83%` | `13,367.10` |
| `Live` | `Short` | `6.84` | 43,760,000.00 USD | 753.63 USD | 0.00 USD | `+58.29%` | `110.10` |
| `Live` | `Short` | `6.87` | 43,770,000.00 USD | 2,650.00 USD | 0.00 USD | `+58.75%` | `386.60` |
| `Live` | `Short` | `6.92` | 43,770,000.00 USD | 6,920.00 USD | 0.00 USD | `+60.14%` | `1,000.00` |
| `Live` | `Short` | `6.96` | 43,800,000.00 USD | 24,540.00 USD | 0.00 USD | `+61.06%` | `3,523.00` |
| `Live` | `Short` | `6.99` | 43,800,000.00 USD | 664.27 USD | 0.00 USD | `+61.53%` | `95.10` |
| `Live` | `Short` | `7.03` | 43,800,000.00 USD | 665.27 USD | 0.00 USD | `+62.45%` | `94.70` |
| `Live` | `Short` | `7.08` | 43,800,000.00 USD | 996.15 USD | 0.00 USD | `+63.84%` | `140.60` |
| `Live` | `Short` | `7.09` | 43,800,000.00 USD | 699.57 USD | 0.00 USD | `+64.07%` | `98.60` |
| `Live` | `Short` | `7.14` | 43,820,000.00 USD | 15,990.00 USD | 0.00 USD | `+65.23%` | `2,237.40` |
| `Live` | `Short` | `7.21` | 43,830,000.00 USD | 13,560.00 USD | 0.00 USD | `+66.84%` | `1,879.60` |
| `Live` | `Short` | `7.24` | 47,670,000.00 USD | 3,840,000.00 USD | 0.00 USD | `+67.31%` | `531,159.30` |
| `Live` | `Short` | `7.25` | 47,680,000.00 USD | 3,770.00 USD | 0.00 USD | `+67.54%` | `520.00` |
| `Live` | `Short` | `7.25` | 47,680,000.00 USD | 575.32 USD | 0.00 USD | `+67.77%` | `79.30` |
| `Live` | `Short` | `7.30` | 47,680,000.00 USD | 3,520.00 USD | 0.00 USD | `+68.93%` | `481.50` |
| `Live` | `Short` | `7.32` | 47,730,000.00 USD | 54,860.00 USD | 0.00 USD | `+69.16%` | `7,500.00` |
| `Live` | `Short` | `7.33` | 47,740,000.00 USD | 1,320.00 USD | 0.00 USD | `+69.62%` | `180.00` |
| `Live` | `Short` | `7.34` | 47,800,000.00 USD | 59,770.00 USD | 0.00 USD | `+69.85%` | `8,137.40` |
| `Live` | `Short` | `7.38` | 47,810,000.00 USD | 12,910.00 USD | 0.00 USD | `+70.54%` | `1,750.00` |
| `Live` | `Short` | `7.41` | 47,810,000.00 USD | 776.04 USD | 0.00 USD | `+71.24%` | `104.80` |
| `Live` | `Short` | `7.43` | 47,920,000.00 USD | 106,150.00 USD | 0.00 USD | `+71.93%` | `14,276.50` |
| `Live` | `Short` | `7.46` | 47,920,000.00 USD | 1,420.00 USD | 0.00 USD | `+72.39%` | `191.10` |
| `Live` | `Short` | `7.46` | 57,890,000.00 USD | 9,970,000.00 USD | 0.00 USD | `+72.63%` | `1,336,000.00` |
| `Live` | `Short` | `7.53` | 65,720,000.00 USD | 7,820,000.00 USD | 0.00 USD | `+74.01%` | `1,039,813.00` |
| `Live` | `Short` | `7.54` | 65,720,000.00 USD | 3,100.00 USD | 0.00 USD | `+74.24%` | `411.40` |
| `Live` | `Short` | `7.62` | 65,750,000.00 USD | 35,860.00 USD | 0.00 USD | `+76.09%` | `4,708.50` |
| `Live` | `Short` | `7.63` | 65,770,000.00 USD | 19,210.00 USD | 0.00 USD | `+76.56%` | `2,516.10` |
| `Live` | `Short` | `7.64` | 65,800,000.00 USD | 23,890.00 USD | 0.00 USD | `+76.79%` | `3,124.90` |
| `Live` | `Short` | `7.66` | 65,820,000.00 USD | 20,000.00 USD | 0.00 USD | `+77.02%` | `2,612.80` |
| `Live` | `Short` | `7.67` | 65,840,000.00 USD | 27,160.00 USD | 0.00 USD | `+77.25%` | `3,543.50` |
| `Live` | `Short` | `7.72` | 65,840,000.00 USD | 259.56 USD | 0.00 USD | `+78.64%` | `33.60` |
| `Live` | `Short` | `7.74` | 65,850,000.00 USD | 4,970.00 USD | 0.00 USD | `+78.87%` | `642.60` |
| `Live` | `Short` | `7.75` | 65,850,000.00 USD | 629.67 USD | 0.00 USD | `+79.10%` | `81.30` |
| `Live` | `Short` | `7.76` | 65,860,000.00 USD | 11,760.00 USD | 0.00 USD | `+79.56%` | `1,514.20` |
| `Live` | `Short` | `7.82` | 65,860,000.00 USD | 1,690.00 USD | 0.00 USD | `+80.72%` | `216.50` |
| `Live` | `Short` | `7.86` | 65,860,000.00 USD | 120.18 USD | 0.00 USD | `+81.64%` | `15.30` |
| `Live` | `Short` | `7.87` | 65,870,000.00 USD | 2,980.00 USD | 0.00 USD | `+81.87%` | `378.70` |
| `Live` | `Short` | `7.95` | 65,870,000.00 USD | 6,120.00 USD | 0.00 USD | `+83.72%` | `769.80` |
| `Live` | `Short` | `7.96` | 65,870,000.00 USD | 166.26 USD | 0.00 USD | `+83.96%` | `20.90` |
| `Live` | `Short` | `7.96` | 65,970,000.00 USD | 95,580.00 USD | 0.00 USD | `+84.19%` | `12,000.00` |
| `Live` | `Short` | `7.99` | 65,970,000.00 USD | 399.25 USD | 0.00 USD | `+84.65%` | `50.00` |
| `Live` | `Short` | `8.03` | 66,400,000.00 USD | 435,420.00 USD | 0.00 USD | `+85.57%` | `54,257.40` |
| `Live` | `Short` | `8.04` | 66,400,000.00 USD | 259.05 USD | 0.00 USD | `+86.04%` | `32.20` |
| `Live` | `Short` | `8.07` | 66,410,000.00 USD | 6,460.00 USD | 0.00 USD | `+86.73%` | `800.00` |
| `Live` | `Short` | `8.20` | 66,410,000.00 USD | 951.44 USD | 0.00 USD | `+89.51%` | `116.10` |
| `Live` | `Short` | `8.24` | 66,480,000.00 USD | 62,980.00 USD | 0.00 USD | `+90.66%` | `7,638.50` |
| `Live` | `Short` | `8.31` | 66,480,000.00 USD | 8,640.00 USD | 0.00 USD | `+92.28%` | `1,039.60` |
| `Live` | `Short` | `8.35` | 66,510,000.00 USD | 25,310.00 USD | 0.00 USD | `+92.97%` | `3,032.60` |
| `Live` | `Short` | `8.37` | 67,610,000.00 USD | 1,100,000.00 USD | 0.00 USD | `+93.44%` | `131,528.10` |
| `Live` | `Short` | `8.38` | 67,610,000.00 USD | 191.79 USD | 0.00 USD | `+93.67%` | `22.90` |
| `Live` | `Short` | `8.41` | 67,610,000.00 USD | 1,220.00 USD | 0.00 USD | `+94.59%` | `145.00` |
| `Live` | `Short` | `8.46` | 67,660,000.00 USD | 53,330.00 USD | 0.00 USD | `+95.75%` | `6,300.00` |
| `Live` | `Short` | `8.47` | 67,660,000.00 USD | 816.99 USD | 0.00 USD | `+95.98%` | `96.40` |
| `Live` | `Short` | `8.48` | 67,670,000.00 USD | 6,640.00 USD | 0.00 USD | `+96.21%` | `782.50` |
| `Live` | `Short` | `8.49` | 67,700,000.00 USD | 25,490.00 USD | 0.00 USD | `+96.44%` | `3,000.00` |
| `Live` | `Short` | `8.53` | 67,730,000.00 USD | 34,680.00 USD | 0.00 USD | `+97.14%` | `4,068.00` |
| `Live` | `Short` | `8.54` | 67,730,000.00 USD | 127.17 USD | 0.00 USD | `+97.37%` | `14.90` |
| `Live` | `Short` | `8.54` | 67,730,000.00 USD | 124.76 USD | 0.00 USD | `+97.60%` | `14.60` |
| `Live` | `Short` | `8.55` | 68,160,000.00 USD | 430,710.00 USD | 0.00 USD | `+97.83%` | `50,346.40` |
| `Live` | `Short` | `8.59` | 68,160,000.00 USD | 240.38 USD | 0.00 USD | `+98.52%` | `28.00` |
| `Live` | `Short` | `8.60` | 68,180,000.00 USD | 17,660.00 USD | 0.00 USD | `+98.76%` | `2,054.80` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `1.00` | 3,060,000.00 USD | 0.00 USD | 585.51 USD | `-76.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.01` | 3,060,000.00 USD | 0.00 USD | 339.82 USD | `-76.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.20` | 3,060,000.00 USD | 0.00 USD | 196.58 USD | `-72.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.34` | 3,060,000.00 USD | 0.00 USD | 331.54 USD | `-68.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.35` | 3,060,000.00 USD | 0.00 USD | 345.25 USD | `-68.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.38` | 3,060,000.00 USD | 0.00 USD | 5,640.00 USD | `-68.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.40` | 3,050,000.00 USD | 0.00 USD | 997.29 USD | `-67.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.49` | 3,050,000.00 USD | 0.00 USD | 582.71 USD | `-65.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.51` | 3,050,000.00 USD | 0.00 USD | 139.83 USD | `-64.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.53` | 3,050,000.00 USD | 0.00 USD | 113.28 USD | `-64.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.54` | 3,050,000.00 USD | 0.00 USD | 4,000.00 USD | `-64.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.55` | 3,050,000.00 USD | 0.00 USD | 324.22 USD | `-64.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.59` | 3,050,000.00 USD | 0.00 USD | 4,590.00 USD | `-63.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.61` | 3,040,000.00 USD | 0.00 USD | 739.67 USD | `-62.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.62` | 3,040,000.00 USD | 0.00 USD | 1,740.00 USD | `-62.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.64` | 3,040,000.00 USD | 0.00 USD | 6,260.00 USD | `-62.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.66` | 3,040,000.00 USD | 0.00 USD | 345.40 USD | `-61.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.68` | 3,040,000.00 USD | 0.00 USD | 167.50 USD | `-61.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.70` | 3,030,000.00 USD | 0.00 USD | 669.02 USD | `-60.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.71` | 3,030,000.00 USD | 0.00 USD | 105.88 USD | `-60.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.73` | 3,030,000.00 USD | 0.00 USD | 172.50 USD | `-60.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.77` | 3,030,000.00 USD | 0.00 USD | 10,650.00 USD | `-58.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.80` | 3,020,000.00 USD | 0.00 USD | 722.00 USD | `-58.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.81` | 3,020,000.00 USD | 0.00 USD | 259.00 USD | `-58.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.82` | 3,020,000.00 USD | 0.00 USD | 103.84 USD | `-57.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.83` | 3,020,000.00 USD | 0.00 USD | 109.00 USD | `-57.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.88` | 3,020,000.00 USD | 0.00 USD | 222.19 USD | `-56.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.89` | 3,020,000.00 USD | 0.00 USD | 10,280.00 USD | `-56.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.91` | 3,010,000.00 USD | 0.00 USD | 558.36 USD | `-55.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.93` | 3,010,000.00 USD | 0.00 USD | 1,520.00 USD | `-55.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.94` | 3,010,000.00 USD | 0.00 USD | 222.14 USD | `-55.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.95` | 3,010,000.00 USD | 0.00 USD | 279.50 USD | `-55.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.98` | 3,010,000.00 USD | 0.00 USD | 197.50 USD | `-54.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.00` | 3,010,000.00 USD | 0.00 USD | 935.66 USD | `-53.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.00` | 3,010,000.00 USD | 0.00 USD | 18,860.00 USD | `-53.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.02` | 2,990,000.00 USD | 0.00 USD | 3,020.00 USD | `-53.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.04` | 2,990,000.00 USD | 0.00 USD | 214.52 USD | `-52.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.06` | 2,990,000.00 USD | 0.00 USD | 1,200.00 USD | `-52.48%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.06` | 2,980,000.00 USD | 0.00 USD | 578.41 USD | `-52.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.10` | 2,980,000.00 USD | 0.00 USD | 18,070.00 USD | `-51.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.10` | 2,970,000.00 USD | 0.00 USD | 108.62 USD | `-51.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.12` | 2,970,000.00 USD | 0.00 USD | 107.23 USD | `-51.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.12` | 2,970,000.00 USD | 0.00 USD | 1,590.00 USD | `-50.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.15` | 2,960,000.00 USD | 0.00 USD | 5,830.00 USD | `-50.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.15` | 2,960,000.00 USD | 0.00 USD | 310.32 USD | `-50.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.17` | 2,960,000.00 USD | 0.00 USD | 1,170.00 USD | `-49.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.19` | 2,960,000.00 USD | 0.00 USD | 576.18 USD | `-49.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.19` | 2,960,000.00 USD | 0.00 USD | 295.67 USD | `-49.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.21` | 2,960,000.00 USD | 0.00 USD | 1,430.00 USD | `-49.01%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.21` | 2,950,000.00 USD | 0.00 USD | 812.68 USD | `-48.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.23` | 2,950,000.00 USD | 0.00 USD | 1,440.00 USD | `-48.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.23` | 2,950,000.00 USD | 0.00 USD | 106.16 USD | `-48.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.25` | 2,950,000.00 USD | 0.00 USD | 6,270.00 USD | `-48.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.25` | 2,950,000.00 USD | 0.00 USD | 478.06 USD | `-47.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.27` | 2,950,000.00 USD | 0.00 USD | 540.88 USD | `-47.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.27` | 2,940,000.00 USD | 0.00 USD | 867.46 USD | `-47.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.29` | 2,940,000.00 USD | 0.00 USD | 759.76 USD | `-47.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.29` | 2,940,000.00 USD | 0.00 USD | 11,060.00 USD | `-46.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.31` | 2,930,000.00 USD | 0.00 USD | 3,690.00 USD | `-46.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.33` | 2,930,000.00 USD | 0.00 USD | 722.15 USD | `-46.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.33` | 2,930,000.00 USD | 0.00 USD | 467.00 USD | `-46.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.35` | 2,930,000.00 USD | 0.00 USD | 506.75 USD | `-45.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.37` | 2,930,000.00 USD | 0.00 USD | 214.27 USD | `-45.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.38` | 2,930,000.00 USD | 0.00 USD | 428.69 USD | `-45.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.38` | 2,930,000.00 USD | 0.00 USD | 322.45 USD | `-44.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.40` | 2,930,000.00 USD | 0.00 USD | 108.25 USD | `-44.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.40` | 2,930,000.00 USD | 0.00 USD | 3,900.00 USD | `-44.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.42` | 2,920,000.00 USD | 0.00 USD | 799.04 USD | `-43.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.44` | 2,920,000.00 USD | 0.00 USD | 6,830.00 USD | `-43.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.44` | 2,910,000.00 USD | 0.00 USD | 137.16 USD | `-43.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.48` | 2,910,000.00 USD | 0.00 USD | 504.41 USD | `-42.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.48` | 2,910,000.00 USD | 0.00 USD | 963.93 USD | `-42.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.50` | 2,910,000.00 USD | 0.00 USD | 6,690.00 USD | `-42.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.52` | 2,910,000.00 USD | 0.00 USD | 541.98 USD | `-41.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.54` | 2,910,000.00 USD | 0.00 USD | 108.75 USD | `-41.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.54` | 2,910,000.00 USD | 0.00 USD | 766.55 USD | `-41.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.56` | 2,900,000.00 USD | 0.00 USD | 7,110.00 USD | `-40.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.58` | 2,900,000.00 USD | 0.00 USD | 1,100.00 USD | `-40.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.58` | 2,900,000.00 USD | 0.00 USD | 100.04 USD | `-40.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.60` | 2,900,000.00 USD | 0.00 USD | 390.75 USD | `-39.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.62` | 2,900,000.00 USD | 0.00 USD | 5,090.00 USD | `-39.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.67` | 2,890,000.00 USD | 0.00 USD | 226.57 USD | `-38.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.69` | 2,890,000.00 USD | 0.00 USD | 104.98 USD | `-37.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.69` | 2,890,000.00 USD | 0.00 USD | 889.89 USD | `-37.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.71` | 2,890,000.00 USD | 0.00 USD | 7,270.00 USD | `-37.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.73` | 2,880,000.00 USD | 0.00 USD | 107.21 USD | `-36.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.75` | 2,880,000.00 USD | 0.00 USD | 197.37 USD | `-36.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.75` | 2,880,000.00 USD | 0.00 USD | 8,110.00 USD | `-36.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.77` | 2,870,000.00 USD | 0.00 USD | 108.39 USD | `-36.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.77` | 2,870,000.00 USD | 0.00 USD | 435.95 USD | `-35.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.79` | 2,870,000.00 USD | 0.00 USD | 217.23 USD | `-35.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.79` | 2,870,000.00 USD | 0.00 USD | 437.98 USD | `-35.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.81` | 2,870,000.00 USD | 0.00 USD | 1,230.00 USD | `-35.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.83` | 2,870,000.00 USD | 0.00 USD | 8,380.00 USD | `-34.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.83` | 2,860,000.00 USD | 0.00 USD | 283.50 USD | `-34.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.85` | 2,860,000.00 USD | 0.00 USD | 109.53 USD | `-34.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.85` | 2,860,000.00 USD | 0.00 USD | 1,230.00 USD | `-33.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.88` | 2,860,000.00 USD | 0.00 USD | 1,960.00 USD | `-33.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.88` | 2,860,000.00 USD | 0.00 USD | 157.81 USD | `-33.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.90` | 2,860,000.00 USD | 0.00 USD | 4,190.00 USD | `-33.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.90` | 2,860,000.00 USD | 0.00 USD | 4,870.00 USD | `-32.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.92` | 2,850,000.00 USD | 0.00 USD | 1,320.00 USD | `-32.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.92` | 2,850,000.00 USD | 0.00 USD | 493.15 USD | `-32.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.94` | 2,850,000.00 USD | 0.00 USD | 1,560.00 USD | `-32.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.94` | 2,850,000.00 USD | 0.00 USD | 24,200.00 USD | `-31.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.96` | 2,820,000.00 USD | 0.00 USD | 738.75 USD | `-31.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.96` | 2,820,000.00 USD | 0.00 USD | 523.32 USD | `-31.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.98` | 2,820,000.00 USD | 0.00 USD | 4,470.00 USD | `-31.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.00` | 2,820,000.00 USD | 0.00 USD | 12,160.00 USD | `-30.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.02` | 2,800,000.00 USD | 0.00 USD | 1,020.00 USD | `-30.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.04` | 2,800,000.00 USD | 0.00 USD | 214.57 USD | `-29.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.04` | 2,800,000.00 USD | 0.00 USD | 249.08 USD | `-29.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.06` | 2,800,000.00 USD | 0.00 USD | 305.50 USD | `-29.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.06` | 2,800,000.00 USD | 0.00 USD | 109.42 USD | `-29.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.10` | 2,800,000.00 USD | 0.00 USD | 9,300.00 USD | `-28.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.12` | 2,790,000.00 USD | 0.00 USD | 8,570.00 USD | `-27.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.12` | 2,790,000.00 USD | 0.00 USD | 104.69 USD | `-27.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.13` | 2,780,000.00 USD | 0.00 USD | 315.69 USD | `-27.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.15` | 2,780,000.00 USD | 0.00 USD | 214.17 USD | `-27.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.15` | 2,780,000.00 USD | 0.00 USD | 329.07 USD | `-27.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.17` | 2,780,000.00 USD | 0.00 USD | 4,210.00 USD | `-26.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.17` | 2,780,000.00 USD | 0.00 USD | 1,030.00 USD | `-26.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.19` | 2,780,000.00 USD | 0.00 USD | 218.81 USD | `-26.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.21` | 2,780,000.00 USD | 0.00 USD | 24,840.00 USD | `-25.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.21` | 2,750,000.00 USD | 0.00 USD | 144.67 USD | `-25.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.23` | 2,750,000.00 USD | 0.00 USD | 273,030.00 USD | `-25.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.25` | 2,480,000.00 USD | 0.00 USD | 27,380.00 USD | `-24.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.25` | 2,450,000.00 USD | 0.00 USD | 1,530.00 USD | `-24.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.27` | 2,450,000.00 USD | 0.00 USD | 104.81 USD | `-24.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.27` | 2,450,000.00 USD | 0.00 USD | 200.10 USD | `-24.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.29` | 2,450,000.00 USD | 0.00 USD | 1,480.00 USD | `-24.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.29` | 2,450,000.00 USD | 0.00 USD | 1,870.00 USD | `-23.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.31` | 2,450,000.00 USD | 0.00 USD | 11,460.00 USD | `-23.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.31` | 2,440,000.00 USD | 0.00 USD | 240.67 USD | `-23.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.33` | 2,440,000.00 USD | 0.00 USD | 306.56 USD | `-23.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.33` | 2,440,000.00 USD | 0.00 USD | 1,670.00 USD | `-22.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.37` | 2,430,000.00 USD | 0.00 USD | 73,220.00 USD | `-22.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.38` | 2,360,000.00 USD | 0.00 USD | 19,600.00 USD | `-21.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.40` | 2,340,000.00 USD | 0.00 USD | 8,490.00 USD | `-21.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.40` | 2,330,000.00 USD | 0.00 USD | 102,530.00 USD | `-21.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.42` | 2,230,000.00 USD | 0.00 USD | 421.41 USD | `-21.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.42` | 2,230,000.00 USD | 0.00 USD | 4,350.00 USD | `-20.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.44` | 2,230,000.00 USD | 0.00 USD | 444.49 USD | `-20.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.44` | 2,230,000.00 USD | 0.00 USD | 2,550.00 USD | `-20.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.46` | 2,220,000.00 USD | 0.00 USD | 1,380.00 USD | `-20.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.46` | 2,220,000.00 USD | 0.00 USD | 344.07 USD | `-19.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.48` | 2,220,000.00 USD | 0.00 USD | 24,320.00 USD | `-19.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.48` | 2,200,000.00 USD | 0.00 USD | 19,170.00 USD | `-19.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.50` | 2,180,000.00 USD | 0.00 USD | 894.72 USD | `-19.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.50` | 2,180,000.00 USD | 0.00 USD | 70,230.00 USD | `-18.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.52` | 2,110,000.00 USD | 0.00 USD | 21,320.00 USD | `-18.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.52` | 2,090,000.00 USD | 0.00 USD | 3,700.00 USD | `-18.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.54` | 2,080,000.00 USD | 0.00 USD | 16,250.00 USD | `-18.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.54` | 2,070,000.00 USD | 0.00 USD | 5,130.00 USD | `-18.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.56` | 2,060,000.00 USD | 0.00 USD | 1,800.00 USD | `-17.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.56` | 2,060,000.00 USD | 0.00 USD | 18,440.00 USD | `-17.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.58` | 2,040,000.00 USD | 0.00 USD | 77,480.00 USD | `-17.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.58` | 1,960,000.00 USD | 0.00 USD | 1,610.00 USD | `-17.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.60` | 1,960,000.00 USD | 0.00 USD | 331.46 USD | `-16.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.60` | 1,960,000.00 USD | 0.00 USD | 56,250.00 USD | `-16.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.62` | 1,900,000.00 USD | 0.00 USD | 632.99 USD | `-16.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.62` | 1,900,000.00 USD | 0.00 USD | 1,000.00 USD | `-16.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.63` | 1,900,000.00 USD | 0.00 USD | 1,210.00 USD | `-15.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.65` | 1,900,000.00 USD | 0.00 USD | 54,670.00 USD | `-15.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.65` | 1,850,000.00 USD | 0.00 USD | 4,080.00 USD | `-15.48%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.67` | 1,840,000.00 USD | 0.00 USD | 4,070.00 USD | `-15.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.67` | 1,840,000.00 USD | 0.00 USD | 367.50 USD | `-15.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.69` | 1,840,000.00 USD | 0.00 USD | 19,240.00 USD | `-14.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.69` | 1,820,000.00 USD | 0.00 USD | 4,370.00 USD | `-14.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.71` | 1,810,000.00 USD | 0.00 USD | 389,710.00 USD | `-14.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.71` | 1,420,000.00 USD | 0.00 USD | 6,300.00 USD | `-14.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.73` | 1,420,000.00 USD | 0.00 USD | 821.36 USD | `-13.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.73` | 1,420,000.00 USD | 0.00 USD | 32,040.00 USD | `-13.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.75` | 1,390,000.00 USD | 0.00 USD | 28,820.00 USD | `-13.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.75` | 1,360,000.00 USD | 0.00 USD | 14,490.00 USD | `-13.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.77` | 1,340,000.00 USD | 0.00 USD | 8,780.00 USD | `-12.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.77` | 1,330,000.00 USD | 0.00 USD | 1,190.00 USD | `-12.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.79` | 1,330,000.00 USD | 0.00 USD | 1,780.00 USD | `-12.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.79` | 1,330,000.00 USD | 0.00 USD | 167,490.00 USD | `-12.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.81` | 1,160,000.00 USD | 0.00 USD | 4,530.00 USD | `-12.01%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.81` | 1,160,000.00 USD | 0.00 USD | 22,340.00 USD | `-11.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.83` | 1,140,000.00 USD | 0.00 USD | 7,350.00 USD | `-11.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.83` | 1,130,000.00 USD | 0.00 USD | 41,340.00 USD | `-11.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.85` | 1,090,000.00 USD | 0.00 USD | 43,060.00 USD | `-11.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.85` | 1,040,000.00 USD | 0.00 USD | 5,890.00 USD | `-10.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.87` | 1,040,000.00 USD | 0.00 USD | 8,380.00 USD | `-10.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.88` | 1,030,000.00 USD | 0.00 USD | 161,230.00 USD | `-10.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.88` | 868,900.00 USD | 0.00 USD | 27,330.00 USD | `-10.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.90` | 841,570.00 USD | 0.00 USD | 8,970.00 USD | `-9.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.90` | 832,600.00 USD | 0.00 USD | 44,340.00 USD | `-9.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.92` | 788,260.00 USD | 0.00 USD | 2,340.00 USD | `-9.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.92` | 785,920.00 USD | 0.00 USD | 6,910.00 USD | `-9.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.94` | 779,010.00 USD | 0.00 USD | 934.17 USD | `-9.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.94` | 778,080.00 USD | 0.00 USD | 5,090.00 USD | `-8.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.96` | 772,990.00 USD | 0.00 USD | 2,780.00 USD | `-8.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.96` | 770,210.00 USD | 0.00 USD | 13,720.00 USD | `-8.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.98` | 756,490.00 USD | 0.00 USD | 317.60 USD | `-8.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.98` | 756,170.00 USD | 0.00 USD | 42,280.00 USD | `-7.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.00` | 713,890.00 USD | 0.00 USD | 667.16 USD | `-7.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.00` | 713,220.00 USD | 0.00 USD | 187,820.00 USD | `-7.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.01` | 525,400.00 USD | 0.00 USD | 350.51 USD | `-7.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.03` | 525,050.00 USD | 0.00 USD | 58,180.00 USD | `-6.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.04` | 466,870.00 USD | 0.00 USD | 428.11 USD | `-6.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.04` | 466,440.00 USD | 0.00 USD | 919.83 USD | `-6.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.05` | 465,520.00 USD | 0.00 USD | 33,630.00 USD | `-6.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.07` | 431,890.00 USD | 0.00 USD | 113.41 USD | `-6.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.08` | 431,780.00 USD | 0.00 USD | 6,150.00 USD | `-5.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.08` | 425,630.00 USD | 0.00 USD | 5,870.00 USD | `-5.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.09` | 419,760.00 USD | 0.00 USD | 29,550.00 USD | `-5.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.11` | 390,210.00 USD | 0.00 USD | 39,120.00 USD | `-5.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.12` | 351,090.00 USD | 0.00 USD | 65,790.00 USD | `-4.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.12` | 285,290.00 USD | 0.00 USD | 8,000.00 USD | `-4.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.13` | 277,290.00 USD | 0.00 USD | 54,000.00 USD | `-4.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.14` | 223,290.00 USD | 0.00 USD | 13,010.00 USD | `-4.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.16` | 210,280.00 USD | 0.00 USD | 42,290.00 USD | `-3.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.17` | 168,000.00 USD | 0.00 USD | 18,740.00 USD | `-3.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.17` | 149,260.00 USD | 0.00 USD | 9,150.00 USD | `-3.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.18` | 140,100.00 USD | 0.00 USD | 3,470.00 USD | `-3.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.20` | 136,640.00 USD | 0.00 USD | 126.69 USD | `-2.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.21` | 136,510.00 USD | 0.00 USD | 24,090.00 USD | `-2.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.21` | 112,420.00 USD | 0.00 USD | 14,410.00 USD | `-2.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.22` | 98,010.00 USD | 0.00 USD | 14,770.00 USD | `-2.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.24` | 83,240.00 USD | 0.00 USD | 16,370.00 USD | `-2.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.25` | 66,870.00 USD | 0.00 USD | 5,190.00 USD | `-1.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.25` | 61,680.00 USD | 0.00 USD | 16,510.00 USD | `-1.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.26` | 45,170.00 USD | 0.00 USD | 101.08 USD | `-1.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.28` | 45,070.00 USD | 0.00 USD | 1,620.00 USD | `-1.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.29` | 43,460.00 USD | 0.00 USD | 143.98 USD | `-0.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.29` | 43,310.00 USD | 0.00 USD | 3,240.00 USD | `-0.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.30` | 40,070.00 USD | 0.00 USD | 310.82 USD | `-0.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.32` | 39,760.00 USD | 0.00 USD | 39,760.00 USD | `-0.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.33` | 182.52 USD | 182.52 USD | 0.00 USD | `+0.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.33` | 1,380.00 USD | 1,190.00 USD | 0.00 USD | `+0.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.34` | 18,760.00 USD | 17,380.00 USD | 0.00 USD | `+0.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.36` | 34,170.00 USD | 15,410.00 USD | 0.00 USD | `+0.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.37` | 195,180.00 USD | 161,010.00 USD | 0.00 USD | `+0.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.38` | 284,810.00 USD | 89,630.00 USD | 0.00 USD | `+1.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.38` | 352,160.00 USD | 67,350.00 USD | 0.00 USD | `+1.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.39` | 535,590.00 USD | 183,430.00 USD | 0.00 USD | `+1.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.41` | 595,950.00 USD | 60,360.00 USD | 0.00 USD | `+1.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.42` | 599,620.00 USD | 3,670.00 USD | 0.00 USD | `+2.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.42` | 608,960.00 USD | 9,340.00 USD | 0.00 USD | `+2.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.43` | 614,910.00 USD | 5,950.00 USD | 0.00 USD | `+2.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.45` | 624,190.00 USD | 9,280.00 USD | 0.00 USD | `+2.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.46` | 673,160.00 USD | 48,970.00 USD | 0.00 USD | `+3.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.46` | 678,650.00 USD | 5,500.00 USD | 0.00 USD | `+3.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.47` | 679,030.00 USD | 375.90 USD | 0.00 USD | `+3.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.49` | 680,340.00 USD | 1,310.00 USD | 0.00 USD | `+3.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.50` | 687,800.00 USD | 7,460.00 USD | 0.00 USD | `+3.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.50` | 737,940.00 USD | 50,130.00 USD | 0.00 USD | `+4.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.51` | 756,870.00 USD | 18,940.00 USD | 0.00 USD | `+4.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.53` | 863,650.00 USD | 106,780.00 USD | 0.00 USD | `+4.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.54` | 865,490.00 USD | 1,830.00 USD | 0.00 USD | `+4.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.54` | 866,400.00 USD | 909.00 USD | 0.00 USD | `+5.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.55` | 890,760.00 USD | 24,360.00 USD | 0.00 USD | `+5.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.57` | 890,990.00 USD | 227.79 USD | 0.00 USD | `+5.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.58` | 893,130.00 USD | 2,150.00 USD | 0.00 USD | `+5.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.58` | 893,890.00 USD | 759.73 USD | 0.00 USD | `+6.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.59` | 911,840.00 USD | 17,950.00 USD | 0.00 USD | `+6.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.61` | 1,030,000.00 USD | 120,610.00 USD | 0.00 USD | `+6.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.62` | 1,030,000.00 USD | 742.55 USD | 0.00 USD | `+6.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.62` | 1,050,000.00 USD | 21,450.00 USD | 0.00 USD | `+6.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.63` | 1,060,000.00 USD | 1,100.00 USD | 0.00 USD | `+7.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.64` | 1,060,000.00 USD | 4,070.00 USD | 0.00 USD | `+7.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.66` | 1,060,000.00 USD | 1,240.00 USD | 0.00 USD | `+7.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.67` | 1,140,000.00 USD | 77,690.00 USD | 0.00 USD | `+7.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.67` | 1,140,000.00 USD | 3,030.00 USD | 0.00 USD | `+8.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.68` | 1,140,000.00 USD | 459.13 USD | 0.00 USD | `+8.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.70` | 1,140,000.00 USD | 152.12 USD | 0.00 USD | `+8.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.71` | 1,570,000.00 USD | 430,140.00 USD | 0.00 USD | `+8.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.71` | 1,810,000.00 USD | 234,640.00 USD | 0.00 USD | `+9.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.72` | 1,810,000.00 USD | 2,650.00 USD | 0.00 USD | `+9.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.74` | 1,890,000.00 USD | 84,970.00 USD | 0.00 USD | `+9.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.75` | 1,900,000.00 USD | 6,160.00 USD | 0.00 USD | `+9.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.75` | 1,930,000.00 USD | 29,420.00 USD | 0.00 USD | `+9.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.76` | 1,940,000.00 USD | 13,030.00 USD | 0.00 USD | `+10.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.78` | 1,950,000.00 USD | 2,640.00 USD | 0.00 USD | `+10.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.79` | 2,760,000.00 USD | 818,860.00 USD | 0.00 USD | `+10.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.79` | 2,770,000.00 USD | 559.58 USD | 0.00 USD | `+10.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.80` | 2,940,000.00 USD | 176,250.00 USD | 0.00 USD | `+11.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.82` | 2,970,000.00 USD | 32,000.00 USD | 0.00 USD | `+11.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.83` | 2,980,000.00 USD | 8,540.00 USD | 0.00 USD | `+11.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.83` | 3,080,000.00 USD | 93,100.00 USD | 0.00 USD | `+11.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.84` | 3,140,000.00 USD | 60,350.00 USD | 0.00 USD | `+12.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.86` | 3,160,000.00 USD | 23,780.00 USD | 0.00 USD | `+12.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.87` | 3,180,000.00 USD | 23,180.00 USD | 0.00 USD | `+12.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.88` | 3,190,000.00 USD | 10,400.00 USD | 0.00 USD | `+12.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.88` | 3,210,000.00 USD | 19,890.00 USD | 0.00 USD | `+12.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.89` | 3,220,000.00 USD | 4,060.00 USD | 0.00 USD | `+13.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.91` | 3,340,000.00 USD | 120,030.00 USD | 0.00 USD | `+13.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.92` | 3,340,000.00 USD | 156.30 USD | 0.00 USD | `+13.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.92` | 3,350,000.00 USD | 13,180.00 USD | 0.00 USD | `+13.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.93` | 3,350,000.00 USD | 4,420.00 USD | 0.00 USD | `+14.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.95` | 3,360,000.00 USD | 313.51 USD | 0.00 USD | `+14.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.96` | 3,360,000.00 USD | 7,900.00 USD | 0.00 USD | `+14.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.96` | 3,410,000.00 USD | 47,350.00 USD | 0.00 USD | `+14.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.97` | 3,410,000.00 USD | 187.06 USD | 0.00 USD | `+15.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.99` | 3,500,000.00 USD | 92,570.00 USD | 0.00 USD | `+15.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.00` | 3,510,000.00 USD | 2,540.00 USD | 0.00 USD | `+15.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.00` | 3,570,000.00 USD | 63,070.00 USD | 0.00 USD | `+15.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.01` | 3,590,000.00 USD | 25,080.00 USD | 0.00 USD | `+15.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.03` | 3,600,000.00 USD | 5,030.00 USD | 0.00 USD | `+16.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.04` | 3,620,000.00 USD | 19,640.00 USD | 0.00 USD | `+16.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.04` | 3,620,000.00 USD | 120.58 USD | 0.00 USD | `+16.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.05` | 3,630,000.00 USD | 14,090.00 USD | 0.00 USD | `+16.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.07` | 3,640,000.00 USD | 5,860.00 USD | 0.00 USD | `+17.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.08` | 3,730,000.00 USD | 87,450.00 USD | 0.00 USD | `+17.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.08` | 3,730,000.00 USD | 5,460.00 USD | 0.00 USD | `+17.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.09` | 3,730,000.00 USD | 178.33 USD | 0.00 USD | `+17.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.11` | 3,800,000.00 USD | 70,250.00 USD | 0.00 USD | `+18.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.12` | 3,820,000.00 USD | 15,350.00 USD | 0.00 USD | `+18.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.12` | 3,820,000.00 USD | 179.38 USD | 0.00 USD | `+18.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.13` | 3,820,000.00 USD | 179.72 USD | 0.00 USD | `+18.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.14` | 3,820,000.00 USD | 217.63 USD | 0.00 USD | `+18.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.16` | 3,820,000.00 USD | 493.85 USD | 0.00 USD | `+19.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.17` | 3,820,000.00 USD | 575.38 USD | 0.00 USD | `+19.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.17` | 3,820,000.00 USD | 327.58 USD | 0.00 USD | `+19.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.18` | 3,820,000.00 USD | 163.85 USD | 0.00 USD | `+19.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.20` | 3,940,000.00 USD | 120,930.00 USD | 0.00 USD | `+20.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.21` | 3,980,000.00 USD | 38,230.00 USD | 0.00 USD | `+20.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.21` | 3,980,000.00 USD | 1,710.00 USD | 0.00 USD | `+20.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.22` | 3,980,000.00 USD | 432.63 USD | 0.00 USD | `+20.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.24` | 3,980,000.00 USD | 2,620.00 USD | 0.00 USD | `+21.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.25` | 3,980,000.00 USD | 537.61 USD | 0.00 USD | `+21.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.25` | 4,400,000.00 USD | 420,400.00 USD | 0.00 USD | `+21.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.26` | 4,400,000.00 USD | 278.52 USD | 0.00 USD | `+21.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.28` | 4,410,000.00 USD | 589.22 USD | 0.00 USD | `+21.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.29` | 4,410,000.00 USD | 733.03 USD | 0.00 USD | `+22.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.29` | 4,410,000.00 USD | 423.60 USD | 0.00 USD | `+22.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.30` | 4,420,000.00 USD | 12,620.00 USD | 0.00 USD | `+22.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.32` | 4,420,000.00 USD | 381.09 USD | 0.00 USD | `+22.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.33` | 4,420,000.00 USD | 961.16 USD | 0.00 USD | `+23.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.33` | 4,420,000.00 USD | 1,570.00 USD | 0.00 USD | `+23.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.34` | 4,430,000.00 USD | 5,650.00 USD | 0.00 USD | `+23.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.36` | 4,430,000.00 USD | 160.11 USD | 0.00 USD | `+23.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.37` | 4,430,000.00 USD | 225.33 USD | 0.00 USD | `+24.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.38` | 4,430,000.00 USD | 438.60 USD | 0.00 USD | `+24.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.38` | 4,430,000.00 USD | 6,610.00 USD | 0.00 USD | `+24.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.39` | 4,480,000.00 USD | 40,880.00 USD | 0.00 USD | `+24.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.41` | 4,490,000.00 USD | 17,160.00 USD | 0.00 USD | `+24.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.42` | 4,500,000.00 USD | 4,330.00 USD | 0.00 USD | `+25.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.42` | 4,500,000.00 USD | 639.61 USD | 0.00 USD | `+25.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.43` | 4,500,000.00 USD | 1,710.00 USD | 0.00 USD | `+25.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.45` | 4,510,000.00 USD | 13,690.00 USD | 0.00 USD | `+25.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.46` | 4,510,000.00 USD | 1,020.00 USD | 0.00 USD | `+26.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.46` | 4,600,000.00 USD | 87,720.00 USD | 0.00 USD | `+26.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.47` | 4,630,000.00 USD | 30,110.00 USD | 0.00 USD | `+26.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.49` | 4,630,000.00 USD | 863.89 USD | 0.00 USD | `+26.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.50` | 4,630,000.00 USD | 1,040.00 USD | 0.00 USD | `+27.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.50` | 5,620,000.00 USD | 986,050.00 USD | 0.00 USD | `+27.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.51` | 5,630,000.00 USD | 5,600.00 USD | 0.00 USD | `+27.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.53` | 5,640,000.00 USD | 19,110.00 USD | 0.00 USD | `+27.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.54` | 5,660,000.00 USD | 18,790.00 USD | 0.00 USD | `+27.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.54` | 5,720,000.00 USD | 58,030.00 USD | 0.00 USD | `+28.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.55` | 5,770,000.00 USD | 46,110.00 USD | 0.00 USD | `+28.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.57` | 5,780,000.00 USD | 14,320.00 USD | 0.00 USD | `+28.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.58` | 5,790,000.00 USD | 11,740.00 USD | 0.00 USD | `+28.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.58` | 5,820,000.00 USD | 23,650.00 USD | 0.00 USD | `+29.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.59` | 5,820,000.00 USD | 384.94 USD | 0.00 USD | `+29.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.61` | 5,820,000.00 USD | 1,300.00 USD | 0.00 USD | `+29.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.62` | 5,820,000.00 USD | 347.06 USD | 0.00 USD | `+30.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.63` | 5,820,000.00 USD | 347.68 USD | 0.00 USD | `+30.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.64` | 5,820,000.00 USD | 491.11 USD | 0.00 USD | `+30.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.66` | 5,820,000.00 USD | 3,290.00 USD | 0.00 USD | `+30.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.67` | 5,820,000.00 USD | 281.55 USD | 0.00 USD | `+31.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.67` | 5,830,000.00 USD | 6,590.00 USD | 0.00 USD | `+31.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.68` | 5,830,000.00 USD | 235.93 USD | 0.00 USD | `+31.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.70` | 5,840,000.00 USD | 5,860.00 USD | 0.00 USD | `+31.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.71` | 5,940,000.00 USD | 103,820.00 USD | 0.00 USD | `+31.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.71` | 5,940,000.00 USD | 705.23 USD | 0.00 USD | `+32.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.72` | 5,950,000.00 USD | 5,720.00 USD | 0.00 USD | `+32.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.75` | 5,950,000.00 USD | 139.03 USD | 0.00 USD | `+32.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.75` | 5,950,000.00 USD | 2,480.00 USD | 0.00 USD | `+33.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.78` | 5,950,000.00 USD | 1,850.00 USD | 0.00 USD | `+33.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.79` | 5,950,000.00 USD | 286.94 USD | 0.00 USD | `+33.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.80` | 5,960,000.00 USD | 7,120.00 USD | 0.00 USD | `+34.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.82` | 5,960,000.00 USD | 329.13 USD | 0.00 USD | `+34.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.83` | 5,960,000.00 USD | 1,970.00 USD | 0.00 USD | `+34.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.83` | 5,960,000.00 USD | 1,020.00 USD | 0.00 USD | `+34.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.84` | 5,960,000.00 USD | 2,720.00 USD | 0.00 USD | `+35.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.86` | 5,970,000.00 USD | 1,190.00 USD | 0.00 USD | `+35.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.87` | 5,970,000.00 USD | 1,770.00 USD | 0.00 USD | `+35.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.88` | 5,970,000.00 USD | 3,450.00 USD | 0.00 USD | `+35.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.88` | 5,970,000.00 USD | 345.45 USD | 0.00 USD | `+36.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.91` | 6,050,000.00 USD | 73,570.00 USD | 0.00 USD | `+36.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.92` | 6,050,000.00 USD | 1,670.00 USD | 0.00 USD | `+36.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.92` | 6,050,000.00 USD | 1,020.00 USD | 0.00 USD | `+37.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.93` | 6,200,000.00 USD | 153,150.00 USD | 0.00 USD | `+37.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.96` | 6,230,000.00 USD | 26,180.00 USD | 0.00 USD | `+37.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.96` | 6,230,000.00 USD | 5,440.00 USD | 0.00 USD | `+37.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.97` | 6,240,000.00 USD | 8,940.00 USD | 0.00 USD | `+38.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.99` | 6,360,000.00 USD | 119,340.00 USD | 0.00 USD | `+38.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.00` | 6,360,000.00 USD | 3,000.00 USD | 0.00 USD | `+38.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.00` | 6,560,000.00 USD | 197,230.00 USD | 0.00 USD | `+38.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.01` | 6,570,000.00 USD | 13,710.00 USD | 0.00 USD | `+39.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.03` | 6,670,000.00 USD | 90,380.00 USD | 0.00 USD | `+39.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.04` | 6,670,000.00 USD | 2,050.00 USD | 0.00 USD | `+39.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.04` | 6,670,000.00 USD | 3,300.00 USD | 0.00 USD | `+39.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.05` | 6,670,000.00 USD | 1,040.00 USD | 0.00 USD | `+40.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.07` | 6,670,000.00 USD | 425.76 USD | 0.00 USD | `+40.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.08` | 6,680,000.00 USD | 4,120.00 USD | 0.00 USD | `+40.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.09` | 6,680,000.00 USD | 2,000.00 USD | 0.00 USD | `+40.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.11` | 6,740,000.00 USD | 61,050.00 USD | 0.00 USD | `+41.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.12` | 6,740,000.00 USD | 1,610.00 USD | 0.00 USD | `+41.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.13` | 6,740,000.00 USD | 1,200.00 USD | 0.00 USD | `+41.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.14` | 6,740,000.00 USD | 420.32 USD | 0.00 USD | `+42.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.16` | 6,740,000.00 USD | 1,940.00 USD | 0.00 USD | `+42.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.17` | 6,750,000.00 USD | 4,010.00 USD | 0.00 USD | `+42.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.21` | 6,810,000.00 USD | 66,060.00 USD | 0.00 USD | `+43.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.21` | 6,820,000.00 USD | 1,890.00 USD | 0.00 USD | `+43.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.22` | 6,820,000.00 USD | 195.46 USD | 0.00 USD | `+43.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.24` | 6,820,000.00 USD | 289.93 USD | 0.00 USD | `+44.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.25` | 6,820,000.00 USD | 116.16 USD | 0.00 USD | `+44.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.30` | 6,820,000.00 USD | 7,310.00 USD | 0.00 USD | `+45.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.32` | 6,820,000.00 USD | 310.70 USD | 0.00 USD | `+46.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.33` | 6,820,000.00 USD | 325.62 USD | 0.00 USD | `+46.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.36` | 6,830,000.00 USD | 1,760.00 USD | 0.00 USD | `+46.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.39` | 6,830,000.00 USD | 3,230.00 USD | 0.00 USD | `+47.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.41` | 6,830,000.00 USD | 5,120.00 USD | 0.00 USD | `+48.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.50` | 6,840,000.00 USD | 1,310.00 USD | 0.00 USD | `+50.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.50` | 6,870,000.00 USD | 30,990.00 USD | 0.00 USD | `+50.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.51` | 6,870,000.00 USD | 104.24 USD | 0.00 USD | `+50.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.54` | 6,880,000.00 USD | 13,580.00 USD | 0.00 USD | `+51.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.58` | 6,880,000.00 USD | 1,630.00 USD | 0.00 USD | `+52.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.59` | 6,880,000.00 USD | 1,370.00 USD | 0.00 USD | `+52.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.61` | 6,890,000.00 USD | 5,400.00 USD | 0.00 USD | `+52.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.62` | 6,890,000.00 USD | 1,620.00 USD | 0.00 USD | `+52.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.67` | 6,890,000.00 USD | 450.55 USD | 0.00 USD | `+54.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.67` | 6,890,000.00 USD | 3,060.00 USD | 0.00 USD | `+54.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.71` | 6,900,000.00 USD | 3,070.00 USD | 0.00 USD | `+55.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.75` | 6,900,000.00 USD | 1,550.00 USD | 0.00 USD | `+55.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.79` | 6,900,000.00 USD | 647.56 USD | 0.00 USD | `+57.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.80` | 6,900,000.00 USD | 1,420.00 USD | 0.00 USD | `+57.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.82` | 6,900,000.00 USD | 2,130.00 USD | 0.00 USD | `+57.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.83` | 6,910,000.00 USD | 6,870.00 USD | 0.00 USD | `+57.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.84` | 6,910,000.00 USD | 342.25 USD | 0.00 USD | `+58.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.87` | 6,910,000.00 USD | 2,990.00 USD | 0.00 USD | `+58.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.89` | 6,920,000.00 USD | 2,970.00 USD | 0.00 USD | `+59.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.91` | 6,920,000.00 USD | 324.54 USD | 0.00 USD | `+59.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.95` | 6,920,000.00 USD | 504.21 USD | 0.00 USD | `+60.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.97` | 6,920,000.00 USD | 166.00 USD | 0.00 USD | `+61.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.99` | 6,920,000.00 USD | 4,190.00 USD | 0.00 USD | `+61.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.00` | 6,940,000.00 USD | 13,480.00 USD | 0.00 USD | `+61.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.04` | 6,940,000.00 USD | 2,860.00 USD | 0.00 USD | `+62.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.11` | 6,940,000.00 USD | 264.31 USD | 0.00 USD | `+64.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.13` | 6,940,000.00 USD | 599.34 USD | 0.00 USD | `+64.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.16` | 6,940,000.00 USD | 193.19 USD | 0.00 USD | `+65.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.18` | 6,940,000.00 USD | 3,950.00 USD | 0.00 USD | `+66.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.21` | 6,940,000.00 USD | 1,940.00 USD | 0.00 USD | `+66.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.25` | 7,110,000.00 USD | 160,550.00 USD | 0.00 USD | `+67.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.28` | 7,110,000.00 USD | 1,290.00 USD | 0.00 USD | `+68.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.32` | 7,110,000.00 USD | 1,180.00 USD | 0.00 USD | `+69.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.39` | 7,110,000.00 USD | 630.05 USD | 0.00 USD | `+71.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.41` | 7,110,000.00 USD | 1,410.00 USD | 0.00 USD | `+71.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.42` | 7,110,000.00 USD | 2,610.00 USD | 0.00 USD | `+71.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.50` | 7,120,000.00 USD | 7,630.00 USD | 0.00 USD | `+73.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.58` | 7,120,000.00 USD | 4,640.00 USD | 0.00 USD | `+75.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.61` | 7,130,000.00 USD | 371.88 USD | 0.00 USD | `+75.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.62` | 7,130,000.00 USD | 2,510.00 USD | 0.00 USD | `+76.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.67` | 7,130,000.00 USD | 380.68 USD | 0.00 USD | `+77.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.79` | 7,140,000.00 USD | 11,170.00 USD | 0.00 USD | `+80.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.80` | 7,170,000.00 USD | 34,360.00 USD | 0.00 USD | `+80.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.82` | 7,170,000.00 USD | 253.21 USD | 0.00 USD | `+80.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.83` | 7,170,000.00 USD | 100.29 USD | 0.00 USD | `+81.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.96` | 7,180,000.00 USD | 10,610.00 USD | 0.00 USD | `+84.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.97` | 7,180,000.00 USD | 309.43 USD | 0.00 USD | `+84.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.99` | 7,190,000.00 USD | 4,640.00 USD | 0.00 USD | `+84.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.01` | 7,230,000.00 USD | 36,740.00 USD | 0.00 USD | `+85.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.03` | 7,310,000.00 USD | 81,310.00 USD | 0.00 USD | `+85.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.15` | 7,310,000.00 USD | 2,150.00 USD | 0.00 USD | `+88.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.19` | 7,310,000.00 USD | 216.90 USD | 0.00 USD | `+89.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.20` | 7,310,000.00 USD | 1,990.00 USD | 0.00 USD | `+89.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.21` | 7,320,000.00 USD | 7,200.00 USD | 0.00 USD | `+89.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.38` | 7,320,000.00 USD | 998.65 USD | 0.00 USD | `+93.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.39` | 7,320,000.00 USD | 1,260.00 USD | 0.00 USD | `+94.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.40` | 7,420,000.00 USD | 103,010.00 USD | 0.00 USD | `+94.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.44` | 7,430,000.00 USD | 1,330.00 USD | 0.00 USD | `+95.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.46` | 7,430,000.00 USD | 721.22 USD | 0.00 USD | `+95.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.51` | 7,430,000.00 USD | 5,130.00 USD | 0.00 USD | `+96.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.61` | 7,430,000.00 USD | 2,010.00 USD | 0.00 USD | `+98.99%` | `TACTICAL (Retail Cluster)` |

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
| `15M` | `NEAR` | `60.71%` | `39.29%` | `1.55` | 3,370,000.00 USD |
| `15M` | `Binance` | `60.21%` | `39.79%` | `1.51` | 836,100.00 USD |
| `15M` | `OKX` | `55.72%` | `44.28%` | `1.26` | 95,120.00 USD |
| `15M` | `Bybit` | `63.23%` | `36.77%` | `1.72` | 128,500.00 USD |
| `15M` | `KuCoin` | `66.62%` | `33.38%` | `2.00` | 15,940.00 USD |
| `15M` | `Gate` | `55.07%` | `44.93%` | `1.23` | 35,310.00 USD |
| `15M` | `Bitget` | `70.83%` | `29.17%` | `2.43` | 64,940.00 USD |
| `15M` | `BingX` | `22.27%` | `77.73%` | `0.29` | 1,380,000.00 USD |
| `15M` | `MEXC` | `69.32%` | `30.68%` | `2.26` | 67,760.00 USD |
| `15M` | `Bitunix` | `54.94%` | `45.06%` | `1.22` | 47,780.00 USD |
| `15M` | `Hyperliquid` | `89.22%` | `10.78%` | `8.28` | 7,510.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `50.26%` | `49.74%` | `1.01` | 375,570.00 USD |
| `15M` | `Crypto.com` | `0%` | `0%` | `1.00` | 20.31 USD |
| `15M` | `WhiteBIT` | `76.49%` | `23.51%` | `3.25` | 276,550.00 USD |
| `15M` | `HTX` | `38.56%` | `61.44%` | `0.63` | 652.52 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `93.83%` | `6.17%` | `15.21` | 15,010.00 USD |
| `15M` | `Aster` | `97.94%` | `2.06%` | `47.54` | 101.66 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `6.6%` | `93.4%` | `0.07` | 13,830.00 USD |
| `15M` | `Whale Positions` | `60.21%` | `39.79%` | `1.51` | 836,100.00 USD |
| `15M` | `Global Accounts` | `60.71%` | `39.29%` | `1.55` | 3,370,000.00 USD |
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
| `0:00 UTC` | `4.25` | `4.26` | `4.25` | `4.30` | `4.21` | 16,835,236.87 USD | 7,874,403.92 USD | 8,960,832.95 USD | -1,086,429.03 USD | `-6.45%` | `8B / 9S` |
| `5:00 UTC` | `4.25` | `4.25` | `4.25` | `4.26` | `4.23` | 9,185,944.44 USD | 4,818,806.27 USD | 4,367,138.17 USD | 451,668.11 USD | `+4.92%` | `4B / 5S` |
| `0:00 UTC` | `4.30` | `4.30` | `4.30` | `4.36` | `4.24` | 30,489,684.47 USD | 19,297,257.05 USD | 11,192,427.43 USD | 8,104,829.62 USD | `+26.58%` | `32B / 2S` |
| `5:00 UTC` | `4.35` | `4.35` | `4.35` | `4.36` | `4.33` | 15,245,662.84 USD | 8,049,667.44 USD | 7,195,995.40 USD | 853,672.05 USD | `+5.60%` | `0B / 3S` |
| `0:00 UTC` | `4.33` | `4.33` | `4.33` | `4.35` | `4.31` | 8,553,382.74 USD | 3,656,231.21 USD | 4,897,151.53 USD | -1,240,920.31 USD | `-14.51%` | `1B / 5S` |
| `5:00 UTC` | `4.31` | `4.35` | `4.31` | `4.39` | `4.31` | 11,576,553.35 USD | 6,334,405.32 USD | 5,242,148.03 USD | 1,092,257.28 USD | `+9.44%` | `19B / 4S` |
| `0:00 UTC` | `4.34` | `4.34` | `4.34` | `4.37` | `4.32` | 8,173,916.95 USD | 4,141,201.50 USD | 4,032,715.45 USD | 108,486.05 USD | `+1.33%` | `4B / 2S` |
| `5:00 UTC` | `4.32` | `4.32` | `4.32` | `4.34` | `4.31` | 8,060,413.67 USD | 4,212,890.12 USD | 3,847,523.55 USD | 365,366.56 USD | `+4.53%` | `0B / 2S` |
| `0:00 UTC` | `4.31` | `4.32` | `4.31` | `4.36` | `4.29` | 5,778,991.37 USD | 2,863,139.85 USD | 2,915,851.52 USD | -52,711.67 USD | `-0.91%` | `7B / 7S` |
| `5:00 UTC` | `4.36` | `4.36` | `4.36` | `4.38` | `4.34` | 5,100,051.71 USD | 2,724,269.37 USD | 2,375,782.33 USD | 348,487.04 USD | `+6.83%` | `5B / 5S` |

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
| `5m` | 55,330.00 USD | 338,320.00 USD | **`ACCUMULATION`** |
| `15m` | 335,480.00 USD | -622,940.00 USD | **`DISTRIBUTION`** |
| `30m` | -74,140.00 USD | -1,950,000.00 USD | **`DISTRIBUTION`** |
| `1h` | -197,180.00 USD | -3,210,000.00 USD | **`DISTRIBUTION`** |
| `2h` | 11,640,000.00 USD | 8,160,000.00 USD | **`ACCUMULATION`** |
| `4h` | 14,610,000.00 USD | 8,090,000.00 USD | **`ACCUMULATION`** |
| `6h` | 15,870,000.00 USD | -648,110.00 USD | **`ACCUMULATION`** |
| `8h` | 25,390,000.00 USD | 17,480,000.00 USD | **`ACCUMULATION`** |
| `12h` | 12,770,000.00 USD | -5,160,000.00 USD | **`ACCUMULATION`** |
| `24h` | -325,100.00 USD | -26,770,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -59,970,000.00 USD | -133,880,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -225,410,000.00 USD | -669,060,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+55.33K` | 15m=`+335.48K` | 1h=`-197.18K` | 24h=`-325.10K`
* Futures Capital Netflows: 5m=`+338.32K` | 15m=`-622.94K` | 1h=`-3.21M` | 24h=`-26.77M`
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
  * `2026-10-30 15:18:36 IST`: [dailyforex.com] - (Sentiment: `Neutral`)
  * `2026-10-30 15:12:36 IST`: [breakingthenews.net] - (Sentiment: `Neutral`)
  * `2026-10-30 14:41:36 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 14:37:36 IST`: [@FirstSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 14:33:36 IST`: [destatis.de] - (Sentiment: `Neutral`)
  * `2026-10-30 14:32:36 IST`: [istat.it] - (Sentiment: `Neutral`)
  * `2026-10-30 15:25:36 IST`: [channelnewsasia.com] - (Sentiment: `Neutral`)
  * `2026-10-30 15:25:36 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 15:25:36 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 15:25:36 IST`: [kof.ethz.ch] - (Sentiment: `Neutral`)
  * `2026-10-30 15:24:36 IST`: [gerlachmacro.substack.com] - (Sentiment: `Neutral`)
  * `2026-10-30 15:24:36 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-30 15:24:36 IST`: [insee.fr] - (Sentiment: `Neutral`)
  * `2026-10-30 15:24:36 IST`: [insee.fr] - (Sentiment: `Neutral`)
  * `2026-10-30 15:24:36 IST`: [@FirstSquawk] - (Sentiment: `Neutral`)


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
  * Spread-Padded Stop Loss: `3.83` (Risk Distance: `0.1137` pts)
  * +2.5R Take Profit: `4.22`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `4.23` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `4.34` (Risk Distance: `0.1137` pts)
  * +2.5R Take Profit: `3.94`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`4.41`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
