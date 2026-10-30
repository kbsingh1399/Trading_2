# 🏛️ SOVEREIGN CANDIDATE DOSSIER: NEAR
**Canonical Key**: `NEAR` | **Broker Instrument**: `NERUSD.p` | **Asset Class**: `Crypto Alt L1`
**Timestamp**: `2026-10-30 09:40:22 IST` (`2026-10-30 04:10:22 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `4.12` | **Live Ask Quote**: `4.15` | **Mid Price**: `4.14`
- **Spread Points**: `29.00` | **Spread BPS**: `70.07 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `4.01` | VWAP Z-Score: `+2.67` (Regime: `STRETCH_EXTREME`)
  * 14-Period ATR: `0.0548` (Volatility Regime: `HIGH_EXPANSION`)
  * 14-Period RSI: `56.45` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `4.17` | Lower -3.00σ Band: `3.85`
  * Upper +2.51σ Band: `4.14` | Lower -2.51σ Band: `3.87`
  * Upper +2.01σ Band: `4.11` | Lower -2.01σ Band: `3.90`
  * Upper +2.00σ Band: `4.11` | Lower -2.00σ Band: `3.90`
  * Upper +1.28σ Band: `4.08` | Lower -1.28σ Band: `3.94`
  * Upper +1.00σ Band: `4.06` | Lower -1.00σ Band: `3.95`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`4.08` | EMA-20=`4.08` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`4.18` (Slope: `+0.0000`) | EMA-100=`4.30`
  * Institutional Anchors: EMA-144=`4.35` | EMA-200=`4.40` (Slope: `-0.9861`) | EMA-233=`4.43`
- **Range Boundaries**: 24H High=`4.67` | 24H Low=`3.89` | Weekly High=`4.80` | Weekly Low=`3.89`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `4.13` (Distance: `+0.21%`)
  * Point of Control (POC) = `4.09` (Distance: `+1.05%`)
  * Value Area Low (VAL) = `3.95` (Distance: `+4.64%`)
  * Auction Positioning: `ABOVE_VALUE (Imbalance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `RANGE_EXPANSION`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`4.57` | POC=`4.41` | VAL=`4.29`
  * Prior Day Extremes: PDH=`4.75` | PDL=`4.08` | PDC=`4.15`
  * Monday Range Blueprint: High=`4.65` | Mid=`4.53` | Low=`4.41`
  * Developing Weekly Value Area: Weekly VAH=`4.68` | Weekly POC=`4.45` | Weekly VAL=`4.39`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`4.26` | Low=`3.89`
  * London Session (08:00-16:00 UTC): High=`4.16` | Low=`4.12`
  * New York Session (13:00-21:00 UTC): High=`4.16` | Low=`4.11`
  * Initial Balance (First Hour): IB High=`4.15` | IB Low=`4.13`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `4.12` - `4.16`
  * Optimal Trade Entry (OTE 0.705): `4.15`
  * Structural Invalidation Anchor (0.786): `4.17`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `4.12` | `4.14` | `4.12` | `4.13` | `760,994` | 3,143,238.73 USD | 282,578.94 USD | `+8.99%` | -30,347,782.66 USD | `-0.05` | **`BULLISH`** | `DELTA ALIGNED` |
| `5m` | `4.13` | `4.16` | `4.13` | `4.16` | `956,959` | 3,968,681.06 USD | 806,131.37 USD | `+20.31%` | -29,541,651.29 USD | `+1.08` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `5m` | `4.16` | `4.17` | `4.14` | `4.16` | `509,244` | 2,114,042.95 USD | 180,758.89 USD | `+8.55%` | -29,360,892.40 USD | `-0.39` | **`BULLISH`** | `DELTA ALIGNED` |
| `15m` | `4.08` | `4.11` | `4.07` | `4.11` | `1,059,310` | 4,324,346.41 USD | 961,608.74 USD | `+22.24%` | -31,350,723.04 USD | `+0.77` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `4.11` | `4.16` | `4.10` | `4.16` | `2,417,383` | 9,990,039.56 USD | 1,647,200.46 USD | `+16.49%` | -29,703,522.59 USD | `+1.09` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `4.16` | `4.17` | `4.14` | `4.16` | `516,322` | 2,143,497.07 USD | 193,528.69 USD | `+9.03%` | -29,509,993.89 USD | `+0.17` | **`BULLISH`** | `DELTA ALIGNED` |
| `1h` | `3.99` | `4.04` | `3.95` | `4.00` | `8,344,084` | 33,377,841.60 USD | -1,208,714.23 USD | `-3.62%` | -36,547,776.95 USD | `+0.14` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `1h` | `4.00` | `4.11` | `3.97` | `4.06` | `7,535,910` | 30,558,990.03 USD | 3,476,842.65 USD | `+11.38%` | -33,070,934.30 USD | `+1.29` | **`BULLISH`** | `DELTA ALIGNED` |
| `1h` | `4.06` | `4.17` | `4.06` | `4.16` | `5,316,001` | 21,850,471.68 USD | 3,560,940.41 USD | `+16.30%` | -29,509,993.89 USD | `+1.20` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `4h` | `4.65` | `4.69` | `4.38` | `4.40` | `28,351,581` | 128,263,626.10 USD | -4,168,943.82 USD | `-3.25%` | -16,525,751.06 USD | `-0.01` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `4.40` | `4.41` | `4.04` | `4.06` | `71,964,012` | 300,508,235.77 USD | -12,043,039.27 USD | `-4.01%` | -28,568,790.33 USD | `-0.87` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `4.06` | `4.17` | `3.90` | `4.16` | `46,135,129` | 185,302,753.20 USD | -941,303.40 USD | `-0.51%` | -29,510,093.73 USD | `+0.58` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `4.32` | `4.44` | `4.31` | `4.42` | `17,257,912` | 75,510,006.79 USD | -1,093,709.03 USD | `-1.45%` | -16,765,834.34 USD | `+1.00` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `4.42` | `4.66` | `4.38` | `4.65` | `38,831,237` | 175,324,190.65 USD | 4,409,027.10 USD | `+2.51%` | -12,356,807.24 USD | `+1.01` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `4.65` | `4.69` | `4.38` | `4.40` | `28,351,581` | 128,263,626.10 USD | -4,168,943.82 USD | `-3.25%` | -16,525,751.06 USD | `-0.01` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `4.40` | `4.41` | `4.04` | `4.06` | `71,964,012` | 300,508,235.77 USD | -12,043,039.27 USD | `-4.01%` | -28,568,790.33 USD | `-0.87` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `4.06` | `4.17` | `3.90` | `4.16` | `46,135,129` | 185,302,753.20 USD | -941,303.40 USD | `-0.51%` | -29,510,093.73 USD | `+0.58` | **`BEARISH`** | `BEARISH ABSORPTION` |

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
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 09:33:32 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `66` | `0x7737...bf66` | `LONG` | 23,312,521.30 USD | `5,640,376.30` | `2.35` | `4.13` | `0.8340` | 10,040,618.48 USD | `+43.07%` | `10X Cross` |
| `105` | `0xefe4...194b` | `SHORT` | 18,624,008.65 USD | `4,507,262.50` | `4.21` | `4.13` | `6.64` | 351,088.06 USD | `+1.89%` | `5X Cross` |
| `135` | `0xb581...6f4f` | `LONG` | 14,876,640.00 USD | `3,600,000.00` | `5.19` | `4.13` | `0.000000` | -3,816,395.22 USD | `-25.65%` | `4X Cross` |
| `217` | `0xdd53...2b13` | `SHORT` | 9,917,634.66 USD | `2,400,202.00` | `2.31` | `4.13` | `29.51` | -4,371,786.11 USD | `-44.08%` | `3X Cross` |
| `273` | `0x77ee...2902` | `LONG` | 8,537,202.19 USD | `2,063,023.10` | `1.93` | `4.13` | `0.000000` | 4,546,006.26 USD | `+53.25%` | `10X Cross` |
| `365` | `0x9df2...c665` | `SHORT` | 6,259,906.46 USD | `1,514,579.00` | `2.36` | `4.13` | `24.19` | -2,679,916.80 USD | `-42.81%` | `10X Cross` |
| `379` | `0xb83d...6e36` | `SHORT` | 5,976,912.70 USD | `1,445,759.10` | `5.19` | `4.13` | `94.59` | 1,532,536.25 USD | `+25.64%` | `3X Cross` |
| `380` | `0x7fda...17d1` | `SHORT` | 5,967,845.50 USD | `1,443,915.10` | `4.28` | `4.13` | `29.41` | 214,233.02 USD | `+3.59%` | `10X Cross` |
| `398` | `0xb46b...538e` | `SHORT` | 5,519,016.00 USD | `1,336,000.00` | `4.33` | `4.13` | `7.49` | 265,848.06 USD | `+4.82%` | `10X Cross` |
| `474` | `0x60b0...991e` | `LONG` | 4,634,922.90 USD | `1,121,307.10` | `5.00` | `4.13` | `0.000000` | -966,501.53 USD | `-20.85%` | `10X Cross` |
| `499` | `0xcac1...26b3` | `SHORT` | 4,439,501.53 USD | `1,073,743.90` | `2.48` | `4.13` | `12.20` | -1,779,558.07 USD | `-40.08%` | `10X Cross` |
| `516` | `0x781e...96b7` | `SHORT` | 4,293,878.88 USD | `1,039,604.60` | `2.45` | `4.13` | `7.52` | -1,749,541.69 USD | `-40.75%` | `10X Cross` |
| `598` | `0x45d2...4029` | `SHORT` | 3,756,731.40 USD | `909,400.00` | `3.26` | `4.13` | `49.47` | -790,581.50 USD | `-21.04%` | `10X Cross` |
| `603` | `0x4cae...7c34` | `LONG` | 3,721,227.14 USD | `900,587.40` | `3.97` | `4.13` | `2.95` | 143,034.35 USD | `+3.84%` | `10X Cross` |
| `837` | `0x005a...61fe` | `LONG` | 2,696,494.78 USD | `652,414.60` | `2.08` | `4.13` | `2.41` | 1,338,963.55 USD | `+49.66%` | `7X Cross` |
| `844` | `0xba5d...a352` | `SHORT` | 2,675,863.30 USD | `647,532.50` | `2.83` | `4.13` | `13.70` | -843,148.36 USD | `-31.51%` | `10X Cross` |
| `855` | `0xb695...a92d` | `SHORT` | 2,642,008.54 USD | `639,231.70` | `4.57` | `4.13` | `45.45` | 281,350.39 USD | `+10.65%` | `10X Cross` |
| `859` | `0xd1dd...9e85` | `SHORT` | 2,638,603.22 USD | `637,621.00` | `4.96` | `4.13` | `18.56` | 524,869.51 USD | `+19.89%` | `10X Cross` |
| `865` | `0x123d...3bff` | `SHORT` | 2,625,440.98 USD | `635,392.30` | `2.09` | `4.13` | `9.14` | -1,299,492.51 USD | `-49.50%` | `10X Cross` |
| `877` | `0xcf53...ee11` | `SHORT` | 2,566,766.27 USD | `621,598.40` | `5.07` | `4.13` | `25.46` | 585,403.98 USD | `+22.81%` | `10X Cross` |
| `1000` | `0xbfc7...80b4` | `SHORT` | 2,194,092.00 USD | `531,000.00` | `2.01` | `4.13` | `7.39` | -1,128,892.61 USD | `-51.45%` | `10X Cross` |
| `1261` | `0x0eec...d4c5` | `LONG` | 1,744,981.20 USD | `422,309.10` | `4.01` | `4.13` | `1.18` | 52,937.46 USD | `+3.03%` | `10X Cross` |
| `1307` | `0xe097...d0fe` | `LONG` | 1,652,000.00 USD | `400,000.00` | `5.29` | `4.13` | `0.000000` | -464,787.30 USD | `-28.13%` | `10X Cross` |
| `1447` | `0x6e8f...4364` | `LONG` | 1,493,280.33 USD | `361,210.50` | `3.28` | `4.13` | `3.52` | 309,220.10 USD | `+20.71%` | `10X Cross` |
| `1456` | `0xef96...9383` | `SHORT` | 1,475,452.33 USD | `357,165.90` | `4.50` | `4.13` | `14.21` | 132,789.46 USD | `+9.00%` | `10X Cross` |
| `1484` | `0xcf67...eb24` | `LONG` | 1,448,125.00 USD | `350,000.00` | `1.98` | `4.13` | `1.57` | 756,507.12 USD | `+52.24%` | `10X Cross` |
| `1485` | `0xdf95...7d72` | `SHORT` | 1,447,694.08 USD | `350,446.40` | `4.23` | `4.13` | `111.14` | 35,505.11 USD | `+2.45%` | `10X Cross` |
| `1602` | `0xfc27...9d9d` | `SHORT` | 1,322,582.49 USD | `319,997.70` | `5.01` | `4.13` | `61.21` | 280,960.13 USD | `+21.24%` | `10X Cross` |
| `1606` | `0x089f...a4f8` | `LONG` | 1,318,829.29 USD | `319,043.30` | `4.06` | `4.13` | `0.000000` | 23,972.58 USD | `+1.82%` | `1X Cross` |
| `1632` | `0x9aa5...58af` | `SHORT` | 1,290,437.24 USD | `312,303.30` | `4.78` | `4.13` | `33.24` | 201,950.94 USD | `+15.65%` | `10X Cross` |
| `1669` | `0x17c3...a868` | `LONG` | 1,259,323.73 USD | `304,921.00` | `4.36` | `4.13` | `0.000000` | -71,257.71 USD | `-5.66%` | `3X Cross` |
| `1691` | `0x9836...457e` | `LONG` | 1,239,002.48 USD | `300,000.60` | `4.57` | `4.13` | `1.87` | -133,070.69 USD | `-10.74%` | `10X Cross` |
| `1737` | `0xe065...0f85` | `SHORT` | 1,190,563.32 USD | `288,027.90` | `2.81` | `4.13` | `5.60` | -380,010.20 USD | `-31.92%` | `10X Cross` |
| `1940` | `0xff43...d924` | `LONG` | 1,032,475.17 USD | `249,474.50` | `4.64` | `4.13` | `3.28` | -125,568.51 USD | `-12.16%` | `10X Isolated` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `5.00` | 5,000.00 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Liquidated Short: 5.00K USD at 5.0000 USD [API] | `2026-10-12 23:39:10` |
| `ANNOUNCEMENT` | `INFO` | `4.72` | 6,698.21 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Whale SELL: 6.70K USD at 4.7237 USD [API] | `2026-10-29 00:27:21` |
| `ANNOUNCEMENT` | `INFO` | `4.72` | 5,843.84 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Whale SELL: 5.84K USD at 4.7242 USD [API] | `2026-10-29 00:29:14` |
| `ANNOUNCEMENT` | `INFO` | `4.69` | 6,417.66 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Whale BUY: 6.42K USD at 4.6899 USD [API] | `2026-10-29 00:52:41` |
| `ANNOUNCEMENT` | `INFO` | `4.69` | 14,286.93 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Whale SELL: 14.29K USD at 4.6907 USD [API] | `2026-10-29 00:52:26` |
| `ANNOUNCEMENT` | `INFO` | `4.67` | 5,170.82 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Whale SELL: 5.17K USD at 4.6744 USD [API] | `2026-10-29 00:57:59` |
| `ANNOUNCEMENT` | `INFO` | `4.66` | 8,960.91 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Whale SELL: 8.96K USD at 4.6601 USD [API] | `2026-10-29 01:18:47` |
| `ANNOUNCEMENT` | `INFO` | `4.62` | 8,623.49 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Whale BUY: 8.62K USD at 4.6189 USD [API] | `2026-10-29 01:33:58` |
| `ANNOUNCEMENT` | `INFO` | `4.58` | 7,940.40 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Whale BUY: 7.94K USD at 4.5795 USD [API] | `2026-10-29 01:39:37` |
| `ANNOUNCEMENT` | `INFO` | `4.51` | 2,645.11 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Liquidated Short: 2.65K USD at 4.5123 USD [API] | `2026-10-29 01:49:15` |
| `ANNOUNCEMENT` | `INFO` | `4.52` | 3,997.91 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Liquidated Short: 4.00K USD at 4.5169 USD [API] | `2026-10-29 01:49:08` |
| `ANNOUNCEMENT` | `INFO` | `4.53` | 9,057.60 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Whale SELL: 9.06K USD at 4.5288 USD [API] | `2026-10-29 01:50:32` |
| `ANNOUNCEMENT` | `INFO` | `4.53` | 9,830.42 USD | `-` | `NEWS_INTEL` | `-` | #NEAR Whale BUY: 9.83K USD at 4.5314 USD [API] | `2026-10-29 01:50:29` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`4.42` (Vol: 795,900.00 USD, Dist: `+6.28%`) | Long MP=`3.90` (Vol: 238,000.00 USD, Dist: `--6.19%`)
  * 48H Horizon: Short MP=`4.41` (Vol: 795,900.00 USD, Dist: `+6.20%`) | Long MP=`3.90` (Vol: 238,000.00 USD, Dist: `--6.21%`)
  * 3D Horizon: Short MP=`4.41` (Vol: 795,900.00 USD, Dist: `+6.20%`) | Long MP=`3.90` (Vol: 238,000.00 USD, Dist: `--6.21%`)
  * 7D Horizon: Short MP=`5.01` (Vol: 953,300.00 USD, Dist: `+20.52%`) | Long MP=`3.90` (Vol: 238,000.00 USD, Dist: `--6.18%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long Liquidation` | `0.8350` | 3,400.00 USD | 21,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8450` | 806.81 USD | 21,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8550` | 2,060.00 USD | 21,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8650` | 433.80 USD | 21,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8750` | 1,160.00 USD | 21,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8850` | 751.19 USD | 21,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.8950` | 38,570.00 USD | 21,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9050` | 713.23 USD | 21,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9150` | 12,280.00 USD | 21,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9450` | 523.34 USD | 21,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9550` | 1,240.00 USD | 21,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9650` | 3,340.00 USD | 21,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9750` | 9,870.00 USD | 21,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9850` | 707.53 USD | 21,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.9950` | 154,200.00 USD | 21,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.00` | 21,400.00 USD | 21,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.02` | 15,410.00 USD | 21,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.03` | 5,070.00 USD | 21,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.04` | 34,960.00 USD | 21,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.05` | 4,330.00 USD | 21,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.06` | 892.90 USD | 21,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.07` | 7,510.00 USD | 21,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.08` | 216.89 USD | 21,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.09` | 2,730.00 USD | 21,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.11` | 557.50 USD | 21,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.12` | 178.20 USD | 21,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.14` | 21,740.00 USD | 21,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.15` | 26,620.00 USD | 21,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.18` | 647.54 USD | 21,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.20` | 128.46 USD | 21,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.22` | 545,080.00 USD | 21,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.24` | 1,200.00 USD | 20,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.25` | 416.83 USD | 20,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.25` | 13,040.00 USD | 20,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.26` | 2,060.00 USD | 20,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.27` | 5,090.00 USD | 20,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.28` | 9,860.00 USD | 20,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.30` | 234.51 USD | 20,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.32` | 3,360.00 USD | 20,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.34` | 2,100.00 USD | 20,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.35` | 2,000.00 USD | 20,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.36` | 1,640.00 USD | 20,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.38` | 12,720.00 USD | 20,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.39` | 1,360.00 USD | 20,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.40` | 931.86 USD | 20,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.42` | 82,080.00 USD | 20,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.43` | 3,860.00 USD | 20,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.44` | 762.85 USD | 20,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.45` | 30,680.00 USD | 20,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.46` | 145,240.00 USD | 20,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.48` | 4,360.00 USD | 20,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.50` | 438.63 USD | 20,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.50` | 1,250.00 USD | 20,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.51` | 454.50 USD | 20,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.53` | 2,110.00 USD | 20,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.56` | 20,570.00 USD | 20,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.57` | 919.17 USD | 20,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.58` | 1,980.00 USD | 20,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.59` | 4,340.00 USD | 20,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.60` | 80,440.00 USD | 20,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.62` | 207.19 USD | 20,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.64` | 32,940.00 USD | 20,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.65` | 981.08 USD | 20,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.66` | 113.70 USD | 20,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.67` | 1,830.00 USD | 20,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.68` | 2,790.00 USD | 20,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.69` | 615,660.00 USD | 20,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.70` | 254.25 USD | 19,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.71` | 2,190.00 USD | 19,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.72` | 188.65 USD | 19,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.73` | 6,150.00 USD | 19,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.74` | 7,770.00 USD | 19,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.75` | 1,320.00 USD | 19,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.75` | 91,070.00 USD | 19,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.77` | 3,470.00 USD | 19,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.80` | 2,930.00 USD | 19,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.81` | 6,870.00 USD | 19,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.82` | 909,920.00 USD | 19,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.83` | 28,850.00 USD | 18,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.84` | 4,160.00 USD | 18,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.85` | 984.26 USD | 18,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.89` | 600,480.00 USD | 18,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.90` | 2,250.00 USD | 17,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.91` | 4,610.00 USD | 17,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.92` | 5,860.00 USD | 17,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.93` | 1,870.00 USD | 17,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.95` | 2,740.00 USD | 17,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.96` | 16,430.00 USD | 17,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.97` | 3,550.00 USD | 17,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.98` | 34,950.00 USD | 17,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.99` | 1,490.00 USD | 17,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.00` | 1,000.00 USD | 17,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.02` | 1,640.00 USD | 17,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.02` | 260.62 USD | 17,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.04` | 3,460.00 USD | 17,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.06` | 411.00 USD | 17,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.06` | 6,070.00 USD | 17,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.08` | 115,690.00 USD | 17,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.08` | 19,630.00 USD | 17,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.10` | 1,910.00 USD | 17,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.10` | 6,980.00 USD | 17,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.12` | 355,570.00 USD | 17,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.12` | 35,160.00 USD | 17,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.13` | 1,660.00 USD | 17,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.15` | 1,150.00 USD | 17,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.15` | 1,020.00 USD | 17,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.17` | 190,720.00 USD | 17,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.17` | 19,250.00 USD | 16,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.19` | 92,620.00 USD | 16,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.19` | 10,120.00 USD | 16,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.21` | 44,560.00 USD | 16,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.21` | 1,200.00 USD | 16,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.23` | 1,620.00 USD | 16,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.23` | 2,590.00 USD | 16,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.25` | 311,490.00 USD | 16,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.25` | 149,240.00 USD | 16,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.27` | 379,560.00 USD | 16,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.29` | 463.86 USD | 15,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.29` | 2,860.00 USD | 15,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.31` | 43,180.00 USD | 15,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.31` | 1,970.00 USD | 15,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.33` | 2,690.00 USD | 15,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.33` | 13,800.00 USD | 15,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.35` | 26,070.00 USD | 15,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.35` | 30,610.00 USD | 15,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.37` | 3,450.00 USD | 15,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.38` | 533,900.00 USD | 15,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.38` | 5,860.00 USD | 15,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.40` | 115.20 USD | 15,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.42` | 420,800.00 USD | 15,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.42` | 1,860,000.00 USD | 14,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.44` | 2,320.00 USD | 13,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.44` | 3,830.00 USD | 13,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.46` | 35,430.00 USD | 13,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.46` | 18,070.00 USD | 12,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.48` | 21,470.00 USD | 12,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.48` | 76,980.00 USD | 12,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.50` | 1,110.00 USD | 12,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.50` | 6,000.00 USD | 12,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.52` | 1,290.00 USD | 12,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.52` | 29,000.00 USD | 12,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.54` | 254,240.00 USD | 12,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.54` | 35,030.00 USD | 12,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.56` | 2,880.00 USD | 12,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.56` | 10,170.00 USD | 12,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.58` | 1,260.00 USD | 12,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.58` | 905.27 USD | 12,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.60` | 116,650.00 USD | 12,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.60` | 3,580.00 USD | 12,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.62` | 13,670.00 USD | 12,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.62` | 1,180.00 USD | 12,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.63` | 37,330.00 USD | 12,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.65` | 2,650.00 USD | 12,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.65` | 16,760.00 USD | 12,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.67` | 12,860.00 USD | 12,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.67` | 7,140.00 USD | 12,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.69` | 4,970.00 USD | 12,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.69` | 3,260.00 USD | 12,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.71` | 120,220.00 USD | 12,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.71` | 25,340.00 USD | 12,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.73` | 27,780.00 USD | 12,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.73` | 13,540.00 USD | 12,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.75` | 41,170.00 USD | 12,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.75` | 25,260.00 USD | 12,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.77` | 349,840.00 USD | 12,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.77` | 398.77 USD | 11,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.79` | 51,460.00 USD | 11,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.79` | 26,200.00 USD | 11,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.81` | 94,090.00 USD | 11,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.81` | 4,110.00 USD | 11,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.83` | 8,640.00 USD | 11,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.83` | 1,710.00 USD | 11,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.85` | 3,030.00 USD | 11,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.85` | 5,640.00 USD | 11,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.87` | 8,690.00 USD | 11,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.88` | 405,640.00 USD | 11,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.88` | 93,770.00 USD | 11,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.90` | 16,720.00 USD | 10,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.90` | 94,420.00 USD | 10,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.92` | 85,280.00 USD | 10,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.92` | 47,510.00 USD | 10,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.94` | 49,960.00 USD | 10,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.94` | 18,120.00 USD | 10,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.96` | 1,470.00 USD | 10,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.96` | 6,880.00 USD | 10,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.98` | 43,150.00 USD | 10,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.98` | 206,990.00 USD | 10,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.00` | 2,000.00 USD | 10,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.00` | 10,410.00 USD | 10,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.02` | 21,690.00 USD | 10,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.02` | 20,590.00 USD | 10,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.04` | 17,500.00 USD | 10,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.04` | 374,580.00 USD | 10,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.06` | 23,800.00 USD | 9,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.06` | 115,550.00 USD | 9,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.08` | 91,140.00 USD | 9,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.08` | 31,900.00 USD | 9,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.10` | 5,590.00 USD | 9,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.10` | 24,750.00 USD | 9,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.12` | 32,910.00 USD | 9,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.12` | 22,120.00 USD | 9,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.13` | 7,780.00 USD | 9,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.15` | 220,990.00 USD | 9,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.15` | 168,940.00 USD | 9,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.17` | 91,330.00 USD | 9,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.17` | 26,600.00 USD | 9,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.19` | 245,670.00 USD | 9,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.21` | 9,520.00 USD | 8,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.21` | 16,350.00 USD | 8,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.23` | 23,780.00 USD | 8,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.23` | 43,870.00 USD | 8,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.25` | 74,100.00 USD | 8,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.25` | 5,640.00 USD | 8,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.27` | 52,930.00 USD | 8,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.27` | 868,070.00 USD | 8,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.29` | 3,180.00 USD | 7,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.29` | 133,280.00 USD | 7,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.31` | 125,000.00 USD | 7,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.31` | 17,590.00 USD | 7,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.33` | 9,990.00 USD | 7,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.33` | 74,540.00 USD | 7,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.35` | 31,800.00 USD | 7,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.35` | 2,440.00 USD | 7,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.37` | 141,980.00 USD | 7,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.38` | 69,770.00 USD | 7,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.38` | 54,830.00 USD | 7,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.40` | 10,810.00 USD | 7,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.40` | 98,820.00 USD | 7,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.42` | 552,690.00 USD | 7,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.42` | 38,260.00 USD | 6,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.44` | 34,830.00 USD | 6,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.44` | 13,870.00 USD | 6,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.46` | 12,320.00 USD | 6,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.46` | 14,030.00 USD | 6,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.48` | 181,230.00 USD | 6,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.48` | 24,690.00 USD | 6,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.50` | 62,550.00 USD | 6,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.50` | 32,800.00 USD | 6,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.52` | 8,020.00 USD | 6,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.52` | 205,380.00 USD | 6,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.54` | 1,440,000.00 USD | 5,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.54` | 168,380.00 USD | 4,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.56` | 383,600.00 USD | 4,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.56` | 8,960.00 USD | 3,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.58` | 43,530.00 USD | 3,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.58` | 34,670.00 USD | 3,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.59` | 12,300,000.00 USD | 12,300,000.00 USD | 176,290.00 USD | 66,810.00 USD | 144,570.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.60` | 24,080.00 USD | 3,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.60` | 11,920,000.00 USD | 11,920,000.00 USD | 64,170.00 USD | 21,460.00 USD | 22,050.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.60` | 60,200.00 USD | 3,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.61` | 11,810,000.00 USD | 11,810,000.00 USD | 55,130.00 USD | 17,400.00 USD | 44,890.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.62` | 21,040.00 USD | 3,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `3.62` | 11,690,000.00 USD | 11,690,000.00 USD | 92,130.00 USD | 26,640.00 USD | 97,570.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.62` | 125,390.00 USD | 3,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.63` | 5,930,000.00 USD | 5,930,000.00 USD | 1,910.00 USD | 9,650.00 USD | 22,610.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.63` | 11,480,000.00 USD | 11,480,000.00 USD | 50,840.00 USD | 8,120.00 USD | 159.02 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.63` | 10,560.00 USD | 3,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.64` | 5,900,000.00 USD | 5,900,000.00 USD | 152.80 USD | 5,040.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.64` | 11,420,000.00 USD | 11,420,000.00 USD | 2,410.00 USD | 14,370.00 USD | 119,140.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.65` | 50,500.00 USD | 3,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.65` | 5,890,000.00 USD | 5,890,000.00 USD | 386.30 USD | 0.00 USD | 13.37 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.65` | 11,280,000.00 USD | 11,280,000.00 USD | 52,910.00 USD | 7,050.00 USD | 31,190.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.65` | 14,180.00 USD | 3,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.66` | 5,890,000.00 USD | 5,890,000.00 USD | 291.38 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.66` | 11,190,000.00 USD | 11,190,000.00 USD | 30,480.00 USD | 15,090.00 USD | 125,270.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.67` | 50,850.00 USD | 3,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.67` | 5,890,000.00 USD | 5,890,000.00 USD | 16,750.00 USD | 3,070.00 USD | 11,520.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.67` | 11,020,000.00 USD | 11,020,000.00 USD | 47,650.00 USD | 14,480.00 USD | 53,670.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.67` | 87,540.00 USD | 3,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.68` | 5,860,000.00 USD | 5,860,000.00 USD | 216.77 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.69` | 146,340.00 USD | 3,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.69` | 5,860,000.00 USD | 5,860,000.00 USD | 23,960.00 USD | 0.00 USD | 281.19 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.69` | 10,900,000.00 USD | 10,900,000.00 USD | 27,750.00 USD | 0.00 USD | 59,840.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.69` | 94,330.00 USD | 3,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.70` | 5,840,000.00 USD | 5,840,000.00 USD | 39,190.00 USD | 4,110.00 USD | 55,010.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.70` | 10,820,000.00 USD | 10,820,000.00 USD | 20,470.00 USD | 7,370.00 USD | 112,470.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.71` | 212,700.00 USD | 3,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.71` | 5,740,000.00 USD | 5,740,000.00 USD | 430.40 USD | 0.00 USD | 522.93 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.71` | 10,680,000.00 USD | 10,680,000.00 USD | 50,620.00 USD | 0.00 USD | 74,330.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.71` | 15,680.00 USD | 2,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.72` | 5,740,000.00 USD | 5,740,000.00 USD | 403.05 USD | 0.00 USD | 18.60 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.72` | 10,550,000.00 USD | 10,550,000.00 USD | 425.03 USD | 0.00 USD | 183.06 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.73` | 271,510.00 USD | 2,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.73` | 5,740,000.00 USD | 5,740,000.00 USD | 8,890.00 USD | 6,020.00 USD | 8,370.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.73` | 10,550,000.00 USD | 10,550,000.00 USD | 38,260.00 USD | 10,880.00 USD | 56,790.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.73` | 394,290.00 USD | 2,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.74` | 5,710,000.00 USD | 5,710,000.00 USD | 94,200.00 USD | 33,110.00 USD | 42,360.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.74` | 10,440,000.00 USD | 10,440,000.00 USD | 128,440.00 USD | 40,020.00 USD | 122,480.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.75` | 39,750.00 USD | 2,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.75` | 5,540,000.00 USD | 5,540,000.00 USD | 0.00 USD | 0.00 USD | 20,450.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.75` | 10,150,000.00 USD | 10,150,000.00 USD | 1,770.00 USD | 24,350.00 USD | 42,760.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.75` | 153,580.00 USD | 2,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.76` | 5,520,000.00 USD | 5,520,000.00 USD | 0.00 USD | 2,230.00 USD | 10,030.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.76` | 10,080,000.00 USD | 10,080,000.00 USD | 32,650.00 USD | 10,110.00 USD | 22,610.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.77` | 69,750.00 USD | 1,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.77` | 5,510,000.00 USD | 5,510,000.00 USD | 187.12 USD | 5,330.00 USD | 2,020.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.77` | 10,020,000.00 USD | 10,020,000.00 USD | 13,170.00 USD | 8,090.00 USD | 23,020.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.77` | 67,960.00 USD | 1,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.78` | 5,500,000.00 USD | 5,500,000.00 USD | 106.91 USD | 4,490.00 USD | 29,810.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.78` | 9,970,000.00 USD | 9,970,000.00 USD | 21,640.00 USD | 15,520.00 USD | 41,570.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.79` | 46,300.00 USD | 1,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.79` | 5,470,000.00 USD | 5,470,000.00 USD | 472.79 USD | 0.00 USD | 176.51 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.79` | 9,900,000.00 USD | 9,900,000.00 USD | 49,420.00 USD | 0.00 USD | 38,980.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.79` | 145,620.00 USD | 1,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.80` | 5,470,000.00 USD | 5,470,000.00 USD | 1,270.00 USD | 0.00 USD | 1,720.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.80` | 9,810,000.00 USD | 9,810,000.00 USD | 1,530.00 USD | 18,170.00 USD | 17,780.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.81` | 472,430.00 USD | 1,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.81` | 5,470,000.00 USD | 5,470,000.00 USD | 54,290.00 USD | 0.00 USD | 13,100.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.81` | 9,770,000.00 USD | 9,770,000.00 USD | 0.00 USD | 0.00 USD | 1,350.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.81` | 202,270.00 USD | 1,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.82` | 5,400,000.00 USD | 5,400,000.00 USD | 487.48 USD | 11,960.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.82` | 9,770,000.00 USD | 9,770,000.00 USD | 527.85 USD | 18,370.00 USD | 25,600.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.83` | 159,740.00 USD | 960,370.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.83` | 5,390,000.00 USD | 5,390,000.00 USD | 1,150.00 USD | 18,900.00 USD | 17,280.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.83` | 9,720,000.00 USD | 9,720,000.00 USD | 0.00 USD | 0.00 USD | 89.29 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.83` | 207,570.00 USD | 800,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.84` | 5,350,000.00 USD | 5,350,000.00 USD | 0.00 USD | 0.00 USD | 784.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.84` | 9,720,000.00 USD | 9,720,000.00 USD | 2,020.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.85` | 133,920.00 USD | 593,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.85` | 5,350,000.00 USD | 5,350,000.00 USD | 929.01 USD | 6,330.00 USD | 141.64 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.85` | 9,720,000.00 USD | 9,720,000.00 USD | 0.00 USD | 0.00 USD | 5,500.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.85` | 122,550.00 USD | 459,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.86` | 5,340,000.00 USD | 5,340,000.00 USD | 2,080.00 USD | 12,320.00 USD | 54,290.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.86` | 9,720,000.00 USD | 9,720,000.00 USD | 2,220.00 USD | 0.00 USD | 72,520.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.87` | 27,290.00 USD | 336,590.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.87` | 5,270,000.00 USD | 5,270,000.00 USD | 1,690.00 USD | 11,800.00 USD | 845.92 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.87` | 9,640,000.00 USD | 9,640,000.00 USD | 57,040.00 USD | 0.00 USD | 29,890.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.88` | 136,810.00 USD | 309,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.88` | 5,260,000.00 USD | 5,260,000.00 USD | 106,680.00 USD | 6,860.00 USD | 39,950.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.88` | 9,550,000.00 USD | 9,550,000.00 USD | 106,950.00 USD | 8,890.00 USD | 101,810.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.88` | 88,930.00 USD | 172,490.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.89` | 5,100,000.00 USD | 5,100,000.00 USD | 113,490.00 USD | 37,150.00 USD | 23,350.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.89` | 9,340,000.00 USD | 9,340,000.00 USD | 1,210.00 USD | 50,710.00 USD | 1,390.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.90` | 75,910.00 USD | 83,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `3.90` | 4,930,000.00 USD | 4,930,000.00 USD | 31,410.00 USD | 10,910.00 USD | 21,360.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `3.90` | 9,280,000.00 USD | 9,280,000.00 USD | 171,750.00 USD | 28,250.00 USD | 51,570.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `3.90` | 4,350.00 USD | 7,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
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
| `Live` | `Long Liquidation` | `3.98` | 3,300.00 USD | 3,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
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
| `1D` | `Short Liquidation` | `4.12` | 309,660.00 USD | 309,660.00 USD | 0.00 USD | 80,980.00 USD | 228,680.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.12` | 1,450.00 USD | 1,450.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.13` | 471,110.00 USD | 471,110.00 USD | 0.00 USD | 0.00 USD | 161,450.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.13` | 6,730.00 USD | 8,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.14` | 531,130.00 USD | 531,130.00 USD | 60,020.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.14` | 377,250.00 USD | 377,250.00 USD | 0.00 USD | 90,830.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.14` | 1,430.00 USD | 9,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.15` | 595,400.00 USD | 595,400.00 USD | 64,270.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.15` | 431,140.00 USD | 431,140.00 USD | 0.00 USD | 53,890.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.16` | 638.21 USD | 10,250.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.17` | 664,710.00 USD | 664,710.00 USD | 0.00 USD | 16,800.00 USD | 52,510.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.17` | 10,040.00 USD | 20,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.18` | 874,490.00 USD | 874,490.00 USD | 192,730.00 USD | 17,040.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.18` | 54,820.00 USD | 75,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.19` | 1,250,000.00 USD | 1,250,000.00 USD | 174,270.00 USD | 20,540.00 USD | 185,170.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.20` | 666.59 USD | 75,780.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `4.20` | 1,030,000.00 USD | 1,030,000.00 USD | 227,690.00 USD | 0.00 USD | 371,630.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.21` | 4,460.00 USD | 80,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.21` | 1,330,000.00 USD | 1,330,000.00 USD | 58,200.00 USD | 20,820.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.21` | 837.10 USD | 81,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.22` | 1,530,000.00 USD | 1,530,000.00 USD | 97,990.00 USD | 27,150.00 USD | 74,260.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.22` | 1,060.00 USD | 82,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.23` | 2,200,000.00 USD | 2,200,000.00 USD | 203,550.00 USD | 468,020.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.24` | 5,820.00 USD | 87,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.24` | 2,880,000.00 USD | 2,880,000.00 USD | 506,300.00 USD | 0.00 USD | 173,430.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.25` | 649.06 USD | 88,610.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.25` | 3,210,000.00 USD | 3,210,000.00 USD | 0.00 USD | 72,920.00 USD | 255,640.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.25` | 1,090,000.00 USD | 1,090,000.00 USD | 0.00 USD | 57,340.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.26` | 3,480,000.00 USD | 3,480,000.00 USD | 92,160.00 USD | 173,320.00 USD | 248.22 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.26` | 1,820,000.00 USD | 1,820,000.00 USD | 0.00 USD | 378,440.00 USD | 355,620.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.26` | 208.99 USD | 88,810.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.27` | 4,340,000.00 USD | 4,340,000.00 USD | 677,660.00 USD | 34,890.00 USD | 152,200.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.27` | 3,610,000.00 USD | 3,610,000.00 USD | 18,140.00 USD | 194,220.00 USD | 1,580,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.28` | 4,860.00 USD | 93,680.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.28` | 4,970,000.00 USD | 4,970,000.00 USD | 305,690.00 USD | 30,410.00 USD | 288,910.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.28` | 5,520,000.00 USD | 5,520,000.00 USD | 113,840.00 USD | 497,680.00 USD | 1,300,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.29` | 163.69 USD | 93,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.29` | 5,320,000.00 USD | 5,320,000.00 USD | 153,130.00 USD | 32,690.00 USD | 161,450.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.29` | 5,570,000.00 USD | 5,570,000.00 USD | 0.00 USD | 46,530.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.29` | 207,690.00 USD | 301,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.30` | 5,560,000.00 USD | 5,560,000.00 USD | 32,410.00 USD | 45,120.00 USD | 163,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.30` | 6,040,000.00 USD | 6,040,000.00 USD | 214,920.00 USD | 180,920.00 USD | 75,610.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.30` | 5,070.00 USD | 306,600.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.31` | 5,970,000.00 USD | 5,970,000.00 USD | 304,920.00 USD | 13,580.00 USD | 95,430.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.31` | 6,470,000.00 USD | 6,470,000.00 USD | 213,530.00 USD | 53,890.00 USD | 170,400.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.32` | 31,130.00 USD | 337,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.32` | 6,130,000.00 USD | 6,130,000.00 USD | 86,850.00 USD | 73,400.00 USD | 18.65 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.32` | 7,120,000.00 USD | 7,120,000.00 USD | 265,720.00 USD | 160,980.00 USD | 222,930.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.33` | 373.68 USD | 338,100.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.33` | 6,570,000.00 USD | 6,570,000.00 USD | 255,620.00 USD | 93,880.00 USD | 87,760.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.33` | 7,240,000.00 USD | 7,240,000.00 USD | 2,690.00 USD | 27,170.00 USD | 88,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.34` | 7,090,000.00 USD | 7,090,000.00 USD | 270,720.00 USD | 140,540.00 USD | 114,690.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.34` | 7,420,000.00 USD | 7,420,000.00 USD | 4,550.00 USD | 28,670.00 USD | 141,900.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.34` | 4,130.00 USD | 342,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.35` | 7,180,000.00 USD | 7,180,000.00 USD | 855.62 USD | 0.00 USD | 84,830.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.35` | 7,500,000.00 USD | 7,500,000.00 USD | 0.00 USD | 0.00 USD | 85,370.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.36` | 3,050.00 USD | 345,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.36` | 7,310,000.00 USD | 7,310,000.00 USD | 84,880.00 USD | 12,310.00 USD | 31,110.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.36` | 7,650,000.00 USD | 7,650,000.00 USD | 8,190.00 USD | 0.00 USD | 140,550.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.37` | 7,540,000.00 USD | 7,540,000.00 USD | 52,520.00 USD | 46,860.00 USD | 130,010.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.38` | 1,110.00 USD | 346,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.38` | 8,380,000.00 USD | 8,380,000.00 USD | 248,590.00 USD | 34,500.00 USD | 559,230.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.38` | 8,050,000.00 USD | 8,050,000.00 USD | 0.00 USD | 141,930.00 USD | 261,380.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.39` | 8,710,000.00 USD | 8,710,000.00 USD | 399.48 USD | 17,360.00 USD | 310,880.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.39` | 8,570,000.00 USD | 8,570,000.00 USD | 248,520.00 USD | 108,260.00 USD | 154,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.39` | 192,710.00 USD | 539,100.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.40` | 9,110,000.00 USD | 9,110,000.00 USD | 288,790.00 USD | 34,040.00 USD | 81,970.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.40` | 9,170,000.00 USD | 9,170,000.00 USD | 108,780.00 USD | 26,950.00 USD | 463,990.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.41` | 1,410.00 USD | 540,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.41` | 9,490,000.00 USD | 9,490,000.00 USD | 196,820.00 USD | 112,990.00 USD | 65,530.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.41` | 9,490,000.00 USD | 9,490,000.00 USD | 0.00 USD | 45,930.00 USD | 278,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.42` | 9,540,000.00 USD | 9,540,000.00 USD | 0.00 USD | 47,240.00 USD | 774.54 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.42` | 10,140,000.00 USD | 10,140,000.00 USD | 404,280.00 USD | 71,590.00 USD | 175,990.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.42` | 104.87 USD | 540,610.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.43` | 9,690,000.00 USD | 9,690,000.00 USD | 5,100.00 USD | 49,400.00 USD | 98,670.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.43` | 10,420,000.00 USD | 10,420,000.00 USD | 163,540.00 USD | 46,230.00 USD | 71,660.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.44` | 10,470,000.00 USD | 10,470,000.00 USD | 154,480.00 USD | 339,100.00 USD | 290,890.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.44` | 10,610,000.00 USD | 10,610,000.00 USD | 0.00 USD | 116,400.00 USD | 72,830.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.45` | 10,530,000.00 USD | 10,530,000.00 USD | 649.63 USD | 50,720.00 USD | 1,400.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.46` | 10,540,000.00 USD | 10,540,000.00 USD | 704.30 USD | 9,070.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.46` | 10,680,000.00 USD | 10,680,000.00 USD | 0.00 USD | 62,110.00 USD | 2,080.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.46` | 468.38 USD | 541,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.47` | 10,570,000.00 USD | 10,570,000.00 USD | 210.23 USD | 16,700.00 USD | 18,310.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.47` | 11,020,000.00 USD | 11,020,000.00 USD | 203,160.00 USD | 135,940.00 USD | 2,060.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.47` | 629.18 USD | 541,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.48` | 10,790,000.00 USD | 10,790,000.00 USD | 117,480.00 USD | 73,240.00 USD | 26,920.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.48` | 11,020,000.00 USD | 11,020,000.00 USD | 0.00 USD | 0.00 USD | 1,510.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.49` | 11,350,000.00 USD | 11,350,000.00 USD | 252,600.00 USD | 155,000.00 USD | 150,280.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.49` | 11,360,000.00 USD | 11,360,000.00 USD | 242,770.00 USD | 93,790.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.50` | 90,180.00 USD | 631,890.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.50` | 11,890,000.00 USD | 11,890,000.00 USD | 361,770.00 USD | 65,710.00 USD | 120,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.50` | 11,930,000.00 USD | 11,930,000.00 USD | 373,240.00 USD | 200,700.00 USD | 1,820.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.50` | 283.81 USD | 632,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.51` | 12,700,000.00 USD | 12,700,000.00 USD | 186,860.00 USD | 307,580.00 USD | 312,530.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.51` | 12,010,000.00 USD | 12,010,000.00 USD | 77,780.00 USD | 0.00 USD | 2,030.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.51` | 967.56 USD | 633,140.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.52` | 13,320,000.00 USD | 13,320,000.00 USD | 287,830.00 USD | 92,260.00 USD | 242,880.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.52` | 12,150,000.00 USD | 12,150,000.00 USD | 2,080.00 USD | 0.00 USD | 138,450.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.53` | 18,820.00 USD | 651,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.53` | 14,090,000.00 USD | 14,090,000.00 USD | 487,540.00 USD | 0.00 USD | 279,080.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.53` | 13,130,000.00 USD | 13,130,000.00 USD | 438,070.00 USD | 232,800.00 USD | 309,560.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.54` | 14,810,000.00 USD | 14,810,000.00 USD | 216.65 USD | 150,600.00 USD | 564,340.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.54` | 14,370,000.00 USD | 14,370,000.00 USD | 0.00 USD | 0.00 USD | 1,240,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.54` | 394.51 USD | 652,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.55` | 15,020,000.00 USD | 15,020,000.00 USD | 0.00 USD | 22,540.00 USD | 195,790.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.56` | 15,430,000.00 USD | 15,430,000.00 USD | 79,110.00 USD | 32,800.00 USD | 288,660.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.56` | 14,850,000.00 USD | 14,850,000.00 USD | 361,350.00 USD | 124,220.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.57` | 243.77 USD | 652,600.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.57` | 15,740,000.00 USD | 15,740,000.00 USD | 177,440.00 USD | 70,180.00 USD | 67,980.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.57` | 15,400,000.00 USD | 15,400,000.00 USD | 305,830.00 USD | 27,650.00 USD | 209,310.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.58` | 182,510.00 USD | 835,110.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.58` | 17,200,000.00 USD | 17,200,000.00 USD | 506,750.00 USD | 73,690.00 USD | 875,260.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.58` | 15,530,000.00 USD | 15,530,000.00 USD | 44,380.00 USD | 0.00 USD | 85,990.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.59` | 18,180,000.00 USD | 18,180,000.00 USD | 826,150.00 USD | 75,460.00 USD | 79,420.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.59` | 17,120,000.00 USD | 17,120,000.00 USD | 760,880.00 USD | 40,640.00 USD | 794,930.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.59` | 827.10 USD | 835,940.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.60` | 18,380,000.00 USD | 18,380,000.00 USD | 54,450.00 USD | 84,420.00 USD | 66,160.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.60` | 17,240,000.00 USD | 17,240,000.00 USD | 3,460.00 USD | 112,080.00 USD | 2,360.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.61` | 1,050.00 USD | 836,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.61` | 18,520,000.00 USD | 18,520,000.00 USD | 66,620.00 USD | 7,560.00 USD | 60,990.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.61` | 17,250,000.00 USD | 17,250,000.00 USD | 3,350.00 USD | 0.00 USD | 960.97 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.62` | 3,920.00 USD | 840,910.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.62` | 18,670,000.00 USD | 18,670,000.00 USD | 95,090.00 USD | 31,380.00 USD | 21,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.62` | 17,380,000.00 USD | 17,380,000.00 USD | 134,680.00 USD | 0.00 USD | 2,720.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.63` | 18,670,000.00 USD | 18,670,000.00 USD | 1,040.00 USD | 0.00 USD | 614.32 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.63` | 17,600,000.00 USD | 17,600,000.00 USD | 213,490.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.63` | 990.04 USD | 841,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.64` | 19,080,000.00 USD | 19,080,000.00 USD | 334,190.00 USD | 11,270.00 USD | 63,790.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.64` | 18,120,000.00 USD | 18,120,000.00 USD | 501,930.00 USD | 18,170.00 USD | 1,670.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.64` | 169.54 USD | 842,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.65` | 20,150,000.00 USD | 20,150,000.00 USD | 423,550.00 USD | 52,020.00 USD | 600,100.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.65` | 18,540,000.00 USD | 18,540,000.00 USD | 420,940.00 USD | 0.00 USD | 2,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.66` | 124.75 USD | 842,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.66` | 21,130,000.00 USD | 21,130,000.00 USD | 281,290.00 USD | 316,500.00 USD | 379,880.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.66` | 18,860,000.00 USD | 18,860,000.00 USD | 144,860.00 USD | 18,370.00 USD | 150,940.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.67` | 101.70 USD | 842,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.67` | 21,690,000.00 USD | 21,690,000.00 USD | 184,440.00 USD | 0.00 USD | 378,090.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.67` | 18,900,000.00 USD | 18,900,000.00 USD | 0.00 USD | 0.00 USD | 43,230.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `4.68` | 22,300,000.00 USD | 22,300,000.00 USD | 345,840.00 USD | 81,340.00 USD | 175,700.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.68` | 19,820,000.00 USD | 19,820,000.00 USD | 381,910.00 USD | 83,630.00 USD | 450,700.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.68` | 48,020.00 USD | 890,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.69` | 22,800,000.00 USD | 22,800,000.00 USD | 213,780.00 USD | 40,000.00 USD | 254,150.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.69` | 19,910,000.00 USD | 19,910,000.00 USD | 2,450.00 USD | 0.00 USD | 88,340.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.70` | 230.06 USD | 890,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.70` | 23,140,000.00 USD | 23,140,000.00 USD | 74,090.00 USD | 123,520.00 USD | 143,310.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.70` | 20,220,000.00 USD | 20,220,000.00 USD | 74,240.00 USD | 60,360.00 USD | 181,210.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.71` | 7,480.00 USD | 898,030.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `4.71` | 24,100,000.00 USD | 24,100,000.00 USD | 359,510.00 USD | 284,360.00 USD | 316,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.71` | 20,630,000.00 USD | 20,630,000.00 USD | 178,360.00 USD | 232,800.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.71` | 460.18 USD | 898,490.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `4.72` | 20,820,000.00 USD | 20,820,000.00 USD | 7,140.00 USD | 0.00 USD | 180,490.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.73` | 20,880,000.00 USD | 20,880,000.00 USD | 59,970.00 USD | 0.00 USD | 894.74 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.74` | 21,200,000.00 USD | 21,200,000.00 USD | 14,750.00 USD | 173,100.00 USD | 127,910.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.75` | 4,310.00 USD | 902,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `4.75` | 21,740,000.00 USD | 21,740,000.00 USD | 17,340.00 USD | 185,060.00 USD | 343,810.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.76` | 23,090,000.00 USD | 23,090,000.00 USD | 1,030,000.00 USD | 46,890.00 USD | 272,560.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.76` | 227.77 USD | 903,020.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `4.77` | 24,000,000.00 USD | 24,000,000.00 USD | 731,680.00 USD | 73,410.00 USD | 101,640.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.78` | 8,780.00 USD | 911,810.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `4.78` | 25,350,000.00 USD | 25,350,000.00 USD | 683,730.00 USD | 513,870.00 USD | 154,510.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.79` | 143.55 USD | 911,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `4.79` | 26,380,000.00 USD | 26,380,000.00 USD | 713,060.00 USD | 249,310.00 USD | 72,120.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.79` | 1,330.00 USD | 913,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `4.80` | 27,970,000.00 USD | 27,970,000.00 USD | 1,160,000.00 USD | 432,340.00 USD | 2,480.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.81` | 28,600,000.00 USD | 28,600,000.00 USD | 400,070.00 USD | 125,900.00 USD | 101,780.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.82` | 45,670.00 USD | 958,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `4.82` | 31,370,000.00 USD | 31,370,000.00 USD | 1,010,000.00 USD | 369,430.00 USD | 1,390,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.83` | 3,020.00 USD | 961,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `4.83` | 33,020,000.00 USD | 33,020,000.00 USD | 822,860.00 USD | 85,680.00 USD | 739,630.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.83` | 1,950.00 USD | 963,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `4.84` | 33,510,000.00 USD | 33,510,000.00 USD | 97,300.00 USD | 71,790.00 USD | 322,840.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.84` | 11,220.00 USD | 975,140.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `4.85` | 35,530,000.00 USD | 35,530,000.00 USD | 487,940.00 USD | 366,970.00 USD | 1,160,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.86` | 36,940,000.00 USD | 36,940,000.00 USD | 444,810.00 USD | 162,380.00 USD | 802,380.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.87` | 137.68 USD | 975,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `4.87` | 38,000,000.00 USD | 38,000,000.00 USD | 264,730.00 USD | 136,820.00 USD | 663,430.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.88` | 39,590,000.00 USD | 39,590,000.00 USD | 449,970.00 USD | 340,260.00 USD | 792,630.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.88` | 827.03 USD | 976,110.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `4.89` | 40,170,000.00 USD | 40,170,000.00 USD | 213,960.00 USD | 100,850.00 USD | 272,060.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.90` | 41,310,000.00 USD | 41,310,000.00 USD | 450,550.00 USD | 145,910.00 USD | 541,330.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.91` | 42,750,000.00 USD | 42,750,000.00 USD | 637,320.00 USD | 208,910.00 USD | 590,510.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.92` | 20,720.00 USD | 996,820.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `4.92` | 44,480,000.00 USD | 44,480,000.00 USD | 576,460.00 USD | 277,640.00 USD | 877,920.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.92` | 2,100.00 USD | 998,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `4.93` | 46,040,000.00 USD | 46,040,000.00 USD | 730,010.00 USD | 78,190.00 USD | 749,940.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.93` | 157.43 USD | 999,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `4.94` | 47,380,000.00 USD | 47,380,000.00 USD | 351,940.00 USD | 290,290.00 USD | 696,960.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.95` | 48,680,000.00 USD | 48,680,000.00 USD | 468,360.00 USD | 161,040.00 USD | 670,270.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.96` | 342.89 USD | 999,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `4.96` | 49,910,000.00 USD | 49,910,000.00 USD | 607,770.00 USD | 214,910.00 USD | 410,880.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.97` | 50,290,000.00 USD | 50,290,000.00 USD | 198,220.00 USD | 72,330.00 USD | 113,320.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `4.97` | 99,810.00 USD | 1,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `4.98` | 50,950,000.00 USD | 50,950,000.00 USD | 251,840.00 USD | 102,410.00 USD | 299,870.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `4.99` | 51,300,000.00 USD | 51,300,000.00 USD | 133,330.00 USD | 103,060.00 USD | 117,980.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `5.00` | 339.66 USD | 1,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `5.00` | 52,000,000.00 USD | 52,000,000.00 USD | 210,680.00 USD | 36,180.00 USD | 454,070.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `5.01` | 53,830,000.00 USD | 53,830,000.00 USD | 781,840.00 USD | 255,770.00 USD | 786,470.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `5.02` | 55,280,000.00 USD | 55,280,000.00 USD | 821,860.00 USD | 309,020.00 USD | 321,920.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `5.03` | 56,410,000.00 USD | 56,410,000.00 USD | 385,330.00 USD | 172,880.00 USD | 567,890.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `5.04` | 57,490,000.00 USD | 57,490,000.00 USD | 305,260.00 USD | 163,190.00 USD | 619,980.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `5.05` | 58,940,000.00 USD | 58,940,000.00 USD | 694,310.00 USD | 267,140.00 USD | 486,680.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `5.05` | 35,380.00 USD | 1,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `5.06` | 59,620,000.00 USD | 59,620,000.00 USD | 92,480.00 USD | 165,230.00 USD | 420,210.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `5.07` | 3,420.00 USD | 1,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `5.07` | 60,660,000.00 USD | 60,660,000.00 USD | 358,750.00 USD | 137,080.00 USD | 542,550.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `5.08` | 61,180,000.00 USD | 61,180,000.00 USD | 204,140.00 USD | 167,810.00 USD | 150,010.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `5.08` | 1,090.00 USD | 1,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `5.09` | 61,720,000.00 USD | 61,720,000.00 USD | 105,390.00 USD | 52,790.00 USD | 385,540.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `5.10` | 62,110,000.00 USD | 62,110,000.00 USD | 182,200.00 USD | 0.00 USD | 201,110.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `5.11` | 62,700,000.00 USD | 62,700,000.00 USD | 369,260.00 USD | 78,100.00 USD | 140,600.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `5.12` | 37,150.00 USD | 1,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `5.12` | 63,270,000.00 USD | 63,270,000.00 USD | 303,840.00 USD | 152,530.00 USD | 115,650.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `5.12` | 2,560.00 USD | 1,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `5.13` | 63,840,000.00 USD | 63,840,000.00 USD | 173,190.00 USD | 71,310.00 USD | 325,090.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `5.14` | 64,280,000.00 USD | 64,280,000.00 USD | 140,950.00 USD | 59,640.00 USD | 239,260.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `5.15` | 64,830,000.00 USD | 64,830,000.00 USD | 205,680.00 USD | 82,350.00 USD | 267,910.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `5.16` | 65,350,000.00 USD | 65,350,000.00 USD | 51,850.00 USD | 112,830.00 USD | 347,470.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `5.17` | 751.51 USD | 1,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `5.17` | 65,960,000.00 USD | 65,960,000.00 USD | 280,710.00 USD | 85,040.00 USD | 244,330.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `5.18` | 66,210,000.00 USD | 66,210,000.00 USD | 67,600.00 USD | 63,250.00 USD | 124,260.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `5.18` | 82,840.00 USD | 1,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `5.19` | 66,430,000.00 USD | 66,430,000.00 USD | 69,310.00 USD | 13,680.00 USD | 138,850.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `5.20` | 22,080.00 USD | 1,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `5.20` | 66,680,000.00 USD | 66,680,000.00 USD | 137,830.00 USD | 45,820.00 USD | 65,990.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `5.21` | 66,920,000.00 USD | 66,920,000.00 USD | 105,330.00 USD | 20,850.00 USD | 110,400.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `5.22` | 66,980,000.00 USD | 66,980,000.00 USD | 48,760.00 USD | 13,410.00 USD | 398.26 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `5.22` | 74,720.00 USD | 1,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `5.23` | 67,040,000.00 USD | 67,040,000.00 USD | 5,060.00 USD | 15,520.00 USD | 34,400.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `5.25` | 143.71 USD | 1,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.25` | 1,970.00 USD | 1,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.26` | 16,140.00 USD | 1,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.29` | 134.77 USD | 1,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.30` | 524.66 USD | 1,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.32` | 718.59 USD | 1,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.33` | 1,070,000.00 USD | 2,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.34` | 616.28 USD | 2,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.36` | 142.44 USD | 2,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.41` | 5,410.00 USD | 2,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.43` | 61,270.00 USD | 2,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.45` | 702.41 USD | 2,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.46` | 43,980.00 USD | 2,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.47` | 627.98 USD | 2,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.50` | 66,470.00 USD | 2,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.51` | 38,800.00 USD | 2,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.54` | 209.22 USD | 2,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.57` | 71,830.00 USD | 2,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.58` | 62,580.00 USD | 2,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.59` | 686.51 USD | 2,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.61` | 56,050.00 USD | 2,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.62` | 1,620,000.00 USD | 4,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.67` | 211.30 USD | 4,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.67` | 228.70 USD | 4,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.68` | 26,090.00 USD | 4,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.70` | 1,520.00 USD | 4,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.71` | 2,130.00 USD | 4,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.75` | 4,580.00 USD | 4,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.75` | 286.02 USD | 4,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.80` | 2,670.00 USD | 4,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.82` | 127.93 USD | 4,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.84` | 310.95 USD | 4,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.86` | 848.39 USD | 4,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.87` | 200.00 USD | 4,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.88` | 7,150.00 USD | 4,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.89` | 88,590.00 USD | 4,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.91` | 151.76 USD | 4,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.92` | 189.28 USD | 4,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.92` | 343,290.00 USD | 4,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `5.95` | 103,650.00 USD | 5,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.00` | 388,640.00 USD | 5,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.03` | 345,420.00 USD | 5,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.04` | 196,080.00 USD | 5,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.07` | 740.54 USD | 5,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.08` | 23,590.00 USD | 6,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.08` | 5,920.00 USD | 6,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.09` | 37,510.00 USD | 6,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.13` | 2,430.00 USD | 6,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.18` | 5,270.00 USD | 6,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.24` | 288,250.00 USD | 6,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.25` | 7,300.00 USD | 6,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.25` | 439.10 USD | 6,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.28` | 397.84 USD | 6,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.32` | 310.70 USD | 6,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.33` | 382.00 USD | 6,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.34` | 214.46 USD | 6,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.37` | 2,060.00 USD | 6,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.38` | 1,460.00 USD | 6,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.38` | 2,000.00 USD | 6,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.41` | 5,740.00 USD | 6,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.42` | 8,700.00 USD | 6,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.42` | 173.47 USD | 6,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.43` | 77,220.00 USD | 6,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.45` | 55,720.00 USD | 6,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.46` | 7,150.00 USD | 6,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.46` | 1,940.00 USD | 6,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.49` | 911.79 USD | 6,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.51` | 380.48 USD | 6,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.54` | 265.07 USD | 6,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.58` | 269,120.00 USD | 6,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.59` | 418.78 USD | 6,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.61` | 700.79 USD | 6,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.64` | 29,950,000.00 USD | 36,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.66` | 48,430.00 USD | 36,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.67` | 233.94 USD | 36,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.67` | 200.25 USD | 36,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.68` | 37,150.00 USD | 36,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.75` | 11,490.00 USD | 36,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.75` | 1,250,000.00 USD | 38,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.76` | 90,430.00 USD | 38,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.79` | 15,200.00 USD | 38,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.84` | 753.63 USD | 38,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.87` | 2,650.00 USD | 38,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.88` | 295.62 USD | 38,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.92` | 6,920.00 USD | 38,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `6.99` | 1,310,000.00 USD | 39,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.00` | 190.96 USD | 39,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.03` | 665.27 USD | 39,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.09` | 699.57 USD | 39,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.20` | 171.96 USD | 39,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.21` | 13,560.00 USD | 39,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.24` | 4,910.00 USD | 39,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.32` | 580.08 USD | 39,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.33` | 1,320.00 USD | 39,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.34` | 11,120.00 USD | 39,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.38` | 1,850.00 USD | 39,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.42` | 106,000.00 USD | 39,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.46` | 1,420.00 USD | 39,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.47` | 783.38 USD | 39,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.53` | 10,050,000.00 USD | 49,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.54` | 2,340.00 USD | 49,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.57` | 7,860,000.00 USD | 57,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.58` | 2,630.00 USD | 57,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.58` | 6,030.00 USD | 57,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.62` | 27,330.00 USD | 57,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.63` | 19,210.00 USD | 57,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.67` | 15,390.00 USD | 57,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.72` | 4,100,000.00 USD | 61,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.74` | 505.87 USD | 61,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.75` | 105,820.00 USD | 61,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.79` | 33,540.00 USD | 61,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.79` | 997,510.00 USD | 62,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.87` | 2,980.00 USD | 62,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.88` | 505.58 USD | 62,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.92` | 1,800.00 USD | 62,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.95` | 6,120.00 USD | 62,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.96` | 134,410.00 USD | 63,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `7.99` | 399.25 USD | 63,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `8.03` | 435,420.00 USD | 63,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `0.8350` | 27,620,000.00 USD | 0.00 USD | 388.44 USD | `-79.94%` | `465.20` |
| `Live` | `Long` | `0.8450` | 27,620,000.00 USD | 0.00 USD | 4,770,000.00 USD | `-79.70%` | `5,640,376.30` |
| `Live` | `Long` | `0.8650` | 22,850,000.00 USD | 0.00 USD | 912.83 USD | `-79.22%` | `1,055.30` |
| `Live` | `Long` | `0.8950` | 22,850,000.00 USD | 0.00 USD | 40,360.00 USD | `-78.50%` | `45,091.40` |
| `Live` | `Long` | `0.9050` | 22,810,000.00 USD | 0.00 USD | 3,040.00 USD | `-78.26%` | `3,354.30` |
| `Live` | `Long` | `0.9150` | 22,810,000.00 USD | 0.00 USD | 11,370.00 USD | `-78.02%` | `12,425.00` |
| `Live` | `Long` | `0.9350` | 22,800,000.00 USD | 0.00 USD | 935.00 USD | `-77.54%` | `1,000.00` |
| `Live` | `Long` | `0.9650` | 22,800,000.00 USD | 0.00 USD | 965.00 USD | `-76.82%` | `1,000.00` |
| `Live` | `Long` | `0.9850` | 22,800,000.00 USD | 0.00 USD | 7,800.00 USD | `-76.34%` | `7,918.30` |
| `Live` | `Long` | `0.9950` | 22,790,000.00 USD | 0.00 USD | 154,200.00 USD | `-76.10%` | `154,969.90` |
| `Live` | `Long` | `1.00` | 22,630,000.00 USD | 0.00 USD | 30,990.00 USD | `-75.86%` | `30,836.80` |
| `Live` | `Long` | `1.02` | 22,600,000.00 USD | 0.00 USD | 10,250.00 USD | `-75.38%` | `10,000.00` |
| `Live` | `Long` | `1.03` | 22,590,000.00 USD | 0.00 USD | 5,070.00 USD | `-75.14%` | `4,897.40` |
| `Live` | `Long` | `1.04` | 22,590,000.00 USD | 0.00 USD | 2,740.00 USD | `-74.90%` | `2,617.40` |
| `Live` | `Long` | `1.05` | 22,590,000.00 USD | 0.00 USD | 8,590.00 USD | `-74.66%` | `8,146.90` |
| `Live` | `Long` | `1.06` | 22,580,000.00 USD | 0.00 USD | 99,270.00 USD | `-74.42%` | `93,214.70` |
| `Live` | `Long` | `1.07` | 22,480,000.00 USD | 0.00 USD | 7,510.00 USD | `-74.18%` | `6,989.70` |
| `Live` | `Long` | `1.08` | 22,470,000.00 USD | 0.00 USD | 337.44 USD | `-73.94%` | `311.00` |
| `Live` | `Long` | `1.09` | 22,470,000.00 USD | 0.00 USD | 16,190.00 USD | `-73.70%` | `14,783.90` |
| `Live` | `Long` | `1.11` | 22,450,000.00 USD | 0.00 USD | 557.50 USD | `-73.22%` | `500.00` |
| `Live` | `Long` | `1.12` | 22,450,000.00 USD | 0.00 USD | 856.24 USD | `-72.98%` | `761.10` |
| `Live` | `Long` | `1.14` | 22,450,000.00 USD | 0.00 USD | 13,510.00 USD | `-72.74%` | `11,906.50` |
| `Live` | `Long` | `1.15` | 22,440,000.00 USD | 0.00 USD | 40,820.00 USD | `-72.50%` | `35,649.30` |
| `Live` | `Long` | `1.17` | 22,400,000.00 USD | 0.00 USD | 144.69 USD | `-72.02%` | `124.20` |
| `Live` | `Long` | `1.18` | 22,400,000.00 USD | 0.00 USD | 1,720.00 USD | `-71.78%` | `1,463.50` |
| `Live` | `Long` | `1.19` | 22,400,000.00 USD | 0.00 USD | 3,440.00 USD | `-71.54%` | `2,906.40` |
| `Live` | `Long` | `1.20` | 22,390,000.00 USD | 0.00 USD | 7,390.00 USD | `-71.30%` | `6,187.90` |
| `Live` | `Long` | `1.21` | 22,380,000.00 USD | 0.00 USD | 56,130.00 USD | `-71.06%` | `46,584.90` |
| `Live` | `Long` | `1.23` | 22,330,000.00 USD | 0.00 USD | 517,410.00 USD | `-70.58%` | `422,373.40` |
| `Live` | `Long` | `1.25` | 21,810,000.00 USD | 0.00 USD | 2,190.00 USD | `-70.10%` | `1,756.00` |
| `Live` | `Long` | `1.25` | 21,810,000.00 USD | 0.00 USD | 2,260.00 USD | `-69.86%` | `1,803.00` |
| `Live` | `Long` | `1.26` | 21,810,000.00 USD | 0.00 USD | 2,310.00 USD | `-69.62%` | `1,827.40` |
| `Live` | `Long` | `1.27` | 21,800,000.00 USD | 0.00 USD | 21,840.00 USD | `-69.38%` | `17,125.90` |
| `Live` | `Long` | `1.28` | 21,780,000.00 USD | 0.00 USD | 428.16 USD | `-69.14%` | `333.20` |
| `Live` | `Long` | `1.30` | 21,780,000.00 USD | 0.00 USD | 116.80 USD | `-68.65%` | `89.50` |
| `Live` | `Long` | `1.31` | 21,780,000.00 USD | 0.00 USD | 1,010.00 USD | `-68.41%` | `770.10` |
| `Live` | `Long` | `1.32` | 21,780,000.00 USD | 0.00 USD | 22,870.00 USD | `-68.17%` | `17,259.90` |
| `Live` | `Long` | `1.34` | 21,760,000.00 USD | 0.00 USD | 603.91 USD | `-67.69%` | `449.00` |
| `Live` | `Long` | `1.35` | 21,760,000.00 USD | 0.00 USD | 2,000.00 USD | `-67.45%` | `1,474.80` |
| `Live` | `Long` | `1.36` | 21,760,000.00 USD | 0.00 USD | 2,860.00 USD | `-67.21%` | `2,096.20` |
| `Live` | `Long` | `1.38` | 21,750,000.00 USD | 0.00 USD | 12,380.00 USD | `-66.97%` | `9,000.00` |
| `Live` | `Long` | `1.39` | 21,740,000.00 USD | 0.00 USD | 295.56 USD | `-66.73%` | `213.40` |
| `Live` | `Long` | `1.40` | 21,740,000.00 USD | 0.00 USD | 1,040.00 USD | `-66.49%` | `743.00` |
| `Live` | `Long` | `1.41` | 21,740,000.00 USD | 0.00 USD | 70,820.00 USD | `-66.25%` | `50,407.00` |
| `Live` | `Long` | `1.42` | 21,670,000.00 USD | 0.00 USD | 112,730.00 USD | `-66.01%` | `79,669.00` |
| `Live` | `Long` | `1.43` | 21,560,000.00 USD | 0.00 USD | 1,020.00 USD | `-65.77%` | `714.90` |
| `Live` | `Long` | `1.44` | 21,550,000.00 USD | 0.00 USD | 15,310.00 USD | `-65.53%` | `10,668.30` |
| `Live` | `Long` | `1.45` | 21,540,000.00 USD | 0.00 USD | 1,660.00 USD | `-65.29%` | `1,146.90` |
| `Live` | `Long` | `1.46` | 21,540,000.00 USD | 0.00 USD | 5,440.00 USD | `-65.05%` | `3,738.20` |
| `Live` | `Long` | `1.47` | 21,530,000.00 USD | 0.00 USD | 429.83 USD | `-64.81%` | `293.40` |
| `Live` | `Long` | `1.48` | 21,530,000.00 USD | 0.00 USD | 1,480.00 USD | `-64.57%` | `1,000.00` |
| `Live` | `Long` | `1.50` | 21,530,000.00 USD | 0.00 USD | 576,020.00 USD | `-64.09%` | `385,297.90` |
| `Live` | `Long` | `1.50` | 20,950,000.00 USD | 0.00 USD | 3,420.00 USD | `-63.85%` | `2,271.90` |
| `Live` | `Long` | `1.51` | 20,950,000.00 USD | 0.00 USD | 454.50 USD | `-63.61%` | `300.00` |
| `Live` | `Long` | `1.52` | 20,950,000.00 USD | 0.00 USD | 605.42 USD | `-63.37%` | `397.00` |
| `Live` | `Long` | `1.53` | 20,950,000.00 USD | 0.00 USD | 1,220.00 USD | `-63.13%` | `797.50` |
| `Live` | `Long` | `1.55` | 20,950,000.00 USD | 0.00 USD | 311.00 USD | `-62.65%` | `200.00` |
| `Live` | `Long` | `1.56` | 20,950,000.00 USD | 0.00 USD | 23,700.00 USD | `-62.41%` | `15,146.30` |
| `Live` | `Long` | `1.57` | 20,920,000.00 USD | 0.00 USD | 589.52 USD | `-62.17%` | `374.30` |
| `Live` | `Long` | `1.58` | 20,920,000.00 USD | 0.00 USD | 1,980.00 USD | `-61.93%` | `1,246.60` |
| `Live` | `Long` | `1.59` | 20,920,000.00 USD | 0.00 USD | 15,740.00 USD | `-61.69%` | `9,870.00` |
| `Live` | `Long` | `1.60` | 20,910,000.00 USD | 0.00 USD | 191.64 USD | `-61.45%` | `119.40` |
| `Live` | `Long` | `1.62` | 20,910,000.00 USD | 0.00 USD | 15,250.00 USD | `-60.97%` | `9,387.20` |
| `Live` | `Long` | `1.64` | 20,890,000.00 USD | 0.00 USD | 3,780.00 USD | `-60.73%` | `2,309.30` |
| `Live` | `Long` | `1.65` | 20,890,000.00 USD | 0.00 USD | 2,040.00 USD | `-60.49%` | `1,240.20` |
| `Live` | `Long` | `1.66` | 20,880,000.00 USD | 0.00 USD | 1,320.00 USD | `-60.25%` | `794.90` |
| `Live` | `Long` | `1.67` | 20,880,000.00 USD | 0.00 USD | 574.59 USD | `-60.01%` | `345.10` |
| `Live` | `Long` | `1.68` | 20,880,000.00 USD | 0.00 USD | 1,380.00 USD | `-59.77%` | `823.50` |
| `Live` | `Long` | `1.69` | 20,880,000.00 USD | 0.00 USD | 12,850.00 USD | `-59.53%` | `7,624.50` |
| `Live` | `Long` | `1.70` | 20,870,000.00 USD | 0.00 USD | 169.50 USD | `-59.29%` | `100.00` |
| `Live` | `Long` | `1.71` | 20,870,000.00 USD | 0.00 USD | 2,190.00 USD | `-59.05%` | `1,286.10` |
| `Live` | `Long` | `1.73` | 20,870,000.00 USD | 0.00 USD | 6,750.00 USD | `-58.57%` | `3,914.50` |
| `Live` | `Long` | `1.74` | 20,860,000.00 USD | 0.00 USD | 5,310.00 USD | `-58.33%` | `3,058.80` |
| `Live` | `Long` | `1.75` | 20,850,000.00 USD | 0.00 USD | 4,230.00 USD | `-58.09%` | `2,422.20` |
| `Live` | `Long` | `1.75` | 20,850,000.00 USD | 0.00 USD | 10,600.00 USD | `-57.85%` | `6,041.40` |
| `Live` | `Long` | `1.76` | 20,840,000.00 USD | 0.00 USD | 722.59 USD | `-57.61%` | `409.40` |
| `Live` | `Long` | `1.77` | 20,840,000.00 USD | 0.00 USD | 3,470.00 USD | `-57.37%` | `1,953.10` |
| `Live` | `Long` | `1.78` | 20,840,000.00 USD | 0.00 USD | 453.93 USD | `-57.13%` | `254.30` |
| `Live` | `Long` | `1.79` | 20,830,000.00 USD | 0.00 USD | 471.73 USD | `-56.89%` | `262.80` |
| `Live` | `Long` | `1.80` | 20,830,000.00 USD | 0.00 USD | 1,350.00 USD | `-56.64%` | `747.90` |
| `Live` | `Long` | `1.81` | 20,830,000.00 USD | 0.00 USD | 8,400.00 USD | `-56.40%` | `4,628.80` |
| `Live` | `Long` | `1.83` | 20,820,000.00 USD | 0.00 USD | 32,440.00 USD | `-55.92%` | `17,680.00` |
| `Live` | `Long` | `1.84` | 20,790,000.00 USD | 0.00 USD | 553,500.00 USD | `-55.68%` | `300,000.60` |
| `Live` | `Long` | `1.85` | 20,240,000.00 USD | 0.00 USD | 13,220.00 USD | `-55.44%` | `7,126.80` |
| `Live` | `Long` | `1.86` | 20,230,000.00 USD | 0.00 USD | 34,420.00 USD | `-55.20%` | `18,455.90` |
| `Live` | `Long` | `1.90` | 20,190,000.00 USD | 0.00 USD | 2,250.00 USD | `-54.48%` | `1,189.40` |
| `Live` | `Long` | `1.91` | 20,190,000.00 USD | 0.00 USD | 2,030.00 USD | `-54.24%` | `1,066.70` |
| `Live` | `Long` | `1.93` | 20,190,000.00 USD | 0.00 USD | 1,870.00 USD | `-53.76%` | `971.20` |
| `Live` | `Long` | `1.94` | 20,180,000.00 USD | 0.00 USD | 34,520.00 USD | `-53.52%` | `17,837.90` |
| `Live` | `Long` | `1.95` | 20,150,000.00 USD | 0.00 USD | 3,710.00 USD | `-53.28%` | `1,909.40` |
| `Live` | `Long` | `1.96` | 20,150,000.00 USD | 0.00 USD | 775.55 USD | `-53.04%` | `396.70` |
| `Live` | `Long` | `1.97` | 20,150,000.00 USD | 0.00 USD | 1,740.00 USD | `-52.80%` | `884.20` |
| `Live` | `Long` | `1.98` | 20,140,000.00 USD | 0.00 USD | 36,170.00 USD | `-52.56%` | `18,315.70` |
| `Live` | `Long` | `1.99` | 20,110,000.00 USD | 0.00 USD | 135.38 USD | `-52.32%` | `68.20` |
| `Live` | `Long` | `2.00` | 20,110,000.00 USD | 0.00 USD | 11,410.00 USD | `-52.08%` | `5,720.40` |
| `Live` | `Long` | `2.00` | 20,100,000.00 USD | 0.00 USD | 102.86 USD | `-51.84%` | `51.30` |
| `Live` | `Long` | `2.02` | 20,100,000.00 USD | 0.00 USD | 20,080.00 USD | `-51.60%` | `9,963.70` |
| `Live` | `Long` | `2.02` | 20,080,000.00 USD | 0.00 USD | 665.62 USD | `-51.36%` | `328.70` |
| `Live` | `Long` | `2.04` | 20,080,000.00 USD | 0.00 USD | 1,390.00 USD | `-51.12%` | `681.60` |
| `Live` | `Long` | `2.04` | 20,070,000.00 USD | 0.00 USD | 3,460.00 USD | `-50.88%` | `1,693.20` |
| `Live` | `Long` | `2.06` | 20,070,000.00 USD | 0.00 USD | 595.33 USD | `-50.64%` | `289.70` |
| `Live` | `Long` | `2.06` | 20,070,000.00 USD | 0.00 USD | 7,870.00 USD | `-50.40%` | `3,809.30` |
| `Live` | `Long` | `2.08` | 20,060,000.00 USD | 0.00 USD | 11,100.00 USD | `-50.16%` | `5,347.70` |
| `Live` | `Long` | `2.08` | 20,050,000.00 USD | 0.00 USD | 18,930.00 USD | `-49.92%` | `9,079.00` |
| `Live` | `Long` | `2.10` | 20,030,000.00 USD | 0.00 USD | 2,760.00 USD | `-49.68%` | `1,317.50` |
| `Live` | `Long` | `2.10` | 20,030,000.00 USD | 0.00 USD | 6,240.00 USD | `-49.44%` | `2,964.60` |
| `Live` | `Long` | `2.12` | 20,020,000.00 USD | 0.00 USD | 15,580.00 USD | `-49.20%` | `7,365.20` |
| `Live` | `Long` | `2.12` | 20,010,000.00 USD | 0.00 USD | 34,490.00 USD | `-48.96%` | `16,232.50` |
| `Live` | `Long` | `2.15` | 19,970,000.00 USD | 0.00 USD | 59,140.00 USD | `-48.48%` | `27,573.10` |
| `Live` | `Long` | `2.15` | 19,910,000.00 USD | 0.00 USD | 92,830.00 USD | `-48.24%` | `43,074.40` |
| `Live` | `Long` | `2.17` | 19,820,000.00 USD | 0.00 USD | 189,270.00 USD | `-48.00%` | `87,423.20` |
| `Live` | `Long` | `2.17` | 19,630,000.00 USD | 0.00 USD | 292.32 USD | `-47.76%` | `134.40` |
| `Live` | `Long` | `2.19` | 19,630,000.00 USD | 0.00 USD | 1,110.00 USD | `-47.52%` | `505.90` |
| `Live` | `Long` | `2.19` | 19,630,000.00 USD | 0.00 USD | 10,010.00 USD | `-47.28%` | `4,560.10` |
| `Live` | `Long` | `2.21` | 19,620,000.00 USD | 0.00 USD | 251,500.00 USD | `-47.04%` | `114,059.40` |
| `Live` | `Long` | `2.21` | 19,370,000.00 USD | 0.00 USD | 3,010.00 USD | `-46.80%` | `1,357.10` |
| `Live` | `Long` | `2.23` | 19,370,000.00 USD | 0.00 USD | 243.19 USD | `-46.56%` | `109.30` |
| `Live` | `Long` | `2.23` | 19,370,000.00 USD | 0.00 USD | 12,270.00 USD | `-46.32%` | `5,491.60` |
| `Live` | `Long` | `2.25` | 19,350,000.00 USD | 0.00 USD | 310,060.00 USD | `-46.08%` | `138,111.20` |
| `Live` | `Long` | `2.25` | 19,040,000.00 USD | 0.00 USD | 184,160.00 USD | `-45.84%` | `81,669.00` |
| `Live` | `Long` | `2.27` | 18,860,000.00 USD | 0.00 USD | 2,370.00 USD | `-45.60%` | `1,045.80` |
| `Live` | `Long` | `2.27` | 18,860,000.00 USD | 0.00 USD | 382,060.00 USD | `-45.36%` | `167,937.60` |
| `Live` | `Long` | `2.29` | 18,470,000.00 USD | 0.00 USD | 463.86 USD | `-45.12%` | `203.00` |
| `Live` | `Long` | `2.29` | 18,470,000.00 USD | 0.00 USD | 2,150.00 USD | `-44.88%` | `936.90` |
| `Live` | `Long` | `2.31` | 18,470,000.00 USD | 0.00 USD | 9,680.00 USD | `-44.64%` | `4,197.70` |
| `Live` | `Long` | `2.31` | 18,460,000.00 USD | 0.00 USD | 9,000.00 USD | `-44.40%` | `3,889.70` |
| `Live` | `Long` | `2.33` | 18,450,000.00 USD | 0.00 USD | 697.50 USD | `-44.15%` | `300.00` |
| `Live` | `Long` | `2.33` | 18,450,000.00 USD | 0.00 USD | 2,670.00 USD | `-43.91%` | `1,145.40` |
| `Live` | `Long` | `2.35` | 18,450,000.00 USD | 0.00 USD | 6,680.00 USD | `-43.67%` | `2,848.60` |
| `Live` | `Long` | `2.37` | 18,440,000.00 USD | 0.00 USD | 7,490.00 USD | `-43.19%` | `3,167.80` |
| `Live` | `Long` | `2.38` | 18,440,000.00 USD | 0.00 USD | 32,450.00 USD | `-42.95%` | `13,661.50` |
| `Live` | `Long` | `2.38` | 18,400,000.00 USD | 0.00 USD | 9,230.00 USD | `-42.71%` | `3,870.50` |
| `Live` | `Long` | `2.40` | 18,390,000.00 USD | 0.00 USD | 1,830,000.00 USD | `-42.47%` | `766,069.90` |
| `Live` | `Long` | `2.42` | 16,560,000.00 USD | 0.00 USD | 186,030.00 USD | `-41.99%` | `77,030.20` |
| `Live` | `Long` | `2.42` | 16,370,000.00 USD | 0.00 USD | 273,060.00 USD | `-41.75%` | `112,601.40` |
| `Live` | `Long` | `2.44` | 16,100,000.00 USD | 0.00 USD | 4,890.00 USD | `-41.51%` | `2,007.40` |
| `Live` | `Long` | `2.44` | 16,100,000.00 USD | 0.00 USD | 3,700.00 USD | `-41.27%` | `1,515.10` |
| `Live` | `Long` | `2.46` | 16,090,000.00 USD | 0.00 USD | 1,240.00 USD | `-41.03%` | `504.90` |
| `Live` | `Long` | `2.46` | 16,090,000.00 USD | 0.00 USD | 17,050.00 USD | `-40.79%` | `6,915.10` |
| `Live` | `Long` | `2.48` | 16,070,000.00 USD | 0.00 USD | 12,710.00 USD | `-40.55%` | `5,135.90` |
| `Live` | `Long` | `2.48` | 16,060,000.00 USD | 0.00 USD | 4,600.00 USD | `-40.31%` | `1,852.60` |
| `Live` | `Long` | `2.50` | 16,060,000.00 USD | 0.00 USD | 2,910.00 USD | `-40.07%` | `1,165.30` |
| `Live` | `Long` | `2.50` | 16,050,000.00 USD | 0.00 USD | 10,310.00 USD | `-39.83%` | `4,116.50` |
| `Live` | `Long` | `2.52` | 16,040,000.00 USD | 0.00 USD | 34,060.00 USD | `-39.35%` | `13,489.80` |
| `Live` | `Long` | `2.54` | 16,010,000.00 USD | 0.00 USD | 395.71 USD | `-39.11%` | `156.10` |
| `Live` | `Long` | `2.54` | 16,010,000.00 USD | 0.00 USD | 105.36 USD | `-38.87%` | `41.40` |
| `Live` | `Long` | `2.56` | 16,010,000.00 USD | 0.00 USD | 7,270.00 USD | `-38.63%` | `2,847.00` |
| `Live` | `Long` | `2.56` | 16,000,000.00 USD | 0.00 USD | 456,880.00 USD | `-38.39%` | `178,122.40` |
| `Live` | `Long` | `2.58` | 15,540,000.00 USD | 0.00 USD | 1,260.00 USD | `-38.15%` | `490.00` |
| `Live` | `Long` | `2.58` | 15,540,000.00 USD | 0.00 USD | 1,340.00 USD | `-37.91%` | `519.60` |
| `Live` | `Long` | `2.60` | 15,540,000.00 USD | 0.00 USD | 83,350.00 USD | `-37.67%` | `32,118.60` |
| `Live` | `Long` | `2.62` | 15,460,000.00 USD | 0.00 USD | 3,820.00 USD | `-37.19%` | `1,459.80` |
| `Live` | `Long` | `2.63` | 15,450,000.00 USD | 0.00 USD | 25,280.00 USD | `-36.71%` | `9,594.00` |
| `Live` | `Long` | `2.65` | 15,430,000.00 USD | 0.00 USD | 2,650.00 USD | `-36.47%` | `1,000.00` |
| `Live` | `Long` | `2.65` | 15,430,000.00 USD | 0.00 USD | 20,520.00 USD | `-36.23%` | `7,730.60` |
| `Live` | `Long` | `2.67` | 15,410,000.00 USD | 0.00 USD | 7,540.00 USD | `-35.75%` | `2,819.10` |
| `Live` | `Long` | `2.69` | 15,400,000.00 USD | 0.00 USD | 5,130.00 USD | `-35.51%` | `1,911.60` |
| `Live` | `Long` | `2.69` | 15,390,000.00 USD | 0.00 USD | 733.85 USD | `-35.27%` | `272.30` |
| `Live` | `Long` | `2.71` | 15,390,000.00 USD | 0.00 USD | 357,920.00 USD | `-35.03%` | `132,319.00` |
| `Live` | `Long` | `2.71` | 15,030,000.00 USD | 0.00 USD | 21,440.00 USD | `-34.79%` | `7,897.20` |
| `Live` | `Long` | `2.73` | 15,010,000.00 USD | 0.00 USD | 28,380.00 USD | `-34.55%` | `10,414.30` |
| `Live` | `Long` | `2.73` | 14,980,000.00 USD | 0.00 USD | 9,400.00 USD | `-34.31%` | `3,435.70` |
| `Live` | `Long` | `2.75` | 14,980,000.00 USD | 0.00 USD | 39,690.00 USD | `-34.07%` | `14,458.30` |
| `Live` | `Long` | `2.75` | 14,940,000.00 USD | 0.00 USD | 26,770.00 USD | `-33.83%` | `9,717.40` |
| `Live` | `Long` | `2.77` | 14,910,000.00 USD | 0.00 USD | 352,610.00 USD | `-33.59%` | `127,526.20` |
| `Live` | `Long` | `2.77` | 14,560,000.00 USD | 0.00 USD | 398.77 USD | `-33.35%` | `143.70` |
| `Live` | `Long` | `2.79` | 14,560,000.00 USD | 0.00 USD | 49,740.00 USD | `-33.11%` | `17,859.80` |
| `Live` | `Long` | `2.79` | 14,510,000.00 USD | 0.00 USD | 191,910.00 USD | `-32.87%` | `68,661.50` |
| `Live` | `Long` | `2.81` | 14,310,000.00 USD | 0.00 USD | 97,490.00 USD | `-32.63%` | `34,757.40` |
| `Live` | `Long` | `2.81` | 14,220,000.00 USD | 0.00 USD | 10,010.00 USD | `-32.39%` | `3,555.20` |
| `Live` | `Long` | `2.83` | 14,210,000.00 USD | 0.00 USD | 11,350.00 USD | `-32.15%` | `4,017.50` |
| `Live` | `Long` | `2.83` | 14,200,000.00 USD | 0.00 USD | 24,770.00 USD | `-31.90%` | `8,736.40` |
| `Live` | `Long` | `2.85` | 14,170,000.00 USD | 0.00 USD | 8,780.00 USD | `-31.66%` | `3,084.70` |
| `Live` | `Long` | `2.85` | 14,160,000.00 USD | 0.00 USD | 2,580,000.00 USD | `-31.42%` | `902,328.30` |
| `Live` | `Long` | `2.87` | 11,590,000.00 USD | 0.00 USD | 9,150.00 USD | `-31.18%` | `3,193.80` |
| `Live` | `Long` | `2.88` | 11,580,000.00 USD | 0.00 USD | 475,530.00 USD | `-30.94%` | `165,401.50` |
| `Live` | `Long` | `2.88` | 11,100,000.00 USD | 0.00 USD | 18,230.00 USD | `-30.70%` | `6,320.30` |
| `Live` | `Long` | `2.90` | 11,080,000.00 USD | 0.00 USD | 14,200.00 USD | `-30.46%` | `4,904.40` |
| `Live` | `Long` | `2.90` | 11,070,000.00 USD | 0.00 USD | 14,830.00 USD | `-30.22%` | `5,103.40` |
| `Live` | `Long` | `2.92` | 11,050,000.00 USD | 0.00 USD | 82,440.00 USD | `-29.98%` | `28,282.50` |
| `Live` | `Long` | `2.92` | 10,970,000.00 USD | 0.00 USD | 49,180.00 USD | `-29.74%` | `16,814.40` |
| `Live` | `Long` | `2.94` | 10,920,000.00 USD | 0.00 USD | 431,620.00 USD | `-29.50%` | `147,058.90` |
| `Live` | `Long` | `2.94` | 10,490,000.00 USD | 0.00 USD | 50,830.00 USD | `-29.26%` | `17,261.00` |
| `Live` | `Long` | `2.96` | 10,440,000.00 USD | 0.00 USD | 1,100.00 USD | `-29.02%` | `372.30` |
| `Live` | `Long` | `2.96` | 10,440,000.00 USD | 0.00 USD | 5,090.00 USD | `-28.78%` | `1,717.90` |
| `Live` | `Long` | `2.98` | 10,430,000.00 USD | 0.00 USD | 37,560.00 USD | `-28.54%` | `12,626.10` |
| `Live` | `Long` | `2.98` | 10,400,000.00 USD | 0.00 USD | 178,230.00 USD | `-28.30%` | `59,709.80` |
| `Live` | `Long` | `3.00` | 10,220,000.00 USD | 0.00 USD | 8,090.00 USD | `-28.06%` | `2,701.70` |
| `Live` | `Long` | `3.00` | 10,210,000.00 USD | 0.00 USD | 11,020.00 USD | `-27.82%` | `3,667.70` |
| `Live` | `Long` | `3.02` | 10,200,000.00 USD | 0.00 USD | 21,490.00 USD | `-27.58%` | `7,128.10` |
| `Live` | `Long` | `3.02` | 10,180,000.00 USD | 0.00 USD | 31,230.00 USD | `-27.34%` | `10,322.50` |
| `Live` | `Long` | `3.04` | 10,150,000.00 USD | 0.00 USD | 1,020.00 USD | `-27.10%` | `335.50` |
| `Live` | `Long` | `3.04` | 10,150,000.00 USD | 0.00 USD | 168,030.00 USD | `-26.86%` | `55,183.00` |
| `Live` | `Long` | `3.06` | 9,980,000.00 USD | 0.00 USD | 178,920.00 USD | `-26.62%` | `58,567.00` |
| `Live` | `Long` | `3.06` | 9,800,000.00 USD | 0.00 USD | 115,550.00 USD | `-26.38%` | `37,700.70` |
| `Live` | `Long` | `3.08` | 9,680,000.00 USD | 0.00 USD | 125,140.00 USD | `-26.14%` | `40,695.80` |
| `Live` | `Long` | `3.08` | 9,560,000.00 USD | 0.00 USD | 7,660.00 USD | `-25.90%` | `2,484.40` |
| `Live` | `Long` | `3.10` | 9,550,000.00 USD | 0.00 USD | 7,660.00 USD | `-25.66%` | `2,473.60` |
| `Live` | `Long` | `3.10` | 9,540,000.00 USD | 0.00 USD | 17,000.00 USD | `-25.42%` | `5,476.00` |
| `Live` | `Long` | `3.12` | 9,530,000.00 USD | 0.00 USD | 31,130.00 USD | `-25.18%` | `9,992.50` |
| `Live` | `Long` | `3.12` | 9,490,000.00 USD | 0.00 USD | 7,930.00 USD | `-24.94%` | `2,537.20` |
| `Live` | `Long` | `3.13` | 9,490,000.00 USD | 0.00 USD | 9,280.00 USD | `-24.70%` | `2,961.00` |
| `Live` | `Long` | `3.15` | 9,480,000.00 USD | 0.00 USD | 23,000.00 USD | `-24.46%` | `7,314.70` |
| `Live` | `Long` | `3.15` | 9,450,000.00 USD | 0.00 USD | 25,240.00 USD | `-24.22%` | `8,000.00` |
| `Live` | `Long` | `3.17` | 9,430,000.00 USD | 0.00 USD | 12,840.00 USD | `-23.98%` | `4,056.10` |
| `Live` | `Long` | `3.17` | 9,420,000.00 USD | 0.00 USD | 57,760.00 USD | `-23.74%` | `18,191.20` |
| `Live` | `Long` | `3.19` | 9,360,000.00 USD | 0.00 USD | 249,290.00 USD | `-23.50%` | `78,269.80` |
| `Live` | `Long` | `3.19` | 9,110,000.00 USD | 0.00 USD | 219.50 USD | `-23.26%` | `68.70` |
| `Live` | `Long` | `3.21` | 9,110,000.00 USD | 0.00 USD | 4,010.00 USD | `-23.02%` | `1,251.10` |
| `Live` | `Long` | `3.21` | 9,100,000.00 USD | 0.00 USD | 13,530.00 USD | `-22.78%` | `4,208.60` |
| `Live` | `Long` | `3.23` | 9,090,000.00 USD | 0.00 USD | 31,660.00 USD | `-22.54%` | `9,815.60` |
| `Live` | `Long` | `3.23` | 9,060,000.00 USD | 0.00 USD | 56,080.00 USD | `-22.30%` | `17,335.30` |
| `Live` | `Long` | `3.25` | 9,000,000.00 USD | 0.00 USD | 20,130.00 USD | `-22.06%` | `6,204.10` |
| `Live` | `Long` | `3.25` | 8,980,000.00 USD | 0.00 USD | 5,640.00 USD | `-21.82%` | `1,733.30` |
| `Live` | `Long` | `3.27` | 8,980,000.00 USD | 0.00 USD | 51,010.00 USD | `-21.58%` | `15,622.30` |
| `Live` | `Long` | `3.27` | 8,930,000.00 USD | 0.00 USD | 874,570.00 USD | `-21.34%` | `267,044.10` |
| `Live` | `Long` | `3.29` | 8,050,000.00 USD | 0.00 USD | 19,440.00 USD | `-21.10%` | `5,916.40` |
| `Live` | `Long` | `3.29` | 8,030,000.00 USD | 0.00 USD | 133,000.00 USD | `-20.86%` | `40,362.70` |
| `Live` | `Long` | `3.31` | 7,900,000.00 USD | 0.00 USD | 131,270.00 USD | `-20.62%` | `39,719.70` |
| `Live` | `Long` | `3.31` | 7,770,000.00 USD | 0.00 USD | 17,060.00 USD | `-20.38%` | `5,145.10` |
| `Live` | `Long` | `3.33` | 7,750,000.00 USD | 0.00 USD | 20,150.00 USD | `-20.14%` | `6,061.00` |
| `Live` | `Long` | `3.33` | 7,730,000.00 USD | 0.00 USD | 73,060.00 USD | `-19.90%` | `21,908.00` |
| `Live` | `Long` | `3.35` | 7,660,000.00 USD | 0.00 USD | 27,160.00 USD | `-19.66%` | `8,119.40` |
| `Live` | `Long` | `3.35` | 7,630,000.00 USD | 0.00 USD | 1,780.00 USD | `-19.41%` | `531.00` |
| `Live` | `Long` | `3.37` | 7,630,000.00 USD | 0.00 USD | 24,580.00 USD | `-19.17%` | `7,305.80` |
| `Live` | `Long` | `3.38` | 7,600,000.00 USD | 0.00 USD | 191,940.00 USD | `-18.93%` | `56,870.10` |
| `Live` | `Long` | `3.38` | 7,410,000.00 USD | 0.00 USD | 44,790.00 USD | `-18.69%` | `13,232.00` |
| `Live` | `Long` | `3.40` | 7,370,000.00 USD | 0.00 USD | 888.47 USD | `-18.45%` | `261.70` |
| `Live` | `Long` | `3.40` | 7,370,000.00 USD | 0.00 USD | 98,820.00 USD | `-18.21%` | `29,022.40` |
| `Live` | `Long` | `3.42` | 7,270,000.00 USD | 0.00 USD | 415,990.00 USD | `-17.97%` | `121,813.20` |
| `Live` | `Long` | `3.42` | 6,850,000.00 USD | 0.00 USD | 28,690.00 USD | `-17.73%` | `8,375.70` |
| `Live` | `Long` | `3.44` | 6,820,000.00 USD | 0.00 USD | 33,630.00 USD | `-17.49%` | `9,789.70` |
| `Live` | `Long` | `3.44` | 6,790,000.00 USD | 0.00 USD | 21,620.00 USD | `-17.25%` | `6,275.80` |
| `Live` | `Long` | `3.46` | 6,770,000.00 USD | 0.00 USD | 12,040.00 USD | `-17.01%` | `3,485.50` |
| `Live` | `Long` | `3.46` | 6,760,000.00 USD | 0.00 USD | 14,380.00 USD | `-16.77%` | `4,150.10` |
| `Live` | `Long` | `3.48` | 6,740,000.00 USD | 0.00 USD | 197,260.00 USD | `-16.53%` | `56,765.10` |
| `Live` | `Long` | `3.48` | 6,540,000.00 USD | 0.00 USD | 29,090.00 USD | `-16.29%` | `8,347.40` |
| `Live` | `Long` | `3.50` | 6,520,000.00 USD | 0.00 USD | 1,320,000.00 USD | `-16.05%` | `378,131.30` |
| `Live` | `Long` | `3.50` | 5,190,000.00 USD | 0.00 USD | 35,120.00 USD | `-15.81%` | `10,019.80` |
| `Live` | `Long` | `3.52` | 5,160,000.00 USD | 0.00 USD | 37,770.00 USD | `-15.57%` | `10,746.00` |
| `Live` | `Long` | `3.52` | 5,120,000.00 USD | 0.00 USD | 195,120.00 USD | `-15.33%` | `55,353.30` |
| `Live` | `Long` | `3.54` | 4,930,000.00 USD | 0.00 USD | 120,780.00 USD | `-15.09%` | `34,168.00` |
| `Live` | `Long` | `3.54` | 4,800,000.00 USD | 0.00 USD | 167,840.00 USD | `-14.85%` | `47,344.30` |
| `Live` | `Long` | `3.56` | 4,640,000.00 USD | 0.00 USD | 374,310.00 USD | `-14.61%` | `105,290.00` |
| `Live` | `Long` | `3.56` | 4,260,000.00 USD | 0.00 USD | 9,160.00 USD | `-14.37%` | `2,569.10` |
| `Live` | `Long` | `3.58` | 4,250,000.00 USD | 0.00 USD | 61,480.00 USD | `-14.13%` | `17,196.70` |
| `Live` | `Long` | `3.58` | 4,190,000.00 USD | 0.00 USD | 33,150.00 USD | `-13.89%` | `9,246.50` |
| `Live` | `Long` | `3.60` | 4,160,000.00 USD | 0.00 USD | 109,830.00 USD | `-13.65%` | `30,549.80` |
| `Live` | `Long` | `3.60` | 4,050,000.00 USD | 0.00 USD | 60,200.00 USD | `-13.41%` | `16,699.70` |
| `Live` | `Long` | `3.62` | 3,990,000.00 USD | 0.00 USD | 16,360.00 USD | `-13.17%` | `4,526.20` |
| `Live` | `Long` | `3.62` | 3,970,000.00 USD | 0.00 USD | 125,710.00 USD | `-12.93%` | `34,678.60` |
| `Live` | `Long` | `3.63` | 3,850,000.00 USD | 0.00 USD | 230,840.00 USD | `-12.69%` | `63,504.80` |
| `Live` | `Long` | `3.65` | 3,620,000.00 USD | 0.00 USD | 19,580.00 USD | `-12.45%` | `5,371.80` |
| `Live` | `Long` | `3.65` | 3,600,000.00 USD | 0.00 USD | 12,700.00 USD | `-12.21%` | `3,474.60` |
| `Live` | `Long` | `3.67` | 3,580,000.00 USD | 0.00 USD | 56,050.00 USD | `-11.97%` | `15,293.30` |
| `Live` | `Long` | `3.67` | 3,530,000.00 USD | 0.00 USD | 99,010.00 USD | `-11.73%` | `26,942.70` |
| `Live` | `Long` | `3.69` | 3,430,000.00 USD | 0.00 USD | 287,470.00 USD | `-11.49%` | `78,011.80` |
| `Live` | `Long` | `3.69` | 3,140,000.00 USD | 0.00 USD | 94,330.00 USD | `-11.25%` | `25,529.50` |
| `Live` | `Long` | `3.71` | 3,050,000.00 USD | 0.00 USD | 212,700.00 USD | `-11.01%` | `57,408.40` |
| `Live` | `Long` | `3.71` | 2,830,000.00 USD | 0.00 USD | 72,730.00 USD | `-10.77%` | `19,577.00` |
| `Live` | `Long` | `3.73` | 2,760,000.00 USD | 0.00 USD | 224,660.00 USD | `-10.53%` | `60,310.30` |
| `Live` | `Long` | `3.73` | 2,540,000.00 USD | 0.00 USD | 122,190.00 USD | `-10.29%` | `32,714.50` |
| `Live` | `Long` | `3.75` | 2,410,000.00 USD | 0.00 USD | 39,750.00 USD | `-10.05%` | `10,614.40` |
| `Live` | `Long` | `3.75` | 2,370,000.00 USD | 0.00 USD | 201,260.00 USD | `-9.81%` | `53,596.90` |
| `Live` | `Long` | `3.77` | 2,170,000.00 USD | 0.00 USD | 60,660.00 USD | `-9.57%` | `16,112.30` |
| `Live` | `Long` | `3.77` | 2,110,000.00 USD | 0.00 USD | 64,270.00 USD | `-9.33%` | `17,024.00` |
| `Live` | `Long` | `3.79` | 2,050,000.00 USD | 0.00 USD | 31,540.00 USD | `-9.09%` | `8,334.20` |
| `Live` | `Long` | `3.79` | 2,020,000.00 USD | 0.00 USD | 137,950.00 USD | `-8.85%` | `36,351.50` |
| `Live` | `Long` | `3.81` | 1,880,000.00 USD | 0.00 USD | 456,920.00 USD | `-8.61%` | `120,083.60` |
| `Live` | `Long` | `3.81` | 1,420,000.00 USD | 0.00 USD | 100,730.00 USD | `-8.37%` | `26,403.80` |
| `Live` | `Long` | `3.83` | 1,320,000.00 USD | 0.00 USD | 161,990.00 USD | `-8.13%` | `42,351.30` |
| `Live` | `Long` | `3.83` | 1,160,000.00 USD | 0.00 USD | 198,060.00 USD | `-7.89%` | `51,646.10` |
| `Live` | `Long` | `3.85` | 961,300.00 USD | 0.00 USD | 123,400.00 USD | `-7.65%` | `32,093.40` |
| `Live` | `Long` | `3.85` | 837,910.00 USD | 0.00 USD | 81,300.00 USD | `-7.41%` | `21,090.60` |
| `Live` | `Long` | `3.87` | 756,600.00 USD | 0.00 USD | 33,810.00 USD | `-7.16%` | `8,747.40` |
| `Live` | `Long` | `3.88` | 722,790.00 USD | 0.00 USD | 29,390.00 USD | `-6.92%` | `7,584.20` |
| `Live` | `Long` | `3.88` | 693,400.00 USD | 0.00 USD | 238,510.00 USD | `-6.68%` | `61,393.20` |
| `Live` | `Long` | `3.90` | 454,890.00 USD | 0.00 USD | 99,530.00 USD | `-6.44%` | `25,552.90` |
| `Live` | `Long` | `3.90` | 355,360.00 USD | 0.00 USD | 6,110.00 USD | `-6.20%` | `1,563.70` |
| `Live` | `Long` | `3.92` | 349,260.00 USD | 0.00 USD | 161,730.00 USD | `-5.96%` | `41,309.30` |
| `Live` | `Long` | `3.92` | 187,530.00 USD | 0.00 USD | 304.58 USD | `-5.72%` | `77.60` |
| `Live` | `Long` | `3.94` | 187,230.00 USD | 0.00 USD | 6,340.00 USD | `-5.48%` | `1,611.10` |
| `Live` | `Long` | `3.94` | 180,890.00 USD | 0.00 USD | 147,750.00 USD | `-5.24%` | `37,452.60` |
| `Live` | `Long` | `3.98` | 33,140.00 USD | 0.00 USD | 33,140.00 USD | `-4.52%` | `8,336.10` |
| `Live` | `Short` | `4.14` | 90,630.00 USD | 90,630.00 USD | 0.00 USD | `-0.44%` | `21,865.20` |
| `Live` | `Short` | `4.17` | 100,670.00 USD | 10,040.00 USD | 0.00 USD | `+0.28%` | `2,404.60` |
| `Live` | `Short` | `4.18` | 102,220.00 USD | 1,550.00 USD | 0.00 USD | `+0.52%` | `370.20` |
| `Live` | `Short` | `4.20` | 102,480.00 USD | 261.35 USD | 0.00 USD | `+0.76%` | `62.30` |
| `Live` | `Short` | `4.21` | 106,580.00 USD | 4,100.00 USD | 0.00 USD | `+1.00%` | `975.40` |
| `Live` | `Short` | `4.21` | 107,420.00 USD | 837.10 USD | 0.00 USD | `+1.24%` | `198.60` |
| `Live` | `Short` | `4.22` | 107,590.00 USD | 165.62 USD | 0.00 USD | `+1.48%` | `39.20` |
| `Live` | `Short` | `4.24` | 125,690.00 USD | 18,110.00 USD | 0.00 USD | `+1.72%` | `4,275.50` |
| `Live` | `Short` | `4.25` | 125,990.00 USD | 296.30 USD | 0.00 USD | `+1.96%` | `69.80` |
| `Live` | `Short` | `4.26` | 185,300.00 USD | 59,310.00 USD | 0.00 USD | `+2.44%` | `13,906.10` |
| `Live` | `Short` | `4.29` | 185,460.00 USD | 163.69 USD | 0.00 USD | `+2.92%` | `38.20` |
| `Live` | `Short` | `4.29` | 396,190.00 USD | 210,730.00 USD | 0.00 USD | `+3.16%` | `49,064.30` |
| `Live` | `Short` | `4.30` | 402,540.00 USD | 6,350.00 USD | 0.00 USD | `+3.40%` | `1,475.50` |
| `Live` | `Short` | `4.32` | 440,290.00 USD | 37,740.00 USD | 0.00 USD | `+3.64%` | `8,746.80` |
| `Live` | `Short` | `4.33` | 440,520.00 USD | 230.52 USD | 0.00 USD | `+3.88%` | `53.30` |
| `Live` | `Short` | `4.34` | 444,640.00 USD | 4,130.00 USD | 0.00 USD | `+4.36%` | `949.40` |
| `Live` | `Short` | `4.36` | 446,940.00 USD | 2,290.00 USD | 0.00 USD | `+4.60%` | `526.70` |
| `Live` | `Short` | `4.37` | 447,360.00 USD | 423.84 USD | 0.00 USD | `+4.84%` | `97.10` |
| `Live` | `Short` | `4.38` | 454,300.00 USD | 6,940.00 USD | 0.00 USD | `+5.08%` | `1,586.30` |
| `Live` | `Short` | `4.38` | 454,500.00 USD | 203.90 USD | 0.00 USD | `+5.33%` | `46.50` |
| `Live` | `Short` | `4.39` | 647,210.00 USD | 192,710.00 USD | 0.00 USD | `+5.57%` | `43,846.50` |
| `Live` | `Short` | `4.41` | 648,620.00 USD | 1,410.00 USD | 0.00 USD | `+5.81%` | `319.80` |
| `Live` | `Short` | `4.42` | 649,290.00 USD | 671.71 USD | 0.00 USD | `+6.29%` | `151.80` |
| `Live` | `Short` | `4.46` | 649,760.00 USD | 468.38 USD | 0.00 USD | `+7.25%` | `104.90` |
| `Live` | `Short` | `4.47` | 650,390.00 USD | 629.18 USD | 0.00 USD | `+7.49%` | `140.60` |
| `Live` | `Short` | `4.50` | 650,670.00 USD | 280.49 USD | 0.00 USD | `+7.97%` | `62.40` |
| `Live` | `Short` | `4.50` | 650,950.00 USD | 283.81 USD | 0.00 USD | `+8.21%` | `63.00` |
| `Live` | `Short` | `4.51` | 651,340.00 USD | 389.19 USD | 0.00 USD | `+8.45%` | `86.20` |
| `Live` | `Short` | `4.53` | 670,170.00 USD | 18,820.00 USD | 0.00 USD | `+8.69%` | `4,160.10` |
| `Live` | `Short` | `4.54` | 670,560.00 USD | 394.51 USD | 0.00 USD | `+9.17%` | `86.80` |
| `Live` | `Short` | `4.58` | 685,250.00 USD | 14,690.00 USD | 0.00 USD | `+9.89%` | `3,211.90` |
| `Live` | `Short` | `4.61` | 686,300.00 USD | 1,050.00 USD | 0.00 USD | `+10.61%` | `227.10` |
| `Live` | `Short` | `4.63` | 687,290.00 USD | 990.04 USD | 0.00 USD | `+11.33%` | `213.60` |
| `Live` | `Short` | `4.64` | 687,430.00 USD | 143.07 USD | 0.00 USD | `+11.57%` | `30.80` |
| `Live` | `Short` | `4.66` | 687,560.00 USD | 124.75 USD | 0.00 USD | `+11.81%` | `26.80` |
| `Live` | `Short` | `4.67` | 687,660.00 USD | 101.70 USD | 0.00 USD | `+12.05%` | `21.80` |
| `Live` | `Short` | `4.68` | 839,130.00 USD | 151,470.00 USD | 0.00 USD | `+12.53%` | `32,330.80` |
| `Live` | `Short` | `4.70` | 839,360.00 USD | 230.06 USD | 0.00 USD | `+12.77%` | `49.00` |
| `Live` | `Short` | `4.71` | 846,840.00 USD | 7,480.00 USD | 0.00 USD | `+13.01%` | `1,590.30` |
| `Live` | `Short` | `4.71` | 847,090.00 USD | 250.37 USD | 0.00 USD | `+13.25%` | `53.10` |
| `Live` | `Short` | `4.78` | 859,930.00 USD | 12,840.00 USD | 0.00 USD | `+14.69%` | `2,689.00` |
| `Live` | `Short` | `4.79` | 860,080.00 USD | 143.55 USD | 0.00 USD | `+14.93%` | `30.00` |
| `Live` | `Short` | `4.79` | 861,410.00 USD | 1,330.00 USD | 0.00 USD | `+15.17%` | `277.70` |
| `Live` | `Short` | `4.83` | 863,150.00 USD | 1,740.00 USD | 0.00 USD | `+15.89%` | `360.90` |
| `Live` | `Short` | `4.83` | 865,100.00 USD | 1,950.00 USD | 0.00 USD | `+16.13%` | `403.60` |
| `Live` | `Short` | `4.84` | 876,320.00 USD | 11,220.00 USD | 0.00 USD | `+16.37%` | `2,316.40` |
| `Live` | `Short` | `4.87` | 876,460.00 USD | 137.68 USD | 0.00 USD | `+16.85%` | `28.30` |
| `Live` | `Short` | `4.88` | 877,290.00 USD | 827.03 USD | 0.00 USD | `+17.33%` | `169.30` |
| `Live` | `Short` | `4.92` | 898,000.00 USD | 20,720.00 USD | 0.00 USD | `+18.06%` | `4,214.80` |
| `Live` | `Short` | `4.92` | 900,100.00 USD | 2,100.00 USD | 0.00 USD | `+18.30%` | `425.70` |
| `Live` | `Short` | `4.93` | 900,260.00 USD | 157.43 USD | 0.00 USD | `+18.54%` | `31.90` |
| `Live` | `Short` | `4.96` | 900,600.00 USD | 342.89 USD | 0.00 USD | `+19.02%` | `69.20` |
| `Live` | `Short` | `4.97` | 1,040,000.00 USD | 135,500.00 USD | 0.00 USD | `+19.50%` | `27,236.50` |
| `Live` | `Short` | `5.00` | 1,040,000.00 USD | 339.66 USD | 0.00 USD | `+19.98%` | `68.00` |
| `Live` | `Short` | `5.05` | 1,070,000.00 USD | 35,380.00 USD | 0.00 USD | `+21.42%` | `6,998.80` |
| `Live` | `Short` | `5.07` | 1,080,000.00 USD | 3,420.00 USD | 0.00 USD | `+21.66%` | `675.80` |
| `Live` | `Short` | `5.12` | 1,080,000.00 USD | 2,560.00 USD | 0.00 USD | `+23.10%` | `500.00` |
| `Live` | `Short` | `5.17` | 1,080,000.00 USD | 751.51 USD | 0.00 USD | `+24.06%` | `145.50` |
| `Live` | `Short` | `5.20` | 1,080,000.00 USD | 1,190.00 USD | 0.00 USD | `+24.78%` | `229.00` |
| `Live` | `Short` | `5.21` | 1,080,000.00 USD | 2,610.00 USD | 0.00 USD | `+25.26%` | `500.00` |
| `Live` | `Short` | `5.22` | 1,150,000.00 USD | 72,110.00 USD | 0.00 USD | `+25.50%` | `13,800.00` |
| `Live` | `Short` | `5.25` | 1,150,000.00 USD | 143.71 USD | 0.00 USD | `+25.98%` | `27.40` |
| `Live` | `Short` | `5.25` | 1,150,000.00 USD | 288.50 USD | 0.00 USD | `+26.22%` | `54.90` |
| `Live` | `Short` | `5.26` | 1,160,000.00 USD | 6,220.00 USD | 0.00 USD | `+26.46%` | `1,181.40` |
| `Live` | `Short` | `5.29` | 1,160,000.00 USD | 134.77 USD | 0.00 USD | `+26.94%` | `25.50` |
| `Live` | `Short` | `5.29` | 1,180,000.00 USD | 21,300.00 USD | 0.00 USD | `+27.18%` | `4,022.20` |
| `Live` | `Short` | `5.30` | 2,240,000.00 USD | 1,060,000.00 USD | 0.00 USD | `+27.42%` | `200,098.90` |
| `Live` | `Short` | `5.32` | 2,300,000.00 USD | 59,660.00 USD | 0.00 USD | `+27.66%` | `11,223.90` |
| `Live` | `Short` | `5.33` | 2,310,000.00 USD | 1,710.00 USD | 0.00 USD | `+28.14%` | `320.50` |
| `Live` | `Short` | `5.36` | 2,310,000.00 USD | 142.44 USD | 0.00 USD | `+28.62%` | `26.60` |
| `Live` | `Short` | `5.39` | 2,310,000.00 USD | 3,900.00 USD | 0.00 USD | `+29.58%` | `722.10` |
| `Live` | `Short` | `5.41` | 2,310,000.00 USD | 5,410.00 USD | 0.00 USD | `+29.82%` | `1,000.00` |
| `Live` | `Short` | `5.43` | 2,320,000.00 USD | 419.04 USD | 0.00 USD | `+30.55%` | `77.10` |
| `Live` | `Short` | `5.47` | 2,610,000.00 USD | 296,230.00 USD | 0.00 USD | `+31.51%` | `54,106.20` |
| `Live` | `Short` | `5.50` | 2,680,000.00 USD | 66,470.00 USD | 0.00 USD | `+31.99%` | `12,097.30` |
| `Live` | `Short` | `5.51` | 2,720,000.00 USD | 38,800.00 USD | 0.00 USD | `+32.47%` | `7,034.90` |
| `Live` | `Short` | `5.54` | 2,720,000.00 USD | 209.22 USD | 0.00 USD | `+32.95%` | `37.80` |
| `Live` | `Short` | `5.54` | 4,310,000.00 USD | 1,600,000.00 USD | 0.00 USD | `+33.19%` | `288,027.90` |
| `Live` | `Short` | `5.55` | 4,370,000.00 USD | 55,550.00 USD | 0.00 USD | `+33.43%` | `10,000.00` |
| `Live` | `Short` | `5.57` | 4,380,000.00 USD | 8,670.00 USD | 0.00 USD | `+33.67%` | `1,557.40` |
| `Live` | `Short` | `5.58` | 4,440,000.00 USD | 62,580.00 USD | 0.00 USD | `+34.15%` | `11,205.20` |
| `Live` | `Short` | `5.59` | 4,440,000.00 USD | 686.51 USD | 0.00 USD | `+34.39%` | `122.70` |
| `Live` | `Short` | `5.63` | 4,510,000.00 USD | 63,960.00 USD | 0.00 USD | `+35.35%` | `11,349.70` |
| `Live` | `Short` | `5.67` | 4,510,000.00 USD | 211.30 USD | 0.00 USD | `+36.07%` | `37.30` |
| `Live` | `Short` | `5.67` | 4,510,000.00 USD | 228.70 USD | 0.00 USD | `+36.31%` | `40.30` |
| `Live` | `Short` | `5.68` | 4,910,000.00 USD | 405,140.00 USD | 0.00 USD | `+36.55%` | `71,265.40` |
| `Live` | `Short` | `5.70` | 4,910,000.00 USD | 1,520.00 USD | 0.00 USD | `+36.79%` | `267.40` |
| `Live` | `Short` | `5.71` | 4,910,000.00 USD | 2,130.00 USD | 0.00 USD | `+37.27%` | `372.40` |
| `Live` | `Short` | `5.75` | 4,920,000.00 USD | 4,580.00 USD | 0.00 USD | `+37.99%` | `796.90` |
| `Live` | `Short` | `5.75` | 4,920,000.00 USD | 286.02 USD | 0.00 USD | `+38.23%` | `49.70` |
| `Live` | `Short` | `5.76` | 4,920,000.00 USD | 148.16 USD | 0.00 USD | `+38.47%` | `25.70` |
| `Live` | `Short` | `5.78` | 4,920,000.00 USD | 670.48 USD | 0.00 USD | `+38.71%` | `116.10` |
| `Live` | `Short` | `5.79` | 4,920,000.00 USD | 2,680.00 USD | 0.00 USD | `+39.19%` | `463.10` |
| `Live` | `Short` | `5.83` | 5,260,000.00 USD | 337,490.00 USD | 0.00 USD | `+39.91%` | `57,938.40` |
| `Live` | `Short` | `5.84` | 5,260,000.00 USD | 439.54 USD | 0.00 USD | `+40.39%` | `75.20` |
| `Live` | `Short` | `5.86` | 5,260,000.00 USD | 848.39 USD | 0.00 USD | `+40.63%` | `144.90` |
| `Live` | `Short` | `5.87` | 5,260,000.00 USD | 200.00 USD | 0.00 USD | `+40.87%` | `34.10` |
| `Live` | `Short` | `5.88` | 5,270,000.00 USD | 7,150.00 USD | 0.00 USD | `+41.35%` | `1,215.40` |
| `Live` | `Short` | `5.89` | 5,360,000.00 USD | 88,590.00 USD | 0.00 USD | `+41.59%` | `15,027.60` |
| `Live` | `Short` | `5.92` | 5,360,000.00 USD | 189.28 USD | 0.00 USD | `+42.07%` | `32.00` |
| `Live` | `Short` | `5.95` | 5,740,000.00 USD | 378,490.00 USD | 0.00 USD | `+42.80%` | `63,665.50` |
| `Live` | `Short` | `6.03` | 6,080,000.00 USD | 345,420.00 USD | 0.00 USD | `+44.72%` | `57,330.80` |
| `Live` | `Short` | `6.07` | 6,080,000.00 USD | 740.54 USD | 0.00 USD | `+45.68%` | `122.10` |
| `Live` | `Short` | `6.08` | 6,090,000.00 USD | 5,920.00 USD | 0.00 USD | `+46.16%` | `973.10` |
| `Live` | `Short` | `6.09` | 6,130,000.00 USD | 37,510.00 USD | 0.00 USD | `+46.40%` | `6,154.10` |
| `Live` | `Short` | `6.13` | 6,130,000.00 USD | 2,430.00 USD | 0.00 USD | `+47.36%` | `396.10` |
| `Live` | `Short` | `6.20` | 6,130,000.00 USD | 1,890.00 USD | 0.00 USD | `+48.80%` | `305.00` |
| `Live` | `Short` | `6.25` | 6,140,000.00 USD | 7,300.00 USD | 0.00 USD | `+50.00%` | `1,168.90` |
| `Live` | `Short` | `6.25` | 6,140,000.00 USD | 439.10 USD | 0.00 USD | `+50.24%` | `70.20` |
| `Live` | `Short` | `6.28` | 6,140,000.00 USD | 397.84 USD | 0.00 USD | `+50.72%` | `63.40` |
| `Live` | `Short` | `6.32` | 6,140,000.00 USD | 310.70 USD | 0.00 USD | `+51.68%` | `49.20` |
| `Live` | `Short` | `6.33` | 6,150,000.00 USD | 14,150.00 USD | 0.00 USD | `+51.92%` | `2,237.40` |
| `Live` | `Short` | `6.33` | 6,150,000.00 USD | 382.00 USD | 0.00 USD | `+52.16%` | `60.30` |
| `Live` | `Short` | `6.34` | 6,150,000.00 USD | 214.46 USD | 0.00 USD | `+52.40%` | `33.80` |
| `Live` | `Short` | `6.37` | 6,180,000.00 USD | 24,830.00 USD | 0.00 USD | `+52.88%` | `3,901.70` |
| `Live` | `Short` | `6.38` | 6,180,000.00 USD | 288.15 USD | 0.00 USD | `+53.12%` | `45.20` |
| `Live` | `Short` | `6.38` | 6,180,000.00 USD | 2,000.00 USD | 0.00 USD | `+53.36%` | `312.80` |
| `Live` | `Short` | `6.39` | 6,440,000.00 USD | 261,360.00 USD | 0.00 USD | `+53.60%` | `40,869.30` |
| `Live` | `Short` | `6.41` | 6,450,000.00 USD | 5,760.00 USD | 0.00 USD | `+53.84%` | `899.50` |
| `Live` | `Short` | `6.42` | 6,460,000.00 USD | 8,700.00 USD | 0.00 USD | `+54.08%` | `1,356.50` |
| `Live` | `Short` | `6.42` | 6,460,000.00 USD | 173.47 USD | 0.00 USD | `+54.32%` | `27.00` |
| `Live` | `Short` | `6.43` | 6,530,000.00 USD | 77,220.00 USD | 0.00 USD | `+54.56%` | `12,000.00` |
| `Live` | `Short` | `6.45` | 6,540,000.00 USD | 5,270.00 USD | 0.00 USD | `+54.81%` | `818.40` |
| `Live` | `Short` | `6.46` | 6,550,000.00 USD | 7,150.00 USD | 0.00 USD | `+55.05%` | `1,107.10` |
| `Live` | `Short` | `6.46` | 6,550,000.00 USD | 1,940.00 USD | 0.00 USD | `+55.29%` | `300.00` |
| `Live` | `Short` | `6.50` | 6,550,000.00 USD | 5,550.00 USD | 0.00 USD | `+56.25%` | `852.80` |
| `Live` | `Short` | `6.51` | 7,780,000.00 USD | 1,230,000.00 USD | 0.00 USD | `+56.49%` | `188,058.40` |
| `Live` | `Short` | `6.54` | 7,820,000.00 USD | 40,450.00 USD | 0.00 USD | `+56.97%` | `6,190.00` |
| `Live` | `Short` | `6.54` | 7,820,000.00 USD | 265.07 USD | 0.00 USD | `+57.21%` | `40.50` |
| `Live` | `Short` | `6.55` | 7,870,000.00 USD | 51,310.00 USD | 0.00 USD | `+57.45%` | `7,827.40` |
| `Live` | `Short` | `6.59` | 7,870,000.00 USD | 418.78 USD | 0.00 USD | `+58.41%` | `63.50` |
| `Live` | `Short` | `6.61` | 7,960,000.00 USD | 88,290.00 USD | 0.00 USD | `+58.65%` | `13,367.10` |
| `Live` | `Short` | `6.66` | 37,960,000.00 USD | 30,000,000.00 USD | 0.00 USD | `+59.85%` | `4,508,349.40` |
| `Live` | `Short` | `6.67` | 37,960,000.00 USD | 233.94 USD | 0.00 USD | `+60.09%` | `35.10` |
| `Live` | `Short` | `6.67` | 37,960,000.00 USD | 200.25 USD | 0.00 USD | `+60.33%` | `30.00` |
| `Live` | `Short` | `6.70` | 37,970,000.00 USD | 9,270.00 USD | 0.00 USD | `+60.81%` | `1,384.00` |
| `Live` | `Short` | `6.72` | 38,010,000.00 USD | 37,370.00 USD | 0.00 USD | `+61.53%` | `5,556.90` |
| `Live` | `Short` | `6.74` | 38,010,000.00 USD | 946.94 USD | 0.00 USD | `+61.77%` | `140.60` |
| `Live` | `Short` | `6.75` | 39,260,000.00 USD | 1,250,000.00 USD | 0.00 USD | `+62.25%` | `184,607.10` |
| `Live` | `Short` | `6.82` | 39,260,000.00 USD | 187.41 USD | 0.00 USD | `+63.69%` | `27.50` |
| `Live` | `Short` | `6.84` | 39,260,000.00 USD | 2,460.00 USD | 0.00 USD | `+64.41%` | `360.10` |
| `Live` | `Short` | `6.87` | 39,260,000.00 USD | 2,650.00 USD | 0.00 USD | `+64.89%` | `386.60` |
| `Live` | `Short` | `6.92` | 39,270,000.00 USD | 6,920.00 USD | 0.00 USD | `+66.33%` | `1,000.00` |
| `Live` | `Short` | `6.99` | 39,270,000.00 USD | 664.27 USD | 0.00 USD | `+67.78%` | `95.10` |
| `Live` | `Short` | `7.03` | 39,270,000.00 USD | 665.27 USD | 0.00 USD | `+68.74%` | `94.70` |
| `Live` | `Short` | `7.05` | 39,270,000.00 USD | 559.46 USD | 0.00 USD | `+69.46%` | `79.30` |
| `Live` | `Short` | `7.09` | 39,270,000.00 USD | 699.57 USD | 0.00 USD | `+70.42%` | `98.60` |
| `Live` | `Short` | `7.21` | 39,290,000.00 USD | 13,560.00 USD | 0.00 USD | `+73.30%` | `1,879.60` |
| `Live` | `Short` | `7.22` | 43,120,000.00 USD | 3,840,000.00 USD | 0.00 USD | `+73.54%` | `531,000.00` |
| `Live` | `Short` | `7.24` | 43,130,000.00 USD | 4,910.00 USD | 0.00 USD | `+73.78%` | `679.30` |
| `Live` | `Short` | `7.28` | 43,130,000.00 USD | 3,500.00 USD | 0.00 USD | `+74.74%` | `481.50` |
| `Live` | `Short` | `7.33` | 43,130,000.00 USD | 1,320.00 USD | 0.00 USD | `+76.18%` | `180.00` |
| `Live` | `Short` | `7.38` | 43,130,000.00 USD | 773.95 USD | 0.00 USD | `+77.38%` | `104.80` |
| `Live` | `Short` | `7.43` | 43,240,000.00 USD | 106,150.00 USD | 0.00 USD | `+78.58%` | `14,276.50` |
| `Live` | `Short` | `7.46` | 43,240,000.00 USD | 1,420.00 USD | 0.00 USD | `+79.06%` | `191.10` |
| `Live` | `Short` | `7.46` | 53,220,000.00 USD | 9,970,000.00 USD | 0.00 USD | `+79.30%` | `1,336,211.30` |
| `Live` | `Short` | `7.49` | 61,010,000.00 USD | 7,800,000.00 USD | 0.00 USD | `+79.79%` | `1,041,428.80` |
| `Live` | `Short` | `7.53` | 61,010,000.00 USD | 1,570.00 USD | 0.00 USD | `+80.75%` | `208.40` |
| `Live` | `Short` | `7.62` | 61,020,000.00 USD | 3,350.00 USD | 0.00 USD | `+82.91%` | `439.40` |
| `Live` | `Short` | `7.63` | 61,030,000.00 USD | 19,210.00 USD | 0.00 USD | `+83.39%` | `2,516.10` |
| `Live` | `Short` | `7.67` | 61,040,000.00 USD | 360.25 USD | 0.00 USD | `+84.11%` | `47.00` |
| `Live` | `Short` | `7.67` | 61,040,000.00 USD | 6,100.00 USD | 0.00 USD | `+84.35%` | `794.40` |
| `Live` | `Short` | `7.72` | 61,040,000.00 USD | 259.56 USD | 0.00 USD | `+85.55%` | `33.60` |
| `Live` | `Short` | `7.74` | 61,040,000.00 USD | 505.87 USD | 0.00 USD | `+85.79%` | `65.40` |
| `Live` | `Short` | `7.75` | 61,150,000.00 USD | 105,820.00 USD | 0.00 USD | `+86.03%` | `13,662.50` |
| `Live` | `Short` | `7.76` | 61,150,000.00 USD | 498.51 USD | 0.00 USD | `+86.51%` | `64.20` |
| `Live` | `Short` | `7.79` | 61,220,000.00 USD | 74,390.00 USD | 0.00 USD | `+86.99%` | `9,555.00` |
| `Live` | `Short` | `7.87` | 61,230,000.00 USD | 2,980.00 USD | 0.00 USD | `+88.91%` | `378.70` |
| `Live` | `Short` | `7.88` | 61,230,000.00 USD | 325.24 USD | 0.00 USD | `+89.15%` | `41.30` |
| `Live` | `Short` | `7.95` | 61,230,000.00 USD | 6,120.00 USD | 0.00 USD | `+90.83%` | `769.80` |
| `Live` | `Short` | `7.96` | 61,370,000.00 USD | 134,240.00 USD | 0.00 USD | `+91.31%` | `16,854.30` |
| `Live` | `Short` | `7.97` | 61,460,000.00 USD | 95,700.00 USD | 0.00 USD | `+91.55%` | `12,000.00` |
| `Live` | `Short` | `7.99` | 61,460,000.00 USD | 399.25 USD | 0.00 USD | `+91.79%` | `50.00` |
| `Live` | `Short` | `8.00` | 61,460,000.00 USD | 167.10 USD | 0.00 USD | `+92.04%` | `20.90` |
| `Live` | `Short` | `8.03` | 61,900,000.00 USD | 435,420.00 USD | 0.00 USD | `+92.76%` | `54,257.40` |
| `Live` | `Short` | `8.04` | 61,900,000.00 USD | 318.19 USD | 0.00 USD | `+93.00%` | `39.60` |
| `Live` | `Short` | `8.20` | 61,900,000.00 USD | 363.86 USD | 0.00 USD | `+96.84%` | `44.40` |
| `Live` | `Short` | `8.22` | 61,900,000.00 USD | 103.64 USD | 0.00 USD | `+97.56%` | `12.60` |
| `Live` | `Short` | `8.28` | 62,600,000.00 USD | 700,250.00 USD | 0.00 USD | `+98.76%` | `84,621.90` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `1.00` | 2,750,000.00 USD | 0.00 USD | 585.51 USD | `-75.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.01` | 2,750,000.00 USD | 0.00 USD | 339.82 USD | `-75.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.20` | 2,750,000.00 USD | 0.00 USD | 196.58 USD | `-71.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.34` | 2,750,000.00 USD | 0.00 USD | 331.54 USD | `-67.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.35` | 2,750,000.00 USD | 0.00 USD | 345.25 USD | `-67.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.38` | 2,750,000.00 USD | 0.00 USD | 5,640.00 USD | `-66.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.40` | 2,740,000.00 USD | 0.00 USD | 997.29 USD | `-66.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.51` | 2,740,000.00 USD | 0.00 USD | 139.83 USD | `-63.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.53` | 2,740,000.00 USD | 0.00 USD | 113.28 USD | `-63.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.54` | 2,740,000.00 USD | 0.00 USD | 4,000.00 USD | `-62.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.55` | 2,740,000.00 USD | 0.00 USD | 324.22 USD | `-62.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.59` | 2,740,000.00 USD | 0.00 USD | 4,590.00 USD | `-61.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.61` | 2,730,000.00 USD | 0.00 USD | 739.67 USD | `-61.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.62` | 2,730,000.00 USD | 0.00 USD | 1,740.00 USD | `-60.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.64` | 2,730,000.00 USD | 0.00 USD | 6,260.00 USD | `-60.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.66` | 2,720,000.00 USD | 0.00 USD | 345.40 USD | `-60.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.68` | 2,720,000.00 USD | 0.00 USD | 167.50 USD | `-59.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.70` | 2,720,000.00 USD | 0.00 USD | 669.02 USD | `-59.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.71` | 2,720,000.00 USD | 0.00 USD | 105.88 USD | `-59.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.73` | 2,720,000.00 USD | 0.00 USD | 172.50 USD | `-58.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.77` | 2,720,000.00 USD | 0.00 USD | 10,650.00 USD | `-57.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.80` | 2,710,000.00 USD | 0.00 USD | 722.00 USD | `-56.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.81` | 2,710,000.00 USD | 0.00 USD | 259.00 USD | `-56.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.82` | 2,710,000.00 USD | 0.00 USD | 103.84 USD | `-56.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.83` | 2,710,000.00 USD | 0.00 USD | 109.00 USD | `-55.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.88` | 2,710,000.00 USD | 0.00 USD | 222.19 USD | `-54.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.89` | 2,710,000.00 USD | 0.00 USD | 10,280.00 USD | `-54.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.91` | 2,700,000.00 USD | 0.00 USD | 558.36 USD | `-54.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.93` | 2,700,000.00 USD | 0.00 USD | 1,520.00 USD | `-53.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.94` | 2,700,000.00 USD | 0.00 USD | 222.14 USD | `-53.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.95` | 2,700,000.00 USD | 0.00 USD | 279.50 USD | `-53.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `1.98` | 2,700,000.00 USD | 0.00 USD | 197.50 USD | `-52.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.00` | 2,700,000.00 USD | 0.00 USD | 935.66 USD | `-52.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.00` | 2,700,000.00 USD | 0.00 USD | 18,860.00 USD | `-51.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.02` | 2,680,000.00 USD | 0.00 USD | 3,020.00 USD | `-51.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.04` | 2,670,000.00 USD | 0.00 USD | 214.52 USD | `-50.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.06` | 2,670,000.00 USD | 0.00 USD | 1,200.00 USD | `-50.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.06` | 2,670,000.00 USD | 0.00 USD | 578.41 USD | `-50.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.10` | 2,670,000.00 USD | 0.00 USD | 18,070.00 USD | `-49.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.10` | 2,650,000.00 USD | 0.00 USD | 108.62 USD | `-49.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.12` | 2,650,000.00 USD | 0.00 USD | 107.23 USD | `-49.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.12` | 2,650,000.00 USD | 0.00 USD | 1,590.00 USD | `-48.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.15` | 2,650,000.00 USD | 0.00 USD | 5,830.00 USD | `-48.48%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.15` | 2,650,000.00 USD | 0.00 USD | 310.32 USD | `-48.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.17` | 2,650,000.00 USD | 0.00 USD | 1,170.00 USD | `-48.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.19` | 2,650,000.00 USD | 0.00 USD | 576.18 USD | `-47.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.19` | 2,640,000.00 USD | 0.00 USD | 295.67 USD | `-47.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.21` | 2,640,000.00 USD | 0.00 USD | 1,430.00 USD | `-47.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.21` | 2,640,000.00 USD | 0.00 USD | 812.68 USD | `-46.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.23` | 2,640,000.00 USD | 0.00 USD | 1,590.00 USD | `-46.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.23` | 2,640,000.00 USD | 0.00 USD | 106.16 USD | `-46.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.25` | 2,640,000.00 USD | 0.00 USD | 6,270.00 USD | `-46.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.25` | 2,630,000.00 USD | 0.00 USD | 478.06 USD | `-45.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.27` | 2,630,000.00 USD | 0.00 USD | 540.88 USD | `-45.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.27` | 2,630,000.00 USD | 0.00 USD | 867.46 USD | `-45.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.29` | 2,630,000.00 USD | 0.00 USD | 759.76 USD | `-45.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.29` | 2,630,000.00 USD | 0.00 USD | 11,060.00 USD | `-44.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.31` | 2,620,000.00 USD | 0.00 USD | 3,690.00 USD | `-44.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.33` | 2,620,000.00 USD | 0.00 USD | 722.15 USD | `-44.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.33` | 2,620,000.00 USD | 0.00 USD | 467.00 USD | `-43.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.35` | 2,620,000.00 USD | 0.00 USD | 506.75 USD | `-43.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.37` | 2,620,000.00 USD | 0.00 USD | 214.27 USD | `-43.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.38` | 2,620,000.00 USD | 0.00 USD | 428.69 USD | `-42.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.38` | 2,610,000.00 USD | 0.00 USD | 322.45 USD | `-42.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.40` | 2,610,000.00 USD | 0.00 USD | 108.25 USD | `-42.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.40` | 2,610,000.00 USD | 0.00 USD | 3,900.00 USD | `-42.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.42` | 2,610,000.00 USD | 0.00 USD | 799.04 USD | `-41.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.44` | 2,610,000.00 USD | 0.00 USD | 6,830.00 USD | `-41.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.44` | 2,600,000.00 USD | 0.00 USD | 137.16 USD | `-41.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.48` | 2,600,000.00 USD | 0.00 USD | 504.41 USD | `-40.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.48` | 2,600,000.00 USD | 0.00 USD | 963.93 USD | `-40.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.50` | 2,600,000.00 USD | 0.00 USD | 6,690.00 USD | `-39.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.52` | 2,590,000.00 USD | 0.00 USD | 541.98 USD | `-39.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.54` | 2,590,000.00 USD | 0.00 USD | 108.75 USD | `-39.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.54` | 2,590,000.00 USD | 0.00 USD | 766.55 USD | `-38.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.56` | 2,590,000.00 USD | 0.00 USD | 7,110.00 USD | `-38.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.58` | 2,590,000.00 USD | 0.00 USD | 1,100.00 USD | `-38.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.58` | 2,580,000.00 USD | 0.00 USD | 100.04 USD | `-37.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.60` | 2,580,000.00 USD | 0.00 USD | 1,220.00 USD | `-37.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.62` | 2,580,000.00 USD | 0.00 USD | 5,090.00 USD | `-37.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.67` | 2,580,000.00 USD | 0.00 USD | 226.57 USD | `-35.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.69` | 2,580,000.00 USD | 0.00 USD | 104.98 USD | `-35.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.69` | 2,580,000.00 USD | 0.00 USD | 889.89 USD | `-35.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.71` | 2,580,000.00 USD | 0.00 USD | 7,270.00 USD | `-35.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.73` | 2,570,000.00 USD | 0.00 USD | 107.21 USD | `-34.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.75` | 2,570,000.00 USD | 0.00 USD | 197.37 USD | `-34.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.75` | 2,570,000.00 USD | 0.00 USD | 8,110.00 USD | `-33.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.77` | 2,560,000.00 USD | 0.00 USD | 108.39 USD | `-33.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.77` | 2,560,000.00 USD | 0.00 USD | 435.95 USD | `-33.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.79` | 2,560,000.00 USD | 0.00 USD | 217.23 USD | `-33.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.79` | 2,560,000.00 USD | 0.00 USD | 437.98 USD | `-32.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.81` | 2,560,000.00 USD | 0.00 USD | 2,720.00 USD | `-32.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.83` | 2,560,000.00 USD | 0.00 USD | 8,380.00 USD | `-32.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.83` | 2,550,000.00 USD | 0.00 USD | 283.50 USD | `-31.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.85` | 2,550,000.00 USD | 0.00 USD | 109.53 USD | `-31.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.85` | 2,550,000.00 USD | 0.00 USD | 1,230.00 USD | `-31.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.88` | 2,550,000.00 USD | 0.00 USD | 1,960.00 USD | `-30.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.88` | 2,550,000.00 USD | 0.00 USD | 746.06 USD | `-30.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.90` | 2,540,000.00 USD | 0.00 USD | 2,900.00 USD | `-30.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.90` | 2,540,000.00 USD | 0.00 USD | 4,870.00 USD | `-30.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.92` | 2,540,000.00 USD | 0.00 USD | 1,700.00 USD | `-29.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.94` | 2,540,000.00 USD | 0.00 USD | 15,370.00 USD | `-29.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.96` | 2,520,000.00 USD | 0.00 USD | 738.75 USD | `-29.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.96` | 2,520,000.00 USD | 0.00 USD | 523.32 USD | `-28.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.98` | 2,520,000.00 USD | 0.00 USD | 4,470.00 USD | `-28.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.00` | 2,510,000.00 USD | 0.00 USD | 22,640.00 USD | `-27.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.02` | 2,490,000.00 USD | 0.00 USD | 1,020.00 USD | `-27.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.02` | 2,490,000.00 USD | 0.00 USD | 345.76 USD | `-27.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.04` | 2,490,000.00 USD | 0.00 USD | 214.57 USD | `-27.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.04` | 2,490,000.00 USD | 0.00 USD | 249.08 USD | `-26.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.06` | 2,490,000.00 USD | 0.00 USD | 305.50 USD | `-26.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.06` | 2,490,000.00 USD | 0.00 USD | 109.42 USD | `-26.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.10` | 2,490,000.00 USD | 0.00 USD | 9,300.00 USD | `-25.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.12` | 2,480,000.00 USD | 0.00 USD | 8,570.00 USD | `-25.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.12` | 2,470,000.00 USD | 0.00 USD | 104.69 USD | `-24.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.13` | 2,470,000.00 USD | 0.00 USD | 315.69 USD | `-24.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.15` | 2,470,000.00 USD | 0.00 USD | 17,510.00 USD | `-24.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.15` | 2,450,000.00 USD | 0.00 USD | 258,640.00 USD | `-24.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.17` | 2,190,000.00 USD | 0.00 USD | 4,210.00 USD | `-23.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.17` | 2,190,000.00 USD | 0.00 USD | 1,030.00 USD | `-23.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.19` | 2,190,000.00 USD | 0.00 USD | 218.81 USD | `-23.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.21` | 2,190,000.00 USD | 0.00 USD | 25,410.00 USD | `-23.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.21` | 2,160,000.00 USD | 0.00 USD | 144.67 USD | `-22.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.25` | 2,160,000.00 USD | 0.00 USD | 27,380.00 USD | `-22.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.25` | 2,140,000.00 USD | 0.00 USD | 1,840.00 USD | `-21.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.27` | 2,130,000.00 USD | 0.00 USD | 104.81 USD | `-21.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.27` | 2,130,000.00 USD | 0.00 USD | 200.10 USD | `-21.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.29` | 2,130,000.00 USD | 0.00 USD | 1,480.00 USD | `-21.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.29` | 2,130,000.00 USD | 0.00 USD | 1,870.00 USD | `-20.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.31` | 2,130,000.00 USD | 0.00 USD | 18,240.00 USD | `-20.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.31` | 2,110,000.00 USD | 0.00 USD | 240.67 USD | `-20.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.33` | 2,110,000.00 USD | 0.00 USD | 465.50 USD | `-20.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.33` | 2,110,000.00 USD | 0.00 USD | 6,590.00 USD | `-19.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.35` | 2,110,000.00 USD | 0.00 USD | 505.76 USD | `-19.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.37` | 2,110,000.00 USD | 0.00 USD | 73,220.00 USD | `-19.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.38` | 2,030,000.00 USD | 0.00 USD | 19,600.00 USD | `-18.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.40` | 2,010,000.00 USD | 0.00 USD | 8,490.00 USD | `-18.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.40` | 2,000,000.00 USD | 0.00 USD | 111,650.00 USD | `-18.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.42` | 1,890,000.00 USD | 0.00 USD | 421.41 USD | `-17.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.42` | 1,890,000.00 USD | 0.00 USD | 506.22 USD | `-17.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.44` | 1,890,000.00 USD | 0.00 USD | 171.75 USD | `-17.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.44` | 1,890,000.00 USD | 0.00 USD | 2,550.00 USD | `-17.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.46` | 1,890,000.00 USD | 0.00 USD | 3,060.00 USD | `-17.01%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.46` | 1,890,000.00 USD | 0.00 USD | 344.07 USD | `-16.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.48` | 1,880,000.00 USD | 0.00 USD | 156.83 USD | `-16.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.50` | 1,880,000.00 USD | 0.00 USD | 894.72 USD | `-16.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.50` | 1,880,000.00 USD | 0.00 USD | 67,780.00 USD | `-15.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.52` | 1,820,000.00 USD | 0.00 USD | 21,320.00 USD | `-15.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.52` | 1,790,000.00 USD | 0.00 USD | 3,700.00 USD | `-15.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.54` | 1,790,000.00 USD | 0.00 USD | 16,250.00 USD | `-15.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.54` | 1,770,000.00 USD | 0.00 USD | 5,130.00 USD | `-14.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.56` | 1,770,000.00 USD | 0.00 USD | 17,420.00 USD | `-14.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.56` | 1,750,000.00 USD | 0.00 USD | 18,440.00 USD | `-14.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.58` | 1,730,000.00 USD | 0.00 USD | 78,170.00 USD | `-14.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.58` | 1,660,000.00 USD | 0.00 USD | 1,250.00 USD | `-13.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.60` | 1,650,000.00 USD | 0.00 USD | 331.46 USD | `-13.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.60` | 1,650,000.00 USD | 0.00 USD | 15,710.00 USD | `-13.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.62` | 1,640,000.00 USD | 0.00 USD | 632.99 USD | `-13.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.62` | 1,640,000.00 USD | 0.00 USD | 172.19 USD | `-12.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.63` | 1,640,000.00 USD | 0.00 USD | 1,410.00 USD | `-12.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.65` | 1,640,000.00 USD | 0.00 USD | 179.33 USD | `-12.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.65` | 1,640,000.00 USD | 0.00 USD | 4,080.00 USD | `-12.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.67` | 1,630,000.00 USD | 0.00 USD | 4,070.00 USD | `-11.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.67` | 1,630,000.00 USD | 0.00 USD | 367.50 USD | `-11.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.69` | 1,630,000.00 USD | 0.00 USD | 34,720.00 USD | `-11.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.69` | 1,590,000.00 USD | 0.00 USD | 4,370.00 USD | `-11.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.71` | 1,590,000.00 USD | 0.00 USD | 234,410.00 USD | `-11.01%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.71` | 1,350,000.00 USD | 0.00 USD | 6,300.00 USD | `-10.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.73` | 1,350,000.00 USD | 0.00 USD | 2,490.00 USD | `-10.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.73` | 1,350,000.00 USD | 0.00 USD | 32,040.00 USD | `-10.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.75` | 1,310,000.00 USD | 0.00 USD | 28,820.00 USD | `-10.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.75` | 1,280,000.00 USD | 0.00 USD | 14,490.00 USD | `-9.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.77` | 1,270,000.00 USD | 0.00 USD | 250,790.00 USD | `-9.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.77` | 1,020,000.00 USD | 0.00 USD | 1,510.00 USD | `-9.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.79` | 1,020,000.00 USD | 0.00 USD | 183.19 USD | `-9.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.79` | 1,020,000.00 USD | 0.00 USD | 181,010.00 USD | `-8.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.81` | 836,400.00 USD | 0.00 USD | 8,720.00 USD | `-8.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.81` | 827,680.00 USD | 0.00 USD | 22,340.00 USD | `-8.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.83` | 805,340.00 USD | 0.00 USD | 36,060.00 USD | `-8.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.83` | 769,280.00 USD | 0.00 USD | 7,990.00 USD | `-7.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.85` | 761,290.00 USD | 0.00 USD | 43,060.00 USD | `-7.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.85` | 718,230.00 USD | 0.00 USD | 5,640.00 USD | `-7.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.87` | 712,600.00 USD | 0.00 USD | 8,620.00 USD | `-7.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.88` | 703,970.00 USD | 0.00 USD | 161,220.00 USD | `-6.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.88` | 542,760.00 USD | 0.00 USD | 27,540.00 USD | `-6.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.90` | 515,210.00 USD | 0.00 USD | 7,770.00 USD | `-6.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.90` | 507,440.00 USD | 0.00 USD | 48,840.00 USD | `-6.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.92` | 458,600.00 USD | 0.00 USD | 441.22 USD | `-5.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.92` | 458,160.00 USD | 0.00 USD | 5,190.00 USD | `-5.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.94` | 452,970.00 USD | 0.00 USD | 1,180.00 USD | `-5.48%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.94` | 451,790.00 USD | 0.00 USD | 4,830.00 USD | `-5.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.96` | 446,960.00 USD | 0.00 USD | 3,600.00 USD | `-5.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.96` | 443,360.00 USD | 0.00 USD | 31,820.00 USD | `-4.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.98` | 411,540.00 USD | 0.00 USD | 317.60 USD | `-4.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.98` | 411,220.00 USD | 0.00 USD | 786.24 USD | `-4.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.00` | 410,430.00 USD | 0.00 USD | 6,000.00 USD | `-4.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.00` | 404,440.00 USD | 0.00 USD | 192,170.00 USD | `-3.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.01` | 212,260.00 USD | 0.00 USD | 20,520.00 USD | `-3.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.03` | 191,740.00 USD | 0.00 USD | 9,590.00 USD | `-3.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.04` | 182,150.00 USD | 0.00 USD | 15,530.00 USD | `-3.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.04` | 166,630.00 USD | 0.00 USD | 1,780.00 USD | `-2.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.05` | 164,850.00 USD | 0.00 USD | 15,600.00 USD | `-2.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.07` | 149,240.00 USD | 0.00 USD | 113.41 USD | `-2.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.08` | 149,130.00 USD | 0.00 USD | 1,290.00 USD | `-2.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.08` | 147,840.00 USD | 0.00 USD | 38,600.00 USD | `-1.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.09` | 109,240.00 USD | 0.00 USD | 41,980.00 USD | `-1.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.11` | 67,270.00 USD | 0.00 USD | 149.83 USD | `-1.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.12` | 67,120.00 USD | 0.00 USD | 58,980.00 USD | `-1.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.12` | 8,140.00 USD | 0.00 USD | 2,010.00 USD | `-0.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.13` | 6,130.00 USD | 0.00 USD | 1,120.00 USD | `-0.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.14` | 5,000.00 USD | 0.00 USD | 3,280.00 USD | `-0.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.16` | 1,730.00 USD | 0.00 USD | 1,730.00 USD | `-0.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.17` | 84,840.00 USD | 84,840.00 USD | 0.00 USD | `+0.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.17` | 86,900.00 USD | 2,060.00 USD | 0.00 USD | `+0.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.18` | 87,460.00 USD | 557.02 USD | 0.00 USD | `+0.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.20` | 459,450.00 USD | 371,990.00 USD | 0.00 USD | `+0.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.21` | 646,540.00 USD | 187,090.00 USD | 0.00 USD | `+1.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.21` | 647,230.00 USD | 687.04 USD | 0.00 USD | `+1.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.22` | 647,360.00 USD | 131.82 USD | 0.00 USD | `+1.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.24` | 647,750.00 USD | 390.47 USD | 0.00 USD | `+1.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.25` | 651,430.00 USD | 3,680.00 USD | 0.00 USD | `+1.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.25` | 684,670.00 USD | 33,240.00 USD | 0.00 USD | `+2.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.26` | 686,850.00 USD | 2,180.00 USD | 0.00 USD | `+2.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.28` | 707,890.00 USD | 21,040.00 USD | 0.00 USD | `+2.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.29` | 713,320.00 USD | 5,430.00 USD | 0.00 USD | `+2.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.29` | 744,730.00 USD | 31,410.00 USD | 0.00 USD | `+3.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.30` | 771,830.00 USD | 27,110.00 USD | 0.00 USD | `+3.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.32` | 772,100.00 USD | 269.26 USD | 0.00 USD | `+3.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.33` | 774,520.00 USD | 2,420.00 USD | 0.00 USD | `+3.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.33` | 776,060.00 USD | 1,540.00 USD | 0.00 USD | `+4.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.34` | 793,440.00 USD | 17,380.00 USD | 0.00 USD | `+4.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.36` | 793,560.00 USD | 120.63 USD | 0.00 USD | `+4.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.37` | 794,020.00 USD | 464.00 USD | 0.00 USD | `+4.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.38` | 819,530.00 USD | 25,510.00 USD | 0.00 USD | `+5.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.38` | 891,430.00 USD | 71,900.00 USD | 0.00 USD | `+5.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.39` | 933,740.00 USD | 42,310.00 USD | 0.00 USD | `+5.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.41` | 1,360,000.00 USD | 422,530.00 USD | 0.00 USD | `+5.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.42` | 1,370,000.00 USD | 13,130.00 USD | 0.00 USD | `+6.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.42` | 1,370,000.00 USD | 4,090.00 USD | 0.00 USD | `+6.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.43` | 1,370,000.00 USD | 301.58 USD | 0.00 USD | `+6.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.45` | 1,370,000.00 USD | 524.07 USD | 0.00 USD | `+6.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.46` | 1,440,000.00 USD | 62,580.00 USD | 0.00 USD | `+7.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.46` | 1,440,000.00 USD | 2,470.00 USD | 0.00 USD | `+7.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.47` | 1,440,000.00 USD | 375.90 USD | 0.00 USD | `+7.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.49` | 1,440,000.00 USD | 133.20 USD | 0.00 USD | `+7.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.50` | 1,470,000.00 USD | 29,550.00 USD | 0.00 USD | `+7.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.50` | 1,490,000.00 USD | 20,580.00 USD | 0.00 USD | `+8.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.51` | 1,500,000.00 USD | 13,100.00 USD | 0.00 USD | `+8.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.53` | 1,560,000.00 USD | 52,300.00 USD | 0.00 USD | `+8.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.54` | 1,560,000.00 USD | 3,390.00 USD | 0.00 USD | `+8.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.54` | 1,560,000.00 USD | 3,180.00 USD | 0.00 USD | `+9.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.55` | 1,560,000.00 USD | 1,190.00 USD | 0.00 USD | `+9.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.57` | 1,560,000.00 USD | 227.79 USD | 0.00 USD | `+9.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.58` | 1,570,000.00 USD | 2,030.00 USD | 0.00 USD | `+9.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.58` | 1,570,000.00 USD | 1,150.00 USD | 0.00 USD | `+10.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.59` | 1,580,000.00 USD | 17,590.00 USD | 0.00 USD | `+10.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.61` | 1,610,000.00 USD | 24,120.00 USD | 0.00 USD | `+10.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.62` | 1,610,000.00 USD | 289.82 USD | 0.00 USD | `+10.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.62` | 1,610,000.00 USD | 3,670.00 USD | 0.00 USD | `+11.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.63` | 1,610,000.00 USD | 1,100.00 USD | 0.00 USD | `+11.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.64` | 1,620,000.00 USD | 7,530.00 USD | 0.00 USD | `+11.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.66` | 1,670,000.00 USD | 44,520.00 USD | 0.00 USD | `+11.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.67` | 1,680,000.00 USD | 16,750.00 USD | 0.00 USD | `+12.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.67` | 1,680,000.00 USD | 617.10 USD | 0.00 USD | `+12.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.68` | 1,700,000.00 USD | 15,710.00 USD | 0.00 USD | `+12.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.70` | 1,700,000.00 USD | 152.12 USD | 0.00 USD | `+12.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.71` | 2,060,000.00 USD | 357,870.00 USD | 0.00 USD | `+13.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.71` | 2,270,000.00 USD | 218,120.00 USD | 0.00 USD | `+13.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.72` | 2,280,000.00 USD | 2,650.00 USD | 0.00 USD | `+13.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.74` | 2,360,000.00 USD | 84,180.00 USD | 0.00 USD | `+13.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.75` | 2,370,000.00 USD | 6,160.00 USD | 0.00 USD | `+13.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.75` | 2,390,000.00 USD | 27,130.00 USD | 0.00 USD | `+14.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.76` | 2,410,000.00 USD | 13,030.00 USD | 0.00 USD | `+14.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.78` | 2,410,000.00 USD | 2,640.00 USD | 0.00 USD | `+14.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.79` | 3,240,000.00 USD | 832,330.00 USD | 0.00 USD | `+14.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.79` | 3,240,000.00 USD | 559.58 USD | 0.00 USD | `+15.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.80` | 3,420,000.00 USD | 177,030.00 USD | 0.00 USD | `+15.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.82` | 3,440,000.00 USD | 20,720.00 USD | 0.00 USD | `+15.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.83` | 3,450,000.00 USD | 8,540.00 USD | 0.00 USD | `+15.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.83` | 3,450,000.00 USD | 283.33 USD | 0.00 USD | `+16.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.84` | 3,460,000.00 USD | 11,760.00 USD | 0.00 USD | `+16.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.86` | 3,490,000.00 USD | 24,370.00 USD | 0.00 USD | `+16.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.87` | 3,510,000.00 USD | 22,170.00 USD | 0.00 USD | `+16.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.88` | 3,520,000.00 USD | 10,400.00 USD | 0.00 USD | `+17.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.88` | 3,540,000.00 USD | 19,890.00 USD | 0.00 USD | `+17.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.89` | 3,540,000.00 USD | 4,060.00 USD | 0.00 USD | `+17.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.91` | 3,670,000.00 USD | 125,180.00 USD | 0.00 USD | `+17.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.92` | 3,670,000.00 USD | 156.30 USD | 0.00 USD | `+18.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.92` | 3,680,000.00 USD | 13,180.00 USD | 0.00 USD | `+18.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.93` | 3,690,000.00 USD | 4,420.00 USD | 0.00 USD | `+18.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.95` | 3,690,000.00 USD | 313.51 USD | 0.00 USD | `+18.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.96` | 3,690,000.00 USD | 5,070.00 USD | 0.00 USD | `+19.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.96` | 3,740,000.00 USD | 47,350.00 USD | 0.00 USD | `+19.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.97` | 3,740,000.00 USD | 187.06 USD | 0.00 USD | `+19.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `4.99` | 3,830,000.00 USD | 92,570.00 USD | 0.00 USD | `+19.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.00` | 3,830,000.00 USD | 2,540.00 USD | 0.00 USD | `+19.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.00` | 3,870,000.00 USD | 40,150.00 USD | 0.00 USD | `+20.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.01` | 3,900,000.00 USD | 25,080.00 USD | 0.00 USD | `+20.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.03` | 3,900,000.00 USD | 5,030.00 USD | 0.00 USD | `+20.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.04` | 3,920,000.00 USD | 19,640.00 USD | 0.00 USD | `+20.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.04` | 3,920,000.00 USD | 120.58 USD | 0.00 USD | `+21.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.05` | 3,940,000.00 USD | 14,440.00 USD | 0.00 USD | `+21.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.07` | 3,940,000.00 USD | 6,090.00 USD | 0.00 USD | `+21.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.08` | 4,030,000.00 USD | 87,290.00 USD | 0.00 USD | `+21.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.08` | 4,040,000.00 USD | 5,640.00 USD | 0.00 USD | `+22.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.09` | 4,040,000.00 USD | 178.33 USD | 0.00 USD | `+22.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.11` | 4,110,000.00 USD | 68,210.00 USD | 0.00 USD | `+22.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.12` | 4,120,000.00 USD | 17,900.00 USD | 0.00 USD | `+22.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.12` | 4,120,000.00 USD | 179.38 USD | 0.00 USD | `+23.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.13` | 4,120,000.00 USD | 179.72 USD | 0.00 USD | `+23.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.14` | 4,120,000.00 USD | 217.63 USD | 0.00 USD | `+23.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.16` | 4,120,000.00 USD | 493.85 USD | 0.00 USD | `+23.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.17` | 4,120,000.00 USD | 575.38 USD | 0.00 USD | `+24.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.17` | 4,130,000.00 USD | 327.58 USD | 0.00 USD | `+24.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.18` | 4,130,000.00 USD | 163.85 USD | 0.00 USD | `+24.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.20` | 4,250,000.00 USD | 120,930.00 USD | 0.00 USD | `+24.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.21` | 4,280,000.00 USD | 38,230.00 USD | 0.00 USD | `+25.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.21` | 4,290,000.00 USD | 1,710.00 USD | 0.00 USD | `+25.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.22` | 4,290,000.00 USD | 432.63 USD | 0.00 USD | `+25.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.24` | 4,290,000.00 USD | 2,620.00 USD | 0.00 USD | `+25.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.25` | 4,290,000.00 USD | 537.61 USD | 0.00 USD | `+25.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.25` | 4,710,000.00 USD | 420,400.00 USD | 0.00 USD | `+26.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.26` | 4,710,000.00 USD | 278.52 USD | 0.00 USD | `+26.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.28` | 4,710,000.00 USD | 589.22 USD | 0.00 USD | `+26.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.29` | 4,710,000.00 USD | 733.03 USD | 0.00 USD | `+26.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.29` | 4,710,000.00 USD | 423.60 USD | 0.00 USD | `+27.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.30` | 4,720,000.00 USD | 10,930.00 USD | 0.00 USD | `+27.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.32` | 4,720,000.00 USD | 381.09 USD | 0.00 USD | `+27.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.33` | 4,720,000.00 USD | 961.16 USD | 0.00 USD | `+27.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.33` | 4,730,000.00 USD | 1,570.00 USD | 0.00 USD | `+28.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.34` | 4,730,000.00 USD | 5,650.00 USD | 0.00 USD | `+28.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.36` | 4,730,000.00 USD | 160.11 USD | 0.00 USD | `+28.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.37` | 4,730,000.00 USD | 225.33 USD | 0.00 USD | `+28.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.38` | 4,730,000.00 USD | 438.60 USD | 0.00 USD | `+29.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.38` | 4,740,000.00 USD | 6,800.00 USD | 0.00 USD | `+29.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.39` | 4,780,000.00 USD | 40,880.00 USD | 0.00 USD | `+29.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.41` | 4,800,000.00 USD | 19,950.00 USD | 0.00 USD | `+29.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.42` | 4,800,000.00 USD | 270.75 USD | 0.00 USD | `+30.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.42` | 4,800,000.00 USD | 639.61 USD | 0.00 USD | `+30.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.43` | 4,800,000.00 USD | 1,710.00 USD | 0.00 USD | `+30.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.45` | 4,820,000.00 USD | 12,600.00 USD | 0.00 USD | `+30.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.46` | 4,820,000.00 USD | 4,190.00 USD | 0.00 USD | `+31.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.46` | 5,010,000.00 USD | 192,640.00 USD | 0.00 USD | `+31.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.47` | 5,040,000.00 USD | 30,110.00 USD | 0.00 USD | `+31.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.49` | 5,080,000.00 USD | 38,920.00 USD | 0.00 USD | `+31.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.50` | 5,080,000.00 USD | 1,180.00 USD | 0.00 USD | `+31.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.50` | 6,050,000.00 USD | 968,610.00 USD | 0.00 USD | `+32.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.51` | 6,060,000.00 USD | 5,600.00 USD | 0.00 USD | `+32.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.53` | 6,080,000.00 USD | 19,110.00 USD | 0.00 USD | `+32.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.54` | 6,090,000.00 USD | 18,790.00 USD | 0.00 USD | `+32.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.54` | 6,150,000.00 USD | 58,030.00 USD | 0.00 USD | `+33.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.55` | 6,200,000.00 USD | 46,110.00 USD | 0.00 USD | `+33.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.57` | 6,210,000.00 USD | 14,320.00 USD | 0.00 USD | `+33.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.58` | 6,220,000.00 USD | 11,740.00 USD | 0.00 USD | `+33.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.58` | 6,250,000.00 USD | 20,540.00 USD | 0.00 USD | `+34.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.59` | 6,250,000.00 USD | 384.94 USD | 0.00 USD | `+34.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.61` | 6,250,000.00 USD | 573.39 USD | 0.00 USD | `+34.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.62` | 6,250,000.00 USD | 347.06 USD | 0.00 USD | `+35.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.64` | 6,250,000.00 USD | 491.11 USD | 0.00 USD | `+35.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.66` | 6,250,000.00 USD | 3,290.00 USD | 0.00 USD | `+35.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.67` | 6,250,000.00 USD | 281.55 USD | 0.00 USD | `+36.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.67` | 6,260,000.00 USD | 6,590.00 USD | 0.00 USD | `+36.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.68` | 6,260,000.00 USD | 235.93 USD | 0.00 USD | `+36.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.70` | 6,260,000.00 USD | 5,860.00 USD | 0.00 USD | `+36.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.71` | 6,370,000.00 USD | 103,470.00 USD | 0.00 USD | `+37.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.71` | 6,370,000.00 USD | 705.23 USD | 0.00 USD | `+37.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.72` | 6,370,000.00 USD | 5,720.00 USD | 0.00 USD | `+37.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.75` | 6,370,000.00 USD | 139.03 USD | 0.00 USD | `+37.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.75` | 6,380,000.00 USD | 2,450.00 USD | 0.00 USD | `+38.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.78` | 6,380,000.00 USD | 1,850.00 USD | 0.00 USD | `+38.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.79` | 6,380,000.00 USD | 286.94 USD | 0.00 USD | `+38.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.80` | 6,390,000.00 USD | 7,120.00 USD | 0.00 USD | `+39.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.82` | 6,390,000.00 USD | 329.13 USD | 0.00 USD | `+39.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.83` | 6,390,000.00 USD | 1,970.00 USD | 0.00 USD | `+39.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.83` | 6,390,000.00 USD | 1,020.00 USD | 0.00 USD | `+40.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.84` | 6,390,000.00 USD | 1,150.00 USD | 0.00 USD | `+40.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.86` | 6,390,000.00 USD | 1,190.00 USD | 0.00 USD | `+40.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.87` | 6,390,000.00 USD | 1,770.00 USD | 0.00 USD | `+40.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.88` | 6,400,000.00 USD | 3,450.00 USD | 0.00 USD | `+41.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.88` | 6,400,000.00 USD | 345.45 USD | 0.00 USD | `+41.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.91` | 6,460,000.00 USD | 65,320.00 USD | 0.00 USD | `+41.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.92` | 6,460,000.00 USD | 2,510.00 USD | 0.00 USD | `+42.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.92` | 6,470,000.00 USD | 1,020.00 USD | 0.00 USD | `+42.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.93` | 6,620,000.00 USD | 153,150.00 USD | 0.00 USD | `+42.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.96` | 6,640,000.00 USD | 26,180.00 USD | 0.00 USD | `+43.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.96` | 6,650,000.00 USD | 5,440.00 USD | 0.00 USD | `+43.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.97` | 6,660,000.00 USD | 8,940.00 USD | 0.00 USD | `+43.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `5.99` | 6,780,000.00 USD | 119,340.00 USD | 0.00 USD | `+43.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.00` | 6,780,000.00 USD | 3,000.00 USD | 0.00 USD | `+44.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.00` | 6,980,000.00 USD | 200,290.00 USD | 0.00 USD | `+44.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.01` | 7,000,000.00 USD | 13,710.00 USD | 0.00 USD | `+44.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.03` | 7,090,000.00 USD | 90,380.00 USD | 0.00 USD | `+44.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.04` | 7,090,000.00 USD | 2,170.00 USD | 0.00 USD | `+44.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.04` | 7,090,000.00 USD | 3,300.00 USD | 0.00 USD | `+45.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.05` | 7,090,000.00 USD | 1,040.00 USD | 0.00 USD | `+45.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.07` | 7,090,000.00 USD | 425.76 USD | 0.00 USD | `+45.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.08` | 7,090,000.00 USD | 2,030.00 USD | 0.00 USD | `+45.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.08` | 7,100,000.00 USD | 4,120.00 USD | 0.00 USD | `+46.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.09` | 7,100,000.00 USD | 2,000.00 USD | 0.00 USD | `+46.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.11` | 7,160,000.00 USD | 61,050.00 USD | 0.00 USD | `+46.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.12` | 7,160,000.00 USD | 1,610.00 USD | 0.00 USD | `+46.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.13` | 7,160,000.00 USD | 1,200.00 USD | 0.00 USD | `+47.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.14` | 7,160,000.00 USD | 420.32 USD | 0.00 USD | `+47.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.16` | 7,170,000.00 USD | 1,940.00 USD | 0.00 USD | `+47.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.17` | 7,170,000.00 USD | 4,010.00 USD | 0.00 USD | `+48.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.18` | 7,170,000.00 USD | 3,960.00 USD | 0.00 USD | `+48.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.21` | 7,240,000.00 USD | 66,060.00 USD | 0.00 USD | `+49.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.21` | 7,240,000.00 USD | 1,890.00 USD | 0.00 USD | `+49.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.22` | 7,240,000.00 USD | 195.46 USD | 0.00 USD | `+49.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.24` | 7,240,000.00 USD | 1,540.00 USD | 0.00 USD | `+49.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.25` | 7,240,000.00 USD | 116.16 USD | 0.00 USD | `+50.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.30` | 7,250,000.00 USD | 7,310.00 USD | 0.00 USD | `+51.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.32` | 7,250,000.00 USD | 310.70 USD | 0.00 USD | `+51.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.33` | 7,250,000.00 USD | 325.62 USD | 0.00 USD | `+52.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.36` | 7,250,000.00 USD | 1,760.00 USD | 0.00 USD | `+52.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.39` | 7,260,000.00 USD | 3,230.00 USD | 0.00 USD | `+53.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.41` | 7,260,000.00 USD | 5,120.00 USD | 0.00 USD | `+53.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.50` | 7,260,000.00 USD | 1,310.00 USD | 0.00 USD | `+56.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.50` | 7,300,000.00 USD | 30,990.00 USD | 0.00 USD | `+56.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.51` | 7,300,000.00 USD | 104.24 USD | 0.00 USD | `+56.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.54` | 7,310,000.00 USD | 13,580.00 USD | 0.00 USD | `+57.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.58` | 7,310,000.00 USD | 1,630.00 USD | 0.00 USD | `+58.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.59` | 7,310,000.00 USD | 1,370.00 USD | 0.00 USD | `+58.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.61` | 7,320,000.00 USD | 5,400.00 USD | 0.00 USD | `+58.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.62` | 7,320,000.00 USD | 1,620.00 USD | 0.00 USD | `+58.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.64` | 7,320,000.00 USD | 3,220.00 USD | 0.00 USD | `+59.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.67` | 7,320,000.00 USD | 450.55 USD | 0.00 USD | `+60.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.67` | 7,330,000.00 USD | 3,060.00 USD | 0.00 USD | `+60.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.71` | 7,330,000.00 USD | 3,070.00 USD | 0.00 USD | `+61.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.74` | 7,330,000.00 USD | 3,120.00 USD | 0.00 USD | `+61.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.75` | 7,330,000.00 USD | 1,550.00 USD | 0.00 USD | `+62.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.78` | 7,340,000.00 USD | 3,080.00 USD | 0.00 USD | `+62.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.79` | 7,340,000.00 USD | 647.56 USD | 0.00 USD | `+63.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.80` | 7,340,000.00 USD | 1,420.00 USD | 0.00 USD | `+63.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.82` | 7,340,000.00 USD | 2,130.00 USD | 0.00 USD | `+63.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.83` | 7,350,000.00 USD | 6,870.00 USD | 0.00 USD | `+63.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.84` | 7,350,000.00 USD | 342.25 USD | 0.00 USD | `+64.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.87` | 7,350,000.00 USD | 2,990.00 USD | 0.00 USD | `+64.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.89` | 7,350,000.00 USD | 2,970.00 USD | 0.00 USD | `+65.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.91` | 7,350,000.00 USD | 324.54 USD | 0.00 USD | `+65.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.95` | 7,350,000.00 USD | 504.21 USD | 0.00 USD | `+66.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.97` | 7,350,000.00 USD | 166.00 USD | 0.00 USD | `+67.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `6.99` | 7,360,000.00 USD | 4,190.00 USD | 0.00 USD | `+67.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.00` | 7,370,000.00 USD | 12,970.00 USD | 0.00 USD | `+68.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.04` | 7,370,000.00 USD | 2,860.00 USD | 0.00 USD | `+69.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.11` | 7,370,000.00 USD | 264.31 USD | 0.00 USD | `+70.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.13` | 7,380,000.00 USD | 599.34 USD | 0.00 USD | `+71.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.16` | 7,380,000.00 USD | 193.19 USD | 0.00 USD | `+71.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.18` | 7,380,000.00 USD | 3,950.00 USD | 0.00 USD | `+72.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.21` | 7,380,000.00 USD | 1,940.00 USD | 0.00 USD | `+73.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.25` | 7,540,000.00 USD | 160,550.00 USD | 0.00 USD | `+74.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.28` | 7,540,000.00 USD | 1,290.00 USD | 0.00 USD | `+74.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.32` | 7,540,000.00 USD | 1,180.00 USD | 0.00 USD | `+75.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.39` | 7,550,000.00 USD | 630.05 USD | 0.00 USD | `+77.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.41` | 7,550,000.00 USD | 1,410.00 USD | 0.00 USD | `+77.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.42` | 7,550,000.00 USD | 2,610.00 USD | 0.00 USD | `+78.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.50` | 7,560,000.00 USD | 7,630.00 USD | 0.00 USD | `+80.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.58` | 7,560,000.00 USD | 4,640.00 USD | 0.00 USD | `+81.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.61` | 7,560,000.00 USD | 371.88 USD | 0.00 USD | `+82.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.62` | 7,560,000.00 USD | 2,510.00 USD | 0.00 USD | `+82.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.67` | 7,560,000.00 USD | 380.68 USD | 0.00 USD | `+84.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.78` | 7,570,000.00 USD | 1,470.00 USD | 0.00 USD | `+86.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.79` | 7,580,000.00 USD | 11,170.00 USD | 0.00 USD | `+87.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.80` | 7,610,000.00 USD | 34,360.00 USD | 0.00 USD | `+87.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.82` | 7,610,000.00 USD | 253.21 USD | 0.00 USD | `+87.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.83` | 7,610,000.00 USD | 100.29 USD | 0.00 USD | `+88.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.96` | 7,620,000.00 USD | 10,610.00 USD | 0.00 USD | `+91.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `7.97` | 7,620,000.00 USD | 309.43 USD | 0.00 USD | `+91.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.01` | 7,660,000.00 USD | 36,300.00 USD | 0.00 USD | `+92.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.03` | 7,740,000.00 USD | 81,310.00 USD | 0.00 USD | `+92.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.12` | 7,740,000.00 USD | 1,390.00 USD | 0.00 USD | `+95.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.19` | 7,740,000.00 USD | 216.90 USD | 0.00 USD | `+96.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.21` | 7,750,000.00 USD | 7,200.00 USD | 0.00 USD | `+97.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.32` | 7,750,000.00 USD | 1,350.00 USD | 0.00 USD | `+99.96%` | `TACTICAL (Retail Cluster)` |

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
  * Total Open Interest: `1.08B` | Total OI Tokens: `260,552,737.2 NEAR`
  * 1h OI Change: `+0.84%` | 4h OI Change: `-4.10%` | 24h OI Change: `-14.49%`
  * Exchange Breakdown: Binance=`204.98M` | Bybit=`146.17M` | OKX=`50.49M` | Hyperliquid=`235.07M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `-32.38K` | Last 24h: `59.84K` | Last 3d: `308.79K` | Last 7d: `236.18K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `-0.0009%` | **USDT OKX** | `-0.0207%` |
| **USDT Bybit** | `-0.0174%` | **USDT KuCoin** | `0.0100%` |
| **USDT MEXC** | `-0.0007%` | **USDT BingX** | `0.0041%` |
| **USDT Gate** | `-0.0626%` | **USDT Bitget** | `-0.0130%` |
| **CoinM Binance** | `0.0100%` | **CoinM OKX** | `-` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `NEAR` | `46.15%` | `53.85%` | `0.86` | 12,960,000.00 USD |
| `15M` | `Binance` | `45.5%` | `54.5%` | `0.83` | 6,240,000.00 USD |
| `15M` | `OKX` | `48.75%` | `51.25%` | `0.95` | 1,840,000.00 USD |
| `15M` | `Bybit` | `48.41%` | `51.59%` | `0.94` | 2,440,000.00 USD |
| `15M` | `KuCoin` | `51.22%` | `48.78%` | `1.05` | 194,930.00 USD |
| `15M` | `Gate` | `34.93%` | `65.07%` | `0.54` | 838,850.00 USD |
| `15M` | `Bitget` | `44%` | `56%` | `0.79` | 623,100.00 USD |
| `15M` | `BingX` | `30.15%` | `69.85%` | `0.43` | 57,050.00 USD |
| `15M` | `MEXC` | `54.23%` | `45.77%` | `1.18` | 115,120.00 USD |
| `15M` | `Bitunix` | `41.8%` | `58.2%` | `0.72` | 183,390.00 USD |
| `15M` | `Hyperliquid` | `62.16%` | `37.84%` | `1.64` | 187,750.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `49.97%` | `50.03%` | `1.00` | 94,020.00 USD |
| `15M` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `WhiteBIT` | `98.64%` | `1.36%` | `72.53` | 22,020.00 USD |
| `15M` | `HTX` | `46.55%` | `53.45%` | `0.87` | 36,470.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Aster` | `68.24%` | `31.76%` | `2.15` | 3,770.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `42.9%` | `57.1%` | `0.75` | 86,450.00 USD |
| `15M` | `Whale Positions` | `45.5%` | `54.5%` | `0.83` | 6,240,000.00 USD |
| `15M` | `Global Accounts` | `46.15%` | `53.85%` | `0.86` | 12,960,000.00 USD |
| `1H` | `NEAR` | `46.81%` | `53.19%` | `0.88` | 17,410,000.00 USD |
| `1H` | `Binance` | `50.49%` | `49.51%` | `1.02` | 6,340,000.00 USD |
| `1H` | `OKX` | `50.38%` | `49.62%` | `1.02` | 883,780.00 USD |
| `1H` | `Bybit` | `51.58%` | `48.42%` | `1.07` | 1,540,000.00 USD |
| `1H` | `KuCoin` | `64.14%` | `35.86%` | `1.79` | 145,530.00 USD |
| `1H` | `Gate` | `39.98%` | `60.02%` | `0.67` | 466,380.00 USD |
| `1H` | `Bitget` | `50.06%` | `49.94%` | `1.00` | 308,130.00 USD |
| `1H` | `BingX` | `44.23%` | `55.77%` | `0.79` | 2,870,000.00 USD |
| `1H` | `MEXC` | `41.05%` | `58.95%` | `0.70` | 515,130.00 USD |
| `1H` | `Bitunix` | `44.24%` | `55.76%` | `0.79` | 503,180.00 USD |
| `1H` | `Hyperliquid` | `34.51%` | `65.49%` | `0.53` | 414,570.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `43.15%` | `56.85%` | `0.76` | 3,200,000.00 USD |
| `1H` | `Crypto.com` | `11.69%` | `88.31%` | `0.13` | 222.05 USD |
| `1H` | `WhiteBIT` | `18.55%` | `81.45%` | `0.23` | 123,480.00 USD |
| `1H` | `HTX` | `57.96%` | `42.04%` | `1.38` | 6,900.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `8.79%` | `91.21%` | `0.10` | 768.06 USD |
| `1H` | `Aster` | `85.81%` | `14.19%` | `6.05` | 2,180.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `20.04%` | `79.96%` | `0.25` | 88,510.00 USD |
| `1H` | `Whale Positions` | `50.49%` | `49.51%` | `1.02` | 6,340,000.00 USD |
| `1H` | `Global Accounts` | `46.81%` | `53.19%` | `0.88` | 17,410,000.00 USD |
| `4H` | `NEAR` | `49.24%` | `50.76%` | `0.97` | 211,220,000.00 USD |
| `4H` | `Binance` | `51.23%` | `48.77%` | `1.05` | 92,120,000.00 USD |
| `4H` | `OKX` | `48.92%` | `51.08%` | `0.96` | 26,740,000.00 USD |
| `4H` | `Bybit` | `50.92%` | `49.08%` | `1.04` | 39,240,000.00 USD |
| `4H` | `KuCoin` | `48.19%` | `51.81%` | `0.93` | 3,590,000.00 USD |
| `4H` | `Gate` | `43.29%` | `56.71%` | `0.76` | 12,060,000.00 USD |
| `4H` | `Bitget` | `48.68%` | `51.32%` | `0.95` | 6,890,000.00 USD |
| `4H` | `BingX` | `34.35%` | `65.65%` | `0.52` | 2,040,000.00 USD |
| `4H` | `MEXC` | `46.87%` | `53.13%` | `0.88` | 4,030,000.00 USD |
| `4H` | `Bitunix` | `48.64%` | `51.36%` | `0.95` | 3,410,000.00 USD |
| `4H` | `Hyperliquid` | `54.07%` | `45.93%` | `1.18` | 7,920,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `49.3%` | `50.7%` | `0.97` | 3,490,000.00 USD |
| `4H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `WhiteBIT` | `21.12%` | `78.88%` | `0.27` | 4,820,000.00 USD |
| `4H` | `HTX` | `45.72%` | `54.28%` | `0.84` | 785,600.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `47.07%` | `52.93%` | `0.89` | 2,470,000.00 USD |
| `4H` | `Aster` | `23.97%` | `76.03%` | `0.32` | 603,620.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `51.3%` | `48.7%` | `1.05` | 1,030,000.00 USD |
| `4H` | `Whale Positions` | `51.23%` | `48.77%` | `1.05` | 92,120,000.00 USD |
| `4H` | `Global Accounts` | `49.24%` | `50.76%` | `0.97` | 211,220,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5:00 UTC` | `3.99` | `3.99` | `3.99` | `4.01` | `3.97` | 6,380,993.73 USD | 2,663,458.31 USD | 3,717,535.41 USD | -1,054,077.10 USD | `-16.52%` | `2B / 11S` |
| `0:00 UTC` | `4.03` | `4.01` | `4.03` | `4.04` | `3.97` | 7,316,250.26 USD | 4,215,105.63 USD | 3,101,144.64 USD | 1,113,960.99 USD | `+15.23%` | `9B / 6S` |
| `5:00 UTC` | `4.06` | `4.05` | `4.06` | `4.08` | `4.02` | 8,251,415.10 USD | 5,342,802.98 USD | 2,908,612.12 USD | 2,434,190.86 USD | `+29.50%` | `19B / 0S` |
| `0:00 UTC` | `4.10` | `4.09` | `4.10` | `4.11` | `4.07` | 8,076,911.53 USD | 4,345,296.52 USD | 3,731,615.01 USD | 613,681.51 USD | `+7.60%` | `5B / 1S` |
| `5:00 UTC` | `4.06` | `4.07` | `4.06` | `4.10` | `4.05` | 6,914,413.13 USD | 3,114,711.21 USD | 3,799,701.92 USD | -684,990.71 USD | `-9.91%` | `2B / 8S` |
| `0:00 UTC` | `4.08` | `4.08` | `4.08` | `4.09` | `4.06` | 5,392,588.64 USD | 3,075,595.58 USD | 2,316,993.06 USD | 758,602.52 USD | `+14.07%` | `1B / 1S` |
| `5:00 UTC` | `4.07` | `4.08` | `4.07` | `4.11` | `4.07` | 4,324,346.41 USD | 2,642,977.58 USD | 1,681,368.84 USD | 961,608.74 USD | `+22.24%` | `17B / 1S` |
| `0:00 UTC` | `4.14` | `4.13` | `4.14` | `4.16` | `4.10` | 9,990,039.56 USD | 5,818,620.01 USD | 4,171,419.55 USD | 1,647,200.46 USD | `+16.49%` | `10B / 2S` |
| `5:00 UTC` | `4.15` | `4.15` | `4.15` | `4.17` | `4.14` | 5,034,918.87 USD | 2,878,643.09 USD | 2,156,275.78 USD | 722,367.31 USD | `+14.35%` | `2B / 1S` |
| `0:00 UTC` | `4.16` | `4.16` | `4.16` | `4.16` | `4.16` | 166,365.65 USD | 11,654.46 USD | 154,711.19 USD | -143,056.72 USD | `-85.99%` | `0B / 6S` |

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
| `5m` | -117,050.00 USD | 322,020.00 USD | **`ACCUMULATION`** |
| `15m` | 512,260.00 USD | 1,220,000.00 USD | **`ACCUMULATION`** |
| `30m` | 2,410,000.00 USD | 3,770,000.00 USD | **`ACCUMULATION`** |
| `1h` | 3,520,000.00 USD | 7,590,000.00 USD | **`ACCUMULATION`** |
| `2h` | 6,100,000.00 USD | 16,350,000.00 USD | **`ACCUMULATION`** |
| `4h` | 3,940,000.00 USD | 3,050,000.00 USD | **`ACCUMULATION`** |
| `6h` | -1,160,000.00 USD | -4,170,000.00 USD | **`DISTRIBUTION`** |
| `8h` | -6,610,000.00 USD | -13,930,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -14,640,000.00 USD | -31,280,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -14,260,000.00 USD | -53,620,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -77,310,000.00 USD | -126,850,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -244,350,000.00 USD | -675,990,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-117.05K` | 15m=`+512.26K` | 1h=`+3.52M` | 24h=`-14.26M`
* Futures Capital Netflows: 5m=`+322.02K` | 15m=`+1.22M` | 1h=`+7.59M` | 24h=`-53.62M`
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
  * `2026-10-30 09:09:56 IST`: [forex.com] - (Sentiment: `Neutral`)
  * `2026-10-30 08:33:56 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 08:32:56 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 09:28:56 IST`: [financemagnates.com] - (Sentiment: `Neutral`)
  * `2026-10-30 09:27:56 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-30 09:27:56 IST`: [kathleenhays.substack.com] - (Sentiment: `Neutral`)
  * `2026-10-30 06:29:56 IST`: [rba.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 06:29:56 IST`: [abs.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 06:29:56 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 05:29:56 IST`: [@NodeWire] - (Sentiment: `Neutral`)
  * `2026-10-30 05:29:56 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 05:29:56 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 05:29:56 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-30 05:29:56 IST`: [media.rabobank.com] - (Sentiment: `Neutral`)
  * `2026-10-30 04:29:56 IST`: [economics.td.com] - (Sentiment: `Neutral`)


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
  * Execution Entry: `3.95` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `3.84` (Risk Distance: `0.1093` pts)
  * +2.5R Take Profit: `4.23`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `4.13` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `4.24` (Risk Distance: `0.1093` pts)
  * +2.5R Take Profit: `3.86`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`4.17`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
